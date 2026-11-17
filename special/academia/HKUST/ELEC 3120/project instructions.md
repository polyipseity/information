---
aliases:
  - AGENTS.md
  - CLAUDE.md
  - ELEC 3120 project instructions
  - ELEC3120 project instructions
  - HKUST ELEC 3120 project instructions
  - HKUST ELEC3120 project instructions
  - agent instructions
  - project instructions
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/project_instructions
  - language/in/English
---

# project instructions

A project instruction file is a durable prompt an agent reads with every new request. It sits in the repository beside the code and records what a glance does not show: the conventions, the commands that check a change, and the limits the agent must not cross.

---

Flashcards for this section are as follows:

- what is a project instruction file? ::@:: A durable prompt an agent reads with every new request, kept in the repository beside the codebase.
- what does a project instruction file state that the codebase does not? ::@:: The conventions the project follows, the commands that check a change, and the limits the agent must not cross.

## instruction file

Codex reads `AGENTS.md`, as do other agents following the AGENTS convention. Claude Code reads `CLAUDE.md`. `/init` writes a first version from the codebase.

---

Flashcards for this section are as follows:

- which file carries project instructions for Codex, and which for Claude Code? ::@:: `AGENTS.md` for Codex and other agents following the AGENTS convention; `CLAUDE.md` for Claude Code.
- what does `/init` produce in an agent that supports it? ::@:: A first version of the project instruction file, written from the codebase.

## useful content

Four things belong in a project instruction file. Project structure says where the parts live. Coding rules say how code is written here. Test commands say what proves a change works. Safety constraints say what the agent must not touch, delete, or publish.

---

Flashcards for this section are as follows:

- which four things make a project instruction file useful? ::@:: The project structure, the coding rules, the test commands, and the safety constraints.
