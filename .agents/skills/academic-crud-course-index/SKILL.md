---
name: academic-crud-course-index
description: Create, read, update, and delete the top-level course index.md (children, logistics, overview, exam records, grades, stats) and course scaffolding under special/academia/<INSTITUTION>/<COURSE>/.
---

# Academic CRUD: Course index

Create, read, update, and delete the top-level course `index.md` and course scaffolding. This skill owns the course root, including exam records, which live inline in the top-level index.

## Target

`special/academia/<INSTITUTION>/<COURSE>/index.md`

## CRUD operations

### Create

Scaffold a new course from `.agents/skills/academic-crud-course-index/course-template.md`.

1. Verify no `index.md` already exists in the course root.
2. Create the directory `special/academia/<INSTITUTION>/<COURSE>/`.
3. Write `index.md`:

```markdown
---
aliases:
  - <INSTITUTION> <COURSE>
  - <INSTITUTION><COURSE>
tags:
  - flashcard/active/special/academia/<INSTITUTION>/<COURSE>
  - function/index
  - language/in/English
---

# <COURSE NAME>

- <INSTITUTION>
- <COURSE>
- <CREDITS>

---

<Course description>

## children

- [assignments/](assignments/index.md)
- [questions/](questions/index.md)
- [AGENTS](AGENTS.md)
- [<topic 1>](<topic%201>.md)
- ...

## logistics

- grading: <grading scheme>
- sections:
  - L1:
    - instructor: <name>
    - ...

## overview

<scope, topic-to-file mapping, orientation material>
```

After scaffolding, create subdirectories as needed:

| Directory | Created when |
| --- | --- |
| `assignments/` | Course has unbound submissions (PS, HW, projects) |
| `questions/` | Course has question sets (iPRs, in-class, practice) |
| `labs/` | Labs require submission |
| `tutorials/` | Tutorials require submission |
| `lectures/` | Lecture-bound submissions exist |

Each subdirectory gets an `index.md` via `academic-crud-index`.

### Read

Show course structure, child count, session list, and exam records.

### Update

Modify children ordering, logistics, session metadata, and overview. Add or update exam sections inline.

### Delete

Remove the entire course directory (with confirmation) and its entry in the institution `index.md`.

## Scope: course index only

Populate only the sections the source provides. A generic course homepage typically supplies description, prerequisites, textbook, grading scheme, section schedules, and announcements; it does not supply week-by-week session content, assignment details, or child file scaffolding. Do not create subdirectories (`labs/`, `assignments/`, `tutorials/`) or session entries (`## week N lecture 1`) from a homepage alone; those require per-item source material (Canvas pages, PRS quizzes, assignment PDFs).

## Keep the index minimal

Prefer less content. Record what the source states and what sessions covered, nothing else.

- __Never write current status or progress__: what has been ingested, what is still missing, or what a section will contain later. It is stale as soon as the next source arrives.
- __Never write provenance__: how a date, figure, or number was established is not index content.
- __Never record platform links__: Canvas or other LMS course URLs are not course facts and go stale.
- The `- note:` lines under `## logistics` and the `- notes` list under `## overview` carry source facts and caveats only: a conflicting source, a tentative schedule, a policy.
- A value that exists but is unknown is marked `\[missing\]`, never described in prose. See [Missing data](#missing-data).

## Session types: lecture, lab, tutorial

Lectures, labs, and tutorials are distinct session types under `## logistics`, each with its own section keys, schedule, and session headings. Never merge them into a single type.

```yaml
- sections:
    - lecture                    # ← section type: lecture
        - L1: venue; time       # ← section key: L1, L2, L3
        - L2: venue; time
    - tutorials                  # ← section type: tutorials (plural)
        - T1: venue; time       # ← section key: T1, T2, T3
        - T2: venue; time
    - labs                       # ← section type: labs (plural)
        - LA1: venue; time      # ← section key: LA1, LA2, LA3
        - LA2: venue; time
```

- Section-type names match `course-template.md`: `lecture` (singular), `tutorials` and `labs` (plural). The chosen section is written after the colon, e.g. `- labs: LA3`.
- Section keys: `L` for lectures, `T` for tutorials, `LA` for labs.
- Session headings use the singular type and always carry the session's ordinal in the week: `## week N lecture 1`, `## week N tutorial 1`, `## week N lab 1`. A recurrent course adds one level and repeats the semester, `### <YYYY term> week N tutorial 1` (see "Recurring courses").

## Session ordering: types repeat every week

Each session type occurs on a fixed weekly pattern: with 3 lectures per week, every week gets `## week N lecture 1`, `## week N lecture 2`, and `## week N lecture 3`, and 1 lab per week gives every week a `## week N lab 1`. The same holds for tutorials.

__Rules:__

1. _Consistent types across weeks._ If week 1 has 2 lectures + 1 lab + 1 tutorial, every later week has the same set (unless marked `status: no class`).
2. _An ordinal on every session._ With N sessions of one type in a week, use `## week N lecture 1`, `## week N lecture 2`, ..., `## week N lecture N`. The first session of a week carries `1`; it is never left unnumbered.
3. _Strictly increasing `datetime:` in file order._ Read top to bottom, each session heading's `datetime:` must be later than the previous one; the `session_datetime_order` rule enforces this. Within a week that means day/time order, so the earliest session comes first regardless of type.
4. _Strict chronological order across weeks._ Week 2 sessions come after week 1 sessions. Never interleave weeks; `## week 1 lecture 1` → `## week 2 lecture 1` → `## week 3 lab 1` is wrong if week 1 also has a lab.
5. _Gap sessions._ If a type does not meet in a week, mark it `status: no class` or `status: public holiday: <name>` instead of omitting the heading.

__Example for a course with 2 lectures + 1 lab per week:__

```markdown
## week 1 lecture 1
- datetime: ...
## week 1 lecture 2
- datetime: ...
## week 1 lab 1
- datetime: ...
## week 2 lecture 1
- datetime: ...
## week 2 lecture 2
- datetime: ...
## week 2 lab 1
- datetime: ...
```

__Wrong:__

```markdown
## week 1 lecture 1
## week 2 lecture 1
## week 3 lab 1    ← week 1's lab is missing, types are mixed across weeks
```

## Recurring courses

A recurrent course runs every term instead of once. It carries `- status: recurrent` in the course header block, groups its sessions by semester, and puts each session heading one level deeper.

```markdown
## 2025 fall

### 2025 fall week 3 tutorial 1

- datetime: 2025-09-17T18:00:00+08:00/2025-09-17T18:50:00+08:00, PT50M
- venue: \[missing\]
- topic: Sun Hung Kai Properties (SHKP)
- status: optional

## 2026 fall

### 2026 fall week 1 tutorial 1

- datetime: 2026-09-02T18:00:00+08:00/2026-09-02T21:00:00+08:00, PT3H
- venue: LTA
- topic: CSE program orientation talk and dinner
- status: optional
```

- __Semester header__: `## <YYYY term>`, using the institution `index.md` term spelling (`## 2026 fall`), placed after `## overview` and in chronological order.
- __Session heading__: `### <YYYY term> week N <type> <number>` — one level deeper than a one-off course, with the semester repeated and the session's ordinal in the week.
- __The repeat is required.__ Without it the same week/type pair recurs in every semester and `markdownlint` MD024 rejects the duplicate headings; `.markdownlint*` is never edited and `index.md` admits no disable directive, so the heading text itself has to differ.
- __Week numbers__ count from the term's first teaching week, so week 1 begins on that term's week-1 Monday.
- __Every session is optional.__ A recurrent course's lectures, labs, and tutorials all carry `- status: optional`, and none is assumed to be attended. Keep `datetime:`, `venue:`, and `topic:`, because the term's schedule is still what the entry records.
- __A session entry normally carries no note or section links__, since an unattended session covered nothing. Add them only for a session that was actually attended and written up.
- __Only attested sessions.__ Record the sessions a source names. Never invent `status: no class` or `status: unscheduled` weeks to complete a weekly pattern for a past term whose full schedule is unknown.
- __The linter enforces the shape.__ `academic-lint` reads `- status: recurrent` from the identity block, then requires the level-3 semester-carrying headings (`session_heading_format`), a matching `## <YYYY term>` header above each session (`session_semester_match`), `status: optional` or a gap marker on each session (`session_optional_status`), chronological semester headers (`index_semester_order`), and week counting that restarts each term (`week_monotonic`, `session_duplicate_heading`).
- Everything else in "Session ordering" applies unchanged: `datetime:` strictly increasing in file order (which keeps the semesters chronological), one heading per meeting, an ordinal on every session inside a week, and `lecture`/`lab`/`tutorial` as the only types. A seminar series or training stream is recorded under whichever of those three it matches, never as a fourth type.

## Session outline content: sections, not files

A session entry records what the session taught. After the metadata, list each note the session created or expanded, then the note sections its material covers:

```markdown
## week 1 lecture 1

- datetime: 2026-09-01T09:00:00+08:00/2026-09-01T10:20:00+08:00
- venue: Rm 4619, Lift 31-32
- topic: basic operating system concepts; computer-system organization
- [operating system](operating%20system.md)
    - [§ what an operating system does](operating%20system.md#what%20an%20operating%20system%20does)
    - [§ kernel and system programs](operating%20system.md#kernel%20and%20system%20programs)
        - [§ microkernel and monolithic kernel](operating%20system.md#microkernel%20and%20monolithic%20kernel)
- [memory hierarchy](memory%20hierarchy.md)
    - [§ hierarchy of storage](memory%20hierarchy.md#hierarchy%20of%20storage)
```

- __A file link alone is never enough.__ Link the sections too.
- __List only the sections the session's material created or expanded.__ A note spanning several sessions is linked under each of them, and each entry lists only its own sections.
- __Link the deepest heading the session's material created or expanded.__ A `###` the session created nests one level (8 spaces) under its `##` bullet; link the `##` alone only when the session created the whole section.
- __Anchor format__: the heading lowercased, spaces as `%20`, colons removed (`## Main memory` → `#main%20memory`). Never dash-slugs (`#main-memory`); the `link_anchor_slug` rule rejects them.
- __A re-levelled section must be re-linked in the same task.__ When the section levelling pass renames, moves, or folds a heading, every session entry and appendix link pointing at its old anchor is updated with it; a stale anchor is a broken link, not a cosmetic one (see "Section levelling pass" in `academic-crud-topic-note`).
- __Filename format__: spaces as `%20`, every other character literal (`cache%20(computing).md`).
- Omit the section links only when the note has no `##` sections.

## Course-root layout rules

- After the course list (`institution`, `name`, `credits`), insert `---` before the description.
- Order: `## children`, then `## logistics`, then `## overview`.
- The `## overview` topic-to-file mapping maps concepts to notes, not source units or source order.
- Children order: folders first, then files, Python string order within each group (see "Children format" in `academic-crud-index`).
- Session headings: each type repeats every week (see "Session ordering" above), or every week of a semester in a recurrent course (see "Recurring courses").
- Session body: list the note sections the session's material created or expanded.
- Session metadata: `datetime:`, `topic:`, `status:`, `assignment:`, `quiz:`.
    - `quiz:` links to the tutorial quiz page when a quiz was administered: `[tutorial <N>](tutorials/tutorial%20<N>/index.md)`, with the grade appended if known (`(grade: 2/2)`).
    - Assignment links go in the last lecture entry on or before the due date, as an `ELEC 1100` child (e.g. `- ELEC 1100 / [assignment name](assignments/<name>/index.md)`).
- Gap sessions: `status: no class` or `status: public holiday: <name>`.
- Optional sessions: `status: optional`, used by every session of a recurrent course (see "Recurring courses").
- Exam sessions: continuous week heading, `status: unscheduled; <exam name>`.
- Session free text: optional content after the `---` separator following the metadata, used for verbatim Canvas announcements as blockquotes (see "Announcement preservation").

## Exam handling

Exams live in the top-level `index.md`, not in separate files.

### Session marking

When a regular slot is used for an exam:

```markdown
## week N lecture 1

- datetime: 2026-04-15T09:00:00+08:00/2026-04-15T11:00:00+08:00
- venue: Hall A
- status: unscheduled; midterm examination
- [§ midterm examination](#midterm%20examination)
```

Keep the week heading continuous, set `status: unscheduled; <exam name>`, and add a `§` link to the exam section.

### Exam section link in session outline

When a major exam (lab, midterm, or final examination) takes place during a regular lecture, lab, or tutorial, add a section link in that session's outline pointing to the dedicated exam section, using the same format as other course links:

```markdown
## week 9 lab 1

- datetime: 2026-03-30T10:30:00+08:00/2026-03-30T13:20:00+08:00, PT2H50M
- venue: Room 2133 & 2134, Academic Building
- topic: lab exam
- ELEC 1100 / [lab examination](#lab%20examination)
```

The session outline then points to the dedicated section holding the full details (statistics, announcements, breakdown). The link text matches the section heading; the anchor is the heading lowercased with `%20` for spaces and colons removed.

### Exam section format

Create a `## <exam name>` section elsewhere in the index, typically after all regular sessions. Field order:

```markdown
## midterm examination

- datetime: 2026-04-15T09:00:00+08:00/2026-04-15T11:00:00+08:00
- venue: Hall A
- scope: all prior content  # default if not specified; replace with actual scope when found in Canvas announcements/pages
- format:
    - calculator: yes
    - cheatsheet: yes (one A4 page)
    - open book: no
    - open notes: no
    - questions: long questions ×5  # or: (item 1) ×(count), (item 2) ×(count), ...
- grade: 89/100  # or updated: "24/25 → 25/25" (synchronized with topmost statistics session)
- statistics:
    - L1:
        - timestamp: 2026-04-20T10:00:00+08:00
        - count: 120  # total students who took the exam
        - mean: 72.5
        - standard deviation: \(none\)
        - low: 35
        - lower quartile: 62
        - median: 74
        - upper quartile: 83
        - high: 98
        - distribution: \(none\)
        - data: \(none\)
        - note: 16 students achieved the maximum score of 20
- breakdown: questions ×4  # or: (item 1) ×(count), (item 2) ×(count), ...
- note: \(none\)
- report:
    - \(none\)
```

#### Statistics rules

- __Session key__: use the section code (`L1:`, `LA3:`, `T2:`), one key per section that took the exam.
- __Canvas grades page stats__: write values directly, without a label. The grades page is the page showing the student's grades across a course.
- __Other source stats__: wrap in parentheses with a label, e.g. `- count: (provided: 16)`. This applies to stats from announcements, discussion topics, or any page other than the grades page; the timestamp is the only exception and is always written directly.
- __Unknown values__: use `\(none\)` (escaped for markdown), never `?`.
- __Statistics note__: the `note:` field inside a session key holds extra source data that does not fit the standard fields (e.g. how many students achieved the maximum score).
- __Updated stats__: use `→` to show the update, applying evenly across all fields including timestamp, with a value on both sides:

  ```yaml
  - statistics:
      - L1:
          - timestamp: 2026-05-21T11:02:00+08:00 → 2026-05-22T16:09:00+08:00
          - count: \(none\) → \(none\)
          - high: (provided: 25) → (provided: 25)
          - mean: (provided: 19.02) → (provided: 19.61)
          - standard deviation: (provided: 4.59) → (provided: 4.72)
          - low: \(none\) → \(none\)
          - lower quartile: \(none\) → \(none\)
          - median: \(none\) → \(none\)
          - upper quartile: \(none\) → \(none\)
          - distribution: \(none\) → \(none\)
          - data: \(none\) → \(none\)
          - note: 30 students achieved the maximum score of 25 (updated from 7 after re-mark)
  ```

  An unchanged value shows as `old → old`, and a `(provided: ...)` label appears on both sides when present.

### Aftermath section

After all exam sections:

```markdown
## aftermath

### total

- grade: 89.15/100
    - letter grade: A+
- statistics:
    - L1:
        - timestamp: \(none\)
        - count: 120  # total students who took the exam
        - mean: 75.2
        ...
```

### Appendix section

An optional section after sessions and exams, before `## aftermath`, holding supplementary topic links that are not in the main `## children` list:

```markdown
## appendix

- [topic name](topic%20name.md)
    - [§ section heading](topic%20name.md#section%20heading)
```

Use `## appendix` for Wikipedia transcludes (see `academic-crud-transcludes`), supplementary reference material, and topics that do not fit the main session flow. Not every course has one; add it only when supplementary content warrants separation from `## children`.

### Announcement preservation

Canvas announcements (discussion/topic pages) are placed as blockquotes in the session entry matching the related assignment or activity, after a `---` separator following the session metadata. An announcement about an assignment goes in the same lecture entry where the assignment link appears (the last lecture on or before the due date); one about a lab or tutorial activity goes in that session's entry.

Add an announcement when a Canvas HTML source is a discussion/topic page (title starting with "Topic:", or page type discussion): extract the title and body and place them in the chronologically matching session entry.

Format each announcement as a blockquote with the title bolded, preserving the original wording, paragraph structure, and inline formatting. Drop the platform chrome: the author/teacher metadata line, the posting timestamp, "This topic is closed for comments", and navigation elements.

- __Names inside the body__: an instructor or TA name the quoted body itself carries, in a greeting or a signature, is redacted as `\[redacted\]`. The body is preserved verbatim, so the name leaves a visible mark where it stood. A name outside a quoted announcement is simply omitted.
- __Paragraphs__: each logical paragraph becomes a separate `>` line group separated by `>` blank lines.
- __Non-paragraph line breaks__: use `<br/>` for line breaks within a paragraph (list items in one visual block, forced breaks in the original HTML). Do not collapse multiple lines into one.
- __Inline formatting__: preserve bold (`__bold__`), italics (`_italic_`), code (`` `code` ``), underline (`<u>text</u>`), and emphasis. Map HTML `<b>`/`<strong>` to `__`, `<i>`/`<em>` to `_`, `<code>` to backticks, and `<u>` to `<u>` tags.
- __Lists__: preserve list items with a `-` prefix, indenting nested items by 2 extra spaces.
- __Separators__: horizontal rules (`---` or `***`) from the original may be omitted or replaced with a blank `>` line.

```markdown
## week N lecture 1

- datetime: ...
- venue: ...
- status: no class

---

> __Announcement Title__
>
> Dear __ELEC1100 (L1)__ students,
>
> You can now check your __Exam Name__ results on the Canvas __ELEC1100 (L1) “Grades”__ page.
>
> Here are the details for your information:
>
> __Exam Name (Full Mark: N)__
>
> - Maximum Score: X (Y)
> - Mean: Z
> - Standard Deviation (SD): W
>
> Please note that __taking photos is NOT allowed__ during the paper review session.
>
> Regards,
>
> \[redacted\]
```

The number in parentheses after Maximum Score (`Maximum Score: 20 (66)`) is the count of students who reached that score, not the total number of students.

When several announcements target the same session, list them as separate blockquotes separated by a blank line. Match each announcement to the session where the related content lives: assignment-related ones to the lecture entry that links the assignment, activity-related ones to that activity's session entry.

## Grade extraction patterns

- Canvas single-student view: mean, median, high, low, quartiles
- `statistics.timestamp` from the Canvas announcement posting datetime
- `statistics.data: \(none\)` (no external LMS links)
- Per-question breakdown from a PDF: run `convert_document` first (see "Document extraction (mandatory)" in `academic-ingest`), then read the per-question marks from `text.md` or the page renders
- Grades notation: `X/N`, or `base+bonus/max+max bonus` when bonus marks are documented

## Validation

Run the humanizer pass over new or changed prose and flashcards, focusing on the course description, `## overview` bullets, and session `topic:` lines (see "Humanizer pass" in `academic-ingest`). Then run `academic-lint`, passing the changed files when known.

## Missing data

__Always use `\[missing\]`.__ Every field that exists but has no value gets `\[missing\]`. Never invent placeholder text ("TBA", "upcoming", "none", "?"). The one exception is exam statistics fields, which use `\(none\)`; that format belongs to the statistics sub-block alone.

Example for an exam section whose details are not yet known:

```yaml
## midterm examination

- datetime: 2026-10-29T19:00:00+08:00/2026-10-29T21:00:00+08:00
- venue: \[missing\]
- scope: \[missing\]
- format:
    - calculator: \[missing\]
    - cheatsheet: \[missing\]
    - open book: \[missing\]
    - open notes: \[missing\]
    - questions: \[missing\]
- grade: \[missing\]
- statistics: \[missing\]
- breakdown: \[missing\]
- note: \[missing\]
- report: \[missing\]
```

See [special.instructions.md](../../instructions/special.instructions.md#missing-data) for the full convention.

## References

- `academic-crud-course-index/course-template.md` scaffold template
- `humanizer` for the AI-writing patterns it removes (see "Humanizer pass" in `academic-ingest`)
- `academic-lint` validation
- `academic-crud-index` subdirectory index format
- `academic-crud-attachments` attachment directories
- `academic-crud-transcludes` Wikipedia article inclusion
- `create-flashcards` exam flashcards
