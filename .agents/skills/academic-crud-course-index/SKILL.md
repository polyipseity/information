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

## Course-root layout rules

- After course list (`institution`, `name`, `credits`), insert `---` before description
- Put `## children` first, then `## logistics`, then `## overview`
- Children order: AGENTS → assignments → questions → topics (chronological)
- Session headings: `## week N lecture`, `## week N tutorial`, `## week N lab`
- Session metadata: `datetime:`, `topic:`, `status:`, `assignment:`
- Gap sessions: `status: no class` or `status: public holiday: <name>`
- Exam sessions: continuous week heading, `status: unscheduled; <exam name>`

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

### Exam section format

Create a `## <exam name>` section elsewhere in the index (typically after all regular sessions):

```markdown
## midterm examination

- datetime: 2026-04-15T09:00:00+08:00/2026-04-15T11:00:00+08:00
- venue: Hall A
- scope: topic 1, topic 2, topic 3
- format:
  - calculator: yes
  - cheatsheet: yes (one A4 page)
  - referencing: closed book, closed notes
  - provided: \[missing\]
  - questions: long questions ×5
- note: \[missing\]
- grade:
  - 89/100
  - letter grade: A+
  - statistics:
    - L1:
      - timestamp: 2026-04-20T10:00:00+08:00
      - count: 120
      - mean: 72.5
      - standard deviation: \[missing\]
      - low: 35
      - lower quartile: 62
      - median: 74
      - upper quartile: 83
      - high: 98
      - distribution: \[missing\]
      - data: \[missing\]
- report:
  - - (topic name) (–1): <error description with flashcard>
  - - (topic name) (+1.5): <surprise with flashcard>
- check:
  - datetime: 2026-04-22T14:00:00+08:00
  - venue: Office
  - report: \[missing\]
```

### Aftermath section

After all exam sections:

```markdown
## aftermath

### total

- grade: 89.15/100
- letter grade: A+
- statistics:
  - L1:
    - timestamp: \[missing\]
    - count: 120
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

Official Canvas announcements as blockquotes after `---`:

```markdown
---

> <announcement text with original formatting preserved>
```

## Grade extraction patterns

- Canvas single-student view: mean, median, high, low, quartiles
- `statistics.timestamp` from Canvas announcement posting datetime
- `statistics.data: \[missing\]` (no external LMS links)
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

Use `\[missing\]` when a field or value is absent. See [special.instructions.md](../../instructions/special.instructions.md#missing-data).

## References

- `academic-crud-course-index/course-template.md` scaffold template
- `academic-lint` validation
- `academic-crud-index` subdirectory index format
- `academic-crud-attachments` attachments directories at any level
- `academic-crud-transcludes` Wikipedia articles included by reference
- `create-flashcards` exam error report flashcards
