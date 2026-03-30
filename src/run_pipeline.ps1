$Slug = ""
$ProjectRoot = $PSScriptRoot
$MaxMilestones = 4

if (-not $Slug) {
    $Slug = Split-Path $ProjectRoot -Leaf
}

$StateVectorPath = "$ProjectRoot\papers\$Slug\state_vector.md"
$PaperPath = "$ProjectRoot\papers\$Slug\paper.md"

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
