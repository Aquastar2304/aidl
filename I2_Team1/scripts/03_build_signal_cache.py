"""
22AIE304 / Card I2 (Team 1) - Step 9, signal parsing.

Reads every eligible records100 signal with wfdb, checks shape/rate/lead order,
and writes one float32 memmap cache so the timed fit in item 7 measures training
rather than WFDB parsing. Cache construction is PREPROCESSING: Annex D0 places it
outside the per-fit clock, and it is timed and reported separately.

Usage: python -I 03_build_signal_cache.py <dataset_root> <out_dir> <cache_dir>
"""
import json
import os
import sys
import time
from collections import Counter

import numpy as np
import pandas as pd
import wfdb

ROOT = os.path.abspath(sys.argv[1])
OUT = os.path.abspath(sys.argv[2])
CACHE = os.path.abspath(sys.argv[3])
os.makedirs(CACHE, exist_ok=True)

EXPECT_LEADS = ["I", "II", "III", "AVR", "AVL", "AVF", "V1", "V2", "V3", "V4", "V5", "V6"]

ids = pd.read_csv(os.path.join(OUT, "I2_official_split_ids.csv"), index_col="ecg_id")
lab = pd.read_csv(os.path.join(OUT, "I2_labels_superclass.csv"), index_col="ecg_id")
files = lab.loc[ids.index, "filename_lr"]
n = len(ids)
print(f"eligible records to parse: {n}")

sig = np.lib.format.open_memmap(
    os.path.join(CACHE, "signals_lr_f32.npy"), mode="w+", dtype=np.float32, shape=(n, 12, 1000)
)

t0 = time.time()
shapes, rates, lead_sets, nan_records, bad = Counter(), Counter(), Counter(), [], []
units = Counter()
for i, (ecg_id, rel) in enumerate(files.items()):
    rec = wfdb.rdrecord(os.path.join(ROOT, rel.replace("/", os.sep)))
    x = rec.p_signal                                   # (samples, leads), physical mV
    shapes[x.shape] += 1
    rates[rec.fs] += 1
    lead_sets[tuple(s.upper() for s in rec.sig_name)] += 1
    units[tuple(rec.units)] += 1
    if not np.isfinite(x).all():
        nan_records.append(int(ecg_id))
        x = np.nan_to_num(x, nan=0.0, posinf=0.0, neginf=0.0)
    if x.shape != (1000, 12):
        bad.append((int(ecg_id), x.shape))
        continue
    sig[i] = x.T.astype(np.float32)
    if (i + 1) % 4000 == 0:
        print(f"  {i+1}/{n}  {time.time()-t0:.0f}s", flush=True)
sig.flush()
elapsed = time.time() - t0

print(f"\nparsed {n} records in {elapsed:.1f}s")
print("distinct (samples, leads) shapes :", dict(shapes))
print("distinct sampling rates          :", dict(rates))
print("distinct lead orders             :", len(lead_sets), "->", list(lead_sets)[0])
print("lead order matches expectation   :", list(lead_sets)[0] == tuple(EXPECT_LEADS))
print("distinct unit strings            :", dict(units))
print("records containing NaN/inf       :", len(nan_records), nan_records[:10])
print("records with unexpected shape    :", len(bad), bad[:5])
print("cache bytes                      :", os.path.getsize(os.path.join(CACHE, "signals_lr_f32.npy")))

amp = np.abs(sig[:: max(1, n // 2000)]).max(axis=(1, 2))
print(f"max |amplitude| (mV) over a 2k sample: min {amp.min():.3f}  median {np.median(amp):.3f}  max {amp.max():.3f}")

flat = int((sig[:: max(1, n // 2000)].std(axis=2) == 0).any(axis=1).sum())
print(f"records with at least one constant (flat) lead, in that 2k sample: {flat}")

with open(os.path.join(OUT, "I2_signal_cache_report.json"), "w", encoding="utf-8") as fh:
    json.dump({
        "records": n,
        "parse_seconds": round(elapsed, 1),
        "shapes": {str(k): v for k, v in shapes.items()},
        "sampling_rates": {str(k): v for k, v in rates.items()},
        "distinct_lead_orders": len(lead_sets),
        "lead_order": list(list(lead_sets)[0]),
        "lead_order_matches_standard_12": list(lead_sets)[0] == tuple(EXPECT_LEADS),
        "nan_records": nan_records,
        "unexpected_shape": bad,
        "cache_bytes": os.path.getsize(os.path.join(CACHE, "signals_lr_f32.npy")),
        "flat_lead_records_in_sample": flat,
    }, fh, indent=2)
print("ok")
