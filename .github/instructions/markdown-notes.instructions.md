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

**Critical**: These enable spaced-repetition flashcard generation via pytextgen. Preserve exactly:

- `{@{ hidden text }@}`: Cloze deletion (text hidden in review)
- `::@::`: Question-answer separator
- `:@:`: Alternative Q&A separator

**Rules**:

- Never escape, encode, or reflow text containing cloze markup
- Do not modify or wrap across multiple lines
- Preserve spacing inside delimiters
- After editing, you do **not** need to regenerate manually; the build system
  handles it and agents should not attempt to invoke any generation command.

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
