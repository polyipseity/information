---
name: Core workflows
description: Common commands, startup checklist, repo gotchas, and workflows for agents
applyTo: "**"
---

# Core Workflows

## Quick-start checklist

1. Enable `chat.useAgentsMdFile = true` and `chat.useAgentSkills = true` in the IDE.
2. Safe startup:

   ```bash
   bun install            # installs Node deps + triggers Python dev extras
   bun run prepare        # register prek hooks
   bun run format && bun run check  # formatting & lint checks
   bun run test           # run tests (pre-push runs this automatically)
   ```

   When targeting specific files with `check:md` or `format:md`, append `--no-globs` and list explicit filenames. Only pass `.md` files (see gotchas below).

3. Adopt a simplification-first mindset: before adding new code, verify whether deletion or inlining would suffice.

## Repository gotchas

- __🔥 Never `cd` into `.agents/skills/` to run `uv`.__ Always run `uv` from the repo root. Running inside a skill folder creates `.venv/`/`uv.lock` trash and fails.
- __🔥 Never run `check:md` or `format:md` on non-`.md` files.__ `markdownlint-cli2` corrupts Python, YAML, and other content (wrapping URLs, converting `*`→`_`, removing blank lines, etc.). Use `format:py` (ruff) or `format:prettier` for non-Markdown. Verify every argument ends in `.md`.
- __🔥 Never edit `.markdownlint*` files.__ Hard ban. Report linter config issues to the user instead.
- Prettier does not format `.md` files — never run bare `bun x prettier --write <file.md>`. Use `bun run format:md --no-globs <file.md>`.
- Preserve `# pytextgen` fences and flashcard markup (cloze `{@{...}@}`, two-sided `::@::`, one-sided `:@:`). Do not reflow, escape, or split across lines.
- Do not import `asyncio` directly. Use AnyIO + Asyncer (`create_task_group`, `soonify`, `runnify`, `asyncify`, `syncify`). All Python scripts use `runnify` (see `python-entry-points.instructions.md`).
- Prefer `bun run <script>` wrappers. For Python in PowerShell, use a here-string piped to `uv run python -`.
- Inline `# /// script` metadata: shebang on line 1, keys alphabetized, `requires-python = ">=3.13.0"`, mirror deps in `[dependency-groups].scripts`.
- Agents must not run `uv run -m init generate` — content refreshes automatically via build workflows.
- Use the Todo List Tool for multi-step tasks; present the proposed commit message before committing (see `commit-convention.instructions.md`).

## Common workflows

Commands are for human reference. Agents do not run `uv run -m init generate`.

| Workflow | Command |
| --- | --- |
| Regenerate | `uv run -m init generate [pytextgen flags] <paths?>` |
| Clear | `uv run -m init clear --type CONTENT <paths?>` |
| Scaffold wiki page | `uv run -m scripts.new_wiki_page` |
| Ingest from clipboard | `uv run -m scripts.convert_wiki --clipboard` |
| Update redirect symlinks | `uv run -m scripts.convert_wiki --update-redirects [--dry-run]` |
| Package bundle | `uv run -m pack -o pack.zip -n 25 --damping-factor 0.5 --page-rank-iterations 100 <paths>` |
| Publish private→public | `uv run -m publish --paths-file <file>` |

See [wiki-ingestion](../skills/wiki-ingestion/SKILL.md) for step-by-step guidance.

## Commit & PR behavior

- Present the proposed commit message to the user before committing.
- Use Conventional Commits; ensure commitlint passes (no body line > 100 chars).
- Run `bun run format` and `bun run check` before committing.
- Full details: [commit-convention.instructions.md](commit-convention.instructions.md).

## Submodule & sensitive data rules

- Do not modify `private/` without explicit owner approval.
- `self/stash/` is not a submodule — user-owned scratch space, only edit when asked.
- `scripts/pyarchivist/` and `scripts/pytextgen/` are submodules — edit only when user requests.
- `self/arts/`, `self/capture the flag/`, `self/ledger/`, `self/passwords/`, `self/polyipseity/` are submodules — prefer upstream edits.
- Do not expose or handle PII unless explicitly approved by the repository owner.

## Tests, types, and CI

- __convert_wiki test layout (strict)__: tests belong in `tests/scripts/convert_wiki/`. The only convert_wiki test file allowed directly in `tests/scripts/` is `test_convert_wiki.py`.
- In async filesystem tests, use `anyio.Path` (not `pathlib.Path`) — its methods are coroutines requiring `await`. `symlink_to` is synchronous.
- Run `uv run --locked ty check` and `bun run test` locally before pushing.
