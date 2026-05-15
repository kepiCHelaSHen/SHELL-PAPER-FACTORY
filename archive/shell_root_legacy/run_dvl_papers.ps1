# run_dvl_papers.ps1 — Run all 11 DVL papers sequentially
# Each paper auto-versions to C:\PROJECTS\SHELL\papers\[SLUG]_[DATE]_[SEQ]\
# via 00_init.md Step 0, then runs the 4-milestone pipeline autonomously.
#
# Usage:
#   cd C:\PROJECTS\SHELL
#   .\run_dvl_papers.ps1
#
# To run a single paper:
#   claude --dangerously-skip-permissions papers/init_triangulation.md

$Papers = @(
    "triangulation",
    "sunk_cost",
    "conspiracy_bayes",
    "dao_voting",
    "doomscrolling",
    "induced_demand",
    "replication_crisis",
    "supply_chain",
    "tech_lockin",
    "vaccine_game",
    "academic_publishing"
)

$ShellRoot = "C:\PROJECTS\SHELL"
$Total = $Papers.Count
$Completed = 0
$Failed = @()

Write-Host ""
Write-Host "============================================"
Write-Host "  DVL PAPERS BATCH RUN"
Write-Host "  Papers: $Total"
Write-Host "  Output: C:\PROJECTS\SHELL\papers\"
Write-Host "  Started: $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
Write-Host "============================================"
Write-Host ""

foreach ($paper in $Papers) {
    $Index = $Papers.IndexOf($paper) + 1
    $InitFile = "papers/init_$paper.md"

    Write-Host "--------------------------------------------"
    Write-Host "[$Index/$Total] Starting: $paper"
    Write-Host "  Init: $InitFile"
    Write-Host "  Time: $(Get-Date -Format 'HH:mm:ss')"
    Write-Host "--------------------------------------------"

    Set-Location $ShellRoot

    try {
        & claude --dangerously-skip-permissions $InitFile 2>&1 | ForEach-Object {
            Write-Host $_
        }
        $Completed++
        Write-Host ""
        Write-Host "[$Index/$Total] DONE: $paper"
        Write-Host ""
    }
    catch {
        $Failed += $paper
        Write-Host ""
        Write-Host "[$Index/$Total] FAILED: $paper - $_"
        Write-Host ""
    }

    # Brief pause between papers
    Start-Sleep -Seconds 10
}

Write-Host ""
Write-Host "============================================"
Write-Host "  BATCH RUN COMPLETE"
Write-Host "  Completed: $Completed / $Total"
if ($Failed.Count -gt 0) {
    Write-Host "  Failed: $($Failed -join ', ')"
}
Write-Host "  Finished: $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
Write-Host "============================================"
