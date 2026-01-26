---
name: Submodule private
description: private/ is a submodule; only edit when user explicitly requests
applyTo: "private/**"
---

# Submodule Private Guidelines

- This is a git submodule pointing to a separate private repository
- **Default behavior**: Avoid editing unless user explicitly requests it
- **If editing is needed but not requested**: Ask the user for permission first
- **When user approves edits**: Make changes here, then sync with upstream private repo
- Keep sensitive data out of public commits; this path is for curated mirroring via `publish.py`
- **Privacy protection**: Do NOT expose information inside the `private/` directory by moving, copying, or taking similar actions that would transfer its content to public directories (e.g., `general/`, `special/`, `archives/`) unless the user explicitly requests such action
- **Submodule instructions**: This submodule may have its own `AGENTS.md` and `.github/instructions/` and `.github/skills/` files that take priority when working within `private/`
