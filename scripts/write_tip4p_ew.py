"""
Write TIP3P-EW parameters into a SMIRNOFF force field. Based on
https://github.com/openmm/openmm/blob/116aed3927066b0a53eba929110d73f3daew64bd/wrappers/python/openmm/app/data/tip4pew.xml
"""
from pathlib import Path

import pandas
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

tip4p_ew = ForceField()

tip4p_ew_electrostatics = ElectrostaticsHandler(version=0.4, scale14=0.8333333333)
tip4p_ew_library = LibraryChargeHandler(version=0.3)
tip4p_ew_vdw = vdWHandler(version=0.4)
tip4p_ew_constraints = ConstraintHandler(version=0.3)
tip4p_ew_virtual_sites = VirtualSiteHandler(version=0.3)

tip4p_ew_vdw.add_parameter(
    {
        "smirks": "[#1]-[#8X2H2+0:1]-[#1]",
        "epsilon": unit.Quantity(0.680946, unit.kilojoule_per_mole),
        "sigma": unit.Quantity(0.316435, unit.nanometer),
        "id": "n-tip4p-ew-O",
    }
)
tip4p_ew_vdw.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1]",
        "epsilon": unit.Quantity(0.0, unit.kilocalorie_per_mole),
        "sigma": unit.Quantity(1.0, unit.nanometer),
        "id": "n-tip4p-ew-H",
    }
)

tip4p_ew_library.add_parameter(
    {
        "smirks": "[#1]-[#8X2H2+0:1]-[#1]",
        "charge1": unit.Quantity(0.0, unit.elementary_charge),
        "id": "q-tip4p-ew-O",
    }
)
tip4p_ew_library.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1]",
        "charge1": unit.Quantity(0.0, unit.elementary_charge),
        "id": "q-tip4p-ew-H",
    }
)

# Virtual site distance = 0.08984267127345 * 2 * 0.09572 * cos(1.82421813418 / 2)
tip4p_ew_virtual_sites.add_parameter(
    {
        "type": "DivalentLonePair",
        "smirks": "[#1:2]-[#8X2H2+0:1]-[#1:3]",
        "match": "once",
        "name": "EP",
        "distance": unit.Quantity(-0.0125, unit.nanometer),
        "sigma": unit.Quantity(1.0, unit.angstrom),
        "epsilon": unit.Quantity(0.0, unit.kilocalorie_per_mole),
        "outOfPlaneAngle": unit.Quantity(0.0, unit.degree),
        "charge_increment1": unit.Quantity(0.0, unit.elementary_charge),
        "charge_increment2": unit.Quantity(0.52422, unit.elementary_charge),
        "charge_increment3": unit.Quantity(0.52422, unit.elementary_charge),
    }
)

tip4p_ew_constraints.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0:2]-[#1]",
        "id": "c-tip4p-ew-H-O",
        "distance": unit.Quantity(0.09572, unit.nanometer),
    }
)
# H-H distance = 2 * 0.09572 * sin(1.82421813418 / 2)
tip4p_ew_constraints.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1:2]",
        "id": "c-tip4p-ew-H-O-H",
        "distance": unit.Quantity(0.15139006545247014, unit.nanometer),
    }
)

for handler in [
    tip4p_ew_vdw,
    tip4p_ew_library,
    tip4p_ew_electrostatics,
    tip4p_ew_constraints,
    tip4p_ew_virtual_sites,
]:
    tip4p_ew.register_parameter_handler(handler)

tip4p_ew.to_file(Path(OFFXML_PATH, "tip4p_ew.offxml"))
tip4p_ew.to_file(Path(OFFXML_PATH, f"tip4p_ew-{VERSION}.offxml"))
