"""
Open Force fields
"""

# Handle versioneer
from ._version import get_versions

# Add imports here
from .openforcefields import get_forcefield_dirs_paths

versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions
