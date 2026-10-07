# 22AIE304 Deep Learning — End-Semester Project

**Groups of 3–4 · 8 weeks · Week 1 begins Monday 28 September 2026 · Week 8 dates to be announced**
**Revision D1 · 21 September 2026 · Amendment 1 to Revision D · issued with your assignment card and your dataset manifest**

## 1. What this project is

You will take a real scientific or engineering problem, build a deep learning solution for it, and then do something most course projects skip: **test whether your result actually holds up**.

That last part is the point. Getting a model to produce an impressive headline metric is not difficult and is not what is being assessed. What is assessed is whether you can show that the number **means** something — that it survives a proper split, that it is honestly compared against a sensible non-deep-learning baseline, and that you have tested what happens when the data shifts.

Note the wording: **compared against**, not *beats*. In several of these projects the classical method is genuinely competitive, and demonstrating that rigorously is a complete and fully-credited result. See §9.

Every project uses a **public dataset** and is designed to run on a **normal laptop CPU**. No GPU is required or expected. That sizing is our responsibility, not yours: if the approved subset or the required runs turn out not to fit on the machines you actually have, **come and tell us and we will cut the scope**. Reducing the number of conditions, the subset size or the model size for a measured reason costs you no marks. Nobody is expected to obtain a GPU.

**The required components are deliberately lightweight.** You are not expected to run extensive hyperparameter searches, train large models, or exhaust your dataset. A small, correct, well-understood experiment beats a large rushed one. Every project also has **optional extensions** — attempt them only once the core is solid.

**One thing to know about the pack you are holding.** Six dataset checks were run on our side between Revisions C and D, and three of them contradicted what we had previously written down. A benchmark we call a clean out-of-domain test set turns out to have a contaminated split; a project's stated split unit turns out not to exist in the released data; and a warning we printed about another benchmark's split turned out to be backwards. All three are recorded in the open, in your card and your manifest, rather than quietly fixed. **Amendment D1** then completed the protocol details your card had referred to without stating — they are now in the Protocol Annexes at the end of the assignment cards — and corrected one card: A1's Paderborn training bearings had included no inner-ring fault. **Before release we walked the data routes again (23 September 2026), and that found more.** A published train/test split leaks crops of one photograph across it (Track B). A data link began serving a different product version (Track C). One species was listed under the wrong name (I5). Two date ranges were wrong, and one original download has gone (Track D, I1). One file stores its bands in a different order from its own package's band list, and a small region recommended for development turned out to lie inside the test region (I6). Each is corrected visibly in your card and manifest; where a fix needed a frozen split or file, that file comes with your card. **A final check before release (24 September 2026) found more, in our own work this time.** The first issued landslide split put one test tile in the wrong scene and shifted the grid positions of 573 others, so it has been rebuilt and reissued (I4-S). The battery cards now come with the cycle-life target as a file, because the source's own field follows two conventions (I3). The bird card's 15 species and 900 source recordings are now fixed rather than chosen (I5). The rule about derived samples now names the two card protocols that deliberately split one recording or one scene, and the time budget is stated as elapsed hours (§4, §8). **If you find something similar, report it — that is a correct result and it is credited.**

## 2. Timeline

**There are eight assessed weeks in total, starting Monday 28 September 2026.** Weeks run Monday to Friday; Saturdays and Sundays are holidays. Your card arrives on Saturday 26 September, the weekend before Week 1; there is no Week 0. Every deadline falls on the Friday that ends its week, and Weeks 1–7 end with the results freeze on Friday 13 November. *(Changed 26 September 2026: weeks were entered as Saturday to Friday, which put the weekend inside each week. They now follow the working week, Monday to Friday; Saturdays and Sundays are holidays. **No deadline moves** — every deadline stays on the same Friday — and your card still arrives on Saturday 26 September, the weekend before Week 1.)* **Week 8 is not yet fixed:** project presentations across all courses begin on or after Wednesday 18 November, and the 22AIE304 presentation schedule, with the report and repository deadlines, will be announced close to 13 November. The full list of dates is in the release calendar at the top of your assignment cards. *(Changed 26 September 2026: Week 8 was entered as Saturday 14 – Friday 20 November. Project presentations across all courses begin on or after Wednesday 18 November, and the 22AIE304 slot within them is not yet known, so the Week-8 dates are withdrawn rather than guessed. Weeks 1–7 and every deadline up to the results freeze are unchanged.)*

| When | What |
|---|---|
| **Already done** | Groups formed, track preferences and individual-project applications submitted, and **project titles allocated**. |
| **The day your card arrives** *(by Saturday 26 September 2026)* | Read your card and the Protocol Annexes behind it. If your project needs a registered account or an API key, **register the same day** — it has to work before your readiness note is due, and that is at most six days later. |
| **Week 1** *(Monday 28 September – Friday 2 October)* | Kickoff. **Dataset readiness note due Friday 2 October** — see §8. Reassignment, if it is needed, also happens inside Week 1. |

**Phases and deliverables**

| Phase | What you do | Due at the end |
|---|---|---|
| **Weeks 1–2** | Readiness note; literature (**≥10 references, ≥4 domain-specific**, not deep-learning papers); data and EDA; written split protocol; non-DL baseline | 2-page proposal + baseline numbers + your split-ID files. The reference list may be attached separately and does not have to fit inside the two pages |
| **Weeks 3–5** | 1-D model → 2-D model → attention with its ablation → **your two-model fusion** | Mid-project demo: every required component running end to end, plus **at least one preliminary run of your novelty experiment** |
| **Weeks 6–7** | Your two core experiments; error analysis | Results freeze at the end of Week 7. No new experiments after that point |
| **Week 8** | Writing up, cleaning the repository, presenting | 4–6 page report, reproducible repository, presentation and individual defense |

**Who checks what.** Before your card is issued, the instructor confirms a feasible data route and the support it needs. **Within the first five working days of Week 1 — Monday 28 September to Friday 2 October — you reproduce the acquisition, counts and splits independently.** *(Corrected at D1: earlier issues said the allocation date was on your card. No card carried one; the dates are in the release calendar, and they were entered on 24 September 2026. Earlier drafts also put gated-account registration in a window between the allocation notice and the examinations. For you that window has passed — the titles were allocated first and the examinations are over — so registration is now the day your card arrives.)*

The Week-5 preliminary novelty run exists so that a missing label, an unavailable metric or an impossible split is discovered in Week 5 rather than Week 6.

**Report format.** 4–6 pages for the main body; references and a reproducibility appendix do not count toward it. Use an IEEE template if one is supplied, or plain formatting — **formatting is not graded** (§9).

**Working practice.** Give every required component a **named owner and a named reviewer**, and rotate so nobody reviews only their own work. The reviewer must be able to explain that component in the defense. Groups that silo one component per member arrive at Week 8 with no member who understands the whole project, which is exactly what the defense tests.

**Week 8 presentations — planned format; the schedule is not yet fixed.** Each shared track is planned to get one 45-minute block — three presentations plus a joint discussion of what the three questions together reveal about the dataset. The individual projects present separately. The format may be adjusted when the schedule is announced.

## 3. How projects are allocated

**Fifteen groups work in five shared tracks** (3 groups per track). The three groups in a track use the **same dataset** and jointly build the download, preprocessing and baseline **code**, then each group investigates a **different research question**. You share the plumbing; you do not share the science.

**You share code, not necessarily a split.** In two tracks the three questions legitimately require different split protocols, so there is no single shared baseline *number* — there is one baseline **per approved protocol**. When the three of you compare results in Week 7, compare only runs on an identical protocol and configuration. A difference there points at a bug; a difference across protocols does not, and small differences from nondeterminism are expected. Your assignment card states which protocol is yours.

**Your repository must stand alone.** You may start from your track's shared download and baseline scripts, but by submission your repository must contain a **complete, independently executable pipeline**. You may not depend on another group's code. The baseline mark is awarded to each group individually, on your own independent reproduction of it — not once to the track.

**Six groups take individual projects.** These are standalone — you build everything yourself, including the pipeline the shared-track groups split three ways. They are more work, and they go to groups who apply for them (§6).

## 4. What every project must deliver

Regardless of which project you get:

- **A split protocol, written down and justified before you train anything.** For most projects a random split is *wrong* — you will need to split by patient, by recording, by bearing, by leaf, by cell, by lot, by region, by recovered scene group or by time. Getting this wrong invalidates everything downstream.

- **Ask one question of every dataset before you split it: are any of these samples derived from a common original?** Augmented copies, multiple photographs of one physical object, several crops from one image, overlapping windows cut from one recording, adjacent tiles cut from one scene. **Use the independent unit appropriate to the claim you make.** Duplicate or augmented views and overlapping raw support must never cross partitions. This single check would have caught most of the published results these projects are auditing.

  **Two approved within-unit protocols, and what they do not show.** The guarded within-recording blocks of Track A (Annex D1) and the guarded within-scene reference of I4-S (Annex D8) deliberately put separated, non-overlapping parts of one recording or one scene on different sides of a split, with discarded guard bands between them. They are approved protocols, not leakage: follow their issued boundaries and guards exactly. They do **not** establish unseen-recording or unseen-scene generalisation, so do not claim it from them. Where physical-object grouping is incomplete in the release — PlantVillage's leaf map is missing or partial for 13 of its 38 classes (Annex D2) — report the grouping you had and the resulting limitation; a group there may be one photograph rather than one leaf. *(Corrected 24 September 2026. This rule used to say that derived samples "must stay together on one side of the split" without exception, which the Track A and I4-S cards themselves require you to break. A card cannot waive common policy, so the policy now names those two protocols. A3's deliberately overlapping audit run is a separate matter: it is an audit control, labelled as such, never used to select the valid model, and exempt from the leakage penalty (§9). That exemption does not extend to ordinary train/test leakage.)*

- **And a second question: does the split the dataset ships actually respect that?** A published split is not automatically a correct one. One of the benchmarks in this pack ships a train/test split with byte-identical photographs on both sides, eight of which carry two different labels. Check before you trust.

- **A non-deep-learning baseline** on exactly the same split. Persistence, a classical signal-processing method, a random forest — whatever your field actually uses.

- **A 1-D/sequential model and a 2-D/spatial model**, where each is scientifically meaningful for your data. For signal projects the 2-D model is usually a time–frequency image (spectrogram, scalogram). For image projects the 1-D model should be a *physically justified* profile — a radial intensity profile, a spectral signature, a cross-section along a meaningful axis — **not an arbitrary re-encoding invented to tick a box**. If you can show with evidence that no meaningful 1-D representation exists for your data, say so; see the alternatives rule in §9.

- **One attention module**, with an ablation showing what it changed.

- **A two-model fusion**, combining the two models **named on your assignment card**, with any fusion weights fixed on validation only. This counts as your ensemble; **nothing further is required** — no test-time augmentation, no stacking, no seed ensemble, no third model. Note what this is *not*: a comparison between two models is not a fusion, and pooling window-level predictions from a single model is an aggregation choice, not a fusion.

- **Your assigned research question**, with its two required experiments.

- **Metrics your field actually uses.** On imbalanced data, plain accuracy is not acceptable as a headline number.

- **Reproducible code** — fixed seeds, pinned `requirements.txt`, an acquisition step (see §12), and a single command in one of two named modes (§12).

- **Transferred bytes and retained working bytes reported separately**, wherever your source ships more than you keep. Several projects in this pack transfer an archive far larger than the subset they use, and two of them have had their scope changed by that number.

- **A written report and an oral defense** in which *every* member can explain the whole project.

**How much has to run, and how many times**

Your card lists exactly two core experiments. To stop that turning into model × condition × split × repeat:

**Demonstrate the required representations, the attention ablation and the named fusion on your card's reference setting — once. Repeat only the model–condition combinations your card lists under the two core experiments.** Annex D0 of the assignment cards gives your reference setting, the number of training runs your card requires and the training budget; Annexes D1–D9 give the protocol details for each track. Where a track or project summary in §5 or §6 suggests an extra sequential model or an extra architecture that your card does not list, it is optional.

**Parameter matching and time matching are two separate comparisons, not one condition.** A classical method has no comparable neural parameter count and does not need an artificial one. A frozen pretrained backbone hides both its total parameter count and its feature-extraction cost, so report **total and trainable parameters separately**, and report preprocessing, training and inference time on the same machine and thread count.

**A note on uncertainty**

**Run only the uncertainty or repetition procedure your card specifies.** Broad multi-seed studies are optional after the semester and are not expected within the eight weeks.

Where your card does specify one, distinguish carefully between variability **across training runs**, across **changed partitions**, and across **resampled test units** — they answer different questions, and in several projects the useful one can be computed from predictions you already have, with no retraining.

Where your card specifies none, report the sample and event counts behind each number and acknowledge the limits of a single-run comparison. **Do not claim statistical significance or equivalence.** And never treat overlapping windows from one recording as independent evidence.

**A note on attention**

If your research question involves "the model attends to X," an attention heatmap by itself is **not evidence**. Attention weights are widely argued not to be faithful explanations. You must test the explanation with an appropriate occlusion, masking or ablation control.

**Report the observed effect whether it supports or contradicts your hypothesis.** An intervention that does not degrade the prediction is evidence *against* the explanatory story, and it is a complete, fully-credited result — not a failed experiment and not non-compliance. Where practical, compare against a matched control intervention, so that generic input damage is not mistaken for evidence about attention.

Where you make no explanatory claim, an architectural attention/no-attention ablation is sufficient. You are not required to run an interpretability study.

## 5. The five shared tracks

Each track lists three research questions. **The question each group takes is assigned by the instructor along with the track**, and is issued to you as an assignment card. Groups do not choose or swap between them — the three questions were balanced against each other deliberately so that no group draws a thinner one.

**Your assignment card governs.** It names your datasets **and the role each one plays** — mandatory, test-only or optional — your split protocol, your baseline, your **two core experiments**, your required models, your fusion pair, your metrics and your scope caps. Where anything else, including the track summary below, appears to require a third experiment or an extra dataset, the card wins and that work is optional.

**What the card does not override:** the common rules in §4, the assessment rules in §9, the ethics and licensing rules in §10, and your manifest entry. A card does not waive a course outcome, a grading rule or a data-use restriction. If you find a conflict in common policy, tell us — it will be resolved centrally and corrected in the released bundle.

**Track A — Bearing Fault Diagnosis**

**Data:** Vibration from rotating machinery test rigs (Case Western Reserve University; Paderborn University). **Paderborn is mandatory for A1 and optional for A2 and A3** — check your card before downloading anything. **Task:** Classify bearing faults from raw vibration. **The two rigs do not share a label set** — CWRU supports healthy / inner / outer / ball, Paderborn is used as healthy / inner / outer. Keep a separate, documented label map for each and never merge them silently. **Classical baseline:** Envelope analysis at the characteristic defect frequencies. It is strong. Beating it convincingly is the challenge.

| Question | What you would investigate |
|---|---|
| **A1** | Does a model trained at one motor load work at another? Two controlled shifts: the CWRU 4×4 motor-load transfer matrix — **four source-load fits evaluated on four targets, not sixteen trained models** — and **Paderborn artificial-damage → natural-damage on a fixed rig**. Which shift hurts more, and why? The Paderborn training side includes artificial outer-ring **and** inner-ring faults *(corrected at D1)*. Note what is actually held fixed: the rig, the sensors and the mounting. The damaged bearing populations still differ, so this **reduces rig-related confounding rather than isolating damage origin**. *(Cross-rig CWRU→Paderborn is optional — it changes rig, sensors and mounting at once, so it answers less.)* |
| **A2** | 1-D CNN vs. spectrogram CNN vs. classical envelope analysis. Which actually wins, and at what cost? **Matched parameter count and matched CPU time are two separate comparisons**, not one condition. Report total and trainable parameters separately, and preprocessing, training and inference time on the same machine and thread count. |
| **A3** | Much published work on this dataset cuts training and test windows from the *same* recording, which inflates results. Quantify that inflation, identical model. Two things to keep straight: *non-overlapping* is **not** the same as *recording-disjoint*, and moving to a different recording can also change load or severity — so state the narrower claim your controls support. Your deliberately overlapping run is an **audit control** your card asked for: label it as such, keep the valid-protocol result as your headline, and no leakage cap applies. |

*What makes this hard:* the secondary dataset ships as per-bearing archives of 150–180 MB each, so the subset you download is not the same thing as the subset you keep. Your card names the archives. **Two things we found in the files.** One CWRU file, `99.mat`, holds a second, duplicate recording besides its own, and a loader that grabs the first signal it finds will quietly put one healthy recording at two motor loads. And one of the Paderborn natural inner-ring bearings, KI04, also has outer-ring damage recorded on its data sheet. Your card says how to handle both.

**Track B — Crop Disease Detection**

**Data:** PlantVillage (lab images, uniform backgrounds) and Cropped-PlantDoc (the same diseases photographed in real fields). **Cropped-PlantDoc is a mandatory test-only set for B1 and optional for B2 and B3.** **Task:** Classify crop diseases from leaf images. **Classical baseline:** Colour and texture features + random forest. Stronger than you expect — many diseases have distinctive colour signatures.

**🔴 What we found in the target set, and what it means for you.** Cropped-PlantDoc is **2,578 images — 2,342 train, 236 test** — at a pinned repository commit. Three things you need before you interpret any number from it. **One class, *Tomato two spotted spider mites leaf*, has two training images and zero test images**, so the evaluable label set is 27, not 28, and that class is reported as unsupported. **The shipped split does not respect parent-photograph grouping**: eleven byte-identical files and sixteen near-duplicate pairs span train and test, covering fifteen of the 236 test images. And **eight of those identical photographs carry two different disease labels** across the split — three across corn grey-leaf-spot/northern-leaf-blight, four across potato early/late blight, one across Septoria/bacterial spot. Those conflicts show inconsistent annotation and make the affected target labels questionable, but they do not by themselves cap your macro-F1 or tell you which of the two labels is right. Report your fixed-universe result and your headline gap both with and without the affected classes, interpret the difference cautiously, and never relabel the target from your model's predictions. *(Corrected 24 September 2026: this said your confusions on those pairs were "partly the benchmark's own label noise" — a conflict across the split does not show which label is wrong.)*

**And in the source set.** PlantVillage's own published 80/20 split puts crops of one photograph on both sides for 243 test images, so you are issued a repaired split file and you use it. Its leaf grouping is complete for 25 of the 38 classes; for the rest, a group is a photograph rather than a leaf. B3 therefore studies the 19 classes with real leaf groups, not all 38.

| Question | What you would investigate |
|---|---|
| **B1** | Lab-to-field: models score >99% on PlantVillage in the literature. How much survives on real field photographs, and which augmentation strategy closes the gap? **Report your own measured in-domain number** beside the field number — the published figure is context, not a target. And read the note above before you interpret the corn and potato confusions. |
| **B2** | What is the model actually looking at? Remove the background and retrain — the dataset ships a segmented (background-removed) version of every image, so this is a controlled intervention you can run directly — and train on greyscale to measure how much is pure colour. **Report leaf-versus-background attribution only.** Quantified overlap between attention and *lesions* is **not** part of this project: no lesion masks exist for this dataset, and a heatmap over a region you have not annotated is not evidence. |
| **B3** | Published results report overall accuracy across 38 classes. Which diseases are genuinely hard, and how many training images per disease do you need for usable recall? Define "usable recall" numerically before you see results, and state whether your training caps are nested. |

*What makes this hard:* the two datasets have different, only partly overlapping label sets. Mapping them is week-one work and the map is published as a file.

**Track C — El Niño / Southern Oscillation Forecasting**

**Data:** NOAA sea-surface temperature — the Niño 3.4 index (a time series) and gridded ERSST v5 (spatial maps). **All three groups need the grids**, for the required 2-D representation and the fusion. **Task:** Forecast the Niño 3.4 anomaly at **1, 3, 6, 9 and 12 month lead times — five fixed leads.** **Classical baseline:** Persistence and an autoregressive model. Both are strong at short leads.

All three groups use **one product snapshot — ERSST v5, January 1950 to December 2024**, issued with the cards. **This mattered.** On 23 September 2026 the page we had named for the index still said ERSST v5, but the file it linked had become ERSST v6. The index now comes from NOAA CPC, and its anomalies use a 1991–2020 base. Check the version inside every file you download.

**One rule that catches everyone:** chronological splitting alone is not enough. At a 12-month lead, an example issued in month *t* has its target at *t*+12, which can land inside your validation or test period. **Every training target must stay in training and every validation target in validation; no test target enters model selection.** Annex D3 of the cards fixes the dates, the 24-month history, the five-output model and the event and onset convention.

| Question | What you would investigate |
|---|---|
| **C1** | ENSO forecasts degrade sharply when they cross boreal spring — the "spring predictability barrier." Do LSTM and TCN memory mechanisms degrade differently across it? Train **one model per architecture and stratify skill by initialisation month afterwards** — do not train twelve monthly models. |
| **C2** | Index-only 1-D models vs. a 2-D CNN on gridded SST maps, matched budget, by lead time. What does the spatial field buy you? Note that the grid model differs in **input and architecture at once**, so this compares two *systems*; it does not isolate the spatial field's contribution. |
| **C3** | Skill is normally reported pooled, where neutral conditions dominate. Report skill on strong El Niño and La Niña *events* specifically, against a baseline, with **signed thresholds for both phases** and the number of **independent** events stated — overlapping seasons are not separate events. Annex D3 of the cards defines the onset month, the neutral comparison and the skill formula. *(Subsurface heat content is optional; it needs an approved data source first.)* |

*What makes this hard:* the data is a few megabytes, so almost all the difficulty is in experimental design. Indexing forecasts by **initialisation** month rather than target month is where groups go wrong. Choose this if you want to think rather than plumb.

**Track D — Traffic Forecasting on Road Networks (Graph Neural Networks)**

**Data:** METR-LA (207 highway sensors in Los Angeles) and PEMS-BAY (325 sensors in the Bay Area), each shipping a **road-network adjacency matrix**. **PEMS-BAY is optional for D1, optional and budgeted for D2, and mandatory as a bounded replication for D3.** **Task:** Forecast traffic speed at every sensor 15, 30 and 60 minutes ahead, treating the sensor network as a graph. **Classical baseline:** Historical average by time-of-day-and-weekday, and ARIMA — plus, critically, a **per-sensor LSTM that ignores the graph entirely**. That control is what makes this track interesting, and it is **one weight-shared model applied across sensors, not 207 separate ones**.

This is the one track that uses the **Graph Neural Network** material from Unit 1. The data is small and the adjacency matrices come with it, so you spend your time on the question rather than the plumbing.

The **graph model is the core architectural contribution**. The per-sensor model, the image model and the historical average are **controls**, not four systems to engineer to equal depth.

| Question | What you would investigate |
|---|---|
| **D1** | **Does the graph actually help?** Graph model vs. per-sensor LSTM vs. a sensor×time image CNN vs. historical average, at matched budget. There is a live argument that simple non-graph baselines are more competitive than published tables suggest. Report **forecast error** (MAE/RMSE/MAPE) against CPU training time, with the cost curve built from those same fits. |
| **D2** | **What does the graph learn?** Compare the real road-network adjacency against one learned from training data and against a deliberately **mismatched** one. Shuffle the adjacency **relative to a fixed signal-node order** — permuting the graph and the signals together merely relabels the nodes and changes nothing, which is the commonest way to get a meaningless null here. Use **repeated** permutations and an identity (no-edge) control, and first **check that nothing else in your architecture mixes nodes**, or the identity control proves nothing. If the mismatched graph performs as well, the correct conclusion is that *this road alignment gave no detectable gain under this protocol* — not that the model ignores topology. |
| **D3** | **Missing sensors.** Mask sensor *inputs* at test time at fixed rates on known nodes, scoring only where ground truth is observed, with the same masks and seeds for every model, and **block outages distinguished from independently missing entries**. Does the graph model degrade more gracefully because neighbours compensate? Repeating on PEMS-BAY is a **replication**, not a controlled comparison — the two cities differ in network, period and much else besides failure rate. |

*What makes this hard:* the data is small and ships ready to use, so the difficulty is in the controls — resisting a positive result before running them, and handling masking and missing-value semantics correctly. A zero in these files is a **missing reading, not a speed of zero**.

**Track E — Semiconductor Wafer Map Defects**

**Data:** WM-811K — 811,457 real wafer maps from **46,293** production lots; 172,950 carry a label. The label set is **eight defect classes plus `none`**, single-label — only 25,519 labelled maps carry an actual defect. There is no mixed-defect class, so mixed-type classification is out of scope. **Task:** Classify spatial defect patterns. **Classical baseline:** Geometric and radial features + random forest.

**Getting the data.** The MIR Lab archive is a direct download with no login: **344,542,743 bytes transferred**, from which the Python pickle extracts to **1.88 GiB retained**. Report both figures. Watch how it marks a missing label: unlabelled rows hold a two-element zero array, not an empty value, so a careless filter counts every wafer as labelled. You should get 172,950 labelled and 638,507 unlabelled.

**What we measured about the built-in split, and why it matters to all three groups.** It is **lot-disjoint** — 5,809 training lots and 4,953 test lots, none shared. It is **test-heavy** — 54,355 training wafers against 118,595 test. And it is **shifted**: 32% of labelled training wafers carry a defect against 7% of test wafers, and the wafer-size distribution differs sharply. Earlier issues of this handout said the built-in split did not support a claim about unseen lots. That was wrong, and your card now says so.

| Question | What you would investigate |
|---|---|
| **E1** | Rare defect patterns. Near-Full has 149 labelled examples against None's 147,431, and only 54 of them are in training. Per-class recall against frequency; can targeted augmentation recover the tail? You work **under the built-in split**, which is lot-disjoint — so your result is an unseen-lot result, on a test set with a very different defect prevalence from training. State both. |
| **E2** | **Distribution shift inside a lot-disjoint benchmark.** The built-in split holds lots out *and* shifts defect prevalence and wafer size. You work with a second lot-disjoint split, issued with your card, stratified to approximately match class mix and wafer size, and compare each model under the two protocols descriptively. The difference combines training-population and size differences, the held-out class and wafer-size mix, and optimisation exposure under the time limit, so report the achieved distributions and updates; it does not isolate a causal cost of the shift. 1-D radial-profile model versus 2-D CNN throughout. *(Corrected 24 September 2026: this said the comparison measures "the cost of that shift".)* |
| **E3** | Only 21% of the dataset is labelled. How much does **one round** of pseudo-labelling from an eligible training-only pool actually buy, per unit of compute? The eligible pool after exclusions is about 620,000 wafers, so the pool is not the limit — CPU time is. Your card therefore fixes two nested pool caps, 2,000 and 10,000 wafers. |

*What makes this hard:* wafer maps vary in size and need a justified resize strategy — and because the values are **categorical** (outside wafer / good die / bad die), an interpolating resize invents values that mean nothing. ~93% of test labels are "None," so accuracy is meaningless. Note also that **E2 uses its own matched lot-disjoint split, issued with its card, while E1 and E3 use the built-in one**: you share loader and baseline *code*, not split membership or a single baseline number.

## 6. The individual projects

These are standalone. **You will build the entire pipeline yourself** — the part shared-track groups split three ways. Choose one only if your group wants that.

| # | Project | The question | What makes it demanding |
|---|---|---|---|
| **I1** | **Satellite telemetry anomaly detection** | A widely used benchmark in this area is criticised in the literature. Run a small deep detector and a *trivial* detector as a control on the better-curated primary benchmark, then run a bounded audit of the criticised one. **The two benchmarks are scored natively and separately** — one uses labelled fragments, the other anomaly intervals in continuous streams, and pooling them would be meaningless. Your core comparison runs in **one label-access regime**, named on your card. You are not asked to reproduce all thirty published baselines. | Conceptually the hardest project offered. You are testing a claim about a literature, not just fitting a model. Either verdict — trivial detector competitive or not — earns full marks. The criticised benchmark's original download has gone, so its two audit streams come with your card, as does the fixed development list for the primary benchmark. No account is needed. |
| **I2** | **ECG diagnostic superclass classification and patient-overlap audit** | Much reported ECG performance comes from splits that put the same patient in train and test. Compare the official patient-disjoint protocol with five fixed record-level audit splits; report the actual patient overlap and the resulting score contrasts. The contrast combines overlap with changed partitions and does not identify a causal leakage effect. *(Corrected 24 September 2026: this said "quantify how much of the headline number that accounts for", which the audit cannot do.)* The core is **five-superclass multi-label** classification on PTB-XL's official folds plus a controlled patient-overlap audit; cross-dataset transfer to MIT-BIH is optional. | Multi-label clinical data — a multi-hot target and thresholds chosen on validation, not an argmax; careful protocol work, and a baseline that has to suit ten-second records rather than rhythm strips. |
| **I3** | **Battery life prediction from early cycles** | Predict a battery's total cycle life from only its first ~100 cycles, before any capacity fade is visible. Then: how few cycles can you get away with? The core task is **regression**. | Strong published baseline to beat; the three data files total **7.70 GiB** to transfer, but you fetch and compact them one at a time and keep only about 116 MB, and the `.mat` structs take real effort to parse; every feature must derive from cycles at or before your horizon; and **five cells appear in two batches**, so your split unit is the physical cell, not the batch-cell pair. The structs' own `cycle_life` field is not always the cell's life, so the target is issued as a file. Your card names the files, the sizes and the duplicate IDs, and it comes with the cell split and the cycle-life targets already fixed. |
| **I4-S** | **Landslide detection from multispectral imagery** *(substitute — see the note below)* | The benchmark's own authors state they performed **no transferability evaluation**, on a dataset deliberately built from multiple regions. Fill that gap: a spatially separated within-group reference versus **transfer from other scene groups**, scored on the same test patches, and does topography transfer better than spectral response? | 14 bands where ImageNet backbones take 3; severe pixel imbalance; **the original download links are offline, so the course uses a pinned mirror, and the release carries no region labels at all**, so the grouping had to be recovered from the pixels by matching tile edges horizontally **and vertically**. That pass has been run: **four scene groups**, and your card issues the split as a frozen file. You reproduce the recovery in Week 1 and report any disagreement. |
| **I5** | **Bird species from audio** | Models are trained on close-mic focal recordings but deployed on distant, cluttered soundscapes. **Measure the gap** against the Powdermill annotated soundscape set (48 species, strongly labelled) and the controlled SNR degradation. Mitigation is optional. | **Register for the API key the day you get your card**, and confirm it works in your readiness note. The species intersection is settled — all 48 qualify on xeno-canto availability, and the full list with counts is in your manifest. Your 15 species and their 900 source recordings are fixed and issued with your card — the 15 of the 22 soundscape-eligible species with the most soundscape windows, each with at least 163 usable recordings against the 50 required — so Week 1 is the access check and reproducing the usability count, not a discovery exercise. The audio files are the recordists' originals, some of them large WAVs, so budget the transfer. Watch the taxonomy: xeno-canto follows IOC and eBird does not, and a mismatched name returns zero recordings with no error. The task is **multi-label in both domains**, so use macro-F1 and per-species recall, not single-label accuracy. Your focal labels are weak and the soundscape labels strong — see Annex D8a. |
| **I6** | **Crop mapping from satellite time series** | Does atmospheric correction of satellite imagery actually help deep models, or do they learn to compensate? The dataset ships both processing levels, so this is directly testable — **but only if you make them comparable.** | Three things differ between the two levels, not one: the default **band selection**, the **column name** for the crop code, and a default transform that **re-samples observation dates at random on every call**. A fourth sits inside the files: the L1C file stores its bands in a different order from the package's own band list, so reading bands by name picks the wrong ones. And the paired data over the official partition is **11.34 GiB** if kept at once, which is over the working-data policy — so your card keeps all four official regions, caps the parcels, and has you process one region at a time. The parcel selection comes with your card. |

**A note on I4.** The CAXTON 3D-printing project has been **withdrawn from this release**. Its 1.27 million images are distributed as one hierarchical archive with no documented route to a bounded subset, and the only public mirror lacks the printer and geometry metadata the project depends on. That is a data fact, not a change of mind about the science; it may return in a later release if a bounded route is confirmed.

**To apply:** half a page per group — which project, why your group wants it, and **what you think the hard part will be**. That last question matters most. Deadline in §7.

**Applications are ranked by suitability, not by preference order.** We rank on whether your group has correctly identified the project's real difficulty. Apply for what you can carry.

## 7. Choosing, and proposing your own

**This section records a process that has already run for you: preferences closed, applications and self-proposals were considered, and the project titles are allocated. It is kept so you can see how your project was chosen and what a self-proposal had to show.**

**Everyone submits:** group members, and your **ranked preference over the five tracks**. We will try to honour preferences; we cannot guarantee them.

**Optionally:** an individual-project application (§6).

**Or propose your own project.** This is allowed and welcomed, but the bar is the same one we applied to every project above. **Be aware that this route is substantially more work than submitting a preference** — the preference form takes about an hour; a credible self-proposal takes several, because it requires you to have the data in hand before you propose. That is deliberate: a good research question on an unusable dataset is not a project.

You must submit, on one page:

- The dataset — **downloaded, on your machine, before you propose it.** A representative approved subset is enough; you do not need the full release.
- Its confirmed shape: how many samples, what dimensions, what the labels actually mean, and **what the split unit is**
- If your metric is per-class or event-based: **how many positive events exist**. A plan to report per-class F1 on classes with five examples is not a plan.
- The non-DL baseline you will compare against
- Your research question, and the two experiments that would answer it

**Instructor approval of your dataset readiness note is required before a self-proposed project is approved.** We will check your numbers before agreeing.

**Preferences, applications and self-proposals closed before allocation, and the titles are now allocated.** A self-proposed project is **provisional** until its readiness note is approved in Week 1 — you propose on the evidence you have, and approval follows the Week-1 check like everyone else's.

## 8. Week 1: the dataset readiness note

**Due Friday 2 October 2026, the last day of Week 1 and its fifth working day. Required and checked — not separately marked.** It gates your track baseline mark (§9) and, for self-proposed projects, project approval. If your numbers do not match, that halts the affected modelling — not the rest of your week, and not your marks.

Before you write any model code, confirm your data is what it claims to be. Your **manifest** lists expected counts, sizes, shapes, class counts and known traps, with an evidence label on each figure — read those labels, because not every number is a gate. **Download the approved required subset named on your card**, not the whole dataset and not the optional extras, after a preliminary access and size check.

Submit one page covering:

1. **The numbers you got**, against the manifest, and **any mismatch** with what you think caused it.
2. **Your declared split unit**, in one sentence, **and how you built the *validation* partition** — not just train and test — with **support in each of the three partitions**. For classification, per-class counts. **For regression and forecasting projects (Track C, D1–D3, I3), report cells, dates, regions or independent events instead** — per-class counts do not apply and you should not invent them.
3. **The access route** you used, including anything that required a login, an API key or manual acceptance of terms. **Never commit a key to your repository.** A lawful manual route with an integrity check is fully acceptable and is **not** a reproducibility penalty.
4. **Your environment** — Python version, OS, pinned package versions used to parse the data.
5. **Transferred bytes and retained working bytes**, where those differ.
6. **Anything that surprised you** — a field you did not expect, a file that would not parse, a count that seemed off.
7. **🔴 Your machine, and one timed run of your card's reference configuration.** Run the reference configuration identified for your card in Annex D0's Week-1 measurement table — one of your required fits, under the D0 limits, reused later in your project and not an additional experiment. Report **hardware** (cores, RAM, operating system), **thread and data-loader worker settings**, **elapsed time and aggregate CPU time**, **epochs and optimisation updates** completed, **which limit stopped the run** (epochs, minutes or early stopping), **peak memory**, **evidence of optimisation** (training and validation loss over the run, or a documented converged state), and **whether validation and one timed inference pass over test-shaped data finished** — time it, but do not compute or look at test labels or test metrics. Comparative accuracy is not graded at this checkpoint, and beating a trivial or classical baseline is not a condition of passing it. Then **project the total required programme** against the 24-hour elapsed budget, including classical baselines and repeated inference, using the stage Annex D0 tells you to time on a subset. A fit that hits the time limit before it has learned anything is not a failure on your part — it is the finding we most need, because the D0 timing limits were set as design bounds and were not piloted on a machine like yours before your card was issued. **The instructor replies to every note by Tuesday 6 October 2026**, confirming your configuration or issuing a corrected one; a scope cut made on measured evidence carries no penalty. *(Added 24 September 2026; rewritten the same day, because "the smallest model your card requires" could be the cheapest model on the card and so miss the one that matters.)*

A machine-readable attachment for counts and split IDs is welcome and does not count against the page.

Once your data is on your machine, the checking typically takes **two to three hours**. That estimate excludes acquisition and model implementation: downloading multi-gigabyte sources, Team 16's reproduction of the scene grouping, a first audio or image pipeline, and the timed run in item 7 all take longer and are not in it. It is the most transferable skill in the course. Real failures in this field come from datasets that were not what someone assumed — a "multivariate" dataset that turns out to be univariate, an image set where thousands of images are rotated copies of the same original leaking across a split, a published split with the same photograph on both sides under two different labels, a project whose split unit turns out not to exist in the released files. Every one of those is in this pack, found by exactly this check.

**For shared tracks:** each of the three groups must run this **independently**, on their own machine. Reproducing the shared baseline is what earns your track's baseline mark.

## 9. Assessment (30 marks) — tentative

**This rubric is tentative.** The components, marks, caps and descriptors in this section may be revised before final assessment. The final rubric will be announced to every group in writing **by Friday 30 October 2026, the end of Week 5**; until then, plan your work against this version. **A revision will not penalise work already done in line with this version.** *(Added 26 September 2026.)*

| Component | Marks |
|---|---|
| Problem formulation and fundamentals | 3 |
| Data pipeline, preprocessing, EDA | 4 |
| Non-DL baseline | 3 |
| Deep learning implementation (1-D, 2-D, attention, fusion) | 7 |
| Research question and experimental study | 6 |
| Evaluation and error analysis | 5 |
| Oral defense and team understanding | 2 |
| **Total** | **30** |

**What the 7-mark implementation component asks for.** Your required models are appropriate and correctly implemented; your attention module has a valid ablation; **the two-model fusion named on your assignment card** is implemented with validation-only weight selection; training and hyperparameters are justified. For most projects the named pair is your 1-D and 2-D models; where your card names a different pairing because the research question turns on it, **the card's pair is what is marked**.

**Writing style is not separately marked.** We are not assessing prose quality, formatting or elegance. But the report **must communicate your methodology, experiments and results clearly enough to be assessed and reproduced** — if we cannot follow what you did, we cannot award marks for it. Clear and plain beats polished and vague.

Note also that implementation (7 marks) is weighted above the research question (6). A group with an excellent, correctly evaluated implementation and an unexciting result outranks a group with a weak implementation and a striking claim. This is a deep learning course first.

**Things you should know before you start**

**Negative results earn full marks.** If you demonstrate rigorously that deep learning does *not* beat the classical baseline, that performance collapses under a shift you defined, or that an attention intervention *fails* to degrade the prediction, that is a complete and correct result. It is scored exactly like a positive one. Do not quietly tune until the numbers look good — we would rather have the honest finding.

**Finding a defect in the data or in this pack is also a result.** A documented manifest error, a contaminated published split, a missing metadata field your project needed — report it, work round it, and say what it does to your claim. That is scored under evaluation and error analysis, and it costs you nothing.

**Three ways to lose marks that have nothing to do with model quality:**

- **Leakage** that invalidates your headline result caps your total at 15/30. *But:* if **you** find your own leakage, report it, and re-run correctly, there is no penalty at all. That is good science and it will be said so. **And a deliberately flawed split that your assignment card asked for is a deliberately leaky audit control, exempt from the leakage penalty** — several of these projects exist precisely to measure what a bad protocol does. Label such runs explicitly as audit controls, keep the valid-protocol result as your headline, and **no cap applies**. This exemption overrides any shorthand about leakage elsewhere in the pack.

- If your team cannot explain its own work in the defense, your total is capped at 18/30 regardless of code quality.

- No working image component caps the **implementation mark at 3 out of 7**, since one of the course outcomes is then unmet.

**The alternatives rule — if a required representation genuinely does not suit your data.** Show it with evidence and propose a defensible alternative. **Get it approved in writing by the end of Week 2.** The approval will name the replacement implementation and state how the relevant course outcome and the seven-mark component are then evidenced. **Rejecting an unsuitable representation is credited** — it is a correct negative finding about something we prescribed — **but it is not by itself an implementation of the outcome it replaces**, so the approval has to say where that outcome is evidenced instead. The gate exists to make sure the component is attempted, not to punish a correct finding.

**A deliberately weakened baseline** to make your model look better scores 1 out of 3. In several of these projects the classical method is genuinely competitive — say so if it wins.

## 10. Ethics and data

- **No project may present its model as a diagnostic or operational tool.** Health-related projects must state in the report that the work is a research exercise, is not clinically validated, and must not be used for diagnosis.

- **Check your dataset's licence before you use it**, not only before you publish, and check it again before any redistribution. Several are research or non-commercial only, and some carry mixed per-item terms. Sharing data within your own track is permitted only where the source terms allow it.

- **Cite the dataset paper**, not just the URL. These datasets took people years to build.

- Human data used here is already de-identified and public. Do not attempt re-identification or cross-linkage.

## 11. On publication

Some of these projects could become conference papers. None will be finished by week 8.

What a strong group has at the end of eight weeks is a clean controlled result and reproducible code. What a submission additionally needs — repeated runs with error bars, a proper related-work section, and the writing itself — is work for after the semester. Treat publication as neither required nor predicted. **Marks here reward correctness, understanding and a well-executed controlled study, including a negative or replication result.** Nothing in §9 depends on whether the work is publishable.

If your group wants to take it that far, tell us in week 8 and we will discuss what it needs. Treat it as an optional continuation, not an expectation.

## 12. Practical rules

- **Python and PyTorch.** CPU only.

- Permitted: 1-D CNNs, LSTM/GRU, autoencoders, **graph convolution / diffusion-convolution layers and graph attention** (Track D builds these — a GCN or diffusion layer stacked with a temporal component is the CPU-friendly choice), lightweight attention (SE, CBAM, temporal pooling), transfer learning with frozen or lightly fine-tuned ResNet-18 / MobileNetV2 / EfficientNet-B0 at ≤224×224, **and small task-specific CNNs trained from scratch where your card allows one**.

- Not permitted within this project: training transformers from scratch, 3-D CNNs, diffusion models, large object detectors.

- **You acquire your own data, and how you do it is marked as reproducibility, not as automation.** Provide an automated download **where the source permits it and it is practical**. Where access requires lawful manual acceptance of terms, a login or an API key, **provide the exact acquisition instructions and an integrity check instead — this is not a reproducibility penalty and it does not cost you marks.** What must be repeatable either way is everything after acquisition: processing, training and evaluation. Do not commit credentials, and do not redistribute data contrary to its terms. Do not share dataset copies between groups except within your own track's shared phase.

- **Check your download budget before you start.** Several of these sources ship far more than the project keeps, and in two cases the measured figure changed the scope or the acquisition plan of the project. Your card carries the numbers. If they do not fit your machine, tell us in Week 1 and we will cut scope — that costs no marks.

- **One command, in one of two named modes,** with the expected runtime of each stated: either **evaluate from saved predictions and checkpoints**, or **retrain the approved configuration**. Say which mode your command runs.

- **AI coding assistants are permitted**, but you must be able to explain the purpose and operation of all substantive code you submit, and justify your main implementation decisions, in the defense. The defense is where this gets checked, and the 18/30 cap applies. You remain responsible for the **correctness, citations, licensing and originality** of everything you submit — this matters especially if your work later goes toward a publication.
