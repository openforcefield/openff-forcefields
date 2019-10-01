# Open Force Fields

[![Build Status](https://travis-ci.com/openforcefield/openforcefields.svg?branch=master)](https://travis-ci.com/openforcefield/openforcefields)

This repository contains force fields released by the [Open Force Field Initiative](https://openforcefield.org)..
These files are in SMIRKS Native Open Force Field (SMIRNOFF) format.
Details about this new format are documented in our recent publication ([doi:10.1021/acs.jctc.8b00640](https://www.doi.org/10.1021/acs.jctc.8b00640) or [bioRxiv](https://doi.org/10.1101/286542)), and the most recent documentation of the specification can be found in the [Open Force Field Toolkit documentation](https://open-forcefield-toolkit.readthedocs.io/en/latest/smirnoff.html).
You can parameterize small molecules with SMIRNOFF using the
`ForceField` class in the [openforcefield toolkit](https://github.com/openforcefield/openforcefield)
for simulations with [OpenMM](http://openmm.org/).

Usage examples can be found in the [openforcefield repository](https://github.com/openforcefield/openforcefield/tree/master/examples).

DOIs for each force field in this repository can be found in the following table:

| Filename | DOI | 
| -------- | --- |
| openff-1.0.0-RC1.offxml | None | 
| openff_unconstrained-1.0.0-RC1.offxml | None | 



## Installation
```bash
conda install -c omnia openforcefields
```

## Use

Installing this package exposes an entry point that makes the `openforcefield-forcefields/offxml` directory easily accessible by other packages in the same python installation. If the [Open Force Field toolkit](https://github.com/openforcefield/openforcefield) is installed, it will automatically detect and use this entry point:

```
>>> from openforcefield.typing.engines.smirnoff import ForceField
>>> ff = ForceField('openff-1.0.0-RC1.offxml') 
```

Otherwise, the entry point can be accessed by querying the `openforcefield.smirnoff_forcefield_directory` entry point group.

```
>>> from pkg_resources import iter_entry_points
>>> for entry_point in iter_entry_points(group='openforcefield.smirnoff_forcefield_directory'):
...     print(entry_point.load()())
```

## What it is

The provided OFFXML (force field) files are successive versions of a general-purpose small molecule force field, written in [the SMIRNOFF format](https://github.com/openforcefield/openforcefield/blob/master/The-SMIRNOFF-force-field-format.md); this force field should cover all or almost all of drug-like chemical space, and illustrate some of the major functionality of the SMIRNOFF format as well as how it simplifies the specification of force field parameters in a compact and chemically sensible way.

## History

Force fields in the `openff-X.Y.Z` line are descended from the [SMIRNOFF99Frosst line of force fields](https://github.com/openforcefield/smirnoff99Frosst/). 
The first official release was made in September 2019 as a result of the Open Force Field Initiative's refitting efforts.

## General versioning guidelines

_Applicable in general to SMIRNOFF-format FFs produced by the Open Force Field Consortium_

Force fields moving forward will be called `name-X.Y.Z`

* `X` denotes some major change in functional form.
* `Y` is the parameterization epoch / generation, or a minor change that can affect energy.
* `Z` is a bugfix version -- e.g. something we've caught and corrected.  



## Versions

## Contributors

Contributors to the relevant .offxml files include:
(Basically everyone in the consortium)

Special thanks go to John D. Chodera (MSKCC) for his initial implementation of `openforcefield` toolkits and the SMIRNOFF format.

Andrea Rizzi (MSKCC) and Jeff Wagner (OFF/UC Irvine) contributed to the Python and Conda infrastructure of this package.

#### Acknowledgements

Project based on the
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.0.
