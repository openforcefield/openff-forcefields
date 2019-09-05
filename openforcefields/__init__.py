"""
Open Force fields
"""

# Add imports here
from .openforcefields import get_forcefield_dirs_paths

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
