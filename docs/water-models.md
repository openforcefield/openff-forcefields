# Water models

The following water models are distributed with this package:

* [TIP3P](https://doi.org/10.1063/1.445869)
* [TIP3P-FB](https://doi.org/10.1021/jz500737m)
* [OPC](https://doi.org/10.1021/jz501780a)

The TIP3P file includes monovalent ion parameters from [Juong and Cheatham](https://dx.doi.org/10.1021/jp8001614).

The OPC file includes the 12-6 hydration free energy (HFE) monovalent ion parameters from [Sengupta et al. 2021](https://doi.org/10.1021/acs.jcim.0c01390), the 12-6 compromise (CM) divalent ion parameters from [Li et al. 2020](https://doi.org/10.1021/acs.jctc.0c00194), and the 12-6 ion-oxygen distance (IOD) trivalent and tetravalent ion parameters from [Li et al. 2021](https://doi.org/10.1021/acs.jctc.0c01320).

These files are not original force fields made by Open Force Field.
Instead they are ports of existing force fields into the [SMIRNOFF](https://openforcefield.github.io/standards/standards/smirnoff/) force field format.

**Note**: Current mainline SMIRNOFF force fields already contain a water model and ion parameters. If you intend to use a mainline OpenFF force field for most molecules in a topology while using an alternate force field specifically for water and ions, ensure that the water-and-ions force field is loaded _last_, so that its parameters take precedence over those from the main-line force field.  

## Versioning

Two identical copies of each file are distributed, one with the shorthand name of each file (i.e. `tip3p.offxml`) for ease of use and another with a tagged version using [semantic versioning](https://semver.org/) (i.e. `tip3p_1.0.0.offxml`).
At all times, the contents of file without an explicit version will match the contents of the corresponding version-tagged file with the highest version number.
Therefore, files without explicit version tags loaded with different versions of `openff-forcefields` **may differ slightly** in the numerical values of parameters.
To eliminate this possibility, use a versioned file name, i.e. `ForceField("tip3p_1.0.0.offxml")` instead of `ForceField("tip3p.offxml")`.


The first version of each file is given version number 1.0.0 and is associated with a best-effort attempt at reproducing the parameters from the original source.
These parameters may not precisely match what is packaged elsewhere, such as those bundled alongside of MD engines. Such files often do not agree with each other to the last significant digit.
The SMIRNOFF format also requires definitions of some terms that affect the total energy of a system, but are either not relevant or not clearly defined for these water models, such as 1-4 scaling factors and nonbonded cutoffs. We make an effort here to choose values for these settings to ensure compatibility with the most recent mainline OpenFF force field, but when using other force fields users may need to update these values manually to ensure compatibility. 


If errors in these files are discovered, changes may be made and released in new versions of these files, i.e. `tip3p_1.0.1.offxml`.
To report a possible issue, please raise an issue on the `openff-forcefields` [GitHub page](https://github.com/openforcefield/openff-forcefields/issues/new).
