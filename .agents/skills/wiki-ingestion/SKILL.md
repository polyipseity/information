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

The script prompts for two inputs, then atomically creates the note file and a
symlink.

#### Inputs

| Prompt | Default | Example | Notes |
|--------|---------|---------|-------|
| `Language? (ISO code)` | `eng` | `eng`, `en`, `zho`, `deu`, `fra` | Case-insensitive. Accepts ISO 639‑1 (2‑letter), ISO 639‑2 (3‑letter), or ISO 639‑3 (3‑letter) codes. Validated via pycountry. |
| `Name?` | — | `Fourier transform`, `machine learning` | The Wikipedia article title — not URL-encoded, no underscores. Cannot be empty. |

#### Transformations applied to the article name

| Output field | How it is derived | Example (`Fourier transform (disambiguation)`) |
|---|---|---|
| **Wikipedia URL name** | Spaces → underscores (used for ``<!-- Source: -->`` comment). | `Fourier_transform_(disambiguation)` |
| **Title** | Trailing parenthetical disambiguation is stripped via regex ``\s\([^()]+\)$``. | `Fourier transform` |
| **Tag name** | Non-alphanumeric chars → ``_`` (except ``–``/``—`` → ``-``). Falls back to ``{title}_`` if result is empty or purely numeric. | `Fourier_transform_(disambiguation)` → `Fourier_transform__disambiguation_` |

#### Language code resolution

1. Input is stripped and lowercased.
2. Matched against pycountry: first tries `alpha_2` (ISO 639‑1), then `alpha_3`
   (ISO 639‑3).
3. Directory code uses the **longest available** code via the fallback chain:
   ``alpha_3`` → ``alpha_2``. This ensures 3-letter codes are preferred when
   they exist.
4. Human-readable name is taken from `lang.name`.
5. The corresponding subdirectory under `general/` must already exist (e.g.
   `general/eng/`, `general/zho/`).

#### Generated YAML frontmatter

```yaml
---
aliases:
  - {title}           # Title derived from the article name (disambiguation stripped)
tags:
  - flashcard/active/general/{dir_code}/{tag_name}
  - language/in/{lang_name}   # Human language name (e.g. "English", "Chinese")
---
```

| Placeholder | Source | Example |
|---|---|---|
| `{title}` | Article name with trailing parenthetical stripped | `Fourier transform` |
| `{dir_code}` | Language ISO code (3-letter preferred) | `eng`, `zho` |
| `{tag_name}` | Article name sanitised for tag use | `Fourier_transform` |
| `{lang_name}` | Human-readable language name from pycountry | `English`, `Chinese` |

#### File layout

- **Note file**: `general/<dir_code>/<name>.md` — contains the YAML frontmatter
  and the attribution footer.
- **Symlink**: `general/<name>.md` → `<dir_code>/<name>.md` — a relative
  symlink at the top level of `general/` for convenient access.
- **Atomicity**: Both files are written to temporary paths first, then
  atomically renamed into place. If either operation fails, both files are
  cleaned up — the creation either succeeds completely or has no effect.

#### Example walkthrough

```
$ uv run -m templates.new_wiki_page
Language? (ISO code, default: eng) zho
Name? Fourier transform
Created: general/zho/Fourier transform.md
Symlink: general/Fourier transform.md -> zho/Fourier transform.md
```

Resulting `general/zho/Fourier transform.md`:

```yaml
---
aliases:
  - Fourier transform
tags:
  - flashcard/active/general/zho/Fourier_transform
  - language/in/Chinese
---

# Fourier transform

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Fourier_transform) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
```

And `general/Fourier transform.md` → `zho/Fourier transform.md` (relative symlink).

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

Flashcard creation is managed automatically by the repository's build workflows; agents and authors are not expected to run any commands to produce flashcards. The generator scans for three kinds of markup:

- `{@{ hidden text }@}` for cloze deletions (hide text within a paragraph),
- `::@::` for two-sided question/answer pairs (line-only, two cards), and
- `:@:` for one-sided question/answer pairs (line-only, single card).

The source must honour the single‑line restriction for the latter two formats; use `<br/>` or `<p>` for any desired visual breaks. When you add these markers, the build updates pytextgen regions behind the scenes. See [pytextgen](../pytextgen/SKILL.md) skill for additional details.

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
# Scaffold new wiki-sourced note (creates file + symlink)
uv run -m templates.new_wiki_page

# Ingest from clipboard
uv run -m convert_wiki
```
