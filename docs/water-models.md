# Water models

The following water models are distributed with this package:

* TIP3P
* TIP4P-Ew
* TIP5P
* [TIP3P-FB](https://doi.org/10.1021/jz500737m)

The TIP3P and TIP4P-Ew files include monovalent ion parameters from [Juong and Cheatham](https://dx.doi.org/10.1021/jp8001614).

The Open Force Field Initiative has not released a new water model. These files are ports of existing force fields into the [SMIRNOFF](https://openforcefield.github.io/standards/standards/smirnoff/) force field format.

## Versioning

Two versions of each file are distributed, one with the shorthand name of each file (i.e. `tip3p.offxml`) for ease of use and another with a tagged version (i.e. `tip3p-1.0.0.offxml`).
The first version of each file is given version number 1.0.0 and is associated with a best-effort attempt at reproducing the parameters from the reported source.
These parameters may not match _exactly_ what is reported in other distributed files, such as those bundled alongside of MD engines, which often do not agree with each other.
If errors in files are discovered, changes may be made and released in new versions of these files, i.e. `tip3p_1.0.1.offxml`).
At all times, the contents of the file named with the short-hand name will match the contents of the file with the highest version number.
Therefore, versions of `tip3p.offxml` loaded with different versions of `openff-forcefields` **may differ slightly** in the numerical values of parameters.
To eliminate this possibility, use a versioned file name, i.e. `ForceField("tip3p-1.0.0.offxml")` instead of `ForceField("tip3p.offxml")`.
