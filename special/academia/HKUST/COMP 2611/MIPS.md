---
aliases:
  - COMP 2611 MIPS
  - COMP 2611 Microprocessor without Interlocked Pipeline Stages
  - MIPS
  - Microprocessor without Interlocked Pipeline Stages
tags:
  - flashcard/active/special/academia/HKUST/COMP_2611/MIPS
  - language/in/English
---

# MIPS

- HKUST COMP 2611

## principles

This seems more like a pedagogical tool...

- good compromises ::@:: Instructions are 32 bits long, to make instruction fetching and decoding simpler. <!--SR:!2026-06-17,358,355!2026-06-02,343,350-->
- make common cases fast ::@:: Variants of instructions that accept _immediate_ operands instead of register or memory operands are available. <!--SR:!2026-04-13,293,330!2026-02-27,268,330-->
- simplicity favors regularity \(less cases\) ::@:: Each instruction is 32 bits long, and has a fixed number of operands. It makes CPU implementations simpler and allows better performance. <!--SR:!2026-03-01,270,330!2026-01-25,238,330-->
  - simplicity favors regularity / comparison ::@:: x86, a _complex_ instruction set computer \(CISC\) ISA, supports a variable number of operands. <!--SR:!2026-02-10,254,330!2026-02-28,269,330-->
- smaller is faster ::@:: Less registers means faster processors. More registers means more propagation delay \(longer travel time\). <!--SR:!2026-03-06,275,330!2026-02-11,255,330-->

## registers

Registers are {@{_fast_ temporary storage _inside_ the processor \(not on the main memory \(RAM\)\) used to hold _data_}@}. There is {@{a limited number}@} of registers. <!--SR:!2026-04-06,286,330!2026-04-13,293,330-->

Variables differ from registers in that {@{the former is a logical concept while the latter is a physical thing}@}. Thus, there can be {@{an unlimited number of variables}@}. <!--SR:!2026-02-09,253,330!2026-02-09,253,330-->

In MIPS, there are {@{32 registers}@}. They can be identified by {@{their names (depends on the _calling convention_) or their numbers \(from `$0` to `$31`\)}@}. They can hold {@{a _word_, which is 32 bits in size}@}. Commonly used registers include: {@{the readonly zero register `$zero` \(`$0`\), saved temporary registers `$s0`–`$s7` \(`$16`–`$23`\), \(non-saved\) temporary registers `$t0`–`$t7` \(`$8`–`$15`\), etc.}@} <!--SR:!2026-02-11,255,330!2026-02-05,249,330!2026-04-09,289,330!2026-02-07,251,330-->

Almost always, {@{the number of variables in a program is much higher than the number of registers}@}. To {@{store those data}@}, {@{register values are transferred from and to the main memory \(via the CPU cache\), but with more propagation delay}@}. <!--SR:!2026-02-27,268,330!2026-03-02,271,330!2026-02-07,251,330-->

The number of registers {@{is a balancing act: it should not be too few or too many}@}. If there are too few, {@{the potentially many variables need to be frequently transferred from and to the main memory \(RAM\), leading to performance loss}@}. If there are too many, {@{processors are more complicated, have higher clock cycle time, which also leads to performance loss}@}. <!--SR:!2026-04-07,287,330!2026-03-05,274,330!2026-03-17,284,330-->

\(__this course__: Note that when doing questions, {@{do not assume registers have a specific value, e.g. 0, unless otherwise specified}@}. That is, you need to {@{initialize its value}@}.\) <!--SR:!2026-11-03,458,401!2026-12-08,492,401-->

## memory

The main memory is usually {@{a physical RAM}@}. It can {@{store much data, much more than the registers}@}. <!--SR:!2026-03-01,270,330!2027-12-05,755,330-->

In MIPS, {@{the main memory cannot be manipulated directly}@}. Instead, {@{values need to be transferred from _registers_ to the main memory, and vice versa}@}. <!--SR:!2026-03-05,274,330!2026-04-12,293,330-->

We can treat the main memory as {@{a _contagious_ storage locations}@}. Each storage location {@{stores a byte, which has a size of 8 bits}@}. The storage location are addressed by {@{indices starting from 0}@}. Usually, addresses are {@{written in hexadecimal}@}. <!--SR:!2026-02-26,267,330!2026-03-07,276,330!2026-03-05,274,330!2026-02-25,266,330-->

In MIPS, to address a memory location, we need {@{a base address and an offset}@}. The base address is {@{provided by a register, while the offset is provided by a constant}@}. The actual address is {@{simply the sum of the base address and the offset}@}. Often, the base address is {@{the starting address of an array}@}, while the offset is {@{an array index _multiplied_ by the array element size \(in higher level programming languages, e.g. C, this multiplication is done for you\)}@}. {@{The _memory operand_ syntax}@} is {@{`offset($base)`, e.g. `-4($s0)`}@}. <!--SR:!2026-03-06,275,330!2026-03-07,276,330!2026-02-26,267,330!2026-02-10,254,330!2026-03-13,281,330!2026-03-15,282,330!2026-03-06,275,330-->

### endianness

When {@{addressing multiple bytes}@}, it is important to {@{take note of _endianness_: _big endian_ and _little endian_}@}. {@{A _big-endian_ system}@} stores {@{the most significant byte of a word at the smallest memory address and the least significant byte \(word _end_\) at the largest}@}. {@{A _little-endian_ system}@} stores {@{the least-significant byte \(word _end_\) at the smallest address}@}. It also describes {@{the order of byte transmission over a digital link}@}. Using a familiar example, when {@{you write numbers, you start with the most significant digit and end with the least significant digit from left to right}@}. This is {@{analogous to _big endian_}@}. <!--SR:!2026-03-13,281,330!2026-02-28,269,330!2026-04-14,294,330!2025-11-24,189,310!2026-03-01,270,330!2026-02-28,269,330!2026-03-07,276,330!2026-07-10,342,381!2026-11-29,484,401-->

For {@{assembly instructions that store multi-byte data}@}, it {@{uses the endianness of the underlying machine, so that you do not need to worry about endianness when defining data}@}. <!--SR:!2026-08-30,413,383!2026-08-19,408,383-->

Note that it does not make sense to {@{talk about the endianness of a register, as they have no memory addresses}@}. When transferring multiple bytes from and to the main memory, big-endian systems {@{stores them in the main memory in big-endian, transfers them to registers by interpreting them in big-endian, and receives them from registers by writing them in big-endian}@}, and {@{vice versa for little-endian}@}. In both cases, {@{the data transfer instructions are agnostic of the endianness, i.e. does not need to care about the endianness}@}. <!--SR:!2026-06-21,362,355!2026-06-18,359,355!2026-05-22,332,355!2026-05-10,321,355-->

## instructions

Each instruction is written as {@{`ins op_1, op_2, ..., op_n`, where `ins` is the instruction and `op_i` are its operands}@}. Each line {@{contain at most one instruction}@}. Comments {@{start with `#` and end with a newline}@}. <!--SR:!2026-04-09,290,330!2026-04-06,286,330!2025-12-07,189,310-->

Below, the accompanying code to the right is {@{a piece of pseudo C code showing its semantics}@}. For placeholders: <!--SR:!2026-05-27,337,355-->

- `$s`, `$t`, and `$d` \(in order of instruction encoding\) ::@:: It can be any 32-bit named/numbered register \(5 bits to encode\). <!--SR:!2026-06-11,352,355!2026-06-01,343,355-->
- `imm` ::@:: It can be any 16-bit constant, which may be unextended, sign-extended, or zero-extended depending on the instruction. <!--SR:!2026-05-15,325,355!2026-05-17,327,355-->
- `offset` ::@:: It can be any 16-bit signed constant. It can represent a signed 16-bit byte offset, or an address or label representable by a signed 16-bit 4-byte offset \(effectively 18 bits\) from the current instruction. <!--SR:!2026-01-30,243,335!2026-06-21,362,355-->
- `target` ::@:: It can be any 26-bit unsigned constant. It can represent an address or label that has its upper 4 bits same as the current instruction \(the lower 28 bits can be different, and the lower 2 bits must be 0\). <!--SR:!2026-05-26,336,355!2026-06-19,360,355-->
- `PC` ::@:: It is the 32-bit address of the current instruction \(program counter\). <!--SR:!2026-06-07,348,355!2026-06-06,347,350-->
  - `nPC` ::@:: It is a _concept_ \(_not_ a real register\) containing the 32-bit address of the _next_ instruction \(next program counter\), i.e. `PC+4`. <!--SR:!2026-11-28,483,401!2026-12-17,495,401-->
- `h` ::@:: It can be any 5-bit unsigned constant. It is used for bit-shit instructions. <!--SR:!2026-06-18,359,355!2026-06-09,350,355-->

Common instruction variants include {@{immediate `_i`, unsigned `_u` \(`_i` comes before `_u`\)}@}. The former {@{indicates that the instruction takes an 16-bit immediate operand in place of a register operand}@}. The latter {@{indicates that the instruction interprets the operands as unsigned integers, and additionally does not _trap_ on _overflow_}@}. Note that {@{signed integers in MIPS are always encoded using two's complement}@}. <!--SR:!2026-06-21,362,355!2026-06-07,348,350!2026-06-16,357,355!2026-08-23,416,372-->

One would notice that {@{some reasonable instructions are missing}@}. This is an example of {@{good design compromise between expressiveness and too many instructions reducing performance of all instructions}@}. <!--SR:!2026-03-02,271,330!2026-04-09,289,330-->

### program counter

{@{The program counter \(PC\) or instruction address register}@} contains {@{the 32-bit address of the current instruction}@}. {@{The _concept_ \(_not_ a real register\) next program counter \(nPC\)}@} contains {@{the next instruction to be executed}@}. Every time {@{an instruction is executed}@}, {@{the PC is updated to the nPC, and nPC is usually added 4 \(next instruction\)}@}. Note that some instruction {@{causes nPC to be added by an offset \(e.g. relative jump instructions\) or causes nPC to be set to a register \(e.g. semi-absolute jump instructions\)}@}. {@{The `goto` in the pseudo C code below}@} is {@{meant to indicate this}@}, but is {@{slightly different from that in C, as explained in the next sentence}@}. Note that in these cases, {@{the PC is still updated to the nPC before updating the nPC}@}, e.g. {@{the next instruction in memory after a jump instruction is still executed}@}. This is why {@{_branch delay slots_ \(mentioned below\) are added after jump instructions}@}. This also explains why {@{the "and link" instructions \(i.e. `jal`, `bgezal`, `bltzal`\) and PC-relative addressing mode is based on nPC or `PC+4`}@}. <!--SR:!2026-10-22,446,401!2026-12-04,488,401!2027-01-17,524,401!2027-01-09,514,401!2026-12-31,507,401!2026-11-17,469,401!2026-10-31,455,401!2026-10-29,453,401!2026-10-20,444,401!2027-01-10,519,401!2027-02-06,537,401!2026-11-10,465,401!2026-10-27,451,401!2027-07-01,651,412-->

\(__this course__: For this course, {@{you do not need to know _branch delay slots_}@}. That is, you write in {@{MIPS without branch delay slots, which MARS simulate by default}@}. But you do need to know that {@{if there is a branch, the PC will need be _flushed_}@}, which allures to that {@{nPC instead of PC is updated by branching instructions}@}.\) <!--SR:!2027-01-16,520,401!2026-11-08,463,401!2027-01-11,480,392!2026-03-20,151,425-->

The program counter {@{cannot be read or written directly}@}. However, it can be indirectly read {@{using `jal`, where the PC of the `jal` instruction _plus 8_ \(for MARS and this course, use _plus 4_\) is saved to `$ra`}@}. It is indirectly written {@{by executing instructions, or branching and jump instructions}@}. <!--SR:!2026-11-12,464,401!2026-11-07,462,401!2026-11-04,459,401-->

### operands

There are {@{3 types of operands}@} \(at least in this course\) in MIPS: {@{immediate \(constant\) operand, memory operand, and register operand}@}. Note that the first one is {@{limited to 16 bits \(see instruction encoding\)}@}, and {@{for _arithmetic_ operations \(e.g. excludes _bitwise_ operations), is always _sign-extended_}@}. <!--SR:!2026-06-19,360,355!2026-05-29,339,355!2026-05-10,320,355!2026-06-07,348,350-->

In terms of {@{execution time}@}, {@{immediate \(constant\) operands}@} are {@{the fastest as they are encoded in the instruction}@}. {@{Register operands}@} are {@{still fast since registers are inside to the processor}@}. {@{Memory operands}@} are {@{extremely slow comparatively since they are very far comparatively from the processor}@}. This is why {@{there are multiple variants of the same operation, but with one accepting immediate operands}@}. <!--SR:!2026-04-10,290,330!2026-04-06,287,330!2026-03-06,275,330!2026-03-13,281,330!2026-03-03,272,330!2026-02-08,252,330!2026-02-23,264,330!2026-02-09,253,330-->

Note that while {@{`$zero` or `$0`}@} has {@{the semantics of _constant_ zero}@}, it is {@{_not_ a constant operand but a register operand}@}. So {@{it can only be used in locations where a register operand is expected}@}. <!--SR:!2026-04-09,289,330!2026-03-07,276,330!2026-03-06,275,330!2026-02-10,254,330-->

### arithmetic instructions

- add ::@:: `add $d, $s, $t`: `$d = $s + $t;`, signed, traps on overflow <!--SR:!2026-06-16,357,355!2026-05-21,331,355-->
- add immediate ::@:: `addi $t, $s, imm`: `$t = $s + imm;`, signed, traps on overflow; `imm` is sign-extended <!--SR:!2026-05-18,328,355!2026-06-21,362,355-->
- add immediate unsigned ::@:: `addiu $t, $s, imm`: `$t = $s + imm;`, unsigned, does not trap on overflow; `imm` is sign-extended \(_surprise_!\) <!--SR:!2026-05-30,340,355!2026-05-24,334,355-->
  - add immediate unsigned / note ::@:: Recall that in two's complement, at a bit level, addition is the same as that for unsigned integers. Thus, for two's complement, `addiu` can be used in place of `addi` to avoid trapping on overflow. <!--SR:!2026-05-30,340,355!2026-05-11,321,355-->
- add unsigned ::@:: `addu $d, $s, $t`: `$d = $s + $t;`, unsigned, does not trap on overflow <!--SR:!2026-05-21,331,355!2026-06-17,358,355-->
  - add unsigned / note ::@:: Recall that in two's complement, at a bit level, addition is the same as that for unsigned integers. Thus, for two's complement, `addu` can be used in place of `add` to avoid trapping on overflow. <!--SR:!2027-09-23,697,335!2026-01-02,215,335-->
- divide ::@:: `div $s, $t`: `$LO = $s / $t; $HI = $s % $t;`, signed; `$LO` \(quotient\) is rounded towards zero, while `$HI` \(remainder\) is such that `$s == $t * $LO + $HI` <!--SR:!2026-05-09,319,355!2026-06-13,355,355-->
- divide immediate ::@:: `divi` does not exist. <!--SR:!2026-06-21,362,355!2026-06-12,353,355-->
- divide immediate unsigned ::@:: `diviu` does not exist. <!--SR:!2026-06-21,362,355!2026-06-17,358,355-->
- divide unsigned ::@:: `divu $s, $t`: `$LO = $s / $t; $HI = $s % $t;`, unsigned; `$LO` \(quotient\) is rounded towards zero <!--SR:!2026-06-14,355,355!2026-05-08,318,355-->
  - divide unsigned / note ::@:: Unlike addition and subtraction, two's complement signed division and unsigned division are not equivalent. <!--SR:!2026-05-27,337,355!2026-05-15,325,355-->
- multiply \(lower 32 bits\) ::@:: `mul $d, $s, $t`: `$d = $s * $t`, signed, lower 32 bits; `$LO` and `$HI` may or may not be cobbled \(MARS cobbles them\); for this course, treat it as a _pseudo-instruction_ \(even though it is not\) <!-- <https://stackoverflow.com/a/52748907> --> <!--SR:!2026-01-06,219,352!2026-02-24,265,352-->
- multiply unsigned \(lower 32 bits\) ::@:: `mulu` does not exist. <!--SR:!2026-08-02,399,372!2026-08-17,411,372-->
- multiply ::@:: `mult $s, $t`: `$HI:$LO = $s * $t;`, signed ; note the register placeholder `$d` is unused <!--SR:!2026-06-11,352,355!2026-05-11,321,355-->
  - multiply / overflow ::@:: Overflow is not possible if you consider `$HI:$LO` together. \(__this course__: No overflow occurs if every bit of `$HI` equals the sign bit of `$LO`.\) <!--SR:!2027-01-17,521,401!2026-06-07,340,381-->
- multiply immediate ::@:: `multi` does not exist. <!--SR:!2026-06-03,344,355!2026-06-06,347,350-->
- multiply immediate unsigned ::@:: `multiu` does not exist. <!--SR:!2026-05-11,321,355!2026-05-11,321,355-->
- multiply unsigned ::@:: `multu $s, $t`: `$HI:$LO = $s * $t;`, unsigned; note the register placeholder `$d` is unused <!--SR:!2026-05-29,339,355!2026-05-21,331,355-->
  - multiply unsigned / note ::@:: Unlike addition and subtraction, two's complement signed division and unsigned division are not equivalent. <!--SR:!2025-12-20,202,330!2026-04-26,306,350-->
  - multiply unsigned / overflow ::@:: Overflow is not possible if you consider `$HI:$LO` together. \(__this course__: No overflow occurs if every bit of `$HI` is 0.\) <!--SR:!2026-12-12,490,401!2027-01-24,524,401-->
- subtract ::@:: `sub $d, $s, $t`: `$d = $s - $t;`, signed, traps on overflow <!--SR:!2026-06-17,358,355!2026-05-24,335,355-->
- subtract immediate ::@:: `subi` does not exist. Use `addi` with a negative constant instead. <!--SR:!2026-06-10,351,355!2026-06-21,362,355-->
- subtract immediate unsigned ::@:: `subiu` does not exist. Use `addiu` with a negative constant instead. <!--SR:!2026-05-15,325,355!2026-05-19,329,355-->
- subtract unsigned ::@:: `subu $d, $s, $t`: `$d = $s - $t;`, unsigned, does not trap on overflow <!--SR:!2026-06-02,343,350!2026-05-09,319,355-->
  - subtract unsigned / note ::@:: Recall that in two's complement, at a bit level, subtraction is the same as that for unsigned integers. Thus, for two's complement, `subu` can be used in place of `sub` to avoid trapping on overflow. <!--SR:!2026-04-24,304,350!2026-05-11,321,355-->

### bitwise instructions

- bitwise and ::@:: `and $d, $s, $t`: `$d = $s & $t;` <!--SR:!2026-06-10,351,355!2026-05-18,328,355-->
- bitwise and immediate ::@:: `andi $t, $s, imm`: `$t = $s & imm;`; `imm` is zero-extended <!--SR:!2026-04-26,306,350!2026-06-10,352,350-->
- bitwise exclusive or ::@:: `xor $d, $s, $t`: `$d = $s ^ $t;` <!--SR:!2026-05-07,317,350!2026-06-07,348,350-->
- bitwise exclusive or immediate ::@:: `xori $t, $s, imm`: `$t = $s ^ imm;`; `imm` is zero-extended <!--SR:!2026-05-16,326,350!2026-05-09,320,355-->
- bitwise nor ::@:: `nor $d, $s, $t`: `$d = ~($s | $t);` <!--SR:!2026-05-10,320,355!2026-06-12,354,355-->
- bitwise nor immediate ::@:: `nori` does not exist. Unfortunately, it cannot be replaced by a single instruction. It can be replaced by `ori` and then a `nor` with `$0`. <!--SR:!2026-05-31,342,355!2026-05-26,336,350-->
- bitwise or ::@:: `or $d, $s, $t`: `$d = $s | $t;` <!--SR:!2026-05-11,321,355!2026-06-17,358,355-->
- bitwise or immediate ::@:: `ori $t, $s, imm`: `$t = $s | imm;`; `imm` is zero-extended <!--SR:!2026-06-06,347,350!2026-05-11,321,355-->
- shift left arithmetic ::@:: `sla` does not exist. It would have been equivalent to `sll`. <!--SR:!2026-05-03,313,355!2026-06-14,355,355-->
- shift left logical ::@:: `sll $d, $t, h`: `$d = $t << h;`, padded by 0 <!--SR:!2026-06-15,356,355!2026-01-04,217,335-->
  - shift left logical / arithmetic ::@:: Assuming _no overflow_, it has the same effect as multiplying a _signed_/_unsigned_ integer by 2<sup>_h_</sup>. <!--SR:!2027-01-10,515,401!2026-12-19,497,401-->
- shift left logical variable ::@:: `sllv $d, $t, $s`: `$d = $t << $s;`, padded by 0; if `$s >= 32`, MIPS IV does not define it, while MIPS32 takes the lower 5 bits <!--SR:!2026-06-12,353,355!2026-02-14,235,335-->
- shift right arithmetic ::@:: `sra $d, $t, h`: `$d = $t >> h;`, sign-extended <!--SR:!2026-04-15,295,350!2026-04-15,295,350-->
  - shift right arithmetic / arithmetic ::@:: It has the same effect as floor dividing \(i.e. rounded towards negative infinity\) a _signed_ integer by 2<sup>_h_</sup>. Overflow is impossible. <!--SR:!2026-04-11,272,381!2026-12-01,485,401-->
- shift right arithmetic variable ::@:: `srav $d, $t, $s`: `$d = $t >> $s;`, sign-extended; if `$s >= 32`, MIPS IV does not define it, while MIPS32 takes the lower 5 bits <!--SR:!2026-08-10,404,372!2027-08-05,673,352-->
- shift right logical ::@:: `srl $d, $t, h`: `$d = $t >> h;`, padded by 0 <!--SR:!2026-06-02,343,350!2026-06-03,344,350-->
  - shift right logical / arithmetic ::@:: It has the same effect as floor dividing \(i.e. rounded towards negative infinity\) an _unsigned_ integer by 2<sup>_h_</sup>. Overflow is impossible. <!--SR:!2026-12-29,509,401!2026-11-11,463,401-->
- shift right logical variable ::@:: `srlv $d, $t, $s`: `$d = $t >> $s;`, padded by 0; if `$s >= 32`, MIPS IV does not define it, while MIPS32 takes the lower 5 bits <!--SR:!2026-05-08,318,350!2025-12-05,200,335-->

### data instructions

- load byte ::@:: `lb $t, offset($s)`: `$t = *((*int8_t) &MEM[$s + offset]);`; the loaded 8 bits are sign-extended <!--SR:!2026-05-22,332,355!2025-12-25,207,335-->
- load byte unsigned ::@:: `lbu $t, offset($s)`: `$t = *((*uint8_t) &MEM[$s + offset]);`; the loaded 8 bits are zero-extended <!--SR:!2026-02-09,250,335!2026-05-26,336,350-->
- load upper immediate ::2:: `lui $t, imm`: `$t = imm << 16;`; `imm` is unextended; note the lower 16 bits are 0s
- load halfword ::@:: `lh $t, offset($s)`: `$t = *((*int16_t) &MEM[$s + offset]);`; the loaded 16 bits are sign-extended <!--SR:!2026-01-18,231,335!2026-05-09,319,355-->
- load halfword unsigned ::@:: `lhu $t, offset($s)`: `$t = *((*uint16_t) &MEM[$s + offset]);`; the loaded 16 bits are zero-extended <!--SR:!2026-01-01,214,330!2026-05-21,331,355-->
- load word ::@:: `lw $t, offset($s)`: `$t = *((*uint32_t) (&MEM[$s + offset]));` <!--SR:!2026-06-12,354,355!2026-05-08,318,355-->
- move from HI ::@:: `mfhi $d`: `$d = $HI;`; note the register placeholder is `$d` instead of `$s` <!--SR:!2026-05-11,321,355!2026-06-08,349,355-->
- move from LO ::2:: `mflo $d`: `$d = $LO;`; note the register placeholder is `$d` instead of `$s`
- store byte ::@:: `sb $t, offset($s)`: `*((*uint8_t) (&MEM[$s + offset])) = 0xff & $t;` <!--SR:!2026-01-01,214,330!2026-01-02,215,330-->
- store halfword ::@:: `sh $t, offset($s)`: `*((*uint16_t) (&MEM[$s + offset])) = 0xffff & $t;` <!--SR:!2026-05-22,332,355!2026-06-11,353,350-->
- store word ::@:: `sw $t, offset($s)`: `*((*uint32_t) (&MEM[$s + offset])) = $t;` <!--SR:!2025-12-19,201,330!2026-01-28,241,335-->

### jump instructions

- branch on equal ::@:: `beq $s, $t, offset`: `if ($s == $t) { goto nPC + offset << 2; }` <!--SR:!2026-05-07,317,355!2026-06-19,360,355-->
- branch on greater than or equal to zero ::@:: `bgez $s, offset`: `if ($s >= 0) { goto nPC + offset << 2; }` <!--SR:!2026-05-18,328,355!2025-12-28,210,335-->
- branch on greater than or equal to zero and link ::@:: `bgezal $s, offset`: `if ($s >= 0) { $ra = nPC + 4; goto nPC + offset << 2; }` \(`nPC+4` instead of nPC is due to a branch delay slot; for MARS and this course, ignore this and treat it as the next instruction: nPC\) <!--SR:!2026-03-16,255,330!2026-05-21,331,355-->
- branch on greater than zero ::@:: `bgtz $s, offset`: `if ($s > 0) { goto nPC + offset << 2; }` <!--SR:!2025-12-26,208,330!2026-01-23,236,335-->
- branch on greater than zero and link ::@:: `bgtzal` does not exist. For uncertain reasons \(maybe because ≥ and < only requires reading the sign bit\), only `bgezal` \(≥\) and `bltzal` \(<\) exist. <!--SR:!2026-06-02,343,355!2026-01-30,243,335-->
- branch on less than or equal to zero ::@:: `blez $s, offset`: `if ($s <= 0) { goto nPC + offset << 2; }` <!--SR:!2026-06-10,351,350!2026-04-21,301,350-->
- branch on less than or equal to zero and link ::@:: `blezal` does not exist. For uncertain reasons \(maybe because ≥ and < only requires reading the sign bit\), only `bgezal` \(≥\) and `bltzal` \(<\) exist. <!--SR:!2026-02-10,231,335!2026-06-18,359,355-->
- branch on less than zero ::@:: `bltz $s, offset`: `if ($s < 0) { goto nPC + offset << 2; }` <!--SR:!2026-05-21,332,355!2027-08-02,644,335-->
- branch on less than zero and link ::@:: `bltzal $s, offset`: `if ($s < 0) { goto offset $ra = nPC + 4; goto nPC + offset << 2; }` \(`nPC+4` instead of nPC is due to a branch delay slot; for MARS and this course, ignore this and treat it as the next instruction: nPC\) <!--SR:!2026-06-08,349,355!2027-03-26,554,350-->
- branch on not equal ::@:: `bne $s, $t, offset`: `if ($s != $t) { goto nPC + offset << 2; }` <!--SR:!2026-05-15,325,350!2026-05-09,319,350-->
- jump ::@:: `j target`: `goto (nPC & 0xf0000000) | (target << 2);` <!--SR:!2026-06-14,355,355!2025-12-26,208,335-->
- jump and link ::@:: `jal target`: `$ra = nPC + 4; goto (nPC & 0xf0000000) | (target << 2);` \(`nPC+4` instead of nPC is due to a branch delay slot; for MARS and this course, ignore this and treat it as the next instruction: nPC\) <!--SR:!2026-05-10,320,355!2026-05-11,321,355-->
- jump register ::@:: `jr $s`: `goto $s;` <!--SR:!2026-06-02,344,355!2026-05-09,319,355-->

### comparison instructions

- set on less than ::@:: `slt $d, $s, $t`: `$d = $s < $t;`, signed <!--SR:!2025-12-29,211,335!2026-06-12,353,355-->
- set on less than immediate ::@:: `slti $t, $s, imm`: `$t = $s < imm;`, signed; `imm` is sign-extended <!--SR:!2026-05-15,325,355!2026-05-11,321,355-->
- set on less than immediate unsigned ::@:: `sltiu $t, $s, imm`: `$t = $s < imm;`, unsigned; `imm` is sign-extended \(_surprise_!\) <!--SR:!2026-10-30,409,310!2026-05-15,325,355-->
- set on less than unsigned ::@:: `sltu $d, $s, $t`: `$d = $s < $t;`, unsigned <!--SR:!2026-06-08,349,350!2026-05-10,320,350-->

## floating-point instructions

Note that the floating-point register operands must be {@{even numbered for double instructions}@}. <!--SR:!2025-11-27,128,404-->

- absolute double ::@:: `abs.d $fd, $fs`: `$fd = abs($fs);` <!--SR:!2025-11-19,124,404!2026-10-19,389,404-->
- absolute single ::@:: `abs.s $fd, $fs`: `$fd = abs($fs);` <!--SR:!2025-12-01,132,404!2025-11-21,126,404-->
- add double ::@:: `add.d $fd, $fs, $ft`: `$fd = $fs + $ft;` <!--SR:!2025-11-20,125,404!2025-11-19,124,404-->
- add single ::@:: `add.s $fd, $fs, $ft`: `$fd = $fs + $ft;` <!--SR:!2025-11-21,126,404!2025-11-23,128,404-->
- branch on false ::@:: `bc1f target`: `if (!$FLAG) { goto (nPC & 0xf0000000) | (target << 2); }` <!--SR:!2025-12-02,133,404!2025-11-23,128,404-->
- branch on true ::@:: `bc1t target`: `if ($FLAG) { goto (nPC & 0xf0000000) | (target << 2); }` <!--SR:!2026-11-19,416,404!2025-11-29,130,404-->
- compare equal to double ::@:: `c.eq.d $fs, $ft`: `$FLAG = $fs == $ft;` <!--SR:!2025-11-20,125,404!2025-11-20,125,404-->
- compare equal to single ::@:: `c.eq.s $fs, $ft`: `$FLAG = $fs == $ft;` <!--SR:!2025-11-24,129,404!2025-11-22,127,404-->
- compare greater than double ::@:: `c.gt.d $fs, $ft`: `$FLAG = $fs > $ft;` <!--SR:!2025-11-19,124,404!2025-11-22,127,404-->
- compare greater than single ::@:: `c.gt.s $fs, $ft`: `$FLAG = $fs > $ft;` <!--SR:!2025-11-23,128,404!2025-11-20,126,404-->
- compare greater than or equal to double ::@:: `c.ge.d $fs, $ft`: `$FLAG = $fs >= $ft;` <!--SR:!2025-11-21,126,404!2025-11-18,123,404-->
- compare greater than or equal to single ::@:: `c.ge.s $fs, $ft`: `$FLAG = $fs >= $ft;` <!--SR:!2025-11-19,124,404!2025-11-19,124,404-->
- compare less than double ::@:: `c.lt.d $fs, $ft`: `$FLAG = $fs < $ft;` <!--SR:!2025-11-16,42,364!2025-11-21,126,404-->
- compare less than single ::@:: `c.lt.s $fs, $ft`: `$FLAG = $fs < $ft;` <!--SR:!2025-11-18,123,404!2025-11-19,125,404-->
- compare less than or equal to double ::@:: `c.le.d $fs, $ft`: `$FLAG = $fs <= $ft;` <!--SR:!2025-11-30,131,404!2025-11-18,124,404-->
- compare less than or equal to single ::@:: `c.le.s $fs, $ft`: `$FLAG = $fs <= $ft;` <!--SR:!2025-11-19,124,404!2025-11-28,129,404-->
- compare not equal to double ::@:: `c.neq.d $fs, $ft`: `$FLAG = $fs != $ft;` <!--SR:!2025-12-04,135,404!2025-12-01,132,404-->
- compare not equal to single ::@:: `c.neq.s $fs, $ft`: `$FLAG = $fs != $ft;` <!--SR:!2025-11-19,124,404!2025-11-18,123,404-->
- divide double ::@:: `div.d $fd, $fs, $ft`: `$fd = $fs / $ft;` <!--SR:!2025-11-27,128,404!2025-11-21,126,404-->
- divide single ::@:: `div.s $fd, $fs, $ft`: `$fd = $fs / $ft;` <!--SR:!2025-11-20,125,404!2025-11-23,128,404-->
- load double coprocessor 1 ::@:: `ldc1 $ft, offset($s)`: `$ft = *((*float64_t) (&MEM[$s + offset]));` <!--SR:!2025-11-18,123,404!2025-11-23,128,404-->
- load word coprocessor 1 ::@:: `lwc1 $ft, offset($s)`: `$ft = *((*float32_t) (&MEM[$s + offset]));` <!--SR:!2025-11-22,127,404!2026-07-28,303,384-->
- multiply double ::@:: `mul.d $fd, $fs, $ft`: `$fd = $fs * $ft;` <!--SR:!2025-11-22,127,404!2025-11-28,129,404-->
- multiply single ::@:: `mul.s $fd, $fs, $ft`: `$fd = $fs * $ft;` <!--SR:!2025-11-23,128,404!2025-11-29,130,404-->
- negate double ::@:: `neg.d $fd, $fs`: `$fd = -$fs;` <!--SR:!2025-11-24,129,404!2025-12-01,132,404-->
- negate single ::@:: `neg.s $fd, $fs`: `$fd = -$fs;` <!--SR:!2025-11-21,126,404!2025-11-22,127,404-->
- store double coprocessor 1 ::@:: `sdc1 $ft, offset($s)`: `*((*float64_t) (&MEM[$s + offset])) = $ft;` <!--SR:!2025-11-18,123,404!2026-06-07,275,384-->
- store word coprocessor 1 ::@:: `swc1 $ft, offset($s)`: `*((*float32_t) (&MEM[$s + offset])) = $ft;` <!--SR:!2025-11-30,131,404!2025-12-02,133,404-->
- subtract double ::@:: `sub.d $fd, $fs, $ft`: `$fd = $fs - $ft;` <!--SR:!2025-12-03,134,404!2025-11-22,127,404-->
- subtract single ::@:: `sub.s $fd, $fs, $ft`: `$fd = $fs - $ft;` <!--SR:!2025-11-18,123,404!2025-11-24,129,404-->

### miscellaneous instructions

- no operation ::@:: `noop`: does nothing; encoded by all 0s, which represents `sll $0, $0, 0` \(in fact, _almost all_ instruction that has `$0` as its destination register does nothing\) <!--SR:!2026-05-08,318,350!2026-06-12,353,355-->
- syscall ::@:: `syscall`: generates a software interrupt <!--SR:!2026-01-28,238,335!2026-04-15,295,350-->

### encoding

All instructions are {@{4 bytes \(32 bits\) long}@}. This is an example of {@{the _regularity_ principle}@}. There are {@{3 formats: R format \(for R instructions\), I format \(for I instructions\), and J format \(for J instructions)}@}. Multiple formats {@{increases hardware complexity, but the formats are kept similar to try to reduce this}@}. Below, the format fields {@{start from higher bits to lower bits}@}. <!--SR:!2026-06-11,352,355!2026-05-16,326,355!2026-05-10,321,355!2026-05-08,319,355!2026-05-08,319,355-->

- R format ::@:: all operands are registers \(ignoring the "immediate" operand in bit-shift instructions\) without offsets <p> opcode: 6 bits → rs: 5 bits → rt: 5 bits → rd: 5 bits → shift \(shamt\): 5 bits → funct: 6 bits <!--SR:!2026-05-15,325,355!2026-05-08,318,355-->
- I format ::@:: one operand is immediate \(the "immediate" operand in bit-shift instructions is not really immediate\) or an offset is present <p> opcode: 6 bits → rs: 5 bits → rt: 5 bits → imm: 16 bits <!--SR:!2026-04-22,303,350!2026-05-10,320,355-->
- J format ::@:: the only operand is an pseudo-address <p> opcode: 6 bits → pseudo-address: 26 bits <!--SR:!2026-06-08,349,355!2026-05-09,320,355-->

The format fields include {@{opcode, rs, rt, rd, shift \(shamt\), funct, imm, and pseudo-address}@}. They mean: <!--SR:!2026-06-20,361,355-->

- opcode ::@:: 6 bits; opcode of the instruction; R format: this is almost always 0, since the funct field is used instead <!--SR:!2026-06-13,354,355!2026-05-08,318,355-->
- rs ::@:: 5 bits; R format: first source register operand; I format: source or memory register operand <!--SR:!2026-01-04,217,335!2026-05-23,334,355-->
- rt ::@:: 5 bits; R format: second source register operand; I format: destination or non-memory register operand <!--SR:!2026-06-10,352,350!2026-06-10,351,355-->
- rd ::@:: 5 bits; R format: destination register operand <!--SR:!2026-05-10,321,350!2026-06-03,344,350-->
- shift \(shamt\) ::@:: 5 bits; R format: number of bits to shift, ranging from 0 to 31 \(i.e. unsigned\), and should almost always be 0 for non-bit-shift instructions <!--SR:!2026-06-06,347,350!2027-08-06,658,335-->
- funct ::@:: 6 bits; R format: opcode of the instruction, and is almost always used instead of the opcode field <!--SR:!2026-05-23,333,350!2026-04-24,304,350-->
- imm ::@:: 16 bits; I format: a 16-bit immediate constant that may be unextended, sign-extended, or zero-extended depending on the instruction, a signed 16-bit offset, or an address or label representable by a signed 16-bit 4-byte offset \(effectively 18 bits\) from the current instruction <!--SR:!2025-12-27,209,335!2026-05-23,333,355-->
- pseudo-address ::@:: 26 bits; J format: a 26-bit unsigned constant, representing an address or label that has its upper 4 bits same as the current instruction \(the lower 28 bits can be different, and the lower 2 bits must be 0\) <!--SR:!2027-03-30,505,315!2026-06-20,361,355-->

The register fields are encoded {@{by the named registers' corresponding number name}@}. <!--SR:!2026-04-15,295,350-->

For {@{bit-shift instructions}@}, note that {@{unlike other instructions, for variable bit-shift instructions, `$s` \(the rs field\) is on the right hand side instead of the left hand side, and `$t` \(the rt field\) is on the left hand side instead of the right hand side}@}. Also, {@{for "immediate" bit-shift instructions, `$s` \(the rs field\) is unused}@}. For {@{instructions taking a single register operand only}@}, {@{`$s` is usually used, and `$d` \(R format\) or `$t` \(I format\) is used if the register is to be written \(e.g. `lui`, `mfhi`, `mflo`\)}@}. For {@{instructions without operands \(e.g. `syscall`\)}@}, {@{they are in R format}@}. <!--SR:!2026-02-18,259,352!2026-04-19,291,352!2026-08-08,404,372!2026-07-30,396,372!2026-08-22,415,372!2027-07-03,653,412!2027-07-02,652,412-->

Notice that {@{some fields are unused}@}. Sometimes, {@{they can be any value \(and we would not care\), but sometimes not}@}, so it is {@{best to always set unused fields to all 0s \(unless otherwise specified\)}@}. <!--SR:!2026-05-26,336,355!2026-01-24,237,335!2026-07-25,393,372-->

## calling conventions

There are {@{two _major_ calling conventions}@} for MIPS: {@{O32, N32/N64}@}. We will {@{use O32}@} for this course. <!--SR:!2026-03-03,272,330!2026-02-25,266,330!2026-02-27,268,330-->

Also take note of {@{callee-saved \(preserved on call\) and caller-saved registers}@}. This is explained in [§ procedures](#procedures) below. <!--SR:!2027-01-13,518,401-->

### O32 calling convention

The 32 registers are used as follows:

| Name            | Number      | Use                                                                       | Callee must preserve?                                                                                                   |
|:---------------:| ----------- | ------------------------------------------------------------------------- |:-----------------------------------------------------------------------------------------------------------------------:|
| __`$zero`__     | `$0`        | constant 0                                                                | —                                                                                                                       |
| __`$at`__       | `$1`        | assembler temporary                                                       | <div style="background: #FFC7C7; color: black; vertical-align: middle; text-align: center;">No</div>                    |
| __`$v0`–`$v1`__ | `$2`–`$3`   | values for function returns and expression evaluation                     | <div style="background: #FFC7C7; color: black; vertical-align: middle; text-align: center;">No</div>                    |
| __`$a0`–`$a3`__ | `$4`–`$7`   | function arguments                                                        | <div style="background: #FFC7C7; color: black; vertical-align: middle; text-align: center;">No</div>                    |
| __`$t0`–`$t7`__ | `$8`–`$15`  | temporaries                                                               | <div style="background: #FFC7C7; color: black; vertical-align: middle; text-align: center;">No</div>                    |
| __`$s0`–`$s7`__ | `$16`–`$23` | saved temporaries                                                         | <div style="background: #9EFF9E; color: black; vertical-align: middle; text-align: center;">Yes</div>                   |
| __`$t8`–`$t9`__ | `$24`–`$25` | temporaries                                                               | <div style="background: #FFC7C7; color: black; vertical-align: middle; text-align: center;">No</div>                    |
| __`$k0`–`$k1`__ | `$26`–`$27` | reserved for OS kernel                                                    | —                                                                                                                       |
| __`$gp`__       | `$28`       | global pointer                                                            | <div style="background: #9EFF9E; color: black; vertical-align: middle; text-align: center;">Yes (except PIC code)</div> |
| __`$sp`__       | `$29`       | [stack pointer](../../../../general/stack-based%20memory%20allocation.md) | <div style="background: #9EFF9E; color: black; vertical-align: middle; text-align: center;">Yes</div>                   |
| __`$fp`__       | `$30`       | [frame pointer](../../../../general/frame%20pointer.md#FRAME-POINTER)     | <div style="background: #9EFF9E; color: black; vertical-align: middle; text-align: center;">Yes</div>                   |
| __`$ra`__       | `$31`       | [return address](../../../../general/return%20statement.md)               | —                                                                                                                       |

> __flashcards__
>
> - register blocks ::@:: `$zero` <br/> `$at` <br/> `$v0`–`$v1` \(2\) <br/> `$a0`–`$a3` \(4\) <br/> `$t0`–`$t7` \(8\) <br/> `$s0`–`$s7` \(8\) <br/> `$t8`–`$t9` \(2\) <br/> `$k0`–`$k1` \(2\) <br/> `$gp` <br/> `$sp` <br/> `$fp` <br/> `$ra` <!--SR:!2026-03-14,224,270!2026-10-27,393,290-->
>   - register blocks / semantics ::@:: zero → asm temp → expr eval & fun ret ×2 → fun arg ×4 → temp ×8 → saved temp ×8 → temp ×2 → kernel ×2 → global ptr → stack ptr → frame \(base\) ptr → return addr <!--SR:!2025-12-22,199,310!2026-03-13,281,330-->
> - __`$zero`__ ::@:: `$0`: constant 0 <!--SR:!2026-04-09,289,330!2026-04-07,287,330-->
> - __`$at`__ ::@:: `$1`: assembler temporary <!--SR:!2026-03-16,283,330!2026-03-07,276,330-->
> - __`$v0`–`$v1`__ ::@:: `$2`–`$3`: values for function returns and expression evaluation <!--SR:!2026-04-08,288,330!2026-03-06,275,330-->
> - __`$a0`–`$a3`__ ::@:: `$4`–`$7`: function arguments <!--SR:!2026-03-05,274,330!2026-04-14,294,330-->
> - __`$t0`–`$t7`__ ::@:: `$8`–`$15`: temporaries <!--SR:!2026-01-27,240,330!2026-02-25,266,330-->
> - __`$s0`–`$s7`__ ::@:: `$16`–`$23`: saved temporaries <!--SR:!2026-03-18,285,330!2026-03-04,273,330-->
> - __`$t8`–`$t9`__ ::@:: `$24`–`$25`: temporaries <!--SR:!2026-02-27,268,330!2026-04-10,290,330-->
> - __`$k0`–`$k1`__ ::@:: `$26`–`$27`: reserved for OS kernel <!--SR:!2025-11-16,181,310!2026-03-01,270,330-->
> - __`$gp`__ ::@:: `$28`: global pointer <!--SR:!2026-02-11,255,330!2026-03-15,282,330-->
> - __`$sp`__ ::@:: `$29`: [stack pointer](../../../../general/stack-based%20memory%20allocation.md) <!--SR:!2025-11-11,176,310!2026-03-02,271,330-->
> - __`$fp`__ ::@:: `$30`: [frame pointer](../../../../general/frame%20pointer.md#FRAME-POINTER) <!--SR:!2026-03-13,281,330!2026-04-13,293,330-->
> - __`$ra`__ ::@:: `$31`: [return address](../../../../general/return%20statement.md) <!--SR:!2026-02-04,248,330!2026-04-14,294,330-->
> - callee-saved register blocks ::@:: saved temp, global ptr \(except PIC code\), stack ptr, frame \(base\) ptr <p> \(__this course__: additionally, return addr\) <!--SR:!2026-03-05,274,330!2027-03-17,534,310-->
> - caller-saved register blocks ::@:: asm temp, expr eval & fun ret, fun arg, temp <!--SR:!2026-04-06,286,330!2027-05-07,543,310-->

The caller places {@{procedure arguments in `$a0`–`$a3` \(4 registers\)}@} \(if you have more arguments, {@{they will need to be passed in the stack}@}\). Then it {@{invokes `jal` to jump to the procedure \(callee\)}@}. The callee saves {@{`$ra` to the stack using the pseudo-instruction `push`}@}. Then it {@{executes}@}. Then it places {@{the return value in `$v0`–`$v1` \(2 registers\) \(the 2 registers are usually used together to hold a 64-bit value\)}@}. Then it {@{pops the stack to `$ra` using the pseudo-instruction `pop`, and returns to the caller by `jr $ra`}@}. <!--SR:!2026-12-12,494,401!2026-11-23,475,401!2027-02-02,533,401!2026-11-23,473,401!2027-01-11,520,401!2026-11-16,471,401!2026-11-04,458,401-->

If {@{you have more than 4 arguments}@}, then you {@{pass the extra arguments \(i.e. arguments after the 4th argument\), _pushing_ from _right to left_ \(so that the stack top points to the 1st extra argument\)}@}. Then, the callee {@{_pops_ the extra arguments from the stack and uses them}@}, so {@{the caller does not need to pop the extra arguments from the stack itself}@}. <!--SR:!2027-02-04,535,401!2026-12-14,492,401!2026-11-06,461,401!2026-11-07,461,401-->

## assembly

{@{The assembler}@} is {@{responsible for translating human-readable assembly to machine-readable machine code}@}. That means we need to {@{learn how to write the human-readable assembly file}@}. <!--SR:!2026-04-14,294,330!2026-03-16,283,330!2026-02-27,268,330-->

### assembly format

Comments {@{start with `#` and end with a newline}@}. {@{Labels}@} are {@{like "bookmarks" of the program}@}, so that {@{you can reference the "bookmark" from other assembly lines by its name}@}. Its syntax is {@{`(label name): (code)`}@}. To {@{load the address of a label into a register}@}, use {@{the _pseudo-instruction_ `la $reg, (label name)` \(load address\)}@}. To {@{specify a location to jump to in an instruction}@}, {@{simply use the label name}@}. <!--SR:!2026-02-06,250,330!2026-02-03,247,330!2026-02-24,265,330!2026-04-08,288,330!2026-02-28,269,330!2026-03-13,281,330!2026-02-11,255,330!2026-02-11,255,330!2026-02-23,264,330-->

In a program, you usually {@{have 2 segments: `.data` and `.text`}@}. To begin such a segment, {@{simply start it with the segment header `.(segment name)` in its own line}@}. Then, {@{all text after this line and before the next segment header}@} belongs to that segment. In {@{the `.data` segment}@}, you {@{put data inside}@}. You can {@{modify the data while executing the program using the instruction `sw`}@}. In {@{the `.text` segment}@}, you {@{put runnable code inside \(the name "text" is quite un-descriptive, but this is historical convention...\)}@}. <!--SR:!2026-02-26,267,330!2026-04-07,288,330!2026-04-08,289,330!2026-03-18,285,330!2026-02-25,266,330!2026-01-28,241,330!2026-02-04,248,330!2026-02-06,250,330-->

In the `.data` segment, {@{data are stored into the memory _contagiously_ in declaration order}@}. The first byte of data {@{may have an arbitrary memory address, called _offset_}@}, and {@{later bytes are stored contagiously \(sometimes with small padding between different data for _alignment_\) after the first byte}@}. <!--SR:!2026-02-26,267,330!2026-04-06,286,330!2026-04-09,290,330-->

{@{The above "instructions" starting with a period `.`}@} are {@{more properly called _assembler directives_}@}. They include directives that {@{specify alignment, data, strings, symbol visibility, etc.}@} They are {@{not actual MIPS instructions}@} since {@{they are processed by the assembler during assembly rather than run during program execution}@}. <!--SR:!2026-02-11,255,330!2026-04-11,292,330!2026-02-26,267,330!2026-04-11,291,330!2026-02-08,252,330-->

### assembly directives

- `.align <n>` ::@:: _Align_ the _next_ datum on a 2<sup>_n_</sup>-byte boundary. That is, the next datum starts at an address that is a multiple of 2<sup>_n_</sup>. <p> If _n_ is 0, automatic _alignment_ is turned off, since 2<sup>0</sup> = 1, which is effectively no alignment. <!--SR:!2026-03-04,273,330!2026-02-03,247,330-->
- `.ascii <str>` ::@:: Stores a non-null-terminated \(ASCII\) string. <!--SR:!2026-04-10,291,330!2026-03-02,271,330-->
- `.asciiz <str>` ::@:: Stores a null-terminated \(ASCII\) string. <!--SR:!2026-03-03,272,330!2026-03-13,281,330-->
- `.byte <b1>, ..., <bn>` ::@:: Stores the specified _n_ bytes \(8 bits\). <!--SR:!2026-03-16,283,330!2026-04-13,293,330-->
- `.data` ::@:: Starts the data segment. <!--SR:!2026-01-29,242,330!2026-02-01,245,330-->
- `.double <d1>, ..., <dn>` ::@:: Stores the specified _n_ doubles \(64 bits, 8 bytes\). <!--SR:!2026-02-02,246,330!2026-04-10,290,330-->
- `.float <f1>, ..., <fn>` ::@:: Stores the specified _n_ floats \(32 bits, 4 bytes\). <!--SR:!2026-03-13,281,330!2026-04-12,292,330-->
- `.globl <sym>` ::@:: \(The name is _not_ a typo!\) Declare the symbol `<sym>` is global. The symbol is not removed from the resulting object/program file. That is, other assembly files can reference it. This is also required for the entry point label, so that the OS knows where to start the program. <!--SR:!2026-01-29,242,330!2026-04-11,291,330-->
- `.half <h1>, ..., <hn>` ::@:: Stores the specified _n_ half-words \(16 bits, 2 bytes\). <!--SR:!2026-02-24,265,330!2026-03-02,271,330-->
- `.space <num>` ::@:: Reserves the specified number of _bytes_. This can be used to define global but uninitialized variables. <!--SR:!2026-12-23,503,401!2026-12-03,483,401-->
- `.text [<addr>]` ::@:: Starts the code \(text\) segment, starting at the \(optional\) address `<addr>`. <!--SR:!2025-12-08,190,310!2026-03-04,273,330-->
- `.word <w1>, ..., <wn>` ::@:: Stores the specified _n_ words \(32 bits, 4 bytes\). <!--SR:!2026-04-14,294,330!2026-03-05,274,330-->

### entry point

The convention is {@{the entry point \(first instruction to be executed when a program starts\) is labeled by the label `.__start`}@}. Additionally, {@{the label needs to be global, specified using `.globl __start`}@}. For example, a way to start a program is: <p> {@{<pre>.text<br/>.globl \_\_start<br/>\_\_start:<br/># your instructions here</pre>}@}. <!--SR:!2026-01-31,244,330!2026-02-11,255,330!2026-03-01,270,330-->

## control flow

In {@{higher level programming languages}@}, we have {@{`do-while`, `if`, `for`, `while`, etc. for control flow}@}. In MIPS, we have {@{`beq` (branch if equal), `bne` (branch if not equal), and `j` (jump) for control flow}@}. These, {@{coupled with comparison instructions \(introduced below\)}@}, can {@{support implementing all conventional control flow structures in higher level programming languages}@}, and additionally {@{allows for unconventional \(less readable\) control flow}@}. <!--SR:!2026-03-03,272,330!2026-03-13,281,330!2026-03-07,276,330!2027-11-25,746,330!2026-02-11,255,330!2026-02-25,266,330-->

To {@{convert structured control flow statements into assembly}@} manually, {@{identify _basic blocks_, which is a sequence of consecutive code that has no branching _to_ and _from_ other code}@}. Then, {@{a control flow graph can be constructed out of these basic blocks}@}. Finally, {@{_label_ the basic blocks at their beginnings and add conditional and/or unconditional jumps at their endings}@} to {@{model the control flow graph}@}. \(__this course__: Include {@{the beginning label and the ending conditional and/or unconditional jumps}@} in a basic block.\) {@{A compiler}@} {@{essentially does the same thing automatically}@}, and {@{with additional optimizations \(e.g. reordering\) for performance and/or code size}@}. Also, during program execution, {@{an advanced processor}@} may {@{identify instructions that form basic blocks and accelerate them}@}. <!--SR:!2026-04-12,292,330!2026-02-06,250,330!2026-04-09,289,330!2025-11-20,185,310!2026-03-15,282,330!2026-04-08,288,330!2026-01-25,238,330!2026-02-28,269,330!2026-02-26,267,330!2026-04-13,293,330!2026-01-26,239,330-->

To convert {@{an `if...else if...else` statement}@}, a common pattern is {@{a bunch of comparison and conditional jumps to the basic blocks, then the basic blocks each ending with a jump to the exit label, and finally the exit label at the end}@}. To convert {@{an `while` statement}@}, a common pattern is {@{a loop label, then comparison and conditional jump to the exit label, the code, and finally a jump to the loop label}@}. You can extrapolate the rest for yourself. You may also simplify the code. <!--SR:!2026-03-17,284,330!2025-12-07,189,310!2026-03-03,272,330!2026-03-02,271,330-->

## pseudo-instructions

Since {@{MIPS have few instructions}@}, some common code {@{requires multiple instructions}@}. Pseudo-instructions are {@{_assembler macros_ that help replace these multiple instructions with a single line}@}. Since {@{these instructions are not real}@}, they are {@{replaced by multiple instructions implementing the pseudo-instruction during assembly}@}, and thus {@{does not appear in the resulting program file}@}. Note that this also means {@{the set of pseudo-instructions available is not standardized and may vary across different assemblers}@}. That means {@{some pseudo-instructions below may not be usable in your assembler}@}. It also means {@{different assemblers may use different implementations \(in particular, different from that given below\) to replace the same pseudo-instruction}@}. <!--SR:!2026-05-25,336,355!2026-06-08,349,350!2026-05-09,320,355!2026-05-11,321,350!2026-05-09,319,355!2026-05-16,326,350!2027-01-11,516,401!2027-01-14,523,401!2027-07-04,654,412-->

The benefit of pseudo-instructions is that {@{they simplify your code to make it more understandable}@}. The _only_ cost is that {@{a register, `$at`, is reserved for use to replace pseudo-instructions with real instructions by the assembler}@}. \({@{Requiring multiple instructions is _not_ a cost}@} since {@{with or without pseudo-instructions, you still need multiple instructions unless the architecture makes it a real instruction}@}.\) <!--SR:!2027-02-05,536,401!2026-10-25,449,401!2027-01-02,513,401!2027-01-25,525,401-->

- absolute ::@:: `abs $d, $s`: `$d = abs($s)`; implemented by `addu $d, $zero, $s; bgez $d, 2; (branch delay slot); sub $d, $zero, $s;` \(use 1 instead of 2 for MIPS without branch delay slots, which MARS simulate by default\) <!--SR:!2026-04-05,262,361!2026-07-17,364,381-->
- branch on equal to zero ::@:: `beqz $s, offset`: `if ($s == 0) { goto nPC + offset << 2; }`; implemented by `beq $s, $zero, offset;` <!--SR:!2025-12-19,139,416!2025-12-23,143,416-->
- branch on greater than ::@:: `bgt $s, $t, offset`: `if ($s > $t) { goto nPC + offset << 2; }`; implemented by `slt $at, $t, $s; bne $at, $zero, offset;` <!--SR:!2026-11-23,478,401!2026-11-05,460,401-->
- branch on greater than or equal to ::@:: `bge $s, $t, offset`: `if ($s >= $t) { goto nPC + offset << 2; }`; implemented by `slt $at, $s, $t; beq $at, $zero, offset;` <!--SR:!2026-07-24,367,381!2026-12-18,496,401-->
- branch on less than ::@:: `blt $s, $t, offset`: `if ($s < $t) { goto nPC + offset << 2; }`; implemented by `slt $at, $s, $t; bne $at, $zero, offset;` <!--SR:!2026-06-18,340,381!2026-11-09,464,401-->
- branch on less than or equal to ::@:: `ble $s, $t, offset`: `if ($s <= $t) { goto nPC + offset << 2; }`; implemented by `slt $at, $t, $s; beq $at, $zero, offset;` <!--SR:!2026-11-24,479,401!2025-12-23,201,361-->
- branch on not equal to zero ::@:: `bnez $s, offset`: `if ($s != 0) { goto nPC + offset << 2; }`; implemented by `bne $s, $zero, offset;` <!--SR:!2025-12-23,143,416!2025-12-18,138,416-->
- load address ::@:: `la $d, addr`: `$d = &addr;`, but `addr` is an address or label; implemented by `lui $at, addr[16:32]; ori $d, $at, addr[0:16];` <!--SR:!2026-05-08,318,355!2025-12-16,198,330-->
- load immediate ::@:: `li $d, imm`: `$d = imm;`, but `imm` is a 32-bit unsigned integer; implemented by `lui $at, imm[16:32]; ori $d, $at, imm[0:16];` <!--SR:!2026-04-24,304,350!2026-06-08,349,350-->
- move ::@:: `mov $d, $s`: `$d = $s;`; implemented by `or $d, $zero, $s;` <!--SR:!2027-01-12,517,401!2026-12-21,497,401-->
- negate ::@:: `neg $d, $s`: `$d = -$s;`; implemented by `subu $d, $zero, $s;` <!--SR:!2026-11-01,456,401!2026-12-30,506,401-->
- not ::@:: `not $d, $s`: `$d = ~$s;`; implemented by `nor $d, $zero, $s;` <!--SR:!2027-05-11,597,335!2026-06-12,353,355-->
- pop ::@:: `pop [$d=$ra]`: pops a 32-bit value from the stack to `$d`; implemented by `lw $d, 0($sp); addi $sp, $sp, 4;` <!--SR:!2026-11-19,471,401!2027-01-04,513,401-->
  - pop / usage ::@:: In practice, when you want to pop multiple values at once \(e.g. popping extra arguments from the stack\), using multiple `pop` is inefficient. Instead, you retrive the multiple values directly using `lw` using offsets from `$sp`, then adjust `$sp` upward apporpriately to shrink the stack. <!--SR:!2026-11-25,475,401!2026-11-03,457,401-->
- push ::@:: `push [$s=$ra]`: pushes the 32-bit value of `$s` to the stack; implemented by `addi $sp, $sp, -4; sw $s, 0($sp);` <!--SR:!2026-11-24,474,401!2027-02-03,534,401-->
  - push / usage ::@:: In practice, when you want to push multiple values at once \(e.g. pushing extra arguments to the stack\), using multiple `push` is inefficient. Instead, you adjust `$sp` downward enough to grow the stack to accommodate the new values, then save the multiple values directly using `sw` using offsets from `$sp`. <!--SR:!2026-08-17,370,381!2027-01-26,526,401-->
- set on greater than ::@:: `sgt $d, $s, $t`: `$d = $s > $t;`; implemented by `slt $d, $t, $s;` <!--SR:!2026-12-28,504,401!2027-01-31,537,401-->
- set on greater than or equal to ::@:: `sge $d, $s, $t`: `$d = $s >= $t`; implemented by `slt $at, $s, $t; xori $d, $at, 1;` <!--SR:!2026-09-03,381,381!2026-07-26,369,381-->

Note that some pseudo-instructions have {@{the same name as some of the _real_ instructions}@}. Whether the instruction or the pseudo-instruction is {@{used depends on the operands}@}. For example, {@{the load word `lw` instruction}@} has {@{several related pseudo-instructions of the same name that does the same thing}@} but {@{for operands not following the format `lw $t, $s(offset)`}@}, which are provided for {@{convenience, e.g. loading data addressed by a label (`lw $t, label`), etc.}@}. <!--SR:!2026-10-19,458,383!2026-10-03,443,383!2026-11-04,470,383!2026-04-30,310,363!2026-09-24,438,383!2026-10-30,465,383-->

\(__this course__: Some questions may {@{require you to not use any pseudo-instructions}@}.\) <!--SR:!2026-06-19,360,355-->

## procedures

In {@{higher level programming languages}@}, we have {@{functions/procedures/subroutines for to group related code and reuse them}@}. In MIPS, we can {@{emulate this feature}@}. Note that a high-level language compiler {@{does essentially the same thing when compiling your program, but they are abstracted away}@}. <!--SR:!2026-12-05,489,401!2027-01-02,508,401!2026-12-26,502,401!2026-11-18,473,401-->

Overall, to call a procedure in MIPS, the caller needs to {@{place the arguments/parameters in specified locations, then transfer control \(jump and link\) to the callee}@}. Then, the callee {@{pushes `$ra` to the stack, acquires the necessary resources, and performs its task}@}. Finally, {@{the callee places the return value \(if any\) in a specified location, pops the stack to `$ra`, and return control \(return\) to the caller}@}. The caller then {@{may access the return value for further use}@}. The specified locations are specified by {@{a calling convention}@}. Note that {@{if you do not call any other procedures in your procedure and your procedure does not modify `$ra` explicitly}@}, you can {@{skip pushing `$ra` to the stack at the beginning and popping `$ra` from the stack at the end}@}. \(__this course__: In this course, we use {@{the [O32 calling convention](#O32%20calling%20convention)}@}.\) <!--SR:!2027-01-01,512,401!2026-12-13,491,401!2027-01-15,519,401!2026-10-19,443,401!2026-12-25,501,401!2026-10-17,441,401!2026-12-15,493,401!2026-12-28,508,401-->

Also take note of {@{callee-saved \(preserved on call\) and caller-saved registers}@}. _Callee-saved_ means {@{the register value is the same before and after calling a procedure}@}. Note this does not mean {@{the register value cannot change during the procedure, just that the register value must be restored before returning}@}. One way to do so is {@{if the registers need to be modified during the procedure, save them to the stack and restore them before returning}@}. _Caller-saved_ means {@{there is no guarantee that the register value is the same before and after calling a procedure}@}. Note this does not mean {@{the register value _must_ change during the procedure, just that the caller cannot _rely_ on it being the same}@}. <!--SR:!2026-10-28,452,401!2026-10-24,448,401!2026-12-29,505,401!2026-12-27,503,401!2026-08-01,361,381!2026-11-21,473,401-->

If you follow the above steps, {@{nested procedures \(calling procedures inside procedures\) and recursion \(procedure calling itself\)}@} works automagically. There is an optimization for {@{procedures not calling any other procedures}@}: it can skip {@{saving `$ra` to the stack, since `$ra` is not modified \(unless the procedure modifies it explicitly\)}@}. <!--SR:!2025-11-28,129,404!2025-11-21,126,404!2025-11-24,129,404-->

## memory layout

A typical MIPS program memory is {@{addressed by 32-bit unsigned integers}@}. Thus, there are {@{2<sup>32</sup> memory byte locations, or 2<sup>30</sup> memory _word_ locations}@}. <!--SR:!2026-12-24,504,401!2026-12-02,482,401-->

It can be separated into {@{5 segments}@}: {@{\(in increasing address\) reserved, text, static data, dynamic data, and stack}@}. Tbe text segment {@{_usually_ starts from 0x0040&nbsp;0000}@}. The static data {@{_usually_ starts from 0x1000&nbsp;0000}@} \(e.g. MARS {@{uses 0x1001&nbsp;0000}@}\), and is somewhat related to {@{the global pointer `$gp` \(e.g. MARS uses 0x1000&nbsp;8000\)}@}. The dynamic data {@{comes after the static data \(no fixed memory address though\)}@}. The stack is {@{different}@}: {@{the previous segments}@} {@{grows in size towards increasing address}@}, but the stack {@{grows in size towards decreasing address}@}. It {@{_usually_ starts from 0x7fff&nbsp;fffc \(0x8000&nbsp;0000 – 0x4\)}@} \(e.g. MARS {@{uses 0x7fff&nbsp;effc}@}\), stored in {@{the stack pointer `$sp`}@}, and {@{_decreases_ as it grow in size}@}. <!--SR:!2026-12-01,481,401!2026-11-11,466,401!2026-11-07,462,401!2026-03-19,249,381!2026-11-15,470,401!2026-08-06,366,381!2026-05-04,313,381!2026-01-31,140,424!2026-02-01,141,424!2026-02-07,146,424!2026-02-02,137,424!2026-02-03,138,424!2026-02-02,137,424!2026-02-02,137,424!2026-02-02,137,424-->

The text segment {@{holds your code}@}, corresponding to {@{the `.text` segment in your assembly file}@}. <!--SR:!2026-10-18,442,401!2026-11-20,475,401-->

The static data segment {@{holds global variables}@}, corresponding to {@{the `.data` segment in your assembly file}@}. <!--SR:!2026-11-21,476,401!2026-10-26,450,401-->

The dynamic data segment is {@{the heap, and is allocated using `malloc` in C \(e.g. C++, Java: `new`\)}@}. It does not {@{correspond to any segment in your assembly file}@}. <!--SR:!2026-12-11,493,401!2027-01-09,518,401-->

The stack segment is {@{automatic storage, used to store local variables in higher level programming language}@}. It does not {@{correspond to any segment in your assembly file}@}. In MIPS, you use it to {@{store extra local variables more than that allowed by the number of registers, and the return address `$ra`}@}. To manipulate this segment, you can use {@{the pseudo-instructions `push` and `pop` to push or pop a 32-bit value to the stack}@}, which manipulates this segment {@{like the data structure _stack_, last-in first-out \(hence its name\)}@}. \(See above for what real instructions they translate to.\) The {@{address of the stack top}@} is {@{stored in `$sp`}@}. <!--SR:!2026-11-27,482,401!2026-12-22,502,401!2026-10-27,451,401!2026-10-23,447,401!2026-10-20,444,401!2026-11-18,470,401!2027-01-01,507,401-->

## addressing modes

MIPS \(MIPS I\) have {@{only one addressing mode: base + displacement}@}. <!--SR:!2026-11-06,460,401-->

\(__this course__: whole paragraph\) However, for this course, we consider addressing mode {@{to include referencing data, not just referencing memory in operands}@}. If so, we have {@{5 addressing mode}@}: {@{immediate, register, base \(+ displacement\), PC-relative, and pseudo-direct addressing}@}. <!--SR:!2026-11-02,457,401!2026-11-26,481,401!2026-11-22,474,401-->

- immediate addressing ::@:: Not really an addressing mode... It refers to the 16-bit immediate field in an I instruction. <!--SR:!2026-11-28,478,401!2026-11-19,474,401-->
- register addressing ::@:: Not really an addressing mode... It refers to the register fields in an R or I instruction. <!--SR:!2027-01-23,523,401!2026-12-25,505,401-->
- base \(+ displacement\) addressing ::@:: Some I instructions interpret the 16-bit immediate field as an address offset from the value of the `$s` register. The `$s` is known as the _base_ and the offset is known as the _displacement_. The operand is written as `offset($s)`. <!--SR:!2027-01-18,522,401!2026-11-17,472,401-->
- PC-relative addressing ::@:: Some I instructions interpret the 16-bit immediate field as an address offset from the program counter \(PC\). These instructions are branch instructions. <p> The address offset is in _words_ \(4 bytes\), not _bytes_, since instructions are aligned to words. The address offset \(multiplied by 4\) is added to nPC \(or `PC+4`\) to find the branch target \(the reason is mentioned above\). This means instructions up to 2<sup>15</sup> words/instructions or 128 kiB away are addressable. <p> Simply put, the branch address is `nPC + offset << 2` or `PC + 4 + offset << 2`. <!--SR:!2026-07-30,378,381!2027-01-30,530,401-->
- pseudo-direct addressing ::@:: The J instructions interpret the 26-bit pseudo-address as the jump target. <p> The address pseudo-address is in _words_ \(4 bytes\), not _bytes_, since instructions are aligned to words. So it can address the 28 lower bits of a 32-bit address or 256 MiB of memory, with the 2 lower bits always being 0. The 4 upper bits of a 32-bit address are provided by the 4 upper bits of the program counter \(PC\). This explains why it is called a "pseudo-address". <p> Simply put, the jump address is `(nPC & 0xf0000000) | (offset << 2)`. Note the `&` operates on `nPC` instead of `PC`. <!--SR:!2026-11-05,459,401!2026-07-10,362,381-->

A problem with PC-relative addressing is that {@{the branch target may be too far away}@}. The assembler {@{may rewrite a branch instruction as a branch instruction followed by a jump instruction, so that pseudo-direct addressing can be used}@}. If pseudo-direct addressing is insufficient, {@{storing the 32-bit address into a register and using `jr` suffices}@}. <!--SR:!2027-01-03,512,401!2026-10-28,452,401!2027-01-13,522,401-->

## interrupt

{@{An _interrupt_, _exception_, or _trap_}@} is {@{a request for the processor to interrupt currently executing code \(when permitted\), so that the event can be processed in a timely manner}@}. MIPS {@{supports interrupts}@}. <!--SR:!2027-01-23,530,401!2027-01-08,517,401!2027-01-19,523,401-->

When {@{an interrupt occurs}@}, control {@{jumps to a predefeined address containing instructions to handle the interrupt}@}. {@{The address of the interrupted instruction}@} is {@{saved to an _exception program counter_ \(EPC\)}@}, so that {@{the interrupt handler can _choose_ to resume the interrupted code using `jr` \(jump register\)}@}. <!--SR:!2026-12-04,484,401!2026-10-19,443,401!2027-01-16,523,401!2026-10-29,453,401!2026-12-06,490,401-->

A common interruption cause is {@{signed integer overflow in arithmetic operations, e.g. `add`, `addi`, and `subi`}@}. Note that {@{their unsigned counterparts, e.g. `addu`, `addiu`, and `subu`, do _not_ interrupt even if there are \(unsigned\) integer overflows}@}. <!--SR:!2026-11-12,467,401!2026-06-17,339,381-->

## floating point

MIPS optionally supports {@{IEEE754 single-precision and double-precision formats}@}. It is handled by {@{an optional floating-point unit \(FPU\), referred to as coprocessor 1 \(CP1\)}@}. <!--SR:!2025-11-24,129,404!2025-11-24,129,404-->

It has its own {@{registers}@}. There are {@{32 32-bit registers}@}, each named {@{`$f_`, where the underscore is an integer in between 0 and 31 \(inclusive\)}@}. Each even-numbered register represents {@{a single-precision format number}@}. Alternatively, each even-numbered register along with the next odd-numbered register represent {@{a double-precision format number}@}. The lower/even-numbered register {@{contains the lower bits}@}, e.g. {@{`$f1:$f0` but not `$f2:$f1` or `$f0:$f1`}@}. These registers are directly accessible {@{from the coprocessor only}@}, so {@{they cannot be used in normal instructions directly}@}. Also, the zeroth floating-point register `$f0` is {@{a normal register instead of always holding 0 like `$zero`}@}. \(Of course, for MIPS64, all of the above is slightly different...\) <!--SR:!2025-11-22,127,404!2025-12-02,133,404!2025-11-21,126,404!2025-11-22,127,404!2025-11-29,130,404!2025-12-04,135,404!2025-11-18,123,404!2025-11-17,123,404!2025-11-18,124,404!2025-11-23,128,404-->

It also has its own {@{instructions}@}. They are listed in [§ floating-point instructions](#floating-point%20instructions). Most of them can only use {@{the coprocessor registers}@}. Common suffixes include {@{-`c1` for "coprocessor 1"}@} and {@{-`.s` and -`.d` for "single-precision" and "double-precision" respectively}@}. There are also interesting differences from normal instructions: <!--SR:!2025-11-21,126,404!2025-11-20,125,404!2025-11-20,125,404!2025-11-18,123,404-->

- arithmetic operations ::@:: Multiplication and division store the result into the destination register instead of special registers, similar to other arithmetic operations. <!--SR:!2025-11-19,125,404!2025-11-19,124,404-->
- comparison ::@:: There is a boolean flag storing the result of the last comparison instruction `c.*.s` or `c.*.d`, which are then used by `b1ct` \(branch if the flag is true\) and `b1cf` \(branch if the flag is false\). <!--SR:!2025-11-20,126,404!2025-11-22,127,404-->
- data transfer ::@:: Since immediate operands cannot store floating point numbers, registers are transferred using `ldc1`, `lwc1`, `sdc1`, and `swc1`. Constants are stored somewhere in the main memory, and then referenced by `offset($gp)`. <!--SR:!2025-11-30,131,404!2026-07-18,295,384-->
- immediate operands ::@:: They cannot be used to represent floating point numbers because they are too small \(16 bits is less than 32 bits\). <!--SR:!2025-11-27,128,404!2025-11-20,125,404-->
- signedness ::@:: All operations are always signed. <!--SR:!2025-11-20,125,404!2025-11-24,129,404-->

## miscellaneous

### 32-bit immediate

The immediate field can {@{only up to 16 bits}@}. A natural question arises: {@{How do we store a 32-bit signed/unsigned integer}@}? The answer is {@{using `lui` and `ori` together}@}. Since {@{this is a common operation}@}, {@{the pseudo-instruction `li` is available and does the same thing}@}. <!--SR:!2027-02-01,532,401!2027-01-05,514,401!2026-10-21,445,401!2027-01-31,531,401!2027-01-03,509,401-->
