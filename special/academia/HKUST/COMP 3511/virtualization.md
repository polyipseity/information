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

Virtualization turns the hardware of one computer into several separate execution environments, so each user or program appears to have a private machine. It lets an operating system run as an application inside another, which makes running several operating systems on one physical machine practical, and it is the base for [cloud computing](cloud%20computing.md), which delivers computing, storage, and applications as a service over a network.

The virtual system it creates is a __virtual machine__, or __VM__, on which operating systems and applications can run, and which behaves like a real computer to the software inside. Each process behaves as if it had a dedicated processor and its own memory, because it is given a virtual copy of the host rather than the machine itself. The guest operating system is therefore a process running under the host, and one machine's hardware is shared among several users or processes that each see a private computer.

---

Flashcards for this section are as follows:

- overview ::@:: Abstracting the hardware of a single computer into several different execution environments, creating the illusion that each user or program runs on its own private computer.
- virtual machine ::@:: A virtual machine is the virtual system created by virtualization, on which operating systems and applications can run.
- operating system inside an operating system ::@:: Virtualization allows an operating system to run as an application within another operating system.
- why several virtual machines fit on one computer ::@:: Each virtual machine is an execution environment built from the hardware of a single computer rather than a machine of its own, so one physical machine can run several concurrently.
- illusion for the guest ::@:: Inside a virtual machine each process behaves as if it ran on a dedicated processor with its own memory.
- several operating systems on one machine ::@:: A single physical machine can run multiple operating systems concurrently, each in its own virtual machine.
- guest operating system as a process ::@:: The guest operating system is a process provided with a virtual copy of the host, which is how one operating system runs as an application inside another.
- sharing the computer ::@:: Because each user or program is given the illusion of a private computer, the hardware of one physical machine can be shared among several users or processes.

## virtual machines and the hypervisor

Virtualization rests on three components. The __host__ is the underlying hardware. The __virtual machine manager__ (__VMM__), or __hypervisor__, creates and manages virtual machines by presenting an interface identical to the host's. The __guest operating systems__ run inside those virtual machines; a guest is a process given a virtual copy of the host, and it is usually an operating system.

The virtual machine manager controls the system's resources completely, so the environment it presents is essentially identical to that of the original machine. Programs running inside it show only minor performance decreases, because their execution passes through more layers of software than on the bare machine.

---

Flashcards for this section are as follows:

- host ::@:: The host is the underlying hardware system on which the virtual machines run.
- virtual machine manager ::@:: The virtual machine manager, or hypervisor, creates and manages virtual machines by presenting an interface identical to the host's.
- guest operating system ::@:: A process provided with a virtual copy of the host, and usually an operating system.
- behaving like a real computer ::@:: The virtual machine manager presents an interface essentially identical to that of the original machine, so a program runs inside the virtual machine as it would on a real computer.
- performance caveat ::@:: Programs running within such an environment show only minor performance decreases, because their execution passes through more layers of software.
- control of system resources ::@:: The virtual machine manager is in complete control of the system's resources.

## system models

Two models matter here: a computer with no virtualization, and the same computer virtualized.

---

Flashcards for this section are as follows:

- what the two models share ::@:: The programming interface above a kernel, so processes in both models use the machine through the same kind of interface.

### without virtualization

In the plain model the hardware supports one __kernel__, which exposes a __programming interface__ to the processes above it, and those processes reach the machine only through it.

---

Flashcards for this section are as follows:

- model without virtualization ::@:: The hardware supports a single kernel, which exposes a programming interface to the processes above it.

### with virtualization

In the virtualized model the virtual machine manager sits on the hardware, and above it each virtual machine holds its own kernel, exposing the same kind of programming interface to its processes.

The virtualized model stacks the same picture several times over one physical machine rather than giving programs a new interface: what the processes see above their kernel is unchanged, and the layers below it are duplicated. The layer that owns the machine is the virtual machine manager, not a kernel, and each virtual machine gives the kernel above it a virtual copy of the host. The manager runs directly on the hardware, with the virtual machines and their kernels above it.

---

Flashcards for this section are as follows:

- virtualized model ::@:: The virtual machine manager sits on the hardware, and above it each virtual machine contains its own kernel, exposing a programming interface to its own processes.
- where the virtual machine manager sits ::@:: In this model the virtual machine manager runs directly on the hardware, with the virtual machines and their kernels layered above it.
- number of kernels ::@:: A system without virtualization has one kernel on the hardware, whereas a virtualized system has one kernel inside each virtual machine.

## motivations for virtualization

__Server consolidation__ is the leading motivation: consolidating multiple operating systems onto fewer hardware platforms lets services run on different machines with different operating systems, or different versions of one.

On a desktop a user can run Linux or macOS and still reach native applications on Windows. Developers can run many operating system types and versions on one machine, which makes testing and debugging easier.

---

Flashcards for this section are as follows:

- server consolidation ::@:: Consolidating multiple operating systems onto fewer hardware platforms, so services can run on machines running different operating systems, or different versions of one.
- several operating systems on one computer ::@:: Because each guest operating system has its own virtual machine, one computer can run several different operating systems at the same time.
- desktop use ::@:: A user can run Linux or macOS and still have access to native applications on a different platform such as Windows.
- developer testing and debugging ::@:: Developers can run many operating system types and versions on just one machine.

## history and adoption

Virtualization was first designed in IBM mainframes in 1972, to let multiple users run tasks concurrently on a system built for one, or to share a batch-oriented system. It later reached general-purpose hardware: VMware runs one or more guest copies of Windows, each with its own applications, on an Intel x86 CPU.

In the late 1990s Intel CPUs became fast enough for virtualization on general-purpose PCs, and Xen and VMware built technologies still used today. Virtualization has since spread to many operating systems, CPUs, and virtual machine managers.

---

Flashcards for this section are as follows:

- origins in IBM mainframes ::@:: Virtualization was originally designed in IBM mainframes in 1972.
- original mainframe goal ::@:: It allowed multiple users to run tasks concurrently in a system designed for a single user, or share a batch-oriented system.
- VMware on x86 ::@:: VMware runs one or more guest copies of Windows, each running its own applications, on an Intel x86 CPU.
- return on general-purpose PCs ::@:: In the late 1990s Intel CPUs became fast enough for virtualization on general-purpose PCs.
- Xen and VMware ::@:: Virtual machine managers such as Xen and VMware created virtualization technologies for x86 that are still used today.
- spread of virtualization ::@:: Virtualization has expanded to many operating systems, CPUs, and virtual machine managers.
