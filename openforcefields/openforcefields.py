"""
openforcefields.py

This module only contains the function that will be the entry point that
will be used by the openforcefield toolkit to find the installed forcefield
files.

"""
from importlib.resources import files


def get_forcefield_dirs_paths() -> list[str]:
    """
    Return the paths to the directories including the forcefield files.

    This function is set as an entry point in setup.py. It will be called
    by the openforcefield toolkit when discovering the installed folders
    including offxml files.

    Returns
    -------
    dir_paths : list[str]
        The list of directory paths containing the SMIRNOFF files.

    """
    return [(files("openforcefields") / "offxml").as_posix()]
