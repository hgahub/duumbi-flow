# Installation

The package uses the Agent Skills `SKILL.md` format. Install the entire skill directory: files under `assets/`, `references/`, and `agents/` may also be required.

## Skills CLI

The [Skills CLI](https://github.com/vercel-labs/skills) supports this repository layout:

```sh
npx skills@latest add hgahub/duumbi-flow
```

Select the skills and client in the installer. This command runs an external package and modifies an installation location; it is a manual installation instruction, not an automatic repository action.

## Manual installation

1. Clone or download the repository.
2. Choose a directory under `skills/`.
3. Copy the entire directory into your agent's documented skills location.
4. Check before overwriting an existing skill with the same name.
5. Verify that the client recognizes the skill and resolves its local references.

The repository itself does not change agent settings. The project or user determines the installation directory.

## Local development checks

Python 3.10 or later:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
.venv/bin/python -m unittest discover -s tests -v
```

The validator checks package structure, skill metadata, and local links. See the [pilot](pilot.md) for behavioral validation.
