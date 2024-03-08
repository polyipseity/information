---
aliases:
  - area
tags:
  - flashcard/general/area
  - language/in/English
---

# area

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```

%%

## formal definition

Area can be defined {{from [axioms](axiom.md)}}. Area is {{a [function](function%20(mathematics).md) from a collection $M$ of measurable sets, for some definition of measurability, to the set of real numbers $\mathbb{R}$ ($a: M \to \mathbb{R}$) satisfying the following properties}}: <!--SR:!2024-04-14,55,310!2024-05-06,66,270-->

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather as _gather
from itertools import chain as _chain
headers = "name", "description"
table = (
  (R"[congruence](congruence%20(geometry).md)", R"If a set $S$ in $M$ is congruent (same shape and size) to $T$, then $T$ is in $M$ and $a(T) = a(S)$.",),
  (R"positivity", R"For all set $S$ in $M$, $a(S) \ge 0$.",),
  (R"rectangle", R"Every rectangle $R$ is in $M$ and a rectangle $R$ with width $w$ and height $h$ has area $a(R) = wh$.",),
  (R"squeezing", R"Let set $Q$ be squeezed in between two step regions $L$ and $U$, i.e. $L \subseteq Q \subseteq U$. A step region is a finite union of disjoint rectangles $R$, so $L$ and $U$ are in $M$ by the other axioms. If there exists an unique number $c$ such that $a(L) \le c \le a(U)$ for all possible $L$ and $U$, then $Q$ is in $M$ and $a(Q) = M$.",),
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2f02"--><!-- The following content is generated at 2024-02-06T17:29:09.681242+08:00. Any edits will be overridden! -->

> | name | description |
> |-|-|
> | [congruence](congruence%20(geometry).md) | If a set $S$ in $M$ is congruent (same shape and size) to $T$, then $T$ is in $M$ and $a(T) = a(S)$. |
> | positivity | For all set $S$ in $M$, $a(S) \ge 0$. |
> | rectangle | Every rectangle $R$ is in $M$ and a rectangle $R$ with width $w$ and height $h$ has area $a(R) = wh$. |
> | squeezing | Let set $Q$ be squeezed in between two step regions $L$ and $U$, i.e. $L \subseteq Q \subseteq U$. A step region is a finite union of disjoint rectangles $R$, so $L$ and $U$ are in $M$ by the other axioms. If there exists an unique number $c$ such that $a(L) \le c \le a(U)$ for all possible $L$ and $U$, then $Q$ is in $M$ and $a(Q) = M$. |
> | subtraction | If two sets $S$ and $T$ are in $M$ with $S \subseteq T$, then $T \setminus S$ is in $M$ and $a(T \setminus S) = a(T) - a(S)$. |
> | union and intersection | If two sets $S$ and $T$ are in $M$, then their union $S \cup T$ and their intersection $S \cap T$ are in $M$ and $a(S \cup T) = a(S) + a(T) - a(S \cap T).$ |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="652a"--><!-- The following content is generated at 2024-02-01T16:56:31.292229+08:00. Any edits will be overridden! -->

- _(begin)_→:::←[congruence](congruence%20(geometry).md) <!--SR:!2024-04-18,58,310!2024-05-01,68,310-->
- [congruence](congruence%20(geometry).md)→:::←positivity <!--SR:!2024-03-10,25,250!2024-03-31,26,210-->
- positivity→:::←rectangle <!--SR:!2024-04-19,47,250!2024-03-12,5,150-->
- rectangle→:::←squeezing <!--SR:!2024-03-14,13,210!2024-04-13,44,250-->
- squeezing→:::←subtraction <!--SR:!2024-03-18,10,150!2024-03-26,31,230-->
- subtraction→:::←union and intersection <!--SR:!2024-03-23,34,270!2024-03-15,23,230-->
- union and intersection→:::←_(end)_ <!--SR:!2024-04-04,42,290!2024-03-11,25,270-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="3b1a"--><!-- The following content is generated at 2024-02-06T17:29:09.663286+08:00. Any edits will be overridden! -->

- [congruence](congruence%20(geometry).md)::If a set $S$ in $M$ is congruent (same shape and size) to $T$, then $T$ is in $M$ and $a(T) = a(S)$. <!--SR:!2024-04-19,58,310-->
- positivity::For all set $S$ in $M$, $a(S) \ge 0$. <!--SR:!2024-04-20,59,310-->
- rectangle::Every rectangle $R$ is in $M$ and a rectangle $R$ with width $w$ and height $h$ has area $a(R) = wh$. <!--SR:!2024-04-17,57,310-->
- squeezing::Let set $Q$ be squeezed in between two step regions $L$ and $U$, i.e. $L \subseteq Q \subseteq U$. A step region is a finite union of disjoint rectangles $R$, so $L$ and $U$ are in $M$ by the other axioms. If there exists an unique number $c$ such that $a(L) \le c \le a(U)$ for all possible $L$ and $U$, then $Q$ is in $M$ and $a(Q) = M$. <!--SR:!2024-03-12,22,230-->
- subtraction::If two sets $S$ and $T$ are in $M$ with $S \subseteq T$, then $T \setminus S$ is in $M$ and $a(T \setminus S) = a(T) - a(S)$. <!--SR:!2024-03-14,20,270-->
- union and intersection::If two sets $S$ and $T$ are in $M$, then their union $S \cup T$ and their intersection $S \cap T$ are in $M$ and $a(S \cup T) = a(S) + a(T) - a(S \cap T).$ <!--SR:!2024-03-19,33,290-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

It can be proved that {{such a function actually exists}}. An example is {{the [Jordan content](Peano–Jordan%20measure.md)}}. However, it is {{not a true [measure](measure%20(mathematics).md) and thus is less well-behaved with infinite countable sets, so [Lebesgue measure](Lebesgue%20measure.md) is more commonly used}}. <!--SR:!2024-04-07,48,290!2024-04-24,62,310!2024-03-17,28,270-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/area) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
