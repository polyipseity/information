---
name: Submodule self
description: self/* submodules prefer upstream edits; only edit when user explicitly requests
applyTo: "self/**"
---
- These paths are git submodules managed in separate upstream repositories
- **Default behavior**: Avoid editing unless user explicitly requests it
- **If editing is needed but not requested**: Ask the user for permission first
- **When user approves edits**: Make changes here, then consider contributing upstream
- Prefer `git submodule update --remote` workflows for syncing upstream changes
