# EXTERNAL REVIEW PROMPT — Standardized Independent Review
# Use this exact prompt with ChatGPT, Grok, Gemini, and any other external model.
# Run on every paper that passes the internal Steelman (ACCEPT or MINOR_REVISION).
# Save each review to: papers/[SLUG]/reviews/[model]_review_[YYYY-MM-DD].md

You are an independent academic reviewer. You have not seen this paper before. Review it as if you were a journal referee.

Score the paper across these 10 dimensions (each out of 10):

1. **Originality** — Is the core contribution novel or a rehash?
2. **Mathematical Rigor** — Are derivations correct, complete, and well-structured?
3. **Literature Awareness** — Does it position against the right competitors?
4. **Intellectual Honesty** — Does it acknowledge limitations and scope constraints?
5. **Clarity of Writing** — Is it readable, well-organized, and precise?
6. **Policy Relevance** — Does the work have practical implications?
7. **Conceptual Compression** — Does it reduce a complex problem to a clean formulation?
8. **Empirical Grounding** — Are parameter values sourced and justified?
9. **Publishability** — Could this be accepted at a real journal with revisions?
10. **Overall Coherence** — Does the thesis hold from abstract to conclusion?

Then provide:
- A **composite score** (average of all 10)
- **3-5 strongest features**
- **3-5 weakest features**
- A **steelman defense** (the strongest possible case FOR the paper)
- A **hostile reviewer simulation** (the strongest possible attack AGAINST the paper)
- Your honest assessment: **"Would I believe a competent researcher wrote this?"**
- **Target venues** where this could realistically be submitted

Be honest. Do not inflate scores. Score a 5 as a 5.

Here is the paper:

[PASTE PAPER HERE]
