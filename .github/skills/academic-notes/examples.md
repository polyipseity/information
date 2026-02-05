# Examples and snippets (academic notes)

## Minimal frontmatter

```markdown
---
aliases:
  - COMP 3031
  - Principles of Programming Languages
tags:
  - flashcard/active/special/academia/<INSTITUTION>/COMP_3031
  - function/index
  - language/in/English
---
```

## Weekly lecture example

```markdown
## week 3 lecture

- datetime: 2025-09-16T12:00:00+08:00/2025-09-16T13:20:00+08:00, PT1H20M
- topic: polymorphism; type bound; variance
- COMP 3031
  - COMP 3031 / polymorphism ::@:: Parametric polymorphism, subtyping polymorphism
```

Notes: prefer using `COMP_3031` (underscore) in course-scoped flashcard activation tags; frontmatter tags should use the canonical institution short name (e.g., `HKUST`).

## Detailed lecture example (content-focused)

```markdown
## week 7 lecture

- datetime: 2025-10-07T12:00:00+08:00/2025-10-07T13:20:00+08:00, PT1H20M
- topic: type inference; Hindley–Milner
- learning_outcomes:
  - Understand the Hindley–Milner inference algorithm conceptually
  - Apply algorithm to small expressions and infer principal types
- takeaway: Principal type inference reduces annotation burden; watch for let-polymorphism corner cases
- COMP 3031
  - HM / algorithm sketch ::@:: Unify constraints from expression syntax tree, solve by substitution
  - HM / worked example (detailed):
    1. Given expression: let f = \x -> (x, x) in f 3
    2. Assign type variables: x: a
    3. Constraint from (x, x): a must be the same for both components
    4. f: a -> (a, a), application f 3 enforces a = Int
    5. Result: (3, 3) :: (Int, Int)
  - !emphasis: Instructor stressed 'generalization at let-bindings' (important for polymorphism in ML-like languages)

  Note: keep long proofs or formal material in `general/` when they are encyclopedic; link from course notes instead of copying.

> Note: Save long proofs or formal definitions in `../../../../general/Hindley–Milner.md` and link from here.
```

## Linking to `general/` (Wikipedia titles)

Use the helper script to find a recommended article title:

```bash
python .github/skills/academic-notes/find_wikipedia.py "Hindley Milner"
```

The script prints JSON lines with suggested `title` and `url`. Pick the top candidate (e.g., `Hindley–Milner`) and link to `../../../../general/Hindley–Milner.md` from course notes. Do NOT create or edit files under `general/`.

## Assignments layout

```text
special/academia/<INSTITUTION>/<COURSE>/assignments/
  index.md
  homework 1/
    index.md
    submission.yml
    attachments/
```

Tip: keep `assignments/` directories small and include a `submission.yml` template for graders; student-submitted files (if containing PII) belong in `private/`.

## Inline gloss & takeaway examples (what we actually see in notes)

```markdown
- topic ::@:: Type inference and Hindley–Milner
- takeaway ::@:: Principal type inference reduces annotation burden; watch for let-polymorphism corner cases
- COMP 3031 / Hindley–Milner ::@:: Unify constraints from expression syntax tree and solve by substitution

Keep glossary one-liners concise; these are the primary source of flashcards via `::@::` markup.
```

## Taxonomy / chain notation (observed)

```markdown
- _(begin)_→::@::←blue ocean strategy: Break the value–cost tradeoff. For example, London cab services (red) and Uber (blue).
- blue ocean strategy: Break the value–cost tradeoff.→::@::←business model canvas
- business model canvas→::@::←competitor analysis
- ...
- value proposition canvas→::@::←_(end)_
```

## Takeaway shorthand (normalization suggestion)

```markdown
- general case analysis question takeaways ::@:: Identify key questions. Choose the question that is most precise and involves least work.

-->

- takeaway: Identify key questions; pick the most precise one that minimizes extra work.
```

## Datetime with duration example

```markdown
- datetime: 2024-02-06T18:00:00+08:00/2024-02-06T20:00:00+08:00
- datetime: 2024-11-09T09:30:00+08:00/2024-11-09T12:30:00+08:00, PT3H
```

## Flashcard activation tag (example frontmatter)

```markdown
---
tags:
  - flashcard/active/special/academia/<INSTITUTION>/COMP_3031
  - function/index
---
```

These examples are institution-agnostic; replace `<INSTITUTION>` with the canonical short name you use (e.g., `HKUST`, `MIT`, `STANFORD`). Use underscores for course codes inside the tag (e.g., `COMP_3031`).
