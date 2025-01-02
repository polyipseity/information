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

Command names can be {@{truncated at the end to produce an abbreviation if the abbreviation is unambiguous, i.e. there is only exactly one command name starting with the abbreviation}@}. For example, `disassemble` can be {@{abbreviated to `disass` or even the more ugly `disassem`}@}. <!--SR:!2025-03-17,130,325!2025-01-13,88,345-->

### common commands

- `apropos <regex>` ::@:: find text matching `<regex>` <!--SR:!2025-06-22,226,330!2025-02-13,119,290-->
- `backtrace` ::@:: print backtrace or call stack <!--SR:!2025-04-29,169,310!2025-07-05,237,330-->
- `break <where>` ::@:: set a breakpoint <!--SR:!2025-06-14,220,330!2025-09-30,301,330-->
- `continue` ::@:: continue program execution <!--SR:!2025-04-12,165,310!2025-05-30,207,330-->
- `delete [<breakpoint>]` ::@:: delete a breakpoint; if breakpoint is not specified, then delete all breakpoints <!--SR:!2025-07-29,255,330!2025-07-10,240,330-->
- `disassemble <address|function>` ::@:: disassemble a specified address or function <!--SR:!2025-06-11,201,345!2025-01-13,88,345-->
- `file <path>` ::@:: load binary file to debug <!--SR:!2025-09-04,281,330!2025-07-27,252,330-->
- `finish` ::@:: run until the current function returns <!--SR:!2025-10-02,303,330!2025-05-23,193,310-->
- `help [<topic>]` ::@:: find information about topic; if topic is not specified, then prints general help <!--SR:!2025-01-13,88,345!2025-07-22,234,345-->
- `info address <symbol>` ::@:: print the `<symbol>`, its type, and its address <!--SR:!2025-01-13,88,345!2025-09-28,283,345-->
- `info breakpoints|regs|threads`::@:: list breakpoints, register values, or threads <!--SR:!2025-07-11,241,330!2025-05-01,184,310-->
- `next` ::@:: go to the next (source) line <!--SR:!2025-06-07,214,330!2025-05-13,194,310-->
- `ni` ::@:: go to the next instruction <!--SR:!2025-07-30,256,330!2025-08-26,277,330-->
- `print <expression>` ::@:: evaluate and print an expression <!--SR:!2025-01-26,97,270!2025-09-29,300,330-->
- `run [<args>...]` ::@:: run program (with args) <!--SR:!2025-07-18,246,330!2025-08-19,271,330-->
- `set <storage> = <value>` ::@:: set storage to value <!--SR:!2025-01-13,88,345!2025-01-13,88,345-->
- `set args <args>...` ::@:: set program args <!--SR:!2025-10-12,311,330!2025-06-15,220,330-->
- `si` ::@:: go to the next instruction stepping into functions <!--SR:!2025-08-07,263,330!2025-06-01,189,270-->
- `starti [<args>...]` ::@:: start program and stop at its first instruction <!--SR:!2025-10-01,302,330!2025-03-27,137,290-->
- `step` ::@:: go to the next (source) line stepping into functions <!--SR:!2025-04-27,167,310!2025-02-14,119,290-->
- `x/<format> <address>` ::@:: examine memory at the given address in the given format (see `help x`) <!--SR:!2025-07-08,217,310!2025-03-27,141,290-->

### reverse debugging

- `rc` ::@:: reverse continue <!--SR:!2025-01-13,88,345!2025-01-13,88,345-->
- `record` ::@:: record execution of every instruction; can make the process run slowly <!--SR:!2025-05-22,185,345!2025-01-13,88,345-->
- `rn` ::@:: rewind to the previous (source) line <!--SR:!2025-01-13,88,345!2025-08-21,264,345-->
- `rni` ::@:: rewind to the previous instruction <!--SR:!2025-01-13,88,345!2025-01-13,88,345-->
- `rs` ::@:: rewind to the previous (source) line stepping into functions <!--SR:!2025-03-08,122,325!2025-09-30,271,345-->
- `rsi` ::@:: rewind to the previous instruction stepping into functions <!--SR:!2025-07-26,238,345!2025-01-13,88,345-->

### `pwndbg`

- `pwndbg>` color (may differ depending on your configuration) ::@:: cyan: program is running; red: program is not running <!--SR:!2025-06-26,229,330!2025-04-28,173,310-->
- `checksec` ::@:: print the binary security settings <!--SR:!2026-01-03,366,365!2025-01-13,88,345-->
- `down` ::@:: move down the backtrace or call stack <!--SR:!2025-04-23,164,310!2025-07-23,249,330-->
- `up` ::@:: move up the backtrace or call stack <!--SR:!2025-05-03,173,310!2025-05-12,185,310-->

#### `pwndbg` heap

- `heap` ::@:: iteratively print chunks on heap (`glibc` only) <!--SR:!2025-10-11,310,330!2025-09-12,286,330-->
- `heap_config` ::@:: show `glibc` allocator hacking configuration <!--SR:!2025-05-14,186,310!2025-08-18,267,330-->

#### `pwndbg` memory

- `vmmap [<address|name>]` ::@:: display memory mappings information (filtered binary address or name) <!--SR:!2025-04-06,161,310!2025-07-11,218,310-->

#### `pwndbg` stack

- `stack <count> <offset>` ::@:: prints stack data with the specified count and offset <!--SR:!2025-01-13,88,345!2025-03-20,128,305-->
- `stackf <count> <offset>` ::@:: prints entire stack frame with the specified count and offset <!--SR:!2025-04-08,141,305!2025-03-10,122,305-->

## miscellaneous

- getting `glibc` version ::@:: Run the library itself, e.g. `/lib/libc.so.6`. Or run the linker with `--version`, e.g. `ldd --version`. Or in a program, use the string returned from `gnu_get_libc_version()` in `<gnu/libc-version.h>`. <!--SR:!2025-05-11,184,310!2025-04-16,168,310-->
