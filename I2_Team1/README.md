# 22AIE304 — Card I2 (Team 1)

**ECG diagnostic superclass classification and patient-overlap audit**
PTB-XL v1.0.3 `records100` · Annexes D0 and D6 · CPU only · seed 22

> Research exercise. **Not clinically validated and not a diagnostic tool.**
> Handout §10.

## Data

| | |
|---|---|
| Source | `https://physionet-open.s3.amazonaws.com/ptb-xl/1.0.3/` (AWS Open Data mirror of `https://physionet.org/content/ptb-xl/1.0.3/`) |
| Version | PhysioNet v1.0.3, pinned in the URL |
| Subset | `records100` only — the approved required subset named on Card I2 |
| Access route | Direct HTTPS. No login, no API key, no manual acceptance of terms |
| Licence | CC BY 4.0 (`LICENSE.txt` in the release) |
| Integrity | Every file verified against the release's own `SHA256SUMS.txt` |

The raw data is **not** committed. `scripts/01_download_records100.py` reproduces it.

Cite: Wagner et al., *PTB-XL, a large publicly available electrocardiography
dataset*, Scientific Data 7:154 (2020); and Goldberger et al., *PhysioBank,
PhysioToolkit, and PhysioNet*, Circulation 101(23):e215–e220 (2000).

## Pipeline

```
scripts/01_download_records100.py  <dataset_root> [workers]
scripts/02_labels_and_counts.py    <dataset_root> <out_dir>
scripts/03_build_signal_cache.py   <dataset_root> <out_dir> <cache_dir>
scripts/04_timed_reference_fit.py  <out_dir> <cache_dir> [threads] [workers]
scripts/05_audit_partitions.py     <out_dir>
scripts/06_classical_baseline.py   <out_dir> <cache_dir>
```

Run every script with `python -I` so no module is picked up from the data
directory. Scripts live outside the data directory and take paths as arguments.

## Two named modes (Handout §12)

* **`retrain`** — `01 → 02 → 03 → 04 → 05 → 06`.
  Expected: acquisition ~28 min (network-bound), cache build ~7 min,
  timed fit ≤30 min by construction, baseline a few minutes.
* **`evaluate`** — `02 → 05 → 06` reusing `outputs/I2_official_1dcnn_best.pt`
  and the saved prediction CSVs; no neural training.

## Key outputs (`outputs/`)

| File | What it is |
|---|---|
| `I2_official_split_ids.csv` | Split-ID file. `ecg_id, patient_id, strat_fold, partition, NORM, MI, STTC, CD, HYP` for all 21,375 eligible records |
| `I2_audit_split_ids.csv` | The five D6 audit partitions, `ecg_id, patient_id, audit_seed, partition` |
| `I2_excluded_records.csv` | The 424 records dropped by the D6 label rule |
| `I2_counts_report.json` | Every manifest/annex figure, reproduced |
| `I2_signal_cache_report.json` | Shapes, rates, lead order, NaN scan |
| `I2_timed_reference_fit.json` | Readiness-note item 7 measurement, with per-epoch history |
| `I2_audit_partitions_report.json` | Patient intersections per audit seed |
| `I2_classical_baseline.json` | Baseline numbers, validation and fold-10 |
| `I2_official_1dcnn_best.pt` | Best-validation checkpoint of the timed reference fit |

## Protocol, in one paragraph

Split unit is the **patient**; the official `strat_fold` protocol supplies it
(folds 1–8 train, fold 9 validation, fold 10 test), and the folds were checked
patient-disjoint. Labels are the five diagnostic superclasses as a multi-hot
target, built from the pinned `scp_statements.csv` with `diagnostic==1` and
record likelihood `>0` (Annex D6). Objective is `BCEWithLogitsLoss`. Per-class
decision thresholds come from `{0.1,…,0.9}` on validation F1, ties to the larger
threshold (Annex D0); never from test. The five record-random audit partitions
(seeds 101–105) are **deliberately leaky audit controls** under Card I2's
audit-control exemption; the fold-10 result stays the headline.
