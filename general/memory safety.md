---
aliases:
  - memory safe
  - memory safeties
  - memory safety
  - memory unsafe
  - memory unsafeties
  - memory unsafety
tags:
  - flashcard/active/general/memory_safety
  - language/in/English
---

# memory safety

- This article is about protection of memory in software development. For hardware protection of memory, see [memory protection](memory%20protection.md).

__Memory safety__ is {{the state of being protected from various [software bugs](software%20bug.md) and [security vulnerabilities](vulnerability%20(computer%20security).md) when dealing with [memory](random-access%20memory.md) access}}, such as {{[buffer overflows](buffer%20overflow.md) and [dangling pointers](dangling%20pointer.md)}}. For example, [Java](java%20(programming%20language).md) is said {{to be memory-safe}} because {{its [runtime error detection](runtime%20error%20detection.md) checks array bounds and pointer dereferences}}. In contrast, [C](c%20(programming%20language).md) and [C++](C++.md) {{allow arbitrary [pointer arithmetic](pointer%20(computer%20programming).md) with pointers implemented as direct memory addresses with no provision for [bounds checking](bounds%20checking.md)}}, and thus {{are potentially __memory-unsafe__}}. <!--SR:!2024-11-05,44,290!2024-11-13,52,290!2024-11-13,56,310!2024-11-22,64,310!2024-11-17,59,310!2024-11-06,48,290-->

## types of memory errors

Many different types of memory errors can occur. Important one includes {{access errors, uninitialized variables, and memory leak}}. <!--SR:!2024-10-30,41,290-->

- __access errors__ ::: Invalid read/write of a pointer. Includes buffer overflow, buffer over-read, invalid page fault, use after free, etc. <!--SR:!2024-11-03,45,290!2024-11-09,48,290-->
  - __[buffer overflow](buffer%20overflow.md)__ ::: Out-of-bound writes can corrupt the content of adjacent objects, or internal data (like bookkeeping information for the [heap](memory%20management.md#HEAP)) or [return](return%20statement.md) addresses. <!--SR:!2024-11-05,44,290!2024-11-06,50,310-->
  - __[buffer over-read](buffer%20over-read.md)__ ::: Out-of-bound reads can reveal sensitive data or help attackers bypass [address space layout randomization](address%20space%20layout%20randomization.md). <!--SR:!2024-11-07,51,310!2024-11-11,54,310-->
  - __[invalid page fault](page%20fault.md#invalid)__ ::: Accessing a pointer outside the virtual memory space. A null pointer dereference will often cause an exception or program termination in most environments, but can cause corruption in operating system [kernels](kernel%20(operating%20system).md) or systems without [memory protection](memory%20protection.md), or when use of the null pointer involves a large or negative offset. <!--SR:!2024-11-12,51,290!2024-10-22,38,290-->
  - __use after free__ ::: Dereferencing a [dangling pointer](dangling%20pointer.md) storing the address of an object that has been deleted. <!--SR:!2024-11-08,52,310!2024-11-22,61,310-->
- __[uninitialized variables](uninitialized%20variable.md)__ ::: A variable that has not been assigned a value is used. It may contain an undesired or, in some languages, a corrupt value. Includes null pointer deference, wild pointers, etc. <!--SR:!2024-11-07,41,250!2024-11-09,52,310-->
  - __[null pointer](null%20pointer.md) dereference__ ::: Dereferencing an invalid pointer or a pointer to memory that has not been allocated <!--SR:!2024-11-14,57,310!2024-11-15,57,310-->
  - __[wild pointers](dangling%20pointer.md)__ ::: Arises when a pointer is used prior to initialization to some known state. They show the same erratic behaviour as dangling pointers, though they are less likely to stay undetected. <!--SR:!2024-11-22,61,310!2024-10-29,44,290-->
- __[memory leak](memory%20leak.md)__ ::: When memory usage is not tracked or is tracked incorrectly. Includes stack exhaustion, heap exhaustion, double free, invalid free, mismatched free, unwanted aliasing, etc. <!--SR:!2024-10-28,40,290!2024-11-05,47,290-->
  - __[stack exhaustion](stack%20overflow.md)__ ::: It occurs when a program runs out of stack space, typically because of too deep [recursion](recursion%20(computer%20science).md). A [guard page](memory%20protection.md) typically halts the program, preventing memory corruption, but functions with large [stack frames](call%20stack.md#STACK-FRAME) may bypass the page. <!--SR:!2024-11-09,48,290!2025-03-08,138,290-->
  - __[heap exhaustion](out%20of%20memory.md)__ ::: The program tries to [allocate](memory%20management.md) more memory than the amount available. In some languages, this condition must be checked for manually after each allocation. <!--SR:!2024-11-23,62,310!2024-11-24,63,310-->
  - __double free__ ::: Repeated calls to [free](c%20dynamic%20memory%20allocation.md) may prematurely free a new object at the same address. If the exact address has not been reused, other corruption may occur, especially in allocators that use [free lists](free%20list.md). <!--SR:!2025-03-12,146,310!2024-10-23,39,290-->
  - __invalid free__ ::: Passing an invalid address to [free](c%20dynamic%20memory%20allocation.md) can corrupt the [heap](memory%20management.md#heap). <!--SR:!2024-11-10,53,310!2024-12-29,82,290-->
  - __mismatched free__ ::: When multiple allocators are in use, attempting to free memory with a deallocation function of a different allocator. <!--SR:!2024-11-04,48,310!2024-11-04,48,310-->
  - __unwanted [aliasing](aliasing%20(computing).md)__ ::: When the same memory location is allocated and modified twice for unrelated purposes. <!--SR:!2024-10-29,45,290!2025-01-29,106,290-->

Some lists may also {{include __[race conditions](race%20condition.md)__ (concurrent reads/writes to shared memory)}} as being part of memory safety (e.g., for access control). The Rust programming language {{prevents many kinds of memory-based race conditions by default, because it ensures there is at most one writer _or_ one or more readers}}. Many other programming languages, such as Java, {{do _not_ automatically prevent memory-based race conditions, yet are still generally considered "memory safe" languages}}. Therefore, {{countering race conditions}} is {{generally _not_ considered necessary for a language to be considered memory safe}}. <!--SR:!2024-12-02,71,310!2024-11-30,69,310!2024-11-05,49,310!2024-11-23,62,310!2024-11-29,68,310-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/memory_safety) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
