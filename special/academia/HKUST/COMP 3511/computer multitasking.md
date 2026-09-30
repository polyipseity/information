---
aliases:
  - COMP 3511 computer multitasking
  - computer multitasking
  - multiprogramming
  - multitasking
  - time sharing
  - time-sharing
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/computer_multitasking
  - language/in/English
---

# computer multitasking

All modern operating systems share two characteristics: __multiprogramming__, a batch system needed for efficiency, and __time sharing__, or multitasking, its logical extension for interactive use. Both exist because a machine running one program at a time cannot keep its processor and its devices busy.

---

Flashcards for this section are as follows:

- two characteristics of modern operating systems ::@:: Multiprogramming, a batch system needed for efficiency, and time sharing (multitasking), which provides interactive computing.

## multiprogramming

Early systems loaded one program into memory at a time, but a single program cannot keep the CPU or the I/O devices busy, and devices grew faster, so all modern systems are multiprogrammed. Multiprogramming organizes jobs so that the CPU always has one to execute. On mainframes, jobs are submitted remotely and queued, then selected and loaded into memory by __job scheduling__.

---

Flashcards for this section are as follows:

- multiprogramming ::@:: Multiprogramming organizes jobs so the CPU always has one to execute, since one program cannot keep the CPU and the I/O devices busy; all modern computer systems are multiprogrammed.
- job scheduling ::@:: On mainframe computers jobs are submitted remotely and queued, and job scheduling selects jobs and loads them into memory.

## time sharing

__Time sharing__ is the logical extension of multiprogramming in which the CPU switches "frequently" between jobs so that users can interact with each while it runs, which is interactive computing; the response time should stay under a certain threshold. A program in execution is a __process__. When several processes are ready to run at once, __CPU scheduling__ decides the order. When processes do not fit in memory, __swapping__ moves them in and out during execution, and __virtual memory__ runs processes that are not completely in memory. Both need operating-system support.

---

Flashcards for this section are as follows:

- time sharing ::@:: The logical extension of multiprogramming: the CPU switches frequently between jobs so users can interact with each while it runs, giving interactive computing with a response time under a certain threshold.
- process and CPU scheduling ::@:: A program in execution is a process; when several are ready to run at the same time, CPU scheduling determines which one runs.
- swapping and virtual memory ::@:: If processes do not fit in memory, swapping moves them in and out during execution, and virtual memory runs processes that are not completely in memory.
