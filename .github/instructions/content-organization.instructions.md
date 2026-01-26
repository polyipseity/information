---
name: Content organization
description: High-level overview of repository structure and content organization principles
applyTo: "**"
---

# Content Organization & Repository Structure

This is a personal Markdown knowledge base with flashcards, tutorials, and archived online content. Content is organized by knowledge type and source:

## Directory structure

- **`general/`**: Encyclopedic knowledge from Wikipedia (broad, widely-applicable content)
  - Purpose: Encyclopedic knowledge, mostly verbatim from Wikipedia
  - Structure: Flat list of `.md` files, each a self-contained article
  - Metadata: YAML frontmatter with `aliases`, `tags` (flashcard activation, language)
  - Linking: Relative links with `%20` encoding; media in `archives/Wikimedia Commons/`
  - Updates: Primarily via `python -m "convert wiki"` workflow

- **`special/`**: Specialized knowledge (e.g., coursework, tutorials, business frameworks)
  - Purpose: Specialized knowledge (coursework, tutorials, frameworks, language texts)
  - Subdirectories:
    - **`academia/`**: Course notes organized by institution → semester/year → course code
      - Institutions: HKUST, Korea University, Pusan National University, USFQ, Yonsei University
      - Structure: Each institution has `reviews.md` and course directories (e.g., `COMP 2012/`)
      - Course metadata: Semester/year tags, credits, status (taken/not taken/transferred)
      - Index maintenance: Keep `index.md` updated with course listings via academic converters
    - Other subdirectories: Language texts, business frameworks, tutorial guides, etc.
  - Convention: Each directory recursively has `index.md` with listings and cross-references

- **`archives/`**: Archived online content (media, web pages, downloads)
  - Purpose: Permanent storage of online content (media, web pages, documents)
  - Subdirectories:
    - **`Wikimedia Commons/`**: Images, audio, video downloaded from Wikimedia Commons (descriptive filenames)
    - **`sparse/`**: Miscellaneous archived content with user-defined filenames (descriptive or arbitrary, not SHA-256 hashed)
    - Future folders: May expand with new archive categories (datasets, papers, books, code)
  - Index maintenance: Each folder has recursive `index.md` with source URL, timestamp, description; pyarchivist auto-updates

- **`tools/`**: Python scripts and utilities (wiki ingestion, LMS converters, packaging, publishing)
  - Core scripts: `init.py`, `convert wiki.py`, `pack.py`, `publish.py`
  - `tools/special/`: Academic converters (Canvas/HKUST Zinc LMS, course catalog fetchers)
  - `tools/templates/`: Note scaffolding templates
  - `tools/pytextgen/` (submodule): Programmatic content generation
  - `tools/pyarchivist/` (submodule): Online content archiving with metadata

## Git submodules

- **`self/`**: Personal metadata, ledger, and project-specific configurations (git submodules)
- **`private/`**: Private mirrored content (git submodule, separate private repository)
- **`tools/pytextgen/`**, **`tools/pyarchivist/`**: External tools (git submodules)

**Submodule hierarchy**: Many submodule folders (including `self/ledger`) have their own `AGENTS.md`, `.github/instructions/`, and `.github/skills/` files. When working in a submodule directory, those innermost agent files take priority. Always check for local `AGENTS.md` first.

## Other important files

- **`preamble.sty`**: LaTeX macro definitions for Extended MathJax in Obsidian (lightweight, backward-compatible)
- **`.git/`**: Git repository (do not edit)
- **`.github/`**: Agent instructions and skills
- **`.obsidian/`**: Obsidian app config, plugins, workspace (edit via Obsidian UI)
- **`.vscode/`**: VS Code workspace config (edit via VS Code settings)
