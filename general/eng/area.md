---
aliases:
  - area
tags:
  - flashcard/active/general/eng/area
  - language/in/English
---

# area

## formal definition

Area can be defined {@{from [axioms](axiom.md)}@}. Area is {@{a [function](function%20(mathematics).md) from a collection $M$ of measurable sets, for some definition of measurability}@}, to {@{the set of real numbers $\mathbb{R}$ ($a: M \to \mathbb{R}$) satisfying the following properties}@}: (annotation: 6 items: {{congruence, nonnegativity, rectangle}}, {{squeezing, subtraction, union and intersection}})

- [congruence](congruence%20(geometry).md) ::@:: If a set $S$ in $M$ is congruent (same shape and size) to $T$, then $T$ is in $M$ and $a(T) = a(S)$.
- nonnegativity ::@:: For all set $S$ in $M$, $a(S) \ge 0$.
- rectangle ::@:: Every rectangle $R$ is in $M$ and a rectangle $R$ with width $w$ and height $h$ has area $a(R) = wh$.
- squeezing ::@:: Let set $Q$ be squeezed in between two step regions $L$ and $U$, i.e. $L \subseteq Q \subseteq U$. A step region is a finite union of disjoint rectangles $R$, so $L$ and $U$ are in $M$ by the other axioms. If there exists an __unique__ number $c$ such that $a(L) \le c \le a(U)$ for all possible $L$ and $U$, then $Q$ is in $M$ and $a(Q) = M$.
- subtraction ::@:: If two sets $S$ and $T$ are in $M$ with $S \subseteq T$, then $T \setminus S$ is in $M$ and $a(T \setminus S) = a(T) - a(S)$.
- union and intersection ::@:: If two sets $S$ and $T$ are in $M$, then their union $S \cup T$ and their intersection $S \cap T$ are in $M$ and $a(S \cup T) = a(S) + a(T) - a(S \cap T).$

It can be proved that {@{such a (annotation: area) function actually exists}@}. An example is {@{the [Jordan content](Peano–Jordan%20measure.md)}@}. However, it is {@{not a true [measure](measure%20(mathematics).md) and thus is less well-behaved with infinite countable sets, so [Lebesgue measure](Lebesgue%20measure.md) is more commonly used}@}.

## references

This text incorporates [content](https://en.wikipedia.org/wiki/area) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
