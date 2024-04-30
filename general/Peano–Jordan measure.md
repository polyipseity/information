---
aliases:
  - Jordan content
  - Jordan contents
  - Jordan measure
  - Jordan measures
  - Peano–Jordan content
  - Peano–Jordan contents
  - Peano–Jordan measure
  - Peano–Jordan measures
tags:
  - flashcard/general/Peano-Jordan_measure
  - language/in/English
---

# Peano–Jordan measure

## simple sets

Consider {{$n$-dimensional [Euclidean space](Euclidean%20space.md) $\mathbb{R}^n$}}. Jordan measure is first defined on {{_<!-- LaTeX separator -->$n$-dimensional rectangles_ that are [Cartesian products](Cartesian%20product.md) of [bounded](bounded%20set.md) closed-on-the-left open-on-the-right [intervals](interval%20(mathematics).md)}}: <!--SR:!2024-09-14,157,310!2024-09-30,168,310-->

$$R := [a_1, b_1) \times [a_2, b_2) \times \cdots \times [a_n, b_n) \qquad a_i, b_i \in \mathbb{R}, a_i < b_i$$

Note that the intervals being half-open is {{a technical choice and it could also be open or closed, as seen below in this section}}. When $n = 1, 2, 3$, a $n$-dimensional rectangle corresponds to {{respectively a [line segment](line%20segment.md), a [rectangle](rectangle.md), and a [cuboid](cuboid.md)}}. <!--SR:!2024-11-23,207,310!2025-01-13,265,330-->

Then, like how you calculate the length, area, or volume of the above familiar objects, the _Jordan measure_ of a rectangle is defined to be {{the product of the lengths of the intervals}}: <!--SR:!2024-11-03,209,330-->

$$m(R) := (b_1 - a_1) (b_2 - a_2) \cdots (b_n - a_n)$$

A _simple set_, or _polyrectangle_, is then {{finite [unions](union%20(set%20theory).md) of rectangles}}: <!--SR:!2024-08-14,132,290-->

$$S := R_1 \cup R_2 \cup \cdots \cup R_k \qquad k \ge 1$$

However, the Jordan measure of a simple set cannot be defined as {{the sum of measures of individual rectangles}}. This is because {{a simple set does not have an unique representation}}, and the different representations give {{inconsistent results if the above definition is used, as the amount of overlap can vary}}. <!--SR:!2024-12-11,239,330!2024-10-30,189,310!2025-01-09,260,330-->

> {{![finite union of 2D rectangles](../archives/Wikimedia%20Commons/Simple%20set1.png)}}
>
> {{finite union of 2D rectangles}} <!--SR:!2024-09-10,154,310!2024-05-24,74,343-->

The above can be fixed by {{rewriting any simple set as the union of mutually [disjoint](disjoint%20sets.md) rectangles}}. The half-open interval requirement makes this possible. In fact, this rewriting is always allowed. This can be seen by {{drawing several overlapping rectangles on a paper, then one can always find a way to cover the same area with non-overlapping rectangles}}. Then the Jordan measure of a simple set can be defined as {{the sum of measures of disjoint rectangles}}. <!--SR:!2024-09-25,174,310!2024-09-27,165,310!2024-09-09,153,310-->

> {{![rewritten union of disjoint rectangles](../archives/Wikimedia%20Commons/Simple%20set2.png)}}
>
> {{rewritten union of disjoint rectangles}} <!--SR:!2025-01-19,269,330!2024-05-20,70,343-->

One can show the above definition of Jordan measure for simple set is {{independent of the representation of simple set as disjoint rectangles, and the openness and closeness of the rectangles. They all give the same value for $m(S)$}}. In fact, the rectangles having disjoint [interior](interior%20(topology).md) suffices. <!--SR:!2024-09-18,160,310-->

## extension to more complicated sets

Using the above definition with half-open rectangles, {{notice that a closed rectangle is not a simple set, and neither is a $n$-dimensional ball}}. This shows {{the set of Jordan measurable sets, as currently defined, is very limited}}. <!--SR:!2024-08-10,138,310!2024-05-01,68,310-->

We can extend the above restricted definition by defining {{a bounded set to be _Jordan measurable_ if it is "well-approximated" by simple sets}}. <!--SR:!2024-09-30,180,310-->

Formally, {{for a bounded set $B$, define its _inner Jordan measure_ as the [supremum](infimum%20and%20supremum.md) of simple sets that are subsets of $B$ and _outer Jordan measure_ as the [infimum](infimum%20and%20supremum.md) of simple sets that are supersets of $B$}}: <!--SR:!2024-06-18,97,290-->

$$\begin{aligned}
m_*(B) := \sup_{S \subseteq B} m(S) \\
m^*(B) := \inf_{S \supseteq B} m(S)
\end{aligned}$$

> {{![squeezing a bounded set by simple sets](../archives/Wikimedia%20Commons/Jordan%20illustration.png)}}
>
> {{squeezing a bounded set by simple sets}} <!--SR:!2024-10-27,188,310!2024-05-16,66,343-->

If the inner Jordan measure equals the outer Jordan measure, then {{$B$ is said to be _Jordan measurable_ and its _Jordan measure_ is simply the common value of the inner and outer Jordan measures}}. Then the _Jordan measure_ is {{the [set function](set%20function.md) that maps Jordan measurable sets to their Jordan measures}}. <!--SR:!2024-11-20,222,330!2024-10-01,169,310-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Peano–Jordan_measure) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
