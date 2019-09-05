"""
openforcefields
"""
import sys
from setuptools import setup
import versioneer

short_description = __doc__.split("\n")

# from https://github.com/pytest-dev/pytest-runner#conditional-requirement
needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

try:
    with open("README.md", "r") as handle:
        long_description = handle.read()
except:
    long_description = "\n".join(short_description[2:]),


setup(
    # Self-descriptive entries which should always be present
    name='openforcefields',
    author='The Open Force Field Initiative',
    author_email='dmobley@uci.edu',
    description=short_description[0],
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license='CC-BY-4.0',

    # Which Python importable modules should be included when your package is installed
    packages=['openforcefields', "openforcefields.tests"],

    # Optional include package data to ship with your package
    # Comment out this line to prevent the files from being packaged with your software
    # Extend/modify the list to include/exclude other items as need be
    package_data={'openforcefields': ["offxml/*"]
                  },

    # Allows `setup.py test` to work correctly with pytest
    setup_requires=[] + pytest_runner,

    # Additional entries you may want simply uncomment the lines you want and fill in the data
    url='https://github.com/openforcefield/openforcefields',  # Website
    # install_requires=[],              # Required packages, pulls from pip if needed; do not use for Conda deployment
    platforms=['Linux',
               'Mac OS-X',
               'Unix'],                 # Valid platforms your code works on, adjust to your flavor
    # python_requires=">=3.5",          # Python version restrictions

    # Manual control if final package is compressible or not, set False to prevent the .egg from being made
    # zip_safe=False,

    # Add entry point so that the forcefield directory can be discovered by the openforcefield toolkit.
    entry_points={
        'openforcefield.smirnoff_forcefield_directory' : [
            'get_forcefield_dirs_paths = openforcefields.openforcefields:get_forcefield_dirs_paths',
        ],
    }
)
