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
    molecule = Molecule.from_smiles("[H:2][O:1][H:3]")
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

    system = ForceField("water/tip3p-1.0.0.offxml").create_openmm_system(
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

    system = ForceField("water/tip3p-fb-1.0.0.offxml").create_openmm_system(
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


def test_tip4p_ew(water_molecule):
    interchange = ForceField("water/tip4p-ew-1.0.0.offxml").create_interchange(
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


def test_tip5p(water_molecule):
    interchange = ForceField("water/tip5p-1.0.0.offxml").create_openmm_system(
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
