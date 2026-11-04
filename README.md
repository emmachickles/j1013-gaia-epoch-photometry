# Gaia epoch photometry of ATLAS J1013−4516

A runnable Jupyter notebook with the Gaia and ATLAS light curves, timing data, figures, and a new seasonal Gaia timing estimator for the 8.56-minute eclipsing binary ATLAS J1013−4516. Prepared for the MIT Gaia DR4 Warm Up Workshop, November 5–6, 2026.

**[Open the executed notebook](j1013_gaia_figures.ipynb).** All science inputs are bundled; Run All works offline. No Box account, original analysis repository, GPU, or LCURVE executable is required.

![Gaia and ATLAS fold](figures/j1013_gaia_atlas_fold.png)

## What it does

- Displays 54 processed Gaia epoch-photometry measurements.
- Cleans the 2,128-row ATLAS input using the source analysis recipe (1,946 rows retained), folds both surveys on the published ephemeris, and exports the 50-bin curves.
- Provides all 15 stored timing epochs and a separate 12-row non-Gaia timing table, with source-row IDs and documented instrument assignments.
- Reproduces the backed-up timing-table O–C fit.
- **Measures three new Gaia seasonal timings directly from the individual fluxes** (20/19/15 points), using a saved high-speed g-band LCURVE template, free seasonal shifts, and a phase evolution fitted to non-Gaia timings only.
- Exports profile-likelihood diagnostics, zero-versus-44-second averaging and harmonic-baseline sensitivities, and an O–C using the newly measured Gaia epochs.

## Scientific status

The published result is **Pdot = (−1.60 ± 0.07) × 10⁻¹² s/s**, from [Chickles et al. (2026), ApJ 1000, 237](https://doi.org/10.3847/1538-4357/ae4871). This repository separates it from two other calculations:

| Calculation | Result / status |
|---|---|
| Refit of the stored 15-row timing table | (−1.725 ± 0.056) × 10⁻¹² s/s; the source table/fit version differs from the paper's quoted result. |
| New flux-based Gaia epochs plus the other timings | Approximately (−1.65 ± 0.07) × 10⁻¹² s/s, with a **conditional formal error**. An exploratory remeasurement, not a validated replacement for the published analysis. |

**The fixed g-to-G template fits the Gaia seasons poorly** (reduced chi-square about 16–34). The notebook inflates local profile errors using residual scatter, but this does not calibrate template systematics. Allowing an extra harmonic baseline switches the preferred eclipse labeling by about half a cycle in two seasons. The supplied Gaia file has no header, original quality flags, or verified ingestion/time-scale record; times are used as stored. The 44-second boxcar is a response assumption checked against zero extra averaging. Two nearly simultaneous input rows cannot be checked for independence without transit IDs. These limitations are exposed in the notebook and sensitivity table; the apparent agreement of the new Pdot with the paper does not establish exact reproduction.

The original Gaia download, initial filtering, and original three-season timing procedure were not recovered. The new estimator is fully specified here. The saved physical-template table is an input; this notebook does not reproduce its original physical-model fit or raw-image reductions.

## Run

Use Python 3.12 (tested):

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter lab j1013_gaia_figures.ipynb
```

Or execute every cell non-interactively in the active Python environment:

```bash
python scripts/run_notebook.py
```

All input files live in `data/`. Run All regenerates PDF/PNG figures in `figures/` and CSV/JSON products in `tables/`. It does not modify input data. `data/source_manifest.json` records original analysis-relative filenames and SHA256 checksums. Absolute workstation and private backup paths are not included.

## Main products

| Product | File |
|---|---|
| Gaia + ATLAS fold | `figures/j1013_gaia_atlas_fold.pdf` |
| New Gaia timing profiles | `figures/j1013_gaia_timing_profiles.pdf` |
| O–C with new Gaia measurements | `figures/j1013_oc_remeasured_gaia.pdf` |
| Measured Gaia epochs | `tables/gaia_measured_timing_epochs.csv` |
| Model/response sensitivities | `tables/gaia_timing_sensitivity.csv` |
| Folded light curves | `tables/gaia_atlas_folded_50bins.csv` |
| Non-Gaia timing input | `data/other_timing_epochs.csv` |

Instrument labels in the original headerless timing table were reconstructed from source figure annotations and observing-era grouping. Its last column is reciprocal timing uncertainty, not an O–C error; the notebook uses the supplied seconds-unit error column. Its day-unit errors were rounded. The ATLAS/Gaia overlay uses an affine rescaling of ATLAS to Gaia's folded interquartile range and is not an absolute amplitude/color comparison. Three displayed cycles repeat the same measurements.

## Citation and attribution

For the binary and published scientific result, cite:

> Chickles, E. T., Chakraborty, J., Burdge, K. B., et al. 2026, “An Eclipsing 8.56 Minutes Orbital Period Mass-transferring Binary,” The Astrophysical Journal, 1000, 237. DOI: [10.3847/1538-4357/ae4871](https://doi.org/10.3847/1538-4357/ae4871).

This work uses data from ESA's Gaia mission, processed by the Gaia Data Processing and Analysis Consortium (DPAC). DPAC funding is provided by national institutions, especially those participating in the Gaia Multilateral Agreement. See [Gaia](https://www.cosmos.esa.int/gaia) and [DPAC](https://www.cosmos.esa.int/web/gaia/dpac/consortium). ATLAS survey photometry and the author's processed high-speed/timing products are included for reproducibility of this specific analysis.

Source code and notebook code cells: [MIT License](LICENSE). Author-created data products, notebook prose, and figures: [CC BY 4.0](LICENSE-DATA). Upstream Gaia/ATLAS data retain their applicable terms and attribution requirements. `CITATION.cff` supplies repository citation metadata.
