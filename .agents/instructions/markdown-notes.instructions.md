---
name: Markdown notes
description: Conventions for Markdown knowledgebase notes and flashcards
applyTo: "general/**/*.md"
---

# Markdown Notes Guidelines

## Frontmatter & metadata

- **YAML structure**: `aliases` (list), `tags` (list with `flashcard/active`, `language/in/English`, subject tags)
- **Preservation**: Keep frontmatter intact during edits; do not strip fields or reorder without user approval
- **Example**:

  ```yaml
  ---
  aliases: [GDP, Gross Domestic Product]
  tags: [flashcard/active, language/in/English, economics]
  ---
  ```

## Cloze & flashcard markup

Flashcards are produced by three distinct markup conventions; agents and
authors should know which one they are using and keep the syntax exact.

- **Cloze flashcards** use `{@{hidden text}@}`.  The text between the
  delimiters is hidden during review and the card asks you to recall the
  omitted portion.  This is the most common form and may appear anywhere in
  a paragraph.

- **Two-sided flashcards** use a single line with a separator `::@::`.
  Example: `term ::@:: definition`.  Two cards are generated: one that shows
  the left side and asks for the right, and one that shows the right side
  and asks for the left.  The source must remain on one Markdown line;
  represent any needed visual breaks with `<br/>` or `<p>` tags.

- **One-sided flashcards** use a single line with a separator `:@:`.  Only
  a single card is created (recall the right-hand text from the left).  The
  same single-line restriction applies.

**Rules**:

- Do not escape, encode, or otherwise alter the delimiters.
- Do not reflow or split markup across multiple physical lines; the
  generator treats each line literally.
- Preserve spacing inside `{@{ }@}`, and around the `::@::` or `:@:`
  separators.
- After editing you do **not** need to run any generation command; the
  build workflows handle flashcard updates automatically.

## pytextgen blocks

**Code fence blocks**:

- Preserve `# pytextgen generate ...` comment lines exactly (module, function, section IDs)
- Never change triple backticks or language identifier
- Keep `return export_seq(...)` signatures intact

**HTML comment blocks**:

- Preserve `<!--pytextgen generate section="..."-->` and `<!--/pytextgen-->` exactly
- Never modify section IDs or format specifiers
- Content between tags is auto-replaced on regeneration

**When editing**: If modifying prose inside/around fences, ensure fence syntax remains untouched. Regeneration is automatic and the agent should avoid running `uv run -m init generate`; instead rely on build checks to validate fence integrity.

## Links & media

- **Relative paths only**: Use `./relative/file.md` or `path/to/file.md` (no absolute URLs unless essential)
- **URL encoding**: Use `%20` for spaces (e.g., `File%20Name.md`), not `%3A` or other encodings
- **Media references**: Point to `archives/` (preferred: `archives/Wikimedia Commons/` for images)
- **Existing links**: Preserve link targets; do not modify working links unnecessarily

## Formatting

- **Respect linting config**: `.markdownlint.json` disables MD013/MD033/MD051 for this repository (line length, HTML blocks, link spacing)
- **KaTeX math**: Preserve `$inline$` and `$$display$$` math exactly; do not escape or wrap
- **Line wrapping**: Avoid hard-wrapping existing lines unless essential for readability
- **Markdown structure**: Preserve heading levels, list nesting, and code fence languages

## Submodules

- **`self/**`, `private/**`, `tools/pytextgen/`, `tools/pyarchivist/`**: Treat as read-only unless user explicitly approves
- **Policy**: Ask user before editing submodule content; follow submodule's own `AGENTS.md` after permission granted
- **Testing**: Always test changes thoroughly before committing (see related skill documentation)

## Integration

- **Wiki ingestion**: Use [wiki-ingestion](../skills/wiki-ingestion/SKILL.md) skill to import Wikipedia articles with proper frontmatter
- **Flashcard generation**: Use [pytextgen](../skills/pytextgen/SKILL.md) skill to regenerate cloze markup into flashcards
- **Note scaffolding**: Use [tools/SKILL.md](../skills/tools/SKILL.md) (templates section) to scaffold new notes with proper structure

## Developer tooling & testing (notes-related changes)

- If you change code that modifies Markdown (`init.py`, `tools/pytextgen`, or converters), add tests that validate generated output and round-trip behaviour. Unit-tests should check small deterministic inputs; integration tests should run the generator end-to-end in `tmp_path: os.PathLike[str]` (annotate the `tmp_path` fixture as `PathLike[str]`) and assert output files and fence contents. When converting path-like objects to `str` in tests or code use `os.fspath(path_like)`.
- For content edits, include a test that verifies generated output is stable without requiring the generator to be executed; avoid running `uv run -m init generate` during automated tests, and agents should not perform it.
