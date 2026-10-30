---
aliases:
  - microkernel
  - microkernel system structure
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/microkernel
  - language/in/English
---

# microkernel

A microkernel keeps little beyond what an operating system needs: process and memory management, plus inter-process communication (IPC). Every other component runs as a user-level program in its own address space.

---

Flashcards for this section are as follows:

- what a microkernel is ::@:: A kernel that holds only process and memory management, plus inter-process communication. Everything else is a user-level program. Each one gets its own address space.
- motivation for microkernels ::@:: Unneeded parts move out of the kernel into user programs. That makes the kernel smaller and simpler.

## inter-process communication

The kernel carries IPC by message passing. An application that wants a file asks the file server through the microkernel; the two never interact directly. When two user-level services talk, the kernel copies each message between their separate address spaces, and that costs time.

---

Flashcards for this section are as follows:

- microkernel inter-process communication (IPC) ::@:: User-level programs and services talk through the microkernel by message passing; they never call each other directly.
- microkernel message-passing overhead ::@:: Two user-level services exchange messages through the kernel, and each message is copied between separate address spaces. That costs time.

## advantages

A new service runs in user space, so extending the system leaves the kernel alone. A smaller kernel means a modification touches fewer places, and porting to new hardware takes less work. Security and reliability improve too: less code runs in kernel mode, so one failing service leaves the rest of the system intact.

---

Flashcards for this section are as follows:

- microkernel advantages ::@:: Easier to extend, port and debug. More secure and reliable, because less code runs in kernel mode.
- microkernel reliability ::@:: One failing service does not crash the rest of the system, because most services run as user processes.

## drawbacks

Performance suffers because crossing into the kernel from user space is expensive. Windows NT started with a layered microkernel and ran worse than Windows 95. Later versions pulled more functions into the kernel, closer to a monolithic design.

---

Flashcards for this section are as follows:

- microkernel performance drawback ::@:: Talking across user space and kernel space is costly. Messages are copied between separate address spaces.
- Windows NT migration ::@:: Windows NT started with a layered microkernel and ran worse than Windows 95. Later versions moved functions into the kernel, closer to a monolithic design.

<!-- check: ignore-next-line[header_style]: proper nouns -->
## Mach and Darwin

Carnegie Mellon University (CMU) built Mach, an early microkernel, in the mid-1980s. Darwin, the hybrid XNU kernel of Mac OS X and iOS, is the best-known microkernel system. It pairs Mach with the BSD UNIX kernel.

Darwin exposes two system-call interfaces: Mach traps and BSD system calls with POSIX functionality. Mach handles memory management, central processing unit (CPU) scheduling and IPC. BSD gives the POSIX application program interface (API), networking, the file system and security. The kernel environment holds an I/O kit for device drivers and dynamically loadable kernel extensions (kexts).

---

Flashcards for this section are as follows:

- Mach microkernel ::@:: An early microkernel from Carnegie Mellon University (CMU) in the mid-1980s. It gave memory management, processor scheduling and inter-process communication (IPC).
- Darwin kernel structure ::@:: Darwin is a hybrid XNU kernel pairing the Mach microkernel with the BSD UNIX kernel. Mach handles memory management, processor scheduling and inter-process communication (IPC); BSD gives the POSIX application program interface (API), networking, file system and security. It offers two system-call interfaces: Mach traps and BSD calls.
- kernel extensions (kexts) ::@:: Loadable modules in the Darwin kernel, used for device drivers.
