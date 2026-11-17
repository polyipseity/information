---
aliases:
  - COMP 3511 AGENTS
  - HKUST COMP 3511 AGENTS
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/AGENTS
  - language/in/English
---

# COMP 3511 agent instructions

__Course convention: every C API call the notes show is carded with an example that carries values.__ The signature alone does not say how a call is used, and an example full of parameter names (`execvp(command, args)`) says as little as the signature.

- `.pi/ingest/COMP 3511` is input only: handouts never enter the repository, and the extracted tree keeps its wording even where a note fixes it.
- Group notes and sections by concept, never by the deck or chapter that delivered them. No chapter number, slide number, or "the lecture" appears in prose, titles, cards, or index entries.
- One card per function, never a bundled card for several calls. `labs/lab 6/lab.md` and `pthreads.md` show the pattern.
- Every argument of a carded call gets its meaning and its value set, so the card answers how to call it without the note: `O_RDONLY`/`O_WRONLY`/`O_RDWR` for the `open()` flags, `"r"`/`"w"` for the `popen()` type, `F_OK`/`R_OK`/`W_OK`/`X_OK` for `access()`. A flag a code example sets is read somewhere in the same example; a written-only variable is a bug in the example. A constant the note uses carries its meaning where it is first used, so `SIGUSR1` and `SIGUSR2` say what a program can do with a signal that has no built-in meaning.
- Each API card carries three parts on one line: the prototype with types, one line of the note's own call with concrete values, and a sentence saying what the call does and what it returns. Two code spans and a sentence fit without HTML separators; `<p>` and `<br/>` are not available inside a card.
- The example is a line of the note's code. When the note lacks the call, add the call or drop the card, and prefer rewriting the note's code over inventing an example in the card.
- Every call a note demonstrates gets a card in that note, including the ones a lab program uses but never explains (`pipe`, `fork`, `wait`, `popen`, `pthread_create`, `pthread_join`).
- A card that only restates what an example passes carries no knowledge. Fold its fact into the prototype card that owns the call and delete it.
- When two notes cover the same call, the note that owns the concept keeps the cards and the other keeps prose with a term link. A lab links into the topic note with `../../` in front of the path.
- Scheduling figures come from a simulator, not from arithmetic done by eye. Response time runs from arrival to the end of a first run, and every average shows its working in the same sentence.
- Durable homes for processes and threads: `process (computing).md` for fork, exec, exit, wait and process state; `thread (computing).md` for thread models, signals, cancellation and `pthread_atfork`; `pthreads.md` for the thread, mutex and condition-variable API.
- Durable homes for synchronization and scheduling: `synchronization (computer science).md` for the critical-section problem and its hardware support; `semaphore (programming).md` for semaphore operations and implementations; `producer–consumer problem.md` and `readers–writers problem.md` for the classical problems.
- Durable homes for the rest: `scheduling (computing).md` and `multilevel feedback queue.md` for scheduling; `deadlock (computer science).md` for deadlock; `named pipe.md`, `inter-process communication.md`, and `system call.md` for the pipe and file-call detail.
- Before calling a note finished: folder-scope `academic-lint`, markdownlint on the changed files, `gcc -fsyntax-only` on every C block, a duplicate-prompt scan, and a check that each card's call appears in its note's code.
