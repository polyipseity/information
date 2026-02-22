---
name: pytextgen
description: Regenerate programmatically-generated content blocks in knowledge base notes using pytextgen.
---

# pytextgen Workflow

> **Continuous improvement:** see `continuous_improvement.md` in this
> folder for documented lessons and evolving best practices.

Use this skill when working with pytextgen-powered content generation, including regenerating flashcards, clearing generated regions, managing caches, and debugging generation issues.

## What pytextgen does

pytextgen is a Python library (git submodule in `tools/pytextgen/`) that generates content programmatically in Markdown files:

- **Flashcard generation**: Creates spaced-repetition cards from cloze markup (`{@{ }@}`, `::@::`, `:@:`)
- **Sequence exports**: Exports data structures as Markdown lists, tables, or custom formats
- **Programmatic content**: Python code blocks that generate Markdown on-demand

## When to use

- Regenerating all generated content after editing source files
- Clearing stale or corrupted generated regions
- Initializing flashcard state for new notes
- Debugging generation errors or fence syntax issues
- Managing pytextgen compile cache

## High-level workflows

### Regenerate generated regions

**Command**: `uv run -m init generate [pytextgen flags] <paths?>`

The `init.py` wrapper:

- Auto-discovers `.md` files (excluding `.git`, `.obsidian`, `tools`)
- Caches `(mtime, inode, text)` to skip unchanged files
- Normalizes newlines to `\n` before passing to pytextgen
- Passes through pytextgen-specific flags

**Common flags**:

- `-C` / `--no-cached`: Rebuild `init.py` cache from scratch
- `--no-code-cache`: Disable pytextgen compile cache (in `__pycache__/`)
- `--init-flashcards`: Initialize or re-seed flashcard state
- `<paths>`: Optional; limit regeneration to specific files/directories

**Example**: `uv run -m init generate -C --init-flashcards`

### Clear generated regions

**Command**: `uv run -m init clear --type CONTENT <paths?>`

Clears generated content blocks without regenerating. Useful for:

- Removing stale generated content before regeneration
- Resolving merge conflicts in generated regions
- Debugging generation issues by starting fresh

**Other ClearType values** (see `tools/pytextgen/io.py`):

- `CONTENT`: Clear generated text only
- Additional types available in pytextgen documentation

### Scaffold new pytextgen sections

Use templates in `tools/templates/` to create new pytextgen fences:

- `pytextgen generate flashcards.md`: Flashcard section template
- `pytextgen generate code.md`: Code block template
- Other templates for common generation patterns

## Deep dive: pytextgen fences

### Code fence syntax

```python
# pytextgen generate module="path.to.module" function="function_name"
# pytextgen generate data="./relative/path/to/data.json" format="table"
```

**Critical rules**:

- Do NOT modify the `# pytextgen generate ...` comment line
- Do NOT change fence delimiters (triple backticks with language identifier)
- Preserve `return export_seq(...)` signatures exactly

### HTML comment syntax

```html
<!--pytextgen generate section="unique-id" format="list"-->
Generated content appears here
<!--/pytextgen-->
```

**Critical rules**:

- Do NOT modify section IDs or format specifiers
- Preserve opening/closing comment tags exactly
- Generated content between tags is replaced on regeneration

### Cloze markup

- `{@{ hidden text }@}`: Cloze deletion (text hidden in flashcard review)
- `::@::`: Separator between question and answer
- `:@:`: Alternative separator for Q&A flashcards

**Editing cloze markup**:

- Never escape or encode the braces/symbols
- Do not reflow text containing cloze markup across lines
- Preserve spacing inside `{@{ }@}`, around `::@::`, and around `:@:`

## Debugging generation issues

### Common errors

1. **Syntax errors in fence comments**:
   - Check for typos in `# pytextgen generate ...` lines
   - Verify module/function names are correct
   - Ensure data paths are relative and exist

2. **Fence delimiters broken**:
   - Ensure triple backticks are intact (not escaped)
   - Check language identifier matches expected format
   - Verify closing fence is present

3. **Cache issues**:
   - Use `-C` / `--no-cached` to rebuild `init.py` cache
   - Use `--no-code-cache` to bypass pytextgen compile cache
   - Check `__pycache__/` for stale compiled modules

4. **Cloze markup broken**:
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

- **Preserve fence syntax**: Never modify pytextgen comments or delimiters
- **Cache management**: Use `-C` when unsure if cache is stale
- **Incremental regeneration**: Pass specific paths to regenerate only changed files
- **Flashcard initialization**: Use `--init-flashcards` when creating new flashcard-enabled notes
- **Submodule updates**: If pytextgen behavior changes, check for submodule updates (`git submodule update --remote tools/pytextgen`)

## When to ask for help

- If fence syntax seems correct but generation fails, ask user to check pytextgen submodule version
- If editing is required in `tools/pytextgen/**`, ask user for permission (it's a submodule)
- If cache behavior is unexpected, clarify with user before deleting cache files

## Integration with other workflows

- **Wiki ingestion**: After running `convert wiki`, use `init generate` to create flashcards from cloze markup
- **Academic notes**: Use pytextgen to generate course indexes, assignment lists, or reference tables
- **Pack/publish**: Regenerate all content before packaging or publishing to ensure consistency
- **Note conventions**: See [markdown-notes](../../instructions/markdown-notes.instructions.md) for cloze markup preservation rules and the `templates` section of [tools/SKILL.md](../tools/SKILL.md) for fence templates
