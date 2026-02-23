# Continuous improvement — academic-notes skill

This note describes the feedback loop for evolving the `academic-notes`
skill.  High-level guidance is captured in the **Continuous improvement**
section of [`SKILL.md`](SKILL.md); consult that file first, then use the
additional detail below when implementing changes.

## Core workflow

1. Collect representative examples from `special/academia/<institution>`
   or from validator output (use `--content` mode).  Record incident reports
   in `.github/skills/academic-notes/reports/feedback_log.md` with a date
   and brief description.  Include any user feedback about missing guidance
   (for example, policies about excluding personal contact details).
2. Update documentation:
   - `patterns.md` for newly observed idioms or normalizations.
   - `examples.md` for concrete snippets illustrating the desired layout.
   - `checklist.md` to surface repeated author actions or gotchas.
3. Enhance `validate_academic.py` when a class of issues recurs.  Add
   corresponding unit tests under `tests/` to prevent regressions.
4. Run the validator against affected content and publish an updated
   summary in `issue_frequencies.md`.
5. Open a small, human-reviewed PR containing the documentation changes,
   any normalization patches, and new tests if applicable.

Keep changes minimal and reversible; avoid bulk regex rewrites without
explicit permission from a maintainer.

## Best practices

- Use `--content` mode to surface advisory suggestions that help authors
  improve notes without blocking commits.
- When suggesting normalizations, list the affected files in the PR
  description so reviewers can inspect them easily.
- Record lessons either in this file or in the repository’s issue tracker.

## Example process

- Identify a pattern: several courses omit the flashcard activation tag.
- Draft edits to `patterns.md` and `checklist.md` explaining the required tag
  format and run the validator to confirm it reports the missing tag.
- (Occasionally a maintainer may add unit tests; if the user prefers not to
  proliferate Python tests in this repo, document that preference and keep
  evaluation manual.)
- After merge, regenerate `issue_frequencies.md` to show reduced counts.

## Version history

- **2026‑02‑22:** Consolidated procedural text into `SKILL.md` and
  shortened this file.  Added the workflow checklist above.
- **2026‑02‑22:** Added explicit reminder that the `academic-notes` skill
  itself is a living document and must be updated whenever new patterns,
  privacy rules, or procedural notes are identified.  Emphasized use of this
  continuous improvement file for tracking such updates and ensuring lessons
  flow back into `SKILL.md`.
- **2026‑02‑23:** Learned several author preferences and encoded them as
  permanent rules:
  - Outline lists should not carry an extra indent level and should appear
    directly beneath the `- topic:` line.
  - Prose summaries must follow the outline and be separated by `---` to
    avoid duplication; added guidance and pattern notes accordingly.
  - Flashcard glosses sharing an identical left‑hand path should be merged
    into a single entry using `<br/>` for multiple points rather than
    repeating the path.
  - Enforced full hierarchy in gloss names by including all parent levels.
  These changes required updates to SKILL.md, patterns.md, and validator
  behaviour.  The validator warning about missing `learning_outcomes` was
  removed and the check converted to advisory guidance instead.

---

Add more lessons or examples here as new patterns or bugs are discovered.
