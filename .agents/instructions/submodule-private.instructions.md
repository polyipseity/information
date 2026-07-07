---
name: Submodule private
description: private/ is a git submodule; edit only with explicit owner approval
applyTo: "private/**"
---

# Submodule Private Guidelines

- `private/` contains sensitive/restricted content.
- __Do not__ copy or move files from `private/` into public trees (`general/`, `special/`, `archives/`) manually.
- If publishing: prepare a migration checklist covering PII, licenses, sensitive datasets, and redactions.
- Validate academic content before migrating:

  ```sh
  uv run .agents/skills/academic-notes/check.py --content private/special/academia/<INSTITUTION>
  ```

1. Use `publish.py` to mirror curated content into the public repository; do not copy files manually.

## Migration checklist (example)

- PII present: YES/NO — if YES, list redactions.
- License/third-party content: YES/NO — include permissions.
- Sensitive datasets: YES/NO — propose sanitized derivative.
- Validation report: path/to/file
- Proposed patch/diff: path/to/patch

## If you lack permission

Open a maintainer request with the justification, validator output, and checklist. Do not edit `private/` until approved.

## Why this matters

These rules prevent accidental exposure of PII or licensed content and preserve a clean history by using the `publish` workflow for public releases.
