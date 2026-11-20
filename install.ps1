$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ProjectRoot
if (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 --version
    if ($LASTEXITCODE -ne 0) { throw "Python 3 is unavailable." }
    & py -3 -m py_compile main.py
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    & python --version
    & python -m py_compile main.py
} else { throw "Python 3 is required. Install Python 3.10 or newer." }
if ($LASTEXITCODE -ne 0) { throw "Python syntax check failed." }
Write-Host "IP-TRACKER 1.0.0 installation check passed."
Write-Host "Start with: .\run.ps1"
