---
aliases:
  - COMP 2611 MARS
  - MARS
tags:
  - flashcard/active/special/academia/HKUST/COMP_2611/MARS
  - function/index
  - language/in/English
---

# MARS

- HKUST COMP 2611

## system calls

In general, system calls can be roughly described as {@{an essential interface between a process and the operating system}@}. In MARS, you can use it to {@{read and write to the console I/O window}@}. <!--SR:!2026-02-08,252,330!2026-02-22,262,330-->

To invoke a system call, {@{specify the service to be called in `$v0` \(`$2`\) and pass any additional arguments required in other registers}@}. Then {@{run the instruction `syscall`}@}. The inputs \(if any\) are usually {@{stored in the `$a0`–`$a3` \(`$4`–`$7`\) registers}@}, while the outputs \(if any\) are usually {@{stored in the `$v0`–`$v1` \(`$2`–`$3`\) registers}@}. <!--SR:!2025-06-11,65,310!2026-03-07,274,330!2025-06-10,64,310!2025-06-12,66,310-->

Some common syscalls are provided below:

- \(`$v0`=1\) `print_int` ::@:: Print an integer. <p> input: `$a0` \(`$4`\) is the integer to be printed. <!--SR:!2026-02-23,263,330!2025-11-23,188,310-->
- \(`$v0`=2\) `print_float` ::@:: Print a float. <p> input: `$f12` is the float to be printed. <!--SR:!2026-02-15,255,330!2025-12-03,185,310-->
- \(`$v0`=3\) `print_double` ::@:: Print a double. <p> input: `$f13:$f12` is the double to be printed. <!--SR:!2025-06-10,64,310!2026-02-11,255,330-->
- \(`$v0`=4\) `print_string` ::@:: Print a _null-terminated_ string. `$at` \(`$1`\) will be cobbled. <p> input: `$a0` \(`$4`\) is the address of the _null-terminated_ string to be printed. <!--SR:!2025-06-13,67,310!2025-06-11,65,310-->
- \(`$v0`=5\) `read_int` ::@:: Read a line as an integer. <p> output: `$v0` \(`$2`\) is the integer read. <!--SR:!2026-02-11,255,330!2026-02-10,254,330-->
- \(`$v0`=6\) `read_float` ::@:: Read a line as a float. <p> output: `$f0` is the float read. <!--SR:!2025-09-18,122,290!2025-12-09,191,310-->
- \(`$v0`=7\) `read_double` ::@:: Read a line as a double. <p> output: `$f1:$f0` is the double read. <!--SR:!2026-02-24,264,330!2026-02-09,253,330-->
- \(`$v0`=8\) `read_string` ::@:: Read a line to a string buffer of a specified size. The string is _null-terminated_, so maximum string size is 1 less than the buffer size. `$at` \(`$1`\) will be cobbled. <p> input: `$a0` \(`$4`\) is the string buffer. `$a1` \(`$5`\) is the string buffer size. <!--SR:!2025-11-08,173,310!2025-09-18,122,290-->
- \(`$v0`=9\) `sbrk` ::@:: Allocate memory of a specified size from the heap. <p> input: `$a0` \(`$4`\) is the memory size required. <br/> output: `$v0` \(`$2`\) is the address of the allocated memory. <!--SR:!2026-02-19,259,330!2026-02-26,266,330-->
- \(`$v0`=10\) `exit` ::@:: Terminate the program. <!--SR:!2025-11-07,172,310!2026-02-10,254,330-->
