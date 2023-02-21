from typing import Dict

import pandas
from openff.toolkit.typing.engines.smirnoff.forcefield import ForceField
from openff.toolkit.typing.engines.smirnoff.parameters import (
    ConstraintHandler,
    ElectrostaticsHandler,
    LibraryChargeHandler,
    vdWHandler,
)
from openff.units import unit
from packaging import version

VERSION = version.Version("1.0.0")
OFFXML_PATH = "openforcefields/offxml/"

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
        "sigma": unit.Quantity(1.0, unit.nanometer),
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

element_to_atomic_number: Dict[str, int] = {
    "Li": 3,
    "Na": 11,
    "K": 19,
    "Rb": 37,
    "Cs": 55,
    "F": 9,
    "Cl": 17,
    "Br": 35,
    "I": 53,
}


for _, row in dataframe.iterrows():
    # Add 'X0' into pattern, i.e. 'Li+'/'Cl-' to 'LiX0+1'/'ClX0-1'
    element_with_charge = row["element"]
    element = element_with_charge[:-1]
    atomic_number = element_to_atomic_number[element]
    charge = element_with_charge[-1]
    smirks = f"[#{atomic_number}X0{charge}1:1]"

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

tip3p.to_file(f"{OFFXML_PATH}tip3p.offxml")
tip3p.to_file(f"{OFFXML_PATH}tip3p_{VERSION}.offxml")
