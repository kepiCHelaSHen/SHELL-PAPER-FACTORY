Write-Host "Step 1: Before Claude"

cmd /c claude.cmd -p "Say OK" --output-format text

Write-Host "Step 2: Claude exited, script still alive"
Write-Host "Step 3: Loop works"
