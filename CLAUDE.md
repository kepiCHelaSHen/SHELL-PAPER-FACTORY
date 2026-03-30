# [EXPERIMENT NAME] — NORTH STAR
# Read this at the start of every session. Two minutes or less.
# If anything here conflicts with CHAIN_PROMPT.md — CHAIN_PROMPT.md wins.

## What We Are Building
[One sentence.]

## Key Files
- `CHAIN_PROMPT.md` — Master doc. All decisions. Authoritative.
- `spec/frozen_spec.md` — The oracle. Never modify after lock.
- `state/innovation_log.md` — Full audit trail.
- `state/state_vector.md` — Save game. Read after every context reset.
- `state/dead_ends.md` — Failed approaches. Do not repeat.
- `prompts/00_orchestrator.md` — The loop. Run with Claude CLI.

## Frozen Coefficients
[Paste the frozen spec table here — the most critical parameters at a glance]

| Parameter | Value | Source |
|-----------|-------|--------|
| [param]   | [val] | [src]  |

## Architecture Rules (Reviewer enforces these)
- [Rule 1]
- [Rule 2]
- [Rule 3]
- All randomness seeded. Same seed = identical results.
- Max 500 lines per file.
- No print statements inside engines. Structured logging only.

## Current Status
See STATUS.md.

## Do Not Touch
See SACRED_FILES.md.
