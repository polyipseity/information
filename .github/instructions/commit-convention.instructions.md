---
name: Commit convention
description: Guidelines and automated checks for files and commits created by agents
applyTo: "**"
---

# Commit convention for agent-made commits

**Agent quickstart:** See `.github/instructions/agent-quickstart.instructions.md` for a short checklist of commands and workflow tips (present commit message to the user, run `pnpm run format`/`pnpm run check`, and prefer `pnpm install` + `pnpm run prepare` before making changes).

Whenever an automated agent or helper wishes to create a git commit on behalf of a user in this repository, the agent MUST follow this instruction **and ensure the commit message passes all commitlint rules enforced by the repository** (including line length, header/body/footer formatting, and any other linting requirements).

1. Use Conventional Commit style for the commit header (`type(scope): short description`). Choose an appropriate type (e.g., feat, fix, docs, chore) and a concise scope such as `notes` when editing note content. **All commit messages MUST comply with commitlint rules as enforced by the repository, including but not limited to:**
   - Commit header length and format
   - **Agents SHOULD wrap commit body lines at 72 characters or fewer (preferred for readability and buffer). Note: commitlint enforces a hard limit of 100 characters — ensure lines are ≤100 to pass.**
   - Proper use of footers and trailers

2. If the changes touch any of the `general/`, `special/`, or `self/` trees, the agent SHOULD suggest the following commit format to the user and prefer splitting documentation and content changes from functional changes. **Agents SHOULD aim to wrap commit body lines at 72 characters or fewer (preferred for readability and buffer); commitlint enforces a hard limit of 100 characters — ensure lines are ≤100 to pass.**
   - If a commit message fails commitlint due to line length, the agent MUST rewrap the body to ≤ 100 chars/line and retry until it passes, or report the error if it cannot be resolved.

   Header example:

   ```text
   feat(notes): improve 13 notes

   Trailers (machine-readable, single-line each):
   - Flashcards-delta: <signed-integer>
   - Flashcards-prev: <integer>
   - Flashcards-now: <integer>
   ```

   Flashcard progress commits (learn/review sessions)

   Agents may create commits that record flashcard learning or review
   sessions automatically without prompting for user confirmation using the
   `commit-staged-flashcard-progress` prompt. These commits MUST use
   Conventional Commit headers in one of these forms (wrap lines to 72
   characters or fewer):

   - Learn only: `chore(flashcards): learn N cards`
   - Review only: `chore(flashcards): review D/T
     cards (YYYY-MM-DD)`
   - Both learn and review: `chore(flashcards): learn N; review D/T cards
     (YYYY-MM-DD)`

   Required trailers (plain ASCII key/value, one per line, wrapped to 72
   characters or fewer):

   - `Flashcards-learned: <N>`
   - `Flashcards-review-target: <T>`
   - `Flashcards-review-done: <D>`
   - `Flashcards-review-date: <YYYY-MM-DD>`

   Optional trailers:

   - `Flashcards-review-remaining: <R>` (if provided)
   - `Flashcards-prev`, `Flashcards-now`, `Flashcards-delta` may be included
     when relevant to note updates.

   When `Review-done` must be computed from `Review-remaining` and
   `Review-target`, prefer running the terminal to compute and display the
   result for traceability. Agents must ensure progress commits pass
   commitlint; if commitlint rejects the message, rewrap/reformat and retry.

   The agent MUST prompt the user for the previous flashcard count and the new flashcard count (or otherwise confirm the values) before finalizing the commit. The agent computes `Flashcards-delta = Flashcards-now - Flashcards-prev` and inserts the three trailers exactly as single-line trailers at the end of the commit message.

3. Trailers must be plain ASCII key/value pairs, one per line. Place them before any repository footers if present. Note: this repository does not require a `Signed-off-by:` footer — any such footer is optional and stylistic.

   Example:

   Flashcards-delta: 41
   Flashcards-prev: 118117
   Flashcards-now: 118158

4. If no flashcard-related counts apply to the change, the agent should omit these trailers.

5. The agent MUST always show the proposed commit message to the user for confirmation before creating the commit. If the user requests changes to the message or the trailer values, the agent must accept and re-present the updated commit message for final confirmation. **The agent MUST check that the message is commitlint-compliant before presenting or using it.**

6. This instruction applies repository-wide; submodules with their own `.github/instructions/` may augment or override these rules for their subtree (innermost `AGENTS.md` wins).

**Pre-commit validation:** Before creating commits, agents MUST run repository formatting and validation steps using `pnpm` script wrappers when available (for example, `pnpm run format`, `pnpm run check`, and `pnpm run test`). The repository includes Husky hooks (`pre-commit`, `commit-msg`, `pre-push`) and `pre-push` runs `pnpm run test` to prevent pushing failing tests. Ensuring these steps locally reduces CI failures and blocked pushes.

## Commitlint compliance

All commit messages MUST pass commitlint checks. In particular:

- The commit header must follow Conventional Commit format and length rules.
- The commit body (if present) should be wrapped at **72 characters or fewer per line** (preferred for readability); commitlint enforces a hard limit of **100 characters** — ensure lines are ≤100 to pass.
- Trailers and footers must be formatted as plain ASCII key/value pairs, one per line.
- No lines may exceed the maximum allowed by commitlint.

If a commit message fails commitlint, the agent MUST rewrap or reformat the message and retry until it passes, or report the error if it cannot be resolved. **Agents must never allow a commit message with a body line exceeding 100 characters (commitlint will block the commit).**

---

Examples

Positive delta

feat(notes): improve 13 notes

Improve 13 note pages and related content.

Flashcards-delta: 41
Flashcards-prev: 118117
Flashcards-now: 118158

Optional footer (not required by this repository): Signed-off-by: Your Name <you@example.com>

Negative delta

feat(notes): improve 13 notes

Update note pages and remove obsolete flashcards.

Flashcards-delta: -3
Flashcards-prev: 118160
Flashcards-now: 118157

Optional footer (not required by this repository): Signed-off-by: Your Name <you@example.com>
