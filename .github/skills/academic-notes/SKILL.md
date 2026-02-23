---
name: academic-notes
description: Content-first conventions, examples, and light tooling for authoring and validating academic course notes across institutions (HKUST, other universities, colleges).
---

# Academic notes — skill overview

This skill documents content-first conventions, examples, and lightweight tooling
for authoring and validating academic course notes across institutions.  It is
intended for any course material stored under `special/academia/<INSTITUTION>`
(regardless of university, department, or subject).

> **Flashcard generation is automatic.**  Authors and agents do **not** need
> to run `init generate` or any similar command when editing course notes;
> the repository’s build and packaging workflows regenerate flashcards for
> you.  If you encounter instructions that suggest manual regeneration, update
> the documentation and templates as part of the continuous‑learning process.

The skill is designed for **continuous learning**: as agents and human authors
work with real course content, their preferences and new patterns inform
updates to the documentation.  Explicit user directives (for example, "never
run init generate automatically") should be incorporated into the text so that
future interactions respect those choices.

The skill has three primary audiences:

1. **Content authors (humans or agents)** writing course pages, lecture notes,
   labs, tutorials, and assignments.  Authors should favour a single index page
   over separate per‑lecture files; the `lectures/` subdirectory is optional and
   generally unnecessary.
2. **Maintainers** who review submissions, normalize style, and ensure metadata
   quality across the repository.
3. **Automated tooling** (validators, helpers) that surface common issues and
   provide search assistance.

> ⚠️ **Important — evolving skill, continuous learning, & long-term feedback**
>
> This skill captures subtle, content-driven conventions that emerge from
> many semesters of note-taking and peer review.  It evolves continuously; new
> patterns appear and old habits are corrected.  Treat the skill as a living
> document.  Agents and maintainers **MUST** solicit, record, and incorporate
> user feedback into the instructions over time.  Explicit preferences expressed
> during interactions (e.g. avoiding certain automation or following specific
> formatting habits) are part of this learning process and should be encoded in
> the text.  See the continuous improvement workflow (`continuous_improvement.md`)
> for how to submit feedback, track action items, and propose small, reviewable
> changes.

## Core components

The `academic-notes` skill is implemented as a collection of markdown files and
Python scripts located under `.github/skills/academic-notes/`.  Key artifacts
include:

- **`SKILL.md`** — this overview and high-level guidance (current file).
- **`patterns.md`** — catalog of observed authoring patterns and preferred
  normalizations; use it when writing or reviewing notes.
- **`examples.md`** — numerous concrete snippets showing how to structure
  frontmatter, sessions, assignments, cross‑references, flashcard markup, etc.
- **`checklist.md`** — an author checklist summarizing required and recommended
  steps before committing course content.
- **`issue_frequencies.md`** — auto‑generated summary of validator warnings
  across the repository; useful for prioritizing improvements.
- **`flashcards.md`** — focused guidance on using `::@::` glosses and frontmatter
  tags to enable flashcard generation.
- **`continuous_improvement.md`** — describes the feedback loop and how to keep
  the skill up to date with real‑world course content.
- **`validate_academic.py`** — validator script; run with `--content` for
  advisory checks (see documentation block inside script).
- **`find_wikipedia.py`** — helper for searching Wikipedia and suggesting
  canonical titles when linking to `general/` pages.

Maintainers should periodically run the validator across `special/academia` and
update `issue_frequencies.md` to reflect common problems.

## Authoring guidelines (summary)

When you create a new course note or update an existing one, follow these
steps:

- Keep lecture/lab/tutorial sessions in strict chronological order by their
  `datetime` values; these entries may interleave.  Always use ISO‑8601
  formatting for dates, times, and datetimes (e.g. `2025-09-02T12:00:00+08:00`).
  Exam sections (midterm, final) should always appear **after** all other
  session types even if the dates overlap.  The validator now emits a warning
  when exams precede other sessions.
- For institution-level indexes, ensure semester headings (`### 2025 fall`, etc.)
  progress chronologically; the validator also checks this and warns if the
  sequence is out of order.

1. Start with the **course-template** (`course-template.md`); fill in aliases,
   tags (note the underscore convention for flashes), name, credits, and a
   brief description.
2. Add a `logistics` section with a nested grading `scheme:` block specifying
   weights for labs, exams, projects, etc.  Must include a `sections:`
   list containing lecture/tutorial/lab stream codes, venues, and weekly
   time patterns (see `patterns.md` for format).
3. Maintain a `children:` list in frontmatter or as a YAML section under the
   heading; keep child pages (lectures, labs, assignments) in teaching order.
4. Use the recommended session structure for lectures/labs/tutorials/exams
   (see examples).  Include `datetime:` entries with ISO intervals; if the time
   is unknown, at least provide the date portion.
   - When adding a prose summary or description for a session, place that
     paragraph *after* the outline/list of bullet items and separate the two
     with a horizontal rule (`---`).  This ordering keeps the outline visible
     at the top and prevents accidental repetition or indentation errors.
5. Capture **content‑first details** and err on the side of completeness:
   - Situational or administrative remarks (schedule links, upcoming-week
     reminders, grading weights) should not appear as outline bullets.  Instead,
     place them in a prose paragraph after the bullet outline and separate the
     paragraph from the outline with a single horizontal rule (`---`).
     Authors should **first draft this prose without any cloze markup** to focus
     on natural flow.  Once the paragraph is finalised, perform a separate
     editing pass to add cloze markup (`{@{ }@}` or `::@::`) for any points you
     wish to convert into flashcards.  See the flashcard-creation skill for
     guidance on writing cloze sentences.
   - **Privacy note:** avoid including instructor, TA, or staff names and
     email addresses in course notes; refer readers to the official syllabus or
     LMS for contact information.
   - Treat the course notes as a structured transcript of the lecture rather
     than a terse summary.  Every slide bullet, formula, definition, and
     instructor remark is a candidate for inclusion; if in doubt, include it
     and the validator/maintainers can trim later.  Flashcards are generated
     automatically so having more material usually improves recall.
   - Preserve the full semantics of the original lecture slides or spoken
     commentary when converting them to prose.  Do **not** compress two
     or three related points into a single vague sentence.  Each separate idea
     or logical step should be its own bullet (or sub‑bullet) with its own
     `::@::` gloss if appropriate.
   - Capture numeric values, parameter ranges, diagrams described in words,
     algorithm steps, and decision criteria.  When an example involves a
     sequence of operations (derivation, code walkthrough, troubleshooting
     procedure), write it out as a numbered list or as multiple bullets rather
     than a sentence fragment.
   - Notes that are too high‑level ("we discussed X") are not sufficient;
     detail what "X" actually consisted of.  Conversely, avoid verbatim copying
     of long proofs or text that belongs in reference material – link to a
     suitable `general/` page or attachment instead.
   - You may preserve, simplify, or omit examples based on their quality, but
     always record at least one representative worked example or problem per
     major concept.  Simplifying long enumerations to alphabetized sublists is
     still considered detail because it exposes structure.
   - Instructor emphasis, asides, warnings about common pitfalls, and
     references to external resources are all valuable; include them as
     standalone bullets or notes.
   - Avoid acronyms unless they recur frequently; when an abbreviation is
     used, spell out the full phrase on first mention with the acronym in
     parentheses (e.g. "Robot Institute of America (RIA) definition").
     This ensures clarity for readers and flashcards.
   - Preserve rhetorical questions and boundary-case prompts ("are animals
     robots?", "is a motorcycle a robot?") as separate bullets.  These often
     surface important distinctions and make excellent flashcard candidates.
   - The level of detail described above applies to **all course content**
     (lectures, tutorials, labs, exams) and is not limited to the first week.
     Make the same effort whenever you add or revise material.
6. Insert `::@::` glosses for flashcard-worthy facts; follow `flashcards.md`
   for best practices.
   - **Formatting rules:** always prefix a gloss with a hierarchical path
     using `parent / … / child` before `::@::`.  The path text must include **all
     ancestors** beginning with the course name (e.g. `ELEC 1100 / teaching
     methodology / traditional limitations`).  Do **not** rely on indentation,
     section headings, or week numbers to provide context; the flashcard
     generator uses the literal text.  Keep the text after the cloze on a single
     source line; if you need multiple lines, simulate them with `<br/>`
     instead of nested bullet lists.  This ensures that the automatic generator
     treats each gloss as a discrete flashcard entry.
   - **Outline hierarchy:** when a session covers multiple related themes, use
     nested bullets to group them logically (e.g. list "Robot fundamentals" as
     a parent bullet and indent definition/features/laws/history underneath).
     Deeper nesting is fine – the only requirement is that flashcard glosses
     stay on a single line.  Nesting may extend across multiple levels; feel
     free to insert an intermediate folder bullet when several child cards share
     the same prefix (see the robotics introduction features example below).
     **Always insert a bullet for each folder level and label it with the full
     path** (`ELEC 1100 / intended learning outcomes`, not just
     `intended learning outcomes`); this makes the hierarchy explicit even when
     the folder itself has no direct glosses.  The validator only checks list
     items that occur after the course-level `- <COURSE>` bullet, so logistics,
     grading tables, and other unrelated lists are not flagged.  When a folder
     contains only a single child entry, flatten it by merging the path into that
     child bullet instead of creating an extra layer.  You may still use parent
     bullets purely for readability, but avoid recreating the session header as
     a parent (e.g. "Week 1 lecture 1" is unnecessary).  Always repeat the
     full path in each gloss itself; this avoids ambiguity when cards are
     generated across different sessions.  The validator now checks for and
     warns about two-space-indented bullets that lack a `/` path prefix, which
     helps catch missing labels earlier.  If you have several cards that would
     share the same left‑hand path, merge them into one entry whose right side
     uses `<br/>` to separate the individual points (e.g. multiple learning
     outcomes).  Avoid flattening related points at the same level; the
     structure should mirror the conceptual hierarchy rather than merely
     separating topics by blank lines.
7. Run the validator (`validate_academic.py`) to catch missing metadata or
   structural issues; address warnings where practical.
8. Add assignments, questions, attachments, and other accessories in their
   designated subfolders and list them under `children`.
9. Use the author checklist (`checklist.md`) before committing to ensure
   nothing important is overlooked.

### Flashcard activation tags

> **Outline formatting reminder:** when writing lists or outlines in source
> code, keep each top‑level bullet on a single line.  Use `<br/>` for hard line
> breaks within an item and `<p>` for separate paragraphs; this keeps the
> machine‑readable structure intact while allowing rich formatting in rendered
> notes.

Tags must follow the pattern

```text
flashcard/active/special/academia/<institution>/<page>
```

`<page>` normally mirrors the course code using underscores (`COMP_3031`).
Spaces should never be percent‑encoded in tags.  Validators flag missing or
malformed tags.  Flashcard state is regenerated automatically by the
repository's build tools; authors do **not** need to run `init generate`
manually when editing notes (the CI and packaging workflows handle it).

### Linking to general content

Course notes should **never** create or modify files under `general/`.
Instead, link to existing encyclopedia articles by name (percent-encoded).
Agents may use `find_wikipedia.py` to query titles and choose the best match.

### Content patterns and normalizations

Refer to `patterns.md` for a comprehensive list of idioms that appear in
existing notes, along with recommended normalizations.  Common patterns
include:

- Inline glosses using `::@::` to attach definitions and takeaways.
- Taxonomy or chain notation connecting related concepts with arrows.
- Takeaway shorthand lines that should be promoted to structured
  `takeaway:` fields.

When performing normalizations, prefer small, targeted PRs with human review.
Do not mass‑apply regex-based rewrites without explicit maintainer approval.

## Validator usage

The `validate_academic.py` script is the primary automation for this skill.
Run it with:

```bash
python .github/skills/academic-notes/validate_academic.py special/academia/HKUST
```

Use the `--content` flag to switch from strict linting to advisory mode.  The
script emits warnings for missing frontmatter keys, absent flashcard tags,
incorrect `datetime:` formats, exam placement, duplicate week numbers, and
other common mistakes.  It now also warns when a session marked
`status: unscheduled` still has a `topic:` field, or when semester headings are
out of order.  The output is intended to help authors self-correct; maintainers
may enforce particular rules as needed.

Example summary (see `issue_frequencies.md` for the latest global report):

- Missing `children:` YAML key.
- Course files without flashcard activation tags.
- Session entries lacking `datetime:`.

Issues are tracked and frequently updated in `issue_frequencies.md`.

## Continuous improvement

This skill is not static.  To keep it accurate and helpful:

- **Collect feedback** from users and agents.  Logs are stored under
  `.github/skills/academic-notes/reports/` (create the directory if needed).
  Include notes about template comments, outline formatting rules, privacy
  policies, and other authoring heuristics so the skill and templates can
  evolve appropriately.
- **Update the documentation** (`patterns.md`, `examples.md`, `checklist.md`)
  whenever a new idiom or frequently occurring issue is observed.
- **Extend the validator** when recurring errors are identified, making sure
  to exercise new rules via tests or sample files.
- **Publish issue frequency summaries** after each major validation run to
  highlight areas where authors consistently struggle.

See `continuous_improvement.md` for a formal workflow and example.

## Contributing changes

- Propose small, atomic PRs that modify one aspect of the skill or fix a
  specific normalization.  Include rationale and before/after examples.
- The skill directory may contain helper Python scripts (e.g. the validator
  or Wikipedia helper).  Tests for those scripts **should be placed in the
  `tests/` subdirectory of the skill itself** (`.github/skills/academic-notes/tests/`), not in the repo’s top-level `tests/` tree.  This keeps
  skill-specific checks close to the code they exercise while avoiding
  pollution of the global test namespace.
- Update or add tests in that skill-local tests folder when extending the
  validator script; don’t scatter academic-notes tests throughout the root
  `tests/` directory unless they are shared with other components.
- Run `pnpm run format` and `pnpm run check` before submitting, and ensure
  `pnpm run test` passes locally.
- When editing skill documentation itself, mention in the PR description that
  the change affects `academic-notes` and reference relevant issue numbers or
  feedback notes.

By continually refining this skill, we can ensure that academic course notes
remain a useful, high-quality resource across the repository.
