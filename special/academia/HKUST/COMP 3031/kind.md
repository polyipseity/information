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

In Scala 3, {@{a _higher‑kinded type_}@} is written {@{`F[_]`}@} and represents {@{a constructor that expects one type argument}@}. It lets {@{a function be polymorphic over any container}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

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
<!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

## type functions

Scala 3 also supports {@{_type functions_}@} written as {@{`[X] =>> ...`}@}. They are equivalent to {@{a type alias with type parameters of its own}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __type functions__
>
> Scala 3 also supports {@{_type functions_}@} written as {@{`[X] =>> ...`}@}. They are equivalent to {@{a type alias with type parameters of its own}@}:
>
> ```Scala
> foo[[X] =>> (X, X), Int](x => (x, x), 1)         // (1, 1) : (Int, Int)
> type G[X] = (X, X); foo[G, Int](x => (x, x), 1)  // (1, 1) : (Int, Int)
> ```
<!--SR:!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,290-->

Intuitively, {@{a type function}@} is like {@{an ordinary function}@}, but accepts {@{types as arguments and output a type}@}. <!--SR:!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,290-->

## monad example

{@{A lawful monad}@} must satisfy {@{three laws: left unit, right unit, essential-associativity}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->

- _left unit_: ::@:: `M.unit(x).flatMap(f) == f(x)` <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->
- _right unit_: ::@:: `m.flatMap(M.unit) == m` <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->
- _essential-associativity_: ::@:: `m.flatMap(f).flatMap(g) == m.flatMap(x => f(x).flatMap(g))` <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->

{@{These laws}@} guarantee that the generic `reduce` {@{behaves consistently when instantiated with a monoid}@}. Because {@{a monad}@} is {@{a property of a _type constructor_ (`F[_]`) rather than a plain type}@}, it is expressed as {@{a higher‑kinded type class}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

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
> {@{`unit`}@} {@{injects a value}@}, {@{`flatMap`}@} {@{chains computations}@}, and {@{`map`}@} is {@{derived from `flatMap`}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{A concrete instance of `Monad`, `ListMonad`}@}, shows how {@{the abstraction works}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->

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
> Because {@{`List` already implements `flatMap`}@}, the instance is {@{trivial to implement}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

Thus {@{the `Monad` type class}@} captures the semantics of both {@{constructing a singleton `List` and `flatMap` a `List`}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->

### monad example motivation

{@{The advantage of monad being a type class}@} is that we can define {@{very abstract and generic operations that work for all monadic structures}@}. For example, we can define {@{`sequence`}@}, a function that converts {@{a `List[F[A]]` into `F[List[A]]`}@} for some {@{monad type constructor  `F[_]`}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

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
<!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{Example uses of `sequence`}@} assuming {@{a `Monad[Option]` instance}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __`sequence` examples__
>
> {@{Example uses of `sequence`}@} assuming {@{a `Monad[Option]` instance}@}:
>
> ```Scala
> sequence(List(Some(1), Some(2), Some(3)))  // == Some(List(1, 2, 3))
> sequence(List(Some(1), None,    Some(3)))  // == None
> ```
<!--SR:!2025-12-25,4,270!2025-12-25,4,270-->

### monad related kinds

{@{A `Monad`}@} extends {@{the more basic `Applicative`}@}, which itself refines {@{a `Functor`}@}. The hierarchy is: <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

- `Functor[F[_]]` ::@:: defines `map: (F[A], A => B) => F[B]`. <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->
- `Applicative[F[_]]` ::@:: extends `Functor` and adds `pure: A => F[A]` and `ap: (F[A], F[A => B]) => F[B]`; it derives `map` from them. <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->
- `Monad[F[_]]` ::@:: extends `Applicative` and adds `flatMap: (F[A], A => F[B]) => F[B]`. <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->

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
> Intuitively, given {@{a function `T => U` in the original context}@}, `map` applies {@{the same function in the `Functor` context `F[_]`}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

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
> Intuitively, given {@{any type `T` (including function types)}@}, it can be lifted to {@{the `Applicative` context `F[_]`}@}. Recall that {@{`map`}@} applies {@{any given function `T => U` in the `Functor` context `F[_]`}@}, and {@{an alternative way to express this using `Applicative`}@} is to lift {@{the function to the `Applicative` context, and then apply it in said context}@}; hence {@{the need for `ap`}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{`Traverse`}@} extends {@{`Functor`}@}. It can transform {@{a structure of values (`F[A]`, where `F[_]` is the structure)}@} into {@{an effect of structure of new values (`G[F[B]]`, where `G[_]` is the effect and `F[_]` is the structure)}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

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
> {@{Typical `sequence` implementations for other containers}@} follow {@{the same pattern}@}. For example, {@{`sequence` for the structure `List[_]`}@} is a function that converts {@{a `List[F[A]]` into `F[List[A]]`}@} for some {@{applicative type constructor `F[_]`}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{The Cats library (<https://typelevel.org/cats>)}@} supplies {@{many such type classes}@}, allowing {@{concise and generic code across different data types}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

## other languages

{@{Higher‑kinded polymorphism}@} is not common {@{outside of Scala and Haskell}@}. The following snippets illustrate {@{the two main patterns used in other mainstream languages}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{In _Haskell_}@} a {@{_type class_}@} is declared with {@{`class`}@}. {@{The standard monad abstraction}@} is: <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

> [!example] __Haskell monad__
>
> {@{In _Haskell_}@} a {@{_type class_}@} is declared with {@{`class`}@}. {@{The standard monad abstraction}@} is:
>
> ```haskell
> class Monad m where
>   bind :: m a -> (a -> m b) -> m b
>   return :: a -> m a
> ```
<!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{`m`}@} is {@{a type constructor of kind `* → *`}@}; {@{the two methods}@} capture {@{the same laws that Scala’s `Monad[F[_]]` encodes}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{In _OCaml_}@} there are {@{no first‑class type classes}@}, but {@{the same idea can be encoded with modules}@}: <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

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
<!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{The signature}@} is {@{a _module type_}@}; {@{concrete modules}@} can be passed as {@{arguments to functions that need monadic behaviour}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{Other ecosystems}@} (e.g. {@{Rust}@} with {@{the `Monad` trait in libraries}@}, or {@{Kotlin’s}@} {@{`Arrow`}@}) follow {@{similar patterns}@}, but {@{Scala and Haskell}@} remain {@{the most idiomatic for higher‑kinded abstractions}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->
