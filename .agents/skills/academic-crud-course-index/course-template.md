# Course note template (institution-agnostic)

Use this file as a scaffold for new course pages under
`special/academia/<INSTITUTION>/<COURSE CODE>/`. It carries the scaffold itself and
the reminders that change how you fill it in; each rule lives in the skill named
on its line.

## Quick reminders

- Keep the fenced `markdown` block machine-readable and put human guidance
  __outside__ it.
- __Scope__: scaffold only what the source material provides. A course homepage
  produces the course `index.md` with logistics and overview and nothing else;
  `labs/`, `assignments/`, `tutorials/`, and session entries each need their own
  per-item source (see "Scope: course index only" in `SKILL.md`).
- When the materials already enumerate repeating deliverables or sessions
  (tutorial rounds, lab rounds, quizzes, homeworks), scaffold minimal child pages
  for them early and keep them lightweight until official content arrives.
- __Missing data__: `\[missing\]` for an unknown value, never an invented
  placeholder such as "TBA", "none", or "?". Exam statistics sub-blocks are the
  one exception and use `\(none\)` (see
  [special.instructions.md](../../instructions/special.instructions.md#missing-data)).
- Frontmatter: aliases cover the spaced and unspaced course code plus
  institution-prefixed variants, sorted alphabetically, and flashcard tags use
  underscore-normalized path fragments such as
  `flashcard/active/special/academia/HKUST/COMP_3031` (see "Frontmatter rules"
  in `academic-crud-index`).
- Course-specific agent instructions go in `AGENTS.md` beside `index.md`, and
  only when the course needs them. If you do not create the file, drop it from
  `children` (see `academic-crud-agents`).
- Top-level sections run `## children`, `## logistics`, `## overview`, then
  sessions and exams, with `assignments/` immediately after `children` and
  before the session entries (see "Course-root layout rules" in `SKILL.md`).
- Prefer one `## overview` for compact orientation material: the official scope
  bullets, the topic-to-file mapping, and short root-level notes.
- Keep the pages lean. The course root holds only the high-value overview,
  folder indexes summarize just enough to navigate, and leaf indexes carry
  minimal logistics until real content is ingested (see "Keep the index minimal"
  in `SKILL.md`).
- Never record current status or progress, meaning what has been ingested and
  what still remains. Prefer less content.
- Name and bound every note by its concept rather than by the source unit, and
  name every section after its sub-concept. The merge, split, and nesting rules
  that decide both are in `academic-crud-topic-note`.
- Link each note a session covers with the sections that session's material
  created or expanded: `- [note](note.md)`, then an indented
  `- [§ heading](note.md#heading)`. A file link alone is never enough.
- Sessions run in strict chronological order, every type repeating each week with
  the same count, each session's ordinal counted within its own week rather than
  carried over from the week before, and types never mixed across weeks. A
  recurring weekly stream is scaffolded continuously, with `status:` metadata on
  the meetings it skips rather than an omitted week (see "Session ordering" in
  `SKILL.md`).
- A __recurrent course__ (`- status: recurrent`) groups its sessions under
  `## <YYYY term>` and adds a level, `### <YYYY term> week N tutorial 1`, with
  `- status: optional` on every session (see "Recurring courses" in `SKILL.md`).
- A leaf index for a Canvas-derived assignment follows `academic-crud-submission`,
  which owns the format down to the `## solution` list style and the rule for
  links into `private/`.
- A lab, tutorial, or lecture leaf index may list an in-class content file
  (`lab.md`, `tutorial.md`, `lecture.md`) as a child, and a Canvas-sourced one
  mirrors its `index.md`'s Canvas header block rather than staying a bare stub
  (see `academic-crud-submission`).

## template content

```markdown
<!-- Remove template comments before committing. -->
---
aliases:
  - <course code>
  - <coursecodewithoutspace>
  - <course code> index
  - <coursecodewithoutspace> index
  - <institution> <course code>
  - <institution> <coursecodewithoutspace>
  - <institution> <course code> index
  - <institution> <coursecodewithoutspace> index
tags:
  - flashcard/active/special/academia/<institution_slug>/<course_slug>
  - function/index
  - language/in/<language>
---

# index

- <institution> <course code>
- name: <course name (English)>
- credits: <number of credits>

---

<course description and any additional notes>

The content is in teaching order.

## children

- [assignments/](assignments/index.md)
- [attachments/](attachments/index.md)
- [labs/](labs/index.md)
- [questions/](questions/index.md)
- [tutorials/](tutorials/index.md)
- [AGENTS](AGENTS.md)

## logistics

- grading
  - <component name>: <percent>%; <optional description>
  - <another component>: <percent>%
- sections:
  - lecture: <chosen section>
    - L1: <venue>; <weekday>T<start>/<weekday>T<end>[, ...]
    - L2: <venue>; <weekday>T<start>/<weekday>T<end>[, ...]
  - tutorials: <chosen section>
    - T1: <venue>; <weekday>T<start>/<weekday>T<end>[, ...]
    - T2: <venue>; <weekday>T<start>/<weekday>T<end>[, ...]
  - labs: <chosen section>
    - LA1: <venue>; <weekday>T<start>/<weekday>T<end>[, ...]
    - LA2: <venue>; <weekday>T<start>/<weekday>T<end>[, ...]

## overview

- official course outline
  - <main lecture theme>
  - <main lecture theme>
- topic-to-file mapping
  - <topic cluster>
    - [<topic note>](<topic%20note>.md)
    - [<topic note>](<topic%20note>.md)
- notes
  - <brief root-level note>
  - <brief root-level note>

## assignments

- assignment 1
  - due: 2025-09-30T23:59:59+08:00
  - points: 100
  - link: [assignment 1](assignments/assignment%201/index.md)
- assignment 2
  - due: 2025-10-21T23:59:59+08:00
  - points: 100
  - link: [assignment 2](assignments/assignment%202/index.md)

## week 1 lecture 1

- datetime: 2025-09-16T12:00:00+08:00/2025-09-16T13:20:00+08:00, PT1H20M
- status: scheduled
- topic: logistics; introduction
- <COURSE CODE>
  - <COURSE CODE> / logistics ::@:: Course logistics, recommended books, evaluation.

## week 1 tutorial 1

- datetime: 2025-09-16T15:00:00+08:00/2025-09-16T16:20:00+08:00, PT1H20M
- topic: functional programming exercises
- <COURSE CODE>
  - <COURSE CODE> / tutorial 1 ::@:: Description for tutorial 1.

## week 1 lecture 2

- datetime: 2025-09-18T12:00:00+08:00/2025-09-18T13:20:00+08:00, PT1H20M
- topic: merge sort; algorithms
- <COURSE CODE>
  - <COURSE CODE> / merge sort ::@:: Divide-and-conquer sorting, stability, complexity.

## midterm examination

- datetime: 2025-10-28T12:00:00+08:00/2025-10-28T14:00:00+08:00
- venue: Room 4621
- format:
  - cheatsheet: allowed
  - open book: no
  - questions: long question ×4

---

Administrative exam notes may be written here as ordinary prose.

## final examination

- datetime: 2025-12-15T08:30:00+08:00/2025-12-15T10:30:00+08:00
- venue: Lecture Theater L
- format:
  - cheatsheet: allowed
  - open book: no
  - questions: long question ×3
```

### Example: recurrent course sessions

A course that runs every term records each term's meetings under its own
semester header:

```markdown
## 2026 fall

### 2026 fall week 1 tutorial 1

- datetime: 2026-09-02T18:00:00+08:00/2026-09-02T21:00:00+08:00, PT3H
- venue: LTA
- topic: CSE program orientation talk and dinner
- status: optional

### 2026 fall week 3 tutorial 1

- datetime: 2026-09-16T18:00:00+08:00/2026-09-16T19:00:00+08:00, PT1H
- venue: LTA
- topic: video taking and processing training module
- status: optional
```

### Example: lab leaf index with dual components

A lab with both out-of-class (pre-lab) and in-class components:

```markdown
---
aliases:
  - HKUST ELEC 2100 lab 1
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/labs/lab_1/index
  - language/in/English
---

# lab 1

- HKUST ELEC 2100

---

- title: Lab 1: Signal Sampling
- due: 2025-09-26T23:59:00+08:00
- points: 20
- submitting: a file upload

---

Lab instructions and sample data.

## attachments

- [`lab1.pdf`](attachments/lab1.pdf)

## submission

- file: [`prelab.pdf`](submission/prelab.pdf)
    - metadata: [`submission.yml`](submission.yml)
- in-class submission
    - metadata: [`lab.yml`](lab.yml)

## solution

- [`solution.pdf`](solution/solution.pdf)

## children

- [lab](lab.md)
```
