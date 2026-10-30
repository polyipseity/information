---
aliases:
  - COMP 3511 lab 3
  - HKUST COMP 3511 lab 3
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/labs/lab_3/lab
  - language/in/English
---

# lab

- HKUST COMP 3511 lab 3
- parent: [lab 3](index.md)

## process creation with fork

`fork()` creates a new process as a copy of the caller. Both return from the call and resume at the next statement, and the child gets its own address space and registers, so a variable written in one copy keeps its old value in the other.

The parent gets the new child's process identifier (PID), the child gets `0`, and `-1` reports failure with the reason in `errno`.

The scheduler picks which runs first, so their output interleaves differently each time.

---

Flashcards for this section are as follows:

- prototype of `fork()`, and the call that starts a child process ::@:: `pid_t fork(void)`, called as `fork()`: returns twice, `0` in the child and the child's process identifier in the parent, or `-1` with the reason in `errno`.
- prototype of `execlp()`, with the arguments that run `ls` ::@:: `int execlp(const char *file, const char *arg0, ...)`, called as `execlp("ls", "ls", "-l", "-h", NULL)`: runs `ls` with one option in place of the current program, and returns only if the search fails.
- prototype of `execvp()`, and the argument array it takes ::@:: `int execvp(const char *file, char *const argv[])`, called as `execvp("ls", args)`: runs `ls` from the array `{"ls", "-l", "-h", NULL}`, whose first element repeats the program name and whose last element `NULL` ends it.
- memory a child process receives from `fork()` ::@:: its own copy of the parent's address space, so a variable written in one copy keeps its old value in the other
- which of the parent and the child reaches the next statement first after `fork()` ::@:: either one, since the scheduler decides; the output order varies between runs
- statement both processes continue from after `fork()` ::@:: the statement that follows the call, because both return from it

## process identifiers and sleeping

`getpid()` returns the process identifier (PID) of the calling process, `getppid()` the parent's. Both return `pid_t`, the system type for a process identifier.

```c
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
    pid_t pid = getpid();
    pid_t ppid = getppid();

    printf("Current program PID: %d\n", pid);
    printf("Parent program PID: %d\n", ppid);

    return 0;
}
```

`sleep()` suspends the caller for whole seconds, `usleep()` for part of one, and `nanosleep()`, declared in `<time.h>`, for seconds and nanoseconds. A sleeping process gives up the processor, so the others run.

---

Flashcards for this section are as follows:

- function that returns the process identifier (PID) of the calling process, and the one that returns its parent's ::@:: `getpid()` for the process, `getppid()` for its parent
- declaration of `getpid()`, and the call that prints the identifier ::@:: `pid_t getpid(void);`, called as `getpid()`: returns the process identifier of the calling process.
- declaration of `getppid()`, and the call that prints the parent's identifier ::@:: `pid_t getppid(void);`, called as `getppid()`: returns the process identifier of the calling process's parent.
- unit of the argument of `sleep()`, and the call to use for part of a second ::@:: whole seconds for `sleep()`, `usleep()` for a fraction of a second
- header that declares `nanosleep()` ::@:: `<time.h>`
- whether a process that calls `sleep()` stops the other processes on the machine ::@:: no; the sleeping process gives up the processor and the others keep running
- unit of the interval that `nanosleep()` sleeps for ::@:: seconds and nanoseconds

## signals as software interrupts

A signal is a software generated interrupt. Ctrl-C sends one to the foreground process, whose default action kills it.

A program replaces the default action with its own handler through [`signal()`](../../thread%20(computing).md#signals%20and%20their%20default%20actions). A child created afterwards inherits its parent's signal settings and keeps the handler.

---

Flashcards for this section are as follows:

- what a signal is in C system programming ::@:: a software generated interrupt
- what pressing Ctrl-C sends to the process in the foreground ::@:: a signal, whose default action terminates the process
- which processes inherit a custom signal handler from their parent ::@:: the child processes created after the handler was installed

## zombie and orphan processes

A terminated process still holds its process table entry and an exit status to collect, until the parent reaps it with `wait()`. That entry is a [zombie process](../../process%20(computing).md#zombie%20process).

When the parent terminates first, the child becomes an [orphan process](../../process%20(computing).md#orphan%20process). The init process, whose process identifier is `1`, adopts and reaps it later, so the entry does not stay.

The program below orphans the child deliberately: the parent prints ten lines and exits, the child sleeps a second, then prints its own.

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main()
{
    pid_t pid;
    int i;

    pid = fork();
    if (pid > 0) {
        for (i = 0; i < 10; i++)
            printf("Parent %d\n", i);
    } else {
        sleep(1);
        for (i = 0; i < 10; i++)
            printf("Child %d\n", i);
    }
    return 0;
}
```

```text
Parent 0
Parent 1
Parent 2
Parent 3
Parent 4
Parent 5
Parent 6
Parent 7
Parent 8
Parent 9
Child 0
Child 1
Child 2
Child 3
Child 4
Child 5
Child 6
Child 7
Child 8
Child 9
```

The shell returns its prompt after the tenth parent line, before any child line appears; the child keeps printing with no parent left to reap it.

---

Flashcards for this section are as follows:

- process that adopts an orphan, and its process identifier (PID) ::@:: the init process, whose process identifier is `1`
- call through which a parent reaps a terminated child ::@:: `wait()`
- where the child's lines appear when the parent prints ten lines and exits while the child sleeps a second ::@:: after the shell prompt, since the parent exits first and leaves no parent to reap the child

## waiting for a child process

`wait()` waits for a child of the calling process to change state. It returns that child's process identifier (PID) and stores the exit status where the argument points; `0` or `NULL` says the status is not needed. `waitpid()` and `waitid()` are more general; the project uses `wait()` alone.

A child that returns `0` from `main` exits without error, and its status reads `0`.

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main()
{
    int child_status;
    pid_t child_pid;

    pid_t pid = fork();
    if (pid == 0) {
        return 0;
    } else {
        printf("Parent PID %d\n", getpid());
        child_pid = wait(&child_status);
        printf("Child PID %d with status %d\n", child_pid, child_status);
    }
    return 0;
}
```

```text
Parent PID 3915
Child PID 3916 with status 0
```

Without a wait the two race, so the output order changes between runs; a wait after the parent's work removes the race.

---

Flashcards for this section are as follows:

- declaration of `wait()`, and the call a parent makes ::@:: `pid_t wait(int *status)`, called as `wait(&child_status)`: blocks until a child ends, returns its identifier, and stores the exit status through the pointer.
- value `wait()` returns once a child has terminated ::@:: the process identifier (PID) of the child that terminated
- exit status `0` of a child process ::@:: the child returned from `main` without an error
- what a `wait(0)` after a parent's own work fixes about its output ::@:: the child has already finished, so the two processes print in a fixed order

## exec family

The `exec` family replaces the running program with another. The names here are `execl`, `execlp`, `execle`, `execv`, `execvp` and `execvpe`, each `exec` plus letters saying how the call is made.

| letter | decision it fixes |
| --- | --- |
| `l` | arguments arrive as separate parameters, closed by `NULL` |
| `v` | arguments arrive as one array, `char *const argv[]`, closed by `NULL` |
| `p` | a program named without a `/` is looked up in the directories of `PATH` |
| `e` | the caller passes `envp`, instead of the new program inheriting `environ` |

Every name carries `l` or `v`, never both, plus `p` or `e` only where one applies, which gives eight combinations. Six carry standard names: `execl` and `execv` with neither letter, `execlp` and `execvp` with the path search, `execle` and `execve` with the environment. The GNU library adds `execvpe`, the seventh, pairing the path search with an environment. The eighth, `execlpe`, has no name, so a caller wanting both builds an array and runs `execvpe`.

`execve` is the call the kernel provides; the rest are library functions around it. The `l` forms gather their parameters into an array, and names without `e` hand over the caller's `environ`.

A successful `exec*()` never returns, since its process image is gone. A failure returns `-1`, so an error message after the call belongs in the child branch.

```c
#include <stdio.h>
#include <unistd.h>

int main()
{
    /* Same as running "ls -l -h" */
    execlp("ls", "ls", "-l", "-h", NULL);

    /* Reached only if execlp fails */
    printf("It won't return. Nothing is shown here\n");

    return 0;
}
```

The vector form takes the same values in one array, which suits a command line built at run time.

```c
#include <stdio.h>
#include <unistd.h>

#define MAX_SEGMENT_LENGTH 256

int main()
{
    char *args[MAX_SEGMENT_LENGTH] = {"ls", "-l", "-h", NULL};

    execvp("ls", args);
    return 0;
}
```

The first element repeats the program name and the array ends with `NULL`, where the call stops reading.

---

Flashcards for this section are as follows:

- what an `exec*()` call does to the calling process ::@:: it replaces the process image with a new program; the process identifier (PID) stays the same
- when an `exec*()` call returns ::@:: only on error, with `-1`; a successful call never returns
- difference between `execlp` and `execvp` ::@:: `execlp` takes each argument as its own parameter, `execvp` a `NULL`-terminated array
- meaning of the `p` in `execlp` and `execvp` ::@:: the call searches the directories named in `PATH` for the program instead of taking a fixed path
- why the argument array of `execvp` ends with `NULL` ::@:: the call reads the array until it meets `NULL`, so the terminator marks the last argument
- meaning of the `e` in the names `execle` and `execvpe` ::@:: the caller supplies the environment for the new program
- the four letters that may follow `exec` in a call name, and the decision each fixes ::@:: `l` takes separate parameters, `v` one array, `p` searches `PATH` for a name without a `/`, and `e` makes the caller pass `envp` instead of letting the new program inherit `environ`.
- which of the `exec` letters every call name carries, and why the choice is forced ::@:: exactly one of `l` or `v`, since the arguments arrive either as separate parameters or as one array; `p` and `e` are added only when the call does that.
- the one `exec` letter combination that has no call of its own ::@:: `execlpe`, a list of arguments with a path search and an explicit environment; the same effect is built as an array and run with `execvpe`.
- which `exec` call the kernel provides, and what the other names are ::@:: `execve`, which takes an array and an environment; the rest are library functions around it, which assemble that array and, without `e`, pass the caller's `environ`.
- what an `exec` call with `p` does when the program name already contains a `/` ::@:: it skips the `PATH` search and treats the name as the path to the program.
- environment the new program starts with when the `exec` name has no `e` ::@:: the caller's own, taken from the external variable `environ`.

## fork counting puzzles

Each fork doubles the process count, since the caller and its new child both carry on. A loop of `n` forks that every process runs ends with $2^n$ processes.

Shortcut evaluation of `&&` and `||` changes the count. In `fork() && fork()`, only the parent runs the second call, since the child's `0` is false; in `fork() || fork()`, only the child runs it, since the parent's non-zero result already decided the test.

> A program runs `for (i = 0; i < 3; i++) fork();` and returns. How many processes exist at the end?
>
> ---
>
> - solution: {@{8 processes}@}
> - explanation: {@{Each pass of the loop}@} {@{doubles the process count}@}, because both {@{the caller and the new child continue the loop}@}. Three {@{doublings give $2^3 = 8$}@}.

<!-- markdownlint MD028 -->

> A program runs `for (i = 0; i < 2; i++) { fork(); for (j = 0; j < 3; j++) if (!fork()) { } }`. How many processes exist at the end?
>
> ---
>
> - solution: {@{256 processes}@}
> - explanation: {@{Each pass of the outer loop}@} runs {@{one `fork()` and then three more inside the `j` loop}@}, so a pass holds {@{four doublings}@}. Eight {@{doublings give $2^8 = 256$}@}.

<!-- markdownlint MD028 -->

> A program runs `for (i = 0; i < 10; i++) { if (fork()) { fork(); fork(); } else fork(); }`. How many processes exist at the end?
>
> ---
>
> - solution: {@{$6^{10}$ processes}@}
> - explanation: In {@{one pass}@}, a process becomes {@{four in the `if` branch, one for itself and two more forks}@}, and {@{two in the `else` branch, one for itself and one more fork}@}. Each pass leaves {@{six processes behind}@}, and ten passes {@{multiply the total by six, ten times}@}.

<!-- markdownlint MD028 -->

> In the test `if (fork() && fork()) ... else ...`, how many processes enter each branch?
>
> ---
>
> - solution: {@{1 process enters the `if` branch and 2 enter the `else` branch}@}
> - explanation: The first `fork()` returns {@{$0$ in the child, and that `0` is false}@}, so the child {@{skips the second `fork()` and takes the `else` branch}@}. The parent returns {@{a non-zero process identifier (PID), so it runs the second `fork()`}@}. The second call {@{splits that parent the same way}@}. Only {@{the parent enters the `if` branch}@}, because {@{the child of the second call receives `0` and falls to the `else`}@}.

<!-- markdownlint MD028 -->

> In the test `if (fork() || fork()) ... else ...`, how many processes enter each branch?
>
> ---
>
> - solution: {@{2 processes enter the `if` branch and 1 enters the `else` branch}@}
> - explanation: The parent of the first `fork()` returns {@{a non-zero process identifier (PID), which is true and ends the test}@}, so it {@{never runs the second `fork()`}@}. The child returns {@{$0$, so it runs the second `fork()`}@}. That second call splits the child the same way. {@{The child of that second call}@} is {@{the single process that reaches the `else` branch}@}.

<!-- markdownlint MD028 -->

> A loop of `n` passes runs `left_fork = fork(); right_fork = fork();` in each pass and then prints one line when the two stored values are equal. How many lines appear when `n` is 3?
>
> ---
>
> - solution: {@{21 lines}@}
> - explanation: Each pass leaves {@{four processes}@}, and {@{exactly one of them sees two equal values}@}, because the two calls return {@{equal values, i.e. 0, only in the child of both calls}@}. Each further pass {@{multiplies the process count by four}@}, so the passes print {@{$1 + 4 + 16$ lines, which is 21}@}.

---

Flashcards for this section are as follows:

- number of processes left by $n$ consecutive `fork()` calls that every process runs ::@:: $2^n$
- number of processes left by `fork() && fork()` ::@:: three processes, with one in the true branch and two in the false branch
- why the second `fork()` of `fork() && fork()` never runs in the first child ::@:: that child receives `0` from the first call, and a false left operand ends the test
- number of processes left by `fork() || fork()` ::@:: three processes, with two in the true branch and one in the false branch
- why the second `fork()` of `fork() || fork()` never runs in the first parent ::@:: that parent receives a non-zero process identifier (PID), and a true left operand already decided the test

## file system calls

The low-level file calls are `open`, `read`, `write` and `close`, declared in `<fcntl.h>` and `<unistd.h>`. Each works on a file descriptor, a small integer naming an open file. Three open at start: `0` for standard input, `1` for standard output, `2` for standard error.

`open` takes a path, a flag holding one access mode (`O_RDONLY`, `O_WRONLY` or `O_RDWR`) plus modifiers such as `O_CREAT`, and permissions for a file it creates. `S_IRUSR` gives owner read and `S_IWUSR` write, so the pair is mode 600.

```c
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>

int main()
{
    int fd;
    char buffer[10];

    /* Example: Write a text file */
    /* create hello.txt for writing, with owner read and write */
    fd = open("hello.txt", O_CREAT | O_WRONLY, S_IRUSR | S_IWUSR);
    write(fd, "hello\n", 6);
    close(fd);

    /* Example: Read a text file */
    /* open the same file for reading */
    fd = open("hello.txt", O_RDONLY);
    read(fd, buffer, 6);

    printf("%s", buffer);
    close(fd);

    return 0;
}
```

`read` returns the byte count and adds no terminator, so a buffer printed as a string must respect that count. The mode argument of `open()` is an OR of constants or one octal number: `S_IRUSR | S_IWUSR` is `0600`, owner read and write; [permission bits](../../system%20call.md#permission%20bits) gives the whole table. The C library's `fopen`, `fread`, `fwrite` and `fclose` work on a `FILE` pointer, and a `FILE` cannot go to the pipe calls, so the project avoids them.

---

Flashcards for this section are as follows:

- four file system calls that work on a file descriptor ::@:: `open`, `read`, `write` and `close`
- prototype of `open()`, and the call that creates the file ::@:: `int open(const char *path, int flags, ...)`, called as `open("hello.txt", O_CREAT | O_WRONLY, S_IRUSR | S_IWUSR)`: `O_CREAT` creates the file, `O_WRONLY` opens it for writing only, and the mode `S_IRUSR | S_IWUSR` is `0600`, owner read and write; the mode is read only because `O_CREAT` is set.
- file descriptors already open for standard input, standard output and standard error ::@:: `0`, `1` and `2`
- flag combination that creates a file for writing, and the permission bits for owner read and write ::@:: `O_CREAT | O_WRONLY`, with `S_IRUSR | S_IWUSR`
- what `read()` returns, and what it does not add to the buffer ::@:: the byte count; it adds no terminating null character
- why the project avoids `FILE *` from `<stdio.h>` ::@:: a `FILE` is a C library structure, and it cannot be passed to the pipe system calls
- file descriptor in the C file system calls ::@:: a small integer that names an open file

## anonymous pipe

A pipe makes the output of one process the input of another. A command line chains several with `|`: `ps aux | grep root | sort | wc -l`.

`pipe(pfds)` creates an unnamed pipe and fills an array of two descriptors: `pfds[0]` reads, `pfds[1]` writes. Data written at one end comes out at the other in order, and a short write stays in one piece instead of mixing with another writer's. Both `read` and `write` block until they can complete, and only a descendant of the creating process can reach the pipe.

---

Flashcards for this section are as follows:

- how an unnamed pipe connects two processes ::@:: the output of one process becomes the input of another
- prototype of `pipe()`, and the call that fills the array ::@:: `int pipe(int pipefd[2])`, called as `pipe(pfds)`: creates the channel and fills the array, with `pfds[0]` reading and `pfds[1]` writing.
- prototype of `read()`, and the call that reads from the pipe ::@:: `ssize_t read(int fd, void *buf, size_t count)`, called as `read(pfds[0], message, 5)`: `pfds[0]` is the read end, `message` the buffer, and `5` the most bytes it may take; it returns how many arrived, `0` at the end, or `-1`.
- prototype of `write()`, and the call that writes to the pipe ::@:: `ssize_t write(int fd, const void *buf, size_t count)`, called as `write(pfds[1], "test", 5)`: `pfds[1]` is the write end, `"test"` the bytes, and `5` how many of them, including the terminator; it returns the count accepted, or `-1`.
- prototype of `close()`, and the call that drops one end ::@:: `int close(int fd)`, called as `close(pfds[0])`: drops the end this process will not use, so the other side sees the end of the data.
- prototype of `dup2()`, and the two descriptors it takes ::@:: `int dup2(int oldfd, int newfd)`, called as `dup2(pfds[1], 1)`: `pfds[1]` is the descriptor to copy and `1` the one it replaces, closed first, so the shell's standard output now ends at the pipe.
- prototype of `dup()`, and the call that copies a descriptor ::@:: `int dup(int oldfd)`, called as `dup(fd)`: returns the lowest free descriptor for the same open file, so two numbers reach one file.
- end of an unnamed pipe held by each element of the array that `pipe()` fills ::@:: `pfds[0]` is the read end, and `pfds[1]` is the write end
- order in which a pipe delivers data it receives ::@:: the order the data was sent
- what the requirement that both ends of a pipe share a parent preserves ::@:: the unnamed pipe is inherited through `fork()`, so both processes must descend from the one that created it
- whether `read` and `write` on a pipe return immediately ::@:: no; both block until the transfer can complete

### pipe between parent and child

The child writes, the parent reads. Each closes the end it does not use: a pipe with a writer still open never reports the end of the data.

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main()
{
    int pfds[2];
    char message[30];

    pipe(pfds);
    pid_t pid = fork();
    if (pid == 0) {
        printf("CHILD: writing to pipe\n");
        close(pfds[0]);
        write(pfds[1], "test", 5);
        printf("CHILD: exiting\n");
    } else {
        printf("PARENT: reading from pipe\n");
        close(pfds[1]);
        wait(NULL);
        read(pfds[0], message, 5);
        printf("PARENT: read \"%s\"\n", message);
    }
    return 0;
}
```

`fork()` hands both ends on, so each process holds both until it closes the one it does not need.

The reverse direction swaps the roles: the parent closes `pfds[0]`, writes to `pfds[1]`, waits and exits; the child closes `pfds[1]` and reads from `pfds[0]`.

---

Flashcards for this section are as follows:

- end of the pipe that the child closes when it writes ::@:: `pfds[0]`, the read end
- why each process closes the end of the pipe it does not use ::@:: a pipe that still has a writer open never reports the end of its data to the reader
- how the child process obtains a working file descriptor for the pipe ::@:: it inherits both descriptors from the parent through `fork()`
- what the parent does before it reads the bytes the child wrote ::@:: it calls `wait(NULL)`, so the child has finished writing

### duplicating file descriptors

`dup(oldfd)` copies an open descriptor into the lowest free number and returns the new one. `dup2(oldfd, newfd)` copies it into a chosen number, closing what was there. Both are declared in `<unistd.h>`.

Closing descriptor `1` and duplicating a file into its place sends standard output there, so `printf` writes into it.

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <fcntl.h>

int main()
{
    int fd;
    fd = open("output.txt", O_CREAT | O_WRONLY, S_IRUSR | S_IWUSR);

    close(1);
    dup(fd);

    printf("Hello World!\n");
    fflush(stdout);

    return 0;
}
```

The program prints nothing on the terminal: standard output now belongs to `output.txt`, which receives the line. `dup2(fd, 1)` does the same in one call and names the target descriptor, so nothing depends on the lowest free number.

---

Flashcards for this section are as follows:

- descriptor that `dup2(oldfd, newfd)` installs the copy in ::@:: the number passed as `newfd`, whose previous file is closed first
- effect of `close(1)` followed by `dup(fd)` ::@:: standard output becomes the open file `fd` names, so `printf` writes into that file
- one call that redirects standard output to an open file descriptor ::@:: `dup2(fd, 1)`

### command-line pipe

The shell command `ls | wc -l` runs two programs on one pipe. The child sends its standard output into `pfds[1]`, the parent takes its standard input from `pfds[0]`, so both keep their usual descriptors and never see the pipe.

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main()
{
    int pfds[2];
    pipe(pfds);
    pid_t pid = fork();
    if (pid == 0) {
        close(1);
        dup2(pfds[1], 1);
        close(pfds[0]);
        execlp("ls", "ls", NULL);
    } else {
        close(0);
        dup2(pfds[0], 0);
        close(pfds[1]);
        wait(0);
        execlp("wc", "wc", "-l", NULL);
    }
    return 0;
}
```

Each process runs the same three steps: close the destination, copy the pipe end into its place, close the unused end, then let `exec` replace the program. The parent waits before it execs the counter, so the listing finishes first.

---

Flashcards for this section are as follows:

- descriptor the child rewires before running `ls` in an `ls | wc -l` implementation ::@:: descriptor `1`, standard output, which is replaced by `pfds[1]`
- descriptor the parent rewires before running `wc` ::@:: descriptor `0`, standard input, which is replaced by `pfds[0]`
- why the unused pipe end is closed before `exec` runs ::@:: the new program inherits the open descriptors, and a stray writer hides the end of the data from the reader
- why the parent waits before it execs the counting program ::@:: the directory listing must be finished before the count starts
- call that redirects standard output into the write end of a pipe in one step ::@:: `dup2(pfds[1], 1)`
- order in which a program on one end of a pipe sets up its descriptors before `exec` replaces it ::@:: close the destination descriptor, copy the pipe end into its place with `dup2`, then close the unused pipe end

## shape of a simplified shell

A shell loops over four steps: prompt and read a line, split it into a program and its arguments, fork, wait. The child branch calls one of the `exec*()` calls; the parent waits. Whatever the child does to file descriptors before the exec, such as a redirection or a pipe end, changes the program it becomes.

The line takes several shapes, each recognised before the fork: a plain command, one with input redirection, one with output redirection, both redirections in either order, or a chain joined by pipes. Redirection reuses `open`, `close` and `dup`. A chain of `n` commands needs `n - 1` pipes and one `fork()` each.

One command cannot be handled that way. `cd` must change the working directory of the shell itself, since a child's change would vanish with the child. `chdir(path)` does that work, and the shell calls it directly.

---

Flashcards for this section are as follows:

- four steps of the loop at the centre of a simplified shell ::@:: read a command line, split it into a program and arguments, fork, and wait for the child
- call that replaces the program in the child of a shell ::@:: one of the `exec*()` calls, such as `execvp`, which searches `PATH`
- why `cd` cannot be run through `fork` and `exec` ::@:: it must change the working directory of the shell itself, and a child's change disappears when the child exits
- call the shell uses to change its own working directory ::@:: `chdir(path)`
- number of pipes a chain of $n$ commands joined by pipes needs ::@:: $n - 1$ pipes, with one `fork()` for each command
- where the shell handles a failed `exec` ::@:: in the child branch, because the call returns only when the program did not start
- what the child can change before `exec` so that the new program inherits it ::@:: its open file descriptors, which is how a redirection or a pipe end reaches the program
- command line shapes that a shell built on `fork` and the `exec*()` calls recognises before it forks ::@:: a plain command, one with input redirection, one with output redirection, both redirections in either order, and a chain of commands joined by pipes
- file system calls a shell redirection is built from ::@:: `open`, `close` and `dup`
