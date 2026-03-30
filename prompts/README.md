# PROMPT LIBRARY — INDEX
# All prompts for SHELL v3. Copy-paste ready.

## Experiment Pipeline (multi-model: Grok + GPT-4o + Claude)

| File | Purpose | Model | Run how |
|------|---------|-------|---------|
| `00_orchestrator.md` | The full autonomous experiment loop | Claude (orchestrator) | `claude --dangerously-skip-permissions prompts/00_orchestrator.md` |
| `01_builder.md` | Builder — generates implementations | Grok-3 (xAI) | Injected by orchestrator via API |
| `02_critic.md` | Critic — validates against frozen spec | GPT-4o (OpenAI) | Injected by orchestrator via API |
| `03_reviewer.md` | Reviewer — audits quality | Claude | Orchestrator switches into this mode |

## Paper Pipeline (multi-model: Grok + GPT-4o + Claude)

| File | Purpose | Model | Run how |
|------|---------|-------|---------|
| `04_paper_orchestrator.md` | Milestone-gated paper pipeline | Claude (orchestrator) | `claude --dangerously-skip-permissions prompts/04_paper_orchestrator.md` |
| `05_author.md` | Author — writes paper sections | Grok-3 (xAI) | Injected by orchestrator via API |
| `06_peer_reviewer.md` | Peer Reviewer — science gate | GPT-4o (OpenAI) | Injected by orchestrator via API |
| `07_editor.md` | Editor — editorial quality | Claude | Orchestrator switches into this mode |
| `run_milestone.md` | Single milestone runner | Claude | Called by `run_pipeline.ps1` |

## Init Files (project scaffolding)

| File | Purpose | Run how |
|------|---------|---------|
| `00_init.md` | Generic project setup wizard | `claude --dangerously-skip-permissions prompts/00_init.md` |

Pre-filled paper init files live in `papers/`:

| File | Purpose | Run how |
|------|---------|---------|
| `papers/init_common_knowledge.md` | Pre-filled: Common Knowledge paper | `claude --dangerously-skip-permissions papers/init_common_knowledge.md` |
| `papers/init_fermi.md` | Pre-filled: Fermi Paradox paper | `claude --dangerously-skip-permissions papers/init_fermi.md` |

## Templates (copy and fill)

| File | Purpose |
|------|---------|
| `iteration_template.md` | Targeted change or feature |
| `debug_template.md` | Bug diagnosis and fix |
| `deep_dive_template.md` | Subsystem deep dive |

## Auto-Populated

| File | Purpose |
|------|---------|
| `turn_prompts_log.md` | Exact prompts sent each turn. Written by orchestrator. |

## Multi-Model Triangulation

SHELL uses three different LLMs to prevent any single model's training prior
from dominating. This is the core mechanism from Rice (2026) — different priors
catch each other's drift.

| Role | Model | Why this model |
|------|-------|---------------|
| Generation (Builder/Author) | Grok-3 (xAI), temp 0.7 | Creative generation from its own prior |
| Validation (Critic/Peer Reviewer) | GPT-4o (OpenAI), temp 0.2 | Low-temp validation with a different prior |
| Quality (Reviewer/Editor) | Claude, temp default | Third prior for quality and orchestration |
