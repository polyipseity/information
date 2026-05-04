---
aliases:
  - COMP 3031 Scala kind
  - COMP 3031 Scala kinds
  - COMP3031 Scala kind
  - COMP3031 Scala kinds
  - HKUST COMP 3031 Scala kind
  - HKUST COMP 3031 Scala kinds
  - HKUST COMP3031 Scala kind
  - HKUST COMP3031 Scala kinds
  - Scala kind
  - Scala kinds
tags:
  - flashcard/active/special/academia/HKUST/COMP_3031/kind
  - language/in/English
---

# Scala kind

- HKUST COMP 3031

---

- see: [general/kind (type theory)](../../../../general/kind%20(type%20theory).md)

In Scala 3, {@{a _higher‑kinded type_}@} is written {@{`F[_]`}@} and represents {@{a constructor that expects one type argument}@}. It lets {@{a function be polymorphic over any container}@}: <!--SR:!2026-12-25,272,330!2026-12-13,262,330!2026-12-11,260,330!2027-01-12,286,330-->

> [!example] __generic foo__
>
> {@{A _higher‑kinded type_}@} lets {@{a function be polymorphic over any container}@}:
>
> ```Scala
> def foo[F[_], X](f: X => F[X], x: X): F[X] = f(x)
> ```
>
> {@{Calling `foo`}@} with {@{concrete constructors}@}
>
> ```Scala
> foo[List, Int](_ :: Nil, 1)          // List(1)
> foo[Option, String](Some(_), "fuel") // Option("fuel")
> ```
<!--SR:!2026-11-16,246,330!2026-11-26,254,330!2027-01-22,289,330!2026-09-09,181,310-->

## type functions

Scala 3 also supports {@{_type functions_}@} written as {@{`[X] =>> ...`}@}. They are equivalent to {@{a type alias with type parameters of its own}@}: <!--SR:!2027-01-05,281,330!2027-01-25,294,330!2027-01-20,287,330-->

> [!example] __type functions__
>
> Scala 3 also supports {@{_type functions_}@} written as {@{`[X] =>> ...`}@}. They are equivalent to {@{a type alias with type parameters of its own}@}:
>
> ```Scala
> foo[[X] =>> (X, X), Int](x => (x, x), 1)         // (1, 1) : (Int, Int)
> type G[X] = (X, X); foo[G, Int](x => (x, x), 1)  // (1, 1) : (Int, Int)
> ```
<!--SR:!2027-03-30,339,350!2027-04-05,345,350!2027-04-08,348,350-->

Intuitively, {@{a type function}@} is like {@{an ordinary function}@}, but accepts {@{types as arguments and output a type}@}. <!--SR:!2027-04-06,346,350!2027-03-01,327,350!2027-03-29,338,350-->

## monad example

{@{A lawful monad}@} must satisfy {@{three laws: left unit, right unit, essential-associativity}@}. <!--SR:!2026-12-30,276,330!2026-11-14,244,330-->

- _left unit_: ::@:: `M.unit(x).flatMap(f) == f(x)` <!--SR:!2026-12-06,256,330!2026-11-16,246,330-->
- _right unit_: ::@:: `m.flatMap(M.unit) == m` <!--SR:!2026-11-02,234,330!2026-11-10,241,330-->
- _essential-associativity_: ::@:: `m.flatMap(f).flatMap(g) == m.flatMap(x => f(x).flatMap(g))` <!--SR:!2026-09-12,184,310!2026-10-23,204,310-->

{@{These laws}@} guarantee that the generic `reduce` {@{behaves consistently when instantiated with a monoid}@}. Because {@{a monad}@} is {@{a property of a _type constructor_ (`F[_]`) rather than a plain type}@}, it is expressed as {@{a higher‑kinded type class}@}: <!--SR:!2027-01-11,285,330!2026-10-30,231,330!2026-12-14,263,330!2027-01-07,282,330!2026-12-25,272,330-->

> [!example] __monad trait__
>
> {@{The `Monad` trait}@} may be defined using {@{a higher-kinded type parameter `F[_]`}@}:
>
> ```Scala
> trait Monad[F[_]]:
>   def unit[T](x: T): F[T]
>   extension [T](x: F[T]):
>     def flatMap[U](f: T => F[U]): F[U]
>     def map[U](f: T => U): F[U] = flatMap(f andThen unit)
> ```
>
> {@{`unit`}@} {@{injects a value}@}, {@{`flatMap`}@} {@{chains computations}@}, and {@{`map`}@} is {@{derived from `flatMap`}@}. <!--SR:!2027-01-14,288,330!2026-11-16,246,330!2026-11-06,237,330!2026-12-24,271,330!2026-11-16,246,330!2026-12-16,264,330!2026-11-27,255,330!2026-12-04,255,330-->

{@{A concrete instance of `Monad`, `ListMonad`}@}, shows how {@{the abstraction works}@}: <!--SR:!2026-10-18,199,310!2027-01-10,285,330-->

> [!example] __list monad__
>
> {@{A concrete instance of `Monad`, `ListMonad`}@}, shows how {@{the abstraction works}@}:
>
> ```Scala
> given ListMonad: Monad[List] with
>   def unit[T](x: T): List[T] = x :: Nil
>   extension [T](x: List[T]):
>     def flatMap[U](f: T => List[U]): List[U] = x.flatMap(f)
> ```
>
> Because {@{`List` already implements `flatMap`}@}, the instance is {@{trivial to implement}@}. <!--SR:!2026-11-27,255,330!2026-11-10,241,330!2026-12-28,269,330!2026-10-26,207,310-->

Thus {@{the `Monad` type class}@} captures the semantics of both {@{constructing a singleton `List` and `flatMap` a `List`}@}. <!--SR:!2026-12-09,259,330!2026-11-10,241,330-->

### monad example motivation

{@{The advantage of monad being a type class}@} is that we can define {@{very abstract and generic operations that work for all monadic structures}@}. For example, we can define {@{`sequence`}@}, a function that converts {@{a `List[F[A]]` into `F[List[A]]`}@} for some {@{monad type constructor  `F[_]`}@}: <!--SR:!2026-12-12,261,330!2026-10-27,228,330!2026-12-20,268,330!2026-11-05,237,330!2026-12-09,259,330-->

> [!example] __`sequence`__
>
> For example, we can define {@{`sequence`}@}, a function that converts {@{a `List[F[A]]` into `F[List[A]]`}@} for some {@{monad type constructor  `F[_]`}@}:
>
> ```Scala
> def sequence[F[_]: Monad, A](as: List[F[A]]): F[List[A]] =
>   as match
>     case Nil => summon[Monad[F]].unit(Nil)
>     case fa :: fas =>
>       for (a <- fa; as <- sequence(fas)) yield a :: as
> ```
<!--SR:!2026-12-08,258,330!2026-11-19,248,330!2026-11-25,253,330-->

{@{Example uses of `sequence`}@} assuming {@{a `Monad[Option]` instance}@}: <!--SR:!2026-10-24,205,310!2026-11-24,252,330-->

> [!example] __`sequence` examples__
>
> {@{Example uses of `sequence`}@} assuming {@{a `Monad[Option]` instance}@}:
>
> ```Scala
> sequence(List(Some(1), Some(2), Some(3)))  // == Some(List(1, 2, 3))
> sequence(List(Some(1), None,    Some(3)))  // == None
> ```
<!--SR:!2026-12-30,276,330!2026-12-14,263,330-->

### monad related kinds

{@{A `Monad`}@} extends {@{the more basic `Applicative`}@}, which itself refines {@{a `Functor`}@}. The hierarchy is: <!--SR:!2026-12-22,269,330!2026-11-29,251,330!2026-12-08,258,330-->

- `Functor[F[_]]` ::@:: defines `map: (F[A], A => B) => F[B]`. <!--SR:!2027-01-01,277,330!2026-11-15,245,330-->
- `Applicative[F[_]]` ::@:: extends `Functor` and adds `pure: A => F[A]` and `ap: (F[A], F[A => B]) => F[B]`; it derives `map` from them. <!--SR:!2026-07-31,135,290!2026-11-23,251,330-->
- `Monad[F[_]]` ::@:: extends `Applicative` and adds `flatMap: (F[A], A => F[B]) => F[B]`. <!--SR:!2026-09-06,174,310!2026-11-10,241,330-->

> [!example] __`Functor` trait__
>
> {@{`Functor[F[_]]`}@} defines {@{`map: (F[A], A => B) => F[B]`}@}.
>
> ```Scala
> trait Functor[F[_]]:
>   extension [T](x: F[T])
>     def map[U](f: T => U): F[U]
> ```
>
> Intuitively, given {@{a function `T => U` in the original context}@}, `map` applies {@{the same function in the `Functor` context `F[_]`}@}. <!--SR:!2026-12-20,268,330!2026-10-22,203,310!2026-12-30,276,330!2026-11-13,243,330-->

<!-- markdownlint MD028 -->

> [!example] __`Applicative` trait__
>
> {@{`Applicative[F[_]]`}@} extends {@{`Functor` and adds `pure: A => F[A]` and `ap: (F[A], F[A => B]) => F[B]`}@}; it derives {@{`map` from them}@}.
>
> ```Scala
> trait Applicative[F[_]] extends Functor[F]:
>   def pure[A](a: A): F[A]
>   extension [A](x: F[A]):
>     def ap[B](f: F[A => B]): F[B]
>     def map[B](f: A => B): F[B] = ap(pure(f))(fa)
> ```
>
> Intuitively, given {@{any type `T` (including function types)}@}, it can be lifted to {@{the `Applicative` context `F[_]`}@}. Recall that {@{`map`}@} applies {@{any given function `T => U` in the `Functor` context `F[_]`}@}, and {@{an alternative way to express this using `Applicative`}@} is to lift {@{the function to the `Applicative` context, and then apply it in said context}@}; hence {@{the need for `ap`}@}. <!--SR:!2027-01-22,291,330!2026-11-16,246,330!2026-09-04,177,310!2026-12-18,266,330!2026-12-28,274,330!2027-01-21,288,330!2027-01-13,287,330!2026-12-07,257,330!2026-09-22,182,310!2026-11-03,235,330-->

{@{`Traverse`}@} extends {@{`Functor`}@}. It can transform {@{a structure of values (`F[A]`, where `F[_]` is the structure)}@} into {@{an effect of structure of new values (`G[F[B]]`, where `G[_]` is the effect and `F[_]` is the structure)}@}: <!--SR:!2027-01-10,285,330!2027-01-18,285,330!2026-09-07,175,310!2026-12-23,270,330-->

> [!example] __traverse__
>
> {@{`Traverse`}@} extends {@{`Functor`}@}. It can transform {@{a structure of values (`F[A]`, where `F[_]` is the structure)}@} into {@{an effect of structure of new values (`G[F[B]]`, where `G[_]` is the effect and `F[_]` is the structure)}@}:
>
> ```Scala
> trait Traverse[F[_]] extends Functor[F]:
>   def traverse[G[_]: Applicative, A, B](fa: F[A])(f: A => G[B]): G[F[B]]
>   // derived: a structure of effects on values into an effect of structure of values
>   def sequence[G[_]: Applicative, A](fga: F[G[A]]): G[F[A]] = traverse(fga)(id)
> ```
>
> {@{Typical `sequence` implementations for other containers}@} follow {@{the same pattern}@}. For example, {@{`sequence` for the structure `List[_]`}@} is a function that converts {@{a `List[F[A]]` into `F[List[A]]`}@} for some {@{applicative type constructor `F[_]`}@}. <!--SR:!2026-12-21,268,330!2026-12-15,263,330!2026-09-28,193,310!2026-12-19,267,330!2027-01-10,285,330!2026-11-20,249,330!2026-11-24,252,330!2026-08-01,156,310!2027-01-05,276,330-->

{@{The Cats library (<https://typelevel.org/cats>)}@} supplies {@{many such type classes}@}, allowing {@{concise and generic code across different data types}@}. <!--SR:!2026-10-12,193,310!2026-12-20,263,330!2026-12-25,272,330-->

## other languages

{@{Higher‑kinded polymorphism}@} is not common {@{outside of Scala and Haskell}@}. The following snippets illustrate {@{the two main patterns used in other mainstream languages}@}. <!--SR:!2026-10-25,206,310!2026-12-12,256,330!2026-11-10,241,330-->

{@{In _Haskell_}@} a {@{_type class_}@} is declared with {@{`class`}@}. {@{The standard monad abstraction}@} is: <!--SR:!2026-11-01,233,330!2026-11-10,241,330!2027-01-03,279,330!2026-11-18,247,330-->

> [!example] __Haskell monad__
>
> {@{In _Haskell_}@} a {@{_type class_}@} is declared with {@{`class`}@}. {@{The standard monad abstraction}@} is:
>
> ```haskell
> class Monad m where
>   bind :: m a -> (a -> m b) -> m b
>   return :: a -> m a
> ```
<!--SR:!2026-12-30,276,330!2026-12-14,263,330!2027-01-04,280,330!2026-12-30,276,330-->

{@{`m`}@} is {@{a type constructor of kind `* → *`}@}; {@{the two methods}@} capture {@{the same laws that Scala’s `Monad[F[_]]` encodes}@}. <!--SR:!2026-10-23,204,310!2026-10-29,230,330!2027-01-27,294,330!2027-01-15,289,330-->

{@{In _OCaml_}@} there are {@{no first‑class type classes}@}, but {@{the same idea can be encoded with modules}@}: <!--SR:!2027-01-26,293,330!2027-01-16,290,330!2026-12-17,265,330-->

> [!example] __OCaml monad module__
>
> {@{In _OCaml_}@} there are {@{no first‑class type classes}@}, but {@{the same idea can be encoded with modules}@}:
>
> ```ocaml
> module type Monad = sig
>   type 'a t
>   val bind : 'a t -> ('a -> 'b t) -> 'b t
>   val return : 'a -> 'a t
> end
> ```
<!--SR:!2026-12-10,259,330!2026-11-17,246,330!2027-01-23,292,330-->

{@{The signature}@} is {@{a _module type_}@}; {@{concrete modules}@} can be passed as {@{arguments to functions that need monadic behaviour}@}. <!--SR:!2027-01-05,281,330!2027-01-10,285,330!2026-11-23,251,330!2027-01-19,286,330-->

{@{Other ecosystems}@} (e.g. {@{Rust}@} with {@{the `Monad` trait in libraries}@}, or {@{Kotlin’s}@} {@{`Arrow`}@}) follow {@{similar patterns}@}, but {@{Scala and Haskell}@} remain {@{the most idiomatic for higher‑kinded abstractions}@}. <!--SR:!2026-11-10,241,330!2026-10-31,232,330!2026-12-10,255,330!2027-01-10,285,330!2026-12-09,259,330!2026-10-28,229,330!2026-11-21,250,330!2026-11-16,245,330-->
