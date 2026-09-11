---
name: Commit convention
description: Guidelines and automated checks for files and commits created by agents
applyTo: "**"
---

# Commit convention for agent-made commits

See `.agents/instructions/core-workflows.instructions.md` for a short checklist of commands and workflow tips (present commit message to the user, run `bun run format`/`bun run check`, and prefer `bun install` + `bun run prepare` before making changes).

When an automated agent creates a git commit on behalf of a user, the agent MUST follow this instruction and ensure the commit message passes all commitlint rules enforced by the repository (line length, header/body/footer formatting, and any other linting requirements).

## Line-length rule (single source of truth)

Agents SHOULD wrap commit body lines at 72 characters or fewer for readability. Commitlint enforces a hard limit of 100 characters — lines must be ≤100 to pass. If commitlint rejects a message due to line length, rewrap the body and retry until it passes.

## Conventional Commit header

Use Conventional Commit style: `type(scope): short description`. Choose an appropriate type (e.g., feat, fix, docs, chore) and a concise scope such as `notes` when editing note content.

## Flashcard trailers

Flashcard trailers (`Flashcards-delta`, `Flashcards-prev`, `Flashcards-now`) apply when ALL of the following conditions are met:

- (a) Changes touch `.md` files under `general/`, `special/`, or `self/`.
- (b) At least one modified `.md` file has flashcard-related tags in its YAML frontmatter (e.g. `flashcard/active`, `flashcard/archive`).
- (c) The change adds or removes flashcards — not a simple fix, metadata-only edit, or reformatting.

When any condition is false, omit the trailers. When all three are met:

- If the changes touch `.md` files under `general/`, `special/`, or `self/`, the agent SHOULD suggest the following commit format and prefer splitting documentation/content changes from functional changes.
- The agent MUST prompt the user for the previous and new flashcard counts (or otherwise confirm the values). Compute `Flashcards-delta = Flashcards-now - Flashcards-prev` and insert the three trailers as single-line values at the end of the commit message.

Trailers are plain ASCII key/value pairs, one per line, placed before any repository footers. This repository does not require a `Signed-off-by:` footer.

```text
feat(notes): improve 13 notes

Improve 13 note pages and related content.

Flashcards-delta: 41
Flashcards-prev: 118117
Flashcards-now: 118158
```

```text
feat(notes): improve 13 notes

Update note pages and remove obsolete flashcards.

Flashcards-delta: -3
Flashcards-prev: 118160
Flashcards-now: 118157
```

## Flashcard progress commits

Agents may create learn/review session commits automatically (via the `commit-staged-flashcard-progress` prompt) without prompting the user. Use these header forms (wrap to 72 chars):

- Learn only: `chore(flashcards): learn N cards`
- Review only: `chore(flashcards): review D/T cards (YYYY-MM-DD)`
- Both: `chore(flashcards): learn N; review D/T cards (YYYY-MM-DD)`

Required trailers:

- `Flashcards-learned: <N>`
- `Flashcards-review-target: <T>`
- `Flashcards-review-done: <D>`
- `Flashcards-review-date: <YYYY-MM-DD>`

Optional trailers: `Flashcards-review-remaining: <R>`, `Flashcards-prev`, `Flashcards-now`, `Flashcards-delta` (when relevant to note updates). When `Review-done` must be computed from remaining and target, prefer running the terminal to compute and display the result for traceability.

## Show before committing

The agent MUST always show the proposed commit message to the user for confirmation before creating the commit. If the user requests changes, re-present the updated message for final confirmation. The agent MUST verify commitlint compliance before presenting or using it.

This instruction applies repository-wide; submodules with their own `.agents/instructions/` may augment or override these rules for their subtree (innermost `AGENTS.md` wins).

## Pre-commit validation

Before creating commits, agents MUST run repository formatting and validation using `bun` script wrappers (e.g., `bun run format`, `bun run check`, `bun run test`). When operating on a subset of files, supply explicit paths (e.g. `bun run check:md --no-globs file.md`) so they complete quickly. The repository uses prek hooks (`pre-commit`, `commit-msg`, `pre-push`) and `pre-push` runs `bun run test` to prevent pushing failing tests.

__Hook failure recovery:__ When `git commit` fails, immediately read the hook output to identify which tool ran and which files it changed. If terminal output is too large, use `git diff --cached`. If a Markdown-specific tool (`markdownlint-cli2`) or Prettier touched non-`.md` files, restore the originals (`git checkout -- <file>`) — do not re-stage corrupted files. Never re-run `format:md` or `check:md` after a failed commit; doing so will corrupt non-markdown files.
