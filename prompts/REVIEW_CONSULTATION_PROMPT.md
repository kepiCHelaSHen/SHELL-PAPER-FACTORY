# REVIEW PROCESS CONSULTATION
# Paste this entire prompt into GPT, Grok, Gemini, Copilot, and any other AI you want opinions from.
# Save each response to: prompts/review_consultation_responses/[MODEL]_response.md

---

I'm building an autonomous academic paper generation framework. The system produces
rigorous, publication-ready papers through multi-agent validation. I need your help
making the EXTERNAL REVIEW step as robust as possible.

## Context

After a paper passes internal quality loops (an internal Linter and a Peer Reviewer
with a 50+ item checklist), it goes to an EXTERNAL REVIEW. This is the final gate.
The external review is run by multiple independent AI models (you are one of them).

The paper is presented AS IF A HUMAN RESEARCHER WROTE IT. The reviewer (you) should
evaluate it exactly as a journal referee would evaluate a submission from a human author.
No special treatment. No "for an AI this is good." Evaluate it on the same standard
you would hold a tenured professor to.

## Current External Review Prompt (v1)

Here is what we currently ask external reviewers to evaluate:

**10 Scored Dimensions (each out of 10):**
1. Originality — Is the core contribution novel or a rehash?
2. Mathematical Rigor — Are derivations correct, complete, and well-structured?
3. Literature Awareness — Does it position against the right competitors?
4. Intellectual Honesty — Does it acknowledge limitations and scope constraints?
5. Clarity of Writing — Is it readable, well-organized, and precise?
6. Policy Relevance — Does the work have practical implications?
7. Conceptual Compression — Does it reduce a complex problem to a clean formulation?
8. Empirical Grounding — Are parameter values sourced and justified?
9. Publishability — Could this be accepted at a real journal with revisions?
10. Overall Coherence — Does the thesis hold from abstract to conclusion?

**Qualitative Sections:**
- Composite score (average of all 10)
- 3-5 strongest features
- 3-5 weakest features
- Steelman defense (strongest case FOR the paper)
- Hostile reviewer simulation (strongest attack AGAINST the paper)
- "Would I believe a competent researcher wrote this?"
- Target venues where this could realistically be submitted

## What I Want From You

I want you to help me make this review process SIGNIFICANTLY more robust. Not
impossible to pass, but rigorous enough that anything that passes it is genuinely
publication-quality. Think of it as designing the review process for a top-tier
journal that also has forensic capabilities.

### Specifically, please provide:

**1. CRITIQUE THE CURRENT 10 DIMENSIONS**
- Are any redundant? Should any be merged?
- Are any too vague to produce consistent scores across different reviewers?
- Are any missing that a real journal referee would care about?

**2. PROPOSE ADDITIONAL SCORED DIMENSIONS**
- What dimensions are we completely missing?
- Think about: methodology, statistical validity, reproducibility, argumentation
  quality, citation integrity, internal consistency, etc.
- Only propose dimensions that would give us ACTIONABLE information. No fluff.

**3. PROPOSE BOOLEAN (YES/NO) CHECKS**
These are pass/fail gates that don't need a 1-10 score. I definitely want these two:

- **AI_WRITTEN_DETECTION**: Does this paper read as if an AI generated it? 
  (Evaluate: sentence structure variation, hedging patterns, vocabulary diversity,
  citation integration naturalness, argument flow, voice consistency, specificity
  of examples, presence of "filler" academic language)

- **EFFORT_ESTIMATION**: How much human time and expertise would this paper require
  if a human wrote it? (Provide: estimated person-hours, estimated expertise level
  required, estimated research phase duration, and a confidence rating on your estimate)

What OTHER boolean checks should we add? Think about:
- Citation fabrication detection
- Logical fallacy detection  
- Scope creep detection
- Data fabrication signals
- Methodology appropriateness
- Statistical red flags
- Formatting compliance
- Any other forensic or quality checks

**4. IMPROVE THE QUALITATIVE SECTIONS**
- What qualitative assessments are we missing?
- Should the hostile reviewer simulation be more structured?
- What about a "desk rejection" check — would an editor even send this out for review?

**5. SCORING METHODOLOGY**
- Should we weight dimensions differently?
- Should there be "automatic fail" thresholds on certain dimensions?
- How should the composite score be calculated?
- Should there be sub-scores within dimensions?

**6. REVIEW FRAMING**
- How should the reviewer persona be framed for maximum rigor?
- What instructions would make the review more consistent across different AI models?
- What biases should we explicitly instruct the reviewer to guard against?

**7. ANYTHING ELSE**
- What am I not thinking of?
- What would a real journal editor want that isn't captured here?
- What forensic checks exist in real peer review that we should add?

## Format Your Response As:

### CURRENT DIMENSIONS: KEEP / MODIFY / DROP
[For each of the 10 current dimensions]

### PROPOSED NEW SCORED DIMENSIONS
[Numbered list with name, description, and why it matters]

### PROPOSED BOOLEAN CHECKS
[Numbered list with name, what to check, and pass/fail criteria]

### QUALITATIVE SECTION IMPROVEMENTS
[Specific additions or modifications]

### SCORING METHODOLOGY RECOMMENDATIONS
[Weights, thresholds, calculation method]

### REVIEWER PERSONA & FRAMING RECOMMENDATIONS
[How to frame the prompt for maximum consistency and rigor]

### WILD CARDS — THINGS YOU THINK WE'RE MISSING
[Anything not covered above]

Be brutally honest. I'd rather have too many suggestions to filter down than miss
something important. The goal is a review process that, if a paper passes it across
multiple independent AI reviewers, we can be genuinely confident it's publication-quality.
