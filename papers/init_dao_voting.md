# INIT — VOTING POWER IN WEIGHTED DAOs
# Pre-filled. Ready to run.
# claude --dangerously-skip-permissions papers/init_dao_voting.md

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: Voting Power in Weighted DAOs: Banzhaf Index Analysis of Token-Based Governance
SLUG: dao_voting_2026
AUTHOR: James P Rice Jr.
TARGET_VENUE: Social Choice and Welfare
PIPELINE: PAPER

PROBLEM:
Applies the Banzhaf power index to token-weighted voting in DAOs. Derives
closed-form expressions for the Banzhaf index as a function of token distribution
(Gini coefficient, Herfindahl index). Proves effective number of decision-makers
is always <= reciprocal of Herfindahl index. For typical crypto distributions
(power-law), fewer than 10 entities control governance regardless of token holder
count. Proposes quadratic voting modification and proves it increases small holder
power. The central contribution is making DAO governance legible through classical
voting power theory: the token distribution determines the power distribution,
and for real-world crypto token distributions, governance is an oligarchy by
construction. Quadratic voting is the proven fix.

FROZEN_SPEC_PARAMETERS:

PARAMETER: Banzhaf power index definition
VALUE: beta_i = (number of swings for player i) / (total swings across all players)
UNIT: dimensionless (normalized to sum to 1)
TOLERANCE: exact — this is the definition
SOURCE: Banzhaf 1965 | Rutgers Law Review 19:317-343
NOTES: A swing for player i is a coalition where i's addition changes the outcome
       from losing to winning. The Banzhaf index measures actual voting power as
       opposed to nominal weight. Must use Banzhaf, not Shapley-Shubik (different
       axiomatics, different results).
DRIFT_RISK: MEDIUM — Author may confuse Banzhaf with Shapley-Shubik index.
             Must use Banzhaf throughout and explain why.

PARAMETER: Herfindahl-Hirschman Index (HHI)
VALUE: HHI = sum(s_i^2) where s_i = share of player i
UNIT: dimensionless (0 to 1 for normalized shares)
TOLERANCE: exact — this is the definition
SOURCE: Standard industrial organization (Herfindahl 1950; Hirschman 1964)
NOTES: HHI measures concentration. The paper must prove that the effective
       number of decision-makers (1/HHI) is an upper bound on the number of
       players with significant Banzhaf power. This is the Herfindahl bound theorem.
DRIFT_RISK: LOW — standard definition, but the bound theorem is novel

PARAMETER: Penrose square root law
VALUE: In large weighted voting games with many small players, Banzhaf power
       is approximately proportional to sqrt(weight)
UNIT: N/A (asymptotic approximation)
TOLERANCE: asymptotic — exact for N -> infinity
SOURCE: Penrose 1946 | Journal of the Royal Statistical Society 109(1):10-20
NOTES: The Penrose approximation gives intuition but breaks down for concentrated
       distributions. The paper must show where the approximation fails (high HHI)
       and use exact Banzhaf computation for real token distributions.
DRIFT_RISK: MEDIUM — Author may rely on Penrose approximation where exact
             computation is needed

PARAMETER: Quadratic voting
VALUE: Cost = votes^2 (buying v votes costs v^2 tokens)
UNIT: N/A (mechanism)
TOLERANCE: N/A
SOURCE: Lalley & Weyl 2018 | Quarterly Journal of Economics 133(1):1-49
NOTES: Under quadratic voting, effective power scales as sqrt(weight) exactly,
       not just asymptotically. The paper must prove this and show quantitatively
       how it redistributes power from whales to small holders.
DRIFT_RISK: MEDIUM — Author may describe quadratic voting without proving the
             power redistribution formally

PARAMETER: Crypto token distributions
VALUE: Power-law with exponent alpha ~ 1.5-2.0 (highly concentrated)
UNIT: dimensionless
TOLERANCE: range from empirical data
SOURCE: Nadler & Guo 2020 | Finance Research Letters 36:101333;
        Somin et al. 2023 | Applied Network Science 8:17
NOTES: Must use actual token distributions from major DAOs (Uniswap, Compound,
       MakerDAO, Aave, etc.) to compute Banzhaf indices. Not hypothetical.
DRIFT_RISK: HIGH — Author may use hypothetical distributions instead of real data

MILESTONES:

M1: Formal model — define the weighted voting game for a DAO. Define Banzhaf
    index, distinguish from Shapley-Shubik. Define HHI for token distributions.
    State the Penrose square root law and its limitations. Establish notation.
    Show why nominal token weight != voting power.

M2: Banzhaf-Herfindahl theorem + Penrose approximation — Prove Theorem 1:
    effective number of decision-makers <= 1/HHI. Prove Theorem 2: for power-law
    token distributions with alpha < 2, fewer than 1/HHI entities have
    significant Banzhaf power. Show where Penrose approximation applies vs fails.
    Compute exact Banzhaf indices for 3-5 real DAO token distributions.

M3: Quadratic voting fix + boundary conditions — Prove Theorem 3: under
    quadratic voting, Banzhaf power scales as sqrt(weight) exactly. Quantify the
    power redistribution: compute Banzhaf indices for the same real DAOs under
    quadratic voting. Show the increase in small holder power. Boundary conditions:
    equal distribution (HHI -> 0), single dictator (HHI -> 1), two-player game.
    Sensitivity analysis table.

M4: Full paper — Introduction (DAO governance as a weighted voting game),
    Related work (Banzhaf 1965, Penrose 1946, Lalley & Weyl 2018, DAO governance
    literature), Discussion (implementation challenges, gas costs of quadratic
    voting, Sybil resistance), Conclusion. Self-contained Abstract.

ORACLE:
The model is valid if and only if:
1. Banzhaf power index is correctly defined and computed (not Shapley-Shubik)
2. The Herfindahl bound (effective decision-makers <= 1/HHI) is proven as a theorem
3. Real DAO token distributions are used, not hypothetical ones
4. The quadratic voting improvement is formally demonstrated with before/after
   Banzhaf computations
5. The Penrose approximation's domain of validity is explicitly characterized

Peer Reviewer must verify: is the Herfindahl bound a proven theorem, and are the
Banzhaf computations done on real token data? If either is missing, REJECT.

KNOWN_DRIFT_RISKS:
- Confusing Banzhaf with Shapley-Shubik index — must use Banzhaf and explain
  the choice (Banzhaf assumes all coalitions equally likely, appropriate for
  decentralized governance where coordination is unstructured)
- Using hypothetical token distributions instead of actual crypto data — must
  use real distributions from named DAOs with cited sources
- Not proving the Herfindahl bound formally — must be a theorem with proof
- Relying on Penrose approximation where exact computation is needed — Penrose
  breaks down for concentrated distributions, which is exactly the case of interest
- Describing quadratic voting without proving the power redistribution — must
  compute Banzhaf indices before and after for real DAOs
- Ignoring Sybil attacks — quadratic voting is vulnerable to identity splitting;
  must discuss this as a limitation
- Making the paper too crypto-specific and losing the voting theory audience —
  frame as voting power theory with DAO as application
- Adding unnecessary blockchain implementation details — keep it mathematical
- Failing to compare with existing DAO governance analysis — must cite and
  distinguish from Somin et al. 2023 and similar work
- Orphan figure references — every figure must have Python/matplotlib code.
  The paper should include at minimum:
    Figure 1: Banzhaf power vs nominal weight for a real DAO (log-log plot)
    Figure 2: Effective decision-makers vs HHI across multiple DAOs
    Figure 3: Banzhaf redistribution under quadratic voting (before/after)

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1 — Create project directory
Create D:\EXPERIMENTS\DAO_VOTING\ with:
  spec/, state/, outputs/, results/raw/, results/validated/, results/final/,
  devlog/, src/, papers/, papers/dao_voting_2026/,
  papers/dao_voting_2026/figures/, prompts/

### Step 2 — Write CLAUDE.md
  # Voting Power in Weighted DAOs — NORTH STAR

  ## What We Are Building
  A Banzhaf index analysis of DAO governance proving token concentration implies
  oligarchic control, with quadratic voting as the proven fix.

  ## The Core Claim
  Effective number of decision-makers in a DAO is bounded by 1/HHI. For real
  crypto token distributions, fewer than 10 entities control governance.
  Quadratic voting redistributes power to small holders.

  ## Frozen Parameters (quick reference)
  | Parameter | Value | Source |
  |-----------|-------|--------|
  | Banzhaf index | swings_i / total_swings | Banzhaf 1965 |
  | HHI | sum(s_i^2) | Standard IO |
  | Penrose law | power ~ sqrt(weight) | Penrose 1946 |
  | Quadratic voting | cost = votes^2 | Lalley & Weyl 2018 |

  ## Critical Enforcements
  - Banzhaf index, not Shapley-Shubik — throughout
  - Herfindahl bound must be a formal theorem
  - Real DAO token distributions, not hypothetical
  - Quadratic voting improvement formally proven, not described

### Step 3 — Write spec/frozen_spec.md
Fill from FROZEN_SPEC_PARAMETERS above. Lock date today.
Locked by: James P Rice Jr.

### Step 4 — Initialize state files
state/state_vector.md — TURN: 0, MILESTONE: M1, MODE: INIT
state/innovation_log.md — header with project name and timestamp
state/dead_ends.md — header with project name

### Step 5 — Copy all prompts from SHELL
Copy from D:\EXPERIMENTS\SHELL\prompts\ into D:\EXPERIMENTS\DAO_VOTING\prompts\:
  04_paper_orchestrator.md
  05_author.md
  06_peer_reviewer.md
  07_editor.md
  run_milestone.md
Do NOT copy 00_init.md — SHELL-level only.

Also write prompts/turn_prompts_log.md:
  # TURN PROMPTS LOG — dao_voting_2026
  # Every exact prompt logged here. Required for reproducibility.
  [No entries yet. First entry written at Turn 1 M1.]

### Step 5b — Write run_pipeline.ps1

Write run_pipeline.ps1 in the project root (D:\EXPERIMENTS\DAO_VOTING\) with
the slug set to "dao_voting_2026". Use the template from
D:\EXPERIMENTS\SHELL\prompts\00_init.md Step 15, replacing [SLUG] with
dao_voting_2026 and [SLUG] paths with DAO_VOTING.

### Step 6 — Write STATUS.md
Phase: INIT -> PAPER PIPELINE
Turn: 0
What Is Done: Scaffolded. Spec locked.
What Is Next: Author writes M1 (weighted voting game, Banzhaf index, token distributions).

### Step 7 — Write remaining required files

Write README.md:
  # Voting Power in Weighted DAOs
  **Author:** James P Rice Jr.
  **Target:** Social Choice and Welfare
  **Status:** In progress
  ## What This Is
  A Banzhaf index analysis of DAO governance. Token concentration implies oligarchy.
  Quadratic voting is the proven fix.
  ## How to Run
  claude --dangerously-skip-permissions prompts/04_paper_orchestrator.md

Write CHAIN_PROMPT.md:
  # CHAIN PROMPT — DAO Voting Paper | THIS FILE WINS ALL CONFLICTS
  Name: Voting Power in Weighted DAOs
  Author: James P Rice Jr.
  Core claim: Effective decision-makers bounded by 1/HHI. Real DAOs are
  oligarchies. Quadratic voting redistributes power.
  Pipeline: PAPER — Claude-only, milestone-by-milestone gating.
  Author: Claude | Peer Reviewer: Claude | Editor: Claude
  [today] | Initialized from SHELL v3

Write SACRED_FILES.md:
  # SACRED FILES | Lock date: [today] | Locked by: James P Rice Jr.
  | File | Reason | Locked |
  |------|--------|--------|
  | spec/frozen_spec.md | Oracle. Never modify after lock. | [today] |

Write BEST_PRACTICES.md:
  # BEST PRACTICES — DAO Voting Paper | SHELL v3 standards
  - Banzhaf index throughout, not Shapley-Shubik. Explain the choice.
  - Herfindahl bound proven as a theorem, not observed.
  - Real DAO token distributions from named projects with cited sources.
  - Quadratic voting power redistribution formally demonstrated (before/after).
  - Penrose approximation's validity domain explicitly characterized.
  - Natural enemy: Somin et al. 2023 — must distinguish our contribution.
  - Sensitivity analysis: vary token distribution parameters, threshold rules.
  - Milestone-by-milestone. No section opens until previous is Peer Reviewer ACCEPT.
  - Every figure needs Python/matplotlib code. No orphan figure references.
  - Lean-ready proofs: all hypotheses explicit, every derivation step justified.

Write devlog/DEV_LOG.md:
  # DEVELOPMENT LOG — dao_voting_2026
  ## [today] — Session 1
  Initialized from SHELL v3. Spec locked. All files created. Git initialized.
  Pipeline: PAPER, Claude-only, milestone-by-milestone gating.
  Models: Claude (Author) -> Claude (Peer Reviewer) -> Claude (Editor).

Write outputs/options.md:
  # OPTIONS LOG — dao_voting_2026
  [No options yet.]

Write outputs/state_vector_backup.md:
  # STATE VECTOR BACKUP — dao_voting_2026
  [No backups yet.]

### Step 8 — Initialize git
  cd D:\EXPERIMENTS\DAO_VOTING
  git init
  git add -A
  git commit -m "Turn 0 | Init | dao_voting_2026"

### Step 9 — Print confirmation and hand off:
  PROJECT INITIALIZED: dao_voting_2026
  Spec locked. All files created. Git initialized.
  Beginning paper pipeline — M1 (Weighted Voting Game + Banzhaf Index) first.
  Output: papers/dao_voting_2026/paper.md
  Running. James P Rice Jr. reviews when done.

---

## HAND OFF — EXECUTE PAPER PIPELINE

Load prompts/04_paper_orchestrator.md.

Pass:
  PROBLEM: [full PROBLEM text above]
  DATA: Real DAO token distributions required (Uniswap, Compound, MakerDAO, Aave).
        Frozen spec parameters are analytical definitions.
  SLUG: dao_voting_2026
  DRIFT_RISKS: [paste KNOWN_DRIFT_RISKS into every Author and Reviewer prompt]
  FROZEN_SPEC: [pass full frozen_spec.md to Peer Reviewer on every pass]

Run the full milestone pipeline: M1 -> M2 -> M3 -> M4.
Do not skip milestones. Do not open M2 until M1 is Peer Reviewer ACCEPT.
Halt only on HALT CONDITIONS.
When done write papers/dao_voting_2026/paper.md and halt.
James P Rice Jr. reviews it.
