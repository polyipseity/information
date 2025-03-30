---
aliases:
  - distance product
  - distance products
  - max-plus matrix multiplication
  - min-plus matrix multiplication
tags:
  - flashcard/active/general/eng/min-plus_matrix_multiplication
  - language/in/English
---

# min-plus matrix multiplication

<!-- | ![](../../archives/Wikimedia%20Commons/Text%20document%20with%20red%20question%20mark.svg) | This article includes a [list of references](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources), [related reading](https://en.wikipedia.org/wiki/Wikipedia:Further%20reading), or [external links](https://en.wikipedia.org/wiki/Wikipedia:External%20links), __but its sources remain unclear because it lacks [inline citations](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources#Inline%20citations)__. Please help [improve](https://en.wikipedia.org/wiki/Wikipedia:WikiProject%20Reliability) this article by [introducing](https://en.wikipedia.org/wiki/Wikipedia:When%20to%20cite) more precise citations. _\(November 2024\)__ \([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ | -->

{@{__Min-plus matrix multiplication__, also known as __distance product__}@}, is {@{an operation on [matrices](matrix%20(mathematics).md)}@}. <!--SR:!2025-08-19,171,310!2025-08-24,173,310-->

Given {@{two $n\times n$ matrices $A=(a_{ij})$ and $B=(b_{ij})$}@}, {@{their distance product $C=(c_{ij})=A\star B$}@} is defined as {@{an $n\times n$ matrix such that $c_{ij}=\min _{k=1}^{n}\{a_{ik}+b_{kj}\}$}@}. This is {@{standard matrix multiplication}@} for {@{the semi-ring of [tropical numbers](tropical%20geometry.md) in the min convention}@}. <!--SR:!2026-01-18,294,330!2025-10-19,203,310!2026-01-18,294,330!2026-01-18,294,330!2025-09-16,176,270-->

This operation is closely related to {@{the [shortest path problem](shortest%20path%20problem.md)}@}. If {@{$W$ is an $n\times n$ matrix containing the edge weights of a [graph](graph%20(discrete%20mathematics).md)}@}, then {@{$W^{k}$ gives the distances between vertices using paths of length at most $k$ edges}@}, and {@{$W^{n}$ is the [distance matrix](distance%20matrix.md) of the graph}@}. <!--SR:!2026-01-18,294,330!2025-10-20,204,310!2025-08-23,172,310!2026-01-18,294,330-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/min-plus_matrix_multiplication) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- [Uri Zwick](Uri%20Zwick.md). 2002. [All pairs shortest paths using bridging sets and rectangular matrix multiplication](http://doi.acm.org/10.1145/567112.567114). _J. ACM_ 49, 3 \(May 2002\), 289–317.
- Liam Roditty and Asaf Shapira. 2008. [All-Pairs Shortest Paths with a Sublinear Additive Error](https://dx.doi.org/10.1007/978-3-540-70575-8_51). ICALP '08, Part I, LNCS 5125, pp. 622–633, 2008.

## see also

- [Floyd–Warshall algorithm](Floyd–Warshall%20algorithm.md)
- [Tropical geometry](tropical%20geometry.md)

| ![graph theory stub](../../archives/Wikimedia%20Commons/Directed.svg) | _This [graph theory](graph%20theory.md)-related article is a [stub](https://en.wikipedia.org/wiki/Wikipedia:Stub). You can help Wikipedia by [expanding it](https://en.wikipedia.org/w/index.php?title=Min-plus_matrix_multiplication&action=edit)._ |

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Graph products](https://en.wikipedia.org/wiki/Category:Graph%20products)
> - [Graph distance](https://en.wikipedia.org/wiki/Category:Graph%20distance)
> - [Graph theory stubs](https://en.wikipedia.org/wiki/Category:Graph%20theory%20stubs)
