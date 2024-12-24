---
aliases:
  - area
tags:
  - flashcard/active/general/eng/area
  - language/in/English
---

# area

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

## formal definition

Area can be defined {@{from [axioms](axiom.md)}@}. Area is {@{a [function](function%20(mathematics).md) from a collection $M$ of measurable sets, for some definition of measurability, to the set of real numbers $\mathbb{R}$ ($a: M \to \mathbb{R}$) satisfying the following properties}@}:

```Python
# pytextgen generate data
from asyncio import gather as _gather
from itertools import chain as _chain
headers = "name", "description"
table = (
  (R"[congruence](congruence%20(geometry).md)", R"If a set $S$ in $M$ is congruent (same shape and size) to $T$, then $T$ is in $M$ and $a(T) = a(S)$.",),
  (R"nonnegativity", R"For all set $S$ in $M$, $a(S) \ge 0$.",),
  (R"rectangle", R"Every rectangle $R$ is in $M$ and a rectangle $R$ with width $w$ and height $h$ has area $a(R) = wh$.",),
  (R"squeezing", R"Let set $Q$ be squeezed in between two step regions $L$ and $U$, i.e. $L \subseteq Q \subseteq U$. A step region is a finite union of disjoint rectangles $R$, so $L$ and $U$ are in $M$ by the other axioms. If there exists an __unique__ number $c$ such that $a(L) \le c \le a(U)$ for all possible $L$ and $U$, then $Q$ is in $M$ and $a(Q) = M$.",),
  (R"subtraction", R"If two sets $S$ and $T$ are in $M$ with $S \subseteq T$, then $T \setminus S$ is in $M$ and $a(T \setminus S) = a(T) - a(S)$.",),
  (R"union and intersection", R"If two sets $S$ and $T$ are in $M$, then their union $S \cup T$ and their intersection $S \cap T$ are in $M$ and $a(S \cup T) = a(S) + a(T) - a(S \cap T).$",),
)
return _chain.from_iterable(await _gather(
  memorize_table(
    __env__.cwf_sects("2f02", "652a",),
    headers,
    table,
  ),
  memorize_map(
    __env__.cwf_sects(None, "3b1a", None,),
    items_to_map(*table),
  )
))
```

<!--pytextgen generate section="2f02"--><!-- The following content is generated at 2024-06-09T08:10:14.963380+08:00. Any edits will be overridden! -->

> | name | description |
> |-|-|
> | [congruence](congruence%20(geometry).md) | If a set $S$ in $M$ is congruent (same shape and size) to $T$, then $T$ is in $M$ and $a(T) = a(S)$. |
> | nonnegativity | For all set $S$ in $M$, $a(S) \ge 0$. |
> | rectangle | Every rectangle $R$ is in $M$ and a rectangle $R$ with width $w$ and height $h$ has area $a(R) = wh$. |
> | squeezing | Let set $Q$ be squeezed in between two step regions $L$ and $U$, i.e. $L \subseteq Q \subseteq U$. A step region is a finite union of disjoint rectangles $R$, so $L$ and $U$ are in $M$ by the other axioms. If there exists an __unique__ number $c$ such that $a(L) \le c \le a(U)$ for all possible $L$ and $U$, then $Q$ is in $M$ and $a(Q) = M$. |
> | subtraction | If two sets $S$ and $T$ are in $M$ with $S \subseteq T$, then $T \setminus S$ is in $M$ and $a(T \setminus S) = a(T) - a(S)$. |
> | union and intersection | If two sets $S$ and $T$ are in $M$, then their union $S \cup T$ and their intersection $S \cap T$ are in $M$ and $a(S \cup T) = a(S) + a(T) - a(S \cap T).$ |

<!--/pytextgen-->

<!--pytextgen generate section="652a"--><!-- The following content is generated at 2024-06-09T08:10:14.981729+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←[congruence](congruence%20(geometry).md)
- [congruence](congruence%20(geometry).md)→::@::←nonnegativity
- nonnegativity→::@::←rectangle
- rectangle→::@::←squeezing
- squeezing→::@::←subtraction
- subtraction→::@::←union and intersection
- union and intersection→::@::←_(end)_

<!--/pytextgen-->

<!--pytextgen generate section="3b1a"--><!-- The following content is generated at 2024-06-09T08:10:15.008056+08:00. Any edits will be overridden! -->

- [congruence](congruence%20(geometry).md):@:If a set $S$ in $M$ is congruent (same shape and size) to $T$, then $T$ is in $M$ and $a(T) = a(S)$.
- nonnegativity:@:For all set $S$ in $M$, $a(S) \ge 0$.
- rectangle:@:Every rectangle $R$ is in $M$ and a rectangle $R$ with width $w$ and height $h$ has area $a(R) = wh$.
- squeezing:@:Let set $Q$ be squeezed in between two step regions $L$ and $U$, i.e. $L \subseteq Q \subseteq U$. A step region is a finite union of disjoint rectangles $R$, so $L$ and $U$ are in $M$ by the other axioms. If there exists an __unique__ number $c$ such that $a(L) \le c \le a(U)$ for all possible $L$ and $U$, then $Q$ is in $M$ and $a(Q) = M$.
- subtraction:@:If two sets $S$ and $T$ are in $M$ with $S \subseteq T$, then $T \setminus S$ is in $M$ and $a(T \setminus S) = a(T) - a(S)$.
- union and intersection:@:If two sets $S$ and $T$ are in $M$, then their union $S \cup T$ and their intersection $S \cap T$ are in $M$ and $a(S \cup T) = a(S) + a(T) - a(S \cap T).$

<!--/pytextgen-->

It can be proved that {@{such a function actually exists}@}. An example is {@{the [Jordan content](Peano–Jordan%20measure.md)}@}. However, it is {@{not a true [measure](measure%20(mathematics).md) and thus is less well-behaved with infinite countable sets, so [Lebesgue measure](Lebesgue%20measure.md) is more commonly used}@}.

## references

This text incorporates [content](https://en.wikipedia.org/wiki/area) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
