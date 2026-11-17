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

A system call is how a running program asks the kernel for a service. User-level code reaches hardware, new processes and kernel-managed resources no other way. The caller never sees the implementation: a system call interface maps application program interface (API) functions onto kernel operations and switches between user mode and kernel mode.

---

Flashcards for this section are as follows:

- what a system call is ::@:: The interface through which a running program asks the kernel for a service, switching between user mode and kernel mode.
- what user mode and kernel mode each allow ::@:: User mode restricts a program to non-privileged instructions; kernel mode grants full access to hardware and system resources, and a system call moves between the two.

<!-- check: ignore-next-line[header_style]: API is an acronym -->
## API (Application Program Interface)

An application program interface (API) lists the functions an application programmer may call, with their parameters and return values. Each one invokes the real system call: Windows `CreateProcess()`, for instance, invokes `NTCreateProcess()` in the kernel.

Three APIs cover most programs: Win32 for Windows, POSIX for UNIX-based systems (Linux, Mac OS X), and the Java API for the Java virtual machine. On UNIX and Linux, C programs reach the API through `libc`.

An API program compiles and runs wherever that API exists, even though implementations differ. Its caller also need not know how the call is implemented, only what it does.

`printf("Greetings")` shows the chain: the library call invokes `write()`, which crosses into kernel mode and back. The standard C library (`libc` on UNIX/Linux) wraps many system calls this way, so programmers rarely call the kernel directly.

---

Flashcards for this section are as follows:

- how an application program interface (API) relates to a system call ::@:: An application program interface (API) lists the functions an application programmer may call, with their parameters and return values; each invokes the actual system call.
- three common application program interfaces (APIs) ::@:: Win32 for Windows, POSIX for UNIX-based systems (UNIX, Linux, Mac OS X), and the Java API for the Java virtual machine.
- advantage of APIs: portability ::@:: A program written against an application program interface (API) runs anywhere that supports it, even though the system calls underneath differ.
- advantage of APIs: abstraction ::@:: The caller need not know how the system call is implemented, only the application program interface (API) format and the expected result.

### system calls behind a file copy

```c
#include <fcntl.h>
#include <unistd.h>

int open(const char *path, int flags, ... /* mode_t mode */);  /* fd, or -1 */
ssize_t read(int fd, void *buf, size_t count);                 /* bytes, 0 at end, -1 */
ssize_t write(int fd, const void *buf, size_t count);          /* bytes written, or -1 */
int close(int fd);                                             /* 0, or -1 */
```

A copy opens both files, moves the bytes in a loop, then closes both.

```c
#include <fcntl.h>
#include <unistd.h>

int main(void)
{
    char buf[4096];
    int in = open("input.txt", O_RDONLY);                  /* flags alone, so no mode */
    if (in == -1)
        return 1;
    int out = open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);  /* mode with O_CREAT */
    if (out == -1)
        return 1;

    ssize_t n;
    while ((n = read(in, buf, sizeof buf)) > 0) {           /* 0 is the end of the file */
        ssize_t done = 0;
        while (done < n) {                                  /* a short write is legal */
            ssize_t w = write(out, buf + done, (size_t) (n - done));
            if (w == -1)
                return 1;
            done += w;
        }
    }
    if (n == -1 || close(out) == -1 || close(in) == -1)
        return 1;
    return 0;
}
```

---

Flashcards for this section are as follows:

- prototype of `open()` ::@:: `int open(const char *path, int flags, ...)`, called as `open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644)`: needs `mode_t` only with `O_CREAT`, and returns a descriptor or `-1` with `errno`.
- prototype of `read()` ::@:: `ssize_t read(int fd, void *buf, size_t count)`, called as `read(in, buf, sizeof buf)`: fills the buffer and returns the bytes read, `0` at the end of the file, or `-1`.
- prototype of `write()` ::@:: `ssize_t write(int fd, const void *buf, size_t count)`, called as `write(out, buf + done, (size_t) (n - done))`: writes the bytes still owed from the buffer and returns how many it took, possibly fewer.
- prototype of `close()` ::@:: `int close(int fd)`, called as `close(out)`: frees the descriptor and returns `0`, or `-1` with `errno` set.
- what a short count from `read()` or `write()` means ::@:: The `ssize_t` return counts the bytes transferred, so a smaller count means fewer bytes were available or accepted; the caller loops for the rest.

### flags of open()

Flags are joined with `|`. Exactly one of `O_RDONLY`, `O_WRONLY` and `O_RDWR` is required and sets the access mode.

The rest are optional. `O_CREAT` creates the file when the name is absent, and only then does the mode matter. `O_EXCL` with `O_CREAT` fails the call when the name exists, so a program can claim it. `O_TRUNC` empties an existing file, so writing starts at byte zero. `O_APPEND` writes at the current end, so two appenders cannot overwrite each other. `O_NONBLOCK` returns instead of waiting, which matters for a FIFO with no partner or a device with no data.

`open` returns the lowest descriptor the process has free, or `-1` with the reason in `errno`. Descriptors `0`, `1` and `2` are standard input, standard output and standard error, so a fresh `open` usually returns `3`.

---

Flashcards for this section are as follows:

- access modes of `open()`, and how many the flags take ::@:: Exactly one of `O_RDONLY`, `O_WRONLY` and `O_RDWR` is required.
- what `O_CREAT` and `O_EXCL` do together ::@:: `O_CREAT` creates the file when the name is free; `O_EXCL` fails the call when the name exists, so the program claims the name first.
- what `O_TRUNC` does to a file that exists ::@:: It empties the file, so the next write starts at the beginning.
- what `O_APPEND` guarantees when writers share a file ::@:: Every write goes to the current end, so appenders cannot overwrite each other's bytes.
- what `O_NONBLOCK` changes about `open()` ::@:: The call returns instead of waiting, which matters for a FIFO with no partner or a device with no data.
- descriptor `open()` returns ::@:: The lowest free descriptor; `0`, `1` and `2` already belong to standard input, standard output and standard error.
- arguments of `read()` ::@:: `fd` names an open descriptor, `buf` the memory to fill, and `count` the most bytes the call may take.
- arguments of `write()` ::@:: `fd` the open descriptor to send through, `buf` the bytes to send, and `count` how many of them.

### permission bits

The third argument of `open()` gives the permissions of a file the call creates; the kernel reads it only when the flags contain `O_CREAT`. `mkfifo()` takes the same bits in its mode argument.

Nine constants spell the bits out: `S_I`, then the access (`R`, `W` or `X`), then the class (`USR`, `GRP` or `OTH`). The classes follow the digits of a mode: owner, group, others. Inside one class read is 4, write 2, execute 1.

| Constant | Octal | Permission |
| --- | --- | --- |
| `S_IRUSR` | `0400` | owner reads |
| `S_IWUSR` | `0200` | owner writes |
| `S_IXUSR` | `0100` | owner executes |
| `S_IRGRP` | `0040` | group reads |
| `S_IWGRP` | `0020` | group writes |
| `S_IXGRP` | `0010` | group executes |
| `S_IROTH` | `0004` | others read |
| `S_IWOTH` | `0002` | others write |
| `S_IXOTH` | `0001` | others execute |

`S_IRUSR | S_IWUSR` says what `0600` says: the owner reads and writes, nobody else gets anything. Read `0644` one digit at a time, 6 for the owner, 4 for the group, 4 for others, and `ls -l` prints `-rw-r--r--`.

The umask clears the bits it names before the file is created, so `0666` under the usual `022` lands as `0644`. An existing path keeps its permissions; the mode applies only where this call creates the file.

---

Flashcards for this section are as follows:

- what the third argument of `open()` sets, and when the kernel reads it ::@:: It sets the permissions of a file the call creates, and matters only when the flags contain `O_CREAT`.
- three permission classes of a file, in the order an octal mode lists them ::@:: The digits list the owner (user), then the group, then others.
- octal value of read, write and execute inside one class ::@:: Read is 4, write is 2, execute is 1; a class digit adds the three it grants.
- permissions of `0644`, and the line `ls -l` prints ::@:: The owner reads and writes (6), the group reads (4), others read (4), printed as `-rw-r--r--`.
- permissions of `0600`, and the line `ls -l` prints ::@:: The owner reads and writes, the group and others get nothing, printed as `-rw-------`.
- how `0640` reads in words ::@:: The owner reads and writes, the group reads, others get nothing, printed as `-rw-r-----`.
- how `S_IRUSR | S_IWUSR` compares with `0600` ::@:: The bits are the same: `S_IRUSR` is `0400` and `S_IWUSR` is `0200`, so the OR is `0600`.
- how a permission constant is built, and what `S_IXOTH` grants ::@:: Each name is `S_I`, then the access `R`, `W` or `X`, then the class `USR`, `GRP` or `OTH`; `S_IXOTH` grants execute to others, octal `0001`.
- order of the three digits of a mode ::@:: Owner, group, others, the same order the constant names use: `USR`, `GRP`, `OTH`.
- what a umask does to the mode argument ::@:: It clears the named bits before the file is created, so `0666` under the usual `022` gives `0644`.
- permissions of a file that already exists when `open()` passes `O_CREAT` ::@:: They stay unchanged, because the mode applies only where the call creates the file.

## system call interface

The run-time environment (RTE) is a set of library functions that provides the system call interface between user programs and the operating system. The interface intercepts application program interface (API) calls, maps each to a numbered system call, looks up that number in a table of kernel entry points, invokes the call in kernel mode, and returns its status and values to the user program.

---

Flashcards for this section are as follows:

- what the system call interface does ::@:: The part of the run-time environment that intercepts application program interface (API) function calls, maps each to a numbered system call, indexes a table of kernel entry points with that number, invokes the call in the kernel, and returns its status and values.
- what a system call number is used for ::@:: The identity number of a system call, used to index a table that routes it to its kernel implementation.

## mode transfer

Control starts in kernel mode and passes to a user program in user mode. It comes back only three ways, and each is a mode transfer.

A system call is the first way: a program asks the kernel for a service, such as `read()` or `exit()`. The call crosses into the kernel like a function call made outside the process, and the kernel returns to user mode when it finishes.

An interrupt is the second way. It is external and asynchronous, raised by a timer or a device finishing input/output (I/O). A timer interrupt is what guarantees control returns to the kernel, even if a program never calls one.

A trap, or exception, is the third way. It is internal and synchronous, raised by the instruction the process is running: a protection violation such as a segmentation fault, or an arithmetic error such as division by zero.

---

Flashcards for this section are as follows:

- three ways control returns to the kernel ::@:: A system call, an interrupt, or a trap or exception.
- whose events a system call, an interrupt and a trap each are ::@:: A system call comes from the process asking for a service; an interrupt is external and asynchronous, from a timer or a device; a trap is internal and synchronous, from the running instruction.
- why a timer interrupt matters ::@:: It guarantees the kernel regains control, even if a program never issues a system call.
- how a system call differs from a function call ::@:: A system call looks like one but runs outside the calling process, crossing from user mode to kernel mode and back.

### walkthrough of a read()

Start with a user program calling `read(fd, buf, 4096)`. The standard C library puts the system call number for `read` in the register the kernel expects and executes a trap instruction. The processor switches to kernel mode and jumps to that trap's handler.

The handler reads the number, indexes the system call table with it and calls the kernel's `read` implementation. That implementation checks the descriptor and the buffer, finds the file position and asks the device for the bytes.

If the data is not in memory, the kernel starts the transfer, marks the process waiting and runs the scheduler, so another process takes the processor. The device raises an interrupt when the transfer finishes. The interrupt handler copies the bytes into the process's buffer, marks the process ready and records how many bytes were read.

The kernel restores the user registers, switches back to user mode and returns to the library. The library call hands the byte count to the program, `0` at end of file, or `-1` with `errno` on error.

---

Flashcards for this section are as follows:

- what a C library call does before the mode transfer ::@:: It puts the system call number in the register the kernel expects and executes a trap instruction.
- what the trap handler does with the system call number ::@:: It indexes the system call table with the number and calls the kernel's `read` implementation.
- what happens to a process when `read()` must wait for a device ::@:: The kernel starts the transfer, marks the process waiting and runs the scheduler, so another process takes the processor.
- how `read()` finishes after a device raises an interrupt ::@:: The interrupt handler copies the bytes into the user's buffer, marks the process ready and records the count; the kernel restores registers, switches to user mode and returns that count.
- what `read()` returns to the program ::@:: The byte count, `0` at end of file, or `-1` with `errno` on error.

## parameter passing

Three methods carry parameters from user programs to the operating system.

The register method is simplest, but registers are few. The block method stores them in a table in memory and passes its address in one register. The stack method pushes them onto the stack, and the kernel pops them off. Neither block nor stack limits the parameter count or length.

---

Flashcards for this section are as follows:

- how the register method of parameter passing works ::@:: Parameters go directly in central processing unit (CPU) registers. It is the simplest method, but registers are few.
- parameter passing: block method ::@:: Parameters sit in a block or table in memory, and its address is passed in a register.
- parameter passing: stack method ::@:: The calling program pushes the parameters onto the stack and the operating system pops them off, with no limit on their number or length.

## categories

Six categories cover the services system calls provide.

__Process control__ system calls create and end processes (`CreateProcess`, `fork`, `exit`) and load and run programs (`exec`). They also get and set process attributes, wait for and signal events, allocate memory, dump it on error, and lock and debug shared data.

__File management__ system calls create and delete files (`CreateFile`, `open`), open and close them, read, write and reposition, and get or set their attributes.

__Device management__ system calls request and release devices, read, write and reposition them, get or set attributes, and attach or detach them logically.

__Information maintenance__ system calls get or set the time and date, read system data, and get or set process, file or device attributes.

__Communications__ system calls create and delete connections, send and receive messages by message passing or share a region under shared memory, transfer status, and attach or detach remote devices.

__Protection__ system calls control access to resources by getting and setting permissions and by allowing or denying a user.

The table maps equivalent system calls across Windows and UNIX:

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
- what process control system calls do ::@:: Create and terminate processes, load and execute programs, get and set attributes, wait for and signal events, allocate and free memory, and manage locks on shared data.
- what file management system calls do ::@:: Create, delete, open and close files, read, write and reposition them, and get and set file attributes.
- what communications system calls do ::@:: Create and delete connections, send and receive messages by message passing or create shared memory regions, transfer status, and attach remote devices.
- what protection system calls do ::@:: Control access to resources, get and set permissions, and allow or deny user access.
- Windows versus UNIX process creation ::@:: Windows uses one call, `CreateProcess()`; UNIX uses `fork()` to copy the calling process, then `exec()` to load a new program into it.
