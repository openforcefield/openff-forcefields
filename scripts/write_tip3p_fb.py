"""
Write TIP3P-FB parameters into a SMIRNOFF force field. Based on
https://github.com/pandegroup/tip3p-tip4p-fb/blob/master/OpenMM/tip3p-fb/tip3p-fb.xml
Ion Lennard-Jones parameters from $AMBERHOME/dat/leap/parm/frcmod.ionslm_126_fb3
"""
from pathlib import Path

import pandas
from openff.toolkit.typing.engines.smirnoff.forcefield import ForceField
from openff.toolkit.typing.engines.smirnoff.parameters import (
    ConstraintHandler,
    ElectrostaticsHandler,
    LibraryChargeHandler,
    vdWHandler,
)
from openff.units import unit
from openff.units.elements import SYMBOLS
from packaging import version

VERSION = version.Version("1.1.0")
OFFXML_PATH = Path("openforcefields", "offxml")

ion_nb_params_df = pandas.read_csv(
    Path("openforcefields", "data", "ionslm_126_fb3.csv")
)

tip3p_fb = ForceField()

tip3p_fb_electrostatics = ElectrostaticsHandler(version=0.4, scale14=0.8333333333)
tip3p_fb_library = LibraryChargeHandler(version=0.3)
tip3p_fb_vdw = vdWHandler(version=0.3)
tip3p_fb_constraints = ConstraintHandler(version=0.3)

tip3p_fb_vdw.add_parameter(
    {
        "smirks": "[#1]-[#8X2H2+0:1]-[#1]",
        "epsilon": unit.Quantity(0.652143528104, unit.kilojoule_per_mole),
        "sigma": unit.Quantity(0.317796456355, unit.nanometer),
        "id": "n-tip3p-fb-O",
    }
)
tip3p_fb_vdw.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1]",
        "epsilon": unit.Quantity(0.0, unit.kilocalorie_per_mole),
        "sigma": unit.Quantity(1.0, unit.nanometer),
        "id": "n-tip3p-fb-H",
    }
)

tip3p_fb_library.add_parameter(
    {
        "smirks": "[#1]-[#8X2H2+0:1]-[#1]",
        "charge1": unit.Quantity(-0.848448690103, unit.elementary_charge),
        "id": "q-tip3p-fb-O",
    }
)
tip3p_fb_library.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1]",
        "charge1": unit.Quantity(0.4242243450515, unit.elementary_charge),
        "id": "q-tip3p-fb-H",
    }
)

tip3p_fb_constraints.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0:2]-[#1]",
        "id": "c-tip3p-fb-H-O",
        "distance": unit.Quantity(0.101181082494, unit.nanometer),
    }
)
# 2 * 0.101181082494 * sin(108.14844252012414 / 2 * degrees)
tip3p_fb_constraints.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1:2]",
        "id": "c-tip3p-fb-H-O-H",
        "distance": unit.Quantity(0.16386837572, unit.nanometer),
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

    tip3p_fb_vdw.add_parameter(
        {
            "smirks": smirks,
            "rmin_half": unit.Quantity(row["rmin_half (Angstrom)"], unit.angstrom),
            "epsilon": unit.Quantity(
                row["epsilon (kcal/mol)"],
                unit.kilocalorie_per_mole,
            ),
            "id": f"n-ionslm-126-tip3p-fb-{ion_name}",
        }
    )

    tip3p_fb_library.add_parameter(
        {
            "smirks": smirks,
            "charge1": unit.Quantity(
                int(f"{charge_sign}{charge_magnitude}"), unit.elementary_charge
            ),
            "id": f"q-ionslm-126-tip3p-fb-{ion_name}",
        }
    )

for handler in [
    tip3p_fb_vdw,
    tip3p_fb_library,
    tip3p_fb_electrostatics,
    tip3p_fb_constraints,
]:
    tip3p_fb.register_parameter_handler(handler)

tip3p_fb.to_file(Path(OFFXML_PATH, "tip3p_fb.offxml"))
tip3p_fb.to_file(Path(OFFXML_PATH, f"tip3p_fb-{VERSION}.offxml"))
