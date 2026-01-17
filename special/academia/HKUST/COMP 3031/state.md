---
aliases:
  - COMP 3031 Scala state
  - COMP 3031 Scala states
  - COMP3031 Scala state
  - COMP3031 Scala states
  - HKUST COMP 3031 Scala state
  - HKUST COMP 3031 Scala states
  - HKUST COMP3031 Scala state
  - HKUST COMP3031 Scala states
  - Scala state
  - Scala states
tags:
  - flashcard/active/special/academia/HKUST/COMP_3031/state
  - language/in/English
---

# Scala state

- HKUST COMP 3031

---

- see: [general/state (computer science)](../../../../general/state%20(computer%20science).md)

{@{__State__}@} is the notion that {@{a program can carry data that changes over time}@}, breaking {@{referential transparency}@}. In {@{functional programming}@} we usually {@{try to avoid it}@}, but in {@{many practical systems – such as databases or user interfaces}@} – {@{mutable state is unavoidable}@}. The following sections describe how {@{Scala models state and why it matters for reasoning about programs}@}. <!--SR:!2026-01-26,15,290!2026-01-26,15,290!2026-01-26,15,290!2026-01-25,14,290!2026-01-25,14,290!2026-01-25,14,290!2026-01-26,15,290!2026-01-26,15,290-->

## substitution model

{@{The λ‑calculus}@} treats {@{a program as a series of substitutions}@}. {@{A function application `f(v)`}@} is rewritten by replacing {@{the formal parameter with the actual argument in the body}@}: <!--SR:!2026-01-25,14,290!2026-01-26,15,290!2026-01-26,15,290!2026-01-25,14,290-->

> [!example] __substitution rule__
>
> {@{The substitution rule}@} rewrites {@{a function application by substituting the argument for the parameter}@}:
>
> ```Scala
> def f(x: Int) = x + 1
> f(3)  // → 3 + 1 → 4
> ```
<!--SR:!2026-01-25,14,290!2026-01-25,14,290-->

{@{This rewriting}@} is {@{deterministic}@}, so if {@{a program terminates it always yields the same result}@}. {@{The Church–Rosser theorem}@} guarantees that {@{any two valid rewrite sequences converge to the same value}@}. A concrete illustration uses {@{`iterate` and `square`}@}: <!--SR:!2026-01-26,15,290!2026-01-25,14,290!2026-01-26,15,290!2026-01-26,15,290!2026-01-26,15,290!2026-01-25,14,290-->

> [!example] __rewrite of `iterate`__
>
> {@{Rewriting steps}@} for {@{`iterate(1, square, 3)`}@}:
>
> ```Scala
> iterate(1, square, 3)
> // → if 1 == 0 then 3 else iterate(0, square, square(3))
> // → iterate(0, square, square(3))
> // → iterate(0, square, 9)
> // → if 0 == 0 then 9 else iterate(-1, square, square(9))
> // → 9
> ```
>
> {@{The sequence}@} ends with {@{the same result regardless of the order}@} in which {@{sub‑expressions are reduced}@}. <!--SR:!2026-01-25,14,290!2026-01-25,14,290!2026-01-26,15,290!2026-01-25,14,290!2026-01-25,14,290-->

## statefulness

{@{A _stateful object_}@} is one whose {@{behaviour depends on a history of updates}@}. Typical implementations use {@{mutable variables (`var`) or private fields that can be changed by methods}@}. <!--SR:!2026-01-25,14,290!2026-01-25,14,290!2026-01-25,14,290-->

> [!example] __`BankAccount`__
>
> {@{A _stateful object_}@} is one whose {@{behaviour depends on a history of updates}@}. Typical implementations use {@{mutable variables (`var`) or private fields that can be changed by methods}@}.
>
> ```Scala
> class BankAccount:
>   private var balance = 0
>   def deposit(amount: Int): Unit =
>     if amount > 0 then balance += amount
>   def withdraw(amount: Int): Int =
>     if 0 < amount && amount <= balance then
>       balance -= amount; balance
>     else throw new IllegalArgumentException("insufficient funds")
> ```
>
> {@{The field `balance`}@} is mutated by {@{`deposit` and `withdraw`}@}, so {@{two calls to the same object can produce different results}@}. <!--SR:!2026-01-26,15,290!2026-01-26,15,290!2026-01-26,15,290!2026-01-25,14,290!2026-01-25,14,290!2026-01-25,14,290-->

{@{Scala objects}@} are {@{instances of classes}@}, therefore an instance that {@{contains a mutable field is (usually; see below) stateful}@}. {@{A proxy class}@} delegating to {@{another stateful object also carries state}@}: <!--SR:!2026-01-25,14,290!2026-01-25,14,290!2026-01-25,14,290!2026-01-26,15,290!2026-01-26,15,290-->

> [!example] __stateful proxy__
>
> {@{The wrapper}@} forwards operations but shares {@{the underlying account’s state}@}:
>
> ```Scala
> class BankAccountProxy(ba: BankAccount):
>   def deposit(amount: Int): Unit = ba.deposit(amount)
>   def withdraw(amount: Int): Int = ba.withdraw(amount)
> ```
<!--SR:!2026-01-25,14,290!2026-01-25,14,290-->

{@{Instances of `BankAccountProxy`}@} are {@{stateful}@} because they expose {@{the mutable behaviour of the wrapped account}@}, showing that {@{statefulness is _infectious_}@}. <!--SR:!2026-01-26,15,290!2026-01-26,15,290!2026-01-26,15,290!2026-01-26,15,290-->

Sometimes, {@{a function}@} may be either {@{stateless or stateful depending on the function inputs}@}. For example, {@{a lazy list built with a mutable field to cache the `tail`}@} is either {@{stateless or stateful}@} depending if {@{the `tail` expression `tl` is stateful}@}: <!--SR:!2026-01-26,15,290!2026-01-25,14,290!2026-01-26,15,290!2026-01-25,14,290!2026-01-25,14,290-->

> [!example] __mutable tail list implementation__
>
> {@{A lazy list built with a mutable field to cache the `tail`}@} is either {@{stateless or stateful}@} depending if {@{the `tail` expression `tl` is stateful}@}:
>
> ```Scala
> def cons[T](hd: T, tl: => TailLazyList[T]) = new TailLazyList[T]:
>   private var tlOpt: Option[TailLazyList[T]] = None
>   def tail: T =
>     tlOpt match
>       case Some(x) => x
>       case None =>
>         tlOpt = Some(tl); tail
> ```
<!--SR:!2026-01-25,14,290!2026-01-26,15,290!2026-01-26,15,290-->

## `var`

{@{Variables declared with `var`}@} can be {@{reassigned}@}: <!--SR:!2026-01-25,14,290!2026-01-26,15,290-->

> [!example] __`var__
>
> {@{Variables declared with `var`}@} can be {@{reassigned}@}:
>
> ```Scala
> var x: String = "abc"
> x = "hi"  // fails if `val` instead of `var` is used
> ```
<!--SR:!2026-01-25,14,290!2026-01-26,15,290-->

## operational equivalence

{@{_Referential transparency_}@} relies on {@{immutable values}@}. When {@{`val x = E; val y = E` where `E` is an expression}@} holds, the two bindings are {@{considered identical}@}. {@{Mutable assignments}@} break {@{this property: different objects created with the same expression may behave differently}@}. <!--SR:!2026-01-26,15,290!2026-01-25,14,290!2026-01-26,15,290!2026-01-26,15,290!2026-01-25,14,290!2026-01-25,14,290-->

{@{Two definitions `x` and `y` are _operationally equivalent_}@} if {@{every possible sequence of operations applied to them yields indistinguishable results}@}. A test consists of executing {@{a program fragment `S` that uses `x` and `y`}@}, then creating {@{a copy `S'` where all occurrences of `y` are replaced by `x`}@}. If {@{the outcomes differ}@}, the two values are {@{not equivalent}@}. <!--SR:!2026-01-26,15,290!2026-01-26,15,290!2026-01-25,14,290!2026-01-26,15,290!2026-01-25,14,290!2026-01-25,14,290-->

> [!example] __operational equivalence test__
>
> {@{The two programs}@} produce {@{different results}@}, so {@{`x` and `y` are not _operationally equivalent_}@}.
>
> ```Scala
> val x = BankAccount()
> val y = BankAccount()
> // S :  x.deposit(30); y.withdraw(20)
> // S':  x.deposit(30); x.withdraw(20)
> ```
>
> If we define {@{`val y = x`}@}, {@{no test can distinguish them}@}; they are {@{operationally the same}@}. <!--SR:!2026-01-25,14,290!2026-01-25,14,290!2026-01-26,15,290!2026-01-26,15,290!2026-01-26,15,290!2026-01-25,14,290-->

{@{The λ‑calculus substitution model}@} replaces {@{a variable by its defining expression}@}. It works for {@{immutable values but fails when mutable state is involved}@}, because replacing {@{a reference with another object changes behaviour}@}. <!--SR:!2026-01-25,14,290!2026-01-25,14,290!2026-01-25,14,290!2026-01-25,14,290-->

> [!example] __substitution failure__
>
> {@{The λ‑calculus substitution model}@} replaces {@{a variable by its defining expression}@}. It works for {@{immutable values but fails when mutable state is involved}@}, because replacing {@{a reference with another object changes behaviour}@}.
>
> ```Scala
> val x = BankAccount()
> val y = x          // y refers to the same account
> // Substituting y with BankAccount() would change the program
> ```
<!--SR:!2026-01-26,15,290!2026-01-25,14,290!2026-01-26,15,290!2026-01-25,14,290-->

{@{A model more robust than the substitution model}@} introduces {@{a store that tracks mutable objects}@}, but this adds {@{considerable complexity}@}. <!--SR:!2026-01-25,14,290!2026-01-26,15,290!2026-01-26,15,290-->
