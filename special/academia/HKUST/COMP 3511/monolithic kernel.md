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

A monolithic kernel runs the entire operating system in kernel mode within a single address space. All functionality — process management, memory management, file systems, device drivers, networking — sits in one static binary. This design has a performance advantage: minimal overhead in the system-call interface, and fast intra-kernel communication through direct function calls rather than message passing.

---

Flashcards for this section are as follows:

- overview ::@:: An OS architecture in which the entire operating system runs in kernel mode in a single address space, with all functionality in one static binary.
- performance advantage of monolithic kernels ::@:: Minimal overhead in the system-call interface and fast intra-kernel communication through direct function calls, since everything runs in one address space.

## original UNIX structure

In traditional UNIX, the kernel consists of everything below the system-call interface and above the physical hardware: signal handling, terminal handling, character I/O, the file system, CPU scheduling, page replacement, demand paging, virtual memory, and device drivers for terminals, disks, and tapes. The hardware layer provides terminal controllers, device controllers, and memory controllers.

UNIX initially had limited structuring due to hardware constraints. All functionality was placed into a single, static binary running in one address space: the monolithic structure. The kernel grew over the years as UNIX evolved, expanding its interfaces and device drivers.

All OS functionality combined into one level makes the system difficult to implement, debug, and maintain. Despite this, monolithic kernels remain in use in UNIX, Linux, and Windows for their speed and efficiency.

---

Flashcards for this section are as follows:

- original UNIX kernel structure ::@:: The kernel consists of everything below the system-call interface and above the physical hardware: signals, I/O, file systems, CPU scheduling, memory management, and device drivers, all in a single address space.
- monolithic kernel drawback ::@:: Enormous functionality combined into one level makes the system difficult to implement, debug, and maintain.
- why monolithic kernels persist ::@:: Their speed and efficiency — direct function calls within one address space have minimal overhead — keep them in use in UNIX, Linux, and Windows.

## Linux system structure <!-- check: ignore-line[header_style]: Linux is a proper noun -->

The Linux kernel is monolithic: it runs entirely in kernel mode in a single address space, with applications using glibc to reach the system-call interface.

Linux also has a modular design that allows the kernel to be modified at runtime through loadable kernel modules (LKMs), combining monolithic performance with the flexibility of adding functionality without recompiling the entire kernel.

---

Flashcards for this section are as follows:

- Linux kernel architecture ::@:: A monolithic kernel running in kernel mode in a single address space, with applications using glibc to reach the system-call interface.
- Linux modularity ::@:: Despite being monolithic, Linux uses loadable kernel modules to add functionality at runtime, combining monolithic performance with modular flexibility.
