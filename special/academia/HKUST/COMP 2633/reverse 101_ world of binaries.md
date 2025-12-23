---
aliases:
  - Rev 101
  - "Rev 101: World of Binaries"
  - Reverse 101
  - "Reverse 101: World of Binaries"
  - rev 101
  - "rev 101: world of binaries"
  - reverse 101
  - "reverse 101: world of binaries"
  - world of binaries
tags:
  - flashcard/active/special/academia/HKUST/COMP_2633/reverse_101__world_of_binaries
  - language/in/English
---

# reverse 101: world of binaries

Why do reverse engineering, apart from CTFs? ::@:: You can analyze malware, ensuring interoperability with closed-source programs, or find vulnerabilities in them. What they have in common is that the program source is not readily available. <!--SR:!2030-03-12,1607,385!2027-11-07,889,343-->

## compiling a program

Assuming {@{you are using Linux}@}. For developers, {@{compiling a C program}@} is {@{simply running the GNU Compiler Collection \(gcc\)}@} using {@{the command `gcc <input>.c -o <output>` in a terminal}@}, which {@{compiles the C code in `<input>.c` into a program called `<output>`}@}. <!--SR:!2028-03-28,945,345!2026-02-27,148,413!2026-02-20,142,413!2026-02-24,145,413!2026-02-26,147,413-->

However, we can go further than this. The program `<output>` is {@{actually a format called an _Executable and Linkable Format_ (ELF) file}@}. The property we can about here is that {@{you can execute it, as evident from the "executable" in its name}@}. Details will be mentioned in later lectures. <!--SR:!2026-01-15,394,365!2030-10-21,1787,385-->

Instead, we are more interested in {@{the compilation process itself}@}. We like to think of {@{compilation as a single process}@}, but it is {@{really composed of several steps}@}: {@{preprocessing \(`-E`\), then compilation \(`-S`\)}@}, then {@{assembly \(`-c`\), and finally linking \(none\)}@}. <!--SR:!2025-12-28,380,365!2028-11-23,1121,343!2026-04-23,144,418!2026-04-25,146,418!2026-04-24,145,418-->

Preprocessing {@{transforms source program (text) into modified source program (still text)}@}. GCC internally {@{uses the program `cpp`, which we can use by itself}@}, for this step. To only run this step with GCC, the command is {@{`gcc -E <input>.c > <output>.i`, which writes to `<output>.i`}@}. <!--SR:!2025-12-22,374,365!2028-11-26,1212,365!2026-05-09,415,303-->

Compilation {@{transforms modified source program (text) into assembly program (still text)}@}. GCC internally {@{uses the program `cc1`, part of the GCC}@}, for this step. To only run this step, the command is {@{`gcc -S <input>.i`, which outputs a `.s` file}@}. <!--SR:!2029-05-13,1357,377!2029-03-12,1296,363!2029-06-26,1302,323-->

Assembly {@{transforms assembly program (text) into relocatable object (binary)}@}. GCC internally {@{uses the program `as`, which we can use by itself}@}, for this step. To only run this step, the command is {@{`gcc -c <input>.s`, which outputs a `.o` file}@}. <!--SR:!2030-01-01,1529,363!2028-08-21,1123,350!2028-05-22,1044,357-->

Linking {@{transforms relocatable object (binary) into an ELF file (binary)}@}, which is the final product we want. GCC internally {@{uses the program `ld`, which we can use by itself}@}, for this step. To only run this step, the command is {@{`gcc <input>.o -o <output>`, which outputs the ELF file as `<output>`}@}. <!--SR:!2027-08-14,828,343!2026-02-18,421,365!2031-01-13,1853,385-->

It is okay that one does not understand everything above. The most important part is that {@{a source file is transformed into assembly program, which is finally transformed into the ELF file}@}. {@{Reversing the ELF file into the assembly program}@} is easy as {@{assembly has a mostly direct correspondence with instructions in the ELF file}@}, but {@{reversing the assembly program into the original source program}@} is difficult as {@{language constructs can be compiled into assembly in a multitude of ways, losing information in the process}@}. Reversing is somewhat about the latter, but more accurately is about {@{understanding the program behavior from the assembly without the source program}@}. And to do so, we need to {@{learn assembly}@}. <!--SR:!2029-05-20,1350,363!2030-06-17,1676,377!2028-04-22,1028,350!2028-11-08,1194,363!2030-02-07,1573,377!2030-09-17,1759,385!2029-06-29,1395,377-->

## assembly language

Assembly is {@{not a single language}@}. Rather, there are {@{multiple languages, called _instruction set architecture_ (ISA)}@}. The most common ones are {@{x86 and x86-64}@}, which we will focus on. Other examples include {@{ARM32, ARM64, RISC-V, Power ISA, and MIPS}@}. <!--SR:!2026-01-18,396,363!2027-07-03,794,343!2030-11-03,1797,385!2029-12-19,1520,363-->

### registers

Registers {@{hold data of fixed small sizes}@}. x86, a {@{32-bit}@} architecture, has {@{8 general-purpose 32-bit registers, named `eax`, `ecx`, `edx`, `ebx`, `esp`, `ebp`, `esi`, and `edi`}@}. x86-64, a {@{64-bit}@} architecture, introduces {@{8 additional general-purpose 64-bit registers, named `r8`, `r9`, `r10`, `r11`, `r12`, `r13`, `r14`, and `r15`}@}, and upgrades {@{the old 8 general-purpose 32-bit registers to 64-bit and changing the starting `e` to `r`}@}. There is also {@{a special 32-bit or 64-bit register named `eip` (32-bit) or `rip` (64-bit)}@}, which {@{points to the current instruction being executed}@}. Unlike other registers, it {@{cannot be read from or written to directly}@}. Lastly, there is {@{another special 32-bit or 64-bit register named `eflags` (32-bit) or `rflags` (64-bit)}@}, which {@{holds various _flags_ (not _flag_ as in CTF) representing the current CPU status (state)}@}. The above registers are {@{the most commonly used ones, and there are many more not mentioned here}@}. <!--SR:!2029-03-27,1307,363!2025-12-30,382,365!2029-07-16,1310,323!2030-05-23,1657,377!2028-05-29,1057,350!2025-12-29,381,365!2028-10-06,1160,350!2030-11-15,1807,385!2029-11-02,1481,363!2028-12-04,1197,357!2027-03-21,718,345!2030-12-17,1832,385-->

A register {@{does not need to be accessed in its entirety}@}. Instead, we can access {@{the lowest (least significant) bits of a register only}@}. To {@{access the entire register (64 bits)}@}, {@{change the register prefix to `r`, e.g. `rax`, `rsp`, `r8`}@}. To {@{access the lowest 32 bits}@}, {@{change the register prefix to `e` if the register name does not contain a number, or append `d` otherwise, e.g. `eax`, `esp`, `r8d`}@}. To {@{access the lowest 16 bits}@}, {@{remove the register prefix if the register name does not contain a number, or append `w` otherwise, e.g. `ax`, `sp`, `r8w`}@}. To {@{access the lowest 8 bits}@}, {@{remove the register prefix, remove the ending `x` if any, and append `l` if the register name does not contain a number, or append `b` otherwise, e.g. `al`, `spl`, `r8b`}@}. For {@{4 of the registers, which are `eax`/`rax`, `ecx`/`rcx`, `edx`/`rdx`, and `ebx`/`rbx`}@}, we can {@{also access the 8 bits just above the lowest 8 bits}@} by {@{writing `ah`, `ch`, `dh`, or `bh`}@}. <!--SR:!2030-10-19,1783,383!2029-06-13,1381,377!2029-01-29,1260,363!2030-08-16,1732,385!2028-07-16,1075,343!2029-07-08,1402,377!2027-03-25,713,330!2026-01-31,406,365!2028-09-09,1134,350!2028-04-04,993,343!2027-11-21,881,337!2029-05-11,1343,363!2027-03-19,698,337-->

The register names of {@{4 registers were intended to have meanings}@}, with {@{`esp` being the "stack pointer", `ebp` being the "base pointer", `esi` being the "source index", and `edi` being the "destination index"}@}, but you can use them {@{in any way you want theoretically}@}. In practice, {@{a convention is adopted, and certain general-purpose registers are intended to be used in a specific way}@}. A common convention is that `rsp` {@{is really the _stack pointer_ pointing to the top \(low address\) of the stack, `rbp` is really the _base pointer_ pointing to the bottom \(high address\) of the current frame in the stack}@}, but `rdi` and `rsi` {@{have no particular meanings}@}. `rsp` is used this way because {@{`push`, `pop`, `call`, and `ret` manipulate `rsp`}@}. <!--SR:!2030-12-12,1827,385!2026-01-07,386,365!2030-10-18,1784,385!2027-07-12,795,343!2028-09-05,1064,343!2029-04-19,1347,391!2026-04-01,146,417-->

### syntax branches

x86 has {@{two main syntax branches: _Intel syntax_ and _AT&T syntax_}@}. We will use the former here. Note that GCC {@{by default outputs the latter, and you need to specify `-masm=intel` (e.g. `gcc -S <input>.i -masm=intel`) to output the former}@}. <!--SR:!2030-07-01,1672,363!2028-10-06,1171,365-->

### instructions

Comment {@{starts with `;` to the end of line}@}, similar to {@{`//` in C}@}. <!--SR:!2029-09-02,1447,377!2026-02-08,414,365-->

An instruction is specified by {@{the operation name and a comma-separated list of operands if any}@}. For most cases, {@{the operands need to be the same size}@}. Operands can be {@{_constants_, _registers_, or _memory references_}@}. The first two are trivial, but the last one will be explained below. <!--SR:!2027-11-12,894,357!2028-08-14,1134,365!2027-10-26,877,343-->

Memory reference has the syntax of {@{`[base + index * scale + offset]` (square brackets are required)}@}. `base` is {@{a register}@}, `index` is {@{another register}@}, `scale` is {@{either 1, 2, 4, or 8}@}, and `offset` is {@{a constant}@}. Any part of it can {@{be omitted, and then said part will be assumed 0}@}. Its semantics is that {@{the memory address to be used as the operand is calculated from the expression inside the square brackets}@}. Note that {@{at most 1 memory reference can be used in an instruction}@}. For example, if one wants to {@{copy the value from a memory address to another}@}, {@{two instructions are required}@}: {@{copy the value from the first address to a register}@}, and then {@{copy the value from the register to the second address}@}. One issue is that {@{a memory reference does not have a specified size}@}, so if {@{the operand size cannot be inferred from other operands}@}, then {@{we need to specify the size of the memory reference}@}. To do so, we can {@{prepend `byte` (1 byte), `word` (2 bytes), `dword` (4 bytes; double word), or `qword` (8 bytes; quadruple word) before the memory reference}@}. <!--SR:!2029-09-21,1449,363!2026-02-02,410,365!2026-02-08,413,365!2028-05-26,1056,350!2026-02-19,422,365!2027-03-11,696,330!2028-05-22,1034,343!2028-05-03,1036,350!2029-07-28,1406,363!2026-01-25,143,337!2026-01-05,384,365!2030-12-11,1827,385!2028-02-03,977,365!2029-07-14,1392,363!2026-02-27,148,413!2026-02-25,146,413-->

A note on endianness. For registers, {@{it does not make sense to talk about endianness as it requires each byte to have an address, which the bytes in a register do not have}@}. At most, you can get {@{the lowest (least significant) bits of a register, which is unambiguous}@}. For reading from or writing to memory addresses, it {@{does matter as the bytes have addresses}@}. Usually, it is {@{little-endian, which means the least significant bits are stored in the lowest (smallest) memory addresses}@}. <!--SR:!2026-01-26,403,365!2029-06-24,1378,363!2026-01-25,403,365!2029-01-27,1262,365-->

Below is a list of common instructions (in learning order):

- `mov <dest>, <src>` ::@:: Copy a value at `<src>` to `<dest>`. <!--SR:!2026-01-30,405,365!2025-12-25,377,365-->
- `add <dest> <src>` ::@:: Increment the value at `<dest>` by `<src>`. <!--SR:!2028-12-14,1214,350!2029-01-11,1248,363-->
- `sub <dest> <src>` ::@:: Decrement the value at `<dest>` by `<src>`. <!--SR:!2026-01-15,393,365!2030-11-21,1812,385-->
- `imul <dest> <src>` ::@:: Multiply the value at `<dest>` by `<src>`, signed. <!--SR:!2028-07-10,1081,357!2028-12-11,1210,365-->
- `idiv <src>` ::@:: Divide the value at `ax` (8-bit), `dx:ax` (16-bit), `edx:eax` (32-bit), or `rdx:rax` (64-bit) by `<src>`, truncated towards 0 and signed. <!--SR:!2027-03-20,584,270!2030-04-02,1614,377-->
- `and <dest> <src>` ::@:: Bitwise and the value at `<dest>` with `<src>`. <!--SR:!2030-09-24,1763,383!2029-06-22,1377,363-->
- `or <dest> <src>` ::@:: Bitwise or the value at `<dest>` with `<src>`. <!--SR:!2026-01-18,397,365!2028-08-17,1119,350-->
- `xor <dest> <src>` ::@:: Bitwise exclusive-or the value at `<dest>` with `<src>`. <!--SR:!2025-12-23,375,365!2026-01-08,387,363-->
- `inc <dest>` ::@:: Increment the value at `<dest>` by 1. <!--SR:!2026-01-14,393,365!2030-07-27,1707,377-->
- `dec <dest>` ::@:: Decrement the value at `<dest>` by 1. <!--SR:!2029-05-24,1367,377!2028-08-11,1115,350-->
- `neg <dest>` ::@:: Negate the value at `<dest>`. <!--SR:!2029-01-15,1239,365!2030-01-28,1564,377-->
- `not <dest>` ::@:: Bitwise not the value at `<dest>`. <!--SR:!2030-01-24,1547,363!2029-08-02,1409,363-->
- `cmp <left>, <right>` ::@:: Subtract `<right>` from `<left>`. If the result is zero, the zero flag `ZF` is set (`1`), otherwise unset (`0`). That is, the zero flag represents if `<left>` equals `<right>`. <!--SR:!2026-01-04,383,365!2030-01-09,1549,377-->
- `je <addr>`, `jz <addr>` ::@:: Jump to `<addr>` if the zero flag `ZF` is set (`1`). Assuming the zero flag is set by `cmp <left> <right>` in the previous executed instruction, then it is jump to `<addr>` if `<left>` equals `<right>`. <!--SR:!2027-08-02,770,345!2029-06-26,1304,365-->
- `jmp <addr>` ::@:: Jump to `<addr>`. Sometimes, the instruction before it in an assembly program (`.i`) is the instruction `jcc`. If `jcc` did not jump due to not satisfying a condition, then this instruction represents the `else` branch. <!--SR:!2028-05-10,1048,357!2028-12-10,1222,363-->
- `test <left>, <right>` ::@:: Bitwise and `<left>` with `<right>`. If the result is zero, the zero flag `ZF` is set (`1`), otherwise unset (`0`). That is, the zero flag represents if there are common `1` bits between `<left>` and `<right>`. If `<left>` equals `<right>`, then this is equivalent to checking if `<left>`/`<right>` is zero. <!--SR:!2028-03-01,915,345!2026-01-05,384,365-->
- `jcc <addr>` ::@:: Jump to `<addr>` depending on a condition. `cc` stands for `condition code`. It represents multiple instructions, such as `je` (jump if equal), `jz` (jump if zero, equivalent to `je`), `jnz` (jump if nonzero), `jg` (jump if greater, signed), `ja` (jump if above, unsigned), `jbe` (jump if below or equal, unsigned), `jnle` (jump if not less or equal), etc. Usually used with a `cmp` or `test` in the previous executed instruction. <!--SR:!2027-04-04,716,345!2028-08-27,1138,363-->
- `nop` ::@:: Does nothing. It has the value `0x90`. <!--SR:!2030-11-18,1806,383!2029-04-08,1317,363-->
- `syscall` ::@:: Perform a system call \(syscall\). A system call interacts with the operating system. The system call invoked depends on the value of `eax`/`rax`, and parameters required by the system call depends on other registers. <!--SR:!2027-12-24,936,357!2028-05-09,1021,343-->
  - `syscall` / write ::@:: `rax` is `1`, `rdi` is the file descriptor to be written to \(`1` for stdout\), `rsi` is the start address of the string to write, and `rdx` is the length of the string to write. Note that the null terminator is irrelevant here, as assembly does not enforce a way to indicate the end of a string and can accommodate any way of doing so. <!--SR:!2026-11-27,454,230!2027-06-02,755,337-->

### sections

An assembly file {@{does not solely consists of instructions}@}. It also {@{contains data or other metadata}@}. Sections {@{split the contents of an assembly file based on the type of content}@}. There are {@{many types of sections}@}, but the most commonly used ones are {@{`.data`, `.bss`, and `.text`}@}. To start a section, the syntax is {@{`section .<section name>`}@}, and {@{all content after this line and before the next section start or end of file}@} is part of this section. <!--SR:!2026-01-24,402,365!2026-02-01,409,365!2026-01-11,390,365!2029-05-31,1359,363!2026-01-27,404,365!2026-01-08,387,365!2029-08-17,1420,363-->

- `.data` ::@:: It contains initialized data, that is, data that we know during assembly. It has read and write permissions. For C, this corresponds to global and static variables that are initialized. <!--SR:!2029-05-05,1339,365!2027-03-31,716,330-->
- `.bss` ::@:: It contains uninitialized data, that is, a memory space for our program to initialize data on during its execution. It has read and write permissions. For C, this corresponds to global and static variables that are uninitialized. <!--SR:!2029-05-25,1354,363!2026-01-06,385,365-->
- `.text` ::@:: It contains the code of our program. It has read and execute permissions. For C, this corresponds to functions. <!--SR:!2027-10-22,873,357!2028-03-01,982,350-->

A key idea in assembly that {@{code and data are treated the same}@}. Indeed, data is represented by {@{instructions (but should not be executed by our program) as well}@}. Some common data instructions include: <!--SR:!2030-10-20,1777,377!2031-01-05,1847,385-->

- `db <data>...` ::@:: Define byte. Represents `<data>...` on a granular level of bytes. This is commonly used to store strings. Remember to add the null terminator for interoperability with C. <!--SR:!2029-09-30,1438,365!2029-02-13,1273,365-->
- `dd <data>` ::@:: Define dword (4 bytes, double word). Represents `<data>` on a granular level of 4 bytes. This can also be used to store `float`s in C. <!--SR:!2030-06-30,1693,383!2029-07-11,1391,363-->
- `dq <data>` ::@:: Define qword (8 bytes, quadruple word). Represents `<data>` on a granular level of 8 bytes. This can also be used to store `double`s in C. <!--SR:!2031-01-11,1852,385!2028-07-03,1086,357-->
- `dw <data>` ::@:: Define word (2 bytes). Represents `<data>` on a granular level of 2 bytes. <!--SR:!2027-11-29,917,357!2028-05-07,1046,357-->
- `resb <size>` ::@:: Reserve `<size>` number of bytes. All modern operating systems will also fill it with zeros. It is commonly used in `.bss`. <!--SR:!2026-01-06,385,365!2030-09-03,1747,385-->
- `resd <size>` ::@:: Reserve `<size>` number of dwords (4 bytes, double word). All modern operating systems will also fill it with zeros. It is commonly used in `.bss`. <!--SR:!2026-01-10,389,365!2028-11-20,1206,365-->
- `resq <size>` ::@:: Reserve `<size>` number of qwords (8 bytes, quadruple word). All modern operating systems will also fill it with zeros. It is commonly used in `.bss`. <!--SR:!2027-09-05,832,345!2026-01-12,391,365-->
- `resw <size>` ::@:: Reserve `<size>` number of word (2 bytes). All modern operating systems will also fill it with zeros. It is commonly used in `.bss`. <!--SR:!2026-08-10,501,323!2029-09-12,1454,377-->

Since {@{a program requires a starting point}@}, usually we are required to {@{[label](#labels) the starting instruction with the name `_start`}@}, and make it {@{global by prepending the line `global _start` before the line with the `_start` label}@}. <!--SR:!2026-04-22,447,323!2029-01-10,1179,365!2026-04-10,143,417-->

### labels

{@{Referencing code or data by their raw address}@} is {@{troublesome and error-prone}@}. We can instead {@{give names, called _labels_, to the code or data at particular addresses}@}. Then we can use {@{those names instead of raw addresses whenever referring to them}@}, such as {@{jump destination and data address}@}. The synax is {@{prepending `<label name>:` before the instruction}@}, e.g. {@{`my_int: dd 2633`, `my_uninit_int: resd 1`}@}. <!--SR:!2026-02-07,412,365!2029-12-26,1524,363!2026-02-02,408,365!2028-12-07,1144,357!2029-08-16,1419,363!2026-04-12,145,417!2026-04-10,143,417-->

Label names are {@{global and unique across an assembly program, and appear in symbol tables of object files}@}. The assembler or linker will {@{transform them into constant addresses during assembly or linking}@}. {@{The loader (before execution of the program)}@} may {@{further modify those constant addresses}@}. <!--SR:!2028-04-06,1015,350!2029-10-13,1484,383!2030-10-09,1777,385!2026-01-06,27,402-->

### assembling a program

To assemble an assembly program as an ELF with {@{NASM}@}, run {@{`nasm -f elf64 <input>.s`, which produces a `.o` object file}@}. Then {@{link the resulting object file(s) using `gcc` or `ld`}@}. <!--SR:!2030-02-22,1592,385!2026-02-05,348,297!2026-01-17,395,365-->

### stack and functions in assembly

x86 and x86-64 makes it easy {@{to enumerate stacks (in both the data structure and memory allocation sense) and functions}@} by {@{providing the instructions `push`, `pop`, `call`, and `ret`}@}. Remember that the stack grows {@{in the negative direction (decreasing address)}@}. <!--SR:!2030-04-23,1632,377!2025-12-26,378,363!2026-12-13,635,330-->

- `push <data>` ::@:: Copy `<data>` to the address pointed by `esp`/`rsp` and then decrement `esp`/`rsp` by the data size. The data size is either 4 or 8 bytes depending on the architecture (but not `<data>`). It can also be 2 bytes if explicitly specified (`push word <data>`), Note that flags are also manipulated. <!--SR:!2028-10-12,1167,350!2028-09-04,1129,365-->
- `pop <dest>` ::@:: Copy the value at the address pointed by `esp`/`rsp` to `<dest>` and then increment `esp`/`rsp` by the data size. The data size is either 4 or 8 bytes depending on the architecture \(but not the value "type" at the stack top\). It can also be 2 bytes if explicitly specified \(`pop word <dest>`\). Note that flags are also manipulated. <!--SR:!2027-07-20,779,345!2028-10-29,1102,343-->
- `call <addr>` ::@:: Push (`push`) the address of the next instruction to the stack and jump to `<addr>`. It can help with implementing function calls in higher-level languages. Note that the _stack pointer_ and _base pointer_ are not modified to create a function frame, and needs to be done by the compiler or yourself. <!--SR:!2026-06-28,464,325!2029-02-07,1269,363-->
- `ret` ::@:: Pop (`pop`) the address of an instruction from the stack and jump to it. This is a bit like `pop eip`/`pop rip`, but this is illegal because `eip`/`rip` is a special register and cannot be read from or written to directly. It can help with implementing function returns in higher-level languages. Note that the _stack pointer_ and _base pointer_ are not modified to restore the function frame, and needs to be done by the compiler or yourself. <!--SR:!2028-06-27,1091,365!2028-08-28,1139,365-->

## tools

There are many types of tools to help us with reversing a program. The three types we will talk about are {@{static analysis, dynamic analysis, and patching}@}. <!--SR:!2025-12-29,358,310-->

Apart from the above, below are some tools useful in general:

- Compiler Explorer: <https://godbolt.org/> ::@:: Edit, compile, and run programs in (almost) any programming language using (almost) any compiler, all in your browser! (By the way, _Godbolt_ is an actual person's name...) <!--SR:!2030-08-03,1715,377!2026-02-17,420,365-->

### tools for static analysis

Static analysis is {@{analyzing the program without actually executing it}@}. Of course, {@{simulating its execution or constucting its control flow graph}@} is also static analysis as long as {@{the program is not actually executed by an actual runtime}@}. An analog is {@{staring at the program until it makes sense}@}. <!--SR:!2029-04-15,1322,365!2030-09-22,1763,385!2027-02-15,691,345!2030-05-11,1648,377-->

Some common tools are:

- `objdump` ::@:: Dump information from object files (`.o`). Use `-d <file>` for disassembly, `-h <file>` for section headers, and add `-M intel` for outputting in the Intel syntax. <!--SR:!2029-11-13,1441,345!2027-06-04,757,345-->
- Radare2 (`r2`) ::@:: Display information from object files (`.o`). To use it interactively, simply pass the filepath to the program. To use it non-interactively, pass `-c "aaaa; pdf @ sym.main; q!"` before the filepath. Common useful commands include `aaaa`, `pdf @ sym.main`, `?`, `<command>?`, etc. <!--SR:!2026-10-18,504,270!2026-01-23,335,290-->
- Ghidra ::@:: An open-source powerful decompiler and disassembler developed by the National Security Agency (NSA). <!--SR:!2025-12-31,382,363!2030-01-25,1562,377-->
- `file <file>` ::@:: Determine possible file types of `<file>`. <!--SR:!2025-12-20,371,357!2028-08-05,1109,350-->
- `strings <file>` ::@:: Print sequences of printable strings in `<file>`. To exclude tiny strings, add `-n <minimum string length>` before `<file>`. <!--SR:!2025-12-21,373,365!2030-11-22,1811,385-->
- `xxd <file>` ::@:: Make a hexdump. To reverse this process, add the `-r` option. <!--SR:!2026-01-17,396,365!2028-03-22,1003,350-->

### tools for dynamic analysis

Dynamic analysis is {@{analyzing the program while executing it}@}. Techniques include {@{fuzzing}@}. Usually we use {@{a debugger, an emulator, or a virtual machine}@}. <!--SR:!2029-07-05,1387,363!2028-10-28,1178,350!2030-01-26,1571,385-->

Some common tools are:

- GNU Debugger (`gdb`) ::@:: A commonly used program debugger on Linux. Best used with extensions like GDB Enhanced Features (GEF), `pwndbg`, etc. <!--SR:!2030-02-28,1588,377!2030-05-30,1661,377-->
- Ghidra ::@:: An open-source powerful decompiler and disassembler developed by the National Security Agency (NSA). It can also act as a debugger itself or use `gdb` as its backend. <!--SR:!2027-12-28,940,357!2030-05-06,1644,377-->
- `strace` ::@:: Trace system calls and signals in realtime. <!--SR:!2030-02-03,1578,385!2028-10-23,1173,350-->
- `ltrace` ::@:: Trace library calls, e.g. `glibc`. <!--SR:!2029-06-19,1375,363!2025-12-18,372,365-->

### tools for patching

While analyzing a program, sometimes we want to {@{change the program behavior, like forcing the program to take a different branch of an `if-else`}@}. In most cases, we want to {@{change the code dynamically while performing [dynamic analysis](#tools%20for%20dynamic%20analysis)}@}. In other cases, we want to {@{process an entire executable before running the program, such as deobfuscation (replace names that had been made nonsense intentionally with sensible ones)}@}. <!--SR:!2026-10-01,573,323!2029-04-09,1317,363!2027-11-28,888,345-->

Some commo tools are:

- GNU Debugger (`gdb`) ::@:: A commonly used program debugger on Linux. We can set breakpoints using `set <location>` so that the program will be suspended for debugging when it executes to that point. <!--SR:!2029-04-03,1312,363!2028-08-06,1110,365-->
- `xxd` and a text editor, e.g. `vim` ::@:: Directly edit the program in heximal format. This does require you to know how instructions are actually stored as data, and is best for small patches. <!--SR:!2030-10-23,1778,377!2030-12-05,1822,385-->
- Ghidra ::@:: An open-source powerful decompiler and disassembler developed by the National Security Agency (NSA). It can also patch code: right-click, press "Patch Instruction", and type assembly code. Best for more complicated patches. <!--SR:!2027-08-11,825,343!2030-11-12,1805,385-->
- Radare2 (`r2`) ::@:: Best for automated or procedural patches. We can interface with it in Python via the `r2pipe` module. <!--SR:!2027-11-22,882,343!2029-02-12,1272,365-->
