# Lessons Learned — SHELL Quality Loop

**Date:** 2026-05-12
**Source:** First overnight batch run (Conspiracy Bayes + Echo Chambers)

---

## What Worked

### 1. Pre-loading Steelman feedback into init files
Conspiracy Bayes had 7 structural fixes from a prior session baked into the init file before the quality loop ran. Result: zero structural issues on Run 1. The Steelman accepted immediately.

**Rule:** Run a paper once, steelman it, then encode ALL structural fixes into the init file before running the quality loop. Don't rely on the loop to fix fundamental spec issues.

### 2. Papers with textbook-level math converge fast
Conspiracy Bayes uses SLLN, Wald's equation, Bayesian consistency -- standard results applied to a new domain. The Author can't get these wrong. The novelty is in the application, not the math.

**Rule:** If the paper's contribution is the application (not novel math), it converges quickly. If the paper promises novel mathematical results, expect more iterations.

### 3. The quality loop detects real mathematical errors
Echo Chambers Run 2: the Steelman caught that Theorem 3 proves the opposite of the paper's central claim. This is not a style issue -- it's a fundamental logical error that would cause a desk reject.

**Rule:** Trust the Steelman on structural issues. If it says the math is wrong, it probably is.

### 4. Claim shrinkage indicates convergence
Conspiracy Bayes: 465 → 446 → 423 lines across runs. The paper tightened naturally under adversarial pressure.

**Rule:** Decreasing line count across runs is a positive signal. Increasing line count (Echo Chambers Run 4: 626 lines) may indicate the Author is adding complexity to paper over problems instead of fixing them.

---

## What Didn't Work

### 1. Frozen spec that promises more than the math can deliver
Echo Chambers spec promises: "critical connectivity threshold λ₂* below which consensus fails" (a phase transition). The actual math only gives: continuous degradation as λ₂ → 0 (no sharp transition). The Steelman caught this three times in different phrasings but the loop couldn't fix it because the SPEC itself is wrong.

**Rule:** If the Steelman flags the same conceptual issue across 2+ runs (even if phrased differently), the problem is in the frozen spec, not the paper. Stop the loop. Revise the spec.

### 2. Revision instructions that patch symptoms instead of root causes
Each Echo Chambers run got 7-10 revision instructions, but they addressed the specific phrasing the Steelman objected to, not the underlying mathematical impossibility. Run 2 "fixed" Run 1's threshold issue but introduced a theorem that contradicts the central claim.

**Rule:** Before injecting revision instructions, check whether they address a phrasing problem or a mathematical impossibility. If the math can't deliver what the spec promises, no amount of revision will fix it.

### 3. Regression across runs (Echo Chambers Run 3)
Run 3 had proofs entirely absent -- theorems with tombstone symbols but no proof bodies. Runs 1 and 2 had proofs. This is a regression: the accumulated revision instructions overwhelmed the Author context and something got dropped.

**Rule:** After 3 runs, the init file accumulates enough revision briefs to confuse the Author. Consider resetting: take the best run's paper.md, extract what worked, write a clean v2 init file, and start fresh.

### 4. Rate limiting killed Run 4 of both papers
Claude Max hit its weekly limit during Run 4 of both loops. The Steelman returned "You've hit your limit" instead of a critique.

**Rule:** Plan for rate limits. 3 runs per paper per session is a safe budget. Run the quality loop with --max-runs 3 unless you know you have headroom.

---

## Patterns to Detect Automatically

These should eventually be checked by the quality loop before starting the next run:

1. **Spec-math mismatch:** If the Steelman flags the same conceptual issue (even rephrased) across 2 consecutive runs → HALT and flag for spec revision
2. **Proof regression:** If Run N has fewer proved theorems than Run N-1 → flag regression, consider reverting to prior run's content
3. **Line count explosion:** If Run N is >30% longer than Run N-1 → the Author is adding complexity instead of fixing problems
4. **Repeated revision instructions:** If the same instruction appears in 2+ consecutive patches → the instruction isn't being followed, investigate why
5. **Rate limit detection:** If Steelman critique contains "hit your limit" or is < 100 chars → stop loop, don't patch init with garbage

---

## Recommended Workflow (Updated)

1. Write init file with frozen spec
2. Run paper once manually (`claude --dangerously-skip-permissions init_file.md`)
3. Steelman it manually (in a Claude session, paste the paper)
4. Encode ALL structural fixes into the init file
5. THEN run the quality loop (`.\run_quality_loop.ps1 -InitFile init.md -MaxRuns 3`)
6. If Steelman ACCEPTs on Run 1 → done
7. If same conceptual issue appears on Runs 1 and 2 → stop, revise spec
8. If Run 3 shows regression → use Run 2's paper, don't continue
