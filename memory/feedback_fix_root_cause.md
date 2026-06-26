---
name: Fix root causes, never hack around them
description: User wants real fixes, not workarounds or logic hacks. If the Steelman is broken, fix the Steelman. Don't bypass it with counting logic or manual steps.
type: feedback
originSessionId: 9cd9e77b-612c-46c7-bcba-7290994a5092
---
Fix the actual problem. Don't propose workarounds that bypass broken components.

**Why:** The user got burned multiple times by suggestions to hack around the Steelman (count structural issues instead of trusting verdict, manually accept the paper, bypass the quality loop). Each one defeats the purpose of having the Steelman in the first place.

**How to apply:** When a component is misbehaving, diagnose WHY it's misbehaving and fix THAT. If the Steelman misclassifies framing as structural, fix the Steelman prompt until it classifies correctly. Don't add code to override its verdict. The system must work correctly, not be patched around.
