---
name: Submodule pytextgen
description: scripts/pytextgen is a submodule; only edit when user explicitly requests
applyTo: "scripts/pytextgen/**"
---

# Submodule PyTextGen Guidelines

Unique rules for this submodule:

- __Fence sensitivity__: pytextgen fences and flashcard markup (cloze `{@{ }@}`, two-sided `::@::`, one-sided `:@:`) must not be altered without explicit intent and tests.
- __API changes__: Preserve backward compatibility or document breaking changes with migration notes.
- __Submodule pointer update__: Use commit message `chore(submodules): update pytextgen to <ref>` and run `bun run check && bun run test` in the parent repo.
- This submodule has its own `AGENTS.md` and `.agents/` that take priority when working inside `scripts/pytextgen/`.
