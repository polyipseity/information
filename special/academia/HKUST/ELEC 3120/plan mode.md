---
aliases:
  - ELEC 3120 plan mode
  - ELEC3120 plan mode
  - HKUST ELEC 3120 plan mode
  - HKUST ELEC3120 plan mode
  - plan mode
  - planning mode
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/plan_mode
  - language/in/English
---

# plan mode

Plan mode makes an agent agree a plan before it changes any code. A plan can be read and corrected, so a wrong assumption costs a sentence before it reaches the code.

---

Flashcards for this section are as follows:

- what does plan mode make an agent do before it edits code? ::@:: Agree a plan before editing any code.

## scope review

Before writing the plan, the agent asks questions to uncover missing requirements, reads the existing code, and compares the options it could take. The plan states the scope of the change, so it can be reviewed and redirected before anything is built.

---

Flashcards for this section are as follows:

- plan mode: what does the agent do before it writes the plan? ::@:: It asks questions to find missing requirements, reads the existing code, and compares the options it could take.
- what does reviewing the plan prevent? ::@:: A wrong assumption spreading through generated code.

## planning threshold

An unclear task, or one spanning several files, needs a plan because its requirements are not settled yet. A simple edit has nothing to settle, so it needs none.

---

Flashcards for this section are as follows:

- which tasks need a plan, and which do not? ::@:: An unclear task or one spanning several files; a simple edit needs none.
