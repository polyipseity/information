---
aliases:
  - COMP 3031 Scala algorithm
  - COMP 3031 Scala algorithms
  - COMP3031 Scala algorithm
  - COMP3031 Scala algorithms
  - HKUST COMP 3031 Scala algorithm
  - HKUST COMP 3031 Scala algorithms
  - HKUST COMP3031 Scala algorithm
  - HKUST COMP3031 Scala algorithms
  - Scala algorithm
  - Scala algorithms
tags:
  - flashcard/active/special/academia/HKUST/COMP_3031/algorithms
  - language/in/English
---

# Scala algorithms

- HKUST COMP 3031

## sorting

### insertion sort

{@{Sorting}@} can be {@{implemented purely functionally}@} using {@{__insertion sort__}@}. The algorithm {@{recursively sorts the tail of the list}@} and then inserts {@{the head element into its correct position within that sorted sub‑list}@}: <!--SR:!2025-12-02,27,290!2025-11-12,16,290!2025-11-11,15,290!2025-11-10,14,290!2025-11-11,15,290-->

> [!example] __insertion sort__
>
> The algorithm {@{recursively sorts the tail of the list}@} and then inserts {@{the head element into its correct position within that sorted sub‑list}@}:
>
> ```Scala
> def isort(xs: List[Int]): List[Int] = xs match {
>   case Nil      => Nil
>   case y :: ys  => insert(y, isort(ys))
> }
> ```
<!--SR:!2025-11-11,15,290!2025-11-11,15,290-->

{@{The helper `insert`}@} places {@{a value in the appropriate spot of an already sorted list}@}. {@{A typical implementation}@} is: <!--SR:!2025-11-10,14,290!2025-11-11,15,290!2025-11-11,15,290-->

> [!example] __insertion sort insertion__
>
> {@{The helper `insert`}@} places {@{a value in the appropriate spot of an already sorted list}@}. {@{A typical implementation}@} is:
>
> ```Scala
> def insert(x: Int, xs: List[Int]): List[Int] = xs match {
>   case Nil      => List(x)
>   case y :: ys =>
>     if (x < y) x :: xs else y :: insert(x, ys)
> }
> ```
<!--SR:!2025-11-10,14,290!2025-11-10,14,290!2025-11-08,12,270-->

{@{The worst‑case time complexity}@} of insertion sort on {@{a list of length _N_}@} is {@{quadratic, i.e., proportional to $N \times N$}@}, because {@{each new element}@} may need to be {@{compared with every preceding element in the sorted sub‑list}@}. <!--SR:!2025-11-12,16,290!2025-11-12,16,290!2025-11-12,16,290!2025-11-12,16,290!2025-11-10,14,290-->

### merge sort

{@{The classic divide‑and‑conquer approach}@} to sorting, {@{_merge sort_}@} is expressed {@{succinctly in Scala}@}: <!--SR:!2025-11-12,16,290!2025-11-11,15,290!2025-11-12,16,290-->

> [!example] __merge sort__
>
> {@{The classic divide‑and‑conquer approach}@} to sorting, {@{_merge sort_}@} is expressed {@{succinctly in Scala}@}:
>
> ```Scala
> def msort(xs: List[Int]): List[Int] =
>   val n = xs.length / 2
>   if n == 0 then xs
>   else
>     def merge(xs: List[Int], ys: List[Int]) = ???
>     val (fst, snd) = xs.splitAt(n)
>     merge(msort(fst), msort(snd))
> ```
<!--SR:!2025-11-11,15,290!2025-11-10,14,290!2025-11-08,12,270-->

The algorithm first splits {@{the list in half using `splitAt`}@}, recursively {@{sorts each half}@}, and finally {@{merges the two sorted sub‑lists}@}. <!--SR:!2025-11-10,14,290!2025-11-10,14,290!2025-11-10,14,290-->

#### merge sort splitting

{@{The split operation `List.splitAt`}@} yields {@{a tuple `(List[A], List[A])` \(a pair of lists\)}@}. {@{The returned pair}@} is commonly used in {@{pattern matching}@}: <!--SR:!2025-11-12,16,290!2025-11-10,14,290!2025-11-10,14,290!2025-11-11,15,290-->

> [!example] __merge sort splitting__
>
> {@{The split operation `List.splitAt`}@} yields {@{a tuple `(List[A], List[A])` \(a pair of lists\)}@}. {@{The returned pair}@} is commonly used in {@{pattern matching}@}:
>
> ```Scala
> val (label, value) = pair
> val (fst, snd) = xs.splitAt(n)
> ```
<!--SR:!2025-11-12,16,290!2025-11-10,14,290!2025-11-11,15,290!2025-11-10,14,290-->

One could {@{re‑implement `splitAt`}@} as {@{an extension method}@}: <!--SR:!2025-11-11,15,290!2025-11-10,14,290-->

> [!example] __`List.splitAt`__
>
> One could {@{re‑implement `splitAt`}@} as {@{an extension method}@}:
>
> ```Scala
> extension [A](xs: List[A])
>   def splitAt(n: Int): (List[A], List[A]) =
>     (xs.take(n), xs.drop(n))
> ```
<!--SR:!2025-11-12,16,290!2025-11-11,15,290-->

### merge sort merging

{@{A safe and exhaustive definition}@} of the merge step uses {@{pattern matching on both input lists}@}: <!--SR:!2025-11-12,16,290!2025-11-12,16,290-->

> [!example] __merge sort merging__
>
> {@{A safe and exhaustive definition}@} of the merge step uses {@{pattern matching on both input lists}@}:
>
> ```Scala
> def merge(xs: List[Int], ys: List[Int]) =
>   (xs, ys) match {
>     case (Nil, ys) => ys
>     case (xs, Nil) => xs
>     case (x :: xs1, y :: ys1) =>
>       if x < y then x :: merge(xs1, ys)
>       else y :: merge(xs, ys1)
>   }
> ```
<!--SR:!2025-11-12,16,290!2025-11-10,14,290-->

The compiler guarantees that {@{all possible shapes of the input lists}@} are handled; {@{any omission}@} results in {@{a warning \(not error\)}@}. <!--SR:!2025-11-12,16,290!2025-11-10,14,290!2025-11-12,16,290-->

### sorting arbitrary types

To sort lists whose {@{elements are not necessarily `Int`}@}, {@{the comparison operation}@} must be {@{supplied explicitly}@}. {@{The most flexible design}@} introduces {@{a polymorphic type parameter}@} and {@{a second argument list that receives a less‑than predicate}@}: <!--SR:!2025-11-11,15,290!2025-11-10,14,290!2025-11-10,14,290!2025-11-12,16,290!2025-11-11,15,290!2025-11-11,15,290-->

> [!example] __merge sort with comparator__
>
> {@{The most flexible design}@} introduces {@{a polymorphic type parameter}@} and {@{a second argument list that receives a less‑than predicate}@}:
>
> ```Scala
> def msort[T](xs: List[T])(lt: (T, T) => Boolean): List[T] =
>   val n = xs.length / 2
>   if n == 0 then xs
>   else
>     def merge(xs: List[T], ys: List[T]) =
>       (xs, ys) match {
>         case (Nil, ys) => ys
>         case (xs, Nil) => xs
>         case (x :: xs1, y :: ys1) =>
>           if lt(x, y) then x :: merge(xs1, ys)
>           else y :: merge(xs, ys1)
>       }
>     val (fst, snd) = xs.splitAt(n)
>     merge(msort(fst)(lt), msort(snd)(lt))
> ```
<!--SR:!2025-11-12,16,290!2025-11-11,15,290!2025-11-12,16,290-->

{@{The `lt` function}@} can be {@{passed by name}@} or {@{inferred from the context \(keyword `implicit`\)}@}. With `msort` accepting {@{a comparison predicate}@}, it can {@{sort any list}@}: <!--SR:!2025-11-12,16,290!2025-11-11,15,290!2025-11-11,15,290!2025-11-11,15,290!2025-11-11,15,290-->

> [!example] __using merge sort with comparator__
>
> {@{The `lt` function}@} can be {@{passed by name}@} or {@{inferred from the context \(keyword `implicit`\)}@}. With `msort` accepting {@{a comparison predicate}@}, it can {@{sort any list}@}:
>
> ```Scala
> val xs      = List(-5, 6, 3, 2, 7)
> val fruits  = List("apple", "pear", "orange", "pineapple")
>
> msort(xs)((x: Int, y: Int) => x < y)
> msort(fruits)((x: String, y: String) => x.compareTo(y) < 0)
>
> // Type inference allows a shorter form
> msort(xs)( (x, y) => x < y )
> ```
<!--SR:!2025-11-10,14,290!2025-11-10,14,290!2025-11-12,16,290!2025-11-12,16,290!2025-11-12,16,290-->

These examples demonstrate how Scala's {@{type inference and higher‑order functions}@} enable {@{concise yet powerful generic algorithms}@}. <!--SR:!2025-11-10,14,290!2025-11-11,15,290-->
