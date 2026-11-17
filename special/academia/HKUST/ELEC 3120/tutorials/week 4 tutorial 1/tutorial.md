---
aliases:
  - ELEC 3120 week 4 tutorial 1 tutorial
  - ELEC3120 week 4 tutorial 1 tutorial
  - HKUST ELEC 3120 week 4 tutorial 1 tutorial
  - HKUST ELEC3120 week 4 tutorial 1 tutorial
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/tutorials/week_4_tutorial_1/tutorial
  - language/in/English
---

# tutorial

- HKUST ELEC 3120 week 4 tutorial 1
- parent: [week 4 tutorial 1](index.md)

## git

Git keeps `reaction-game` in three places. The working tree holds the files being edited, `game.js` and `README.md`. The `.git` directory beside them holds the local history and the branches, so it works without a network. GitHub holds a separate copy that others reach.

---

Flashcards for this section are as follows:

- a Git project sits in three places: what does each hold? ::@:: The working tree holds the files being edited, the `.git` directory holds the local history and branches, and GitHub holds a separate copy.
- which of the working tree, the `.git` directory and GitHub works without a network connection? ::@:: Only the local history in `.git`.

### branch

A branch is a movable name pointing at a commit. In `reaction-game`, `main` and `restart` both point at C, sharing the commits A and B behind it. A commit D made on `restart` advances `restart` and leaves `main` at C.

---

Flashcards for this section are as follows:

- what is a branch? ::@:: A movable name that points at a commit.
- commits A, B and C are on `main` and a commit D is made on `restart`: where does each name point? ::@:: `restart` points at D, and `main` still points at C.

### staging area

The staging area holds the content chosen for the next commit. On `restart` the working tree carries three changes: `game.js` adds the R keyboard shortcut, `game.test.js` checks that the shortcut resets the game, and `README.md` gets an unrelated wording edit. Only the two game files are staged. A later edit to a staged file needs staging again.

---

Flashcards for this section are as follows:

- `game.js` and `game.test.js` are staged and the `README.md` edit is not: what does the staging area hold? ::@:: The versions of the two game files; the `README.md` edit stays unstaged in the working tree.
- a file is edited again after it was staged: what does the next commit take? ::@:: The version that was staged; the later edit has to be staged again.

### commit

A commit records the staged snapshot in local history and advances the current branch to it. Commit E carries the staged `game.js` and `game.test.js` under the message "Add R shortcut and test". The README edit stays in the working tree, uncommitted.

---

Flashcards for this section are as follows:

- what does a commit record, and what does it move? ::@:: The staged snapshot, and it advances the current branch to the new commit.
- after commit E is made, where does the unstaged README edit stand? ::@:: Still in the working tree, uncommitted.

### push

A push sends the committed history the remote lacks and updates the selected remote branch. Local history sits at E, so the GitHub copy moves from D to E.

---

Flashcards for this section are as follows:

- what does a push send, and what does it update? ::@:: The committed history the remote lacks, and it updates the selected remote branch.
- before and after the push to GitHub, what does the remote branch point at? ::@:: D before the push, E after.

## directing the agent

### project instructions

A project instruction file is a durable prompt given to the agent with every request. `AGENTS.md` serves Codex and other agents following the AGENTS convention, and `CLAUDE.md` serves Claude Code. It carries the project structure, the coding rules, the test commands and the safety constraints. `/init` writes a first version.

---

Flashcards for this section are as follows:

- `AGENTS.md` and `CLAUDE.md`: what is each, and who reads it? ::@:: A durable prompt sent with every new request, read by Codex and by Claude Code.
- what belongs in a project instruction file? ::@:: The project structure, the coding rules, the test commands, and the safety constraints.
- `/init`: what does it produce? ::@:: A first version of the project instruction file.

### plan mode

Plan mode settles the plan before any code changes. The agent asks questions that uncover missing requirements, reads the existing code and compares options, then presents the plan with its scope for review. A wrong assumption corrected there never reaches the generated code. Unclear or multi-file tasks need the plan; a simple edit can go straight to agent mode.

---

Flashcards for this section are as follows:

- plan mode: what does the agent produce before it edits code? ::@:: A plan covering missing requirements, the existing code and the options, with its scope open to review.
- which tasks need a plan, and which can skip it? ::@:: Unclear or multi-file tasks; a simple edit can go straight to agent mode.

## context window

The context window holds the information the model can use for its current response. It is one limited budget of tokens, and the capacity depends on the model. In `reaction-game` it holds the task of adding a leaderboard, the rule that the leaderboard stays offline, an excerpt of `game.js`, a sorting test that fails, and the room the answer needs. Files left on disk stay saved and take up nothing in the window.

---

Flashcards for this section are as follows:

- what fills a context window, and what stays out of it? ::@:: The task, the rules, the code excerpts and tool results read in, and the room for the answer; files left on disk stay outside.
- what is a token, and what sets the size of the budget? ::@:: A chunk of text; the model's own capacity sets the budget.

### context curation

The capacity stays the same, so a bigger window does not repair a crowded one. The agent selects and summarises instead, so old colour experiments, repeated debug logs and earlier discussion give way to the goal, the current code and the failing test. Agents may do this themselves; subagents are one means. The human checks that the goal, the constraints and the current state survived.

---

Flashcards for this section are as follows:

- the window fills up: what does the agent do, and what stays the same? ::@:: It selects and summarises what it keeps; the capacity stays the same.
- after the agent compresses the context, what does the human check? ::@:: That the goal, the constraints and the current state survived.

## subscription region

A model subscription follows the account's region, not the buyer's address. The app-store or web account has to sit in a region where payment works, and the subscription is charged to that region's gift card or to an overseas card.

---

Flashcards for this section are as follows:

- what decides where a model subscription is sold? ::@:: The account's region, not the buyer's address.
