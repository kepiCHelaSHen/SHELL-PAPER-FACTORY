# INIT — GAME THEORY OF VACCINE HESITANCY: FREE-RIDING AND HERD IMMUNITY (v3 — ASSAY-Integrated)
# EXECUTE IMMEDIATELY. Do not summarize, analyze, or ask questions.
# Read the INPUTS below, then execute the SETUP SEQUENCE step by step.
# Load prompts/00_init.md for the setup procedure, then run it with these inputs.
# This is not a document to review — it is a set of instructions to follow NOW.

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: Game Theory of Vaccine Hesitancy: Free-Riding, Herd Immunity Thresholds, and the Nash Equilibrium of Incomplete Coverage
SLUG: VACCINE_GAME_2026
AUTHOR: James P Rice Jr.
TARGET_VENUE: Journal of Health Economics
PIPELINE: PAPER

PROBLEM:
Models vaccination as a public goods game where rational individuals weigh
private vaccination costs against infection risk, which depends on population
coverage. Derives the Nash equilibrium coverage level p* and shows it is
generically below the herd immunity threshold 1-1/R0 for any disease with
R0 > 1 and positive vaccination cost. The free-rider gap (Delta = herd threshold
- observed coverage) is a measurable quantity. Uses WHO/UNICEF coverage data
for measles, pertussis, polio, and HPV to calibrate the model against real
gaps. The central result: voluntary vaccination alone cannot achieve herd
immunity as long as vaccination carries any private cost, no matter how small.

FROZEN_SPEC_PARAMETERS:

PARAMETER: Nash equilibrium coverage
VALUE: p* = 1 - 1/R0 - c/b (in simple linear-cost model) or interior solution
       to dU/dp = 0 where U(p) = -(1-p)*I(P) - p*c
UNIT: proportion [0,1]
TOLERANCE: functional form — the specific formula depends on the infection
           probability function I(P)
SOURCE: Bauch & Earn 2004; Geoffard & Philipson 1997
NOTES: p* < 1-1/R0 whenever c > 0 and R0 > 1. This is the free-rider gap.
DRIFT_RISK: HIGH — Author may derive p* = 1-1/R0 exactly, eliminating the gap

PARAMETER: Basic reproduction number R0
VALUE: Measles 12-18 (central: 15), Pertussis 12-17 (central: 14.5),
       Polio 5-7 (central: 6), HPV 2-6 (central: 4)
UNIT: dimensionless
TOLERANCE: sensitivity analysis across full range
SOURCE: Anderson & May 1991; Guerra et al. 2017
DRIFT_RISK: LOW — well-established parameters

PARAMETER: Herd immunity threshold
VALUE: 1 - 1/R0 (measles: 93.3%, pertussis: 93.1%, polio: 83.3%, HPV: 75.0%)
UNIT: proportion
TOLERANCE: exact at given R0
SOURCE: Anderson & May 1991
DRIFT_RISK: LOW

PARAMETER: Cost ratio c (vaccination cost / infection cost)
VALUE: Estimated from ASSAY gap data; c in (0,1) for all diseases
UNIT: dimensionless ratio
TOLERANCE: calibrated to match ASSAY-observed gaps
SOURCE: Inferred from ASSAY coverage data
DRIFT_RISK: MEDIUM — Author may assume c rather than calibrate it

MILESTONES:

M1: Game-theoretic framework — define the vaccination game, derive Nash
    equilibrium p*, prove p* < 1-1/R0 for c > 0. Show the free-rider gap
    as an equilibrium phenomenon.

M2: Empirical calibration — use ASSAY coverage data (measles gap 7.9 pp,
    pertussis 6.7 pp, polio -2.4 pp) to calibrate cost ratio c for each
    disease. Confront the polio negative gap explicitly.

M3: Policy analysis — derive conditions under which subsidies, mandates,
    or information campaigns close the gap. Comparative statics on c, R0.

M4: Full paper — Introduction, literature review, model, calibration,
    policy discussion, conclusion.

ORACLE:
The model is valid if and only if:
1. Nash equilibrium p* is correctly derived and shown to be below herd threshold
2. The free-rider gap matches ASSAY-observed gaps within CIs for measles/pertussis
3. The polio negative gap is explained (coverage exceeds threshold due to mandates/subsidies)
4. Policy analysis derives sufficient conditions for gap closure
5. R0 sensitivity analysis spans the full epidemiological range

---

## ASSAY EVIDENCE

### ASSAY Report: VACCINE_COVERAGE (Global Coverage Gaps)
PATH: C:\PROJECTS\ASSAY\reports\VACCINE_COVERAGE_2026-05-15_001\integration_block.yaml
REPORT_ID: ASSAY-VACCINE-COVERAGE-2026-05-15-001
DATA SOURCE: WHO/UNICEF WUENIC 2024; Anderson & May 1991
CONTAINS:
  - Measles gap (Delta): 7.9 pp [95% CI: 6.2, 10.1], N=194 countries
    Method: Bootstrap BCa (10,000 resamples, seed=42)
    Delta = herd_threshold(R0=15) - mean(country_coverage)
  - Pertussis gap (Delta): 6.7 pp [95% CI: 5.0, 8.8], N=194 countries
    Method: Bootstrap BCa (10,000 resamples, seed=42)
    Delta = herd_threshold(R0=14.5) - mean(country_coverage)
  - Polio gap (Delta): -2.4 pp [95% CI: -4.2, -0.1], N=194 countries
    Method: Bootstrap BCa (10,000 resamples, seed=42)
    Delta = herd_threshold(R0=6) - mean(country_coverage)
    NOTE: NEGATIVE — coverage exceeds herd threshold. CI upper bound barely excludes zero.
  - HPV gap (Delta): 22.3 pp [95% CI: 17.9, 27.0], N=132 countries
    Method: Bootstrap BCa (10,000 resamples, seed=42)
    NOTE: HPV R0 highly uncertain (2-6); direction is assumption-dependent
  - Fraction of countries below measles herd threshold: 0.639 [95% CI: 0.569, 0.703]
    (124/194 countries below 93.3%)
  - Population-weighted measles gap: 5.8 pp [95% CI: 2.6, 11.2]
AVAILABLE FIGURES (3):
  - Global gap comparison across diseases
  - Regional measles coverage variation
  - R0 sensitivity analysis for Delta

---

## DOMAIN CONSTRAINTS

The Author MUST enforce these parameter ranges. Any value outside these ranges
is a model error that must be flagged, not silently used.

| Parameter | Valid Range | Justification |
|-----------|------------|---------------|
| p* (Nash coverage) | [0, 1] | Coverage is a proportion. If p* > 1 for any disease, FLAG IT — the model is predicting impossible coverage. This means vaccination cost is negative (subsidy exceeds cost). Do not silently clamp to 1. |
| R0 | R0 > 1 | For R0 <= 1, disease cannot sustain transmission and herd immunity is not relevant |
| Cost ratio c | c in (0, 1) | c=0 means free vaccination (Nash eq = herd threshold). c >= 1 means vaccination cost exceeds infection cost (Nash eq = 0). Both boundary cases must be discussed. |
| Delta (gap) | Can be negative | A negative gap means coverage EXCEEDS herd threshold. Polio Delta = -2.4 pp is negative. This is not an error — it reflects mandates/subsidies pushing coverage above the voluntary equilibrium. The model must explain WHY polio is negative when the free-rider logic predicts positive gaps. |
| Herd threshold | (0, 1) | 1-1/R0 is in (0,1) for R0 > 1. At R0=1: threshold=0. As R0->infinity: threshold->1. |

FLAG CONDITIONS:
- If p* > 1 for any parameter combination: FLAG — do not silently use. Explain.
- If calibrated c < 0 for any disease: FLAG — negative cost means subsidy exceeds cost
- Polio gap is NEGATIVE (-2.4 pp). This is the most important case to explain.
  The voluntary game predicts positive gaps. Polio's negative gap means policy
  interventions (mandates, GAVI subsidies, eradication campaigns) have pushed
  coverage ABOVE the herd threshold. Discuss why this does not invalidate the
  model but rather confirms it: absent mandates, the free-rider gap would appear.

---

## CALIBRATION INSTRUCTIONS

The Author MUST perform these specific model-data comparisons using ASSAY values:

1. PRIMARY CALIBRATION — MEASLES: Compute Nash equilibrium p* for measles
   using R0=15 (herd threshold = 93.3%) and the ASSAY-observed mean coverage
   (93.3% - 7.9% = 85.4%). Solve for the implied cost ratio c that makes
   p* = 85.4%. The free-rider gap Delta = herd threshold - p* should equal
   7.9 pp (ASSAY value). Verify the calibrated c is in (0,1).
   Report: "For measles (R0=15), the ASSAY-observed gap of 7.9 pp [6.2, 10.1]
   implies a cost ratio c = [computed value], meaning vaccination cost is
   [X]% of infection cost."

2. PERTUSSIS CHECK: Repeat for pertussis (R0=14.5, gap=6.7 pp [5.0, 8.8]).
   The pertussis gap should be similar to measles (similar R0). Verify.

3. POLIO — CRITICAL NEGATIVE CASE: The ASSAY polio gap is -2.4 pp [-4.2, -0.1].
   Coverage EXCEEDS the herd threshold. The voluntary game CANNOT produce this.
   The paper MUST explain: "The polio gap is negative because the Global Polio
   Eradication Initiative, national mandates, and GAVI subsidies effectively
   set c <= 0 (vaccination is free or incentivized). When c <= 0, the model
   predicts p* >= 1-1/R0, consistent with the data. Polio is the counterfactual
   that shows what happens when free-rider incentives are eliminated."

4. R0 SENSITIVITY: The ASSAY data notes R0 uncertainty shifts measles Delta
   from 6.3 to 9.1 pp across R0=12-18. Reproduce this sensitivity curve.
   For polio (R0=5-7), Delta ranges from -5.7 to 0.0 pp — at R0=7, the gap
   is approximately zero. Report this boundary.

5. HPV — EXPLORATORY: HPV gap is 22.3 pp [17.9, 27.0] but R0 is highly
   uncertain (2-6). At R0=2.2, Delta sign flips. Present HPV as exploratory,
   not confirmatory.

---

# === STEELMAN REVISION BRIEF ===

KNOWN_DRIFT_RISKS:
- DO NOT invent coverage data. All gaps come from ASSAY-VACCINE-COVERAGE-2026-05-15-001.
- The polio negative gap is the most interesting result. Do NOT ignore it.
  Do NOT treat it as an error. Explain it as evidence that policy can overcome free-riding.
- Do NOT claim the model "predicts" herd immunity thresholds — those are inputs, not outputs.
- Do NOT conflate voluntary and mandatory vaccination. The model applies to
  voluntary settings. Mandates change the game.
- R0 values have ranges, not point estimates. Use the full range in sensitivity.

# === CROSS-PAPER FINDINGS ===

- [F-005] POLICY LANGUAGE OVERSHOOTS MODEL SCOPE — The model shows voluntary
  coverage falls short. It does NOT derive optimal subsidy levels, mandate
  thresholds, or information campaign designs. Scope policy discussion accordingly.

- [F-002] "ILLUSTRATIVE" COMPONENT — The free-rider gap is THE result.
  Do not present it as one of several findings. It is the finding.

- [F-036/F-024] FIGURES CODE-ONLY — Render all figures. Include at minimum:
  Figure 1: Gap comparison across 4 diseases (bar chart with CIs from ASSAY)
  Figure 2: Nash equilibrium p* vs herd threshold as function of c
  Figure 3: R0 sensitivity for each disease

- [F-006] NOTATION — R0 is the basic reproduction number ONLY. Do not reuse
  R for anything else (note: the replication crisis paper uses R for prior odds —
  in THIS paper, use R0 for reproduction number consistently).

- [DE-038] PLACEHOLDER VALUES — Every gap, CI, and R0 must be from ASSAY data.
  No "[computed from model]" placeholders.

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1 — Create project directory (auto-versioned)
Resolve the project directory using auto-versioning:
1. List all existing directories matching C:\PROJECTS\SHELL\papers\VACCINE_GAME_2026_*
2. If none exist: use VACCINE_GAME_2026_[TODAY]_001
3. If some exist: find the highest sequence number, increment by 1
Store as RESOLVED_DIR.

Create RESOLVED_DIR with subdirectories:
  figures/, outputs/, results/raw/, results/final/,
  devlog/, prompts/

### Step 2 — Write CLAUDE.md
  # Game Theory of Vaccine Hesitancy — NORTH STAR

  ## What We Are Building
  A game-theoretic model of vaccination showing the Nash equilibrium coverage
  is generically below herd immunity for voluntary vaccination with positive cost.

  ## The Core Claim
  The free-rider gap (Delta = herd threshold - Nash coverage) is positive for
  any disease with R0 > 1 and c > 0. ASSAY data confirms: measles 7.9 pp,
  pertussis 6.7 pp. Polio is NEGATIVE (-2.4 pp) due to mandates — the exception
  that proves the rule.

  ## ASSAY Data Available
  - VACCINE_COVERAGE_2026-05-15_001: gaps for measles, pertussis, polio, HPV
  USE THESE VALUES. Do not invent coverage data.

  ## Frozen Parameters (quick reference)
  | Parameter | Value | Source |
  |-----------|-------|--------|
  | R0 measles | 15 (range 12-18) | Anderson & May 1991 |
  | R0 pertussis | 14.5 (range 12-17) | Anderson & May 1991 |
  | R0 polio | 6 (range 5-7) | Anderson & May 1991 |
  | Measles gap | 7.9 pp [6.2, 10.1] | ASSAY |
  | Pertussis gap | 6.7 pp [5.0, 8.8] | ASSAY |
  | Polio gap | -2.4 pp [-4.2, -0.1] | ASSAY |

### Step 3 — Write frozen_spec.md
Fill from FROZEN_SPEC_PARAMETERS above. Lock date today.

### Step 4 — Initialize state files
### Step 5 — Copy all prompts from SHELL
### Step 5b — Write run_pipeline.ps1
### Step 6 — Write STATUS.md
### Step 7 — Write remaining required files
### Step 8 — Initialize git
### Step 9 — Print confirmation and hand off

[Follow identical structure to REPLICATION_CRISIS_2026 init for steps 4-9,
 substituting VACCINE_GAME_2026 for the slug throughout.]

---

## HAND OFF — EXECUTE PAPER PIPELINE

DO NOT STOP HERE. The setup is complete. Now you must execute the paper pipeline.

Read prompts/04_paper_orchestrator.md NOW and follow every instruction in it.

YOUR INPUTS:
  PROBLEM: [the full PROBLEM text from the INPUTS section above]
  DATA: ASSAY integration block at:
    - C:\PROJECTS\ASSAY\reports\VACCINE_COVERAGE_2026-05-15_001\integration_block.yaml
    Read this file and use the computed values. Key values:
      Measles gap: 7.9 pp [6.2, 10.1], N=194
      Pertussis gap: 6.7 pp [5.0, 8.8], N=194
      Polio gap: -2.4 pp [-4.2, -0.1], N=194 (NEGATIVE)
      HPV gap: 22.3 pp [17.9, 27.0], N=132 (exploratory)
      Fraction below measles threshold: 0.639 [0.569, 0.703]
      Population-weighted measles gap: 5.8 pp [2.6, 11.2]
  SLUG: VACCINE_GAME_2026
  DRIFT_RISKS: [paste KNOWN_DRIFT_RISKS above]
  FROZEN_SPEC: [pass full frozen_spec.md to Peer Reviewer]

BEGIN NOW. Run M1. Do not ask for confirmation. Execute it. Write the paper.
