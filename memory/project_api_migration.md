---
name: API migration timing
description: User is using CLI for dev iteration to save cost. Will switch to API for fully autonomous quality loop once system is solid. Claude should recommend when ready.
type: project
originSessionId: 9cd9e77b-612c-46c7-bcba-7290994a5092
---
Currently using Claude CLI for all paper generation and quality loop runs. The CLI requires manual Ctrl+C twice per run (can't auto-exit), so the quality loop isn't fully autonomous yet.

**Why:** API tokens are expensive. CLI usage during dev/iteration phase saves cost while the system (init files, consolidated findings, drift risks) is still being refined.

**When to switch:** Once the consolidated findings system is proven (papers converging on Run 1 with pre-loaded findings), recommend switching to API keys for fully autonomous runs. The Ctrl+C problem disappears with API because there's no interactive CLI session.

**How to apply:** Track how many runs papers need to reach Steelman ACCEPT. When a new paper gets ACCEPT on Run 1 (or MAJOR_REVISION with only minor/framing issues, no structural), that's the signal to recommend an API test run. Flag it proactively — don't wait for the user to ask.
