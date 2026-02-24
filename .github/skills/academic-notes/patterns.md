# Academic notes — detailed patterns

This document collects observed patterns from academic course notes and the preferred conventions for authoring new content across institutions.

## Frontmatter

- Begin file with a YAML frontmatter block delimited by `---` lines.
- Recommended keys:
  - `aliases:` list with course code variants and human names.
  - `tags:` must include `flashcard/active/special/academia/<INSTITUTION>/<PAGE>` for flashcard activation. **This tag is required in all course note files under `special/academia` when flashcards are desired.** Also include `function/index` and `language/in/English` where appropriate.
- **Optional tests:** Occasionally we add a small Python test to document a
  specific pattern (e.g. ensuring a child link is folder‑first).  These
  tests are ephemeral; once the pattern is established in the skill docs the
  test may be deleted with no loss.  Authors do *not* need to create tests
  for ordinary content edits.

> **Reminder:** you do not need to run `init generate` when editing
> academic notes; flashcard state is regenerated automatically by the
> repository’s build/packaging workflows, and agents must never invoke the
> command themselves.  If any internal instructions or templates mention
> manual regeneration, update them as part of continuous improvement.

Example:

```markdown
---
aliases:
  - COMP 3031
  - Principles of Programming Languages
tags:
  - flashcard/active/special/academia/<INSTITUTION>_3031
  - function/index
  - language/in/English
---
```

## Index file structure

- Top-level file is `index.md` and starts with `# index` heading.
- Include an explicit `children` section listing child pages in teaching order.
- Add a `grading` section, optionally with a `scheme` subsection listing assignments/exams and weights.
- When listing child sections under a lecture entry that link to a separate topic-specific note, include full anchor URLs (e.g. `electronic%20component.md#atoms%20and%20charge`) as part of the hierarchical path.  This makes it easy for readers to jump directly to the relevant subsection in the external note.

## Weekly entries

- Use `## week N lecture` / `## week N lab` / `## week N tutorial` headings.  These sessions should be listed in **strict chronological order** according to their `datetime:` fields.  Lectures, labs and tutorials are allowed (and expected) to interleave based on actual dates and times.
  - If the syllabus specifies particular numbered sections (e.g. LA3, T2), ask the user which specific session code(s) apply.  Generate entries only for those sections; ignore others.  After filtering, when each week has at most one lab and one tutorial, reset the numbering to `lab 1`/`tutorial 1` for that week.  Only increment the number within a week if multiple sessions of the same type actually occur.
  - Beware of duplicate week numbers around holidays; a repeated “week 9” should trigger a manual shift (week 10, etc.) and a `status: public holiday` entry.  The validator now warns on duplicate week headings.
  - When a session is marked `status: unscheduled` (holiday, cancelled, overflow), omit the `topic:` field entirely.  This keeps the entry from generating misleading flashcards.
  - Sessions without a known time should still include an ISO date interval; use full ISO intervals when possible to aid automatic auditing and clash detection.
- **Examinations** are treated specially: they should always appear *after* all lecture, lab, and tutorial entries, even if their datetime would place them earlier.  Within the exam block the individual exam entries themselves still follow chronological order.
- Each session includes:
  - `datetime: ISO_START/ISO_END, DURATION` (example: `2025-09-02T12:00:00+08:00/2025-09-02T13:20:00+08:00, PT1H20M`)
  - `topic:` short description (omit when `status: unscheduled`)
  - Optional: `status:`, `venue:`
- Content uses indented bullets to group course-specific annotations and cross-links.
- Venues are especially important for room assignments; at HKUST a bare numeric or range (e.g. `2133&2134`) denotes an Academic Building room, which should be rendered as “Room 2133 & 2134, Academic Building” in the note.  Consistent venue entries aid schedule parsing.
- The new preferred way to record your own lecture/tutorial/lab streams is with a nested `sections:` list in the logistics block.  The outer list groups by type (`lecture`, `tutorials`, `labs`) while the inner list uses dedicated section identifiers (e.g. `L1`, `T2`, `LA3`).  Each inner line pairs the identifier with a venue and a comma‑separated sequence of weekly day‑of‑week/time patterns:

  ```markdown
  - sections:
    - lecture: L1
      - L1: CYT-LTL; MondayT16:00:00/MondayT16:50:00, FridayT11:30:00/FridayT12:20:00
    - tutorials: T2
      - T2: CYT-G001; TuesdayT14:00:00/TuesdayT15:20:00
    - labs: LA3
      - LA3: Room 2133 & 2134, Academic Building; WednesdayT09:00:00/WednesdayT11:00:00
  ```

  The placeholder term `<section identifier>` is used in templates to remind
  authors that the same label appears both at the outer type level and as the
  key for the inner list.  This structure replaces the older `session_times:`
  block and keeps all metadata self‑contained; the comma‑separated list may
  include any number of day/time pairs without upper bound.

## Inline conventions

- `::@::` is used to provide a concise definition or gloss for a linked term.  The left side should resemble a hierarchical path of concepts separated by ` / ` (e.g., `parent / child ::@:: Description`).  The right side must be a single line of source text; do not use sublists — insert `<br/>` to simulate line breaks when needed.
- **Math delimiters:** use `$…$` for inline math and `$$…$$` for display equations.  Avoid TeX‑style `\(\)`/`\[\]` delimiters, which are not consistently supported by the Markdown renderer and linting tools.
- **Emphasis style:** italics should be marked with single underscores `_like this_` rather than asterisks.  Bold text uses double underscores `__like this__` instead of `**`.  This convention reduces ambiguity with Markdown tables and cloze markup and is applied across all note types.
- Use `- Section / subsection ::@:: summary` to create taxonomy-like entries.
- When writing lists or outlines in source, put each top-level item on its own line; insert `<br/>` for hard line breaks within an item and `<p>` for separate paragraphs.  This preserves machine readability while allowing formatted output.
- Every `::@::` gloss must begin with a complete hierarchical path that starts with the course name and includes all intermediate folders (e.g. `ELEC 1100 / what is a robot? / features ::@:: …`).  Do not rely on indentation or headings for context; repeat the full path on each gloss so the flashcard generator can operate independently of the surrounding outline.

- Descriptive paragraphs (e.g. lecture summaries, administrative commentary such as "check Canvas" or grading reminders) should follow the outline list and be separated from it by `---` to avoid accidental duplication and extra indentation.  In the sample week‑1 outline these paragraphs carry all of the course logistics while leaving the bullets reserved for conceptual content.
- **Personal data:** do not include real names, email addresses, phone numbers, or other personal identifiers for instructors, TAs, IAs, TOs, or staff in course notes.  Use generic role descriptions and refer readers to the official syllabus or LMS for contact details; do not add parenthetical notes about omission.
- **Human recall lists:** when a cluster of features or characteristics is
  meant to be memorized straight, avoid multi-line sub-bullets; instead
  collapse them into a single gloss line with hyphen-separated items and
  `<br/>` breaks.  This keeps flashcards succinct while preserving each
  element.
- **Prose descriptors:** after outlining flashcard-worthy bullets, follow with a
  prose paragraph separated by `---` if the instructor gives situational or
  administrative commentary (schedule links, next-week reminders, grading
  breakdowns).  Embed any flashcards via cloze markup in that paragraph.

## What content to capture (content-first guidance)

When creating or improving course notes, aim for **comprehensive, slide‑level
detail**.  Think of your notes as an enhanced transcript: every bullet point or
visual element from the lecture slides, every spoken definition or warning,
and every worked example should be reflected in the text.  Do not settle for a
one‑sentence paraphrase of a concept; expand each idea into its own bullet,
explain the underlying reasoning, and record any numerical values, parameters,
or algorithmic steps mentioned.

Key points:

- **Slide fidelity**: Convert slide bullets directly – if a slide lists three
  characteristics of a device, create three separate outline items.  Add
  instructor elaboration that accompanied the slide as additional bullets or
  notes.
- **Examples**: Preserve worked examples verbatim when they clearly illustrate a
  method.  For multi‑step examples, use numbered lists or multiple bullets that
  mirror the sequence of operations.  If an example is merely a list, render it
  as a sorted sub‑list to expose structure.  Always include *at least one*
  representative example per major concept.
- **Definitions & formulas**: Record full definitions, formula sheets, and the
  conditions under which formulas apply.  Use `::@::` glosses for concise
  flashcard questions, but keep the glossary right‑hand side detailed (e.g.,
  include parameter names and units).  When a concept is linked to a
  `general/` article, provide a path in the glossary and cross‑link accordingly.
- **Instructor commentary**: Capture asides, caveats, and common pitfalls the
  instructor mentions.  These are often exam fodder and should be treated as
  detail rather than noise.
- **Verbatim text**: Avoid copying large proofs or policy statements; instead
  summarize and link to existing `general/` pages or attachments.  However,
  short quotes or definitions that are central to the lecture should be copied
  in full.
- **Level consistency**: Apply this detailedness uniformly across lectures,
  tutorials, labs, and even exam review sessions.  The goal is to make the notes
  self‑contained enough that a reader could reconstruct the lecture flow and
  review all critical content without referring back to slides or recordings.

This high level of detail supports better flashcards, easier exam revision, and
more accurate archival of course knowledge.  Err on the side of including more
information; excess material can always be trimmed later by a maintainer.

For each session, prefer the following elements where appropriate:

- `topic:` and a short `takeaway:` line — scannable summary for revision.
- Instructor emphasis — note any points the instructor stressed.
- Key definitions & concise glosses — use `::@::` for flashcard-worthy bites;
  cross-link to canonical `general/` pages for full definitions.
- Worked examples & step-by-step solutions — include at least one worked
  example demonstrating common techniques or pitfalls.
- Sample exam-style questions / practice problems — add problems and link to
  solutions in `questions/solutions.md`.
- References & resources — slides, recordings, page numbers, and further
  reading links.

## Field types and expectations

- `datetime:` — ISO interval `YYYY-MM-DDThh:mm:ss+TZ/END` and optional ISO duration after a comma.  In fact, all date/time fields in notes (simple `date:`, `time:`, `datetime:`) should use ISO‑8601 format consistently.
- `topic:` — short, plain-text summary.
- `attachments:` — list or folder; reference files using relative links.
- `::@::` concise glosses — inline, short definitions intended to be flashcard-friendly.

## Cross-references

- Prefer linking to `general/` canonical notes for repeated concepts (e.g., `../../../../general/functional%20programming.md`).
- When choosing which `general/` page to link, prefer authoritative article titles (Wikipedia or canonical sources). Agents should use the included helper `find_wikipedia.py` to search Wikipedia and select a candidate. Do NOT create, modify, or add files under `general/`; instead link to the expected `general/` path.
- When a concept merits its own topic-specific note, create a new page in the
  course folder using the Wikipedia article title as the filename.  Lowercase
  the filename and use normal capitalization only where required (e.g.
  `electronic component.md`).  The top‑level heading inside the note should
  match this style (i.e. `# electronic component` rather than `# Electronic
  component`) to mimic Wikipedia’s lowercase‑first convention.  Write the
  note in a Wikipedia‑style voice – neutral, third person – but the level of
  detail should reflect the available course materials (slides, transcripts).
  Add the new file to the course index and link to it from relevant lecture
  entries; the topic note itself may cross-link back to the `general/`
  article for additional background.

  - **No hard line breaks:** avoid inserting manual newline characters for
    readability; rely on soft-wrap.  This keeps Git diffs clean and makes
    automated tools simpler.
  - **Self‑contained paragraphs:** split text into paragraphs only when the
    subject matter shifts; each paragraph should stand on its own so that a
    reader skimming for a term can understand it without context from
    neighbouring paragraphs.
  - **Math handling:** all LaTeX (inline or block) must appear on a single
    source line.  Block equations should not be isolated on their own lines
    with surrounding blank lines; they belong directly in the paragraph that
    introduces or follows them.

## Observed usage patterns

- `::@::` is heavily used as the inline gloss/flashcard separator.
- Hierarchies may span multiple levels; group related flashcards under intermediate
  folders (e.g. `/ robotics introduction / features / …`) when it helps readability.
- Taxonomy / chain notation: authors sometimes list chains of related concepts using arrows and `::@::` boundaries (seen in several course collections). Preserve these as-is when possible.
- Takeaway shorthand: many files use a single-line `takeaway ::@:: ...` — treat these as candidates for `takeaway:` in a normalization PR.
- Authors often capture their lab/tutorial section codes (e.g. LA3, T2) near the top of the note; agents should request this early and filter schedules accordingly to avoid clutter from irrelevant streams.
- Multiple lectures per week are common; capture each with a separate numbered heading and ensure the order follows the actual datetimes.
- HTML comments such as `<!-- future term sections ... -->` are sometimes inserted to simplify long-term editing of index files.
- Inline annotation tokens (e.g., `{@{...}@}`) are used for emphasis or examiner notes; preserve them unless a maintainer asks for normalization.

## Normalization recommendations

- Accept liberal use of `::@::` as a flashcard signal, but normalize session metadata when editing (convert inline `topic ::@::` to `- topic:` and add `datetime:` when available).- When a lecture produces a long enumeration of related subfields or topics, consolidate the list by grouping items into logical categories or merging them into a single gloss.  Avoid dozens of standalone bullets that merely repeat each item; this improves readability and reduces flashcard noise.
- Do not duplicate material that already lives in a topic-specific note.  The index should link to the external file with appropriate section anchors and may include only a brief summary or lecturer comment.  Copying full definitions or examples back into the index introduces redundancy and makes future edits harder.- Preserve existing `flashcard/active/...` tags; where missing, report files and propose adding the tag in a PR rather than mass-editing.
- When linking to `general/`, prefer authoritative article titles and link to the percent-encoded filename (do not create `general/` files in the same PR unless requested).

## Validation hints

The validator (`validate_academic.py`) supplements these patterns with
mechanical checks.  It currently warns for:

- Missing or malformed frontmatter tags (flashcard activation tag required).
- `index.md` files without a `# index` heading or a `children:` list.
- Session entries lacking `datetime:` or `topic:` (the latter only in
  `--content` mode).
- Exams appearing before other sessions; duplicate week numbers (suggesting
  holidays); and unscheduled sessions that still include a `topic:` field.
- Semester headings in institution indexes that are out of chronological
  order.

These warnings are advisory by default, but they often point to real
content inconsistencies.  Consult the checklist and examples when addressing
them.

## Formatting gotchas

- HTML fragments (`<p>`, `<br/>`) are often necessary when preserving manual line breaks in outline items; use them as described in the inline conventions section.  Keep each list item on a single source line.
- Avoid creating separate lecture files; the index page with nested sections and sub-items is the preferred structure.
