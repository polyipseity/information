---
aliases:
  - COMP 3511 inter-process communication
  - IPC
  - inter-process communication
  - interprocess communication
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/inter-process_communication
  - language/in/English
---

# inter-process communication

Cooperating processes share data, and sharing needs a mechanism: inter-process communication (IPC). Two models cover it. With shared memory, processes read and write one region of memory; with message passing, they exchange explicit messages. Message passing costs more, because every message goes through the kernel, but it still works between machines that share no memory. Pipes, sockets and remote procedure calls are built on both.

---

Flashcards for this section are as follows:

- inter-process communication (IPC) ::@:: A mechanism that lets cooperating processes exchange data through shared memory or by passing messages.
- two models of inter-process communication (IPC) ::@:: Shared memory, in which processes read and write a common region, and message passing, in which they exchange explicit messages.
- how the two models differ in cost ::@:: Once the region exists, shared memory moves data by ordinary memory access. Message passing sends every exchange through the kernel: slower, but it works across machines.
- concrete mechanisms built on the shared-memory and message-passing models ::@:: Pipes, sockets and remote procedure calls.

## cooperation between processes

A process is independent when it can neither affect nor be affected by another. It cooperates when it shares data with others, so each can change the other's state. Cooperation happens inside one multithreaded process as well as between processes.

Processes cooperate for three reasons. Information sharing covers applications that need the same data, as when text is copied in one application and pasted into another. Computation speedup splits a task into subtasks that run in parallel, as in machine learning work. Modularity divides a system among separate processes or threads.

---

Flashcards for this section are as follows:

- independent process ::@:: A process that neither affects nor is affected by another process.
- cooperating process ::@:: A process that shares data with another, so each can change the other's state.
- reasons for processes to cooperate ::@:: Information sharing, computation speedup and modularity.
- information sharing ::@:: Several applications want the same data, as when text copied in one application is pasted into another.
- computation speedup ::@:: A task divided into subtasks that run in parallel, as in machine learning work.
- modularity ::@:: A system divides its functions among separate processes or threads.
- why cooperation needs a mechanism ::@:: One process's writes must reach another, and separate address spaces offer no way to do so without the kernel.
- where cooperation occurs besides between separate processes ::@:: Inside one multithreaded process, whose threads share data with each other.

## shared memory

In the shared-memory model a region of memory belongs to two or more processes, and each exchanges information by writing into that region and reading from it. No message is sent, so the communication is implicit: one process stores a value and another finds it there.

The kernel sets the region up once and then takes no part, so each exchange is an ordinary memory access rather than a system call, which makes shared memory the faster model. Synchronization is the price: nothing stops two processes from writing the same slot at once, so they must agree on who writes when and who reads when.

The producer-consumer pair is the standard case. A producer writes at index in of a bounded buffer of $n$ slots, a consumer reads at index out, and both indices advance modulo $n$. A full buffer and an empty one both leave index in equal to out, so the buffer keeps one slot free and holds at most $n-1$ items. An unbounded buffer has no practical limit.

---

Flashcards for this section are as follows:

- shared memory ::@:: An inter-process communication model in which two or more processes own one region and exchange information by writing into it and reading from it.
- why shared-memory communication is implicit ::@:: No message is sent: one process writes a value into the shared region and another reads it there.
- why shared memory is fast ::@:: The kernel sets the region up once and then takes no part, so each exchange is an ordinary memory access, not a system call.
- what shared memory requires before use ::@:: The processes must agree on a region and its size, and each must reach it in its address space.
- synchronization burden of shared memory ::@:: Nothing stops two processes writing the same slot, so they must agree on the order of their reads and writes.
- producer and consumer processes ::@:: A producer makes information a consumer uses; the pair is the standard case of cooperating processes.
- bounded buffer with $n$ slots, indices in and out ::@:: The producer writes at index in, the consumer reads at index out, and each advances modulo $n$.
- why a simple bounded buffer holds $n-1$ items ::@:: A full buffer and an empty one both leave index in equal to index out, so keeping one slot free tells the two cases apart.
- unbounded buffer ::@:: A buffer with no practical limit on size, so its producer never waits.

## message passing

Message passing lets processes communicate and synchronize without sharing an address space, which makes it usable across a distributed system. It has two operations, send(message) and receive(message), and messages may be of fixed or variable size. Two processes must first establish a link, then exchange messages.

---

Flashcards for this section are as follows:

- message passing ::@:: An inter-process communication model in which processes exchange explicit messages through send() and receive() without sharing an address space.
- why message passing suits a distributed system ::@:: No shared memory is needed, so processes on different machines can use it.
- the two operations of message passing ::@:: send(message) and receive(message). A message may have a fixed size or a variable one.
- what two communicating processes must do first ::@:: Establish a link between them, then exchange messages through send() and receive().
- three decisions that shape a message-passing link ::@:: How the two processes name each other; whether send and receive block; and how many messages the link may queue.

### direct and indirect communication

In direct communication each process names the other, as in send(P, message) and receive(Q, message). The link exists automatically, belongs to that pair alone, and each pair has exactly one. The weakness is modularity: change one process's identifier and every process that names it must change too.

In indirect communication messages go to and come from a mailbox, each with a unique identifier, and two processes communicate only while they share one. The kernel creates mailboxes, carries messages through them and destroys them. A link exists only while both processes hold the mailbox, may involve more than two processes, and gives a pair one link per shared mailbox. Several processes reading one mailbox need a rule: the system may allow a link to at most two processes, allow one receive at a time, or pick a receiver and tell the sender which one it chose.

---

Flashcards for this section are as follows:

- direct communication ::@:: Each process names the other explicitly, as in send(P, message) and receive(Q, message).
- properties of a direct link ::@:: It exists automatically between each pair that wants to communicate and belongs to that pair alone; each pair has exactly one.
- weakness of direct communication ::@:: Modularity is poor. Changing one process's identifier means editing every process that names it.
- indirect communication ::@:: Messages go to and come from mailboxes, each with a unique identifier. Processes communicate only while they share a mailbox.
- mailbox operations the kernel provides ::@:: Create a mailbox, send and receive through it, and destroy it.
- properties of an indirect link ::@:: It exists only while both processes hold the mailbox, may involve more than two processes, and a pair may have one link for each shared mailbox.
- several receivers on one mailbox ::@:: Only one process receives each message. The system may limit a link to two processes, allow one receive at a time, or choose a receiver and tell the sender which one.

### synchronous and asynchronous communication

Send and receive are synchronous when they block, asynchronous when they return at once. A blocking send waits until a process receives the message or the system places it in a mailbox; a blocking receive waits until a message is available. A non-blocking send hands the message over and continues; a non-blocking receive returns a valid message or null.

A blocking send and a blocking receive on a link with no room to queue make a rendezvous: the sender waits for a receiver, and the message passes straight into the receiver's hands with nothing stored between them. The second to arrive completes the handover. The name belongs to the meeting, not the waiting.

Only one of the two waits at a time: a blocking send waits for a receiver and a blocking receive for a message, but whichever arrives second satisfies the first, so the pair is never both stuck on each other. Nor is it a cycle of waits: a message in flight is not a resource either side holds while asking for another, so nothing circular forms and a rendezvous alone cannot deadlock. Coupling is the cost. The sender cannot run even one message ahead of the receiver, so a slow receiver throttles it and an absent one blocks it forever. That suits a request and reply exchange; unequal speeds waste throughput.

Blocking primitives settle the producer-consumer problem at once. The producer sends, the consumer receives, and the blocking keeps the two in step.

---

Flashcards for this section are as follows:

- blocking send ::@:: A synchronous send in which the sender waits until a process receives the message or the system places it in a mailbox.
- blocking receive ::@:: A synchronous receive in which the receiver waits until a message is available.
- non-blocking send ::@:: An asynchronous send in which the sender hands the message over and continues without waiting for a receiver.
- non-blocking receive ::@:: An asynchronous receive that returns a valid message if one is available and null otherwise.
- rendezvous ::@:: A transfer on a link with no room to queue: the sender waits for a receiver, the message passes straight through, and the second arrival completes the handover.
- what the name rendezvous names ::@:: The meeting itself, not the waiting. Both processes must arrive for the message to pass, and the second finds the other there.
- why a rendezvous is not two processes waiting on each other ::@:: Only one waits at a time, since the second arrival satisfies the first; a message in flight is not a resource either side holds while asking for another.
- cost of a rendezvous ::@:: The sender cannot run even one message ahead, so a slow receiver throttles it and an absent one blocks it forever.
- blocking primitives and the producer-consumer problem ::@:: The producer calls send() and the consumer calls receive(). Blocking keeps them in step, needing no other coordination.

### buffering capacity

Messages wait in a temporary queue on the link, whose capacity decides when a sender waits.

---

Flashcards for this section are as follows:

- zero-capacity link ::@:: A link that queues no messages. The sender waits until the receiver takes the message, which is a rendezvous.
- link whose queue holds at most $n$ messages ::@:: The sender waits while the queue holds $n$ messages, and continues when one is taken.
- unbounded-capacity link ::@:: A link whose queue has no fixed limit in length, so the sender never waits.

## ordinary pipe

A pipe is among the earliest inter-process communication mechanisms in UNIX. Four questions decide how one behaves: which way the data flows, half duplex or full duplex for a two-way pipe, whether the processes must be related, and whether it reaches across a network.

An ordinary pipe answers them narrowly: unidirectional, parent-child only, both processes on one machine. No outside process can reach it, and it ends when its users do.

A shell composes separate programs with a pipe. For `ls | grep x` it creates one and runs both commands: standard output of ls goes into the write end, grep reads the other end as standard input and prints only the lines containing x. Windows calls the same mechanism an anonymous pipe, reached through ReadFile() and WriteFile().

---

Flashcards for this section are as follows:

- ordinary pipe ::@:: A unidirectional inter-process communication channel between a parent process and its child on one machine, used through read() and write().
- lifetime of an ordinary pipe ::@:: It exists only while its processes do and ceases when they terminate.
- the four design questions for a pipe ::@:: Whether it is unidirectional or bidirectional, whether a bidirectional one is half duplex or full duplex, whether the processes must be related, and whether it spans a network.
- how a shell builds `ls | grep x` ::@:: It creates a pipe and two children: standard output of ls goes to the write end, standard input of grep comes from the read end, and both run at once.
- anonymous pipe ::@:: The Windows form of an ordinary pipe: unidirectional, needing a parent-child relationship, reached through ReadFile() and WriteFile().

### pipe() descriptors

```c
#include <unistd.h>

int pipe(int pipefd[2]);    /* 0 on success, -1 with errno set */
```

One message travels from the parent to the child; each side closes the end it does not use.

```c
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main(void)
{
    int pipefd[2];                    /* pipefd[0] reads, pipefd[1] writes */
    char message[16];
    if (pipe(pipefd) == -1)           /* the call fills both descriptors */
        return 1;

    pid_t child = fork();
    if (child == 0) {
        close(pipefd[0]);             /* the child writes, so it drops the read end */
        write(pipefd[1], "hello", 5); /* five bytes, the length of the message */
        close(pipefd[1]);
        _exit(0);
    }

    close(pipefd[1]);                 /* the parent reads, so it drops the write end */
    ssize_t n = read(pipefd[0], message, sizeof message);   /* at most 16 bytes */
    close(pipefd[0]);
    waitpid(child, NULL, 0);
    return n == 5 ? 0 : 1;
}
```

`pipe()` fills the array with two descriptors and no more: `pipefd[0]` is the read end, `pipefd[1]` the write end. UNIX treats a pipe as a special kind of file, so the standard `read()` and `write()` work on those descriptors. A child inherits both ends across `fork()`, and each side closes the end it does not use.

---

Flashcards for this section are as follows:

- `pipe()` descriptor ends ::@:: `pipe()` fills a two-element array: `pipefd[0]` reads and `pipefd[1]` writes.
- signature of `pipe()`, and the call the example makes on it ::@:: `int pipe(int pipefd[2])`, called as `pipe(pipefd)`: creates the channel and fills both integers, `pipefd[0]` reading and `pipefd[1]` writing.
- prototype of `fork()`, and the call that starts the writing child ::@:: `pid_t fork(void)`, called as `fork()`: makes the child that holds the write end, returning `0` there and its identifier in the parent.
- prototype of `_exit()`, and the call that ends the child once its bytes are sent ::@:: `void _exit(int status)`, called as `_exit(0)`: `status` is what the parent reads through `wait`, `0` for success; the call ends the child at once, skipping a flush of output its parent already printed.
- prototype of `write()`, and the call the child sends with ::@:: `ssize_t write(int fd, const void *buf, size_t count)`, called as `write(pipefd[1], "hello", 5)`: `pipefd[1]` is the write end, `"hello"` the bytes, `5` how many of them, so the terminator stays out; returns the count, or `-1`.
- prototype of `read()`, and the call the parent receives with ::@:: `ssize_t read(int fd, void *buf, size_t count)`, called as `read(pipefd[0], message, sizeof message)`: takes the five bytes the child wrote into a 16-byte buffer and returns the count, `0` once every writer has closed.
- prototype of `close()`, and the call that drops the end a process will not use ::@:: `int close(int fd)`, called as `close(pipefd[0])`: releases the descriptor; the reader sees the end of data only once every writer has closed its own end.
- prototype of `waitpid()`, and the call that reaps the writing child ::@:: `pid_t waitpid(pid_t pid, int *wstatus, int options)`, called as `waitpid(child, NULL, 0)`: `child` names that one child, `NULL` discards its status, and `0` blocks until it ends; returns its identifier, or `-1`.
- why ordinary read() and write() work on a UNIX pipe ::@:: UNIX treats a pipe as a special kind of file, so standard read() and write() operate on it.
- why an ordinary pipe needs related processes ::@:: The child inherits both ends across fork(); a process with no such relationship cannot reach it.
- closing the ends of a pipe ::@:: Each process closes the end it does not use: the writer closes the read end, the reader the write end.

## named pipe

A named pipe removes the parent-child condition: it appears as a file in the file system, so unrelated processes open it by name and several can write to it. It exists until someone deletes it, not until its users end. In UNIX a named pipe is a FIFO, created with mkfifo(). A FIFO is half duplex, so exchanging data both ways takes two, and both processes must sit on one machine. Windows named pipes allow full duplex and connect processes on different machines.

---

Flashcards for this section are as follows:

- named pipe ::@:: An inter-process communication channel that appears as a file in the file system. Unrelated processes open it by name, and several can write to it.
- lifetime of a named pipe ::@:: It continues to exist after the processes using it finish, until someone deletes it.
- FIFO ::@:: The UNIX form of a named pipe, created with mkfifo() and appearing as a file in the file system.
- direction of a UNIX FIFO ::@:: Half duplex: data travels one way at a time, so both directions need two.
- Windows named pipes ::@:: They allow full-duplex communication and connect processes on different machines, unlike the UNIX FIFO.
- machine scope of a UNIX FIFO ::@:: Both processes must sit on one machine.

## client-server communication

A client and a server often run on different machines, so their communication crosses a network. Sockets and remote procedure calls do it. In both, the server runs continuously at an address its clients know, waiting for requests, and only a client starts a conversation.

---

Flashcards for this section are as follows:

- two mechanisms for client-server communication ::@:: Sockets and remote procedure calls.
- role of a server in client-server communication ::@:: It runs continuously at a known address, waits for requests and answers them.
- who starts a client-server conversation ::@:: The client. A server only answers requests.

### socket

A socket is an endpoint of communication; a connection between two processes is a pair of sockets, one at each end. An address and a port number identify one: the address names the host, the port names the process on it. An Internet Protocol (IP) address is globally unique, 32 bits long in Internet Protocol version 4 (IPv4) and 128 bits long in Internet Protocol version 6 (IPv6).

A server listens on a well-known port below 1024, a range reserved for standard services. Secure Shell (SSH) listens on 22, File Transfer Protocol (FTP) on 21, and Hypertext Transfer Protocol (HTTP) on 80. A client knows the server's address and port, takes a free port above 1024, and connects. Four values identify the pair of communicating processes: the source address, the source port, the destination address and the destination port.

---

Flashcards for this section are as follows:

- socket ::@:: An endpoint of communication. A connection between two processes is a pair of sockets, one at each end.
- what identifies a socket ::@:: An Internet Protocol (IP) address naming the host, and a port number naming the process.
- Internet Protocol (IP) address sizes ::@:: 32 bits for Internet Protocol version 4 (IPv4) and 128 bits for Internet Protocol version 6 (IPv6). Every address is globally unique.
- well-known ports ::@:: Ports below 1024, reserved for standard services. A Secure Shell (SSH) server listens on 22, a File Transfer Protocol (FTP) server on 21 and a Hypertext Transfer Protocol (HTTP) server on 80.
- port a client chooses ::@:: A free port above 1024; the client already knows its own address and the server's.
- the four-tuple identifying a connection ::@:: The source Internet Protocol (IP) address, the source port, the destination address and the destination port.
- which side may start a socket conversation ::@:: The client. The server waits at its well-known port for clients.

### remote procedure call

A remote procedure call (RPC) makes a procedure call run on another machine: the call and its result cross the network as messages, so the scheme is message based. Distributed file systems use it, with daemons at the server and client programs on the user's side letting a local call reach a file that lives elsewhere.

---

Flashcards for this section are as follows:

- remote procedure call (RPC) ::@:: A procedure call whose procedure runs on another machine, reached across a network connection.
- why a remote procedure call is message based ::@:: The call and its result must cross a network, so both travel as messages between the two machines.
- remote procedure calls in distributed file systems ::@:: A set of daemons at the server and client programs on the user side let an ordinary procedure call operate on files held elsewhere.
