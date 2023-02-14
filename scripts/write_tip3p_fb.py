"""
Write TIP3P-FB parameters into a SMIRNOFF force field. Based on
https://github.com/pandegroup/tip3p-tip4p-fb/blob/master/OpenMM/tip3p-fb/tip3p-fb.xml
"""
from packaging import version
from openff.toolkit.typing.engines.smirnoff.forcefield import ForceField
from openff.toolkit.typing.engines.smirnoff.parameters import (
    ConstraintHandler,
    ElectrostaticsHandler,
    LibraryChargeHandler,
    vdWHandler,
)
from openff.units import unit

VERSION = version.Version("1.0.0")

tip3p_fb = ForceField()

tip3p_fb_electrostatics = ElectrostaticsHandler(version=0.4)
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
        "distance": unit.Quantity(0.16386837572, unit.angstrom),
    }
)

for handler in [
    tip3p_fb_vdw,
    tip3p_fb_library,
    tip3p_fb_electrostatics,
    tip3p_fb_constraints,
]:
    tip3p_fb.register_parameter_handler(handler)

tip3p_fb.to_file("tip3p-fb.offxml")
tip3p_fb.to_file(f"tip3p-fb_{VERSION}.offxml")
