---
aliases:
  - COMP 3031 Scala futures and promises
  - COMP3031 Scala futures and promises
  - HKUST COMP 3031 Scala futures and promises
  - HKUST COMP3031 Scala futures and promises
  - Scala futures and promises
tags:
  - flashcard/active/special/academia/HKUST/COMP_3031/futures_and_promises
  - language/in/English
---

# Scala futures and promises

- HKUST COMP 3031

---

- see: [general/futures and promises](../../../../general/futures%20and%20promises.md)

{@{_Asynchronous programming_}@} lets a program start {@{a long‑running task on another thread and continue immediately}@}. In Scala this is expressed by {@{the __`Future`__ abstraction}@}, which represents {@{a value that may become available later, together with its eventual result or failure}@}. <!--SR:!2026-03-16,57,310!2026-01-19,15,290!2026-03-13,54,310!2026-01-20,16,290-->

## motivation

When a function has to wait {@{for an I/O operation or a remote service}@}, {@{blocking the current thread}@} would {@{waste resources and stall other work}@}. Futures allow the calling code to {@{proceed while the computation runs in parallel}@}, improving {@{responsiveness and throughput on multi‑core machines}@}. They also make it easier to express {@{concurrent workflows without explicit thread management}@}. <!--SR:!2026-01-19,15,290!2026-03-16,57,310!2026-01-19,15,290!2026-03-15,56,310!2026-03-13,54,310!2026-03-14,55,310-->

### continuation-passing style

A common early pattern is {@{_continuation-passing style_ (CPS), or more commonly known as _callback style_}@}. Instead of {@{returning a value}@}, a function takes {@{an extra argument – the continuation that consumes the result once it becomes available}@}. This transforms {@{the call chain into nested callbacks}@}: <!--SR:!2026-03-14,55,310!2026-03-16,57,310!2026-03-14,55,310!2026-01-19,15,290-->

> [!example] __callback nesting__
>
> Instead of {@{returning a value}@}, a function takes {@{an extra argument – the continuation that consumes the result once it becomes available}@}. This transforms {@{the call chain into nested callbacks}@}:
>
> ```Scala
> def makeCoffee(done: Coffee => Unit): Unit = …
> def coffeeBreak(): Unit =
>   makeCoffee { c1 =>
>     drink(c1)
>     chatWithColleagues()
>   }
> ```
>
> The continuation {@{`c1 => ...` is invoked}@} when {@{the coffee is ready}@}. As {@{more asynchronous steps are added}@}, the code quickly becomes {@{hard to read and reason about}@}, causing {@{_callback hell_}@}. <!--SR:!2026-01-20,16,290!2026-01-19,15,290!2026-03-17,58,310!2026-01-19,15,290!2026-01-19,15,290!2026-03-17,58,310!2026-03-17,58,310!2026-03-16,57,310-->

### drawbacks of CPS

Apart from being ugly to {@{compose asynchronous steps (_callback hell_)}@}, CPS inflates {@{type signatures}@}: {@{every function that participates in an async flow}@} must accept {@{a callback, turning simple `A => B` into `A => (B => Unit)`}@}. Callbacks also hide {@{the thread on which they run}@}; if a callback mutates {@{shared state without proper synchronization}@}, {@{race conditions can arise}@}. For example: <!--SR:!2026-03-16,57,310!2026-01-19,15,290!2026-01-20,16,290!2026-01-19,15,290!2026-01-19,15,290!2026-01-19,15,290!2026-01-19,15,290-->

> [!example] __race condition in CPS__
>
> Callbacks also hide {@{the thread on which they run}@}; if a callback mutates {@{shared state without proper synchronization}@}, {@{race conditions can arise}@}. For example:
>
> ```Scala
> def makeCoffee(done: Coffee => Unit): Unit = …
>
> // two concurrent coffees that share mutable state
> var firstCoffee: Option[Coffee] = None
> val k = (c: Coffee) =>
>   firstCoffee match {
>     case None    => firstCoffee = Some(c)
>     case Some(other) => coffeesDone(c, other)
>   }
> makeCoffee(k); makeCoffee(k)          // race if the callbacks run on different threads
> ```
>
> Because `k` is executed {@{concurrently by two invocations of `makeCoffee`}@}, {@{the shared variable `firstCoffee`}@} can be {@{updated in any order}@}. <!--SR:!2026-01-20,16,290!2026-01-19,15,290!2026-03-16,57,310!2026-01-19,15,290!2026-01-20,16,290!2026-01-19,15,290-->

Because `k` is executed {@{concurrently by two invocations of `makeCoffee`}@}, {@{the shared variable `firstCoffee`}@} can be {@{updated in any order}@}. Without synchronization, {@{the resulting read—write pairs}@} may be {@{inconsistent or even lost}@}, illustrating why {@{CPS code that mutates external state is fragile when run asynchronously}@}. <!--SR:!2026-01-19,15,290!2026-03-15,56,310!2026-01-19,15,290!2026-01-20,16,290!2026-01-20,16,290!2026-01-20,16,290-->

Moreover, {@{exceptions thrown inside callbacks}@} are not {@{caught by surrounding `try/catch` blocks unless explicitly handled inside the callback}@}. <!--SR:!2026-01-19,15,290!2026-01-19,15,290-->

### CPS to direct style

{@{A `Future[T]`}@} can be seen as {@{a _direct_ representation of an asynchronous computation}@} that will {@{eventually produce a value of type `T`}@}. We can transform {@{a CPS function into one that returns a `Future`}@}. <!--SR:!2026-01-20,16,290!2026-01-19,15,290!2026-01-19,15,290!2026-03-17,58,310-->

> [!example] __CPS to `Future`__
>
> We start with {@{the CPS form}@}:
>
> ```Scala
> def program(a: A, k: B => Unit): Unit = …
> ```
>
> {@{Currying the continuation}@} gives:
>
> ```Scala
> def program(a: A): (B => Unit) => Unit = …
> ```
>
> By {@{introducing a type alias}@} we obtain:
>
> ```Scala
> type Future[+T] = (T => Unit) => Unit
> def program(a: A): Future[B] = …
> ```
>
> This is how one may obtain {@{`Future` in its most basic form}@}. <!--SR:!2026-01-21,17,310!2026-01-21,17,310!2026-01-21,17,310!2026-01-21,17,310-->

<!-- markdownlint MD028 -->

> [!example] __`Future` with error handling__
>
> And using {@{`Try[T]` instead of `T` as the future result}@}, {@{error handling}@} is built-in:
>
> ```Scala
> type Future[+T] = (Try[T] => Unit) => Unit
> def program(a: A): Future[B] = …
> ```
>
> Our `Future` can be further {@{improved in other ways}@}. In practice Scala provides {@{the `Future` trait}@}. <!--SR:!2026-01-21,17,311!2026-01-21,17,311!2026-01-21,17,311!2026-01-21,17,310-->

In practice Scala provides {@{the `Future` trait}@}, which extends {@{a function that accepts a callback}@} and offers {@{convenient combinators}@}. <!--SR:!2026-01-21,17,310!2026-01-21,17,310!2026-01-21,17,310-->

> [!example] __Scala Future API__
>
> In practice Scala provides {@{the `Future` trait}@}, which extends {@{a function that accepts a callback}@} and offers {@{convenient combinators}@}.
>
> ```Scala
> import scala.concurrent.{Future, ExecutionContext}
> implicit val ec: ExecutionContext = ExecutionContext.global
> def program(a: A): Future[B] =
>   Future { /* compute */ }
> ```
>
> {@{The `Future.apply` helper}@} hides {@{the CPS details}@}; {@{code written with `Future`}@} looks like {@{ordinary synchronous code but runs asynchronously}@}. <!--SR:!2026-01-20,16,290!2026-01-19,15,290!2026-01-19,15,290!2026-03-13,54,310!2026-03-16,57,310!2026-03-15,56,310!2026-01-19,15,290-->

Using {@{a `Future`}@} also gives {@{built‑in failure handling via `Try[T]`}@}, and combinators such as {@{`map`, `flatMap` and `onComplete`}@}. These facilities allow {@{composing several asynchronous steps without nesting callbacks or ugly error handling}@}, turning {@{the callback chain into fluent, readable pipelines}@}. <!--SR:!2026-03-17,58,310!2026-01-20,16,290!2026-03-13,54,310!2026-01-19,15,290!2026-03-13,54,310-->

## future

{@{A `Future[T]`}@} holds {@{a computation that will produce a value of type _T_ (or an exception)}@}. The library schedules {@{the task on an execution context}@} and the caller can register {@{callbacks that run when the future completes}@}. Because {@{the completion is asynchronous}@}, {@{`Future` offers combinators}@} such as {@{`map`, `flatMap`, and `zip`}@} to compose {@{independent computations without blocking}@}, and {@{`recover` and `recoverWith`}@} to {@{handle errors}@}. <!--SR:!2026-01-20,16,290!2026-01-20,16,290!2026-01-20,16,290!2026-01-19,15,290!2026-01-20,16,290!2026-01-19,15,290!2026-03-17,58,310!2026-01-19,15,290!2026-03-17,58,310!2026-01-19,15,290-->

> [!example] __Creating a Future__
>
> The following code creates {@{a future}@} that computes {@{the factorial of _n_ concurrently}@} (and actually {@{also in parallel using `ec`}@}):
>
> ```Scala
> import scala.concurrent._
> implicit val ec = ExecutionContext.global
> val fact: Future[Int] = Future { (1 to 10).product }
> ```
>
> The result can be {@{manipulated with `fact.map(_ + 1)`}@} or {@{awaited with `Await.result(fact, 5.seconds)`}@}. <!--SR:!2026-03-17,58,310!2026-01-20,16,290!2026-01-20,16,290!2026-01-19,15,290!2026-03-15,56,310-->

{@{The type signature of a non-concurrent pure function}@} is {@{`A => B`}@}. Returning {@{a future `Future[B]` instead of a plain value `B`}@} lifts the call into {@{asynchronous style}@}. <!--SR:!2026-03-15,56,310!2026-03-14,55,310!2026-01-19,15,290!2026-03-13,54,310-->

## promise

{@{A `Promise[T]`}@} is {@{a writable container that can be completed once}@}. {@{The owning code}@} creates {@{a promise}@} and hands {@{its `Future` obtained from `Promise.future` to callers}@}; {@{another part of the program}@} completes {@{the promise, which automatically completes all awaiting futures}@}. This pattern decouples {@{the producer from the consumer}@} and makes it easy to {@{bridge legacy APIs}@}. <!--SR:!2026-01-20,16,290!2026-01-20,16,290!2026-01-20,16,290!2026-01-20,16,290!2026-03-14,55,310!2026-01-20,16,290!2026-01-20,16,290!2026-01-20,16,290!2026-03-13,54,310-->

> [!example] __`Promise` usage__
>
> {@{The owning code}@} creates {@{a promise}@} and hands {@{its `Future` obtained from `Promise.future` to callers}@}; {@{another part of the program}@} completes {@{the promise, which automatically completes all awaiting futures}@}.
>
> ```Scala
> def asyncAdd(x: Int, y: Int): Future[Int] =
>   val p: Promise[Int] = Promise()
>   asyncAddLegacy(x, y, result => p.success(x + y))
>   p.future
> ```
>
> {@{The promise}@} is completed {@{after `asyncAddLegacy` calls the provided callback}@}; {@{any future that has been obtained from `p`}@} will {@{receive the result}@}. <!--SR:!2026-01-20,16,290!2026-01-19,15,290!2026-03-14,55,310!2026-03-14,55,310!2026-01-19,15,290!2026-01-20,16,290!2026-03-14,55,310!2026-01-19,15,290!2026-01-20,16,290-->

## transformations

`Future` offers {@{a small but expressive set of combinators}@} that lift {@{ordinary functions into the asynchronous world and compose several futures together}@}. The API is intentionally analogous to {@{the standard collection operations}@}, which makes reasoning {@{about pipelines straightforward}@}. These transformation operators let developers write {@{clear, linear‑looking code while still exploiting concurrency}@} (and {@{parallelism if the execution context is parallel}@}) and {@{failure handling}@} that `Future` provides. <!--SR:!2026-01-19,15,290!2026-03-14,55,310!2026-03-17,58,310!2026-01-20,16,290!2026-01-19,15,290!2026-01-20,16,290!2026-03-13,54,310-->

{@{`map`}@} applies {@{a pure function to the value produced by a `Future`}@}. If {@{the original future fails}@}, the resulting one {@{propagates the failure unchanged}@}. <!--SR:!2026-01-19,15,290!2026-01-20,16,290!2026-01-20,16,290!2026-03-15,56,310-->

> [!example] __`Future.map`__
>
> {@{`map`}@} applies {@{a pure function to the value produced by a `Future`}@}. If {@{the original future fails}@}, the resulting one {@{propagates the failure unchanged}@}.
>
> ```Scala
> def makeCoffee(): Future[Coffee] =
>   grindBeans().map(b => brew(b))
> ```
>
> {@{The `b` in the lambda}@} is supplied only after {@{the first future completes _successfully_}@}, and {@{any exception from `grindBeans` is automatically forwarded}@}. <!--SR:!2026-01-20,16,290!2026-03-15,56,310!2026-01-19,15,290!2026-01-20,16,290!2026-01-19,15,290!2026-01-20,16,290!2026-01-20,16,290-->

When {@{the next step itself returns a `Future`}@}, {@{`flatMap`}@} chains {@{them without nesting callbacks}@}. It keeps {@{the overall result type flat: `Future[B]`}@}. {@{Failure}@} still propagates {@{through every stage of the chain}@}. <!--SR:!2026-01-19,15,290!2026-01-20,16,290!2026-03-15,56,310!2026-01-19,15,290!2026-01-19,15,290!2026-03-13,54,310-->

> [!example] __`Future.flatMap`__
>
> When {@{the next step itself returns a `Future`}@}, {@{`flatMap`}@} chains {@{them without nesting callbacks}@}. It keeps {@{the overall result type flat: `Future[B]`}@}. {@{Failure}@} still propagates {@{through every stage of the chain}@}.
>
> ```Scala
> def makeCoffee(): Future[Coffee] =
>   grindBeans().flatMap(b => brew(b))
> ```
>
> {@{The call to `brew`}@} is performed only when {@{`grindBeans` succeeds}@}; otherwise {@{the failure is passed on}@}. <!--SR:!2026-01-20,16,290!2026-01-20,16,290!2026-03-14,55,310!2026-01-20,16,290!2026-01-19,15,290!2026-01-20,16,290!2026-01-20,16,290!2026-03-17,58,310!2026-03-15,56,310-->

{@{`zip`}@} combines {@{two independent futures, yielding a future of a tuple}@}. It does _not_ {@{introduce any dependency between them}@} – both run {@{concurrently (and in parallel if the execution context supports parallelism)}@}. If {@{either operand fails}@}, {@{the combined future fails as well}@}. <!--SR:!2026-01-20,16,290!2026-01-20,16,290!2026-03-16,57,310!2026-01-20,16,290!2026-03-13,54,310!2026-01-20,16,290-->

> [!example] __`Future.zip`__
>
> {@{`zip`}@} combines {@{two independent futures, yielding a future of a tuple}@}. It does _not_ {@{introduce any dependency between them}@} – both run {@{concurrently (and in parallel if the execution context supports parallelism)}@}. If {@{either operand fails}@}, {@{the combined future fails as well}@}.
>
> ```Scala
> def makeTwoCoffees(): Future[(Coffee, Coffee)] =
>   grindBeans().zip(grindBeans())
> ```
>
> {@{The two coffees}@} may be {@{prepared concurrently}@}; {@{the result is available only}@} when {@{both futures finish successfully}@}. <!--SR:!2026-01-20,16,290!2026-03-15,56,310!2026-01-20,16,290!2026-03-14,55,310!2026-03-15,56,310!2026-01-19,15,290!2026-01-20,16,290!2026-01-19,15,290!2026-03-15,56,310!2026-03-13,54,310-->

{@{`recover`}@} turns {@{a failed future into a successful one by supplying an alternative value}@}. {@{`recoverWith`}@} allows supplying {@{another asynchronous computation as the recovery path}@}, which is essentially {@{the flat version of `recover`}@}. <!--SR:!2026-01-19,15,290!2026-01-20,16,290!2026-03-14,55,310!2026-03-14,55,310!2026-01-19,15,290-->

> [!example] __`Future.recover`__
>
> {@{`recover`}@} turns {@{a failed future into a successful one by supplying an alternative value}@}.
>
> ```Scala
> val coffeeOrSoda: Future[Coffee] =
>   makeCoffee().recover { case _: java.io.IOException => defaultCoffee }
> ```
<!--SR:!2026-03-14,55,310!2026-01-19,15,290-->

### for-comprehensions

Because {@{`Future` implements `map`, `flatMap`, and `withFilter`}@}, it can be used in {@{a for‑comprehension}@}, which reads {@{naturally as a sequence of steps}@}. <!--SR:!2026-01-20,16,290!2026-03-16,57,310!2026-01-20,16,290-->

> [!example] __for-comprehension with `Future`__
>
> Because {@{`Future` implements `map`, `flatMap`, and `withFilter`}@}, it can be used in {@{a for‑comprehension}@}, which reads {@{naturally as a sequence of steps}@}.
>
> ```Scala
> val recipe: Future[Coffee] =
>   for {
>     beans <- grindBeans()
>     brew  <- coffee(beans)
>     cup   <- addSugar(brew)
>   } yield cup
> ```
<!--SR:!2026-01-20,16,290!2026-01-19,15,290!2026-01-19,15,290-->

## dataflow programming

{@{_Dataflow programming_}@} views a program as {@{a network of independent computations that communicate by passing values along edges}@}. Each node executes when {@{all its input values are available}@}, and the result is then {@{propagated to downstream nodes}@}. Scala’s {@{`Future` and `Promise`}@} naturally fit this model: {@{a `Future`}@} represents {@{an edge whose value will be supplied later}@}, while {@{a `Promise`}@} acts as {@{a writable sink that can be completed by any thread}@}. <!--SR:!2026-03-16,57,310!2026-01-19,15,290!2026-01-20,16,290!2026-01-20,16,290!2026-03-14,55,310!2026-03-14,55,310!2026-03-17,58,310!2026-01-19,15,290!2026-01-20,16,290-->

In {@{a dataflow graph}@}, a node may have {@{several inputs}@}; in code this is expressed with {@{the combinators `map`, `flatMap`, or `zip`}@}. When {@{all required futures finish}@}, {@{the next step}@} runs. Because the language guarantees that {@{each future is evaluated at most once}@}, the graph remains {@{acyclic and free of race conditions}@}, provided {@{the underlying execution context}@} respects {@{the promises’ completion semantics}@}. <!--SR:!2026-03-16,57,310!2026-01-20,16,290!2026-03-15,56,310!2026-01-19,15,290!2026-03-15,56,310!2026-01-20,16,290!2026-01-20,16,290!2026-01-20,16,290!2026-01-20,16,290-->

> [!example] __`Future` dataflow example__
>
> The following snippet builds {@{a small pipeline}@} where {@{three independent stages run in parallel}@}:
>
> ```Scala
> val beans  = Future { grindBeans() }          // node 1
> val water = Future { heatWater() }            // node 2
> val brew  = for {
>   b <- beans
>   w <- water
> } yield makeCoffee(b, w)                       // node 3 depends on 1 and 2
> ```
>
> {@{The `for`‑comprehension}@} expands to {@{`beans.flatMap { ... }.zip(water).map{…}`}@}, which is {@{a concise dataflow representation}@}. When {@{either `beans` or `water` fails}@}, {@{the whole pipeline fails immediately}@}; if {@{both succeed}@}, `brew` starts only {@{after the two inputs arrive}@}. <!--SR:!2026-01-19,15,290!2026-01-19,15,290!2026-03-17,58,310!2026-03-17,58,310!2026-01-20,16,290!2026-01-19,15,290!2026-01-19,15,290!2026-01-20,16,290!2026-03-13,54,310-->

{@{A `Promise`}@} can be used when {@{an external event must feed into the graph}@}. The producer {@{completes the promise}@}, which triggers {@{all dependent futures}@}: <!--SR:!2026-01-19,15,290!2026-03-13,54,310!2026-03-16,57,310!2026-01-20,16,290-->

> [!example] __using a `Promise` as a data‑sink__
>
> {@{A `Promise`}@} can be used when {@{an external event must feed into the graph}@}. The producer {@{completes the promise}@}, which triggers {@{all dependent futures}@}:
>
> ```Scala
> val p = Promise[Int]()
> // later, possibly on another thread
> p.success(42)
>
> // downstream computation waits for the value
> val answer: Future[Int] = p.future
> ```
>
> {@{The promise’s `future` field}@} is a {@{normal `Future`}@}, so it can be {@{composed with other futures in the same dataflow network}@}. <!--SR:!2026-01-19,15,290!2026-03-17,58,310!2026-01-19,15,290!2026-01-19,15,290!2026-03-13,54,310!2026-01-20,16,290!2026-01-20,16,290-->

{@{_Lenient evaluation_}@}, which evaluates {@{an expression as soon as it becomes available but only once}@}, is essentially the same idea as {@{dataflow}@}: each node {@{runs when its inputs are ready}@}. {@{`Futures`}@} provide {@{a convenient runtime for this pattern}@} without {@{explicit scheduling or graph construction}@}; {@{the Scala compiler and the execution context}@} take care of {@{wiring the edges behind the scenes}@}. <!--SR:!2026-01-19,15,290!2026-01-20,16,290!2026-01-20,16,290!2026-01-20,16,290!2026-01-19,15,290!2026-03-13,54,310!2026-01-19,15,290!2026-03-16,57,310!2026-01-20,16,290-->

## execution context

{@{A `Future`}@} does not {@{decide by itself where its continuation runs}@}. {@{The _execution context_}@} is {@{a runtime object that owns a thread pool or a scheduler}@} and decides on {@{which worker a callback will be invoked}@}. By importing {@{an implicit `ExecutionContext`}@}, {@{every `Future`}@} automatically {@{submits its work to the same pool}@}, making it trivial to switch from {@{a single‑threaded environment to a fixed‑size thread pool or even a custom executor}@}. <!--SR:!2026-01-19,15,290!2026-01-19,15,290!2026-01-20,16,290!2026-01-19,15,290!2026-01-20,16,290!2026-01-19,15,290!2026-01-19,15,290!2026-01-20,16,290!2026-01-20,16,290-->

> [!example] __implicit execution context__
>
> {@{The default global execution context}@} uses {@{a cached thread pool that grows with demand and shrinks when idle}@}:
>
> ```Scala
> import scala.concurrent.ExecutionContext.Implicits.global
> val f = Future { heavyComputation() }   // runs on the implicit EC
> ```
>
> To use {@{a custom pool}@}, you can provide {@{your own `ExecutionContext`}@}:
>
> ```Scala
> import java.util.concurrent.Executors
> val ec: ExecutionContext =
>   ExecutionContext.fromExecutor(Executors.newFixedThreadPool(4))
> Future { /* … */ }(ec)                     // explicitly pass the EC
> ```
<!--SR:!2026-01-20,16,290!2026-01-19,15,290!2026-01-20,16,290!2026-01-19,15,290-->

{@{The execution context}@} is also used when {@{chaining futures with `map`, `flatMap` or `onComplete`}@}; each callback uses {@{the implicit context from the surrounding code}@}. <!--SR:!2026-01-19,15,290!2026-01-19,15,290!2026-01-20,16,290-->

## API mitigation

When {@{an existing library}@} offers {@{a callback‑based asynchronous method}@}, converting it to {@{a `Future`}@} keeps {@{the original API while giving you the full power of Scala’s concurrent collections}@}. The usual pattern is to create {@{a `Promise`, hand it to the callback}@}, and expose {@{its `future` field}@}. <!--SR:!2026-01-19,15,290!2026-03-17,58,310!2026-01-19,15,290!2026-01-20,16,290!2026-03-16,57,310!2026-01-20,16,290-->

> [!example] __Lifting callbacks to Future__
>
> {@{A typical callback signature}@} as follows
>
> ```Scala
> def makeCoffee(
>   coffeeDone: Coffee => Unit,
>   onFailure: Exception => Unit): Unit = …
> ```
>
> can be {@{lifted into a `Future`}@} by wrapping {@{the two callbacks in a single `Promise`}@}:
>
> ```Scala
> import scala.concurrent.{Future, Promise}
>
> def makeCoffee2(): Future[Coffee] =
>   val p = Promise[Coffee]()
>   makeCoffee(
>     coffee => p.trySuccess(coffee),
>     e    => p.tryFailure(e))
>   p.future
> ```
>
> Assuming {@{_no exceptions_ are thrown before returning `p.future`}@}, the `Promise` is {@{completed exactly once}@}; subsequent calls to {@{`trySuccess` or `tryFailure` are ignored}@}, guaranteeing {@{a single result}@}. <!--SR:!2026-01-19,15,290!2026-03-17,58,310!2026-03-15,56,310!2026-01-19,15,290!2026-01-20,16,290!2026-03-15,56,310!2026-01-19,15,290-->

Assuming {@{_no exceptions_ are thrown before returning `p.future`}@}, the `Promise` is {@{completed exactly once}@}; subsequent calls to {@{`trySuccess` or `tryFailure` are ignored}@}, guaranteeing {@{a single result}@}. Using this pattern keeps {@{the original callback API intact}@} while enabling callers to compose {@{the operation with other futures via `map`, `flatMap`, or `zip`}@}. <!--SR:!2026-01-20,16,290!2026-01-19,15,290!2026-01-19,15,290!2026-03-16,57,310!2026-03-13,54,310!2026-03-16,57,310-->
