import sys
from pathlib import Path

import numpy as np
from openforcefield.topology import Molecule
from openmmforcefields.generators import SystemGenerator
from pkg_resources import resource_filename
from simtk import openmm, unit
from simtk.openmm import app

DATA_PATH = Path(resource_filename("openforcefields", "../canary/data/")).resolve()

coverage_mols = DATA_PATH / "coverage.smi"
propyne_mols = DATA_PATH / "propynes.smi"


class NANEnergyError(Exception):
    """Base exception for a system with NaN-like potential energy"""


class CanaryError(Exception):
    """Base exception for canary"""

    def __init__(self, message, runs):
        super(CanaryError, self).__init__(message)
        self.message = message
        self.runs = runs

    def __str__(self):
        return self.message + "\n" + "\n".join(["\t".join(run) for run in self.runs])


class HMRCanaryError(CanaryError):
    """Exception for an HMR canary test failing"""


def hmr_driver(mol, ff_name):
    """Given an OpenFF Molecule, run a short 4 fs HMR simulation. This function is adapted from
    https://github.com/openforcefield/openforcefields/issues/19#issuecomment-689816995"""
    print(
        f"Running HMR with force field {ff_name} and molecule with SMILES {mol.to_smiles()}"
    )

    forcefield_kwargs = {
        "constraints": app.HBonds,
        "rigidWater": True,
        "removeCMMotion": False,
        "hydrogenMass": 4
        * unit.amu,  # Does this also _subtract_ mass from heavy atoms?:w
    }

    system_generator = SystemGenerator(
        small_molecule_forcefield=ff_name,
        forcefield_kwargs=forcefield_kwargs,
        molecules=mol,
    )
    system = system_generator.create_system(mol.to_topology().to_openmm())

    temperature = 300 * unit.kelvin
    collision_rate = 1.0 / unit.picoseconds
    timestep = 4.0 * unit.femtoseconds

    integrator = openmm.LangevinIntegrator(temperature, collision_rate, timestep)
    context = openmm.Context(system, integrator)
    mol.generate_conformers(n_conformers=1)
    context.setPositions(mol.conformers[0])

    # Run for 10 ps
    integrator.step(2500)

    state = context.getState(getEnergy=True)
    pot = state.getPotentialEnergy()
    # OpenMM will silenty "fail" if energies aren't explicitly checked
    if np.isnan(pot / pot.unit):
        raise NANEnergyError()


if __name__ == "__main__":
    """This function expects to be called with a list of OFFXML files passed to it,
    i.e. piped from git diff upstream/master  --name-only"""
    # Read force field filenames from stdin
    failed_runs = []
    for line in sys.stdin:
        if "_unconstrained" in line:
            continue
        ff_name = line.split("/")[-1][:-8]
        # Molecule.from_file fails on pathlib.Path ojects, despite being str-like
        hmr_mols = Molecule.from_file(
            str(propyne_mols),
            file_format="smi",
            allow_undefined_stereo=True,
        )
        # Append coverage set, with known failures stripped out
        hmr_mols += Molecule.from_file(
            str(coverage_mols),
            file_format="smi",
            allow_undefined_stereo=True,
        )
        for mol in hmr_mols:
            try:
                hmr_driver(mol, ff_name)
            except NANEnergyError:
                failed_runs.append([mol.to_smiles(), ff_name, "NaN energy"])
            except Exception:
                # OpenMM's OpenMMException cannot be caught as it does not
                # inherit from BaseException; therefore this clause may
                # hit other errors than NaN positions
                failed_runs.append([mol.to_smiles(), ff_name, "NaN position(s)"])

    if len(failed_runs) > 0:
        raise HMRCanaryError("HMR tests failed:", failed_runs)
