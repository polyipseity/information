---
name: commit-staged-change
description: Produce a commit message for the currently staged changes and commit by default.
argument-hint: Optional extras (e.g., ticket=ABC-123). To skip committing, pass `commitNow=no`.
agent: agent
---

# Commit Staged Change

When run, perform the task using exactly two shell commands: one to read the staged patch and one to create the commit (unless `commitNow=no`).

1. **Command 1 — read the staged changes**
    - Run exactly one compound command that prints the staged file list and the full staged patch. Example:

        ```shell
        git diff --cached --name-status --no-color && git --no-pager diff --cached --staged --patch --no-color
        ```

    - Present the exact command you will run; the IDE will request approval and execute it. Do not pause the chat waiting for manual approval. The agent MUST NOT solicit approval from the user directly — the IDE handles approvals. If Command 1 is not executed (no output), produce a best-effort commit message from available context and stop. Do not ask the user for clarification or confirmation for any actions in this prompt. The agent must never ask the user if they are ready to commit or require confirmation at any step.

2. **Compose the commit message**
    - Inspect Command 1 output and repository conventions (CONTRIBUTING.md, `.github/`, `package.json`, `commitlint`, `.husky`, `CHANGELOG.md`, etc.) and produce a final commit message with:
        - a short subject (~50 chars),
        - optional body wrapped at ~72 chars with bullet points, and
        - footer (BREAKING CHANGE / Refs / Ticket) including `${input:extra}` if provided.
    - If conventions conflict, prefer tooling-enforced rules. If unsure, default to Conventional Commits. Do not ask the user for clarification or confirmation for any actions in this prompt. The agent must never ask the user if they are ready to commit or require confirmation at any step.

3. **Command 2 — create the commit**
    - If `${input:commitNow}` is `no`, do not run Command 2; only present the message.
    - Otherwise, present the exact Command 2 you will run; the IDE will request approval and execute it. The agent MUST NOT ask the user to grant approval itself. Command 2 must be a single compound command that creates the commit from stdin and prints the new SHA. The agent must never ask the user if they are ready to commit or require confirmation at any step.

    **IMPORTANT:**
    - Do NOT blindly use the Command 2 example as-is. You MUST adapt the commit command to the user's current shell (PowerShell, Bash, zsh, etc.).
    - Always detect the shell and use the correct heredoc or here-string syntax for that shell.
    - See below for examples for common shells:
        - **PowerShell (Windows):**

            ```powershell
            @"
            <full commit message>
            "@ | git commit --file=-
            git rev-parse HEAD
            ```

        - **Bash (Linux/macOS):**

            ```bash
            git commit --file - <<'MSG'
            <full commit message>
            MSG
            git rev-parse HEAD
            ```

        - **zsh (Linux/macOS):**

            ```zsh
            git commit --file - <<'MSG'
            <full commit message>
            MSG
            git rev-parse HEAD
            ```

        - If unsure, prefer the syntax for the detected shell. Do not use the PowerShell example on Bash or vice versa.
    - Construct Command 2 appropriate for the current shell (PowerShell here-strings vs POSIX heredoc). If Command 2 runs, capture exit status and new HEAD SHA.
    - If Command 2 fails due to shell quoting/heredoc syntax, the agent MAY retry up to 3 corrected forms (presenting each revised command for the IDE to run). For other failures (git hooks, refs, permissions), report the error and do not modify the index.
    - If Command 2 is not executed, report that no commit was performed.
    - Do not ask the user for clarification or confirmation for any actions in this prompt. Proceed automatically using best-effort defaults and available context. The agent must never ask the user if they are ready to commit or require confirmation at any step.

4. **Output (must follow):**
    - 1–2 line summary: staged files and detected convention
    - Commit message block labelled `Commit message` (header/body/footer)
    - If Command 2 ran: `Commit result` with exit status and new commit SHA
    - 1–3 line justification why this message fits the change

**Rules:**

- Do not run any other shell commands beyond the two approved commands.
- Do not run `git add` / `git reset` or otherwise change the index.
  - If the user denies approval for Command 1, still propose a best-effort commit message using available non-executed context. Do not ask the user for clarification or confirmation for any actions in this prompt. The agent must never ask the user if they are ready to commit or require confirmation at any step.

**Inputs:**

- `${input:extra}` — optional extra text to include in footer
- `${input:commitNow}` — `no` to skip committing; default is to commit

End of prompt.
