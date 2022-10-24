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

tip4p = ForceField()

tip4p_electrostatics = ElectrostaticsHandler(version=0.4)
tip4p_library = LibraryChargeHandler(version=0.3)
tip4p_vdw = vdWHandler(version=0.3)
tip4p_constraints = ConstraintHandler(version=0.3)
tip4p_virtual_sites = VirtualSiteHandler(version=0.3)

tip4p_vdw = vdWHandler(version=0.3)
tip4p_vdw.add_parameter(
    {
        "smirks": "[#1]-[#8X2H2+0:1]-[#1]",
        "epsilon": unit.Quantity(6.80946e-01, unit.kilocalorie_per_mole),
        "sigma": unit.Quantity(3.16435e-01, unit.nanometer),
        "id": "n-tip4p-ew-O",
    }
)
tip4p_vdw.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1]",
        "epsilon": unit.Quantity(0.0, unit.kilocalorie_per_mole),
        "sigma": unit.Quantity(1.0, unit.angstrom),
        "id": "n-tip4p-ew-H",
    }
)

tip4p_library = LibraryChargeHandler(version=0.3)
tip4p_library.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0:2]-[#1:3]",
        "name": "TIP5P",
        "charge1": unit.Quantity(0.0, unit.elementary_charge),
        "charge2": unit.Quantity(0.0, unit.elementary_charge),
        "charge3": unit.Quantity(0.0, unit.elementary_charge),
    }
)

for _, row in dataframe.iterrows():
    smirks = f"[{row['element']}1:1]"
    tip4p_vdw.add_parameter(
        {
            "smirks": smirks,
            "rmin_half": unit.Quantity(
                row["tip4pew_rmin2 (A)"],
                unit.angstrom,
            ),
            "epsilon": unit.Quantity(
                row["tip4pew_eps (kcal/mol)"],
                unit.kilocalorie_per_mole,
            ),
        }
    )

    tip4p_library.add_parameter(
        {
            "smirks": smirks,
            "charge1": unit.Quantity(
                int(row["element"][-1] + "1"), unit.elementary_charge
            ),
        }
    )

tip4p_constraints = ConstraintHandler(version=0.3)
tip4p_constraints.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0:2]-[#1]",
        "id": "c-tip4p-ew-H-O",
        "distance": unit.Quantity(0.9572, unit.angstrom),
    }
)
tip4p_constraints.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1:2]",
        "id": "c-tip4p-ew-H-O-H",
        "distance": unit.Quantity(1.5139006545247014, unit.angstrom),
    }
)

tip4p_virtual_sites.add_parameter(
    {
        "type": "DivalentLonePair",
        "smirks": "[#1:2]-[#8X2H2+0:1]-[#1:3]",
        "match": "once",
        "name": "EP",
        "distance": unit.Quantity(-0.125, unit.angstrom),
        "sigma": unit.Quantity(1.0, unit.angstrom),
        "epsilon": unit.Quantity(0.0, unit.kilocalories_per_mole),
        "outOfPlaneAngle": unit.Quantity(0.0, unit.degree),
        "charge_increment1": unit.Quantity(0.0, unit.elementary_charge),
        "charge_increment2": unit.Quantity(0.52422, unit.elementary_charge),
        "charge_increment3": unit.Quantity(0.52422, unit.elementary_charge),
    }
)

for handler in [
    tip4p_vdw,
    tip4p_library,
    tip4p_electrostatics,
    tip4p_constraints,
    tip4p_virtual_sites,
]:
    tip4p.register_parameter_handler(handler)

tip4p.to_file("tip4p-ew.offxml")
