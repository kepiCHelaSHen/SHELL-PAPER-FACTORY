#Requires -Version 5.1
<#
.SYNOPSIS
    All-in-one launcher for a 4-pane Claude setup across SHELL projects.

.DESCRIPTION
    First run: injects 4 custom color schemes (Capit-Blue, Capit-Red,
    Capit-Yellow, Capit-White) into Windows Terminal's settings.json,
    backing up the original first. Then launches Windows Terminal with
    a 2x2 grid -- each pane cd'd to a project directory running:
        claude --dangerously-skip-permissions

    Pane layout:
        SHELL     (Blue)   |  PROSPECT  (Red)
        DEMO      (Yellow) |  ASSAY     (White)

    Idempotent: safe to run repeatedly. Schemes only merged once.

.PARAMETER LaunchOnly
    Skip the schemes merge step; just open the panes.

.EXAMPLE
    .\launch-shell.ps1

.NOTES
    To run at Windows startup:
      1. Win+R, type:  shell:startup
      2. Right-click in that folder -> New -> Shortcut
      3. Target:
         powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -File "C:\PROJECTS\SHELL\launch-shell.ps1"
      4. Name it whatever, hit Finish.
#>

[CmdletBinding()]
param(
    [switch]$LaunchOnly
)

$ErrorActionPreference = 'Stop'

# ============================================================
# Embedded scheme JSON. Kept as a single text block so we can
# textually splice it into settings.json -- preserves the
# user's existing comments and formatting.
# ============================================================
$SchemesBlock = @'
        {
            "name": "Capit-Blue",
            "background": "#0d1b2a",
            "foreground": "#e0f2ff",
            "cursorColor": "#7dd3fc",
            "selectionBackground": "#1e3a5f",
            "black": "#0d1b2a",
            "red": "#ff6b6b",
            "green": "#51cf66",
            "yellow": "#ffd93d",
            "blue": "#7dd3fc",
            "purple": "#c792ea",
            "cyan": "#89ddff",
            "white": "#e0f2ff",
            "brightBlack": "#415a77",
            "brightRed": "#ff8787",
            "brightGreen": "#69db7c",
            "brightYellow": "#ffe066",
            "brightBlue": "#a5d8ff",
            "brightPurple": "#d4a8ff",
            "brightCyan": "#a5e9ff",
            "brightWhite": "#ffffff"
        },
        {
            "name": "Capit-Red",
            "background": "#2a0d12",
            "foreground": "#ffe0e0",
            "cursorColor": "#ff8787",
            "selectionBackground": "#5a1a25",
            "black": "#2a0d12",
            "red": "#ff6b6b",
            "green": "#51cf66",
            "yellow": "#ffd93d",
            "blue": "#7dd3fc",
            "purple": "#c792ea",
            "cyan": "#89ddff",
            "white": "#ffe0e0",
            "brightBlack": "#774a4a",
            "brightRed": "#ff8787",
            "brightGreen": "#69db7c",
            "brightYellow": "#ffe066",
            "brightBlue": "#a5d8ff",
            "brightPurple": "#d4a8ff",
            "brightCyan": "#a5e9ff",
            "brightWhite": "#ffffff"
        },
        {
            "name": "Capit-Yellow",
            "background": "#2a240d",
            "foreground": "#fff8e0",
            "cursorColor": "#ffd93d",
            "selectionBackground": "#5a4a1a",
            "black": "#2a240d",
            "red": "#ff6b6b",
            "green": "#51cf66",
            "yellow": "#ffd93d",
            "blue": "#7dd3fc",
            "purple": "#c792ea",
            "cyan": "#89ddff",
            "white": "#fff8e0",
            "brightBlack": "#776e4a",
            "brightRed": "#ff8787",
            "brightGreen": "#69db7c",
            "brightYellow": "#ffe066",
            "brightBlue": "#a5d8ff",
            "brightPurple": "#d4a8ff",
            "brightCyan": "#a5e9ff",
            "brightWhite": "#ffffff"
        },
        {
            "name": "Capit-White",
            "background": "#1a1a1a",
            "foreground": "#f5f5f5",
            "cursorColor": "#ffffff",
            "selectionBackground": "#3a3a3a",
            "black": "#1a1a1a",
            "red": "#ff6b6b",
            "green": "#51cf66",
            "yellow": "#ffd93d",
            "blue": "#7dd3fc",
            "purple": "#c792ea",
            "cyan": "#89ddff",
            "white": "#f5f5f5",
            "brightBlack": "#6a6a6a",
            "brightRed": "#ff8787",
            "brightGreen": "#69db7c",
            "brightYellow": "#ffe066",
            "brightBlue": "#a5d8ff",
            "brightPurple": "#d4a8ff",
            "brightCyan": "#a5e9ff",
            "brightWhite": "#ffffff"
        }
'@

$SchemeNames = @('Capit-Blue', 'Capit-Red', 'Capit-Yellow', 'Capit-White')

# ============================================================
# Step 1: Merge schemes into settings.json (idempotent)
# ============================================================
function Merge-Schemes {
    $candidates = @(
        "$env:LOCALAPPDATA\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json",
        "$env:LOCALAPPDATA\Packages\Microsoft.WindowsTerminalPreview_8wekyb3d8bbwe\LocalState\settings.json",
        "$env:LOCALAPPDATA\Microsoft\Windows Terminal\settings.json"
    )
    $settingsPath = $candidates | Where-Object { Test-Path $_ } | Select-Object -First 1

    if (-not $settingsPath) {
        Write-Warning "Couldn't find Windows Terminal settings.json. Panes will use default colors."
        return
    }

    Write-Host "[*] settings.json: $settingsPath" -ForegroundColor DarkGray

    $content = Get-Content -Path $settingsPath -Raw

    # Already merged? (all 4 names present = skip)
    $allPresent = $true
    foreach ($name in $SchemeNames) {
        if ($content -notmatch [regex]::Escape("`"name`": `"$name`"")) {
            $allPresent = $false
            break
        }
    }
    if ($allPresent) {
        Write-Host "[OK] Capit schemes already present -- skipping merge." -ForegroundColor DarkGreen
        return
    }

    # Backup before touching
    $backup = "$settingsPath.backup-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
    Copy-Item -Path $settingsPath -Destination $backup -Force
    Write-Host "[*] Backup -> $backup" -ForegroundColor DarkGray

    # Find the schemes array opening:  "schemes": [
    $m = [regex]::Match($content, '"schemes"\s*:\s*\[')
    if (-not $m.Success) {
        Write-Warning "No 'schemes' array found in settings.json. Skipping merge."
        return
    }

    $insertPos = $m.Index + $m.Length

    # Detect empty array: skip whitespace, see if next char is ]
    $i = $insertPos
    while ($i -lt $content.Length -and [char]::IsWhiteSpace($content[$i])) { $i++ }
    $isEmpty = ($i -lt $content.Length -and $content[$i] -eq ']')

    $prefix = $content.Substring(0, $insertPos)
    $suffix = $content.Substring($insertPos)

    if ($isEmpty) {
        $newContent = $prefix + "`r`n" + $SchemesBlock + "`r`n    " + $suffix.TrimStart()
    } else {
        $newContent = $prefix + "`r`n" + $SchemesBlock + ",`r`n        " + $suffix.TrimStart()
    }

    # UTF-8 without BOM (cross-version safe)
    [System.IO.File]::WriteAllText($settingsPath, $newContent, (New-Object System.Text.UTF8Encoding $false))

    Write-Host "[OK] Merged 4 Capit schemes into settings.json." -ForegroundColor Green
}

if (-not $LaunchOnly) {
    try {
        Merge-Schemes
    } catch {
        Write-Warning "Scheme merge failed: $_"
        Write-Warning "Continuing to launch -- panes may use default colors."
    }
}

# ============================================================
# Step 2: Sanity checks
# ============================================================
if (-not (Get-Command wt.exe -ErrorAction SilentlyContinue)) {
    Write-Error "wt.exe not found on PATH. Install Windows Terminal from the Microsoft Store."
    exit 1
}

$Projects = @(
    "C:\PROJECTS\SHELL",
    "C:\PROJECTS\PROSPECT",
    "C:\PROJECTS\DEMO",
    "C:\PROJECTS\ASSAY"
)

foreach ($p in $Projects) {
    if (-not (Test-Path $p)) {
        Write-Warning "Project path not found: $p -- pane will open but cd will fail."
    }
}

# ============================================================
# Step 3: Launch the 4-pane window
#         Backtick-semicolons (`;) are wt pane separators,
#         NOT PowerShell statement terminators.
#
#         Layout:
#           SHELL     (Blue)   |  PROSPECT  (Red)
#           DEMO      (Yellow) |  ASSAY     (White)
# ============================================================
$Cmd = "claude --dangerously-skip-permissions"

wt.exe `
    new-tab    --title "SHELL"    --colorScheme "Capit-Blue"   -d "C:\PROJECTS\SHELL"    powershell -NoExit -Command $Cmd `; `
    split-pane -V --title "PROSPECT" --colorScheme "Capit-Red"    -d "C:\PROJECTS\PROSPECT" powershell -NoExit -Command $Cmd `; `
    move-focus left `; `
    split-pane -H --title "DEMO"     --colorScheme "Capit-Yellow" -d "C:\PROJECTS\DEMO"     powershell -NoExit -Command $Cmd `; `
    move-focus right `; `
    split-pane -H --title "ASSAY"    --colorScheme "Capit-White"  -d "C:\PROJECTS\ASSAY"    powershell -NoExit -Command $Cmd
