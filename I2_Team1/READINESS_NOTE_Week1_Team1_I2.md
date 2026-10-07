# Week 1 dataset readiness note — Team 1, Card I2

**ECG diagnostic superclass classification and patient-overlap audit**
PTB-XL v1.0.3 `records100` · Annexes D0 and D6 · acquisition and checks run 7 October 2026

> **Submitted late.** The note was due Friday 2 October 2026. All seven items are
> complete and the measurements are real; the lateness is ours, not a data problem.

---

### 1. The numbers we got, against the manifest

Bundle first: the zip's SHA-256 is `5221…cfd2` as issued, and `sha256sum -c
SHA256SUMS.txt` reports **32 of 32 files OK**. *Team 1: hashes OK.*

| Figure | Manifest / Annex D6 | We got | |
|---|---:|---:|---|
| `records100` files | 43,598 | 43,598 | match |
| `records100` bytes | 536,340,888 | 536,340,888 | match |
| Records in `ptbxl_database.csv` | 21,799 | 21,799 | match |
| Patients | 18,869 | 18,869 | match |
| SCP statements | 71 | 71 | match |
| Eligible records under the D6 rule | 21,375 | 21,375 | match |
| Dropped, no retained superclass | 424 | 424 | match |
| Dropped **only** by likelihood 0 | 13 | 13 | match |
| Eligible, folds 1–8 | 17,073 | 17,073 | match |
| Eligible, fold 9 | 2,145 | 2,145 | match |
| Eligible, fold 10 | 2,157 | 2,157 | match |
| Patients in more than one fold | 0 | 0 | match |
| Patients holding >1 eligible record | 2,027 | 2,027 | match |
| Records held by those patients | 4,792 | 4,792 | match |

**No mismatches.** Every file's SHA-256 was additionally checked against the
release's own `SHA256SUMS.txt` during download: 43,598/43,598 verified, 0 failures.

**Label policy, stated as the card requires.** We retain a diagnostic mapping
where `diagnostic==1` in the pinned v1.0.3 `scp_statements.csv` **and** that
record's likelihood is strictly `>0`, then set each mapped superclass to one;
a record with no retained superclass is dropped. 44 of the 71 statements are
diagnostic, 19 are form and 12 are rhythm; the form and rhythm statements map
nowhere and we never read an unmapped statement as evidence of absence.
`scp_codes` is parsed with `ast.literal_eval`, never `eval`. The likelihood
filter discards 213 mapped diagnostic codes in all, which removes 13 records
outright — reproducing D6's figure exactly.

### 2. Declared split unit, and how validation was built

**The split unit is the patient.** We use the official `strat_fold` protocol —
folds 1–8 train, **fold 9 validation**, fold 10 test — and we confirmed, rather
than assumed, that it is patient-disjoint: no patient_id appears in two folds.
Validation is therefore not resampled by us; it is fold 9 taken whole, which is
what keeps the validation partition patient-disjoint from training.

| Partition | Records | Patients | NORM | MI | STTC | CD | HYP | multi-label |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Train (folds 1–8) | 17,073 | 14,818 | 7,596 | 4,379 | 4,087 | 3,907 | 2,119 | 4,069 |
| Validation (fold 9) | 2,145 | 1,916 | 955 | 540 | 515 | 495 | 268 | 502 |
| Test (fold 10) | 2,157 | 1,876 | 963 | 550 | 506 | 496 | 262 | 497 |

All five classes are supported in all three partitions, so none of Annex D0's
unsupported-class rules is triggered and macro-AUC is defined. Mean labels per
record 1.29.

**Derived-sample check (Handout §4).** No record is an augmented or cropped view
of another; the unit of acquisition is a ten-second 12-lead recording. The one
real derived-sample risk here is **one patient contributing several recordings**,
and 2,027 patients do (4,792 records). The official folds already group by
patient, so that risk is handled — and it is exactly what Core experiment 1 then
audits deliberately.

**The five audit partitions are built and frozen** (Annex D6, seeds 101–105:
permute eligible record IDs, 80/10/10 with floor counts, whole records retained →
17,100 / 2,137 / 2,138). D6 fixes the seeds and proportions but not the
permutation engine, so we declare ours: `numpy.random.default_rng` (PCG64) over
eligible `ecg_id` in ascending order. Measured patient overlap:

| Seed | Patients shared train∩test | Test records whose patient is in training |
|---|---:|---:|
| 101 | 388 | 401 (18.76 %) |
| 102 | 367 | 378 (17.68 %) |
| 103 | 406 | 427 (19.97 %) |
| 104 | 398 | 419 (19.60 %) |
| 105 | 408 | 431 (20.16 %) |

Mean 19.23 %, range 17.68–20.16 %, against **0 %** under the official folds. These
are deliberately leaky audit controls under Card I2's audit-control exemption; the
fold-10 result remains the headline. We note, as the card instructs, that the
audit changes the test set as well as the split, so the contrast is descriptive,
not a causal estimate of leakage.

### 3. Access route

Direct HTTPS from the AWS Open Data mirror,
`https://physionet-open.s3.amazonaws.com/ptb-xl/1.0.3/`, which the manifest
records as serving the same bytes as physionet.org. **No login, no API key, no
manual acceptance of terms, no credential of any kind** — so nothing to keep out
of the repository. Version pinned in the URL. Licence **CC BY 4.0**, read before
use. Only `records100` plus the five metadata files were fetched; `records500`
was not downloaded. Access date 7 October 2026. Acquisition is fully automated in
`scripts/01_download_records100.py`, which verifies every file against the
release's own `SHA256SUMS.txt` as it goes.

### 4. Environment

Python 3.13.7 · Windows 11 Home Single Language 10.0.26200 (build 26200), 64-bit ·
CPU only. `numpy==2.5.1`, `pandas==3.0.3`, `scipy==1.18.0`, `scikit-learn==1.9.0`,
`torch==2.13.0+cpu`, `wfdb==4.3.1`, `psutil==7.2.2`. Pinned in `requirements.txt`.
Seed 22 throughout.

### 5. Transferred bytes and retained working bytes

| | Bytes | |
|---|---:|---|
| Transferred — `records100` | 536,340,888 | |
| Transferred — metadata (`ptbxl_database.csv`, `scp_statements.csv`, `RECORDS`, `SHA256SUMS.txt`, `LICENSE.txt`) | 16,037,192 | |
| **Transferred, total** | **552,378,080** | 526.8 MiB |
| Retained — the above, kept as-is | 552,378,080 | |
| Retained — derived float32 signal cache (21,375 × 12 × 1000) | 1,026,000,128 | 978.5 MiB |
| Retained — outputs, split files, checkpoint | 5,508,150 | |
| **Retained working data, total** | **1,583,886,358** | **1.475 GiB** |

Against Annex D0's 5 GB retained cap: **comfortable**. Peak temporary disk use
equals retained — the source ships loose files, so no archive is ever held and
then deleted. Retained exceeds transferred here only because the cache is
derived; it is rebuildable and could be dropped to 526.8 MiB at the cost of
re-parsing.

### 6. Anything that surprised us

- **One dead lead.** `ecg_id 12722` (fold 2, training side) has lead **V5
  constant at exactly 0.0 mV** for the whole ten seconds. Not noise — a flat
  channel. It is the only such record in all 21,375. It stays in, and our
  lead-wise baseline features give it zero variance on that lead; we flag it
  rather than drop it.
- **Amplitudes beyond physiology.** 281 records peak above 5 mV and **23 above
  10 mV** (maximum 20.03 mV), which is not a plausible surface ECG and looks like
  saturation or electrode artefact. Median peak is 1.84 mV. We have not clipped
  anything yet and would like guidance before we do, since clipping is a
  preprocessing choice that must be fitted on training data only.
- **259 patients vanish entirely** under the D6 label rule: 18,869 patients hold
  records, but only 18,610 hold at least one *eligible* record. The 424 dropped
  records are not spread evenly over patients. The manifest does not state this
  figure and we are not claiming it contradicts anything — just noting it, since
  it slightly changes the patient population the audit draws from.
- **The 100 Hz set is clean.** All 21,375 parse to exactly (1000, 12) at 100 Hz,
  one single lead order (I, II, III, AVR, AVL, AVF, V1–V6), all in mV, format 16,
  gain 1000, and **zero** NaN or infinite samples. Nothing needed repairing.
- **`ptbxl_database.csv` has no `sampling_frequency` column.** The rate lives in
  the `.hea` headers and in the `filename_lr` / `filename_hr` split. Worth knowing
  before writing a loader that expects it.

### 7. Our machine, and one timed run of the reference configuration

**Hardware.** AMD Ryzen 5 5600H, **6 physical cores / 12 logical**, 3.3 GHz ·
**9.86 GB usable RAM** · Windows 11 (10.0.26200) · CPU only, no GPU used.

> **This machine is below the D0 reference on memory.** The reference machine is
> "16 GB RAM with a 6-to-10-core CPU". We match the low end on cores but have
> **9.86 GB, not 16 GB**. It did not bite on this fit (peak 2.5 GB), but it is the
> constraint most likely to bite on the 2-D model, so we are flagging it now.

**Configuration timed** — Annex D0's Week-1 row for I2: **official-fold 1-D CNN,
17,073 training records**. This is the no-attention 1-D CNN the card already
requires; Core experiment 1 and the five audit fits reuse it, and the
lead-attention variant uses the same backbone so this fit is also its ablation.
Not an extra experiment.

| | |
|---|---|
| Threads / data-loader workers | `torch.set_num_threads(6)` / **0 workers** (data pre-cached in RAM, so workers only add process overhead on Windows) |
| Batch size · seed | 128 · 22 |
| Trainable parameters | **153,797** (D0 cap 250,000) |
| **Elapsed (first training batch → last validation + checkpoint)** | **492.4 s** (8 min 12 s) |
| **Aggregate CPU time** | **2,916.7 s** — 5.92× elapsed, i.e. ~5.9 of 6 cores busy |
| Epochs completed · optimisation updates | **9** · **1,206** (134 updates/epoch) |
| **Which limit stopped it** | **Early stopping** — 5 validation checks without improvement. *Neither the 30-epoch nor the 30-minute limit was reached.* |
| Peak memory (RSS) | **2,529 MB** |
| Preprocessing, outside the clock | 3.3 s (training-only per-lead standardisation) |

**Evidence of optimisation.** Training loss fell monotonically **0.34258 → 0.23273**
over nine epochs; validation loss fell **0.31117 → 0.28179** by epoch 4 and then
rose, which is why early stopping fired. The best-validation checkpoint (epoch 4)
is kept.

| epoch | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| train | .3426 | .2861 | .2713 | .2622 | .2520 | .2491 | .2434 | .2395 | .2327 |
| val | .3112 | .3002 | .2819 | **.2818** | .2838 | .2964 | .3160 | .2935 | .2960 |

Each epoch took a steady 54–56 s.

**Validation and inference both completed.** Validation ran every epoch. One
**timed, unscored** inference pass over test-shaped data (2,157 records) took
**2.10 s elapsed / 12.48 s CPU**, produced 2,157 rows, all finite. **No test label
was read and no test metric was computed at this checkpoint**, as item 7 requires.

**Throughput probe for the 2-D model** (not a fit; no checkpoint, no selection, in
the manner Annex D0 permits for Card A3). Per-lead log-power STFT, `nperseg` 64 /
`noverlap` 48 → 12 × 33 × 63 per record; transform costs 0.38 s per 1,000 records.
A 78,053-parameter 2-D CNN runs 0.301 s/update → **~40 s/epoch, ~20.2 min for 30
epochs** — inside the 30-minute cap.

**Projection of the whole required programme against the 24-hour elapsed budget.**
Card I2 requires 8 neural fits (official 1-D + five audit 1-D + image + attention);
fusion adds none.

| Stage | Expected | Worst case (every fit runs to the 30-min cap) |
|---|---:|---:|
| Official 1-D CNN (measured) | 492 s | 1,800 s |
| Five audit 1-D fits | 2,460 s | 9,000 s |
| 2-D spectrogram CNN (projected) | 1,210 s | 1,800 s |
| Lead-attention variant | 550 s | 1,800 s |
| Classical baseline (measured, 25 s of the 3,600 s allowance) | 25 s | 3,600 s |
| Acquisition + parse + quality scan + per-fit scaling | 2,649 s | 2,649 s |
| Repeated inference, all protocols | ~60 s | ~120 s |
| Two permitted development fits | 0 s | 3,600 s |
| **Total** | **≈ 7,446 s ≈ 2.1 h** | **≈ 24,369 s ≈ 6.8 h** |

**We are inside the 24-hour budget with large headroom** — about 3.5× even if
every fit runs to its cap. We are not requesting a scope cut.

---

### Baseline numbers, ready early (Week-2 item)

The Annex D6 classical baseline is already fitted: one-vs-rest L2 logistic
regression on 120 lead-wise features (mean, std, min, max, Q1/Q2/Q3, RMS,
peak-to-peak, first-difference RMS × 12 leads), training-only scaling. No RR and
no HRV feature is used, as the card requires. `C=10` selected on fold 9; all five
thresholds selected on fold 9 F1 from {0.1…0.9}; everything frozen before fold 10
was scored once.

| | macro-F1 | macro-AUC | NORM | MI | STTC | CD | HYP |
|---|---:|---:|---:|---:|---:|---:|---:|
| Validation (fold 9) F1 | 0.6311 | 0.8329 | 0.7768 | 0.5726 | 0.5953 | 0.6380 | 0.5729 |
| **Test (fold 10) F1 — headline** | **0.6198** | **0.8271** | 0.7590 | 0.5784 | 0.5804 | 0.6206 | 0.5605 |

Fold-10 sensitivity/specificity: NORM 0.865/0.666, MI 0.651/0.795, STTC 0.642/0.825,
CD 0.615/0.890, HYP 0.645/0.909. Classical fitting used 25.3 s of the 3,600 s
allowance.

### Attached, machine-readable

`I2_official_split_ids.csv` (21,375 rows: `ecg_id, patient_id, strat_fold,
partition`, 5 multi-hot labels) · `I2_audit_split_ids.csv` (the five audit
partitions) · `I2_excluded_records.csv` (the 424 dropped records) ·
`I2_counts_report.json` · `I2_signal_cache_report.json` ·
`I2_signal_quality_scan.json` · `I2_timed_reference_fit.json` (per-epoch history) ·
`I2_audit_partitions_report.json` · `I2_classical_baseline.json` ·
`I2_2d_throughput_probe.json`.

### One question

The 23 records peaking above 10 mV (item 6) — should we clip, exclude, or leave
them? We will leave them untouched unless told otherwise, since any clipping rule
is a preprocessing choice that would have to be fitted on training data only and
declared before modelling.

---

*This work is a research exercise. It is not clinically validated and must not be
used for diagnosis (Handout §10). PTB-XL: Wagner et al., Scientific Data 7:154
(2020); PhysioNet: Goldberger et al., Circulation 101(23):e215–e220 (2000).*
