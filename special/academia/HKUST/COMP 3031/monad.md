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

In {@{functional programming}@}, {@{many data structures}@} that provide {@{`unit` \(also called `return`\) and `flatMap` \(also called `bind`\) operations}@} fall under {@{a common algebraic abstraction known as a _monad_}@}. <!--SR:!2026-10-28,284,330!2026-10-12,271,330!fsrs,2029-07-22T00:00:00.000Z,1049,1049.13725568,1,2,9,0,0,2026-09-07T00:00:00.000Z!2026-10-27,283,330-->

{@{The monad abstraction}@} underpins {@{many Scala types beyond collections}@}, such as {@{generators, options, and tries}@}. When {@{a type implements `flatMap`}@} \(and optionally {@{`withFilter` for _monads with zero_}@}\), it becomes {@{eligible to participate in Scala's `for`-comprehensions}@}. {@{The three monad laws}@} provide designers with {@{powerful guidance}@}: they enforce {@{consistent composition semantics}@} and enable reasoning about {@{program behavior across different contexts}@}. <!--SR:!2026-11-04,290,330!2026-11-05,291,330!fsrs,2028-02-03T00:00:00.000Z,508,507.95545468,5.00637887,2,9,0,0,2026-09-13T00:00:00.000Z!2026-11-07,293,330!2026-10-31,287,330!2026-10-11,270,330!fsrs,2029-12-23T00:00:00.000Z,1172,1172.20432607,1,2,9,0,0,2026-10-08T00:00:00.000Z!fsrs,2028-08-16T00:00:00.000Z,698,697.52483893,2.49272837,2,9,0,0,2026-09-18T00:00:00.000Z!2026-11-02,289,330!fsrs,2029-12-28T00:00:00.000Z,1176,1176.0199518,1,2,9,0,0,2026-10-09T00:00:00.000Z-->

## motivation

{@{The Scala _for_ notation}@} is a concise syntax for expressing {@{compositional queries over collections}@}. {@{Its semantics}@} are essentially equivalent to {@{the map–flatMap–filter pipeline}@} that underlies {@{many database query languages}@}, and it can be applied to {@{any type that supplies `map`, `flatMap` and `withFilter` \(lazy version of `filter`\)}@}. <!--SR:!2026-10-26,282,330!fsrs,2029-10-22T00:00:00.000Z,1122,1122.43990816,1,2,9,0,0,2026-09-26T00:00:00.000Z!fsrs,2029-12-04T00:00:00.000Z,1157,1156.92457827,1,2,9,0,0,2026-10-04T00:00:00.000Z!fsrs,2030-01-02T00:00:00.000Z,1180,1179.83367202,1,2,9,0,0,2026-10-10T00:00:00.000Z!2026-10-11,270,330!2026-11-05,291,330-->

Indeed, any domain that {@{supplies these methods}@}—{@{booleans, strings, tuples, trees, even random number streams}@}—can participate in {@{a _for_ comprehension}@}. Further, such objects are called {@{_monads_}@} in {@{functional programming}@}, and they provide {@{a powerful abstraction for structuring programs}@}. <!--SR:!fsrs,2029-12-04T00:00:00.000Z,1157,1156.92457827,1,2,9,0,0,2026-10-04T00:00:00.000Z!2026-10-27,283,330!fsrs,2029-10-22T00:00:00.000Z,1122,1122.43990816,1,2,9,0,0,2026-09-26T00:00:00.000Z!2026-11-08,294,330!fsrs,2029-11-29T00:00:00.000Z,1153,1153.10014712,1,2,9,0,0,2026-10-03T00:00:00.000Z!2026-10-17,276,330-->

### generator

{@{A minimal abstraction}@} for producing {@{random values of some type `T`}@} is the following trait: <!--SR:!fsrs,2029-07-03T00:00:00.000Z,1034,1033.61384781,1,2,9,0,0,2026-09-03T00:00:00.000Z!fsrs,2028-01-31T00:00:00.000Z,506,506.03526322,5.00637887,2,9,0,0,2026-09-12T00:00:00.000Z-->

> [!example] __`Generator` definition__
>
> {@{A minimal abstraction}@} for producing {@{random values of some type `T`}@} is the following trait:
>
> ```Scala
> trait Generator[+T] { def generate(): T }
> ```
<!--SR:!2026-10-31,287,330!2026-10-25,281,330-->

{@{Concrete generators}@} can be created by {@{extending the trait `Generator`}@}.  For example, {@{an integer generator}@} that draws {@{from a `java.util.Random` instance}@} looks like <!--SR:!fsrs,2029-12-28T00:00:00.000Z,1176,1176.0199518,1,2,9,0,0,2026-10-09T00:00:00.000Z!2026-10-16,275,330!2026-10-24,280,330!2026-10-25,281,330-->

> [!example] __integer generator__
>
> For example, {@{an integer generator}@} that draws {@{from a `java.util.Random` instance}@} looks like
>
> ```Scala
> val integers = new Generator[Int]:
>   val rand = java.util.Random()
>   def generate() = rand.nextInt()
> ```
<!--SR:!2026-11-03,290,330!fsrs,2029-10-27T00:00:00.000Z,1126,1126.27892251,1,2,9,0,0,2026-09-27T00:00:00.000Z-->

Using {@{the same pattern}@} one can define {@{a boolean generator}@}: <!--SR:!fsrs,2029-06-28T00:00:00.000Z,1030,1029.72783972,1,2,9,0,0,2026-09-02T00:00:00.000Z!2026-11-03,290,330-->

> [!example] __boolean generator__
>
> Using {@{the same pattern}@} one can define {@{a boolean generator}@}:
>
> ```Scala
> val booleans = new Generator[Boolean]:
>   def generate() = integers.generate() > 0
> ```
<!--SR:!fsrs,2029-11-29T00:00:00.000Z,1153,1153.10014712,1,2,9,0,0,2026-10-03T00:00:00.000Z!2026-10-17,276,330-->

and {@{a pair generator}@} that produces {@{two independent random integers}@}: <!--SR:!fsrs,2029-10-13T00:00:00.000Z,1115,1114.75652523,1,2,9,0,0,2026-09-24T00:00:00.000Z!fsrs,2029-11-06T00:00:00.000Z,1134,1133.95119242,1,2,9,0,0,2026-09-29T00:00:00.000Z-->

> [!example] __pair generator__
>
> and {@{a pair generator}@} that produces {@{two independent random integers}@}:
>
> ```Scala
> val pairs = new Generator[(Int, Int)]:
>   def generate() = (integers.generate(), integers.generate())
> ```
<!--SR:!fsrs,2028-09-02T00:00:00.000Z,710,710.13394084,2.49272837,2,9,0,0,2026-09-23T00:00:00.000Z!fsrs,2029-07-07T00:00:00.000Z,1037,1037.49777357,1,2,9,0,0,2026-09-04T00:00:00.000Z-->

#### generator monad

Rather than writing {@{a new anonymous class}@} for {@{each derived generator}@}, {@{the `Generator` trait}@} can be {@{enriched with higher-order methods}@}. {@{An extension}@} that adds {@{`map`}@} is <!--SR:!2026-11-06,292,330!2026-10-17,276,330!2026-10-17,276,330!fsrs,2029-11-16T00:00:00.000Z,1142,1141.61620684,1,2,9,0,0,2026-10-01T00:00:00.000Z!fsrs,2029-06-18T00:00:00.000Z,1022,1021.94953015,1,2,9,0,0,2026-08-31T00:00:00.000Z!2026-10-26,282,330-->

> [!example] __`Generator.map`__
>
> {@{An extension}@} that adds {@{`map`}@} is
>
> ```Scala
> extension [T, S](g: Generator[T])
>   def map(f: T => S) = new Generator[S]:
>     def generate() = f(g.generate())
> ```
<!--SR:!fsrs,2029-12-28T00:00:00.000Z,1176,1176.0199518,1,2,9,0,0,2026-10-09T00:00:00.000Z!2026-10-21,277,330-->

and {@{a corresponding extension}@} to add {@{`flatMap`}@}: <!--SR:!2026-11-06,292,330!2026-10-14,273,330-->

> [!example] __`Generator.flatMap`__
>
> and {@{a corresponding extension}@} to add {@{`flatMap`}@}:
>
> ```Scala
> def flatMap(f: T => Generator[S]) = new Generator[S]:
>   def generate() = f(g.generate()).generate()
> ```
<!--SR:!2026-10-23,279,330!2026-10-29,285,330-->

With {@{these in place}@}, {@{the boolean generator}@} can be written {@{succinctly using `map`}@} as <!--SR:!fsrs,2029-10-22T00:00:00.000Z,1122,1122.43990816,1,2,9,0,0,2026-09-26T00:00:00.000Z!fsrs,2029-11-29T00:00:00.000Z,1153,1153.10014712,1,2,9,0,0,2026-10-03T00:00:00.000Z!2026-10-13,272,330-->

> [!example] __boolean generator using `map`__
>
> With {@{these in place}@}, {@{the boolean generator}@} can be {@{written succinctly}@} as
>
> ```Scala
> val booleans = integers.map(x => x > 0)
> ```
<!--SR:!fsrs,2029-12-23T00:00:00.000Z,1172,1172.20432607,1,2,9,0,0,2026-10-08T00:00:00.000Z!2026-10-24,280,330!2026-10-13,272,330-->

and {@{a generic pair generator}@} becomes, using {@{`flatMap`}@}: <!--SR:!fsrs,2029-06-23T00:00:00.000Z,1026,1025.83973773,1,2,9,0,0,2026-09-01T00:00:00.000Z!fsrs,2028-08-12T00:00:00.000Z,695,694.99996464,2.49272837,2,9,0,0,2026-09-17T00:00:00.000Z-->

> [!example] __pair generator using `flatMap`__
>
> and {@{a generic pair generator}@} becomes, using {@{`flatMap`}@}:
>
> ```Scala
> def pairs[T, U](t: Generator[T], u: Generator[U]) =
>   t.flatMap(x => u.map(y => (x, y)))
> ```
<!--SR:!2026-10-15,274,330!2026-10-13,272,330-->

The compiler rewrites {@{these _for_ expressions}@} in the same way {@{it does for collections}@}; {@{`for x <- g yield f(x)`}@} becomes {@{`g.map(f)`}@}, while {@{nested generators}@} translate into {@{successive calls to `flatMap`}@}. <!--SR:!fsrs,2029-10-27T00:00:00.000Z,1126,1126.27892251,1,2,9,0,0,2026-09-27T00:00:00.000Z!fsrs,2029-11-29T00:00:00.000Z,1153,1153.10014712,1,2,9,0,0,2026-10-03T00:00:00.000Z!2026-11-06,292,330!fsrs,2029-10-22T00:00:00.000Z,1122,1122.43990816,1,2,9,0,0,2026-09-26T00:00:00.000Z!2026-10-13,272,330!fsrs,2029-07-22T00:00:00.000Z,1049,1049.13725568,1,2,9,0,0,2026-09-07T00:00:00.000Z-->

#### generator monad recursion

{@{Generators}@} can be {@{combined recursively}@}. For example, {@{a generator of integer lists}@} is defined by first {@{choosing whether the list should be empty or non-empty}@} and then {@{constructing it accordingly}@}: <!--SR:!2026-11-04,290,330!2026-10-14,273,330!fsrs,2029-11-16T00:00:00.000Z,1142,1141.61620684,1,2,9,0,0,2026-10-01T00:00:00.000Z!2026-11-03,290,330!fsrs,2029-10-27T00:00:00.000Z,1126,1126.27892251,1,2,9,0,0,2026-09-27T00:00:00.000Z-->

> [!example] __integer list generator__
>
> For example, {@{a generator of integer lists}@} is defined by first {@{choosing whether the list should be empty or non-empty}@} and then {@{constructing it accordingly}@}
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
<!--SR:!fsrs,2029-12-04T00:00:00.000Z,1157,1156.92457827,1,2,9,0,0,2026-10-04T00:00:00.000Z!2026-10-29,285,330!fsrs,2029-06-28T00:00:00.000Z,1030,1029.72783972,1,2,9,0,0,2026-09-02T00:00:00.000Z-->

{@{A more sophisticated example}@} is {@{a random tree generator}@}. Defining {@{the tree shape}@} as {@{an `enum`}@}: <!--SR:!2026-10-17,276,330!2026-10-24,280,330!fsrs,2029-11-11T00:00:00.000Z,1138,1137.78464757,1,2,9,0,0,2026-09-30T00:00:00.000Z!2026-10-28,284,330-->

> [!example] __`Tree` definition__
>
> {@{A more sophisticated example}@} is {@{a random tree generator}@}. Defining {@{the tree shape}@} as {@{an `enum`}@}:
>
> ```Scala
> enum Tree:
>   case Inner(left: Tree, right: Tree)
>   case Leaf(x: Int)
> ```
<!--SR:!2026-10-16,275,330!2026-10-15,274,330!2026-10-26,282,330!fsrs,2029-08-11T00:00:00.000Z,1065,1064.62815785,1,2,9,0,0,2026-09-11T00:00:00.000Z-->

we can generate {@{leaves and inner nodes}@} by combining {@{existing generators}@}: <!--SR:!2026-10-27,283,330!2026-10-22,278,330-->

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
<!--SR:!fsrs,2028-08-23T00:00:00.000Z,703,702.57151752,2.49272837,2,9,0,0,2026-09-20T00:00:00.000Z!2026-10-25,281,330-->

#### generator monad usage

{@{Unit tests}@} traditionally {@{supply concrete inputs and check a post-condition}@}.  Using {@{generators}@}, one can instead {@{automatically produce many random test cases}@}: <!--SR:!fsrs,2029-12-04T00:00:00.000Z,1157,1156.92457827,1,2,9,0,0,2026-10-04T00:00:00.000Z!fsrs,2029-12-23T00:00:00.000Z,1172,1172.20432607,1,2,9,0,0,2026-10-08T00:00:00.000Z!fsrs,2029-12-28T00:00:00.000Z,1176,1176.0199518,1,2,9,0,0,2026-10-09T00:00:00.000Z!fsrs,2029-10-27T00:00:00.000Z,1126,1126.27892251,1,2,9,0,0,2026-09-27T00:00:00.000Z-->

> [!example] __unit test__
>
> {@{Unit tests}@} traditionally {@{supply concrete inputs and check a post-condition}@}.  Using {@{generators}@}, one can instead {@{automatically produce many random test cases}@}:
>
> ```Scala
> def test[T](g: Generator[T], numTimes: Int = 100)(test: T => Boolean): Unit =
>   for i <- 0 until numTimes do
>     val value = g.generate()
>     assert(test(value), s"test failed for $value")
>   println(s"passed $numTimes tests")
> ```
<!--SR:!2026-10-13,272,330!2026-11-01,288,330!fsrs,2029-12-04T00:00:00.000Z,1157,1156.92457827,1,2,9,0,0,2026-10-04T00:00:00.000Z!2026-10-31,287,330-->

{@{An example property}@} that {@{fails}@} is <!--SR:!fsrs,2029-10-27T00:00:00.000Z,1126,1126.27892251,1,2,9,0,0,2026-09-27T00:00:00.000Z!2026-10-17,276,330-->

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
> which should be corrected {@{to `>=` instead of `>`}@}.  This illustrates how {@{generators can reveal subtle invariants}@}. <!--SR:!fsrs,2028-02-03T00:00:00.000Z,508,507.95545468,5.00637887,2,9,0,0,2026-09-13T00:00:00.000Z!2026-10-14,273,330!fsrs,2029-10-22T00:00:00.000Z,1122,1122.43990816,1,2,9,0,0,2026-09-26T00:00:00.000Z!2026-11-04,290,330-->

The same idea is {@{used in the _ScalaCheck_ library}@}.  {@{A property expressed as a lambda}@} can be automatically {@{checked against many random inputs}@}: <!--SR:!2026-10-12,271,330!2026-10-13,272,330!fsrs,2029-07-12T00:00:00.000Z,1041,1041.37962848,1,2,9,0,0,2026-09-05T00:00:00.000Z-->

> [!example] ___ScalaCheck___
>
> The same idea is {@{used in the _ScalaCheck_ library}@}.  {@{A property expressed as a lambda}@} can be automatically {@{checked against many random inputs}@}:
>
> ```Scala
> forAll { (l1: List[Int], l2: List[Int]) =>
>   (l1 ++ l2).size == l1.size + l2.size
> }
> ```
<!--SR:!fsrs,2029-06-23T00:00:00.000Z,1026,1025.83973773,1,2,9,0,0,2026-09-01T00:00:00.000Z!2026-11-02,289,330!2026-10-24,280,330-->

ScalaCheck integrates {@{with ScalaTest or can run stand-alone}@}, providing a systematic way to {@{validate program behaviour without hand-crafted test data}@}. <!--SR:!2026-10-14,273,330!fsrs,2028-07-20T00:00:00.000Z,745,744.93144381,1,2,8,0,0,2026-07-06T00:00:00.000Z-->

## definition

{@{A monad}@} is defined for {@{a parametric type constructor `M[_]`}@}. {@{Two fundamental operations}@} must be supplied: <!--SR:!2026-11-07,293,330!2026-10-29,285,330!fsrs,2029-12-23T00:00:00.000Z,1172,1172.20432607,1,2,9,0,0,2026-10-08T00:00:00.000Z-->

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
<!--SR:!2026-11-02,289,330!2026-11-07,293,330!fsrs,2029-07-27T00:00:00.000Z,1053,1053.01305103,1,2,9,0,0,2026-09-08T00:00:00.000Z-->

{@{`flatMap`}@} chains {@{computations that may produce values wrapped in the monad}@}, while {@{`unit`}@} injects {@{a plain value into the monadic context}@}. Additionally, these operations must {@{respect the monad laws}@}. <!--SR:!2026-10-15,274,330!2026-10-17,276,330!fsrs,2029-10-13T00:00:00.000Z,1115,1114.75652523,1,2,9,0,0,2026-09-24T00:00:00.000Z!2026-10-28,284,330!2026-11-01,288,330-->

In Scala, {@{`flatMap`}@} is typically {@{implemented as a method of the type itself or an extension method}@}; {@{`unit`}@} can be provided as {@{a constructor of the type}@}. <!--SR:!2026-10-24,280,330!2026-10-29,285,330!fsrs,2029-10-22T00:00:00.000Z,1122,1122.43990816,1,2,9,0,0,2026-09-26T00:00:00.000Z!2026-10-29,285,330-->

### monad laws

For a type to be {@{considered a true monad}@}, {@{three algebraic laws}@} must hold: \(annotation: 3 items: {@{associativity, left identity, right identity}@}\) <!--SR:!2026-10-25,281,330!fsrs,2029-11-16T00:00:00.000Z,1142,1141.61620684,1,2,9,0,0,2026-10-01T00:00:00.000Z!fsrs,2029-12-04T00:00:00.000Z,1157,1156.92457827,1,2,9,0,0,2026-10-04T00:00:00.000Z-->

- __Associativity__ ::@:: `m.flatMap(f).flatMap(g) == m.flatMap(x => f(x).flatMap(g))` <!--SR:!2026-11-08,294,330!2026-11-06,292,330-->
- __Left Identity (Left Unit Law)__ ::@:: `unit(x).flatMap(f) == f(x)` <!--SR:!2026-11-07,293,330!fsrs,2029-10-22T00:00:00.000Z,1122,1122.43990816,1,2,9,0,0,2026-09-26T00:00:00.000Z-->
- __Right Identity (Right Unit Law)__ ::@:: `m.flatMap(unit) == m` <!--SR:!fsrs,2030-01-02T00:00:00.000Z,1180,1179.83367202,1,2,9,0,0,2026-10-10T00:00:00.000Z!fsrs,2029-11-11T00:00:00.000Z,1138,1137.78464757,1,2,9,0,0,2026-09-30T00:00:00.000Z-->

{@{These laws}@} ensure that {@{monadic chaining behaves predictably}@}, enabling {@{reasoning about code and allowing optimizations}@}. <!--SR:!fsrs,2029-11-11T00:00:00.000Z,1138,1137.78464757,1,2,9,0,0,2026-09-30T00:00:00.000Z!2026-10-16,275,330!2026-11-04,290,330-->

### `map`

Although monads only {@{require `flatMap` and `unit`}@}, {@{a `map` operation}@} can always be {@{defined in terms of them}@}: <!--SR:!fsrs,2029-10-27T00:00:00.000Z,1126,1126.27892251,1,2,9,0,0,2026-09-27T00:00:00.000Z!fsrs,2029-12-23T00:00:00.000Z,1172,1172.20432607,1,2,9,0,0,2026-10-08T00:00:00.000Z!fsrs,2029-11-29T00:00:00.000Z,1153,1153.10014712,1,2,9,0,0,2026-10-03T00:00:00.000Z-->

> [!example] __monad `map`__
>
> Although monads only {@{require `flatMap` and `unit`}@}, {@{a `map` operation}@} can always be {@{defined in terms of them}@}:
>
> ```Scala
> m.map(f) == m.flatMap(x => unit(f(x)))
> m.map(f) == m.flatMap(f andThen unit)
> ```
<!--SR:!2026-11-05,291,330!2026-10-12,271,330!2026-10-25,281,330-->

Because {@{every monad supports this construction}@}, it is often convenient to {@{expose a dedicated `map` method for clarity}@}. <!--SR:!2026-10-31,287,330!fsrs,2029-06-13T00:00:00.000Z,1018,1018.05728725,1,2,9,0,0,2026-08-30T00:00:00.000Z-->

## examples

{@{Typical examples}@} include: \(annotation: 4 items: {@{`List`, `Set`, `Option`, `Generator`}@}\) <!--SR:!2026-11-01,288,330!2026-10-31,287,330-->

- `List`: ::@:: `unit(x) = List(x)` <!--SR:!2026-11-08,294,330!fsrs,2029-10-18T00:00:00.000Z,1119,1118.59914239,1,2,9,0,0,2026-09-25T00:00:00.000Z-->
- `Set`:  ::@:: `unit(x) = Set(x)` <!--SR:!2026-10-16,275,330!2026-10-15,274,330-->
- `Option`: ::@:: `unit(x) = Some(x)` <!--SR:!2026-10-29,285,330!fsrs,2029-11-16T00:00:00.000Z,1142,1141.61620684,1,2,9,0,0,2026-10-01T00:00:00.000Z-->
- `Generator`: ::@:: `unit(x) = single(x)` <!--SR:!2026-10-16,275,330!2026-10-25,281,330-->

{@{All of these types}@} provide {@{a natural implementation of `flatMap`}@} that preserves {@{the structure of the container}@}. <!--SR:!fsrs,2029-11-11T00:00:00.000Z,1138,1137.78464757,1,2,9,0,0,2026-09-30T00:00:00.000Z!2026-10-25,281,330!fsrs,2029-12-28T00:00:00.000Z,1176,1176.0199518,1,2,9,0,0,2026-10-09T00:00:00.000Z-->

## significance for `for`-expressions

{@{Scala's syntactic sugar}@} for {@{monadic composition}@} is {@{the `for`-expression}@}. <!--SR:!fsrs,2029-11-01T00:00:00.000Z,1130,1130.11601442,1,2,9,0,0,2026-09-28T00:00:00.000Z!2026-10-15,274,330!2026-10-29,285,330-->

{@{Associativity}@} guarantee that {@{nested `for`-expressions}@} can {@{always be collapsed into a single `for`-expression}@}: <!--SR:!2026-10-13,272,330!2026-10-17,276,330!2027-04-20,419,390-->

> [!example] __flatten `for`-expressions__
>
> {@{Associativity}@} guarantees that {@{nested `for`-expressions}@} can {@{always be flattened into a single `for`-expression}@}:
>
> ```Scala
> for {
>   y <- for { x <- m; y <- f(x) } yield y
>   z <- g(y)
> } yield z
> == for { x <- m; y <- f(x); z <- g(y) } yield z
> ```
<!--SR:!2026-10-29,285,330!fsrs,2029-11-06T00:00:00.000Z,1134,1133.95119242,1,2,9,0,0,2026-09-29T00:00:00.000Z!2027-04-15,415,390-->

{@{The right-unit law}@} implies that {@{a single generator without further bindings}@} is {@{equivalent to the monad itself}@} ({@{`for { x <- m } yield x == m`}@}). {@{The left-unit law ensures}@} that {@{a binding from `unit(x)` followed by another function}@} simply yields {@{that function applied to `x`}@} ({@{`for { y <- unit(x); r <- f(y) } yield r == f(x)`}@}). <!--SR:!fsrs,2029-12-28T00:00:00.000Z,1176,1176.0199518,1,2,9,0,0,2026-10-09T00:00:00.000Z!2026-10-24,280,330!2026-11-05,291,330!2026-10-29,285,330!fsrs,2029-11-01T00:00:00.000Z,1130,1130.11601442,1,2,9,0,0,2026-09-28T00:00:00.000Z!2026-10-26,282,330!2026-11-01,288,330!fsrs,2028-08-26T00:00:00.000Z,705,705.09333259,2.49272837,2,9,0,0,2026-09-21T00:00:00.000Z-->

## `Option`

For instance, consider {@{Scala's `Option`}@}. {@{Its `flatMap`}@} is defined by {@{pattern matching}@}: <!--SR:!fsrs,2029-12-04T00:00:00.000Z,1157,1156.92457827,1,2,9,0,0,2026-10-04T00:00:00.000Z!2026-10-14,273,330!2026-10-16,275,330-->

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
<!--SR:!2026-11-01,288,330!2026-10-23,279,330!2026-10-11,270,330-->

Using {@{simple algebraic reasoning}@}, one can verify that {@{all three laws hold for `Option`}@}. {@{The left-unit law}@} is immediate because {@{`Some(x).flatMap(f)` evaluates to `f(x)`}@}, and {@{the right-unit law}@} follows from the fact that {@{mapping a value with `unit` (i.e., `Some`) leaves it unchanged}@}. {@{Associativity}@} can be shown by unfolding {@{both sides and observing that they reduce to identical pattern matches}@}. <!--SR:!2026-11-08,294,330!2026-10-20,276,330!2026-10-25,281,330!fsrs,2029-08-06T00:00:00.000Z,1061,1060.7584061,1,2,9,0,0,2026-09-10T00:00:00.000Z!2026-11-01,288,330!2026-11-06,292,330!fsrs,2029-12-23T00:00:00.000Z,1172,1172.20432607,1,2,9,0,0,2026-10-08T00:00:00.000Z!fsrs,2028-08-19T00:00:00.000Z,700,700.04868809,2.49272837,2,9,0,0,2026-09-19T00:00:00.000Z-->

## `Try`

While {@{exceptions}@} are {@{inexpensive in Scala}@}, they have {@{drawbacks}@}: \(annotation: 2 items: {@{no effect on function type, cross-evaluation context}@}\) <!--SR:!fsrs,2029-11-16T00:00:00.000Z,1142,1141.61620684,1,2,9,0,0,2026-10-01T00:00:00.000Z!2026-10-11,270,330!2026-10-15,274,330!fsrs,2028-08-30T00:00:00.000Z,708,707.6141386,2.49272837,2,9,0,0,2026-09-22T00:00:00.000Z-->

- no effect on function type ::@:: The types of functions that may throw are not reflected in the signature (unlike Java's `throws` clause). <!--SR:!2026-11-03,290,330!fsrs,2030-01-02T00:00:00.000Z,1180,1179.83367202,1,2,9,0,0,2026-10-10T00:00:00.000Z-->
- cross-evaluation context ::@:: Exceptions can only propagate within the current evaluation context \(e.g. current thread\). They do not propagate naturally across threads or asynchronous boundaries. <!--SR:!fsrs,2029-11-29T00:00:00.000Z,1153,1153.10014712,1,2,9,0,0,2026-10-03T00:00:00.000Z!2026-10-26,282,330-->

Because of {@{these issues}@}, it is sometimes preferable to treat {@{failures as ordinary values}@}. {@{This idea}@} is captured by {@{the `scala.util.Try` _monad_ type}@}. <!--SR:!2026-10-31,287,330!2026-10-17,276,330!2026-10-25,281,330!2026-10-15,274,330-->

{@{`scala.util.Try`}@} behaves like{@{ an `Option`}@}, but distinguishes {@{between success and failure}@}: <!--SR:!2026-10-30,286,330!2026-10-28,284,330!2026-10-17,276,330-->

> [!example] __`Try` definition__
>
> {@{`scala.util.Try`}@} behaves like{@{ an `Option`}@}, but distinguishes {@{between success and failure}@}:
>
> ```Scala
> abstract class Try[+T]
> case class Success[+T](x: T) extends Try[T]
> case class Failure(ex: Exception) extends Try[Nothing]
> ```
<!--SR:!2026-10-24,280,330!2026-10-14,273,330!2026-10-12,271,330-->

{@{A convenient factory for `Try`}@} wraps {@{arbitrary computations}@}: <!--SR:!2026-10-17,276,330!fsrs,2029-11-29T00:00:00.000Z,1153,1153.10014712,1,2,9,0,0,2026-10-03T00:00:00.000Z-->

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
<!--SR:!2026-11-05,291,330!fsrs,2029-10-27T00:00:00.000Z,1126,1126.27892251,1,2,9,0,0,2026-09-27T00:00:00.000Z-->

{@{`Try`}@} supports {@{monadic composition}@} via {@{`flatMap` and `map`}@}: <!--SR:!fsrs,2029-10-27T00:00:00.000Z,1126,1126.27892251,1,2,9,0,0,2026-09-27T00:00:00.000Z!fsrs,2030-01-02T00:00:00.000Z,1180,1179.83367202,1,2,9,0,0,2026-10-10T00:00:00.000Z!2026-10-27,283,330-->

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
<!--SR:!fsrs,2029-11-01T00:00:00.000Z,1130,1130.11601442,1,2,9,0,0,2026-09-28T00:00:00.000Z!fsrs,2029-12-23T00:00:00.000Z,1172,1172.20432607,1,2,9,0,0,2026-10-08T00:00:00.000Z!2026-11-08,294,330-->

Thus {@{`t.map(f)`}@} equals {@{`t.flatMap(x => Try(f(x)))`}@}, mirroring {@{the general monadic definition of `map`}@}. <!--SR:!2026-11-02,289,330!2026-10-14,273,330!2026-11-02,289,330-->

One might ask whether {@{`Try` satisfies the monad laws with `unit = Try.apply`}@}. {@{The left-unit law}@} fails: {@{`Try(expr).flatMap(f)`}@} will {@{never throw a non-fatal exception}@}, whereas {@{`f(expr)` may}@}. Consequently, `Try` trades {@{the left identity law}@} for {@{a useful property}@}—{@{any composition of `Try`, `map`, and `flatMap`}@} guarantees that {@{no non-fatal exception propagates outward}@} ({@{the "bullet-proof" principle}@}\). <!--SR:!2026-10-17,276,330!2026-10-25,281,330!2026-10-29,285,330!2026-10-17,276,330!2026-10-30,286,330!2026-10-24,280,330!fsrs,2029-07-17T00:00:00.000Z,1045,1045.2595081,1,2,9,0,0,2026-09-06T00:00:00.000Z!2026-10-24,280,330!2026-11-03,290,330!2026-11-07,293,330-->

In {@{general practice}@}, {@{monad-like type \(which are not true monads\)}@} aims to capture {@{some computation _effect_}@} and treating it as {@{_data_ and hence part of the _type_}@}. When {@{this effect is a _side effect_ \(e.g. throwing exceptions\)}@}, then {@{the left identity law may not hold}@} as {@{the side effect is captured and represented by monad-like type data instead}@}. <!--SR:!2027-01-09,345,350!2026-12-07,319,350!2027-01-03,339,350!2026-12-11,321,350!2026-12-18,328,350!2027-01-14,350,350!fsrs,2029-10-17T00:00:00.000Z,1107,1107.06552019,1,2,9,0,0,2026-10-06T00:00:00.000Z-->
