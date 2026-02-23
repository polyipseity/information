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
  - References in glosses should use full bibliographic form and,
    when listing multiple works, simulate a list using dashes and
    `<br/>` line breaks on the right‑hand side with **a space before the
    `<br/>`**.  (Addresses user preference for clearer citation formatting.)
  - Preserve slide-level material in full, including rhetorical questions
    and boundary-case prompts (e.g. "are animals robots?"); these become
    their own bullets and are useful flashcards.  Added explicit question
    bullet guidance and examples in patterns.md and examples.md.
  - Acronyms should be avoided unless pervasive; when they are used spell
    out the full phrase on first mention with the abbreviation in
    parentheses.
  - Lists intended for human recall (e.g. robot features) should be collapsed
    to a single-gloss line using hyphens and `<br/>` separators rather than
    multiple sub-bullets; updated patterns and examples accordingly.  (Earlier
    the ELEC 1100 note still used multiple sub-bullets; the issue was fixed on
    2026‑02‑23.  Also corrected missing spaces before `<br/>` in that gloss.)
  - Do not include personal names or contact information for teaching staff
    in course notes; changed ELEC 1100 teaching team entry and added rules to
    patterns, checklist, and SKILL.  (Privacy reminder added 2026‑02‑23.)  Also
    removed the explanatory parenthetical text rather than just marking omissions.
  - Reinforced ISO‑8601 requirement for all date/time fields in the notes;
    updated patterns, SKILL, and checklist accordingly (2026‑02‑23).  This
    prevents ambiguity and aids tooling.  Additionally updated general
    paragraphs to use ISO dates for schedule references, demonstrating the
    practice in actual prose.  Corrected an earlier draft that still used
    abbreviated month names (Feb 9/12/13) and rewrote them as full ISO dates
    (2026‑02‑09, 2026‑02‑12, 2026‑02‑13).  Removed unnecessary spaces before
    percent signs in a grading list to match formatting conventions, including
    non‑breaking spaces earlier.
  - Improved preservation of examples: added multiple modern robot examples
    as separate items in ELEC 1100 and emphasized requirement in patterns.
  - Administrative bullets such as teaching team, grading scheme, makeup
    policy, and honour code were relocated to prose paragraphs after the outline
    on 2026‑02‑23; they remain flashcard‑enabled via cloze markup.  (Paragraphs
    were drafted without cloze first, then clozes added in a separate pass as
    per updated workflow guidance.)  The first rewrite replaced the earlier
    cloze‑laden paragraph with a clean prose summary of the slide content,
    demonstrating the two‑step process in practice.

  made these documented rules in SKILL.md, patterns.md, checklist.md, and
  examples.md.
  These changes required updates to SKILL.md, patterns.md, examples.md,
  checklist.md, and validator behaviour.  The validator warning about missing
  `learning_outcomes` was removed and the check converted to advisory guidance
  instead.

---

Add more lessons or examples here as new patterns or bugs are discovered.
