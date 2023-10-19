"""
Write TIP5P parameters into a SMIRNOFF force field. Based on
https://docs.lammps.org/Howto_tip5p.html
"""
from pathlib import Path

from openff.toolkit.typing.engines.smirnoff.forcefield import ForceField
from openff.toolkit.typing.engines.smirnoff.parameters import (
    ConstraintHandler,
    ElectrostaticsHandler,
    LibraryChargeHandler,
    VirtualSiteHandler,
    vdWHandler,
)
from openff.units import unit
from packaging import version

VERSION = version.Version("1.0.0")
OFFXML_PATH = Path("openforcefields", "offxml")

tip5p = ForceField()

tip5p_electrostatics = ElectrostaticsHandler(version=0.4, scale14=0.8333333333)
tip5p_library = LibraryChargeHandler(version=0.3)
tip5p_vdw = vdWHandler(version=0.4)
tip5p_constraints = ConstraintHandler(version=0.3)
tip5p_virtual_sites = VirtualSiteHandler(version=0.3)

tip5p_vdw.add_parameter(
    {
        "smirks": "[#1]-[#8X2H2+0:1]-[#1]",
        "epsilon": unit.Quantity(0.16, unit.kilocalorie_per_mole),
        "sigma": unit.Quantity(0.312, unit.nanometer),
        "id": "n-tip5p-O",
    }
)
tip5p_vdw.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1]",
        "epsilon": unit.Quantity(0.0, unit.kilocalorie_per_mole),
        "sigma": unit.Quantity(1.0, unit.nanometer),
        "id": "n-tip5p-H",
    }
)

tip5p_library.add_parameter(
    {
        "smirks": "[#1]-[#8X2H2+0:1]-[#1]",
        "charge1": unit.Quantity(0.0, unit.elementary_charge),
        "id": "q-tip5p-O",
    }
)
tip5p_library.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1]",
        "charge1": unit.Quantity(0.0, unit.elementary_charge),
        "id": "q-tip5p-H",
    }
)

tip5p_virtual_sites.add_parameter(
    {
        "type": "DivalentLonePair",
        "smirks": "[#1:2]-[#8X2H2+0:1]-[#1:3]",
        "match": "all_permutations",
        "name": "EP",
        "distance": unit.Quantity(0.07, unit.nanometer),
        "sigma": unit.Quantity(10.0, unit.angstrom),
        "epsilon": unit.Quantity(0.0, unit.kilocalorie_per_mole),
        "outOfPlaneAngle": unit.Quantity(54.735, unit.degree),
        "charge_increment1": unit.Quantity(0.0, unit.elementary_charge),
        "charge_increment2": unit.Quantity(0.1205, unit.elementary_charge),
        "charge_increment3": unit.Quantity(0.1205, unit.elementary_charge),
    }
)

tip5p_constraints.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0:2]-[#1]",
        "id": "c-tip5p-H-O",
        "distance": unit.Quantity(0.09572, unit.nanometer),
    }
)
# H-H distance = 2 * 0.09572 * sin(104.52 degrees / 2)
tip5p_constraints.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1:2]",
        "id": "c-tip5p-H-O-H",
        "distance": unit.Quantity(0.15139006545, unit.nanometer),
    }
)


for handler in [
    tip5p_vdw,
    tip5p_library,
    tip5p_electrostatics,
    tip5p_constraints,
    tip5p_virtual_sites,
]:
    tip5p.register_parameter_handler(handler)

tip5p.to_file(Path(OFFXML_PATH, "tip5p.offxml"))
tip5p.to_file(Path(OFFXML_PATH, f"tip5p-{VERSION}.offxml"))
