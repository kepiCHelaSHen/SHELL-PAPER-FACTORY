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

    $LineCount = (Get-Content $PaperPath | Measure-Object -Line).Lines
    Log "Paper: $($ProjectDir.Name) ($LineCount lines)"

    # Step 3: Run full-paper Steelman review
    Log ""
    Log "--- Running Steelman review ---"

    $PaperText = Get-Content $PaperPath -Raw -Encoding UTF8
    $SpecPath = Join-Path $ProjectDir.FullName "frozen_spec.md"
    $SpecText = if (Test-Path $SpecPath) { Get-Content $SpecPath -Raw -Encoding UTF8 } else { "(not found)" }

    $SteelmanPrompt = @"
You are a senior associate editor who has reviewed 200+ papers.
You have just read a complete academic paper. Write a referee report.

Target venue context is provided in the frozen specification. Evaluate against
that venue's standards and format expectations, not against an idealized
research article.

Organize your critique into:

## STRUCTURAL ISSUES (would cause rejection)
A structural issue is a MATHEMATICAL error in the paper's own derivations.
These are ONLY:
- A proof contains a logical error or incorrect derivation step
- A theorem's stated conditions are violated within the paper's own proof
- A definition is internally inconsistent (used one way in the definition,
  differently in the proof)

If the math is correct but you disagree with how the contribution is framed,
that is a FRAMING issue, not structural. Specifically, these are NEVER structural:
- The contribution is "trivial" or "just algebra" — that is a framing concern
- The paper overclaims novelty relative to prior work — that is framing
- A competing model can also derive a similar result — that is framing
- Parameter interpretations or definitional choices you would make differently
- Missing engagement with related literature
- False claims about what prior work did or did not do — that is a CITATION error
- Scope or framing concerns about how the contribution is presented

Numbered list. If none, write "None identified."

## FRAMING & POSITIONING ISSUES (would cause major revision)
Numbered list. If none, write "None identified."

## MINOR ISSUES (would appear in a revise-and-resubmit letter)
Numbered list. If none, write "None identified."

## VERDICT
Use this rubric:
- ACCEPT: No structural issues AND fewer than 3 framing issues AND all framing
  issues are addressable without rewriting proofs or restructuring the paper.
- MINOR_REVISION: No structural issues. Framing issues exist but do not require
  rewriting proofs or restructuring the paper.
- MAJOR_REVISION: Structural issues exist, OR framing issues require substantial
  rewriting of proofs or paper structure.
- REJECT: Fundamental mathematical errors, or the contribution does not exist.

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

    # Convert critique to a single string (it may come back as array from pipe)
    $CritiqueStr = $Critique | Out-String

    # Save critique to project dir
    $CritiquePath = Join-Path $ProjectDir.FullName "steelman_full_paper_critique.md"
    Set-Content -Path $CritiquePath -Value $CritiqueStr -Encoding UTF8
    Log "Saved critique to $($ProjectDir.Name)\steelman_full_paper_critique.md"

    # Consolidate findings into central logs
    python src/consolidate.py --critique $CritiquePath 2>&1 | ForEach-Object { Log $_ }
    $DeadEndsPath = Join-Path $ProjectDir.FullName "dead_ends.md"
    if (Test-Path $DeadEndsPath) {
        python src/consolidate.py --dead-ends $DeadEndsPath 2>&1 | ForEach-Object { Log $_ }
    }

    # Log the full critique
    Add-Content -Path $LogFile -Value "============ STEELMAN CRITIQUE - Run $run ============" -Encoding UTF8
    Add-Content -Path $LogFile -Value $CritiqueStr -Encoding UTF8
    Add-Content -Path $LogFile -Value "============ END CRITIQUE ============" -Encoding UTF8

    # Extract verdict from the VERDICT section specifically
    $Verdict = "UNKNOWN"
    # Find lines after ## VERDICT
    $InVerdict = $false
    foreach ($line in $CritiqueStr -split "`n") {
        if ($line -match "^##\s*VERDICT") {
            $InVerdict = $true
            continue
        }
        if ($InVerdict -and $line -match "^##") {
            break
        }
        if ($InVerdict -and $line.Trim().Length -gt 0) {
            if ($line -match "REJECT") { $Verdict = "REJECT" }
            elseif ($line -match "MAJOR_REVISION") { $Verdict = "MAJOR_REVISION" }
            elseif ($line -match "MINOR_REVISION") { $Verdict = "MINOR_REVISION" }
            elseif ($line -match "ACCEPT") { $Verdict = "ACCEPT" }
            if ($Verdict -ne "UNKNOWN") { break }
        }
    }

    Log ""
    Log "  STEELMAN VERDICT: $Verdict"
    Log ""

    # Step 4: Check if we're done
    if ($Verdict -eq "ACCEPT" -or $Verdict -eq "MINOR_REVISION") {
        Log "Steelman $Verdict. Quality loop complete."
        break
    }

    if ($run -ge $MaxRuns) {
        Log "Max runs ($MaxRuns) reached."
        break
    }

    # Step 5: Extract revision instructions and patch init file
    # Parse the critique line by line to extract sections safely
    $RevisionLines = @()
    $StructuralLines = @()
    $CurrentSection = ""

    foreach ($line in $CritiqueStr -split "`n") {
        if ($line -match "^##\s*STRUCTURAL ISSUES") { $CurrentSection = "structural"; continue }
        elseif ($line -match "^##\s*FRAMING") { $CurrentSection = "framing"; continue }
        elseif ($line -match "^##\s*MINOR") { $CurrentSection = "minor"; continue }
        elseif ($line -match "^##\s*VERDICT") { $CurrentSection = "verdict"; continue }
        elseif ($line -match "^##\s*REVISION INSTRUCTIONS") { $CurrentSection = "revision"; continue }
        elseif ($line -match "^##\s") { $CurrentSection = ""; continue }

        if ($CurrentSection -eq "structural" -and $line.Trim().Length -gt 0 -and $line.Trim() -ne "None identified.") {
            $StructuralLines += $line
        }
        if ($CurrentSection -eq "revision" -and $line.Trim().Length -gt 0 -and $line.Trim() -ne "No revisions needed.") {
            $RevisionLines += $line
        }
    }

    $Patch = "`n# === STEELMAN REVISION BRIEF (from run $run) ===`n"
    $Patch += "# The next run MUST address every item.`n"

    if ($StructuralLines.Count -gt 0) {
        $Patch += "# STRUCTURAL ISSUES:`n"
        $Patch += ($StructuralLines -join "`n") + "`n"
    }
    if ($RevisionLines.Count -gt 0) {
        $Patch += "# REVISION INSTRUCTIONS:`n"
        $Patch += ($RevisionLines -join "`n") + "`n"
    }

    # Patch init file - remove previous brief, then insert new one
    $InitContent = Get-Content $InitFile -Raw -Encoding UTF8
    # Remove any existing revision brief (keep only the latest)
    $InitContent = $InitContent -replace "(?s)# === STEELMAN REVISION BRIEF.*?(?=KNOWN_DRIFT_RISKS:)", ""
    $InsertPoint = $InitContent.IndexOf("KNOWN_DRIFT_RISKS:")
    if ($InsertPoint -ge 0) {
        $InitContent = $InitContent.Insert($InsertPoint, "$Patch`n")
    } else {
        $InitContent += $Patch
    }
    Set-Content -Path $InitFile -Value $InitContent -Encoding UTF8
    Log "Patched $InitFile with $($StructuralLines.Count) structural issues, $($RevisionLines.Count) revision instructions"
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
