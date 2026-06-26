---
name: Always test ONE paper before launching a batch
description: Launching 8 papers at once without testing one first has cost the user $100+ twice. Always run one paper, verify it completes, then batch.
type: feedback
originSessionId: 9cd9e77b-612c-46c7-bcba-7290994a5092
---
NEVER launch a full batch without testing one paper first. This has burned the user twice:
- v2 inits: 8 papers with bad ASSAY integration, Grok caught decorative citation = $75 wasted
- v3 inits: 8 papers with bloated inits (10-26KB), 7 of 8 timed out = $100+ wasted

**Why:** Each paper costs $12-25. A batch of 8 costs $100-200. Testing one first costs $12-25 and catches systemic issues before they multiply.

**How to apply:** Before ANY batch run:
1. Run ONE paper (the simplest one)
2. Verify it completes within the time window
3. Verify the output quality (best_paper.md exists, ASSAY data is calibrated not decorative)
4. THEN launch the rest

If you're tempted to "save time" by launching all at once — remember this cost $175+ in wasted runs.
