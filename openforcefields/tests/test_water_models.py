from typing import Dict

import openmm
import openmm.unit
import pytest
from openff.interchange.interop.openmm import to_openmm_topology
from openff.toolkit import ForceField, Molecule, Topology
from openmm.app import ForceField as OpenMMForceField
from openmm.app import HAngles
from openmm.app import Topology as OpenMMTopology

from openforcefields.tests.compare import _compare


@pytest.fixture
def water_molecule() -> Topology:
    molecule = Molecule.from_mapped_smiles("[H:2][O:1][H:3]")
    molecule.generate_conformers(n_conformers=1)
    return molecule.to_topology()


def compare_water_systems(
    reference: openmm.System,
    system: openmm.System,
    tolerances: Dict[str, openmm.unit.Quantity],
):
    # OpenMM creates bond and angle forces despite each containing 0 parameters
    for index, force in enumerate(reference.getForces()):
        if isinstance(force, openmm.HarmonicBondForce):
            assert force.getNumBonds() == 0
            bond_force: int = index

    reference.removeForce(bond_force)

    for index, force in enumerate(reference.getForces()):
        if isinstance(force, openmm.HarmonicAngleForce):
            assert force.getNumAngles() == 0
            angle_force: int = index

    reference.removeForce(angle_force)

    for index, force in enumerate(reference.getForces()):
        if isinstance(force, openmm.CMMotionRemover):
            cmm_force: int = index

    reference.removeForce(cmm_force)

    _compare(reference, system, tolerances)


def test_tip3p(water_molecule):
    reference = OpenMMForceField("tip3p.xml").createSystem(
        water_molecule.to_openmm(),
        constraints=HAngles,
        rigidWater=True,
    )

    system = ForceField("tip3p-1.0.0.offxml").create_openmm_system(
        water_molecule,
    )

    compare_water_systems(
        reference,
        system,
        {
            "charge": 1e-10 * openmm.unit.elementary_charge,
            "sigma": 5.3e-6 * openmm.unit.nanometer,
            "epsilon": 4.185e-4 * openmm.unit.kilojoule_per_mole,
        },
    )


def test_tip3p_fb(water_molecule):
    reference = OpenMMForceField("tip3pfb.xml").createSystem(
        water_molecule.to_openmm(),
        constraints=HAngles,
        rigidWater=True,
    )

    system = ForceField("tip3p_fb-1.0.0.offxml").create_openmm_system(
        water_molecule,
    )

    compare_water_systems(
        reference,
        system,
        {
            "charge": 1e-10 * openmm.unit.elementary_charge,
            "sigma": 1e-10 * openmm.unit.nanometer,
            "epsilon": 1e-10 * openmm.unit.kilojoule_per_mole,
        },
    )


@pytest.mark.skip(reason="Skipping in first pass")
def test_tip4p_ew(water_molecule):
    interchange = ForceField("tip4p-ew_1.0.0.offxml").create_interchange(
        water_molecule,
    )

    openmm_topology = to_openmm_topology(interchange)

    reference = OpenMMForceField("tip4pew.xml").createSystem(
        openmm_topology,
        constraints=HAngles,
        rigidWater=True,
    )

    compare_water_systems(
        reference, interchange.to_openmm(combine_nonbonded_forces=True)
    )


@pytest.mark.skip(reason="Skipping in first pass")
def test_tip5p(water_molecule):
    interchange = ForceField("tip5p_1.0.0.offxml").create_openmm_system(
        water_molecule,
    )

    openmm_topology = to_openmm_topology(interchange)

    reference = OpenMMForceField("tip5p.xml").createSystem(
        openmm_topology,
        constraints=HAngles,
        rigidWater=True,
    )

    compare_water_systems(
        reference, interchange.to_openmm(combine_nonbonded_forces=True)
    )


@pytest.mark.parametrize(
    "water_model,pattern",
    [("tip3p", "^tip3p(?!.*fb)"), ("tip3p_fb", "^tip3p_fb")],
)
def test_most_recent_version_match(water_model, pattern):
    import re

    from openff.toolkit.typing.engines.smirnoff.forcefield import (
        get_available_force_fields,
    )
    from packaging import version

    maximum_version = version.Version("0.0.0")

    matched_files = list(
        filter(lambda x: re.match(pattern, x) is not None, get_available_force_fields())
    )

    assert len(matched_files) > 0, f"Failed to match any files for pattern {pattern}!"

    for file in matched_files:
        split = re.split(pattern + "-", file.strip(".offxml"))

        if len(split) == 2:
            found_verison = version.Version(split[1])
            if found_verison > maximum_version:
                maximum_version = found_verison

    assert maximum_version > version.Version(
        "0.0.0"
    ), f"failed to update version of {water_model}"

    maximum_version_file = f"{water_model}-{maximum_version}.offxml"
    shorthand_file = f"{water_model}.offxml"

    assert hash(ForceField(maximum_version_file)) == hash(ForceField(shorthand_file))


def test_ion_parameter_assignment(water_molecule):
    """Make sure that the ion parameters are assigned properly"""
    ff = ForceField("tip3p.offxml")

    ion_vdw_params_used = {}
    for parameter in ff["vdW"]:
        # assume that all parameters with "X0" in their smirks should be tested here
        if "X0" in parameter.smirks:
            ion_vdw_params_used[parameter.smirks] = False

    ion_librarycharge_params_used = {}
    for parameter in ff["LibraryCharges"]:
        if "X0" in parameter.smirks:
            ion_librarycharge_params_used[parameter.smirks] = False

    off_top = Topology.from_molecules(
        [
            Molecule.from_smiles("[Li+]"),
            Molecule.from_smiles("[Na+]"),
            Molecule.from_smiles("[K+]"),
            Molecule.from_smiles("[Rb+]"),
            Molecule.from_smiles("[Cs+]"),
            Molecule.from_smiles("[F-]"),
            Molecule.from_smiles("[Cl-]"),
            Molecule.from_smiles("[Br-]"),
            Molecule.from_smiles("[I-]"),
        ]
    )
    system = ff.create_openmm_system(off_top)

    nbf = [
        force for force in system.getForces() if type(force) is openmm.NonbondedForce
    ][0]

    sigma_tol = 1e-10 * openmm.unit.nanometer
    eps_tol = 1e-10 * openmm.unit.kilojoule_per_mole
    charge_tol = 1e-10 * openmm.unit.elementary_charge

    # Loop over each atom and ensure that the appropriate parameters were assigned
    # to it by directly matching to the atomic number in the parameter smirks.
    for atom in off_top.atoms:
        topology_atom_index = off_top.atom_index(atom)
        for vdw_parameter in ff["vdW"].parameters:
            if f"#{atom.atomic_number}X0" in vdw_parameter.smirks:

                (
                    assigned_charge,
                    assigned_sigma,
                    assigned_epsilon,
                ) = nbf.getParticleParameters(topology_atom_index)

                expected_epsilon = vdw_parameter.epsilon.to_openmm()
                assert abs(expected_epsilon - assigned_epsilon) < eps_tol

                expected_sigma = vdw_parameter.sigma.to_openmm()
                assert abs(expected_sigma - assigned_sigma) < sigma_tol
                ion_vdw_params_used[vdw_parameter.smirks] = True

                lc_parameter = ff["LibraryCharges"][vdw_parameter.smirks]
                expected_charge = lc_parameter.charge[0].to_openmm()
                assert abs(expected_charge - assigned_charge) < charge_tol
                ion_librarycharge_params_used[vdw_parameter.smirks] = True

    # Ensure that this test covered all the ion parameters
    for key, parameter_was_used in ion_vdw_params_used.items():
        assert (
            parameter_was_used
        ), f"The ion vdW parameter with smirks {key} was not assigned"

    for key, parameter_was_used in ion_librarycharge_params_used.items():
        assert (
            parameter_was_used
        ), f"The ion LibraryCharge parameter with smirks {key} was not assigned"

def test_water_model_is_compatible_with_mainline():
    """Ensure that the latest water model FF is compatible with the latest main-line FF"""
    # Since we don't have a way to get the most recent mainline FF, be sure
    # to occasionally update the first FF listed here
    ForceField('openff-2.0.0.offxml', 'tip3p.offxml')
    ForceField('openff-2.0.0.offxml', 'tip3p_fb.offxml')