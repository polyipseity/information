---
aliases:
  - COMP 3031 Scala collection
  - COMP 3031 Scala collections
  - COMP3031 Scala collection
  - COMP3031 Scala collections
  - HKUST COMP 3031 Scala collection
  - HKUST COMP 3031 Scala collections
  - HKUST COMP3031 Scala collection
  - HKUST COMP3031 Scala collections
  - Scala collection
  - Scala collections
tags:
  - flashcard/active/special/academia/HKUST/COMP_3031/collections
  - language/in/English
---

# Scala collections

- HKUST COMP 3031

## hierarchy

{@{The type hierarchy}@} for {@{sequential collections}@} is rooted in {@{the abstract class `Seq`}@}, which extends {@{`Iterable`}@}. {@{Concrete subclasses}@} include {@{`List` and `Vector`}@}. {@{The Java‑backed}@} {@{`Array` and `String`}@} are {@{_not_ subclasses of `Seq` \(as they come from Java\)}@}, but they can be {@{converted into `Seq` where needed}@}.

{@{`Set` and `Map`}@} are also {@{subclasses of `Iterable`}@}, but they do not {@{inherit from `Seq`}@}.

## list

In Scala {@{a __list__}@} is {@{the canonical immutable linear data structure}@} used {@{throughout functional programming}@}. A list {@{containing the elements _x₁, ..., xₙ_}@} is written {@{`List(x₁, ..., xₙ)`}@}. Typical examples include

> [!example] __list construction__
>
> A list {@{containing the elements _x₁, ..., xₙ_}@} is written {@{`List(x₁, ..., xₙ)`}@}. Typical examples include
>
> ```Scala
> val fruits = List("apples", "oranges", "pears")
> val nums   = List(1, 2, 3, 4)
> val diag3  = List(List(1,0,0), List(0,1,0), List(0,0,1))
> val empty  = List()
> ```

Unlike {@{arrays}@}, lists are {@{__immutable__}@}—once constructed {@{their contents cannot be altered}@}—and they are inherently {@{__recursive__}@}; {@{each element is prepended}@} to a list by storing {@{the element and the remaining of the list as another list}@}. Lists are also {@{__homogeneous__}@}: all elements must {@{share the same type _T_}@}, so {@{a list of integers}@} is written {@{`List[Int]`}@} and its type annotation can be {@{omitted when inferred}@}.

{@{Every list}@} in Scala is {@{built from two primitives}@}. {@{The empty list}@} is denoted by {@{the constant `Nil`}@}, while {@{the cons operator `::`}@} constructs {@{a new list by prepending an element to an existing one (`x :: xs`)}@}. Because {@{operators ending with a colon}@} {@{associate to the right}@}, {@{a sequence of cons operations}@} can be {@{written without parentheses}@}:

> [!example] __operator associativity__
>
> Because {@{operators ending with a colon}@} {@{associate to the right}@}, {@{a sequence of cons operations}@} can be {@{written without parentheses}@}:
>
> ```Scala
> val nums = 1 :: (2 :: (3 :: (4 :: Nil)))
> val nums = 1 ::  2 ::  3 ::  4 :: Nil     // Equivalent
> ```

{@{This right associativity}@} means {@{`A :: B :: C`}@} is parsed as {@{`A :: (B :: C)`}@}.

{@{The basic list API}@} exposes {@{three core methods}@}: \(annotation: 3 items: {@{`head`, `tail`, `isEmpty`}@}\)

- `head`, ::@:: which returns the first element;
- `tail`, ::@:: which yields a new list containing all elements except the head;
- `isEmpty`, ::@:: which reports whether the list contains no elements.

{@{These operations}@} are defined as {@{methods on any instance of `List`}@}. For example, {@{`fruits.head` \(`fruits` is nonempty\)}@} evaluates to {@{its first element}@}, whereas calling {@{`Nil.head` throws a `NoSuchElementException`}@}.

Pattern matching works {@{seamlessly with lists}@}. {@{The constant `Nil`}@} matches {@{an empty list}@}; {@{the pattern `p :: ps`}@} matches {@{a non‑empty list}@} whose first element {@{satisfies pattern `p` and whose remainder satisfies pattern `ps`}@}. {@{A shorthand}@} for {@{a concrete list of length _n_}@} is {@{`List(p₁, ..., pₙ)`}@}, which expands to {@{nested conses ending in `Nil`}@}. For instance, {@{the pattern `1 :: 2 :: xs`}@} matches {@{any list that begins with `1` followed by `2`}@}, while {@{`x :: Nil`}@} matches {@{a singleton list}@}. {@{More elaborate patterns}@} such as {@{`x :: y :: List(xs, ys) :: zs`}@} illustrate {@{nested matching}@}.

Overall, lists provide {@{a simple yet powerful abstraction}@} for {@{ordered collections}@}: they are {@{immutable, recursively defined, and naturally suited to pattern matching}@}, making them {@{a staple of functional Scala code}@}.

### list covariance

Scala's {@{immutable `List`}@} is {@{covariant}@}. This means that {@{`List[A]` is a subtype of `List[B]`}@} whenever {@{`A` is a subtype of `B`}@}. Covariance is denoted by {@{the `+` symbol in the type parameter}@}: {@{`List[+T]`}@}.

By declaring it {@{covariant (`sealed abstract class List[+T]`)}@} we allow {@{`Nil`}@} to be represented as {@{a singleton object of type `List[Nothing]`}@}, which is {@{a subtype of any `List[T]`}@}.

However, adding {@{a method that "mutates" \(no actual mutation occurs\) the list (e.g. `prepend(elem: T): List[T]`)}@} {@{breaks covariance}@} because it {@{accepts an argument of type `T`—an input position for a covariant parameter}@}. To restore {@{variance correctness}@} we can use {@{a lower bound on the method's parameter}@}:

> [!example] __implementing `prepend` on `List`__
>
> However, adding {@{a method that "mutates" \(no actual mutation occurs\) the list (e.g. `prepend(elem: T): List[T]`)}@} {@{breaks covariance}@} because it {@{accepts an argument of type `T`—an input position for a covariant parameter}@}. To restore {@{variance correctness}@} we can use {@{a lower bound on the method's parameter}@}:
>
> ```Scala
> trait List[+T]:
>   def prepend[U >: T](elem: U): List[U] = Cons(elem, this)
> ```
>
> This is okay because {@{covariant parameters}@} can be used in {@{lower bounds of method type parameters}@}. The same holds for {@{upper bounds of method type parameters}@} and {@{contravariant parameters}@}.

This is okay because {@{covariant parameters}@} can be used in {@{lower bounds of method type parameters}@}. The same holds for {@{upper bounds of method type parameters}@} and {@{contravariant parameters}@}. Now `prepend` accepts {@{any supertype of `T`}@}, producing a list whose {@{element type is that supertype}@}. For example, calling {@{`xs.prepend(orange)` on a `List[Apple]` \(where `Apple` and `Orange` are _direct_ subclasses of `Fruit`\)}@} yields {@{a `List[Fruit]`}@}.

An alternative to {@{adding a method type parameter}@} is to {@{use extension methods (available in Scala 3)}@}. By defining {@{an extension method for the element type rather than the list itself}@}, we sidestep {@{variance violations}@}:

> [!example] __implementing `prepend` on `List` using extension method__
>
> An alternative to {@{adding a method type parameter}@} is to {@{use extension methods (available in Scala 3)}@}. By defining {@{an extension method for the element type rather than the list itself}@}, we sidestep {@{variance violations}@}:
>
> ```Scala
> extension [T](x: T)
>   def ::(xs: List[T]): List[T] = Cons(x, xs)
> ```
>
> This approach does not require {@{adding a method type parameter}@} and allows {@{natural list construction syntax (`1 :: 2 :: Nil`)}@}.

### list methods

Lists are {@{the fundamental data structure}@} that will {@{recur throughout the course}@}. In Scala a list is {@{an immutable linked‑list whose type carries the element type}@}: {@{`List[Fruit]`}@}. A list can be constructed in {@{two idiomatic ways}@}: using {@{the factory method `List.apply`}@}, which accepts {@{zero or more arguments}@}, or by prepending {@{elements to the sentinel value `Nil` with the cons operator (`::`)}@}. For example:

> [!example] __list construction__
>
> A list can be constructed in {@{two idiomatic ways}@}: using {@{the factory method `List.apply`}@}, which accepts {@{zero or more arguments}@}, or by prepending {@{elements to the sentinel value `Nil` with the cons operator (`::`)}@}. For example:
>
> ```Scala
> val fruits = List("Apple", "Orange", "Banana")
> val nums   = 1 :: 2 :: Nil          // equivalent to List(1, 2)
> ```

{@{Decomposition}@} is equally {@{concise}@}. {@{The head of a list}@} is accessed by {@{`.head` \(the first element\)}@}, {@{the tail by `.tail` \(a list of the remaining elements\)}@}, and {@{pattern matching}@} can be used to {@{deconstruct lists directly}@}:

> [!example] __list decomposition__
>
> {@{Decomposition}@} is equally {@{concise}@}. {@{The head of a list}@} is accessed by {@{`.head`}@}, {@{the tail by `.tail`}@}, and {@{pattern matching}@} can be used to {@{deconstruct lists directly}@}:
>
> ```Scala
> val fruits = List("Apple", "Orange", "Banana")
> val nums   = 1 :: 2 :: Nil   // equivalent to List(1, 2)
>
> fruits.head                  // "Apple"
> nums.tail                    // 2 :: Nil
> nums.isEmpty                 // false
>
> nums match {
>   case x :: y :: _ => x + y  // 3
> }
> ```

The `List` API offers {@{a rich set of operations}@} for {@{sublists, element access, and construction}@}. Methods such as {@{`.length`, `.take(n)`, `.drop(n)`}@}, {@{`.last` \(the last element\), `.init` \(a list of all the elements except for `.lasat`\) and the indexer `xs(n)`}@} provide {@{standard functional list manipulation}@}. {@{The last three}@} are {@{_partial_ methods}@} because they {@{throw exceptions on empty lists or out‑of‑range indices}@}; consequently it is preferable to {@{use safer alternatives whenever possible}@}.

{@{Additional constructors}@} include {@{concatenation (`xs ::: ys`), reversal (`xs.reverse`) and update (`xs.updated(n, x)`)}@}. {@{Element search}@} is supported by {@{`.indexOf(x)` and `.contains(x)`}@}.

{@{The implementation of `last` and `init`}@}, for instance, is {@{linear in the length of the list}@} because it must {@{traverse all elements to reach the tail}@}.

> [!example] __`List.last`, `List.init`__
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

> [!example] __concatenation operator `:::`__
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

> [!example] __`List.reverse`__
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

> [!example] __`List.removeAt`__
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

> [!example] __`deepFlatten`__
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

> [!example] __`map`__
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

> [!example] __`map` example__
>
> Using {@{`map`}@}, {@{a simple scaling routine}@} can be written as:
>
> ```Scala
> def scaleList(xs: List[Double], factor: Double) =
>   xs.map(x => x * factor)
> ```

### filter

{@{Filtering \(`filter`\)}@} extracts {@{elements that satisfy a Boolean predicate}@}:

> [!example] __`filter`__
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

> [!example] __`filter` example__
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

> [!example] __`pack`__
>
> {@{The `pack` function}@} groups {@{consecutive duplicate elements into sublists}@}:
>
> ```Scala
> def pack[T](xs: List[T]): List[::[T]] =
>   xs match
>     case Nil          => Nil
>     case x :: xs1 =>
>       val (more, rest) = xs1.span(y => y == x)
>       (new ::(x, more)) :: pack(rest)
> ```
>
> In {@{the return type of `pack`}@}, {@{`::[T]`}@} is used to {@{represent _nonempty_ lists}@}.

In {@{the return type of `pack`}@}, {@{`::[T]`, a case class under `List[T]`}@}, is used to {@{represent _nonempty_ lists}@}. Using {@{`pack`}@}, {@{a run‑length encoder \(RLE\)}@} is obtained:

> [!example] __`pack` example__
>
> Using {@{`pack`}@}, {@{a run‑length encoder \(RLE\)}@} is obtained:
>
> ```Scala
> def encode[T](xs: List[T]): List[(T, Int)] =
>   pack(xs).map(ys => (ys.head, ys.length))
> ```

As {@{`pack`}@} returns {@{`List[::[T]]` instead of `List[List[T]]`}@}, it is {@{type-safe}@} to {@{call `ys.head`}@} as {@{`ys` is `::[T]` instead of `List[T]`}@}.

### reduce

{@{The generic `reduceLeft`}@} inserts {@{a binary operator between adjacent elements}@} in a {@{left-associative manner}@}:

> [!example] __`reduceLeft`__
>
> {@{The generic `reduceLeft`}@} inserts {@{a binary operator between adjacent elements}@} in a {@{left-associative manner}@}:
>
> ```Scala
> List(x1, ..., xn).reduceLeft((x, y) => x.op(y))
> ```

Using {@{`reduceLeft`}@}, {@{summation}@} becomes:

> [!example] __`reduceLeft` example__
>
> Using {@{`reduceLeft`}@}, {@{summation}@} becomes:
>
> ```Scala
> def sum(xs: List[Int]) = (0 :: xs).reduceLeft(_ + _)
> ```

{@{`reduceLeft`}@} does not {@{support empty lists}@}. It also does not support {@{returning other types other than a supertype of the collection `T`}@}. {@{`foldLeft`}@} generalizes `reduceLeft` by {@{supplying an initial accumulator `z`}@} that is {@{used as a starting value}@}, and returned for {@{an empty list as the starting value is simply returned}@}. It also supports {@{returning any other types}@}, as long as {@{the initial value and the operation have the right types}@}.

> [!example] __`foldLeft`__
>
> {@{`reduceLeft`}@} does not {@{support empty lists}@}. It also does not support {@{returning other types other than a supertype of the collection `T`}@}. {@{`foldLeft`}@} generalizes `reduceLeft` by {@{supplying an initial accumulator `z`}@} that is {@{used as a starting value}@}, and returned for {@{an empty list as the starting value is simply returned}@}. It also supports {@{returning any other types}@}, as long as {@{the initial value and the operation have the right types}@}.
>
> ```Scala
> def sum(xs: List[Int]) = xs.foldLeft(0)(_ + _)
> def product(xs: List[Int]) = xs.foldLeft(1)(_ * _)
> def stringify(xs: List[Int]) = xs.foldLeft("")(_ + _.toString)  # `String` is not a subtype of `Int`
> ```

{@{`reduceRight` and `foldRight`}@} are {@{the right-associative counterparts}@} of {@{`reduceLeft` and `foldLeft` respectively}@}:

> [!example] __`reduceRight`, `foldRight`__
>
> {@{`reduceRight` and `foldRight`}@} are {@{the right-associative counterparts}@} of {@{`reduceLeft` and `foldLeft` respectively}@}:
>
> ```Scala
> def concat[T](xs: List[T], ys: List[T]): List[T] =
>   xs.foldRight(ys)(_ :: _)
> ```

{@{Replacing `foldRight` with `foldLeft`}@} would {@{reverse the order of operations}@}. When {@{the operator is associative and commutative}@}, the final result is {@{the same}@}; otherwise, {@{the types or semantics change}@}. {@{`foldRight`}@} also does not {@{work with infinite lists}@}, as there is {@{no rightmost or ending element to start folding}@}.

{@{Both `reduceLeft` and `foldLeft`}@} can be {@{defined directly in the abstract `List` class}@}:

> [!example] __`reduceLeft`, `foldLeft` implementation__
>
> {@{Both `reduceLeft` and `foldLeft`}@} can be {@{defined directly in the abstract `List` class}@}:
>
> ```Scala
> sealed abstract class List[T]:
>   def reduceLeft(op: (T, T) => T): T =
>     this match
>       case Nil      => throw IllegalOperationException("Nil.reduceLeft")
>       case x :: xs  => xs.foldLeft(x)(op)
>
>   def foldLeft[U](z: U)(op: (U, T) => U): U =
>     this match
>       case Nil      => z
>       case x :: xs  => xs.foldLeft(op(z, x))(op)
> ```
>
> {@{Analogous definitions}@} exist for {@{`reduceRight` and `foldRight`}@}.

{@{Analogous definitions}@} exist for {@{`reduceRight` and `foldRight`}@}. For {@{an example of `foldLeft`}@}, {@{a linear‑time reverse}@} is obtained by {@{folding left with an empty list as the initial value and prepending each element}@}:

> [!example] __`foldLeft` example__
>
> For {@{an example of `foldLeft`}@}, {@{a linear‑time reverse}@} is obtained by {@{folding left with an empty list as the initial value and prepending each element}@}:
>
> ```Scala
> def reverse[T](xs: List[T]): List[T] =
>   xs.foldLeft[List[T]](Nil)((acc, x) => x :: acc)
> ```

## vector

In Scala, {@{`List`}@} is {@{a singly‑linked list}@}: {@{accessing the head is constant time}@} while {@{random access to an element in the middle or at the end}@} requires {@{traversing a length proportional to the length of the list}@}. For workloads where {@{more balanced access patterns are required}@}, the library provides {@{the immutable `Vector` type}@}. A vector internally uses {@{a shallow tree of 32‑element blocks}@}; this design gives {@{roughly logarithmic‑time complexity}@} for {@{both indexing and updates}@} while {@{preserving immutability}@}.

Vectors are constructed {@{in exactly the same way as lists}@}:

> [!example] __`Vector` construction__
>
> Vectors are constructed {@{in exactly the same way as lists}@}:
>
> ```Scala
> val nums   = Vector(1, 2, 3, -88)
> val people = Vector("Bob", "James", "Peter")
> ```

Unlike {@{`List`}@}, vectors do not {@{support the cons operator (`::`)}@}. Instead {@{two operators with a colon pointing toward the sequence operand}@} are provided:

- `x +: xs` ::@:: creates a new vector whose first element is `x` followed by all elements of `xs`;
- `xs :+ x` ::@:: appends `x` to the end of `xs`. In both cases the colon points toward the sequence, reflecting that the operation acts on the whole collection rather than just its head.

## Java sequences

{@{Arrays and strings}@} behave {@{like sequences}@}: while they {@{could _not_ be subclasses of `Seq` \(as they come from Java\)}@}, {@{an `Array[Int]` or a `String`}@} can be used {@{in place of any `Seq[T]` or `Seq[Char]` respectively}@} because the compiler {@{inserts an implicit conversion}@}. Thus one can write:

> [!example] __Java sequence examples__
>
> {@{Arrays and strings}@} behave {@{like sequences}@}: while they {@{could _not_ be subclasses of `Seq` \(as they come from Java\)}@}, {@{an `Array[Int]` or a `String`}@} can be used {@{in place of any `Seq[T]`}@} because the compiler {@{inserts an implicit conversion}@}. Thus one can write:
>
> ```Scala
> val xs: Array[Int] = Array(1, 2, 3)
> xs.map(x => 2 * x)
>
> val ys: String = "Hello world!"
> ys.filter(_.isUpper)
> ```

## range

{@{A `Range`}@} is {@{a lightweight representation of an arithmetic progression}@}. It stores {@{only three fields – lower bound, upper bound and step size}@} – and implements {@{the `Seq[Int]` interface}@}. {@{Three constructor operators}@} are available:

> [!example] __`Range` examples__
>
> {@{Three constructor operators}@} are available:
>
> ```Scala
> val r = 1 until 5  // 1,2,3,4 (end is exclusive)
> val s = 1 to 5     // 1,2,3,4,5 (end is inclusive)
> 1 to 10 by 3       // 1,4,7,10
> 6 to 1 by -2       // 6,4,2
> ```

Because ranges are {@{lazy and small}@}, they provide {@{constant‑time `contains`, `head`, `last` and indexing}@}.

## sequence methods

The following operations are {@{common to all `Seq`s}@} (and thus to {@{lists, vectors, arrays, strings and ranges}@}):

- `exists(p)` ::@:: Returns `true` if any element satisfies predicate `p`. For empty sequences it returns `false`.
- `forall(p)` ::@:: Returns `true` only if every element satisfies `p`. For empty sequences it returns `true`.
- `zip(ys)` ::@:: Combines two sequences into a sequence of pairs. If they do not have the same length, the result is truncated to the shorter length.
- `unzip` ::@:: Splits a sequence of pairs into two separate sequences.
- `flatMap(f)` ::@:: Applies a collection‑valued function to each element and concatenates the results.
- `sum`, `product` ::@:: Aggregate numeric collections.
- `max`, `min` ::@:: Return the largest or smallest element (requires an implicit `Ordering`).

These operations are typically implemented via {@{recursion or tail‑recursion}@} over {@{the underlying list structure}@}.

> [!example] __combinations__
>
> To enumerate {@{all pairs `(x, y)` with `x ∈ 1..M` and `y ∈ 1..N`}@}, one can write:
>
> ```Scala
> (1 to M).flatMap(x => (1 to N).map(y => (x, y)))
> ```

<!-- markdownlint MD028 -->

> [!example] __scalar product__
>
> Given {@{two numeric vectors of equal length}@}, {@{their scalar product}@} is {@{the sum of element‑wise products}@}. In Scala this can be expressed concisely:
>
> ```Scala
> def scalarProduct(xs: Vector[Double], ys: Vector[Double]): Double =
>   xs.zip(ys).map(_ * _).sum
> ```
>
> Here {@{`zip`}@} produces {@{a sequence of pairs}@}; {@{`_ * _`}@} is {@{shorthand for `(x, y) => x * y`}@}.

<!-- markdownlint MD028 -->

> [!example] __primality test__
>
> {@{A concise way}@} to test whether {@{an integer `n` is prime}@} uses {@{the `forall` operation}@}:
>
> ```Scala
> def isPrime(n: Int): Boolean =
>   (2 to n - 1).forall(d => n % d != 0)
> ```
>
> Although {@{not efficient for large numbers}@}, this expression captures {@{the mathematical definition in a single line}@}.

## mapping

{@{A `Map`}@} associates {@{keys of type `Key` with values of type `Value`}@}. {@{The literal syntax `key -> value`}@} is {@{syntactic sugar for a pair `(key, value)`}@}, implemented as {@{an extension method on any object}@}. Typical examples:

> [!example] __`Map` construction__
>
> {@{The literal syntax `key -> value`}@} is {@{syntactic sugar for a pair `(key, value)`}@}, implemented as {@{an extension method on any object}@}. Typical examples:
>
> ```Scala
> val romanNumerals    = Map("I" -> 1, "V" -> 5, "X" -> 10)
> val capitalOfCountry = Map("US" -> "Washington", "Switzerland" -> "Bern")
> ```

Maps extend {@{`Iterable[(Key, Value)]`}@}, so {@{all collection operations}@} apply {@{to key/value pairs}@}. Moreover, `Map` extends {@{the function type `Key => Value`}@}; thus a map can be {@{used as a function}@}:

> [!example] __`Map` as a function example__
>
> Moreover, `Map` extends {@{the function type `Key => Value`}@}; thus a map can be {@{used as a function}@}:
>
> ```Scala
> val capitalOfCountry = Map("US" -> "Washington", "Switzerland" -> "Bern")
> capitalOfCountry("US")  // returns "Washington"
> ```

Attempting to {@{call a map with a missing key}@} throws {@{an `java.util.NoSuchElementException`}@}; {@{safer access}@} is provided by {@{the `get` method}@} which {@{returns an `Option[Value]`}@}. {@{The `Option` type}@} has {@{two subclasses, `Some(value)` and `None`}@}, enabling {@{pattern matching}@}:

> [!example] __`Map.get` example__
>
> Attempting to {@{call a map with a missing key}@} throws {@{an `java.util.NoSuchElementException`}@}; {@{safer access}@} is provided by {@{the `get` method}@} which {@{returns an `Option[Value]`}@}.
>
> ```Scala
> val capitalOfCountry = Map("US" -> "Washington", "Switzerland" -> "Bern")
> def showCapital(country: String) =
>   capitalOfCountry.get(country) match {
>     case Some(capital) => capital
>     case None          => "missing data"
>   }
> ```

### map update

Because {@{maps are immutable}@}, updates {@{produce new maps}@}. {@{The operator `+`}@} adds {@{a single key/value pair}@}; {@{the operator `++`}@} {@{merges two maps}@}:

> [!example] __`++` and `+` example__
>
> Because {@{maps are immutable}@}, updates {@{produce new maps}@}. {@{The operator `+`}@} adds {@{a single key/value pair}@}; {@{the operator `++`}@} {@{merges two maps}@}:
>
> ```Scala
> val m1 = Map("red" -> 1, "blue" -> 2)
> val m2 = m1 + ("blue" -> 3)      // blue now maps to 3
> val m3 = m1 ++ Map("blue" -> 3)  // same as above
> ```

{@{Both operations}@} are {@{purely functional}@}: {@{the original map}@} {@{remains unchanged}@}.

### map methods

{@{Ordering a collection}@} can be expressed with {@{`sortWith` or `sorted`}@}. For example:

> [!example] __`sortWith` and `sorted` examples__
>
> {@{Ordering a collection}@} can be expressed with {@{`sortWith` or `sorted`}@}. For example:
>
> ```Scala
> val fruit = List("apple", "pear", "orange", "pineapple")
> fruit.sortWith(_.length < _.length)  // order by length
> fruit.sorted                         // natural ordering
> ```

{@{Grouping \(`groupBy`\)}@} partitions {@{a collection into a map}@} keyed by {@{the result of a discriminator function}@}:

> [!example] __`groupBy` examples__
>
> {@{Grouping}@} partitions {@{a collection into a map}@} keyed by {@{the result of a discriminator function}@}:
>
> ```Scala
> val fruit = List("apple", "pear", "orange", "pineapple")
> fruit.groupBy(_.head)  // Map('a' -> List("apple"), 'p' -> List("pear", "pineapple"), ...)
> ```

{@{`Map.withDefaultValue`}@} turns {@{a map into a total function}@} by providing {@{a default value for missing keys}@}.

<!-- markdownlint MD028 -->

> [!example] __polynomial__
>
> {@{A polynomial}@} can be represented as {@{a map from exponent to coefficient}@}. For instance, {@{`x^3 - 2x + 5`}@} becomes:
>
> ```Scala
> Map(0 -> 5, 1 -> -2, 3 -> 1)
> ```

<!-- markdownlint MD028 -->

> [!example] __`Polynomial`__
>
> {@{This observation}@} motivates {@{the following `Polynomial` class}@}, which stores {@{its terms in an immutable map}@} and provides {@{arithmetic operations}@}:
>
> ```Scala
> class Polynomial(nonZeroTerms: Map[Int, Double]) {
>   def this(bindings: (Int, Double)*) = this(bindings.toMap)
>
>   val terms = nonZeroTerms.withDefaultValue(0.0)
>
>   def +(other: Polynomial): Polynomial =
>     Polynomial(terms ++ other.terms.map { case (exp, coeff) =>
>       exp -> (coeff + terms(exp))
>     })
>     /*
>     Alternative implementation:
>     Polynomial(other.terms.foldLeft(terms) { case (acc, (exp, coeff)) =>
>       acc + (exp -> (coeff + acc(exp)))
>     })
>     */
>
>   override def toString: String =
>     if (terms.isEmpty) "0"
>     else {
>       val termStrings = terms.toList.sorted.reverse.map {
>         case (exp, coeff) =>
>           val exponent = if (exp == 0) "" else s"x^$exp"
>           s"$coeff$exponent"
>       }
>       termStrings.mkString(" + ")
>     }
> }
> ```

To avoid {@{the verbosity of `Polynomial(Map(...))`}@}, {@{a _varargs_ constructor}@} is provided:

> [!example] __`Polynomial` varargs constructor__
>
> To avoid {@{the verbosity of `Polynomial(Map(...))`}@}, {@{a _varargs_ constructor}@} is provided:
>
> ```Scala
> def this(bindings: (Int, Double)*) = this(bindings.toMap)
> ```

## set

{@{Scala's collections library}@} supplies {@{the immutable `Set`}@}, which represents {@{an _unordered_ collection of _distinct_ elements}@}. Sets are declared {@{in the same way as sequences}@}:

> [!example] __`Set` construction__
>
> Sets are declared {@{in the same way as sequences}@}:
>
> ```Scala
> val fruit = Set("apple", "banana", "pear")
> val s     = (1 to 6).toSet                  // Set(1,2,3,4,5,6)
> ```

{@{Most sequence operations}@} have {@{direct counterparts for sets}@}. For instance

> [!example] __`Set` methods__
>
> {@{Most sequence operations}@} have {@{direct counterparts for sets}@}. For instance
>
> ```Scala
> val fruit = Set("apple", "banana", "pear")
> val s     = (1 to 6).toSet                  // Set(1,2,3,4,5,6)
>
> s.map(_ + 2)                       // Set(3,4,5,6,7,8)
> fruit.filter(_.startsWith("app"))  // Set("apple")
> s.nonEmpty                         // true
> ```

{@{The core distinction}@} between {@{a `Set` and a `Seq`}@} is that the former {@{does not preserve order and automatically removes duplicates}@}; consequently {@{the only fundamental operation}@} on a set is {@{membership testing via `contains`}@}. {@{A small example}@} shows {@{how duplicate values collapse}@}:

> [!example] __`Set` deduplication__
>
> {@{A small example}@} shows {@{how duplicate values collapse}@}:
>
> ```Scala
> val s = (1 to 6).toSet  // Set(1,2,3,4,5,6)
> s.map(_ / 2)            // Set(0,1,2,3)
> ```

{@{These properties}@} make sets especially suitable for {@{combinatorial search problems}@} where the focus lies on {@{the presence or absence of items rather than their position}@}.
