# INIT PROMPT — PROJECT SETUP WIZARD v2
# Runs ONCE at the start of a new project.
# Copies SHELL structure, fills all templates, creates ALL required files,
# initializes git, locks the spec, hands off to pipeline.
#
# Generic template. For a pre-filled project, see papers/init_[project].md
#
# claude --dangerously-skip-permissions papers/init_[project].md

---

## YOUR JOB

Set up a new research project based on SHELL. Do not skip any step.
Every file listed below must be created. Missing files break the pipeline.

---

## INPUTS

PROJECT_NAME: [full name]
SLUG: [short filesystem-safe name]
AUTHOR: James P Rice Jr.
TARGET_VENUE: [journal or preprint server]
PIPELINE: [PAPER / EXPERIMENT]
PROBLEM: [the research question — one paragraph]
FROZEN_SPEC_PARAMETERS: [list of parameters, values, sources]
MILESTONES:
  M1: [first deliverable]
  M2: [second deliverable]
  M3: [third deliverable]
  M4: [integration / full paper]
ORACLE: [how outputs will be validated]
KNOWN_DRIFT_RISKS: [what LLM prior is likely to get wrong]

---

## SETUP SEQUENCE — DO NOT SKIP ANY STEP

### Step 1 — Create ALL directories

Create D:\EXPERIMENTS\[SLUG]\ with every subdirectory:
  spec/
  state/
  outputs/
  results/raw/
  results/validated/
  results/final/
  devlog/
  src/
  papers/
  papers/[SLUG]/
  papers/[SLUG]/figures/
  prompts/

### Step 2 — Write README.md

Contents:
  # [PROJECT_NAME]
  **Author:** James P Rice Jr.
  **Status:** In progress
  **Target venue:** [TARGET_VENUE]

  ## What This Is
  [One paragraph from PROBLEM]

  ## Key Files
  - spec/frozen_spec.md — locked parameters, never modify
  - state/state_vector.md — current loop state
  - state/innovation_log.md — full audit trail
  - papers/[SLUG]/paper.md — final output (when complete)

  ## How to Run
  claude --dangerously-skip-permissions prompts/04_paper_orchestrator.md

### Step 3 — Write CLAUDE.md

  # [PROJECT_NAME] — NORTH STAR
  # Read this at the start of every session. Two minutes max.

  ## What We Are Building
  [One sentence from PROBLEM]

  ## The Core Claim
  [The central result — one sentence. From frozen spec.]

  ## Key Files
  - CHAIN_PROMPT.md — master doc, wins all conflicts
  - spec/frozen_spec.md — frozen parameters, never modify
  - state/state_vector.md — save game
  - state/innovation_log.md — audit trail
  - state/dead_ends.md — do not repeat these
  - prompts/04_paper_orchestrator.md — the pipeline

  ## Frozen Parameters (quick reference)
  [Table from FROZEN_SPEC_PARAMETERS]

  ## Critical Enforcements
  [List from KNOWN_DRIFT_RISKS — top 3-4]

  ## Do Not Touch
  See SACRED_FILES.md.

### Step 4 — Write CHAIN_PROMPT.md

  # CHAIN PROMPT — [PROJECT_NAME]
  # THIS FILE WINS ALL CONFLICTS
  # Updated: [today's date]

  ## Experiment Identity
  Name: [PROJECT_NAME]
  Slug: [SLUG]
  Author: James P Rice Jr.
  Location: D:\EXPERIMENTS\[SLUG]\
  Target: [TARGET_VENUE]
  Status: INIT

  ## Problem
  [PROBLEM]

  ## Confirmed Design Decisions
  Spec locked: spec/frozen_spec.md
  Pipeline: [PIPELINE] — multi-model triangulation, milestone-by-milestone gating
  Author: Grok-3 (xAI, temp 0.7) — generation
  Peer Reviewer: GPT-4o (OpenAI, temp 0.2) — validation
  Editor: Claude — editorial quality and orchestration
  Review format: Markdown

  ## Milestones
  M1: [M1 description]
  M2: [M2 description]
  M3: [M3 description]
  M4: [M4 description]

  ## Frozen Parameters
  [Table from FROZEN_SPEC_PARAMETERS]

  ## Change Log
  [today's date] | Project initialized from SHELL

### Step 5 — Write SACRED_FILES.md

  # SACRED FILES
  # Never modify after lock date.

  Lock date: [today]
  Locked by: James P Rice Jr.

  | File | Reason | Locked |
  |------|--------|--------|
  | spec/frozen_spec.md | The oracle. Modifying invalidates the experiment. | [today] |

### Step 6 — Write BEST_PRACTICES.md

  # BEST PRACTICES — [PROJECT_NAME]
  # Read before starting any session.
  # Author: James P Rice Jr.

  ## Non-Negotiables
  - Formalism first. Definitions Block before Abstract, always.
  - Lean-ready proofs. Every hypothesis explicit. Every step justified.
  - Literature gap formula in Introduction for every major prior work.
  - Boundary Conditions section must try to break the theory.
  - Milestone-by-milestone. No section unlocks until previous is Peer Reviewer ACCEPT.

  ## Context Resets
  Read in order: CLAUDE.md → state/state_vector.md → state/dead_ends.md
  Do not rely on chat history. Everything lives in files.

### Step 7 — Write STATUS.md

  # [PROJECT_NAME] — Current Status
  Phase: INIT
  Turn: 0
  Mode: VALIDATION
  What Is Done: Project scaffolded. Spec locked.
  What Is Next: Begin M1 — Foundations (Definitions Block + Introduction)
  Open Flags: NONE
  Updated: [today]

### Step 8 — Write .gitignore

  api.env
  __pycache__/
  *.pyc
  .DS_Store
  *.egg-info/

### Step 9 — Write spec/frozen_spec.md

Fill every PARAMETER block from FROZEN_SPEC_PARAMETERS.
Fill ORACLE section.
Fill MILESTONE MAP table.
Fill KNOWN PRIOR DRIFT RISK blocks.
Write lock date: [today]
Write: Locked by: James P Rice Jr.

### Step 10 — Initialize state files

Write state/state_vector.md:
  TURN: 0
  MILESTONE: M1
  MODE: INIT
  FLAGS: NONE
  CONSECUTIVE_BLOCKS: 0
  LAST_COMMITTED_METRICS: N/A
  LAST_COMMITTED_TURN: N/A
  EXPERIMENT: [PROJECT_NAME]
  TIMESTAMP: [today]

Write state/innovation_log.md:
  # INNOVATION LOG — [PROJECT_NAME]
  # Append-only. Never edit previous entries. Add to bottom only.
  # Managed by Orchestrator. One entry per milestone attempt.
  # Format: YAML blocks inside markdown for machine + human readability.

  === EXPERIMENT: [PROJECT_NAME] ===
  === LOOP INITIALIZED: [today] ===
  === FROZEN SPEC LOCKED: [spec/frozen_spec.md — confirmed] ===
  === MILESTONES: M1 | M2 | M3 | M4 ===

  [Loop entries begin below on Turn 1]

Write state/dead_ends.md:
  # DEAD ENDS — [PROJECT_NAME]
  # Append-only. Author reads before every milestone.

  === EXPERIMENT: [PROJECT_NAME] ===
  === INITIALIZED: [today] ===

  [No dead ends yet.]

### Step 11 — Write outputs/options.md and outputs/state_vector_backup.md

Write outputs/options.md:
  # OPTIONS LOG — [PROJECT_NAME]
  # Candidate approaches not yet committed.
  [No options yet.]

Write outputs/state_vector_backup.md:
  # STATE VECTOR BACKUP — [PROJECT_NAME]
  [No backups yet. Written before any high-risk operation.]

### Step 12 — Write devlog/DEV_LOG.md

  # DEVELOPMENT LOG — [PROJECT_NAME]
  # Human-written. Append-only. One entry per session.

  ## [today] — Session 1
  **Status at start:** Project initialized.
  **What was done:**
  - Scaffolded from SHELL
  - Frozen spec locked
  - All state files initialized
  **Decisions:**
  Pipeline: PAPER. Milestone-by-milestone gating.
  Review format: Markdown for VS Code / Obsidian review.
  Zenodo upload: manual, after James P Rice Jr. approves.
  **Blockers:** None.
  **Status at end:** Ready to run M1.

### Step 13 — Copy and update all prompts

Copy from SHELL/prompts/ into [SLUG]/prompts/:
  04_paper_orchestrator.md
  05_author.md
  06_peer_reviewer.md
  07_editor.md
  run_milestone.md

Do NOT copy 00_init.md or init_*.md into the project prompts.
Those are SHELL-level files only.

### Step 14 — Write prompts/turn_prompts_log.md

  # TURN PROMPTS LOG — [PROJECT_NAME]
  # Every exact prompt sent to Author, Peer Reviewer, Editor logged here.
  # Required for reproducibility. Append after every call.

  ## Format:
  ### Turn [N] | M[milestone] | [role] | [date]
  [exact prompt text]
  ---

  [No entries yet. First entry written at Turn 1 M1.]

### Step 15 — Write run_pipeline.ps1

Write run_pipeline.ps1 in the project root with this exact content
(no special characters, no emoji, plain ASCII only):

  $Slug = "[SLUG]"
  $ProjectRoot = "D:\EXPERIMENTS\[SLUG]"
  $StateVectorPath = "$ProjectRoot\papers\$Slug\state_vector.md"
  $PaperPath = "$ProjectRoot\papers\$Slug\paper.md"
  $MaxMilestones = 4

  Write-Host ""
  Write-Host "SHELL PAPER PIPELINE"
  Write-Host "Project: $Slug"
  Write-Host ""

  for ($i = 1; $i -le $MaxMilestones; $i++) {

      if (Test-Path $PaperPath) {
          Write-Host "PAPER COMPLETE - open papers\$Slug\paper.md"
          break
      }

      if (Test-Path $StateVectorPath) {
          $StateContent = Get-Content $StateVectorPath -Raw

          if ($StateContent -match "(?m)^STATUS: HALTED") {
              Write-Host "HALTED - check outputs\halt_report.md"
              break
          }

          if ($StateContent -match "(?m)^MILESTONE: (M\d)") {
              $CurrentMilestone = $Matches[1]
          } else {
              $CurrentMilestone = "M1"
          }
      } else {
          $CurrentMilestone = "M1"
      }

      Write-Host "--------------------------------------------"
      Write-Host "Running: $CurrentMilestone  $(Get-Date -Format 'HH:mm:ss')"
      Write-Host "Watch: $ProjectRoot\LIVE_STATUS.md"
      Write-Host "--------------------------------------------"

      "[$CurrentMilestone] Starting... $(Get-Date -Format 'HH:mm:ss')" | Set-Content "$ProjectRoot\LIVE_STATUS.md"

      $Prompt = "Load prompts/run_milestone.md. SLUG: $Slug. Read papers/$Slug/state_vector.md first. Run ONE milestone then exit cleanly. Write progress to LIVE_STATUS.md after every action."

      Set-Location $ProjectRoot

      & claude --dangerously-skip-permissions -p $Prompt 2>&1 | ForEach-Object {
          Write-Host $_
          $_ | Add-Content "$ProjectRoot\run_log.txt"
      }

      Write-Host ""
      Start-Sleep -Seconds 5

      if (Test-Path $PaperPath) {
          Write-Host ""
          Write-Host "PAPER COMPLETE"
          Write-Host "papers\$Slug\paper.md - ready for review"
          break
      }

      if (Test-Path $StateVectorPath) {
          $StateContent = Get-Content $StateVectorPath -Raw
          if ($StateContent -match "(?m)^STATUS: HALTED") {
              Write-Host "HALTED - check outputs\halt_report.md"
              break
          }
      }
  }

  Write-Host ""
  Write-Host "Pipeline run complete."

### Step 16 — Initialize git

Run:
  cd D:\EXPERIMENTS\[SLUG]
  git init
  git add -A
  git commit -m "Turn 0 | Init | [PROJECT_NAME]"

### Step 17 — Print confirmation

  ✅ PROJECT INITIALIZED: [PROJECT_NAME]
  📁 D:\EXPERIMENTS\[SLUG]\
  🔒 Spec locked: spec/frozen_spec.md
  📝 All files created. Git initialized.
  ▶  Handing off to paper pipeline — M1 begins now.

### Step 18 — Hand off

PAPER pipeline → load prompts/04_paper_orchestrator.md and begin M1.
EXPERIMENT pipeline → load prompts/00_orchestrator.md and begin Turn 1.
