---
aliases:
  - ELEC 3120 agent execution loop
  - ELEC3120 agent execution loop
  - HKUST ELEC 3120 agent execution loop
  - HKUST ELEC3120 agent execution loop
  - LLM agent
  - agent
  - agent loop
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/agent_execution_loop
  - language/in/English
---

# agent execution loop

An LLM on its own is a text predictor: isolated, without memory, unable to act on the world. An agent is that model given hands, eyes and memory, and running its turns in a loop rather than answering once.

---

Flashcards for this section are as follows:

- what does an agent add to the bare model? ::@:: Hands to act through, eyes to read with, and memory to keep, plus a loop that runs its turns toward a goal instead of answering once
- what is a large language model on its own? ::@:: A text predictor. It is isolated and without memories, and it cannot act on the world

## the loop

Ask an agent to build a website and it enters a loop of three steps.

1. __Think__, working out what to do next.
2. __Act__, calling a tool to do it.
3. __Observe__, reading what came back.

Observe feeds what came back into the next turn of think, and that is what makes it a loop rather than a sequence. Each turn is a choice between calling a tool and answering, and the figure draws both routes. Your prompt enters the model, a tool call leaves it for tool call(s) and the tool result comes back, and an arrow labelled no tool calls bypasses the loop to reach a final answer. <p> ![agent execution loop: your prompt enters a box where the model evaluates; an arrow labelled tool calls leaves it for tool call(s), and an arrow labelled tool result returns; both sit inside a dashed agent loop, which an arrow labelled no tool calls bypasses to reach a final answer](attachments/agent_execution_loop.svg)

The figure names the parts rather than the steps. The box the model evaluates is think, tool call(s) is act, and the tool result arriving is what observe reads. The arrow out of the loop marks the end of it: the loop stops when the model asks for no tool calls, because a turn that calls no tool produces the final answer instead of another pass round.

---

Flashcards for this section are as follows:

- think, act and observe: which step calls a tool, and which reads what came back? ::@:: Act calls a tool, and observe reads what came back
- why is the sequence a loop rather than three steps in a row? ::@:: Because what observe reads becomes the input to the next turn of think, so each turn starts from the last one's result
- what tells the agent the loop is over? ::@:: A turn with no tool call, which produces the final answer instead of another pass round
- the agent execution loop figure: does it draw the three steps or the parts they run through? ::@:: The parts. The model evaluating is think, tool call(s) is act, and the tool result is what observe reads

## the core tool set

__Read__ ingests context: it scans an existing codebase, reads API documentation, and checks the current state of a file before modifying it.

__Write and edit__ change files. An agent either creates a new file or applies surgical edits to an existing one. Advanced agents use diff-matching to replace specific lines without rewriting the whole file.

__Bash__, to execute, is the most powerful of the three. It installs dependencies such as `npm install`, runs tests, and starts a server so the agent can verify its own work.

---

Flashcards for this section are as follows:

- read tool: what does it do? ::@:: Ingests context, by scanning the codebase, reading API documentation, and checking a file's state before modifying it
- write and edit tool: what separates an advanced agent's version from a basic one? ::@:: Diff-matching, so it replaces specific lines instead of rewriting the whole file
- bash tool: what is it used for? ::@:: Running terminal commands to install dependencies, run tests, and start a server so the agent can verify its own work
