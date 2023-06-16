"""
Write OPC parameters into a SMIRNOFF force field.
Based on ambertools-22.0-py310h206695f.
Water Lennard-Jones parameters and geometry from $AMBERHOME/dat/leap/parm/frcmod.opc3
Water hydrogen charge from $AMBERHOME/dat/leap/lib/solvents.lib
Ion Lennard-Jones parameters from $AMBERHOME/dat/leap/parm/frcmod.ionslm_126_opc3
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
from openff.units.elements import SYMBOLS
from packaging import version

VERSION = version.Version("1.0.1")
OFFXML_PATH = Path("openforcefields", "offxml")

ion_nb_params_df = pandas.read_csv(
    Path("openforcefields", "data", "ionslm_126_opc.csv")
)

opc = ForceField()

opc_electrostatics = ElectrostaticsHandler(version=0.4, scale14=0.8333333333)
opc_library = LibraryChargeHandler(version=0.3)
opc_vdw = vdWHandler(version=0.3)
opc_constraints = ConstraintHandler(version=0.3)
opc_virtual_sites = VirtualSiteHandler(version=0.3)

opc_vdw.add_parameter(
    {
        "smirks": "[#1]-[#8X2H2+0:1]-[#1]",
        "epsilon": unit.Quantity(0.2128008130, unit.kilocalorie_per_mole),
        "rmin_half": unit.Quantity(1.777167268, unit.angstrom),
        "id": "n-opc-O",
    }
)
opc_vdw.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1]",
        "epsilon": unit.Quantity(0.0, unit.kilocalorie_per_mole),
        "rmin_half": unit.Quantity(1.0, unit.angstrom),
        "id": "n-opc-H",
    }
)

opc_library.add_parameter(
    {
        "smirks": "[#1]-[#8X2H2+0:1]-[#1]",
        "charge1": unit.Quantity(0.0, unit.elementary_charge),
        "id": "q-opc-O",
    }
)
opc_library.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1]",
        "charge1": unit.Quantity(0.0, unit.elementary_charge),
        "id": "q-opc-H",
    }
)

opc_virtual_sites.add_parameter(
    {
        "type": "DivalentLonePair",
        "smirks": "[#1:2]-[#8X2H2+0:1]-[#1:3]",
        "match": "once",
        "name": "EP",
        "distance": unit.Quantity(-0.15939833, unit.angstrom),
        "rmin_half": unit.Quantity(1.0, unit.angstrom),
        "epsilon": unit.Quantity(0.0, unit.kilocalorie_per_mole),
        "outOfPlaneAngle": unit.Quantity(0.0, unit.degree),
        "charge_increment1": unit.Quantity(0.0, unit.elementary_charge),
        "charge_increment2": unit.Quantity(0.679142, unit.elementary_charge),
        "charge_increment3": unit.Quantity(0.679142, unit.elementary_charge),
    }
)

opc_constraints.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0:2]-[#1]",
        "id": "c-opc-H-O",
        "distance": unit.Quantity(0.87243313, unit.angstrom),
    }
)
opc_constraints.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1:2]",
        "id": "c-opc-H-O-H",
        "distance": unit.Quantity(1.37120510, unit.angstrom),
    }
)

# Construct dict of element symbol to atomic number
_SYMBOLS_TO_ATOMIC_NUMBER = {
    symbol: atomic_number for atomic_number, symbol in SYMBOLS.items()
}

for _, row in ion_nb_params_df.iterrows():
    ion_name = row["element"]

    # Handle variable length element names
    if any(charge_str in ion_name for charge_str in ["2+", "3+", "4+"]):
        atomic_number = _SYMBOLS_TO_ATOMIC_NUMBER[ion_name[:-2]]
        charge_sign = "+"
        charge_magnitude = ion_name[-2]

    else:
        atomic_number = _SYMBOLS_TO_ATOMIC_NUMBER[ion_name[:-1]]
        charge_sign = ion_name[-1]
        charge_magnitude = "1"

    smirks = f"[#{atomic_number}X0{charge_sign}{charge_magnitude}:1]"

    opc_vdw.add_parameter(
        {
            "smirks": smirks,
            "rmin_half": unit.Quantity(row["rmin_half (Angstrom)"], unit.angstrom),
            "epsilon": unit.Quantity(
                row["epsilon (kcal/mol)"],
                unit.kilocalorie_per_mole,
            ),
            "id": f"n-ionslm-126-opc-{ion_name}",
        }
    )

    opc_library.add_parameter(
        {
            "smirks": smirks,
            "charge1": unit.Quantity(
                int(f"{charge_sign}{charge_magnitude}"), unit.elementary_charge
            ),
            "id": f"q-ionslm-126-opc-{ion_name}",
        }
    )

for handler in [
    opc_vdw,
    opc_library,
    opc_electrostatics,
    opc_constraints,
    opc_virtual_sites,
]:
    opc.register_parameter_handler(handler)

opc.to_file(Path(OFFXML_PATH, "opc.offxml"))
opc.to_file(Path(OFFXML_PATH, f"opc-{VERSION}.offxml"))
