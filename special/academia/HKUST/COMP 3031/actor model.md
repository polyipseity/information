---
aliases:
  - COMP 3031 Scala actor model
  - COMP3031 Scala actor model
  - HKUST COMP 3031 Scala actor model
  - HKUST COMP3031 Scala actor model
  - Scala actor model
tags:
  - flashcard/active/special/academia/HKUST/COMP_3031/actor_model
  - language/in/English
---

# Scala actor model

- HKUST COMP 3031

---

- see: [general/actor model](../../../../general/actor%20model.md)

{@{The __actor model__}@} replaces {@{shared‑memory concurrency}@} with {@{isolated actors that communicate only by sending messages}@}. By treating each actor as {@{a black box that owns its own state}@}, the need for {@{locks and explicit synchronization disappears}@}, simplifying {@{reasoning about concurrent programs}@} and avoiding {@{classic pitfalls such as race conditions and deadlocks}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

## motivation

In {@{modern multicore CPUs}@}, {@{parallelism}@} is achieved by {@{running many tasks simultaneously on distinct cores}@}. {@{Traditional thread‑based approaches}@} force programmers to protect {@{shared mutable data with mutexes or semaphores}@}. Such mechanisms are {@{error‑prone}@}: {@{a missing lock}@} can cause {@{data races}@}; {@{nested locks}@} can {@{lead to deadlocks}@}. Moreover, {@{the overhead of context switching and contention}@} limits {@{scalability}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

Actors {@{sidestep these issues}@} by enforcing {@{_encapsulation_: an actor never exposes its internal state to other actors}@}. The only interaction is through {@{immutable messages sent asynchronously}@}. This guarantees that {@{two actors cannot interfere with each other’s data}@}, so {@{no lock is required}@}. Because sending {@{a message does not block the sender}@}, the model naturally supports {@{high‑throughput, non‑blocking systems}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

Actors provide {@{a clean abstraction for parallelism}@}: they eliminate {@{shared mutable state}@}, remove {@{lock‑based synchronization, and avoid deadlocks}@} while still allowing {@{many actors to run concurrently}@}. This makes Scala programs easier to {@{write, reason about, and scale on modern multicore hardware}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

### actor vs. thread

{@{A thread}@} is {@{a lightweight execution context}@} that shares {@{the same address space as every other thread}@}. When two threads {@{modify the same variable}@}, they must coordinate through {@{synchronization primitives}@}. In contrast, an actor has {@{its own private mailbox}@}; it processes {@{one message at a time in its own event loop}@}. {@{The cost of creating many actors}@} is {@{far lower than spawning thousands of threads}@}, and the runtime can schedule {@{them efficiently on the available cores}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

### avoiding synchronization

Consider a bank account example where {@{two concurrent deposits update a shared balance}@}. With {@{threads}@} you would guard {@{the `balance` field}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __`BankAccount` with `synchronized`__
>
> {@{The classic approach}@} uses {@{Java/Scala synchronization primitives}@}:
>
> ```Scala
> class BankAccount {
>   private var balance = 0
>   def deposit(amount: Int): Unit =
>     this.synchronized { if (amount > 0) balance += amount }
>   def withdraw(amount: Int): Int =
>     this.synchronized {
>       if (0 < amount && amount <= balance)
>         balance -= amount
>       else throw new Error("insufficient funds")
>     }
> }
> ```
>
> While {@{correct}@}, {@{the locks}@} can {@{serialize access and expose the program to deadlocks}@} when {@{multiple accounts are involved}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{A classic deadlock}@} occurs when {@{two actors (or threads)}@} {@{lock shared resources in reverse order}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __deadlock in nested synchronized transfer__
>
> {@{A classic deadlock}@} occurs when {@{two actors (or threads)}@} {@{lock shared resources in reverse order}@}.
>
> ```Scala
> def transfer(from: BankAccount, to: BankAccount, amount: Int): Unit =
>   from.synchronized {
>     to.synchronized {        // ← locks acquired in opposite order by another thread
>       from.withdraw(amount)
>       to.deposit(amount)
>     }
>   }
> ```
>
> If `transfer(a,b,x)` runs {@{concurrently with `transfer(b,a,y)`}@}, each thread holds {@{one lock and waits for the other}@}, causing {@{a deadlock}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{An actor version of `BankAccount`}@}, `BankActor`, removes {@{the lock}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __`BankAccount` actor__
>
> {@{The same logic}@} expressed as {@{an actor}@}:
>
> ```Scala
> case class Deposit(amount: Int)
> case class Withdraw(amount: Int, replyTo: ActorRef)
> case class Balance(replyTo: ActorRef)
>
> object BankActor extends Actor {
>   private var balance = 0
>   def receive: Receive = {
>     case Deposit(a)            => if (a > 0) balance += a
>     case Withdraw(a, replyTo) =>
>       if (0 < a && a <= balance) { balance -= a; replyTo ! Right(balance) }
>       else replyTo ! Left("insufficient funds")
>     case Balance(replyTo)      => replyTo ! balance
>   }
> }
> ```
>
> Here {@{each message}@} is {@{processed sequentially by the actor}@}, so {@{no explicit locks are needed}@} and concurrent deposits cannot {@{interleave in a way that corrupts `balance`}@}. <!--SR:!2025-12-25,4,291!2025-12-25,4,291!2025-12-25,4,291!2025-12-25,4,291!2025-12-25,4,290!2025-12-25,4,290-->

Actors process {@{each message _sequentially_}@}, so {@{no explicit locks are needed}@}, and concurrent messages cannot {@{interleave in a way that corrupts the actor state}@}. <!--SR:!2025-12-25,4,291!2025-12-25,4,291!2025-12-25,4,291-->

## history

{@{The concept originated}@} with {@{Hewitt et al. in 1973 as a formalism for artificial‑intelligence research}@}. In {@{1986 Gul Agha expanded the theory}@} and defined {@{common communication patterns}@}. {@{Erlang/OTP adopted actors in 1995}@}, making them {@{the backbone of telecom platforms}@}. Scala added {@{a lightweight Actor trait to its standard library in 2006}@}. Two years later {@{Akka was released as an independent Scala actor framework}@}; it has since been used by {@{large services such as WhatsApp and Fortnite}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

## actor

{@{An _actor_}@} is an object that {@{possesses identity, a behavior, and communicates only by sending messages asynchronously}@}. It does not {@{expose its internal state to other actors}@}; instead, it receives {@{messages via an `ActorRef`}@} and reacts {@{according to its own logic}@}. The model was formalised by {@{Hewitt et al. in 1973 as a universal modular framework for artificial intelligence}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{The core of Scala’s actor implementation}@} is {@{the trait `Actor`}@}. Its {@{single abstract member `receive`}@} defines how it {@{handles incoming messages}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __Scala `Actor` trait__
>
> {@{The trait}@} declares {@{the message‑handling function `receive`}@} that actors must implement:
>
> ```Scala
> type Receive = PartialFunction[Any, Unit]
> trait Actor { def receive: Receive }
> ```
>
> {@{A concrete actor}@} supplies {@{a `receive` method}@} that {@{pattern matches on received messages}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{A minimal example}@} shows {@{an actor}@} that counts {@{how many times it has been told to increment}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __`Counter` actor__
>
> {@{A minimal example}@} shows {@{an actor}@} that counts {@{how many times it has been told to increment}@}:
>
> ```Scala
> class Counter extends Actor {
>   private var count = 0
>   def receive: Receive =
>     case "incr" => count += 1
> }
> ```
>
> {@{The `count` field}@} is {@{internal to the actor}@}; {@{other actors can only influence it}@} by sending {@{the `"incr"` message}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

### actor creation

Actors are {@{instantiated through the actor system}@}, which supplies {@{a unique reference}@}. {@{A reference (`ActorRef`)}@} is what {@{other actors use to send messages}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __creating an actor__
>
> Actors are {@{instantiated through the actor system}@}, which supplies {@{a unique reference}@}. {@{A reference (`ActorRef`)}@} is what {@{other actors use to send messages}@}:
>
> ```Scala
> val counter = context.actorOf(Props[Counter], "counter")
> ```
>
> {@{The returned `ActorRef`}@} can be used to {@{post a message}@}:
>
> ```Scala
> counter ! "incr"
> ```
>
> Because {@{messages are queued}@}, the sender does not {@{wait for the receiver}@}; {@{this asynchronous, non‑blocking communication}@} is one of {@{the key advantages of the actor model}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

### message passing

{@{Actors}@} can {@{reply to the sender of a message}@} by using {@{`sender()`}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __`Counter` with reply__
>
> {@{Actors}@} can {@{reply to the sender of a message}@} by using {@{`sender()`}@}:
>
> ```Scala
> class Counter extends Actor {
>   private var count = 0
>   def receive: Receive =
>     case "incr" => count += 1
>     case ("get", client: ActorRef) => client ! count
> }
> ```
>
> {@{The `sender()` helper}@} obtains {@{the actor that sent the current message}@}, allowing {@{a two‑way interaction}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{The core of communication}@} is {@{the `!` operator}@}. It queues {@{a message for the target and returns immediately}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __message sending__
>
> {@{The core of communication}@} is {@{the `!` operator}@}. It queues {@{a message for the target and returns immediately}@}:
>
> ```Scala
> val counter = context.actorOf(Props[Counter], "counter")
> counter ! "incr"
> ```
>
> {@{The sender’s address}@} is passed {@{automatically}@}, so {@{the recipient can reply}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

### actor sate

Actors may alter {@{their own behaviour at runtime with `context.become`}@}. This technique keeps {@{state local to a particular behaviour}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __dynamic behaviour__
>
> Actors may alter {@{their own behaviour at runtime with `context.become`}@}. This technique keeps {@{state local to a particular behaviour}@}:
>
> ```Scala
> class Counter extends Actor {
>   def counter(n: Int): Receive = {
>     case "incr" => context.become(counter(n + 1))
>     case "get"  => sender() ! n
>   }
>   def receive: Receive = counter(0)
> }
> ```
<!--SR:!2025-12-25,4,291!2025-12-25,4,291-->

{@{Switching behaviour}@} is functionally equivalent to {@{mutating a field}@} but keeps {@{the state explicitly scoped}@}. <!--SR:!2025-12-25,4,291!2025-12-25,4,291!2025-12-25,4,291-->

### actor lifecycle

Actors are not {@{instantiated directly with `new`}@}. The runtime supplies {@{a unique reference (which may live on other computers!!)}@} when {@{an actor is created}@}, and {@{the creating actor (or an `ActorSystem`)}@} performs this work through {@{the `ActorContext`}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __creating an actor__
>
> {@{An actor is spawned}@} by calling {@{`actorOf` on an `ActorContext`}@}:
>
> ```Scala
> val counter = context.actorOf(Props[Counter], "counter")
> ```
>
> {@{The returned value}@} is an {@{`ActorRef`}@}. Other actors use this reference to send {@{messages with the asynchronous operator `!`}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{Instantiating actors with `new`}@} would bypass {@{the actor framework’s bookkeeping}@}: the runtime would not assign {@{a unique `ActorRef`}@}, nor would it be able to schedule {@{the actor on another machine}@}. Using {@{the context’s `actorOf`}@} delegates {@{creation, life‑cycle management, and potential distribution}@} to the framework. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

When {@{an actor receives a message}@} it may: {@{send other messages}@}; {@{create or stop actors}@}; or {@{change its own behaviour with `context.become`}@}. These capabilities let an actor orchestrate {@{complex workflows without shared mutable data}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{Stopping an actor}@} releases {@{its resources and removes it from the system}@}. The usual way is to call {@{`stop` on a reference}@}, often from {@{inside the actor itself via `context.stop(self)`}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __stopping an actor__
>
> {@{The same actor}@} can terminate by sending {@{a stop signal to its own reference}@}:
>
> ```Scala
> context.stop(self)
> ```
>
> After this call {@{the actor’s mailbox is drained and its resources are reclaimed}@}. Actors may also be stopped externally through {@{`system.actorOf(Props[MyActor])` followed by `system.stop(actor)`}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{These primitives}@} give actors {@{a well‑defined lifecycle that fits naturally into the asynchronous, message‑driven model}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->

### actor encapsulation

Actors expose only {@{a _mailbox_ through an `ActorRef`}@}. {@{No external code}@} can read or modify {@{the internal state of an actor}@}; all interaction must be performed by {@{sending a message}@}. Each actor knows {@{its own address via `self`}@}, and can give that address {@{to others inside a message _implicitly_}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __passing `self`__
>
> {@{The current actor’s reference}@} is available as {@{`self`}@} and can be sent back to {@{the sender _implicitly_}@}:
>
> ```Scala
> case "get" => sender() ! count          // reply to the caller with `self` implicitly
> ```
>
> Because {@{messages are immutable}@}, {@{no shared data is exposed}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{The encapsulation}@} guarantees that {@{two actors cannot interfere with each other’s state}@}, eliminating {@{races}@}. Actors live in {@{separate heaps}@}; they communicate only through {@{asynchronous messages}@}, so the runtime can schedule {@{them independently without global locks}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

### message processing

An actor processes {@{its mailbox _sequentially_}@}. When {@{a message arrives}@} it is {@{dequeued and handled by the current `Receive` function}@}. {@{Changing behaviour with `context.become`}@} takes effect {@{before the next message is taken}@}, so each message is {@{an atomic unit of execution}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __message order__
>
> {@{An actor that counts up}@} demonstrates {@{this ordering}@}:
>
> ```Scala
> class Counter extends Actor {
>   private var n = 0
>   def receive: Receive =
>     case "inc" => n += 1          // atomic update
>     case "get" => sender() ! n
> }
> ```
>
> If two messages {@{“inc” arrive concurrently}@}, they are {@{queued and executed one after the other}@}; {@{no interleaving can corrupt `n`}@}. <!--SR:!2025-12-25,4,291!2025-12-25,4,291!2025-12-25,4,291!2025-12-25,4,291!2025-12-25,4,291-->

If two messages {@{arrive concurrently}@}, they are {@{queued and executed one after the other}@}; {@{no interleaving can corrupt the actor state}@}. The actor’s {@{single‑threaded model}@} turns {@{locking into simple sequencing}@}. <!--SR:!2025-12-25,4,291!2025-12-25,4,291!2025-12-25,4,291!2025-12-25,4,291!2025-12-25,4,291-->

## entry point

{@{A minimal program}@} that creates {@{a counter}@}, sends {@{three increment messages}@}, asks for {@{the result, prints it}@}, and then {@{stops itself}@} is written as {@{an actor}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __`Main` actor__
>
> {@{This actor}@} creates {@{a `Counter`}@}, performs {@{some operations on it}@}, and {@{terminates}@}:
>
> ```Scala
> class Main extends Actor {
>   val counter = context.actorOf(Props[Counter], "counter")
>   counter ! "incr"; counter ! "incr"; counter ! "incr"
>   counter ! "get"
>
>   def receive: Receive = {
>     case count: Int =>
>       println(s"count was $count")
>       context.stop(self)
>   }
> }
> ```
>
> {@{The `!` operator}@} posts {@{a message asynchronously}@}, so {@{the main actor continues immediately after sending}@}. When {@{the counter replies with an `Int`}@}, the main actor {@{prints it and then stops itself}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

### bank account example

In {@{an actor‑based design}@}, {@{a `BankAccount`}@} exposes only {@{two operations: `Deposit` and `Withdraw`}@}. The messages are declared {@{in the companion object}@} so they can be {@{imported elsewhere without leaking implementation details}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __`BankAccount` messages__
>
> {@{The messages}@} are declared {@{in the companion object}@} so they can be {@{imported elsewhere without leaking implementation details}@}.
>
> ```Scala
> object BankAccount {
>   case class Deposit(amount: BigInt) { require(amount > 0) }
>   case class Withdraw(amount: BigInt) { require(amount > 0) }
>   case object Done
>   case object Failed
> }
> ```
<!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{The actor itself}@} keeps {@{a mutable balance}@} and replies with {@{`Done` or `Failed`}@}. When it {@{receives a `Withdraw`}@}, the amount is checked {@{against the current balance}@}; if insufficient, it signals {@{failure}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __BankAccount actor__
>
> {@{The actor itself}@} keeps {@{a mutable balance}@} and replies with {@{`Done` or `Failed`}@}. When it {@{receives a `Withdraw`}@}, the amount is checked {@{against the current balance}@}; if insufficient, it signals {@{failure}@}.
>
> ```Scala
> class BankAccount extends Actor {
>   import BankAccount._
>   private var balance = BigInt(0)
>   def receive: Receive =
>     case Deposit(a)          => balance += a; sender() ! Done
>     case Withdraw(a) if a <= balance =>
>       balance -= a; sender() ! Done
>     case _                    => sender() ! Failed
> }
> ```
<!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{A `WireTransfer` actor}@} demonstrates how {@{two bank accounts can cooperate without shared state}@}. It first asks {@{the source account to withdraw}@}, waits for {@{its reply}@}, and only then {@{deposits into the destination}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __`WireTransfer` actor__
>
> It first asks {@{the source account to withdraw}@}, waits for {@{its reply}@}, and only then {@{deposits into the destination}@}.
>
> ```Scala
> object WireTransfer {
>   case class Transfer(from: ActorRef, to: ActorRef, amount: BigInt)
>   case object Done; case object Failed
> }
>
> class WireTransfer extends Actor {
>   import WireTransfer._
>   def receive: Receive = {
>     case Transfer(f, t, a) =>
>       f ! BankAccount.Withdraw(a)
>       context.become(awaitWithdraw(t, a, sender()))
>   }
>
>   private def awaitWithdraw(to: ActorRef,
>                             amount: BigInt,
>                             client: ActorRef): Receive = {
>     case BankAccount.Done   => to ! BankAccount.Deposit(amount); context.become(awaitDeposit(client))
>     case BankAccount.Failed => client ! Failed; context.stop(self)
>   }
>
>   private def awaitDeposit(client: ActorRef): Receive = {
>     case BankAccount.Done => client ! Done; context.stop(self)
>     case _                => client ! Failed; context.stop(self)
>   }
> }
> ```
<!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{The actor hierarchy}@} is therefore {@{safe and composable}@}: each account owns {@{its own balance}@}, {@{the transfer logic}@} runs {@{in a separate actor}@}, and all communication proceeds {@{through immutable messages}@}. This pattern illustrates how actors avoid {@{shared‑memory pitfalls}@} while enabling {@{fine‑grained concurrent interactions}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

## message delivery

{@{Actor communication}@} is {@{asynchronous and, by its nature, unreliable}@}. {@{A send}@} may {@{drop the packet or duplicate it}@}. {@{The three classical delivery semantics}@} are: {@{_at-most-once_, _at-least-once_, and _exactly-once_}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

- _at-most-once_: ::@:: a single send may be dropped or delivered once; the receiver must tolerate loss. <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->
- _at-least-once_: ::@:: the sender repeats until it receives an acknowledgment, so the message is delivered one or more times. <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->
- _exactly-once_: ::@:: the system guarantees that only the first reception is processed, typically by combining at‑least‑once delivery with idempotent handlers or persistent state. <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->

One may rely on {@{business logic}@} to {@{ignore duplicates}@}. {@{Akka actors}@} provide {@{persistence primitives}@} that let {@{a message be stored and replayed}@}, enabling {@{exactly‑once processing}@} when coupled with {@{unique correlation IDs}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __reliable transfer using IDs__
>
> {@{A simple way}@} to make {@{a `WireTransfer` reliable}@} is to {@{attach an ID and persist the operation}@}:
>
> ```Scala
> object WireTransfer {
>   case class Transfer(id: String, from: ActorRef, to: ActorRef, amount: BigInt)
> }
>
> // in WireTransfer.receive
> case WireTransfer.Transfer(id, f, t, a) =>
>   persist(Transfer(id, f, t, a)) { _ => … }   // store before sending
> ```
>
> {@{The actor}@} can later replay {@{the stored record}@} if it crashes, ensuring that {@{every transfer is processed exactly once}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

When {@{several messages are sent to the same recipient}@} they keep {@{the order in which they were issued}@}; this is {@{an Akka‑specific guarantee}@}. {@{Messages to different actors}@} may arrive {@{interleaved arbitrarily}@}. {@{The lack of global ordering}@} means a system must reason about {@{partial orders when composing components}@}, but {@{the single‑threaded mailbox}@} guarantees that each message is {@{processed atomically and that no two messages can be handled simultaneously by one actor}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

## web client example

{@{The design}@} starts by decomposing {@{the crawling task into independent units that communicate only through messages}@}. Actors are considered {@{replaceable “people”}@}; {@{their interactions}@} are drawn in {@{a diagram}@}, but {@{the concrete implementation is free to change}@} as long as {@{the message protocol remains unchanged}@}. {@{A link‑checker actor system}@} follows this pattern: {@{a `Receptionist`}@} receives {@{client requests}@}, spawns {@{a `Controller` per request}@}, and the controller creates {@{`Getter` actors for each discovered link}@} until {@{a depth limit is reached}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{A naive version of `WebClient.get`}@} blocks {@{the calling actor, tying up a thread}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __blocking web client__
>
> {@{A naive version of `WebClient.get`}@} waits for {@{the HTTP response}@} before returning.
>
> ```Scala
> val client = new AsyncHttpClient
> def get(url: String): String =
>   val resp = client.prepareGet(url).execute().get
>   if (resp.getStatusCode < 400)
>     resp.getResponseBodyExcerpt(131072)
>   else throw BadStatus(resp.getStatusCode)
> ```
<!--SR:!2025-12-25,4,270!2025-12-25,4,270-->

{@{The non‑blocking version}@} uses {@{a `Future` and the actor’s dispatcher}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __non‑blocking web client__
>
> {@{The result}@} is wrapped in {@{a `Future`}@}, allowing {@{the caller to continue immediately}@}.
>
> ```Scala
> private val client = new AsyncHttpClient
> def get(url: String)(using exec: Executor): Future[String] =
>   val f = client.prepareGet(url).execute()
>   val p = Promise[String]()
>   f.addListener(new Runnable {
>     def run =
>       val r = f.get
>       if (r.getStatusCode < 400) p.success(r.getResponseBodyExcerpt(131072))
>       else p.failure(BadStatus(r.getStatusCode))
>   }, exec)
>   p.future
> ```
<!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{A `Getter` actor}@} fetches {@{a URL asynchronously}@}, extracts {@{links with Jsoup}@}, forwards them to {@{its parent controller}@}, and stops {@{itself when finished or on failure}@}. {@{The `pipeTo` helper}@} simplifies sending {@{the future result back to the actor}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __`Getter` actor__
>
> {@{A `Getter` actor}@} fetches {@{a URL asynchronously}@}, extracts {@{links with Jsoup}@}, forwards them to {@{its parent controller}@}, and stops {@{itself when finished or on failure}@}. {@{The `pipeTo` helper}@} simplifies sending {@{the future result back to the actor}@}.
>
> ```Scala
> class Getter(url: String, depth: Int) extends Actor:
>   given exec = context.dispatcher
>   WebClient.get(url).pipeTo(self)
>   def receive =
>     case body: String =>
>       for (link <- findLinks(body)) context.parent ! Controller.Check(link, depth-1)
>       stop()
>     case _: Status.Failure => stop()
>     case Abort => stop()
>   private def stop(): Unit =
>     context.parent ! Done
>     context.stop(self)
> ```
<!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{The `Controller`}@} keeps {@{a cache of already visited URLs}@} and {@{a set of running getters}@}. When {@{all children finish}@}, it reports {@{the collected links back to its parent}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __`Controller` actor__
>
> {@{The `Controller`}@} keeps {@{a cache of already visited URLs}@} and {@{a set of running getters}@}. When {@{all children finish}@}, it reports {@{the collected links back to its parent}@}.
>
> ```Scala
> class Controller extends Actor with ActorLogging:
>   var cache = Set.empty[String]
>   var children = Set.empty[ActorRef]
>   def receive =
>     case Check(url, depth) =>
>       if (!cache(url) && depth > 0) {
>         val c = context.actorOf(Props(new Getter(url, depth-1)))
>         children += c
>       }
>       cache += url
>     case Done =>
>       children -= sender()
>       if (children.isEmpty) context.parent ! Result(cache)
> ```
<!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

Actors can schedule {@{timeouts via the actor system’s scheduler}@}. {@{A controller}@} that aborts {@{all unfinished getters after a fixed delay}@} is shown; {@{the timeout message}@} is sent to {@{the controller itself}@}, preserving {@{encapsulation}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __`Controller` with overall timeout__
>
> Actors can schedule {@{timeouts via the actor system’s scheduler}@}. {@{A controller}@} that aborts {@{all unfinished getters after a fixed delay}@} is shown; {@{the timeout message}@} is sent to {@{the controller itself}@}, preserving {@{encapsulation}@}.
>
> ```Scala
> class Controller extends Actor with ActorLogging:
>   import context.dispatcher
>   var children = Set.empty[ActorRef]
>   context.system.scheduler.scheduleOnce(10.seconds, self, Timeout)
>   def receive =
>     case Timeout => children.foreach(_ ! Abort)
>     // other cases …
> ```
>
> {@{Note that `scheduleOnce`}@} also accepts {@{a runnable}@}. However, we cannot use it to {@{_directly_ run `children.foreach(_ ! Abort)`}@} as it {@{breaks encapsulation}@}. That is, the actor state is {@{accessed from outside the actor's `receive` function}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{A `Cache` actor}@} may be {@{further split from the `Controller` actor}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __`Cache` actor with futures__
>
> {@{A `Cache` actor}@} may be {@{further split from the `Controller` actor}@}.
>
> ```Scala
> class Cache extends Actor:
>   var cache = Map.empty[String, String]
>   def receive =
>     case Get(url) =>
>       if (cache contains url) sender() ! cache(url)
>       else
>         val client = sender()
>         WebClient.get(url).map(Result(client, url, _)) pipeTo self
>     case Result(client, url, body) =>
>       cache += url -> body
>       client ! body
> ```
<!--SR:!2025-12-25,4,270!2025-12-25,4,270-->

{@{The `Receptionist`}@} {@{serialises incoming requests}@} and limits {@{the number of concurrent crawls}@}. It uses {@{`context.become`}@} to switch between {@{waiting and running states}@} while keeping state {@{local to each behavior}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __`Receptionist` actor__
>
> {@{The `Receptionist`}@} {@{serialises incoming requests}@} and limits {@{the number of concurrent crawls}@}. It uses {@{`context.become`}@} to switch between {@{waiting and running states}@} while keeping state {@{local to each behavior}@}.
>
> ```Scala
> class Receptionist extends Actor:
>   def receive = waiting
>   val waiting: Receive =
>     case Get(url) => context.become(runNext(Vector(Job(sender(), url))))
>   def runNext(queue: Vector[Job]): Receive =
>     case Controller.Result(links) =>
>       queue.head.client ! Result(queue.head.url, links)
>       context.stop(sender())
>       context.become(runNext(queue.tail))
>     case Get(url) => enqueueJob(queue, Job(sender(), url))
>   def enqueueJob(q: Vector[Job], job: Job): Receive =
>     if q.size > 3 then sender() ! Failed(job.url)
>     else runNext(q :+ job)
> ```
<!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{These pieces}@} together form {@{a fully non‑blocking crawler}@} that scales with {@{the number of available cores}@} and demonstrates {@{key actor‑model idioms}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

## actor application

{@{Actors}@} are conceived as {@{replaceable workers that communicate only through messages}@}. {@{The design of an actor application}@} starts by decomposing {@{the task into independent actors}@}, drawing {@{a diagram of their interactions}@} and then wiring them together with {@{simple message types}@}. Then, following {@{the principles below}@} to implement {@{the actor application}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

Actors are {@{_event‑driven_}@}: they wait for {@{a message in their mailbox}@} and then {@{process it}@}. Because {@{sending a message is an asynchronous operation}@}, the sender continues {@{immediately without blocking}@}. This pattern keeps {@{the system responsive even under heavy load}@} and aligns with {@{reactive streams principles where data flows through event pipelines}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{An actor’s code}@} runs on {@{a dispatcher—a thread pool that can be shared among many actors}@}. The same dispatcher often executes {@{`Future` computations as well}@}, allowing actors to {@{off‑load work without spawning extra threads}@}. {@{Choosing an appropriate dispatcher (e.g., a bounded thread pool)}@} prevents actors from exhausting {@{system resources}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

Actors should expose only {@{immutable data to callers}@}. Inside an actor, {@{mutable fields may be used}@}, but they are never {@{shared with other code}@}. When an actor replies, it sends {@{a copy of its internal data rather than the original object}@}. Using {@{immutable snapshots}@} guarantees that {@{concurrent reads do not corrupt state}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

Actors often have {@{several logical states (e.g., idle, processing)}@}. The {@{`context.become` method}@} replaces {@{the current message handler with a new one and optionally keeps the old state}@}. {@{State‑specific logic is thus kept local}@}, reducing {@{accidental interaction with unrelated behaviours}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

When an actor sends {@{a blocking message to another actor}@} or starts {@{a `Future`}@}, the original actor must not read {@{its own mutable fields until the callback completes}@}. Any required data should be {@{copied into the message}@} so that it remains {@{valid during the call}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

By following {@{these guidelines}@}, {@{Scala actors}@} can form {@{robust, scalable reactive applications without the pitfalls of shared‑memory synchronization}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->
