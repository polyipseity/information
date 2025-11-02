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

Normally in Scala, {@{values \(terms\) and types}@} infer {@{types}@}, e.g. {@{inferring type parameters}@}. Sometimes you want {@{types to infer values}@} instead, called {@{_type-directed programming_}@}. This is helpful for abstracting {@{context based on types}@}.

## motivation

We want to write {@{code that is _modular_}@} by {@{abstracting over the "context" in which it will run}@}. {@{Context}@} can be {@{the current configuration, security level}@}, or even {@{a user on whose behalf an operation executes}@}.  In practice this means making {@{functions and classes independent of global state \(dependent on "context"\)}@} so they can be {@{reused safely across modules}@}. There are several {@{common approaches}@}: \(annotation: 5 items: {@{globals, mutable globals, monkey patch, dependency injection, functional context}@}\)

- globals ::@:: Simple to use. Rigid, hard to change per module.
- mutable globals ::@:: Flexible but unsafe. Risk of interference \(e.g. race conditions\).
- monkey patch ::@:: Powerful and dynamic. Can break code and debugging.
- dependency injection ::@:: Encapsulates configuration. Relies on bytecode rewriting and opaque. Frameworks include Guice, Spring, etc.
- functional context ::@:: Normally, values and types infer types but not values, e.g. inferring type parameters. With `using`, types are used to infer values. Those values provide "context".

### higher-order functions

When {@{a method}@} needs to {@{operate over arbitrary types}@} – for example, {@{a generic `sort`}@} – {@{the natural solution}@} is to {@{type parameterise it}@}:

> [!example] __parameterized sort__
>
> When {@{a method}@} needs to {@{operate over arbitrary types}@} – for example, {@{a generic `sort`}@} – {@{the natural solution}@} is to {@{type parameterise it}@}:
>
> ```Scala
> def sort[T](xs: List[T]): List[T] = ???
> ```

However, {@{sorting}@} requires {@{an ordering relation `<`}@}, which {@{does not exist for all types}@}.  {@{The resolution}@} is to {@{_parameterise with an ordering_ rather than just a type}@}.

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

Scala provides {@{the `scala.math.Ordering` trait}@} to {@{represent the sorting function}@}:

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

## `using`

To {@{reduce boilerplate}@} {@{the `ord` argument}@} can be declared {@{_implicit_ via a `using` clause}@}:

> [!example] __parameterized sort with implicit ordering__
>
> To {@{reduce boilerplate}@} {@{the `ord` argument}@} can be declared {@{_implicit_ via a `using` clause}@}:
>
> ```Scala
> def sort[T](xs: List[T])(using ord: Ordering[T]): List[T] = ...
> ```
>
> Now {@{callers}@} need not {@{supply it explicitly \(though it could if it chooses to\)}@}; {@{the compiler}@} searches for {@{an implicit `Ordering[T]` in scope}@} and {@{supplies it automatically}@}.

Now {@{callers}@} need not {@{supply it explicitly \(though it could if it chooses to\)}@}; {@{the compiler}@} searches for {@{an implicit `Ordering[T]` in scope}@} and {@{supplies it automatically}@}. {@{Calling it}@} becomes {@{simpler}@}:

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
> The compiler also infers {@{the type argument `T` from the argument list}@}. If {@{a single obvious value exists for a type}@}, the compiler may even infer {@{that _term_ itself (e.g., `Ordering.Int`)}@}.

The compiler also infers {@{the type argument `T` from the argument list}@}. If {@{a single obvious value exists for a type}@}, the compiler may even infer {@{that _term_ itself (e.g., `Ordering.Int`)}@}, as in the above example.

### `using` syntax

In Scala, {@{an implicit parameter}@} is introduced through {@{a `using` clause in the method signature}@}:

> [!example] __`using` in method__
>
> In Scala, {@{an implicit parameter}@} is introduced through {@{a `using` clause in the method signature}@}:
>
> ```Scala
> def sort[T](xs: List[T])(using ord: Ordering[T]): List[T] = …
> ```

When calling {@{such a method}@}, you may {@{supply the argument explicitly}@} via {@{another `using` clause}@}:

> [!example] __`using` in method call__
>
> When calling {@{such a method}@}, you may {@{supply the argument explicitly}@} via {@{another `using` clause}@}:
>
> ```Scala
> sort(strings)(using Ordering.String)
> sort(strings)  // compiler finds `Ordering.String`
> ```
>
> However, {@{explicit passing}@} is {@{usually unnecessary}@}.

However, {@{explicit passing}@} is {@{usually unnecessary}@}. If the caller {@{omits the `using` argument}@}, the compiler {@{automatically searches for an appropriate instance of `Ordering[T]`}@} and {@{supplies it implicitly}@}, as in the second line above.

{@{The syntax for `using` clauses}@} is {@{flexible}@}. {@{A single clause}@} may contain {@{multiple parameters}@}:

> [!example] __`using` multiple parameters__
>
> {@{The syntax for `using` clauses}@} is {@{flexible}@}. {@{A single clause}@} may contain {@{multiple parameters}@}:
>
> ```Scala
> def f(x: Int)(using a: A, b: B) = ...
> f(10)(using a, b)
> ```

Alternatively, {@{separate `using` clauses}@} can be {@{chained}@}. {@{`using` clauses}@} can also be {@{interleaved with ordinary parameter lists}@}, allowing {@{a mix of implicit and explicit arguments}@}:

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

{@{Anonymous `using` clauses}@} let a method declare {@{an implicit parameter without naming it}@}; the compiler will still {@{supply and forward that instance to other methods automatically}@}. For example,

> [!example] __anonymous `using` clauses__
>
> {@{Anonymous `using` clauses}@} let a method declare {@{an implicit parameter without naming it}@}; the compiler will still {@{supply and forward that instance to other methods automatically}@}. For example,
>
> ```Scala
> def sort[T](xs: List[T])(using Ordering[T]): List[T] =
>   ...  // omitted
>   merge(sort(fst), sort(snd)) …
> ```
>
> can be written with {@{an unnamed `Ordering[T]`}@}, yet internally {@{each `merge` and `sort` implicitly receives the same ordering}@}.

This is equivalent to explicitly {@{passing a named `ord` through every call that needs an `Ordering` implicitly}@}, but keeps the body of `sort` {@{free from boilerplate}@} and shows that {@{the implicit context can propagate transparently}@} even when the method itself {@{never directly references the parameter}@}.

### context bound

{@{A shorthand}@} for declaring {@{an implicit parameter}@} is {@{the _context bound_}@}, which {@{expands to a `using` clause under the hood}@}:

> [!example] __context bound__
>
> {@{A shorthand}@} for declaring {@{an implicit parameter}@} is {@{the _context bound_}@}, which {@{expands to a `using` clause under the hood}@}:
>
> ```Scala
> def printSorted[T: Ordering](xs: List[T]) =
>   println(sort(xs))
> ```
>
> Intuitively, this may be interpreted as {@{`T` "satisfying" the trait `Ordering`}@}, i.e. having {@{a defined ordering}@}.

Intuitively, {@{a context bound `T : U`}@} may be interpreted as {@{the type parameter `T` "satisfying" the "trait" `U`}@}.

More generally, {@{any definition `def f[T : {U1, ..., Un}](ps) : R`}@} \({@{_deprecated_ syntax}@}: {@{`def f[T : U1 : ... : Un](ps) : R`}@}\) is expanded to {@{`def f[T](ps)(using U1[T], ..., Un[T]) : R`}@}. {@{This transformation}@} makes {@{context bounds a convenient shorthand}@} for {@{implicit parameters without altering the generated code}@}.

## `given`

Scala 3 introduces {@{_given instances_}@} – {@{values}@} that can be {@{automatically supplied for implicit parameters}@}:

> [!example] __`Ordering.Int`__
>
> Scala 3 introduces {@{_given instances_}@} – {@{values}@} that can be {@{automatically supplied for implicit parameters}@}:
>
> ```Scala
> object Ordering:
>   given Int: Ordering[Int] with
>     def compare(x: Int, y: Int): Int =
>       if (x < y) -1 else if (x > y) 1 else 0
> ```

{@{Anonymous instances}@} can be {@{declared without a name}@}; the compiler will {@{generate a name}@}:

> [!example] __`Ordering[Double]`__
>
> {@{Anonymous instances}@} can be {@{declared without a name}@}; the compiler will {@{generate a name}@}:
>
> ```Scala
> given Ordering[Double] with
>   def compare(x: Double, y: Double): Int = ...
> ```

To refer to {@{an instance directly without using `using`}@}, you may {@{use `summon`}@}:

> [!example] __`summon`__
>
> To refer to {@{an instance directly without using `using`}@}, you may {@{use `summon`}@}:
>
> ```Scala
> val intOrd = summon[Ordering[Int]]      // expands to Ordering.Int
> val dblOrd = summon[Ordering[Double]]   // anonymous name
> ```

{@{`summon`}@} simply uses {@{`using` in its implementation}@}; it is {@{defined as}@}:

> [!example] __`summon` implementation__
>
> {@{`summon`}@} simply uses {@{`using` in its implementation}@}; it is {@{defined as an identity function on the implicit argument}@}:
>
> ```Scala
> def summon[T](using x: T): T = x
> ```

### importing `given`s

There are {@{three forms of import}@} to {@{import `given`s}@}: \(annotation: 3 items: {@{by name, by type, by wildcard}@}\)

- by name ::@:: `import scala.math.Ordering.Int`
- by type ::@:: using the `given` keyword, e.g., `import scala.math.Ordering.{given Ordering[Int]}`, `import scala.math.Ordering.{given Ordering[?]}`
- by wildcard ::@:: via a blanket wildcard, e.g. `import scala.math.given`

Since {@{the actual names of given instances}@} are {@{irrelevant to resolution}@}, {@{importing by type}@} is {@{preferred}@} because it explicitly {@{states which implicit instance you intend to use}@}.

### conditional `given`

{@{A given instance}@} may itself {@{require an implicit argument}@}, making it {@{_conditional_ on if the implicit argument can be provided}@}. For example {@{a give instance that order lists}@} yields:

> [!example] __conditional `given`__
>
> {@{A given instance}@} may itself {@{require an implicit argument}@}, making it {@{_conditional_ on if the implicit argument can be provided}@}. For example {@{a give instance that order lists}@} yields:
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
> {@{An `Ordering[List[A]]` exists}@} only when {@{an `Ordering[A]` is available}@}.

In {@{some sense}@}, {@{conditional `given`}@} {@{pattern matches on type and its type parameter}@}. In the example above, {@{`listOrdering[T]`}@} pattern matches on {@{`T`}@} for {@{the pattern `List[U]`}@}.

### recursive `given` resolution

When {@{a method}@} requires {@{an instance that depends on another instance}@}, {@{the compiler}@} {@{resolves them recursively}@}. For example:

> [!example] __`listOrdering`__
>
> When {@{a method}@} requires {@{an instance that depends on another instance}@}, {@{the compiler}@} {@{resolves them recursively}@}. For example:
>
> ```Scala
> def sortListOfLists(xs: List[List[Int]]) =
>   sort(xs)  // uses `listOrdering[List[Int]]`, then uses `Ordering.Int` inside `listOrdering`
> ```
>
> {@{The compiler}@} first finds {@{`Ordering[List[Int]]`}@}, then finds {@{`Ordering[Int]`}@}, and finally {@{builds them in reverse order}@} and {@{supplies it to `sort`}@}.

For {@{another example}@} of {@{recursive `given` resolution}@}, {@{pairs}@} can be {@{ordered lexicographically}@} if {@{both components are orderable}@}:

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
> This enables {@{sorting of address records}@} represented as {@{`(Int, String)`}@} by {@{zip code and street name}@}.

## context inference

When a method expects {@{an implicit of type `T` \(e.g. `Ordering[Int]` in the above example\)}@}, the compiler looks for {@{a _given instance_ that}@}: \(annotation: 2 items: {@{compatible, visible}@}\)

- compatible ::@:: Has a compatible type.
- visibility ::@:: Is visible in the current scope (lexical, imports, parameters) or defined in a companion object associated with `T`.

If {@{exactly one suitable instance exists}@} it is {@{used}@}; otherwise {@{compilation fails}@} due to {@{no instance found}@} or {@{ambiguity}@} if {@{there is more than one _most specific_ instance}@}. It will {@{search in \(in no particular order\)}@}: \(annotation: 3 items: {@{lexical scope, companion objects, enclosing objects}@}\)

- lexical scope ::@:: Visible given instances in the lexical scope, including inherited, imported and defined instances.
- companion objects ::@:: Companion objects of `T`, its super‑classes, its type arguments, super-classes of its type arguments, etc.
- enclosing objects ::@:: For inner classes, outer enclosing objects.

{@{This mechanism}@} allows {@{libraries}@} to provide {@{default behaviours}@} that can be {@{overridden locally without changing every call site}@}.

If, after {@{searching the above scopes}@}, {@{more than one candidate exists}@}, the compiler selects {@{the _most specific_ when one of the following is satisfied}@}: \(annotation: 4 items: {@{lexical scope, hierarchy, subtyping, generic instance}@}\)

- specificity, lexical scope ::@:: A definition that is in a closer lexical scope is more specific; or
- specificity, hierarchy ::@:: A definition that is in a subclass is more specific than one that in a superclass.
- specificity, subtyping ::@:: A definition that has a type that is a subclass of the type of the other definition is more specific.
- specificity, generic instance ::@:: A definition that has a type that is a generic instance \(e.g. `Type[Int]`\) of the type of the other definition \(e.g. `Type[T]` where `T` is generic\) is more specific.

Thus you can provide {@{multiple givens}@} and rely on Scala's rules to pick {@{the appropriate one automatically}@}.

## type class

In Scala {@{a _type class_}@} is {@{a generic trait}@} that declares {@{operations for a type `A`}@} and is instantiated by {@{`given` definitions for particular types}@}. {@{The pattern}@} is inspired by {@{Haskell's type‑class mechanism}@} but expressed in Scala through {@{contextual parameters (`using`) and implicit resolution}@}.

{@{Type classes}@} turn {@{a type into a value}@} by providing {@{a trait and concrete instances}@}. They enable {@{_ad‑hoc polymorphism_}@}: {@{different implementations}@} for {@{different types}@}.

{@{Other languages}@} adopt {@{similar concepts}@}: {@{Haskell}@}'s {@{built‑in type classes}@}, {@{Rust}@}'s {@{traits}@}, and {@{emerging features}@} in {@{Agda, Lean, and OCaml}@}. In {@{Scala}@} {@{the mechanism is realized}@} through {@{contextual parameters (`using`) and implicit resolution}@}, giving programmers {@{fine‑grained control over polymorphic behaviour}@}.

### type class pattern

To {@{declare a "type class"}@} in Scala, use {@{`trait`}@}:

> [!example] __type class definition__
>
> To {@{declare a "type class"}@} in Scala, use {@{`trait`}@}:
>
> ```Scala
> trait Ordering[A]:
>   def compare(x: A, y: A): Int
> ```

{@{A `given` instance}@} supplies {@{the implementation for a concrete type}@}:

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

With {@{such `given` instances}@} in scope {@{a polymorphic method}@} can be written:

> [!example] __type class implementation__
>
> With {@{such `given` instances}@} in scope {@{a polymorphic method}@} can be written:
>
> ```Scala
> def sort[A](xs: List[A])(using ord: Ordering[A]): List[A] =
>   xs.sorted // uses `ord` for comparison
> ```
>
> {@{The compiler}@} resolves {@{the appropriate `Ordering[A]` at compile time}@}.

### retroactive extension

{@{A type class}@} can be {@{implemented for a data type}@} without {@{modifying its definition}@}. For example, {@{a rational number type}@}:

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
> Now {@{`Rational` values}@} can be {@{sorted or compared using the same generic machinery \(e.g. `sort`\)}@}. Note {@{the definition of `Rational`}@} does not {@{need to be modified}@}.

### extension methods

{@{A type‑class trait}@} may declare {@{_extension methods_}@} that become {@{available when an instance is in scope}@}:

> [!example] __type class extension methods__
>
> {@{A type‑class trait}@} may declare {@{_extension methods_}@} that become {@{available when an instance is in scope}@}:
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

With {@{an `Ordering[T]` in scope}@} one can {@{write}@}:

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
> No {@{explicit import of the instance `Ordering[T]`}@} is {@{required}@}; {@{the extension method `<`}@} is resolved {@{via the implicit `Ordering[T]`}@}.

### type class in other languages

{@{Haskell}@} treats {@{type classes}@} as {@{a first‑class feature of the language}@}.  {@{The standard library}@} defines {@{an `Ordering` data type}@} ({@{`data Ordering = LT | EQ | GT`}@}) and declares {@{the class}@}

> [!example] __type class in Haskell__
>
> {@{The standard library}@} defines {@{an `Ordering` data type}@} ({@{`data Ordering = LT | EQ | GT`}@}) and declares {@{the class}@}
>
> ```Haskell
> class Ord a where
>     compare :: a -> a -> Int
> ```
>
> {@{`class Ord`}@} specifies {@{how values of any type `a` can be compared}@}.

{@{`class Ord`}@} specifies {@{how values of any type `a` can be compared}@}. Because {@{the mechanism is built‑in}@}, Haskell's {@{type‑class system}@} is {@{simpler to reason about}@} than Scala's {@{more general contextual parameters}@}.

{@{Modern systems such as Rust}@} have adopted {@{an analogous construct}@}: the language offers {@{_traits_}@}, which are {@{essentially type classes}@}. {@{A typical Rust trait}@} that {@{mirrors `Ord`}@} looks like:

> [!example] __type class in Rust__
>
> {@{A typical Rust trait}@} that {@{mirrors `Ord`}@} looks like:
>
> ```Rust
> pub trait Ord: Eq + PartialOrd {
>     fn cmp(&self, other: &Self) -> Ordering;
> }
> ```

{@{The syntax in Rust}@} is {@{slightly different}@} but {@{the concept}@} remains {@{the same}@}—defining {@{a set of operations}@} that can be {@{implemented for many distinct types}@}.

{@{Other functional and dependently‑typed languages}@} are moving {@{toward a similar approach}@}.  {@{Agda, Lean, and soon OCaml}@} provide {@{general _contextual parameters_ or equivalent mechanisms}@} that allow {@{programmers to encode type‑class‑like behaviour}@} in a manner analogous to {@{Scala's `given` instances}@}.  {@{These systems}@} combine the expressiveness of {@{Haskell's type classes with Scala‑style contextual resolution}@}, enabling {@{conditional polymorphism across a wide range of types}@}.
