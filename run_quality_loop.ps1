param(
    [Parameter(Mandatory=$true)]
    [string]$InitFile
)

# SHELL Quality Loop Launcher v2
# The quality loop now runs INSIDE the orchestrator (04_paper_orchestrator.md v5).
# This script: invokes Claude once, then consolidates findings from the output.
# No external loop. No init-file patching. No Ctrl+C between runs.

$ShellRoot = "C:\PROJECTS\SHELL"
Set-Location $ShellRoot

# Log everything to file
$LogFile = "$ShellRoot\logs\quality_loop_$(Get-Date -Format 'yyyyMMdd_HHmmss').log"
New-Item -ItemType Directory -Path "$ShellRoot\logs" -Force | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    Write-Host $line
    Add-Content -Path $LogFile -Value $line -Encoding UTF8
}

Log "SHELL Quality Loop Launcher v2"
Log "Log file: $LogFile"
Log "Init file: $InitFile"

# Validate init file exists
if (-not (Test-Path $InitFile)) {
    Log "ERROR: Init file not found: $InitFile"
    exit 1
}

# Extract base slug from init file
$SlugLine = Select-String -Path $InitFile -Pattern "^SLUG:" | Select-Object -First 1
$BaseSlug = ($SlugLine -replace ".*SLUG:\s*", "").Trim().ToUpper()
Log "Base slug: $BaseSlug"

# Single Claude invocation — the orchestrator handles the quality loop internally
Log ""
Log "============================================================"
Log "  INVOKING CLAUDE (internal quality loop)"
Log "  The orchestrator will run up to 3 iterations internally."
Log "  No Ctrl+C needed. Wait for completion."
Log "============================================================"
Log ""

$StartTime = Get-Date

# Read init file and pipe as prompt. Passing as positional arg causes Claude to
# ask "What would you like to do?" instead of executing. Piping as stdin with -p
# ensures Claude treats it as instructions to execute immediately.
$InitContent = Get-Content $InitFile -Raw -Encoding UTF8
$InitContent | cmd /c claude.cmd -p --dangerously-skip-permissions
$Duration = (Get-Date) - $StartTime

Log ""
Log "--- Claude exited after $([math]::Round($Duration.TotalMinutes, 1)) minutes ---"

# Find the project directory
$ProjectDir = Get-ChildItem -Path "$ShellRoot\papers" -Directory -Filter "$BaseSlug*" |
    Sort-Object Name | Select-Object -Last 1

if (-not $ProjectDir) {
    Log "ERROR: No project directory found for $BaseSlug"
    exit 1
}

Log "Project directory: $($ProjectDir.Name)"

# Check for best_paper.md (produced by the internal quality loop)
$BestPaperPath = Join-Path $ProjectDir.FullName "best_paper.md"
if (Test-Path $BestPaperPath) {
    $LineCount = (Get-Content $BestPaperPath | Measure-Object -Line).Lines
    Log "best_paper.md found ($LineCount lines)"
} else {
    # Fallback: check for paper.md in run directories
    $LatestRun = Get-ChildItem -Path $ProjectDir.FullName -Directory -Filter "run*" |
        Sort-Object Name | Select-Object -Last 1
    if ($LatestRun) {
        $PaperPath = Join-Path $LatestRun.FullName "paper.md"
        if (Test-Path $PaperPath) {
            Log "WARNING: No best_paper.md but found $($LatestRun.Name)/paper.md"
        } else {
            Log "WARNING: No paper.md found in latest run directory"
        }
    } else {
        # Legacy structure: paper.md in project root
        $PaperPath = Join-Path $ProjectDir.FullName "paper.md"
        if (Test-Path $PaperPath) {
            Log "Found paper.md in project root (legacy structure)"
        } else {
            Log "ERROR: No paper output found. Pipeline may have halted."
            Log "Check state_vector.md for halt reason."
        }
    }
}

# Post-run consolidation (safety net — orchestrator should have done this already)
$RunDirs = Get-ChildItem -Path $ProjectDir.FullName -Directory -Filter "run*" | Sort-Object Name
foreach ($RunDir in $RunDirs) {
    $CritiquePath = Join-Path $RunDir.FullName "steelman_critique.md"
    if (Test-Path $CritiquePath) {
        Log "Consolidating findings from $($RunDir.Name)/steelman_critique.md"
        python src/consolidate.py --critique $CritiquePath 2>&1 | ForEach-Object { Log $_ }
    }
}

# Consolidate dead ends if present
$DeadEndsPath = Join-Path $ProjectDir.FullName "dead_ends.md"
if (Test-Path $DeadEndsPath) {
    Log "Consolidating dead ends from project"
    python src/consolidate.py --dead-ends $DeadEndsPath 2>&1 | ForEach-Object { Log $_ }
}

# Report state vector
$StateVectorPath = Join-Path $ProjectDir.FullName "state_vector.md"
if (Test-Path $StateVectorPath) {
    Log ""
    Log "--- STATE VECTOR ---"
    Get-Content $StateVectorPath | ForEach-Object { Log "  $_" }
}

# Report run manifest if present
$ManifestPath = Join-Path $ProjectDir.FullName "outputs\run_manifest.md"
if (Test-Path $ManifestPath) {
    Log ""
    Log "--- RUN MANIFEST ---"
    Get-Content $ManifestPath | Select-Object -First 20 | ForEach-Object { Log "  $_" }
}

Log ""
Log "============================================================"
Log "  QUALITY LOOP COMPLETE"
Log "  Project: $($ProjectDir.Name)"
Log "  Duration: $([math]::Round($Duration.TotalMinutes, 1)) minutes"
Log "  Log: $LogFile"
Log "============================================================"
