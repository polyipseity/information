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

__Command__: `uv run -m scripts.new_wiki_page`

The script prompts for two inputs, then atomically creates the note file and a symlink.

#### Inputs

| Prompt                 | Default | Example                                 | Notes                                                                                                                         |
| ---------------------- | ------- | --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `Language? (ISO code)` | `eng`   | `eng`, `en`, `zho`, `deu`, `fra`        | Case-insensitive. Accepts ISO 639‑1 (2‑letter), ISO 639‑2 (3‑letter), or ISO 639‑3 (3‑letter) codes. Validated via pycountry. |
| `Name?`                | —       | `Fourier transform`, `machine learning` | The Wikipedia article title — not URL-encoded, no underscores. Cannot be empty.                                               |

#### Transformations applied to the article name

| Output field           | How it is derived                                                                                                   | Example (`Fourier transform (disambiguation)`)                              |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| __Wikipedia URL name__ | Spaces → underscores (used for `<!-- Source: -->` comment).                                                         | `Fourier_transform_(disambiguation)`                                        |
| __Title__              | Trailing parenthetical disambiguation is stripped via regex `\s\([^()]+\)$`.                                        | `Fourier transform`                                                         |
| __Tag name__           | Non-alphanumeric chars → `_` (except `–`/`—` → `-`). Falls back to `{title}_` if result is empty or purely numeric. | `Fourier_transform_(disambiguation)` → `Fourier_transform__disambiguation_` |

#### Language code resolution

1. Input is stripped and lowercased.
2. Matched against pycountry: first tries `alpha_2` (ISO 639‑1), then `alpha_3` (ISO 639‑3).
3. Directory code uses the __longest available__ code via the fallback chain: `alpha_3` → `alpha_2`. This ensures 3-letter codes are preferred when they exist.
4. Human-readable name is taken from `lang.name`.
5. The corresponding subdirectory under `general/` must already exist (e.g. `general/eng/`, `general/zho/`).

#### Generated YAML frontmatter

```yaml
---
aliases:
  - { title } # Title derived from the article name (disambiguation stripped)
tags:
  - flashcard/active/general/{dir_code}/{tag_name}
  - language/in/{lang_name} # Human language name (e.g. "English", "Chinese")
---
```

| Placeholder   | Source                                            | Example              |
| ------------- | ------------------------------------------------- | -------------------- |
| `{title}`     | Article name with trailing parenthetical stripped | `Fourier transform`  |
| `{dir_code}`  | Language ISO code (3-letter preferred)            | `eng`, `zho`         |
| `{tag_name}`  | Article name sanitised for tag use                | `Fourier_transform`  |
| `{lang_name}` | Human-readable language name from pycountry       | `English`, `Chinese` |

#### File layout

- __Note file__: `general/<dir_code>/<name>.md` — contains the YAML frontmatter and the attribution footer.
- __Symlink__: `general/<name>.md` → `<dir_code>/<name>.md` — a relative symlink at the top level of `general/` for convenient access.
- __Atomicity__: Both files are written to temporary paths first, then atomically renamed into place. If either operation fails, both files are cleaned up — the creation either succeeds completely or has no effect.

#### Example walkthrough

```text
$ uv run -m scripts.new_wiki_page
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

This text incorporates [content](https://zh.wikipedia.org/wiki/Fourier_transform) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
```

And `general/Fourier transform.md` → `zho/Fourier transform.md` (relative symlink).

Note the created file path — you will need it when re-invoking the skill after later manual steps.

### Step 2: Copy Wikipedia HTML to clipboard

The agent constructs the Wikipedia URL from the article name (provided in Step 1) by replacing spaces with underscores and using the language selected in Step 1 to determine the subdomain: `https://{<wikipedia_lang>}.wikipedia.org/wiki/{<article_name>}`. Wikipedia uses 2-letter ISO 639-1 codes for language subdomains (e.g., `en.wikipedia.org` for English, `zh.wikipedia.org` for Chinese, `de.wikipedia.org` for German). Present it as a clickable Markdown link.

For example, if the article name is `Fourier transform` and the language is English:

→ [`Fourier transform`](https://en.wikipedia.org/wiki/Fourier_transform)

Then instruct the user:

1. Click the link above to open the article in your browser.
2. Select all content (Ctrl+A on Windows/Linux, Cmd+A on macOS).
3. Copy (Ctrl+C on Windows/Linux, Cmd+C on macOS).

⏸️ __Stop here.__ This step requires human action. Open the link, select all content, and copy the HTML. Resume once the HTML is in the clipboard.

When re-invoking the skill to continue, tell the agent the file path of the note being ingested (`general/<dir_code>/<name>.md`) and that Step 2 (copying HTML) is done.

### Step 3: Ingest HTML

__Command__: `uv run -m scripts.convert_wiki --output-mode append --output-file "<note_path>"`

Replace `<note_path>` with the path to the note file created in Step 1 (e.g. `general/eng/Fourier transform.md`).

- Tool reads from clipboard
- Normalizes Markdown formatting (lists, tables, code, emphasis)
- Downloads images to `archives/Wikimedia Commons/` using `scripts/assets/convert_wiki.name_map.jsonc` for filename renames
- Normalizes links to relative paths with `%20` encoding (not `%3A` or other encodings)
- Outputs Markdown that preserves Wikipedia structure
- The script appends the generated Markdown directly to your note file.

### Step 4: Clean up Markdown

#### Merge `## references` sections

After pasting, the file has two `## references` sections: the __template section__ (top, contains the CC-BY-SA attribution) and the __Wikipedia section__ (inside the pasted content, may contain external links / footnotes). The pasted content is everything after the template's `## references`.

1. Search for `## references` only within the __pasted Wikipedia content__ (i.e. after the template's `## references`). Find the __last__ occurrence in that region — this is the Wikipedia references heading. If there is none, skip to step 4.
2. Prepend the template's reference content (everything between the template's `## references` heading and the pasted content) to the Wikipedia `## references` section: insert it right after the heading line, with a blank line between heading and content. Preserve the exact text and line breaks of the template's attribution.
3. Delete the template's `## references` section (heading + its content, including trailing blank line) from the top of the file.
4. If the pasted content has __no__ `## references`, leave the template's `## references` in place — the attribution stays at its current position.

### Step 5: Manual review and editing

⏸️ __Stop here.__ Let humans review the Markdown output manually, fix formatting issues, add flashcards (cloze or QA markup), and make any other edits. The agent should not perform these tasks.

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

## Reference: name_map mechanism in `convert_wiki.py`

The name_map is a `dict[str, str]` that maps Wikipedia page titles (or variants) to
local filename stems used in `general/eng/`. It ensures links and section headers in
ingested Wikipedia articles use the correct casing to match actual `general/eng/*.md` files.

### How entries are generated (`_build_names_map`)

Auto-discovers all `general/*/*.md` files, producing __4 entries per file__:

| Key (Wikipedia-style title)                                             | Value (local filename stem)             |
| ----------------------------------------------------------------------- | --------------------------------------- |
| `Three-dimensional space (mathematics)`                                 | `Three-dimensional space (mathematics)` |
| `Three-dimensional space (mathematics)` with `'`→`’` (curly apostrophe) | same with curly apostrophe              |
| `three-...` (first char lowercased)                                     | `Three-dimensional space (mathematics)` |
| lowercased + curly apostrophe variant                                   | same with curly apostrophe              |

Then merged with manual entries from `scripts/assets/convert_wiki.name_map.jsonc`.
Conflicting keys between auto and manual map raise `ValueError`.

### How lookup works (`_fix_name_maybe`)

```python
def _fix_name_maybe(name, *, normalize=True, replace_underscores=False, names_map=None):
```

The function applies a single sequential heuristic:

1. __Normalize__: replace ` ` (nbsp) → space if `normalize=True` (default).
2. __Exact lookup__ in `names_map` — if found, return immediately.
3. __Underscores__: if `replace_underscores=True`, replace `_` with space.
4. __Retry lookup__ with the (potentially underscore-replaced) name. If still not found,
   apply the __lowercase-first-char fallback__:
   `name[1:].islower() or len(name)≤1` → lowercase first char, else identity.

This lowercases the first character when the rest is all lowercase (normal English
capitalisation like `Fourier...` → `fourier...`), and leaves mixed-case names like
`iPhone` alone.

### Where `_fix_name_maybe` is called

| Call site                      | `replace_underscores` | Input                             |
| ------------------------------ | --------------------- | --------------------------------- |
| `_handle_header`               | `False`               | Section header text               |
| `_handle_link` — `title` param | `True`                | Link display text / page title    |
| `_handle_link` — `to` param    | `True`                | Redirect-resolved target filename |
| `_handle_link` — `to_fragment` | `True`                | `#fragment` part of link          |

__Critical__: `title` and `to` are independent inputs — `title` is the `<a>` tag's
`title` attribute, `to` is `redirect_map[title].to`. Both go through the same
`_fix_name_maybe` independently. A name_map entry covering the display text does
NOT cover the link target; both need separate entries if they differ.

### Snapshot tests and `aux.json`

The snapshot test uses `tests/scripts/test_convert_wiki/snapshots/<name>.aux.json`
to supply a pre-computed `name_map` isolating the test from the live filesystem:

```json
{
  "redirect_cache": { "Wikipedia title": {"to": "...", "tofragment": ""} },
  "name_map": { "Fourier transform": "Fourier transform", "fourier transform": "Fourier transform", ... },
  "image_metadata": {}
}
```

### Key gotchas

- __Headers vs links__: By convention, section headers never use underscore
  replacement (`replace_underscores=False`). Wikipedia section headings use
  spaces, not underscores, so any underscore in a header is a literal underscore
  and must not be converted. Links use `replace_underscores=True` because
  Wikipedia URLs encode spaces as underscores.
- __nbsp__: Non-breaking spaces (`\u00a0`) are normalized to regular space before
  lookup, but all other whitespace must match the key exactly.
- __Prettier + snapshot__: Running Prettier on `aux.json` reorders JSON keys,
  which can slightly alter pipeline output (table LaTeX wrapping). Always
  regenerate `expected.md` after running Prettier on `aux.json`.
- __Link target fixes__: When fixing link target casing, remember that the `to`
  parameter is passed through `_fix_name_maybe` independently — name_map entries
  must cover the Wikipedia title case of the target, not just the display text.
