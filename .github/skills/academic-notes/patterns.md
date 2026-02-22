# Academic notes — detailed patterns

This document collects observed patterns from academic course notes and the preferred conventions for authoring new content across institutions.

## Frontmatter

- Begin file with a YAML frontmatter block delimited by `---` lines.
- Recommended keys:
  - `aliases:` list with course code variants and human names.
  - `tags:` must include `flashcard/active/special/academia/<INSTITUTION>/<PAGE>` for flashcard activation. **This tag is required in all course note files under `special/academia` when flashcards are desired.** Also include `function/index` and `language/in/English` where appropriate.

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
- The new preferred way to record your own lecture/tutorial/lab streams is with a `sections:` list in the logistics block.  Each entry uses semicolons to separate the stream code, venue, and weekly day‑of‑week/time pattern (e.g. `L1; CYT‑LTL; MondayT16:00:00/MondayT16:50:00`).  This replaces the older `session_times:` block and keeps all metadata self‑contained.

## Inline conventions

- `::@::` is used to provide a concise definition or gloss for a linked term (e.g., `expression ::@:: It is a combination of symbols`).
- Use `- Section / subsection ::@:: summary` to create taxonomy-like entries.

## What content to capture (content-first guidance)

When creating or improving course notes, prioritize capturing content that helps learning and revision. For each lecture/tutorial/lab session prefer the following elements where appropriate:

- `learning_outcomes:` — 1–3 concise bullet points describing what students should know after the session.
- `topic:` and a short `takeaway:` line — scannable summary for revision.
- Instructor emphasis — note any points the instructor stressed.
- Key definitions & concise glosses — use `::@::` for flashcard-worthy bites; cross-link to canonical `general/` pages for full definitions.
- Worked examples & step-by-step solutions — include at least one worked example demonstrating common techniques or pitfalls.
- Sample exam-style questions / practice problems — add problems and link to solutions in `questions/solutions.md`.
- References & resources — slides, recordings, page numbers, and further reading links.

## Field types and expectations

- `datetime:` — ISO interval `YYYY-MM-DDThh:mm:ss+TZ/END` and optional ISO duration after a comma.
- `topic:` — short, plain-text summary.
- `learning_outcomes:` — YAML list of 1–3 outcomes.
- `takeaway:` — single-line concise takeaway.
- `attachments:` — list or folder; reference files using relative links.
- `::@::` concise glosses — inline, short definitions intended to be flashcard-friendly.

## Cross-references

- Prefer linking to `general/` canonical notes for repeated concepts (e.g., `../../../../general/functional%20programming.md`).
- When choosing which `general/` page to link, prefer authoritative article titles (Wikipedia or canonical sources). Agents should use the included helper `find_wikipedia.py` to search Wikipedia and select a candidate. Do NOT create, modify, or add files under `general/`; instead link to the expected `general/` path.

## Observed usage patterns

- `::@::` is heavily used as the inline gloss/flashcard separator.
- Taxonomy / chain notation: authors sometimes list chains of related concepts using arrows and `::@::` boundaries (seen in several course collections). Preserve these as-is when possible.
- Takeaway shorthand: many files use a single-line `takeaway ::@:: ...` — treat these as candidates for `takeaway:` in a normalization PR.
- Authors often capture their lab/tutorial section codes (e.g. LA3, T2) near the top of the note; agents should request this early and filter schedules accordingly to avoid clutter from irrelevant streams.
- Multiple lectures per week are common; capture each with a separate numbered heading and ensure the order follows the actual datetimes.
- HTML comments such as `<!-- future term sections ... -->` are sometimes inserted to simplify long-term editing of index files.
- Inline annotation tokens (e.g., `{@{...}@}`) are used for emphasis or examiner notes; preserve them unless a maintainer asks for normalization.

## Normalization recommendations

- Accept liberal use of `::@::` as a flashcard signal, but normalize session metadata when editing (convert inline `topic ::@::` to `- topic:` and add `datetime:` when available).
- Preserve existing `flashcard/active/...` tags; where missing, report files and propose adding the tag in a PR rather than mass-editing.
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

- HTML fragments (`<p>`, `<br/>`) are occasionally used for emphasis — prefer Markdown where possible.
