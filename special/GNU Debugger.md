---
aliases:
  - GDB
  - GNU Debugger
  - GNU debugger
  - gdb
tags:
  - flashcard/active/special/GNU_Debugger
  - language/in/English
---

# GNU Debugger

- see: [GNU Debugger](../general/GNU%20Debugger.md)

## commands

### common commands

- `apropos <topic>` ::: find information about topic <!--SR:!2024-09-17,13,290!2024-10-16,31,270-->
- `backtrace` ::: print backtrace or call stack <!--SR:!2024-09-18,14,290!2024-09-17,13,290-->
- `break <where>` ::: set a breakpoint <!--SR:!2024-09-17,13,290!2024-09-21,17,290-->
- `continue` ::: continue program execution <!--SR:!2024-09-19,15,290!2024-09-17,13,290-->
- `delete <breakpoint>` ::: delete a breakpoint <!--SR:!2024-09-19,15,290!2024-09-18,14,290-->
- `down` ::: move down the backtrace or call stack <!--SR:!2024-09-18,14,290!2024-09-19,15,290-->
- `file <path>` ::: load binary file to debug <!--SR:!2024-09-20,16,290!2024-09-19,15,290-->
- `finish` ::: run until the current function returns <!--SR:!2024-09-21,17,290!2024-09-20,16,290-->
- `info breakpoints|regs|threads`::: list breakpoints, register values, or threads <!--SR:!2024-09-18,14,290!2024-10-29,45,290-->
- `next` ::: go to the next (source) line <!--SR:!2024-09-17,13,290!2024-10-31,46,290-->
- `ni` ::: go to the next instruction <!--SR:!2024-09-18,14,290!2024-09-19,15,290-->
- `print <expression>` ::: evaluate and print an expression <!--SR:!2024-09-16,13,270!2024-09-21,17,290-->
- `run [<args>...]` ::: run program (with args) <!--SR:!2024-09-19,15,290!2024-09-19,15,290-->
- `set args <args>...` ::: set program args <!--SR:!2024-09-21,17,290!2024-09-17,13,290-->
- `si` ::: go to the next instruction stepping into functions <!--SR:!2024-09-18,14,290!2024-10-01,20,250-->
- `starti [<args>...]` ::: start program and stop at its first instruction <!--SR:!2024-09-21,17,290!2024-09-20,16,290-->
- `step` ::: go to the next (source) line stepping into functions <!--SR:!2024-09-18,14,290!2024-09-16,12,270-->
- `up` ::: move up the backtrace or call stack <!--SR:!2024-09-17,13,290!2024-09-20,16,290-->
- `x/<format> <address>` ::: examine memory at the given address in the given format (see `help x`) <!--SR:!2024-09-21,17,290!2024-09-19,15,290-->

### `pwndbg`

- `pwndbg>` color (may differ depending on your configuration) ::: cyan: program is running; red: program is not running <!--SR:!2024-09-17,13,290!2024-09-20,16,290-->

#### `pwndbg` heap hacking

- `heap` ::: (ensure program is running) iteratively print chunks on heap (`glibc` only) <!--SR:!2024-09-21,17,290!2024-09-20,16,290-->
- `heap_config` ::: show `glibc` allocator hacking configuration <!--SR:!2024-09-20,16,290!2024-09-20,16,290-->

#### `pwndbg` memory commands

- `vmmap [<address|name>]` ::: (ensure program is running) display memory mappings information (filtered binary address or name) <!--SR:!2024-09-18,14,290!2024-09-21,17,290-->

## miscellaneous

- getting `glibc` version ::: Run the library itself, e.g. `/lib/libc.so.6`. Or run the linker with `--version`, e.g. `ldd --version`. Or in a program, use the string returned from `gnu_get_libc_version()` in `<gnu/libc-version.h>`. <!--SR:!2024-09-20,16,290!2024-09-19,15,290-->
