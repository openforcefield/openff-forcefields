# Open Force Fields

[![Build Status](https://github.com/openforcefield/openff-forcefields/workflows/CI/badge.svg)](https://github.com/openforcefield/openff-forcefields/actions?query=branch%3Amaster+workflow%3ACI)  [![Paper DOI](https://img.shields.io/badge/Paper%20DOI-10.1021%2Facs.jctc.1c00571-blue)](https://doi.org/10.1021/acs.jctc.1c00571)



This repository contains force fields released by the [Open Force Field Initiative](https://openforcefield.org).
These files are in SMIRKS Native Open Force Field (SMIRNOFF) format.
Details about this new format are documented in our recent publication ([doi:10.1021/acs.jctc.8b00640](https://www.doi.org/10.1021/acs.jctc.8b00640) or [bioRxiv](https://doi.org/10.1101/286542)), and the most recent specification can be found in the [Open Force Field Toolkit documentation](https://open-forcefield-toolkit.readthedocs.io/en/latest/smirnoff.html).
You can parameterize small molecules with SMIRNOFF using the
`ForceField` class in the [Open Force Field toolkit](https://github.com/openforcefield/openff-toolkit)
for simulations with [OpenMM](http://openmm.org/). The resulting system can also be converted to several other simulation formats using [ParmEd](http://parmed.github.io/ParmEd/html/index.html).

Usage examples can be found in the [openff-toolkit repository](https://github.com/openforcefield/openff-toolkit/tree/master/examples).

Each force field is currently available in two forms --  Both with and without bond constraints to hydrogen. The default version of each force field is suitable for typical molecular dynamics simulations with constrained bonds to hydrogen. The `unconstrained` version of each force field should be used when single-point energies are a major concern (e.g. geometry optimizations) and when comparing the force field to QM data.

To cite the Parsley line of force fields (`openff-1.X.Y`) please use [this citation](https://doi.org/10.1021/acs.jctc.1c00571). Optionally, consider also citing the version-specific Zenodo DOI for the particular force field from the table below.

Details for each force field in this repository can be found in the following table:

| Filename | DOI | FF line | Release Date | Major format changes? |
| -------- | --- | -------- | --- | --- |
| `openff-2.0.0.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5214478.svg)](https://doi.org/10.5281/zenodo.5214478) | Sage | Aug 16, 2021 | No |
| `openff_unconstrained-2.0.0.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5214478.svg)](https://doi.org/10.5281/zenodo.5214478) | Sage | Aug 16, 2021 | No |
| `openff-2.0.0-rc.2.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5156698.svg)](https://doi.org/10.5281/zenodo.5156698) | Sage | Aug 3, 2021 | No |
| `openff_unconstrained-2.0.0-rc.2.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5156698.svg)](https://doi.org/10.5281/zenodo.5156698) | Sage | Aug 3, 2021 | No |
| `openff-2.0.0-rc.1.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5009196.svg)](https://doi.org/10.5281/zenodo.5009196) | Sage | June 21, 2021 | No |
| `openff_unconstrained-2.0.0-rc.1.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5009196.svg)](https://doi.org/10.5281/zenodo.5009196) | Sage | June 21, 2021 | No |
| `openff-1.3.1.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5009058.svg)](https://doi.org/10.5281/zenodo.5009058) | Parsley | June 21, 2021 | No |
| `openff_unconstrained-1.3.1.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5009058.svg)](https://doi.org/10.5281/zenodo.5009058) | Parsley | June 21, 2021 | No |
| `openff-1.3.1-alpha.1.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4697390.svg)](https://doi.org/10.5281/zenodo.4697390) | Parsley | Apr 15, 2021 | No |
| `openff_unconstrained-1.3.1-alpha.1.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4697390.svg)](https://doi.org/10.5281/zenodo.4697390) | Parsley | Apr 15, 2021 | No |
| `openff-1.3.0.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4118484.svg)](https://doi.org/10.5281/zenodo.4118484) | Parsley | Oct 21, 2020 | No |
| `openff_unconstrained-1.3.0.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4118484.svg)](https://doi.org/10.5281/zenodo.4118484) | Parsley | Oct 21, 2020 | No |
| `openff-1.2.1.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4021623.svg)](https://doi.org/10.5281/zenodo.4021623) | Parsley | Sep 9, 2020 | No |
| `openff_unconstrained-1.2.1.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4021623.svg)](https://doi.org/10.5281/zenodo.4021623) | Parsley | Sep 9, 2020 | No |
| `openff-1.2.0.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3872244.svg)](https://doi.org/10.5281/zenodo.3872244) | Parsley | May 29, 2020 | No |
| `openff_unconstrained-1.2.0.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3872244.svg)](https://doi.org/10.5281/zenodo.3872244) | Parsley | May 29, 2020 | No |
| `openff-1.1.1.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3751818.svg)](https://doi.org/10.5281/zenodo.3751818) | Parsley | Apr 14, 2020 | No |
| `openff_unconstrained-1.1.1.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3751818.svg)](https://doi.org/10.5281/zenodo.3751818) | Parsley | Apr 14, 2020 | No |
| `openff-1.1.0.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3695094.svg)](https://doi.org/10.5281/zenodo.3695094) | Parsley | Mar 3, 2020 | No |
| `openff_unconstrained-1.1.0.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3695094.svg)](https://doi.org/10.5281/zenodo.3695094) | Parsley | Mar 3, 2020 | No |
| `openff-1.0.1.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3751812.svg)](https://doi.org/10.5281/zenodo.3751812) | Parsley | Apr 14, 2020 | No |
| `openff_unconstrained-1.0.1.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3751812.svg)](https://doi.org/10.5281/zenodo.3751812) | Parsley | Apr 14, 2020 | No |
| `openff-1.0.0.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3483227.svg)](https://doi.org/10.5281/zenodo.3483227) | Parsley | Oct 12, 2019 | No |
| `openff_unconstrained-1.0.0.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3483227.svg)](https://doi.org/10.5281/zenodo.3483227) | Parsley | Oct 12, 2019 | No |
| `openff-1.0.0-RC2.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3473554.svg)](https://doi.org/10.5281/zenodo.3473554) | None | Oct 4, 2019 | No |
| `openff_unconstrained-1.0.0-RC2.offxml` | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3473554.svg)](https://doi.org/10.5281/zenodo.3473554) | None | Oct 4, 2019 | No |
| `openff-1.0.0-RC1.offxml` | None | None | Oct 4, 2019 | N/A |
| `openff_unconstrained-1.0.0-RC1.offxml` | None | None | Oct 4, 2019 | N/A |



## Installation
```bash
conda install -c conda-forge openff-forcefields
```

## Use

Installing this package exposes an entry point that makes the `openforcefield-forcefields/offxml` directory easily accessible by other packages in the same python installation. If the [Open Force Field toolkit](https://github.com/openforcefield/openff-toolkit) is installed, it will automatically detect and use this entry point:

```
>>> from openff.toolkit.typing.engines.smirnoff import ForceField
>>> ff = ForceField('openff-1.0.0-RC1.offxml') 
```

Otherwise, the entry point can be accessed by querying the `openforcefield.smirnoff_forcefield_directory` entry point group.

```
>>> from pkg_resources import iter_entry_points
>>> for entry_point in iter_entry_points(group='openforcefield.smirnoff_forcefield_directory'):
...     print(entry_point.load()())
```

## What it is

The provided OFFXML (force field) files are successive versions of a general-purpose small molecule force field, written in [the SMIRNOFF format](https://github.com/openforcefield/openff-toolkit/blob/master/The-SMIRNOFF-force-field-format.md); this force field should cover all or almost all of drug-like chemical space, and illustrate some of the major functionality of the SMIRNOFF format as well as how it simplifies the specification of force field parameters in a compact and chemically sensible way.

## History

Force fields in the `openff-X.Y.Z` line are descended from the [SMIRNOFF99Frosst line of force fields](https://github.com/openforcefield/smirnoff99Frosst/). 
The first official release was made in September 2019 as a result of the Open Force Field Initiative's refitting efforts.

## General versioning guidelines

_Applicable in general to SMIRNOFF-format FFs produced by the Open Force Field Consortium_

Force fields moving forward will be called `name-X.Y.Z`

* `X` denotes some major change in functional form or fitting strategy.
* `Y` is the parameterization epoch / generation, or a minor change that can affect energy.
* `Z` is a bugfix version -- e.g. something we've caught and corrected.  


## Versions
- `v1.0.0 Parsley` : First major forcefield release.

    - `v1.0.1 Parsley `: This bugfix release contains following changes: (1) Addition of monatomic ion `LibraryCharges`.

- `v1.1.0 Parsley `: This minor release contains following changes: (1) Addition of new proper torsions and improper torsions for tetrazole; (2) Corrections to N-N bond rotation periodicity; (3) Removal of redundant periodicity component in `t19`; (4) Addition of three new bond and angle terms, `a22a`, `b14a` and `b36a`.

    - `v1.1.1 Parsley `: This bugfix release contains following changes: (1) Addition of monatomic ion `LibraryCharges`.

- `v1.2.0 Parsley `: This minor release contains following changes: (1) New, carefully designed quantum chemical dataset was utilized in training valence parameters in the force field and (2) Removal of redundancy in `t108` SMIRKS pattern

- `v1.2.1 Parsley `: This bugfix release manually changes two bond force constants to resolve an issue seen in propyne substituents when using hydrogen mass repartitioning with a 4fs timestep. Full details are available at https://github.com/openforcefield/openforcefields/issues/19 . 

- `v1.3.0 Parsley `: This minor release contains a fix of amide-related issues; (1) a poor performance of v1.2 in reproducing amide torsional energy profiles and (2) absence of appropriate torsion parameters for dialkyl amides.

- `v1.3.1-alpha.1 Parsley`: The new force field files in this release are adapted from the openff-1.3.0 release, except that two angle parameters have been reverted to their original values from smirnoff99Frosst 1.1.0, in an attempt to fix sulphonamide geometries.

- `v1.3.1 Parsley`: This release is identical to `v1.3.1-alpha.1 Parsley`.

- `v2.0.0-rc.1 Sage`: This major release candidate contains both refit valence and vdW terms. Full details are available at https://github.com/openforcefield/openff-sage/releases/tag/2.0.0-rc.1

- `v2.0.0-rc.2 Sage`: This major release candidate is identical to `v2.0.0-rc.1 Sage` except that the `angle` value for `a16` has been changed to `180.0 * degree`, as the previous value of `183... * degree` causes geometry optimizers to fail to converge. 

- `v2.0.0 Sage`: This major release contains the same physical parameters as `v2.0.0-rc.2 Sage`, but has the parameter ids changed. For more information see the [openff-sage repository](https://github.com/openforcefield/openff-sage).


#### Acknowledgements

Project based on the
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.0.
