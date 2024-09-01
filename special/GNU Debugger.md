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

- `apropos <topic>` ::: find information about topic <!--SR:!2024-09-04,4,270!2024-09-03,3,250-->
- `backtrace` ::: print backtrace or call stack <!--SR:!2024-09-04,4,270!2024-09-04,4,270-->
- `break <where>` ::: set a breakpoint <!--SR:!2024-09-04,4,270!2024-09-04,4,270-->
- `continue` ::: continue program execution <!--SR:!2024-09-04,4,270!2024-09-04,4,270-->
- `delete <breakpoint>` ::: delete a breakpoint <!--SR:!2024-09-04,4,270!2024-09-04,4,270-->
- `down` ::: move down the backtrace or call stack <!--SR:!2024-09-04,4,270!2024-09-04,4,270-->
- `file <path>` ::: load binary file to debug <!--SR:!2024-09-04,4,270!2024-09-04,4,270-->
- `finish` ::: run until the current function returns <!--SR:!2024-09-04,4,270!2024-09-04,4,270-->
- `info breakpoints|regs|threads`::: list breakpoints, register values, or threads <!--SR:!2024-09-04,4,270!2024-09-03,3,250-->
- `next` ::: go to the next (source) line <!--SR:!2024-09-04,4,270!2024-09-03,3,250-->
- `ni` ::: go to the next instruction <!--SR:!2024-09-04,4,270!2024-09-04,4,270-->
- `print <expression>` ::: evaluate and print an expression <!--SR:!2024-09-03,3,250!2024-09-04,4,270-->
- `run [<args>...]` ::: run program (with args) <!--SR:!2024-09-04,4,270!2024-09-04,4,270-->
- `set args <args>...` ::: set program args <!--SR:!2024-09-04,4,270!2024-09-04,4,270-->
- `si` ::: go to the next instruction stepping into functions <!--SR:!2024-09-04,4,270!2024-09-03,3,250-->
- `starti [<args>...]` ::: start program and stop at its first instruction <!--SR:!2024-09-04,4,270!2024-09-04,4,270-->
- `step` ::: go to the next (source) line stepping into functions <!--SR:!2024-09-04,4,270!2024-09-04,4,270-->
- `up` ::: move up the backtrace or call stack <!--SR:!2024-09-04,4,270!2024-09-04,4,270-->
- `x/<format> <address>` ::: examine memory at the given address in the given format (see `help x`) <!--SR:!2024-09-04,4,270!2024-09-04,4,270-->

### `pwndbg`

- `pwndbg>` color (may differ depending on your configuration) ::: cyan: program is running; red: program is not running <!--SR:!2024-09-04,4,270!2024-09-04,4,270-->

#### `pwndbg` heap hacking

- `heap` ::: (ensure program is running) iteratively print chunks on heap (`glibc` only) <!--SR:!2024-09-04,4,270!2024-09-04,4,270-->
- `heap_config` ::: show `glibc` allocator hacking configuration <!--SR:!2024-09-04,4,270!2024-09-04,4,270-->

#### `pwndbg` memory commands

- `vmmap [<address|name>]` ::: (ensure program is running) display memory mappings information (filtered binary address or name) <!--SR:!2024-09-04,4,270!2024-09-04,4,270-->

## miscellaneous

- getting `glibc` version ::: Run the library itself, e.g. `/lib/libc.so.6`. Or run the linker with `--version`, e.g. `ldd --version`. Or in a program, use the string returned from `gnu_get_libc_version()` in `<gnu/libc-version.h>`. <!--SR:!2024-09-04,4,270!2024-09-04,4,270-->
