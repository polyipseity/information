---
name: Submodules
description: Guardrails for all git submodules in the repository
applyTo: "private/**, self/arts/**, self/capture the flag/**, self/ledger/**, self/passwords/**, self/polyipseity/**"
---

# Submodule Guidelines

All submodules have their own `AGENTS.md` and `.agents/` that take priority when working inside them. `self/stash/` is __not__ a submodule — it is part of the parent repository and is not covered by this instruction.

## private/

- `private/` contains sensitive/restricted content managed in a separate upstream repository.
- Routing exception: `academic-ingest` sends non-in-class submission artifacts and question pages into `private/` at their mirrored paths; writing that content during an ingestion is expected and needs no separate approval.
- __Do not__ copy or move files from `private/` into public trees (`general/`, `special/`, `archives/`) manually.
- If publishing: prepare a migration checklist covering PII, licenses, sensitive datasets, and redactions.
- Validate academic content before migrating:

  ```sh
  uv run python .agents/skills/academic-lint/main.py private/special/academia/<INSTITUTION>
  ```

1. Use `publish.py` to mirror curated content into the public repository; do not copy files manually.

### Migration checklist (example)

- PII present: YES/NO — if YES, list redactions.
- License/third-party content: YES/NO — include permissions.
- Sensitive datasets: YES/NO — propose sanitized derivative.
- Validation report: path/to/file
- Proposed patch/diff: path/to/patch

### If you lack permission

Open a maintainer request with the justification, validator output, and checklist. Do not edit `private/` until approved.

### Why this matters

These rules prevent accidental exposure of PII or licensed content and preserve a clean history by using the `publish` workflow for public releases.

## self/* (arts, capture the flag, ledger, passwords, polyipseity)

- Prefer `git submodule update --remote` for syncing upstream changes.
