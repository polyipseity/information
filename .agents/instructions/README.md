# Instruction files index (README.md)

This index summarizes the repository instruction files under `.agents/instructions/` to help agents and maintainers find the authoritative guidance quickly.

| File | Purpose | applyTo |
| --- | --- | --- |
| `core-workflows.instructions.md` | Startup checklist, workflows, and repo gotchas | `**` |
| `commit-convention.instructions.md` | Commit/PR message rules and trailers | `**` |
| `content-organization.instructions.md` | Repo structure and content layout | `**` |
| `editing-conventions.instructions.md` | Markdown editing rules, cloze/pytextgen guards, config folder policy, skill integrations | `**/*.md` |
| `python-entry-points.instructions.md` | Python `__name__ == "__main__"` entry point convention | `**/*.py` |
| `special.instructions.md` | Conventions for `special/` content and tooling | `special/**/*.md, special/**/*.py` |
| `submodule-pyarchivist.instructions.md` | Guardrails for `scripts/pyarchivist` submodule | `scripts/pyarchivist/**` |
| `submodule-private.instructions.md` | Guardrails for `private/` submodule | `private/**` |
| `submodule-pytextgen.instructions.md` | Guardrails for `scripts/pytextgen` submodule | `scripts/pytextgen/**` |
| `submodule-self.instructions.md` | Guardrails for `self/*` submodules | `self/arts/**, self/capture the flag/**, self/ledger/**, self/passwords/**, self/polyipseity/**` |

Each instruction file contains its own metadata (`name`, `description`, `applyTo`, etc.) in the YAML frontmatter. Only `name`, `description`, and `applyTo` are supported keys – do not add other fields to instruction frontmatter, as they will be ignored.

> __Note:__ Skills use a different set of allowed keys and no longer support `applyTo`.  See `.agents/skills/README.md` for details.
