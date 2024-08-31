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

- `apropos <topic>` ::: find information about topic
- `backtrace` ::: print backtrace or call stack
- `break <where>` ::: set a breakpoint
- `continue` ::: continue program execution
- `delete <breakpoint>` ::: delete a breakpoint
- `down` ::: move down the backtrace or call stack
- `file <path>` ::: load binary file to debug
- `finish` ::: run until the current function returns
- `info breakpoints|regs|threads`::: list breakpoints, register values, or threads
- `next` ::: go to the next (source) line
- `ni` ::: go to the next instruction
- `print <expression>` ::: evaluate and print an expression
- `run [<args>...]` ::: run program (with args)
- `set args <args>...` ::: set program args
- `si` ::: go to the next instruction stepping into functions
- `starti [<args>...]` ::: start program and stop at its first instruction
- `step` ::: go to the next (source) line stepping into functions
- `up` ::: move up the backtrace or call stack
- `x/<format> <address>` ::: examine memory at the given address in the given format (see `help x`)

### `pwndbg`

- `pwndbg>` color (may differ depending on your configuration) ::: cyan: program is running; red: program is not running

#### `pwndbg` heap hacking

- `heap` ::: (ensure program is running) iteratively print chunks on heap (`glibc` only)
- `heap_config` ::: show `glibc` allocator hacking configuration

#### `pwndbg` memory commands

- `vmmap [<address|name>]` ::: (ensure program is running) display memory mappings information (filtered binary address or name)

## miscellaneous

- getting `glibc` version ::: Run the library itself, e.g. `/lib/libc.so.6`. Or run the linker with `--version`, e.g. `ldd --version`. Or in a program, use the string returned from `gnu_get_libc_version()` in `<gnu/libc-version.h>`.
