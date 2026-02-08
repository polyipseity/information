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

In general, system calls can be roughly described as {@{an essential interface between a process and the operating system}@}. In MARS, you can use it to {@{read and write to the console I/O window}@}. <!--SR:!2029-04-07,1154,350!2026-02-22,262,330-->

To invoke a system call, {@{specify the service to be called in `$v0` \(`$2`\) and pass any additional arguments required in other registers}@}. Then {@{run the instruction `syscall`}@}. The inputs \(if any\) are usually {@{stored in the `$a0`–`$a3` \(`$4`–`$7`\) registers}@}, while the outputs \(if any\) are usually {@{stored in the `$v0`–`$v1` \(`$2`–`$3`\) registers}@}. <!--SR:!2026-03-21,278,330!2026-03-07,274,330!2026-03-23,280,330!2026-03-31,288,330-->

Some common syscalls are provided below:

- \(`$v0`=1\) `print_int` ::@:: Print an integer. <p> input: `$a0` \(`$4`\) is the integer to be printed. <!--SR:!2026-02-23,263,330!2028-02-08,807,330-->
- \(`$v0`=2\) `print_float` ::@:: Print a float. <p> input: `$f12` is the float to be printed. <!--SR:!2026-02-15,255,330!2028-02-12,801,330-->
- \(`$v0`=3\) `print_double` ::@:: Print a double. <p> input: `$f13:$f12` is the double to be printed. <!--SR:!2026-03-18,275,330!2026-02-11,255,330-->
- \(`$v0`=4\) `print_string` ::@:: Print a _null-terminated_ string. `$at` \(`$1`\) will be cobbled. <p> input: `$a0` \(`$4`\) is the address of the _null-terminated_ string to be printed. <!--SR:!2026-04-05,293,330!2026-03-24,281,330-->
- \(`$v0`=5\) `read_int` ::@:: Read a line as an integer. <p> output: `$v0` \(`$2`\) is the integer read. <!--SR:!2026-02-11,255,330!2026-02-10,254,330-->
- \(`$v0`=6\) `read_float` ::@:: Read a line as a float. <p> output: `$f0` is the float read. <!--SR:!2027-01-28,497,310!2028-03-10,822,330-->
- \(`$v0`=7\) `read_double` ::@:: Read a line as a double. <p> output: `$f1:$f0` is the double read. <!--SR:!2026-02-24,264,330!2026-02-09,253,330-->
- \(`$v0`=8\) `read_string` ::@:: Read a line to a string buffer of a specified size. The string is _null-terminated_, so maximum string size is 1 less than the buffer size. `$at` \(`$1`\) will be cobbled. <p> input: `$a0` \(`$4`\) is the string buffer. `$a1` \(`$5`\) is the string buffer size. <!--SR:!2027-04-28,536,310!2027-01-27,496,310-->
- \(`$v0`=9\) `sbrk` ::@:: Allocate memory of a specified size from the heap. <p> input: `$a0` \(`$4`\) is the memory size required. <br/> output: `$v0` \(`$2`\) is the address of the allocated memory. <!--SR:!2026-02-19,259,330!2026-02-26,266,330-->
- \(`$v0`=10\) `exit` ::@:: Terminate the program. <!--SR:!2027-11-14,737,330!2026-02-10,254,330-->
