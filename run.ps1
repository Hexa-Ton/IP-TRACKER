$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ProjectRoot
if (Get-Command py -ErrorAction SilentlyContinue) { & py -3 main.py @args }
elseif (Get-Command python -ErrorAction SilentlyContinue) { & python main.py @args }
else { throw "Python 3 is not installed." }
exit $LASTEXITCODE
