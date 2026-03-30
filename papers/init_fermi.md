# INIT — FERMI PARADOX AS A SURVIVAL FUNCTION
# Pre-filled. Ready to run.
# claude --dangerously-skip-permissions papers/init_fermi.md

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: The Fermi Paradox as a Survival Function: What the Silence Implies About Civilizational Hazard Rates
SLUG: fermi_survival_2025
AUTHOR: James P Rice Jr.
TARGET_VENUE: Zenodo preprint — target International Journal of Astrobiology or Acta Astronautica
PIPELINE: PAPER

PROBLEM:
The Drake equation is not a scientific model — it is a multiplication of unknowns that
produces no falsifiable predictions and provides no mechanism for updating on evidence.
Its central failure is structural: it treats the emergence of communicating civilizations
as a product of independent probabilities rather than as a survival process unfolding
over time. This paper replaces the Drake equation with a formal survival analysis
framework. Each term that could end a civilization's communicative window is modeled
as a hazard rate in a continuous-time survival function. The observed silence — zero
confirmed detections across 60+ years of SETI — is treated as a censored observation
and used to derive posterior constraints on the hazard rates. The result is a
falsifiable, updatable model with a brutal punchline: under any parameterization
consistent with the observed silence, the data are most consistent with a dominant
late-stage filter — a civilizational hazard that strikes after technological maturity.
The model quantifies what the silence implies, rather than speculating about what
might explain it.

FROZEN_SPEC_PARAMETERS:

PARAMETER: Observational baseline
VALUE: 0 confirmed detections in 60+ years of SETI observation
UNIT: dimensionless
TOLERANCE: exact — this is the censored data point the model conditions on
SOURCE: Tarter 2001 | The Search for Extraterrestrial Intelligence | ARA&A 39:511-548
NOTES: The silence is not absence of evidence — it is a censored observation in
       the survival analysis sense. The model must treat it formally as such.
DRIFT_RISK: LOW — this fact is not in dispute

PARAMETER: Galaxy age
VALUE: 13.6 Gyr
UNIT: billion years
TOLERANCE: ± 0.1 Gyr
SOURCE: Planck Collaboration 2020 | A&A 641:A6
NOTES: Sets the upper bound on the time domain of the survival function.
DRIFT_RISK: LOW

PARAMETER: Milky Way stellar count (communicating-capable stars)
VALUE: ~10^11
UNIT: stars
TOLERANCE: order of magnitude
SOURCE: Bland-Hawthorn & Gerhard 2016 | ARA&A 54:529-596
NOTES: Used only to set the population baseline. Exact value doesn't drive results —
       the survival function result is robust across an order of magnitude.
DRIFT_RISK: LOW

PARAMETER: SETI sensitivity baseline
VALUE: Kardashev Type I equivalent transmitters detectable within ~100 light-years
SOURCE: Tarter 2001; updated by Enriquez et al. 2017 | ApJ 849:104
NOTES: This scopes what "silence" means. The model must be explicit about what
       the silence rules out vs. what it cannot constrain.
DRIFT_RISK: MEDIUM — LLM prior may overstate SETI coverage

PARAMETER: Survival function form
VALUE: Exponential hazard (constant hazard rate) as baseline; Weibull extension for
       age-dependent hazard (increasing hazard = late filter; decreasing = early filter)
SOURCE: Cox 1972 | Journal of the Royal Statistical Society 34(2):187-220
NOTES: Start with exponential for tractability. Weibull lets you distinguish early
       vs. late filter formally. This is the core methodological contribution.
DRIFT_RISK: HIGH — Author may default to simpler probabilistic framing without
             survival analysis machinery. Must use Cox/Weibull formalism.

PARAMETER: The core result
VALUE: Under exponential hazard, the maximum likelihood hazard rate consistent with
       zero detections implies a mean civilizational communicative lifetime short
       enough to be consistent ONLY with a late-stage filter (post-technological).
SOURCE: Rice [this paper] — derived result
NOTES: This is the punchline. Do not soften it. Derive it formally and state it
       plainly: the silence points to a filter ahead of us, not behind us.
DRIFT_RISK: HIGH — Author may hedge. The Peer Reviewer must enforce the claim if
             the math supports it.

MILESTONES:

M1: Formal model setup — define the survival function framework, hazard rates,
    the censored observation structure. Show why Drake is not a survival model
    and what is lost by treating it as one. Establish notation.

M2: The core derivation — derive the maximum likelihood hazard rate consistent
    with zero detections over the observational baseline. Show the Weibull
    extension distinguishing early vs. late filter formally.

M3: The implication — what does the ML hazard rate imply about where the filter
    is? Derive the result quantitatively. This is the holy shit moment —
    state it as a theorem, not as speculation.

M4: Full paper — Introduction (Drake's failure), Related work (Hart 1975,
    Brin 1983, Hanson 1998, Cirkovic 2018), Discussion (what could update the
    model, AI as a potential late filter, limitations), Conclusion.
    Self-contained Abstract.

ORACLE:
The model is valid if and only if:
1. The survival function is formally defined with explicit hazard rates
2. The censored observation (zero detections) is correctly incorporated via
   the likelihood function, not treated as a simple probability
3. The ML hazard rate is derived analytically, not estimated by intuition
4. The filter location result follows mathematically from M2 — not re-argued
5. The Drake equation critique in the Introduction is precise, not rhetorical

Peer Reviewer must verify: does the late-filter conclusion follow from the math,
or is it asserted? If asserted, REJECT.

KNOWN_DRIFT_RISKS:
- Reverting to Drake equation framing instead of survival analysis
- Treating zero detections as P(detection)=0 instead of a censored observation
- Hedging the late-filter conclusion when the math supports a strong claim
- Conflating the Great Filter (Hanson) with the survival function result —
  these are related but distinct; the paper derives the filter location,
  Hanson assumed it
- Adding speculative sections on specific filter candidates (AI, nuclear war,
  climate) — this paper is formal, not speculative; keep it tight
- Overstating SETI coverage — be precise about what the silence constrains
- Skipping the sensitivity analysis table — M3 must include a table varying
  λ (hazard rate), SETI detection radius, and galaxy age by order of magnitude
  and showing whether the late-filter conclusion holds under each perturbation
- Failing to formally reject competing models — the following must each be
  rejected with a specific formal reason:
    Drake equation: fails because it treats emergence as independent probabilities
      rather than a survival process; cannot incorporate censored observations
    Rare Earth (Hart 1975): assumes early filter; paper must show this is
      inconsistent with the ML hazard rate under the survival model
    Great Filter (Hanson 1998): assumes filter location rather than deriving it;
      paper must show our model derives what Hanson assumed
    Non-Poisson emergence: what if civilization emergence is not memoryless?
      Must address whether Weibull extension handles this or not
    Non-uniform emergence rate: what if emergence rate varies over galactic time?
      Must state whether this is within or outside the model's scope
- Orphan figure references — every figure must have Python/matplotlib code.
  The paper should include at minimum:
    Figure 1: survival function S(t) under exponential and Weibull hazard
    Figure 2: likelihood function L(λ) given zero detections over T years
    Figure 3: filter location posterior (early vs. late filter probability)

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1 — Create project directory
Create D:\EXPERIMENTS\FERMI\ with:
  spec/, state/, outputs/, results/raw/, results/validated/, results/final/,
  devlog/, src/, papers/, papers/fermi_survival_2025/, papers/fermi_survival_2025/figures/,
  prompts/

### Step 2 — Write CLAUDE.md
  # The Fermi Paradox as a Survival Function — NORTH STAR

  ## What We Are Building
  A formal survival analysis model replacing the Drake equation. The silence
  is a censored observation. The math points to a late-stage filter.

  ## The Core Claim
  Under exponential hazard, zero detections over 60 years implies a mean
  communicative lifetime consistent only with a dominant post-technological filter.
  This is derived, not speculated.

  ## Frozen Parameters (quick reference)
  | Parameter | Value | Source |
  |-----------|-------|--------|
  | Detections | 0 (censored) | Tarter 2001 |
  | Galaxy age | 13.6 Gyr | Planck 2020 |
  | Hazard model | Exponential + Weibull | Cox 1972 |
  | Core result | Late-stage filter | Rice [this paper] |

  ## Critical Enforcements
  - Survival function formalism — not Drake probability math
  - Zero detections = censored observation, not P=0
  - Late-filter conclusion must be derived, not asserted
  - No speculation about specific filter candidates

### Step 3 — Write spec/frozen_spec.md
Fill from FROZEN_SPEC_PARAMETERS above. Lock date today.
Locked by: James P Rice Jr.

### Step 4 — Initialize state files
state/state_vector.md — TURN: 0, MILESTONE: M1, MODE: INIT
state/innovation_log.md — header with project name and timestamp
state/dead_ends.md — header with project name

### Step 5 — Copy all prompts from SHELL
Copy from D:\EXPERIMENTS\SHELL\prompts\ into D:\EXPERIMENTS\FERMI\prompts\:
  04_paper_orchestrator.md
  05_author.md
  06_peer_reviewer.md
  07_editor.md
  run_milestone.md
Do NOT copy 00_init.md — SHELL-level only.

Also write prompts/turn_prompts_log.md:
  # TURN PROMPTS LOG — fermi_survival_2025
  # Every exact prompt logged here. Required for reproducibility.
  [No entries yet. First entry written at Turn 1 M1.]

### Step 5b — Write run_pipeline.ps1

Write run_pipeline.ps1 in the project root (D:\EXPERIMENTS\FERMI\) with
the slug set to "fermi_survival_2025". Use the template from
D:\EXPERIMENTS\SHELL\prompts\00_init.md Step 15, replacing [SLUG] with
fermi_survival_2025 and [SLUG] paths with FERMI.

### Step 6 — Write STATUS.md
Phase: INIT → PAPER PIPELINE
Turn: 0
What Is Done: Scaffolded. Spec locked.
What Is Next: Author writes M1 (survival function setup, Drake critique).

### Step 7 — Write remaining required files

Write README.md:
  # The Fermi Paradox as a Survival Function
  **Author:** James P Rice Jr.
  **Target:** International Journal of Astrobiology / Acta Astronautica
  **Status:** In progress
  ## What This Is
  A formal survival analysis model replacing the Drake equation.
  Zero detections = censored observation. ML hazard rate implies late-stage filter.
  ## How to Run
  claude --dangerously-skip-permissions prompts/04_paper_orchestrator.md

Write CHAIN_PROMPT.md:
  # CHAIN PROMPT — Fermi Survival Paper | THIS FILE WINS ALL CONFLICTS
  Name: The Fermi Paradox as a Survival Function
  Author: James P Rice Jr.
  Core claim: Under exponential hazard, zero detections implies a dominant
  post-technological filter. Derived, not speculated.
  Pipeline: PAPER — multi-model triangulation, milestone-by-milestone gating.
  Author: Grok-3 (xAI, temp 0.7) | Peer Reviewer: GPT-4o (OpenAI, temp 0.2) | Editor: Claude
  [today] | Initialized from SHELL v3

Write SACRED_FILES.md:
  # SACRED FILES | Lock date: [today] | Locked by: James P Rice Jr.
  | File | Reason | Locked |
  |------|--------|--------|
  | spec/frozen_spec.md | Oracle. Never modify after lock. | [today] |

Write BEST_PRACTICES.md:
  # BEST PRACTICES — Fermi Survival Paper | SHELL v3 standards
  - Survival function formalism first — not Drake probability math.
  - Zero detections is a censored observation in the Cox/Weibull sense.
  - Late-filter conclusion must be derived from ML hazard rate, never asserted.
  - Natural enemy: Hart (1975) and Hanson (1998) — address both explicitly.
  - No speculation about specific filter candidates (AI, nuclear, climate).
  - Milestone-by-milestone. No section opens until previous is Peer Reviewer ACCEPT.
  - Sensitivity analysis table required in M3: vary λ, SETI radius, galaxy age.
  - Competing models must be formally rejected: Drake, Rare Earth, Great Filter.
  - Every figure needs Python/matplotlib code. No orphan figure references.
  - Lean-ready proofs: all hypotheses explicit, every derivation step justified.
  - Literature gap formula required for every major prior work in Introduction.

Write devlog/DEV_LOG.md:
  # DEVELOPMENT LOG — fermi_survival_2025
  ## [today] — Session 1
  Initialized from SHELL v3. Spec locked. All files created. Git initialized.
  Pipeline: PAPER, multi-model triangulation, milestone-by-milestone gating.
  Models: Grok-3 (Author) → GPT-4o (Peer Reviewer) → Claude (Editor).
  Decisions: Markdown output, manual Zenodo upload, James P Rice Jr. reviews.

Write outputs/options.md:
  # OPTIONS LOG — fermi_survival_2025
  [No options yet.]

Write outputs/state_vector_backup.md:
  # STATE VECTOR BACKUP — fermi_survival_2025
  [No backups yet.]

Write prompts/turn_prompts_log.md:
  # TURN PROMPTS LOG — fermi_survival_2025
  # Every exact prompt logged here. Required for reproducibility.
  [No entries yet.]

### Step 8 — Initialize git
  cd D:\EXPERIMENTS\FERMI
  git init
  git add -A
  git commit -m "Turn 0 | Init | fermi_survival_2025"

### Step 9 — Print confirmation and hand off:
  ✅ PROJECT INITIALIZED: fermi_survival_2025
  🔒 Spec locked. All files created. Git initialized.
  ▶  Beginning paper pipeline — M1 (Survival Function Setup + Drake Critique) first.
  📄 Output: papers/fermi_survival_2025/paper.md
  🚀 Running. James P Rice Jr. reviews when done.

---

## HAND OFF — EXECUTE PAPER PIPELINE

Load prompts/04_paper_orchestrator.md.

Pass:
  PROBLEM: [full PROBLEM text above]
  DATA: No empirical data beyond the observational baseline in frozen spec.
        All results derived analytically from the survival function.
  SLUG: fermi_survival_2025
  DRIFT_RISKS: [paste KNOWN_DRIFT_RISKS into every Author and Reviewer prompt]
  FROZEN_SPEC: [pass full frozen_spec.md to Peer Reviewer on every pass]

Run the full milestone pipeline: M1 → M2 → M3 → M4.
Do not skip milestones. Do not open M2 until M1 is Peer Reviewer ACCEPT.
Halt only on HALT CONDITIONS.
When done write papers/fermi_survival_2025/paper.md and halt.
James P Rice Jr. reviews it.
