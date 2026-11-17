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

A traditional computer had one processor with one central processing unit (CPU) and one core. All work passed through one general-purpose unit and its registers, arithmetic-logic unit, and control unit. Modern systems spread the work over several processors, or over several cores on one chip. That changes how an operating system schedules work and manages memory.

---

Flashcards for this section are as follows:

- what multiprocessing is ::@:: Multiprocessing spreads one computer's work over more than one processor or core instead of a single processor with one core. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- what the single-processor baseline is ::@:: One processor holding one central processing unit (CPU) with a single core; most early computers worked this way. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- why multiprocessing matters to an operating system ::@:: Processors or cores share one memory and one system bus, so the operating system schedules work and manages memory across units that run at once. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- asymmetric versus symmetric multiprocessing ::@:: Asymmetric multiprocessing uses a master processor that assigns work to the others. Symmetric multiprocessing treats every processor the same. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- multicore versus multiprocessor ::@:: Multicore puts several cores on one chip. A multiprocessor system holds several processors. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->

## single-processor systems

Most early computers had one processor with one CPU and a single core. A core executes instructions and keeps local data in its registers. A general-purpose core runs a general-purpose instruction set.

A general-purpose CPU holds an arithmetic-logic unit, processor registers, and a control unit with an instruction register and a program counter. These systems also carry special-purpose processors: disk controllers, graphics controllers, and graphics processing units. Those run a narrow instruction set and usually do not execute instructions from user processes.

---

Flashcards for this section are as follows:

- single-processor system ::@:: One processor holding one central processing unit (CPU) with a single core; most early computers worked this way. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- processing core ::@:: The part of a central processing unit (CPU) that runs instructions and keeps local data in registers. A general-purpose core runs a general-purpose instruction set. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- general-purpose CPU contents ::@:: A central processing unit (CPU) holding an arithmetic-logic unit, processor registers, and a control unit with an instruction register and a program counter. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- special-purpose processors ::@:: Single-processor systems still carry device-specific processors: disk controllers, graphics controllers, and graphics processing units (GPUs). These run a narrow instruction set and usually do not run user instructions. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->

## multiprocessor systems

Multiprocessor systems are now the norm. The classic arrangement has two or more processors, each with a single-core CPU.

More processors raise throughput. Sharing input/output hardware, power supplies, housings, and peripherals gives economy of scale. Reliability improves as well, because the system keeps working when one processor fails, either by graceful degradation or by fault tolerance.

Adding processors does not scale proportionally: the speed-up with $N$ processors is less than $N$, because of overhead such as contention for the system bus or memory. Such systems are also harder to design in hardware and in software; parallel programming is one case.

Two kinds exist: asymmetric multiprocessing and symmetric multiprocessing.

---

Flashcards for this section are as follows:

- multiprocessor system ::@:: A system with two or more processors, each holding a single-core central processing unit (CPU). <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- advantages of multiprocessor systems ::@:: More processors raise throughput. Shared input/output hardware, power supplies, housings, and peripherals give economy of scale. Reliability improves, because a failed processor leaves the system running, through graceful degradation or fault tolerance. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- scaling with $N$ processors ::@:: The speed-up with $N$ processors is less than $N$, because contention for the system bus or memory adds overhead. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- complexity of multiprocessor systems ::@:: Such systems are harder to build, in hardware and in software, than single-processor ones. Parallel programming is one case. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->

### asymmetric multiprocessing

In __asymmetric multiprocessing__, often called master-slave, one master processor hands specific tasks to the slave processors and handles input/output itself. The processors are not equal.

---

Flashcards for this section are as follows:

- asymmetric multiprocessing ::@:: One master processor assigns tasks to slave processors and handles input/output itself, often called master-slave. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->

### symmetric multiprocessing

Symmetric multiprocessing, or SMP, treats every processor the same. Each CPU has its own registers and a private, or local, cache, but all processors share physical memory through the system bus. Any processor runs any task, operating-system functions and user processes alike, and any can handle input/output. None is reserved as a master, and that separates SMP from asymmetric multiprocessing.

---

Flashcards for this section are as follows:

- symmetric multiprocessing ::@:: All processors are treated the same. Each central processing unit (CPU) keeps its own registers and cache. All of them share memory through the system bus. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- what state is private to each central processing unit (CPU) in symmetric multiprocessing (SMP) ::@:: Each CPU keeps its own registers and a private local cache. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- symmetric multiprocessing (SMP) shared memory ::@:: All processors share memory through the system bus. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- symmetric multiprocessing (SMP) task and input/output handling ::@:: Every processor runs all tasks, operating-system functions and user processes alike. Any processor can handle input/output. None is reserved as a master. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- symmetric versus asymmetric multiprocessing ::@:: Symmetric multiprocessing treats all processors the same. Any of them can handle input/output. Asymmetric multiprocessing has one master central processing unit (CPU) that hands tasks to slave CPUs and usually handles input/output itself. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->

### multicore systems

A multicore design puts several cores on one chip. On-chip communication is faster than between-chip communication, so one such chip beats several single-core chips. It also draws much less power. That matters for phones and laptops, which run on battery.

Each core keeps its own registers and its own L1 cache. The cores share one L2 cache between them and main memory, so the first level is private and the next is shared.

---

Flashcards for this section are as follows:

- what a multicore design is ::@:: One chip holding several computing cores. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- on-chip versus between-chip communication ::@:: On-chip communication is faster than between-chip communication, so one multicore chip beats several single-core chips. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- multicore power consumption ::@:: One chip with several cores draws much less power than several single-core chips. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- why multicore power matters ::@:: Phones and laptops run on battery, so the lower power draw of one multicore chip matters.
- multicore cache topology ::@:: Each core keeps its own registers and its own L1 cache. The cores share one L2 cache between them and main memory. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->

### non-uniform memory access

Adding CPUs to a multiprocessor system may not scale, because contention for the system bus can bottleneck it. One alternative gives each CPU, or group of CPUs, local memory on a small, fast local bus. A shared interconnect joins them, and they still share one physical address space. This is non-uniform memory access, or NUMA.

A CPU reaches another CPU's memory across the shared interconnect, and that trip takes longer than a local one. The extra latency affects scheduling and memory management.

---

Flashcards for this section are as follows:

- non-uniform memory access ::@:: Each central processing unit (CPU), or group of CPUs, has its own local memory on a small, fast local bus. A shared interconnect joins them into one address space. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- why non-uniform memory access (NUMA) is used ::@:: Adding CPUs may not scale, because contention for the system bus becomes a bottleneck. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- why NUMA access times are not uniform ::@:: Local memory sits on a small, fast local bus. Remote memory sits across the shared interconnect, so the two accesses differ in speed. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- non-uniform memory access (NUMA) local memory ::@:: Each central processing unit (CPU), or group of CPUs, has local memory on a small, fast local bus. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- non-uniform memory access (NUMA) drawback ::@:: Reaching remote memory across the system interconnect has higher latency, which affects processor scheduling and memory management. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->

## cpu, processor, and core terminology

The terms nest. A CPU is the hardware that executes instructions. A processor is a chip holding one or more CPUs. A core is the basic computation unit of a CPU: the part that executes instructions and holds registers for local data. Multicore puts several cores on one chip, and a multiprocessor system holds several processors.

---

Flashcards for this section are as follows:

- terminology: central processing unit (CPU) ::@:: The hardware that executes instructions. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- terminology: processor ::@:: A chip holding one or more central processing units (CPUs). <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- terminology: core ::@:: The basic computation unit of a central processing unit (CPU). It runs instructions and keeps local data in registers. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- terminology: multicore ::@:: Several computing cores on one physical processor chip. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- terminology: multiprocessor system ::@:: A system holding several processors. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
