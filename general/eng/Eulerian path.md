---
aliases:
  - Eulerian circuit
  - Eulerian circuits
  - Eulerian cycle
  - Eulerian cycles
  - Eulerian path
  - Eulerian paths
  - Eulerian walk
  - Eulerian walks
tags:
  - flashcard/active/general/eng/Eulerian_path
  - language/in/English
---

# Eulerian path

> {@{![[multigraphs](multigraph.md) of [Königsberg Bridges](Seven%20Bridges%20of%20Königsberg.md) and [five room puzzles](five-room%20puzzle.md)](../../archives/Wikimedia%20Commons/Comparison%207%20bridges%20of%20Konigsberg%205%20room%20puzzle%20graphs.svg)}@}
>
> {@{[Multigraphs](multigraph.md)}@} of {@{both [Königsberg Bridges](Seven%20Bridges%20of%20Königsberg.md) and [Five room puzzles](five-room%20puzzle.md)}@} have {@{more than two odd vertices \(in orange\)}@}, thus {@{are not Eulerian and hence the puzzles have no solutions}@}. <!--SR:!2026-02-04,347,362!2029-03-21,1237,362!2026-03-19,380,362!2025-12-16,301,336!2027-12-10,863,350-->

<!-- markdownlint MD028 -->

> ![a labeled Eulerian graph](../../archives/Wikimedia%20Commons/Labelled%20Eulergraph.svg)
>
> {@{Every vertex of this graph}@} has {@{an even degree}@}. Therefore, {@{this is an Eulerian graph}@}. {@{Following the edges in alphabetical order}@} gives {@{an Eulerian circuit/cycle}@}. <!--SR:!2026-02-26,364,362!2026-02-23,361,362!2025-12-15,301,336!2026-03-05,369,362!2026-03-21,382,362-->

In [graph theory](graph%20theory.md), {@{an __Eulerian trail__ \(or __Eulerian path__\)}@} is {@{a [trail](path%20(graph%20theory).md#walk,%20trail,%20and%20path) in a finite [graph](graph%20(discrete%20mathematics).md) that visits every [edge](glossary%20of%20graph%20theory.md#edge) exactly once \(allowing for revisiting vertices\)}@}. Similarly, {@{an __Eulerian circuit__ or __Eulerian cycle__}@} is {@{an Eulerian trail that starts and ends on the same [vertex](vertex%20(graph%20theory).md)}@}. They were first {@{discussed by [Leonhard Euler](Leonhard%20Euler.md)}@} while {@{solving the famous [Seven Bridges of Königsberg](Seven%20Bridges%20of%20Königsberg.md) problem in 1736}@}. The problem can be stated mathematically like this: <!--SR:!2026-02-14,354,362!2028-09-19,1068,350!2028-12-28,1172,362!2026-03-22,383,362!2029-01-02,1153,350!2027-02-03,601,330-->

> Given {@{the graph in the image}@}, is it possible to {@{construct a [path](path%20(graph%20theory).md) \(or a [cycle](cycle%20(graph%20theory).md); i.e., a path starting and ending on the same vertex\) that visits each edge exactly once}@}? <!--SR:!2026-04-03,393,362!2026-03-11,373,362-->

Euler [proved](mathematical%20proof.md) that {@{a necessary condition for the existence of Eulerian circuits is that all vertices in the graph have an [even](parity%20(mathematics).md) [degree](degree%20(graph%20theory).md)}@}, and {@{stated without proof that [connected graphs](connectivity%20(graph%20theory).md) with all vertices of even degree have an Eulerian circuit}@}. {@{The first complete proof of this latter claim}@} was {@{published posthumously in 1873}@} by {@{[Carl Hierholzer](Carl%20Hierholzer.md)}@}.<sup>[\[1\]](#^ref-1)</sup> This is known as {@{__Euler's Theorem:__}@} <!--SR:!2028-04-08,966,362!2028-08-03,1059,362!2026-03-30,390,362!2026-05-29,403,310!2025-12-17,303,336!2026-03-18,380,362-->

> {@{__Euler's Theorem__}@} — {@{A connected graph has an Euler cycle}@} {@{[if and only if](if%20and%20only%20if.md) every vertex has even degree}@}. <!--SR:!2026-02-27,365,362!2026-02-13,355,362!2026-03-09,371,362-->

{@{The term __Eulerian graph__}@} has {@{two common meanings in graph theory}@}. One meaning is {@{a graph with an Eulerian circuit}@}, and the other is {@{a graph with every vertex of even degree}@}. These definitions {@{coincide for connected graphs}@}.<sup>[\[2\]](#^ref-2)</sup> <!--SR:!2025-12-12,299,336!2026-04-01,391,362!2026-04-07,397,362!2026-02-27,364,362!2026-03-10,374,362-->

For {@{the existence of Eulerian trails}@} it is {@{necessary that zero or two vertices have an [odd](parity%20(mathematics).md) degree}@}; this means {@{the Königsberg graph is _not_ Eulerian}@}. If {@{there are no vertices of odd degree}@}, {@{all Eulerian trails are circuits}@}. If {@{there are exactly two vertices of odd degree}@}, {@{all Eulerian trails start at one of them and end at the other}@}. {@{A graph that has an Eulerian trail but not an Eulerian circuit}@} is {@{called __semi-Eulerian__}@}. <!--SR:!2026-02-05,344,350!2026-03-04,368,362!2027-09-16,778,342!2026-03-06,370,362!2026-03-26,387,362!2029-02-02,1200,362!2026-04-04,394,362!2028-04-12,935,336!2025-12-16,302,336-->

## definition

{@{An __Eulerian trail__,<sup>[\[note 1\]](#^note-1)</sup> or __Euler walk__}@}, in {@{an [undirected graph](graph%20(discrete%20mathematics).md#undirected%20graph) is a walk that uses each edge exactly once}@}. If {@{such a walk exists}@}, the graph is {@{called __traversable__ or __semi-eulerian__}@}.<sup>[\[3\]](#^ref-3)</sup> <!--SR:!2026-03-29,388,362!2025-12-14,300,336!2025-11-16,263,342!2026-03-13,375,362-->

{@{An __Eulerian cycle__,<sup>[\[note 1\]](#^note-1)</sup> also called an __Eulerian circuit__ or __Euler tour__}@}, in {@{an undirected graph is a [cycle](cycle%20(graph%20theory).md) that uses each edge exactly once}@}. If {@{such a cycle exists}@}, the graph is {@{called __Eulerian__ or __unicursal__}@}.<sup>[\[4\]](#^ref-4)</sup> {@{The term "Eulerian graph"}@} is also sometimes {@{used in a weaker sense to denote a graph where every vertex has even degree}@}. For {@{finite [connected graphs](connectivity%20(graph%20theory).md#connected%20vertices%20and%20graphs) the two definitions are equivalent}@}, while {@{a possibly unconnected graph is Eulerian in the weaker sense}@} {@{if and only if each connected component has an Eulerian cycle}@}. <!--SR:!2026-02-28,365,362!2026-03-25,385,362!2026-03-19,381,362!2026-03-14,376,362!2029-03-11,1228,362!2026-07-26,452,322!2028-08-15,1055,350!2026-03-28,388,362!2026-04-01,392,362-->

For {@{[directed graphs](directed%20graph.md)}@}, "path" has to be {@{replaced with _[directed path](path%20(graph%20theory).md)_ and "cycle" with _[directed cycle](cycle%20(graph%20theory).md)_}@}. <!--SR:!2026-03-15,377,362!2026-04-08,398,362-->

{@{The definition and properties of Eulerian trails, cycles and graphs}@} are {@{valid for [multigraphs](multigraph.md)}@} as well. <!--SR:!2026-02-07,346,350!2025-12-15,300,336-->

{@{An __Eulerian orientation__}@} of {@{an undirected graph _G_ is an assignment of a direction to each edge of _G_}@} such that, {@{at each vertex _v_, the [indegree](directed%20graph.md#indegree%20and%20outdegree) of _v_ equals the [outdegree](directed%20graph.md#indegree%20and%20outdegree) of _v_}@}. {@{Such an orientation exists}@} for {@{any undirected graph in which every vertex has even degree}@}, and may be found by {@{constructing an Euler tour in each connected component of _G_ and then orienting the edges according to the tour}@}.<sup>[\[5\]](#^ref-5)</sup> {@{Every Eulerian orientation of a connected graph}@} is {@{a [strong orientation](strong%20orientation.md), an orientation that makes the resulting directed graph [strongly connected](strongly%20connected%20component.md)}@}. <!--SR:!2026-02-14,352,350!2026-03-15,377,362!2026-03-14,376,362!2026-03-25,386,362!2028-03-24,921,336!2027-11-13,823,342!2029-04-03,1248,362!2026-03-17,379,362-->

## properties

- An undirected graph has an Eulerian cycle ::@:: if and only if every vertex has even degree, and all of its vertices with nonzero degree belong to a single [connected component](component%20(graph%20theory).md).<sup>[\[6\]](#^ref-6)</sup> <!--SR:!2028-08-13,1042,350!2028-03-30,959,362-->
- An undirected graph can be decomposed into edge-disjoint [cycles](cycle%20(graph%20theory).md) ::@:: if and only if all of its vertices have even degree. So, a graph has an Eulerian cycle if and only if it can be decomposed into edge-disjoint cycles and its nonzero-degree vertices belong to a single connected component. <!--SR:!2027-09-20,749,342!2028-07-21,1049,362-->
- An undirected graph has an Eulerian trail ::@:: if and only if exactly zero or two vertices have odd degree, and all of its vertices with nonzero degree belong to a single connected component.<sup>[\[6\]](#^ref-6)</sup> <!--SR:!2025-11-12,259,342!2028-03-30,926,336-->
- A directed graph has an Eulerian cycle ::@:: if and only if every vertex has equal [in degree](degree%20(graph%20theory).md) and [out degree](degree%20(graph%20theory).md), and all of its vertices with nonzero degree belong to a single [strongly connected component](strongly%20connected%20component.md). <!--SR:!2028-03-27,923,336!2027-12-12,805,342-->
  - Equivalently, a directed graph has an Eulerian cycle ::@:: if and only if it can be decomposed into edge-disjoint [directed cycles](cycle%20(graph%20theory).md) and all of its vertices with nonzero degree belong to a single strongly connected component.<sup>[\[6\]](#^ref-6)</sup> <!--SR:!2028-07-20,1034,350!2028-04-24,905,342-->
- A directed graph has an Eulerian trail ::@:: if and only if at most one vertex has \([out-degree](degree%20(graph%20theory).md)\) − \([in-degree](degree%20(graph%20theory).md)\) = 1, at most one vertex has \(in-degree\) − \(out-degree\) = 1, every other vertex has equal in-degree and out-degree, and all of its vertices with nonzero degree belong to a single connected component of the underlying undirected graph.<sup>[\[6\]](#^ref-6)</sup> <!--SR:!2029-01-03,1153,350!2028-12-20,1142,350-->

## constructing Eulerian trails and circuits

> {@{![Eulerian trail puzzles](../../archives/Wikimedia%20Commons/Eulerian%20path%20puzzles.svg)}@}
>
> Using {@{Eulerian trails}@} to {@{solve puzzles involving drawing a shape with a continuous stroke}@}:
>
> 1. As {@{the [Haus vom Nikolaus puzzle](Haus%20vom%20Nikolaus.md) has two odd-degree vertices \(orange\)}@}, the trail {@{must start at one and end at the other}@}.
> 2. {@{A variant with four odd-degree vertices}@} has {@{no solution}@}.
> 3. If {@{there are no odd-degree vertices}@}, the trail {@{can start anywhere and forms an Eulerian cycle}@}.
> 4. {@{Loose ends}@} are {@{considered vertices of degree 1}@}.
> 5. The graph {@{must also be connected}@}. <!--SR:!2026-06-24,425,310!2025-12-13,298,336!2026-03-10,372,362!2028-04-12,896,342!2026-03-26,386,362!2028-10-03,1102,362!2026-02-11,353,362!2026-04-03,393,362!2029-02-08,1205,362!2028-07-18,1032,350!2026-02-02,346,362!2026-03-17,379,362-->

### Fleury's algorithm

{@{__Fleury's algorithm__}@} is {@{an elegant but inefficient algorithm that dates to 1883}@}.<sup>[\[7\]](#^ref-7)</sup> Consider {@{a graph known to have all edges in the same component and at most two vertices of odd degree}@}. The algorithm {@{starts at a vertex of odd degree, or, if the graph has none, it starts with an arbitrarily chosen vertex}@}. At each step it {@{chooses the next edge in the path to be one whose deletion would not disconnect the graph}@}, unless {@{there is no such edge, in which case it picks the remaining edge left at the current vertex}@}. It then {@{moves to the other endpoint of that edge and deletes the edge}@}. At {@{the end of the algorithm there are no edges left}@}, and {@{the sequence from which the edges were chosen}@} forms {@{an Eulerian cycle if the graph has no vertices of odd degree, or an Eulerian trail if there are exactly two vertices of odd degree}@}. <!--SR:!2027-12-11,804,342!2026-08-18,468,322!2026-03-03,368,362!2026-03-14,375,362!2026-12-25,561,312!2026-03-16,378,362!2028-02-19,836,330!2027-12-19,851,342!2029-03-07,1227,362!2029-01-04,1177,362-->

While {@{the _graph traversal_ in Fleury's algorithm is linear in the number of edges, i.e. $O(|E|)$}@}, we also need to {@{factor in the complexity of detecting [bridges](bridge%20(graph%20theory).md)}@}. If {@{we are to re-run [Tarjan](Robert%20Tarjan.md)'s linear time [bridge-finding algorithm](bridge%20(graph%20theory).md#Tarjan's%20bridge-finding%20algorithm)<sup>[\[8\]](#^ref-8)</sup> after the removal of every edge}@}, Fleury's algorithm will {@{have a time complexity of $O(|E|^{2})$}@}. {@{A dynamic bridge-finding algorithm of [Thorup \(2000\)](#^CITEREFThorup2000)}@} allows this {@{to be improved to $O(|E|\cdot \log ^{3}|E|\cdot \log \log |E|)$}@}, but {@{this is still significantly slower than alternative algorithms}@}. <!--SR:!2029-03-19,1236,362!2028-04-25,980,362!2029-04-22,1264,362!2027-10-27,811,342!2027-02-09,559,322!2026-05-17,309,242!2026-03-16,378,362-->

### Hierholzer's algorithm

{@{[Hierholzer](Carl%20Hierholzer.md)'s 1873 paper}@} provides {@{a different method for finding Euler cycles that is more efficient than Fleury's algorithm}@}: <!--SR:!2029-04-08,1252,362!2026-03-08,372,362-->

- Choose {@{any starting vertex _v_}@}, and {@{follow a trail of edges from that vertex until returning to _v_}@}. It is {@{not possible to get stuck at any vertex other than _v_}@}, because {@{the even degree of all vertices ensures that, when the trail enters another vertex _w_ there must be an unused edge leaving _w_}@}. {@{The tour formed in this way}@} is {@{a closed tour, but may not cover all the vertices and edges of the initial graph}@}.
- As long as {@{there exists a vertex _u_ that belongs to the current tour but that has adjacent edges not part of the tour}@}, start {@{another trail from _u_, following unused edges until returning to _u_}@}, and {@{join the tour formed in this way to the previous tour}@}.
- Since we {@{assume the original graph is [connected](connectivity%20(graph%20theory).md#connected%20vertices%20and%20graphs)}@}, {@{repeating the previous step will exhaust all edges of the graph}@}. <!--SR:!2026-01-16,330,350!2028-03-31,926,336!2026-03-20,381,362!2026-03-09,373,362!2026-03-20,382,362!2029-04-02,1249,362!2026-03-27,388,362!2027-12-21,873,350!2025-12-12,299,336!2026-02-11,349,350!2028-10-19,1115,362-->

By using {@{a data structure such as a [doubly linked list](doubly%20linked%20list.md)}@} {@{to maintain the set of unused edges incident to each vertex, to maintain the list of vertices on the current tour that have unused edges, and to maintain the tour itself}@}, {@{the individual operations of the algorithm}@} \({@{finding unused edges exiting each vertex, finding a new starting vertex for a tour, and connecting two tours that share a vertex}@}\) may be {@{performed in constant time each}@}, so {@{the overall algorithm takes [linear time](time%20complexity.md#linear%20time), $O(|E|)$}@}.<sup>[\[9\]](#^ref-9)</sup> <!--SR:!2026-03-09,373,362!2026-06-29,436,322!2026-03-19,381,362!2026-03-08,372,362!2028-10-14,1111,362!2029-03-27,1243,362-->

This algorithm may also {@{be implemented with a [deque](double-ended%20queue.md)}@}. Because {@{it is only possible to get stuck when the deque represents a closed tour}@}, one should {@{rotate the deque by removing edges from the tail and adding them to the head until unstuck}@}, and then {@{continue until all edges are accounted for}@}. This {@{also takes linear time}@}, as {@{the number of rotations performed is never larger than $|E|$}@} \(intuitively, {@{fresh edges are added to the head}@}, while {@{bad edges are shifted towards the tail}@}\) <!--SR:!2026-04-02,393,362!2025-12-15,301,336!2027-12-13,846,342!2026-04-05,395,362!2027-04-05,662,342!2027-12-27,796,330!2025-11-15,262,342!2025-11-22,26,389-->

> {@{![Hamiltonian platonic graphs](../../archives/Wikimedia%20Commons/Hamiltonian%20platonic%20graphs.svg)}@}
>
> {@{Orthographic projections and Schlegel diagrams}@} with {@{[Hamiltonian cycles](hamiltonian%20path.md) of the vertices of the five platonic solids}@} – {@{only the octahedron has an __Eulerian path__ or cycle}@}, by {@{extending its path with the dotted one}@}
>
> <!-- - [v](https://en.wikipedia.org/wiki/Template:Hamiltonian%20platonic%20graphs.svg) -->
> <!-- - [t](https://en.wikipedia.org/wiki/Template_talk:Hamiltonian%20platonic%20graphs.svg) -->
> <!-- - [e](https://en.wikipedia.org/wiki/Special:EditPage/Template:Hamiltonian%20platonic%20graphs.svg) --> <!--SR:!2027-04-19,632,302!2027-11-23,832,342!2027-08-05,683,316!2026-07-30,456,322!2025-11-23,268,342-->

## counting Eulerian circuits

### complexity issues

{@{The number of Eulerian circuits in _[digraphs](directed%20graph.md)_}@} can be calculated using {@{the so-called __[BEST theorem](BEST%20theorem.md)__}@}, named after {@{[de __B__<!-- markdown separator -->ruijn](Nicolaas%20Govert%20de%20Bruijn.md), [van Aardenne-__E__<!-- markdown separator -->hrenfest](Tatyana%20Ehrenfest.md), [__S__<!-- markdown separator -->mith](Cedric%20Smith%20(statistician).md) and [__T__<!-- markdown separator -->utte](W.%20T.%20Tutte.md)}@}. The formula states that {@{the number of Eulerian circuits in a digraph is the product of certain degree factorials and the number of rooted [arborescences](arborescence%20(graph%20theory).md)}@}. The latter can be {@{computed as a [determinant](determinant.md), by the [matrix tree theorem](Kirchhoff's%20theorem.md)}@}, giving {@{a polynomial time algorithm}@}. <!--SR:!2025-12-13,283,342!2026-04-02,392,362!2026-07-07,433,310!2026-07-27,451,322!2027-12-21,818,322!2026-03-17,378,362-->

{@{BEST theorem is first stated in this form}@} in {@{a "note added in proof"}@} to {@{the Aardenne-Ehrenfest and de Bruijn paper \(1951\)}@}. The original proof was {@{[bijective](bijective%20proof.md) and generalized the [de Bruijn sequences](de%20Bruijn%20sequence.md)}@}. It is {@{a variation on an earlier result by Smith and Tutte \(1941\)}@}. <!--SR:!2026-03-29,389,362!2026-04-03,393,362!2026-07-22,448,322!2028-04-02,926,336!2025-12-06,220,282-->

{@{Counting the number of Eulerian circuits on _undirected_ graphs}@} is {@{much more difficult}@}. This problem is {@{known to be [\#P-complete](%23P-complete.md)}@}.<sup>[\[10\]](#^ref-10)</sup> In {@{a positive direction}@}, {@{a [Markov chain Monte Carlo](Markov%20chain%20Monte%20Carlo.md) approach}@}, via {@{the _Kotzig transformations_}@} \(introduced by {@{[Anton Kotzig](Anton%20Kotzig.md) in 1968}@}\) is {@{believed to give a sharp approximation for the number of Eulerian circuits in a graph}@}, though {@{as yet there is no proof of this fact \(even for graphs of bounded degree\)}@}. <!--SR:!2026-03-18,379,362!2026-03-24,385,362!2025-12-08,280,342!2026-02-26,363,362!2026-08-21,478,316!2028-08-18,1057,350!2027-10-31,776,302!2029-02-27,1221,362!2026-03-15,376,362-->

### special cases

{@{An [asymptotic formula](asymptotic%20analysis.md)}@} for {@{the number of Eulerian circuits in the [complete graphs](complete%20graph.md)}@} was determined by {@{[McKay](Brendan%20McKay%20(mathematician).md) and Robinson \(1995\)}@}:<sup>[\[11\]](#^ref-11)</sup> $$\operatorname {ec} (K_{n})=2^{\frac {(n+1)}{2} }\pi ^{\frac {1}{2} }e^{ {\frac {-n^{2} }{2} }+{\frac {11}{12} } }n^{\frac {(n-2)(n+1)}{2} }{\bigl (}1+O(n^{-{\frac {1}{2} }+\epsilon }){\bigr )}.$$ <!--SR:!2028-11-01,1127,362!2029-01-05,1179,362!2026-08-19,469,322-->

A similar formula was {@{later obtained by M.I. Isaev \(2009\)}@} for {@{[complete bipartite graphs](complete%20bipartite%20graph.md)}@}:<sup>[\[12\]](#^ref-12)</sup> $$\operatorname {ec} (K_{n,n})=\left({\frac {n}{2} }-1\right)!^{2n}2^{n^{2}-n+{\frac {1}{2} } }\pi ^{-n+{\frac {1}{2} } }n^{n-1}{\bigl (}1+O(n^{-{\frac {1}{2} }+\epsilon }){\bigr )}.$$ <!--SR:!2026-07-28,452,322!2027-05-05,689,342-->

## applications

Eulerian trails are used in {@{[bioinformatics](bioinformatics.md)}@} to {@{reconstruct the [DNA sequence](nucleic%20acid%20sequence.md) from its fragments}@}.<sup>[\[13\]](#^ref-13)</sup> They are also used in {@{[CMOS](CMOS.md) circuit design}@} to {@{find an optimal [logic gate](logic%20gate.md) ordering}@}.<sup>[\[14\]](#^ref-14)</sup> There are {@{some algorithms for processing [trees](tree%20(graph%20theory).md)}@} that {@{rely on an Euler tour of the tree \(where each edge is treated as a pair of arcs\)}@}.<sup>[\[15\]](#^ref-15)</sup><sup>[\[16\]](#^ref-16)</sup> {@{The [de Bruijn sequences](de%20Bruijn%20sequence.md)}@} can be constructed as {@{Eulerian trails of [de Bruijn graphs](de%20Bruijn%20graph.md)}@}.<sup>[\[17\]](#^ref-17)</sup> <!--SR:!2026-04-05,395,362!2029-03-04,1225,362!2029-03-28,1244,362!2025-11-22,267,342!2026-02-15,353,350!2029-04-13,1256,362!2026-03-10,374,362!2029-01-15,1187,362-->

## in infinite graphs

> {@{![An infinite graph with all vertex degrees equal to four but with no Eulerian line](../../archives/Wikimedia%20Commons/Kely%20graph%20of%20F2%20clear.svg)}@}
>
> {@{An infinite graph with all vertex degrees equal to four but with no Eulerian line}@} <!--SR:!2028-03-13,912,336!2026-03-04,369,362-->

In {@{an [infinite graph](glossary%20of%20graph%20theory.md#infinite)}@}, {@{the corresponding concept to an Eulerian trail or Eulerian cycle}@} is {@{an Eulerian line}@}, {@{a doubly-infinite trail that covers all of the edges of the graph}@}. It is {@{not sufficient for the existence of such a trail that the graph be connected and that all vertex degrees be even}@}; for instance, {@{the infinite [Cayley graph](cayley%20graph.md) shown, with all vertex degrees equal to four, has no Eulerian line}@}. {@{The infinite graphs that contain Eulerian lines}@} were {@{characterized by [Erdõs, Grünwald & Weiszfeld \(1936\)](#^CITEREFErd%C3%B5sGr%C3%BCnwaldWeiszfeld1936)}@}. For {@{an infinite graph or multigraph _G_ to have an Eulerian line}@}, it is {@{necessary and sufficient that all of the following three conditions be met}@}:<sup>[\[18\]](#^ref-18)</sup><sup>[\[19\]](#^ref-19)</sup> <!--SR:!2025-12-14,300,336!2028-07-30,1042,350!2026-01-11,326,350!2026-03-11,373,362!2028-05-23,1002,362!2026-03-28,388,362!2026-03-21,383,362!2026-07-17,443,322!2025-12-13,300,336!2025-11-24,269,342-->

- _G_ is ::@:: connected. <!--SR:!2026-03-12,374,362!2026-04-06,396,362-->
- _G_ has ::@:: [countable sets](countable%20set.md) of vertices and edges. <!--SR:!2025-12-16,301,336!2026-02-25,362,362-->
- _G_ has no ::@:: vertices of \(finite\) odd degree. <!--SR:!2026-03-31,391,362!2026-04-02,393,362-->
- Removing ::@:: (the edges of) any finite subgraph _S_ from _G_ leaves at most two infinite connected components in the remaining graph, and if _S_ has even degree at each of its vertices then removing _S_ leaves exactly one infinite connected component. <!--SR:!2026-04-06,338,302!2027-07-27,742,342-->

## undirected Eulerian graphs

Euler stated {@{a necessary condition for a finite graph to be Eulerian as all vertices must have even degree}@}. {@{Hierholzer}@} {@{proved this is a sufficient condition}@} in {@{a paper published in 1873}@}. This leads to {@{the following necessary and sufficient statement for what a finite graph must have to be Eulerian}@}: {@{An undirected connected finite graph}@} is {@{Eulerian if and only if every vertex of G has even degree}@}.<sup>[\[20\]](#^ref-20)</sup> <!--SR:!2029-01-20,1190,362!2026-03-13,374,362!2026-03-23,384,362!2029-03-14,1233,362!2026-04-05,395,362!2025-12-16,301,336!2025-12-12,282,342-->

The following result was {@{proved by Veblen in 1912}@}: {@{An undirected connected graph is Eulerian}@} {@{if and only if it is the disjoint union of some cycles}@}.<sup>[\[20\]](#^ref-20)</sup> <!--SR:!2026-05-03,394,322!2025-12-13,300,336!2026-02-21,359,362-->

{@{Hierholzer}@} developed {@{a linear time algorithm for constructing an Eulerian tour in an undirected graph}@}. <!--SR:!2028-11-07,1132,362!2026-02-13,351,350-->

## directed Eulerian graphs

> {@{![a directed graph with all even degrees that is not Eulerian](../../archives/Wikimedia%20Commons/Even%20directed%20graph%20that%20is%20not%20Eulerian%20counterexample.svg)}@}
>
> {@{A directed graph with all even degrees that is not Eulerian}@}, serving as {@{a counterexample to the statement that a sufficient condition for a directed graph to be Eulerian is that it has all even degrees}@} <!--SR:!2025-11-11,257,330!2026-03-29,389,362!2027-01-29,614,342-->

It is possible to {@{have a [directed graph](directed%20graph.md) that has all even out-degrees but is not Eulerian}@}. Since {@{an Eulerian circuit leaves a vertex the same number of times as it enters that vertex}@}, {@{a necessary condition for an Eulerian circuit to exist}@} is that {@{the in-degree and out-degree are equal at each vertex}@}. Obviously, {@{connectivity is also necessary}@}. {@{König}@} proved that {@{these conditions are also sufficient}@}. That is, {@{a directed graph is Eulerian if and only if it is connected and the in-degree and out-degree are equal at each vertex}@}.<sup>[\[20\]](#^ref-20)</sup> <!--SR:!2026-03-07,371,362!2025-12-08,295,332!2028-08-07,1037,350!2029-01-15,1186,362!2026-09-28,464,310!2028-10-02,1101,362!2028-10-04,1079,350!2026-01-27,341,362-->

{@{In this theorem}@} it {@{doesn't matter whether "connected" means "weakly connected" or "strongly connected"}@} since {@{they are equivalent for Eulerian graphs}@}. <!--SR:!2026-02-06,345,350!2025-12-14,299,336!2026-03-18,380,362-->

{@{Hierholzer's linear time algorithm for constructing an Eulerian tour}@} is {@{also applicable to directed graphs}@}.<sup>[\[20\]](#^ref-20)</sup> <!--SR:!2026-03-31,390,362!2026-02-12,354,362-->

## mixed Eulerian graphs

> {@{![an even but non-symmetric mixed graph that is Eulerian](../../archives/Wikimedia%20Commons/Eulerian%20mixed%20graph%20that%20is%20even%20but%20not%20symmetric%20proving%20that%20evenness%20and%20symmetricness%20is%20not%20a%20necessary%20and%20sufficient%20condition%20for%20a%20mixed%20graph%20to%20be%20Eulerian.svg)}@}
>
> {@{This mixed graph is Eulerian}@}. The graph is {@{even but not symmetric}@} which proves that {@{evenness and symmetricness are not necessary and sufficient conditions for a mixed graph to be Eulerian}@}. <!--SR:!2026-04-06,396,362!2026-03-07,371,362!2027-12-25,856,342!2026-03-20,382,362-->

{@{All [mixed graphs](mixed%20graph.md) that are both even and symmetric}@} are {@{guaranteed to be Eulerian}@}. However, {@{this is not a necessary condition}@}, as {@{it is possible to construct a non-symmetric, even graph that is Eulerian}@}.<sup>[\[20\]](#^ref-20)</sup> <!--SR:!2029-02-01,1200,362!2029-03-24,1241,362!2026-01-27,337,350!2026-03-26,387,362-->

{@{Ford and Fulkerson proved in 1962}@} in {@{their book _Flows in Networks_}@} {@{a necessary and sufficient condition for a graph to be Eulerian}@}, viz., that {@{every vertex must be even and satisfy the balance condition}@}, i.e. for {@{every subset of vertices S}@}, {@{the difference between the number of arcs leaving S and entering S must be less than or equal to the number of (non-arc) edges incident with S}@}.<sup>[\[20\]](#^ref-20)</sup> <!--SR:!2026-07-18,444,322!2026-03-06,370,362!2026-04-01,392,362!2028-07-23,1036,350!2025-12-12,298,332!2026-08-05,460,322-->

{@{The process of checking if a mixed graph is Eulerian}@} is {@{harder than checking if an undirected or directed graph is Eulerian}@} because {@{the balanced set condition concerns every possible subset of vertices}@}. <!--SR:!2026-03-01,366,362!2026-04-04,394,362!2026-03-30,389,362-->

> {@{![An even mixed graph that violates the balanced set condition and is therefore not Eulerian.](../../archives/Wikimedia%20Commons/Even%20mixed%20graph%20that%20violates%20the%20balanced%20set%20condition%20and%20is%20therefore%20not%20Eulerian.svg)}@}
>
> {@{An even mixed graph}@} that {@{violates the balanced set condition and is therefore not Eulerian}@}. <!--SR:!2027-12-30,820,342!2029-02-23,1206,362!2025-11-29,26,390-->

<!-- markdownlint MD028 -->

> {@{![An even mixed graph that satisfies the balanced set condition and is therefore an Eulerian mixed graph.](../../archives/Wikimedia%20Commons/Even%20mixed%20graph%20satisfies%20the%20balanced%20set%20condition%20and%20is%20therefore%20an%20Eulerian%20mixed%20graph.svg)}@}
>
> {@{An even mixed graph}@} that {@{satisfies the balanced set condition and is therefore an Eulerian mixed graph}@}. <!--SR:!2028-11-05,1129,362!2028-04-18,902,342!2025-11-28,25,390-->

## see also

- [Eulerian matroid](Eulerian%20matroid.md), an abstract generalization of Eulerian graphs
- [five room puzzle](five-room%20puzzle.md)
- [handshaking lemma](handshaking%20lemma.md), ::@:: proven by Euler in his original paper, showing that any undirected connected graph has an even number of odd-degree vertices <!--SR:!2028-07-24,1037,350!2028-02-26,897,330-->
- [Hamiltonian path](Hamiltonian%20path.md) – ::@:: a path that visits each _vertex_ exactly once. <!--SR:!2026-02-02,346,362!2026-02-22,360,362-->
- [route inspection problem](Chinese%20postman%20problem.md), ::@:: search for the shortest path that visits all edges, possibly repeating edges if an Eulerian path does not exist. <!--SR:!2029-02-21,1216,362!2026-03-13,375,362-->
- [Veblen's theorem](Veblen's%20theorem.md), ::@:: which states that graphs with even vertex degree can be partitioned into edge-disjoint cycles regardless of their connectivity <!--SR:!2026-03-28,387,362!2026-12-22,518,310-->

## notes

1. Some people reserve {@{the terms _path_ and _cycle_}@} to {@{mean _non-self-intersecting_ path and cycle}@}. {@{A \(potentially\) self-intersecting path}@} is {@{known as a __trail__ or an __open walk__}@}; and {@{a \(potentially\) self-intersecting cycle}@}, {@{a __circuit__ or a __closed walk__}@}. {@{This ambiguity can be avoided}@} by {@{using the terms Eulerian trail and Eulerian circuit when self-intersection is allowed}@}. <a id="^note-1"></a>^note-1 <!--SR:!2026-03-12,374,362!2026-03-02,367,362!2026-03-27,387,362!2026-02-19,358,362!2026-03-31,391,362!2026-03-27,388,362!2028-01-20,896,350!2026-03-30,390,362-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Eulerian_path) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. N. L. Biggs, E. K. Lloyd and R. J. Wilson, _[Graph Theory, 1736–1936](Graph%20Theory,%201736–1936.md)_, Clarendon Press, Oxford, 1976, 8–9, [ISBN](ISBN.md) [0-19-853901-0](https://en.wikipedia.org/wiki/Special:BookSources/0-19-853901-0). <a id="^ref-1"></a>^ref-1
2. C. L. Mallows, N. J. A. Sloane \(1975\). ["Two-graphs, switching classes and Euler graphs are equal in number"](http://neilsloane.com/doc/MallowsSloane.pdf) \(PDF\). _[SIAM Journal on Applied Mathematics](SIAM%20Journal%20on%20Applied%20Mathematics.md)_. __28__ \(4\): 876–880. [doi](digital%20object%20identifier.md):[10.1137/0128070](https://doi.org/10.1137%2F0128070). [JSTOR](JSTOR.md) [2100368](https://www.jstor.org/stable/2100368). <a id="^ref-2"></a>^ref-2
3. Jun-ichi Yamaguchi, [Introduction of Graph Theory](http://jwilson.coe.uga.edu/EMAT6680/Yamaguchi/emat6690/essay1/GT.html). <a id="^ref-3"></a>^ref-3
4. Schaum's outline of theory and problems of graph theory By V. K. Balakrishnan [\[1\]](https://books.google.com/books?id=1NTPbSehvWsC&dq=unicursal&pg=PA60). <a id="^ref-4"></a>^ref-4
5. [Schrijver, A.](Alexander%20Schrijver.md) \(1983\), ["Bounds on the number of Eulerian orientations"](https://ir.cwi.nl/pub/10053), _Combinatorica_, __3__ \(3–4\): 375–380, [doi](digital%20object%20identifier.md):[10.1007/BF02579193](https://doi.org/10.1007%2FBF02579193), [MR](Mathematical%20Reviews.md) [0729790](https://mathscinet.ams.org/mathscinet-getitem?mr=0729790), [S2CID](Semantic%20Scholar.md#S2CID) [13708977](https://api.semanticscholar.org/CorpusID:13708977). <a id="^ref-5"></a>^ref-5
6. [Pólya, George](George%20Pólya.md); [Tarjan, Robert E.](Robert%20Tarjan.md); [Woods, Donald R.](Don%20Woods%20(programmer).md) \(October 2009\), "Hamiltonian and Eulerian Paths", _Notes on Introductory Combinatorics_, Birkhäuser Boston, pp. 157–168, [doi](digital%20object%20identifier.md):[10.1007/978-0-8176-4953-1\_13](https://doi.org/10.1007%2F978-0-8176-4953-1_13), [ISBN](ISBN.md) [9780817649531](https://en.wikipedia.org/wiki/Special:BookSources/9780817649531) <a id="^ref-6"></a>^ref-6
7. Fleury, Pierre-Henry \(1883\), ["Deux problèmes de Géométrie de situation"](https://books.google.com/books?id=l-03AAAAMAAJ&pg=PA257), _Journal de mathématiques élémentaires_, 2nd ser. \(in French\), __2__: 257–261. <a id="^ref-7"></a>^ref-7
8. [Tarjan, R. Endre](Robert%20Tarjan.md) \(1974\), "A note on finding the bridges of a graph", _Information Processing Letters_, __2__ \(6\): 160–161, [doi](digital%20object%20identifier.md):[10.1016/0020-0190\(74\)90003-9](https://doi.org/10.1016%2F0020-0190%2874%2990003-9), [MR](Mathematical%20Reviews.md) [0349483](https://mathscinet.ams.org/mathscinet-getitem?mr=0349483). <a id="^ref-8"></a>^ref-8
9. Fleischner, Herbert \(1991\), "X.1 Algorithms for Eulerian Trails", [_Eulerian Graphs and Related Topics: Part 1, Volume 2_](https://archive.org/details/euleriangraphsre0001flei/page/), Annals of Discrete Mathematics, vol. 50, Elsevier, pp. [X.1–13](https://archive.org/details/euleriangraphsre0001flei/page/), [ISBN](ISBN.md) [978-0-444-89110-5](https://en.wikipedia.org/wiki/Special:BookSources/978-0-444-89110-5). <a id="^ref-9"></a>^ref-9
10. Brightwell and [Winkler](Peter%20Winkler.md), "[Note on Counting Eulerian Circuits](http://www.cdam.lse.ac.uk/Reports/Files/cdam-2004-12.pdf)", 2004. <a id="^ref-10"></a>^ref-10
11. [Brendan McKay](Brendan%20McKay%20(mathematician).md) and Robert W. Robinson, [Asymptotic enumeration of eulerian circuits in the complete graph](http://cs.anu.edu.au/~bdm/papers/euler.pdf), _[Combinatorica](combinatorica.md)_, 10 \(1995\), no. 4, 367–377. <a id="^ref-11"></a>^ref-11
12. M.I. Isaev \(2009\). "Asymptotic number of Eulerian circuits in complete bipartite graphs". _Proc. 52-nd MFTI Conference_ \(in Russian\). Moscow: 111–114. <a id="^ref-12"></a>^ref-12
13. Pevzner, Pavel A.; Tang, Haixu; Waterman, Michael S. \(2001\). ["An Eulerian trail approach to DNA fragment assembly"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC55524). _Proceedings of the National Academy of Sciences of the United States of America_. __98__ \(17\): 9748–9753. [Bibcode](bibcode.md):[2001PNAS...98.9748P](https://ui.adsabs.harvard.edu/abs/2001PNAS...98.9748P). [doi](digital%20object%20identifier.md):[10.1073/pnas.171285098](https://doi.org/10.1073%2Fpnas.171285098). [PMC](PubMed%20Central.md#PMCID) [55524](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC55524). [PMID](PubMed.md#PubMed%20identifier) [11504945](https://pubmed.ncbi.nlm.nih.gov/11504945). <a id="^ref-13"></a>^ref-13
14. Roy, Kuntal \(2007\). ["Optimum Gate Ordering of CMOS Logic Gates Using Euler Path Approach: Some Insights and Explanations"](https://doi.org/10.2498%2Fcit.1000731). _Journal of Computing and Information Technology_. __15__ \(1\): 85–92. [doi](digital%20object%20identifier.md):[10.2498/cit.1000731](https://doi.org/10.2498%2Fcit.1000731). <a id="^ref-14"></a>^ref-14
15. Tarjan, Robert E.; Vishkin, Uzi \(1985\). "An efficient parallel biconnectivity algorithm". _SIAM Journal on Computing_. __14__ \(4\): 862–874. [CiteSeerX](CiteSeerX.md) [10.1.1.465.8898](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.465.8898). [doi](digital%20object%20identifier.md):[10.1137/0214061](https://doi.org/10.1137%2F0214061). <a id="^ref-15"></a>^ref-15
16. Berkman, Omer; Vishkin, Uzi \(Apr 1994\). "Finding level-ancestors in trees". _J. Comput. Syst. Sci_. 2. __48__ \(2\): 214–230. [doi](digital%20object%20identifier.md):[10.1016/S0022-0000\(05\)80002-9](https://doi.org/10.1016%2FS0022-0000%2805%2980002-9). <a id="^ref-16"></a>^ref-16
17. Savage, Carla \(January 1997\). "A Survey of Combinatorial Gray Codes". _SIAM Review_. __39__ \(4\): 605–629. [doi](digital%20object%20identifier.md):[10.1137/S0036144595295272](https://doi.org/10.1137%2FS0036144595295272). [ISSN](ISSN.md) [0036-1445](https://search.worldcat.org/issn/0036-1445). <a id="^ref-17"></a>^ref-17
18. [Komjáth, Peter](Péter%20Komjáth.md) \(2013\), ["Erdős's work on infinite graphs"](https://books.google.com/books?id=7_zFBAAAQBAJ&pg=PA325), _Erdös centennial_, Bolyai Soc. Math. Stud., vol. 25, János Bolyai Math. Soc., Budapest, pp. 325–345, [doi](digital%20object%20identifier.md):[10.1007/978-3-642-39286-3\_11](https://doi.org/10.1007%2F978-3-642-39286-3_11), [MR](Mathematical%20Reviews.md) [3203602](https://mathscinet.ams.org/mathscinet-getitem?mr=3203602). <a id="^ref-18"></a>^ref-18
19. [Bollobás, Béla](Béla%20Bollobás.md) \(1998\), [_Modern graph theory_](https://books.google.com/books?id=JeIlBQAAQBAJ&pg=PA20), Graduate Texts in Mathematics, vol. 184, Springer-Verlag, New York, p. 20, [doi](digital%20object%20identifier.md):[10.1007/978-1-4612-0619-4](https://doi.org/10.1007%2F978-1-4612-0619-4), [ISBN](ISBN.md) [0-387-98488-7](https://en.wikipedia.org/wiki/Special:BookSources/0-387-98488-7), [MR](Mathematical%20Reviews.md) [1633290](https://mathscinet.ams.org/mathscinet-getitem?mr=1633290). <a id="^ref-19"></a>^ref-19
20. Corberán, Ángel; Laporte, Gilbert, eds. \(2015\). [_Arc Routing: Problems, Methods, and Applications_](https://epubs.siam.org/doi/book/10.1137/1.9781611973679). MOS-SIAM Series on Optimization. SIAM. [doi](digital%20object%20identifier.md):[10.1137/1.9781611973679](https://doi.org/10.1137%2F1.9781611973679). [ISBN](ISBN.md) [978-1-61197-366-2](https://en.wikipedia.org/wiki/Special:BookSources/978-1-61197-366-2). Retrieved 2022-08-19. <a id="^ref-20"></a>^ref-20

## bibliography

- [Erdõs, Pál](Paul%20Erdős.md); [Grünwald, Tibor](Tibor%20Gallai.md); [Weiszfeld, Endre](Andrew%20Vázsonyi.md) \(1936\), ["Végtelen gráfok Euler vonalairól"](https://www.renyi.hu/~p_erdos/1936-11.pdf) \[On Euler lines of infinite graphs\] \(PDF\), _Mat. Fix. Lapok_ \(in Hungarian\), __43__: 129–140. Translated as [Erdős, P.](Paul%20Erdős.md); [Grünwald, T.](Tibor%20Gallai.md); Vázsonyi, E. \(1938\), ["Über Euler-Linien unendlicher Graphen"](http://www.renyi.hu/~p_erdos/1938-15.pdf) \[On Eulerian lines in infinite graphs\] \(PDF\), _J. Math. Phys._ \(in German\), __17__ \(1–4\): 59–75, [doi](digital%20object%20identifier.md):[10.1002/sapm193817159](https://doi.org/10.1002%2Fsapm193817159). <a id="^CITEREFErdõsGrünwaldWeiszfeld1936"></a>^CITEREFErdõsGrünwaldWeiszfeld1936
- Euler, L., "[Solutio problematis ad geometriam situs pertinentis](http://www.math.dartmouth.edu/~euler/pages/E053.html)", _Comment. Academiae Sci. I. Petropolitanae_ __8__ \(1736\), 128–140.
- [Hierholzer, Carl](Carl%20Hierholzer.md) \(1873\), ["Ueber die Möglichkeit, einen Linienzug ohne Wiederholung und ohne Unterbrechung zu umfahren"](https://zenodo.org/record/1447429), _[Mathematische Annalen](Mathematische%20Annalen.md)_, __6__ \(1\): 30–32, [doi](digital%20object%20identifier.md):[10.1007/BF01442866](https://doi.org/10.1007%2FBF01442866), [S2CID](Semantic%20Scholar.md#S2CID) [119885172](https://api.semanticscholar.org/CorpusID:119885172).
- Lucas, E., _Récréations Mathématiques IV_, Paris, 1921.
- Fleury, "Deux problemes de geometrie de situation", _Journal de mathematiques elementaires_ \(1883\), 257–261.
- [T. van Aardenne-Ehrenfest](Tatyana%20Ehrenfest.md) and [N. G. de Bruijn](Nicolaas%20Govert%20de%20Bruijn.md) \(1951\) "Circuits and trees in oriented linear graphs", [Simon Stevin](Simon%20Stevin%20(journal).md) 28: 203–217.
- [Thorup, Mikkel](Mikkel%20Thorup.md) \(2000\), "Near-optimal fully-dynamic graph connectivity", [_Proc. 32nd ACM Symposium on Theory of Computing_](Symposium%20on%20Theory%20of%20Computing.md), pp. 343–350, [doi](digital%20object%20identifier.md):[10.1145/335305.335345](https://doi.org/10.1145%2F335305.335345), [S2CID](Semantic%20Scholar.md#S2CID) [128282](https://api.semanticscholar.org/CorpusID:128282) <a id="^CITEREFThorup2000"></a>^CITEREFThorup2000
- [W. T. Tutte](W.%20T.%20Tutte.md) and [C. A. B. Smith](Cedric%20Smith%20(statistician).md) \(1941\) "On Unicursal Paths in a Network of Degree 4", [American Mathematical Monthly](The%20American%20Mathematical%20Monthly.md) 48: 233–237.

## external links

> ![Wikimedia Commons logo](../../archives/Wikimedia%20Commons/Commons-logo.svg)
>
> Wikimedia Commons has media related to ___[Eulerian paths](https://commons.wikimedia.org/wiki/Category:Eulerian%20paths)___.

- [Discussion of early mentions of Fleury's algorithm](http://mathforum.org/kb/message.jspa?messageID=3648262&tstart=135).
- [_Euler tour_](http://www.encyclopediaofmath.org/index.php/Euler_tour) at [Encyclopedia of Mathematics](Encyclopedia%20of%20Mathematics.md).
