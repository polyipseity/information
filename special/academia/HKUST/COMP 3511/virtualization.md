---
aliases:
  - COMP 3511 virtualization
  - virtual machine
  - virtualization
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/virtualization
  - language/in/English
---

# virtualization

Virtualization splits one computer's hardware into several separate execution environments, each looking like a private machine to its user or program. An operating system can then run as an application inside another, so one physical machine holds several at once. It also underlies [cloud computing](cloud%20computing.md), which delivers computing, storage and applications over a network.

The virtual system it creates is a __virtual machine__, or __VM__, which looks like a real computer to the software inside; operating systems and applications run on it. A process there behaves as if it had a dedicated processor and its own memory, because it holds a virtual copy of the host. The guest operating system runs as a process under the host, so one machine's hardware serves several users or processes, each seeing a private computer.

---

Flashcards for this section are as follows:

- what virtualization is ::@:: Virtualization turns one computer's hardware into several execution environments, so each user or program appears to run on a private computer.
- what a virtual machine is ::@:: A virtual machine is the system virtualization creates, and operating systems and applications run on it.
- what virtualization lets a guest operating system do ::@:: An operating system can run as an application inside another operating system.
- why several virtual machines fit on one computer ::@:: Each virtual machine is an execution environment built from one computer's hardware, so a single machine runs several at once.
- what each process inside a virtual machine sees ::@:: The process behaves as if it had a dedicated processor and its own memory.
- what one physical machine can run ::@:: One physical machine can run several operating systems at once, one per virtual machine.
- how a guest operating system runs ::@:: The guest operating system is a process under the host, given a virtual copy of it.
- what lets several users share one computer ::@:: Each user or program sees a private computer, so one machine's hardware is shared among several.

## virtual machines and the hypervisor

Virtualization has three parts. The __host__ is the hardware underneath. The __virtual machine manager__ (__VMM__), or __hypervisor__, creates and manages virtual machines by presenting an interface identical to the host's. Inside those machines run the __guest operating systems__, processes given a virtual copy of the host and usually operating systems themselves.

The manager controls the system's resources completely, so the environment it presents is essentially identical to the original machine's. Programs inside it slow down only slightly, because execution passes through more software layers than on bare hardware.

---

Flashcards for this section are as follows:

- what the host is ::@:: The host is the hardware underneath, and the virtual machines run on it.
- what the virtual machine manager does ::@:: The virtual machine manager, or hypervisor, creates and manages virtual machines, giving each an interface identical to the host's.
- what a guest operating system is ::@:: A guest operating system is a process given a virtual copy of the host, usually an operating system itself.
- what interface the virtual machine manager presents ::@:: The manager presents an interface essentially identical to the original machine's, so programs run as they would on real hardware.
- how fast programs run inside a virtual machine ::@:: They slow down only slightly, because execution passes through more software layers than on bare hardware.
- who controls the system's resources ::@:: The virtual machine manager controls them completely.

## machine switch

A context switch saves one process, and a machine switch saves a whole virtual machine. The manager stores the entire machine state of the guest: registers, program counter and the privileged hardware state that a context switch leaves alone. It then restores the state of the incoming guest and jumps to its program counter, which may sit in that guest's kernel, midway through a system call, or in a user process.

---

Flashcards for this section are as follows:

- machine switch ::@:: The virtual machine manager saving one guest's entire machine state, privileged hardware state included, and loading another's.
- what a machine switch saves that a context switch does not ::@:: The privileged hardware state, which a context switch leaves alone.
- where a restored guest resumes after a machine switch ::@:: At its saved program counter, which may sit inside its kernel, mid system call, or inside a user process.

## system models

Two models matter: a computer without virtualization, and the same one with it.

---

Flashcards for this section are as follows:

- what the two models share ::@:: The processes above a kernel reach the machine through the same programming interface in both.

### without virtualization

The plain model has one __kernel__ on the hardware, which exposes a __programming interface__ to the processes above it; they reach the machine only through that interface.

---

Flashcards for this section are as follows:

- how the plain model is arranged ::@:: One kernel sits on the hardware and exposes a programming interface to the processes above it.

### with virtualization

In the virtualized model the manager sits on the hardware, and each virtual machine above it holds its own kernel, exposing the same kind of programming interface to its processes.

The virtualized model repeats one picture several times over one machine and gives programs no new interface. What a process sees above its kernel stays the same; everything below it is duplicated. The virtual machine manager owns the machine, not a kernel, and each virtual machine hands the kernel above it a virtual copy of the host. The manager runs directly on the hardware, under the virtual machines and their kernels.

---

Flashcards for this section are as follows:

- what the virtualized model looks like ::@:: The manager sits on the hardware, and each virtual machine above it holds its own kernel, which exposes a programming interface to its processes.
- where the virtual machine manager sits ::@:: The manager runs directly on the hardware, under the virtual machines and their kernels.
- how many kernels each model has ::@:: A system without virtualization has one kernel on the hardware, while a virtualized system has one inside each virtual machine.

## motivations for virtualization

__Server consolidation__ is the main motivation: several operating systems on fewer hardware platforms, so services run on machines with different operating systems, or different versions of one.

A desktop user can run Linux or macOS and still reach native Windows applications. Developers can run many operating system types and versions on one machine, so testing and debugging get easier.

---

Flashcards for this section are as follows:

- what server consolidation is ::@:: Server consolidation puts several operating systems on fewer hardware platforms, so services run on machines with different operating systems, or different versions of one.
- why one computer can run several operating systems ::@:: Each guest operating system has its own virtual machine, so one computer runs several at the same time.
- what a desktop user gains ::@:: A user can run Linux or macOS and still reach native applications on another platform, such as Windows.
- why developers use virtual machines ::@:: Developers can run many operating system types and versions on one machine, so testing and debugging get easier.

## history and adoption

Virtualization first appeared on IBM mainframes in 1972, so several users could run tasks at once on a system built for one, or share a batch-oriented system. Later it reached general-purpose hardware: VMware runs one or more guest copies of Windows, each with its own applications, on an Intel x86 central processing unit (CPU).

In the late 1990s Intel CPUs grew fast enough for virtualization on ordinary PCs, and Xen and VMware built technologies still in use. It has since spread across many operating systems, CPUs, and virtual machine managers.

---

Flashcards for this section are as follows:

- where and when virtualization started ::@:: Virtualization was first designed in IBM mainframes in 1972.
- what the mainframe version was for ::@:: It let several users run tasks at once on a system built for one, or share a batch-oriented system.
- VMware on x86 ::@:: VMware runs one or more guest copies of Windows, each with its own applications, on an Intel x86 central processing unit (CPU).
- what made virtualization practical on PCs ::@:: In the late 1990s Intel central processing units (CPUs) became fast enough for it on general-purpose PCs.
- Xen and VMware ::@:: Virtual machine managers such as Xen and VMware built virtualization technologies for x86 that are still in use.
- where virtualization has spread ::@:: It has spread to many operating systems, central processing units (CPUs), and virtual machine managers.
