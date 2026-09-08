---
name: Editing conventions
description: General editing rules for Markdown notes, links, formatting, and submodules
applyTo: "**/*.md"
---

# Editing Conventions

## General editing rules

- __Frontmatter__: Keep YAML (`aliases`, `tags`, `language/in/English`) intact. Avoid adding unauthorized fields; add new fields only with user approval.

- __Cloze & flashcard markup__: Preserve the three patterns exactly and understand what they do:
    - `{@{ hidden text }@}` – cloze deletion; the inner text is hidden when the card is shown and must be recalled. (Most common.) __Closing delimiter:__ place `}@}` __before__ any trailing punctuation so punctuation sits outside the cloze (e.g. `{@{text}@}.` not `{@{text.}@}`).
    - `::@::` – two‑sided question/answer pair on a single Markdown line; creates two cards (left→right and right→left). Use `<br/>` for line breaks or `<p>` for paragraphs if needed, but keep the source line literal.
    - `:@:` – one‑sided question/answer pair on a single Markdown line; creates a single card where the right side is recalled from the left. Same line‑only rule applies.
    Do __not__ reflow, escape, or split any of these markers across lines; altering spacing or wrapping can break generation.  For guidance on _what_ to cloze and how to split sentences into fine-grained clozes, see the `flashcard-creation` skill (§ "Cloze creation methodology").

Agent quickstart pointer: See `.agents/instructions/core-workflows.instructions.md` for a concise agent checklist and quick repository gotchas (preserve pytextgen fences, don't reflow cloze markup, and prefer `bun run <script>` wrappers for reproducible runs).

- __pytextgen fences__: Do not modify `# pytextgen generate ...` comments, fence delimiters, or `return export_seq(...)` signatures. These are parsed by pytextgen; breaking them prevents regeneration. Preserve HTML comment variants (`<!--pytextgen generate section="..."-->` / `<!--/pytextgen-->`) exactly. Content between tags is auto-replaced on regeneration; do not run `uv run -m init generate`.

- __Links__: Always relative with `%20` encoding (not `%3A` or other encodings). Use `archives/` for shared media. Point media to `archives/Wikimedia Commons/` (preferred). Preserve existing link targets.

- __Math__: Keep KaTeX `$...$` (inline) and `$$...$$` (block) intact; don't wrap or escape.

- __Formatting__: Respect `.markdownlint.json` settings (MD013/MD033/MD051 disabled). Avoid rewrapping existing lines; preserve layout. For emphasis in Markdown, prefer underscore: `_italic_` and `__bold__` (not `*`/`**`) so formatting is consistent and asterisks are reserved for lists and math.

## MD028 (consecutive blockquotes)

When two separate blockquote blocks appear adjacent (separated only by blank lines), insert `<!-- markdownlint MD028 -->` between them — exactly one blank line before and after, literal comment text, no trailing whitespace. If the blockquotes are one continuous quote, merge them instead.

```markdown
> End of prior block.

<!-- markdownlint MD028 -->

> Start of next block.
```

## Submodule editing policy

- __Default behavior__: Treat as read-only; ask user for permission if editing seems necessary
- __`private/**`__: Managed in separate upstream repository
- __`self/stash/`__: Part of the parent repo rather than a git submodule; still treat it as user-owned scratch space and avoid editing it unless requested.
- __When user approves edits__: Make changes here, test thoroughly, then contribute upstream
- __Priority__: Follow the submodule's own `AGENTS.md` first (submodule instructions take priority)

## Config folder policy

- These folders and files contain auto-generated or sensitive configuration. Do not edit them unless explicitly requested by the user.
- `.git/`: Git repository internals — editing may corrupt the repository.
- `.markdownlint*` files: markdownlint configuration. Never add, remove, or modify rules in these files unless the user explicitly asks. This is a hard ban — markdownlint config is owned by the user.
- `.obsidian/`: Obsidian app settings, plugins, and workspace state — changes should be made in the Obsidian UI or after explicit user permission.
- `.vscode/`: VS Code workspace configuration — changes should be made in VS Code settings or after explicit user permission.
- If a task requires editing these folders, ask the user for explicit permission first.

## Formatting & linting

- __markdownlint__: Configuration in `.markdownlint.json` (root, `scripts/`, `special/`, `archives/`) disables MD013 (line length), MD033 (HTML blocks), MD051 (link spacing)
    - Per-directory configs (in `scripts/`, `special/`, `archives/`, and subdirectories) extend the root config via `"extends": "../.markdownlint.jsonc"`.
- __running markdownlint-cli2__: when invoking the CLI with explicit file paths or filenames (for example `bun run check:md file1.md file2.md` or `bun run format:md file1.md`), __always__ include `--no-globs` and list the exact files you want to process. Without `--no-globs` markdownlint-cli2 will treat the arguments as a glob pattern, which may cause it to scan the entire repository instead of just the files you specified. This applies whether you call the command directly or via a bun script.
    - Respects and preserves existing formatting; avoid auto-reformatting unless requested
    - Useful for validating structure without breaking KaTeX or special layouts

- __YAML frontmatter__: `aliases`, `tags`, `language/in/English` are standard fields; preserve during edits

- __KaTeX math__: `$inline$` and `$$display$$` formats untouched; Extended MathJax in Obsidian uses `.obsidian/plugins/obsidian-latex/preamble.sty` for custom macros

## Skill integrations

Use [wiki-ingestion](../skills/wiki-ingestion/SKILL.md) for Wikipedia imports, [pytextgen](../skills/pytextgen/SKILL.md) for flashcard regeneration, and [tools/SKILL.md](../skills/tools/SKILL.md) for note scaffolding.

## Developer tooling & testing conventions

Developer tooling and testing conventions are documented in [AGENTS.md](../AGENTS.md) (see the "Developer tooling & testing conventions" section).
