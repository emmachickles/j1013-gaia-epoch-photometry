# Gaia epoch photometry of ATLAS J1013−4516

Light curves, timing data, and a Jupyter notebook for the 8.56-minute eclipsing binary ATLAS J1013−4516. Prepared for the MIT Gaia DR4 Warm Up Workshop, November 5–6, 2026.

**[Open the executed notebook](j1013_gaia_figures.ipynb)** to view the light curves, measure seasonal Gaia timings, and construct observed-minus-calculated (O–C) diagrams. Input data are included in `data/`.

![Gaia and ATLAS fold](figures/j1013_gaia_atlas_fold.png)

## Analysis

The notebook contains 54 processed Gaia measurements, ATLAS photometry, a high-speed g-band light-curve template, and 15 timing epochs. It:

- Applies the original ATLAS cleaning and phase-folding recipe and exports the 50-bin Gaia/ATLAS comparison.
- Fits a quadratic ephemeris to the supplied timing table.
- Remeasures Gaia timings in three seasons containing 20, 19, and 15 measurements, with free seasonal shifts relative to an ephemeris fitted to the 12 non-Gaia epochs.
- Examines profile likelihoods, exposure averaging, and waveform sensitivity, then constructs an O–C using the remeasured Gaia epochs.

## Interpretation

The published period derivative is **Pdot = (−1.60 ± 0.07) × 10⁻¹² s/s** ([Chickles et al. 2026](https://doi.org/10.3847/1538-4357/ae4871)). The notebook distinguishes this from:

| Calculation | Pdot (10⁻¹² s/s) |
|---|---|
| Fit to the supplied timing table | −1.725 ± 0.056 |
| Fit using remeasured Gaia epochs | −1.65 ± 0.07, conditional formal uncertainty |

The difference between the supplied-table fit and the published value remains unresolved. The phase-folded comparison uses the published ephemeris.

**The Gaia remeasurements are exploratory.** The transferred g-band template fits poorly (reduced χ² ≈ 16–34), and allowing an additional harmonic baseline changes the preferred eclipse labeling by about half a cycle in two seasons. Residual-scaled profile errors describe the local fit; they do not capture these waveform uncertainties.

The processed Gaia file lacks the original quality flags and a verified time-scale conversion record. Times are used as supplied. The nominal 44-second boxcar response is an assumption, with zero additional averaging tested as a sensitivity check. These issues, the nearly simultaneous pair of measurements, and the unpropagated uncertainty in within-season phase evolution are discussed alongside the timing fits. Agreement with the published Pdot does not validate the remeasurement procedure.

## Run

Tested with Python 3.12:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter lab j1013_gaia_figures.ipynb
```

To execute all cells from the command line:

```bash
python scripts/run_notebook.py
```

Run All regenerates PDF/PNG figures in `figures/` and CSV/JSON products in `tables/`. Original input filenames and SHA256 checksums are recorded in `data/source_manifest.json`.

## Main products

| Product | File |
|---|---|
| Gaia/ATLAS fold | `figures/j1013_gaia_atlas_fold.pdf` |
| Gaia timing profiles | `figures/j1013_gaia_timing_profiles.pdf` |
| O–C with remeasured Gaia epochs | `figures/j1013_oc_remeasured_gaia.pdf` |
| Remeasured Gaia epochs | `tables/gaia_measured_timing_epochs.csv` |
| Timing sensitivities | `tables/gaia_timing_sensitivity.csv` |
| Folded light curves | `tables/gaia_atlas_folded_50bins.csv` |
| Non-Gaia timing input | `data/other_timing_epochs.csv` |

The notebook documents the reconstructed instrument labels and timing-error columns. The Gaia/ATLAS overlay rescales ATLAS fluxes to Gaia's folded interquartile range; it compares waveform shapes rather than absolute amplitudes. The three plotted cycles repeat the same data.

## Citation and attribution

For the binary and published result, cite:

> Chickles, E. T., Chakraborty, J., Burdge, K. B., et al. 2026, “An Eclipsing 8.56 Minutes Orbital Period Mass-transferring Binary,” The Astrophysical Journal, 1000, 237. DOI: [10.3847/1538-4357/ae4871](https://doi.org/10.3847/1538-4357/ae4871).

This work uses data from ESA's [Gaia mission](https://www.cosmos.esa.int/gaia), processed by the [Gaia Data Processing and Analysis Consortium (DPAC)](https://www.cosmos.esa.int/web/gaia/dpac/consortium). DPAC funding is provided by national institutions, especially those participating in the Gaia Multilateral Agreement. ATLAS survey photometry and author-provided high-speed and timing products support the analysis.

Code: [MIT License](LICENSE). Author-created data products, prose, and figures: [CC BY 4.0](LICENSE-DATA). Upstream Gaia/ATLAS data retain their applicable terms and attribution requirements. Repository citation metadata are in `CITATION.cff`.
