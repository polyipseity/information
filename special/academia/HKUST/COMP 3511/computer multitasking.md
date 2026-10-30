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

Every modern operating system does both. __Multiprogramming__ is the batch system kept for efficiency. __Time sharing__, or multitasking, extends it for interactive use. Both exist because one program at a time leaves the processor and devices idle.

---

Flashcards for this section are as follows:

- two characteristics of modern operating systems ::@:: Multiprogramming is the batch system kept for efficiency, and time sharing, or multitasking, extends it for interactive use.

## multiprogramming

Early systems loaded one program into memory at a time, and that program cannot keep the central processing unit (CPU) or the input/output (I/O) devices busy. Faster devices made every modern system multiprogrammed. Multiprogramming arranges jobs so the CPU always has one to run. On a mainframe, remote jobs queue up; __job scheduling__ picks and loads them into memory.

---

Flashcards for this section are as follows:

- multiprogramming ::@:: Multiprogramming arranges jobs so the central processing unit (CPU) always has one to run. One program cannot keep the CPU and the input/output (I/O) devices busy, so every modern system is multiprogrammed.
- job scheduling ::@:: On a mainframe, remote jobs queue up. Job scheduling picks and loads them into memory.

## time sharing

__Time sharing__ extends multiprogramming: the CPU switches between jobs often enough for users to interact with each while it runs. That switching is interactive computing, and response time must stay under a threshold. A program in execution is a __process__. When several are ready at once, __CPU scheduling__ chooses the order. When they do not all fit in memory, __swapping__ moves them in and out during execution, and __virtual memory__ runs processes not completely in memory. Both need operating-system support.

---

Flashcards for this section are as follows:

- time sharing ::@:: Time sharing extends multiprogramming: the central processing unit (CPU) switches between jobs often enough for users to interact with each while it runs. That switching is interactive computing, and response time must stay under a threshold.
- process and central processing unit (CPU) scheduling ::@:: A program in execution is a process. When several are ready at once, central processing unit (CPU) scheduling chooses which one runs.
- swapping and virtual memory ::@:: When processes do not all fit in memory, swapping moves them in and out during execution, and virtual memory runs processes not completely in memory.
