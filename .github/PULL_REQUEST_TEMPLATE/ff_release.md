---
name: Force field release
about: Release a force field.

---

This PR adds ...

Working repo link:

Release link:

### Checklist

- [ ] Open a new branch or fork on this repo.
- [ ] Add the new force field file to the branch.
- [ ] Update the date in the FF files
- [ ] Update the authors in the `.zenodo.json` file - Details and validation info can be found [here](https://developers.zenodo.org/#add-metadata-to-your-github-repository-release)
- [ ] Check that regular and `unconstrained` forcefields have constraints applied and absent, respectively
- [ ] Ensure that there are no cosmetic attributes
- [ ] Visually inspect for whitespace irregularities, etc. (Importantly: Tabs should be turned into 4 spaces)
- [ ] Ensure that comments and authors are up to date
- [ ] Ensure that `Bonds` `version="0.4"`, `fractional_bondorder_method="AM1-Wiberg"` and `fractional_bondorder_interpolation="linear"`
- [ ] Ensure that `ProperTorsions` `version="0.4"`, `fractional_bondorder_method="AM1-Wiberg"` and `fractional_bondorder_interpolation="linear"`
- [ ] Ensure the Electrostatics `scale14` value is `0.8333333333` (10 sig figs). Change it by hand if more 3's need to be added.
- [ ] Add monoatomic ion charges to the FF, just before the `ToolkitAM1BCC` tag
- [ ] Ensure that new FFs are loadable in newest stable release of OFF toolkit
- [ ] Draft a "version" description at the bottom of the README file in a branch or fork. _A zenodo DOI link is not necessary at this stage_
- [ ] Prepare the fitting tarball (or other record of the files and/or code that produced the new parameters), which is often associated with a release like [this](https://github.com/openforcefield/openforcefield-forcebalance/releases/tag/v1.0.0-RC2). This collection of assets should include:
    - [ ] a static copy of the data (QM and phys prop) used for the fit
    - [ ] a static copy of the scripts used for the fit
    - [ ] A file containing the environment used for the fit (like the output of `conda env export`)
    - [ ] Generally, anything else required to re-run the exact fit that was performed
- [ ] Open a PR to main, for example [this](https://github.com/openforcefield/openforcefields/pull/6)
