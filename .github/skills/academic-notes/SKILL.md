---
name: academic-notes
description: Content conventions, examples, and tooling for course notes under special/academia.
---

# Academic notes — skill overview

This skill explains how to author, validate, and maintain academic course notes stored under `special/academia/<INSTITUTION>`. It is written for AI agents, human authors, and maintainers. **Agents must read *every file* in this skill folder and absorb all lines before acting; do not rely on summaries or partial reads.** Flashcards are generated automatically by the build system; do not run `init generate` yourself.

## Key principles

1. **Content first**: capture every slide bullet, formula, definition, and instructor comment as prose or hierarchical bullets. Err on the side of completeness; extra detail helps recall and tooling filters out noise.
2. **Automatic flashcards**: flashcard markup (`{@{ }@}`, `::@::`, `:@:`) is the only mechanism for memorization. Update cards whenever you expand or revise a section. Generators run in CI; agents must never invoke them.
3. **Structured metadata**: use ISO‑8601 datetimes, maintain `children:` lists, add flashcard activation tags (`flashcard/active/special/academia/...`), and keep semester headings chronological.
4. **Continuous learning**: record new rules and patterns in this skill’s files (`patterns.md`, `examples.md`, etc.) and update documentation when instructions evolve. Feedback lives in `continuous_improvement.md`.

## Audience

- **Agents and authors** writing or editing course content.
- **Maintainers** normalizing style, resolving warnings, and reviewing submissions.
- **Tools** such as the validator and Wikipedia helper.

## Contents of the skill

- `patterns.md` — common idioms and recommended normalizations.
- `examples.md` — concrete snippets showing templates, flashcards, links.
- `checklist.md` — pre‑commit author checklist.
- `flashcards.md` — detailed flashcard markup guidance.
- `continuous_improvement.md` — feedback workflow.
- `validate_academic.py` — lint/validator script (`--content` for advisory).
- `find_wikipedia.py` — search tool for canonical article titles.

## Authoring workflow

1. Start with `course-template.md`. Fill aliases (singular, plural, concatenated), tags (include underscore course code), name, credits, and brief description. Sort aliases alphabetically.
2. Add a `logistics` section with `scheme:` weights and a nested `sections:` list grouped by lectures/tutorials/labs. Include identifiers, venues, and weekly time patterns.
3. Maintain a `children:` list with lectures, labs, assignments, topics, questions, attachments and keep entries in teaching order.
4. Use the session structure from examples. Add `datetime:` entries with ISO intervals (date only if time unknown). Place prose summaries after the bullet outline separated by `---`.
5. Capture content‑first details in prose paragraphs, not bullets. Draft explanatory prose before adding cloze markup. After prose, add flashcard lists or inline glosses.
6. Always add a flashcard block for every markdown section in topic notes. Index pages only require cards per session entry.
7. When adding or changing any section, audit the whole file for missing or malformed flashcards, separators, numeric values, tags, and indentation.
8. Run the validator and address warnings.
9. Add assignments, questions, attachments in their folders and list under `children`.
10. Run `checklist.md` before committing.

### Cards and markup

- Use `::@::` for two‑sided cards, `:@:` for one‑sided, and `{@{ }@}` for clozes. Cards must be single source lines. Use `<br/>` or `<p>` for visible breaks; never insert hard newlines in card text.
- One separator per line. Extra separators break the generator.
- Prefix glosses with the full hierarchical path (`COURSE / topic / item`).
- Merge cards sharing the same prefix with `<br/>` to separate right‑hand points.
- Keep math units inside `$…$` or `$$…$$`.
- Do not write next‑lecture remarks inside sessions.
- Avoid acronyms; spell out first use.
- Preserve rhetorical questions or instructor hints as separate bullets.
- For numerical examples, include all given values on the left and outline the computation steps on the right.
- Never merge flashcards across sections; each heading gets its own block.

### Flashcard tags

Always add `flashcard/active/special/academia/<institution>/<page>` to frontmatter. `<page>` mirrors the course code with underscores. Do not percent encode spaces. Validators flag missing or malformed tags.

## Topic-specific notes

Create a new file under the course directory when a topic is broad enough to warrant its own page or will be reused. Use Wikipedia article titles for filenames. Use neutral, descriptive prose; avoid slide‑transcript style. Paragraphs may be long and may wrap freely. Math expressions must stay on a single source line. Include a link back to the canonical `general/` article and add the new file to the course `children:` list. Update index entries with `- COURSE / [topic](file.md)` and nested anchors for covered sections. When later lectures revisit the same topic, append to the existing note instead of creating duplicates.

Use `find_wikipedia.py` to search titles. Always search before creating a file and reuse existing notes if the topic is already present.

## Validator and tooling

Run `python .github/skills/academic-notes/validate_academic.py special/academia/<path>` regularly. Use `--content` for advisory warnings during drafting. Address issues where practical; common warnings include missing tags, absent `datetime:` values, out‑of-order semesters, and sections without cards.

Before committing run `pnpm run format`, `pnpm run check`, and `pnpm run test` with explicit paths to affected files. Use `checklist.md` to ensure nothing is overlooked.

## Continuous improvement

Record every new pattern, bug, or user preference in `continuous_improvement.md` and consider updating `patterns.md`, `examples.md`, or the validator accordingly. Keep the skill up to date; it evolves with real course content and user feedback. Solicit feedback from users and the repository owner, then add brief notes under `.github/skills/academic-notes/reports/` when appropriate.
