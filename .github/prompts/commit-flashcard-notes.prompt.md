---
name: commit-flashcard-notes
description: Commit staged changes to notes/flashcards using the repository's flashcard commit convention.
argument-hint: Provide flashcard counts and details. To skip committing, pass `commitNow=no`.
agent: agent
---

# Commit Flashcard Notes Change

**Never ask for confirmation or clarification. Always proceed automatically using best-effort defaults and available context.**

## Workflow

1. **Read staged changes**
   - Run a single compound command to print the staged file list and full staged patch:

     ```shell
     git diff --cached --name-status --no-color && git --no-pager diff --cached --staged --patch --no-color
     ```

   - Present the exact command to be run. If not executed, produce a best-effort commit message from available context and stop.

2. **Gather flashcard data**
   - Use available context or best-effort defaults for:
     - Previous flashcard count (`Flashcards-prev`)
     - New flashcard count (`Flashcards-now`)
     - (Optional) Details about flashcard changes (added, removed, improved)
   - Compute `Flashcards-delta = Flashcards-now - Flashcards-prev` and include all three trailers in the commit message if provided.
   - If no flashcard-related counts apply, omit these trailers.

3. **Compose commit message**
   - Use Conventional Commit style for the commit header (e.g., `feat(notes): improve 13 notes`).
   - The header should summarize the number of notes added/edited (count from files added/edited in `general/`, `special/`, or `self/`).
   - The body should briefly describe the changes. **Each line in the commit header, body, and all flashcard trailers must be wrapped to 72 characters or fewer. This is strictly enforced by commitlint. If the commit is rejected due to line length or formatting, rewrap and retry until the commit passes.**
   - Add the three flashcard trailers as plain ASCII key/value pairs, one per line, before any optional footers. **Wrap each trailer line to 72 characters or fewer.**
   - Do not show the proposed commit message to the user for confirmation before creating the commit. Proceed automatically to creating the commit using best-effort defaults and available context.

4. **Create the commit**
    - If `${input:commitNow}` is `no`, skip this step and only present the message.
    - Otherwise, present the exact command to create the commit from stdin and print the new SHA. **Both commands must be run in the same shell command block to ensure correct context.** Use the correct heredoc/here-string syntax for the detected shell:
       - **PowerShell (Windows):**

         ```powershell
         (@"
         <full commit message>
         "@ | git commit --file=-) ; git rev-parse HEAD
         ```

         **Note on special characters and quoting:**
         Prefer PowerShell single-quoted here-strings (`@'... '@`) to avoid variable
         expansion and backtick escapes. If using double-quoted here-strings
         (`@"..."@`), escape backticks and `$` as needed or switch forms.

       - **Bash/zsh (Linux/macOS):**

         ```bash
         (git commit --file - <<'MSG'
         <full commit message>
         MSG
         ) && git rev-parse HEAD
         ```

         **Note on special characters and quoting:**
         Use a single-quoted heredoc (`<<'MSG'`) to prevent expansion so backticks
         and `$` are preserved. If the delimiter appears in the message, pick a
         different, unique delimiter to avoid syntax errors.

    - If Command 2 fails due to quoting/heredoc syntax, retry up to 3 corrected forms. For other failures, report the error and do not modify the index.

5. **Output**
   - 1–2 line summary: staged files and detected convention
   - Commit message block labelled `Commit message` (header/body/footer)
   - If Command 2 ran: `Commit result` with exit status and new commit SHA
   - 1–3 line justification why this message fits the change

## Rules

- Never ask for confirmation or clarification. Always proceed automatically using best-effort defaults and available context.
- Only run the two approved shell commands. Do not run `git add`, `git reset`, or otherwise change the index.
- If Command 1 is denied, still propose a best-effort commit message using available context.

## Inputs

- `${input:Flashcards-prev}` — previous flashcard count (integer)
- `${input:Flashcards-now}` — new flashcard count (integer)
- `${input:commitNow}` — `no` to skip committing; default is to commit
- `${input:extra}` — optional extra text for footer

End of prompt.
