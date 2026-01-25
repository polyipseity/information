---
name: Submodule private
description: private/ is a submodule; only edit when user explicitly requests
applyTo: "private/**"
---
- This is a git submodule pointing to a separate private repository
- **Default behavior**: Avoid editing unless user explicitly requests it
- **If editing is needed but not requested**: Ask the user for permission first
- **When user approves edits**: Make changes here, then sync with upstream private repo
- Keep sensitive data out of public commits; this path is for curated mirroring via `publish.py`
