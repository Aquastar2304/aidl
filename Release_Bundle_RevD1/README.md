# 22AIE304 Deep Learning — project release bundle, Revision D1

**Issued with your assignment card. Assembled 25 September 2026; documents updated 26 September 2026.**

This bundle holds the three project documents and every data file that a card or annex says is *issued with the cards*, plus the two scripts and three reference inputs that make the I4-S grouping runnable. It does **not** hold any dataset itself: you acquire your data by the route your card and manifest describe, and these files fix the splits, selections and label maps you apply to it.

## Check the files before you use them

Every file's SHA-256 is in `SHA256SUMS.txt`. From the bundle folder:

- Linux or macOS: `sha256sum -c SHA256SUMS.txt` (macOS: `shasum -a 256 -c SHA256SUMS.txt`)
- Windows PowerShell: `Get-FileHash -Algorithm SHA256 <file>` and compare with the line for that file

Every line must match. **A file whose hash does not match is not the issued file: stop and report it.** Where your own reproduction of a split or selection differs from an issued file, the issued file governs and you report the difference in your readiness note.

## Documents (`docs/`)

| File | What it is |
|---|---|
| `Assignment_Cards_RevD1.md` | All 21 assignment cards and Protocol Annexes D0–D9. Your card and the annexes it names are your specification |
| `Student_Handout_RevD1.md` | Timeline, common requirements, assessment, ethics and practical rules |
| `Dataset_Manifests_RevD1.md` | Expected counts, sizes, routes and traps for every dataset, and the readiness-note list |

## Data files, by folder

| Folder | File | Bytes | For cards | Annex | Note |
|---|---|---:|---|---|---|
| `TrackA/` | `cwru_recordings.json` | 7,672 | A1, A2, A3 | D1 | Hashes and native rates of the sixteen CWRU source files; students download the .mat files themselves |
| `TrackB/` | `B1_common_label_map.csv` | 2,268 | B1 | D2 | 28 mapped, 27 evaluable, 10 excluded |
| `TrackB/` | `PlantVillage_B2_alignment.csv` | 16,766,383 | B2 | D2 | Colour–segmented–greyscale correspondence |
| `TrackB/` | `PlantVillage_class_support.csv` | 3,153 | B1, B2, B3 | D2 | Per-class group and image support under the caps |
| `TrackB/` | `PlantVillage_color_split.csv` | 10,027,686 | B1, B2, B3 | D2 | Repaired split, 54,305 rows |
| `TrackC/` | `TrackC_ERSSTv5_subset.npz` | 4,921,092 | C1, C2, C3 | D3 | File hash; the card quotes the hash of the float32 array inside it (`8e566e66…3570`), a different number |
| `TrackC/` | `ersst5.nino.mth.91-20.ascii` | 67,087 | C1, C2, C3 | D3 | CPC index as downloaded (public domain, NOAA) |
| `TrackE/` | `TrackE_split_lot_lists.json` | 235,630 | E1, E2, E3 | D5 | E1/E3 validation lots, E2 matched lists, E3 cap row indices |
| `I1/` | `OPSSAT_nominal_dev_segments.csv` | 3,455 | I1 | D6 | 254 development segments |
| `I1/` | `SMAP_MSL_test_C-1.npy` | 996,288 | I1 | D6 | 2,264 × 55 |
| `I1/` | `SMAP_MSL_test_P-1.npy` | 1,701,128 | I1 | D6 | 8,505 × 25 |
| `I1/` | `SMAP_MSL_train_C-1.npy` | 949,648 | I1 | D6 | 2,158 × 55 |
| `I1/` | `SMAP_MSL_train_P-1.npy` | 574,528 | I1 | D6 | 2,872 × 25, from the TranAD repository (commit 7ffb98d) |
| `I1/` | `labeled_anomalies.csv` | 3,956 | I1 | D6 | telemanom label file, byte-identical in TranAD |
| `I3/` | `I3_cell_split.csv` | 5,913 | I3 | D7 | 128 cells, 75 / 24 / 29 |
| `I3/` | `I3_cycle_life_targets.csv` | 4,994 | I3 | D7 | Issued target per physical cell, with rule A/B/C |
| `I4-S/` | `Landslide4Sense_I4S_folds.csv` | 241 | I4-S | D8 | Reissued 24 September 2026 (the first issue is withdrawn) |
| `I4-S/` | `Landslide4Sense_I4S_split.csv` | 114,886 | I4-S | D8 | Reissued 24 September 2026 (the first issue is withdrawn) |
| `I4-S/` | `Landslide4Sense_scene_group_summary.csv` | 322 | I4-S | D8 | Reissued 24 September 2026 (the first issue is withdrawn) |
| `I4-S/` | `Landslide4Sense_scene_groups.csv` | 48,848 | I4-S | D8 | Reissued 24 September 2026 (the first issue is withdrawn) |
| `I4-S/` | `i4s_extract_seams.py` | 2,289 | I4-S | D8 | Builds `seams.bin`, `pos.bin` and `stats.bin` from the 3,799 patches and masks; compare your output with `reference_inputs/` |
| `I4-S/` | `i4s_grouping_and_split.py` | 8,722 | I4-S | D8 | Reference implementation of Annex D8. Run it on `reference_inputs/` to reproduce the four CSVs, or on the output of `i4s_extract_seams.py` |
| `I4-S/reference_inputs/` | `pos.bin` | 15,200 | I4-S | D8 | Reference input: landslide pixels per patch |
| `I4-S/reference_inputs/` | `seams.bin` | 7,782,400 | I4-S | D8 | Reference input: band-14 edge vectors |
| `I4-S/reference_inputs/` | `stats.bin` | 60,800 | I4-S | D8 | Reference input: band-14 min, max, slope max, band-14 range |
| `I5/` | `I5_source_selection.csv` | 116,416 | I5 | D8a | 900 source recordings, 60 per species |
| `I5/` | `powdermill_window_support.csv` | 1,872 | I5 | D8a | Window support for all 48 species |
| `I6/` | `I6_parcel_selection.csv` | 836,102 | I6 | D9 | 13,317 / 4,500 / 4,500 |
| `I6/` | `classmapping.csv` | 441 | I6 | D9 | Package file at commit 6de796e (reference copy) |

Tracks D and I2 have no issued file: they use the authors' published files and official folds, reproduced by each group.

## Running the I4-S grouping

From `I4-S/`: `python i4s_grouping_and_split.py 0.05 out reference_inputs/seams.bin reference_inputs/pos.bin reference_inputs/stats.bin` writes four CSVs to `out/` that are byte-identical to the issued ones. To reproduce the inputs yourself, download the 3,799 training images and masks from the pinned mirror (see your manifest) and run `python i4s_extract_seams.py <images folder> <masks folder> my_inputs`; your three files should equal `reference_inputs/` byte for byte. Report any difference.

## Licences

The files here are derived from public sources; cite the original datasets as your card and manifest say. The SMAP/MSL streams (`I1/`) come from a public mirror because the original download has gone; the Track C grid subset is cut from NOAA's public ERSST v5 file; the I4-S reference inputs are small derived values (edges and counts) from the Landslide4Sense training patches, released by the authors under CC BY 4.0 — cite the Landslide4Sense paper. Recordings listed in `I5/I5_source_selection.csv` carry their own Creative Commons licences, recorded in that file; some forbid derivatives, so do not redistribute audio or mixtures made from them.
