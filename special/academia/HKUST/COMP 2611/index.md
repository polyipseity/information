---
aliases:
  - COMP 2611
  - COMP 2611 index
  - COMP2611
  - COMP2611 index
  - Computer Organization
  - Computer Organization index
  - HKUST COMP 2611
  - HKUST COMP 2611 index
  - HKUST COMP2611
  - HKUST COMP2611 index
tags:
  - flashcard/active/special/academia/HKUST/COMP_2611/index
  - function/index
  - language/in/English
---

# index

- HKUST COMP 2611
- name: Computer Organization

The content is in teaching order.

- grading
  - scheme
    - individual written homework ×4: 15%
    - midterm exam: 30%
    - individual programming project: 15%
    - final exam: 40%
- logistics
  - course learning outcomes (CLOs) ::@:: assembly language, digital logic, instruction set architecture (ISA), organizational paradigms, processor & memory <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - topics ::@:: brief digital circuit, data representation and arithmetic, instruction set architecture and assembly, computer architecture <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
    1. digital logic: combinational, sequential
    2. data representation: integer, fractional, character
    3. instruction set architecture (ISA)
    4. MIPS assembly language
    5. processor: datapath, control; pipeline
    6. memory system: cache, virtual memory

## children

<!-- - [questions](questions.md) -->

## week 1 lecture

- datetime: 2025-02-03T13:30:00+08:00/2025-02-03T14:50:00+08:00
- logistics
- [numeral system](../../../../general/numeral%20system.md) ::@:: a mathematical notation for representing numbers of a given set, using digits or other symbols in a consistent manner <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - numeral system / common examples ::@:: binary (base 2; used by digital computers), octal (base 8), decimal (base 10; used by people), hexadecimal (base 16; concisely expresses a binary sequence), sexagesimal (base 60; used for timekeeping) <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
- [positional notation](../../../../general/positional%20notation.md) ::@:: (_d_<sub>_n_<!-- markdown separator -->−1</sub>..._d_<sub>0</sub>)<sub>_r_</sub> = _d_<sub>_n_<!-- markdown separator -->−1</sub> × _r_<sup>_n_<!-- markdown separator -->−1</sup> + ... + _d_<sub>0</sub> × _r_<sup>0</sup> , where _d_<sub>_i_</sub> is the _i_+1-th _least significant digit_ and _r_ is the _base_ or _radix_ <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - positional notation / conversion ::@:: To convert from any base _a_ to any other base _b_, the simplest way _for humans_ is to convert it from base _a_ to base 10, and then from base 10 to base _b_. <p> To convert from base _a_ to base 10, use the positional notation definition. <p> To convert from base 10 to base _b_, keep doing round-toward-zero division by _b_ until the number is 0, keeping track of the remainders. Join the remainders to get the number in base _b_. The first remainder is the least significant digit. <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
- [binary number](../../../../general/binary%20number.md) (base 2) ::@:: a method for representing numbers that uses only two symbols for the natural numbers: typically "0" (zero) and "1" (one) <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - binary number / usage ::@:: It can model series of electrical signals computers use to represent information as a _bit sequence_, where "0" represents no/low voltage or off state and "1" represents presence/high voltage or on state. <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
- [byte § multiple-byte units](../../../../general/byte.md#multiple-byte%20units) ::@:: powers of 10: 1 B (byte), 1 kB (kilobyte) = 1000 B, 1 MB (megabyte) = 1000<sup>2</sup> B, 1 GB (gigabyte) = 1000<sup>3</sup> B, ... <br/> powers of 2: 1 B, 1 kiB (kibibyte) = 1024 B, 1 MiB (mebibyte) = 1024<sup>2</sup> B, 1 GiB (gibibyte) = 1024<sup>3</sup> B, ... <p> However, in practice... (very important!) <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - [byte § multiple-byte units](../../../../general/byte.md#multiple-byte%20units) / confusion ::@:: People frequently confuse the units for powers of 10 and powers of 2. In many contexts, the symbol for the units of powers of 10 are used to meant both, and which one it meant depends on the specific context. <p> In this course, when dealing with _size_, we mean the units of powers of 2. When dealing with _frequency_ or _rate_, we mean the units of powers of 10. In both cases, we use the symbol for the units of powers of 10, e.g. always use "kB". <!--SR:!2025-02-12,4,270!2025-02-19,8,250-->
- [classes of computers](../../../../general/classes%20of%20computers.md) ::@:: (in increasing power) embedded computers, personal computers, server computers, supercomputers <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - [personal computer](../../../../general/personal%20computer.md) ::@:: general purpose; many software; subject to cost—performance tradeoff <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - [server computer](../../../../general/server%20(computing).md) ::@:: network-based; high capacity, performance, reliability; ranges from small-sized to building-sized <!--SR:!2025-02-12,4,270!2025-02-22,11,270-->
  - [supercomputer](../../../../general/supercomputer.md) ::@:: high-end computers, often specialized for certain workloads, e.g. engineering, science; highest capabilities but very little market share <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - [embedded computer](../../../../general/embedded%20system.md) ::@:: hidden as components of systems; stringent constraints on cost, performance, power, etc. <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
- [abstraction layer](../../../../general/abstraction%20layer.md) ::@:: a way of hiding the working details of a subsystem. <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - abstraction layer / common computer layers ::@:: (from top to bottom) user, application, operating system, hardware <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - abstraction layer / application ::@:: written in high-level language <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - abstraction layer / operating system ::@:: compiler: high-level language to machine code; operating system: handle IO, manage memory and storage, manage resources, schedule tasks <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - abstraction layer / hardware ::@:: IO controllers, memory, processor <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
- [computer program](../../../../general/computer%20program.md) ::@:: a sequence or set of instructions in a programming language for a computer to execute <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - computer program / levels ::@:: (from top to bottom) high-level language, assembly language, machine code <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - computer program / high-level language ::@:: level of abstraction closer to the problem domain, so that you can work productivity and make the program more portable <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - computer program / assembly language ::@:: textual representation of instructions, in symbolic language <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - computer program / machine code ::@:: binary bits, which are encoded data or instructions <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
- abstraction layer
  - abstraction layer / necessity ::@:: It is impossible to understand computers by looking at every single transistor. Abstraction helps with coping with complexity. <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - abstraction layer / key ideas ::@:: Organize computer software and hardware into hierarchical layers. In a layer, details in the lower layers are hidden to simplify the current layer. Interactions between layers happen between well-defined interfaces. <p> An example is instruction set architecture (ISA), an interface between hardware and software. <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
- [instruction set architecture](../../../../general/instruction%20set%20architecture.md) (ISA) ::@:: an abstract model that generally defines how software controls the CPU in a computer or a family of computers <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - instruction set architecture / advantages ::@:: Allows your ISA code to run on different implementations of the ISA, e.g. different CPUs. <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - instruction set architecture / examples ::@:: ARM, MIPS, PowerPC, SPARC, x86 <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
- [computer](../../../../general/computer.md) ::@:: a machine that can be programmed to automatically carry out sequences of arithmetic or logical operations (computation) <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - computer / the very first computers ::@:: some uses punch cards as computer programs, very large (can be as large as a building), very low capabilities (compared to nowadays) <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
- [von Neumann architecture](../../../../general/von%20Neumann%20architecture.md) ::@:: control unit, processing unit, memory, storage, input/output mechanisms <p> in this course, 5 components: input, output, memory, processor (control + datapath) <!--SR:!2025-02-12,4,270!2025-02-19,8,250-->
  - von Neumann architecture / input ::@:: communicate with the computers; transfer data and instructions to the memory <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - von Neumann architecture / output ::@:: communicate with the users; transfer data from the memory <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - von Neumann architecture / memory ::@:: store to keep data and instructions <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - von Neumann architecture / processing unit (datapath) ::@:: unit to process data according to instructions <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - von Neumann architecture / control unit (control) ::@:: unit to control input, output, memory, and processing unit <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
- [information age](../../../../general/informaion%20age.md) ::@:: the agricultural revolution, then the industrial revolution, then the information revolution (computer revolution); thus we have the information age, and computers are pervasive <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - information age / why ::@:: one of the reasons: Moore's law: the number of transistors in an integrated circuit (IC) doubles about every two years <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - information age / applications ::@:: artificial intelligence, automobile computers, human genome project, search engines, world wide web <!--SR:!2025-02-12,4,270!2025-02-12,4,270-->
  - information age / trend ::@:: electronics technology continues to evolve due to increased capacity and reduced cost, e.g. vacuum tubes (1950s), transistors (1950, 1960s) to integrated circuits (1960s, 1970s), very large scale integrated (VLSI) circuits (since 1980s) <!--SR:!2025-02-19,8,250!2025-02-19,8,250-->

## week 1 lab

- datetime: 2025-02-04T15:00:00+08:00/2025-02-04T15:50:00+08:00
- status: unscheduled, no lab

## week 1 tutorial

- datetime: 2025-02-04T18:00:00+08:00/2025-02-04T18:50:00+08:00
- status: unscheduled, no tutorial

## assignments

## midterm examination

## final examination

## aftermath

### total
