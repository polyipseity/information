---
name: Archives structure
description: Guidelines for archives/ organization, content storage, and index.md maintenance
applyTo: "archives/**/*.md"
---

# Archives Structure & Guidelines

## General Principles

- __Permanence__: Once archived, files should remain stable (no renaming/deletion without good reason)
- __Index maintenance__: Every archive subdirectory has `index.md` with metadata (source URL, timestamp, description, optional hash)
- __Relative links__: Notes reference archived files using relative paths with `%20` encoding
- __Organization__: Group related content into subdirectories; use descriptive or content-addressed filenames as appropriate

## Current Subdirectories

- `archives/Wikimedia Commons/`: Media (images, audio, video) sourced from Wikimedia Commons
    - Filenames: Descriptive names for easy identification (e.g., `04 production-possibilities-frontier-1.png`)
    - May be renamed via `scripts/assets/convert_wiki.name_map.jsonc` during Wikipedia ingestion

- `archives/sparse/`: Miscellaneous archived content with user-defined filenames
    - __Important__: Filenames are user-defined (descriptive or arbitrary), NOT automatically SHA-256 hashed
    - Users manually add files with chosen filenames
    - Entry in `index.md` must include source URL, timestamp, and description

## index.md Format

__Required metadata for each entry__:

- Filename (as Markdown link)
- Description (brief summary)
- Source (original URL or provenance)
- Timestamp (download/archive date)
- Hash (optional; SHA-256 for verification)
- License (optional; for Wikimedia Commons media)

__Example__:

```markdown
- [example-article.md](example-article.md) — Archived blog post about X
  - Source: https://example.com/blog/article
  - Downloaded: 2024-01-20
```

## Developer tooling

Tools writing to `archives/` must include tests (use `tmp_path: os.PathLike[str]`, convert paths with `os.fspath(path_like)`). Follow repo AnyIO/Asyncer conventions for async tools. Document invariants in `archives/index.md`.
