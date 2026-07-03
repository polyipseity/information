---
name: Markdown notes
description: Conventions for Markdown knowledgebase notes and flashcards
applyTo: "general/**/*.md"
---

# Markdown Notes Guidelines

## Frontmatter & metadata

- __YAML structure__: `aliases` (list), `tags` (list with `flashcard/active`, `language/in/English`, subject tags)
- __Preservation__: Keep frontmatter intact during edits; do not strip fields or reorder without user approval
- __Example__:

  ```yaml
  ---
  aliases: [GDP, Gross Domestic Product]
  tags: [flashcard/active, language/in/English, economics]
  ---
  ```

## Cloze & flashcard markup

Flashcards are produced by three distinct markup conventions; agents and authors should know which one they are using and keep the syntax exact.

- __Cloze flashcards__ use `{@{hidden text}@}`. The text between the
  delimiters is hidden during review and the card asks you to recall the
  omitted portion. This is the most common form and may appear anywhere in
  a paragraph.

- __Two-sided flashcards__ use a single line with a separator `::@::`.
  Example: `term ::@:: definition`. Two cards are generated: one that shows
  the left side and asks for the right, and one that shows the right side
  and asks for the left. The source must remain on one Markdown line;
  represent any needed visual breaks with `<br/>` or `<p>` tags.

- __One-sided flashcards__ use a single line with a separator `:@:`. Only
  a single card is created (recall the right-hand text from the left). The
  same single-line restriction applies.

__Rules__:

- Do not escape, encode, or otherwise alter the delimiters.
- Do not reflow or split markup across multiple physical lines; the
  generator treats each line literally.
- Preserve spacing inside `{@{ }@}`, and around the `::@::` or `:@:`
  separators.
- After editing you do __not__ need to run any generation command; the
  build workflows handle flashcard updates automatically.

## pytextgen blocks

__Code fence blocks__:

- Preserve `# pytextgen generate ...` comment lines exactly (module, function, section IDs)
- Never change triple backticks or language identifier
- Keep `return export_seq(...)` signatures intact

__HTML comment blocks__:

- Preserve `<!--pytextgen generate section="..."-->` and `<!--/pytextgen-->` exactly
- Never modify section IDs or format specifiers
- Content between tags is auto-replaced on regeneration

__When editing__: If modifying prose inside/around fences, ensure fence syntax remains untouched. Regeneration is automatic and the agent should avoid running `uv run -m init generate`; instead rely on build checks to validate fence integrity.

## Links & media

- __Relative paths only__: Use `./relative/file.md` or `path/to/file.md` (no absolute URLs unless essential)
- __URL encoding__: Use `%20` for spaces (e.g., `File%20Name.md`), not `%3A` or other encodings
- __Media references__: Point to `archives/` (preferred: `archives/Wikimedia Commons/` for images)
- __Existing links__: Preserve link targets; do not modify working links unnecessarily

## Formatting

- __Respect linting config__: `.markdownlint.json` disables MD013/MD033/MD051 for this repository (line length, HTML blocks, link spacing)
- __KaTeX math__: Preserve `$inline$` and `$$display$$` math exactly; do not escape or wrap
- __Line wrapping__: Avoid hard-wrapping existing lines unless essential for readability
- __Markdown structure__: Preserve heading levels, list nesting, and code fence languages

## Submodules

- __`private/**`__: Treat as read-only unless user explicitly approves
- __`self/stash/`__ is not a git submodule; if it is relevant to a notes task, still treat it as user-owned scratch space and avoid editing it unless requested.
- __Policy__: Ask user before editing submodule content; follow submodule's own `AGENTS.md` after permission granted
- __Testing__: Always test changes thoroughly before committing (see related skill documentation)

## Integration

- __Wiki ingestion__: Use [wiki-ingestion](../skills/wiki-ingestion/SKILL.md) skill to import Wikipedia articles with proper frontmatter
- __Flashcard generation__: Use [pytextgen](../skills/pytextgen/SKILL.md) skill to regenerate cloze markup into flashcards
- __Note scaffolding__: Use [tools/SKILL.md](../skills/tools/SKILL.md) (templates section) to scaffold new notes with proper structure

## Developer tooling & testing (notes-related changes)

- If you change code that modifies Markdown content generation or converters, add tests that validate generated output and round-trip behaviour. Unit-tests should check small deterministic inputs; integration tests should run the generator end-to-end in `tmp_path: os.PathLike[str]` (annotate the `tmp_path` fixture as `PathLike[str]`) and assert output files and fence contents. When converting path-like objects to `str` in tests or code use `os.fspath(path_like)`.
- For content edits, include a test that verifies generated output is stable without requiring the generator to be executed; avoid running `uv run -m init generate` during automated tests, and agents should not perform it.
