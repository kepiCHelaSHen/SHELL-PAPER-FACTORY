# INIT — DOOMSCROLLING V4: PUBLICATION-READY
# EXECUTE IMMEDIATELY. Do not summarize, analyze, or ask questions.
# Read the INPUTS below, then execute the SETUP SEQUENCE step by step.
# Load prompts/00_init.md for the setup procedure, then run it with these inputs.
# This is not a document to review — it is a set of instructions to follow NOW.
#
# V4 fixes v3 steelman findings + publishability improvements:
#   SF-1: Lemma 3 ordering WRONG — must be INCREASING (minimal sufficient), not decreasing
#   AN-1: Restore search theory (Stigler 1961, McCall 1970) — dropped from v2→v3
#   AN-2: Move Definitions AFTER Introduction (standard journal format)
#   AN-4: Restore dropped references (Laibson, Gabaix, Sims, Gul-Pesendorfer)
#   Publishability: Tighten length ~25%, empirical grounding for satiation

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: Doomscrolling as Optimal Stopping Failure: Welfare Characterization Under Algorithmic Feeds with Satiation
SLUG: DOOMSCROLLING_V4
AUTHOR: James P Rice Jr.
TARGET_VENUE: Journal of Behavioral Decision Making
PIPELINE: PAPER

PROBLEM:
V4 of the doomscrolling paper. Same model as v3 with targeted fixes for
publication readiness. This is NOT a new model — it is v3 with corrections
and tightening.

V4 FIXES:

1. ORDERING DIRECTION (SF-1 — BLOCKING):
   V3 Lemma 3 claimed the E[T]-maximizing platform orders items in DECREASING
   quality. This is WRONG. Simple counterexample: items {10,5,3,2}, thresholds
   s*(1)=1, s*(2)=2, s*(3)=3, s*(4)=4.
   - Decreasing: 10,5,3,2 → T_algo = 3 (2 < 4, fails at t=4)
   - Increasing (minimal sufficient): 2,3,5,10 → T_algo = 4 (all clear)
   
   The correct strategy is INCREASING order (minimal sufficient first, best
   last). Save expensive items for later high-threshold positions. Use cheap
   items where the threshold is low. This was correct in v2 (Lemma 4) but
   v3 regressed.
   
   CONSEQUENCES:
   - The E[T]-maximizer shows INCREASING quality over a session (not decreasing)
   - The worked example must use increasing-order item placement
   - The quality trajectory prediction: E[T]-maximizers show increasing quality,
     welfare-maximizers show decreasing quality (SAME as v2, OPPOSITE of v3)
   
   DRIFT_RISK: CRITICAL — if the Author writes "decreasing order" for the
   E[T]-maximizing strategy: REJECT IMMEDIATELY. This was wrong in v3.

2. SEARCH THEORY CONNECTION (AN-1):
   V2 had a section on search theory (Stigler 1961, McCall 1970) distinguishing
   the rising-threshold tail-dependence from the classical constant-threshold
   variance result. V3 dropped this entirely. V4 must restore it.
   Key point: under constant threshold (classical search), variance increases
   option value uniformly. Under RISING threshold (our model), the relevant
   feature is tail decay rate relative to threshold growth rate c·t^α —
   a finer distinction than classical search provides.

3. STANDARD JOURNAL FORMAT (AN-2):
   Move Definitions AFTER Introduction. Standard format:
   Abstract → Introduction → Model Setup (definitions) → Results → ...
   JBDM reviewers expect motivation before formalism.

4. RESTORE DROPPED REFERENCES (AN-4):
   Restore: Stigler (1961), McCall (1970), Laibson (1997), Gabaix (2019),
   Sims (2003), Gul and Pesendorfer (2001). These were in v2's competing
   models section and are expected by reviewers.

5. TIGHTEN LENGTH:
   Target: ~800 lines (v3 was 1038). Cut:
   - Boundary conditions: merge edge cases into sensitivity table
   - Competing models: tighter engagement (2-3 sentences per model, not paragraphs)
   - Related work: combine with Introduction's literature positioning where possible
   - Remove redundant restatements of results across sections

6. ALL V1-V3 FIXES CARRY FORWARD:
   - Discounted cost (no c*T)
   - Δ_reorder sign not assumed (survival correction)
   - α* implicitly characterized (not explicit)
   - Three figures with code
   - Bursztyn = Rao, Roth, Yanagizawa-Drott
   - Che-Mierendorff = "Optimal Dynamic Allocation of Attention"
   - Within-session enjoyment = conjecture
   - Survival bias acknowledged
   - Worked numerical examples
   - Ferguson = survey
   - N_above(t) distinguished from N
   - Limitations labeled as limitations

FROZEN_SPEC_PARAMETERS:

All v3 parameters carry forward with this modification:

PARAMETER: Platform's optimal ordering
VALUE: INCREASING quality order (minimal sufficient first, best last).
       At each position t, place the item with the LOWEST quality that
       still clears the threshold s*(t). Conserve high-quality items for
       later positions where the rising threshold demands them.
       NEVER "decreasing order." The swap argument: moving a good item
       from a later position to an earlier one WASTES its ability to
       clear a high threshold that a worse item cannot handle.
DRIFT_RISK: CRITICAL — v3 had this wrong. If "decreasing" appears as the
             E[T]-maximizing strategy: REJECT.

PARAMETER: Section ordering
VALUE: Abstract → Introduction → Model Setup (definitions) → Core Results
       → Application → Boundary Conditions → Related Work → Discussion
       → Conclusion → References
DRIFT_RISK: MEDIUM — Author may default to v3's definitions-first format.
             Introduction MUST come before definitions.

PARAMETER: Search theory engagement
VALUE: Must cite and distinguish from Stigler (1961) and McCall (1970).
       Key distinction: constant threshold (classical) vs. rising threshold
       (our model) changes which distributional feature matters.
DRIFT_RISK: HIGH — v3 dropped this. Must be restored.

PARAMETER: Length target
VALUE: ~800 lines. Tighter than v3 (1038). Merge edge cases into table,
       compress competing models, reduce redundancy.
DRIFT_RISK: MEDIUM — Author may write at v3 length. Enforce concision.

MILESTONES:

M1: Introduction (first!) + Model Setup (definitions, now Section 2).
    Introduction must motivate before formalism. Literature positioning
    includes search theory (Stigler, McCall). All v3 definitions carry
    forward but placed AFTER Introduction.

M2: Core proofs. CORRECT ordering (increasing/minimal sufficient). Worked
    example recomputed with correct ordering. All v3 theorems carry forward
    with Lemma 3 corrected. Include counterexample showing why decreasing
    fails.

M3: Application + Boundary Conditions (tightened — edge cases in table).
    Competing models compressed. Search theory section restored.

M4: Full paper assembly. Related Work, Discussion, Conclusion, References.
    Restore Stigler, McCall, Laibson, Gabaix, Sims, Gul-Pesendorfer.
    Target ~800 lines total.

ORACLE:
1. Ordering is INCREASING (minimal sufficient). Never decreasing.
2. Introduction comes before definitions.
3. Stigler and McCall cited and distinguished.
4. All v1-v3 oracle conditions hold.
5. Paper is ≤900 lines.
6. Worked example uses correct (increasing) ordering.

Peer Reviewer: if "decreasing order" appears as E[T]-maximizing strategy, REJECT.

KNOWN_DRIFT_RISKS:

### NEW for v4
- ORDERING REGRESSION: "decreasing order" for E[T]-maximizing strategy is WRONG.
  Correct: INCREASING (minimal sufficient). Counterexample: {10,5,3,2} with
  thresholds {1,2,3,4}. Decreasing gives T=3, increasing gives T=4. REJECT
  if decreasing appears.
- SECTION ORDER: Introduction must precede definitions. Not definitions-first.
- SEARCH THEORY GAP: Must cite Stigler (1961) and McCall (1970). Distinguish
  constant-threshold variance effect from rising-threshold tail decay effect.
- LENGTH: Target ≤900 lines. v3 was 1038. Compress edge cases, competing
  models, reduce redundancy.

### Carried from v1-v3
- Discounted cost only (no c*T)
- Δ_reorder sign not assumed (survival correction)
- α* implicitly characterized (not explicit)
- Three figures with code REQUIRED
- Bursztyn = Rao, Roth, Yanagizawa-Drott
- Che-Mierendorff = "Optimal Dynamic Allocation of Attention"
- Within-session enjoyment = conjecture
- Survival bias acknowledged
- Ferguson = survey
- N_above(t) distinguished from N
- Limitations are limitations, not open problems
- Lead with welfare characterization, not trap theorem

FIGURE SPECIFICATION:
- Figure 1: Rising threshold s*(t) for various α
- Figure 2: ΔW vs α showing harmful/beneficial regions (with correct ordering)
- Figure 3: Tail dependence — Feed A vs Feed B, α* comparison

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1-7 — Standard scaffolding
Create DOOMSCROLLING_V4_2026-05-11_001 with all standard files.
dead_ends.md must include ALL v1-v3 dead ends plus:
  "V3 Lemma 3 claimed decreasing order optimal. WRONG. Counterexample:
   {10,5,3,2} thresholds {1,2,3,4}. Decreasing T=3, increasing T=4.
   Correct: INCREASING (minimal sufficient first, best last).
   V3 dropped Stigler/McCall search theory connection.
   V3 had definitions before introduction (non-standard)."

### Step 8 — git init and commit
### Step 9 — Hand off to pipeline

---

## HAND OFF — EXECUTE PAPER PIPELINE

DO NOT STOP HERE. Read prompts/04_paper_orchestrator.md NOW and execute it.

YOUR INPUTS:
  PROBLEM: [full PROBLEM text above]
  DATA: No empirical data. Three figures required.
  SLUG: DOOMSCROLLING_V4_2026-05-11_001
  DRIFT_RISKS: [ALL v1-v4 drift risks]
  FROZEN_SPEC: [full frozen_spec.md]

BEGIN NOW. Run M1.
