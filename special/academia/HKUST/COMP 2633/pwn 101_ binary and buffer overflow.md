---
aliases:
  - Pwn 101
  - "Pwn 101: Binary and Buffer Overflow"
  - binary and buffer overflow
  - pwn 101
  - "pwn 101: binary and buffer overflow"
tags:
  - flashcard/active/special/academia/HKUST/COMP_2633/pwn_101__binary_and_buffer_overflow
  - language/in/English
---

# pwn 101: binary and buffer overflow

{@{__Pwn__, in a general context}@}, means {@{the domination of a player in a video game or argument, or the successful hacking of a website or computer}@}. In {@{CTFs}@}, it is {@{one of the major categories and usually refers to __binary exploitation__}@}. <!--SR:!2027-07-23,788,330!2026-12-24,625,330!2025-09-30,25,375!2025-09-30,25,375-->

{@{__Binary exploitation__}@} is about {@{finding vulnerabilities in a program binary, and then exploiting them}@}. To {@{find vulnerabilities without its source}@}, we need to {@{reverse the binary}@}, {@{the basics of which}@} are {@{taught in [reverse 101](reverse%20101_%20world%20of%20binaries.md)}@}, so it is recommended that {@{reverse is first learnt}@}. <!--SR:!2029-02-17,1252,350!2027-12-23,854,330!2025-09-29,24,375!2025-09-29,24,375!2025-09-30,25,375!2025-09-29,24,375!2025-09-30,25,375-->

{@{A quick recap of types of tools used for reverse}@}: {@{static analysis, dynamic analysis, and patching}@}. <!--SR:!2028-06-13,1057,350!2025-09-29,24,375-->

## memory model

What is a memory model? It refers to how {@{memory in a program is modelled by the OS}@}. In {@{the good o' days of computing}@}, memory address is {@{really the address of the physical memory}@}. But modern OSes do not do that. One of the many reasons is security: {@{consider that the physical memory is shared by all processes, it is insecure for one process to be able to access the memory of any other process, e.g. a password manager}@}. <!--SR:!2027-04-19,712,330!2026-11-26,603,330!2025-10-07,287,330!2027-05-25,729,330-->

Instead, modern OSes has the concept of {@{virtual memory}@}, which is managed by {@{a hardware called the memory management unit (MMU)}@}. To any single process, it looks like {@{there is still a "physical" memory}@}, but {@{the OS maps different parts of the "physical" memory to different parts of the actual physical memory, or even files on storage devices}@}! Some parts {@{may not be mapped (unmapped) at all, and accessing them will likely crash the program  (receive `SIGSEGV` signal)}@}. The mapping is {@{usually private to a single process, that is, that mapping is only used by that process and no other processes}@}. This is {@{good for security as a process can only access the memory of itself but not other processes}@}. <!--SR:!2027-07-31,796,330!2027-09-07,823,330!2028-07-14,1077,350!2026-07-27,500,310!2028-07-03,1074,350!2025-12-13,309,290!2027-07-15,780,330-->

However, further knowledge memory model is {@{not exactly important in basic pwn}@}. All one needs to know is that {@{parts of memory in a program are mapped to different parts of the actual physical memory or some files on storage devices}@}. <!--SR:!2027-08-27,813,330!2028-01-06,898,330-->

### memory mapping

For pwn, it is more important to know {@{the typical memory mapping for a process}@}. A memory mapping is {@{called a segment, not to be confused with sections, as a segment can contain multiple sections}@}. We will learn about {@{4 segments, in the order of low (small) address to high (large) address: read-execute segment, read-write segment, heap, and stack}@}. There may {@{or may not be unmapped space in between the segments}@}. Ignoring those space, {@{read-execute segment, read-write segment, and heap are very close together}@}. The heap {@{can dynamically grow upwards (increasing address) at runtime}@}, while others {@{usually cannot grow}@}. The stack {@{is very close to the highest address and can dynamically grow downwards (decreasing address) at runtime}@}. <!--SR:!2027-06-05,740,330!2028-05-05,1027,350!2025-10-03,290,330!2027-05-11,733,330!2028-11-25,1186,350!2025-09-28,285,330!2028-10-29,1165,350!2026-06-28,486,310-->

The meanings of the 4 segments are:

- read-execute segment ::@:: The segment that the program can read from and execute code on it. It usually contains the ELF header, `.rodata` (read-only data) and `.text` (code) sections in assembly. <!--SR:!2028-01-07,846,290!2027-05-21,725,330-->
- read-write segment ::@:: The segment that the program and read from and write to. It usually contains the `.bss` and `.data` sections in assembly. <!--SR:!2028-05-25,1044,350!2028-07-02,1073,350-->
- heap ::@:: It contains memory allocated at runtime. Usually, it is allocated for manual memory management (e.g. `malloc`, `new`). It grows upwards (increasing address). <!--SR:!2028-09-09,1126,350!2028-06-27,1068,350-->
- stack ::@:: It also contains memory allocated at runtime, but for small data (e.g., local variables) and also function-related data. Usually, it is allocated for automatic memory management (e.g. local variables). It grows downwards (decreasing address). <!--SR:!2027-02-07,601,310!2027-04-16,709,330-->

Note that the `.rodata` (read-only data) section is located on the read-execute segment. This means {@{the program can execute the data in `.rodata` section as code, which makes it less secure}@}. The linkers of some newer Linux distributions {@{add an additional one or two read segments (the program can only read from it) for the ELF header and `.rodata` section to improve security}@}. <!--SR:!2025-10-05,285,330!2025-10-05,285,330-->

## executable and linkable format

For pwn, it is also important to know {@{the overall structure of an executable and linkable format (ELF) file}@}. ELF files are commonly used on {@{UNIX (including Linux) systems}@}. <!--SR:!2028-07-25,1088,350!2028-12-12,1200,350-->

Like {@{many file formats}@}, an ELF file has {@{a ELF header indicating that it is an ELF file and the properties of it (32 or 64 bit, offsets, ...)}@}. Its magic number, i.e. {@{the bytes an ELF file must start with}@}, is {@{`0x7F 'E' 'L' 'F'`}@}. Additionally, an ELF file has {@{a program header table at the beginning of the file right after the ELF header, and a section header table at the end of the file}@}. <!--SR:!2027-06-10,745,330!2025-10-18,298,330!2028-06-07,1051,350!2027-05-24,728,330!2026-09-20,534,310-->

The program header table {@{specifies how the process image is created, i.e. how the OS should map the memory of the new process to the ELF, i.e. segment (not section) information}@}. The section header table {@{identifies all the sections in an ELF file}@}. Examples of sections are: {@{`.text`, `.data`, `.bss`, `.rodata` (read-only data), etc.}@} <!--SR:!2027-12-09,879,330!2028-08-04,1097,350!2028-03-13,985,350-->

## stack in x86 and x86-64 assembly

Revisiting reverse 101... We will use {@{the Intel syntax}@} here. <!--SR:!2027-05-30,734,330-->

In x86 and x86-64, there are {@{two registers related to the stack: `esp`/`rsp` and `ebp`/`rbp`}@}. (We will use the x86-64 registers thereafter.) <!--SR:!2026-11-17,601,330-->

`rsp` is {@{the stack pointer, which points to the top (low address) of the stack memory}@}. This is easy to understand. The more difficult one is {@{`rbp`, which is the stack/function frame base pointer, which points to the bottom (high address) of the current stack/function frame}@}. Yet we do not know {@{what a stack/function frame is, and this will be introduced later}@}. <!--SR:!2028-09-11,1128,350!2027-05-12,734,330!2028-06-14,1058,350-->

There are {@{several instructions that modify the stack memory and the `rsp` and `rbp` registers appropriately}@}. Some of them are: {@{`push`, `pop`, `call`, `ret`, and `leave`}@}. <!--SR:!2028-01-26,915,330!2025-10-15,295,330-->

- `push <src>` ::@:: Push `<src>` on top of the stack. This writes a value right below the address pointed by `rsp` and decrements `rsp`. <!--SR:!2029-01-01,1216,350!2028-06-28,1069,350-->
- `pop <dest>` ::@:: Pop the top of the stack and write it to `<dest>`. This reads a value at the address pointed by `rsp` and increments `rsp`. <!--SR:!2025-10-06,293,330!2027-09-26,832,330-->
- `call <address>` ::@:: This pushes (`push`) the `rip` (instruction pointer, pointing to the currently executing instruction) onto the stack, and then jumps (`jmp`) to `<address>`. `<address>`. This is usually used to call a function, in conjunction with `ret`. <!--SR:!2025-10-06,286,330!2028-10-09,1147,350-->
- `ret`::@:: This pops (`pop`) a value off from the stack and jumps (`jmp`) to it. (Note that this is similar to `pop rip`, but `pop rip` is invalid because `rip` cannot be modified directly.) This is usually used to return from a function, in conjunction with `call`. <!--SR:!2029-01-06,1220,350!2028-03-08,923,310-->
- `leave` ::@:: This sets `rsp` to `rbp`, effectively clearing the current stack frame. Then it pops (`pop`) a value off from the stack to `rbp`. This effectively restores the previous stack frame (the state right before the current function is called (`call`)). This is usually used to cleanup the stack and registers just before returning from a function (`ret`). <!--SR:!2027-01-02,586,310!2026-02-03,335,290-->

A related instruction is {@{`lea`}@}: <!--SR:!2025-10-01,288,330-->

- `lea <dest>, <src>` ::@:: <u>L</u>oad <u>e</u>ffective <u>a</u>ddress. This sets `<dest>` to the memory address of `<src>` (instead of the value at `<src>`). It can be used with memory references to perform arithmetic operations on memory addresses. (In fact, `lea` can be exploited to do addition and multiplication of unsigned integers.) <!--SR:!2028-11-03,1171,350!2028-10-19,1157,350-->

Since `lea` can {@{mostly be replaced with `add` and `imul` (with the exception of flags)}@}, a natural question is {@{why is there a `lea` instruction in the first place}@}? Apart from {@{`lea` not setting some flags}@}, it is also {@{convenient for implementing array access}@}. Further reading: <https://stackoverflow.com/q/1658294>. <!--SR:!2027-03-02,679,330!2028-01-24,946,350!2028-11-24,1188,350!2025-10-13,293,330-->

## calling convention

The instructions above are used to {@{implementing the concept of functions in assembly}@}. However, they {@{do not specify how they should be used}@}. A __calling convention__ specifies {@{how the above instructions are used to manipulate the stack in such a way to represent functions}@}. It is called a _convention_ because {@{the caller and callee (the function to be called by the caller) needs to follow the same (or compatible) calling conventions}@}, or otherwise {@{the stack will be manipulated incorrectly, and the program will likely crash}@}. <!--SR:!2028-11-28,1191,350!2027-06-29,764,330!2027-07-08,763,330!2028-12-13,1201,350!2029-02-16,1252,350-->

There are {@{many different incompatible calling conventions in use}@}. For x86, {@{there are many different ones, but for x86-64, there are only 2 common in use}@}. They are {@{the Microsoft x64 calling convention and the System V AMD64 ABI}@}. We will {@{only introduce a calling convention for x86-64, as the binaries you encounter in CTFs are most likely 64-bit, and that calling convention is the latter one because we are using Linux}@}. Further, you should be able to {@{extract the general principles of calling conventions from the example below and extrapolate them to others}@}. <!--SR:!2025-10-17,297,330!2028-01-06,928,350!2028-10-02,1140,350!2028-02-11,961,350!2028-06-20,1063,350-->

### System V AMD64 ABI

The complete calling convention {@{would be too much to discuss here, so we will only discuss a (rather small) part of it}@}. Some parts of the process may {@{be optimized away by the compiler}@}. To avoid this, {@{pass `-O0` (for GCC) to disable optimization}@}. <!--SR:!2027-02-28,676,330!2029-03-23,1281,350!2027-06-24,759,330-->

A stack/function frame is {@{a portion of the stack that belongs to one function only}@}. Each time {@{one calls a function}@}, {@{a stack/function frame is added on top of the old one}@}. Each time {@{one returns from a function}@}, {@{the current stack/function frame is cleared and the old (the frame for the callee) is restored}@}. `rsp` and `rbp` then refers to {@{respectively the top and the bottom of the topmost stack/function frame (so the current function frame is in between `rsp` and `rbp`)}@}. <!--SR:!2025-10-07,294,330!2027-03-16,690,330!2028-04-17,1009,350!2025-10-08,295,330!2025-10-14,294,330!2027-08-05,791,330-->

The detail process of creating a stack frame is {@{pushing `rbp` onto the stack (decrementing `rsp` at the same time) (`push rbp`), and then set `rbp` to `rsp` (`mov rbp rsp`)}@}. One may then note that {@{the current stack/function frame is empty as `rsp` equals `rbp`}@}. Reversing the above operations, i.e. {@{popping a value, previously pushed by `push rbp`, from the stack (incrementing `rsp` at the same time) and storing it to `rbp` (`pop rbp`)}@}, {@{restores the previous stack frame, given the current stack frame is empty}@}. If the current stack frame is {@{nonempty (`rsp` not equals `rbp`)}@}, then {@{simply clear the current stack frame by setting `rsp` to `rbp` (`mov rsp rbp`)}@}. These two operations are so common that {@{the operations have dedicated instructions respectively called `enter` and `leave`}@}. In practice, {@{`enter` has horrible performance so compilers almost always emit `push` and `mov` instead of a single `enter` instruction}@}, but {@{`leave` has okay performance and compilers may emit a single `leave` instruction instead of `mov` and `pop`}@}. <!--SR:!2027-06-30,755,330!2027-07-21,776,330!2027-03-06,681,330!2026-10-23,560,310!2028-05-10,1029,350!2027-05-05,728,330!2028-03-22,992,350!2028-11-09,1174,350!2028-08-21,1110,350-->

In System V AMD64 ABI, the process of creating and destroying a stack frame are {@{both done inside the callee}@}. The caller is responsible for {@{passing the arguments before calling the function and cleaning up the passed arguments after calling the function}@}. <!--SR:!2025-09-26,283,330!2026-11-18,598,330-->

The above only describes how a stack frame is created or destroyed. The missing thing is {@{how arguments and return value are passed}@}. Arguments are passed {@{using registers, and also the stack if there are too many arguments or the arguments are too large in size}@}. To {@{describe how arguments of any type are passed}@} is too complicated here, so we will {@{only consider passing 64-bit integers or pointers}@}. The first 6 arguments goes into {@{the registers, in order, `rdi`, `rsi`, `rdx`, `rcx`, `r8`, and `r9`}@}. The rest are {@{pushed onto the stack before calling the function (`call`)}@}. The return value is {@{also passed using registers}@}. If {@{the return value is within 64 bits, then `rax` is used, or if within 128 bits, then `rdx:rax` is used}@}. Otherwise, {@{the caller will provide a space to store the return value and pass a pointer to that space as the 1st argument, shifting all other arguments by 1}@}. The passed pointer will {@{be written to `rax` by the callee just before returning (`ret`)}@}. An important note is that {@{the argument order does not necessarily match that in the high-level programming language}@}. When C code is compiled with System V AMD64 ABI in GCC, while {@{the first 6 arguments are assigned left to right, the remaining arguments are pushed from right to left \(rightmost argument is pushed first\)}@}. <!--SR:!2025-10-09,289,330!2027-05-02,725,330!2026-01-24,332,290!2028-11-25,1189,350!2027-07-18,773,330!2027-06-04,739,330!2025-10-06,286,330!2027-06-03,738,330!2027-12-26,923,350!2027-07-18,783,330!2028-07-28,1091,350!2026-02-01,331,290-->

To summarize, the process of calling a function is: {@{passing the arguments, calling the function (`call`), creating a stack frame, doing stuff and setting the return value, restoring the previous stack frame, returning from the function (`ret`), and finally cleaning up the passed arguments}@}. <!--SR:!2026-09-27,537,310-->

## GNU Debugger and pwndbg

To {@{see the registers and the stack while running a program}@}, we will use {@{the GNU Debugger (`gdb`), which is only available on Linux}@}. But {@{the debugger is sometimes rather inconvenient to use for pwn}@}, so we will also use {@{a `gdb` plugin called `pwndbg` (URL: <https://github.com/pwndbg/pwndbg>)}@}. It {@{adds additional commands}@}, and {@{improve existing commands and views}@}. These should make it {@{easier to solve pwn challenges}@}. Install both of them first. <!--SR:!2027-08-17,803,330!2026-01-24,366,310!2028-07-17,1080,350!2025-10-12,292,330!2027-10-29,813,330!2026-01-09,120,392!2026-01-09,120,392-->

Let's learn some basic `gdb` commands (not exclusive to `pwndbg`):

- `apropos <regex>` ::@:: find text matching `<regex>` in the manual <!--SR:!2028-10-12,1150,350!2025-10-10,290,330-->
- `help [<topic>]` ::@:: find information about topic; if topic is not specified, then prints general help <!--SR:!2025-10-11,291,330!2028-11-27,1187,350-->
- `file <path>` ::@:: load binary file to debug <!--SR:!2029-02-22,1256,350!2025-10-18,298,330-->
- `run [<args>...]` ::@:: run program (with args) <!--SR:!2028-10-27,1165,350!2027-04-04,704,330-->
- `set args <args>...` ::@:: set program args <!--SR:!2029-03-29,1286,350!2027-08-25,811,330-->
- `starti [<args>...]` ::@:: start program and stop at its first instruction <!--SR:!2025-10-06,293,330!2025-10-16,296,330-->
- `disassemble <address|function>` ::@:: disassemble a specified address or function <!--SR:!2028-02-17,965,350!2025-10-12,292,330-->
- `break <where>` ::@:: set a breakpoint <!--SR:!2025-10-08,288,330!2028-02-11,960,350-->
- `delete [<breakpoint>]` ::@:: delete a breakpoint; if breakpoint is not specified, then delete all breakpoints <!--SR:!2025-10-10,290,330!2028-03-01,976,350-->
- `info address <symbol>` ::@:: print the `<symbol>` (which can be a function name), its type, and its address <!--SR:!2028-11-03,1169,350!2025-10-07,294,330-->
- `info breakpoints|regs|threads`::@:: list breakpoints, register values, or threads <!--SR:!2025-10-16,296,330!2025-10-13,293,330-->
- `backtrace` ::@:: print backtrace or call stack <!--SR:!2028-08-18,1111,350!2028-10-16,1154,350-->
- `ni` ::@:: go to the next instruction <!--SR:!2027-10-13,849,330!2028-05-24,1043,350-->
- `si` ::@:: go to the next instruction stepping into functions <!--SR:!2027-06-26,751,330!2029-01-29,1238,350-->
- `continue` ::@:: continue program execution <!--SR:!2028-06-15,1059,350!2025-10-15,295,330-->
- `finish` ::@:: run until the current function returns <!--SR:!2025-10-11,291,330!2028-10-13,1151,350-->
- `x/<format> <address>` ::@:: examine memory at the given address in the given format (see `help x`) <!--SR:!2028-08-16,1105,350!2025-10-17,297,330-->
- `print <expression>` ::@:: evaluate and print an expression <!--SR:!2025-10-05,285,330!2028-09-17,1133,350-->
- `record` ::@:: record execution of every instruction; can make the process run slowly <!--SR:!2025-10-18,298,330!2028-06-19,1062,350-->
- `rni` ::@:: rewind to the previous instruction <!--SR:!2028-12-03,1194,350!2028-07-09,1072,350-->
- `rsi` ::@:: rewind to the previous instruction stepping into functions <!--SR:!2026-09-19,533,310!2028-08-26,1115,350-->
- `rc` ::@:: reverse continue <!--SR:!2028-01-23,945,350!2028-07-10,1073,350-->
- `set <storage> = <value>` ::@:: set storage to value <!--SR:!2029-04-02,1288,350!2028-03-30,997,350-->

Let's also learn some basic `pwndbg` commands:

- `down` ::@:: move down the backtrace or call stack <!--SR:!2028-09-23,1136,350!2028-07-16,1079,350-->
- `up` ::@:: move up the backtrace or call stack <!--SR:!2028-12-01,1192,350!2028-08-27,1116,350-->
- `checksec` ::@:: print the binary security settings <!--SR:!2029-01-25,1233,350!2028-12-09,1200,350-->
- `stack <count> <offset>` ::@:: prints stack data with the specified count and offset <!--SR:!2029-01-11,1223,350!2027-07-16,781,330-->
- `vmmap [<address|name>]` ::@:: display memory mappings information (filtered binary address or name) <!--SR:!2025-10-04,291,330!2026-10-08,560,310-->

Commands names can be {@{truncated at the end to produce an abbreviation if the abbreviation is unambiguous, i.e. there is only exactly one command name starting with the abbreviation}@}. For example, `disassemble` can be {@{abbreviated to `disass` or the uglier `disassem`}@}. <!--SR:!2027-08-03,789,330!2025-10-06,286,330-->

## buffer overflow

A buffer is {@{simply a portion of the memory used to store the data}@}. As {@{real computers have limited memory}@}, the buffer is {@{also limited in its size}@}. The buffer may be on {@{the stack, the heap, read-write segment, read-execute segment, or really anywhere the memory is mapped by the OS}@}. A buffer is {@{usually contagious, that is, it is a continuous portion of the memory}@}, so we can identify a buffer by {@{its low (start) address (inclusive) and high (end) address (exclusive)}@}. <!--SR:!2025-10-11,291,330!2027-09-11,828,330!2027-10-20,849,330!2026-03-17,377,310!2027-05-04,727,330!2028-03-28,997,350-->

The buffers we are usually interested in exploiting is {@{usually on the first three \(stack, heap, read-write segment\)}@} because we can {@{write to the buffer}@}. We will only {@{focus on buffers on the stack because they are the easiest to exploit}@}. <!--SR:!2028-02-19,894,330!2027-06-11,746,330!2025-10-12,24,377-->

Buffer overflow, then, is {@{simply writing data outside the buffer}@}. Assume the buffer is {@{on the stack}@}. This is likely to {@{overwrite data on other unrelated buffers in the stack, corrupting them}@}. Usually, this {@{results in a program crash}@}. However, if we use buffer overflow to {@{write data to specific locations outside the buffer with specific values}@}, then we can {@{manipulate the program to do unintended things}@}. In CTFs, {@{this is used to find the flag in pwn challenges}@}. <!--SR:!2028-05-14,1033,350!2028-12-04,1195,350!2028-03-12,984,350!2028-09-07,1125,350!2028-09-02,1122,350!2028-04-26,1018,350!2028-11-24,1185,350-->

There are many ways to {@{manipulate the program using buffer overflow}@}, and we will {@{talk about only one interesting way related to function calls}@}. Recall that calling a function via `call` {@{pushes the address to jump to (the next instruction after `call` in the memory) after the function finishes to the stack}@}, and that the function returns {@{via `ret`, which pops the address that we have pushed before calling the function from the stack and jumps back to it, finishing the function call}@}. Using buffer overflow, we can {@{write to that location in the stack and change it to any value we want}@}. Then, when {@{the functions returns via `ret`}@}, instead of {@{jumping back to the caller, it jumps to an arbitrary location that we can freely specify}@}. <!--SR:!2025-10-19,299,330!2027-01-26,651,330!2026-10-05,560,310!2025-12-23,302,290!2028-05-30,1048,350!2028-05-23,1042,350!2026-01-13,372,349-->

### finding buffer overflows

The most common way buffer overflow occurs is {@{not checking the whether the location in the buffer to be written to}@}. This may be {@{a programming error like a off-by-one error}@}: <!--SR:!2025-10-19,299,330!2027-07-06,771,330-->

```C
int buffer[4]; // Only `buffer[0]`, `buffer[1]`, `buffer[2]`, and `buffer[3]` are within `buffer`.
for (size_t idx = 0; idx <= 4; ++idx) { // Notice the `<=`.
  buffer[idx] = 42; // `idx` can be 4, which will cause this statement to write past the end of `buffer`.
}
```

The above example demonstrates how buffer overflow actually happens. The cases we are usually more interested in is {@{unsafe C string functions that accepts inputs (best if they can be provided by the user directly or indirectly) and writes to other buffers}@}, such as {@{`gets`, `scanf`, `strcpy`, etc.}@} These functions are vulnerable because {@{they will write to the buffer as long as there is data in the input without taking the buffer size into consideration at all}@}. So if {@{the input data is too large to be fit into the destination buffers}@}, then {@{a buffer overflow occurs as the excess data is written past the end of the destination buffers}@}, similar to the example above. An example: <!--SR:!2027-09-19,819,330!2028-08-13,1107,350!2027-03-14,694,330!2027-08-18,804,330!2025-10-05,292,330-->

```C
char buffer[4];
gets(buffer); // This prompts for user input. If the user input is longer than 3 characters (4 characters including the null terminator), then a buffer overflow occurs.
scanf("%s", buffer); // Same as above.
```

By now, you should have figured out how to identify code that is vulnerable to buffer overflow.

#### exploiting buffer overflows

Once you have found code that is vulnerable to buffer overflows, {@{identify what special locations you want to overwrite with what values}@}. For example, {@{overwriting the address in the stack that `ret` will jump to with another address pointing to another function}@}. Then simply {@{craft the data required and pass it to the program}@}. One needs to note that {@{the stack grows in decreasing address}@}, while {@{the above functions write to the buffer in increasing address (from low to high address)}@}, so writing beyond a buffer {@{traverses the stack downwards (items pushed less recently) instead of upwards (items pushed more recently)}@}. Food for thought: What if {@{the stack grows in increasing address}@}? <!--SR:!2027-07-24,789,330!2027-07-07,772,330!2025-09-27,284,330!2028-10-26,1164,350!2027-08-26,812,330!2026-12-01,606,330!2028-04-27,1019,350-->

To help with this process, there are {@{some tools available}@}. Three tools are {@{`pwntools`, `gdb`, and `patchelf`}@}. <!--SR:!2025-10-10,297,330!2025-10-11,298,330-->

`pwntools` (URL: {@{<https://github.com/Gallopsled/pwntools>}@}) is {@{a Python package that contains many functions for pwn}@}. To use it, {@{import from the Python package using `import pwn` (not `import pwntools`)}@}. To {@{help see what is going on by logging more info}@}, we can {@{set the `pwntools` log level to debug using `pwn.context.log_level = "debug"`}@}. To {@{encode an address as bytes (in little-endian form for x86 and x86-64)}@}, we can {@{use `pwn.p64(<address>) -> bytes`. For example, `pwn.p64(0xdeadbeeffacedead) == b'\xad\xde\xce\xfa\xef\xbe\xad\xde'`}@}. <!--SR:!2028-08-26,1115,350!2028-11-11,1177,350!2027-09-27,833,330!2028-12-10,1201,350!2027-05-07,711,330!2025-10-08,288,330!2027-11-23,883,330-->

Using `gdb`, we can {@{find the address of a buffer (to find the addresses of the old `rbp` and old `rsp` in the stack) or a function (to find targets to jump to)}@}. To find the address of a local buffer in a function, we can use {@{`disassemble <address|function>` to disassemble a function and figure out the offset of a local buffer from the `rbp`}@}. (A quick note: The declaration order of local variables in C {@{do not necessarily correspond to their positions on the stack}@}.) To {@{find the address of a function}@}, use {@{the `info address <symbol>` command and replace `<symbol>` with the function name}@}. <!--SR:!2027-04-15,708,330!2027-12-31,892,330!2027-06-02,737,330!2027-05-29,733,330!2029-01-17,1228,350-->

One more thing is that you may need to {@{exploit the binary running on a remote server as the flag is only available there}@}. In this case, {@{your `glibc` (GNU library for C) and `ld` (dynamic loader and linker) may differ from that on the server}@}. As a result, {@{function addresses (used as targets to be jumped to) may differ between your local machine and the remote server}@}, and {@{a successful exploitation on your local machine may fail on the remote server}@}. We can use {@{`patchelf`}@} to resolve this. First, {@{identify the `glibc` and `ld` version the remote server is using, and download said files from the remote server or elsewhere online}@}. Then, put the downloaded `glibc` (with the filename {@{`libc.so.6`}@}) and `ld` in the same folder as your ELF. Patch {@{the ELF to use the downloaded files instead of system ones (this directly modifies the ELF file, so copy the ELF file if you want to keep the original copy)}@}. Use the CLI options {@{`--set-interpreter <ld file>` and `--set-rpath <directory containing glibc>`}@}: <!--SR:!2026-08-04,504,310!2029-04-04,1289,350!2025-11-29,301,290!2028-09-04,1122,350!2028-07-23,1086,350!2028-01-11,903,330!2028-10-06,1149,350!2027-09-03,819,330!2026-11-02,564,310-->

```shell
patchelf --set-interpreter 'ld-<version>.so' 'my_elf' # This sets the dynamic loader and linker `ld` to the one in the current directory instead of the system one.
patchelf --set-rpath './' 'my_elf' # This sets the path to be searched for `glibc` to the current directory, so the `libc.so.6` in the current directory will be used isntead of the system one.
```

To {@{verify `patchelf` has successfully patched the executable}@}, run {@{`ldd <patched ELF file>`}@}. You should see {@{`libc.so.6` being linked (`=>`) to the one in the current directory, and `ld-<version>.so` in the current directory replacing (`=>`) the system one}@}. For example: <!--SR:!2027-02-19,668,330!2028-04-16,1008,350!2026-05-08,416,310-->

```shell
$ ldd 'my_elf'
    linux-vdso.so.1 (0x00007ffe285e9000)
    libc.so.6 => ./libc.so.6 (0x00007ff0ffe00000)
    ./ld-2.23.so => /lib64/ld-linux-x86-64.so.2 (0x00007ff10050d000)
```

If so, you are good to go! Otherwise, try harder.

## protection

There are {@{protection schemes to inhibit exploitation of buffer overflow even if they exist}@}. We will talk about {@{two of them: [stack canaries](#stack%20canaries) and [address randomization](#address%20randomization)}@}. Of course, there is always the solution of {@{[avoiding buffer overflows](#avoiding%20buffer%20overflows) in the first place}@}. <!--SR:!2028-07-19,1082,350!2028-01-24,913,330!2025-09-25,285,330-->

We should know these protection so that {@{we can bypass them in pwn challenges}@}. To see what protections has been enabled for an executale, {@{run the `pwndbg` command `checksec`}@}. It will print {@{a list of protections and their status, some of which are not introduced here and you will need to look them up yourself}@}. For example: <!--SR:!2028-12-02,1191,350!2025-10-19,299,330!2027-06-16,751,330-->

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

The best way to avoid buffer overflows being exploited is {@{simply not have buffer overflows in the first place}@}. <!--SR:!2026-10-31,583,330-->

Recall unsafe C functions can lead to buffer overflows. There are {@{safe versions of them, usually named by appending `_s`, e.g. `gets_s`, `scanf_s`, `strcpy_s`}@}. They are safe because {@{they require an additional argument stating the buffer size (including the null terminator), and they will not attempt to write beyond the specified size}@}. However, if {@{the provided buffer size is larger than the actual buffer size}@}, then {@{buffer overflow is still possible}@}. For example: <!--SR:!2028-01-29,950,350!2026-01-18,344,290!2028-08-02,1096,350!2027-08-19,805,330-->

```C
int buffer[4];
gets_s(buffer, 4); // Not vulnerable to buffer overflow.
gets_s(buffer, 3); // Still not vulnerable to buffer overflow.
gets_s(buffer, 5); // Vulnerable to buffer overflow, but you can only overflow by 1 byte.
```

### stack canaries

In the real world, canaries are birds used {@{to detect toxic gases in coal mines}@}. As {@{they are more sensitive to the toxic gases before humans}@}, {@{the birds would get sick before the humans}@}, allowing {@{the humans to avoid the toxic gases}@}. <!--SR:!2025-10-02,289,330!2025-10-13,293,330!2028-02-08,959,350!2027-04-28,721,330-->

In buffer overflow, stack canary is {@{a 32 or 64-bit value on top of the old `rip` and `rbp` but below the local variables in the stack}@}. The stack canary is {@{checked to be unmodified before returning from the function, printing an error and terminating the program if modified}@}. This inhibits {@{exploitation of buffer overflow because overwriting the old `rip` and `rbp` also involves overwriting the stack canary}@}. <!--SR:!2027-12-27,855,330!2025-10-10,290,330!2025-10-07,287,330-->

Usually, the stack canary is {@{random, so that the attacker cannot know the stack canary and very likely modifies the stack canary}@}. It is {@{unlikely the attacker can guess the canary as the stack canary has 64 or 56 of its bits random}@}. The stack canary can be {@{either fully random (_random canary_); or fully random except that its least significant bit (low address) is always the zero byte `\x00`, i.e. the null terminator (_terminator canary_); or XOR-ed with a piece of control data (_random XOR canary_)}@}. <!--SR:!2026-11-08,590,330!2025-10-09,296,330!2026-11-11,534,310-->

We will only discuss _terminator canary_ in more details. In particular, {@{many C string functions treat the null terminator as the end of string}@}. So if {@{an attacker were to read the canary value for exploitation}@}, {@{C string reading functions would read the null terminator at the low address and then stop, so the more significant bits of the canary value are unleaked}@}. Even if {@{the attacker knows the canary value to be written and include it in the payload}@}, {@{C string writing functions cannot write past the canary value because they would think the payload ends at the null terminator}@}. However, {@{non-string functions are not affected by the above, as they do not treat the null terminator specially}@}. <!--SR:!2026-10-04,568,330!2028-09-05,1123,350!2025-10-14,294,330!2028-10-17,1155,350!2027-07-20,785,330!2027-07-19,784,330-->

As mentioned above, stack canary can be bypassed {@{if you know the canary value and is able to write past the canary}@}. The canary value {@{may be obtained by another buffer overflow that causes the canary value to be leaked}@}. <!--SR:!2026-12-16,617,330!2028-07-30,1093,350-->

### address randomization

Buffer overflow is often used to {@{jump to a particular function}@}. This can be inhibited if {@{the function addresses are randomized each time the program is executed}@}. Then {@{the attacker will need to find out the address of that particular function during that one program execution (does not work across execution)}@}. <!--SR:!2028-09-18,1132,350!2027-06-15,750,330!2026-09-22,558,330-->

To do so, the executable must {@{consists of position-independent code (PIC), making the executable a position-independent executable (PIE)}@}. Said code {@{can work properly regardless of the code's base (start) address (thus cannot refer to absolute addresses)}@}. Then the technique of {@{address space layout randomization (ASLR)}@} can be applied. Usually, it will {@{randomize the base (start) address of the program (read-execute and read-write segment are treated as one segment for ASLR), the heap, and the stack}@}. However, {@{as only the base (start) address of segments are randomized}@}, {@{functions and data inside the same segment still have the same relative offset to each other}@}. <!--SR:!2027-08-22,797,330!2025-10-12,292,330!2028-09-12,1127,350!2025-10-09,289,330!2028-11-29,1192,350!2025-10-09,289,330-->

To bypass address randomization, we need to {@{know the exact versions of programs and libraries used}@}. Then, we {@{leak (obtain) the absolute address of any function or data in the same segment as the function we wanted to jump to}@}, perhaps {@{using another vulnerability}@}. Finally, {@{calculate the absolute address of the function we wanted to jump to using the relative offset, which can be found on the local machine, given the exact versions of programs and libraries are used}@}. <!--SR:!2028-12-17,1204,350!2027-06-23,758,330!2028-05-09,1028,350!2025-10-14,294,330-->

## next week notes

Next week, we will be teaching {@{decompilers. In particular, we will use Ghidra (URL: <https://github.com/NationalSecurityAgency/ghidra/releases>)}@}. <!--SR:!2028-11-19,1184,350-->

Also, a general recommendation when analyzing a unknown executable is {@{analyze it in a virtual machine}@}, because {@{the unknown executable may be a malware}@}. <!--SR:!2028-05-06,1028,350!2028-05-13,1032,350-->
