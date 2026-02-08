---
name: Submodule pyarchivist
description: tools/pyarchivist is a submodule; only edit when user explicitly requests
applyTo: "tools/pyarchivist/**"
---

# Submodule PyArchivist Guidelines

- This is a git submodule for the pyarchivist archiving tool (external dependency)
- **Default behavior**: Avoid editing unless user explicitly requests it
- **If editing is needed but not requested**: Ask the user for permission first
- **When user approves edits**: Make changes here, test thoroughly, then contribute upstream
- For upstream contributions: work in the pyarchivist repo, merge changes, then update submodule pointer
- **Submodule instructions**: This submodule has its own `AGENTS.md` and `.github/instructions/` and `.github/skills/` files that take priority when working within `tools/pyarchivist/`
- **Working directory**: Always set your current working directory to the submodule root before running project or release commands. Run `cd tools/pyarchivist` first and then execute `uv`, `git`, or build commands from there.
- **Release reminder**: When publishing a new version, after updating the package version string run `uv sync` to refresh `uv.lock`; add and commit `uv.lock` (or include it in the release commit) before creating the release tag and pushing.

## Developer tooling & testing (pyarchivist submodule)

- Edits that affect archiving or index generation must include tests that verify index updates, idempotency, and correct metadata. Tests should run against a temporary directory and verify `index.md` changes and downloaded media placement.
- Coordinate with the parent repo to ensure that post-install behavior and `pyproject.toml` dependency declarations remain consistent.
