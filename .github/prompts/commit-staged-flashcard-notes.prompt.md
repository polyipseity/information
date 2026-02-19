---
name: commit-staged-flashcard-notes
description: Commit staged changes to notes/flashcards using the repository's flashcard commit convention.
argument-hint: Provide flashcard counts and details. To skip committing, pass `commitNow=no`.
agent: agent
---

# Commit Staged Flashcard Notes Change

**Never ask for confirmation or clarification. Always proceed automatically using best-effort defaults and available context.**

## Workflow

1. **Read staged changes**
   - Run a single compound command to print the staged file list and full staged patch:

     ```shell
     git diff --cached --name-status --no-color && git --no-pager diff --cached --staged --patch --no-color
     ```

   - Count notes added and edited using a platform-specific command:
     - **PowerShell (Windows):**

       ```powershell
       $staged = git diff --cached --name-status --no-color | Select-String -Pattern '^[AM]\s+"?(general|special|self)/.*\.md"?$'; $added = ($staged | Select-String -Pattern '^A').Count; $modified = ($staged | Select-String -Pattern '^M').Count; Write-Host "Added: $added, Modified: $modified"
       ```

     - **Bash/zsh (Linux/macOS):**

       ```bash
       staged=$(git diff --cached --name-status --no-color | grep -E '^[AM]\s+"?(general|special|self)/.*\.md"?$'); added=$(echo "$staged" | grep '^A' | wc -l); modified=$(echo "$staged" | grep '^M' | wc -l); echo "Added: $added, Modified: $modified"
       ```

   - Present the exact commands to be run. If not executed, produce a best-effort commit message from available context and stop.

2. **Gather flashcard data**
   - The user MUST provide at least **two** of the following inputs: `${input:Flashcards-prev}`,
     `${input:Flashcards-now}`, `${input:Flashcards-delta}`. Use the user-provided values as the
     primary source of truth.
   - If exactly two values are provided, compute the missing value using shell arithmetic in the
     detected shell (PowerShell on Windows, POSIX shells otherwise) and include all three trailers
     in the commit message. Example commands (replace placeholders with the provided integers):
     - POSIX (bash/zsh):
       - Provided `Flashcards-prev` and `Flashcards-now`:
         `Flashcards-delta=$((Flashcards_now - Flashcards_prev)); echo "Flashcards-delta:$Flashcards-delta"`
       - Provided `Flashcards-prev` and `Flashcards-delta`:
         `Flashcards-now=$((Flashcards_prev + Flashcards_delta)); echo "Flashcards-now:$Flashcards-now"`
       - Provided `Flashcards-now` and `Flashcards-delta`:
         `Flashcards-prev=$((Flashcards_now - Flashcards_delta)); echo "Flashcards-prev:$Flashcards-prev"`
     - PowerShell (Windows):
       - Provided `Flashcards-prev` and `Flashcards-now`:
         `$delta = [int]$Env:Flashcards_now - [int]$Env:Flashcards_prev; Write-Host "Flashcards-delta:$delta"`
       - Provided `Flashcards-prev` and `Flashcards-delta`:
         `$now = [int]$Env:Flashcards_prev + [int]$Env:Flashcards_delta; Write-Host "Flashcards-now:$now"`
       - Provided `Flashcards-now` and `Flashcards-delta`:
         `$prev = [int]$Env:Flashcards_now - [int]$Env:Flashcards_delta; Write-Host "Flashcards-prev:$prev"`
   - If fewer than two values are provided, prompt the user to supply the missing inputs and
     abort the automated commit operation until the missing values are provided. Do not attempt
     to compute missing values via repository scans or other fallbacks.
   - If the user does not provide the missing values when requested, omit the flashcard trailers
     from the commit message and include a short note in the commit body stating that user-
     provided flashcard counts were unavailable.
   - If computed or provided counts are inconsistent (for example, negative values), request
     clarification from the user and do not include flashcard trailers until the user provides
     consistent values.
   - If no flashcard-related counts apply, omit these trailers.

3. **Compose commit message**
   - The commit header MUST begin with `feat(notes):` and SHOULD include
     counts in a concise, natural format that shows only nonzero values.
     Use `add <N> note(s)` when the added count is nonzero and
     `edit <M> note(s)` when the edited count is nonzero. When both
     counts are present, separate them with a semicolon and a space
     in that order.
     Examples:
     - `feat(notes): add 3 note(s); edit 2 note(s)`
     - `feat(notes): add 3 note(s)`
     - `feat(notes): edit 2 note(s)`
     - `feat(notes): add 1 note(s); edit 2 note(s)`
   - If both counts are zero, omit counts from the header and use a
     short descriptive header (for example `feat(notes): tidy headings`).
   - The body should briefly describe the changes. **Each line in the commit header, body, and all flashcard trailers must be wrapped to 72 characters or fewer. This is strictly enforced by commitlint. If the commit is rejected due to line length or formatting, rewrap and retry until the commit passes.**
   - Add the three flashcard trailers as plain ASCII key/value pairs, one per line, before any optional footers. **Wrap each trailer line to 72 characters or fewer.**
   - Do not show the proposed commit message to the user for confirmation before creating the commit. Proceed automatically to creating the commit using best-effort defaults and available context.

4. **Create the commit**
    - If `${input:commitNow}` is `no`, skip this step and only present the message.
    - Otherwise, present the exact command to create the commit from stdin and print the new SHA. **Both operations must be run in the same shell command block to ensure correct context.** Use the correct heredoc/here-string syntax for the detected shell:
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

    - If the commit command fails due to quoting/heredoc syntax, retry up to 3 corrected forms. For other failures, report the error and do not modify the index.

5. **Output**
   - 1–2 line summary: staged files and detected convention
   - Commit message block labelled `Commit message` (header/body/footer)
   - If the commit command ran: `Commit result` with exit status and new commit SHA
   - 1–3 line justification why this message fits the change

## Rules

- Never ask for confirmation or clarification. Always proceed automatically using best-effort defaults and available context.
- Only run the approved shell commands (diff, count, commit as specified in the workflow). Do not run `git add`, `git reset`, or otherwise change the index.
- If the diff or count commands are denied, still propose a best-effort commit message using available context.

## Inputs

- `${input:Flashcards-prev}` — previous flashcard count (integer). Optional; **at least two** of the three
  flashcard inputs must be supplied.
- `${input:Flashcards-now}` — new flashcard count (integer). Optional; **at least two** of the three
  flashcard inputs must be supplied.
- `${input:Flashcards-delta}` — change in flashcard count (integer). Optional; **at least two** of the
  three flashcard inputs must be supplied.
- `${input:commitNow}` — `no` to skip committing; default is to commit
- `${input:extra}` — optional extra text for footer

End of prompt.
