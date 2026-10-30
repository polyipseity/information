---
aliases:
  - POSIX Threads
  - POSIX threads
  - pthreads
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/pthreads
  - language/in/English
---

# pthreads

POSIX Threads, or pthreads, is the interface a C program uses to run several threads inside one process. The calls sit in `<pthread.h>`. The standard fixes what each call does, not how it is built, so every UNIX-like system supplies its own library under the same names.

A thread shares its process's memory with the other threads. That sharing makes starting one cheap and forces the threads to synchronize. A program begins with the initial thread in `main`, which creates the rest; each new thread runs a function of its own, and the creator waits for the others before reading what they produced.

---

Flashcards for this section are as follows:

- POSIX Threads (pthreads) ::@:: The interface a C program uses to create and synchronize threads inside one process. The POSIX standard fixes the calls, and each system supplies a library behind them.
- what a thread made through POSIX Threads (pthreads) shares with the others in its process ::@:: The process's memory, so a variable one thread writes is visible to the others.
- the two consequences of a thread sharing its process's memory ::@:: Starting a thread is cheap, and the threads need synchronization.
- the shape every threaded program follows ::@:: The initial thread in `main` creates the others; each runs a function of its own, and the creator waits for them before reading what they produced.
- header that declares the POSIX Threads (pthreads) calls ::@:: `<pthread.h>`.

## thread handles and creation

A thread is named by a `pthread_t` value. The creator declares one and passes its address for `pthread_create` to fill in; every later call on that thread passes the same value.

`pthread_create` takes four arguments: the address for the identifier, the attributes, the function where the new thread begins, and the argument handed to it.

```c
#include <pthread.h>

int pthread_create(pthread_t *thread,
                   const pthread_attr_t *attr,
                   void *(*start_routine)(void *),
                   void *arg);
```

The start routine has the fixed type `void *(*)(void *)`, one `void *` in and one out. The interface cannot know what a program passes, so it moves an address and lets the thread interpret it.

Attributes live in a `pthread_attr_t`, which holds the stack size and scheduling information. `pthread_attr_init` fills it with defaults; `NULL` for the attributes asks for the same ones.

---

Flashcards for this section are as follows:

- type that names one POSIX Threads (pthreads) thread ::@:: `pthread_t`. The creator declares one, and `pthread_create()` fills it in.
- prototype of `pthread_create()`, and the call that starts the first thread ::@:: `int pthread_create(pthread_t *tid, const pthread_attr_t *attr, void *(*start)(void *), void *arg)`, called as `pthread_create(&tid, NULL, returned, (void *) "done")`: `&tid` receives the identifier, `NULL` picks default attributes, `returned` is where the thread starts, and `(void *) "done"` is the one pointer it gets; returns `0` or an error number.
- type of a POSIX Threads (pthreads) start routine, and why it takes a `void *` ::@:: `void *(*)(void *)`, one `void *` in and one out, so the interface can carry an argument and a result of any type.
- how a thread that receives a pointer converts it back to its own type ::@:: It casts the `void *` back to the pointer type its creator passed.
- which argument passes into and out of a POSIX Threads (pthreads) start routine without a cast ::@:: A `char *` such as `argv[1]` of `main()`; any other type takes a cast in and a cast out.
- what `pthread_attr_init(&attr)` fills, and what passing `NULL` for the attributes means ::@:: The attributes a new thread gets when the caller changes nothing: stack size, scheduling policy and the like. `NULL` for the attributes argument of `pthread_create()` asks for those defaults.
- what a `pthread_attr_t` holds ::@:: A thread's attributes, such as its stack size and scheduling information.

### void pointer argument

`void *` is an address with no type attached, so it can point at anything. It holds the address of an `int` or a structure, and the compiler stops checking what sits there. It cannot hold the object itself, so the thread interface passes addresses, never values.

Size decides this. A call must know how many bytes each argument takes into the callee, and a pointer is one address wide, which both sides know. The object behind it has a size only its type gives, and the type is what the interface lacks.

The thread casts the address back to the type its creator used. Nothing checks that cast, so a wrong one compiles. `char *` needs no cast either way, since it converts to `void *` and back implicitly; every other pointer type takes one cast in and one out.

An integer can travel through the same argument: cast it to `intptr_t`, wide enough to hold a pointer, and cast back inside the thread. Whatever the address points at must outlive the read, so a local of the creating function is safe only until that function returns.

---

Flashcards for this section are as follows:

- what `void *` means as a type ::@:: A pointer to anything: an address with no type attached that holds any object's address while the compiler stops checking what is stored there.
- why a thread interface passes arguments as `void *` instead of by value ::@:: A call must know each argument's size, and a pointer has one fixed width that both sides know, while an object of unknown type gives no size to copy.
- what the start routine does with the `void *` it receives ::@:: It casts the pointer back to the type the creating thread passed, and the cast is not checked at compile time.
- pointer type that converts to `void *` and back without a cast ::@:: `char *`, so a string such as `argv[1]` passes through unchanged. Every other pointer type needs a cast in each direction.
- how an integer travels through a `void *` argument ::@:: By a cast to `intptr_t`, an integer type wide enough to hold a pointer, and a cast back inside the thread.
- how long the object behind a thread argument must live ::@:: As long as the thread reads it, so a local of the creating function is safe only until that function returns.

## joining and ending a thread

A join tells the reader the writer has finished; without one, `main` may read a value before the thread that writes it has run, and the output then depends on the schedule.

`pthread_join(tid, NULL)` waits for the thread named by `tid` to terminate; its second argument can receive the value the thread returned. A thread ends by returning from its start routine or calling `pthread_exit(0)`, and either makes the join return. A program joins several threads in a loop, one identifier per call.

```c
#include <pthread.h>

int pthread_join(pthread_t thread, void **retval);   /* 0, or an error number */
int pthread_detach(pthread_t thread);                /* 0, or an error number */
void pthread_exit(void *retval);                     /* never returns */
```

Joining collects the pointer the thread handed back; detaching gives that up on purpose:

```c
#include <pthread.h>

void *returned(void *arg)
{
    return arg;                   /* the join collects this pointer */
}

int main(void)
{
    pthread_t tid;
    void *ret;

    pthread_create(&tid, NULL, returned, (void *) "done");
    pthread_join(tid, &ret);      /* &ret receives "done" */
    return 0;
}
```

```c
#include <pthread.h>

void *idle(void *arg)
{
    pthread_exit(arg);            /* hands arg to a joiner, then ends */
}

int main(void)
{
    pthread_t tid;
    if (pthread_create(&tid, NULL, idle, NULL) != 0)
        return 1;
    pthread_detach(tid);          /* no thread will ever join it */
    pthread_exit(NULL);           /* ends this thread, not the process */
}
```

`retval` is where the joiner receives the thread's exit value, and nothing ever joins a detached thread.

---

Flashcards for this section are as follows:

- what `pthread_join(tid, NULL)` does ::@:: It waits for the thread named by `tid` to terminate; the second argument can receive the value the thread returned.
- prototype of `pthread_join()`, and the call that collects the result ::@:: `int pthread_join(pthread_t thread, void **retval)`, called as `pthread_join(tid, &ret)`: waits for that thread and copies the pointer it returned through `&ret`; `NULL` for the second argument discards the value. Returns `0` or an error number.
- prototype of `pthread_detach()`, and what the call gives up ::@:: `int pthread_detach(pthread_t tid)`, called as `pthread_detach(tid)`: gives up the join, so no thread waits for the value and the resources are freed when the thread ends.
- prototype of `pthread_exit()`, and the call that ends the detached thread ::@:: `void pthread_exit(void *ret)`, called as `pthread_exit(NULL)`: ends this thread only and leaves nothing for a joiner, so the process keeps running.
- two ways a POSIX Threads (pthreads) thread ends ::@:: It returns from its start routine, or calls `pthread_exit(0)`.
- why a thread is joined before its result is used ::@:: The join marks the point where the thread has finished, so without it the main thread may run first and the output depends on the schedule.
- how a program waits for several threads ::@:: It calls `pthread_join()` once per thread identifier, in a loop.

### return values

The start routine hands back a `void *`, by returning it or passing it to `pthread_exit`, and `pthread_join` copies it into the place named by its second argument: a `void **`, the address of a `void *` variable for the join to fill.

```c
struct result { int sum; };

void *work(void *arg)
{
    struct result *r = malloc(sizeof *r);

    r->sum = 42;
    return r;                  /* the thread's result */
}

int main(void)
{
    pthread_t tid;
    void *ret;                 /* receives the result */

    pthread_create(&tid, NULL, work, NULL);
    pthread_join(tid, &ret);
    struct result *r = (struct result *) ret;
    ...
    free(ret);                 /* the joiner owns the block now */
}
```

The thread's own stack cannot hold the result: a local dies when the start routine returns, so the address it hands back points at memory the thread no longer owns. Put the result in a `malloc` block the joiner frees, in a static object, or in a structure the joiner already owns.

The join consumes the value, so collect it once. The standard does not define joining the same thread twice; a program that needs the value in two places saves it after the first join.

Returning `NULL` is legal and means no result, though the joiner cannot tell that from a thread that returned a null pointer. A cancelled thread returns `PTHREAD_CANCELED`, a value to test against.

A detached thread keeps no result, since no join will ask for one; `pthread_detach` tells the implementation to reclaim the thread itself.

---

Flashcards for this section are as follows:

- type of the value a POSIX Threads (pthreads) thread returns ::@:: `void *`, the same pointer type the start routine takes as its argument.
- two ways a thread hands back its result ::@:: It returns the pointer from its start routine, or passes it to `pthread_exit()`.
- type of the second argument of `pthread_join()`, and what it receives ::@:: A `void **`, the address of a `void *` variable that the join fills with the pointer the thread returned.
- where a returned thread pointer has to point ::@:: At memory that outlives the thread: a `malloc` block the joiner frees, a static object, or a structure the joiner already owns.
- why a thread cannot return the address of its local variable ::@:: The local dies when the start routine returns, so the address points at memory the thread no longer owns.
- how many times a thread's result can be collected ::@:: Once. The join consumes it, and the standard does not define joining the same thread again.
- what `pthread_join()` receives from a thread that returned `NULL` and from a cancelled thread ::@:: `NULL` for the thread that returned no result, and `PTHREAD_CANCELED` for the cancelled one, a distinct value to test against.
- what happens to a detached thread's result ::@:: Nothing is kept, because no join asks for it. `pthread_detach()` lets the implementation reclaim the thread when it ends; it must not be joined.

## synchronization

### mutex

A mutex gives mutual exclusion to the threads of one process. The type is `pthread_mutex_t`; the four calls are `pthread_mutex_init`, `pthread_mutex_lock`, `pthread_mutex_unlock` and `pthread_mutex_destroy`; and around the shared resource the order is lock, access, unlock.

A thread receives its mutex as an argument: an address passed to `pthread_create`, which arrives as a `void *` and is cast back to `pthread_mutex_t *` before the lock calls use it.

```c
void *add(void *arg)
{
    pthread_mutex_t *m = (pthread_mutex_t *) arg;

    pthread_mutex_lock(m);
    /* critical section */
    pthread_mutex_unlock(m);
    return NULL;
}
```

A thread that dies while holding a mutex leaves it held, and every other thread wanting it blocks.

```c
#include <pthread.h>

int pthread_mutex_init(pthread_mutex_t *mutex, const pthread_mutexattr_t *attr);
int pthread_mutex_lock(pthread_mutex_t *mutex);
int pthread_mutex_unlock(pthread_mutex_t *mutex);
int pthread_mutex_destroy(pthread_mutex_t *mutex);
```

A mutex is initialised, taken around the change, released, and destroyed last:

```c
#include <pthread.h>

pthread_mutex_t mutex;

int guarded_increment(int *shared)
{
    if (pthread_mutex_init(&mutex, NULL) != 0)   /* NULL: the default attributes */
        return -1;
    pthread_mutex_lock(&mutex);
    *shared += 1;                                /* the invariant changes here */
    pthread_mutex_unlock(&mutex);
    return pthread_mutex_destroy(&mutex);        /* 0 only with no holder left */
}
```

Each returns 0 or an error number and leaves `errno` alone; `attr` may be `NULL` for the default attributes.

---

Flashcards for this section are as follows:

- mutex in POSIX Threads (pthreads) ::@:: A lock that lets one thread at a time into a critical section, with one shared resource per mutex.
- prototype of `pthread_mutex_init()`, and the call the guarded program makes ::@:: `int pthread_mutex_init(pthread_mutex_t *mutex, const pthread_attr_t *attr)`, called as `pthread_mutex_init(&mutex, NULL)`: fills the mutex and gives it the default attributes, since `NULL` names none; a mutex that lives as long as the program skips the call and starts as `PTHREAD_MUTEX_INITIALIZER`.
- prototype of `pthread_mutex_lock()`, and the call around the change ::@:: `int pthread_mutex_lock(pthread_mutex_t *mutex)`, called as `pthread_mutex_lock(&mutex)`: takes the lock, waiting while another thread holds it, and returns `0` or an error number.
- prototype of `pthread_mutex_unlock()`, and the call that ends the section ::@:: `int pthread_mutex_unlock(pthread_mutex_t *mutex)`, called as `pthread_mutex_unlock(&mutex)`: releases the lock and returns `0` or an error number.
- prototype of `pthread_mutex_destroy()`, and when the program calls it ::@:: `int pthread_mutex_destroy(pthread_mutex_t *mutex)`, called as `pthread_mutex_destroy(&mutex)`: frees the mutex once nobody holds or waits for it, and returns `0` or an error number.
- the order a thread follows around a mutex ::@:: Lock the mutex, access the shared resource, unlock the mutex.
- how a mutex reaches the thread that locks it ::@:: As an address passed to `pthread_create()`, which arrives in the start routine as a `void *` and is cast back to `pthread_mutex_t *`.
- what happens to other threads when one dies while holding a mutex ::@:: They block forever, because nothing releases the lock.

### condition variable

A condition variable lets a thread wait for a change of state, and it always travels with a mutex that protects that state. The type is `pthread_cond_t`, and its calls are `pthread_cond_init`, `pthread_cond_wait`, `pthread_cond_signal`, `pthread_cond_broadcast` and `pthread_cond_destroy`; a signal wakes one waiter and a broadcast wakes all of them.

`pthread_cond_wait(&cond, &mutex)` releases the mutex and blocks the caller in one atomic step, so another thread can take the mutex and change the shared state. Done separately, they leave a gap: a signal between the release and the sleep finds no waiter, and the thread sleeps on after its condition has come true. When the signal arrives the waiter wakes, takes the mutex back, and returns.

The waiter re-reads the flag in a `while` loop after each return, since a wake says only that something changed and its own condition may still be false.

```c
pthread_mutex_lock(&mutex);
while (!ready) {
    pthread_cond_wait(&cond, &mutex);
}
pthread_mutex_unlock(&mutex);
```

A waiting thread sleeps instead of spinning, so the processor runs other work.

```c
#include <pthread.h>

int pthread_cond_init(pthread_cond_t *cond, const pthread_condattr_t *attr);
int pthread_cond_wait(pthread_cond_t *cond, pthread_mutex_t *mutex);
int pthread_cond_destroy(pthread_cond_t *cond);
```

The wait takes the mutex as its second argument, releases it and blocks as one step, then re-acquires it before returning; all three return 0 or an error number.

---

Flashcards for this section are as follows:

- condition variable in POSIX Threads (pthreads) ::@:: An object on which a thread waits for a change of state, always paired with a mutex that protects that state.
- prototype of `pthread_cond_init()`, and the call that sets up the condition ::@:: `int pthread_cond_init(pthread_cond_t *cond, const pthread_attr_t *attr)`, called as `pthread_cond_init(&ready, NULL)`: fills the condition variable with the default attributes, and a static one starts as `PTHREAD_COND_INITIALIZER` instead.
- prototype of `pthread_cond_wait()`, and the call the waiter makes ::@:: `int pthread_cond_wait(pthread_cond_t *cond, pthread_mutex_t *mutex)`, called as `pthread_cond_wait(&ready, &mutex)`: releases the mutex and sleeps in one step, then re-takes the mutex on the way out.
- prototype of `pthread_cond_signal()`, and the call for the single waiter ::@:: `int pthread_cond_signal(pthread_cond_t *cond)`, called as `pthread_cond_signal(&ready)`: wakes one waiter and returns `0` or an error number.
- prototype of `pthread_cond_broadcast()`, and why the second round calls it ::@:: `int pthread_cond_broadcast(pthread_cond_t *cond)`, called as `pthread_cond_broadcast(&ready)`: wakes every waiter on that condition and returns `0` or an error number.
- prototype of `pthread_cond_destroy()`, and when the program calls it ::@:: `int pthread_cond_destroy(pthread_cond_t *cond)`, called as `pthread_cond_destroy(&ready)`: frees the condition variable once no thread waits on it, and returns `0` or an error number.
- what `pthread_cond_wait(&cond, &mutex)` does in one atomic step ::@:: It releases the mutex and blocks the caller, so another thread can take the mutex and change the shared state.
- why the release and the sleep must be one step in `pthread_cond_wait()` ::@:: Separated, they leave a gap where a signal finds no waiter and is lost, so the thread sleeps while the condition it waited for already holds.
- what a signalled thread does before `pthread_cond_wait()` returns ::@:: It wakes, takes the mutex back, then returns from the call.
- why a waiter re-reads its flag in a loop ::@:: The signal does not say which state was reached, so the thread waits again unless its condition is true.
- difference between `pthread_cond_signal()` and `pthread_cond_broadcast()` ::@:: `pthread_cond_signal()` wakes one waiting thread, and `pthread_cond_broadcast()` wakes all of them.
- why waiting on a condition variable wastes less processor time than spinning ::@:: A waiting thread sleeps and gives the processor back, while a spinning thread keeps testing the flag.
- which thread changes the state a condition variable waits on ::@:: Another thread, holding the same mutex, sets the flag, signals the condition, then releases the mutex.

### signal and broadcast

`pthread_cond_wait` must be called with the mutex held, and it releases that mutex while the thread sleeps. `pthread_cond_signal` and `pthread_cond_broadcast` may be called with or without it, and neither releases one the caller holds.

Signalling while holding the mutex is the usual habit, and the safe one, at a small cost. The woken thread becomes runnable, finds the mutex held, and blocks again, so a wake and a sleep pass with nothing done. That is hurry-up-and-wait. Signalling after the unlock lets the waiter take the mutex at once. Some implementations skip the round trip: wait morphing moves the waiter from the condition variable onto the mutex's wait queue while the signaller holds the mutex, so it runs only when the mutex is free. glibc's earlier native threads library did this through a futex requeue; a library without the trick pays the round.

Correctness is a separate question. A signal sent inside the mutex is ordered after the change to the predicate and before the unlock, so no waiter can test the old state and sleep through it. A signal sent outside works when the predicate changes only under the mutex and every waiter re-tests in a `while`: a signal that reaches nobody leaves a state the next test sees. It breaks when the predicate changes outside the mutex, or when a waiter tests once with `if`, since the signal can land between the test and the sleep.

How many waiters the change releases decides the call. `pthread_cond_signal` wakes one, which suits a resource one thread can consume, such as a single slot or item. `pthread_cond_broadcast` wakes every waiter, which a change that lets several proceed at once needs, such as a shutdown flag or a state they can all act on. Each waiter still takes the mutex in turn, so [the returns happen one after another](synchronization%20(computer%20science).md#waking%20waiters). A broadcast also covers waiters sharing one condition variable while testing different predicates, where a single wake may reach a thread that cannot go on. Broadcasting costs a thundering herd: every waiter runs, re-tests, and goes back to sleep unless it can proceed, and each wakeup costs a context switch.

```c
int pthread_cond_signal(pthread_cond_t *cond);      /* wakes one waiter */
int pthread_cond_broadcast(pthread_cond_t *cond);   /* wakes every waiter */
```

One thread waits on a flag, and the signaller sets it: a single wake for one waiter, a broadcast for two.

```c
#include <pthread.h>

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t ready;
int done;

void *waiter(void *arg)
{
    pthread_mutex_lock(&mutex);
    while (!done)                            /* re-tested after every wake */
        pthread_cond_wait(&ready, &mutex);   /* releases the mutex, then re-takes it */
    pthread_mutex_unlock(&mutex);
    return NULL;
}

int main(void)
{
    pthread_t one, two;

    if (pthread_cond_init(&ready, NULL) != 0)   /* NULL: the default attributes */
        return 1;

    pthread_create(&one, NULL, waiter, NULL);
    pthread_mutex_lock(&mutex);
    done = 1;
    pthread_cond_signal(&ready);                /* one waiter, so one wake */
    pthread_mutex_unlock(&mutex);
    pthread_join(one, NULL);

    done = 0;                                   /* a second round with two waiters */
    pthread_create(&one, NULL, waiter, NULL);
    pthread_create(&two, NULL, waiter, NULL);
    pthread_mutex_lock(&mutex);
    done = 1;
    pthread_cond_broadcast(&ready);             /* both waiters wake */
    pthread_mutex_unlock(&mutex);

    pthread_join(one, NULL);
    pthread_join(two, NULL);
    return pthread_cond_destroy(&ready);        /* 0 once nobody waits */
}
```

Neither call takes or releases the mutex.

---

Flashcards for this section are as follows:

- where POSIX allows `pthread_cond_signal()` to be called, compared with `pthread_cond_wait()` ::@:: The signal may be sent with or without the mutex held, while the wait must be called with it held.
- what `pthread_cond_wait()` does to the mutex that `pthread_cond_signal()` does not ::@:: The wait releases the mutex while the thread sleeps and re-acquires it before returning. The signal never releases a mutex.
- what holding the mutex while signalling costs ::@:: The woken thread runs, finds the mutex held, and blocks again, so a wake and a sleep pass with nothing done between them.
- what wait morphing saves ::@:: The trip back to a blocked state: the waiter moves onto the mutex's wait queue while the signaller holds the mutex, so it runs only once the mutex is free.
- which thread library used a futex requeue to implement wait morphing ::@:: glibc's earlier native threads library, which moved a waiter onto the mutex's queue through `lll_futex_cmp_requeue_pi`.
- why a signal sent inside the mutex is safe by construction ::@:: The predicate changes under the mutex and the signal is ordered between that change and the unlock, so no waiter tests the old state and sleeps through it.
- when a signal sent outside the mutex is still correct ::@:: When the predicate changes only under the mutex and every waiter re-tests in a `while`, so a signal that reaches nobody leaves a state the next test sees.
- what `pthread_cond_broadcast()` is for, compared with `pthread_cond_signal()` ::@:: Waking every waiter, which a change that lets several proceed at once needs, such as a shutdown flag or a state they can all act on.
- thundering herd as the cost of broadcasting ::@:: Every waiter wakes, re-tests its predicate, and goes back to sleep unless it can proceed, so each wakeup costs a context switch with nothing behind it.
- when one condition variable carries waiters that test different predicates ::@:: Broadcasting is the safe choice, since `pthread_cond_signal()` may wake a thread whose own predicate is still false.

## practices

### mutex practice

A mutex protects an invariant, so the critical section covers that invariant and nothing else. Every line inside keeps the other threads out, so work that does not touch the protected data belongs outside: build the value before the lock, use it after the unlock. Waiting for another thread, doing I/O, or taking a second lock inside stalls every thread that wants the mutex.

One mutex per set of invariants beats one mutex per variable. Variables that must change together need the same lock, or a reader catches half a change; unrelated variables can have separate locks, so threads on different data do not queue behind each other. A program that holds two locks needs one order for all of them, fixed once and followed everywhere. The opposite order in another thread deadlocks as soon as the timing lines up.

Initialise the mutex before any thread can reach it. The unlock belongs on every path, the early return and the error branch included; a mutex held by a thread that leaves never reaches the others. The lock calls can fail, and a thread that ignores a failed `pthread_mutex_lock` carries on without the exclusion it believes it holds.

---

Flashcards for this section are as follows:

- what a mutex critical section should contain ::@:: The reads and writes of the invariant it protects, and nothing else, since every line inside keeps the other threads out.
- work that must stay outside a mutex ::@:: Waiting for another thread, doing I/O, and taking a second lock, since each one stalls every thread that wants the mutex.
- how many mutexes one shared state needs ::@:: One per set of variables that must change together, while unrelated variables can have separate locks so their threads do not queue behind each other.
- rule for taking two mutexes ::@:: Fix one order for all mutexes and follow it everywhere, because the opposite order in another thread deadlocks once the timing lines up.
- two mutex mistakes at the end of a critical section ::@:: Leaving it locked on an early return or an error path, and destroying it while a thread still holds or waits for it.
- why the return value of `pthread_mutex_lock()` is checked ::@:: The call can fail, and a thread that ignores the failure continues without the exclusion it believes it holds.

### condition practice

What a condition variable waits for lives in the predicate, not in the variable. The predicate is state under the mutex, the wait sits in a `while`, and the thread that changes the state holds the same mutex, so the test, the change and the signal stay ordered.

Send the signal once the predicate is true, preferably while the mutex is still held, which keeps the change and the wake in one order. Each reason to wait gets its own condition variable, so a signal reaches waiters that can act on it. `pthread_cond_broadcast` covers what a single wake cannot: several waiters able to act at once, or one variable serving several predicates.

A waiting thread also needs a way out. Shutdown is the usual one: a `done` flag under the same mutex, broadcast when it is set, with a loop that checks the flag as well as its own predicate. Without it a thread waits forever, and a program that stops signalling before its workers finish hangs at exit.

---

Flashcards for this section are as follows:

- where a condition variable's predicate lives ::@:: In shared state protected by the same mutex, so the test, the change and the signal stay ordered.
- why a condition wait sits in a `while` rather than an `if` ::@:: The signal says only that something changed, so the thread re-tests its predicate and goes back to sleep after a wake it cannot use.
- when a thread signals a condition variable ::@:: After it has made the predicate true, while it still holds the mutex, so the change and the wake reach waiters in one order.
- how many condition variables one mutex should have ::@:: One per reason to wait, so each signal wakes waiters that can act on it.
- how a waiting thread is told to stop ::@:: Through a `done` flag under the same mutex, broadcast when it is set, with the wait loop checking the flag as well as its own predicate.
- what happens when a program stops signalling before its waiters finish ::@:: The waiting threads never wake, so the program hangs at exit even though the work is done.

## building and linking

The thread calls live in a separate library, so the link step names it.

```bash
gcc demo.c -pthread -o demo
```

`-pthread` adds the compiler and linker settings a threaded program needs. `-lpthread` names only the library, without those settings.

---

Flashcards for this section are as follows:

- flag that builds a program using POSIX Threads (pthreads) with the settings the library needs ::@:: `-pthread`, as in `gcc demo.c -pthread -o demo`.
- library behind the POSIX Threads (pthreads) calls, and the flag that names it alone ::@:: The library is `libpthread`, named by `-lpthread`.
- why a threaded program needs anything in its link step ::@:: The thread calls live in a separate library, so the executable has to be linked against it.
