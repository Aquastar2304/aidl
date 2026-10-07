# 22AIE304 — Assignment Cards

**Revision D1 · 21 September 2026 · Amendment 1 to Revision D · Issued with Student_Handout_RevD1 and Dataset_Manifests_RevD1**

**What changed in Amendment D1.** Revision D closed the open measurements. It did not complete the protocol details that a verification of Revision C, dated 16 September, had found missing, and D1 does. **Card A1 is corrected.** The five artificially damaged Paderborn training bearings named in Revisions C and D — KA01, KA03, KA05, KA07, KA09 — are **all outer-ring faults**, so A1's training side had no inner-fault example while its test side had two. KA07 and KA09 are replaced by the artificial inner-ring bearings **KI01 and KI03**. A1's CWRU validation rule is also replaced: it asked for validation "by the same unit" (the load) inside a single-load fit, which cannot be done. **Protocol Annexes D0–D9 at the end of this document are new, and they are part of every card.** They fix each card's reference setting, the number of training runs it requires and the training budget, and the exact split, window, event and pool rules that earlier cards referred to without stating. **Cards C3, I4-S, I5 and I6 gain definitions they previously referred to but did not give.** **A release calendar is added below.** Where an annex and a Revision D measurement meet, the measurement stands.

**What changed at Revision D (history).**

Six open items were closed by measurement against the artifacts rather than the record. Cards **B1**, **I3**, **I4-S**, **I5**, **I6**, **E1**, **E2** and **E3** change. **E2 is rewritten:** the built-in split turned out to be lot-disjoint already, which removed the contrast its second experiment was built on. **E1's scope statement is reversed** for the same reason. Every other card is unchanged from Revision C.

## How to read your card

Your card is the specification for your project. It names your datasets and the role each one plays, your split and validation protocol, your baseline, the models you must build, the two-model fusion pair, your **two core experiments**, your primary metrics, your scope caps and your required outputs.

**The card governs.** Where anything else in the pack — including the track and project summaries in Handout §5 and §6 — appears to require a third experiment, an extra model or a different fusion, the card wins and that extra work is optional. The manifest supplies dataset description, traps and context. *(Corrected 25 September 2026: this sentence pointed to parts of the instructor's project portfolio, which is not issued to students. Every rule it named is in the handout section given here.)*

**What the card does not override.** The common rules in Handout §4, the assessment rules in Handout §9, the ethics and licensing requirements in Handout §10 and the manifest entry for each named dataset apply to everyone. A card does not silently waive a course outcome, a grading rule or a data-use restriction. If you find a conflict in common policy, bring it to the instructor; it will be resolved and corrected in the released bundle, not decided by you mid-project. *(One such conflict was found and resolved before release, 24 September 2026: the common derived-sample rule now names the Track A guarded within-recording blocks and the I4-S guarded within-scene reference as approved within-unit protocols, so following those cards no longer breaks it.)*

**Component demonstration versus research comparison.** Every project must demonstrate a 1-D model, a 2-D model, an attention module with its ablation and the named fusion. Unless your card says otherwise, those run **once, on the card's reference setting**. Only the model–condition combinations listed under your two core experiments are repeated. This is what stops "two experiments" turning into model × condition × split × repeat.

**Uncertainty.** Run only the uncertainty or repetition procedure your card specifies. Where none is specified, report the sample and event counts behind each number and acknowledge the limits of a single run; do not claim significance or equivalence. Broad multi-seed studies are optional after the semester.

**Files issued with your card.** Every file a card or annex says is "issued with the cards" comes in the release bundle with its full SHA-256. Check the hash of each file you receive before you use it, and report any mismatch at once; a mismatched file is not the issued one. *(Added 24 September 2026.)*

**Choices that remain yours,** inside the stated bounds: optimizer and learning-rate schedule, batch size, an early-stopping rule within Annex D0's limits, a justified feature-extraction parameter, and the engineering of the pipeline.

## Which card is yours

Each card names its team by the team's allocation number.

| Team | Card | Project |
|---|---|---|
| 1 | I2 | Individual — ECG diagnostic superclasses |
| 2 | C1 | Track C — ENSO |
| 3 | C2 | Track C — ENSO |
| 4 | I3 | Individual — battery early-life prediction |
| 5 | I1 | Individual — satellite telemetry anomaly detection |
| 6 | A1 | Track A — Bearings |
| 7 | E1 | Track E — Wafer maps |
| 8 | E2 | Track E — Wafer maps |
| 9 | B1 | Track B — Crop disease |
| 10 | A2 | Track A — Bearings |
| 11 | B2 | Track B — Crop disease |
| 12 | I6 | Individual — crop mapping (BreizhCrops) |
| 13 | C3 | Track C — ENSO |
| 14 | D1 | Track D — Traffic / graph deep learning |
| 15 | B3 | Track B — Crop disease |
| 16 | I4-S | Individual — landslide detection (Landslide4Sense) |
| 17 | A3 | Track A — Bearings |
| 18 | E3 | Track E — Wafer maps |
| 19 | I5 | Individual — bird species from audio |
| 20 | D2 | Track D — Traffic / graph deep learning |
| 21 | D3 | Track D — Traffic / graph deep learning |

Card I4 (3-D printing errors, CAXTON) is withdrawn and not issued; Team 16 takes Card I4-S. *(Added 26 September 2026: earlier drafts numbered groups 1–21 in card order, A1 to I6. The cards now carry the issued team numbers.)*

## Release calendar

| Event | Date |
|---|---|
| Project titles allocated | Completed before this pack was issued |
| **Cards, annexes and full project details issued.** Register any gated account your card names (for example the xeno-canto API key) **on the day you receive your card** | By Saturday 26 September 2026 |
| Week 1 begins | Monday 28 September 2026 |
| Dataset readiness note due | **Friday 2 October 2026** — the last day of Week 1, and its fifth working day |
| End of Week 2: proposal, baseline numbers, split-ID files | Friday 9 October 2026 |
| End of Week 5: mid-project demo, every component including the fusion, plus a preliminary run of your core experiment | Friday 30 October 2026 |
| End of Week 7: results freeze | Friday 13 November 2026 |
| Week 8: report, repository, presentation and individual defense | **Not yet fixed.** Project presentations across all courses begin on or after Wednesday 18 November 2026; the 22AIE304 presentation schedule, and the report and repository deadlines, will be announced close to Friday 13 November |

**Weeks run Monday to Friday; Saturdays and Sundays are holidays.** Week 1 28 Sep – 2 Oct · Week 2 5 – 9 Oct · Week 3 12 – 16 Oct · Week 4 19 – 23 Oct · Week 5 26 – 30 Oct · Week 6 2 – 6 Nov · Week 7 9 – 13 Nov 2026. Every deadline falls on the Friday that ends its week. *(Changed 26 September 2026: weeks were entered as Saturday to Friday, which put the weekend inside each week. They now follow the working week, Monday to Friday; Saturdays and Sundays are holidays. **No deadline moves** — every deadline stays on the same Friday — and your card still arrives on Saturday 26 September, the weekend before Week 1.)* **Week 8 follows the results freeze; its dates are not yet fixed** (see the table). *(Changed 26 September 2026: Week 8 was entered as Saturday 14 – Friday 20 November. Project presentations across all courses begin on or after Wednesday 18 November, and the 22AIE304 slot within them is not yet known, so the Week-8 dates are withdrawn rather than guessed. Weeks 1–7 and every deadline up to the results freeze are unchanged.)*

**Who checks what.** Before a card is issued, the instructor confirms a feasible data route and the support it needs. Where your source needs an account, you register on the day you receive your card. **Within the first five working days of Week 1 — Monday 28 September to Friday 2 October — you reproduce the acquisition, counts and splits independently.** *(Restated 24 September 2026. The rule previously said "the first 3–5 days". Week 1 then opened on a Saturday, so counting calendar days put the deadline on its third working day.)*

*(Corrected at D1: Revisions C and D told you the allocation date was stated on your card. No card carried one. The dates live in this table. A revision date is not an allocation date.)*

*(Dates entered 24 September 2026. Earlier drafts of this table carried three rows before Week 1 — preferences close, allocation notice, examinations — and put gated-account registration in the gap between the allocation notice and the first examination. For this cohort that gap no longer exists: the project titles were allocated before this pack was ready, and the mid-semester examinations are over. Those three rows are withdrawn, and registration moves to the day you receive your card, which is at most six days before your readiness note is due. If your card names a gated account, register the same day and say in your readiness note that the account works.)*

---

# TRACK A — BEARINGS (Catalogue P32)

Shared in Weeks 1–2: one download and preprocessing script, one EDA, one baseline implementation. **You share code, not split membership.** Each of the three groups reproduces the baseline under its own protocol, and there is one baseline result per protocol, not one number per track.

## Card A1 — Team 6 · Strategy S4 · Catalogue P32

**Execution contract.** Annex D0 fixes this card's reference setting, required training runs and budget; Annex D1 fixes the protocol details. Both are part of this card.

**Datasets and roles.** CWRU Bearing Data Center — **mandatory, primary**. Paderborn KAt — **mandatory, transfer study**. No other dataset.

**Task and labels.** Multi-class fault classification. Two label maps, never merged: CWRU **healthy / inner / outer / ball**; Paderborn **healthy / inner / outer**. The three combined-fault Paderborn bearings (KB23, KB24, KB27) are excluded.

**Split and validation.** Use Annex D1. For each CWRU source load, train and validate on separated time blocks within that load; evaluate on fixed held-out blocks at all four loads, including the within-load diagonal. This is a guarded within-recording protocol, not unseen-bearing generalisation. Paderborn uses the explicit, bearing-disjoint train/validation/test IDs in D1; healthy IDs are also disjoint.

**Baseline.** Envelope analysis at the characteristic defect frequencies, reproduced under both protocols.

**Required models.** Small 1-D CNN on raw vibration windows; small 2-D CNN on spectrograms; frequency attention in the image model with its no-attention ablation. **Fusion pair: the 1-D vibration model with the spectrogram model**, weights fixed on validation only.

**Core experiment 1.** CWRU cross-load transfer with the **no-attention 1-D CNN** and envelope baseline: four source-load fits of each evaluated on four held-out target loads. Demonstrate the other components only at the 0-hp reference; do not repeat the image model, attention or fusion across the matrix.

**Core experiment 2.** Paderborn artificial-damage → natural-damage transfer at N15_M07_F10, bearing-disjoint, with the same no-attention 1-D architecture and its independently fitted envelope baseline. Use the three-class output for this dataset.

**Primary metrics.** Macro-F1 and per-fault recall with support are primary. Also report accuracy and the within-load versus cross-load accuracy change on CWRU. For Paderborn report source-validation and natural-test performance separately; their difference is descriptive because bearing populations differ. Report KI04 separately in the error analysis (Annex D1).

**Scope caps.** Download **only the approved bearing archives** listed below — the Paderborn repository ships **32 per-bearing `.rar` archives of 152–178 MB each (≈5.1 GB in total)** and there is **no per-condition archive**, so selecting N15_M07_F10 reduces what you retain, not what you transfer. Approved subset: healthy **K001, K002, K003, K004**; artificial **KA01, KA03, KA05, KI01, KI03**; natural **KA04, KA15, KA22, KI04, KI16** — fourteen archives, **2,356,527,381 B (2.19 GiB) transferred** (measured 24 September 2026). Extract and retain N15_M07_F10 records only. Extracted whole, those 280 records are 2.45 GB, more than the archives, because the archives are compressed; keep the vibration channel, which the card uses, and you retain about a twentieth of that. **Report transferred archive bytes separately from retained working bytes.** CWRU acquisition is restricted to the sixteen recordings in D1; window caps and preprocessing are specified there.

**🔴 Corrected at D1 — the artificial-damage archive list.** Revisions C and D approved artificial **KA01, KA03, KA05, KA07 and KA09**. In the Paderborn scheme every KA bearing is an outer-ring fault and every KI bearing an inner-ring fault (Lessmeier et al., Table 4), so that list gave your training side **no inner-fault example** while your natural-damage test side has two (KI04, KI16). The inner class would have failed as an unseen class, and the failure would have been read as a damage-origin effect. KA07 and KA09 are replaced by the artificial inner-ring bearings **KI01 and KI03**. The count stays at fourteen archives. The partition table is in Annex D1.

**Required outputs.** Readiness note; declared split with published IDs; baseline result per protocol; the four required components; both core experiments; error analysis; 4–6 page report; repository; defense.

**Read carefully.** Same-rig artificial-to-natural transfer **reduces rig-related confounding; it does not isolate damage origin** — the artificially damaged and naturally degraded bearing populations differ in which bearings they are and in damage extent. State the narrower claim. Do not compare gap magnitudes across CWRU and Paderborn causally.

**Optional, credited:** CWRU→Paderborn cross-rig transfer.

## Card A2 — Team 10 · Strategy S2 · Catalogue P32

**Execution contract.** Annex D0 fixes this card's reference setting, required training runs and budget; Annex D1 fixes the protocol details. Both are part of this card.

**Datasets and roles.** CWRU — **mandatory, primary**. Paderborn — **optional**; you have no obligation to train any variant on it.

**Task and labels.** CWRU four-class fault classification.

**Split and validation.** Use the fixed guarded 60/20/20 time blocks for the D1 CWRU recording set, pooling loads within each partition. Hold membership constant across all compared models. This estimates within-recording generalisation, not unseen-bearing performance.

**Baseline.** Envelope analysis at the characteristic defect frequencies.

**Required models.** 1-D CNN; spectrogram CNN; frequency attention with ablation. **Fusion pair: 1-D vibration model with spectrogram model.**

**Core experiment 1.** 1-D CNN versus spectrogram CNN versus envelope analysis under **two separately reported matching regimes: matched trainable-parameter count, and matched CPU time.** These are two comparisons, not one condition.

**Core experiment 2.** Cost comparison built **from the fits of experiment 1** — no new training runs. Report preprocessing, training and inference time on the same machine and thread count, and **total and trainable parameters separately**.

**Primary metrics.** Macro-F1 and per-fault recall; wall-clock training time; CPU inference latency per window; parameter counts. A Pareto plot of macro-F1 against cost is the headline figure; accuracy is supplementary.

**Scope caps.** CWRU only unless you choose the optional Paderborn leg, in which case the A1 archive list and byte-reporting rule apply. No hyperparameter sweep is required.

**Read carefully.** Envelope analysis has **no comparable neural parameter count**, and a frozen backbone hides both its total parameter count and its feature-extraction cost. Do not construct an artificial parameter match for the classical method. Published CWRU scores are contextual and are not comparable once the protocol is rescoped.

## Card A3 — Team 17 · Strategy S1 · Catalogue P32

**Execution contract.** Annex D0 fixes this card's reference setting, required training runs and budget; Annex D1 fixes the protocol details. Both are part of this card.

**Datasets and roles.** CWRU — **mandatory, primary**. Paderborn — **optional**.

**Task and labels.** CWRU four-class fault classification, one fixed model architecture throughout.

**Split and validation.** Use the guarded-block reference in Annex D1 because the selected set contains one healthy recording per load. Partition time first, then cut windows; report the narrower within-recording claim. The separate random overlapping-window audit deliberately violates this protection.

**Baseline.** Envelope analysis, reproduced under the guarded-block protocol of Annex D1.

**Required models.** 1-D CNN; spectrogram CNN; frequency attention with ablation. **Fusion pair: 1-D with spectrogram.**

**Core experiment 1.** The valid reference: one fixed model under the guarded-block protocol of Annex D1.

**Core experiment 2.** The **audit control**: the same fixed model under an overlapping-window split cut from shared recordings. Quantify the inflation, with recording IDs and the class and load support of each partition reported.

**Primary metrics.** Macro-F1 and per-fault recall under both protocols; the inflation gap as the headline; error analysis drawn from the same comparison.

**Scope caps.** One **research** architecture, the no-attention 1-D CNN, under two protocols. The image model and attention ablation run only on the valid reference; they are still required component demonstrations. CWRU only; Paderborn remains optional.

**Read carefully.** ***Non-overlapping* is not *recording-disjoint*.** Windows that do not overlap can still come from one recording and remain strongly correlated. And moving to a different recording may also change fault type, severity or load, so the measured gap is not a pure overlap effect unless those are held fixed.

**Audit-control exemption applies.** The deliberately overlapping run in experiment 2 is asked for by this card. It is a **deliberately leaky audit control, exempt from the leakage penalty**, and attracts **no cap**, provided you label it explicitly as an audit control and keep the valid-protocol result as your headline.

---

# TRACK B — CROP DISEASE (Catalogue P45)

Shared in Weeks 1–2 as above. All three groups use the **issued PlantVillage split**, `PlantVillage_color_split.csv`, which keeps every leaf group in one partition. Annex D2 says how it was built and why the published 80/20 split is not used as it stands.

## Card B1 — Team 9 · Strategy S4 · Catalogue P45

**Execution contract.** Annex D0 fixes this card's reference setting, required training runs and budget; Annex D2 fixes the protocol details. Both are part of this card.

**Datasets and roles.** PlantVillage, **authors' repository `raw/color/`** — mandatory source domain. **Cropped-PlantDoc** — mandatory **target test set only**.

**The target set is now pinned.** `github.com/pratikkayal/PlantDoc-Dataset` at commit **`5467f6012d78d1c446145d5f582da6096f852ae8`** (frozen since 2 May 2021), CC BY 4.0. **2,578 image files: 2,342 train, 236 test.** 28 class folders under `train/`, 27 under `test/`. Counted 20 September 2026. The 2,598 figure in the PlantDoc paper counts data points; this release is not a per-bounding-box release and there is no multiple-crops-per-parent structure in it.

**Task and labels.** Multi-class disease classification on the **common label intersection** of the two datasets. The common-label map is frozen and issued with this card as `B1_common_label_map.csv`. **28 Cropped-PlantDoc classes map one-to-one to 28 PlantVillage classes**, and 27 of them have target test images (236 in total). The other **10 PlantVillage classes have no Cropped-PlantDoc counterpart and are excluded in both domains**: Apple black rot, Cherry powdery mildew, Corn healthy, Grape esca, Grape leaf blight, Orange Haunglongbing, Peach bacterial spot, Potato healthy, Strawberry leaf scorch and Tomato target spot. Reproduce the map independently in Week 1 and report any disagreement; the issued file governs, and your readiness note publishes your version as a machine-readable file.

**🔴 The evaluable target label set is 27, not 28.** *Tomato two spotted spider mites leaf* has **two training images and zero test images**. Under the shipped split that class has no target support: report it as unsupported under the common absent-class rule. Do not drop it silently from a macro-average and do not manufacture support for it.

**Split and validation.** Source: **by leaf group** — for the 13 classes where the leaf map is missing or partial, a group is one photograph, not one leaf (Annex D2), so the source split is not leaf-disjoint there; say so. Target: the shipped Cropped-PlantDoc split. Model selection and augmentation choice use **source validation only**; the target test partition stays untouched until the final run.

**🔴 The shipped target split does not respect parent-photograph grouping — this was checked, and it fails.** Revision C told you to verify it. The measurement: 2,578 files carry only **2,566 distinct MD5 hashes**; twelve byte-identical groups, eleven of them spanning train and test. Perceptual hashing finds **16 cross-split near-duplicate pairs covering 15 of the 236 test images**, and all 16 were inspected by eye. **Publish the duplicate list in your readiness note.** You are not required to repair the benchmark; you are required to know this and to say what it does to your numbers.

**🔴 Eight identical photographs carry two different disease labels across the split.**

| File | Train label | Test label |
|---|---|---|
| `2015070295153021.jpg` | Corn Gray leaf spot | Corn leaf blight |
| `corn-gray-leaf-spot-f4.jpg` | Corn Gray leaf spot | Corn leaf blight |
| `IMG_42231.jpg` | Corn leaf blight | Corn Gray leaf spot |
| `1421_0.jpeg?itok=FMtmgePj.jpg` | Potato leaf early blight | Potato leaf late blight |
| `5816740026_d42ef24413_Phytophthora-Infestans.jpg` | Potato leaf early blight | Potato leaf late blight |
| `irish-blight-symptoms-on-potato-leaves-atmf8b.jpg` | Potato leaf early blight | Potato leaf late blight |
| `backus-056-potato-blight.jpg` | Potato leaf late blight | Potato leaf early blight |
| `tomato_V8.jpg` | Tomato Septoria leaf spot | Tomato leaf bacterial spot |

A ninth identical pair sits inside `train/` (Potato early `18028_1.jpg` / Potato late `24064_1.jpg`).

**Baseline.** HSV colour histograms plus LBP texture with a random forest, on the identical split.

**Required models.** 1-D colour/texture profile CNN; 2-D transfer-learning CNN (MobileNetV2 at 128×128, frozen then partially fine-tuned, as fixed in Annex D0); CBAM with ablation. **Fusion pair: profile model with image model.** Test-time augmentation is **not** required and must not be added to the fusion.

**Core experiment 1.** PlantVillage→PlantVillage versus PlantVillage→Cropped-PlantDoc on the common labels, same model.

**Core experiment 2.** On the 2-D image model only: colour jitter, random occlusion, and their combination against the unchanged colour control. The two families and settings are fixed before test evaluation; source validation selects no target-informed variant. Exact caps and fits: Annex D2.

**Primary metrics.** Macro-F1 and per-class recall in both domains, with per-class support in both; the in-domain-versus-field gap as the headline. **Report your own measured in-domain result** beside the field result; a published near-99% figure is background context with its source and differing protocol identified, and is neither a required result nor a tuning target.

**🔴 Report the headline gap twice: with and without the affected classes** (Corn grey-leaf-spot/northern-leaf-blight, potato early/late blight and Septoria/bacterial spot). The cross-partition conflicts demonstrate inconsistent annotation and make the affected target labels questionable; they do not by themselves establish a ceiling on test macro-F1 or determine which label is correct. Report the fixed-universe result and the prescribed sensitivity analysis excluding the affected classes. Interpret differences cautiously and do not relabel the target using model predictions. *(Corrected 24 September 2026: this said the conflicts put "a ceiling on achievable macro-F1" on the confusable pairs and that the confusion there is "partly the benchmark's own label noise". B1 never trains on PlantDoc's training partition, and a conflict across partitions does not show which of the two labels is wrong, so neither claim follows. The remaining classes are not thereby verified clean, and the source–target gap also reflects target class support, not only acquisition conditions.)*

**Scope caps.** Two augmentation families and their combination, on the 2-D image model only; one backbone; one fine-tuning schedule. Per-class image caps are in Annex D2.

**Required outputs.** Readiness note including the duplicate list and the published label map; the four required components; both core experiments with the gap reported both ways; error analysis; report; repository; defense.

**Confirm the count yourself in Week 1** against the figures above and report any discrepancy. A documented mismatch costs you nothing.

## Card B2 — Team 11 · Strategy S3 · Catalogue P45

**Execution contract.** Annex D0 fixes this card's reference setting, required training runs and budget; Annex D2 fixes the protocol details. Both are part of this card.

**Datasets and roles.** PlantVillage **colour, segmented and greyscale** releases from the authors' repository — all mandatory. PlantDoc is **not required** for this project.

**Task and labels.** Multi-class disease classification over the 38 PlantVillage classes.

**Split and validation.** **By leaf group** using Annex D2, with the **same leaf groups and the same original-image IDs matched across all three representations** — colour, segmented and greyscale must be aligned image-for-image, or the intervention is confounded by a different split. The alignment is issued as `PlantVillage_B2_alignment.csv` (Annex D2). Validation from training leaf groups only.

**Baseline.** HSV colour histograms plus LBP texture with a random forest.

**Required models.** 1-D colour/texture profile CNN; 2-D transfer-learning CNN; CBAM with ablation. **Fusion pair: profile model with image model.**

**Core experiment 1.** **Background-removal intervention**: retrain on the segmented release against a matched control on the colour release, identical split and budget. Inspect and report mask quality on a sample.

**Core experiment 2.** **Greyscale versus colour** under the same split, with an intervention-based attribution check.

**Primary metrics.** Macro-F1 and per-class recall for each representation; the macro-F1 and per-class-recall change under each intervention as the headline.

**Scope caps.** Three representations, one backbone. No annotation work.

**Read carefully.** **Report leaf-versus-background attribution only.** Quantified overlap between attention and **lesions** is out of scope: no lesion masks exist for this dataset, and a heatmap over an unannotated region is a hypothesis, not a measurement.

**An intervention that does not degrade the prediction is a result, not a failure.** Report the observed effect either way; where practical, compare against a matched control intervention so generic input damage is not mistaken for evidence about attention.

## Card B3 — Team 15 · Strategy S1 · Catalogue P45

**Execution contract.** Annex D0 fixes this card's reference setting, required training runs and budget; Annex D2 fixes the protocol details. Both are part of this card.

**Datasets and roles.** PlantVillage authors' repository — mandatory. PlantDoc — **optional**. If you use it, the count, the split contamination and the label inconsistency recorded on Card B1 apply to you too.

**Task and labels.** Multi-class disease classification over the **19 eligible classes** listed in Annex D2, analysed per class and per crop species.

**Split and validation.** By leaf group. **Validation and test partitions stay fixed across every training cap.**

**Baseline.** HSV plus LBP with a random forest.

**Required models.** 1-D profile CNN; 2-D transfer-learning CNN; CBAM with ablation. **Fusion pair: profile with image model.**

**Core experiment 1.** Per-class and per-crop recall against training support for the fixed eligible class set in Annex D2. Usable recall means ≥0.70; report its leaf-group bootstrap interval and do not call a point estimate a guaranteed threshold.

**Core experiment 2.** Nested training caps of **10, 25 and 50 leaf groups per eligible class**, fixed validation and test, for the 2-D image model. The 50-group condition is the reference. Eligibility and total image bounds are fixed in Annex D2.

**Primary metrics.** Per-class recall against support (primary); macro-F1; the smallest tested leaf-group cap reaching the declared recall threshold, with actual image counts and uncertainty; report “not reached” when appropriate.

**Uncertainty procedure (required, bounded).** Report uncertainty on per-class recall by **bootstrapping over leaf groups using predictions you already have**. No repeated training.

**Scope caps.** Three caps, one architecture, one backbone.

---

# TRACK C — ENSO (Catalogue P49)

**One product snapshot for the whole track.** Use **NOAA CPC's ERSST v5 Niño 3.4 file** (`ersst5.nino.mth.91-20.ascii`) and **PSL's ERSST v5 grid** (`sst.mnmean.nc`), restricted to **January 1950–December 2024**. Annex D3 defines the histories, the chronological target periods and the course event convention. The instructor's snapshot and checksums are issued with the cards, and you reproduce them. Check the version inside every file you download, not the page that links it, and do not substitute ERSST v6. *(Corrected 23 September 2026: earlier issues named PSL's Niño 3.4 series page. The file it links now reads ERSST V6 in its own footer, so that route is withdrawn. See Annex D3.)*

**Gridded SST is a track-wide input, not a C2 resource.** Every group needs it for the required 2-D representation and the named fusion. It is demonstrated on the reference setting and need not be rerun across every condition.

**Fixed lead times for all three groups: 1, 3, 6, 9 and 12 months.** Five leads. Not twelve.

**Forecast boundary rule for all three groups.** Chronological splitting alone is not enough: at a 12-month lead, an example issued in month *t* has its target at *t*+12. **Every output target in a training example must lie in the training period, and every validation target in the validation period. No test-period target enters model selection.** Earlier input history may cross a partition boundary if it was available at issue time. Fit every learned preprocessing step, including anomaly standardisation, on training data only, and distinguish a fixed published climatology from a statistic estimated over held-out course data. *(Corrected at D1: the earlier rule protected the training boundary only, which left validation targets free to run into the test period.)*

## Card C1 — Team 2 · Strategy S5 · Catalogue P49

**Execution contract.** Annex D0 fixes this card's reference setting, required training runs and budget; Annex D3 fixes the protocol details. Both are part of this card.

**Datasets and roles.** NOAA CPC ERSST v5 Niño 3.4 index, 1991–2020 base (monthly, 1950/01→) — mandatory primary. NOAA ERSST v5 gridded SST — **mandatory**, for the required image and fusion component. Subsurface heat content — **optional**, needs an approved versioned source first.

**Task and labels.** Multi-step regression of the pinned ERSST v5 Niño 3.4 series at the five fixed leads, with the exact product and course event convention in D3. CPC ONI is contextual only and is not substituted into the target or event computation.

**Split and validation.** Annex D3: 24-month input history; training targets through December 1994, validation targets January 1995–December 2004, test targets January 2005–December 2024; every five-output target vector must stay wholly within its partition.

**Baseline.** Persistence and a fitted autoregressive model.

**Required models.** LSTM and TCN on the index (both are required here — the contrast **is** the question); a small 2-D CNN on Pacific SST-anomaly maps; temporal attention with ablation. **Fusion pair: the index sequential model with the SST-map CNN**, weights fixed on validation only.

**Core experiment 1.** Skill by **forecast initialisation month × lead time**, resolving the spring dip explicitly.

**Core experiment 2.** LSTM versus TCN versus AR versus persistence across barrier-crossing and non-crossing windows.

**Primary metrics.** Anomaly correlation coefficient and RMSE by initialisation month and lead; a month × lead heatmap is the headline figure.

**Scope caps.** **One model per architecture, with skill stratified by initialisation month afterwards. Do not train twelve monthly models.** The grid model runs once on the reference setting.

**Read carefully.** Index forecasts by **initialisation** month, not target month. Getting this wrong makes the whole analysis meaningless.

## Card C2 — Team 3 · Strategy S2 · Catalogue P49

**Execution contract.** Annex D0 fixes this card's reference setting, required training runs and budget; Annex D3 fixes the protocol details. Both are part of this card.

**Datasets and roles.** The same index and gridded snapshot as C1 and C3 — both mandatory.

**Task and labels.** As C1, at the five fixed leads, same pinned product.

**Split and validation.** Identical boundaries to C1 and C3, same forecast information cutoff, same permitted histories, same target months.

**Baseline.** Persistence and AR.

**Required models.** Index-only LSTM and 2-D CNN on SST-anomaly maps, both **fixed in Annex D3 at 29,657 and 30,229 trainable parameters** — the LSTM on this card is 84 units wide, not C1's 32; temporal attention with ablation. **Fusion pair: index model with map CNN.** *(Corrected 24 September 2026; see Annex D3.)*

**Core experiment 1.** Sequential-system versus spatial-system comparison at matched budget across the five leads.

**Core experiment 2.** Lead-wise skill and CPU cost **from the same fits**.

**Primary metrics.** ACC and RMSE by lead; parameter counts; CPU training time.

**Scope caps.** One LSTM, one CNN and the fixed Pacific grid/history in Annex D3. No architecture sweep.

**Read carefully.** This is a comparison of **representation-and-model systems**. The grid model differs from the index model in input *and* architecture simultaneously, so it does not isolate what the spatial field contributes. Say so; do not claim more.

## Card C3 — Team 13 · Strategy S1 · Catalogue P49

**Execution contract.** Annex D0 fixes this card's reference setting, required training runs and budget; Annex D3 fixes the protocol details. Both are part of this card.

**Datasets and roles.** Same index and gridded snapshot — mandatory. Subsurface heat content — **optional**, approved versioned source required first.

**Task and labels.** Five-output Niño 3.4 regression as C1. Annex D3 defines a retrospective **course event convention** from the same target series: five consecutive centred three-month means at or above +0.5°C (warm), or at or below −0.5°C (cold); strong events reach +1.5°C or −1.5°C respectively. This is not a claim to reproduce official ONI classifications.

**Split and validation.** As the track rule. The event definition is retrospective. A forecast issued in month *t* may use only months *t*−23 to *t* (Annex D3), never event membership.

**Baseline.** Persistence and AR, evaluated on the same event and neutral partitions.

**Required models.** Index-only LSTM (fixed in Annex D3); SST-map CNN; temporal attention with ablation. **Fusion pair: index model with map CNN.**

**Core experiment 1.** Forecast error on strong warm and strong cold events versus neutral conditions.

**Core experiment 2.** Persistence-relative and AR-relative RMSE skill for forecasts **whose target month is the event onset**, at each of the five leads; onset, neutral selection and skill formula are defined in Annex D3. Reuse experiment 1 predictions; no new fits.

**Primary metrics.** Event-weighted RMSE by phase and lead; ACC where defined; onset skill separately against persistence and AR. Report independent event counts and undefined/unsupported cells explicitly. The neutral comparison and weighting are fixed in Annex D3.

**Scope caps.** One sequential architecture, one CNN. No new covariates in the core.

*(Corrected at D1: Revisions C and D said "the card defines the onset month and the neutral comparison period." The card did not. Annex D3 now defines event persistence, strength, onset, the neutral exclusion, event weighting and the skill formula.)*

---

# TRACK D — TRAFFIC / GRAPH DEEP LEARNING (Catalogue P55)

**Scope note for all three groups.** The **graph model is the core architectural contribution**. The per-sensor model, the sensor×time image model and the historical average are **controls and alternative representations**, not four systems to be engineered to equal depth. Build one good graph model and three deliberately simple, fairly budgeted comparators.

**Adjacency provenance, required of all three.** Record the adjacency file, the sensor order, the distance threshold, whether the matrix is treated as directed, and the self-loop convention. **Edge counts depend on all of those**: METR-LA's 1,515 and PEMS-BAY's 2,369 are counts under the DCRNN generator's conventions, not universal checksums. Compare counts only under the same convention, and **never alter a correct graph to match an unqualified literature count.** Confirm the adjacency is not accidentally the identity before training.

**Missing-value semantics, required of all three.** A zero in these files is a **missing reading, not a measured speed of zero**. Build an explicit mask, keep masked positions out of the loss and out of MAE/RMSE/MAPE. Fit scalers on the training partition only.

## Card D1 — Team 14 · Strategy S2 · Catalogue P55

**Execution contract.** Annex D0 fixes this card's reference setting, required training runs and budget; Annex D4 fixes the protocol details. Both are part of this card.

**Datasets and roles.** METR-LA — mandatory primary. PEMS-BAY — **optional**.

**Task and labels.** Multi-horizon speed forecasting at 15, 30 and 60 minutes across all sensors.

**Split and validation.** Chronological **70/10/20**, the DCRNN convention. Never random.

**Baseline.** Historical average by time-of-day-and-weekday, and ARIMA.

**Required models.** GCN or diffusion-convolution layer stacked with a temporal component; **one weight-shared per-sensor model applied across sensors — not 207 separately trained LSTMs**; a 2-D CNN on the sensor×time matrix; graph attention with ablation. **Fusion pair: graph model with per-sensor model.**

**Core experiment 1.** Four research systems: GCN+GRU, weight-shared per-sensor LSTM, sensor×time CNN and historical average, at 15/30/60 minutes. ARIMA is an additional bounded baseline demonstration, not a fifth model family to tune. Annex D4 specifies the common CPU allowance and ARIMA scope.

**Core experiment 2.** An **error-versus-compute Pareto curve built from those same fits**, not from new ones.

**Primary metrics.** MAE, RMSE, MAPE per horizon; CPU training time; parameter counts.

**Scope caps.** One graph architecture, one temporal component, one image model. METR-LA only unless you take the optional replication.

## Card D2 — Team 20 · Strategy S3 · Catalogue P55

**Execution contract.** Annex D0 fixes this card's reference setting, required training runs and budget; Annex D4 fixes the protocol details. Both are part of this card.

**Datasets and roles.** METR-LA — mandatory primary. PEMS-BAY — **optional, and only if explicitly budgeted**.

**Task and labels.** As D1, one fixed model architecture across all adjacency conditions.

**Split and validation.** Chronological 70/10/20.

**Baseline.** Historical average and ARIMA, plus the per-sensor control.

**Required models.** One graph model, fixed across conditions; per-sensor control; sensor×time image model; graph attention with ablation. **Fusion pair: graph model with per-sensor model.**

**Core experiment 1.** Geographic, training-data-derived, identity, and ten mismatched adjacencies, **each fitted from scratch with the same no-attention GCN+GRU architecture and training seed**: 13 graph fits in total. Permute graph indices relative to fixed signals. Annex D4 defines the learned graph, seeds and CPU limits; these are topology-realisation comparisons, not a multi-seed training study. Permuting the graph and the signals together is an isomorphism: it relabels the nodes and changes nothing.

**Core experiment 2.** On the geographic reference only, quantify the relation between attention weights and supplied finite road distances, then remove the highest-weight 10% and 30% of non-self edges versus matched seeded random removals. Freeze parameters: no retraining for this sensitivity analysis. Reuse the same test inputs (Annex D4).

**Primary metrics.** MAE, RMSE, MAPE per horizon per adjacency condition; correlation between learned edge weight and road distance; the sensitivity curve.

**Scope caps.** One architecture. Ten permutations. Four adjacency conditions. No second city unless budgeted.

**🔴 The conclusion this experiment supports.** If the mismatched graph performs nearly as well, the supportable conclusion is that **the tested road alignment gave no detectable gain under this protocol** — *not* that the model ignores topology, and not that topology is irrelevant.

**Architectural check, required before the identity control means anything.** An identity adjacency removes cross-node exchange **only if no other component of your model mixes nodes**. State where node mixing can occur in your architecture and show that the identity run removes all of it. A dense layer over the sensor axis anywhere in the network silently invalidates this control.

## Card D3 — Team 21 · Strategy S4 · Catalogue P55

**Execution contract.** Annex D0 fixes this card's reference setting, required training runs and budget; Annex D4 fixes the protocol details. Both are part of this card.

**Datasets and roles.** METR-LA — mandatory primary. PEMS-BAY — **mandatory, bounded replication only**.

**Task and labels.** As D1, under test-time input masking.

**Split and validation.** Chronological 70/10/20.

**Baseline.** Historical average, ARIMA and the per-sensor control, all under the same masking.

**Required models.** Graph model; weight-shared per-sensor model; sensor×time image model; graph attention with ablation. **Fusion pair: graph model with per-sensor model.**

**Core experiment 1.** Paired degradation curves, graph versus non-graph, masking sensor **inputs at test time on known nodes** at rates **0, 5, 10, 20, 30 and 40 per cent**, with **block outages of 12 consecutive steps** distinguished from independently missing entries, scored only where ground truth is observed, using the **same masks and the same seed list (5 seeds) for every model compared**.

**Core experiment 2.** A bounded repeat of that protocol on PEMS-BAY.

**Primary metrics.** MAE, RMSE, MAPE per horizon per masking rate, on observed targets only; degradation slope as the headline.

**Scope caps.** Two trained research models per city: graph and shared per-sensor. Six rates × two outage types × five **mask seeds**, with no retraining per mask. Historical-average and ARIMA baseline scores reuse fitted models; the image and attention demonstrations run only on clean METR-LA. Annex D4 fixes inputs, indicators and PEMS-BAY bounds.

**Read carefully.** The METR-LA/PEMS-BAY contrast changes city, network, period and much else besides failure rate, so experiment 2 is a **replication, not a controlled comparison of missingness**. Missing readings, temporarily unavailable sensors and entirely unseen nodes are three different tasks; only the first is core, and inductive prediction at unseen nodes is out of scope.

---

# TRACK E — WAFER MAPS (Catalogue P30, WM-811K)

**The three groups do not share one split.** E1 and E3 use the dataset's built-in `trainTestLabel`; E2 builds its own lot-disjoint partitions. Share the loader, the preprocessing and the baseline *code*; do not assume shared split membership or a single baseline number.

**Categorical values, required of all three.** Wafer-map values are categorical — outside-wafer, good die, bad die. **Any interpolating resize invents values that mean nothing.** Use nearest-neighbour or padding, and report per-class and per-lot counts **before and after** the transform.

**Absent classes, required of all three.** A class with no support in an evaluation partition is **reported as unsupported**. It is not silently dropped from a macro-average.

**Acquisition.** The original MIR Lab corpus is a direct, no-login download: `http://mirlab.org/dataSet/public/MIR-WM811K.zip`, **344,542,743 bytes transferred**, SHA-256 `81431a81ceac0e96caef08f50aaecc4970edc56e7df7703ee17fb9e321853eef`. Inside it, `MIR-WM811K/Python/WM811K.pkl` is **2,022,961,642 bytes uncompressed**. **328.6 MiB transferred, 1.88 GiB retained.** Report both.

**🔴 How this pickle encodes a missing label — a trap the instructor's own script fell into.** Labelled rows carry a plain string in `failureType` and `trainTestLabel`. **Unlabelled rows carry `array([0, 0], dtype=uint64)`** — a two-element zero array, not an empty one and not `NaN`. A filter such as "failureType is non-empty" therefore counts all 811,457 wafers as labelled. Test for a string. The correct counts are **172,950 labelled, 638,507 unlabelled**, and they are your first readiness check.

**🔴 The built-in split, measured on the source pickle on 21 September 2026. This settles what E1 and E3 may claim, and it changes E2.**

| | Training | Test |
|---|---|---|
| Labelled wafers | **54,355** | **118,595** |
| Lots | **5,809** | **4,953** |
| **Lots in both** | **0** | |
| Defect-pattern wafers | 17,625 (32.4%) | 7,894 (6.7%) |
| `none` | 36,730 (67.6%) | 110,701 (93.3%) |
| Distinct wafer shapes | 335 | 51 (40 shared) |
| Wafers whose shape never occurs in the other partition | 16,269 (29.9%) | 8,263 (7.0%) |
| Median `dieSize` | 533 | 845 |

**Three facts follow.** (1) **The built-in split is lot-disjoint.** No lot contributes a wafer to both partitions, so a result under it *is* an unseen-lot result. (2) **It is test-heavy** — 69% of labelled wafers are in Test. (3) **It carries a large distribution shift besides lot separation**: the defect share falls from 32.4% to 6.7%, and the wafer-size distribution differs sharply between partitions.

**Per-class support under the built-in split** (wafers, and the number of lots they come from):

| Class | Train wafers | Train lots | Test wafers | Test lots | Share in Test |
|---|---|---|---|---|---|
| Center | 3,462 | 1,130 | 832 | 518 | 19.4% |
| Donut | 409 | 123 | 146 | 110 | 26.3% |
| Edge-Loc | 2,417 | 1,536 | 2,772 | 1,675 | 53.4% |
| Edge-Ring | 8,554 | 756 | 1,126 | 319 | 11.6% |
| Loc | 1,620 | 1,022 | 1,973 | 1,450 | 54.9% |
| **Near-full** | **54** | **54** | **95** | **83** | 63.8% |
| Random | 609 | 267 | 257 | 182 | 29.7% |
| Scratch | 500 | 428 | 693 | 631 | 58.1% |
| none | 36,730 | 1,654 | 110,701 | 4,937 | 75.1% |

Every class has support in both partitions. Near-full is the thinnest: 54 training wafers, one per lot.

**A correction to the pack's lot count.** Revisions B, C and the first issue of D all stated **46,393** lots. The source pickle has **46,293** distinct `lotName` values. The earlier figure is wrong by exactly 100 and looks like a transcription slip. Expect 46,293; if you get 46,393 you have a different copy and should say so.

## Card E1 — Team 7 · Strategy S1 · Catalogue P30

**Execution contract.** Annex D0 fixes this card's reference setting, required training runs and budget; Annex D5 fixes the protocol details. Both are part of this card.

**Datasets and roles.** Labelled WM-811K subset (172,950 maps; 25,519 with a defect pattern) — mandatory, sole dataset.

**Task and labels.** Single-label classification over **eight defect classes plus `none`**. There is no mixed-type class in this dataset; mixed-defect classification is out of scope.

**Split and validation.** The **built-in `trainTestLabel` protocol**. Validation is the fixed hash-ordered 20% of **training lots** in Annex D5, never using test labels. Lot grouping is supportable for every class — Near-full's 54 training wafers come from 54 different lots.

**🔴 The scope of your claim — corrected at Revision D.** Revisions C and the first issue of D told you this protocol "does not license a claim of unseen-lot generalisation." **That was wrong, and the measurement above shows it.** The built-in partitions share no lot. **Your test result is an unseen-lot result**, and you may say so. What you may not say is that it isolates lot separation: the test partition also differs in defect prevalence (6.7% against 32.4%) and in wafer size. Report the lot-disjointness and the shift together.

**Baseline.** Radon-transform and geometric/region features with a random forest, under this protocol.

**Required models.** 1-D radial and angular defect-density profile CNN; 2-D CNN on the resized map; spatial attention with ablation. **Fusion pair: radial-profile model with 2-D CNN.**

**Core experiment 1.** Per-class recall against class frequency, with the contrast against headline accuracy stated explicitly. **Plot against training-partition frequency and report test support beside it** — the two differ by up to a factor of six (Edge-Ring is 15.7% of training and 0.95% of test).

**Core experiment 2.** Rare-class targeted augmentation — **rotation and reflection only**, both physically valid on wafer maps — against an unchanged control.

**Primary metrics.** Macro-F1 (primary), per-class recall, balanced accuracy. Overall accuracy is reported only to expose how misleading it is at 93.3 per cent `none` in the test partition.

**Scope caps.** One augmentation policy, one backbone, one resize strategy: nearest-neighbour to 64×64 (Annex D5).

**🔴 Time your first fit before you plan the rest.** The instructor's throughput check of 24 September 2026 put a 64×64 2-D CNN of about 137,000 parameters over this card's 43,308 training wafers at roughly 170 seconds per epoch on **two** cores — about ten epochs inside the 30-minute cap. Six cores may do better, but scaling across cores is not guaranteed and was not measured, so **time your card's reference configuration (Annex D0's Week-1 table) and report it in your readiness note** (§8 item 7). If the cap stops you before the model has learned, say so; the configuration will be corrected and nothing is lost from your marks. **This card's sibling E2 is tighter still** — its matched split trains on 103,853 wafers — so Track E should compare timings between groups in Week 1.

**Read carefully.** Any decision threshold or class prior you fit on training-side validation is fitted to a 32% defect prevalence and scored against a 7% one. That is not your error to fix, but it is yours to state.

## Card E2 — Team 8 · Strategy S4 · Catalogue P30

**Execution contract.** Annex D0 fixes this card's reference setting, required training runs and budget; Annex D5 fixes the protocol details. Both are part of this card.

**🔴 This card is rewritten at Revision D, because the measurement removed the contrast it was built on.** Revision C's experiment 2 compared each model's built-in-split result with its lot-disjoint result and called the gap "lot separation." **The built-in split is already lot-disjoint.** Both arms of that contrast hold lots out, so the gap between them could not have measured lot separation at all. What differs between the two protocols is the distribution shift the built-in split carries — defect prevalence falling from 32.4% to 6.7%, 295 wafer shapes present in training and absent from test, median die size 533 against 845. **That shift is now the question.** The strategy (S4, robustness to a named shift), the models and the fusion pair are unchanged.

**Datasets and roles.** Labelled WM-811K — mandatory.

**Task and labels.** As E1.

**Split and validation.** Two lot-disjoint protocols, both published as `lotName` ID lists:

- **Built-in** — the shipped `trainTestLabel`. Lot-disjoint, and shifted in prevalence and wafer size.
- **Matched** — a lot-disjoint split, **stratified so that training, validation and test carry approximately the same class mix and wafer-size distribution** (grouped stratification approximates the match; it does not guarantee identical distributions, so report the achieved ones), built by the fixed algorithm in Annex D5 (60/20/20 by lot) and **issued with this card as frozen lot lists**. Every class spans at least 137 lots, so grouped stratification is feasible. In the issued split every class has support in all three partitions (Near-full 91 / 29 / 29 wafers), and 0.22% of test wafers have a map shape absent from training, against 7.58% under the built-in protocol with E1's validation carve.

Validation is a disjoint set of training lots under each protocol: the matched split's own 20%, and for the built-in protocol the same hash-ordered 20% of training lots that E1 uses.

**Baseline.** Radon and geometric features with a random forest, **reproduced under both protocols** — your own numbers, not E1's.

**Required models.** 1-D radial-profile CNN; 2-D CNN; spatial attention with ablation. **Fusion pair: radial-profile with 2-D CNN.**

**Core experiment 1.** Radial-profile model versus 2-D CNN on the **matched** lot-disjoint split.

**Core experiment 2.** Compare each model's result under the two lot-disjoint protocols — **built-in** and **matched** — descriptively. The difference combines training-population and training-size differences, the held-out class and wafer-size mix, and potentially optimisation exposure under the time limit. Report achieved distributions and optimisation updates under both protocols. It does not isolate a causal cost of distribution shift or of lot separation. Break it down by wafer shape (seen versus unseen in training) and by class. *(Corrected 24 September 2026: this said the gap "estimates the cost of the prevalence and wafer-size shift" with lot separation held fixed. Both protocols are lot-disjoint, but they also differ in training population, training size, held-out population and, under a time cap, optimisation exposure; Annex D5 already said so.)*

**Primary metrics.** Macro-F1 and per-class recall under both protocols; the protocol gap as the headline; support tables for both, including per-shape support.

**Scope caps.** Two protocols for the two no-attention neural models and the classical baseline. Attention and the named fusion are demonstrated on the matched reference only, and are not repeated under the built-in split. No further splits.

**Read carefully.** Two shifts travel together in the built-in split — label prevalence and wafer size. Your matched split reduces both at once, and it also changes who is in training and in test. **Do not attribute the gap to either shift, or to the pair of them, as a causal cost**; a control that separates them is optional and credited. And the one thing this card no longer lets you claim is a lot-separation effect: both arms hold lots out.

## Card E3 — Team 18 · Strategy S2 · Catalogue P30

**Execution contract.** Annex D0 fixes this card's reference setting, required training runs and budget; Annex D5 fixes the protocol details. Both are part of this card.

**Datasets and roles.** Labelled WM-811K — mandatory. The **unlabelled pool** — mandatory, restricted as below.

**Task and labels.** As E1.

**Split and validation.** Built-in `trainTestLabel` protocol; validation is the fixed hash-ordered 20% of training lots in Annex D5. **Pool eligibility: exclude every wafer belonging to a validation or test partition, and every wafer from any lot represented in validation or test.** The pseudo-label confidence threshold is fixed at **0.95**. Stopping uses validation only.

**🔴 The eligible pool, counted on the source pickle on 21 September 2026.**

| Step | Unlabelled wafers | Lots |
|---|---|---|
| All unlabelled wafers | 638,507 | 41,608 |
| Of which sit in a lot that also has a **Test** wafer — **excluded** | 5,230 | 1,125 |
| **After excluding every Test lot** — the upper bound | **633,277** | 40,483 |
| After also excluding a validation carve of 10 / 15 / 20% of training lots (Revision D, approximate carves) | 626,656 / 623,535 / 619,987 | 39,980 / 39,742 / 39,500 |
| **After the fixed Annex D5 carve** (first 20% of training lots in hash order; instructor run, 23 Sep 2026) | **620,038** | 39,496 |
| Floor — if validation took every training lot | 566,611 | |

**What that means for your caps.** The exclusion rule matters — 6,077 lots mix labelled and unlabelled wafers, and 5,230 unlabelled wafers share a lot with a test wafer — but it removes less than 1% of the pool. **No cap a laptop can train on will be constrained by the pool; both are constrained by CPU time.** The caps are therefore fixed on this card: **2,000 and 10,000 eligible wafers, nested** (Annex D5). Report the eligible count your validation carve produces; it should be 620,038. *(Changed at D1: Revision D left the two caps to you. Sizing CPU work is the instructor's job, so the caps are now stated.)*

**Baseline.** Radon and geometric features with a random forest under this protocol.

**Required models.** 1-D radial-profile CNN; 2-D CNN; spatial attention with ablation. **Fusion pair: radial-profile with 2-D CNN.**

**Core experiment 1.** Supervised-only versus **one round** of pseudo-labelling from a single capped, eligible, training-only pool.

**Core experiment 2.** Gain versus CPU cost at **one additional pool cap**.

**Primary metrics.** Macro-F1 and per-class recall; gain per unit CPU time; the count of pseudo-labels accepted at each cap.

**Scope caps.** One pseudo-labelling round with the **2-D CNN**. Nested eligible-pool caps of **2,000 and 10,000 wafers**. No iteration to convergence. Details in Annex D5.

**Read carefully.** Pseudo-label contamination is the failure mode this project exists to avoid, and the pool is not drawn from the test distribution: pseudo-labels inherit whatever prevalence the pool has, and the test partition is 93.3% `none`. Report the class mix of the accepted pseudo-labels at each cap.

---

# THE SIX INDIVIDUAL PROJECTS

No shared phase. You build the pipeline, EDA and baseline alone in Weeks 1–2 while the shared tracks split that work three ways.

## Card I1 — Team 5 · Strategy S2 · Catalogue P8

**Execution contract.** Annex D0 fixes this card's reference setting, required training runs and budget; Annex D6 fixes the protocol details. Both are part of this card.

**Datasets and roles.** **OPSSAT-AD** — mandatory primary. **SMAP/MSL** — mandatory, **bounded audit only**, on the fixed streams SMAP **P-1** and MSL **C-1**, which are issued with the cards (Annex D6).

**Task and labels.** Anomaly detection. OPSSAT-AD is **univariate**: 2,123 single-channel fragments across 9 channels, ~20 per cent anomalous, scored at **fragment** level. SMAP/MSL supplies anomaly intervals within continuous streams, scored at **point or event** level.

**Label-access regime — decided here, not by you.** Run the core comparison **within one regime: nominal-only training.** The deep detector, the classical controls and the trivial detector all see nominal data only. A supervised image-side formulation may be run **as a separately labelled cross-regime demonstration**; if you run it, it does not support any conclusion about architecture.

**Split and validation.** OPSSAT-AD's provided train/test split. Calibration and thresholds are fitted on a declared nominal development partition of the training side (Annex D6) — **never on test**. SMAP/MSL: the benchmark's own train/test files for P-1 and C-1.

**Baseline.** Isolation Forest, PCA reconstruction error, and — critically — a **trivial constant/threshold detector**.

**Required models.** **One** small 1-D convolutional autoencoder on the fragment, as fixed in D6; one image-side formulation on the fragment spectrogram, under the same nominal-only regime; temporal attention within a fragment, with ablation. **Fusion pair: the reconstruction score with the image-side score**, with **a declared common score orientation and normalisation fitted on development data only**, and fusion weights fixed on validation only.

**Core experiment 1.** One small deep detector versus trivial and classical controls on **OPSSAT-AD**, under the declared nominal-only regime.

**Core experiment 2.** Audit **SMAP P-1 and MSL C-1 only**, retaining each complete published test stream. Fit the same no-attention 1-D autoencoder architecture independently per stream and compare with the classical and trivial controls. Annex D6 fixes window scoring, nominal calibration and the point-adjusted audit.

**Primary metrics.** Precision, recall and F1 **per benchmark under that benchmark's native protocol, never averaged across the two**. **On SMAP/MSL only, point-adjusted F1 is required as a clearly labelled audit figure beside the unadjusted point score; OPSSAT-AD has no such adjustment.** Time-based rates such as false alarms per day require validated continuous time coverage and are **not** reportable on OPSSAT-AD fragments.

**Scope caps.** One global sequential detector and one image autoencoder on OPSSAT-AD; two stream-specific sequential detectors for the SMAP/MSL audit. Only OPSSAT-AD receives the attention and fusion demonstrations. No thirty-baseline reproduction; Annex D6 fixes data handling and costs.

**Specify in your readiness note.** The 256-sample resampling and native stream-window rules in D6, with original-length distributions and their effect on score calibration.

**Two inherited limitations to record, not fix.** SMAP/MSL telemetry ships pre-scaled to (−1,1) using **test-set** min/max, so training-only preprocessing cannot be claimed on it; timing is anonymised. Neither is your bug.

**Read carefully.** Conclusions concern the tested algorithms, the declared label access and the native protocol. Any supervised-versus-nominal-only comparison is explicitly labelled and does not isolate architecture. The published criticism of SMAP/MSL is a **hypothesis you are testing**, not a verdict to reach; either outcome earns full marks.

## Card I2 — Team 1 · Strategy S4 · Catalogue P12

**Execution contract.** Annex D0 fixes this card's reference setting, required training runs and budget; Annex D6 fixes the protocol details. Both are part of this card.

**Project title: ECG diagnostic superclass classification and patient-overlap audit.**

**Datasets and roles.** **PTB-XL v1.0.3, `records100`** — mandatory, sole core dataset. **MIT-BIH — optional**, and not required by either core experiment.

**Task and labels.** **Five-superclass multi-label** classification (NORM, MI, STTC, CD, HYP): a multi-hot target, a BCE-style objective, decision thresholds selected on validation only. Samples are **ten-second, 12-lead records**, not beats. Construct labels from the diagnostic statements using the pinned `scp_statements.csv` mapping with an **explicit likelihood/filter policy stated in your readiness note** — the 71 SCP statements include form and rhythm statements that do not map into the five diagnostic superclasses.

**Split and validation.** The official `strat_fold` protocol: folds 1–8 train, 9 validation, 10 test. **Patient IDs govern the split.** The fold-10 result is your fixed headline.

**Baseline.** A modest, reproducible **multilead feature baseline including waveform morphology or simple lead-wise statistics**, mapped to the same multilabel target with validation-only thresholds, with feature extraction and missing-feature handling documented. **Not an RR/HRV-dominated feature set** — three of the five superclasses are morphological and a ten-second record carries few beats, so an RR-heavy baseline is weak for the wrong reason. Clinical-grade delineation is **not** required.

**Required models.** 1-D CNN over 12 leads; 2-D CNN on per-lead scalograms or spectrograms stacked as channels; lead-wise channel attention with ablation. **Fusion pair: the 1-D model with the chosen time–frequency image model.**

**Core experiment 1.** The official folds versus a record-random patient-overlap audit, using the **no-attention 1-D CNN only**. Use the same eligible record pool and the D6 partition algorithm; publish patient intersections. Official folds remain the headline.

**Core experiment 2.** **Class-wise analysis of that gap**, with **five repeated audit partitions** so the contrast carries a measure of partition variability — not a causal leakage estimate or confidence interval (Annex D6). The official-fold result stays fixed; only the audit partitions repeat.

**Primary metrics.** Macro-F1, per-class sensitivity and specificity, macro-AUC. Report the flawed and correct protocols side by side — that contrast **is** the result.

**Scope caps.** One 1-D architecture (no LSTM variant required), one 2-D backbone, five audit repetitions. MIT-BIH transfer is optional and is a second project's worth of work.

**Read carefully.** The audit changes the **test set** as well as the split, so the gap is a **descriptive contrast between two protocols**, not a clean point estimate of the leakage effect. Say so.

**Audit-control exemption applies** to the deliberately overlapping partitions. Labelled as audit controls, with the valid-protocol result as the headline, they are deliberately leaky audit controls, exempt from the leakage penalty, and attract no cap.

## Card I3 — Team 4 · Strategy S1 · Catalogue P27

**Execution contract.** Annex D0 fixes this card's reference setting, required training runs and budget; Annex D7 fixes the protocol details. Both are part of this card.

**Datasets and roles.** **Severson et al. fast-charging dataset** (124 LFP cells, 72 charging policies) — mandatory, sole core dataset. **Attia et al. 2020 follow-up — optional and unverified.**

**The file-level route, demonstrated 20 September 2026 — this replaces Revision C's unresolved prerequisite.**

```
GET https://data.matr.io/1/api/v1/edp/projects/5c48dd2bc625d700019f3204/batches
GET https://data.matr.io/1/api/v1/file/<fileId>            # metadata, including exact size
GET https://data.matr.io/1/api/v1/file/<fileId>/download   # the bytes; HTTP Range supported
```

| Batch | `structFileId` | Filename | Bytes |
|---|---|---|---|
| 2017-05-12 | `5c86c0b5fa2ede00015ddf66` | `2017-05-12_batchdata_updated_struct_errorcorrect.mat` | 3,025,320,241 |
| 2017-06-30 | `5c86bf13fa2ede00015ddd82` | `2017-06-30_batchdata_updated_struct_errorcorrect.mat` | 2,007,331,155 |
| 2018-04-12 | `5c86bd64fa2ede00015ddbb2` | `2018-04-12_batchdata_updated_struct_errorcorrect.mat` | 3,236,690,412 |

**All three structs: 8,269,341,808 bytes = 7.70 GiB transferred. Do not retain them.** Kept whole, they are 7.70 GiB of working data against Annex D0's 5 GB cap. *(Corrected 24 September 2026. This line said "transferred and retained", which put the card in direct conflict with D0.)* **Acquire one struct at a time and compact it before fetching the next:**

1. Download one struct (Range requests return `206` with the size in `content-range`, so the download is resumable — use that rather than restarting).
2. Parse it lazily with h5py and keep, for every test record, the `Qdlin` and `Tdlin` curves (1,000 points on the authors' voltage grid) for **the available cycles through 100, with their original cycle IDs**, and the complete per-cycle `summary` series (all eight fields), as float32. That is everything the features, the three horizons and the target check need. **Required completeness is cycles 2–100.** Cycle 1 is absent in the 2017-05-12 batch (Annex D7): it is not an exclusion criterion, and you must not renumber cycles or fabricate it. *(Corrected 25 September 2026: this said "cycles 1–100", which a loader could read as a completeness requirement that the 2017-05-12 cells cannot meet.)*
3. Delete the struct. For the five continuing cells, merge the 2017-06-30 summary onto the 2017-05-12 record at the offset Annex D7 gives.

**Measured on the 2017-06-30 struct, 24 September 2026:** 48 records compacted to **39,323,488 bytes** in 12.8 s with peak memory 52 MB (h5py 3.16.0, 2 cores). The curves are a fixed 800,000 bytes per record, so all 140 records compact to **about 116 MB**. **Peak disk use is one struct plus the compact store — at most 3,236,690,412 + ~116,000,000 bytes, about 3.35 GB** — and the retained working set after the third struct is about 116 MB. Report transferred bytes, peak temporary bytes and final retained bytes separately. This keeps all 128 pool cells, the issued split and identical horizons; nothing is dropped.

**The per-cell CSV route exists and is the more expensive one.** 140 cell records each carry a `dataFileId`: 2017-05-12 46 cells / 8,233,368,355 B; 2017-06-30 48 cells / 4,933,944,543 B; 2018-04-12 46 cells / 6,218,776,178 B — **18.05 GiB in total**, with a median per-cell CSV of 103–167 MB. **Do not substitute one batch for the sequential route.** Taking only the 2017-06-30 struct would change the issued 128-cell, 75 / 24 / 29 protocol: the five continuing cells have their first cycles in the other file, so they would lack cycles 1–100 and drop out, and two whole batches of held-out cells would go with them. If the sequential route above fails on your machine, report it in the readiness note and the instructor decides; do not cut the pool yourself. *(Corrected 24 September 2026: this paragraph previously offered the single batch as a fallback.)*

**Task and labels.** **Regression of cycle life** from early-cycle data. This is the core task. Life-band classification is **optional** and is not required by either experiment.

**Target.** **Use the issued `cycle_life_target`** in `I3_cycle_life_targets.csv` (Annex D7) for scoring — one value per physical cell, built by the documented end-of-life rule and global-cycle join, including the five continuing cells. Batch-local run lengths and censored endpoints are not substitute targets. Reproduce the target check from the platform's discharge-capacity summaries; never infer a target from early-cycle inputs.

**Split and validation.** **By physical cell, never by cycle.** Annex D7 fixes one 60/20/20 cell split, computed once from the platform's cell listing, with **identical held-out cell IDs at every horizon**. It is **issued as a frozen list**: 128 cells in the pool, 75 train, 24 validation and 29 test (Annex D7). Publish the IDs and the exclusion list in the readiness note. Validation cells are disjoint from test cells and fixed across horizons.

**🔴 Deduplicate by physical cell before you split.** The platform lists **140 cell tests but only 135 distinct cell IDs**. Five cells appear in both the 2017-05-12 and the 2017-06-30 batch — `el150800460486`, `el150800460514`, `el150800464977`, `el150800460623`, `el150800464865` — because the second batch resumed them; its own batch note says channels 1, 2, 3, 5 and 6 "carry over from batch 1 … these are NOT new experiments." **`(batch, cell)` is not the split unit. The physical cell is.** Treating the pairs as independent puts the same cell on both sides of your split.

**Fix your held-out cells before you download anything.** Each cell record carries a `summary` field holding the full discharge-capacity-versus-cycle series, so the cell list, the exclusion list and the **mean-life floor** are all computable from the API alone. Across all 140 records the series length runs 172 / 533 / 789 / 1,010 / 2,239 at min / p25 / median / p75 / max. Put the resulting cell IDs in your readiness note.

**Baseline.** The published **elastic-net on ΔQ(V) features**, plus the **mean-life predictor as a floor**, with the mean computed on **training cells only**.

**Required models.** 1-D CNN with branches for the ΔQ(V) curve and cycle-summary sequence; small 2-D CNN on the cycle×voltage surface; temporal attention on the 1-D sequence branch with no-attention ablation. **Fusion pair: elastic-net prediction with the no-attention 1-D CNN prediction**, at the 100-cycle reference only.

**Core experiment 1.** Window sweep at **three fixed horizons — 100, 30 and 10 cycles** — for the elastic-net baseline, the mean-life floor and **one** bounded deep model.

**Core experiment 2.** The DL-versus-elastic-net **crossover read off that same sweep**. No new fits.

**Primary metrics.** RMSE and MAPE in cycle life, plotted against window size, with the mean-life floor reported at each horizon.

**Uncertainty procedure (required, bounded).** Resample the **held-out cells** from predictions you already have, at each horizon. No repeated training. With 29 test cells from a pool of 128, the held-out set is small and a single RMSE is not interpretable.

**Scope caps.** Three horizons for the elastic net, the mean-life floor and the no-attention 1-D CNN. The 2-D model, attention and fusion run at 100 cycles only. Annex D7 fixes the horizon endpoints, the split and the bootstrap. Intermediate windows (50, 20) are optional. Report transferred and retained bytes.

**🔴 Horizon-safe features — the leakage trap.** At horizon *k*, **every feature must derive from cycles ≤ k**. The published ΔQ(V) feature is defined between cycles 100 and 10 and is **not computable at a 10-cycle horizon**; adapt the endpoints per horizon and state them. The same applies to any normalisation or target statistic computed in preprocessing. No future-cycle reuse anywhere.

**Licence.** CC BY 4.0, stated on the project page. Cite the Severson et al. paper, not the URL.

## Card I4 — Team 16 · Catalogue P35 · **NOT ISSUABLE**

**Status: withheld.** This card is not issued and Project 35 is not assignable in this release.

**Why, and what was checked (16 September 2026).** The CAXTON dataset is distributed as a **single hierarchical archive** — `print0/` through `print191/`, each directory holding `image-0.jpg …` at 1280×720 — with **no documented per-print, per-row or per-subset download route**. The Cambridge repository record exposes only the five CSV files (≈640 MB combined). The authors' code repository ships **8 sample images**. The one public mirror, `cemag/tl-caxton`, holds **4,040 images at 350×350 with flow rate only** — no printer identity, no geometry identity, no four-parameter labels — and therefore cannot support a printer or geometry holdout. At 1.27 million JPGs of that resolution the full archive is on the order of 100 GB.

The manifest's instruction to cap the working set at 30,000–50,000 images therefore presumes a selective route that has not been shown to exist. A row cap is not a byte cap, and in this case the byte cap is the project.

**What would reopen it.** A confirmed bounded image route — per-print access from the repository, an author-supplied subset, or a mirror carrying printer and geometry metadata — with measured transferred bytes for the approved subset. Until then the project stays in the catalogue as a reserve.

**Team 16 is reassigned** to the substitute below, at the instructor's decision.

## Card I4-S — Team 16 (substitute) · Strategy S4 · Catalogue P54

**Execution contract.** Annex D0 fixes this card's reference setting, required training runs and budget; Annex D8 fixes the protocol details. Both are part of this card.

**Datasets and roles.** **Landslide4Sense (IARAI, 2022)** — mandatory, sole dataset. 3,799 labelled patches of 128 × 128 × 14 bands: Sentinel-2 B1–B12 plus **slope (B13)** and **DEM (B14)** from ALOS PALSAR, resampled to 10 m, HDF5.

**🔴 Acquisition — the original `iarai.ac.at` download endpoints are offline; the course uses its demonstrated, pinned mirror.** *(Narrowed 25 September 2026 from "the official distribution is offline": the authors' Zenodo record still lists the archives, as the manifest records; it is not adopted.)* `iarai.ac.at` no longer resolves, checked 20 September 2026 by two independent paths; IARAI was wound down in 2023. **Both download links in the benchmark repository's README are dead**, as is its pretrained-model link. The GitHub repository itself — code, file lists, README — is still up and is still the reference for the data description.

**The route that works:** `huggingface.co/datasets/ibm-nasa-geospatial/Landslide4sense`, public and ungated, last modified 22 October 2024.

- `image_N.h5` is **1,837,056 bytes** each — 128 × 128 × 14 in float64 plus a 2,048-byte header. `mask_N.h5` is **18,432 bytes**.
- The whole mirror is 4,844 images and 4,844 masks: **8,987,983,872 bytes = 8.37 GiB, transferred and retained, uncompressed.**
- **The subset this card uses is smaller, and it was measured on 24 September 2026:** the 3,799 labelled images plus their masks are **7,048,998,912 bytes = 6.56 GiB transferred**, and **3,547,840,512 bytes = 3.30 GiB retained** once the images are cast to float32 and the masks kept as `uint8`. **That retained figure is 71% of Annex D0's 5 GB working-data cap before any intermediate file**, so convert on ingest and **do not keep a float64 copy alongside** — that alone would put you over. Say in your readiness note what you retained. The instructor's full pass took 48.9 minutes with sixteen concurrent fetches. **The mirror answers no multi-range request**, so a partial read of each file is not available: budget for the whole 6.56 GiB.
- **Cast to float32 on ingest**, which halves the retained figure. The values are already globally rescaled into roughly [0, 7] — they are **not** raw reflectance and band 14 is **not** elevation in metres — so an integer downcast needs a stated scale factor and is not free. Report transferred and retained bytes separately.
- The official loader reads `hf['img'][:]`, shape (128, 128, 14) band-last, then transposes to (14, 128, 128) and standardises per band. Match that convention or state yours.

**Two defects in the mirror, both named so you do not trip over them.** (1) It carries masks for the **validation and test** splits — 1,045 patches whose labels the competition withheld — and its README does not say where they came from. **Checked at source on 24 September 2026, and nothing says:** the extras are exactly `annotations/validation` (245) plus `annotations/test` (800); the README describes only the folder structure; and the repository's six commits, all 22 October 2024, carry generic `huggingface_hub` upload titles. **They are an optional extension whose provenance cannot be established and must not appear in any headline result — that bar is settled, not provisional.** Everything marked uses the 3,799 competition-labelled training patches only. (2) `annotations/train/` holds 3,804 files: the 3,799 masks plus five 800-byte strays named `image_1.h5`, `image_10.h5`, `image_100.h5`, `image_1000.h5`, `image_1001.h5`. A naive glob picks them up as masks. Glob `mask_*.h5` explicitly.

**Task and labels.** **Patch-level binary classification.** A patch is **positive if its mask contains at least one pixel of value 1**, and negative otherwise. A missing or unreadable mask is excluded and counted, never called negative. Pixel-wise segmentation is an optional extension and is not required.

**🔴 Split and validation — this replaces Revision C's "by case-study area", which the release does not support.** The distributed set is a flat sequence, `image_1.h5 … image_3799.h5`, with **no region column, no metadata file and no folder-per-area**. The organisers withheld it deliberately; their README FAQ says the geographic information and acquisition time "will not be released at the current phase in case participants may directly look for the corresponding high-resolution images to check." There is therefore no region identifier to split on and none to publish.

**🔴 The grouping has been recovered, and the split is issued. This replaces D1's "the full pass is yours to produce".** The instructor ran the full pass over all 3,799 patches on **24 September 2026**, because the result decides whether this card runs as written or under S1, and that is not a question to answer in Week 1. **There are four scene groups.**

| Scene | Patches | Positive | Negative | Landslide pixels | Raster grid |
|---|---|---|---|---|---|
| **S1** | 3,033 | 1,934 | 1,099 | 1,269,296 | 41 × 74 |
| **S2** | 150 | 126 | 24 | 108,533 | 15 × 10 |
| **S3** | 121 | 69 | 52 | 16,108 | 11 × 11 |
| **S4** | 494 | 102 | 392 | 48,853 | 26 × 19 |

*(Reissued 24 September 2026: patch 2460 had been put in S2 and S1's grid coordinates were shifted for 573 patches, which left 15 test-block patches adjacent to training patches. See Annex D8. The figures in this table are the corrected ones.)* Each group is a contiguous run of patch IDs and has one dominant vertical raster stride — 41, 15, 11, 26 — and those four strides are an independent confirmation of the count: four scenes, four tilings. Horizontal best match is the next index for 3,566 of 3,799 patches, and S4's 468 vertical links are all exact. **Prevalence 58.73%; landslide pixels 2.3180% of all pixels**, confirming the manifest figures at full scale.

**You reproduce this in Week 1; you do not discover it.** Annex D8 gives the procedure, the threshold and the rules the instructor had to add, and the reference script `i4s_grouping_and_split.py` is issued with the card. Run it or your own implementation, publish your group assignment, and **report any patch you place differently**. Recovering the grouping still counts under Component 1, and a documented disagreement with the issued file is a finding, not an error. **Two kinds of disagreement are different:** a patch or two placed differently by a harmless implementation choice is reported and carries no penalty, and the issued file still governs; but corrupted or missing files, a patch you find at two conflicting coordinates, or any overlap between partitions of the issued split must go to the instructor straight away, because they would change the split.

*(Corrected at D1: Revision D's instruction matched right-to-left edges only. The probe that validated the method found no vertical match within indices 1–24 and stopped there. If rows of one scene were never joined, two vertically adjacent rows would become two "groups", and leave-one-group-out would put neighbouring tiles on both sides of the split — the leakage this grouping exists to prevent. **The full pass confirms the correction was necessary and shows why the probe missed it: the probe's vertical search covered patches 1–24, all in S1, whose row stride is 41.**)* *(That explanation corrected 24 September 2026: it previously said all four strides were beyond the 24-index window; 15 and 11 are not.)*

**Publish, in the readiness note:** the edge-match threshold you used, your histogram of best-match distances, the recovered scene groups, the group count, the patch count per group, the number of horizontal and vertical links, and **your count of degenerate patches**. State any disagreement with the issued files.

**The split is issued as a frozen file, `Landslide4Sense_I4S_split.csv`** (SHA-256 `21aad749…e44c`), with the four folds in `Landslide4Sense_I4S_folds.csv` (`835eb37b…c74b`), and the script that produces both, `i4s_grouping_and_split.py`. *(Reissued 24 September 2026; the files of the same names hashed `ed9e42d0…b0da` and `beb696d7…4e23` are withdrawn.)* Annex D8 defines two protocols on the **same held-out test patches**. The **within-group reference** trains on spatially separated blocks of the target group itself, with a one-column guard band between blocks. The **transfer** protocol trains on other groups only, and validates on a further disjoint group. **Every claim names the unit as a scene group recovered from tile adjacency — an explicit proxy for a case-study area, never a region or a country.**

**🔴 The target group is S1, and that is a change of protocol, not a choice of convenience.** D1 assumed any eligible group could be a target. It cannot. A target must carry a guarded three-block split of its own, because the within-group reference and the transfer model are scored on the same test patches. **The requirement is explicit: at least 20 positive and 20 negative patches in the target's guarded test block** (Annex D8). Under the pinned block rule S4's test block holds 114 patches with only 3 positives — its landslides sit mostly in rows 4–11 (80 of 102) and thin out to the east — while S2's test block is 40 patches (29 / 11) and S3's 33 (17 / 16). S1 is the only group that qualifies, and the matched comparison runs there: *(Corrected 24 September 2026: this said rows 4–11 held 89 of S4's positives and that S2 and S3 were too small for three blocks at all.)*

| Fold | Test set | Transfer trains on | Transfer validates on |
|---|---|---|---|
| **F1 — the matched fold** | S1's guarded test block, **570 patches (210 pos / 360 neg)** | S2 + S4 (644) | S3 (121) |
| F2 | all of S2, 150 (126 / 24) | S1 + S4 | S3 |
| F3 | all of S3, 121 (69 / 52) | S1 + S2 | S4 |
| F4 | all of S4, 494 (102 / 392) | S1 + S3 | S2 |

**Only F1 carries a within-group reference.** F2, F3 and F4 are transfer-only whole-scene folds and exist so that core experiment 2 is answered on four terrains rather than one. Within S1 the grid columns are cut at 23 and 31 with one-column guards: **train 1,702 (1,277 pos / 425 neg), validation 507 (346 / 161), test 570 (210 / 360)**, with 141 guard patches discarded.

*(Corrected at D1: Revision D's core experiment compared a "within-group baseline" with leave-one-scene-group-out without saying how the within-group reference was split. A within-group reference that shares neighbouring tiles between its own train and test measures leakage, not transfer. Annex D8 now fixes it.)*

**Screen for degenerate patches — there are 114, and they are already excluded.** A degenerate patch has band 14 constant and slope identically zero. The instructor's pass found **114** (115 have a constant band 14; one of those has non-zero slope and is kept). **All 114 are negative**, 113 of them in S1, and all are marked `excluded_degenerate` in the issued split. Patch 2500, named at D1, is one of them. Reproduce the count and report any disagreement. *(Corrected 24 September 2026: D1 said "at least one patch". The true figure is 114, which is 3.0% of the set and all of it on one side of the label.)*

**Baseline.** A random forest on single-date per-patch band summaries and slope/DEM summaries, plus a training-derived majority floor. **Check the band scaling before computing NDVI or a bare-soil index.** The mirror's values are globally rescaled (see above), so an index computed from rescaled bands is valid only if every band shares one documented scale. Otherwise omit the index and say why. A slope feature needs no physical units for a random forest; a hand-set slope threshold does. **Do not attempt an NDVI-change feature: these patches are single-date and there is no second observation.**

**Required models.** Per-pixel 14-band spectral-plus-topographic signature 1-D CNN, aggregated to patch level; a small 2-D CNN on the patch (ImageNet backbones take 3 channels, not 14 — band selection, a learned 14→3 projection, or a small CNN from scratch are all defensible, and the choice is yours to justify); band attention with ablation. **Fusion pair: the spectral 1-D model with the spatial 2-D model.**

**Core experiment 1.** Within-group reference versus **transfer from other scene groups**, both scored on **F1's 570 test patches of S1**, quantifying the drop. The two training populations differ in size as well as origin — 1,702 patches within S1 against 644 in S2 + S4 — so report the contrast as descriptive, not as a pure measure of domain shift. *(Corrected 24 September 2026: D1 said "leave-one-scene-group-out", which presumed every eligible group could be a target. Only S1 can.)*

**Core experiment 2.** Twelve spectral bands versus twelve bands plus slope and DEM. Does topography improve **transfer** more than it improves within-group accuracy — is it the transferable signal while spectral response is group-specific? The within-group comparison exists only in **F1**, so that is where the two-protocol contrast is made; **F2, F3 and F4 give the band contrast under transfer onto three further scenes**, which is what turns a single-scene result into a claim about transfer. *(This experiment never depended on region identity. Corrected 24 September 2026: "under both protocols" was true of F1 only.)*

**Primary metrics.** **Landslide-class precision, recall and F1; binary balanced accuracy** (the mean of the two class recalls); per-scene-group positive and negative support and results. Pixel accuracy is banned from the headline. Pixel-level IoU applies only if you take the optional segmentation extension. *(Corrected at D1: earlier wording said "balanced accuracy on the landslide class", which is not a defined quantity.)*

**Scope caps.** **Four folds, fixed above — F1 with both protocols, F2 to F4 transfer only.** One 2-D research architecture; two band conditions in every fold and protocol. That is **ten 2-D fits** (F1: two protocols × two band conditions; F2–F4: one protocol × two band conditions). The 1-D model, the attention ablation and the fusion are demonstrated on **F1's transfer protocol with 14 bands only**, adding two more fits: **twelve neural fits in total**. The random forest and the majority floor are refit alongside each 2-D condition and are cheap. *(Corrected 24 September 2026: D1's "4F + 2" gave 18 fits at F = 4 and assumed a within-group reference in every fold.)*

**The S1 fallback is not triggered and is retained only as history.** Had the pass yielded fewer than three groups, or fewer than two eligible, the card would have been reissued as: detection performance against **landslide pixel fraction and patch difficulty**, computable from the masks alone, with the slope/DEM ablation kept as core experiment 2 inside a pooled split. Four groups were found and four are eligible, so that branch is closed. **It does not reopen if your Week-1 reproduction disagrees with the issued grouping — report the disagreement and run the issued split.**

**Why this project.** The benchmark's own authors state that they performed **no transferability evaluation**, in a dataset deliberately built from multiple regions. The gap is real. The release withholds the geography needed to close it, so the grouping had to be recovered from the pixels before any split could be declared — four scenes, from tile edges alone. You reproduce that recovery, and you name the proxy in every claim you make.

## Card I5 — Team 19 · Strategy S4 · Catalogue P43

**Execution contract.** Annex D0 fixes this card's reference setting, required training runs and budget; Annex D8a fixes the protocol details. Both are part of this card.

**Datasets and roles.** **xeno-canto** focal recordings — mandatory training source. **Powdermill annotated soundscapes, Dryad version 2 (6 April 2021), `mp3_Files.zip` (136.95 MB)** — mandatory **test set only**; never train on it, never select thresholds or augmentations on it, and never use it as a source of background audio. **freefield1010 (`ff1010bird`), `hasbird == 0` subset** — mandatory **ambient-noise source** for core experiment 2.

**🔴 Species universe — measured 20 September 2026, and the answer is all of them.** The intersection of Powdermill's 48 species with xeno-canto availability is **48 of 48**. Every species clears the ≥50 A–C threshold; the five tightest are *Meleagris gallopavo* 127, *Buteo lineatus* 148, *Vermivora cyanoptera* 174, *Parkesia motacilla* 198 and *Geothlypis formosa* 212, and the largest is *Corvus corax* at 2,783. The full list with counts is in the manifest. *(Corrected 23 September 2026. Revision D's 48-species table listed American Golden-Plover, *Pluvialis dominica* (`amgplo`), in place of **American goldfinch**, *Spinus tristis* (Powdermill code `AMGO`). The dataset README and all 62 `AMGO` annotations identify the goldfinch; no golden-plover occurs in Powdermill. The "48 of 48" availability result still holds for the correct 48 — the goldfinch has 379 A–C recordings worldwide and 234 in the United States — but the golden-plover counts and the geography warning built on them were about a species that is not in the test set, and are withdrawn.)* **Your 15 species are fixed, not chosen.** Of the 22 species with enough soundscape support (at least ten positive Powdermill windows across at least two of the four soundscape recordings), the card takes **the 15 with the most positive Powdermill windows**: Eastern towhee, wood thrush, black-throated green warbler, American crow, northern cardinal, black-capped chickadee, tufted titmouse, ovenbird, common yellowthroat, scarlet tanager, blue jay, black-and-white warbler, brown-headed cowbird, blue-headed vireo and red-bellied woodpecker. **Their source recordings are issued with this card** as `I5_source_selection.csv` — 60 per species, 900 in all, with their train / validation / test assignment (Annex D8a). Every one of the 15 has at least 163 usable A–C recordings against the 50 required, counted on 24 September 2026. You reproduce the usable counts and the selection in Week 1. If a selected species falls below 50 usable recordings when you reproduce it, Annex D8a says exactly what happens; you do not pick a replacement yourself. *(Changed 24 September 2026: the card previously let you choose 15 of the 22 and left the minimum to be checked in Week 1. Availability is not usability, and a group should not discover after issue that its species list cannot be filled.)*

**🔴 Two traps found while measuring, both of which would have cost you silently.**

**Taxonomy.** xeno-canto follows IOC; Powdermill's labels and eBird follow Clements. Hairy Woodpecker is *Dryobates villosus* to eBird and ***Leuconotopicus villosus*** to xeno-canto. A name-based scrape using the eBird name returns **zero recordings and no error**. It was the only mismatch in the 48. **Resolve every name against xeno-canto's own taxonomy, and log any species that returns zero rather than dropping it.**

**Geography.** Those counts are worldwide. Restricted to `cnt:"United States"`, the tightest are *Meleagris gallopavo* 109, *Buteo lineatus* 142, *Vermivora cyanoptera* 162, *Parkesia motacilla* 177 and *Geothlypis formosa* 180; the goldfinch has 234. No species is near the threshold if you restrict to North American recordings. *(The Revision D warning about the American Golden-Plover is withdrawn: that species is not in Powdermill. See the correction above.)*

**Task and labels — fixed, and this replaces earlier drafts' "multi-class or multi-label".** **Multi-label in both domains**: one sigmoid output per selected species, identical species order and identical window convention in both domains. Annex D8a fixes 5-second non-overlapping windows and explicitly separates **weak recording-derived focal targets** from strongly annotated Powdermill targets. Unlisted focal species are assumed negative only under that declared weak-label convention, not verified absent. The domain contrast is descriptive and includes annotation-regime differences. **"No selected species" is not "no bird"** — Powdermill's 48-species universe is not the set of all birds.

**Split and validation.** Focal: **by recording**, and ideally by recordist and location. Thresholds and fusion weights are selected on **focal validation data only**. Powdermill windows are test-only.

**Baseline.** MFCC plus spectral features with a random forest, mapped to the same multilabel target.

**Required models.** 1-D CNN over the waveform; 2-D CNN on the log-mel spectrogram; time–frequency attention with ablation. **Fusion pair: the waveform model with the spectrogram model**, at prediction level. Clip-level pooling of window predictions is an **aggregation** choice, not a fusion, though it is worth reporting.

**Core experiment 1.** Focal-held-out versus Powdermill soundscape, reported with **the same named multilabel metrics on both**.

**Core experiment 2.** On fixed held-out focal windows, mix bird-absent freefield1010 noise at **−5, 0, 5, 10 and 20 dB**, plus a clean reference, using the D8a RMS rule and identical window/noise pairs across systems and SNRs. No noisy-data retraining.

**Ambient-noise source — supplied, and these are its terms.** freefield1010 (`ff1010bird`): **7,690 field-recording excerpts, 10 seconds each, 44.1 kHz mono WAV, CC BY 4.0**, with a binary `hasbird` label in `ff1010bird_metadata_2018.csv`. Use **only clips labelled `hasbird == 0`**. The subset is **5,755 of 7,690** clips (1,935 are `hasbird == 1`), counted 23 September 2026 from the label file, which is on figshare (file 10853303, linked from the DCASE 2018 task page), not in the archive.org item. Confirm the count. Retain **at most 300 clips**; report transferred archive bytes separately from retained working bytes. **You do not need the 5.77 GB archive:** archive.org serves each clip inside it individually at `https://archive.org/download/ff1010bird/ff1010bird_wav.zip/wav%2F<itemid>.wav` (882,044 bytes each; checked 24 September 2026 — the listing holds 7,690 members and one member downloaded and parsed as a 10-second WAV). Fetch only your ≤300 `hasbird == 0` clips that way, at most about 265 MB. Spot-check a sample by ear and exclude anything with audible bird sound: `hasbird` is a detection label from a challenge, not a guarantee. Attribute CC BY 4.0 in your report.

**Primary metrics.** Macro-F1 and per-species recall in both domains; macro-F1 against SNR. Label focal scores **weak-label scores**. Do not use single-label argmax accuracy or replace these metrics with exact-match accuracy. The gap also reflects weak versus strong annotation and is not a pure acoustic-domain effect. *(Corrected at D1: earlier wording said a multi-label target "does not have" an accuracy. Exact-match accuracy is defined for multi-label targets; it is simply not the measure this project needs.)*

**Scope caps.** 15 species; at most **60 source recordings per species**, at most the first 30 seconds of each, at most six 5-second windows per recording. One waveform model, one spectrogram model, five SNRs plus clean; both models repeat evaluation only, with no retraining per SNR. No bulk download before the approved inventory is reproduced. Throttle requests.

**Access, and do it early.** The xeno-canto API v3 has **required an API key since October 2025** — free, but needs a registered account with a verified email. The key is for metadata queries; the audio itself comes from each recording's public download link, `https://xeno-canto.org/<number>/download`, which the instructor exercised on 24 September 2026 for one test recording per selected species (Annex D8a). **Those files are the recordists' original uploads, not a uniform format:** of the fifteen, thirteen were MP3 and two WAV, at 16 to 48 kHz, mono and stereo, and the server sends no length and ignores byte ranges, so every file is transferred whole even though you keep only 30 seconds. The fifteen totalled 80,966,563 bytes, 64,545,530 of them one 168-second 48 kHz stereo float WAV. Decode by content, not by file extension; trim and resample each file as it arrives and delete the original; and report transferred and retained bytes separately. **Register on the day you receive this card**, and confirm in your readiness note that the key works. Before issue the instructor confirms access, the species intersection and the soundscape window support. Within the first five working days of Week 1 — Monday 28 September to Friday 2 October — before any bulk download, you reproduce the approved inventory. Recordings carry a **mix of Creative Commons licence versions**; check and record them **before use and again before redistribution**.

**Read carefully.** **Do not infer window-level support from Powdermill's 16,052 annotation count** — annotations are vocalisations, not evaluation windows, and per-species window support is far smaller. Count it before promising per-species recall. And the focal-to-soundscape contrast changes **acoustic mixture and species prevalence as well as microphone distance**; it is not an isolated distance effect.

**Mitigation is optional.** Measure the gap and the controlled degradation. Background-mixing augmentation as a *remedy* is an optional extension, not a requirement.

## Card I6 — Team 12 · Strategy S2 · Catalogue P46

**Execution contract.** Annex D0 fixes this card's reference setting, required training runs and budget; Annex D9 fixes the protocol details. Both are part of this card.

**Datasets and roles.** **BreizhCrops**, both **L1C and L2A** processing levels — both mandatory.

**🔴 L2A exists for 2017 only.** 2018 ships L1C alone, and `kermaux` has no L2A at all. **The paired experiment is a 2017 experiment** over frh01–frh04 or belle-ile.

**🔴 Download size — measured at source, and it decides your scope.** The package's own `FILESIZES` table, which the loader asserts the extracted `.h5` against, gives **retained** bytes:

| Region | L1C | L2A | Paired total |
|---|---|---|---|
| frh01 | 2,559,635,960 | 987,259,904 | 3,546,895,864 |
| frh02 | 2,253,658,856 | 803,457,960 | 3,057,116,816 |
| frh03 | 2,493,572,704 | 890,027,448 | 3,383,600,152 |
| frh04 | 1,555,075,632 | 639,215,848 | 2,194,291,480 |
| belle-ile | 17,038,944 | 8,037,952 | 25,076,896 |

The official NUTS-3 protocol is frh01+frh02 train, frh03 validation, frh04 test — **all four regions, 12,181,904,312 bytes = 11.34 GiB if kept at once**, plus the `.tar.gz` archives on top, which the loader deletes after extraction. That exceeds the ~5 GB working-data policy, which governs what you **retain**, not what you transfer.

**How this card stays inside the policy without dropping a region: process one region and one level at a time.** Download one region's L1C and L2A files, copy out only the parcels selected by Annex D9, delete the region's files, then move to the next region. Peak retained data is then **one region's two files plus one archive**. Measured on 24 September 2026, the worst case is frh01 with the package loader: **4,204,595,712 bytes**, because its L1C archive (1,644,959,752 bytes) sits beside the extracted 2,559,635,960-byte file until the loader deletes it. Add a compact paired store of the selected parcels, about 63 MB as float32. **The transfer is 7,141,517,144 bytes of archives plus 124,220,579 bytes of index files: less than the 11.34 GiB retained, because the archives are compressed.** *(Corrected 24 September 2026: earlier issues said the transfer was at least 11.34 GiB.)* The host serves about 0.9 MB/s per connection, so plan the download. Report transferred bytes, peak retained bytes and final retained bytes separately. **🔴 Do not use `belle-ile` for development.** Every belle-ile parcel is also in frh04, your test region. Build and debug on training-region parcels. *(Corrected 24 September 2026: earlier issues recommended belle-ile for building the pipeline.)*

*(Changed at D1: Revision D made "a permitted regional subset, agreed in Week 1" the expected path and left the choice open. D1 keeps all four official regions and caps parcels instead, so no regional allocation is delegated to you.)*

**Task and labels.** Multi-class crop-type classification over the 9 classes from a per-parcel annual Sentinel-2 time series. **Exclude `code_cultu` and every other label or identifier column from the feature tensor, and assert it in code** — the L2A raw column list contains the crop code.

**Split and validation.** Use the fixed 2017 course region assignment in Annex D9: **frh01 + frh02 training, frh03 validation, frh04 test**. Preserve whole regions and the paired parcel inventory. This names the course configuration; the approved subset is not a claim to reproduce full published benchmark scores.

**Baseline.** The dataset's published Random Forest on temporal features.

**Required models.** One 1-D sequential model over the multi-band series; a 2-D CNN on the time × band matrix; temporal attention with ablation. **Fusion pair: the 1-D temporal model with the time-band image model.**

**Core experiment 1.** The three systems — 1-D temporal, time-band CNN, Random Forest — at matched budget on the fixed course regional splits in D9, **with three seeds on the reference configuration only**.

**Core experiment 2.** **L1C versus L2A**, paired, for each system.

**🔴 Three things must be matched, not one.**

**Bands.** The package's `SELECTED_BANDS` **differ by processing level**: L1C selects B1–B12 plus QA10, QA20, QA60 and doa; L2A selects B2–B8, B8A, B11, B12 plus CLD, EDG, SAT and doa. Use the **common ten-band subset: B2, B3, B4, B5, B6, B7, B8, B8A, B11, B12**, in identical band order at both levels.

**🔴 The L1C `.h5` does not store its columns in `SELECTED_BANDS` order.** Its 17 columns follow the package's raw `BANDS` order with `label` and `id` removed: B1, B10, B11, B12, B2, B3, B4, B5, B6, B7, B8, B8A, B9, QA10, QA20, QA60, doa. The common bands are therefore L1C columns 4, 5, 6, 7, 8, 9, 10, 11, 2 and 3 (B2 to B12 in the order above) and L2A columns 1 to 10; `doa` is the last L1C column and the first L2A column. Indexing L1C by `SELECTED_BANDS` names hands you B10, the cirrus band, where you expect B2. This was found by comparing the two levels on matched dates, where the raw reading agrees band by band and the `SELECTED_BANDS` reading does not (24 September 2026). The package's own default transform takes all thirteen L1C bands under shuffled names, so its published pipeline is unaffected; a ten-band comparison built on the names is not.

**Observations.** `get_default_transform` calls `np.random.choice(x.shape[0], sequencelength, replace=replace)` with `sequencelength = 45` — **it draws a fresh random subset of observation dates on every call**. Two loaders over the same parcel therefore see different dates, and a global seed does not fix it because the draw depends on call order. **Build a deterministic paired observation index per parcel, compute it once, store it, and use it identically for every level, every model, validation and test.** Record unmatched observations and your cloud/missing-data policy.

**Column names.** The culture-code column is named **`label` at L1C and `code_cultu` at L2A** — the loader branches on this. A single hard-coded column name silently mislabels one of the two levels.

**Primary metrics.** Macro-F1 and per-class recall (the class distribution is very uneven — meadows dominate), overall accuracy, parameter count, CPU training time. **Report macro-F1 twice: over all nine classes (the headline, fixed universe) and over a predeclared adequately supported subset of seven classes that excludes sunflower and nuts.** Sunflower and nuts are near-empty: in the issued selection sunflower has 7 training parcels and none in validation or test, and nuts has 28 / 1 / 1. **Sunflower:** validation and test recall are **NA** under Annex D0 (no positives). **Nuts:** its recall and F1 are defined — report them descriptively beside n = 1, with no population claim. If you report balanced accuracy under D0's supported-class definition (at least one positive), its test denominator is **eight** classes (all but sunflower); a seven-class balanced accuracy is a separate, separately named figure. *(Corrected 24 September 2026: this called the seven "supported" and told you to mark both rare classes unsupported. Nuts has one validation and one test positive, so under D0 its recall is defined, however unstable.)*

**Scope caps.** Training ≤18,000 paired parcels (≤2,000 per class across frh01/frh02), validation ≤4,500 and test ≤4,500 selected independently of labels by the deterministic D9 rule. The issued selection, `I6_parcel_selection.csv`, holds 13,317 / 4,500 / 4,500; training falls short of 18,000 because orchards, nuts and sunflower have fewer than 2,000 eligible parcels each. Three seeds **only for the no-attention 1-D CNN at L2A on that same subset**; all other model–level combinations use one seed. No alternate regional allocation is delegated to students.

**Optional, credited:** the early-season accuracy curve and additional regional holdouts beyond the fixed D9 split. **Neither is a required result.**

**Read carefully.** **Measured 24 September 2026:** 99.9% of mapped parcels appear at both levels with the same label (607,945 paired parcels across the four regions), and all but one have at least 12 matched dates with finite common bands (median 35). Reproduce this in Week 1 and report it. If deterministic observation matching cannot be achieved for enough parcels, **narrow the result to a comparison of processing pipelines** and label it as such, which is what a defaults-versus-defaults run actually measures. Do not simply re-run the authors' code and report their numbers.

---

# Appendix — what every card inherits by name

| Inherited rule | Where it lives |
|---|---|
| Leakage-free split declared before modelling; derived-sample check before the split is fixed; the independent unit matched to the claim, with the two approved within-unit protocols (Track A guarded blocks, I4-S within-scene reference) named there | Handout §4 |
| Non-DL baseline on the identical split | Handout §4; §9 |
| 1-D and 2-D representations where each is scientifically meaningful; waiver route with Week-2 approval | Handout §4; §9 (the alternatives rule) |
| One attention module with ablation; intervention reported whichever way it comes out | Handout §4 (a note on attention) |
| Two-model fusion of the pair named on this card, weights fixed on validation only | Handout §4; §9 |
| Component demonstration once on the reference setting; only card experiments repeat | Handout §4 (how much has to run) |
| Uncertainty only where this card specifies it | Handout §4 (a note on uncertainty) |
| Domain-appropriate metrics; no bare accuracy on imbalanced data | Handout §4; §9 |
| Fixed seeds, pinned `requirements.txt`, reproducible run in two named modes | Handout §4; §12 |
| Readiness note; Week-2 proposal, baseline and split IDs; Week-5 all-component demo and preliminary core-experiment run; Week-7 results freeze; Week-8 report, repository, presentation and individual defense | Handout §2 and §8; the release calendar above |
| Reference setting, required training runs, training budget, thresholds and the unsupported-class metric rules | Annex D0 |
| Lawful acquisition; licence checked before use | Handout §10; Manifests |
| Transferred bytes and retained bytes reported separately wherever they differ | Handout §4; Annex D0 |
| Ethics: no model presented as a diagnostic or operational tool | Handout §10 |
| Rubric, hard caps, audit-control exemption, negative results at full marks | Handout §9 |

---

# Protocol Annex D0 — Execution limits and release calendar

These annexes complete the cards. Their numerical limits are **course design limits**, not measured runtime claims or dataset facts, and an untested cap is not evidence of feasibility.

**🔴 Read this before you plan your Week 1.** The data limits in these annexes were checked against the artifacts before issue. **The timing limits were not, and we are telling you so rather than implying otherwise.** The reference machine below is 6 cores and 16 GB; the instructor had no 6-core machine to pilot on before issue, and a timing from a smaller one cannot certify the budget. So **your readiness note carries the measurement** (§8 item 7): one timed run of **the reference configuration named for your card in the Week-1 measurement table below** — a fit your card already requires, chosen because it is the one most likely to hit the limit, not the cheapest one. It is reused in your project; it is not an extra experiment. Comparative accuracy is not graded at this checkpoint, and **beating a trivial or classical baseline is not a condition**: what the run has to show is that it trains, validates, produces finite outputs, shows evidence of optimisation (or a documented converged state) and completes an inference pass. **Test labels and test metrics play no part in it** — time an inference pass over test-shaped data, but do not score it, and lock every choice before any scored test evaluation. A fit that hits the time limit before it learns anything is the finding we most need, and reporting it costs you nothing. **The instructor answers every readiness note by Tuesday 6 October 2026** with either "configuration confirmed" or a corrected configuration, so the Week-2 deliverable of 9 October runs on a settled configuration. A scope cut made on your measured evidence carries no penalty. Groups do not change a protocol silently. *(Changed 24 September 2026: the note previously asked for "the smallest model your card requires", which can be the cheapest model on the card and so misses the one that matters.)* *(Changed 24 September 2026. Amendment D1 said these limits would be checked by a pre-issue CPU pilot. That pilot did not happen, for the reason above, and the sentence promising it is withdrawn rather than left standing.)*

## Calendar

The dates are in the **Release calendar** near the top of this document, entered on 24 September 2026.

## Common training and selection contract

- A **fit** means one model trained under one data/architecture/condition/seed combination. Evaluation on several targets, masks, strata or SNRs is not a new fit. Fitted preprocessing is refitted from training data for each changed training partition.
- Default seed: **22**. Train small neural models with at most **30 epochs or 30 minutes of elapsed wall-clock time per fit**, whichever occurs first. The clock runs from the first training batch to the end of the last validation pass and checkpoint save, so per-epoch validation and checkpointing are inside it; data preparation before training and the final test evaluation are outside it and are reported separately. *(Corrected 24 September 2026. This said "30 minutes elapsed CPU time", which mixes two different measures: elapsed time is what a stopwatch reads, CPU time is summed over every busy core. Every per-fit limit in these annexes is an elapsed limit.)* Early stopping applies after five validation checks without improvement. Keep the best validation checkpoint within that allowance. C1–C3 and I3 may use up to 100 epochs but at most 15 minutes per fit. D2 permits at most 20 epochs/20 minutes per fit. Use the first applicable stopping limit and **report which stopped the run** — in your readiness note for the first fit, and in your report for every fit thereafter. A run stopped by the clock rather than by epochs or early stopping is a finding about the limit, and it is the single most useful number you can send back in Week 1.
- Use one fixed architecture per named model family. Small from-scratch models have at most **250,000 trainable parameters**; Track C at most 50,000. Track B uses MobileNetV2 at 128×128: train its head with the backbone frozen, then optionally unfreeze only its last block within the same allowance. Record pretrained weight identity. Pretrained inference and feature-extraction time count as compute. No GPU or exhaustive search is required.
- At most **two additional development fits per group**, using training/validation only and together ≤60 minutes, may settle a learning rate or diagnose optimisation. Freeze those choices before the core comparisons. Do not give one condition a larger search budget. Classical tuning uses at most three declared settings. **All required classical fitting — tuning and final fits, including D1's and D3's ARIMA banks — shares one allowance of 60 minutes elapsed**; its internal fits are recorded separately from the neural count below. Whether the complete ARIMA banks fit inside it has not been measured, which is why D1 and D3 project them in Week 1. *(Clarified 25 September 2026: the register had treated the banks as outside every limit while this annex placed them inside the classical allowance.)* Default RF: 200 trees; select maximum depth from {10, 20, unrestricted} on validation. No parameter-count matching is imposed on a classical method.
- Pipeline acceptance: ≤5 GB retained working data — what you keep on disk to run the project — reported separately from **peak temporary disk use** during acquisition (an archive or struct held briefly before it is compacted and deleted) and from transferred bytes; the 5 GB cap governs the retained figure, and your card states any peak it expects (I3 about 3.35 GB, I6 about 4.2 GB). Streamed batches, measured peak memory compatible with the cohort's machines — **the reference machine is 16 GB RAM with a 6-to-10-core CPU, and every limit here is sized against the low end of that range, 6 cores** — and a projected **≤24 hours of elapsed machine time for the entire required programme** on the reference machine, including preprocessing, classical fits, permitted development, core training and repeated inference. **Report elapsed time and aggregate CPU time separately**: aggregate CPU time is user plus system time summed over the main process and every worker process (Python's `time.process_time()` covers the calling process only, so data-loader workers must be added), with the thread and worker settings used. **Meeting the per-fit limits does not by itself establish compliance with the programme budget**: the per-fit limits bound scheduled training time, and preprocessing, classical fits and repeated inference sit outside them. *(Corrected 24 September 2026. This said "≤24 CPU-hours". Every figure the pack used to justify it was elapsed time, and on a six-core machine running every core, 24 CPU-hours is only four elapsed hours — less than several cards' scheduled training. The budget is therefore stated as what it was always computed as: 24 elapsed hours on the reference machine.)* **You record the actual hardware, threads, memory and timing** — cores, RAM and OS in the readiness note, and peak memory, elapsed time, CPU time and per-epoch time for every reported fit. These limits are not a substitute for that record. A reference fit must complete a functioning training/validation cycle and an inference pass, not merely one batch; if yours cannot within the limit, say so and say what it would need. *(Corrected 25 September 2026: this said "demonstrate learning and a usable full evaluation". A correctly implemented model that does not beat a baseline has not failed this check; negative results earn full marks.)* Negative comparative results remain valid.
- The **reference** means the no-attention models and named fusion on the row's data/protocol. Add one attention-enabled variant to the named host; the no-attention fit already counts as its ablation. All component metrics must be reported on the same reference split. Fusion adds no neural fit: combine two predictions, with one global weight from {0, 0.25, 0.5, 0.75, 1} selected on validation (ties: closest to 0.5). I1 uses fixed 0.5 because nominal-only development cannot optimise anomalous-class F1. Use no-attention partners for the named fusion; do not add a third model.
- For multilabel tasks, select each class threshold from {0.1, 0.2, …, 0.9} on validation F1; ties favour the larger threshold. If either label value is unsupported, use 0.5, mark selection unsupported, and report the support. No threshold selection on test. I1's anomaly thresholds follow D6 instead.
- Macro-F1 uses the **fixed, declared label universe**, with zero contribution for an undefined per-class F1 and an explicit unsupported flag. Per-class recall with no positives is **NA**, not zero evidence of failure; report the number of supported classes. Balanced accuracy is the mean recall over supported classes, labelled with that denominator. AUC is NA when only one label value is present; a complete-universe macro-AUC is NA if any required class is undefined. Never silently change the class universe to improve a score. No uncertainty method makes a handful of independent units sufficient for population claims.

| Card | Reference and attention host | Required neural fits, including demonstrations | Evaluation/repetition that adds no fit |
|---|---|---:|---|
| A1 | CWRU 0-hp guarded blocks; frequency attention in image CNN | 7: four source-load 1-D fits + one Paderborn 1-D + image + attention | Four target loads per CWRU fit |
| A2 | Pooled-load guarded blocks, parameter-matched pair; image attention | 5: two parameter-matched + two time-matched + attention | Cost/Pareto table from those fits |
| A3 | Pooled-load guarded blocks; image attention | 4: valid/audit 1-D + image + attention | Gap is descriptive |
| B1 | Colour/common-label source split, no extra augmentation; image CBAM | 6: control + three augmentation variants + profile + CBAM | All four image variants on both domains |
| B2 | Matched colour split; image CBAM | 5: colour/segmented/greyscale + profile + CBAM | Fixed attribution interventions |
| B3 | 50 training leaf groups/class; image CBAM | 5: three image caps + profile + CBAM | 1,000 leaf-group bootstrap draws |
| C1 | Full D3 five-output forecast; attention on LSTM | 4: LSTM + TCN + map CNN + attention | Month/lead/barrier slices |
| C2 | Same D3 forecast; attention on LSTM | 3: LSTM + map CNN + attention | Lead/cost table |
| C3 | Same D3 forecast; attention on LSTM | 3: LSTM + map CNN + attention | Event/neutral/onset slices |
| D1 | Clean METR-LA; graph attention | 4: graph + per-sensor + image + attention | Four-system table; ARIMA is an extra classical baseline |
| D2 | Geographic METR-LA; graph attention | 16: thirteen no-attention graph fits + per-sensor + image + attention | Edge sensitivity without retraining |
| D3 | Clean METR-LA; graph attention | 6: graph/per-sensor in two cities + METR image + attention | Five paired mask seeds, six rates, two outage types |
| E1 | Built-in split, unaugmented; image spatial attention | 4: image control/augmented + profile + attention | Rare-class frequency analysis |
| E2 | Matched lot-disjoint split; image spatial attention | 5: two models × two protocols + attention | Fusion only on the matched reference |
| E3 | Built-in supervised-only reference; image spatial attention | 5: supervised image + two pseudo-label fits + profile + attention | One pseudo-label round per cap |
| I1 | OPSSAT-AD nominal training; temporal attention in 1-D autoencoder | 5: OPSSAT sequential/image/attention + two stream sequential fits | Native scores and point-adjusted audit |
| I2 | Official PTB-XL folds; 1-D lead attention | 8: official 1-D + five audit 1-D + image + attention | Class-wise analysis of the five contrasts |
| I3 | 100-cycle horizon; attention on 1-D cycle-summary branch | 5: three horizon 1-D + image + attention | 1,000 paired held-out-cell bootstrap draws |
| I4-S | F1 (target S1), transfer protocol, 14 bands; image band attention | **12**: F1 two protocols × two band sets, F2–F4 transfer only × two band sets, + 1-D + attention | Both protocols scored on F1's 570 S1 test patches; F2–F4 are transfer-only whole-scene folds |
| I5 | Clean focal split; spectrogram time–frequency attention | 3: waveform + spectrogram + attention | Two research models, clean + five SNRs, same test windows |
| I6 | L2A fixed paired subset, seed 22; 1-D temporal attention | 7: two models × two levels + two extra L2A 1-D seeds + attention | L1C/L2A contrasts; reference seed summary only |

**Week-1 measurement (readiness note, §8 item 7).** Time the configuration below — it is one of your required fits, run once under the D0 limits and reused later — and project the stage in the last column from a measured subset rather than running it in full. *(Added 24 September 2026. Each entry is the required configuration most likely to hit a limit on your card: the largest training set, the largest input, or a classical or inference stage that the neural limits do not bound.)*

| Card | Reference configuration to time | Stage to project from a measured subset |
|---|---|---|
| A1 | Paderborn 1-D CNN (3,116 training windows) | CWRU spectrogram CNN, one source load |
| A2 | Pooled-load spectrogram CNN, parameter-matched | The 15-minute time-matched pair |
| A3 | Valid guarded-protocol 1-D CNN — learning and validation are judged on this fit only | Audit-protocol 1-D workload (stride-512 windows, the largest training set on the card): time a fixed number of **training** updates for throughput only; do not run audit validation or test, and do not use it to set anything |
| B1 | MobileNetV2 head, no-augmentation control, 28-class caps | Cropped-PlantDoc evaluation of four models |
| B2 | MobileNetV2 head, colour condition | Segmented-mask attribution pass over 100 images |
| B3 | MobileNetV2 head at the 50-group cap | 1,000-draw leaf-group bootstrap |
| C1–C3 | Map CNN on the 24-month grid stack | — |
| D1 | GCN+GRU on METR-LA | ARIMA bank: time 20 sensors, project 207 |
| D2 | One geographic GCN+GRU fit at the 20-minute limit | Thirteen graph fits = 13 × that elapsed time |
| D3 | GCN+GRU on PEMS-BAY | ARIMA banks: time 20 sensors per city, project 207 + 325; one mask seed × six rates × two outage types, project five seeds |
| E1 | Augmented image CNN on the built-in split | — |
| E2 | Image CNN on the matched split (103,853 training wafers) | Built-in-protocol fits |
| E3 | Image CNN with the 10,000-wafer pseudo-label cap | Pseudo-labelling pass over the eligible pool |
| I1 | 2-D spectrogram autoencoder on OPSSAT-AD | Stride-1 scoring of P-1 and C-1 |
| I2 | Official-fold 1-D CNN (17,073 training records) | — the five audit fits repeat it |
| I3 | 2-D CNN on the 100-cycle surface | Struct parsing and compaction (Card I3), one batch |
| I4-S | F2 transfer fit, 14 bands (S1 + S4 training, 3,414 non-degenerate patches, the largest fold) | F1 within-group fit |
| I5 | Log-mel CNN on the focal training windows | One full evaluation: clean + five SNRs on focal test, plus all Powdermill windows |
| I6 | L2A time–band image CNN | Per-region acquisition and pairing, one region |

Report, for that run: hardware (cores, RAM, OS), thread and data-loader worker settings, elapsed time and aggregate CPU time, epochs and optimisation updates completed, which limit stopped it, peak memory, the evidence of optimisation (training and validation loss over the run, or a documented converged state), and whether validation and one **timed, unscored** inference pass over test-shaped data finished — never compute or look at test metrics here. **I1:** judge optimisation by reconstruction loss and nominal calibration on nominal-development data only; there is no anomalous-class validation selection. Fewer than five completed epochs prompts a review of the configuration, not an automatic failure. Then project your whole required programme — neural fits, classical baselines and repeated inference — against the 24-hour elapsed budget.

Every card inherits **all** Handout §2 checkpoints and outputs, including the 4–6-page report, independent repository and individual defense. Optional work never becomes a prerequisite for full marks. D0 does not change the rubric or the Week-2 written outcome-alternative rule.

# Protocol Annex D1 — Bearings

**CWRU recording selection.** Use the official drive-end **12 kHz, 0.007-inch** inner, ball and outer-at-6-o'clock faults at each load 0/1/2/3 hp (`IR007_0`…`IR007_3`, `B007_0`…`B007_3`, `OR007@6_0`…`OR007@6_3`), plus `Normal_0`…`Normal_3`. Use drive-end acceleration only. The instructor resolved the files on 24 September 2026; you reproduce them. Fault files: `105`–`108.mat` (IR007_0–3), `118`–`121.mat` (B007_0–3), `130`–`133.mat` (OR007@6_0–3), all 12 kHz. Normal files: `97`–`100.mat` (Normal_0–3). The sixteen files total 70,056,712 B; hashes are in `cwru_recordings.json`, issued with the cards. **The normal files are 48 kHz**: CWRU's pages do not say so, but their lengths (about 484,000 samples, about 10 s) and their shaft-harmonic structure agree on it. Anti-alias and resample all four to 12 kHz (polyphase, factor 1/4). Do not relabel sample indices as a new sampling rate. **🔴 `99.mat` (Normal_2) holds two recordings**: `X099_DE_time` and a byte-identical copy of Normal_1's `X098_DE_time`. Use `X099_DE_time`. A loader that takes the first `_DE_time` variable it finds would put Normal_1 at two loads. **`97.mat` (Normal_0) is only 5.08 s**, so the 0-hp healthy recording supports 16 / 3 / 4 train / validation / test windows, against 34 / 9 / 10 for most recordings. `98.mat` and `99.mat` carry no RPM variable; use the page's nominal speeds. These source labels are listed on the [CWRU fault page](https://engineering.case.edu/bearingdatacenter/12k-drive-end-bearing-fault-data) and [normal page](https://engineering.case.edu/bearingdatacenter/normal-baseline-data).

For each recording of length N after resampling, let a=floor(0.6N), b=floor(0.8N), L=2,048 samples. Use half-open sample intervals train [0,a−L), validation [a+L,b−L), test [b+L,N). Omit the two guard intervals. Cut L-sample windows at stride L wholly inside each block; no window crosses a boundary. Use all supported windows, at most 1,000 per recording/partition by evenly spaced start indices if necessary. The instructor's count over the sixteen recordings is 527 / 139 / 155 windows; no recording reaches the cap. Apply the same IDs and windows to both representations. Fit scaling and any envelope-classifier decision rule on training data. Tune on source validation only.

**A1:** one source load per fit; all four fixed test blocks supply the matrix columns. The diagonal is held out, not resubstitution. Fault diameter and outer position stay fixed, but recording/bearing identity may still be shared across loads. Call the result **cross-load performance in this rig and selected faults**, not unseen-machine or unseen-bearing generalisation.

**A2:** pool the four loads within each of those partitions. Parameter-matched 1-D/image models target 50,000 trainable parameters ±10%, with identical 30-epoch caps and the D0 time ceiling. Separately rerun the same two architectures with **15-minute allowances each** on the same machine and thread count; remove the epoch ceiling for that time-matched comparison, retain validation checkpointing, and log optimisation updates. A ≤1-update timing overrun is recorded. Classical envelope features have no artificial parameter target. Report macro-F1 against cost; accuracy is supplementary.

**A3:** the valid experiment uses A2's guarded blocks. For the audit only, cut windows of L=2,048 with stride 512 across the same complete recordings and assign windows 60/20/20 using a seed-22 permutation within recording. Record the actual raw-sample overlap between partitions; never use the audit for model selection of the valid run. **Freeze every valid-run choice — architecture, optimisation settings, checkpoint — before any scored audit run.** The Week-1 audit measurement is a training-throughput timing only (Annex D0), and nothing it shows may change the valid configuration. *(Added 25 September 2026: the Week-1 table had named the audit fit as A3's reference, which would have let the leaky protocol steer the valid one.)* Fit preprocessing separately under each protocol. The test population changes, so the observed gap combines overlap and changed partitions. The audit is deliberately leaky and exempt from the leakage penalty.

**Paderborn A1 — the approved split.** **Confirmed 24 September 2026:** all fourteen archives parse; each holds 80 `.mat` records, 20 of them at N15_M07_F10; and each bearing's own data sheet in the archive matches the table below. KA01, KA03 and KA05 are artificial outer-ring damage, KI01 and KI03 artificial inner-ring damage, KA04 and KA22 natural outer-ring pitting, KA15 natural outer-ring indentations, and KI16 natural inner-ring pitting. **KI04 carries two damages.** Its data sheet in the archive lists fatigue pitting on the inner ring and particle-caused indentations on the outer ring (damage combination "M"). It keeps the authors' inner-ring designation here, as a natural inner-ring test bearing, but report KI04's results separately in your error analysis and do not read its errors as pure inner-fault behaviour. Use N15_M07_F10 vibration only: `Y` channel `vibration_1`, 64 kHz. Its length varies by record, from 250,604 to 284,704 samples; do not assume 256,000. Resample 64 kHz to 16 kHz with an anti-alias filter, then use 2,048-sample non-overlapping windows. Never mix these samples with CWRU labels.

| Partition | Healthy | Artificial outer | Artificial inner | Natural outer | Natural inner |
|---|---|---|---|---|---|
| Train | K001, K002 | KA01, KA03 | KI01 | — | — |
| Validation | K003 | KA05 | KI03 | — | — |
| Test | K004 | — | — | KA04, KA15, KA22 | KI04, KI16 |

This is fourteen archives. KI01/KI03 replace the erroneous KA07/KA09 choices of Revisions C and D; the [official index](https://groups.uni-paderborn.de/kat/BearingDataCenter/) lists those archives, and their inner-ring assignment is in the [original dataset paper, Table 4](https://papers.phmsociety.org/index.php/phme/article/download/1577/542). Archive existence is not a completed parse check. Publish the 5/3/6 bearing counts and measured recording/window counts. The instructor's count at 16 kHz is 620–632 windows per bearing: train 1,242 healthy / 1,254 outer / 620 inner, validation 620 / 622 / 621, test 620 / 1,862 / 1,242. The small number of independent bearings, especially source inner faults, limits inference; windows do not increase that independent count.

The envelope baseline must use an actual implemented decision model, not a plotted spectrum: extract envelope-band energy around the dataset's documented defect-frequency ratios and harmonics, plus RMS/kurtosis, then a small validation-selected classifier (nearest-centroid or RF). Cite the geometry/frequency source and keep the extraction rule fixed across the compared protocols. Frequency attention is in the spectrogram CNN, with frequency axis kept intact. No spectral feature or filter parameter is tuned on target test recordings.

# Protocol Annex D2 — Crop disease

**Splits and subsets.** The split is **issued as a frozen file, `PlantVillage_color_split.csv`** (54,305 rows, SHA-256 `dfca1873…13fe`), with per-class group and image support in `PlantVillage_class_support.csv`. It was built by three rules. You reproduce it in Week 1; where your run differs, the issued file governs.

1. **Leaf ID.** Images are `raw/color/` at commit `7f7ecc7e1eaca78107e3affe7cb5abd9427e139a` of the authors' GitHub repository. The leaf ID follows the authors' Hugging Face loader (`plant_village.py`, dataset `mohanty/PlantVillage` at revision `9e97599868962bd0079b8db4b7f1efa9185fa1e7`): remove `_final_masked`, keep the part after the last `___`, cut at `copy`, remove the extension, strip spaces, and look the lower-cased stem up in `leaf_grouping/leaf-map.json`. Take a single suggestion; otherwise take the suggestion containing the class folder name; otherwise, or if the stem is absent, the ID is `fallback_<stem>`.
2. **Published membership, repaired.** Start from the published lists on the Hugging Face dataset at that revision (`splits/color_train.txt`, 43,596 images; `splits/color_test.txt`, 10,709). **Any leaf ID found on both sides goes wholly to training.** This moves 243 test images in 227 leaf IDs.
3. **Validation carve.** Within training, per class, sort leaf IDs by the SHA-256 hex digest of `22|<leaf_id>` (the issued `leaf_id` string, UTF-8, ascending) and move the first floor(20%) to validation. Every class has at least 22 training leaf IDs before the carve, so every class gets validation groups.

**Result: 35,015 train, 8,824 validation, 10,466 test images; 20,015 leaf IDs, none in two partitions and none in two classes.** All images of a leaf remain together. A conflicting class label within a leaf group would be a data gate, not permission to split it; none occurs. Hash ordering is deterministic; do not redraw until test scores improve.

**🔴 Corrected 23 September 2026: what the source provides.** Earlier issues said the authors' 80/20 split respects leaf grouping and that the grouping covers the dataset. Neither holds in full.

- **The published split leaks.** For 227 photograph stems, crops of one photograph (files named `… copy`, `… copy 2` and so on) sit on both sides of it: 243 test images, 187 of them among Corn healthy's 250. One case was confirmed by eye. Rule 2 repairs this.
- **The leaf map covers 25 of the 38 classes** (at least 99.9% of each class's images). It has no entries for eight classes — all four Corn classes, Grape healthy, Squash powdery mildew, Tomato mosaic virus and Tomato target spot — and covers five only partly: Strawberry leaf scorch 70%, Tomato healthy 63%, Tomato Septoria leaf spot 57%, Tomato yellow leaf curl virus 51% and Tomato late blight 48%. There, a `fallback_` ID groups the crops of one photograph, **not** separate photographs of one leaf, and those cannot be grouped from the release. Treat results on these 13 classes as possibly optimistic, and say so. Apple black rot's leaf IDs are listed under `Apple_Frogeye Spot`, the same disease; they are used as they stand.
- **The splits are on Hugging Face, not in the GitHub repository**, which holds the images and the leaf map.
- **`raw/color/` holds 21 byte-identical pairs** (42 files). Every pair shares one leaf ID, so one partition; five of them straddled the published split.

B1/B2 train on at most **300 images per class**, validation on at most 100 and source test on at most 100, adding whole groups in hash order only if the complete group fits the cap.

**🔴 Time your first fit before you plan the rest.** The instructor's throughput check of 24 September 2026 put MobileNetV2 at 128×128 with a frozen backbone and a trained head over the 10,766 images these caps allow at roughly **122 seconds per epoch on two cores** — about fourteen epochs inside the 30-minute limit. The reference machine has six cores, but more cores do not reliably mean proportionally faster training — memory bandwidth, thread scheduling and oversubscription all intervene — and **your machine was not measured before your card was issued**, so time the reference configuration for your card (Annex D0's Week-1 table) and report it in your readiness note (§8 item 7). Remember that the frozen backbone's forward pass is most of that cost and that D0 counts inference time as compute. If the cap stops you before the head has learned, say so and the configuration will be corrected — a scope cut made on measured evidence carries no penalty. B1 keeps only the issued common-label map (`B1_common_label_map.csv`: 28 mapped classes, 27 evaluable on the target, 10 excluded) and excludes unmapped labels in both domains. Under these caps B1's 28 classes give at most 7,972 / 2,521 / 2,645 source images, and all 38 classes give 10,766 / 3,429 / 3,530; per-class figures are in `PlantVillage_class_support.csv`. Use the shipped **Cropped-PlantDoc test partition only** — 236 images at the pinned commit — and report *Tomato two spotted spider mites leaf* as unsupported. Never train on either PlantDoc partition. Report the headline gap with and without the classes affected by the eight cross-split label conflicts listed on Card B1.

**B1 research:** train the image model under no additional augmentation, colour jitter, random occlusion and both. Jitter uses brightness/contrast/saturation factors uniformly in [0.8,1.2]; occlusion covers one square of 10% image area, chosen uniformly among valid positions and filled with the source-training channel mean. These are training-only transformations. Keep schedule and partitions fixed. Evaluate the four already-fixed models on both test domains once; no further tuning follows target inspection. Profile/CBAM/fusion are reference demonstrations only.

**B2 research:** use identical image IDs in colour, segmented and greyscale, with the colour-ID split propagated to all. The correspondence is issued as `PlantVillage_B2_alignment.csv`. 53,109 colour images match their segmented file by name; 1,196 match on the part after the last `___`, because only the segmented name carries the UUID prefix (1,192 of them Corn common rust). Greyscale matches all 54,305 by name. One segmented file, `Grape___Esca_(Black_Measles)/7e1fd9b9-1fd9-4f98-93f5-8cf9ebc60dd9___FAM_B.Msls 4430_final_masked.jpg`, has no colour counterpart and is not used. Four segmented files are not 256×256 (324 to 470 × 512) and one is single-channel: resize and convert them, and report it. Greyscale files are stored with three channels. Greyscale is repeated into three channels; no independently sampled greyscale split. Retrain only the image model for these three conditions. For the attribution check, use at most 100 fixed hash-selected source-test images, a leaf/background mask inferred from the segmented counterpart with manual spot-checks, and a same-area random occlusion control. Report mask failures and observed changes; no lesion localisation claim or new lesion annotation is required. This post-training analysis never selects the model.

**B3 research:** define eligibility from the frozen source inventory, not model results: at least 50 training, 10 validation and 10 test leaf groups for a class, **counting only real leaf groups**, meaning a class whose images are at least 99% covered by the leaf map. A `fallback_` ID groups a photograph, not a leaf, so it cannot support a per-leaf learning curve. Retain that same eligible class universe at all caps. Use the first 10/25/50 training groups per class in the fixed hash order; smaller sets are nested. To bound multiple views, keep the first two images per selected leaf group, in ascending order of the issued `path`, at all caps. Validation/test use up to 20 groups per class and the same two-view bound. Report exclusions and the fact that this is a supported-class study, not all 38 classes if some fail. **Confirmed 23 September 2026: 19 classes across 11 crops are eligible** — Apple scab, Apple healthy, Blueberry healthy, Cherry healthy, Grape black rot, Grape esca, Grape leaf blight, Orange Haunglongbing, Peach bacterial spot, Pepper bacterial spot, Pepper healthy, Potato early blight, Potato late blight, Soybean healthy, Strawberry healthy, Tomato bacterial spot, Tomato early blight, Tomato leaf mold and Tomato spider mites. Six classes with real groups fall short on support: Apple black rot, Apple cedar rust, Cherry powdery mildew, Peach healthy, Potato healthy and Raspberry healthy. The 13 classes with missing or partial leaf maps are excluded on coverage; counting their `fallback_` IDs as groups would have made 32 eligible. At the three caps the study uses 190 / 475 / 950 training groups (380 / 949 / 1,899 images); validation uses 373 groups (746 images) and test 375 groups (750 images). Bootstrap 1,000 draws of test leaf groups within each class, preserving their image bundles, seed 22. Report percentile intervals for recall and paired differences; interval width does not establish a universal sample requirement.

# Protocol Annex D3 — ENSO forecast and event contract

**Products and scope.** The target is the **ERSST v5 Niño 3.4 monthly anomaly published by NOAA CPC**: the `ANOM` column after `NINO3.4` in [`ersst5.nino.mth.91-20.ascii`](https://www.cpc.ncep.noaa.gov/data/indices/ersst5.nino.mth.91-20.ascii), January 1950–December 2024, against CPC's fixed **1991–2020** monthly climatology. The grid is PSL's ERSST v5 [`sst.mnmean.nc`](https://downloads.psl.noaa.gov/Datasets/noaa.ersst.v5/sst.mnmean.nc) ([dataset page](https://psl.noaa.gov/data/gridded/data.noaa.ersst.v5.html)), 2° native cells in **20°S–20°N, 120°E–280°E**. That box holds 21 × 81 = 1,701 cells: 75 are land in every month and 1,626 are ocean in every month, so the land mask is fixed. Use the same 1950–2024 interval and retain the ocean cells.

**Issued snapshot, 23 September 2026.** Both files are live and revised monthly, so the instructor's copies govern. Index: 67,087 B, SHA-256 `bedcd068…8012`, last modified 5 August 2026, no missing month in 1950–2024. Grid: 159,094,577 B transferred, SHA-256 `651c3ced…a971`, last modified 3 September 2026. The index is issued as downloaded; the grid is issued as its D3 subset, `TrackC_ERSSTv5_subset.npz` (900 months × 21 × 81, land as NaN, 4,921,092 B; SHA-256 of the float32 array `8e566e66…3570`). Download the grid yourself in Week 1 and confirm your subset matches; if it does not, report the difference and use the issued copies. The index and the grid are the same product: the cos-latitude-weighted grid mean over 5°S–5°N, 170°W–120°W matches CPC's absolute Niño 3.4 within 0.027 °C in every month.

**🔴 Corrected 23 September 2026: the PSL route delivered v6.** Earlier issues named PSL's Niño 3.4 page, titled ERSST v5 with a 1981–2010 climatology, and its data file `nina34.anom.data`. On 23 September that file's own footer read **ERSST V6**, it began in 1948, and it had been modified that day; the page's CSV and NetCDF links carried a different product (OISST v2). The route is withdrawn. CPC's 1981–2010 v5 file stops at December 2020, so the course uses CPC's current v5 file and its 1991–2020 base. The change of base moves anomalies by at most 0.14 °C, depending on calendar month, and leaves the number of strong events in each partition unchanged. The supplied series is a retrospective analysis with a published reference climatology; this is a hindcast study, not an operational real-time forecast claim.

**Examples.** At issue month t (after that month's data are available), inputs contain months t−23…t. The index model has 24 scalar inputs. The image model uses the same 24 months as channels over the Pacific spatial grid; no future maps. Compute grid monthly climatology from **1950–1994 only** and subtract it; standardise channels using training examples only. The target remains the published index in °C, not a newly recomputed regional mean. Difference between the published target climatology and training-grid climatology is explicit. Land is filled with zero after standardisation and excluded from fitted grid statistics.

All neural models produce **five direct outputs**, y(t+1), y(t+3), y(t+6), y(t+9), y(t+12), with one fit per model, not one per lead. Keep an example only if **all five target months** lie inside exactly one interval: training January 1950–December 1994; validation January 1995–December 2004; test January 2005–December 2024. The 24-month input rule naturally removes early examples. Report excluded boundary examples and resulting counts. The instructor's count is **505 training, 109 validation and 229 test issue months**, with 22 excluded because their five targets span two periods (865 in all). No current/future target values enter input normalisation or model selection.

**Baselines and models.** Persistence predicts y(t) at every lead. Fit a direct multi-output ridge autoregression from the same 24 index lags, selecting alpha from {0.1, 1, 10} on validation; this is the card's AR baseline. C1 and C3 use one single-layer LSTM (32 hidden units) with a linear five-output head, and C1 adds one small dilated TCN. All use the map CNN, and temporal attention is on the LSTM. **C2 matches its two neural systems to 30,000 trainable parameters ±20% (24,000–36,000) and the same 15-minute allowance, so it uses the fixed pair below**; report actual counts and updates.

**C2's matched pair, counted with PyTorch 2.14.0 on 24 September 2026.** *Index LSTM:* `nn.LSTM(input_size=1, hidden_size=84)` over the 24 monthly steps, last hidden state into `nn.Linear(84, 5)` — **29,657** trainable parameters. *Map CNN:* input 24 channels × 21 × 81 (land zero-filled); `Conv2d(24→32, 3×3, pad 1)` → ReLU → `MaxPool2d(2)` → `Conv2d(32→32, 3×3, pad 1)` → ReLU → `MaxPool2d(2)` → `Conv2d(32→16, 3×3, pad 1)` → ReLU → `AdaptiveAvgPool2d((3, 6))` → flatten (288) → `Linear(288→32)` → ReLU → `Linear(32→5)` — **30,229** trainable parameters. Both sit inside the ±20% band and under Track C's 50,000 ceiling. The attention variant adds its parameters to the LSTM and is reported separately; it is not part of the matched pair. *(Corrected 24 September 2026. This annex told C2 to use C1's 32-unit LSTM and also to match 30,000 parameters. A scalar-input 32-unit LSTM with a five-output head has 4,645 parameters, far outside the band, so the two instructions could not both be followed. The recurrent layer stays at 32 units for C1 and C3; C2 widens it to 84 units, which is the only change.)* A CNN seeing the field and an LSTM seeing an index compare input-and-model systems, not architecture in isolation.

**C1 barrier strata.** Define a barrier-crossing pair as one whose months t+1…t+h include at least one April, May or June; otherwise non-crossing. This is a declared course stratification, not a universal physical definition of the barrier. Index the heatmap by **issue month**, with five lead columns. Report counts, RMSE and Pearson correlation of anomaly predictions and observed anomalies (ACC); return NA if fewer than three pairs or either variance is zero. Use matching target pairs across systems.

**C3 events.** Define z(m)=[y(m−1)+y(m)+y(m+1)]/3. A warm event is a maximal run of at least five consecutive central months with z≥+0.5°C; a cold event uses z≤−0.5°C. A warm event is strong if its run reaches z≥+1.5°C, and a cold event if it reaches z≤−1.5°C. **Onset is the first central month of that qualifying run.** Build events on the full pinned series for retrospective evaluation only. Exclude edge-truncated runs and any event that intersects a target partition boundary from per-event summaries; report these exclusions. Do not feed retrospective z or event membership to a forecast.

**The instructor's count on the issued index.** 16 warm events (9 strong) and 25 cold events (8 strong). Usable strong events by the partition of their onset: warm 5 / 1 / 3 and cold 4 / 1 / 2 (train / validation / test). The test period's strong events have onsets 2009-08, 2015-03 and 2023-06 (warm) and 2007-07 and 2010-06 (cold). Excluded: two non-strong warm events that cross a boundary (1994-09 to 1995-02 and 2004-08 to 2005-01) and the strong cold event of 1950-02 to 1951-03, which touches the series edge. **The cold phase has two test events, so it is a descriptive case series under the rule below.**

Neutral months satisfy |z|<0.5°C and lie at least **three months outside every qualifying warm/cold event**, including non-strong events. On the issued index this gives six test spells and 44 months: 2005-05 to 2005-07, 2012-07 to 2014-10, 2017-04 to 2017-06, 2019-09 to 2019-10, 2020-01 to 2020-04 and 2024-08 to 2024-11. *(Corrected 23 September 2026: this said six months. With six, the test period has three neutral spells, 23 months, one month and one month, and equal spell weighting would give each single month the weight of the two-year spell.)* Group consecutive neutral months into neutral spells. Experiment 1 scores forecasts **targeting** strong-event months versus neutral months. At a given lead, compute mean squared error within each event/spell, average those means equally across supported events/spells, then take the square root. Report pooled month-weighted RMSE separately if useful; never confuse it with the equal-event score. ACC is descriptive on all supported pairs with counts; no significance claim from adjacent months.

Experiment 2 scores only forecasts whose **target month equals onset**; the corresponding issue is onset−h. For each lead and each comparator b (persistence and AR separately), skill is **1−RMSE_model/RMSE_b**, using the identical supported onset events with equal event weight. If RMSE_b=0 or no event is supported, skill is NA. Report individual event errors; a phase with fewer than three independent events is a descriptive case series, not evidence of general phase superiority. No reruns or new training are needed for these slices.

# Protocol Annex D4 — Traffic

Use complete METR-LA and, for D3, complete PEMS-BAY raw time axes and supplied sensor orders. Let N be the number of chronological rows; boundaries are floor(0.7N) and floor(0.8N). Input history is **12 five-minute steps** and outputs are steps **3, 6 and 12**. Every output target in an example must remain inside its own partition; earlier history may cross a boundary if already observed. This preserves the 70/10/20 intent with an explicit boundary purge and is not an exact reproduction claim for every published DCRNN preprocessing detail. Train at every sixth eligible issue time to bound cost; validation/test use every twelfth eligible issue time. Always keep all sensors and report example counts. This rule also bounds D3's PEMS-BAY replication without selecting a different city segment after results.

**The instructor's parse, 23 September 2026.** `metr-la.h5` (57,038,056 B, SHA-256 `64784b76…7c05`) and `pems-bay.h5` (135,930,936 B, `65d69fb0…153c8f`) from the authors' Google Drive folder; `adj_mx.pkl` and `adj_mx_bay.pkl` from the DCRNN repository at commit `602afd9`. Sensor order in each speed file equals the order in its adjacency pickle. The 1,515 and 2,369 edges are **directed off-diagonal non-zeros**; counting the self-loops gives 1,722 and 2,694. Neither matrix is symmetric. One METR-LA sensor and six PEMS-BAY sensors have no off-diagonal edge. METR-LA runs 1 March to 27 June 2012 with no gap. PEMS-BAY runs 1 January to 30 June 2017, with one 12-step gap at 2017-03-12 02:00, the daylight-saving change; rows are consecutive either side of it. Zeros are 8.11% of METR-LA entries: 7.1% of the training partition and 12.1% of test. 2,148 METR-LA time steps are zero at every sensor, in 97 outages (the longest 381 steps; 666 of those rows fall in test). PEMS-BAY zeros are 0.0031%. Under this annex, METR-LA has 3,995 / 285 / 571 train / validation / test issue times (N = 34,272; boundaries at rows 23,990 and 27,417), and PEMS-BAY 6,077 / 434 / 868 (N = 52,116; boundaries 36,481 and 41,692).

Fit per-sensor means/scales on observed training speeds. A zero marks missingness. Impute missing values with that sensor's training mean, hence zero after scaling, and append a separate observed/missing indicator to each model's input. All models use the same allowed information. Exclude originally missing target values from losses/metrics; artificial input masks never delete valid scoring targets. Inverse-transform predictions before scoring. MAPE averages |prediction−truth|/|truth| over observed truth >0 and multiplies by 100; report its count and low-speed sensitivity beside MAE/RMSE.

Historical average uses training observations at the matching weekday and five-minute slot, falling back to sensor training mean when unsupported. **ARIMA:** fixed (2,0,1) independently per sensor, fitted once per city on observed/imputed training data; no order search or refitting at test time. Roll its state forward with only available observations. If convergence fails, publish the affected sensors and use the historical-average fallback for those sensors with the failure count. Count those classical fits and their cost. **The ARIMA banks are the largest classical fits in the pack — 207 independent fits for METR-LA and 325 for PEMS-BAY, 532 in D3 — and they were not timed before issue.** Time 20 sensors, project the full bank or banks, and report elapsed and CPU time in your readiness note alongside your neural timing (§8 item 7; Annex D0's Week-1 table). If the full bank does not fit the 60-minute classical allowance, say so rather than trimming it. *(Corrected 24 September 2026: this said "207 independent ARIMA fits per city"; PEMS-BAY has 325 sensors.)* **Do not silently evaluate ARIMA on a favourable subset.** *(Changed 24 September 2026: this sentence previously said an instructor pre-issue pilot confirmed the bank fits. No such pilot was run; see Annex D0 and your readiness note, item 7.)*

The GCN+GRU shares its temporal and output weights across nodes. The per-sensor LSTM shares weights but has **no cross-node mixing**. The image CNN may mix nodes, but it is not part of D2's identity architectural control. D1 uses the same per-fit time allowance for its three neural systems and reports actual parameter differences; it does not assert simultaneous parameter matching.

**D2 graph construction and fit semantics.** Geographic adjacency follows the shipped direction/threshold convention with node alignment checked; fix self-loops consistently. Construct a separate training-derived graph from pairwise training-speed correlations on jointly observed values (at least 100 paired times). Rank positive correlations, ties by sensor IDs, keep exactly as many directed non-self edges as the geographic graph, and normalise rows consistently; if there are too few usable positive pairs, stop and consult; the construction is then revised openly. This is a data-derived adjacency, not evidence of end-to-end learned geography. Identity uses self-edges only. Every permutation P A Pᵀ (seeds 101–110) is applied to graph indices while signals remain in their original order. Retrain for each adjacency with training seed 22, giving thirteen graph fits. A model with a dense sensor-axis layer fails the identity precondition.

For the attention variant on the geographic reference, average non-self edge weights over a fixed validation subset to define the removal ranking; compare them with finite supplied road distances using Spearman correlation and report the edge count. Remove the top 10% and 30% (floor counts) versus one seed-22 random set of identical size at each rate, retaining self-loops and renormalising the remaining weights. Evaluate clean and removed graphs without retraining. Interpret as reliance on those edges, not a causal account of traffic or proof that attention explains the mechanism.

**D3 masks.** Seeds 101–105 are mask realisations only. Draw uniforms once per seed; increasing mask rates use nested thresholds, shared across every compared system. Independent masking selects each originally observed input entry. Block masking selects sensors and removes all **12 history steps** for each selected sensor; it is a full one-hour input outage. Set the selected values to the training-mean fill and their indicators to missing. Report achieved missing fractions, as original missingness changes them. Do not mask future labels. Evaluate graph, per-sensor, historical average and the fixed ARIMA bank under the same information cutoff; historical average is expected not to change because it uses no current sensor observations. Train only graph/per-sensor models in PEMS-BAY; image/attention/fusion remain METR-LA demonstrations. Across seeds report mask-realisation variation, not training uncertainty.

# Protocol Annex D5 — Wafer maps

Retain nine labels in their documented mapping. Build one inventory from `WM811K.pkl`: the row index as wafer ID, `lotName`, label, original map shape, die count (cells that are not outside-wafer) and built-in membership, testing labels as strings (Track E preamble). Its totals must reproduce the Track E tables. Labels must not be inferred from folder order. Convert maps by nearest-neighbour resizing to **64×64**, retaining categorical values; compute radial/angular profiles from the original valid wafer mask. Do not interpolate categories or treat the outside-wafer region as a good die.

**E1/E3:** preserve built-in test membership. Sort training-side lots by SHA-256 of `22|lotName`, use the first floor(20%) of lots for validation and the remainder for training. The built-in partitions share no lot (Track E preamble), so this validation is lot-disjoint from test as well as from training. If a class has no validation support under this rule, report it and consult. The instructor's run (23 September 2026) gives 1,161 validation lots out of 5,809, and every class has validation support; the thinnest is Near-full at 10 wafers in 10 lots. The validation lot list is in `TrackE_split_lot_lists.json`. Never redraw a split on model results. The core contains all labelled maps; use streamed batches, not a materialised stack of all resized images in RAM.

**E2 (matched split).** Give every labelled wafer a stratum: its class × its die-count quintile. Compute the edges as `edges = np.quantile(die_count, [0.2, 0.4, 0.6, 0.8])` over all 172,950 labelled wafers, with NumPy's default linear method; they come out at 533, 741, 1,060 and 1,376. Assign the quintile as `np.searchsorted(edges, die_count, side="right")`, so a wafer exactly on an edge goes into the upper quintile. Die count equals the pickle's `dieSize` field for every labelled wafer; check one against the other. Run scikit-learn **1.8.0** `StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=22)` with `groups=lotName` and `y=stratum`. Fold *k* is the *k*-th test fold that `split()` yields: fold 0 is test, fold 1 validation and folds 2–4 training. **The split is issued, not regenerated.** The instructor's run is frozen in `TrackE_split_lot_lists.json` (SHA-256 `4083f50c334318891f1f4ac2b6af9712205e77b2be2526d443895da84f6902a6`), issued with the cards: 6,460 training, 2,158 validation and 2,144 test lots, holding 103,853, 34,440 and 34,657 wafers. Reproduce it in Week 1 and report any difference; where your run differs, the issued lists govern. *(Corrected 23 September 2026. This annex previously named die-count quintiles without saying how a wafer on an edge is binned. 14,350 wafers sit exactly on the first edge, and two reasonable rules — the one above and `pandas.qcut` — put 79% of wafers in different folds, so the split was not reproducible as written.)* Beside the same figures for the built-in split, report per-class counts, per-quintile counts, and the share of test wafers whose exact map shape never occurs in training. Compare the 1-D and image CNNs, and fit the classical baseline, under this split and under the built-in protocol with E1's validation rule. Attention and fusion run only on the matched reference. The two protocols are both lot-disjoint, but they differ in training population and size, in held-out class and wafer-size mix, and potentially in optimisation exposure under the time cap, so the gap is a descriptive contrast, not a causal estimate of distribution shift or of lot separation. Report the achieved per-class and per-quintile distributions and the optimisation updates under both. Use D0's unsupported-metric rule.

**E1 augmentation:** classes with <1,000 training examples receive a uniformly sampled multiple-of-90° rotation and a horizontal/vertical reflection during training, with class-balanced sampling capped at four times the original examples of any class per epoch. The unchanged-control and augmented 2-D models share the split, seed and update budget. No extra annotation or synthetic mixed-defect target.

**E3 pools:** exclude every labelled validation/test wafer and every unlabelled wafer whose lot occurs in either partition. Sort eligible unlabelled wafers by SHA-256 of `22|` plus their row index; caps are first 2,000 and first 10,000, hence nested. The supervised image reference supplies pseudo-labels once. Accept a pseudo-label only at probability ≥0.95; freeze this threshold before test. For each cap train a fresh image model with the same supervised data plus accepted pseudo-labels, identical budget and equal weighting per example. No iterative self-training. Report accepted counts by predicted class, class collapse and unchanged/negative gain. No accepted pseudo-labels is a valid finding, not a reason to lower the threshold after seeing test results. The eligible pool was counted on the source pickle at Revision D — 633,277 wafers before the validation carve (Card E3) — so both caps are available. Under this annex's validation carve the eligible pool is **620,038** wafers in 39,496 lots (instructor run, 23 September 2026), and the row indices of both caps are in `TrackE_split_lot_lists.json`.

# Protocol Annex D6 — Telemetry and ECG

## I1 telemetry

Use the provided OPSSAT-AD split. Within its nominal training fragments, order segment IDs by the SHA-256 hex digest of `22|<segment>` and reserve the first floor(20%) as nominal development; train and scale on the other 80%. Anomalous training fragments are unused in the nominal-only core. Report counts by channel. *(Corrected 23 September 2026: this said "the fixed hash" without naming it.)* The instructor's run gives **254 development and 1,019 fitting fragments** from 1,273 nominal training fragments, issued as `OPSSAT_nominal_dev_segments.csv`. Two channels are thin: CADC0886 has five nominal training fragments and none in development, and CADC0890 has three nominal training fragments and no nominal test fragment. Use Zenodo record **12588359** exactly. A later version (record 15108715) shifts 235,509 timestamps by one second, recomputes the duration features and writes `anomaly` into the `label` column of every row. In either version `label` is not the anomaly label: use the `anomaly` column. 1,748 of the 2,123 fragments are shorter than 256 samples, so the resampling below mostly upsamples. Resample each fragment to **256 evenly spaced samples** for the fixed-size autoencoder comparison; keep original lengths and state that this changes time resolution. Use the same nominal preprocessing for the 1-D conv autoencoder and a 2-D spectrogram autoencoder. Reconstruction MSE is oriented high=anomalous. Fit its scale using nominal-development scores only (median and interquartile range; use scale 1 if IQR=0). Fuse the two standardised scores at fixed weight 0.5. Set each detector/fusion threshold at the **99th percentile of its own nominal-development scores**. Do not optimise test F1. The nominal quantile may produce a different test alarm rate.

Isolation Forest and PCA use the same training-only standardisation and a fixed summary feature vector (mean, std, min, max, slope, lag-1 correlation; undefined features imputed by training median). PCA retains the smallest dimension explaining ≥95% training variance; Isolation Forest uses 100 trees, seed 22. Threshold both at the nominal-development 99th percentile. The trivial detector thresholds distance of the fragment mean from the nominal-training mean in training-standard-deviation units, with the same calibration rule; also report constant-all-nominal F1 as a floor. These are declared course controls, not a reproduction of every published baseline.

SMAP **P-1** and MSL **C-1** use their published train/test files and interval labels. **Confirmed and issued, 23 September 2026.** The original S3 archive now returns 403, and telemanom's README routes acquisition through a Kaggle copy that needs an account. The four files are issued with the cards as `SMAP_MSL_train_P-1.npy`, `SMAP_MSL_test_P-1.npy`, `SMAP_MSL_train_C-1.npy` and `SMAP_MSL_test_C-1.npy`, with telemanom's `labeled_anomalies.csv`. They come from the TranAD repository (commit `7ffb98d`), whose readme says they were taken from the original archive; its label file is byte-identical to telemanom's, and every test length equals the label file's `num_values`. P-1: train 2,872 × 25, test 8,505 × 25, three anomaly intervals covering 751 test points. C-1: train 2,158 × 55, test 2,264 × 55, two intervals covering 312 points. C-1's training stream reaches 2.19 while its test stream spans exactly [−1, 1], which is consistent with scaling fitted on the test stream. In the full label file P-2 appears twice with different intervals, and T-10 has files but no label row; neither affects P-1 or C-1. Use column 0 as the sensor input, and audit command-column variability descriptively. Split the nominal training stream into the first 80% fit and last 20% calibration with a **256-step guard gap**. Use 256-step windows, stride 64 for training, stride 1 for scoring; score a time point by mean squared reconstruction error over covering windows. Use the full published test stream and its native index units; handle prefix/suffix with the same padding rule and mask padded values out of losses. Apply the 99th-percentile nominal calibration rule separately per stream. Classical controls use the same windows and reduce their window scores to covered points by averaging. No image/attention/fusion repeat is required on the secondary streams.

Report unadjusted point precision/recall/F1 for each stream and **separately** a point-adjusted audit: if any thresholded predicted point intersects a labelled anomaly interval, fill that entire true interval as detected, leaving predictions outside intervals unchanged. This intentionally uses test labels in the scoring adjustment; never use it for tuning or as the headline. Report interval counts and alarmed-point counts. OPSSAT-AD remains fragment-level and receives no point adjustment. Neither benchmark supplies validated continuous wall-clock coverage for an alarms-per-day claim. Inherited SMAP/MSL test-scaling remains a limitation, not evidence of a clean deployment evaluation.

## I2 ECG

Read `scp_codes` safely as data. Retain diagnostic mappings where `diagnostic==1` in v1.0.3 `scp_statements.csv` and the record's likelihood is **>0**; set each mapped superclass to one. Drop records with no retained superclass and publish IDs/counts by official fold. Do not infer disease absence from an unmapped rhythm/form statement. Use 100 Hz, 10-second, 12-lead signals and all eligible records; confirm that the official folds are patient-disjoint and report it. The instructor's check on the v1.0.3 metadata: 21,799 records from 18,869 patients, none in more than one fold. This rule leaves **21,375 eligible records**: 17,073 in folds 1–8, 2,145 in fold 9 and 2,157 in fold 10. 424 records have no retained superclass, 13 of them only because their diagnostic statements carry likelihood 0. For the audit, 2,027 patients hold more than one eligible record (4,792 records).

The classical baseline is one-vs-rest regularised logistic regression on per-lead mean, std, min, max, quartiles, RMS, peak-to-peak amplitude and first-difference RMS, with training-only scaling; C in {0.1,1,10} is selected on validation. This is a simple multilead statistical baseline, not clinical-grade ECG delineation. Use identical multilabel targets and threshold rules for all systems.

For audit seeds **101–105**, randomly permute eligible **record IDs**, assign 80% train / 10% validation / 10% test (floor counts for train/validation), and retain whole records. Fit only the no-attention 1-D CNN for each audit, using training seed 22 and refitting scaling/thresholds within that audit. Report patient-ID intersections and the fraction of test records whose patient is in training. If an audit has no actual patient overlap, label it accordingly; do not manipulate it to force a larger gap. Fit official models and lock all choices **before** audit training; audit reuse of former official-test records must never feed back into the official headline. Five contrasts describe partition variability with a fixed official reference, not five independent estimates of causal leakage. Show all five values and their mean/range; no causal confidence interval is implied.

# Protocol Annex D7 — Battery

**Route and identities.** The three struct files, their sizes and the API route are on Card I3 (demonstrated at Revision D). The platform lists 140 cell tests across 135 distinct cell IDs; five cells continue from 2017-05-12 into 2017-06-30 and each is one physical cell. The [authors' repository](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation) supplies processing examples but states that access to its modelling code requires an academic licence. Students implement the declared elastic net themselves; no access to restricted author modelling code is required. Do not mistake repository code access for data access.

Freeze the usable cell pool **once**: a known cycle-life target, complete cycles through 100 and the required discharge-voltage samples. For a continuing cell, join its two records before applying this test. State the resulting selection and survivorship limitation. Never create a different test set at each horizon. Assign each physical cell to the batch in which its cycling began — for the five continuing cells, 2017-05-12. Within each batch, sort physical cell IDs by SHA-256 of `22|` plus the cell ID **in lower case** (for example `22|el150800460486`) and assign 60% train / 20% validation / 20% test, rounding train and validation down and leaving the remainder to test. This can be computed from the platform's cell listing and its `summary` series before any struct is downloaded (Card I3).

**The instructor's pre-issue run, 23 September 2026.** The listing gives 140 tests and 135 physical cells. Seven cells have no cycle-life target, because their batch notes say the test stopped before 80% of nominal capacity: 2017-05-12 channels 13, 19, 21, 22 and 31, and 2018-04-12 channels 33 and 41. The pool is therefore **128 cells** — 41, 43 and 44 by starting batch. All three structs were then parsed, and every pool cell has finite 1,000-point `Qdlin` discharge curves on the authors' `Vdlin` grid for every cycle from 2 to 100. The split is **75 train, 24 validation and 29 test** cells (24/8/9, 25/8/10 and 26/8/10 by batch), and **it is issued, not regenerated**: `I3_cell_split.csv`, SHA-256 `3054cf83e0bc1a140cfd09357a4af13182619186d5dc12da20a974aff4507ff1`, issued with the cards. Reproduce it in Week 1 and report any difference; where your run differs, the issued list governs. Two cells flagged in the batch notes stay in the pool because their required samples are present: 2018-04-12 channel 46 (noisy voltage profiles) and 2017-06-30 channel 10 (possibly defective; life 148 cycles). Name both in your readiness note. *(Corrected 23 September 2026. The raw `cellId` is upper case throughout 2017-05-12 and for six cells in the other two batches, and lower case otherwise, and this annex did not fix the case. Hashing upper-case IDs moves 64 of the 128 cells to a different partition, so the split was not reproducible as written.)*

**The target is issued, and this is how it was built (24 September 2026).** `I3_cycle_life_targets.csv` (SHA-256 `e9b53a78b462b008de0b33bc4540897de2914f27e97a09c85ae23dc4eae67127`) gives `cycle_life_target` for all 128 pool cells, with the rule used. End of life is **80% of the 1.1 Ah nominal capacity, 0.88 Ah**. Cycle positions are 0-based indices into the per-cycle discharge-capacity series that the platform listing carries for each test record (the "Discharge capacity vs cycle number" summary; it has two more entries than the struct's own summary for every record). The authors' `cycle_life` field follows **two different conventions**, and the target reproduces both exactly:

- **Rule A — 2017-05-12 (36 cells) and 2017-06-30 (43 cells):** the index of the first entry below 0.88 Ah. Reproduced for all 79 cells.
- **Rule B — 2018-04-12 (44 cells):** these tests stopped on reaching 0.88 Ah and their series never falls below it (minimum 0.8800–0.8817 Ah), so the field is the index of the final entry. Reproduced for all 44.
- **Rule C — the five continuing cells:** global cycle numbering continues the 2017-05-12 record, so the target is the number of cycles in the 2017-05-12 struct summary plus the Rule-A index in the 2017-06-30 series. This is exactly the authors' published join (their batch-1 `cycle_life` plus batch-2 `cycle_life` minus one): **1,434, 1,709, 1,852, 2,160 and 2,237** for `el150800464977`, `el150800464865`, `el150800460514`, `el150800460486` and `el150800460623`.

No duplicate or missing entry affects any crossing. Training-cell targets run 148 to 2,160 (mean 824.6 cycles, which is the mean-life floor); validation 457 to 2,237; test 438 to 1,852.

**Two `cycle_life` traps in the structs.** (1) In the 2017-06-30 struct, `cycle_life` for the five continuing cells counts only the cycles run in that batch — 209 to 1,061 — not the cell's life. *(Corrected 24 September 2026: this said the life was "roughly the sum of its two records (1,435 to 2,238)" and told you to "compute the target from the joined series" without saying how. The sum of the two fields overstates every one of the five by one cycle; the issued target uses the authors' join.)* (2) The 2017-05-12 struct gives a numeric `cycle_life` (879 to 906) for its five tests that stopped before 80%; those are censored run lengths, not lives. The 2018-04-12 struct marks its two such tests `NaN`. Neither field is a safe target without the batch notes. The 2017-05-12 struct also has no cycle 1, as its batch note says; the features above start at cycle 2.

Use ΔQ(V)=Q_k(V)−Q_2(V) at k=10 and 30; at k=100 use Q_100(V)−Q_10(V). Thus the 100-cycle case preserves the published endpoint idea while shorter horizons are explicitly **adapted baselines**. Use the authors' common voltage grid when present; otherwise interpolate to 100 common voltage points in the valid overlap of training-cell ranges only. No extrapolated future cycle. Extract log variance (with a declared epsilon), mean, minimum and maximum of ΔQ, and early capacity-trend slope fitted using only cycles ≤k. Fit elastic net on log cycle life; choose three fixed alpha values {0.001,0.01,0.1}, l1_ratio=0.5, training-only standardisation, validation RMSE selection; invert to cycles before evaluation. This is a bounded reproduction/adaptation, not a promise to duplicate published performance.

The 1-D CNN has a voltage-curve branch and a cycle-summary branch with Q-discharge, duration and temperature only where valid through k. Missing fields are handled by a training-fitted fill plus missing indicators, and their availability is reported. At the reference horizon, the 2-D CNN uses the cycle×voltage capacity surface; the attention variant attends over the cycle-summary branch. The fusion combines the elastic-net and no-attention 1-D predictions at 100 cycles. The mean-life floor is the same training-cell mean at all horizons because the cell pool is fixed.

Use 1,000 paired bootstrap draws of held-out cell IDs, seed 22, resampling the same IDs for both models and every horizon; report percentile intervals for RMSE and the paired difference. This quantifies uncertainty over these held-out cells, not independent-batch generalisation. If fewer than ten independent test cells survive, report individual-cell errors and consult the instructor before interpreting the crossover; do not present an unstable threshold as established.

# Protocol Annex D8 — Landslides: recovered scene groups

**Data and label.** Use the 3,799 competition-labelled development patches from the IBM/NASA mirror (Card I4-S), cast to float32. The mirror's 1,045 validation and test masks have no stated provenance — **established 24 September 2026 as a negative result: they are exactly `annotations/validation` (245) plus `annotations/test` (800), and neither the README nor any of the six upload commits of 22 October 2024 says where they came from** — and they appear in no marked result. A patch is positive if its mask has at least one pixel equal to 1. **Degenerate patches — band 14 constant and slope identically zero — number 114**, all of them negative. They take part in grouping — their seams are near-constant, so they are placed by raster contiguity (rule 4 below) — and are then excluded from every partition, marked `excluded_degenerate` in the issued split file. *(Corrected 24 September 2026: this said they were excluded from grouping, which the reported group sizes contradicted: 113 of them are counted in S1.)*

**Recovering scene groups — the reference procedure, reconciled with the executed code on 24 September 2026.** The issued files are produced by `i4s_grouping_and_split.py`, which is issued with the cards; where this prose and the script ever disagree, the script and its output files govern. **The chain is runnable from the bundle.** `i4s_extract_seams.py` reads the 3,799 patches and masks and writes the script's three inputs — `seams.bin` (band-14 left, right, top and bottom edges, float32), `pos.bin` (landslide pixels per patch, int32) and `stats.bin` (band-14 min and max, slope max, band-14 range, float32), slot 0 unused. The instructor's copies of those three files are issued as `reference_inputs/`, so you can run the grouping script at once and then check your own extraction against them byte for byte. *(Added 25 September 2026. The extraction was checked on eight patches from the pinned mirror revision `4b291891…1435`, including 2460, 2500 and 3034: identical bytes; and the grouping script, run inside the bundle on `reference_inputs/`, reproduces all four issued CSVs exactly.)* For each patch take band 14 and record four edge vectors of 128 values: left and right columns, top and bottom rows. The distance between two seams is the maximum absolute difference over the 128 pixels (Chebyshev). Use vectorised code or a nearest-neighbour index, not a Python double loop.

1. **Informative seams only.** A seam is *near-constant* if its maximum minus minimum is below 0.01 in the normalised band 14. Near-constant seams take no part in matching **on either side of a link**: a near-constant right or bottom edge proposes no link, and a near-constant left or top edge receives none. Counts: right 153, bottom 149, left 158, top 172 (of which exactly constant: 132, 139, 140, 162). The reason is a trap: two near-constant seams can sit at distance 0, nearer than a true neighbour, which differs by about 0.018 because adjacent tiles share no pixel column.
2. **Reciprocal nearest neighbours.** For a horizontal link *i → j*: *j*'s left edge is the nearest informative left edge to *i*'s right edge, **and** *i*'s right edge is the nearest informative right edge to *j*'s left edge, **and** the distance is below τ. Exact ties go to the lower patch ID. Vertical links (bottom of *i* to top of *j*) follow the same rule. Scene groups are the connected components over both directions.
3. **Threshold.** τ is set **before grouping** from the histogram of best-match distances, and the histogram is published. **τ = 0.05.** The true-neighbour mode lies at 0.015–0.020 and is exhausted by 0.05; a random pair falls below 0.05 only 0.31% of the time, against a random-pair median of 1.3095. The four groups are identical for every τ from 0.04 to 0.10; at 0.03 S1 fragments.
4. **Unlinked patches, by raster contiguity.** A patch left with no link joins the group of its lower index neighbour, taking IDs in ascending order, unless the very next ID is already linked into a different group, in which case it is left unassigned. The tiles were written in scan order, which the links themselves establish. This attaches **129 of 130** unlinked patches; **patch 3034**, the last before S2 begins, is left unassigned, and it is degenerate in any case.
5. **Degenerate patches take part in grouping and are excluded afterwards.** The 114 degenerate patches have near-constant seams, so all of them are unlinked and are placed by rule 4 — 113 in S1, plus patch 3034. They are then excluded from every partition (`excluded_degenerate` in the split file). The group sizes below therefore include them.
6. **Coordinates.** Within a group whose lowest ID is *f* and dominant vertical link offset is *w*, patch *p* sits at column (*p* − *f*) mod *w*, row ⌊(*p* − *f*) / *w*⌋. Walking the links from *f* gives the same coordinate for every linked patch except one false horizontal link between patches 1804 and 1887 (both in S1), which conflicts and is ignored; the arithmetic coordinates are the issued ones.

**🔴 Corrected 24 September 2026 — the issued grouping and split were wrong, and the files are reissued.** The executed pass differed from its own prose in two ways, and both mattered. (a) Its "mutual" rule was collision resolution — *i → j* was kept if, among patches whose best partner was *j*, *i* was the closest — which is not reciprocal nearest neighbours, and it gated only the proposing seam. Patch **2460**, whose four seams are all exactly constant, therefore received a link from S2's patch 3170 at distance 0.034 and was put in S2, although it lies at column 40, row 59 of S1 — inside S1's test block. (b) Grid coordinates were assigned by enumerating each group's patches in ascending order, so removing 2460 from S1 shifted the coordinates of the **573 patches from 2461 to 3033** by one position. In rows 60–73 the true column 0 was labelled column 40, so **15 test-block patches were edge-adjacent to training patches**, and 2460 put a test-block neighbour into F1's transfer training set. The reissued files have no train–test or test–transfer edge adjacency on true positions (checked). The group count and S1's status as the only target are unchanged; S1 gains patch 2460, S2 loses it, S2's grid becomes an exact 15 × 10, and the S1 block counts move by a few patches. Earlier prose also claimed the grouping was unchanged for τ from 0.03 to 0.07; under the executed rule that was true, under the corrected rule it holds from 0.04.

**Publish:** τ and the histogram; the group of every patch; the number of groups; patches, positive patches and negative patches per group; the number of horizontal and vertical links; the counts of near-constant seams and degenerate patches; and any patch you place differently. **The reference pass gives 3,490 horizontal and 3,487 vertical reciprocal links, and four groups** — S1 3,033 (IDs 1–3033), S4 494 (3306–3799), S2 150 (3035–3184), S3 121 (3185–3305); every group is a contiguous ID range — issued as `Landslide4Sense_scene_groups.csv` (SHA-256 `49c9fb5f…7cf8`) and `Landslide4Sense_scene_group_summary.csv` (`0b9e0e19…4a9a`).

**The row strides are 41, 15, 11 and 26.** Each group has exactly one dominant stride, which is the independent check that the four components are four tilings and not one tiling cut in four. S4's 468 vertical links are all exact. **Why the D1 probe missed the vertical links:** its vertical search covered patches 1–24, which all lie in S1, and a tile's lower neighbour in S1 is 41 IDs further on, outside that window. *(Corrected 24 September 2026: this said all four strides were "beyond the 24 indices that probe searched"; 15 and 11 are not, and the probe never reached S2 or S3.)* If your own pass finds no vertical link, you have a bug.

**Grid sizes.** S1 41 × 74 with a partial last row (3,033 of 3,034 cells), S2 15 × 10, S3 11 × 11, S4 26 × 19 — the last three exactly rectangular.

**🔴 Fold-eligible groups — the rule is now explicit.** A **target** group carries the within-group reference as well as the transfer test, and both are scored on the same test patches, so a target must survive the guarded three-block split below with **at least 20 positive and 20 negative non-degenerate patches in its test block** — the D1 group minimum applied to the block that is actually scored. **Only S1 qualifies.** Under the same rule S2's test block is 40 patches (29 / 11), S3's 33 (17 / 16) and S4's 114 (3 / 111): S4's positives thin out toward its eastern columns, and 80 of its 102 positives lie in rows 4–11. **The issued folds are F1 (target S1, both protocols) and F2–F4 (whole-scene transfer onto S2, S3 and S4), as tabulated on Card I4-S.** *(Corrected 24 September 2026. The earlier text said 89 of S4's positives lie in rows 4–11 — it is 80 — and that S2 and S3 would leave test blocks of "about eleven patches"; under the pinned rule they leave 40 and 33. The conclusion stands, and it now rests on a stated threshold rather than on those figures.)*

**Within-group reference, target group S1.** **The guarded three-block rule:** with *W* grid columns, training takes the first ⌊0.6(*W* − 2)⌋ columns, then one guard column, validation the next ⌊0.2(*W* − 2)⌋ columns, then one guard column, and test the rest; each guard column is discarded whole, one column at each of the two boundaries. For S1 (*W* = 41) that is **training columns 0–22, guard 23, validation 24–30, guard 31, test 32–40**. After removing the 113 degenerate patches: **train 1,702 (1,277 pos / 425 neg), validation 507 (346 / 161), test 570 (210 / 360)**, with 141 patches dropped in the guards. The within-group model trains and selects on S1's training and validation blocks only. *(Corrected 24 September 2026: previously train 1,702 (1,282 / 420), validation 500, test 578 and 139 guard patches, on the shifted coordinates; and the parenthetical general rule said "a whole guard column on either side of each boundary", which reads as two per boundary. It is one.)*

**Transfer protocol.** In **F1**, test on S1's test block, validate on **S3**, train on **S2 + S4** (644 patches). No patch of S1 enters training or model selection. In **F2–F4** the test set is the whole of the target scene and there is no within-group reference: F2 tests on S2 (train S1 + S4, validate S3), F3 on S3 (train S1 + S2, validate S4), F4 on S4 (train S1 + S3, validate S2). **A fold's own scene never appears in its training or validation set.**

**Research fits.** In every fold and every protocol available in it, fit the small 2-D CNN twice at the same budget: (i) the twelve spectral bands, and (ii) those bands plus slope and DEM. Fit the random-forest baseline and the majority floor the same way. Demonstrate the 1-D spectral-signature model, the band-attention variant and the fusion only on **F1's transfer protocol with 14 bands**. For the 1-D model, use 256 regularly spaced valid pixels per patch, average their predictions to patch level and keep all pixels of a patch together. **That is ten 2-D fits — F1 two protocols × two band conditions, F2–F4 one protocol × two band conditions — plus two, so twelve neural fits.** *(Corrected 24 September 2026: "4F + 2" assumed a within-group reference in all four folds and gave 18.)*

**Band scaling.** The mirror's values are globally rescaled (Card I4-S). Compute NDVI or a bare-soil index only if every band involved shares one documented scale; otherwise omit it and say why. A random forest needs no physical units for slope; a hand-set slope threshold does.

**Interpretation.** Within-group and transfer models see different and differently sized training populations — **1,702 patches inside S1 against 644 in S2 + S4** — so the drop is a descriptive contrast on matched test patches, not a pure measure of domain shift. The four scenes also differ sharply in prevalence: S2 is 84% positive, S4 only 21%, so a transfer number is as much about the target's base rate as about the model. Report per-scene support beside every per-scene result. Name the unit as a recovered scene group in every claim. Never replace the question with a random-patch split.

# Protocol Annex D8a — Bird labels, windows and SNR

Before issue the instructor freezes the taxonomy map, the species eligible under the window rule below, their Powdermill window counts, **the 15 selected species and their 900 source recordings** (below); you reproduce them. **A soundscape recording is one of the four dawn recordings (`Recording_1` to `Recording_4`, one per date), not a five-minute segment file.** Recording 3 has a single segment. Use 15 species with ≥50 usable source recordings each (on availability all 48 clear ≥50 A–C recordings; Card I5). Count usable **recordings**, not windows. A species is eligible only with at least ten positive Powdermill windows across at least two soundscape recordings, which is what a descriptive per-species estimate needs; report day/recorder concentration and avoid independence claims from adjacent windows. These are course acceptance minima, not confidence guarantees.

**The instructor's pre-issue count, 23 September 2026.** The v2 annotation archive (SHA-256 `7edf8a0e…44cb`) holds 77 segment files — 36, 14, 1 and 26 across the four recordings — and 16,052 annotations over 48 species codes. All 77 mp3 segments are 300.06 s long, giving **4,620 complete 5-second windows**; 4,448 contain at least one annotated species. The README states that all identifiable vocalisations other than short chips were annotated, and no window is marked incomplete, so every window is scored; the annotation universe excludes chips and unidentifiable sounds. **22 species are eligible:**

| Code | Species | Positive windows | Recordings (of 4) | Largest single-recording share |
|---|---|---|---|---|
| EATO | Eastern towhee | 3,549 | 4 | 47% |
| WOTH | Wood thrush | 1,261 | 3 | 51% |
| BTNW | Black-throated green warbler | 1,145 | 2 | 81% |
| AMCR | American crow | 1,097 | 3 | 44% |
| NOCA | Northern cardinal | 1,076 | 4 | 64% |
| BCCH | Black-capped chickadee | 874 | 4 | 38% |
| TUTI | Tufted titmouse | 737 | 3 | 84% |
| OVEN | Ovenbird | 584 | 3 | 81% |
| COYE | Common yellowthroat | 439 | 2 | 94% |
| SCTA | Scarlet tanager | 387 | 2 | 85% |
| BLJA | Blue jay | 330 | 3 | 88% |
| BAWW | Black-and-white warbler | 180 | 3 | 57% |
| BHCO | Brown-headed cowbird | 177 | 3 | 64% |
| BHVI | Blue-headed vireo | 144 | 2 | 64% |
| RBWO | Red-bellied woodpecker | 110 | 3 | 49% |
| HOWA | Hooded warbler | 107 | 2 | 97% |
| NOFL | Northern flicker | 100 | 3 | 57% |
| LOWA | Louisiana waterthrush | 55 | 2 | 69% |
| AMGO | American goldfinch | 39 | 2 | 64% |
| WITU | Wild turkey | 19 | 3 | 63% |
| WBNU | White-breasted nuthatch | 19 | 2 | 74% |
| DOWO | Downy woodpecker | 11 | 2 | 82% |

Eight eligible species have more than 80% of their windows in one recording; report that concentration. Five well-supported species are ineligible because all their windows fall in one recording: REVI 363, AMRE 315, KEWA 260, BGGN 189 and HETH 138. Reading "recording" as segment file would have made 33 species eligible. The per-species table for all 48 is issued with the cards as `powdermill_window_support.csv`.

**Selected species and source recordings — frozen before issue, 24 September 2026.** The card's 15 species are the 15 eligible species with the most positive Powdermill windows, ties broken by code: EATO, WOTH, BTNW, AMCR, NOCA, BCCH, TUTI, OVEN, COYE, SCTA, BLJA, BAWW, BHCO, BHVI, RBWO. **Reserves, in order:** HOWA, NOFL, LOWA, AMGO, WBNU, WITU, DOWO. A source recording is **usable** when it is quality A–C, its foreground species is the selected species (a recording labelled with a subspecies counts), none of the other 14 selected species appears in its background ("also") metadata, and it is at least 5 seconds long, so that it yields one complete window. The instructor's inventory, read from xeno-canto's own search pages on 24 September 2026 (the A–C totals reproduce the 20 September availability figures for all 22 species, BLJA having gained one recording, 566 → 567), gives these usable counts: EATO 313, WOTH 276, BTNW 205, AMCR 453, NOCA 747, BCCH 413, TUTI 274, OVEN 304, COYE 661, SCTA 163, BLJA 443, BAWW 268, BHCO 279, BHVI 219, RBWO 164 — **the smallest is 163, against the minimum of 50**. Within each species, usable recordings are sorted by the SHA-256 hex digest of `22|XC<number>` (for example `22|XC486218`), the first 60 are taken, and the first 36 / next 12 / last 12 in that order are train / validation / test. **Issued as `I5_source_selection.csv`**: 900 recordings with species, partition, hash rank, length, quality, licence and recordist. Recordists are not held apart: in every species between two and seven test-partition recordists also appear in training or validation, so the focal split is by recording, not by recordist, and you report that overlap. The selected recordings carry eight Creative Commons variants — 665 BY-NC-SA 4.0, 75 BY-NC-SA 3.0, 85 BY-NC-ND 2.5, 41 BY-NC-ND 4.0, 17 BY-NC-ND 3.0, 9 BY-SA 3.0, 7 BY-SA 4.0 and one CC0 — so record the licence of each file you use; the no-derivatives licences permit analysis but not redistribution of mixtures.

**Acquisition demonstrated.** One test-partition recording per selected species (15 files) was downloaded through the public download link and decoded with soundfile 0.14.0 (libsndfile 1.2.2): 15 of 15 decoded; thirteen MP3 and two WAV; 16, 32, 44.1 and 48 kHz; mono and stereo; 70 complete 5-second windows in their first 30 seconds, none silent under the RMS rule. The server returns neither a content length nor a byte range, so each file is transferred whole: 80,966,563 bytes for the fifteen, with one 48 kHz stereo float WAV of 64,545,530 bytes. Transfer for all 900 is therefore not bounded by the 30-second cap; trim and resample each file on arrival, keep the retained windows (at most six 5-second windows per recording at 22.05 kHz, about 2.6 MB as float32), and report the transferred total.

**If the selection cannot be filled — the action is fixed, not left to the group.** (1) A selected recording that is withdrawn, fails to download or fails to decode is replaced by the next usable recording of the same species in hash order, placed in the same partition; log every replacement. A replacement keeps the partition of the recording it replaces, never takes an ID already used in any partition, and an already downloaded recording keeps its partition. (2) **If a selected species cannot be refilled to 60** — because fewer than 60 usable recordings remain once withdrawn or failed ones are removed — stop and report it in the readiness note; the instructor reissues the selection by Tuesday 6 October. With **50–59** usable recordings, the instructor either replaces the species with the first reserve that can supply 60, recomputing the background filter for the new set of 15, or approves the available *n* with the fixed partition ⌊0.6*n*⌋ / ⌊0.2*n*⌋ / remainder in the same hash order. With **fewer than 50**, the species is replaced by the first reserve that can supply 60. Students never change the species universe or the partition sizes themselves. *(Corrected 25 September 2026: the rule covered only the below-50 case, so a species left with 50–59 recordings could follow neither the 60-recording instruction nor the replacement branch.)* (3) If fewer than 15 species can be filled from the 22, the card runs on the species that can, with the reduced universe named in every claim; that is a scope reduction on measured evidence and carries no penalty. *(Added 24 September 2026. The card previously said only "hash-order recording IDs" and "use 15 species with ≥50 usable source recordings", and left the usable count and the choice of species to Week 1.)*

**Source selection and weak targets.** Keep quality A–C focal recordings for which a selected species is the main species and no other selected species is listed in background metadata; exclude unknown main species and corrupt audio. Empty background metadata is **not proof of absence**. Order recording IDs within main species by the SHA-256 of `22|XC<number>`, keep the first 60 usable, and assign 36 / 12 / 12 train/validation/test before windowing, exactly as issued in `I5_source_selection.csv`. Document recordist/location overlap. Retain at most the first 30 seconds; resample to **22.05 kHz mono** with anti-aliasing; use **5-second windows, hop 5 seconds**, dropping trailing incomplete windows. Reject only silent/invalid windows by a fixed numerical criterion (RMS<10⁻⁶ in floating audio scaled to [−1,1]); do not screen according to model confidence.

Each retained focal window inherits the recording's main-species positive label and treats other selected species as assumed negatives for the **weak-label training/evaluation convention**. Some windows may lack the main species or contain unlisted birds. Use BCE/sigmoid outputs and label all focal metrics **weak-label metrics**. Report a small, fixed spot-check of ten hash-selected source recordings to describe obvious label limitations; this is not a new annotation dataset or permission to revise test labels opportunistically. No claim that focal-window truth has become strong annotation is allowed.

**Target labels.** On every complete Powdermill window, a species is positive if an annotation for it has **strictly positive temporal overlap** with the window; otherwise it is zero within the documented annotation universe. Multiple positives and all-zero selected-species targets are permitted. Windows marked by source metadata as incompletely annotated are excluded; if completeness cannot be established, stop and consult before scoring those windows. Do not equate an all-zero selected-species target with silence or absence of all birds. Use all valid windows; no model-based filtering. Strong annotations fix evaluation targets, never source thresholds or augmentation choices.

**Thresholds and claims.** Fit class thresholds on weak source validation only and keep them for clean focal, every noisy focal condition and Powdermill. The same metric names make the output contract consistent, but their truth quality differs: the measured focal–soundscape gap combines acoustics, prevalence and **annotation regime**, and is not a clean estimate of domain shift alone. The SNR curve is paired degradation against fixed weak targets. Negative findings and these limitations are reportable results.

**Noise mixing.** Use ≤300 `hasbird==0` freefield1010 clips from the frozen inventory, spot-checking for audible birds. Fetch them individually from the archive.org member links (Card I5), not by transferring the 5.77 GB archive; the temporary space this needs is the clips themselves, at most about 265 MB. Resample identically. Choose a fixed noise clip and 5-second offset per focal test window with seed 22; reuse them across all models/SNRs. Centre clean signal x and noise n. With nonzero RMS values, set a=RMS(x)/(RMS(n)·10^(SNR/20)) and mix x+a n at **−5, 0, 5, 10, 20 dB**. Do not peak-normalise each mixture independently: choose one shared gain per clean-window/noise pair that keeps the clean signal and **all five mixtures** within [−0.99,0.99], and apply that same gain to every member of the pair's comparison. This avoids clipping while preserving SNR and relative clean-signal level. Log silent-pair exclusions and actual achieved SNR before the common gain.

The waveform and log-mel CNNs, plus the RF on MFCC/spectral summaries, are evaluated on identical clean/noisy windows. Use 64 mel bins, 1,024-sample FFT and 256-sample hop; training-only feature scaling. No model is retrained at each SNR. Powdermill is never a noise source. Noise augmentation as mitigation remains optional. Source acquisition terms apply **before use** and again before redistribution; API keys never enter submitted files.

# Protocol Annex D9 — BreizhCrops

Use 2017 **frh01+frh02 train, frh03 validation, frh04 test**, both processing levels. The [maintained repository](https://github.com/dl4sits/BreizhCrops) identifies frh04 as evaluation data; this annex explicitly fixes the course's full assignment and subset. The package is pinned at GitHub commit `6de796e` (11 May 2022, the latest; PyPI 0.0.4.1), with `classmapping.csv` SHA-256 `e850f71d…42e9`: nine class IDs over 23 crop codes. The index files differ in layout between regions and levels (some carry a UTF-8 byte-order mark or a leading unnamed column), so read them by column name. Use the nine labels defined by that mapping; do not hand-transcribe crop names from a secondary list or use `code_cultu` as an input feature. Read the crop code from `label` at L1C and from `code_cultu` at L2A.

**Acquisition, one region at a time.** Obtain one region's L1C and L2A files, build that region's paired inventory, copy the selected parcels' complete series into a compact store, then delete the region files before the next region. Peak retained data is one region's two files plus one archive, plus the compact store: at worst 4,204,595,712 bytes with the package loader (frh01, measured 24 September 2026). Streaming the `.h5` out of the archive without keeping it, as the instructor's scripts do, lowers this to the frh01 pair itself, 3,546,895,864 bytes. Report transferred, peak retained and final retained bytes.

Join L1C/L2A by parcel ID and exact observation date, requiring matching labels and year. Keep only finite common-band observations in **B2,B3,B4,B5,B6,B7,B8,B8A,B11,B12** order. At L1C these are `.h5` columns 4, 5, 6, 7, 8, 9, 10, 11, 2 and 3, not the `SELECTED_BANDS` positions (Card I6). At a duplicate date choose the first stable source-row ID at each level and record duplicates. Require ≥12 matched distinct dates per parcel; exclude failures before any model scores. Use dates common to both levels and **no processing-level-specific cloud filter in the core**; log cloud flags descriptively. This controls availability/filtering but does not imply identical atmospheric information.

From ≥45 common dates choose 45 evenly spaced indices in chronological order. From 12–44 dates retain all, pad at the end with zero after training-only scaling and add a validity mask. **Never randomly redraw dates**, never repeat observations as if independently measured. Store paired row indices and parcel IDs once and reuse them for every model and seed. Image CNN input is time×band with a separate validity channel; temporal pooling excludes padding. Class/parcel/region IDs are never model features.

For training, order eligible paired parcel IDs by the SHA-256 hex digest of `22|<parcel id>` within each class across frh01/frh02, retaining at most 2,000 per class (18,000 total). For validation and test, order all eligible paired IDs the same way, independently of labels, and retain at most 4,500 in each region. *(Pinned 24 September 2026: "hash-order" did not name the hash.)* The instructor's run is issued as `I6_parcel_selection.csv` (SHA-256 `f85047a0…609f`): 13,317 training parcels (8,100 from frh01, 5,217 from frh02), 4,500 validation and 4,500 test. Do not rebalance held-out class prevalence. Report actual supported counts, exclusions and source-region contribution. No parcel may occur in two partitions. A missing test class is reported under D0. Absence of a training class, or inadequate pairing, is resolved before issue; if it is found in Week 1, stop and consult.

Fit the same small temporal 1-D CNN, time-band image CNN and RF at each level. RF uses temporal band-wise means/std/min/max and the same validity mask to exclude padding. Neural systems share the D0 time allowance and at most 100,000 trainable parameters; report actual counts rather than claiming exact parameter equality. Fit scaling independently on each level's **same training parcel/date set**; this processing choice is reported. Repeat only the no-attention **L2A 1-D CNN** at seeds 22,23,24 on the identical subset. Other fits use seed 22; the two additional reference seeds are not an ensemble. Attention/fusion are L2A seed-22 demonstrations. Report three-seed mean/std only for that reference, and single-run limitations for the paired level contrasts.

If common dates or band units cannot be validated, do not announce that atmospheric correction was isolated: narrow the claim to a comparison of processing pipelines, as Card I6 says. The paired-parcel match rate was measured on 24 September 2026 (Card I6); the pipeline-comparison fallback remains the rule if your own reproduction falls short of it. No different region split or extra early-season experiment is required.
