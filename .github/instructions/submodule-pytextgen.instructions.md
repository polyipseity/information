---
name: Submodule pytextgen
description: tools/pytextgen is a submodule; only edit when user explicitly requests
applyTo: "tools/pytextgen/**"
---

# Submodule PyTextGen Guidelines

- This is a git submodule for the pytextgen content generation library (external dependency)
- **Default behavior**: Avoid editing unless user explicitly requests it
- **If editing is needed but not requested**: Ask the user for permission first
- **When user approves edits**: Make changes here, test thoroughly, then contribute upstream
- For upstream contributions: work in the pytextgen repo, merge changes, then update submodule pointer
- **Submodule instructions**: This submodule has its own `AGENTS.md` and `.github/instructions/` and `.github/skills/` files that take priority when working within `tools/pytextgen/`
