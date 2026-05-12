# INIT — DOOMSCROLLING V3: SURVIVAL-CORRECTED WELFARE CHARACTERIZATION
# EXECUTE IMMEDIATELY. Do not summarize, analyze, or ask questions.
# Read the INPUTS below, then execute the SETUP SEQUENCE step by step.
# Load prompts/00_init.md for the setup procedure, then run it with these inputs.
# This is not a document to review — it is a set of instructions to follow NOW.
#
# V3 of doomscrolling. Incorporates v2 steelman feedback:
#   SF-1: Δ_reorder sign not proven — survival probability asymmetry
#   SF-2: α* is implicit, not "explicit" — overclaim
#   AN-1: No figures despite spec — add three figures with code
#   AN-2: Two bibliographic errors (Bursztyn coauthors, Che-Mierendorff title)
#   AN-3: Unsourced empirical claim about within-session enjoyment
#   AN-4: Quality trajectory prediction has survival bias
#   AN-5: "Is This Obvious?" needs worked numerical example

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: Doomscrolling as Optimal Stopping Failure: Welfare Characterization Under Algorithmic Feeds with Satiation
SLUG: DOOMSCROLLING_V3
AUTHOR: James P Rice Jr.
TARGET_VENUE: Journal of Behavioral Decision Making
PIPELINE: PAPER

PROBLEM:
Models social media feed consumption as an optimal stopping problem with
satiation (φ(t) = t^{−α}, decreasing enjoyment over a session). The platform
reorders items to maximize session duration. V3 corrects a proof error in v2's
welfare characterization and adds figures, worked examples, and bibliographic
fixes.

V3 is NOT a new model. It is v2 with targeted fixes:

1. SURVIVAL-CORRECTED WELFARE DECOMPOSITION (SF-1 from v2 steelman):
   V2 claimed Δ_reorder ≥ 0 (the algorithmic feed's reordering cost in the
   shared window is non-negative). This is WRONG when the chronological feed's
   survival probability Pr(T_chron ≥ t) is low — the algorithmic feed
   guarantees reaching period t while the chronological feed may not.

   V3 must do ONE of:
   (a) Prove Δ_reorder ≥ 0 rigorously by showing the survival-weighted surplus
       under the chronological feed exceeds the algorithmic feed's lower surplus
       at every t in the shared window (this may be false — check first), OR
   (b) Drop the assumption Δ_reorder ≥ 0 and state the full sign condition:
       ΔW > 0 iff Δ_reorder > Surplus_ext, where Δ_reorder can be positive
       or negative. This changes the welfare characterization — the harmful
       regime is now smaller than v2 claimed (because Δ_reorder < 0 in some
       cases makes ΔW more likely negative/beneficial).

   The Author MUST work through the survival probability asymmetry carefully.
   Specifically: at time t in the shared window, π_chron(t) = Pr(T_chron ≥ t) ·
   (φ(t)·E_top(t) − c) and π_algo(t) = 1 · (φ(t)·u(q(σ*(t))) − c). When
   Pr(T_chron ≥ t) is much less than 1, π_chron(t) < π_algo(t) even though
   E_top(t) > u(q(σ*(t))). The reordering "cost" becomes a reordering "benefit"
   because the algorithmic feed guarantees reaching periods the chronological
   feed rarely reaches.

   If option (b): the welfare characterization becomes richer. The sign of ΔW
   depends on TWO quantities (Δ_reorder and Surplus_ext), both of which have
   economic interpretations. Δ_reorder < 0 means the algorithmic feed's
   reliability (guaranteed continuation) outweighs its lower per-item quality.
   This is actually a MORE interesting result than v2's clean dichotomy.

2. α* IS IMPLICITLY DEFINED (SF-2 from v2 steelman):
   V2 claimed α* is "an explicit function of the model parameters." It is not.
   It is the unique solution to an implicit equation where α* appears in the
   summation limits, conditional expectations, and survival probabilities.
   V3 must say "implicitly characterized" or "characterized by [equation]."
   Existence and uniqueness are proven via IVT — that is the correct claim.

3. FIGURES REQUIRED (AN-1 from v2 steelman):
   V2 had no figures. V3 MUST include three figures with Python/matplotlib code:
   - Figure 1: Rising threshold s*(t) under satiation for different α values
   - Figure 2: ΔW as a function of α, showing harmful (ΔW > 0) and beneficial
     (ΔW < 0) regions, with the survival-corrected decomposition
   - Figure 3: Illustrative worked example showing how low-mean high-variance
     feeds sustain the trap longer than high-mean low-variance feeds

4. BIBLIOGRAPHIC FIXES (AN-2 from v2 steelman):
   - Bursztyn et al.: body text must match reference. The paper is Bursztyn,
     Rao, Roth, and Yanagizawa-Drott (2022), "Opinions as Facts," RES.
   - Che and Mierendorff (2019): correct title is "Optimal Dynamic Allocation
     of Attention," AER 109(11). NOT "Optimal Sequential Decision with
     Limited Attention."

5. UNSOURCED EMPIRICAL CLAIM (AN-3 from v2 steelman):
   V2 claimed "self-reported enjoyment of social media sessions is decreasing
   within sessions" without citation. V3 must either cite a source or label
   this as a stylized assumption. If no source: write "we conjecture that
   within-session enjoyment declines, consistent with the satiation assumption,
   though direct empirical measurement of this pattern is an open question."

6. SURVIVAL BIAS IN TESTABLE PREDICTION (AN-4 from v2 steelman):
   V2's "quality trajectory" prediction (E[T]-maximizers show increasing
   quality conditional on survival) has survival bias — conditioning on
   reaching position t creates upward selection. V3 must either:
   (a) Propose a bias-corrected measurement (e.g., compare quality trajectories
       across platforms with different algorithmic intensity, or compare early
       items of long vs. short sessions), OR
   (b) Acknowledge the survival bias explicitly and state what additional
       data would be needed to test the prediction cleanly.

7. WORKED NUMERICAL EXAMPLE (AN-5 from v2 steelman):
   The "Is This Obvious?" section needs a concrete example. V3 must include
   a worked example showing: Feed A (mean 5, variance 1, thin tail) vs.
   Feed B (mean 3, variance 10, heavy tail). Compute α* for each. Show
   Feed B sustains longer sessions. Show the welfare sign depends on what
   the platform places in the extended window. Numbers, not prose.

FROZEN_SPEC_PARAMETERS:

All parameters from v2 frozen spec CARRY FORWARD with these modifications:

PARAMETER: Welfare characterization — SURVIVAL-CORRECTED
VALUE: ΔW = Δ_reorder − Surplus_ext where Δ_reorder = ∑_{shared} δ^{t−1}
       [π_chron(t) − π_algo(t)]. Δ_reorder CAN BE NEGATIVE when the
       algorithmic feed's guaranteed survival outweighs its lower per-item
       surplus. The sign of ΔW depends on BOTH Δ_reorder and Surplus_ext.
       Must derive the full two-dimensional sign condition.
DRIFT_RISK: CRITICAL — Author may default to v2's Δ_reorder ≥ 0 assumption.
             If the Author asserts Δ_reorder ≥ 0 without rigorous proof
             accounting for survival probabilities: REJECT.

PARAMETER: Critical exponent characterization
VALUE: α* is the unique solution to Π_algo(α*) = Π_chron(α*). This is an
       IMPLICIT characterization. α* exists and is unique (by IVT and
       monotonicity). It is NOT an explicit/closed-form function.
DRIFT_RISK: HIGH — Author may write "explicit" or "closed-form." Only
             "implicitly characterized" or "characterized by [equation]"
             is acceptable.

PARAMETER: Figures
VALUE: Three figures required with Python/matplotlib code per Author Rule 5.
       Figure 1: Rising threshold under different α
       Figure 2: ΔW regions (harmful/beneficial) with survival correction
       Figure 3: Tail-dependence worked example (Feed A vs Feed B)
DRIFT_RISK: HIGH — v2 had no figures. Author MUST include figure code.
             "No figures required" is NOT acceptable for v3.

PARAMETER: All other parameters
VALUE: Inherited from v2 frozen spec without modification. Specifically:
       - Discounted cost: sum δ^{t−1}(φ(t)·u(r_t) − c). NOT c*T.
       - Satiation: φ(t) = t^{−α}, α > 0, decreasing, φ(1)=1, φ→0.
       - Ferguson = historical survey. Chow-Robbins-Siegmund = theory.
       - N_above(t) distinguished from N throughout.
       - Limitations labeled as limitations, not open problems.
DRIFT_RISK: See v2 frozen spec for full drift risk list.

MILESTONES:

M1: Definitions (carry forward from v2) + Introduction with corrected
    contributions list (α* "implicitly characterized," not "explicit").
    Bibliographic corrections. Same literature engagement as v2.

M2: Core proofs with SURVIVAL-CORRECTED welfare decomposition:
    - Lemma 1-3 carry forward from v2 (satiation Bellman, shrinking pool,
      finite session)
    - Theorem 1 carries forward with corrected language (α* implicit)
    - Theorem 2 REWRITTEN: either prove Δ_reorder ≥ 0 with survival
      probabilities, or state the full sign condition without assuming sign.
      Include worked numerical example showing the survival asymmetry.
    - Theorem 3 carries forward (welfare benefit cap)
    - Corollary 1 carries forward or is modified per new Theorem 2
    - FIGURE CODE for all three figures in this milestone

M3: Application + Boundary Conditions with:
    - Survival-bias-corrected testable prediction
    - Worked numerical example (Feed A vs Feed B)
    - Unsourced claim fixed (cite or label as conjecture)
    - All other v2 M3 content carries forward

M4: Full paper with figures, corrected bibliography, "Is This Obvious?"
    section with numerical example. Everything assembled.

ORACLE:
The model is valid if and only if:
1. Welfare decomposition handles survival probability asymmetry correctly —
   either proves Δ_reorder ≥ 0 rigorously or states the full sign condition
2. α* described as "implicitly characterized," NOT "explicit"
3. Three figures included with Python/matplotlib code
4. Bursztyn coauthors match between body and references
5. Che-Mierendorff title is "Optimal Dynamic Allocation of Attention"
6. Within-session enjoyment claim is sourced or labeled as conjecture
7. Quality trajectory prediction addresses survival bias
8. Worked numerical example demonstrates tail-dependence non-obviousness
9. All v2 oracle conditions also hold (discounted cost, satiation boundary
   theorem, Ferguson as survey, pool distinction, etc.)

Peer Reviewer: if the Author asserts Δ_reorder ≥ 0 without a rigorous
proof that accounts for survival probability, REJECT on M2.1(b).

KNOWN_DRIFT_RISKS:

- V2 REGRESSION: Δ_reorder ≥ 0 asserted without proof. The survival
  probability Pr(T_chron ≥ t) can be much less than 1 in the shared window,
  making π_chron(t) < π_algo(t). If the Author writes "Δ_reorder ≥ 0" without
  showing the survival-weighted comparison holds term by term: REJECT.

- V2 REGRESSION: α* called "explicit." It is implicit. If the Author writes
  "explicit function" or "closed-form expression" for α*: flag immediately.

- V2 REGRESSION: No figures. V3 MUST have three figures with code. If the
  Author writes "No figures required": REJECT.

- V2 REGRESSION: Bursztyn coauthor mismatch. Body must say "Bursztyn, Rao,
  Roth, and Yanagizawa-Drott (2022)." NOT "Bursztyn, González, and
  Yanagizawa-Drott."

- V2 REGRESSION: Che-Mierendorff title. Reference must say "Optimal Dynamic
  Allocation of Attention." NOT "Optimal Sequential Decision with Limited
  Attention."

- V2 REGRESSION: Unsourced empirical claim about within-session enjoyment.
  Must cite or label as conjecture.

- ALL V1 AND V2 DRIFT RISKS CARRY FORWARD:
  - Discounted cost only (no c*T)
  - Welfare "characterization" not "loss" (except where sign proven positive)
  - Ferguson = survey, Chow-Robbins-Siegmund = theory
  - Satiation boundary must be proven theorem
  - Distinguish N_above(t) from N
  - Limitations are limitations, not open problems
  - Engage strategic experimentation literature
  - Lead with welfare characterization, not trap theorem

- NEW: SURVIVAL BIAS in testable prediction. The quality trajectory conditional
  on survival is biased upward. The Author must address this — either propose
  a corrected measurement or acknowledge the bias explicitly.

- NEW: WORKED EXAMPLE required. The "Is This Obvious?" section must include
  a numerical example with specific distributions, computed α*, and welfare
  sign. Not prose — numbers.

- PROOF STRATEGY for Δ_reorder sign: The Author should first CHECK whether
  Δ_reorder ≥ 0 is actually true. Work through a specific example:
  φ(t) = t^{-0.3}, F = Lognormal(1, 1), c = 1, δ = 0.95. Compute
  π_chron(t) and π_algo(t) for t = 1, 5, 10, 20. If π_chron(t) < π_algo(t)
  at ANY t, then Δ_reorder ≥ 0 is false and option (b) is required.

- FIGURE SPECIFICATION:
    Figure 1: Plot s*(t) = c/φ(t) for α = 0.1, 0.3, 0.5, 1.0 vs. constant
              threshold (α = 0). Show how threshold rises with satiation.
    Figure 2: Simulate ΔW for a range of α values with fixed F. Show the
              harmful (ΔW > 0) and beneficial (ΔW < 0) regions. Mark α*.
              Include the survival-corrected decomposition.
    Figure 3: Two distributions — Feed A (thin tail, high mean) and Feed B
              (heavy tail, low mean). Show α* is larger for Feed B. Show
              session length under algorithmic feed for each.

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 0 — Resolve project directory
Base slug: DOOMSCROLLING_V3
Check existing: C:\PROJECTS\SHELL\papers\DOOMSCROLLING_V3*
Use auto-versioning: DOOMSCROLLING_V3_[YYYY-MM-DD]_001

### Step 1 — Create project directory
Create resolved directory with:
  figures/, results/raw/, results/final/, outputs/, devlog/, prompts/

### Step 2 — Write CLAUDE.md
North star: survival-corrected welfare characterization under algorithmic feeds
with satiation. V3 fixes v2's Δ_reorder sign error, adds figures, fixes
bibliography, adds worked examples.

### Step 3 — Write frozen_spec.md
Fill from FROZEN_SPEC_PARAMETERS above plus all v2 parameters carried forward.
Lock date today. Locked by: James P Rice Jr.
Include v1 ref: C:\PROJECTS\SHELL\papers\DOOMSCROLLING\paper.md
Include v2 ref: C:\PROJECTS\SHELL\papers\DOOMSCROLLING_V2_2026-05-11_001\paper.md

### Step 4 — Initialize state files
state_vector.md — TURN: 0, MILESTONE: M1, MODE: INIT
innovation_log.md — header with project name and timestamp
dead_ends.md — header; add ALL v1 and v2 dead ends plus:
  "V2 asserted Δ_reorder ≥ 0 without accounting for survival probability
   asymmetry. V2 called α* 'explicit' when it is implicit. V2 had no figures.
   V2 had Bursztyn coauthor mismatch and Che-Mierendorff title error."

### Step 5 — Copy all prompts from SHELL
Copy from C:\PROJECTS\SHELL\prompts\ into project prompts/:
  04_paper_orchestrator.md, 05_author.md, 06_peer_reviewer.md,
  07_editor.md, 08_steelman.md, run_milestone.md
Also write prompts/turn_prompts_log.md

### Step 5b — Write run_pipeline.ps1
Use template from C:\PROJECTS\SHELL\prompts\00_init.md Step 15.

### Step 6 — Write STATUS.md, README.md, CHAIN_PROMPT.md, SACRED_FILES.md,
             BEST_PRACTICES.md, devlog/DEV_LOG.md, outputs/options.md,
             outputs/state_vector_backup.md, .gitignore

### Step 7 — Initialize git
  cd [RESOLVED_DIR]
  git init && git add -A && git commit -m "Turn 0 | Init | doomscrolling_v3"

### Step 8 — Print confirmation and hand off

---

## HAND OFF — EXECUTE PAPER PIPELINE

DO NOT STOP HERE. Read prompts/04_paper_orchestrator.md NOW and execute it.

YOUR INPUTS:
  PROBLEM: [full PROBLEM text above including V3 fixes]
  DATA: No empirical data. All results analytical. THREE FIGURES REQUIRED.
  SLUG: [RESOLVED_SLUG]
  DRIFT_RISKS: [paste ALL drift risks — v1, v2, and v3 — into every prompt]
  FROZEN_SPEC: [pass full frozen_spec.md to Peer Reviewer on every review pass]

BEGIN NOW. Run M1. Do not ask for confirmation. Write the paper.
