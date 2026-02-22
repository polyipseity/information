---
name: tools
description: Repository-wide tooling including init wrapper, pack/publish utilities, and all helper scripts. Links to tools-special and tools-templates for subfolder details.
---

# Repository Tools Overview

> **Continuous improvement:** see `continuous_improvement.md` in this
> folder for notes on tool behaviour, past feedback, and update
> procedures.

Use this skill when working with repository-wide tools, understanding tool architecture, or coordinating workflows across multiple tool categories.

## Tool categories

The `tools/` directory contains all helper scripts and utilities:

### Core scripts (tools/)

1. **`init.py`**: Async wrapper for pytextgen with mtime/inode caching
   - Discovers changed `.md` files (excludes `.git`, `.obsidian`, `tools`)
   - Caches `(mtime, inode, text)` to skip unchanged files
   - Normalizes newlines to `\n` before pytextgen processing
   - Passes through pytextgen flags (`-C`, `--no-code-cache`, `--init-flashcards`)
   - Commands: `uv run -m init generate`, `uv run -m init clear`

2. **`convert wiki.py`**: Wikipedia HTML → Markdown converter
   - Reads HTML from clipboard
   - Normalizes links (relative paths with `%20` encoding)
   - Downloads media to `archives/Wikimedia Commons/`
   - Uses `convert wiki.py.names map.json` for filename renames
   - Preserves Wikipedia attribution
   - Command: `uv run -m "convert wiki"`

3. **`pack.py`**: PageRank-ordered zip bundling
   - Walks Markdown links to build dependency graph
   - Computes PageRank to prioritize important files
   - Creates zip bundle with metadata (ranks, omissions, link closure)
   - Configurable: damping factor, iterations, max files
   - Command: `python -m pack -o pack.zip -n 25 --damping-factor 0.5 --page-rank-iterations 100 <paths>`

4. **`publish.py`**: Private → public history mirroring via git filter-repo
   - Clones `private/.git` temporarily
   - Runs `git filter-repo` with property `Private-commit` filtering
   - Rewrites commit history to remove sensitive paths
   - Rebases with signing, adds remote to public `.git`
   - Command: `python -m publish --paths-file <file>` (with `literal:<path>` lines)

### Subfolder tools

- **`tools/special/`**: Academic LMS converters and course management (see `tools-special` skill)
  - Canvas/HKUST Zinc converters
  - Course catalog fetchers
  
- **`tools/templates/`**: Note scaffolding and pytextgen templates (see `tools-templates` skill)
  - `new wiki page.py`
  - `pytextgen generate *.md` templates

### Submodule tools

- **`tools/pytextgen/`**: Git submodule for content generation library (see `pytextgen` skill)
- **`tools/pyarchivist/`**: Git submodule for archiving tool (see `pyarchivist` skill)

## When to use this skill

- Understanding tool relationships and dependencies
- Coordinating multi-tool workflows (e.g., wiki ingestion → generation → packaging)
- Troubleshooting tool interactions
- Planning new tool development or refactoring

## Common workflows

### End-to-end wiki ingestion

1. Scaffold note: `uv run -m "templates.new wiki page"` (tools-templates)
2. Ingest HTML: `uv run -m "convert wiki"` (convert wiki.py)
3. Generate flashcards: `uv run -m init generate <file>` (init.py + pytextgen)

### Academic course organization

1. Convert LMS export: `python -m tools.special."convert Canvas submission"` (tools-special)
2. Update index: Edit `special/academia/<Institution>/index.md`
3. Generate course tables: Add pytextgen fences, run `python -m init generate` (pytextgen)

### Packaging and publishing

1. Regenerate all: `uv run -m init generate -C` (init.py)
2. Package bundle: `uv run -m pack -o bundle.zip -n 50 <paths>` (pack.py)
3. Publish filtered history: `uv run -m publish --paths-file paths.txt` (publish.py)

### Archive management

1. Archive content: Use pyarchivist tool (pyarchivist skill)
2. Verify index: Check `archives/*/index.md` updated
3. Reference in notes: Add relative links with `%20` encoding

## Tool dependencies

### Python requirements

See `requirements.txt` for package dependencies:

- `anyio`: Async I/O for init.py
- `aiohttp`: HTTP client for downloads
- `bs4` (BeautifulSoup): HTML parsing for convert wiki.py
- `PyYAML`: YAML frontmatter parsing
- `pytextgen`: Content generation library
- Others as needed

Install: `pip install -r requirements.txt`

### External tools

- **git**: Required for all workflows
- **git-filter-repo**: Required for `publish.py`
- **Python 3.8+**: Minimum version for async features

### Git submodules

- `tools/pytextgen/`: Content generation engine
- `tools/pyarchivist/`: Archiving tool
- `self/**`: Personal metadata submodules
- `private/**`: Private content submodule

## Tool architecture

### init.py caching strategy

1. On first run: Walk workspace, compute `(mtime, inode)` for all `.md` files
2. Cache text and metadata in memory
3. On subsequent runs: Skip files with unchanged `(mtime, inode)`
4. Normalize `\n` before passing to pytextgen
5. Use `-C` / `--no-cached` to rebuild cache

**Cache location**: In-memory (not persisted to disk)

### pytextgen compile cache

1. Compiled Python modules cached in `__pycache__/`
2. Use `--no-code-cache` to bypass
3. Clear with `rm -rf __pycache__/` if stale

### Git filter-repo workflow

1. Clone `private/.git` to temporary directory
2. Run `git filter-repo --path-rename` based on `--paths-file`
3. Filter commits by `Private-commit` property
4. Rebase and sign commits
5. Add temporary remote to public `.git`
6. User must manually push

## CLI stability

**Critical**: Core tools have established interfaces; preserve:

- Argument names and order
- Expected input formats (clipboard, files, stdin)
- Output formats (Markdown, YAML, CSV, ZIP)
- Error codes and messages

If changes are needed, ask user for permission first.

## Best practices

### Tool coordination

- **Regenerate before packaging**: Always run `uv run -m init generate -C` before `pack.py`
- **Clean before publishing**: Verify `private/` content is properly filtered before `publish.py`
- **Archive before ingestion**: Use pyarchivist for media before manual note creation
- **Template before conversion**: Scaffold frontmatter before ingesting content

### Error handling

- Check tool exit codes before proceeding
- Verify file existence before processing
- Validate YAML/HTML/CSV formats before parsing
- Use `--dry-run` or preview modes when available

### Performance

- Use init.py caching to skip unchanged files
- Parallelize independent operations (e.g., multiple `convert wiki` runs)
- Limit PageRank iterations in `pack.py` for large graphs
- Use `--exclude-extension` in pack.py to skip large assets

## When to ask for help

- If tool behavior is unexpected, consult user or check tool documentation
- If editing submodules (`pytextgen`, `pyarchivist`), ask user for permission
- If new tool is needed, discuss requirements and architecture with user
- If tool fails mysteriously, check Python version and dependencies

## Common issues

1. **Cache staleness**: Use `-C` / `--no-cached` if init.py skips changed files
2. **Module import errors**: Ensure `requirements.txt` packages installed
3. **Git submodule out of date**: Run `git submodule update --remote`
4. **Path encoding issues**: Ensure `%20` encoding for spaces in links
5. **Clipboard access**: Some tools require clipboard support (may fail in headless environments)

## Editing guidelines for tools/**/*.py

When editing Python helper scripts in `tools/`:

- **Preserve CLI surfaces**: Keep argument names, defaults, and help text stable; avoid breaking `uv run -m init generate/clear`, `uv run -m pack`, `uv run -m publish`, and other tool entrypoints
- **Maintain async/anyio patterns**: Preserve async patterns like `anyio.Path`, `asyncio.create_task`, `TaskGroup`, `BoundedSemaphore` and caching behaviors (init cache, pytextgen compile cache in `__pycache__/`)
- **Keep submodules read-only unless requested**: `tools/pytextgen`, `tools/pyarchivist`, `self/**`, `private/**` are git submodules; ask user before editing
- **Normalize newlines**: When touching the init wrapper, normalize to `\n`; do not bypass its exclusion list (`.git`, `.obsidian`, `tools`)
- **Favor relative imports**: Use relative imports within the tools package; do not hardcode absolute host paths
- **Update requirements.txt**: When adding dependencies, update `requirements.txt` and note any non-pip prerequisites; prefer lightweight stdlib/typed solutions
- **Test thoroughly**: Python tools are critical infrastructure; test changes carefully before committing
