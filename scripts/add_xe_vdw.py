from openff.toolkit import ForceField
from openff.toolkit.typing.engines.smirnoff import vdWHandler
from openff.units import unit

sage_21 = ForceField("openff-2.1.0.offxml")
sage_21_uc = ForceField("openff_unconstrained-2.1.0.offxml")

# Add the new parameters, from:
# Tang, K.T., Toennies, J.P. New combining rules for well parameters and shapes
# of the van der Waals potential of mixed rare gas systems. Z Phys D - Atoms,
# Molecules and Clusters 1, 91–101 (1986). https://doi.org/10.1007/BF01384663
xe_param = vdWHandler.vdWType(
    smirks="[#54:1]",
    epsilon=0.56108 * unit.kilocalorie / unit.mole,
    sigma=4.363 * unit.angstrom,
    id="n36",
)

sage_21.get_parameter_handler("vdW").parameters.append(xe_param)
sage_21.to_file("../openforcefields/offxml/openff-2.1.1.offxml")
sage_21_uc.get_parameter_handler("vdW").parameters.append(xe_idx_sage21, xe_param)
sage_21_uc.to_file("../openforcefields/offxml/openff_unconstrained-2.1.1.offxml")

# Make sure new FF loads with most recent toolkit version
test_sage_211 = ForceField("../openforcefields/offxml/openff-2.1.1.offxml")
test_sage_211_uc = ForceField(
    "../openforcefields/offxml/openff_unconstrained-2.1.1.offxml"
)
print("Success!")
