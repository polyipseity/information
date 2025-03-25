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
  - course learning outcomes (CLOs) ::@:: assembly language, digital logic, instruction set architecture (ISA), organizational paradigms, processor & memory <!--SR:!2025-04-21,54,310!2025-04-22,55,310-->
  - topics ::@:: brief digital circuit, data representation and arithmetic, instruction set architecture and assembly, computer architecture <!--SR:!2025-04-12,47,290!2025-03-28,32,270-->
    1. digital logic: combinational, sequential
    2. data representation: integer, fractional, character
    3. instruction set architecture (ISA)
    4. MIPS assembly language
    5. processor: datapath, control; pipeline
    6. memory system: cache, virtual memory

## children

- [MARS](MARS.md)
- [MIPS](MIPS.md)
<!-- - [questions](questions.md) -->

## week 1 lecture

- datetime: 2025-02-03T13:30:00+08:00/2025-02-03T14:50:00+08:00
- topic: course information, introduction
- logistics
- [numeral system](../../../../general/numeral%20system.md) ::@:: a mathematical notation for representing numbers of a given set, using digits or other symbols in a consistent manner <!--SR:!2025-04-24,57,310!2025-04-10,45,290-->
  - numeral system / common examples ::@:: binary (base 2; used by digital computers), octal (base 8), decimal (base 10; used by people), hexadecimal (base 16; concisely expresses a binary sequence), sexagesimal (base 60; used for timekeeping) <!--SR:!2025-04-21,54,310!2025-04-09,42,290-->
- [positional notation](../../../../general/positional%20notation.md) ::@:: (_d_<sub>_n_<!-- markdown separator -->−1</sub>..._d_<sub>0</sub>)<sub>_r_</sub> = _d_<sub>_n_<!-- markdown separator -->−1</sub> × _r_<sup>_n_<!-- markdown separator -->−1</sup> + ... + _d_<sub>0</sub> × _r_<sup>0</sup> , where _d_<sub>_i_</sub> is the _i_+1-th _least significant digit_ and _r_ is the _base_ or _radix_  <p> An extension to the above includes decimals by extending the positions to beyond the decimal point analogously. <!--SR:!2025-04-12,47,290!2025-04-22,55,310-->
  - positional notation / integral conversion ::@:: To convert from any base _a_ to any other base _b_, the simplest way _for humans_ is to convert it from base _a_ to base 10, and then from base 10 to base _b_. <p> To convert from base _a_ to base 10, use the positional notation definition. <p> To convert from base 10 to base _b_, keep doing round-toward-zero division by _b_ until the number is 0, keeping track of the remainders. Join the remainders to get the number in base _b_. The first remainder is the least significant digit. <!--SR:!2025-04-24,57,310!2025-04-22,55,310-->
- [binary number](../../../../general/binary%20number.md) (base 2) ::@:: a method for representing numbers that uses only two symbols for the natural numbers: typically "0" (zero) and "1" (one) <!--SR:!2025-04-22,55,310!2025-04-24,57,310-->
  - binary number / usage ::@:: It can model series of electrical signals computers use to represent information as a _bit sequence_, where "0" represents no/low voltage or off state and "1" represents presence/high voltage or on state. <!--SR:!2025-04-22,55,310!2025-04-10,43,290-->
- [byte § multiple-byte units](../../../../general/byte.md#multiple-byte%20units) ::@:: powers of 10: 1 B (byte), 1 kB (kilobyte) = 1000 B, 1 MB (megabyte) = 1000<sup>2</sup> B, 1 GB (gigabyte) = 1000<sup>3</sup> B, ... <br/> powers of 2: 1 B, 1 kiB (kibibyte) = 1024 B, 1 MiB (mebibyte) = 1024<sup>2</sup> B, 1 GiB (gibibyte) = 1024<sup>3</sup> B, ... <p> However, in practice... (very important!) <!--SR:!2025-04-08,41,290!2025-04-25,58,310-->
  - [byte § multiple-byte units](../../../../general/byte.md#multiple-byte%20units) / confusion ::@:: People frequently confuse the units for powers of 10 and powers of 2. In many contexts, the symbol for the units of powers of 10 are used to meant both, and which one it meant depends on the specific context. <p> In this course, when dealing with _size_, we mean the units of powers of 2. When dealing with _frequency_ or _rate_, we mean the units of powers of 10. In both cases, we use the symbol for the units of powers of 10, e.g. always use "kB". <!--SR:!2025-04-08,41,290!2025-05-24,73,270-->
- [classes of computers](../../../../general/classes%20of%20computers.md) ::@:: (in increasing power) embedded computers, personal computers, server computers, supercomputers <!--SR:!2025-04-10,45,290!2025-04-24,57,310-->
  - [personal computer](../../../../general/personal%20computer.md) ::@:: general purpose; many software; subject to cost—performance tradeoff <!--SR:!2025-04-25,58,310!2025-04-23,56,310-->
  - [server computer](../../../../general/server%20(computing).md) ::@:: network-based; high capacity, performance, reliability; ranges from small-sized to building-sized <!--SR:!2025-04-10,43,290!2025-07-15,113,290-->
  - [supercomputer](../../../../general/supercomputer.md) ::@:: high-end computers, often specialized for certain workloads, e.g. engineering, science; highest capabilities but very little market share <!--SR:!2025-04-09,44,290!2025-04-21,54,310-->
  - [embedded computer](../../../../general/embedded%20system.md) ::@:: hidden as components of systems; stringent constraints on cost, performance, power, etc. <!--SR:!2025-04-11,46,290!2025-04-10,45,290-->
- [abstraction layer](../../../../general/abstraction%20layer.md) ::@:: a way of hiding the working details of a subsystem. <!--SR:!2025-04-23,56,310!2025-04-25,58,310-->
  - abstraction layer / common computer layers ::@:: (from top to bottom) user, application, operating system, hardware <!--SR:!2025-04-09,42,290!2025-04-09,42,290-->
  - abstraction layer / application ::@:: written in high-level language <!--SR:!2025-04-21,54,310!2025-04-07,40,290-->
  - abstraction layer / operating system ::@:: compiler: high-level language to machine code; operating system: handle IO, manage memory and storage, manage resources, schedule tasks <!--SR:!2025-04-08,41,290!2025-04-25,58,310-->
  - abstraction layer / hardware ::@:: IO controllers, memory, processor <!--SR:!2025-04-24,57,310!2025-04-21,54,310-->
- [computer program](../../../../general/computer%20program.md) ::@:: a sequence or set of instructions in a programming language for a computer to execute <!--SR:!2025-04-09,42,290!2025-04-09,42,290-->
  - computer program / levels ::@:: (from top to bottom) high-level language, assembly language, machine code <!--SR:!2025-04-21,54,310!2025-04-22,55,310-->
  - computer program / high-level language ::@:: level of abstraction closer to the problem domain, so that you can work productivity and make the program more portable <!--SR:!2025-04-25,58,310!2025-04-08,41,290-->
  - computer program / assembly language ::@:: textual representation of instructions, in symbolic language <!--SR:!2025-04-25,58,310!2025-04-12,47,290-->
  - computer program / machine code ::@:: binary bits, which are encoded data or instructions <!--SR:!2025-04-22,55,310!2025-04-23,56,310-->
- abstraction layer
  - abstraction layer / necessity ::@:: It is impossible to understand computers by looking at every single transistor. Abstraction helps with coping with complexity. <!--SR:!2025-04-22,55,310!2025-04-25,58,310-->
  - abstraction layer / key ideas ::@:: Organize computer software and hardware into hierarchical layers. In a layer, details in the lower layers are hidden to simplify the current layer. Interactions between layers happen between well-defined interfaces. <p> An example is instruction set architecture (ISA), an interface between hardware and software. <!--SR:!2025-04-22,55,310!2025-04-24,57,310-->
- [instruction set architecture](../../../../general/instruction%20set%20architecture.md) (ISA) ::@:: an abstract model that generally defines how software controls the CPU in a computer or a family of computers <!--SR:!2025-04-23,56,310!2025-04-24,57,310-->
  - instruction set architecture / advantages ::@:: Allows your ISA code to run on different implementations of the ISA, e.g. different CPUs. <!--SR:!2025-04-24,57,310!2025-04-23,56,310-->
  - instruction set architecture / examples ::@:: ARM, MIPS, PowerPC, SPARC, x86 <!--SR:!2025-04-23,56,310!2025-04-23,56,310-->
- [computer](../../../../general/computer.md) ::@:: a machine that can be programmed to automatically carry out sequences of arithmetic or logical operations (computation) <!--SR:!2025-04-10,43,290!2025-04-25,58,310-->
  - computer / the very first computers ::@:: some uses punch cards as computer programs, very large (can be as large as a building), very low capabilities (compared to nowadays) <!--SR:!2025-04-21,54,310!2025-04-21,54,310-->
- [von Neumann architecture](../../../../general/von%20Neumann%20architecture.md) ::@:: control unit, processing unit, memory, storage, input/output mechanisms <p> in this course, 5 components: input, output, memory, processor (control + datapath) <!--SR:!2025-04-08,41,290!2025-04-27,48,250-->
  - von Neumann architecture / input ::@:: communicate with the computers; transfer data and instructions to the memory <!--SR:!2025-04-23,56,310!2025-04-24,57,310-->
  - von Neumann architecture / output ::@:: communicate with the users; transfer data from the memory <!--SR:!2025-04-21,54,310!2025-04-21,54,310-->
  - von Neumann architecture / memory ::@:: store to keep data and instructions <!--SR:!2025-04-25,58,310!2025-04-08,41,290-->
  - von Neumann architecture / processing unit (datapath) ::@:: unit to process data according to instructions <!--SR:!2025-04-09,42,290!2025-04-10,43,290-->
  - von Neumann architecture / control unit (control) ::@:: unit to control input, output, memory, and processing unit <!--SR:!2025-03-28,32,270!2025-04-10,43,290-->
- [information age](../../../../general/informaion%20age.md) ::@:: the agricultural revolution, then the industrial revolution, then the information revolution (computer revolution); thus we have the information age, and computers are pervasive <!--SR:!2025-04-23,56,310!2025-04-23,56,310-->
  - information age / why ::@:: one of the reasons: Moore's law: the number of transistors in an integrated circuit (IC) doubles about every two years <!--SR:!2025-04-25,58,310!2025-04-11,46,290-->
  - information age / applications ::@:: artificial intelligence, automobile computers, human genome project, search engines, world wide web <!--SR:!2025-04-09,44,290!2025-04-11,46,290-->
  - information age / trend ::@:: electronics technology continues to evolve due to increased capacity and reduced cost, e.g. vacuum tubes (1950s), transistors (1950, 1960s), integrated circuits (1960s, 1970s), very large scale integrated (VLSI) circuits (since 1980s) <!--SR:!2025-03-29,24,230!2025-04-28,49,250-->

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
    - positional notation / integral conversion / base 2, base 16 ::@:: 4 base 2 digits can be grouped together, which _directly_ corresponds to 1 base 16 digit, and vice versa. This can help ease conversion between these two bases. <p> Note that you may need to add or remove padding zeros to make the original or resulting base 2 number have digit count that is a multiple of 4. <!--SR:!2025-05-31,84,345!2025-05-31,84,345-->

## week 1 lecture 2

- datetime: 2025-02-07T09:00:00+08:00/2025-02-07T10:20:00+08:00
- topic: logic gates, truth table, logic function, multiplexor
- [analog signal](../../../../general/analog%20signal.md) ::@:: any continuous-time signal representing some other quantity; values vary over a broad range continuously <!--SR:!2025-05-31,84,345!2025-05-23,77,345-->
- [digital signal](../../../../general/digital%20signal.md) ::@:: a signal that represents data as a sequence of discrete values; at any given time it can only take on, at most, one of a finite number of values <!--SR:!2025-05-31,84,345!2025-05-31,84,345-->
  - digital signal / typical voltage ::@:: low/0: 0 V to 0.5 V; high/1: 2.4 V to 2.9 V; illegal: outside of the aforementioned ranges <!--SR:!2025-05-31,84,345!2025-05-31,84,345-->
- [bit](../../../../general/bit.md) ::@:: represents a logical state with one of two possible values <!--SR:!2025-05-31,84,345!2025-05-21,75,345-->
  - bit / applications in computers ::@:: instructions (e.g. operands, operations), number representations (e.g. floats, integers, rationals) <!--SR:!2025-05-31,84,345!2025-05-31,84,345-->
- [truth table](../../../../general/truth%20table.md) ::@:: a mathematical table used in logic—specifically in connection with Boolean algebra, Boolean functions, and propositional calculus—which sets out the functional values of logical expressions on each of their functional arguments, that is, for each combination of values taken by their logical variables; i.e. a table tha shows the _single_ (in this course, can be _multiple_) Boolean output of a function accepting _zero or more_ Boolean inputs <!--SR:!2025-05-22,76,345!2025-05-31,84,345-->
  - truth table / format ::@:: one column for each input and output; one row for each possible combination of inputs <!--SR:!2025-05-31,84,345!2025-04-14,44,325-->
- [Boolean algebra](../../../../general/Boolean%20algebra.md) ::@:: values: 0/true, 1/false; variables: can only take the aforementioned 2 values; operations: AND, NAND, NOR, NOT, OR, XOR <!--SR:!2025-05-31,84,345!2025-05-31,84,345-->
- [logic gate](../../../../general/logic%20gate.md) ::@:: a device that performs a Boolean function, a logical operation performed on one or more binary inputs that produces a single binary output <!--SR:!2025-05-31,84,345!2025-05-24,78,345-->
  - logic gate / basic examples ::@:: AND, NAND, NOR, NOT, OR, XOR <!--SR:!2025-05-31,84,345!2025-05-31,84,345-->
  - logic gate / NOT, inverter ::@:: $0 \mapsto 1; 1 \mapsto 0$ <br/> ${\overline {A} }$ or $\neg A$ <br/> ![NOT symbol](../../../../archives/Wikimedia%20Commons/NOT%20ANSI%20Labelled.svg) <!--SR:!2025-05-31,84,345!2025-05-31,84,345-->
  - logic gate / AND, conjunction ::@:: $(0, 0) \mapsto 0; (0, 1) \mapsto 0; (1, 0) \mapsto 0; (1, 1) \mapsto 1$ <br/> $A\cdot B$ or $A\land B$ <br/> ![AND symbol](../../../../archives/Wikimedia%20Commons/AND%20ANSI%20Labelled.svg) <!--SR:!2025-05-24,78,345!2025-05-21,75,345-->
  - logic gate / OR, disjunction ::@:: $(0, 0) \mapsto 0; (0, 1) \mapsto 1; (1, 0) \mapsto 1; (1, 1) \mapsto 1$ <br/> $A+B$ or $A\lor B$ <br/> ![OR symbol](../../../../archives/Wikimedia%20Commons/OR%20ANSI%20Labelled.svg) <!--SR:!2025-05-31,84,345!2025-05-31,84,345-->
  - logic gate / NAND, alternative denial ::@:: $(0, 0) \mapsto 1; (0, 1) \mapsto 1; (1, 0) \mapsto 1; (1, 1) \mapsto 0$ <br/> ${\overline {A\cdot B} }$ or $A\uparrow B$ <br/> ![NAND symbol](../../../../archives/Wikimedia%20Commons/NAND%20ANSI%20Labelled.svg) <!--SR:!2025-05-31,84,345!2025-05-08,61,325-->
  - logic gate / NOR, joint denial ::@:: $(0, 0) \mapsto 1; (0, 1) \mapsto 0; (1, 0) \mapsto 0; (1, 1) \mapsto 0$ <br/> ${\overline {A+B} }$ or $A\downarrow B$ <br/> ![NOR symbol](../../../../archives/Wikimedia%20Commons/NOR%20ANSI%20Labelled.svg) <!--SR:!2025-05-31,84,345!2025-05-25,79,345-->
  - logic gate / XOR, exclusive or ::@:: $(0, 0) \mapsto 0; (0, 1) \mapsto 1; (1, 0) \mapsto 1; (1, 1) \mapsto 0$ <br/> $A\oplus B$ or $A\veebar B$ <br/> ![XOR symbol](../../../../archives/Wikimedia%20Commons/XOR%20ANSI%20Labelled.svg) <!--SR:!2025-05-31,84,345!2025-05-31,84,345-->
  - logic gate / logic function ::@:: It is a function on binary variables whose output is also a binary variable. It can be represented by logic gates. AND, NOT, and OR are fundamental to all operations in modern computers. <!--SR:!2025-05-31,84,345!2025-05-31,84,345-->
    - logic gate / logic function / representations ::@:: graphics (e.g. Karnaugh map), logical expressions, truth table <!--SR:!2025-05-22,76,345!2025-05-31,84,345-->
  - logic gate / example ::@:: 1-bit half adder: given _A_ and _B_, outputs _S_ and _C_. _S_ = _A_ XOR _B_, _C_ = _A_ AND _B_. <p> So _S_ is interpreted as the resulting bit after addition, while _C_ is the carry bit (e.g. to be connected to another 1-bit half adder). <!--SR:!2025-05-23,77,345!2025-05-31,84,345-->
  - logic gate / circuit types ::@:: 2 main ones: combinational logic circuit, sequential logic circuit <!--SR:!2025-05-31,84,345!2025-05-25,79,345-->
- [combinational logic](../../../../general/combinational%20logic.md) ::@:: It has no memory. The outputs depend entirely on the _current_ inputs and noting else. It is essentially the same as a logic function, so can be represented by a truth table. <!--SR:!2025-05-31,84,345!2025-05-31,84,345-->
- [sequential logic](../../../../general/sequential%20logic.md) ::@:: It has memory. The outputs depend on the _current_ inputs and the _state_ (value stored in _memory_). That is, the output _additionally_ depends on the input history. <!--SR:!2025-05-31,84,345!2025-05-31,84,345-->
- [combinational logic](../../../../general/combinational%20logic.md)
  - [combinational logic](../../../../general/combinational%20logic.md) / circuits ::@:: e.g. multiplexor/demultiplexor, encoder/decoder, two-level logic, programmable logic array (PLA); these are higher-level basic building blocks that are commonly seen in combinational logic <!--SR:!2025-05-31,84,345!2025-05-31,84,345-->
- [multiplexer](../../../../general/multiplexer.md)/selector, demultiplexer ::@:: (former) a device that selects between several analog or digital input signals and forwards the selected input to a single output line <p> (latter) a device that takes a single input signal and selectively forwards it to one of several output lines <!--SR:!2025-05-31,84,345!2025-05-31,84,345-->
  - multiplexer / 2<sup>_n_</sup>-to-1 multiplexer ::@:: 2<sup>_n_</sup> data inputs, _n_ selection inputs, and 1 output <p> The _n_ selection inputs have 2<sup>_n_</sup> possible combinations. Each combination selects 1 data input and forwards it to the output. <!--SR:!2025-05-31,84,345!2025-05-31,84,345-->
    - multiplexer / 2<sup>_n_</sup>-to-1 multiplexer / implementation ::@:: Use an AND gate for each data input. Connect the data input to its corresponding AND gate. Then connect the _n_ selection inputs to the AND gates, adding NOT gates as needed, such that each unique combination of _n_ selection inputs makes exactly one AND gate possible to be made output 1 iff its corresponding input is 1. Finally, connect all the AND gates into 1 giant OR gate, and that is the output. <!--SR:!2025-05-31,84,345!2025-03-30,33,305-->

## week 2 lecture

- datetime: 2025-02-10T13:30:00+08:00/2025-02-10T14:50:00+08:00
- topic: decoder, two-level logic, programmable logic array
- [binary decoder](../../../../general/binary%20decoder.md), encoder ::@:: (former) a combinational logic circuit that converts binary information from the n coded inputs to a maximum of 2<sup>_n_</sup> unique outputs <p> (latter) does the reverse <!--SR:!2025-05-31,84,345!2025-05-31,84,345-->
  - binary decoder / _n_-to-2<sup>_n_</sup> decoder ::@:: _n_ data inputs, 2<sup>_n_</sup> data outputs <p> Each unique combination of inputs activates exactly one output. For machine learning people: This is just an _one hot_ encoder. <!--SR:!2025-05-31,84,345!2025-05-31,84,345-->
    - binary decoder / _n_-to-2<sup>_n_</sup> decoder / implementation ::@:: Use an AND gate for each data output. Connect the data output to its corresponding AND gate. Then connect the _n_ selection inputs to the AND gates, adding NOT gates as needed, such that each unique combination of _n_ selection inputs makes exactly one AND gate output 1. <!--SR:!2025-05-31,84,345!2025-05-31,84,345-->
- [logic gate](../../../../general/logic%20gate.md)
  - logic gate / design process ::@:: problem specification, truth table, logical expression, simplification, implementation <!--SR:!2025-05-31,84,345!2025-05-31,84,345-->
    - logic gate / design process / example ::@:: 3-people majority vote: output 1 if two or more inputs are 1, otherwise 0 <!--SR:!2025-05-31,84,345!2025-05-31,84,345-->
- [canonical normal form](../../../../general/canonical%20normal%20form.md) ::@:: Any Boolean function can be expressed as a disjunction (OR) of minterms or a conjunction (AND) of maxterms. <!--SR:!2025-06-14,92,362!2025-06-14,92,362-->
  - [minterm](../../../../general/canonical%20normal%20form.md#minterms) ::@:: For $n$ input variables, it is a product (AND) term in which each of the $n$ variables appears _exactly_ once (either in its complemented or uncomplemented form). <p> If you put this term as the output in a truth table for all possible _n_ inputs, you will see _exactly_ one row outputs 1. This is the key insight to how it works. <!--SR:!2025-06-09,88,362!2025-04-29,53,342-->
    - minterm / indexing ::@:: There are $2^n$ possible minterms. Assign the value 1 to the direct form \($x_{i}$\) and 0 to the complemented form \($x'_{i}$\) (these assignments are reversed for maxterm); the minterm is then $\sum \limits _{i=1}^{n}2^{i-1}\operatorname {value} (x_{i})$. <p> For example, minterm $abc'$ is numbered 110<sub>2</sub> = 6<sub>10</sub> and denoted $m_{6}$. <!--SR:!2025-06-06,85,362!2025-05-21,68,342-->
  - [maxterm](../../../../general/canonical%20normal%20form.md#maxterm) ::@:: For $n$ input variables, it is a sum (OR) term in which each of the $n$ variables appears _exactly_ once (either in its complemented or uncomplemented form). <p> If you put this term as the output in a truth table for all possible _n_ inputs, you will see _exactly_ one row outputs 0. This is the key insight to how it works. <!--SR:!2025-06-14,92,362!2025-06-04,83,362-->
    - maxterm / indexing ::@:: There are $2^n$ possible maxtems. Assign the value 0 to the direct form \($x_{i}$\) and 1 to the complemented form \($x'_{i}$\) (these assignments are reversed for minterm); the maxterm is then $\sum \limits _{i=1}^{n}2^{i-1}\operatorname {value} (x_{i})$. <p> For example, we assign the index 6 to the maxterm $a'+b'+c$ \(110\) and denote that maxterm as _M_<sub>6</sub>. The complement $(a'+b'+c)'$ is the minterm $abc'=m_{6}$, using [de Morgan's law](../../../../general/De%20Morgan's%20law.md). <!--SR:!2025-06-04,83,362!2025-04-17,40,322-->
  - two-level representation ::@:: A representation where every input is a variable or its complement, one level consists of AND only, and the other level consists of OR only. There are two forms: sum of products (SOP), product of sums (POS). <!--SR:!2025-06-14,92,362!2025-06-14,92,362-->
  - [minterm canonical form](../../../../general/canonical%20normal%20form.md#minterm%20canonical%20form), sum of products (SOP) ::@:: Given the truth table of a logical function, it is possible to write the function as a "sum of products" or "sum of minterms". This is a _two-level representation_. <p> The key insight is that since a minterm is 1 for _exactly_ one input possible combination, adding (OR) minterms appropriately can produce any truth table. This is done by adding (OR) the minterms for which the corresponding row in the given truth table outputs 1. <!--SR:!2025-04-29,53,342!2025-06-14,92,362-->
  - [maxterm canonical form](../../../../general/canonical%20normal%20form.md#maxterm%20canonical%20form), sum of products (SOP) ::@:: Given the truth table of a logical function, it is possible to write the function as a "product of sums" or "product of maxterms". This is a _two-level representation_. <p> The key insight is that since a maxterm is 0 for _exactly_ one input possible combination, multiplying (AND) maxterms appropriately can produce any truth table. This is done by multiplying (AND) the maxterms for which the corresponding row (note the variables are negated) in the given truth table outputs 0. <!--SR:!2025-05-07,60,342!2025-06-08,87,362-->
- [programmable logic array](../../../../general/progammable%20logic%20array.md) (PLA) ::@:: a kind of programmable logic device used to implement combinational logic circuits <!--SR:!2025-06-06,85,362!2025-06-07,86,362-->
  - programmable logic array (PLA) / description ::@:: It has 2<sup>N</sup> AND gates for N input variables, and for M outputs from the PLA, there should be M OR gates, each with programmable inputs from all of the AND gates. <p> Each AND gate represents a minterm. Each OR gate represents a sum of products. An optimization is that if a minterm will not be used, less AND gates are needed (in the lecture slides, the PLA example has 7 AND gates only for 3 inputs). <!--SR:!2025-06-14,92,362!2025-05-21,68,342-->
  - programmable logic array (PLA) / intuition ::@:: The AND plane consisting of 2<sup>N</sup> AND gates produce all possible minterms. The OR plane consisting of M gates produces the required M outputs, assembled from all possible minterms from the AND plane. <!--SR:!2025-06-07,86,362!2025-06-14,92,362-->
  - programmable logic array (PLA) / duality ::@:: Theoretically, product of sums (POS) could be used instead, with an OR plane generating all possible maxterms, connected to an AND plane generating the required outputs. <p> However, negations are needed when you convert a truth table to POS, which is more mentally demanding and less intuitive. So that is why this is not often seen in practice. <!--SR:!2025-06-05,84,362!2025-06-05,84,362-->

## week 2 lab

- datetime: 2025-02-11T15:00:00+08:00/2025-02-11T15:50:00+08:00
- status: unscheduled, no lab

## week 2 tutorial

- datetime: 2025-02-11T18:00:00+08:00/2025-02-11T18:50:00+08:00
- status: unscheduled, no tutorial

## week 2 lecture 2

- datetime: 2025-02-14T09:00:00+08:00/2025-02-14T10:20:00+08:00
- topic: logical equivalence, Boolean algebra, K-map
- [logical equivalence](../../../../general/logical%20equivalence.md) ::@:: Two statements are this if they have the same truth value in every model. <p> In the context of combinational logic, this means two Boolean functions have the same output for every combination of inputs. <!--SR:!2025-06-06,82,367!2025-06-06,82,367-->
  - logical equivalence / methods ::@:: logical expression, truth table <!--SR:!2025-06-18,92,367!2025-06-11,86,367-->
  - logical equivalence / truth table ::@:: Very easy to prove equivalence: Check if all rows are the same. However the number of rows grows exponentially: 2<sup>_n_</sup>. <!--SR:!2025-06-08,84,367!2025-06-19,93,367-->
  - logical equivalence / logical expression ::@:: They give a more concise way to express Boolean functions, especially ones with many input variables. However, it is not always obvious that two different expressions are the same logically, so we need to simplify the expressions using Boolean algebra or Karnaugh map. <!--SR:!2025-06-11,86,367!2025-06-17,91,367-->
- Boolean algebra
  - Boolean algebra / laws ::@:: Translate logical statements into mathematical symbols. Then these laws may be used to simplify the mathematical expression. Then get back simplified logical statements. <!--SR:!2025-06-20,94,367!2025-06-12,87,367-->
    - Boolean algebra / laws / identity laws ::@:: $$\begin{aligned} p \land \top & \equiv p \\ p \lor \bot & \equiv p \end{aligned}$$ <!--SR:!2025-06-12,87,367!2025-06-05,81,367-->
    - Boolean algebra / laws / domination laws (null laws) ::@:: $$\begin{aligned} p \lor \top & \equiv \top \\ p \land \bot & \equiv \bot \end{aligned}$$ <!--SR:!2025-06-12,87,367!2025-06-18,92,367-->
    - Boolean algebra / laws / idempotent or tautology laws ::@:: $$\begin{aligned} p \lor p & \equiv p \\ p \land p & \equiv p \end{aligned}$$ <!--SR:!2025-06-18,92,367!2025-06-12,87,367-->
    - Boolean algebra / laws / negation laws (inverse laws) ::@:: $$\begin{aligned} p \lor \lnot p & \equiv \top \\ p \land \lnot p & \equiv \bot \end{aligned}$$ <!--SR:!2025-06-11,86,367!2025-06-18,92,367-->
    - Boolean algebra / laws / [commutative laws](commutative%20property.md) ::@:: $$\begin{aligned} p\vee q & \equiv q\vee p \\ p\wedge q &\equiv q\wedge p \end{aligned}$$ <!--SR:!2025-06-07,83,367!2025-06-07,83,367-->
    - Boolean algebra / laws / [associative laws](associative%20property.md) ::@:: $$\begin{aligned} (p \lor q) \lor r & \equiv p \lor (q \lor r) \\ (p \land q) \land r & \equiv p \land (q \land r) \end{aligned}$$ <!--SR:!2025-06-14,89,367!2025-06-20,94,367-->
    - Boolean algebra / laws / [distributive laws](distributive%20property.md) ::@:: $$\begin{aligned} p \lor (q \land r) & \equiv (p \lor q) \land (p \lor r) \\ p \land (q \lor r) & \equiv (p \land q) \lor (p \land r) \end{aligned}$$ <!--SR:!2025-06-06,82,367!2025-06-18,92,367-->
    - Boolean algebra / laws / [absorption laws](absorption%20law.md) ::@:: $$\begin{aligned} p \lor (p \land q) & \equiv p \\ p \land (p \lor q) & \equiv p \end{aligned}$$ <!--SR:!2025-06-06,82,367!2025-06-17,91,367-->
    - Boolean algebra / laws / [De Morgan's laws](De%20Morgan's%20laws.md) ::@:: $$\begin{aligned} \lnot (p \land q) & \equiv \lnot p \lor \lnot q \\ \lnot (p \lor q) & \equiv \lnot p \land \lnot q \end{aligned}$$ <!--SR:!2025-06-19,93,367!2025-06-08,84,367-->
    - Boolean algebra / laws / [double negation](double%20negation.md) law ::@:: $$\neg (\neg p)\equiv p$$ <!--SR:!2025-06-11,86,367!2025-06-19,93,367-->
- [Karnaugh map](../../../../general/Karnaugh%20map.md) (K-map) ::@:: A diagram that can be used to simplify a Boolean algebra expression. <p> (Note: K-map for 5 variables or more exist.) <!--SR:!2025-06-18,92,367!2025-06-13,88,367-->
  - Karnaugh map / construction ::@:: The row and column indices (shown across the top and down the left side of the Karnaugh map) are ordered in Gray code rather than binary numerical order. Gray code ensures that only one variable changes between each pair of adjacent cells. Each cell of the completed Karnaugh map contains a binary digit representing the function's output for that combination of inputs (i.e. a minterm). <!--SR:!2025-06-07,83,367!2025-06-08,84,367-->
    - Karnaugh map / construction / 2 inputs ::@:: ![Karnaugh map for 2 inputs](../../../../archives/Wikimedia%20Commons/K-map%202x2%20empty.svg) <!--SR:!2025-06-13,88,367!2025-06-19,93,367-->
    - Karnaugh map / construction / 3 inputs ::@:: ![Karnaugh map for 3 inputs](../../../../archives/Wikimedia%20Commons/K-map%202x4%20empty.svg) <!--SR:!2025-06-06,82,367!2025-06-19,93,367-->
    - Karnaugh map / construction / 4 inputs ::@:: ![Karnaugh map for 4 inputs](../../../../archives/Wikimedia%20Commons/K-map%204x4%20empty.svg) <!--SR:!2025-06-20,94,367!2025-06-07,83,367-->
    - Karnaugh map / construction / 5 inputs ::@:: It is possible, but you will need to think in 3D. Stack 2 4×4 Karnaugh map vertically. It gets even harder for 6 inputs or more... <!--SR:!2025-06-14,89,367!2025-06-07,83,367-->
    - Karnaugh map / construction / torus ::@:: You should not use a torus in practice. This is simply to demonstrate how a K-map can be made into a torus: ![Karnaugh map for 4 inputs as a torus](../../../../archives/Wikimedia%20Commons/Karnaugh%20map%20torus.svg) <!--SR:!2025-06-14,89,367!2025-06-14,89,367-->
  - Karnaugh map / grouping ::@:: Group adjacent 1s in the diagram. The grid is toroidally connected (torus shaped), so _adjacent_ cells include wrapping across the edges of the diagram (left/right edge, top/bottom edge). That means groups can wrap across the edges. <!--SR:!2025-06-13,88,367!2025-06-13,88,367-->
    - Karnaugh map / grouping / rules ::@:: The union of all groups covers all 1s. <br/> Each group has a size that is a power of 2 (i.e. 1, 2, 4, 8, ...). <br/> Each group should be as large as possible, so that the resulting minterm has the least number of variables. <br/> Number of groups should be the fewest, so that the resulting SOP has the least number of minterms. <br/> Groups may overlap: make use of this extensively to make the groups as large as possible and cover all 1s with the least number of groups. <p> Note that the best grouping may not be unique. <!--SR:!2025-05-16,61,347!2025-05-16,61,347-->
  - Karnaugh map / solution ::@:: Each group corresponds to one minterm. It can be found by examining which variables stay the same within each box. Those that stay the same should be included, while those do not should be excluded. Intuitively, each term halves the grouping size. <p> Finally, add the minterms together to get a SOP. <!--SR:!2025-05-14,59,347!2025-06-17,91,367-->
  - Karnaugh map / inverse ::@:: Group adjacent 0s in the diagram instead. This produces a SOP for the inverse. Using De Morgan's laws, we can obtain a POS for the original function. <!--SR:!2025-05-14,59,347!2025-06-19,93,367-->
  - Karnaugh map / don't cares ::@:: Those cells are marked with a X. In that case, we can either cover or not cover them, choosing the one that gives the better grouping. <!--SR:!2025-06-17,91,367!2025-06-14,89,367-->
- [seven-segment display](../../../../general/seven-segment%20display.md) ::@:: It is a form of electronic display device for displaying decimal numerals that is an alternative to the more complex dot matrix displays. <p> Basically a display with a gray 8-shape with sharp corners, which have certain edges of the 8-shape activated (glowing) to show a decimal (0123456789)/hexadecimal (0123456789AbCdEF) digit. <!--SR:!2025-06-20,94,367!2025-06-20,94,367-->

## week 3 lecture

- datetime: 2025-02-17T13:30:00+08:00/2025-02-17T14:50:00+08:00
- topic: sequential logic, S-R latch, D latch, D flip-flop
- [flip-flop](../../../../general/flip-flop%20(electronics).md) ::@:: They are circuits that have two stable states that can store state information – a bistable multivibrator. The circuit can be made to change state by signals applied to one or more control inputs and will output its state (often along with its logical complement too). It is the basic storage element in sequential logic. <!--SR:!2025-05-18,66,347!2025-06-06,82,367-->
  - flip-flop / SR NOR latch ::@:: An unclocked/asynchronous memory element. Its 2 inputs are S (set) and R (reset). Its 2 outputs are Q (stored output) and its complement. It consists of two parallel NOR gates where the output of each NOR is also fanned out into one input of the other NOR. <!--SR:!2025-06-20,94,367!2025-05-10,59,347-->
    - flip-flop / SR NOR latch / symbol, figure ::@:: symbol: ![SR NOR latch symbol](../../../../archives/Wikimedia%20Commons/SR%20(NAND)%20Flip-flop.svg) <br/> figure: ![SR NOR latch figure](../../../../archives/Wikimedia%20Commons/R-S%20mk2.gif) <!--SR:!2025-05-17,66,347!2025-05-21,65,347-->
    - flip-flop / SR NOR latch / operations ::@:: hold/_quiescent_/latch state: If S and R are both 0, Q and its complement keep their previous outputs. <br/> set: If S is 1 and R is 0, Q becomes 1 and its complement becomes 0. <br/> unset: If S is 0 and R is 1, Q becomes 0 and its complement becomes 1. <br/> _forbidden/race condition_: S and R are not allowed to be both 1, as both outputs are now 0. Then, if S and R both goes to 0 _simultaneously_ afterwards, the outputs are metastable and may eventually lock at either 1 or 0 depending on the propagation time relations between the gates. <!--SR:!2025-04-09,34,327!2025-06-19,93,367-->
      - flip-flop / SR NOT latch / operations / note ::@:: __Important__: In this course, whenever you have something resembling a latch \(i.e. a circuit that has a latch state\) and you put it into an invalid state, we consider it a _race condition_. This is regardless even if you hold both inputs forever, in which both outputs \(or the one output if the complement is not outputted\) will remain 0 forever and no "racing" occurs. <p> This is because we consider if, whenever there is more than one path to go from the current state to the latch state \(note the inputs may not be all 0s in latch state\), whether the final outputs are always the same. If not, it is a race condition. <!--SR:!2025-04-04,23,371!2025-04-06,25,371-->
  - flip-flop / SR NAND latch ::@:: It is also possible to use NAND instead of NOR to make a SR latch. But it is more rare because the inputs' meaning are negated, i.e. the hold state requires both inputs to be 1. <!--SR:!2025-06-17,91,367!2025-06-18,92,367-->
  - flip-flop / SR AND-OR latch ::@:: It may be easier from a teaching point of view. See the figure and try to figure its mechanism yourself: ![SR AND-OR latch](../../../../archives/Wikimedia%20Commons/RS-and-or-flip-flop.png) <!--SR:!2025-06-12,87,367!2025-05-17,66,347-->
  - flip-flop / gated latches ::@:: Latches are designed to be _transparent_. That is, input signal changes cause immediate changes in output. Additional logic can be added to a transparent latch to make it _non-transparent_ or _opaque_ when another input (an "enable" input) is not asserted. <!--SR:!2025-06-11,86,367!2025-06-08,84,367-->
  - flip-flop / gated SR latch ::@:: Literally just an additionally "enable" input E AND-ing with the other 2 inputs. If E is 1, it works exactly as a SR latch. Otherwise, no action (hold state), no matter how the other 2 inputs are. <!--SR:!2025-06-14,89,367!2025-06-18,92,367-->
    - flip-flop / gated SR latch / symbol, figure ::@:: symbol: ![gated SR latch symbol](../../../../archives/Wikimedia%20Commons/Gated%20SR%20flip-flop%20Symbol.svg) <br/> figure: ![gated SR latch figure](../../../../archives/Wikimedia%20Commons/SR%20(Clocked)%20Flip-flop%20Diagram.svg) <!--SR:!2025-06-13,88,367!2025-06-12,87,367-->
  - flip-flop / gated D latch ::@:: This latch exploits the fact that, in the two active input combinations (01 and 10) of a gated SR latch, R is the complement of S. <p> So what we do is, on top of the gated SR latch, instead of having the inputs S and R, we have one input D (data) only, connecting to the (now internal) S an R inputs. Assuming E is 1. If D is 0, S is 0 and R is 1. Otherwise, S is 1 and R is 0. If E is 0, nothing happens, as in the gated SR latch. <p> When E is 1, it looks like the input D is being "written" into the gate memory, so D is called _data_. The "enable" input E is sometimes also called WE (write enable) instead for the same reason. <!--SR:!2025-04-10,35,327!2025-05-12,61,347-->
    - flip-flop / gated D latch / symbol, figure ::@:: symbol: ![gated D latch symbol](../../../../archives/Wikimedia%20Commons/Transparent%20Latch%20Symbol.svg) <br/> figure: ![gated D latch symbol](../../../../archives/Wikimedia%20Commons/D-type%20Transparent%20Latch%20(NOR).svg) <!--SR:!2025-04-09,34,327!2025-05-18,66,347-->
    - flip-flop / gated D latch / register ::@:: It stores a multi-bit value. A _n_-bit \(_this_\) can be implemented using _n_ gated D latches, all controlled by a common WE. Then when we want to write to the register, set WE to 1 and the _n_ D inputs to the desired data. <!--SR:!2025-05-20,64,347!2025-05-15,60,347-->
- [clock signal](../../../../general/clock%20signal.md) ::@:: It is an electronic logic signal (voltage or current) which oscillates between a high and a low state at a constant frequency and is used like a metronome to synchronize actions of digital circuits. <!--SR:!2025-06-19,93,367!2025-06-18,92,367-->
  - clock signal / synchronization ::@:: In a _synchronous_ logic circuit, the most common type of digital circuit, the clock signal is applied to all storage devices, flip-flops and latches, and causes them all to change state simultaneously, preventing race conditions. <p> In a computer, there are many types of circuits, and each take different time to complete (propagation delay). If we do not clock the circuits, then the outputs of circuits can change unpredictably. <p> A clock-less circuit is known as _asynchronous_ circuit, but it is much harder to design than _synchronous_ ones, and is out-of-scope for this course. <!--SR:!2025-06-11,86,367!2025-06-18,92,367-->
  - clock / terminology ::@:: A _clock_ is is a free-running signal with a fixed _cycle time_ (called _clock period_) or, equivalently, a fixed _clock frequency_ (i.e., inverse of the _cycle time_). _Edge-triggered clocking_ refers to state changes in a circuit on a clock (rising or falling) edge. <!--SR:!2025-06-07,83,367!2025-06-08,84,367-->
- [digital timing diagram](../../../../general/digital%20timing%20diagram.md) ::@:: It represents a set of signals in the time domain. A timing diagram can contain many rows, usually one of them being the clock. <!--SR:!2025-05-15,60,347!2025-06-07,83,367-->
  - digital timing diagram / conventions ::@:: Higher value is a logic one. Lower value is a logic zero. A slot showing a high and low is an either-or (such as on a data line). A Z indicates high impedance. A greyed out slot is a don't-care or indeterminate. <!--SR:!2025-06-13,88,367!2025-06-20,94,367-->
- flip-flop
  - flip-flop / latch vs. flip-flop ::@:: For the former, outputs can change any time the clock is asserted (high). For the latter, outputs can change only on a clock (rising or falling) edge. <!--SR:!2025-06-08,84,367!2025-05-14,59,347-->
  - flip-flop / D flip-flop ::@:: It is widely used, and known as a "data" flip-flop. It captures the value of the D-input at a definite portion of the clock cycle (such as the rising edge of the clock). That captured value becomes the Q output. At other times, the output Q does not change. It can be viewed as a memory cell, a zero-order hold, or a delay line. <!--SR:!2025-06-20,94,367!2025-06-07,83,367-->
    - flip-flop / D flip-flop / S, R inputs ::@:: Most D-type flip-flops in ICs have the capability to be forced to the set or reset state (which ignores the D and clock inputs), much like an SR flip-flop. Usually, the illegal S = R = 1 condition is resolved in D-type flip-flops. Setting S = R = 0 makes the flip-flop behave as described above. <p> In this course, our flip-flops do not have these inputs. <!--SR:!2025-06-12,87,367!2025-06-20,94,367-->
    - flip-flop / D flip-flop / symbol ::@:: ![D flip-flop symbol](../../../../archives/Wikimedia%20Commons/D-Type%20Flip-flop.svg) <!--SR:!2025-06-08,84,367!2025-04-10,35,327-->
  - flip-flop / master–slave edge-triggered D flip-flop ::@:: It is created by connecting two gated D latches in series, and inverting the enable input to one of them. It is called master–slave because the master latch controls the slave latch's output value Q and forces the slave latch to hold its value whenever the slave latch is enabled, as the slave latch always copies its new value from the master latch and changes its value only in response to a change in the value of the master latch and clock signal. <!--SR:!2025-05-16,61,347!2025-06-11,86,367-->
    - flip-flop / master–slave edge-triggered D flip-flop / diagrams ::@:: rising/positive edge: ![master–slave rising/positive-edge-triggered D flip-flop diagram](../../../../archives/Wikimedia%20Commons/D-Type%20Flip-flop%20Diagram.svg) <br/> falling/negative edge: ![master–slave falling/negative-edge-triggered D flip-flop diagram](../../../../archives/Wikimedia%20Commons/Negative-edge%20triggered%20master%20slave%20D%20flip-flop.svg) <!--SR:!2025-04-01,26,307!2025-05-13,58,347-->
    - flip-flop / master–slave edge-triggered D flip-flop / intuition ::@:: Using the falling/negative-edge-triggered variant as an example. When the clock is high, the first latch (master) has its WE as 1, so it is writable, while the second latch (slave) has its WE as 0, so its output remains unchanged. When the clock is low, the first latch (master) has its WE as 0, so it is not writeable, while the second latch (slave) has its WE as 1, so its output copies from the first latch (master). <p> We see that first latch (master) is only writable when the clock is high, while the output update takes place when the clock is low. When the clock falls from high to low, this is precisely when the latest input to the first latch (master) is saved and not affected by subsequent changes, while the second latch (slave) copies from the newly saved state of first latch (master). Thus it is falling/negative-edge-triggered. <!--SR:!2025-05-21,65,347!2025-05-11,60,347-->
- sequential logic
  - sequential logic / synchronous ::@:: In a sequential circuit, it remembers its state (a "snapshot"). When it is _additionally_ clocked, i.e. synchronous sequential circuit, we can treat its state as changing _on and only on_ each clock cycle. <!--SR:!2025-06-08,84,367!2025-06-11,86,367-->

## week 3 lab

- datetime: 2025-02-18T15:00:00+08:00/2025-02-18T15:50:00+08:00
- topic: introduction to Logisim, combinational circuits
- Logisim ::@:: It is an interactive graphical interface for designing, simulating digital logic circuit. (Runs on Java 5... ancient software?!?) <!--SR:!2025-06-14,89,367!2025-06-19,93,367-->
  - Logisim / download ::@:: <https://sourceforge.net/projects/circuit/> <!--SR:!2025-06-08,84,367!2025-06-14,89,367-->
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
  - logic gate / logic gate to expression: hints ::@:: Work from the output to the input step-by-step. Use extra variables when needed, especially when dealing with an output connected to multiple inputs at different levels. <!--SR:!2025-06-12,87,367!2025-06-08,84,367-->
- Boolean algebra
  - Boolean algebra / simplification: hints ::@:: You may need to think of new terms to add to the expression... And also you can use extra variables to replace variables that always appear together. <!--SR:!2025-06-19,93,367!2025-05-15,60,347-->
- 2-bit comparator ::@:: 4 inputs, grouped into 2 groups of 2 inputs, each group representing a 2-bit unsigned integer. 3 outputs, respectively representing greater than, equal to, and less than. <!--SR:!2025-06-06,82,367!2025-06-07,83,367-->
  - 2-bit comparator / hints ::@:: Consider each output separately. You can always use a truth table and its SOP to write the expression. SOP is especially suitable if given a PLA. <!--SR:!2025-06-08,84,367!2025-05-16,65,347-->
- 8-to-3 encoder ::@:: 8 inputs, in one-hot encoding. 3 outputs, representing an unsigned integer from 0 to 7. <!--SR:!2025-06-11,86,367!2025-06-20,94,367-->
- 4-to-1 multiplexer ::@:: 4 inputs, representing the 4 channels to be muxed. 2 control signals, controlling which channel to output. 1 output. <!--SR:!2025-06-13,88,367!2025-06-17,91,367-->
- multiplexer
  - multiplexer / input bit width ::@:: Its output bit width is the same as its input bit width. <!--SR:!2025-06-25,93,386!2025-06-25,93,386-->
  - multiplexer / control bit width ::@:: Given _n_ control bits, the _maximum_ number of inputs is 2<sup>_n_</sup>. <br/> Given _n_ inputs, the _minimum_ number of control bits is ceil\(log<sub>2</sub>\(_n_\)\). <p> (Of course, you can violate these, but then it is not a multiplexer, isn't it?) <!--SR:!2025-04-29,45,346!2025-06-05,73,366-->

## week 3 lecture 2

- datetime: 2025-02-21T09:00:00+08:00/2025-02-21T10:20:00+08:00
- topic: 2's complement, max, min, range
- [computer number format](../../../../general/computer%20number%20format.md) ::@:: It is the internal representation of numeric values in digital device hardware and software, such as in programmable computers and calculators. <!--SR:!2025-06-28,96,386!2025-06-27,95,386-->
  - computer number format / motivation ::@:: This is one of the ways to represent numbers using bits. We may want to know more: how about unsigned integers, fractions, and reals? And what are their representable ranges? And how to do arithmetic operations on them? <!--SR:!2025-06-02,74,366!2025-07-01,98,386-->
  - computer number format / bits ::@:: They are represented by a group of bits, i.e. a bit sequence. They are grouped from the right (least significant bits) to the left (most significant bits). <!--SR:!2025-06-25,93,386!2025-07-05,102,386-->
  - computer number format / unsigned integer ::@:: It is literally positional notation but with base 2. <!--SR:!2025-06-25,93,386!2025-07-02,99,386-->
    - computer number format / unsigned integer / range ::@:: _n_ bits: \[0, 2<sup>_n_</sup>−1\] <!--SR:!2025-07-03,100,386!2025-06-28,96,386-->
    - computer number format / unsigned integer / max ::@:: It has all bits set to 1. <!--SR:!2025-07-01,98,386!2025-06-29,97,386-->
    - computer number format / unsigned integer / min ::@:: It has all bits set to 0. <!--SR:!2025-07-04,101,386!2025-07-05,102,386-->
- [two's complement](../../../../general/two's%20complement.md) ::@:: It is the most common method of representing signed (positive, negative, and zero) integers on computers, and more generally, fixed point binary values. <p> We can do natural arithmetic on it without using special rules. <!--SR:!2025-06-30,97,386!2025-06-25,93,386-->
  - two's complement / sign bit ::@:: The most significant bit (MSB) is \(_this_\). If 0, then positive. If 1, then negative. <!--SR:!2025-06-09,76,366!2025-07-06,103,386-->
  - two's complement / nonnegative integers ::@:: Same as that for unsigned integers. Beware of the range though... in particular, the _sign bit_ is always 0. (Or you can use the _sign bit_ anyway; but when it is 1, the result after the whole procedure overflows and becomes a negative integer.) <!--SR:!2025-07-04,101,386!2025-06-30,97,386-->
  - two's complement / negative integers ::@:: Start with the absolute binary representation of the number, with the leading bit being a sign bit. (If the _sign bit_ is 1, the result after the whole procedure overflows (less accurately "underflows") and becomes a positive integer.) Then invert (or flip) all bits – changing every 0 to 1, and every 1 to 0. Finally, add 1 to the entire inverted number, ignoring any overflow. Accounting for overflow will produce the wrong value for the result. <!--SR:!2025-06-02,74,366!2025-05-07,49,346-->
  - two's complement / range ::@:: _n_ bits: \[−2<sup>_n_<!-- markdown separator -->−1</sup>, 2<sup>_n_<!-- markdown separator -->−1</sup>−1\] <!--SR:!2025-06-25,93,386!2025-06-29,97,386-->
  - two's complement / max ::@:: It has all bits set to 1 except for the sign bit, which is set to 0. <!--SR:!2025-07-05,102,386!2025-07-06,103,386-->
  - two's complement / min ::@:: It has all bits set to 0 except for the sign bit, which is set to 1. <!--SR:!2025-07-04,101,386!2025-07-01,98,386-->
    - two's complement / min / weirdness ::@:: Notice what happens if we try to negate the minimum integer. It becomes itself instead of actually negating. This is because its corresponding positive integer is not representable. <!--SR:!2025-06-02,74,366!2025-06-26,94,386-->
- [integer overflow](../../../../general/integer%20overflow.md) ::@:: It occurs when an arithmetic operation on integers attempts to create a numeric value that is outside of the range that can be represented with a given number of digits – either higher than the maximum or lower than the minimum representable value. <p> (_Important_: In this course, we also use "integer underflow", see below.) <!--SR:!2025-06-24,92,386!2025-06-30,98,386-->
  - integer overflow / integer underflow ::@:: The above definition of "integer overflow" refers to the ideal result being outside the representable range. <p> An alternative definition uses "integer overflow" to refer to the ideal result being _higher_ than the maximum representable integer, while using "integer underflow" to refer to the ideal result being _lower_ than the minimum representable integer. <p> (_Important_: In this course, we use the latter definition.) <!--SR:!2025-07-03,100,386!2025-07-02,99,386-->

## week 4 lecture

- datetime: 2025-02-24T13:30:00+08:00/2025-02-24T14:50:00+08:00
- topic: signed/unsigned number, floating point, IEEE754 examples
- two's complement
  - two's complement / sign extension ::@:: When turning a two's-complement number with a certain number of bits into one with more bits (e.g., when copying from a one-byte variable to a two-byte variable), the most-significant bit must be repeated in all the extra bits. Other examples include: right shift (but not left shift, the sign bit is shifted out as normal). <!--SR:!2025-04-05,24,371!2025-03-31,19,351-->
- [sign extension](../../../../general/sign%20extension.md) ::@:: the operation, in computer arithmetic, of increasing the number of bits of a binary number while preserving the number's sign (positive/negative) and value <!--SR:!2025-04-06,25,371!2025-04-04,23,371-->
  - sign extension / zero extension ::@:: Fill in the missing most-significant bits with zero, e.g. bitwise logical operations, up-casting unsigned integers, etc. <!--SR:!2025-04-05,24,371!2025-04-05,24,371-->
- [floating-point arithmetic](../../../../general/floating-point%20arithmetic.md)
  - floating-point arithmetic / motivation ::@:: To represent non-integral numbers, which includes fractions, very small numbers, and very large numbers. <!--SR:!2025-04-05,24,371!2025-04-06,25,371-->
  - floating-point arithmetic / representation ::@:: Roughly speaking, just like how we use a decimal point to represent non-integral numbers as decimal representation, computers use binary point to represent non-integral numbers as binary representation. <!--SR:!2025-04-05,24,371!2025-04-05,24,371-->
- [scientific notation](../../../../general/scientific%20notation.md) ::@:: a way of expressing numbers that are too large or too small to be conveniently written in decimal form, since to do so would require writing out an inconveniently long string of digits <!--SR:!2025-04-06,25,371!2025-04-05,24,371-->
  - scientific notation / form ::@:: Nonzero numbers are written in the form <p> _m_ × 10<sup>_n_</sup> <p> or _m_ times ten raised to the power of _n_, where _n_ is an [integer](../../../../general/integer.md), and the [coefficient](../../../../general/coefficient.md) _m_ is a nonzero [real number](../../../../general/real%20number.md) \(usually between 1 and 10 in absolute value, and nearly always written as a [terminating decimal](../../../../general/decimal.md)\). The integer _n_ is called the [exponent](../../../../general/exponent.md) and the real number _m_ is called the _[significand](../../../../general/significand.md)_ or _mantissa_ (not to be confused with that of the same name in floating-point arithmetic). <!--SR:!2025-04-04,23,371!2025-04-04,23,371-->
    - scientific notation / form / normalized ::@:: When _m_ is at least 1 and less than (_not_ equal to) 10. <p> For _binary_ representation, this means the leading digit is always 1. <!--SR:!2025-04-04,23,371!2025-04-06,25,371-->
- floating-point arithmetic
  - floating-point arithmetic / name ::@:: It is _floating_ because the binary point is not fixed (affected by the significand). <!--SR:!2025-04-04,23,371!2025-03-31,19,351-->
  - floating-point arithmetic / form ::@:: $$1.xxx \ldots xxx_2 \times 2^{yyy \ldots yyy_2} \,,$$ where $xxx \ldots xxx_2$ is the _significand_ or _mantissa_ (not to be confused with that of the same name in scientific notation) and $yyy \ldots yyy_2$ is the _exponent_. They have a fixed number of digits (bits). <!--SR:!2025-04-04,23,371!2025-04-05,24,371-->
  - floating-point arithmetic / distribution ::@:: Looking at its form, we can see that the distribution of floating-point numbers is not even. The density of representable numbers doubles/halves every time you cross a power of 2. <!--SR:!2025-04-04,23,371!2025-04-04,23,371-->
  - floating-point arithmetic / precision ::@:: The arithmetic is _approximate_ (i.e. not _exact_). Thus we say it has a finite range and _limited_ precision. <!--SR:!2025-04-06,25,371!2025-04-05,24,371-->
- [single-precision floating-point format](../../../../genral/single-precision%20floating-point%20format.md) (`float`) ::@:: 32-bit floating-point format, starting from the left (MSB) to the right (LSB): 1 sign bit, 8 exponent bits, and 23 significand bits (precision is 24 bits). <!--SR:!2025-04-04,23,371!2025-04-05,24,371-->
  - single-precision floating-point format / precision ::@:: about 7 significant _decimal_ digits (6 to 9) <!--SR:!2025-04-06,25,371!2025-04-06,25,371-->
  - single-precision floating-point format / exponent range ::@:: 2<sup>−126</sup> ≈ 10<sup>−38</sup> to 2<sup>+127</sup> ≈ 10<sup>+38</sup> <!--SR:!2025-04-06,25,371!2025-04-06,25,371-->
  - single-precision floating-point format
- [double-precision floating-point format](../../../../genral/double-precision%20floating-point%20format.md) (`double`) ::@:: 64-bit floating-point format, starting from the left (MSB) to the right (LSB): 1 sign bit, 11 exponent bits, and 52 significand bits (precision is 53 bits). <!--SR:!2025-04-06,25,371!2025-04-05,24,371-->
  - double-precision floating-point format / precision ::@:: about 16 significant _decimal_ digits (15 to 17) <!--SR:!2025-04-06,25,371!2025-04-06,25,371-->
  - double-precision floating-point format / exponent range ::@:: 2<sup>−1026</sup> ≈ 10<sup>−308</sup> to 2<sup>+1027</sup> ≈ 10<sup>+308</sup> <!--SR:!2025-04-06,25,371!2025-04-04,23,371-->
    - double-precision floating-point format / exponent range / mnemonic ::@:: Compare the exponents with that of single-precision... notice that "0" is inserted as the 2nd digit. Hmm... <!--SR:!2025-04-05,24,371!2025-04-04,23,371-->
- [IEEE 754](../../../../general/IEEE%20754.md) ::@:: a technical standard for floating-point arithmetic originally established in 1985 by the Institute of Electrical and Electronics Engineers \(IEEE\) <!--SR:!2025-04-06,25,371!2025-04-04,23,371-->
  - IEEE 754 / history (brief) ::@:: It was developed in response to divergence of representations, which can cause portability issues for scientific code. Now it is almost universally adopted. <!--SR:!2025-04-06,25,371!2025-04-05,24,371-->
  - IEEE 754 / representations ::@:: single precision (32-bit), double precision (64-bit), ... (there are much more not covered in this course) <!--SR:!2025-04-06,25,371!2025-04-04,23,371-->

## week 4 lab

- datetime: 2025-02-25T15:00:00+08:00/2025-02-25T15:50:00+08:00
- topic: building sequential logics with Logisim
- Logisim
  - Logisim / magnification ::@:: Use magnification to help you connect wires and draw graphics. <!--SR:!2025-04-05,24,371!2025-04-05,24,371-->
  - Logisim / wire color ::@:: Light green means 1. Dark green means 0. Any other color means connection problem. <!--SR:!2025-04-05,24,371!2025-04-06,25,371-->
  - Logisim / auto build ::@:: Given a logical expression, it can build a circuit for you. You can convert a truth table into an expression using SOP (or POS). <!--SR:!2025-04-04,23,371!2025-04-06,25,371-->
- flip-flop
  - flip-flop / SR NOR latch
  - flip-flop / SR NAND latch
  - flip-flop / gated D latch
- clock
- flip-flop
  - flip-flop / master–slave edge-triggered D flip-flop
  - flip-flop / gated D latch
    - flip-flop / gated D latch / register

## week 4 tutorial

- datetime: 2025-02-25T18:00:00+08:00/2025-02-25T18:50:00+08:00
- topic: sequential logic circuit
- combinational logic
- sequential logic
- clock
  - clock / terminology
- flip-flop
  - flip-flop / SR NAND latch
- flip-flop
  - flip-flop / gated D latch
  - flip-flop / master–slave edge-triggered D flip-flop
- [register file](../../../../general/register%20file.md) ::@:: an array of processor registers in a central processing unit (CPU) <!--SR:!2025-04-06,25,371!2025-04-05,24,371-->
  - register file / implementation ::@:: fast static RAMs with multiple ports <!--SR:!2025-04-05,24,371!2025-04-04,23,371-->
- [counter](../../../../general/counter%20(digital).md) ::@:: a device which stores (and sometimes displays) the number of times a particular event or process has occurred, often in relationship to a clock <!--SR:!2025-04-04,23,371!2025-04-05,24,371-->
  - counter / synchronous 2-bit counter ::@:: The counter has 2 gated D latches, each linked to an output. The output cycles through 00, 01, 10, and 11. Its input has the clock only.  <p> The 2 required combinational logic gates are the NOT gate and XOR gate. <!--SR:!2025-04-06,25,371!2025-04-06,25,371-->
    - counter / synchronous 2-bit counter / hints ::@:: truth table/transition table → K-map → logic simplification → circuit design <!--SR:!2025-04-04,23,371!2025-04-06,25,371-->

## week 4 lecture 2

- datetime: 2025-02-28T09:00:00+08:00/2025-02-28T10:20:00+08:00
- topic: IEEE754 rational: implicit 1, biased exponent, range, precision, special cases
- IEEE 754
  - IEEE 754 / format ::@:: It is composed of 3 parts, in order from MSB to LSB: a _sign_, an _exponent_, and then a _significand_. <!--SR:!2025-04-05,24,371!2025-04-05,24,371-->
    - IEEE 754 / format / input ::@:: Inputs required to design a IEEE 754 format: a base _b_ that is either 2 or 10 (for simplicity, __we only consider _b_ = 2 henceforth__), a precision _p_, and an exponent range from _emin_ to _emax_ (inclusive) satisfying _emin_ = −(_emax_ − 1) = 1 − _emax_. <!--SR:!2025-04-06,25,371!2025-05-27,66,371-->
    - IEEE 754 / format / number ::@:: We have 3 types of numbers: signed finite numbers (including two signed zeros), two infinities, and two kinds of NaN (not-a-number): a quiet NaN (qNaN) and a signaling NaN (sNaN). <!--SR:!2025-04-04,23,371!2025-04-06,25,371-->
    - IEEE 754 / format / finite numbers ::@:: _s_ = a sign that is either 0 or 1, <br/> _c_ = a _significand_ that is an _integer_ from 0 to _b_<sup>_p_</sup>−1 (at most _p_ base-_b_ digits), and <br/> _q_ = an _exponent_ such that _emin_ ≤ _q_ + _p_ − 1 ≤ _emax_. <br/> The numerical value of such a finite number is \(−1\)<sup>_s_</sup> × _c_ × _b_<sup>_q_</sup>. <p> Equivalently, _q_ = an _exponent_ such that _emin_ ≤ _q_ ≤ _emax_. <br> The numerical value of such a finite number is \(−1\)<sup>_s_</sup> × \(_c_ × _b_<sup>1 − _p_</sup>\) × _b_<sup>_q_</sup>, where \(_c_ × _b_<sup>1 − _p_</sup>\) can be interpreted as _c_ but the decimal point is right after the first digit. This latter definition more closely matches the actual binary representation. We will __use this latter definition henceforth__. <!--SR:!2025-04-25,36,331!2025-05-07,46,351-->
    - IEEE 754 / format / sign bit ::@:: 0 is nonnegative, 1 is negative. This is obvious. <!--SR:!2025-04-04,23,371!2025-04-04,23,371-->
    - IEEE 754 / format / significand bits ::@:: Given precision _p_ (number of digits), we could just simply have _p_ bits directly corresponding to the _p_ digits of _c_. However, we have a problem: 0 have many different representations, two (due to the sign bit) for each combination of exponent bits. <p> To avoid this, we use the _implicit bit convention_: the first digit of _c_ is always 1, except when representing 0 \(and subnormal numbers\). 0 is represented by the significand bits and exponent bits being all 0s. <!--SR:!2025-04-04,23,371!2025-05-10,51,351-->
      - IEEE 754 / format / significand bits / implicit bit ::@:: This has two advantages: We now only have two representations for 0. And we can represent _p_ digits with only _p_ − 1 bits! The disadvantage is now we have _subnormal numbers_ (the other being named _normal numbers_) when the exponent bits are all 0s but not the significand bits, which has a precision less than _p_ depending on the value (and some other things mentioned below). <!--SR:!2025-04-04,23,371!2025-04-05,24,371-->
    - IEEE 754 / format / exponent bits ::@:: Usually we decide the exponent range from the number of bits instead of the other way around. Given _n_ exponent bits, we have 2<sup>_n_</sup> combinations. For _normal numbers_, the exponent bits are not all 0s (_subnormal numbers_) and not all 1s (_infinities_ and _NaNs_). So we only have 2<sup>_n_</sup> − 2 combinations left. <p> Then the range is \[−(2<sup>_n_ − 1</sup> − 2), 2<sup>_n_ − 1</sup> − 1\]. The exponent bits are _biased_. <!--SR:!2025-04-04,23,371!2025-04-05,24,371-->
      - IEEE 754 / format / exponent bits / bias ::@:: An actual exponent of 0 is represented by all bits 1 except for the MSB, which is 0. From this, we derive a _bias_, which is 2<sup>_n_ − 1</sup> − 1. <p> This can be interpreted as: interpreting the exponent bits as an _unsigned_ integer, _subtracting_ it by the _bias_ gives the actual exponent; or the exponent bits as an _unsigned_ integer stores the actual exponent _plus_ the _bias_. <p> Its advantage is that floating-point numbers of the _same sign_ can be compared directly as if they are unsigned integers (if the sign bit is 1, the ordering is reversed). <!--SR:!2025-04-04,23,371!2025-04-04,23,371-->
    - IEEE 754 / format / infinity ::@:: The signed infinities are represented by setting the exponent bits to all 1s and the significand bits to all 0s. <p> The sign bit determines if it is positive or negative. <!--SR:!2025-04-04,23,371!2025-04-05,24,371-->
    - IEEE 754 / format / NaN ::@:: NaNs are represented by setting the exponent bits to all 1s and the significand bits to _not_ all 0s. <p> The sign bit is ignored by most applications. <!--SR:!2025-04-04,23,371!2025-04-05,24,371-->
      - IEEE 754 / format / NaN / quiet, signaling ::@:: If the most significant significand bit is 0, it is _signaling_. If it is 1, it is _quiet_. The remaining bits (and rarely the sign bit) is a _payload_ that can store anything. For signaling NaNs, the payload cannot be all 0s or else it becomes an infinity. <p> The above convention (0 is signal, 1 is quiet) means one can silence a signaling NaN into a quiet NaN by simply setting the most significant significand bit to 1. The reverse convention _may_ convert a signaling NaN to an infinity instead if the payload is all 0s. <!--SR:!2025-04-06,25,371!2025-03-31,19,351-->
  - IEEE 754 / conversion from a number ::@:: (for humans) Write the number in terms of _normalized_ scientific notation in base _b_ for the significand. Set the sign bit directly, the exponent bits (remember to add the bias), and the significant bits (discarding the leading implicit 1). Finally, check that the resulting format represents a finite (normal) number instead of special numbers \(may include subnormal numbers depending on the context\). Otherwise, the number to be represented is out of range. <!--SR:!2025-04-05,24,371!2025-03-31,19,351-->
- single-precision floating-point format
  - single-precision floating-point format / range \(zero, normal\) ::@:: in absolute value (i.e. discard sign): 0, \[1×2<sup>–126</sup> ≈ 1.2×10<sup>–38</sup>, (2−2<sup>−23</sup>)×2<sup>+127</sup> ≈ 3.4×10<sup>+38</sup>\] (figure out the representations yourself) <!--SR:!2025-04-05,24,371!2025-04-06,25,371-->
  - single-precision floating-point format / range \(subnormal\) ::@:: in absolute value (i.e. discard sign): \[2<sup>−23</sup>×2<sup>–126</sup> ≈ 1.4×10<sup>–45</sup>, (1−2<sup>−23</sup>)×2<sup>–126</sup> ≈ 1.2×10<sup>–38</sup>\] (figure out the representations yourself) <!--SR:!2025-05-11,52,351!2025-03-31,19,351-->
- double-precision floating-point format
  - double-precision floating-point format / range \(zero, normal\) ::@:: in absolute value (i.e. discard sign): 0, \[1×2<sup>–1022</sup> ≈ 2.2×10<sup>–308</sup>, (2−2<sup>−52</sup>)×2<sup>+1023</sup> ≈ 1.8×10<sup>+308</sup>\] (figure out the representations yourself) <!--SR:!2025-03-31,19,351!2025-04-26,37,331-->
  - double-precision floating-point format / range \(subnormal\) ::@:: in absolute value (i.e. discard sign): \[2<sup>−52</sup>×2<sup>–1022</sup> ≈ 4.9×10<sup>–324</sup>, (1−2<sup>−52</sup>)×2<sup>–1022</sup> ≈ 2.2×10<sup>–308</sup>\] (figure out the representations yourself) <!--SR:!2025-04-05,24,371!2025-03-31,19,351-->
- [arithmetic underflow](../../../../general/arithmetic%20underflow.md) ::@:: It is a condition in a computer program where the result of a calculation is a number of more precise absolute value than the computer can actually represent in memory on its central processing unit (CPU). <p> The exponent becomes too small (slides: negative exponent becomes too large) to fit in the exponent field. This is not the same as a number becoming too negative, which is arithmetic overflow instead. <!--SR:!2025-04-04,23,371!2025-04-04,23,371-->
  - arithmetic underflow / arithmetic overflow ::@:: Similar to integer overflow. The (slides: positive) exponent becomes too large to fit in the exponent field. Equivalently, the number becomes too negative or too positive. <!--SR:!2025-04-06,25,371!2025-04-05,24,371-->
  - arithmetic underflow / integer ::@:: First, see above discussion of "integer underflow" in integer overflow. <p> Unlike "integer underflow", arithmetic underflow is _not_ used like how "integer underflow" is used relative to "integer overflow". That is, arithmetic underflow never refers to a number becoming too negative. <!--SR:!2025-04-06,25,371!2025-04-04,23,371-->
- [normal number](../../../../general/normal%20number%20(computing).md) ::@:: It is a normal number is a non-zero number in a floating-point representation which is within the balanced range supported by a given floating-point format: it is a floating point number that can be represented without leading zeros in its significand. <!--SR:!2025-04-05,24,371!2025-04-06,25,371-->
- [subnormal number](../../../../general/subnormal%20number.md) ::@:: They fill the underflow gap around zero in floating-point arithmetic. Any non-zero number with magnitude smaller than the smallest positive normal number is _subnormal_, while _denormal_ can also refer to numbers outside that range. <!--SR:!2025-04-05,24,371!2025-04-04,23,371-->
  - subnormal number / significand ::@:: Note that the leading _implicit_ bit is now 0 instead of 1. This is the defining characteristic. <!--SR:!2025-04-06,25,371!2025-04-05,24,371-->
  - subnormal number / exponent ::@:: Note that the actual exponent for subnormal numbers is as if the exponent bits has an unsigned value of 1 instead of being all 0s, even though the exponent bits are actually all 0s. <!--SR:!2025-04-06,25,371!2025-04-05,24,371-->
  - subnormal number / issues ::@:: They fill the underflow gap with _evenly_ spaced values, instead of being _logarithmically_ spaced like normal numbers. <p> Some system handle these numbers much more slowly than normal numbers. <!--SR:!2025-04-06,25,371!2025-04-05,24,371-->
- IEEE 754
  - IEEE 754 / format
    - IEEE 754 / format / infinity
      - IEEE 754 / format / infinity / usage ::@:: It can be used in subsequent calculations, which avoids need for checking overflows. <!--SR:!2025-04-04,23,371!2025-04-04,23,371-->
    - IEEE 754 / format / NaN
      - IEEE 754 / format / NaN / usage ::@:: It can be used in subsequent calculations, which avoids need for illegal checking illegal or undefined operations, e.g. dividing 0 by 0. <!--SR:!2025-04-05,24,371!2025-04-04,23,371-->
- [ASCII](../../../../general/ASCII.md) ::@:: It is a character encoding standard for electronic communication, used by most computers today. <p> It is a 7-bit code, so there are 128 code points. Each unsigned integer maps to a character. But most of time we use an unsigned byte, which has 8 bits, to represent a character with the MSB set to 0. <!--SR:!2025-04-04,23,371!2025-04-06,25,371-->
  - ASCII / full name ::@:: American Standard Code for Information Interchange <!--SR:!2025-04-05,24,371!2025-04-06,25,371-->
  - ASCII / patterns ::@:: Some notable patterns: <br/> Alphabets (A to Z, a to z) and numbers (0 to 9) are in order. <br/> groups: NUL (null) → control characters → punctuations → numbers → punctuations → big alphabets → punctuations → small alphabets → punctuations → DEL (a control character) <!--SR:!2025-04-20,32,331!2025-04-04,23,371-->
  - ASCII / note ::@:: How can 128 code points store all characters? This is why we have _Unicode_, but Unicode is much more complicated and involves a variable number of bytes to encode a character. It will not be covered here. <!--SR:!2025-04-06,25,371!2025-04-05,24,371-->

## week 5 lecture

- datetime: 2025-03-03T13:30:00+08:00/2025-03-03T14:50:00+08:00
- topic: basic instructions, register, memory operand
- instruction set architecture
  - instruction set architecture / analogy as a language ::@:: Words are _instructions_. A vocabulary (set of all words\) is an _instruction set_. Programmers write in _assembly language_. After assembly by an _assembler_, it becomes _machine language_, which hardware can understand. <!--SR:!2025-03-29,14,364!2025-04-11,25,384-->
  - instruction set architecture / specifications ::@:: addressing modes, exception handling, external I/O, native data types, instructions, interrupt handling, memory architecture, opcodes \(machine language\), registers <!--SR:!2025-05-12,48,364!2025-04-03,17,364-->
  - instruction set architecture / vs. assembly language ::@:: The former is a public interface to processors implementing this ISA. The latter is simply a programming language. <p> Ideally, a ISA should have a corresponding language. In practice, there are variations. They are defined by the assembler. <!--SR:!2025-04-10,24,384!2025-04-10,24,384-->
  - instruction set architecture / advantages
    - instruction set architecture / advantages / compatibility ::@:: Hardware changes will \(usually\) not impact existing programs: no re-programming is required. Hardware improvement can be made as long as it conforms to the ISA. <!--SR:!2025-04-11,25,384!2025-04-12,26,384-->
  - instruction set architecture / examples
- [reduced instruction set computer](../../../../general/reduced%20instruction%20set%20computer.md) \(RISC\) ::@:: It is a computer architecture designed to simplify the individual instructions given to the computer to accomplish tasks. <!--SR:!2025-04-10,24,384!2025-04-11,25,384-->
  - reduced instruction set computer / comparison ::@:: Compared to the instructions given to a complex instruction set computer (CISC), a RISC computer might require more instructions (more code) in order to accomplish a task because the individual instructions are written in simpler code. <!--SR:!2025-04-10,24,384!2025-04-12,26,384-->
  - reduced instruction set computer / advantages ::@:: Easy to learn and understand. Have a large share of the embedded computers market. Less instructions. <!--SR:!2025-04-11,25,384!2025-04-11,25,384-->
  - reduced instruction set computer / principles ::@:: good compromises, make common cases fast, simplicity favors regularity \(less cases\), smaller is faster <!--SR:!2025-04-11,25,384!2025-04-12,26,384-->
- [MIPS architecture](../../../../general/MIPS%20architecture.md) ::@:: It is the RISC that we will learn here. <p> It was a research project conducted by John L. Hennessy at Stanford University between 1981 and 1984. Then it was commercialized and developed by MIPS Technologies. <!--SR:!2025-04-12,26,384!2025-04-12,26,384-->
  - MIPS architecture / full name ::@:: Microprocessor without Interlocked Pipeline Stages <!--SR:!2025-04-10,24,384!2025-04-12,26,384-->
  - MIPS architecture / reference ::@:: MIPS reference data green card <!--SR:!2025-04-11,25,384!2025-04-12,26,384-->
  - [MIPS](MIPS.md)
    - [§ principles](MIPS.md#principles)
    - [§ arithmetic instructions](MIPS.md#arithmetic%20instructions): `add`, `sub`, `addi`
    - [§ instructions](MIPS.md#instructions)
    - [§ registers](MIPS.md#registers)
    - [§ memory](MIPS.md#memory)
    - [§ data instructions](MIPS.md#data%20instructions): `lw`, `sw`
    - [§ endianness](MIPS.md#endianness)
    - [§ operands](MIPS.md#operands)
    - [§ bitwise instructions](MIPS.md#bitwise%20instructions): `and`, `or`, `nor`, `andi`, `ori`, `sll`, `srl`

## week 5 lab

- datetime: 2025-03-04T15:00:00+08:00/2025-03-04T15:50:00+08:00
- topic: building registers
- [processor register](../../../../general/processor%20register.md) ::@:: a quickly accessible location available to a computer's processor <!--SR:!2025-04-12,26,384!2025-04-10,24,384-->
  - processor register / implementation
    - processor register / implementation / 2-bit register ::@:: Have 2 D flip-flops. Connect the same clock signal to both of them. Split the 2-bit data inputs via a "splitter", and connect each to a D flip-flop. Combine their output as 2-bit data outputs via a "combiner". <!--SR:!2025-04-10,24,384!2025-04-03,17,364-->
      - processor register / implementation / 2-bit register / write enabled ::@:: Add a muxer that selects between the current input and the current output. The 2 D flip-flops inputs are now provided by the muxer instead of the current input. Add a write enabled \(WE\) input that connects to the muxer to select the appropriate muxer input. <!--SR:!2025-04-12,26,384!2025-04-10,24,384-->
- register file
  - register file / implementation ::@:: The idea is that we have several registers, and a register file has an input to select which register to use. <p> Have several registers. Connect the same clock signal to all registers. Add an input that selects a register for both writing and reading. Add a decoder that uses the register selection to write-enable _exactly one_ of the registers. Add a muxer that uses the register selection to select the output of _exactly one_ of the registers. <!--SR:!2025-03-26,11,344!2025-04-12,26,384-->
    - register file / implementation / extensions ::@:: We could separate the register selection for writing and reading. We could also add a write-enable input. <!--SR:!2025-04-12,26,384!2025-04-11,25,384-->

## week 5 tutorial

- datetime: 2025-03-04T18:00:00+08:00/2025-03-04T18:50:00+08:00
- topic: base conversion, integer representation
- positional notation
  - positional notation / integral conversion
    - positional notation / integral conversion / base 2, base 16
- [hexadecimal](../../../../general/hexadecimal.md)
  - hexadecimal / notations ::@:: In mathematics, a subscript is typically used to specify the base. For example, the decimal value 711 would be expressed in hexadecimal as 2C7<sub>16</sub>. \(A rarely seen notation is 2C7<sub>hex</sub>.\) In programming, several notations denote hexadecimal numbers, usually involving a prefix. The prefix `0x` is used in [C](c%20(programming%20language).md), which would denote this value as `0x2C7`. <p> In writing, we may express it as 2C7<sub>(16)</sub>, so that the base is distinguished from the number even with bad handwriting <small>\(e.g. me\)</small>. <!--SR:!2025-04-12,26,384!2025-04-10,24,384-->
- [signed number representations](../../../../general/signed%20number%20representations.md) ::@:: In mathematics, negative numbers in any base are represented by prefixing them with a minus sign ("−"). However, in RAM or CPU registers, numbers are represented only as sequences of bits, without extra symbols. <!--SR:!2025-04-12,26,384!2025-04-12,26,384-->
  - [sign–magnitude](../../../../general/signed%20number%20representations.md#sign–magnitude) ::@:: The sign bit is 0 if positive, 1 if negative. The magnitude is represented by the remaining bits. <p> examples: IEEE 754 _significand_ field <!--SR:!2025-04-12,26,384!2025-04-11,25,384-->
    - sign–magnitude / addition ::@:: If the signs are the same, add the magnitude. If the signs are different, subtract the larger magnitude from the smaller magnitude. The sign is the same as the number with the larger magnitude. <!--SR:!2025-04-10,24,384!2025-04-12,26,384-->
    - sign–magnitude / disadvantages ::@:: Arithmetic is complex, so are the circuits to implement it. <!--SR:!2025-04-11,25,384!2025-04-10,24,384-->
  - signed number representations / systems ::@:: sign–magnitude, offset binary, one's complement, two's complement, etc. <!--SR:!2025-04-12,26,384!2025-04-12,26,384-->
- [one's complement](../../../../general/one's%20complement.md) ::@:: It of a binary number is the value obtained by inverting (flipping) all the bits in the binary representation of the number. The sign bit is 0 if the number is positive, 1 if negative. <!--SR:!2025-04-12,26,384!2025-04-11,25,384-->
  - one's complement / naming ::@:: The name "ones' complement" refers to the fact that such an inverted value, if added to the original, would always produce an "all ones" number (the term "complement" refers to such pairs of mutually additive inverse numbers, here in respect to a non-0 base number). <!--SR:!2025-04-10,24,384!2025-04-11,25,384-->
  - one's complement / addition ::@:: Adding two values is straightforward. Simply align the values on the least significant bit and add, propagating any carry to the bit one position left. If the carry extends past the end of the word it is said to have "wrapped around", a condition called an "_end-around carry_". When this occurs, the bit must be added back in at the right-most bit. This phenomenon does not occur in two's complement arithmetic. <!--SR:!2025-04-03,17,364!2025-04-11,25,384-->
  - one's complement / subtraction ::@:: Subtraction is similar, except that borrows, rather than carries, are propagated to the left. If the borrow extends past the end of the word it is said to have "wrapped around", a condition called an "_end-around borrow_". When this occurs, the bit must be subtracted from the right-most bit. This phenomenon does not occur in two's complement arithmetic. <p> An alternative is using the [method of complements](../../../../general/method%20of%20complements.md) to implement subtraction. For example, subtracting −5 from 15 is just adding 5 to 15. <!--SR:!2025-04-11,25,384!2025-05-05,42,364-->
  - one's complement / advantages ::@:: Arithmetic is simpler \(slightly more complex than two's complement\), so are the circuits to implement it. Negation is always possible. <!--SR:!2025-04-11,25,384!2025-04-10,24,384-->
  - one's complement / disadvantages ::@:: Zero is signed \(this may be an advantage in some scenarios\). Addition and subtraction requires _end-around_ carrying and _end-around_ borrowing respectively. <!--SR:!2025-03-28,13,364!2025-04-11,25,384-->
- [two's complement](../../../../general/two's%20complement.md)
  - two's complement / addition ::@:: Adding two's complement numbers requires no special processing even if the operands have opposite signs; the sign of the result is determined automatically. Simply align the values on the least significant bit and add, propagating any carry to the bit one position left. If the carry extends past the end of the word, discard it. <p> This actually reflects the [ring](../../../../general/ring%20(mathematics).md) structure on all integers [modulo](../../../../general/modular%20arithmetic.md) [2<sup>_N_</sup>](../../../../general/power%20of%20two.md): $\mathbb {Z} /2^{N}\mathbb {Z}$. <!--SR:!2025-04-12,26,384!2025-04-10,24,384-->
  - two's complement / subtraction ::@:: Computers usually use the [method of complements](../../../../general/method%20of%20complements.md) to implement subtraction. For example, subtracting −5 from 15 is just adding 5 to 15. <!--SR:!2025-04-12,26,384!2025-04-10,24,384-->
  - two's complement / advantages ::@:: Arithmetic is simpler \(even simpler than one's complement\), so are the circuits to implement it. Zero is unsigned \(this may be an disadvantage in some scenarios\). <!--SR:!2025-04-10,24,384!2025-04-11,25,384-->
  - two's complement / disadvantages ::@:: Negation is not possible for the most negative number. <!--SR:!2025-04-12,26,384!2025-04-12,26,384-->
- integer overflow
  - integer overflow / integer underflow
- [offset binary](../../../../general/offset%20binary.md) ::@:: \(untaught\) It is a method for [signed number representation](signed%20number%20representation.md) where a signed number _n_ is represented by the bit pattern corresponding to the unsigned number _n_+_K_, _K_ being the _biasing value_ or _offset_. <p> examples: IEEE 754 _exponent_ field \(_K_ = 2<sup>_n_<!-- markdown separator -->−1</sup> − 1\) <!--SR:!2025-04-10,24,384!2025-04-12,26,384-->
  - offset binary / value of _K_ ::@:: There is no standard for offset binary, but most often the _K_ for an _n_-bit binary word is _K_ = 2<sup>_n_<!-- markdown separator -->−1</sup> \(for example, the offset for a four-digit binary number would be 2<sup>3</sup>=8\). This has the consequence that the minimal negative value is represented by all-zeros, the "zero" value is represented by a 1 in the most significant bit and zero in all other bits, and the [maximal positive value](../../../../general/integer%20overflow.md) is represented by all-ones \(conveniently, this is the same as using [two's complement](../../../../general/two's%20complement.md) but with the most significant bit inverted\). <p> For IEEE 754, unusually however, instead of using "excess 2<sup>_n_<!-- markdown separator -->−1</sup>" it uses "excess 2<sup>_n_<!-- markdown separator -->−1</sup> − 1" which means that inverting the leading (high-order) bit of the exponent will not convert the exponent to correct two's complement notation. <!--SR:!2025-04-12,26,384!2025-04-12,26,384-->
  - offset binary / advantages ::@:: In a logical comparison operation, one gets the same result as with a true form numerical comparison operation, whereas, in two's complement notation a logical comparison will agree with true form numerical comparison operation if and only if the numbers being compared have the same sign. Otherwise the sense of the comparison will be inverted, with all negative values being taken as being larger than all positive values. <!--SR:!2025-04-11,25,384!2025-04-10,24,384-->

## week 5 lecture 2

- datetime: 2025-03-07T09:00:00+08:00/2025-03-07T10:20:00+08:00
- topic: first MIPS program, MIPS Control Flow, branch, loop
- MIPS architecture
  - [MIPS](MIPS.md)
    - [§ assembly](MIPS.md#assembly)
    - [§ assembly format](MIPS.md#assembly%20format)
    - [§ assembly directives](MIPS.md#assembly%20directives): `.data`, `.align`, `.ascii`, `.asciiz`, `.byte`, `.word`, `.double`, `.text`, `.globl`
    - [§ pseudo-instructions](MIPS.md#pseudo-instructions): `la`
    - [§ entry point](MIPS.md#entry%20point)
    - [§ control flow](MIPS.md#control%20flow)
    - [§ jump instructions](MIPS.md#jump%20instructions): `beq`, `bne`, `j`

## week 6 lecture

- datetime: 2025-03-10T13:30:00+08:00/2025-03-10T14:50:00+08:00
- topic: `slt`, `jr`
- MIPS architecture
  - [MIPS](MIPS.md)
    - [§ control flow](MIPS.md#control%20flow)
    - [§ comparison instructions](MIPS.md#comparison%20instructions): `slt`, `slti`
    - [§ jump instructions](MIPS.md#jump%20instructions): `jr`

## week 6 lab

- datetime: 2025-03-11T15:00:00+08:00/2025-03-11T15:50:00+08:00
- topic: introduction to MARS, MIPS syscall services
- MARS ::@:: It is a GUI-based MIPS emulator designed for use in education, specifically for use with Hennessy's _Computer Organization and Design_. (Runs on Java 8... slightly less ancient software...) <!--SR:!2025-04-14,24,388!2025-04-14,24,388-->
  - MARS / architecture ::@:: MARS opens an assembly program into its memory. Then the memory is manipulated using a simulated MIPS processor. The processor can additionally interact with a console I/O window through I/O. <p> For debugging, MARS provides data segment window, register window, messages window, and text segment window. <!--SR:!2025-04-14,24,388!2025-04-14,24,388-->
  - MARS / download ::@:: <https://computerscience.missouristate.edu/mars-mips-simulator.htm> <!-- <https://courses.missouristate.edu/KenVollmar/MARS/> --> \(GitHub: <https://github.com/dpetersanderson/MARS/>\) <!--SR:!2025-04-14,24,388!2025-04-14,24,388-->
  - MARS / installation
  - MARS / usage
  - MARS / windows :;@:: console I/O window, data segment window, register window, messages window, text segment window
    - MARS / windows / console I/O window
    - MARS / windows / data segment window ::@:: It shows the data segment in the memory, which stores your data \(`.data`\). By default, it starts from 0x1001&nbsp;0000, goes upward in address. Static data is stored first, and then dynamic data. When more space is needed for dynamic data, it grows upwards in address. <!--SR:!2025-04-14,24,388!2025-04-14,24,388-->
    - MARS / windows / register window
    - MARS / windows / messages window
    - MARS / windows / text segment window ::@:: It shows the text segment in the memory, which stores your program \(`.text`\). By default, it starts from 0x0040&nbsp;0000, and goes upward in address. <!--SR:!2025-04-14,24,388!2025-04-14,24,388-->
- [system call](../../../../general/system%20call.md) ::@:: It is the programmatic way in which a computer program requests a service from the operating system on which it is executed. This may include hardware-related services \(for example, accessing a hard disk drive or accessing the device's camera\), creation and execution of new processes, and communication with integral kernel services such as process scheduling. System calls provide an essential interface between a process and the operating system. <!--SR:!2025-04-14,24,388!2025-04-14,24,388-->
- MARS
  - MARS / system call
  - [MARS](MARS.md)
    - [§ system calls](MIPS.md#system%20calls): `print_int` \(must know\), `print_float`, `print_double`, `print_string` \(must know\), `read_int` \(must know\), `read_float`, `read_double`, `read_string`, `sbrk`, `exit` \(must know\)
- MIPS architecture
  - [MIPS](MIPS.md)
    - [§ pseudo-instructions](MIPS.md#pseudo-instructions): `la`, `li`
  
## week 6 tutorial

- datetime: 2025-03-11T18:00:00+08:00/2025-03-11T18:50:00+08:00
- topic: floating point number representation, character
- single-precision floating-point format
  - single-precision floating-point format / conversion from decimal ::@:: First, write the decimal in scientific notation, with the significand in base 2. Normalize the scientific notation. <p> Write the sign bit, with positive being 0 and negative being 1. Write the exponent bits by addig the bias to the exponent, and representing it as an unsigned integer. Write the significand bits by discarding the leading 1 digit and writing the remaining digits verbatim, zero-padding at the end if necessary. <p> Finally, check if the resulting format represents a finite (normal) number instead of special numbers \(may include subnormal numbers depending on the context\). Otherwise, the decimal is out of range. <p> If the decimal requires too many digits to be written \(more than the number of significand bits, ignoring the implicit leading 1\), then the conversion is inexact. \(this course: we also say such a decimal is not representable\) <!--SR:!2025-04-08,18,368!2025-03-30,11,348-->
- double-precision floating-point format

## week 6 lecture 2

- datetime: 2025-03-14T09:00:00+08:00/2025-03-14T10:20:00+08:00
- topic: machine code
- MIPS architecture
  - [MIPS](MIPS.md)
    - [§ encoding](MIPS.md#encoding)
    - [§ arithmetic instructions](MIPS.md#arithmetic%20instructions): `addu`, `subu`
    - [§ data instructions](MIPS.md#data%20instructions): `lb`, `lbu`, `sb`
    - [§ pseudo-instructions](MIPS.md#pseudo-instructions): `not`
    - [§ bitwise instructions](MIPS.md#bitwise%20instructions): `nor`, `sllv`, `srlv`
- [stored-program computer](../../../../general/stored-program%20computer.md) ::@:: It is a computer that stores program instructions in electronically, electromagnetically, or optically accessible memory. This contrasts with systems that stored the program instructions with plugboards or similar mechanisms. <p> The definition is often extended with the requirement that the treatment of programs and data in memory be interchangeable or uniform. <!--SR:!2025-04-14,24,388!2025-04-14,24,388-->
  - stored-program computer / examples ::@:: Instructions and data are both represented by binary. They can be both stored in memory. Programs can operate on programs. Binary compatibility \(e.g. ISA\) allows programs to work on different computers. <!--SR:!2025-04-14,24,388!2025-04-14,24,388-->

## assignments

## midterm examination

## final examination

## aftermath

### total
