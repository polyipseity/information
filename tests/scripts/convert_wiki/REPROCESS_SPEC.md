# Reprocess mode specification

`convert_wiki --reprocess` fixes outdated `name_map` entries after manual review. It updates the JSONC map, reconciles redirect symlinks as-if the new mappings existed at ingestion, and rewrites markdown link targets without re-running the HTML pipeline (flashcards preserved).

## Inputs

| Input | Semantics |
| ----- | --------- |
| `--mapping KEY=VALUE` | Repeatable; title variant → canonical local stem (same as `name_map.jsonc`) |
| `--mapping-file` | JSONC object merged before CLI mappings (CLI wins on conflict) |
| `--article` | Repeatable; stem or path under `general/` |
| `--update-links` | Rewrite link targets in all `general/**/*.md` real files |
| `--dry-run` | Plan only; no writes |

At least one of `--mapping`, `--mapping-file`, or `--article` is required.

## Merge precedence

```text
effective_map = base_names_map | file_mappings | cli_mappings
```

Later sources override earlier ones.

## Invariants

1. Real `.md` files are never deleted or overwritten by symlink operations.
2. Redirect symlinks are created, retargeted, or removed only when `from_stem != to_stem` (or the inverse when they become equal).
3. Markdown rewrite changes link targets and the first `#` heading only; flashcard delimiters `{@{...}@}` and other prose stay intact.
4. Rename collisions raise an error before any markdown rewrites run.

## Stem migration

For each title in `redirect_cache.keys() ∪ effective_map.keys() ∪ article_titles`:

```python
old_stem = _stem_for_title(title, base_map)
new_stem = _stem_for_title(title, effective_map)
```

When `old_stem != new_stem`, record `old_stem → new_stem` for link rewriting.

### Worked example

| Field | Before | After |
| ----- | ------ | ----- |
| Mapping | `"Modern physics": "modern physics"` | `"Modern physics": "Modern physics"` |
| Article file | `general/eng/modern physics.md` | `general/eng/Modern physics.md` |
| Link target | `modern%20physics.md` | `Modern%20physics.md` |
| Symlink | `Modern physics.md → modern physics.md` | removed (from == to under new map) |

## Symlink decision table

Derived from `_handle_link` + redirect cache (not live API):

| Condition | Action |
| --------- | ------ |
| `from_stem != to_stem` and no symlink | create |
| `from_stem != to_stem` and symlink points elsewhere | retarget |
| `from_stem == to_stem` and symlink exists | remove |
| Real file at path | never touch |

Chain preference: when first-hop target file is absent locally but `final_to` stem exists, use `final_to` (same as `--update-redirects`).

## Markdown rewrite rules

1. Match markdown link targets `](<path>.md[#fragment])`.
2. Decode `%20` to spaces; apply stem migration; re-encode with `_markdown_link_target` rules.
3. Preserve `#fragment` unchanged.
4. Replace the first `# heading` after YAML frontmatter (if present) when reprocessing a listed article.

## Apply order

1. Persist `effective_map` to JSONC and reload module map.
2. Symlink actions.
3. File renames (listed articles).
4. Markdown rewrites.

Operations are sequential, not transactional across the whole run.

## CLI examples

```bash
# Mapping + one article
uv run -m scripts.convert_wiki --reprocess \
  --mapping "Modern physics=Modern physics" \
  --article "modern physics"

# Mapping only (name_map + symlinks)
uv run -m scripts.convert_wiki --reprocess \
  --mapping "Modern physics=Modern physics"

# Corpus-wide link fixes
uv run -m scripts.convert_wiki --reprocess \
  --mapping "Modern physics=Modern physics" \
  --update-links

# Preview
uv run -m scripts.convert_wiki --reprocess \
  --mapping "Modern physics=Modern physics" \
  --dry-run
```
