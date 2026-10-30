---
aliases:
  - readers and writers problem
  - readers-writers problem
  - readers–writers problem
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/readers–writers_problem
  - language/in/English
---

# readers–writers problem

The problem starts with a data set that many processes read and a few update. A plain lock makes it safe but slow, because it queues the readers behind one another as well as behind the writer. The aim is to keep the readers running together while a writer still gets the data set to itself.

The rule settles who may be inside together and leaves the waiting order open. A solution can let readers in and hold a writer aside while more arrive, or stop new readers once a writer waits. Both orders are correct, and either can starve the side it does not favour.

---

Flashcards for this section are as follows:

- why a plain lock is not enough for a shared data set ::@:: It queues readers behind one another although they do not conflict, so the concurrency the problem exists to keep is lost.
- what the readers-writers solutions differ in ::@:: Which side waits. A solution favours readers or favours writers, and either choice can starve the other side.

## reader and writer access rule

The shared object is a database, a file, or any structure several processes reach at once. A reader only reads, and a writer reads and updates. The rule admits any number of readers with no writer, or one writer with no readers.

Readers never conflict: neither changes what the other sees. A writer conflicts with every reader and with every other writer. An update overlapping a read would show half-changed data, and two overlapping updates would leave the object in a state neither writer intended.

---

Flashcards for this section are as follows:

- what the readers-writers rule allows at one moment ::@:: Any number of readers and no writer, or one writer and no reader.
- what a reader process does ::@:: It only reads the shared data set and changes nothing.
- what a writer process does ::@:: It reads the shared data set and also updates it.
- why two readers never conflict ::@:: Neither one changes the data, so each sees the same contents whether or not the other is inside.
- why a reader conflicts with a writer ::@:: The reader could see half an update, and the update could land while the reader still reads the old contents.
- why two writers conflict on the shared data set ::@:: Both update the data set, so overlapping updates leave it in a state that neither writer intended.
- what the access rule leaves undecided ::@:: Which side waits when both want the data set. The rule fixes who may be inside together, not who goes first.

## semaphore initialisation

Each solution guards its shared state with `sem_t` objects, unnamed POSIX semaphores that every call takes by address. `sem_init` fills one in.

```c
#include <semaphore.h>

int sem_init(sem_t *sem, int pshared, unsigned int value);
```

The second argument is the sharing flag. Zero keeps the semaphore among the threads of one process; a non-zero value shares it between processes, and then it must sit in shared memory.

The count is the third argument, and it decides the role. One makes a lock: the first `sem_wait` takes the count to zero and passes, and the next caller blocks until a `sem_post` raises it again. Zero makes a waiting signal: a caller blocks at once and proceeds only when another thread posts.

The call returns 0, or −1 with `errno` set. `sem_destroy` frees the semaphore once no thread holds or waits on it.

---

Flashcards for this section are as follows:

- type behind the semaphores in the readers-writers solutions, and the call that fills one in ::@:: `sem_t`, filled by `sem_init()`, with every operation taking its address.
- prototype of `sem_init()`, and the call the reader-preference solution makes ::@:: `int sem_init(sem_t *sem, int pshared, unsigned int value)`, called as `sem_init(&read_mutex, 0, 1)`: `&read_mutex` guards the reader count, `pshared` `0` keeps it inside this process, and `value` `1` makes it a lock; every semaphore here starts at one for the same reason.
- what the third argument of `sem_init()` sets ::@:: The initial count: one makes the semaphore a lock, and zero makes it a waiting signal.
- what the second argument of `sem_init()` selects in these solutions ::@:: 0 for the threads of one process, and a non-zero value to share the semaphore between processes, which then needs it in shared memory.
- call that frees a POSIX semaphore, and when it is safe ::@:: `sem_destroy()`, once no thread holds or waits on the semaphore.

## reader-preference solution

This solution favours readers: no reader waits unless a writer already holds the data set. `read_count` counts the readers inside, `read_mutex` guards that count, and `data_gate` guards the data set. Both semaphores start at one and the count at zero.

---

Flashcards for this section are as follows:

- shared state of the reader-preference solution ::@:: `read_count` starting at zero, `read_mutex` at one guarding the count, and `data_gate` at one guarding the data set.

### count-guarded reader access

A reader takes `read_mutex` only long enough to raise the count. The first reader through takes `data_gate` as well, which keeps every writer out while a reader is inside. The last reader out releases `data_gate`. Readers in between never touch it, which is why they enter without queueing behind one another.

```c
/* wait() and signal() are the semaphore operations sem_wait() and sem_post(). */
sem_t read_mutex;   /* guards read_count, initialised to 1 */
sem_t data_gate;    /* guards the data set, initialised to 1 */
int read_count = 0;

void init(void)
{
    sem_init(&read_mutex, 0, 1);
    sem_init(&data_gate, 0, 1);
}

/* a reader */
while (1) {
    wait(&read_mutex);
    read_count++;
    if (read_count == 1)
        wait(&data_gate);    /* first reader in takes the data set */
    signal(&read_mutex);

    /* read the data set */

    wait(&read_mutex);
    read_count--;
    if (read_count == 0)
        signal(&data_gate);  /* last reader out releases it */
    signal(&read_mutex);
}
```

A reader that arrives while a writer holds the data set blocks on `data_gate`, still holding `read_mutex`. Every reader behind it then queues on `read_mutex` until that first one gets through.

---

Flashcards for this section are as follows:

- what the first reader does in the reader-preference solution ::@:: It holds `read_mutex`, raises `read_count` to one, and then waits on `data_gate` before reading, so no writer is inside.
- what later readers take in the reader-preference solution ::@:: Only `read_mutex`, and only long enough to raise the count, so they enter while the first reader holds `data_gate`.
- what the last reader out does in the reader-preference solution ::@:: It lowers `read_count`, and at zero it signals `data_gate`, which lets a waiting writer enter.
- where readers queue while a writer holds the data set in the reader-preference solution ::@:: On `read_mutex`. The first arriving reader blocks on `data_gate` while holding `read_mutex`, so the readers behind it wait there.

### data gate as writer lock

A writer holds `data_gate` for its whole update. The gate is a semaphore used as a plain lock, and it excludes readers and writers alike.

```c
/* a writer */
while (1) {
    wait(&data_gate);
    /* write the data set */
    signal(&data_gate);
}
```

---

Flashcards for this section are as follows:

- what a writer does in the reader-preference solution ::@:: It waits on `data_gate`, updates the data set, and signals `data_gate`, one semaphore that excludes readers and other writers alike.

### starvation of writers

Readers arrive faster than they leave, so `read_count` never falls to zero and `data_gate` is never released. A writer that queues then waits for as long as readers keep arriving. The data stays as old as the last writer that got in.

---

Flashcards for this section are as follows:

- why the reader-preference solution favours readers ::@:: A reader enters whenever no writer holds the data set and never waits for another reader, so a writer waits behind a stream of arriving readers.
- why a writer starves in the reader-preference solution ::@:: Readers keep arriving, so `read_count` never returns to zero, `data_gate` is never released, and the writer waits without a bound.

### comparison with the writer-preference solution

The writer-preference solution keeps this skeleton and adds two objects: a count of waiting writers behind its own guard, and a gate every reader passes. Here the reader never touches that gate, and shutting it is what turns the favour round.

---

Flashcards for this section are as follows:

- what the writer-preference solution adds to the reader-preference skeleton ::@:: A count of waiting writers behind `write_mutex`, and `readers_gate`, which every reader passes and the first waiting writer shuts.

## writer-preference solution

This solution favours writers: once a writer is waiting, no new reader starts, and that writer enters as soon as the readers already inside have left. `read_count`, `read_mutex` and `data_gate` work as before; `write_count` counts the writers waiting or inside, `write_mutex` guards it, and `readers_gate` holds readers out.

```c
sem_t read_mutex;        /* guards read_count, initialised to 1 */
sem_t data_gate;         /* guards the data set, initialised to 1 */
sem_t write_mutex;       /* guards write_count, initialised to 1 */
sem_t readers_gate;      /* shuts readers out while a writer waits, initialised to 1 */
int read_count = 0;
int write_count = 0;

void init(void)
{
    sem_init(&read_mutex, 0, 1);
    sem_init(&data_gate, 0, 1);
    sem_init(&write_mutex, 0, 1);
    sem_init(&readers_gate, 0, 1);
}
```

---

Flashcards for this section are as follows:

- rule of the writer-preference solution ::@:: Once a writer is waiting, no new reader starts, and that writer gets the data set as soon as the readers already inside have left.
- shared state of the writer-preference solution ::@:: `read_count` and `read_mutex` as before, `data_gate` for the data set, `write_count` behind `write_mutex`, and `readers_gate` that every reader passes.

### gated reader access

A reader passes `readers_gate`, then raises `read_count` under `read_mutex` and takes `data_gate` if it is the first one inside. It reopens `readers_gate` for the next reader. The gate shuts only while a writer is queued, so at any other time readers pass through without stopping.

```c
/* a reader */
while (1) {
    wait(&readers_gate);      /* waits here while a writer is queued */
    wait(&read_mutex);
    read_count++;
    if (read_count == 1)
        wait(&data_gate);     /* first reader in takes the data set */
    signal(&read_mutex);
    signal(&readers_gate);    /* lets the next reader through */

    /* read the data set */

    wait(&read_mutex);
    read_count--;
    if (read_count == 0)
        signal(&data_gate);   /* last reader out releases it */
    signal(&read_mutex);
}
```

---

Flashcards for this section are as follows:

- what a reader passes to enter in the writer-preference solution ::@:: `readers_gate`, then `read_mutex` to raise `read_count`, then `data_gate` if it is the first reader inside.
- why a reader reopens `readers_gate` right after raising the count ::@:: So the next reader can pass instead of queueing behind a reader that is only changing the count. The gate shuts again only for a queued writer.

### gate shutdown by a writer

A writer works in three stages. It raises `write_count` under `write_mutex` and shuts `readers_gate` if it is the first to queue, then waits on `data_gate` for the readers inside to leave, and at the end lowers the count and reopens the gate if it is the last to finish. Readers already inside finish their work, since shutting the gate stops new ones without disturbing their count.

```c
/* a writer */
while (1) {
    wait(&write_mutex);
    write_count++;
    if (write_count == 1)
        wait(&readers_gate);  /* first waiting writer shuts the gate */
    signal(&write_mutex);

    wait(&data_gate);         /* waits for the readers inside to leave */
    /* write the data set */
    signal(&data_gate);

    wait(&write_mutex);
    write_count--;
    if (write_count == 0)
        signal(&readers_gate); /* last writer out reopens the gate */
    signal(&write_mutex);
}
```

---

Flashcards for this section are as follows:

- what the first waiting writer does in the writer-preference solution ::@:: It raises `write_count` under `write_mutex` and takes `readers_gate`, so no new reader starts while it waits.
- where a writer waits for the readers inside to leave ::@:: On `data_gate`, taken after it has shut `readers_gate`, so the readers already inside finish and no new one joins them.
- what the last writer out does in the writer-preference solution ::@:: It lowers `write_count`, and at zero it signals `readers_gate`, which lets readers start again.
- why the first writer shuts `readers_gate` before it waits on `data_gate` ::@:: So the readers inside drain without new ones joining, and the writer reaches the data set once instead of waiting behind an unbroken stream.

### starvation of readers

Writers arrive faster than they leave, so `write_count` never returns to zero and `readers_gate` stays shut. Readers then wait for as long as writers keep arriving, and the writers hand the data set among themselves. A stream of writers is enough on its own, because only the writer that finds no other writer left reopens the gate.

---

Flashcards for this section are as follows:

- why the writer-preference solution favours writers ::@:: A waiting writer shuts `readers_gate`, so readers that arrive after it wait although no reader conflicts with them.
- who starves in the writer-preference solution ::@:: Readers. Writers keep arriving, so `write_count` never returns to zero and `readers_gate` stays shut.

### comparison with the reader-preference solution

The extra state moves where readers wait. Here they queue on `readers_gate` before touching any count; in the reader-preference solution they queue on `read_mutex` behind a reader blocked on the data set. Each solution admits one side without limit, and the side that keeps arriving keeps the data set.

---

Flashcards for this section are as follows:

- how the two solutions differ in where readers wait ::@:: In the reader-preference solution they wait on `read_mutex` behind a reader blocked on the data set, and in the writer-preference solution on `readers_gate` before touching any count.
- what stays the same in both readers-writers solutions ::@:: The first reader takes `data_gate`, the last reader releases it, and a writer needs only `data_gate` to reach the data set.

## reader-writer lock

A reader-writer lock packs the rule into one object, and acquiring it names a mode. Read mode gives shared access, so any number of processes hold the lock at once; write mode gives exclusive access, so its holder excludes every reader.

The gain over a semaphore used as a plain lock is that readers hold the lock together instead of queueing one at a time. That pays for data read often and written rarely, and for code sections long enough that the contention shows.

The lock is harder to build than a semaphore or a mutex, because it counts the readers, notes whether a writer waits, and applies a policy such as reader priority or writer priority. A kernel takes on that build only for the structures that repay it.

---

Flashcards for this section are as follows:

- reader-writer lock ::@:: A lock acquired in a named mode: read mode admits any number of holders, and write mode admits one holder and excludes every reader.
- what a reader-writer lock gains over a semaphore ::@:: Readers hold it together, where a semaphore used as a plain lock would make them queue one at a time.
- cost of a reader-writer lock ::@:: It is harder to build than a semaphore or a mutex, since it counts readers, notes a waiting writer, and applies a priority policy.
- when a kernel chooses a reader-writer lock ::@:: For data read often and written rarely, and for code sections long enough that reader concurrency repays the extra cost.
