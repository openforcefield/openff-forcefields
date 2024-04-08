"""
openff-forcefields
"""

from setuptools import setup

import versioneer

short_description = __doc__.split("\n")

with open("README.md") as handle:
    long_description = handle.read()


setup(
    # Self-descriptive entries which should always be present
    name="openforcefields",
    author="The Open Force Field Initiative",
    author_email="info@openforcefield.org",
    description=short_description[0],
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license="CC-BY-4.0",
    # Which Python importable modules should be included when your package is installed
    packages=["openforcefields", "openforcefields.tests"],
    # Optional include package data to ship with your package
    # Comment out this line to prevent the files from being packaged with your software
    # Extend/modify the list to include/exclude other items as need be
    package_data={"openforcefields": ["offxml/*"]},
    # Additional entries you may want simply uncomment the lines you want and fill in the data
    url="https://github.com/openforcefield/openforcefields",
    platforms=[
        "Linux",
        "Mac OS-X",
        "Unix",
    ],  # Valid platforms your code works on, adjust to your flavor
    # Add entry point so that the forcefield directory can be discovered by the openforcefield toolkit.
    entry_points={
        "openforcefield.smirnoff_forcefield_directory": [
            "get_forcefield_dirs_paths = openforcefields.openforcefields:get_forcefield_dirs_paths",
        ],
    },
)
