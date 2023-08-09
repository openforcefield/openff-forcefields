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

spce = ForceField()

spce_electrostatics = ElectrostaticsHandler(version=0.4, scale14=0.8333333333)
spce_library = LibraryChargeHandler(version=0.3)
spce_vdw = vdWHandler(version=0.4)
spce_constraints = ConstraintHandler(version=0.3)

spce_vdw.add_parameter(
    {
        "smirks": "[#1]-[#8X2H2+0:1]-[#1]",
        "epsilon": unit.Quantity(0.1553942681, unit.kilocalorie_per_mole),
        "sigma": unit.Quantity(3.16555789, unit.angstrom),
        "id": "n-spce-O",
    }
)
spce_vdw.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1]",
        "epsilon": unit.Quantity(0.0, unit.kilocalorie_per_mole),
        "sigma": unit.Quantity(1.0, unit.nanometer),
        "id": "n-spce-H",
    }
)

spce_library.add_parameter(
    {
        "smirks": "[#1]-[#8X2H2+0:1]-[#1]",
        "charge1": unit.Quantity(-0.8476, unit.elementary_charge),
        "id": "q-spce-O",
    }
)
spce_library.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1]",
        "charge1": unit.Quantity(0.4238, unit.elementary_charge),
        "id": "q-spce-H",
    }
)

spce_constraints.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0:2]-[#1]",
        "id": "c-spce-H-O",
        "distance": unit.Quantity(1.0, unit.angstrom),
    }
)
spce_constraints.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1:2]",
        "id": "c-spce-H-O-H",
        "distance": unit.Quantity(1.63298086184, unit.angstrom),
    }
)

for handler in [spce_vdw, spce_library, spce_electrostatics, spce_constraints]:
    spce.register_parameter_handler(handler)

spce.to_file(f"{OFFXML_PATH}spce.offxml")
spce.to_file(f"{OFFXML_PATH}spce-{VERSION}.offxml")
