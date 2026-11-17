---
aliases:
  - ELEC 3120 week 2 tutorial 1 tutorial
  - ELEC3120 week 2 tutorial 1 tutorial
  - HKUST ELEC 3120 week 2 tutorial 1 tutorial
  - HKUST ELEC3120 week 2 tutorial 1 tutorial
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/tutorials/week_2_tutorial_1/tutorial
  - language/in/English
---

# tutorial

- HKUST ELEC 3120 week 2 tutorial 1
- parent: [week 2 tutorial 1](index.md)

## model and agent

A large language model predicts text. It keeps nothing between requests and cannot reach anything outside the text it returns. An agent adds tools it can call, memory of what it has read, and a goal it works toward. The model still does the reasoning.

---

Flashcards for this section are as follows:

- a large language model on its own: what does it do, and what does it lack? ::@:: It predicts text, keeps no memory between requests, and cannot reach outside the text it returns.
- what turns a language model into an agent? ::@:: Tools it can call, memory of what it has read, and a goal it works toward.

## execution loop

An agent's turn has three steps. It thinks about what to do next. It acts by calling a tool and observes by reading what came back. That opens the next turn, and the loop ends when a turn calls no tool, because that turn is the answer. The figure in [agent execution loop](agent%20execution%20loop.md) draws the loop.

---

Flashcards for this section are as follows:

- an agent's turn: which three steps repeat, and what ends the loop? ::@:: Think, act and observe. A turn that calls no tool is the answer, so the loop ends.
- inside the loop, what does the observe step pass on, and where does it go? ::@:: The tool's result, which opens the next turn.

## tool set

A read tool scans the codebase, reads documentation, and checks a file before editing it. A write or edit tool changes files. A diff-matching edit tool replaces specific lines instead of rewriting the file. A bash tool runs commands: an agent installs a dependency, runs the tests, or starts a server to check its own work.

---

Flashcards for this section are as follows:

- a bash tool: what does it let an agent do that reading and editing cannot? ::@:: Run commands: install dependencies, run tests, or start a server to check its own work.
- diff matching in an edit tool: what does it allow? ::@:: Replacing specific lines, so one function changes without the file being rewritten.

## model access in Hong Kong

Five routes reach a model from Hong Kong: local models, Chinese models, third-party proxies to a model's application programming interface, a virtual private network into an overseas plan, and GitHub Copilot. None costs only money, and [language model access](language%20model%20access.md) compares them.

---

Flashcards for this section are as follows:

- local models and Chinese models as routes to a model: what does each cost? ::@:: Answer quality: the local models cost nothing extra, and the Chinese ones are cheap and stable but weaker than Claude and GPT.
- a virtual private network route into a model plan: what does it provide, and what does it cost? ::@:: Native Codex and Claude plans, at the price of an overseas credit card and a risk of a ban.
