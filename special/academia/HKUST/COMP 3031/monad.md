---
aliases:
  - COMP 3031 Scala monad
  - COMP 3031 Scala monads
  - COMP3031 Scala monad
  - COMP3031 Scala monads
  - HKUST COMP 3031 Scala monad
  - HKUST COMP 3031 Scala monads
  - HKUST COMP3031 Scala monad
  - HKUST COMP3031 Scala monads
  - Scala monad
tags:
  - flashcard/active/special/academia/HKUST/COMP_3031/monad
  - language/in/English
---

# Scala monad

- HKUST COMP 3031

In {@{functional programming}@}, {@{many data structures}@} that provide {@{`unit` \(also called `return`\) and `flatMap` \(also called `bind`\) operations}@} fall under {@{a common algebraic abstraction known as a _monad_}@}. <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

{@{The monad abstraction}@} underpins {@{many Scala types beyond collections}@}, such as {@{generators, options, and tries}@}. When {@{a type implements `flatMap`}@} \(and optionally {@{`withFilter` for _monads with zero_}@}\), it becomes {@{eligible to participate in Scala's `for`‑comprehensions}@}. {@{The three monad laws}@} provide designers with {@{powerful guidance}@}: they enforce {@{consistent composition semantics}@} and enable reasoning about {@{program behavior across different contexts}@}. <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

## motivation

{@{The Scala _for_ notation}@} is a concise syntax for expressing {@{compositional queries over collections}@}. {@{Its semantics}@} are essentially equivalent to {@{the map–flatMap–filter pipeline}@} that underlies {@{many database query languages}@}, and it can be applied to {@{any type that supplies `map`, `flatMap` and `withFilter` \(lazy version of `filter`\)}@}. <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

Indeed, any domain that {@{supplies these methods}@}—{@{booleans, strings, tuples, trees, even random number streams}@}—can participate in {@{a _for_ comprehension}@}. Further, such objects are called {@{_monads_}@} in {@{functional programming}@}, and they provide {@{a powerful abstraction for structuring programs}@}. <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

### generator

{@{A minimal abstraction}@} for producing {@{random values of some type `T`}@} is the following trait: <!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

> [!example] __`Generator` definition__
>
> {@{A minimal abstraction}@} for producing {@{random values of some type `T`}@} is the following trait:
>
> ```Scala
> trait Generator[+T] { def generate(): T }
> ```
<!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

{@{Concrete generators}@} can be created by {@{extending the trait `Generator`}@}.  For example, {@{an integer generator}@} that draws {@{from a `java.util.Random` instance}@} looks like <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

> [!example] __integer generator__
>
> For example, {@{an integer generator}@} that draws {@{from a `java.util.Random` instance}@} looks like
>
> ```Scala
> val integers = new Generator[Int]:
>   val rand = java.util.Random()
>   def generate() = rand.nextInt()
> ```
<!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

Using {@{the same pattern}@} one can define {@{a boolean generator}@}: <!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

> [!example] __boolean generator__
>
> Using {@{the same pattern}@} one can define {@{a boolean generator}@}:
>
> ```Scala
> val booleans = new Generator[Boolean]:
>   def generate() = integers.generate() > 0
> ```
<!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

and {@{a pair generator}@} that produces {@{two independent random integers}@}: <!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

> [!example] __pair generator__
>
> and {@{a pair generator}@} that produces {@{two independent random integers}@}:
>
> ```Scala
> val pairs = new Generator[(Int, Int)]:
>   def generate() = (integers.generate(), integers.generate())
> ```
<!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

#### generator monad

Rather than writing {@{a new anonymous class}@} for {@{each derived generator}@}, {@{the `Generator` trait}@} can be {@{enriched with higher‑order methods}@}. {@{An extension}@} that adds {@{`map`}@} is <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

> [!example] __`Generator.map`__
>
> {@{An extension}@} that adds {@{`map`}@} is
>
> ```Scala
> extension [T, S](g: Generator[T])
>   def map(f: T => S) = new Generator[S]:
>     def generate() = f(g.generate())
> ```
<!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

and {@{a corresponding extension}@} to add {@{`flatMap`}@}: <!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

> [!example] __`Generator.flatMap`__
>
> and {@{a corresponding extension}@} to add {@{`flatMap`}@}:
>
> ```Scala
> def flatMap(f: T => Generator[S]) = new Generator[S]:
>   def generate() = f(g.generate()).generate()
> ```
<!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

With {@{these in place}@}, {@{the boolean generator}@} can be written {@{succinctly using `map`}@} as <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

> [!example] __boolean generator using `map`__
>
> With {@{these in place}@}, {@{the boolean generator}@} can be {@{written succinctly}@} as
>
> ```Scala
> val booleans = integers.map(x => x > 0)
> ```
<!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

and {@{a generic pair generator}@} becomes, using {@{`flatMap`}@}: <!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

> [!example] __pair generator using `flatMap`__
>
> and {@{a generic pair generator}@} becomes, using {@{`flatMap`}@}:
>
> ```Scala
> def pairs[T, U](t: Generator[T], u: Generator[U]) =
>   t.flatMap(x => u.map(y => (x, y)))
> ```
<!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

The compiler rewrites {@{these _for_ expressions}@} in the same way {@{it does for collections}@}; {@{`for x <- g yield f(x)`}@} becomes {@{`g.map(f)`}@}, while {@{nested generators}@} translate into {@{successive calls to `flatMap`}@}. <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

#### generator monad recursion

{@{Generators}@} can be {@{combined recursively}@}. For example, {@{a generator of integer lists}@} is defined by first {@{choosing whether the list should be empty or non‑empty}@} and then {@{constructing it accordingly}@}: <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

> [!example] __integer list generator__
>
> For example, {@{a generator of integer lists}@} is defined by first {@{choosing whether the list should be empty or non‑empty}@} and then {@{constructing it accordingly}@}
>
> ```Scala
> def lists: Generator[List[Int]] =
>   for
>     isEmpty <- booleans
>     list    <- if isEmpty then single(Nil) else nonEmptyLists
>   yield list
> def nonEmptyLists: Generator[List[Int]] =
>   for
>     head <- integers
>     tail <- lists
>   yield head :: tail
> ```
<!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

{@{A more sophisticated example}@} is {@{a random tree generator}@}. Defining {@{the tree shape}@} as {@{an `enum`}@}: <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

> [!example] __`Tree` definition__
>
> {@{A more sophisticated example}@} is {@{a random tree generator}@}. Defining {@{the tree shape}@} as {@{an `enum`}@}:
>
> ```Scala
> enum Tree:
>   case Inner(left: Tree, right: Tree)
>   case Leaf(x: Int)
> ```
<!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

we can generate {@{leaves and inner nodes}@} by combining {@{existing generators}@}: <!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

> [!example] __tree generator__
>
> we can generate {@{leaves and inner nodes}@} by combining {@{existing generators}@}:
>
> ```Scala
> def leaves: Generator[Tree.Leaf] = for x <- integers yield Tree.Leaf(x)
> def inners: Generator[Tree.Inner] =
>   for l <- trees; r <- trees yield Tree.Inner(l, r)
> def trees: Generator[Tree] =
>   for
>     cutoff <- booleans
>     tree   <- if (cutoff) leaves else inners
>   yield tree
> ```
<!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

#### generator monad usage

{@{Unit tests}@} traditionally {@{supply concrete inputs and check a post‑condition}@}.  Using {@{generators}@}, one can instead {@{automatically produce many random test cases}@}: <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

> [!example] __unit test__
>
> {@{Unit tests}@} traditionally {@{supply concrete inputs and check a post‑condition}@}.  Using {@{generators}@}, one can instead {@{automatically produce many random test cases}@}:
>
> ```Scala
> def test[T](g: Generator[T], numTimes: Int = 100)(test: T => Boolean): Unit =
>   for i <- 0 until numTimes do
>     val value = g.generate()
>     assert(test(value), s"test failed for $value")
>   println(s"passed $numTimes tests")
> ```
<!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

{@{An example property}@} that {@{fails}@} is <!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

> [!example] __unit test usage__
>
> {@{An example property}@} that {@{fails}@} is
>
> ```Scala
> test(pairs(lists, lists)) {
>   case (xs, ys) => (xs ++ ys).length > xs.length
> }
> ```
>
> which should be corrected {@{to `>=` instead of `>`}@}.  This illustrates how {@{generators can reveal subtle invariants}@}. <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

The same idea is {@{used in the _ScalaCheck_ library}@}.  {@{A property expressed as a lambda}@} can be automatically {@{checked against many random inputs}@}: <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

> [!example] ___ScalaCheck___
>
> The same idea is {@{used in the _ScalaCheck_ library}@}.  {@{A property expressed as a lambda}@} can be automatically {@{checked against many random inputs}@}:
>
> ```Scala
> forAll { (l1: List[Int], l2: List[Int]) =>
>   (l1 ++ l2).size == l1.size + l2.size
> }
> ```
<!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

ScalaCheck integrates {@{with ScalaTest or can run stand‑alone}@}, providing a systematic way to {@{validate program behaviour without hand‑crafted test data}@}. <!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

## definition

{@{A monad}@} is defined for {@{a parametric type constructor `M[_]`}@}. {@{Two fundamental operations}@} must be supplied: <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

> [!example] __monad definition__
>
> {@{A monad}@} is defined for {@{a parametric type constructor `M[_]`}@}. {@{Two fundamental operations}@} must be supplied:
>
> ```Scala
> extension [T](m: M[T]) {
>   def flatMap[U](f: T => M[U]): M[U]
> }
> def unit[T](x: T): M[T]
> ```
<!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

{@{`flatMap`}@} chains {@{computations that may produce values wrapped in the monad}@}, while {@{`unit`}@} injects {@{a plain value into the monadic context}@}. Additionally, these operations must {@{respect the monad laws}@}. <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

In Scala, {@{`flatMap`}@} is typically {@{implemented as a method of the type itself or an extension method}@}; {@{`unit`}@} can be provided as {@{a constructor of the type}@}. <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

### monad laws

For a type to be {@{considered a true monad}@}, {@{three algebraic laws}@} must hold: \(annotation: 3 items: {@{associativity, left identity, right identity}@}\) <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

- __Associativity__ ::@:: `m.flatMap(f).flatMap(g) == m.flatMap(x => f(x).flatMap(g))` <!--SR:!2025-10-13,4,270!2025-10-13,4,270-->
- __Left Identity (Left Unit Law)__ ::@:: `unit(x).flatMap(f) == f(x)` <!--SR:!2025-10-13,4,270!2025-10-13,4,270-->
- __Right Identity (Right Unit Law)__ ::@:: `m.flatMap(unit) == m` <!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

{@{These laws}@} ensure that {@{monadic chaining behaves predictably}@}, enabling {@{reasoning about code and allowing optimizations}@}. <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

### `map`

Although monads only {@{require `flatMap` and `unit`}@}, {@{a `map` operation}@} can always be {@{defined in terms of them}@}: <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

> [!example] __monad `map`__
>
> Although monads only {@{require `flatMap` and `unit`}@}, {@{a `map` operation}@} can always be {@{defined in terms of them}@}:
>
> ```Scala
> m.map(f) == m.flatMap(x => unit(f(x)))
> m.map(f) == m.flatMap(f andThen unit)
> ```
<!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

Because {@{every monad supports this construction}@}, it is often convenient to {@{expose a dedicated `map` method for clarity}@}. <!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

## examples

{@{Typical examples}@} include: \(annotation: 4 items: {@{`List`, `Set`, `Option`, `Generator`}@}\) <!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

- `List`: ::@:: `unit(x) = List(x)` <!--SR:!2025-10-13,4,270!2025-10-13,4,270-->
- `Set`:  ::@:: `unit(x) = Set(x)` <!--SR:!2025-10-13,4,270!2025-10-13,4,270-->
- `Option`: ::@:: `unit(x) = Some(x)` <!--SR:!2025-10-13,4,270!2025-10-13,4,270-->
- `Generator`: ::@:: `unit(x) = single(x)` <!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

{@{All of these types}@} provide {@{a natural implementation of `flatMap`}@} that preserves {@{the structure of the container}@}. <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

## significance for `for`-expressions

{@{Scala's syntactic sugar}@} for {@{monadic composition}@} is {@{the `for`‑expression}@}. <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

{@{Associativity}@} guarantee that {@{nested `for`-expressions can always be collapsed into a single `for`-expression}@}: <!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

> [!example] __flatten `for`-expressions__
>
> {@{Associativity}@} guarantees that {@{nested `for`-expressions can always be flattened into a single `for`-expression}@}:
>
> ```Scala
> for {
>   y <- for { x <- m; y <- f(x) } yield y
>   z <- g(y)
> } yield z
> == for { x <- m; y <- f(x); z <- g(y) } yield z
> ```
<!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

{@{The right‑unit law}@} implies that {@{a single generator without further bindings}@} is {@{equivalent to the monad itself}@} ({@{`for { x <- m } yield x == m`}@}). {@{The left‑unit law ensures}@} that {@{a binding from `unit(x)` followed by another function}@} simply yields {@{that function applied to `x`}@} ({@{`for { y <- unit(x); r <- f(y) } yield r == f(x)`}@}). <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

## `Option`

For instance, consider {@{Scala's `Option`}@}. {@{Its `flatMap`}@} is defined by {@{pattern matching}@}: <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

> [!example] __`Option.flatMap`__
>
> For instance, consider {@{Scala's `Option`}@}. {@{Its `flatMap`}@} is defined by {@{pattern matching}@}:
>
> ```Scala
> extension [T](xo: Option[T]) {
>   def flatMap[U](f: T => Option[U]): Option[U] =
>     xo match { case Some(x) => f(x); case None => None }
> }
> ```
<!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

Using {@{simple algebraic reasoning}@}, one can verify that {@{all three laws hold for `Option`}@}. {@{The left‑unit law}@} is immediate because {@{`Some(x).flatMap(f)` evaluates to `f(x)`}@}, and {@{the right‑unit law}@} follows from the fact that {@{mapping a value with `unit` (i.e., `Some`) leaves it unchanged}@}. {@{Associativity}@} can be shown by unfolding {@{both sides and observing that they reduce to identical pattern matches}@}. <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

## `Try`

While {@{exceptions}@} are {@{inexpensive in Scala}@}, they have {@{drawbacks}@}: \(annotation: 2 items: {@{no effect on function type, cross-evaluation context}@}\) <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

- no effect on function type ::@:: The types of functions that may throw are not reflected in the signature (unlike Java's `throws` clause). <!--SR:!2025-10-13,4,270!2025-10-13,4,270-->
- cross-evaluation context ::@:: Exceptions can only propagate within the current evaluation context \(e.g. current thread\). They do not propagate naturally across threads or asynchronous boundaries. <!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

Because of {@{these issues}@}, it is sometimes preferable to treat {@{failures as ordinary values}@}. {@{This idea}@} is captured by {@{the `scala.util.Try` _monad_ type}@}. <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

{@{`scala.util.Try`}@} behaves like{@{ an `Option`}@}, but distinguishes {@{between success and failure}@}: <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

> [!example] __`Try` definition__
>
> {@{`scala.util.Try`}@} behaves like{@{ an `Option`}@}, but distinguishes {@{between success and failure}@}:
>
> ```Scala
> abstract class Try[+T]
> case class Success[+T](x: T) extends Try[T]
> case class Failure(ex: Exception) extends Try[Nothing]
> ```
<!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

{@{A convenient factory for `Try`}@} wraps {@{arbitrary computations}@}: <!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

> [!example] __`Try.apply`__
>
> {@{A convenient factory for `Try`}@} wraps {@{arbitrary computations}@}:
>
> ```Scala
> object Try {
>   def apply[T](expr: => T): Try[T] =
>     try Success(expr)
>     catch case NonFatal(ex) => Failure(ex)
> }
> ```
<!--SR:!2025-10-13,4,270!2025-10-13,4,270-->

{@{`Try`}@} supports {@{monadic composition}@} via {@{`flatMap` and `map`}@}: <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

> [!example] __`Try.flatMap`__
>
> {@{`Try`}@} supports {@{monadic composition}@} via {@{`flatMap` and `map`}@}:
>
> ```Scala
> extension [T](xt: Try[T]) {
>   def flatMap[U](f: T => Try[U]): Try[U] = xt match {
>     case Success(x) => try f(x) catch { case NonFatal(ex) => Failure(ex) }
>     case fail: Failure => fail
>   }
>   def map[U](f: T => U): Try[U] = xt match {
>     case Success(x) => Try(f(x))
>     case fail: Failure => fail
>   }
> }
> ```
<!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

Thus {@{`t.map(f)`}@} equals {@{`t.flatMap(x => Try(f(x)))`}@}, mirroring {@{the general monadic definition of `map`}@}. <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->

One might ask whether {@{`Try` satisfies the monad laws with `unit = Try.apply`}@}. {@{The left‑unit law}@} fails: {@{`Try(expr).flatMap(f)`}@} will {@{never throw a non‑fatal exception}@}, whereas {@{`f(expr)` may}@}. Consequently, `Try` trades {@{the left identity law}@} for {@{a useful property}@}—{@{any composition of `Try`, `map`, and `flatMap`}@} guarantees that {@{no non‑fatal exception propagates outward}@} ({@{the "bullet‑proof" principle}@}\). <!--SR:!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270!2025-10-13,4,270-->
