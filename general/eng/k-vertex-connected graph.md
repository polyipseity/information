---
aliases:
  - _k_-vertex-connected graph
  - _k_-vertex-connected graphs
  - k-vertex-connected graph
  - k-vertex-connected graphs
tags:
  - flashcard/active/general/eng/k-vertex-connected_graph
  - language/in/English
---

# _k_-vertex-connected graph

> {@{![A graph with connectivity 4](../../archives/Wikimedia%20Commons/4-connected%20graph.svg)}@}
>
> {@{A graph with connectivity 4.}@} <!--SR:!2025-03-28,64,310!2025-03-31,67,310-->

In {@{[graph theory](graph%20theory.md)}@}, {@{a connected [graph](graph%20(discrete%20mathematics).md) _G_}@} is said to be {@{___k_-vertex-connected__ \(or ___k_-connected__\)}@} if {@{it has more than _k_ [vertices](vertex%20(graph%20theory).md) and remains [connected](connectivity%20(graph%20theory).md) whenever fewer than _k_ vertices are removed}@}. <!--SR:!2025-03-29,65,310!2025-03-31,67,310!2025-03-29,65,310!2025-03-27,63,310-->

{@{The __vertex-connectivity__, or just __connectivity__}@}, of {@{a graph is the largest _k_ for which the graph is _k_-vertex-connected}@}. <!--SR:!2025-03-29,65,310!2025-03-10,46,290-->

## definitions

{@{A graph \(other than a [complete graph](complete%20graph.md)\)}@} has {@{connectivity _k_ if _k_ is the size of the smallest subset of vertices such that the graph becomes disconnected if you delete them}@}.<sup>[\[1\]](#^ref-1)</sup> In {@{[complete graphs](complete%20graph.md)}@}, there is {@{no subset whose removal would disconnect the graph}@}. Some sources {@{modify the definition of connectivity to handle this case}@}, by {@{defining it as the size of the smallest subset of vertices whose deletion results in either a disconnected graph or a single vertex}@}. For this variation, {@{the connectivity of a complete graph $K_{n}$ is $n-1$}@}.<sup>[\[2\]](#^ref-2)</sup> <!--SR:!2025-03-28,64,310!2025-03-25,62,310!2025-03-30,66,310!2025-03-31,67,310!2025-03-26,63,310!2025-03-26,63,310!2025-03-23,60,310-->

An equivalent definition is that {@{a graph with at least two vertices is _k_-connected}@} if, {@{for every pair of its vertices, it is possible to find _k_ vertex-independent [paths](path%20(graph%20theory).md) connecting these vertices; see [Menger's theorem](Menger's%20theorem.md)}@} \([Diestel 2005](#CITEREFDiestel2005), p. 55\). This definition {@{produces the same answer, _n_ − 1, for the connectivity of the complete graph _K_<sub>_n_</sub>}@}.<sup>[\[1\]](#^ref-1)</sup> <!--SR:!2025-03-10,46,290!2025-04-22,73,270!2025-03-12,48,290-->

{@{A 1-connected graph is called [connected](connectivity%20(graph%20theory).md#connected%20vertices%20and%20graphs)}@}; {@{a 2-connected graph is called [biconnected](biconnected%20graph.md)}@}. {@{A 3-connected graph is called triconnected}@}. <!--SR:!2025-03-27,63,310!2025-03-23,60,310!2025-03-24,61,310-->

## applications

### components

Every graph {@{decomposes into a disjoint union of [1-connected components](component%20(graph%20theory).md)}@}. 1-connected graphs {@{decompose into a tree of [biconnected components](biconnected%20component.md)}@}. 2-connected graphs {@{decompose into a tree of [triconnected components](SPQR%20tree.md)}@}. <!--SR:!2025-03-30,66,310!2025-03-22,59,310!2025-03-07,44,290-->

### polyhedral combinatorics

{@{The 1-[skeleton](n-skeleton.md) (annotation: i.e. vertices and edges of the polytope represented as a graph) of any _k_-dimensional convex [polytope](polytope.md)}@} forms {@{a _k_-vertex-connected graph \([Balinski's theorem](Balinski's%20theorem.md)\)}@}.<sup>[\[3\]](#^ref-3)</sup> As {@{a partial converse, [Steinitz's theorem](Steinitz's%20theorem.md)}@} states that {@{any 3-vertex-connected [planar graph](planar%20graph.md) forms the skeleton of a convex [polyhedron](polyhedron.md)}@}. <!--SR:!2025-04-19,71,270!2025-02-20,24,230!2025-03-29,65,310!2025-05-08,80,270-->

## computational complexity

{@{The vertex-connectivity of an input graph _G_}@} can be {@{computed in polynomial time in the following way}@}<sup>[\[4\]](#^ref-4)</sup> consider {@{all possible pairs $(s,t)$ of nonadjacent nodes to disconnect}@}, using {@{[Menger's theorem](Menger's%20theorem.md) to justify that the minimal-size separator for $(s,t)$ is the number of pairwise vertex-independent paths between them}@}, encode the input by {@{doubling each vertex as an edge (annotation: Transform the undirected graph to a digraph by replacing each edge with a pair of directed edges. For each vertex, double it by replacing it with two vertices, one with the original incoming edges and the other with the original outgoing edges. Additionally, connect the former to the latter with a directed edge.)}@} to {@{reduce to a computation of the number of pairwise edge-independent paths}@}, and {@{compute the maximum number of such paths by computing the [maximum flow](maximum%20flow%20problem.md) in the graph between $s$ and $t$ with capacity 1 to each edge}@}, noting that {@{a flow of $k$ in this graph corresponds, by the [integral flow theorem](maximum%20flow%20problem.md#integral%20flow%20theorem), to $k$ pairwise edge-independent paths from $s$ to $t$}@}. <!--SR:!2025-03-30,66,310!2025-03-09,45,290!2025-06-13,115,290!2025-05-06,78,270!2025-03-11,47,290!2025-03-11,47,290!2025-03-08,44,290!2025-03-28,64,310-->

## properties

Let {@{_k≥2_}@}. <!--SR:!2025-03-27,63,310-->

- (annotation: _k≥2_) Every _k_-connected graph of order (annotation: i.e. number of vertices) at least $2k$ ::@:: contains a [cycle](cycle%20(graph%20theory).md) of length at least $2k$ <!--SR:!2025-03-23,50,250!2025-02-19,31,270-->
- (annotation: _k≥2_) In a _k_-connected graph, ::@:: any $k$ vertices in $G$ lie on a common [cycle](cycle%20(graph%20theory).md).<sup>[\[5\]](#^ref-5)</sup> <!--SR:!2025-05-10,81,270!2025-03-09,45,290-->

{@{The [cycle space](cycle%20space.md) of a 3-connected graph}@} is generated by {@{its non-separating [induced cycles](induced%20path.md)}@}. <sup>[\[6\]](#^ref-6)</sup> <!--SR:!2025-02-20,32,270!2025-04-09,58,270-->

## _k_-linked graph

{@{A graph with at least $2k$ vertices}@} is called ___k_-linked__ if {@{there are $k$ (vertex-)disjoint paths connecting $a_i$ to $b_i$ for any sequences $a_{1},\dots ,a_{k}$ and $b_{1},\dots ,b_{k}$ of $2k$ distinct vertices}@}. {@{Every _k_-linked graph}@} is {@{$(2k-1)$-connected graph, but not necessarily $2k$-connected}@}. <sup>[\[7\]](#^ref-7)</sup> <!--SR:!2025-02-27,39,290!2025-03-01,41,290!2025-03-22,59,310!2025-03-02,42,290-->

If {@{a graph is $2k$-connected and has average degree of at least $16k$}@}, then {@{it is $k$-linked}@}. <sup>[\[8\]](#^ref-8)</sup> <!--SR:!2025-03-14,43,250!2025-03-05,42,290-->

## see also

- [_k_-edge-connected graph](k-edge-connected%20graph.md)
- [Connectivity \(graph theory\)](connectivity%20(graph%20theory).md)
- [Menger's theorem](Menger's%20theorem.md)
- [Structural cohesion](structural%20cohesion.md)
- [Tutte embedding](Tutte%20embedding.md)
- [Vertex separator](vertex%20separator.md)

## notes

This text incorporates [content](https://en.wikipedia.org/wiki/k-vertex-connected_graph) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
`

1. <a id="CITEREFSchrijver2003"></a> Schrijver \(12 February 2003\), [_Combinatorial Optimization_](https://books.google.com/books?id=mqGeSQ6dJycC&q=%22k-vertex-connected+%22), Springer, [ISBN](ISBN.md) [9783540443896](https://en.wikipedia.org/wiki/Special:BookSources/9783540443896) <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFBeinekeBagga2021"></a> Beineke, Lowell W.; Bagga, Jay S. \(2021\), [_Line Graphs and Line Digraphs_](https://books.google.com/books?id=um1LEAAAQBAJ&pg=PA87), Developments in Mathematics, vol. 68, Springer Nature, p. 87, [ISBN](ISBN.md) [9783030813864](https://en.wikipedia.org/wiki/Special:BookSources/9783030813864) <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFBalinski1961"></a> [Balinski, M. L.](Michel%20Balinski.md) \(1961\), "On the graph structure of convex polyhedra in _n_-space", _[Pacific Journal of Mathematics](Pacific%20Journal%20of%20Mathematics.md)_, __11__ \(2\): 431–434, [doi](digital%20object%20identifier.md):[10.2140/pjm.1961.11.431](https://doi.org/10.2140%2Fpjm.1961.11.431). <a id="^ref-3"></a>^ref-3
4. _The algorithm design manual_, p 506, and _Computational discrete mathematics: combinatorics and graph theory with Mathematica_, p. 290-291 <a id="^ref-4"></a>^ref-4
5. [Diestel \(2016\)](#CITEREFDiestel2016), p.84 <a id="^ref-5"></a>^ref-5
6. [Diestel \(2012\)](#CITEREFDiestel2012), p.65. <a id="^ref-6"></a>^ref-6
7. [Diestel \(2016\)](#CITEREFDiestel2016), p.85 <a id="^ref-7"></a>^ref-7
8. [Diestel \(2016\)](#CITEREFDiestel2016), p.75 <a id="^ref-8"></a>^ref-8

## references

- <a id="CITEREFDiestel2005"></a> [Diestel, Reinhard](Reinhard%20Diestel.md) \(2005\), [_Graph Theory_](http://www.math.uni-hamburg.de/home/diestel/books/graph.theory/) \(3rd ed.\), Berlin, New York: Springer-Verlag, [ISBN](ISBN.md) [978-3-540-26183-4](https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-26183-4)
- <a id="CITEREFDiestel2012"></a> Diestel, Reinhard \(2012\), _Graph Theory_ \(corrected 4th electronic ed.\)
- <a id="CITEREFDiestel2016"></a> Diestel, Reinhard \(2016\), [_Graph Theory_](https://diestel-graph-theory.com/index.html) \(5th ed.\), Berlin, New York: Springer-Verlag, [ISBN](ISBN.md) [978-3-662-53621-6](https://en.wikipedia.org/wiki/Special:BookSources/978-3-662-53621-6)

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Graph connectivity](https://en.wikipedia.org/wiki/Category:Graph%20connectivity)
> - [Graph families](https://en.wikipedia.org/wiki/Category:Graph%20families)
