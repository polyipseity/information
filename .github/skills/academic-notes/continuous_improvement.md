# Continuous improvement — academic-notes skill

This note documents the feedback loop for evolving the `academic-notes` skill.
High‑level guidance is captured in the **Continuous improvement** section of
[`SKILL.md`](SKILL.md); consult that file first and use the short workflow
below when making changes.

## Core workflow

1. Collect representative examples from `special/academia/<institution>` or
   run the validator (`--content` mode) and record incidents in
   `.github/skills/academic-notes/reports/feedback_log.md` with a date and
   brief description.  Include user feedback such as privacy concerns or
   template suggestions.
2. Update documentation:
   - Add new idioms/normalizations to `patterns.md`.
   - Write illustrative snippets in `examples.md`.
   - Surface repeated author actions or gotchas in `checklist.md`.
3. Extend `validate_academic.py` when a pattern recurs, and add corresponding
   unit tests in `.github/skills/academic-notes/tests/`.
4. Run the validator on affected files and refresh `issue_frequencies.md`.
5. Open a focused PR containing the documentation/test changes and any
   normalization patches; keep edits human-reviewable and avoid mass regex
   rewrites without owner approval.

## Best practices

- Use `--content` mode for advisory warnings.
- When proposing normalizations, list affected files in the PR description.
- Prioritize updating skill docs over this file; store process notes in the
  feedback log or the repository issue tracker.

## Example process

- Spot a recurring omission (e.g. missing flashcard tags).
- Update `patterns.md`/`checklist.md` and verify the validator detects it.
- After merge, regenerate `issue_frequencies.md` and watch the frequency drop.

## Version history

Early history recorded numerous lessons; most of those entries have now been
migrated into the active skill files listed above.  See the Git log or the
individual documents for detailed change rationales.  This file retains only a
brief archive of the latest consolidation.

- **2026‑02‑25 (latest consolidation):** Moved the bulk of the continuous
  improvement entries into `SKILL.md`, `patterns.md`, `examples.md`,
  `checklist.md`, `issue_frequencies.md`, and validator tests.  Added a note
  to the course template and introduced explicit rules requiring every
  Markdown section to include a flashcard block and for authors/agents to
  update flashcards when editing sections.  The remaining text here serves
  as a provenance record; actionable guidance should now be sought in the
  other documents.
