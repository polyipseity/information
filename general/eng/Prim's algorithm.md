---
aliases:
  - Prim algorithm
  - Prim algorithms
  - Prim's algorithm
  - Prim's algorithms
tags:
  - flashcard/active/general/eng/Prim_s_algorithm
  - language/in/English
---

# Prim's algorithm

> ![A demo for Prim's algorithm based on Euclidean distance](../../archives/Wikimedia%20Commons/PrimAlgDemo.gif)
>
> A demo for {@{Prim's algorithm based on Euclidean distance}@} <!--SR:!2029-01-13,1177,350-->

In [computer science](computer%20science.md), {@{__Prim's algorithm__}@} is {@{a [greedy algorithm](greedy%20algorithm.md) that finds a [minimum spanning tree](minimum%20spanning%20tree.md) for a [weighted](glossary%20of%20graph%20theory.md#weighted%20graph) [undirected graph](graph%20(discrete%20mathematics).md#undirected%20graph)}@}. This means it {@{finds a subset of the [edges](glossary%20of%20graph%20theory.md#edge) that forms a [tree](tree%20(graph%20theory).md)}@} that {@{includes every [vertex](vertex%20(graph%20theory).md), where the total weight of all the [edges](graph%20theory.md) in the tree is minimized}@}. The algorithm operates by {@{building this tree one vertex at a time}@}, from {@{an arbitrary starting vertex}@}, at each step {@{adding the cheapest possible connection from the tree to another vertex}@}. <!--SR:!2029-06-17,1297,350!2029-05-31,1284,350!2029-04-19,1253,350!2029-04-24,1256,350!2029-03-08,1220,350!2025-12-08,293,330!2029-03-17,1225,350-->

The algorithm was developed {@{in 1930}@} by {@{[Czech](Czechs.md) mathematician [Vojtěch Jarník](Vojtěch%20Jarník.md)}@}<sup>[\[1\]](#^ref-1)</sup> and later {@{rediscovered and republished}@} by {@{[computer scientists](computer%20scientist.md) [Robert C. Prim](Robert%20C.%20Prim.md) in 1957}@}<sup>[\[2\]](#^ref-2)</sup> and {@{[Edsger W. Dijkstra](Edsger%20W.%20Dijkstra.md) in 1959}@}.<sup>[\[3\]](#^ref-3)</sup> Therefore, it is also sometimes called {@{the __Jarník's algorithm__,<sup>[\[4\]](#^ref-4)</sup> __Prim–Jarník algorithm__,<sup>[\[5\]](#^ref-5)</sup> __Prim–Dijkstra algorithm__<sup>[\[6\]](#^ref-6)</sup> or the __DJP algorithm__}@}.<sup>[\[7\]](#^ref-7)</sup> <!--SR:!2029-02-06,1196,350!2026-11-21,528,310!2029-04-30,1262,350!2026-02-08,316,290!2026-02-09,317,290!2027-11-27,785,310-->

{@{Other well-known algorithms for this problem}@} include {@{[Kruskal's algorithm](Kruskal's%20algorithm.md) and [Borůvka's algorithm](Borůvka's%20algorithm.md)}@}.<sup>[\[8\]](#^ref-8)</sup> These algorithms {@{find the minimum spanning forest in a possibly disconnected graph}@}; in contrast, {@{the most basic form of Prim's algorithm only finds minimum spanning trees in connected graphs}@}. However, {@{running Prim's algorithm separately for each [connected component](component%20(graph%20theory).md) of the graph}@}, it can {@{also be used to find the minimum spanning forest}@}.<sup>[\[9\]](#^ref-9)</sup> In terms of {@{their asymptotic [time complexity](time%20complexity.md)}@}, these three algorithms are {@{equally fast for [sparse graphs](dense%20graph.md)}@}, but {@{slower than other more sophisticated algorithms}@}.<sup>[\[7\]](#^ref-7)</sup><sup>[\[6\]](#^ref-6)</sup> However, for {@{graphs that are sufficiently dense}@}, Prim's algorithm can be {@{made to run in [linear time](time%20complexity.md#linear%20time), meeting or improving the time bounds for other algorithms}@}.<sup>[\[10\]](#^ref-10)</sup> <!--SR:!2025-12-07,292,330!2029-06-09,1291,350!2026-09-14,480,310!2029-06-15,1296,350!2029-01-15,1177,350!2029-01-25,1183,350!2027-12-25,809,330!2027-07-23,738,330!2029-01-20,1183,350!2028-12-13,1151,350!2029-05-09,1265,350-->

> {@{![Prim's algorithm](../../archives/Wikimedia%20Commons/Prim's%20algorithm.svg)}@}
>
> {@{Prim's algorithm starting at vertex A}@}. In the third step, {@{edges BD and AB both have weight 2, so BD is chosen arbitrarily}@}. After that step, {@{AB is no longer a candidate for addition to the tree}@} because {@{it links two nodes that are already in the tree}@}. <!--SR:!2029-02-17,1204,350!2029-05-19,1273,350!2027-11-07,820,330!2029-02-05,1195,350!2025-12-09,294,330-->

## description

The algorithm may informally be described as performing the following steps:

1. Initialize ::@:: a tree with a single vertex, chosen arbitrarily from the graph. <!--SR:!2029-06-05,1288,350!2029-02-16,1203,350-->
2. Grow ::@:: the tree by one edge: Of the edges that connect the tree to vertices not yet in the tree, find the minimum-weight edge, and transfer it to the tree. <!--SR:!2025-12-07,292,330!2028-02-04,877,330-->
3. Repeat ::@:: step 2 \(until all vertices are in the tree\). <!--SR:!2029-04-22,1254,350!2025-12-08,293,330-->

In more detail, it may be implemented following the [pseudocode](pseudocode.md) below.

1. {@{Associate with each vertex _v_}@} of {@{the graph a number _C_\[_v_\] \(the cheapest cost of a connection to _v_\) and an edge _E_\[_v_\] \(the edge providing that cheapest connection\)}@}. To {@{initialize these values}@}, {@{set all values of _C_\[_v_\] to +∞ \(or to any number larger than the maximum edge weight\)}@} and {@{set each _E_\[_v_\] to a special [flag value](sentinel%20value.md) indicating that there is no edge connecting _v_ to earlier vertices}@}.
2. Initialize {@{an empty forest _F_}@} and {@{a set _Q_ of vertices that have not yet been included in _F_ \(initially, all vertices\)}@}.
3. Repeat {@{the following steps until _Q_ is empty}@}:
    1. Find {@{and remove a vertex _v_ from _Q_ having the minimum possible value of _C_\[_v_\]}@}
    2. Add {@{_v_ to _F_}@} and, if {@{_E_\[_v_\] is not the special flag value, also add _E_\[_v_\] to _F_}@}
    3. Loop over {@{the edges _vw_ connecting _v_ to other vertices _w_}@}. For each such edge, if {@{_w_ still belongs to _Q_ and _vw_ has smaller weight than _C_\[_w_\]}@}, perform the following steps:
        1. Set _C_\[_w_\] to {@{the cost of edge _vw_}@}
        2. Set _E_\[_w_\] to {@{point to edge _vw_}@}.
4. Return {@{_F_, which specifically includes the corresponding edges in E}@} <!--SR:!2029-06-01,1285,350!2027-09-29,793,330!2028-12-30,1166,350!2025-12-02,288,330!2028-03-21,872,330!2025-12-08,293,330!2029-04-07,1243,350!2028-11-14,1128,350!2026-07-16,400,290!2025-12-07,292,330!2027-10-15,794,330!2029-06-18,1298,350!2027-11-18,819,330!2027-09-23,788,330!2025-12-01,287,330!2025-12-09,294,330-->

As described above, {@{the starting vertex for the algorithm}@} will {@{be chosen arbitrarily}@}, because {@{the first iteration of the main loop of the algorithm will have a set of vertices in _Q_ that all have equal weights}@}, and {@{the algorithm will automatically start a new tree in _F_}@} when {@{it completes a spanning tree of each connected component of the input graph}@}. The algorithm may be modified to {@{start with any particular vertex _s_ by setting _C_\[_s_\] to be a number smaller than the other values of _C_ \(for instance, zero\)}@}, and it may be modified to {@{only find a single spanning tree rather than an entire spanning forest \(matching more closely the informal description\)}@} by {@{stopping whenever it encounters another vertex flagged as having no associated edge}@}. <!--SR:!2029-01-09,1174,350!2025-12-07,292,330!2027-09-08,775,330!2027-09-27,779,330!2029-04-21,1253,350!2026-06-08,372,290!2027-10-26,811,330!2027-10-04,786,330-->

{@{Different variations of the algorithm}@} {@{differ from each other in how the set _Q_ is implemented}@}: as {@{a simple [linked list](linked%20list.md) or [array](array%20(data%20structure).md) of vertices, or as a more complicated [priority queue](priority%20queue.md) data structure}@}. This choice leads to {@{differences in the [time complexity](time%20complexity.md) of the algorithm}@}. In general, {@{a priority queue will be quicker at finding the vertex _v_ with minimum cost}@}, but {@{will entail more expensive updates when the value of _C_\[_w_\] changes}@}. <!--SR:!2029-05-20,1274,350!2027-10-09,800,330!2026-10-14,505,310!2025-12-08,293,330!2025-12-09,294,330!2026-12-04,541,310-->

## time complexity

> ![The generation of a maze using a randomized Prim's algorithm. This maze is 30x20 in size.](../../archives/Wikimedia%20Commons/MAZE%2030x20%20Prim.ogv)
>
> Prim's algorithm has {@{many applications, such as in the [generation](maze%20generation%20algorithm.md) of this maze}@}, which {@{applies Prim's algorithm to a randomly weighted}@} [grid graph](lattice%20graph.md). <!--SR:!2029-04-24,1257,350!2028-02-13,884,330-->

{@{The time complexity of Prim's algorithm}@} depends on {@{the data structures used for the graph and for ordering the edges by weight}@}, which can be done {@{using a [priority queue](priority%20queue.md)}@}. The following table shows the typical choices: <!--SR:!2029-03-29,1236,350!2029-02-11,1200,350!2028-11-16,1131,350-->

| __Minimum edge weight data structure__                                          | __Time complexity \(total\)__                                                                        |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| [adjacency matrix](adjacency%20matrix.md), searching                            | $O(\lvert V \rvert^{2})$                                                                             |
| [binary heap](binary%20heap.md) and [adjacency list](adjacency%20list.md)       | $O((\lvert V \rvert + \lvert E \rvert)\log \lvert V \rvert)=O(\lvert E \rvert \log \lvert V \rvert)$ |
| [Fibonacci heap](Fibonacci%20heap.md) and [adjacency list](adjacency%20list.md) | $O(\lvert E \rvert + \lvert V \rvert \log \lvert V \rvert)$                                          |

> __flashcards__
>
> - [adjacency matrix](adjacency%20matrix.md), searching ::@:: $O(\lvert V \rvert^{2})$ <!--SR:!2026-12-13,547,310!2026-04-16,345,310-->
> - [binary heap](binary%20heap.md) and [adjacency list](adjacency%20list.md) ::@:: $O((\lvert V \rvert + \lvert E \rvert)\log \lvert V \rvert)=O(\lvert E \rvert \log \lvert V \rvert)$ <!--SR:!2026-06-16,203,210!2026-04-06,334,290-->
> - [Fibonacci heap](Fibonacci%20heap.md) and [adjacency list](adjacency%20list.md) ::@:: $O(\lvert E \rvert + \lvert V \rvert \log \lvert V \rvert)$ <!--SR:!2026-02-03,106,250!2026-05-13,275,210-->

A simple implementation of Prim's, using {@{an [adjacency matrix](adjacency%20matrix.md) or an [adjacency list](adjacency%20list.md) graph representation}@} and {@{linearly searching an array of weights to find the minimum weight edge to add}@}, requires {@{[O](big%20O%20notation.md)\(\|V\|<sup>2</sup>\) running time}@}. However, {@{this running time can be greatly improved}@} by {@{using [heaps](heap%20(data%20structure).md) to implement finding minimum weight edges in the algorithm's inner loop}@}. <!--SR:!2027-02-06,552,310!2028-02-09,842,330!2025-12-09,294,330!2025-12-07,292,330!2026-10-16,338,381-->

A first improved version uses {@{a heap to store all edges of the input graph, ordered by their weight}@}. This leads to {@{an O\(\|E\| log \|E\|\) worst-case running time}@}. But {@{storing vertices instead of edges can improve it still further}@}. The heap should order the vertices by {@{the smallest edge-weight that connects them to any vertex in the partially constructed [minimum spanning tree](minimum%20spanning%20tree.md) \(MST\) \(or infinity if no such edge exists\)}@}. Every time {@{a vertex _v_ is chosen and added to the MST}@}, {@{a decrease-key operation is performed on all vertices _w_ outside the partial MST such that _v_ is connected to _w_}@}, setting {@{the key to the minimum of its previous value and the edge cost of \(_v_,_w_\)}@}. <!--SR:!2026-10-16,507,310!2028-02-18,888,330!2026-10-03,497,310!2026-12-16,550,310!2025-12-03,289,330!2028-03-18,870,330!2028-12-18,1156,350-->

Using {@{a simple [binary heap](binary%20heap.md) data structure}@}, Prim's algorithm can now be shown to {@{run in time [O](big%20O%20notation.md)\(\|E\| log \|V\|\) where \|E\| is the number of edges and \|V\| is the number of vertices}@}. Using {@{a more sophisticated [Fibonacci heap](Fibonacci%20heap.md)}@}, this can be brought down to {@{[O](big%20O%20notation.md)\(\|E\| + \|V\| log \|V\|\)}@}, which is {@{[asymptotically faster](asymptotic%20computational%20complexity.md) when the graph is [dense](dense%20graph.md) enough that \|E\| is [ω](big%20O%20notation.md#Family%20of%20Bachmann.E2.80.93Landau%20notations)\(\|V\|\)}@}, and {@{[linear time](time%20complexity.md#linear%20time) when \|E\| is at least \|V\| log \|V\|}@}. For {@{graphs of even greater density \(having at least \|V\|<sup>_c_</sup> edges for some _c_ \> 1\)}@}, Prim's algorithm can be {@{made to run in linear time even more simply, by using a [_d_-ary heap](d-ary%20heap.md) in place of a Fibonacci heap}@}.<sup>[\[10\]](#^ref-10)</sup><sup>[\[11\]](#^ref-11)</sup> <!--SR:!2026-09-25,489,310!2026-04-05,332,290!2026-11-01,516,310!2026-04-04,332,290!2027-10-17,748,290!2028-03-30,878,330!2026-11-15,527,310!2026-05-17,357,290-->

> {@{![Diagram to assist in proof of Prim's algorithm.](../../archives/Wikimedia%20Commons/Prim's%20algorithm%20proof.svg)}@}
>
> {@{Demonstration of proof}@}. In this case, {@{the graph _Y<sub>1</sub>_ = _Y_ − _f_ + _e_ is already equal to _Y_}@}. In general, {@{the process may need to be repeated}@}. <!--SR:!2025-12-08,293,330!2029-06-06,1289,350!2027-11-01,818,330!2029-06-08,1290,350-->

## proof of correctness

Let _P_ be {@{a connected, weighted [graph](graph%20theory.md)}@}. At {@{every iteration of Prim's algorithm}@}, {@{an edge must be found that connects a vertex in a subgraph to a vertex outside the subgraph}@}. Since {@{_P_ is connected}@}, {@{there will always be a path to every vertex}@}. The output _Y_ of Prim's algorithm is {@{a [tree](tree%20(graph%20theory).md), because the edge and vertex added to tree _Y_ are connected}@}. Let {@{_Y<sub>1</sub>_ be a minimum spanning tree of graph P}@}. If {@{_Y<sub>1</sub>_=_Y_ then _Y_ is a minimum spanning tree}@}. Otherwise, {@{let _e_ be the first edge added during the construction of tree _Y_ that is not in tree _Y<sub>1</sub>_}@}, and {@{_V_ be the set of vertices connected by the edges added before edge _e_}@}. Then {@{one endpoint of edge _e_ is in set _V_ and the other is not}@}. Since {@{tree _Y<sub>1</sub>_ is a spanning tree of graph _P_}@}, there is {@{a path in tree _Y<sub>1</sub>_ joining the two endpoints}@}. As {@{one travels along the path}@}, {@{one must encounter an edge _f_ joining a vertex in set _V_ to one that is not in set _V_}@}. Now, at {@{the iteration when edge _e_ was added to tree _Y_}@}, {@{edge _f_ could also have been added and it would be added instead of edge _e_ if its weight was less than _e_}@}, and since {@{edge _f_ was not added}@}, we conclude that {@{$$w(f)\geq w(e).$$}@} Let {@{tree _Y<sub>2</sub>_ be the graph obtained by removing edge _f_ from and adding edge _e_ to tree _Y<sub>1</sub>_}@}. It is easy to show that {@{tree _Y<sub>2</sub>_ is connected, has the same number of edges as tree _Y<sub>1</sub>_, and the total weights of its edges is not larger than that of tree _Y<sub>1</sub>_}@}, therefore {@{it is also a minimum spanning tree of graph _P_ and it contains edge _e_ and all the edges added before it during the construction of set _V_}@}. {@{Repeat the steps above}@} and we will {@{eventually obtain a minimum spanning tree of graph _P_ that is identical to tree _Y_}@}. This {@{shows _Y_ is a minimum spanning tree}@}. The minimum spanning tree allows for {@{the first subset of the sub-region to be expanded into a larger subset _X_}@}, which {@{we assume to be the minimum}@}. <!--SR:!2029-04-26,1258,350!2027-07-06,725,330!2029-05-08,1264,350!2029-02-14,1202,350!2028-12-30,1167,350!2028-01-08,857,330!2025-12-09,294,330!2028-11-20,1133,350!2027-11-03,818,330!2025-12-09,294,330!2029-05-01,1263,350!2029-01-24,1183,350!2028-01-02,855,330!2027-08-20,760,330!2026-10-10,502,310!2027-12-10,837,330!2028-09-29,1090,350!2028-02-27,896,330!2025-12-07,292,330!2029-01-29,1189,350!2026-12-30,561,310!2027-05-03,612,310!2029-02-26,1212,350!2029-06-16,1296,350!2025-12-09,294,330!2027-10-04,794,330!2029-06-07,1289,350-->

## parallel algorithm

> {@{![Distributed adjacency matrix as used by parallel version of the Prim algorithm.](../../archives/Wikimedia%20Commons/Distributed%20adjacency%20matrix%20for%20parallel%20prim.png)}@}
>
> {@{The adjacency matrix distributed between multiple processors for parallel Prim's algorithm}@}. In {@{each iteration of the algorithm}@}, {@{every processor updates its part of _C_}@} by {@{inspecting the row of the newly inserted vertex in its set of columns in the adjacency matrix}@}. The results are then {@{collected and the next vertex to include in the MST is selected globally}@}. <!--SR:!2027-04-14,665,330!2029-04-07,1242,350!2029-04-23,1255,350!2026-12-29,560,310!2026-10-23,509,310!2027-09-28,789,330-->

{@{The main loop of Prim's algorithm}@} is {@{inherently sequential and thus not [parallelizable](parallel%20algorithm.md)}@}. However, {@{the [inner loop](#step3c), which determines the next edge of minimum weight that does not form a cycle}@}, can be {@{parallelized by dividing the vertices and edges between the available processors}@}.<sup>[\[12\]](#^ref-12)</sup> The following [pseudocode](pseudocode.md) demonstrates this. <!--SR:!2029-05-13,1268,350!2029-04-25,1257,350!2026-09-22,488,310!2029-04-29,1261,350-->

1. Assign {@{each processor $P_{i}$}@} {@{a set $V_{i}$ of consecutive vertices of length ${\tfrac {|V|}{|P|} }$}@}.
2. Create {@{C (cheapest edge weights), E (cheapest edges), F (resulting forest), and Q (vertices not in F) as in the [sequential algorithm](#sequential%20algorithm)}@} and {@{divide C, E, as well as the graph between all processors}@} such that {@{each processor holds the incoming edges to its set of vertices}@}. Let $C_{i}$, $E_{i}$ denote {@{the parts of _C_, _E_ stored on processor $P_{i}$}@}.
3. Repeat {@{the following steps until _Q_ is empty}@}:
    1. On every processor: find {@{the vertex $v_{i}$ having the minimum value in $C_{i}$\[$v_{i}$\] \(local solution\)}@}.
    2. {@{[Min-reduce](reduction%20operator.md) the local solutions}@} to {@{find the vertex _v_ having the minimum possible value of _C_\[_v_\] \(global solution\)}@}.
    3. [Broadcast](broadcasting%20(networking).md) {@{the selected node to every processor}@}.
    4. Add {@{_v_ to _F_}@} and, if {@{_E_\[_v_\] is not the special flag value, also add _E_\[_v_\] to _F_}@}.
    5. On every processor: update {@{$C_{i}$ and $E_{i}$ as in the sequential algorithm}@}.
4. Return {@{_F_}@} <!--SR:!2025-12-09,294,330!2029-05-14,1269,350!2027-09-15,770,330!2025-12-08,293,330!2029-06-16,1297,350!2029-06-14,1295,350!2025-11-29,285,330!2025-11-30,286,330!2029-01-29,1190,350!2028-11-10,1126,350!2025-12-09,294,330!2029-03-07,1219,350!2027-11-24,824,330!2026-11-28,535,310!2029-03-15,1226,350-->

{@{This algorithm can generally be implemented}@} on {@{distributed machines<sup>[\[12\]](#^ref-12)</sup> as well as on shared memory machines}@}.<sup>[\[13\]](#^ref-13)</sup> The running time is {@{$O({\tfrac {|V|^{2} }{|P|} })+O(|V|\log |P|)$}@}, assuming that {@{the _reduce_ and _broadcast_ operations can be performed in $O(\log |P|)$}@}.<sup>[\[12\]](#^ref-12)</sup> {@{A variant of Prim's algorithm for shared memory machines}@}, in which {@{Prim's sequential algorithm is being run in parallel, starting from different vertices}@}, has also been explored.<sup>[\[14\]](#^ref-14)</sup> It should, however, be noted that {@{more sophisticated algorithms exist}@} to {@{solve the [distributed minimum spanning tree](distributed%20minimum%20spanning%20tree.md) problem in a more efficient manner}@}. <!--SR:!2028-10-08,1098,350!2027-04-22,670,330!2025-12-23,161,210!2027-05-31,629,310!2025-12-03,289,330!2025-12-08,293,330!2025-12-04,290,330!2028-02-07,879,330-->

## see also

- [Dijkstra's algorithm](Dijkstra's%20algorithm.md), ::@:: a very similar algorithm for the [shortest path problem](shortest%20path%20problem.md) <!--SR:!2027-08-21,751,330!2025-12-09,294,330-->
- [greedoids](greedoid.md) ::@:: offer a general way to understand the correctness of Prim's algorithm <!--SR:!2027-12-18,843,330!2026-10-25,510,310-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Prim's_algorithm) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFJarník1930"></a> [Jarník, V.](Vojtěch%20Jarník.md) \(1930\), "O jistém problému minimálním" \[About a certain minimal problem\], _Práce Moravské Přírodovědecké Společnosti_ \(in Czech\), __6__ \(4\): 57–63, [hdl](Handle%20System.md):[10338.dmlcz/500726](https://hdl.handle.net/10338.dmlcz%2F500726). <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFPrim1957"></a> [Prim, R. C.](Robert%20C.%20Prim.md) \(November 1957\), ["Shortest connection networks And some generalizations"](https://archive.org/details/bstj36-6-1389), _[Bell System Technical Journal](Bell%20Labs%20Technical%20Journal.md)_, __36__ \(6\): 1389–1401, [Bibcode](bibcode.md):[1957BSTJ...36.1389P](https://ui.adsabs.harvard.edu/abs/1957BSTJ...36.1389P), [doi](digital%20object%20identifier.md):[10.1002/j.1538-7305.1957.tb01515.x](https://doi.org/10.1002%2Fj.1538-7305.1957.tb01515.x). <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFDijkstra1959"></a> [Dijkstra, E. W.](Edsger%20W.%20Dijkstra.md) \(December 1959\), ["A note on two problems in connexion with graphs"](https://www-m3.ma.tum.de/twiki/pub/MN0506/WebHome/dijkstra.pdf) \(PDF\), _Numerische Mathematik_, __1__ \(1\): 269–271, [CiteSeerX](CiteSeerX.md) [10.1.1.165.7577](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.165.7577), [doi](digital%20object%20identifier.md):[10.1007/BF01386390](https://doi.org/10.1007%2FBF01386390), [S2CID](Semantic%20Scholar.md#S2CID) [123284777](https://api.semanticscholar.org/CorpusID:123284777). <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFSedgewickWayne2011"></a> [Sedgewick, Robert](Robert%20Sedgewick%20(computer%20scientist).md); Wayne, Kevin Daniel \(2011\), [_Algorithms_](https://books.google.com/books?id=MTpsAQAAQBAJ&pg=PA628) \(4th ed.\), Addison-Wesley, p. 628, [ISBN](ISBN.md) [978-0-321-57351-3](https://en.wikipedia.org/wiki/Special:BookSources/978-0-321-57351-3). <a id="^ref-4"></a>^ref-4
5. <a id="CITEREFRosen2011"></a> Rosen, Kenneth \(2011\), [_Discrete Mathematics and Its Applications_](https://books.google.com/books?id=6EJOCAAAQBAJ&pg=PA798) \(7th ed.\), McGraw-Hill Science, p. 798. <a id="^ref-5"></a>^ref-5
6. <a id="CITEREFCheritonTarjan1976"></a> [Cheriton, David](David%20Cheriton.md); [Tarjan, Robert Endre](Robert%20Tarjan.md) \(1976\), "Finding minimum spanning trees", _[SIAM Journal on Computing](SIAM%20Journal%20on%20Computing.md)_, __5__ \(4\): 724–742, [doi](digital%20object%20identifier.md):[10.1137/0205051](https://doi.org/10.1137%2F0205051), [MR](Mathematical%20Reviews.md) [0446458](https://mathscinet.ams.org/mathscinet-getitem?mr=0446458). <a id="^ref-6"></a>^ref-6
7. <a id="CITEREFPettieRamachandran2002"></a> Pettie, Seth; [Ramachandran, Vijaya](Vijaya%20Ramachandran.md) \(January 2002\), ["An optimal minimum spanning tree algorithm"](http://www.cs.utexas.edu/~vlr/papers/optmsf-jacm.pdf) \(PDF\), _Journal of the ACM_, __49__ \(1\): 16–34, [CiteSeerX](CiteSeerX.md) [10.1.1.110.7670](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.110.7670), [doi](digital%20object%20identifier.md):[10.1145/505241.505243](https://doi.org/10.1145%2F505241.505243), [MR](Mathematical%20Reviews.md) [2148431](https://mathscinet.ams.org/mathscinet-getitem?mr=2148431), [S2CID](Semantic%20Scholar.md#S2CID) [5362916](https://api.semanticscholar.org/CorpusID:5362916). <a id="^ref-7"></a>^ref-7
8. <a id="CITEREFTarjan1983"></a> [Tarjan, Robert Endre](Robert%20Tarjan.md) \(1983\), "Chapter 6. Minimum spanning trees. 6.2. Three classical algorithms", _Data Structures and Network Algorithms_, CBMS-NSF Regional Conference Series in Applied Mathematics, vol. 44, [Society for Industrial and Applied Mathematics](Society%20for%20Industrial%20and%20Applied%20Mathematics.md), pp. 72–77. <a id="^ref-8"></a>^ref-8
9. <a id="CITEREFKepnerGilbert2011"></a> Kepner, Jeremy; Gilbert, John \(2011\), [_Graph Algorithms in the Language of Linear Algebra_](https://books.google.com/books?id=JBXDc83jRBwC&pg=PA55), Software, Environments, and Tools, vol. 22, [Society for Industrial and Applied Mathematics](Society%20for%20Industrial%20and%20Applied%20Mathematics.md), p. 55, [ISBN](ISBN.md) [9780898719901](https://en.wikipedia.org/wiki/Special:BookSources/9780898719901). <a id="^ref-9"></a>^ref-9
10. [Tarjan \(1983\)](#CITEREFTarjan1983), p. 77. <a id="^ref-10"></a>^ref-10
11. <a id="CITEREFJohnson1975"></a> [Johnson, Donald B.](Donald%20B.%20Johnson.md) \(December 1975\), "Priority queues with update and finding minimum spanning trees", _Information Processing Letters_, __4__ \(3\): 53–57, [doi](digital%20object%20identifier.md):[10.1016/0020-0190\(75\)90001-0](https://doi.org/10.1016%2F0020-0190%2875%2990001-0). <a id="^ref-11"></a>^ref-11
12. <a id="CITEREFGramaGuptaKarypisKumar2003"></a> Grama, Ananth; Gupta, Anshul; Karypis, George; Kumar, Vipin \(2003\), _Introduction to Parallel Computing_, Addison-Wesley, pp. 444–446, [ISBN](ISBN.md) [978-0201648652](https://en.wikipedia.org/wiki/Special:BookSources/978-0201648652) <a id="^ref-12"></a>^ref-12
13. <a id="CITEREFQuinnDeo1984"></a> Quinn, Michael J.; Deo, Narsingh \(1984\), "Parallel graph algorithms", _ACM Computing Surveys_, __16__ \(3\): 319–348, [doi](digital%20object%20identifier.md):[10.1145/2514.2515](https://doi.org/10.1145%2F2514.2515), [S2CID](Semantic%20Scholar.md#S2CID) [6833839](https://api.semanticscholar.org/CorpusID:6833839) <a id="^ref-13"></a>^ref-13
14. <a id="CITEREFSetia2009"></a> Setia, Rohit \(2009\), ["A new parallel algorithm for minimum spanning tree problem"](https://ncit-cluster.grid.pub.ro/trac/PP2009/export/157/proiecte/pgraph/Documentation/parallelspannintree.pdf) \(PDF\), _Proc. International Conference on High Performance Computing \(HiPC\)_ <a id="^ref-14"></a>^ref-14

## external links

- [Prim's Algorithm progress on randomly distributed points](https://meyavuz.wordpress.com/2017/03/10/prims-algorithm-animation-for-randomly-distributed-points)
- ![Wikimedia Commons logo](../../archives/Wikimedia%20Commons/Commons-logo.svg) Media related to [Prim's algorithm](https://commons.wikimedia.org/wiki/Category:Prim%27s%20algorithm) at Wikimedia Commons
