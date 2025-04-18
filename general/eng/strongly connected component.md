---
aliases:
  - SCC
  - SCCs
  - strongly connected component
  - strongly connected components
tags:
  - flashcard/active/general/eng/strongly_connected_component
  - language/in/English
---

# strongly connected component

> {@{![Graph with strongly connected components marked](../../archives/Wikimedia%20Commons/Scc-1.svg)}@}
>
> {@{Graph with strongly connected components marked}@}

| Relevant topics on <br/> [Graph connectivity](connectivity%20(graph%20theory).md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| - [Connectivity](connectivity%20(graph%20theory).md) <br/> - [Algebraic connectivity](algebraic%20connectivity.md) <br/> - [Cycle rank](cycle%20rank.md) <br/> - [Rank \(graph theory\)](rank%20(graph%20theory).md) <br/> - [SPQR tree](SPQR%20tree.md) <br/> - [St-connectivity](st-connectivity.md) <br/> - [Pixel connectivity](pixel%20connectivity.md) <br/> - [Vertex separator](vertex%20separator.md) <br/> - __Strongly connected component__ <br/> - [Biconnected graph](biconnected%20graph.md) <br/> - [Bridge](bridge%20(graph%20theory).md) |
<!-- -->
<!-- | - [v](https://en.wikipedia.org/wiki/Template:Graph%20connectivity%20sidebar) <br/> - [t](https://en.wikipedia.org/wiki/Template%20talk:Graph%20connectivity%20sidebar%20) <br/> - [e](https://en.wikipedia.org/wiki/Special:EditPage/Template:Graph%20connectivity%20sidebar) | -->

In {@{the [mathematical](mathematics.md) theory of [directed graphs](directed%20graph.md)}@}, {@{a graph is said to be __strongly connected__}@} if {@{every vertex is [reachable](reachability.md) from every other vertex}@}. {@{The __strongly connected components__ of a directed graph}@} form {@{a [partition](partition%20of%20a%20set.md) into [subgraphs](glossary%20of%20graph%20theory.md#subgraph) that are themselves strongly connected}@}. It is possible to {@{test the strong [connectivity](connectivity%20(graph%20theory).md) of a graph, or to find its strongly connected components}@}, in {@{[linear time](time%20complexity.md#linear%20time) \(that is, Θ\(<!-- markdown separator -->_V_ + _E_&hairsp;\)\)}@}.

## definitions

{@{A [directed graph](directed%20graph.md) is called __strongly connected__}@} if {@{there is a [path](path%20(graph%20theory).md) in each direction between each pair of vertices of the graph}@}. That is, {@{a path exists from the first vertex in the pair to the second, and another path exists from the second vertex to the first}@}. In {@{a directed graph _G_ that may not itself be strongly connected}@}, {@{a pair of vertices _u_ and _v_ are said to be strongly connected to each other}@} if {@{there is a path in each direction between them}@}.

{@{The [binary relation](binary%20relation.md) of being strongly connected}@} is {@{an [equivalence relation](equivalence%20relation.md)}@}, and {@{the [induced subgraphs](induced%20subgraph.md) of its [equivalence classes](equivalence%20class.md) are called __strongly connected components__<!-- markdown separator -->}@}. Equivalently, {@{a __strongly connected component__ of a directed graph _G_ is a subgraph that is strongly connected}@}, and {@{is [maximal](maximal%20and%20minimal%20elements.md) with this property}@}: {@{no additional edges or vertices from _G_ can be included in the subgraph without breaking its property of being strongly connected}@}. {@{The collection of strongly connected components}@} forms {@{a partition of the set of vertices of _G_<!-- markdown separator -->}@}. {@{A strongly connected component _C_ is called _trivial_}@} when {@{_C_ consists of a single vertex which is not connected to itself with an edge}@}, and {@{_non-trivial_ otherwise}@}.<sup>[\[1\]](#^ref-1)</sup>

> {@{![The yellow [directed acyclic graph](directed%20acyclic%20graph.md) is the condensation of the blue directed graph.](../../archives/Wikimedia%20Commons/Graph%20Condensation.svg)}@}
>
> {@{The yellow [directed acyclic graph](directed%20acyclic%20graph.md) is the condensation of the blue directed graph}@}. It is formed by {@{contracting each strongly connected component of the blue graph into a single yellow vertex}@}.

If {@{each strongly connected component is [contracted](edge%20contraction.md#vertex%20identification) to a single vertex}@}, {@{the resulting graph is a [directed acyclic graph](directed%20acyclic%20graph.md), the __condensation__ of _G_<!-- markdown separator -->}@}. A directed graph is {@{acyclic [if and only if](if%20and%20only%20if.md) it has no strongly connected subgraphs with more than one vertex}@}, because {@{a [directed cycle](cycle%20(graph%20theory).md) is strongly connected}@} and {@{every non-trivial strongly connected component contains at least one directed cycle}@}.

## algorithms

### DFS-based linear-time algorithms

{@{Several [algorithms](algorithm.md) based on [depth-first search](depth-first%20search.md)}@} compute {@{strongly connected components in linear time}@}.

- {@{[Kosaraju's algorithm](Kosaraju's%20algorithm.md)}@} uses {@{two passes of depth-first search}@}. The first, in {@{the original graph}@}, is used to {@{choose the order in which the outer loop of the second depth-first search tests vertices for having been visited already and [recursively](recursion.md) explores them if not}@}. The second depth-first search is on {@{the [transpose graph](transpose%20graph.md) (annotation: the transpose graph is the original graph but with all edges reversed) of the original graph}@}, and {@{each recursive exploration finds a single new strongly connected component}@}.<sup>[\[2\]](#^ref-2)</sup><sup>[\[3\]](#^ref-3)</sup> It is named after {@{[S. Rao Kosaraju](S.%20Rao%20Kosaraju.md)}@}, who {@{described it \(but did not publish his results\) in 1978}@}; {@{[Micha Sharir](Micha%20Sharir.md)}@} later {@{published it in 1981}@}.<sup>[\[4\]](#^ref-4)</sup>
- {@{[Tarjan's strongly connected components algorithm](Tarjan's%20strongly%20connected%20components%20algorithm.md)}@}, published by {@{[Robert Tarjan](Robert%20Tarjan.md) in 1972}@},<sup>[\[5\]](#^ref-5)</sup> performs {@{a single pass of depth-first search}@}. It maintains {@{a [stack](stack%20(abstract%20data%20type).md) of vertices that have been explored by the search but not yet assigned to a component}@}, and calculates {@{"low numbers" of each vertex \(an index number of the highest ancestor reachable in one step from a descendant of the vertex\)}@} which {@{it uses to determine when a set of vertices should be popped off the stack into a new component}@}.
- {@{The [path-based strong component algorithm](path-based%20strong%20component%20algorithm.md)}@} uses {@{a depth-first search, like Tarjan's algorithm, but with two stacks}@}. One of the stacks is used to {@{keep track of the vertices not yet assigned to components, while the other keeps track of the current path in the depth-first search tree}@}. {@{The first linear time version of this algorithm}@} was {@{published by [Edsger W. Dijkstra](Edsger%20W.%20Dijkstra.md) in 1976}@}.<sup>[\[6\]](#^ref-6)</sup>

Although {@{Kosaraju's algorithm is conceptually simple}@}, {@{Tarjan's and the path-based algorithm require only one depth-first search rather than two}@}.

### reachability-based algorithms

{@{Previous linear-time algorithms}@} are {@{based on depth-first search which is generally considered hard to parallelize}@}. {@{Fleischer et al.<sup>[\[7\]](#^ref-7)</sup> in 2000}@} proposed {@{a [divide-and-conquer](divide-and-conquer%20algorithm.md) approach based on [reachability](reachability.md) queries}@}, and such algorithms are usually called {@{reachability-based SCC algorithms}@}. The idea of this approach is to {@{pick a random pivot vertex and apply forward and backward reachability queries from this vertex}@}. The two queries {@{partition the vertex set into 4 subsets: vertices reached by both, either one, or none of the searches}@}. One can show that {@{a strongly connected component has to be contained in one of the subsets}@}. {@{The vertex subset reached by both searches}@} forms {@{a strongly connected component}@}, and {@{the algorithm then recurses on the other 3 subsets}@}.

{@{The expected sequential running time of this algorithm}@} is {@{shown to be O\(<!-- markdown separator -->_n_ log _n_<!-- markdown separator -->\), a factor of O\(log _n_<!-- markdown separator -->\) more than the classic algorithms}@}. The parallelism comes from: \(1\) {@{the reachability queries can be parallelized more easily}@} \(e.g. by {@{a [breadth-first search](breadth-first%20search.md) \(BFS\)}@}, and it can be fast if {@{the [diameter](distance%20(graph%20theory).md#diameter) of the graph is small}@}\); and \(2\) {@{the independence between the subtasks in the divide-and-conquer process}@}. This algorithm performs {@{well on real-world graphs}@},<sup>[\[3\]](#^ref-3)</sup> but {@{does not have theoretical guarantee on the parallelism}@} \(consider if {@{a graph has no edges}@}, {@{the algorithm requires O\(<!-- markdown separator -->_n_<!-- markdown separator -->\) levels of recursions}@}\).

{@{Blelloch et al.<sup>[\[8\]](#^ref-8)</sup> in 2016}@} shows that if {@{the reachability queries are applied in a random order}@}, {@{the cost bound of O\(<!-- markdown separator -->_n_ log _n_<!-- markdown separator -->\) still holds}@}. Furthermore, the queries then can be {@{batched in a prefix-doubling manner \(i.e. 1, 2, 4, 8 queries\)}@} and {@{run simultaneously in one round}@}. {@{The overall [span](analysis%20of%20parallel%20algorithms.md) of this algorithm}@} is {@{log<sub>2</sub> _n_ reachability queries}@}, which is {@{probably the optimal parallelism that can be achieved using the reachability-based approach}@}.

### generating random strongly connected graphs

{@{Peter M. Maurer}@} describes {@{an algorithm for generating random strongly connected graphs}@},<sup>[\[9\]](#^ref-9)</sup> based on {@{a modification of an algorithm for [strong connectivity augmentation](strong%20connectivity%20augmentation.md)}@}, the problem of {@{adding as few edges as possible to make a graph strongly connected}@}. When used in conjunction with {@{the Gilbert or Erdős-Rényi models with node relabelling}@}, the algorithm is capable of {@{generating any strongly connected graph on _n_ nodes, without restriction on the kinds of structures that can be generated}@}.

## applications

{@{Algorithms for finding strongly connected components}@} may be used to {@{solve [2-satisfiability](2-satisfiability.md) problems \(systems of Boolean variables with constraints on the values of pairs of variables\)}@}: as {@{[Aspvall, Plass & Tarjan \(1979\)](#CITEREFAspvallPlassTarjan1979) showed}@}, {@{a 2-satisfiability instance is unsatisfiable}@} {@{if and only if there is a variable _v_ such that _v_ and its negation are both contained}@} in the {@{same strongly connected component of the [implication graph](implication%20graph.md) of the instance}@}.<sup>[\[10\]](#^ref-10)</sup>

Strongly connected components are also used to {@{compute the [Dulmage–Mendelsohn decomposition](Dulmage–Mendelsohn%20decomposition.md)}@}, {@{a classification of the edges of a [bipartite graph](bipartite%20graph.md)}@}, according to {@{whether or not they can be part of a [perfect matching](perfect%20matching.md) in the graph}@}.<sup>[\[11\]](#^ref-11)</sup>

## related results

{@{A directed graph is strongly connected}@} {@{if and only if it has an [ear decomposition](ear%20decomposition.md)}@}, {@{a partition of the edges into a sequence of directed paths and cycles}@} such {@{that the first subgraph in the sequence is a cycle}@}, and {@{each subsequent subgraph is either a cycle sharing one vertex with previous subgraphs, or a path sharing its two endpoints with previous subgraphs}@}.

According to {@{[Robbins' theorem](Robbins'%20theorem.md)}@}, {@{an undirected graph}@} may be {@{[oriented](orientation%20(graph%20theory).md) in such a way that it becomes strongly connected}@}, {@{if and only if it is [2-edge-connected](k-edge-connected%20graph.md)}@}. {@{One way to prove this result}@} is to {@{find an ear decomposition of the underlying undirected graph and then orient each ear consistently}@}.<sup>[\[12\]](#^ref-12)</sup>

## see also

- [clique \(graph theory\)](clique%20(graph%20theory).md)
- [connected component \(graph theory\)](component%20(graph%20theory).md)
- [modular decomposition](modular%20decomposition.md)
- [weak component](weak%20component.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/strongly_connected_component) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFNuutilaSoisalon-Soininen1994"></a> Nuutila, Esko; Soisalon-Soininen, Eljas \(1994\), "On finding the strongly connected components in a directed graph", _Information Processing Letters_, __49__ \(1\): 9–14, [doi](digital%20object%20identifier.md):[10.1016/0020-0190\(94\)90047-7](https://doi.org/10.1016%2F0020-0190%2894%2990047-7) <a id="^ref-1"></a>^ref-1
2. [Thomas H. Cormen](Thomas%20H.%20Cormen.md), [Charles E. Leiserson](Charles%20E.%20Leiserson.md), [Ronald L. Rivest](Ron%20Rivest.md), and [Clifford Stein](Clifford%20Stein.md). _[Introduction to Algorithms](Introduction%20to%20Algorithms.md)_, Second Edition. MIT Press and McGraw-Hill, 2001. [ISBN](ISBN.md) [0-262-03293-7](https://en.wikipedia.org/wiki/Special:BookSources/0-262-03293-7). Section 22.5, pp. 552–557. <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFHongRodiaOlukotun2013"></a> Hong, Sungpack; Rodia, Nicole C.; Olukotun, Kunle \(2013\), ["On fast parallel detection of strongly connected components \(SCC\) in small-world graphs"](https://ppl.stanford.edu/papers/sc13-hong.pdf) \(PDF\), _Proceedings of the International Conference on High Performance Computing, Networking, Storage and Analysis - SC '13_, pp. 1–11, [doi](digital%20object%20identifier.md):[10.1145/2503210.2503246](https://doi.org/10.1145%2F2503210.2503246), [ISBN](ISBN.md) [9781450323789](https://en.wikipedia.org/wiki/Special:BookSources/9781450323789), [S2CID](Semantic%20Scholar.md#S2CID) [2156324](https://api.semanticscholar.org/CorpusID:2156324) <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFSharir1981"></a> [Sharir, Micha](Micha%20Sharir.md) \(1981\), "A strong-connectivity algorithm and its applications in data flow analysis", _Computers & Mathematics with Applications_, __7__: 67–72, [doi](digital%20object%20identifier.md):[10.1016/0898-1221\(81\)90008-0](https://doi.org/10.1016%2F0898-1221%2881%2990008-0) <a id="^ref-4"></a>^ref-4
5. <a id="CITEREFTarjan1972"></a> [Tarjan, R. E.](Robert%20Tarjan.md) \(1972\), "Depth-first search and linear graph algorithms", _[SIAM Journal on Computing](SIAM%20Journal%20on%20Computing.md)_, __1__ \(2\): 146–160, [doi](digital%20object%20identifier.md):[10.1137/0201010](https://doi.org/10.1137%2F0201010), [S2CID](Semantic%20Scholar.md#S2CID) [16467262](https://api.semanticscholar.org/CorpusID:16467262) <a id="^ref-5"></a>^ref-5
6. <a id="CITEREFDijkstra1976"></a> [Dijkstra, Edsger](Edsger%20W.%20Dijkstra.md) \(1976\), _A Discipline of Programming_, NJ: Prentice Hall, Ch. 25. <a id="^ref-6"></a>^ref-6
7. <a id="CITEREFFleischerHendricksonPınar2000"></a> Fleischer, Lisa K.; Hendrickson, Bruce; Pınar, Ali \(2000\), ["On Identifying Strongly Connected Components in Parallel"](https://cfwebprod.sandia.gov/cfdocs/CompResearch/docs/irreg00.pdf) \(PDF\), _Parallel and Distributed Processing_, Lecture Notes in Computer Science, vol. 1800, pp. 505–511, [doi](digital%20object%20identifier.md):[10.1007/3-540-45591-4\_68](https://doi.org/10.1007%2F3-540-45591-4_68), [ISBN](ISBN.md) [978-3-540-67442-9](https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-67442-9) <a id="^ref-7"></a>^ref-7
8. <a id="CITEREFBlellochGuShunSun2016"></a> Blelloch, Guy E.; Gu, Yan; Shun, Julian; Sun, Yihan \(2016\), ["Parallelism in Randomized Incremental Algorithms"](https://people.csail.mit.edu/guyan/paper/SPAA16/Incremental.pdf) \(PDF\), _Proceedings of the 28th ACM Symposium on Parallelism in Algorithms and Architectures - SPAA '16_, pp. 467–478, [doi](digital%20object%20identifier.md):[10.1145/2935764.2935766](https://doi.org/10.1145%2F2935764.2935766), [hdl](Handle%20System.md):[1721.1/146176](https://hdl.handle.net/1721.1%2F146176), [ISBN](ISBN.md) [9781450342100](https://en.wikipedia.org/wiki/Special:BookSources/9781450342100). <a id="^ref-8"></a>^ref-8
9. <a id="CITEREFMaurer, P. M.2018"></a> Maurer, P. M. \(February 2018\), [_Generating strongly connected random graphs_](https://csce.ucmss.com/cr/books/2017/LFS/CSREA2017/MSV3359.pdf) \(PDF\), Int'l Conf. Modeling, Sim. and Vis. Methods MSV'17, CSREA Press, [ISBN](ISBN.md) [978-1-60132-465-8](https://en.wikipedia.org/wiki/Special:BookSources/978-1-60132-465-8), retrieved December 27, 2019 <a id="^ref-9"></a>^ref-9
10. <a id="CITEREFAspvallPlassTarjan1979"></a> Aspvall, Bengt; Plass, Michael F.; [Tarjan, Robert E.](Robert%20Tarjan.md) \(1979\), "A linear-time algorithm for testing the truth of certain quantified boolean formulas", _Information Processing Letters_, __8__ \(3\): 121–123, [doi](digital%20object%20identifier.md):[10.1016/0020-0190\(79\)90002-4](https://doi.org/10.1016%2F0020-0190%2879%2990002-4). <a id="^ref-10"></a>^ref-10
11. <a id="CITEREFDulmageMendelsohn1958"></a> Dulmage, A. L. & [Mendelsohn, N. S.](Nathan%20Mendelsohn.md) \(1958\), "Coverings of bipartite graphs", _Can. J. Math._, __10__: 517–534, [doi](digital%20object%20identifier.md):[10.4153/cjm-1958-052-0](https://doi.org/10.4153%2Fcjm-1958-052-0), [S2CID](Semantic%20Scholar.md#S2CID) [123363425](https://api.semanticscholar.org/CorpusID:123363425). <a id="^ref-11"></a>^ref-11
12. <a id="CITEREFRobbins1939"></a> [Robbins, H. E.](Herbert%20Robbins.md) \(1939\), "A theorem on graphs, with an application to a problem on traffic control", _[American Mathematical Monthly](The%20American%20Mathematical%20Monthly.md)_, __46__ \(5\): 281–283, [doi](digital%20object%20identifier.md):[10.2307/2303897](https://doi.org/10.2307%2F2303897), [JSTOR](JSTOR.md) [2303897](https://www.jstor.org/stable/2303897). <a id="^ref-12"></a>^ref-12

## external links

- [Java implementation for computation of strongly connected components](https://code.google.com/p/jbpt/) in the jBPT library \(see StronglyConnectedComponents class\).
- [C++ implementation of Strongly Connected Components](http://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/)
