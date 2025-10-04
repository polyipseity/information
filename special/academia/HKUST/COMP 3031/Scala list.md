---
aliases:
  - COMP 3031 Scala list
  - COMP 3031 Scala lists
  - COMP3031 Scala list
  - COMP3031 Scala lists
  - HKUST COMP 3031 Scala list
  - HKUST COMP 3031 Scala lists
  - HKUST COMP3031 Scala list
  - HKUST COMP3031 Scala lists
  - Scala list
  - Scala lists
tags:
  - flashcard/active/special/academia/HKUST/COMP_3031/Scala_list
  - language/in/English
---

# Scala list

- HKUST COMP 3031

In Scala {@{a __list__}@} is {@{the canonical immutable linear data structure}@} used {@{throughout functional programming}@}. A list {@{containing the elements _x₁, …, xₙ_}@} is written {@{`List(x₁, …, xₙ)`}@}. Typical examples include

> [!example] __example__
>
> A list {@{containing the elements _x₁, …, xₙ_}@} is written {@{`List(x₁, …, xₙ)`}@}. Typical examples include
>
> ```Scala
> val fruits = List("apples", "oranges", "pears")
> val nums   = List(1, 2, 3, 4)
> val diag3  = List(List(1,0,0), List(0,1,0), List(0,0,1))
> val empty  = List()
> ```

Unlike {@{arrays}@}, lists are {@{__immutable__}@}—once constructed {@{their contents cannot be altered}@}—and they are inherently {@{__recursive__}@}; {@{each element is prepended}@} to a list by storing {@{the element and the remaining of the list as another list}@}. Lists are also {@{__homogeneous__}@}: all elements must {@{share the same type _T_}@}, so {@{a list of integers}@} is written {@{`List[Int]`}@} and its type annotation can be {@{omitted when inferred}@}.

{@{Every list}@} in Scala is {@{built from two primitives}@}. {@{The empty list}@} is denoted by {@{the constant `Nil`}@}, while {@{the cons operator `::`}@} constructs {@{a new list by prepending an element to an existing one (`x :: xs`)}@}. Because {@{operators ending with a colon}@} {@{associate to the right}@}, {@{a sequence of cons operations}@} can be {@{written without parentheses}@}:

> [!example] __example__
>
> Because {@{operators ending with a colon}@} {@{associate to the right}@}, {@{a sequence of cons operations}@} can be {@{written without parentheses}@}:
>
> ```Scala
> val nums = 1 :: 2 :: 3 :: 4 :: Nil
> ```

{@{This right associativity}@} means {@{`A :: B :: C`}@} is parsed as {@{`A :: (B :: C)`}@}.

{@{The basic list API}@} exposes {@{three core methods}@}:

- `head`, ::@:: which returns the first element;
- `tail`, ::@:: which yields a new list containing all elements except the head;
- `isEmpty`, ::@:: which reports whether the list contains no elements.

{@{These operations}@} are defined as {@{methods on any instance of `List`}@}. For example, {@{`fruits.head` \(`fruits` is nonempty\)}@} evaluates to {@{its first element}@}, whereas calling {@{`Nil.head` throws a `NoSuchElementException`}@}.

Pattern matching works {@{seamlessly with lists}@}. {@{The constant `Nil`}@} matches {@{an empty list}@}; {@{the pattern `p :: ps`}@} matches {@{a non‑empty list}@} whose first element {@{satisfies pattern `p` and whose remainder satisfies pattern `ps`}@}. {@{A shorthand}@} for {@{a concrete list of length _n_}@} is {@{`List(p₁, …, pₙ)`}@}, which expands to {@{nested conses ending in `Nil`}@}. For instance, {@{the pattern `1 :: 2 :: xs`}@} matches {@{any list that begins with `1` followed by `2`}@}, while {@{`x :: Nil`}@} matches {@{a singleton list}@}. {@{More elaborate patterns}@} such as {@{`x :: y :: List(xs, ys) :: zs`}@} illustrate {@{nested matching}@}.

Overall, lists provide {@{a simple yet powerful abstraction}@} for {@{ordered collections}@}: they are {@{immutable, recursively defined, and naturally suited to pattern matching}@}, making them {@{a staple of functional Scala code}@}.

## covariance

Scala's {@{immutable `List`}@} is {@{covariant}@}. This means that {@{`List[A]` is a subtype of `List[B]`}@} whenever {@{`A` is a subtype of `B`}@}. Covariance is denoted by {@{the `+` symbol in the type parameter}@}: {@{`List[+T]`}@}.

By declaring it {@{covariant (`sealed abstract class List[+T]`)}@} we allow {@{`Nil`}@} to be represented as {@{a singleton object of type `List[Nothing]`}@}, which is {@{a subtype of any `List[T]`}@}.

However, adding {@{a method that "mutates" \(no actual mutation occurs\) the list (e.g. `prepend(elem: T): List[T]`)}@} {@{breaks covariance}@} because it {@{accepts an argument of type `T`—an input position for a covariant parameter}@}. To restore {@{variance correctness}@} we can use {@{a lower bound on the method’s parameter}@}:

> [!example] __example__
>
> To restore {@{variance correctness}@} we can use {@{a lower bound on the method's parameter}@}:
>
> ```Scala
> trait List[+T]:
>   def prepend[U >: T](elem: U): List[U] = Cons(elem, this)
> ```

This is okay because {@{covariant parameters}@} can be used in {@{lower bounds of method type parameters}@}. The same holds for {@{upper bounds of method type parameters}@} and {@{contravariant parameters}@}. Now `prepend` accepts {@{any supertype of `T`}@}, producing a list whose {@{element type is that supertype}@}. For example, calling {@{`xs.prepend(orange)` on a `List[Apple]` \(where `Apple` and `Orange` are _direct_ subclasses of `Fruit`\)}@} yields {@{a `List[Fruit]`}@}.

An alternative to {@{adding a method type parameter}@} is to {@{use extension methods (available in Scala 3)}@}. By defining {@{an extension method for the element type rather than the list itself}@}, we sidestep {@{variance violations}@}:

> [!example] __example__
>
> An alternative to {@{adding a method type parameter}@} is to {@{use extension methods (available in Scala 3)}@}. By defining {@{an extension method for the element type rather than the list itself}@}, we sidestep {@{variance violations}@}:
>
> ```Scala
> extension [T](x: T)
>   def ::(xs: List[T]): List[T] = Cons(x, xs)
> ```
>
> This approach does not require {@{adding a method type parameter}@} and allows {@{natural list construction syntax (`1 :: 2 :: Nil`)}@}.

## methods

Lists are {@{the fundamental data structure}@} that will {@{recur throughout the course}@}. In Scala a list is {@{an immutable linked‑list whose type carries the element type}@}: {@{`List[Fruit]`}@}. A list can be constructed in {@{two idiomatic ways}@}: using {@{the factory method `List.apply`}@}, which accepts {@{zero or more arguments}@}, or by prepending {@{elements to the sentinel value `Nil` with the cons operator (`::`)}@}. For example:

> [!example] __example__
>
> A list can be constructed in {@{two idiomatic ways}@}: using {@{the factory method `List.apply`}@}, which accepts {@{zero or more arguments}@}, or by prepending {@{elements to the sentinel value `Nil` with the cons operator (`::`)}@}. For example:
>
> ```Scala
> val fruits = List("Apple", "Orange", "Banana")
> val nums   = 1 :: 2 :: Nil          // equivalent to List(1, 2)
> ```

{@{Decomposition}@} is equally {@{concise}@}. {@{The head of a list}@} is accessed by {@{`.head`}@}, {@{the tail by `.tail`}@}, and {@{pattern matching}@} can be used to {@{deconstruct lists directly}@}:

> [!example] __example__
>
> {@{Decomposition}@} is equally {@{concise}@}. {@{The head of a list}@} is accessed by {@{`.head`}@}, {@{the tail by `.tail`}@}, and {@{pattern matching}@} can be used to {@{deconstruct lists directly}@}:
>
> ```Scala
> val fruits = List("Apple", "Orange", "Banana")
> val nums   = 1 :: 2 :: Nil          // equivalent to List(1, 2)
>
> fruits.head      // "Apple"
> nums.tail        // 2 :: Nil
> nums.isEmpty     // false
>
> nums match {
>   case x :: y :: _ => x + y   // 3
> }
> ```

The `List` API offers {@{a rich set of operations}@} for {@{sublists, element access, and construction}@}. Methods such as {@{`.length`, `.take(n)`, `.drop(n)`}@}, {@{`.last`, `.init` and the indexer `xs(n)`}@} provide {@{standard functional list manipulation}@}. {@{The last three}@} are {@{_partial_ methods}@} because they {@{throw exceptions on empty lists or out‑of‑range indices}@}; consequently it is preferable to {@{use safer alternatives whenever possible}@}.

{@{Additional constructors}@} include {@{concatenation (`xs ::: ys`), reversal (`xs.reverse`) and update (`xs.updated(n, x)`)}@}. {@{Element search}@} is supported by {@{`.indexOf(x)` and `.contains(x)`}@}.

{@{The implementation of `last` and `init`}@}, for instance, is {@{linear in the length of the list}@} because it must {@{traverse all elements to reach the tail}@}.

> [!example] __example__
>
> {@{The implementation of `last` and `init`}@}, for instance, is {@{linear in the length of the list}@} because it must {@{traverse all elements to reach the tail}@}:
>
> ```Scala
> def last[T](xs: List[T]): T = xs match {
>   case Nil          => throw new NoSuchElementException("last of empty list")
>   case x :: Nil     => x
>   case _ :: ys      => last(ys)
> }
> ```
>
> ```Scala
> def init[T](xs: List[T]): List[T] = xs match {
>   case Nil          => throw new NoSuchElementException("init of empty list")
>   case _ :: Nil     => Nil
>   case y :: ys      => y :: init(ys)
> }
> ```

{@{The concatenation operator `:::`}@} can be implemented by {@{pattern matching on the left operand}@}. This recursive definition runs in time {@{proportional to the length of the left list, `O(xs.length)`}@}.

> [!example] __example__
>
> {@{The concatenation operator `:::`}@} can be implemented by {@{pattern matching on the left operand}@}. This recursive definition runs in time {@{proportional to the length of the left list, `O(xs.length)`}@}.
>
> ```Scala
> extension [T](xs: List[T])
>   def ::: (ys: List[T]): List[T] = xs match {
>     case Nil        => ys
>     case x :: xs1   => x :: xs1 ::: ys
>   }
> ```

{@{Reversal}@} can be _naively_ written by {@{recursively reversing the tail and appending the head}@}:

> [!example] __example__
>
> {@{Reversal}@} can be _naively_ written by {@{recursively reversing the tail and appending the head}@}:
>
> ```Scala
> extension [T](xs: List[T])
>   def reverse: List[T] = xs match {
>     case Nil        => Nil
>     case y :: ys    => ys.reverse ::: (y :: Nil)
>   }
> ```

Because {@{each recursive call}@} concatenates {@{a singleton list to the result of reversing the tail}@}, the complexity is {@{quadratic, `O(xs.length²)`}@}. {@{A linear‑time implementation}@} would use {@{an accumulator}@}.

{@{Removing the _n_-th element}@} can be defined by {@{pattern matching on the index}@}:

> [!example] __example__
>
> {@{Removing the _n_-th element}@} can be defined by {@{pattern matching on the index}@}:
>
> ```Scala
> def removeAt[T](n: Int, xs: List[T]): List[T] = xs match {
>   case Nil          => Nil
>   case y :: ys =>
>     if (n == 0) ys else y :: removeAt(n - 1, ys)
> }
> ```

{@{A "deep" flattening routine}@} demonstrates {@{recursion over heterogeneous structures}@}:

> [!example] __example__
>
> {@{A "deep" flattening routine}@} demonstrates {@{recursion over heterogeneous structures}@}:
>
> ```Scala
> def deepFlatten(xs: Any): List[Any] = xs match {
>   case Nil          => Nil
>   case y :: ys      => deepFlatten(y) ::: deepFlatten(ys)
>   case nonList      => nonList :: Nil
> }
> ```
>
> Calling `deepFlatten(List(List(1, 1), 2, List(3, List(5, 8))))` yields {@{`List(1, 1, 2, 3, 5, 8)`}@}.

## higher-order methods

{@{Typical list algorithms}@} fall into {@{three broad categories}@}: \(annotation: 3 items: {@{map, filter, reduce/fold}@}\)

- __Mapping__ ::@:: – transform every element in a list.
- __Filtering__ ::@:: – extract all elements that satisfy a predicate.
- __Reduction / Folding__ ::@:: – combine the elements of a list with an associative operator.

### map

{@{A generic `map`}@} applies {@{a function to each element of the list}@}:

> [!example] __example__
>
> {@{A generic `map`}@} applies {@{a function to each element of the list}@}:
>
> ```Scala
> extension [T](xs: List[T])
>   def map[U](f: T => U): List[U] =
>     xs match
>       case Nil          => Nil
>       case x :: xs     => f(x) :: xs.map(f)
> ```

Using {@{`map`}@}, {@{a simple scaling routine}@} can be written as:

> [!example] __example__
>
> Using {@{`map`}@}, {@{a simple scaling routine}@} can be written as:
>
> ```Scala
> def scaleList(xs: List[Double], factor: Double) =
>   xs.map(x => x * factor)
> ```

### filter

{@{Filtering \(`filter`\)}@} extracts {@{elements that satisfy a Boolean predicate}@}:

> [!example] __example__
>
> {@{Filtering \(`filter`\)}@} extracts {@{elements that satisfy a Boolean predicate}@}:
>
> ```Scala
> extension [T](xs: List[T])
>   def filter(p: T => Boolean): List[T] =
>     xs match
>       case Nil          => Nil
>       case x :: xs     =>
>         if p(x) then x :: xs.filter(p)
>         else       xs.filter(p)
> ```

{@{The `posElems`}@} example becomes, using {@{`filter`}@}:

> [!example] __example__
>
> {@{The `posElems`}@} example becomes, using {@{`filter`}@}:
>
> ```Scala
> def posElems(xs: List[Int]): List[Int] =
>   xs.filter(x => x > 0)
> ```

{@{Other useful filter-like operations}@} are built from `filter`, such as {@{`filterNot`, `partition`, `takeWhile`, `dropWhile`, and `span`}@}.  Each of these performs {@{a single traversal}@} while producing {@{different views of the original list}@}.

### pack

{@{The _pack_ function}@} groups {@{consecutive duplicate elements into sublists}@}:

> [!example] __example__
>
> {@{The _pack_ function}@} groups {@{consecutive duplicate elements into sublists}@}:
>
> ```Scala
> def pack[T](xs: List[T]): List[::[T]] =
>   xs match
>     case Nil          => Nil
>     case x :: xs1 =>
>       val (more, rest) = xs1.span(y => y == x)
>       (new ::(x, more)) :: pack(rest)
> ```

In {@{the return type of `pack`}@}, {@{`::[T]`}@} is used to {@{represent _nonempty_ lists}@}.

Using {@{`pack`}@}, {@{a run‑length encoder \(RLE\)}@} is obtained:

> [!example] __example__
>
> Using {@{`pack`}@}, {@{a run‑length encoder \(RLE\)}@} is obtained:
>
> ```Scala
> def encode[T](xs: List[T]): List[(T, Int)] =
>   pack(xs).map(ys => (ys.head, ys.length))
> ```

As {@{`pack`}@} returns {@{`List[::[T]]` instead of `List[List[T]]`}@}, it is {@{type-safe}@} to {@{call `ys.head`}@}.

### reduce

{@{The generic `reduceLeft`}@} inserts {@{a binary operator between adjacent elements}@} in a {@{left-associative manner}@}:

> [!example] __example__
>
> {@{The generic `reduceLeft`}@} inserts {@{a binary operator between adjacent elements}@} in a {@{left-associative manner}@}:
>
> ```Scala
> List(x1, …, xn).reduceLeft((x, y) => x.op(y))
> ```

Using {@{`reduceLeft`}@}, {@{summation}@} becomes:

> [!example] __example__
>
> Using {@{`reduceLeft`}@}, {@{summation}@} becomes:
>
> ```Scala
> def sum(xs: List[Int]) = (0 :: xs).reduceLeft(_ + _)
> ```

{@{`reduceLeft`}@} does not {@{support empty lists}@}. {@{`foldLeft`}@} generalises `reduceLeft` by {@{supplying an initial accumulator `z`}@} that is {@{used as a starting value, and returned for the empty list}@}:

> [!example] __example__
>
> {@{`reduceLeft`}@} does not {@{support empty lists}@}. {@{`foldLeft`}@} generalises {@{`reduceLeft` by supplying an initial accumulator `z`}@} that is {@{used as a starting value, and returned for the empty list}@}:
>
> ```Scala
> def sum(xs: List[Int]) = xs.foldLeft(0)(_ + _)
> def product(xs: List[Int]) = xs.foldLeft(1)(_ * _)
> ```

{@{`reduceRight` and `foldRight`}@} are {@{the right-associative counterparts}@}:

> [!example] __example__
>
> {@{`reduceRight` and `foldRight`}@} are {@{the right-associative counterparts}@}:
>
> ```Scala
> def concat[T](xs: List[T], ys: List[T]): List[T] =
>   xs.foldRight(ys)(_ :: _)
> ```

{@{Replacing `foldRight` with `foldLeft`}@} would {@{reverse the order of operations}@}. When {@{the operator is associative and commutative}@}, the final result is {@{the same}@}; otherwise, {@{the types or semantics change}@}. {@{`foldRight`}@} also does not {@{work with infinite lists}@}, as there is {@{no rightmost or ending element to start folding}@}.

{@{Both `reduceLeft` and `foldLeft`}@} can be {@{defined directly in the abstract `List` class}@}:

> [!example] __example__
>
> {@{Both `reduceLeft` and `foldLeft`}@} can be {@{defined directly in the abstract `List` class}@}:
>
> ```Scala
> sealed abstract class List[T]:
>   def reduceLeft(op: (T, T) => T): T =
>     this match
>       case Nil          => throw IllegalOperationException("Nil.reduceLeft")
>       case x :: xs     => xs.foldLeft(x)(op)
> 
>   def foldLeft[U](z: U)(op: (U, T) => U): U =
>     this match
>       case Nil          => z
>       case x :: xs     => xs.foldLeft(op(z, x))(op)
> ```

{@{Analogous definitions}@} exist for {@{`reduceRight` and `foldRight`}@}.

For {@{an example of `reduceLeft`}@}, {@{a linear‑time reverse}@} is obtained by {@{folding left with an empty list as the initial value and prepending each element}@}:

> [!example] __example__
>
> For {@{an example of `reduceLeft`}@}, {@{a linear‑time reverse}@} is obtained by {@{folding left with an empty list as the initial value and prepending each element}@}:
>
> ```Scala
> def reverse[T](xs: List[T]): List[T] =
>   xs.foldLeft[List[T]](Nil)((acc, x) => x :: acc)
> ```
