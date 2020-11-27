# Scaffold for python scripts
This repository stores code for scaffolding like snippets for CLI option parser in Python.

## How To Run
This code depends on poetry to manage modules.
```bash
pip install poetry
poetry install
```
Before running, need to activate virtual-env
```bash
source ./.venv/bin/activate
```

## Key feature
The module spf13/cobra is super excellent module written in Golang providing option parser with well-readable structured statement. The uroboros is the module inspired by spf13/cobra for python option parser.
So this repository is arranging cobra like stanzas as scaffold if we write python CLI tool and need to write option parser statement. I believe it's helpful to write code more easily and more understandable.
