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

## set properties

To assert that {@{an implementation of a set actually behaves as a set}@}, we state {@{three algebraic laws}@} that {@{any correct representation of a set}@} must satisfy: \(annotation: 3 items: {@{empty contains nothing, insertion guarantees presence, non-insertion preserves membership}@}\)

- __Empty contains nothing__ ::@:: $$\text{Empty.contains}(x) = \text{false}$$
- __Insertion guarantees presence__ ::@:: $$s.\text{incl}(x).\text{contains}(x) = \text{true}$$
- __Non‑insertion preserves membership__ ::@:: For distinct elements $x\neq y$, $$s.\text{incl}(y).\text{contains}(x) = s.\text{contains}(x)$$

These laws capture {@{the essential behavior}@} of a set: {@{an empty set}@} contains {@{nothing}@}; {@{inserting an element}@} guarantees that it is {@{now present}@}; and {@{inserting another element}@} does not {@{disturb the membership status of unrelated elements}@}.

## structural induction

The familiar principle of {@{natural induction on the natural numbers}@} states that to prove {@{a property $P(n)$ for all integers $n \ge b$}@}, one must show: \(annotation: 2 items: {@{base case → inductive step}@}\)

1. \(annotation: natural induction\) __Base case__: ::@:: $P(b)$ holds.
2. \(annotation: natural induction\) __Inductive step__: ::@:: For every $n \ge b$, if $P(n)$ holds then so does $P(n+1)$.

For {@{lists, trees, etc.}@}, the analogous principle is {@{_structural induction_}@}.

A list can be {@{either `Nil` or an element cons‑ed onto another list (`x :: xs`)}@}. To prove {@{a property $P(\texttt{xs})$ for all lists}@}, we show:

1. \(annotation: structural induction on lists\) __Base case__: ::@:: $P(\texttt{Nil})$ holds.
2. \(annotation: structural induction on lists\) __Inductive step__: ::@:: For any element `x` and any sublist `xs`, if $P(\texttt{xs})$ holds then so does $P(\texttt{x :: xs})$.

Because {@{list construction is recursive}@}, structural induction mirrors {@{the shape of the data}@}. It also holds for {@{trees and other recursively defined structures}@} with modifications of {@{the base and inductive cases to match the constructors}@}.

### structural induction on trees

Unlike {@{list induction}@}, which relies on {@{a single predecessor element}@}, {@{tree induction}@} proceeds from {@{the leaves upward}@}. The general principle is:

- inductive hypotheses ::@:: To prove a property $P(t)$ for every tree $t$ of a given type, first show that $P(l)$ holds for all leaf nodes $l$.
- induction step ::@:: Then, for each constructor of internal nodes—say an internal node $n$ with sub‑trees $s_{1},\dots ,s_{k}$—prove that the conjunction $\bigwedge_{i} P(s_{i})$ implies $P(n)$.

The proof is typically structured as {@{a base case (leaves)}@} followed by {@{an inductive step for each node constructor}@}. The technique guarantees that {@{any property established in this way}@} holds for {@{all trees, no matter how deeply nested}@}.

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

> [!example] __proof: part 1__
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
> At this point we {@{cannot directly simplify further}@}. Try to {@{_factor_ out _common subexpressions_}@}.

<!-- markdownlint MD028 -->

> [!example] __proof: part 2__
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

### proving set properties

{@{An application}@} of tree induction is {@{the implementation of a binary search tree}@} representing {@{a set of integers}@}. {@{The `IntSet` type}@} can be expressed as:

> [!example] __binary tree integer set__
>
> {@{An application}@} of tree induction is {@{the implementation of a binary search tree}@} representing {@{a set of integers}@}. {@{The `IntSet` type}@} can be expressed as:
>
> ```Scala
> sealed abstract class IntSet {
>   def contains(x: Int): Boolean
>   def incl(x: Int): IntSet
> }
> object Empty extends IntSet {
>   def contains(x: Int) = false
>   def incl(x: Int)     = NonEmpty(x, Empty, Empty)
> }
> case class NonEmpty(elem: Int, left: IntSet, right: IntSet) extends IntSet {
>   def contains(x: Int): Boolean =
>     if (x < elem) left.contains(x)
>     else if (x > elem) right.contains(x)
>     else true
>   def incl(x: Int): IntSet =
>     if (x < elem) NonEmpty(elem, left.incl(x), right)
>     else if (x > elem) NonEmpty(elem, left, right.incl(x))
>     else this
> }
> ```

{@{The tree is binary}@} because {@{each internal node}@} has {@{at most two children}@}. {@{The _leaf_ constructor}@} is {@{`Empty`}@}; {@{the only _internal_ constructor}@} is {@{`NonEmpty`}@}.

> [!example] __proving empty contains nothing__
>
> {@{The base case}@} is {@{trivial}@} because {@{`Empty.contains` is defined as `false`}@}. {@{No inductive step}@} is {@{required}@}.

<!-- markdownlint MD028 -->

> [!example] __proving insertion guarantees presence: base case__
>
> {@{Base}@}: for {@{an empty tree}@},
>
> ```Scala
> Empty.incl(x).contains(x) = NonEmpty(x, Empty, Empty).contains(x)
> ```
>
> which evaluates to {@{`true` \(RHS\) by the definition of `NonEmpty.contains`}@}.

<!-- markdownlint MD028 -->

> [!example] __proving non‑insertion preserves membership: inductive step__
>
> {@{Inductive step}@}: assume {@{$P(s)$ holds for a subtree $s$}@}; we must show it for {@{`NonEmpty(elem, l, r)`}@}. That is,
>
> ```Scala
> NonEmpty(elem, l, r).incl(x).contains(x) == true
> ```
>
> - If {@{`x == elem`}@}, {@{the `incl` method}@} returns {@{the same node}@}, and {@{`contains(x)` is `true`}@}.
> - If {@{`x < elem`}@}, `incl` recurses {@{into the left child: `NonEmpty(elem, l.incl(x), r)`}@}. By {@{the induction hypothesis}@}, {@{`l.incl(x).contains(x)` is `true`}@}; consequently {@{the whole expression evaluates to `true`}@}.
> - {@{The case `x > elem`}@} is {@{analogous with the right child}@}.
>
> Thus {@{law 2 holds for all trees}@}.

<!-- markdownlint MD028 -->

> [!example] __proving non‑insertion preserves membership: base case__
>
> The proof {@{mirrors law 2}@} but keeps {@{track of a distinct element $y$}@}.
>
> {@{Base}@}: for {@{an empty tree}@},
>
> ```Scala
> Empty.incl(y).contains(x) = NonEmpty(y, Empty, Empty).contains(x)
> ```
>
> which reduces to {@{`Empty.contains(x)` \(RHS\)}@} by {@{the definition of `NonEmpty.contains`}@}.

<!-- markdownlint MD028 -->

> [!example] __proving non‑insertion preserves membership: inductive step__
>
> {@{Inductive step}@}: consider {@{`NonEmpty(elem, l, r)`}@} and assume {@{$y \neq x$}@}. We need to show:
>
> ```Scala
> NonEmpty(z, l, r).incl(y).contains(x) == NonEmpty(z, l, r).contains(x)
> ```
>
> - If {@{$z = x$}@} – then {@{both sides evaluate to `true`}@} because {@{the node itself contains $x$}@} and {@{`incl(y)` keeps $x$ as the element of the current node}@}.
> - If {@{$z = y$}@} – `incl(y)` {@{returns the node as-is}@}.
> - If {@{$z < x$ and $z < y$ \($z$ is smallest, i.e. $z < x < y$ or $z < y < x$\)}@} – the search {@{continues into the right child: `r.incl(y).contains(x)`}@}. By {@{induction hypothesis the property holds there}@}; consequently {@{both sides reduce into the same expression}@}.
> - If {@{$z > x$ and $z > y$ \($z$ is largest, i.e. $x < y < z$ or $y < x < z$\)}@} – {@{analogous reasoning applies to the left child}@}.
> - If {@{$x < z < y$ or $y < z <ｘ$ \($z$ is in the middle\)}@} – `incl(y)` {@{recurses into one child and "modifies" it}@}, while `incl(y).contains(x)` {@{recurses into the other "unmodified" child}@}; consequently {@{both side reduces into the same expression}@}.
>
> {@{All possible orderings of $(x, y, z)$ \(6 permutations\)}@} are covered, completing {@{the inductive proof}@}.

### proving set union property

{@{A natural extension}@} is to {@{add set union}@}:

> [!example] __`IntSet.union` definition__
>
> {@{A natural extension}@} is to {@{add set union}@}:
>
> ```Scala
> sealed abstract class IntSet {
>   def union(other: IntSet): IntSet
> }
> object Empty extends IntSet {
>   def union(other: IntSet) = other
> }
> case class NonEmpty(elem: Int, left: IntSet, right: IntSet) extends IntSet {
>   def union(other: IntSet) =
>     left.union(right.union(other)).incl(elem)
> }
> ```

{@{The correctness of `union`}@} can be expressed by {@{the following proposition}@}:

> [!example] __`IntSet.union` property__
>
> {@{The correctness of `union`}@} can be expressed by {@{the following proposition}@}:
>
> For {@{any sets $x$ and $y$ and element $e$}@}, {@{$$x.\text{union}(y).\text{contains}(e) = x.\text{contains}(e)\; \lor\; y.\text{contains}(e)$$}@}

The reader can {@{carry out the argument in detail}@}, or refer {@{to below}@}. The proof is more {@{difficult}@}. {@{The three properties above}@} only use {@{some properties of a binary tree}@} but not {@{those specific to a binary _search_ tree \(BST\)}@}. Indeed, the above three properties {@{still holds and can be proven very similarly}@} if `incl` {@{inserts `x` into both subtrees: `NonEmpty(elem, left.incl(x), right.incl(x))`}@}. The proof below, however, also {@{requires properties of a BST}@}. The trouble is that one needs to {@{additionally assume that only `Empty` and `incl` is used to build trees \(i.e. the constructor of `NonEmpty` cannot be used directly\)}@}, so that {@{any instances of `IntSet` are indeed BSTs}@}. {@{This required additional assumption}@} is {@{not very apparent}@}.

> [!example] __`IntSet.union` property proof: part 1__
>
> The proof proceeds by {@{structural induction}@} on {@{the first argument `x`}@}. The proof is {@{rather difficult}@}; see {@{the previous paragraph}@}.
>
> {@{_Base:_}@} if {@{`x` is `Empty`}@}, then {@{`union` returns `y`}@}; membership reduces to {@{`y.contains(e)`}@}. The right hand side {@{reduces to the same expression}@} because {@{`x.contains(e)` evaluates to `false`}@}.
>
> {@{_Inductive step:_}@} for {@{a node `NonEmpty(z, l, r)`}@}, assume {@{the inductive property holds for `l` and `r`}@}, i.e. {@{`l.union(y).contains(e) == l.contains(e) || y.contains(e)` and similarly for `r`}@}. We must show that
>
> ```Scala
> NonEmpty(z, l, r).union(y).contains(e) == NonEmpty(z, l, r).contains(e) || y.contains(e)
> ```
>
> One expands {@{the left hand side}@} to {@{`l.union(r.union(y)).incl(z).contains(e)`}@}.
>
> - If {@{`z == e`}@}, then {@{both sides easily reduce to `true`}@}.
> - If {@{`z != e`}@}, then the above can be reduced to {@{`l.union(r.union(y)).contains(e)`}@} by that {@{non-insertion preserves membership}@}. Then apply {@{the inductive hypothesis twice}@}: {@{`l.contains(e) || r.union(y).contains(e)`, and then `l.contains(e) || r.contains(e) || y.contains(e)`}@}. Extracting {@{common subexpressions}@}, what remains to show is that {@{`l.contains(e) || r.contains(e) == NonEmpty(z, l, r).contains(e)`}@}.

<!-- markdownlint MD028 -->

> [!example] __`IntSet.union` property proof: part 2__
>
> To prove {@{the above assuming `z != e`}@}, {@{split cases on `z > e` and `z < e`}@}.
>
> - If {@{`z > e`}@}, then {@{RHS reduces to `l.contains(e)`}@}. We need to show {@{`r.contains(e)` is `false` to reduce LHS to the same expression}@}. This requires {@{an additional property coming from that `NonEmpty` is a binary _search_ tree}@} if {@{they are constructed _exclusively_ using `Empty` and then `incl`}@}. See {@{the part below}@}.
> - If {@{`z < e`}@}, the proof is {@{analogous}@}.

<!-- markdownlint MD028 -->

> [!example] __`IntSet.union` property proof: part 3__
>
> We need to prove {@{an additional property coming from that `NonEmpty` is a binary _search_ tree}@} if {@{they are constructed _exclusively_ using `Empty` and then `incl`}@}. {@{This restriction is required}@} because {@{`NonEmpty(z, l, r)` is not necessarily a BST}@} if it is {@{directly constructed from arbitrarily trees `l` and `r`}@}.
>
> First we observe that {@{`incl` does not change the element in the root node}@}. So the only way to {@{obtain a `NonEmpty(z, l, r)`}@} is by {@{starting with `Empty.incl(z) == NonEmpty(z, Empty, Empty)`}@}. We can perform {@{another induction}@}, starting with {@{`NonEmpty(z, Empty, Empty)` and _exclusively_ using `incl` to build up the `IntSet`}@}
>
> - {@{_Base case_}@}: Consider {@{`NonEmpty(z, Empty, Empty).contains(e)`}@}, which {@{clearly satisfies `r.contains(e) == False`}@}.
> - {@{_Inductive step_}@}: Then, no matter {@{what the `x` in `incl(x)` is}@}, we only have {@{`NonEmpty(z, l, r.incl(x))` when `x > z`}@}. Then {@{`r.incl(x).contains(e) == r.contains(e) == false`}@} since {@{`x > z > e` and by induction hypothesis `r.contains(e) == false`}@}.
>
> This {@{finishes the proof}@}.
