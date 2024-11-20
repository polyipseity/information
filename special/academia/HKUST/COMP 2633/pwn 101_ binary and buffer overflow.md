---
aliases:
  - Pwn 101
  - 'Pwn 101: Binary and Buffer Overflow'
  - binary and buffer overflow
  - pwn 101
  - 'pwn 101: binary and buffer overflow'
tags:
  - flashcard/active/special/academia/HKUST/COMP_2633/pwn_101__binary_and_buffer_overflow
  - function/index
  - language/in/English
---

# pwn 101: binary and buffer overflow

__Pwn__, in a general context, means {@{the domination of a player in a video game or argument, or the successful hacking of a website or computer}@}. In CTFs, it is {@{one of the major categories and usually refers to __binary exploitation__}@}. <!--SR:!2024-11-23,46,290!2025-04-08,146,310-->

__Binary exploitation__ is about {@{finding vulnerabilities in a program binary, and then exploiting them}@}. To find vulnerabilities without its source, we need to {@{reverse the binary, the basics of which are taught in [reverse 101](reverse%20101_%20world%20of%20binaries.md), so it is recommended that reverse is first learnt}@}. <!--SR:!2024-12-13,64,310!2024-12-06,59,310-->

A quick recap of types of tools used for reverse: {@{static analysis, dynamic analysis, and patching}@}. <!--SR:!2024-11-30,53,310-->

## memory model

What is a memory model? It refers to how {@{memory in a program is modelled by the OS}@}. In {@{the good o' days of computing}@}, memory address is {@{really the address of the physical memory}@}. But modern OSes do not do that. One of the many reasons is security: {@{consider that the physical memory is shared by all processes, it is insecure for one process to be able to access the memory of any other process, e.g. a password manager}@}. <!--SR:!2025-05-03,166,310!2025-03-31,140,310!2024-12-24,68,310!2024-11-21,42,290-->

Instead, modern OSes has the concept of {@{virtual memory}@}, which is managed by {@{a hardware called the memory management unit (MMU)}@}. To any single process, it looks like {@{there is still a "physical" memory}@}, but {@{the OS maps different parts of the "physical" memory to different parts of the actual physical memory, or even files on storage devices}@}! Some parts {@{may not be mapped (unmapped) at all, and accessing them will likely crash the program  (receive `SIGSEGV` signal)}@}. The mapping is {@{usually private to a single process, that is, that mapping is only used by that process and no other processes}@}. This is {@{good for security as a process can only access the memory of itself but not other processes}@}. <!--SR:!2024-11-23,46,290!2024-11-26,47,290!2024-12-02,55,310!2025-03-14,124,290!2024-12-01,54,310!2025-02-07,105,290!2024-11-24,45,290-->

However, further knowledge memory model is {@{not exactly important in basic pwn}@}. All one needs to know is that {@{parts of memory in a program are mapped to different parts of the actual physical memory or some files on storage devices}@}. <!--SR:!2024-11-24,47,290!2024-12-24,68,310-->

### memory mapping

For pwn, it is more important to know {@{the typical memory mapping for a process}@}. A memory mapping is {@{called a segment, not to be confused with sections, as a segment can contain multiple sections}@}. We will learn about {@{4 segments, in the order of low (small) address to high (large) address: read-execute segment, read-write segment, heap, and stack}@}. There may {@{or may not be unmapped space in between the segments}@}. Ignoring those space, {@{read-execute segment, read-write segment, and heap are very close together}@}. The heap {@{can dynamically grow upwards (increasing address) at runtime}@}, while others {@{usually cannot grow}@}. The stack {@{is very close to the highest address and can dynamically grow downwards (decreasing address) at runtime}@}. <!--SR:!2025-05-09,171,310!2024-11-29,52,310!2024-12-15,66,310!2025-05-08,170,310!2024-12-09,60,310!2024-12-15,66,310!2024-12-08,59,310!2025-02-27,119,290-->

The meanings of the 4 segments are:

- read-execute segment ::@:: The segment that the program can read from and execute code on it. It usually contains the ELF header, `.rodata` (read-only data) and `.text` (code) sections in assembly. <!--SR:!2025-02-01,84,270!2024-11-21,42,290-->
- read-write segment ::@:: The segment that the program and read from and write to. It usually contains the `.bss` and `.data` sections in assembly. <!--SR:!2024-11-29,52,310!2024-12-01,54,310-->
- heap ::@:: It contains memory allocated at runtime. Usually, it is allocated for manual memory management (e.g. `malloc`, `new`). It grows upwards (increasing address). <!--SR:!2024-12-06,57,310!2024-12-01,54,310-->
- stack ::@:: It also contains memory allocated at runtime, but for small data (e.g., local variables) and also function-related data. Usually, it is allocated for automatic memory management (e.g. local variables). It grows downwards (decreasing address). <!--SR:!2024-11-27,48,290!2025-05-04,165,310-->

Note that the `.rodata` (read-only data) section is located on the read-execute segment. This means {@{the program can execute the data in `.rodata` section as code, which makes it less secure}@}. The linkers of some newer Linux distributions {@{add an additional one or two read segments (the program can only read from it) for the ELF header and `.rodata` section to improve security}@}. <!--SR:!2024-12-24,68,310!2024-12-24,68,310-->

## executable and linkable format

For pwn, it is also important to know {@{the overall structure of an executable and linkable format (ELF) file}@}. ELF files are commonly used on {@{UNIX (including Linux) systems}@}. <!--SR:!2024-12-02,55,310!2024-12-09,60,310-->

Like {@{many file formats}@}, an ELF file has {@{a ELF header indicating that it is an ELF file and the properties of it (32 or 64 bit, offsets, ...)}@}. Its magic number, i.e. {@{the bytes an ELF file must start with}@}, is {@{`0x7F 'E' 'L' 'F'`}@}. Additionally, an ELF file has {@{a program header table at the beginning of the file right after the ELF header, and a section header table at the end of the file}@}. <!--SR:!2025-05-12,173,310!2024-12-24,68,310!2024-11-30,53,310!2024-12-02,55,310!2024-11-22,45,290-->

The program header table {@{specifies how the process image is created, i.e. how the OS should map the memory of the new process to the ELF, i.e. segment (not section) information}@}. The section header table {@{identifies all the sections in an ELF file}@}. Examples of sections are: {@{`.text`, `.data`, `.bss`, `.rodata` (read-only data), etc.}@} <!--SR:!2024-12-15,66,310!2024-12-05,56,310!2024-11-27,50,310-->

## stack in x86 and x86-64 assembly

Revisiting reverse 101... We will use {@{the Intel syntax}@} here. <!--SR:!2024-12-02,55,310-->

In x86 and x86-64, there are {@{two registers related to the stack: `esp`/`rsp` and `ebp`/`rbp`}@}. (We will use the x86-64 registers thereafter.) <!--SR:!2025-03-26,140,310-->

`rsp` is {@{the stack pointer, which points to the top (low address) of the stack memory}@}. This is easy to understand. The more difficult one is {@{`rbp`, which is the stack/function frame base pointer, which points to the bottom (high address) of the current stack/function frame}@}. Yet we do not know {@{what a stack/function frame is, and this will be introduced later}@}. <!--SR:!2024-12-04,57,310!2025-05-08,170,310!2024-12-01,54,310-->

There are {@{several instructions that modify the stack memory and the `rsp` and `rbp` registers appropriately}@}. Some of them are: {@{`push`, `pop`, `call`, `ret`, and `leave`}@}. <!--SR:!2024-12-24,68,310!2024-12-24,68,310-->

- `push <src>` ::@:: Push `<src>` on top of the stack. This writes a value right below the address pointed by `rsp` and decrements `rsp`. <!--SR:!2024-12-10,61,310!2024-12-01,54,310-->
- `pop <dest>` ::@:: Pop the top of the stack and write it to `<dest>`. This reads a value at the address pointed by `rsp` and increments `rsp`. <!--SR:!2024-12-16,67,310!2024-11-26,47,290-->
- `call <address>` ::@:: This pushes (`push`) the `rip` (instruction pointer, pointing to the currently executing instruction) onto the stack, and then jumps (`jmp`) to `<address>`. `<address>`. This is usually used to call a function, in conjunction with `ret`. <!--SR:!2024-12-24,68,310!2024-12-07,58,310-->
- `ret`::@:: This pops (`pop`) a value off from the stack and jumps (`jmp`) to it. (Note that this is similar to `pop rip`, but `pop rip` is invalid because `rip` cannot be modified directly.) This is usually used to return from a function, in conjunction with `call`. <!--SR:!2024-12-10,61,310!2025-01-11,79,290-->
- `leave` ::@:: This sets `rsp` to `rbp`, effectively clearing the current stack frame. Then it pops (`pop`) a value off from the stack to `rbp`. This effectively restores the previous stack frame (the state right before the current function is called (`call`)). This is usually used to cleanup the stack and registers just before returning from a function (`ret`). <!--SR:!2025-05-26,189,310!2025-03-03,113,290-->

A related instruction is {@{`lea`}@}: <!--SR:!2024-12-15,66,310-->

- `lea <dest>, <src>` ::@:: <u>L</u>oad <u>e</u>ffective <u>a</u>ddress. This sets `<dest>` to the memory address of `<src>` (instead of the value at `<src>`). It can be used with memory references to perform arithmetic operations on memory addresses. (In fact, `lea` can be exploited to do addition and multiplication of unsigned integers.) <!--SR:!2024-12-06,59,310!2024-12-07,58,310-->

Since `lea` can {@{mostly be replaced with `add` and `imul` (with the exception of flags)}@}, a natural question is {@{why is there a `lea` instruction in the first place}@}? Apart from {@{`lea` not setting some flags}@}, it is also {@{convenient for implementing array access}@}. Further reading: <https://stackoverflow.com/q/1658294>. <!--SR:!2025-04-22,157,310!2024-11-25,48,310!2024-12-07,60,310!2024-12-24,68,310-->

## calling convention

The instructions above are used to {@{implementing the concept of functions in assembly}@}. However, they {@{do not specify how they should be used}@}. A __calling convention__ specifies {@{how the above instructions are used to manipulate the stack in such a way to represent functions}@}. It is called a _convention_ because {@{the caller and callee (the function to be called by the caller) needs to follow the same (or compatible) calling conventions}@}, or otherwise {@{the stack will be manipulated incorrectly, and the program will likely crash}@}. <!--SR:!2024-12-07,60,310!2024-11-21,44,290!2024-12-05,58,310!2024-12-09,60,310!2024-12-12,63,310-->

There are {@{many different incompatible calling conventions in use}@}. For x86, {@{there are many different ones, but for x86-64, there are only 2 common in use}@}. They are {@{the Microsoft x64 calling convention and the System V AMD64 ABI}@}. We will {@{only introduce a calling convention for x86-64, as the binaries you encounter in CTFs are most likely 64-bit, and that calling convention is the latter one because we are using Linux}@}. Further, you should be able to {@{extract the general principles of calling conventions from the example below and extrapolate them to others}@}. <!--SR:!2024-12-24,68,310!2024-11-25,48,310!2024-12-06,57,310!2024-11-26,49,310!2024-12-01,54,310-->

### System V AMD64 ABI

The complete calling convention {@{would be too much to discuss here, so we will only discuss a (rather small) part of it}@}. Some parts of the process may {@{be optimized away by the compiler}@}. To avoid this, {@{pass `-O0` (for GCC) to disable optimization}@}. <!--SR:!2025-04-23,158,310!2024-12-13,64,310!2024-11-21,44,290-->

A stack/function frame is {@{a portion of the stack that belongs to one function only}@}. Each time {@{one calls a function}@}, {@{a stack/function frame is added on top of the old one}@}. Each time {@{one returns from a function}@}, {@{the current stack/function frame is cleared and the old (the frame for the callee) is restored}@}. `rsp` and `rbp` then refers to {@{respectively the top and the bottom of the topmost stack/function frame (so the current function frame is in between `rsp` and `rbp`)}@}. <!--SR:!2024-12-16,67,310!2025-04-25,160,310!2024-11-29,52,310!2024-12-17,68,310!2024-12-24,68,310!2024-11-25,46,290-->

The detail process of creating a stack frame is {@{pushing `rbp` onto the stack (decrementing `rsp` at the same time) (`push rbp`), and then set `rbp` to `rsp` (`mov rbp rsp`)}@}. One may then note that {@{the current stack/function frame is empty as `rsp` equals `rbp`}@}. Reversing the above operations, i.e. {@{popping a value, previously pushed by `push rbp`, from the stack (incrementing `rsp` at the same time) and storing it to `rbp` (`pop rbp`)}@}, {@{restores the previous stack frame, given the current stack frame is empty}@}. If the current stack frame is {@{nonempty (`rsp` not equals `rbp`)}@}, then {@{simply clear the current stack frame by setting `rsp` to `rbp` (`mov rsp rbp`)}@}. These two operations are so common that {@{the operations have dedicated instructions respectively called `enter` and `leave`}@}. In practice, {@{`enter` has horrible performance so compilers almost always emit `push` and `mov` instead of a single `enter` instruction}@}, but {@{`leave` has okay performance and compilers may emit a single `leave` instruction instead of `mov` and `pop`}@}. <!--SR:!2024-12-06,57,310!2024-12-05,58,310!2025-04-24,159,310!2024-11-24,47,290!2024-11-29,52,310!2025-05-07,168,310!2024-11-28,51,310!2024-12-08,59,310!2024-12-03,56,310-->

In System V AMD64 ABI, the process of creating and destroying a stack frame are {@{both done inside the callee}@}. The caller is responsible for {@{passing the arguments before calling the function and cleaning up the passed arguments after calling the function}@}. <!--SR:!2024-12-15,66,310!2025-03-30,139,310-->

The above only describes how a stack frame is created or destroyed. The missing thing is {@{how arguments and return value are passed}@}. Arguments are passed {@{using registers, and also the stack if there are too many arguments or the arguments are too large in size}@}. To {@{describe how arguments of any type are passed}@} is too complicated here, so we will {@{only consider passing 64-bit integers or pointers}@}. The first 6 arguments goes into {@{the registers, in order, `rdi`, `rsi`, `rdx`, `rcx`, `r8`, and `r9`}@}. The rest are {@{pushed onto the stack before calling the function (`call`)}@}. The return value is {@{also passed using registers}@}. If {@{the return value is within 64 bits, then `rax` is used, or if within 128 bits, then `rdx:rax` is used}@}. Otherwise, {@{the caller will provide a space to store the return value and pass a pointer to that space as the 1st argument, shifting all other arguments by 1}@}. The passed pointer will {@{be written to `rax` by the callee just before returning (`ret`)}@}. An important note is that {@{the argument order does not necessarily match that in the high-level programming language}@}. When C code is compiled with System V AMD64 ABI in GCC, while {@{the first 6 arguments are assigned left to right, the remaining arguments are pushed from right to left (rightmost argument is pushed)}@}. <!--SR:!2024-12-24,68,310!2025-05-07,169,310!2025-02-26,112,290!2024-12-07,60,310!2024-12-07,58,310!2024-11-22,43,290!2024-12-24,68,310!2025-05-10,172,310!2024-11-25,48,310!2024-11-22,45,290!2024-12-05,56,310!2025-03-07,112,290-->

To summarize, the process of calling a function is: {@{passing the arguments, calling the function (`call`), creating a stack frame, doing stuff and setting the return value, restoring the previous stack frame, returning from the function (`ret`), and finally cleaning up the passed arguments}@}. <!--SR:!2024-11-23,46,290-->

## GNU Debugger and pwndbg

To {@{see the registers and the stack while running a program}@}, we will use {@{the GNU Debugger (`gdb`), which is only available on Linux}@}. But {@{the debugger is sometimes rather inconvenient to use for pwn}@}, so we will also use {@{a `gdb` plugin called `pwndbg` (URL: <https://github.com/pwndbg/pwndbg>)}@}. It {@{adds additional commands, and improve existing commands and views. These should make it easier to solve pwn challenges}@}. Install both of them first. <!--SR:!2024-11-25,46,290!2025-01-23,89,290!2024-12-02,55,310!2024-12-24,68,310!2024-12-03,56,310-->

Let's learn some basic `gdb` commands (not exclusive to `pwndbg`):

- `apropos <regex>` ::@:: find text matching `<regex>` in the manual <!--SR:!2024-12-05,58,310!2024-12-24,68,310-->
- `help [<topic>]` ::@:: find information about topic; if topic is not specified, then prints general help <!--SR:!2024-12-24,68,310!2024-12-09,60,310-->
- `file <path>` ::@:: load binary file to debug <!--SR:!2024-12-12,63,310!2024-12-24,68,310-->
- `run [<args>...]` ::@:: run program (with args) <!--SR:!2024-12-06,59,310!2025-04-30,164,310-->
- `set args <args>...` ::@:: set program args <!--SR:!2024-12-13,64,310!2024-11-23,46,290-->
- `starti [<args>...]` ::@:: start program and stop at its first instruction <!--SR:!2024-12-17,68,310!2024-12-24,68,310-->
- `disassemble <address|function>` ::@:: disassemble a specified address or function <!--SR:!2024-11-27,50,310!2024-12-24,68,310-->
- `break <where>` ::@:: set a breakpoint <!--SR:!2024-12-24,68,310!2024-11-27,50,310-->
- `delete [<breakpoint>]` ::@:: delete a breakpoint; if breakpoint is not specified, then delete all breakpoints <!--SR:!2024-12-24,68,310!2024-11-27,50,310-->
- `info address <symbol>` ::@:: print the `<symbol>` (which can be a function name), its type, and its address <!--SR:!2024-12-08,59,310!2024-12-17,68,310-->
- `info breakpoints|regs|threads`::@:: list breakpoints, register values, or threads <!--SR:!2024-12-24,68,310!2024-12-24,68,310-->
- `backtrace` ::@:: print backtrace or call stack <!--SR:!2024-12-03,56,310!2024-12-05,58,310-->
- `ni` ::@:: go to the next instruction <!--SR:!2024-11-28,49,290!2024-11-30,53,310-->
- `si` ::@:: go to the next instruction stepping into functions <!--SR:!2024-12-04,57,310!2024-12-11,62,310-->
- `continue` ::@:: continue program execution <!--SR:!2024-12-01,54,310!2024-12-24,68,310-->
- `finish` ::@:: run until the current function returns <!--SR:!2024-12-24,68,310!2024-12-07,58,310-->
- `x/<format> <address>` ::@:: examine memory at the given address in the given format (see `help x`) <!--SR:!2024-12-05,56,310!2024-12-24,68,310-->
- `print <expression>` ::@:: evaluate and print an expression <!--SR:!2024-12-24,68,310!2024-12-04,57,310-->
- `record` ::@:: record execution of every instruction; can make the process run slowly <!--SR:!2024-12-24,68,310!2024-12-01,54,310-->
- `rni` ::@:: rewind to the previous instruction <!--SR:!2024-12-07,60,310!2024-12-02,55,310-->
- `rsi` ::@:: rewind to the previous instruction stepping into functions <!--SR:!2024-11-24,45,290!2024-12-05,56,310-->
- `rc` ::@:: reverse continue <!--SR:!2024-11-26,49,310!2024-12-02,55,310-->
- `set <storage> = <value>` ::@:: set storage to value <!--SR:!2024-12-14,65,310!2024-11-28,51,310-->

Let's also learn some basic `pwndbg` commands:

- `down` ::@:: move down the backtrace or call stack <!--SR:!2024-12-06,57,310!2024-12-01,54,310-->
- `up` ::@:: move up the backtrace or call stack <!--SR:!2024-12-07,60,310!2024-12-05,56,310-->
- `checksec` ::@:: print the binary security settings <!--SR:!2024-12-12,63,310!2024-12-07,60,310-->
- `stack <count> <offset>` ::@:: prints stack data with the specified count and offset <!--SR:!2024-12-11,62,310!2025-05-17,182,310-->
- `vmmap [<address|name>]` ::@:: display memory mappings information (filtered binary address or name) <!--SR:!2024-12-16,67,310!2025-03-27,139,290-->

Commands names can be {@{truncated at the end to produce an abbreviation if the abbreviation is unambiguous, i.e. there is only exactly one command name starting with the abbreviation}@}. For example, `disassemble` can be {@{abbreviated to `disass` or the uglier `disassem`}@}. <!--SR:!2024-11-24,45,290!2024-12-24,68,310-->

## buffer overflow

A buffer is {@{simply a portion of the memory used to store the data}@}. As {@{real computers have limited memory}@}, the buffer is {@{also limited in its size}@}. The buffer may be on {@{the stack, the heap, read-write segment, read-execute segment, or really anywhere the memory is mapped by the OS}@}. A buffer is {@{usually contagious, that is, it is a continuous portion of the memory}@}, so we can identify a buffer by {@{its low (start) address (inclusive) and high (end) address (exclusive)}@}. <!--SR:!2024-12-24,68,310!2025-05-31,193,310!2024-12-06,50,290!2025-03-03,121,310!2025-05-05,168,310!2024-11-28,51,310-->

The buffers we are usually interested in exploiting is {@{usually on the first three because we can write to the buffer}@}. We will only {@{focus on buffers on the stack because they are the easiest to exploit}@}. <!--SR:!2024-12-11,62,310!2024-11-22,43,290-->

Buffer overflow, then, is {@{simply writing data outside the buffer}@}. Assume the buffer is {@{on the stack}@}. This is likely to {@{overwrite data on other unrelated buffers in the stack, corrupting them}@}. Usually, this {@{results in a program crash}@}. However, if we use buffer overflow to {@{write data to specific locations outside the buffer with specific values}@}, then we can {@{manipulate the program to do unintended things}@}. In CTFs, {@{this is used to find the flag in pwn challenges}@}. <!--SR:!2024-11-29,52,310!2024-12-07,60,310!2024-11-27,50,310!2024-12-04,57,310!2024-12-03,56,310!2024-11-28,51,310!2024-12-09,60,310-->

There are many ways to {@{manipulate the program using buffer overflow}@}, and we will {@{talk about only one interesting way related to function calls}@}. Recall that calling a function via `call` {@{pushes the address to jump to (the next instruction after `call` in the memory) after the function finishes to the stack}@}, and that the function returns {@{via `ret`, which pops the address that we have pushed before calling the function from the stack and jumps back to it, finishing the function call}@}. Using buffer overflow, we can {@{write to that location in the stack and change it to any value we want}@}. Then, when {@{the functions returns via `ret`}@}, instead of {@{jumping back to the caller, it jumps to an arbitrary location that we can freely specify}@}. <!--SR:!2024-12-24,68,310!2025-04-15,152,310!2025-03-24,139,290!2025-02-24,103,290!2024-11-30,53,310!2024-11-29,52,310!2025-01-06,81,329-->

### finding buffer overflows

The most common way buffer overflow occurs is {@{not checking the whether the location in the buffer to be written to}@}. This may be {@{a programming error like a off-by-one error}@}: <!--SR:!2024-12-24,68,310!2024-11-21,44,290-->

```C
int buffer[4]; // Only `buffer[0]`, `buffer[1]`, `buffer[2]`, and `buffer[3]` are within `buffer`.
for (size_t idx = 0; idx <= 4; ++idx) { // Notice the `<=`.
  buffer[idx] = 42; // `idx` can be 4, which will cause this statement to write past the end of `buffer`.
}
```

The above example demonstrates how buffer overflow actually happens. The cases we are usually more interested in is {@{unsafe C string functions that accepts inputs (best if they can be provided by the user directly or indirectly) and writes to other buffers}@}, such as {@{`gets`, `scanf`, `strcpy`, etc.}@} These functions are vulnerable because {@{they will write to the buffer as long as there is data in the input without taking the buffer size into consideration at all}@}. So if {@{the input data is too large to be fit into the destination buffers}@}, then {@{a buffer overflow occurs as the excess data is written past the end of the destination buffers}@}, similar to the example above. An example: <!--SR:!2024-12-12,63,310!2024-12-03,56,310!2025-04-19,161,310!2024-11-23,46,290!2024-12-16,67,310-->

```C
char buffer[4];
gets(buffer); // This prompts for user input. If the user input is longer than 3 characters (4 characters including the null terminator), then a buffer overflow occurs.
scanf("%s", buffer); // Same as above.
```

By now, you should have figured out how to identify code that is vulnerable to buffer overflow.

#### exploiting buffer overflows

Once you have found code that is vulnerable to buffer overflows, {@{identify what special locations you want to overwrite with what values}@}. For example, {@{overwriting the the address in the stack that `ret` will jump to with another address pointing to another function}@}. Then simply {@{craft the data required and pass it to the program}@}. One needs to note that {@{the stack grows in decreasing address}@}, while {@{the above functions write to the buffer in increasing address (from low to high address)}@}, so writing beyond a buffer {@{traverses the stack downwards (items pushed less recently) instead of upwards (items pushed more recently)}@}. Food for thought: What if {@{the stack grows in increasing address}@}? <!--SR:!2024-11-22,45,290!2024-11-21,44,290!2024-12-15,66,310!2024-12-05,58,310!2024-11-25,46,290!2025-04-04,143,310!2024-11-29,52,310-->

To help with this process, there are {@{some tools available}@}. Three tools are {@{`pwntools`, `gdb`, and `patchelf`}@}. <!--SR:!2024-12-17,68,310!2024-12-17,68,310-->

`pwntools` (URL: {@{<https://github.com/Gallopsled/pwntools>}@}) is {@{a Python package that contains many functions for pwn}@}. To use it, {@{import from the Python package using `import pwn` (not `import pwntools`)}@}. To {@{help see what is going on by logging more info}@}, we can {@{set the `pwntools` log level to debug using `pwn.context.log_level = "debug"`}@}. To {@{encode an address as bytes (in little-endian form for x86 and x86-64)}@}, we can {@{use `pwn.p64(<address>) -> bytes`. For example, `pwn.p64(0xdeadbeeffacedead) == b'\xad\xde\xce\xfa\xef\xbe\xad\xde'`}@}. <!--SR:!2024-12-03,56,310!2024-12-06,59,310!2024-11-27,48,290!2024-12-07,60,310!2024-11-30,53,310!2024-12-24,68,310!2024-11-29,50,290-->

Using `gdb`, we can {@{find the address of a buffer (to find the addresses of the old `rbp` and old `rsp` in the stack) or a function (to find targets to jump to)}@}. To find the address of a local buffer in a function, we can use {@{`disassemble <address|function>` to disassemble a function and figure out the offset of a local buffer from the `rbp`}@}. (A quick note: The declaration order of local variables in C {@{do not necessarily correspond to their positions on the stack}@}.) To {@{find the address of a function}@}, use {@{the `info address <symbol>` command and replace `<symbol>` with the function name}@}. <!--SR:!2025-05-02,165,310!2024-12-24,68,310!2024-11-21,42,290!2024-11-21,42,290!2024-12-11,62,310-->

One more thing is that you may need to {@{exploit the binary running on a remote server as the flag is only available there}@}. In this case, {@{your `glibc` (GNU library for C) and `ld` (dynamic loader and linker) may differ from that on the server}@}. As a result, {@{function addresses (used as targets to be jumped to) may differ between your local machine and the remote server}@}, and {@{a successful exploitation on your local machine may fail on the remote server}@}. We can use {@{`patchelf`}@} to resolve this. First, {@{identify the `glibc` and `ld` version the remote server is using, and download said files from the remote server or elsewhere online}@}. Then, put the downloaded `glibc` (with the filename {@{`libc.so.6`}@}) and `ld` in the same folder as your ELF. Patch {@{the ELF to use the downloaded files instead of system ones (this directly modifies the ELF file, so copy the ELF file if you want to keep the original copy)}@}. Use the CLI options {@{`--set-interpreter <ld file>` and `--set-rpath <directory containing glibc>`}@}: <!--SR:!2025-03-17,125,290!2024-12-14,65,310!2025-02-01,102,290!2024-12-06,57,310!2024-12-05,56,310!2024-12-24,68,310!2024-12-05,58,310!2024-11-27,48,290!2024-11-27,48,290-->

```shell
patchelf --set-interpreter 'ld-<version>.so' 'my_elf' # This sets the dynamic loader and linker `ld` to the one in the current directory instead of the system one.
patchelf --set-rpath './' 'my_elf' # This sets the path to be searched for `glibc` to the current directory, so the `libc.so.6` in the current directory will be used isntead of the system one.
```

To {@{verify `patchelf` has successfully patched the executable}@}, run {@{`ldd <patched ELF file>`}@}. You should see {@{`libc.so.6` being linked (`=>`) to the one in the current directory, and `ld-<version>.so` in the current directory replacing (`=>`) the system one}@}. For example: <!--SR:!2025-04-21,156,310!2024-11-29,52,310!2025-03-17,132,310-->

```shell
$ ldd 'my_elf'
    linux-vdso.so.1 (0x00007ffe285e9000)
    libc.so.6 => ./libc.so.6 (0x00007ff0ffe00000)
    ./ld-2.23.so => /lib64/ld-linux-x86-64.so.2 (0x00007ff10050d000)
```

If so, you are good to go! Otherwise, try harder.

## protection

There are {@{protection schemes to inhibit exploitation of buffer overflow even if they exist}@}. We will talk about {@{two of them: [stack canaries](#stack%20canaries) and [address randomization](#address%20randomization)}@}. Of course, there is always the solution of {@{[avoiding buffer overflows](#avoiding%20buffer%20overflows) in the first place}@}. <!--SR:!2024-12-02,55,310!2024-12-24,68,310!2024-12-14,65,310-->

We should know these protection so that {@{we can bypass them in pwn challenges}@}. To see what protections has been enabled for an executale, {@{run the `pwndbg` command `checksec`}@}. It will print {@{a list of protections and their status, some of which are not introduced here and you will need to look them up yourself}@}. For example: <!--SR:!2024-12-09,60,310!2024-12-24,68,310!2024-11-22,43,290-->

```shell
pwndbg> checksec
[*] '/home/example/a folder/my_elf'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
```

### avoiding buffer overflows

The best way to avoid buffer overflows being exploited is {@{simply not have buffer overflows in the first place}@}. <!--SR:!2025-03-27,136,310-->

Recall unsafe C functions can lead to buffer overflows. There are {@{safe versions of them, usually named by appending `_s`, e.g. `gets_s`, `scanf_s`, `strcpy_s`}@}. They are safe because {@{they require an additional argument stating the buffer size (including the null terminator), and they will not attempt to write beyond the specified size}@}. However, if {@{the provided buffer size is larger than the actual buffer size}@}, then {@{buffer overflow is still possible}@}. For example: <!--SR:!2024-11-26,49,310!2025-02-08,90,270!2024-12-02,55,310!2024-11-23,46,290-->

```C
int buffer[4];
gets_s(buffer, 4); // Not vulnerable to buffer overflow.
gets_s(buffer, 3); // Still not vulnerable to buffer overflow.
gets_s(buffer, 5); // Vulnerable to buffer overflow, but you can only overflow by 1 byte.
```

### stack canaries

In the real world, canaries are birds used {@{to detect toxic gases in coal mines}@}. As {@{they are more sensitive to the toxic gases before humans}@}, {@{the birds would get sick before the humans}@}, allowing {@{the humans to avoid the toxic gases}@}. <!--SR:!2024-12-15,66,310!2024-12-24,68,310!2024-11-26,49,310!2025-05-06,168,310-->

In buffer overflow, stack canary is {@{a 32 or 64-bit value on top of the old `rip` and `rbp` but below the local variables in the stack}@}. The stack canary is {@{checked to be unmodified before returning from the function, printing an error and terminating the program if modified}@}. This inhibits {@{exploitation of buffer overflow because overwriting the old `rip` and `rbp` also involves overwriting the stack canary}@}. <!--SR:!2024-12-08,59,310!2024-12-24,68,310!2024-12-24,68,310-->

Usually, the stack canary is {@{random, so that the attacker cannot know the stack canary and very likely modifies the stack canary}@}. It is {@{unlikely the attacker can guess the canary as the stack canary has 64 or 56 of its bits random}@}. The stack canary can be {@{either fully random (_random canary_); or fully random except that its least significant bit (low address) is always the zero byte `\x00`, i.e. the null terminator (_terminator canary_); or XOR-ed with a piece of control data (_random XOR canary_)}@}. <!--SR:!2025-03-28,137,310!2024-12-17,68,310!2024-12-02,55,310-->

We will only discuss _terminator canary_ in more details. In particular, {@{many C string functions treat the null terminator as the end of string}@}. So if {@{an attacker were to read the canary value for exploitation}@}, {@{C string reading functions would read the null terminator at the low address and then stop, so the more significant bits of the canary value are unleaked}@}. Even if {@{the attacker knows the canary value to be written and include it in the payload}@}, {@{C string writing functions cannot write past the canary value because they would think the payload ends at the null terminator}@}. However, {@{non-string functions are not affected by the above, as they do not treat the null terminator specially}@}. <!--SR:!2025-03-15,131,310!2024-12-05,56,310!2024-12-24,68,310!2024-12-06,59,310!2024-11-23,46,290!2024-11-24,45,290-->

As mentioned above, stack canary can be bypassed {@{if you know the canary value and is able to write past the canary}@}. The canary value {@{may be obtained by another buffer overflow that causes the canary value to be leaked}@}. <!--SR:!2025-04-06,144,310!2024-12-02,55,310-->

### address randomization

Buffer overflow is often used to {@{jump to a particular function}@}. This can be inhibited if {@{the function addresses are randomized each time the program is executed}@}. Then {@{the attacker will need to find out the address of that particular function during that one program execution (does not work across execution)}@}. <!--SR:!2024-12-06,57,310!2024-11-22,43,290!2025-03-13,130,310-->

To do so, the executable must {@{consists of position-independent code (PIC), making the executable a position-independent executable (PIE)}@}. Said code {@{can work properly regardless of the code's base (start) address (thus cannot refer to absolute addresses)}@}. Then the technique of {@{address space layout randomization (ASLR)}@} can be applied. Usually, it will {@{randomize the base (start) address of the program (read-execute and read-write segment are treated as one segment for ASLR), the heap, and the stack}@}. However, {@{as only the base (start) address of segments are randomized}@}, {@{functions and data inside the same segment still have the same relative offset to each other}@}. <!--SR:!2024-12-08,59,310!2024-12-24,68,310!2024-12-06,57,310!2024-12-24,68,310!2024-12-07,60,310!2024-12-24,68,310-->

To bypass address randomization, we need to {@{know the exact versions of programs and libraries used}@}. Then, we {@{leak (obtain) the absolute address of any function or data in the same segment as the function we wanted to jump to}@}, perhaps {@{using another vulnerability}@}. Finally, {@{calculate the absolute address of the function we wanted to jump to using the relative offset, which can be found on the local machine, given the exact versions of programs and libraries are used}@}. <!--SR:!2024-12-10,61,310!2025-05-10,177,310!2024-11-30,53,310!2024-12-24,68,310-->

## next week notes

Next week, we will be teaching {@{decompilers. In particular, we will use Ghidra (URL: <https://github.com/NationalSecurityAgency/ghidra/releases>)}@}. <!--SR:!2024-12-06,59,310-->

Also, a general recommendation when analyzing a unknown executable is {@{analyze it in a virtual machine}@}, because {@{the unknown executable may be a malware}@}. <!--SR:!2024-11-30,53,310!2024-11-30,53,310-->
