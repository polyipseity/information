---
aliases:
  - syscall
  - system call
  - system calls
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/system_call
  - language/in/English
---

# system call

A system call is the programmatic interface through which a running program requests a service from the operating system kernel. It is the only way user-level code can access hardware, create processes, or use kernel-managed resources. The caller knows nothing about how a system call is implemented; it interacts through a system call interface that maps API function calls to kernel-level operations, moving between user mode and kernel mode.

---

Flashcards for this section are as follows:

- overview ::@:: The programmatic interface through which a running program requests a service from the operating system kernel, moving between user mode and kernel mode.
- user mode versus kernel mode ::@:: User mode restricts a program to non-privileged instructions; kernel mode grants full access to hardware and system resources. A system call is the mechanism that transitions between the two.

## API (Application Program Interface) <!-- check: ignore-line[header_style]: API is an acronym -->

An application program interface (API) specifies functions available to application programmers, including parameters and return values. API functions then invoke the actual system call on behalf of the program. For example, Windows `CreateProcess()` invokes the `NTCreateProcess()` system call in the Windows kernel.

Three common APIs exist: Win32 for Windows, POSIX for UNIX-based systems (including Linux and Mac OS X), and the Java API for the Java virtual machine. In UNIX and Linux, C programs access the API through the `libc` standard C library.

APIs have two advantages over direct system calls. Program portability: a program using an API compiles and runs on any system supporting that API, even though system call implementations vary across machines. Abstraction: the caller need not know how the system call is implemented — only what the operating system will do as a result.

A C program calling `printf("Greetings")` illustrates the full chain: the library call invokes the `write()` system call, crossing from user mode into kernel mode and back. The standard C library (`libc` on UNIX/Linux) wraps many system calls into friendlier functions, so programmers rarely invoke system calls directly. The `read()` function takes three parameters: `int fd` (file descriptor), `void *buf` (buffer), and `size_t count` (maximum bytes); it returns `0` for end of file, `-1` for error.

---

Flashcards for this section are as follows:

- API versus direct system calls ::@:: An API specifies functions that application programmers use, including parameters and return values; API functions then invoke the actual system call on the programmer's behalf.
- three common APIs ::@:: Win32 (Windows), POSIX (UNIX, Linux, Mac OS X), and Java API (Java virtual machine).
- advantage of APIs: portability ::@:: A program using an API compiles and runs on any system supporting that API, even though the underlying system call implementations vary across machines.
- advantage of APIs: abstraction ::@:: The caller need not know how the system call is implemented; it need only obey the API format and understand the expected result.
- `cp` involves multiple system calls ::@:: `cp in.txt out.txt` requires a sequence: open source, read, open destination, write, close both.
- `read()` POSIX parameters ::@:: `int fd` (file descriptor), `void *buf` (buffer), `size_t count` (max bytes); returns `0` for EOF, `-1` for error.

## implementation

The run-time environment (RTE) — a set of library functions — provides a system call interface linking user programs to the operating system. Each system call has an identity number, and the interface maintains a table indexed by these numbers.

When a program calls an API function, the system call interface intercepts it, invokes the kernel system call, and returns status and values. The caller stays in user mode; the transition to kernel mode happens inside the interface.

---

Flashcards for this section are as follows:

- system call interface ::@:: The component of the run-time environment that intercepts API function calls, maps each to a numbered system call, invokes it in the kernel, and returns the status and any values to the caller.
- system call number ::@:: An identity number associated with each system call, used to index into a table that routes the call to its kernel implementation.

## parameter passing

A system call often requires more than its identity. The type and amount of data vary by OS and call. Three methods pass parameters from user programs to the operating system.

The simplest passes parameters in registers, though this is limited by register count. The block method stores parameters in a memory table and passes the table address in a register. The stack method pushes parameters onto the stack and pops them off in the kernel. Block and stack methods have no limit on parameter count or length.

---

Flashcards for this section are as follows:

- parameter passing: register method ::@:: Parameters are passed directly in CPU registers; the simplest method but limited by the number of available registers.
- parameter passing: block method ::@:: Parameters are stored in a block or table in memory, and the address of that block is passed in a register.
- parameter passing: stack method ::@:: Parameters are pushed onto the stack by the calling program and popped off by the operating system, with no limit on the number or length of parameters.

## types

System calls are grouped into six major categories by the service they provide.

__Process control__ system calls handle creating and terminating processes (`CreateProcess`, `fork`, `exit`), loading and executing programs (`exec`), getting and setting process attributes, waiting for time or events, signalling events, allocating and freeing memory, dumping memory on error, and providing debugger and lock facilities for managing shared data between processes.

__File management__ system calls create and delete files (`CreateFile`, `open`), open and close them, read, write, and reposition, and get and set file attributes.

__Device management__ system calls request and release devices, read, write, and reposition them, get and set device attributes, and logically attach or detach devices.

__Information maintenance__ system calls get and set the time or date, get system data, and get and set process, file, or device attributes.

__Communications__ system calls create and delete communication connections, send and receive messages under the message passing model (or create and gain access to memory regions under the shared-memory model), transfer status information, and attach and detach remote devices.

__Protection__ system calls control access to resources, get and set permissions, and allow or deny user access.

The following table compares equivalent system calls across Windows and UNIX:

| Category | Windows | UNIX |
| --- | --- | --- |
| Process control | `CreateProcess()`, `ExitProcess()`, `WaitForSingleObject()` | `fork()`, `exit()`, `wait()` |
| File management | `CreateFile()`, `ReadFile()`, `WriteFile()`, `CloseHandle()` | `open()`, `read()`, `write()`, `close()` |
| Device management | `SetConsoleMode()`, `ReadConsole()`, `WriteConsole()` | `ioctl()`, `read()`, `write()` |
| Information maintenance | `GetCurrentProcessID()`, `SetTimer()`, `Sleep()` | `getpid()`, `alarm()`, `sleep()` |
| Communications | `CreatePipe()`, `CreateFileMapping()`, `MapViewOfFile()` | `pipe()`, `shm_open()`, `mmap()` |
| Protection | `SetFileSecurity()`, `InitializeSecurityDescriptor()` | `chmod()`, `umask()`, `chown()` |

---

Flashcards for this section are as follows:

- six categories of system calls ::@:: Process control, file management, device management, information maintenance, communications, and protection.
- process control system calls ::@:: Create and terminate processes, load and execute programs, get and set attributes, wait and signal events, allocate and free memory, and manage shared data locks.
- file management system calls ::@:: Create, delete, open, close, read, write, reposition files, and get and set file attributes.
- communications system calls ::@:: Create and delete connections, send and receive messages (message passing) or create shared memory regions, transfer status, and attach remote devices.
- protection system calls ::@:: Control access to resources, get and set permissions, and allow or deny user access.
- Windows versus UNIX process creation ::@:: Windows uses `CreateProcess()` as a single call; UNIX uses `fork()` to create a copy of the calling process, then `exec()` to load a new program into it.
