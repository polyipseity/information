# Course note template (institution-agnostic)

This template follows the practical layout used in exemplar course pages (for example, `COMP 3031` and `ACCT 3010`) and captures common, repeatable patterns found in those examples. Use it when creating new course pages under `special/academia/<INSTITUTION>/<COURSE CODE>/`.

Key patterns to follow (seen in the examples):

- Provide multiple `aliases:` forms (with/without spaces, with/without `index`, and with the institution prefix) so note pages are easily discoverable.
- Use `tags:` with the course code using an underscore (e.g., `COMP_3031`) for flashcard activation and include `language/in/<LANGUAGE>`.
- Include the short line "The content is in teaching order." under the course `name` (this appears in the examples and makes ordering explicit).
- Keep `children:` ordered and include `assignments/` immediately after `children` (and before sessions); include `attachments` and `questions` if relevant.
- Use a nested grading `scheme:` block and include exam metadata such as `venue:` and `format:` (e.g., `cheatsheet`, `open book`) when applicable.
- Use session `status:` fields for cancellations/unscheduled/online notes and add `::@::` takeaways for flashcard generation.

See `.github/skills/academic-notes/examples.md` for concrete snippets and validated frontmatter examples (lectures, labs, assignments, exams).

## Short style notes (must appear outside the code block)

- Keep the code block strictly machine-readable: frontmatter and topical entries belong inside the fenced `markdown` block only. ❗
- Add human-readable guidance and style notes *outside* the fenced block (below the block) so they are not copied into course pages. ✅
- Use `COMP_3031` (underscore) for flashcard activation tags in `tags:`; in prose use the spaced form `COMP 3031` as the visible heading. 🔖
- For repeated sessions in one week, use numbered subheadings: `lecture 1`, `lecture 2`, `lab 1`, `lab 2`, etc. 🔁
- Include a one-line `::@::` takeaway per topic for flashcard generation; keep takeaways short and actionable (one sentence or fragment). ✍️
- Use `datetime` with ISO format and optional duration (e.g., `, PT1H20M`) where appropriate. ⏱️

> Note: Always add style/explanatory notes outside the fenced code block; never place explanatory text inside the template's `markdown` code block.

### assignments

- NOTE: Place the `assignments/` child immediately after `children` and before any session entries (lectures, labs, tutorials, exams). Each assignment lives under `assignments/assignment N/` with an `index.md` and optional `submission.yml`. Always list assignments in chronological order by due date.

### sessions and chronology

- Session entries (lectures, labs, tutorials, exams) may interleave in time. Always list all sessions in strict chronological order. Use dated `datetime` fields to make ordering explicit and machine-readable.
- For multiple sessions within a week, use numbered subheadings (e.g., `lecture 1`, `lecture 2`, `lab 1`, `lab 2`) and keep them ordered by datetime.

## template content

```markdown
---
aliases:
  - <COURSE CODE>
  - <COURSE CODE> index
  - <INSTITUTION> <COURSE CODE>
  - <INSTITUTION> <COURSE CODE> index
tags:
  - flashcard/active/special/academia/<INSTITUTION>/<COURSE_CODE>
  - function/index
  - language/in/<LANGUAGE>
---

# index

- <INSTITUTION> <COURSE CODE>
- name: <Course Name (English)>
- credits: <N>

Short course description goes here. Keep it concise (1–3 lines).

The content is in teaching order.

## logistics

- grading
  - scheme
    - assignments ×<n>: <percent>%
    - midterm examination: <percent>%
    - final examination: <percent>%

## children

- [assignments/](assignments/index.md)
- [attachments/](attachments/index.md)
- [labs/](labs/index.md)
- [lectures/](lectures/index.md)
- [questions/](questions/index.md)
- [tutorials/](tutorials/index.md)

## assignments

- assignment 1
  - due: 2025-09-30
  - points: 100
  - link: [assignment 1](assignments/assignment%201/index.md)
- assignment 2
  - due: 2025-10-21
  - points: 100
  - link: [assignment 2](assignments/assignment%202/index.md)

### week 1 lecture 1

- datetime: 2025-09-16T12:00:00+08:00/2025-09-16T13:20:00+08:00, PT1H20M
- status: scheduled
- topic: logistics; introduction
- <COURSE CODE>
  - <COURSE_CODE> / logistics ::@:: Course logistics, recommended books, evaluation
- [link to general article](../../../../general/link%20to%20general%20article.md) ::@:: Description for "link to general article".

### week 1 lab 1

- datetime: 2025-09-15T15:00:00+08:00/2025-09-15T16:20:00+08:00, PT1H20M
- topic: functional programming exercises
- <COURSE CODE>
  - <COURSE CODE> / lab 1 ::@:: Description for lab 1.
    - <COURSE CODE> / lab 1 / Pascal's triangle ::@:: Purely recursive solution; no mutation allowed

### week 1 tutorial 1

- datetime: 2025-09-16T15:00:00+08:00/2025-09-16T16:20:00+08:00, PT1H20M
- topic: functional programming exercises
- <COURSE CODE>
  - <COURSE CODE> / tutorial 1 ::@:: Description for tutorial 1.
    - <COURSE CODE> / tutorial 1 / Pascal's triangle ::@:: Purely recursive solution; no mutation allowed

### week 1 lab 2

- datetime: 2025-09-17T15:00:00+08:00/2025-09-17T16:20:00+08:00, PT1H20M
- topic: additional lab (make-up)
- <COURSE CODE>
  - <COURSE CODE> / lab 2 ::@:: Description for lab 2.

### week 1 lecture 2

- datetime: 2025-09-18T12:00:00+08:00/2025-09-18T13:20:00+08:00, PT1H20M
- topic: merge sort; algorithms
- <COURSE CODE>
  - <COURSE_CODE> / merge sort ::@:: Divide-and-conquer sorting, stability, complexity
- [merge sort](../../../../general/merge%20sort.md) ::@:: Description for merge sort.

## midterm examination

- datetime: 2025-10-28T12:00:00+08:00/2025-10-28T14:00:00+08:00
- venue: Room 4621
- format:
  - cheatsheet: allowed
  - open book: no
  - questions: long question ×4 (with subquestions)

## final examination

- datetime: 2025-12-15T08:30:00+08:00/2025-12-15T10:30:00+08:00
- venue: Lecture Theater L
- format:
  - cheatsheet: allowed
  - open book: no
  - questions: long question ×3

## aftermath

### total

- grades: 100/100
  - statistics: ?
```
