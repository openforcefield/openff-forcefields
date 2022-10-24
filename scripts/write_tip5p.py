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

dataframe = pandas.read_csv("openforcefields/data/jc.csv")

tip5p = ForceField()

tip5p_electrostatics = ElectrostaticsHandler(version=0.4)
tip5p_library = LibraryChargeHandler(version=0.3)
tip5p_vdw = vdWHandler(version=0.3)
tip5p_constraints = ConstraintHandler(version=0.3)
tip5p_virtual_sites = VirtualSiteHandler(version=0.3)

tip5p_vdw = vdWHandler(version=0.3)
tip5p_vdw.add_parameter(
    {
        "smirks": "[#1]-[#8X2H2+0:1]-[#1]",
        "epsilon": unit.Quantity(0.66944, unit.kilocalorie_per_mole),
        "sigma": unit.Quantity(0.312, unit.nanometer),
        "id": "n-tip5p-O",
    }
)
tip5p_vdw.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1]",
        "epsilon": unit.Quantity(0.0, unit.kilocalorie_per_mole),
        "sigma": unit.Quantity(1.0, unit.angstrom),
        "id": "n-tip5p-H",
    }
)

tip5p_library = LibraryChargeHandler(version=0.3)
tip5p_library.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0:2]-[#1:3]",
        "name": "TIP5P",
        "charge1": unit.Quantity(0.0, unit.elementary_charge),
        "charge2": unit.Quantity(0.0, unit.elementary_charge),
        "charge3": unit.Quantity(0.0, unit.elementary_charge),
    }
)

tip5p_constraints = ConstraintHandler(version=0.3)
tip5p_constraints.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0:2]-[#1]",
        "id": "c-tip5p-H-O",
        "distance": unit.Quantity(0.9572, unit.angstrom),
    }
)
tip5p_constraints.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1:2]",
        "id": "c-tip5p-H-O-H",
        "distance": unit.Quantity(1.5139006545247014, unit.angstrom),
    }
)

tip5p_virtual_sites.add_parameter(
    {
        "type": "DivalentLonePair",
        "smirks": "[#1:2]-[#8X2H2+0:1]-[#1:3]",
        "match": "all_permutations",
        "name": "EP",
        "distance": unit.Quantity(0.15, unit.angstrom),
        "sigma": unit.Quantity(1.0, unit.angstrom),
        "epsilon": unit.Quantity(0.0, unit.kilocalories_per_mole),
        "outOfPlaneAngle": unit.Quantity(54.71384225, unit.degree),
        "charge_increment1": unit.Quantity(0.0, unit.elementary_charge),
        "charge_increment2": unit.Quantity(0.1205, unit.elementary_charge),
        "charge_increment3": unit.Quantity(0.1205, unit.elementary_charge),
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

tip5p.to_file("tip5p.offxml")
