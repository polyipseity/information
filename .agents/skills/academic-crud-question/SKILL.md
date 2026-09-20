---
name: academic-crud-question
description: Create, read, update, and delete question and problem-set pages under special/academia/<INSTITUTION>/<COURSE>/questions/. Covers iPRs, in-class exercises, quizzes, practice problems, and anything without a formal submission.
---

# Academic CRUD: Question pages

Question pages hold problems and exercises from any source (lectures, labs, tutorials, materials, quizzes) that do not require formal submission.

## Target

`special/academia/<INSTITUTION>/<COURSE>/questions/<name>.md`

For multi-page question sets: `questions/<name>/index.md` with child pages.

The `##` sections inside a question page group questions by concept or question type, not by the source's layout or ordering (see "Grouping: concepts, not source layout" in `academic-crud-topic-note`).

## CRUD operations

### Create

1. __Extract questions__ from the input (PDF text extraction, Canvas quiz HTML, manual):
   - Identify official problem statements vs self-authored content
   - Extract solutions if available
   - Identify the source (tutorial sheet, problem set, practice exam)
2. __Write the page__ in this structure:

```markdown
---
aliases:
  - <INSTITUTION> <COURSE> <name>
tags:
  - flashcard/active/special/academia/<INSTITUTION>/<COURSE>/questions/<name>
  - language/in/English
---

# <name>

- <INSTITUTION> <COURSE>
- topics: <comma-separated topic list>

<Page description — pedagogical aim, source materials, skill progression>

---

<!-- Source: <description> -->

> **Problem 1.** <problem statement>
>
> **Solution:**
> <solution with cloze flashcards>

<!-- markdownlint MD028 -->

> **Problem 2.** <problem statement>
>
> **Solution:**
> <solution>
```

1. __Add cloze flashcards__ to the solutions:
   - Use `{@{ }@}` (cloze), not QA format
   - __Solution lines:__ one cloze per solution, on the core result, formula, or decisive step. Very long solutions (multi-step derivations, lengthy prose) may carry several clozes, one per logical step.
   - __Explanation lines:__ prefer several clozes, breaking the explanation into individual claims, conditions, and reasoning steps.
   - Split prose and equation into separate clozes: `{@{prose}@} is {@{$equation$}@}`
   - Cloze technique names: `{@{Swap sum order}@}`, `{@{completing the square}@}`
   - See `create-flashcards` for the cloze methodology.
2. __Create `questions/index.md`__ via `academic-crud-index` if this is the first question page.
3. __Reconcile the topic notes.__ The problems carry concepts the course's notes may already own; extend, prune, or create them, or record that they are covered (see "Topic-note reconciliation (mandatory)" in `academic-ingest`). A question page is not the home of a durable concept.

### Read

List question pages; search by topic; show flashcard coverage.

### Update

- Add questions and enhance solutions.
- Ensure each solution has a cloze and each explanation has several.
- Cross-reference with topic notes: `(from Problem N)`.

### Delete

Remove the question page and update `questions/index.md`.

## Missing data

Use `\[missing\]` for absent values, such as a problem with no solution yet or a quiz with no timestamp (see [special.instructions.md](../../instructions/special.instructions.md#missing-data)).

## Blockquote formatting

- Official problems in blockquotes (`>`)
- `> Solution:` on its own line within each blockquote
- `<!-- markdownlint MD028 -->` between adjacent blockquotes
- Blank blockquote lines (`>`) between display math and prose:

```markdown
> $$f_X(x) = \lambda e^{-\lambda x}$$
>
> The CDF is obtained by integrating.
```

Every line inside a blockquote must begin with `>`, blank lines included.

## Solution conventions

- Decompose → apply bound/theorem → evaluate → conclude
- Show intermediate steps (antiderivative, geometric-series closed form, factorial-ratio simplification)
- Cross-reference: `(from Problem 2(b))`
- True/false: `__False.__` with a counterexample; `__True.__` with a theorem reference
- Alternative solutions: `__Alternative (method name):__` bold header
- Cloze as logical implication: visible premise → hidden conclusion
- Display math merged onto the blockquote line: `> The form simplifies to $$...$$`

## Canvas quiz handling

### Public/private paired layout

- Public: `questions/quiz N.md` with an active flashcard tag and `## hints`
- Private: mirrored private path with an archive tag and `## content`
- Keep basenames aligned on both sides

### Public quiz page

- Transform the official quiz into review material.
- Recognition rules, conceptual hints, compact worked reminders.
- Active-recall prompts in the same order as the archived question order.
- Do not copy the full official question set verbatim when a private page exists.

### Private quiz page

- Preserve the official prompt text in blockquotes.
- Label answers `- archived selection:` or `- selected answer:`, not `- solution:` unless confirmed.
- Preserve quiz metadata: datetime, points, time limit, attempts.
- Extract figures from Canvas HTML into `attachments/` (`academic-vision` covers looking at each one and writing its alt text).
- Keep `Explanation:` with cloze coverage even for image-based questions.

## Flashcard conventions for question pages

- Cloze `{@{ }@}` format, not QA
- Cloze both technique names and final results
- `{@{ }@}` must never appear inside `$…$` or `$$…$$`; wrap from outside
- Place `}@}` before trailing punctuation
- Progressive difficulty: simple case first, then extend
- __Humanizer pass:__ load the `humanizer` skill, then run it over the solution and explanation prose after inserting clozes. Keep the hint words that make each deletion answerable and drop the filler around them; text quoted from the official question stays verbatim (see "Humanizer pass" in `academic-ingest`).

## References

- `create-flashcards` for cloze methodology and patterns
- `humanizer` for the AI-writing patterns the humanizer pass removes (see "Humanizer pass" in `academic-ingest`)
- `academic-crud-index` for parent index updates
- `academic-crud-attachments` for questions-level attachments
- `academic-lint` for validation
