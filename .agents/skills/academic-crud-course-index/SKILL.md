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

Scaffold a new course from the template at `.agents/skills/academic-crud-course-index/course-template.md`.

1. Verify no `index.md` already exists in the course root.
2. Create directory: `special/academia/<INSTITUTION>/<COURSE>/`
3. Write `index.md` with:

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

- [AGENTS](AGENTS.md)
- [assignments](assignments/index.md)
- [questions](questions/index.md)
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

1. Create subdirectories as needed:

| Directory | Created when |
| --- | --- |
| `assignments/` | Course has unbound submissions (PS, HW, projects) |
| `questions/` | Course has question sets (iPRs, in-class, practice) |
| `labs/` | Labs require submission |
| `tutorials/` | Tutorials require submission |
| `lectures/` | Lecture-bound submissions exist |

Each subdirectory gets an `index.md` via `academic-crud-index`.

### Read

Show course structure, child count, session list, exam records.

### Update

Modify children ordering, logistics, session metadata, overview. Add/update exam sections inline.

### Delete

Remove entire course directory (with confirmation). Remove from institution `index.md`.

## Scope: course index only

When creating from a course homepage or syllabus, only populate sections that the source material actually provides. A generic course homepage typically provides: description, prerequisites, textbook, grading scheme, section schedules (lectures and labs), and possibly announcements. It does NOT provide week-by-week session content, individual assignment details, or child file scaffolding.

Do NOT create subdirectories (`labs/`, `assignments/`, `tutorials/`) or session entries (`## week N lecture`) from a course homepage alone. These require specific per-item source material (Canvas pages, PRS quizzes, assignment PDFs).

## Session types: lecture, lab, tutorial

Lectures, labs, and tutorials are distinct session types under `## logistics`. Each type has its own section keys, schedule, and session headings. Never merge them into a single type.

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

- Section-type names match `course-template.md`: `lecture` (singular), `tutorials` and `labs` (plural); the chosen section is written after the colon, e.g. `- labs: LA3`
- Section keys follow the convention: `L` for lectures, `T` for tutorials, `LA` for labs
- Session headings use the singular type: `## week N lecture`, `## week N tutorial`, `## week N lab`

## Session ordering: types repeat every week

Each session type occurs on a fixed weekly pattern. If a course has 3 lectures per week, EVERY week gets `## week N lecture`, `## week N lecture 2`, `## week N lecture 3`. If it has 1 lab per week, EVERY week gets `## week N lab`. The same applies to tutorials.

__Rules:__

1. _Consistent types across weeks._ If week 1 has 2 lectures + 1 lab + 1 tutorial, every subsequent week has the same set of session types (unless marked `status: no class`).
2. _Numbered suffixes for multiple sessions of the same type._ When there are N sessions of the same type in a week, use `## week N lecture`, `## week N lecture 2`, ..., `## week N lecture N`.
3. _Chronological order within each week._ Within a single week, list sessions in day/time order: lecture first (earliest), then tutorial, then lab (or whatever the actual chronological order is).
4. _Strict chronological order across weeks._ Week 2 sessions come after week 1 sessions. Never interleave weeks (e.g., `## week 1 lecture` → `## week 2 lecture` → `## week 3 lab` is WRONG if week 1 also has a lab).
5. _Gap sessions._ If a session type does not meet in a particular week, mark it with `status: no class` or `status: public holiday: <name>` rather than omitting the heading.

__Example for a course with 2 lectures + 1 lab per week:__

```markdown
## week 1 lecture
- datetime: ...
## week 1 lecture 2
- datetime: ...
## week 1 lab
- datetime: ...
## week 2 lecture
- datetime: ...
## week 2 lecture 2
- datetime: ...
## week 2 lab
- datetime: ...
```

__Wrong — do NOT do this:__

```markdown
## week 1 lecture
## week 2 lecture
## week 3 lab    ← week 1's lab is missing, types are mixed across weeks
```

## Course-root layout rules

- After course list (`institution`, `name`, `credits`), insert `---` before description
- Put `## children` first, then `## logistics`, then `## overview`
- Children order: AGENTS → assignments → questions → topics (chronological)
- Session headings: see "Session ordering" above — each type repeats every week
- Session metadata: `datetime:`, `topic:`, `status:`, `assignment:`, `quiz:`
    - `quiz:` links to the tutorial quiz page when a quiz was administered:
      `[tutorial <N>](tutorials/tutorial%20<N>/index.md)`
      Append grade if known: `(grade: 2/2)`
    - Assignment links: in the last lecture entry on or before the assignment due date, add the assignment as an `ELEC 1100` child (e.g. `- ELEC 1100 / [assignment name](assignments/<name>/index.md)`)
- Gap sessions: `status: no class` or `status: public holiday: <name>`
- Exam sessions: continuous week heading, `status: unscheduled; <exam name>`
- Session free text: optional content after the `---` separator following session metadata; used for verbatim Canvas announcements as blockquotes (see "Announcement preservation")

## Exam handling

Exams live in the top-level `index.md`, not in separate files.

### Session marking

When a regular slot is used for an exam:

```markdown
## week N lecture

- datetime: 2026-04-15T09:00:00+08:00/2026-04-15T11:00:00+08:00
- venue: Hall A
- status: unscheduled; midterm examination
- [§ midterm examination](#midterm%20examination)
```

Keep the week heading continuous. Set `status: unscheduled; <exam name>`. Add `§` link to the exam section.

### Exam section link in session outline

When a major exam (lab examination, midterm examination, final examination) takes place during a regular lecture, lab, or tutorial session, add a section link in that session's outline pointing to the dedicated exam section. Use the same format as other course links:

```markdown
## week 9 lab 1

- datetime: 2026-03-30T10:30:00+08:00/2026-03-30T13:20:00+08:00, PT2H50M
- venue: Room 2133 & 2134, Academic Building
- topic: lab exam
- ELEC 1100 / [lab examination](#lab%20examination)
```

This ensures the session outline links to the dedicated section where full details (statistics, announcements, breakdown) are recorded. The link text matches the section heading; the anchor uses lowercase with hyphens.

### Exam section format

Create a `## <exam name>` section elsewhere in the index (typically after all regular sessions). Field order:

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

- __Session key__: Use the section code as the key (e.g. `L1:`, `LA3:`, `T2:`). One key per section that took the exam.
- __Canvas grades page stats__: Write values directly (no label). The grades page is the page showing the student's all grades in a course.
- __Other source stats__: Wrap in parentheses with label: `- count: (provided: 16)`. Applies to stats from announcements, discussion topics, or any page other than the grades page. __Timestamp is the only exception__ — always written directly.
- __Unknown values__: Use `\(none\)` (escaped for markdown). Never use `?`.
- __Statistics note__: Use the `note:` field inside the session key for extra data from the source that doesn't fit the standardized fields (e.g. count of students who achieved the maximum score).
- __Updated stats__: Use `→` to show the update, applying evenly across all fields including timestamp. Every field must have a value on both sides of `→`:

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

  When a value is unchanged, show `old → old`. The `(provided: ...)` label must appear on both sides of `→` when present.

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

Optional section after sessions/exams, before `## aftermath`. Holds supplementary topic links not in the main `## children` section.

```markdown
## appendix

- [topic name](topic%20name.md)
    - topic name / [§ section heading](topic%20name.md#section%20heading)
```

Use `## appendix` for:

- Wikipedia transcludes (see `academic-crud-transcludes`)
- Supplementary reference material
- Topics that don't fit the main session flow

Not all courses use `## appendix`. Only add it when there is supplementary content that warrants separation from the main `## children` list.

### Announcement preservation

Official Canvas announcements (discussion/topic pages) are placed as blockquotes in the session entry that matches the related assignment or activity, after a `---` separator following the session metadata. When an announcement relates to an assignment, place it in the same lecture entry where the assignment link appears (the last lecture on or before the due date). When an announcement relates to a lab or tutorial activity, place it in that session's entry.

__When to add__: When a Canvas HTML source is a discussion/topic page (title starts with "Topic:" or page type is discussion), extract the title and body and place them in the chronologically matching session entry.

__Format__: Each announcement is a blockquote with the title bolded. Omit the author name and platform chrome ("This topic is closed for comments", navigation elements). Preserve the original wording, paragraph structure, and inline formatting of the body text.

- __Paragraphs__: Each logical paragraph from the original becomes a separate `>` line group separated by `>` blank lines.
- __Non-paragraph line breaks__: Use `<br/>` for line breaks within a paragraph (e.g. list items that are part of the same visual block, or forced breaks in the original HTML). Do NOT collapse multiple lines into one.
- __Inline formatting__: Preserve bold (`__bold__`), italics (`_italic_`), code (`` `code` ``), underline (`<u>text</u>`), and emphasis from the original HTML. Map HTML `<b>`/`<strong>` to `__`, `<i>`/`<em>` to `_`, `<code>` to backticks, `<u>` to `<u>` tags.
- __Lists__: Preserve list items with `-` prefix. Indent nested items with 2 extra spaces.
- __Separators__: Horizontal rules (`---` or `***`) from the original can be omitted or replaced with a blank `>` line.

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
```

__Maximum Score parentheses__: The number in parentheses after Maximum Score (e.g. `Maximum Score: 20 (66)`) is the count of students who achieved that maximum score, not the total number of students.

__Multiple announcements__: When several announcements target the same session, list them sequentially as separate blockquotes. Separate consecutive blockquotes with a blank line.

__Placement rule__: Match the announcement to the session where the related content lives. Assignment-related announcements go in the lecture entry that links the assignment (last lecture on or before due date). Activity-related announcements (labs, tutorials) go in the session entry for that activity. When multiple announcements target the same session, list them sequentially as separate blockquotes.

## Grade extraction patterns

- Canvas single-student view: mean, median, high, low, quartiles
- `statistics.timestamp` from Canvas announcement posting datetime
- `statistics.data: \(none\)` (no external LMS links)
- Per-question breakdown from PDF via PyMuPDF:

  ```python
  import fitz
  doc = fitz.open(path)
  for page in doc:
      text = page.get_text("text")
  ```

- Grades notation: `X/N` unless bonus marks documented, then `base+bonus/max+max bonus`

## Validation

Run `academic-lint` after every edit. If you know which files changed, pass those files specifically. Otherwise lint the whole course folder.

## Missing data

__Always use `\[missing\]`.__ Every field that exists but has no value gets `\[missing\]` as its value. Never invent placeholder text ("TBA", "upcoming", "none", "?"). The only exception is exam statistics fields, which use `\(none\)` — this format is specific to the statistics sub-block and must not be used elsewhere.

Example for an exam section where details are not yet known:

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
- `academic-lint` validation
- `academic-crud-index` subdirectory index format
- `academic-crud-attachments` attachments directories at any level
- `academic-crud-transcludes` Wikipedia articles included by reference
- `create-flashcards` exam error report flashcards
