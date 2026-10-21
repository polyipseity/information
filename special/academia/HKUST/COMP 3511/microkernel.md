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

- what a microkernel is ::@:: A minimal kernel. It gives only the core mechanisms: process management, memory management and inter-process communication. Every other service is a user-level program, in its own address space.
- motivation for microkernels ::@:: They move nonessential components out of the kernel into user-level programs. That cuts the kernel's size and complexity.

## inter-process communication

One main function of a microkernel is IPC through message passing. An application that wants a file must go through the microkernel to the file server. The program and the service never interact directly. When two user-level services communicate, the messages are copied between their separate address spaces, which costs time.

---

Flashcards for this section are as follows:

- microkernel inter-process communication (IPC) ::@:: User-level programs and services talk through the microkernel by message passing. They never call each other directly.
- microkernel message-passing overhead ::@:: Two user-level services exchange messages through the kernel. Each message is copied between separate address spaces. That costs time.

## advantages

A microkernel is easier to extend because new services go into user space without modifying the kernel. The kernel is smaller, so modifications involve fewer changes. Porting to new hardware is simpler. The system is also more secure and reliable. Less code runs in kernel mode, so a service that fails leaves the rest of the operating system intact.

---

Flashcards for this section are as follows:

- microkernel advantages ::@:: Easier to extend, port and debug. More secure and reliable, because less code runs in kernel mode.
- microkernel reliability ::@:: One service failure does not crash the rest of the system. Most services run as user processes.

## drawbacks

Performance suffers from the overhead of user space talking to kernel space. Messages between user-level services are copied across separate address spaces. Windows NT first used a layered microkernel, and it performed worse than Windows 95. Later versions moved more functions into the kernel, which made them closer to monolithic.

---

Flashcards for this section are as follows:

- microkernel performance drawback ::@:: User space and kernel space are costly to talk across. Messages are copied between separate address spaces.
- Windows NT migration ::@:: Windows NT first used a layered microkernel, and ran worse than Windows 95. Later versions moved functions into the kernel, making them closer to monolithic.

<!-- check: ignore-next-line[header_style]: proper nouns -->
## Mach and Darwin

Mach, developed at CMU in the mid-1980s, was an early microkernel. The best-known microkernel OS is Darwin, used in Mac OS X and iOS. Darwin is a hybrid XNU kernel combining the Mach microkernel and the BSD UNIX kernel.

Darwin provides two system-call interfaces: Mach traps and BSD system calls (providing POSIX functionality). Mach handles memory management, central processing unit (CPU) scheduling, and IPC. BSD provides the POSIX application program interface (API), networking, file system, and security. The kernel environment includes an I/O kit for device drivers and dynamically loadable modules called kernel extensions (kexts).

---

Flashcards for this section are as follows:

- Mach microkernel ::@:: An early microkernel from Carnegie Mellon University (CMU) in the mid-1980s. It gave memory management, processor scheduling and inter-process communication (IPC).
- Darwin kernel structure ::@:: A hybrid XNU kernel. It pairs the Mach microkernel with the BSD UNIX kernel. The Mach side handles memory management, processor scheduling and inter-process communication (IPC). The BSD side gives the POSIX application program interface (API), networking, file system and security. Two system-call interfaces reach it: Mach traps and BSD calls.
- kernel extensions (kexts) ::@:: Loadable modules in the Darwin kernel, used for device drivers.
