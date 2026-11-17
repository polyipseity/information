---
aliases:
  - COMP 3511 lab 2
  - HKUST COMP 3511 lab 2
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/labs/lab_2/lab
  - language/in/English
---

# lab

- HKUST COMP 3511 lab 2
- parent: [lab 2](index.md)

## why operating systems are written in C

Most operating systems are written in C, which gives the programmer precise control of the hardware. A kernel sets a register, reads a device buffer and walks a page table; no language runtime decides where those objects live. The standard C library is the interface to the system calls of UNIX and Linux, so a program asks the kernel for a service by calling a C function.

---

Flashcards for this section are as follows:

- why most operating systems are written in C ::@:: C gives the programmer precise control of the underlying hardware
- what the standard C library is on UNIX and Linux ::@:: the interface to the system calls, so a program requests a kernel service by calling a C function

## data types of fixed width

Every C data type has a fixed size in bits, which lets a C program describe a hardware register or a file field exactly. Three families cover the language: primary types such as `int`, `char` and `float`; derived types built from them, such as pointers, arrays and functions; and user-defined types, which the programmer names. `sizeof` reports the width of any type in bytes.

---

Flashcards for this section are as follows:

- three families of C data type ::@:: primary types, derived types such as pointers and arrays, and user-defined types
- what lets a C program describe a hardware register exactly ::@:: every C data type has a fixed size in bits
- operator that reports the size of a type or a variable in bytes ::@:: `sizeof` reports that width

## pointers and addresses

C passes every argument by value, so a function receives a copy. A swap on two plain integers cannot reach the caller's variables, so they keep their values. Passing the addresses reaches the originals, and a pointer holds one such address in virtual memory.

In a declaration, `*` marks a pointer. In an expression it reads the value at that address; `&` gives the address of a variable.

```c
#include <stdio.h>

int outer_a = 7;
int b = 1;

void swapInt(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

int main()
{
    int a = outer_a;
    int b = 100 + 200 / 10 - 3 * 10;
    printf("Before: %d %d\n", a, b);
    swapInt(&a, &b);
    printf("After : %d %d\n", a, b);
    return 0;
}
```

```text
Before: 7 90
After : 90 7
```

The local `b` takes its value from an expression, so the global `b = 1` never enters the swap. Division and multiplication run first: `200 / 10` is 20, `3 * 10` is 30, and 100 + 20 - 30 makes 90. The local shadows the global, which keeps its value 1 while the printed local starts at 90.

---

Flashcards for this section are as follows:

- what a pointer holds ::@:: the address in virtual memory of a variable
- meaning of `*` in a pointer declaration and in an expression ::@:: in a declaration it marks a pointer, and in an expression it reads the value at that address
- operator that produces the address of a variable ::@:: `&`, the address-of operator
- why `swapInt` takes two pointers ::@:: C passes arguments by value, so a swap on copies would leave the caller's variables unchanged
- value of the local `b` after `int b = 100 + 200 / 10 - 3 * 10;` ::@:: `90`, because division and multiplication run first
- value of the global `b = 1` after `swapInt(&a, &b)` returns ::@:: `1`, because the local `b` shadows the global and the swap reaches only the local one

## structs and heap memory

A `struct` declares a composite type whose members sit together in one block, in declaration order. The type holds no methods, so an operation on one is a separate function taking it as an argument.

```c
struct IntPair {
    int first, second;
};

int IntPair_sum(struct IntPair pair)
{
    return pair.first + pair.second;
}
```

Heap memory comes from `malloc` and goes back through `free`; `<stdlib.h>` declares both. Each allocation states its size, which is why these `sizeof` calls name a type.

```c
#include <stdlib.h>

struct IntPair {
    int first, second;
};

int main()
{
    int *intVar = malloc(sizeof(int));
    int *intArr = malloc(sizeof(int) * 100);
    struct IntPair *intPair = malloc(sizeof(struct IntPair));

    free(intVar);
    free(intArr);
    free(intPair);
    return 0;
}
```

---

Flashcards for this section are as follows:

- how a `struct` places its members in memory ::@:: together in one block, in the order they are declared
- function that returns heap memory to the system, and the header that declares it ::@:: `free`, declared in `<stdlib.h>` beside `malloc`
- what `malloc(sizeof(struct IntPair))` reserves ::@:: room for one `struct IntPair`, with a pointer to that block returned
- how an operation on a struct is written in C ::@:: as a separate function that takes the struct as an argument

## strings as character arrays

A C string is a character array that ends with the null character `'\0'`. Nothing else marks the end, so a loop walks the array until it meets that character. `strcpy` copies one string into an array, terminator included; `<string.h>` declares it.

```c
#include <stdio.h>
#include <string.h>

int main()
{
    char str[100];
    strcpy(str, "Hello World!");

    int i = 0;
    while (str[i] != '\0' && i < 100)
        i++;
    printf("Last char: %c\n", str[i-1]);

    return 0;
}
```

```text
Last char: !
```

The loop carries a second condition, `i < 100`, because a string that lost its terminator would be read past the end of the array; the scan stops at whichever comes first. That also leaves `i` on the terminator, so the program prints `str[i - 1]` and the last character sits one place back.

`sscanf` reads fields out of a string with the same format rules `scanf` applies to input, so a line of text splits without a file.

```c
#include <stdio.h>
#include <string.h>

int main()
{
    char line[100], linuxText[20], machineName[20], kernelText[50];
    int kernelMajor, kernelMinor;

    strcpy(line, "Linux csl2wk21 5.14.0-687.42.1.el9_8.x86_64");
    sscanf(line, "%s %s %s", linuxText, machineName, kernelText);
    sscanf(kernelText, "%d.%d", &kernelMajor, &kernelMinor);
    printf("Version: %d.%d\n", kernelMajor, kernelMinor);

    return 0;
}
```

```text
Version: 5.14
```

The first call fills three arrays with the three words of the line. The second reads two integers out of the version word: each `%d` stops at the first non-digit, so the build string after `5.14` stays behind.

---

Flashcards for this section are as follows:

- character that ends a C string ::@:: the null character `'\0'`
- function that copies one C string into a character array, and the header that declares it ::@:: `strcpy`, declared in `<string.h>`
- why the scanning loop of `str_demo.c` tests `i < 100` as well as the terminator ::@:: a string that lost its terminator would be read past the end of the array, so the loop stops at whichever is first
- why `str_demo.c` prints `str[i - 1]` rather than `str[i]` ::@:: the scan stops with `i` on the terminator, so the last character sits one place back
- function that reads fields out of a C string with format rules ::@:: `sscanf`, which applies the same rules as input
- what `sscanf(line, "%s %s %s", linuxText, machineName, kernelText)` stores from `"Linux csl2wk21 5.14.0-687.42.1.el9_8.x86_64"` ::@:: the three words: `Linux`, the machine name, and the version string
- values `sscanf(kernelText, "%d.%d", ...)` returns for a version string like `5.14.0-687` ::@:: `5` and `14`, because each `%d` stops at the first non-digit

## file input and output

`fopen` opens a file and returns a `FILE` pointer; the mode says whether the file is read or written. `fscanf` reads formatted values, `fprintf` writes formatted text, and `fclose` releases the file.

```c
#include <stdio.h>

int main()
{
    int a, b;
    FILE *fin = fopen("input.txt", "r");
    fscanf(fin, "%d %d", &a, &b);
    fclose(fin);

    int result = a + b;
    FILE *fout = fopen("output.txt", "w");
    fprintf(fout, "The sum of %d & %d is %d\n", a, b, result);
    fclose(fout);

    return 0;
}
```

With `3 4` in `input.txt`, the program leaves `The sum of 3 & 4 is 7` in `output.txt` and prints nothing to the terminal; `cat output.txt` reads it back.

---

Flashcards for this section are as follows:

- what the second argument of `fopen` chooses ::@:: the mode, which selects reading as `"r"` or writing as `"w"`
- function that reads formatted values from a file, and the one that writes formatted text to a file ::@:: `fscanf` reads them, and `fprintf` writes them
- where the sum appears after the program runs ::@:: it appears in `output.txt`, written by `fprintf`, since the program prints nothing to the terminal

## build chain from source to program

`gcc` is the GNU Compiler Collection, and it runs four stages in order. Preprocessing expands the `#include` lines and the macros of one source file into a translation unit. Compiling turns that unit into assembly for the machine. Assembling turns the assembly into a relocatable object file. Linking joins the objects and the libraries into one executable, which the loader later places in memory.

Each stage can be stopped and inspected:

```bash
gcc -E program.c -o program.i
gcc -S program.i -o program.s
gcc -c program.s -o program.o
gcc program.o -o program
```

A library is linked by naming it with `-l`. The math functions need the option, because `gcc` leaves the C math library out by default:

```bash
gcc m.c -o m -lm
./m
```

```text
sqrt(2) = 1.414214
```

The option names `libm`: `-l` joins the letters to the `lib` prefix and the `.a` or `.so` suffix. `-lmath` asks for a library called `libmath`, which does not exist. Leaving `-lm` out leaves `sqrt` unresolved at the link stage.

Written as `sqrt(2.0)`, with a constant argument, the call is evaluated while compiling: no `sqrt` symbol reaches the object file, and the program links without `-lm`. A value unknown at compile time, such as a `double` from the command line, keeps the call, and the link then needs the library.

---

Flashcards for this section are as follows:

- four stages a C program passes through before it runs, in order ::@:: preprocessing, compiling, assembling, then linking
- option that stops `gcc` after preprocessing, and the one that stops it after producing assembly ::@:: `-E` for preprocessing, and `-S` for assembly
- option that makes `gcc` produce an object file without linking ::@:: `-c`
- kind of file `gcc -c` writes, and whether it can run ::@:: a relocatable object file, which cannot run until the linker combines it with others
- option that links the C math library, and why it is needed ::@:: `-lm`, because `gcc` leaves that library out and `sqrt` stays unresolved without it
- why `gcc m.c -o m -lmath` fails ::@:: the letters after `-l` name the library, so the option asks for `libmath` while the math library is `libm`
- what the linker produces from several relocatable object files ::@:: one executable file, which the loader then places in memory
- why `sqrt(2.0)` links without `-lm` while `sqrt(x)` does not ::@:: a constant argument lets the compiler evaluate the call, so no `sqrt` symbol reaches the linker; a value unknown at compile time keeps the call, which then needs `-lm`
- what the preprocessing stage does to a C source file ::@:: it expands the `#include` lines and the macros into a translation unit

## compiler warnings

The compiler reports some defects before the program runs. `-Wall` turns on the common warnings and `-Wextra` adds the rest. The program declares `int arr[5]`, whose valid indices are 0 to 4, then reads up to `arr[5]` in the second loop.

```c
#include <stdio.h>

int main()
{
    int arr[5];
    int i;
    for (i = 0; i < 5; i++)
        arr[i] = i;
    for (i = 0; i <= 5; i++)
        printf("%d\n", arr[i]);
    return 0;
}
```

```bash
gcc -Wall -Wextra -O2 buggy.c -o buggy
```

The warning names the undefined behaviour of that last read: the index is one element past the array, so the value printed is whatever memory follows.

---

Flashcards for this section are as follows:

- options that turn on the common compiler warnings and the rest ::@:: `-Wall` for the common warnings, `-Wextra` for the rest
- valid indices of `int arr[5]` ::@:: `0` to `4`
- why the second loop of `buggy.c` reads outside the array ::@:: it runs while `i <= 5`, so the last read is `arr[5]`, one past the final element
- what an out-of-bounds read such as `arr[5]` of an `int arr[5]` yields, and why ::@:: undefined behaviour, so the value printed is whatever memory follows the array

## build automation with make

`make` reads a Makefile and runs the commands that bring targets up to date. A Makefile is a list of rules; each rule carries a target, its prerequisites, and the commands that build it. Command lines start with a Tab, never a space.

<!-- markdownlint-disable MD010 -->

```make
all: hello io_console

hello: hello.c
	gcc -o hello hello.c

io_console: io_console.c
	gcc -o io_console io_console.c

clean:
	rm -f hello io_console
```

<!-- markdownlint-enable MD010 -->

`make` with no argument builds the first rule, here `all`, which builds both programs. `make clean` removes them. The prerequisites make the build incremental: `touch hello.c` leaves `hello.c` newer than `hello`, so the next `make` rebuilds `hello` and leaves `io_console` alone.

```bash
make clean
make
./hello
./io_console
```

```text
Hello World!
```

`./io_console` asks for a name and an age before printing anything.

---

Flashcards for this section are as follows:

- three parts of one rule in a Makefile ::@:: a target, its prerequisites, and the commands that build it
- character the command lines of a Makefile must begin with ::@:: a Tab, never a space
- what `make` rebuilds after `touch hello.c` ::@:: only `hello`, because its prerequisite is now newer than the program
- what `make clean` does ::@:: it runs `rm -f hello io_console`, removing both programs
- rule `make` builds with no target argument ::@:: the first rule in the file, here `all`

## debugging with gdb

`gdb` is the GNU Debugger. It needs source line information inside the executable, and `-g` adds it at compile time.

```bash
gcc buggy.c -o buggy -g
gdb buggy
```

Inside the debugger, `list` shows the source around the current line, `break` places a breakpoint, and `run` starts the program. `print` shows a variable's value; `output` shows the same value without its `$` variable number.

```text
(gdb) break 9
Breakpoint 1 at 0x400544: file buggy.c, line 9.
(gdb) run
Starting program: /homes/<user name>/test/buggy
Breakpoint 1, main () at buggy.c:9
9     for (i=0;i<=5;i++)
(gdb) output arr
{0, 1, 2, 3, 4}
(gdb) output i
5
```

The breakpoint stops the program before the second loop runs. `arr` already holds the five values the first loop wrote, and `i` is 5, the index that reads outside the array. Without a breakpoint, `run` goes to the end.

`break 9` names a line number, so it stops on the second loop only while `buggy.c` keeps its layout: the blank line and the brace on its own line put the loop on line 9. Reformatting the file moves the statement, and the breakpoint with it.

After a stop, `continue` resumes until the next breakpoint. `next` runs the whole next line as one instruction, even when that line calls a function; `step` enters the function instead.

---

Flashcards for this section are as follows:

- option that makes a compiled program carry the line information `gdb` needs ::@:: `-g` adds it
- command that starts the GNU Debugger (gdb) on a program ::@:: `gdb <program>`
- why `break 9` in `buggy.c` stops where it does ::@:: line 9 holds the second loop only while the file keeps its blank line and brace placement; reformatting puts the breakpoint on a different statement
- gdb command that places a breakpoint, and the one that starts the program ::@:: `break <line>` places it, `run` starts the program
- gdb command that prints the value of a variable ::@:: `print <variable>`
- difference between `next` and `step` in the GNU Debugger (gdb) ::@:: `next` runs the whole next line, and `step` enters the function it calls
- gdb command that resumes a stopped program until the next breakpoint ::@:: `continue`
- values of `arr` and `i` at the breakpoint on the second loop of `buggy.c` ::@:: `arr` is `{0, 1, 2, 3, 4}` and `i` is `5`
- GNU Debugger (gdb) command that shows the source around the current line ::@:: `list`
- difference between the `print` and `output` commands of the GNU Debugger (gdb) ::@:: `print` stores the value in a numbered dollar-sign variable, and `output` shows the bare value

## forking inside a running program

`fork()` returns twice, once in each process, so a program that calls it more than once ends up with more processes than calls. The program below makes three calls; the questions ask for counts, not an order, because the counts stay the same on every run.

```c
#include <stdio.h>
#include <unistd.h>

int main()
{
    pid_t pid = fork();
    int cnt = 0;
    if (pid == 0) {
        cnt += 10;
        pid = fork();
        if (pid != 0) {
            cnt += 10;
            pid = fork();
        }
    }
    printf("%d \n", pid);
    printf("%d \n", cnt);
    return 0;
}
```

```text
14479
0
14481
20
0
10
0
20
```

The program ends with four processes. The original forks once; its child forks again only where it is already the parent. Two processes print a real identifier: the original prints its child's, and that child prints the one it creates. The other two print `0` for an identifier, and the original's counter is `0`, the third zero. The counter separates the rest: the first child raises its copy to 10, forks, raises its own to 20 and forks again, so the child of the second fork inherits 20 and the child of the first inherits 10.

---

Flashcards for this section are as follows:

- which processes print a non-zero identifier in the three-call fork program, and how many ::@:: 2: the original and its first child, each printing the identifier of a child it created
- where the three zeros of the three-call fork program come from ::@:: two child processes print `0` in place of an identifier, and the original prints a counter of `0`
- why the three-call fork program prints `10` exactly once ::@:: the first child raises its counter to 10, forks, raises its own to 20 and forks again, so only the child of the first fork keeps a counter of 10
- prototype of `fork()`, and the form the three-call program calls ::@:: `pid_t fork(void)`, called as `fork()`: returns twice, with `0` in the child and the child's process identifier in the parent.
- how many processes remain after three `fork()` calls, where the first is unconditional and each later one runs only in the parent branch ::@:: four processes remain

## ordering the output of forked processes

All three branches of the program below call `fflush(stdout)` after their `printf`. A terminal is line buffered, a pipe or a file is block buffered, so without the flush each line waits in its own process's buffer and the three lines reach the console in whatever order the processes exit.

> Run this program and it should print `The value x in process 3 is 1`, then the same line for process 2, then the line for process 1, every time. Which two calls fill its four blanks?
>
> ```c
> int main() {
>     int x = 0;
>     if (BLANK1) {
>         x = x + 1;
>         BLANK2;
>         printf("The value x in process 1 is %d\n", x);
>         fflush(stdout);
>     } else if (BLANK3) {
>         x = x + 1;
>         BLANK4;
>         printf("The value x in process 2 is %d\n", x);
>         fflush(stdout);
>     } else {
>         x = x + 1;
>         printf("The value x in process 3 is %d\n", x);
>         fflush(stdout);
>     }
>     return 0;
> }
> ```
>
> ---
>
> - solution: {@{`fork()` in `BLANK1` and `BLANK3`, and `wait(0)` in `BLANK2` and `BLANK4`}@}
> - explanation: The first {@{`fork()` keeps the original process}@} on the branch that prints {@{the line for process 1}@}; the second {@{`fork()` splits the other branch into the processes that print 2 and 3}@}. Process 1 then calls {@{`wait(0)`, so it cannot print until its child, process 2, has finished}@}, and process 2 {@{waits the same way for process 3}@}. Process 3 {@{prints first and the other two follow}@}.

---

Flashcards for this section are as follows:

- calls that make the three forked processes print in the order 3, 2, 1 on every run ::@:: `fork()` in the two conditions and `wait(0)` in the two bodies, so each parent waits for its child before printing
- why each branch flushes standard output right after printing ::@:: output to a pipe or a file is block buffered, so without the flush the lines land in whatever order the processes exit
- how standard output is buffered when a C program's output goes to a terminal ::@:: it is line buffered, so each complete line is written as it is printed
