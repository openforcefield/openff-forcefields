import pandas
from openff.toolkit.typing.engines.smirnoff.forcefield import ForceField
from openff.toolkit.typing.engines.smirnoff.parameters import (
    ConstraintHandler,
    ElectrostaticsHandler,
    LibraryChargeHandler,
    vdWHandler,
)
from openff.units import unit

dataframe = pandas.read_csv("openforcefields/data/jc.csv")

tip3p = ForceField()

tip3p_electrostatics = ElectrostaticsHandler(version=0.4)
tip3p_library = LibraryChargeHandler(version=0.3)
tip3p_vdw = vdWHandler(version=0.3)
tip3p_constraints = ConstraintHandler(version=0.3)

tip3p_vdw.add_parameter(
    {
        "smirks": "[#1]-[#8X2H2+0:1]-[#1]",
        "epsilon": unit.Quantity(0.1521, unit.kilocalorie_per_mole),
        "sigma": unit.Quantity(3.1507, unit.angstrom),
        "id": "n-tip3p-O",
    }
)
tip3p_vdw.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1]",
        "epsilon": unit.Quantity(0.0, unit.kilocalorie_per_mole),
        "sigma": unit.Quantity(1.0, unit.angstrom),
        "id": "n-tip3p-H",
    }
)

tip3p_library.add_parameter(
    {
        "smirks": "[#1]-[#8X2H2+0:1]-[#1]",
        "charge1": unit.Quantity(-0.834, unit.elementary_charge),
        "id": "q-tip3p-O",
    }
)
tip3p_library.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1]",
        "charge1": unit.Quantity(0.417, unit.elementary_charge),
        "id": "q-tip3p-H",
    }
)

for _, row in dataframe.iterrows():
    smirks = f"[{row['element']}1:1]"
    tip3p_vdw.add_parameter(
        {
            "smirks": smirks,
            "rmin_half": unit.Quantity(
                row["tip3p_rmin2 (A)"],
                unit.angstrom,
            ),
            "epsilon": unit.Quantity(
                row["tip3p_eps (kcal/mol)"],
                unit.kilocalorie_per_mole,
            ),
        }
    )

    tip3p_library.add_parameter(
        {
            "smirks": smirks,
            "charge1": unit.Quantity(
                int(row["element"][-1] + "1"), unit.elementary_charge
            ),
        }
    )

tip3p_constraints.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0:2]-[#1]",
        "id": "c-tip3p-H-O",
        "distance": unit.Quantity(0.9572, unit.angstrom),
    }
)
tip3p_constraints.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1:2]",
        "id": "c-tip3p-H-O-H",
        "distance": unit.Quantity(1.5139006545247014, unit.angstrom),
    }
)

for handler in [tip3p_vdw, tip3p_library, tip3p_electrostatics, tip3p_constraints]:
    tip3p.register_parameter_handler(handler)

tip3p.to_file("tip3p.offxml")
