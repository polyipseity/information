---
aliases:
  - process synchronization
  - synchronization
  - synchronization (computer science)
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/synchronization_(computer_science)
  - language/in/English
---

# synchronization (computer science)

Cooperating flows of execution share data, and any one can be interrupted between two machine instructions. Two threads of one process reach a shared variable as readily as two processes do, and either pair can leave it in a state neither intended. Synchronization orders the conflicting steps so the scheduler cannot interleave them.

A mutex lock, a semaphore, and a condition variable do this work, and none is a hand-built lock. A condition variable lets a thread sleep instead of spinning. The bounded buffer of the [producer-consumer problem](producer–consumer%20problem.md) uses all three.

---

Flashcards for this section are as follows:

- what synchronization does for an operating system ::@:: It orders the steps of cooperating processes that share data, so the result does not depend on the scheduler.
- why concurrent access to shared data is dangerous ::@:: A process can be switched out between any two machine instructions, so another can read a shared variable halfway through an update.
- three primitives an operating system supplies for synchronization ::@:: A mutex lock, a semaphore, and a condition variable.

## race conditions and the critical section

### race conditions

Two flows that update the same variable can lose an update. `counter++` looks like one step in C; the machine runs it as three: load the counter, add one, store it back. `counter--` does the same with a subtraction.

Start the counter at 5 with one increment and one decrement in flight. The incrementing flow loads 5, adds one, and holds 6. The decrementing flow loads 5 before that store lands and holds 4. Both stores land, the last one wins, and an update vanishes: the counter ends at 6 or at 4 where cancelling should have left 5.

A race condition is several flows reaching shared data at once, with the outcome changing from run to run. It leaves data inconsistent, and one run can still look right.

One core is enough, and one process is enough. Two threads of a single program, run one at a time on one processor, interleave exactly as two processes do, because the scheduler switches between them between instructions. Whether the flows are threads or processes matters only for how they reach the data: threads share memory directly, processes need shared memory or a file.

The kernel has the same problem. `fork()` takes the next free process identifier from a shared kernel variable, so two processes forking at once can get the same identifier. The process list, the memory table, and the open-file table are shared the same way.

---

Flashcards for this section are as follows:

- why `counter++` is not one action ::@:: The compiler emits three steps: load the counter into a register, add one, store it back. Another flow can run between any two.
- whether a race condition needs two processes ::@:: No. Two threads of one process reach the same memory, and either pair interleaves between instructions.
- whether a race condition needs several cores ::@:: No. The scheduler interleaves the two flows on one core, so a single processor loses the update just the same.
- what a race condition turns on ::@:: The interleaving of steps at instruction level: the steps of one access are separated by the steps of another.
- what changes when the flows are threads of one process ::@:: Only how they reach the data, since threads share memory directly while processes need shared memory or a file.
- what a race condition is ::@:: Two or more processes reach a shared variable at once and the result depends on the order of their accesses, so the output changes from run to run.
- how one increment and one decrement lose an update starting from a counter of 5 ::@:: Both processes load 5 before either stores, one computes 6 and the other 4, and the later store overwrites the earlier one.
- what a shared counter holds after one increment and one decrement that both start from 5 ::@:: 4 if the decrement stores last, or 6 if the increment stores last. The correct 5 never appears.
- what data inconsistency means ::@:: Shared state left in a condition that no serial order of the same updates could have produced.
- why two processes calling `fork()` at once can get the same process identifier ::@:: Both read the next free identifier from the same kernel variable before either updates it, so both children can get it.

### critical section problem

A critical section is the part of a flow of execution that touches data shared with another flow: a shared variable, a table, a file. While one flow is inside, no other may be inside its own section for that data, whether the two are processes or threads. The rule is mutual exclusion, and writing a protocol that enforces it is the critical-section problem.

Each process runs four parts in order: an entry section that asks permission, the critical section, an exit section that gives it back, and a remainder section.

A solution must satisfy three requirements. Mutual exclusion is safety: at most one process inside. Progress is liveness: if nobody is inside and some want in, one of them enters, and the choice cannot be postponed forever. Bounded waiting caps the wait: once a process asks, only a bounded number of others may enter before its request is granted.

The requirements assume little. Every process runs at some nonzero speed, and nothing is assumed about relative speeds. A process can be preempted at any point, so a protocol that needs a run of steps to finish undisturbed has assumed the problem away.

---

Flashcards for this section are as follows:

- what a critical section is ::@:: The part of a process that reads or writes data shared with another, so it must not run at the same time as that other process's section on the same data.
- four parts of a process around its critical section ::@:: An entry section that asks permission, the critical section, an exit section that gives the permission back, and a remainder section.
- three requirements of a critical-section solution ::@:: Mutual exclusion, progress, and bounded waiting.
- what mutual exclusion requires ::@:: While one process is inside its critical section, no other process is inside a critical section for the same data.
- what progress requires ::@:: If no process is inside and some want in, one of them is chosen to enter, and that choice cannot be put off forever.
- what bounded waiting requires ::@:: A bound on how many other processes may enter their critical sections after one process asks and before its own request is granted.
- what a solution satisfies when it never admits any process ::@:: Mutual exclusion only. It is safe and useless, and it fails progress.
- what a critical-section solution assumes about process speed ::@:: Every process runs at a nonzero speed, and nothing is assumed about their relative speeds.
- what a critical-section solution must assume about preemption ::@:: A process can be switched out between any two instructions, so no solution may rely on a sequence of steps finishing undisturbed.

## software and hardware support

<!-- check: ignore-next-line[header_style]: Peterson is a proper noun -->
### Peterson's solution

Peterson's solution is a software protocol for two processes that alternate between critical sections and remainder sections. They share `flag[2]`, two booleans where `flag[i]` true means process $i$ wants in, and `turn`, an integer holding 0 or 1 that names whose turn it is.

Process $i$ sets `flag[i]` to true, sets `turn` to the other process's index $j$, and spins while `flag[j]` is true and `turn` is still $j$. On the way out it clears `flag[i]`.

```c
#include <stdatomic.h>
#include <stdbool.h>

static atomic_bool flag[2] = { false, false };   /* who wants in */
static atomic_int turn = 0;                      /* whose turn it is */

void lock(int i)                     /* i is 0 or 1 */
{
    int j = 1 - i;

    atomic_store(&flag[i], true);    /* I want in */
    atomic_store(&turn, j);          /* but you go first if you want it */
    while (atomic_load(&flag[j]) && atomic_load(&turn) == j)
        ;                            /* spin while the other wants in and it is its turn */
}

void unlock(int i)
{
    atomic_store(&flag[i], false);
}
```

Both cannot be inside at once. With both flags true, `turn` holds one value, so exactly one process finds its spin condition false: the one `turn` names. The other waits, having stored to `turn` last.

The protocol needs two things from the machine. Each load and store of one variable must be indivisible, so no reader sees a half-written `turn`. The two stores in the entry section must keep their order, so the raised flag is visible before the new turn. Without that ordering the exclusion argument fails.

The first costs nothing: an aligned load or store of one word is a single machine instruction, and no interrupt splits it. The second is not free, because a processor may buffer or reorder its stores. The code orders them with a barrier: `atomic_thread_fence(memory_order_seq_cst)` in C11, `mfence` on x86, or `dmb ish` on ARM. The `atomic_store` and `atomic_load` calls above are sequentially consistent by default, so they carry both properties without a fence.

A process waits at most one turn. It never writes `turn` while it spins, so once the other process leaves, the spinner either sees the flag cleared or finds `turn` naming itself. Progress needs no extra rule: a process whose partner is not interested reads a false flag and enters at once.

Enlarging the arrays does not turn the two-process version into an n-process solution; the generalizations are different algorithms. Peterson's filter algorithm stacks $n - 1$ levels, each with a flag and a turn, and a thread walks up them to enter. Lamport's bakery gives each thread a ticket and admits the smallest, breaking ties by thread order.

No real system uses them. The protocol needs sequential consistency, which costs more than the atomic instructions a processor offers, and it busy-waits without holding a lock. Its value is the proof that mutual exclusion needs nothing beyond ordinary loads and stores with the right ordering.

---

Flashcards for this section are as follows:

- what the two shared variables of Peterson's solution hold ::@:: `flag[0]` and `flag[1]`, where a true flag means that process wants in, and `turn`, an integer holding 0 or 1 that names whose turn it is.
- what process `i` does in the entry section of Peterson's solution ::@:: It sets `flag[i]` to true, sets `turn` to the other process's index `j`, and spins while `flag[j]` is true and `turn` still equals `j`.
- why two processes cannot both be inside under Peterson's solution ::@:: A process spins out only when the other's flag is false or `turn` names itself, and `turn` holds one value, so at most one finds its condition false.
- which process waits when both want to enter under Peterson's solution ::@:: The one that wrote `turn` last. The other is named by `turn`, finds its spin condition false, and goes in.
- what Peterson's solution needs from the machine ::@:: Each load and store of one variable is indivisible, and the two stores of the entry section keep their order, so the raised flag is visible before the new turn.
- how long one process can wait under Peterson's solution ::@:: At most one turn. It never writes `turn` while it spins, so when the other process leaves the critical section the spinner enters.
- what Peterson's solution costs ::@:: Busy waiting, different code for each of the two processes, and a protocol that needs sequential consistency.
- which atomics the C version of Peterson's solution uses ::@:: `atomic_bool` for the flags and `atomic_int` for `turn`, all sequentially consistent by default, so the stores keep their order.
- what the second store in Peterson's entry section accomplishes ::@:: `turn = j` gives the other process priority. The process that stores last loses the turn and waits.
- why `unlock()` clears only the thread's own flag under Peterson's solution ::@:: Clearing `flag[i]` withdraws the request, and `turn` stays as it is so a waiting partner sees a false flag and enters.
- what makes an aligned single-word load or store atomic ::@:: It is one machine instruction, so no interrupt lands in the middle and no reader sees half a value.
- how the ordering requirement of Peterson's solution is met ::@:: With a memory barrier: `atomic_thread_fence(memory_order_seq_cst)` in C11, `mfence` on x86, or `dmb ish` on ARM.
- whether Peterson's solution extends to n processes ::@:: Not by enlarging the arrays. The n-process generalizations are different algorithms.
- idea of Peterson's filter algorithm with $n$ threads ::@:: It stacks $n - 1$ levels, each with a flag and a turn, and a thread walks up them to enter.
- idea of Lamport's bakery algorithm ::@:: Each thread takes a ticket, and the thread with the smallest ticket enters, with ties broken by thread order.
- why real systems do not use Peterson's solution ::@:: It needs sequential consistency, which costs more than the atomic instructions hardware offers, and it busy-waits.
- why Peterson's solution meets the progress requirement without an extra rule ::@:: A process whose partner is not interested reads `flag[j]` as false and enters at once, so a critical section nobody is inside is never left idle.

### test-and-set and compare-and-swap

Masking interrupts stops preemption on one processor and makes a short run of instructions atomic. With several cores the other processors keep running, so hardware instead offers instructions that are atomic by themselves. Atomic means non-interruptible: the read and the write happen as one step, and two started together run one after the other.

`test_and_set(&target)` reads the word, writes true into it whatever it read, and returns what it read, all in one indivisible step. The return is the word's value just before the call, so it is never true because of the call. False means the caller took a free word; true means somebody had set it first.

`compare_and_swap(&value, expected, new_value)` also returns the old value, but only its write is conditional: it reads the word, stores `new_value` when the value it read equals `expected`, and stores nothing otherwise. Comparing the return with `expected` says which case happened. Equal means the store landed; different means another writer got there first and the word is unchanged. A caller retries until the return equals `expected`, feeding that return back as the next `expected`; a lock test just repeats the call.

```c
/* Each of these runs as one indivisible step in hardware, so no core observes
   the word between the read and the write. */
bool test_and_set(bool *target)
{
    bool old = *target;
    *target = true;
    return old;
}

int compare_and_swap(int *value, int expected, int new_value)
{
    int old = *value;
    if (old == expected)     /* store only when nobody changed the word first */
        *value = new_value;
    return old;
}
```

The slides write these as pseudo-code instructions, not library calls. `boolean test_and_set(boolean *target)` returns the old word and sets it true; `int compare_and_swap(int *value, int expected, int new_value)` returns the old word and stores `new_value` only on a match; `void increment(atomic_int *v)` loops that call until its addition lands. A C program calls `atomic_exchange` and `atomic_compare_exchange_strong` from `stdatomic.h` instead, because a compiler cannot be trusted to keep the two steps of the listing together, and spells the slide's `boolean` as `bool`.

The same two calls with concrete values:

```c
void examples(void)
{
    bool lock = false;
    bool old = test_and_set(&lock);              /* old is false; lock is true now */

    int value = 0;
    int before = compare_and_swap(&value, 0, 1); /* before is 0; value becomes 1 */
    int again = compare_and_swap(&value, 0, 2);  /* again is 1; value stays 1 */
}
```

A lock built on `test_and_set` is a shared boolean `lock` that starts false. A process spins on `while (test_and_set(&lock));`, runs its critical section, and sets `lock = false` on the way out. The first caller through receives false and takes the lock; the rest receive true and keep spinning. Nothing bounds the wait, because a process that keeps coming back can keep winning.

An array `waiting[n]` supplies the bound. A process sets `waiting[i]` to true before it spins, and spins while `waiting[i]` and its local key are both true, the key taking whatever `test_and_set` returns. A process leaving the critical section scans `waiting` in cyclic order from $i+1$ and hands the lock to the first waiter by clearing that waiter's `waiting` entry. If nobody waits, it clears `lock`. So a waiter is passed over at most $n-1$ times.

```c
#define N 8

bool test_and_set(bool *target);   /* defined above: one indivisible step */

static bool waiting[N];
static bool lock = false;

void acquire(int i)              /* i in 0 .. N-1 */
{
    bool key;

    waiting[i] = true;           /* announce the intention */
    key = true;
    while (waiting[i] && key)
        key = test_and_set(&lock);
    waiting[i] = false;
}

void release(int i)
{
    int j = (i + 1) % N;

    while (j != i && !waiting[j])   /* first waiter in cyclic order */
        j = (j + 1) % N;
    if (j == i)
        lock = false;               /* nobody waiting: free the lock */
    else
        waiting[j] = false;         /* hand it over to that waiter */
}
```

`lock` stays true for the whole critical section. Clearing the next waiter's `waiting` entry ends its spin directly; clearing `lock` would turn every spinner loose to race again and lose the bound.

---

Flashcards for this section are as follows:

- what makes `test_and_set` atomic ::@:: The hardware reads the word and writes true as one uninterruptible step, so no other core sees it in between.
- what `test_and_set` returns ::@:: The word's value from just before the call. It always writes true and hands back what it read, so false means it took a free word and true means somebody had set it first.
- why `test_and_set` makes a lock possible ::@:: Exactly one caller receives false and leaves the word true. Every other caller receives true and knows it lost.
- signature of `test_and_set()` as the slides define it, and the call that takes the lock ::@:: `boolean test_and_set(boolean *target)`, from the slides rather than a library, called as `test_and_set(&lock)` with `lock` at false: sets `lock` true and returns false.
- what `compare_and_swap` stores and returns ::@:: It stores the new value only when the word held the expected value, and returns what it read. A return equal to `expected` means the store happened; anything else means nothing was stored.
- how a caller locks with `compare_and_swap` ::@:: It calls `compare_and_swap` on the lock word with expected 0 and new value 1, and repeats until the return is 0.
- signature of `compare_and_swap()` as the slides define it, and the call that stores only on a match ::@:: `int compare_and_swap(int *value, int expected, int new_value)`, called as `compare_and_swap(&value, 0, 1)` with `value` at `0`: stores `1` and returns `0`. The same call with `value` at `1` returns `1` and stores nothing.
- why a plain `test_and_set` lock provides no bounded waiting ::@:: A process that returns to the lock quickly can win it every time, so another process can be passed over without limit.
- how the bounded-waiting version built on `test_and_set` bounds the wait with $n$ processes ::@:: Each process raises its own entry of a waiting array before spinning. A process leaving the critical section hands the lock to the first waiter in cyclic order, so none is passed more than $n - 1$ times.
- why masking interrupts cannot make a critical-section solution atomic on a multiprocessor ::@:: Masking stops preemption on the one processor that does it. The other cores keep executing and still reach the shared data concurrently.
- how a waiter stops spinning in the bounded-waiting lock built on `test_and_set` ::@:: It spins while its own `waiting[i]` entry and the key are both true. The leaving process clears that entry instead of `lock`, which ends the spin.
- C11 equivalent of `test_and_set` ::@:: `atomic_exchange`, which replaces the word's value and returns the old one in one atomic step.
- C11 equivalent of `compare_and_swap` ::@:: `atomic_compare_exchange_strong`, which stores the new value only if the word still holds the expected one and reports whether it did.
- why the bounded-waiting lock's `release()` clears the next waiter's flag ::@:: Clearing `waiting[j]` ends that thread's spin directly. Clearing `lock` would let every spinner race for the lock again and lose the bound.
- what `release()` does when no thread is waiting ::@:: It clears `lock`, so the next `acquire()` takes the lock at once.
- what the bounded-waiting `acquire()` and `release()` replace in the plain spin lock ::@:: `acquire()` replaces the `while (test_and_set(&lock));` loop, and `release()` replaces `lock = false` with a handover through `waiting`.
- what `release(i)` scans, and why it starts at `i + 1` ::@:: It walks `waiting` in cyclic order from the next index, so every waiter is reached before any is reached twice. That is what bounds the wait.
- what `acquire(i)` does before and during its spin ::@:: It raises `waiting[i]`, then spins while that entry is set, calling `test_and_set(&lock)` each pass until the call returns false or another process clears `waiting[i]`.

### sketch proof of the bounded-waiting lock

Each requirement from the critical section needs its own argument.

Mutual exclusion holds because a process leaves its spin in only two ways. Either `test_and_set` returns false, which happens to one caller, since that call leaves `lock` true and every later call reads true. Or another process clears its `waiting` entry, and a leaving process clears exactly one entry. So at most one process passes the spin.

Progress holds because the leaving process either hands the lock to a waiter or frees it when nobody waits. Either action lets a waiting process continue.

Bounded waiting holds because the scan is cyclic. A leaving process looks from $i+1$ forward through the array and stops at the first entry that is set, so every waiter is chosen before any waiter is chosen twice. From the moment a process raises its entry, at most $n-1$ other processes enter ahead of it.

---

Flashcards for this section are as follows:

- two ways a process leaves the bounded-waiting spin ::@:: `test_and_set` returns false, or another process clears that process's `waiting` entry.
- why the bounded-waiting lock keeps mutual exclusion ::@:: Only one caller receives false from `test_and_set`, since each call leaves `lock` true, and a leaving process clears exactly one `waiting` entry.
- why the bounded-waiting lock satisfies progress ::@:: A leaving process clears the next waiter's `waiting` entry, or clears `lock` when nobody waits, and either action lets a waiting process continue.
- why the bounded-waiting lock bounds the wait at $n-1$ turns ::@:: The handover scans cyclically from $i+1$ and takes the first waiter, so every waiter is chosen before any waiter is chosen twice.

### atomic variables

An atomic variable is one basic value, an integer or a boolean, whose updates cannot be interrupted. It is built from `compare_and_swap`, with the retry loop inside a function such as `increment`. Linux calls its atomic integer type `atomic_t`.

`increment(&sequence)` loads the value into a local, calls `compare_and_swap` with that local as expected and the local plus one as new, and repeats while the return differs from the local. A matching return means the store happened, so the increment landed once. Two increments at the same moment cannot both compare against the same old value: the second comparison fails, and it retries against the value the first one wrote.

```c
#include <stdatomic.h>

int compare_and_swap(int *value, int expected, int new_value);  /* the instruction above */

static int sequence = 7;

void increment(int *v)          /* the slides write atomic_int *v */
{
    int temp;
    do {
        temp = *v;
    } while (temp != compare_and_swap(v, temp, temp + 1));
}

void next_ticket(void)
{
    increment(&sequence);   /* 7 becomes 8; a concurrent increment retries */
}
```

That settles a counter and nothing larger. An atomic variable makes one word indivisible, and no instruction updates a whole structure at once. A linked list or a matrix changes through several words, so every word atomic still lets a reader see half an update. For a structure, the answer is a lock around it.

---

Flashcards for this section are as follows:

- what an atomic variable guarantees ::@:: That an update to one basic value, an integer or a boolean, cannot be interrupted or interleaved with another update.
- what Linux calls its atomic integer type ::@:: `atomic_t`.
- how an increment is built from `compare_and_swap` ::@:: Load the value into a local, then call `compare_and_swap` with that local as expected and the local plus one as new, repeating while the return differs from the local.
- signature of `increment()` as the slides define it, and the call that adds one ::@:: `void increment(atomic_int *v)`, also defined by the slides, called as `increment(&sequence)` with `sequence` at `7`: retries `compare_and_swap` until its store lands, leaving `8` and returning nothing.
- why the `compare_and_swap` increment never loses an update ::@:: The store happens only if the word still holds the value the caller read, so a concurrent update makes this call fail and the caller retries on the newer value.
- why an atomic variable cannot protect a whole data structure ::@:: It makes one word indivisible, while a list or a matrix changes through several words, so a reader can still see half of an update.

## mutex locks

A mutex lock is the smallest tool an operating system provides, and most systems build their other locks on it. It holds one boolean saying whether the lock is free. `acquire()` waits for it to say free and then takes it; `release()` sets it free again. Both calls must be atomic, so they rest on the hardware instructions above.

A lock whose wait is a loop is a spinlock: the waiting process repeats the test instead of sleeping. Spinning costs processor cycles and buys one thing, no context switch. A context switch takes time, so on a multiprocessor, with one core spinning while another finishes a short critical section, spinning can cost less than sleeping. That trade needs the lock to be held briefly and another core to make progress meanwhile.

Kernels disable preemption while a spinlock is held, because a holder that gets preempted cannot reach `release()`, and every cycle the spinner spends then waits on a thread that is not running. That guarantee also makes a spinlock work on a single-processor machine: the spinner and the holder cannot both run there, so the wait depends on the holder never losing the only processor.

The Linux kernel offers a spinlock for short sections and a semaphore where a waiting thread should sleep; on a single processor it turns its spinlocks into a kernel preemption switch. Windows exposes mutex locks as dispatcher objects, signaled while free and non-signaled while a thread holds one. A thread that finds one non-signaled blocks.

```c
#include <stdbool.h>

bool test_and_set(bool *target);   /* the hardware instruction, from the section above */

static bool lock = false;   /* false = free, true = held */
static int counter = 0;     /* shared between the threads */

static void acquire(void)
{
    while (test_and_set(&lock))   /* sets lock to true, returns the old value */
        ;                         /* spin until the old value was false */
}

static void release(void)
{
    lock = false;
}

static void increment(void)
{
    acquire();
    counter++;    /* one thread at a time inside this section */
    release();
}
```

The lock covers only what sits inside it. A thread must release it on every path out; one that exits while holding it leaves every other thread waiting forever.

---

Flashcards for this section are as follows:

- what a mutex lock holds ::@:: One boolean that says whether the lock is free.
- what `acquire` and `release` do on a mutex lock ::@:: `acquire` waits until the lock is free and then takes it, and `release` makes it free again. Both must run atomically.
- why a lock that spins is called a spinlock ::@:: A process waiting for it repeats the test in a loop instead of sleeping.
- when spinning for a lock is the right choice ::@:: When the lock is held only briefly on a multiprocessor: one core spins while another finishes the critical section, and no context switch is paid.
- what spinning for a lock costs ::@:: Processor cycles. A spinning process runs and produces nothing, so a long wait belongs on a sleeping lock instead.
- why a kernel disables preemption while holding a spinlock ::@:: A preempted holder cannot reach `release()`, so the spinner burns its cycles on a thread that is not running.
- how a spinlock still works on a single-processor machine ::@:: Preemption stays off while the lock is held, so the holder never loses the only processor and always reaches `release()`.
- prototype of `pthread_mutex_lock()`, and the call that takes the lock ::@:: `int pthread_mutex_lock(pthread_mutex_t *mutex)`, called as `pthread_mutex_lock(&mutex)`: takes the lock, waiting while another thread holds it, and returns `0` or an error number.
- prototype of `pthread_mutex_unlock()`, and the call that frees it ::@:: `int pthread_mutex_unlock(pthread_mutex_t *mutex)`, called as `pthread_mutex_unlock(&mutex)`: releases the lock so the next waiter can enter.
- the names Linux and Windows give a mutex lock ::@:: Linux offers a spinlock for short sections and a semaphore where a waiter should sleep; Windows exposes mutex locks as dispatcher objects, signaled while free and non-signaled while held.
- what happens to the other threads when a thread leaves while still holding a mutual exclusion (mutex) lock ::@:: Every thread that later calls `acquire` on that lock waits forever, because nothing ever sets its boolean back to free.

### adaptive mutex

A fixed choice of spinning or sleeping suits one situation and hurts the other, so an adaptive mutex decides as it waits. On a multiprocessor it spins while the thread holding it runs on another core, because that holder is making progress and should release soon. If the holder keeps the lock for too long, the spinner will waste many cycles, so in practice an adaptive mutex will give up spinning and block after a time or when spinning looks bad. It blocks when the holder is not running, because a thread off the processor may not return for a long time. Solaris builds its mutexes this way.

---

Flashcards for this section are as follows:

- adaptive mutex ::@:: A mutual exclusion (mutex) lock that spins while its holder runs on another core and blocks when the holder is not running or when holding the lock runs long enough that spinning wastes cycles.
- when an adaptive mutex spins ::@:: While the thread holding it runs on another core, where the wait should be short.
- when an adaptive mutex blocks ::@:: When the holder is not running, since a thread off the processor may not return soon, or when the holder keeps the lock long enough that spinning wastes cycles.
- which system uses adaptive mutexes ::@:: Solaris, for its mutexes on a multiprocessor.

## semaphores

A semaphore is an integer that only two atomic operations change, `wait()` and `signal()`. A boolean lock admits one process; an integer admits as many as its count allows, and that count gives the semaphore two jobs.

The first job is mutual exclusion. Shared by several processes and started at one, it admits one process at a time: each waits before its critical section and signals after.

The second job is order. Started at zero, a semaphore makes one process wait until another reaches a named point. The earlier process runs its statement and signals; the later one waits, then continues. The semaphore carries no data, only the fact that the first process arrived.

---

Flashcards for this section are as follows:

- the two jobs a semaphore does in synchronization ::@:: Mutual exclusion, when several processes share it as a lock, and order, when one process signals that it has reached a point another is waiting for.
- how a semaphore makes one statement run before another in a different process ::@:: It starts at zero. The earlier process runs its statement and signals; the later one waits on the semaphore, so it cannot pass until that signal arrives.
- what a semaphore carries besides permission ::@:: A count. It records how many permits are free or how many signals have not yet been taken, so a signal is not lost.
- what initial count lets a semaphore admit one process at a time ::@:: One, with the semaphore shared by several processes: each waits before its critical section and signals after it, so the single permit admits one at a time.

### implementation

A busy-waiting version tests the count in a loop and lowers it only when a permit is free:

```c
typedef struct { int value; } semaphore;

void wait(semaphore *S)
{
    while (S->value <= 0)     /* spin until a permit appears */
        ;
    S->value--;
}

void signal(semaphore *S)
{
    S->value++;
}
```

That version burns a core while it waits, and it is wrong unless the test and the decrement run as one step, since two threads can both see the same permit and both take it. Real systems move the waiting into the kernel, where the count turns negative as waiters queue and a signal wakes one of them. The blocking listing is in [semaphore (programming)](semaphore%20(programming).md#blocking%20implementation).

POSIX exposes the same two operations. A binary semaphore used as a lock looks like this:

```c
#include <semaphore.h>
#include <stddef.h>                /* NULL */

sem_t mutex;                       /* one permit, so a lock */

void init(void)
{
    sem_init(&mutex, 0, 1);
}

void *worker(void *arg)
{
    sem_wait(&mutex);              /* blocks while another thread holds it */
    /* critical section */
    sem_post(&mutex);
    return NULL;
}
```

The operations, the binary and counting forms, the blocking implementation, and the ways a semaphore goes wrong are in [semaphore (programming)](semaphore%20(programming).md).

---

Flashcards for this section are as follows:

- what the busy-waiting `wait()` of a semaphore does ::@:: It spins while the count is at most zero, then lowers the count to take a permit.
- why the busy-waiting semaphore needs atomicity ::@:: The test and the decrement are separate steps, so two threads can both see the same permit and both take it.
- how the blocking semaphore implementation avoids spinning ::@:: The count goes negative as waiters queue, `wait` blocks instead of looping, and `signal` wakes the first queued waiter.
- behaviour of the POSIX calls on an unavailable semaphore ::@:: `sem_wait(&s)` blocks until another thread posts, and `sem_post(&s)` raises the count and wakes a waiter if one is queued.
- prototype of `sem_init()`, and the call that makes a binary semaphore ::@:: `int sem_init(sem_t *sem, int pshared, unsigned int value)`, called as `sem_init(&mutex, 0, 1)`: `&mutex` names the semaphore, `pshared` `0` so only threads of this process share it, and `value` `1` starts the count at one, which makes it a lock.
- prototype of `sem_wait()`, and the call that takes the permit ::@:: `int sem_wait(sem_t *sem)`, called as `sem_wait(&mutex)`: lowers the count by one, blocking while it is zero, and returns `0` or `-1` with `errno` set.
- prototype of `sem_post()`, and the call that returns it ::@:: `int sem_post(sem_t *sem)`, called as `sem_post(&mutex)`: raises the count and wakes a waiter.

## condition variables

A condition variable lets a thread sleep until shared state changes instead of spinning on it. It is always paired with a mutex that protects the state being tested.

A waiting thread calls `wait(&cond, &mutex)`, which releases the mutex and blocks the caller in one atomic step, then re-acquires the mutex before returning. `signal(&cond)` wakes one waiter, and `broadcast(&cond)` wakes all of them. The Portable Operating System Interface (POSIX) names them `pthread_cond_wait`, `pthread_cond_signal`, and `pthread_cond_broadcast`.

The declarations:

```c
#include <pthread.h>

int pthread_cond_wait(pthread_cond_t *cond, pthread_mutex_t *mutex);
int pthread_cond_signal(pthread_cond_t *cond);
int pthread_cond_broadcast(pthread_cond_t *cond);
```

Two workers wait on one condition variable: a single work item arrives, and then a shutdown flag releases both.

```c
#include <pthread.h>

pthread_cond_t cond = PTHREAD_COND_INITIALIZER;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
int ready, done;

void *worker(void *arg)
{
    pthread_mutex_lock(&mutex);
    for (;;) {
        while (!ready && !done)              /* both flags are tested */
            pthread_cond_wait(&cond, &mutex);
        if (!ready)                          /* done, and nothing left to do */
            break;
        ready--;                             /* take one item */
        pthread_mutex_unlock(&mutex);
        /* the work runs outside the mutex */
        pthread_mutex_lock(&mutex);
    }
    pthread_mutex_unlock(&mutex);
    return NULL;
}

int main(void)
{
    pthread_t a, b;
    pthread_create(&a, NULL, worker, NULL);
    pthread_create(&b, NULL, worker, NULL);

    pthread_mutex_lock(&mutex);
    ready = 1;
    pthread_cond_signal(&cond);             /* one item, so one waiter is enough */
    pthread_mutex_unlock(&mutex);

    pthread_mutex_lock(&mutex);
    done = 1;
    pthread_cond_broadcast(&cond);          /* shutdown reaches both waiters */
    pthread_mutex_unlock(&mutex);

    pthread_join(a, NULL);
    pthread_join(b, NULL);
    return 0;
}
```

Only the wait takes the mutex, and it requires that mutex to be held. The two wake calls may be made with or without it.

`ready` and `done` are both flags under `mutex`, tested together because a wake does not say which one changed. `done` is the shutdown request: a worker leaves only once it is set and no item is left, and that is the only way out of the loop. Without it the two workers would sleep forever once the item had been taken. Taking the item first lets an early shutdown still drain the work.

The wait takes the mutex as a parameter because it must release and re-take it. While a waiter sleeps, the thread that changes the state needs that mutex; a waiter that kept it would shut the changer out and never be woken.

A wake proves only that the state may have changed. Another waiter can reach the mutex first and take what this one wanted, so the thread tests again in a loop:

```c
pthread_mutex_lock(&mutex);
while (!ready)                       /* re-tested after every wake */
    pthread_cond_wait(&cond, &mutex);
/* ready is true and the mutex is held */
pthread_mutex_unlock(&mutex);
```

The `while` makes that correct. An `if` is a bug that shows up only when two waiters share one condition.

A condition variable has no value and remembers nothing, so a signal sent while nobody waits is lost. A semaphore keeps a count, so a signal sent early is remembered and the next wait passes at once. A semaphore therefore orders two events separated in time; a condition variable only tells a thread to look again.

---

Flashcards for this section are as follows:

- what a condition variable lets a thread do ::@:: Sleep until another thread signals that a shared state may have changed, then wake and test the state again.
- what a condition variable is always used with ::@:: A mutex, which protects the shared state the waiting thread tests.
- what the `done` flag adds to a condition-variable loop ::@:: The shutdown request. A waiter tests it beside the work flag and leaves when it is set instead of sleeping again; that is the only exit.
- what waiting on a condition variable does to its mutex ::@:: The call releases the mutex before the thread sleeps and re-acquires it before returning, so the caller holds the mutex whenever it runs outside the wait.
- why a wait must release the mutex it holds ::@:: Otherwise the thread that has to change the state could not take the mutex to change it or to signal, and the waiter would never wake.
- why a thread re-tests its condition after a wake ::@:: A wake only says the state may have changed, and another waiter may have taken what this one wanted first, so the thread tests again and waits again if the condition is still false.
- why a waiter tests every flag after one wake ::@:: A wake says the state may have changed, not which part, so the loop re-tests each flag it depends on.
- what `signal` and `broadcast` do on a condition variable ::@:: `signal` wakes one waiting thread and `broadcast` wakes every thread waiting on the condition variable.
- what a broadcast wakes, and why the waiters do not return at the same moment ::@:: Every waiter on the condition variable. Each must re-acquire the mutex before its wait returns, so the returns come one after another.
- how a signal and a broadcast differ for two waiters that each release the mutex at once ::@:: A signal returns from one wait and a broadcast from both, and the returns come one after the other because each waiter must take the mutex first. Only the work after the release overlaps.
- how a condition variable differs from a semaphore ::@:: A condition variable has no value and remembers no signal, so a signal sent with nobody waiting is lost, while a semaphore counts and a signal sent early lets a later wait pass.
- the Portable Operating System Interface (POSIX) functions that wait on a condition variable and wake its waiters ::@:: `pthread_cond_wait` waits on it, `pthread_cond_signal` wakes one waiter, and `pthread_cond_broadcast` wakes all of them.
- why the thread that signals a condition variable holds the mutex while it changes the shared state ::@:: So no waiter can test the old state and then sleep through the change.

### waking waiters

The signaller changes the state under the mutex; where the signal goes is a separate question. Sent while the mutex is held, it is safe by construction: the change and the wake stay ordered, so no waiter tests the old state and then sleeps through the signal. The cost is a round trip, since the woken thread becomes runnable, finds the mutex held by the signaller, and blocks again. That is hurry-up-and-wait. Sent after the unlock, the waiter takes the mutex at once.

POSIX allows either placement. The outside one is correct here because the predicate changes only under the mutex and every waiter re-tests in a `while`, so a signal that reaches nobody leaves a state the next test sees. Some implementations remove the round for code that signals inside the lock: wait morphing moves the waiter onto the mutex's wait queue while the signaller still holds it, so the waiter does not run until the mutex is free. glibc's earlier native threads library did this with a futex requeue; a library without the trick pays the round.

`signal` and `broadcast` differ in what the change releases. Waking several looks odd while the wake leads to the mutex, which admits one thread at a time; what each woken thread finds after taking the mutex settles it. A broadcast suits a state that lets several proceed: a shutdown flag every worker must see, or a buffer with room for more than one item. A single wake hands the mutex to one thread, which takes its item or sees the flag and leaves, while the rest sleep on although the state they wait for is already true. The price is the thundering herd, where every waiter runs, re-tests, and sleeps again unless it can go on.

Two waiters show the difference. One work item arrives, and `signal` returns from one `wait`. At shutdown, `broadcast` returns from both, but not together: the first takes the mutex, finds `done`, releases it, and only then does the second return. Each leaves the mutex as soon as it can, so the calls differ by one return against two, not by two threads running at once. What each does after that release can overlap, which is where the extra concurrency appears.

---

Flashcards for this section are as follows:

- signature of `pthread_cond_wait()`, and the call the waiter makes ::@:: `int pthread_cond_wait(pthread_cond_t *cond, pthread_mutex_t *mutex)`, called as `pthread_cond_wait(&cond, &mutex)`: `cond` is the condition and `mutex` the lock the caller holds, which the call releases and re-takes in one atomic step. The predicate is re-tested in a `while` loop.
- signature of `pthread_cond_signal()`, and the call that wakes one waiter ::@:: `int pthread_cond_signal(pthread_cond_t *cond)`, called as `pthread_cond_signal(&cond)`: wakes one waiter on that condition.
- signature of `pthread_cond_broadcast()`, and the call that wakes every waiter ::@:: `int pthread_cond_broadcast(pthread_cond_t *cond)`, called as `pthread_cond_broadcast(&cond)`: wakes every waiter, which is what the shutdown round needs.
- signature of `pthread_create()`, and the call that starts a worker ::@:: `int pthread_create(pthread_t *tid, const pthread_attr_t *attr, void *(*start_routine)(void *), void *arg)`, called as `pthread_create(&a, NULL, worker, NULL)`: starts `worker` on a new thread with default attributes and no argument. The call with `&b` starts the second worker.
- signature of `pthread_join()`, and the call that waits for a worker to end ::@:: `int pthread_join(pthread_t tid, void **ret)`, called as `pthread_join(a, NULL)`: waits for that thread to end and discards its return value.
- which condition-variable call requires the mutex to be held ::@:: Only `pthread_cond_wait()`. The signal and the broadcast may be called with or without it.
- what signal sent inside the lock costs the woken thread ::@:: One round trip: it becomes runnable, finds the mutex still held, and blocks again, which is hurry-up-and-wait.
- why signalling after the unlock is safe ::@:: The predicate changes only under the mutex and every waiter re-tests in a `while`, so a signal that reaches nobody leaves a state the next test finds.
- what wait morphing does when a signaller holds the mutex ::@:: It moves the waiter onto the mutex's wait queue, so it runs only once the mutex is free.
- when a broadcast is needed although the mutex admits one thread at a time ::@:: When the change lets several waiters proceed in turn, such as a shutdown flag or room for more than one item. One wake would leave the rest asleep on a state that is already true.
- what a broadcast costs ::@:: The thundering herd: every waiter runs, re-tests its predicate, and goes back to sleep unless it can proceed.
