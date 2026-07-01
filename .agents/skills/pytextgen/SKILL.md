---
name: pytextgen
description: Regenerate programmatically-generated content blocks in knowledge base notes using pytextgen.
---

# pytextgen Workflow

> __Continuous improvement:__ see `continuous_improvement.md` in this
> folder for documented lessons and evolving best practices.

Use this skill when working with pytextgen-powered content generation, including regenerating flashcards, clearing generated regions, managing caches, and debugging generation issues.

> __Agent note:__ the examples below describe how the `init generate` tool works
> when a human runs it. Agents should __not__ trigger this command on their
> own while editing notes—flashcard and other generated content are rebuilt
> automatically during normal build and packaging workflows.

## What pytextgen does

pytextgen is a Python library (git submodule in `scripts/pytextgen/`) that generates content programmatically in Markdown files:

- __Flashcard generation__: Creates spaced-repetition cards from cloze markup (`{@{ }@}`, `::@::`, `:@:`)
- __Sequence exports__: Exports data structures as Markdown lists, tables, or custom formats
- __Programmatic content__: Python code blocks that generate Markdown on-demand

## When to use

- Regenerating all generated content after editing source files
- Clearing stale or corrupted generated regions
- Initializing flashcard state for new notes
- Debugging generation errors or fence syntax issues
- Managing pytextgen compile cache

## High-level workflows

### Regenerate generated regions

__Command__: `uv run -m init generate [pytextgen flags] <paths?>`

The `init.py` wrapper:

- Auto-discovers `.md` files (excluding `.git`, `.obsidian`, `tools`)
- Caches `(mtime, inode, text)` to skip unchanged files
- Normalizes newlines to `\n` before passing to pytextgen
- Passes through pytextgen-specific flags

__Common flags__:

- `-C` / `--no-cached`: Rebuild `init.py` cache from scratch
- `--no-code-cache`: Disable pytextgen compile cache (in `__pycache__/`)
- `--init-flashcards`: Initialize or re-seed flashcard state
- `<paths>`: Optional; limit regeneration to specific files/directories

__Example__: `uv run -m init generate -C --init-flashcards`

### Clear generated regions

__Command__: `uv run -m init clear --type CONTENT <paths?>`

Clears generated content blocks without regenerating. Useful for:

- Removing stale generated content before regeneration
- Resolving merge conflicts in generated regions
- Debugging generation issues by starting fresh

__Other ClearType values__ (see `scripts/pytextgen/io.py`):

- `CONTENT`: Clear generated text only
- Additional types available in pytextgen documentation

### Scaffold new pytextgen sections

Use templates in `scripts/templates/` to create new pytextgen fences:

- `pytextgen generate flashcards.md`: Flashcard section template
- `pytextgen generate code.md`: Code block template
- Other templates for common generation patterns

## Deep dive: pytextgen fences

### Code fence syntax

```python
# pytextgen generate module="path.to.module" function="function_name"
# pytextgen generate data="./relative/path/to/data.json" format="table"
```

__Critical rules__:

- Do NOT modify the `# pytextgen generate ...` comment line
- Do NOT change fence delimiters (triple backticks with language identifier)
- Preserve `return export_seq(...)` signatures exactly

### HTML comment syntax

```html
<!--pytextgen generate section="unique-id" format="list"-->
Generated content appears here
<!--/pytextgen-->
```

__Critical rules__:

- Do NOT modify section IDs or format specifiers
- Preserve opening/closing comment tags exactly
- Generated content between tags is replaced on regeneration

### Cloze & Flashcard markup

pytextgen recognises three distinct patterns that drive flashcard
creation. Keep them exactly as shown and understand their semantics:

- __Cloze flashcards__ use `{@{hidden text}@}`. The text between the
  delimiters is hidden during review and replaced with a blank that the user
  must recall. Clozes may appear anywhere in a paragraph and multiple clozes
  can coexist on a single line.

- __Two-sided cards__ use a single line with a separator `::@::`. Example:
  `term ::@:: definition`. Two cards are generated: one showing the left
  side and asking for the right, and vice versa. The entire source must be
  on one Markdown line; visual breaks are represented with `<br/>` or `<p>`.

- __One-sided cards__ use a single line with separator `:@:`. Only one card
  is produced (recall right side from left). The same single-line rule
  applies.

__Editing guidance__:

- Do __not__ escape, encode or alter the delimiters in any way.
- Do __not__ reflow or split markup across multiple physical lines; the
  generator splits on newline characters and treats each line literally.
- Preserve spacing inside `{@{ }@}` and around the `::@::` or `:@:`
  separators.
- Two‑sided or one‑sided separators may appear at most once per line;
  multiple separators will confuse the generator.

(The earlier term "cloze markup" is retained only for historical reasons.)

## Debugging generation issues

### Common errors

1. __Syntax errors in fence comments__:
   - Check for typos in `# pytextgen generate ...` lines
   - Verify module/function names are correct
   - Ensure data paths are relative and exist

2. __Fence delimiters broken__:
   - Ensure triple backticks are intact (not escaped)
   - Check language identifier matches expected format
   - Verify closing fence is present

3. __Cache issues__:
   - Use `-C` / `--no-cached` to rebuild `init.py` cache
   - Use `--no-code-cache` to bypass pytextgen compile cache
   - Check `__pycache__/` for stale compiled modules

4. __Cloze markup broken__:
   - Verify `{@{ }@}` pairs are balanced
   - Check for accidental escaping or encoding
   - Ensure separators (`::@::`, `:@:`) are not modified

### Diagnostic commands

```bash
# Regenerate with fresh caches
uv run -m init generate -C --no-code-cache

# Clear and regenerate specific file
uv run -m init clear --type CONTENT path/to/file.md
uv run -m init generate path/to/file.md

# Check for syntax errors (manual inspection)
grep -n "# pytextgen generate" path/to/file.md
```

## Best practices

- __Preserve fence syntax__: Never modify pytextgen comments or delimiters
- __Cache management__: Use `-C` when unsure if cache is stale
- __Incremental regeneration__: Pass specific paths to regenerate only changed files
- __Flashcard initialization__: Use `--init-flashcards` when creating new flashcard-enabled notes
- __Submodule updates__: If pytextgen behavior changes, check for submodule updates (`git submodule update --remote scripts/pytextgen`)

## When to ask for help

- If fence syntax seems correct but generation fails, ask user to check pytextgen submodule version
- If editing is required in `scripts/pytextgen/**`, ask user for permission (it's a submodule)
- If cache behavior is unexpected, clarify with user before deleting cache files

## Integration with other workflows

- __Wiki ingestion__: After running `convert_wiki`, use `init generate` to create flashcards from cloze markup
- __Academic notes__: Use pytextgen to generate course indexes, assignment lists, or reference tables
- __Pack/publish__: Regenerate all content before packaging or publishing to ensure consistency
- __Note conventions__: See [markdown-notes](../../instructions/markdown-notes.instructions.md) for cloze markup preservation rules and the `templates` section of [tools/SKILL.md](../tools/SKILL.md) for fence templates
