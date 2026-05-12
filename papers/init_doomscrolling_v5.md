# INIT — DOOMSCROLLING V5: FINAL PUBLICATION-READY
# EXECUTE IMMEDIATELY. Do not summarize, analyze, or ask questions.
# Read the INPUTS below, then execute the SETUP SEQUENCE step by step.
# Load prompts/00_init.md for the setup procedure, then run it with these inputs.
# This is not a document to review — it is a set of instructions to follow NOW.
#
# V5 fixes v4 steelman — TWO issues remaining, then submittable:
#   SF-1: Proposition 2 wrong — Surplus_ext >= 0, not ambiguous. DELETE Prop 2.
#   SF-2: Theorem 3 IVT proof boundary problems — fix or restrict.
#   AN-1: Figure 2 illustrative not computed — compute from model.
#   AN-2: Worked example lacks quantitative detail — add numbers.
#   AN-3: Myopic stopping rule not prominently flagged.

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: Doomscrolling as Optimal Stopping with Satiation: A Welfare Characterization
SLUG: DOOMSCROLLING_V5
AUTHOR: James P Rice Jr.
TARGET_VENUE: Journal of Economic Theory
PIPELINE: PAPER

PROBLEM:
V5 of the doomscrolling paper. Same model as v4 with two targeted fixes:

1. SURPLUS_EXT >= 0 (SF-1 — easy fix):
   V4 Proposition 2 claimed Surplus_ext can be negative. This is WRONG.
   Under the myopic stopping rule (Definition 9), the agent continues only
   when phi(t)*u(r_t) - c >= 0. Every extension-period payoff is non-negative.
   A sum of non-negative terms is non-negative. Therefore Surplus_ext >= 0.

   FIX: Delete Proposition 2 entirely. Replace with a one-line observation:
   "Surplus_ext >= 0 because the stopping rule ensures phi(t)*u(r_t) - c >= 0
   at every period the agent continues."

   This SIMPLIFIES the welfare characterization:
   - Delta_W = Delta_reorder - Surplus_ext
   - Surplus_ext >= 0 (always)
   - Delta_reorder can be + or - (survival probability asymmetry)
   - Delta_W > 0 iff Delta_reorder > Surplus_ext (harmful)
   - Delta_W < 0 when Delta_reorder < 0 (guaranteed beneficial — algorithmic
     feed better in shared window AND extended window)
   - Delta_W < 0 also possible when Delta_reorder > 0 but Surplus_ext >
     Delta_reorder (extension surplus dominates reordering cost)

   This is CLEANER than v4. Present it as the clean version.

2. THEOREM 3 BOUNDARY ARGUMENT (SF-2 — needs thought):
   V4 Theorem 3 claimed alpha* exists via IVT with:
   - Delta_W > 0 for alpha -> 0
   - Delta_W < 0 for alpha -> infinity
   Both boundary claims were wrong:
   - alpha -> 0: sign is ambiguous (depends on F)
   - alpha -> infinity: Delta_W -> 0 (both feeds show 1 item)

   FIX OPTIONS (Author should choose the best one):

   (A) RESTRICT to distributions where alpha* exists. State:
       "For distributions F with F(s*(1)) in (0,1) — i.e., some items above
       and some below the initial threshold — there exists alpha* such that..."
       This is the interesting case anyway. When F(s*(1)) = 0 (all items above
       threshold), the chronological feed has survival 1 and reordering is
       irrelevant. When F(s*(1)) = 1, no items clear the threshold.

   (B) PROVE the boundary behavior for the restricted class. Specifically:
       - For small alpha with F(s*(1)) > 0: the extension window is large
         (T_algo >> T_chron in expectation because the chronological feed
         suffers stochastic early stopping while the algorithmic feed extends
         deterministically). Surplus_ext is large. Meanwhile Delta_reorder
         depends on survival probability — with high early-stopping probability,
         Delta_reorder < 0 (algorithmic feed better in shared window). So
         Delta_W = (negative or small positive) - (large positive) < 0.
         WAIT — this gives Delta_W < 0 for small alpha too! That means the
         algorithmic feed is BENEFICIAL for slow satiation, contradicting v4.

       Let me think about this differently. The key question is: for what
       alpha values is Delta_W > 0 (harmful)?

       Actually, the harmful case occurs when the session extension has LOW
       surplus but the session still extends. This happens when:
       - The platform places barely-above-threshold items in the extension
         (minimal surplus per period)
       - The extension is long (many periods of near-zero surplus)
       - The agent would have been BETTER OFF stopping at T_chron

       Under the myopic rule, each extension period has surplus >= 0, so
       the extension never HURTS the agent's welfare directly. The harm
       comes from Delta_reorder > 0: the reordering cost in the shared
       window exceeds the extension benefit.

       For Delta_reorder > 0 to hold: the chronological feed must deliver
       higher expected per-period quality than the algorithmic feed in the
       shared window, accounting for survival probabilities. This requires
       HIGH survival probability under the chronological feed (so the
       chronological feed's quality advantage isn't crushed by attrition).

       HIGH survival requires most of F above threshold: F(s*(1)) small.
       But when F(s*(1)) is small, the extension window is also small
       (because the chronological feed already reaches most items).

       So the harmful regime requires: F(s*(1)) small (high survival) AND
       sufficient extension. These are in tension. The harmful regime exists
       but is narrower than v4 claimed.

   (C) REFRAME: Don't claim a single alpha* separating two regimes. Instead
       characterize Delta_W as a function of (alpha, F) and state the sign
       conditions directly. This is more honest than the binary alpha* framing
       and the decomposition Delta_W = Delta_reorder - Surplus_ext already
       provides the characterization. The "threshold alpha*" narrative is
       compelling but may not be supported by the math.

   RECOMMENDED: Option (A) + (B). Restrict to F with F(s*(1)) in (epsilon, 1-epsilon)
   and prove the boundary behavior for this class. If the IVT argument doesn't
   work cleanly, fall back to option (C): present the decomposition as the
   main result and note conditions under which alpha* exists.

3. COMPUTED FIGURE 2 (AN-1):
   Replace the illustrative Figure 2 with a simulation-computed figure.
   Use F = Lognormal(1, 0.8) truncated to [0, 20], c = 1, delta = 0.95,
   N = 50. Sweep alpha from 0.1 to 3. Compute Delta_W at each alpha by
   Monte Carlo (draw items, compute optimal ordering, compute welfare
   under both feeds, average). Plot the result.

4. QUANTITATIVE WORKED EXAMPLE (AN-2):
   Add a table showing Delta_W, Delta_reorder, Surplus_ext for specific
   alpha values (0.3, 0.5, 1.0, 1.5, 2.0) with a specific F. Show numbers.

5. MYOPIC RULE FLAGGING (AN-3):
   Add a prominent statement in the Model Setup: "The stopping rule is
   myopic — the agent continues whenever the current-period payoff is
   non-negative. This is a simplification; a forward-looking agent would
   account for declining continuation value. Assumption A5 in Boundary
   Conditions discusses the forward-looking alternative."

FROZEN_SPEC_PARAMETERS:

All v4 parameters carry forward with these modifications:

PARAMETER: Surplus_ext sign
VALUE: Surplus_ext >= 0. This is a CONSEQUENCE of the myopic stopping rule,
       not an assumption. Each extension-period payoff is non-negative by
       construction. DELETE any proposition claiming Surplus_ext can be negative.
DRIFT_RISK: CRITICAL — v4 had Proposition 2 claiming Surplus_ext < 0 possible.
             This is wrong. If the Author includes a proposition about
             Surplus_ext being negative: REJECT.

PARAMETER: Theorem 3 (alpha* existence)
VALUE: State conditions on F under which alpha* exists. Do NOT claim alpha*
       always exists. If the IVT boundary argument doesn't work cleanly,
       present the decomposition as the main result and note alpha* existence
       as a property of specific distribution classes.
DRIFT_RISK: HIGH — v4 IVT proof had wrong boundaries. Author must either
             fix the boundaries or restrict the claim.

PARAMETER: Figure 2
VALUE: Must be computed from the model (Monte Carlo simulation), not
       illustrative. Sweep alpha, compute Delta_W.
DRIFT_RISK: MEDIUM — v4 used hand-tuned illustrative function.

PARAMETER: All other parameters
VALUE: Inherited from v4 without modification. Ordering is INCREASING.
       Introduction before definitions. Search theory engaged. Discounted cost.
       Ferguson = survey. Citations correct. Three figures with code.
       Myopic rule flagged prominently.

MILESTONES:

M1: Introduction + Model Setup. Same as v4 but: (a) myopic rule flagged
    prominently in Definition 9, (b) Definition 12 welfare decomposition
    states Surplus_ext >= 0 directly.

M2: Core proofs. DELETE Proposition 2. Theorem 3 (alpha* existence) either
    restricted to appropriate F class or reframed as decomposition-first.
    Computed numerical example with table. Computed Figure 2 code.

M3: Application + Boundary Conditions. Tightened from v4. Myopic rule
    addressed in assumption violations.

M4: Full paper. Target <= 800 lines. All figures computed. All v1-v4
    dead ends avoided.

ORACLE:
1. No proposition claiming Surplus_ext < 0. Surplus_ext >= 0 stated directly.
2. Theorem 3 either has correct boundary argument OR is restricted/reframed.
3. Figure 2 computed from model, not illustrative.
4. Worked example has numerical table with specific Delta_W values.
5. Myopic stopping rule flagged in Model Setup.
6. All v1-v4 oracle conditions hold.
7. Paper <= 850 lines.

KNOWN_DRIFT_RISKS:

### NEW for v5
- Surplus_ext >= 0. If "Surplus_ext can be negative" appears: REJECT.
- Theorem 3 boundaries: Do NOT claim Delta_W > 0 at alpha -> 0 or
  Delta_W < 0 at alpha -> infinity without proof. Both limits give Delta_W -> 0
  in general. The harmful regime (if it exists) is in the interior.
- Figure 2 must be COMPUTED, not illustrative.

### ALL v1-v4 risks carry forward
- Ordering is INCREASING (not decreasing). Counterexample: {10,5,3,2}.
- Discounted cost only (no c*T).
- Delta_reorder sign not assumed.
- alpha* implicitly characterized (not explicit).
- Introduction before definitions.
- Search theory (Stigler, McCall) engaged.
- Ferguson = survey. Bursztyn = Rao/Roth/YD. Che-Mierendorff correct title.
- Within-session enjoyment = conjecture.
- Survival bias acknowledged.
- N_above(t) distinguished from N.
- Limitations are limitations.
- Three figures with code.

---

## SETUP SEQUENCE — EXECUTE NOW

Standard scaffolding at DOOMSCROLLING_V5_2026-05-11_001.
Dead ends: ALL v1-v4 dead ends plus:
  "V4 Proposition 2 claimed Surplus_ext < 0 possible. WRONG — sum of
   non-negative terms is non-negative. V4 Theorem 3 IVT proof had wrong
   boundary behavior at both alpha -> 0 and alpha -> infinity."

Copy prompts. Git init. Hand off to pipeline.

---

## HAND OFF — EXECUTE PAPER PIPELINE

DO NOT STOP HERE. Read prompts/04_paper_orchestrator.md NOW and execute it.

YOUR INPUTS:
  PROBLEM: [full PROBLEM text above]
  DATA: No empirical data. Three figures required (Figure 2 COMPUTED).
  SLUG: DOOMSCROLLING_V5_2026-05-11_001
  DRIFT_RISKS: [ALL v1-v5 drift risks]
  FROZEN_SPEC: [full frozen_spec.md]

BEGIN NOW. Run M1.
