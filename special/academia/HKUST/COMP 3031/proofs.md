---
aliases:
  - COMP 3031 Scala proof
  - COMP 3031 Scala proofs
  - COMP3031 Scala proof
  - COMP3031 Scala proofs
  - HKUST COMP 3031 Scala proof
  - HKUST COMP 3031 Scala proofs
  - HKUST COMP3031 Scala proof
  - HKUST COMP3031 Scala proofs
  - Scala proof
tags:
  - flashcard/active/special/academia/HKUST/COMP_3031/proofs
  - language/in/English
---

# Scala proofs

- HKUST COMP 3031

## list properties

In {@{functional programming}@}, lists are {@{one of the most common data structures}@} and they form {@{the basis for many proofs about program correctness}@}. {@{A central operation}@} on lists is {@{concatenation}@}, denoted by {@{`:::` in Scala}@}. For {@{two lists `xs` and `ys`}@}, {@{the expression `xs ::: ys`}@} produces a new list that contains {@{all elements of `xs` followed by all elements of `ys`}@}. {@{Two fundamental algebraic laws}@} hold for this operator: \(annotation: 2 items: {@{associativity, neutral element}@}\)

- __Associativity__ ::@:: `(xs ::: ys) ::: zs = xs ::: (ys ::: zs)`
- __Neutral element__ ::@:: – the empty list `Nil` is a left and right identity: `xs ::: Nil = xs` and `Nil ::: xs = xs`

These laws are not {@{merely curiosities}@}; they enable reasoning about {@{program transformations, optimisations, and correctness proofs}@}. {@{The standard way to establish them}@} in a purely functional setting is {@{_structural induction_}@}.

## structural induction

The familiar principle of {@{natural induction on the natural numbers}@} states that to prove {@{a property $P(n)$ for all integers $n \ge b$}@}, one must show: \(annotation: 2 items: {@{base case → inductive step}@}\)

1. \(annotation: natural induction\) __Base case__: ::@:: $P(b)$ holds.
2. \(annotation: natural induction\) __Inductive step__: ::@:: For every $n \ge b$, if $P(n)$ holds then so does $P(n+1)$.

For {@{lists, trees, etc.}@}, the analogous principle is {@{_structural induction_}@}.

A list can be {@{either `Nil` or an element cons‑ed onto another list (`x :: xs`)}@}. To prove {@{a property $P(\texttt{xs})$ for all lists}@}, we show:

1. \(annotation: structural induction on lists\) __Base case__: ::@:: $P(\texttt{Nil})$ holds.
2. \(annotation: structural induction on lists\) __Inductive step__: ::@:: For any element `x` and any sublist `xs`, if $P(\texttt{xs})$ holds then so does $P(\texttt{x :: xs})$.

Because {@{list construction is recursive}@}, structural induction mirrors {@{the shape of the data}@}. It also holds for {@{trees and other recursively defined structures}@} with modifications of {@{the base and inductive cases to match the constructors}@}.

## referential transparency

{@{Functional programs}@} are {@{_pure_}@}: functions have {@{no side effects}@} and every expression denotes {@{a value that depends solely on its inputs}@}. This property—{@{_referential transparency_}@}—allows us to replace {@{any sub‑expression with an equal one without changing program behaviour}@}. In {@{proofs}@}, it means we may freely {@{apply reduction rules (the equations defining `:::` or other functions) inside larger terms}@}. {@{The factorial example}@} below illustrates {@{this principle}@}.

## proofs

### proving lower bounds on factorial

Consider {@{the standard recursive definition of factorial}@} in Scala:

> [!example] __factorial definition__
>
> Consider {@{the standard recursive definition of factorial}@} in Scala:
>
> ```Scala
> def factorial(n: Int): Int =
>   if n == 0 then 1         // base case
>   else n * factorial(n-1)  // recursive step
> ```

We wish to prove that for {@{all integers $n \ge 4$}@}, {@{$$\texttt{factorial}(n) \;>\; 2^n \,.$$}@}

> [!example] __proof__
>
> {@{_Base case._}@} `factorial(4)` {@{evaluates to `24`, and `2^4 = 16`}@}; thus {@{the inequality holds}@}.
>
> {@{_Inductive step._}@} Assume {@{`factorial(n) > 2^n` for some $n \ge 4$}@}. Then
>
> ```pseudocode
> factorial(n + 1)
>   = (n + 1) * factorial(n)  // by definition
>   > 2 * factorial(n)        // because n+1 > 2
>   > 2 * 2^n                 // by induction hypothesis
>   = 2^(n+1).                // by exponentiation rule
> ```
>
> Each line follows from {@{a referentially transparent rewrite}@}: the first uses {@{the recursive clause}@}, the second uses {@{arithmetic comparison}@}, and the third applies {@{the induction hypothesis}@}. Thus the property {@{holds for all $n \ge 4$}@}.

### proving associativity of `:::` by structural induction

Let us prove {@{the associativity law}@} for lists: {@{`(xs ::: ys) ::: zs = xs ::: (ys ::: zs)`}@}. {@{The definition of `:::`}@} is:

> [!example] __concatenation definition__
>
> {@{The definition of `:::`}@} is:
>
> ```Scala
> extension [T](xs: List[T]) {
>   def :::(ys: List[T]): List[T] =
>     xs match {
>       case Nil          => ys                 // 1st clause
>       case x :: xs1     => x :: (xs1 ::: ys)  // 2nd clause
>     }
> }
> ```

<!-- markdownlint MD028 -->

> [!example] __proof__
>
> {@{__Base case (`xs = Nil`).__}@}
>
> - Left‑hand side: `(Nil ::: ys) ::: zs` reduces {@{by the first clause to `ys ::: zs`}@}.
> - Right‑hand side: `Nil ::: (ys ::: zs)` reduces, {@{again by the first clause, to `ys ::: zs`}@}.
> - Both sides are {@{identical, so the base case holds}@}.
>
> {@{__Inductive step (`xs = x :: xs1`).__}@}
>
> Assume {@{the property for `xs1`}@}; we must show it for {@{`x :: xs1`}@}.
>
> {@{Left‑hand side}@}:
>
> ```pseudocode
> ((x :: xs1) ::: ys) ::: zs
>   = (x :: (xs1 ::: ys)) ::: zs  // by 2nd clause of :::
>   = x :: ((xs1 ::: ys) ::: zs)  // by 2nd clause again
>   = x :: (xs1 ::: (ys ::: zs))  // induction hypothesis
> ```
>
> {@{Right‑hand side}@}:
>
> ```pseudocode
> (x :: xs1) ::: (ys ::: zs)
>   = x :: (xs1 ::: (ys ::: zs))  // by 2nd clause of :::
> ```
>
> Both sides {@{reduce to the same expression}@}, completing {@{the inductive step}@}. Hence {@{associativity holds for all lists}@}.

### proving `xs ::: Nil = xs`

To {@{prove `xs ::: Nil = xs`}@}, the proof {@{proceeds similarly}@}. {@{The base case is trivial}@} because {@{`Nil ::: Nil` reduces directly to `Nil`}@}. In {@{the inductive step}@} we need {@{two equations}@}: one from {@{the definition of `:::` applied to `x :: xs`}@} and one from {@{the induction hypothesis that `xs ::: Nil = xs`}@}. Thus, {@{_two_ equations}@} are needed.

### proving reverse is its own inverse

Define {@{list reversal}@} recursively:

> [!example] __`reverse` definition__
>
> Define {@{list reversal}@} recursively:
>
> ```Scala
> extension [T](xs: List[T]) {
>   def reverse: List[T] =
>     xs match {
>       case Nil      => Nil                        // 1st clause
>       case x :: xs1 => xs1.reverse ::: (x :: Nil) // 2nd clause
>     }
> }
> ```

We aim to prove that {@{reversing twice yields the original list}@}: {@{`xs.reverse.reverse = xs`}@}.

> [!example] __proof__
>
> {@{__Base case (`xs = Nil`).__}@} {@{`Nil.reverse.reverse`}@} reduces to {@{`Nil`, matching the right‑hand side}@}.
>
> {@{__Inductive step (`xs = x :: xs1`).__}@}
>
> {@{Left hand side}@}:
>
> ```pseudocode
> (x :: xs1).reverse.reverse
>   = (xs1.reverse ::: (x :: Nil)).reverse  // by 2nd clause of reverse
> ```
>
> {@{Right hand side}@}:
>
> ```psuedocode
> x :: xs1
>   = x :: xs1.reverse.reverse  // by inductive hypothesis
> ```
>
> At this point we {@{cannot directly simplify further}@}. Try to {@{_factor_ out _common subexpressions_}@}. In particular, we see {@{the sub-expression `xs1.reverse` appears in both terms}@}. We must introduce {@{an auxiliary lemma replacing the common sub-expression by a new symbol `ys`}@}:
>
> > For {@{any list `ys` and element `x`}@}, {@{`(ys ::: (x :: Nil)).reverse = x :: ys.reverse`}@}.
>
> {@{This lemma}@} is proved by {@{a second induction on `ys`}@}. Its base case uses {@{the first clause of `:::` and the second clause of `reverse`}@}; the inductive step employs {@{the second clause of `:::`, the second clause of `reverse`, and the induction hypothesis}@}. Once {@{this auxiliary equation is established}@}, we can {@{finish the main proof}@}:
>
> ```pseudocode
> (x :: xs1).reverse.reverse
>   = (xs1.reverse ::: (x :: Nil)).reverse  // original rewrite
>   = x :: xs1.reverse.reverse              // by auxiliary lemma
>   = x :: xs1                              // induction hypothesis on xs1
> ```
>
> Thus {@{`xs.reverse.reverse = xs` holds for all lists}@}.

### proving `map` is distributive over concatenation

A further law often used in functional programming is that {@{mapping a function over the concatenation of two lists}@} equals {@{the concatenation of the mapped sublists}@}: {@{`(xs ::: ys).map(f) = xs.map(f) ::: ys.map(f)`}@}.

To prove this, one again uses {@{structural induction on `xs`}@}. {@{The base case}@} follows from {@{`Nil.map(f) = Nil` and `Nil ::: ys = ys`}@}. In {@{the inductive step}@}, we rely on {@{both clauses of `:::` and on the two equations defining `map`}@}:

> [!example] __`map` definition__
>
> In {@{the inductive step}@}, we rely on {@{both clauses of `:::` and on the two equations defining `map`}@}:
>
> ```Scala
> extension [T](xs: List[T]) {
>   def map[S](f: T => S): List[S] =
>     xs match {
>       case Nil      => Nil                 // 1st clause
>       case x :: xs1 => f(x) :: xs1.map(f)  // 2nd clause
>     }
> }
> ```
