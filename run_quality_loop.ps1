param(
    [Parameter(Mandatory=$true)]
    [string]$InitFile,
    [int]$MaxRuns = 10
)

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

Log "Log file: $LogFile"

# Backup init file
$BackupFile = "$InitFile.bak"
if (-not (Test-Path $BackupFile)) {
    Copy-Item $InitFile $BackupFile
    Log "Backed up $InitFile"
}

# Extract base slug from init file
$SlugLine = Select-String -Path $InitFile -Pattern "^SLUG:" | Select-Object -First 1
$BaseSlug = ($SlugLine -replace ".*SLUG:\s*", "").Trim().ToUpper()
Log "Base slug: $BaseSlug"

for ($run = 1; $run -le $MaxRuns; $run++) {
    Log ""
    Log "============================================================"
    Log "  RUN $run / $MaxRuns"
    Log "============================================================"
    Log ""
    Log "--- Generating paper ---"
    # cmd /c isolates claude.cmd so its exit doesn't kill this script
    cmd /c claude.cmd --dangerously-skip-permissions $InitFile
    Log ""
    Log "--- Claude exited ---"

    # Step 2: Find the latest project directory
    $ProjectDir = Get-ChildItem -Path "$ShellRoot\papers" -Directory -Filter "$BaseSlug*" |
        Sort-Object Name | Select-Object -Last 1

    if (-not $ProjectDir) {
        Log "ERROR: No project directory found for $BaseSlug"
        break
    }

    $PaperPath = Join-Path $ProjectDir.FullName "paper.md"
    if (-not (Test-Path $PaperPath)) {
        Log "ERROR: No paper.md in $($ProjectDir.Name). Pipeline may have halted."
        break
    }

    Log "Paper: $($ProjectDir.Name) ($(Get-Content $PaperPath | Measure-Object -Line | Select-Object -ExpandProperty Lines) lines)"

    # Step 3: Run full-paper Steelman review
    Log ""
    Log "--- Running Steelman review ---"

    $PaperText = Get-Content $PaperPath -Raw -Encoding UTF8
    $SpecPath = Join-Path $ProjectDir.FullName "frozen_spec.md"
    $SpecText = if (Test-Path $SpecPath) { Get-Content $SpecPath -Raw -Encoding UTF8 } else { "(not found)" }

    $SteelmanPrompt = @"
You are a senior associate editor who has reviewed 200+ papers.
You have just read a complete academic paper. Write a referee report.

Organize your critique into:
## STRUCTURAL ISSUES (would cause rejection)
Numbered list. If none, write "None identified."
## FRAMING & POSITIONING ISSUES (would cause major revision)
Numbered list. If none, write "None identified."
## MINOR ISSUES (would appear in a revise-and-resubmit letter)
Numbered list. If none, write "None identified."
## VERDICT
One of: ACCEPT, MAJOR_REVISION, or REJECT
## REVISION INSTRUCTIONS
If not ACCEPT: numbered actionable instructions. If ACCEPT: "No revisions needed."

Here is the paper:
$PaperText

Here is the frozen specification:
$SpecText
"@

    # Write prompt to temp file to avoid command line length limits
    $TempFile = [System.IO.Path]::GetTempFileName()
    Set-Content -Path $TempFile -Value $SteelmanPrompt -Encoding UTF8

    $Critique = Get-Content $TempFile -Raw | cmd /c claude.cmd -p --output-format text --dangerously-skip-permissions 2>&1
    Remove-Item $TempFile -ErrorAction SilentlyContinue

    # Save critique
    $CritiquePath = Join-Path $ProjectDir.FullName "steelman_full_paper_critique.md"
    Set-Content -Path $CritiquePath -Value $Critique -Encoding UTF8
    Log "Saved critique to $($ProjectDir.Name)\steelman_full_paper_critique.md"
    # Log the full critique
    Add-Content -Path $LogFile -Value "============ STEELMAN CRITIQUE — Run $run ============" -Encoding UTF8
    Add-Content -Path $LogFile -Value $Critique -Encoding UTF8
    Add-Content -Path $LogFile -Value "============ END CRITIQUE ============" -Encoding UTF8

    # Extract verdict - check simple string contains
    $Verdict = "UNKNOWN"
    $CritiqueStr = $Critique | Out-String
    if ($CritiqueStr -match "REJECT") {
        $Verdict = "REJECT"
    } elseif ($CritiqueStr -match "MAJOR_REVISION") {
        $Verdict = "MAJOR_REVISION"
    } elseif ($CritiqueStr -match "ACCEPT") {
        $Verdict = "ACCEPT"
    }

    Log ""
    Log "  STEELMAN VERDICT: $Verdict"
    Log ""

    # Step 4: Check if we're done
    if ($Verdict -eq "ACCEPT") {
        Log "Steelman ACCEPTED. Quality loop complete."
        break
    }

    if ($run -ge $MaxRuns) {
        Log "Max runs ($MaxRuns) reached."
        break
    }

    # Step 5: Extract revision instructions and patch init file
    $RevisionMatch = [regex]::Match($Critique, "(?s)##\s*REVISION INSTRUCTIONS\s*\n(.*?)(?:\n##|\z)")
    $StructuralMatch = [regex]::Match($Critique, "(?s)##\s*STRUCTURAL ISSUES.*?\n(.*?)(?:\n##|\z)")

    $Patch = "`n# === STEELMAN REVISION BRIEF (from run $run) ===`n"
    $Patch += "# The next run MUST address every item.`n"

    if ($StructuralMatch.Success -and $StructuralMatch.Groups[1].Value.Trim() -ne "None identified.") {
        $Patch += "# STRUCTURAL ISSUES:`n"
        $Patch += $StructuralMatch.Groups[1].Value.Trim() + "`n"
    }
    if ($RevisionMatch.Success -and $RevisionMatch.Groups[1].Value.Trim() -ne "No revisions needed.") {
        $Patch += "# REVISION INSTRUCTIONS:`n"
        $Patch += $RevisionMatch.Groups[1].Value.Trim() + "`n"
    }

    $InitContent = Get-Content $InitFile -Raw -Encoding UTF8
    if ($InitContent -match "KNOWN_DRIFT_RISKS:") {
        $InitContent = $InitContent -replace "KNOWN_DRIFT_RISKS:", "$Patch`nKNOWN_DRIFT_RISKS:"
    } else {
        $InitContent += $Patch
    }
    Set-Content -Path $InitFile -Value $InitContent -Encoding UTF8
    Log "Patched $InitFile with revision instructions"
    Log "Waiting 10s before next run..."
    Start-Sleep -Seconds 10
}

# Restore original init file
if (Test-Path $BackupFile) {
    Copy-Item $BackupFile $InitFile -Force
    Log "Restored original $InitFile from backup"
}

Log ""
Log "============================================================"
Log "  QUALITY LOOP COMPLETE"
Log "  Runs: $run"
Log "  Log: $LogFile"
Log "============================================================"
