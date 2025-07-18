---
aliases:
  - COMP 2611 MARS
  - MARS
tags:
  - flashcard/active/special/academia/HKUST/COMP_2611/MARS
  - language/in/English
---

# MARS

- HKUST COMP 2611

## system calls

In general, system calls can be roughly described as {@{an essential interface between a process and the operating system}@}. In MARS, you can use it to {@{read and write to the console I/O window}@}.

To invoke a system call, {@{specify the service to be called in `$v0` \(`$2`\) and pass any additional arguments required in other registers}@}. Then {@{run the instruction `syscall`}@}. The inputs \(if any\) are usually {@{stored in the `$a0`–`$a3` \(`$4`–`$7`\) registers}@}, while the outputs \(if any\) are usually {@{stored in the `$v0`–`$v1` \(`$2`–`$3`\) registers}@}.

Some common syscalls are provided below:

- \(`$v0`=1\) `print_int` ::@:: Print an integer. <p> input: `$a0` \(`$4`\) is the integer to be printed.
- \(`$v0`=2\) `print_float` ::@:: Print a float. <p> input: `$f12` is the float to be printed.
- \(`$v0`=3\) `print_double` ::@:: Print a double. <p> input: `$f13:$f12` is the double to be printed.
- \(`$v0`=4\) `print_string` ::@:: Print a _null-terminated_ string. `$at` \(`$1`\) will be cobbled. <p> input: `$a0` \(`$4`\) is the address of the _null-terminated_ string to be printed.
- \(`$v0`=5\) `read_int` ::@:: Read a line as an integer. <p> output: `$v0` \(`$2`\) is the integer read.
- \(`$v0`=6\) `read_float` ::@:: Read a line as a float. <p> output: `$f0` is the float read.
- \(`$v0`=7\) `read_double` ::@:: Read a line as a double. <p> output: `$f1:$f0` is the double read.
- \(`$v0`=8\) `read_string` ::@:: Read a line to a string buffer of a specified size. The string is _null-terminated_, so maximum string size is 1 less than the buffer size. `$at` \(`$1`\) will be cobbled. <p> input: `$a0` \(`$4`\) is the string buffer. `$a1` \(`$5`\) is the string buffer size.
- \(`$v0`=9\) `sbrk` ::@:: Allocate memory of a specified size from the heap. <p> input: `$a0` \(`$4`\) is the memory size required. <br/> output: `$v0` \(`$2`\) is the address of the allocated memory.
- \(`$v0`=10\) `exit` ::@:: Terminate the program.
