---
aliases:
  - ELEC 3120 context window
  - ELEC3120 context window
  - HKUST ELEC 3120 context window
  - HKUST ELEC3120 context window
  - context window
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/context_window
  - language/in/English
---

# context window

A context window is the information a large language model can use for its current response, counted in tokens. One budget of tokens covers the prompt, every file and tool result read in, and the room the answer needs. A file on disk stays outside the window until the agent reads it.

---

Flashcards for this section are as follows:

- what is a context window? ::@:: The information a large language model can use for its current response, held in one fixed budget of tokens.
- which parts of a request share the context window? ::@:: The prompt, the files and tool results read in, and the room the answer needs.
- a project file sitting on disk: is it in the context window? ::@:: No. It enters the window only when the agent reads it.

## capacity

A token is a chunk of text, and the model's capacity sets how many fit at once. That budget is shared, so a longer transcript leaves less room for the answer.

---

Flashcards for this section are as follows:

- what is a token, and what decides how many fit? ::@:: A chunk of text; the model's capacity decides how many fit in its window.
- a longer transcript: what does it cost the answer? ::@:: Room. The transcript, the file excerpts and the tool output share one budget.

## context curation

The capacity stays the same when the window fills, so the agent selects and summarises. Earlier discussion, repeated debug logs and abandoned experiments give way to the goal, the constraints, the current code and the failing test. Agents do this themselves, subagents included. A human then checks that the goal, the constraints and the current state survived.

---

Flashcards for this section are as follows:

- a context window fills up: what does the agent do, and what stays the same? ::@:: It selects and summarises the earlier material; the capacity stays the same.
- after an agent selects and summarises its context, what does the human check? ::@:: That the goal, the constraints and the current state survived.
