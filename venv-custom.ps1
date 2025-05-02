$env:PIP_REQUIRE_VIRTUALENV = "true"

function pip-update-reqs {
    pip freeze | Out-File -Encoding ASCII "$PWD\requirements.txt"
}

function pip {
    param([Parameter(ValueFromRemainingArguments = $true)][string[]]$args)
    & python -m pip install @args
    pip-update-reqs
}

function pipu {
    param([Parameter(ValueFromRemainingArguments = $true)][string[]]$args)
    & python -m pip uninstall -y @args
    pip-update-reqs
}
