---
name: wiki-ingestion
description: Ingest Wikipedia HTML, normalize links/media, and archive to knowledge base.
---

# Wiki Ingestion Workflow

> __Continuous improvement:__ see `continuous_improvement.md` in this folder for a running log of lessons learned and guidance on evolving the wiki-ingestion skill.

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

The workflow alternates between agent-run and human-run steps. After each manual step (marked with ⏸️), the user re-invokes this skill to continue. When resuming, the agent should ask the user:

- Which step to resume from
- The file path of the note being ingested (`general/<dir_code>/<name>.md`)

### Step 1: Scaffold new note

__Command__: `uv run -m templates.new_wiki_page`

The script prompts for two inputs, then atomically creates the note file and a symlink.

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
2. Matched against pycountry: first tries `alpha_2` (ISO 639‑1), then `alpha_3` (ISO 639‑3).
3. Directory code uses the **longest available** code via the fallback chain: ``alpha_3`` → ``alpha_2``. This ensures 3-letter codes are preferred when they exist.
4. Human-readable name is taken from `lang.name`.
5. The corresponding subdirectory under `general/` must already exist (e.g. `general/eng/`, `general/zho/`).

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

- **Note file**: `general/<dir_code>/<name>.md` — contains the YAML frontmatter and the attribution footer.
- **Symlink**: `general/<name>.md` → `<dir_code>/<name>.md` — a relative symlink at the top level of `general/` for convenient access.
- **Atomicity**: Both files are written to temporary paths first, then atomically renamed into place. If either operation fails, both files are cleaned up — the creation either succeeds completely or has no effect.

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

Note the created file path — you will need it when re-invoking the skill after later manual steps.

### Step 2: Copy Wikipedia HTML to clipboard

- Open Wikipedia article in browser
- Select all content (Ctrl+A or Cmd+A)
- Copy (Ctrl+C or Cmd+C)
- Content is now in clipboard

⏸️ **Stop here.** The agent cannot perform this step. A human must manually copy the article content from the Wikipedia page. Resume once the HTML is in the clipboard.

When re-invoking the skill to continue, tell the agent the file path of the note being ingested and that Step 2 (copying HTML) is done.

### Step 3: Ingest HTML

__Command__: `uv run -m convert_wiki`

- Tool reads from clipboard
- Normalizes Markdown formatting (lists, tables, code, emphasis)
- Downloads images to `archives/Wikimedia Commons/` using `convert_wiki.filename_rename_map.jsonc` for filename renames
- Normalizes links to relative paths with `%20` encoding (not `%3A` or other encodings)
- Outputs Markdown that preserves Wikipedia structure
- __Action__: Paste output below the frontmatter in your note file

### Step 4: Clean up Markdown

This step is empty for now.

### Step 5: Manual review and editing

⏸️ **Stop here.** Let humans review the Markdown output manually, fix formatting issues, add flashcards (cloze or QA markup), and make any other edits. The agent should not perform these tasks.

When re-invoking the skill to continue, tell the agent the file path of the note being reviewed and that manual editing is complete.

### Step 6: Review and finalize

- Review `aliases` and `tags` in YAML frontmatter
- Ensure all media references are correct (check `archives/Wikimedia Commons/`)
- Ensure the note is complete before committing

### Step 7: Commit the note

Stage and commit the new note using the [commit-staged-flashcard-notes](../prompts/commit-staged-flashcard-notes.prompt.md) prompt.

The agent __must ask the user__ to provide at least two of the three flashcard count values (`Flashcards-prev`, `Flashcards-now`, `Flashcards-delta`). The agent must __not__ compute these values itself. The agent then follows the commit-staged-flashcard-notes workflow to compose and create the commit.

## Post-ingestion checks

- __Media archives__: Ensure all images/files are downloaded to `archives/Wikimedia Commons/` with `%20`-encoded filenames. If downloads fail, check that clipboard HTML was complete and retry `convert_wiki`.
- __Link normalization__: Use relative paths only; verify `%20` encoding for spaces (not `%3A` or other encodings).
- __Formatting__: Simplify complex tables/lists if needed; respect `.markdownlint.json` settings.
- __Frontmatter__: Follow [markdown-notes](../instructions/markdown-notes.instructions.md) conventions for `aliases` and `tags`.
- __Attribution__: Preserve the Wikipedia source URL in frontmatter or as an HTML comment.
- __Editing rules__: See [editing-conventions](../instructions/editing-conventions.instructions.md) for general rules when editing imported notes.
