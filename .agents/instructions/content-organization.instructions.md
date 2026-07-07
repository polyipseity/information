---
name: Content organization
description: High-level overview of repository structure and content organization principles
applyTo: "**"
---

# Content Organization & Repository Structure

This repository is a personal Markdown knowledgebase with flashcards, tutorials, and archived online content. Content is organized by type and purpose for clarity and predictable tooling.

## Directory structure

- __`general/`__ — Encyclopedic content (mostly verbatim from Wikipedia).
  - Flat `.md` files with YAML frontmatter (`aliases`, `tags`, `language`).
  - Use __relative links__ (encode spaces as `%20`) and store media under `archives/Wikimedia Commons/`.
  - Updated primarily via: `uv run -m convert_wiki`.

- __`special/`__ — Specialized materials: course notes, tutorials, and frameworks.
  - `academia/` is organized by __institution → semester/year → course__; each institution typically includes `reviews.md` and course folders.
  - Maintain `index.md` files for listings and cross-references.

- __`archives/`__ — Downloaded online content (media, pages, documents).
  - Subfolders: `Wikimedia Commons/` (media), `sparse/` (misc files).
  - Each archive directory should include an `index.md` with source URL, timestamp and description.

- __`scripts/`__ — Scripts and utilities (wiki ingestion, LMS converters, packaging, publishing).
  - Prefer running wrappers (`bun run ...` or `uv run -m ...`) rather than hand-editing generated outputs.
    Agent quickstart: For a one-page checklist of startup steps, commit rules, and quick gotchas see `.agents/instructions/core-workflows.instructions.md` (enable `chat.useAgentsMdFile` and `chat.useAgentSkills` for integrated guidance).

---

## Intent & ownership

- This is __primarily a public knowledgebase__; most content (encyclopedic articles, tutorials, course notes) is intended to be public and editable by maintainers.
- Small, well-documented fixes are welcome via PRs. Avoid bulk or automated rewrites unless there is an agreed plan and review.

## Git submodules

- Common submodules: __`private/`__.
- `self/stash/` is part of the parent repository and stores scratch scripts; treat it as ordinary repo content, not as a git submodule.

## Course content & migrations

- Notes under `special/academia` are expected to be public by default. Use the `academic-notes` skill to validate structure and metadata.
- To propose moving content from `private/` to public, run the validator and attach its output to the migration request:

```sh
uv run .agents/skills/academic-notes/check.py --content private/special/academia/<INSTITUTION>
```

- Use the `publish` workflow to mirror filtered content from `private/` to the public repository (this preserves history and applies filtering rules). Do not copy private files into the public tree manually.

## When to use `private/` vs public folders

- Keep content public unless it contains __PII__, confidential academic records, commercial/embargoed research, contracts, or other sensitive material.
- If in doubt, place content in `private/` and consult the repository owner. Follow the publish/migration checklist (PII/license/redaction/validation) before requesting a public migration.

---

## Developer tooling & testing conventions

Developer tooling and testing conventions are documented in [AGENTS.md](../AGENTS.md) (see the "Developer tooling & testing conventions" section).

---

## Other important files

- __`.obsidian/plugins/obsidian-latex/preamble.sty`__ — LaTeX macros used by Extended MathJax in Obsidian.
- __`.git/`__, __`.github/`__, __`.obsidian/`__, __`.vscode/`__ — configuration and workspace files (do not edit unless explicitly requested).
