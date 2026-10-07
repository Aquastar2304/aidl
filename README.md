# aidl — 22AIE304 Deep Learning, end-semester project

**Team 1 · Card I2 — ECG diagnostic superclass classification and patient-overlap audit**
Amrita Vishwa Vidyapeetham, School of Artificial Intelligence, Bengaluru

---

## What is here

| Path | What it is |
|---|---|
| [`I2_Team1/`](I2_Team1/) | **Our project.** Pipeline, results, split files, readiness note, proposal |
| [`I2_Team1/READINESS_NOTE_Week1_Team1_I2.md`](I2_Team1/READINESS_NOTE_Week1_Team1_I2.md) | Week-1 dataset readiness note (the seven items of Handout §8) |
| [`I2_Team1/PROPOSAL_Week2_Team1_I2.md`](I2_Team1/PROPOSAL_Week2_Team1_I2.md) | Week-2 proposal |
| [`I2_Team1/scripts/`](I2_Team1/scripts/) | The reproducible pipeline, `01` → `07` |
| [`I2_Team1/outputs/`](I2_Team1/outputs/) | Split-ID files, count reports, timing measurements, baseline numbers |
| `Release_Bundle_RevD1/` | The course release bundle as issued (Revision D1), SHA-256 verified |
| `Release_Bundle_RevD1.zip` | The bundle as received, SHA-256 `522127833d726863f3aa0e907ba838b09c14ddec6da2dda5961e187146b0cfd2` |

**The dataset is not in this repository.** PTB-XL v1.0.3 `records100` (536 MB) and
the derived signal cache (978 MB) are reproduced by
[`I2_Team1/scripts/01_download_records100.py`](I2_Team1/scripts/01_download_records100.py),
which verifies every file against PhysioNet's own `SHA256SUMS.txt`.

## Results at a glance

Every figure in the course manifest and Annex D6 reproduced **exactly**, with no
mismatch: 21,799 records · 18,869 patients · 21,375 eligible under the D6 label
rule · 17,073 / 2,145 / 2,157 across folds 1–8 / 9 / 10 · **0** patients shared
between any two official folds · 2,027 patients holding 4,792 eligible records.

| | |
|---|---|
| Split unit | **Patient** — official `strat_fold`, folds 1–8 train, 9 validation, 10 test |
| Timed reference fit (official-fold 1-D CNN, 153,797 params) | 492.4 s elapsed / 2,916.7 s CPU · 9 epochs · peak RSS 2,529 MB · **stopped by early stopping**, not by either D0 limit |
| Classical baseline, fold 10 | macro-F1 **0.6198**, macro-AUC **0.8271** |
| Audit patient overlap (seeds 101–105) | mean **19.23 %** of test records share a patient with training, vs **0 %** officially |
| 24-hour programme projection | ≈ 2.1 h expected, ≈ 6.8 h worst case |

## Reproduce it

```bash
pip install -r I2_Team1/requirements.txt
cd I2_Team1
python -I scripts/01_download_records100.py <dataset_root> 24
python -I scripts/02_labels_and_counts.py    <dataset_root> outputs
python -I scripts/03_build_signal_cache.py   <dataset_root> outputs <cache_dir>
python -I scripts/04_timed_reference_fit.py  outputs <cache_dir> 6 0
python -I scripts/05_audit_partitions.py     outputs
python -I scripts/06_classical_baseline.py   outputs <cache_dir>
```

See [`I2_Team1/README.md`](I2_Team1/README.md) for the two named run modes and the
full protocol.

## Licence and citation

PTB-XL is CC BY 4.0. Cite the dataset papers, not just the URL:

- Wagner, P. et al. *PTB-XL, a large publicly available electrocardiography
  dataset.* Scientific Data **7**, 154 (2020).
- Goldberger, A. et al. *PhysioBank, PhysioToolkit, and PhysioNet.* Circulation
  **101**(23), e215–e220 (2000).

> This is a **research exercise for coursework**. The models here are **not
> clinically validated** and must not be used for diagnosis (Handout §10).
> Human data used is already de-identified and public; no re-identification or
> cross-linkage was attempted.
