# DEEP DIVE TEMPLATE
# Use for: thorough analysis of a specific subsystem, parameter set, or domain question
# Copy this file, fill in DEEP DIVE TARGET and QUESTIONS, send to Claude

================================================================================
CONTEXT INJECTION — READ FIRST
================================================================================

Before doing anything, read:
  1. CHAIN_PROMPT.md
  2. CLAUDE.md
  3. spec/frozen_spec.md
  4. state/innovation_log.md (last 3 entries)
  5. [relevant source file or domain document]

================================================================================
DEEP DIVE TARGET: [SUBSYSTEM OR DOMAIN QUESTION]
================================================================================

Domain area:     [what area of the experiment this covers]
Current status:  [what exists, what is missing]
Relevant spec:   [which frozen spec parameters are relevant]

================================================================================
DEEP DIVE QUESTIONS
================================================================================

[Paste specific questions here. Be precise.]

Examples:
  - What is the most defensible value for [parameter] given the literature?
  - How should [formula] be structured? What are the alternatives?
  - What does [source, year] actually say about [mechanism]?
  - What are the failure modes if [parameter] drifts from [spec value]?

================================================================================
DELIVERABLES
================================================================================

1. A design memo (docs/deep_dive_[topic].md):
   - Findings from the literature
   - Recommended implementation with exact parameter values
   - Tradeoffs and limitations
   - What a reviewer would challenge

2. If applicable: updated spec entry with better-grounded source citation

3. Updated CHAIN_PROMPT.md CONFIRMED DECISIONS section

4. devlog/DEV_LOG.md entry for this session

================================================================================
CONSTRAINTS
================================================================================

- Do not touch sacred files
- Do not propose parameter values without a literature source
- Do not make architectural decisions — document options and defer
- All proposed values must be traceable to a specific document, table, page
