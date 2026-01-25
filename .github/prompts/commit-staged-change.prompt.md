---
name: commit-staged-change
description: Produce a commit message for the currently staged changes and commit by default.
argument-hint: Optional extras (e.g., ticket=ABC-123). To skip committing, pass `commitNow=no`.
agent: agent
---

# Commit Staged Change

When run, perform the task using only two shell commands (each requires explicit user approval before execution):

1. Command 1 — gather everything needed to write the commit message.

    - Run exactly one compound command that prints the staged file list and the full staged patch. Example (single command):

      ```shell
      git diff --cached --name-status --no-color && git --no-pager diff --cached --staged --patch --no-color
      ```

    - Present the exact command you will run in your response; the IDE will request the user's approval when executing the command. Do not pause the chat waiting for manual approval. If the command is not executed (no output received), proceed to produce a best-effort commit message using available context and do not attempt further commands.

2. Compose the commit message.

    - Using the output from Command 1 and by inspecting repository files for documented conventions (CONTRIBUTING.md, `.github/`, `package.json` entries, `commitlint` configs, `.husky/`, `CHANGELOG.md`, etc.), detect the commit convention and produce a ready-to-use commit message:

      - 1-line subject (~50 chars)
      - optional body wrapped ~72 chars, with bullet points for key details
      - footer (BREAKING CHANGE / Refs / Ticket) and include `${input:extra}` if provided

    - If multiple conventions conflict, prefer the one enforced by tooling (commitlint, husky, CI). If unsure, ask one concise clarifying question and otherwise default to Conventional Commits.

3. Command 2 — create the commit and collect summary info.

    - If `${input:commitNow}` is `no`, skip Command 2 and only output the message.
    - Otherwise, present the exact Command 2 you will run; the IDE will request the user's approval when executing the command. Do not pause the chat waiting for manual approval. Command 2 must be a single compound command that:

      - creates the commit reading the message from stdin, and
      - prints the new commit SHA (or other data needed for a summary).

        Example (single command):

        ```shell
        git commit --no-verify --file - <<'MSG'
        <full commit message>
        MSG
        && git rev-parse HEAD
        ```

    - If Command 2 is executed, capture exit status and new HEAD SHA. The agent MUST construct Command 2 appropriate for the current shell (for example, use a PowerShell-friendly here-string when running in PowerShell, or a POSIX heredoc for bash). When presenting Command 2, show the exact command that will be executed for the current shell; the IDE will request approval and, if executed, will return the command output.

    - If the commit fails and the failure appears to be a shell syntax/heredoc/quoting issue (not a git error), the agent MAY attempt to fix the command syntax and retry up to 3 times. For each retry:

      - Present the revised command to run (the IDE will request execution). Do not run additional unrelated commands.
      - If the retry succeeds, capture exit status and new HEAD SHA and continue.
      - If the retry still fails with a syntax error, try another corrected form until attempts are exhausted.

    - If the commit ultimately fails for any other reason (git error, hooks, refs, permissions), report the error and do not attempt any staging changes.
    - If Command 2 is not executed, report that no commit was performed.

4. Output (must follow):

    - 1–2 line summary: staged files and detected convention
    - Commit message block labelled `Commit message` (header/body/footer)
    - If Command 2 ran: `Commit result` with exit status and new commit SHA
    - 1–3 line justification why this message fits the change

Rules:

- Do not run any other shell commands beyond the two approved commands.
- Do not run `git add` / `git reset` or otherwise change the index.
- If the user denies approval for Command 1, still propose a best-effort commit message using available non-executed context.

Inputs:

- `${input:extra}` — optional extra text to include in footer
- `${input:commitNow}` — `no` to skip committing; default is to commit

End of prompt.
