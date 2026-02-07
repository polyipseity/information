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
  - Updated primarily via: `python -m "convert wiki"`.

- **`special/`** — Specialized materials: course notes, tutorials, and frameworks.
  - `academia/` is organized by **institution → semester/year → course**; each institution typically includes `reviews.md` and course folders.
  - Maintain `index.md` files for listings and cross-references.

- **`archives/`** — Downloaded online content (media, pages, documents).
  - Subfolders: `Wikimedia Commons/` (media), `sparse/` (misc files).
  - Each archive directory should include an `index.md` with source URL, timestamp and description; `pyarchivist` can auto-update these.

- **`tools/`** — Scripts and utilities (wiki ingestion, LMS converters, packaging, publishing).
  - Prefer running wrappers (`pnpm run ...` or `python -m ...`) rather than hand-editing generated outputs.
  - Notable submodules: `tools/pytextgen/` and `tools/pyarchivist/` (treat as external tools).

---

## Intent & ownership

- This is **primarily a public knowledgebase**; most content (encyclopedic articles, tutorials, course notes) is intended to be public and editable by maintainers.
- Small, well-documented fixes are welcome via PRs. Avoid bulk or automated rewrites unless there is an agreed plan and review.

## Git submodules

- Common submodules: **`self/`** (personal metadata), **`private/`** (private mirrored content), **`tools/pytextgen/`**, **`tools/pyarchivist/`**.
- When working inside a submodule, check its local `AGENTS.md` and `.github/instructions/` first — they take precedence.

## Course content & migrations

- Notes under `special/academia` are expected to be public by default. Use the `academic-notes` skill to validate structure and metadata.
- To propose moving content from `private/` to public, run the validator and attach its output to the migration request:

```sh
python .github/skills/academic-notes/validate_academic.py --content private/special/academia/<INSTITUTION>
```

- Use the `publish` workflow to mirror filtered content from `private/` to the public repository (this preserves history and applies filtering rules). Do not copy private files into the public tree manually.

## When to use `private/` vs public folders

- Keep content public unless it contains **PII**, confidential academic records, commercial/embargoed research, contracts, or other sensitive material.
- If in doubt, place content in `private/` and consult the repository owner. Follow the publish/migration checklist (PII/license/redaction/validation) before requesting a public migration.

---

## Developer tooling & testing conventions

- Use `pyproject.toml` as the authoritative Python dependency manifest. Keep runtime dependencies in `[project].dependencies` and developer tools in `[dependency-groups].dev` (PEP 722 style). Running `pnpm install` will trigger the `postinstall` hook that installs dev extras with `python -m pip install -e . --group dev`.
- Tests: Place tests under `tests/`, mirror the source layout when possible, and use `pytest` (`test_*.py` naming). Add tests for any script, tool or instruction change (especially changes that affect content generation or publishing). Use `pytest.mark.asyncio` for async tests.
- Hooks & automation: Register Husky hooks with `pnpm run prepare`. Pre-commit runs lint-staged which runs markdown and code formatters; pre-push runs the test suite to avoid broken pushes.
- Local validation: Before committing or opening a PR run `pnpm run format` and `pnpm run check` and `pnpm run test` locally.

---

## Other important files

- **`preamble.sty`** — LaTeX macros used by Extended MathJax in Obsidian.
- **`.git/`**, **`.github/`**, **`.obsidian/`**, **`.vscode/`** — configuration and workspace files (do not edit unless explicitly requested).
