---
name: commit-staged-flashcard-progress
description: Commit staged changes that record a flashcard learning or review session.
argument-hint: Provide learning and/or review counts. To skip committing, pass `commitNow=no`.
agent: agent
---

# Commit Staged Flashcard Progress

**Never ask for confirmation or clarification. Always proceed automatically using
best-effort defaults and available context.**

This prompt is intended for commits that record a user's flashcard activity: a
learning session ("Learn N cards") and/or a review session ("Review D of T
cards for YYYY-MM-DD"). It follows Conventional Commits and includes
machine-readable trailers for the learning/review counts.

## Inputs

- `${input:Learn}` — number of cards learned in this session (integer).
- `${input:Review-target}` — number of cards scheduled to review today (integer).
- `${input:Review-done}` — number of cards actually reviewed (integer).
- `${input:Review-remaining}` — alternative to `Review-done`: number of cards
  remaining to review today (integer). If provided with `Review-target`, the
  agent should compute `Review-done = Review-target - Review-remaining` using
  the terminal (preferred) or arithmetic as a fallback.
- `${input:Review-date}` — optional date to tag the review (YYYY-MM-DD). If not
  provided, default to the current date in ISO format.
- `${input:commitNow}` — `no` to skip creating the commit; default is to commit.
- `${input:extra}` — optional extra text for footer.

Note: If terminal-based calculations succeed they override these inputs; if
they fail or are unavailable, fall back to the provided input values.

## Workflow

1. Read staged changes
   - Run the single compound command to print the staged file list and the
     full staged patch (same as other commit prompts):

     ```powershell
     git diff --cached --name-status --no-color && git --no-pager diff --cached --staged --patch --no-color
     ```

   - Present the exact command to be run. If Command 1 is denied, continue and
     produce a best-effort commit message using available context.

2. Gather session data
   - Use the provided inputs. If `Review-done` is not provided but
     `Review-target` and `Review-remaining` are, prefer computing
     `Review-done = Review-target - Review-remaining` using a read-only
     terminal command for traceability. Examples:

     - POSIX (bash/zsh):
       - `echo $(( {Review-target} - {Review-remaining} ))`
       - or: `expr {Review-target} - {Review-remaining}`

     - PowerShell (Windows):
       - `$done = {Review-target} - {Review-remaining}; Write-Output $done`

     Replace `{Review-target}` and `{Review-remaining}` with the integer
     input values or run the commands using the numeric inputs. If the
     terminal cannot be run or the commands fail, compute arithmetically as a
     fallback and note the fallback in the commit body. When a terminal
     command was run, include its numeric output or an explicit note in the
     commit body for traceability.

   - If neither review nor learn inputs are provided, assume zero and still
     compose a commit summarizing the staged changes (but omit numeric trailers
     that don't apply).

3. Compose commit message
   - Use Conventional Commit style for the commit header.
   - Use these header formats (choose the one that matches the session):
     - Learn only: `chore(flashcards): learn N card(s)`
     - Review only: `chore(flashcards): review D/T card(s) (YYYY-MM-DD)`
     - Both learn and review: `chore(flashcards): learn N; review D/T card(s) (YYYY-MM-DD)`

   - The commit body should briefly describe the session and any relevant
     context (e.g., sources, study constraints). Keep lines wrapped to 72
     characters or fewer.

   - Required trailers (one per line, ASCII, wrapped to 72 chars):
     - If Learn provided: `Flashcards-learned: <N>`
     - If Review provided: `Flashcards-review-target: <T>`
     - If Review provided: `Flashcards-review-done: <D>`
     - If Review-date provided or used: `Flashcards-review-date: <YYYY-MM-DD>`

   - Optional trailers:
     - `Flashcards-review-remaining: <R>` (if provided and helpful)
     - `Flashcards-prev/Flashcards-now/Flashcards-delta` may be included if
       there is relevant change in the note data (only include when
       applicable).

   - Examples (each line must be <= 72 chars):

     Header: chore(flashcards): learn 2648 cards

     Header: chore(flashcards): review 5677/14390 cards (2026-01-04)

     Header: chore(flashcards): learn 42; review 12/40 cards (2026-01-04)

     Trailers:
     Flashcards-learned: 2648
     Flashcards-review-target: 14390
     Flashcards-review-done: 5677
     Flashcards-review-date: 2026-01-04

4. Create the commit
   - If `${input:commitNow}` is `no`, skip creating the commit and only
     present the message.

   - Otherwise, create the commit. Use the exact commands below depending on
     the detected shell. Always include both commands in the same shell block
     so the second command prints the new SHA.

     PowerShell (Windows):

     ```powershell
     (@"
     <full commit message>
     "@ | git commit --file=-) ; git rev-parse HEAD
     ```

     Notes on quoting: Prefer single-quoted here-strings (`@'... '@`) to avoid
     variable expansion. If using double-quoted here-strings, escape `$` and
     backticks as needed.

     Bash/zsh (Linux/macOS):

     ```bash
     (git commit --file - <<'MSG'
     <full commit message>
     MSG
     ) && git rev-parse HEAD
     ```

   - If the commit command fails due to quoting/heredoc syntax, retry up to
     three corrected forms. For other failures, report the error and do not
     change the index.

5. Output
   - 1–2 line summary: staged files and detected convention
   - `Commit message` block showing header, body, and trailers
   - If commit ran: `Commit result` with exit status and new commit SHA
   - 1–3 line justification why this message fits the change

## Rules

- Never ask for confirmation or clarification. Proceed automatically using
  best-effort defaults and available context.
- Use the precise header formats above. Keep all lines wrapped to 72 chars or
  fewer (commitlint will reject otherwise — retry with corrected wrapping).
- You may run additional read-only shell/terminal commands (for example, the
  arithmetic commands shown above) to compute session numbers. Do not run
  commands that modify the index or repository state (no `git add` or `git
  reset`). Continue to use the two approved commands for reading the staged
  diff and committing.
- When both learning and review happen, include both in the header and
  include both relevant trailers.
- When computing `Review-done` from `Review-remaining`, prefer running the
  terminal to compute and display the result for traceability.

End of prompt.
