---
name: Editing conventions
description: General editing rules for Markdown notes, links, formatting, and submodules
applyTo: "**/*.md"
---

# Editing Conventions

## General editing rules

- **Frontmatter**: Keep YAML (`aliases`, `tags`, `language/in/English`) intact. Avoid adding unauthorized fields; add new fields only with user approval.

- **Cloze markup**: Preserve `{@{ ... }@}`, `::@::`, and `:@:` unchanged; do not reflow or escape. These are used for flashcard generation.

Agent quickstart pointer: See `.github/instructions/agent-quickstart.instructions.md` for a concise agent checklist and quick repository gotchas (preserve pytextgen fences, don't reflow cloze markup, and prefer `pnpm run <script>` wrappers for reproducible runs).

- **pytextgen fences**: Do not modify `# pytextgen generate ...` comments, fence delimiters, or `return export_seq(...)` signatures. These are parsed by pytextgen; breaking them prevents regeneration.

- **Links**: Always relative with `%20` encoding (not `%3A` or other encodings). Use `archives/` for shared media.

- **Math**: Keep KaTeX `$...$` (inline) and `$$...$$` (block) intact; don't wrap or escape.

- **Formatting**: Respect `.markdownlint.json` settings (MD013/MD033/MD051 disabled). Avoid rewrapping existing lines; preserve layout.

## Submodule editing policy

- **Default behavior**: Treat as read-only; ask user for permission if editing seems necessary
- **`self/**`**, **`private/**`**: Managed in separate upstream repositories
- **`tools/pytextgen/`**, **`tools/pyarchivist/`**: External dependencies
- **When user approves edits**: Make changes here, test thoroughly, then contribute upstream
- **Priority**: Follow the submodule's own `AGENTS.md` first (submodule instructions take priority)

## Config folder policy

- **`.git/`, `.obsidian/`, `.vscode/`**: Do not edit unless explicitly requested; use UI tools to modify app settings

## Formatting & linting

- **markdownlint**: Configuration in `.markdownlint.json` (root, `tools/`, `special/`, `archives/`) disables MD013 (line length), MD033 (HTML blocks), MD051 (link spacing)
- **running markdownlint-cli2**: when invoking the CLI with explicit file paths or filenames (for example `pnpm run check:md file1.md file2.md` or `pnpm run format:md file1.md`), **always** include `--no-globs` and list the exact files you want to process.  Without `--no-globs` markdownlint-cli2 will treat the arguments as a glob pattern, which may cause it to scan the entire repository instead of just the files you specified.  This applies whether you call the command directly or via a pnpm script.

  - Respects and preserves existing formatting; avoid auto-reformatting unless requested
  - Useful for validating structure without breaking KaTeX or special layouts

- **YAML frontmatter**: `aliases`, `tags`, `language/in/English` are standard fields; preserve during edits

- **KaTeX math**: `$inline$` and `$$display$$` formats untouched; Extended MathJax in Obsidian uses `.obsidian/plugins/obsidian-latex/preamble.sty` for custom macros

## Developer tooling & testing conventions

- Dependency management: `pyproject.toml` is authoritative; add runtime deps to `[project].dependencies` and developer/test tools to `[dependency-groups].dev`. Run `pnpm install` (which triggers `prepare`, running `uv sync`) to register Husky hooks and install dev extras locally.
- Tests: Place tests in `tests/` and use `pytest` (`test_*.py` naming). Mirror source layout when helpful, and add unit and integration tests for any change to scripts or generators.
- Async tests: Use `pytest-asyncio` and `pytest.mark.asyncio` for async code. Prefer deterministic fixtures like `tmp_path: os.PathLike[str]` and `monkeypatch`. When typing tests, annotate `tmp_path` parameters as `PathLike[str]`; and when converting `PathLike` objects to strings **always** use `os.fspath(path_like)` rather than `str(path_like)`.
- Local validation: Run `pnpm run format`, `pnpm run check`, and `pnpm run test` before pushing changes to avoid Husky hooks and CI failures.  When only a subset of files are affected, supply explicit paths to these commands so they complete quickly instead of scanning the entire repo.
