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
  - Sections metadata template was overhauled (2026‑02‑23): documentation and
    examples now describe a nested `sections:` list keyed by **section
    identifier**, with the identifier repeated at the inner list level and
    allowing an unbounded comma-separated sequence of weekday/time pairs.  The
    course template, patterns, examples, and checklist were all updated and a
    unit test added to ensure the placeholder remains present.

  made these documented rules in SKILL.md, patterns.md, checklist.md, and
  examples.md.
  These changes required updates to SKILL.md, patterns.md, examples.md,
  checklist.md, and validator behaviour.  The validator warning about missing
  `learning_outcomes` was removed and the check converted to advisory guidance
  instead.
- **2026‑02‑23:** Learned several author preferences and encoded them as
  permanent rules:
- **2026‑02‑24:** Added guidelines for topic-specific notes:
  - Agents should proactively propose and scaffold course notes for broad
    concepts (e.g. electronic component) rather than crowding lecture
    entries.  Notes belong under `special/academia/<INST>/<COURSE>/` with
    lowercase filenames; include singular/plural aliases and concatenated
    course-code variants.  Links from sessions should include section
    anchors.  Added extensive examples in SKILL.md, examples.md, patterns.md,
    and validator checks reflect this pattern.  See the ELEC 1100 changes
    committed on the same date for a concrete implementation.
  - **Formatting rules for topic notes:** do not insert manual line breaks;
    rely on editor soft-wrap.  Paragraphs should be logically self-contained
    – they may be long but should make sense on their own.  All LaTeX must be
    on a single source line, and block math should not be surrounded by
    empty lines.  These styling points were added to SKILL.md and patterns.md.
  - **Emphasis delimiters:** switched to underscores for italics (`_x_`) and
    double underscores for bold (`__x__`) rather than `*`/`**`.  This
    convention was noted in patterns.md to avoid conflicts with tables and
    cloze markup and now applies to all note types.- **2026‑02‑24 (evening):** Learned additional author preferences during
  the ELEC 1100 Week 1 work, and subsequently **removed a temporary python
  test** that verified outline formatting (the pattern is now documented in
  the skill itself):
  - `children:` lists must place all folders before files (folder-first) –
    updated checklist and validator language.
  - Avoid editing earlier lecture summaries when adding new sessions; each
    paragraph should concern only its own session.
  - Session outlines may link to specific sections of external topic notes
    using anchors; updated examples and patterns accordingly.
  - Math equations should *always* use `$…$`/`$$…$$`; TeX-style delimiters
    are prohibited.  Added explicit guidance in patterns and examples.
  - Topic-note filenames and headings follow normal sentence casing; section
    headings adhere to the same rule.  Reinforced in examples.

- **2026‑02‑25:** Added explicit rules about prose paragraphs before
  flashcard lists and removed the requirement for generic "lecture summary"
  sections unless they contain important grading information.  Updated
  SKILL.md accordingly and applied fixes to existing ELEC 1100 notes.
- **2026‑02‑25 (later):** Introduced two further conventions:

  1. Paragraph cohesion – prose should read with Wikipedia‑style flow and
     transitions rather than a sequence of disjoint statements.
  2. Mathematical notation must always use LaTeX in math mode; Unicode
     symbols are discouraged outside of `$…$`/`$$…$$`.  Updated SKILL.md and
     patterns.md, and converted existing ELEC 1100 passages to comply.
- **2026‑02‑25 (even later):** Added guidance on:

  - Example calculations in flashcards: left side holds all given data, right
    side outlines computation steps.
  - Index entries linking to topic‑specific note sections via anchors.
  - Flashcard formatting: cards must be one‑line in source; use `<br/>` or
    `<p>` for any required hard breaks instead of actual newlines.  Flashcards
    should contain exactly one `::@::` (or at most one `:@:` for one-sided
    cards); earlier versions of this note mistakenly generated cards with two
    separators which prevented proper generation.  For calculation examples,
    ensure *every number used in the computation* — including intermediate
    values and final answers — appears before the separator.  The right side
    may then be limited to generic formulaic instructions.  Long left-hand
    text is permitted for clarity.
  - **Audit habit:** when fixing or adding flashcards, read each line of the
    source file sequentially to catch any hidden calculations or formatting
    errors.  Partial reviews led to earlier mistakes; a complete pass avoids
    omissions.  - Line wrapping policy: avoid hard wraps; soft wrapping is used by editors.
  - Lesson: the Ohm’s law example card originally placed $V$ and $R$ after the separator; the misplacement was caught and corrected on 2026‑02‑25, and a subsequent edit accidentally added a second `::@::` which had to be removed; always re‑check flashcards after editing.

These rules were added to SKILL.md and applied to the ELEC 1100 index.

---

Add more lessons or examples here as new patterns or bugs are discovered.
