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
uv run -m scripts.convert_wiki  # Paste Wikipedia HTML from clipboard
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

- Use `pyproject.toml` as the authoritative dependency source for Python. Do __not__ reintroduce a long-lived `requirements.txt`; it is only a transient compatibility helper at best and the canonical metadata is maintained in `pyproject.toml`'s `[project]` and `[dependency-groups]` sections.
- Keep runtime dependencies in `[project].dependencies`, developer/test tools in `[dependency-groups].dev`, and the full union of dependencies referenced by inline `# /// script` metadata in `[dependency-groups].scripts` even when a package also appears in `[project].dependencies`.
- For inline `# /// script` metadata: (1) all files __must__ begin with `#!/usr/bin/env python` shebang on line 1, (2) keep keys alphabetized (`dependencies`, `requires-python`, `timestamp`), (3) set `requires-python = ">=3.13.0"`.
  - `bun install` runs the `postinstall` hook which executes `uv sync` to install development extras declared under `[dependency-groups].dev`. Run `bun install` and then `bun run prepare` to install deps and register `prek.toml` hooks locally.
- Formatting & linters: Use `prettier`, `markdownlint-cli2`, `ty`, and `ruff`. Ruff replaces Black and isort for code formatting and import sorting. Git hooks are managed by `prek.toml` (pre-commit, commit-msg, pre-push).
- __Python entry points__: All Python scripts and modules must follow a strict convention for runnable entry points. See `.agents/instructions/python-entry-points.instructions.md` for comprehensive guidance on the `__name__ == "__main__"` pattern, async dispatch with `runnify`, and integration with Asyncer.
- Testing conventions:
  - Tests are placed under `tests/` and must mirror the working tree structure where applicable (for example, `scripts/foo.py` → `tests/scripts/test_foo.py`).
  - Use `pytest` (config in `pyproject.toml`) and name tests `test_*.py`. Use `pytest.mark.anyio` for async tests with the AnyIO plugin and prefer deterministic fixtures (use `monkeypatch`, `tmp_path: os.PathLike[str]` and the `conftest.py` fixtures provided). When writing tests, annotate the `tmp_path` fixture as `PathLike[str]` where possible and, when converting path-like objects to strings, __always__ use `os.fspath(path_like)` rather than `str(path_like)` so the filesystem path protocol is correctly respected. Prefer importing concurrency helpers from Asyncer (`create_task_group`, `soonify`, `asyncify`) instead of calling `anyio.create_task_group` directly.
  - Include tests for all substantive behavior changes, especially for scripts and tools (`scripts/` and `scripts/`). Add tests that exercise error paths and edge cases.
  - CI and local pre-push both run the test suite: `prek` `pre-push` runs `bun run test` which invokes `uv run --locked pytest`. The GitHub Actions CI runs `bun install --frozen-lockfile --ignore-scripts && uv sync --locked` and then `bun run check` and `bun run test` to validate changes.
- Type checking: The repo uses `ty` configured via `[tool.ty]` in `pyproject.toml`. Run `uv run --locked ty check` as part of local checks and pre-commit hooks.
  - Typing guidance: prefer PEP 585 built-in generics for concrete collections (for example `list[str]`, `dict[str, int]`) and use `collections.abc` abstract base classes for interface/parameter annotations (for example `collections.abc.Sequence[str]`, `collections.abc.Mapping[str, int]`, `collections.abc.Iterable[str]`). Avoid `typing.List`, `typing.Dict`, and `typing.Sequence` in new code. Keep `os.PathLike` for path-like types and use `os.fspath(path_like)` when converting to `str`.

- Coverage: Use `pytest-cov` (pytest `addopts` includes `--cov=./`). Strive to add tests for new behavior; test coverage thresholds are recommended to be added as the project matures.
- Commit & change policy: Always run `bun run format` and `bun run check` before committing. Agents must ensure commit messages follow Conventional Commits (see `.agents/instructions/commit-convention.instructions.md`) and must show proposed commit messages for review before committing.

---

## Setup

Install Node.js dependencies, register Git hooks, and install Python dev extras:

```bash
bun install            # installs node deps; runs `postinstall` hook which installs Python dev extras
bun run prepare        # Installs prek hooks (registers Git hooks)
```

Notes:

- The repository uses `pyproject.toml` as the canonical Python dependency metadata. Development extras (dev dependency group) are installed by the `postinstall` script which runs `uv sync`. Ensure `pyproject.toml` lists dev dependencies under `[dependency-groups].dev`.
- Remove `requirements.txt` — dependency management is consolidated in `pyproject.toml`. See the `core-workflows` instructions for migration steps.
- `prek.toml` hooks enforce pre-commit checks (markdownlint, prettier, ruff for Python). A pre-push hook runs `bun run test` to prevent pushing failing tests.
- Prefer using `bun run <script>` wrappers to ensure consistent, reproducible tool versions and to trigger package lifecycle hooks.

__Tooling & scripts:__ Prefer using `bun` script wrappers when available. Run `bun run <script>` from the repository root to ensure project-local tools and the lockfile are used.

Common scripts (see `package.json`):

- `bun run check` — repository checks (runs `check:md`). When you later run `bun run check:md` (or `bun run format:md`) with explicit paths or filenames, always add `--no-globs` and list the exact files so the paths are treated literally and the entire workspace is not scanned.
- `bun run format` — formatting helpers (runs `format:md`)
- `bun run commitlint` — validate commit messages
- `bun run prepare` — install prek hooks

This enables:

- __Commit message validation__ (commitlint) - enforces Conventional Commits
- __Markdown formatting checks__ (markdownlint) - validates `**/*.md` files
- __Pre-commit hooks__ - auto-fixes and validates Markdown before commits
- __CI workflows__ - GitHub Actions runs the same checks on push/PR

## Custom instructions

Instruction files auto-apply via glob patterns. See `.agents/instructions/` for details:

### Content notes

- [content-organization.instructions.md](.agents/instructions/content-organization.instructions.md) → `**` (repository structure overview)
- [editing-conventions.instructions.md](.agents/instructions/editing-conventions.instructions.md) → `**/*.md` (general editing rules)
- [markdown-notes.instructions.md](.agents/instructions/markdown-notes.instructions.md) → `general/**/*.md`
- [special.instructions.md](.agents/instructions/special.instructions.md) → `special/**/*.md`, `special/**/*.py`
- [archives.instructions.md](.agents/instructions/archives.instructions.md) → `archives/**/*.md`
- [commit-convention.instructions.md](.agents/instructions/commit-convention.instructions.md) → `**` (enforce conventional commit usage for agent-made commits; prompt for flashcard counts and append machine-readable trailers when changes affect `.md` files under `general/`, `special/`, or `self/` that have flashcard tags and genuinely add/remove flashcards; see it for the `commit-staged-flashcard-progress` prompt and flashcard progress commit format.)

### Workflows

- [core-workflows.instructions.md](.agents/instructions/core-workflows.instructions.md) → `**` (command-line workflows)

### Config folders

- [config-folders.instructions.md](.agents/instructions/config-folders.instructions.md) → `.git/**`, `.obsidian/**`, `.vscode/**`

### Submodule guards

- [submodule-private.instructions.md](.agents/instructions/submodule-private.instructions.md) → `private/**`

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

## Recent updates (agent guidance)

- 2026-04-20: Inline `# /// script` policy tightened — every package referenced by inline script metadata must also appear in `[dependency-groups].scripts`; inline metadata keys should stay alphabetized and include `requires-python = ">=3.13.0"`. Clarified that `self/stash/` is part of the parent repo while only specific `self/*` folders are git submodules.
- 2026-02-09: Added `.agents/instructions/agent-quickstart.instructions.md` (now merged into `core-workflows.instructions.md`) — startup commands, quick gotchas, test/format sequence, and submodule guardrails.
- 2026-02-09: Updated commit message guidance — agents should prefer wrapping commit body lines to __72 characters__ (readability/buffer). Tooling (commitlint) continues to enforce a __100-character__ hard limit, so ensure lines are ≤100 to pass.
- 2026-03-02: Validation strictness increased — __all warnings must be addressed just like errors__ (fix or suppress with a valid rationale). The validator message has been updated accordingly.
- __MD060 (table-column-style):__ Agents should __ignore__ MD060 violations; do not attempt to fix them. The human will fix table formatting manually.

## AI agent quickstart ✅

- See `.agents/instructions/core-workflows.instructions.md` for a concise checklist agents should follow before changing files or making commits.
- Recommended workspace settings: `chat.useAgentsMdFile = true`, `chat.useAgentSkills = true` to enable skill-based guidance and the root `AGENTS.md` for context.
- Safe startup: `bun install` → `bun run prepare` → `bun run format` → `bun run check` → `bun run test`.
- Regeneration of content happens automatically, so there's no need to run `uv run -m init generate -C`; use `uv run -m pack` and `uv run -m publish` only after tests pass and user approval for publishing sensitive content.
- Keep inline `# /// script` metadata synchronized with `pyproject.toml`: every inline-script dependency belongs in `[dependency-groups].scripts`, files must begin with `#!/usr/bin/env python` shebang on line 1, metadata keys stay alphabetized, and `requires-python` stays at `>=3.13.0`.
- Always follow `.agents/instructions/commit-convention.instructions.md` for agent-made commits (Conventional Commits, trailer rules); __prefer wrapping commit body lines to 72 characters or fewer for readability and buffer, but ensure lines are ≤100 to pass commitlint.__
- Ask for explicit permission before editing `private/`, any actual submodule under `self/`, or any other submodule content; `self/stash/` is not a submodule, but it is still user-owned scratch space and should only be changed when requested.
- Use the Todo List Tool for multi-step tasks and include short, test-backed PRs with a clear rationale when making non-trivial changes.
