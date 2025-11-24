---
aliases:
  - _k_-edge-connected graph
  - _k_-edge-connected graphs
  - k-edge-connected graph
  - k-edge-connected graphs
tags:
  - flashcard/active/general/eng/k-edge-connected_graph
  - language/in/English
---

# k-edge-connected graph

In {@{[graph theory](graph%20theory.md)}@}, {@{a connected [graph](graph%20(discrete%20mathematics).md)}@} is ___k_-edge-connected__ if {@{it remains [connected](connectivity%20(graph%20theory).md) whenever fewer than _k_ edges are removed}@}. <!--SR:!2026-01-14,290,330!2025-12-06,259,330!2028-02-24,861,330-->

{@{The __edge-connectivity__ of a graph}@} is {@{the largest _k_ for which the graph is _k_-edge-connected}@}. <!--SR:!2026-01-20,294,330!2027-08-04,715,330-->

{@{Edge connectivity and the [enumeration](graph%20enumeration.md) of _k_-edge-connected graphs}@} was studied by {@{[Camille Jordan](Camille%20Jordan.md) in 1869}@}.<sup>[\[1\]](#^ref-1)</sup> <!--SR:!2026-12-10,492,310!2027-01-15,494,250-->

## formal definition

> {@{![A 2-edge-connected graph](../../archives/Wikimedia%20Commons/2-edge%20connected%20graph.svg)}@}
>
> {@{A 2-edge-connected graph}@} <!--SR:!2026-01-14,290,330!2026-01-14,290,330-->

Let {@{$G=(V,E)$ be an arbitrary graph}@}. If {@{the [subgraph](glossary%20of%20graph%20theory.md#subgraphs) $G'=(V,E\setminus X)$ is connected for all $X\subseteq E$ where $|X|<k$}@}, then {@{_G_ is said to be _k_-edge-connected}@}. {@{The edge connectivity of $G$}@} is {@{the maximum value _k_ such that _G_ is _k_-edge-connected}@}. {@{The smallest set _X_ whose removal disconnects _G_}@} is {@{a [minimum cut](minimum%20cut.md) in _G_}@}. <!--SR:!2025-12-10,262,330!2027-01-23,550,310!2025-12-22,272,330!2025-12-15,266,330!2028-02-26,863,330!2028-02-06,850,330!2029-01-30,1158,350-->

{@{The edge connectivity version of [Menger's theorem](Menger's%20theorem.md)}@} provides {@{an alternative and equivalent characterization, in terms of edge-disjoint paths in the graph}@}. {@{If and only if every two [vertices](vertex%20(graph%20theory).md) of _G_ form the endpoints of _k_ paths, no two of which share an edge with each other}@}, then {@{_G_ is _k_-edge-connected}@}. In one direction this is easy: {@{if a system of paths like this exists, then every set _X_ of fewer than _k_ edges is disjoint from at least one of the paths}@}, and {@{the pair of vertices remains connected to each other even after _X_ is deleted}@}. In the other direction, {@{the existence of a system of paths for each pair of vertices in a graph that cannot be disconnected by the removal of few edges}@} can be proven {@{using the [max-flow min-cut theorem](max-flow%20min-cut%20theorem.md) from the theory of [network flows](flow%20network.md)}@}. <!--SR:!2027-10-18,775,330!2027-01-28,551,310!2026-08-06,385,290!2025-12-31,278,330!2026-01-19,293,330!2026-01-20,294,330!2027-01-14,542,310!2027-10-24,779,330-->

## related concepts

{@{Minimum [vertex degree](degree%20(graph%20theory).md)}@} gives {@{a trivial upper bound on edge-connectivity}@}. That is, if {@{a graph $G=(V,E)$ is _k_-edge-connected}@} then {@{it is necessary that _k_ ≤ δ\(_G_\), where δ\(_G_\) is the minimum degree of any vertex _v_ ∈ _V_}@}. {@{Deleting all edges incident to a vertex _v_}@} would {@{disconnect _v_ from the graph}@}. <!--SR:!2025-12-16,267,330!2028-02-25,862,330!2029-02-10,1167,350!2027-05-03,581,310!2029-01-21,1150,350!2028-01-03,835,330-->

Edge connectivity is {@{the dual concept to [girth](girth%20(graph%20theory).md), the length of the shortest cycle in a graph}@}, in the sense that {@{the girth of a [planar graph](planar%20graph.md) is the edge connectivity of its [dual graph](dual%20graph.md), and vice versa}@}. These concepts are {@{unified in [matroid theory](matroid.md)}@} by {@{the [girth of a matroid](matroid%20girth.md), the size of the smallest dependent set in the matroid}@}. For {@{a [graphic matroid](graphic%20matroid.md)}@}, {@{the matroid girth equals the girth of the underlying graph}@}, while {@{for a co-graphic matroid it equals the edge connectivity}@}.<sup>[\[2\]](#^ref-2)</sup> <!--SR:!2027-10-26,780,330!2027-06-26,572,270!2027-08-19,730,330!2027-01-22,479,270!2026-01-19,293,330!2025-12-19,214,270!2026-12-30,512,290-->

{@{The 2-edge-connected graphs}@} can also be characterized by {@{the absence of [bridges](bridge%20(graph%20theory).md)}@}, by {@{the existence of an [ear decomposition](ear%20decomposition.md)}@}, or by {@{[Robbins' theorem](Robbins'%20theorem.md) according to which these are exactly the graphs that have a [strong orientation](strong%20orientation.md)}@}.<sup>[\[3\]](#^ref-3)</sup> <!--SR:!2025-12-11,263,330!2026-01-20,294,330!2026-01-20,294,330!2025-12-08,203,250-->

## computational aspects

There is {@{a polynomial-time algorithm}@} to {@{determine the largest _k_ for which a graph _G_ is _k_-edge-connected}@}. A simple algorithm would, {@{for every pair _\(u,v\)_, determine the [maximum flow](maximum%20flow%20problem.md) from _u_ to _v_ with the capacity of all edges in _G_ set to 1 for both directions}@}. {@{A graph is _k_-edge-connected}@} {@{if and only if the maximum flow from _u_ to _v_ is at least _k_ for any pair _\(u,v\)_}@}, so {@{_k_ is the least _u-v_-flow among all _\(u,v\)_}@}. <!--SR:!2025-12-02,255,330!2025-12-22,271,330!2025-12-20,270,330!2028-03-03,868,330!2025-12-19,269,330!2026-01-20,294,330-->

If {@{_n_ is the number of vertices in the graph}@}, this simple algorithm would {@{perform $O(n^{2})$ iterations of the Maximum flow problem, which can be solved in $O(n^{3})$ time}@}. Hence {@{the complexity of the simple algorithm described above is $O(n^{5})$ in total}@}. <!--SR:!2026-01-08,285,330!2028-01-28,843,330!2025-12-11,263,330-->

An improved algorithm will {@{solve the maximum flow problem for every pair _\(u,v\)_ where _u_ is arbitrarily fixed while _v_ varies over all vertices}@}. This {@{reduces the complexity to $O(n^{4})$}@} and is {@{sound since, if a [cut](cut%20(graph%20theory).md) of capacity less than _k_ exists, it is bound to separate _u_ from some other vertex}@}. It can be further improved by {@{an algorithm of [Gabow](Harold%20N.%20Gabow.md)}@} that runs in {@{worst case $O(n^{3})$ time}@}. <sup>[\[4\]](#^ref-4)</sup> <!--SR:!2025-12-28,276,330!2025-12-05,258,330!2027-06-10,610,310!2026-10-24,490,310!2026-08-16,437,310-->

{@{The Karger–Stein variant of [Karger's algorithm](Karger's%20algorithm.md)}@} provides {@{a faster [randomized algorithm](randomized%20algorithm.md) for determining the connectivity}@}, with {@{expected runtime $O(n^{2}\log ^{3}n)$}@}.<sup>[\[5\]](#^ref-5)</sup> <!--SR:!2025-12-27,233,250!2025-12-18,268,330!2026-03-30,229,210-->

A related problem: finding {@{the minimum _k_-edge-connected spanning subgraph of _G_}@} \(that is: select {@{as few as possible edges in _G_ that your selection is _k_-edge-connected}@}\) is {@{NP-hard for $k\geq 2$}@}.<sup>[\[6\]](#^ref-6)</sup> <!--SR:!2026-10-12,370,230!2027-12-09,805,330!2026-01-20,85,373-->

## see also

- [k-vertex-connected graph](k-vertex-connected%20graph.md)
- [Connectivity \(graph theory\)](connectivity%20(graph%20theory).md)
- [Matching preclusion](matching%20preclusion.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/k-edge-connected_graph) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFJordan1869"></a> [Jordan, Camille](Camille%20Jordan.md) \(1869\). ["Sur les assemblages de lignes"](http://resolver.sub.uni-goettingen.de/purl?GDZPPN002153998). _[Journal für die reine und angewandte Mathematik](Crelle's%20Journal.md)_ \(in French\). __70__ \(2\): 185–190. <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFChoChenDing2007"></a> Cho, Jung Jin; Chen, Yong; Ding, Yu \(2007\), "On the \(co\)girth of a connected matroid", _Discrete Applied Mathematics_, __155__ \(18\): 2456–2470, [doi](digital%20object%20identifier.md):[10.1016/j.dam.2007.06.015](https://doi.org/10.1016%2Fj.dam.2007.06.015), [MR](Mathematical%20Reviews.md) [2365057](https://mathscinet.ams.org/mathscinet-getitem?mr=2365057). <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFRobbins1939"></a> [Robbins, H. E.](Herbert%20Robbins.md) \(1939\). "A theorem on graphs, with an application to a problem on traffic control". _[American Mathematical Monthly](The%20American%20Mathematical%20Monthly.md)_. __46__ \(5\): 281–283. [doi](digital%20object%20identifier.md):[10.2307/2303897](https://doi.org/10.2307%2F2303897). [JSTOR](JSTOR.md#content) [2303897](https://www.jstor.org/stable/2303897). <a id="^ref-3"></a>^ref-3
4. [Harold N. Gabow](Harold%20N.%20Gabow.md). A matroid approach to finding edge connectivity and packing arborescences. _J. Comput. Syst. Sci._, 50\(2\):259–273, 1995. <a id="^ref-4"></a>^ref-4
5. <a id="CITEREFKargerStein1996"></a> [Karger, David R.](David%20Karger.md); [Stein, Clifford](Clifford%20Stein.md) \(1996\). ["A new approach to the minimum cut problem"](http://www.columbia.edu/~cs2035/courses/ieor6614.S09/Contraction.pdf) \(PDF\). _Journal of the ACM_. __43__ \(4\): 601. [doi](digital%20object%20identifier.md):[10.1145/234533.234534](https://doi.org/10.1145%2F234533.234534). <a id="^ref-5"></a>^ref-5
6. M.R. Garey and D.S. Johnson. _Computers and Intractability: a Guide to the Theory of NP-Completeness_. Freeman, San Francisco, CA, 1979. <a id="^ref-6"></a>^ref-6

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Graph connectivity](https://en.wikipedia.org/wiki/Category:Graph%20connectivity)
> - [Graph families](https://en.wikipedia.org/wiki/Category:Graph%20families)
