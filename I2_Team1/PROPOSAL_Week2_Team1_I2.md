# Week 2 proposal — Team 1, Card I2

**ECG diagnostic superclass classification and patient-overlap audit**
PTB-XL v1.0.3 `records100` · Annexes D0 and D6 · CPU only · seed 22
Due Friday 9 October 2026

---

## 1. The question

Much published ECG performance is reported on splits that place the same patient
on both sides. PTB-XL ships patient-stratified folds, so the correct protocol and
a leaky one can be run on identical data with identical code. We run both and
report them side by side. **That contrast is the result** — not a leakage
coefficient.

We state the limit up front, as the card instructs: our audit changes the **test
set** as well as the split, so the gap between protocols confounds patient overlap
with ordinary partition variability. It is a **descriptive contrast between two
protocols**, not a causal point estimate of the leakage effect, and we will not
present it as one.

## 2. Data, and what is already verified

PTB-XL v1.0.3 `records100`, acquired 7 October 2026 from the AWS Open Data mirror
(`physionet-open/ptb-xl/1.0.3/`), CC BY 4.0, no login or key. 43,598 files,
536,340,888 bytes — both exact to the manifest, every file SHA-256-verified.

The Annex D6 label rule (diagnostic statements with `diagnostic==1` and record
likelihood `>0`, multi-hot over NORM/MI/STTC/CD/HYP, records with no retained
superclass dropped) reproduces **every** figure in the manifest and the annex:
21,799 records → **21,375 eligible**, 424 dropped (13 by likelihood alone),
17,073 / 2,145 / 2,157 across folds 1–8 / 9 / 10, **0** patients in two folds,
2,027 patients holding 4,792 eligible records. No mismatch anywhere.

**Split unit: the patient.** Official `strat_fold`; folds 1–8 train, fold 9
validation, fold 10 test. Fold 10 is the fixed headline. Split-ID files are
attached.

## 3. What we will build

| Component | Specification | Runs |
|---|---|---|
| Classical baseline | One-vs-rest L2 logistic regression, 120 lead-wise features (mean, std, min, max, Q1/Q2/Q3, RMS, peak-to-peak, first-difference RMS × 12 leads); `C ∈ {0.1,1,10}` on validation. No RR, no HRV. | **Done** |
| 1-D model | 1-D CNN over 12 leads, 153,797 params | reference + 5 audits |
| 2-D model | 2-D CNN on per-lead log-power spectrograms stacked as 12 channels (12 × 33 × 63), 78,053 params | once |
| Attention | **Lead-wise channel attention** on the 1-D backbone; the no-attention fit is its ablation | once |
| Fusion | **1-D model × 2-D spectrogram model** — the pair named on the card. One global weight from {0, 0.25, 0.5, 0.75, 1} on validation, ties to 0.5. No third model, no TTA, no stacking. | adds no fit |

**8 neural fits in total**, exactly the Annex D0 count for I2. Components are
demonstrated **once** on the reference setting; only the audit condition repeats.

Thresholds: each class threshold from {0.1,…,0.9} on validation F1, ties to the
larger threshold (Annex D0). Never on test, and identical rules for every system.

Metrics: macro-F1 on the fixed five-class universe, per-class sensitivity and
specificity, macro-AUC. No bare accuracy. All five classes are supported in all
three partitions, so no unsupported-class flag is needed.

## 4. The two core experiments

**Core experiment 1 — official folds versus a record-random patient-overlap audit.**
The **no-attention 1-D CNN only**, same eligible pool, same architecture, same
seed 22. The five audit partitions follow Annex D6 (seeds 101–105, permute
eligible record IDs, 80/10/10 with floor counts, whole records retained →
17,100 / 2,137 / 2,138), with the permutation engine declared as
`numpy.random.default_rng` (PCG64) over ascending `ecg_id`. Already built and
frozen; measured patient intersection:

| Seed | 101 | 102 | 103 | 104 | 105 | mean |
|---|---:|---:|---:|---:|---:|---:|
| Test records whose patient is in training | 18.76 % | 17.68 % | 19.97 % | 19.60 % | 20.16 % | **19.23 %** |

Against **0 %** under the official folds. Scaling and thresholds are refit inside
each audit. Official models are fitted and **every choice locked before any audit
training begins**; no audit result ever feeds back into the official headline.

**Core experiment 2 — class-wise analysis of that gap.** The five audit partitions
give five contrasts against one fixed official reference. We report all five
per-class values plus their mean and range. This measures **partition
variability**, not five independent estimates of a causal effect, and we will
quote no confidence interval and claim no significance. We expect the gap to
differ by class — NORM and the morphological classes (MI, STTC, HYP) have
different per-patient record structure — and that class-wise pattern is the
deliverable.

The audit partitions are **deliberately leaky audit controls**, labelled as such,
and fall under Card I2's audit-control exemption. The fold-10 result stays the
headline.

## 5. Baseline numbers (already measured)

`C=10` selected on fold 9; thresholds NORM 0.4, MI 0.3, STTC 0.3, CD 0.3, HYP 0.2
selected on fold 9; all frozen before fold 10 was scored once.

| | macro-F1 | macro-AUC | NORM | MI | STTC | CD | HYP |
|---|---:|---:|---:|---:|---:|---:|---:|
| Validation (fold 9) F1 | 0.6311 | 0.8329 | 0.7768 | 0.5726 | 0.5953 | 0.6380 | 0.5729 |
| **Test (fold 10) F1** | **0.6198** | **0.8271** | 0.7590 | 0.5784 | 0.5804 | 0.6206 | 0.5605 |

Fold-10 sensitivity / specificity — NORM 0.865/0.666 · MI 0.651/0.795 ·
STTC 0.642/0.825 · CD 0.615/0.890 · HYP 0.645/0.909.

This is a deliberately modest statistical baseline, not clinical delineation. It
uses 25 s of the 3,600 s classical allowance.

## 6. Compute plan

Measured on an AMD Ryzen 5 5600H, 6 cores / 12 threads, 9.86 GB RAM, Windows 11,
CPU only. **Our machine has 9.86 GB against the D0 reference's 16 GB**; cores
match the low end.

The timed reference fit (official-fold 1-D CNN, 17,073 records) ran **492.4 s
elapsed / 2,916.7 s CPU**, 9 epochs, 1,206 updates, peak RSS 2,529 MB, stopped by
**early stopping**, not by either D0 limit. Training loss 0.3426 → 0.2327;
validation best 0.2818 at epoch 4.

| Stage | Expected | Worst case |
|---|---:|---:|
| 8 neural fits | 4,712 s | 14,400 s |
| Classical baseline | 25 s | 3,600 s |
| Acquisition, parse, scaling | 2,649 s | 2,649 s |
| Repeated inference | 60 s | 120 s |
| Two permitted development fits | 0 s | 3,600 s |
| **Total against the 24-hour budget** | **≈ 2.1 h** | **≈ 6.8 h** |

Comfortable. **No scope cut requested.**

## 7. What we think the hard part is

Not the compute, and not the modelling. Three things:

1. **Keeping the audit honest.** The temptation is to build audit partitions that
   maximise overlap and so maximise the gap. D6 forbids it and we will not: if an
   audit shows little actual overlap we will report that. The five seeds are
   already frozen, before any audit fit exists.
2. **Resisting the causal reading.** Every sentence of the result has to survive
   the fact that the test set changed too. We will state this in the abstract, not
   in a footnote.
3. **A baseline that is weak for the right reason.** An RR/HRV baseline would
   underperform because ten-second records carry few beats — a measurement
   artefact, not evidence about deep learning. Hence lead-wise morphology
   statistics instead.

## 8. Open items for the instructor

- **The 23 records peaking above 10 mV** (max 20.03 mV, median 1.84 mV): clip,
  exclude, or leave? We leave them untouched pending your reply, since clipping is
  a preprocessing choice to be fitted on training data only and declared first.
- **`ecg_id 12722`** has lead V5 flat at exactly 0.0 mV throughout — the only such
  record. Currently retained and flagged.
- **259 patients hold no eligible record** (18,869 → 18,610). Noted, not a
  mismatch with anything the manifest states.

## 9. Attachments

`I2_official_split_ids.csv` · `I2_audit_split_ids.csv` · `I2_excluded_records.csv` ·
`I2_counts_report.json` · `I2_classical_baseline.json` ·
`I2_timed_reference_fit.json` · `I2_audit_partitions_report.json` ·
`I2_signal_quality_scan.json` · `I2_2d_throughput_probe.json` · `requirements.txt`

---

*Research exercise. Not clinically validated; not for diagnosis (Handout §10).
PTB-XL: Wagner et al., Scientific Data 7:154 (2020). PhysioNet: Goldberger et al.,
Circulation 101(23):e215–e220 (2000).*
