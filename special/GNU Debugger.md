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

Command names can be {@{truncated at the end to produce an abbreviation if the abbreviation is unambiguous, i.e. there is only exactly one command name starting with the abbreviation}@}. For example, `disassemble` can be {@{abbreviated to `disass` or even the more ugly `disassem`}@}.

### common commands

- `apropos <regex>` ::@:: find text matching `<regex>`
- `backtrace` ::@:: print backtrace or call stack
- `break <where>` ::@:: set a breakpoint
- `continue` ::@:: continue program execution
- `delete [<breakpoint>]` ::@:: delete a breakpoint; if breakpoint is not specified, then delete all breakpoints
- `disassemble <address|function>` ::@:: disassemble a specified address or function
- `file <path>` ::@:: load binary file to debug
- `finish` ::@:: run until the current function returns
- `help [<topic>]` ::@:: find information about topic; if topic is not specified, then prints general help
- `info address <symbol>` ::@:: print the `<symbol>`, its type, and its address
- `info breakpoints|regs|threads`::@:: list breakpoints, register values, or threads
- `next` ::@:: go to the next (source) line
- `ni` ::@:: go to the next instruction
- `print <expression>` ::@:: evaluate and print an expression
- `run [<args>...]` ::@:: run program (with args)
- `set <storage> = <value>` ::@:: set storage to value
- `set args <args>...` ::@:: set program args
- `si` ::@:: go to the next instruction stepping into functions
- `starti [<args>...]` ::@:: start program and stop at its first instruction
- `step` ::@:: go to the next (source) line stepping into functions
- `x/<format> <address>` ::@:: examine memory at the given address in the given format (see `help x`)

### reverse debugging

- `rc` ::@:: reverse continue
- `record` ::@:: record execution of every instruction; can make the process run slowly
- `rn` ::@:: rewind to the previous (source) line
- `rni` ::@:: rewind to the previous instruction
- `rs` ::@:: rewind to the previous (source) line stepping into functions
- `rsi` ::@:: rewind to the previous instruction stepping into functions

### `pwndbg`

- `pwndbg>` color (may differ depending on your configuration) ::@:: cyan: program is running; red: program is not running
- `checksec` ::@:: print the binary security settings
- `down` ::@:: move down the backtrace or call stack
- `up` ::@:: move up the backtrace or call stack

#### `pwndbg` heap

- `heap` ::@:: iteratively print chunks on heap (`glibc` only)
- `heap_config` ::@:: show `glibc` allocator hacking configuration

#### `pwndbg` memory

- `vmmap [<address|name>]` ::@:: display memory mappings information (filtered binary address or name)

#### `pwndbg` stack

- `stack <count> <offset>` ::@:: prints stack data with the specified count and offset
- `stackf <count> <offset>` ::@:: prints entire stack frame with the specified count and offset

## miscellaneous

- getting `glibc` version ::@:: Run the library itself, e.g. `/lib/libc.so.6`. Or run the linker with `--version`, e.g. `ldd --version`. Or in a program, use the string returned from `gnu_get_libc_version()` in `<gnu/libc-version.h>`.
