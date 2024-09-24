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

Command names can be {{truncated at the end to produce an abbreviation if the abbreviation is unambiguous, i.e. there is only exactly one command name starting with the abbreviation}}. For example, `disassemble` can be {{abbreviated to `disass` or even the more ugly `disassem`}}. <!--SR:!2024-10-04,10,305!2024-10-13,19,325-->

### common commands

- `apropos <regex>` ::: find text matching `<regex>` <!--SR:!2024-11-08,52,310!2024-10-16,31,270-->
- `backtrace` ::: print backtrace or call stack <!--SR:!2024-11-11,54,310!2024-11-10,54,310-->
- `break <where>` ::: set a breakpoint <!--SR:!2024-11-06,50,310!2024-12-02,69,310-->
- `continue` ::: continue program execution <!--SR:!2024-10-29,40,290!2024-11-04,48,310-->
- `delete [<breakpoint>]` ::: delete a breakpoint; if breakpoint is not specified, then delete all breakpoints <!--SR:!2024-11-16,58,310!2024-11-12,55,310-->
- `disassemble <address|function>` ::: disassemble a specified address or function <!--SR:!2024-10-05,11,305!2024-10-13,19,325-->
- `file <path>` ::: load binary file to debug <!--SR:!2024-11-27,64,310!2024-11-17,59,310-->
- `finish` ::: run until the current function returns <!--SR:!2024-12-03,70,310!2024-11-11,48,290-->
- `help [<topic>]` ::: find information about topic; if topic is not specified, then prints general help <!--SR:!2024-10-13,19,325!2024-10-06,12,305-->
- `info address <symbol>` ::: print the `<symbol>`, its type, and its address <!--SR:!2024-10-13,19,325!2024-10-12,18,325-->
- `info breakpoints|regs|threads`::: list breakpoints, register values, or threads <!--SR:!2024-11-12,55,310!2024-10-29,45,290-->
- `next` ::: go to the next (source) line <!--SR:!2024-11-05,49,310!2024-10-31,46,290-->
- `ni` ::: go to the next instruction <!--SR:!2024-11-16,59,310!2024-11-22,64,310-->
- `print <expression>` ::: evaluate and print an expression <!--SR:!2024-10-21,35,270!2024-12-02,69,310-->
- `run [<args>...]` ::: run program (with args) <!--SR:!2024-11-14,56,310!2024-11-21,63,310-->
- `set <storage> = <value>` ::: set storage to value <!--SR:!2024-10-13,19,325!2024-10-13,19,325-->
- `set args <args>...` ::: set program args <!--SR:!2024-12-05,72,310!2024-11-07,51,310-->
- `si` ::: go to the next instruction stepping into functions <!--SR:!2024-11-17,60,310!2024-10-01,20,250-->
- `starti [<args>...]` ::: start program and stop at its first instruction <!--SR:!2024-12-02,69,310!2024-11-10,47,290-->
- `step` ::: go to the next (source) line stepping into functions <!--SR:!2024-11-11,54,310!2024-10-18,32,270-->
- `x/<format> <address>` ::: examine memory at the given address in the given format (see `help x`) <!--SR:!2024-12-03,70,310!2024-11-06,48,290-->

### reverse debugging

- `rc` ::: reverse continue <!--SR:!2024-10-13,19,325!2024-10-13,19,325-->
- `record` ::: record execution of every instruction; can make the process run slowly <!--SR:!2024-10-04,10,305!2024-10-13,19,325-->
- `rn` ::: rewind to the previous (source) line <!--SR:!2024-10-13,19,325!2024-10-03,14,305-->
- `rni` ::: rewind to the previous instruction <!--SR:!2024-10-13,19,325!2024-10-13,19,325-->
- `rs` ::: rewind to the previous (source) line stepping into functions <!--SR:!2024-10-04,10,305!2024-10-12,18,325-->
- `rsi` ::: rewind to the previous instruction stepping into functions <!--SR:!2024-10-06,12,305!2024-10-13,19,325-->

### `pwndbg`

- `pwndbg>` color (may differ depending on your configuration) ::: cyan: program is running; red: program is not running <!--SR:!2024-11-09,53,310!2024-11-06,43,290-->
- `checksec` ::: print the binary security settings <!--SR:!2024-10-12,18,325!2024-10-13,19,325-->
- `down` ::: move down the backtrace or call stack <!--SR:!2024-11-10,53,310!2024-11-16,58,310-->
- `up` ::: move up the backtrace or call stack <!--SR:!2024-11-11,55,310!2024-11-08,45,290-->

#### `pwndbg` heap

- `heap` ::: iteratively print chunks on heap (`glibc` only) <!--SR:!2024-12-05,72,310!2024-11-29,66,310-->
- `heap_config` ::: show `glibc` allocator hacking configuration <!--SR:!2024-11-09,46,290!2024-11-24,61,310-->

#### `pwndbg` memory

- `vmmap [<address|name>]` ::: display memory mappings information (filtered binary address or name) <!--SR:!2024-10-27,39,290!2024-12-04,71,310-->

#### `pwndbg` stack

- `stack <count> <offset>` ::: prints stack data with the specified count and offset <!--SR:!2024-10-13,19,325!2024-09-30,11,285-->
- `stackf <count> <offset>` ::: prints entire stack frame with the specified count and offset <!--SR:!2024-10-03,14,305!2024-09-29,10,285-->

## miscellaneous

- getting `glibc` version ::: Run the library itself, e.g. `/lib/libc.so.6`. Or run the linker with `--version`, e.g. `ldd --version`. Or in a program, use the string returned from `gnu_get_libc_version()` in `<gnu/libc-version.h>`. <!--SR:!2024-11-08,45,290!2024-10-30,41,290-->
