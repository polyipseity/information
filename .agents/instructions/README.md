# Instruction files index (README.md)

This index summarizes the repository instruction files under `.agents/instructions/` to help agents and maintainers find the authoritative guidance quickly.

| File | Purpose | applyTo |
| --- | --- | --- |
| `core-workflows.instructions.md` | Startup checklist, workflows, and repo gotchas | `**` |
| `commit-convention.instructions.md` | Commit/PR message rules and trailers | `**` |
| `editing-conventions.instructions.md` | Markdown editing rules, cloze/pytextgen guards, config folder policy, skill integrations | `**/*.md` |
| `python-entry-points.instructions.md` | Python `__name__ == "__main__"` entry point convention | `**/*.py` |
| `special.instructions.md` | Conventions for `special/` content and tooling | `special/**/*.md, special/**/*.py` |
| `submodules.instructions.md` | Guardrails for all git submodules (private, pyarchivist, pytextgen, self/*) | `private/**, scripts/pyarchivist/**, scripts/pytextgen/**, self/arts/**, self/capture the flag/**, self/ledger/**, self/passwords/**, self/polyipseity/**` |

Each instruction file contains its own metadata (`name`, `description`, `applyTo`, etc.) in the YAML frontmatter. Only `name`, `description`, and `applyTo` are supported keys – do not add other fields to instruction frontmatter, as they will be ignored.

> __Note:__ Skills use a different set of allowed keys and no longer support `applyTo`.  See `.agents/skills/README.md` for details.
