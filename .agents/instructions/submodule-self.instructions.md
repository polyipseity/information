---
name: Submodule self
description: self/* git submodules prefer upstream edits; only edit when user explicitly requests
applyTo: "self/arts/**, self/capture the flag/**, self/ledger/**, self/passwords/**, self/polyipseity/**"
---

# Submodule Self Guidelines

Unique rules for this subtree:

- `self/stash/` is __not__ a submodule; it is part of the parent repository and is not covered by this instruction.
- Prefer `git submodule update --remote` for syncing upstream changes.
- Each submodule under `self/` may have its own `AGENTS.md` and `.agents/` that take priority.
