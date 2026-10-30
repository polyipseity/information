---
aliases:
  - bounded buffer problem
  - bounded-buffer problem
  - producer-consumer problem
  - producer–consumer problem
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/producer–consumer_problem
  - language/in/English
---

# producer–consumer problem

Two processes share a buffer of fixed size. One stores items; the other takes them. A full buffer stops the producer, an empty one stops the consumer.

Two rules hold: no item may be overwritten before it is taken, and none may be taken before it is stored. A pipe, a message queue and a print spooler work this way.

The buffer is small enough to trace by hand, and every failure a synchronization tool must prevent appears in it: a lost update, a write into a full buffer, a read from an empty one, and two processes waiting forever.

---

Flashcards for this section are as follows:

- what the producer-consumer problem asks of two processes ::@:: One process stores items into a fixed-size buffer while the other takes them, and neither loses nor invents an item while both make progress.
- what makes a bounded buffer harder than an unlimited one ::@:: It runs out of room and of items: the producer waits when every slot is full, the consumer when none is, so each must know the other's state.
- why the producer-consumer problem is a good test of a synchronization tool ::@:: It needs mutual exclusion on the buffer and ordering between the store and the take, so a tool supplying only one fails.
- what everyday systems have the producer-consumer shape ::@:: A pipe, a message queue and a print spooler.

## problem statement

The buffer is $n$ slots of one item each. The producer creates an item, waits for a free slot, then stores it; the consumer waits for a filled slot, removes the item and uses it. Storing into an occupied slot destroys an item not yet taken; taking from a free slot reads what was never written.

Both also share the bookkeeping: the slots, the write index, the read index and a count of stored items. The critical sections come from there.

---

Flashcards for this section are as follows:

- what a bounded buffer holds ::@:: A fixed number n of slots, each holding at most one item.
- what the producer does in the producer-consumer problem ::@:: It creates an item, waits for a free slot, then stores it there.
- what the consumer does in the producer-consumer problem ::@:: It waits for a filled slot, removes the item, then uses it.
- the condition that limits the producer ::@:: It stores only into a free slot, so it never overwrites an item not yet taken.
- the condition that limits the consumer ::@:: It takes only from a filled slot, so it never reads what was never written.
- what the two processes share besides the slots ::@:: The write index, the read index, and the count of stored items.

## attempt with a shared counter

A first attempt uses one integer `counter`, the number of occupied slots, starting at 0. The producer stores an item then increments it; the consumer removes one then decrements it. The producer loops while `counter == n`, the consumer while `counter == 0`.

The increment takes three machine steps: load the counter into a register, add one, store it back. The decrement does the same with a subtraction.

With 5 items stored, the producer loads 5 and computes 6, the consumer loads 5 before that store lands and computes 4. Whichever store lands last decides the count, so one update disappears; the true count is 5.

Either wrong value misleads a decision. At 4 the producer sees room that is not there and overwrites an item; at 6 the consumer sees an item that is not and takes whatever the slot holds. The test is sound, the value is not.

---

Flashcards for this section are as follows:

- what `counter` counts in the shared-counter attempt and what it starts at ::@:: The number of occupied slots in the buffer, starting at 0.
- the three machine steps behind `counter++` ::@:: Load the counter into a register, add one, store it back.
- how the shared counter loses an update with 5 items stored ::@:: The producer and the consumer both load 5 before either stores, one computes 6, the other 4, and whichever store lands second overwrites the first.
- what the shared counter holds after one store and one take that both start from 5 ::@:: 4 if the consumer's store lands last, or 6 if the producer's does. The true count is 5.
- why a count of 4 with 5 items stored breaks the buffer ::@:: The producer trusts the count, believes a slot is free, and overwrites an item not yet taken.
- why a count of 6 with 5 items stored breaks the buffer ::@:: The consumer trusts the count, believes an item is stored, and reads a slot never written.
- what has to become atomic in the counter attempt ::@:: The whole read-modify-write of the count: one process finishes all three steps before the other starts.
- the order in which the shared-counter attempt changes the buffer and the count ::@:: The producer stores, then increments `counter`; the consumer removes, then decrements `counter`.
- the test that stops each process in the shared-counter attempt ::@:: The producer loops while `counter == n`, where n is the number of slots, and the consumer loops while `counter == 0`.

## semaphore and condition-variable solutions

### mutex with two counting semaphores

Three [semaphores](semaphore%20(programming).md) do the work. `mutex` starts at 1 and guards the buffer and its indices; `empty` starts at $n$ and counts free slots; `full` starts at 0 and counts stored items.

The producer waits on `empty` then `mutex`, stores its item, and signals `mutex` then `full`. The consumer waits on `full` then `mutex`, removes an item, and signals `mutex` then `empty`.

A producer that took `mutex` first and found `empty` at 0 would hold `mutex` while waiting. The consumer could never take `mutex` to remove an item, `empty` would never rise, and both would wait forever. So the counting semaphore goes first, the mutex second.

Keep the critical section as small as the shared update: whatever the mutex covers, the other process cannot pass through, so a long section costs more than a short wait. The item is created before the lock and used after the unlock, so the mutex covers only the store or the take. Both counting semaphore waits happen outside it, and the post follows the unlock. The counts also check a trace: `empty` plus `full` is always $n$.

```c
#include <semaphore.h>

#define N 8          /* slots in the buffer */
typedef int item;

sem_t mutex;   /* guards the buffer and its indices */
sem_t empty;   /* counts free slots */
sem_t full;    /* counts stored items */

static item buffer[N];
static int in = 0, out = 0;

void init(void)
{
    sem_init(&mutex, 0, 1);
    sem_init(&empty, 0, N);
    sem_init(&full, 0, 0);
}

void *producer(void *arg)
{
    while (1) {
        item next = produce();
        sem_wait(&empty);        /* a free slot must exist first */
        sem_wait(&mutex);
        buffer[in] = next;
        in = (in + 1) % N;
        sem_post(&mutex);
        sem_post(&full);
    }
}

void *consumer(void *arg)
{
    while (1) {
        sem_wait(&full);         /* a stored item must exist first */
        sem_wait(&mutex);
        item next = buffer[out];
        out = (out + 1) % N;
        sem_post(&mutex);
        sem_post(&empty);
        consume(next);
    }
}
```

Each misplacement fails differently. A mutex taken before `empty` or `full` holds the lock while waiting: the other process never reaches the buffer, the count it would raise never rises, and both wait forever. Skip `sem_post(&mutex)` on one path and the other blocks on a lock nobody releases, a hang with nothing wrong in the buffer. Match a wait to the wrong post and the counts drift, so one side waits for a slot or an item the other never supplies; starting `empty` at 0 does the same. Posting `full` before `mutex` is the mild case: the consumer wakes only to block, a round spent for nothing.

---

Flashcards for this section are as follows:

- prototype of `sem_init()`, and the call that fills the free-slot count ::@:: `int sem_init(sem_t *sem, int pshared, unsigned int value)`, called as `sem_init(&empty, 0, N)`: `&empty` counts free slots, `pshared` `0` keeps it inside this process, `value` `N` is the slot count, and a producer blocks once every slot is full.
- prototype of `sem_wait()`, and the call the producer makes ::@:: `int sem_wait(sem_t *sem)`, called as `sem_wait(&empty)`: takes a free slot and waits while the buffer is full.
- prototype of `sem_post()`, and the call the consumer makes ::@:: `int sem_post(sem_t *sem)`, called as `sem_post(&full)`: raises the stored-item count and wakes a waiting consumer.
- prototype of `pthread_mutex_lock()` in the condition-variable solution, and the call around the change ::@:: `int pthread_mutex_lock(pthread_mutex_t *mutex)`, called as `pthread_mutex_lock(&mutex)`: takes the lock before either side reads or changes `count`.
- prototype of `pthread_mutex_unlock()` in the condition-variable solution, and the call that ends the section ::@:: `int pthread_mutex_unlock(pthread_mutex_t *mutex)`, called as `pthread_mutex_unlock(&mutex)`: releases the lock once the change to `count` is made.
- the initial values of the three semaphores in this solution ::@:: `mutex` at 1, `empty` at n, `full` at 0.
- what the producer waits on, in order ::@:: `empty` first, then `mutex`. After storing it signals `mutex` and then `full`.
- what the consumer waits on, in order ::@:: `full` first, then `mutex`. After taking it signals `mutex` and then `empty`.
- what `empty`, `full` and `mutex` each count ::@:: `empty` counts free slots, `full` counts stored items, and `mutex` admits one process at a time into the buffer.
- why the producer takes `empty` before `mutex` ::@:: Holding `mutex` while waiting for `empty` would stop the consumer from removing an item, so `empty` never rises and both wait forever.
- why the consumer takes `full` before `mutex` ::@:: Holding `mutex` while waiting for `full` would stop the producer from storing, so `full` never rises and both wait forever.
- how much of the work the mutex covers in the semaphore solution ::@:: Only the store into the buffer or the take from it, never the item's creation or use.
- where the mutex goes in the semaphore solution ::@:: Keep the critical section as small as the shared update: the other process cannot pass through whatever the mutex covers. Create the item and use it outside the lock.
- why both counting semaphore waits sit outside the mutex ::@:: They carry the ordering. Waiting for either one under the mutex would hold the lock while waiting for the other process to act.
- why `full` is posted after `sem_post(&mutex)` ::@:: Posting first wakes the consumer while the mutex is still held, so it wakes only to block again. The later post costs nothing.
- what the two counts tell you about a bounded buffer of $n$ slots ::@:: `empty` and `full` always sum to $n$; a trace where they do not has already lost a signal.
- how a missing `sem_post(&mutex)` shows up in the semaphore solution ::@:: The other process blocks on `mutex` forever, so the program hangs with no buffer state to explain it.
- how a wait matched to the wrong post shows up in a buffer of $n$ slots ::@:: The counts drift, `empty` and `full` stop summing to $n$, and one side waits forever for a slot or an item the other never supplies.
- why starting `empty` at 0 hangs the semaphore solution ::@:: The producer waits for a free slot that only the consumer can create, while the consumer waits for an item only the producer can store.

### mutex with conditional waiting

A mutex and two condition variables replace the counting semaphores. The consumer signals `not_full` when it frees a slot, the producer `not_empty` when it stores an item, and the indices `in` and `out` walk a circular array.

With only those two indices, `in == out` means the buffer is empty, but a full buffer would make them equal as well. So this version stores at most $n-1$ items and keeps one slot free. The consumer reads `in == out` as empty, the producer `(in + 1) % n == out` as full.

The producer locks the mutex, waits on `not_full` while the buffer is full, stores, advances `in`, signals `not_empty`, and unlocks. The consumer mirrors it with `not_empty`, `out` and `not_full`: it waits while the buffer is empty, removes an item, advances `out`, signals, unlocks.

The wait sits in a `while`; an `if` would be wrong. A woken thread re-acquires the mutex, and another thread may have taken the slot meantime, so the test runs again. While it waits the thread sleeps instead of holding a processor.

```c
#include <pthread.h>

#define N 8
typedef int item;

static item buffer[N];
static int in = 0, out = 0;
static pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
static pthread_cond_t not_full = PTHREAD_COND_INITIALIZER;
static pthread_cond_t not_empty = PTHREAD_COND_INITIALIZER;

void *producer(void *arg)
{
    while (1) {
        item next = produce();
        pthread_mutex_lock(&mutex);
        while ((in + 1) % N == out)          /* one slot stays free */
            pthread_cond_wait(&not_full, &mutex);
        buffer[in] = next;
        in = (in + 1) % N;
        pthread_cond_signal(&not_empty);
        pthread_mutex_unlock(&mutex);
    }
}

void *consumer(void *arg)
{
    while (1) {
        pthread_mutex_lock(&mutex);
        while (in == out)                    /* nothing stored */
            pthread_cond_wait(&not_empty, &mutex);
        item next = buffer[out];
        out = (out + 1) % N;
        pthread_cond_signal(&not_full);
        pthread_mutex_unlock(&mutex);
        consume(next);
    }
}
```

POSIX fixes where the two calls stand. `pthread_cond_wait` must be called with the mutex held; it releases the mutex while the thread sleeps and re-acquires it before returning, release and sleep forming one atomic step. `pthread_cond_signal` may be called with or without the mutex, and it does not release one the caller holds.

Signalling while holding the mutex costs a scheduling round: the woken thread becomes runnable, finds the mutex still held, and blocks again. That is hurry-up-and-wait. Signalling after the unlock avoids it, because the waiter can take the mutex at once. Some implementations repair the inside-the-lock case with wait morphing, handing the waiter straight from the condition variable onto the mutex's wait queue, so it does not run until the mutex is free. glibc's earlier native threads library did this with a futex requeue; a library without it pays the round.

Both placements are safe here. The indices change only under the mutex, and every waiter re-tests its predicate in a `while`, so a signal sent while nobody waits does no harm: the next test sees the change. A wake is lost when a signaller changes the predicate outside the mutex, or a waiter tests once with `if`: the signal lands between the test and the sleep, no waiter takes it, and the thread sleeps through a promised change.

---

Flashcards for this section are as follows:

- what this solution uses to track the buffer ::@:: A mutex, the condition variables `not_full` and `not_empty`, and the indices `in` and `out` in a circular array.
- why this version keeps one slot free ::@:: Equal indices mean the buffer is empty, and a full buffer would make them equal too, so storing at most n-1 items holds the two states apart.
- the test for a full buffer in the mutex and condition-variable solution ::@:: `(in + 1) % n == out`. One slot stays free, so a full buffer cannot look empty.
- why the wait sits in a `while` rather than an `if` ::@:: A wake does not promise the condition still holds: another thread can take the slot before this one gets the mutex back, so the test repeats after every wake.
- what the producer signals and when ::@:: It signals `not_empty` after storing an item. Either placement is correct, since the index changed under the mutex and the consumer re-tests in a loop.
- POSIX rule about `pthread_cond_wait` and its mutex ::@:: The mutex must be held when the call is made. The call releases it while the thread sleeps and re-acquires it on return, atomically with the sleep.
- POSIX rule about `pthread_cond_signal` and the mutex ::@:: It may be called with or without the mutex, and it does not release a mutex that the caller holds.
- cost of signalling with the mutex held, and why signalling after the unlock avoids it ::@:: The woken thread runs, finds the mutex still held, and blocks again, so a wake and a sleep are spent with no work between them. After the unlock the waiter finds the mutex free and continues.
- what wait morphing does ::@:: It hands a waiter straight from the condition variable onto the mutex's wait queue while the signaller still holds the mutex, so the waiter does not wake only to block again. glibc's earlier native threads library did it with a futex requeue.
- why signalling after the unlock is still correct in this buffer ::@:: The indices change under the mutex and the waiter re-tests in a `while`, so a signal sent while nobody waits leaves a state the next test sees.
- when a signal from outside the mutex is lost ::@:: When the predicate changes outside the mutex, or the waiter tests it once with `if`. The signal lands between the test and the sleep and no waiter takes it.
- what the consumer signals and when ::@:: It signals `not_full` after removing an item, under the mutex or after the unlock, since `out` changed under the mutex and the producer re-tests in a loop.
- prototype of `pthread_cond_wait()`, and the call the producer waits with ::@:: `int pthread_cond_wait(pthread_cond_t *cond, pthread_mutex_t *mutex)`, called as `pthread_cond_wait(&not_full, &mutex)`: `cond` is the condition to sleep on and `mutex` the lock the caller holds, which the call releases and re-takes; it returns once a slot frees.
- prototype of `pthread_cond_signal()`, and the call that wakes a consumer ::@:: `int pthread_cond_signal(pthread_cond_t *cond)`, called as `pthread_cond_signal(&not_empty)`: wakes one consumer waiting for an item, which is enough because one item appeared.
- what a condition variable buys over spinning on the count ::@:: The waiting thread sleeps, so it holds no processor; it wakes when a signal reports the state may have changed.

## unbounded buffer variant

With no limit on the buffer size, the producer never waits for room. `empty` disappears and only the consumer can block. A linked list replaces the circular array, so the index arithmetic goes too: emptiness is `head == NULL`, and there is no full state to test.

The bounded version's discipline carries over. The node is allocated before the mutex is taken, because `malloc` may block or take a lock of its own. Linking happens under the mutex, the consumer still takes `full` before `mutex`, and both posts follow the unlock.

```c
#include <semaphore.h>
#include <stdlib.h>

typedef int item;

struct node {
    item value;
    struct node *next;
};

static struct node *head = NULL;   /* oldest stored item */
static struct node *tail = NULL;   /* where the next item is linked */

static sem_t mutex;                /* guards head and tail */
static sem_t full;                 /* counts stored items */

void init(void)
{
    sem_init(&mutex, 0, 1);
    sem_init(&full, 0, 0);
}

void *producer(void *arg)
{
    while (1) {
        item next = produce();
        struct node *slot = malloc(sizeof *slot);   /* outside the lock */
        if (slot == NULL)
            abort();                                /* no bound to stop it first */
        slot->value = next;
        slot->next = NULL;
        sem_wait(&mutex);                           /* no empty to wait on */
        if (tail == NULL)
            head = tail = slot;
        else {
            tail->next = slot;
            tail = slot;
        }
        sem_post(&mutex);
        sem_post(&full);                            /* after the unlock */
    }
}

void *consumer(void *arg)
{
    while (1) {
        sem_wait(&full);                            /* order still matters */
        sem_wait(&mutex);
        struct node *slot = head;
        item next = slot->value;
        head = slot->next;
        if (head == NULL)
            tail = NULL;
        sem_post(&mutex);
        free(slot);                                 /* outside the lock */
        consume(next);
    }
}
```

Three differences go beyond the missing semaphore. The wait order still decides whether the program can hang: a consumer that took `mutex` first would wait for `full` while holding the only lock the producer needs. Allocation and freeing bring a second: with `malloc` or `free` inside the critical section, the allocator's lock is taken under `mutex`, and a thread holding it while waiting for `mutex` closes a cycle the buffer no longer offers. The third is growth: a producer faster than the consumer eats memory without bound, so the machine runs out where the bounded version would have blocked.

The condition-variable form loses the same parts. One condition variable, `not_empty`, covers the only wait; `not_full`, the free-slot arithmetic and the reserved slot go with the array, and the consumer waits with `while (head == NULL)`. The producer locks, links, signals and unlocks; the allocator rule and the wait order carry over unchanged.

---

Flashcards for this section are as follows:

- why only the consumer blocks with an unbounded buffer ::@:: There is always room for another item, so only the consumer finds nothing to take.
- what the unbounded variant drops and what replaces the array ::@:: `empty` goes; a linked list replaces the circular array, so `head` and `tail` replace the indices and emptiness is `head == NULL`.
- why the unbounded producer allocates its node before taking the mutex ::@:: `malloc` may block or take the allocator's lock, so holding `mutex` through the allocation sets up an opposite order between the two locks.
- deadlock that disappears in the unbounded variant ::@:: The producer never waits for room, so it cannot hold `mutex` while waiting for a slot.
- deadlock opportunity that survives in the unbounded variant ::@:: Allocating or freeing inside the critical section takes the allocator's lock under `mutex`, which another thread may take in the opposite order.
- failure that replaces waiting in the unbounded variant ::@:: Unbounded growth: a producer faster than the consumer consumes memory until the machine runs out, where a bounded buffer would have blocked.
- what the unbounded consumer still waits on, and in what order ::@:: `full` first, then `mutex`. Holding `mutex` while waiting for an item would stop the producer from linking one.
- how the condition-variable form of the unbounded buffer differs ::@:: One condition variable, `not_empty`, with `while (head == NULL)`. The full test, the free-slot arithmetic and the reserved slot go with the array.
