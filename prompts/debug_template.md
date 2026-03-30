# DEBUG TEMPLATE
# Use for: bug diagnosis and fix
# Copy this file, fill in ERROR DESCRIPTION, send to Claude

================================================================================
CONTEXT INJECTION — READ FIRST
================================================================================

Before diagnosing anything, read:
  1. CHAIN_PROMPT.md
  2. CLAUDE.md
  3. state/innovation_log.md (last 3 entries)

================================================================================
BUG REPORT
================================================================================

ERROR TYPE: [ Exception / Wrong Output / Performance / Logical Error ]

ERROR MESSAGE (paste exact traceback):
  [PASTE HERE]

HOW TO REPRODUCE:
  [Exact command that triggers the error]

EXPECTED BEHAVIOR:
  [What should happen]

ACTUAL BEHAVIOR:
  [What actually happens]

LAST CHANGE MADE:
  [What changed before this error appeared]

================================================================================
DEBUGGING INSTRUCTIONS
================================================================================

1. Read the traceback — identify exact line and file
2. Read that file and surrounding context
3. Identify root cause (not where it throws — WHY it throws)
4. Fix the minimum code needed to resolve it
5. Do not change unrelated code
6. Verify: run 3-seed sigma check after fix
7. Update devlog/DEV_LOG.md with DEBUG entry: root cause + fix
8. If the bug reveals a systemic issue, document in state/dead_ends.md
