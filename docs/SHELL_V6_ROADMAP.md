# SHELL v6 Roadmap — From Paper Factory to Scientific Reasoning Engine

**Date:** 2026-05-11
**Author:** James P Rice Jr. (feedback) + Claude (analysis)
**Status:** Design phase

---

## Context

After running the doomscrolling paper through 5 steelman iterations (v1: 3 blocking flags -> v5: 0 blocking flags, 45-55% JET acceptance probability), the following observations emerged about what SHELL is actually building and where it needs to go.

---

## 10 Design Principles (from production experience)

### 1. Binary Gating is the Core Innovation

The BLOCKING / non-blocking severity separation prevents:
- Endless rewriting
- Reviewer oscillation
- Aesthetic churn

**Rule:** Never add a third severity level between "blocks" and "doesn't block." Binary gating is why the loop terminates. Resist the temptation to add SOFT_BLOCK or CONDITIONAL_BLOCK.

**Status:** Implemented. Keep strengthening.

### 2. Regression Detection > Paper Generation

"V2 had this right. V3 regressed." -- this signal means SHELL is optimizing historically, not just locally. Most AI systems only optimize locally.

**What to build:**
- Theorem regression tests (every accepted claim becomes a test fixture)
- Citation regression tests
- Assumption regression tests
- Numerical consistency tests
- Notation drift tests
- Venue-fit regressions

**Implementation:** `src/regression_tests.py` — reads locked milestones from prior runs, generates assertions that subsequent runs must preserve.

**Priority:** HIGH — this is the difference between "generate papers" and "accumulate knowledge."

### 3. Independent Failure-Generating Reviewers

Current reviewers share Claude's ontology. Need deliberate adversarial diversity.

**Specialized reviewer personas needed:**
- Formal math reviewer (proof correctness only)
- Empirical realism reviewer (are the assumptions plausible?)
- Literature attack reviewer (is this actually novel?)
- Hidden assumption reviewer (what's unstated?)
- "Elegant nonsense" detector (technically correct but vacuous)
- Hostile journal gatekeeper (simulates Reviewer 2)
- Replication feasibility reviewer (could someone verify this?)

**Implementation options:**
- Separate prompt files per reviewer persona, cycled through by the quality loop
- Use different models for review (GPT-4o for Steelman instead of Claude) — genuinely different priors
- Multi-model review: run the same critique prompt through 2-3 models, compare

**Priority:** MEDIUM — current Steelman is good but shares the author's blind spots.

### 4. Preserve Failed Branches Permanently

Do NOT just keep winning papers. Rejected branches are scientifically valuable:
- Dead theorems
- Invalid proofs
- Overclaim collapses
- Hidden assumption discoveries
- Venue rejection simulations
- Contradictory reviewer trajectories

**What to build:** `branch_autopsy.md` — written by the quality loop when a run's Steelman verdict is REJECT, documenting WHY this version failed. This becomes a failure corpus for epistemic analysis.

**The archives may become more valuable than the papers.**

**Priority:** MEDIUM — partially implemented (auto-versioned dirs preserved), needs structured autopsy reports.

### 5. Importance Filters (Pre-Pipeline)

Biggest future risk: SHELL becomes very good at creating internally coherent formal systems that are trivial.

**Questions the system must ask BEFORE running the pipeline:**
- Why does this matter?
- Would experts care?
- Is this merely technically clever?
- Does this change a field?
- Is the effect size meaningful?
- Is this rediscovery?
- Is this externally falsifiable?

**Implementation:** An importance pre-screen that evaluates the init file's PROBLEM statement before the pipeline runs. If the answer to "who changes their behavior if this is proven?" is "nobody," the paper shouldn't be written.

**Priority:** HIGH — prevents optimizing for elegant academic artifacts instead of important scientific contributions.

### 6. Anti-Goodhart Modules

The quality loop optimizes for "Steelman ACCEPT." If the Steelman's priors are stable, the system Goodharts on publishability over correctness.

**Counter-pressure needed:**
- Novelty skepticism (is this actually new?)
- Anti-overfitting reviewer (could a simpler model explain this?)
- Replication-cost penalty (flag results nobody could verify)
- Simplicity reward (penalize complexity beyond what the result requires)
- Real-world grounding reward
- Hidden-variable attacks

**These must be separate from the Steelman** — the Steelman is already optimizing for acceptance.

**Priority:** HIGH — this happens to humans too. The system will unconsciously optimize for publishability over correctness without explicit counter-pressure.

### 7. Kill Reports

The pipeline should sometimes conclude: "This paper should die."

Currently NOVELTY_KILL is treated as a failure. It should sometimes be a SUCCESS:
- "This question isn't worth answering"
- "This approach is provably insufficient for this problem class"
- "The contribution is below the importance threshold"

**Implementation:** `--allow-kill` flag in quality_loop.py that lets the Steelman recommend termination as a positive outcome. Kill reports become first-class artifacts.

**A healthy scientific system must be able to terminate projects. Not every loop should converge.**

**Priority:** MEDIUM — maturity milestone.

### 8. The Logs Are the Real Product

The papers are proof-of-concept. The logs are the product.

What's being generated:
- Reasoning trajectories
- Theorem collapses
- Epistemic corrections
- Adversarial interactions
- Convergence patterns
- Scientific debugging behavior

**This is machine-readable scientific cognition trace data. It is extremely rare.**

**Implementation:** Formalize the log schema. Ensure structured YAML throughout. Build `src/log_analyzer.py` to extract patterns across runs.

**Priority:** HIGH — this is the moat. The paper factory is the demo.

### 9. Milestone Isolation Architecture

Fresh-context-per-milestone is a very strong design choice. It reduces:
- Context poisoning
- Recursive drift
- Hidden contamination
- Reinforcement spirals

Combined with frozen specs, sacred files, and state vectors, this approximates deterministic builds. Each milestone is a build step with defined inputs and outputs. Any step can be replayed independently.

**Status:** Implemented. Protect this property.

### 10. Epistemic Metrics

The transition from "paper factory" to "measurable scientific reasoning system."

**Currently tracked:**
- Loops, rejections, locks, regressions

**Need to track:**
- Theorem survival rate (% of claims that survive across runs)
- Reviewer disagreement entropy (how much do reviewers disagree?)
- Revision convergence slope (how fast does quality improve per run?)
- Claim shrinkage rate (how much does scope narrow under review?)
- Empirical grounding score (ratio of grounded vs ungrounded claims)
- Citation confidence score (CrossRef verification rate)
- Hidden-assumption density (assumptions per theorem)
- External falsification coverage (% of claims that are testable)
- Replication feasibility score

**Implementation:** `src/epistemic_metrics.py` — reads innovation logs and quality loop reports, computes scores across runs.

**Priority:** HIGH — once you have this, you can ask "does the system get better at reasoning over time?"

---

## Implementation Priority

### Phase 1: Foundation (do now)
1. **Regression tests** (#2) — turn locked claims into test fixtures
2. **Importance pre-screen** (#5) — prevent trivial papers
3. **Anti-Goodhart counter-pressure** (#6) — separate from Steelman

### Phase 2: Measurement (do next)
4. **Epistemic metrics** (#10) — measure reasoning quality
5. **Log analyzer** (#8) — extract patterns from cognition traces
6. **Branch autopsies** (#4) — structured failure documentation

### Phase 3: Diversity (do after)
7. **Multi-model review** (#3) — different models for Steelman
8. **Specialized reviewer personas** (#3) — cycle through in quality loop
9. **Kill reports** (#7) — positive termination as a feature

### Phase 4: Meta (long-term)
10. **Importance filters as formal module** (#5) — pre-pipeline gate
11. **Anti-Goodhart as formal module** (#6) — post-pipeline check
12. **Cross-paper regression** (#2) — claims from Paper 1 tested in Paper 2

---

## Connection to Norstella

This roadmap describes the architecture of a governed scientific reasoning system. The papers are the test harness. The real system is:
- Adversarial validation with epistemic metrics
- Regression detection across reasoning attempts
- Anti-Goodhart pressure against optimization for form over substance
- Kill conditions for unproductive research directions
- Machine-readable cognition traces as the primary data product

Applied to 20T RWD records, this becomes governed AI-driven scientific discovery with formal validation guarantees, auditable reasoning chains, and measurable epistemic quality. The paper factory is the proof of concept. The reasoning engine is the product.
