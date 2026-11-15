---
aliases:
  - ELEC 3120 Git
  - ELEC3120 Git
  - Git
  - HKUST ELEC 3120 Git
  - HKUST ELEC3120 Git
  - git
  - version control
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/Git
  - language/in/English
---

# Git

Git is a distributed version control system. Every copy of a project carries the whole history, so the recorded states can be compared, kept, shared and recovered without a server. GitHub holds one of those copies.

---

Flashcards for this section are as follows:

- what makes version control distributed? ::@:: Every copy of the project carries the whole history, so it works without a server; a remote host holds one copy among peers.
- what can be done with the states Git records? ::@:: They can be compared, kept, shared and recovered.

## project history

Git keeps a project in three places. The working tree holds the files being edited. The `.git` directory beside it holds the local history and branches, and needs no network. A remote host holds another copy of that history, for sharing.

---

Flashcards for this section are as follows:

- a Git project's three places: what does each one hold? ::@:: The working tree holds the edited files, `.git` holds the local history and branches, and a remote host holds a separate copy.
- which of the three places works without a network? ::@:: The local history in `.git`; the remote copy is the one that needs the network.

## branch

A branch is a movable name pointing at a commit. Two branches share the history below the commit where they diverge. A commit made on one advances that name alone, so one repository carries several lines of work at once.

---

Flashcards for this section are as follows:

- what is a branch? ::@:: A movable name that points at a commit.
- a commit is made on one of two branches sharing earlier history: what happens to the other name? ::@:: It stays where it was, because the new commit advances only the branch it was made on.

## staging area

The staging area holds the content selected for the next commit. Staging records the version of a file at that moment, so an edit made afterwards needs staging again. One file can carry a staged change beside an unstaged one.

---

Flashcards for this section are as follows:

- what does the staging area hold? ::@:: The content selected for the next commit, recorded at the version that was staged.
- a file is edited after it has been staged: what does the next commit take? ::@:: The staged version; the later edit has to be staged again.

## commit

A commit records the staged snapshot in local history and advances the current branch to it. Anything unstaged stays in the working tree.

---

Flashcards for this section are as follows:

- what does a commit record, and what does it advance? ::@:: The staged snapshot, and the current branch, which it moves to the new commit.
- what happens to the changes that were not staged? ::@:: They stay in the working tree, outside the commit.

## push

A push sends the committed history the remote lacks and updates the selected remote branch. Only commits travel, so work that is unstaged or uncommitted stays local. A push with nothing new to send leaves the remote branch unchanged.

---

Flashcards for this section are as follows:

- what does a push send? ::@:: The committed history the remote lacks, which updates the selected remote branch.
- do unstaged and uncommitted changes travel with a push? ::@:: No. Only commits travel, so they stay on the local machine.
