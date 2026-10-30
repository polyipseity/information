---
aliases:
  - COMP 3511 thread
  - thread
  - thread (computing)
  - thread of execution
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/thread_(computing)
  - language/in/English
---

# thread (computing)

A thread is one flow of execution inside a process. It owns a program counter, registers and a stack; the code, the data and the open files belong to the process, so every thread reaches the same copies.

Work split into threads instead of processes stays in one address space, so a thread costs less to create and switch than a process. The shared data is also why the program must stop two threads changing it at once.

---

Flashcards for this section are as follows:

- what a thread is in a process ::@:: One flow of execution inside the process, with its own program counter, registers and stack, sharing the process's code, data and open files.
- why a thread costs less than a process ::@:: The threads of one process share an address space, so creating a thread or switching between two takes less work than with a process.
- what goes wrong in a multithreaded program without care ::@:: The threads see the same data, so the program must keep them from changing it at once.

## thread components

A thread is the unit the processor is handed, and it is scheduled and run in its own right. It holds a thread identifier, a program counter, a register set, a stack and execution flags.

The program counter says which instruction the thread fetches next; the registers hold the part of its state that is not in memory. A thread runs on a processor exactly while its state sits in those registers.

The kernel represents a thread with a thread control block (TCB). It holds the execution state: the registers, the program counter and a pointer to the stack. It also holds scheduling information such as state, priority and processor time, accounting information, the pointers that queue the thread for the scheduler, and a pointer to the process control block of its process.

Threads are the active part of a process, the address space the passive part: threads carry concurrency, the address space protection from other processes. A process with several threads has no state of its own, only a state for each thread. A new thread is cheap, since the process and its data structures stay as they are and it adds only a thread control block and a stack.

---

Flashcards for this section are as follows:

- components of a thread ::@:: A thread identifier, a program counter, a register set, a stack and execution flags.
- what a thread shares with other threads of its process ::@:: The code, the data, the heap, the open files and the signals. All threads of a process run in one address space.
- thread control block (TCB) ::@:: The kernel structure for one thread: execution state, scheduling information, accounting information, queue pointers and a pointer to the process control block of its process.
- active and passive parts of a process ::@:: Threads are the active part and carry concurrency; the address space is the passive part and carries protection from other processes.
- state of a process with several threads ::@:: The process has no state of its own. Each thread has one, and a thread control block holds it.
- thread as the unit of scheduling ::@:: The scheduler hands a core to a thread, so a thread is what runs and gets switched out.
- when a thread is running on a processor ::@:: Exactly while its state sits in the processor's registers. Until then the state waits in memory.
- cost of creating a thread against cost of creating a process ::@:: A new thread needs only a thread control block and a stack; the process and its data structures stay unchanged, so it takes far less work than a process.

## benefits of multithreading

Several threads in one process give four benefits:

- Responsiveness keeps the program answering while one of its threads blocks.
- Resource sharing needs no setup, since the threads already share their process's memory.
- Economy favours threads: one takes less time and memory to create than a process, and switching between two threads of one process is faster than switching between two processes.
- Scalability puts the threads on several cores at once.

A web browser shows the first two: one thread draws the images and text the user sees while another fetches data over the network, so a slow network does not freeze the window. A word processor runs three threads: one draws the text, a second reads keystrokes, a third checks spelling in the background.

---

Flashcards for this section are as follows:

- four benefits of multithreading ::@:: Responsiveness, resource sharing, economy and scalability.
- responsiveness given by threads ::@:: If one thread blocks, the others keep running, so an interactive program still answers the user.
- resource sharing among threads ::@:: Threads share the memory of their process by default, so nothing has to be set up and nothing passes as a message.
- economy of threads ::@:: A thread takes less time and memory to create than a process, and switching between two threads of one process is faster than between two processes.
- scalability of threads ::@:: Threads of one process can run at the same time on several cores.
- browser threads ::@:: A web browser may draw images or text in one thread while another fetches data from the network.
- word processor threads ::@:: A word processor may draw text in one thread, read keystrokes in a second and check spelling in a third.

## concurrency and parallelism

Concurrency means several tasks are in progress over the same period. On one core they take turns, each running a slice before the scheduler switches, so the tasks overlap in time while only one executes at any instant. Parallelism means several tasks execute at the same instant, each on a core of its own. A single core is concurrent, never parallel. Several cores give parallelism only to a program with work to spread.

Two threads on one core show concurrency alone. The first computes while the second waits for a disk, and the core goes to the first during that wait, so both make progress though neither ever runs beside the other. On two cores with no shared data the same pair shows parallelism: each holds a core and both advance at once. A browser drawing its interface in one thread while another downloads a file is concurrent on any machine; splitting one image across eight cores is parallel.

Concurrency hides waits and keeps the processor busy, so an interactive program responds sooner. Parallelism shortens the elapsed time of a divisible workload, and the serial part of a program caps what extra cores can add.

---

Flashcards for this section are as follows:

- concurrency ::@:: Several tasks in progress over the same period, interleaved by the scheduler, at most one executing at any instant.
- parallelism ::@:: Several tasks execute at the same instant, each on a core of its own.
- difference between concurrency and parallelism ::@:: Concurrency interleaves many tasks on one core. Parallelism runs many tasks at one instant on several cores.
- two threads on one core as an example of concurrency ::@:: One thread computes while the other waits for a disk, and the core goes to the computing thread during that wait, so both progress though never at once.
- why a single core cannot be parallel ::@:: One core runs one instruction stream at a time, so tasks take turns and never run at the same instant.
- what several cores add to a program ::@:: Parallelism, and only for work that splits into independent parts; a program with no independent work runs one part at a time.
- what concurrency buys an interactive program ::@:: It hides waits such as a blocking disk read and keeps the processor busy, so the program responds sooner.
- what parallelism buys a divisible workload ::@:: A shorter elapsed time, bounded by the serial part of the program that no extra core can shorten.

## multicore programming

A multicore chip puts several computing cores on one piece of silicon. The hardware case for it over several single-core chips is in [multiprocessing](multiprocessing.md#multicore%20systems). Software is harder: the work itself must be split across the cores, and the serial part caps the gain. A program that is three quarters parallel gains about 1.6 times from a second core, not twice.

---

Flashcards for this section are as follows:

- limit on the gain from more cores ::@:: The serial part of a program bounds the gain. A program that is three quarters parallel gains about 1.6 times from a second core, not twice.

### design challenges

Splitting a program across cores brings five problems:

- The work must be cut into separate tasks that can run at once.
- The tasks must balance, so each does about the same amount of work and no core sits idle at the end.
- The data the tasks use must be divided too, so each core works on its own part.
- Where two tasks share a data dependency, the program must synchronize them.
- Testing and debugging get harder, because the path of execution differs from run to run.

---

Flashcards for this section are as follows:

- challenges of multicore programming ::@:: Dividing the work into tasks, balancing it, splitting the data, handling data dependencies, testing and debugging.
- task balancing across cores ::@:: Each task should do about the same amount of work, or some cores finish early and sit idle.
- data dependency between tasks ::@:: Two tasks need the same data in a fixed order, so the program must synchronize them.
- why parallel programs are hard to test ::@:: The path of execution varies between runs, so a fault may appear in one run and not in the next.

### data and task parallelism

Data parallelism spreads subsets of the same data over the cores and runs one operation on each, a pattern common in distributed machine learning. Task parallelism gives each core a different task. An application may use both.

---

Flashcards for this section are as follows:

- data parallelism ::@:: The same operation runs on every core, each over a different subset of the data.
- task parallelism ::@:: Each core runs a different task, so each does a different operation.
- combined parallelism ::@:: One application can use both data parallelism and task parallelism.

## user threads and kernel threads

A user thread is the abstraction a program works with. A library creates it, keeps its stack and bookkeeping in the process's own memory, and offers the create, join and synchronize calls a programmer writes. A kernel thread is what the operating system schedules: it owns a thread control block, and only the scheduler can put it on a core.

The library can create and order user threads, but cannot give one a processor. The kernel can schedule threads, but knows nothing of the ones the library invented. A user thread runs only while a kernel thread carries it, and the multithreading model is how that carrying is arranged. Only kernel threads are scheduled, and a thread control block belongs to one, which runs kernel code or a user program.

The examples sit on one level or the other, with one case mapped between them:

- pthreads on Linux, Windows threads and Java threads are library threads. Each is bound one-to-one to a kernel thread today, so the library object is a handle on a kernel entity the scheduler can place.
- Solaris Green Threads and GNU Portable Threads create user threads with no kernel thread of their own. All of them are multiplexed onto the single kernel thread the process has.
- Windows with the ThreadFiber package multiplexed its library threads onto several kernel threads, a many-to-many mapping.
- Linux has one construct at both levels. Every thread and every process is a task, and the `clone()` flags decide which resources the new task shares with its parent, so a pthreads thread is a task sharing the address space.
- A kernel thread needs no user program. The kernel runs its own, such as one writing dirty pages back to disk, and the scheduler treats them like any other thread.

Three thread libraries are common: Portable Operating System Interface (POSIX) threads, usually called pthreads, Windows threads and Java threads. Windows, Linux, macOS, iOS and Android all have kernel threads underneath.

---

Flashcards for this section are as follows:

- user thread ::@:: The library-level abstraction a program works with: a thread library creates and manages it in the process's own memory, unknown to the kernel.
- kernel thread ::@:: The operating-system construct a scheduler can put on a core, with its own thread control block and the resources behind it.
- why the two thread levels need each other ::@:: The library can create and order user threads but cannot give one a processor; the kernel can schedule threads but knows nothing of the ones the library invented.
- which threads the kernel schedules ::@:: Only kernel threads. A user thread runs only while a kernel thread carries it.
- which thread gets a thread control block (TCB) ::@:: A kernel thread. The thread control block and the resources behind it belong to it.
- level of a pthreads, Windows or Java thread ::@:: A library thread bound one-to-one to a kernel thread, little more than a handle on a kernel entity the scheduler places.
- level of a Solaris Green Thread or a GNU Portable Thread ::@:: A user thread with no kernel thread of its own, multiplexed onto the single kernel thread the process has.
- level of a ThreadFiber thread in Windows ::@:: A library thread multiplexed onto several kernel threads, a many-to-many mapping.
- how Linux represents threads and processes ::@:: As one construct, the task. The `clone()` flags decide which resources the new task shares with its parent; a thread is a task sharing the address space.
- kernel thread with no user program ::@:: A thread the kernel runs for itself, such as one writing dirty pages back to disk, scheduled like any other.
- the three common thread libraries ::@:: Portable Operating System Interface (POSIX) threads, usually called pthreads, Windows threads and Java threads.
- do general-purpose systems support kernel threads ::@:: Windows, Linux, macOS, iOS and Android all do.

## multithreading models

A user thread lives in a library and a kernel thread in the kernel, so a mapping has to carry each user thread to one. Without it, no user thread reaches a core. Three mappings are common, two of them resting on an intermediate object, the lightweight process.

Not every system keeps threads and processes apart. Linux calls both a task, so a thread is a task that shares the address space, and each task has its own task_struct. Windows keeps the distinction: one process structure describes the shared resources and points at one thread structure per thread.

---

Flashcards for this section are as follows:

- why user threads must be mapped to kernel threads ::@:: A user thread is invisible to the kernel, and only a kernel thread runs on a core, so one has to carry it.
- threads in Linux ::@:: Linux does not separate threads from processes. Each is a task with its own task_struct, and a thread is a task sharing resources such as the address space.
- threads in Windows ::@:: One process structure describes the shared resources, such as the address space and open files, and points to a thread structure per thread.

### many-to-one model

Many user threads map to one kernel thread. The library decides in user space which user thread that kernel thread runs, which is [process-contention scope](scheduling%20(computing).md#process-contention%20scope%20and%20system-contention%20scope), and the kernel takes no part. If the kernel thread blocks, every user thread mapped to it blocks with it and the whole process stops. One kernel thread rules out two threads in parallel. Few systems use the model; Solaris Green Threads and GNU Portable Threads did.

---

Flashcards for this section are as follows:

- many-to-one model ::@:: Many user threads are mapped to a single kernel thread.
- advantage of the many-to-one model ::@:: All thread management happens in the user-space library, with no help from the kernel.
- cost of the many-to-one model ::@:: If the one kernel thread blocks, every user thread mapped to it blocks, so the whole process stops.
- parallelism in the many-to-one model ::@:: None across cores. One kernel thread exists, so one thread is active at a time.

### one-to-one model

Each user thread maps to a kernel thread of its own, which gives the most concurrency: when one thread blocks another runs, and threads run in parallel on several cores. Every user thread needs a kernel thread, and each costs memory and other resources, so systems limit how many threads a process may hold. Windows and Linux use the model, and most systems have moved to it.

---

Flashcards for this section are as follows:

- one-to-one model ::@:: Each user thread is mapped to its own kernel thread.
- advantage of the one-to-one model ::@:: It gives the most concurrency: another thread keeps running when one blocks, and threads run in parallel on several cores.
- cost of the one-to-one model ::@:: Every user thread needs its own kernel thread, and each costs memory and other resources, so threads per process are limited.
- which systems use the one-to-one model ::@:: Windows and Linux, and most operating systems today.

### many-to-many model

The many-to-many model multiplexes many user threads onto a smaller or equal number of kernel threads, so the user thread count does not follow the kernel thread count. Concurrency sits between many-to-one and one-to-one, and the operating system can create a pool of kernel threads in advance. One variant adds an option to this mapping, covered next. The model is the most flexible and the hardest to implement, because the operating system and the thread library must agree on the mapping. Windows with the ThreadFiber package used it; few others do. More cores on a chip make the limit on kernel threads matter less.

---

Flashcards for this section are as follows:

- many-to-many model ::@:: Many user threads are multiplexed onto a smaller or equal number of kernel threads.
- concurrency of the many-to-many model ::@:: More than many-to-one and less than one-to-one, while the user thread count is not limited by the kernel thread count.
- thread pool ::@:: A set of kernel threads the operating system creates in advance, so a user thread gets one without a new thread.
- cost of the many-to-many model ::@:: The hardest model to implement, because the operating system and the thread library must coordinate the mapping. It is also the most flexible.

### two-level model

The two-level model is the many-to-many model with one addition: a user thread may be bound to a kernel thread of its own. Most user threads stay multiplexed onto the pool; a bound one keeps a kernel thread to itself, so the library cannot multiplex another user thread onto it.

---

Flashcards for this section are as follows:

- two-level model ::@:: The many-to-many model plus the ability to bind a user thread to a kernel thread of its own.
- how a bound thread sits in the two-level model ::@:: It keeps a kernel thread to itself, while the other user threads stay multiplexed onto the pool.
- cost of binding a user thread in the two-level model ::@:: The library cannot multiplex another user thread onto that kernel thread.

### lightweight process

A lightweight process is the library's handle on a kernel thread: a virtual processor the library schedules user threads onto, backed by one kernel thread the kernel schedules. The library decides which user thread runs on each lightweight process; the kernel decides which lightweight process runs on which core. On Solaris it was a kernel object carrying the register state and signal mask of the thread sitting on it.

The many-to-one and many-to-many models need that handle: the library has a scheduling decision to make and needs something schedulable to attach it to. The one-to-one model has no such decision. Each user thread already owns a kernel thread, so an intermediate object would only repeat an identity it already has. Linux and Windows do without one.

A lightweight process runs only while its kernel thread runs, so a blocking call in one stops every user thread on it, and a preempted kernel thread stops them as well. The library can move a user thread to another lightweight process only where it controls the switch.

---

Flashcards for this section are as follows:

- lightweight process (LWP) ::@:: The thread library's handle on a kernel thread, a virtual processor for scheduling user threads.
- who decides what in a lightweight process ::@:: The library decides which user thread runs on each lightweight process, and the kernel decides which lightweight process runs on which core.
- what a Solaris lightweight process carried ::@:: The register state and signal mask of the thread on it, as a kernel object.
- which multithreading models are built on a lightweight process (LWP) ::@:: The many-to-one and many-to-many models, which need a virtual processor the thread library can schedule user threads onto.
- why the one-to-one model needs no lightweight process ::@:: Each user thread already owns a kernel thread, so an intermediate object would repeat an identity the thread already has.
- blocking of a lightweight process ::@:: If its kernel thread blocks, the lightweight process (LWP) blocks too, and so do its user threads.
- effect of preempting the kernel thread under a lightweight process ::@:: Every user thread on that lightweight process stops, since none has a kernel thread of its own.

## threading issues

Several threads in one process raise three questions: what fork() and exec() mean, where a signal goes, how a thread is ended early.

---

Flashcards for this section are as follows:

- three questions that multithreading raises ::@:: What fork() and exec() mean in a multithreaded process, where a signal goes, and how a thread is cancelled.

### fork() and exec() in a multithreaded process

Does a child of `fork()` hold every thread of the parent, or only the one that called? POSIX answers one thread, a copy of the caller.

The rest of the address space is copied. A mutex another thread held arrives locked, with nobody left in the child to release it, so a child that touches it hangs. A child that calls `exec()` at once never touches that state: `exec()` replaces the whole address space, locks included.

Some systems offered both behaviours: Solaris had `fork1()` for the single-thread child beside `forkall()` for a copy of every thread, and the standard keeps the single-thread child. Where library state must be repaired across the call, `pthread_atfork()` registers three handlers: one in the parent before the fork, one in the parent after it, one in the child.

Linux reaches the same result through `clone()`, whose flags say what the new task shares. A thread is `clone(CLONE_VM | CLONE_FS | CLONE_FILES | CLONE_SIGHAND, 0)`: the four flags share the address space, the file-system information, the open file table and the signal handlers with the parent, and the second argument stays `0`. A process is `clone(SIGCHLD, 0)`, with no sharing flags, and `SIGCHLD` names the signal the parent receives when the child ends. `fork()` is that call.

```c
#include <pthread.h>
#include <sys/types.h>
#include <unistd.h>

pid_t fork(void);                       /* -1 on error, 0 in the child, child's pid in the parent */
int pthread_atfork(void (*prepare)(void),   /* runs in the parent before the fork */
                   void (*parent)(void),    /* runs in the parent after the fork */
                   void (*child)(void));    /* runs in the child after the fork */
```

The three handlers keep a mutex consistent across the fork: the first locks it, the other two release it, one per process.

```c
#include <pthread.h>
#include <sys/types.h>
#include <unistd.h>

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

void prepare(void) { pthread_mutex_lock(&mutex); }     /* parent, before the fork */
void parent(void)  { pthread_mutex_unlock(&mutex); }   /* parent, after the fork */
void child(void)   { pthread_mutex_unlock(&mutex); }   /* child, after the fork */

int main(void)
{
    pid_t child_pid;

    pthread_atfork(prepare, parent, child);   /* one handler for each moment */
    child_pid = fork();                       /* 0 in the child, its pid in the parent */
    if (child_pid == 0)
        _exit(0);                             /* the child holds one thread only */
    return 0;
}
```

---

Flashcards for this section are as follows:

- threads in the child of `fork()` ::@:: One, a copy of the thread that called `fork()`. The parent's other threads do not exist in the child.
- why a lock copied across `fork()` is dangerous ::@:: A mutex another thread held arrives in the child already locked, with no thread left to release it, so a child that uses it hangs.
- why a child that calls `exec()` escapes that danger ::@:: `exec()` replaces the whole address space, which discards the inherited locks along with the rest of the parent's memory.
- prototype of `fork()` in a multithreaded process, and the call the handler program makes ::@:: `pid_t fork(void)`, called as `fork()`: copies the calling thread alone into the child, returning `0` there and the child's identifier in the parent.
- prototype of `pthread_atfork()`, and the three handlers the program registers ::@:: `int pthread_atfork(void (*prepare)(void), void (*parent)(void), void (*child)(void))`, called as `pthread_atfork(prepare, parent, child)`: `prepare` runs before the fork in the parent, `parent` after it in the parent, `child` after it in the child; each may be `NULL` where nothing is needed.
- prototype of `_exit()`, and the call the child makes instead of returning ::@:: `void _exit(int status)`, called as `_exit(0)`: ends the child at once, so it never runs the flushing path its parent would.
- prototype of `pthread_mutex_lock()`, and the call the prepare handler makes ::@:: `int pthread_mutex_lock(pthread_mutex_t *mutex)`, called as `pthread_mutex_lock(&mutex)`: takes the lock in the parent before the fork, so the child inherits a mutex somebody holds.
- prototype of `pthread_mutex_unlock()`, and the call both later handlers make ::@:: `int pthread_mutex_unlock(pthread_mutex_t *mutex)`, called as `pthread_mutex_unlock(&mutex)`: releases the inherited lock, once in the parent and once in the child.
- Solaris variants of `fork()` for a multithreaded parent ::@:: `fork1()`, which copies only the calling thread as POSIX requires, and `forkall()`, which duplicates every thread of the parent.
- how Linux makes a thread rather than a process ::@:: By calling `clone()` with `CLONE_VM | CLONE_FS | CLONE_FILES | CLONE_SIGHAND`, the flags that share the address space, the file-system information, the open file table and the signal handlers with the parent.
- the `clone()` call that makes a process on Linux ::@:: `clone(SIGCHLD, 0)`: no sharing flags, and `SIGCHLD` tells the parent when the child ends. `fork()` is this call.
- what `SIGCHLD` does in `clone(SIGCHLD, 0)` ::@:: It names the signal the parent receives when the child terminates.

### signals and their default actions

A signal tells a process that an event happened. A synchronous signal comes from the process's own execution, as with an illegal memory access or a division by zero, and goes to the thread that caused it. An asynchronous one comes from outside, as with an expiring timer or control-C.

A signal's default action is one of five: terminate the process, terminate it and dump core, ignore the signal, stop the process, continue a stopped one. A handler installed by the program replaces the default; that is what makes a signal useful.

`SIGUSR1` and `SIGUSR2` are the opposite case: the standard gives them a number and a default action of terminate, nothing more. The program assigns the meaning, and both ends agree on it in the source, usually as an out-of-band command to a running instance such as reopening its log file or reloading configuration. A program that handles one usually handles both, so it gains two channels without a new interface. The delivery example uses that: `SIGUSR1` goes to the process, `SIGUSR2` to one thread, and neither number means anything until the program says so.

`SIGKILL` and `SIGSTOP` are the exception. Neither can be caught, blocked or ignored, so no program can stop itself being killed outright or suspended: one ends a process that has stopped responding, the other freezes it. `SIGSEGV`, `SIGFPE`, `SIGILL` and `SIGBUS` can be caught, but a handler that returns leaves the faulting instruction to run again, so the usual response is to record the error and exit.

| signal | number | default action | usual reason to handle it |
| --- | --- | --- | --- |
| `SIGHUP` | 1 | terminate | the terminal closed; reload the configuration |
| `SIGINT` | 2 | terminate | control-C from the keyboard |
| `SIGQUIT` | 3 | terminate and dump core | control-backslash |
| `SIGILL` | 4 | terminate and dump core | an illegal instruction |
| `SIGTRAP` | 5 | terminate and dump core | a breakpoint or trap |
| `SIGABRT` | 6 | terminate and dump core | `abort()` was called |
| `SIGBUS` | 7 | terminate and dump core | a bad memory access, such as a misaligned one |
| `SIGFPE` | 8 | terminate and dump core | an arithmetic error such as division by zero |
| `SIGKILL` | 9 | terminate, cannot be caught | forcing a process to end |
| `SIGUSR1` | 10 | terminate | application-defined meaning |
| `SIGSEGV` | 11 | terminate and dump core | an invalid memory reference |
| `SIGUSR2` | 12 | terminate | application-defined meaning |
| `SIGPIPE` | 13 | terminate | writing to a pipe or socket with no reader |
| `SIGALRM` | 14 | terminate | an `alarm()` timer expired |
| `SIGTERM` | 15 | terminate | a request to end cleanly |
| `SIGCHLD` | 17 | ignore | a child stopped or exited |
| `SIGCONT` | 18 | continue | resume a process stopped by `SIGSTOP` |
| `SIGSTOP` | 19 | stop, cannot be caught | forcing a process to suspend |
| `SIGTSTP` | 20 | stop | control-Z from the keyboard |
| `SIGTTIN` | 21 | stop | a background process reading the terminal |
| `SIGTTOU` | 22 | stop | a background process writing the terminal |
| `SIGWINCH` | 28 | ignore | the terminal window was resized |

The numbers are those of Linux on x86-64.

```c
#include <pthread.h>
#include <signal.h>
#include <sys/types.h>
#include <unistd.h>

/* older interface: installs handler and returns the previous one, or SIG_ERR */
void (*signal(int signum, void (*handler)(int)))(int);

/* the portable one: 0 on success, -1 with errno on failure */
int sigaction(int signum, const struct sigaction *act, struct sigaction *oldact);
int kill(pid_t pid, int sig);
int raise(int sig);
int pthread_kill(pthread_t thread, int sig);     /* 0 or an error number */
int pthread_sigmask(int how, const sigset_t *set, sigset_t *oldset);  /* 0 or -1 */
```

A handler is installed, then a signal is sent three ways, then one is blocked for the calling thread.

```c
#include <pthread.h>
#include <signal.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>

void on_signal(int signum) { (void) signum; }

int main(void)
{
    struct sigaction act;
    memset(&act, 0, sizeof act);
    act.sa_handler = on_signal;            /* the function to run */
    sigemptyset(&act.sa_mask);             /* nothing extra blocked while it runs */
    act.sa_flags = 0;
    if (sigaction(SIGINT, &act, NULL) == -1)   /* NULL: the old action is not wanted */
        return 1;

    raise(SIGINT);                         /* the calling thread signals itself */
    kill(getpid(), SIGUSR1);               /* some thread of the process takes it */
    pthread_kill(pthread_self(), SIGUSR2); /* that one thread alone takes it */

    sigset_t set, old;
    sigemptyset(&set);
    sigaddset(&set, SIGINT);
    pthread_sigmask(SIG_BLOCK, &set, &old); /* the calling thread's mask, not the process's */
    return 0;
}

/* the older call, which installs a handler and nothing else */
void (*signal(int signum, void (*handler)(int)))(int);

int install_with_signal(void)
{
    signal(SIGINT, on_signal);   /* installs the handler for SIGINT */
    signal(SIGINT, SIG_IGN);     /* ignores it instead */
    signal(SIGINT, SIG_DFL);     /* restores the default action */
    return 0;
}
```

A `struct sigaction` carries the handler in `sa_handler`, the signals to block while it runs in `sa_mask`, and flags in `sa_flags`. Its third argument receives the previous action, or `NULL`.

Before `sigaction` there was `signal`, which installs a handler in one call and returns the previous one. It takes no mask and no flags, and the two historic implementations disagreed about the rest: System V cleared the handler when it fired, BSD kept it and restarted interrupted calls, so portable code could rely on neither. `sigaction` states the behaviour rather than inheriting it. Either call accepts `SIG_DFL` for the default action and `SIG_IGN` for ignoring the signal.

`SA_RESTART` restarts an interrupted call once the handler returns. `SA_SIGINFO` asks for the three-argument handler in `sa_sigaction`. `SA_RESETHAND`, `SA_NODEFER`, `SA_ONSTACK`, `SA_NOCLDSTOP` and `SA_NOCLDWAIT` change the rest.

---

Flashcards for this section are as follows:

- signal ::@:: A notification to a process that an event happened, such as an expiring timer or an illegal memory access by the program itself.
- synchronous signal ::@:: A signal raised by the running program's own execution, such as a division by zero or an illegal memory access. It goes to the thread that caused it.
- asynchronous signal ::@:: A signal raised by an event outside the running process, such as an expiring timer or a keystroke like control-C.
- the five default actions for a signal ::@:: Terminate the process, terminate it and dump core, ignore the signal, stop the process, continue a stopped process.
- signals that cannot be caught, blocked or ignored ::@:: `SIGKILL`, number 9, and `SIGSTOP`, number 19. They exist so a process can always be killed or suspended.
- why catching `SIGKILL` is impossible ::@:: The kernel acts on it without consulting a handler, so a program cannot refuse to end.
- what happens when a handler for `SIGSEGV` returns ::@:: The faulting instruction runs again and faults again, so the usual response is to record the error and exit.
- default action of `SIGCHLD` ::@:: Ignore it. It reports that a child stopped or exited.
- default action of `SIGHUP` and `SIGALRM` ::@:: Both terminate the process. `SIGHUP` reports that the terminal closed, `SIGALRM` that an `alarm()` timer expired.
- default action of `SIGQUIT`, `SIGILL`, `SIGTRAP`, `SIGABRT`, `SIGBUS` and `SIGFPE` ::@:: Terminate the process and dump core. Each reports a fatal program fault or an explicit `abort()`.
- default action of `SIGUSR1` and `SIGUSR2` ::@:: Both terminate the process. The program gives them whatever meaning it wants.
- typical use of `SIGUSR1` and `SIGUSR2` ::@:: An out-of-band command to a running program, such as reopening its log file, dumping or resetting state, reloading configuration.
- why the delivery example sends `SIGUSR1` to the process and `SIGUSR2` to one thread ::@:: Neither number means anything on its own, so the two keep the two kinds of delivery apart in the output.
- default action of `SIGTTIN` and `SIGTTOU` ::@:: Both stop the process. They report a background process reading from or writing to the terminal.
- default action of `SIGINT` and `SIGTERM` ::@:: Both terminate the process. `SIGINT` comes from control-C, `SIGTERM` is a request to end cleanly.
- default action of `SIGPIPE` ::@:: Terminate the process, which happens when it writes to a pipe or socket with no reader.
- default action of `SIGTSTP` and `SIGCONT` ::@:: `SIGTSTP`, from control-Z, stops the process, and `SIGCONT` resumes a stopped process.
- default action of `SIGWINCH` ::@:: Ignore it. It reports that the terminal window was resized.
- signature of `sigaction()`, and the call that installs the handler ::@:: `int sigaction(int signum, const struct sigaction *act, struct sigaction *oldact)`, called as `sigaction(SIGINT, &act, NULL)`: `signum` picks the signal, `act` describes the new handler, and `oldact` receives the previous one or is `NULL` when the program does not want it.
- flags the `sa_flags` field accepts, and what the two common ones change ::@:: `SA_NOCLDSTOP`, `SA_NOCLDWAIT`, `SA_NODEFER`, `SA_ONSTACK`, `SA_RESETHAND`, `SA_RESTART` and `SA_SIGINFO`, OR'd; `SA_RESTART` restarts an interrupted call, `SA_SIGINFO` asks for the three-argument handler in `sa_sigaction`.
- what a `struct sigaction` holds ::@:: The handler in `sa_handler`, the signals to block while it runs in `sa_mask`, and flags in `sa_flags`.
- why `sigaction()` replaced `signal()` ::@:: `signal()` set no mask and no flags, and System V reset the handler when it fired while BSD kept it and restarted interrupted calls, so portable code could rely on neither; `sigaction()` states the behaviour instead.
- prototype of `signal()`, and the call that installs a handler ::@:: `void (*signal(int signum, void (*handler)(int)))(int)`, called as `signal(SIGINT, on_signal)`: installs `on_signal` for that signal and returns the previous handler or `SIG_ERR`; the handler type is `sig_t` on BSD and `sighandler_t` on glibc.
- special handler values `signal()` accepts ::@:: `SIG_DFL`, which restores the default action, and `SIG_IGN`, which ignores the signal.
- what `signal()` cannot set that `sigaction()` can ::@:: The mask of signals blocked while the handler runs, and the flags such as `SA_RESTART` and `SA_SIGINFO`.

### signal delivery in a multithreaded process

A signal is addressed to a thread, a process or a process group. Only the first names one thread.

`pthread_kill()` and `raise()` address one thread, so the signal reaches that thread alone and waits there if the thread blocks it. `kill()` addresses a process, so the kernel picks one thread that does not block it; if every thread blocks it, the signal stays pending until one unblocks. A process group is the set of processes a shell puts one job into, so `kill(0)` and `kill(-pgid)` reach every process in the group, each of which then picks one of its own threads.

A synchronous fault goes to the thread that caused it; an asynchronous request such as a termination signal goes to any thread that does not block it. Whatever thread takes it, the default action belongs to the process, so a terminating signal ends every thread. The `sigaction()` handler is process-wide; the mask is per-thread, so `pthread_sigmask()` changes the calling thread alone and a new thread inherits the creator's mask. A child inherits both, and `exec` keeps an ignored signal ignored while resetting a caught one to the default action.

---

Flashcards for this section are as follows:

- prototype of `kill()`, and the call that signals its own process ::@:: `int kill(pid_t pid, int sig)`, called as `kill(getpid(), SIGUSR1)`: sends `sig` to the process `pid` names, and a `sig` of `0` only tests that the target exists. Returns `0`, or `-1` with `errno`.
- how many processes one `kill()` call reaches ::@:: One for a positive `pid`, every process in the caller's group for `0`, every process it may signal for `-1`, and every process in the group `|pid|` for a `pid` below `-1`.
- prototype of `raise()`, and the call that signals its own thread ::@:: `int raise(int sig)`, called as `raise(SIGINT)`: sends the signal to the calling thread, the same as `pthread_kill(pthread_self(), sig)`, never to the whole process.
- prototype of `pthread_kill()`, and the call that names one thread ::@:: `int pthread_kill(pthread_t thread, int sig)`, called as `pthread_kill(pthread_self(), SIGUSR2)`: `thread` names the one thread that receives the signal and `sig` is its number, where `0` only tests whether the thread still exists.
- prototype of `pthread_cancel()`, and the call that asks a thread to end ::@:: `int pthread_cancel(pthread_t thread)`, called as `pthread_cancel(tid)`: `tid` names the target, and the request acts only when that thread reaches a cancellation point or enables asynchronous cancellation.
- prototype of `getpid()`, and the call that names its own process ::@:: `pid_t getpid(void)`, called as `getpid()`: returns the caller's identifier, the value the `kill` call sends to address this process.
- prototype of `pthread_sigmask()`, and the call that blocks a signal for one thread ::@:: `int pthread_sigmask(int how, const sigset_t *set, sigset_t *oldset)`, called as `pthread_sigmask(SIG_BLOCK, &set, &old)`: `how` is `SIG_BLOCK` to add the set to the mask, `SIG_UNBLOCK` to remove it, or `SIG_SETMASK` to replace the mask; `oldset` keeps the previous mask or may be `NULL`. It changes the calling thread alone.
- prototype of `pthread_create()`, and the call that starts the worker ::@:: `int pthread_create(pthread_t *tid, const pthread_attr_t *attr, void *(*start_routine)(void *), void *arg)`, called as `pthread_create(&tid, NULL, worker, NULL)`: starts `worker` on a new thread with the default attributes and no argument.
- prototype of `pthread_join()`, and the call that waits for it ::@:: `int pthread_join(pthread_t tid, void **ret)`, called as `pthread_join(tid, NULL)`: waits for the thread to end and discards its return value.
- how a thread blocks a signal for itself ::@:: It calls `pthread_sigmask()` with `SIG_BLOCK` and a set holding that signal, and the change touches the calling thread alone.
- how a program arranges for one thread to take all signals ::@:: Every other thread blocks them with `pthread_sigmask()`, and the chosen thread waits for them.
- choices for delivering a signal to a multithreaded process ::@:: A signal is addressed to a thread (`pthread_kill`, `raise`), to a process (`kill`) or to a process group (`kill(0)` or `kill(-pgid)`); a process-directed signal is taken by one thread that does not block it.
- where a process-directed signal goes, and what happens when every thread blocks it ::@:: To one thread the kernel picks that does not block it; if all block it, the signal stays pending until one unblocks.
- what a terminating default action does to a multithreaded process ::@:: Ends the whole process, whichever thread took the signal, so a termination request never ends one thread alone.
- what is process-wide and what is per-thread about handlers and masks ::@:: The `sigaction()` handler is process-wide, the mask per-thread, so `pthread_sigmask()` changes only the calling thread's.
- signal mask a new thread starts with ::@:: The mask of the thread that created it.
- what a child process inherits of the signal setup, and what `exec` keeps ::@:: The handlers and the mask; `exec` keeps an ignored signal ignored and resets a caught one to the default action, mask unchanged.
- why blocking a signal in one thread does not shield the others ::@:: The mask is per-thread, so a signal the caller blocks still reaches any thread that leaves it unblocked.

### thread cancellation

Cancellation ends a thread before it has finished; the thread being ended is the target. Asynchronous cancellation stops the target at once, possibly inside `malloc` or a critical section, so a structure can be left half changed with no thread left to repair it. That danger is why the type is rarely used. Deferred cancellation sets a request and lets the target end itself in order.

POSIX makes deferred the default type, and the target ends at a cancellation point: a blocking or long call such as `read`, `write`, `sleep`, `pthread_cond_wait` or `pthread_join`. Cancellation is on by default. `pthread_setcancelstate` turns it off so a critical section can finish; `pthread_setcanceltype` selects deferred or asynchronous. A thread that computes for a long time without such a call never notices the request, so `pthread_testcancel()` exists: it makes a cancellation point of its own.

Cleanup is what makes deferred cancellation safe. `pthread_cleanup_push` registers a handler that runs when the thread is cancelled or returns, so a lock it holds is released and the memory it allocated is freed; `pthread_cleanup_pop` removes it again. A join on a cancelled thread returns the sentinel `PTHREAD_CANCELED` in place of the value the routine returned, so the joiner learns the thread never finished.

```c
#include <pthread.h>

int pthread_cancel(pthread_t thread);                  /* 0 or an error number */
int pthread_setcancelstate(int state, int *oldstate);   /* PTHREAD_CANCEL_ENABLE, PTHREAD_CANCEL_DISABLE */
int pthread_setcanceltype(int type, int *oldtype);      /* PTHREAD_CANCEL_DEFERRED, PTHREAD_CANCEL_ASYNCHRONOUS */
void pthread_testcancel(void);

/* the next two are macros that bracket the protected region */
void protected_region(void (*cleanup)(void *), void *arg)
{
    pthread_cleanup_push(cleanup, arg);   /* cleanup runs if the thread is cancelled */
    pthread_testcancel();                 /* a pending request acts here */
    pthread_cleanup_pop(1);               /* 1 runs the handler, 0 discards it */
}
```

The worker turns cancellation off for its critical section, on again, and honours a request at the test point.

```c
#include <pthread.h>

void release(void *arg) { (void) arg; }   /* unlocks or frees what the thread holds */

void *worker(void *arg)
{
    int old_state, old_type;
    pthread_setcancelstate(PTHREAD_CANCEL_DISABLE, &old_state);  /* taken at a point */
    /* the critical section runs to its end here */
    pthread_setcancelstate(PTHREAD_CANCEL_ENABLE, &old_state);

    pthread_setcanceltype(PTHREAD_CANCEL_DEFERRED, &old_type);   /* act at a point, not at once */
    pthread_cleanup_push(release, arg);   /* runs if the thread is cancelled or returns */
    pthread_testcancel();                 /* a computing loop can honour a request here */
    pthread_cleanup_pop(0);               /* 0: discard the handler, do not run it */
    return arg;
}

int main(void)
{
    pthread_t tid;
    pthread_create(&tid, NULL, worker, NULL);
    pthread_cancel(tid);                  /* asks that thread to end */
    pthread_join(tid, NULL);
    return 0;
}
```

---

Flashcards for this section are as follows:

- thread cancellation ::@:: Ending a thread before it has finished. The thread being ended is the target thread.
- asynchronous cancellation ::@:: The target thread stops at once, possibly in the middle of an update it has not completed.
- deferred cancellation ::@:: The target thread is sent a request and ends itself when it reaches a cancellation point.
- cost of asynchronous cancellation ::@:: The target can stop while it holds a lock or a block from the allocator, with no thread left to repair the structure.
- cancellation point ::@:: A call at which a thread checks for a pending cancellation request, such as `read`, `write`, `sleep`, `pthread_cond_wait` or `pthread_join`.
- which cancellation type POSIX uses by default ::@:: Deferred, with cancellation enabled unless the thread disables it.
- prototype of `pthread_setcancelstate()`, and the call that closes the window ::@:: `int pthread_setcancelstate(int state, int *oldstate)`, called as `pthread_setcancelstate(PTHREAD_CANCEL_DISABLE, &old_state)`: `state` is `PTHREAD_CANCEL_ENABLE` or `PTHREAD_CANCEL_DISABLE`, and `oldstate` keeps the previous state or may be `NULL`.
- prototype of `pthread_setcanceltype()`, and the call that defers the end ::@:: `int pthread_setcanceltype(int type, int *oldtype)`, called as `pthread_setcanceltype(PTHREAD_CANCEL_DEFERRED, &old_type)`: `type` is `PTHREAD_CANCEL_DEFERRED`, which waits for a cancellation point, or `PTHREAD_CANCEL_ASYNCHRONOUS`, which acts at once; `oldtype` keeps the previous type or may be `NULL`.
- prototype of `pthread_testcancel()`, and the call that offers a cancellation point ::@:: `void pthread_testcancel(void)`, called as `pthread_testcancel()`: makes a cancellation point, so a pending request ends the thread here; otherwise the call returns at once.
- prototype of `pthread_cleanup_push()`, and the call that registers the handler ::@:: `void pthread_cleanup_push(void (*routine)(void *), void *arg)`, called as `pthread_cleanup_push(release, arg)`: registers `release` to run with `arg` if the thread is cancelled or returns.
- prototype of `pthread_cleanup_pop()`, and what its argument decides ::@:: `void pthread_cleanup_pop(int execute)`, called as `pthread_cleanup_pop(0)`: removes the handler without running it, where `1` would run it on the way out.
- purpose of `pthread_setcancelstate()` ::@:: It turns cancellation on or off for the calling thread, so a critical section finishes before a request is taken.
- options of `pthread_setcanceltype()` ::@:: `PTHREAD_CANCEL_DEFERRED`, which ends the thread at the next cancellation point, and `PTHREAD_CANCEL_ASYNCHRONOUS`, which ends it at once.
- purpose of `pthread_testcancel()` ::@:: It acts as a cancellation point, so a thread that only computes can still honour a pending request.
- purpose of `pthread_cleanup_push()` and `pthread_cleanup_pop()` ::@:: They register and remove a handler that releases resources when the thread is cancelled or returns.
- what a join returns for a cancelled thread ::@:: `PTHREAD_CANCELED`, a sentinel the joiner tests to learn the thread did not finish normally.
- why a compute-bound loop resists deferred cancellation ::@:: It never calls a cancellation point, so the request stays pending until it makes one with `pthread_testcancel()`.
- which cancellation to prefer ::@:: Deferred cancellation, because the thread finishes what it was doing and runs its cleanup handlers.
