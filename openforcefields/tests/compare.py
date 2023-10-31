from typing import Dict

import openmm
import openmm.unit


def _compare(
    system1: openmm.System,
    system2: openmm.System,
    tolerances: Dict[str, openmm.unit.Quantity],
):
    """Check that two OpenMM systems have the same parameters.

    Adapted from the OpenFF Toolkit:
    https://github.com/openforcefield/openff-toolkit/blob/0.12.0/openff/toolkit/tests/utils.py#L1306-L1403

    Parameters
    ----------
    system1 : openmm.System
        The first system to compare.
    system2 : openmm.System
        The second system to compare.

    """
    assert (
        system1.getNumForces() == system2.getNumForces()
    ), f"{system1.getForces()} != {system2.getForces()}"

    for force in system1.getForces():
        assert type(force) in [openmm.NonbondedForce]

    for force1, force2 in zip(system1.getForces(), system2.getForces()):
        assert type(force1) is type(force2)

        if isinstance(force1, openmm.NonbondedForce):
            _compare_nonbonded_forces(force1, force2, tolerances)


def _compare_nonbonded_forces(
    force1: openmm.NonbondedForce,
    force2: openmm.NonbondedForce,
    tolerances: Dict[str, openmm.unit.Quantity],
):
    assert force1.getNumParticles() == force2.getNumParticles()

    for particle_index in range(force1.getNumParticles()):
        charge1, sigma1, epsilon1 = force1.getParticleParameters(particle_index)
        charge2, sigma2, epsilon2 = force2.getParticleParameters(particle_index)

        assert (
            abs(charge1 - charge2) < tolerances["charge"]
        ), f"{charge1} != {charge2}, {charge1 - charge2}"

        # Water models commonly have zero epsilon and meaningless/inconsistent values
        # of sigma. In this case, do not compare sigma values.
        if epsilon1._value * epsilon2._value != 0.0:
            assert (
                abs(sigma1 - sigma2) < tolerances["sigma"]
            ), f"{sigma1} != {sigma2}, {sigma1 - sigma2}"

        assert (
            abs(epsilon1 - epsilon2) < tolerances["epsilon"]
        ), f"{epsilon1} != {epsilon2}, {epsilon1 - epsilon2}"
