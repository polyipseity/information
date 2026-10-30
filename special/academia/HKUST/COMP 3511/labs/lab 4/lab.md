---
aliases:
  - COMP 3511 lab 4
  - HKUST COMP 3511 lab 4
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/labs/lab_4/lab
  - language/in/English
---

# lab

- HKUST COMP 3511 lab 4
- parent: [lab 4](index.md)

## pipes

### anonymous pipe

An [ordinary pipe](../../inter-process%20communication.md#ordinary%20pipe) carries data one way between a process and its child; no other process can reach it. `pipe(pfds)` fills `pfds[0]` to read and `pfds[1]` to write, returning `-1` with the reason in `errno`. Made before `fork()`, the pipe passes both ends to the child.

Each side closes the end it will not use: the writer drops `pfds[0]`, the reader `pfds[1]`. A write end open anywhere keeps the pipe from ever reporting the end of the data. `read()` blocks until data arrives or every write end closes.

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main()
{
    int pfds[2];      /* pipe descriptors: pfds[0] reads, pfds[1] writes */
    char message[30];

    if (pipe(pfds) == -1) {
        perror("pipe failed");
        return 1;
    }

    pid_t pid = fork();          /* 0 in the child, non-zero in the parent */

    if (pid != 0) {              /* parent process */
        printf("PARENT: writing to pipe\n");
        close(pfds[0]);          /* drop the read end */
        write(pfds[1], "test", 5);
        wait(NULL);
        printf("PARENT: exiting\n");
    } else {                     /* child process */
        printf("CHILD: reading from pipe\n");
        close(pfds[1]);          /* drop the write end */
        read(pfds[0], message, 5);
        printf("CHILD: read \"%s\"\n", message);
    }

    printf("world!\n");
    return 0;
}
```

Five bytes travel: the four letters of `test` and the null byte that ends it. The parent's and the child's lines can appear in either order, since the scheduler picks which process runs.

---

Flashcards for this section are as follows:

- which end of an ordinary pipe each side closes ::@:: The writer closes `pfds[0]` and the reader closes `pfds[1]`.
- prototype of `pipe()`, and the call that creates the channel ::@:: `int pipe(int pipefd[2])`, called as `pipe(pfds)`: creates the channel and fills the array, `pfds[0]` to read, `pfds[1]` to write.
- prototype of `fork()`, and the call that makes the writing child ::@:: `pid_t fork(void)`, called as `fork()`: starts the child that writes into the channel; returns `0` there and the child's identifier in the parent.
- prototype of `wait()`, and the call the parent reaps with ::@:: `pid_t wait(int *wstatus)`, called as `wait(NULL)`: blocks until a child ends and throws its status away.
- why a write end left open in the reading process keeps it waiting ::@:: `read()` on a pipe reports the end of the data only when no write end is open anywhere.
- what `read()` on an empty ordinary pipe does while a writer still holds it open ::@:: It blocks until data arrives.
- why the lines of the parent and the child may appear in either order after `fork()` ::@:: The scheduler picks which process runs next, so the two lines interleave; each process's own lines stay in order.
- how many bytes `write(pfds[1], "test", 5)` sends ::@:: Five: the four letters of `test` and the null character ending the string.

### exchange in both directions

A pipe carries data one way, so two-way exchange takes two pipes, one per direction. Each process keeps only the ends it uses: the parent writes `p2c[1]`, reads `c2p[0]`; the child writes `c2p[1]`, reads `p2c[0]`.

> The program below is meant to send one message each way. Which calls fill its six blanks?
>
> ```c
> int main() {
>     char buffer[10] = {};     /* initialized to zero */
>     int p2c[2], c2p[2];
>     BLANK1;
>     BLANK2;
>     pid_t pid = fork();
>     if (pid == 0) {           /* child process */
>         const char msg[] = "Child";
>         close(c2p[0]);
>         BLANK3;
>         close(p2c[1]);
>         BLANK4;
>         printf("Child received the message: %s\n", buffer);
>     } else {                  /* parent process */
>         const char msg[] = "Parent";
>         close(c2p[1]);
>         BLANK5;
>         close(p2c[0]);
>         BLANK6;
>         printf("Parent received the message: %s\n", buffer);
>     }
>     return 0;
> }
> ```
>
> ---
>
> - solution: {@{`pipe(p2c)` and `pipe(c2p)` in the first two blanks, then `write(c2p[1], msg, 6)`, `read(p2c[0], buffer, 7)`, `read(c2p[0], buffer, 6)` and `write(p2c[1], msg, 7)`}@}
> - explanation: Both pipes are created {@{before `fork()`, so the child inherits all four descriptors}@}. The child closes {@{`c2p[0]`, the read end of the pipe it writes to}@}, so its message {@{leaves through `c2p[1]`}@}. It then closes {@{`p2c[1]`, the write end of the pipe it reads}@} and reads {@{the parent's reply from `p2c[0]`}@}. The parent {@{does the same in reverse, reading `c2p[0]` and writing `p2c[1]`}@}. {@{The byte counts}@} follow the strings: {@{`"Child"` with its null is 6 bytes and `"Parent"` with its null is 7}@}.

---

Flashcards for this section are as follows:

- number of pipes needed for exchange in both directions ::@:: Two, one for each direction.
- which ends the parent keeps when `p2c` goes parent to child and `c2p` comes back ::@:: The write end `p2c[1]` and the read end `c2p[0]`.
- which ends the child keeps in a two-pipe exchange ::@:: The read end `p2c[0]` and the write end `c2p[1]`.
- where the `pipe()` calls belong relative to `fork()` ::@:: Before it, so the child inherits all four descriptors; one made after `fork()` belongs to a single process.
- why each process closes the pipe ends it does not use ::@:: An open write end stops the other side's `read()` from seeing the end of the data.

### popen and pclose

`popen(cmdstring, type)`, declared in `<stdio.h>`, runs `cmdstring` in a child process and returns a `FILE *` attached to it. With `"r"` the stream is the command's standard output, with `"w"` its standard input. On failure it returns `NULL`.

`pclose(fp)` closes the stream, waits for the command, and returns its termination status, or `-1` if the wait fails. Ordinary stdio calls, such as `fgets`, read the stream, so nothing is closed by hand and no `wait()` runs.

```c
#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *fp = popen("ls", "r");
    if (fp == NULL) {
        printf("Failed to run command\n");
        exit(1);
    }

    char path[1035];
    while (fgets(path, sizeof(path), fp) != NULL)
        printf("%s", path);

    int status = pclose(fp);
    if (status == -1) {
        printf("pclose() failed!\n");
        return 1;
    }
    return 0;
}
```

The type string sets the direction; no other value is valid.

---

Flashcards for this section are as follows:

- two standard-library calls that run a command behind a pipe, and the header that declares them ::@:: `popen()` and `pclose()`, both declared in `<stdio.h>`.
- what `popen(cmdstring, "r")` connects its stream to ::@:: The standard output of the command it starts, so the caller reads that output.
- what `popen(cmdstring, "w")` connects its stream to ::@:: The standard input of the command it starts, so whatever the caller writes, the command reads.
- which calls read the stream that `popen()` returns ::@:: Ordinary stdio calls, such as `fgets`, on the `FILE *` it returns.
- what `pclose()` returns when the wait for the command fails ::@:: `-1`.
- prototype of `popen()`, and the call that starts the command ::@:: `FILE *popen(const char *command, const char *type)`, called as `popen("ls", "r")`: declared in `<stdio.h>`, runs `ls`, and returns a stream to read its output or `NULL` when the command cannot start.
- prototype of `pclose()`, and the call that finishes it ::@:: `int pclose(FILE *stream)`, called as `pclose(fp)`: declared in `<stdio.h>`, closes the stream, waits for the command and returns its termination status, or `-1` when the wait fails.
- values the type argument of `popen()` accepts, and what each connects ::@:: `"r"` reads the command's standard output, `"w"` writes to its standard input, and no other string is valid.

### named pipe as a file

A named pipe, also called a first-in first-out (FIFO), has a name in the file system. `mkfifo` creates that name, `mode` sets its permissions, and the call returns `0` on success and `-1` on failure. The name lists like a file, yet nothing is stored: what one process writes, another reads once, and the data is gone.

A FIFO works through the ordinary calls `open`, `read`, `write` and `close`. `access(path, amode)` asks the question `amode` names: `F_OK` about the name, `R_OK`, `W_OK` and `X_OK` about access. `F_OK` returns `0` when the name exists, so a program tests it before `mkfifo()`.

`open` on a FIFO blocks until a process holds the other end, so either program can start first: `O_WRONLY` waits for a reader, `O_RDONLY` for a writer. `O_NONBLOCK` skips the wait, and the program learns later whether the other end exists.

A FIFO consumes data instead of storing it, which sets two limits. It cannot send one message to two readers. A process that writes then reads may read back its own message.

A write of at most `PIPE_BUF` bytes arrives whole; a larger one may mix with another writer's data. Once `PIPE_BUF` bytes wait, further writes block until a reader takes some.

---

Flashcards for this section are as follows:

- named pipe, and its other name ::@:: A pipe that appears as a file in the file system, also called a first-in first-out (FIFO).
- prototype of `mkfifo()` in the lab program, and the call that creates the pipe ::@:: `int mkfifo(const char *path, mode_t mode)`, called as `mkfifo(FIFO_NAME, 0777)`: creates the named pipe with read, write and execute for owner, group and others; returns `-1` when the name is taken.
- prototype of `access()` in the lab's create-if-missing step ::@:: `int access(const char *path, int amode)`, called as `access(FIFO_NAME, F_OK)`: `amode` names the question, `F_OK` about the name, `R_OK`, `W_OK` and `X_OK` about read, write and execute access, which may be OR'd; returns `0` for yes, `-1` with `errno` for no.
- values `access()` takes for `amode`, and what each asks ::@:: `F_OK` whether the name exists, `R_OK` whether it may be read, `W_OK` whether it may be written, `X_OK` whether it may be executed; the last three OR together, `F_OK` stands alone.
- prototype of `open()`, and the call that attaches to the pipe ::@:: `int open(const char *path, int flags, ...)`, called as `open(FIFO_NAME, O_WRONLY)`: the flag is one access mode, `O_RDONLY`, `O_WRONLY` or `O_RDWR`, no `O_CREAT` since the FIFO exists, so no mode argument is passed; the writer waits until the reader opens, and the reader calls the same way with `O_RDONLY`.
- prototype of `read()`, and the count the lab's FIFO reader passes ::@:: `ssize_t read(int fd, void *buf, size_t count)`, called as `read(pipe_fd, buffer, BUFFER_SIZE)`: `pipe_fd` is the open FIFO, `buffer` the memory to fill, `count` the most bytes, `BUFFER_SIZE` here, defined as `4096`; returns the count, `0` at the end, or `-1`.
- prototype of `write()`, and the count the lab's FIFO writer passes ::@:: `ssize_t write(int fd, const void *buf, size_t count)`, called as `write(pipe_fd, buffer, BUFFER_SIZE)`: `pipe_fd` the open FIFO, `buffer` the bytes, `count` how many, `BUFFER_SIZE` here, defined as `4096`; returns the count accepted, or `-1`.
- prototype of `close()`, and the call that lets the other end see the end of the data ::@:: `int close(int fd)`, called as `close(pipe_fd)`: releases the descriptor once the messages are through.
- prototype of `getpid()`, and the call that says which process opened the pipe ::@:: `pid_t getpid(void)`, called as `getpid()`: returns the caller's identifier, which tells the two FIFO programs apart.
- prototype of `exit()`, and the call that ends a failing program ::@:: `void exit(int status)`, called as `exit(EXIT_FAILURE)`: flushes the streams and ends the program with a failure status for whoever waits.
- call that tests whether a named pipe already exists ::@:: `access(path, F_OK)`, which returns `0` when the name exists.
- what `open` on a named pipe does when no process holds the other end ::@:: It blocks: a write-open waits for a reader and a read-open waits for a writer.
- open flag that removes the wait at `open` on a named pipe ::@:: `O_NONBLOCK`.
- why a named pipe makes a poor two-way channel ::@:: It carries data one way at a time, so a process that writes then reads may read back its own message.
- size below which a write to a named pipe is atomic ::@:: Up to `PIPE_BUF` bytes, which arrives whole.
- what happens to writes once `PIPE_BUF` bytes are waiting in a named pipe ::@:: Further writes block until a reader takes some.
- why a first-in first-out (FIFO) named pipe cannot send one message to two readers ::@:: A FIFO consumes what it carries instead of storing it: the first `read` takes the message, and the second reader finds nothing.
- which calls a program uses a named pipe through once `mkfifo()` has created it ::@:: The ordinary descriptor calls `open`, `read`, `write` and `close`.

### producer and consumer on a named pipe

A producer and a consumer need no common ancestor: each opens the same path, either can start first, and both wait at `open` for the other.

A shared header names the FIFO and the buffer size.

```c
#include <limits.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>

#define FIFO_NAME "/tmp/testp"
#define BUFFER_SIZE 4096
```

The producer creates the FIFO if absent, writes ten megabytes into it, and closes.

```c
#define TEN_MEG (1024 * 1024 * 10)

int main(void)
{
    int pipe_fd;
    int res;
    /* the writer asks for writing only */
    int bytes_sent = 0;
    char buffer[BUFFER_SIZE + 1] = {0};

    if (access(FIFO_NAME, F_OK) == -1) {
        res = mkfifo(FIFO_NAME, 0777);
        if (res != 0) {
            fprintf(stderr, "Could not create fifo %s\n", FIFO_NAME);
            exit(EXIT_FAILURE);
        }
    }

    printf("Process %d opening FIFO O_WRONLY\n", getpid());
    pipe_fd = open(FIFO_NAME, O_WRONLY);
    printf("Process %d opened fd %d\n", getpid(), pipe_fd);

    if (pipe_fd != -1) {
        while (bytes_sent < TEN_MEG) {
            res = write(pipe_fd, buffer, BUFFER_SIZE);
            if (res == -1) {
                fprintf(stderr, "Write error on pipe\n");
                exit(EXIT_FAILURE);
            }
            bytes_sent += res;
        }
        close(pipe_fd);
    } else {
        exit(EXIT_FAILURE);
    }

    printf("Process %d finished\n", getpid());
    exit(EXIT_SUCCESS);
}
```

The consumer loops on `read` until it returns `0`, the end of the data once the producer closes its descriptor.

```c
int main(void)
{
    int pipe_fd;
    int res;
    /* the reader asks for reading only */
    int bytes_read = 0;
    char buffer[BUFFER_SIZE + 1];

    memset(buffer, '\0', sizeof(buffer));

    printf("Process %d opening FIFO O_RDONLY\n", getpid());
    pipe_fd = open(FIFO_NAME, O_RDONLY);
    printf("Process %d opened fd %d\n", getpid(), pipe_fd);

    if (pipe_fd != -1) {
        do {
            res = read(pipe_fd, buffer, BUFFER_SIZE);
            bytes_read += res;
        } while (res > 0);
        close(pipe_fd);
    } else {
        exit(EXIT_FAILURE);
    }

    printf("Process %d finished, %d bytes read\n", getpid(), bytes_read);
    exit(EXIT_SUCCESS);
}
```

```text
./fifo_prod
Process 4211 opening FIFO O_WRONLY
Process 4211 opened fd 3
Process 4211 finished
```

```text
./fifo_con
Process 4212 opening FIFO O_RDONLY
Process 4212 opened fd 3
Process 4212 finished, 10485760 bytes read
```

The consumer reads $10 \times 1024 \times 1024 = 10485760$ bytes, exactly `TEN_MEG`.

---

Flashcards for this section are as follows:

- whether a producer and a consumer on a named pipe must share a parent ::@:: No. Each opens the same path, so any two processes can use it and either may start first.
- what a process sees when it opens a named pipe before the other end exists ::@:: Its `open` blocks until another process opens the pipe.
- how the consumer in the producer-consumer pair knows the data has ended ::@:: Its `read` returns `0` when the producer closes its write end.
- how many bytes the producer writes when `TEN_MEG` is `1024 * 1024 * 10` and the buffer holds `4096` bytes ::@:: 10485760 bytes, in writes of `BUFFER_SIZE` bytes each.
- what the consumer's `do` loop adds to `bytes_read` ::@:: The count each `read` returns, until one returns `0`.
- what the producer checks before it creates the named pipe ::@:: Whether the name exists, with `access(FIFO_NAME, F_OK)`, so a second run reuses the pipe instead of failing at `mkfifo`.

## threads

### thread handles and creation

POSIX Threads, known as pthreads, is the standard thread interface in C, declared in `<pthread.h>`. It specifies behaviour, so each system supplies its own library behind the same calls.

A `pthread_t` value names a thread. A `pthread_attr_t` structure carries its attributes, such as stack size and scheduling, and `pthread_attr_init(&attr)` fills it with the defaults.

`pthread_create(&tid, &attr, start_routine, arg)` starts a thread in `start_routine`, with `arg` as its only argument. A start routine has the fixed type `void *(*)(void *)`.

```c
#include <pthread.h>

int pthread_create(pthread_t *thread,
                   const pthread_attr_t *attr,
                   void *(*start_routine)(void *),
                   void *arg);
```

`arg` is a `void *`, so a value of another type converts on the way in and back on the way out. A `char *` such as `argv[1]` needs no cast: any object pointer converts to `void *`.

---

Flashcards for this section are as follows:

- prototype of `pthread_create()`, and the call the summation program makes ::@:: `int pthread_create(pthread_t *tid, const pthread_attr_t *attr, void *(*start_routine)(void *), void *arg)`, called as `pthread_create(&tid, &attr, runner, argv[1])`: starts `runner` on a new thread, stores the identifier in `&tid`, reads attributes from `&attr`, and hands `runner` `argv[1]`.
- prototype of `pthread_join()`, and the call that waits for the thread ::@:: `int pthread_join(pthread_t tid, void **ret)`, called as `pthread_join(tid, NULL)`: `tid` names the thread and `NULL` discards the pointer returned.
- prototype of `pthread_exit()`, and the call the summing thread makes ::@:: `void pthread_exit(void *ret)`, called as `pthread_exit(0)`: ends the calling thread and reports `0` to a joiner.
- prototype of `pthread_attr_init()`, and the call that fills the attributes ::@:: `int pthread_attr_init(pthread_attr_t *attr)`, called as `pthread_attr_init(&attr)`: fills the structure with the defaults `pthread_create` then reads.
- type that names one thread, and the type that carries a thread's attributes ::@:: `pthread_t` names the thread; `pthread_attr_t` holds its attributes such as stack size and scheduling information.
- the type of a POSIX Threads (pthreads) start routine, and why that type is fixed ::@:: `void *(*)(void *)`, one `void *` in and one `void *` out, so the interface carries any argument and any result.
- why an argument of type `char *` needs no conversion when it is passed to `pthread_create()` ::@:: A `char *` converts to `void *` and back without a cast, as any object pointer does.
- which thread starts a program that uses POSIX Threads (pthreads) ::@:: The initial thread, which begins in `main()` and creates the rest.
- whether POSIX Threads (pthreads) is one implementation or a specification, and what follows from it ::@:: The standard specifies behaviour, and each system supplies its own library behind the same calls.

### joining and ending a thread

`pthread_join(tid, NULL)` waits for the thread named by `tid` to end, and its second argument can receive the value returned. A thread ends by returning from its start routine or by calling `pthread_exit(0)`; either way the join returns.

The join orders the results: a program that prints a shared value without joining may print it before the thread writes it. Several threads are joined in a loop, one identifier per pass.

---

Flashcards for this section are as follows:

- how the summing thread ends, and the other way a thread can end ::@:: It calls `pthread_exit(0)`; a thread also ends by returning from its start routine, and either way the join returns.
- why a program joins a thread before it reads what the thread wrote ::@:: The join marks where the thread has finished, so without it the reader may run before the write.
- how ten threads are joined ::@:: By calling `pthread_join()` once per thread identifier in a loop.
- what the second argument of `pthread_join()` can receive ::@:: The value the joined thread returned.

### building with the pthread library

The thread calls sit in a separate library, so the link step names it.

```bash
gcc pthread_demo.c -pthread -o pthread_demo
```

`-pthread` turns on the compiler and linker settings a threaded program needs; `-lpthread` names the library alone and links it without them.

---

Flashcards for this section are as follows:

- link flag that builds the threaded demo, and where it goes ::@:: `-pthread`, on the `gcc` command line, as in `gcc pthread_demo.c -pthread -o pthread_demo`.
- what naming `-lpthread` alone leaves out ::@:: The compiler settings `-pthread` also turns on, so the library is linked without them.
- why a threaded program links a library ::@:: The thread calls live in a separate library, so the executable links against it.

### summation in a thread

The program below adds $1$ to $n$ in a second thread. `sum` is global, so both threads reach it: the child writes it, and the main thread reads it after the join.

```c
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

int sum;                     /* shared by both threads */
void *runner(void *param);   /* the function the child thread runs */

int main(int argc, char *argv[])
{
    pthread_t tid;           /* the thread identifier */
    pthread_attr_t attr;     /* the thread's attributes */

    if (argc != 2) {
        fprintf(stderr, "usage: a.out <integer value>\n");
        return -1;
    }
    if (atoi(argv[1]) < 0) {
        fprintf(stderr, "%d must be >= 0\n", atoi(argv[1]));
        return -1;
    }

    pthread_attr_init(&attr);            /* default attributes */
    pthread_create(&tid, &attr, runner, argv[1]);
    pthread_join(tid, NULL);             /* wait for the thread */

    printf("sum = %d\n", sum);
    return 0;
}

void *runner(void *param)
{
    int i, upper = atoi(param);

    sum = 0;
    for (i = 1; i <= upper; i++)
        sum += i;

    pthread_exit(0);
}
```

---

Flashcards for this section are as follows:

- why `sum` needs no passing between the threads of the summation program ::@:: It is a global, so the main thread and the summing thread reach the same object.
- which thread computes the sum in the summation program, and which one prints it ::@:: The thread made by `pthread_create()` computes it in `runner`; the main thread prints it once `pthread_join()` returns.
- what the argument of the summing thread holds, and how the thread reads it ::@:: The string `argv[1]` handed over as a `void *`, which the thread converts with `atoi`.
- what the main thread does between creating the summing thread and printing the result ::@:: It calls `pthread_join(tid, NULL)` and waits for the thread to end.
- why the program checks `argc` and the sign of `argv[1]` before creating a thread ::@:: The sum needs a supplied, non-negative upper bound, and both checks reject a run the loop cannot handle.

### thread scheduling order

Threads run independently, so the scheduler decides at run time which lines come first. The program below creates two threads printing one letter each, joins both, and prints a line before and after.

```c
#include <pthread.h>
#include <stdio.h>

void *mychild(void *arg)
{
    printf("%s\n", (char *) arg);
    return NULL;
}

int main()
{
    pthread_t t1, t2;

    printf("main: begin\n");
    pthread_create(&t1, NULL, mychild, "A");
    pthread_create(&t2, NULL, mychild, "B");
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    printf("main: end\n");
    return 0;
}
```

Two lines are fixed. `main: begin` comes before any line from either thread; `main: end` comes after both joins return.

| trace | first line | second line | third line | fourth line |
| --- | --- | --- | --- | --- |
| first thread runs when created | `main: begin` | `A` | `B` | `main: end` |
| second thread finishes first | `main: begin` | `B` | `A` | `main: end` |

The count of orders grows with the lines each thread prints. Give each thread a `begin of <name>` line and an `end of <name>` line in a loop long enough to interleave, and the threads contribute four lines. Each thread's own two lines stay in order, leaving the four free in $\binom{4}{2} = 6$ ways, so the program has six outputs.

---

Flashcards for this section are as follows:

- what fixes the first and last output lines of a program whose main thread joins its children ::@:: Program order: the main thread prints before creating the threads, and again only after both joins return.
- how many output orders the two-thread program with one letter each has, and what they are ::@:: Two. `A` then `B`, or `B` then `A`, with `main: begin` first and `main: end` last.
- how many possible outputs two threads have when each prints a begin line and an end line ::@:: Six: the four thread lines interleave in any order that keeps each begin line ahead of its own end line.
- who decides which thread runs next ::@:: The scheduler, so the same program can print the lines in a different order on a later run.
- why joining both threads still leaves the order of their lines undecided ::@:: The joins place `main: end` after both threads and order nothing between the threads.

### threads against processes

The threads of one process share its memory; a child made by `fork()` gets its own copy.

```c
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

void *child(void *arg)
{
    int *counter = (int *) arg;
    (*counter)++;
    return NULL;
}

int main()
{
    int counter = 0;
    pthread_t thread;

    pthread_create(&thread, NULL, child, (void *) &counter);
    pthread_join(thread, NULL);
    printf("%d\n", counter);
    fflush(stdout);

    counter = 0;
    pid_t pid = fork();
    if (pid)
        wait(NULL);
    else {
        child((void *) &counter);
        exit(0);
    }
    printf("%d\n", counter);
    fflush(stdout);

    return 0;
}
```

The thread takes `counter`'s address, so its increment reaches the variable and the first line prints `1`. The `fork()` child runs the same function on its own copy and prints `1`; the parent prints `1` from the untouched copy.

---

Flashcards for this section are as follows:

- what the two lines of the thread-and-fork counter program are ::@:: `1` and `1`: the thread's increment reaches the main thread's variable, while the child's lands in a copy.
- why a variable changed by a thread is visible to the thread that created it ::@:: The threads of one process share its memory, so a write through a shared address reaches both.
- why a variable changed by a child of `fork()` is not visible to the parent ::@:: The child gets its own copy of the address space, so its write lands there.
- what `fflush(stdout)` guarantees in a program that also calls `fork()` ::@:: The pending output is written before the process splits, so no buffered line prints twice, once per copy.
- what the parent does instead of incrementing its own counter after `fork()` ::@:: It calls `wait(NULL)`, lets the child increment, then prints its own unchanged value.
