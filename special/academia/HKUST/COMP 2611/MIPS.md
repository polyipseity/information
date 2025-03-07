---
aliases:
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

- good compromises
- make common cases fast ::@:: Variants of instructions that accept _immediate_ operands instead of register or memory operands are available.
- simplicity favors regularity \(less cases\) ::@:: Each instruction has a fixed number of operands. It makes CPU implementations simpler and allows better performance.
  - simplicity favors regularity / comparison ::@:: x86, a _complex_ instruction set computer \(CISC\) ISA, supports a variable number of operands.
- smaller is faster ::@:: Less registers means faster processors. More registers means more propagation delay \(longer travel time\).

## registers

Registers are {@{_fast_ temporary storage _inside_ the processor \(not on the main memory \(RAM\)\) used to hold _data_}@}. There is {@{a limited number}@} of registers.

Variables differ from registers in that {@{the former is a logical concept while the latter is a physical thing}@}. Thus, there can be {@{an unlimited number of variables}@}.

In MIPS, there are {@{32 registers}@}. They can be identified by {@{their names (depends on the _calling convention_) or their numbers \(from `$0` to `$31`\)}@}. They can hold {@{a _word_, which is 32 bits in size}@}. Commonly used registers include: {@{the readonly zero register `$zero` \(`$0`\), saved temporary registers `$s0`–`$s7` \(`$16`–`$23`\), \(non-saved\) temporary registers `$t0`–`$t7` \(`$8`–`$15`\), etc.}@}

Almost always, {@{the number of variables in a program is much higher than the number of registers}@}. To {@{store those data}@}, {@{register values are transferred from and to the main memory, but with more propagation delay}@}.

The number of registers {@{is a balancing act: it should not be too few or too many}@}. If there are too few, {@{the potentially many variables need to be frequently transferred from and to the main memory \(RAM\), leading to performance loss}@}. If there are too many, {@{processors are more complicated, have higher clock cycle time, which also leads to performance loss}@}.

## main memory

The main memory is usually {@{a physical RAM}@}. It can {@{store much data, much more than the registers}@}.

In MIPS, {@{the main memory cannot be manipulated directly}@}. Instead, {@{values need to be transferred from _registers_ to the main memory, and vice versa}@}.

We can treat the main memory as {@{a _contagious_ storage locations}@}. Each storage location {@{stores a byte, which has a size of 8 bits}@}. The storage location are addressed by {@{indices starting from 0}@}. Usually, addresses are {@{written using hexadecimal}@}.

In MIPS, to address a memory location, we need {@{a base address and an offset}@}. The base address is {@{provided by a register, while the offset is provided by a constant}@}. The actual address is {@{simply the sum of the base address and the offset}@}. Often, the base address is {@{the starting address of an array}@}, while the offset is {@{an array index _multiplied_ by the array element size}@}. {@{The _memory operand_ syntax}@} is {@{`$offset($base)`, e.g. `-4($s0)`}@}.

### endianness

When {@{addressing multiple bytes}@}, it is important to {@{take note of _endianness_: _big endian_ and _little endian_}@}. {@{A _big-endian_ system}@} stores {@{the most significant byte of a word at the smallest memory address and the least significant byte \(word _end_\) at the largest}@}. {@{A _little-endian_ system}@} stores {@{the least-significant byte \(word _end_\) at the smallest address}@}. It also describes {@{the order of byte transmission over a digital link}@}.

## instructions

Each instruction is written as {@{`ins op_1, op_2, ..., op_n`, where `ins` is the instruction and `op_i` are its operands}@}. Each line {@{contain at most one instruction}@}. Comments {@{start with `#` and end with a newline}@}.

Below, the accompanying code to the right is {@{a piece of pseudo C code showing its semantics}@}. For placeholders: `$s_` can be {@{any register}@}. `$imm_` can be {@{any constant}@}.

### operands

There are {@{3 types of operands}@} \(at least in this course\) in MIPS: {@{immediate \(constant\) operand, memory operand, and register operand}@}.

In terms of {@{execution time}@}, {@{immediate \(constant\) operands}@} are {@{the fastest as they are encoded in the instruction}@}. {@{Register operands}@} are {@{still fast since registers are inside to the processor}@}. {@{Memory operands}@} are {@{extremely slow comparatively since they are very far comparatively from the processor}@}. This is why {@{there are multiple variants of the same operation, but with one accepting immediate operands}@}.

Note that while {@{`$zero` or `$0`}@} has {@{a semantic of _constant_ zero}@}, it is {@{_not_ a constant operand but a register operand}@}. So {@{it can only be used in locations where a register operand is expected}@}.

### arithmetic

- add ::@:: `add $s0, $s1, $s2`: `$s0 = $s1 + $s2`
- add immediate ::@:: `addi $s0, $s1, $imm0`: `$s0 = $s1 - $imm0`
- subtract ::@:: `sub $s0, $s1, $s2`: `$s0 = $s1 - $s2`
- subtract immediate ::@:: This does not exist. Use `addi` with a negative constant instead.

### logical

- logical and ::@:: `and $s0, $s1, $s2`: `$s0 = $s1 & $s2`
- logical and immediate ::@:: `andi $s0, $s1, $imm0`: `$s0 = $s1 & $imm0`
- logical nor ::@:: `nor $s0, $s1, $s2`: `$s0 = ~($s1 | $s2)`
- logical nor immediate ::@:: This does not exist. Unfortunately, it cannot be directly replaced with `ori`.
- logical or ::@:: `or $s0, $s1, $s2`: `$s0 = $s1 | $s2`
- logical or immediate ::@:: `ori $s0, $s1, $imm0`: `$s0 = $s1 | $imm0`
- shift left logical ::@:: `sll $s0, $s1, $imm0`: `$s0 = $s1 << $imm0`, padded by 0
- shift right logical ::@:: `srl $s0, $s1, $imm0`: `$s0 = $s1 >> $imm0`, padded by 0

### data transfer

- load word ::@:: `lw $s0, $imm0($s1)`: `$s0 = mem[$s1 + $imm0]`
- store word ::@:: `sw $s0, $imm0($s1)`: `mem[$s1 + $imm0] = $s0`

## calling conventions

There are {@{two _major_ calling conventions}@} for MIPS: {@{O32, N32/N64}@}. We will {@{use O32}@} for this course.

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
> - register blocks ::@:: `$zero` <br/> `$at` <br/> `$v0`–`$v1` \(2\) <br/> `$a0`–`$a3` \(4\) <br/> `$t0`–`$t7` \(8\) <br/> `$s0`–`$s7` \(8\) <br/> `$t8`–`$t9` \(2\) <br/> `$k0`–`$k1` \(2\) <br/> `$gp` <br/> `$sp` <br/> `$fp` <br/> `$ra`
>   - register blocks / semantics ::@:: zero → asm temp → expr eval & fun ret ×2 → fun arg ×4 → temp ×8 → saved temp ×8 → temp ×2 → kernel ×2 → global ptr → stack ptr → frame \(base\) ptr → return adr
> - __`$zero`__ ::@:: `$0`: constant 0
> - __`$at`__ ::@:: `$1`: assembler temporary
> - __`$v0`–`$v1`__ ::@:: `$2`–`$3`: values for function returns and expression evaluation
> - __`$a0`–`$a3`__ ::@:: `$4`–`$7`: function arguments
> - __`$t0`–`$t7`__ ::@:: `$8`–`$15`: temporaries
> - __`$s0`–`$s7`__ ::@:: `$16`–`$23`: saved temporaries
> - __`$t8`–`$t9`__ ::@:: `$24`–`$25`: temporaries
> - __`$k0`–`$k1`__ ::@:: `$26`–`$27`: reserved for OS kernel
> - __`$gp`__ ::@:: `$28`: global pointer
> - __`$sp`__ ::@:: `$29`: [stack pointer](../../../../general/stack-based%20memory%20allocation.md)
> - __`$fp`__ ::@:: `$30`: [frame pointer](../../../../general/frame%20pointer.md#FRAME-POINTER)
> - __`$ra`__ ::@:: `$31`: [return address](../../../../general/return%20statement.md)
> - callee-saved register blocks ::@:: saved temp, global ptr \(except PIC code\), stack ptr, frame \(base\) ptr <br/> in this course: return addr
> - caller-saved register blocks ::@:: asm temp, expr eval & fun ret, fun arg, temp
