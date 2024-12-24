---
aliases:
  - edge cover
  - edge covers
tags:
  - flashcard/active/general/eng/edge_cover
  - language/in/English
---

# edge cover

In {@{[graph theory](graph%20theory.md)}@}, an __edge cover__ of {@{a [graph](graph%20(discrete%20mathematics).md) is a set of [edges](glossary%20of%20graph%20theory.md#edge) such that every [vertex](vertex%20(graph%20theory).md) of the graph is incident to at least one edge of the set}@}. In {@{[computer science](computer%20science.md)}@}, the __minimum edge cover problem__ is {@{the problem of finding an edge cover of minimum size}@}. It is {@{an [optimization problem](optimization%20problem.md) that belongs to the class of [covering problems](covering%20problems.md)}@} and can be {@{solved in [polynomial time](time%20complexity.md#polynomial%20time)}@}. <!--SR:!2024-12-26,4,270!2024-12-25,3,250!2024-12-26,4,270!2024-12-26,4,270!2024-12-26,4,270!2024-12-25,3,250-->

> __[Covering/packing-problem pairs](linear%20programming.md#covering%2Fpacking%20dualities)__
>
> | __[Covering problems](covering%20problems.md)__ | __[Packing problems](packing%20problems.md)__                      |
> |:-----------------------------------------------:|:------------------------------------------------------------------:|
> | [Minimum set cover](set%20cover%20problem.md)   | [Maximum set packing](set%20packing.md)                            |
> | __Minimum edge cover__                          | [Maximum matching](matching%20(graph%20theory).md)                 |
> | [Minimum vertex cover](vertex%20cover.md)       | [Maximum independent set](independent%20set%20(graph%20theory).md) |
> | [Bin covering](bin%20covering%20problem.md)     | [Bin packing](bin%20packing%20problem.md)                          |
> | [Polygon covering](polygon%20covering.md)       | [Rectangle packing](rectangle%20packing.md)                        |
<!-- -->
<!-- | - [v](https://en.wikipedia.org/wiki/Template:Covering/packing-problem%20pairs) <br/> - [t](https://en.wikipedia.org/wiki/Template%20talk:Covering/packing-problem%20pairs) <br/> - [e](https://en.wikipedia.org/wiki/Special:EditPage/Template%3ACovering/packing-problem%20pairs) | -->

## definition

Formally, {@{an edge cover of a graph _G_}@} is {@{a set of edges _C_ such that each vertex in _G_ is incident with at least one edge in _C_}@}. The set _C_ is said to {@{_cover_ the vertices of _G_}@}. The following figure shows examples of edge coverings in two graphs \(the set _C_ is marked with red\). <p> {@{![examples of edge coverings in two graphs](../../archives/Wikimedia%20Commons/Edge-cover.svg)}@} <!--SR:!2024-12-25,3,250!2024-12-26,4,270!2024-12-26,4,270!2024-12-26,4,270-->

A __minimum edge covering__ is {@{an edge covering of smallest possible size}@}. {@{The __edge covering number__ _ρ_\(_G_\)}@} is {@{the size of a minimum edge covering}@}. The following figure shows examples of minimum edge coverings \(again, the set _C_ is marked with red\). <p> {@{![examples of minimum edge coverings](../../archives/Wikimedia%20Commons/Minimum-edge-cover.svg)}@} <!--SR:!2024-12-26,4,270!2024-12-25,3,250!2024-12-26,4,270!2024-12-25,3,250-->

Note that the figure on the right is {@{not only an edge cover but also a [matching](matching%20(graph%20theory).md)}@}. In particular, it is {@{a [perfect matching](perfect%20matching.md): a matching _M_ in which every vertex is incident with exactly one edge in _M_}@}. {@{A perfect matching \(if it exists\)}@} is {@{always a minimum edge covering}@}. <!--SR:!2024-12-26,4,270!2024-12-26,4,270!2024-12-26,4,270!2024-12-26,4,270-->

### examples

- The set of all edges ::@:: is an edge cover, assuming that there are no degree-0 vertices. <!--SR:!2024-12-26,4,270!2024-12-26,4,270-->
- The [complete bipartite graph](complete%20bipartite%20graph.md) _K<sub>m,n</sub>_ ::@:: has edge covering number max\(_m_, _n_\). <!--SR:!2024-12-26,4,270!2024-12-26,4,270-->

## algorithms

A smallest edge cover can be {@{found in [polynomial time](time%20complexity.md#polynomial%20time)}@} by {@{finding a [maximum matching](maximum%20cardinality%20matching.md) and extending it greedily so that all vertices are covered}@}.<sup>[\[1\]](#^ref-1)</sup><sup>[\[2\]](#^ref-2)</sup> In the following figure, {@{a maximum matching is marked with red}@}; {@{the extra edges that were added to cover unmatched nodes are marked with blue}@}. \({@{The figure on the right}@} {@{shows a graph in which a maximum matching is a [perfect matching](perfect%20matching.md)}@}; hence {@{it already covers all vertices and no extra edges were needed}@}.\) <p> {@{![examples of finding a maximum matching on two graphs](../../archives/Wikimedia%20Commons/Minimum-edge-cover-from-maximum-matching.svg)}@} <!--SR:!2024-12-26,4,270!2024-12-26,4,270!2024-12-26,4,270!2024-12-26,4,270!2024-12-26,4,270!2024-12-25,3,250!2024-12-26,4,270!2024-12-26,4,270-->

On the other hand, the related problem of {@{finding a smallest [vertex cover](vertex%20cover.md)}@} is {@{an [NP-hard](NP-hardness.md) problem}@}.<sup>[\[1\]](#^ref-1)</sup> <!--SR:!2024-12-26,4,270!2024-12-26,4,270-->

{@{Looking at the image}@} it already becomes obvious why, for {@{a given minimum edge cover $C$ and [maximum matching](maximum%20cardinality%20matching.md) $M$, letting $c$ and $m$ be the number of edges in $C$ and $M$ respectively}@}, we have:<sup>[\[3\]](#^ref-3)</sup> {@{$|V|=c+m$}@}. Indeed, {@{$C$ contains a maximum matching}@}, so {@{the edges of $C$ can be decomposed between the $m$ edges of a maximum matching, covering $2m$ vertices}@}, and {@{the $c-m$ other edges that each cover one other vertex}@}. Thus, as {@{$C$ covers all of the $|V|$ vertices, we have $|V|=2m+(c-m)$ giving the desired equality}@}. <!--SR:!2024-12-26,4,270!2024-12-26,4,270!2024-12-26,4,270!2024-12-26,4,270!2024-12-25,3,250!2024-12-26,4,270!2024-12-25,3,250-->

## see also

- [Vertex cover](vertex%20cover.md)
- [Set cover](set%20cover%20problem.md) – ::@:: the edge cover problem is a special case of the set cover problem: the elements of the _universe_ are vertices, and each _subset_ covers exactly two elements. <!--SR:!2024-12-25,3,250!2024-12-26,4,270-->

## notes

1. [Garey & Johnson \(1979\)](#CITEREFGareyJohnson1979), p. 79, uses edge cover and vertex cover as one example of a pair of similar problems, one of which can be solved in polynomial time while the other one is NP-hard. See also p. 190. <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFLawler2001"></a> Lawler, Eugene L. \(2001\), [_Combinatorial optimization: networks and matroids_](https://books.google.com/books?id=m4MvtFenVjEC&pg=PA222), Dover Publications, pp. 222–223, [ISBN](ISBN.md) [978-0-486-41453-9](https://en.wikipedia.org/wiki/Special:BookSources/978-0-486-41453-9). <a id="^ref-2"></a>^ref-2
3. ["Prove that the sum of minimum edge cover and maximum matching is the vertex count"](https://math.stackexchange.com/q/2187560). _Mathematics Stack Exchange_. Retrieved 2024-02-18. <a id="^ref-3"></a>^ref-3

## references

This text incorporates [content](https://en.wikipedia.org/wiki/edge_cover) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- <a id="CITEREFWeisstein"></a> [Weisstein, Eric W.](Eric%20W.%20Weisstein.md) ["Edge Cover"](https://mathworld.wolfram.com/EdgeCover.html). _[MathWorld](MathWorld.md)_.
- <a id="CITEREFGareyJohnson1979"></a> [Garey, Michael R.](Michael%20Garey.md); [Johnson, David S.](David%20S.%20Johnson.md) \(1979\), _[Computers and Intractability: A Guide to the Theory of NP-Completeness](Computers%20and%20Intractability.md)_, W.H. Freeman, [ISBN](ISBN.md) [0-7167-1045-5](https://en.wikipedia.org/wiki/Special:BookSources/0-7167-1045-5).

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Computational problems in graph theory](https://en.wikipedia.org/wiki/Category:Computational%20problems%20in%20graph%20theory)
> - [Polynomial-time problems](https://en.wikipedia.org/wiki/Category:Polynomial-time%20problems)
> - [Covering problems](https://en.wikipedia.org/wiki/Category:Covering%20problems)
