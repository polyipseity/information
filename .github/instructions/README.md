# Instruction files index (README.md)

This index summarizes the repository instruction files under `.github/instructions/` to help agents and maintainers find the authoritative guidance quickly.

| File | Purpose | applyTo |
| --- | --- | --- |
| `agent-quickstart.instructions.md` | One-page checklist for agents (startup, tests, quick gotchas) | `**` |
| `core-workflows.instructions.md` | Command-line workflows (generate, pack, publish) | `**` |
| `content-organization.instructions.md` | Repo structure and content layout | `**` |
| `editing-conventions.instructions.md` | Markdown editing rules, cloze/pytextgen guards | `**/*.md` |
| `markdown-notes.instructions.md` | Conventions for `general/` encyclopedia notes | `general/**/*.md` |
| `special.instructions.md` | Conventions for `special/` content and tooling | `special/**/*.md, special/**/*.py` |
| `init-wrapper.instructions.md` | Guardrails for `init.py` (pytextgen wrapper) | `init.py` |
| `commit-convention.instructions.md` | Commit/PR message rules and trailers for agents | `**` |
| `latex-preamble.instructions.md` | Editing rules for `.obsidian` LaTeX preamble | `.obsidian/plugins/obsidian-latex/preamble.sty` |
| `submodule-*.instructions.md` | Submodule guardrails (see submodule-specific AGENTS.md) | `self/**`, `private/**`, `tools/pytextgen/**` |

Each instruction file contains its own metadata (`name`, `description`, `applyTo`, etc.) in the YAML frontmatter. Only `name`, `description`, and `applyTo` are supported keys – do not add other fields to instruction frontmatter, as they will be ignored.

> **Note:** Skills use a different set of allowed keys and no longer
> support `applyTo`.  See `.github/skills/README.md` for details.

If you want this index extended (per-skill or per-submodule), tell me which areas to prioritise and I will expand it.
