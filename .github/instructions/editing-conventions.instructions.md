---
name: Editing conventions
description: General editing rules for Markdown notes, links, formatting, and submodules
applyTo: "**/*.md"
---

## General editing rules

- **Frontmatter**: Keep YAML (`aliases`, `tags`, `language/in/English`) intact. Avoid adding unauthorized fields; add new fields only with user approval.

- **Cloze markup**: Preserve `{@{ ... }@}`, `::@::`, and `:@:` unchanged; do not reflow or escape. These are used for flashcard generation.

- **pytextgen fences**: Do not modify `# pytextgen generate ...` comments, fence delimiters, or `return export_seq(...)` signatures. These are parsed by pytextgen; breaking them prevents regeneration.

- **Links**: Always relative with `%20` encoding (not `%3A` or other encodings). Use `archives/` for shared media.

- **Math**: Keep KaTeX `$...$` (inline) and `$$...$$` (block) intact; don't wrap or escape.

- **Formatting**: Respect `.markdownlint.json` settings (MD013/MD033/MD051 disabled). Avoid rewrapping existing lines; preserve layout.

## Submodule editing policy

- **Default behavior**: Treat as read-only; ask user for permission if editing seems necessary
- **`self/**`**, **`private/**`**: Managed in separate upstream repositories
- **`tools/pytextgen/`**, **`tools/pyarchivist/`**: External dependencies
- **When user approves edits**: Make changes here, test thoroughly, then contribute upstream
- **Priority**: Follow the submodule's own `AGENTS.md` first (submodule instructions take priority)

## Config folder policy

- **`.git/`, `.obsidian/`, `.vscode/`**: Do not edit unless explicitly requested; use UI tools to modify app settings

## Formatting & linting

- **markdownlint**: Configuration in `.markdownlint.json` (root, `tools/`, `special/`, `archives/`) disables MD013 (line length), MD033 (HTML blocks), MD051 (link spacing)
  - Respects and preserves existing formatting; avoid auto-reformatting unless requested
  - Useful for validating structure without breaking KaTeX or special layouts

- **YAML frontmatter**: `aliases`, `tags`, `language/in/English` are standard fields; preserve during edits

- **KaTeX math**: `$inline$` and `$$display$$` formats untouched; Extended MathJax in Obsidian uses `preamble.sty` for custom macros
