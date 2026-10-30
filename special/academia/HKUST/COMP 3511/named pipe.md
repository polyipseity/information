---
aliases:
  - FIFO
  - first-in first-out pipe
  - named pipe
  - named pipes
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/named_pipe
  - language/in/English
---

# named pipe

A named pipe, also called a first-in first-out (FIFO), is a pipe with a name in the file system. The name outlives its creator, so two processes with no common ancestor can share one: each opens the same path and exchanges data through it.

A named pipe differs from an ordinary pipe in reach and in direction. An ordinary pipe is created by one process and inherited by its child, so it dies with them and carries data one way. A named pipe sits at a path instead, any process with permission opens it, and it stays until someone deletes it. Its communication runs both ways.

---

Flashcards for this section are as follows:

- what a named pipe is ::@:: A pipe with a name in the file system, so two processes with no common ancestor can open the same channel.
- other name of a named pipe ::@:: First-in first-out (FIFO).
- what a named pipe lifts that an ordinary pipe requires ::@:: The parent-child relationship: any process that can reach the path may open the pipe.
- what an ordinary pipe and a named pipe do the same way ::@:: Both carry bytes in written order and discard what a reader has taken.
- direction of a named pipe against an ordinary pipe ::@:: A named pipe carries data both ways, while an ordinary pipe carries it one way.

## creating a named pipe

`mkfifo` creates the FIFO and is declared in `<sys/stat.h>`. The name appears in a directory listing with the file type of a FIFO, not a regular file.

A program that may run more than once checks the name first: `access(path, F_OK)` asks only whether it exists and returns `0` or `-1`, so a second run skips the creation. The other flags test permissions, `R_OK` for reading, `W_OK` for writing, `X_OK` for executing.

Nothing removes the name on its own: it stays until a process deletes it, even after every user has exited.

The calls used below:

```c
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int mkfifo(const char *path, mode_t mode);          /* 0, or -1 with errno */
int access(const char *path, int amode);            /* 0 if reachable, -1 with errno */
int open(const char *path, int flags, ... /* mode_t mode */);   /* fd, or -1 */
ssize_t read(int fd, void *buf, size_t count);      /* bytes read, 0 at end, -1 */
ssize_t write(int fd, const void *buf, size_t count); /* bytes written, or -1 */
int close(int fd);                                  /* 0, or -1 */
```

A program that creates the pipe only when it is missing, then sends one message:

```c
#include <fcntl.h>
#include <sys/stat.h>
#include <unistd.h>

#define FIFO_PATH "/tmp/demo.fifo"
#define MESSAGE "hello"

int main(void)
{
    if (access(FIFO_PATH, F_OK) == -1)         /* F_OK asks only whether the name exists */
        if (mkfifo(FIFO_PATH, 0600) == -1)     /* 0600: the owner reads and writes */
            return 1;                          /* the name exists and is not ours */

    int fd = open(FIFO_PATH, O_WRONLY);         /* blocks until a reader opens as well */
    if (fd == -1)
        return 1;
    if (write(fd, MESSAGE, sizeof MESSAGE - 1) == -1)   /* the count excludes the terminator */
        return 1;
    return close(fd);                           /* 0 when the descriptor is released */
}
```

---

Flashcards for this section are as follows:

- header that declares `mkfifo()` ::@:: `<sys/stat.h>`.
- prototype of `mkfifo()`, and the call that creates the pipe ::@:: `int mkfifo(const char *path, mode_t mode)`, called as `mkfifo(FIFO_PATH, 0600)`: creates the named pipe at `path` with owner read and write only, and returns `0` or `-1` with `errno` set.
- prototype of `access()`, and the call that tests for the name ::@:: `int access(const char *path, int amode)`, called as `access(FIFO_PATH, F_OK)`: `amode` picks the question (`F_OK` for the name), and the call answers `0` or `-1` with `errno`.
- flag of `access()` that asks only whether the name exists ::@:: `F_OK`, which answers `0` for an existing path, so a second run skips creating the pipe.
- flags of `access()` that test reading, writing and executing ::@:: `R_OK`, `W_OK` and `X_OK`. They combine with `|` to ask about several kinds of access at once; `F_OK` stands alone because it asks about the name.
- how a named pipe looks in a directory listing ::@:: Like a file, but with the file type of a first-in first-out (FIFO), which stores no data.
- when a named pipe's name disappears ::@:: Only when a process deletes it; the name outlives every process that used it.
- prototype of `open()`, and the call that attaches the writer to the pipe ::@:: `int open(const char *path, int flags, ...)`, called as `open(FIFO_PATH, O_WRONLY)`: `path` names the existing FIFO, `flags` holds one access mode (`O_RDONLY`, `O_WRONLY` or `O_RDWR`), and no `mode_t` is passed because the file exists; it waits for a reader and returns a descriptor, or `-1`.
- prototype of `write()`, and the call the creating program sends with ::@:: `ssize_t write(int fd, const void *buf, size_t count)`, called as `write(fd, MESSAGE, sizeof MESSAGE - 1)`: `fd` is the open FIFO, `MESSAGE` the string, and `count` its bytes, terminator left out; it returns the count accepted, or `-1`.
- prototype of `close()`, and the call that ends the program ::@:: `int close(int fd)`, called as `close(fd)`: `fd` names the open FIFO; it releases the descriptor and returns `0`, or `-1` with `errno`, and the program passes that result on.

## blocking open

A FIFO conveys nothing while only one end is open, so `open` blocks. A process opening for `O_WRONLY` waits for a reader; one opening for `O_RDONLY` waits for a writer. Either may start first: whichever comes second releases the first from its `open`.

`O_NONBLOCK` in the flags removes the wait: `open` returns at once. The caller then learns nothing from `open` about the other end, so it must handle a write that finds no reader.

A writer cannot get ahead of its reader: its `open` returns only once a reader is there. While it waits, it can do nothing else.

---

Flashcards for this section are as follows:

- why `open` on a named pipe blocks ::@:: Until both ends are open the pipe conveys nothing, so the call waits for the other end.
- what a process that opens a named pipe for `O_WRONLY` waits for ::@:: A process that opens the same pipe for reading.
- what a process that opens a named pipe for `O_RDONLY` waits for ::@:: A process that opens the same pipe for writing.
- why the order in which two programs start does not matter on a named pipe ::@:: Whichever opens first blocks in `open` until the other opens, so neither runs ahead.
- open flag that stops a named pipe's `open` from blocking ::@:: `O_NONBLOCK`.
- what a writer gives up by opening a named pipe with `O_NONBLOCK` ::@:: Any word from `open` about whether a reader exists, so it must handle a write that finds none.
- what a blocking `open` on a named pipe protects a writer from ::@:: Getting ahead of its reader: no message leaves before a reader has the pipe open.
- cost a blocking `open` on a named pipe puts on a writer ::@:: The writer can do nothing else while it waits for a reader.

## reading and writing

Once both ends are open the FIFO works through the ordinary file calls: `open`, then `read` and `write` on the descriptor, then `close`. `read` returns how many bytes it took, possibly fewer than were asked for, and `0` only when nothing is left and no writer holds the pipe open. `write` returns how many bytes it accepted, also possibly fewer; the data reaches the reader at once and is stored nowhere.

The receiver opens for reading, takes at most a buffer's worth, and passes on exactly what arrived.

```c
#include <fcntl.h>
#include <unistd.h>

#define FIFO_PATH "/tmp/demo.fifo"
#define BUFSIZE 64

int main(void)
{
    char message[BUFSIZE];
    int fd = open(FIFO_PATH, O_RDONLY);          /* blocks until a writer opens as well */
    if (fd == -1)
        return 1;
    ssize_t n = read(fd, message, sizeof message);   /* at most BUFSIZE bytes */
    if (n == -1)                                 /* -1 reports the failure itself */
        return 1;
    if (write(STDOUT_FILENO, message, (size_t) n) != n)   /* pass on exactly what arrived */
        return 1;
    return close(fd);
}
```

The data is consumed: a byte one reader has taken is gone. A FIFO queues bytes for a single consumer; it is not a file several processes can read. When the last descriptor closes, any data still unread is discarded.

---

Flashcards for this section are as follows:

- the calls that use a named pipe once both ends are open ::@:: `open`, then `read` and `write` on the descriptor, then `close`.
- prototype of `read()`, and the call the receiving program makes ::@:: `ssize_t read(int fd, void *buf, size_t count)`, called as `read(fd, message, sizeof message)`: `fd` is the open FIFO, `message` the buffer, and `count` the most bytes to take; it returns the count, `0` at the end of the data, or `-1`.
- what `read()` returns on a named pipe, and when it returns `0` ::@:: How many bytes it took, possibly fewer than asked for; `0` means nothing is left and no writer holds the pipe open.
- what `write()` returns on a named pipe, and where the bytes go ::@:: How many bytes it accepted, possibly fewer; the bytes reach the reader at once and are stored nowhere.
- what happens to data in a named pipe once a reader has taken it ::@:: It is gone, so the pipe serves one consumer and the data cannot be read twice.
- what `close` does to a named pipe's unread data ::@:: The unread data is discarded once the last descriptor closes.

## several writers

Several processes may write to one FIFO. An ordinary pipe cannot do that, since it belongs to the family that inherited it. The traffic still reaches one reader: whoever reads a message first takes it.

---

Flashcards for this section are as follows:

- how many processes may write to one named pipe ::@:: Several, where an ordinary pipe allows only its own family.
- why a named pipe cannot broadcast one message to several readers ::@:: A `read` consumes the data, so only the reader that takes it gets the message.

### atomic writes and PIPE_BUF

`PIPE_BUF` is the system's size limit on an atomic pipe write: at least 512 bytes under the POSIX standard, 4096 on Linux. A write up to that size arrives in one piece, with no other writer's bytes inside it. A larger write may be split and mixed with another writer's output, so a reader can find two records interleaved. Once `PIPE_BUF` bytes are waiting, the next write blocks until a reader takes some.

---

Flashcards for this section are as follows:

- what `PIPE_BUF` is, and its two values ::@:: The system's size limit on an atomic pipe write: at least 512 bytes under POSIX, 4096 on Linux.
- size at which a write to a named pipe stays in one piece ::@:: Up to `PIPE_BUF` bytes, which arrives whole, with no other writer's bytes inside it.
- what can happen to a write larger than `PIPE_BUF` on a shared named pipe ::@:: It may be split and interleaved with another writer's output.
- what a write to a named pipe does once `PIPE_BUF` bytes are waiting ::@:: It blocks until a reader takes some.

## placement and permissions

A FIFO needs a path both processes can reach, and `/tmp` is the usual place because any user may create a file there. That reach is also the risk: a name in `/tmp` is visible to every user, so the permissions passed to `mkfifo` decide who can open the pipe, and someone else can create a predictable name first. Those bits are the same mode `open()` takes, tabulated under [permission bits](system%20call.md#permission%20bits).

Two habits follow: check the name before creating the pipe, and delete it afterwards, since a FIFO in `/tmp` outlives the processes that used it.

---

Flashcards for this section are as follows:

- why a named pipe is usually created under `/tmp` ::@:: Every user may create a file there, so two processes with no shared directory still reach one path.
- what decides which processes may open a named pipe ::@:: Its permissions, which the `mode` argument of `mkfifo()` sets.
- why a predictable name in `/tmp` is risky ::@:: Every user sees the name and can create it first, so the program may find someone else's pipe.
- why a program checks for a named pipe before creating it ::@:: Creating a name that already exists fails, so a second run reuses the pipe.
- why a named pipe in `/tmp` should be deleted when it is no longer needed ::@:: It outlives the processes that used it, so the name stays behind run after run.
