"""
quenchlab_analysis.py
-------------------
Companion analysis script for the QuenchLab heat-treatment simulator.

Model (deliberately simplified for teaching / portfolio purposes -- NOT a
substitute for a real CCT/TTT diagram or Jominy test):

For a given alloy with a "critical cooling rate" CCR (the rate above which
the transformation is fully martensitic), we place four phases at
characteristic cooling rates spaced on a log scale:

    martensite  centered at   CCR
    bainite     centered at   CCR / 6
    pearlite    centered at   CCR / 30
    ferrite     centered at   CCR / 150

Each phase's "affinity" at a given cooling rate is a Gaussian in
log10(cooling rate) space. Normalizing the four affinities to sum to 1 gives
smooth, physically-reasonable phase fractions that mimic the shape of a real
CCT diagram (fast cooling -> martensite, slow cooling -> ferrite/pearlite),
without needing a full diffusion/nucleation simulation.

Final hardness is the phase-fraction-weighted average of each phase's
Rockwell-C hardness for that alloy (from alloys_data.csv).
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "alloys_data.csv"
SIGMA = 0.55  # width of each phase's affinity peak, in log10(cooling rate) units

PHASE_OFFSETS = {
    "martensite": 1.0,
    "bainite": 1 / 6,
    "pearlite": 1 / 30,
    "ferrite": 1 / 150,
}

PHASE_HARDNESS_COL = {
    "martensite": "martensite_HRC",
    "bainite": "bainite_HRC",
    "pearlite": "pearlite_HRC",
    "ferrite": "ferrite_HRC",
}


def phase_fractions(cooling_rate, ccr):
    """Return dict of phase -> fraction (sums to 1) for a given cooling rate."""
    log_cr = np.log10(cooling_rate)
    affinities = {}
    for phase, offset in PHASE_OFFSETS.items():
        center = np.log10(ccr * offset)
        affinities[phase] = np.exp(-0.5 * ((log_cr - center) / SIGMA) ** 2)
    total = sum(affinities.values())
    return {phase: a / total for phase, a in affinities.items()}


def predicted_hardness(row, cooling_rate):
    """Weighted-average HRC for one alloy (a pandas row) at one cooling rate."""
    fracs = phase_fractions(cooling_rate, row["critical_cooling_rate_Ks"])
    return sum(fracs[p] * row[PHASE_HARDNESS_COL[p]] for p in fracs)


def hardness_curve(row, cr_range):
    return np.array([predicted_hardness(row, cr) for cr in cr_range])


def main():
    df = pd.read_csv(DATA_FILE)
    cr_range = np.logspace(-1, 3.3, 200)  # 0.1 to ~2000 K/s

    # --- Plot: hardness vs cooling rate for every alloy ---
    plt.figure(figsize=(9, 6))
    for _, row in df.iterrows():
        curve = hardness_curve(row, cr_range)
        plt.plot(cr_range, curve, label=row["alloy_name"], linewidth=2)

    plt.xscale("log")
    plt.xlabel("Cooling rate (K/s, log scale)")
    plt.ylabel("Predicted hardness (HRC)")
    plt.title("Simplified pseudo-CCT hardness response by alloy")
    plt.legend(fontsize=8, loc="lower right")
    plt.grid(True, which="both", alpha=0.3)
    plt.tight_layout()
    plt.savefig("hardness_vs_cooling_rate.png", dpi=150)
    print("Saved plot: hardness_vs_cooling_rate.png")

    # --- Table: hardness at three representative quench severities ---
    quench_points = {"Furnace cool (~1 K/s)": 1, "Air cool (~10 K/s)": 10, "Oil quench (~80 K/s)": 80,
                      "Water quench (~400 K/s)": 400}

    results = []
    for _, row in df.iterrows():
        entry = {"alloy": row["alloy_name"], "category": row["category"]}
        for label, cr in quench_points.items():
            entry[label] = round(predicted_hardness(row, cr), 1)
        results.append(entry)

    results_df = pd.DataFrame(results)
    results_df.to_csv("hardness_predictions.csv", index=False)
    print("\nPredicted hardness (HRC) at representative quench rates:\n")
    print(results_df.to_string(index=False))
    print("\nSaved table: hardness_predictions.csv")


if __name__ == "__main__":
    main()
