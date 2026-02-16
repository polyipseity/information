---
name: wiki-ingestion
description: Ingest Wikipedia HTML, normalize links/media, and archive to knowledge base.
---

# Wiki Ingestion Workflow

Use this skill when importing Wikipedia articles or converting HTML content into Markdown notes.

## What wiki ingestion does

Converts Wikipedia HTML (or similar web content) into well-formed Markdown with:

- Normalized relative links (URL-encoded with `%20` for spaces)
- Media references extracted to `archives/Wikimedia Commons/`
- YAML frontmatter scaffolding for new notes
- Markdown table and list conversion

## When to use

- Importing encyclopedia articles from Wikipedia verbatim
- Converting web pages to Markdown for knowledge base
- Extracting and organizing media from online sources
- Creating new notes with pre-filled structure from web content

## Detailed workflow

### Step 1: Scaffold new note

**Command**: `uv run -m "templates.new wiki page"`

- Script prompts for Wikipedia article name (e.g., "Fourier Transform")
- Generates YAML frontmatter template:

  ```yaml
  ---
  aliases: [Alternative name]
  tags: [flashcard/active, language/in/English]
  ---
  ```

- Adds Wikipedia link comment: `<!-- Source: https://en.wikipedia.org/wiki/Article_Name -->`
- Copies template to clipboard
- **Action**: Paste into new file `general/Article Name.md` (or `special/` if specialized content)

### Step 2: Copy Wikipedia HTML to clipboard

- Open Wikipedia article in browser
- Select all content (Ctrl+A or Cmd+A)
- Copy (Ctrl+C or Cmd+C)
- Content is now in clipboard

### Step 3: Ingest HTML

**Command**: `uv run -m "convert wiki"`

- Tool reads from clipboard
- Normalizes Markdown formatting (lists, tables, code, emphasis)
- Downloads images to `archives/Wikimedia Commons/` using `convert wiki.py.names map.json` for filename renames
- Normalizes links to relative paths with `%20` encoding (not `%3A` or other encodings)
- Outputs Markdown that preserves Wikipedia structure
- **Action**: Paste output below the frontmatter in your note file

### Step 4: Generate flashcards

**Command**: `uv run -m init generate <file>`

- Scans note for cloze markup: `{@{ hidden text }@}`, `::@::`, `:@:`
- Generates spaced-repetition flashcard state
- Inserts generated flashcard regions marked with `<!--pytextgen generate section=...-->`
- See [pytextgen](../pytextgen/SKILL.md) skill for details

### Step 5: Review and finalize

- Review `aliases` and `tags` in YAML frontmatter
- Ensure all media references are correct (check `archives/Wikimedia Commons/`)
- Verify cloze markup is added to key terms
- Test regeneration: `uv run -m init generate -C <file>`
- Commit when satisfied

## Best practices

- **Check media archives**: Ensure all images/files downloaded to `archives/Wikimedia Commons/` with `%20`-encoded filenames
- **Verify link normalization**: Relative paths only; no external URLs unless absolutely necessary
- **YAML structure**: Use [markdown-notes](../instructions/markdown-notes.instructions.md) conventions for `aliases` and `tags`
- **Keep attribution**: Preserve Wikipedia source URL in frontmatter or as HTML comment
- **Review formatting**: Simplify complex tables/lists if needed; respect `.markdownlint.json` settings
- **Test generation**: After editing, run `python -m init generate <file>` to verify flashcard creation
- **Add cloze markup**: Manually annotate key terms with `{@{ }@}`, `::@::`, or `:@:` for active recall

## Common issues

1. **Media download failures**: Check if clipboard HTML is complete; retry `convert wiki`
2. **Broken relative links**: Verify `%20` encoding for spaces (not `%3A` or other encodings)
3. **Complex tables**: Some Wikipedia tables don't convert well; manually edit to simpler Markdown format
4. **Cloze markup missing**: Manually add after generation; see [pytextgen](../pytextgen/SKILL.md) skill for syntax

## Integration

- **Note scaffolding**: Use [tools-templates](../tools-templates/SKILL.md) to understand frontmatter conventions
- **Flashcard generation**: Use [pytextgen](../pytextgen/SKILL.md) to regenerate cloze markup into flashcards
- **Edit conventions**: See [editing-conventions](../instructions/editing-conventions.instructions.md) for general rules while editing imported notes

## Typical command pattern

```bash
# Ingest from clipboard
uv run -m "convert wiki"

# Scaffold new wiki-sourced note
uv run -m "templates.new wiki page"
```
