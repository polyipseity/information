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
> you.  Agents in particular must **never** attempt to invoke the generator
> manually.  If you encounter instructions that suggest manual regeneration,
> update the documentation and templates as part of the continuous‑learning
> process.

The skill is designed for **continuous learning**: as agents and human authors
work with real course content, their preferences and new patterns inform
updates to the documentation.  Lessons and feedback gathered during usage
should be recorded in this skill’s folder—in particular the
`continuous_improvement.md` document—ensuring that observations persist
alongside the documentation and are easy for maintainers to review later.  Explicit user directives
(for example, "never run init generate automatically") should be incorporated
into the text so that future interactions respect those choices.

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
   brief description.  For aliases include both singular and plural forms
   where they make sense (e.g. "assignment" and "assignments"), and add
   concatenated variants without spaces if the course code is normally
   written with or without a space (e.g. `ELEC 1100`/`ELEC1100`).  Sort the
   alias list strictly in alphabetical order to aid consistent diffs and
   validator checks.
2. Add a `logistics` section with a nested grading `scheme:` block specifying
   weights for labs, exams, projects, etc.  Must include a `sections:` list
   containing lecture/tutorial/lab **section identifiers** together with
   venues and comma‑separated weekly time patterns.  The list is nested by
   session type (lectures, tutorials, labs) and allows an unlimited number of
   day/time pairs per identifier; refer to `patterns.md` for the exact layout.

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
   - Situational or administrative remarks (schedule links, upcoming-week reminders, grading weights, Canvas/LMS alerts) should **never** be written as outline bullets.  The example week‑1 lecture shows the proper approach: all logistics, exam weights, and rights/expectations appear in a continuous prose paragraph following the structured bullet hierarchy.  Place the paragraph **after** the bullet outline and separate it from the list with a horizontal rule (`---`).  Draft the prose first without cloze markup to ensure natural flow, then add `{@{ }@}` or `::@::` glosses in a second pass for any facts you want to memorise.  See the flashcard-creation skill for help writing effective cloze sentences.
   - **Paragraph style before flashcards:** when you transition from explanatory content to a `Flashcards for this section` list, the preceding text must be written as one or more natural paragraphs rather than as a continuation of the bullet outline.  Avoid using hyphen‑prefixed list items for prose; bullets are reserved for hierarchical points and gloss hints only.  This keeps rendered notes readable and prevents the outline validator from misclassifying descriptive text as additional flashcards.
   - **Example calculation flashcards:** when a session contains worked numerical examples, the left‑hand path must include all given values and parameters required for the computation, and the right‑hand side should briefly outline the calculation steps (formula substitution, intermediate values, final result).  This ensures the card stands alone and is useful during review.
   - **Paragraph cohesion:** aim for high lexical and conceptual cohesion in prose sections, similar to the style used in Wikipedia articles.  Combine related sentences with transitional phrases and minimise abrupt topic shifts; treat paragraphs as self‑contained mini‑essays rather than a list of loosely related statements.
   - **Lecture summaries:** do not add a separate "lecture summary" section at the end of a session unless it conveys an important grading component (for example, exam due dates, weightings, or review topics).  Most summaries are redundant and clutter the notes; the validator will warn if a summary heading is present so authors can re‑evaluate its necessity.
     - **Privacy note:** omit real names, emails, phone numbers, office locations, or any personally identifying information for instructors, TAs, IAs, TOs, or staff; refer readers back to the official syllabus/LMS for contact details and do not flag that you have redacted names.
   - Treat the course notes as a structured transcript of the lecture rather than a terse summary.  Every slide bullet, formula, definition, and instructor comment is a candidate for inclusion; err on the side of including too much because flashcards are generated automatically and extra content aids recall.  The opening week example demonstrates how multiple related concepts (definitions, history, features, examples, comparisons) can coexist under a single session header using nested bullets and full hierarchical paths.
   - Preserve the full semantics of the original lecture slides or spoken commentary.  Do **not** merge two or three separate points into one vague sentence.  Each distinct idea or logical step should occupy its own bullet (or sub‑bullet) along with a corresponding `::@::` gloss if appropriate.  When capturing enumerations such as the robot features or example lists shown in the week‑1 outline, either use nested sub‑bullets or put the entire list on one line with `<br/>` separators so the flashcard generator still treats them as a single entry.
   - Capture numeric values, parameter ranges, diagrams described in words, algorithm steps, and decision criteria.  For multi‑step examples (derivations, code walkthroughs, troubleshooting procedures), write them out as numbered lists or multiple bullets that mirror the sequence of operations.
   - Avoid high‑level summaries like "we discussed X"; instead, spell out what "X" consisted of.  Conversely, lengthy proofs or policy text that belong in reference material should be summarised with a link to an appropriate `general/` page or attachment rather than transcribed verbatim.
   - Always include at least one representative worked example or problem per major concept.  Simplifying long enumerations to alphabetized sublists is still considered adequate detail because it exposes the underlying structure.
   - When a slide or lecture discussion generates a long list of related areas (e.g. “ECE areas relevant to robotics”), resist creating a separate top‑level bullet for each item.  Instead, chunk them under a descriptive parent or combine them into a single gloss with `<br/>` separators.  Grouping similar concepts improves readability and prevents an explosion of low‑value flashcards.
   - Do **not** duplicate material that already appears in a topic‑specific note.  The index entry should simply link to the external file (with appropriate section anchors) and may include a brief summary or the instructor’s remark.  Transcribing full definitions, examples, or explanations from the note back into the index bloats the outline and creates maintenance headaches.
   - Record instructor emphases, asides, exam hints, and common pitfalls as standalone bullets or nested notes – these often turn into valuable flashcards.
   - Avoid introducing acronyms unless they recur frequently.  When you do use an abbreviation, spell out the full phrase on first mention with the acronym in parentheses (e.g. "Robot Institute of America (RIA) definition") to ensure clarity for readers and flashcards.
   - Preserve rhetorical questions and boundary-case prompts ("are animals robots?", "is a motorcycle a robot?") as separate bullets; they surface important distinctions and make excellent flashcard candidates.
   - This detailed, content‑first approach applies **uniformly** to all course materials – lectures, tutorials, labs, exams, and review sessions.  Do not treat later weeks more tersely just because they are routine; maintain the same level of bullet‑by‑bullet fidelity throughout the semester.
6. Insert `::@::` glosses for flashcard-worthy facts; follow `flashcards.md`
   for best practices.  The linked document also describes an alternate
   two-sided Q/A style used in some course topic notes: when a section
   contains a list of question/answer pairs, precede it with a horizontal
   rule (`---`), insert a blank line, and then add the exact sentence
   “Flashcards for this section are as follows:” so that tooling and readers
   can recognise the start of the QA list.  (The flashcard-creation skill has its own guidance and
   examples for performing the rewrite.)

   - **Example calculation flashcards:** when class material includes
     numerical examples, ensure the left‑hand path lists all given values
     and the question being asked, and use the right-hand side to sketch the
     computation steps (formula application, intermediate results, final
     value).  Cards should be self-contained.
   - **Single-line flashcards:** all flashcards (two‑sided Q/A or cloze) must
     be written as a *single source line* with no hard newline characters.
     The automatic generator splits on line breaks, so inserting a newline
     will break the card.  If you need logical visual separation, use
     `<br/>` or `<p>` instead.
   - **Single separator:** for two-sided cards use exactly one `::@::` and for
     one-sided cards at most one `:@:`.  Multiple separators on a line will
     confuse the generator and produce invalid cards.   - **Newline encoding:** avoid wrapping long lines – soft wrap is used in
     editors.  When a hard break is genuinely necessary for readability,
     insert `<br/>` for a line break or `<p>` for a new paragraph rather than
     hitting Enter in the source.
   - **Index link rule:** lecture entries in the index that cover material
     located in a separate topic note must include explicit bullets linking
     to each relevant section of that note via an anchor.  This documents
     which sections were discussed and lets readers jump directly to the
     appropriate subsection.
   - **Duplicate section check:** before adding a new `### week N lecture M`
     heading in an index file, search for an existing section with the same
     title.  Agents should never blindly create a new section if one already
     exists; instead update the existing entry.  This prevents accidental
     duplicates and keeps the chronology coherent.

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
repository's build tools; authors and agents do **not** need (and should not)
run `init generate` manually when editing notes (the CI and packaging workflows
handle it).

### Linking to general content

Course notes should **never** create or modify files under `general/`.
Instead, link to existing encyclopedia articles by name (percent-encoded).
Agents may use `find_wikipedia.py` to query titles and choose the best match.

### Topic-specific notes

When a lecture introduces a concept that is broad enough to merit its own
encyclopedic article and is (or will be) discussed in sufficient depth, you
should create a **topic-specific note** under the course directory.  These
notes serve as stable reference pages that can be linked from multiple
sessions without repeating the same material.  The note itself should be
written in a neutral, Wikipedia-like style – third person, descriptive tone
– although the level of detail is governed by the available course
materials (lecture/talk transcripts, slides, lab manuals, etc.).

- **File layout:** topic-specific notes are authoritative reference pages,
  not slide transcripts.  They live under `special/academia/<INST>/<COURSE>/`
  with filenames derived from canonical Wikipedia article titles.  Authors
  and agents should **never** insert hard line breaks for readability – rely
  on the editor’s soft-wrap and the rendered viewer.  Paragraphs may be long
  or split, but each paragraph should be mostly self-contained (a reader who
  reads only that paragraph should understand its subject roughly 80 % on its
  own).  Do not insert blank lines arbitrarily except to separate logical
  paragraphs.
- **Math formatting:** both inline `$…$` and display `$$…$$` LaTeX must remain
  on a single source line.  Never break the math code across lines.  Block
  equations should appear in the same paragraph as surrounding text; avoid
  placing a `$$` line by itself or inserting additional blank lines before or
  after it.  This rule applies globally, not just within topic notes.
- **Paragraph style:** large paragraphs are acceptable; feel free to split
  when the content naturally shifts focus.  The reader should not have to
  backtrack to preceding or following paragraphs to understand the current
  one.  Conciseness is valued, but do not trim detail to the point of
  obscuring meaning.
- **Cross-references:** link from lecture entries to the note and include
  section anchors for specific headings if the session covers only part of
  the topic.  See the index-linking examples later in this section.

- **When to create**: the subject should be general (i.e. something that could
  plausibly have a Wikipedia page) and it should either appear in the current
  lecture slides with substantial detail or be scheduled for extended coverage
  later in the semester.  If the topic is only mentioned in passing or is
  highly idiosyncratic to the course, keep the discussion inside the lecture
  entry instead.
- **Agent behaviour:** when acting as an agent transcribing notes, watch for
  sessions that produce long lists of related definitions or examples (e.g.
  charge, current, voltage, resistor, capacitor).  Rather than bloating a
  single lecture entry, you should **proactively propose creating a new
  topic-specific note**.  Run `find_wikipedia.py` with an appropriate keyword to
  find a canonical title.  The script will print a suggested `general/` path;
  **ignore that suggestion**.  course topic notes must always live under the
  course folder (`special/academia/<INST>/<COURSE>/`).  Scaffold the new file
  there using the template above, and add a link/see‑also reference in the
  session outline.  This automation keeps course pages concise and makes later
  reuse easier.  The remainder of the current session’s bullet list can then
  be collapsed to a summary pointing at the new note.
- **Checking for duplicates**: before creating a new file, search the course
  folder for existing topic notes (a simple `grep`, `fd`, or `rg` on the topic
  name works well).  If a suitable note already exists, append the new
  content there and add additional index links as needed; **do not create a
  duplicate file**.  The `children:` list at the top of `index.md` should be
  updated whenever a new note is added so that the hierarchy remains explicit.
- **Naming the file**: use the canonical Wikipedia article title as the
  filename, converted to lowercase with only necessary capitalization (for
  example `electronic component.md`, `forward contract.md`).  The helper
  script `find_wikipedia.py` is highly recommended; run it with the topic
  keyword(s) and pick the top candidate from its JSON output.

Example invocation:

```bash
python .github/skills/academic-notes/find_wikipedia.py "electronic component"
```

The script prints lines containing `"title"` and `"url"`; the `title` gives
you the proper article name.  Use that title (percent‑encoded) when linking to
`general/` and as the basis for the filename in `special/academia`.

- **Template for a new topic-specific note**: adapt the aliases and tags for
  the current course.  Replace `<INSTITUTION>` and `<COURSE>` with the
  appropriate values, and convert spaces to underscores in the flashcard tag.
  As with course pages, include plural variants and sort the alias list
  alphabetically.

```markdown
---
aliases:
  - <COURSE> <topic>
  - <COURSE><topic>
  - <INSTITUTION> <COURSE> <topic>
  - <INSTITUTION> <COURSE><topic>
  - <topic>
tags:
  - flashcard/active/special/academia/<INSTITUTION>/<COURSE>/<topic_with_spaces_replaced_by_underscore>
  - language/in/English
---

# <topic>

- <INSTITUTION> <COURSE>

---

- see: [general/<wiki_title>](../../../../general/<wiki_filename>.md)
```

- **Index linkage**: add the new note to the `children:` section of the main
  `index.md` file and insert a `- see also:` cross‑reference under the
  relevant lecture(s).  For example, after the outline for week 1 lecture 2
  you might add:

  ```markdown
  - see also: [electronic component](electronic%20component.md)
  ```

  This approach lets learners navigate from a session summary to the
  dedicated topic note.

  When a topic-specific page has multiple sections, you should also create a
  nested index list under the course entry that enumerates each major
  subsection in the same order they were covered in lecture.  **However, the
  `children:` list itself should only link to the file**; the sub‑adornment of
  section anchors belongs in the session entries, not in `children:`.  Topic
  notes must appear **after all folder entries** (assignments, attachments,
  labs, questions, tutorials) and, among files, should be sorted
  alphabetically by filename.  This keeps the index clean and predictable.

  The session entries (lectures/labs/tutorials) should include both a link to
  the file and a `§` reference to the specific section covered.  Do **not**
  prefix with "see also:"; instead nest the course path directly under the
  entry.  For example:

  ```markdown
  - topic: basic components
  - ELEC 1100
    - ELEC 1100 / [electronic component](electronic%20component.md)
      - [§ definition](electronic%20component.md#definition)
  ```

  The nested list of anchors in the broader index is optional but still
  useful for long topics; it must mirror lecture order exactly.  A generic
  template for the index structure is:

  ```markdown
  - <COURSE_CODE>
    - <COURSE_CODE> / <topic>
      - [§ <heading>](<topic>.md#<anchor>)
      - [§ next heading](<topic>.md#<next-anchor>)
      - …
  ```

  Concrete examples (FINA 3103 and Scala) demonstrate how the pattern looks
  in practice while preserving the original teaching sequence.
- **Ongoing maintenance**: when later lectures revisit the same topic,
  append new material to the existing topic note rather than creating a new
  page.  The link from each session can remain the same.

These topic-specific pages help avoid duplication, make detailed concepts
easier to find, and encourage reuse of general knowledge across multiple
courses.

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
