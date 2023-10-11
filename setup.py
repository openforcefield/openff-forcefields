"""
openforcefields
"""
from setuptools import setup

import versioneer

short_description = __doc__.split("\n")

with open("README.md", "r") as handle:
    long_description = handle.read()


setup(
    name="openforcefields",
    author="The Open Force Field Initiative",
    author_email="info@openforcefield.org",
    description=short_description[0],
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license="CC-BY-4.0",
    packages=["openforcefields", "openforcefields.tests"],
    package_data={"openforcefields": ["offxml/*"]},
    url="https://github.com/openforcefield/openforcefields",
    platforms=[
        "Linux",
        "Mac OS-X",
        "Unix",
    ],
    entry_points={
        "openforcefield.smirnoff_forcefield_directory": [
            "get_forcefield_dirs_paths = openforcefields.openforcefields:get_forcefield_dirs_paths",
        ],
    },
)
