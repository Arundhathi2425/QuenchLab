# QuenchLab — Heat Treatment Simulator

A companion project to **Alloy Atlas**, extending the "materials selector" idea from
static properties into **process parameters**: how cooling rate during heat treatment
changes an alloy's phase mix and resulting hardness.

## What's in here

| File | What it does | Skills shown |
|---|---|---|
| `index.html` | Interactive simulator: pick an alloy, drag a cooling-rate slider (or hit a quench preset), see live phase-fraction bars and a hardness-vs-cooling-rate curve | HTML, CSS, JavaScript (Chart.js, logarithmic scales, live UI state) |
| `quenchlab_analysis.py` | Same phase-fraction model in Python; batch-computes hardness curves for all 10 alloys, exports a comparison plot and a CSV of predicted hardness at four standard quench severities | Python, pandas, matplotlib, numerical modeling |
| `alloys_data.csv` | Dataset: 10 alloys (plain-carbon, low-alloy, tool steel, stainless, titanium) with critical cooling rate and phase-specific hardness (HRC) | Data structuring, hardenability concepts |

## The model (and its limits)

This is a **simplified teaching model**, not a substitute for a measured CCT/TTT
diagram or Jominy end-quench test. It captures the right qualitative behavior —
fast cooling favors martensite, alloying additions shift the "nose" of the curve to
slower cooling rates (hardenability) — using a lightweight approximation instead of
a full nucleation-and-growth simulation:

- Each phase (martensite, bainite, pearlite, ferrite) is assigned a characteristic
  cooling rate, spaced on a log scale relative to the alloy's **critical cooling
  rate (CCR)** — the rate above which transformation is fully martensitic.
- Phase "affinity" at a given cooling rate is a Gaussian in log-cooling-rate space,
  normalized across the four phases so fractions sum to 100%.
- Final hardness is the fraction-weighted average of each phase's HRC for that alloy.

This connects directly to concepts from **Metallurgical Thermodynamics and Kinetics**
(transformation kinetics, JMAK-style reasoning) and **Deformation Behaviour of
Materials** (how microstructure sets mechanical response).

## Running it

**Web app:** open `index.html` in any browser — no build step, no server.

**Python script:**
```bash
pip install pandas matplotlib
python quenchlab_analysis.py
```
Outputs `hardness_vs_cooling_rate.png` and `hardness_predictions.csv`.

## Possible extensions

- Replace the Gaussian-affinity approximation with real JMAK (Avrami) kinetics
  fit to published TTT data for one alloy, as a validation case study
- Add a second slider for austenitizing temperature and grain size, since both
  shift hardenability
- Import real Jominy end-quench test data (if available from a lab course) and
  overlay measured vs. predicted hardness
- Extend the CSV/model to include tempering behavior (hardness vs. tempering
  temperature and time) for a full quench-and-temper simulator

## Suggested CV bullet points

- *Built an interactive heat-treatment simulator (HTML/JS + Chart.js) modeling
  phase-fraction evolution and resulting hardness as a function of cooling rate,
  grounded in CCT-diagram concepts from metallurgical kinetics coursework.*
- *Implemented a Python/pandas phase-fraction model to batch-predict hardness
  across 10 alloy systems at standard quench severities, exporting comparison
  plots and CSV summaries.*
