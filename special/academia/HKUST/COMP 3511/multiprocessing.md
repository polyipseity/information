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

A traditional computer had one processor holding one central processing unit (CPU) with one core, so all work passed through a single general-purpose unit with its own registers, arithmetic-logic unit, and control unit. Modern systems, from phones to servers, spread work over several processors and over several cores on one chip instead, which changes how an operating system schedules work and manages memory.

---

Flashcards for this section are as follows:

- what multiprocessing is ::@:: Using more than one processor, or more than one core, in a computer. Systems from phones to servers rely on it instead of one processor with one core.
- single-processor baseline ::@:: The old design: one processor holding one central processing unit (CPU) with a single core. It runs a general-purpose instruction set.
- why multiprocessing matters to an operating system ::@:: Processors or cores share the same memory and system bus. The operating system must then schedule work and manage memory across units running at once.
- asymmetric versus symmetric multiprocessing ::@:: Asymmetric multiprocessing uses a master processor that assigns work to the others. Symmetric multiprocessing treats every processor equally.
- multicore versus multiprocessor ::@:: Multicore means several cores on one chip. A multiprocessor system holds several processors.

## single-processor systems

Most early computer systems used one processor containing one CPU with a single core. A core executes instructions and holds registers for local data, and a CPU core can execute a general-purpose instruction set.

A general-purpose CPU contains an arithmetic-logic unit, processor registers, and a control unit with an instruction register and a program counter. Such systems also hold special-purpose processors, such as disk and graphics controllers and graphics processing units. These run a limited instruction set and usually do not execute instructions from user processes.

---

Flashcards for this section are as follows:

- single-processor system ::@:: One processor holding one central processing unit (CPU) with a single core. Most early computers worked that way.
- processing core ::@:: The part that runs instructions and holds registers for local data. A central processing unit (CPU) core runs a general-purpose instruction set.
- general-purpose CPU contents ::@:: A central processing unit holding an arithmetic-logic unit and processor registers. It also has a control unit, with an instruction register and a program counter.
- special-purpose processors ::@:: Single-processor systems still hold device-specific processors: disk controllers, graphics controllers and graphics processing units (GPUs). They run a fixed, narrow instruction set and usually do not run instructions from user processes.

## multiprocessor systems

Multiprocessor systems are now the norm, from mobile devices to servers. Traditionally such a system has two or more processors, each with a single-core CPU.

They offer three advantages. Throughput rises with the extra computing capability. Economy of scale comes from sharing devices such as input/output, power supplies, housings, and peripherals. Reliability improves, because the system can keep working when one processor fails, either by graceful degradation or by fault tolerance.

Adding processors does not scale proportionally: the speed-up with $N$ processors is less than $N$, because of overhead such as contention for the system bus or for memory. Multiprocessor systems are also more complex in hardware design and in software, for example in parallel programming.

Two kinds of multiprocessor system are distinguished, asymmetric multiprocessing and symmetric multiprocessing.

---

Flashcards for this section are as follows:

- multiprocessor system ::@:: A system with two or more processors, once each with a single-core central processing unit (CPU). It is now the norm from phones to servers.
- advantages of multiprocessor systems ::@:: More processors raise throughput. Sharing input/output, power supplies, housings and peripherals gives economy of scale. Graceful degradation, or fault tolerance, adds reliability.
- scaling with $N$ processors ::@:: The speed-up with $N$ processors is less than $N$ because of overhead from contention for the system bus or memory.
- complexity of multiprocessor systems ::@:: They are far more complex than single-processor systems, in hardware and in software. Parallel programming is one example.

### asymmetric multiprocessing

In __asymmetric multiprocessing__, often a master-slave arrangement, the master processor assigns specific tasks to the slave processors and handles input/output itself, so the processors are not equal.

---

Flashcards for this section are as follows:

- asymmetric multiprocessing ::@:: A master processor assigns tasks to slave processors, an arrangement often called master-slave. The master also handles input/output.

### symmetric multiprocessing

Symmetric multiprocessing, or SMP, treats all processors equally. Each CPU has its own registers and a private, or local, cache, but all processors share physical memory through the system bus. Every processor performs all tasks, including operating-system functions and user processes, and any of them can handle input/output, so none is reserved as a master.

That is what separates it from asymmetric multiprocessing.

---

Flashcards for this section are as follows:

- symmetric multiprocessing ::@:: All processors are treated equally. Each central processing unit (CPU) has its own registers and its own cache. All processors share memory through the system bus.
- symmetric multiprocessing (SMP) private state per central processing unit (CPU) ::@:: Each has its own registers and a private local cache.
- symmetric multiprocessing (SMP) shared memory ::@:: All processors share memory through the system bus.
- symmetric multiprocessing (SMP) task and input/output handling ::@:: Every processor runs all tasks, including operating-system functions and user processes. Any processor can handle input/output, rather than one master.
- symmetric versus asymmetric multiprocessing ::@:: Symmetric multiprocessing treats all processors equally and lets any handle input/output. Asymmetric multiprocessing has one master central processing unit (CPU) that hands tasks to the slave CPUs. The master usually handles input/output itself.

### multicore systems

A multicore design puts several computing cores on one chip. On-chip communication is faster than between-chip, so one such chip beats several single-core chips. It also uses significantly less power, which matters for phones and laptops running on battery.

Within the chip each core keeps its own registers and its own L1 cache, and the cores share one L2 cache that sits between them and main memory. The first cache level is therefore private to a core, while the next level is shared.

---

Flashcards for this section are as follows:

- multicore design ::@:: Several cores sit on one chip.
- on-chip versus between-chip communication ::@:: On-chip talk is faster than between-chip talk, which makes one multicore chip better than several single-core chips.
- multicore power consumption ::@:: One chip with several cores uses much less power than several single-core chips.
- why multicore power matters ::@:: Lower power use matters for battery-powered devices: phones and laptops.
- multicore cache topology ::@:: Each core on the chip keeps its own registers and its own L1 cache. The cores share one L2 cache, which sits between them and main memory.

### non-uniform memory access

Adding CPUs to a multiprocessor system may not scale, because contention for the system bus can become a bottleneck. One alternative gives each CPU, or group of CPUs, its own local memory reached through a small, fast local bus. The CPUs are then joined by a shared interconnect while still sharing one physical address space. This is non-uniform memory access, or NUMA.

A CPU reaches its own local memory over a fast local bus, but reaches another CPU's memory across the shared interconnect, so access times are not uniform. The drawback is the added latency of remote access, which has implications for scheduling and memory management.

---

Flashcards for this section are as follows:

- non-uniform memory access ::@:: Each central processing unit (CPU), or group of CPUs, has its own local memory, reached over a small, fast local bus. A shared interconnect joins the CPUs, which share one address space.
- why non-uniform memory access (NUMA) is used ::@:: Adding more CPUs to a multiprocessor system may not scale because of contention for the system bus, which can become a bottleneck.
- why NUMA access times are not uniform ::@:: In non-uniform memory access (NUMA), a processor reaches its own local memory over a small, fast local bus. It reaches remote memory across the shared system interconnect. The two kinds of access differ in speed.
- non-uniform memory access (NUMA) local memory ::@:: Local memory per central processing unit (CPU), or per group of CPUs, reached through a small, fast local bus.
- non-uniform memory access (NUMA) drawback ::@:: Access to remote memory across the system interconnect has higher latency. That latency affects processor scheduling and memory management.

## cpu, processor, and core terminology

The terms nest. A CPU is the hardware that executes instructions. A processor is a chip holding one or more CPUs. A core is the basic computation unit of a CPU, the part that executes instructions and holds registers for local data. Multicore means several cores on one chip; a multiprocessor system contains several processors.

---

Flashcards for this section are as follows:

- terminology: central processing unit (CPU) ::@:: The hardware that executes instructions.
- terminology: processor ::@:: A physical chip that contains one or more central processing units (CPUs).
- terminology: core ::@:: The basic computation unit of the central processing unit (CPU), executing instructions and holding registers for storing data locally.
- terminology: multicore ::@:: Multiple computing cores on a single physical processor chip.
- terminology: multiprocessor system ::@:: A system including multiple processors.
