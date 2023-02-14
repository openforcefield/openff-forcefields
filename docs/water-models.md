# Water models

The following water models are distributed with this package:

* [TIP3P](https://doi.org/10.1063/1.445869)
* [TIP3P-FB](https://doi.org/10.1021/jz500737m)

The TIP3P file includes monovalent ion parameters from [Juong and Cheatham](https://dx.doi.org/10.1021/jp8001614).

Future releases of this package may include the following models:

* TIP4P-Ew (with Juong and Cheatham monovalent ion parameters)
* TIP5P

The Open Force Field Initiative has not refit a new water model.
These files are ports of existing force fields into the [SMIRNOFF](https://openforcefield.github.io/standards/standards/smirnoff/) force field format.

## Versioning

Two identical copies of each file are distributed, one with the shorthand name of each file (i.e. `tip3p.offxml`) for ease of use and another with a tagged version using [semantic versioning](https://semver.org/) (i.e. `tip3p_1.0.0.offxml`).
Versions of force field files do not correspond to versions of the `openff-forcefields` package.
The first version of each file is given version number 1.0.0 and is associated with a best-effort attempt at reproducing the parameters from the original source.
These parameters may not precisely match what is packaged elsewhere, such as those bundled alongside of MD engines. Such files often do not agree with each other to the last significant digit.
If errors in these files are discovered, changes may be made and released in new versions of these files, i.e. `tip3p_1.0.1.offxml`.
To report a possible issue, please raise an issue on the `openff-forcefields` [GitHub page](https://github.com/openforcefield/openff-forcefields/issues/new).
At all times, the contents of file without explicit versions tags will match the contents of the corresponding version-tagged file with the highest version number.
Therefore, files without explicit version tags loaded with different versions of `openff-forcefields` **may differ slightly** in the numerical values of parameters.
To eliminate this possibility, use a versioned file name, i.e. `ForceField("tip3p_1.0.0.offxml")` instead of `ForceField("tip3p.offxml")`.
