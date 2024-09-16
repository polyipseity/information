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

Command names can be {{truncated at the end to produce an abbreviation if the abbreviation is unambiguous, i.e. there is only exactly one command name starting with the abbreviation}}. For example, `disassemble` can be {{abbreviated to `disass` or even the more ugly `disassem`}}.

### common commands

- `apropos <regex>` ::: find text matching `<regex>` <!--SR:!2024-09-17,13,290!2024-10-16,31,270-->
- `backtrace` ::: print backtrace or call stack <!--SR:!2024-09-18,14,290!2024-09-17,13,290-->
- `break <where>` ::: set a breakpoint <!--SR:!2024-09-17,13,290!2024-09-21,17,290-->
- `continue` ::: continue program execution <!--SR:!2024-09-19,15,290!2024-09-17,13,290-->
- `delete [<breakpoint>]` ::: delete a breakpoint; if breakpoint is not specified, then delete all breakpoints <!--SR:!2024-09-19,15,290!2024-09-18,14,290-->
- `disassemble <address|function>` ::: disassemble a specified address or function
- `file <path>` ::: load binary file to debug <!--SR:!2024-09-20,16,290!2024-09-19,15,290-->
- `finish` ::: run until the current function returns <!--SR:!2024-09-21,17,290!2024-09-20,16,290-->
- `help [<topic>]` ::: find information about topic; if topic is not specified, then prints general help
- `info address <symbol>` ::: print the `<symbol>`, its type, and its address
- `info breakpoints|regs|threads`::: list breakpoints, register values, or threads <!--SR:!2024-09-18,14,290!2024-10-29,45,290-->
- `next` ::: go to the next (source) line <!--SR:!2024-09-17,13,290!2024-10-31,46,290-->
- `ni` ::: go to the next instruction <!--SR:!2024-09-18,14,290!2024-09-19,15,290-->
- `print <expression>` ::: evaluate and print an expression <!--SR:!2024-10-21,35,270!2024-09-21,17,290-->
- `run [<args>...]` ::: run program (with args) <!--SR:!2024-09-19,15,290!2024-09-19,15,290-->
- `set <storage> = <value>` ::: set storage to value
- `set args <args>...` ::: set program args <!--SR:!2024-09-21,17,290!2024-09-17,13,290-->
- `si` ::: go to the next instruction stepping into functions <!--SR:!2024-09-18,14,290!2024-10-01,20,250-->
- `starti [<args>...]` ::: start program and stop at its first instruction <!--SR:!2024-09-21,17,290!2024-09-20,16,290-->
- `step` ::: go to the next (source) line stepping into functions <!--SR:!2024-09-18,14,290!2024-10-18,32,270-->
- `x/<format> <address>` ::: examine memory at the given address in the given format (see `help x`) <!--SR:!2024-09-21,17,290!2024-09-19,15,290-->

### reverse debugging

- `rc` ::: reverse continue
- `record` ::: record execution of every instruction; can make the process run slowly
- `rn` ::: rewind to the previous (source) line
- `rni` ::: rewind to the previous instruction
- `rs` ::: rewind to the previous (source) line stepping into functions
- `rsi` ::: rewind to the previous instruction stepping into functions

### `pwndbg`

- `pwndbg>` color (may differ depending on your configuration) ::: cyan: program is running; red: program is not running <!--SR:!2024-09-17,13,290!2024-09-20,16,290-->
- `checksec` ::: print the binary security settings
- `down` ::: move down the backtrace or call stack <!--SR:!2024-09-18,14,290!2024-09-19,15,290-->
- `up` ::: move up the backtrace or call stack <!--SR:!2024-09-17,13,290!2024-09-20,16,290-->

#### `pwndbg` heap

- `heap` ::: iteratively print chunks on heap (`glibc` only) <!--SR:!2024-09-21,17,290!2024-09-20,16,290-->
- `heap_config` ::: show `glibc` allocator hacking configuration <!--SR:!2024-09-20,16,290!2024-09-20,16,290-->

#### `pwndbg` memory

- `vmmap [<address|name>]` ::: display memory mappings information (filtered binary address or name) <!--SR:!2024-09-18,14,290!2024-09-21,17,290-->

#### `pwndbg` stack

- `stack <count> <offset>` ::: prints stack data with the specified count and offset
- `stackf <count> <offset>` ::: prints entire stack frame with the specified count and offset

## miscellaneous

- getting `glibc` version ::: Run the library itself, e.g. `/lib/libc.so.6`. Or run the linker with `--version`, e.g. `ldd --version`. Or in a program, use the string returned from `gnu_get_libc_version()` in `<gnu/libc-version.h>`. <!--SR:!2024-09-20,16,290!2024-09-19,15,290-->
