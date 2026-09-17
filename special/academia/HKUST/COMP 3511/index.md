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

The published learning outcomes are to define the fundamental principles, strategies, and algorithms used in the design and implementation of operating systems; analyze and evaluate operating system functions; understand the basic structure of an operating system kernel and identify the relationship between its subsystems; identify the typical events, alerts, and symptoms that indicate potential operating system problems; and design and implement programs for basic operating system functions and algorithms.

This note records the `L1` lecture and `LA3` lab schedule, which are the sections taken by the maintainer of this note.

The content is in teaching order.

## children

- [cache (computing)](cache%20(computing).md)
- [cloud computing](cloud%20computing.md)
- [memory hierarchy](memory%20hierarchy.md)
- [multiprocessing](multiprocessing.md)
- [operating system](operating%20system.md)
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
    - overview and system architecture
        - [operating system](operating%20system.md)
        - [von Neumann architecture](von%20Neumann%20architecture.md)
    - memory and storage
        - [cache (computing)](cache%20(computing).md)
        - [memory hierarchy](memory%20hierarchy.md)
    - architecture and services
        - [cloud computing](cloud%20computing.md)
        - [multiprocessing](multiprocessing.md)
        - [virtualization](virtualization.md)
- notes
    - There are 9 labs in total, and the schedule given above is tentative and subject to lecture progress.

## week 1 lecture

- datetime: 2026-09-01T09:00:00+08:00/2026-09-01T10:20:00+08:00
- venue: Rm 4619, Lift 31-32
- topic: basic operating system concepts; computer-system organization
- [operating system](operating%20system.md)
    - [§ what an operating system does](operating%20system.md#what%20an%20operating%20system%20does)
    - [§ kernel and system programs](operating%20system.md#kernel%20and%20system%20programs)
    - [§ operating system environments](operating%20system.md#operating%20system%20environments)
    - [§ multiprogramming and time sharing](operating%20system.md#multiprogramming%20and%20time%20sharing)
- [von Neumann architecture](von%20Neumann%20architecture.md)
    - [§ computer system organization](von%20Neumann%20architecture.md#computer%20system%20organization)
    - [§ instruction execution cycle](von%20Neumann%20architecture.md#instruction%20execution%20cycle)
    - [§ input and output subsystem](von%20Neumann%20architecture.md#input%20and%20output%20subsystem)
    - [§ storage units and notation](von%20Neumann%20architecture.md#storage%20units%20and%20notation)
- [memory hierarchy](memory%20hierarchy.md)
    - [§ hierarchy of storage](memory%20hierarchy.md#hierarchy%20of%20storage)
    - [§ main memory](memory%20hierarchy.md#main%20memory)
    - [§ secondary storage](memory%20hierarchy.md#secondary%20storage)
    - [§ storage characteristics and access times](memory%20hierarchy.md#storage%20characteristics%20and%20access%20times)
- [cache (computing)](cache%20(computing).md)
    - [§ caching](cache%20(computing).md#caching)
    - [§ locality of reference](cache%20(computing).md#locality%20of%20reference)

## week 1 lecture 2

- datetime: 2026-09-03T09:00:00+08:00/2026-09-03T10:20:00+08:00
- venue: Rm 4619, Lift 31-32
- topic: computer-system architecture; virtualization; computing environments
- [multiprocessing](multiprocessing.md)
    - [§ single-processor systems](multiprocessing.md#single-processor%20systems)
    - [§ multiprocessor systems](multiprocessing.md#multiprocessor%20systems)
    - [§ symmetric multiprocessing](multiprocessing.md#symmetric%20multiprocessing)
    - [§ multicore systems](multiprocessing.md#multicore%20systems)
    - [§ non-uniform memory access](multiprocessing.md#non-uniform%20memory%20access)
    - [§ cpu, processor, and core terminology](multiprocessing.md#cpu,%20processor,%20and%20core%20terminology)
- [virtualization](virtualization.md)
    - [§ virtual machines and the hypervisor](virtualization.md#virtual%20machines%20and%20the%20hypervisor)
    - [§ system models](virtualization.md#system%20models)
    - [§ motivations for virtualization](virtualization.md#motivations%20for%20virtualization)
    - [§ history and adoption](virtualization.md#history%20and%20adoption)
- [cloud computing](cloud%20computing.md)
    - [§ deployment models](cloud%20computing.md#deployment%20models)
    - [§ service models](cloud%20computing.md#service%20models)

## midterm examination

- datetime: 2026-10-29T19:00:00+08:00/2026-10-29T21:00:00+08:00
- venue: \[missing\]
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
- note: \[missing\]
- report: \[missing\]

---

> __Announcements__
>
> __Midterm Exam Schedule (07-Sep-2026).__ Date: __29-Oct-2026 (Thu)__, Time: __07:00PM - 09:00PM__, Venues: TBA. Please mark the schedule on your calendar. Please inform the course instructor ASAP if you have time conflict with other midterm exams.
>
> __Classroom Changes (16-Sep-2026, effective 21-Sep-2026).__ COMP3511 L2: LTB => CYTG002. COMP3511 LA1: LTB => Room 2407.

## final examination

- datetime: \[missing\]
- venue: \[missing\]
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
- note: \[missing\]
- report: \[missing\]
