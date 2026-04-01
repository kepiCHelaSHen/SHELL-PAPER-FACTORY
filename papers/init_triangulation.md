# INIT — MULTI-MODEL TRIANGULATION CONSENSUS ACCURACY
# Pre-filled. Ready to run.
# claude --dangerously-skip-permissions papers/init_triangulation.md

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: Multi-Model Consensus as a Specification Drift Detector: When Three LLMs Agree, They Are Right
SLUG: triangulation_2026
AUTHOR: James P Rice Jr.
TARGET_VENUE: NeurIPS or ICML (Workshop on Reliable AI) — Zenodo preprint first
PIPELINE: PAPER

PROBLEM:
Large language models generate from training priors rather than user specifications,
producing confident but incorrect outputs — a phenomenon termed specification drift
(Rice 2026, DOI: 10.5281/zenodo.19217024). The standard response is to improve
individual model accuracy. This paper demonstrates a fundamentally different approach:
exploit the fact that different models have DIFFERENT training priors. When multiple
LLMs with independent training data are queried independently on the same question
and unanimously agree, their consensus accuracy exceeds any individual model's accuracy.

We present empirical results from a controlled experiment: 20 test cases with known
correct answers, each designed to have a specific "drift target" (the wrong answer
that training priors would produce). Three frontier LLMs (GPT-4o, Grok-3, Claude)
were queried independently with identical prompts at low temperature (0.2).

Results:
- Individual accuracy: GPT-4o 95%, Claude 95%, Grok-3 80%
- Unanimous consensus (all 3 agree): 16 cases, 100% correct (16/16)
- When models disagreed: the dissenting model was wrong in every case
- The one case where ALL three drifted (Stag Hunt payoffs): each produced a
  DIFFERENT wrong answer from its own training prior — three independent priors,
  three independent failures, zero consensus on the wrong answer

The result formalizes a mechanism: multi-model consensus acts as a specification
drift detector because specification-compliant answers are stable across priors
(all models converge to the same correct answer) while prior-driven answers are
unstable (different priors produce different wrong answers). Unanimous agreement
is therefore a sufficient statistic for correctness in this experimental regime.

FROZEN_SPEC_PARAMETERS:

PARAMETER: Number of test cases
VALUE: 20
UNIT: dimensionless
TOLERANCE: exact
SOURCE: Rice [this paper] — experimental design
NOTES: Each test case has a known correct answer and a documented drift target.

PARAMETER: Models tested
VALUE: GPT-4o (OpenAI), Grok-3 (xAI), Claude (Anthropic)
UNIT: N/A
TOLERANCE: exact — these specific models
SOURCE: Rice [this paper]
NOTES: Three frontier LLMs with independent training data. Temperature 0.2 for all.

PARAMETER: Individual accuracy — GPT-4o
VALUE: 19/20 = 95%
UNIT: proportion
TOLERANCE: exact count
SOURCE: Rice [this paper] — experimental result
DRIFT_RISK: LOW — this is measured data, not a parameter to generate

PARAMETER: Individual accuracy — Grok-3
VALUE: 16/20 = 80%
UNIT: proportion
TOLERANCE: exact count
SOURCE: Rice [this paper] — experimental result
DRIFT_RISK: LOW

PARAMETER: Individual accuracy — Claude
VALUE: 19/20 = 95%
UNIT: proportion
TOLERANCE: exact count
SOURCE: Rice [this paper] — experimental result
DRIFT_RISK: LOW

PARAMETER: Unanimous consensus accuracy
VALUE: 16/16 = 100%
UNIT: proportion
TOLERANCE: exact count
SOURCE: Rice [this paper] — experimental result
DRIFT_RISK: HIGH — Author may soften "100%" to "near-perfect" or add caveats.
  The result is 16/16 = 100%. State it. The small sample caveat belongs in
  boundary conditions, not in the result statement.

PARAMETER: Unanimous wrong cases
VALUE: 0 (Stag Hunt had all 3 wrong but with different answers — not unanimous)
UNIT: count
TOLERANCE: exact
SOURCE: Rice [this paper]
NOTES: All three models got Stag Hunt wrong, but each produced a DIFFERENT wrong
  answer. This is not unanimous agreement on wrong — it is three independent
  prior-driven failures. The consensus mechanism correctly produces NO consensus
  in this case, which is the detection working.

MILESTONES:

M1: Formal framework — define specification drift, training prior, consensus
    mechanism, and the key theoretical objects. Prove that if priors are
    independent and specification-compliant answers are unique, unanimous
    consensus is a sufficient statistic for correctness. This is the theorem
    that explains WHY the empirical result works.

M2: Experimental design and results — present the 20 test cases, the
    methodology, the raw results. Prove the statistical significance of
    the consensus accuracy vs individual accuracy difference. The empirical
    result is the evidence; the theorem from M1 is the explanation.

M3: Application and boundary conditions — when does triangulation fail?
    What if all models share a training prior bias? What if the question
    has no unique correct answer? Sensitivity analysis on number of models,
    temperature, question type. Competing approaches (ensembling, self-
    consistency, chain-of-thought) and why they don't achieve the same thing.

M4: Full paper assembly — Introduction (the drift problem), Related Work
    (ensemble methods, self-consistency, constitutional AI, debate),
    Discussion (implications for AI safety, scientific code generation,
    the DVL framework), Conclusion.

ORACLE:
The paper is valid if and only if:
1. The theorem in M1 provides formal conditions under which consensus
   implies correctness (not just an empirical observation)
2. The experimental results in M2 are presented with exact counts, not
   rounded percentages, with statistical tests
3. The boundary conditions in M3 identify specific failure modes (shared
   prior bias, ambiguous questions) with formal analysis
4. The Stag Hunt case is analyzed as the key example of the detection
   mechanism working (different wrong answers = no consensus = drift flagged)
5. The paper connects to Rice (2026) DOI: 10.5281/zenodo.19217024 as the
   framework this result validates

KNOWN_DRIFT_RISKS:
- Softening the 100% result to "near-perfect" — the result is 16/16. State it.
  The sample size caveat goes in boundary conditions, not the result.
- Treating the Stag Hunt case as a "failure" — it is the mechanism working.
  Three different wrong answers means no consensus, which means drift detected.
- Conflating this with ensemble methods — ensemble methods average predictions
  from the SAME model. This uses DIFFERENT models with DIFFERENT priors. The
  mechanism is fundamentally different: prior diversity, not prediction averaging.
- Conflating with self-consistency (Wang et al. 2023) — self-consistency samples
  multiple outputs from ONE model. Same prior, same blind spots. This uses
  independent priors.
- Not formalizing the theorem — the empirical result alone is a workshop paper.
  The theorem (independent priors + unique correct answer = consensus implies
  correctness) is what makes it a full paper.
- PROOF STRATEGY: The theorem must use a probabilistic argument showing that
  under prior independence, the probability of unanimous wrong consensus
  decreases exponentially with the number of models, while the probability of
  unanimous correct consensus is stable. This is a coupon-collector / birthday
  paradox type argument applied to prior diversity.
- Not citing Rice (2026) DOI: 10.5281/zenodo.19217024 — this paper is the
  empirical validation of that framework. The citation is mandatory.
- Making the experiment sound like a survey — it is a controlled experiment
  with known ground truth, not a poll of LLM opinions.
- Figures required:
    Figure 1: Accuracy comparison (individual vs majority vs unanimous) — bar chart
    Figure 2: Agreement matrix — heatmap showing which models agreed on which questions
    Figure 3: The Stag Hunt case — visualization of three different wrong answers
              from three different priors

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1 — Create project directory
Create D:\EXPERIMENTS\TRIANGULATION\ with:
  spec/, state/, outputs/, results/raw/, results/validated/, results/final/,
  devlog/, src/, papers/, papers/triangulation_2026/,
  papers/triangulation_2026/figures/, prompts/

### Step 2 — Write CLAUDE.md
  # Multi-Model Consensus as a Specification Drift Detector — NORTH STAR

  ## What We Are Building
  A formal paper proving that when 3 LLMs with independent priors unanimously
  agree, their consensus accuracy is 100% (16/16) vs 80-95% individual.

  ## The Core Claim
  Unanimous multi-model consensus is a sufficient statistic for correctness
  when priors are independent and the correct answer is unique.

  ## The Key Data
  20 test cases. GPT-4o 95%, Grok-3 80%, Claude 95%. Unanimous: 100%.
  Stag Hunt: all 3 wrong but different wrong answers — detection works.

  ## Frozen Parameters
  | Parameter | Value | Source |
  |-----------|-------|--------|
  | GPT-4o accuracy | 19/20 (95%) | Experiment |
  | Grok-3 accuracy | 16/20 (80%) | Experiment |
  | Claude accuracy | 19/20 (95%) | Experiment |
  | Unanimous accuracy | 16/16 (100%) | Experiment |

  ## Critical Enforcements
  - 100% is the result. Do not soften it.
  - Stag Hunt is the mechanism working, not a failure.
  - This is NOT ensemble methods. Different models, different priors.
  - Theorem required: formalize why consensus implies correctness.
  - Cite Rice (2026) DOI: 10.5281/zenodo.19217024

### Step 3 — Write spec/frozen_spec.md
Use the FROZEN_SPEC_PARAMETERS above. Lock date today.

### Step 4 — Initialize state files
state/state_vector.md — TURN: 0, MILESTONE: M1, MODE: INIT
state/innovation_log.md — YAML format header
state/dead_ends.md — header

### Step 5 — Copy all prompts from SHELL
Copy from D:\EXPERIMENTS\SHELL\prompts\ into TRIANGULATION\prompts\:
  04_paper_orchestrator.md
  05_author.md
  06_peer_reviewer.md
  07_editor.md
  run_milestone.md
Do NOT copy 00_init.md — SHELL-level only.

Also write prompts/turn_prompts_log.md:
  # TURN PROMPTS LOG — triangulation_2026
  # Every exact prompt logged here. Required for reproducibility.
  [No entries yet. First entry written at Turn 1 M1.]

### Step 5b — Write run_pipeline.ps1

Write run_pipeline.ps1 in the project root (D:\EXPERIMENTS\TRIANGULATION\) with
the slug set to "triangulation_2026". Use the template from
D:\EXPERIMENTS\SHELL\prompts\00_init.md Step 15, replacing [SLUG] with
triangulation_2026 and [SLUG] paths with TRIANGULATION.

### Step 6 — Write STATUS.md
Phase: INIT → PAPER PIPELINE
Turn: 0
What Is Done: Scaffolded. Spec locked. Experiment data available.
What Is Next: Author writes M1 (formal framework + theorem).

### Step 7 — Write remaining required files
README.md, CHAIN_PROMPT.md, SACRED_FILES.md, BEST_PRACTICES.md,
.gitignore, devlog/DEV_LOG.md, outputs/options.md,
outputs/state_vector_backup.md

CHAIN_PROMPT.md must include:
  Pipeline: PAPER — Claude-only, milestone-by-milestone gating
  Author: Claude | Peer Reviewer: Claude | Editor: Claude

### Step 7b — Copy experiment data
Copy the experiment results into the project for the Author to reference:
  Copy D:\EXPERIMENTS\SHELL\outputs\triangulation_experiment.md
  to D:\EXPERIMENTS\TRIANGULATION\data\triangulation_experiment.md

### Step 8 — Initialize git
  cd D:\EXPERIMENTS\TRIANGULATION
  git init
  git add -A
  git commit -m "Turn 0 | Init | triangulation_2026"

### Step 9 — Print confirmation and hand off

DO NOT STOP HERE. The setup is complete. Now you must execute the paper pipeline.

Read prompts/04_paper_orchestrator.md NOW and follow every instruction in it.
You are the Orchestrator. Begin at the INITIALIZE section. This is not a file
to summarize — it is your operating manual. Execute it.

YOUR INPUTS:
  PROBLEM: [the full PROBLEM text from the INPUTS section above]
  DATA: Empirical experiment results in data/triangulation_experiment.md.
        20 test cases, 3 models, known correct answers. Full raw data available.
  SLUG: triangulation_2026
  DRIFT_RISKS: [paste KNOWN_DRIFT_RISKS above into every Author and Reviewer prompt]
  FROZEN_SPEC: [pass full frozen_spec.md to Peer Reviewer on every review pass]

BEGIN NOW. Run M1. Do not ask for confirmation. Do not summarize the orchestrator.
Execute it. Write the paper.
