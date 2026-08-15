---
name: wiki-ingestion
description: Ingest Wikipedia HTML, normalize links/media, archive to knowledge base, and fix capitalization in ingested notes (links, headers, stems) via convert_wiki --reprocess.
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
- Fixing capitalization in ingested notes (link targets, section headers, filename stems) — always via `convert_wiki --reprocess`, never by hand-editing the note, symlinks, or `name_map.jsonc`

## Detailed workflow

The workflow alternates between agent-run and human-run steps. After each manual step (marked with ⏸️), the user re-invokes this skill to continue. When resuming, the agent should ask the user which step to resume from and the file path of the note being ingested (`general/<dir_code>/<name>.md`). Common resume points: Step 2 after copying HTML, Step 5 after manual editing, Step 6 after review and capitalization fixes.

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

> __Important: Wikipedia article filenames keep spaces.__ The filename for a
> Wikipedia-derived note (e.g. `general/eng/Fourier transform.md`) must
> preserve spaces — never replace them with underscores. This is a hard rule:
> Wikipedia articles are stored with spaces in their filenames. Underscores
> in filenames are reserved for non-Wikipedia content (test fixtures, custom
> notes, internal references).

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

__Command__: `uv run -m scripts.convert_wiki --clipboard --output-mode append --output-file "<note_path>"`

Replace `<note_path>` with the path to the note file created in Step 1 (e.g. `general/eng/Fourier transform.md`).

- Always pass `--clipboard` (or `-c`): without it the script reads from stdin and blocks waiting for input.
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

#### Step 4a: Review capitalization (suggestions only, semantic)

Mechanical casing alignment — matching every link target and section header to existing files, `name_map` stems, and redirect targets — is `convert_wiki`'s job: it happens automatically at ingestion and via `--reprocess` for later fixes. The review below therefore checks only __semantic__ capitalization: whether the casing conveys the correct meaning. Never re-compare against files or `name_map`.

For every link target, section header at ALL levels (`#` through `######`), and the article filename stem, judge only the semantic correctness of the casing:

- __Proper nouns and eponyms__ — people's names, named theorems, principles, laws, and transforms, and adjectives derived from names — must be capitalized (e.g. `Newton's laws`, `D'Alembert's principle`, `Lagrange multipliers`, `Euler–Lagrange equations`, `Hamiltonian mechanics`, `Fourier analysis`, `Noether's theorem`, `Lagrangian point`).
- __Common descriptive phrases__ follow normal sentence case and need no review (e.g. `equations of motion`, `non-uniqueness`, `conservative force`); title case for such phrases is not an error.
- Flag only semantically wrong casing — most commonly a proper noun whose first letter was lowercased (e.g. `newton's laws` → `Newton's laws`). This typically happens when the term is absent from `name_map` and the converter's lowercase-first-char fallback damaged it.

Do __not__ flag: mechanical differences between link targets/headers and actual files or `name_map` stems (the converter guarantees these; `--reprocess` fixes them), link display text (preserved verbatim from Wikipedia), or style choices that are semantically acceptable.

Present findings in this standard, concise format (one line per finding, tagged by kind; no prose):

```text
Proposed capitalization fixes (suggestions only — not applied):
- link: `lagrangian point.md` → `Lagrangian point.md`
- header (`###`): `newton's laws` → `Newton's laws`
- stem: `modern physics` → `Modern physics`
```

or the single line `No capitalization fixes proposed.` when the review finds nothing.

__Hard rule:__ during this review pass the agent applies NOTHING — do not edit the note, do not run `--reprocess`, do not modify `name_map.jsonc`. The human decides during Step 5; approved suggestions are applied by the tool in Step 6b. Notes, symlinks, and `name_map.jsonc` are never hand-edited at any point.

### Step 5: Manual review and editing

⏸️ __Stop here.__ Let humans review the Markdown output manually, fix formatting issues, add flashcards (cloze or QA markup), review the Step 4a suggestions (accepting or rejecting each), and make any other edits. The agent should not perform these tasks.

When re-invoking the skill to continue, tell the agent the file path of the note being reviewed and that manual editing (including the Step 4a suggestion decisions) is complete.

### Step 6: Review and finalize

#### Step 6a: Review and finalize

- Review `aliases` and `tags` in YAML frontmatter
- Ensure all media references are correct (check `archives/Wikimedia Commons/`)
- Ensure the note is complete before committing

#### Step 6b: Apply capitalization fixes (always via the tool)

__First rule:__ whenever the user asks to fix capitalization (in this note or any other), run `uv run -m scripts.convert_wiki --reprocess --mapping ...` — do NOT hand-edit markdown link targets, section headers, symlinks, or `name_map.jsonc`. The tool updates `name_map.jsonc`, reconciles redirect symlinks, and rewrites link targets and section headers at all levels.

__Do not think — execute immediately.__ When the user asks to fix capitalization, map each provided fix verbatim to a `--mapping "FROM" "TO"` flag pair and run the tool. No deliberation about the fixes' correctness, no occurrence enumeration, no planning — the `--dry-run` report (run first) is the only analysis ever needed. Consult the __4 title variants per stem__ convention (below) only when the report shows unmatched variants.

__The only allowed thought: misspellings.__ Before running the tool, scan every term in the user's fix list for misspellings (e.g. `newton's lawes`). If any term appears misspelled, prompt the user whether the misspelling is intended — proceed verbatim if intended, corrected if not. The tool never validates `--mapping` TITLEs: a typo silently pollutes `name_map.jsonc` and can rewrite links to a wrong stem, so this check is the only guard.

__Always pass the note being ingested via `--article "<note_path>"`:__ the tool only rewrites links/headers in the listed articles, so omitting `--article` leaves the ingested note's own link targets and section headers untouched.

Run this when Step 5 review finds semantically wrong link-target casing, semantically wrong section-header casing at any level (`#` through `######`), or a semantically wrong filename stem — including the suggestions accepted from Step 4a. Mechanical alignment fixes are not reviewed or fixed here; `convert_wiki` already handles them. The same `--reprocess` command applies for ad-hoc fixes outside the ingestion workflow.

1. Map each provided fix directly to `--mapping "FROM" "TO"` — no transformation, no analysis. Use repeated `--mapping` flags for multiple fixes, or a single `--mapping-file` JSONC object (not both). Only if the `--dry-run` report shows unmatched variants, add the missing __4 title variants per stem__ entries (see [Reference: name_map mechanism](#reference-name_map-mechanism-in-convert_wikipy) below).
2. Preview with dry-run, always including `--article "<note_path>"`:

```bash
uv run -m scripts.convert_wiki --reprocess \
  --mapping "Modern physics" "Modern physics" \
  --article "<note_path>" \
  --dry-run
```

1. Apply when the dry-run report looks correct, keeping `--article "<note_path>"`:

```bash
uv run -m scripts.convert_wiki --reprocess \
  --mapping "Modern physics" "Modern physics" \
  --article "<note_path>"
```

Replace `<note_path>` with the note from Step 1 (e.g. `general/eng/modern physics.md`). `--article` accepts a stem or path.

__Anti-pattern:__ do NOT grep/sed/readlink the note to enumerate occurrences of wrong casing — the `--dry-run` report IS the analysis. Run `--dry-run` first and read its report.

| Situation | Flags |
| --------- | ----- |
| Fix only the article being ingested | `--mapping TITLE STEM` + `--article` |
| Multiple title variants for one stem | repeat `--mapping TITLE STEM`, or use `--mapping-file` |
| Same mapping affects links in other notes too | add `--update-links` |
| Update name_map / symlinks only (no body edits) | `--mapping` or `--mapping-file` only (no `--article`) |
| Preview before writing | `--dry-run` |

`--mapping` and `--mapping-file` are mutually exclusive. At least one of `--mapping`, `--mapping-file`, or `--article` is required.

`--reprocess` updates `name_map.jsonc`, reconciles redirect symlinks as-if the mappings existed at ingestion, and rewrites markdown link targets and section headers at all levels (`#`-`######`) — it does __not__ re-fetch Wikipedia HTML and is not a substitute for Step 3. Merge precedence: `effective_map = base_names_map | cli_pairs` (inline `--mapping`) or `base_names_map | file_mappings` (`--mapping-file`).

| Invariant | Rule |
| --------- | ---- |
| Real files | `.md` files are never deleted or overwritten by symlink operations |
| Symlinks | Created, retargeted, or removed only when `from_stem != to_stem` |
| Markdown | Link targets and section headers at all levels (`#`-`######`); flashcard `{@{...}@}` preserved |
| Collisions | Rename collisions raise before any markdown rewrites |

Stem migration compares `_stem_for_title(title, base_map)` vs `_stem_for_title(title, effective_map)` for titles in the redirect cache, effective map, and listed articles. Example: mapping `"Modern physics": "modern physics"` → `"Modern physics": "Modern physics"` renames `general/eng/modern physics.md` to `Modern physics.md`, updates link targets, and removes the redirect symlink when from == to.

Apply order: persist map → symlink actions → file renames → markdown rewrites (sequential, not transactional). Add `--update-links` for corpus-wide link fixes; use `--mapping-file` for batch variant entries.

When re-invoking the skill to continue, tell the agent the file path of the note and that Step 6 (review and any capitalization fixes) is complete.

### Step 7: Commit the note

Stage all ingestion changes (note, symlinks, archives, `name_map` updates).

The agent __must ask the user__ for at least two of the three flashcard count values (`Flashcards-prev`, `Flashcards-now`, `Flashcards-delta`). The agent must __not__ compute these values itself.

Use [commit-staged-flashcard-notes](../prompts/commit-staged-flashcard-notes.prompt.md) only for staging inspection and note counts (added / edited / deleted under `general/`, `special/`, `self/`). __Do not__ use that prompt's default commit header — wiki ingestion uses the format below.

__Commit message format__ (validate with `bun x commitlint` before committing; wrap lines to 72 characters or fewer):

1. __Header__ — article filename from Step 1, not a count summary:

   ```text
   feat(notes): add `<name>.md`
   ```

   Use the Step 1 note filename (e.g. `modern physics.md`), wrapped in backticks.

2. __Body__ — immediately after the header:
   - Count line(s) using the commit-staged wording (`add <N> note(s)`, `edit <M> note(s)`, `delete <D> note(s)`; only nonzero counts; semicolon-separated when multiple). Keep these on their own line(s), separate from the prose below.
   - A blank line.
   - One brief sentence in natural English stating which article was ingested (e.g. `Ingested the modern physics article from Wikipedia.`). Do not list generic ingestion mechanics (flashcards, symlinks, archives) — every wiki ingestion includes those.

3. __Footer__ — flashcard trailers when applicable (see [commit-convention](../instructions/commit-convention.instructions.md)): `Flashcards-delta`, `Flashcards-prev`, `Flashcards-now` as plain ASCII key/value pairs, one per line.

Full example:

```text
feat(notes): add `modern physics.md`

Add 18 note(s).

Ingested the modern physics article from Wikipedia.

Flashcards-delta: 0
Flashcards-prev: 0
Flashcards-now: 0
```

Present the proposed commit message to the user for confirmation before committing.

## Post-ingestion checks

- __Media archives__: Ensure all images/files are downloaded to `archives/Wikimedia Commons/` with `%20`-encoded filenames. If downloads fail, check that clipboard HTML was complete and retry `convert_wiki`.
- __Link normalization__: Use relative paths only; verify `%20` encoding for spaces (not `%3A` or other encodings).
- __Formatting__: Simplify complex tables/lists if needed; respect `.markdownlint.json` settings.
- __Frontmatter__: Follow [markdown-notes](../instructions/markdown-notes.instructions.md) conventions for `aliases` and `tags`.
- __Attribution__: Preserve the Wikipedia source URL in frontmatter or as an HTML comment.
- __Editing rules__: See [editing-conventions](../instructions/editing-conventions.instructions.md) for general rules when editing imported notes.
- __Redirect symlinks__: Redirect symlinks may point at articles not yet ingested. The `check-symlinks` pre-commit hook excludes `general/`; dangling wiki redirects are intentional.

## Maintenance: update redirect symlinks

Wikipedia redirects change over time: a redirect may retarget, become a full article, or a full article may become a redirect. Run this maintenance mode to reconcile the redirect symlinks in `general/` against the live Wikipedia API:

__Command__: `uv run -m scripts.convert_wiki --update-redirects`

- Scans every language subdirectory of `general/` for `*.md` symlinks
- Retargets symlinks whose Wikipedia redirect target changed (prefers the final target of a redirect chain when the first hop is not ingested locally)
- Removes symlinks for titles that became full articles
- Leaves missing pages and real files untouched — an article that became a redirect is never changed
- Refreshes the redirect cache so subsequent ingestion stays consistent

Add `--dry-run` to report what would change without modifying anything:

__Command__: `uv run -m scripts.convert_wiki --update-redirects --dry-run`

The `--dry-run` flag has no effect without `--update-redirects`. The report prints scan/retarget/remove/keep counts and the list of changed titles to stdout.

## Reference: name_map mechanism in `convert_wiki.py`

The name_map is a `dict[str, str]` that maps Wikipedia page titles (or variants) to
local filename stems used in `general/eng/`. It ensures links and section headers at
ALL levels (h1-h6) in ingested Wikipedia articles use the correct casing to match
actual `general/eng/*.md` files.

### How entries are maintained (`_load_names_map`)

All entries live in `scripts/assets/convert_wiki.name_map.jsonc`. The map is loaded at
import time with no filesystem scan. Redirect symlinks under `general/` still exist for
navigation, but they no longer feed name_map implicitly.

When adding or fixing entries manually, use the __4 title variants per filename stem__
convention (especially for redirect source titles):

| Key (Wikipedia-style title)                                             | Value (local filename stem)             |
| ----------------------------------------------------------------------- | --------------------------------------- |
| `Three-dimensional space (mathematics)`                                 | `Three-dimensional space (mathematics)` |
| `Three-dimensional space (mathematics)` with `'`→`’` (curly apostrophe) | same with curly apostrophe              |
| `three-...` (first char lowercased)                                     | `Three-dimensional space (mathematics)` |
| lowercased + curly apostrophe variant                                   | same with curly apostrophe              |

Add explicit JSONC entries when `_fix_name_maybe` heuristics are insufficient.

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

| Call site                        | `replace_underscores` | Input                                            |
| -------------------------------- | --------------------- | ------------------------------------------------ |
| `_handle_header`                 | `False`               | Section header text (all heading levels, h1-h6)  |
| `_handle_anchor` — `title` param | `True`                | Link display text / page title                   |
| `_handle_anchor` — `to` param    | `True`                | Redirect-resolved target filename                |
| `_handle_anchor` — `to_fragment` | `True`                | `#fragment` part of link                         |

During `--reprocess`, the effective name_map is re-applied to every section header
at all levels (`_rewrite_markdown_headings`) and to link targets, so capitalization
fixes accepted in Step 5 propagate to already-ingested notes.

__Critical__: `title` and `to` are independent inputs — `title` is the `<a>` tag's
`title` attribute, `to` is `redirect_map[title].to`. Both go through the same
`_fix_name_maybe` independently. A name_map entry covering the display text does
NOT cover the link target; both need separate entries if they differ.

### Snapshot tests and `aux.json`

The snapshot test uses `tests/scripts/convert_wiki/snapshots/<name>.aux.json` together with the shared `name_map.jsonc` baseline (a symlink to `scripts/assets/convert_wiki.name_map.jsonc`). Per-test overrides use `name_map_overrides`:

```json
{
  "redirect_cache": { "Wikipedia title": {"to": "...", "tofragment": ""} },
  "name_map_overrides": { "Fourier transform": "Fourier transform" },
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
