---
aliases:
  - ELEC 3120 prompt engineering
  - ELEC3120 prompt engineering
  - HKUST ELEC 3120 prompt engineering
  - HKUST ELEC3120 prompt engineering
  - prompt design
  - prompt engineering
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/prompt_engineering
  - language/in/English
---

# prompt engineering

Prompt engineering structures the instruction given to a generative model so that the response is the one wanted.

A prompt is the instruction, question, or discussion topic typed into a generative AI tool.

---

Flashcards for this section are as follows:

- what is prompt engineering? ::@:: Structuring the instruction given to a generative model so that its response is the one wanted.
- what is a prompt? ::@:: The instruction, question, or discussion topic typed into a generative AI tool.

## specificity

Clear, specific wording ties the response to the task. A prompt naming only its subject leaves the model to choose the work.

---

Flashcards for this section are as follows:

- what makes a prompt return a relevant response? ::@:: Clear, specific wording that names the task.

## layered task prompt

A task too big for one sentence is layered, one job per line, with the evidence that shows each job is done:

1. Read the requirements of the checkpoint.
2. Pull the code into the working directory.
3. Build and test it inside the vagrant virtual machine, and fix what fails.
4. Review the final diff, and summarise what changed and what was tested.
5. Run `submit.py` at the project root, which generates `submit.zip`.

The requirements line comes first because it settles what counts as done. Evidence decides the rest, so the model never judges completion.

---

Flashcards for this section are as follows:

- how is a task too big for one sentence written as a prompt? ::@:: One job per line, each with the evidence that shows the job is done.
- in the layered checkpoint prompt, which two lines put the code where the work happens? ::@:: The line that pulls the code into the working directory, and the line that builds and tests it inside the vagrant virtual machine.
- which line of the layered checkpoint prompt asks for evidence that the change works? ::@:: The line that reviews the final diff and summarises what changed and what was tested.
