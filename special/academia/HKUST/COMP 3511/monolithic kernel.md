---
aliases:
  - monolithic kernel
  - monolithic operating system
  - monolithic structure
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/monolithic_kernel
  - language/in/English
---

# monolithic kernel

A monolithic kernel runs the whole operating system in kernel mode, in one address space. Process management, memory management, file systems, device drivers and networking all sit in a single static binary. That arrangement is fast. A system call carries little overhead, and one part calls another directly instead of passing a message.

---

Flashcards for this section are as follows:

- what a monolithic kernel is ::@:: An operating system (OS) architecture that runs everything in kernel mode, in one address space, as one static binary.
- performance advantage of monolithic kernels ::@:: A system call crosses little overhead, and parts call each other directly instead of passing messages.

## original UNIX structure

In traditional UNIX the kernel covers everything between the system-call interface and the physical hardware. That means signals, terminals, character input/output (I/O) and the file system. It also covers central processing unit (CPU) scheduling, page replacement, demand paging and virtual memory, plus drivers for terminals, disks and tapes. Below it, the hardware layer supplies terminal controllers, device controllers and memory controllers.

Hardware limits left early UNIX with little structure. Everything went into one static binary running in one address space, which is the monolithic structure. The kernel then grew as UNIX grew, adding interfaces and device drivers.

One level holding every operating system function makes the system hard to implement, debug and maintain. UNIX, Linux and Windows still use monolithic kernels, because they are fast and efficient.

---

Flashcards for this section are as follows:

- original UNIX kernel structure ::@:: Everything below the system-call interface and above the hardware: signals, input/output (I/O), file systems, central processing unit (CPU) scheduling, memory and drivers, all in one address space.
- monolithic kernel drawback ::@:: Combining every function into one level makes the system hard to implement, debug and maintain.
- why monolithic kernels persist ::@:: They are fast. Direct calls inside one address space cost little, so UNIX, Linux and Windows keep them.

<!-- check: ignore-next-line[header_style]: Linux is a proper noun -->
## Linux system structure

The Linux kernel is monolithic. It runs entirely in kernel mode in one address space, and applications reach the system-call interface through glibc.

Linux is also modular. Loadable kernel modules (LKMs) change the kernel at runtime, so it keeps monolithic speed and still gains functions without recompiling everything.

---

Flashcards for this section are as follows:

- Linux kernel architecture ::@:: A monolithic kernel in kernel mode, one address space, with applications reaching the system-call interface through glibc.
- Linux modularity ::@:: Loadable kernel modules (LKMs) add functions at runtime, so Linux keeps monolithic speed and still changes without a rebuild.
