# Canary tests
### Scripts and data files used for canary tests.
These tests are designed to be quick checks for basic behavior to safeguard
against releasing bad force fields. These are **not** rigorous benchmarks or
thorough tests of correct behavior across general uses.

This is stored in a directory separate from `openforcefields/tests` because
these are **not** unit tests

For implementation, see .github/workflows/canary.yaml

### Data sources

* `data/coverage.smi`: Seeded from [here](https://raw.githubusercontent.com/openforcefield/open-forcefield-data/master/Utilize-All-Parameters/selected/chosen.smi)
* `data/propynes.smi`: Curated from [reported HMR failure](https://github.com/openforcefield/openforcefields/issues/19)

### Scripts

* `scripts/run_hmr.py`: Runs short (10 ps) HMR simulations with a 4 fs timestep
