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

Command names can be {@{truncated at the end to produce an abbreviation if the abbreviation is unambiguous, i.e. there is only exactly one command name starting with the abbreviation}@}. For example, `disassemble` can be {@{abbreviated to `disass` or even the more ugly `disassem`}@}. <!--SR:!2026-05-16,424,325!2026-03-11,422,365-->

### common commands

- `apropos <regex>` ::@:: find text matching `<regex>` <!--SR:!2028-04-12,1024,350!2029-11-30,1402,310-->
- `backtrace` ::@:: print backtrace or call stack <!--SR:!2027-05-03,725,330!2028-06-17,1078,350-->
- `break <where>` ::@:: set a breakpoint <!--SR:!2028-03-17,1000,350!2029-07-01,1370,350-->
- `continue` ::@:: continue program execution <!--SR:!2027-03-22,707,330!2027-12-31,942,350-->
- `delete [<breakpoint>]` ::@:: delete a breakpoint; if breakpoint is not specified, then delete all breakpoints <!--SR:!2028-10-05,1161,350!2028-07-10,1093,350-->
- `disassemble <address|function>` ::@:: disassemble a specified address or function <!--SR:!2028-02-04,958,365!2031-12-10,2102,385-->
- `file <path>` ::@:: load binary file to debug <!--SR:!2029-03-08,1281,350!2028-09-17,1147,350-->
- `finish` ::@:: run until the current function returns <!--SR:!2029-07-12,1379,350!2027-08-31,828,330-->
- `help [<topic>]` ::@:: find information about topic; if topic is not specified, then prints general help <!--SR:!2026-03-12,423,365!2028-08-07,1111,365-->
- `info address <symbol>` ::@:: print the `<symbol>`, its type, and its address <!--SR:!2029-09-15,1409,365!2028-05-31,976,345-->
- `info breakpoints|regs|threads`::@:: list breakpoints, register values, or threads <!--SR:!2028-07-14,1097,350!2027-07-09,792,330-->
- `next` ::@:: go to the next (source) line <!--SR:!2028-02-19,973,350!2027-09-04,832,330-->
- `ni` ::@:: go to the next instruction <!--SR:!2028-10-11,1167,350!2029-02-06,1260,350-->
- `print <expression>` ::@:: evaluate and print an expression <!--SR:!2028-07-07,993,290!2029-06-29,1369,350-->
- `run [<args>...]` ::@:: run program (with args) <!--SR:!2028-08-15,1124,350!2029-01-03,1233,350-->
- `set <storage> = <value>` ::@:: set storage to value <!--SR:!2026-03-14,425,365!2031-11-24,2089,385-->
- `set args <args>...` ::@:: set program args <!--SR:!2029-08-27,1415,350!2028-03-16,999,350-->
- `si` ::@:: go to the next instruction stepping into functions <!--SR:!2028-11-15,1196,350!2027-05-10,707,290-->
- `starti [<args>...]` ::@:: start program and stop at its first instruction <!--SR:!2028-06-24,997,330!2026-10-03,555,310-->
- `step` ::@:: go to the next (source) line stepping into functions <!--SR:!2027-04-25,717,330!2026-06-16,487,310-->
- `x/<format> <address>` ::@:: examine memory at the given address in the given format (see `help x`) <!--SR:!2028-01-30,931,330!2026-05-14,413,290-->

### reverse debugging

- `rc` ::@:: reverse continue <!--SR:!2026-03-10,421,365!2026-03-13,424,365-->
- `record` ::@:: record execution of every instruction; can make the process run slowly <!--SR:!2027-10-23,881,365!2031-11-08,2075,385-->
- `rn` ::@:: rewind to the previous (source) line <!--SR:!2029-09-14,1408,365!2029-01-25,1253,365-->
- `rni` ::@:: rewind to the previous instruction <!--SR:!2031-11-16,2082,385!2031-11-28,2092,385-->
- `rs` ::@:: rewind to the previous (source) line stepping into functions <!--SR:!2026-04-14,402,325!2029-04-07,1285,365-->
- `rsi` ::@:: rewind to the previous instruction stepping into functions <!--SR:!2028-08-30,1129,365!2029-09-10,1404,365-->

### `pwndbg`

- `pwndbg>` color (may differ depending on your configuration) ::@:: cyan: program is running; red: program is not running <!--SR:!2028-05-06,1045,350!2026-10-27,537,310-->
- `checksec` ::@:: print the binary security settings <!--SR:!2031-01-17,1832,385!2029-09-16,1410,365-->
- `down` ::@:: move down the backtrace or call stack <!--SR:!2027-03-26,702,330!2028-08-29,1133,350-->
- `up` ::@:: move up the backtrace or call stack <!--SR:!2027-05-21,743,330!2027-07-29,795,330-->

#### `pwndbg` heap

- `heap` ::@:: iteratively print chunks on heap (`glibc` only) <!--SR:!2029-08-20,1409,350!2029-04-04,1300,350-->
- `heap_config` ::@:: show `glibc` allocator hacking configuration <!--SR:!2027-08-06,803,330!2028-12-16,1216,350-->

#### `pwndbg` memory

- `vmmap [<address|name>]` ::@:: display memory mappings information (filtered binary address or name) <!--SR:!2026-08-25,504,310!2028-02-02,934,330-->

#### `pwndbg` stack

- `stack <count> <offset>` ::@:: prints stack data with the specified count and offset <!--SR:!2031-12-05,2098,385!2026-09-13,541,325-->
- `stackf <count> <offset>` ::@:: prints entire stack frame with the specified count and offset <!--SR:!2026-06-12,430,305!2026-08-04,512,325-->

## miscellaneous

- getting `glibc` version ::@:: Run the library itself, e.g. `/lib/libc.so.6`. Or run the linker with `--version`, e.g. `ldd --version`. Or in a program, use the string returned from `gnu_get_libc_version()` in `<gnu/libc-version.h>`. <!--SR:!2027-07-27,793,330!2026-09-20,521,310-->
