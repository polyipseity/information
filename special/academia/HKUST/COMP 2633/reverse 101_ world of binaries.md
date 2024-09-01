---
aliases:
  - Rev 101
  - 'Rev 101: World of Binaries'
  - Reverse 101
  - 'Reverse 101: World of Binaries'
  - rev 101
  - 'rev 101: world of binaries'
  - reverse 101
  - 'reverse 101: world of binaries'
  - world of binaries
tags:
  - flashcard/active/special/academia/HKUST/COMP_2633/reverse_101__world_of_binaries
  - function/index
  - language/in/English
---

# reverse 101: world of binaries

## introduction

- Why do reverse engineering, apart from CTFs? ::: You can analyze malware, ensuring interoperability with closed-source programs, or find vulnerabilities in them. What do have in common is that the program source is not readily available.

## compiling a program

Assuming you are using Linux. For developers, compiling a C program is {{simply running the GNU Compiler Collection (gcc) using the ocmmand `gcc <input>.c -o <output>` in a terminal, which compiles the C code in `<input>.c` into a program called `<output>`}}.

However, we can go further than this. The program `<output>` is {{actually a format called an _Executable and LinkableFormat_ (ELF) file}}. The property we can about here is that {{you can execute it, as evident from the "executable" in its name}}. Details will be mentioned in later lectures.

Instead, we are more interested in {{the compilation process itself}}. We like to think of compilation as a single process, but {{it is really composed of several steps: preprocessing (`-E`), then compilation (`-S`), then assembly (`-c`), and finally linking (none)}}.

Preprocessing {{transforms source program (text) into modified source program (still text)}}. GCC internally {{uses the program `cpp`, which we can use by itself}}, for this step. To only run this step with GCC, the command is {{`gcc -E <input>.c > <output>.i`, which writes to `<output>.i`}}.

Compilation {{transforms modified source program (text) into assembly program (still text)}}. GCC internally {{uses the program `cc1`, part of the GCC}}, for this step. To only run this step, the command is {{`gcc -S <input>.i`, which outputs a `.s` file}}.

Assembly {{transforms assembly program (text) into relocatable object (binary)}}. GCC internally {{uses the program `as`, which we can use by itself}}, for this step. To only run this step, the command is {{`gcc -c <input>.s`, which outputs a `.o` file}}.

Linking {{transform relocatable object (binary) into an ELF file (binary)}}, which is the final product we want. GCC internally {{uses the program `ld`, which we can sue by itself}}, for this step. To only run this step, the command is {{`gcc <input>.o -o <output>`, which outputs the ELF file as `<output>`}}.

It is okay that one does not understand everything above. The most important part is that {{a source file is transformed into assembly program, which is finally transformed into the ELF file}}. {{Reversing the ELF file into the assembly program}} is easy as {{assembly has a mostly direct correspondence with instructions in the ELF file}}, but {{reversing the assembly program into the original source program}} is difficult as {{language constructs can be compiled into assembly in a multitude of ways, losing information in the process}}. Reversing is somewhat about the latter, but more accurately is about {{understanding the program behavior from the assembly without the source program}}. And to do so, we need to {{learn assembly}}.
