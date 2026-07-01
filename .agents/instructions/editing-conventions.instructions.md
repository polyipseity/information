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
    Do __not__ reflow, escape, or split any of these markers across lines; altering spacing or wrapping can break generation.

Agent quickstart pointer: See `.agents/instructions/agent-quickstart.instructions.md` for a concise agent checklist and quick repository gotchas (preserve pytextgen fences, don't reflow cloze markup, and prefer `bun run <script>` wrappers for reproducible runs).

- __pytextgen fences__: Do not modify `# pytextgen generate ...` comments, fence delimiters, or `return export_seq(...)` signatures. These are parsed by pytextgen; breaking them prevents regeneration.

- __Links__: Always relative with `%20` encoding (not `%3A` or other encodings). Use `archives/` for shared media.

- __Math__: Keep KaTeX `$...$` (inline) and `$$...$$` (block) intact; don't wrap or escape.

- __Formatting__: Respect `.markdownlint.json` settings (MD013/MD033/MD051 disabled). Avoid rewrapping existing lines; preserve layout. For emphasis in Markdown, prefer underscore: `_italic_` and `__bold__` (not `*`/`**`) so formatting is consistent and asterisks are reserved for lists and math.

## MD028 (consecutive blockquotes)

When two blockquote blocks (`> ...`) appear adjacent without intervening
non-blockquote content, markdownlint rule MD028 fires. To suppress it
legitimately (when the blockquotes are intentionally separate), always use
the exact pattern below. The `<!-- markdownlint MD028 -->` comment is
required **whenever two separate blockquote blocks** appear adjacent to
each other (separated only by blank lines). If the blockquotes represent
distinct content that should remain separate (e.g., questions and answers,
different speakers, or separate quotations), you must insert the separator
comment. If the blockquotes should be treated as a single continuous
blockquote (same speaker, same context), write them as one blockquote
without separation.

### Required pattern

```markdown
> (end of prior block)

<!-- markdownlint MD028 -->

> (start of next block)
```

### Rules (enforced by checks)

1. __Exactly one blank line__ before `<!-- markdownlint MD028 -->` — no more,
   no fewer. A blank line means an empty line (zero visible characters)
   between the last line of the prior blockquote and the comment.
2. __Exactly one blank line__ after `<!-- markdownlint MD028 -->` — no more,
   no fewer. An empty line between the comment and the first line of the
   next blockquote.
3. __Comment text is literal__ — use `<!-- markdownlint MD028 -->` exactly.
   Do __not__ use `<!-- markdownlint-disable-next-line MD028 -->`,
   `<!-- markdownlint-enable MD028 -->`, or any other markdownlint
   directive. This is a plain HTML comment whose content merely names the
   rule; it is not a tool command.
4. __No trailing whitespace__ on the comment line or the blank lines.
5. __Use only when separation is intentional__: Insert the comment only
   between blockquotes that are genuinely separate. If blockquotes form one
   continuous quote, merge them into a single blockquote instead.

### Example

```markdown
> First blockquote paragraph.
> More text in the first block.

<!-- markdownlint MD028 -->

> Second blockquote paragraph.
> More text in the second block.
```

### Rationale

The comment acts as a semantic separator (intentional break) that also
prevents markdownlint from flagging adjacent blockquotes as a single
merged block. Using a plain HTML comment instead of a suppression
directive keeps the intent explicit for both human readers and linters.

## Submodule editing policy

- __Default behavior__: Treat as read-only; ask user for permission if editing seems necessary
- __`private/**`__: Managed in separate upstream repository
- __`self/stash/`__: Part of the parent repo rather than a git submodule; still treat it as user-owned scratch space and avoid editing it unless requested.
- __When user approves edits__: Make changes here, test thoroughly, then contribute upstream
- __Priority__: Follow the submodule's own `AGENTS.md` first (submodule instructions take priority)

## Config folder policy

- __`.git/`, `.obsidian/`, `.vscode/`__: Do not edit unless explicitly requested; use UI tools to modify app settings

## Formatting & linting

- __markdownlint__: Configuration in `.markdownlint.json` (root, `scripts/`, `special/`, `archives/`) disables MD013 (line length), MD033 (HTML blocks), MD051 (link spacing)
- __running markdownlint-cli2__: when invoking the CLI with explicit file paths or filenames (for example `bun run check:md file1.md file2.md` or `bun run format:md file1.md`), __always__ include `--no-globs` and list the exact files you want to process. Without `--no-globs` markdownlint-cli2 will treat the arguments as a glob pattern, which may cause it to scan the entire repository instead of just the files you specified. This applies whether you call the command directly or via a bun script.
  - Respects and preserves existing formatting; avoid auto-reformatting unless requested
  - Useful for validating structure without breaking KaTeX or special layouts

- __YAML frontmatter__: `aliases`, `tags`, `language/in/English` are standard fields; preserve during edits

- __KaTeX math__: `$inline$` and `$$display$$` formats untouched; Extended MathJax in Obsidian uses `.obsidian/plugins/obsidian-latex/preamble.sty` for custom macros

## Developer tooling & testing conventions

- Dependency management: `pyproject.toml` is authoritative; add runtime deps to `[project].dependencies`, developer/test tools to `[dependency-groups].dev`, and the union of dependencies used in inline `# /// script` metadata to `[dependency-groups].scripts`. Inline script metadata should (1) begin with `#!/usr/bin/env python` shebang on line 1, (2) keep keys alphabetized, and (3) set `requires-python = ">=3.13.0"`. Run `bun install` (which triggers `prepare`, running `uv sync`) to register Husky hooks and install dev extras locally.
- Tests: Place tests in `tests/` and use `pytest` (`test_*.py` naming). Mirror source layout when helpful, and add unit and integration tests for any change to scripts or generators.
- Async tests: Prefer `@pytest.mark.anyio` with the AnyIO pytest plugin and import concurrency helpers from Asyncer (`create_task_group`, `soonify`, `asyncify`) instead of calling `anyio.create_task_group` directly. Avoid using event-loop runners inside tests. Prefer deterministic fixtures like `tmp_path: os.PathLike[str]` and `monkeypatch`. When typing tests, annotate `tmp_path` parameters as `PathLike[str]`; and when converting `PathLike` objects to strings __always__ use `os.fspath(path_like)` rather than `str(path_like)`.
- Local validation: Run `bun run format`, `bun run check`, and `bun run test` before pushing changes to avoid Husky hooks and CI failures. When only a subset of files are affected, supply explicit paths to these commands so they complete quickly instead of scanning the entire repo.
