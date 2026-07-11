---
name: Core workflows
description: Common commands, startup checklist, repo gotchas, and workflows for agents
applyTo: "**"
---

# Core Workflows

## Quick-start checklist

1. Enable `chat.useAgentsMdFile = true` and `chat.useAgentSkills = true` in the IDE to let agent skills and the root `AGENTS.md` guide behavior.
2. Safe startup:

   ```bash
   bun install            # installs Node deps and triggers Python dev extras install
   bun run prepare        # register prek hooks
   bun run format && bun run check  # formatting & lint checks
   bun run test           # run tests locally (pre-push runs this automatically)
   ```

   When targeting specific files with `check:md` or `format:md`, always append `--no-globs` and list the explicit filenames to avoid accidentally processing the entire repo.

3. Adopt a simplification-first mindset: before adding new code, verify whether deletion or inlining would suffice.

## Repository gotchas

- __🔥 CRITICAL: Never `cd` into `.agents/skills/` to run `uv` commands.__ Always run `uv` from the repo root. Running `uv` inside a skill folder creates `.venv/`/`uv.lock` trash there and fails due to missing deps.
- Preserve `# pytextgen` fences and flashcard markup. There are three forms: cloze deletions `{@{...}@}` (common), two-sided pairs `::@::` (one line only, creates two cards), and one-sided pairs `:@:` (one line only, single card). These are parsed automatically; do not reflow, escape, or split them across lines.
- Async code should __not__ import or use `asyncio` directly. Use AnyIO for cross-platform structured concurrency and the Asyncer helper library for enhanced editor/typing support. Key Asyncer helpers: `create_task_group` (preferred over `anyio.create_task_group`), `soonify` for concurrent calls with `SoonValue` return, `runnify` for wrapping async main for sync entry points (__all Python scripts use this; see `python-entry-points.instructions.md`__), `asyncify` for blocking sync code from async context, `syncify` for calling async from sync context.
- Always prefer `bun run <script>` wrappers; if invoking Python directly, set `cwd=scripts/` when required.
- When writing shell commands for Python in a PowerShell terminal, use a here-string and pipe into `uv run python -`. For POSIX shells, regular heredocs work fine.
- For standalone Python files that use inline `# /// script` metadata: (1) begin with `#!/usr/bin/env python` shebang on line 1, (2) keep metadata keys alphabetized (`dependencies`, `requires-python`, `timestamp`), (3) set `requires-python = ">=3.13.0"` (inline scripts target >=3.13.0; the project minimum in AGENTS.md is >=3.14 — the higher bar is intentional for the full project), and (4) mirror the union of every inline-script dependency in `pyproject.toml`'s `[dependency-groups].scripts` even when a package is also present in `[project].dependencies`.
- Generated content (flashcards, pytextgen blocks) is refreshed automatically by build workflows. Agents should __not__ run `uv run -m init generate` themselves. The command syntax is provided below for human reference only.
- Use the Todo List Tool for multi-step tasks and present the proposed commit message to the user before committing (see `commit-convention.instructions.md`).

## Common workflows

### Regenerate generated regions (human reference)

__Command__: `uv run -m init generate [pytextgen flags] <paths?>`

The `init.py` wrapper auto-discovers `.md` files (excluding `.git`, `.obsidian`, `tools`), caches `(mtime, inode, text)` to skip unchanged files, and normalizes newlines to `\n` before passing to pytextgen. Common flags: `-C`/`--no-cached` (rebuild cache), `--no-code-cache` (bypass compile cache), `--init-flashcards` (seed flashcard state), `<paths>` (limit scope).

### Clear generated content (human reference)

__Command__: `uv run -m init clear --type CONTENT <paths?>`

Clears generated content blocks without regenerating. Useful for resolving merge conflicts.

### Wiki ingestion

- Scaffold: `uv run -m scripts.new_wiki_page`
- Ingest: `uv run -m scripts.convert_wiki` (reads clipboard HTML)
- Flashcards: handled automatically by build workflows
- __See__: [wiki-ingestion](../skills/wiki-ingestion/SKILL.md) skill for step-by-step guidance

### Package bundle

__Command__: `uv run -m pack -o pack.zip -n 25 --damping-factor 0.5 --page-rank-iterations 100 <paths>`

Creates PageRank-sorted zip with link-closure metadata. Generated content is usually up-to-date; manual `uv run -m init generate` is unnecessary.

### Publish bridge

__Command__: `uv run -m publish --paths-file <file>`

Mirrors filtered history from `private/.git` into public `.git` using `git filter-repo`.

## Commit & PR behavior

- Always present the proposed commit message to the user for confirmation.
- Use Conventional Commits and ensure commitlint passes (no body line > 100 chars).
- Run `bun run format` and `bun run check` before committing.
- __Full details__: [commit-convention.instructions.md](commit-convention.instructions.md) — includes flashcard trailers, learn/review session commit formats, and commitlint compliance.

## Submodule & sensitive data rules

- __Do not__ modify `private/` without explicit owner approval; check the submodule's `AGENTS.md` first.
- `self/stash/` is not a submodule, but it is still user-owned scratch space; only edit it when the user explicitly asks.
- Avoid exposing or handling PII unless instructed and explicitly approved by the repository owner.
- `scripts/pyarchivist/` and `scripts/pytextgen/` are submodules; only edit when user explicitly requests.
- `self/arts/`, `self/capture the flag/`, `self/ledger/`, `self/passwords/`, `self/polyipseity/` are submodules; prefer upstream edits.

## Tests, types, and CI

- Add/modify tests under `tests/` mirroring source layout. Use `pytest` and `pytest.mark.anyio` for async tests when relevant.
- Typing guidance: prefer PEP 585 built-in generics for concrete containers (e.g. `list[str]`, `dict[str, int]`) and use `collections.abc` for abstract interfaces (e.g. `collections.abc.Sequence[str]`). Avoid `typing.List`/`typing.Dict`/`typing.Sequence` in new code.
- Run `uv run --locked ty check`/`bun run check` and `bun run test` locally to reduce CI failures.

## Related instructions

- [content-organization](content-organization.instructions.md): Directory structure and conventions
- [editing-conventions](editing-conventions.instructions.md): General editing rules for Markdown files
- [markdown-notes](markdown-notes.instructions.md): Specific conventions for general/\*\*.md files
- [special](special.instructions.md): Conventions for specialized content
