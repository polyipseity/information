---
name: pyarchivist
description: Archive online content into archives/ with automatic index.md updates via pyarchivist tool.
---
# pyarchivist Workflow

Use this skill when archiving web content, media, or online documents into the knowledge base.

## What pyarchivist does

`pyarchivist/` is a git submodule that automatically archives online content to `archives/` and updates `index.md` files with metadata (source URL, timestamp, file hash).

## When to use

- Archiving articles, web pages, or media from online sources
- Storing Wikimedia Commons images alongside notes
- Creating permanent backups of time-sensitive online content
- Auto-maintaining `archives/index.md` files

## Basic workflow

1. Use pyarchivist's interface (CLI or Python API) to download and archive content
2. Specify target directory (`archives/Wikimedia Commons/` for media, `archives/sparse/` for documents)
3. pyarchivist auto-generates metadata (timestamp, source URL, content hash)
4. `index.md` entries are auto-created with source and timestamp information
5. Filenames are generated consistently (hash-based for deduplication or descriptive for media)

## Best practices

- Let pyarchivist handle file naming and `index.md` updates
- Use `archives/Wikimedia Commons/` for images/media with descriptive names
- Use `archives/sparse/` for miscellaneous content (hashes for filenames automatically)
- Always preserve source URL and timestamp metadata in `index.md`
- Check that `index.md` was updated correctly after archiving

## Typical command pattern

```shell
uv run -m pyarchivist [options] --target <archives/folder> <source_url>
```

(Exact interface depends on pyarchivist's implementation)

## When in doubt

Consult the pyarchivist documentation or ask the user for guidance on specific archiving needs.
