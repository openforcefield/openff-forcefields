"""
Write TIP3P-FB parameters into a SMIRNOFF force field. Based on
https://github.com/pandegroup/tip3p-tip4p-fb/blob/master/OpenMM/tip4p-fb/tip4p-fb.xml
Ion Lennard-Jones parameters from $AMBERHOME/dat/leap/parm/frcmod.ionslm_126_fb4
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
    Path("openforcefields", "data", "ionslm_126_fb4.csv")
)

tip4p_fb = ForceField()

tip4p_fb_electrostatics = ElectrostaticsHandler(version=0.4, scale14=0.8333333333)
tip4p_fb_library = LibraryChargeHandler(version=0.3)
tip4p_fb_vdw = vdWHandler(version=0.4)
tip4p_fb_constraints = ConstraintHandler(version=0.3)
tip4p_fb_virtual_sites = VirtualSiteHandler(version=0.3)

tip4p_fb_vdw.add_parameter(
    {
        "smirks": "[#1]-[#8X2H2+0:1]-[#1]",
        "epsilon": unit.Quantity(0.7492790213533, unit.kilojoule_per_mole),
        "sigma": unit.Quantity(0.3165552430462, unit.nanometer),
        "id": "n-tip4p-fb-O",
    }
)
tip4p_fb_vdw.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1]",
        "epsilon": unit.Quantity(0.0, unit.kilocalorie_per_mole),
        "sigma": unit.Quantity(1.0, unit.nanometer),
        "id": "n-tip4p-fb-H",
    }
)

tip4p_fb_library.add_parameter(
    {
        "smirks": "[#1]-[#8X2H2+0:1]-[#1]",
        "charge1": unit.Quantity(0.0, unit.elementary_charge),
        "id": "q-tip4p-fb-O",
    }
)
tip4p_fb_library.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1]",
        "charge1": unit.Quantity(0.0, unit.elementary_charge),
        "id": "q-tip4p-fb-H",
    }
)

# Virtual site distance = 0.08984267127345 * 2 * 0.09572 * cos(1.82421813418 / 2)
tip4p_fb_virtual_sites.add_parameter(
    {
        "type": "DivalentLonePair",
        "smirks": "[#1:2]-[#8X2H2+0:1]-[#1:3]",
        "match": "once",
        "name": "EP",
        "distance": unit.Quantity(-0.010527445756662016, unit.nanometer),
        "sigma": unit.Quantity(1.0, unit.angstrom),
        "epsilon": unit.Quantity(0.0, unit.kilocalorie_per_mole),
        "outOfPlaneAngle": unit.Quantity(0.0, unit.degree),
        "charge_increment1": unit.Quantity(0.0, unit.elementary_charge),
        "charge_increment2": unit.Quantity(0.5258681106763, unit.elementary_charge),
        "charge_increment3": unit.Quantity(0.5258681106763, unit.elementary_charge),
    }
)

tip4p_fb_constraints.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0:2]-[#1]",
        "id": "c-tip4p-fb-H-O",
        "distance": unit.Quantity(0.09572, unit.nanometer),
    }
)
# H-H distance = 2 * 0.09572 * sin(1.82421813418 / 2)
tip4p_fb_constraints.add_parameter(
    {
        "smirks": "[#1:1]-[#8X2H2+0]-[#1:2]",
        "id": "c-tip4p-fb-H-O-H",
        "distance": unit.Quantity(0.15139006545247014, unit.nanometer),
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

    tip4p_fb_vdw.add_parameter(
        {
            "smirks": smirks,
            "rmin_half": unit.Quantity(row["rmin_half (Angstrom)"], unit.angstrom),
            "epsilon": unit.Quantity(
                row["epsilon (kcal/mol)"],
                unit.kilocalorie_per_mole,
            ),
            "id": f"n-ionslm-126-tip4p-fb-{ion_name}",
        }
    )

    tip4p_fb_library.add_parameter(
        {
            "smirks": smirks,
            "charge1": unit.Quantity(
                int(f"{charge_sign}{charge_magnitude}"), unit.elementary_charge
            ),
            "id": f"q-ionslm-126-tip4p-fb-{ion_name}",
        }
    )

for handler in [
    tip4p_fb_vdw,
    tip4p_fb_library,
    tip4p_fb_electrostatics,
    tip4p_fb_constraints,
    tip4p_fb_virtual_sites,
]:
    tip4p_fb.register_parameter_handler(handler)

tip4p_fb.to_file(Path(OFFXML_PATH, "tip4p_fb.offxml"))
tip4p_fb.to_file(Path(OFFXML_PATH, f"tip4p_fb-{VERSION}.offxml"))
