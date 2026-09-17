---
aliases:
  - COMP 3511 multiprocessing
  - SMP
  - multiprocessor system
  - symmetric multiprocessing
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/multiprocessing
  - language/in/English
---

# multiprocessing

A traditional computer had one processor holding one CPU with one core, so all work passed through a single general-purpose unit with its own registers, arithmetic-logic unit, and control unit. Modern systems, from phones to servers, spread work over several processors and over several cores on one chip instead, which changes how an operating system schedules work and manages memory.

---

Flashcards for this section are as follows:

- overview ::@:: The use of more than one processor, or more than one computing core, in a computer system; modern systems from mobile devices to servers rely on it instead of a single processor with one core.
- single-processor baseline ::@:: The traditional design: one processor holding one CPU with a single core executing a general-purpose instruction set.
- why multiprocessing matters to an operating system ::@:: Processors or cores share the same physical memory and system bus, so the operating system must schedule work and manage memory across concurrently executing units.
- asymmetric versus symmetric multiprocessing ::@:: Asymmetric multiprocessing uses a master processor that assigns work to the others, whereas symmetric multiprocessing treats every processor equally.
- multicore versus multiprocessor ::@:: Multicore means several computing cores on one physical chip, while a multiprocessor system contains several processors.

## single-processor systems

Most early computer systems used one processor containing one CPU with a single core. A core executes instructions and holds registers for local data, and a CPU core can execute a general-purpose instruction set.

A general-purpose CPU contains an arithmetic-logic unit, processor registers, and a control unit with an instruction register and a program counter. Such systems also hold special-purpose processors, such as disk and graphics controllers and graphics processing units. These run a limited instruction set and usually do not execute instructions from user processes.

---

Flashcards for this section are as follows:

- single-processor system ::@:: One processor containing one CPU with a single core, the traditional arrangement for most early computer systems.
- processing core ::@:: The component that executes instructions and holds registers for local data; a CPU core executes a general-purpose instruction set.
- general-purpose CPU contents ::@:: A central processing unit containing an arithmetic-logic unit and processor registers, plus a control unit containing an instruction register and a program counter.
- special-purpose processors ::@:: Single-processor systems still contain device-specific processors such as disk controllers and graphics controllers (GPUs), which run a specific and limited instruction set and usually do not execute instructions from user processes.

## multiprocessor systems

Multiprocessor systems are now the norm, from mobile devices to servers. Traditionally such a system has two or more processors, each with a single-core CPU.

They offer three advantages. Throughput rises with the extra computing capability. Economy of scale comes from sharing devices such as input/output, power supplies, housings, and peripherals. Reliability improves, because the system can keep working when one processor fails, either by graceful degradation or by fault tolerance.

Adding processors does not scale proportionally: the speed-up with $N$ processors is less than $N$, because of overhead such as contention for the system bus or for memory. Multiprocessor systems are also more complex in hardware design and in software, for example in parallel programming.

Two types are distinguished. In asymmetric multiprocessing, often a master-slave arrangement, the master assigns tasks to the slaves and handles input/output itself. In symmetric multiprocessing all processors are equal, so every one performs all tasks, including operating-system functions and user processes, and any processor can handle input/output.

---

Flashcards for this section are as follows:

- multiprocessor system ::@:: A system with two or more processors, traditionally each with a single-core CPU; now the norm from mobile devices to servers.
- advantages of multiprocessor systems ::@:: Increased throughput through more computing capability, economy of scale from sharing devices such as input/output, power supplies, housings, and peripherals, and increased reliability through graceful degradation or fault tolerance.
- scaling with $N$ processors ::@:: The speed-up with $N$ processors is less than $N$ because of overhead such as contention for shared resources, namely the system bus or memory.
- asymmetric multiprocessing ::@:: A master processor assigns specific tasks to slave processors, an arrangement often described as master-slave, and the master handles input/output.
- complexity of multiprocessor systems ::@:: They are far more complex than single-processor systems in both hardware design and software, for example in parallel programming.

## symmetric multiprocessing

Symmetric multiprocessing, or SMP, treats all processors equally. Each CPU has its own registers and a private, or local, cache, but all processors share physical memory through the system bus. Every processor performs all tasks, including operating-system functions and user processes, and any of them can handle input/output, so none is reserved as a master.

That is what separates it from asymmetric multiprocessing, where one master CPU distributes tasks among the slave CPUs and usually handles input/output alone.

---

Flashcards for this section are as follows:

- symmetric multiprocessing ::@:: All processors are treated equally: each CPU has its own registers and private cache while all processors share physical memory through the system bus.
- SMP private state per CPU ::@:: Each CPU has its own registers and a private (local) cache.
- SMP shared memory ::@:: All processors share physical memory through the system bus.
- SMP task and input/output handling ::@:: Every processor performs all tasks, including operating-system functions and user processes, so input/output can be handled by any processor rather than by one master.
- symmetric versus asymmetric multiprocessing ::@:: Symmetric multiprocessing treats all processors equally and lets any processor handle input/output, whereas asymmetric multiprocessing has one master CPU that distributes tasks among the slave CPUs and usually performs input/output itself.

## multicore systems

A multicore design puts several computing cores on one chip. On-chip communication is faster than between-chip, so one such chip beats several single-core chips. It also uses significantly less power, which matters for phones and laptops running on battery.

Within the chip each core keeps its own registers and its own L1 cache, and the cores share one L2 cache that sits between them and main memory. The first cache level is therefore private to a core, while the next level is shared.

---

Flashcards for this section are as follows:

- multicore design ::@:: Multiple computing cores reside on a single physical chip.
- on-chip versus between-chip communication ::@:: On-chip communication is faster than between-chip communication, which makes one multicore chip more efficient than multiple processor chips each holding a single core.
- multicore power consumption ::@:: One chip with multiple cores uses significantly less power than multiple single-core chips.
- why multicore power matters ::@:: Lower power use matters for battery-powered devices such as mobile devices and laptops.
- multicore cache topology ::@:: Each core on the chip keeps its own registers and its own L1 cache, while the cores share one L2 cache sitting between them and main memory.

## non-uniform memory access

Adding CPUs to a multiprocessor system may not scale, because contention for the system bus can become a bottleneck. One alternative gives each CPU, or group of CPUs, its own local memory reached through a small, fast local bus. The CPUs are then joined by a shared interconnect while still sharing one physical address space. This is non-uniform memory access, or NUMA.

A CPU reaches its own local memory over a fast local bus, but reaches another CPU's memory across the shared interconnect, so access times are not uniform. The drawback is the added latency of remote access, which has implications for scheduling and memory management.

---

Flashcards for this section are as follows:

- non-uniform memory access ::@:: Each CPU, or group of CPUs, has its own local memory reached through a small, fast local bus, while the CPUs are joined by a shared interconnect and share one physical address space.
- why NUMA is used ::@:: Adding more CPUs to a multiprocessor system may not scale because of contention for the system bus, which can become a bottleneck.
- why NUMA access times are not uniform ::@:: A CPU reaches its own local memory over a small, fast local bus, but reaches remote memory across the shared system interconnect, so the two kinds of access differ in speed.
- NUMA local memory ::@:: Local memory per CPU, or per group of CPUs, reached through a small, fast local bus.
- NUMA drawback ::@:: Increased latency when a CPU must access remote memory across the system interconnect, which has implications for CPU scheduling and memory management.

## cpu, processor, and core terminology

The terms nest. A CPU is the hardware that executes instructions. A processor is a chip holding one or more CPUs. A core is the basic computation unit of a CPU, the part that executes instructions and holds registers for local data. Multicore means several cores on one chip; a multiprocessor system contains several processors.

---

Flashcards for this section are as follows:

- terminology: CPU ::@:: The hardware that executes instructions.
- terminology: processor ::@:: A physical chip that contains one or more CPUs.
- terminology: core ::@:: The basic computation unit of the CPU, executing instructions and holding registers for storing data locally.
- terminology: multicore ::@:: Multiple computing cores on a single physical processor chip.
- terminology: multiprocessor system ::@:: A system including multiple processors.
