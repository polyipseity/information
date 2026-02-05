---
name: Submodule private
description: private/ is a git submodule; edit only with explicit owner approval
applyTo: "private/**"
---

# Overview

`private/` is a git submodule pointing to a separate private repository. It contains sensitive or restricted content and must not be modified without explicit owner permission.

## Rules

- Do not edit files in `private/` unless the repository owner or maintainer explicitly approves the change.
- Do not copy or move files from `private/` into public trees (`general/`, `special/`, `archives/`) manually.
- Follow submodule-local instructions (for example, `AGENTS.md`, `.github/instructions/`, and `.github/skills/`) when working inside `private/`. The innermost (submodule-local) instructions take priority over top-level repository guidance.

## When edits are allowed

Acceptable reasons include upstream syncs, urgent security fixes, owner-requested public releases, or owner-approved cleanup.

Required artifacts when proposing edits:

- Owner approval
- Short justification
- If publishing: a migration checklist covering PII, licenses, sensitive datasets, and redactions

## Migration workflow (recommended)

1. Validate academic content (if applicable):

```sh
python .github/skills/academic-notes/validate_academic.py --content private/special/academia/<INSTITUTION>
```

1. Prepare a migration checklist and a sanitized patch/diff.
2. Use `publish.py` to mirror curated content into the public repository; do not copy files manually.

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
