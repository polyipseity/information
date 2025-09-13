---
aliases:
  - memory safe
  - memory safeties
  - memory safety
  - memory unsafe
  - memory unsafeties
  - memory unsafety
tags:
  - flashcard/active/general/eng/memory_safety
  - language/in/English
---

# memory safety

- This article is about protection of memory in software development. For hardware protection of memory, see [memory protection](memory%20protection.md).

__Memory safety__ is {@{the state of being protected from various [software bugs](software%20bug.md) and [security vulnerabilities](vulnerability%20(computer%20security).md) when dealing with [memory](random-access%20memory.md) access}@}, such as {@{[buffer overflows](buffer%20overflow.md) and [dangling pointers](dangling%20pointer.md)}@}. For example, [Java](java%20(programming%20language).md) is said {@{to be memory-safe}@} because {@{its [runtime error detection](runtime%20error%20detection.md) checks array bounds and pointer dereferences}@}. In contrast, [C](c%20(programming%20language).md) and [C++](C++.md) {@{allow arbitrary [pointer arithmetic](pointer%20(computer%20programming).md) with pointers implemented as direct memory addresses with no provision for [bounds checking](bounds%20checking.md)}@}, and thus {@{are potentially __memory-unsafe__}@}.

## types of memory errors

Many different types of memory errors can occur. Important one includes {@{access errors, uninitialized variables, and memory leak}@}.

- __access errors__ ::@:: Invalid read/write of a pointer. Includes buffer overflow, buffer over-read, invalid page fault, use after free, etc.
  - __[buffer overflow](buffer%20overflow.md)__ ::@:: Out-of-bound writes can corrupt the content of adjacent objects, or internal data (like bookkeeping information for the [heap](memory%20management.md#HEAP)) or [return](return%20statement.md) addresses.
  - __[buffer over-read](buffer%20over-read.md)__ ::@:: Out-of-bound reads can reveal sensitive data or help attackers bypass [address space layout randomization](address%20space%20layout%20randomization.md).
  - __[invalid page fault](page%20fault.md#invalid)__ ::@:: Accessing a pointer outside the virtual memory space. A null pointer dereference will often cause an exception or program termination in most environments, but can cause corruption in operating system [kernels](kernel%20(operating%20system).md) or systems without [memory protection](memory%20protection.md), or when use of the null pointer involves a large or negative offset.
  - __use after free__ ::@:: Dereferencing a [dangling pointer](dangling%20pointer.md) storing the address of an object that has been deleted.
- __[uninitialized variables](uninitialized%20variable.md)__ ::@:: A variable that has not been assigned a value is used. It may contain an undesired or, in some languages, a corrupt value. Includes null pointer deference, wild pointers, etc.
  - __[null pointer](null%20pointer.md) dereference__ ::@:: Dereferencing an invalid pointer or a pointer to memory that has not been allocated
  - __[wild pointers](dangling%20pointer.md)__ ::@:: Arises when a pointer is used prior to initialization to some known state. They show the same erratic behaviour as dangling pointers, though they are less likely to stay undetected.
- __[memory leak](memory%20leak.md)__ ::@:: When memory usage is not tracked or is tracked incorrectly. Includes stack exhaustion, heap exhaustion, double free, invalid free, mismatched free, unwanted aliasing, etc.
  - __[stack exhaustion](stack%20overflow.md)__ ::@:: It occurs when a program runs out of stack space, typically because of too deep [recursion](recursion%20(computer%20science).md). A [guard page](memory%20protection.md) typically halts the program, preventing memory corruption, but functions with large [stack frames](call%20stack.md#STACK-FRAME) may bypass the page.
  - __[heap exhaustion](out%20of%20memory.md)__ ::@:: The program tries to [allocate](memory%20management.md) more memory than the amount available. In some languages, this condition must be checked for manually after each allocation.
  - __double free__ ::@:: Repeated calls to [free](c%20dynamic%20memory%20allocation.md) may prematurely free a new object at the same address. If the exact address has not been reused, other corruption may occur, especially in allocators that use [free lists](free%20list.md).
  - __invalid free__ ::@:: Passing an invalid address to [free](c%20dynamic%20memory%20allocation.md) can corrupt the [heap](memory%20management.md#heap).
  - __mismatched free__ ::@:: When multiple allocators are in use, attempting to free memory with a deallocation function of a different allocator.
  - __unwanted [aliasing](aliasing%20(computing).md)__ ::@:: When the same memory location is allocated and modified twice for unrelated purposes.

Some lists may also {@{include __[race conditions](race%20condition.md)__ \(concurrent reads/writes to shared memory\)}@} as {@{being part of memory safety \(e.g., for access control\)}@}. {@{The Rust programming language}@} prevents {@{many kinds of memory-based race conditions by default}@}, because it {@{ensures there is at most one writer _or_ one or more readers}@}. {@{Many other programming languages, such as Java}@}, do _not_ {@{automatically prevent memory-based race conditions, yet are still generally considered "memory safe" languages}@}. Therefore, {@{countering race conditions}@} is {@{generally _not_ considered necessary for a language to be considered memory safe}@}.

## references

This text incorporates [content](https://en.wikipedia.org/wiki/memory_safety) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
