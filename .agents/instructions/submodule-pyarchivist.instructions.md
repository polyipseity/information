---
name: Submodule pyarchivist
description: scripts/pyarchivist is a submodule; only edit when user explicitly requests
applyTo: "scripts/pyarchivist/**"
---

# Submodule PyArchivist Guidelines

Unique rules for this submodule:

- __Working directory__: Always `cd scripts/pyarchivist` before running project or release commands.
- __Release workflow__: After updating version string, run `uv sync` to refresh `uv.lock`; commit `uv.lock` before creating the release tag and pushing.
- __Tests__: Changes affecting archiving/index generation must include tests that verify index updates, idempotency, and correct metadata (run against a temp directory).
- This submodule has its own `AGENTS.md` and `.agents/` that take priority when working inside `scripts/pyarchivist/`.
