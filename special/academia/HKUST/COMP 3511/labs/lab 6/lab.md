---
aliases:
  - COMP 3511 lab 6
  - HKUST COMP 3511 lab 6
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/labs/lab_6/lab
  - language/in/English
---

# lab

- HKUST COMP 3511 lab 6
- parent: [lab 6](index.md)

## race conditions and the critical section

A race condition is an answer that depends on timing: switch threads at the wrong moment and the result changes. Take `counter++`, which reads `counter`, adds one, writes the value back. Thread A reads 5 and loses the processor. B reads 5 and writes 6. A resumes and writes 6, so two increments leave the counter one larger.

The critical section is the code touching a shared variable or resource. A race can begin only there, so one thread at a time may run it.

---

Flashcards for this section are as follows:

- race condition ::@:: An answer that depends on timing, so a context switch at the wrong moment changes it.
- the three steps behind `counter++` ::@:: Read `counter` into a register, add one, write the value back.
- how two increments leave `counter` one larger ::@:: One thread reads 5, is switched out, the second reads 5 and writes 6, then the first resumes and writes 6.
- critical section ::@:: Code touching a shared variable or resource, which races unless one thread runs it at a time.

### atomicity

Atomic means all or nothing: the sequence happens at once, nothing interleaved. Some hardware has one instruction that reads, adds and writes, and `counter++` compiled to it cannot be split. On x86 that is `lock add`.

Hardware atomicity reaches only small units. No instruction updates a linked list or a thousand by thousand matrix in one step, so the system supplies synchronization primitives: some rest on hardware, some need help from the operating system.

---

Flashcards for this section are as follows:

- what atomic means for a sequence of actions ::@:: The sequence appears to happen at once, so nothing interleaves in the middle.
- how a hardware atomic instruction removes the race on `counter++` ::@:: One instruction reads, adds and writes without a split, so no other thread runs between them.
- why not every shared structure is made atomic by an instruction ::@:: A hardware instruction updates one small unit; no instruction updates a whole matrix or a linked list at once.
- what takes the place of hardware atomicity for a structure too large for one instruction ::@:: Synchronization primitives take their place: some rest on hardware support, some on the operating system.
- the x86 instruction that reads, adds and writes as one unsplittable step ::@:: `lock add`, the instruction a shared `counter++` rests on.

## critical-section solution requirements

Three requirements decide whether a solution works: one for safety, two for liveness. Liveness means the program keeps making progress, so a thread that keeps asking gets in eventually.

Mutual exclusion is the safety requirement: at most one thread sits inside the critical section at a time, so the race cannot give a wrong answer. A solution that admits nobody keeps it and makes no progress, so liveness must hold too.

Progress is the first liveness requirement: with the section empty and threads asking, one gets in without indefinite delay. Only threads that want in take part, so work elsewhere cannot hold them out.

Bounded waiting is the fairness requirement: once a thread asks to enter, a limit applies to how many others may get in ahead of it, so no thread starves while the rest keep circulating. Progress alone does not give this, since one thread may win every time. Two threads looping on `counter++`, with a scheduler that always picks the first, leave the second waiting forever: no answer comes out wrong, but its increments never happen.

---

Flashcards for this section are as follows:

- mutual exclusion as a critical-section requirement ::@:: At most one thread is inside the critical section at a time, so the race cannot give a wrong answer.
- progress as a critical-section requirement ::@:: With the critical section empty and threads wanting in, one gets in without indefinite delay.
- bounded waiting as a critical-section requirement ::@:: Once a thread asks to enter, a limit applies to how many others may enter before it.
- which critical-section requirement a solution that never lets anybody enter satisfies ::@:: Mutual exclusion alone; progress fails, so nobody ever gets in.
- what bounded waiting rules out, and what a failure of it costs ::@:: Starvation. The starved thread's increments never happen, so its work is never done.
- why a thread doing unrelated work must not block a critical section ::@:: Progress requires that work unrelated to the critical section cannot hold out a thread that wants in.
- which of mutual exclusion, progress and bounded waiting is a safety property ::@:: Mutual exclusion; progress and bounded waiting are the two liveness properties.
- what liveness means for a critical-section solution ::@:: The program keeps making progress instead of getting stuck, so a thread that keeps asking enters eventually.
- which critical-section requirement is the fairness one, and what it stops ::@:: Bounded waiting; it stops one thread starving while the rest keep circulating.
- why progress alone does not stop starvation ::@:: It asks only that some waiter gets in, which one thread can satisfy every time, leaving another waiting.

<!-- check: ignore-next-line[header_style]: Peterson is a proper noun -->
## Peterson's algorithm

Peterson's algorithm is a software-only protocol for the critical-section problem with two processes. Both alternate between a critical section and a remainder section, and the protocol asks of the machine only a load and a store.

They share `flag[2]`, two booleans where `flag[i]` true means process $i$ wants to enter, and `turn`, an integer, 0 or 1, naming whose turn it is.

A process enters by raising its own flag, setting `turn` to the other, then spinning while the other's flag is raised and the turn still names the other. On the way out it lowers its flag.

```c
/* the entry and exit sections, for process i with the other process j = 1 - i */
flag[i] = true;
turn = j;
while (flag[j] && turn == j)
    ;
/* critical section */
flag[i] = false;
/* remainder section */
```

Both cannot be inside at once. With both flags raised, `turn` names exactly one process, and only that one finds the spin condition false. The other waits, since its store to `turn` landed first.

Progress costs nothing extra: when the partner is not interested its flag stays lowered, so the other reads a false spin condition and enters at once.

A process waits at most one turn, since it never writes `turn` while it spins. Once the partner leaves, the spinner reads a lowered flag or finds the turn naming itself.

Each load and store of a single variable has to be atomic, so nobody reads a half-written `turn`. In C the variables are declared `atomic_bool` and `atomic_int`, and every access names `memory_order_seq_cst`, which also keeps the stores in order.

```c
#include <pthread.h>
#include <stdatomic.h>
#include <stdbool.h>
#include <stdio.h>

static atomic_bool flag[2];
static atomic_int turn;
static long long counter = 0;

#define ITER 1000000

static inline void enter_region(int i)
{
    int j = 1 - i;

    atomic_store_explicit(&flag[i], true, memory_order_seq_cst);
    atomic_store_explicit(&turn, j, memory_order_seq_cst);

    /* spin while the other process wants in and it holds the turn */
    while (atomic_load_explicit(&flag[j], memory_order_seq_cst) &&
           atomic_load_explicit(&turn, memory_order_seq_cst) == j) {
        /* spin */
    }
}

static inline void exit_region(int i)
{
    atomic_store_explicit(&flag[i], false, memory_order_seq_cst);
}

void *worker0(void *arg)
{
    for (int k = 0; k < ITER; ++k) {
        enter_region(0);
        counter++;                    /* critical section */
        exit_region(0);
        /* remainder section */
    }
    return NULL;
}
```

`worker1` is the same function with index 1.

```c
int main(void)
{
    atomic_store(&flag[0], false);
    atomic_store(&flag[1], false);
    atomic_store(&turn, 0);

    pthread_t t0, t1;
    if (pthread_create(&t0, NULL, worker0, NULL) ||
        pthread_create(&t1, NULL, worker1, NULL)) {
        perror("pthread_create");
        return 1;
    }

    pthread_join(t0, NULL);
    pthread_join(t1, NULL);

    printf("Expected counter = %d\n", 2 * ITER);
    printf("Actual   counter = %lld\n", counter);
    return 0;
}
```

```text
./peterson
Expected counter = 2000000
Actual   counter = 2000000
```

The costs belong to any software solution: tangled code even for two processes, a separate version per process, and processor time burned spinning that a sleeping process would give back.

---

Flashcards for this section are as follows:

- Peterson's algorithm ::@:: A software-only solution to the critical-section problem for two processes, each alternating between a critical section and a remainder section.
- the two variables Peterson's algorithm shares, for process $i$ and the other process $j$ ::@:: `flag[2]`, where `flag[i]` true means process $i$ wants to enter, and `turn`, an integer naming whose turn it is.
- what process $i$ does to enter its critical section under Peterson's algorithm ::@:: It raises `flag[i]`, sets `turn` to the other process's index $j$, then spins while `flag[j]` is raised and `turn` still equals $j$.
- why two processes cannot both be inside under Peterson's algorithm ::@:: With both flags raised, `turn` holds one value, so only the process it names finds the spin condition false.
- which process waits when both want to enter under Peterson's algorithm ::@:: The one whose store to `turn` landed first, since `turn` names the other process.
- how long one process can wait under Peterson's algorithm ::@:: At most one turn, because it never writes `turn` while spinning, so it enters once the partner leaves.
- what Peterson's algorithm assumes about loads and stores ::@:: Each load and store of a single variable is atomic, so no one reads a half-written `turn`.
- why the atomic version of Peterson's algorithm names `memory_order_seq_cst` on every access ::@:: The stores of the entry section keep their order, so the partner sees the raised flag before the new turn.
- what Peterson's algorithm costs ::@:: Tangled code for two processes, a separate version for each of them, and processor time spent spinning.
- why Peterson's algorithm still satisfies progress when the other process never wants in ::@:: That process leaves its `flag` entry lowered, so the spin condition is false at once.
- the C types that hold the shared variables of Peterson's algorithm ::@:: `atomic_bool` for the two `flag` entries and `atomic_int` for `turn`.
- what a two-thread Peterson program prints after each thread increments a shared `counter` `ITER` times ::@:: An expected counter of `2 * ITER` and an actual counter of the same value, so no increment is lost.
- prototype of `pthread_create()`, and the call that starts the two threads ::@:: `int pthread_create(pthread_t *tid, const pthread_attr_t *attr, void *(*start_routine)(void *), void *arg)`, called as `pthread_create(&t0, NULL, worker0, NULL)`: starts `worker0` with default attributes and no argument.
- prototype of `pthread_join()`, and its use ::@:: `int pthread_join(pthread_t tid, void **ret)`, called as `pthread_join(t0, NULL)`: waits for that thread to end and discards its return value.

## kernel synchronization primitives

### mutex locks

A mutex gives mutual exclusion to the threads of one process and guards one shared resource or critical section. The type is `pthread_mutex_t` from `<pthread.h>`, with four calls: init, lock, unlock, destroy.

The order is lock, access, unlock. A thread that exits while holding the lock blocks every other thread that wants it, since nothing releases the lock. What belongs inside that region is in [mutex practice](../../pthreads.md#mutex%20practice).

```c
#include <pthread.h>

pthread_mutex_t mutex;

int main()
{
    /* create and initialize the mutex lock */
    pthread_mutex_init(&mutex, NULL);

    /* lock, use the shared resource, unlock */
    pthread_mutex_lock(&mutex);
    /* critical section */
    pthread_mutex_unlock(&mutex);

    pthread_mutex_destroy(&mutex);
    return 0;
}
```

---

Flashcards for this section are as follows:

- mutex ::@:: A lock that gives mutual exclusion to the threads of one process, guarding one shared resource or critical section.
- prototype of `pthread_mutex_init()`, and its use ::@:: `int pthread_mutex_init(pthread_mutex_t *mutex, const pthread_attr_t *attr)`, called as `pthread_mutex_init(&mutex, NULL)`: `&mutex` is the lock, `NULL` asks for default attributes.
- prototype of `pthread_mutex_lock()`, and its use ::@:: `int pthread_mutex_lock(pthread_mutex_t *mutex)`, called as `pthread_mutex_lock(&mutex)`: takes the lock and returns only once this thread holds it.
- prototype of `pthread_mutex_unlock()`, and its use ::@:: `int pthread_mutex_unlock(pthread_mutex_t *mutex)`, called as `pthread_mutex_unlock(&mutex)`: releases the lock so another thread can enter.
- prototype of `pthread_mutex_destroy()`, and when it is called ::@:: `int pthread_mutex_destroy(pthread_mutex_t *mutex)`, called as `pthread_mutex_destroy(&mutex)`: frees the mutex after the critical section, when no thread holds or waits for it.
- what happens to the other threads when one thread dies while holding a mutex ::@:: They block forever, since nothing releases the lock for the dead thread.
- header that declares the mutex type and its calls ::@:: `<pthread.h>`.

### semaphores

A semaphore is a non-negative integer acting as a generalised lock. Edsger Dijkstra defined it in the late 1960s; original UNIX made it its main synchronization primitive.

`wait(S)` takes a permit: if `S` is above zero it subtracts one, otherwise the caller sleeps until someone signals. `signal(S)` returns a permit: it adds one and wakes one sleeper if any waits. Dijkstra named them `P()` and `V()`, from Dutch `proberen` (to test) and `verhogen` (to increment).

The two operations must run atomically, so no more than one process changes a semaphore at a time. An initial value of 1 allows one holder and behaves like a mutex; larger values count resources, and 0 orders events.

The POSIX calls are `sem_init`, `sem_wait`, `sem_post`, `sem_destroy`, declared in `<semaphore.h>`. The `pshared` argument of `sem_init` says how far the semaphore reaches: 0 shares it among one process's threads, any other value across processes that share memory.

```c
#include <semaphore.h>

sem_t sem;

int main()
{
    /* one permit, shared among the threads of this process */
    sem_init(&sem, 0, 1);

    sem_wait(&sem);      /* take the permit */
    /* critical section */
    sem_post(&sem);      /* return it */

    sem_destroy(&sem);
    return 0;
}
```

---

Flashcards for this section are as follows:

- semaphore ::@:: A non-negative integer that acts as a generalised lock, changed only by `wait()` and `signal()`.
- who defined the semaphore, and what it was in original UNIX ::@:: Edsger Dijkstra, in the late 1960s; it was the main synchronization primitive of original UNIX.
- what `wait(S)` does ::@:: If `S` is above zero it subtracts one, and otherwise the caller sleeps until someone signals.
- what `signal(S)` does ::@:: It adds one to `S` and wakes one sleeping waiter if there is one.
- the original names of `wait()` and `signal()`, and the Dutch words behind them ::@:: `P()` and `V()`, from `proberen` (to test) and `verhogen` (to increment).
- why the operations on a semaphore must be atomic ::@:: So that no more than one process changes the same semaphore at a time and no update is lost.
- what a semaphore with an initial value of 1 does ::@:: It allows one holder at a time, so it behaves like a mutex.
- prototype of `sem_init()`, and its use ::@:: `int sem_init(sem_t *sem, int pshared, unsigned int value)`, called as `sem_init(&sem, 0, 1)`: `&sem` names the semaphore, `pshared` is `0` so only this process's threads share it, `value` is `1`, which makes it a lock.
- prototype of `sem_wait()`, and its use ::@:: `int sem_wait(sem_t *sem)`, called as `sem_wait(&sem)`: takes the permit, waiting until one exists.
- prototype of `sem_post()`, and its use ::@:: `int sem_post(sem_t *sem)`, called as `sem_post(&sem)`: returns the permit and wakes a waiter.
- prototype of `sem_destroy()`, and when it is called ::@:: `int sem_destroy(sem_t *sem)`, called as `sem_destroy(&sem)`: frees the semaphore once no thread waits on it.
- what the `pshared` argument of `sem_init()` chooses ::@:: How far the semaphore reaches: 0 for the threads of one process, non-zero across processes that share memory.
- what a semaphore above 1 and a semaphore at 0 are used for ::@:: A value above 1 counts the copies of a resource left, and 0 orders events, blocking a waiter until another process signals.

### condition variables

A condition variable lets threads wait for a change of state, and always pairs with a mutex protecting the condition. The type is `pthread_cond_t`, with init, wait, signal, broadcast, destroy calls.

`pthread_cond_wait(&cond, &mutex)` releases the mutex and puts the caller to sleep in one atomic step, so another thread can take the mutex and change the shared state. Doing the two separately opens a gap: a signal arriving between release and sleep finds no waiter, gets lost, and the thread sleeps on a condition that already holds. A signal wakes the waiter, which takes the mutex back and returns.

The waiter re-reads the flag in a `while` loop and waits again unless its condition now holds.

```c
#include <pthread.h>
#include <stddef.h>

#define ITEM_COUNT 2

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cond;
int items;        /* stored and not yet taken */
int finished;     /* the producer has stopped */

/* thread 0: the producer, which changes the condition */
void *producer(void *arg)
{
    for (int i = 0; i < ITEM_COUNT; i++) {
        pthread_mutex_lock(&mutex);
        items++;
        pthread_cond_signal(&cond);          /* one waiter takes the new item */
        pthread_mutex_unlock(&mutex);
    }

    pthread_mutex_lock(&mutex);
    finished = 1;
    pthread_cond_broadcast(&cond);           /* every remaining waiter leaves */
    pthread_mutex_unlock(&mutex);
    return NULL;
}

/* threads 1 and 2: the consumers, which wait for it */
void *consumer(void *arg)
{
    pthread_mutex_lock(&mutex);
    while (items == 0 && !finished) {
        pthread_cond_wait(&cond, &mutex);
    }
    pthread_mutex_unlock(&mutex);
    return NULL;
}

int main(void)
{
    pthread_t producer_id, first, second;

    pthread_cond_init(&cond, NULL);            /* before any thread can wait */
    pthread_create(&producer_id, NULL, producer, NULL);
    pthread_create(&first, NULL, consumer, NULL);
    pthread_create(&second, NULL, consumer, NULL);

    pthread_join(producer_id, NULL);
    pthread_join(first, NULL);
    pthread_join(second, NULL);
    pthread_cond_destroy(&cond);               /* no waiter is left */
    return 0;
}
```

A waiting consumer spends no processor time, unlike one spinning on a loop. Which wake-up call to use is in [signal and broadcast](../../pthreads.md#signal%20and%20broadcast).

---

Flashcards for this section are as follows:

- condition variable ::@:: A POSIX Threads (pthreads) object on which a thread waits for a change of state, always paired with a mutex that protects the condition.
- prototype of `pthread_cond_init()`, and its use ::@:: `int pthread_cond_init(pthread_cond_t *cond, const pthread_condattr_t *attr)`, called as `pthread_cond_init(&cond, NULL)`: fills the condition variable with default attributes before any thread can wait on it.
- prototype of `pthread_cond_wait()`, and its use ::@:: `int pthread_cond_wait(pthread_cond_t *cond, pthread_mutex_t *mutex)`, called as `pthread_cond_wait(&cond, &mutex)`: `cond` is the condition the producer signals, `mutex` the lock the caller holds, which the call releases and re-takes; the caller re-tests the predicate in a `while` loop.
- prototype of `pthread_cond_signal()`, and its use ::@:: `int pthread_cond_signal(pthread_cond_t *cond)`, called as `pthread_cond_signal(&cond)`: wakes one waiter, enough when one item becomes available.
- prototype of `pthread_cond_broadcast()`, and its use ::@:: `int pthread_cond_broadcast(pthread_cond_t *cond)`, called as `pthread_cond_broadcast(&cond)`: wakes every waiter, which the shutdown flag needs.
- prototype of `pthread_cond_destroy()`, and when it is called ::@:: `int pthread_cond_destroy(pthread_cond_t *cond)`, called as `pthread_cond_destroy(&cond)`: frees the condition variable after the joins, when no thread is asleep on it.
- what `pthread_cond_wait(&cond, &mutex)` does in one step ::@:: It releases the mutex and blocks the caller, so another thread can take the mutex and change the shared state.
- what a waiting thread does when it is signalled ::@:: It wakes, takes the mutex back, then returns from `pthread_cond_wait()`.
- why the waiter re-reads the flag in a `while` loop ::@:: It waits again unless the condition it needs has become true, since the signal alone does not say which state was reached.
- what the producer in a condition-variable pair does ::@:: It takes the mutex, sets the flag the consumer waits on, signals the condition, and releases the mutex.
- why a condition variable wastes less processor time than a spin loop ::@:: A waiting thread sleeps and gives the processor back; a spinning thread keeps checking.

### lifetime and misuse

Each object is initialized, used and destroyed, and the standard guarantees only the middle part. Destroying an idle object is safe: an unlocked mutex, or a semaphore or condition variable with no blocked thread. Destroying a locked mutex, one another thread waits on, or a semaphore or condition variable with a thread asleep, is undefined behaviour. The call may still succeed and take the object away, `sem_destroy` may report `EBUSY` instead, and the sleeping thread may never wake.

Destroying an object leaves it uninitialized, so its calls stay undefined until the matching init call runs again. Using one before init is undefined for the same reason: the call may report `EINVAL`, and a zeroed object often behaves like a default mutex or a semaphore at 0, so the mistake passes a test and later fails.

Unlocking a mutex the calling thread does not hold reports an error only on the error-checking type, which returns `EPERM`. The default type checks nothing, and the effect is undefined.

A semaphore can be destroyed while permits are outstanding, since no thread is blocked then. The remaining count is discarded, so a process that waits afterwards blocks until the semaphore is initialized again.

Destroying each object after the last join that can reach it avoids all of this: the condition variable goes before the mutex it waits on.

---

Flashcards for this section are as follows:

- when a mutex, semaphore or condition variable may be destroyed ::@:: Only while it is idle: an unlocked mutex, or a semaphore or condition variable with no thread blocked on it.
- what happens when a locked mutex, or a semaphore or condition variable with a waiting thread, is destroyed ::@:: Undefined behaviour: the call may take the object away, `sem_destroy` may report `EBUSY` instead, and the sleeping thread may never wake.
- using a mutex, semaphore or condition variable after its destroy call ::@:: Undefined until it is initialized again, since destroy leaves the object uninitialized.
- what a mutex lock or a semaphore wait does before the init call runs ::@:: Undefined behaviour; the call may report `EINVAL`, and a zeroed object often behaves like a default mutex or a semaphore at 0, so the mistake can pass unnoticed.
- what unlocking a mutex from a thread that does not hold it does ::@:: It fails with `EPERM` only for the error-checking type; the default type detects nothing and the effect is undefined.
- what destroying a semaphore with permits outstanding does ::@:: The remaining count is discarded, so a process that waits afterwards blocks until the semaphore is initialized again.

## synchronization exercises

### strict alternation

> The three threads below must run their critical sections in the order T1, T2, T3, T1, T2, T3, and so on, where `wait` takes a permit and `signal` returns one. What are the initial values of S1, S2 and S3?
>
> ```c
> /* thread T1 */
> while (TRUE) {
>     wait(S1);
>     /* critical section */
>     signal(S2);
> }
>
> /* thread T2 */
> while (TRUE) {
>     wait(S2);
>     /* critical section */
>     signal(S3);
> }
>
> /* thread T3 */
> while (TRUE) {
>     wait(S3);
>     /* critical section */
>     signal(S1);
> }
> ```
>
> ---
>
> - solution: {@{`S1 = 1`, `S2 = 0` and `S3 = 0`}@}
> - explanation: T1 enters first, so {@{it starts with the one permit}@}. Each thread {@{hands on the permit the next one waits for}@}, so {@{S2 and S3 start empty, which keeps the cycle in order}@}. {@{Starting all three at 1}@} would let {@{every thread into its critical section at once}@}.

<!-- markdownlint MD028 -->

> Three processes must enter their critical sections in the order P0, P1, P2, P0, P1, P2. Which values and calls fill the seven blanks?
>
> ```c
> /* S0, S1 and S2 are shared */
> S0 = BLANK1;
> S1 = BLANK2;
> S2 = BLANK3;
>
> /* process P0 */
> while (true) {
>     wait(S0);
>     /* critical section */
>     BLANK4;
> }
>
> /* process P1 */
> while (true) {
>     BLANK5;
>     /* critical section */
>     BLANK6;
> }
>
> /* process P2 */
> while (true) {
>     BLANK7;
>     /* critical section */
>     signal(S0);
> }
> ```
>
> ---
>
> - solution: {@{`S0 = 1`, `S1 = 0` and `S2 = 0`, with `signal(S1)` in P0, `wait(S1)` and `signal(S2)` in P1, and `wait(S2)` in P2}@}
> - explanation: P0 runs first, so {@{S0 holds the single permit at the start}@}. Each process {@{waits on the permit the previous one returns}@}, which {@{chains the three critical sections in order}@}, and P2 {@{returns the permit to S0 so the cycle repeats}@}.

### permits of a counting semaphore

> Three processes use four counting semaphores, initialised as `S0 = 1`, `S1 = 0`, `S2 = 0` and `S3 = 0`. How many times does the `1` of P0 get printed?
>
> ```c
> /* process P0 */
> while (true) {
>     wait(S0);
>     print '1';
>     release(S1);
>     release(S2);
>     release(S3);
> }
>
> /* process P1 */
> wait(S1);
> release(S0);
>
> /* process P2 */
> wait(S2);
> release(S0);
> wait(S3);
> release(S0);
> ```
>
> ---
>
> - solution: {@{4 times}@}
> - explanation: The first print {@{consumes the one permit S0 starts with}@}, then returns {@{three more S0 permits, one through S1 and two through S2 and S3}@}. Each of the three permits {@{lets P0 print again}@}, so four S0 permits are {@{spent in all and the fifth `wait(S0)` blocks forever}@}.

### protection with a mutex

> The program below increments a shared `counter` from two threads. What fills its three blanks, and what is the final value of `counter`?
>
> ```c
> #include <stdio.h>
> #include <pthread.h>
>
> unsigned int counter = 0;
> #define TOTAL_ITERATIONS 5000
>
> void *add(void *arg) {
>   int i;
>   pthread_mutex_t* m = BLANK1;
>   for (i=0; i<TOTAL_ITERATIONS; i++) {
>     BLANK2;
>     ++counter;
>     BLANK3;
>   }
>   return NULL;
> }
>
> int main() {
>   pthread_t tid1, tid2;
>   pthread_mutex_t mutex;
>   pthread_mutex_init(&mutex, NULL);
>   pthread_create(&tid1, NULL, add, &mutex);
>   pthread_create(&tid2, NULL, add, &mutex);
>   pthread_join(tid1, NULL);
>   pthread_join(tid2, NULL);
>   printf("The final counter value is %d\n", counter);
>   return 0;
> }
> ```
>
> ---
>
> - solution: {@{`(pthread_mutex_t*) arg`, `pthread_mutex_lock(m)` and `pthread_mutex_unlock(m)`, with a final count of 10000}@}
> - explanation: {@{The fourth argument of `pthread_create()`}@} is `&mutex`, so `arg` holds {@{the address of the mutex and the cast restores its type}@}. The lock goes {@{before the increment and the unlock after it}@}. Each thread adds {@{5000 to the same variable}@}, and the two joins {@{let the main thread read the whole 10000}@}.

<!-- markdownlint MD028 -->

> The two fragments below implement a reader-writer lock over a shared data set: a writer needs it to itself, readers may be inside together, and no reader and writer may hold it at once. Many readers and many writers run the same fragments, so `read_count`, which starts at 0, says how many readers are inside. Which calls fill the six blanks of the reader process?
>
> ```c
> /* the structure of a writer process */
> do {
>     pthread_mutex_lock(&rw_mutex);
>     /* writing is performed */
>     pthread_mutex_unlock(&rw_mutex);
> } while (true);
>
> /* the structure of a reader process */
> do {
>     BLANK1;
>     read_count++;
>     if (read_count == 1)
>         BLANK2;
>     BLANK3;
>     /* reading is performed */
>     BLANK4;
>     read_count--;
>     if (read_count == 0)
>         BLANK5;
>     BLANK6;
> } while (true);
> ```
>
> ---
>
> - solution: {@{`pthread_mutex_lock(&mutex)`, `pthread_mutex_lock(&rw_mutex)`, `pthread_mutex_unlock(&mutex)`, `pthread_mutex_lock(&mutex)`, `pthread_mutex_unlock(&rw_mutex)`, `pthread_mutex_unlock(&mutex)`}@}
> - explanation: `rw_mutex` is {@{the read-write lock on the data}@}, and readers {@{share it as a group to exclude any writer}@}: {@{the first reader takes it and the last one releases it}@}. `mutex` protects {@{`read_count`, whose increment suffers the same race as `counter++`}@}, so every change to it sits {@{inside a lock of `mutex` and outside the reading}@}.

<!-- markdownlint MD028 -->

> Is a binary semaphore equivalent to a mutex lock (Yes/No)? Explain briefly.
>
> ---
>
> - solution: {@{No}@}
> - explanation: A binary semaphore {@{initialised to 1 does hold one thread at a time}@}, so it can {@{stand in for a mutex}@}. The same type is also used {@{with an initial value of 0 to order events}@}, where it {@{holds no lock at all}@}, so {@{the two are not equivalent}@}.

### possible outputs

> Two processes share semaphores X and Y, both initialised to 0. Which outputs are possible when both processes complete?
>
> ```cpp
> /* process A */
> wait(X);
> cout << "b";
> signal(Y);
> wait(Y);
> cout << "c";
> signal(Y);
>
> /* process B */
> signal(X);
> cout << "a";
> wait(Y);
> cout << "d";
> ```
>
> ---
>
> - solution: {@{`abcd`, `bacd` and `bcad`}@}
> - explanation: {@{`wait(X)` and `signal(X)`}@} cancel out, so `a` and `b` may {@{appear in either order}@}. Only {@{`Y` orders anything}@}. Process {@{A signals `Y` after `b` and again after `c`}@}, and process {@{B never signals it}@}, so the first permit is {@{the one A sends after `b`}@}. Two waits {@{compete for that permit}@}: {@{A's `wait(Y)` and B's}@}. If {@{B takes it}@}, then {@{A blocks at its own wait}@} and the signal that {@{could release A comes after `c`}@}, which {@{A never reaches, so those runs are discarded}@}. The permit must {@{reach A instead}@}, which forces {@{`b` before `c`}@}, {@{`c` before `d`}@} because B {@{prints `d` only after A's second signal}@}, and {@{`a` before `d`}@}. Into {@{the fixed order `b < c < d`}@}, `a` can {@{go first, between `b` and `c`, or between `c` and `d`}@}, giving {@{`abcd`, `bacd` and `bcad`}@}; after `d` it would {@{break `a < d`}@}.

<!-- markdownlint MD028 -->

> Two threads run the code below with `a = 1`, `b = 3` and `c = 0`. Reads and writes of each variable are atomic, and each thread keeps the order of its own statements. Which values can `c` hold after both finish?
>
> ```c
> /* thread 1 */
> a = b + 1;
> c = a - b;
>
> /* thread 2 */
> a = 13;
> b = 10;
> c = 2;
> ```
>
> ---
>
> - solution: {@{`-6`, `1`, `2`, `3` and `10`}@}
> - explanation: {@{Thread 2's `c = 2`}@} stands alone: it may be {@{the last write of `c`, which makes `2` a possible answer}@}. Every other run ends at {@{thread 1's `c = a - b`, whose two reads need not agree}@}, so the answer turns on {@{which write each read sees}@}. The choice starts at {@{thread 1's first read, of `b` in `a = b + 1`}@}, which can see {@{3 or 10}@}. Reading 10 means {@{thread 2 has already run `a = 13`}@}, so thread 1 writes {@{`a = 11`}@} afterwards and the subtraction can then {@{read only 11 and 10, giving `1`}@}. Reading {@{3 means thread 1 writes `a = 4`}@}, and {@{the pair the subtraction reads}@} may then be {@{4 and 3, 4 and 10, 13 and 3, or 13 and 10}@}, giving {@{`1`, `-6`, `10` and `3`}@}. With `2` these are {@{the five values}@}.

---

Flashcards for this section are as follows:

- what one line such as `c = a - b` is made of, when each variable access is atomic ::@:: The line is three atomic actions: a read of `a`, a read of `b`, a write of the difference, with another thread free to run between them.
- how a thread can subtract an `a` written by itself from a `b` written by the other thread ::@:: It loads `a` first and `b` later, so the other thread's write to `b` lands between the two reads.
- which of the two threads decides the final value of `c` when both write it ::@:: The one whose write comes last, so either thread's value can survive.
