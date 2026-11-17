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

A monolithic kernel runs the whole operating system in kernel mode, in one address space. Process management, memory management, file systems, device drivers and networking share one static binary. System calls cost little, since parts call each other directly instead of passing messages.

---

Flashcards for this section are as follows:

- what a monolithic kernel is ::@:: An operating system (OS) architecture that runs everything in kernel mode, in one address space, as one static binary. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- performance advantage of monolithic kernels ::@:: System calls cost little, since one part of the kernel calls another directly and no message is sent. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->

## original UNIX structure

In traditional UNIX the kernel covers everything between the system-call interface and the physical hardware. It handles signals, terminals, character input/output (I/O), the file system, and drivers for terminals, disks and tapes. It also runs central processing unit (CPU) scheduling, page replacement, demand paging and virtual memory. Below it, the hardware layer supplies terminal, device and memory controllers.

Hardware limits left early UNIX with little structure: everything went into one static binary in one address space. That is the monolithic structure. Interfaces and device drivers arrived as UNIX grew.

Every operating system function at one level makes a system hard to implement, debug and maintain. UNIX, Linux and Windows still use monolithic kernels because they are fast.

---

Flashcards for this section are as follows:

- original UNIX kernel structure ::@:: Everything between the system-call interface and the hardware: signals, input/output (I/O), file systems, central processing unit (CPU) scheduling, memory and device drivers, all in one address space. <!--SR:!fsrs,2027-01-23T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-18T00:00:00.000Z!fsrs,2027-01-23T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-18T00:00:00.000Z-->
- monolithic kernel drawback ::@:: One level holding every operating system function makes a system hard to implement, debug and maintain. <!--SR:!fsrs,2027-01-23T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-18T00:00:00.000Z!fsrs,2027-01-23T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-18T00:00:00.000Z-->
- why monolithic kernels persist ::@:: Direct calls inside one address space cost little, so UNIX, Linux and Windows stay monolithic. <!--SR:!fsrs,2027-01-23T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-18T00:00:00.000Z!fsrs,2027-01-23T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-18T00:00:00.000Z-->

<!-- check: ignore-next-line[header_style]: Linux is a proper noun -->
## Linux system structure

The Linux kernel is monolithic and runs entirely in kernel mode in one address space. Applications reach the system-call interface through glibc.

Linux is modular too. Loadable kernel modules (LKMs) add functions at runtime without recompiling everything, so the kernel keeps its monolithic speed.

---

Flashcards for this section are as follows:

- Linux kernel architecture ::@:: A monolithic kernel running in kernel mode in one address space, with applications reaching the system-call interface through glibc. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- Linux modularity ::@:: Loadable kernel modules (LKMs) add functions at runtime without a rebuild, so Linux keeps monolithic speed. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
