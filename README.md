# OpenFF Force Fields

[![Build Status](https://github.com/openforcefield/openff-forcefields/workflows/CI/badge.svg)](https://github.com/openforcefield/openff-forcefields/actions?query=branch%3Amain+workflow%3ACI)


This repository contains force fields released by the [Open Force Field Initiative](https://openforcefield.org).
These force fields use the SMIRKS Native Open Force Field (SMIRNOFF) format.
By convention these files use the `.offxml` file extension.
The SMIRNOFF format has a [specification](https://openforcefield.github.io/standards/standards/smirnoff/) and is discussed in a [JCTC publication](https://www.doi.org/10.1021/acs.jctc.8b00640) and associated [pre-print](https://doi.org/10.1101/286542).

The [OpenFF Toolkit](https://github.com/openforcefield/openff-toolkit) provides a reference implementation of the SMIRNOFF format. In particular, the [`ForceField`](https://docs.openforcefield.org/projects/toolkit/en/stable/api/generated/openff.toolkit.typing.engines.smirnoff.forcefield.ForceField.html#openff.toolkit.typing.engines.smirnoff.forcefield.ForceField) class is used to load SMIRNOFF-format force fields and the [`create_openmm_system`](https://docs.openforcefield.org/projects/toolkit/en/stable/api/generated/openff.toolkit.typing.engines.smirnoff.forcefield.ForceField.html#openff.toolkit.typing.engines.smirnoff.forcefield.ForceField.create_openmm_system) method enables the parametrization of small molecules into OpenMM objects.

Detailed usage examples can be found in the [OpenFF Toolkit repository](https://github.com/openforcefield/openff-toolkit/tree/main/examples).

Each mainline force field is currently available in two forms -- both with and without bond constraints to hydrogen. The default version of each force field (i.e. `openff-2.0.0.offxml`) is suitable for typical molecular dynamics simulations with constrained bonds to hydrogen. The "unconstrained" version of each force field (i.e. `openff_unconstrained-2.0.0.offxml`) should be used when single-point energies are a major concern (e.g. geometry optimizations) and when comparing the force field to QM data.

This repository may also contain other useful force fields, data, or utilities, separate from mainline OpenFF force fields. More information on those can be found in the `docs/` directory in this repository.

## How to cite

To cite the **Parsley** line of force fields (`openff-1.Y.Z`) please use [this citation](https://doi.org/10.1021/acs.jctc.1c00571).

To cite the **Sage** line of force fields (`openff-2.Y.Z`) please use [this citation](https://pubs.acs.org/doi/10.1021/acs.jctc.3c00039).

Optionally, consider also citing the version-specific Zenodo DOI for the particular force field from the table below.

Details for each force field in this repository can be found on our [website](https://openforcefield.org/force-fields/force-fields/) or in the following table:

| Filename                                    | Fitting repo | DOI                                                                                                       | FF line | Release Date  | Major format changes? |
|---------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------|---------|---------------|-----------------------|
| `openff-2.2.1.offxml`                   | [repo](https://github.com/openforcefield/sage-2.2.1/releases/tag/2.2.1) |                                                                                                           | Sage    | September 11, 2024 | No                    |
| `openff_unconstrained-2.2.1.offxml`     | [repo](https://github.com/openforcefield/sage-2.2.1/releases/tag/2.2.1) |                                                                                                           | Sage    | September 11, 2024 | No                    |
| `openff-2.2.1-rc1.offxml`                   | [repo](https://github.com/openforcefield/sage-2.2.1/releases/tag/2.2.1-rc1) |                                                                                                           | Sage    | July 22, 2024 | No                    |
| `openff_unconstrained-2.2.1-rc1.offxml`     | [repo](https://github.com/openforcefield/sage-2.2.1/releases/tag/2.2.1-rc1) |                                                                                                           | Sage    | July 22, 2024 | No                    |
| `openff-2.2.0.offxml`                       | [repo](https://github.com/openforcefield/sage-2.2.0/releases/tag/v2.2.0) | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10995191.svg)](https://doi.org/10.5281/zenodo.10995191) | Sage    | April 18, 2024 | No                    |
| `openff_unconstrained-2.2.0.offxml`         | [repo](https://github.com/openforcefield/sage-2.2.0/releases/tag/v2.2.0) | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10995191.svg)](https://doi.org/10.5281/zenodo.10995191) | Sage    | April 18, 2024 | No                    |
| `openff-2.2.0-rc1.offxml`                   | [repo](https://github.com/openforcefield/sage-2.2.0/releases/tag/v2.2.0-rc1) |                                                                                                           | Sage    | March 6, 2024 | No                    |
| `openff_unconstrained-2.2.0-rc1.offxml`     | [repo](https://github.com/openforcefield/sage-2.2.0/releases/tag/v2.2.0-rc1) |                                                                                                           | Sage    | March 6, 2024 | No                    |
| `openff-2.1.1.offxml`                       | None | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10553473.svg)](https://doi.org/10.5281/zenodo.10553473) | Sage    | Jan 22, 2024  | No                    |
| `openff_unconstrained-2.1.1.offxml`         | None | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10553473.svg)](https://doi.org/10.5281/zenodo.10553473) | Sage    | Jan 22, 2024  | No                    |
| `tip5p-1.0.0.offxml`                        | None | see `docs/water-models.md`                                                                                | Ports   | Nov 6, 2023   | No                    |
| `spce-1.0.0.offxml`                         | None | see `docs/water-models.md`                                                                                | Ports   | Nov 6, 2023   | No                    |
| `tip4p_ew-1.0.0.offxml`                     | None | see `docs/water-models.md`                                                                                | Ports   | Nov 6, 2023   | No                    |
| `opc-1.0.2.offxml`                          | None | see `docs/water-models.md`                                                                                | Ports   | Aug 9, 2023   | No                    |
| `opc3-1.0.1.offxml`                         | None | see `docs/water-models.md`                                                                                | Ports   | Aug 9, 2023   | No                    |
| `tip3p_fb-1.1.1.offxml`                     | None | see `docs/water-models.md`                                                                                | Ports   | Aug 9, 2023   | No                    |
| `tip3p-1.0.1.offxml`                        | None | see `docs/water-models.md`                                                                                | Ports   | Aug 9, 2023   | No                    |
| `tip4p_fb-1.0.1.offxml`                     | None | see `docs/water-models.md`                                                                                | Ports   | Aug 9, 2023   | No                    |
| `opc-1.0.1.offxml`                          | None | see `docs/water-models.md`                                                                                | Ports   | May 24, 2023  | No                    |
| `opc3-1.0.0.offxml`                         | None | see `docs/water-models.md`                                                                                | Ports   | May 24, 2023  | No                    |
| `tip3p_fb-1.1.0.offxml`                     | None | see `docs/water-models.md`                                                                                | Ports   | May 24, 2023  | No                    |
| `tip4p_fb-1.0.0.offxml`                     | None | see `docs/water-models.md`                                                                                | Ports   | May 24, 2023  | No                    |
| `openff-2.1.0.offxml`                       | [repo](https://github.com/openforcefield/sage-2.1.0) | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7889050.svg)](https://doi.org/10.5281/zenodo.7889050) | Sage    | May 2, 2023   | No                    |
| `openff_unconstrained-2.1.0.offxml`         | [repo](https://github.com/openforcefield/sage-2.1.0) | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7889050.svg)](https://doi.org/10.5281/zenodo.7889050) | Sage    | May 2, 2023   | No                    |
| `opc-1.0.0.offxml`                          | None | see `docs/water-models.md`                                                                                | Ports   | May 1, 2023   | No                    |
| `openff-2.1.0-rc.1.offxml`                  | [repo](https://github.com/openforcefield/sage-2.1.0) |                                                                                                           | Sage    | Apr 10, 2023  | No                    |
| `openff_unconstrained-2.1.0-rc.1.offxml`    | [repo](https://github.com/openforcefield/sage-2.1.0) |                                                                                                           | Sage    | Apr 10, 2023  | No                    |
| `tip3p_fb-1.0.0.offxml`                     | None | see `docs/water-models.md`                                                                                | Ports   | Feb 27, 2023  | No                    |
| `tip3p-1.0.0.offxml`                        | None | see `docs/water-models.md`                                                                                | Ports   | Feb 27, 2023  | No                    |
| `openff-2.0.0.offxml`                       | [repo](https://github.com/openforcefield/openff-sage/tree/2.0.0-rc.1) | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5214478.svg)](https://doi.org/10.5281/zenodo.5214478) | Sage    | Aug 16, 2021  | No                    |
| `openff_unconstrained-2.0.0.offxml`         | [repo](https://github.com/openforcefield/openff-sage/tree/2.0.0-rc.1) | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5214478.svg)](https://doi.org/10.5281/zenodo.5214478) | Sage    | Aug 16, 2021  | No                    |
| `openff-2.0.0-rc.2.offxml`                  | None | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5156698.svg)](https://doi.org/10.5281/zenodo.5156698) | Sage    | Aug 3, 2021   | No                    |
| `openff_unconstrained-2.0.0-rc.2.offxml`    | None | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5156698.svg)](https://doi.org/10.5281/zenodo.5156698) | Sage    | Aug 3, 2021   | No                    |
| `openff-2.0.0-rc.1.offxml`                  | [repo](https://github.com/openforcefield/openff-sage/releases/tag/2.0.0-rc.1) | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5009196.svg)](https://doi.org/10.5281/zenodo.5009196) | Sage    | June 21, 2021 | No                    |
| `openff_unconstrained-2.0.0-rc.1.offxml`    | [repo](https://github.com/openforcefield/openff-sage/releases/tag/2.0.0-rc.1) | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5009196.svg)](https://doi.org/10.5281/zenodo.5009196) | Sage    | June 21, 2021 | No                    |
| `openff-1.3.1.offxml`                       | None | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5009058.svg)](https://doi.org/10.5281/zenodo.5009058) | Parsley | June 21, 2021 | No                    |
| `openff_unconstrained-1.3.1.offxml`         | None | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5009058.svg)](https://doi.org/10.5281/zenodo.5009058) | Parsley | June 21, 2021 | No                    |
| `openff-1.3.1-alpha.1.offxml`               | None | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4697390.svg)](https://doi.org/10.5281/zenodo.4697390) | Parsley | Apr 15, 2021  | No                    |
| `openff_unconstrained-1.3.1-alpha.1.offxml` | None | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4697390.svg)](https://doi.org/10.5281/zenodo.4697390) | Parsley | Apr 15, 2021  | No                    |
| `openff-1.3.0.offxml`                       | [repo](https://github.com/openforcefield/openforcefield-forcebalance/releases/tag/v1.3.0) | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4118484.svg)](https://doi.org/10.5281/zenodo.4118484) | Parsley | Oct 21, 2020  | No                    |
| `openff_unconstrained-1.3.0.offxml`         | [repo](https://github.com/openforcefield/openforcefield-forcebalance/releases/tag/v1.3.0) | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4118484.svg)](https://doi.org/10.5281/zenodo.4118484) | Parsley | Oct 21, 2020  | No                    |
| `openff-1.2.1.offxml`                       | None | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4021623.svg)](https://doi.org/10.5281/zenodo.4021623) | Parsley | Sep 9, 2020   | No                    |
| `openff_unconstrained-1.2.1.offxml`         | None | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4021623.svg)](https://doi.org/10.5281/zenodo.4021623) | Parsley | Sep 9, 2020   | No                    |
| `openff-1.2.0.offxml`                       | [repo](https://github.com/openforcefield/openforcefield-forcebalance/releases/tag/v1.2.0) | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3872244.svg)](https://doi.org/10.5281/zenodo.3872244) | Parsley | May 29, 2020  | No                    |
| `openff_unconstrained-1.2.0.offxml`         | [repo](https://github.com/openforcefield/openforcefield-forcebalance/releases/tag/v1.2.0) | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3872244.svg)](https://doi.org/10.5281/zenodo.3872244) | Parsley | May 29, 2020  | No                    |
| `openff-1.1.1.offxml`                       | None | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3751818.svg)](https://doi.org/10.5281/zenodo.3751818) | Parsley | Apr 14, 2020  | No                    |
| `openff_unconstrained-1.1.1.offxml`         | None | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3751818.svg)](https://doi.org/10.5281/zenodo.3751818) | Parsley | Apr 14, 2020  | No                    |
| `openff-1.1.0.offxml`                       | [repo](https://github.com/openforcefield/openforcefield-forcebalance/releases/tag/v1.1.0) | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3695094.svg)](https://doi.org/10.5281/zenodo.3695094) | Parsley | Mar 3, 2020   | No                    |
| `openff_unconstrained-1.1.0.offxml`         | [repo](https://github.com/openforcefield/openforcefield-forcebalance/releases/tag/v1.1.0) | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3695094.svg)](https://doi.org/10.5281/zenodo.3695094) | Parsley | Mar 3, 2020   | No                    |
| `openff-1.0.1.offxml`                       | None | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3751812.svg)](https://doi.org/10.5281/zenodo.3751812) | Parsley | Apr 14, 2020  | No                    |
| `openff_unconstrained-1.0.1.offxml`         | None | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3751812.svg)](https://doi.org/10.5281/zenodo.3751812) | Parsley | Apr 14, 2020  | No                    |
| `openff-1.0.0.offxml`                       | [repo](https://github.com/j-wags/release-1-fitting/releases/tag/v1.0.0-RC2) | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3483227.svg)](https://doi.org/10.5281/zenodo.3483227) | Parsley | Oct 12, 2019  | No                    |
| `openff_unconstrained-1.0.0.offxml`         | [repo](https://github.com/j-wags/release-1-fitting/releases/tag/v1.0.0-RC2) | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3483227.svg)](https://doi.org/10.5281/zenodo.3483227) | Parsley | Oct 12, 2019  | No                    |
| `openff-1.0.0-RC2.offxml`                   | [repo](https://github.com/openforcefield/openforcefield-forcebalance/releases/tag/v0.0.9) | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3473554.svg)](https://doi.org/10.5281/zenodo.3473554) | None    | Oct 4, 2019   | No                    |
| `openff_unconstrained-1.0.0-RC2.offxml`     | [repo](https://github.com/openforcefield/openforcefield-forcebalance/releases/tag/v0.0.9) | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3473554.svg)](https://doi.org/10.5281/zenodo.3473554) | None    | Oct 4, 2019   | No                    |
| `openff-1.0.0-RC1.offxml`                   | None | None                                                                                                      | None    | Oct 4, 2019   | N/A                   |
| `openff_unconstrained-1.0.0-RC1.offxml`     | None | None                                                                                                      | None    | Oct 4, 2019   | N/A                   |



## Installation

```shell
conda install -c conda-forge openff-forcefields
```

## Use

Installing this package exposes an [entry point](https://packaging.python.org/en/latest/specifications/entry-points/) that makes the `openforcefields/offxml/` directory easily accessible by other packages in the same Python installation. If the [OpenFF Toolkit](https://docs.openforcefield.org/projects/toolkit/en/stable/) is installed, it will automatically detect and use this entry point when loading OFFXML files:

```python
from openff.toolkit.typing.engines.smirnoff import ForceField
ff = ForceField('openff-2.0.0.offxml')
```

Otherwise, the entry point can be [accessed by querying](https://docs.python.org/3/library/importlib.metadata.html#entry-points) the `openforcefield.smirnoff_forcefield_directory` entry point group.

```python
from importlib.metadata import entry_points

for entry_point in iter_entry_points(group='openforcefield.smirnoff_forcefield_directory'):
    print(entry_point.load()())
```

For convenience, the OpenFF Toolkit also has a standalone function [`get_available_force_fields`](https://docs.openforcefield.org/projects/toolkit/en/stable/api/generated/openff.toolkit.typing.engines.smirnoff.forcefield.get_available_force_fields.html#openff.toolkit.typing.engines.smirnoff.forcefield.get_available_force_fields) that lists the force fields discered by this entry point group:

```pycon
>>> from openff.toolkit.typing.engines.smirnoff.forcefield import get_available_force_fields
>>> get_available_force_fields()
['smirnoff99Frosst-1.0.2.offxml', 'smirnoff99Frosst-1.0.0.offxml', 'smirnoff99Frosst-1.1.0.offxml', 'smirnoff99Frosst-1.0.4.offxml', 'smirnoff99Frosst-1.0.8.offxml', 'smirnoff99Frosst-1.0.6.offxml', 'smirnoff99Frosst-1.0.3.offxml', 'smirnoff99Frosst-1.0.1.offxml', 'smirnoff99Frosst-1.0.5.offxml', 'smirnoff99Frosst-1.0.9.offxml', 'smirnoff99Frosst-1.0.7.offxml', 'ff14sb_off_impropers_0.0.2.offxml', 'ff14sb_0.0.1.offxml', 'ff14sb_0.0.3.offxml', 'ff14sb_off_impropers_0.0.1.offxml', 'ff14sb_off_impropers_0.0.3.offxml', 'ff14sb_0.0.2.offxml', 'openff-1.0.1.offxml', 'openff-1.1.1.offxml', 'openff-1.0.0-RC1.offxml', 'openff-1.2.0.offxml', 'openff-1.3.0.offxml', 'openff_unconstrained-2.0.0-rc.1.offxml', 'openff_unconstrained-1.3.1.offxml', 'openff_unconstrained-1.2.1.offxml', 'openff-2.0.0-rc.2.offxml', 'openff_unconstrained-1.0.0-RC2.offxml', 'openff_unconstrained-1.1.0.offxml', 'openff_unconstrained-1.0.0.offxml', 'openff-2.0.0.offxml', 'openff_unconstrained-2.0.0.offxml', 'openff_unconstrained-2.0.0-rc.2.offxml', 'openff-1.1.0.offxml', 'openff-1.0.0.offxml', 'openff-1.0.0-RC2.offxml', 'openff-1.3.1.offxml', 'openff-1.2.1.offxml', 'openff-1.3.1-alpha.1.offxml', 'openff_unconstrained-1.0.0-RC1.offxml', 'openff_unconstrained-1.2.0.offxml', 'openff_unconstrained-1.3.0.offxml', 'openff-2.0.0-rc.1.offxml', 'openff_unconstrained-1.0.1.offxml', 'openff_unconstrained-1.1.1.offxml', 'openff_unconstrained-1.3.1-alpha.1.offxml']
```

## History

Force fields in the Parsley and Sage lines are descended from the [SMIRNOFF99Frosst line of force fields](https://github.com/openforcefield/smirnoff99Frosst/).
The first official release (`openff-1.0.0.offxml`, code name "Parsley") was made in September 2019 as a result of the Open Force Field Initiative's refitting efforts.

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

- `v1.2.1 Parsley `: This bugfix release manually changes two bond force constants to resolve an issue seen in propyne substituents when using hydrogen mass repartitioning with a 4fs timestep. Full details are available at https://github.com/openforcefield/openforcefields/issues/19.

- `v1.3.0 Parsley `: This minor release contains a fix of amide-related issues; (1) a poor performance of v1.2 in reproducing amide torsional energy profiles and (2) absence of appropriate torsion parameters for dialkyl amides.

- `v1.3.1-alpha.1 Parsley`: The new force field files in this release are adapted from the openff-1.3.0 release, except that two angle parameters have been reverted to their original values from smirnoff99Frosst 1.1.0, in an attempt to fix sulphonamide geometries.

- `v1.3.1 Parsley`: This release is identical to `v1.3.1-alpha.1 Parsley`.

- `v2.0.0-rc.1 Sage`: This major release candidate contains both refit valence and vdW terms. Full details are available at https://github.com/openforcefield/openff-sage/releases/tag/2.0.0-rc.1

- `v2.0.0-rc.2 Sage`: This major release candidate is identical to `v2.0.0-rc.1 Sage` except that the `angle` value for `a16` has been changed to `180.0 * degree`, as the previous value of `183... * degree` causes geometry optimizers to fail to converge.

- `v2.0.0 Sage`: This major release contains the same physical parameters as `v2.0.0-rc.2 Sage`, but has the parameter ids changed. For more information see the [openff-sage repository](https://github.com/openforcefield/openff-sage).

- `2023.02.1`: This release switches to a calendar-versioning system and adds `tip3p-1.0.0.offxml` and `tip3p-fb-1.0.0.offxml`, as well as `tip3p.offxml` and `tip3p-fb.offxml`, which will always point to the latest files in their respective lines.

- `2023.04.1`: This release adds `openff-2.1.0-rc.1.offxml` Sage 2.1.0 Release Candidate 1, with several small parameter fixes and improvements.

- `2023.05.0`: This release adds the `opc-1.0.0.offxml`, our initial port of the OPC water model.

- `2023.05.1`: This release adds `openff-2.1.0.offxml`, Sage 2.1.0, with identical physics parameters to `openff-2.1.0-rc.1.offxml`.

- `2023.06.0`: This release adds `opc-1.0.1.offxml`, standardizing the use of the string "kilocalorie_per_mole". It also adds `tip3p-fb-1.1.0.offxml`, which fixes a unit error in the geometric constraints and adds additional ion parameters. Finally, it adds `opc3-1.0.0.offxml` and `tip4p_fb-1.0.0.offxml`.

- `2024.01.0`: This release adds `openff-2.1.1.offxml` and `openff_unconstrained-2.1.1.offxml`, Sage 2.1.1, which has identical parameters to Sage 2.1.0 (originally released in version `2023.05.1` of the `openff-forcefields` package) but adds Xe van der Waals parameters from [Tang, K.T., Toennies, J.P. New combining rules for well parameters and shapes of the van der Waals potential of mixed rare gas systems. Z Phys D - Atoms, Molecules and Clusters 1, 91–101 (1986).](https://doi.org/10.1007/BF01384663)

- `2024.03.0`: This release adds `openff-2.2.0-rc1.offxml` and `openff_unconstrained-2.2.0-rc1.offxml`, Sage 2.2.0 Release Candidate 1, which modifies some small ring internal angles and remedies issues with sulfamide geometries.

- `2024.04.0`: This release adds `openff-2.2.0.offxml` and `openff_unconstrained-2.2.0.offxml`, Sage 2.2.0, with identical parameters to `openff-2.2.0-rc1.offxml`.

- `2024.07.0`: This release adds `openff-2.2.1-rc1.offxml` and `openff_unconstrained-2.2.1-rc1.offxml`, which contains re-fit valence parameters where linear angles have been pinned to linear equilibrium values.

- `2024.09.0` This release adds the Sage 2.2.1 force field with `openff-2.2.1.offxml` and `openff_unconstrained-2.2.1.offxml`, with identifical parameters to 2.2.1-rc1.

#### Acknowledgements

Project based on the
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.0.
