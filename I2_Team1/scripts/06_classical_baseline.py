"""
22AIE304 / Card I2 (Team 1) - the non-deep-learning baseline (Week-2 deliverable).

Annex D6, verbatim:
    "The classical baseline is one-vs-rest regularised logistic regression on
     per-lead mean, std, min, max, quartiles, RMS, peak-to-peak amplitude and
     first-difference RMS, with training-only scaling; C in {0.1,1,10} is
     selected on validation. This is a simple multilead statistical baseline,
     not clinical-grade ECG delineation. Use identical multilabel targets and
     threshold rules for all systems."

Card I2 additionally requires the baseline to be morphology/lead-statistics based
rather than RR/HRV-dominated. Every feature below is a lead-wise amplitude or
shape statistic of the 10-second record; no beat detection, no RR interval and no
HRV quantity is computed.

Threshold rule (Annex D0): each class threshold selected from {0.1,...,0.9} on
validation F1; ties favour the LARGER threshold. No threshold selection on test.

Order of operations: C and all five thresholds are selected on fold 9 and frozen;
only then is fold 10 scored once. Fold 10 is the fixed headline (Card I2).

Metrics (Card I2): macro-F1, per-class sensitivity and specificity, macro-AUC,
on the fixed five-class label universe, with D0's unsupported-class rules.

Usage: python -I 06_classical_baseline.py <out_dir> <cache_dir>
"""
import json
import os
import sys
import time

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, roc_auc_score

OUT = os.path.abspath(sys.argv[1])
CACHE = os.path.abspath(sys.argv[2])
SUPER = ["NORM", "MI", "STTC", "CD", "HYP"]
CS = [0.1, 1.0, 10.0]
THRESHOLDS = [round(0.1 * i, 1) for i in range(1, 10)]
SEED = 22

FEATURE_NAMES = ["mean", "std", "min", "max", "q25", "q50", "q75", "rms", "ptp", "diff_rms"]


def features(X):
    """X: (n, 12, 1000) -> (n, 12*10). Lead-wise amplitude/shape statistics only."""
    q = np.percentile(X, [25, 50, 75], axis=2)                 # (3, n, 12)
    d = np.diff(X, axis=2)
    f = np.stack([
        X.mean(axis=2), X.std(axis=2), X.min(axis=2), X.max(axis=2),
        q[0], q[1], q[2],
        np.sqrt((X ** 2).mean(axis=2)),
        X.max(axis=2) - X.min(axis=2),
        np.sqrt((d ** 2).mean(axis=2)),
    ], axis=2)                                                  # (n, 12, 10)
    return f.reshape(len(X), -1)


def specificity(y_true, y_pred):
    tn = int(((y_true == 0) & (y_pred == 0)).sum())
    fp = int(((y_true == 0) & (y_pred == 1)).sum())
    return float(tn / (tn + fp)) if (tn + fp) else None


def sensitivity(y_true, y_pred):
    tp = int(((y_true == 1) & (y_pred == 1)).sum())
    fn = int(((y_true == 1) & (y_pred == 0)).sum())
    return float(tp / (tp + fn)) if (tp + fn) else None        # D0: NA, not zero


ids = pd.read_csv(os.path.join(OUT, "I2_official_split_ids.csv"), index_col="ecg_id")
sig = np.load(os.path.join(CACHE, "signals_lr_f32.npy"), mmap_mode="r")
part = ids["partition"].values
Y = ids[SUPER].values.astype(np.int8)

t0 = time.time()
Xtr = features(np.ascontiguousarray(sig[part == "train"]))
Xva = features(np.ascontiguousarray(sig[part == "val"]))
Xte = features(np.ascontiguousarray(sig[part == "test"]))
feat_seconds = time.time() - t0
print("features: %s  (%d per lead x 12 leads)  extracted in %.1fs"
      % (Xtr.shape, len(FEATURE_NAMES), feat_seconds))

n_nonfinite = int((~np.isfinite(Xtr)).sum() + (~np.isfinite(Xva)).sum() + (~np.isfinite(Xte)).sum())
print("non-finite feature values anywhere: %d" % n_nonfinite)

# training-only scaling
mu, sd = Xtr.mean(axis=0), Xtr.std(axis=0)
sd[sd == 0] = 1.0
Ztr, Zva, Zte = (Xtr - mu) / sd, (Xva - mu) / sd, (Xte - mu) / sd

Ytr, Yva, Yte = Y[part == "train"], Y[part == "val"], Y[part == "test"]

# ------------------------------------------------------- C selection on validation
t0 = time.time()
sel = []
for C in CS:
    pv_c = np.zeros_like(Yva, dtype=float)
    for k, cls in enumerate(SUPER):
        clf = LogisticRegression(C=C, max_iter=2000, random_state=SEED)
        clf.fit(Ztr, Ytr[:, k])
        pv_c[:, k] = clf.predict_proba(Zva)[:, 1]
    macro = f1_score(Yva, (pv_c >= 0.5).astype(int), average="macro", zero_division=0)
    sel.append({"C": C, "val_macro_f1_at_0.5": round(float(macro), 5)})
    print("  C=%-5s val macro-F1 @0.5 = %.5f" % (C, macro))
best_C = max(sel, key=lambda r: r["val_macro_f1_at_0.5"])["C"]
print("selected C = %s  (on validation, never on test)" % best_C)

# ------------------------------------------------------- refit at selected C
pv = np.zeros_like(Yva, dtype=float)
pt = np.zeros_like(Yte, dtype=float)
for k, cls in enumerate(SUPER):
    clf = LogisticRegression(C=best_C, max_iter=2000, random_state=SEED)
    clf.fit(Ztr, Ytr[:, k])
    pv[:, k] = clf.predict_proba(Zva)[:, 1]
    pt[:, k] = clf.predict_proba(Zte)[:, 1]
fit_seconds = time.time() - t0

# ------------------------------------------------------- thresholds on validation
thr = {}
for k, cls in enumerate(SUPER):
    scores = [(f1_score(Yva[:, k], (pv[:, k] >= t).astype(int), zero_division=0), t) for t in THRESHOLDS]
    best = max(scores)                       # ties resolve to the LARGER threshold
    thr[cls] = best[1]
    print("  threshold %-4s = %.1f  (val F1 %.4f)" % (cls, best[1], best[0]))


# ------------------------------------------------------- frozen; now score fold 10 once
def evaluate(Ytrue, P, tag):
    pred = np.zeros_like(Ytrue)
    for k, cls in enumerate(SUPER):
        pred[:, k] = (P[:, k] >= thr[cls]).astype(int)
    per_class, f1s, aucs, unsupported = {}, [], [], []
    for k, cls in enumerate(SUPER):
        pos = int(Ytrue[:, k].sum())
        sup = 0 < pos < len(Ytrue)
        f1 = f1_score(Ytrue[:, k], pred[:, k], zero_division=0) if pos > 0 else 0.0
        if not sup:
            unsupported.append(cls)
        sens = sensitivity(Ytrue[:, k], pred[:, k])
        spec = specificity(Ytrue[:, k], pred[:, k])
        per_class[cls] = {
            "support_positive": pos,
            "f1": round(float(f1), 5) if pos > 0 else None,
            "sensitivity": round(sens, 5) if sens is not None else None,
            "specificity": round(spec, 5) if spec is not None else None,
            "auc": round(float(roc_auc_score(Ytrue[:, k], P[:, k])), 5) if sup else None,
            "supported": sup,
        }
        f1s.append(f1)                       # D0: undefined per-class F1 contributes zero
        if sup:
            aucs.append(per_class[cls]["auc"])
    out = {
        "n": int(len(Ytrue)),
        "macro_f1_fixed_universe": round(float(np.mean(f1s)), 5),
        "macro_auc": round(float(np.mean(aucs)), 5) if len(aucs) == len(SUPER) else None,
        "macro_auc_NA_reason": None if len(aucs) == len(SUPER) else "a required class is undefined",
        "supported_classes": len(SUPER) - len(unsupported),
        "unsupported_classes": unsupported,
        "balanced_accuracy_over_supported": round(float(np.mean(
            [per_class[c]["sensitivity"] for c in SUPER if per_class[c]["supported"]])), 5),
        "per_class": per_class,
    }
    print("")
    print("%s  macro-F1 %.4f   macro-AUC %s   supported %d/5"
          % (tag, out["macro_f1_fixed_universe"], out["macro_auc"], out["supported_classes"]))
    for cls in SUPER:
        c = per_class[cls]
        print("   %-5s n+=%-5d F1 %.4f  sens %.4f  spec %.4f  AUC %.4f"
              % (cls, c["support_positive"], c["f1"], c["sensitivity"], c["specificity"], c["auc"]))
    return out


val_metrics = evaluate(Yva, pv, "VALIDATION (fold 9)")
test_metrics = evaluate(Yte, pt, "TEST (fold 10) - the fixed headline")

report = {
    "card": "I2", "team": 1,
    "baseline": "one-vs-rest L2-regularised logistic regression (Annex D6)",
    "features_per_lead": FEATURE_NAMES, "n_features": int(Xtr.shape[1]),
    "rr_or_hrv_features_used": False,
    "scaling": "training-partition mean/std only",
    "C_grid": CS, "C_selected_on_validation": best_C, "C_selection_detail": sel,
    "threshold_grid": THRESHOLDS, "thresholds_selected_on_validation": thr,
    "seed": SEED,
    "feature_extraction_seconds": round(feat_seconds, 1),
    "model_fitting_seconds": round(fit_seconds, 1),
    "validation": val_metrics, "test_fold10_headline": test_metrics,
    "note": ("All model and threshold choices were frozen on fold 9 before fold 10 was "
             "scored once. Not clinically validated; research exercise only."),
}
with open(os.path.join(OUT, "I2_classical_baseline.json"), "w", encoding="utf-8") as fh:
    json.dump(report, fh, indent=2)

pd.DataFrame(pv, columns=[c + "_p" for c in SUPER],
             index=ids.index[part == "val"]).to_csv(os.path.join(OUT, "I2_baseline_val_predictions.csv"))
pd.DataFrame(pt, columns=[c + "_p" for c in SUPER],
             index=ids.index[part == "test"]).to_csv(os.path.join(OUT, "I2_baseline_test_predictions.csv"))

print("")
print("classical allowance used: %.1f s elapsed (D0 budget for ALL classical fitting: 3600 s)"
      % (feat_seconds + fit_seconds))
