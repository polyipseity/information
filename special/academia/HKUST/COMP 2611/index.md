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
  - flashcard/active/special/academia/HKUST/COMP_2611
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
  - course learning outcomes (CLOs) ::@:: assembly language, digital logic, instruction set architecture (ISA), organizational paradigms, processor & memory <!--SR:!2025-12-13,235,330!2025-12-14,236,330-->
  - topics ::@:: brief digital circuit, data representation and arithmetic, instruction set architecture and assembly, computer architecture <!--SR:!2025-10-14,185,310!2026-12-12,497,310-->
    1. digital logic: combinational, sequential
    2. data representation: integer, fractional, character
    3. instruction set architecture (ISA)
    4. MIPS assembly language
    5. processor: datapath, control; pipeline
    6. memory system: cache, virtual memory

## children

- [MARS](MARS.md)
- [MIPS](MIPS.md)
- [assignments](assignments/index.md)
<!-- - [questions](questions.md) -->

## week 1 lecture

- datetime: 2025-02-03T13:30:00+08:00/2025-02-03T14:50:00+08:00
- topic: course information, introduction
- logistics
- [numeral system](../../../../general/numeral%20system.md) ::@:: a mathematical notation for representing numbers of a given set, using digits or other symbols in a consistent manner <!--SR:!2025-12-28,248,330!2027-11-02,759,330-->
  - numeral system / common examples ::@:: binary (base 2; used by digital computers), octal (base 8), decimal (base 10; used by people), hexadecimal (base 16; concisely expresses a binary sequence), sexagesimal (base 60; used for timekeeping) <!--SR:!2025-12-12,234,330!2027-09-20,725,330-->
- [positional notation](../../../../general/positional%20notation.md) ::@:: (_d_<sub>_n_<!-- markdown separator -->−1</sub>..._d_<sub>0</sub>)<sub>_r_</sub> = _d_<sub>_n_<!-- markdown separator -->−1</sub> × _r_<sup>_n_<!-- markdown separator -->−1</sup> + ... + _d_<sub>0</sub> × _r_<sup>0</sup> , where _d_<sub>_i_</sub> is the _i_+1-th _least significant digit_ and _r_ is the _base_ or _radix_  <p> An extension to the above includes decimals by extending the positions to beyond the decimal point analogously. <!--SR:!2025-10-15,186,310!2025-12-13,235,330-->
  - positional notation / integral conversion ::@:: To convert from any base _a_ to any other base _b_, the simplest way _for humans_ is to convert it from base _a_ to base 10, and then from base 10 to base _b_. <p> To convert from base _a_ to base 10, use the positional notation definition. <p> To convert from base 10 to base _b_, keep doing round-toward-zero division by _b_ until the number is 0, keeping track of the remainders. Join the remainders to get the number in base _b_. The first remainder is the least significant digit. <!--SR:!2025-12-21,241,330!2025-12-14,236,330-->
- [binary number](../../../../general/binary%20number.md) (base 2) ::@:: a method for representing numbers that uses only two symbols for the natural numbers: typically "0" (zero) and "1" (one) <!--SR:!2025-12-16,238,330!2025-12-29,249,330-->
  - binary number / usage ::@:: It can model series of electrical signals computers use to represent information as a _bit sequence_, where "0" represents no/low voltage or off state and "1" represents presence/high voltage or on state. <!--SR:!2025-12-14,236,330!2027-10-26,754,330-->
- [byte § multiple-byte units](../../../../general/byte.md#multiple-byte%20units) ::@:: powers of 10: 1 B (byte), 1 kB (kilobyte) = 1000 B, 1 MB (megabyte) = 1000<sup>2</sup> B, 1 GB (gigabyte) = 1000<sup>3</sup> B, ... <br/> powers of 2: 1 B, 1 kiB (kibibyte) = 1024 B, 1 MiB (mebibyte) = 1024<sup>2</sup> B, 1 GiB (gibibyte) = 1024<sup>3</sup> B, ... <p> However, in practice... (very important!) <!--SR:!2027-02-07,508,310!2026-01-01,251,330-->
  - [byte § multiple-byte units](../../../../general/byte.md#multiple-byte%20units) / confusion ::@:: People frequently confuse the units for powers of 10 and powers of 2. In many contexts, the symbol for the units of powers of 10 are used to meant both, and which one it meant depends on the specific context. <p> In this course, when dealing with _size_, we mean the units of powers of 2. When dealing with _frequency_ or _rate_, we mean the units of powers of 10. In both cases, we use the symbol for the units of powers of 10, e.g. always use "kB". <!--SR:!2027-08-19,700,330!2026-03-10,279,290-->
- [classes of computers](../../../../general/classes%20of%20computers.md) ::@:: (in increasing power) embedded computers, personal computers, server computers, supercomputers <!--SR:!2027-11-13,768,330!2025-12-25,245,330-->
  - [personal computer](../../../../general/personal%20computer.md) ::@:: general purpose; many software; subject to cost—performance tradeoff <!--SR:!2025-12-31,250,330!2025-12-18,239,330-->
  - [server computer](../../../../general/server%20(computing).md) ::@:: network-based; high capacity, performance, reliability; ranges from small-sized to building-sized <!--SR:!2027-03-12,530,310!2026-10-17,458,310-->
  - [supercomputer](../../../../general/supercomputer.md) ::@:: high-end computers, often specialized for certain workloads, e.g. engineering, science; highest capabilities but very little market share <!--SR:!2027-11-01,759,330!2025-12-10,232,330-->
  - [embedded computer](../../../../general/embedded%20system.md) ::@:: hidden as components of systems; stringent constraints on cost, performance, power, etc. <!--SR:!2027-11-25,777,330!2027-11-08,764,330-->
- [abstraction layer](../../../../general/abstraction%20layer.md) ::@:: a way of hiding the working details of a subsystem. <!--SR:!2025-12-23,244,330!2026-01-04,254,330-->
  - abstraction layer / common computer layers ::@:: (from top to bottom) user, application, operating system, hardware <!--SR:!2026-12-16,494,310!2027-09-22,728,330-->
  - abstraction layer / application ::@:: written in high-level language <!--SR:!2025-12-12,234,330!2027-08-09,692,330-->
  - abstraction layer / operating system ::@:: compiler: high-level language to machine code; operating system: handle IO, manage memory and storage, manage resources, schedule tasks <!--SR:!2027-02-09,508,310!2026-01-03,253,330-->
  - abstraction layer / hardware ::@:: IO controllers, memory, processor <!--SR:!2025-12-27,247,330!2025-12-13,235,330-->
- [computer program](../../../../general/computer%20program.md) ::@:: a sequence or set of instructions in a programming language for a computer to execute <!--SR:!2027-09-23,727,330!2027-09-07,715,330-->
  - computer program / levels ::@:: (from top to bottom) high-level language, assembly language, machine code <!--SR:!2025-12-12,234,330!2025-12-16,238,330-->
  - computer program / high-level language ::@:: level of abstraction closer to the problem domain, so that you can work productivity and make the program more portable <!--SR:!2025-12-30,249,330!2027-08-17,698,330-->
  - computer program / assembly language ::@:: textual representation of instructions, in symbolic language <!--SR:!2025-12-27,246,330!2025-10-17,188,310-->
  - computer program / machine code ::@:: binary bits, which are encoded data or instructions <!--SR:!2025-12-15,237,330!2025-12-24,245,330-->
- abstraction layer
  - abstraction layer / necessity ::@:: It is impossible to understand computers by looking at every single transistor. Abstraction helps with coping with complexity. <!--SR:!2025-12-14,236,330!2025-12-28,247,330-->
  - abstraction layer / key ideas ::@:: Organize computer software and hardware into hierarchical layers. In a layer, details in the lower layers are hidden to simplify the current layer. Interactions between layers happen between well-defined interfaces. <p> An example is instruction set architecture (ISA), an interface between hardware and software. <!--SR:!2025-12-16,238,330!2025-12-20,240,330-->
- [instruction set architecture](../../../../general/instruction%20set%20architecture.md) (ISA) ::@:: an abstract model that generally defines how software controls the CPU in a computer or a family of computers <!--SR:!2025-12-16,237,330!2025-12-19,239,330-->
  - instruction set architecture / advantages ::@:: Allows your ISA code to run on different implementations of the ISA, e.g. different CPUs. <!--SR:!2025-12-30,250,330!2025-12-25,246,330-->
  - instruction set architecture / examples ::@:: ARM, MIPS, PowerPC, SPARC, x86 <!--SR:!2025-12-15,236,330!2025-12-14,235,330-->
- [computer](../../../../general/computer.md) ::@:: a machine that can be programmed to automatically carry out sequences of arithmetic or logical operations (computation) <!--SR:!2027-09-28,731,330!2025-12-24,243,330-->
  - computer / the very first computers ::@:: some uses punch cards as computer programs, very large (can be as large as a building), very low capabilities (compared to nowadays) <!--SR:!2025-12-11,233,330!2025-12-10,232,330-->
- [von Neumann architecture](../../../../general/von%20Neumann%20architecture.md) ::@:: control unit, processing unit, memory, storage, input/output mechanisms <p> in this course, 5 components: input, output, memory, processor \(control + datapath\) <!--SR:!2027-08-12,694,330!2025-10-15,168,270-->
  - von Neumann architecture / input ::@:: communicate with the computers; transfer data and instructions to the memory <!--SR:!2025-12-22,243,330!2025-12-31,251,330-->
  - von Neumann architecture / output ::@:: communicate with the users; transfer data from the memory <!--SR:!2025-12-12,234,330!2025-12-11,233,330-->
  - von Neumann architecture / memory ::@:: store to keep data and instructions <!--SR:!2025-12-29,248,330!2027-08-13,695,330-->
  - von Neumann architecture / processing unit (datapath) ::@:: unit to process data according to instructions <!--SR:!2027-09-03,710,330!2027-10-28,755,330-->
  - von Neumann architecture / control unit (control) ::@:: unit to control input, output, memory, and processing unit <!--SR:!2026-12-20,505,310!2027-10-16,746,330-->
- [information age](../../../../general/informaion%20age.md) ::@:: the agricultural revolution, then the industrial revolution, then the information revolution (computer revolution); thus we have the information age, and computers are pervasive <!--SR:!2025-12-13,234,330!2025-12-19,240,330-->
  - information age / why ::@:: one of the reasons: Moore's law: the number of transistors in an integrated circuit (IC) doubles about every two years <!--SR:!2026-01-05,255,330!2027-12-12,791,330-->
  - information age / applications ::@:: artificial intelligence, automobile computers, human genome project, search engines, world wide web <!--SR:!2027-10-27,755,330!2027-11-26,777,330-->
  - information age / trend ::@:: electronics technology continues to evolve due to increased capacity and reduced cost, e.g. vacuum tubes (1950s), transistors (1950, 1960s), integrated circuits (1960s, 1970s), very large scale integrated (VLSI) circuits (since 1980s) <!--SR:!2026-01-15,206,250!2026-11-10,435,270-->

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
    - positional notation / integral conversion / base 2, base 16 ::@:: 4 base 2 digits can be grouped together, which _directly_ corresponds to 1 base 16 digit, and vice versa. This can help ease conversion between these two bases. <p> Note that you may need to add or remove padding zeros to make the original or resulting base 2 number have digit count that is a multiple of 4. <!--SR:!2026-07-02,393,365!2026-07-13,404,365-->

## week 1 lecture 2

- datetime: 2025-02-07T09:00:00+08:00/2025-02-07T10:20:00+08:00
- topic: logic gates, truth table, logic function, multiplexor
- [analog signal](../../../../general/analog%20signal.md) ::@:: any continuous-time signal representing some other quantity; values vary over a broad range continuously <!--SR:!2026-07-07,398,365!2026-05-29,359,365-->
- [digital signal](../../../../general/digital%20signal.md) ::@:: a signal that represents data as a sequence of discrete values; at any given time it can only take on, at most, one of a finite number of values <!--SR:!2026-07-15,406,365!2026-07-15,406,365-->
  - digital signal / typical voltage ::@:: low/0: 0 V to 0.5 V; high/1: 2.4 V to 2.9 V; illegal: outside of the aforementioned ranges <!--SR:!2026-07-14,405,365!2026-07-10,401,365-->
- [bit](../../../../general/bit.md) ::@:: represents a logical state with one of two possible values <!--SR:!2026-07-12,403,365!2026-05-24,354,365-->
  - bit / applications in computers ::@:: instructions (e.g. operands, operations), number representations (e.g. floats, integers, rationals) <!--SR:!2026-07-13,404,365!2026-07-14,405,365-->
- [truth table](../../../../general/truth%20table.md) ::@:: a mathematical table used in logic—specifically in connection with Boolean algebra, Boolean functions, and propositional calculus—which sets out the functional values of logical expressions on each of their functional arguments, that is, for each combination of values taken by their logical variables; i.e. a table tha shows the _single_ (in this course, can be _multiple_) Boolean output of a function accepting _zero or more_ Boolean inputs <!--SR:!2026-05-31,361,365!2026-07-04,395,365-->
  - truth table / format ::@:: one column for each input and output; one row for each possible combination of inputs <!--SR:!2026-07-14,405,365!2025-10-28,197,345-->
- [Boolean algebra](../../../../general/Boolean%20algebra.md) ::@:: values: 0/true, 1/false; variables: can only take the aforementioned 2 values; operations: AND, NAND, NOR, NOT, OR, XOR <!--SR:!2026-07-15,406,365!2026-07-15,406,365-->
- [logic gate](../../../../general/logic%20gate.md) ::@:: a device that performs a Boolean function, a logical operation performed on one or more binary inputs that produces a single binary output <!--SR:!2026-07-12,403,365!2026-06-05,366,365-->
  - logic gate / basic examples ::@:: AND, NAND, NOR, NOT, OR, XOR <!--SR:!2026-07-09,403,365!2026-07-13,404,365-->
  - logic gate / NOT, inverter ::@:: $0 \mapsto 1; 1 \mapsto 0$ <br/> ${\overline {A} }$ or $\neg A$ <br/> ![NOT symbol](../../../../archives/Wikimedia%20Commons/NOT%20ANSI%20Labelled.svg) <!--SR:!2026-07-11,402,365!2026-07-09,400,365-->
  - logic gate / AND, conjunction ::@:: $(0, 0) \mapsto 0; (0, 1) \mapsto 0; (1, 0) \mapsto 0; (1, 1) \mapsto 1$ <br/> $A\cdot B$ or $A\land B$ <br/> ![AND symbol](../../../../archives/Wikimedia%20Commons/AND%20ANSI%20Labelled.svg) <!--SR:!2026-06-08,369,365!2026-05-26,356,365-->
  - logic gate / OR, disjunction ::@:: $(0, 0) \mapsto 0; (0, 1) \mapsto 1; (1, 0) \mapsto 1; (1, 1) \mapsto 1$ <br/> $A+B$ or $A\lor B$ <br/> ![OR symbol](../../../../archives/Wikimedia%20Commons/OR%20ANSI%20Labelled.svg) <!--SR:!2026-07-03,394,365!2026-07-04,395,365-->
  - logic gate / NAND, alternative denial ::@:: $(0, 0) \mapsto 1; (0, 1) \mapsto 1; (1, 0) \mapsto 1; (1, 1) \mapsto 0$ <br/> ${\overline {A\cdot B} }$ or $A\uparrow B$ <br/> ![NAND symbol](../../../../archives/Wikimedia%20Commons/NAND%20ANSI%20Labelled.svg) <!--SR:!2026-03-24,293,345!2025-11-22,198,325-->
  - logic gate / NOR, joint denial ::@:: $(0, 0) \mapsto 1; (0, 1) \mapsto 0; (1, 0) \mapsto 0; (1, 1) \mapsto 0$ <br/> ${\overline {A+B} }$ or $A\downarrow B$ <br/> ![NOR symbol](../../../../archives/Wikimedia%20Commons/NOR%20ANSI%20Labelled.svg) <!--SR:!2026-03-25,294,345!2026-06-10,374,365-->
  - logic gate / XOR, exclusive or ::@:: $(0, 0) \mapsto 0; (0, 1) \mapsto 1; (1, 0) \mapsto 1; (1, 1) \mapsto 0$ <br/> $A\oplus B$ or $A\veebar B$ <br/> ![XOR symbol](../../../../archives/Wikimedia%20Commons/XOR%20ANSI%20Labelled.svg) <!--SR:!2026-07-08,399,365!2026-07-12,403,365-->
  - logic gate / logic function ::@:: It is a function on binary variables whose output is also a binary variable. It can be represented by logic gates. AND, NOT, and OR are fundamental to all operations in modern computers. <!--SR:!2026-07-01,392,365!2026-07-15,406,365-->
    - logic gate / logic function / representations ::@:: graphics (e.g. Karnaugh map), logical expressions, truth table <!--SR:!2026-06-01,362,365!2026-07-02,393,365-->
  - logic gate / example ::@:: 1-bit half adder: given _A_ and _B_, outputs _S_ and _C_. _S_ = _A_ XOR _B_, _C_ = _A_ AND _B_. <p> So _S_ is interpreted as the resulting bit after addition, while _C_ is the carry bit (e.g. to be connected to another 1-bit half adder). <!--SR:!2026-06-04,365,365!2026-07-11,402,365-->
  - logic gate / circuit types ::@:: 2 main ones: combinational logic circuit, sequential logic circuit <!--SR:!2026-07-05,396,365!2026-06-14,375,365-->
- [combinational logic](../../../../general/combinational%20logic.md) ::@:: It has no memory. The outputs depend entirely on the _current_ inputs and noting else. It is essentially the same as a logic function, so can be represented by a truth table. <!--SR:!2026-07-09,400,365!2026-07-08,399,365-->
- [sequential logic](../../../../general/sequential%20logic.md) ::@:: It has memory. The outputs depend on the _current_ inputs and the _state_ (value stored in _memory_). That is, the output _additionally_ depends on the input history. <!--SR:!2026-07-15,406,365!2026-07-11,402,365-->
- [combinational logic](../../../../general/combinational%20logic.md)
  - [combinational logic](../../../../general/combinational%20logic.md) / circuits ::@:: e.g. multiplexor/demultiplexor, encoder/decoder, two-level logic, programmable logic array (PLA); these are higher-level basic building blocks that are commonly seen in combinational logic <!--SR:!2026-07-05,396,365!2026-07-03,394,365-->
- [multiplexer](../../../../general/multiplexer.md)/selector, demultiplexer ::@:: (former) a device that selects between several analog or digital input signals and forwards the selected input to a single output line <p> (latter) a device that takes a single input signal and selectively forwards it to one of several output lines <!--SR:!2026-07-15,406,365!2026-07-07,398,365-->
  - multiplexer / 2<sup>_n_</sup>-to-1 multiplexer ::@:: 2<sup>_n_</sup> data inputs, _n_ selection inputs, and 1 output <p> The _n_ selection inputs have 2<sup>_n_</sup> possible combinations. Each combination selects 1 data input and forwards it to the output. <!--SR:!2026-03-23,292,345!2026-07-10,401,365-->
    - multiplexer / 2<sup>_n_</sup>-to-1 multiplexer / implementation ::@:: Use an AND gate for each data input. Connect the data input to its corresponding AND gate. Then connect the _n_ selection inputs to the AND gates, adding NOT gates as needed, such that each unique combination of _n_ selection inputs makes exactly one AND gate possible to be made output 1 iff its corresponding input is 1. Finally, connect all the AND gates into 1 giant OR gate, and that is the output. <!--SR:!2026-07-15,406,365!2026-09-14,428,325-->

## week 2 lecture

- datetime: 2025-02-10T13:30:00+08:00/2025-02-10T14:50:00+08:00
- topic: decoder, two-level logic, programmable logic array
- [binary decoder](../../../../general/binary%20decoder.md), encoder ::@:: (former) a combinational logic circuit that converts binary information from the n coded inputs to a maximum of 2<sup>_n_</sup> unique outputs <p> (latter) does the reverse <!--SR:!2026-07-06,397,365!2026-07-08,399,365-->
  - binary decoder / _n_-to-2<sup>_n_</sup> decoder ::@:: _n_ data inputs, 2<sup>_n_</sup> data outputs <p> Each unique combination of inputs activates exactly one output. For machine learning people: This is just an _one hot_ encoder. <!--SR:!2026-07-15,406,365!2026-07-06,397,365-->
    - binary decoder / _n_-to-2<sup>_n_</sup> decoder / implementation ::@:: Use an AND gate for each data output. Connect the data output to its corresponding AND gate. Then connect the _n_ selection inputs to the AND gates, adding NOT gates as needed, such that each unique combination of _n_ selection inputs makes exactly one AND gate output 1. <!--SR:!2026-07-01,392,365!2026-07-07,398,365-->
- [logic gate](../../../../general/logic%20gate.md)
  - logic gate / design process ::@:: problem specification, truth table, logical expression, simplification, implementation <!--SR:!2026-07-15,406,365!2026-07-15,406,365-->
    - logic gate / design process / example ::@:: 3-people majority vote: output 1 if two or more inputs are 1, otherwise 0 <!--SR:!2026-07-15,406,365!2026-07-10,401,365-->
- [canonical normal form](../../../../general/canonical%20normal%20form.md) ::@:: Any Boolean function can be expressed as a disjunction (OR) of minterms or a conjunction (AND) of maxterms. <!--SR:!2026-09-21,462,382!2026-09-30,464,382-->
  - [minterm](../../../../general/canonical%20normal%20form.md#minterms) ::@:: For $n$ input variables, it is a product (AND) term in which each of the $n$ variables appears _exactly_ once (either in its complemented or uncomplemented form). <p> If you put this term as the output in a truth table for all possible _n_ inputs, you will see _exactly_ one row outputs 1. This is the key insight to how it works. <!--SR:!2026-09-08,442,382!2025-10-28,181,342-->
    - minterm / indexing ::@:: There are $2^n$ possible minterms. Assign the value 1 to the direct form \($x_{i}$\) and 0 to the complemented form \($x'_{i}$\) (these assignments are reversed for maxterm); the minterm is then $\sum \limits _{i=1}^{n}2^{i-1}\operatorname {value} (x_{i})$. <p> For example, minterm $abc'$ is numbered 110<sub>2</sub> = 6<sub>10</sub> and denoted $m_{6}$. <!--SR:!2026-08-04,424,382!2026-04-27,327,362-->
  - [maxterm](../../../../general/canonical%20normal%20form.md#maxterm) ::@:: For $n$ input variables, it is a sum (OR) term in which each of the $n$ variables appears _exactly_ once (either in its complemented or uncomplemented form). <p> If you put this term as the output in a truth table for all possible _n_ inputs, you will see _exactly_ one row outputs 0. This is the key insight to how it works. <!--SR:!2026-10-02,464,382!2026-07-28,419,382-->
    - maxterm / indexing ::@:: There are $2^n$ possible maxtems. Assign the value 0 to the direct form \($x_{i}$\) and 1 to the complemented form \($x'_{i}$\) (these assignments are reversed for minterm); the maxterm is then $\sum \limits _{i=1}^{n}2^{i-1}\operatorname {value} (x_{i})$. <p> For example, we assign the index 6 to the maxterm $a'+b'+c$ \(110\) and denote that maxterm as _M_<sub>6</sub>. The complement $(a'+b'+c)'$ is the minterm $abc'=m_{6}$, using [de Morgan's law](../../../../general/De%20Morgan's%20law.md). <!--SR:!2026-04-01,301,362!2025-10-30,67,302-->
  - two-level representation ::@:: A representation where every input is a variable or its complement, one level consists of AND only, and the other level consists of OR only. There are two forms: sum of products (SOP), product of sums (POS). <!--SR:!2026-09-22,463,382!2026-09-29,463,382-->
  - [minterm canonical form](../../../../general/canonical%20normal%20form.md#minterm%20canonical%20form), sum of products (SOP) ::@:: Given the truth table of a logical function, it is possible to write the function as a "sum of products" or "sum of minterms". This is a _two-level representation_. <p> The key insight is that since a minterm is 1 for _exactly_ one input possible combination, adding (OR) minterms appropriately can produce any truth table. This is done by adding (OR) the minterms for which the corresponding row in the given truth table outputs 1. <!--SR:!2026-01-08,253,362!2026-09-30,464,382-->
  - [maxterm canonical form](../../../../general/canonical%20normal%20form.md#maxterm%20canonical%20form), sum of products (SOP) ::@:: Given the truth table of a logical function, it is possible to write the function as a "product of sums" or "product of maxterms". This is a _two-level representation_. <p> The key insight is that since a maxterm is 0 for _exactly_ one input possible combination, multiplying (AND) maxterms appropriately can produce any truth table. This is done by multiplying (AND) the maxterms for which the corresponding row (note the variables are negated) in the given truth table outputs 0. <!--SR:!2026-02-20,289,362!2026-08-29,432,382-->
- [programmable logic array](../../../../general/progammable%20logic%20array.md) (PLA) ::@:: a kind of programmable logic device used to implement combinational logic circuits <!--SR:!2026-08-03,423,382!2026-08-17,427,382-->
  - programmable logic array (PLA) / description ::@:: It has 2<sup>N</sup> AND gates for N input variables, and for M outputs from the PLA, there should be M OR gates, each with programmable inputs from all of the AND gates. <p> Each AND gate represents a minterm. Each OR gate represents a sum of products. An optimization is that if a minterm will not be used, less AND gates are needed (in the lecture slides, the PLA example has 7 AND gates only for 3 inputs). <!--SR:!2026-09-27,463,382!2026-04-24,324,362-->
  - programmable logic array (PLA) / intuition ::@:: The AND plane consisting of 2<sup>N</sup> AND gates produce all possible minterms. The OR plane consisting of M gates produces the required M outputs, assembled from all possible minterms from the AND plane. <!--SR:!2026-08-24,427,382!2026-09-27,461,382-->
  - programmable logic array (PLA) / duality ::@:: Theoretically, product of sums (POS) could be used instead, with an OR plane generating all possible maxterms, connected to an AND plane generating the required outputs. <p> However, negations are needed when you convert a truth table to POS, which is more mentally demanding and less intuitive. So that is why this is not often seen in practice. <!--SR:!2026-08-02,423,382!2026-08-03,424,382-->

## week 2 lab

- datetime: 2025-02-11T15:00:00+08:00/2025-02-11T15:50:00+08:00
- status: unscheduled, no lab

## week 2 tutorial

- datetime: 2025-02-11T18:00:00+08:00/2025-02-11T18:50:00+08:00
- status: unscheduled, no tutorial

## week 2 lecture 2

- datetime: 2025-02-14T09:00:00+08:00/2025-02-14T10:20:00+08:00
- topic: logical equivalence, Boolean algebra, K-map
- [logical equivalence](../../../../general/logical%20equivalence.md) ::@:: Two statements are this if they have the same truth value in every model. <p> In the context of combinational logic, this means two Boolean functions have the same output for every combination of inputs. <!--SR:!2026-07-30,419,387!2026-07-30,419,387-->
  - logical equivalence / methods ::@:: logical expression, truth table <!--SR:!2026-10-02,466,387!2026-08-28,431,387-->
  - logical equivalence / truth table ::@:: Very easy to prove equivalence: Check if all rows are the same. However the number of rows grows exponentially: 2<sup>_n_</sup>. <!--SR:!2026-08-22,423,387!2026-10-08,472,387-->
  - logical equivalence / logical expression ::@:: They give a more concise way to express Boolean functions, especially ones with many input variables. However, it is not always obvious that two different expressions are the same logically, so we need to simplify the expressions using Boolean algebra or Karnaugh map. <!--SR:!2026-08-30,433,387!2026-09-29,463,387-->
- Boolean algebra
  - Boolean algebra / laws ::@:: Translate logical statements into mathematical symbols. Then these laws may be used to simplify the mathematical expression. Then get back simplified logical statements. <!--SR:!2026-10-12,476,387!2026-09-01,442,387-->
    - Boolean algebra / laws / identity laws ::@:: $$\begin{aligned} p \land \top & \equiv p \\ p \lor \bot & \equiv p \end{aligned}$$ <!--SR:!2026-09-04,438,387!2026-07-23,413,387-->
    - Boolean algebra / laws / domination laws (null laws) ::@:: $$\begin{aligned} p \lor \top & \equiv \top \\ p \land \bot & \equiv \bot \end{aligned}$$ <!--SR:!2026-09-05,439,387!2026-10-03,467,387-->
    - Boolean algebra / laws / idempotent or tautology laws ::@:: $$\begin{aligned} p \lor p & \equiv p \\ p \land p & \equiv p \end{aligned}$$ <!--SR:!2026-10-06,470,387!2026-09-03,437,387-->
    - Boolean algebra / laws / negation laws (inverse laws) ::@:: $$\begin{aligned} p \lor \lnot p & \equiv \top \\ p \land \lnot p & \equiv \bot \end{aligned}$$ <!--SR:!2026-08-24,434,387!2026-10-02,466,387-->
    - Boolean algebra / laws / [commutative laws](commutative%20property.md) ::@:: $$\begin{aligned} p\vee q & \equiv q\vee p \\ p\wedge q &\equiv q\wedge p \end{aligned}$$ <!--SR:!2026-08-19,422,387!2026-08-14,417,387-->
    - Boolean algebra / laws / [associative laws](associative%20property.md) ::@:: $$\begin{aligned} (p \lor q) \lor r & \equiv p \lor (q \lor r) \\ (p \land q) \land r & \equiv p \land (q \land r) \end{aligned}$$ <!--SR:!2026-09-07,448,387!2026-10-13,477,387-->
    - Boolean algebra / laws / [distributive laws](distributive%20property.md) ::@:: $$\begin{aligned} p \lor (q \land r) & \equiv (p \lor q) \land (p \lor r) \\ p \land (q \lor r) & \equiv (p \land q) \lor (p \land r) \end{aligned}$$ <!--SR:!2026-07-29,418,387!2026-10-03,467,387-->
    - Boolean algebra / laws / [absorption laws](absorption%20law.md) ::@:: $$\begin{aligned} p \lor (p \land q) & \equiv p \\ p \land (p \lor q) & \equiv p \end{aligned}$$ <!--SR:!2026-07-30,419,387!2026-09-28,462,387-->
    - Boolean algebra / laws / [De Morgan's laws](De%20Morgan's%20laws.md) ::@:: $$\begin{aligned} \lnot (p \land q) & \equiv \lnot p \lor \lnot q \\ \lnot (p \lor q) & \equiv \lnot p \land \lnot q \end{aligned}$$ <!--SR:!2026-10-07,471,387!2026-08-18,428,387-->
    - Boolean algebra / laws / [double negation](double%20negation.md) law ::@:: $$\neg (\neg p)\equiv p$$ <!--SR:!2026-08-31,434,387!2026-10-10,472,387-->
- [Karnaugh map](../../../../general/Karnaugh%20map.md) (K-map) ::@:: A diagram that can be used to simplify a Boolean algebra expression. <p> (Note: K-map for 5 variables or more exist.) <!--SR:!2026-10-05,469,387!2026-09-12,446,387-->
  - Karnaugh map / construction ::@:: The row and column indices (shown across the top and down the left side of the Karnaugh map) are ordered in Gray code rather than binary numerical order. Gray code ensures that only one variable changes between each pair of adjacent cells. Each cell of the completed Karnaugh map contains a binary digit representing the function's output for that combination of inputs (i.e. a minterm). <!--SR:!2026-08-15,418,387!2026-08-21,422,387-->
    - Karnaugh map / construction / 2 inputs ::@:: ![Karnaugh map for 2 inputs](../../../../archives/Wikimedia%20Commons/K-map%202x2%20empty.svg) <!--SR:!2026-09-05,446,387!2026-10-10,474,387-->
    - Karnaugh map / construction / 3 inputs ::@:: ![Karnaugh map for 3 inputs](../../../../archives/Wikimedia%20Commons/K-map%202x4%20empty.svg) <!--SR:!2026-07-31,420,387!2026-10-12,474,387-->
    - Karnaugh map / construction / 4 inputs ::@:: ![Karnaugh map for 4 inputs](../../../../archives/Wikimedia%20Commons/K-map%204x4%20empty.svg) <!--SR:!2026-10-18,480,387!2026-08-14,424,387-->
    - Karnaugh map / construction / 5 inputs ::@:: It is possible, but you will need to think in 3D. Stack 2 4×4 Karnaugh map vertically. It gets even harder for 6 inputs or more... <!--SR:!2026-09-19,453,387!2026-08-18,421,387-->
    - Karnaugh map / construction / torus ::@:: You should not use a torus in practice. This is simply to demonstrate how a K-map can be made into a torus: ![Karnaugh map for 4 inputs as a torus](../../../../archives/Wikimedia%20Commons/Karnaugh%20map%20torus.svg) <!--SR:!2026-09-14,455,387!2026-09-11,452,387-->
  - Karnaugh map / grouping ::@:: Group adjacent 1s in the diagram. The grid is toroidally connected (torus shaped), so _adjacent_ cells include wrapping across the edges of the diagram (left/right edge, top/bottom edge). That means groups can wrap across the edges. <!--SR:!2026-09-13,447,387!2026-09-03,444,387-->
    - Karnaugh map / grouping / rules ::@:: The union of all groups covers all 1s. <br/> Each group has a size that is a power of 2 (i.e. 1, 2, 4, 8, ...). <br/> Each group should be as large as possible, so that the resulting minterm has the least number of variables. <br/> Number of groups should be the fewest, so that the resulting SOP has the least number of minterms. <br/> Groups may overlap: make use of this extensively to make the groups as large as possible and cover all 1s with the least number of groups. <p> Note that the best grouping may not be unique. <!--SR:!2026-03-10,295,367!2026-03-11,296,367-->
  - Karnaugh map / solution ::@:: Each group corresponds to one minterm. It can be found by examining which variables stay the same within each box. Those that stay the same should be included, while those do not should be excluded. Intuitively, each term halves the grouping size. <p> Finally, add the minterms together to get a SOP. <!--SR:!2026-03-01,286,367!2026-09-26,460,387-->
  - Karnaugh map / inverse ::@:: Group adjacent 0s in the diagram instead. This produces a SOP for the inverse. Using De Morgan's laws, we can obtain a POS for the original function. <!--SR:!2026-03-03,288,367!2026-10-09,473,387-->
  - Karnaugh map / don't cares ::@:: Those cells are marked with a X. In that case, we can either cover or not cover them, choosing the one that gives the better grouping. <!--SR:!2026-10-01,465,387!2026-09-16,448,387-->
- [seven-segment display](../../../../general/seven-segment%20display.md) ::@:: It is a form of electronic display device for displaying decimal numerals that is an alternative to the more complex dot matrix displays. <p> Basically a display with a gray 8-shape with sharp corners, which have certain edges of the 8-shape activated (glowing) to show a decimal (0123456789)/hexadecimal (0123456789AbCdEF) digit. <!--SR:!2026-10-12,476,387!2026-10-13,477,387-->

## week 3 lecture

- datetime: 2025-02-17T13:30:00+08:00/2025-02-17T14:50:00+08:00
- topic: sequential logic, S-R latch, D latch, D flip-flop
- [flip-flop](../../../../general/flip-flop%20(electronics).md) ::@:: They are circuits that have two stable states that can store state information – a bistable multivibrator. The circuit can be made to change state by signals applied to one or more control inputs and will output its state (often along with its logical complement too). It is the basic storage element in sequential logic. <!--SR:!2026-04-01,317,367!2026-07-31,420,387-->
  - flip-flop / SR NOR latch ::@:: An unclocked/asynchronous memory element. Its 2 inputs are S (set) and R (reset). Its 2 outputs are Q (stored output) and its complement. It consists of two parallel NOR gates where the output of each NOR is also fanned out into one input of the other NOR. <!--SR:!2026-10-13,479,387!2026-02-27,284,367-->
    - flip-flop / SR NOR latch / symbol, figure ::@:: symbol: ![SR NOR latch symbol](../../../../archives/Wikimedia%20Commons/SR%20(NAND)%20Flip-flop.svg) <br/> figure: ![SR NOR latch figure](../../../../archives/Wikimedia%20Commons/R-S%20mk2.gif) <!--SR:!2026-04-06,322,367!2026-04-13,313,367-->
    - flip-flop / SR NOR latch / operations ::@:: hold/_quiescent_/latch state: If S and R are both 0, Q and its complement keep their previous outputs. <br/> set: If S is 1 and R is 0, Q becomes 1 and its complement becomes 0. <br/> unset: If S is 0 and R is 1, Q becomes 0 and its complement becomes 1. <br/> _forbidden/race condition_: S and R are not allowed to be both 1, as both outputs are now 0. Then, if S and R both goes to 0 _simultaneously_ afterwards, the outputs are metastable and may eventually lock at either 1 or 0 depending on the propagation time relations between the gates. <!--SR:!2027-02-22,531,347!2026-10-11,475,387-->
- [race condition](../../../../general/race%20condition.md) ::@:: It is the condition of an electronics, software, or other system where the system's substantive behavior is dependent on the sequence or timing of other uncontrollable events, leading to unexpected or inconsistent results. It becomes a bug when one or more of the possible behaviors is undesirable. <!--SR:!2027-12-30,814,440!2027-04-20,575,420-->
  - race condition / in electronics ::@:: A typical example of a race condition may occur when a logic gate combines signals that have traveled along different paths from the same source. The inputs to the gate can change at slightly different times in response to a change in the source signal. The output may, for a brief period, change to an unwanted state before settling back to the designed state. <!--SR:!2028-02-01,841,440!2027-12-25,809,440-->
  - race condition / note ::@:: \(__this course__: __important__: It seems like the actual rules for deciding if a state is _forbidden_ is very complicated. It seems like there are three ways this can arise: adjacent 1s or 0s not covered by a contagious grouping, undefined states of SR latch, and shortest paths to latch states passing through undefined states. See the Karnaugh map race hazards examples below.\) <!--SR:!2027-12-08,795,440!2027-05-08,581,420-->
- Karnaugh map
  - Karnaugh map / race hazards ::@:: Karnaugh maps are useful for detecting and eliminating race conditions. Race hazards are very easy to spot using a Karnaugh map, because a race condition _may_ exist when moving between any pair of adjacent, but disjoint, regions circumscribed on the map. <p> Whether glitches will actually occur depends on the physical nature of the implementation, and whether we need to worry about it depends on the application. In clocked logic, it is enough that the logic settles on the desired value in time to meet the timing deadline. In our example, we are not considering clocked logic. <!--SR:!2025-10-14,148,420!2027-11-26,784,440-->
    - Karnaugh map / race hazards / SR latch ::@:: Consider the circuit $$\begin{aligned} Q & = \overline{R + \overline{S + Q} } = \overline R (S + Q) = \overline R S + \overline R Q \\ \overline Q & = \overline{S + \overline{R + \overline Q} } = \overline S (R + \overline Q) = R \overline S + \overline S \, \overline Q \,. \end{aligned}$$ <p> Its K-maps are: <p> ![SR latch K-map Q](attachments/SR%20latch%20K-map%20Q.png) <br/> ![SR latch K-map not Q](attachments/SR%20latch%20K-map%20not%20Q.png) <p> The _latch_ states are also grouped. Take note of the two labeled transitions, each transition making its two states "adjacent". While we can see movement between any adjacent pair of 1s or 0s is covered by a continuous region, there are 2 undefined states. These are also _race hazards_ \(but of a _different kind_ from that described above\). <!--SR:!2027-05-12,584,420!2026-04-03,282,380-->
    - Karnaugh map / race hazards / gated D latch ::@:: \(__this course__: midterm examination\) Consider the circuit $$Q = DE + DQ + \overline E Q \,.$$ The $\overline Q$ is naturally defined as the inverse of above, so we do not need to care about the 0s. <p> Its K-map is: <p> ![gated D latch K-map](attachments/gated%20D%20latch%20K-map.png) <p> The _latch_ states are also grouped. Take note of the two _transitions_, each transition making its two states "adjacent". One can see there are no _possible_ race conditions, since movement between any adjacent pair of 1s is covered by a continuous region. <!--SR:!2026-08-16,390,400!2026-09-07,391,400-->
    - Karnaugh map / race hazards / complex example ::@:: \(__this course__: homework 1\) Consider the circuit: <p> ![homework 1 circuit](attachments/homework%201%20circuit.png) <p> which can be written as $$\begin{aligned} Q & = \overline R S + \overline R Q \\ \overline Q & = R \overline S + \overline S \, \overline Q \,, \end{aligned}$$ where \(only eliminate subgroupings in the K-map\) $$\begin{aligned} R & = D = A \oplus \overline{BC} = ABC + \overline A \, \overline{BC} = ABC + \overline A \, \overline B + \overline A \, \overline C \\ \overline R & = (\overline A + \overline B + \overline C) (A + B) (A + C) = \overline A B C + A \overline B + A \overline C \\ S & = E = \overline{BC} \oplus C = \overline{BC} \, \overline C + BC = \overline C + BC \\ \overline S & = C (\overline B + \overline C) = \overline B C \,. \end{aligned}$$ Then, \(only eliminate subgroupings in the K-map\) $$\begin{aligned} Q & = A \overline C + \overline A BC + \overline A BCQ + A \overline B Q + A \overline C Q = A \overline C + \overline A B C + A \overline B Q \\ \overline Q & = \overline A \, \overline B C+ \overline B C \overline Q \,. \end{aligned}$$ <p> Its K-maps are: <p> ![homework 1 circuit K-map Q](attachments/homework%201%20circuit%20K-map%20Q.png) <br/> ![homework 1 circuit K-map not Q](attachments/homework%201%20circuit%20K-map%20not%20Q.png) <p> The _latch_ states are also grouped. Take note of the two labeled transitions, each transition making its two states "adjacent". While one can see movement between any adjacent pair of 1s or 0s is covered by a continuous region, there are 6 undefined states. These are also _race hazards_ \(but of a _different kind_ from that described above\). Also, the 4 defined cells _not directly adjacent_ to the latch states are also _race hazards_ \(and of a _different kind_ from the above two kinds...\), since there exists _shortest paths_ to the latch state passing through undefined states. <!--SR:!2026-11-20,440,400!2026-04-02,281,380-->
- flip-flop
  - flip-flop / SR NAND latch ::@:: It is also possible to use NAND instead of NOR to make a SR latch. But it is more rare because the inputs' meaning are negated, i.e. the hold state requires both inputs to be 1. <!--SR:!2026-10-01,465,387!2026-10-04,468,387-->
  - flip-flop / SR AND-OR latch ::@:: It may be easier from a teaching point of view. See the figure and try to figure its mechanism yourself: ![SR AND-OR latch](../../../../archives/Wikimedia%20Commons/RS-and-or-flip-flop.png) <!--SR:!2026-09-04,445,387!2026-04-06,322,367-->
  - flip-flop / gated latches ::@:: Latches are designed to be _transparent_. That is, input signal changes cause immediate changes in output. Additional logic can be added to a transparent latch to make it _non-transparent_ or _opaque_ when another input (an "enable" input) is not asserted. <!--SR:!2026-09-05,437,387!2026-08-20,423,387-->
  - flip-flop / gated SR latch ::@:: Literally just an additionally "enable" input E AND-ing with the other 2 inputs. If E is 1, it works exactly as a SR latch. Otherwise, no action (hold state), no matter how the other 2 inputs are. <!--SR:!2026-09-15,449,387!2026-10-04,468,387-->
    - flip-flop / gated SR latch / symbol, figure ::@:: symbol: ![gated SR latch symbol](../../../../archives/Wikimedia%20Commons/Gated%20SR%20flip-flop%20Symbol.svg) <br/> figure: ![gated SR latch figure](../../../../archives/Wikimedia%20Commons/SR%20(Clocked)%20Flip-flop%20Diagram.svg) <!--SR:!2026-09-14,448,387!2026-05-15,326,367-->
  - flip-flop / gated D latch ::@:: This latch exploits the fact that, in the two active input combinations (01 and 10) of a gated SR latch, R is the complement of S. <p> So what we do is, on top of the gated SR latch, instead of having the inputs S and R, we have one input D (data) only, connecting to the (now internal) S an R inputs. Assuming E is 1. If D is 0, S is 0 and R is 1. Otherwise, S is 1 and R is 0. If E is 0, nothing happens, as in the gated SR latch. <p> When E is 1, it looks like the input D is being "written" into the gate memory, so D is called _data_. The "enable" input E is sometimes also called WE (write enable) instead for the same reason. <!--SR:!2027-03-04,538,347!2026-03-09,294,367-->
    - flip-flop / gated D latch / symbol, figure ::@:: symbol: ![gated D latch symbol](../../../../archives/Wikimedia%20Commons/Transparent%20Latch%20Symbol.svg) <br/> figure: ![gated D latch symbol](../../../../archives/Wikimedia%20Commons/D-type%20Transparent%20Latch%20(NOR).svg) <!--SR:!2026-12-09,494,347!2026-04-05,321,367-->
    - flip-flop / gated D latch / register ::@:: It stores a multi-bit value. A _n_-bit \(_this_\) can be implemented using _n_ gated D latches, all controlled by a common WE. Then when we want to write to the register, set WE to 1 and the _n_ D inputs to the desired data. <!--SR:!2026-04-09,309,367!2025-12-09,204,347-->
- [clock signal](../../../../general/clock%20signal.md) ::@:: It is an electronic logic signal (voltage or current) which oscillates between a high and a low state at a constant frequency and is used like a metronome to synchronize actions of digital circuits. <!--SR:!2026-10-10,474,387!2026-10-05,469,387-->
  - clock signal / synchronization ::@:: In a _synchronous_ logic circuit, the most common type of digital circuit, the clock signal is applied to all storage devices, flip-flops and latches, and causes them all to change state simultaneously, preventing race conditions. <p> In a computer, there are many types of circuits, and each take different time to complete (propagation delay). If we do not clock the circuits, then the outputs of circuits can change unpredictably. <p> A clock-less circuit is known as _asynchronous_ circuit, but it is much harder to design than _synchronous_ ones, and is out-of-scope for this course. <!--SR:!2026-09-01,435,387!2026-10-06,468,387-->
  - clock / terminology ::@:: A _clock_ is is a free-running signal with a fixed _cycle time_ (called _clock period_) or, equivalently, a fixed _clock frequency_ (i.e., inverse of the _cycle time_). _Edge-triggered clocking_ refers to state changes in a circuit on a clock (rising or falling) edge. <!--SR:!2026-08-17,420,387!2026-08-15,416,387-->
- [digital timing diagram](../../../../general/digital%20timing%20diagram.md) ::@:: It represents a set of signals in the time domain. A timing diagram can contain many rows, usually one of them being the clock. <!--SR:!2026-03-08,293,367!2026-08-16,419,387-->
  - digital timing diagram / conventions ::@:: Higher value is a logic one. Lower value is a logic zero. A slot showing a high and low is an either-or (such as on a data line). A Z indicates high impedance. A greyed out slot is a don't-care or indeterminate. <!--SR:!2026-09-16,450,387!2026-10-15,479,387-->
- flip-flop
  - flip-flop / latch vs. flip-flop ::@:: For the former, outputs can change any time the clock is asserted (high). For the latter, outputs can change only on a clock (rising or falling) edge. <!--SR:!2026-08-21,424,387!2026-03-02,287,367-->
  - flip-flop / D flip-flop ::@:: It is widely used, and known as a "data" flip-flop. It captures the value of the D-input at a definite portion of the clock cycle (such as the rising edge of the clock). That captured value becomes the Q output. At other times, the output Q does not change. It can be viewed as a memory cell, a zero-order hold, or a delay line. <!--SR:!2026-10-12,478,387!2026-08-16,425,387-->
    - flip-flop / D flip-flop / S, R inputs ::@:: Most D-type flip-flops in ICs have the capability to be forced to the set or reset state (which ignores the D and clock inputs), much like an SR flip-flop. Usually, the illegal S = R = 1 condition is resolved in D-type flip-flops. Setting S = R = 0 makes the flip-flop behave as described above. <p> In this course, our flip-flops do not have these inputs. <!--SR:!2026-09-07,441,387!2026-10-14,478,387-->
    - flip-flop / D flip-flop / symbol ::@:: ![D flip-flop symbol](../../../../archives/Wikimedia%20Commons/D-Type%20Flip-flop.svg) <!--SR:!2026-08-22,425,387!2027-09-27,744,367-->
  - flip-flop / master–slave edge-triggered D flip-flop ::@:: It is created by connecting two gated D latches in series, and inverting the enable input to one of them. It is called master–slave because the master latch controls the slave latch's output value Q and forces the slave latch to hold its value whenever the slave latch is enabled, as the slave latch always copies its new value from the master latch and changes its value only in response to a change in the value of the master latch and clock signal. <!--SR:!2026-03-13,298,367!2026-09-06,440,387-->
    - flip-flop / master–slave edge-triggered D flip-flop / diagrams ::@:: rising/positive edge: ![master–slave rising/positive-edge-triggered D flip-flop diagram](../../../../archives/Wikimedia%20Commons/D-Type%20Flip-flop%20Diagram.svg) <br/> falling/negative edge: ![master–slave falling/negative-edge-triggered D flip-flop diagram](../../../../archives/Wikimedia%20Commons/Negative-edge%20triggered%20master%20slave%20D%20flip-flop.svg) <!--SR:!2026-06-05,347,327!2025-12-01,196,347-->
    - flip-flop / master–slave edge-triggered D flip-flop / intuition ::@:: Using the falling/negative-edge-triggered variant as an example. When the clock is high, the first latch (master) has its WE as 1, so it is writable, while the second latch (slave) has its WE as 0, so its output remains unchanged. When the clock is low, the first latch (master) has its WE as 0, so it is not writeable, while the second latch (slave) has its WE as 1, so its output copies from the first latch (master). <p> We see that first latch (master) is only writable when the clock is high, while the output update takes place when the clock is low. When the clock falls from high to low, this is precisely when the latest input to the first latch (master) is saved and not affected by subsequent changes, while the second latch (slave) copies from the newly saved state of first latch (master). Thus it is falling/negative-edge-triggered. <!--SR:!2026-04-14,314,367!2026-03-08,293,367-->
- sequential logic
  - sequential logic / synchronous ::@:: In a sequential circuit, it remembers its state (a "snapshot"). When it is _additionally_ clocked, i.e. synchronous sequential circuit, we can treat its state as changing _on and only on_ each clock cycle. <!--SR:!2026-08-15,425,387!2026-09-06,438,387-->

## week 3 lab

- datetime: 2025-02-18T15:00:00+08:00/2025-02-18T15:50:00+08:00
- topic: introduction to Logisim, combinational circuits
- Logisim ::@:: It is an interactive graphical interface for designing, simulating digital logic circuit. (Runs on Java 5... ancient software?!?) <!--SR:!2026-09-18,452,387!2026-10-13,475,387-->
  - Logisim / download ::@:: <https://sourceforge.net/projects/circuit/> <!--SR:!2026-08-13,423,387!2026-09-12,453,387-->
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
  - logic gate / logic gate to expression: hints ::@:: Work from the output to the input step-by-step. Use extra variables when needed, especially when dealing with an output connected to multiple inputs at different levels. <!--SR:!2026-09-02,436,387!2026-08-23,426,387-->
- Boolean algebra
  - Boolean algebra / simplification: hints ::@:: You may need to think of new terms to add to the expression... And also you can use extra variables to replace variables that always appear together. <!--SR:!2026-10-11,475,387!2026-03-08,293,367-->
- 2-bit comparator ::@:: 4 inputs, grouped into 2 groups of 2 inputs, each group representing a 2-bit unsigned integer. 3 outputs, respectively representing greater than, equal to, and less than. <!--SR:!2026-07-29,418,387!2026-08-12,422,387-->
  - 2-bit comparator / hints ::@:: Consider each output separately. You can always use a truth table and its SOP to write the expression. SOP is especially suitable if given a PLA. <!--SR:!2026-08-27,430,387!2026-03-31,316,367-->
- 8-to-3 encoder ::@:: 8 inputs, in one-hot encoding. 3 outputs, representing an unsigned integer from 0 to 7. <!--SR:!2026-09-07,439,387!2026-10-16,480,387-->
- 4-to-1 multiplexer ::@:: 4 inputs, representing the 4 channels to be muxed. 2 control signals, controlling which channel to output. 1 output. <!--SR:!2026-09-13,445,387!2026-10-01,465,387-->
- multiplexer
  - multiplexer / input bit width ::@:: Its output bit width is the same as its input bit width. <!--SR:!2026-11-02,495,406!2026-10-31,493,406-->
  - multiplexer / control bit width ::@:: Given _n_ control bits, the _maximum_ number of inputs is 2<sup>_n_</sup>. <br/> Given _n_ inputs, the _minimum_ number of control bits is ceil\(log<sub>2</sub>\(_n_\)\). <p> (Of course, you can violate these, but then it is not a multiplexer, isn't it?) <!--SR:!2025-11-26,210,366!2026-03-05,273,366-->

## week 3 lecture 2

- datetime: 2025-02-21T09:00:00+08:00/2025-02-21T10:20:00+08:00
- topic: 2's complement, max, min, range
- [computer number format](../../../../general/computer%20number%20format.md) ::@:: It is the internal representation of numeric values in digital device hardware and software, such as in programmable computers and calculators. <!--SR:!2026-11-20,509,406!2026-11-13,504,406-->
  - computer number format / motivation ::@:: This is one of the ways to represent numbers using bits. We may want to know more: how about unsigned integers, fractions, and reals? And what are their representable ranges? And how to do arithmetic operations on them? <!--SR:!2026-06-09,370,386!2026-12-05,521,406-->
  - computer number format / bits ::@:: They are represented by a group of bits, i.e. a bit sequence. They are grouped from the right (least significant bits) to the left (most significant bits). <!--SR:!2026-10-27,489,406!2026-12-29,542,406-->
  - computer number format / unsigned integer ::@:: It is literally positional notation but with base 2. <!--SR:!2026-10-25,487,406!2026-12-11,527,406-->
    - computer number format / unsigned integer / range ::@:: _n_ bits: \[0, 2<sup>_n_</sup>−1\] <!--SR:!2026-12-14,529,406!2026-11-21,510,406-->
    - computer number format / unsigned integer / max ::@:: It has all bits set to 1. <!--SR:!2026-12-08,524,406!2026-11-27,516,406-->
    - computer number format / unsigned integer / min ::@:: It has all bits set to 0. <!--SR:!2026-12-22,536,406!2026-12-30,543,406-->
- [two's complement](../../../../general/two's%20complement.md) ::@:: It is the most common method of representing signed (positive, negative, and zero) integers on computers, and more generally, fixed point binary values. <p> We can do natural arithmetic on it without using special rules. <!--SR:!2026-11-29,517,406!2026-10-30,492,406-->
  - two's complement / sign bit ::@:: The most significant bit (MSB) is \(_this_\). If 0, then nonnegative \(_not_ just positive\). If 1, then negative. <!--SR:!2026-07-16,388,386!2027-01-08,550,406-->
  - two's complement / nonnegative integers ::@:: Same as that for unsigned integers. Beware of the range though... in particular, the _sign bit_ is always 0. (Or you can use the _sign bit_ anyway; but when it is 1, the result after the whole procedure overflows and becomes a negative integer.) <!--SR:!2026-12-23,537,406!2026-11-30,518,406-->
  - two's complement / negative integers ::@:: Start with the absolute binary representation of the number, with the leading bit being a sign bit. (If the _sign bit_ is 1, the result after the whole procedure overflows (less accurately "underflows") and becomes a positive integer.) Then invert (or flip) all bits – changing every 0 to 1, and every 1 to 0. Finally, add 1 to the entire inverted number, ignoring any overflow. Accounting for overflow will produce the wrong value for the result. <!--SR:!2026-06-10,371,386!2025-12-26,233,366-->
  - two's complement / range ::@:: _n_ bits: \[−2<sup>_n_<!-- markdown separator -->−1</sup>, 2<sup>_n_<!-- markdown separator -->−1</sup>−1\] <!--SR:!2026-11-03,496,406!2026-11-28,517,406-->
  - two's complement / max ::@:: It has all bits set to 1 except for the sign bit, which is set to 0. <!--SR:!2026-12-28,541,406!2027-01-09,551,406-->
  - two's complement / min ::@:: It has all bits set to 0 except for the sign bit, which is set to 1. <!--SR:!2026-12-24,538,406!2026-12-06,522,406-->
    - two's complement / min / weirdness ::@:: Notice what happens if we try to negate the minimum integer. It becomes itself instead of actually negating. This is because its corresponding positive integer is not representable. <!--SR:!2026-03-08,277,366!2026-11-09,501,406-->
- [integer overflow](../../../../general/integer%20overflow.md) ::@:: It occurs when an arithmetic operation on integers attempts to create a numeric value that is outside of the range that can be represented with a given number of digits – either higher than the maximum or lower than the minimum representable value. <p> \(__this course__: __important__: We also use "integer underflow", see below.\) <!--SR:!2026-10-24,486,406!2026-12-02,520,406-->
  - integer overflow / integer underflow ::@:: The above definition of "integer overflow" refers to the ideal result being outside the representable range. <p> An alternative definition uses "integer overflow" to refer to the ideal result being _higher_ than the maximum representable integer, while using "integer underflow" to refer to the ideal result being _lower_ than the minimum representable integer. <p> \(__this course__: __important__: We use the latter definition.\) <!--SR:!2026-12-15,530,406!2026-12-14,530,406-->

## week 4 lecture

- datetime: 2025-02-24T13:30:00+08:00/2025-02-24T14:50:00+08:00
- topic: signed/unsigned number, floating point, IEEE754 examples
- two's complement
  - two's complement / sign extension ::@:: When turning a two's-complement number with a certain number of bits into one with more bits (e.g., when copying from a one-byte variable to a two-byte variable), the most-significant bit must be repeated in all the extra bits. Other examples include: right shift (but not left shift, the sign bit is shifted out as normal). <!--SR:!2027-05-11,643,411!2026-05-30,341,371-->
- [sign extension](../../../../general/sign%20extension.md) ::@:: the operation, in computer arithmetic, of increasing the number of bits of a binary number while preserving the number's sign (positive/negative) and value <!--SR:!2027-06-17,674,411!2027-04-28,634,411-->
  - sign extension / zero extension ::@:: Fill in the missing most-significant bits with zero, e.g. bitwise logical operations, up-casting unsigned integers, etc. <!--SR:!2026-11-20,472,391!2027-05-02,635,411-->
- [floating-point arithmetic](../../../../general/floating-point%20arithmetic.md)
  - floating-point arithmetic / motivation ::@:: To represent non-integral numbers, which includes fractions, very small numbers, and very large numbers. <!--SR:!2027-05-08,640,411!2027-07-07,687,411-->
  - floating-point arithmetic / representation ::@:: Roughly speaking, just like how we use a decimal point to represent non-integral numbers as decimal representation, computers use binary point to represent non-integral numbers as binary representation. <!--SR:!2027-05-01,634,411!2027-05-21,650,411-->
- [scientific notation](../../../../general/scientific%20notation.md) ::@:: a way of expressing numbers that are too large or too small to be conveniently written in decimal form, since to do so would require writing out an inconveniently long string of digits <!--SR:!2027-07-05,690,411!2027-05-18,649,411-->
  - scientific notation / form ::@:: Nonzero numbers are written in the form <p> _m_ × 10<sup>_n_</sup> <p> or _m_ times ten raised to the power of _n_, where _n_ is an [integer](../../../../general/integer.md), and the [coefficient](../../../../general/coefficient.md) _m_ is a nonzero [real number](../../../../general/real%20number.md) \(usually between 1 and 10 in absolute value, and nearly always written as a [terminating decimal](../../../../general/decimal.md)\). The integer _n_ is called the [exponent](../../../../general/exponent.md) and the real number _m_ is called the _[significand](../../../../general/significand.md)_ or _mantissa_ (not to be confused with that of the same name in floating-point arithmetic). <!--SR:!2027-05-08,644,411!2027-04-16,622,411-->
    - scientific notation / form / normalized ::@:: When _m_ is at least 1 and less than (_not_ equal to) 10. <p> For _binary_ representation, this means the leading digit is always 1. <!--SR:!2027-04-17,623,411!2027-06-30,686,411-->
- floating-point arithmetic
  - floating-point arithmetic / name ::@:: It is _floating_ because the binary point is not fixed (affected by the significand). <!--SR:!2027-04-15,621,411!2026-10-23,477,391-->
  - floating-point arithmetic / form ::@:: $$1.xxx \ldots xxx_2 \times 2^{yyy \ldots yyy_2} \,,$$ where $xxx \ldots xxx_2$ is the _significand_ or _mantissa_ (not to be confused with that of the same name in scientific notation) and $yyy \ldots yyy_2$ is the _exponent_. They have a fixed number of digits (bits). <!--SR:!2027-05-05,641,411!2027-05-06,639,411-->
  - floating-point arithmetic / distribution ::@:: Looking at its form, we can see that the distribution of floating-point numbers is not even. The density of representable numbers doubles/halves every time you cross a power of 2. <!--SR:!2027-04-14,620,411!2027-04-18,624,411-->
  - floating-point arithmetic / precision ::@:: The arithmetic is _approximate_ (i.e. not _exact_). Thus we say it has a finite range and _limited_ precision. <!--SR:!2027-06-23,680,411!2027-05-27,656,411-->
- [single-precision floating-point format](../../../../genral/single-precision%20floating-point%20format.md) (`float`) ::@:: 32-bit floating-point format, starting from the left (MSB) to the right (LSB): 1 sign bit, 8 exponent bits, and 23 significand bits (precision is 24 bits). <!--SR:!2027-04-02,608,411!2026-10-24,468,391-->
  - single-precision floating-point format / precision ::@:: about 7 significant _decimal_ digits (6 to 9) <!--SR:!2027-07-14,694,411!2027-06-28,684,411-->
  - single-precision floating-point format / exponent range ::@:: 2<sup>−126</sup> ≈ 10<sup>−38</sup> to 2<sup>+127</sup> ≈ 10<sup>+38</sup> <!--SR:!2026-11-10,485,391!2026-12-18,494,391-->
  - single-precision floating-point format
- [double-precision floating-point format](../../../../genral/double-precision%20floating-point%20format.md) (`double`) ::@:: 64-bit floating-point format, starting from the left (MSB) to the right (LSB): 1 sign bit, 11 exponent bits, and 52 significand bits (precision is 53 bits). <!--SR:!2027-06-11,669,411!2027-05-29,658,411-->
  - double-precision floating-point format / precision ::@:: about 16 significant _decimal_ digits (15 to 17) <!--SR:!2027-07-09,689,411!2027-07-08,688,411-->
  - double-precision floating-point format / exponent range ::@:: 2<sup>−1022</sup> ≈ 10<sup>−308</sup> to 2<sup>+1023</sup> ≈ 10<sup>+308</sup> <!--SR:!2026-02-03,223,371!2025-12-04,183,371-->
    - double-precision floating-point format / exponent range / mnemonic ::@:: Compare the exponents with that of single-precision... notice that "0" is inserted as the 2nd digit. Hmm... <!--SR:!2027-05-04,637,411!2027-04-13,619,411-->
- [IEEE 754](../../../../general/IEEE%20754.md) ::@:: a technical standard for floating-point arithmetic originally established in 1985 by the Institute of Electrical and Electronics Engineers \(IEEE\) <!--SR:!2027-06-26,682,411!2027-04-11,617,411-->
  - IEEE 754 / history (brief) ::@:: It was developed in response to divergence of representations, which can cause portability issues for scientific code. Now it is almost universally adopted. <!--SR:!2027-06-05,663,411!2027-05-23,652,411-->
  - IEEE 754 / representations ::@:: single precision (32-bit), double precision (64-bit), ... (there are much more not covered in this course) <!--SR:!2027-06-16,673,411!2027-05-07,643,411-->

## week 4 lab

- datetime: 2025-02-25T15:00:00+08:00/2025-02-25T15:50:00+08:00
- topic: building sequential logics with Logisim
- Logisim
  - Logisim / magnification ::@:: Use magnification to help you connect wires and draw graphics. <!--SR:!2027-05-15,646,411!2026-10-07,457,391-->
  - Logisim / wire color ::@:: Light green means 1. Dark green means 0. Any other color means connection problem. <!--SR:!2027-05-20,651,411!2027-06-25,681,411-->
  - Logisim / auto build ::@:: Given a logical expression, it can build a circuit for you. You can convert a truth table into an expression using SOP (or POS). <!--SR:!2027-03-27,602,411!2027-06-15,672,411-->
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
- [register file](../../../../general/register%20file.md) ::@:: an array of processor registers in a central processing unit (CPU) <!--SR:!2027-07-10,690,411!2027-05-22,651,411-->
  - register file / implementation ::@:: fast static RAMs with multiple ports <!--SR:!2027-05-13,645,411!2027-04-04,610,411-->
- [counter](../../../../general/counter%20(digital).md) ::@:: a device which stores (and sometimes displays) the number of times a particular event or process has occurred, often in relationship to a clock <!--SR:!2027-04-03,609,411!2027-05-24,653,411-->
  - counter / synchronous 2-bit counter ::@:: The counter has 2 gated D latches, each linked to an output. The output cycles through 00, 01, 10, and 11. Its input has the clock only.  <p> The 2 required combinational logic gates are the NOT gate and XOR gate. <!--SR:!2026-11-12,487,391!2027-06-10,668,411-->
    - counter / synchronous 2-bit counter / hints ::@:: truth table/transition table → K-map → logic simplification → circuit design <!--SR:!2027-04-30,636,411!2027-07-06,691,411-->

## week 4 lecture 2

- datetime: 2025-02-28T09:00:00+08:00/2025-02-28T10:20:00+08:00
- topic: IEEE754 rational: implicit 1, biased exponent, range, precision, special cases
- IEEE 754
  - IEEE 754 / format ::@:: It is composed of 3 parts, in order from MSB to LSB: a _sign_, an _exponent_, and then a _significand_. <!--SR:!2027-05-10,642,411!2026-10-30,474,391-->
    - IEEE 754 / format / input ::@:: Inputs required to design a IEEE 754 format: a base _b_ that is either 2 or 10 (for simplicity, __we only consider _b_ = 2 henceforth__), a precision _p_, and an exponent range from _emin_ to _emax_ (inclusive) satisfying _emin_ = −(_emax_ − 1) = 1 − _emax_. <!--SR:!2027-06-12,670,411!2026-05-11,341,391-->
    - IEEE 754 / format / number ::@:: We have 3 types of numbers: signed finite numbers (including two signed zeros), two infinities, and two kinds of NaN (not-a-number): a quiet NaN (qNaN) and a signaling NaN (sNaN). <!--SR:!2027-05-06,642,411!2027-06-09,667,411-->
    - IEEE 754 / format / finite numbers ::@:: _s_ = a sign that is either 0 or 1, <br/> _c_ = a _significand_ that is an _integer_ from 0 to _b_<sup>_p_</sup>−1 (at most _p_ base-_b_ digits), and <br/> _q_ = an _exponent_ such that _emin_ ≤ _q_ + _p_ − 1 ≤ _emax_. <br/> The numerical value of such a finite number is \(−1\)<sup>_s_</sup> × _c_ × _b_<sup>_q_</sup>. <p> Equivalently, _q_ = an _exponent_ such that _emin_ ≤ _q_ ≤ _emax_. <br> The numerical value of such a finite number is \(−1\)<sup>_s_</sup> × \(_c_ × _b_<sup>1 − _p_</sup>\) × _b_<sup>_q_</sup>, where \(_c_ × _b_<sup>1 − _p_</sup>\) can be interpreted as _c_ but the decimal point is right after the first digit. This latter definition more closely matches the actual binary representation. We will __use this latter definition henceforth__. <!--SR:!2026-09-23,396,331!2025-12-10,217,371-->
    - IEEE 754 / format / sign bit ::@:: 0 is nonnegative, 1 is negative. This is obvious. <!--SR:!2027-05-04,640,411!2027-04-24,630,411-->
    - IEEE 754 / format / significand bits ::@:: Given precision _p_ (number of digits), we could just simply have _p_ bits directly corresponding to the _p_ digits of _c_. However, we have a problem: 0 have many different representations, two (due to the sign bit) for each combination of exponent bits. <p> To avoid this, we use the _implicit bit convention_: the first digit of _c_ is always 1, except when representing 0 \(and subnormal numbers\). 0 is represented by the significand bits and exponent bits being all 0s. <!--SR:!2027-04-22,628,411!2026-01-26,252,371-->
      - IEEE 754 / format / significand bits / implicit bit ::@:: This has two advantages: We now only have two representations for 0. And we can represent _p_ digits with only _p_ − 1 bits! The disadvantage is now we have _subnormal numbers_ (the other being named _normal numbers_) when the exponent bits are all 0s but not the significand bits, which has a precision less than _p_ depending on the value (and some other things mentioned below). <!--SR:!2027-05-03,639,411!2027-05-28,657,411-->
    - IEEE 754 / format / exponent bits ::@:: Usually we decide the exponent range from the number of bits instead of the other way around. Given _n_ exponent bits, we have 2<sup>_n_</sup> combinations. For _normal numbers_, the exponent bits are not all 0s (_subnormal numbers_) and not all 1s (_infinities_ and _NaNs_). So we only have 2<sup>_n_</sup> − 2 combinations left. <p> Then the range is \[−(2<sup>_n_ − 1</sup> − 2), 2<sup>_n_ − 1</sup> − 1\]. The exponent bits are _biased_. <!--SR:!2026-09-22,447,391!2027-05-16,647,411-->
      - IEEE 754 / format / exponent bits / bias ::@:: An actual exponent of 0 is represented by all bits 1 except for the MSB, which is 0. From this, we derive a _bias_, which is 2<sup>_n_ − 1</sup> − 1. <p> This can be interpreted as: interpreting the exponent bits as an _unsigned_ integer, _subtracting_ it by the _bias_ gives the actual exponent; or the exponent bits as an _unsigned_ integer stores the actual exponent _plus_ the _bias_. <p> Its advantage is that floating-point numbers of the _same sign_ can be compared directly as if they are unsigned integers (if the sign bit is 1, the ordering is reversed). <!--SR:!2026-09-12,440,391!2026-08-28,427,391-->
    - IEEE 754 / format / infinity ::@:: The signed infinities are represented by setting the exponent bits to all 1s and the significand bits to all 0s. <p> The sign bit determines if it is positive or negative. <!--SR:!2027-04-11,617,411!2026-10-29,473,391-->
    - IEEE 754 / format / NaN ::@:: NaNs are represented by setting the exponent bits to all 1s and the significand bits to _not_ all 0s. <p> The sign bit is ignored by most applications. <!--SR:!2027-05-02,638,411!2027-05-19,650,411-->
      - IEEE 754 / format / NaN / quiet, signaling ::@:: If the most significant significand bit is 0, it is _signaling_. If it is 1, it is _quiet_. The remaining bits (and rarely the sign bit) is a _payload_ that can store anything. For signaling NaNs, the payload cannot be all 0s or else it becomes an infinity. <p> The above convention (0 is signal, 1 is quiet) means one can silence a signaling NaN into a quiet NaN by simply setting the most significant significand bit to 1. The reverse convention _may_ convert a signaling NaN to an infinity instead if the payload is all 0s. <!--SR:!2026-11-13,488,391!2026-05-12,330,371-->
  - IEEE 754 / conversion from a number ::@:: (for humans) Write the number in terms of _normalized_ scientific notation in base _b_ for the significand. Set the sign bit directly, the exponent bits (remember to add the bias), and the significant bits (discarding the leading implicit 1). Finally, check that the resulting format represents a finite (normal) number instead of special numbers \(may include subnormal numbers depending on the context\). Otherwise, the number to be represented is out of range. <!--SR:!2027-05-30,659,411!2026-05-22,333,371-->
- single-precision floating-point format
  - single-precision floating-point format / range \(zero, normal\) ::@:: in absolute value (i.e. discard sign): 0, \[1×2<sup>–126</sup> ≈ 1.2×10<sup>–38</sup>, (2−2<sup>−23</sup>)×2<sup>+127</sup> ≈ 3.4×10<sup>+38</sup>\] (figure out the representations yourself) <!--SR:!2027-05-05,638,411!2026-12-22,497,391-->
  - single-precision floating-point format / range \(subnormal\) ::@:: in absolute value (i.e. discard sign): \[2<sup>−23</sup>×2<sup>–126</sup> ≈ 1.4×10<sup>–45</sup>, (1−2<sup>−23</sup>)×2<sup>–126</sup> ≈ 1.2×10<sup>–38</sup>\] (figure out the representations yourself) <!--SR:!2025-11-17,182,351!2026-03-01,249,351-->
- double-precision floating-point format
  - double-precision floating-point format / range \(zero, normal\) ::@:: in absolute value (i.e. discard sign): 0, \[1×2<sup>–1022</sup> ≈ 2.2×10<sup>–308</sup>, (2−2<sup>−52</sup>)×2<sup>+1023</sup> ≈ 1.8×10<sup>+308</sup>\] (figure out the representations yourself) <!--SR:!2026-02-18,247,351!2026-10-21,414,331-->
  - double-precision floating-point format / range \(subnormal\) ::@:: in absolute value (i.e. discard sign): \[2<sup>−52</sup>×2<sup>–1022</sup> ≈ 4.9×10<sup>–324</sup>, (1−2<sup>−52</sup>)×2<sup>–1022</sup> ≈ 2.2×10<sup>–308</sup>\] (figure out the representations yourself) <!--SR:!2026-10-15,459,391!2026-02-20,242,351-->
- [arithmetic underflow](../../../../general/arithmetic%20underflow.md) ::@:: It is a condition in a computer program where the result of a calculation is a number of more precise absolute value than the computer can actually represent in memory on its central processing unit (CPU). <p> The exponent becomes too small (slides: negative exponent becomes too large) to fit in the exponent field. This is not the same as a number becoming too negative, which is arithmetic overflow instead. <!--SR:!2026-09-17,444,391!2026-10-30,454,391-->
  - arithmetic underflow / arithmetic overflow ::@:: Similar to integer overflow. The (slides: positive) exponent becomes too large to fit in the exponent field. Equivalently, the number becomes too negative or too positive. <!--SR:!2027-07-16,696,411!2027-05-17,648,411-->
  - arithmetic underflow / integer ::@:: First, see above discussion of "integer underflow" in integer overflow. <p> Unlike "integer underflow", arithmetic underflow is _not_ used like how "integer underflow" is used relative to "integer overflow". That is, arithmetic underflow never refers to a number becoming too negative. <!--SR:!2027-06-08,666,411!2027-04-23,629,411-->
- [normal number](../../../../general/normal%20number%20(computing).md) ::@:: It is a normal number is a non-zero number in a floating-point representation which is within the balanced range supported by a given floating-point format: it is a floating point number that can be represented without leading zeros in its significand. <!--SR:!2026-10-09,459,391!2026-11-14,489,391-->
- [subnormal number](../../../../general/subnormal%20number.md) ::@:: They fill the underflow gap around zero in floating-point arithmetic. Any non-zero number with magnitude smaller than the smallest positive normal number is _subnormal_, while _denormal_ can also refer to numbers outside that range. <!--SR:!2027-05-09,641,411!2027-04-07,613,411-->
  - subnormal number / significand ::@:: Note that the leading _implicit_ bit is now 0 instead of 1. This is the defining characteristic. <!--SR:!2027-07-17,697,411!2027-04-30,633,411-->
  - subnormal number / exponent ::@:: Note that the actual exponent for subnormal numbers is as if the exponent bits has an unsigned value of 1 instead of being all 0s, even though the exponent bits are actually all 0s. <!--SR:!2027-07-04,689,411!2027-05-31,660,411-->
  - subnormal number / issues ::@:: They fill the underflow gap with _evenly_ spaced values, instead of being _logarithmically_ spaced like normal numbers. <p> Some system handle these numbers much more slowly than normal numbers. <!--SR:!2027-06-27,683,411!2027-05-25,654,411-->
- IEEE 754
  - IEEE 754 / format
    - IEEE 754 / format / infinity
      - IEEE 754 / format / infinity / usage ::@:: It can be used in subsequent calculations, which avoids need for checking overflows. <!--SR:!2027-04-12,618,411!2027-04-19,625,411-->
    - IEEE 754 / format / NaN
      - IEEE 754 / format / NaN / usage ::@:: It can be used in subsequent calculations, which avoids need for illegal checking illegal or undefined operations, e.g. dividing 0 by 0. <!--SR:!2026-10-26,470,391!2027-04-08,614,411-->
- [ASCII](../../../../general/ASCII.md) ::@:: It is a character encoding standard for electronic communication, used by most computers today. <p> It is a 7-bit code, so there are 128 code points. Each unsigned integer maps to a character. But most of time we use an unsigned byte, which has 8 bits, to represent a character with the MSB set to 0. <!--SR:!2027-04-10,616,411!2027-06-07,665,411-->
  - ASCII / full name ::@:: American Standard Code for Information Interchange <!--SR:!2027-05-07,640,411!2027-06-06,664,411-->
  - ASCII / patterns ::@:: Some notable patterns: <br/> Alphabets (A to Z, a to z) and numbers (0 to 9) are in order. <br/> groups: NUL (null) → control characters → punctuations → numbers → punctuations → big alphabets → punctuations → small alphabets → punctuations → DEL (a control character) <!--SR:!2027-02-19,521,351!2026-05-25,329,371-->
  - ASCII / note ::@:: How can 128 code points store all characters? This is why we have _Unicode_, but Unicode is much more complicated and involves a variable number of bytes to encode a character. It will not be covered here. <!--SR:!2027-07-13,693,411!2027-04-29,632,411-->

## week 5 lecture

- datetime: 2025-03-03T13:30:00+08:00/2025-03-03T14:50:00+08:00
- topic: basic instructions, register, memory operand
- instruction set architecture
  - instruction set architecture / analogy as a language ::@:: Words are _instructions_. A vocabulary (set of all words\) is an _instruction set_. Programmers write in _assembly language_. After assembly by an _assembler_, it becomes _machine language_, which hardware can understand. <!--SR:!2026-07-07,379,404!2027-08-25,734,424-->
  - instruction set architecture / specifications ::@:: addressing modes, exception handling, external I/O, native data types, instructions, interrupt handling, memory architecture, opcodes \(machine language\), registers <!--SR:!2026-01-19,245,384!2026-09-05,436,404-->
  - instruction set architecture / vs. assembly language ::@:: The former is a public interface to processors implementing this ISA. The latter is simply a programming language. <p> Ideally, a ISA should have a corresponding language. In practice, there are variations. They are defined by the assembler. <!--SR:!2027-07-19,699,424!2027-07-30,710,424-->
  - instruction set architecture / advantages
    - instruction set architecture / advantages / compatibility ::@:: Hardware changes will \(usually\) not impact existing programs: no re-programming is required. Hardware improvement can be made as long as it conforms to the ISA. <!--SR:!2027-08-31,738,424!2027-09-12,747,424-->
  - instruction set architecture / examples
- [reduced instruction set computer](../../../../general/reduced%20instruction%20set%20computer.md) \(RISC\) ::@:: It is a computer architecture designed to simplify the individual instructions given to the computer to accomplish tasks. <!--SR:!2027-06-28,685,424!2027-09-01,740,424-->
  - reduced instruction set computer / comparison ::@:: Compared to the instructions given to a complex instruction set computer (CISC), a RISC computer might require more instructions (more code) in order to accomplish a task because the individual instructions are written in simpler code. <!--SR:!2027-07-31,711,424!2027-10-18,779,424-->
  - reduced instruction set computer / advantages ::@:: Easy to learn and understand. Have a large share of the embedded computers market. Less instructions. <!--SR:!2027-08-23,732,424!2027-08-31,739,424-->
  - reduced instruction set computer / principles ::@:: good compromises, make common cases fast, simplicity favors regularity \(less cases\), smaller is faster <!--SR:!2027-08-24,733,424!2027-10-11,773,424-->
- [MIPS architecture](../../../../general/MIPS%20architecture.md) ::@:: It is the RISC that we will learn here. <p> It was a research project conducted by John L. Hennessy at Stanford University between 1981 and 1984. Then it was commercialized and developed by MIPS Technologies. <!--SR:!2027-09-28,762,424!2027-09-18,753,424-->
  - MIPS architecture / full name ::@:: Microprocessor without Interlocked Pipeline Stages <!--SR:!2027-07-17,702,424!2027-09-22,756,424-->
  - MIPS architecture / reference ::@:: MIPS reference data green card <!--SR:!2027-08-16,726,424!2027-09-30,763,424-->
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
- [processor register](../../../../general/processor%20register.md) ::@:: a quickly accessible location available to a computer's processor <!--SR:!2027-10-17,778,424!2027-06-19,677,424-->
  - processor register / implementation
    - processor register / implementation / 2-bit register ::@:: Have 2 D flip-flops. Connect the same clock signal to both of them. Split the 2-bit data inputs via a "splitter", and connect each to a D flip-flop. Combine their output as 2-bit data outputs via a "combiner". <!--SR:!2027-07-02,688,424!2026-10-11,466,404-->
      - processor register / implementation / 2-bit register / write enabled ::@:: Add a muxer that selects between the current input and the current output. The 2 D flip-flops inputs are now provided by the muxer instead of the current input. Add a write enabled \(WE\) input that connects to the muxer to select the appropriate muxer input. <!--SR:!2027-10-08,770,424!2026-12-31,506,404-->
- register file
  - register file / implementation ::@:: The idea is that we have several registers, and a register file has an input to select which register to use. <p> Have several registers. Connect the same clock signal to all registers. Add an input that selects a register for both writing and reading. Add a decoder that uses the register selection to write-enable _exactly one_ of the registers. Add a muxer that uses the register selection to select the output of _exactly one_ of the registers. <!--SR:!2026-02-19,276,384!2027-09-14,749,424-->
    - register file / implementation / extensions ::@:: We could separate the register selection for writing and reading. We could also add a write-enable input. <!--SR:!2027-09-20,755,424!2027-08-29,737,424-->

## week 5 tutorial

- datetime: 2025-03-04T18:00:00+08:00/2025-03-04T18:50:00+08:00
- topic: base conversion, integer representation
- positional notation
  - positional notation / integral conversion
    - positional notation / integral conversion / base 2, base 16
- [hexadecimal](../../../../general/hexadecimal.md)
  - hexadecimal / notations ::@:: In mathematics, a subscript is typically used to specify the base. For example, the decimal value 711 would be expressed in hexadecimal as 2C7<sub>16</sub>. \(A rarely seen notation is 2C7<sub>hex</sub>.\) In programming, several notations denote hexadecimal numbers, usually involving a prefix. The prefix `0x` is used in [C](c%20(programming%20language).md), which would denote this value as `0x2C7`. <p> In writing, we may express it as 2C7<sub>(16)</sub>, so that the base is distinguished from the number even with bad handwriting <small>\(e.g. me\)</small>. <!--SR:!2027-09-29,762,424!2027-07-01,687,424-->
- [signed number representations](../../../../general/signed%20number%20representations.md) ::@:: In mathematics, negative numbers in any base are represented by prefixing them with a minus sign ("−"). However, in RAM or CPU registers, numbers are represented only as sequences of bits, without extra symbols. <!--SR:!2027-10-15,776,424!2027-10-16,777,424-->
  - [sign–magnitude](../../../../general/signed%20number%20representations.md#sign–magnitude) ::@:: The sign bit is 0 if positive, 1 if negative. The magnitude is represented by the remaining bits. <p> examples: IEEE 754 _sign_ bit and _significand_ field together <!--SR:!2027-09-19,753,424!2027-08-15,725,424-->
    - sign–magnitude / addition ::@:: If the signs are the same, add the magnitude. If the signs are different, subtract the larger magnitude from the smaller magnitude. The sign is the same as the number with the larger magnitude. <!--SR:!2027-06-20,678,424!2027-09-28,762,424-->
    - sign–magnitude / disadvantages ::@:: Arithmetic is complex, so are the circuits to implement it. <!--SR:!2027-09-08,746,424!2027-07-16,701,424-->
  - signed number representations / systems ::@:: sign–magnitude, offset binary, one's complement, two's complement, etc. <!--SR:!2027-10-03,766,424!2027-10-05,767,424-->
- [one's complement](../../../../general/one's%20complement.md) ::@:: It of a binary number is the value obtained by inverting (flipping) all the bits in the binary representation of the number. The sign bit is 0 if the number is positive, 1 if negative. <!--SR:!2027-10-10,772,424!2027-09-02,740,424-->
  - one's complement / naming ::@:: The name "ones' complement" refers to the fact that such an inverted value, if added to the original, would always produce an "all ones" number (the term "complement" refers to such pairs of mutually additive inverse numbers, here in respect to a non-0 base number). <!--SR:!2027-07-15,700,424!2027-09-01,739,424-->
  - one's complement / addition ::@:: Adding two values is straightforward. Simply align the values on the least significant bit and add, propagating any carry to the bit one position left. If the carry extends past the end of the word it is said to have "wrapped around", a condition called an "_end-around carry_". When this occurs, the bit must be added back in at the right-most bit. This phenomenon does not occur in two's complement arithmetic. <!--SR:!2026-09-20,448,404!2027-08-26,735,424-->
  - one's complement / subtraction ::@:: Subtraction is similar, except that borrows, rather than carries, are propagated to the left. If the borrow extends past the end of the word it is said to have "wrapped around", a condition called an "_end-around borrow_". When this occurs, the bit must be subtracted from the right-most bit. This phenomenon does not occur in two's complement arithmetic. <p> An alternative is using the [method of complements](../../../../general/method%20of%20complements.md) to implement subtraction. For example, subtracting −5 from 15 is just adding 5 to 15. <!--SR:!2027-08-14,724,424!2025-11-28,205,384-->
  - one's complement / advantages ::@:: Arithmetic is simpler \(slightly more complex than two's complement\), so are the circuits to implement it. Negation is always possible. <!--SR:!2027-08-13,723,424!2027-07-26,706,424-->
  - one's complement / disadvantages ::@:: Zero is signed \(this may be an advantage in some scenarios\). Addition and subtraction requires _end-around_ carrying and _end-around_ borrowing respectively. <!--SR:!2026-05-25,355,404!2027-08-30,737,424-->
- [two's complement](../../../../general/two's%20complement.md)
  - two's complement / addition ::@:: Adding two's complement numbers requires no special processing even if the operands have opposite signs; the sign of the result is determined automatically. Simply align the values on the least significant bit and add, propagating any carry to the bit one position left. If the carry extends past the end of the word, discard it. <p> This actually reflects the [ring](../../../../general/ring%20(mathematics).md) structure on all integers [modulo](../../../../general/modular%20arithmetic.md) [2<sup>_N_</sup>](../../../../general/power%20of%20two.md): $\mathbb {Z} /2^{N}\mathbb {Z}$. <!--SR:!2027-10-09,771,424!2026-12-30,505,404-->
  - two's complement / subtraction ::@:: Computers usually use the [method of complements](../../../../general/method%20of%20complements.md) to implement subtraction. For example, subtracting −5 from 15 is just adding 5 to 15. <!--SR:!2027-10-04,767,424!2027-07-23,703,424-->
  - two's complement / advantages ::@:: Arithmetic is simpler \(even simpler than one's complement\), so are the circuits to implement it. Zero is unsigned \(this may be an disadvantage in some scenarios\). <!--SR:!2027-07-24,704,424!2027-08-30,738,424-->
  - two's complement / disadvantages ::@:: Negation is not possible for the most negative number. <!--SR:!2027-10-05,768,424!2027-09-21,755,424-->
- integer overflow
  - integer overflow / integer underflow
- [offset binary](../../../../general/offset%20binary.md) ::@:: \(untaught\) It is a method for [signed number representation](signed%20number%20representation.md) where a signed number _n_ is represented by the bit pattern corresponding to the unsigned number _n_+_K_, _K_ being the _biasing value_ or _offset_. <p> examples: IEEE 754 _exponent_ field \(_K_ = 2<sup>_n_<!-- markdown separator -->−1</sup> − 1\) <!--SR:!2027-01-05,510,404!2027-10-14,775,424-->
  - offset binary / value of _K_ ::@:: There is no standard for offset binary, but most often the _K_ for an _n_-bit binary word is _K_ = 2<sup>_n_<!-- markdown separator -->−1</sup> \(for example, the offset for a four-digit binary number would be 2<sup>3</sup>=8\). This has the consequence that the minimal negative value is represented by all-zeros, the "zero" value is represented by a 1 in the most significant bit and zero in all other bits, and the [maximal positive value](../../../../general/integer%20overflow.md) is represented by all-ones \(conveniently, this is the same as using [two's complement](../../../../general/two's%20complement.md) but with the most significant bit inverted\). <p> For IEEE 754, unusually however, instead of using "excess 2<sup>_n_<!-- markdown separator -->−1</sup>" it uses "excess 2<sup>_n_<!-- markdown separator -->−1</sup> − 1" which means that inverting the leading (high-order) bit of the exponent will not convert the exponent to correct two's complement notation. <!--SR:!2027-09-17,752,424!2027-09-19,754,424-->
  - offset binary / advantages ::@:: In a logical comparison operation, one gets the same result as with a true form numerical comparison operation, whereas, in two's complement notation a logical comparison will agree with true form numerical comparison operation if and only if the numbers being compared have the same sign. Otherwise the sense of the comparison will be inverted, with all negative values being taken as being larger than all positive values. <!--SR:!2027-08-12,722,424!2027-07-20,700,424-->

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
- MARS ::@:: It is a GUI-based MIPS emulator designed for use in education, specifically for use with Hennessy's _Computer Organization and Design_. (Runs on Java 8... slightly less ancient software...) <!--SR:!2027-08-12,721,428!2027-08-06,715,428-->
  - MARS / architecture ::@:: MARS opens an assembly program into its memory. Then the memory is manipulated using a simulated MIPS processor. The processor can additionally interact with a console I/O window through I/O. <p> For debugging, MARS provides data segment window, register window, messages window, and text segment window. <!--SR:!2027-08-22,730,428!2027-08-10,719,428-->
  - MARS / download ::@:: <https://computerscience.missouristate.edu/mars-mips-simulator.htm> <!-- <https://courses.missouristate.edu/KenVollmar/MARS/> --> \(GitHub: <https://github.com/dpetersanderson/MARS/>\) <!--SR:!2027-08-15,723,428!2027-08-20,728,428-->
  - MARS / installation
  - MARS / usage
  - MARS / windows :;@:: console I/O window, data segment window, register window, messages window, text segment window
    - MARS / windows / console I/O window
    - MARS / windows / data segment window ::@:: It shows the data segment in the memory, which stores your data \(`.data`\). By default, it starts from 0x1001&nbsp;000 \(global pointer `$gp`\), goes upward in address. Static data is stored first, and then dynamic data. When more space is needed for dynamic data, it grows upwards in address. <!--SR:!2027-01-27,524,408!2027-08-14,722,428-->
    - MARS / windows / register window
    - MARS / windows / messages window
    - MARS / windows / text segment window ::@:: It shows the text segment in the memory, which stores your program \(`.text`\). By default, it starts from 0x0040&nbsp;0000, and goes upward in address. <!--SR:!2027-08-19,727,428!2027-08-08,717,428-->
- [system call](../../../../general/system%20call.md) ::@:: It is the programmatic way in which a computer program requests a service from the operating system on which it is executed. This may include hardware-related services \(for example, accessing a hard disk drive or accessing the device's camera\), creation and execution of new processes, and communication with integral kernel services such as process scheduling. System calls provide an essential interface between a process and the operating system. <!--SR:!2027-08-11,720,428!2027-08-16,724,428-->
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
  - single-precision floating-point format / conversion from decimal ::@:: First, write the decimal in scientific notation, with the significand in base 2. Normalize the scientific notation. <p> Write the sign bit, with positive being 0 and negative being 1. Write the exponent bits by adding the bias to the exponent, and representing it as an unsigned integer. Write the significand bits by discarding the leading 1 digit and writing the remaining digits verbatim, zero-padding at the end if necessary. <p> Finally, check if the resulting format represents a finite (normal) number instead of special numbers \(may include subnormal numbers depending on the context\). Otherwise, the decimal is out of range. <p> If the decimal requires too many digits to be written \(more than the number of significand bits, ignoring the implicit leading 1\), then the conversion is inexact. \(__this course__: we also say such a decimal is not representable\) <!--SR:!2026-06-11,353,388!2027-06-09,631,368-->
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
- [stored-program computer](../../../../general/stored-program%20computer.md) ::@:: It is a computer that stores program instructions in electronically, electromagnetically, or optically accessible memory. This contrasts with systems that stored the program instructions with plugboards or similar mechanisms. <p> The definition is often extended with the requirement that the treatment of programs and data in memory be interchangeable or uniform. <!--SR:!2027-08-18,726,428!2027-08-07,716,428-->
  - stored-program computer / examples ::@:: Instructions and data are both represented by binary. They can be both stored in memory. Programs can operate on programs. Binary compatibility \(e.g. ISA\) allows programs to work on different computers. <!--SR:!2027-08-09,718,428!2027-08-17,725,428-->

## week 7 lecture

- datetime: 2025-03-17T13:30:00+08:00/2025-03-17T14:50:00+08:00
- topic: procedure, nested procedures with stack
- MIPS architecture
  - [MIPS](MIPS.md)
    - [§ procedures](MIPS.md#procedures)
    - [§ calling conventions](MIPS.md#calling%20conventions)
    - [§ jump instructions](MIPS.md#jump%20instructions): `jal`, `jr`
    - [§ program counter](MIPS.md#program%20counter)
    - [§ O32 calling convention](MIPS.md#O32%20calling%20convention)
    - [§ memory layout](MIPS.md#memory%20layout)
    - [§ pseudo-instructions](MIPS.md#pseudo-instructions): `push`, `pop`
- ASCII
  - ASCII / full name
  - ASCII / common characters ::@:: space: 0x20 \(32\) <!--SR:!2027-12-27,811,440!2028-01-22,833,440-->
- MIPS architecture
  - [MIPS](MIPS.md)
    - [§ data instructions](MIPS.md#data%20instructions): `lb`, `sb`, `lbu`

## week 7 lab

- datetime: 2025-03-18T15:00:00+08:00/2025-03-18T15:50:00+08:00
- topic: MIPS programming
- MARS
  - [MARS](MARS.md)
  - MARS / exercises ::@:: number guessing game \(and enhancing it\), number multiplier, etc. <!--SR:!2027-12-02,790,440!2028-01-14,826,440-->

## week 7 tutorial

- datetime: 2025-03-18T18:00:00+08:00/2025-03-18T18:50:00+08:00
- topic: introduction to MIPS assembly
- instruction set architecture
- MIPS architecture
  - [MIPS](MIPS.md)
    - [§ calling conventions](MIPS.md#calling%20conventions)
    - [§ O32 calling convention](MIPS.md#O32%20calling%20convention)
    - [§ assembly directives](MIPS.md#assembly%20directives): `.space`
    - [§ instructions](MIPS.md#instructions)
    - [§ arithmetic instructions](MIPS.md#arithmetic%20instructions): `addi`, `add`, `sub`
    - [§ bitwise instructions](MIPS.md#bitwise%20instructions): `sll`, `and`, `nor`, `xor`, `srl`, `sra`
    - [§ entry point](MIPS.md#entry%20point)
    - [§ pseudo-instructions](MIPS.md#pseudo-instructions): `not`, `abs`, `blt`, `bgt`, `ble`, `bge`, `neg`, `not`, `li`, `la`, `move`, `sge`, `sgt`
    - [§ data instructions](MIPS.md#data%20instructions): `lb`, `lw`, `sw`
    - [§ memory layout](MIPS.md#memory%20layout)

## week 7 lecture 2

- datetime: 2025-03-21T09:00:00+08:00/2025-03-21T10:20:00+08:00
- topic: 32-bit immediate, addressing mode, jump range, CISC/RISC
- MIPS architecture
  - [MIPS](MIPS.md)
    - [§ data instructions](MIPS.md#data%20instructions): `lui`
    - [§ pseudo-instructions](MIPS.md#pseudo-instructions): `move`, `blt`, `ble`, `bgt`, `bge`
    - [§ addressing modes](MIPS.md#addressing%20modes)
    - [§ jump instructions](MIPS.md#jump%20instructions): `j`, `jr`
- reduced instruction set computer
  - reduced instruction set computer / antonym ::@:: complex instruction set computer \(CISC\) <p> fun fact: CISC was retroactively coined in contrast to RISC. <!--SR:!2027-11-27,795,440!2028-01-25,836,440-->
  - reduced instruction set computer / characteristics ::@:: Since each instruction \(at least tries to\) do one thing, more instructions are needed in a program. However, executing each instruction is usually faster. Hardware design is simple. <!--SR:!2027-12-20,805,440!2027-12-11,797,440-->
    - reduced instruction set computer / characteristics / motivation ::@:: After quantitative measurement, the most useful instructions and addressing modes are chosen. <!--SR:!2028-01-10,823,440!2025-10-16,150,420-->
    - reduced instruction set computer / characteristics / hardware ::@:: Machine code is usually directly executed on the hardware. <!--SR:!2027-11-17,777,440!2025-10-14,148,420-->
    - reduced instruction set computer / characteristics / memory ::@:: Due to simple hardware, more registers and bigger CPU caches can be equipped. <!--SR:!2027-12-14,800,440!2027-11-19,778,440-->
    - reduced instruction set computer / characteristics / use ::@:: Assembly language is harder to write. Compilers are harder to write as well. <!--SR:!2028-01-12,825,440!2027-11-05,766,440-->
- [complex instruction set computer](../../../../general/complex%20instruction%20set%20computer.md) \(CISC\) ::@:: It is a computer architecture in which single instructions can execute several low-level operations (such as a load from memory, an arithmetic operation, and a memory store) or are capable of multi-step operations or addressing modes within single instructions. <!--SR:!2028-02-08,848,440!2027-11-07,777,440-->
  - complex instruction set computer / characteristics ::@:: Since each instruction may do many things, less instructions are needed in a program. However, executing each instruction is usually slower. Hardware design is complex. <!--SR:!2027-04-03,561,420!2025-10-14,148,420-->
    - complex instruction set computer / characteristics / motivation ::@:: Instructions and addressing modes are chosen to make translation of high-level programming language to assembly easier. <!--SR:!2027-12-21,806,440!2027-11-23,782,440-->
    - complex instruction set computer / characteristics / hardware ::@:: Machine code is usually executed in microcode, which sits in between the hardware and the machine code. <!--SR:!2027-11-05,776,440!2025-10-15,149,420-->
    - complex instruction set computer / characteristics / memory ::@:: Due to complex hardware, less registers and smaller CPU caches can be equipped. <!--SR:!2025-10-14,148,420!2027-11-12,772,440-->
    - complex instruction set computer / characteristics / use ::@:: Assembly language is easier to write. Compilers are easier to write as well. <!--SR:!2027-04-18,573,420!2028-01-23,834,440-->

## week 8 lecture

- datetime: 2025-03-24T13:30:00+08:00/2025-03-24T14:50:00+08:00, PT1H20M
- topic: MIPS recursion, computer arithmetic, addition, subtraction, overflow
- two's complement
  - two's complement / addition
  - two's complement / subtraction
- [method of complements](../../../../general/method%20of%20complements.md) ::@:: It is a technique to encode a symmetric range of positive and negative integers in a way that they can use the same algorithm (or mechanism) for addition throughout the whole range. <!--SR:!2027-11-14,784,440!2027-11-25,784,440-->
  - method of complements / binary method ::@:: The method of complements is especially useful in binary \(radix 2\) since the ones' complement is very easily obtained by inverting each bit \(changing '0' to '1' and vice versa\). Adding 1 to get the two's complement can be done by simulating a carry into the least significant bit. <!--SR:!2027-04-17,564,420!2027-12-19,804,440-->
- two's complement
  - two's complement / addition
    - two's complement / addition / overflow ::@:: The last two bits of the carry row \(reading right-to-left\) contain vital information: whether the calculation resulted in an arithmetic overflow, a number too large for the binary system to represent. An overflow condition exists when these last two bits are different from one another. <!--SR:!2027-12-13,799,440!2025-10-15,149,420-->
      - two's complement / addition / overflow / alternative ::@:: When two numbers have the same sign, but the resulting number has a different sign from the first number, then overflow occurs. <!--SR:!2027-05-05,577,420!2028-02-07,847,440-->
  - two's complement / subtraction
    - two's complement / subtraction / overflow ::@:: Overflow is detected the same way as for addition, by examining the two leftmost (most significant) bits of the borrows; overflow has occurred if they are different. <!--SR:!2028-01-18,830,440!2027-04-19,574,420-->
      - two's complement / addition / overflow / alternative ::@:: When two numbers have different signs, but the resulting number has a different sign from the first number, then overflow occurs. <!--SR:!2028-01-17,829,440!2026-11-01,434,400-->
- MIPS architecture
  - [MIPS](MIPS.md)
    - [§ instructions](MIPS.md#data%20instructions): two's complement is used to represent signed integers
    - [§ arithmetic instructions](MIPS.md#arithmetic%20instructions): `addu`, `subu`, `addiu`
    - [§ comparison instructions](MIPS.md#comparison%20instructions): `sltu`, `sltui`
    - [§ data instructions](MIPS.md#data%20instructions): `lhu`, `lbu`
    - [§ interrupt](MIPS.md#interrupt)
- [interrupt](../../../../general/interrupt.md) ::@:: It is a request for the processor to interrupt currently executing code \(when permitted\), so that the event can be processed in a timely manner. <!--SR:!2027-11-03,774,440!2028-01-09,822,440-->
- sign extension
  - sign extension / zero extension

## midterm examination

- datetime: 2025-03-24T19:30:00+08:00/2025-03-24T21:00:00+08:00, PT1H30M
  - actual: 2025-03-24T19:30:00+08:00/2025-03-24T21:10:00+08:00, PT1H40M
- venue: Lecture Theater A, Academic Building; Lecture Theater B, Academic Building
- format
  - calculator: no
  - cheatsheet: no
  - referencing: closed book, closed notes
  - provided: \(none\)
  - questions: multiple choice questions ×17, long questions ×5
- grades: 91/100 → 96/100
  - statistics
    - timestamps: 2025-03-27T15:17+08:00 → 2025-03-29+08:00
    - mean: ? \(provided: 71.56\) → 70.54
    - standard deviation: ? \(provided: 16.41\) → ?
    - low: 0 → 0
    - lower quartile: 60 → 60
    - median: 73 \(provided: 73\) → 73
    - upper quartile: 84 → 84
    - high: 97 → 100
    - distribution: ![midterm examination distribution](attachments/midterm%20examination%20distribution.png) → ?
- report
  - race hazards \(–4\) ::@:: It seems like the rules for deciding if a state is _forbidden_ is more complex than expected. See above. <!--SR:!2028-01-04,818,440!2025-10-16,150,420-->
  - time limit ::@:: Plenty of time left. In fact, the instructor added an extra 10 minutes... <!--SR:!2027-11-19,779,440!2028-02-06,846,440-->
- check
  - datetime: 2025-03-28T19:00:00+08:00 → 2025-03-28T20:30:00+08:00
  - venue: Lecture Theater C, Academic Building
  - report
    - MIPS programming \(+5\) ::@:: I think the TA gave up looking at the very messy organization of the code... <!--SR:!2027-12-29,813,440!2028-01-18,830,440-->

## week 8 lab

- datetime: 2025-03-25T15:00:00+08:00/2025-03-25T15:50:00+08:00, PT50M
- topic: MIPS procedures
- MIPS architecture
  - [MIPS](MIPS.md)
    - [§ procedures](MIPS.md#procedures)
    - [§ memory layout](MIPS.md#memory%20layout): stack
    - [§ pseudo-instructions](MIPS.md#pseudo-instructions): `push`, `pop`
    - [§ calling conventions](MIPS.md#calling%20conventions)
    - [§ O32 calling convention](MIPS.md#O32%20calling%20convention): passing more than 4 arguments

## week 8 tutorial

- datetime: 2025-03-25T18:00:00+08:00/2025-03-25T18:50:00+08:00, PT50M
- topic: MIPS branches, jump instructions
- MARS
  - [MARS](MARS.md)
    - [§ system calls](MARS.md#system%20calls)
  - MARS / generate random numbers ::@:: Usually in C, we use the current system timestamp as the RNG seed. Then we generate random numbers, limiting its range using the modulo operator. <p> We can do the same in MARS using syscalls. <!--SR:!2027-04-16,563,420!2027-11-15,775,440-->
- MIPS architecture
  - [MIPS](MIPS.md)
    - [§ jump instructions](MIPS.md#jump%20instructions): `beq`, `bne`, `j`
    - [§ arithmetic instructions](MIPS.md#arithmetic%20instructions): `addu`, `subu`, `addiu`
    - [§ comparison instructions](MIPS.md#comparison%20instructions): `slt`, `slti`
    - [§ control flow](MIPS.md#control%20flow)

## week 8 lecture 2

- datetime: 2025-03-28T09:00:00+08:00/2025-03-28T10:20:00+08:00, PT1H20M
- topic: arithmetic logic unit \(ALU\)
- [arithmetic logic unit](../../../../general/arithmetic%20logic%20unit.md) \(ALU\) ::@:: It is a combinational digital circuit that performs arithmetic and bitwise operations on integer binary numbers. <!--SR:!2028-01-28,838,440!2027-12-18,803,440-->
  - arithmetic logic unit / processor ::@:: It is an important part of a processor, with the other parts being cache, control unit, and registers. <!--SR:!2027-11-18,777,440!2028-02-02,842,440-->
  - arithmetic logic unit / bit width ::@:: It depends on the ISA. For examples, MIPS requires 32-bit ALUs. <p> In theory, we could build an _n_-bit ALU by connecting _n_ 1-bit ALUs together. <!--SR:!2027-12-28,812,440!2027-12-01,789,440-->
  - arithmetic logic unit / functions ::@:: arithmetic, bit shift, bitwise logical, other \(passthrough\) <!--SR:!2027-12-02,799,440!2028-01-02,816,440-->
    - arithmetic logic unit / functions / selection ::@:: An ALU can carry out many functions. An _opcode_ input is passed to a selector/multiplexor to select the correct output. <!--SR:!2027-11-04,775,440!2025-10-15,149,420-->
- [adder](../../../../general/adder%20(electronics).md) ::@:: It is a digital circuit that performs addition of numbers. <!--SR:!2027-11-30,788,440!2027-10-27,768,440-->
  - adder / half adder ::@:: It adds two single binary digits $A$ and $B$. It has two outputs, sum \($S$\) and carry \($C$\). The carry signal represents an [overflow](../../../../general/integer%20overflow.md) into the next digit of a multi-digit addition. The value of the sum is $2C+S$. <!--SR:!2027-11-06,767,440!2027-11-12,773,440-->
    - add / half adder / implementation ::@:: The simplest half-adder design, pictured on the right, incorporates an [XOR gate](../../../../general/XOR%20gate.md) for $S$ and an [AND gate](../../../../general/AND%20gate.md) for $C$. The Boolean logic for the sum \(in this case $S$\) will be $A\oplus B$ whereas for the carry \($C$\) will be $A\cdot B$. With the addition of an [OR gate](../../../../general/OR%20gate.md) to combine their carry outputs, two half adders can be combined to make a full adder. <!--SR:!2027-03-03,552,420!2027-12-20,805,440-->
    - add / half adder / schematic ::@:: [Schematic](../../../../general/schematic.md) of half adder implemented with one [XOR gate](../../../../general/XOR%20gate.md) and one [AND gate](../../../../general/AND%20gate.md): <p> ![Schematic of half adder implemented with one XOR gate and one AND gate.](../../../../archives/Wikimedia%20Commons/Half%20Adder.svg) <!--SR:!2027-05-01,575,420!2027-11-18,778,440-->
  - adder / full adder ::@:: It adds binary numbers and accounts for values carried in as well as out. A one-bit full-adder adds three one-bit numbers, often written as $A$, $B$, and $C_{in}$; $A$ and $B$ are the operands, and $C_{in}$ is a bit carried in from the previous less-significant stage. The circuit produces a two-bit output. <!--SR:!2027-11-28,796,440!2027-12-10,806,440-->
    - adder / full adder / implementation ::@:: A full adder can be implemented in many different ways such as with a custom [transistor](../../../../general/transistor.md)-level circuit or composed of other gates. The most common implementation is with: $$\begin{aligned} S & = A\oplus B\oplus C_{in} \\ C_{out} & = (A\cdot B)+(C_{in}\cdot (A\oplus B)) \end{aligned}$$ The above expressions for $S$ and $C_{in}$ can be derived from using a [Karnaugh map](../../../../general/Karnaugh%20map.md) to simplify the truth table. <!--SR:!2027-04-04,589,420!2028-01-11,824,440-->
    - adder / full adder / schematic ::@:: [Schematic](../../../../general/schematic.md) of full adder implemented with two [XOR gates](../../../../general/XOR%20gate.md), two [AND gates](../../../../general/AND%20gate.md), one [OR gate](../../../../general/OR%20gate.md): <p> ![Schematic of full adder implemented with two XOR gates, two AND gates, one OR gate.](../../../../archives/Wikimedia%20Commons/Full-adder%20logic%20diagram.svg) <!--SR:!2027-04-16,588,420!2027-11-21,780,440-->
  - adder / ripple-carry adder ::@:: It is possible to create a logical circuit using multiple full adders to add _N_-bit numbers. Each full adder inputs a $C_{in}$, which is the $C_{out}$ of the previous adder. This kind of adder is called a __ripple-carry adder__ \(RCA\), since each carry bit "ripples" to the next full adder. The first \(and only the first\) full adder may be replaced by a half adder \(under the assumption that $C_{in}=0$\). <!--SR:!2028-01-07,820,440!2028-01-27,837,440-->
    - adder / ripple-carry adder / characteristics ::@:: The layout of a ripple-carry adder is simple, which allows fast design time; however, the ripple-carry adder is relatively slow, since each full adder must wait for the carry bit to be calculated from the previous full adder. <!--SR:!2027-12-12,798,440!2027-12-26,810,440-->
- method of complements
- arithmetic logic unit
  - arithmetic logic unit / signals ::@:: data, opcode, status \(outputs, inputs\) <!--SR:!2028-01-29,839,440!2027-11-22,781,440-->
    - arithmetic logic unit / signals / data ::@:: 2 inputs, 1 output; their bit widths are usually the same, and same as the native ISA <!--SR:!2028-01-31,841,440!2028-01-22,833,440-->
    - arithmetic logic unit / signals / opcode ::@:: It conveys to the ALU an operation selection code, which is an enumerated value that specifies the desired arithmetic or logic operation to be performed by the ALU. <p> Passing it to a multiplexor/selector can be used to choose the right output. <!--SR:!2027-11-24,783,440!2027-12-23,808,440-->
    - arithmetic logic unit / signals / status outputs ::@:: carry-out, zero, negative, overflow, parity, etc. <!--SR:!2027-12-22,807,440!2028-01-01,815,440-->
    - arithmetic logic unit / signals / status inputs ::@:: carry-in, etc. <!--SR:!2027-12-24,808,440!2027-04-03,588,420-->
  - arithmetic logic unit / functions
    - arithmetic logic unit / functions / bitwise operations ::@:: Use the corresponding logic gates. <!--SR:!2025-10-16,150,420!2027-12-06,793,440-->
    - arithmetic logic unit / functions / addition ::@:: Use full-adders. Two common ways to add multiple-bit numbers are _ripple carry_ and _carry lookahead_. <!--SR:!2027-11-23,791,440!2027-11-08,778,440-->
    - arithmetic logic unit / functions / subtraction ::@:: Assuming signed integers are represented using two's complement. <p> The circuit for addition can be reused. However, the second operand \(the _subtrahend_\) needs to be inverted and then added one to get its complement. One way to implement this is to invert the second operand \(by setting an additional input _binvert_ to 1\), and additionally set the carry-in of the LSB full-adder to 1. We could combine these two inputs \(_binvert_ + carry-in of LSB\) as an input _bnegate_. <!--SR:!2028-01-05,819,440!2027-04-24,568,420-->
    - arithmetic logic unit / functions / comparison ::@:: To check if `$s < $t`, we can use `slt $d, $s, $t`. This is equivalent to checking `$s - $t < 0`, i.e. checking if the sign bit \(assuming no overrflow\) of `$s - $t` equals 1. <p> To implement `slt`, we can add a _less_ input to all ALUs, which is passthrough as the _less_ output \(opcode: SLT\). Then, the _less_ input is always zero except for the LSB ALU, which is connected to a _set_ output of the MSB ALU. The _set_ output is simply the subtraction MSB bit. \(__this course__: The lecture slides do not handle overflows. To handle overflows, detect if a subtraction overflow is possible, i.e. the two operand sign bits are different, and if so, the _set_ output uses the sign bit of the second operand.\) <p> Remember to also set the carry-in bit of the LSB to perform subtraction properly. <!--SR:!2027-03-10,568,420!2026-01-18,207,360-->
    - arithmetic logic unit / functions / equal ::@:: To check if `$s = $t` \(e.g. `beq`\), this is equivalent to checking `$s - $t == 0`. <p> To implement this, it is similar to subtraction, but you additionally add a NOR gate acting on all the output bits. This produces a _zero_ status output, which indicates if the subtraction result is zero. Also in this case, you do not need to worry about overrflow affecting the result \(i.e. it is impossible for two distinct signed integers differing so much that their difference overflows to zero\). <!--SR:!2026-11-04,437,400!2027-11-04,765,440-->
  - arithmetic logic unit / diagram ::@:: An arithmetic logic unit and its associated status register. The stored carry-out is connected to carry-in to facilitate efficient carry propagation: <p> ![An arithmetic logic unit and its associated status register.](../../../../archives/Wikimedia%20Commons/AluStatusRegister.svg) <!--SR:!2027-03-17,573,420!2028-01-18,829,440-->
  - arithmetic logic unit / note ::@:: \(__this course__: Our 32-bit ALU has an AND gate \(00\), a OR gate \(01\), a full adder \(10\), and _less_ passthrough \(11\). Additionally, it has a _bnegate_ input as the 3rd control signal. Thus we support 5 operations: 000: AND; 001: OR; 010: ADD; 110: SUB; 111: SLT.\) <!--SR:!2026-08-21,400,400!2027-05-10,582,420-->
- adder
  - adder / carry-lookahead adder ::@:: Two signals \($P$ and $G$\) are introduced for each bit position, based on whether a carry is propagated through from a less significant bit position \(at least one input is a 1\), generated in that bit position \(both inputs are 1\), or killed in that bit position \(both inputs are 0\). In most cases, $P$ is simply the sum output of a half adder and $G$ is the carry output of the same adder. After $P$ and $G$ are generated, the carries for every bit position are created. <p> Note: $P = A + B$ \(described in the first sentence\) or $P = A \oplus B$ \(the output of a half-adder\) are both acceptable, since if $A = B = 1$, the next carry bit is generated, so whether the current carry bit is propagated has no effect. \(__this course__: use $A \oplus B$\) <!--SR:!2027-12-21,806,440!2027-03-09,557,420-->
    - adder / carry-lookahead adder / carry bits ::@:: The _n_-th \(0-based\) carry bit is: $$C_n = G_{n - 1} + G_{n - 2} P_{n - 1} + \cdots + G_0 P_1 \cdots P_{n - 1} + C_0 P_0 \cdots P_{n - 1} \,,$$ where $C_0$ is the LSB carry bit. <p> The above can be intutively understood: A carry bit is generated or propagated from any of the previous/lower carry bits. <!--SR:!2027-12-03,791,440!2026-01-18,207,360-->
    - adder / carry-lookahead adder / characteristics ::@:: Now we can add the two numbers and then the carry bits in parallel without rippling. <p> This is possible because electronic chips are becoming cheaper and denser. <!--SR:!2027-12-07,794,440!2027-05-07,580,420-->

## week 9 lecture

- datetime: 2025-03-31T13:30:00+08:00/2025-03-31T14:50:00+08:00, PT1H20M
- topic: multiplication
- [binary multiplier](../../../../general/binary%20multiplier.md) ::@:: It is an electronic circuit used in digital electronics, such as a computer, to multiply two binary numbers. <!--SR:!2028-01-30,840,440!2028-01-08,821,440-->
  - binary multiplier / binary long multiplication ::@:: The method taught in school for multiplying decimal numbers is based on calculating partial products, shifting them to the left and then adding them together. <p> A binary computer does exactly the same multiplication as decimal numbers do, but with binary numbers. In binary encoding each long number is multiplied by one digit \(either 0 or 1\), and that is much easier than in decimal, as the product by 0 or 1 is just 0 or the same number. Therefore, the multiplication of two binary numbers comes down to calculating partial products \(which are 0 or the first number\), shifting them left, and then adding them together \(a binary addition, of course\). <!--SR:!2028-01-15,827,440!2027-12-15,801,440-->
  - binary multiplier / bit width ::@:: Ignoring the sign bit, multiplying a _n_-bit number with a _m_-bit number yields at most a _n_&nbsp;+&nbsp;_m_-bit number. <!--SR:!2025-10-14,148,420!2027-11-16,776,440-->
  - binary multiplier / binary long multiplication
    - binary multiplier / binary long multiplication / implementation, naive ::@:: We have a _n_-bit _multiplicand_ \(first operand\) and a _n_-bit _multiplier_ \(second operand\). Assume both integers are unsigned. <p> First, zero-extend the multiplicand to 2\*_n_ bits. Have another 2\*_n_-bit register to store the _product_, initialized to all 0s. <p> Perform the following steps _n_ times: Add the multiplicand to the product if the LSB of the multiplier is 1. Then shift the multiplicand left by 1 bit and the multiplier right by 1 bit. <!--SR:!2026-10-26,430,400!2027-05-27,596,420-->
      - binary multiplier / binary long multiplication / implementation, naive / observations ::@:: Only half of the zero-extended multiplicand bits ever contain useful information. Also, using a 2\*_n_-bit ALU is slower than using a _n_-bit ALU. <p> We also note that later additions do not affect the product LSBs. This hints at a better implementation... <!--SR:!2028-01-24,835,440!2028-01-03,817,440-->
    - binary multiplier / binary long multiplication / implementation, improved ::@:: We have a _n_-bit _multiplicand_ \(first operand\) and a _n_-bit _multiplier_ \(second operand\). Assume both integers are unsigned. <p> First, have another 2\*_n_-bit register to store the _product_. <p> Perform the following steps _n_ times: Add the multiplicand to the upper _n_ bits of product if the LSB of the multiplier is 1. This addition may overflow by at most 1 bit: save it. Then shift the _product_ and the multiplier right by 1 bit. If the previous addition overflows, set the highest bit of product to 1. <!--SR:!2026-10-29,432,400!2028-01-16,828,440-->
      - binary multiplier / binary long multiplication / implementation, improved / observations ::@:: No multiplicand bits are wasted. We can keep using a _n_-bit ALU. <p> We also note that the product contains 1 _more_ bit of useful information and the multiplier contains 1 _less_ bit of useful information per addition. This means we can combine the product and multiplier registers into one 2\*_n_-bit register, where initially the multiplier value is stored into the lower _n_ bits, and then shift them right by 1 bit together per addition. <!--SR:!2027-05-11,583,420!2027-04-15,562,420-->
    - binary multiplier / binary long multiplication / implementation ::@:: We have a _n_-bit _multiplicand_ \(first operand\) and a _n_-bit _multiplier_ \(second operand\). Assume both integers are unsigned. <p> First, have another 2\*_n_-bit register to store the _product_. Store the multiplier into \(the lower bits of\) the register. <p> Perform the following steps _n_ times: Add the multiplicand to the upper _n_ bits of product if the LSB of the product is 1. This addition may overflow by at most 1 bit: save it. Then shift the _product_ right by 1 bit. If the previous addition overflows, set the highest bit of product to 1. <!--SR:!2027-01-04,467,422!2025-12-17,157,441-->
  - binary multiplier / signed ::@:: The simplest idea is to consider the sign explicitly. Both the multiplicand and the multiplier are forced to become positive. Multiply them to get a positive product. Finally, if the original multiplicand and multiplier signs disagree, negate the product. <p> A more efficient and elegant idea is [Booth's multiplication algorithm](../../../../general/Booth's%20multiplication%20algorithm.md). <!--SR:!2027-11-11,771,440!2027-11-26,785,440-->
- MIPS architecture
  - [MIPS](MIPS.md)
    - [§ instructions](MIPS.md#data%20instructions): two's complement is used to represent signed integers
    - [§ arithmetic instructions](MIPS.md#arithmetic%20instructions): `mult`, `multu`

## week 9 lab

- datetime: 2025-04-01T15:00:00+08:00/2025-04-01T15:50:00+08:00, PT50M
- status: unscheduled, midterm break

## week 9 tutorial

- datetime: 2025-04-01T18:00:00+08:00/2025-04-01T18:50:00+08:00, PT50M
- status: unscheduled, midterm break

## week 9 lecture makeup

- datetime: 2025-04-02T14:00:00+08:00/2025-04-02T15:30:00+08:00, PT1H30M
- topic: multiplication, division
- status: makeup, online, recorded
- MIPS architecture
  - [MIPS](MIPS.md)
    - [§ data instructions](MIPS.md#bitwise%20instructions): `mflo`, `mfhi`
  - MIPS architecture / multiplication ::@:: The product register is `$HI:$LO`. That is, `$HI` is its upper half bits and `$LO` is its lower half bits. <!--SR:!2025-12-21,156,441!2026-01-03,164,441-->
    - MIPS architecture / multiplication / overflow ::@:: If you consider the entire product register `$HI:$LO` together, multiplication never overflows. However, if you force yourself to consider one register only \(i.e. if `$LO` can store the product\), then an overflow occurs if `$HI` bits are not all 0 for unsigned multiplication or `$HI` bits are not all the sign bit of `$LO` for signed multiplication. \(__this course__: Consider one register only.\) <!--SR:!2025-12-31,162,442!2025-10-27,106,422-->
- MIPS architecture
  - [MIPS](MIPS.md)
    - [§ bitwise instructions](MIPS.md#bitwise%20instructions): `srl`, `sra`
- [binary divider](../../../../general/binary%20divider.md) ::@:: It is an electronic circuit used in digital electronics, such as a computer, to divide two binary numbers. <!--SR:!2025-12-17,148,442!2025-12-16,147,442-->
  - binary divider / binary long division ::@:: Similar to long division taught in school. <!--SR:!2025-12-09,149,442!2026-01-01,163,442-->
    - binary divider / binary long division / implementation, naive ::@:: We have a _n_-bit _dividend_ \(first operand\) and a _n_-bit _divisor_ \(second operand\). Assume both integers are unsigned. <p> First, zero-extend the dividend to 2\*_n_ bits, and also call it _remainder_. Zero-extend the divisor to 2\*_n_ bits as well, with the original divisor in the upper bits. Have another _n_-bit register to store the _quotient_, initialized to all 0s. <p> Perform the following steps _n_+1 times: Subtract divisor from dividend/remainder. If the MSB is 1 \(dividend/remainder is negative interpreted as a signed number\), undo \(add divisor\). Otherwise, keep it unchanged. Shift the quotient left by 1 bit, and set its rightmost bit to 0 if undo happens or 1 otherwise. Shift the divisor right by 1 bit. <!--SR:!2026-08-23,321,399!2025-11-15,121,422-->
      - binary divider / binary long division / implementation, naive / variation ::@:: The above steps are in the lecture slides. Below is a simpler variant: The registers are initialized in the same way. Then the remaining steps are different. <p> Perform the following steps _n_ \(not _n_+1\) times: Shift the divisor right by 1 bit. Shift the quotient left by 1 bit. Subtract divisor from dividend/remainder. If the MSB is 1 \(dividend/remainder is negative interpreted as a signed number\), undo \(add the divisor\). Otherwise, keep it unchanged. Set the rightmost bit of quotient to 0 if undo happens or 1 otherwise. <p> Isn't it so much better? <!--SR:!2025-12-17,148,442!2025-12-18,158,442-->
      - binary divider / binary long division / implementation, naive / observations ::@:: Only half of the zero-extended divisor bits ever contain useful information. Also, using a 2\*_n_-bit ALU is slower than using a _n_-bit ALU. <p> We also note that the quotient contains 1 _more_ bit of useful information and the dividend/remainder contains 1 _less_ bit of useful information per subtraction. This means we can combine the dividend/remainder and quotient registers into one 2\*_n_-bit register, where initially the dividend value is stored into the lower _n_ bits, and then shift them left by 1 bit together per subtraction. This hints at a better implementation... <!--SR:!2025-12-29,160,439!2025-12-27,158,441-->
    - binary divider / binary long division / implementation ::@:: We have a _n_-bit _dividend_ \(first operand\) and a _n_-bit _divisor_ \(second operand\). Assume both integers are unsigned. <p> First, have another 2\*_n_-bit register to store the _dividend_/_remainder_/_quotient_. Store the dividend into \(the lower bits of\) the register. <p> Before the first iteration, shift dividend/remainder/quotient left by 1 bit. Perform the following steps _n_ times: Subtract divisor from dividend/remainder/quotient. If the MSB is 1 \(dividend/remainder/quotient is negative interpreted as a signed number\), undo \(add divisor\). Otherwise, keep it unchanged. Shift dividend/remainder/quotient left by 1 bit, and set its rightmost bit to 0 if undo happens or 1 otherwise. After the last iteration, shift the upper half bits of dividend/remainder/quotient right by 1 bit \(correction\). <!--SR:!2025-11-12,118,419!2026-08-05,320,399-->
      - binary divider / binary long division / implementation / variation ::@:: The above steps are in the lecture slides. Below is a simpler variant: The registers are initialized in the same way. Then the remaining steps are different. <p> Perform the following steps _n_ times: Shift dividend/remainder/quotient left by 1 bit. Subtract divisor from dividend/remainder/quotient. If the MSB is 1 \(dividend/remainder/quotient is negative interpreted as a signed number\), undo \(add divisor\). Otherwise, keep it unchanged. Set its rightmost bit to 0 if undo happens or 1 otherwise. <p> Isn't it so much better? No correction step is needed! <!--SR:!2025-12-16,156,442!2026-08-20,319,402-->
      - binary divider / binary long division / implementation / observations ::@:: No divisor bits are wasted. We can keep using a _n_-bit ALU. <!--SR:!2025-12-18,158,441!2026-01-03,164,442-->
  - binary divider / signed ::@:: The idea is to consider the sign explicitly. Both the dividend and the divisor are forced to become positive. Divide them to get a positive remainder and quotient. If the original dividend and divisor signs disagree, negate the quotient. Negate the remainder if the original dividend is negative. A mnemonic for the remainder sign is: dividend=divisor\*quotient+remainder. <p> Unfortunately \(or fortunately for your examinations\) there is no [Booth's multiplication algorithm](../../../../general/Booth's%20multiplication%20algorithm.md) analog for division. <!--SR:!2025-12-18,158,442!2025-12-27,158,442-->
- MIPS architecture
  - [MIPS](MIPS.md)
    - [§ arithmetic instructions](MIPS.md#arithmetic%20instructions): `div`, `divu`

> Dear student of COMP2611 L2,
>
> As you may know, we are going to lose quite a number of lectures in the front \(i.e. we will lose 3 classes in April and 1 class in May\). Because of this, we will have 1 less class than the other two COMP2611 sections. That will put our section in an extremely disadvantageous position when it comes to doing HW4 and preparing for the final exam.
>
> Therefore, I decided to hold an online makeup class this Wednesday \(2/4\) from 2:00pm to 3:30pm. This time is carefully chosen - it happens during the mid-semester break and we will do it in the afternoon (so that you don't need to wake up early). The link for the makeup class is at : \[redacted\]
>
> The class will be video recorded and I will send you the video link as soon as I have received it \(likely to be on this Wed or Thur\). During the makeup class, we will do a quick revision of versions 2 and 3 of the multiplication algorithm and finish the division algorithms \(i.e. slides 38-61 of \[redacted\] \).
>
> Moreover, I added some additional slides to the arithmetic note set to explain the multiplication and division algorithms. I am attaching this modified arithmetic note set to the email in case it would be useful. In this modified note set, I added slides 39-42 and slides 57-75.
>
> Hope this helps! I hope you will have plenty of rest in the break and I also hope you will have a happy and fruitful break!
>
> \[redacted\]

## week 9 lecture 2

- datetime: 2025-04-04T09:00:00+08:00/2025-04-04T10:20:00+08:00, PT1H20M
- status: unscheduled, midterm break

## week 10 lecture

- datetime: 2025-04-07T13:30:00+08:00/2025-04-07T14:50:00+08:00, PT1H20M
- topic: floating-point arithmetic
- tags: optional
- [floating-point arithmetic](../../../../general/floating-point%20arithmetic.md) \(FP\) ::@:: It is arithmetic on subsets of real numbers formed by a _significand_ \(a signed sequence of a fixed number of digits in some base\) multiplied by an integer power of that base. <!--SR:!2025-12-31,162,442!2025-12-29,160,442-->
  - floating-point arithmetic / addition ::@:: Align decimal points by shifting the number with the smaller exponent. Add the significands. Normalize and check for underflow and overflow \(may set exceptions\). Round \(depends on rounding mode\). Start from the normalize step again if not normalized. Otherwise, it is the result. <!--SR:!2025-12-28,159,442!2025-12-24,160,442-->
    - floating-point arithmetic / addition / hardware ::@:: Probably contains an integer adder. Much more complicated than an integer adder. Likely requires multiple clock cycles, pipelined; otherwise would make one clock cycle too long. <!--SR:!2025-12-16,156,442!2025-12-18,149,442-->
  - floating-point arithmetic / multiplication ::@:: Add the exponents. Multiply the significands. Normalize and check for underflow and overflow \(may set exceptions\). Round \(depends on rounding mode\). Start from the normalize step again if not normalized. Otherwise, continue. Set the sign bit from the operands. <!--SR:!2026-01-03,164,442!2025-11-16,122,419-->
    - floating-point arithmetic / multiplication / hardware ::@:: Probably contains an integer multiplier. Much more complicated than an integer multiplier. Likely requires multiple clock cycles, pipelined; otherwise would make one clock cycle too long. <!--SR:!2025-12-28,159,442!2025-12-19,150,442-->
  - floating-point arithmetic / operations ::@:: addition, subtraction, multiplication, division, reciprocal, square root, integer conversion, etc. <!--SR:!2025-12-29,160,442!2025-12-27,158,442-->
- MIPS architecture
  - [MIPS](MIPS.md)
    - [§ floating point](MIPS.md#floating%20point)
    - [§ floating-point instructions](MIPS.md#floating-point%20instructions): `add.s`, `add.d`, `sub.s`, `sub.d`, `mul.s`, `mul.d`, `div.s`, `div.d`, `c.*.s` \(`*` is `eq`, `neq`, `lt`, `le`, `gt`, `ge`\), `c.*.d` \(`*` is `eq`, `neq`, `lt`, `le`, `gt`, `ge`\), `bc1t`, `bc1f`, `lwc1`, `swc1`
- floating-point arithmetic
  - floating-point arithmetic / accuracy problems ::@:: The fact that floating-point numbers cannot accurately represent all real numbers, and that floating-point operations cannot accurately represent true arithmetic operations, leads to many surprising situations. This is related to the finite precision with which computers generally represent numbers. <!--SR:!2025-12-31,162,442!2025-12-28,159,442-->
  - floating-point arithmetic / addition
    - floating-point arithmetic / addition / intermediate ::@:: For binary addition or subtraction using careful implementation techniques only a _guard_ bit, a _rounding_ bit and one extra _sticky_ bit need to be carried beyond the precision of the operands. <!--SR:!2025-12-25,156,442!2025-12-22,158,439-->
  - floating-point arithmetic / rounding modes ::@:: Rounding is used when the exact result of a floating-point operation \(or a conversion to floating-point format\) would need more digits than there are digits in the significand. IEEE 754 requires _correct rounding_: that is, the rounded result is as if infinitely precise arithmetic was used to compute the value and then rounded \(although in implementation only three extra bits are needed to ensure this\). There are several different [rounding](../../../../general/rounding.md) schemes \(or _rounding modes_\). <!--SR:!2026-01-02,164,442!2025-12-27,163,441-->

## week 10 lab

- datetime: 2025-04-08T15:00:00+08:00/2025-04-08T15:50:00+08:00, PT50M
- topic: MIPS recursion
- [recursion](../../../../general/recursion.md) ::@:: \(_this_\) occurs when the definition of a concept or process depends on a simpler or previous version of itself. \(_this_\) is used in a variety of disciplines ranging from linguistics to logic. The most common application of \(_this_\) is in mathematics and computer science, where a function being defined is applied within its own definition. <!--SR:!2025-12-13,149,442!2025-12-30,161,442-->
- MIPS architecture
  - [MIPS](MIPS.md)
    - [§ procedures](MIPS.md#procedures): recursion
    - [§ calling conventions](MIPS.md#calling%20conventions)
    - [§ O32 calling convention](MIPS.md#O32%20calling%20convention): `$ra`
    - [§ memory layout](MIPS.md#memory%20layout): stack

## week 10 tutorial

- datetime: 2025-04-08T18:00:00+08:00/2025-04-08T18:50:00+08:00, PT50M
- topic: MIPS machine code, procedures
- MIPS architecture
  - [MIPS](MIPS.md)
    - [§ encoding](MIPS.md#encoding): R format, I format, J format
    - [§ operands](MIPS.md#operands): zero extension, sign extension
    - [§ calling conventions](MIPS.md#calling%20conventions)
    - [§ O32 calling convention](MIPS.md#O32%20calling%20convention): registers, caller-saved, callee-saved
    - [§ procedures](MIPS.md#procedures): caller, callee

## week 10 lecture 2

- datetime: 2025-04-11T09:00:00+08:00/2025-04-11T10:20:00+08:00, PT1H20M
- topic: single-cycle datapath
- [single-cycle processor](../../../../general/single-cycle%20processor.md) ::@:: It is a processor that carries out one instruction in a single clock cycle. <!--SR:!2025-12-26,157,441!2025-12-29,160,439-->
- [classic RISC pipeline](../../../../general/classic%20RISC%20pipeline.md) ::@:: In the history of computer hardware, some early reduced instruction set computer central processing units \(RISC CPUs\) used a very similar architectural solution. <!--SR:!2025-12-19,150,442!2025-12-13,153,439-->
  - classical RISC pipeline / stages ::@:: IF = instruction fetch → ID = instruction decode → EX = execute → MEM = memory access → WB = _register_ write back <!--SR:!2025-12-28,159,441!2025-12-27,163,442-->
- [datapath](../../../../general/datapath.md) ::@:: It is a collection of functional units such as arithmetic logic units \(ALUs\) or multipliers that perform data processing operations, registers, and buses. Along with the control unit it composes the central processing unit \(CPU\). A larger data path can be made by joining more than one data paths using multiplexers. <!--SR:!2026-01-02,164,442!2025-11-10,120,422-->
  - datapath / components ::@:: adder, arithmetic logic unit \(ALU\), data memory, instruction memory, multiplexers, program counter \(PC\), register file, etc. <!--SR:!2025-12-26,163,442!2025-12-26,162,442-->
- classical RISC pipeline
  - classical RISC pipeline / instruction fetch ::@:: The instructions reside in memory that takes one cycle to read. This memory can be dedicated to SRAM, or an Instruction Cache. A 32-bit instruction is fetched from the instruction memory. <!--SR:!2025-12-09,149,442!2025-12-17,148,442-->
    - classical RISC pipeline / instruction fetch / program counter ::@:: The program counter \(PC\) is a register that holds the address that is presented to the instruction memory. The address is presented to instruction memory at the start of a cycle. Then during the cycle, the instruction is read out of instruction memory, and at the same time, a calculation is done to determine the next PC. The next PC is calculated by incrementing the PC by 4, and by choosing whether to take that as the next PC or to take the result of a branch/jump calculation as the next PC. Note that in classic RISC, all instructions have the same length. <!--SR:!2025-12-27,158,439!2025-12-31,162,441-->
    - classical RISC pipeline / instruction fetch / MIPS ::@:: Simplified. A PC counter connected to an adder that adds 4 per cycle \(with pipelining, it is still 4 because the adder still updates the PC directly\) to execute the next instruction. A multiplexer controlled by the _PCSrc_ control signal is added for branching \(to be elaborated later\). The adder connects to the multiplexer. The multiplexer writes back to the PC counter. The PC counter outputs to the instruction memory to output a 32-bit instruction. <p> relevant control signals: __Branch__, __PCSrc__, __Zero__ <!--SR:!2025-12-05,145,439!2025-11-10,116,421-->
  - classical RISC pipeline / instruction decode ::@:: All MIPS, SPARC, and DLX instructions have at most two register inputs. During the decode stage, the indexes of these two registers are identified within the instruction, and the indexes are presented to the register memory, as the address. Thus the two registers named are read from the register file. In the MIPS design, the register file had 32 entries. <!--SR:!2026-01-02,164,442!2025-12-09,149,442-->
    - classical RISC pipeline / instruction decode / branch ::@:: If the instruction decoded is a branch or jump, the target address of the branch or jump is computed in parallel with reading the register file. The branch condition is computed in the following cycle \(after the register file is read\), and if the branch is taken or if the instruction is a jump, the PC in the first stage is assigned the branch target, rather than the incremented PC that has been computed. Some architectures made use of the Arithmetic logic unit \(ALU\) in the Execute stage, at the cost of slightly decreased instruction throughput. \(__this course__: ALUs are used in the execute stage only.\) <!--SR:!2025-11-10,120,422!2025-10-25,104,422-->
    - classical RISC pipeline / instruction decode / MIPS ::@:: Simplified. The `opcode` field \(first 6 bits\) goes to the control unit \(CU\), which then asserts the control signals correctly. The remaining bits are fed into the register file and the ALU used for arithmetic. Multiplexers controlled by the control signals are added as needed so that R format, I format, and J format instructions are decoded correctly and the registers are read correctly. <p> relevant control signals: __RegDst__ <!--SR:!2025-12-17,148,442!2025-12-28,164,441-->
  - classical RISC pipeline / execute ::@:: The Execute stage is where the actual computation occurs. Typically this stage consists of an ALU, and also a bit shifter. It may also include a multiple cycle multiplier and divider. <p> The ALU is responsible for performing Boolean operations \(and, or, not, nand, nor, xor, xnor\) and also for performing integer addition and subtraction. Besides the result, the ALU typically provides status bits such as whether or not the result was 0, or if an overflow occurred. <p> The bit shifter is responsible for shift and rotations. \(__this course__; This stage contains all ALUs. Outside information may put the branching ALU the stage before or after.\) <!--SR:!2025-11-11,117,419!2025-12-30,161,442-->
    - classical RISC pipeline / execute / latency ::@:: - Register-Register Operation \(Single-cycle latency\): Add, subtract, compare, and logical operations. During the execute stage, the two arguments were fed to a simple ALU, which generated the result by the end of the execute stage. <br/> - Memory Reference \(Two-cycle latency\): All loads from memory. During the execute stage, the ALU added the two arguments \(a register and a constant offset\) to produce a virtual address by the end of the cycle. <!--SR:!2025-12-22,158,439!2025-11-11,121,422-->
    - classical RISC pipeline / execute / MIPS ::@:: Simplified. There is a sign extension component for extending the 16-bit immediate. An ALU for arithmetic or calculating memory address runs. A separate ALU for calculating branching address also runs, which feeds into the multiplexer before the PC counter. Multiplexers controlled by the control signals are added as needed. <p> relevant control signals: __ALUOp__, __ALUSrc__, __Branch__, __Zero__ <!--SR:!2025-12-26,163,442!2025-12-16,147,442-->
  - classical RISC pipeline / memory access ::@:: If data memory needs to be accessed, it is done in this stage. <p> During this stage, single cycle latency instructions simply have their results forwarded to the next stage. This forwarding ensures that both one and two cycle instructions always write their results in the same stage of the pipeline so that just one write port to the register file can be used, and it is always available. <!--SR:!2025-12-23,159,441!2025-12-23,159,439-->
    - classical RISC pipeline / memory access / MIPS ::@:: Simplified. There is a data memory component for reading from and writing to the main memory. The memory address is taken from the ALU otherwise for arithmetic. The data is taken from the second read register. _MemRead_ and _MemWrite_ control if the component reads, writes, or does nothing. <p> relevant control signals: __MemRead__, __MemWrite__ <!--SR:!2025-12-21,158,442!2025-12-27,164,442-->
  - classical RISC pipeline / register write back ::@:: During this stage, both single cycle and two cycle instructions write their results into the register file. <!--SR:!2025-12-23,154,441!2025-12-28,159,439-->
    - classical RISC pipeline / register write back / hazard ::@:: Note that two different stages are accessing the register file at the same time—the decode stage is reading two source registers, at the same time that the writeback stage is writing a previous instruction's destination register. On real silicon, this can be a hazard \(see below for more on hazards\). That is because one of the source registers being read in decode might be the same as the destination register being written in writeback. When that happens, then the same memory cells in the register file are being both read and written the same time. On silicon, many implementations of memory cells will not operate correctly when read and written at the same time. <!--SR:!2026-01-02,164,442!2026-01-03,164,441-->
    - classical RISC pipeline / register write back / MIPS ::@:: Simplified. A multiplexer controlled by _MemToReg_ is fed the output of ALU for arithmetic and the data memory output. _RegWrite_ controls the register file if the multiplexer output writes back to the destination register. <p> relevant control signals: __MemToReg__, __RegWrite__ <!--SR:!2025-12-28,164,442!2025-12-30,161,442-->

## week 11 lecture

- datetime: 2025-04-14T13:30:00+08:00/2025-04-14T14:50:00+08:00, PT1H20M
- topic: single-cycle control
- [control unit](../../../../general/control%20unit.md) \(CU\) ::@:: It is a component of a computer's central processing unit \(CPU\) that directs the operation of the processor. A CU typically uses a binary decoder to convert coded instructions into timing and control signals that direct the operation of the other units \(memory, arithmetic logic unit and input and output devices, etc.\). <!--SR:!2026-01-03,164,442!2025-12-17,148,442-->
  - control unit / MIPS ::@:: Our CPU uses two-level decoding. The `opcode` field is decoded by the main CU, which outputs a 2-bit _ALUOp_. The ALU control unit takes the 2-bit _ALUOp_ and the 6-bit `funct` field and outputs a 4-bit ALU control signal. <!--SR:!2025-12-26,157,439!2025-12-15,155,442-->
    - control unit / MIPS / one-level decoding ::@:: If one-level decoding is used, then the ALU control unit takes the full 6-bit `opcode` field instead of the 2-bit _ALUOp_. More input bits are required, and the logic is potentially more complicated and slower. <!--SR:!2025-12-15,155,442!2025-12-16,156,442-->
    - control unit / MIPS / _ALUOp_ ::@:: \(__this course__: Our _ALUOp_ contains two bits. The operations: 00: ignore `funct`, force ADD; 01/X1: ignore `funct`, force SUBTRACT; 10/1X: decode `funct`; 11: undefined. 10 is only used with R format, because it has the `funct` field. 00 is used for memory access instructions. 01 is used for branching instructions. <p> We can implement converting the 8-bit inputs into 4-bit inputs using simple logic gates, simplifying it using many don't care values.\) <!--SR:!2025-11-10,111,422!2025-11-09,115,422-->
    - control unit / MIPS / arithmetic logic unit ::@:: \(__this course__: Our 32-bit ALU has an AND gate \(00\), a OR gate \(01\), a full adder \(10\), and _less_ passthrough \(11\). Additionally, it has a _bnegate_ input as the 3rd control signal. Thus we support 5 operations: 000: AND; 001: OR; 010: ADD; 110: SUB; 111: SLT. <p> But our ALU control signal is 4 bit! We add another bit \(unexplained\), and the above functions has this bit as 0. We add a new function: 1100: NOR. No idea why they do that.\) <!--SR:!2026-01-02,164,442!2026-10-22,401,421-->
    - control unit / MIPS / signals ::@:: 9 of them \(10 bits\): _ALUOp_ \(2 bits\), _ALUSrc_, _Jmp_, _PCSrc_ \(_Branch_ AND _Zero_\), _MemRead_, _MemToReg_, _MemWrite_, _RegDst_, _RegWrite_ <!--SR:!2025-12-30,161,442!2025-12-11,151,442-->
    - control unit / MIPS / _RegDst_ ::@:: 0: `rt` as destination register; 1: `rd` as destination register <!--SR:!2025-12-31,162,442!2025-12-15,146,442-->
    - control unit / MIPS / _RegWrite_ ::@:: 1: write to the destination register <!--SR:!2025-12-06,146,442!2025-12-31,162,442-->
    - control unit / MIPS / _ALUSrc_ ::@:: 0: second read register; 1: sign-extended 16-bit immediate <!--SR:!2025-12-25,156,442!2025-12-07,147,439-->
    - control unit / MIPS / _PCSrc_ ::@:: 0: use PC+4; 1: use calculated branch address <p> It is calculated from _Branch_ \(from the main CU\) AND _Zero_ \(from the ALU for arithmetic\). <!--SR:!2025-12-18,149,442!2025-12-16,147,442-->
    - control unit / MIPS / _MemRead_ ::@:: 1: read from the main memory <!--SR:!2026-01-01,163,442!2025-12-15,146,442-->
    - control unit / MIPS / _MemWrite_ ::@:: 1: write to the main memory <!--SR:!2025-12-27,158,442!2025-12-20,157,439-->
    - control unit / MIPS / _MemToReg_ ::@:: 0: write back uses ALU for arithmetic; 1: write back uses value read from the main memory <!--SR:!2026-01-02,164,441!2025-12-20,155,439-->
    - control unit / MIPS / implementation ::@:: Using a truth table, adding don't cares for simplification, we can use a PLA to configure the 10-bit outputs from the 6-bit `opcode` field. <!--SR:!2025-12-30,161,442!2025-12-30,161,442-->
      - control unit / MIPS / implementation / don't cares ::@:: They help simplify the truth table. Compare setting a signal to 0 vs. 1 to see if it makes any behavioral difference. If not, use don't care. <p> _MemRead_ and _MemWrite_ almost always need to be asserted \(cannot be don't care\), otherwise bad memory addresses may be read from or written to. <!--SR:!2025-12-07,147,442!2026-01-02,163,439-->
    - control unit / MIPS / _Jmp_ ::@:: So far, we are missing the case for pseudo-address jumps. \(Actually also register jump `jr`, but the lecture slides do not cover it.\) Simply add extra control signals, datapath, and multiplexers! In this case, the _Jmp_ signal controls an additional multiplexer. <p> 0: PC behavior remains the same as before; 1: use the calculated address <!--SR:!2026-01-01,163,442!2025-12-26,157,442-->
- single-cycle processor
  - single-cycle processor / disadvantages ::@:: It cannot run very fast. The instruction with the greatest latency \(e.g. load word `lw`, excluding multi-cycle instructions\), known as the _critical_ path, determines the minimum clock period. We cannot vary the period for different instructions. It violates the design principle "fast common cases". <p> _Pipelining_ mitigates this. <!--SR:!2026-01-02,164,442!2025-12-11,151,442-->
- single-cycle processor

## week 11 lab

- datetime: 2025-04-15T15:00:00+08:00/2025-04-15T15:50:00+08:00, PT50M
- topic: MARS debugging
- MARS
  - MARS / debugging ::@:: breakpoint, registers, step, undo <!--SR:!2025-12-20,151,442!2025-12-12,152,442-->
    - MARS / debugging / breakpoint ::@:: You can set breakpoints. The program will pause whenever execution reaches a breakpoint. Then you can perform other debugging actions. <!--SR:!2025-12-16,147,439!2026-01-02,164,442-->
    - MARS / debugging / step ::@:: You can execute exactly one instruction and then pause. <!--SR:!2025-12-11,151,442!2026-01-02,164,441-->
    - MARS / debugging / undo ::@:: You can undo one instruction and then pause each time you click the button. However, system calls generally cannot be undone. <!--SR:!2025-12-25,161,442!2025-12-08,148,441-->
    - MARS / debugging / register ::@:: When the program is paused, you can view and modify register values. <!--SR:!2025-12-16,147,442!2025-12-11,151,442-->

## week 11 tutorial

- datetime: 2025-04-15T18:00:00+08:00/2025-04-15T18:50:00+08:00, PT50M
- topic: nested procedures, arithmetic logic unit
- MIPS architecture
  - [MIPS](MIPS.md)
    - [§ procedures](MIPS.md#procedures): procedures, nested procedures
    - [§ jump instructions](MIPS.md#jump%20instructions): `jal`, `jr`
- adder
  - adder / ripple-carry adder
- method of complements
- arithmetic logic unit
  - arithmetic logic unit / signals

## week 11 lecture 2

- datetime: 2025-04-18T09:00:00+08:00/2025-04-18T10:20:00+08:00, PT1H20M
- status: unscheduled, public holiday: Good Friday

## week 12 lecture

- datetime: 2025-04-21T13:30:00+08:00/2025-04-21T14:50:00+08:00, PT1H20M
- status: unscheduled, public holiday: Easter Monday

## week 12 lab

- datetime: 2025-04-22T15:00:00+08:00/2025-04-22T15:50:00+08:00, PT50M
- topic: building a 4-bit arithmetic logic unit with Logisim
- arithmetic logic unit
  - arithmetic logic unit / signals
- Logisim
  - Logisim / arithmetic logic unit ::@:: Essentially follow the lecture slides. Reuse circuits by saving them and using them as libraries. <!--SR:!2025-12-26,157,442!2026-01-01,163,442-->

## week 12 tutorial

- datetime: 2025-04-22T18:00:00+08:00/2025-04-22T18:50:00+08:00, PT50M
- topic: computer arithmetic
- binary multiplier
  - binary multiplier / binary long multiplication
    - binary multiplier / binary long multiplication / implementation, naive
    - binary multiplier / binary long multiplication / implementation, improved
    - binary multiplier / binary long multiplication / implementation
  - binary multiplier / signed
- binary divider
  - binary divider / binary long division
    - binary divider / binary long division / implementation, naive
    - binary divider / binary long division / implementation
  - binary divider / signed
- [Booth's multiplication algorithm](../../../../general/Booth's%20multiplication%20algorithm.md) ::@:: \(__this course__: optional\) <p> \(_this_\) is a multiplication algorithm that multiplies two signed binary numbers in two's complement notation. The algorithm was invented by Andrew Donald Booth in 1950. <!--SR:!2025-12-30,161,442!2026-01-02,164,442-->
  - Booth's multiplication algorithm / idea ::@:: \(__this course__: optional\) <p> Express the multiplier in binary. Each consecutive group of 1s can be expressed as one addition and one subtraction. This reduces the number of operations. <p> For example, we rewrite the multiplier as 01111110<sub>\(2\)</sub>=10000000<sub>\(2\)</sub>-00000010<sub>\(2\)</sub>. Then we only need an addition and a subtraction instead of 6 additions. <!--SR:!2026-01-02,164,442!2025-10-14,90,421-->
  - Booth's multiplication algorithm / implementation ::@:: \(__this course__: optional\) <p> Booth's algorithm can be implemented by repeatedly adding \(with ordinary unsigned binary addition\) one of two predetermined values _A_ and _S_ to a product _P_, then performing a rightward [arithmetic shift](../../../../general/arithmetic%20shift.md) on _P_. Let __m__ and __r__ be the [multiplicand](../../../../general/multiplicand.md) and [multiplier](../../../../general/multiplication.md#terminology), respectively; and let _x_ and _y_ represent the number of bits in __m__ and __r__. <!--SR:!2025-12-15,146,442!2025-12-23,160,442-->
    - Booth's multiplication algorithm / implementation / setup ::@:: \(__this course__: optional\) <p> 1. Determine the values of _A_ and _S_, and the initial value of _P_. All of these numbers should have a length equal to \(_x_ + _y_ + 1\). <br/> &emsp; 1. A: Fill the most significant \(leftmost\) bits with the value of __m__. Fill the remaining \(_y_ + 1\) bits with zeros. <br/> &emsp; 2. S: Fill the most significant bits with the value of \(−<!-- markdown separator -->__m__\) in two's complement notation. Fill the remaining \(_y_ + 1\) bits with zeros. <br/> &emsp; 3. P: Fill the most significant _x_ bits with zeros. To the right of this, append the value of __r__. Fill the least significant \(rightmost\) bit with a zero. <!--SR:!2025-12-18,158,442!2026-08-23,330,402-->
    - Booth's multiplication algorithm / implementation / loop ::@:: \(__this course__: optional\) <p> 2. Determine the two least significant \(rightmost\) bits of _P_. <br/> &emsp; 1. If they are 01, find the value of _P_ + _A_. Ignore any overflow. <br/> &emsp; 2. If they are 10, find the value of _P_ + _S_. Ignore any overflow. <br/> &emsp; 3. If they are 00, do nothing. Use _P_ directly in the next step. <br/> &emsp; 4. If they are 11, do nothing. Use _P_ directly in the next step. <br/> 3. [Arithmetically shift](../../../../general/arithmetic%20shift.md) the value obtained in the 2nd step by a single place to the right. Let _P_ now equal this new value. <br/> 4. Repeat steps 2 and 3 until they have been done _y_ times. <br/> 5. Drop the least significant \(rightmost\) bit from _P_. This is the product of __m__ and __r__. <!--SR:!2025-12-23,160,442!2025-12-24,155,442-->
    - Booth's multiplication algorithm / implementation / overflow ::@:: \(__this course__: optional\) <p> Overflow is ignored. This is because for each group of 1s, subtraction is performed before addition. And multiplication of two _signed_ integers cannot overflow _x_ + _y_ bits. So overflow is impossible. <!--SR:!2025-12-24,155,439!2026-01-03,164,442-->
  - Booth's multiplication algorithm / signedness ::@:: \(__this course__: optional\) <p> Note that this algorithm is for multiplying _signed_ integers, not _unsigned_ ones. _Unsigned_ multiplication can overflow _x_ + _y_ bits \(but not _x_ + _y_ + 1 bits\). <!--SR:!2025-12-26,157,442!2025-12-21,157,439-->

## week 12 extra tutorial

- datetime: 2025-04-22T20:30:00+08:00/2025-04-22T21:20:00+08:00, PT50M
- topic: programming assignment

> Dear all,
>
> You may have noticed that the PA has been released, and the deadline is <br/>
> May 11. \[redacted\], the designer of the PA, will kindly conduct a PA <br/>
> Intro and Q&A session tomorrow \(Tuesday\) evening at 8:30 PM via Zoom.
>
> Canvas Zoom link: \[redacted\]
>
> You are welcome to join in real time. We will also record the session and release the video afterwards.
>
> Best regards, <br/>
> \[redacted\] and \[redacted\] <br/>
> COMP2611 Instructors

## week 12 lecture 2

- datetime: 2025-04-25T09:00:00+08:00/2025-04-25T10:20:00+08:00, PT1H20M
- topic: pipeline basics
- [instruction pipelining](../../../../general/instruction%20pipelining.md) ::@:: It is a technique for implementing instruction-level parallelism within a single processor. Pipelining attempts to keep every part of the processor busy with some instruction by dividing incoming instructions into a series of sequential steps \(the eponymous "pipeline"\) performed by different processor units with different parts of instructions processed in parallel. <!--SR:!2025-12-14,145,439!2025-10-23,102,419-->
  - instruction pipelining ::@:: The steps should be independent of each other. It does not help with the latency \(execution time\) of a single instruction, but it increases instruction throughput \(number of instructions per time\). <p> The maximum potential speedup factor equals the number of stages. This requires the stages takes the same time, otherwise the factor decreases. <!--SR:!2025-10-16,101,422!2025-12-26,157,439-->
- [Gantt chart](../../../../general/Gantt%20chart.md) ::@:: It is a bar chart that illustrates a project schedule. It can show the sequence, duration, and dependence of activities. <!--SR:!2025-12-15,155,442!2026-01-01,163,442-->
- MIPS architecture
  - MIPS architecture / pipeline ::@:: It is designed for pipelining. Its instructions have the same size. Its instruction formats are few and similar. It supports memory operands in loads and stores only. It requires memory operands to be aligned, so memory access at most requires a single transfer. <!--SR:!2025-11-06,116,419!2026-01-02,164,442-->
- classical RISC pipeline
  - classical RISC pipeline / instruction fetch
  - classical RISC pipeline / instruction decode
  - classical RISC pipeline / execute
  - classical RISC pipeline / memory access
  - classical RISC pipeline / register write back
    - classical RISC pipeline / register write back / hazard
  - classical RISC pipeline / diagram ::@:: The stage-by-stage architecture of a MIPS microprocessor with a pipeline. Although the memory is shown twice for clarity of the pipeline, MIPS architectures have only one memory bank \(i.e. von Neumann architecture\). <p> ![The stage-by-stage architecture of a MIPS microprocessor with a pipeline. Although the memory is shown twice for clarity of the pipeline, MIPS architectures have only one memory bank \(i.e. von Neumann architecture\).](../../../../archives/Wikimedia%20Commons/MIPS%20Architecture%20(Pipelined).svg) <p> \(__this course__: Note some components are different from taught in this course. In particular, the output of the adder after PC _additionally_ updates PC directly after one cycle, rather than going through the pipeline variables as in this diagram. There are two separate ALUs, one for arithmetic and the other for branching, as opposed to only one ALU in this diagram. Control signals are missing from this diagram.\) <!--SR:!2026-08-05,310,402!2025-12-25,161,439-->
- instruction pipelining
  - instruction pipelining / pipeline registers ::@:: In between each stage \(so 4 components for the classical RISC pipeline\), there is a component storing information from the previous stage produced in the previous cycle. Their names are "\(before stage\)/\(after stage\)", e.g. "EX/MEM". <!--SR:!2025-12-31,162,442!2025-12-20,155,442-->
- classical RISC pipeline
  - classical RISC pipeline / instruction decode
    - classical RISC pipeline / instruction decode / register write back ::@:: In a pipelined CPU, the destination register input and the _RegWrite_ signal is forwarded from the MEM/WB pipeline register instead of from the current instruction executing in the ID stage. <p> Further, the register writing for the current instruction executing in the WB stage is performed in the first half of the current cycle, and the register reading for the current instruction executing in the ID stage is performed in the second half of the current cycle. This also implies the execution time of the ID stage and WB stage should add up to one cycle at most. <!--SR:!2025-11-07,108,421!2025-12-16,147,441-->
  - classical RISC pipeline / note ::@:: \(__this course__: The IF stage contains the adder and the instruction memory. The ID stage stops right after the outputs of control unit, register file, sign-extension component, and the lower instruction bits. The EXE stage contains components not covered by other stages in this description, thus in particular including arithmetic ALU, branching ALU and its shift-left-by-2-bits component, and _RegDst_ multiplexer. The MEM stage contains the AND gate for _PCSrc_ and data memory. The WB stage contains the _MemToReg_ multiplexer.\) <!--SR:!2025-11-03,113,422!2025-11-17,118,422-->
  - classical RISC pipeline / diagrams ::@:: single-clock-cycle pipeline diagram, multi-clock-cycle pipeline diagram <!--SR:!2026-01-03,164,442!2025-12-18,149,442-->
    - classical RISC pipeline / diagrams / single-clock-cycle ::@:: It shows the current state of all stages in the same cycle. <!--SR:!2025-12-30,161,442!2026-01-03,164,442-->
    - classical RISC pipeline / diagrams / multi-clock-cycle ::@:: Literally just an Gantt chart. <!--SR:!2025-12-30,161,442!2025-12-21,157,439-->

## week 12 extra tutorial 2

- datetime: 2025-04-25T20:30:00+08:00/2025-04-25T21:20:00+08:00, PT50M
- topic: homework 2

> Dear COMP2611 students,
>
> It's toward the end of semester and our PGTAs will offer optional Zoom <br/>
> tutorials on HW2 and HW3 to help you review the related topics. You can <br/>
> also ask any questions related afterwards.
>
> HW3 tutorial: Fri \(Apr 25\) 8:30pm by \[redacted\]
> \[redacted\]
>
> HW2 tutorial: coming Mon \(Apr 28\) 8:30pm by \[redacted\]
> \[redacted\]
>
> You can also find the Zoom links under COMP2611 Canvas.
>
> Best regards, <br/>
> \[redacted\] and \[redacted\]

## week 13 lecture

- datetime: 2025-04-28T13:30:00+08:00/2025-04-28T14:50:00+08:00, PT1H20M
- topic: pipeline control, pipeline hazards
- classical RISC pipeline
  - classical RISC pipeline / control ::@:: How to pipeline control signals? Just pass the control signals along the pipeline the same way you pass the corresponding data along the datapath. When a control signal is used in a stage and will not be further used, you do not need to pass it further. <p> Extra: The PC+4 value is also passed along the stages \(note the PC+4 in a stage uses the PC of the currently executing instruction in that stage\), and is written to the PC register at the start of the MEM stage \(not WB stage!\). Later, when we talk about branching, we make this happen even earlier: the PC \(with branching considered\) is written during the first half of the EXE stage, which reduces bubbling. <p> Below shows what control signals are used in each stage. <!--SR:!2025-12-07,147,442!2025-10-14,101,422-->
    - classical RISC pipeline / control / instruction fetch ::@:: control signals used: \(none\) <p> The PC+4 value and the _PCSrc_ signal is received from the MEM stage at the start of the cycle. <!--SR:!2025-11-08,114,422!2025-12-31,162,442-->
    - classical RISC pipeline / control / instruction decode ::@:: control signals used: \(none\) <p> The _RegWrite_ signal is received from the WB stage. <!--SR:!2025-12-31,162,442!2025-12-17,157,442-->
    - classical RISC pipeline / control / execute ::@:: control signals used: _ALUOp_, _ALUSrc_, _RegDest_ <!--SR:!2025-12-29,160,442!2025-12-27,158,442-->
    - classical RISC pipeline / control / memory access ::@:: control signals used: _MemRead_, _MemWrite_, _PCSrc_ \(_Branch_ AND _Zero_\) <!--SR:!2025-12-14,154,439!2025-12-31,162,442-->
    - classical RISC pipeline / control / register write back ::@:: control signals used: _MemToReg_, _RegWrite_ <!--SR:!2025-12-27,164,442!2025-12-19,150,442-->
- [hazard](../../../../general/hazard%20(computer%20architecture).md) ::@:: They are are problems with the instruction pipeline in CPU microarchitectures when the next instruction cannot execute in the following clock cycle, and can potentially lead to incorrect computation results. <!--SR:!2025-11-07,114,419!2025-12-30,161,442-->
  - hazard / causes ::@:: data dependency, control dependency <!--SR:!2025-11-05,112,422!2025-12-28,159,442-->
    - hazard / causes / data dependency ::@:: read after write: An instruction writes to a register. A very close next instruction reads from the same register. <!--SR:!2025-12-21,158,442!2025-12-13,153,442-->
    - hazard / causes / control dependency ::@:: The next instruction address is unavailable due to an ongoing branch or jump. <!--SR:!2025-12-09,149,442!2025-12-16,147,442-->
  - hazard / types ::@:: Three common types of hazards are data hazards, structural hazards, and control hazards \(branching hazards\). <!--SR:!2025-12-31,162,439!2025-12-27,158,442-->
    - hazard / types / data ::@:: Hazards caused by data dependencies. <!--SR:!2025-12-29,160,439!2025-12-15,146,442-->
    - hazard / types / structural ::@:: A required hardware is busy. <!--SR:!2025-12-19,150,442!2025-12-29,160,442-->
    - hazard / types / control ::@:: Hazards caused by control dependencies. <!--SR:!2025-12-26,157,442!2025-12-27,158,442-->
  - hazard / bubbling ::@:: It can always resolve hazards. In the extreme case of always waiting, it degenerates the pipeline into working like a single-cycle processor \(but each instruction takes 5 shorter cycles\). <!--SR:!2025-12-13,153,439!2025-12-16,152,442-->
    - hazard / bubbling / note ::@:: \(__this course__: Ignore below. Also, if a question asks you to add bubbles \(BUB\), by default only add them before the IF stage of the instruction being bubbled. Do not put bubbles after the ID stage or propagate bubbles to other instructions.\) <p> Strictly speaking, we can only bubble after instruction decode \(ID\), the second step, is done, otherwise we do not know that the instruction requires bubbling. That means the bubble starts after ID. <!--SR:!2025-11-13,114,422!2025-12-13,153,439-->
  - hazard / structural hazards ::@:: A structural hazard occurs when two \(or more\) instructions that are already in pipeline need the same resource. The result is that instruction must be executed in series rather than parallel for a portion of pipeline. Structural hazards are sometimes referred to as resource hazards. <p> Example: A situation in which multiple instructions are ready to enter the execute instruction phase and there is a single ALU \(Arithmetic Logic Unit\). One solution to such resource hazard is to increase available resources, such as having multiple ports into main memory and multiple ALU \(Arithmetic Logic Unit\) units. <!--SR:!2025-12-30,161,442!2025-12-17,148,442-->
    - hazard / structural hazards / memory ::@:: Instructions and data are in the same main memory. If the same memory is used in the IF and MEM stage, these two stages cannot run at the same time. <p> A solution is to use separate memories, or have separate caches: instruction cache and data cache. <!--SR:!2025-12-18,158,442!2025-10-23,108,422-->
    - hazard / structural hazards / registers ::@:: Both ID and WB stage uses the register file. <p> The solution is that the WB stage runs in the first half of a cycle and ID stage runs in the second half of a cycle. This is possible because register access is very fast. This also means writing to and then reading from the same register in a cycle is well-defined. <!--SR:!2025-12-12,152,442!2025-12-19,150,442-->
  - hazard / data hazards ::@:: A piece of data is computed but not yet stored to the register file or the main memory. A currently executing instruction requires this piece of data, but reading from the register file or the main memory would yield the old value. Waiting definitely can solve this, but there are other solutions: operand forwarding, out-of-order execution, etc. <p> In the classical RISC pipeline: Assuming no mitigations, a _register_ read after write requires two bubbles so that the WB stage \(first half of the cycle\) aligns with the ID stage \(second half of the cycle\). <!--SR:!2025-12-20,151,441!2025-12-17,157,442-->
    - hazard / data hazard / operand forwarding ::@:: A piece of data is computed but not yet stored to the register file or the main memory. We add extra datapaths to the CPU so that it can be forwarded to any stage in the next cycle. Extra control signals and multiplexers are added so that the new value forwarded instead of the old value read is used in the next cycle. <!--SR:!2025-12-12,152,442!2026-01-02,164,442-->
      - hazard / data hazard / operand forwarding / limitation ::@:: Note that the data can only be passed forward in time - the data cannot be bypassed back to an earlier stage if it has not been processed yet. <p> This means bubbles are still needed. However, operand forwarding may still help by reducing the number of bubbles required. <p> In the classical RISC pipeline: A _register_ read after write, but the data comes from the MEM stage, requires one bubble instead of two bubbles with forwarding. <!--SR:!2025-12-17,157,442!2025-12-23,159,442-->
    - hazard / data hazard / out-of-order execution ::@:: Reorder code so that dependant instructions are far enough away. Of course, you have to be careful that this does not change the program behavior. <p> The reordering could be done by a assembler, a compiler, or by the CPU hardware. <!--SR:!2025-12-14,145,439!2025-12-25,161,442-->
  - hazard / control hazards ::@:: The next instruction address is unavailable due to an ongoing branch or jump. <p> In the MIPS implementation as described so far above, the next instruction address is fed back into the PC counter at the start of the MEM stage, which requires two bubbles! This is way too slow! <!--SR:!2026-01-02,164,442!2025-12-22,153,441-->
    - hazard / control hazards / hardware ::@:: __important__: Two bubbles is too slow! So we add extra hardware and control signals, so that branches \(including the comparison results\) and jumps are computed in the ID stage. Then the next instruction address is available at the start of the EX stage, requiring one bubble only. __We assume this henceforth.__ <p> sidenote: Actually, the above is kinda wrong... Rather, the branch conditions are checked in the EX stage in the first half of a cycle. This is possible because the branch conditions are very simple. Then the result and the address are forwarded to the IF stage. The IF stage only runs in the second half of a cycle. <!-- <https://stackoverflow.com/a/58601958> --> <!--SR:!2025-12-10,150,442!2025-12-14,154,442-->
    - hazard / control hazards / schemes ::@:: Since we require one bubble, we can mitigate this bubble by inserting something to do in the bubble. What to insert there depends on the scheme used. Obviously, the program behavior needs to be preserved. <p> There are four schemes to solve this performance problem with branches: predict not taken, branch likely, branch delay slot, and branch prediction. <!--SR:!2026-01-01,163,439!2025-12-29,160,439-->
      - hazard / control hazards / schemes / predict not taken ::@:: Always fetch the instruction after the branch from the instruction cache, but only execute it if the branch is not taken. If the branch is not taken, the pipeline stays full. If the branch is taken, the instruction is flushed \(marked as if it were a NOP\), and one cycle's opportunity to finish an instruction is lost. <!--SR:!2025-12-21,152,439!2025-12-31,162,442-->
      - hazard / control hazards / schemes / branch likely ::@:: Always fetch the instruction after the branch from the instruction cache, but only execute it if the branch was taken. The compiler can always fill the branch delay slot on such a branch, and since branches are more often taken than not, such branches have a smaller IPC penalty than the previous kind. <!--SR:!2025-12-13,153,439!2025-12-24,155,442-->
      - hazard / control hazards / schemes / branch delay slot ::@:: Depending on the design of the delayed branch and the branch conditions, it is determined whether the instruction immediately following the branch instruction is executed even if the branch is taken. Instead of taking an IPC penalty for some fraction of branches either taken \(perhaps 60%\) or not taken \(perhaps 40%\), branch delay slots take an IPC penalty for those branches into which the compiler could not schedule the branch delay slot. The SPARC, MIPS, and MC88K designers designed a branch delay slot into their ISAs. <!--SR:!2025-12-17,157,442!2025-12-22,159,439-->
      - hazard / control hazards / schemes / branch prediction ::@:: In parallel with fetching each instruction, guess if the instruction is a branch or jump, and if so, guess the target. On the cycle after a branch or jump, fetch the instruction at the guessed target. When the guess is wrong, flush the incorrectly fetched target. <!--SR:!2025-12-16,156,442!2025-12-07,147,441-->

## week 13 extra tutorial

- datetime: 2025-04-28T20:30:00+08:00/2025-04-28T21:20:00+08:00, PT50M
- topic: homework 3

> Dear COMP2611 students,
>
> It's toward the end of semester and our PGTAs will offer optional Zoom <br/>
> tutorials on HW2 and HW3 to help you review the related topics. You can <br/>
> also ask any questions related afterwards.
>
> HW3 tutorial: Fri \(Apr 25\) 8:30pm by \[redacted\]
> \[redacted\]
>
> HW2 tutorial: coming Mon \(Apr 28\) 8:30pm by \[redacted\]
> \[redacted\]
>
> You can also find the Zoom links under COMP2611 Canvas.
>
> Best regards, <br/>
> \[redacted\] and \[redacted\]

## week 13 lab

- datetime: 2025-04-29T15:00:00+08:00/2025-04-29T15:50:00+08:00, PT50M
- topic: building a computer with Logisim
- single-cycle processor
- classical RISC pipeline
  - classical RISC pipeline / diagram
- datapath
- Logisim
  - Logisim / computer ::@:: Essentially simply follow the lecture slides. Use the RAM component in Logisim to store data and instructions. Reuse circuits by saving them and using them as libraries. <!--SR:!2025-12-30,161,442!2025-12-14,150,442-->

## week 13 tutorial

- datetime: 2025-04-29T18:00:00+08:00/2025-04-29T18:50:00+08:00, PT50M
- topic: single-cycle datapath, single-cycle control
- datapath
- classic RISC pipeline
  - classic RISC pipeline / instruction fetch
  - classic RISC pipeline / instruction decode
  - classic RISC pipeline / execute
  - classic RISC pipeline / memory access
  - classic RISC pipeline / register write back
- control unit

## week 13 lecture 2

- datetime: 2025-05-02T09:00:00+08:00/2025-05-02T10:20:00+08:00, PT1H20M
- topic: memory system, locality, hierarchy, performance
- [memory hierarchy](../../../../general/memory%20hierarchy.md) ::@:: It separates computer storage into a hierarchy based on response time. Since response time, complexity, and capacity are related, the levels may also be distinguished by their performance and controlling technologies. <!--SR:!2025-12-24,155,442!2025-12-11,151,442-->
  - memory hierarchy / diagram ::@:: Diagram showing the memory hierarchy of a modern computer architecture. <p> ![Diagram showing the memory hierarchy of a modern computer architecture](../../../../archives/Wikimedia%20Commons/ComputerMemoryHierarchy.svg) <!--SR:!2025-12-15,155,442!2025-10-14,101,422-->
  - memory hierarchy / example ::@:: The list below is sorted in ascending "distance" from the CPU, i.e. time to access data. In general, with increasing "distance", access becomes rarer and capacity becomes higher. <p> - primary storage: registers &lt; cache memory &lt; main memory \(via memory bus\) <br/> - secondary storage: mass storage device \(hard disk\) <br/> - offline storage: removable media \(read by removable media drive\), e.g. CD, DVD <br/> - tertiary storage: even more removable media, but very hard to access \(e.g. via a robotic access system\) <!--SR:!2025-12-22,153,439!2025-11-17,123,421-->
- [computer memory](../../../../general/computer%20memory.md) ::@:: It stores information, such as data and programs, for immediate use in the computer. The term _memory_ is often synonymous with the terms _RAM_, _main memory_, or _primary storage_. <!--SR:!2026-01-02,164,442!2025-12-30,161,442-->
  - computer memory / characteristics ::@:: It is fast. Ideally it should also be cost-efficient \(cost per capacity\) and/or large, but it is hard to achieve. <!--SR:!2025-12-13,153,439!2026-01-03,164,442-->
- [computer data storage](../../../../general/computer%20data%20storage.md) ::@:: It is a technology consisting of computer components and recording media that are used to retain digital data. It is a core function and fundamental component of computers. <!--SR:!2025-12-10,150,442!2025-12-26,157,442-->
  - computer data storage / characteristics ::@:: It is cost-efficient \(cost per capacity\) and large. Ideally it should also be fast, but it is hard to achieve. <!--SR:!2025-12-05,145,439!2025-12-28,159,439-->
  - computer data storage / typical access time ::@:: 5–20&nbsp;ms <!--SR:!2025-12-20,151,439!2025-12-06,146,439-->
  - computer data storage / typical cost ::@:: \$0.2–2 per GB <!--SR:!2025-12-14,154,439!2025-12-30,161,442-->
- [dynamic random-access memory](../../../../general/dynamic%20random-access%20memory.md) \(DRAM\) ::@:: It is a type of random-access semiconductor memory that stores each bit of data in a memory cell, usually consisting of a tiny capacitor and a transistor, both typically based on metal–oxide–semiconductor \(MOS\) technology. <p> Usually used as the main memory in a computer. <!--SR:!2025-12-21,157,439!2025-12-28,159,439-->
  - dynamic random-access memory / typical access time ::@:: 50–70&nbsp;ns <!--SR:!2026-01-01,163,442!2025-12-21,152,442-->
  - dynamic random-access memory / typical cost ::@:: \$20–75 per GB <!--SR:!2025-12-30,161,441!2026-01-02,164,442-->
  - dynamic random-access memory / diagram ::@:: DRAM ece385 illustrative example, illustrating how DRAM \(dynamic random access memory\) works, with simple 4 by 4 array. <p> ![DRAM ece385 illustrative example, illustrating how DRAM \(dynamic random access memory\) works, with simple 4 by 4 array.](../../../../archives/Wikimedia%20Commons/Square%20array%20of%20mosfet%20cells%20read.svg) <!--SR:!2025-12-28,159,442!2025-12-17,148,442-->
  - dynamic random-access memory / mechanism ::@:: Oversimplified. Each bit consists of a transistor and a capacitor. The transistor controls read/write. The capacitor stores a bit, with 1 being charged. <!--SR:!2025-12-27,158,441!2025-12-22,153,439-->
  - dynamic random-access memory / advantages ::@:: They are structurally simple \(only a transistor and a capacitor\). They are high density and low cost. <!--SR:!2025-12-31,162,441!2026-01-01,163,442-->
  - dynamic random-access memory / disadvantages ::@:: Real capacitors leak electrons. Reading also discharges electrons \(i.e. reading is destructive\). So the capacitors need to be refreshed periodically and after read to avoid the information fading away. Hence "dynamic" in the name. <!--SR:!2025-12-18,158,442!2025-12-25,156,442-->
- [static random-access memory](../../../../general/static%20random-access%20memory.md) \(SRAM\) ::@:: It is a type of random-access memory \(RAM\) that uses latching circuitry \(flip-flop\) to store each bit. SRAM is volatile memory; data is lost when power is removed. <p> Usually used as CPU caches in a computer. <!--SR:!2025-12-20,151,439!2025-12-19,150,442-->
  - static random-access memory / typical access time ::@:: 0.5–2.5&nbsp;ns <!--SR:!2026-01-01,163,442!2025-12-30,161,442-->
  - static random-access memory / typical cost ::@:: \$2000–5000 per GB <!--SR:!2025-12-30,161,441!2025-12-19,154,439-->
  - static random-access memory / diagram ::@:: Circuit diagram of an SRAM cell, built with six MOSFETs. The bulk connection of all transistors is to ground, but is not shown from simplicity. <p> ![Circuit diagram of an SRAM cell, built with six MOSFETs. The bulk connection of all transistors is to ground, but is not shown from simplicity.](../../../../archives/Wikimedia%20Commons/SRAM%20Cell%20(6%20Transistors).svg) <!--SR:!2027-01-26,473,419!2025-12-25,156,442-->
  - static random-access memory / mechanism ::@:: Oversimplified. Each cell consists of transistors only \(e.g 6 transistors in a CMOS SRAM cell\). <!--SR:!2025-12-24,161,442!2025-12-30,161,442-->
  - static random-access memory / advantages ::@:: The cells do not need to be refreshed periodically, only power is required. Reading is not destructive. Hence "static" in the name. <!--SR:!2025-12-31,162,442!2026-01-03,164,442-->
  - static random-access memory / disadvantages ::@:: They are medium density and very high cost. <!--SR:!2025-12-18,149,441!2025-12-14,145,439-->
- classical RISC pipeline
  - classical RISC pipeline / memory access ::@:: __important__: We have been assuming memory access takes almost one CPU clock cycle. But in reality, we see the typical access time is much _higher_ than that. _Let's drop the aforementioned assumption henceforth._ <!--SR:!2025-12-12,152,442!2025-12-12,152,442-->
- [hard disk drive](../../../../general/hard%20disk%20drive.md) \(HDD\) ::@:: It is an electro-mechanical data storage device that stores and retrieves digital data using magnetic storage with one or more rigid rapidly rotating platters coated with magnetic material. The platters are paired with magnetic heads, usually arranged on a moving actuator arm, which read and write data to the platter surfaces. <!--SR:!2025-12-27,158,441!2025-12-28,164,441-->
  - hard disk drive / sector ::@:: A HDD consists of many __disk sectors__. Each is associated with a unique ID, has fixed capacity \(usually 512 bytes, 4096 bytes is increasingly common\). It may support error correction codes \(ECC\) to correct errors invisibly. It has synchronization fields and gaps for synchronization \(no idea what this means\). <!--SR:!2025-12-17,148,442!2025-12-13,153,442-->
  - hard disk drive / read ::@:: To calculate average read time, you need to understand how a HDD reads data. <p> First, the head assembly seeks the disk track containing the disk sector to be read. Then it needs to rotate to the disk sector. On average, it needs to rotate half a circle. Then it needs to transfer the data. All data in the disk sector is transferred. Finally, there is a controller overhead. <!--SR:!2025-12-29,160,439!2026-01-02,163,439-->
    - hard disk drive / read / calculation ::@:: average read time = average seek time \(given\) + rotational latency + transfer time + controller delay \(given\) <br/> rotational latency = 0.5 / \(rpm / 60\) <br/> transfer time = disk sector capacity / transfer rate <!--SR:!2026-01-02,164,442!2025-12-29,160,442-->
- [solid-state drive](../../../../general/solid-state%20drive.md) \(SSD\) ::@:: It is a type of solid-state storage device that uses integrated circuits to store data persistently. <!--SR:!2025-12-31,162,442!2026-01-03,164,442-->
  - solid-state drive / vs. hard disk drive ::@:: It could be 100–1000 times faster than HDDs. It is smaller, takes less power, and more robust. Less cost-efficient \(cost per capacity\). <p> Various densities and capacities are achieved by stacking chips in a grid. <!--SR:!2025-12-31,162,442!2025-12-30,161,442-->
- von Neumann architecture
  - von Neumann architecture / von Neumann bottleneck ::@:: The use of the same bus to fetch instructions and data leads to the von Neumann bottleneck, the limited throughput \(data transfer rate\) between the central processing unit \(CPU\) and memory compared to the amount of memory. This seriously limits the effective processing speed when the CPU is required to perform minimal processing on large amounts of data. The CPU is continually forced to wait for needed data to move to or from memory. <!--SR:!2025-12-14,145,439!2025-12-12,152,442-->
    - von Neumann architecture / von Neumann bottleneck / trend ::@:: Since CPU speed and memory size have increased much faster than the throughput between them, the bottleneck has become more of a problem, a problem whose severity increases with every new generation of CPU. <!--SR:!2025-12-28,159,442!2026-01-03,164,442-->
    - von Neumann architecture / von Neumann bottleneck / mitigations ::@:: Exploiting locality of reference can help mitigate this. <!--SR:!2025-12-14,145,439!2025-11-06,107,422-->
- [locality of reference](../../../../general/locaity%20of%20reference.md) ::@:: It is the tendency of a processor to access the same set of memory locations repetitively over a short period of time. <!--SR:!2025-12-23,160,441!2025-12-20,151,439-->
  - locality of reference / types ::@:: There are two basic types of reference locality – temporal and spatial locality. Temporal locality refers to the reuse of specific data and/or resources within a relatively small time duration. Spatial locality \(also termed _data locality_\) refers to the use of data elements within relatively close storage locations. <!--SR:!2025-12-27,158,439!2025-12-28,159,442-->
- [cache](../../../../general/cache%20(computing).md) ::@:: It is a hardware or software component that stores data so that future requests for that data can be served faster; the data stored in a cache might be the result of an earlier computation or a copy of data stored elsewhere. A __cache hit__ occurs when the requested data can be found in a cache, while a __cache miss__ occurs when it cannot. <!--SR:!2026-01-02,163,439!2025-12-11,151,442-->
  - cache / cache hit ::@:: When the cache client \(a CPU, web browser, operating system\) needs to access data presumed to exist in the backing store, it first checks the cache. If an entry can be found with a tag matching that of the desired data, the data in the entry is used instead. This situation is known as a __cache hit__. The percentage of accesses that result in cache hits is known as the __hit rate__ or __hit ratio__ of the cache. <!--SR:!2025-11-16,117,422!2025-12-29,160,439-->
  - cache / cache miss ::@:: The alternative situation, when the cache is checked and found not to contain any entry with the desired tag, is known as a __cache miss__. This requires a more expensive access of data from the backing store. Once the requested data is retrieved, it is typically copied into the cache, ready for the next access. <p> The percentage of access that result in cache misses is known as the __miss rate__ of the cache, which equals 1 subtracted by the hit rate. <!--SR:!2025-12-15,146,439!2025-12-25,162,442-->
  - cache / measures ::@:: hit rate, miss rate: described above <br/> hit time: time to determine miss or hit and then access the cache <br/> miss penalty: average time to read the backing store <!--SR:!2025-12-08,148,442!2025-12-14,145,439-->
- [cache hierarchy](../../../../general/cache%20hierarchy.md) ::@:: It is a memory architecture that uses a hierarchy of memory stores based on varying access speeds to cache data. Highly requested data is cached in high-speed access memory stores, allowing swifter access by central processing unit \(CPU\) cores. <!--SR:!2025-12-14,145,439!2025-12-15,155,442-->
  - cache hierarchy / average access time \(AAT\) ::@:: average memory latency = hit time + miss rate \* miss penalty <br/> For multilevel caches, the miss penalty of a cache level equals the average memory latency of the next cache level. So you can chain this equation. <!--SR:!2025-12-28,164,442!2025-12-17,148,441-->
  - cache hierarchy / tradeoffs ::@:: In general, more levels make the average memory latency approach the ideal case \(always cache hit in the first level\), with diminishing returns. It also makes the hardware more complicated and expensive. <!--SR:!2025-12-26,157,441!2025-12-25,162,442-->

## week 14 lecture

- datetime: 2025-05-05T13:30:00+08:00/2025-05-05T14:50:00+08:00, PT1H20M
- topic: direct mapped cache, block placement, block identification
- cache
  - cache / structure ::@:: A cache is made up of a pool of entries. Each entry has associated data, which is a copy of the same data in some _backing store_. Each entry also has a _tag_, which specifies the identity of the data in the backing store of which the entry is a copy. <p> Common used entry sizes \(today\) include 32 bytes and 64 bytes. <!--SR:!2026-01-01,163,442!2025-12-17,148,442-->
- [cache placement policies](../../../../general/cache%20placement%20policies.md) ::@:: They are policies that determine where a particular memory block can be placed when it goes into a CPU cache. A block of memory cannot necessarily be placed at an arbitrary location in the cache; it may be restricted to a particular cache line or a set of cache lines by the cache's placement policy. <!--SR:!2025-12-26,157,441!2026-01-01,163,442-->
  - cache placement policies / types ::@:: There are three different policies available for placement of a memory block in the cache: direct-mapped, fully associative, and set-associative. Originally this space of cache organizations was described using the term "congruence mapping". <!--SR:!2025-11-08,118,422!2025-12-31,162,441-->
  - cache placement policies / identification ::@:: A cache entry has a _tag_, which specifies the identity of the data in the backing store of which the entry is a copy. Sometimes, the cache entry has no valid data yet. Either a special tag value is used to denote this \(e.g. a tag value of all 0s\), or an additional _valid_ bit is used to denote this. \(__this course__: Use the valid bit.\) <!--SR:!2025-12-05,145,439!2025-12-27,163,441-->
  - cache placement policies / direct-mapped cache ::@:: In a direct-mapped cache structure, the cache is organized into multiple sets with a single cache line per set. Based on the address of the memory block, it can only occupy a single cache line. The cache can be framed as a _n_&nbsp;×&nbsp;1 column matrix. <p> many-to-one mapping <!--SR:!2025-12-15,155,442!2026-01-02,164,441-->
    - cache placement policies / direct-mapped cache / mapping ::@:: Theoretically, it could be any function taking the address of a memory block and outputting a valid address of a cache block. <p> In practice, it is simply the the address of the memory block the address resides in \(i.e. dropping the byte offset bits and keeping the tag bits and the index bits only\), then modulo it by the number of cache blocks. \(__this course__: Use the mapping in practice.\) <!--SR:!2025-12-30,161,442!2025-12-18,149,442-->
    - cache placement policies / direct-mapped cache / placement ::@:: - The set is determined by the index bits derived from the address of the memory block. <br/> - The memory block is placed in the set identified and the tag is stored in the tag field associated with the set. <br/> - If the cache line is previously occupied, then the new data replaces the memory block in the cache. <!--SR:!2025-11-09,119,422!2025-12-10,150,442-->
    - cache placement policies / direct-mapped cache / address subdivision ::@:: If the cache block size and the number of cache blocks are both powers of 2, then any memory address expressed in binary can be subdivided into 3 parts. <p> Assuming the cache block size is 2<sup>_n_</sup>&nbsp;bytes and the number of cache blocks is 2<sup>_m_</sup>. Then the lowest _n_ bits is the _byte offset_. The next lower _m_ bits is the _index_. The remaining highest bits are the _tag_. The memory _block address_ is the address without the byte offset. <!--SR:!2025-12-25,156,441!2025-12-18,149,442-->
    - cache placement policies / direct-mapped cache / tag ::@:: The tag field of a cache block stores the tag when the address is subdivided. The _index_ bits are not needed: they are the same as the cache block address. So the tag field bit width is the same as the tag bit width. <p> There may also be an extra _valid_ bit, denoting if the cache block has data. \(__this course__: Use the valid bit.\) <!--SR:!2025-12-30,161,442!2025-12-27,158,442-->
    - cache placement policies / direct-mapped cache / search ::@:: - The set is identified by the index bits of the address. <br> - The tag bits derived from the memory block address are compared with the tag bits associated with the set. \(__this course__: Since we use the valid bit, we also need to check if the valid bit is 1.\) If the tag matches, then there is a cache hit and the cache block is returned to the processor. Else there is a cache miss and the memory block is fetched from the lower memory \(main memory, disk\). <!--SR:!2025-12-14,145,439!2025-12-12,148,439-->
- cache
  - cache / size ::@:: Cache size are often quoted by their data capacity only. The _actual cache size_ is often slightly larger due to extra data required to track cache blocks. <p> Each cache block has the block data, the tag field, and sometimes the valid bit. To calculate the actual cache size _in bits_, find the number of cache blocks. Then find the _actual_ size _in bits_ of a cache block. Finally, multiply it by the number of cache blocks. \(__this course__: We use the valid bit. Also, sizes are expressed in units of powers of 2.\) <!--SR:!2025-11-16,117,422!2025-12-16,156,442-->
    - cache / size / tradeoff ::@:: Determining cache size requires balancing tradeoffs. Too small, then locality of reference is not exploited fully. Too large, then there are frequent cache misses due to frequent replacement of data from having less cache sets and/or cache lines. <!--SR:!2026-01-01,163,442!2025-12-16,147,442-->
  - cache / cache miss
    - cache / cache miss / CPU ::@:: On cache hit, CPU proceeds normally. On cache miss, the CPU pipeline stalls \(for many bubbles\) until the data is available. Meanwhile, the cache fetches from the backing store \(which could be another cache\). <p> CPU fetches two kinds of data: instruction and data. So usually it has two cache types: instruction cache and data cache. If instruction cache misses, the IF stage restarts. If data cache misses, the CPU waits for the data, which may require a complete data access \(fetch from the main memory\). <!--SR:!2025-12-23,154,439!2026-01-01,163,442-->
- cache placement policies
  - cache placement policies / direct-mapped cache
    - cache placement policies / direct-mapped cache / advantages ::@:: - This placement policy is power efficient as it avoids the search through all the cache lines. <br/> - The placement policy and the replacement policy is simple. <br/> - Simple and low-cost hardware can be used, as only one tag needs to be checked at a time. <!--SR:!2025-12-29,160,439!2025-12-29,160,439-->
    - cache placement policies / direct-mapped cache / disadvantages ::@:: It has lower cache hit rate, as there is only one cache line available in a set. Every time a new memory is referenced to the same set, the cache line is replaced, which causes conflict miss. <!--SR:!2025-12-12,152,442!2025-12-10,150,442-->
  - cache placement policies / fully associative cache ::@:: The cache is organized into a single cache set with multiple cache lines. A memory block can occupy any of the cache lines. The cache organization can be framed as 1&nbsp;×&nbsp;m row matrix. <!--SR:!2025-12-29,160,441!2025-12-20,151,439-->
    - cache placement policies / fully associative cache / advantages ::@:: - Fully associative cache structure provides us the flexibility of placing memory block in any of the cache lines and hence full utilization of the cache. <br/> - The placement policy provides better cache hit rate. <br/> - It offers the flexibility of utilizing a wide variety of replacement algorithms if a cache miss occurs. <!--SR:!2025-12-17,148,442!2025-12-21,152,439-->
    - cache placement policies / fully associative cache / disadvantages ::@:: - The placement policy is power hungry as the comparison circuitry has to run over the entire cache to locate a block. <br/> - The most expensive of all methods, due to the high cost of associative-comparison hardware. <!--SR:!2025-12-24,160,439!2025-12-23,154,439-->
    - cache placement policies / fully associative cache / placement ::@:: - The cache line is selected based on the valid bit associated with it. If the valid bit is 0, the new memory block can be placed in the cache line, else it has to be placed in another cache line with valid bit 0. <br/> - If the cache is completely occupied then a block is evicted and the memory block is placed in that cache line. <br/> - The eviction of memory block from the cache is decided by the replacement policy. <!--SR:!2025-12-10,150,442!2025-12-18,158,442-->
    - cache placement policies / fully associative cache / search ::@:: - The Tag field of the memory address is compared with tag bits associated with all the cache lines. If it matches, the block is present in the cache and is a cache hit. If it does not match, then it is a cache miss and has to be fetched from the lower memory. <br/> - Based on the Offset, a byte is selected and returned to the processor. <!--SR:!2026-01-03,164,442!2025-12-16,147,442-->
  - cache placement policies / set-associative cache ::@:: Set-associative cache is a trade-off between direct-mapped cache and fully associative cache. <p> A set-associative cache can be imagined as a n&nbsp;×&nbsp;m matrix. The cache is divided into 'n' sets and each set contains 'm' cache lines. A memory block is first mapped onto a set and then placed into any cache line of the set. <!--SR:!2026-01-03,164,442!2025-12-14,154,441-->
  - cache placement policies / set-associative cache / advantages ::@:: - The placement policy is a trade-off between direct-mapped and fully associative cache. <br/> - It offers the flexibility of using replacement algorithms if a cache miss occurs. <!--SR:!2025-12-29,160,439!2025-12-22,158,442-->
  - cache placement policies / set-associative cache / disadvantages ::@:: - The placement policy will not effectively use all the available cache lines in the cache and suffers from conflict miss. <!--SR:!2025-12-21,152,439!2025-12-29,160,439-->
  - cache placement policies / set-associative cache / examples ::@:: one-way \(direct-mapped\), two-way \(common\), four-way \(common\), eight-way, ..., fully associative <!--SR:!2025-12-27,158,442!2025-12-21,152,442-->
  - cache placement policies / set-associative cache / placement ::@:: - The set is determined by the index bits derived from the address of the memory block. <br/> - The memory block is placed in an available cache line in the set identified, and the tag is stored in the tag field associated with the line. If all the cache lines in the set are occupied, then the new data replaces the block identified through the replacement policy. <!--SR:!2025-12-15,146,442!2026-01-01,163,441-->
  - cache placement policies / set-associative cache / search ::@:: - The set is determined by the index bits derived from the address of the memory block. <br/> - The tag bits are compared with the tags of all cache lines present in selected set. If the tag matches any of the cache lines, it is a cache hit and the appropriate line is returned. If the tag does not match any of the lines, then it is a cache miss and the data is requested from next level in the memory hierarchy. <!--SR:!2025-11-08,115,419!2025-12-16,156,442-->
  - cache placement policies / set-associative cache / tradeoffs ::@:: Increasing associativity decreases miss rate but increases hit time \(search time\). But miss rate decrease with diminishing returns. <!--SR:!2025-12-22,153,439!2026-01-01,163,442-->
  - cache placement policies / set-associative cache / hardware ::@:: In direct-mapped cache, the tag is compared \(__this course__: and the valid bit is checked\) to calculate the _hit_ boolean, while the _data_ is read out. <p> In _n_-way associative cache, the above hardware is duplicated _n_ times. The _hit_ booleans are OR-ed, while the data is selected using a multiplexer. So lookup is _parallel_ in a cache set. <!--SR:!2025-12-29,160,442!2025-12-28,159,439-->
- [CPU cache](../../../../CPU%20cache.md) ::@:: A hardware cache used by the central processing unit \(CPU\) of a computer to reduce the average cost \(time or energy\) to access data from the main memory. A cache is a smaller, faster memory, located closer to a processor core, which stores copies of the data from frequently used main memory locations. <!--SR:!2025-12-27,158,442!2025-12-22,159,442-->
  - CPU cache / hierarchy ::@:: Most CPUs have a hierarchy of multiple cache levels \(L1, L2, often L3, and rarely even L4\), with different instruction-specific and data-specific caches at level 1. \(__this course__: The lecture slides show an example CPU with 2 L1 caches and L2 cache. The L1 caches are split into instruction cache and data cache.\) <!--SR:!2025-12-18,149,442!2025-12-23,154,442-->
  - CPU cache / instruction cache miss ::@:: The IF stage access the instruction pointed by the PC counter. If a cache hit happens, the pipeline continues. <p> Otherwise, a cache miss happens. stall the pipeline. The instruction is read from the main memory and placed into the cache. Then the pipeline restarts, with the IF stage trying to access the same instruction again, this time a cache hit. <!--SR:!2026-01-01,163,442!2026-01-01,163,439-->
- [cache replacement policies](../../../../general/cache%20replacement%20policies.md) ::@:: They are optimizing instructions or algorithms which a computer program or hardware-maintained structure can utilize to manage a cache of information. Caching improves performance by keeping recent or often-used data items in memory locations which are faster, or computationally cheaper to access, than normal memory stores. When the cache is full, the algorithm must choose which items to discard to make room for new data. <!--SR:!2025-12-24,155,442!2025-12-25,156,441-->
  - cache replacement policies / this course ::@:: \(__this course__: random replacement \(RR\), least recently used \(LRU\)\) <!--SR:!2025-12-28,159,442!2026-01-03,164,442-->
  - cache replacement policies / random replacement \(RR\) ::@:: Random replacement selects an item and discards it to make space when necessary. This algorithm does not require keeping any access history. It has been used in ARM processors due to its simplicity, and it allows efficient stochastic simulation. <!--SR:!2025-12-06,146,442!2025-12-29,160,442-->
  - cache replacement policies / least recently used \(LRU\) ::@:: Discards least recently used items first. This algorithm requires keeping track of what was used and when, which is cumbersome. It requires "age bits" for cache lines, and tracks the least recently used cache line based on these age bits. When a cache line is used, the age of the other cache lines changes. <p> It is costly to implement if associativity exceeds 2 or 4. <!--SR:!2025-12-14,154,442!2026-01-02,164,442-->
    - cache replacement policies / least recently used \(LRU\) / steps ::@:: On cache miss, replace the LRU position data with the new data, and move it to the MRU position. On cache hit, move the cached data to the MRU position. <!--SR:!2025-12-09,149,441!2025-12-27,158,441-->
- cache
  - cache / write policies ::@:: Cache writes must eventually be propagated to the backing store. The timing for this is governed by the _write policy_. The two primary write policies are: _write-through_ and _write-back_. <!--SR:!2025-12-24,155,442!2025-12-15,155,442-->
    - cache / write policies / write-back ::@:: Initially, writing is done only to the cache. The write to the backing store is postponed until the modified content is about to be replaced by another cache block. <!--SR:!2025-12-17,148,442!2025-12-24,160,442-->
      - cache / write policies / write-back / advantages ::@:: Processors can write at a rate limited by the cache instead of the memory. Then, when a replacement occurs, the entire cache block is written back into the main memory, effectively merging the writes to fully exploit high bandwidth transfer. <p> Since CPU speeds increase faster than DRAM speeds, this strategy is becoming more common. <!--SR:!2025-11-05,115,422!2025-12-31,162,439-->
      - cache / write policies / write-back / disadvantages ::@:: A write-back cache is more complex to implement since it needs to track which of its locations have been written over and mark them as _dirty_ for later writing to the backing store. The data in these locations are written back to the backing store only when they are evicted from the cache, a process referred to as a _lazy write_. For this reason, a read miss in a write-back cache may require two memory accesses to the backing store: one to write back the dirty data, and one to retrieve the requested data. <!--SR:!2025-12-11,151,442!2025-12-15,146,442-->
      - cache / write policies / write-back / write miss ::@:: Typically, a write-back cache typically employs write allocate, anticipating that subsequent writes or reads to the same location will benefit from having the data already in the cache. <!--SR:!2025-12-17,157,441!2025-12-28,159,439-->
    - cache / write policies / write-through ::@:: Writes are performed synchronously to both the cache and the backing store. <!--SR:!2025-12-26,162,442!2025-12-28,159,442-->
      - cache / write policies / write-through / advantages ::@:: It is easier to implement than write-back. Handling cache read-miss is simpler, because there is no need to write the dirty data to the memory then read from it, as in write-back. <!--SR:!2025-12-29,160,442!2025-12-08,148,439-->
      - cache / write policies / write-through / disadvantages ::@:: Multiple writes to the same location waste bandwidth compared to that in write-back. This potentially slows down read. <p> Often, a _write buffer_ to hold data to be written to the main memory is needed for a high-speed system. <!--SR:!2025-12-28,164,442!2025-12-16,147,441-->
      - cache / write policies / write-through / write-miss ::@:: Typically, a write-through cache uses no-write allocate. Here, subsequent writes have no advantage, since they still need to be written directly to the backing store. <!--SR:!2026-01-02,164,441!2025-12-17,148,442-->
    - cache / write policies / write-miss ::@:: Write operations do not return data. Consequently, a decision needs to be made for write misses: whether or not to load the data into the cache. This is determined by these _write-miss policies_: <!--SR:!2025-12-06,146,442!2026-01-01,163,442-->
      - cache / write policies / write-miss / write allocate ::@:: Data at the missed-write location is loaded to cache, followed by a write-hit operation. In this approach, write misses are similar to read misses. <!--SR:!2025-12-16,147,442!2025-12-24,155,442-->
      - cache / write policies / write-miss / no-write allocate ::@:: Data at the missed-write location is not loaded to cache, and is written directly to the backing store. In this approach, data is loaded into the cache on read misses only. <!--SR:!2025-12-26,157,442!2025-12-24,161,441-->

## week 14 lab

- datetime: 2025-05-06T15:00:00+08:00/2025-05-06T15:50:00+08:00, PT50M
- status: unscheduled

## week 14 tutorial

- datetime: 2025-05-06T18:00:00+08:00/2025-05-06T18:50:00+08:00, PT50M
- topic: pipeline
- classical RISC pipeline
  - classical RISC pipeline / instruction fetch
  - classical RISC pipeline / instruction decode
    - classical RISC pipeline / instruction decode / register write back
  - classical RISC pipeline / execute
  - classical RISC pipeline / memory access
  - classical RISC pipeline / register write back
    - classical RISC pipeline / register write back / hazard
  - classical RISC pipeline / diagram
  - classical RISC pipeline / diagrams
  - classical RISC pipeline / control
- hazard
  - hazard / causes
    - hazard / causes / data dependency
    - hazard / causes / control dependency
  - hazard / types
    - hazard / types / data
    - hazard / types / structural
    - hazard / types / control
  - hazard / bubbling
  - hazard / data hazards
    - hazard / data hazard / operand forwarding
      - hazard / data hazard / operand forwarding / limitation

## week 14 lecture 2

- datetime: 2025-05-09T09:00:00+08:00/2025-05-09T10:20:00+08:00, PT1H20M
- topic: virtual memory, revision
- [virtual memory](../../../../general/virtual%20memory.md) ::@:: It is a memory management technique that provides an "idealized abstraction of the storage resources that are actually available on a given machine" which "creates the illusion to users of a very large \(main\) memory". <!--SR:!2025-12-28,159,439!2025-12-31,162,441-->
  - virtual memory / motivations ::@:: The primary benefits of virtual memory include freeing applications from having to manage a shared memory space \(protection\), ability to share memory used by libraries between processes, increased security due to memory isolation, and being able to conceptually use more memory than might be physically available, using the technique of paging or segmentation. <!--SR:!2025-12-29,160,439!2025-12-19,150,442-->
  - virtual memory / operation ::@:: The computer's operating system, using a combination of hardware and software, maps memory addresses used by a program, called _virtual addresses_, into _physical addresses_ in computer memory. Main storage, as seen by a process or task, appears as a contiguous address space or collection of contiguous segments. <!--SR:!2025-12-23,154,442!2026-01-02,164,441-->
  - virtual memory / capacity extension ::@:: Software within the operating system may extend these capabilities, utilizing, e.g., disk storage, to provide a virtual address space that can exceed the capacity of real memory and thus reference more memory than is physically present in the computer. <p> Pages \(see below\) not used recently is in secondary storage. When the program accesses it, the page is _shuttled_ into memory \(primary storage\) and _replaces_ not recently used pages \(similar to the LRU cache replacement policy\). <!--SR:!2025-12-26,162,442!2026-07-28,312,402-->
  - virtual memory / paged ::@:: Nearly all current implementations of virtual memory divide a virtual address space into pages, blocks of contiguous virtual memory addresses. Pages on contemporary systems are usually at least 4 kilobytes in size; systems with large virtual address ranges or amounts of real memory generally use larger page sizes. <!--SR:!2025-12-26,157,439!2025-10-24,109,422-->
    - virtual memory / paged / motivation ::@:: Theoretically, we can have a giant table in memory that maps virtual addresses into physical addresses. But this is impractical. Instead, we split both the virtual and physical address space into _pages_, which are typically 4 kiB in size. Then the mapping operates on pages instead of addresses. Obviously, virtual pages and their corresponding physical pages should have the same size. <!--SR:!2026-01-03,164,442!2025-12-31,162,439-->
    - virtual memory / paged / page tables ::@:: They are used to translate the virtual addresses seen by the application into physical addresses used by the hardware to process instructions; such hardware that handles this specific translation is often known as the memory management unit. <!--SR:!2025-12-23,154,442!2025-12-22,153,439-->
      - virtual memory / paged / page tables / structure ::@:: Each entry in the page table holds a flag indicating whether the corresponding page is in real memory or not. If it is in real memory, the page table entry will contain the real memory address at which the page is stored. <p> Unlike cache entries, a tag field is not required since the entire virtual space address is represented in the page table. <!--SR:!2026-01-01,163,442!2025-12-26,157,441-->
      - virtual memory / paged / page tables / count ::@:: Systems can have, e.g., one page table for the whole system, separate page tables for each address space or process, separate page tables for each segment. \(__this course__: Our systems have one page table, whose address is stored in the _page table register_.\) <!--SR:!2025-11-02,112,422!2025-12-27,158,442-->
      - virtual memory / paged / page tables / address translation ::@:: Assuming the page size is 2<sup>_n_</sup> bytes. The memory address in binary representation can be separated into 2 parts: _virtual/physical page number_ \(remaining upper bits\) and _page offset_ \(lower _n_ bits\). <p> Address translation is simple: The _virtual_ page number of a _virtual_ memory address is used to access an page table entry, which contains the _physical_ page number if valid, and then simply replace the page number with the physical one to get the _physical_ memory address. <p> Note the number of page number bits can differ between virtual and physical memory addresses. <!--SR:!2025-12-28,164,442!2025-12-14,154,442-->
      - virtual memory / paged / page tables / page fault ::@:: When a reference is made to a page by the hardware, if the page table entry for the page indicates that it is not currently in real memory, the hardware raises a page fault exception, invoking the paging supervisor component of the operating system. <p> The penalty of a page fault is large. Program execution stalls until the page fault is resolved. So pages should _not_ be too small to reduce page faults, but _not_ too large to reduce _page fragmentation_. <!--SR:!2025-12-15,146,442!2025-12-26,157,442-->
- [translation lookaside buffer](../../../../general/translation%20lookaside%20buffer.md) \(TLB\) ::@:: It is a memory cache that stores the recent translations of virtual memory to physical memory. It is used to reduce the time taken to access a user memory location. It can be called an address-translation cache. <!--SR:!2026-01-01,163,442!2025-12-15,146,441-->
  - translation lookaside buffer / motivation ::@:: If TLB is not used, every memory access involves two memory accesses, one to read the page table for address translation, the other to read the actual physical memory. <p> We can exploit locality of reference again to mitigate this... <!--SR:!2025-11-03,113,422!2026-01-01,163,442-->
  - translation lookaside buffer / associativity ::@:: It is usually a small fully-associative cache with 16 to 64 entries. <!--SR:!2025-12-25,156,439!2025-12-16,147,442-->
  - translation lookaside buffer / structure ::@:: Each entry in the TLB consists of two parts: a tag and a value. If the tag of the incoming virtual address matches the tag in the TLB, the corresponding value \(physical page number\) is returned. <p> Extra fields in the page table may also be cached as well, including _valid_ bit, _dirty_ bit, _ref_ bit \(if it is in main memory \(primary storage\)\). <!--SR:!2025-12-21,152,442!2025-12-08,148,441-->
  - translation lookaside buffer / operation ::@:: Mostly works similarly to CPU caches. <p> First, read from TLB. If cached, translate the address. If not, read from page table. If valid, translate the address. Otherwise, a page fault is generated. After the page fault is resolved, the CPU memory access stage restarts. <!--SR:!2025-12-09,149,442!2025-12-14,154,439-->

## week 14 extra tutorial

- datetime: 2025-05-09T20:00:00+08:00/2025-05-09T20:50:00+08:00, PT50M
- topic: homework 4

> Dear COMP2611 students,
>
> We'll offer again the optional tutorial for homework.
>
> This Friday \(May 9\) 8pm will be the optional tutorial for HW4. PGTA \[redacted\] <br/>
> and \[redacted\] are going to lead it.
>
> \[redacted\]
>
> You can also find the Zoom links under COMP2611 Canvas.
>
> Best regards, <br/>
> \[redacted\] and \[redacted\]

## final examination

- datetime: 2025-05-19T16:30:00+08:00/2025-05-19T18:30:00+08:00, PT2H
- venue: S H Ho Sports Hall, Academic Building
- format
  - calculator: no
  - cheatsheet: no
  - referencing: closed book, closed notes
  - provided: \(none\)
  - questions: multiple choice questions ×10, long questions ×7
- grades: 100/100 → 100/100
  - statistics
    - timestamps: 2025-05-22T10:08+08:00 → 2025-05-24T11:32:09+08:00
    - mean: 58.96 → 59.53 \(provided: 60.12\)
    - standard deviation: ? → ? \(provided: 19.94\)
    - low: 0 → 0
    - lower quartile: 44 → 45
    - median: 61.5 → 62 \(provided: 62\)
    - upper quartile: 75.5 → 77
    - high: 100 → 100
    - distribution: ? → ![final examination distribution](attachments/final%20examination%20distribution.png)
- report
  - cache set \(0\) ::@:: Almost did not know what a "cache set" is... <p> A cache can consists of one to many cache sets. Each cache set has a number of cache line determined by its _associativity_. As a special case, a _fully-associative_ cache has exactly one cache set \(otherwise it is not fully-associative\). <!--SR:!2026-01-18,169,457!2026-01-18,169,457-->
  - cache miss \(0\) ::@:: On cache miss, the CPU \(at least for most designs\) does not _directly_ fetch the data or instruction from the main memory, but does so _indirectly_ via its cache; that is, the data or instruction is loaded into the CPU cache first, then the CPU reads it again, this time with a cache hit. <!--SR:!2025-12-22,153,442!2025-11-05,112,421-->
  - R format instruction signals \(0\) ::@:: The controls described in the lectures need to be changed to accommodate for a new R format instruction requiring _MemRead_ or _MemWrite_ to be 1. <p> The original controls does not pass the `funct` field to the main control, so it cannot distinguish R format instructions requiring memory access. Without the new instruction, this is okay, since all R format instructions do not require memory access.  <p> \(I wrote an answer that has the wrong explanation but contains the keyword "conflict", so the TA did not catch it...\) <!--SR:!2025-12-17,157,442!2025-12-14,145,439-->
- check
  - datetime: 2025-05-22T15:30:00+08:00 → 2025-05-22T17:00:00+08:00
  - venue: Lecture Theater G, Academic Building
  - report: \(none\)

> Dear COMP2611 students,
>
> COMP2611 final exam is arranged on May 19 Monday afternoon. Please find the exam details in this email.
>
> Date and Time: May 19 \(Monday\), 4:30 pm – 6:30 pm \(2 hours\)
>
> Venue \(main batch\): S H Ho Sports Hall. The seating plan will be released the day before the final exam.
>
> Venue \(SEN students\): Room 2302. SEN students will receive individual emails about the special exam time.
>
> Coverage: Everything learned \(including tutorials and labs\) during the semester, with emphasis on the knowledge not covered by midterm. For the “memory system” note set, since not all sections finished it, we will cover slides 1-64 \(excluding slide 60\). Anything in the lecture note sets marked “optional” is not included, e.g. CISC vs RISC, Carry Lookahead, Booth algorithm, floating point arithmetic.
>
> Reference materials: This is a closed book, closed note exam. The exam paper will provide the following diagrams/resources if needed:
>
> Green MIPS information sheet <br/>
> <https://course.cse.ust.hk/comp2611/reference/MIPS_Green_Sheet.pdf>
>
> Diagram of unsigned integer multiplication/division hardware \(optimized version\)
>
> Datapath and control of single-cycle processor
>
> Datapath and control of pipelined single-cycle processor
>
> Past papers:
>
> Two sample past papers have already been posted on COMP2611 course website -&gt; Exam.
>
> Kindly notice COMP2611 evolves and updates in the past year.  If you have no ideas on an exam question in the past paper, that means it is no longer covered in recent COMP2611 offerings.
>
> Although the knowledge tested are the same, exact question format may also vary in each exam.
>
> Revision suggestion:
>
> Go through the lecture notes once. Make sure you understand the examples and can work them out by your own. Revisit homework and tutorial exercises. Practice sample final exam papers. Then compare your answer with solution and reflect.
>
> Online Forum:
>
> You can always post your questions to COMP2611 Piazza
>
> <https://piazza.com/ust.hk/spring2025/comp2611>
>
> Instructor Q&A sessions:
>
> \[redacted\], F2F Q&A session
>
> May 19 \(Monday\), 11:00am to 1:00pm, Room 3525 \(Lifts 25/26, near CSE admin office\)
>
> \[redacted\], F2F Q&A session \(mixed mode, Zoom link \[redacted\] \)
>
> May 12 \(Monday\), 3:30pm-5:30pm, Room 3548 \(Lifts 27/28\)
>
> Good luck to all your final exams!
>
> Best regards,
>
> \[redacted\] and \[redacted\]
>
> COMP2611 instructors

## aftermath

### total

- grades: 98.8/100
  - statistics: \(none\)
