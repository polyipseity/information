---
name: Submodule self
description: self/* submodules prefer upstream edits; only edit when user explicitly requests
applyTo: "self/**"
---

# Submodule Self Guidelines

- These paths are git submodules managed in separate upstream repositories
- **Default behavior**: Avoid editing unless user explicitly requests it
- **If editing is needed but not requested**: Ask the user for permission first
- **When user approves edits**: Make changes here, then consider contributing upstream
- Prefer `git submodule update --remote` workflows for syncing upstream changes

## Developer tooling & testing (self/ submodules)

- Apply the same repo-level developer and testing conventions inside submodules: use `pyproject.toml`, add unit and integration tests, run `pnpm run check` and `pnpm run test` locally, and document any submodule-specific deviations in the submodule's `AGENTS.md`.
- If a submodule requires different Python or tooling constraints (different Python version or unique CI steps), document them clearly in the submodule `AGENTS.md` and `.github/instructions/` so agents and CI can pick up the correct settings.
- **Submodule instructions**: Each submodule under `self/` may have its own `AGENTS.md` and `.github/instructions/` and `.github/skills/` files that take priority when working within that specific submodule
- **`self/stash/`**: A workspace for miscellaneous, small Python utility scripts (stashed tools). These files are user-managed and may be created or edited only when the user explicitly requests it; consider adding an index (`index.md`) to document scripts placed here.
