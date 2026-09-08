---
name: Markdown notes
description: Conventions for Markdown knowledgebase notes and flashcards
applyTo: "general/**/*.md"
---

# Markdown Notes Guidelines

## Frontmatter

Keep YAML (`aliases`, `tags`, `language/in/English`) intact during edits. Do not strip fields or reorder without user approval.

## pytextgen blocks

Preserve `# pytextgen generate ...` comments, fence delimiters, and `return export_seq(...)` signatures exactly. Preserve HTML comment variants (`<!--pytextgen generate section="..."-->` / `<!--/pytextgen-->`) exactly. Content between tags is auto-replaced on regeneration; do not run `uv run -m init generate`.

## Links & media

Use relative paths with `%20` encoding. Point media to `archives/` (preferred: `archives/Wikimedia Commons/`). Preserve existing link targets.

## Formatting

Preserve KaTeX `$inline$` and `$$display$$` math. Respect `.markdownlint.json` (MD013/MD033/MD051 disabled). Avoid hard-wrapping existing lines.

## Submodules

Treat `private/**` as read-only unless user approves. `self/stash/` is not a submodule; treat as user-owned scratch space.

## Integration

Use [wiki-ingestion](../skills/wiki-ingestion/SKILL.md) for Wikipedia imports, [pytextgen](../skills/pytextgen/SKILL.md) for flashcard regeneration, and [tools/SKILL.md](../skills/tools/SKILL.md) for note scaffolding.
