---
aliases:
  - microkernel
  - microkernel system structure
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/microkernel
  - language/in/English
---

# microkernel

A microkernel provides only the near-minimum mechanisms needed for an operating system: process management, memory management, and inter-process communication (IPC). All other components are removed from the kernel and implemented as user-level programs running in separate address spaces.

---

Flashcards for this section are as follows:

- overview ::@:: A minimal kernel that provides only fundamental mechanisms — process management, memory management, and inter-process communication — with all other services implemented as user-level programs in separate address spaces.
- motivation for microkernels ::@:: Microkernels move nonessential components out of the kernel into user-level programs, reducing kernel size and complexity.

## inter-process communication

One main function of a microkernel is IPC through message passing. If an application program wishes to access a file, it must interact with the file server through the microkernel; the program and service never interact directly. When two user-level services communicate, messages must be copied between their separate address spaces, introducing overhead.

---

Flashcards for this section are as follows:

- microkernel IPC ::@:: In a microkernel, user-level programs and services communicate indirectly through message passing via the microkernel, rather than interacting directly with each other.
- microkernel message-passing overhead ::@:: When two user-level services communicate, messages must be copied between separate address spaces, introducing performance overhead.

## advantages

A microkernel is easier to extend because new services go into user space without modifying the kernel. The kernel is smaller, so modifications involve fewer changes. Porting to new hardware is simpler. The system is more secure and reliable: less code runs in kernel mode, so if a service fails, the rest of the OS stays intact.

---

Flashcards for this section are as follows:

- microkernel advantages ::@:: Easier to extend, port, and debug; more secure and reliable because less code runs in kernel mode.
- microkernel reliability ::@:: A single service failure does not crash the rest of the operating system, since most services run as user processes.

## drawbacks

Performance suffers due to user-space to kernel-space communication overhead. Messages between user-level services are copied across separate address spaces. Windows NT originally had a layered microkernel design and performed worse than Windows 95; later versions moved more functions into the kernel, becoming more monolithic.

---

Flashcards for this section are as follows:

- microkernel performance drawback ::@:: Overhead from user-space to kernel-space communication and message copying between separate address spaces.
- Windows NT migration ::@:: Windows NT originally used a layered microkernel but performed worse than Windows 95; later versions moved more functions into the kernel, becoming more monolithic for performance.

## Mach and Darwin <!-- check: ignore-line[header_style]: proper nouns -->

Mach, developed at CMU in the mid-1980s, was an early microkernel. The best-known microkernel OS is Darwin, used in Mac OS X and iOS. Darwin is a hybrid XNU kernel combining the Mach microkernel and the BSD UNIX kernel.

Darwin provides two system-call interfaces: Mach traps and BSD system calls (providing POSIX functionality). Mach handles memory management, CPU scheduling, and IPC. BSD provides the POSIX API, networking, file system, and security. The kernel environment includes an I/O kit for device drivers and dynamically loadable modules called kernel extensions (kexts).

---

Flashcards for this section are as follows:

- Mach microkernel ::@:: An early microkernel from CMU (mid-1980s) providing memory management, CPU scheduling, and IPC.
- Darwin kernel structure ::@:: A hybrid XNU kernel: Mach microkernel (memory management, CPU scheduling, IPC) plus BSD UNIX kernel (POSIX API, networking, file system, security), with two system-call interfaces: Mach traps and BSD calls.
- kernel extensions (kexts) ::@:: Dynamically loadable modules in the Darwin kernel, used for device drivers and other extensions.
