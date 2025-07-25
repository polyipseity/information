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

Why do reverse engineering, apart from CTFs? ::@:: You can analyze malware, ensuring interoperability with closed-source programs, or find vulnerabilities in them. What they have in common is that the program source is not readily available.

## compiling a program

Assuming you are using Linux. For developers, compiling a C program is {@{simply running the GNU Compiler Collection (gcc) using the ocmmand `gcc <input>.c -o <output>` in a terminal, which compiles the C code in `<input>.c` into a program called `<output>`}@}.

However, we can go further than this. The program `<output>` is {@{actually a format called an _Executable and Linkable Format_ (ELF) file}@}. The property we can about here is that {@{you can execute it, as evident from the "executable" in its name}@}. Details will be mentioned in later lectures.

Instead, we are more interested in {@{the compilation process itself}@}. We like to think of compilation as a single process, but {@{it is really composed of several steps: preprocessing (`-E`), then compilation (`-S`), then assembly (`-c`), and finally linking (none)}@}.

Preprocessing {@{transforms source program (text) into modified source program (still text)}@}. GCC internally {@{uses the program `cpp`, which we can use by itself}@}, for this step. To only run this step with GCC, the command is {@{`gcc -E <input>.c > <output>.i`, which writes to `<output>.i`}@}.

Compilation {@{transforms modified source program (text) into assembly program (still text)}@}. GCC internally {@{uses the program `cc1`, part of the GCC}@}, for this step. To only run this step, the command is {@{`gcc -S <input>.i`, which outputs a `.s` file}@}.

Assembly {@{transforms assembly program (text) into relocatable object (binary)}@}. GCC internally {@{uses the program `as`, which we can use by itself}@}, for this step. To only run this step, the command is {@{`gcc -c <input>.s`, which outputs a `.o` file}@}.

Linking {@{transforms relocatable object (binary) into an ELF file (binary)}@}, which is the final product we want. GCC internally {@{uses the program `ld`, which we can use by itself}@}, for this step. To only run this step, the command is {@{`gcc <input>.o -o <output>`, which outputs the ELF file as `<output>`}@}.

It is okay that one does not understand everything above. The most important part is that {@{a source file is transformed into assembly program, which is finally transformed into the ELF file}@}. {@{Reversing the ELF file into the assembly program}@} is easy as {@{assembly has a mostly direct correspondence with instructions in the ELF file}@}, but {@{reversing the assembly program into the original source program}@} is difficult as {@{language constructs can be compiled into assembly in a multitude of ways, losing information in the process}@}. Reversing is somewhat about the latter, but more accurately is about {@{understanding the program behavior from the assembly without the source program}@}. And to do so, we need to {@{learn assembly}@}.

## assembly language

Assembly is {@{not a single language}@}. Rather, there are {@{multiple languages, called _instruction set architecture_ (ISA)}@}. The most common ones are {@{x86 and x86-64}@}, which we will focus on. Other examples include {@{ARM32, ARM64, RISC-V, Power ISA, and MIPS}@}.

### registers

Registers {@{hold data of fixed small sizes}@}. x86, a {@{32-bit}@} architecture, has {@{8 general-purpose 32-bit registers, named `eax`, `ecx`, `edx`, `ebx`, `esp`, `ebp`, `esi`, and `edi`}@}. x86-64, a {@{64-bit}@} architecture, introduces {@{8 additional general-purpose 64-bit registers, named `r8`, `r9`, `r10`, `r11`, `r12`, `r13`, `r14`, and `r15`}@}, and upgrades {@{the old 8 general-purpose 32-bit registers to 64-bit and changing the starting `e` to `r`}@}. There is also {@{a special 32-bit or 64-bit register named `eip` (32-bit) or `rip` (64-bit)}@}, which {@{points to the current instruction being executed}@}. Unlike other registers, it {@{cannot be read from or written to directly}@}. Lastly, there is {@{another special 32-bit or 64-bit register named `eflags` (32-bit) or `rflags` (64-bit)}@}, which {@{holds various _flags_ (not _flag_ as in CTF) representing the current CPU status (state)}@}. The above registers are {@{the most commonly used ones, and there are many more not mentioned here}@}.

A register {@{does not need to be accessed in its entirety}@}. Instead, we can access {@{the lowest (least significant) bits of a register only}@}. To {@{access the entire register (64 bits)}@}, {@{change the register prefix to `r`, e.g. `rax`, `rsp`, `r8`}@}. To {@{access the lowest 32 bits}@}, {@{change the register prefix to `e` if the register name does not contain a number, or append `d` otherwise, e.g. `eax`, `esp`, `r8d`}@}. To {@{access the lowest 16 bits}@}, {@{remove the register prefix if the register name does not contain a number, or append `w` otherwise, e.g. `ax`, `sp`, `r8w`}@}. To {@{access the lowest 8 bits}@}, {@{remove the register prefix, remove the ending `x` if any, and append `l` if the register name does not contain a number, or append `b` otherwise, e.g. `al`, `spl`, `r8b`}@}. For {@{4 of the registers, which are `eax`/`rax`, `ecx`/`rcx`, `edx`/`rdx`, and `ebx`/`rbx`}@}, we can {@{also access the 8 bits just above the lowest 8 bits}@} by {@{writing `ah`, `ch`, `dh`, or `bh`}@}.

The register names of {@{4 registers were intended to have meanings}@}, with {@{`esp` being the "stack pointer", `ebp` being the "base pointer", `esi` being the "source index", and `edi` being the "destination index"}@}, but you can use them {@{in any way you want theoretically}@}. In practice, {@{a convention is adopted, and certain general-purpose registers are intended to be used in a specific way}@}. A common convention is that {@{`rsp` is really the _stack pointer_ pointing to the top (low address) of the stack, `rbp` is really the _base pointer_ pointing to the bottom (high address) of the current frame in the stack, but `rdi` and `rsi` have no particular meanings}@}. `rsp` is used this way because {@{`push`, `pop`, `call`, and `ret` manipulate `rsp`}@}.

### syntax branches

x86 has {@{two main syntax branches: _Intel syntax_ and _AT&T syntax_}@}. We will use the former here. Note that GCC {@{by default outputs the latter, and you need to specify `-masm=intel` (e.g. `gcc -S <input>.i -masm=intel`) to output the former}@}.

### instructions

Comment {@{starts with `;` to the end of line}@}, similar to {@{`//` in C}@}.

An instruction is specified by {@{the operation name and a comma-separated list of operands if any}@}. For most cases, {@{the operands need to be the same size}@}. Operands can be {@{_constants_, _registers_, or _memory references_}@}. The first two are trivial, but the last one will be explained below.

Memory reference has the syntax of {@{`[base + index * scale + offset]` (square brackets are required)}@}. `base` is {@{a register}@}, `index` is {@{another register}@}, `scale` is {@{either 1, 2, 4, or 8}@}, and `offset` is {@{a constant}@}. Any part of it can {@{be omitted, and then said part will be assumed 0}@}. Its semantics is that {@{the memory address to be used as the operand is calculated from the expression inside the square brackets}@}. Note that {@{at most 1 memory reference can be used in an instruction}@}. For example, if one wants to {@{copy the value from a memory address to another}@}, {@{two instructions are required, copy the value from the first address to a register, and then copy the value from the register to the second address}@}. One issue is that {@{a memory reference does not have a specified size}@}, so if {@{the operand size cannot be inferred from other operands}@}, then {@{we need to specify the size of the memory reference}@}. To do so, we can {@{prepend `byte` (1 byte), `word` (2 bytes), `dword` (4 bytes; double word), or `qword` (8 bytes; quadruple word) before the memory reference}@}.

A note on endianness. For registers, {@{it does not make sense to talk about endianness as it requires each byte to have an address, which the bytes in a register do not have}@}. At most, you can get {@{the lowest (least significant) bits of a register, which is unambiguous}@}. For reading from or writing to memory addresses, it {@{does matter as the bytes have addresses}@}. Usually, it is {@{little-endian, which means the least significant bits are stored in the lowest (smallest) memory addresses}@}.

Below is a list of common instructions (in learning order):

- `mov <dest>, <src>` ::@:: Copy a value at `<src>` to `<dest>`.
- `add <dest> <src>` ::@:: Increment the value at `<dest>` by `<src>`.
- `sub <dest> <src>` ::@:: Decrement the value at `<dest>` by `<src>`.
- `imul <dest> <src>` ::@:: Multiply the value at `<dest>` by `<src>`, signed.
- `idiv <src>` ::@:: Divide the value at `ax` (8-bit), `dx:ax` (16-bit), `edx:eax` (32-bit), or `rdx:rax` (64-bit) by `<src>`, truncated towards 0 and signed.
- `and <dest> <src>` ::@:: Bitwise and the value at `<dest>` with `<src>`.
- `or <dest> <src>` ::@:: Bitwise or the value at `<dest>` with `<src>`.
- `xor <dest> <src>` ::@:: Bitwise exclusive-or the value at `<dest>` with `<src>`.
- `inc <dest>` ::@:: Increment the value at `<dest>` by 1.
- `dec <dest>` ::@:: Decrement the value at `<dest>` by 1.
- `neg <dest>` ::@:: Negate the value at `<dest>`.
- `not <dest>` ::@:: Bitwise not the value at `<dest>`.
- `cmp <left>, <right>` ::@:: Subtract `<right>` from `<left>`. If the result is zero, the zero flag `ZF` is set (`1`), otherwise unset (`0`). That is, the zero flag represents if `<left>` equals `<right>`.
- `je <addr>`, `jz <addr>` ::@:: Jump to `<addr>` if the zero flag `ZF` is set (`1`). Assuming the zero flag is set by `cmp <left> <right>` in the previous executed instruction, then it is jump to `<addr>` if `<left>` equals `<right>`.
- `jmp <addr>` ::@:: Jump to `<addr>`. Sometimes, the instruction before it in an assembly program (`.i`) is the instruction `jcc`. If `jcc` did not jump due to not satisfying a condition, then this instruction represents the `else` branch.
- `test <left>, <right>` ::@:: Bitwise and `<left>` with `<right>`. If the result is zero, the zero flag `ZF` is set (`1`), otherwise unset (`0`). That is, the zero flag represents if there are common `1` bits between `<left>` and `<right>`. If `<left>` equals `<right>`, then this is equivalent to checking if `<left>`/`<right>` is zero.
- `jcc <addr>` ::@:: Jump to `<addr>` depending on a condition. `cc` stands for `condition code`. It represents multiple instructions, such as `je` (jump if equal), `jz` (jump if zero, equivalent to `je`), `jnz` (jump if nonzero), `jg` (jump if greater, signed), `ja` (jump if above, unsigned), `jbe` (jump if below or equal, unsigned), `jnle` (jump if not less or equal), etc. Usually used with a `cmp` or `test` in the previous executed instruction.
- `nop` ::@:: Does nothing. It has the value `0x90`.
- `syscall` ::@:: Perform a system call (syscall). A system call interacts with the operating system. The system call invoked depends on the value of `eax`/`rax`, and parameters required by the system call depends on other registers.
  - `syscall` / write ::@:: `rax` is `1`, `rdi` is the file descriptor to be written to (`1` for stdout), `rsi` is the start address of the string to write, and `rdx` is the length of the string to write. Note that the null terminator is irrelevant here, as assembly does not specify a way to indicate the end of a string and can accommodate any way of doing so.

### sections

An assembly file {@{does not solely consists of instructions}@}. It also {@{contains data or other metadata}@}. Sections {@{split the contents of an assembly file based on the type of content}@}. There are {@{many types of sections}@}, but the most commonly used ones are {@{`.data`, `.bss`, and `.text`}@}. To start a section, the syntax is {@{`section .<section name>`}@}, and {@{all content after this line and before the next section start or end of file}@} is part of this section.

- `.data` ::@:: It contains initialized data, that is, data that we know during assembly. It has read and write permissions. For C, this corresponds to global and static variables that are initialized.
- `.bss` ::@:: It contains uninitialized data, that is, a memory space for our program to initialize data on during its execution. It has read and write permissions. For C, this corresponds to global and static variables that are uninitialized.
- `.text` ::@:: It contains the code of our program. It has read and execute permissions. For C, this corresponds to functions.

A key idea in assembly that {@{code and data are treated the same}@}. Indeed, data is represented by {@{instructions (but should not be executed by our program) as well}@}. Some common data instructions include:

- `db <data>...` ::@:: Define byte. Represents `<data>...` on a granular level of bytes. This is commonly used to store strings. Remember to add the null terminator for interoperability with C.
- `dd <data>` ::@:: Define dword (4 bytes, double word). Represents `<data>` on a granular level of 4 bytes. This can also be used to store `float`s in C.
- `dq <data>` ::@:: Define qword (8 bytes, quadruple word). Represents `<data>` on a granular level of 8 bytes. This can also be used to store `double`s in C.
- `dw <data>` ::@:: Define word (2 bytes). Represents `<data>` on a granular level of 2 bytes.
- `resb <size>` ::@:: Reserve `<size>` number of bytes. All modern operating systems will also fill it with zeros. It is commonly used in `.bss`.
- `resd <size>` ::@:: Reserve `<size>` number of dwords (4 bytes, double word). All modern operating systems will also fill it with zeros. It is commonly used in `.bss`.
- `resq <size>` ::@:: Reserve `<size>` number of qwords (8 bytes, quadruple word). All modern operating systems will also fill it with zeros. It is commonly used in `.bss`.
- `resw <size>` ::@:: Reserve `<size>` number of word (2 bytes). All modern operating systems will also fill it with zeros. It is commonly used in `.bss`.

Since {@{a program requires a starting point}@}, usually we are required to {@{[label](#labels) the starting instruction with the name `_start`, and make it global by prepending the line `global _start` before the line with the `_start` label}@}.

### labels

{@{Referencing code or data by their raw address}@} is {@{troublesome and error-prone}@}. We can instead {@{give names, called _labels_, to the code or data at particular addresses}@}. Then we can {@{use those names instead of raw addresses whenever referring to them, such as jump destination and data address}@}. The synax is {@{prepending `<label name>:` before the instruction, e.g. `my_int: dd 2633`, `my_uninit_int: resd 1`}@}.

Label names are {@{global and unique across an assembly program, and appear in symbol tables of object files}@}. The assembler or linker will {@{transform them into constant addresses during assembly or linking}@}. The loader {@{(before execution of the program) may further modify those constant addresses}@}.

### assembling a program

To assemble an assembly program as an ELF with {@{NASM}@}, run {@{`nasm -f elf64 <input>.s`, which produces a `.o` object file}@}. Then {@{link the resulting object file(s) using `gcc` or `ld`}@}.

### stack and functions in assembly

x86 and x86-64 makes it easy {@{to enumerate stacks (in both the data structure and memory allocation sense) and functions}@} by {@{providing the instructions `push`, `pop`, `call`, and `ret`}@}. Remember that the stack grows {@{in the negative direction (decreasing address)}@}.

- `push <data>` ::@:: Copy `<data>` to the address pointed by `esp`/`rsp` and then decrement `esp`/`rsp` by the data size. The data size is either 4 or 8 bytes depending on the architecture (but not `<data>`). It can also be 2 bytes if explicitly specified (`push word <data>`), Note that flags are also manipulated.
- `pop <dest>` ::@:: Copy the value at the address pointed by `esp`/`rsp` to `<dest>` and then increment `esp`/`rsp` by the data size. The data size is either 4 or 8 bytes depending on the architecture \(but not the value "type" at the stack top\). It can also be 2 bytes if explicitly specified \(`pop word <dest>`\). Note that flags are also manipulated.
- `call <addr>` ::@:: Push (`push`) the address of the next instruction to the stack and jump to `<addr>`. It can help with implementing function calls in higher-level languages. Note that the _stack pointer_ and _base pointer_ are not modified to create a function frame, and needs to be done by the compiler or yourself.
- `ret` ::@:: Pop (`pop`) the address of an instruction from the stack and jump to it. This is a bit like `pop eip`/`pop rip`, but this is illegal because `eip`/`rip` is a special register and cannot be read from or written to directly. It can help with implementing function returns in higher-level languages. Note that the _stack pointer_ and _base pointer_ are not modified to restore the function frame, and needs to be done by the compiler or yourself.

## tools

There are many types of tools to help us with reversing a program. The three types we will talk about are {@{static analysis, dynamic analysis, and patching}@}.

Apart from the above, below are some tools useful in general:

- Compiler Explorer: <https://godbolt.org/> ::@:: Edit, compile, and run programs in (almost) any programming language using (almost) any compiler, all in your browser! (By the way, _Godbolt_ is an actual person's name...)

### tools for static analysis

Static analysis is {@{analyzing the program without actually executing it}@}. Of course, {@{simulating its execution or constucting its control flow graph}@} is also static analysis as long as {@{the program is not actually executed by an actual runtime}@}. An analog is {@{staring at the program until it makes sense}@}.

Some common tools are:

- `objdump` ::@:: Dump information from object files (`.o`). Use `-d <file>` for disassembly, `-h <file>` for section headers, and add `-M intel` for outputting in the Intel syntax.
- Radare2 (`r2`) ::@:: Display information from object files (`.o`). To use it interactively, simply pass the filepath to the program. To use it non-interactively, pass `-c "aaaa; pdf @ sym.main; q!"` before the filepath. Common useful commands include `aaaa`, `pdf @ sym.main`, `?`, `<command>?`, etc.
- Ghidra ::@:: An open-source powerful decompiler and disassembler developed by the National Security Agency (NSA).
- `file <file>` ::@:: Determine possible file types of `<file>`.
- `strings <file>` ::@:: Print sequences of printable strings in `<file>`. To exclude tiny strings, add `-n <minimum string length>` before `<file>`.
- `xxd <file>` ::@:: Make a hexdump. To reverse this process, add the `-r` option.

### tools for dynamic analysis

Dynamic analysis is {@{analyzing the program while executing it}@}. Techniques include {@{fuzzing}@}. Usually we use {@{a debugger, an emulator, or a virtual machine}@}.

Some common tools are:

- GNU Debugger (`gdb`) ::@:: A commonly used program debugger on Linux. Best used with extensions like GDB Enhanced Features (GEF), `pwndbg`, etc.
- Ghidra ::@:: An open-source powerful decompiler and disassembler developed by the National Security Agency (NSA). It can also act as a debugger itself or use `gdb` as its backend.
- `strace` ::@:: Trace system calls and signals in realtime.
- `ltrace` ::@:: Trace library calls, e.g. `glibc`.

### tools for patching

While analyzing a program, sometimes we want to {@{change the program behavior, like forcing the program to take a different branch of an `if-else`}@}. In most cases, we want to {@{change the code dynamically while performing [dynamic analysis](#tools%20for%20dynamic%20analysis)}@}. In other cases, we want to {@{process an entire executable before running the program, such as deobfuscation (replace names that had been made nonsense intentionally with sensible ones)}@}.

Some commo tools are:

- GNU Debugger (`gdb`) ::@:: A commonly used program debugger on Linux. We can set breakpoints using `set <location>` so that the program will be suspended for debugging when it executes to that point.
- `xxd` and a text editor, e.g. `vim` ::@:: Directly edit the program in heximal format. This does require you to know how instructions are actually stored as data, and is best for small patches.
- Ghidra ::@:: An open-source powerful decompiler and disassembler developed by the National Security Agency (NSA). It can also patch code: right-click, press "Patch Instruction", and type assembly code. Best for more complicated patches.
- Radare2 (`r2`) ::@:: Best for automated or procedural patches. We can interface with it in Python via the `r2pipe` module.
