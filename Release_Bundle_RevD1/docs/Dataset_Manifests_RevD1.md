# 22AIE304 — Dataset Manifests

**Revision D1 · 21 September 2026 · Amendment 1 to Revision D.** Supersedes Revision D of the same date.

**What changed in Amendment D1.** The protocol details that the assignment cards had referred to without stating are now fixed in the cards' **Protocol Annexes D0–D9**, and this manifest points to them. Three corrections of fact: **A1's Paderborn artificial-damage subset** named only outer-ring bearings and is corrected; **the readiness-note list below** was not in fact identical to the handout's, although this manifest said it was, and the two are now identical; and **Landslide4Sense's grouping probe** matched horizontal edges only and now matches vertical edges too. The manifest records source properties and evidence; the annexes record the selected protocols.

**What changed at Revision D (history).** Every unresolved prerequisite from Revision C is closed by measurement against the artifact: **Cropped-PlantDoc's count** (and, unexpectedly, its split), the **Severson file-level route**, the **BreizhCrops download size**, **Project 54's region identifiers** — which do not exist, and whose absence is now handled — the **xeno-canto species intersection**, and both **WM-811K** measurements. The WM-811K result reverses what this manifest previously said about the built-in split, and it corrects the lot count.

**For the Week 1 readiness note, due Friday 2 October 2026 — the last day of Week 1.** Download **the approved required subset named on your assignment card** — not the whole dataset, and not the optional secondary sources — after a preliminary access and size check. Then check your numbers against the manifest below and report matches, mismatches and anything that surprised you.

**🔴 If a figure marked as a selected-artifact check does not match, STOP the affected modelling and contact the instructor.**

Do not "work around" that kind of mismatch. It usually means a different dataset version, a partial download or a modified mirror — all of which quietly corrupt every result afterwards, often without a visible symptom until Week 7. It halts the affected modelling, not the rest of your week, and not your marks.

**But read the evidence label first.** Not every number here is a gate. A figure describing the whole source collection is not a promise about every file in it, and a figure describing the full release is not what you should get after an approved subset or filter. **Compare like with like.** An approximate figure is not an exact gate. **A documented error in this manifest never costs you marks** — report it and it is credited.

## What the evidence labels mean

| Label | Meaning |
|---|---|
| **Source-documented** | The figure is stated by the dataset's own documentation or paper. It describes the **collection**, and does not guarantee that every individual file carries every field. |
| **Selected-artifact check** | The figure was checked against the specific release, version or file this project uses. **This is the kind you stop for.** |
| **Approximate range** | A sanity band, not a target. Close is fine; wildly different is not. |
| **Unresolved prerequisite** | Something this project requires that is **not yet settled**. Never optional. If one appears on your card, it is the instructor's to close, not yours. |

| Role | Meaning |
|---|---|
| **Mandatory** | Named on your assignment card as required. |
| **Test-only** | Used for final evaluation. Never trained on, never used to select thresholds, models or augmentations. |
| **Optional** | Credited if used well; never required, and not part of your readiness note. |

**What a check does and does not certify.** A checked figure was verified against source documentation or the data on the date recorded beside it. It does **not** mean the dataset cannot have changed since, and it certifies nothing about download size, parse time or CPU cost.

**Withdrawn in Revision C, and it stays withdrawn.** Revision B stated that "every primary and mandatory secondary dataset in this document has been verified for the specific role it plays." That was stronger than the evidence. What is true is recorded per row, with the date.

## Record these for every dataset

| Field | Why |
|---|---|
| **Source URL used** | Mirrors differ from originals |
| **Dataset version / release** | e.g. "PhysioNet 1.0.3", "Dryad v2", a git commit — **pin a revision, not a landing page** |
| **Access date** | Datasets are revised without notice |
| **Archive filename and file size** | The cheapest possible integrity check |
| **Transferred bytes and retained working bytes** | These are **different numbers** wherever an archive is larger than the subset you keep. Report both. |
| **Checksum (MD5 or SHA-256)** | Recommended for any manually downloaded archive. If your results ever diverge from a groupmate's, compare this first |
| **Licence** | Read it **before use**, not only before publication. Several are non-commercial or carry mixed per-item terms |
| **Access route** | Direct download, package, API, or a gated page requiring login or manual acceptance. **Never commit an API key to your repository** |
| **Validation partition** | How you built validation — not just train and test. State the unit and the support in **each** of the three partitions |
| **Environment** | Python version, OS, and the pinned package versions you used to parse the data |

Your report can then state, for example: *"PlantVillage, authors' repository `raw/color/`, commit `7f7ecc7`, accessed 2026-10-06, CC BY-SA 3.0."* That single line is the difference between reproducible and not. *(Until 23 September 2026 this example gave the licence as CC0 1.0. No source supports that; see the PlantVillage entry.)*

**🔴 Correction carried visibly from Revision B.** This section previously used *"PlantVillage, Mendeley version 1, accessed [date], CC0 1.0"* as its worked example — the very artifact this manifest prohibits two pages below. The example endorsed the augmented variant while the trap paragraph warned against it. That is the same failure the PlantVillage entry itself records: the property was right and the artifact was wrong. The example above is corrected, and illustrative examples elsewhere use placeholders rather than any real record.

---

## TRACK A — BEARINGS

### A-primary · CWRU Bearing Data Center — mandatory (A1, A2, A3)

| Field | Expected | Evidence |
|---|---|---|
| **Source** | https://engineering.case.edu/bearingdatacenter/download-data-file | — |
| **Cleaned mirror** | https://github.com/srigas/CWRU_Bearing_NumPy (.npz, if the .mat files are troublesome) | — |
| **Format** | MATLAB `.mat`, one file per operating condition/fault | Source-documented |
| **Size** | The sixteen D1 files are 70,056,712 B | Selected-artifact check, 24 Sep 2026 |
| **Sampling rate** | 12 kHz and 48 kHz (drive end); 12 kHz (fan end) | Source-documented |
| **Motor loads** | 4 conditions: 0, 1, 2, 3 hp → 1797, 1772, 1750, 1730 rpm | Source-documented |
| **Fault diameters** | 0.007, 0.014, 0.021, 0.028 in (some sources list up to 0.040) | Source-documented |
| **Fault locations** | Inner race, outer race, ball — plus healthy baseline | Source-documented |
| **Channels** | DE, FE, BA accelerometers | Source-documented |
| **Selected recordings** | **Sixteen**: drive-end 12 kHz, 0.007-inch inner, ball and outer-at-6-o'clock faults at loads 0–3 hp (`105`–`108`, `118`–`121`, `130`–`133.mat`), plus the four normal-baseline recordings (`97`–`100.mat`, **48 kHz**). Drive-end channel only. Exact list, hashes and resampling rule: Cards Annex D1 | Card; files checked 24 Sep 2026 |
| **Split unit** | **Differs by group.** A1: source load, with guarded within-recording train/validation/test blocks. A2: pooled-load guarded blocks. A3: guarded blocks versus a deliberately leaky overlapping-window audit. Block rule: Cards Annex D1 | Card |
| **Access** | Direct download, no account | — |

**These are collection properties, not per-file guarantees.** The rates, loads, diameters and channels above describe what the *collection* contains. **An individual file need not carry every field** — not every fault location is recorded at every diameter, and not every recording has all three channels. A missing combination in one file is not a failed download and is not a reason to stop. What halts modelling is a mismatch in what you actually loaded: wrong sampling rate on a file you assumed, a truncated record, a channel that is all zeros.

**🔴 Trap found in the files (24 September 2026): `99.mat` holds two recordings.** Normal_2's file contains `X099_DE_time` and also a byte-identical copy of Normal_1's `X098_DE_time`. Use `X099_DE_time`. A loader that takes the first drive-end variable it finds would silently put the 1-hp healthy recording at 2 hp as well. Also: the normal files are 48 kHz and must be resampled; `97.mat` (Normal_0) is only 5 s long, half the others; and `98.mat` and `99.mat` carry no RPM variable.

**Known trap — this is A3's whole project.** Windows cut from one continuous recording and then split randomly share information. Much published work does this.

**Two distinctions A3 must keep straight.** (1) *Non-overlapping* is not *recording-disjoint*: windows that do not overlap can still come from one recording and remain strongly correlated. **Follow Cards Annex D1 exactly.** The valid protocol cuts each recording into guarded time blocks — train [0, a−L), validation [a+L, b−L), test [b+L, N) with a = ⌊0.6N⌋, b = ⌊0.8N⌋, L = 2,048 — and cuts non-overlapping windows wholly inside each block, so no window crosses a boundary and the two guard intervals are discarded. The audit protocol (A3 only) cuts stride-512 windows across the same complete recordings and assigns them 60/20/20 by a seed-22 permutation within recording; it is deliberately leaky, labelled as an audit control, and never used to select the valid model. The guarded-block protocol is an approved within-recording protocol: it supports a claim about separated time blocks of these recordings, not about unseen recordings. *(Corrected 24 September 2026: this paragraph said "partition recordings first, then cut windows", which contradicts the guarded-block protocol every Track A card uses. With one normal recording per load, a recording-first split cannot separate the classes.)* (2) Moving to a different recording may also change fault type, severity or load, so the gap is not purely an overlap effect unless those are held fixed. Report recording IDs and the class and load support of each partition, and state the narrower claim.

### A-secondary · Paderborn University (KAt) — mandatory for A1; optional for A2 and A3

| Field | Expected | Evidence |
|---|---|---|
| **Source** | https://groups.uni-paderborn.de/kat/BearingDataCenter/ | — |
| **🔴 How it is packaged** | **32 per-bearing `.rar` archives**, named by bearing (K001–K006, KA*, KB*, KI*), **152–178 MB each, ≈5.1 GB in total.** There is **no per-operating-condition archive.** | Selected-artifact check, 16 Sep 2026 |
| **Full extracted size** | ~20.8 GB unzipped, across all four operating conditions | Source-documented |
| **What to download** | **Only the bearing archives named on your card.** Approved A1 subset: healthy **K001, K002, K003, K004**; artificial **KA01, KA03, KA05, KI01, KI03**; natural **KA04, KA15, KA22, KI04, KI16** — fourteen archives, **2,356,527,381 B (2.19 GiB) transferred**, measured 24 Sep 2026 | Card; selected-artifact check, 24 Sep 2026 |
| **What to retain** | Records at operating condition **N15_M07_F10** (1500 rpm, 0.7 Nm, 1000 N) only — the standard condition in the literature. Extracted whole, the fourteen bearings' 280 records are **2,448,600,888 B, more than the archives**. Keep only the `vibration_1` channel your card uses: about 123 MB as compressed float32 | Card; selected-artifact check, 24 Sep 2026 |
| **Bearings** | 32 total, type 6203: 6 healthy · 12 artificially damaged · 14 real damage | Source-documented |
| **Usable for 3-class work** | 29 — KB23, KB24, KB27 carry combined inner+outer faults and are conventionally excluded | Source-documented |
| **Sampling** | Vibration 64 kHz (1 ch); motor current 64 kHz (2 ch); force/torque/speed 4 kHz; temperature 1 Hz | Source-documented |
| **Recording length** | 4 seconds, 20 repetitions per bearing per condition. In the fourteen approved bearings `vibration_1` runs from 250,604 to 284,704 samples at 64 kHz, so do not hard-code 256,000 | Source-documented; lengths checked 24 Sep 2026 |
| **Licence** | **CC BY-NC 4.0** — non-commercial, citation required | Source-documented |
| **Split unit** | **By bearing**, using the explicit 5 / 3 / 6 train / validation / test bearing IDs in Cards Annex D1. Healthy bearing IDs partitioned too, never pooled. Publish excluded and held-out IDs | Card |
| **Classes** | **healthy / inner / outer** (3-class). The four-way scheme including ball faults is CWRU's. Separate documented label map per dataset | Source-documented |

**🔴 Correction at D1 — the artificial subset.** Revisions C and D approved artificial KA01, KA03, KA05, KA07 and KA09. **Every KA bearing is an outer-ring fault** (Lessmeier et al., Table 4), so A1's training side had no inner-fault example while its test side has two, KI04 and KI16. KA07 and KA09 are replaced by the artificial inner-ring bearings **KI01 and KI03**. Still fourteen archives. **Confirmed 24 September 2026:** every approved archive parses, holds 20 N15_M07_F10 records, and carries its stated class on its own data sheet. **One qualification:** KI04's sheet lists two damages, fatigue pitting on the inner ring and particle-caused indentations on the outer ring. It keeps the authors' inner-ring designation; A1 reports it separately.

**🔴 Correction carried visibly from Revision B.** Revision B said restricting to N15_M07_F10 "cuts the download to a manageable fraction." **It does not.** The repository ships archives per *bearing*, not per *condition*, so selecting an operating condition reduces what you **extract and retain**, not what you **transfer**. Download only the approved bearing archives, and **report transferred archive bytes separately from retained working bytes.** Note that all 32 archives would be ≈5.1 GB — the whole of the ~5 GB working-data policy (Cards Annex D0), before extraction.

**🔴 Correction carried visibly from Revision B.** Revision B said that in the artificial-to-natural comparison "only the damage origin changes." **That overstates it.** What is held fixed is the **rig, the sensors and the mounting** — which is why this is a better-controlled transfer test than CWRU→Paderborn. But the artificially damaged and naturally degraded **bearing populations are different bearings with different damage characteristics and extents**. Same-rig transfer *reduces rig-related confounding*; it does not isolate damage origin. State the narrower claim. And do not compare gap magnitudes across CWRU and Paderborn causally.

---

## TRACK B — CROP DISEASE

### B-primary · PlantVillage — mandatory (B1, B2, B3)

| Field | Expected | Evidence |
|---|---|---|
| **Source** | https://github.com/spMohanty/PlantVillage-Dataset — the **authors' repository**. `raw/color/` is the original colour set. (plantvillage.org is dead.) Pin commit `7f7ecc7e1eaca78107e3affe7cb5abd9427e139a` | Selected-artifact check, 23 Sep 2026 |
| **Access route and bytes** | `git clone --filter=blob:none --sparse --depth 1`, then `git sparse-checkout set raw/color`: **854,394,188 B transferred, 850,785,369 B of images retained**; the clone's `.git` keeps about another 844 MiB unless you delete it. B2 also needs `raw/segmented` and `raw/grayscale`: another 1,313,002,201 B transferred | Selected-artifact check, 23 Sep 2026 |
| **🔴 Do NOT use** | https://data.mendeley.com/datasets/tywbtsjrjv/1 — the **augmented** variant. Revision A listed it as canonical. That was wrong. | Selected-artifact check |
| **Images** | **54,305** in `raw/color/` at the pinned commit, all decodable. Published enumerations vary between 54,303 and 54,306; confirm the count | Selected-artifact check, 23 Sep 2026 |
| **Classes** | **38** crop-disease combinations across **14** crop species. There is **no** background class | Source-documented |
| **Leaf grouping** | `leaf_grouping/leaf-map.json` says which images are views of the **same physical leaf**, but **fully for only 25 of the 38 classes**; see Trap 3. The published 80/20 splits are on the Hugging Face dataset `mohanty/PlantVillage` (`splits/`, revision `9e97599`), **not** in the GitHub repository, and they leak. Use the split issued with the cards | Selected-artifact check, 23 Sep 2026 |
| **Segmented and greyscale releases** | Both ship alongside `raw/color/`: greyscale 54,305 images, segmented **54,306**. **B2 needs all three, aligned image-for-image**; the alignment is issued with the cards. One segmented file has no colour counterpart, four are not 256 × 256, and one is single-channel | Selected-artifact check, 23 Sep 2026 |
| **Image size** | 256 × 256 for every `raw/color/` file; one is a PNG with an alpha channel, the rest JPEG | Selected-artifact check, 23 Sep 2026 |
| **Class balance** | Severe — largest class ≈ 5,500 images, smallest ≈ 150 | Source-documented |
| **Licence** | **CC BY-SA 3.0**, as stated on the authors' Hugging Face dataset card. The GitHub repository has no licence file. The authors' own loader marks that entry as an assumption to verify, so cite the paper and attribute the authors. *(Corrected 23 Sep 2026: earlier issues said CC0 1.0, and no source supports that.)* | Selected-artifact check, 23 Sep 2026 |
| **Split unit** | **By leaf group**, on any version. Splitting by image is not acceptable. **Use the issued split file** `PlantVillage_color_split.csv` (35,015 / 8,824 / 10,466). Construction, validation carve and per-class caps: Cards Annex D2 | Card |

**🔴 Critical trap 1 — the wrong download.** The Mendeley record `tywbtsjrjv/1` is titled *"Data for: Identification of Plant Leaf Diseases Using a 9-layer Deep Convolutional Neural Network"* and contains **61,486 images across 39 classes** (38 diseases plus a background class), generated by six augmentation techniques applied to the original set. **If your download has ~61k images or 39 class folders, you have the wrong version.** A random split on it places transformed copies of one leaf in train and test and will inflate your accuracy substantially. Count your images and your class folders.

**🔴 Critical trap 2 — leaf grouping, which applies to the correct version too.** The authors state that multiple images frequently capture the **same physical leaf**, and that separating those across train and test biases evaluation. Same shared-source failure as trap 1, one layer down. Affects all three Track B groups.

**🔴 Critical trap 3 — the published split leaks, and the grouping is incomplete (found 23 September 2026).** The authors' published 80/20 split places crops of one photograph (files named `… copy`, `… copy 2`) on both sides for **227 photograph stems, 243 test images** — 187 of them in Corn healthy's test set of 250. The issued split moves each such group wholly to training. Separately, the leaf map has no entries for eight classes (all four Corn classes, Grape healthy, Squash powdery mildew, Tomato mosaic virus, Tomato target spot) and covers five only in part (Strawberry leaf scorch 70%, Tomato healthy 63%, Septoria 57%, yellow leaf curl virus 51%, late blight 48%). There, a group is a photograph, not a leaf; separate photographs of one leaf cannot be grouped from the release, and results on those classes may be optimistic. Also, 21 pairs of byte-identical files exist in `raw/color/`; each pair shares one leaf ID and so stays in one partition.

### B-secondary · Cropped-PlantDoc — mandatory **test-only** for B1; optional for B2 and B3

**🔴 Counted at Revision D, and the count was the least of it.**

| Field | Expected | Evidence |
|---|---|---|
| **Source, pinned** | https://github.com/pratikkayal/PlantDoc-Dataset at commit **`5467f6012d78d1c446145d5f582da6096f852ae8`** — frozen since 2 May 2021. The README's first line states this repository holds **Cropped-PlantDoc**, the classification release; the object-detection release is a separate repository | Selected-artifact check, 20 Sep 2026 |
| **Images** | **2,578 files — 2,342 train, 236 test.** 2,576 `.jpg`, one `.jpeg`, one `.png`; none unreadable | Selected-artifact check, 20 Sep 2026 |
| **Class folders** | **28 under `train/`, 27 under `test/`** | Selected-artifact check, 20 Sep 2026 |
| **Evaluable label set** | **27.** *Tomato two spotted spider mites leaf* has two training images and **zero test images** | Selected-artifact check, 20 Sep 2026 |
| **Image sizes** | 115×69 to 6000×6000, median 800×667, 1,506 distinct sizes. These are whole photographs at native resolution, **not uniform crops** | Selected-artifact check, 20 Sep 2026 |
| **Coverage** | 13 plant species, 17 disease classes, ~27–28 joint labels | Source-documented |
| **Split** | Ships its own published train/test split | Source-documented |
| **Split unit** | The provided split. **It does not respect parent-photograph grouping — see below** | Card |
| **Licence** | CC BY 4.0 (`LICENSE.txt`) | Selected-artifact check |
| **Role** | **B1: test-only.** Never train on it, and never select augmentations or thresholds on it | Card |

**🔴 Correction to Revision C.** This manifest said the cropped release was "a different number derived from the bounding boxes" and left the figure unpinned. **It is not a per-bounding-box release.** There is one file per data point, 2,578 of them — twenty fewer than the paper's 2,598 — and there is no multiple-crops-per-parent structure to group by. The instruction to count it yourself stands as a confirmation step, not as an open question.

**🔴 The shipped split is contaminated, and Revision C's "verify this before relying on it" has now been verified — it fails.** 2,578 files carry only **2,566 distinct MD5 hashes**. Twelve byte-identical groups; **eleven span train and test**. Perceptual hashing finds **16 cross-split near-duplicate pairs covering 15 of the 236 test images**, and all 16 were inspected visually.

**🔴 Worse: eight identical photographs carry two different disease labels across the split.** `2015070295153021.jpg`, `corn-gray-leaf-spot-f4.jpg` and `IMG_42231.jpg` sit on both sides of the Corn Gray leaf spot / Corn leaf blight boundary; `1421_0.jpeg?itok=FMtmgePj.jpg`, `5816740026_d42ef24413_Phytophthora-Infestans.jpg`, `irish-blight-symptoms-on-potato-leaves-atmf8b.jpg` and `backus-056-potato-blight.jpg` sit on both sides of Potato early / late blight; `tomato_V8.jpg` sits across Tomato Septoria leaf spot / Tomato leaf bacterial spot. A ninth identical pair sits inside `train/`.

**What this means for you.** For B1 this set is test-only, so the contamination does not leak into your model — you train on PlantVillage. The cross-partition conflicts demonstrate inconsistent annotation and make the affected target labels questionable; they do not by themselves establish a ceiling on test macro-F1 or determine which label is correct. Report the fixed-universe result and the prescribed sensitivity analysis excluding the affected classes. Interpret differences cautiously and do not relabel the target using model predictions. **Publish the duplicate list in your readiness note and report the headline gap both with and without the affected classes.** *(Corrected 24 September 2026: this said the conflicts put "a ceiling on achievable macro-F1" on the confusable pairs and that the confusion there is "partly the benchmark's own label noise". B1 never trains on PlantDoc's training partition, and a conflict across partitions does not show which of the two labels is wrong, so neither claim follows. The remaining classes are not thereby verified clean, and the source–target gap also reflects target class support, not only acquisition conditions.)* Finding this is a correct result; it costs you nothing.

**Trap: the label sets do not match.** PlantVillage has 38 classes, Cropped-PlantDoc 27 evaluable, and they overlap only partly. The common-label map is frozen and issued with Card B1 as `B1_common_label_map.csv`: 28 classes map, 27 of them have target test images, and 10 PlantVillage classes are excluded in both domains. Reproduce it in Week 1, publish your version as a machine-readable file, and report any disagreement. Decisions here directly affect your reported transfer gap.

---

## TRACK C — ENSO

**One snapshot for the whole track.** Use ERSST v5 Niño 3.4 and ERSST v5 gridded SST, **January 1950–December 2024**, with the forecast, event and preprocessing contract in Cards Annex D3. The instructor's snapshot of both files, with checksums, is issued with the cards; confirm your own download against it. Do not silently replace v5 with v6.

**Gridded SST is a track-wide input.** Revision B labelled it "for C2." That was wrong: every group needs it for the required 2-D representation and the named fusion. It is demonstrated once on the card's reference setting and need not be rerun across every condition.

| Field | Expected | Evidence |
|---|---|---|
| **Niño 3.4 index** | **NOAA CPC**, https://www.cpc.ncep.noaa.gov/data/indices/ersst5.nino.mth.91-20.ascii — ERSST v5, absolute and anomaly columns for four Niño regions, anomalies against a fixed 1991–2020 base. Use the `ANOM` column after `NINO3.4`. *(Corrected 23 Sep 2026: this row named PSL's Niño 3.4 page, whose linked file is now ERSST v6. That route is withdrawn.)* | Selected-artifact check, 23 Sep 2026 |
| **Gridded SST (all three groups)** | https://psl.noaa.gov/data/gridded/data.noaa.ersst.v5.html — file https://downloads.psl.noaa.gov/Datasets/noaa.ersst.v5/sst.mnmean.nc, NetCDF4 (readable with `h5py` or `netCDF4`), 89 × 180 global grid, January 1854 to August 2026 on 23 Sep 2026 | Selected-artifact check, 23 Sep 2026 |
| **CPC ONI** | https://origin.cpc.ncep.noaa.gov/products/analysis_monitoring/ensostuff/ONI_v5.php | Selected-artifact check |
| **Size** | Index: **67,087 B**. Grid: **159,094,577 B transferred**, since the file is global and 1854 onwards; the Track C subset retained is 4,921,092 B as a compressed `.npz` | Selected-artifact check, 23 Sep 2026 |
| **Temporal coverage** | **Index: monthly, 1950/01 → present.** **Gridded ERSST: 1854 → present.** Different coverages — use the **common valid range** of the two products you actually load, and state it | Source-documented |
| **Lead times** | **1, 3, 6, 9 and 12 months. Five leads, fixed.** | Card |
| **Grid resolution** | 2° × 2° (ERSST v5) | Source-documented |
| **Split unit** | **Chronological**: training targets to December 1994, validation January 1995–December 2004, test January 2005–December 2024, with the target-boundary rule below (Cards Annex D3) | Card |

**Notes.**

**(1) 🔴 The version ambiguity became a version change (23 September 2026).** Earlier issues warned that PSL's Niño 3.4 page was labelled ERSST **v5** while PSL's listing labelled the series **v6**. On 23 September the page still said v5, but the file it links said ERSST V6 in its own footer. That route is withdrawn, and the target now comes from CPC's v5 file above. Check the version inside whatever you download, not the page that links it; all three groups use the issued snapshot.

**(2) Pin one product for the target, and identify the event reference separately.** The CPC ERSST v5 Niño 3.4 monthly anomaly and the CPC ONI product use **different anomaly constructions and are not numerically interchangeable.** Use one as the forecast target. If you use the other to define events, say so and say why.

**(3) 🔴 The forecast boundary rule — chronological splitting alone is not enough.** At a 12-month lead, a training example issued in month *t* has its target at *t*+12, which can fall inside your validation or test period even when *t* does not. **Keep every target of a training example within the training period and every validation target within validation; no test-period target may enter model selection.** Earlier history may cross boundaries when available at issue time. Use the exact dates and five-output rule in Cards Annex D3. *(Corrected at D1: the earlier wording protected the training boundary only.)* Fit every learned preprocessing step, including anomaly standardisation, on training data only, and distinguish a fixed published climatology from a statistic you estimated over held-out course data.

**(4)** For C1, you need the **initialisation month** of each forecast, not just the target month. Build that indexing carefully or the spring-barrier analysis is meaningless.

**(5)** C3 uses the course event convention, onset, neutral selection and skill formula fixed in Cards Annex D3: **signed thresholds for both phases**, at least five consecutive centred three-month means, overlapping seasons grouped into events. It is derived from the pinned forecast-target series, not substituted CPC ONI values. Consecutive overlapping three-month seasons are not independent observations; report how many independent events you have before computing anything per-event. Events are retrospective evaluation strata, never information supplied to a forecast. *(Corrected at D1: this note previously said "your card defines the onset month and the neutral comparison period". The card did not; Annex D3 does.)*

**(6) Subsurface heat content is optional** and is not manifested. Bring a versioned source to the instructor first.

---

## TRACK D — TRAFFIC / GRAPH DEEP LEARNING

| Field | Expected | Evidence |
|---|---|---|
| **Source** | https://github.com/liyaguang/DCRNN (commit `602afd9`) — adjacency matrices and sensor lists in `data/sensor_graph/`. The speed files `metr-la.h5` (57,038,056 B) and `pems-bay.h5` (135,930,936 B) are **not in the repository**: its README links them on the authors' Google Drive, with a Baidu mirror. *(Corrected 23 Sep 2026: this row said the repository holds the data.)* | Selected-artifact check, 23 Sep 2026 |
| **Raw PeMS portal** | https://pems.dot.ca.gov/ (not needed if you use the packaged version) | — |
| **METR-LA nodes** | **207** sensors | Source-documented |
| **METR-LA timesteps** | **34,272** (1 Mar – 27 Jun 2012), 5-minute aggregation, no gaps. *(Corrected 23 Sep 2026: earlier issues said 30 Jun.)* | Selected-artifact check, 23 Sep 2026 |
| **METR-LA missing data** | **8.11%** of entries are zero — real, and what D3 exploits. 2,148 time steps are zero at every sensor (97 outages, the longest 381 steps). Zeros are 7.1% of the training partition and 12.1% of test | Selected-artifact check, 23 Sep 2026 |
| **PEMS-BAY nodes** | **325** sensors | Source-documented |
| **PEMS-BAY timesteps** | **52,116** (1 Jan – 30 Jun 2017), 5-minute, with one 12-step gap at 2017-03-12 02:00, the daylight-saving change. *(Corrected 23 Sep 2026: earlier issues said 31 May.)* | Selected-artifact check, 23 Sep 2026 |
| **PEMS-BAY missing data** | ≈ **0.003%** — the natural contrast with METR-LA | Source-documented |
| **Edge counts** | **1,515 (METR-LA) and 2,369 (PEMS-BAY) — under the DCRNN generator's conventions only.** In the shipped pickles these are directed off-diagonal non-zeros; with self-loops they are 1,722 and 2,694. One METR-LA sensor and six PEMS-BAY sensors have no off-diagonal edge. See the convention rule below | Selected-artifact check, 23 Sep 2026 |
| **Adjacency construction** | Thresholded Gaussian kernel on road-network driving distance; **directed/asymmetric**, commonly symmetrised as ½(A + Aᵀ) | Source-documented |
| **Split** | **Chronological 70 / 10 / 20** (DCRNN convention) — never random | Card |
| **Normalisation** | Z-score on inputs, **fit on the training partition only**. Fitting the scaler on the whole series is leakage | Card |
| **Missing-value encoding** | Zeros denote **missing readings**, not a measured speed of zero. Build an explicit mask, exclude masked positions from the loss and from MAE/RMSE/MAPE | Card |
| **Size** | 57,038,056 B and 135,930,936 B as downloaded; both fit comfortably in memory | Selected-artifact check, 23 Sep 2026 |
| **Roles** | D1: METR-LA mandatory, PEMS-BAY optional. D2: METR-LA mandatory, second city optional and only if budgeted. D3: METR-LA mandatory, **PEMS-BAY mandatory as a bounded replication** | Card |

**🔴 Edge counts are convention-dependent, not a universal checksum.** Revision B told you to print the edge count and confirm it matched this table. That instruction was wrong as stated: the count depends on the distance threshold, on whether the matrix is treated as directed, and on whether self-loops are counted. **Record the adjacency file, the sensor order, the threshold, the direction convention and the self-loop convention, and compare counts only under the same convention. Never alter a correct graph to match an unqualified literature count.**

**What you should still check:** that the adjacency loaded, has the right dimensions, aligns with your sensor ordering, and has **nontrivial connectivity**. A common bug loads the adjacency incorrectly and leaves a graph with no edges, which silently turns your GNN into a per-sensor model and makes D2's question unanswerable.

**Published baselines** — historical average, VAR, linear regression, SVR, ARIMA, LSTM, DCRNN, Graph WaveNet.

**Use them as a leak detector, not as a target.** If your error is *dramatically better* than the published numbers, suspect your chronological split before you believe your model. This is a smell test. It is **not** a correctness gate and agreement is not required: direct comparison with published tables needs matched data, preprocessing, splits, null masks and metrics, and a rescoped protocol does not have them.

**For D3.** Mask sensor *inputs* at test time on known nodes, at rates **0/5/10/20/30/40 per cent**, distinguishing **block outages of 12 consecutive steps** from independently missing entries, scoring only where ground truth is observed, with the **same masks and the same five seeds for every model compared**. Predicting at entirely unseen nodes is a different (inductive) task and is not core.

---

## TRACK E — WAFER MAPS (WM-811K)

| Field | Expected | Evidence |
|---|---|---|
| **Original source, and the recommended route** | `http://mirlab.org/dataSet/public/MIR-WM811K.zip` — direct HTTP, **no login**, Range supported. **344,542,743 bytes transferred** | Selected-artifact check, 20 Sep 2026 |
| **What is inside the archive** | `MIR-WM811K/Python/WM811K.pkl` — **2,022,961,642 bytes uncompressed**; `MIR-WM811K/MATLAB/WM811K.mat` — **3,596,549,129 bytes uncompressed**; plus readmes and screenshots | Selected-artifact check, 20 Sep 2026 |
| **Transferred vs retained** | **328.6 MiB transferred; 1.88 GiB retained** if you extract the Python pickle only, 3.35 GiB for the MATLAB copy, 5.23 GiB for both. Report both figures | Selected-artifact check, 20 Sep 2026 |
| **Mirror** | https://www.kaggle.com/datasets/qingyi/wm811k-wafer-map (`LSWMD.pkl`, ≈214 MB) — requires a Kaggle account | Selected-artifact check |
| **Total wafer maps** | **811,457** from **46,293** lots. *(Corrected at Revision D: every earlier issue said 46,393. The source pickle has 46,293 distinct `lotName` values.)* | Selected-artifact check, 21 Sep 2026 |
| **SHA-256 of the archive** | `81431a81ceac0e96caef08f50aaecc4970edc56e7df7703ee17fb9e321853eef` | Selected-artifact check, 21 Sep 2026 |
| **Labelled** | **172,950** (21%); **638,507 unlabelled** | Selected-artifact check, 21 Sep 2026 |
| **🔴 Missing-label encoding** | In `WM811K.pkl`, labelled rows hold a **plain string**; unlabelled rows hold **`array([0, 0], dtype=uint64)`** in both `failureType` and `trainTestLabel`. Test for a string. A "non-empty" test counts every wafer as labelled | Selected-artifact check, 21 Sep 2026 |
| **With an actual defect pattern** | **25,519** | Selected-artifact check |
| **Fields** | `waferMap`, `dieSize`, `lotName`, `waferIndex`, `trainTestLabel`, `failureType` | Selected-artifact check |
| **Split unit** | **E1 and E3:** the built-in `trainTestLabel`. **E2:** disjoint `lotName` groups | Card |
| **Lot overlap of the built-in split** | **Zero.** 5,809 training lots, 4,953 test lots, **none shared**; 0 of 118,595 test wafers share a lot with a training wafer | Selected-artifact check, 21 Sep 2026 |
| **Built-in partition sizes** | **Training 54,355, Test 118,595** labelled wafers — the split is **test-heavy** | Selected-artifact check, 21 Sep 2026 |
| **Shift between the built-in partitions** | Defect-pattern share **32.4% → 6.7%**; `none` 67.6% → 93.3%; 335 wafer shapes in training, 51 in test, 40 shared; **7.0% of test wafers** have a shape absent from training; median `dieSize` 533 → 845 | Selected-artifact check, 21 Sep 2026 |
| **E3 eligible pool size after exclusions** | **633,277** unlabelled wafers in 40,483 lots after excluding every lot with a test wafer (5,230 excluded); **619,987–626,656** after a further 10–20% training-lot validation carve; **620,038** in 39,496 lots under the fixed Annex D5 carve; floor 566,611 | Selected-artifact check, 21 and 23 Sep 2026 |

**🔴 Correction to Revision C.** This manifest gave a single "Size ≈ 214 MB" row. That figure describes the Kaggle mirror's pickle and is neither the transferred nor the retained figure for the original route. The rows above replace it, and this is exactly the transferred-versus-retained distinction Handout §4 makes a rule of.

**🔴 The three groups do not share one split.** Share the loader, the preprocessing and the baseline *code*; do **not** assume shared split membership or a single baseline number. One baseline result per approved protocol, and compare across groups only where protocol and configuration are identical.

**🔴 What the built-in protocol measures — settled at Revision D, and it reverses Revision C.** Revision C said that unless the measurement showed otherwise, a result under the built-in split was **not** a claim about unseen-lot generalisation. **The measurement shows otherwise: the built-in split is lot-disjoint.** A result under it is an unseen-lot result. What it is *not* is a clean lot-separation result, because the test partition is also shifted in defect prevalence and wafer size — see the rows above. E1 and E3 state both facts. E2 now uses a **matched** lot-disjoint split, stratified on class and wafer size (die-count quintile). The gap between it and the built-in split is a descriptive contrast: it combines the held-out class and wafer-size mix with differences in training population, training size and optimisation exposure, and it measures neither the shift alone nor lot separation. Report the achieved distributions. *(Corrected 24 September 2026: this said the gap "measures the shift".)*

**Validation construction.** Follow Cards Annex D5. **E1 and E3:** the first 20% of training lots in SHA-256 order of `22|lotName`, never using test labels. **E2:** a matched lot-disjoint 60/20/20 split built with `StratifiedGroupKFold` on class × die-count quintile, grouped by `lotName`, with the quintile tie rule and the scikit-learn version pinned in Annex D5. **The E2 split and the E1/E3 validation lots are issued with the cards** as `TrackE_split_lot_lists.json` (SHA-256 `4083f50c…02a6`); reproduce them and report any difference. Die count equals `dieSize` for every labelled wafer. No split is redrawn on model results. *(Corrected 23 September 2026: without a pinned tie rule, two reasonable quintile rules put 79% of wafers in different E2 folds.)*

**E3 pool rule.** The unlabelled pseudo-label pool must exclude **every wafer belonging to a validation or test partition, and every wafer from any lot represented in validation or test**. The card fixes two nested caps, **2,000 and 10,000 eligible wafers**, and the pseudo-label confidence threshold at **0.95** (Cards Annex D5). Report the eligible count your validation carve produces; it should be 620,038. Stopping uses validation only. If the exclusion leaves too little pool for a meaningful study, tell the instructor — the protocol will be revised openly rather than quietly using held-out data.

**Class counts (labelled subset)** — selected-artifact check. Taxonomy is **eight defect classes plus `none`, single-label**. There is no mixed-type class; datasets with mixed patterns (e.g. MixedWM38) are separately synthesised and out of scope.

| Class | Count |
|---|---|
| none | 147,431 |
| Edge-Ring | 9,680 |
| Edge-Loc | 5,189 |
| Center | 4,294 |
| Loc | 3,593 |
| Scratch | 1,193 |
| Random | 866 |
| Donut | 555 |
| **Near-full** | **149** |

**The same classes under the built-in split** — selected-artifact check, 21 Sep 2026. Wafers, with the number of lots they come from.

| Class | Train | Train lots | Test | Test lots |
|---|---|---|---|---|
| none | 36,730 | 1,654 | 110,701 | 4,937 |
| Edge-Ring | 8,554 | 756 | 1,126 | 319 |
| Center | 3,462 | 1,130 | 832 | 518 |
| Edge-Loc | 2,417 | 1,536 | 2,772 | 1,675 |
| Loc | 1,620 | 1,022 | 1,973 | 1,450 |
| Random | 609 | 267 | 257 | 182 |
| Scratch | 500 | 428 | 693 | 631 |
| Donut | 409 | 123 | 146 | 110 |
| **Near-full** | **54** | **54** | **95** | **83** |
| **Total** | **54,355** | **5,809** | **118,595** | **4,953** |

Every class has support in both partitions. Near-full's training wafers come one per lot, so a lot-grouped validation carve is feasible for every class.

**Traps.** (0) **The nine counts sum to 172,950 and the eight defect counts to 25,519.** Check both sums — the cheapest error detector you have. (1) **Wafer maps vary in size**, so you need a resize or padding strategy and must justify it. **Values are categorical** (outside-wafer / good die / bad die), so any interpolating resize invents meaningless values: use nearest-neighbour or padding, and report per-class and per-lot counts **before and after** the transform — rare classes can disappear entirely once you split by lot. (2) ~85% of labelled maps are `none`, so **accuracy is meaningless**; use macro-F1 and per-class recall. (3) The dataset contains **known mislabelled instances** — acknowledge this in limitations rather than discovering it late. (4) A class with **no support in an evaluation partition is reported as unsupported**, not dropped from the macro-average. Cards Annex D0 fixes the macro-F1 label universe and the explicit NA conventions for recall, balanced accuracy and AUC.

---

## I1 — Satellite Telemetry Anomaly Detection

### Primary · OPSSAT-AD — mandatory

| Field | Expected | Evidence |
|---|---|---|
| **Data** | https://zenodo.org/records/12588359 — **pin this record**: `segments.csv` 17,970,946 B, `dataset.csv` 507,568 B. A later version (record 15108715) shifts timestamps by one second and writes `anomaly` into the `label` column of every row; values, anomaly flags and the split are identical. Use the `anomaly` column, never `label` | Selected-artifact check, 23 Sep 2026 |
| **Code / baselines** | https://github.com/kplabs-pl/OPS-SAT-AD | Selected-artifact check |
| **Paper** | https://doi.org/10.1038/s41597-025-05035-3 | Selected-artifact check |
| **Fragments** | **2,123** | Selected-artifact check |
| **Channels** | **9** telemetry channels | Selected-artifact check |
| **Dimensionality** | **Univariate** — each fragment is a single channel | Selected-artifact check |
| **Anomalous fraction** | ≈ **20%** | Selected-artifact check |
| **Files** | `segments.csv` (raw signals), `dataset.csv` (extracted features) | Selected-artifact check |
| **Published baselines** | 30 algorithms with results | Source-documented |
| **Split** | A train/test split and suggested metrics are provided — use them | Source-documented |
| **Fragment length** | **Variable.** Cards Annex D6 resamples every fragment to 256 samples; report the original-length distribution and its effect on score calibration in your readiness note | Card |

**This dataset is univariate.** Do not design cross-channel attribution experiments; there are no simultaneous channels within a fragment. The natural comparison is **per-channel specialised models versus one global model**, which the benchmark paper itself reports.

**🔴 Do not pool metrics.** OPSSAT-AD is evaluated at **fragment level**; SMAP/MSL at **point or event level** within continuous streams. Score each natively, report side by side, never average across the two. **Point-adjusted F1 applies only to the SMAP/MSL point-level audit, beside the unadjusted point score; never to OPSSAT-AD fragments.** Time-based rates (false alarms per day) require validated continuous time coverage — OPSSAT-AD fragments are not continuous, so do not report them there.

**Label access — decided on your card, not by you.** A supervised classifier and a nominal-only autoencoder receive different information. Your core comparison runs **within one regime: nominal-only**. A supervised image-side formulation may be run as a **separately labelled cross-regime demonstration**, which does not support a conclusion about architecture.

**Score fusion.** Declare a common score orientation and normalisation, and fit them — with thresholds — **on nominal development data only, never on test**. Cards Annex D6 fixes the fusion weight at 0.5 and the threshold at the 99th percentile of nominal-development scores.

### Secondary · SMAP / MSL — mandatory, bounded audit only

| Field | Expected | Evidence |
|---|---|---|
| **Source** | https://github.com/khundman/telemanom. The original S3 archive returns 403 (23 Sep 2026), and the README now routes acquisition through a Kaggle copy that needs an account. **The P-1 and C-1 files are issued with the cards.** They come from the TranAD repository (commit `7ffb98d`), whose label file is byte-identical to telemanom's. Reproduce from either route in Week 1 and compare hashes | Selected-artifact check, 23 Sep 2026 |
| **Telemetry streams** | **55 (SMAP) + 27 (MSL)** — counts of *streams*, i.e. separate files, **not** columns within a file. In `labeled_anomalies.csv`, P-2 appears twice with different intervals and T-10 has files but no label row | Selected-artifact check |
| **Columns per stream** | **25 for SMAP, 55 for MSL.** Within each stream, **column 0 is the telemetry value** and every remaining column is a one-hot command flag. Each stream carries exactly **one** sensor signal | Selected-artifact check |
| **Stream subset** | **SMAP P-1 and MSL C-1**, fixed by Cards Annex D6; complete published test streams | Card |
| **🔴 Preprocessing limitation** | Telemetry ships **pre-scaled to (−1,1) using min/max taken from the test set**. You cannot claim training-only preprocessing on this benchmark. Record it as an inherited limitation; do not try to undo it | Selected-artifact check |

**Read the structure correctly before you write the audit.** The published criticism is that each stream has a single sensor channel padded with command flags — **not** that 54 of the 55 SMAP streams are command flags. Confirm the column layout yourself. "One-hot" also does not imply constant: **measure** how much the command columns vary and contribute rather than assuming they are inert.

**Your job is to test the claim, not to confirm it.** Whether the trivial detector turns out competitive or not, a controlled answer earns full marks. The published criticism is a hypothesis under test, not a verdict to reach.

---

## I2 — ECG Diagnostic Superclass Classification and Patient-Overlap Audit

### Primary · PTB-XL — mandatory

| Field | Expected | Evidence |
|---|---|---|
| **Source** | https://physionet.org/content/ptb-xl/1.0.3/ — **pin the version in the URL.** The bare path follows the latest release and will move. `records100` is 536,340,888 B in 43,598 files. The AWS mirror `s3://physionet-open/ptb-xl/1.0.3/` serves the same bytes (`aws s3 sync --no-sign-request`) and was far faster than PhysioNet's own server on 23 Sep 2026 | Selected-artifact check, 23 Sep 2026 |
| **Records** | **21,799** in the v1.0.3 `ptbxl_database.csv`, counted 23 Sep 2026. (The 21,837 figure describes v1.0.0.) Under Cards Annex D6's label rule, 21,375 are eligible | Selected-artifact check, 23 Sep 2026 |
| **Patients** | **18,869** in v1.0.3 (18,885 in v1.0.0) | Selected-artifact check |
| **Leads** | 12 | Source-documented |
| **Duration** | 10 seconds | Source-documented |
| **Sampling rates** | 500 Hz and **100 Hz** — **use `records100`**, ~5× cheaper and what most baselines use | Source-documented |
| **Labels** | **71 SCP-ECG statements**, which include **diagnostic, form and rhythm** statements. Only the diagnostic statements map into the 5 superclasses (NORM, MI, STTC, CD, HYP) | Source-documented |
| **Label construction** | From the pinned `scp_statements.csv` mapping, with an **explicit likelihood/filter policy stated in your readiness note**. Target is **multi-hot**, not argmax | Card |
| **Folds** | **10 patient-stratified folds.** Standard protocol: 1–8 train, 9 validation, 10 test | Source-documented |
| **Split unit** | **By patient** — the folds already do this | Card |

**Core task, fixed.** Five-superclass **multi-label** classification on `records100` under the official `strat_fold` protocol, plus a predeclared patient-overlap audit. A multi-hot target, a BCE-style objective, decision thresholds on validation only.

### Secondary · MIT-BIH Arrhythmia — **optional**

| Field | Expected | Evidence |
|---|---|---|
| **Source** | https://physionet.org/content/mitdb/1.0.0/ | Selected-artifact check |
| **Records** | **48** half-hour excerpts from **47** subjects | Source-documented |
| **Leads** | 2 (usually modified limb lead II + V1) | Source-documented |
| **Sampling** | **360 Hz**, 11-bit over 10 mV | Source-documented |
| **Annotations** | ≈ **110,000** beat labels | Source-documented |
| **AAMI class counts** | N 90,593 · S 2,781 · V 7,235 · F 802 · Q 8,040 — **these are pre-exclusion totals for the whole collection.** After the four paced records are removed and beats are extracted under your chosen window, your counts **will not match these and are not expected to** | Source-documented |
| **Standard split** | Inter-patient **DS1/DS2**: 22 train / 22 test; paced records **102, 104, 107, 217 excluded** per AAMI | Source-documented |

**🔴 The two datasets are not directly compatible.** PTB-XL: 12-lead, record-level *diagnostic* labels. MIT-BIH: 2-lead, beat-level *morphology* labels. **Different target spaces — a PTB-XL classifier cannot be evaluated on MIT-BIH.** If you attempt the optional leg, the only well-posed form is *representation* transfer: pretrain the encoder on PTB-XL, freeze it, train a new beat-classification head on MIT-BIH, and compare against training from scratch. **A new head does not dissolve the other incompatibilities** — specify the lead mapping, a justified **common** sampling rate with proper antialiasing (upsampling 100 Hz to 360 Hz recovers no bandwidth; resample both to a common rate), the beat-extraction window, how a fixed-length encoder handles variable-length input, and which records and annotations you exclude.

**Baseline note.** Build a modest multilead feature baseline that includes **waveform morphology or simple lead-wise statistics**. An RR/HRV-dominated feature set is a poor match here: three of the five superclasses are morphological and a ten-second record carries few beats, so such a baseline would be weak for the wrong reason. Clinical-grade delineation is not required and short-record HRV is not a prerequisite.

---

## I3 — Battery Early-Life Prediction

**🔴 The file-level route is closed at Revision D.** Revision C recorded it as an unresolved prerequisite and warned that a project landing page is not a pipeline. The route below was walked on 20 September 2026: the file list was read from the platform's own API and a ranged request was issued against each struct, returning `206` with the size in `content-range` and the filename in `content-disposition`.

| Field | Expected | Evidence |
|---|---|---|
| **Project page** | https://data.matr.io/1/projects/5c48dd2bc625d700019f3204 — the bare `data.matr.io/1/` root does **not** resolve to the data | Selected-artifact check |
| **API route** | `GET /1/api/v1/edp/projects/5c48dd2bc625d700019f3204/batches` → each batch's `structFileId` → `GET /1/api/v1/file/<id>/download`. `GET /1/api/v1/file/<id>` returns metadata including the exact size | Selected-artifact check, 20 Sep 2026 |
| **File 1** | `2017-05-12_batchdata_updated_struct_errorcorrect.mat`, id `5c86c0b5fa2ede00015ddf66`, **3,025,320,241 bytes** | Selected-artifact check, 20 Sep 2026 |
| **File 2** | `2017-06-30_batchdata_updated_struct_errorcorrect.mat`, id `5c86bf13fa2ede00015ddd82`, **2,007,331,155 bytes** | Selected-artifact check, 20 Sep 2026 |
| **File 3** | `2018-04-12_batchdata_updated_struct_errorcorrect.mat`, id `5c86bd64fa2ede00015ddbb2`, **3,236,690,412 bytes** | Selected-artifact check, 20 Sep 2026 |
| **All three** | **8,269,341,808 bytes = 7.70 GiB transferred — not retained.** Acquire and compact one struct at a time (Card I3): keep `Qdlin`/`Tdlin` for the available cycles through 100 with their original cycle IDs (required completeness is cycles 2–100; the 2017-05-12 batch has no cycle 1, which is not an exclusion) and the full per-cycle summary as float32, then delete the struct. Measured on 2017-06-30: 48 records → 39,323,488 B in 12.8 s, peak memory 52 MB; all 140 records → about 116 MB retained. Peak temporary disk: one struct plus the compact store, at most about 3.35 GB. HTTP Range supported, so the download resumes. *(Corrected 24 Sep 2026: this said "transferred and retained", in conflict with the 5 GB working-data cap.)* | Selected-artifact check, 20 Sep 2026; compaction measured 24 Sep 2026 |
| **Per-cell CSV route** | Exists and is **more** expensive: 140 cell files totalling **19,386,089,076 bytes = 18.05 GiB**, median per cell 103–167 MB | Selected-artifact check, 20 Sep 2026 |
| **Smallest single struct** | The **2017-06-30** struct, 2,007,331,155 bytes, 48 cells. It is **not** a substitute for the sequential route: alone it drops the five continuing cells and two batches of held-out cells, which changes the issued protocol | Selected-artifact check, 20 Sep 2026 |
| **Cells** | **124** usable commercial LFP/graphite 18650 cells in the source paper (A123 APR18650M1A, 1.1 Ah nominal). The platform lists **140 cell tests across 135 distinct cell IDs**. **Annex D7's pool is 128**: the 135 cells less seven tests the batch notes say stopped before 80% capacity | Source-documented; platform listing checked 20 and 23 Sep 2026; all three structs parsed 23 Sep 2026 |
| **Charging policies** | **72** distinct fast-charging protocols | Source-documented |
| **Cycle life range** | **148 – 2,237** cycles over the 128-cell pool (issued targets, 24 Sep 2026); the source paper's ≈ 150 – 2,300. Discharge-capacity series lengths over the 140 listed tests: min 172, p25 533, median 789, p75 1,010, max 2,239 | Selected-artifact check, 20 Sep 2026 |
| **Format** | MATLAB `.mat`, nested struct — parsing takes real effort, budget for it | Source-documented |
| **Licence** | CC BY 4.0, stated on the project page | Selected-artifact check |
| **Split unit** | **By physical cell.** Never by cycle, and never by `(batch, cell)` — see below | Card |
| **Extension** | Attia et al. (2020) follow-up, ~45 further cells | **Optional**, unverified — verify it yourself and record what you find |

**🔴 Five cells appear in two batches.** `el150800460486`, `el150800460514`, `el150800464977`, `el150800460623` and `el150800464865` are listed under both 2017-05-12 and 2017-06-30, because the second batch resumed them — its own batch note says channels 1, 2, 3, 5 and 6 "carry over from batch 1 … these are NOT new experiments." **Deduplicate by physical cell ID before splitting.** 140 listed tests, 135 distinct cells.

**Fix your held-out cells before you download anything.** Each cell record in the `/tests` listing carries a `summary` field holding the full discharge-capacity-versus-cycle series. The cell list, the exclusion list and the **mean-life floor** are therefore computable from the API alone, at no transfer cost. Cards Annex D7 fixes the 60/20/20 split rule: each physical cell belongs to the batch where its cycling began, and a continuing cell's two records are joined first. Put the resulting IDs in your readiness note. **The split is issued with the cards** as `I3_cell_split.csv` (128 cells: 75 / 24 / 29); cell IDs are hashed **in lower case**, because the raw `cellId` field mixes cases. **Do not take `cycle_life` from the structs at face value:** for the five continuing cells the 2017-06-30 value counts only that batch's cycles, and the 2017-05-12 struct gives censored run lengths for its five tests that stopped before 80%. *(Corrected 23 September 2026.)* **The target is issued** as `I3_cycle_life_targets.csv` (Cards Annex D7): end of life at 0.88 Ah (80% of 1.1 Ah); the authors' field is the first entry below 0.88 Ah in the platform's discharge-capacity series for 2017-05-12 and 2017-06-30 cells, and the final entry for 2018-04-12 cells, whose tests stopped at 0.88 Ah; the five continuing cells use the authors' join (1,434 to 2,237 cycles — adding the two batch fields overstates each by one). Reproduce the check from the listing's summaries; score against the issued file. *(Added 24 September 2026. The earlier sentence here, that the 2017-06-30 struct alone drops the five continuing cells, stays true; it is no longer offered as a route.)*

**🔴 Horizon-safe features — the leakage trap.** At an observation horizon of *k* cycles, **every feature must be derived from cycles ≤ k**. The published ΔQ(V) baseline is defined between cycle 100 and cycle 10 and is **not computable at a 10-cycle horizon**; adapt the endpoints per horizon and state them. The same applies to any normalisation or target statistic computed in preprocessing. Core horizons are **100 / 30 / 10** cycles; intermediate windows are optional.

**Baseline to beat:** the published elastic-net on ΔQ(V) features. Also report the **mean-life predictor** as a floor, with the mean computed on **training cells only**.

**The core task is regression of cycle life.** Life-band classification is optional and is not required by either core experiment.

---

## I4 — 3D-Printing Error Detection (CAXTON) — **WITHDRAWN**

**This project is not assignable in this release, and no card is issued for it.**

| Field | Finding | Evidence |
|---|---|---|
| **Distribution** | A **single hierarchical archive**: `dataset/` containing five root CSVs and `print0/` … `print191/`, each holding per-print logs and `image-0.jpg …` at **1280 × 720** | Selected-artifact check, 16 Sep 2026 |
| **Repository record** | The Cambridge item exposes **only the five CSVs** — 119.96, 110.74, 144.4, 138.1 and 126.29 MB, ≈640 MB combined. No image archive is listed | Selected-artifact check, 16 Sep 2026 |
| **Code repository** | Ships **8 cropped and full sample images**, nothing more | Selected-artifact check, 16 Sep 2026 |
| **Public mirror** | `cemag/tl-caxton`: **4,040 images at 350 × 350** with flow rate and nozzle coordinates only — **no printer identity, no geometry identity, no four-parameter labels** | Selected-artifact check, 16 Sep 2026 |
| **Images** | 1,272,465 captured, 1,272,273 labelled | Source-documented |
| **Selective download route** | **None documented.** At 1.27 M JPGs of that resolution the full archive is on the order of 100 GB | Unresolved prerequisite |

**Why this matters more than a broken link.** Revision B told the group to cap its working set at 30,000–50,000 images stratified across printers and parts, and to confirm reachable archives and bytes in Week 1. That instruction presumes a selective route which has not been shown to exist. **A row cap is not a byte cap**, and here the byte cap is the project. The mirror cannot substitute: without printer and geometry identity there is no holdout to construct, and the whole project is a cross-printer generalisation audit.

**What would reopen it.** A confirmed bounded image route — per-print access from the repository, an author-supplied subset, or a mirror carrying printer and geometry metadata — with measured transferred bytes for the approved subset.

**Team 16 takes the substitute below.**

---

## I4-S — Landslide Detection (Landslide4Sense) — Team 16

**🔴 Two findings at Revision D, and both change how this project runs.**

### The original `iarai.ac.at` download endpoints are offline; the course uses its pinned mirror

`iarai.ac.at` no longer resolves. Checked 20 September 2026 by two independent paths: a browser could not load `https://www.iarai.ac.at/landslide4sense/` or `https://cloud.iarai.ac.at/…`, and a server-side fetch returned "Name or service not known" for the domain. IARAI was wound down in 2023. **Both download links printed in the benchmark repository's README are dead**, as is its pretrained-model link. The GitHub repository itself — code, file lists, README — is still up and is still the reference for the data description.

### The release carries no region identifiers, and that is deliberate

The development set ships as a flat sequence, `TrainData/img/image_1.h5 … image_3799.h5` with matching masks, and the repository's own lists carry paths only. There is **no region column, no metadata file and no folder-per-area**. The organisers' README FAQ states it plainly: the geographic information and acquisition time "will not be released at the current phase in case participants may directly look for the corresponding high-resolution images to check."

**Revision C's "split by case-study area" and "publish the region IDs" are therefore not executable and are withdrawn.** They are replaced by a grouping probe, below.

| Field | Expected | Evidence |
|---|---|---|
| **The course's route** | https://huggingface.co/datasets/ibm-nasa-geospatial/Landslide4sense — public, ungated, last modified 22 Oct 2024. **The course's demonstrated and currently pinned route**, not the only one: an author-maintained Zenodo record also lists the competition archives (see the note below the table) | Selected-artifact check, 20 Sep 2026 |
| **Route that does not** | The two `cloud.iarai.ac.at` links in the benchmark README, and the competition site. **Dead** | Selected-artifact check, 20 Sep 2026 |
| **Reference repository** | https://github.com/iarai/Landslide4Sense-2022 — still live; code, file lists, data description | Selected-artifact check, 20 Sep 2026 |
| **Paper** | https://arxiv.org/abs/2206.00515 | Source-documented |
| **Patches (labelled, competition)** | **3,799**, 128 × 128 × 14 | Selected-artifact check |
| **Per-file size** | `image_N.h5` **1,837,056 bytes** (128 × 128 × 14 float64 + 2,048-byte header); `mask_N.h5` **18,432 bytes** | Selected-artifact check, 20 Sep 2026 |
| **Whole mirror** | 4,844 images + 4,844 masks = **8,987,983,872 bytes = 8.37 GiB**, transferred and retained, uncompressed | Selected-artifact check, 20 Sep 2026 |
| **The subset this project uses** | 3,799 images + 3,799 masks = **7,048,998,912 B = 6.56 GiB transferred**; **3,547,840,512 B = 3.30 GiB retained** as float32 images and `uint8` masks. **The mirror serves single ranges but refuses multi-range requests**, so the whole subset must be read | Full pass, 24 Sep 2026 |
| **Value range** | Already globally rescaled into roughly [0, 7]. **Band 14 is not elevation in metres and the spectral bands are not raw reflectance.** The official loader then standardises per band with means −0.4914 … 0.7819 and stds 0.88 … 1.61 | Selected-artifact check, 20 Sep 2026 |
| **Storage advice** | **Cast to float32 on ingest** — halves the retained figure safely. An integer downcast needs a stated scale factor and is not free | Card |
| **Bands** | Sentinel-2 **B1–B12** plus **slope (B13)** and **DEM (B14)** from ALOS PALSAR, resampled to 10 m | Selected-artifact check |
| **Format** | HDF5, one dataset per file, data at byte offset 2048, shape (128, 128, 14) band-last | Selected-artifact check, 20 Sep 2026 |
| **Pixel imbalance** | **58.73%** of patches contain landslide pixels (2,231 of 3,799) but only **2.3180% of all pixels** are landslide (1,442,790 of 62,242,816). Pixel accuracy is meaningless | Full pass, 24 Sep 2026 — confirms the Revision D estimate |
| **Degenerate patches** | **114** with band 14 constant and slope identically zero, **all of them negative**, 113 in scene group S1. One further patch has a constant band 14 but non-zero slope and is kept | Full pass, 24 Sep 2026 |
| **Split unit** | **Recovered scene group. Four exist, and they are issued** — see below | Full pass, 24 Sep 2026 |

**A second route exists, and it is not adopted.** An author-maintained Zenodo record, [DOI 10.5281/zenodo.10463239](https://zenodo.org/records/10463239) (Ghorbanzadeh et al., version v1, record created 5 January 2024, CC BY 4.0), lists `TrainData.zip` (2.5 GB, MD5 `408f09247e3dd256458bc2f6e9edbffb`), `ValidData.zip` (143.4 MB) and `TestData.zip` (470.9 MB), and states that masks are released for the training set only. Read in the built-in browser on 24 September 2026; nothing was downloaded. It does **not** establish byte equivalence with the mirror, a successful course download, or any provenance for the mirror's 1,045 extra masks. The issued grouping and split are built on the mirror's bytes and stay there; comparing the two routes is an optional check, and a group that uses Zenodo must show its 3,799 patches are identical before using the issued split. *(Added 24 September 2026. Earlier wording called the mirror the only surviving route; it is the course's demonstrated and currently pinned route.)*

**🔴 Two defects in the mirror.** (1) It carries masks for the **validation and test** splits — 1,045 patches whose labels the competition withheld — and its README does not say where they came from. **Checked at source, 24 September 2026, and the answer is that nothing says:** `annotations/validation` holds 245 masks and `annotations/test` 800, which is exactly the 1,045; the README describes the folder structure and no more; and the repository's six commits, all dated 22 October 2024, carry only generic `huggingface_hub` upload titles. The bar on marked use therefore stands as a settled negative, not as an open question. **Treat them as an optional extension with unverified provenance; they must not appear in any marked result.** Everything assessed uses the 3,799 competition-labelled training patches. (2) `annotations/train/` holds **3,804** files: the 3,799 masks plus five 800-byte strays named `image_1.h5`, `image_10.h5`, `image_100.h5`, `image_1000.h5`, `image_1001.h5`. Glob `mask_*.h5` explicitly.

**🔴 The grouping is recovered and issued. This replaces the D1 wording that left the full pass to Week 1.** The patches were cut as a raster tiling and written in scan order, so adjacent tiles share an edge. Edge signatures from band 14 were matched **right edge to left edge and bottom edge to top edge across all 3,799 × 3,799 ordered pairs**, and scene groups taken as connected components of reciprocal nearest-neighbour matches below τ = 0.05. Full procedure, threshold rule, the seam and contiguity rules and the within-group block rule: Cards Annex D8, with the reference script `i4s_grouping_and_split.py`. *(Corrected at D1: the Revision D wording matched horizontal edges only. Without vertical links, two rows of one scene would count as two groups and leave-one-group-out would leak across them. **The full pass confirms this: the row strides are 41, 15, 11 and 26.**)*

**The full pass, 24 September 2026.** All 3,799 images and masks streamed from the mirror — **7,048,998,912 B in 48.9 minutes, no failed fetch** — and reduced to four 128-value band-14 edge vectors per patch (7,858,400 B retained). τ = 0.05, set from the histogram before grouping: the true-neighbour mode lies at 0.015–0.020, a random pair falls below 0.05 only 0.31% of the time against a random-pair median of 1.3095, and the grouping is unchanged for τ from 0.04 to 0.10. **3,490 horizontal and 3,487 vertical reciprocal links. Four scene groups, each a contiguous run of patch IDs** *(reissued 24 September 2026 — see the correction below)*:

| Scene | Patches | Positive | Negative | Landslide pixels | Raster grid |
|---|---|---|---|---|---|
| **S1** | 3,033 | 1,934 | 1,099 | 1,269,296 | 41 × 74 |
| **S2** | 150 | 126 | 24 | 108,533 | 15 × 10 |
| **S3** | 121 | 69 | 52 | 16,108 | 11 × 11 |
| **S4** | 494 | 102 | 392 | 48,853 | 26 × 19 |

Each group has exactly one dominant vertical stride — 41, 15, 11, 26 — which is an independent confirmation that four components means four tilings. Horizontal best match is the next index for 3,566 of 3,799 patches; S4's 468 vertical links are all exact.

**🔴 Defects in the method as D1 stated it, found by running it.** (1) **A near-constant seam matches any other near-constant seam at distance 0** — closer than a real neighbour, which differs by about 0.018 because adjacent tiles share no pixel column. Near-constant seams (range below 0.01: 153 right, 149 bottom, 158 left, 172 top) are barred from linking on **both** sides of a link. (2) The unlinked patches — 130 of them — are attached by raster index contiguity; 129 attach and patch 3034 is left unassigned. (3) **Degenerate patches number 114, not the "at least one" D1 recorded** — all negative, 113 placed in S1 by contiguity — and are excluded from every partition after grouping.

**🔴 Corrected 24 September 2026: the first issued grouping and split were wrong, and are reissued.** The executed pass kept a link when the proposer was the closest claimant of its partner (collision resolution, not reciprocal nearest neighbours) and barred only the proposing seam, so patch 2460 — all four seams exactly constant, and positioned inside S1's test block — was linked into S2. Its grid coordinates were then assigned by enumeration, which shifted 573 S1 patches (IDs 2461–3033) by one grid position and left **15 test-block patches edge-adjacent to training patches**. The reissued files use reciprocal matching with both seams gated and coordinates from ID arithmetic; they have no train–test or test–transfer adjacency. The group count, the S1-only target and the fold design are unchanged.

**The issued files (reissued 24 September 2026):** `Landslide4Sense_scene_groups.csv` (SHA-256 `49c9fb5f…7cf8`), `Landslide4Sense_scene_group_summary.csv` (`0b9e0e19…4a9a`), `Landslide4Sense_I4S_split.csv` (`21aad749…e44c`), `Landslide4Sense_I4S_folds.csv` (`835eb37b…c74b`), the scripts `i4s_extract_seams.py` and `i4s_grouping_and_split.py`, and the reference inputs `seams.bin`, `pos.bin` and `stats.bin` (Cards Annex D8). The mirror is pinned at revision `4b291891badf301b5c75c2153f0f8fe00eeb1435` (last modified 22 October 2024). The earlier files with hashes `6500242c…`, `dfa576fc…`, `ed9e42d0…` and `beb696d7…` are withdrawn. Team 16 reproduces the pass in Week 1 and reports any disagreement; recovery still counts under Component 1. **Every claim names the unit as a scene group recovered from tile adjacency — a proxy for a case-study area, never a region or a country.**

**🔴 The fold structure changed as a result, and this is the substantive finding.** Four groups clear D1's eligibility bar, but a **target** group must also carry a guarded three-block split of its own, because the within-group reference and the transfer model are scored on the same test patches. The requirement is now explicit: **at least 20 positive and 20 negative patches in the target's guarded test block**. Under the pinned block rule S4's test block holds 114 patches with 3 positives (80 of its 102 positives lie in rows 4–11 and they thin out eastward), S2's holds 40 (29 / 11) and S3's 33 (17 / 16). **S1 is the only possible target.** *(Corrected 24 September 2026: this said rows 4–11 held 89 positives and that S2 and S3 could not carry three blocks.)* Card I4-S now issues one matched fold on S1 (test 570 patches, 210 positive) and three whole-scene transfer folds onto S2, S3 and S4.

**Screen for degenerate patches — the count is 114.** Band 14 min = mean = max and slope identically zero. All 114 are negative; 113 are in S1 and one is the unassigned patch 3034. Patch 2500, the example named at D1, is one of them. They are marked `excluded_degenerate` in the issued split. Reproduce the count and report any disagreement.

**Task: patch-level binary classification.** A patch is positive if its mask has at least one pixel of value 1. Pixel-wise segmentation is an optional extension. Metrics follow the task: **landslide-class precision, recall and F1; binary balanced accuracy**; per-scene-group support and results; pixel accuracy banned from the headline. *(Corrected at D1: "balanced accuracy on the landslide class" is not a defined quantity; balanced accuracy averages both class recalls.)*

**🔴 Baseline correction, carried from Revision C.** An earlier project description listed "NDVI change" as a baseline. **These patches are single-date — there is no second observation and no change feature is computable.** Use a random forest on single-date band summaries and slope/DEM summaries, plus a training-derived majority floor (Cards Annex D8). **Check band scaling first:** the values are globally rescaled (above), so NDVI or a bare-soil index is valid only if every band involved shares one documented scale. Otherwise omit it and say why.

**Note on channels.** ImageNet backbones take 3 channels, not 14. Band selection, a learned 14→3 projection, or a small CNN from scratch are all defensible; the choice is a real design decision and you justify it.

---

## I5 — Bird Species from Audio

### Primary · xeno-canto — mandatory training source

| Field | Expected | Evidence |
|---|---|---|
| **API** | https://xeno-canto.org/api/3/recordings | Selected-artifact check |
| **Terms** | https://xeno-canto.org/about/terms | Selected-artifact check |
| **🔴 API key** | **Required since October 2025.** Free, but needs a registered account with a verified email. **Register on the day you receive your card**, and confirm in your readiness note that the key works | Selected-artifact check |
| **Rate limit** | Of order 1,000 requests/hour; mass downloading is explicitly discouraged | Source-documented |
| **Audio route and bytes** | Each recording's public link `https://xeno-canto.org/<number>/download` serves the recordist's **original upload** — MP3 or WAV, 16–48 kHz, mono or stereo — with no content length and no byte-range support, so each file is transferred whole. One test recording per selected species (15 files) transferred **80,966,563 B**, one of them a 64,545,530 B stereo float WAV; all 15 decoded. Decode by content, trim to 30 s and resample on arrival, delete the original, and report transferred and retained bytes | Selected-artifact check, 24 Sep 2026 |
| **Licence** | **Mixed** — recordings carry different Creative Commons versions. Check and record them before use and again before redistribution | Source-documented |
| **Quality ratings** | A–E per recording | Source-documented |
| **🔴 Species intersection** | **Closed at Revision D: 48 of 48.** Every Powdermill species clears the ≥50 A–C threshold. Full counts below | Selected-artifact check, 20 Sep 2026 |
| **Working scope** | **15 species** from the 48 that also have **at least ten positive Powdermill windows across at least two soundscape recordings** (Cards Annex D8a). **22 species qualify** (Cards Annex D8a, counted 23 Sep 2026); a soundscape recording is one of the four dawn recordings, not a segment file. **The 15 are fixed** — the 15 eligible species with the most positive Powdermill windows — and their 900 source recordings (60 per species, 36 / 12 / 12) are issued as `I5_source_selection.csv` (Cards Annex D8a, 24 Sep 2026). The shortfall action is fixed in D8a | Card; selected-artifact check, 24 Sep 2026 |
| **Split unit** | **By recording**, and ideally by recordist and location | Card |

**🔴 Trap 1 — taxonomy.** xeno-canto follows **IOC**; Powdermill's labels and eBird follow **Clements**. Hairy Woodpecker is *Dryobates villosus* to eBird and ***Leuconotopicus villosus*** to xeno-canto. A name-based scrape using the eBird name returns **zero recordings and no error message**. It was the only mismatch in the 48, and it would have silently cost a species. **Resolve every name against xeno-canto's own taxonomy and log any species that returns zero rather than dropping it.**

**Trap 2 — geography.** The counts below are worldwide. Restricted to `cnt:"United States"`: *Meleagris gallopavo* 109, *Buteo lineatus* 142, *Vermivora cyanoptera* 162, *Parkesia motacilla* 177, *Geothlypis formosa* 180, *Spinus tristis* 234. No species is near the threshold. *(Corrected 23 September 2026. Revision D's 48-species table listed American Golden-Plover, *Pluvialis dominica* (`amgplo`), in place of **American goldfinch**, *Spinus tristis* (Powdermill code `AMGO`). The dataset README and all 62 `AMGO` annotations identify the goldfinch; no golden-plover occurs in Powdermill. The "48 of 48" availability result still holds for the correct 48 — the goldfinch has 379 A–C recordings worldwide and 234 in the United States — but the golden-plover counts and the geography warning built on them were about a species that is not in the test set, and are withdrawn.)*

**The 48-species universe, with A–C recording counts** — measured 20 September 2026, foreground species only, quality A–C. Scientific names follow xeno-canto's taxonomy where it differs from eBird's.

| eBird code | Scientific name | A–C | eBird code | Scientific name | A–C |
|---|---|---|---|---|---|
| cangoo | *Branta canadensis* | 759 | ovenbi1 | *Seiurus aurocapilla* | 426 |
| wiltur | *Meleagris gallopavo* | 127 | louwat | *Parkesia motacilla* | 198 |
| yebcuc | *Coccyzus americanus* | 262 | buwwar | *Vermivora cyanoptera* | 174 |
| amegfi | ***Spinus tristis*** *(corrected 23 Sep 2026; was* Pluvialis dominica *126)* | 379 | bawwar | *Mniotilta varia* | 420 |
| reshaw | *Buteo lineatus* | 148 | naswar | *Leiothlypis ruficapilla* | 296 |
| rebwoo | *Melanerpes carolinus* | 242 | kenwar | *Geothlypis formosa* | 212 |
| dowwoo | *Dryobates pubescens* | 321 | comyel | *Geothlypis trichas* | 793 |
| haiwoo | ***Leuconotopicus villosus*** | 406 | hoowar | *Setophaga citrina* | 317 |
| norfli | *Colaptes auratus* | 503 | amered | *Setophaga ruticilla* | 636 |
| pilwoo | *Dryocopus pileatus* | 243 | babwar | *Setophaga castanea* | 231 |
| eawpew | *Contopus virens* | 309 | chswar | *Setophaga pensylvanica* | 345 |
| reevir1 | *Vireo olivaceus* | 447 | btnwar | *Setophaga virens* | 271 |
| buhvir | *Vireo solitarius* | 298 | scatan | *Piranga olivacea* | 244 |
| blujay | *Cyanocitta cristata* | 566 | robgro | *Pheucticus ludovicianus* | 354 |
| amecro | *Corvus brachyrhynchos* | 517 | norcar | *Cardinalis cardinalis* | 888 |
| comrav | *Corvus corax* | 2,783 | swathr | *Catharus ustulatus* | 870 |
| cedwax | *Bombycilla cedrorum* | 229 | herthr | *Catharus guttatus* | 574 |
| tuftit | *Baeolophus bicolor* | 392 | veery | *Catharus fuscescens* | 457 |
| bkcchi | *Poecile atricapillus* | 521 | woothr | *Hylocichla mustelina* | 414 |
| ruckin | *Corthylio calendula* | 530 | amerob | *Turdus migratorius* | 926 |
| carwre | *Thryothorus ludovicianus* | 692 | eastow | *Pipilo erythrophthalmus* | 425 |
| buggna | *Polioptila caerulea* | 404 | balori | *Icterus galbula* | 340 |
| whbnut | *Sitta carolinensis* | 474 | rewbla | *Agelaius phoeniceus* | 997 |
| brncre | *Certhia americana* | 437 | bnhcow | *Molothrus ater* | 358 |

**These are availability counts, not usability counts.** The usability filter in Cards Annex D8a — foreground species (subspecies included), no other selected species in the background metadata, at least 5 seconds — was run on 24 September 2026 for all 22 eligible species. For the 15 selected it leaves 163 (scarlet tanager) to 747 (northern cardinal) usable recordings, so every species clears 50 with room to spare. Reproduce the counts in Week 1, and record each file's licence: eight Creative Commons variants occur among the selected recordings.

### Secondary · Powdermill soundscapes — mandatory, **test-only**

| Field | Expected | Evidence |
|---|---|---|
| **Source** | https://datadryad.org/dataset/doi:10.5061/dryad.d2547d81z | Selected-artifact check |
| **Paper** | Chronister et al., *Ecology* 102(6):e03329 — https://doi.org/10.1002/ecy.3329 | Selected-artifact check |
| **🔴 Version — pinned** | **Version 2, 6 April 2021.** Dryad holds two versions: v1 (1 Apr 2021, wav 1.43 GB, mp3 182.28 MB) and **v2 (6 Apr 2021, wav 1.05 GB, mp3 136.95 MB)**. Annotation archives are identical across both. **Use v2, `mp3_Files.zip` (136.95 MB)**; `wav_Files.zip` (1.05 GB) is the fallback if you hit a decoding problem | Selected-artifact check, 16 Sep 2026 |
| **Duration** | **385 minutes (6.41 hours)** of dawn-chorus recordings | Selected-artifact check |
| **Recorders / days** | 4 autonomous recording units, 4 days, April–July 2018, Powdermill Nature Reserve, Pennsylvania | Selected-artifact check |
| **Species** | **48** — the list above | Selected-artifact check |
| **Annotations** | **16,052**, *strongly labelled* — start time, end time, frequency bounds and species per vocalisation. 77 segment files (Recordings 1–4: 36 / 14 / 1 / 26), each 300.06 s — **4,620 complete 5-second windows**. The README states that every identifiable vocalisation other than short chips was annotated | Selected-artifact check, 23 Sep 2026 |
| **🔴 Access route** | Dryad's API now requires a bearer token for file downloads, and the web download links pass through an automated browser check. **Download by hand in a browser** and record the SHA-256 (annotation archive `7edf8a0e…44cb`, mp3 archive `8571423c…3155`). A manual route with an integrity check is not a reproducibility penalty | Selected-artifact check, 23 Sep 2026 |
| **Licence** | **No copyright or proprietary restrictions.** Cite the paper | Selected-artifact check |
| **Split unit** | **Test set only** — never train on it, never select thresholds, models or augmentations on it, and never use it as a source of background noise | Card |

**🔴 Evaluation targets.** **Fixed-window multi-label** targets from the strong labels — a window may contain several species, or none. Cards Annex D8a fixes the convention: **5-second windows, hop 5 seconds, 22.05 kHz mono**; a species is positive in a window if one of its annotations overlaps the window by any positive duration. **Do not infer window-level support from the 16,052 annotation count**: annotations are vocalisations, not evaluation windows, and per-species window support is much smaller. Count it.

**"No selected species" is not "no bird."** Powdermill's 48-species universe is not the set of all birds.

**The species list no longer has to be extracted before scraping.** It is above, and the availability intersection is settled. The window-support filter above is applied by the instructor before issue; in Week 1 you reproduce it and do the **per-species usability count**.

### Ambient noise · freefield1010 (`ff1010bird`) — mandatory for core experiment 2

| Field | Expected | Evidence |
|---|---|---|
| **Source** | https://archive.org/details/ff1010bird | Selected-artifact check, 16 Sep 2026 |
| **Challenge page** | https://dcase.community/challenge2018/task-bird-audio-detection | Selected-artifact check, 16 Sep 2026 |
| **Clips** | **7,690** field-recording excerpts, sourced from Freesound worldwide | Selected-artifact check |
| **Duration** | **10 seconds each** | Selected-artifact check |
| **Format** | **44.1 kHz mono PCM WAV**, 16-bit, amplitude-normalised per excerpt | Selected-artifact check |
| **Licence** | **CC BY 4.0** — attribute in your report | Selected-artifact check |
| **Labels** | Binary `hasbird` (0/1) per recording, in `ff1010bird_metadata_2018.csv` — **on figshare (file 10853303, linked from the DCASE 2018 task page), not in the archive.org item** *(corrected 23 Sep 2026)* | Selected-artifact check, 23 Sep 2026 |
| **Class balance** | **5,755 `hasbird == 0` and 1,935 `hasbird == 1`, of 7,690.** Confirm the count in your readiness note | Selected-artifact check, 23 Sep 2026 |
| **Archive** | `ff1010bird_wav.zip`, **5,772,437,544 bytes** (5.38 GiB) on archive.org; the label file separately, on figshare. **You do not need the archive:** archive.org serves each member individually at `https://archive.org/download/ff1010bird/ff1010bird_wav.zip/wav%2F<itemid>.wav`, 882,044 bytes per clip, so ≤300 clips is ≤264,613,200 bytes transferred | Selected-artifact check, 23 Sep 2026; member route checked 24 Sep 2026 |
| **What to use** | **Only clips labelled `hasbird == 0`.** Retain **at most 300 clips**. Report transferred archive bytes separately from retained working bytes | Card |
| **Split role** | Noise source for the SNR mixture only. Never a training target, never evaluated on | Card |

**Why this source is admissible.** It is independent of Powdermill in recorder, site and date; it is redistributable under CC BY 4.0 with attribution; and it carries an explicit bird-absent label, so mixing does not inject unlabelled positives into your SNR curve.

**Two cautions.** (1) `hasbird` is a **detection label from a challenge**, not a guarantee — a clip labelled 0 may still contain faint or distant bird sound. **Spot-check a sample by ear and exclude anything with audible bird sound.** (2) The full archive is larger than the clips you need, and the host permits fetching individual files from within it (checked 24 September 2026: the listing holds 7,690 members, and a member download returned an 882,044-byte WAV). Use that route; you then need no temporary space beyond the clips themselves. Report both byte figures. *(Changed 24 September 2026: this left the member route to be checked in Week 1, with a 5.77 GB transfer as the fallback.)*

---

## I6 — Crop Mapping (BreizhCrops)

| Field | Expected | Evidence |
|---|---|---|
| **Source** | https://github.com/dl4sits/breizhcrops — pip-installable, fetches data automatically | Selected-artifact check |
| **Region** | Brittany, France | Source-documented |
| **Classes** | **9** class IDs from the pinned package `classmapping.csv` (SHA-256 `e850f71d…42e9`, 23 crop codes); use its exact names and mapping, not a hand-transcribed crop list. **Two are near-empty:** sunflower has 7 eligible training parcels across frh01/frh02 and nuts 28. In the issued selection sunflower has 0 / 0 validation / test parcels (recall NA) and nuts 1 / 1 (recall defined, reported beside n = 1). Card I6 reports macro-F1 over all nine and over a predeclared seven-class subset excluding both; D0's supported-class balanced accuracy has eight classes on test *(corrected 24 Sep 2026)* | Source-documented; counted 24 Sep 2026 |
| **🔴 Processing levels, and when they exist** | **L2A exists for 2017 only.** 2018 ships L1C alone, and `kermaux` has no L2A at all. **The paired experiment is a 2017 experiment** | Selected-artifact check, 20 Sep 2026 |
| **🔴 Download size — retained bytes** | From the package's own `FILESIZES` table, which the loader asserts the extracted `.h5` against. frh01 L1C 2,559,635,960 + L2A 987,259,904 · frh02 2,253,658,856 + 803,457,960 · frh03 2,493,572,704 + 890,027,448 · frh04 1,555,075,632 + 639,215,848 · belle-ile 17,038,944 + 8,037,952 | Selected-artifact check, 20 Sep 2026 |
| **🔴 The official partition, paired** | frh01+frh02 train, frh03 validation, frh04 test = **12,181,904,312 bytes = 11.34 GiB retained**, plus the `.tar.gz` on top, which the loader deletes after extracting | Selected-artifact check, 20 Sep 2026 |
| **🔴 `belle-ile` — do not use** | 25,076,896 bytes, but **every belle-ile parcel is also in frh04, the test region** (1,341 of 1,341 L1C and 1,050 of 1,050 L2A IDs). Developing on it means developing on test parcels. *(Corrected 24 Sep 2026: earlier issues recommended it for building the pipeline.)* | Selected-artifact check, 24 Sep 2026 |
| **Transferred bytes** | **7,141,517,144 bytes of `.h5.tar.gz`** for the four regions at both levels (L1C 1,644,959,752 / 1,454,637,750 / 1,595,835,853 / 1,008,000,500; L2A 423,918,335 / 349,623,184 / 384,320,619 / 280,221,151), plus 124,220,579 bytes of index files. Less than the retained 11.34 GiB, because the archives are compressed. About 0.9 MB/s per connection from this host | Selected-artifact check, 24 Sep 2026 |
| **🔴 Default band sets differ by level** | `SELECTED_BANDS` for **L1C** is B1–B12 plus QA10, QA20, QA60 and doa; for **L2A** it is B2–B8, B8A, B11, B12 plus CLD, EDG, SAT and doa. **Different count, different bands, different mask semantics** | Selected-artifact check, 16 Sep 2026 |
| **🔴 The L1C file's column order is not `SELECTED_BANDS`** | The shipped L1C `.h5` stores B1, B10, B11, B12, B2, B3, B4, B5, B6, B7, B8, B8A, B9, QA10, QA20, QA60, doa. The ten common bands are L1C columns 4–11, 2 and 3; indexing by `SELECTED_BANDS` names returns B10 (cirrus) as "B2". Cards Annex D9 gives the column indices | Selected-artifact check, 24 Sep 2026 |
| **Common band subset — use this** | **B2, B3, B4, B5, B6, B7, B8, B8A, B11, B12** — ten bands present at both levels, in identical order | Selected-artifact check, 20 Sep 2026 |
| **🔴 The culture-code column is named differently by level** | **`label` at L1C, `code_cultu` at L2A** — `load_culturecode_and_id` branches on it. A single hard-coded column name silently mislabels one level | Selected-artifact check, 20 Sep 2026 |
| **🔴 The default transform samples observations at random** | `get_default_transform` runs `idxs = np.random.choice(x.shape[0], sequencelength, replace=replace)` with `sequencelength = 45`. **Every call draws a fresh subset of observation dates** | Selected-artifact check, 16 Sep 2026 |
| **🔴 Label leakage in the raw columns** | The L2A raw band list includes `code_cultu`, the crop code. Exclude label and identifier columns from the feature tensor explicitly and assert it in code | Selected-artifact check |
| **Parcel-ID intersection between levels** | **99.9%** of mapped parcels in every region appear at both levels, all with the same label: 607,945 paired parcels. All but one have ≥12 matched dates with finite common bands (median 35, maximum 65). Reproduce it in Week 1. The index files differ in layout between regions and levels (byte-order mark, leading unnamed column), so read them by column name | Selected-artifact check, 24 Sep 2026 |
| **Structure** | Per-parcel Sentinel-2 time series | Source-documented |
| **Splits** | Official **NUTS-3 region partitions**. Course assignment, fixed: 2017, frh01+frh02 train, frh03 validation, frh04 test, with the parcel caps and pairing rules in Cards Annex D9 | Source-documented; Card |
| **Baselines** | Published Random Forest + 7 deep architectures | Source-documented |
| **Split unit** | **By NUTS-3 region** | Card |

**🔴 The size figure changes how this project acquires data, so read it before you plan.** 11.34 GiB kept at once for the paired comparison over the official partition exceeds the ~5 GB working-data policy in Cards Annex D0, which governs **retained** data. **Process one region at a time**: obtain its L1C and L2A files, copy out the parcels selected by Cards Annex D9, delete the region's files, and move on. Peak retained data is then one region's pair plus one archive and a compact store: **4,204,595,712 bytes at worst** (frh01 with the package loader), about 63 MB of it the compact store's upper bound aside, measured 24 Sep 2026. Report transferred, peak retained and final retained bytes. *(Changed at D1: Revision D made a permitted regional subset, agreed in Week 1, the expected path. D1 keeps all four regions and caps parcels instead.)*

**🔴 Three things must be matched, not one.** Revision B caught the band mismatch. Revision C caught the observation draw. Revision D adds the column name. The pre-issue check of 24 September adds a fourth trap on top of these three: the L1C file's column order (table above). Because `get_default_transform` re-draws on every call, two loaders over the same parcel — one at L1C, one at L2A — see **different dates**, and a global seed does not fix it, since the draw depends on which loader is constructed and iterated first. Your L1C-versus-L2A comparison then measures two random date samples plus atmospheric correction.

**Requirement:** build a **deterministic paired observation index per parcel**, compute it once, store it, and use it identically for every level, every model, in validation and test. Record unmatched observations and your cloud/missing-data policy.

**If matching cannot be achieved for enough parcels,** narrow the result to a comparison of **processing pipelines** and label it as such — which is what a defaults-versus-defaults run actually measures.

**Do not simply re-run the authors' code and report their numbers.** The published baselines are your comparison point, not your result. The class distribution is very uneven (meadows dominate) — use macro-F1.

---

## What to submit — the Week 1 readiness note

**One page per group.** This list is identical to §8 of the student handout; if the two ever disagree, tell the instructor. *(Corrected at D1: Revision D said so while the two lists differed in three items. They are now word-for-word the same.)*

1. **The numbers you got**, against the manifest, and **any mismatch** with what you think caused it.
2. **Your declared split unit**, in one sentence, **and how you built the *validation* partition** — not just train and test — with **support in each of the three partitions**. For classification, per-class counts. **For regression and forecasting projects (Track C, D1–D3, I3), report cells, dates, regions or independent events instead** — per-class counts do not apply and you should not invent them.
3. **The access route** you used, including anything that required a login, an API key or manual acceptance of terms. **Never commit a key to your repository.** A lawful manual route with an integrity check is fully acceptable and is **not** a reproducibility penalty.
4. **Your environment** — Python version, OS, pinned package versions used to parse the data.
5. **Transferred bytes and retained working bytes**, where those differ.
6. **Anything that surprised you** — a field you did not expect, a file that would not parse, a count that seemed off.
7. **🔴 Your machine, and one timed run of your card's reference configuration.** Run the reference configuration identified for your card in Annex D0's Week-1 measurement table — one of your required fits, under the D0 limits, reused later in your project and not an additional experiment. Report **hardware** (cores, RAM, operating system), **thread and data-loader worker settings**, **elapsed time and aggregate CPU time**, **epochs and optimisation updates** completed, **which limit stopped the run** (epochs, minutes or early stopping), **peak memory**, **evidence of optimisation** (training and validation loss over the run, or a documented converged state), and **whether validation and one timed inference pass over test-shaped data finished** — time it, but do not compute or look at test labels or test metrics. Comparative accuracy is not graded at this checkpoint, and beating a trivial or classical baseline is not a condition of passing it. Then **project the total required programme** against the 24-hour elapsed budget, including classical baselines and repeated inference, using the stage Annex D0 tells you to time on a subset. A fit that hits the time limit before it has learned anything is not a failure on your part — it is the finding we most need, because the D0 timing limits were set as design bounds and were not piloted on a machine like yours before your card was issued. **The instructor replies to every note by Tuesday 6 October 2026**, confirming your configuration or issuing a corrected one; a scope cut made on measured evidence carries no penalty. *(Added 24 September 2026; rewritten the same day, because "the smallest model your card requires" could be the cheapest model on the card and so miss the one that matters.)*

A machine-readable attachment for counts and split IDs is welcome and does not count against the page.

**If you find an error in this manifest, report it. That is a correct result and it will be credited.** Revision D exists because six such checks were run on the instructor's side and three of them contradicted what this document previously said — including a lot count that had been wrong since Revision B.
