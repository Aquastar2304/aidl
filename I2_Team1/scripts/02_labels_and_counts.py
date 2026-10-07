"""
22AIE304 / Card I2 (Team 1) - Steps 9 (parse + counts) and the label policy of Annex D6.

Builds the five-superclass multi-hot target from the pinned v1.0.3
scp_statements.csv mapping, applies Annex D6's likelihood policy, reproduces
every count the manifest and Annex D6 state, confirms the official folds are
patient-disjoint, and writes the split-ID files.

Annex D6 rule, implemented verbatim:
  "Read `scp_codes` safely as data. Retain diagnostic mappings where
   diagnostic==1 in v1.0.3 scp_statements.csv and the record's likelihood is >0;
   set each mapped superclass to one. Drop records with no retained superclass
   and publish IDs/counts by official fold."

Usage: python -I 02_labels_and_counts.py <dataset_root> <out_dir>
"""
import ast
import json
import os
import sys
from collections import Counter

import numpy as np
import pandas as pd

ROOT = os.path.abspath(sys.argv[1])
OUT = os.path.abspath(sys.argv[2])
os.makedirs(OUT, exist_ok=True)

SUPER = ["NORM", "MI", "STTC", "CD", "HYP"]
report = {}


def say(k, v, expected=None):
    report[k] = v
    tag = ""
    if expected is not None:
        tag = "  [manifest/annex: %s] %s" % (expected, "MATCH" if v == expected else "*** MISMATCH ***")
    print(f"{k:<52} {v}{tag}")


# ---------------------------------------------------------------- load
db = pd.read_csv(os.path.join(ROOT, "ptbxl_database.csv"), index_col="ecg_id")
scp = pd.read_csv(os.path.join(ROOT, "scp_statements.csv"), index_col=0)

print("=== 1. Raw collection counts ===")
say("records in ptbxl_database.csv", int(len(db)), 21799)
say("distinct patient_id", int(db.patient_id.nunique()), 18869)
say("SCP statements in scp_statements.csv", int(len(scp)), 71)
say("statements with diagnostic==1", int((scp["diagnostic"] == 1).sum()))
say("distinct strat_fold values", int(db.strat_fold.nunique()), 10)
say("sampling_frequency column present", "sampling_frequency" in db.columns)

diag_classes = scp.loc[scp["diagnostic"] == 1, "diagnostic_class"]
say("distinct diagnostic_class values", sorted(diag_classes.dropna().unique().tolist()))
say("diagnostic statements with NaN diagnostic_class", int(diag_classes.isna().sum()))

by_super = Counter(diag_classes.dropna())
print("    diagnostic statements per superclass:", dict(sorted(by_super.items())))

# statement-type breakdown (the card's 'form and rhythm statements do not map')
for col in ("diagnostic", "form", "rhythm"):
    if col in scp.columns:
        print(f"    statements with {col}==1: {int((scp[col] == 1).sum())}")

# ---------------------------------------------------------------- D6 label rule
code_to_super = {c: diag_classes[c] for c in diag_classes.index if isinstance(diag_classes[c], str)}

print("\n=== 2. Annex D6 label construction ===")
parsed = db.scp_codes.apply(ast.literal_eval)          # safe: literal_eval, never eval
db["_scp"] = parsed

Y = np.zeros((len(db), len(SUPER)), dtype=np.int8)
sup_index = {s: i for i, s in enumerate(SUPER)}
n_lik0_dropped_codes = 0
for r, (_, codes) in enumerate(parsed.items()):
    for code, lik in codes.items():
        if code in code_to_super and lik > 0:
            Y[r, sup_index[code_to_super[code]]] = 1
        elif code in code_to_super and lik <= 0:
            n_lik0_dropped_codes += 1

lab = pd.DataFrame(Y, columns=SUPER, index=db.index)
eligible = lab.sum(axis=1) > 0

# counterfactual: ignoring the likelihood>0 filter, which records would survive?
Y_nofilter = np.zeros_like(Y)
for r, (_, codes) in enumerate(parsed.items()):
    for code in codes:
        if code in code_to_super:
            Y_nofilter[r, sup_index[code_to_super[code]]] = 1
elig_nofilter = Y_nofilter.sum(axis=1) > 0

say("eligible records (>=1 retained superclass)", int(eligible.sum()), 21375)
say("dropped: no retained superclass", int((~eligible).sum()), 424)
say("dropped ONLY because likelihood==0", int((elig_nofilter & ~eligible.values).sum()), 13)
say("mapped diagnostic codes discarded at likelihood 0", n_lik0_dropped_codes)

print("\n=== 3. Counts by official fold (D6 / manifest) ===")
fold = db.strat_fold
say("eligible in folds 1-8 (train)", int(eligible[fold.isin(range(1, 9))].sum()), 17073)
say("eligible in fold 9 (validation)", int(eligible[fold == 9].sum()), 2145)
say("eligible in fold 10 (test)", int(eligible[fold == 10].sum()), 2157)
per_fold = {int(f): int(eligible[fold == f].sum()) for f in sorted(fold.unique())}
print("    eligible per fold:", per_fold)
report["eligible_per_fold"] = per_fold

print("\n=== 4. Patient-disjointness of the official folds ===")
pf = db.groupby("patient_id").strat_fold.nunique()
say("patients appearing in >1 fold", int((pf > 1).sum()), 0)
say("patients (all records)", int(len(pf)), 18869)
say("patients with >=1 eligible record", int(db.loc[eligible.values].patient_id.nunique()))

print("\n=== 5. Patient-overlap potential for the core-experiment-2 audit ===")
el = db.loc[eligible.values]
per_patient = el.groupby("patient_id").size()
say("patients holding >1 eligible record", int((per_patient > 1).sum()), 2027)
say("eligible records held by those patients", int(per_patient[per_patient > 1].sum()), 4792)

print("\n=== 6. Multi-label support, per partition ===")
split_name = {"train(folds 1-8)": fold.isin(range(1, 9)), "val(fold 9)": fold == 9, "test(fold 10)": fold == 10}
support = {}
for name, mask in split_name.items():
    m = (mask & eligible).values
    sub = lab[m]
    support[name] = {
        "records": int(m.sum()),
        "patients": int(db.loc[m].patient_id.nunique()),
        "per_class": {c: int(sub[c].sum()) for c in SUPER},
        "labels_per_record_mean": round(float(sub.sum(axis=1).mean()), 4),
        "multi_label_records": int((sub.sum(axis=1) > 1).sum()),
    }
    print(f"  {name:<18} n={support[name]['records']:>6}  patients={support[name]['patients']:>6}  "
          f"{support[name]['per_class']}  multi-label={support[name]['multi_label_records']}")
report["support"] = support

print("\n=== 7. Signal-file bookkeeping ===")
say("filename_lr column present", "filename_lr" in db.columns)
say("distinct filename_lr", int(db.filename_lr.nunique()))
missing_heads = db.filename_lr.isna().sum()
say("records with no filename_lr", int(missing_heads), 0)

# ---------------------------------------------------------------- write artefacts
lab_out = lab.copy()
lab_out["strat_fold"] = fold
lab_out["patient_id"] = db.patient_id
lab_out["filename_lr"] = db.filename_lr
lab_out["eligible"] = eligible.astype(int)
lab_out.to_csv(os.path.join(OUT, "I2_labels_superclass.csv"))

off = lab_out[lab_out.eligible == 1].copy()
off["partition"] = np.where(off.strat_fold <= 8, "train", np.where(off.strat_fold == 9, "val", "test"))
off[["patient_id", "strat_fold", "partition"] + SUPER].to_csv(os.path.join(OUT, "I2_official_split_ids.csv"))

excl = lab_out[lab_out.eligible == 0]
excl[["patient_id", "strat_fold"]].to_csv(os.path.join(OUT, "I2_excluded_records.csv"))

with open(os.path.join(OUT, "I2_counts_report.json"), "w", encoding="utf-8") as fh:
    json.dump(report, fh, indent=2, default=str)

print("\nwrote:", OUT)
