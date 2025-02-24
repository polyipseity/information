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
  - topics ::@:: brief digital circuit, data representation and arithmetic, instruction set architecture and assembly, computer architecture <!--SR:!2025-04-12,47,290!2025-03-28,32,270-->
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
- [numeral system](../../../../general/numeral%20system.md) ::@:: a mathematical notation for representing numbers of a given set, using digits or other symbols in a consistent manner <!--SR:!2025-02-26,14,290!2025-04-10,45,290-->
  - numeral system / common examples ::@:: binary (base 2; used by digital computers), octal (base 8), decimal (base 10; used by people), hexadecimal (base 16; concisely expresses a binary sequence), sexagesimal (base 60; used for timekeeping) <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
- [positional notation](../../../../general/positional%20notation.md) ::@:: (_d_<sub>_n_<!-- markdown separator -->−1</sub>..._d_<sub>0</sub>)<sub>_r_</sub> = _d_<sub>_n_<!-- markdown separator -->−1</sub> × _r_<sup>_n_<!-- markdown separator -->−1</sup> + ... + _d_<sub>0</sub> × _r_<sup>0</sup> , where _d_<sub>_i_</sub> is the _i_+1-th _least significant digit_ and _r_ is the _base_ or _radix_  <p> An extension to the above includes decimals by extending the positions to beyond the decimal point analogously. <!--SR:!2025-04-12,47,290!2025-02-26,14,290-->
  - positional notation / integral conversion ::@:: To convert from any base _a_ to any other base _b_, the simplest way _for humans_ is to convert it from base _a_ to base 10, and then from base 10 to base _b_. <p> To convert from base _a_ to base 10, use the positional notation definition. <p> To convert from base 10 to base _b_, keep doing round-toward-zero division by _b_ until the number is 0, keeping track of the remainders. Join the remainders to get the number in base _b_. The first remainder is the least significant digit. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
- [binary number](../../../../general/binary%20number.md) (base 2) ::@:: a method for representing numbers that uses only two symbols for the natural numbers: typically "0" (zero) and "1" (one) <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - binary number / usage ::@:: It can model series of electrical signals computers use to represent information as a _bit sequence_, where "0" represents no/low voltage or off state and "1" represents presence/high voltage or on state. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
- [byte § multiple-byte units](../../../../general/byte.md#multiple-byte%20units) ::@:: powers of 10: 1 B (byte), 1 kB (kilobyte) = 1000 B, 1 MB (megabyte) = 1000<sup>2</sup> B, 1 GB (gigabyte) = 1000<sup>3</sup> B, ... <br/> powers of 2: 1 B, 1 kiB (kibibyte) = 1024 B, 1 MiB (mebibyte) = 1024<sup>2</sup> B, 1 GiB (gibibyte) = 1024<sup>3</sup> B, ... <p> However, in practice... (very important!) <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - [byte § multiple-byte units](../../../../general/byte.md#multiple-byte%20units) / confusion ::@:: People frequently confuse the units for powers of 10 and powers of 2. In many contexts, the symbol for the units of powers of 10 are used to meant both, and which one it meant depends on the specific context. <p> In this course, when dealing with _size_, we mean the units of powers of 2. When dealing with _frequency_ or _rate_, we mean the units of powers of 10. In both cases, we use the symbol for the units of powers of 10, e.g. always use "kB". <!--SR:!2025-02-26,14,290!2025-03-11,20,250-->
- [classes of computers](../../../../general/classes%20of%20computers.md) ::@:: (in increasing power) embedded computers, personal computers, server computers, supercomputers <!--SR:!2025-04-10,45,290!2025-02-26,14,290-->
  - [personal computer](../../../../general/personal%20computer.md) ::@:: general purpose; many software; subject to cost—performance tradeoff <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - [server computer](../../../../general/server%20(computing).md) ::@:: network-based; high capacity, performance, reliability; ranges from small-sized to building-sized <!--SR:!2025-02-26,14,290!2025-03-24,30,270-->
  - [supercomputer](../../../../general/supercomputer.md) ::@:: high-end computers, often specialized for certain workloads, e.g. engineering, science; highest capabilities but very little market share <!--SR:!2025-04-09,44,290!2025-02-26,14,290-->
  - [embedded computer](../../../../general/embedded%20system.md) ::@:: hidden as components of systems; stringent constraints on cost, performance, power, etc. <!--SR:!2025-04-11,46,290!2025-04-10,45,290-->
- [abstraction layer](../../../../general/abstraction%20layer.md) ::@:: a way of hiding the working details of a subsystem. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - abstraction layer / common computer layers ::@:: (from top to bottom) user, application, operating system, hardware <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - abstraction layer / application ::@:: written in high-level language <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - abstraction layer / operating system ::@:: compiler: high-level language to machine code; operating system: handle IO, manage memory and storage, manage resources, schedule tasks <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - abstraction layer / hardware ::@:: IO controllers, memory, processor <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
- [computer program](../../../../general/computer%20program.md) ::@:: a sequence or set of instructions in a programming language for a computer to execute <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - computer program / levels ::@:: (from top to bottom) high-level language, assembly language, machine code <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - computer program / high-level language ::@:: level of abstraction closer to the problem domain, so that you can work productivity and make the program more portable <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - computer program / assembly language ::@:: textual representation of instructions, in symbolic language <!--SR:!2025-02-26,14,290!2025-04-12,47,290-->
  - computer program / machine code ::@:: binary bits, which are encoded data or instructions <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
- abstraction layer
  - abstraction layer / necessity ::@:: It is impossible to understand computers by looking at every single transistor. Abstraction helps with coping with complexity. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - abstraction layer / key ideas ::@:: Organize computer software and hardware into hierarchical layers. In a layer, details in the lower layers are hidden to simplify the current layer. Interactions between layers happen between well-defined interfaces. <p> An example is instruction set architecture (ISA), an interface between hardware and software. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
- [instruction set architecture](../../../../general/instruction%20set%20architecture.md) (ISA) ::@:: an abstract model that generally defines how software controls the CPU in a computer or a family of computers <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - instruction set architecture / advantages ::@:: Allows your ISA code to run on different implementations of the ISA, e.g. different CPUs. <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - instruction set architecture / examples ::@:: ARM, MIPS, PowerPC, SPARC, x86 <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
- [computer](../../../../general/computer.md) ::@:: a machine that can be programmed to automatically carry out sequences of arithmetic or logical operations (computation) <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - computer / the very first computers ::@:: some uses punch cards as computer programs, very large (can be as large as a building), very low capabilities (compared to nowadays) <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
- [von Neumann architecture](../../../../general/von%20Neumann%20architecture.md) ::@:: control unit, processing unit, memory, storage, input/output mechanisms <p> in this course, 5 components: input, output, memory, processor (control + datapath) <!--SR:!2025-02-26,14,290!2025-03-10,19,250-->
  - von Neumann architecture / input ::@:: communicate with the computers; transfer data and instructions to the memory <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - von Neumann architecture / output ::@:: communicate with the users; transfer data from the memory <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - von Neumann architecture / memory ::@:: store to keep data and instructions <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - von Neumann architecture / processing unit (datapath) ::@:: unit to process data according to instructions <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - von Neumann architecture / control unit (control) ::@:: unit to control input, output, memory, and processing unit <!--SR:!2025-03-28,32,270!2025-02-26,14,290-->
- [information age](../../../../general/informaion%20age.md) ::@:: the agricultural revolution, then the industrial revolution, then the information revolution (computer revolution); thus we have the information age, and computers are pervasive <!--SR:!2025-02-26,14,290!2025-02-26,14,290-->
  - information age / why ::@:: one of the reasons: Moore's law: the number of transistors in an integrated circuit (IC) doubles about every two years <!--SR:!2025-02-26,14,290!2025-04-11,46,290-->
  - information age / applications ::@:: artificial intelligence, automobile computers, human genome project, search engines, world wide web <!--SR:!2025-04-09,44,290!2025-04-11,46,290-->
  - information age / trend ::@:: electronics technology continues to evolve due to increased capacity and reduced cost, e.g. vacuum tubes (1950s), transistors (1950, 1960s), integrated circuits (1960s, 1970s), very large scale integrated (VLSI) circuits (since 1980s) <!--SR:!2025-03-05,10,230!2025-03-10,19,250-->

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
  - bit / applications in computers ::@:: instructions (e.g. operands, operations), number representations (e.g. floats, integers, rationals) <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
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

## week 2 lecture

- datetime: 2025-02-10T13:30:00+08:00/2025-02-10T14:50:00+08:00
- topic: decoder, two-level logic, programmable logic array
- [binary decoder](../../../../general/binary%20decoder.md), encoder ::@:: (former) a combinational logic circuit that converts binary information from the n coded inputs to a maximum of 2<sup>_n_</sup> unique outputs <p> (latter) does the reverse <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
  - binary decoder / _n_-to-2<sup>_n_</sup> decoder ::@:: _n_ data inputs, 2<sup>_n_</sup> data outputs <p> Each unique combination of inputs activates exactly one output. For machine learning people: This is just an _one hot_ encoder. <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
    - binary decoder / _n_-to-2<sup>_n_</sup> decoder / implementation ::@:: Use an AND gate for each data output. Connect the data output to its corresponding AND gate. Then connect the _n_ selection inputs to the AND gates, adding NOT gates as needed, such that each unique combination of _n_ selection inputs makes exactly one AND gate output 1. <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
- [logic gate](../../../../general/logic%20gate.md)
  - logic gate / design process ::@:: problem specification, truth table, logical expression, simplification, implementation <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
    - logic gate / design process / example ::@:: 3-people majority vote: output 1 if two or more inputs are 1, otherwise 0 <!--SR:!2025-03-08,18,325!2025-03-08,18,325-->
- [canonical normal form](../../../../general/canonical%20normal%20form.md) ::@:: Any Boolean function can be expressed as a disjunction (OR) of minterms or a conjunction (AND) of maxterms. <!--SR:!2025-03-14,19,342!2025-03-14,19,342-->
  - [minterm](../../../../general/canonical%20normal%20form.md#minterms) ::@:: For $n$ input variables, it is a product (AND) term in which each of the $n$ variables appears _exactly_ once (either in its complemented or uncomplemented form). <p> If you put this term as the output in a truth table for all possible _n_ inputs, you will see _exactly_ one row outputs 1. This is the key insight to how it works. <!--SR:!2025-03-13,18,342!2025-03-07,12,322-->
    - minterm / indexing ::@:: There are $2^n$ possible minterms. Assign the value 1 to the direct form \($x_{i}$\) and 0 to the complemented form \($x'_{i}$\) (these assignments are reversed for maxterm); the minterm is then $\sum \limits _{i=1}^{n}2^{i-1}\operatorname {value} (x_{i})$. <p> For example, minterm $abc'$ is numbered 110<sub>2</sub> = 6<sub>10</sub> and denoted $m_{6}$. <!--SR:!2025-03-13,18,342!2025-03-14,19,342-->
  - [maxterm](../../../../general/canonical%20normal%20form.md#maxterm) ::@:: For $n$ input variables, it is a sum (OR) term in which each of the $n$ variables appears _exactly_ once (either in its complemented or uncomplemented form). <p> If you put this term as the output in a truth table for all possible _n_ inputs, you will see _exactly_ one row outputs 0. This is the key insight to how it works. <!--SR:!2025-03-14,19,342!2025-03-13,18,342-->
    - maxterm / indexing ::@:: There are $2^n$ possible maxtems. Assign the value 0 to the direct form \($x_{i}$\) and 1 to the complemented form \($x'_{i}$\) (these assignments are reversed for minterm); the maxterm is then $\sum \limits _{i=1}^{n}2^{i-1}\operatorname {value} (x_{i})$. <p> For example, we assign the index 6 to the maxterm $a'+b'+c$ \(110\) and denote that maxterm as _M_<sub>6</sub>. The complement $(a'+b'+c)'$ is the minterm $abc'=m_{6}$, using [de Morgan's law](../../../../general/De%20Morgan's%20law.md). <!--SR:!2025-03-13,18,342!2025-03-08,13,322-->
  - two-level representation ::@:: A representation where every input is a variable or its complement, one level consists of AND only, and the other level consists of OR only. There are two forms: sum of products (SOP), product of sums (POS). <!--SR:!2025-03-14,19,342!2025-03-14,19,342-->
  - [minterm canonical form](../../../../general/canonical%20normal%20form.md#minterm%20canonical%20form), sum of products (SOP) ::@:: Given the truth table of a logical function, it is possible to write the function as a "sum of products" or "sum of minterms". This is a _two-level representation_. <p> The key insight is that since a minterm is 1 for _exactly_ one input possible combination, adding (OR) minterms appropriately can produce any truth table. This is done by adding (OR) the minterms for which the corresponding row in the given truth table outputs 1. <!--SR:!2025-03-07,12,322!2025-03-14,19,342-->
  - [maxterm canonical form](../../../../general/canonical%20normal%20form.md#maxterm%20canonical%20form), sum of products (SOP) ::@:: Given the truth table of a logical function, it is possible to write the function as a "product of sums" or "product of maxterms". This is a _two-level representation_. <p> The key insight is that since a maxterm is 0 for _exactly_ one input possible combination, multiplying (AND) maxterms appropriately can produce any truth table. This is done by multiplying (AND) the maxterms for which the corresponding row (note the variables are negated) in the given truth table outputs 0. <!--SR:!2025-03-08,13,322!2025-03-13,18,342-->
- [programmable logic array](../../../../general/progammable%20logic%20array.md) (PLA) ::@:: a kind of programmable logic device used to implement combinational logic circuits <!--SR:!2025-03-13,18,342!2025-03-13,18,342-->
  - programmable logic array (PLA) / description ::@:: It has 2<sup>N</sup> AND gates for N input variables, and for M outputs from the PLA, there should be M OR gates, each with programmable inputs from all of the AND gates. <p> Each AND gate represents a minterm. Each OR gate represents a sum of products. An optimization is that if a minterm will not be used, less AND gates are needed (in the lecture slides, the PLA example has 7 AND gates only for 3 inputs). <!--SR:!2025-03-14,19,342!2025-03-14,19,342-->
  - programmable logic array (PLA) / intuition ::@:: The AND plane consisting of 2<sup>N</sup> AND gates produce all possible minterms. The OR plane consisting of M gates produces the required M outputs, assembled from all possible minterms from the AND plane. <!--SR:!2025-03-13,18,342!2025-03-14,19,342-->
  - programmable logic array (PLA) / duality ::@:: Theoretically, product of sums (POS) could be used instead, with an OR plane generating all possible maxterms, connected to an AND plane generating the required outputs. <p> However, negations are needed when you convert a truth table to POS, which is more mentally demanding and less intuitive. So that is why this is not often seen in practice. <!--SR:!2025-03-13,18,342!2025-03-13,18,342-->

## week 2 lab

- datetime: 2025-02-11T15:00:00+08:00/2025-02-11T15:50:00+08:00
- status: unscheduled, no lab

## week 2 tutorial

- datetime: 2025-02-11T18:00:00+08:00/2025-02-11T18:50:00+08:00
- status: unscheduled, no tutorial

## week 2 lecture 2

- datetime: 2025-02-14T09:00:00+08:00/2025-02-14T10:20:00+08:00
- topic: logical equivalence, Boolean algebra, K-map
- [logical equivalence](../../../../general/logical%20equivalence.md) ::@:: Two statements are this if they have the same truth value in every model. <p> In the context of combinational logic, this means two Boolean functions have the same output for every combination of inputs. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
  - logical equivalence / methods ::@:: logical expression, truth table <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
  - logical equivalence / truth table ::@:: Very easy to prove equivalence: Check if all rows are the same. However the number of rows grows exponentially: 2<sup>_n_</sup>. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
  - logical equivalence / logical expression ::@:: They give a more concise way to express Boolean functions, especially ones with many input variables. However, it is not always obvious that two different expressions are the same logically, so we need to simplify the expressions using Boolean algebra or Karnaugh map. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
- Boolean algebra
  - Boolean algebra / laws ::@:: Translate logical statements into mathematical symbols. Then these laws may be used to simplify the mathematical expression. Then get back simplified logical statements. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
    - Boolean algebra / laws / identity laws ::@:: $$\begin{aligned} p \land \top & \equiv p \\ p \lor \bot & \equiv p \end{aligned}$$ <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
    - Boolean algebra / laws / domination laws (null laws) ::@:: $$\begin{aligned} p \lor \top & \equiv \top \\ p \land \bot & \equiv \bot \end{aligned}$$ <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
    - Boolean algebra / laws / idempotent or tautology laws ::@:: $$\begin{aligned} p \lor p & \equiv p \\ p \land p & \equiv p \end{aligned}$$ <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
    - Boolean algebra / laws / negation laws (inverse laws) ::@:: $$\begin{aligned} p \lor \lnot p & \equiv \top \\ p \land \lnot p & \equiv \bot \end{aligned}$$ <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
    - Boolean algebra / laws / [commutative laws](commutative%20property.md) ::@:: $$\begin{aligned} p\vee q & \equiv q\vee p \\ p\wedge q &\equiv q\wedge p \end{aligned}$$ <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
    - Boolean algebra / laws / [associative laws](associative%20property.md) ::@:: $$\begin{aligned} (p \lor q) \lor r & \equiv p \lor (q \lor r) \\ (p \land q) \land r & \equiv p \land (q \land r) \end{aligned}$$ <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
    - Boolean algebra / laws / [distributive laws](distributive%20property.md) ::@:: $$\begin{aligned} p \lor (q \land r) & \equiv (p \lor q) \land (p \lor r) \\ p \land (q \lor r) & \equiv (p \land q) \lor (p \land r) \end{aligned}$$ <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
    - Boolean algebra / laws / [absorption laws](absorption%20law.md) ::@:: $$\begin{aligned} p \lor (p \land q) & \equiv p \\ p \land (p \lor q) & \equiv p \end{aligned}$$ <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
    - Boolean algebra / laws / [De Morgan's laws](De%20Morgan's%20laws.md) ::@:: $$\begin{aligned} \lnot (p \land q) & \equiv \lnot p \lor \lnot q \\ \lnot (p \lor q) & \equiv \lnot p \land \lnot q \end{aligned}$$ <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
    - Boolean algebra / laws / [double negation](double%20negation.md) law ::@:: $$\neg (\neg p)\equiv p$$ <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
- [Karnaugh map](../../../../general/Karnaugh%20map.md) (K-map) ::@:: A diagram that can be used to simplify a Boolean algebra expression. <p> (Note: K-map for 5 variables or more exist.) <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
  - Karnaugh map / construction ::@:: The row and column indices (shown across the top and down the left side of the Karnaugh map) are ordered in Gray code rather than binary numerical order. Gray code ensures that only one variable changes between each pair of adjacent cells. Each cell of the completed Karnaugh map contains a binary digit representing the function's output for that combination of inputs (i.e. a minterm). <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
    - Karnaugh map / construction / 2 inputs ::@:: ![Karnaugh map for 2 inputs](../../../../archives/Wikimedia%20Commons/K-map%202x2%20empty.svg) <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
    - Karnaugh map / construction / 3 inputs ::@:: ![Karnaugh map for 3 inputs](../../../../archives/Wikimedia%20Commons/K-map%202x4%20empty.svg) <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
    - Karnaugh map / construction / 4 inputs ::@:: ![Karnaugh map for 4 inputs](../../../../archives/Wikimedia%20Commons/K-map%204x4%20empty.svg) <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
    - Karnaugh map / construction / 5 inputs ::@:: It is possible, but you will need to think in 3D. Stack 2 4x4 Karnaugh map vertically. It gets even harder for 6 inputs or more... <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
    - Karnaugh map / construction / torus ::@:: You should not use a torus in practice. This is simply to demonstrate how a K-map can be made into a torus: ![Karnaugh map for 4 inputs as a torus](../../../../archives/Wikimedia%20Commons/Karnaugh%20map%20torus.svg) <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
  - Karnaugh map / grouping ::@:: Group adjacent 1s in the diagram. The grid is toroidally connected (torus shaped), so _adjacent_ cells include wrapping across the edges of the diagram (left/right edge, top/bottom edge). That means groups can wrap across the edges. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
    - Karnaugh map / grouping / rules ::@:: The union of all groups covers all 1s. <br/> Each group has a size that is a power of 2 (i.e. 1, 2, 4, 8, ...). <br/> Each group should be as large as possible, so that the resulting minterm has the least number of variables. <br/> Number of groups should be the fewest, so that the resulting SOP has the least number of minterms. <br/> Groups may overlap: make use of this extensively to make the groups as large as possible and cover all 1s with the least number of groups. <p> Note that the best grouping may not be unique. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
  - Karnaugh map / solution ::@:: Each group corresponds to one minterm. It can be found by examining which variables stay the same within each box. Those that stay the same should be included, while those do not should be excluded. Intuitively, each term halves the grouping size. <p> Finally, add the minterms together to get a SOP. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
  - Karnaugh map / inverse ::@:: Group adjacent 0s in the diagram instead. This produces a SOP for the inverse. Using De Morgan's laws, we can obtain a POS for the original function. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
  - Karnaugh map / don't cares ::@:: Those cells are marked with a X. In that case, we can either cover or not cover them, choosing the one that gives the better grouping. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
- [seven-segment display](../../../../general/seven-segment%20display.md) ::@:: It is a form of electronic display device for displaying decimal numerals that is an alternative to the more complex dot matrix displays. <p> Basically a display with a gray 8-shape with sharp corners, which have certain edges of the 8-shape activated (glowing) to show a decimal (0123456789)/hexadecimal (0123456789AbCdEF) digit. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->

## week 3 lecture

- datetime: 2025-02-17T13:30:00+08:00/2025-02-17T14:50:00+08:00
- topic: sequential logic, S-R latch, D latch, D flip-flop
- [flip-flop](../../../../general/flip-flop%20(electronics).md) ::@:: They are circuits that have two stable states that can store state information – a bistable multivibrator. The circuit can be made to change state by signals applied to one or more control inputs and will output its state (often along with its logical complement too). It is the basic storage element in sequential logic. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
  - flip-flop / SR NOR latch ::@:: An unclocked/asynchronous memory element. Its 2 inputs are S (set) and R (reset). Its 2 outputs are Q (stored output) and its complement. It consists of two parallel NOR gates where the output of each NOR is also fanned out into one input of the other NOR. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
    - flip-flop / SR NOR latch / symbol, figure ::@:: symbol: ![SR NOR latch symbol](../../../../archives/Wikimedia%20Commons/SR%20(NAND)%20Flip-flop.svg) <br/> figure: ![SR NOR latch figure](../../../../archives/Wikimedia%20Commons/R-S%20mk2.gif) <!--SR:!2025-02-26,3,307!2025-02-27,4,327-->
    - flip-flop / SR NOR latch / operations ::@:: hold/_quiescent_/latch state: If S and R are both 0, Q and its complement keep their previous outputs <br/> set: If S is 1 and R is 0, Q becomes 1 and its complement becomes 0. <br/> unset: If S is 0 and R is 1, Q becomes 0 and its complement becomes 1. <br/> _race condition_: S and R are not allowed to be both 1, as both outputs are now 0. Then, if S and R both goes to 0 _simultaneously_ afterwards, the outputs are metastable and may eventually lock at either 1 or 0 depending on the propagation time relations between the gates. <!--SR:!2025-02-26,3,307!2025-02-27,4,327-->
  - flip-flop / SR NAND latch ::@:: It is also possible to use NAND instead of NOR to make a SR latch. But it is more rare because the inputs' meaning are negated, i.e. the hold state requires both inputs to be 1. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
  - flip-flop / SR AND-OR latch ::@:: It may be easier from a teaching point of view. See the figure and try to figure its mechanism yourself: ![SR AND-OR latch](../../../../archives/Wikimedia%20Commons/RS-and-or-flip-flop.png) <!--SR:!2025-02-27,4,327!2025-02-26,3,307-->
  - flip-flop / gated latches ::@:: Latches are designed to be _transparent_. That is, input signal changes cause immediate changes in output. Additional logic can be added to a transparent latch to make it _non-transparent_ or _opaque_ when another input (an "enable" input) is not asserted. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
  - flip-flop / gated SR latch ::@:: Literally just an additionally "enable" input E AND-ing with the other 2 inputs. If E is 1, it works exactly as a SR latch. Otherwise, no action (hold state), no matter how the other 2 inputs are. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
    - flip-flop / gated SR latch / symbol, figure ::@:: symbol: ![gated SR latch symbol](../../../../archives/Wikimedia%20Commons/Gated%20SR%20flip-flop%20Symbol.svg) <br/> figure: ![gated SR latch figure](../../../../archives/Wikimedia%20Commons/SR%20(Clocked)%20Flip-flop%20Diagram.svg) <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
  - flip-flop / gated D latch ::@:: This latch exploits the fact that, in the two active input combinations (01 and 10) of a gated SR latch, R is the complement of S. <p> So what we do is, on top of the gated SR latch, instead of having the inputs S and R, we have one input D (data) only, connecting to the (now internal) S an R inputs. Assuming E is 1. If D is 0, S is 0 and R is 1. Otherwise, S is 1 and R is 0. If E is 0, nothing happens, as in the gated SR latch. <p> When E is 1, it looks like the input D is being "written" into the gate memory, so D is called _data_. The "enable" input E is sometimes also called WE (write enable) instead for the same reason. <!--SR:!2025-02-26,3,307!2025-02-27,4,327-->
    - flip-flop / gated D latch / symbol, figure ::@:: symbol: ![gated D latch symbol](../../../../archives/Wikimedia%20Commons/Transparent%20Latch%20Symbol.svg) <br/> figure: ![gated D latch symbol](../../../../archives/Wikimedia%20Commons/D-type%20Transparent%20Latch%20(NOR).svg) <!--SR:!2025-02-26,3,307!2025-02-27,4,327-->
    - flip-flop / gated D latch / register ::@:: It stores a multi-bit value. A _n_-bit \(_this_\) can be implemented using _n_ gated D-latches, all controlled by a common WE. Then when we want to write to the register, set WE to 1 and the _n_ D inputs to the desired dat. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
- [clock signal](../../../../general/clock%20signal.md) ::@:: It is an electronic logic signal (voltage or current) which oscillates between a high and a low state at a constant frequency and is used like a metronome to synchronize actions of digital circuits. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
  - clock signal / synchronization ::@:: In a _synchronous_ logic circuit, the most common type of digital circuit, the clock signal is applied to all storage devices, flip-flops and latches, and causes them all to change state simultaneously, preventing race conditions. <p> In a computer, there are many types of circuits, and each take different time to complete (propagation delay). If we do not clock the circuits, then the outputs of circuits can change unpredictably. <p> A clock-less circuit is known as _asynchronous_ circuit, but it is much harder to design than _synchronous_ ones, and is out-of-scope for this course. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
  - clock / terminology ::@:: A _clock_ is is a free-running signal with a fixed _cycle time_ (called _clock period_) or, equivalently, a fixed _clock frequency_ (i.e., inverse of the _cycle time_). _Edge-triggered clocking_ refers to state changes in a circuit on a clock (rising or falling) edge. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
- [digital timing diagram](../../../../general/digital%20timing%20diagram.md) ::@:: It represents a set of signals in the time domain. A timing diagram can contain many rows, usually one of them being the clock. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
  - digital timing diagram / conventions ::@:: Higher value is a logic one. Lower value is a logic zero. A slot showing a high and low is an either-or (such as on a data line). A Z indicates high impedance. A greyed out slot is a don't-care or indeterminate. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
- flip-flop
  - flip-flop / latch vs. flip-flop ::@:: For the former, outputs can change any time the clock is asserted (high). For the latter, outputs can change only on a clock (rising or falling) edge. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
  - flip-flop / D flip-flop ::@:: It is widely used, and known as a "data" flip-flop. It captures the value of the D-input at a definite portion of the clock cycle (such as the rising edge of the clock). That captured value becomes the Q output. At other times, the output Q does not change. It can be viewed as a memory cell, a zero-order hold, or a delay line. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
    - flip-flop / D flip-flop / S, R inputs ::@:: Most D-type flip-flops in ICs have the capability to be forced to the set or reset state (which ignores the D and clock inputs), much like an SR flip-flop. Usually, the illegal S = R = 1 condition is resolved in D-type flip-flops. Setting S = R = 0 makes the flip-flop behave as described above. <p> In this course, our flip-flops do not have these inputs. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
    - flip-flop / D flip-flop / symbol ::@:: ![D flip-flop symbol](../../../../archives/Wikimedia%20Commons/D-Type%20Flip-flop.svg) <!--SR:!2025-02-27,4,327!2025-02-26,3,307-->
  - flip-flop / master–slave edge-triggered D flip-flop ::@:: It is created by connecting two gated D latches in series, and inverting the enable input to one of them. It is called master–slave because the master latch controls the slave latch's output value Q and forces the slave latch to hold its value whenever the slave latch is enabled, as the slave latch always copies its new value from the master latch and changes its value only in response to a change in the value of the master latch and clock signal. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
    - flip-flop / master–slave edge-triggered D flip-flop / diagrams ::@:: rising/positive edge: ![master–slave rising/positive-edge-triggered D flip-flop diagram](../../../../archives/Wikimedia%20Commons/D-Type%20Flip-flop%20Diagram.svg) <br/> falling/negative edge: ![master–slave falling/negative-edge-triggered D flip-flop diagram](../../../../archives/Wikimedia%20Commons/Negative-edge%20triggered%20master%20slave%20D%20flip-flop.svg) <!--SR:!2025-02-26,3,307!2025-02-27,4,327-->
    - flip-flop / master–slave edge-triggered D flip-flop / intuition ::@:: Using the falling/negative-edge-triggered variant as an example. When the clock is high, the first latch (master) has its WE as 1, so it is writable, while the second latch (slave) has its WE as 0, so its output remains unchanged. When the clock is low, the first latch (master) ha its WE as 0, so it is not writeable, while the second latch (slave) has its WE as 1, so its output copies from the first latch (master). <p> We see that first latch (master) is only writable when the clock is high, while the output update takes place when the clock is low. When the clock falls from high to low, this is precisely when the latest input to the first latch (master) is saved and not affected by subsequent changes, while the second latch (slave) copies from the newly saved state of first latch (master). Thus it is falling/negative-edge-triggered. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
- sequential logic
  - sequential logic / synchronous ::@:: In a sequential circuit, it remembers its state (a "snapshot"). When it is _additionally_ clocked, i.e. synchronous sequential circuit, we can treat its state as changing _on and only on_ each clock cycle. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->

## week 3 lab

- datetime: 2025-02-18T15:00:00+08:00/2025-02-18T15:50:00+08:00
- topic: introduction to Logisim, combinational circuits
- Logisim ::@:: It is an interactive graphical interface for designing, simulating digital logic circuit. (Runs on Java 5... ancient software?!?) <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
  - Logisim / download ::@:: <https://sourceforge.net/projects/circuit/> <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
  - Logisim / installation
  - Logisim / usage
  - Logisim / save as library

## week 3 tutorial

- datetime: 2025-02-18T18:00:00+08:00/2025-02-18T18:50:00+08:00
- topic: combinational logic circuit
- combinational logic
- sequential logic
- logic gate
  - logic gate / design process
  - logic gate / logic gate to expression: hints ::@:: Work from the output to the input step-by-step. Use extra variables when needed, especially when dealing with an input connected to multiple outputs at different levels. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
- Boolean algebra
  - Boolean algebra / simplification: hints ::@:: You may need to think of new terms to add to the expression... And also you can use extra variables to replace variables that always appear together. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
- 2-bit comparator ::@:: 4 inputs, grouped into 2 groups of 2 inputs, each group representing a 2-bit unsigned integer. 3 outputs, respectively representing greater than, equal to, and less than. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
  - 2-bit comparator / hints ::@:: Consider each output separately. You can always use a truth table and its SOP to write the expression. SOP is especially suitable if given a PLA. <!--SR:!2025-02-27,4,327!2025-02-26,3,307-->
- 8-to-3 encoder ::@:: 8 inputs, in one-hot encoding. 3 outputs, representing an unsigned integer from 0 to 7. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
- 4-to-1 multiplexer ::@:: 4 inputs, representing the 4 channels to be muxed. 2 control signals, controlling which channel to output. 1 output. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
- multiplexer
  - multiplexer / input bit width ::@:: Its output bit width is the same as its input bit width. <!--SR:!2025-02-27,4,327!2025-02-27,4,327-->
  - multiplexer / control bit width ::@:: Given _n_ control bits, the _maximum_ number of inputs is 2<sup>_n_</sup>. <br/> Given _n_ inputs, the _minimum_ number of control bits is ceil\(log<sub>2</sub>\(_n_\)\). <p> (Of course, you can violate these, but then it is not a multiplexer, isn't it?) <!--SR:!2025-02-26,3,307!2025-02-27,4,327-->

## assignments

## midterm examination

## final examination

## aftermath

### total
