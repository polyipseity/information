---
name: Content organization
description: High-level overview of repository structure and content organization principles
applyTo: "**"
---

# Content Organization & Repository Structure

This repository is a personal Markdown knowledgebase with flashcards, tutorials, and archived online content. Content is organized by type and purpose for clarity and predictable tooling.

## Directory structure

- **`general/`** — Encyclopedic content (mostly verbatim from Wikipedia).
  - Flat `.md` files with YAML frontmatter (`aliases`, `tags`, `language`).
  - Use **relative links** (encode spaces as `%20`) and store media under `archives/Wikimedia Commons/`.
  - Updated primarily via: `uv run -m convert_wiki`.

- **`special/`** — Specialized materials: course notes, tutorials, and frameworks.
  - `academia/` is organized by **institution → semester/year → course**; each institution typically includes `reviews.md` and course folders.
  - Maintain `index.md` files for listings and cross-references.

- **`archives/`** — Downloaded online content (media, pages, documents).
  - Subfolders: `Wikimedia Commons/` (media), `sparse/` (misc files).
  - Each archive directory should include an `index.md` with source URL, timestamp and description.

- **`scripts/`** — Scripts and utilities (wiki ingestion, LMS converters, packaging, publishing).
  - Prefer running wrappers (`bun run ...` or `uv run -m ...`) rather than hand-editing generated outputs.
    Agent quickstart: For a one-page checklist of startup steps, commit rules, and quick gotchas see `.agents/instructions/agent-quickstart.instructions.md` (enable `chat.useAgentsMdFile` and `chat.useAgentSkills` for integrated guidance).

---

## Intent & ownership

- This is **primarily a public knowledgebase**; most content (encyclopedic articles, tutorials, course notes) is intended to be public and editable by maintainers.
- Small, well-documented fixes are welcome via PRs. Avoid bulk or automated rewrites unless there is an agreed plan and review.

## Git submodules

- Common submodules: **`private/`**.
- `self/stash/` is part of the parent repository and stores scratch scripts; treat it as ordinary repo content, not as a git submodule.

## Course content & migrations

- Notes under `special/academia` are expected to be public by default. Use the `academic-notes` skill to validate structure and metadata.
- To propose moving content from `private/` to public, run the validator and attach its output to the migration request:

```sh
uv run .agents/skills/academic-notes/check.py --content private/special/academia/<INSTITUTION>
```

- Use the `publish` workflow to mirror filtered content from `private/` to the public repository (this preserves history and applies filtering rules). Do not copy private files into the public tree manually.

## When to use `private/` vs public folders

- Keep content public unless it contains **PII**, confidential academic records, commercial/embargoed research, contracts, or other sensitive material.
- If in doubt, place content in `private/` and consult the repository owner. Follow the publish/migration checklist (PII/license/redaction/validation) before requesting a public migration.

---

## Developer tooling & testing conventions

- Use `pyproject.toml` as the authoritative Python dependency manifest. Keep runtime dependencies in `[project].dependencies`, developer tools in `[dependency-groups].dev`, and the full union of packages referenced by inline `# /// script` metadata in `[dependency-groups].scripts`. Inline script metadata should (1) begin with `#!/usr/bin/env python` shebang on line 1, (2) keep keys alphabetized, and (3) set `requires-python = ">=3.13.0"`. Running `bun install` will trigger `prepare`, which runs `uv sync` to install dev extras from `pyproject.toml` using the project's `uv.lock`.
- Tests: Place tests under `tests/`, mirror the source layout when possible, and use `pytest` (`test_*.py` naming). Add tests for any script, tool or instruction change (especially changes that affect content generation or publishing). Use `pytest.mark.anyio` for async tests (AnyIO pytest plugin).
- Async helper code should use AnyIO/Asyncer (`create_task_group`, `soonify`, `asyncify`, `syncify`, `runnify`) rather than importing `asyncio` directly. See agent quickstart for examples; this applies to any Python utilities under `scripts/` or `special/`.
- Hooks & automation: Register Husky hooks with `bun run prepare`. Pre-commit runs lint-staged which runs markdown and code formatters; pre-push runs the test suite to avoid broken pushes.
- Local validation: Before committing or opening a PR run `bun run format` and `bun run check` and `bun run test` locally. When only a subset of files are affected, supply explicit paths to the commands (for example `bun run check:md --no-globs file1.md file2.md`) so they run quickly instead of scanning the whole repo.

---

## Other important files

- **`.obsidian/plugins/obsidian-latex/preamble.sty`** — LaTeX macros used by Extended MathJax in Obsidian.
- **`.git/`**, **`.github/`**, **`.obsidian/`**, **`.vscode/`** — configuration and workspace files (do not edit unless explicitly requested).
