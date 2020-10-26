# Canary tests
### Scripts and data files used for canary tests.
These tests are designed to be quick checks for basic behavior to safeguard
against releasing bad force fields. These are **not** rigorous benchmarks or
thorough tests of correct behavior across general uses.

For implementation, see .github/workflows/canary.yaml

This is stored in a directory separate from `openforcefields/tests` because
these are **not** unit tests. If you intended to run the test suite for the
`openforcefields` package, point `pytest` to the unit test directory:

```python3
pytest -v openforcefields/tests/
```

### Data sources

* `data/coverage.smi`: Seeded from [here](https://raw.githubusercontent.com/openforcefield/open-forcefield-data/master/Utilize-All-Parameters/selected/chosen.smi). Molecules that do not type and/or fail with `openff-1.3.0` were commented out (10/26/20).
* `data/propynes.smi`: Curated from [reported HMR failure](https://github.com/openforcefield/openforcefields/issues/19)

### Scripts

* `scripts/run_hmr.py`: Runs short (10 ps) HMR simulations with a 4 fs timestep
