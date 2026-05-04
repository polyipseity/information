---
name: Submodule pytextgen
description: scripts/pytextgen is a submodule; only edit when user explicitly requests
applyTo: "scripts/pytextgen/**"
---

# Submodule PyTextGen Guidelines

- This is a git submodule for the pytextgen content generation library (external dependency)
- **Default behavior**: Avoid editing unless user explicitly requests it
- **If editing is needed but not requested**: Ask the user for permission first
- **When user approves edits**: Make changes here, test thoroughly, then contribute upstream
- For upstream contributions: work in the pytextgen repo, merge changes, then update submodule pointer
- **Submodule instructions**: This submodule has its own `AGENTS.md` and `.agents/instructions/` and `.agents/skills/` files that take priority when working within `scripts/pytextgen/`. Agents: consult `.agents/instructions/agent-quickstart.instructions.md` and the submodule `AGENTS.md` before editing; pytextgen fences and flashcard markup (cloze `{@{ }@}`, two-sided `::@::`,
and one-sided `:@:`) are sensitive and must not be altered without explicit
intent and tests.

## Developer tooling & testing (pytextgen submodule)

- If you must edit `scripts/pytextgen/`, add unit tests for new behavior and integration tests that demonstrate correct generation of fences and flashcards. Place tests under the submodule's `tests/` and ensure they run in CI for the submodule; also add coordination tests in the parent repo where meaningful.
- When writing or modifying any async helpers or utilities inside pytextgen, prefer AnyIO/Asyncer patterns rather than importing `asyncio`.  Import `create_task_group`, `soonify`, `asyncify`, etc. from Asyncer for improved typing and consistency with the parent repo.
- Ensure changes to pytextgen APIs preserve backwards compatibility or document breaking changes and add migration notes.
- When updating the submodule pointer in the parent repo, include a short commit message `chore(submodules): update pytextgen to <ref>` and run the parent repo `bun run check` and `bun run test` to validate integration (use explicit file/path arguments when feasible to speed up these commands).
