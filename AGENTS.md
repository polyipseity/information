# AGENTS

Personal Markdown knowledgebase with flashcards, tutorials, and archived online content.

## Quick reference

- __`general/`__: Wikipedia encyclopedia articles (verbatim, flashcard-enabled)
- __`special/`__: Coursework, tutorials, frameworks, language texts
- __`archives/`__: Archived media and web content (Wikimedia Commons, sparse)
- __`scripts/`__: Python scripts (init, convert_wiki, pack, publish, templates)

__Git submodules__: `private/`

__Not submodules__: `self/stash/` remains part of this repository and stores user-managed scratch scripts.

__Submodule hierarchy__: Innermost `AGENTS.md` takes priority.

## Quick start: Common workflows

__Creating notes__:

```bash
# Scaffold new wiki-sourced note (see wiki-ingestion skill)
uv run -m scripts.new_wiki_page
uv run -m scripts.convert_wiki --clipboard  # Paste Wikipedia HTML from clipboard
# Flashcards are created automatically by the build; do not run
# `uv run -m init generate` yourself.
```

__Maintaining content__:

```bash
# The repository rebuild workflows handle regeneration; agents and
# authors typically do not invoke `uv run -m init generate` manually.

# If you need to clear stale generated regions, the clear command is
# available:
uv run -m init clear --type CONTENT <optional-paths>
```

__Organizing & publishing__:

```bash
# Generated content is rebuilt automatically during packaging; manual
# `uv run -m init generate` is not required.

# Create PageRank-optimized bundle (see tools skill)
uv run -m pack -o pack.zip -n 25 --damping-factor 0.5 <paths>

# Mirror private→public filtered history (see tools skill)
uv run -m publish --paths-file paths.txt
```

For detailed workflows, see [core-workflows.instructions.md](.agents/instructions/core-workflows.instructions.md). Instruction metadata now lives in each file's frontmatter. Only `name`, `description`, and `applyTo` are supported keys in instruction frontmatter—do not add extra fields.

## Dependencies

- __Python >=3.14__ — declared in `pyproject.toml` (this is the canonical source of Python dependency metadata).
- __Node.js 24+__ with `package.json` packages (commitlint, markdownlint, prettier, etc.).
- External tools: `git`, `git-filter-repo`.
- Obsidian plugins: Extended MathJax (for `.obsidian/plugins/obsidian-latex/preamble.sty`).

---

## Developer tooling & testing conventions

- `pyproject.toml` is the canonical Python dependency source. No `requirements.txt`. Runtime deps in `[project].dependencies`, dev tools in `[dependency-groups].dev`, inline-script deps in `[dependency-groups].scripts`.
- Inline `# /// script` files: shebang on line 1, alphabetized keys, `requires-python = ">=3.13.0"`.
- `bun install` runs `postinstall` → `uv sync` (installs dev extras). Then `bun run prepare` registers prek hooks.
- Linters: `prettier`, `markdownlint-cli2`, `ty`, `ruff`. Git hooks via `prek.toml`.
- Python entry points: see `.agents/instructions/python-entry-points.instructions.md`.
- Tests: mirror source layout under `tests/`. Use `pytest`, `pytest.mark.anyio` for async, `tmp_path: os.PathLike[str]` fixtures, `os.fspath()` for path conversion. Async helpers from Asyncer, not `anyio` directly.
- Type checking: `uv run --locked ty check`. Prefer PEP 585 builtins (`list[str]`, `dict[str, int]`) and `collections.abc` for abstract types. No `typing.List`/`typing.Dict`.
- Coverage: `pytest-cov` (`--cov=./`).
- Pre-commit: `bun run format` + `bun run check` before committing. Follow `.agents/instructions/commit-convention.instructions.md`.

---

## Setup

```bash
bun install            # installs node deps; postinstall runs uv sync for Python dev extras
bun run prepare        # registers prek hooks
```

Prefer `bun run <script>` wrappers (see `package.json`). `bun run check` → markdownlint. `bun run format` → formatting. `bun run commitlint` → commit validation. When targeting specific files with `check:md`/`format:md`, append `--no-globs` and list exact filenames.

## Custom instructions

Instruction files in `.agents/instructions/` auto-apply via `applyTo` globs. See [`.agents/instructions/README.md`](.agents/instructions/README.md) for the full index.

## Agent skills

Enable `chat.useAgentSkills` in VS Code for auto-loading. See `.agents/skills/` for details:

__Skills metadata__: Each skill is self-described in its `SKILL.md` frontmatter with `name`, `description`, and `applyTo` (and optional `parent` or `license`). Agents may inspect individual skill documents directly.

### Content creation & ingestion

- __[wiki-ingestion](.agents/skills/wiki-ingestion/SKILL.md)__ — Import Wikipedia articles, normalize links/media, scaffold new notes
- __[pytextgen](.agents/skills/pytextgen/SKILL.md)__ — Regenerate/clear content blocks, fence syntax, cloze markup, debugging
- __[tools](.agents/skills/tools/SKILL.md)__ — Repository-wide tooling overview (includes templates & academic LMS converters), tool coordination, dependency management
- __[pyarchivist](.agents/skills/pyarchivist/SKILL.md)__ — Archive online content, auto-maintain `index.md`, media management
- __[academic-notes](.agents/skills/academic-notes/SKILL.md)__ — Writing notes in academic course style: frontmatter conventions, index & weekly structure, flashcard metadata, cross-references, and scaffolding templates (institution-agnostic)

__Skill flow__: Most workflows use multiple skills in sequence; see individual skill files for cross-references and integration guidance.

## Recent updates

- 2026-04-20: Inline `# /// script` deps must appear in `[dependency-groups].scripts`. `self/stash/` is parent-repo; only specific `self/*` are submodules.
- 2026-03-02: All warnings treated as errors (fix or suppress with rationale).
- MD060: ignore; human fixes table formatting.

## AI agent quickstart

- Enable `chat.useAgentsMdFile = true` and `chat.useAgentSkills = true`.
- Startup: `bun install` → `bun run prepare` → `bun run format` → `bun run check` → `bun run test`.
- Content regenerates automatically; do not run `uv run -m init generate`.
- See `core-workflows.instructions.md` for detailed workflows and gotchas.
