"""
Unit and regression test for the openforcefields package.
"""

import glob
import os

import pytest

from openforcefields import get_forcefield_dirs_paths

try:
    import openff.toolkit  # noqa

    has_off_toolkit = True
except ModuleNotFoundError:
    has_off_toolkit = False


def find_all_offxml_files():
    """Return a list of the offxml files shipped with the package."""
    file_names = []
    for dir_path in get_forcefield_dirs_paths():
        file_pattern = os.path.join(dir_path, "*.offxml")
        file_paths = [file_path for file_path in glob.glob(file_pattern)]
        file_names.extend([os.path.basename(file_path) for file_path in file_paths])
    return file_names


@pytest.mark.parametrize("offxml_file_name", find_all_offxml_files())
def test_openforcefields_entrypoint(offxml_file_name):
    """Test that the OpenFF Toolkit can find and parse the files."""
    import os

    ff_found = False
    for dir_path in get_forcefield_dirs_paths():
        ff_path = os.path.join(dir_path, offxml_file_name)
        if os.path.exists(ff_path):
            ff_found = True
            break
    assert ff_found


@pytest.mark.skipif(not (has_off_toolkit), reason="Test requires OFF toolkit")
@pytest.mark.parametrize("offxml_file_name", find_all_offxml_files())
def test_forcefield_data_is_loadable(offxml_file_name):
    """Test that the OpenFF Toolkit can find and parse the files."""
    from openff.toolkit.typing.engines.smirnoff import ForceField

    ForceField(offxml_file_name)


@pytest.mark.skipif(not (has_off_toolkit), reason="Test requires OFF toolkit")
def test_forcefield_data_is_not_loadable():
    """Test that the OpenFF Toolkit does raise an Exception if
    a nonexistent FF isn't found."""
    from openff.toolkit.typing.engines.smirnoff import ForceField

    with pytest.raises(OSError):
        ForceField("openff-9.9.9.offxml")


@pytest.mark.skipif(not (has_off_toolkit), reason="Test requires OFF toolkit")
@pytest.mark.parametrize("offxml_file_name", ["openff-2.3.0-rc1.offxml", "openff_unconstrained-2.3.0-rc1.offxml"])
def test_can_charge_nagl_nodownload(offxml_file_name):
    """
    Test that the OpenFF Toolkit can load and usethe NAGLCharges section.

    This is a specific test to check hash matching and loading of the model file.
    """
    pytest.importorskip("openff.nagl_models")
    from openff.toolkit import ForceField, Molecule

    ff = ForceField(offxml_file_name)
    mol = Molecule.from_smiles("CCO")
    ff.create_interchange(mol.to_topology())
