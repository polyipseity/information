---
name: Editing conventions
description: General editing rules for Markdown notes, links, formatting, and submodules
applyTo: "**/*.md"
---

# Editing Conventions

## General editing rules

- **Frontmatter**: Keep YAML (`aliases`, `tags`, `language/in/English`) intact. Avoid adding unauthorized fields; add new fields only with user approval.

- **Cloze & flashcard markup**: Preserve the three patterns exactly and understand what they do:
  - `{@{ hidden text }@}` – cloze deletion; the inner text is hidden when the card is shown and must be recalled. (Most common.) **Closing delimiter:** place `}@}` **before** any trailing punctuation so punctuation sits outside the cloze (e.g. `{@{text}@}.` not `{@{text.}@}`).
  - `::@::` – two‑sided question/answer pair on a single Markdown line; creates two cards (left→right and right→left). Use `<br/>` for line breaks or `<p>` for paragraphs if needed, but keep the source line literal.
  - `:@:` – one‑sided question/answer pair on a single Markdown line; creates a single card where the right side is recalled from the left. Same line‑only rule applies.
    Do **not** reflow, escape, or split any of these markers across lines; altering spacing or wrapping can break generation.

Agent quickstart pointer: See `.agents/instructions/agent-quickstart.instructions.md` for a concise agent checklist and quick repository gotchas (preserve pytextgen fences, don't reflow cloze markup, and prefer `bun run <script>` wrappers for reproducible runs).

- **pytextgen fences**: Do not modify `# pytextgen generate ...` comments, fence delimiters, or `return export_seq(...)` signatures. These are parsed by pytextgen; breaking them prevents regeneration.

- **Links**: Always relative with `%20` encoding (not `%3A` or other encodings). Use `archives/` for shared media.

- **Math**: Keep KaTeX `$...$` (inline) and `$$...$$` (block) intact; don't wrap or escape.

- **Formatting**: Respect `.markdownlint.json` settings (MD013/MD033/MD051 disabled). Avoid rewrapping existing lines; preserve layout. For emphasis in Markdown, prefer underscore: `_italic_` and `__bold__` (not `*`/`**`) so formatting is consistent and asterisks are reserved for lists and math.

## Submodule editing policy

- **Default behavior**: Treat as read-only; ask user for permission if editing seems necessary
- **`self/arts/**`**, **`self/capture the flag/**`**, **`self/ledger/**`**, **`self/passwords/**`**, **`self/polyipseity/**`**, **`private/**`**: Managed in separate upstream repositories
- **`scripts/pytextgen/`**, **`scripts/pyarchivist/`**: External dependencies
- **`self/stash/`**: Part of the parent repo rather than a git submodule; still treat it as user-owned scratch space and avoid editing it unless requested.
- **When user approves edits**: Make changes here, test thoroughly, then contribute upstream
- **Priority**: Follow the submodule's own `AGENTS.md` first (submodule instructions take priority)

## Config folder policy

- **`.git/`, `.obsidian/`, `.vscode/`**: Do not edit unless explicitly requested; use UI tools to modify app settings

## Formatting & linting

- **markdownlint**: Configuration in `.markdownlint.json` (root, `scripts/`, `special/`, `archives/`) disables MD013 (line length), MD033 (HTML blocks), MD051 (link spacing)
- **running markdownlint-cli2**: when invoking the CLI with explicit file paths or filenames (for example `bun run check:md file1.md file2.md` or `bun run format:md file1.md`), **always** include `--no-globs` and list the exact files you want to process. Without `--no-globs` markdownlint-cli2 will treat the arguments as a glob pattern, which may cause it to scan the entire repository instead of just the files you specified. This applies whether you call the command directly or via a bun script.
  - Respects and preserves existing formatting; avoid auto-reformatting unless requested
  - Useful for validating structure without breaking KaTeX or special layouts

- **YAML frontmatter**: `aliases`, `tags`, `language/in/English` are standard fields; preserve during edits

- **KaTeX math**: `$inline$` and `$$display$$` formats untouched; Extended MathJax in Obsidian uses `.obsidian/plugins/obsidian-latex/preamble.sty` for custom macros

## Developer tooling & testing conventions

- Dependency management: `pyproject.toml` is authoritative; add runtime deps to `[project].dependencies`, developer/test tools to `[dependency-groups].dev`, and the union of dependencies used in inline `# /// script` metadata to `[dependency-groups].scripts`. Inline script metadata should (1) begin with `#!/usr/bin/env python` shebang on line 1, (2) keep keys alphabetized, and (3) set `requires-python = ">=3.13.0"`. Run `bun install` (which triggers `prepare`, running `uv sync`) to register Husky hooks and install dev extras locally.
- Tests: Place tests in `tests/` and use `pytest` (`test_*.py` naming). Mirror source layout when helpful, and add unit and integration tests for any change to scripts or generators.
- Async tests: Prefer `@pytest.mark.anyio` with the AnyIO pytest plugin and import concurrency helpers from Asyncer (`create_task_group`, `soonify`, `asyncify`) instead of calling `anyio.create_task_group` directly. Avoid using event-loop runners inside tests. Prefer deterministic fixtures like `tmp_path: os.PathLike[str]` and `monkeypatch`. When typing tests, annotate `tmp_path` parameters as `PathLike[str]`; and when converting `PathLike` objects to strings **always** use `os.fspath(path_like)` rather than `str(path_like)`.
- Local validation: Run `bun run format`, `bun run check`, and `bun run test` before pushing changes to avoid Husky hooks and CI failures. When only a subset of files are affected, supply explicit paths to these commands so they complete quickly instead of scanning the entire repo.
