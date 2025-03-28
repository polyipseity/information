---
aliases:
  - COMP 2611 MIPS
  - COMP 2611 Microprocessor without Interlocked Pipeline Stages
  - MIPS
  - Microprocessor without Interlocked Pipeline Stages
tags:
  - flashcard/active/special/academia/HKUST/COMP_2611/MIPS
  - function/index
  - language/in/English
---

# MIPS

- HKUST COMP 2611

## principles

This seems more like a pedagogical tool...

- good compromises ::@:: Instructions are 32 bits long, to make instruction fetching and decoding simpler. <!--SR:!2025-04-07,17,315!2025-04-07,17,310-->
- make common cases fast ::@:: Variants of instructions that accept _immediate_ operands instead of register or memory operands are available. <!--SR:!2025-04-02,16,290!2025-04-01,15,290-->
- simplicity favors regularity \(less cases\) ::@:: Each instruction is 32 bits long, and has a fixed number of operands. It makes CPU implementations simpler and allows better performance. <!--SR:!2025-04-01,15,290!2025-03-31,14,290-->
  - simplicity favors regularity / comparison ::@:: x86, a _complex_ instruction set computer \(CISC\) ISA, supports a variable number of operands. <!--SR:!2025-03-31,14,290!2025-04-01,15,290-->
- smaller is faster ::@:: Less registers means faster processors. More registers means more propagation delay \(longer travel time\). <!--SR:!2025-04-01,15,290!2025-03-31,14,290-->

## registers

Registers are {@{_fast_ temporary storage _inside_ the processor \(not on the main memory \(RAM\)\) used to hold _data_}@}. There is {@{a limited number}@} of registers. <!--SR:!2025-04-02,16,290!2025-04-02,16,290-->

Variables differ from registers in that {@{the former is a logical concept while the latter is a physical thing}@}. Thus, there can be {@{an unlimited number of variables}@}. <!--SR:!2025-03-31,14,290!2025-03-31,14,290-->

In MIPS, there are {@{32 registers}@}. They can be identified by {@{their names (depends on the _calling convention_) or their numbers \(from `$0` to `$31`\)}@}. They can hold {@{a _word_, which is 32 bits in size}@}. Commonly used registers include: {@{the readonly zero register `$zero` \(`$0`\), saved temporary registers `$s0`–`$s7` \(`$16`–`$23`\), \(non-saved\) temporary registers `$t0`–`$t7` \(`$8`–`$15`\), etc.}@} <!--SR:!2025-03-31,14,290!2025-03-31,14,290!2025-04-02,16,290!2025-03-31,14,290-->

Almost always, {@{the number of variables in a program is much higher than the number of registers}@}. To {@{store those data}@}, {@{register values are transferred from and to the main memory, but with more propagation delay}@}. <!--SR:!2025-04-01,15,290!2025-04-01,15,290!2025-03-31,14,290-->

The number of registers {@{is a balancing act: it should not be too few or too many}@}. If there are too few, {@{the potentially many variables need to be frequently transferred from and to the main memory \(RAM\), leading to performance loss}@}. If there are too many, {@{processors are more complicated, have higher clock cycle time, which also leads to performance loss}@}. <!--SR:!2025-04-02,16,290!2025-04-01,15,290!2025-04-02,16,290-->

## memory

The main memory is usually {@{a physical RAM}@}. It can {@{store much data, much more than the registers}@}. <!--SR:!2025-04-01,15,290!2025-03-31,14,290-->

In MIPS, {@{the main memory cannot be manipulated directly}@}. Instead, {@{values need to be transferred from _registers_ to the main memory, and vice versa}@}. <!--SR:!2025-04-01,15,290!2025-04-02,16,290-->

We can treat the main memory as {@{a _contagious_ storage locations}@}. Each storage location {@{stores a byte, which has a size of 8 bits}@}. The storage location are addressed by {@{indices starting from 0}@}. Usually, addresses are {@{written in hexadecimal}@}. <!--SR:!2025-04-01,15,290!2025-04-01,15,290!2025-04-01,15,290!2025-04-01,15,290-->

In MIPS, to address a memory location, we need {@{a base address and an offset}@}. The base address is {@{provided by a register, while the offset is provided by a constant}@}. The actual address is {@{simply the sum of the base address and the offset}@}. Often, the base address is {@{the starting address of an array}@}, while the offset is {@{an array index _multiplied_ by the array element size \(in higher level programming languages, e.g. C, this multiplication is done for you\)}@}. {@{The _memory operand_ syntax}@} is {@{`offset($base)`, e.g. `-4($s0)`}@}. <!--SR:!2025-04-01,15,290!2025-04-01,15,290!2025-04-01,15,290!2025-03-31,14,290!2025-04-02,16,290!2025-04-02,16,290!2025-04-01,15,290-->

### endianness

When {@{addressing multiple bytes}@}, it is important to {@{take note of _endianness_: _big endian_ and _little endian_}@}. {@{A _big-endian_ system}@} stores {@{the most significant byte of a word at the smallest memory address and the least significant byte \(word _end_\) at the largest}@}. {@{A _little-endian_ system}@} stores {@{the least-significant byte \(word _end_\) at the smallest address}@}. It also describes {@{the order of byte transmission over a digital link}@}. <!--SR:!2025-04-02,16,290!2025-04-01,15,290!2025-04-02,16,290!2025-04-02,16,290!2025-04-01,15,290!2025-04-01,15,290!2025-04-01,15,290-->

For {@{assembly instructions that store multi-byte data}@}, it {@{uses the endianness of the underlying machine, so that you do not need to worry about endianness when defining data}@}. <!--SR:!2025-03-29,4,323!2025-03-29,4,323-->

Note that it does not make sense to {@{talk about the endianness of a register, as they have no memory addresses}@}. When transferring multiple bytes from and to the main memory, big-endian systems {@{stores them in the main memory in big-endian, transfers them to registers by interpreting them in big-endian, and receives them from registers by writing them in big-endian}@}, and {@{vice versa for little-endian}@}. In both cases, {@{the data transfer instructions are agnostic of the endianness, i.e. does not need to care about the endianness}@}. <!--SR:!2025-04-07,17,315!2025-04-07,17,315!2025-04-06,16,315!2025-04-05,15,315-->

## instructions

Each instruction is written as {@{`ins op_1, op_2, ..., op_n`, where `ins` is the instruction and `op_i` are its operands}@}. Each line {@{contain at most one instruction}@}. Comments {@{start with `#` and end with a newline}@}. <!--SR:!2025-04-02,16,290!2025-04-02,16,290!2025-04-02,16,290-->

Below, the accompanying code to the right is {@{a piece of pseudo C code showing its semantics}@}. For placeholders: <!--SR:!2025-04-06,16,315-->

- `$s`, `$t`, and `$d` \(in order of instruction encoding\) ::@:: It can be any 32-bit named/numbered register \(5 bits to encode\). <!--SR:!2025-04-07,17,315!2025-04-06,16,315-->
- `imm` ::@:: It can be any 16-bit constant, which may be unextended, sign-extended, or zero-extended depending on the instruction. <!--SR:!2025-04-06,16,315!2025-04-06,16,315-->
- `offset` ::@:: It can be any 16-bit signed constant. It can represent a signed 16-bit byte offset, or an address or label representable by a signed 16-bit 4-byte offset \(effectively 18 bits\) from the current instruction. <!--SR:!2025-04-01,13,295!2025-04-07,17,315-->
- `target` ::@:: It can be any 26-bit unsigned constant. It can represent an address or label that has its upper 4 bits same as the current instruction \(the lower 28 bits can be different, and the lower 2 bits must be 0\). <!--SR:!2025-04-06,16,315!2025-04-07,17,315-->
- `PC` ::@:: It is the 32-bit address of the current instruction \(program counter\). <!--SR:!2025-04-07,17,315!2025-04-07,17,310-->
- `h` ::@:: It can be any 5-bit unsigned constant. It is used for bit-shit instructions. <!--SR:!2025-04-07,17,315!2025-04-07,17,315-->

Common instruction variants include {@{immediate `_i`, unsigned `_u`}@}. The former {@{indicates that the instruction takes an 16-bit immediate operand in place of a register operand}@}. The latter {@{indicates that the instruction interprets the operands as unsigned integers, and additionally does not _trap_ on _overflow_}@}. Note that {@{signed integers in MIPS are always encoded using two's complement}@}. <!--SR:!2025-04-07,17,315!2025-04-07,17,310!2025-04-07,17,315!2025-04-09,18,332-->

One would notice that {@{some reasonable instructions are missing}@}. This is an example of {@{good design compromise between expressiveness and too many instructions reducing performance of all instructions}@}. <!--SR:!2025-04-01,15,290!2025-04-02,16,290-->

### operands

There are {@{3 types of operands}@} \(at least in this course\) in MIPS: {@{immediate \(constant\) operand, memory operand, and register operand}@}. Note that the first one is {@{limited to 16 bits \(see instruction encoding\)}@}, and {@{for _arithmetic_ operations \(e.g. excludes _bitwise_ operations), is always _sign-extended_}@}. <!--SR:!2025-04-07,17,315!2025-04-06,16,315!2025-04-05,15,315!2025-04-07,17,310-->

In terms of {@{execution time}@}, {@{immediate \(constant\) operands}@} are {@{the fastest as they are encoded in the instruction}@}. {@{Register operands}@} are {@{still fast since registers are inside to the processor}@}. {@{Memory operands}@} are {@{extremely slow comparatively since they are very far comparatively from the processor}@}. This is why {@{there are multiple variants of the same operation, but with one accepting immediate operands}@}. <!--SR:!2025-04-02,16,290!2025-04-02,16,290!2025-04-01,15,290!2025-04-02,16,290!2025-04-01,15,290!2025-03-31,14,290!2025-04-01,15,290!2025-03-31,14,290-->

Note that while {@{`$zero` or `$0`}@} has {@{the semantics of _constant_ zero}@}, it is {@{_not_ a constant operand but a register operand}@}. So {@{it can only be used in locations where a register operand is expected}@}. <!--SR:!2025-04-02,16,290!2025-04-01,15,290!2025-04-01,15,290!2025-03-31,14,290-->

### arithmetic instructions

- add ::@:: `add $d, $s, $t`: `$d = $s + $t;`, signed, traps on overflow <!--SR:!2025-04-07,17,315!2025-04-06,16,315-->
- add immediate ::@:: `addi $t, $s, imm`: `$t = $s + imm;`, signed, traps on overflow; `imm` is sign-extended <!--SR:!2025-04-06,16,315!2025-04-07,17,315-->
- add immediate unsigned ::@:: `addiu $t, $s, imm`: `$t = $s + imm;`, unsigned, does not trap on overflow; `imm` is sign-extended \(surprise!\) <!--SR:!2025-04-06,16,315!2025-04-06,16,315-->
  - add immediate unsigned / note ::@:: Recall that in two's complement, at a bit level, addition is the same as that for unsigned integers. Thus, for two's complement, `addiu` can be used in place of `addi` to avoid trapping on overflow. <!--SR:!2025-04-06,16,315!2025-04-05,15,315-->
- add unsigned ::@:: `addu $d, $s, $t`: `$d = $s + $t;`, unsigned, does not trap on overflow <!--SR:!2025-04-06,16,315!2025-04-07,17,315-->
  - add unsigned / note ::@:: Recall that in two's complement, at a bit level, addition is the same as that for unsigned integers. Thus, for two's complement, `addu` can be used in place of `add` to avoid trapping on overflow. <!--SR:!2025-04-01,13,295!2025-04-02,12,295-->
- divide ::@:: `div $s, $t`: `$LO = $s / $t; $HI = $s % $t;`, signed; `$LO` \(quotient\) is rounded towards zero, while `$HI` \(remainder\) is such that `$s == $t * $LO + $HI` <!--SR:!2025-04-05,15,315!2025-04-07,17,315-->
- divide immediate ::@:: `divi` does not exist. <!--SR:!2025-04-07,17,315!2025-04-07,17,315-->
- divide immediate unsigned ::@:: `diviu` does not exist. <!--SR:!2025-04-07,17,315!2025-04-07,17,315-->
- divide unsigned ::@:: `divu $s, $t`: `$LO = $s / $t; $HI = $s % $t;`, unsigned <!--SR:!2025-04-07,17,315!2025-04-05,15,315-->
  - divide unsigned / note ::@:: Unlike addition and subtraction, two's complement signed division and unsigned division are not equivalent. <!--SR:!2025-04-06,16,315!2025-04-06,16,315-->
- multiply \(lower 32 bits\) ::@:: `mul $d, $s, $t`: `$d = $s * $t`, signed, lower 32 bits; `$LO` and `$HI` may or may not be cobbled \(MARS cobbles them\); for this course, treat it as a _pseudo-instruction_ \(even though it is not\) <!-- <https://stackoverflow.com/a/52748907> --> <!--SR:!2025-04-02,11,312!2025-04-08,17,332-->
- multiply unsigned \(lower 32 bits\) ::@:: `mulu` does not exist. <!--SR:!2025-04-08,17,332!2025-04-09,18,332-->
- multiply ::@:: `mult $s, $t`: `$HI:$LO = $s * $t;`, signed <!--SR:!2025-04-07,17,315!2025-04-05,15,315-->
- multiply immediate ::@:: `multi` does not exist. <!--SR:!2025-04-06,16,315!2025-04-07,17,310-->
- multiply immediate unsigned ::@:: `multiu` does not exist. <!--SR:!2025-04-05,15,315!2025-04-05,15,315-->
- multiply unsigned ::@:: `multu $s, $t`: `$HI:$LO = $s * $t;`, unsigned <!--SR:!2025-04-06,16,315!2025-04-06,16,315-->
  - multiply unsigned / note ::@:: Unlike addition and subtraction, two's complement signed division and unsigned division are not equivalent. <!--SR:!2025-04-06,16,310!2025-04-05,15,310-->
- subtract ::@:: `sub $d, $s, $t`: `$d = $s - $t;`, signed, traps on overflow <!--SR:!2025-04-07,17,315!2025-04-06,16,315-->
- subtract immediate ::@:: `subi` does not exist. Use `addi` with a negative constant instead. <!--SR:!2025-04-07,17,315!2025-04-07,17,315-->
- subtract immediate unsigned ::@:: `subiu` does not exist. Use `addiu` with a negative constant instead. <!--SR:!2025-04-06,16,315!2025-04-06,16,315-->
- subtract unsigned ::@:: `subu $d, $s, $t`: `$d = $s - $t;`, unsigned, does not trap on overflow <!--SR:!2025-04-07,17,310!2025-04-05,15,315-->
  - subtract unsigned / note ::@:: Recall that in two's complement, at a bit level, subtraction is the same as that for unsigned integers. Thus, for two's complement, `subu` can be used in place of `sub` to avoid trapping on overflow. <!--SR:!2025-04-05,15,310!2025-04-05,15,315-->

### bitwise instructions

- bitwise and ::@:: `and $d, $s, $t`: `$d = $s & $t;` <!--SR:!2025-04-07,17,315!2025-04-06,16,315-->
- bitwise and immediate ::@:: `andi $t, $s, imm`: `$t = $s & imm;`; `imm` is zero-extended <!--SR:!2025-04-05,15,310!2025-04-07,17,310-->
- bitwise exclusive or ::@:: `xor $d, $s, $t`: `$d = $s ^ $t;` <!--SR:!2025-04-06,16,310!2025-04-07,17,310-->
- bitwise exclusive or immediate ::@:: `xori $t, $s, imm`: `$t = $s ^ imm;`; `imm` is zero-extended <!--SR:!2025-04-06,16,310!2025-04-05,15,315-->
- bitwise nor ::@:: `nor $d, $s, $t`: `$d = ~($s | $t);` <!--SR:!2025-04-05,15,315!2025-04-07,17,315-->
- bitwise nor immediate ::@:: `nori` does not exist. Unfortunately, it cannot be replaced by a single instruction. It can be replaced by `ori` and then a `nor` with `$0`. <!--SR:!2025-04-06,16,315!2025-04-07,17,310-->
- bitwise or ::@:: `or $d, $s, $t`: `$d = $s | $t;` <!--SR:!2025-04-05,15,315!2025-04-07,17,315-->
- bitwise or immediate ::@:: `ori $t, $s, imm`: `$t = $s | imm;`; `imm` is zero-extended <!--SR:!2025-04-07,17,310!2025-04-05,15,315-->
- shift left arithmetic ::@:: `sla` does not exist. It would have been equivalent to `sll`. <!--SR:!2025-04-05,15,315!2025-04-07,17,315-->
- shift left logical ::@:: `sll $d, $t, h`: `$d = $t << h;`, padded by 0 <!--SR:!2025-04-07,17,315!2025-04-02,12,295-->
- shift left logical variable ::@:: `sllv $d, $t, $s`: `$d = $t << $s;`, padded by 0; if `$s >= 32`, MIPS IV does not define it, while MIPS32 takes the lower 5 bits <!--SR:!2025-04-07,17,315!2025-04-06,16,315-->
- shift right arithmetic ::@:: `sra $d, $t, h`: `$d = $t >> h;`, sign-extended <!--SR:!2025-04-05,15,310!2025-04-05,15,310-->
- shift right arithmetic variable ::@:: `srav $d, $t, h`: `$d = $t >> h;`, sign-extended; if `$s >= 32`, MIPS IV does not define it, while MIPS32 takes the lower 5 bits <!--SR:!2025-04-09,18,332!2025-04-02,11,312-->
- shift right logical ::@:: `srl $d, $t, h`: `$d = $t >> h;`, padded by 0 <!--SR:!2025-04-07,17,310!2025-04-07,17,310-->
- shift right logical variable ::@:: `srlv $d, $t, $s`: `$d = $t >> $s;`, padded by 0; if `$s >= 32`, MIPS IV does not define it, while MIPS32 takes the lower 5 bits <!--SR:!2025-04-06,16,310!2025-04-01,11,295-->

### data instructions

- load byte ::@:: `lb $t, offset($s)`: `$t = *((*int8_t) &MEM[$s + offset]);`; the loaded 8 bits are sign-extended <!--SR:!2025-04-06,16,315!2025-04-05,15,315-->
- load byte unsigned ::@:: `lbu $t, offset($s)`: `$t = *((*uint8_t) &MEM[$s + offset]);`; the loaded 8 bits are zero-extended <!--SR:!2025-04-07,17,315!2025-04-07,17,310-->
- load upper immediate ::2:: `lui $t, imm`: `$t = imm << 16;`; `imm` is unextended; note the lower 16 bits are 0s
- load halfword ::@:: `lh $t, offset($s)`: `$t = *((*int16_t) &MEM[$s + offset]);`; the loaded 16 bits are sign-extended <!--SR:!2025-04-07,17,315!2025-04-05,15,315-->
- load halfword unsigned ::@:: `lhu $t, offset($s)`: `$t = *((*uint16_t) &MEM[$s + offset]);`; the loaded 16 bits are zero-extended <!--SR:!2025-04-07,17,310!2025-04-06,16,315-->
- load word ::@:: `lw $t, offset($s)`: `$t = *((*uint32_t) (&MEM[$s + offset]));` <!--SR:!2025-04-07,17,315!2025-04-05,15,315-->
- move from HI ::@:: `mfhi $d`: `$d = $HI;`; note the register placeholder is `$d` instead of `$s` <!--SR:!2025-04-05,15,315!2025-04-07,17,315-->
- move from LO ::2:: `mflo $d`: `$d = $LO;`; note the register placeholder is `$d` instead of `$s`
- store byte ::@:: `sb $t, offset($s)`: `*((*uint8_t) (&MEM[$s + offset])) = 0xff & $t;` <!--SR:!2025-04-07,17,310!2025-04-07,17,310-->
- store halfword ::@:: `sh $t, offset($s)`: `*((*uint16_t) (&MEM[$s + offset])) = 0xffff & $t;` <!--SR:!2025-04-06,16,315!2025-04-07,17,310-->
- store word ::@:: `sw $t, offset($s)`: `*((*uint32_t) (&MEM[$s + offset])) = $t;` <!--SR:!2025-04-06,16,310!2025-04-07,17,315-->

### jump instructions

- branch on equal ::@:: `beq $s, $t, offset`: `if ($s == $t) { goto PC + offset << 2; }` <!--SR:!2025-04-05,15,315!2025-04-07,17,315-->
- branch on greater than or equal to zero ::@:: `bgez $s, offset`: `if ($s >= 0) { goto PC + offset << 2; }` <!--SR:!2025-04-06,16,315!2025-04-06,16,315-->
- branch on greater than or equal to zero and link ::@:: `bgezal $s, offset`: `if ($s >= 0) { $ra = PC + 8; goto PC + offset << 2; }` \(`PC + 8` instead of `PC + 4` is due to a branch delay slot; for MARS and this course, ignore this and treat it as the next instruction: `PC + 4`\) <!--SR:!2025-04-07,17,310!2025-04-06,16,315-->
- branch on greater than zero ::@:: `bgtz $s, offset`: `if ($s > 0) { goto PC + offset << 2; }` <!--SR:!2025-04-06,16,310!2025-04-07,17,315-->
- branch on greater than zero and link ::@:: `bgtzal` does not exist. For reasons unmentioned, only `bgezal` \(≥\) and `bltzal` \(<\) exist. <!--SR:!2025-04-06,16,315!2025-04-07,17,315-->
- branch on less than or equal to zero ::@:: `blez $s, offset`: `if ($s <= 0) { goto PC + offset << 2; }` <!--SR:!2025-04-07,17,310!2025-04-05,15,310-->
- branch on less than or equal to zero and link ::@:: `blezal` does not exist. For reasons unmentioned here, only `bgezal` \(≥\) and `bltzal` \(<\) exist. <!--SR:!2025-04-05,15,315!2025-04-07,17,315-->
- branch on less than zero ::@:: `bltz $s, offset`: `if ($s < 0) { goto PC + offset << 2; }` <!--SR:!2025-04-06,16,315!2025-04-05,15,315-->
- branch on less than zero and link ::@:: `bltzal $s, offset`: `if ($s < 0) { goto offset $ra = PC + 8; goto PC + offset << 2; }` \(`PC + 8` instead of `PC + 4` is due to a branch delay slot; for MARS and this course, ignore this and treat it as the next instruction: `PC + 4`\) <!--SR:!2025-04-07,17,315!2025-04-05,15,310-->
- branch on not equal ::@:: `bne $s, $t, offset`: `if ($s != $t) { goto PC + offset << 2; }` <!--SR:!2025-04-06,16,310!2025-04-06,16,310-->
- jump ::@:: `j target`: `goto (PC & 0xf0000000) | (target << 2);` <!--SR:!2025-04-07,17,315!2025-04-06,16,315-->
- jump and link ::@:: `jal target`: `$ra = PC + 8; goto (PC & 0xf0000000) | (target << 2);` \(`PC + 8` instead of `PC + 4` is due to a branch delay slot; for MARS and this course, ignore this and treat it as the next instruction: `PC + 4`\) <!--SR:!2025-04-05,15,315!2025-04-05,15,315-->
- jump register ::@:: `jr $s`: `goto $s;` <!--SR:!2025-04-06,16,315!2025-04-05,15,315-->

### comparison instructions

- set on less than ::@:: `slt $d, $s, $t`: `$d = $s < $t;`, signed <!--SR:!2025-04-06,16,315!2025-04-07,17,315-->
- set on less than immediate ::@:: `slti $t, $s, imm`: `$t = $s < imm;`, signed; `imm` is sign-extended <!--SR:!2025-04-06,16,315!2025-04-05,15,315-->
- set on less than immediate unsigned ::@:: `sltiu $t, $s, imm`: `$t = $s < imm;`, unsigned; `imm` is sign-extended \(surprise!\) <!--SR:!2025-04-01,11,290!2025-04-06,16,315-->
- set on less than unsigned ::@:: `sltu $d, $s, $t`: `$d = $s < $t;`, unsigned <!--SR:!2025-04-07,17,310!2025-04-06,16,310-->

### miscellaneous instructions

- no operation ::@:: `noop`: does nothing; encoded by all 0s, which represents `sll $0, $0, 0` \(in fact, _almost all_ instruction that has `$0` as its destination register does nothing\) <!--SR:!2025-04-06,16,310!2025-04-07,17,315-->
- syscall ::@:: `syscall`: generates a software interrupt <!--SR:!2025-04-07,17,315!2025-04-05,15,310-->

### encoding

All instructions are {@{4 bytes \(32 bits\) long}@}. This is an example of {@{the principle regularity}@}. There are {@{3 formats: R format \(for R instructions\), I format \(for I instructions\), and J format \(for J instructions)}@}. Multiple formats {@{increases hardware complexity, but the formats are kept similar to try to reduce this}@}. Below, the format fields {@{start from higher bits to lower bits}@}. <!--SR:!2025-04-07,17,315!2025-04-06,16,315!2025-04-05,15,315!2025-04-05,15,315!2025-04-05,15,315-->

- R format ::@:: all operands are registers \(ignoring the "immediate" operand in bit-shift instructions\) without offsets <p> opcode: 6 bits → rs: 5 bits → rt: 5 bits → rd: 5 bits → shift \(shamt\): 5 bits → funct: 6 bits <!--SR:!2025-04-06,16,315!2025-04-05,15,315-->
- I format ::@:: one operand is immediate \(the "immediate" operand in bit-shift instructions is not really immediate\) or an offset is present <p> opcode: 6 bits → rs: 5 bits → rt: 5 bits → imm: 16 bits <!--SR:!2025-04-05,15,310!2025-04-05,15,315-->
- J format ::@:: the only operand is an pseudo-address <p> opcode: 6 bits → pseudo-address: 26 bits <!--SR:!2025-04-07,17,315!2025-04-05,15,315-->

The format fields include {@{opcode, rs, rt, rd, shift \(shamt\), funct, imm, and pseudo-address}@}. They mean: <!--SR:!2025-04-07,17,315-->

- opcode ::@:: 6 bits; opcode of the instruction; R format: this is almost always 0, since the funct field is used instead <!--SR:!2025-04-07,17,315!2025-04-05,15,315-->
- rs ::@:: 5 bits; R format: first source register operand; I format: source or memory register operand <!--SR:!2025-04-02,12,295!2025-04-06,16,315-->
- rt ::@:: 5 bits; R format: second source register operand; I format: destination or non-memory register operand <!--SR:!2025-04-07,17,310!2025-04-07,17,315-->
- rd ::@:: 5 bits; R format: destination register operand <!--SR:!2025-04-06,16,310!2025-04-07,17,310-->
- shift \(shamt\) ::@:: 5 bits; R format: number of bits to shift, ranging from 0 to 31 \(i.e. unsigned\), and should almost always be 0 for non-bit-shift instructions <!--SR:!2025-04-07,17,310!2025-04-01,13,295-->
- funct ::@:: 6 bits; R format: opcode of the instruction, and is almost always used instead of the opcode field <!--SR:!2025-04-06,16,310!2025-04-05,15,310-->
- imm ::@:: 16 bits; I format: a 16-bit immediate constant that may be unextended, sign-extended, or zero-extended depending on the instruction, a signed 16-bit offset, or an address or label representable by a signed 16-bit 4-byte offset \(effectively 18 bits\) from the current instruction <!--SR:!2025-04-06,16,315!2025-04-06,16,315-->
- pseudo-address ::@:: 26 bits; J format: a 26-bit unsigned constant, representing an address or label that has its upper 4 bits same as the current instruction \(the lower 28 bits can be different, and the lower 2 bits must be 0\) <!--SR:!2025-04-07,17,315!2025-04-07,17,315-->

The register fields are encoded {@{by the named registers' corresponding number name}@}. <!--SR:!2025-04-05,15,310-->

For {@{bit-shift instructions}@}, note that {@{unlike other instructions, for variable bit-shift instructions, `$s` \(the rs field\) is on the right hand side instead of the left hand side, and `$t` \(the rt field\) is on the left hand side instead of the right hand side}@}. Also, {@{for "immediate" bit-shift instructions, `$s` \(the rs field\) is unused}@}. For {@{instructions taking a single register operand only}@}, {@{`$s` is usually used, and `$d` \(R format\) or `$t` \(I format\) is used if the register is to be written \(e.g. `lui`, `mfhi`, `mflo`\)}@}. <!--SR:!2025-04-08,17,332!2025-04-09,18,332!2025-04-09,18,332!2025-04-08,17,332!2025-04-09,18,332-->

Notice that {@{some fields are unused}@}. Sometimes, {@{they can be any value \(and we would not care\), but sometimes not}@}, so it is {@{best to always set unused fields to all 0s \(unless otherwise specified\)}@}. <!--SR:!2025-04-06,16,315!2025-04-07,17,315!2025-04-08,17,332-->

## calling conventions

There are {@{two _major_ calling conventions}@} for MIPS: {@{O32, N32/N64}@}. We will {@{use O32}@} for this course. <!--SR:!2025-04-01,15,290!2025-04-01,15,290!2025-04-01,15,290-->

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
> - register blocks ::@:: `$zero` <br/> `$at` <br/> `$v0`–`$v1` \(2\) <br/> `$a0`–`$a3` \(4\) <br/> `$t0`–`$t7` \(8\) <br/> `$s0`–`$s7` \(8\) <br/> `$t8`–`$t9` \(2\) <br/> `$k0`–`$k1` \(2\) <br/> `$gp` <br/> `$sp` <br/> `$fp` <br/> `$ra` <!--SR:!2025-03-29,12,270!2025-04-01,15,290-->
>   - register blocks / semantics ::@:: zero → asm temp → expr eval & fun ret ×2 → fun arg ×4 → temp ×8 → saved temp ×8 → temp ×2 → kernel ×2 → global ptr → stack ptr → frame \(base\) ptr → return addr <!--SR:!2025-04-02,16,290!2025-04-02,16,290-->
> - __`$zero`__ ::@:: `$0`: constant 0 <!--SR:!2025-04-02,16,290!2025-04-02,16,290-->
> - __`$at`__ ::@:: `$1`: assembler temporary <!--SR:!2025-04-02,16,290!2025-04-01,15,290-->
> - __`$v0`–`$v1`__ ::@:: `$2`–`$3`: values for function returns and expression evaluation <!--SR:!2025-04-02,16,290!2025-04-01,15,290-->
> - __`$a0`–`$a3`__ ::@:: `$4`–`$7`: function arguments <!--SR:!2025-04-01,15,290!2025-04-02,16,290-->
> - __`$t0`–`$t7`__ ::@:: `$8`–`$15`: temporaries <!--SR:!2025-03-31,14,290!2025-04-01,15,290-->
> - __`$s0`–`$s7`__ ::@:: `$16`–`$23`: saved temporaries <!--SR:!2025-04-02,16,290!2025-04-01,15,290-->
> - __`$t8`–`$t9`__ ::@:: `$24`–`$25`: temporaries <!--SR:!2025-04-01,15,290!2025-04-02,16,290-->
> - __`$k0`–`$k1`__ ::@:: `$26`–`$27`: reserved for OS kernel <!--SR:!2025-04-01,15,290!2025-04-01,15,290-->
> - __`$gp`__ ::@:: `$28`: global pointer <!--SR:!2025-03-31,14,290!2025-04-02,16,290-->
> - __`$sp`__ ::@:: `$29`: [stack pointer](../../../../general/stack-based%20memory%20allocation.md) <!--SR:!2025-03-31,14,290!2025-04-01,15,290-->
> - __`$fp`__ ::@:: `$30`: [frame pointer](../../../../general/frame%20pointer.md#FRAME-POINTER) <!--SR:!2025-04-02,16,290!2025-04-02,16,290-->
> - __`$ra`__ ::@:: `$31`: [return address](../../../../general/return%20statement.md) <!--SR:!2025-03-31,14,290!2025-04-02,16,290-->
> - callee-saved register blocks ::@:: saved temp, global ptr \(except PIC code\), stack ptr, frame \(base\) ptr <br/> in this course: return addr <!--SR:!2025-04-01,15,290!2025-03-29,12,270-->
> - caller-saved register blocks ::@:: asm temp, expr eval & fun ret, fun arg, temp <!--SR:!2025-04-02,16,290!2025-05-10,43,290-->

## assembly

{@{The assembler}@} is {@{responsible for translating human-readable assembly to machine-readable machine code}@}. That means we need to {@{learn how to write the human-readable assembly file}@}. <!--SR:!2025-04-02,16,290!2025-04-02,16,290!2025-04-01,15,290-->

### assembly format

Comments {@{start with `#` and end with a newline}@}. {@{Labels}@} are {@{like "bookmarks" of the program}@}, so that {@{you can reference the "bookmark" from other assembly lines by its name}@}. Its syntax is {@{`(label name): (code)`}@}. To {@{load the address of a label into a register}@}, use {@{the _pseudo-instruction_ `la $reg, (label name)` \(load address\)}@}. To {@{specify a location to jump to in an instruction}@}, {@{simply use the label name}@}. <!--SR:!2025-03-31,14,290!2025-03-31,14,290!2025-04-01,15,290!2025-04-02,16,290!2025-04-01,15,290!2025-04-02,16,290!2025-03-31,14,290!2025-03-31,14,290!2025-04-01,15,290-->

In a program, you usually {@{have 2 segments: `.data` and `.text`}@}. To begin such a segment, {@{simply start it with the segment header `.(segment name)` in its own line}@}. Then, {@{all text after this line and before the next segment header}@} belongs to that segment. In {@{the `.data` segment}@}, you {@{put data inside}@}. You can {@{modify the data while executing the program using the instruction `sw`}@}. In {@{the `.text` segment}@}, you {@{put runnable code inside \(the name "text" is quite un-descriptive, but this is historical convention...\)}@}. <!--SR:!2025-04-01,15,290!2025-04-02,16,290!2025-04-02,16,290!2025-04-02,16,290!2025-04-01,15,290!2025-03-31,14,290!2025-03-31,14,290!2025-03-31,14,290-->

In the `.data` segment, {@{data are stored into the memory _contagiously_ in declaration order}@}. The first byte of data {@{may have an arbitrary memory address, called _offset_}@}, and {@{later bytes are stored contagiously \(sometimes with small padding between different data for _alignment_\) after the first byte}@}. <!--SR:!2025-04-01,15,290!2025-04-02,16,290!2025-04-02,16,290-->

{@{The above "instructions" starting with a period `.`}@} are {@{more properly called _assembler directives_}@}. They include directives that {@{specify alignment, data, strings, symbol visibility, etc.}@} They are {@{not actual MIPS instructions}@} since {@{they are processed by the assembler during assembly rather than run during program execution}@}. <!--SR:!2025-03-31,14,290!2025-04-02,16,290!2025-04-01,15,290!2025-04-02,16,290!2025-03-31,14,290-->

### assembly directives

- `.align <n>` ::@:: _Align_ the _next_ datum on a 2<sup>_n_</sup>-byte boundary. That is, the next datum starts at an address that is a multiple of 2<sup>_n_</sup>. <p> If _n_ is 0, automatic _alignment_ is turned off, since 2<sup>0</sup> = 1, which is effectively no alignment. <!--SR:!2025-04-01,15,290!2025-03-31,14,290-->
- `.ascii <str>` ::@:: Stores a non-null-terminated \(ASCII\) string. <!--SR:!2025-04-02,16,290!2025-04-01,15,290-->
- `.asciiz <str>` ::@:: Stores a null-terminated \(ASCII\) string. <!--SR:!2025-04-01,15,290!2025-04-02,16,290-->
- `.byte <b1>, ..., <bn>` ::@:: Stores the specified _n_ bytes \(8 bits\). <!--SR:!2025-04-02,16,290!2025-04-02,16,290-->
- `.data` ::@:: Starts the data segment. <!--SR:!2025-03-31,14,290!2025-03-31,14,290-->
- `.double <d1>, ..., <dn>` ::@:: Stores the specified _n_ doubles \(64 bits, 8 bytes\). <!--SR:!2025-03-31,14,290!2025-04-02,16,290-->
- `.float <f1>, ..., <fn>` ::@:: Stores the specified _n_ floats \(32 bits, 4 bytes\). <!--SR:!2025-04-02,16,290!2025-04-02,16,290-->
- `.globl <sym>` ::@:: \(The name is _not_ a typo!\) Declare the symbol `<sym>` is global. The symbol is not removed from the resulting object/program file. That is, other assembly files can reference it. This is also required for the entry point label, so that the OS knows where to start the program. <!--SR:!2025-03-31,14,290!2025-04-02,16,290-->
- `.half <h1>, ..., <hn>` ::@:: Stores the specified _n_ half-words \(16 bits, 2 bytes\). <!--SR:!2025-04-01,15,290!2025-04-01,15,290-->
- `.text [<addr>]` ::@:: Starts the code \(text\) segment, starting at the \(optional\) address `<addr>`. <!--SR:!2025-04-02,16,290!2025-04-01,15,290-->
- `.word <w1>, ..., <wn>` ::@:: Stores the specified _n_ words \(32 bits, 4 bytes\). <!--SR:!2025-04-02,16,290!2025-04-01,15,290-->

### entry point

The convention is {@{the entry point \(first instruction to be executed when a program starts\) is labeled by the label `.__start`}@}. Additionally, {@{the label needs to be global, specified using `.globl __start`}@}. For example, a way to start a program is: <p> {@{<pre>.text<br/>.globl \_\_start<br/>\_\_start:<br/># your instructions here</pre>}@}. <!--SR:!2025-03-31,14,290!2025-03-31,14,290!2025-04-01,15,290-->

## control flow

In {@{higher level programming languages}@}, we have {@{`do-while`, `if`, `for`, `while`, etc. for control flow}@}. In MIPS, we have {@{`beq` (branch if equal), `bne` (branch if not equal), and `j` (jump) for control flow}@}. These, {@{coupled with comparison instructions \(introduced below\)}@}, can {@{support implementing all conventional control flow structures in higher level programming languages}@}, and additionally {@{allows for unconventional \(less readable\) control flow}@}. <!--SR:!2025-04-01,15,290!2025-04-02,16,290!2025-04-01,15,290!2025-03-31,14,290!2025-03-31,14,290!2025-04-01,15,290-->

To {@{convert structured control flow statements into assembly}@} manually, {@{identify _basic blocks_, which is a sequence of consecutive code that has no branching _to_ and _from_ other code}@}. Then, {@{a control flow graph can be constructed out of these basic blocks}@}. Finally, {@{_label_ the basic blocks at their beginnings and add conditional and/or unconditional jumps at their endings}@} to {@{model the control flow graph}@}. \(this course: Include {@{the beginning label and the ending conditional and/or unconditional jumps}@} in a basic block.\) {@{A compiler}@} {@{essentially does the same thing automatically}@}, and {@{with additional optimizations \(e.g. reordering\) for performance and/or code size}@}. Also, during program execution, {@{an advanced processor}@} may {@{identify instructions that form basic blocks and accelerate them}@}. <!--SR:!2025-04-02,16,290!2025-03-31,14,290!2025-04-02,16,290!2025-04-01,15,290!2025-04-02,16,290!2025-04-02,16,290!2025-03-31,14,290!2025-04-01,15,290!2025-04-01,15,290!2025-04-02,16,290!2025-03-31,14,290-->

To convert {@{an `if...else if...else` statement}@}, a common pattern is {@{a bunch of comparison and conditional jumps to the basic blocks, then the basic blocks each ending with a jump to the exit label, and finally the exit label at the end}@}. To convert {@{an `while` statement}@}, a common pattern is {@{a loop label, then comparison and conditional jump to the exit label, the code, and finally a jump to the loop label}@}. You can extrapolate the rest for yourself. You may also simplify the code. <!--SR:!2025-04-02,16,290!2025-04-02,16,290!2025-04-01,15,290!2025-04-01,15,290-->

## pseudo-instructions

Since {@{MIPS have few instructions}@}, some common code {@{requires multiple instructions}@}. Pseudo-instructions are {@{_assembler macros_ that help replace these multiple instructions with a single line}@}. Since {@{these instructions are not real}@}, they are {@{replaced by multiple instructions implementing the pseudo-instruction during assembly}@}, and thus {@{does not appear in the resulting program file}@}. <!--SR:!2025-04-06,16,315!2025-04-07,17,310!2025-04-05,15,315!2025-04-06,16,310!2025-04-05,15,315!2025-04-06,16,310-->

- load address ::@:: `la $d, addr`; `$d = &addr;`, but `addr` is an address or label; implemented by `lui $at, 0x1001; ori $d, $at, addr[0:16];` <!--SR:!2025-04-05,15,315!2025-04-05,15,310-->
- load immediate ::@:: `li $d, imm`: `$d = imm;`, but `imm` is a 32-bit unsigned integer; implemented by `lui $at, imm[16:32]; ori $d, $at, imm[0:16];` <!--SR:!2025-04-05,15,310!2025-04-07,17,310-->
- not ::@:: `not $d, $s`: `$d = ~$s`; implemented by `nor $d, $zero, $s;` <!--SR:!2025-05-01,34,295!2025-04-07,17,315-->

Note that some pseudo-instructions have {@{the same name as some of the _real_ instructions}@}. Whether the instruction or the pseudo-instruction is {@{used depends on the operands}@}. For example, {@{the load word `lw` instruction}@} has {@{several related pseudo-instructions of the same name that does the same thing}@} but {@{for operands not following the format `lw $t, $s(offset)`}@}, which are provided for {@{convenience, e.g. loading data addressed by a label (`lw $t, label`), etc.}@}. <!--SR:!2025-03-29,4,323!2025-03-29,4,323!2025-03-29,4,323!2025-03-29,4,323!2025-03-29,4,323!2025-03-29,4,323-->

\(this course: Some questions may {@{require you to not use any pseudo-instructions}@}.\) <!--SR:!2025-04-07,17,315-->
