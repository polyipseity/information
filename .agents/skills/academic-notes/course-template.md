# Course note template (institution-agnostic)

Use this file as a scaffold for new course pages under
`special/academia/<INSTITUTION>/<COURSE CODE>/`.

## What belongs here

- Template-facing reminders that directly affect how to fill the scaffold.
- Short notes about aliases, tags, ordering, and section layout.
- Example structure for a course `index.md`.

Keep detailed policy, edge cases, and advanced note-writing rules in `SKILL.md`.

## Quick reminders

- Keep the fenced `markdown` block machine-readable.
- Put human guidance **outside** the fenced block.
- For course indexes, include spaced and unspaced course-code aliases plus
  institution-prefixed variants, sorted alphabetically.
- Use underscore-normalized path fragments in flashcard tags, for example
  `flashcard/active/special/academia/HKUST/COMP_3031` or
  `flashcard/active/special/academia/Pusan_National_University/IT3000504`.
- Put course-specific agent instructions in `AGENTS.md` in the same course
  folder only when needed. If you create that file, keep it concise, use the
  title `# <course code> agent instructions`, and do not use flashcard markup
  there (`{@{ }@}`, `:@:`, `::@::`). If you do not create `AGENTS.md`, remove it
  from the `children` list.
- If the provided materials already enumerate repeating deliverables or sessions
  (for example tutorial rounds, lab rounds, quizzes, or homeworks), scaffold
  minimal child pages for those foreseeable items early and keep them lightweight
  until official content arrives.
- Keep `index.md` pages lean: the course root should hold only the high-value
  overview, folder indexes should summarize just enough to navigate, and leaf
  indexes should usually contain only minimal logistics until real content is
  ingested.
- For Canvas-derived assignment-style leaf indexes (for example lab rounds,
  homework folders, quiz handouts, or similar deliverables), structure the page
  as index metadata, `## children`, `## description`, `## attachments`,
  `## submission`, and `## solution`; do not insert an extra `---` after the
  parent line. In `## description`, store the Canvas title header as the first
  list item `- title: <verbatim title>` rather than as a heading, keep the
  visible Canvas wording verbatim, and point the attachments list at local
  `attachments/` files.
- In a course-root `index.md`, order the main top-level sections as `## children`,
  then `## logistics`, then `## overview`; keep sessions and exams after those.
- Prefer one `## overview` section for compact orientation material such as
  official scope bullets, topic-to-file mapping, and short root-level notes.
- When turning lecture PDFs into topic notes, preserve the concrete teaching
  detail: explicit classifications, key formulas, named signal or system
  families, and representative examples or counterexamples from the source.
- Place `assignments/` immediately after `children` and before session entries.
- Keep sessions in strict chronological order and use headings of the form
  `## week N lecture`, `## week N lecture 2`, `## week N lab`, and
  `## week N tutorial`.
- If the official materials define a recurring weekly stream, scaffold that
  stream continuously across the term and mark skipped meetings with `status:`
  metadata rather than omitting the week.
- Use underscore emphasis (`_italic_`, `__bold__`).
- Keep units inside math delimiters, for example `$5\text{ V}$`.

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
  - due: 2025-09-30
  - points: 100
  - link: [assignment 1](assignments/assignment%201/index.md)
- assignment 2
  - due: 2025-10-21
  - points: 100
  - link: [assignment 2](assignments/assignment%202/index.md)

## week 1 lecture

- datetime: 2025-09-16T12:00:00+08:00/2025-09-16T13:20:00+08:00, PT1H20M
- status: scheduled
- topic: logistics; introduction
- <COURSE CODE>
  - <COURSE CODE> / logistics ::@:: Course logistics, recommended books, evaluation.

## week 1 tutorial

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
