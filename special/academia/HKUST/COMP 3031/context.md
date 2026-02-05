---
aliases:
  - COMP 3031 Scala context
  - COMP 3031 Scala contexts
  - COMP3031 Scala context
  - COMP3031 Scala contexts
  - HKUST COMP 3031 Scala context
  - HKUST COMP 3031 Scala contexts
  - HKUST COMP3031 Scala context
  - HKUST COMP3031 Scala contexts
  - Scala context
  - Scala contexts
tags:
  - flashcard/active/special/academia/HKUST/COMP_3031/context
  - language/in/English
---

# Scala context

- HKUST COMP 3031

Normally in Scala, {@{values \(terms\) and types}@} infer {@{types}@}, e.g. {@{inferring type parameters}@}. Sometimes you want {@{types to infer values}@} instead, called {@{_type-directed programming_}@}. This is helpful for abstracting {@{context based on types}@}. <!--SR:!2026-02-06,70,329!2026-11-19,289,349!2026-11-24,294,349!2026-02-13,76,329!2026-02-13,76,329!2026-02-07,71,329-->

## motivation

We want to write {@{code that is _modular_}@} by {@{abstracting over the "context" in which it will run}@}. {@{Context}@} can be {@{the current configuration, security level}@}, or even {@{a user on whose behalf an operation executes}@}.  In practice this means making {@{functions and classes independent of global state \(dependent on "context"\)}@} so they can be {@{reused safely across modules}@}. There are several {@{common approaches}@}: \(annotation: 5 items: {@{globals, mutable globals, monkey patch, dependency injection, functional context}@}\) <!--SR:!2026-02-13,76,329!2026-12-16,314,349!2026-02-06,70,329!2026-11-23,293,349!2026-02-13,76,329!2026-02-13,76,329!2026-10-02,251,330!2026-09-22,241,330!2026-11-20,294,349-->

- globals ::@:: Simple to use. Rigid, hard to change per module. <!--SR:!2026-12-06,306,349!2026-12-19,317,349-->
- mutable globals ::@:: Flexible but unsafe. Risk of interference \(e.g. race conditions\). <!--SR:!2026-12-20,318,349!2026-11-20,290,349-->
- monkey patch ::@:: Powerful and dynamic. Can break code and debugging. <!--SR:!2026-02-13,76,329!2026-11-25,295,349-->
- dependency injection ::@:: Encapsulates configuration. Relies on bytecode rewriting and opaque. Frameworks include Guice, Spring, etc. <!--SR:!2026-11-23,293,349!2026-11-19,293,349-->
- functional context ::@:: Normally, values and types infer types but not values, e.g. inferring type parameters. With `using`, types are used to infer values. Those values provide "context". <!--SR:!2026-02-13,76,329!2026-11-12,282,349-->

### higher-order functions

When {@{a method}@} needs to {@{operate over arbitrary types}@} – for example, {@{a generic `sort`}@} – {@{the natural solution}@} is to {@{type parameterise it}@}: <!--SR:!2026-02-13,76,329!2026-02-13,76,329!2026-11-26,296,349!2026-12-07,307,349!2026-12-04,304,349-->

> [!example] __parameterized sort__
>
> When {@{a method}@} needs to {@{operate over arbitrary types}@} – for example, {@{a generic `sort`}@} – {@{the natural solution}@} is to {@{type parameterise it}@}:
>
> ```Scala
> def sort[T](xs: List[T]): List[T] = ???
> ```
<!--SR:!2026-02-13,76,329!2026-12-05,305,349!2026-02-07,71,329!2026-11-25,295,349!2026-12-01,301,349-->

However, {@{sorting}@} requires {@{an ordering relation `<`}@}, which {@{does not exist for all types}@}.  {@{The resolution}@} is to {@{_parameterise with an ordering_ rather than just a type}@}. <!--SR:!2026-10-01,250,330!2026-02-06,70,329!2026-02-06,70,329!2026-12-08,308,349!2026-02-07,71,329-->

> [!example] __parameterized sort with ordering__
>
> However, {@{sorting}@} requires {@{an ordering relation `<`}@}, which {@{does not exist for all types}@}.  {@{The resolution}@} is to {@{_parameterise with an ordering_ rather than just a type}@}.
>
> ```Scala
> def sort[T](xs: List[T])(lessThan: (T,T) => Boolean): List[T] = ...
> ```
>
> {@{Example usage}@}:
>
> ```Scala
> val ints    = List(-5, 6, 3, 2, 7)
> val strings = List("apple", "pear", "orange", "pineapple")
> sort(ints)((x, y) => x < y)
> sort(strings)((s1, s2) => s1.compareTo(s2) < 0)
> ```
<!--SR:!2026-11-22,296,349!2026-11-11,281,349!2026-02-13,76,329!2026-11-17,287,349!2026-02-06,70,329!2026-11-21,291,349-->

Scala provides {@{the `scala.math.Ordering` trait}@} to {@{represent the sorting function}@}: <!--SR:!2026-12-22,320,349!2026-02-13,76,329-->

> [!example] __parameterized sort with ordering using `Ordering`__
>
> Scala provides {@{the `scala.math.Ordering` trait}@} to {@{represent the sorting function}@}:
>
> ```Scala
> import scala.math.Ordering
> def sort[T](xs: List[T])(ord: Ordering[T]): List[T] = {
>   // use ord.compare(x, y)
> }
> ```
>
> {@{Calling it}@} becomes {@{simpler}@}:
>
> ```Scala
> val ints    = List(-5, 6, 3, 2, 7)
> val strings = List("apple", "pear", "orange", "pineapple")
> sort(ints)(Ordering.Int)
> sort(strings)(Ordering.String)
> ```
<!--SR:!2026-12-22,320,349!2026-11-16,290,349!2026-02-13,76,329!2026-11-17,287,349-->

## `using`

To {@{reduce boilerplate}@} {@{the `ord` argument}@} can be declared {@{_implicit_ via a `using` clause}@}: <!--SR:!2026-12-05,305,349!2026-11-12,286,349!2026-12-16,314,349-->

> [!example] __parameterized sort with implicit ordering__
>
> To {@{reduce boilerplate}@} {@{the `ord` argument}@} can be declared {@{_implicit_ via a `using` clause}@}:
>
> ```Scala
> def sort[T](xs: List[T])(using ord: Ordering[T]): List[T] = ...
> ```
>
> Now {@{callers}@} need not {@{supply it explicitly \(though it could if it chooses to\)}@}; {@{the compiler}@} searches for {@{an implicit `Ordering[T]` in scope}@} and {@{supplies it automatically}@}. <!--SR:!2026-02-07,71,329!2026-02-13,76,329!2026-12-15,313,349!2026-02-16,78,348!2026-02-16,78,348!2026-02-17,79,348!2026-02-20,82,348!2026-02-19,81,348-->

Now {@{callers}@} need not {@{supply it explicitly \(though it could if it chooses to\)}@}; {@{the compiler}@} searches for {@{an implicit `Ordering[T]` in scope}@} and {@{supplies it automatically}@}. {@{Calling it}@} becomes {@{simpler}@}: <!--SR:!2026-09-26,245,330!2026-09-29,248,330!2026-02-13,76,329!2026-11-09,283,349!2026-12-20,318,349!2026-02-13,76,329!2026-11-21,292,349-->

> [!example] __using parameterized sort with implicit ordering__
>
> Now {@{callers}@} need not {@{supply it explicitly \(though it could if it chooses to\)}@}; {@{the compiler}@} searches for {@{an implicit `Ordering[T]` in scope}@} and {@{supplies it automatically}@}. {@{Calling it}@} becomes {@{simpler}@}:
>
> ```Scala
> val ints    = List(-5, 6, 3, 2, 7)
> val strings = List("apple", "pear", "orange", "pineapple")
> sort(ints)     // `sort(ints)(using Ordering.Int)`
> sort(strings)  // `sort(strings)(using Ordering.String)`
> ```
>
> The compiler also infers {@{the type argument `T` from the argument list}@}. If {@{a single obvious value exists for a type}@}, the compiler may even infer {@{that _term_ itself (e.g., `Ordering.Int`)}@}. <!--SR:!2026-02-18,80,347!2026-02-17,79,347!2026-02-20,82,347!2026-12-18,316,349!2026-02-06,70,329!2026-02-06,70,329!2026-12-21,319,349!2026-12-07,307,349!2026-11-17,291,349!2026-09-20,239,330-->

The compiler also infers {@{the type argument `T` from the argument list}@}. If {@{a single obvious value exists for a type}@}, the compiler may even infer {@{that _term_ itself (e.g., `Ordering.Int`)}@}, as in the above example. <!--SR:!2026-02-18,80,348!2026-02-18,80,348!2026-02-19,81,348-->

### `using` syntax

In Scala, {@{an implicit parameter}@} is introduced through {@{a `using` clause in the method signature}@}: <!--SR:!2026-11-27,297,349!2026-11-13,283,349-->

> [!example] __`using` in method__
>
> In Scala, {@{an implicit parameter}@} is introduced through {@{a `using` clause in the method signature}@}:
>
> ```Scala
> def sort[T](xs: List[T])(using ord: Ordering[T]): List[T] = …
> ```
<!--SR:!2026-11-29,299,349!2026-11-20,290,349-->

When calling {@{such a method}@}, you may {@{supply the argument explicitly}@} via {@{another `using` clause}@}: <!--SR:!2026-02-13,76,329!2026-12-08,308,349!2026-12-10,310,349-->

> [!example] __`using` in method call__
>
> When calling {@{such a method}@}, you may {@{supply the argument explicitly}@} via {@{another `using` clause}@}:
>
> ```Scala
> sort(strings)(using Ordering.String)
> sort(strings)  // compiler finds `Ordering.String`
> ```
>
> However, {@{explicit passing}@} is {@{usually unnecessary}@}. <!--SR:!2026-02-17,79,348!2026-02-08,72,348!2026-02-22,84,349!2026-02-19,81,348!2026-02-16,78,348-->

However, {@{explicit passing}@} is {@{usually unnecessary}@}. If the caller {@{omits the `using` argument}@}, the compiler {@{automatically searches for an appropriate instance of `Ordering[T]`}@} and {@{supplies it implicitly}@}, as in the second line above. <!--SR:!2026-02-14,77,348!2026-02-16,78,348!2026-02-16,78,348!2026-02-08,72,348!2026-02-21,83,348-->

{@{The syntax for `using` clauses}@} is {@{flexible}@}. {@{A single clause}@} may contain {@{multiple parameters}@}: <!--SR:!2026-10-02,251,330!2026-12-19,317,349!2026-12-03,303,349!2026-02-13,76,329-->

> [!example] __`using` multiple parameters__
>
> {@{The syntax for `using` clauses}@} is {@{flexible}@}. {@{A single clause}@} may contain {@{multiple parameters}@}:
>
> ```Scala
> def f(x: Int)(using a: A, b: B) = ...
> f(10)(using a, b)
> ```
<!--SR:!2026-02-06,70,329!2026-09-30,249,330!2026-11-21,295,349!2026-11-26,296,349-->

Alternatively, {@{separate `using` clauses}@} can be {@{chained}@}. {@{`using` clauses}@} can also be {@{interleaved with ordinary parameter lists}@}, allowing {@{a mix of implicit and explicit arguments}@}: <!--SR:!2026-02-07,71,329!2026-11-20,294,349!2026-11-28,298,349!2026-12-10,310,349!2026-02-13,76,329-->

> [!example] __`using` in multiple parameter lists__
>
> Alternatively, {@{separate `using` clauses}@} can be {@{chained}@}. {@{`using` clauses}@} can also be {@{interleaved with ordinary parameter lists}@}, allowing {@{a mix of implicit and explicit arguments}@}:
>
> ```Scala
> def f(x: Int)(using a: A)(using b: B) = ...
> def g(x: Int)(using a: A)(y: Boolean)(using b: B) = ...
>
> f(10)(using a)(using b)
> f(10)(using a)(true)(using b)
> ```
<!--SR:!2026-10-03,252,330!2026-11-16,286,349!2026-02-13,76,329!2026-02-06,70,329!2026-12-20,318,349-->

{@{Anonymous `using` clauses}@} let a method declare {@{an implicit parameter without naming it}@}; the compiler will still {@{supply and forward that instance to other methods automatically}@}. For example, <!--SR:!2026-02-13,76,329!2026-11-21,291,349!2026-11-23,297,349-->

> [!example] __anonymous `using` clauses__
>
> {@{Anonymous `using` clauses}@} let a method declare {@{an implicit parameter without naming it}@}; the compiler will still {@{supply and forward that instance to other methods automatically}@}. For example,
>
> ```Scala
> def sort[T](xs: List[T])(using Ordering[T]): List[T] =
>   ...  // omitted
>   merge(sort(fst), sort(snd))
>   ...  // omitted
> ```
>
> can be written with {@{an unnamed `Ordering[T]`}@}, yet internally {@{each `merge` and `sort` implicitly receives the same ordering}@}. <!--SR:!2026-09-19,238,330!2026-02-07,71,329!2026-02-13,76,329!2026-02-13,76,329!2026-09-14,233,330-->

{@{Writing `(using Ordering[T])` inside a parameter list}@} is equivalent to explicitly {@{passing a named `ord` through every call that needs an `Ordering` implicitly}@}, but keeps the body of `sort` {@{free from boilerplate}@} and shows that {@{the implicit context can propagate transparently}@} even when the method itself {@{never directly references the parameter}@}. <!--SR:!2026-10-02,251,330!2026-12-21,319,349!2026-10-05,254,330!2026-12-09,309,349!2026-05-01,117,391-->

### context bound

{@{A shorthand}@} for declaring {@{an implicit parameter}@} is {@{the _context bound_}@}, which {@{expands to a `using` clause under the hood}@}: <!--SR:!2026-02-07,71,329!2026-12-04,304,349!2026-12-08,308,349!2026-11-28,298,349-->

> [!example] __context bound__
>
> {@{A shorthand}@} for declaring {@{an implicit parameter}@} is {@{the _context bound_}@}, which {@{expands to a `using` clause under the hood}@}:
>
> ```Scala
> def printSorted[T: Ordering](xs: List[T]) =
>   println(sort(xs))
> ```
>
> Intuitively, this may be interpreted as {@{`T` "satisfying" the trait `Ordering`}@}, i.e. having {@{a defined ordering}@}. <!--SR:!2026-02-17,79,348!2026-02-23,85,349!2026-02-19,81,347!2026-02-16,78,347!2026-02-13,76,329!2026-02-13,76,329-->

Intuitively, {@{a context bound `T : U`}@} may be interpreted as {@{the type parameter `T` "satisfying" the "trait" `U`}@}. <!--SR:!2026-02-17,79,348!2026-02-22,84,348-->

More generally, {@{any definition `def f[T : {U1, ..., Un}](ps) : R`}@} \({@{_deprecated_ syntax}@}: {@{`def f[T : U1 : ... : Un](ps) : R`}@}\) is expanded to {@{`def f[T](ps)(using U1[T], ..., Un[T]) : R`}@}. {@{This transformation}@} makes {@{context bounds a convenient shorthand}@} for {@{implicit parameters without altering the generated code}@}. <!--SR:!2026-11-24,294,349!2026-10-04,253,330!2026-02-13,76,329!2026-11-18,288,349!2026-12-01,301,349!2026-02-18,80,348!2026-02-14,77,348-->

## `given`

Scala 3 introduces {@{_`given` instances_}@} – {@{values}@} that can be {@{automatically supplied for implicit parameters}@}. The following {@{creates a new instance of `Ordering[Int]`}@}: <!--SR:!2026-02-13,76,329!2026-02-06,70,329!2026-02-13,76,329!2026-05-29,115,391-->

> [!example] __`Ordering.Int`__
>
> Scala 3 introduces {@{_`given` instances_}@} – {@{values}@} that can be {@{automatically supplied for implicit parameters}@}. The following {@{creates a new instance of `Ordering[Int]`}@}:
>
> ```Scala
> object Ordering:
>   given Int: Ordering[Int] with
>     def compare(x: Int, y: Int): Int =
>       if (x < y) -1 else if (x > y) 1 else 0
> ```
<!--SR:!2026-02-13,76,329!2026-12-18,316,349!2026-11-26,296,349!2026-06-04,121,391-->

{@{Anonymous instances}@} can be {@{declared without a name}@}; the compiler will {@{create a new instance and generate a name}@}: <!--SR:!2026-12-05,305,349!2026-12-10,310,349!2026-02-13,76,329-->

> [!example] __`Ordering[Double]`__
>
> {@{Anonymous instances}@} can be {@{declared without a name}@}; the compiler will {@{create a new instance and generate a name}@}:
>
> ```Scala
> given Ordering[Double] with
>   def compare(x: Double, y: Double): Int = ...
> ```
<!--SR:!2026-05-30,116,391!2026-05-30,116,391!2026-06-10,127,391-->

To {@{assign an already existing instance to `given`}@}, use {@{the assignment operator `=`}@}: <!--SR:!2026-06-02,119,391!2026-05-27,117,391-->

> [!example] __assigning to `given`__
>
> To {@{assign an already existing instance to `given`}@}, use {@{the assignment operator `=`}@}:
>
> ```Scala
> given Type = instance        // unnamed
> given name: Type = instance  // named: `name`
> ```
<!--SR:!2026-06-01,118,391!2026-06-09,126,391-->

### `summon`
<!--SR:!2026-01-31,65,329!2026-02-05,69,329!2026-01-23,58,310-->

To refer to {@{an instance directly without using `using`}@}, you may {@{use `summon`}@}: <!--SR:!2026-09-18,237,330!2026-10-06,255,330-->

> [!example] __`summon`__
>
> To refer to {@{an instance directly without using `using`}@}, you may {@{use `summon`}@}:
>
> ```Scala
> val intOrd = summon[Ordering[Int]]      // expands to Ordering.Int
> val dblOrd = summon[Ordering[Double]]   // anonymous name
> ```
<!--SR:!2026-02-13,76,329!2026-11-07,281,349-->

{@{`summon`}@} simply uses {@{`using` in its implementation}@}; it is {@{defined as}@}: <!--SR:!2026-02-13,76,329!2026-12-04,304,349!2026-02-13,76,329-->

> [!example] __`summon` implementation__
>
> {@{`summon`}@} simply uses {@{`using` in its implementation}@}; it is {@{defined as an identity function on the implicit argument}@}:
>
> ```Scala
> def summon[T](using x: T): T = x
> ```
<!--SR:!2026-02-13,76,329!2026-11-24,294,349!2026-11-18,288,349-->

### importing `given`s

There are {@{three forms of import}@} to {@{import `given`s}@}: \(annotation: 3 items: {@{by name, by type, by wildcard}@}\) <!--SR:!2026-11-13,283,349!2026-02-06,70,329!2026-02-13,76,329-->

- by name ::@:: `import scala.math.Ordering.Int` <!--SR:!2026-10-02,251,330!2026-02-13,76,329-->
- by type ::@:: using the `given` keyword, e.g., `import scala.math.Ordering.{given Ordering[Int]}`, `import scala.math.Ordering.{given Ordering[?]}` <!--SR:!2026-11-18,288,349!2026-12-08,308,349-->
- by wildcard ::@:: via a blanket wildcard, e.g. `import scala.math.given` <!--SR:!2026-11-30,300,349!2026-02-13,76,329-->

Since {@{the actual names of `given` instances}@} are {@{irrelevant to resolution}@}, {@{importing by type}@} is {@{preferred}@} because it explicitly {@{states which implicit instance you intend to use}@}. <!--SR:!2026-12-22,320,349!2026-02-07,71,329!2026-02-07,71,329!2026-11-29,299,349!2026-11-19,289,349-->

### conditional `given`

{@{A `given` instance}@} may itself {@{require an implicit argument}@}, making it {@{_conditional_ on if the implicit argument can be provided}@}. For example {@{a give instance that order lists}@} yields: <!--SR:!2026-12-02,302,349!2026-11-15,285,349!2026-11-22,292,349!2026-11-24,294,349-->

> [!example] __conditional `given`__
>
> {@{A `given` instance}@} may itself {@{require an implicit argument}@}, making it {@{_conditional_ on if the implicit argument can be provided}@}. For example {@{a give instance that order lists}@} yields:
>
> ```Scala
> given listOrdering[A](using ord: Ordering[A]): Ordering[List[A]] with
>   def compare(xs: List[A], ys: List[A]) =
>     (xs, ys) match {
>       case (Nil, Nil)     => 0
>       case (Nil, _)       => -1
>       case (_, Nil)       => 1
>       case (x :: xs1, y :: ys1) =>
>         val c = ord.compare(x, y)
>         if c != 0 then c else compare(xs1, ys1)
>     }
> ```
>
> {@{An `Ordering[List[A]]` exists}@} only when {@{an `Ordering[A]` is available}@}. <!--SR:!2026-02-20,82,350!2026-02-21,83,350!2026-02-19,81,348!2026-02-16,78,348!2026-02-18,80,347!2026-02-16,79,347-->

In {@{some sense}@}, {@{conditional `given`}@} {@{pattern matches on types and their type parameters}@}. In the example above, {@{`listOrdering[A]`}@} pattern matches on {@{`T` in `Ordering[T]`}@} for {@{the pattern `List[A]` in `Ordering[List[A]]`}@}. <!--SR:!2026-12-05,305,349!2026-02-13,76,329!2026-10-04,253,330!2026-11-12,282,349!2026-12-06,306,349!2026-12-08,308,349-->

### recursive `given` resolution

When {@{a method}@} requires {@{an instance that depends on another instance}@}, {@{the compiler}@} {@{resolves them recursively}@}. For example: <!--SR:!2026-02-13,76,329!2026-02-13,76,329!2026-12-03,303,349!2026-02-06,70,329-->

> [!example] __`listOrdering`__
>
> When {@{a method}@} requires {@{an instance that depends on another instance}@}, {@{the compiler}@} {@{resolves them recursively}@}. For example:
>
> ```Scala
> def sortListOfLists(xs: List[List[Int]]) =
>   sort(xs)  // uses `listOrdering[List[Int]]`, then uses `Ordering.Int` inside `listOrdering`
> ```
>
> {@{The compiler}@} first finds {@{`Ordering[List[Int]]`}@}, then finds {@{`Ordering[Int]`}@}, and finally {@{builds them in reverse order}@} and {@{supplies it to `sort`}@}. <!--SR:!2026-02-16,78,347!2026-02-20,82,347!2026-02-15,78,347!2026-02-16,79,347!2026-02-06,70,329!2026-02-13,76,329!2026-02-07,71,329!2026-11-18,292,349!2026-02-17,79,348-->

For {@{another example}@} of {@{recursive `given` resolution}@}, {@{pairs}@} can be {@{ordered lexicographically}@} if {@{both components are orderable}@}: <!--SR:!2026-12-20,318,349!2026-11-09,283,349!2026-10-02,251,330!2026-02-13,76,329!2026-11-27,297,349-->

> [!example] __`pairOrdering`__
>
> For {@{another example}@} of {@{recursive `given` resolution}@}, {@{pairs}@} can be {@{ordered lexicographically}@} if {@{both components are orderable}@}:
>
> ```Scala
> given pairOrdering[A, B](using oa: Ordering[A], ob: Ordering[B]): Ordering[(A, B)] with
>   def compare(x: (A, B), y: (A, B)) =
>     val c = oa.compare(x._1, y._1)
>     if c != 0 then c else ob.compare(x._2, y._2)
> ```
>
> This enables {@{sorting of address records}@} represented as {@{`(Int, String)`}@} by {@{zip code and street name}@}. <!--SR:!2026-02-17,79,347!2026-02-22,84,347!2026-02-19,81,347!2026-02-07,71,329!2026-11-28,298,349!2026-11-27,297,349!2026-02-09,73,348!2026-02-19,81,348-->

## context inference

When a method expects {@{an implicit of type `T` \(e.g. `Ordering[Int]` in the above example\)}@}, the compiler looks for {@{a _`given` instance_ that}@}: \(annotation: 2 items: {@{compatible, visible}@}\) <!--SR:!2026-12-01,301,349!2026-02-13,76,329!2026-02-07,71,329-->

- compatible ::@:: Has a compatible type. <!--SR:!2026-12-04,304,349!2026-11-11,281,349-->
- visibility ::@:: Is visible in the current scope (lexical, imports, parameters) or defined in a companion object associated with `T`. <!--SR:!2026-10-05,254,330!2026-02-13,76,329-->

If {@{exactly one suitable instance exists}@} it is {@{used}@}; otherwise {@{compilation fails}@} due to {@{no instance found}@} or {@{ambiguity}@} if {@{there is more than one _most specific_ instance}@}. It will {@{search in \(in no particular order\)}@}: \(annotation: 3 items: {@{lexical scope, companion objects, enclosing objects}@}\) <!--SR:!2026-10-03,252,330!2026-02-07,71,329!2026-11-25,295,349!2026-12-19,317,349!2026-02-13,76,329!2026-02-13,76,329!2026-02-07,71,329!2026-12-11,311,349-->

- lexical scope ::@:: Visible `given` instances in the lexical scope, including inherited, imported and defined instances. <!--SR:!2026-11-08,282,349!2026-02-13,76,329-->
- companion objects ::@:: Companion objects of `T`, its super-classes, its type arguments, super-classes of its type arguments, etc. <!--SR:!2026-12-17,315,349!2026-10-05,254,330-->
- enclosing objects ::@:: For inner classes, outer enclosing objects. <!--SR:!2026-02-13,76,329!2026-11-28,298,349-->

{@{This mechanism}@} allows {@{libraries}@} to provide {@{default behaviours}@} that can be {@{overridden locally without changing every call site}@}. <!--SR:!2026-12-21,319,349!2026-02-06,70,329!2026-11-15,285,349!2026-11-13,287,349-->

If, after {@{searching the above scopes}@}, {@{more than one candidate exists}@}, the compiler selects {@{the _most specific_ one}@}. {@{A candidate is _more specific_ than another}@} when {@{at least one of the following 4 items hold}@}: \(annotation: 4 items: {@{lexical scope, hierarchy, subtyping, generic instance}@}\) <!--SR:!2026-02-06,70,329!2026-09-23,242,330!2026-08-16,213,329!2026-02-07,71,329!2026-03-04,90,371!2026-03-03,89,371-->

- specificity: lexical scope ::@:: A definition that is in a closer lexical scope is more specific; or <!--SR:!2026-12-14,312,349!2026-11-13,283,349-->
- specificity: hierarchy ::@:: A definition that is in a subclass is more specific than one that in a superclass. <!--SR:!2026-09-17,236,330!2026-02-13,76,329-->
- specificity: subtyping ::@:: A definition that has a type that is a subclass of the type of the other definition is more specific. <!--SR:!2026-02-07,71,329!2026-02-13,76,329-->
- specificity: generic instance ::@:: A definition that has a type that is a generic instance \(e.g. `Type[Int]`\) of the type of the other definition \(e.g. `Type[T]` where `T` is generic\) is more specific. <!--SR:!2026-09-21,240,330!2026-02-07,71,329-->

Thus you can provide {@{multiple `given`s}@} and rely on Scala's rules to pick {@{the appropriate one automatically}@}. <!--SR:!2026-11-25,295,349!2026-02-07,71,329-->

## type class

In Scala {@{a _type class_}@} is {@{a generic trait}@} that declares {@{operations for a type `A`}@} and is instantiated by {@{`given` definitions for particular types}@}. {@{The pattern}@} is inspired by {@{Haskell's type-class mechanism}@} but expressed in Scala through {@{contextual parameters (`using`) and implicit resolution}@}. <!--SR:!2026-10-06,255,330!2026-11-26,296,349!2026-11-16,286,349!2026-09-19,238,330!2026-12-06,306,349!2026-02-07,71,329!2026-02-06,70,329-->

{@{Type classes}@} turn {@{a type into a value}@} by providing {@{a trait and concrete instances}@}. They enable {@{_ad-hoc polymorphism_}@}: {@{different implementations}@} for {@{different types}@}. <!--SR:!2026-11-17,287,349!2026-12-11,311,349!2026-02-13,76,329!2026-11-27,297,349!2026-02-13,76,329!2026-11-27,297,349-->

{@{Other languages}@} adopt {@{similar concepts}@}: {@{Haskell}@}'s {@{built-in type classes}@}, {@{Rust}@}'s {@{traits}@}, and {@{emerging features}@} in {@{Agda, Lean, and OCaml}@}. In {@{Scala}@} {@{the mechanism is realized}@} through {@{contextual parameters (`using`) and implicit resolution}@}, giving programmers {@{fine-grained control over polymorphic behaviour}@}. <!--SR:!2026-11-11,281,349!2026-11-22,292,349!2026-12-21,319,349!2026-12-03,303,349!2026-11-07,281,349!2026-11-15,285,349!2026-02-13,76,329!2026-12-06,306,349!2026-02-06,70,329!2026-02-13,76,329!2026-02-13,76,329!2026-02-13,76,329-->

### type class pattern

To {@{declare a "type class"}@} in Scala, use {@{`trait`}@}: <!--SR:!2026-12-09,309,349!2026-12-02,302,349-->

> [!example] __type class definition__
>
> To {@{declare a "type class"}@} in Scala, use {@{`trait`}@}:
>
> ```Scala
> trait Ordering[A]:
>   def compare(x: A, y: A): Int
> ```
<!--SR:!2026-12-11,311,349!2026-02-13,76,329-->

{@{A `given` instance}@} supplies {@{the implementation for a concrete type}@}: <!--SR:!2026-12-17,315,349!2026-11-10,284,349-->

> [!example] __type class implementation__
>
> {@{A `given` instance}@} supplies {@{the implementation for a concrete type}@}:
>
> ```Scala
> given orderingInt: Ordering[Int] with
>   def compare(x: Int, y: Int) =
>     if x < y then -1 else if x > y then 1 else 0
> given orderingString: Ordering[String] with
>   def compare(s: String, t: String) = s.compareTo(t)
> ```
<!--SR:!2026-02-06,70,329!2026-02-13,76,329-->

With {@{such `given` instances}@} in scope {@{a polymorphic method}@} can be written: <!--SR:!2026-02-07,71,329!2026-02-06,70,329-->

> [!example] __type class implementation__
>
> With {@{such `given` instances}@} in scope {@{a polymorphic method}@} can be written:
>
> ```Scala
> def sort[A](xs: List[A])(using ord: Ordering[A]): List[A] =
>   xs.sorted // uses `ord` for comparison
> ```
>
> {@{The compiler}@} resolves {@{the appropriate `Ordering[A]` at compile time}@}. <!--SR:!2026-02-07,71,329!2026-09-30,249,330!2026-12-22,320,349!2026-11-30,300,349-->

### retroactive extension

{@{A type class}@} can be {@{implemented for a data type}@} without {@{modifying its definition}@}. For example, {@{a rational number type}@}: <!--SR:!2026-11-29,299,349!2026-02-13,76,329!2026-11-16,286,349!2026-11-11,285,349-->

> [!example] __retroactively extending `Rational`__
>
> {@{A type class}@} can be {@{implemented for a data type}@} without {@{modifying its definition}@}. For example, {@{a rational number type}@}:
>
> ```Scala
> case class Rational(num: Int, denom: Int)
>
> given rationalOrdering: Ordering[Rational] with
>   def compare(x: Rational, y: Rational) =
>     val xn = x.num * y.denom
>     val yn = y.num * x.denom
>     if xn < yn then -1 else if xn > yn then 1 else 0
> ```
>
> Now {@{`Rational` values}@} can be {@{sorted or compared using the same generic machinery \(e.g. `sort`\)}@}. Note {@{the definition of `Rational`}@} does not {@{need to be modified}@}. <!--SR:!2026-02-22,84,350!2026-02-22,84,350!2026-02-23,85,350!2026-02-21,83,350!2026-02-18,80,348!2026-02-21,83,348!2026-02-11,75,348!2026-02-10,74,348-->

### extension methods

{@{A type-class trait}@} may declare {@{_extension methods_}@} that become {@{available when an instance is in scope}@}: <!--SR:!2026-12-02,302,349!2026-11-22,292,349!2026-02-06,70,329-->

> [!example] __type class extension methods__
>
> {@{A type-class trait}@} may declare {@{_extension methods_}@} that become {@{available when an instance is in scope}@}:
>
> ```Scala
> trait Ordering[A]:
>   def compare(x: A, y: A): Int
>   extension (x: A)
>     def <(y: A)   = compare(x, y) < 0
>     def <=(y: A)  = compare(x, y) <= 0
>     def >(y: A)   = compare(x, y) > 0
>     def >=(y: A)  = compare(x, y) >= 0
> ```
<!--SR:!2026-02-06,70,329!2026-02-06,70,329!2026-12-07,307,349-->

With {@{an `Ordering[T]` in scope}@} one can {@{write}@}: <!--SR:!2026-10-03,252,330!2026-02-06,70,329-->

> [!example] __type class extension methods usage__
>
> With {@{an `Ordering[T]` in scope}@} one can {@{write}@}:
>
> ```Scala
> def merge[T](xs: List[T], ys: List[T])(using ord: Ordering[T]): List[T] =
>   (xs, ys) match {
>     case (Nil, _) => ys
>     case (_, Nil) => xs
>     case (x :: xs1, y :: ys1) =>
>       if x < y then x :: merge(xs1, ys)
>       else y :: merge(xs, ys1)
>   }
> ```
>
> No {@{explicit import of the instance `Ordering[T]`}@} is {@{required}@}; {@{the extension method `<`}@} is resolved {@{via the implicit `Ordering[T]`}@}. <!--SR:!2026-02-21,83,350!2026-02-22,84,350!2026-02-23,85,350!2026-02-23,85,350!2026-02-16,78,348!2026-02-18,80,348-->

### type class in other languages

{@{Haskell}@} treats {@{type classes}@} as {@{a first-class feature of the language}@}.  {@{The standard library}@} defines {@{an `Ordering` data type}@} ({@{`data Ordering = LT | EQ | GT`}@}) and declares {@{the class}@} <!--SR:!2026-02-13,76,329!2026-02-07,71,329!2026-02-13,76,329!2026-11-30,300,349!2026-02-13,76,329!2026-12-19,317,349!2026-09-14,233,330-->

> [!example] __type class in Haskell__
>
> {@{The standard library}@} defines {@{an `Ordering` data type}@} ({@{`data Ordering = LT | EQ | GT`}@}) and declares {@{the class}@}
>
> ```Haskell
> class Ord a where
>     compare :: a -> a -> Int
> ```
>
> {@{`class Ord`}@} specifies {@{how values of any type `a` can be compared}@}. <!--SR:!2026-02-23,85,350!2026-02-17,80,350!2026-02-21,83,350!2026-02-21,83,350!2026-02-20,82,350!2026-02-17,80,350-->

{@{`class Ord`}@} specifies {@{how values of any type `a` can be compared}@}. Because {@{the mechanism is built-in}@}, Haskell's {@{type-class system}@} is {@{simpler to reason about}@} than Scala's {@{more general contextual parameters}@}. <!--SR:!2026-02-22,84,351!2026-02-20,82,351!2026-02-23,85,351!2026-02-23,85,351!2026-02-23,85,351!2026-02-20,82,351-->

{@{Modern systems such as Rust}@} have adopted {@{an analogous construct}@}: the language offers {@{_traits_}@}, which are {@{essentially type classes}@}. {@{A typical Rust trait}@} that {@{mirrors `Ord`}@} looks like: <!--SR:!2026-02-06,70,329!2026-11-29,299,349!2026-07-08,175,310!2026-02-13,76,329!2026-11-18,292,349!2026-02-13,76,329-->

> [!example] __type class in Rust__
>
> {@{A typical Rust trait}@} that {@{mirrors `Ord`}@} looks like:
>
> ```Rust
> pub trait Ord: Eq + PartialOrd {
>     fn cmp(&self, other: &Self) -> Ordering;
> }
> ```
<!--SR:!2026-12-11,311,349!2026-02-13,76,329-->

{@{The syntax in Rust}@} is {@{slightly different}@} but {@{the concept}@} remains {@{the same}@}—defining {@{a set of operations}@} that can be {@{implemented for many distinct types}@}. <!--SR:!2026-02-07,71,329!2026-09-16,235,330!2026-10-02,251,330!2026-12-09,309,349!2026-02-13,76,329!2026-02-07,71,329-->

{@{Other functional and dependently-typed languages}@} are moving {@{toward a similar approach}@}.  {@{Agda, Lean, and soon OCaml}@} provide {@{general _contextual parameters_ or equivalent mechanisms}@} that allow {@{programmers to encode type-class-like behaviour}@} in a manner analogous to {@{Scala's `given` instances}@}.  {@{These systems}@} combine the expressiveness of {@{Haskell's type classes with Scala-style contextual resolution}@}, enabling {@{conditional polymorphism across a wide range of types}@}. <!--SR:!2026-11-30,300,349!2026-02-13,76,329!2026-10-02,251,330!2026-10-06,255,330!2026-02-13,76,329!2026-02-13,76,329!2026-11-08,282,349!2026-02-13,76,329!2026-12-04,305,349-->

## monoid example

{@{Monoids extend semigroups}@} by adding {@{a neutral element _unit_}@}. A simple {@{Scala definition}@} is <!--SR:!2026-06-11,128,391!2026-06-01,118,391!2026-06-03,120,391-->

> [!example] __monoid trait__
>
> {@{The monoid interface}@} extends {@{the semigroup}@} and declares {@{an abstract `unit`}@}.
>
> ```Scala
> trait Monoid[T] extends SemiGroup[T]:
>   def unit: T
> ```
<!--SR:!2026-05-30,120,391!2026-06-11,128,391!2026-06-03,124,391-->

{@{The standard list reduction `reduce`}@} can be rewritten using {@{a monoid instance}@}, making use of {@{the neutral element `unit`}@}: <!--SR:!2026-06-04,121,391!2026-06-05,122,391!2026-06-10,127,391-->

> [!example] __monoid‑aware reduce__
>
> Uses {@{the monoid’s `unit`}@} as {@{initial value}@}, so {@{empty lists are handled}@}.
>
> ```Scala
> def reduce[T: Monoid](xs: List[T]): T =
>   xs.reduceLeft(Monoid[T].unit)(_.combine(_))
> ```
<!--SR:!2026-06-06,123,391!2026-06-03,120,391!2026-06-01,118,391-->

With {@{a _context bound_ (`T: Monoid`)}@} and {@{the companion object}@} we avoid passing {@{the instance (`Monoid[T]`) explicitly}@}. <!--SR:!2026-06-10,127,391!2026-06-08,125,391!2026-06-02,119,391-->

A type may have {@{several monoid instances}@}, e.g. {@{`Int`}@} with {@{addition or multiplication}@}: <!--SR:!2026-06-05,122,391!2026-06-05,122,391!2026-06-04,121,391-->

> [!example] __integer monoids__
>
> {@{Two given instances for `Int`}@}: one for {@{sum, one for product}@}.
>
> ```Scala
> given sumMonoid: Monoid[Int] with
>   extension (x: Int) def combine(y: Int): Int = x + y
>   def unit: Int = 0
> given prodMonoid: Monoid[Int] with
>   extension (x: Int) def combine(y: Int): Int = x * y
>   def unit: Int = 1
> ```
<!--SR:!2026-05-31,117,391!2026-06-03,124,391-->

Using these, {@{`sum` and `product`}@} are defined by supplying {@{the appropriate instance to `reduce`}@}: <!--SR:!2026-06-01,118,391!2026-06-05,122,391-->

> [!example] __sum and product__
>
> {@{Calls `reduce`}@} with {@{the chosen monoid}@} to implement {@{`sum` and `product`}@}.
>
> ```Scala
> def sum(xs: List[Int]): Int   = reduce(xs)(using sumMonoid)
> def product(xs: List[Int]): Int = reduce(xs)(using prodMonoid)
> ```
<!--SR:!2026-06-04,125,391!2026-05-31,117,391!2026-06-03,120,391-->

{@{Omitting the `using` clause}@} leads to {@{an _ambiguity_ error}@} because {@{both instances (`sumMonoid` and `prodMonoid`) are in scope}@}. The expression {@{`reduce(xs)(using sumMonoid)`}@} showcases {@{_context_—the implicit search that supplies the correct monoid}@}. If {@{no instance is found or multiple exist}@}, {@{compilation fails}@}, enforcing the rule that each type has {@{at most one lawful monoid per program fragment}@}. <!--SR:!2026-06-03,120,391!2026-06-03,124,391!2026-05-29,115,391!2026-06-07,124,391!2026-06-09,126,391!2026-06-05,122,391!2026-06-06,123,391!2026-06-02,123,391-->

{@{A monoid}@} must satisfy {@{the associativity law `x.combine(y).combine(z) == x.combine(y.combine(z))` and the identity laws `unit.combine(x) == x  &&  x.combine(unit) == x`}@}. These laws guarantee that {@{`reduce` behaves consistently}@}, e.g. for {@{empty lists}@} it returns {@{the neutral element}@} and for {@{non‑empty lists}@} it equals {@{the left fold using the monoid’s combine}@}. {@{The same pattern applies}@} to other algebraic structures such as {@{_groups_ or _monads_}@}, where a type class encodes {@{the operations and their laws}@}. <!--SR:!2026-06-08,125,391!2026-06-06,123,391!2026-06-02,119,391!2026-06-05,126,391!2026-06-02,119,391!2026-06-09,126,391!2026-06-01,122,391!2026-05-30,116,391!2026-06-10,127,391!2026-05-31,117,391-->

## context management

{@{There are two major ways}@} to use {@{Scala context}@}: {@{type classes and providing execution context}@}. Above, we have focused on {@{type classes}@}, which are about {@{_type_ instances of generic traits}@}. To use an instance, {@{a contextual parameter}@} is required: <!--SR:!2026-06-05,126,391!2026-05-29,115,391!2026-06-02,119,391!2026-06-06,123,391!2026-06-05,126,391!2026-06-10,127,391-->

> [!example] __using a contextual parameter__
>
> {@{Type classes}@} are about {@{_type_ instances of generic traits}@}. To use an instance, {@{a contextual parameter}@} is required:
>
> ```Scala
> def foo[T](x: T)(using ev: TC[T]) = …
> ```
>
> Here `ev` supplies {@{the concrete implementation of the type class `TC`}@}. {@{Contextual parameters}@} are {@{values, not types}@}; they are looked up at {@{call site}@}. <!--SR:!2026-05-31,117,391!2026-06-08,125,391!2026-05-28,114,391!2026-06-09,126,391!2026-06-05,126,391!2026-05-31,117,391!2026-05-31,117,391-->

In contrast, {@{an execution context}@} usually abstracts over {@{a simple type}@}, and provides information needed to {@{execute the current code}@}. Intuitively, {@{_type classes_, implemented using Scala contexts}@}, provide {@{_type-level_ information}@}, while {@{_execution contexts_, also implemented using Scala contexts}@}, provide {@{_runtime-level_ information}@}. <!--SR:!2026-06-07,124,391!2026-06-09,126,391!2026-06-01,118,391!2026-06-02,123,391!2026-06-08,125,391!2026-06-04,121,391!2026-06-07,124,391-->

### execution contexts  

An example where {@{execution contexts become useful}@} is {@{parallel runtimes}@}. Parallel runtimes need {@{schedulers}@}. {@{A scheduler}@} is represented by {@{the type `ExecutionContext`}@}. {@{A default instance}@} is usually declared as <!--SR:!2026-06-02,123,391!2026-06-05,122,391!2026-06-08,125,391!2026-06-11,128,391!2026-06-05,122,391!2026-06-02,119,391-->

> [!example] __default execution context__
>
> Parallel runtimes need {@{schedulers}@}. {@{A scheduler}@} is represented by {@{the type `ExecutionContext`}@}. {@{A default instance}@} is usually declared as
>
> ```Scala
> given global: ExecutionContext = ForkJoinPool.commonPool()
> ```
>
> {@{The scheduler pool}@} is {@{lazily initialised on first use}@}. <!--SR:!2026-06-04,125,391!2026-06-06,123,391!2026-05-31,117,391!2026-06-04,125,391!2026-06-03,124,391!2026-06-04,125,391-->

{@{Functions that run asynchronous code}@} take it as {@{a contextual parameter}@}: <!--SR:!2026-06-03,120,391!2026-06-01,118,391-->

> [!example] __passing an execution context__
>
> {@{Functions that run asynchronous code}@} take it as {@{a contextual parameter}@}:
>
> ```Scala
> def processItems(items: List[Int])(using ec: ExecutionContext): Unit = ...
> ```
<!--SR:!2026-06-11,128,391!2026-06-06,127,391-->

{@{The same mechanism}@} propagates {@{the context through a call chain without having to thread the value explicitly}@}. When {@{specific code needs to use a specialized `ExecutionContext`}@}, {@{declaring another `given` instance}@} can be used to override {@{the `global` instance}@}. <!--SR:!2026-06-09,126,391!2026-06-11,128,391!2026-06-09,126,391!2026-06-09,126,391!2026-06-08,125,391-->

Another example is {@{an expression language}@} carrying {@{its own _environment_ as a contextual value}@}. <!--SR:!2026-05-30,120,391!2026-06-11,128,391-->

> [!example] __expression language environment__
>
> Another example is {@{an expression language}@} carrying {@{its own _environment_ as a contextual value}@}.
>
> ```Scala
> enum Expr:
>   case Number(n: Int)
>   case Sum(x, y: Expr)
>   case Prod(x, y: Expr)
>   case Var(name: String)
>   case Let(name: String, rhs: Expr, body: Expr)
>
> def eval(e: Expr): Int =
>   def recur(e: Expr)(using env: Map[String, Int]): Int = e match
>     case Number(n)            => n
>     case Sum(x, y)             => recur(x) + recur(y)
>     case Prod(x, y)            => recur(x) * recur(y)
>     case Var(name)             => env(name)
>     case Let(name, rhs, body)  =>
>       recur(body)(using env + (name -> recur(rhs)))
>   recur(e)(using Map.empty)
> ```
<!--SR:!2026-06-04,121,391!2026-06-06,127,391-->

{@{The `env` contextual parameter}@} is {@{implicitly supplied at each recursive call}@}; it represents {@{the current bindings of variables}@}. This pattern demonstrates how {@{contextual parameters can model mutable state that is scoped to a computation}@}, without {@{leaking it into the surrounding code}@}. <!--SR:!2026-06-06,123,391!2026-06-11,128,391!2026-06-07,124,391!2026-06-04,121,391!2026-06-04,121,391-->

### opaque type aliases for safety

{@{Using common types such as `Int` or `String`}@} as {@{global given instances}@} is {@{error‑prone}@}. Instead, {@{opaque types}@} hide {@{the underlying representation}@}: <!--SR:!2026-06-07,124,391!2026-06-07,124,391!2026-06-01,118,391!2026-05-31,117,391!2026-06-08,125,391-->

> [!example] __opaque type alias__
>
> {@{Using common types such as `Int` or `String`}@} as {@{global given instances}@} is {@{error‑prone}@}. Instead, {@{opaque types}@} hide {@{the underlying representation}@}:
>
> ```Scala
> object Conf:
>   opaque type Viewers = Set[String]
>   def create(v: Person*): Viewers = v.map(_.name).toSet
> ```
>
> Outside {@{the current scope (`Conf`)}@}, the alias is {@{an abstract type}@}; two different modules can declare {@{their own `Viewers` without clash}@}. <!--SR:!2026-05-28,114,391!2026-05-30,120,391!2026-06-06,123,391!2026-06-07,124,391!2026-06-10,127,391!2026-06-02,119,391!2026-05-29,115,391!2026-05-31,121,391-->

Outside {@{the current scope (`Conf`)}@}, the alias is {@{an abstract type}@}; two different modules can declare {@{their own `Viewers` without clash}@}. When {@{a function requires this context}@}, it declares {@{a contextual parameter}@}: <!--SR:!2026-06-03,120,391!2026-06-06,127,391!2026-06-05,126,391!2026-06-06,127,391!2026-06-02,119,391-->

> [!example] __contextual parameter with opaque type__
>
> When {@{a function requires this context}@}, it declares {@{a contextual parameter}@}:
>
> ```Scala
> def task(x: Int)(using v: Conf.Viewers): Boolean =
>   summon[Conf.Viewers].contains("Alice")
> ```
<!--SR:!2026-06-03,120,391!2026-05-30,116,391-->

## implicit function types

{@{Scala's _using_ clauses}@} can be lifted into {@{first‑class values}@} by turning them into {@{implicit function types (`A ?=> B`)}@} <!--SR:!2026-05-30,120,391!2026-05-31,117,391!2026-06-05,126,391-->

A method that previously {@{required an explicit `using Viewers` argument}@} can now be written as {@{a method returning a value of type `Viewers ?=> List[Paper]`}@}. The compiler infers {@{the `using` argument automatically}@}, so callers still {@{need not pass it explicitly just as before}@}. <!--SR:!2026-06-05,122,391!2026-06-04,125,391!2026-05-28,114,391!2026-05-30,116,391-->

> [!example] __implicit function type__
>
> A method that previously {@{required an explicit `using Viewers` argument}@} can now be written as {@{a method returning a value of type `Viewers ?=> List[Paper]`}@}. The compiler infers {@{the `using` argument automatically}@}, so callers still {@{need not pass it explicitly just as before}@}.
>
> ```Scala
> def rankings: Viewers ?=> List[Paper]
> ```
>
> The expression `rankings` expands to {@{`rankings(using viewers)`}@}; {@{the implicit argument}@} is supplied by {@{the compiler}@}. <!--SR:!2026-05-28,118,391!2026-06-03,120,391!2026-06-03,120,391!2026-06-05,122,391!2026-06-10,127,391!2026-05-30,116,391!2026-06-06,127,391-->

Replacing {@{a method signature ending in `/* ... */ (using Viewers): T`}@} with {@{`/* ... */ : Viewed[T]` (where `type Viewed[T] = Viewers ?=> T`)}@} shortens {@{the syntax and keeps the same semantics}@}. <!--SR:!2026-06-01,118,391!2026-06-09,126,391!2026-06-04,121,391-->

> [!example] __type alias for context abstraction__
>
> Replacing {@{a method signature ending in `/* ... */ (using Viewers): T`}@} with {@{`/* ... */ : Viewed[T]` (where `type Viewed[T] = Viewers ?=> T`)}@} shortens {@{the syntax and keeps the same semantics}@}.
>
> ```Scala
> type Viewed[T] = Viewers ?=> T
> def rankings: Viewed[List[Paper]]
> ```
<!--SR:!2026-05-28,114,391!2026-06-01,118,391!2026-06-04,121,391-->

It trades {@{a term for a type}@}. Originally, the developer writes {@{the required implicit _type_ (`Viewers`)}@}, and {@{the compiler supplies the actual value}@}. Now with {@{implicit function types}@}, the developer writes {@{the _return type_ (`Viewed[List[Paper]]`)}@}, and the compiler {@{_additionally_ infers implicit function parameters before inferring its actual value}@}. <!--SR:!2026-06-08,125,391!2026-06-03,124,391!2026-05-29,115,391!2026-05-29,119,391!2026-06-02,119,391!2026-05-30,120,391-->
