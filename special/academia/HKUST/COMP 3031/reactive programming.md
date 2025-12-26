---
aliases:
  - COMP 3031 Scala reactive programming
  - COMP3031 Scala reactive programming
  - HKUST COMP 3031 Scala reactive programming
  - HKUST COMP3031 Scala reactive programming
  - Scala reactive programming
tags:
  - flashcard/active/special/academia/HKUST/COMP_3031/reactive_programming
  - language/in/English
---

# Scala reactive programming

- HKUST COMP 3031

---

- see: [general/reactive programming](../../../../general/reactive%20programming.md)

{@{__Reactive programming__}@} can be compared with {@{the classic _observer_ pattern}@}, which then hints at {@{a more functional alternative in Scala}@}.

## observer pattern

In {@{the classic _observer_ pattern}@}, {@{a model publishes events to interested observers}@} that react by {@{updating views or other state}@}. In the following sections we describe how this pattern can be implemented, why it has drawbacks, and hint at a more functional alternative.

{@{The core idea}@} is that {@{a _publisher_ keeps a set of _subscribers_}@}. {@{A subscriber implements `handler`}@} so that it receives {@{notifications from the publisher whenever something changes}@}. The publisher offers three operations: {@{`subscribe`, `unsubscribe`}@} and {@{`publish`}@}.

> [!example] __publisher/subscriber traits__  
>
> {@{The core idea}@} is that {@{a _publisher_ keeps a set of _subscribers_}@}. {@{A subscriber implements `handler`}@} so that it receives {@{notifications from the publisher whenever something changes}@}. The publisher offers three operations: {@{`subscribe`, `unsubscribe`}@} and {@{`publish`}@}.
>
> ```Scala
> trait Subscriber { def handler(pub: Publisher): Unit }
> 
> trait Publisher {
>   private var subs = Set.empty[Subscriber]
>   def subscribe(sub: Subscriber): Unit = subs += sub
>   def unsubscribe(sub: Subscriber): Unit = subs -= sub
>   def publish(): Unit = subs.foreach(_.handler(this))
> }
> ```

### observer pattern example

{@{A bank account}@} can expose {@{its balance and notify observers whenever the balance changes}@}. {@{The `deposit` and `withdraw` methods}@} update {@{the internal state and call `publish`}@}.

> [!example] __`BankAccount` publisher__  
>
> {@{A bank account}@} can expose {@{its balance and notify observers whenever the balance changes}@}. {@{The `deposit` and `withdraw` methods}@} update {@{the internal state and call `publish`}@}.
>
> ```Scala
> class BankAccount extends Publisher {
>   private var bal = 0
>   def currentBalance: Int = bal
>   def deposit(a:Int): Unit =
>     if a > 0 then { bal += a; publish() }
>   def withdraw(a:Int): Unit =
>     if a > 0 && a <= bal then { bal -= a; publish() } else throw Error()
> }
> ```

{@{An observer that keeps the total of many bank accounts}@} can be written as {@{a single subscriber}@}. It registers {@{itself with every account}@}, computes {@{the sum on each notification and exposes it through `totalBalance`}@}.

> [!example] __`Consolidator` subscriber__  
>
> {@{An observer that keeps the total of many bank accounts}@} can be written as {@{a single subscriber}@}. It registers {@{itself with every account}@}, computes {@{the sum on each notification and exposes it through `totalBalance`}@}.
>
> ```Scala
> class Consolidator(observed: List[BankAccount]) extends Subscriber {
>   observed.foreach(_.subscribe(this))
>   private var total = compute()
>   def compute() = observed.map(_.currentBalance).sum
>   def handler(pub: Publisher): Unit = { total = compute() }
>   def totalBalance: Int = total
> }
> ```

### shortcomings of the observer pattern

{@{The observer style}@} is {@{_imperative_}@}: handlers are {@{side-effecting and tightly couple views to model state}@}. They must be {@{registered manually}@}, and concurrency can introduce {@{subtle bugs when notifications arrive while an update is in progress}@}.

{@{A more compositional approach}@} treats {@{events as first-class values}@} and chains {@{them with combinators such as `map`, `filter` or `scan`}@}. This removes the need for {@{explicit subscription lists}@} and makes it easier to {@{reason about data flow}@}.

## functional reactive programming

{@{Functional reactive programming (FRP) in Scala}@} moves beyond {@{the classic observer pattern}@} by treating {@{time-varying values as first-class citizens called _signals_}@}. Signals let us compose {@{computations over changing data without the manual bookkeeping of subscribers}@}, and they fit naturally into {@{a functional style}@}. It replaces {@{event-based callbacks with declarative combinators such as `map` and `filter`}@}.

## signals

FRP describes programs that react {@{to sequences of events or signals}@}. {@{A _signal_}@} represents {@{a value that can change over time}@}; it is modelled as {@{a function from time to a value}@}. Instead of {@{mutating state}@}, new signals are defined {@{in terms of existing ones}@}. For example, {@{the current mouse position}@} could be expressed as

> [!example] __mouse position signal__  
>
> Instead of {@{mutating state}@}, new signals are defined {@{in terms of existing ones}@}. For example, {@{the current mouse position}@} could be expressed as
>
> `val mousePosition: Signal[Position] = ...`
>
> {@{The value `mousePosition()`}@} yields {@{the latest coordinates}@}.

{@{A minimal `Signal` type}@} can be {@{written as follows}@}:

> [!example] __minimal `Signal`__  
>
> {@{A minimal `Signal` type}@} can be {@{written as follows}@}:
>
> ```Scala
> class Signal[T](f: () => T) { def apply() = f() }
> ```

{@{The `Signal` type}@} is {@{immutable}@}; its value is {@{computed when `apply()` is called}@}. {@{`Signal.Var`}@} extends {@{`Signal` with an `update` method}@}, allowing {@{direct mutation}@}:

> [!example] __`Signal.Var` usage__
>
> {@{`Signal.Var`}@} extends {@{`Signal` with an `update` method}@}, allowing {@{direct mutation}@}:
>
> ```Scala
> val v = Signal.Var(3)  // v() == 3
> v.update(5)            // now v() == 5
> ```
>
> {@{The syntax `v() = 5`}@} is {@{syntactic sugar for `v.update(5)`}@}.

{@{Signals can be combined}@} to yield {@{new signals}@}:

> [!example] __`Signal` combinator__  
>
> {@{Signals can be combined}@} to yield {@{new signals}@}:
>
> ```Scala
> val x = Signal.Var(1)
> val y = Signal(x() * 2)   // y always equals twice the current x
> ```

### signal example

{@{A bank account}@} becomes {@{a publisher of its own balance signal}@}:

> [!example] __signal-based `BankAccount`__  
>
> {@{A bank account}@} becomes {@{a publisher of its own balance signal}@}:
>
> ```Scala
> class BankAccount { 
>   private val bal = Signal.Var(0)
>   def balance: Signal[Int] = bal
>   def deposit(a:Int): Unit =
>     if a > 0 then bal() = bal() + a
>   def withdraw(a:Int): Int =
>     if 0 < a && a <= bal() then { bal() = bal() - a; bal() } 
>     else throw Error("insufficient funds")
> }
> ```

{@{A _consolidator_}@} aggregates {@{balances of many accounts}@}:

> [!example] __signal-based `consolidated`__  
>
> {@{A _consolidator_}@} aggregates {@{balances of many accounts}@}:
>
> ```Scala
> def consolidated(accounts: BankAccount*): Signal[Int] =
>   Signal(accounts.map(_.balance()).sum)
> ```
>
> {@{The signal `c = consolidated(accounts)`}@} reflects {@{the total automatically whenever any account changes}@}.

### signal reassignment

{@{Updating a signal}@} must go through {@{the `Signal` object}@} rather than {@{reassigning to the `Signal` variable}@}.

> [!example] __signal reassignment__
>
> {@{Updating a signal}@} must go through {@{the `Signal` object}@} rather than {@{reassigning to the `Signal` variable}@}. For instance, the following {@{changes `twice`}@}:
>
> ```Scala
> val num = Signal.Var(1)
> val twice = Signal(num() * 2)  // `twice` depends on current `num`
> num.update(2)                  // `twice` becomes 4
> ```
>
> But {@{writing the following}@} does _not_ {@{change `twice`}@}:
>
> ```Scala
> var num = Signal.Var(1)
> val twice = Signal(num() * 2)  // `twice` depends on current `num`
> num = Signal.Var(2)            // `twice` remains 2
> ```
>
> Instead, it replaces {@{the variable `num` with a new signal, leaving `twice` bound to the old one}@}.  Hence {@{the final value of `twice()`}@} differs {@{from the first fragment}@}.

### signal implementation

{@{The core of a Scala FRP library}@} is {@{the `Signal` abstraction and its mutable variant `Var`}@}. {@{A `Signal[T]`}@} represents {@{a value that can change over time}@}; {@{a `Var[T]`}@} extends {@{it with an `update` method}@} so callers can {@{re-define the underlying expression}@}. {@{The implementation hides details}@} inside {@{the companion object `frp.Signal`}@}.

> [!example] __FRP interface__
>
> {@{The core of a Scala FRP library}@} is {@{the `Signal` abstraction and its mutable variant `Var`}@}. {@{A `Signal[T]`}@} represents {@{a value that can change over time}@}; {@{a `Var[T]`}@} extends {@{it with an `update` method}@} so callers can {@{re-define the underlying expression}@}. {@{The implementation hides details}@} inside {@{the companion object `frp.Signal`}@}.
>
> ```Scala
> trait Signal[+T] { def apply(): T }
> object Signal {
>   def apply[T](expr: => T): Signal[T]
>   class Var[T](initExpr: => T) extends Signal[T] {
>     def update(expr: => T): Unit = ...
>   }
> }
> ```
>
> Notice that {@{`T` in `Signal`}@} is {@{covariant while `T` in `Signal.Var` is invariant}@}, due to {@{their different mutability}@}.

{@{`Signal`}@} constructs {@{a signal from an expression}@}. {@{A `Signal.Var`}@} keeps {@{the current expression and can be updated to a new one}@}.

> [!example] __creating signals__  
>
> {@{`Signal`}@} constructs {@{a signal from an expression}@}. {@{A `Signal.Var`}@} keeps {@{the current expression and can be updated to a new one}@}.
>
> ```Scala
> val time = Signal.Var(0)
> val doubled = Signal(time() * 2)
> time.update(1)  // `Signal.Var` can be updated
> ```

{@{The presented implementation}@} is {@{a minimal, imperative-style FRP}@} that works for {@{discrete signals}@}. It does not guarantee {@{thread safety}@} and treats {@{continuous values only by sampling}@}. {@{More sophisticated libraries}@} add {@{pure propagation, event streams, and continuous time support}@}.

#### dependency tracking

When {@{a signal is read}@}, it registers {@{the calling signal as an observer}@}, which is represented by {@{an opaque type `Signal.Observer`}@}. If {@{its value changes}@}, the observer set is {@{copied and cleared first}@} so that {@{new dependencies (caused by re-evaluation) can be recorded}@}, and then {@{all observers in the copy are re-evaluated}@}.

> [!example] __reevaluation logic__  
>
> When {@{a signal is read}@}, it registers {@{the calling signal as an observer}@}, which is represented by {@{an opaque type `Signal.Observer`}@}. If {@{its value changes}@}, the observer set is {@{copied and cleared first}@} so that {@{new dependencies (caused by re-evaluation) can be recorded}@}, and then {@{all observers in the copy are re-evaluated}@}.
>
> ```Scala
> object Signal:
>   opaque type Observer = AbstractSignal[?]
>   // ...
>   class AbstractSignal[+T] /* ... */:
>     // ...
>     protected def computeValue(): Unit = {
>       val newVal = eval()
>       if (newVal != current) {
>         current = newVal
>         val obs: Set[Observer] = observers
>         observers = Set()
>         obs.foreach(_.computeValue())
>       }
>     }
>     // ...
> ```

To know {@{on whose behalf a signal expression is evaluated}@}, each signal must record {@{the _caller_ that triggered its computation}@}.{@{ The straightforward approach}@} is to thread {@{an explicit `Signal.Observer` argument through every call}@}: replace {@{`expr: () => T` with `expr: Signal.Observer => T`}@}. During evaluation, `s()` {@{would be rewritten as `s(caller)`}@}, where `caller` {@{denotes the signal that requested the value}@}. This technique {@{works but introduces a lot of boilerplate and is easy to misuse}@}. Scala solves it by treating {@{the caller as an _implicit_ using argument}@}. With {@{`def expr: (using Signal.Observer) => T`}@} (not {@{valid Scala syntax}@}) the compiler {@{automatically supplies the current observer}@}, making signal definitions look like {@{ordinary code while still wiring up dependencies}@}.

> [!example] __implicit caller injection__  
>
> With {@{`def expr: (using Signal.Observer) => T`}@} (not {@{valid Scala syntax}@}) the compiler {@{automatically supplies the current observer}@}, making signal definitions look like {@{ordinary code while still wiring up dependencies}@}.
>
> ```Scala
> def foo()(using Signal.Observer): Int = Signal { /* body */ }
> ```
>
> The caller is {@{injected implicitly}@}, so users do not have to {@{manage it manually}@}. Using {@{_implicit function types_}@}, it may be {@{simplified further}@}:
>
> ```Scala
> type Observed[T] = Signal.Observer ?=> T
> def foo(): Observed[Int] = Signal { /* body */ }
> ```

{@{The `noObserver` value}@} in {@{the companion object of `Signal`}@} provides {@{a default `Signal.Observer` context for top-level evaluations}@}, ensuring that {@{a signal can be read from ordinary code}@}.

> [!example] __default `Signal.Observer`__  
>
> {@{The `noObserver` value}@} in {@{the companion object of `Signal`}@} provides {@{a default `Signal.Observer` context for top-level evaluations}@}, ensuring that {@{a signal can be read from ordinary code}@}.
>
> ```Scala
> given noObserver: Signal.Observer = new AbstractSignal[Unit] {
>   def eval() = ()
>   override def computeValue() = ()
> }
> ```
