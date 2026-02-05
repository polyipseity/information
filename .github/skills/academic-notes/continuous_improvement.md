# Continuous improvement — academic-notes skill

This document describes the feedback loop for continuously improving the `academic-notes` skill and its validator/examples.

Workflow

- Gather examples from course folders under `special/academia/<INSTITUTION>`.
- Update `patterns.md` and `examples.md` with newly observed idioms and normalization guidance.
- Run `validate_academic.py --content` to discover common missing metadata and produce reports.
- Create small, reviewable PRs containing suggested normalizations and example patches.
- After merge, re-run validator and update `issue_frequencies.md`.

Best practices

- Prefer human-reviewed PRs for normalization; do not mass-apply automated fixes without maintainer consent.
- Record any new inline idioms (e.g., `::@::` variants, taxonomy chains) in `patterns.md` with examples in `examples.md`.
- Keep the validator conservative — use `--content` mode for advisory warnings and only enforce rules when maintainers request stricter behavior.

Example: improving the skill instructions (no PR performed)

- Step 1 — collect feedback: a user reports that the flashcard activation tag examples are confusing. Record the feedback in a short note file (e.g., `./reports/feedback_log.md`) with date, reporter, and brief description.
- Step 2 — draft a minimal instruction edit locally: update `SKILL.md` or `patterns.md` with a one-paragraph clarification and an explicit example. Keep the change atomic and well-commented.
- Step 3 — validate locally: run `python validate_academic.py --content special/academia/<INSTITUTION>` and confirm no regressions in examples.
- Step 4 — present the draft to the maintainer as a patch or PR for review. Since you asked for "no PR" in this workflow example, instead save the draft change as a patch file (`git format-patch` or a unified diff) and attach it to the feedback note so a maintainer can apply it.
- Step 5 — after review, incorporate reviewer comments into the instruction and update `issue_frequencies.md` if the change reduces common warnings.

Notes:

- Keep edits minimal and reversible. Prefer adding examples and clarifications rather than sweeping automated normalizations.
- Always link feedback to a short test or validation run to show the effect of the change.
