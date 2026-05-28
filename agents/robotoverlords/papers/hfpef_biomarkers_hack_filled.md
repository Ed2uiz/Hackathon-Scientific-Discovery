# Research Digest: Biomarker Identification for Functional HFpEF Patient Stratification

**Audience:** FoO extension scoping — sourcing background and a candidate preprint to extend the Flow-of-Options paper (arXiv 2502.12929) into HFpEF biomarker stratification
**Date generated:** 2026-05-28
**Working directory:** `~/paperclip-test/hfpef_biomarkers_hack/`
**Searches run:** scope (s_bed621fd, s_297cf960, s_9662c964, s_b4fa8c8e); sq1 pools (s_23f40c67, s_b754ff67); maps m_781d7da9, m_e22262c9, m_cb0c9d8e — full per-SQ tags listed in each section.

---

## Clinical question (verbatim from intake)

What biomarkers enable meaningful functional patient stratification in heart failure with preserved ejection fraction (HFpEF), and which existing preprint in this domain is the strongest candidate to extend with a Flow-of-Options-style diversified-option reasoning layer?

**Context from team discussion:** The end goal is to find a specific preprint to build on as a domain-specific extension of Flow-of-Options (FoO; Nair, Trase, Kim, ICML 2025, arXiv 2502.12929). FoO is a reasoning method that builds a network of explicitly enumerated "options" per task step to force LLMs to explore a diverse solution space, demonstrated on AutoML including tabular classification/regression and therapeutic chemistry. SQ1–SQ4 establish the biomarker/stratification landscape; SQ5 uses that landscape to produce a ranked list of candidate preprints to extend, weighting candidates where a diversified-option / agentic-ML reasoning layer would plausibly add value (feature-selection-heavy phenomapping, multi-omic pipelines with many modeling choices, AutoML-adjacent stratification work).

---

## Scoping notes

- SQ1–SQ4 are largely independent landscape questions and can be searched in parallel; SQ5 is interdependent and must consume the keeper sets and synthesis from SQ1–SQ4 rather than being searched in a vacuum.
- Population scope spans the HFpEF clinical spectrum — definitions vary across studies (LVEF cutoffs of ≥50% vs ≥45%, HFmrEF inclusion, varying use of natriuretic peptide/invasive hemodynamic confirmation). Note per-study which definition is used.
- Decisions made during research:
  - **Corpus constraint surfaced in Phase 0:** the Paperclip corpus is PMC-open-access + preprints (bioRxiv/medRxiv/arXiv). The foundational closed-access HFpEF literature — Shah's 2015 *Circulation* phenomapping paper and most of Borlaug's invasive-hemodynamics canon — is NOT indexed. The digest is therefore preprint/OA-weighted by construction (relevant to SQ5's preprint bias; tracked as a cross-cutting finding).
  - **`filter` unreliable in this session:** the relevance-cache appears to have been poisoned by an over-strict early filter (subsequent filters on overlapping papers collapsed to 1 survivor). Switched to the sanctioned fallback — manual curation from auto-summaries plus `map --output_schema` for structured extraction. Logged in `_progress.md`.
  - **Identifier policy:** PMC IDs are used as the PubMed-linked identifier for PMC papers; DOIs added where extracted; preprint rows use the medRxiv/bioRxiv DOI.
- Searches run: tags `scope`, `sq1m`, `sq1anch` (+ SQ2–SQ5 tags below). Result IDs recorded per sub-question.

---

## Sub-Question 1: Candidate biomarkers that differentiate HFpEF subphenotypes

**Scope:** Circulating, imaging, and multi-omic biomarkers shown to differentiate HFpEF subphenotypes or phenogroups. Cover what each biomarker captures (inflammation, fibrosis, congestion, cardiometabolic, natriuretic axis) and the strength of subphenotype discrimination, not just association with diagnosis.

### Search and filter notes
- Search terms used: "circulating biomarkers differentiate HFpEF subphenotypes inflammation fibrosis congestion cardiometabolic"; "HFpEF biomarker phenogroup proteomic lipidomic signature distinct pathophysiology"; "HFpEF imaging biomarker CMR fibrosis microvascular atrial phenotype"; "HFpEF circulating marker GDF-15 ST2 galectin-3 CA-125 IL-16 subgroup discrimination"; plus anchor-targeted pass (Woolley/Downie/Binek/Tamaki phrasings).
- Result IDs: pool s_23f40c67 (48 papers), anchor pool s_b754ff67 (42); maps m_781d7da9 (13), m_e22262c9 / m_cb0c9d8e (anchors).
- Filter criteria applied: relevance to "biomarkers that differentiate HFpEF subphenotypes/phenogroups OR characterize a distinct HFpEF biological axis with reported discrimination." Per Rule A the filter language kept both the broad-biomarker and the subphenotype-specific framings. `--require` filtering was abandoned mid-SQ1 (cache poisoning, see Rule C note); curation done manually from map output.
- Rule C event: an over-strict filter pass ("…not solely HFpEF-vs-control diagnosis") collapsed 30→1; inspection showed it was wrongly dropping on-topic discrimination papers (Woolley, Downie, Binek). Recovered by rebuilding the pool under fresh tags and curating manually. Logged.
- Excluded and why: pure HFpEF-vs-control *diagnostic* markers with no within-HFpEF discrimination were down-weighted to keeper-notes rather than table rows (SERPINA3 proteomics PMC11980230; untargeted metabolomics PMC12583173 — both diagnosis-only, AUC ~0.72–0.84 vs controls). Reviews kept as context, not rows (Bayes-Genis PMC9253965; Morfino PMC9409788). Two preclinical-model papers retained only as axis illustrations (see synthesis), not as patient-discrimination rows.
- Keeper papers:
  - med_8004d82c9276 | BECAME-HF lipidomics — 3 plasma-lipid phenogroups (B1 high-risk multisystem, B2 aging/AF, B3 obese-metabolic), cross-cohort validated
  - PMC9065816 | Henkens HFA-PEFF — Olink CVDIII separates 4 early-HFpEF phenogroups
  - PMC10945015 | Siggins — Olink cardiometabolic splits a fibrosis(ECV) vs microvascular(MPR) HFpEF axis (only CHL1 shared)
  - PMC10848361 | Dattani DIAMOND-HFpEF — fibro-inflammatory panel → 3 k-means phenogroups; AF vs SR marker differences
  - PMC11287331 | Tamaki — IL-16 elevated specifically in the ventricular-arterial-uncoupling acute-HFpEF phenogroup
  - bio_65b01df68651 | Binek — cardiac ventricular proteome → 2 molecular HFpEF clusters differing in sex ratio
  - PMC12320929 | Downie — SomaScan plasma proteomics → 3 molecular phenogroups, survival differences independent of clinical vars
  - PMC9684116 | protein remodeling/inflammation panel (CATHGEN/TECOS/JHS) — 13–20 protein models, externally validated, prognostic subtyping
  - PMC7373930 | KaRen MPO/uric acid — microvascular-inflammation markers split diastolic-dysfunction & structural HFpEF subgroups; uric acid prognostic
  - PMC7230638 | Jirak — sST2/GDF-15/suPAR/H-FABP signature separates HFpEF from HFrEF aetiologies
  - PMC12175437 | atrial-dysfunction CMR + Gal-3/Pentraxin-3 — LA strain discriminates obese-T2DM HFpEF
  - PMC9626230 | irisin/leptin/MDA — HFpEF-with-AF vs HFpEF-without-AF cardiometabolic/oxidative axis

### Biomarker summary table

| Biomarker / panel | Modality | Biological axis captured | Subphenotype it differentiates | Discrimination evidence (effect / AUC / HR) | Population & HFpEF definition | Validation status | DOI/PMID |
|---|---|---|---|---|---|---|---|
| Untargeted plasma lipidomics (235 lipids; 10-lipid signature: long-chain acylcarnitines, ether-PC, oxidized SM) | omic (LC-MS) | Cardiometabolic / mitochondrial-peroxisomal dysfunction, fibrosis, congestion | 3 phenogroups: B1 high-risk multisystem (cardiac+liver fibrosis, congestion), B2 aging/AF, B3 obese-metabolic | 158/235 lipids differ across clusters (KW p<7×10⁻⁴); B1 vs B2/B3 worse survival (p=0.0008); composite HR 1.98 (1.19–3.82) | BECAME-HF: Belgian n=177, Canadian n=177 (105+74 HFpEF); LVEF/confirmation per parent cohort (NP-based) | External (RF classifier Belgian→Canadian; lower-risk groups replicate, B1 underrepresented) | 10.64898/2026.03.31.26349865 |
| Olink CVDIII 92-protein panel (top: NT-proBNP, GDF-15, MMP-2, OPG, TIMP4, CHI3L1, IGFBP2/7) | circulating proteomic | Inflammation + ECM remodeling + natriuretic | 4 early-HFpEF phenogroups by LVDD severity / structure / BNP | 32/92 proteins differ across phenogroups; top 8 survive Bonferroni; HFA-PEFF score rises G1→G4 (p<0.001) | HELPFul cohort N=507; ambulatory, age ≥45, LVEF ≥50%, no prior HF; NP via HFA-PEFF | Internal (1000× bootstrap); no external cohort | PMC9065816 |
| Olink Cardiometabolic 92-protein panel (ECV: DPP4,CNDP1,KIT,CA4,UMOD,MEGF9,CHL1; MPR: NCAM1,PLA2G7,TIMD4,FETUB,PCOLCE,CHL1) | circulating proteomic | Fibrosis (ECV) vs microvascular dysfunction (MPR); only CHL1 shared | Two distinct intra-HFpEF biological subphenotypes (fibrosis vs microvascular) | OPLS: ECV model R²=0.85/Q²=0.53; MPR R²=0.92/Q²=0.32; PLS-DA vs control Q²=0.47 | n=18 HFpEF, 15 controls; LVEF >45%; NYHA≥II or BNP≥150; DD on echo or invasive PCWP | Derivation only (n small) | 10.3389/fcvm.2024.1334226 |
| 49-marker fibro-inflammatory panel (syndecan-1, MMP-2, proBNP, angiopoietin-2, pentraxin-3, IL-8, NTproANP, Gal-3, ST2…) | circulating | Fibrosis, inflammation, endothelial, natriuretic, cardiometabolic | 3 k-means phenogroups (cardiometabolic-female; adverse fibro-inflammatory-male worst outcome; AF-predominant) + AF-vs-SR | Cluster↔AF p=0.023; Cluster 2 worst composite (log-rank p=0.029); AF higher MMP-2/Ang-2/proBNP/syndecan-1, lower IL-8 | DIAMOND-HFpEF (NCT03050593) N=136; LVEF ≥50% on TTE; clinical/radiographic HF; median FU 8.5 y | Derivation only | 10.1186/s12872-024-03734-0 |
| Interleukin-16 (IL-16) | circulating (ELISA) | Inflammation → LV myocardial fibrosis/stiffening | Elevated specifically in the ventricular-arterial-uncoupling phenogroup of acute HFpEF | IL-16 higher in V-A-uncoupling phenogroup; associated with worse outcomes only in that group (full HR not extracted) | Acute decompensated HFpEF registry (Japan, PURSUIT-HFpEF-type), LVEF ≥50%; 4 predefined phenogroups | Derivation only | PMC11287331 |
| Cardiac ventricular proteome (4411 proteins; 1684 differential between clusters) | omic (tissue proteomics) | Structural/contractile machinery + cellular/ECM communication | 2 molecular HFpEF clusters (A vs B) differing in sex ratio (sex per se NOT a distinct signature) | 1684/4411 proteins differ A vs B; minimal overlap with HFrEF proteome | Multicenter HFpEF & HFrEF ventricular biobank samples (Kass/Hahn/Zile/Van Eyk) | Derivation (multicenter, cross-institution) | 10.64898/2025.12.18.695212 |
| Plasma SomaScan proteomics (7151 SOMAmers; 831 used for clustering) | omic | Multi-pathway molecular signature | 3 molecular HF phenogroups with differing survival, independent of clinical characteristics | Phenogroups differ in survival independent of clinical variables (population proteomic clustering) | Population-based HF cohort (large-scale) | Derivation; population-based | PMC12320929 |
| 13-protein LASSO + 20-protein Olink panel (LCN2, U-PAR, IL-1ra, KIM1, CSTB, Gal-9, CLSTN2…) | circulating proteomic | Inflammation, fibrosis/remodeling, kidney injury, angiogenesis, metabolic | Diagnosis + prognostic subtyping (HFpEF vs control; distinct from HFrEF; outcome strata) | AUC 0.92 vs 0.82 (clinical+NTproBNP) in CATHGEN; 0.86 vs 0.75 in TECOS; individual OR 1.93–7.97 | CATHGEN n=176 (EF≥45%, DD≥1), TECOS n=109 (EF≥55%, T2DM), JHS prognostic n=570/448 | External (CATHGEN→TECOS; JHS prognostic) | 10.1038/s41598-022-24226-1 |
| MPO, uric acid, calprotectin, ADMA/SDMA, arginine ratios | circulating | Microvascular inflammation / oxidative stress / NO availability | HFpEF with diastolic dysfunction (E/e′>14) and structural (LAVI>34) subgroups; high vs low uric-acid risk | Uric acid 421 vs 344 µM (p=0.012), SDMA p=0.039; uric-acid>median composite HR 4.79 (1.55–14.82), adj 3.76 | KaRen multicentre N=86; LVEF ≥45%; acute HF (Framingham)+NT-proBNP>300; 46 controls | Derivation only | PMC7373930 |
| sST2, GDF-15, suPAR, H-FABP | circulating | Subclinical ischemia (H-FABP), remodeling (GDF-15), strain/inflammation (sST2), immune (suPAR) | HFpEF vs HFrEF aetiologies (ICM/DCM): HFpEF marked by ↑H-FABP/GDF-15 but normal sST2/suPAR | H-FABP AUC 0.79, GDF-15 AUC 0.79 (HFpEF vs others); sST2/suPAR not elevated vs control (p=0.37/0.57) | 252 outpatients (18 HFpEF, 77 DCM, 62 ICM, 95 control); HFpEF per 2016 ESC, LVEF >50% | Derivation only | PMC7230638 |
| LA function (max volume, reservoir/conduit/booster strain) + Galectin-3, Pentraxin-3 | imaging (CMR feature-tracking) + circulating | Atrial remodeling (congestion/cardiometabolic) + inflammation/pro-fibrotic | Obese-T2DM HFpEF vs obese/diabetic controls; LA strain is sole independent discriminator (ECV/MPR & serum markers NS after adjustment) | LA reservoir strain AUC 0.83, conduit 0.81, max-vol 0.79; LA max-vol OR 1.13 (p=0.011); Gal-3/PTX-3 NS adjusted | n=35 (13 HFpEF+T2DM); LVEF ≥50%; E/e′≥8, BNP>220/NT-proBNP≥200, on GDMT | Derivation only (exploratory) | 10.1186/s12933-025-02808-3 |
| Irisin, leptin, MDA, NT-proBNP, adiponectin, IGF-1 | circulating | Cardiometabolic, oxidative stress, congestion | HFpEF-with-permanent-AF vs HFpEF-without-AF | Irisin 4.75 vs 13.5 ng/mL (p=0.007); leptin p=0.023; MDA p=0.017; NT-proBNP 2365 vs 529 (p<0.001) | n=52, age ≥65; LVEF ≥50%, LAVI>34, NT-proBNP>125, E/e′>9, sPAP>35 | Derivation only | PMC9626230 |
| Cardiac biomarker panel mapped onto echo-defined structural phenotypes | imaging (echo)-defined phenotype ↔ circulating biomarkers | Structural remodeling (LAE, DD, RV dysfunction) + corresponding biomarker axes | LCA-derived structural HFpEF phenotypes that differ in cardiac biomarker profiles | Distinct biomarker profiles across LCA structural phenotypes (RELAX secondary analysis); phenotype-specific natural history/prognosis | RELAX trial n=216; LVEF ≥50% (echo incl. EF≤55% as a class feature); HFpEF per RELAX criteria | Derivation (secondary analysis of one RCT) | med 10.1101/2024.04.30.24306660 |

### Paragraph answer
Within the HFpEF spectrum, biomarkers cluster along a small set of recurring biological axes — natriuretic/congestion (NT-proBNP, NT-proANP, CA-125), inflammation (IL-16, GDF-15, pentraxin-3, MPO/uric acid, IL-1ra), fibrosis/ECM remodeling (MMP-2, TIMP, syndecan-1, ECV by CMR), microvascular/endothelial dysfunction (ADMA/SDMA, MPR by CMR), and cardiometabolic/lipid dysregulation (acylcarnitines, ceramides, leptin/irisin, BCAA) — and the strongest *subphenotype-discriminating* evidence now comes from multi-marker omic panels rather than any single analyte. The clearest within-HFpEF separations are: a high-risk multisystem/fibrotic-congestive lipidomic phenogroup vs aging/AF vs obese-metabolic (BECAME, externally validated, composite HR ~2); a fibrosis-dominant (ECV) vs microvascular-dominant (MPR) cardiometabolic-proteomic split (Siggins, only one of ~13 markers shared between axes); two cardiac-tissue proteomic clusters that track sex ratio but not sex per se (Binek); and four early-HFpEF Olink phenogroups graded by diastolic/structural severity (Henkens). By contrast, the classic single markers (NT-proBNP, sST2, galectin-3) perform mainly as diagnosis/prognosis tools and largely lose independent discrimination once adjusted (e.g., Gal-3/pentraxin-3 NS after BMI adjustment in obese-T2DM HFpEF), and several heavily-cited proteomic/metabolomic "HFpEF biomarkers" (SERPINA3, tryptophan/PC species) are validated only against healthy controls, not across HFpEF subphenotypes. Discrimination strength is thus modality- and design-dependent: omic panels with explicit clustering deliver subphenotype separation but mostly at derivation/small-N stage, whereas externally validated work (BECAME cross-cohort; the CATHGEN→TECOS protein model) is the exception rather than the rule.

### Synthesis bullets
- Strongest subphenotype discrimination: **multi-omic/proteomic panels with explicit clustering** (lipidomics, Olink cardiometabolic/CVDIII, SomaScan, tissue proteomics) — these produce reproducible-looking phenogroups and, in BECAME, cross-cohort replication.
- Best-supported single axes: **congestion/natriuretic** and **inflammation** discriminate subgroups most consistently; **fibrosis vs microvascular dysfunction** is a genuine intra-HFpEF axis split (Siggins) but rests on small N.
- Largely aspirational / diagnosis-only: **galectin-3, ST2, SERPINA3, untargeted metabolomite panels** — strong vs controls, weak or non-independent for within-HFpEF subphenotyping.
- Cross-modal convergence: **imaging (LA strain, ECV, MPR) and circulating markers point at the same axes** (atrial/congestion, fibrosis, microvascular), suggesting biomarker-to-phenotype maps exist but are under-formalized.
- Recurring gap: most subphenotype-discrimination evidence is **derivation-stage, single-cohort, small-N**; external validation is the exception, which is exactly the heterogeneity-of-modeling-choices surface SQ4/SQ5 care about.

### Confidence read
- **Evidence quality:** Moderate. Many on-point studies, but dominated by single-cohort derivation work with small N; few externally validated (BECAME, CATHGEN→TECOS the standouts).
- **Direction of evidence:** Consistent that HFpEF is biomarker-separable into recurring axes (cardiometabolic, inflammatory/fibrotic, congestive, microvascular); inconsistent on *which* discrete phenogroup scheme is canonical.
- **Key uncertainty:** Whether biomarker-defined subphenotypes are stable across cohorts and HFpEF definitions, and whether they carry predictive (not merely prognostic) weight — addressed in SQ3.

---

## Sub-Question 2: Validated functional / clinical axes for HFpEF stratification

**Scope:** Functional and clinical axes used to stratify HFpEF — exercise hemodynamics, CPET-derived parameters (peak VO2, VE/VCO2), diastolic/contractile reserve, invasive exercise PCWP, and functional capacity measures. Assess which axes are most validated as stratification targets that biomarkers could map onto, and which are reference standards vs surrogates.

### Search and filter notes
- Search terms used: "HFpEF cardiopulmonary exercise testing peak VO2 VE/VCO2 prognosis stratification"; "HFpEF invasive exercise hemodynamics pulmonary capillary wedge pressure right heart catheterization"; "HFpEF diastolic reserve contractile reserve stress echocardiography exercise"; "HFpEF functional capacity six minute walk chronotropic incompetence peripheral oxygen extraction". Plus Phase-0 exercise-hemodynamics pool (s_b4fa8c8e).
- Result IDs: pool s_8e36cb55 (50 papers); map m_4ee30a15 (functional_axis classification for 15 papers; full structured fields not retrievable post-hoc — see flakiness note); quantitative anchors pulled by `paperclip grep` on individual papers.
- Filter criteria applied: relevance to "functional/clinical axis used to stratify HFpEF and whether it is a reference standard vs surrogate." `filter` not used (cache issue from SQ1); curated manually from the map functional-axis tags + auto-summaries + targeted reads.
- Excluded and why: exercise-*therapy* / rehab trials (Baduanjin PMC7668503; knee-extensor training PMC9350466; exercise-therapy-rescues-myopathy PMC11733766) — treatment, not stratification axis. Animal models (feline PMC5707379; Ca²⁺-removal mouse) excluded as non-clinical. Beta-blocker secondary analysis (med_4d549ed76ef2) noted but not a row (treatment effect).
- Keeper papers:
  - PMC2908890 | peak VO2 & VE/VCO2 slope head-to-head prognosis in chronic HF — reference for the two core CPET axes
  - PMC12692155 | Di Spigno CPET-in-HFpEF review — peak VO2, VE/VCO2, O2 pulse as primary axes
  - PMC9715813 | Baratto meta-analysis of exercise hemodynamics — steeper exercise PAWP rise defines HFpEF
  - med_6da399156fea | Chowdhury/Systrom/Waxman — supine vs upright invasive CPET changes measured PCWP (reference-standard caveat)
  - PMC11313028 | oxygen cascade by HFpEF likelihood — Fick decomposition (delivery vs a-vO2 extraction)
  - PMC11994855 | peripheral O2-extraction recovery is the strongest predictor of capacity/outcome
  - PMC11299572 | %predicted peak O2 pulse — surrogate for SV / ventricular-vascular response, independent mortality predictor
  - PMC8863971 | exercise systolic reserve + exercise PH improve HFpEF diagnosis
  - PMC11052864 | exercise CO/CI by real-time CMR — contractile/systolic reserve
  - PMC12719814 | out-of-proportion exercise afterload & impaired RV contractile reserve
  - PMC12246590 | RV myocardial work predicts exercise PCWP rise
  - PMC12449948 | chronotropic incompetence → HF hospitalization / CV death (invasive CPET cohort)
  - PMC9333393 | diastolic filling time + chronotropic response ↔ exercise capacity
  - PMC12202100 | meta-analysis VO2peak & 6MWD, HFrEF vs HFpEF — 6MWD as submaximal surrogate

### Functional axis table

| Functional axis | Measurement modality | What it captures physiologically | Reference standard vs surrogate | Validation evidence for stratification | Population & HFpEF definition | Limitations / feasibility | DOI/PMID |
|---|---|---|---|---|---|---|---|
| Exercise PCWP / PAWP–CO slope | Invasive (i)CPET + right-heart catheterization | LV filling-pressure response to exercise; defining lesion of HFpEF | **Reference standard** for HFpEF diagnosis & exercise hemodynamics | Meta-analysis: HFpEF shows disproportionately steep PAWP rise at peak exercise vs controls (rest+peak PAWP pooled across studies); core diagnostic criterion | Baratto: pooled HFpEF cohorts, LVEF≥50%, invasive exercise; definitions heterogeneous across pooled studies | Invasive, low throughput; supine vs upright positioning materially changes measured PCWP (med_6da399156fea) | PMC9715813; med 10.1101/2025.02.24.25322825 |
| Peak VO2 (peak oxygen uptake) | CPET (expired-gas) | Integrated maximal O2 transport/utilization (whole O2 cascade) | **Reference standard** for functional capacity / prognosis | In chronic HF, peak VO2 a primary prognostic discriminator (long-validated CPET endpoint); HFpEF peak VO2 reduced & predicts outcome | Chronic HF incl. HFpEF cohorts; LVEF varies | Effort-dependent; needs gas analysis & maximal effort | PMC2908890; PMC12692155 |
| VE/VCO2 slope (ventilatory efficiency) | CPET | Ventilation–perfusion matching, chemosensitivity, pulmonary vascular response | Prognostic **surrogate** (complements peak VO2) | Independent prognostic value alongside peak VO2 in chronic HF; abnormal in HFpEF, tracks pulmonary-vascular involvement | Chronic HF/HFpEF CPET cohorts | Effort-independent advantage but confounded by hyperventilation/lung disease | PMC2908890; PMC12692155 |
| Peripheral O2 extraction / a-vO2 difference (Fick) | Invasive CPET (Fick) | Skeletal-muscle O2 utilization (peripheral limb of the cascade) | **Reference** (direct Fick); marks peripheral phenotype | Poor peripheral O2-extraction *recovery* is the strongest predictor of exercise capacity & adverse outcomes among cascade components | Invasive-CPET HFpEF cohorts, LVEF≥50% | Requires invasive Fick; isolates peripheral vs central limitation | PMC11994855; PMC11313028 |
| % predicted peak O2 pulse (VO2/HR) | CPET | Surrogate for stroke-volume response / ventricular-vascular coupling | **Surrogate** for SV & VVR | 154 HFpEF (invasive CPET) by %PredO2P tertiles: higher %PredO2P → better VVR and independently predicted lower all-cause mortality | n=154 HFpEF, mean age 57±15, invasive CPET; LVEF≥50% | Surrogate, HR-dependent; less established than peak VO2 | PMC11299572 |
| Contractile / systolic reserve | Exercise stress echo / real-time CMR | Ability to augment LV systolic function & cardiac output on exertion | **Surrogate** for cardiac reserve | Exercise systolic reserve + exercise PH improve HFpEF diagnosis; exercise CO/CI quantifiable by real-time CMR | HFpEF stress-test cohorts, LVEF≥50% | Image quality at peak HR; CMR exercise not widely available | PMC8863971; PMC11052864 |
| Diastolic reserve / exercise LV filling pressure (E/e′) | Exercise stress echocardiography | Rise in filling pressure when preload/HR increase | **Surrogate** for invasive exercise PCWP | Diastolic stress echo (E/e′ on exercise) used in HFA-PEFF/diagnostic algorithms; diastolic filling time interacts with chronotropy to set capacity | HFpEF & at-risk cohorts, LVEF≥50% | Feasibility/repeatability of peak-exercise E/e′; surrogate for gold-standard PCWP | PMC9333393; PMC12692155 |
| RV–PA coupling / RV contractile reserve | Exercise echo / CMR (Ees/Ea, RV work) | RV adaptation to exercise afterload; ventricular interaction | Emerging **stratifier** (not yet reference standard) | Out-of-proportion exercise afterload + impaired RV contractile reserve mark a high-risk HFpEF group; RV myocardial work predicts exercise PCWP rise | HFpEF (± PH) exercise cohorts, LVEF≥50% | Load-dependence of indices; methodologically heterogeneous | PMC12719814; PMC12246590 |
| Chronotropic response / incompetence | CPET / invasive CPET (HR reserve, MCR) | HR augmentation capacity during exercise | Prognostic **surrogate** | Invasive-CPET HFpEF: chronotropic incompetence associated with elevated filling pressures, worse ventilatory efficiency, reduced capacity, and ↑ HF hospitalization / CV death | n=359 invasive CPET (HFpEF after exclusions), LVEF≥50% | Confounded by rate-limiting drugs (β-blockers); definition thresholds vary | PMC12449948; PMC9333393 |
| 6-minute walk distance (6MWD) | 6-minute walk test | Submaximal functional capacity | **Surrogate** / pragmatic endpoint | Meta-analysis: 6MWD & VO2peak both reduced in HFpEF (less than HFrEF); widely used trial endpoint but coarse stratifier | Pooled HFrEF vs HFpEF cohorts | Floor/ceiling, motivation/comorbidity-dependent; weak physiologic specificity | PMC12202100 |

### Paragraph answer
The functional axes used to stratify HFpEF form a hierarchy anchored by one true reference standard — the exercise/invasive pulmonary capillary wedge pressure response (PAWP–CO or PCWP–CO slope on invasive CPET/RHC), which captures the defining lesion of HFpEF (a disproportionate exercise rise in filling pressure) and underpins the HFA/ESC diagnostic criteria; Baratto's meta-analysis confirms the steep peak-exercise PAWP rise as the discriminating signature, while the positioning study shows even this "gold standard" is sensitive to methodology (supine vs upright). Around it sit complementary CPET axes: peak VO2 (the integrated reference for functional capacity and prognosis) and VE/VCO2 slope (effort-independent ventilatory-efficiency surrogate), plus Fick decomposition that increasingly localizes HFpEF limitation to *peripheral* O2 extraction rather than central output — peripheral O2-extraction recovery emerging as the single strongest predictor of capacity and outcome. Echo/CMR-based reserve measures (diastolic E/e′ reserve, contractile/systolic reserve, RV–PA coupling and RV contractile reserve, chronotropic response) are validated as prognostic *surrogates* and are the practical stratification targets a biomarker layer could map onto, while 6MWD remains a coarse pragmatic endpoint. Crucially, biomarker-to-function mapping is still sparse: only a handful of studies (e.g., R. Shah's proteomics-of-exercise-phenotypes pilot) explicitly link circulating signatures to invasive exercise physiology, so the functional axes are well-validated as endpoints but largely *unmapped* to the biomarker axes from SQ1 — a gap, not a solved problem.

### Synthesis bullets
- Best-validated stratification endpoint: **exercise/invasive PCWP** (reference standard); peak VO2 is the reference for capacity/prognosis; VE/VCO2 the robust effort-independent surrogate.
- Rising signal: HFpEF exercise intolerance is increasingly **peripheral** (O2 extraction, skeletal muscle), not purely central — peripheral O2-extraction recovery outperforms central measures as a predictor.
- Reserve measures (diastolic, contractile, RV–PA coupling, chronotropic) are **prognostic surrogates** and the realistic targets a biomarker could be mapped to; RV-side reserve marks a distinct high-risk axis.
- **Biomarker→function mapping is largely absent**: few studies connect SQ1 circulating/omic signatures to invasive exercise physiology — the clearest white space and a strong rationale for an option-enumerating pipeline (SQ5).
- HFpEF-definition heterogeneity is acute here: invasive vs echo confirmation and LVEF cutoffs change which patients enter functional cohorts, limiting cross-study comparability.

### Confidence read
- **Evidence quality:** Moderate-to-high for the axes themselves (invasive PCWP, peak VO2, VE/VCO2 are extensively validated); lower for newer surrogates (RV–PA coupling, peripheral extraction) which rest on smaller single-center invasive-CPET cohorts.
- **Direction of evidence:** Consistent — exercise PCWP is the defining/standard axis; peripheral and RV-side limitation are reproducibly important; reserve measures stratify prognosis.
- **Key uncertainty:** Whether any biomarker reliably *maps onto* these functional axes (largely untested), and how feasibly invasive-CPET-grade stratification scales beyond expert centers.

---

## Sub-Question 3: Biomarker-defined clusters with differential treatment response or prognosis

**Scope:** HFpEF phenogroups or biomarker-defined clusters that show differential prognosis or differential treatment response (e.g., to SGLT2 inhibitors, MRAs, GLP-1 RAs). Distinguish clusters with demonstrated treatment-effect heterogeneity from clusters validated only for prognosis.

### Search and filter notes
- Search terms used: "HFpEF phenogroup cluster differential prognosis mortality hospitalization outcomes"; "HFpEF cluster differential treatment response SGLT2 inhibitor spironolactone subgroup interaction"; "HFpEF latent class phenomapping treatment effect heterogeneity trial"; "HFpEF biomarker subgroup SGLT2i GLP-1 finerenone response predictive"; targeted pass for Woolley/Uijl/TOPCAT-phenomapping/STEP-HFpEF.
- Result IDs: pools s_65fb58c0 (48), s_230576e7 (49); map m_7eaae57c (8 papers, design/N classification); effect sizes via `paperclip grep` on individual papers.
- Filter criteria applied: relevance to "HFpEF clusters/subgroups showing differential PROGNOSIS or differential TREATMENT RESPONSE." Manually curated; the SQ scope distinction (prognostic vs predictive) was used as the keep/sort axis.
- Excluded and why: generic drug-class efficacy reviews & mechanism papers that do NOT condition effect on a cluster/subgroup (network meta-analysis; "SGLT2i cardiac metabolism fact or fiction" PMC12079913; beta-blocker review PMC11802620; epicardial-fat phenotype descriptive). Animal semaglutide (PMC10714176) excluded. These establish that therapies work in HFpEF broadly but not by biomarker cluster.
- Keeper papers:
  - PMC8359985 | Uijl — LCA, 5 SwedeHF clusters, externally validated (CHECK-HF); prognosis + differing drug therapy
  - PMC8360080 | Woolley — unsupervised clustering of 363 biomarkers in 429 HFpEF → 4 subgroups, distinct outcomes
  - med_8004d82c9276 | BECAME — 3 lipid phenogroups, B1 composite HR 1.98, cross-cohort
  - PMC12320929 | Downie — 3 proteomic phenogroups, survival differences independent of clinical variables
  - med_6891987272dd | Raza PH-HFpEF — high-risk RV-dysfunction phenogroup, worse outcomes
  - PMC12719802 | suPAR TOPCAT ancillary — strong prognostic biomarker that spironolactone does NOT modulate (prognostic ≠ predictive)
  - PMC12572816 | Li — DeepCluster 3 phenogroups; SGLT2i/ARNI benefit concentrated in metabolic phenogroup 1; externally validated
  - PMC10504076 | STEP-HFpEF — semaglutide benefit in the obesity phenotype, consistent across obesity classes
  - PMC11400859 | STEP-HFpEF + STEP-HFpEF-DM pooled — semaglutide benefit by diuretic/congestion status

### Cluster outcomes table

| Study | Design | N | Population & HFpEF definition | Clustering basis | Outcome examined | Differential effect | Validated externally? | DOI/PMID |
|---|---|---|---|---|---|---|---|---|
| Uijl 2021 | Latent class analysis (cluster) | 6909 derivation + 2153 external | SwedeHF; LVEF ≥50% | Clinical variables/comorbidities | **Prognosis** (+ differing HF drug therapy) | 5 clusters with distinct mortality/HF-hospitalization; clusters differ in prognosis | **Yes** — external validation in CHECK-HF (ESC-HF-LT) | PMC8359985 |
| Woolley 2021 | Unsupervised cluster analysis | 429 | HFpEF (BIOSTAT-CHF–type); LVEF ≥45/50% | 363 circulating biomarkers | **Prognosis** | 4 mutually-exclusive subgroups with distinct biomarker pathways & outcomes; highest-risk cluster worst prognosis | Derivation (internal); not externally validated | PMC8360080 |
| BECAME-HF (Hussin/Menghoum) | Hierarchical clustering (lipidomics) | 105 + 74 HFpEF (2 cohorts) | Belgian + Canadian; NP-based HFpEF | Plasma lipidomics (235 lipids) | **Prognosis** | B1 (high-risk) composite HR 1.98 (1.19–3.82); KM survival p=0.0008 | **Cross-cohort** (Belgian→Canadian classifier; lower-risk groups replicate) | 10.64898/2026.03.31.26349865 |
| Downie 2025 | Proteomic clustering | population cohort | LVEF per cohort adjudication | SomaScan (831 proteins) | **Prognosis** | 3 molecular phenogroups, significant survival differences independent of clinical characteristics | Derivation; population-based | PMC12320929 |
| Raza 2025 (PH-HFpEF) | k-means (multimodal) | 42 PH-HFpEF | invasive PH-HFpEF; LVEF ≥50% | iCPET hemodynamics + clinical + transcriptomics | **Prognosis** | High-risk RV-dysfunction phenogroup with worse outcomes & distinct transcriptome | Derivation only (small N) | 10.1101/2025.05.15.25327467 |
| suPAR-TOPCAT (2025) | Biomarker ancillary within RCT | 406 | TOPCAT N. America; LVEF >45% | suPAR (single inflammatory biomarker) | **Prognosis, NOT predictive** | suPAR independently predicts poor outcome; **spironolactone does not modulate suPAR** (no treatment interaction) | Within-trial (TOPCAT) | PMC12719802 |
| Li 2025 | DeepCluster (ML) + Rx response | 2147 train + external | PKUTH hospitalized HF, LVEF ≥50% | Clinical + echo features (deep clustering) | **Treatment response (predictive)** | 3 phenogroups; SGLT2i & ARNI benefit greatest in metabolic Phenogroup 1 (n=815, ↓HF rehospitalization) | **Yes** — externally validated cohort | PMC12572816 |
| STEP-HFpEF (Butler/Kosiborod 2023) | RCT, prespecified subgroup | 529 (263 sema / 266 pbo) | Obesity-phenotype HFpEF; LVEF ≥45%, BMI ≥30 | Obesity phenotype (BMI classes) | **Treatment response** | Semaglutide ↑ KCCQ-CSS & 6MWD vs placebo, benefit **consistent across obesity classes** (no strong heterogeneity by BMI) | RCT (single-phenotype enrollment) | PMC10504076 |
| STEP-HFpEF + DM pooled (2024) | Pooled analysis of 2 RCTs | 1145 | Obesity-phenotype HFpEF ± T2DM; LVEF ≥45% | Congestion/diuretic-use strata | **Treatment response** | Semaglutide benefit on symptoms/weight across diuretic-use (congestion) strata; larger absolute effect in more-congested | Pooled RCT | PMC11400859 |

### Paragraph answer
HFpEF clusters carry strong *prognostic* weight but only weak, mostly post-hoc *predictive* (treatment-response) weight. The prognostic signal is robust and, in places, externally validated: Uijl's five latent-class clusters replicate from SwedeHF (n=6909) into CHECK-HF (n=2153); Woolley's four biomarker-defined subgroups, BECAME's three lipidomic phenogroups (high-risk B1 composite HR ~2), and Downie's three proteomic phenogroups all separate survival, the last independent of clinical variables. By contrast, evidence that a *biomarker-defined cluster predicts who responds to therapy* is thin and rests on (a) machine-learning phenomaps reporting concentrated benefit — Li's DeepCluster finds SGLT2i/ARNI effect largest in the metabolic phenogroup — and (b) trial subgroup analyses anchored to the obesity *phenotype* rather than to a biomarker cluster (STEP-HFpEF: semaglutide improves KCCQ/6MWD, but benefit is broadly *consistent across* obesity classes rather than driven by a discrete subgroup). The sharpest illustration of the prognostic–predictive gap is the suPAR-TOPCAT ancillary: suPAR independently predicts poor outcomes yet spironolactone does not modulate that pathway, i.e., a powerful prognostic marker with no demonstrated treatment-interaction. So the honest read is that the field has many prognostically-distinct clusters and essentially one well-defined responsive phenotype (obesity/cardiometabolic → incretin/SGLT2i), with formal biomarker-cluster × treatment interaction testing still largely absent.

### Synthesis bullets
- **Prognostic** clusters are the norm and the best-validated (Uijl externally validated; Woolley, BECAME, Downie separate survival).
- **Predictive** (treatment-response) clusters are scarce and largely post-hoc: the obesity/cardiometabolic phenotype responding to semaglutide (STEP-HFpEF) and SGLT2i benefit concentrated in Li's metabolic phenogroup are the strongest, but neither is a randomized biomarker-cluster-by-treatment interaction.
- **suPAR-TOPCAT is the cautionary case**: strong prognostic biomarker, zero predictive value for spironolactone — prognosis does not imply treatment-effect heterogeneity.
- Treatment-effect-heterogeneity claims lean heavily on **post-hoc subgroup analyses of single trials**; there is no prospective HFpEF trial randomizing within biomarker clusters.
- The one phenotype with converging predictive signal — **cardiometabolic/obese HFpEF** — is also the most biomarker-rich (SQ1) and methods-heavy (SQ4), making it the natural locus for SQ5 extension work.

### Confidence read
- **Evidence quality:** Prognostic evidence moderate-high (large registries, some external validation); predictive evidence low (post-hoc, single-trial, phenotype- not cluster-randomized).
- **Direction of evidence:** Consistent that clusters separate prognosis; inconsistent/weak that they predict differential treatment response beyond the obesity phenotype.
- **Key uncertainty:** Whether any biomarker cluster carries genuine predictive (treatment-interaction) value — currently unproven prospectively; the cardiometabolic phenotype is the only credible candidate.

---

## Sub-Question 4: Analytic / methodological approaches and reproducibility of phenogroups

**Scope:** Methods used to derive HFpEF phenogroups — unsupervised clustering (k-means, hierarchical), latent class analysis, ML/AutoML pipelines, multi-omic integration — and how reproducible the resulting phenogroups are across cohorts. Pay attention to the number and configuration of modeling choices at each pipeline step, since that is where a diversified-option reasoning layer would intervene.

### Search and filter notes
- Search terms used: "HFpEF phenogroup unsupervised clustering methods k-means hierarchical latent class reproducibility"; "HFpEF machine learning pipeline feature selection model selection phenomapping cohorts"; "HFpEF multi-omic integration clustering external validation reproducibility across cohorts"; "comparison clustering algorithms HFpEF subgroups validation".
- Result IDs: pool s_1f5162b9 (45); map attempt (stream-timeout); methods detail via `paperclip grep` on Meijs/Nouraei/O'Sullivan/Versnjak.
- Filter criteria applied: relevance to "methods used to derive HFpEF phenogroups and their reproducibility," with explicit attention to the *number/configuration of modeling choices per pipeline step* (the FoO intervention surface). Curated manually.
- Excluded and why: pure diagnostic-prediction ML (AIM-HFpEF EHR detection, fairness models) where the goal is HFpEF detection not phenogroup derivation — noted but not rows. Protocol/rationale papers (OPTIMISE-HFpEF, STADIA-HFpEF) excluded as non-results.
- Keeper papers:
  - PMC10589200 | Meijs — systematic review, 34 clustering studies (19 HFpEF); "significant heterogeneity in variables and techniques"; the reproducibility meta-finding
  - PMC9033031 | Nouraei — head-to-head of hierarchical vs PAM vs k-prototype; internal validation indices; exposes algorithm/k/distance choices
  - PMC8359985 | Uijl — latent class analysis, externally validated (CHECK-HF)
  - PMC8360080 | Woolley — unsupervised clustering of 363 biomarkers (feature-heavy)
  - PMC10192264 | Kyodo — unsupervised ML, 3 phenogroups
  - PMC12803610 | Versnjak — multi-omics integration, deep phenotyping, pre-symptomatic subgroups
  - med_0981ca997369 | O'Sullivan — multimodal ML (genomic+proteomic), 90+ loci, causal-vs-noncausal, 11 targets
  - med_07d52075716b | Brown — AI-enabled EHR phenogrouping, reproducible 4 groups + trajectories
  - arx_2408.00200 | UnPaSt — unsupervised biclustering of omics (generic, cross-dataset method)
  - PMC9244058 | Heinzel & Shah — review "The future of HFpEF" (Herz); frames methods of sub-phenotyping, ML phenomapping approaches, and their **pitfalls** — the canonical Shah methods/framework reference for this SQ
  - med_9351c9a5757d | Hyson/Kao — LCA on echo features (RELAX) yields structural phenotypes with distinct biomarker profiles — an example of latent-class phenomapping bridging imaging and biomarkers (also SQ1)

### Methods table

| Study | Method class | Input features & modalities | Model-selection / pipeline choices exposed | Reproducibility / external validation | Population & HFpEF definition | Reported limitations | DOI/PMID |
|---|---|---|---|---|---|---|---|
| Meijs 2023 (systematic review) | Review of unsupervised clustering across EF spectrum | 34 studies (19 HFpEF); mixed clinical/echo/biomarker variables | Surveys the *space* of choices: variable selection, algorithm, cluster number, validation — finds them inconsistent across studies | Meta-level: 149/165 described clusters; **"significant heterogeneity in variables and techniques"**; few externally validated; calls for transparency | Pooled HF (EF spectrum), definitions vary | Cross-study comparison "difficult"; transparency/validation gaps | PMC10589200 |
| Nouraei 2022 | Clustering algorithm comparison (hierarchical vs PAM vs k-prototype) | Clinical + echo variables | **Explicitly enumerates**: 3 algorithms, distance metric, k via silhouette/connectivity/Dunn indices | Internal validation indices; PAM selected (6 subgroups); no external cohort | HFpEF, LVEF ≥50% | Single-cohort; choice of indices drives k | PMC9033031 |
| Uijl 2021 | Latent class analysis | Clinical variables/comorbidities | Class number selection, variable set, model fit criteria | **External** (SwedeHF→CHECK-HF) | SwedeHF n=6909 + 2153; LVEF ≥50% | LCA assumptions; clinical-only (no omics) | PMC8359985 |
| Woolley 2021 | Unsupervised cluster analysis (biomarker-driven) | 363 circulating biomarkers | Feature-heavy: 363-marker input, dimensionality reduction, algorithm, k | Internal only; not externally validated | n=429 HFpEF; LVEF ≥45/50% | High-dimensional, single cohort | PMC8360080 |
| Kyodo 2023 | Unsupervised ML clustering | Clinical/echo features | Algorithm, k, feature set | Internal (Japanese cohort); no external | HFpEF, LVEF ≥50% | Single-center, derivation | PMC10192264 |
| Versnjak 2025 | Multi-omics integration + ML phenotyping | Clinical + molecular (multi-omics) | **Many**: omics-integration method, feature selection, model, detection threshold for pre-symptomatic cases | Internal; identifies pre-symptomatic high-risk subgroups | HFpEF + at-risk; LVEF per cohort | Integration choices under-justified; validation early | PMC12803610 |
| O'Sullivan 2026 | Multimodal ML (genomic + proteomic) | GWAS + plasma proteomics (SomaScan-scale) | **Very many**: modality weighting, causal inference (MR) vs association, locus prioritization, target ranking | Large-scale; distinguishes causal vs non-causal proteins; 90+ loci, 11 targets | Population/biobank-scale HFpEF probability | Pipeline opacity; many tunable steps | 10.64898/2026.02.07.26345811 |
| Brown 2025 | AI-enabled EHR phenogrouping | EHR (structured longitudinal) | Algorithm, feature engineering, trajectory modeling | Emphasizes **reproducible** 4 groups; early vs end-stage trajectories | EHR HFpEF; LVEF ≥50% | EHR bias; label/feature choices | 10.1101/2025.06.09.25329306 |
| UnPaSt (Hartung 2024) | Unsupervised biclustering of omics | Multi-omics (disease-agnostic) | Biclustering hyperparameters, gene/sample thresholds, integration | Tested across multiple omics datasets; recovers known subtypes | Generic (not HFpEF-specific) | Not HFpEF-validated; method paper | arx_2408.00200 |

### Paragraph answer
The methods landscape is dominated by unsupervised clustering of clinical/echo variables (k-means, hierarchical, PAM, latent class analysis), with a fast-growing tail of multi-omic-integration and multimodal-ML pipelines — and its defining feature is *under-constrained methodological heterogeneity*. Meijs's systematic review is the load-bearing evidence: across 34 clustering studies (19 in HFpEF) there is "significant heterogeneity in variables and techniques," few studies externally validate, and the review explicitly flags poor transparency, so the ~9 recurring clusters it catalogs are not a settled taxonomy. Reproducibility, where attempted, is the exception rather than the rule: Uijl's latent-class clusters externally replicate (SwedeHF→CHECK-HF) and BECAME's lipidomic phenogroups replicate cross-cohort, but most influential studies (Woolley's 363-biomarker clustering, Kyodo, the multi-omic pilots) report internal validation only. Critically for the FoO objective, every step of these pipelines hides a fork with many defensible options that are typically fixed by convention rather than justified: variable/feature selection, scaling, distance metric, clustering algorithm, the number of clusters (silhouette vs Dunn vs dendrogram, as Nouraei makes explicit by comparing three algorithms that yield different k), omics-integration strategy, and — in O'Sullivan's multimodal genomic-proteomic pipeline — modality weighting, causal-vs-associational filtering, and target prioritization. Nouraei's head-to-head (PAM vs hierarchical vs k-prototype giving different subgroup structures) and O'Sullivan's many-stage causal pipeline are the clearest demonstrations that HFpEF phenomapping carries a large, largely unexplored option space at each node — exactly the surface a diversified-option reasoning layer is designed to enumerate.

### Synthesis bullets
- **Dominant methods:** unsupervised clustering (k-means/hierarchical/PAM) and LCA on clinical+echo variables; multi-omic integration and multimodal ML are the growth area.
- **Reproducibility is weak and inconsistent:** only a minority externally validate (Uijl, BECAME); Meijs documents pervasive heterogeneity in variables/techniques and poor transparency — the field has no settled phenogroup taxonomy.
- **The FoO intervention surface is large and explicit:** feature selection, scaling, distance metric, algorithm, cluster-number criterion, omics-integration method, causal-vs-associational filtering, target ranking — each a fork usually fixed by convention. Nouraei (algorithm choice changes k) and O'Sullivan (many-stage multimodal pipeline) are the sharpest examples.
- **Best extension targets are the multi-omic/multimodal pipelines** (O'Sullivan, Versnjak, BECAME, UnPaSt) where the number of under-justified modeling choices is highest.
- **Note:** UnPaSt is a disease-agnostic method (not HFpEF-validated) — a method to *apply*, not an HFpEF result to extend.

### Confidence read
- **Evidence quality:** High for the descriptive claim (methods are heterogeneous, mostly internally validated — Meijs is a registered systematic review); moderate for any specific phenogroup scheme's reproducibility.
- **Direction of evidence:** Strongly consistent — phenogroups are not reproducible across cohorts as a rule, and pipelines carry many unjustified choices.
- **Key uncertainty:** Which modeling-choice nodes most affect downstream cluster stability/clinical utility — largely untested, and itself an argument for option-enumeration.

---

## Sub-Question 5: Ranked candidate preprints to extend with a Flow-of-Options layer

**Scope:** Using the landscape established in SQ1–SQ4, produce a ranked list of 5–10 candidate preprints in HFpEF biomarker stratification that are strong candidates to extend with a Flow-of-Options-style diversified-option reasoning layer. Prioritize preprints (arXiv / medRxiv / bioRxiv) over published papers where possible. Rank by extension fit: preprints with feature-selection-heavy phenomapping, multi-omic pipelines with many modeling choices, or AutoML-adjacent stratification work score higher, since that is where enumerating and exploring a diverse option space plausibly adds value. One row = one candidate preprint.

### Search and filter notes
- Search terms used: SQ5 was **not searched in a vacuum** — candidates were drawn from the SQ1–SQ4 keeper sets and filtered to preprints (arXiv/medRxiv/bioRxiv). Supplementary check confirmed the FoO paper itself is in-corpus (arx_2502.12929, Nair/Trase/Kim, arXiv 2025-02-18).
- Result IDs: candidates sourced from s_23f40c67, s_b754ff67 (SQ1), s_1f5162b9 (SQ4), s_65fb58c0/s_230576e7 (SQ3); preprint DOIs from `paperclip cat` meta.json.
- Filter criteria applied: **extension fit = number/diversity of exposed, under-justified modeling choices where option-enumeration adds value** (per Constraints), NOT biomarker quality alone. Preprints preferred. Multi-omic / multimodal / feature-selection-heavy / AutoML-adjacent pipelines score highest; fixed single-path pipelines score low even if rigorous.
- Excluded and why (strong-but-non-extendable, see synthesis): Uijl 2021 (PMC8359985) — methodologically strong & externally validated, but a **fixed single-path LCA** and already *published*, few option-nodes to diversify; suPAR-TOPCAT (PMC12719802) — single-biomarker, fixed analysis, published; Di Spigno / Baratto / Bayes-Genis — reviews/meta-analyses, no pipeline; UnPaSt (arx_2408.00200) and LOTUS (arx_2510.07569) — generic AutoML/biclustering *methods* (the kind of tool a FoO layer would orchestrate), not HFpEF stratification results to extend.
- Keeper papers (candidate preprints):
  - med_0981ca997369 | O'Sullivan 2026 — multimodal genomic+proteomic ML; many causal/modality/prioritization choices
  - med_8004d82c9276 | BECAME 2026 — lipidomic phenogroups; LASSO feature selection + hierarchical clustering + RF cross-cohort classifier
  - med_6891987272dd | Raza 2025 (PH-HFpEF) — k-means integrating iCPET functional axis + clinical + transcriptomics
  - bio_5d87948b83e1 | Allerton 2025 — 4-layer multi-omics integration (cardiometabolic HFpEF; preclinical)
  - bio_65b01df68651 | Binek 2025 — cardiac tissue proteome clustering (4411 proteins → 2 clusters)
  - med_07d52075716b | Brown 2025 — AI EHR phenogrouping, reproducible 4 groups + trajectories

### Candidate preprints table (ranked)

| Rank | Preprint (first author, year) | Venue | Core claim / contribution | Method & pipeline (modeling choices exposed) | Data / cohort | Extension opportunity (where FoO adds value) | Gap / limitation it leaves open | Extension-fit rationale | DOI / preprint ID |
|---|---|---|---|---|---|---|---|---|---|
| 1 | O'Sullivan 2026 | medRxiv | Multimodal ML maps the genomic+proteomic architecture of HFpEF; 90+ novel loci, distinguishes causal vs non-causal proteins, prioritizes 11 therapeutic targets | **Highest option density**: modality weighting (genomic vs proteomic), feature/locus selection, causal-inference (MR) vs association filtering, target prioritization & ranking, model class — each a fork fixed by convention | Biobank/population-scale GWAS + plasma proteomics | FoO can enumerate alternative causal-filtering, modality-fusion, and target-ranking options and compare the resulting target sets — directly the AutoML/therapeutic-chemistry regime FoO was demonstrated on | No within-HFpEF *subphenotype* clustering or treatment-response link; causal pipeline opaque | Most modeling nodes of any candidate; preprint; spans SQ1(omic biomarkers)+SQ4(multimodal pipeline); aligns with FoO's demonstrated tabular+therapeutic use | 10.64898/2026.02.07.26345811 |
| 2 | BECAME-HF (Hussin/Menghoum) 2026 | medRxiv | Plasma lipidomics identifies 3 HFpEF phenogroups incl. a high-risk multisystem signature; 10-lipid minimal signature | Feature-selection-heavy: 235→10 lipids via **LASSO resampling (>50% selection freq)**, hierarchical clustering, ridge score, **RF cross-cohort classifier**; choices at scaling, k, feature threshold, classifier | Belgian (n=177) + Canadian (n=177); NP-based HFpEF | FoO can enumerate feature-selection strategies, cluster-number criteria, and classifier options, testing which preserve the externally-validated B1 high-risk group — a built-in reproducibility test | High-risk B1 underrepresented in validation cohort; LVEF/confirmation under-reported | Externally validated (rare), feature-selection-heavy, preprint; spans SQ1+SQ3(prognosis)+SQ4 — strongest *clustering* candidate | 10.64898/2026.03.31.26349865 |
| 3 | Raza 2025 (PH-HFpEF) | medRxiv | Multimodal characterization of a high-risk PH-HFpEF phenogroup with RV dysfunction (vascular mechanics + transcriptomics) | k-means integrating **functional axis (iCPET hemodynamics) + clinical + myocardial transcriptomics**; choices at variable inclusion, integration, k | n=42 PH-HFpEF (+25 pre-capillary PH) | Uniquely links the SQ2 **functional axis** to SQ1 omics — FoO can explore which functional/omic feature combinations and integration schemes define the high-risk RV group | Very small N; derivation only | Directly addresses the SQ2 biomarker→function mapping gap; multimodal; preprint | 10.1101/2025.05.15.25327467 |
| 4 | Allerton 2025 | bioRxiv | Multi-omics integration reveals a skeletal-muscle metabolic myopathy in cardiometabolic HFpEF | **4-layer omics** (transcriptomics/proteomics/metabolomics/lipidomics) integration; many DE thresholds, enrichment, integration choices | ZSF1-obese rat model (preclinical) | FoO can enumerate omics-integration and pathway-prioritization options; relevant to the cardiometabolic phenotype that recurs in SQ1/SQ3 | **Preclinical (rat)** — not a patient stratification pipeline; no human cohort | High option density but preclinical lowers translational extension value | 10.64898/2025.12.15.694522 |
| 5 | Binek 2025 | bioRxiv | Cardiac tissue proteomics → two discrete HFpEF molecular signatures (sex-ratio-linked, not sex per se) | Proteome clustering of **4411 proteins → 1684 differential**; choices at protein filtering, clustering, cluster number, upstream-regulator analysis | Multicenter HFpEF/HFrEF ventricular biobank | FoO can diversify feature-filtering and clustering options on a very high-dimensional proteome to test whether 2 clusters is stable vs an artifact of choices | Tissue-based (low throughput, not scalable to stratify living patients); only 2 clusters | Feature-heavy preprint, but tissue modality limits clinical stratification use | 10.64898/2025.12.18.695212 |
| 6 | Brown 2025 | medRxiv | AI-enabled EHR phenogrouping yields reproducible HFpEF groups & early/end-stage trajectories | EHR feature engineering + clustering + trajectory modeling; choices at feature set, algorithm, trajectory model | EHR HFpEF cohort | FoO can enumerate feature-engineering/algorithm options and test trajectory-group reproducibility | Fewer omic/option nodes than 1–4; EHR bias | Reproducibility focus is valuable but option space narrower (structured EHR only) | 10.1101/2025.06.09.25329306 |

### Paragraph answer
Grounded in SQ1–SQ4, the single strongest FoO extension target is **O'Sullivan 2026 (medRxiv, multimodal genomic+proteomic ML of HFpEF)**, because extension fit is governed by the density of exposed, under-justified modeling choices (SQ4's central finding) rather than biomarker quality, and O'Sullivan's pipeline carries the most such forks: modality weighting, causal-vs-associational filtering, locus/feature selection, and therapeutic-target ranking — precisely the AutoML-and-therapeutic-chemistry regime on which FoO was originally demonstrated, so a diversified-option layer can enumerate alternative causal-filter/fusion/ranking paths and compare the resulting target sets. The closest runner-up is **BECAME-HF**, the best *clustering* candidate: it is feature-selection-heavy (LASSO resampling 235→10 lipids, hierarchical clustering, an RF cross-cohort classifier) and, unusually for SQ4, externally validated — which makes it ideal for using FoO to enumerate feature-selection and cluster-number options and test which choices preserve the externally-replicated high-risk B1 phenogroup (a built-in reproducibility probe). **Raza's PH-HFpEF preprint** ranks third because it uniquely bridges the SQ2 gap — it fuses an invasive *functional* axis (iCPET) with transcriptomics via k-means — making it the natural place to let FoO explore which function×omic feature combinations define the high-risk RV phenotype, though its tiny N caps confidence. The ranking logic throughout is: maximize (exposed modeling-choice count × translational relevance × preprint status), which is why Allerton (option-rich but preclinical) and Binek (option-rich but tissue-based and only two clusters) sit below the human, scalable, multi-node pipelines, and why methodologically excellent but *fixed-pipeline* work (Uijl's externally-validated LCA; the suPAR-TOPCAT analysis) is explicitly excluded as strong-but-non-extendable.

### Synthesis bullets
- **Top candidate (O'Sullivan) beats the field on option density**: its multimodal causal pipeline has more independent, convention-fixed forks (modality fusion, MR vs association, locus/target ranking) than any clustering paper, matching FoO's demonstrated AutoML + therapeutic-target regime; BECAME is the strongest clustering alternative and adds an external-validation reproducibility test FoO can exploit.
- **Strong-but-NON-extendable, explicitly excluded:** Uijl 2021 (externally-validated LCA, but a single fixed path with few option-nodes, and published); suPAR-TOPCAT (single biomarker, fixed analysis); reviews/meta-analyses (Baratto, Di Spigno, Bayes-Genis). UnPaSt/LOTUS are generic *methods* a FoO layer would orchestrate, not HFpEF results to extend.
- **The candidate pool is preprint-RICH** (medRxiv/bioRxiv heavily represented: O'Sullivan, BECAME, Raza, Allerton, Binek, Brown) — the SQ5 preprint-bias is satisfiable without padding; this contrasts with the *closed-access* gap noted in cross-cutting observations (the foundational published canon — Shah 2015 phenomapping, Borlaug hemodynamics — is absent from corpus, but the cutting-edge methods work is precisely in preprints).
- **Best-aligned extension theme:** the cardiometabolic/obese HFpEF phenotype recurs as biomarker-rich (SQ1), the one phenotype with predictive treatment signal (SQ3), and methods-heavy (SQ4) — candidates touching it (O'Sullivan targets, BECAME B3, Allerton, Raza) are the most fertile FoO ground.

### Confidence read
- **Evidence quality:** Moderate-high for the ranking *logic* (directly derived from SQ4's documented option-space and SQ3's prognostic/predictive split); moderate for individual candidate internals (preprints, some not yet peer-reviewed; small N for Raza).
- **Direction of evidence:** Consistent — multimodal/multi-omic preprints with many exposed choices are the clear extension targets; fixed-pipeline work is not.
- **Key uncertainty:** Whether O'Sullivan's pipeline exposes its choice-points reproducibly enough to instrument (preprint detail-limited); and whether BECAME's external validation is robust enough that FoO-driven option search would meaningfully change the high-risk phenogroup.

---

## Cross-cutting observations

- **Prognostic ≠ predictive ≠ functional, and the three rarely connect.** SQ1 produces biomarker-separable subphenotypes, SQ2 produces well-validated functional axes, SQ3 shows clusters are prognostic but seldom predictive — yet almost no study links a biomarker signature to an *invasive functional* axis (Raza's PH-HFpEF and R. Shah's exercise-proteomics pilot are the rare exceptions). The biomarker→function map is the field's clearest white space.
- **The cardiometabolic/obese phenotype is the connective tissue across all SQs:** biomarker-rich (lipidomics/metabolomics/inflammation, SQ1), the one phenotype with a predictive treatment signal (semaglutide/SGLT2i, SQ3), peripherally-limited on exercise (SQ2), and methods-heavy (SQ4). It is the most fertile ground for an extension target (SQ5).
- **Conflict — definition heterogeneity undermines comparability:** LVEF cutoffs vary (≥45% in CATHGEN/Siggins/STEP vs ≥50% in most), confirmation ranges from echo-only to invasive PCWP, and some "HFpEF" cohorts are diagnosis-vs-control while others are within-HFpEF. Biomarker/phenogroup conclusions that hold under one definition (e.g., obese-T2DM HFpEF, LVEF≥50%, NP-confirmed) may not generalize to NP-negative or invasively-confirmed populations. This directly limits cross-cohort reproducibility (SQ4) and means SQ5 candidates carry their cohort's definition as a hidden modeling choice.
- **Conflict — single markers vs panels:** galectin-3 and ST2 are heavily cited yet repeatedly lose independent discrimination after adjustment (e.g., NS after BMI adjustment in obese-T2DM HFpEF), whereas multi-marker omic panels with explicit clustering carry the subphenotype signal — a recurring tension between legacy biomarkers and omic phenomaps.
- **Notable absence 1 — the foundational closed-access canon is not in corpus:** Shah's 2015 *Circulation* phenomapping paper and most of Borlaug's invasive-hemodynamics work are absent (corpus is PMC-OA + preprints). Shah is represented only via the Heinzel & Shah review (PMC9244058) and Borlaug via the STEP-HFpEF analyses (PMC10504076) rather than his hemodynamics canon. The digest is therefore preprint/OA-weighted — fortuitously aligned with SQ5's preprint bias, but a real coverage gap for the classical literature.
- **Notable absence 2 — no prospective biomarker-cluster-randomized trial.** Every treatment-response claim is post-hoc; no HFpEF trial prospectively randomizes within a biomarker cluster. This is the gap a credible FoO-extended pipeline would ultimately be built to inform.
- **Shah's own framework flags the pitfalls (PMC9244058):** the canonical methods review explicitly warns that data-driven HFpEF subtypes need mechanistic follow-up and are prone to over-interpretation — independent corroboration of SQ4's reproducibility concern and a direct motivation for option-enumeration over single-path phenomapping.

---

## Verification anchors

For load-bearing claims likely to appear in the final brief, anchor to specific lines in source papers.

Format: `paper_id : L<line_number_or_range> : <quoted phrase or specific fact>`

Line numbers are from each paper's `content.lines` (located via `paperclip grep`). NB: the `map` tool's internal `_citations` line numbers were found to be offset from `content.lines`, so all anchors below were re-located by grep against `content.lines`.

**SQ1 — biomarker subphenotype discrimination**
- med_8004d82c9276 : L27 : "we tested the differential survival probabilities of the HFpEF patient clusters" — BECAME lipidomic phenogroups separate survival (high-risk B1 composite HR ~1.98)
- PMC9065816 : L29 : "subjects in Phenogroup 1 were relatively young and had a normal left ventricular (LV) function; subjects in Phenogroup 2 were characterized by functional (diastolic) LV abnormalities…" — HFA-PEFF 4 early-HFpEF phenogroups
- PMC10945015 : L55 : "two OPLS models from the 92 plasma biomarker variables were generated… [for] ECV and MPR" — fibrosis(ECV) vs microvascular(MPR) intra-HFpEF axis split
- PMC10848361 : L65 : "The K-means clustering that produced the optimal number of clusters was K = 3… Feature selection identified 25 variables" — AF-HFpEF 3 phenogroups
- PMC7230638 : L34 : "a ROC analysis was performed… AUC was calculated for sST2, suPAR, GDF-15…" — H-FABP/GDF-15 outperform sST2/suPAR for HFpEF
- med_9351c9a5757d : L11 : "Latent class analysis (LCA) was applied to echocardiographic data… from 216 patients" — RELAX structural phenotypes correspond to distinct biomarkers

**SQ2 — functional axes**
- PMC9715813 : L13 : "Studies reporting pulmonary artery wedge pressure (PAWP) at rest and peak exercise were extracted" — exercise PCWP is the reference-standard axis (meta-analysis)
- PMC11299572 : L12 : "Our cohort of 154 HFpEF patients underwent invasive CPET and were grouped into %PredO2P tertiles" — %predicted peak O2 pulse as functional surrogate / VVR
- PMC12449948 : L10 : "359 subjects undergoing invasive cardiopulmonary exercise testing for heart failure symptoms were enrolled" — chronotropic incompetence cohort (→ HF hosp/CV death)

**SQ3 — prognosis vs predictive**
- PMC8359985 : L18 : "We derived a cluster model from 6909 HFpEF patients from the Swedish Heart Failure Registry (SwedeHF) and externally validated this in 2153 patients" — externally validated 5-cluster prognosis
- PMC7373930 : L62 : "uric acid above median was associated with decreased survival and predicted the composite endpoint… [HR 4.79 (95% CI 1.55–14.82)]" — biomarker prognosis
- PMC12572816 : L19 : "Three distinct HFpEF phenogroups were identified. Phenogroup 1 (n = 815) had the highest burden of metabolic comorbidities" — treatment-response phenomap (SGLT2i/ARNI)
- PMC12719802 : L15 : "While suPAR levels independently predict poor outcomes in HFpEF patients, spironolactone does not modulate this inflammatory pathway" — prognostic ≠ predictive (key)

**SQ4 — methods & reproducibility**
- PMC10589200 : L16 : "34 studies were identified (n = 19 in HFpEF). There was significant heterogeneity in variables and techniques used" — the reproducibility/heterogeneity meta-finding
- PMC8360080 : L21 : "unsupervised cluster analysis using 363 biomarkers from 429 patients with HFpEF" — feature-heavy biomarker clustering (4 subgroups)
- PMC9033031 : L19 : "The hierarchical clustering method… generated six different clusters. The optimal number of clusters was determined by the dendrogram" — cluster number depends on algorithm/criterion (FoO surface)

**SQ5 — top extension candidate**
- med_0981ca997369 : L22 : "Genome-wide and proteomic analyses reveal over 90 novel loci… prioritizing 11 therapeutic targets" — O'Sullivan multimodal genomic+proteomic pipeline (rank-1 FoO target)

---

## Bibliography

Compiled via `paperclip sql` (authors/journal/DOI/year) and preprint `meta.json`. Alphabetical by first author. Preprint IDs are Paperclip filesystem IDs.

- Allerton, T. D., et al. (2025). *Multiomics Integration Reveals a Metabolic Myopathy in Cardiometabolic HFpEF.* bioRxiv. DOI 10.64898/2025.12.15.694522 (bio_5d87948b83e1)
- Baratto, C., Caravita, S., Soranna, D., et al. (2022). *Exercise haemodynamics in heart failure with preserved ejection fraction: a systematic review and meta-analysis.* ESC Heart Failure. DOI 10.1002/ehf2.13979 (PMC9715813)
- Bayes-Genis, A., Cediel, G., Domingo, M., et al. (2022). *Biomarkers in Heart Failure with Preserved Ejection Fraction.* Cardiac Failure Review. DOI 10.15420/cfr.2021.37 (PMC9253965)
- Beyer, R. E., Müller, M. L., et al. (2025). *Atrial dysfunction: a contrast-free marker for HFpEF in obese diabetics—insights from comprehensive CMR and serum biomarker analyses.* Cardiovascular Diabetology. DOI 10.1186/s12933-025-02808-3 (PMC12175437)
- Binek, A., Janssens, J. V., et al. (2025). *Multicenter HFpEF study identifies sex disparity linked with two discrete cardiac proteomic signatures.* bioRxiv. DOI 10.64898/2025.12.18.695212 (bio_65b01df68651)
- Borlaug, B. A., Kitzman, D. W., Davies, M. J., et al. (2023). *Semaglutide in HFpEF across obesity class and by body weight reduction (STEP-HFpEF).* Nature Medicine. DOI 10.1038/s41591-023-02526-x (PMC10504076)
- Bosanac, J., Straus, L., Novaković, M., et al. (2022). *HFpEF and Atrial Fibrillation: The Enigmatic Interplay of Dysmetabolism, Biomarkers, and Vascular Endothelial Dysfunction.* Disease Markers. DOI 10.1155/2022/9539676 (PMC9626230)
- Brown, S., Soltani, F., Wu, J., et al. (2025). *Artificial Intelligence Enabled Phenogrouping of HFpEF Depicts Early and End-Stage Trajectories.* medRxiv. DOI 10.1101/2025.06.09.25329306 (med_07d52075716b)
- Chowdhury, M. A., Squires, J., Systrom, D. M., Waxman, A. B. (2025). *Impact of Patient Positioning on Hemodynamic Assessment: Supine vs Upright Right Heart Catheterization in Pulmonary Hypertension and HFpEF.* medRxiv. DOI 10.1101/2025.02.24.25322825 (med_6da399156fea)
- Dattani, A., Brady, E. M., Kanagala, P., et al. (2024). *Is atrial fibrillation in HFpEF a distinct phenotype? Insights from multiparametric MRI and circulating biomarkers.* BMC Cardiovascular Disorders. DOI 10.1186/s12872-024-03734-0 (PMC10848361)
- Di Spigno, F., Dall'Ospedale, V., Gerra, L., et al. (2025). *Cardiopulmonary Exercise Testing and HFpEF: Diagnostic and Therapeutic Perspectives.* Healthcare. DOI 10.3390/healthcare13233098 (PMC12692155)
- Downie, C. G., Shearer, J. J., Kuku, K. O., et al. (2025). *Molecular Phenogroups in Heart Failure: Large-Scale Proteomics in a Population-Based Cohort.* Circulation: Genomic and Precision Medicine. DOI 10.1161/CIRCGEN.124.004953 (PMC12320929)
- El Shaer, A., Garcia-Arango, M., Abed, A., et al. (2025). *Breaking down the recovery of O2 pathway: Peripheral extraction recovery pattern defines exercise capacity and clinical outcomes.* Physiological Reports. DOI 10.14814/phy2.70337 (PMC11994855)
- Hage, C., Michaëlsson, E., Kull, B., et al. (2020). *Myeloperoxidase and related biomarkers are suggestive footprints of endothelial microvascular inflammation in HFpEF (KaRen).* ESC Heart Failure. DOI 10.1002/ehf2.12700 (PMC7373930)
- Hartung, M., Maier, A., Burankova, Y., et al. (2024). *UnPaSt: unsupervised patient stratification by biclustering of omics data.* arXiv:2408.00200 (arx_2408.00200)
- Heinzel, F. R., & Shah, S. J. (2022). *The future of heart failure with preserved ejection fraction* (review). Herz. (PMC9244058)
- Henkens, M. T. H. M., van Ommen, A.-M., Remmelzwaal, S., et al. (2022). *The HFA-PEFF score identifies 'early-HFpEF' phenogroups associated with distinct biomarker profiles.* ESC Heart Failure. DOI 10.1002/ehf2.13861 (PMC9065816)
- Huang, K.-C., Lin, T.-T., Lin, L.-C., et al. (2025). *Right Ventricular Myocardial Work Predicts Pulmonary Capillary Wedge Pressure Rise During Exercise in Heart Failure.* JACC: Advances. DOI 10.1016/j.jacadv.2025.101905 (PMC12246590)
- Hussin, J., Menghoum, N., Forest, A., et al. (2026). *Lipidomics Identifies HFpEF Phenogroups and a High-Risk Metabolic Signature (BECAME-HF).* medRxiv. DOI 10.64898/2026.03.31.26349865 (med_8004d82c9276)
- Hutten, C. G., Tekumulla, A., Ismail, A., et al. (2025). *Soluble urokinase plasminogen activator receptor and outcomes in HFpEF: a TOPCAT ancillary study.* ESC Heart Failure. DOI 10.1002/ehf2.15423 (PMC12719802)
- Hyson, P. R., & Kao, D. P. (2024). *Biomarkers Correspond with Echocardiographic Phenotypes in HFpEF: A Secondary Analysis of the RELAX Trial.* medRxiv. DOI 10.1101/2024.04.30.24306660 (med_9351c9a5757d)
- Jirak, P., Pistulli, R., Lichtenauer, M., et al. (2020). *Expression of the Novel Cardiac Biomarkers sST2, GDF-15, suPAR, and H-FABP in HFpEF Patients Compared to ICM, DCM, and Controls.* Journal of Clinical Medicine. DOI 10.3390/jcm9041130 (PMC7230638)
- Kagami, K., Obokata, M., Harada, T., et al. (2022). *Diastolic Filling Time, Chronotropic Response, and Exercise Capacity in HFpEF with Sinus Rhythm.* JAHA. DOI 10.1161/JAHA.121.026009 (PMC9333393)
- Kyodo, A., Kanaoka, K., Keshi, A., et al. (2023). *Heart failure with preserved ejection fraction phenogroup classification using machine learning.* ESC Heart Failure. DOI 10.1002/ehf2.14368 (PMC10192264)
- Li, J. P., Slocum, C., Sbarbaro, J., et al. (2024). *Percent Predicted Peak Exercise Oxygen Pulse Provides Insights Into Ventricular-Vascular Response and Prognosticates HFpEF.* JACC: Advances. DOI 10.1016/j.jacadv.2024.101101 (PMC11299572)
- Li, R., Liu, Y., Zhao, Z., et al. (2025). *Machine learning-based phenotyping and assessment of treatment responses in HFpEF.* eClinicalMedicine. DOI 10.1016/j.eclinm.2025.103462 (PMC12572816)
- Lin, T.-T., Chen, T.-Y., Cheng, J.-F., et al. (2025). *Chronotropic Incompetence and Cardiovascular Outcomes in Patients With HFpEF.* JAHA. DOI 10.1161/JAHA.124.037290 (PMC12449948)
- Meijs, C., Handoko, M. L., Savarese, G., et al. (2023). *Discovering Distinct Phenotypical Clusters in Heart Failure Across the Ejection Fraction Spectrum: a Systematic Review.* Current Heart Failure Reports. DOI 10.1007/s11897-023-00615-z (PMC10589200)
- Morfino, P., Aimo, A., Castiglione, V., et al. (2022). *Biomarkers of HFpEF: Natriuretic Peptides, High-Sensitivity Troponins and Beyond.* Journal of Cardiovascular Development and Disease. DOI 10.3390/jcdd9080256 (PMC9409788)
- Nair, L., Trase, I., & Kim, M. (2025). *Flow-of-Options: Diversified and Improved LLM Reasoning by Thinking Through Options.* arXiv:2502.12929 (arx_2502.12929) — the method being extended
- Nouraei, H., Nouraei, H., & Rabkin, S. W. (2022). *Comparison of Unsupervised Machine Learning Approaches for Cluster Analysis to Define Subgroups of HFpEF with Different Outcomes.* Bioengineering. DOI 10.3390/bioengineering9040175 (PMC9033031)
- O'Sullivan, J. W., Yun, T., Cai, R., et al. (2026). *Multimodal Machine Learning Reveals the Genomic and Proteomic Architecture of HFpEF.* medRxiv. DOI 10.64898/2026.02.07.26345811 (med_0981ca997369)
- Prokopidis, K., Irlik, K., Ispoglou, T., et al. (2025). *Exercise capacity in heart failure: a systematic review and meta-analysis of HFrEF and HFpEF disparities in VO2 peak and 6-minute walking distance.* European Heart Journal Open. DOI 10.1093/ehjopen/oeaf055 (PMC12202100)
- Raza, F., Gregorich, Z. R., Freeman, J., et al. (2025). *Multimodal Characterization of High-risk PH-HFpEF phenogroup with Right Ventricular Dysfunction: Vascular Mechanics and Myocardial Transcriptomics.* medRxiv. DOI 10.1101/2025.05.15.25327467 (med_6891987272dd)
- Regan, J. A., Truby, L. K., Tahir, U. A., et al. (2022). *Protein biomarkers of cardiac remodeling and inflammation associated with HFpEF and incident events.* Scientific Reports. DOI 10.1038/s41598-022-24226-1 (PMC9684116)
- Sarullo, F. M., Fazio, G., Brusca, I., et al. (2010). *Cardiopulmonary Exercise Testing in Patients with Chronic Heart Failure: Prognostic Comparison from Peak VO2 and VE/VCO2 Slope.* The Open Cardiovascular Medicine Journal. DOI 10.2174/1874192401004010127 (PMC2908890)
- Schulz, A., Mittelmeier, H., Wagenhofer, L., et al. (2024). *Assessment of the cardiac output at rest and during exercise stress using real-time cardiovascular magnetic resonance imaging in HFpEF-patients.* International Journal of Cardiovascular Imaging. DOI 10.1007/s10554-024-03054-6 (PMC11052864)
- Shah, S. J., Sharma, K., Borlaug, B. A., Butler, J., et al. (2024). *Semaglutide and diuretic use in obesity-related HFpEF: a pooled analysis of the STEP-HFpEF and STEP-HFpEF-DM trials.* European Heart Journal. DOI 10.1093/eurheartj/ehae322 (PMC11400859)
- Siggins, C., Pan, J. A., Löffler, A. I., et al. (2024). *Cardiometabolic biomarker patterns associated with cardiac MRI defined fibrosis and microvascular dysfunction in HFpEF.* Frontiers in Cardiovascular Medicine. DOI 10.3389/fcvm.2024.1334226 (PMC10945015)
- Tamaki, S., Sotomi, Y., Nagai, Y., et al. (2024). *Relationship of interleukin-16 with different phenogroups in acute heart failure with preserved ejection fraction.* ESC Heart Failure. DOI 10.1002/ehf2.14808 (PMC11287331)
- Uijl, A., Savarese, G., Vaartjes, I., et al. (2021). *Identification of distinct phenotypic clusters in heart failure with preserved ejection fraction.* European Journal of Heart Failure. DOI 10.1002/ejhf.2169 (PMC8359985)
- Versnjak, J., Kuehne, T., Fahjen, P., et al. (2025). *Deep phenotyping of heart failure with preserved ejection fraction through multi-omics integration.* European Journal of Heart Failure. DOI 10.1002/ejhf.70041 (PMC12803610)
- Verwerft, J., Verbrugge, F. H., Claessen, G., et al. (2022). *Exercise Systolic Reserve and Exercise Pulmonary Hypertension Improve Diagnosis of HFpEF.* Frontiers in Cardiovascular Medicine. DOI 10.3389/fcvm.2022.814601 (PMC8863971)
- Verwerft, J., Foulkes, S., Bekhuis, Y., et al. (2024). *The Oxygen Cascade According to HFpEF Likelihood.* JACC: Advances. DOI 10.1016/j.jacadv.2024.101039 (PMC11313028)
- Wolter, J. S., Schulz, A., Lange, T., et al. (2025). *Exercise-induced out-of-proportion increase in afterload and impaired right ventricular contractile reserve in HFpEF.* ESC Heart Failure. DOI 10.1002/ehf2.70007 (PMC12719814)
- Woolley, R. J., Ceelen, D., Ouwerkerk, W., et al. (2021). *Machine learning based on biomarker profiles identifies distinct subgroups of heart failure with preserved ejection fraction.* European Journal of Heart Failure. DOI 10.1002/ejhf.2144 (PMC8360080)
