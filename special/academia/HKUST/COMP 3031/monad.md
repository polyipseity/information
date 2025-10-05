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

## motivation

{@{The Scala _for_ notation}@} is a concise syntax for expressing {@{compositional queries over collections}@}. {@{Its semantics}@} are essentially equivalent to {@{the map–flatMap–filter pipeline}@} that underlies {@{many database query languages}@}, and it can be applied to {@{any type that supplies `map`, `flatMap` and `withFilter` \(lazy version of `filter`\)}@}.

Indeed, any domain that {@{supplies these methods}@}—{@{booleans, strings, tuples, trees, even random number streams}@}—can participate in {@{a _for_ comprehension}@}. Further, such objects are called {@{_monads_}@} in {@{functional programming}@}, and they provide {@{a powerful abstraction for structuring programs}@}.

### generator

{@{A minimal abstraction}@} for producing {@{random values of some type `T`}@} is the following trait:

> [!example] __`Generator` definition__
>
> {@{A minimal abstraction}@} for producing {@{random values of some type `T`}@} is the following trait:
>
> ```Scala
> trait Generator[+T] { def generate(): T }
> ```

{@{Concrete generators}@} can be created by {@{extending the trait `Generator`}@}.  For example, {@{an integer generator}@} that draws {@{from a `java.util.Random` instance}@} looks like

> [!example] __integer generator__
>
> For example, {@{an integer generator}@} that draws {@{from a `java.util.Random` instance}@} looks like
>
> ```Scala
> val integers = new Generator[Int]:
>   val rand = java.util.Random()
>   def generate() = rand.nextInt()
> ```

Using {@{the same pattern}@} one can define {@{a boolean generator}@}:

> [!example] __boolean generator__
>
> Using {@{the same pattern}@} one can define {@{a boolean generator}@}:
>
> ```Scala
> val booleans = new Generator[Boolean]:
>   def generate() = integers.generate() > 0
> ```

and {@{a pair generator}@} that produces {@{two independent random integers}@}:

> [!example] __pair generator__
>
> and {@{a pair generator}@} that produces {@{two independent random integers}@}:
>
> ```Scala
> val pairs = new Generator[(Int, Int)]:
>   def generate() = (integers.generate(), integers.generate())
> ```

#### generator monad

Rather than writing {@{a new anonymous class}@} for {@{each derived generator}@}, {@{the `Generator` trait}@} can be {@{enriched with higher‑order methods}@}. {@{An extension}@} that adds {@{`map`}@} is

> [!example] __`Generator.map`__
>
> {@{An extension}@} that adds {@{`map`}@} is
>
> ```Scala
> extension [T, S](g: Generator[T])
>   def map(f: T => S) = new Generator[S]:
>     def generate() = f(g.generate())
> ```

and {@{a corresponding extension}@} to add {@{`flatMap`}@}:

> [!example] __`Generator.flatMap`__
>
> and {@{a corresponding extension}@} to add {@{`flatMap`}@}:
>
> ```Scala
> def flatMap(f: T => Generator[S]) = new Generator[S]:
>   def generate() = f(g.generate()).generate()
> ```

With {@{these in place}@}, {@{the boolean generator}@} can be written {@{succinctly using `map`}@} as

> [!example] __boolean generator using `map`__
>
> With {@{these in place}@}, {@{the boolean generator}@} can be {@{written succinctly}@} as
>
> ```Scala
> val booleans = integers.map(x => x > 0)
> ```

and {@{a generic pair generator}@} becomes, using {@{`flatMap`}@}:

> [!example] __pair generator using `flatMap`__
>
> and {@{a generic pair generator}@} becomes, using {@{`flatMap`}@}:
>
> ```Scala
> def pairs[T, U](t: Generator[T], u: Generator[U]) =
>   t.flatMap(x => u.map(y => (x, y)))
> ```

The compiler rewrites {@{these _for_ expressions}@} in the same way {@{it does for collections}@}; {@{`for x <- g yield f(x)`}@} becomes {@{`g.map(f)`}@}, while {@{nested generators}@} translate into {@{successive calls to `flatMap`}@}.

#### generator monad recursion

{@{Generators}@} can be {@{combined recursively}@}. For example, {@{a generator of integer lists}@} is defined by first {@{choosing whether the list should be empty or non‑empty}@} and then {@{constructing it accordingly}@}:

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

{@{A more sophisticated example}@} is {@{a random tree generator}@}. Defining {@{the tree shape}@} as {@{an `enum`}@}:

> [!example] __`Tree` definition__
>
> {@{A more sophisticated example}@} is {@{a random tree generator}@}. Defining {@{the tree shape}@} as {@{an `enum`}@}:
>
> ```Scala
> enum Tree:
>   case Inner(left: Tree, right: Tree)
>   case Leaf(x: Int)
> ```

we can generate {@{leaves and inner nodes}@} by combining {@{existing generators}@}:

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

#### generator monad usage

{@{Unit tests}@} traditionally {@{supply concrete inputs and check a post‑condition}@}.  Using {@{generators}@}, one can instead {@{automatically produce many random test cases}@}:

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

{@{An example property}@} that {@{fails}@} is

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
> which should be corrected {@{to `>=` instead of `>`}@}.  This illustrates how {@{generators can reveal subtle invariants}@}.

The same idea is {@{used in the _ScalaCheck_ library}@}.  {@{A property expressed as a lambda}@} can be automatically {@{checked against many random inputs}@}:

> [!example] ___ScalaCheck___
>
> The same idea is {@{used in the _ScalaCheck_ library}@}.  {@{A property expressed as a lambda}@} can be automatically {@{checked against many random inputs}@}:
>
> ```Scala
> forAll { (l1: List[Int], l2: List[Int]) =>
>   (l1 ++ l2).size == l1.size + l2.size
> }
> ```

ScalaCheck integrates {@{with ScalaTest or can run stand‑alone}@}, providing a systematic way to {@{validate program behaviour without hand‑crafted test data}@}.
