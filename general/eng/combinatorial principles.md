---
aliases:
  - combinatorial principle
  - combinatorial principles
tags:
  - flashcard/active/general/eng/combinatorial_principles
  - language/in/English
---

# combinatorial principles

In {@{proving results in [combinatorics](combinatorics.md)}@} {@{several useful __combinatorial rules__ or __combinatorial principles__ are commonly recognized and used}@}. <!--SR:!2025-10-27,291,330!2025-11-14,305,330-->

{@{The [rule of sum](addition%20principle.md), [rule of product](rule%20of%20product.md), and [inclusion–exclusion principle](inclusion–exclusion%20principle.md)}@} are often used for {@{[enumerative](enumerative%20combinatorics.md) purposes}@}. {@{[Bijective proofs](bijective%20proof.md)}@} are utilized to {@{demonstrate that two sets have the same [number of elements](cardinality.md)}@}. {@{The [pigeonhole principle](pigeonhole%20principle.md)}@} often {@{ascertains the existence of something or is used to determine the minimum or maximum number of something in a [discrete](discrete%20mathematics.md) context}@}. <!--SR:!2025-11-17,308,330!2029-06-11,1324,350!2025-11-15,306,330!2025-11-19,310,330!2029-06-01,1315,350!2026-05-06,381,290-->

{@{Many combinatorial identities}@} arise from {@{[double counting](double%20counting%20(proof%20technique).md) methods or the [method of distinguished element](method%20of%20distinguished%20element.md)}@}. {@{[Generating functions](generating%20function.md) and [recurrence relations](recurrence%20relation.md)}@} are {@{powerful tools that can be used to manipulate sequences, and can describe if not resolve many combinatorial situations}@}. <!--SR:!2025-11-20,311,330!2029-05-10,1297,350!2025-11-21,312,330!2025-11-19,310,330-->

## rule of sum

- see: [rule of sum](addition%20principle.md)

{@{The rule of sum}@} is {@{an intuitive principle}@} stating that if there are {@{_a_ possible outcomes for an event (or ways to do something) and _b_ possible outcomes for another event (or ways to do another thing)}@}, and {@{the two events cannot both occur (or the two things can't both be done)}@}, then there are {@{_a + b_ total possible outcomes for the events (or total possible ways to do one of the things)}@}. More formally, {@{the sum of the sizes of two [disjoint sets](disjoint%20sets.md)}@} is equal to {@{the size of their union}@}. <!--SR:!2029-06-02,1316,350!2028-06-09,957,330!2025-11-18,309,330!2026-01-15,305,290!2025-10-13,4,344!2025-10-13,4,344!2025-10-13,4,344-->

## rule of product

- see: [rule of product](rule%20of%20product.md)

{@{The rule of product}@} is {@{another intuitive principle}@} stating that if there are {@{_a_ ways to do something and _b_ ways to do another thing}@}, then there are {@{_a_ · _b_ ways to do both things}@}. <!--SR:!2026-12-28,613,330!2028-02-26,927,330!2025-11-21,312,330!2025-10-13,4,344-->

## inclusion–exclusion principle

- see: [inclusion–exclusion principle](inclusion–exclusion%20principle.md)

The inclusion–exclusion principle relates {@{the size of the union of multiple sets, the size of each set, and the size of each possible intersection of the sets}@}. The smallest example is {@{when there are two sets}@}: {@{the number of elements in the union of _A_ and _B_}@} is equal to {@{the sum of the number of elements in _A_ and _B_, minus the number of elements in their intersection}@}. <!--SR:!2026-04-04,399,310!2026-11-30,564,310!2028-03-01,927,330!2025-12-05,86,379-->

Generally, according to this principle, if {@{_A_<sub>1</sub>, …, _A<sub>n</sub>_ are finite sets}@}, then {@{$${\begin{aligned}\left|\bigcup _{i=1}^{n}A_{i}\right|&{}=\sum _{i=1}^{n}\left|A_{i}\right|-\sum _{i,j\,:\,1\leq i<j\leq n}\left|A_{i}\cap A_{j}\right|\\&{}\qquad +\sum _{i,j,k\,:\,1\leq i<j<k\leq n}\left|A_{i}\cap A_{j}\cap A_{k}\right|-\ \cdots \ +\left(-1\right)^{n-1}\left|A_{1}\cap \cdots \cap A_{n}\right|.\end{aligned} }$$}@} <!--SR:!2025-11-15,306,330!2029-05-19,1305,350-->

## rule of division

- see: [rule of division (combinatorics)](rule%20of%20division%20(combinatorics).md)

The rule of division states that {@{there are _n/d_ ways to do a task}@} if {@{it can be done using a procedure that can be carried out in _n_ ways}@}, and for {@{every way _w_, exactly _d_ of the _n_ ways of the procedure correspond to way _w_}@}. <!--SR:!2029-05-26,1310,350!2025-11-18,309,330!2029-05-27,1311,350-->

## bijective proof

- see: [bijective proof](bijective%20proof.md)

Bijective proofs prove that {@{two sets have the same number of elements}@} by {@{finding a [bijective function](bijection.md) (one-to-one correspondence) from one set to the other}@}. <!--SR:!2025-10-31,295,330!2028-02-23,925,330-->

## double counting

- see: [double counting (proof technique)](double%20counting%20(proof%20technique).md)

Double counting is {@{a technique that equates two expressions that count the size of a set in two ways}@}. <!--SR:!2025-10-29,293,330-->

## pigeonhole principle

- see: [pigeonhole principle](pigeonhole%20principle.md)

The pigeonhole principle states that if {@{_a_ items are each put into one of _b_ boxes, where _a_ > _b_}@}, then {@{one of the boxes contains more than one item}@}. Using this one can, for example, {@{demonstrate the existence of some element in a set with some specific properties}@}. <!--SR:!2025-10-30,294,330!2027-01-11,622,330!2025-11-14,305,330-->

## method of distinguished element

- see: [method of distinguished element](method%20of%20distinguished%20element.md)

The method of distinguished element {@{singles out a "distinguished element" of a set to prove some result}@}. <!--SR:!2025-11-16,307,330-->

## generating function

- see: [generating function](generating%20function.md)

Generating functions can be thought of as {@{polynomials with infinitely many terms whose coefficients correspond to terms of a sequence}@}. This new representation of the sequence {@{opens up new methods for finding identities and closed forms pertaining to certain sequences}@}. {@{The (ordinary) generating function of a sequence _a_<sub>_n_</sub>}@} is {@{$$G(a_{n};x)=\sum _{n=0}^{\infty }a_{n}x^{n}.$$}@} <!--SR:!2026-05-06,417,310!2028-01-12,903,330!2025-11-20,311,330!2025-11-17,308,330-->

## recurrence relation

- see: [recurrence relation](recurrence%20relation.md)

A recurrence relation {@{defines each term of a sequence in terms of the preceding terms}@}. Recurrence relations may {@{lead to previously unknown properties of a sequence}@}, but {@{generally [closed-form expressions](closed-form%20expression.md) for the terms of a sequence are more desired}@}. <!--SR:!2025-11-16,307,330!2025-10-28,292,330!2029-05-21,1306,350-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/combinatorial_principles) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- van Lint, J.H.; Wilson, R.M. (2001). _A Course in Combinatorics_ (2nd ed.). Cambridge University Press. [ISBN](ISBN.md) [0-521-00601-5](https://en.wikipedia.org/wiki/Special:BookSources/0-521-00601-5).
