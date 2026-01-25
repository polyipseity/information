# Commit convention for agent-made commits

Whenever an automated agent or helper wishes to create a git commit on behalf of a user in this repository, the agent MUST follow this instruction.

1. Use Conventional Commit style for the commit header (type(scope): short description). Choose an appropriate type (e.g., feat, fix, docs, chore) and a concise scope such as `notes` when editing note content.

2. If the changes touch any of the `general/`, `special/`, or `self/` trees, the agent SHOULD suggest the following commit format to the user and prefer splitting documentation and content changes from functional changes:

   Header example:

   feat(notes): improve 13 notes

   Trailers (machine-readable, single-line each):
   - Flashcards-delta: <signed-integer>
   - Flashcards-prev: <integer>
   - Flashcards-now: <integer>

   The agent MUST prompt the user for the previous flashcard count and the new flashcard count (or otherwise confirm the values) before finalizing the commit. The agent computes `Flashcards-delta = Flashcards-now - Flashcards-prev` and inserts the three trailers exactly as single-line trailers at the end of the commit message.

3. Trailers must be plain ASCII key/value pairs, one per line. Place them before any repository footers if present. Note: this repository does not require a `Signed-off-by:` footer — any such footer is optional and stylistic.

   Example:

   Flashcards-delta: 41
   Flashcards-prev: 118117
   Flashcards-now: 118158

4. If no flashcard-related counts apply to the change, the agent should omit these trailers.

5. The agent MUST always show the proposed commit message to the user for confirmation before creating the commit. If the user requests changes to the message or the trailer values, the agent must accept and re-present the updated commit message for final confirmation.

6. This instruction applies repository-wide; submodules with their own `.github/instructions/` may augment or override these rules for their subtree (innermost `AGENTS.md` wins).

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
