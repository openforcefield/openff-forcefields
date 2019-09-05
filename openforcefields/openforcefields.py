"""
openforcefields.py
A general small molecule forcefield descended from AMBER99 and parm@Frosst in the SMIRNOFF format.

This module only contains the function that will be the entry point that
will be used by the openforcefield toolkit to find the installed forcefield
files.

"""

from pkg_resources import resource_filename


def get_forcefield_dirs_paths():
    """
    Return the paths to the directories including the forcefield files.

    This function is set as an entry point in setup.py. It will be called
    by the openforcefield toolkit when discovering the installed folders
    including offxml files.

    Returns
    -------
    dir_paths : List[str]
        The list of directory paths containing the SMIRNOFF files.

    """
    return [resource_filename('openforcefields', 'offxml')]
