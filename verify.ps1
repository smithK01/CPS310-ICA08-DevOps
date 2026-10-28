# CPS 310 verification script scaffold

Write-Host "Running project verification..."

python -m pytest -v

Write-Host ""
Write-Host "Checking required files..."


if (Test-Path "requirements.txt") {
    Write-Host "requirements.txt found."
}
else {
    Write-Host "requirements.txt is missing."
}

if (Test-Path "config.json") {
    Write-Host "config.json found."
}
else {
    Write-Host "config.json is missing."
}
Write-Host ""
Write-Host "Checking Git status..."

git status --short
