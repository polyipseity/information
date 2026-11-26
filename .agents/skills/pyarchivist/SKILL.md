---
name: pyarchivist
description: Archive online content into archives/ or a course attachments directory with automatic index.md updates via the pyarchivist package.
---

# pyarchivist Workflow

> __Continuous improvement:__ see `continuous_improvement.md` in this
> folder for a history of feedback and tips for using pyarchivist.

Use this skill when archiving web content, media, or online documents into the knowledge base.

## What pyarchivist does

`pyarchivist` is a Python package declared in `pyproject.toml` and locked in `uv.lock`, run as `uv run -m pyarchivist`. It downloads a file, writes it to the target directory, and appends a credit line to that directory's `index.md` with the source URL, the licence, and the author. Run it from the repository root; there is no local checkout to `cd` into.

## When to use

- Archiving articles, web pages, or media from online sources
- Storing Wikimedia Commons images beside notes, including a course's own `attachments/`
- Creating permanent backups of time-sensitive online content
- Auto-maintaining `archives/index.md` files

## Basic workflow

1. Pick the destination: `archives/Wikimedia Commons/` for shared media, `archives/sparse/` for documents, or the course's `attachments/` when the figure belongs to that course.
2. Run the archiver with `-d` for the directory and `-i` for the `index.md` it should credit.
3. Confirm the file landed and that `index.md` gained its credit line.
4. Write the child entry and the description line in `index.md` yourself: the tool maintains credits, not prose.

## Command patterns

Wikimedia Commons, whose inputs are page titles:

```shell
uv run -m pyarchivist Wikimedia_Commons -d "<destination>" -i "<destination>/index.md" "File:Name.png"
```

`--ignore-individual-errors` keeps a batch going past one bad title. `--no-trust-env` ignores `HTTPS_PROXY`/`HTTP_PROXY` when a proxy breaks the fetch.

A `File:` page title is the input. A Commons file page URL is not: the title reaches the API as written, so a URL fails.

## Best practices

- Let pyarchivist handle file naming and the credit line
- Use `archives/Wikimedia Commons/` for shared media with descriptive names
- Use `archives/sparse/` for miscellaneous content
- Point a course figure at that course's `attachments/`, so the course stays self-contained
- Check that `index.md` was credited correctly after the run

## When in doubt

Ask for the exact Commons title, and read `uv run -m pyarchivist --help` for the current subcommands.
