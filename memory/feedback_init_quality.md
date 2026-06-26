---
name: Init file mistakes cost real money
description: Every init file error costs $25-75 in wasted runs. Triple-check inits before running. Sanity check all ASSAY values against model domain constraints.
type: feedback
originSessionId: 9cd9e77b-612c-46c7-bcba-7290994a5092
---
Init file mistakes are expensive — each wasted run costs $25-75 in CLI/API tokens.

**What happened:** v2 init files cited ASSAY data but didn't sanity-check the values against model constraints. Result: p* > 1 for pertussis (impossible), ASSAY data used as decoration instead of calibration, and Grok caught an "apparently fabricated ASSAY Report."

**Why:** Carelessness. The inits were written by an agent without verifying that ASSAY values were compatible with the model's domain (e.g., vaccination rate must be in [0,1]).

**How to apply:**
- Before writing any init, read the ASSAY integration block and verify every value against the model's domain constraints
- Add explicit sanity checks to drift risks: "If any computed value falls outside the model's valid range, flag it and explain why — do not silently use it"
- Tell the Author to CALIBRATE against data, not just CITE it. "Use ASSAY values to test model predictions" not "mention ASSAY values in the application section"
- Every init should be reviewed before running — the cost of a bad init is a wasted run
