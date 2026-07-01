---
name: wiki-ingestion
description: Ingest Wikipedia HTML, normalize links/media, and archive to knowledge base.
---

# Wiki Ingestion Workflow

> __Continuous improvement:__ see `continuous_improvement.md` in this
> folder for a running log of lessons learned and guidance on evolving
> the wiki-ingestion skill.

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

__Command__: `uv run -m templates.new_wiki_page`

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
- __Action__: Paste into new file `general/Article Name.md` (or `special/` if specialized content)

### Step 2: Copy Wikipedia HTML to clipboard

- Open Wikipedia article in browser
- Select all content (Ctrl+A or Cmd+A)
- Copy (Ctrl+C or Cmd+C)
- Content is now in clipboard

### Step 3: Ingest HTML

__Command__: `uv run -m convert_wiki`

- Tool reads from clipboard
- Normalizes Markdown formatting (lists, tables, code, emphasis)
- Downloads images to `archives/Wikimedia Commons/` using `convert_wiki.filename_rename_map.jsonc` for filename renames
- Normalizes links to relative paths with `%20` encoding (not `%3A` or other encodings)
- Outputs Markdown that preserves Wikipedia structure
- __Action__: Paste output below the frontmatter in your note file

### Step 4: Flashcard state

Flashcard creation is managed automatically by the repository’s build
workflows; agents and authors are not expected to run any commands to
produce flashcards. The generator scans for three kinds of markup:

- `{@{ hidden text }@}` for cloze deletions (hide text within a paragraph),
- `::@::` for two-sided question/answer pairs (line-only, two cards), and
- `:@:` for one-sided question/answer pairs (line-only, single card).

The source must honour the single‑line restriction for the latter two
formats; use `<br/>` or `<p>` for any desired visual breaks. When you add
these markers, the build updates pytextgen regions behind the scenes. See
[pytextgen](../pytextgen/SKILL.md) skill for additional details.

### Step 5: Review and finalize

- Review `aliases` and `tags` in YAML frontmatter
- Ensure all media references are correct (check `archives/Wikimedia Commons/`)
- Verify cloze markup is added to key terms
- Trust the automated build process to regenerate flashcards; there is no
  need for manual commands.
- Commit when satisfied

## Best practices

- __Check media archives__: Ensure all images/files downloaded to `archives/Wikimedia Commons/` with `%20`-encoded filenames
- __Verify link normalization__: Relative paths only; no external URLs unless absolutely necessary
- __YAML structure__: Use [markdown-notes](../instructions/markdown-notes.instructions.md) conventions for `aliases` and `tags`
- __Keep attribution__: Preserve Wikipedia source URL in frontmatter or as HTML comment
- __Review formatting__: Simplify complex tables/lists if needed; respect `.markdownlint.json` settings
- __Test generation__: This is handled by CI/build automatically; the agent
  should not run the generator manually when verifying edits.
- __Add cloze markup__: Manually annotate key terms with `{@{ }@}`, `::@::`, or `:@:` for active recall

## Common issues

1. __Media download failures__: Check if clipboard HTML is complete; retry `convert_wiki`
2. __Broken relative links__: Verify `%20` encoding for spaces (not `%3A` or other encodings)
3. __Complex tables__: Some Wikipedia tables don't convert well; manually edit to simpler Markdown format
4. __Cloze markup missing__: Manually add after generation; see [pytextgen](../pytextgen/SKILL.md) skill for syntax

## Integration

- __Note scaffolding__: Use [tools/SKILL.md](../tools/SKILL.md) (templates section) to understand frontmatter conventions
- __Flashcard generation__: Use [pytextgen](../pytextgen/SKILL.md) to regenerate cloze markup into flashcards
- __Edit conventions__: See [editing-conventions](../instructions/editing-conventions.instructions.md) for general rules while editing imported notes

## Typical command pattern

```bash
# Ingest from clipboard
uv run -m convert_wiki

# Scaffold new wiki-sourced note
uv run -m templates.new_wiki_page
```
