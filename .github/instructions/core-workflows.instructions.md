---
name: Core workflows
description: Common command-line workflows for regenerating content, ingesting Wikipedia, packaging, and publishing
applyTo: "**"
---

# Core Workflows

**Tooling & pnpm wrappers:** Prefer `pnpm` script wrappers when available. Check `package.json` for repository scripts and prefer `pnpm run <script>` from the repository root to ensure project-local tools and the lockfile are used. When no pnpm wrapper exists for an operation, run the underlying command shown below (for example, `python -m init generate`). Always run `pnpm install` before using `pnpm run`.

Important: `pnpm install` triggers the `prepare` script which runs `uv sync --all-extras --dev` to install Python development extras declared in `pyproject.toml`'s `[dependency-groups].dev` using the project's `uv.lock`. For CI and deterministic installs prefer `uv sync --locked --all-extras --dev`. `pyproject.toml` is the canonical source for Python dependency metadata in this repository; keep it up-to-date and add dev-only tools there rather than in a `requirements.txt` file.

## Regenerate generated regions

**Command**: `python -m init generate [pytextgen flags] <paths?>`

- Add `-C/--no-cached` to rebuild cache from scratch
- Pass pytextgen flags like `--no-code-cache`, `--init-flashcards`
- Regenerates pytextgen content blocks in Markdown files
- **See**: [pytextgen](../skills/pytextgen/SKILL.md) skill for detailed fence syntax and debugging

## Clear generated content

**Command**: `python -m init clear --type CONTENT <paths?>`

- Other `ClearType` values available in `tools/pytextgen` (check skill documentation)
- Clears generated regions without regenerating; useful for resolving merge conflicts
- **See**: [pytextgen](../skills/pytextgen/SKILL.md) skill for detailed options

## Wiki ingestion (3-step workflow)

**Step 1**: `python -m "templates.new wiki page"`

- Scaffolds frontmatter + Wikipedia link template, copies to clipboard

**Step 2**: `python -m "convert wiki"`

- Reads clipboard HTML, normalizes to Markdown, downloads media to `archives/Wikimedia Commons/`

**Step 3**: `python -m init generate <file>`

- Generates flashcards from cloze markup

- **See**: [wiki-ingestion](../skills/wiki-ingestion/SKILL.md) skill for step-by-step guidance

## Package bundle

**Command**: `python -m pack -o pack.zip -n 25 --damping-factor 0.5 --page-rank-iterations 100 <paths>`

- Creates PageRank-sorted zip with link-closure metadata
- `-n 25`: Max 25 files in bundle
- `--damping-factor 0.5`: PageRank weighting (0.0-1.0, default 0.85)
- `--page-rank-iterations 100`: Convergence iterations
- Prioritizes important files based on link structure
- **Best practice**: Always run `python -m init generate -C` first to ensure fresh content
- **See**: [tools](../skills/tools/SKILL.md) skill for dependency management

## Publish bridge

**Command**: `python -m publish --paths-file <file>`

- Mirrors filtered history from `private/.git` into public `.git`
- Uses `git filter-repo` to rewrite history (returns exit code 0 on success)
- Optional: `--allow-trailing-whitespaces-in-paths` for relaxed validation
- **Paths file format**: Lines with `literal:<path>` patterns to filter
- **Best practice**: Verify `private/` content is properly filtered before publishing
- **See**: [tools](../skills/tools/SKILL.md) skill for tool architecture and coordination

## Related instructions

- [content-organization](content-organization.instructions.md): Directory structure and conventions
- [editing-conventions](editing-conventions.instructions.md): General editing rules for Markdown files
- [markdown-notes](markdown-notes.instructions.md): Specific conventions for general/**.md files
- [special](special.instructions.md): Conventions for specialized content
