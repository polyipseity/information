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
  - course learning outcomes (CLOs) ::@:: assembly language, digital logic, instruction set architecture (ISA), organizational paradigms, processor & memory <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - topics ::@:: brief digital circuit, data representation and arithmetic, instruction set architecture and assembly, computer architecture <!--SR:!2025-02-24,12,270!2025-02-24,12,270-->
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
- topic: course information, introduction
- logistics
- [numeral system](../../../../general/numeral%20system.md) ::@:: a mathematical notation for representing numbers of a given set, using digits or other symbols in a consistent manner <!--SR:!2025-02-26,14,290!2025-02-24,12,270-->
  - numeral system / common examples ::@:: binary (base 2; used by digital computers), octal (base 8), decimal (base 10; used by people), hexadecimal (base 16; concisely expresses a binary sequence), sexagesimal (base 60; used for timekeeping) <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
- [positional notation](../../../../general/positional%20notation.md) ::@:: (_d_<sub>_n_<!-- markdown separator -->−1</sub>..._d_<sub>0</sub>)<sub>_r_</sub> = _d_<sub>_n_<!-- markdown separator -->−1</sub> × _r_<sup>_n_<!-- markdown separator -->−1</sup> + ... + _d_<sub>0</sub> × _r_<sup>0</sup> , where _d_<sub>_i_</sub> is the _i_+1-th _least significant digit_ and _r_ is the _base_ or _radix_ <!--SR:!2025-02-24,12,270!2025-02-26,14,290--> <p> An extension to the above includes decimals by extending the positions to beyond the decimal point analogously.
  - positional notation / integral conversion ::@:: To convert from any base _a_ to any other base _b_, the simplest way _for humans_ is to convert it from base _a_ to base 10, and then from base 10 to base _b_. <p> To convert from base _a_ to base 10, use the positional notation definition. <p> To convert from base 10 to base _b_, keep doing round-toward-zero division by _b_ until the number is 0, keeping track of the remainders. Join the remainders to get the number in base _b_. The first remainder is the least significant digit. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
- [binary number](../../../../general/binary%20number.md) (base 2) ::@:: a method for representing numbers that uses only two symbols for the natural numbers: typically "0" (zero) and "1" (one) <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - binary number / usage ::@:: It can model series of electrical signals computers use to represent information as a _bit sequence_, where "0" represents no/low voltage or off state and "1" represents presence/high voltage or on state. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
- [byte § multiple-byte units](../../../../general/byte.md#multiple-byte%20units) ::@:: powers of 10: 1 B (byte), 1 kB (kilobyte) = 1000 B, 1 MB (megabyte) = 1000<sup>2</sup> B, 1 GB (gigabyte) = 1000<sup>3</sup> B, ... <br/> powers of 2: 1 B, 1 kiB (kibibyte) = 1024 B, 1 MiB (mebibyte) = 1024<sup>2</sup> B, 1 GiB (gibibyte) = 1024<sup>3</sup> B, ... <p> However, in practice... (very important!) <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - [byte § multiple-byte units](../../../../general/byte.md#multiple-byte%20units) / confusion ::@:: People frequently confuse the units for powers of 10 and powers of 2. In many contexts, the symbol for the units of powers of 10 are used to meant both, and which one it meant depends on the specific context. <p> In this course, when dealing with _size_, we mean the units of powers of 2. When dealing with _frequency_ or _rate_, we mean the units of powers of 10. In both cases, we use the symbol for the units of powers of 10, e.g. always use "kB". <!--SR:!2025-02-26,14,290!2025-02-19,8,250-->
- [classes of computers](../../../../general/classes%20of%20computers.md) ::@:: (in increasing power) embedded computers, personal computers, server computers, supercomputers <!--SR:!2025-02-24,12,270!2025-02-26,14,290-->
  - [personal computer](../../../../general/personal%20computer.md) ::@:: general purpose; many software; subject to cost—performance tradeoff <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - [server computer](../../../../general/server%20(computing).md) ::@:: network-based; high capacity, performance, reliability; ranges from small-sized to building-sized <!--SR:!2025-02-26,14,290!2025-02-22,11,270-->
  - [supercomputer](../../../../general/supercomputer.md) ::@:: high-end computers, often specialized for certain workloads, e.g. engineering, science; highest capabilities but very little market share <!--SR:!2025-02-24,12,270!2025-02-26,14,290-->
  - [embedded computer](../../../../general/embedded%20system.md) ::@:: hidden as components of systems; stringent constraints on cost, performance, power, etc. <!--SR:!2025-02-24,12,270!2025-02-24,12,270-->
- [abstraction layer](../../../../general/abstraction%20layer.md) ::@:: a way of hiding the working details of a subsystem. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - abstraction layer / common computer layers ::@:: (from top to bottom) user, application, operating system, hardware <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - abstraction layer / application ::@:: written in high-level language <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - abstraction layer / operating system ::@:: compiler: high-level language to machine code; operating system: handle IO, manage memory and storage, manage resources, schedule tasks <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - abstraction layer / hardware ::@:: IO controllers, memory, processor <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
- [computer program](../../../../general/computer%20program.md) ::@:: a sequence or set of instructions in a programming language for a computer to execute <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - computer program / levels ::@:: (from top to bottom) high-level language, assembly language, machine code <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - computer program / high-level language ::@:: level of abstraction closer to the problem domain, so that you can work productivity and make the program more portable <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - computer program / assembly language ::@:: textual representation of instructions, in symbolic language <!--SR:!2025-02-26,14,290!2025-02-24,12,270-->
  - computer program / machine code ::@:: binary bits, which are encoded data or instructions <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
- abstraction layer
  - abstraction layer / necessity ::@:: It is impossible to understand computers by looking at every single transistor. Abstraction helps with coping with complexity. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - abstraction layer / key ideas ::@:: Organize computer software and hardware into hierarchical layers. In a layer, details in the lower layers are hidden to simplify the current layer. Interactions between layers happen between well-defined interfaces. <p> An example is instruction set architecture (ISA), an interface between hardware and software. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
- [instruction set architecture](../../../../general/instruction%20set%20architecture.md) (ISA) ::@:: an abstract model that generally defines how software controls the CPU in a computer or a family of computers <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - instruction set architecture / advantages ::@:: Allows your ISA code to run on different implementations of the ISA, e.g. different CPUs. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - instruction set architecture / examples ::@:: ARM, MIPS, PowerPC, SPARC, x86 <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
- [computer](../../../../general/computer.md) ::@:: a machine that can be programmed to automatically carry out sequences of arithmetic or logical operations (computation) <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - computer / the very first computers ::@:: some uses punch cards as computer programs, very large (can be as large as a building), very low capabilities (compared to nowadays) <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
- [von Neumann architecture](../../../../general/von%20Neumann%20architecture.md) ::@:: control unit, processing unit, memory, storage, input/output mechanisms <p> in this course, 5 components: input, output, memory, processor (control + datapath) <!--SR:!2025-02-26,14,290!2025-02-19,8,250-->
  - von Neumann architecture / input ::@:: communicate with the computers; transfer data and instructions to the memory <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - von Neumann architecture / output ::@:: communicate with the users; transfer data from the memory <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - von Neumann architecture / memory ::@:: store to keep data and instructions <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - von Neumann architecture / processing unit (datapath) ::@:: unit to process data according to instructions <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - von Neumann architecture / control unit (control) ::@:: unit to control input, output, memory, and processing unit <!--SR:!2025-02-24,12,270!2025-02-26,14,290-->
- [information age](../../../../general/informaion%20age.md) ::@:: the agricultural revolution, then the industrial revolution, then the information revolution (computer revolution); thus we have the information age, and computers are pervasive <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - information age / why ::@:: one of the reasons: Moore's law: the number of transistors in an integrated circuit (IC) doubles about every two years <!--SR:!2025-02-26,14,290!2025-02-24,12,270-->
  - information age / applications ::@:: artificial intelligence, automobile computers, human genome project, search engines, world wide web <!--SR:!2025-02-24,12,270!2025-02-24,12,270-->
  - information age / trend ::@:: electronics technology continues to evolve due to increased capacity and reduced cost, e.g. vacuum tubes (1950s), transistors (1950, 1960s), integrated circuits (1960s, 1970s), very large scale integrated (VLSI) circuits (since 1980s) <!--SR:!2025-02-19,8,250!2025-02-19,8,250-->

## week 1 lab

- datetime: 2025-02-04T15:00:00+08:00/2025-02-04T15:50:00+08:00
- status: unscheduled, no lab

## week 1 tutorial

- datetime: 2025-02-04T18:00:00+08:00/2025-02-04T18:50:00+08:00
- status: unscheduled, no tutorial
- topic: number systems
- [numeral system](../../../../general/numeral%20system.md)
- [positional notation](../../../../general/positional%20notation.md)
  - positional notation / integral conversion
    - positional notation / integral conversion / base 2, base 16 ::@:: 4 base 2 digits can be grouped together, which _directly_ corresponds to 1 base 16 digit, and vice versa. This can help ease conversion between these two bases. <p> Note that you may need to add or remove padding zeros to make the original or resulting base 2 number have digit count that is a multiple of 4. <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->

## week 1 lecture 2

- datetime: 2025-02-07T09:00:00+08:00/2025-02-07T10:20:00+08:00
- topic: logic gates, truth table, logic function, multiplexor
- [analog signal](../../../../general/analog%20signal.md) ::@:: any continuous-time signal representing some other quantity; values vary over a broad range continuously <!--SR:!2025-03-08,18,325!2025-03-07,17,325-->
- [digital signal](../../../../general/digital%20signal.md) ::@:: a signal that represents data as a sequence of discrete values; at any given time it can only take on, at most, one of a finite number of values <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
  - digital signal / typical voltage ::@:: low/0: 0 V to 0.5 V; high/1: 2.4 V to 2.9 V; illegal: outside of the aforementioned ranges <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
- [bit](../../../../general/bit.md) ::@:: represents a logical state with one of two possible values <!--SR:!2025-03-08,18,325!2025-03-07,17,325-->
  - bit / applications in computers ::@:: instructions (e.g. operands, operations), number representations (e.g. floats, integers) <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
- [truth table](../../../../general/truth%20table.md) ::@:: a mathematical table used in logic—specifically in connection with Boolean algebra, Boolean functions, and propositional calculus—which sets out the functional values of logical expressions on each of their functional arguments, that is, for each combination of values taken by their logical variables; i.e. a table tha shows the _single_ (in this course, can be _multiple_) Boolean output of a function accepting _zero or more_ Boolean inputs <!--SR:!2025-03-07,17,325!2025-03-08,18,325-->
  - truth table / format ::@:: one column for each input and output; one row for each possible combination of inputs <!--SR:!2025-03-08,18,325!2025-03-01,11,305-->
- [Boolean algebra](../../../../general/Boolean%20algebra.md) ::@:: values: 0/true, 1/false; variables: can only take the aforementioned 2 values; operations: AND, NAND, NOR, NOT, OR, XOR <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
- [logic gate](../../../../general/logic%20gate.md) ::@:: a device that performs a Boolean function, a logical operation performed on one or more binary inputs that produces a single binary output <!--SR:!2025-03-08,18,325!2025-03-07,17,325-->
  - logic gate / basic examples ::@:: AND, NAND, NOR, NOT, OR, XOR <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
  - logic gate / NOT, inverter ::@:: $0 \mapsto 1; 1 \mapsto 0$ <br/> ${\overline {A} }$ or $\neg A$ <br/> ![NOT symbol](../../../../archives/Wikimedia%20Commons/NOT%20ANSI%20Labelled.svg) <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
  - logic gate / AND, conjunction ::@:: $(0, 0) \mapsto 0; (0, 1) \mapsto 0; (1, 0) \mapsto 0; (1, 1) \mapsto 1$ <br/> $A\cdot B$ or $A\land B$ <br/> ![AND symbol](../../../../archives/Wikimedia%20Commons/AND%20ANSI%20Labelled.svg) <!--SR:!2025-03-07,17,325!2025-03-07,17,325-->
  - logic gate / OR, disjunction ::@:: $(0, 0) \mapsto 0; (0, 1) \mapsto 1; (1, 0) \mapsto 1; (1, 1) \mapsto 1$ <br/> $A+B$ or $A\lor B$ <br/> ![OR symbol](../../../../archives/Wikimedia%20Commons/OR%20ANSI%20Labelled.svg) <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
  - logic gate / NAND, alternative denial ::@:: $(0, 0) \mapsto 1; (0, 1) \mapsto 1; (1, 0) \mapsto 1; (1, 1) \mapsto 0$ <br/> ${\overline {A\cdot B} }$ or $A\uparrow B$ <br/> ![NAND symbol](../../../../archives/Wikimedia%20Commons/NAND%20ANSI%20Labelled.svg) <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
  - logic gate / NOR, joint denial ::@:: $(0, 0) \mapsto 1; (0, 1) \mapsto 0; (1, 0) \mapsto 0; (1, 1) \mapsto 0$ <br/> ${\overline {A+B} }$ or $A\downarrow B$ <br/> ![NOR symbol](../../../../archives/Wikimedia%20Commons/NOR%20ANSI%20Labelled.svg) <!--SR:!2025-03-08,18,325!2025-03-07,17,325-->
  - logic gate / XOR, exclusive or ::@:: $(0, 0) \mapsto 0; (0, 1) \mapsto 1; (1, 0) \mapsto 1; (1, 1) \mapsto 0$ <br/> $A\oplus B$ or $A\veebar B$ <br/> ![XOR symbol](../../../../archives/Wikimedia%20Commons/XOR%20ANSI%20Labelled.svg) <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
  - logic gate / logic function ::@:: It is a function on binary variables whose output is also a binary variable. It can be represented by logic gates. AND, NOT, and OR are fundamental to all operations in modern computers. <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
    - logic gate / logic function / representations ::@:: graphics (e.g. Karnaugh map), logical expressions, truth table <!--SR:!2025-03-07,17,325!2025-03-08,18,325-->
  - logic gate / example ::@:: 1-bit half adder: given _A_ and _B_, outputs _S_ and _C_. _S_ = _A_ XOR _B_, _C_ = _A_ AND _B_. <p> So _S_ is interpreted as the resulting bit after addition, while _C_ is the carry bit (e.g. to be connected to another 1-bit half adder). <!--SR:!2025-03-07,17,325!2025-03-08,18,325-->
  - logic gate / circuit types ::@:: 2 main ones: combinational logic circuit, sequential logic circuit <!--SR:!2025-03-08,18,325!2025-03-07,17,325-->
- [combinational logic](../../../../general/combinational%20logic.md) ::@:: It has no memory. The outputs depend entirely on the _current_ inputs and noting else. It is essentially the same as a logic function, so can be represented by a truth table. <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
- [sequential logic](../../../../general/sequential%20logic.md) ::@:: It has memory. The outputs depend on the _current_ inputs and the _state_ (value stored in _memory_). That is, the output _additionally_ depends on the input history. <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
- [combinational logic](../../../../general/combinational%20logic.md)
  - [combinational logic](../../../../general/combinational%20logic.md) / circuits ::@:: e.g. multiplexor/demultiplexor, encoder/decoder, two-level logic, programmable logic array (PLA); these are higher-level basic building blocks that are commonly seen in combinational logic <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
- [multiplexer](../../../../general/multiplexer.md)/selector, demultiplexer ::@:: (former) a device that selects between several analog or digital input signals and forwards the selected input to a single output line <p> (latter) a device that takes a single input signal and selectively forwards it to one of several output lines <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
  - multiplexer / 2<sup>_n_</sup>-to-1 multiplexer ::@:: 2<sup>_n_</sup> data inputs, _n_ selection inputs, and 1 output <p> The _n_ selection inputs have 2<sup>_n_</sup> possible combinations. Each combination selects 1 data input and forwards it to the output. <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
    - multiplexer / 2<sup>_n_</sup>-to-1 multiplexer / implementation ::@:: Use an AND gate for each data input. Connect the data input to its corresponding AND gate. Then connect the _n_ selection inputs to the AND gates, adding NOT gates as needed, such that each unique combination of _n_ selection inputs makes exactly one AND gate possible to be made output 1 iff its corresponding input is 1. Finally, connect all the AND gates into 1 giant OR gate, and that is the output. <!--SR:!2025-03-08,18,325!2025-02-25,8,285-->
- [binary decoder](../../../../general/binary%20decoder.md), encoder ::@:: (former) a combinational logic circuit that converts binary information from the n coded inputs to a maximum of 2<sup>_n_</sup> unique outputs <p> (latter) does the reverse <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
  - binary decoder / _n_-to-2<sup>_n_</sup> decoder ::@:: _n_ data inputs, 2<sup>_n_</sup> data outputs <p> Each unique combination of inputs activates exactly one output. For machine learning people: This is just an _one hot_ encoder. <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
    - binary decoder / _n_-to-2<sup>_n_</sup> decoder / implementation ::@:: Use an AND gate for each data output. Connect the data output to its corresponding AND gate. Then connect the _n_ selection inputs to the AND gates, adding NOT gates as needed, such that each unique combination of _n_ selection inputs makes exactly one AND gate output 1. <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
- [logic gate](../../../../general/logic%20gate.md)
  - logic gate / design process ::@:: problem specification, truth table, logical expression, simplification, implementation <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
    - logic gate / design process / example ::@:: 3-people majority vote: output 1 if two or more inputs are 1, otherwise 0 <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->

## assignments

## midterm examination

## final examination

## aftermath

### total
