---
name: resolve-merge-conflicts-flashcard-states
description: Resolve markdown merge conflicts by keeping incoming content, transferring matching SR flashcard states, and verifying non-state parity with incoming branch.
argument-hint: Optional: incomingBranch=origin/main threshold=0.50 paths="file1.md,file2.md" stage=yes
---

# Resolve Merge Conflicts (Incoming-First + SR State Transfer)

Use this prompt when resolving merge conflicts in markdown notes where spaced-repetition state comments (`<!--SR:...-->`) must be preserved when possible.

## Objective

For each conflicted markdown file:

1. Keep **incoming branch content** as the base resolution.
2. Transfer compatible SR state comments from the current side onto matching incoming lines.
3. Use similarity matching (default threshold: `0.50`) to find corresponding flashcards.
4. Discard unmatched SR states.
5. Prove non-state content was not changed relative to incoming.

## Inputs

- `${input:incomingBranch}` (optional, default: `origin/main`)
- `${input:threshold}` (optional, default: `0.50`; minimum allowed: `0.50`)
- `${input:paths}` (optional CSV of markdown paths; if omitted, use currently conflicted markdown files)
- `${input:stage}` (optional: `yes`/`no`, default: `yes`)

## Hard Rules

- Accept incoming content and discard conflicting current content, **except** transferable SR states.
- A flashcard is considered corresponding if normalized similarity is **>= threshold**.
- Never modify non-SR text unless required to remove conflict markers.
- **Do not commit.**
- You may stage resolved files with `git add` when `${input:stage}` is `yes`.

## Matching Rules (Best Practice)

When matching flashcards between current and incoming versions:

1. Normalize both lines before similarity comparison:
   - Remove SR comments (`<!--SR:...-->`).
   - Trim and collapse whitespace.
   - Compare in lowercase.
2. Prefer one-to-one matching to avoid reusing the same incoming target repeatedly.
3. If multiple candidates pass threshold, choose highest similarity.
4. If no candidate reaches threshold, drop that SR state.

## Execution Workflow

1. Identify target files.
   - If `${input:paths}` is provided, use those files.
   - Otherwise, detect unmerged markdown files from Git index.

2. Resolve conflicts in each target file.
   - For each conflict hunk:
     - Keep incoming side text.
     - Extract SR states from current side lines.
     - Map states to incoming lines using threshold matching.
     - Append mapped SR comments to matched incoming lines.
   - Remove all conflict markers.

3. Validate content integrity.
   - For each resolved file:
     - Strip SR comments from working tree version.
     - Compare exact stripped text with `${input:incomingBranch}:<path>`.
   - Any mismatch is a blocker and must be fixed.

4. Validate conflict completeness.
   - Confirm no `<<<<<<<`, `=======`, `>>>>>>>` markers remain.
   - Confirm no unmerged entries remain in `git status --porcelain`.

5. Stage results (optional).
   - If `${input:stage}` is `yes`, run `git add` on resolved files.

6. Report results.

## Required Output Format

Provide a concise report with:

- `Files processed`
- `Conflict hunks resolved`
- `SR states found`
- `SR states mapped`
- `SR states dropped`
- `Conflict markers remaining` (must be `0`)
- `Non-state parity mismatches` (must be `0`)
- `Unmerged index entries` (must be `0`)
- `Staged` (`yes`/`no`)

Also include a short per-file summary for mapped/dropped SR counts.

## Failure Handling

If validation fails:

- Stop and show exact files that failed.
- Explain whether failure is due to non-state mismatch, unresolved markers, or unmerged index entries.
- Do not proceed to commit.

End of prompt.
