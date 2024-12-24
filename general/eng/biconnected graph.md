---
aliases:
  - biconnected graph
  - biconnected graphs
tags:
  - flashcard/active/general/eng/biconnected_graph
  - language/in/English
---

# biconnected graph

| Relevant topics on <br/> [Graph connectivity](connectivity%20(graph%20theory).md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [Connectivity](connectivity%20(graph%20theory).md) <br/> - [Algebraic connectivity](algebraic%20connectivity.md) <br/> - [Cycle rank](cycle%20rank.md) <br/> - [Rank \(graph theory\)](rank%20(graph%20theory).md) <br/> - [SPQR tree](SPQR%20tree.md) <br/> - [St-connectivity](st-connectivity.md) <br/> - [Pixel connectivity](pixel%20connectivity.md) <br/> - [Vertex separator](vertex%20separator.md) <br/> - [Strongly connected component](strongly%20connected%20component.md) <br/> - __Biconnected graph__ <br/> - [Bridge](bridge%20(graph%20theory).md) |
<!-- -->
<!-- | - [v](https://en.wikipedia.org/wiki/Template:Graph%20connectivity%20sidebar) <br/> - [t](https://en.wikipedia.org/wiki/Template%20talk:Graph%20connectivity%20sidebar) <br/> - [e](https://en.wikipedia.org/wiki/Special:EditPage/Template%3AGraph%20connectivity%20sidebar) | -->

In {@{[graph theory](graph%20theory.md)}@}, a __biconnected graph__ is {@{a connected and "nonseparable" [graph](graph%20(discrete%20mathematics).md)}@}, meaning that {@{if any one [vertex](vertex%20(graph%20theory).md) were to be removed, the graph will remain connected}@}. Therefore {@{a biconnected graph has no [articulation vertices](biconnected%20component.md)}@}. <!--SR:!2024-12-26,4,272!2024-12-26,4,272!2024-12-26,4,270!2024-12-26,4,272-->

{@{The property of being [2-connected](k-vertex-connected%20graph.md)}@} is {@{equivalent to biconnectivity, except that the [complete graph](complete%20graph.md) of two vertices is usually not regarded as 2-connected}@}. <!--SR:!2024-12-26,4,272!2024-12-26,4,272-->

This property is especially {@{useful in maintaining a graph with a two-fold [redundancy](redundancy%20(engineering).md)}@}, to {@{prevent disconnection upon the removal of a single [edge](glossary%20of%20graph%20theory.md#edge) \(or connection\)}@}. <!--SR:!2024-12-26,4,272!2024-12-26,4,272-->

{@{The use of __biconnected__ graphs}@} is {@{very important in the field of networking \(see [Network flow](flow%20network.md)\)}@}, because of {@{this property of redundancy}@}. <!--SR:!2024-12-26,4,272!2024-12-26,4,272!2024-12-26,4,272-->

## definition

{@{A __biconnected__ [undirected graph](graph%20(discrete%20mathematics).md#undirected%20graph)}@} is {@{a connected graph that is not broken into disconnected pieces by deleting any single vertex \(and its incident edges\)}@}. <!--SR:!2024-12-26,4,272!2024-12-26,4,272-->

{@{A __biconnected__ [directed graph](directed%20graph.md)}@} is {@{one such that for any two vertices _v_ and _w_ there are two directed paths from _v_ to _w_ which have no vertices in common other than _v_ and _w_}@}. <!--SR:!2024-12-26,4,272!2024-12-25,3,252-->

## examples

> {@{![A biconnected graph on four vertices and four edges](../../archives/Wikimedia%20Commons/4%20Node%20Biconnected.svg)}@}
>
> {@{A biconnected graph on four vertices and four edges}@} <!--SR:!2024-12-26,4,272!2024-12-26,4,272-->

<!-- markdownlint MD028 -->

> {@{![A graph that is not biconnected. The removal of vertex x would disconnect the graph.](../../archives/Wikimedia%20Commons/4%20Node%20Not-Biconnected.svg)}@}
>
> {@{A graph that is not biconnected. The removal of vertex x would disconnect the graph.}@} <!--SR:!2024-12-26,4,272!2024-12-26,4,272-->

<!-- markdownlint MD028 -->

> {@{![A biconnected graph on five vertices and six edges](../../archives/Wikimedia%20Commons/5%20Node%20Biconnected.svg)}@}
>
> {@{A biconnected graph on five vertices and six edges}@} <!--SR:!2024-12-26,4,272!2024-12-26,4,272-->

<!-- markdownlint MD028 -->

> {@{![A graph that is not biconnected. The removal of vertex x would disconnect the graph.](../../archives/Wikimedia%20Commons/5%20Node%20Not-Biconnected.svg)}@}
>
> {@{A graph that is not biconnected. The removal of vertex x would disconnect the graph.}@} <!--SR:!2024-12-26,4,272!2024-12-26,4,272-->

__Nonseparable \(or 2-connected\) graphs \(or blocks\) with n nodes \(sequence {@{[A002218](https://oeis.org/A002218)}@} in the [OEIS](On-Line%20Encyclopedia%20of%20Integer%20Sequences.md)\)__ <!--SR:!2024-12-25,3,252-->

| Vertices | Number of Possibilities             |
|:--------:|:-----------------------------------:|
| __1__    | 0                                   |
| __2__    | 1                                   |
| __3__    | 1                                   |
| __4__    | 3                                   |
| __5__    | 10                                  |
| __6__    | 56                                  |
| __7__    | 468                                 |
| __8__    | 7123                                |
| __9__    | 194066                              |
| __10__   | 9743542                             |
| __11__   | 900969091                           |
| __12__   | 153620333545                        |
| __13__   | 48432939150704                      |
| __14__   | 28361824488394169                   |
| __15__   | 30995890806033380784                |
| __16__   | 63501635429109597504951             |
| __17__   | 244852079292073376010411280         |
| __18__   | 1783160594069429925952824734641     |
| __19__   | 24603887051350945867492816663958981 |

## structure of 2-connected graphs

{@{Every 2-connected graph}@} can be {@{constructed inductively by adding [paths](path%20(graph%20theory).md) to a [cycle](cycle%20(graph%20theory).md)}@} \([Diestel 2016](#CITEREFDiestel2016), p. 59\). <!--SR:!2024-12-26,4,272!2024-12-26,4,272-->

## see also

- [Biconnected component](biconnected%20component.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/biconnected_graph) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- Eric W. Weisstein. "Biconnected Graph." From MathWorld—A Wolfram Web Resource. [http://mathworld.wolfram.com/BiconnectedGraph.html](http://mathworld.wolfram.com/BiconnectedGraph.html)
- Paul E. Black, "biconnected graph", in Dictionary of Algorithms and Data Structures \[online\], Paul E. Black, ed., U.S. National Institute of Standards and Technology. 17 December 2004. \(accessed TODAY\) Available from: [https://xlinux.nist.gov/dads/HTML/biconnectedGraph.html](https://xlinux.nist.gov/dads/HTML/biconnectedGraph.html)
- <a id="CITEREFDiestel2016"></a> [Diestel, Reinhard](Reinhard%20Diestel.md) \(2016\), [_Graph Theory_](https://diestel-graph-theory.com/index.html) \(5th ed.\), Berlin, New York: Springer-Verlag, [ISBN](ISBN.md) [978-3-662-53621-6](https://en.wikipedia.org/wiki/Special:BookSources/978-3-662-53621-6).

## external links

- [The tree of the biconnected components Java implementation](https://code.google.com/p/jbpt/) in the jBPT library \(see BCTree class\).

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Graph families](https://en.wikipedia.org/wiki/Category:Graph%20families)
> - [Graph connectivity](https://en.wikipedia.org/wiki/Category:Graph%20connectivity)
