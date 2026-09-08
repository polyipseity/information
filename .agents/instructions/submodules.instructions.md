---
name: Submodules
description: Guardrails for all git submodules in the repository
applyTo: "private/**, scripts/pyarchivist/**, scripts/pytextgen/**, self/arts/**, self/capture the flag/**, self/ledger/**, self/passwords/**, self/polyipseity/**"
---

# Submodule Guidelines

All submodules have their own `AGENTS.md` and `.agents/` that take priority when working inside them. `self/stash/` is __not__ a submodule — it is part of the parent repository and is not covered by this instruction.

## private/

- `private/` contains sensitive/restricted content managed in a separate upstream repository.
- __Do not__ copy or move files from `private/` into public trees (`general/`, `special/`, `archives/`) manually.
- If publishing: prepare a migration checklist covering PII, licenses, sensitive datasets, and redactions.
- Validate academic content before migrating:

  ```sh
  uv run .agents/skills/academic-notes/check.py --content private/special/academia/<INSTITUTION>
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

## scripts/pyarchivist/

- __Working directory__: Always `cd scripts/pyarchivist` before running project or release commands.
- __Release workflow__: After updating version string, run `uv sync` to refresh `uv.lock`; commit `uv.lock` before creating the release tag and pushing.
- __Tests__: Changes affecting archiving/index generation must include tests that verify index updates, idempotency, and correct metadata (run against a temp directory).

## scripts/pytextgen/

- __Fence sensitivity__: pytextgen fences and flashcard markup (cloze `{@{ }@}`, two-sided `::@::`, one-sided `:@:`) must not be altered without explicit intent and tests.
- __API changes__: Preserve backward compatibility or document breaking changes with migration notes.
- __Submodule pointer update__: Use commit message `chore(submodules): update pytextgen to <ref>` and run `bun run check && bun run test` in the parent repo.

## self/* (arts, capture the flag, ledger, passwords, polyipseity)

- Prefer `git submodule update --remote` for syncing upstream changes.
