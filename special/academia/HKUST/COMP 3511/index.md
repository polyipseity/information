---
aliases:
  - COMP 3511
  - COMP 3511 index
  - COMP3511
  - COMP3511 index
  - HKUST COMP 3511
  - HKUST COMP 3511 index
  - HKUST COMP3511
  - HKUST COMP3511 index
  - Operating Systems
  - Operating Systems index
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/index
  - function/index
  - language/in/English
---

# index

- HKUST COMP 3511
- name: Operating Systems
- credits: 3

---

This is an introductory course on operating systems. The topics will include the basic concepts of operating systems, process and threads, inter-process communications, process synchronization, scheduling, memory allocation, page and segmentation, secondary storage, I/O systems, file systems, and protection. It contains the key concepts as well as examples drawn from a variety of real systems such as Microsoft Windows and Linux.

Prerequisites: COMP 2611, ELEC 2300, or ELEC 2350 for computer organization, covering the von Neumann machine, the CPU, pipelining, caching, the memory hierarchy, I/O systems, interrupts, and storage and hard drives, and COMP 2011 or COMP 2012H for C programming. Basic UNIX/Linux knowledge and the ability to program in C are assumed.

Textbook: _Operating System Concepts_, 10th Edition, Abraham Silberschatz, Peter B. Galvin, Greg Gagne, John Wiley & Sons Ltd, April 2018, ISBN: 978-1-118-09375-7.

Reference: _Operating Systems: Three Easy Pieces_, Remzi Arpaci-Dusseau & Andrea Arpaci-Dusseau, ISBN: 978-1-985-08659-3; the book is [freely available online](http://pages.cs.wisc.edu/~remzi/OSTEP/#book-chapters).

Canvas: [COMP3511 Canvas](https://canvas.ust.hk/courses/71995)

Course website: [COMP3511 course website](https://course.cse.ust.hk/comp3511/)

The published learning outcomes are:

- define the fundamental principles, strategies, and algorithms used in the design and implementation of operating systems
- analyze and evaluate operating system functions
- understand the basic structure of an operating system kernel and identify the relationship between its subsystems
- identify the typical events, alerts, and symptoms that indicate potential operating system problems
- design and implement programs for basic operating system functions and algorithms

This note records the `L1` lecture and `LA3` lab schedule, which are the sections taken by the maintainer of this note.

The content is in teaching order.

## children

- [labs/](labs/index.md)
- [AGENTS](AGENTS.md)
- [cache (computing)](cache%20(computing).md)
- [cloud computing](cloud%20computing.md)
- [computer multitasking](computer%20multitasking.md)
- [computing environments](computing%20environments.md)
- [deadlock (computer science)](deadlock%20(computer%20science).md)
- [inter-process communication](inter-process%20communication.md)
- [loadable kernel module](loadable%20kernel%20module.md)
- [memory hierarchy](memory%20hierarchy.md)
- [microkernel](microkernel.md)
- [monolithic kernel](monolithic%20kernel.md)
- [multilevel feedback queue](multilevel%20feedback%20queue.md)
- [multiprocessing](multiprocessing.md)
- [named pipe](named%20pipe.md)
- [operating system](operating%20system.md)
- [process (computing)](process%20(computing).md)
- [producer–consumer problem](producer–consumer%20problem.md)
- [pthreads](pthreads.md)
- [readers–writers problem](readers–writers%20problem.md)
- [scheduling (computing)](scheduling%20(computing).md)
- [semaphore (programming)](semaphore%20(programming).md)
- [synchronization (computer science)](synchronization%20(computer%20science).md)
- [system call](system%20call.md)
- [thread (computing)](thread%20(computing).md)
- [units of information](units%20of%20information.md)
- [virtualization](virtualization.md)
- [von Neumann architecture](von%20Neumann%20architecture.md)

## logistics

- grading
    - homework ×4: 20%; written assignments worth 5% each; homework 1 in weeks 3–5, homework 2 in weeks 5–7, homework 3 in weeks 8–10, homework 4 in weeks 11–13
    - projects ×3: 30%; individual programming assignments worth 10% each; project 1 in weeks 4–6, project 2 in weeks 7–9, project 3 in weeks 11–13
    - midterm examination: 20%; week 9
    - final examination: 30%
- sections:
    - lecture: L1
        - L1: Rm 4619, Lift 31-32; TuesdayT09:00:00/TuesdayT10:20:00, ThursdayT09:00:00/ThursdayT10:20:00
        - L2: Lecture Theater B until 02-Oct-2026, then LG6102, Teaching Hub from 05-Oct-2026; MondayT13:30:00/MondayT14:50:00, FridayT09:00:00/FridayT10:20:00
        - L3: G010, CYT Bldg; TuesdayT15:00:00/TuesdayT16:20:00, ThursdayT15:00:00/ThursdayT16:20:00
    - labs: LA3
        - LA1: Lecture Theater B until 24-Sep-2026, then LG6101, Teaching Hub from 08-Oct-2026; ThursdayT18:00:00/ThursdayT19:50:00
        - LA2: G010, CYT Bldg; TuesdayT18:00:00/TuesdayT19:50:00
        - LA3: Lecture Theater E; MondayT18:00:00/MondayT19:50:00
- note: The venue information for L2 and LA1 differs between the two available sources. The course announcement of 16-Sep-2026 reports that L2 moves to CYTG002 and LA1 to Room 2407 from 21-Sep-2026, while the lecture slides report that L2 moves to LG6102 from 05-Oct-2026 and LA1 to LG6101 from 08-Oct-2026. Both readings are recorded here until the course confirms one of them.
- note: Written and programming assignments are due at the specified time. Late work loses 10% and only one day of delay is allowed.
- note: All examinations are open-book and open-notes for hard copies only, and electronic devices are not allowed. No make-up examination is given unless there are special circumstances such as sickness with letters of proof, and the instructor must be informed before the examination.
- note: Labs and tutorials cover the Unix environment, the `vim` editor, compiling and running programs, and `Makefile`, basic C and C++ programming, the programming assignments, C programming APIs and interfaces, and supplementary examples and exercises. Lecture notes are released before the lectures, and each chapter has a comprehensive summary.
- note: Programming assignments run on the CS Lab 2 Linux machines and are submitted through Canvas.

## overview

- official course outline
    - overview, 4 lectures: basic operating system concepts for 2 lectures; system architecture for 2 lectures
    - process and thread, 12 lectures: process and thread for 4 lectures; CPU scheduling for 4 lectures; synchronization and synchronization examples for 2 lectures; deadlock for 2 lectures
    - memory and storage, 8 lectures: memory management for 2 lectures; virtual memory for 3 lectures; secondary storage for 1 lecture; file systems and implementation for 2 lectures
    - protection, 1 lecture
    - security, 1 lecture, optional
- course coverage
    - overview: a high-level description of operating systems and the basic components of computer systems, including multiprocessor and parallel systems, and virtualization
    - operating system structures: the services an operating system provides, including APIs and system calls, and the common design approaches of monolithic, layered, microkernel, and modular kernels
    - process: the process concept that captures a program execution, creating and terminating a process, and process communication
    - thread: the thread concept and the multithreaded process for concurrent execution of a program
    - CPU scheduling: the common CPU scheduling algorithms including real-time scheduling, and the issues associated with multiprocessor scheduling and thread scheduling
    - synchronization: the critical-section problem, hardware and software synchronization tools, and synchronization examples
    - deadlock: deadlock characterization, the resource-allocation graph, and deadlock prevention, avoidance, and detection algorithms
    - memory management: contiguous memory allocation, segmentation, and paging including hierarchical paging
    - virtual memory: virtual versus physical memory, demand paging, page-replacement algorithms, thrashing, and frame allocation
    - secondary storage: hard drives, disk structure, disk-scheduling algorithms, and RAID
    - file systems and implementation
    - protection
    - security, optional
- lab schedule
    - week 1: no lab
    - week 2, 07, 08, and 10 Sep: lab 1, introduction to the lab environment
    - week 3, 14, 15, and 17 Sep: lab 2, C and C++ programming in Linux
    - week 4, 21, 22, and 24 Sep: lab 3, lecture review and Linux system programming, and the introduction of project 1
    - week 5: no lab; the sessions of 28, 29 Sep and 1 Oct are dropped because of a holiday
    - week 6, 05, 06, and 08 Oct: lab 4, named pipes and the Pthread library
    - week 7, 12, 13, and 15 Oct: lab 5, CPU scheduling review, and the introduction of project 2
    - weeks 8–9, 20, 22, and 26 Oct: lab 6, synchronization and deadlock; the 19 Oct session is dropped because of a holiday
    - week 9, 29 Oct: midterm examination
    - week 10, 02, 03, and 05 Nov: lab 7, deadlock continued and memory management
    - week 11, 09, 10, and 12 Nov: lab 8, memory management continued, and the introduction of project 3
    - week 12: no lab; buffer week
    - week 13, 23, 24, and 26 Nov: lab 9, virtual memory management continued, mass-storage systems, and file systems
- topic-to-file mapping
    - operating system foundations
        - [computer multitasking](computer%20multitasking.md)
        - [computing environments](computing%20environments.md)
        - [operating system](operating%20system.md)
    - machine organization
        - [cache (computing)](cache%20(computing).md)
        - [memory hierarchy](memory%20hierarchy.md)
        - [units of information](units%20of%20information.md)
        - [von Neumann architecture](von%20Neumann%20architecture.md)
    - operating system structures
        - [loadable kernel module](loadable%20kernel%20module.md)
        - [microkernel](microkernel.md)
        - [monolithic kernel](monolithic%20kernel.md)
        - [system call](system%20call.md)
    - processes and threads
        - [inter-process communication](inter-process%20communication.md)
        - [named pipe](named%20pipe.md)
        - [process (computing)](process%20(computing).md)
        - [pthreads](pthreads.md)
        - [thread (computing)](thread%20(computing).md)
    - CPU scheduling
        - [multilevel feedback queue](multilevel%20feedback%20queue.md)
        - [scheduling (computing)](scheduling%20(computing).md)
    - synchronization
        - [producer–consumer problem](producer–consumer%20problem.md)
        - [readers–writers problem](readers–writers%20problem.md)
        - [semaphore (programming)](semaphore%20(programming).md)
        - [synchronization (computer science)](synchronization%20(computer%20science).md)
    - deadlock
        - [deadlock (computer science)](deadlock%20(computer%20science).md)
    - parallelism
        - [multiprocessing](multiprocessing.md)
    - virtualized infrastructure
        - [cloud computing](cloud%20computing.md)
        - [virtualization](virtualization.md)
- notes
    - There are 9 labs in total, and the schedule given above is tentative and subject to lecture progress.

## week 1 lecture 1

- datetime: 2026-09-01T09:00:00+08:00/2026-09-01T10:20:00+08:00
- venue: Rm 4619, Lift 31-32
- topic: basic operating system concepts; computer-system organization
- [operating system](operating%20system.md)
    - [§ roles and goals](operating%20system.md#roles%20and%20goals)
    - [§ composition](operating%20system.md#composition)
        - [§ kernel and system programs](operating%20system.md#kernel%20and%20system%20programs)
- [computer multitasking](computer%20multitasking.md)
    - [§ multiprogramming](computer%20multitasking.md#multiprogramming)
    - [§ time sharing](computer%20multitasking.md#time%20sharing)
- [von Neumann architecture](von%20Neumann%20architecture.md)
    - [§ computer system organization](von%20Neumann%20architecture.md#computer%20system%20organization)
    - [§ instruction execution cycle](von%20Neumann%20architecture.md#instruction%20execution%20cycle)
        - [§ processor registers](von%20Neumann%20architecture.md#processor%20registers)
        - [§ interrupts](von%20Neumann%20architecture.md#interrupts)
    - [§ input and output subsystem](von%20Neumann%20architecture.md#input%20and%20output%20subsystem)
        - [§ device drivers and kernel services](von%20Neumann%20architecture.md#device%20drivers%20and%20kernel%20services)
        - [§ programmed I/O and direct memory access](von%20Neumann%20architecture.md#programmed%20I/O%20and%20direct%20memory%20access)
- [memory hierarchy](memory%20hierarchy.md)
    - [§ primary, secondary, and tertiary storage](memory%20hierarchy.md#primary,%20secondary,%20and%20tertiary%20storage)
    - [§ main memory](memory%20hierarchy.md#main%20memory)
    - [§ secondary storage](memory%20hierarchy.md#secondary%20storage)
    - [§ storage characteristics and access times](memory%20hierarchy.md#storage%20characteristics%20and%20access%20times)
- [cache (computing)](cache%20(computing).md)
    - [§ cache management and performance](cache%20(computing).md#cache%20management%20and%20performance)
    - [§ locality of reference](cache%20(computing).md#locality%20of%20reference)
- [units of information](units%20of%20information.md)
    - [§ binary and decimal prefixes](units%20of%20information.md#binary%20and%20decimal%20prefixes)

## week 1 lecture 2

- datetime: 2026-09-03T09:00:00+08:00/2026-09-03T10:20:00+08:00
- venue: Rm 4619, Lift 31-32
- topic: computer-system architecture; virtualization; computing environments
- [multiprocessing](multiprocessing.md)
    - [§ single-processor systems](multiprocessing.md#single-processor%20systems)
    - [§ multiprocessor systems](multiprocessing.md#multiprocessor%20systems)
        - [§ asymmetric multiprocessing](multiprocessing.md#asymmetric%20multiprocessing)
        - [§ symmetric multiprocessing](multiprocessing.md#symmetric%20multiprocessing)
        - [§ multicore systems](multiprocessing.md#multicore%20systems)
        - [§ non-uniform memory access](multiprocessing.md#non-uniform%20memory%20access)
    - [§ cpu, processor, and core terminology](multiprocessing.md#cpu,%20processor,%20and%20core%20terminology)
- [virtualization](virtualization.md)
    - [§ virtual machines and the hypervisor](virtualization.md#virtual%20machines%20and%20the%20hypervisor)
    - [§ system models](virtualization.md#system%20models)
    - [§ machine switch](virtualization.md#machine%20switch)
        - [§ without virtualization](virtualization.md#without%20virtualization)
        - [§ with virtualization](virtualization.md#with%20virtualization)
    - [§ motivations for virtualization](virtualization.md#motivations%20for%20virtualization)
    - [§ history and adoption](virtualization.md#history%20and%20adoption)
- [cloud computing](cloud%20computing.md)
    - [§ deployment models](cloud%20computing.md#deployment%20models)
    - [§ service models](cloud%20computing.md#service%20models)
- [computing environments](computing%20environments.md)

## week 2 lab 1

- datetime: 2026-09-07T18:00:00+08:00/2026-09-07T19:50:00+08:00
- venue: Lecture Theater E
- status: no class

---

> __No Labs on Week 1__
>
> We don't have labs on week 1 (i.e., 01-04 Sep 2026).
>
> We don't have labs on week 2 (i.e., 07-11 Sep 2026).
>
> Lab1+2 will be combined on week 3 (i.e., 14,15,17 Sep 2026) after the add/drop period.

## week 2 lecture 1

- datetime: 2026-09-08T09:00:00+08:00/2026-09-08T10:20:00+08:00
- venue: Rm 4619, Lift 31-32
- topic: operating system services; user interfaces; system calls; system programs; linkers and loaders
- [operating system](operating%20system.md)
    - [§ composition](operating%20system.md#composition)
        - [§ system programs](operating%20system.md#system%20programs)
        - [§ linkers and loaders](operating%20system.md#linkers%20and%20loaders)
    - [§ modes and protection](operating%20system.md#modes%20and%20protection)
    - [§ services](operating%20system.md#services)
        - [§ user interfaces](operating%20system.md#user%20interfaces)
- [system call](system%20call.md)
    - [§ API (Application Program Interface)](system%20call.md#API%20(Application%20Program%20Interface))
        - [§ system calls behind a file copy](system%20call.md#system%20calls%20behind%20a%20file%20copy)
        - [§ flags of open()](system%20call.md#flags%20of%20open())
        - [§ permission bits](system%20call.md#permission%20bits)
    - [§ system call interface](system%20call.md#system%20call%20interface)
    - [§ mode transfer](system%20call.md#mode%20transfer)
        - [§ walkthrough of a read()](system%20call.md#walkthrough%20of%20a%20read())
    - [§ parameter passing](system%20call.md#parameter%20passing)
    - [§ categories](system%20call.md#categories)

## week 2 lecture 2

- datetime: 2026-09-10T09:00:00+08:00/2026-09-10T10:20:00+08:00
- venue: Rm 4619, Lift 31-32
- topic: OS design and implementation; operating system structures
- [operating system](operating%20system.md)
    - [§ design](operating%20system.md#design)
        - [§ design goals](operating%20system.md#design%20goals)
        - [§ structure](operating%20system.md#structure)
- [monolithic kernel](monolithic%20kernel.md)
    - [§ original UNIX structure](monolithic%20kernel.md#original%20UNIX%20structure)
    - [§ Linux system structure](monolithic%20kernel.md#Linux%20system%20structure)
- [microkernel](microkernel.md)
    - [§ inter-process communication](microkernel.md#inter-process%20communication)
    - [§ advantages](microkernel.md#advantages)
    - [§ drawbacks](microkernel.md#drawbacks)
    - [§ Mach and Darwin](microkernel.md#Mach%20and%20Darwin)
- [loadable kernel module](loadable%20kernel%20module.md)
    - [§ design](loadable%20kernel%20module.md#design)
    - [§ Linux and LKMs](loadable%20kernel%20module.md#Linux%20and%20LKMs)

## week 3 lab 1

- datetime: 2026-09-14T18:00:00+08:00/2026-09-14T19:50:00+08:00
- venue: Lecture Theater E
- topic: the lab environment and C programming in Linux
- [lab 1](labs/lab%201/index.md)
- [lab 2](labs/lab%202/index.md)

## week 3 lecture 1

- datetime: 2026-09-15T09:00:00+08:00/2026-09-15T10:20:00+08:00
- venue: Rm 4619, Lift 31-32
- topic: the process concept; process memory layout; process state; process control block; context switching
- [process (computing)](process%20(computing).md)
    - [§ process memory layout](process%20(computing).md#process%20memory%20layout)
    - [§ process control block](process%20(computing).md#process%20control%20block)
    - [§ process states and queues](process%20(computing).md#process%20states%20and%20queues)
        - [§ state transitions](process%20(computing).md#state%20transitions)
        - [§ ready queue and device queues](process%20(computing).md#ready%20queue%20and%20device%20queues)
    - [§ context switch](process%20(computing).md#context%20switch)

## week 3 lecture 2

- datetime: 2026-09-17T09:00:00+08:00/2026-09-17T10:20:00+08:00
- venue: Rm 4619, Lift 31-32
- topic: process creation and termination; inter-process communication; shared memory; message passing
- [process (computing)](process%20(computing).md)
    - [§ process creation](process%20(computing).md#process%20creation)
        - [§ fork() return values](process%20(computing).md#fork()%20return%20values)
        - [§ exec() and the program image](process%20(computing).md#exec()%20and%20the%20program%20image)
    - [§ process termination](process%20(computing).md#process%20termination)
        - [§ wait() and the exit status](process%20(computing).md#wait()%20and%20the%20exit%20status)
        - [§ decoding the exit status](process%20(computing).md#decoding%20the%20exit%20status)
        - [§ zombie process](process%20(computing).md#zombie%20process)
        - [§ orphan process](process%20(computing).md#orphan%20process)
- [inter-process communication](inter-process%20communication.md)
    - [§ cooperation between processes](inter-process%20communication.md#cooperation%20between%20processes)
    - [§ shared memory](inter-process%20communication.md#shared%20memory)
    - [§ message passing](inter-process%20communication.md#message%20passing)
        - [§ direct and indirect communication](inter-process%20communication.md#direct%20and%20indirect%20communication)
        - [§ synchronous and asynchronous communication](inter-process%20communication.md#synchronous%20and%20asynchronous%20communication)
        - [§ buffering capacity](inter-process%20communication.md#buffering%20capacity)

## week 4 lab 1

- datetime: 2026-09-21T18:00:00+08:00/2026-09-21T19:50:00+08:00
- venue: Lecture Theater E
- topic: lecture review and Linux system programming; the introduction of project 1
- [lab 3](labs/lab%203/index.md)

## week 4 lecture 1

- datetime: 2026-09-22T09:00:00+08:00/2026-09-22T10:20:00+08:00
- venue: Rm 4619, Lift 31-32
- topic: pipes; client-server communication; the thread concept
- [inter-process communication](inter-process%20communication.md)
    - [§ ordinary pipe](inter-process%20communication.md#ordinary%20pipe)
        - [§ pipe() descriptors](inter-process%20communication.md#pipe()%20descriptors)
    - [§ named pipe](inter-process%20communication.md#named%20pipe)
    - [§ client-server communication](inter-process%20communication.md#client-server%20communication)
        - [§ socket](inter-process%20communication.md#socket)
        - [§ remote procedure call](inter-process%20communication.md#remote%20procedure%20call)
- [named pipe](named%20pipe.md)
    - [§ creating a named pipe](named%20pipe.md#creating%20a%20named%20pipe)
    - [§ blocking open](named%20pipe.md#blocking%20open)
    - [§ reading and writing](named%20pipe.md#reading%20and%20writing)
    - [§ several writers](named%20pipe.md#several%20writers)
        - [§ atomic writes and PIPE_BUF](named%20pipe.md#atomic%20writes%20and%20PIPE_BUF)
    - [§ placement and permissions](named%20pipe.md#placement%20and%20permissions)
- [thread (computing)](thread%20(computing).md)
    - [§ thread components](thread%20(computing).md#thread%20components)
    - [§ benefits of multithreading](thread%20(computing).md#benefits%20of%20multithreading)

## week 4 lecture 2

- datetime: 2026-09-24T09:00:00+08:00/2026-09-24T10:20:00+08:00
- venue: Rm 4619, Lift 31-32
- topic: multicore programming; user and kernel threads; multithreading models; threading issues
- [thread (computing)](thread%20(computing).md)
    - [§ concurrency and parallelism](thread%20(computing).md#concurrency%20and%20parallelism)
    - [§ multicore programming](thread%20(computing).md#multicore%20programming)
        - [§ design challenges](thread%20(computing).md#design%20challenges)
        - [§ data and task parallelism](thread%20(computing).md#data%20and%20task%20parallelism)
    - [§ user threads and kernel threads](thread%20(computing).md#user%20threads%20and%20kernel%20threads)
    - [§ multithreading models](thread%20(computing).md#multithreading%20models)
        - [§ many-to-one model](thread%20(computing).md#many-to-one%20model)
        - [§ one-to-one model](thread%20(computing).md#one-to-one%20model)
        - [§ many-to-many model](thread%20(computing).md#many-to-many%20model)
        - [§ two-level model](thread%20(computing).md#two-level%20model)
        - [§ lightweight process](thread%20(computing).md#lightweight%20process)
    - [§ threading issues](thread%20(computing).md#threading%20issues)
        - [§ fork() and exec() in a multithreaded process](thread%20(computing).md#fork()%20and%20exec()%20in%20a%20multithreaded%20process)
        - [§ signals and their default actions](thread%20(computing).md#signals%20and%20their%20default%20actions)
        - [§ signal delivery in a multithreaded process](thread%20(computing).md#signal%20delivery%20in%20a%20multithreaded%20process)
        - [§ thread cancellation](thread%20(computing).md#thread%20cancellation)
- [pthreads](pthreads.md)
    - [§ thread handles and creation](pthreads.md#thread%20handles%20and%20creation)
        - [§ void pointer argument](pthreads.md#void%20pointer%20argument)
    - [§ joining and ending a thread](pthreads.md#joining%20and%20ending%20a%20thread)
        - [§ return values](pthreads.md#return%20values)
    - [§ synchronization](pthreads.md#synchronization)
        - [§ mutex](pthreads.md#mutex)
        - [§ condition variable](pthreads.md#condition%20variable)
        - [§ signal and broadcast](pthreads.md#signal%20and%20broadcast)
    - [§ practices](pthreads.md#practices)
        - [§ mutex practice](pthreads.md#mutex%20practice)
        - [§ condition practice](pthreads.md#condition%20practice)
    - [§ building and linking](pthreads.md#building%20and%20linking)

## week 5 lab 1

- datetime: 2026-09-28T18:00:00+08:00/2026-09-28T19:50:00+08:00
- venue: Lecture Theater E
- status: no class

## week 5 lecture 1

- datetime: 2026-09-29T09:00:00+08:00/2026-09-29T10:20:00+08:00
- venue: Rm 4619, Lift 31-32
- topic: basic concepts of CPU scheduling; scheduling criteria; the dispatcher; preemptive and non-preemptive scheduling
- [scheduling (computing)](scheduling%20(computing).md)
    - [§ scheduling basics](scheduling%20(computing).md#scheduling%20basics)
        - [§ CPU and I/O bursts](scheduling%20(computing).md#CPU%20and%20I/O%20bursts)
        - [§ scheduling criteria](scheduling%20(computing).md#scheduling%20criteria)
        - [§ dispatcher and dispatch latency](scheduling%20(computing).md#dispatcher%20and%20dispatch%20latency)
        - [§ preemptive and non-preemptive scheduling](scheduling%20(computing).md#preemptive%20and%20non-preemptive%20scheduling)
        - [§ long-term, medium-term and short-term schedulers](scheduling%20(computing).md#long-term,%20medium-term%20and%20short-term%20schedulers)

## week 5 lecture 2

- datetime: 2026-10-01T09:00:00+08:00/2026-10-01T10:20:00+08:00
- venue: Rm 4619, Lift 31-32
- status: public holiday: National Day

## week 6 lab 1

- datetime: 2026-10-05T18:00:00+08:00/2026-10-05T19:50:00+08:00
- venue: Lecture Theater E
- topic: named pipes and the Pthread library
- [lab 4](labs/lab%204/index.md)

## week 6 lecture 1

- datetime: 2026-10-06T09:00:00+08:00/2026-10-06T10:20:00+08:00
- venue: Rm 4619, Lift 31-32
- topic: first-come first-served; shortest job first; shortest remaining time first; round robin; priority; multilevel queue
- [scheduling (computing)](scheduling%20(computing).md)
    - [§ scheduling algorithms](scheduling%20(computing).md#scheduling%20algorithms)
        - [§ first-come, first-served scheduling](scheduling%20(computing).md#first-come,%20first-served%20scheduling)
        - [§ shortest job first scheduling](scheduling%20(computing).md#shortest%20job%20first%20scheduling)
        - [§ shortest remaining time first scheduling](scheduling%20(computing).md#shortest%20remaining%20time%20first%20scheduling)
        - [§ round-robin scheduling](scheduling%20(computing).md#round-robin%20scheduling)
        - [§ priority scheduling](scheduling%20(computing).md#priority%20scheduling)
    - [§ queue-based scheduling](scheduling%20(computing).md#queue-based%20scheduling)
        - [§ multilevel queue scheduling](scheduling%20(computing).md#multilevel%20queue%20scheduling)

## week 6 lecture 2

- datetime: 2026-10-08T09:00:00+08:00/2026-10-08T10:20:00+08:00
- venue: Rm 4619, Lift 31-32
- topic: multilevel feedback queue; thread and multiprocessor scheduling; real-time scheduling; algorithm evaluation
- [multilevel feedback queue](multilevel%20feedback%20queue.md)
    - [§ queue structure and parameters](multilevel%20feedback%20queue.md#queue%20structure%20and%20parameters)
    - [§ three-queue trace](multilevel%20feedback%20queue.md#three-queue%20trace)
    - [§ starvation and aging](multilevel%20feedback%20queue.md#starvation%20and%20aging)
- [scheduling (computing)](scheduling%20(computing).md)
    - [§ scheduling algorithms](scheduling%20(computing).md#scheduling%20algorithms)
        - [§ next CPU burst estimation](scheduling%20(computing).md#next%20CPU%20burst%20estimation)
    - [§ queue-based scheduling](scheduling%20(computing).md#queue-based%20scheduling)
        - [§ multilevel feedback queue scheduling](scheduling%20(computing).md#multilevel%20feedback%20queue%20scheduling)
    - [§ thread and multiprocessor scheduling](scheduling%20(computing).md#thread%20and%20multiprocessor%20scheduling)
        - [§ process-contention scope and system-contention scope](scheduling%20(computing).md#process-contention%20scope%20and%20system-contention%20scope)
        - [§ symmetric and asymmetric multiprocessing scheduling](scheduling%20(computing).md#symmetric%20and%20asymmetric%20multiprocessing%20scheduling)
        - [§ load balancing and processor affinity](scheduling%20(computing).md#load%20balancing%20and%20processor%20affinity)
        - [§ multicore scheduling](scheduling%20(computing).md#multicore%20scheduling)
    - [§ real-time scheduling](scheduling%20(computing).md#real-time%20scheduling)
        - [§ rate-monotonic scheduling](scheduling%20(computing).md#rate-monotonic%20scheduling)
        - [§ earliest deadline first](scheduling%20(computing).md#earliest%20deadline%20first)
    - [§ starvation and fairness](scheduling%20(computing).md#starvation%20and%20fairness)
        - [§ starvation by policy](scheduling%20(computing).md#starvation%20by%20policy)
    - [§ algorithm evaluation](scheduling%20(computing).md#algorithm%20evaluation)

## week 7 lab 1

- datetime: 2026-10-12T18:00:00+08:00/2026-10-12T19:50:00+08:00
- venue: Lecture Theater E
- topic: CPU scheduling review; the multilevel feedback queue project
- [lab 5](labs/lab%205/index.md)

## week 7 lecture 1

- datetime: 2026-10-13T09:00:00+08:00/2026-10-13T10:20:00+08:00
- venue: Rm 4619, Lift 31-32
- topic: race conditions; the critical-section problem; Peterson's solution; synchronization hardware; mutex locks
- [synchronization (computer science)](synchronization%20(computer%20science).md)
    - [§ race conditions and the critical section](synchronization%20(computer%20science).md#race%20conditions%20and%20the%20critical%20section)
        - [§ race conditions](synchronization%20(computer%20science).md#race%20conditions)
        - [§ critical section problem](synchronization%20(computer%20science).md#critical%20section%20problem)
    - [§ software and hardware support](synchronization%20(computer%20science).md#software%20and%20hardware%20support)
        - [§ Peterson's solution](synchronization%20(computer%20science).md#Peterson's%20solution)
        - [§ test-and-set and compare-and-swap](synchronization%20(computer%20science).md#test-and-set%20and%20compare-and-swap)
        - [§ sketch proof of the bounded-waiting lock](synchronization%20(computer%20science).md#sketch%20proof%20of%20the%20bounded-waiting%20lock)
        - [§ atomic variables](synchronization%20(computer%20science).md#atomic%20variables)
    - [§ mutex locks](synchronization%20(computer%20science).md#mutex%20locks)
        - [§ adaptive mutex](synchronization%20(computer%20science).md#adaptive%20mutex)

## week 7 lecture 2

- datetime: 2026-10-15T09:00:00+08:00/2026-10-15T10:20:00+08:00
- venue: Rm 4619, Lift 31-32
- topic: semaphores; condition variables; the producer-consumer problem; synchronization examples; readers and writers
- [producer–consumer problem](producer–consumer%20problem.md)
    - [§ problem statement](producer–consumer%20problem.md#problem%20statement)
    - [§ attempt with a shared counter](producer–consumer%20problem.md#attempt%20with%20a%20shared%20counter)
    - [§ semaphore and condition-variable solutions](producer–consumer%20problem.md#semaphore%20and%20condition-variable%20solutions)
        - [§ mutex with two counting semaphores](producer–consumer%20problem.md#mutex%20with%20two%20counting%20semaphores)
        - [§ mutex with conditional waiting](producer–consumer%20problem.md#mutex%20with%20conditional%20waiting)
    - [§ unbounded buffer variant](producer–consumer%20problem.md#unbounded%20buffer%20variant)
- [readers–writers problem](readers–writers%20problem.md)
    - [§ reader and writer access rule](readers–writers%20problem.md#reader%20and%20writer%20access%20rule)
    - [§ semaphore initialisation](readers–writers%20problem.md#semaphore%20initialisation)
    - [§ reader-preference solution](readers–writers%20problem.md#reader-preference%20solution)
        - [§ count-guarded reader access](readers–writers%20problem.md#count-guarded%20reader%20access)
        - [§ data gate as writer lock](readers–writers%20problem.md#data%20gate%20as%20writer%20lock)
        - [§ starvation of writers](readers–writers%20problem.md#starvation%20of%20writers)
        - [§ comparison with the writer-preference solution](readers–writers%20problem.md#comparison%20with%20the%20writer-preference%20solution)
    - [§ writer-preference solution](readers–writers%20problem.md#writer-preference%20solution)
        - [§ gated reader access](readers–writers%20problem.md#gated%20reader%20access)
        - [§ gate shutdown by a writer](readers–writers%20problem.md#gate%20shutdown%20by%20a%20writer)
        - [§ starvation of readers](readers–writers%20problem.md#starvation%20of%20readers)
        - [§ comparison with the reader-preference solution](readers–writers%20problem.md#comparison%20with%20the%20reader-preference%20solution)
    - [§ reader-writer lock](readers–writers%20problem.md#reader-writer%20lock)
- [semaphore (programming)](semaphore%20(programming).md)
    - [§ operations](semaphore%20(programming).md#operations)
        - [§ semaphore calls](semaphore%20(programming).md#semaphore%20calls)
    - [§ semaphore kinds](semaphore%20(programming).md#semaphore%20kinds)
        - [§ binary semaphore](semaphore%20(programming).md#binary%20semaphore)
        - [§ counting semaphore](semaphore%20(programming).md#counting%20semaphore)
        - [§ ordering use](semaphore%20(programming).md#ordering%20use)
    - [§ blocking implementation](semaphore%20(programming).md#blocking%20implementation)
    - [§ implementation with test-and-set](semaphore%20(programming).md#implementation%20with%20test-and-set)
    - [§ pitfalls](semaphore%20(programming).md#pitfalls)
- [synchronization (computer science)](synchronization%20(computer%20science).md)
    - [§ semaphores](synchronization%20(computer%20science).md#semaphores)
        - [§ implementation](synchronization%20(computer%20science).md#implementation)
    - [§ condition variables](synchronization%20(computer%20science).md#condition%20variables)
        - [§ waking waiters](synchronization%20(computer%20science).md#waking%20waiters)

## week 8 lab 1

- datetime: 2026-10-19T18:00:00+08:00/2026-10-19T19:50:00+08:00
- venue: Lecture Theater E
- status: public holiday: the day following Chung Yeung Festival

## week 8 lecture 1

- datetime: 2026-10-20T09:00:00+08:00/2026-10-20T10:20:00+08:00
- venue: Rm 4619, Lift 31-32
- topic: deadlock characterization; the resource-allocation graph; deadlock prevention
- [deadlock (computer science)](deadlock%20(computer%20science).md)
    - [§ system model](deadlock%20(computer%20science).md#system%20model)
    - [§ resource-allocation graph](deadlock%20(computer%20science).md#resource-allocation%20graph)
    - [§ wait-for graph](deadlock%20(computer%20science).md#wait-for%20graph)
    - [§ prevention](deadlock%20(computer%20science).md#prevention)
        - [§ mutual exclusion](deadlock%20(computer%20science).md#mutual%20exclusion)
        - [§ hold and wait](deadlock%20(computer%20science).md#hold%20and%20wait)
        - [§ no preemption](deadlock%20(computer%20science).md#no%20preemption)
        - [§ circular wait](deadlock%20(computer%20science).md#circular%20wait)

## week 8 lecture 2

- datetime: 2026-10-22T09:00:00+08:00/2026-10-22T10:20:00+08:00
- venue: Rm 4619, Lift 31-32
- topic: deadlock avoidance; the banker's algorithm; deadlock detection and recovery from deadlock
- [deadlock (computer science)](deadlock%20(computer%20science).md)
    - [§ avoidance](deadlock%20(computer%20science).md#avoidance)
    - [§ banker's algorithm](deadlock%20(computer%20science).md#banker's%20algorithm)
        - [§ state structures](deadlock%20(computer%20science).md#state%20structures)
        - [§ safety algorithm](deadlock%20(computer%20science).md#safety%20algorithm)
        - [§ worst-case assumption](deadlock%20(computer%20science).md#worst-case%20assumption)
        - [§ resource request](deadlock%20(computer%20science).md#resource%20request)
        - [§ five-process walkthrough](deadlock%20(computer%20science).md#five-process%20walkthrough)
    - [§ detection](deadlock%20(computer%20science).md#detection)
        - [§ start state of the detection algorithm](deadlock%20(computer%20science).md#start%20state%20of%20the%20detection%20algorithm)
        - [§ comparison with the banker's algorithm](deadlock%20(computer%20science).md#comparison%20with%20the%20banker's%20algorithm)
    - [§ recovery](deadlock%20(computer%20science).md#recovery)

## week 9 lab 1

- datetime: 2026-10-26T18:00:00+08:00/2026-10-26T19:50:00+08:00
- venue: Lecture Theater E
- topic: synchronization review
- [lab 6](labs/lab%206/index.md)

## midterm examination

- datetime: 2026-10-29T20:00:00+08:00/2026-10-29T22:00:00+08:00
- venue: LTD
- scope: the material through synchronization tools
- format:
    - calculator: no
    - cheatsheet: \[missing\]
    - open book: yes
    - open notes: yes (hard copies only)
    - questions: \[missing\]
- grade: \[missing\]
- statistics: \[missing\]
- breakdown: \[missing\]
- note: The examination runs 2 hours.
- report: \[missing\]

---

> __Updated Midterm Exam Details__
>
> The midterm exam schedule:
>
> - Date: __29-Oct-2026 (Thu)__
> - Time: __08:00PM - 10:00PM__ (Note: 2 hours for the midterm exam)
>     - _Note: The university cannot find suitable venues for 7pm-9pm_
> - Venues:
>     - L1 students: LTD
>     - L2 students: LSKG012
>     - L3 students: LTB
> - Coverage: Chapters 1-6 (up to Synchronization tools)

## final examination

- datetime: 2026-12-19T12:30:00+08:00/2026-12-19T15:00:00+08:00
- venue: S H Ho Sports Hall
- scope: \[missing\]
- format:
    - calculator: no
    - cheatsheet: \[missing\]
    - open book: yes
    - open notes: yes (hard copies only)
    - questions: \[missing\]
- grade: \[missing\]
- statistics: \[missing\]
- breakdown: \[missing\]
- note: The examination runs 2.5 hours.
- report: \[missing\]

---

> __Final Exam Schedule__
>
> Note: Please do not mess up with the midterm exam schedule The university released the COMP3511 Final Exam schedule:
>
> - Date: __19-Dec-2026 (Sat)__
> - Time: __12:30PM - 03:00PM__ (Note: We only use 2.5 hours instead of 3 hours for the final exam)
> - Venue: S H Ho Sports Hall
