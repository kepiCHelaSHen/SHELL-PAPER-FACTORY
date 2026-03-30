# ITERATION TEMPLATE
# Use for: targeted changes, bug fixes, new features, parameter tuning
# Copy this file, fill in the sections, send to Claude

================================================================================
CONTEXT INJECTION — READ FIRST
================================================================================

Before doing anything, read:
  1. CHAIN_PROMPT.md
  2. CLAUDE.md
  3. state/innovation_log.md (last 3 entries)
  4. state/dead_ends.md

Do not refactor unless explicitly asked.
Do not touch SACRED_FILES.md listed files.

================================================================================
CHANGE REQUEST
================================================================================

TYPE: [ BUG FIX / NEW FEATURE / ENHANCEMENT / PARAMETER TUNING ]

DESCRIPTION:
  [Describe exactly what needs to change and why]

FILES LIKELY AFFECTED:
  [List files you think need to change]

ACCEPTANCE CRITERIA:
  [How do we know this is done correctly?]

DO NOT CHANGE:
  [List anything that must not be touched]

================================================================================
INSTRUCTIONS
================================================================================

1. Make targeted, minimal changes only
2. Explain what changed and why before making changes
3. If bug: show the root cause before fixing
4. If new feature: confirm it does not touch sacred files
5. Run the sigma gate: 3 seeds minimum after any change
6. Update devlog/DEV_LOG.md with a new entry
7. Update CHAIN_PROMPT.md CONFIRMED DECISIONS if any design decision changed
8. Git commit with message: "[TYPE] | [one-line summary]"
