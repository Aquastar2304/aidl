"""
22AIE304 / Card I2 (Team 1) - the five record-random audit partitions of Annex D6.

Annex D6, verbatim:
    "For audit seeds 101-105, randomly permute eligible record IDs, assign
     80% train / 10% validation / 10% test (floor counts for train/validation),
     and retain whole records. ... Report patient-ID intersections and the
     fraction of test records whose patient is in training."

This script only BUILDS and DESCRIBES the partitions. No model is fitted here.
D6 requires the official models to be fitted and all choices locked before any
audit training; partition bookkeeping is not training and carries no such order.

The annex fixes the seeds and the proportions but not the permutation engine, so
the engine is declared here and in the readiness note: numpy.random.default_rng
(PCG64), permuting eligible ecg_id in ascending order.

Usage: python -I 05_audit_partitions.py <out_dir>
"""
import json
import os
import sys

import numpy as np
import pandas as pd

OUT = os.path.abspath(sys.argv[1])
SEEDS = [101, 102, 103, 104, 105]
SUPER = ["NORM", "MI", "STTC", "CD", "HYP"]

ids = pd.read_csv(os.path.join(OUT, "I2_official_split_ids.csv"), index_col="ecg_id")
ids = ids.sort_index()
n = len(ids)
n_tr = int(np.floor(0.8 * n))
n_va = int(np.floor(0.1 * n))
n_te = n - n_tr - n_va
print("eligible records %d  ->  audit train %d / val %d / test %d" % (n, n_tr, n_va, n_te))

ecg = ids.index.to_numpy()
pat = ids["patient_id"].to_numpy()
rows, summary = [], []

for seed in SEEDS:
    rng = np.random.default_rng(seed)
    perm = rng.permutation(n)
    part = np.empty(n, dtype=object)
    part[perm[:n_tr]] = "train"
    part[perm[n_tr:n_tr + n_va]] = "val"
    part[perm[n_tr + n_va:]] = "test"

    p_tr = set(pat[part == "train"])
    p_va = set(pat[part == "val"])
    p_te = set(pat[part == "test"])
    te_mask = part == "test"
    leaked = np.isin(pat[te_mask], list(p_tr))

    s = {
        "seed": seed,
        "n_train": int((part == "train").sum()),
        "n_val": int((part == "val").sum()),
        "n_test": int(te_mask.sum()),
        "patients_train": len(p_tr), "patients_val": len(p_va), "patients_test": len(p_te),
        "patient_intersection_train_test": len(p_tr & p_te),
        "patient_intersection_train_val": len(p_tr & p_va),
        "patient_intersection_val_test": len(p_va & p_te),
        "test_records_whose_patient_is_in_train": int(leaked.sum()),
        "fraction_test_records_patient_in_train": round(float(leaked.mean()), 5),
        "per_class_test": {c: int(ids[c].to_numpy()[te_mask].sum()) for c in SUPER},
    }
    summary.append(s)
    print("seed %d  train/val/test %d/%d/%d   patients(tr^te)=%d   "
          "test records with a training patient: %d (%.2f%%)"
          % (seed, s["n_train"], s["n_val"], s["n_test"],
             s["patient_intersection_train_test"],
             s["test_records_whose_patient_is_in_train"],
             100 * s["fraction_test_records_patient_in_train"]))

    df = pd.DataFrame({"ecg_id": ecg, "patient_id": pat, "audit_seed": seed, "partition": part})
    rows.append(df)

pd.concat(rows).to_csv(os.path.join(OUT, "I2_audit_split_ids.csv"), index=False)

overall = {
    "eligible_records": n, "n_train": n_tr, "n_val": n_va, "n_test": n_te,
    "permutation_engine": "numpy.random.default_rng (PCG64), permuting eligible ecg_id ascending",
    "seeds": SEEDS,
    "per_seed": summary,
    "mean_fraction_test_patient_in_train": round(
        float(np.mean([s["fraction_test_records_patient_in_train"] for s in summary])), 5),
    "range_fraction_test_patient_in_train": [
        min(s["fraction_test_records_patient_in_train"] for s in summary),
        max(s["fraction_test_records_patient_in_train"] for s in summary)],
}
with open(os.path.join(OUT, "I2_audit_partitions_report.json"), "w", encoding="utf-8") as fh:
    json.dump(overall, fh, indent=2)

print("")
print("mean fraction of audit-test records whose patient is also in audit-train: %.4f"
      % overall["mean_fraction_test_patient_in_train"])
print("range: %s" % (overall["range_fraction_test_patient_in_train"],))
print("official folds, for contrast: 0 patients shared between any two folds")
