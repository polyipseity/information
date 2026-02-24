---
name: Agent quickstart
description: One-page checklist for AI agents to get productive in this repository
applyTo: "**"
---

# Agent quickstart ✅

This file is a short, actionable checklist for an AI agent (or new contributor) to become productive quickly in this repository. It complements `AGENTS.md` and the repository's instruction files; read the referenced docs for full details.

1. Workspace configuration
   - Enable `chat.useAgentsMdFile = true` and `chat.useAgentSkills = true` in the IDE to let agent skills and the root `AGENTS.md` guide behavior.
   - Consult individual `SKILL.md` frontmatter for skill metadata. Allowed keys are `name`, `description` plus the small set of optional fields documented in `.github/skills/README.md`. Instruction files only support `name`, `description`, and `applyTo`.

     > **Warning:** `applyTo` is no longer valid in skill files. Do not include it when creating new skills; it remains allowed in instruction files only.

2. First commands (safe startup)
   - `pnpm install`  # installs Node deps and triggers Python dev extras install
   - `pnpm run prepare`  # register Husky Git hooks
   - `pnpm run format` && `pnpm run check`  # formatting & lint checks (when targeting specific files with `check:md` or `format:md`, remember to append `--no-globs` and list the explicit filenames to avoid accidentally processing the entire repo; in general, when running any pnpm script prefer supplying explicit paths to limit work and speed up the command)
   - `pnpm run test`  # run tests locally (pre-push runs this automatically)

3. Common repository actions
   - Regenerate generated content: build workflows handle this automatically; manual `uv run -m init generate -C` is rarely needed and agents should not suggest it (see `core-workflows.instructions.md`).
   - Ingest a Wikipedia page: `uv run -m "templates.new wiki page"` → `uv run -m "convert wiki"` (flashcards are created by the build; no manual generation step)
   - Package: `uv run -m pack -o pack.zip ...` (generated content will already be fresh)
   - Publish (private→public): `uv run -m publish --paths-file <file>` (exercise caution)

Repository gotchas & quick tips

- Preserve `# pytextgen` fences and cloze markup (`{@{ ... }@}`, `::@::`, `:@:`). These are parsed automatically; do not reflow or escape them.
- Always prefer `pnpm run <script>` wrappers; if invoking Python directly, set `cwd=scripts/` when required.
- Generated content is refreshed automatically; agents should not advise running `uv run -m init generate -C` before pack or publishing workflows.
- Use the Todo List Tool for multi-step tasks and present the proposed commit message to the user before committing (see `commit-convention.instructions.md`).

1. Commit & PR behavior (must follow `commit-convention.instructions.md`)
   - Always present the proposed commit message to the user for confirmation.
   - Use Conventional Commits and ensure commitlint passes (no body line > 100 chars).
   - Run `pnpm run format` and `pnpm run check` before committing. Use the Todo List Tool for multi-step changes and show progress.

2. Submodule & sensitive data rules
   - **Do not** modify `private/`, `self/` or a submodule's contents without explicit owner approval; check the submodule `AGENTS.md` first.
   - Avoid exposing or handling PII unless instructed and explicitly approved by the repository owner.

3. Tests, types, and CI
   - Add/modify tests under `tests/` mirroring source layout. Use `pytest` and `pytest.mark.asyncio` for async tests when relevant.
   - Typing guidance: prefer PEP 585 built-in generics for concrete containers (e.g. `list[str]`, `dict[str, int]`) and use `collections.abc` for abstract interfaces (e.g. `collections.abc.Sequence[str]`, `collections.abc.Mapping[str, int]`). Avoid `typing.List`/`typing.Dict`/`typing.Sequence` in new code.
   - Run `pyright`/`pnpm run check` and `pnpm run test` locally to reduce CI failures.

4. When in doubt
   - Ask the user one short clarifying question before making non-trivial changes (e.g., “Should I modify `special/` or only add tests?”).
   - If the user is unavailable, prepare a short PR draft with the rationale and tests, and ask for approval.

---

Keep this file concise — for detailed guidance see `AGENTS.md`, `.github/instructions/`, and the `SKILL.md` files in `.github/skills/`.
