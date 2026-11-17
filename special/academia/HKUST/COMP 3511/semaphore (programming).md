---
aliases:
  - binary semaphore
  - counting semaphore
  - semaphore
  - semaphore (programming)
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/semaphore_(programming)
  - language/in/English
---

# semaphore (programming)

A semaphore is an integer that only `wait()` and `signal()` change, each atomically. The same integer can act as a lock, count the free copies of a resource, or carry a signal from one process to another.

Edsger Dijkstra defined it in the late 1960s; early UNIX used it as its main synchronization primitive.

How semaphores drive a bounded buffer is in [producer-consumer problem](producer–consumer%20problem.md).

---

Flashcards for this section are as follows:

- what a semaphore's value is and what may change it ::@:: An integer that only `wait()` and `signal()` change, each atomically.
- how a mutex lock relates to a semaphore ::@:: A mutex lock is a semaphore held between 0 and 1, admitting one process at a time.
- who defined the semaphore and when ::@:: Edsger Dijkstra, in the late 1960s.
- what role the semaphore played in early UNIX ::@:: The semaphore was early UNIX's main synchronization primitive.

## operations

`wait(S)` and `signal(S)` are atomic: no two processes run either on one semaphore at once. Otherwise two processes could both read 1 and both write back 0, losing a permit the way a shared counter loses an update.

In its busy-waiting form, `wait(S)` spins while the value is not positive, then lowers it by one and returns. `signal(S)` raises the value by one. A process that meets a semaphore at 0 waits for a signal before it can pass.

The original names are $P$ and $V$, from the Dutch "proberen", to test, and "verhogen", to increment; some textbooks still use them.

---

Flashcards for this section are as follows:

- what `wait` does to a semaphore's value ::@:: Blocks while the value is not positive, otherwise lowering it by one.
- what `signal` does to a semaphore's value ::@:: Raises the value by one, which may let one waiting process through.
- why `wait` and `signal` must be atomic on one semaphore ::@:: Two processes could both read 1 and both write back 0, losing a permit the way a shared counter loses an update.
- what the letters P and V stand for in the original semaphore operations ::@:: P is for the Dutch "proberen", to test, and V is for "verhogen", to increment.
- what a process does when it waits on a semaphore holding 0 ::@:: Spins or sleeps inside the implementation until another process signals.

### semaphore calls

POSIX names the pair `sem_wait` and `sem_post`, and adds calls to create and destroy the semaphore:

```c
#include <semaphore.h>

int sem_init(sem_t *sem, int pshared, unsigned int value);  /* 0, or -1 with errno */
int sem_wait(sem_t *sem);                                   /* 0, or -1 with errno */
int sem_post(sem_t *sem);                                   /* 0, or -1 with errno */
int sem_destroy(sem_t *sem);                                /* 0, or -1 with errno */
```

`sem_init` takes three arguments. `sem` is the semaphore the caller declared. `pshared` is `0` when threads of one process share it, nonzero when separate processes do, and that case needs it in shared memory. `value` is the starting count: `1` makes a lock, `0` makes a gate whose first waiter blocks until someone posts, and a larger number admits that many callers at once.

---

Flashcards for this section are as follows:

- POSIX names for the wait and signal operations on a semaphore ::@:: `sem_wait` and `sem_post`.
- signature of `sem_init()`, and the call that makes the lock ::@:: `int sem_init(sem_t *sem, int pshared, unsigned int value)`, called as `sem_init(&synch, 0, 0)`: `&synch` names the semaphore, `0` keeps it inside this process, and a count of `0` blocks the first `sem_wait` until the other side posts. Returns `0`, or `-1` with `errno` set.
- values the pshared argument of `sem_init()` takes ::@:: `0` for threads of one process, or nonzero for processes sharing it, which then has to live in shared memory.
- starting values `sem_init()` accepts, and what each makes ::@:: `1` a lock, `0` a gate whose first waiter blocks until a post, and a larger count one that admits that many callers at once.
- signature of `sem_wait()`, and the call that takes the permit ::@:: `int sem_wait(sem_t *sem)`, called as `sem_wait(&mutex)`: takes the single permit, waits while another thread holds it, and returns `0`, or `-1` with `errno` set, including `EINTR` when a signal interrupts the wait.
- signature of `sem_post()`, and the call that returns the permit ::@:: `int sem_post(sem_t *sem)`, called as `sem_post(&synch)`: raises the count by one, wakes the thread waiting on it, and returns `0`, or `-1` with `errno` set.
- signature of `sem_destroy()`, and where the listing calls it ::@:: `int sem_destroy(sem_t *sem)`, called as `sem_destroy(&mutex)`: frees the semaphore once no thread waits on it and returns `0`, or `-1` with `errno` set.
- signature of `pthread_create()`, and the call that starts the two threads ::@:: `int pthread_create(pthread_t *tid, const pthread_attr_t *attr, void *(*start_routine)(void *), void *arg)`, called as `pthread_create(&t1, NULL, first, NULL)`: starts `first` with the default attributes and no argument.
- signature of `pthread_join()`, and the call that waits for both ::@:: `int pthread_join(pthread_t tid, void **ret)`, called as `pthread_join(t1, NULL)`: waits for that thread to end and discards its return value.

## semaphore kinds

### binary semaphore

A binary semaphore holds 0 or 1. Started at 1 it is a mutex lock: each process waits before its critical section and signals after, so one is inside at a time. Started at 0 it is a signal, and the first wait blocks until someone signals.

---

Flashcards for this section are as follows:

- what range a binary semaphore's value covers ::@:: 0 and 1 only.
- how a binary semaphore works as a mutex lock ::@:: Starts at 1, and each process waits before its critical section and signals after, so one is inside at a time.

### counting semaphore

A counting semaphore takes every non-negative integer and counts free copies of a resource. A pool of $n$ identical resources starts it at $n$; each user waits for a copy and signals when done, so the $(n+1)$-th wait blocks until one comes back.

---

Flashcards for this section are as follows:

- what a counting semaphore counts ::@:: The free copies of a resource, starting at the copy count; each user waits for one and signals it back when done.
- how many processes a counting semaphore started at $n$ admit at once ::@:: $n$ of them. Each wait takes one unit, so the next wait blocks until a copy is signalled back.
- what values a counting semaphore can take ::@:: Every non-negative integer, unlike a binary semaphore's 0 or 1.

### ordering use

Ordering needs a semaphore that starts at 0. Two processes share one, `synch`. The first runs S1, then signals; the second waits before S2. The wait cannot pass before the signal arrives, so S1 runs before S2 whichever process the scheduler starts, which is how a producer tells a consumer an item is ready.

```c
#include <pthread.h>
#include <semaphore.h>
#include <stddef.h>                /* NULL */

sem_t mutex;   /* mutual exclusion: starts at 1 */
sem_t synch;   /* ordering: starts at 0 */

void init(void)
{
    sem_init(&mutex, 0, 1);
    sem_init(&synch, 0, 0);
}

void *first(void *arg)
{
    sem_wait(&mutex);
    /* critical section */
    sem_post(&mutex);

    s1();
    sem_post(&synch);    /* tells the other process that s1 has run */
    return NULL;
}

void *second(void *arg)
{
    sem_wait(&synch);    /* cannot pass until s1 has run */
    s2();

    sem_wait(&mutex);
    /* critical section */
    sem_post(&mutex);
    return NULL;
}

int main(void)
{
    pthread_t t1, t2;
    init();                    /* sem_init fills both semaphores */
    pthread_create(&t1, NULL, first, NULL);
    pthread_create(&t2, NULL, second, NULL);
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    sem_destroy(&mutex);       /* legal only once no thread waits */
    return sem_destroy(&synch);
}
```

Here `sem_init` gets 0 as its second argument, keeping each semaphore inside one process. A nonzero value shares it between processes and needs it in shared memory.

---

Flashcards for this section are as follows:

- how a semaphore started at 0 orders two statements in two processes ::@:: The earlier process runs its statement and signals; the later process waits on the semaphore before its own statement and cannot pass until the signal.
- which initial value gives mutual exclusion and which gives ordering ::@:: 1 for mutual exclusion, so the first caller passes straight through; 0 for ordering, so the later process waits for the signal.

## blocking implementation

Busy waiting burns processor time for nothing, so the usual implementation queues waiting processes on the semaphore. `block()` suspends the caller and puts it on that queue; `wakeup(p)` removes the waiting process `p` and makes it ready to run.

`wait` lowers the value, then blocks and queues the caller if the value has gone negative. `signal` raises it, then wakes one queued process if the value is still at most zero. Both change the value before testing it; the busy-waiting version tested first.

A negative value records debt: its magnitude is the number of waiters. The busy-waiting version never falls below zero.

```c
struct semaphore {
    int value;
    struct process *list;   /* processes blocked on this semaphore */
};

void wait(struct semaphore *s)
{
    s->value--;
    if (s->value < 0) {
        add_to_list(s->list, current);
        block();            /* suspends the caller */
    }
}

void signal(struct semaphore *s)
{
    s->value++;
    if (s->value <= 0) {
        struct process *p = remove_from_list(s->list);
        wakeup(p);          /* moves p to the ready queue */
    }
}
```

---

Flashcards for this section are as follows:

- what a semaphore's waiting queue holds ::@:: The processes blocked on it, held as linked records.
- what `block` and `wakeup` do in a semaphore ::@:: `block` suspends the calling process and leaves it queued; `wakeup` takes one process off the queue and makes it ready to run.
- what a negative semaphore value means ::@:: Its magnitude is the number of processes waiting on that semaphore.
- why the blocking version changes the value before testing it ::@:: The value is permits minus waiters. A process that pushes it below zero has just become a waiter, and a signal leaving it at most zero must wake one.
- how the blocking version avoids busy waiting ::@:: A process that cannot proceed suspends itself and leaves the processor, so it spends no cycles waiting.
- why a busy-waiting semaphore's value never falls below zero ::@:: `wait` spins while the value is not positive, so it lowers the value only once positive.

## implementation with test-and-set

Both operations read the value and write it back, so those writes need a critical section. Each takes a spinlock built from `test_and_set`, changes the value and the queue, then releases. `test_and_set` writes into a word and returns what it held before, so exactly one of the processes racing for a lock sees the clear value; the rest see the mark.

The spinlock makes one operation indivisible against the other. It deliberately lets the value go negative: a `wait` that finds no permit records the debt before arranging the wait, so the negative value is the queue length.

A process suspends only after releasing the spinlock. One that blocked while holding it would leave every other user spinning on a lock that a sleeping process never releases.

---

Flashcards for this section are as follows:

- how a semaphore's operations are made atomic in software ::@:: Each one takes a spinlock built from `test_and_set` around the value and the waiting queue, makes its change, then releases.
- why a semaphore's value can be negative in this implementation ::@:: The value is lowered before the caller is queued, so it counts permits minus waiters.
- why a process must not block while holding the semaphore's own spinlock ::@:: Every other user would spin forever on a lock that a sleeping process never releases.

## pitfalls

Deadlock comes from taking two semaphores in opposite orders. Let `S` and `Q` both start at 1, with one process waiting on `S` then `Q` and the other on `Q` then `S`. If the first takes `S` and the second takes `Q`, each waits for a signal the other never sends, so the program stops though every wait is correct on its own.

Starvation is indefinite blocking: a process sits on a semaphore queue and is never chosen. Serve the most recent waiter first, or the one with the highest priority, and some process is passed over while others keep arriving.

A wrong initial value fails quietly. Started too high, a semaphore admits more processes than the resource allows, and exclusion is gone. Started too low, a permit was never there, so a process that should have passed blocks forever.

---

Flashcards for this section are as follows:

- how two semaphores deadlock two processes ::@:: If one process waits on `S` and then `Q` while the other waits on `Q` and then `S`, each can hold one semaphore and wait for the other's signal, and neither ever signals.
- what starvation means for a semaphore ::@:: A blocked process is never taken off the queue, so it waits forever while others keep taking the signal.
- how the queue order can starve a process ::@:: Taking the most recent waiter first, or the one with the highest priority, leaves a particular process behind however many signals arrive.
- what a wrong initial value does ::@:: Started too high it admits more processes than the resource allows, and started too low it withholds a permit, so a process that should pass blocks forever.
