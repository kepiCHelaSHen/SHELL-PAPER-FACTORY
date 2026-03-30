# INIT — COMMON KNOWLEDGE PAPER
# Pre-filled. Ready to run tonight.
# Load this file and execute. No questions needed.
#
# claude --dangerously-skip-permissions papers/init_common_knowledge.md

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: A Deterministic Solution to the Infinite Regress of Common Knowledge
SLUG: common_knowledge_2025
AUTHOR: James P Rice Jr.
TARGET_VENUE: Games and Economic Behavior (Zenodo preprint first)
PIPELINE: PAPER

PROBLEM:
Common knowledge — the condition where A knows B knows A knows B knows... ad
infinitum — is foundational to game theory (Aumann 1976) but practically
unprovable in real-world multi-agent scenarios because the regress is infinite
and human agents are inconsistent. This paper proves that within a constrained
information architecture — specifically, a shared Sacred File and tracked State
Vector — two rational agents achieve common knowledge in a finite, provable
number of steps. The architecture is demonstrated using the Stag Hunt coordination
game, where common knowledge of rationality determines which Nash equilibrium
agents select. The result is a deterministic mechanism that eliminates coordination
failure without requiring repeated interaction or costly signaling.

FROZEN_SPEC_PARAMETERS:

PARAMETER: Coordination game
VALUE: Stag Hunt
SOURCE: Luce & Raiffa 1957 | Games and Decisions
NOTES: Canonical two-equilibrium coordination game. Do not substitute Prisoner's
       Dilemma or Battle of the Sexes — both have different common knowledge
       requirements.

PARAMETER: Stag Hunt payoff matrix
VALUE: (Stag,Stag)=(2,2) | (Hare,Hare)=(1,1) | (Stag,Hare)=(0,1) | (Hare,Stag)=(1,0)
SOURCE: Skyrms 2004 | The Stag Hunt and the Evolution of Social Structure | p.3-4
NOTES: These exact values. Do not normalize. Do not use generic (a,b,c,d) without
       mapping back to these values explicitly.
DRIFT_RISK: HIGH — LLM prior often uses (3,3)/(2,2)/(0,2) variant from Rousseau framing.

PARAMETER: Common knowledge definition
VALUE: Aumann 1976 partitional information model
SOURCE: Aumann 1976 | Agreeing to Disagree | Annals of Statistics 4(6):1236-1239
NOTES: Use the partition model formulation. Do not use the epistemic logic
       (K_i) formulation as primary — it can appear in discussion but the
       proof must use Aumann's model.
DRIFT_RISK: MEDIUM — LLMs often conflate mutual knowledge with common knowledge.
            Mutual knowledge (everyone knows X) ≠ common knowledge (everyone knows
            everyone knows everyone knows... X). Flag this distinction explicitly.

PARAMETER: Information architecture
VALUE: Sacred File (shared public document) + State Vector (append-only audit log)
SOURCE: Rice [this paper] — novel contribution
NOTES: The Sacred File is the mechanism. Both agents read identical content.
       The State Vector tracks consensus. These are the core novel claims.
       Do not let the Author underplay this as "just a database."

PARAMETER: Regress termination step
VALUE: Step 1 (single shared read of Sacred File achieves common knowledge)
SOURCE: Rice [this paper] — proven in M2
NOTES: This is the punchline. If both agents read the same Sacred File and
       both know the other has read it (State Vector confirms), the regress
       terminates at step 1 because the information partition collapses to
       a single element. Do not soften this claim.
DRIFT_RISK: HIGH — Author may hedge to "finite steps" without proving step 1.
            Push for the strongest defensible claim.

MILESTONES:

M1: Formal model — define agents, information partitions, Sacred File architecture,
    State Vector. Establish notation. This is the Methods section equivalent.

M2: Proof — show that Sacred File architecture achieves common knowledge at step 1
    under the Aumann partition model. Formal proof with lemmas.

M3: Stag Hunt application — apply the proof to the Stag Hunt. Show that under
    this architecture, rational agents always select (Stag, Stag). Discuss
    implications for coordination failure elimination.

M4: Full paper assembly — Introduction, related work, Discussion (implications for
    mechanism design, AI multi-agent systems, organizational theory), Conclusion.
    Ensure Abstract is self-contained. Figures if needed.

ORACLE:
The proof in M2 is valid if and only if:
1. It correctly applies the Aumann (1976) partition model formalism
2. It shows the partition collapses to a single element after both agents
   read the Sacred File
3. The step count is proven, not asserted
4. The Stag Hunt application in M3 follows from the proof — not separately argued

Peer Reviewer must check: does the M3 result FOLLOW from M2, or is it re-argued?
If re-argued, that is a flaw — the proof should do the work.

KNOWN_DRIFT_RISKS:
- Conflating mutual knowledge with common knowledge (define the distinction early,
  enforce throughout)
- Using the wrong Stag Hunt payoff matrix (enforce frozen values)
- Softening "step 1" to "finite steps" without proving the bound (enforce the claim)
- Treating the Sacred File as a metaphor rather than a formal object (it must be
  formally defined as a public information partition element)
- Adding unnecessary sections on evolutionary game theory or behavioral economics
  (this is a formal theory paper — keep it tight)

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1 — Create project directory

Create D:\EXPERIMENTS\COMMON_KNOWLEDGE\ with full subdirectory structure:
  spec/, state/, outputs/, results/raw/, results/validated/, results/final/,
  devlog/, src/, papers/, papers/common_knowledge_2025/, papers/common_knowledge_2025/figures/
  prompts/

### Step 2 — Write CLAUDE.md

Contents:
  # A Deterministic Solution to the Infinite Regress of Common Knowledge — NORTH STAR
  # Read this at the start of every session.
  # If anything conflicts with CHAIN_PROMPT.md — CHAIN_PROMPT.md wins.

  ## What We Are Building
  A formal proof that a Sacred File + State Vector architecture achieves common
  knowledge in one step, eliminating coordination failure in the Stag Hunt.

  ## Key Files
  - spec/frozen_spec.md — frozen parameters and proof obligations. Never modify.
  - state/innovation_log.md — full audit trail
  - state/state_vector.md — save game
  - state/dead_ends.md — do not repeat these
  - prompts/04_paper_orchestrator.md — the paper pipeline

  ## The Core Claim
  Within a Sacred File + State Vector information architecture, two rational agents
  achieve common knowledge at step 1 (not "finite steps" — step ONE).

  ## Frozen Parameters (quick reference)
  | Parameter | Value | Source |
  |-----------|-------|--------|
  | Game | Stag Hunt | Luce & Raiffa 1957 |
  | Payoffs | (2,2)/(1,1)/(0,1)/(1,0) | Skyrms 2004 p.3 |
  | CK definition | Aumann 1976 partition model | Ann. Stat. 4(6) |
  | Regress termination | Step 1 | Rice [this paper] |

  ## Critical Distinctions to Enforce
  - Mutual knowledge ≠ common knowledge
  - Sacred File is a formal object, not a metaphor
  - "Step 1" is a proven bound, not a hedge

  ## Do Not Touch
  See SACRED_FILES.md.

### Step 3 — Write spec/frozen_spec.md
Use the FROZEN_SPEC_PARAMETERS above. Fill every block. Write lock date as today.

### Step 4 — Initialize state files
Write state/state_vector.md, state/innovation_log.md, state/dead_ends.md
with project name and today's timestamp. TURN: 0.

### Step 5 — Copy all prompts from SHELL
Copy 04_paper_orchestrator.md, 05_author.md, 06_peer_reviewer.md,
07_editor.md into D:\EXPERIMENTS\COMMON_KNOWLEDGE\prompts\
Do NOT copy 00_init.md — that is SHELL-level only.

Also write prompts/turn_prompts_log.md:
  # TURN PROMPTS LOG — common_knowledge_2025
  # Every exact prompt logged here. Required for reproducibility.
  [No entries yet. First entry written at Turn 1 M1.]

### Step 6 — Write STATUS.md
Phase: INIT → PAPER PIPELINE
Turn: 0
What Is Done: Scaffolded. Spec locked.
What Is Next: Author writes M1 (formal model).

### Step 7 — Write remaining required files

Write README.md:
  # A Deterministic Solution to the Infinite Regress of Common Knowledge
  **Author:** James P Rice Jr.
  **Target:** Games and Economic Behavior (Zenodo preprint first)
  **Status:** In progress
  ## What This Is
  A formal proof that a Sacred File + State Vector architecture achieves
  common knowledge in one step, eliminating coordination failure in the Stag Hunt.
  ## How to Run
  claude --dangerously-skip-permissions prompts/04_paper_orchestrator.md

Write CHAIN_PROMPT.md:
  # CHAIN PROMPT — Common Knowledge Paper | THIS FILE WINS ALL CONFLICTS
  Name: A Deterministic Solution to the Infinite Regress of Common Knowledge
  Author: James P Rice Jr. | Target: Games and Economic Behavior
  Core claim: Sacred File + State Vector achieves common knowledge at step 1.
  Pipeline: PAPER — multi-model triangulation, milestone-by-milestone gating.
  Author: Grok-3 (xAI, temp 0.7) | Peer Reviewer: GPT-4o (OpenAI, temp 0.2) | Editor: Claude
  [today] | Initialized from SHELL v3

Write SACRED_FILES.md:
  # SACRED FILES | Lock date: [today] | Locked by: James P Rice Jr.
  | File | Reason | Locked |
  |------|--------|--------|
  | spec/frozen_spec.md | Oracle. Never modify after lock. | [today] |

Write BEST_PRACTICES.md:
  # BEST PRACTICES — Common Knowledge Paper
  - Formalism first. Definitions Block before everything.
  - Lean-ready proofs. Every hypothesis explicit. Every step justified.
  - Literature gap formula required for Halpern-Moses, Rubinstein, Monderer-Samet.
  - Boundary Conditions must name Halpern-Moses as the natural enemy.
  - Step 1 claim must be derived from the proof. Never asserted.
  - Milestone-by-milestone. No section opens until previous is Peer Reviewer ACCEPT.

Write devlog/DEV_LOG.md:
  # DEVELOPMENT LOG — common_knowledge_2025
  ## [today] — Session 1
  Initialized from SHELL v3. Spec locked. All files created. Git initialized.
  Pipeline: PAPER, multi-model triangulation, milestone-by-milestone gating.
  Models: Grok-3 (Author) → GPT-4o (Peer Reviewer) → Claude (Editor).
  Decisions: Markdown output, manual Zenodo upload, James P Rice Jr. reviews.

Write outputs/options.md:
  # OPTIONS LOG — common_knowledge_2025
  [No options yet.]

Write outputs/state_vector_backup.md:
  # STATE VECTOR BACKUP — common_knowledge_2025
  [No backups yet.]

### Step 8 — Initialize git
  cd D:\EXPERIMENTS\COMMON_KNOWLEDGE
  git init
  git add -A
  git commit -m "Turn 0 | Init | common_knowledge_2025"

### Step 9 — Print confirmation and hand off:
  ✅ PROJECT INITIALIZED: common_knowledge_2025
  🔒 Spec locked. All files created. Git initialized.
  ▶  Beginning paper pipeline — M1 (Definitions Block + Introduction) first.
  📄 Output: papers/common_knowledge_2025/paper.md
  💤 Running overnight. James P Rice Jr. reviews in the morning.

---

## HAND OFF — EXECUTE PAPER PIPELINE

Load prompts/04_paper_orchestrator.md.

Pass:
  PROBLEM: [the full PROBLEM text above]
  DATA: No empirical data. This is a formal theory paper.
        The proof itself is the result. Author derives analytically.
  SLUG: common_knowledge_2025
  DRIFT_RISKS: [paste KNOWN_DRIFT_RISKS above into every Author and Reviewer prompt]
  FROZEN_SPEC: [pass full frozen_spec.md to Peer Reviewer on every review pass]

Run the full milestone pipeline: M1 → M2 → M3 → M4.
Do not skip milestones. Do not open M2 until M1 is Peer Reviewer ACCEPT.
Halt only on HALT CONDITIONS.
When done, write papers/common_knowledge_2025/paper.md and halt.
James P Rice Jr. reviews in the morning.
