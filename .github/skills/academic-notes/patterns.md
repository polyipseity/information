# Academic notes — patterns for agent guidance

**Agents must read every line of every file in this directory (`.github/skills/academic-notes/`) before making decisions; do not skim or skip sections.**

This file is a compact reference used by the academic-notes skill to drive note creation, validation and normalization. It enumerates the rules and conventions agents must apply when authoring or editing `special/academia/**` content. Keep lines unwrapped; each bullet is a discrete rule.

## frontmatter

- every note must start with `---` YAML block.
- aliases list should include every course code variant and the human name; tags list must include a single `flashcard/active/special/academia/<INSTITUTION>/<PAGE>` tag. index pages also need `function/index` and most pages should have `language/in/English`.
- optional ephemeral tests may accompany pattern descriptions; authors do not need to add tests for ordinary edits.
- do not run `init generate` in notes; build workflows rebuild flashcard state automatically and agents must never invoke it.

## index files

- filename `index.md` with top header `# index`
- include a `children:` list with child pages in teaching order
- add a `grading:` section, optionally with a `scheme:` listing assignments/exams and weights
- in child lists, if linking into another note, include full anchor URLs (`topic.md#subsection`) so readers jump directly

## weekly/session entries

- use headings `## week N lecture` or `lab` or `tutorial`; sessions ordered strictly by the `datetime:` ISO interval field.
- lectures, labs and tutorials may interleave; multiple same-type sessions in one week get numbers only if more than one actually occur.
- ask users for their specific section codes (LA3, T2, etc) when the syllabus lists many; only generate entries for codes the user attends.
- duplicate week numbers around holidays require manual renumbering plus a `status: public holiday` entry; validator warns on duplicates.
- entries with `status: unscheduled` must omit the `topic:` field.
- always include an ISO date interval even if start or end is missing; use full ISO intervals for audit/clash detection.
- examinations are grouped after all regular sessions regardless of datetime; order exams chronologically within that block.

session metadata:

- `datetime:` ISO_START/ISO_END[, DURATION]
- `topic:` short text (omit if `status: unscheduled`)
- optional `status:` and `venue:`
- venue shorthand like `2133&2134` means “Room 2133 & 2134, Academic Building”; keep them consistent for schedule parsing.

- bullets nested under a session hold course-specific notes and cross-links.
- to record a user’s personal stream use a nested `sections:` list in the logistics block; the outer list groups by type and each inner item pairs a section identifier with venue and comma-separated weekday/time patterns. This replaces the old `session_times:` block.

## inline conventions

- **every markdown section in a topic note must have at least one flashcard.** add a horizontal rule `---` immediately before the first flashcard. the validator flags missing separators or missing cards. index files are exempt from this rule.
- do not merge cards from different sections; each heading has its own block directly beneath the prose.
- units must appear inside math delimiters (`$5\text{ V}$`); numbers followed by V A Ω W mW kΩ C Hz outside math trigger warnings.
- remove next-lecture comments unless they describe a grading event.
- inline glosses use `::@::` with the left side a full hierarchical path (course name plus intermediate folders) separated by ` / ` and the right side a single line of text; use `<br/>` for line breaks, never sublists.
- two-sided QA lists start with `---`, a blank line, the sentence `Flashcards for this section are as follows:` and bullets using `Q ::@:: A` or `Q :@:`. this format is recognised by the skill.
- emphasis italics `_like this_` bold `__like this__` to avoid conflicts with tables and cloze markers.
- math always uses `$…$` or `$$…$$`; avoid TeX `\(\)`/`\[\]` and Unicode symbols outside math.
- taxonomy entries use `- Section / subsection ::@:: summary`.
- outlines: each top-level item on its own source line; use `<br/>` for hard breaks and `<p>` for paragraphs.
- descriptive paragraphs follow outlines separated by `---`; no generic “lecture summary” sections unless they contain grading info.
- do not include personal contact details; use generic roles only.
- when memorizing a list of features collapse into a single gloss with hyphen separators and `<br/>` breaks.
- analogies and instructor caveats should be captured in the prose block and turned into glosses when appropriate.
- rewrite slide fragments into full sentences before adding cards.

## content capture rules

- aim for slide-level detail; every bullet or example from materials should appear in text.
- slides with multiple characteristics become separate outline items.
- worked examples are preserved verbatim; multi-step examples use numbered lists or multiple bullets.
- definitions and formulas are recorded fully; gloss right-hand sides may include parameters and units. cross-link to `general/` pages and include the path in the gloss.
- capture instructor asides, caveats and pitfalls as detail.
- quotes should be short; long proofs or policies are summarised and linked elsewhere.
- apply the same level of detail to lectures, labs, tutorials and review sessions so notes are self-contained.
- prefer `topic:` and a short `takeaway:` in session entries.
- include at least one worked example per concept and sample exam-style problems linked to `questions/solutions.md`.
- add references and resources at the end of the session.

## field expectations

- `datetime:` uses ISO interval with optional duration.
- `topic:` is a short summary.
- `attachments:` is a list or folder path relative to the note.
- `::@::` glosses are inline, short definitions for flashcards.

## cross-references

- link to existing `general/` articles using percent-encoded filenames.
- choose authoritative wikipedia titles; agents may use `find_wikipedia.py` to search.
- never create or edit `general/` files; link to the expected path.
- for a concept that deserves its own note create a new file in the course folder using the Wikipedia title as filename, lowercase first letter unless proper nouns require caps. heading inside the note matches filename lowercasing. write in neutral voice, add the new file to the index and link from sessions; topic notes may link back to `general/`.
- avoid hard line breaks in new topic notes; rely on soft wrap.
- split paragraphs only when the subject changes; each should be self-contained.
- LaTeX must appear on a single source line; block equations live in the same paragraph that introduces them.

## usage patterns agents should notice

- `::@::` is the common gloss separator.
- avoid extra indentation below `- topic:`; parsers expect two spaces per indent.
- bibliographic references on gloss RHS use dash lists with `<br/>`.
- hierarchies can span many levels; group related cards under intermediate folders as needed.
- arrows and chain notation in glosses may appear; preserve them.
- single-line `takeaway ::@:: …` entries often convert to `takeaway:` metadata.
- ask users early for their lab/tutorial section codes and filter schedules.
- multiple lectures per week require separate numbered headings ordered by datetime.
- HTML comments like `<!-- future term sections ... -->` may be present in long indexes; leave them intact.
- inline tokens such as `{@{…}@}` are used for emphasis; keep them.
- when auditing flashcards read the file sequentially to catch hidden errors.

## normalization tips

- keep `::@::` use but normalize session metadata: convert inline `topic ::@::` to `- topic:` and add `datetime:` when known.
- merge long enumerations into categorized glosses.
- avoid copying topic note material into the index; link instead.
- preserve existing flashcard tags; report missing tags rather than mass editing.
- when linking to `general/` use percent encoding; do not add new `general/` files in the same PR.

## validator warnings

- missing/malformed frontmatter tags.
- index.md without `# index` or `children:` list.
- session entries missing `datetime:` or (in content mode) `topic:`.
- exams before other sessions, duplicate week numbers, unscheduled sessions with a `topic:` field.
- semester headings out of order in institution indexes.

## formatting gotchas

- HTML fragments (`<p>`, `<br/>`) are normal inside outline items; keep each list item on one source line.
- prefer the single-index file structure; do not split lectures into separate files unless absolutely necessary.
