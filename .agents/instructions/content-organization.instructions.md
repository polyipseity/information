---
name: Content organization
description: High-level overview of repository structure and content organization principles
applyTo: "**"
---

# Content Organization & Repository Structure

This repository is a personal Markdown knowledgebase with flashcards, tutorials, and archived online content. Content is organized by type and purpose for clarity and predictable tooling.

## Directory structure

- __`general/`__ — Wikipedia articles (verbatim). Flat `.md` with YAML frontmatter. Use relative links (`%20` encoding), media in `archives/Wikimedia Commons/`. Updated via `uv run -m scripts.convert_wiki --clipboard`.
- __`special/`__ — Course notes, tutorials, frameworks. `academia/` organized by institution → semester → course. Maintain `index.md` files.
- __`archives/`__ — Downloaded media and pages. Each subdirectory needs `index.md` with source URL, timestamp, description.
- __`scripts/`__ — Utilities. Prefer `bun run ...` or `uv run -m ...` wrappers.

---

## Intent & ownership

- This is __primarily a public knowledgebase__; most content (encyclopedic articles, tutorials, course notes) is intended to be public and editable by maintainers.
- Small, well-documented fixes are welcome via PRs. Avoid bulk or automated rewrites unless there is an agreed plan and review.

## Git submodules

- Common submodules: __`private/`__.
- `self/stash/` is part of the parent repository and stores scratch scripts; treat it as ordinary repo content, not as a git submodule.

## Migrations from private/

Use `publish` to mirror filtered content from `private/` to public. Run the validator first:

```sh
uv run .agents/skills/academic-notes/check.py --content private/special/academia/<INSTITUTION>
```

Do not copy private files into the public tree manually.

## Public vs private

Keep content public unless it contains PII, confidential academic records, commercial/embargoed research, or contracts. If in doubt, place in `private/` and consult the owner.
