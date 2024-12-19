---
aliases:
  - distinguished element
  - distinguished elements
  - method of distinguished element
  - method of distinguished elements
tags:
  - flashcard/active/general/method_of_distinguished_element
  - language/in/English
---

# method of distinguished element

- "Distinguished element" redirects here. For {@{sets with pre-defined distinguished elements}@}, see {@{[pointed set](pointed%20set.md)}@}. <!--SR:!2025-01-10,70,310!2025-01-10,70,310-->

In the [mathematical](mathematics.md) field of {@{[enumerative combinatorics](enumerative%20combinatorics.md)}@}, {@{[identities](identity%20(mathematics).md) are sometimes established}@} by {@{arguments that rely on singling out one __"distinguished element"__ of a set}@}. <!--SR:!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310-->

## definition

Let {@{${\mathcal {A} }$ be a [family of subsets](family%20of%20sets.md) of the set $A$ and let $x\in A$ be a distinguished element of set $A$}@}. Then suppose {@{there is a [predicate](predicate%20(mathematical%20logic).md) $P(X,x)$ that relates a subset $X\subseteq A$ to $x$}@}. Denote {@{${\mathcal {A} }(x)$ to be the set of subsets $X$ from ${\mathcal {A} }$ for which $P(X,x)$ is true and ${\mathcal {A} }-\mathcal A(x)$ to be the set of subsets $X$ from ${\mathcal {A} }$ for which $P(X,x)$ is false}@}, then {@{${\mathcal {A} }(x)$ and ${\mathcal {A} }-\mathcal A(x)$ are disjoint sets}@}, so {@{by the method of summation, the cardinalities are additive}@}<sup>[\[1\]](#^ref-1)</sup> {@{$$|{\mathcal {A} }|=|{\mathcal {A} }(x)|+|{\mathcal {A} }-\mathcal A(x)|$$}@} Thus the distinguished element allows for {@{a decomposition according to a predicate that is a simple form of a [divide and conquer algorithm](divide-and-conquer%20algorithm.md)}@}. In combinatorics, this allows for {@{the construction of [recurrence relations](recurrence%20relation.md)}@}. Examples are in the next section. <!--SR:!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310-->

## examples

- {@{The [binomial coefficient](binomial%20coefficient.md) ${n \choose k}$}@} is {@{the number of size-_k_ subsets of a size-_n_ set}@}. A basic identity—one of whose consequences is that {@{the binomial coefficients are precisely the numbers appearing in [Pascal's triangle](pascal's%20triangle.md)}@}—states that: {@{$${n \choose k-1}+{n \choose k}={n+1 \choose k}.$$}@} <p> __Proof:__ In a size-(_n_ + 1) set, {@{choose one distinguished element}@}. The set of all size-_k_ subsets contains: {@{(1) all size-_k_ subsets that _do_ contain the distinguished element, and (2) all size-_k_ subsets that _do not_ contain the distinguished element}@}. If {@{a size-_k_ subset of a size-(_n_ + 1) set _does_ contain the distinguished element}@}, then {@{its other _k_ − 1 elements are chosen from among the other _n_ elements of our size-(_n_ + 1) set}@}. The number of ways to choose those is {@{therefore ${n \choose k-1}$}@}. If {@{a size-_k_ subset _does not_ contain the distinguished element}@}, then {@{all of its _k_ members are chosen from among the other _n_ "non-distinguished" elements}@}. The number of ways to choose those is {@{therefore ${n \choose k}$}@}.
- {@{The number of subsets of any size-_n_ set}@} is {@{2<sup>_n_</sup>}@}. <p> __Proof:__ We use {@{[mathematical induction](mathematical%20induction.md)}@}. The basis for induction is {@{the truth of this proposition in case _n_ = 0}@}. The [empty set](empty%20set.md) has {@{0 members and 1 subset, and 2<sup>0</sup> = 1}@}. The induction hypothesis is {@{the proposition in case _n_; we use it to prove case _n_ + 1}@}. In a size-(_n_ + 1) set, {@{choose a distinguished element}@}. Each subset {@{either contains the distinguished element or does not}@}. If {@{a subset contains the distinguished element}@}, then {@{its remaining elements are chosen from among the other _n_ elements}@}. By {@{the induction hypothesis, the number of ways to do that is 2<sup>_n_</sup>}@}. If {@{a subset does not contain the distinguished element}@}, then {@{it is a subset of the set of all non-distinguished elements}@}. By {@{the induction hypothesis, the number of such subsets is 2<sup>_n_</sup>}@}. Finally, the whole list of subsets of our size-(_n_ + 1) set contains {@{2<sup>_n_</sup> + 2<sup>_n_</sup> = 2<sup>_n_+1</sup> elements}@}.
- Let _B_<sub>_n_</sub> be {@{the _n_-th [Bell number](bell%20number.md), i.e., the number of [partitions of a set](partition%20of%20a%20set.md) of _n_ members}@}. Let _C_<sub>_n_</sub> be {@{the total number of "parts" (or "blocks", as combinatorialists often call them) among all partitions of that set}@}. For example, the partitions of the size-3 set {_a_, _b_, _c_} may be written thus: {@{$${\begin{matrix}abc\\a/bc\\b/ac\\c/ab\\a/b/c\end{matrix} }$$}@} We see {@{5 partitions, containing 10 blocks, so _B_<sub>3</sub> = 5 and _C_<sub>3</sub> = 10}@}. An identity states: {@{$$B_{n}+C_{n}=B_{n+1}.$$}@} <p> __Proof:__ In a size-(_n_ + 1) set, {@{choose a distinguished element}@}. In {@{each partition of our size-(_n_ + 1) set}@}, either {@{the distinguished element is a "singleton", i.e., the set containing _only_ the distinguished element is one of the blocks, or the distinguished element belongs to a larger block}@}. If {@{the distinguished element is a singleton}@}, then {@{deletion of the distinguished element leaves a partition of the set containing the _n_ non-distinguished elements}@}. There are {@{_B_<sub>_n_</sub> ways to do that}@}. If {@{the distinguished element belongs to a larger block}@}, then {@{its deletion leaves a block in a partition of the set containing the _n_ non-distinguished elements}@}. There are {@{_C_<sub>_n_</sub> such blocks}@}. <!--SR:!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-07-14,207,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-01-10,70,310!2025-03-12,98,270!2025-01-10,70,310!2025-01-10,70,310!2025-05-01,145,290!2025-01-10,70,310-->

## see also

- [combinatorial principles](combinatorial%20principles.md)
- [combinatorial proof](combinatorial%20proof.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/method_of_distinguished_element) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. Petkovšek, Marko; Tomaž Pisanski (November 2002). ["Combinatorial Interpretation of Unsigned Stirling and Lah Numbers"](http://www.imfm.si/preprinti/PDF/00837.pdf) (PDF). _University of Ljubljana preprint series_. __40__ (837): 1–6. Retrieved 12 July 2013. <a id="^ref-1"></a>^ref-1
