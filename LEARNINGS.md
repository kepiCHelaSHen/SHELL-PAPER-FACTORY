# LEARNINGS — Accumulated Operational Knowledge
# Updated: 2026-05-15
# Read this before writing any init file, modifying the pipeline, or running papers.

---

## 1. Init File Quality

**Every bad init costs $25-75 in wasted tokens. Triple-check before running.**

### 1.1 ASSAY Integration Must Be Calibrated, Not Decorative
- DO NOT just cite ASSAY values as context. The Author must USE them to calibrate
  and TEST the theoretical model's predictions.
- BAD: "The ASSAY report found phi = 7.39 for psychology. Our model addresses
  publication bias." (decorative)
- GOOD: "Setting phi = 7.39 (ASSAY Report PHI_EST, 95% CI [5.0, 10.5]) in our
  threshold formula yields phi* = 2.0 for psychology, confirming that the field
  operates above its critical threshold." (calibrated)

### 1.2 Sanity Check ASSAY Values Against Model Domains
- Before putting any ASSAY value in an init, verify it falls within the model's
  valid parameter range.
- Example failure: ASSAY computed coverage gaps that implied p* > 1 for pertussis.
  p* is a probability — it CANNOT exceed 1. The init should have flagged this.
- Rule: Add explicit domain constraints to drift risks:
  "If any ASSAY-computed value falls outside [valid range], flag it in the paper
  and explain why the model's domain is violated. Do not silently use invalid values."

### 1.3 The Init Is the Most Expensive File in the System
- A prompt file costs nothing to iterate on.
- An init file costs $25-75 every time it runs.
- Spend 10 minutes reviewing an init to save $75 on a failed run.

### 1.4 "If Available" Language Is Banned
- Never write "if ASSAY data is available" in an init.
- Either the data IS available (point to the exact path) or it ISN'T (don't reference it).
- Ambiguous data references cause the Author to hallucinate values or write "illustrative."

---

## 2. Steelman Classification

### 2.1 Structural = Mathematical Errors Only
- A proof is wrong (logical error, incorrect derivation)
- A theorem's conditions are violated within the paper's own proof
- A definition is internally inconsistent
- NOTHING ELSE is structural. Not novelty disagreements, not "trivial algebra,"
  not competing models, not framing concerns.

### 2.2 False Claims About Prior Work = Citation Error, Not Structural
- "Ioannidis has no closed-form threshold" is factually wrong but it's a
  citation/framing error, not a math error.
- This distinction took 5 iterations to get right. Do not regress.

### 2.3 The Steelman Ignores Rubrics in Prompts
- Putting the rubric in the Steelman prompt is necessary but not sufficient.
- The rubric must also be in the orchestrator (04_paper_orchestrator.md) where
  the verdict is evaluated.
- Both must agree or the Steelman will classify framing as structural.

---

## 3. Agent Dispatch Architecture

### 3.1 Each Agent Gets Fresh Context
- Author, Peer Reviewer, Steelman, Editor are separate agents.
- Each receives ONLY what it needs for its role.
- This prevents context saturation and keeps each agent focused.

### 3.2 Files Are the Memory, Not Context
- state_vector.md, innovation_log.md, dead_ends.md persist between agents.
- The orchestrator reads files and passes relevant content to each agent.
- No agent needs the full history — just what's relevant to its current task.

### 3.3 Steelman Feedback Flows Through Orchestrator
- Between quality loop runs, the orchestrator reads the steelman critique
  and passes relevant items as ADDITIONAL_DRIFT_RISKS to the next run's Author.
- NO init file patching. The orchestrator holds the context.

---

## 4. Quality Loop

### 4.1 MINOR_REVISION = Stop
- The loop stops on ACCEPT or MINOR_REVISION.
- MINOR_REVISION means "publishable with minor edits" — running another
  full pipeline pass to fix 3 phrasing issues is overkill and risks regression.

### 4.2 Max 3 Runs, Then Take Best
- After 3 runs, accumulated revision briefs confuse the Author.
- If Run 3 still gets MAJOR_REVISION, take the best run and move on.

### 4.3 Revision Briefs: Latest Only
- Cap at 1 revision brief (latest only, not cumulative).
- Stacked briefs from multiple runs degrade Author performance.

---

## 5. Figure Handling

### 5.1 Code Blocks Must Be Replaced
- The orchestrator's Step 6 replaces Python code blocks with image references.
- If the Steelman sees code blocks, it flags them as structural every time.
- Verify: grep paper.md for triple-backtick python blocks after figure generation.

### 5.2 Figures Must Be Rendered, Not Referenced
- "See Figure 1" without a rendered image = Steelman structural flag.
- Every figure must exist as a PNG/PDF in the figures/ directory.

---

## 6. Dead Ends and Findings

### 6.1 Dead Ends Are Logged on Peer Reviewer REJECT
- The orchestrator appends to dead_ends.md every time the Peer Reviewer rejects.
- Format: [Turn N] Run M MX REJECT: description. REASON: checklist items.

### 6.2 Findings Are Consolidated After Each Steelman Critique
- consolidate.py --critique extracts and categorizes findings.
- consolidate.py --dead-ends extracts dead ends.
- Both are called by the quality loop launcher as a safety net.
- FIXED 2026-05-15: Launcher now recursively searches for ALL steelman_critique*.md
  and ALL dead_ends.md files in the project directory, not just expected locations.
  Previously the orchestrator was supposed to call consolidate.py during the run,
  but since that depends on Claude following a prompt instruction (unreliable),
  the launcher now guarantees consolidation post-run regardless.

### 6.3 Pre-Loading Findings Works
- Conspiracy Bayes: 7 pre-loaded findings -> 0 structural issues on Run 1.
- v2 papers (tonight): pre-loaded cross-paper findings eliminated scope disguise,
  placeholder tables, Lean-readiness claims, and figure code blocks.

---

## 7. ASSAY Integration

### 7.1 ASSAY Reports Are Evidence, Not Arguments
- THESIS interprets. ASSAY computes.
- ASSAY's integration_block.yaml includes forbidden_interpretations that
  THESIS must respect.

### 7.2 Negative Results Are Valuable
- Geo Variation: density-spending relationship is negative (opposite of SID).
- Drug Spending: Pareto model too simple for real data.
- Both make the papers MORE credible, not less.

### 7.3 ASSAY Data Must Be Calibrated, Not Just Cited
- The Author must use ASSAY values to test model predictions.
- Show: "Model predicts X. ASSAY computed Y. They match / they don't match / here's why."
- NOT: "ASSAY found X. Our model is about the same topic."

### 7.4 Check ASSAY Report Completeness Before Writing Init
- Does the ASSAY report have an integration_block.yaml? 
- Does it have rendered figures?
- Are the computed values within the model's valid domain?
- Are there forbidden_interpretations the paper must respect?

### 7.5 ASSAY Integration Is Enforced at THREE Levels (Fixed 2026-05-15)
Previously, ASSAY integration was only in the init file. This meant one bad
init could waste $75. Now it's enforced at:

1. **Orchestrator (04_paper_orchestrator.md):** Reads ASSAY integration blocks
   before dispatching Author. Checks domain constraints. Passes forbidden
   interpretations to both Author and Peer Reviewer. Flags out-of-domain values.

2. **Author (05_author.md, Rule 5):** Explicit instructions to CALIBRATE against
   ASSAY data, not just cite it. Must respect domain constraints and forbidden
   interpretations. Must cite ASSAY report IDs.

3. **Peer Reviewer (06_peer_reviewer.md, U8):** New checklist item that catches:
   - Decorative citation without calibration → REJECT
   - Domain constraint violations used silently → REJECT
   - Forbidden interpretations violated → REJECT
   - "Illustrative" language for computed values → REJECT
   - Missing ASSAY report ID citations → REJECT

This three-level enforcement means a bad init can't slip through — even if the
init is vague about ASSAY usage, the Peer Reviewer will catch it.

---

## 8. External Review

### 8.1 Standardized Prompt at prompts/09_external_review.md
- Same prompt for all 3 models (GPT, Grok, Gemini).
- 10 dimensions, composite score, steelman, hostile, credibility assessment.

### 8.2 Grok Is the Toughest Reviewer
- GPT tends generous (8-9 range).
- Gemini is moderate (7-9 range).
- Grok is harsh and catches real issues (6-8 range).
- If Grok gives 7+, the paper is genuinely good.

### 8.3 Score Parsing
- Different models format scores differently.
- Parser handles: "Originality — 7/10", "**Originality (8/10)**", "Originality: 7", "Originality | 8 |"
- api.env keys must not have surrounding quotes — strip them on load.

### 8.4 API Timeouts
- Grok can take 120+ seconds on long papers.
- Set timeout to 300s for all APIs.
- Catch TimeoutError explicitly in retry logic.

---

## 9. Cost Management

### 9.1 Token Burn Per Paper
- Full pipeline (M1-M4 + reviews): ~150-200K tokens
- Steelman review: ~10-20K tokens
- 3-run quality loop: ~500-600K tokens
- External reviews (3 APIs): ~$0.50-1.00

### 9.2 Use Cheaper Models for Mechanical Roles
- Author: Opus (creative writing, proof construction)
- Steelman: Opus (finding weaknesses requires strongest model)
- Peer Reviewer: Sonnet (checklist validation, pattern matching)
- Editor: Sonnet or Haiku (formatting, prose clarity)
- Saves ~40% of token cost per run.

### 9.3 One-Shot Is the Goal
- Papers that converge on Run 1 cost 1/3 of papers that need 3 runs.
- The findings database is what makes one-shots possible.
- Every paper that one-shots saves $50-100 in token costs.

---

## 10. Evidence-First Workflow (Learned 2026-05-15)

**DO NOT write papers hoping the data will support the model. Run ASSAY first.**

### 10.1 The Old Workflow (Expensive, Risky)
1. Pick a paper idea
2. Write the paper
3. Run ASSAY for evidence
4. Hope the data confirms the model
5. If it doesn't → wasted $25-75 on a paper that can't be published

### 10.2 The New Workflow (Cheap, Safe)
1. Run ASSAY on available data ($2-5 per analysis)
2. Build a catalog of confirmed empirical findings
3. Match findings against PAPER_IDEAS.md
4. Only write papers where ASSAY confirms the core prediction
5. 100% of papers that run have empirical grounding built in

### 10.3 Viability Check
Before ANY paper init is written, verify:
- Does ASSAY data exist for this topic?
- Does the data SUPPORT the model's core prediction?
- If the data contradicts the model (e.g., Geo Variation density-spending
  negative), DO NOT write the paper. Log the negative result and move on.
- A paper arguing around contradictory data will score 7.0 or lower.
  A paper calibrated against confirming data will score 8.0+.

### 10.4 ASSAY Is Cheap, THESIS Is Expensive
- ASSAY run: $2-5 (mostly Python execution)
- THESIS run: $25-75 (full LLM pipeline)
- Running 100 ASSAY analyses: $200-500
- Running 100 THESIS papers: $2,500-7,500
- If ASSAY eliminates 20% of bad papers, it pays for itself immediately.

---

## 11. How to Hit 9s Consistently (Learned 2026-05-15)

The pipeline consistently produces 7.5-8.5 papers. The gap to 9+ is methodology.

### 11.1 What Already Works (maintain, don't fix)
- Intellectual Honesty: 9.5 average — the adversarial pipeline produces this
- Clarity of Writing: 9.0 — the Definitions Block and Author prompt handle this
- Conceptual Compression: 8.9 — the "derive threshold, map across cases" pattern
- Overall Coherence: 8.7 — consistent thesis, no drift

### 11.2 The Template for 9+ Papers
Drug Spending v3 scored 9.1 from Gemini. It did everything right:
1. ASSAY data was REAL (CMS Part D, $274B, 3,206 drugs)
2. The core theorem was TESTED against data (Lorenz overlay)
3. The test FAILED (Pareto model underestimates concentration)
4. The failure was CONFRONTED honestly (not hidden or explained away)
5. The failure was INFORMATIVE (constrains the model space, motivates richer spec)
6. The paper was TIGHT (not bloated with caveats)

### 11.3 What Separates 8 from 9 on Each Dimension

**Originality (6.5 avg → need 8+):**
- 8-level: known math applied to new domain (reparameterization)
- 9-level: the core theorem reveals something NON-OBVIOUS
- How to get there: pick paper ideas where the ASSAY data shows a SURPRISING
  pattern that the model explains. If the finding is expected, the originality
  score stays at 6-7 no matter how clean the math is.

**Empirical Grounding (5.5 avg → need 8+):**
- 8-level: cite ASSAY computed values with CIs
- 9-level: TEST model predictions against data, show match or mismatch
- 10-level: a genuine empirical contribution (new finding from real data)
- Drug Spending got 10 because the negative calibration result IS a finding
- How to get there: evidence-first workflow. Only write papers where ASSAY
  produces interesting findings, then build theory around the findings.

**Mathematical Rigor (8.4 avg → need 9+):**
- 8-level: correct proofs, well-structured, all steps justified
- 9-level: non-obvious proof technique, or result that doesn't follow
  immediately from the setup
- How to get there: avoid papers where the theorem is "solve for x in a
  known equation." Pick papers where the result requires a lemma that
  reveals structure.

**Publishability (7.3 avg → need 8+):**
- Follows from everything else. A paper with 9 on originality, 9 on
  empirical grounding, and 9 on rigor is automatically publishable.

**Literature Awareness (8.1 avg → need 9+):**
- 8-level: cite the right competitors, position correctly
- 9-level: show exactly HOW your result extends each competitor,
  derive their result as a special case, identify the precise
  assumption that distinguishes your model from theirs

### 11.4 Paper Selection Criteria (for 9+ targeting)
Before writing any init, the paper idea must pass ALL of these:
1. ASSAY data EXISTS and CONFIRMS the core prediction
2. The core finding from ASSAY is SURPRISING (not expected)
3. The theorem that explains the finding is NON-OBVIOUS
4. The model can be TESTED (not just calibrated) against the data
5. There is a NATURAL ENEMY in the literature to position against
6. The paper can be written in <800 lines (tight, not bloated)

If any of these fail, pick a different paper idea.

---

## 12. System Signature (from 40+ independent reviews)

The system consistently produces papers with this profile:

| Dimension | Typical Score | Notes |
|-----------|--------------|-------|
| Intellectual Honesty | 9-10 | System's strongest dimension |
| Clarity of Writing | 8-9 | Clean definitions, precise prose |
| Conceptual Compression | 8-9 | Reduces complex problems to clean formulations |
| Overall Coherence | 8-9 | Thesis holds from abstract to conclusion |
| Mathematical Rigor | 8-9 | Correct derivations, well-structured proofs |
| Literature Awareness | 7-8 | Good positioning against competitors |
| Policy Relevance | 7-8 | Actionable when scoped properly |
| Publishability | 7-8 | Publishable with revisions at field journals |
| Originality | 6-8 | Applied theory, not frontier math |
| Empirical Grounding | 5-7 | ASSAY integration improves this |
