# INIT FILE — Canary Regression Test
# PURPOSE: A deliberately simple paper that exercises all pipeline components.
# Run after every engine change as a regression check.
# Target time: < 15 minutes. Target cost: < $10.
# If scores degrade by >0.5 from baseline, the engine change broke something.

## Experiment Identity
Name: The Prisoner's Dilemma Has a Unique Nash Equilibrium: A Formalization with Sensitivity Analysis
Slug: CANARY_REGRESSION
Author: James P Rice Jr.
Target: Games and Economic Behavior (for framing purposes)
Status: REGRESSION_TEST

## Problem
Prove that the standard two-player Prisoner's Dilemma with payoffs T > R > P > S
and 2R > T + S has a unique Nash equilibrium at (Defect, Defect), reached by
iterated elimination of strictly dominated strategies. Provide sensitivity analysis
showing robustness to payoff perturbations and boundary conditions identifying
when the result breaks (repeated games, continuous action spaces, evolutionary
dynamics).

## Confirmed Design Decisions
Spec locked: frozen_spec.md
Pipeline: PAPER — milestone-by-milestone gating
Author: Claude (Agent dispatch)
Peer Reviewer: Claude (Agent dispatch)
Editor: Claude (Agent dispatch)
Review format: Markdown
ASSAY DATA: none (pure theory paper)

## Milestones
M1: Definitions Block + Introduction. Define: players N={1,2}, strategy sets S_i={C,D},
    payoff matrix u_i(s), Nash equilibrium, strict dominance. Introduction: position
    against Axelrod (1984) iterated PD, Nowak (2006) evolutionary dynamics. State
    contribution: first complete formalization with sensitivity analysis.
M2: Core Proof. Theorem 1: D strictly dominates C for both players. Theorem 2:
    (D,D) is the unique NE. Corollary: it is also the unique rationalizable outcome.
M3: Application + Boundary Conditions. Application: compute equilibrium payoffs.
    Boundary: Natural Enemy (Folk Theorem for repeated games), Assumption Violations
    (what if T=R? what if continuous actions?), Sensitivity table (perturb each payoff
    by ±1, ±10), Competing Models (evolutionary game theory, Tit-for-Tat).
M4: Full paper assembly. Abstract, Related Work, Discussion, Conclusion.
    Note: "No figures required" — this is pure theory.

## Frozen Parameters

| Parameter | Value | Source |
|-----------|-------|--------|
| T (temptation) | 3 | Standard PD parameterization (Axelrod 1984) |
| R (reward) | 2 | Standard PD parameterization |
| P (punishment) | 1 | Standard PD parameterization |
| S (sucker) | 0 | Standard PD parameterization |
| Constraint 1 | T > R > P > S | Definition of PD |
| Constraint 2 | 2R > T + S | Cooperation Pareto-dominates alternation |

## Oracle
- The NE is (Defect, Defect). Unique.
- Proof by iterated elimination of strictly dominated strategies.
- Result holds for ALL payoff values satisfying T > R > P > S.
- Result BREAKS for: repeated games (infinite horizon + sufficiently patient players),
  continuous action spaces (may have interior equilibria), evolutionary dynamics
  (can sustain cooperation via replicator dynamics).

## Drift Risks
- LOW: This is a textbook result. The math cannot drift.
- MEDIUM: The sensitivity analysis must use the EXACT frozen payoff values.
- HIGH: Do NOT claim novelty of the result itself. The contribution is the
  formalization + sensitivity framework, not the equilibrium finding.

## Peer Reviewer Must Verify
- All four payoff values appear exactly as frozen
- Strict dominance condition uses strict inequality (not weak)
- Uniqueness proof is by iterated dominance, not by enumeration
- Sensitivity table uses ±1 and ±10 perturbations
- Natural Enemy (Folk Theorem) is correctly stated and bounded

## SETUP SEQUENCE
1. Create directory: papers/CANARY_REGRESSION_[DATE]_001/
2. Copy frozen parameters to frozen_spec.md
3. Initialize state_vector.md
4. Run pipeline: prompts/04_paper_orchestrator.md

## REGRESSION BASELINE (established 2026-05-16)
- Gemini composite: ~7.5 (DESK_REJECT on novelty — expected for textbook result)
- Grok run1 composite: ~7.8 (MINOR_REVISION)
- Grok run2 composite: 6.90
- AI detection (B1): Grok=NO_APPEARS_HUMAN, Gemini=UNCERTAIN
- Human authorship: Grok=YES_CONVINCINGLY, Gemini=UNCERTAIN
- Citation integrity (B3): N/A (pure theory paper, no citations to fabricate)

## REGRESSION THRESHOLDS
- D2 (Math Rigor): must stay >= 8. If drops: proofs got sloppy.
- D6 (Reproducibility): must stay >= 9. If drops: definitions became implicit.
- D9 (Intellectual Honesty): must stay >= 8. If drops: overclaiming crept in.
- D10 (Precision/Economy): must stay >= 8. If drops: verbosity introduced.
- D12 (Internal Consistency): must stay >= 9. If drops: coherence lost.
- D1 (Originality): should stay 1-4. If goes UP: Author is overclaiming novelty.
- D13 (Impact): should stay 2-4. If goes UP: Author is inflating significance.
- B1 (AI detection): Grok should stay NO_APPEARS_HUMAN. If flips to YES: writing discipline regressed.
