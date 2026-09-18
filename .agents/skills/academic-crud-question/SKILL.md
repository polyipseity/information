---
name: academic-crud-question
description: Create, read, update, and delete question and problem-set pages under special/academia/<INSTITUTION>/<COURSE>/questions/. Covers iPRs, in-class exercises, quizzes, practice problems, and anything without a formal submission.
---

# Academic CRUD: Question pages

Create, read, update, and delete question pages. These are problems and exercises from any source (lectures, labs, tutorials, materials, quizzes) that do not require formal submission.

## Target

`special/academia/<INSTITUTION>/<COURSE>/questions/<name>.md`

For multi-page question sets: `questions/<name>/index.md` with child pages.

The `##` sections inside a question page group questions by concept or question type, not by the source's layout or ordering — see "Grouping: concepts, not source layout" in `academic-crud-topic-note`.

## CRUD operations

### Create

1. __Extract questions__ from input (PDF text extraction, Canvas quiz HTML, manual):
   - Identify official problem statements vs self-authored content
   - Extract solutions if available
   - Identify source (tutorial sheet, problem set, practice exam, etc.)

2. __Structure page:__

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

1. __Flashcards (cloze):__
   - Use `{@{ }@}` (cloze) format for solutions — NOT QA format
   - __Solution lines:__ ideally one cloze per solution — cloze the core result, formula, or decisive step. Only for very long solutions (multi-step derivations, lengthy prose) may multiple clozes appear, one per logical step.
   - __Explanation lines:__ prefer multiple clozes whenever possible — break the explanation into individual claims, conditions, and reasoning steps, each wrapped in its own cloze.
   - Split prose + equation into separate clozes: `{@{prose}@} is {@{$equation$}@}`
   - Cloze technique names: `{@{Swap sum order}@}`, `{@{completing the square}@}`
   - Reference `create-flashcards` skill for cloze methodology

2. __Create `questions/index.md`__ via `academic-crud-index` if first question page.

### Read

List question pages; search by topic; show flashcard coverage.

### Update

- Add questions, enhance solutions
- Ensure each solution has a cloze and each explanation has multiple clozes
- Cross-reference with topic notes: `(from Problem N)`

### Delete

Remove question page. Update `questions/index.md`.

## Missing data

Use `\[missing\]` for absent values — for example, when a problem has no solution yet or a quiz has no timestamp. See [special.instructions.md](../../instructions/special.instructions.md#missing-data).

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

Every line inside a blockquote must begin with `>` — including blank lines.

## Solution conventions

- Decompose → apply bound/theorem → evaluate → conclude
- Show intermediate steps (antiderivative, geometric-series closed form, factorial-ratio simplification)
- Cross-reference: `(from Problem 2(b))`
- True/false: __False.__ with counterexample; __True.__ with theorem reference
- Alternative solutions: __Alternative (method name):__ bold header
- Cloze as logical implication: visible premise → hidden conclusion
- Display math merged onto blockquote line: `> The form simplifies to $$...$$`

## Canvas quiz handling

### Public/private paired layout

- Public: `questions/quiz N.md` with active flashcard tag and `## hints`
- Private: mirrored private path with archive tag and `## content`
- Keep basenames aligned on both sides

### Public quiz page

- Transform official quiz into review material
- Recognition rules, conceptual hints, compact worked reminders
- Active-recall prompts in same order as archived question order
- Do NOT copy full official question set verbatim when private page exists

### Private quiz page

- Preserve official prompt text in blockquotes
- Label answers as `- archived selection:` or `- selected answer:` (not `- solution:` unless confirmed)
- Preserve quiz metadata: datetime, points, time limit, attempts
- Image extraction: extract figures from Canvas HTML into `attachments/`
- Keep `Explanation:` with cloze coverage even for image-based questions

## Flashcard conventions for question pages

- Cloze `{@{ }@}` format (NOT QA)
- __Solution lines:__ ideally one cloze per solution — cloze the core result, formula, or decisive step. Only for very long solutions may multiple clozes appear, one per logical step.
- __Explanation lines:__ prefer multiple clozes whenever possible — one cloze per claim, condition, or reasoning step.
- Cloze both technique names and final results
- `{@{ }@}` must never appear inside `$…$` or `$$…$$` — wrap from outside
- Place `}`@}` before trailing punctuation
- Progressive difficulty: simple case first, then extend

## References

- `create-flashcards` cloze methodology and patterns
- `humanizer` verbosity pass over new prose and flashcards (see "Humanizer pass" in `academic-ingest`)
- `academic-crud-index` parent index updates
- `academic-crud-attachments` questions-level attachments
- `academic-lint` validation
