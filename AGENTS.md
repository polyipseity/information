# AGENTS

Personal Markdown knowledgebase with flashcards, tutorials, and archived online content.

## Quick reference

- **`general/`**: Wikipedia encyclopedia articles (verbatim, flashcard-enabled)
- **`special/`**: Coursework, tutorials, frameworks, language texts  
- **`archives/`**: Archived media and web content (Wikimedia Commons, sparse)
- **`tools/`**: Python scripts (init, convert wiki, pack, publish, templates)

**Git submodules**: `self/`, `private/`, `tools/pytextgen/`, `tools/pyarchivist/`

**Submodule hierarchy**: Innermost `AGENTS.md` takes priority. Many submodules (e.g., `self/ledger`) have their own `.github/instructions/` and `.github/skills/`.

## Quick start: Common workflows

**Creating notes**:

```bash
# Scaffold new wiki-sourced note (see wiki-ingestion skill)
uv run -m "templates.new wiki page"
uv run -m "convert wiki"  # Paste Wikipedia HTML from clipboard
uv run -m init generate <file>  # Generate flashcards from cloze markup
```

**Maintaining content**:

```bash
# Regenerate all generated blocks (see pytextgen skill)
uv run -m init generate -C  # Force cache rebuild

# Clear stale content before troubleshooting (see pytextgen skill)
uv run -m init clear --type CONTENT <optional-paths>
```

**Organizing & publishing**:

```bash
# Before packaging/publishing, regenerate everything (see tools skill)
uv run -m init generate -C

# Create PageRank-optimized bundle (see tools skill)
uv run -m pack -o pack.zip -n 25 --damping-factor 0.5 <paths>

# Mirror private→public filtered history (see tools skill)
uv run -m publish --paths-file paths.txt
```

For detailed workflows, see [core-workflows.instructions.md](.github/instructions/core-workflows.instructions.md).

## Dependencies

- **Python >=3.12** — declared in `pyproject.toml` (this is the canonical source of Python dependency metadata).
- **Node.js 24+** with `package.json` packages (commitlint, markdownlint, prettier, pyright, etc.).
- External tools: `git`, `git-filter-repo`.
- Obsidian plugins: Extended MathJax (for `.obsidian/plugins/obsidian-latex/preamble.sty`).

---

## Developer tooling & testing conventions

- Use `pyproject.toml` as the authoritative dependency source for Python. Do **not** reintroduce a long-lived `requirements.txt`; it is only a transient compatibility helper at best and the canonical metadata is maintained in `pyproject.toml`'s `[project]` and `[dependency-groups]` sections.
- `pnpm install` runs the `postinstall` hook which executes `uv sync --all-extras --dev` to install development extras declared under `[dependency-groups].dev`. Run `pnpm install` and then `pnpm run prepare` to install deps and register Husky hooks locally.
- Formatting & linters: Use `prettier`, `markdownlint-cli2`, `pyright`, and `ruff`. Ruff replaces Black and isort for code formatting and import sorting. `lint-staged` is configured to run relevant formatters/linters on staged files and Husky hooks enforce pre-commit and pre-push checks.
- Testing conventions:
  - Tests are placed under `tests/` and must mirror the working tree structure where applicable (for example, `scripts/foo.py` → `tests/scripts/test_foo.py`).
  - Use `pytest` (config in `pyproject.toml`) and name tests `test_*.py`. Use `pytest.mark.asyncio` for async tests and prefer deterministic fixtures (use `monkeypatch`, `tmp_path: os.PathLike[str]` and the `conftest.py` fixtures provided). When writing tests, annotate the `tmp_path` fixture as `PathLike[str]` where possible and, when converting path-like objects to strings, **always** use `os.fspath(path_like)` rather than `str(path_like)` so the filesystem path protocol is correctly respected.
  - Include tests for all substantive behavior changes, especially for scripts and tools (`tools/` and `scripts/`). Add tests that exercise error paths and edge cases.
  - CI and local pre-push both run the test suite: Husky `pre-push` runs `pnpm run test` which invokes `uv run --locked pytest`. The GitHub Actions CI runs `pnpm install --frozen-lockfile --ignore-scripts && uv sync --locked --all-extras --dev` and then `pnpm run check` and `pnpm run test` to validate changes.
- Type checking: The repo supports `pyright` with a root-level `pyrightconfig.json` (strict mode). Run `pyright` as part of local checks and in lint-staged if appropriate.

  - Typing guidance: prefer PEP 585 built-in generics for concrete collections (for example `list[str]`, `dict[str, int]`) and use `collections.abc` abstract base classes for interface/parameter annotations (for example `collections.abc.Sequence[str]`, `collections.abc.Mapping[str, int]`, `collections.abc.Iterable[str]`). Avoid `typing.List`, `typing.Dict`, and `typing.Sequence` in new code. Keep `os.PathLike` for path-like types and use `os.fspath(path_like)` when converting to `str`.
- Coverage: Use `pytest-cov` (pytest `addopts` includes `--cov=./`). Strive to add tests for new behavior; test coverage thresholds are recommended to be added as the project matures.
- Commit & change policy: Always run `pnpm run format` and `pnpm run check` before committing. Agents must ensure commit messages follow Conventional Commits (see `.github/instructions/commit-convention.instructions.md`) and must show proposed commit messages for review before committing.

---

## Setup

Install Node.js dependencies, register Git hooks, and install Python dev extras:

```bash
pnpm install            # installs node deps; runs `postinstall` hook which installs Python dev extras
pnpm run prepare        # Activates Husky hooks (registers Git hooks)
```

Notes:

- The repository uses `pyproject.toml` as the canonical Python dependency metadata. Development extras (dev dependency group) are installed by the `postinstall` script which runs `uv sync --all-extras --dev`. Ensure `pyproject.toml` lists dev dependencies under `[dependency-groups].dev`.
- Remove `requirements.txt` — dependency management is consolidated in `pyproject.toml`. See the `core-workflows` instructions for migration steps.
- Husky hooks and lint-staged enforce pre-commit checks (markdownlint, prettier, ruff for Python). A pre-push hook runs `pnpm run test` to prevent pushing failing tests.
- Prefer using `pnpm run <script>` wrappers to ensure consistent, reproducible tool versions and to trigger package lifecycle hooks.

**Tooling & scripts:** Prefer using `pnpm` script wrappers when available. Run `pnpm run <script>` from the repository root to ensure project-local tools and the lockfile are used.

Common scripts (see `package.json`):

- `pnpm run check` — repository checks (runs `check:md`)
- `pnpm run format` — formatting helpers (runs `format:md`)
- `pnpm run commitlint` — validate commit messages
- `pnpm run prepare` — register Husky hooks

This enables:

- **Commit message validation** (commitlint) - enforces Conventional Commits
- **Markdown formatting checks** (markdownlint) - validates `**/*.md` files
- **Pre-commit hooks** - auto-fixes and validates Markdown before commits
- **CI workflows** - GitHub Actions runs the same checks on push/PR

## Custom instructions

Instruction files auto-apply via glob patterns. See `.github/instructions/` for details:

### Content notes

- [content-organization.instructions.md](.github/instructions/content-organization.instructions.md) → `**` (repository structure overview)
- [editing-conventions.instructions.md](.github/instructions/editing-conventions.instructions.md) → `**/*.md` (general editing rules)
- [markdown-notes.instructions.md](.github/instructions/markdown-notes.instructions.md) → `general/**/*.md`
- [special.instructions.md](.github/instructions/special.instructions.md) → `special/**/*.md`, `special/**/*.py`
- [archives.instructions.md](.github/instructions/archives.instructions.md) → `archives/**/*.md`
- [commit-convention.instructions.md](.github/instructions/commit-convention.instructions.md) → `**` (enforce conventional commit usage for agent-made commits; prompt for flashcard counts and append machine-readable trailers when changes affect `general/`, `special/`, or `self/`; see it for the `commit-staged-flashcard-progress` prompt and flashcard progress commit format.)

### Workflows

- [core-workflows.instructions.md](.github/instructions/core-workflows.instructions.md) → `**` (command-line workflows)

### Tools

- [init-wrapper.instructions.md](.github/instructions/init-wrapper.instructions.md) → `init.py`

### LaTeX & config

- [latex-preamble.instructions.md](.github/instructions/latex-preamble.instructions.md) → `.obsidian/plugins/obsidian-latex/preamble.sty`
- [config-folders.instructions.md](.github/instructions/config-folders.instructions.md) → `.git/**`, `.obsidian/**`, `.vscode/**`

### Submodule guards

- [submodule-self.instructions.md](.github/instructions/submodule-self.instructions.md) → `self/**`
- [submodule-private.instructions.md](.github/instructions/submodule-private.instructions.md) → `private/**`
- [submodule-pytextgen.instructions.md](.github/instructions/submodule-pytextgen.instructions.md) → `tools/pytextgen/**`
- [submodule-pyarchivist.instructions.md](.github/instructions/submodule-pyarchivist.instructions.md) → `tools/pyarchivist/**`

## Agent skills

Enable `chat.useAgentSkills` in VS Code for auto-loading. See `.github/skills/` for details:

### Content creation & ingestion

- **[wiki-ingestion](.github/skills/wiki-ingestion/SKILL.md)** — Import Wikipedia articles, normalize links/media, scaffold new notes
- **[tools-templates](.github/skills/tools-templates/SKILL.md)** — Template scaffolding, YAML conventions, pytextgen fence templates
- **[pytextgen](.github/skills/pytextgen/SKILL.md)** — Regenerate/clear content blocks, fence syntax, cloze markup, debugging
- **[academic-notes](.github/skills/academic-notes/SKILL.md)** — Writing notes in academic course style: frontmatter conventions, index & weekly structure, flashcard metadata, cross-references, and scaffolding templates (institution-agnostic)

### Tools & workflows

- **[tools](.github/skills/tools/SKILL.md)** — Repository-wide tooling overview, tool coordination, dependency management
- **[tools-special](.github/skills/tools-special/SKILL.md)** — LMS converters (Canvas/HKUST Zinc), course catalog fetchers, academic workflows
- **[pyarchivist](.github/skills/pyarchivist/SKILL.md)** — Archive online content, auto-maintain `index.md`, media management

**Skill flow**: Most workflows use multiple skills in sequence; see individual skill files for cross-references and integration guidance.

## Recent updates (agent guidance)

- 2026-02-09: Added `.github/instructions/agent-quickstart.instructions.md` — a one-page checklist for AI agents (startup commands, quick gotchas, test/format sequence, and submodule guardrails). Linked core instruction files and submodule AGENTS.md to improve discoverability and cohesion.
- 2026-02-09: Updated commit message guidance — agents should prefer wrapping commit body lines to **72 characters** (readability/buffer). Tooling (commitlint) continues to enforce a **100-character** hard limit, so ensure lines are ≤100 to pass.

## AI agent quickstart ✅

- See `.github/instructions/agent-quickstart.instructions.md` for a concise checklist agents should follow before changing files or making commits.
- Recommended workspace settings: `chat.useAgentsMdFile = true`, `chat.useAgentSkills = true` to enable skill-based guidance and the root `AGENTS.md` for context.
- Safe startup: `pnpm install` → `pnpm run prepare` → `pnpm run format` → `pnpm run check` → `pnpm run test`.
- Regenerate content before packaging: `uv run -m init generate -C`; use `uv run -m pack` and `uv run -m publish` only after tests pass and user approval for publishing sensitive content.
- Always follow `.github/instructions/commit-convention.instructions.md` for agent-made commits (Conventional Commits, trailer rules); **prefer wrapping commit body lines to 72 characters or fewer for readability and buffer, but ensure lines are ≤100 to pass commitlint.**
- Ask for explicit permission before editing `private/`, `self/`, or any submodule content; update that submodule's `AGENTS.md` and `.github/instructions/` when you introduce new commands or workflows.
- Use the Todo List Tool for multi-step tasks and include short, test-backed PRs with a clear rationale when making non-trivial changes.
