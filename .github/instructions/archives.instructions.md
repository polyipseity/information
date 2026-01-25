---
name: Archives structure
description: Guidelines for archives/ organization, content storage, and index.md maintenance
applyTo: "archives/**/*.md"
---

## General Principles

- **Permanence**: Once archived, files should remain stable (no renaming/deletion without good reason)
- **Index maintenance**: Every archive subdirectory has `index.md` with metadata (source URL, timestamp, description, optional hash)
- **Relative links**: Notes reference archived files using relative paths with `%20` encoding
- **Organization**: Group related content into subdirectories; use descriptive or content-addressed filenames as appropriate

## Current Subdirectories

- `archives/Wikimedia Commons/`: Media (images, audio, video) sourced from Wikimedia Commons
  - Filenames: Descriptive names for easy identification (e.g., `04 production-possibilities-frontier-1.png`)
  - May be renamed via `convert wiki.py.names map.json` during Wikipedia ingestion
  
- `archives/sparse/`: Miscellaneous archived content with user-defined filenames
  - **Important**: Filenames are user-defined (descriptive or arbitrary), NOT automatically SHA-256 hashed
  - Users manually add files with chosen filenames
  - Entry in `index.md` must include source URL, timestamp, and description

## Future Expansion

Additional archive categories may be added as needed:
- `archives/datasets/`: Research datasets, CSV files
- `archives/papers/`: Academic papers, preprints
- `archives/books/`: E-books, full-length texts
- `archives/code/`: Archived source code, repos

## index.md Format

**Required metadata for each entry**:
- Filename (as Markdown link)
- Description (brief summary)
- Source (original URL or provenance)
- Timestamp (download/archive date)
- Hash (optional; SHA-256 for verification)
- License (optional; for Wikimedia Commons media)

**Example**:
```markdown
- [example-article.md](example-article.md) — Archived blog post about X
  - Source: https://example.com/blog/article
  - Downloaded: 2024-01-20
```

**Automation**: pyarchivist tool (`tools/pyarchivist/`) can auto-update `index.md` when archiving new content

## Best Practices

- Use descriptive filenames when human-readability matters
- Use content hashes when deduplication is critical
- Keep `index.md` updated (manually or via pyarchivist)
- Preserve existing archive structure; don't reorganize without reason
- Link to archives from notes using relative paths
