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

Area can be defined {@{from [axioms](axiom.md)}@}. Area is {@{a [function](function%20(mathematics).md) from a collection $M$ of measurable sets, for some definition of measurability, to the set of real numbers $\mathbb{R}$ ($a: M \to \mathbb{R}$) satisfying the following properties}@}: <!--SR:!2026-09-30,728,330!2026-03-21,505,270-->

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

- _(begin)_→::@::←[congruence](congruence%20(geometry).md) <!--SR:!2025-06-21,321,310!2027-05-24,908,330-->
- [congruence](congruence%20(geometry).md)→::@::←nonnegativity <!--SR:!2026-10-17,629,270!2025-11-12,379,230-->
- nonnegativity→::@::←rectangle <!--SR:!2025-06-02,292,250!2025-04-03,195,190-->
- rectangle→::@::←squeezing <!--SR:!2026-03-06,384,210!2025-10-05,261,230-->
- squeezing→::@::←subtraction <!--SR:!2025-10-24,261,170!2026-08-08,568,250-->
- subtraction→::@::←union and intersection <!--SR:!2026-12-14,657,270!2027-01-16,704,270-->
- union and intersection→::@::←_(end)_ <!--SR:!2025-07-18,349,290!2025-03-08,269,290-->

<!--/pytextgen-->

<!--pytextgen generate section="3b1a"--><!-- The following content is generated at 2024-06-09T08:10:15.008056+08:00. Any edits will be overridden! -->

- [congruence](congruence%20(geometry).md):@:If a set $S$ in $M$ is congruent (same shape and size) to $T$, then $T$ is in $M$ and $a(T) = a(S)$. <!--SR:!2026-11-19,765,330-->
- nonnegativity:@:For all set $S$ in $M$, $a(S) \ge 0$. <!--SR:!2028-02-18,1147,350-->
- rectangle:@:Every rectangle $R$ is in $M$ and a rectangle $R$ with width $w$ and height $h$ has area $a(R) = wh$. <!--SR:!2026-11-02,753,330-->
- squeezing:@:Let set $Q$ be squeezed in between two step regions $L$ and $U$, i.e. $L \subseteq Q \subseteq U$. A step region is a finite union of disjoint rectangles $R$, so $L$ and $U$ are in $M$ by the other axioms. If there exists an __unique__ number $c$ such that $a(L) \le c \le a(U)$ for all possible $L$ and $U$, then $Q$ is in $M$ and $a(Q) = M$. <!--SR:!2025-05-12,261,230-->
- subtraction:@:If two sets $S$ and $T$ are in $M$ with $S \subseteq T$, then $T \setminus S$ is in $M$ and $a(T \setminus S) = a(T) - a(S)$. <!--SR:!2027-01-31,801,310-->
- union and intersection:@:If two sets $S$ and $T$ are in $M$, then their union $S \cup T$ and their intersection $S \cap T$ are in $M$ and $a(S \cup T) = a(S) + a(T) - a(S \cap T).$ <!--SR:!2025-09-10,408,310-->

<!--/pytextgen-->

It can be proved that {@{such a function actually exists}@}. An example is {@{the [Jordan content](Peano–Jordan%20measure.md)}@}. However, it is {@{not a true [measure](measure%20(mathematics).md) and thus is less well-behaved with infinite countable sets, so [Lebesgue measure](Lebesgue%20measure.md) is more commonly used}@}. <!--SR:!2026-02-19,546,310!2028-05-04,1206,350!2027-05-19,806,290-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/area) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
