# PROMPT LIBRARY — INDEX
# All prompts for SHELL v5. Copy-paste ready.

## Paper Pipeline (Claude-only — all roles via CLI)

| File | Purpose | Role | Run how |
|------|---------|------|---------|
| `04_paper_orchestrator.md` | Milestone-gated paper pipeline | Orchestrator | `claude --dangerously-skip-permissions prompts/04_paper_orchestrator.md` |
| `05_author.md` | Author — writes paper sections | Author persona | Orchestrator reads and adopts persona |
| `06_peer_reviewer.md` | Peer Reviewer — science gate | Peer Reviewer persona | Orchestrator reads and adopts persona |
| `07_editor.md` | Editor — editorial quality | Editor persona | Orchestrator reads and adopts persona |
| `run_milestone.md` | Single milestone runner | Orchestrator | Called by `run_pipeline.ps1` |

## Experiment Pipeline (multi-model: Grok + GPT-4o + Claude)

| File | Purpose | Model | Run how |
|------|---------|-------|---------|
| `00_orchestrator.md` | The full autonomous experiment loop | Claude (orchestrator) | `claude --dangerously-skip-permissions prompts/00_orchestrator.md` |
| `01_builder.md` | Builder — generates implementations | Grok-3 (xAI) | Injected by orchestrator via API |
| `02_critic.md` | Critic — validates against frozen spec | GPT-4o (OpenAI) | Injected by orchestrator via API |
| `03_reviewer.md` | Reviewer — audits quality | Claude | Orchestrator switches into this mode |

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

## Model Strategy

**Paper pipeline:** Claude-only. All three roles (Author, Peer Reviewer, Editor)
are Claude with distinct personas and adversarial checklists. Writing quality
and proof rigor are the priority. No external API keys needed (except one
GPT-4o call for orchestrator accountability audit).

**Experiment pipeline:** Multi-model triangulation (Grok-3 / GPT-4o / Claude).
Three different training priors catch each other's specification drift.
This is the core mechanism from Rice (2026) — see https://zenodo.org/records/19217024
