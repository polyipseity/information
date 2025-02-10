---
aliases:
  - Kruskal's algorithm
  - Kruskal's algorithms
tags:
  - flashcard/active/general/eng/Kruskal_s_algorithm
  - language/in/English
---

# Kruskal's algorithm

- Not to be confused with {@{[Kruskal's principle](Kruskal%20count.md)}@}. <!--SR:!2025-02-11,62,310-->

> __Kruskal's algorithm__
>
> ![A demo for Kruskal's algorithm to find minimum spanning tree on a 2D plane.](../../archives/Wikimedia%20Commons/KruskalDemo.gif)
>
> {@{Animation of Kruskal's algorithm on a [complete graph](complete%20graph.md) with weights based on Euclidean distance}@}
>
> - __Class__ ::@:: [Minimum spanning tree algorithm](minimum%20spanning%20tree.md) <!--SR:!2025-02-17,66,310!2025-02-16,66,310-->
> - __Data structure__ ::@:: [Graph](graph%20(abstract%20data%20type).md) <!--SR:!2025-02-16,66,310!2025-02-18,67,310-->
> - __[Worst-case](best,%20worst%20and%20average%20case.md) [performance](time%20complexity.md)__ ::@:: $O(|E|\log |V|)$ <!--SR:!2025-03-24,79,270!2025-02-15,26,210-->

{@{__Kruskal's algorithm__}@}<sup>[\[1\]](#^ref-1)</sup> finds {@{a [minimum spanning forest](minimum%20spanning%20tree.md) of an undirected [edge-weighted graph](glossary%20of%20graph%20theory.md#weighted%20graph)}@}. If {@{the graph is [connected](connectivity%20(graph%20theory).md)}@}, it {@{finds a [minimum spanning tree](minimum%20spanning%20tree.md)}@}. It is {@{a [greedy algorithm](greedy%20algorithm.md) that in each step adds to the forest the lowest-weight edge that will not form a [cycle](cycle%20(graph%20theory).md)}@}.<sup>[\[2\]](#^ref-2)</sup> {@{The key steps of the algorithm}@} are {@{[sorting](sorting.md) and the use of a [disjoint-set data structure](disjoint-set%20data%20structure.md) to detect cycles}@}. Its running time is {@{dominated by the time to sort all of the graph edges by their weight}@}. <!--SR:!2025-10-25,258,330!2025-02-11,62,310!2025-02-12,63,310!2025-10-30,263,330!2025-08-14,197,310!2025-10-21,255,330!2025-02-17,66,310!2025-02-18,67,310-->

{@{A minimum spanning tree of a connected weighted graph}@} is {@{a connected subgraph, without cycles, for which the sum of the weights of all the edges in the subgraph is minimal}@}. For {@{a disconnected graph}@}, {@{a minimum spanning forest}@} is {@{composed of a minimum spanning tree for each [connected component](component%20(graph%20theory).md)}@}. <!--SR:!2025-02-11,62,310!2025-02-16,66,310!2025-02-16,66,310!2025-02-18,67,310!2025-07-09,168,310-->

This algorithm was first published by {@{[Joseph Kruskal](Joseph%20Kruskal.md) in 1956}@},<sup>[\[3\]](#^ref-3)</sup> and was {@{rediscovered soon afterward}@} by {@{[Loberman & Weinberger \(1957\)](#^ref-4)}@}.<sup>[\[4\]](#^ref-4)</sup> Other algorithms for this problem include {@{[Prim's algorithm](Prim's%20algorithm.md), [Borůvka's algorithm](Borůvka's%20algorithm.md), and the [reverse-delete algorithm](reverse-delete%20algorithm.md)}@}. <!--SR:!2025-05-31,127,290!2025-08-10,193,310!2025-05-06,112,290!2025-04-14,80,250-->

## algorithm

The algorithm performs the following steps:

- Create ::@:: a forest \(a set of trees\) initially consisting of a separate single-vertex tree for each vertex in the input graph. <!--SR:!2025-10-31,263,330!2025-06-08,133,290-->
- Sort ::@:: the graph edges by weight. <!--SR:!2025-02-17,67,310!2025-02-17,67,310-->
- Loop through ::@:: the edges of the graph, in ascending sorted order by their weight. For each edge: <!--SR:!2025-08-17,188,310!2025-02-12,63,310-->
  - Test ::@:: whether adding the edge to the current forest would create a cycle. <!--SR:!2025-02-18,67,310!2025-10-17,252,330-->
  - If not, ::@:: add the edge to the forest, combining two trees into a single tree. <!--SR:!2025-02-11,62,310!2025-02-11,62,310-->

At {@{the termination of the algorithm}@}, {@{the forest forms a minimum spanning forest of the graph}@}. If {@{the graph is connected}@}, the forest {@{has a single component and forms a minimum spanning tree}@}. <!--SR:!2025-02-17,66,310!2025-10-25,259,330!2025-02-17,67,310!2025-02-16,66,310-->

## pseudocode

The following code is implemented with {@{a [disjoint-set data structure](disjoint-set%20data%20structure.md)}@}. It represents {@{the forest _F_ as a set of undirected edges}@}, and {@{uses the disjoint-set data structure to efficiently determine whether two vertices are part of the same tree}@}. <!--SR:!2025-02-12,63,310!2025-08-01,186,310!2025-06-15,138,290-->

<pre>
<b>algorithm</b> Kruskal(<i>G</i>) <b>is</b>
    F:= ∅
    <b>for each</b> v <b>in</b> G.V <b>do</b>
        MAKE-SET(v)
    <b>for each</b> {u, v} <b>in</b> G.E ordered by weight({u, v}), increasing <b>do</b>
        <b>if</b> FIND-SET(u) ≠ FIND-SET(v) <b>then</b>
            F&nbsp;:= F ∪ { {u, v} }
            UNION(FIND-SET(u), FIND-SET(v))
    <b>return</b> F
</pre>

> [!info]- code
>
> ```psuedocode
> algorithm Kruskal(G) is
>     F:= ∅
>     for each v in G.V do
>         MAKE-SET(v)
>     for each {u, v} in G.E ordered by weight({u, v}), increasing do
>         if FIND-SET(u) ≠ FIND-SET(v) then
>             F := F ∪ { {u, v} }
>             UNION(FIND-SET(u), FIND-SET(v))
>     return F
> ```

<!-- markdownlint MD028 -->

> __code flashcards__
>
> <pre>
> {@{<b>algorithm</b> Kruskal(<i>G</i>)}@} <b>is</b>
>     {@{F:= ∅}@}
>     {@{<b>for each</b> v <b>in</b> G.V}@} <b>do</b>
>         {@{MAKE-SET(v)}@}
>     {@{<b>for each</b> {u, v} <b>in</b> G.E ordered by weight({u, v}), increasing}@} <b>do</b>
>         {@{<b>if</b> FIND-SET(u) ≠ FIND-SET(v)}@} <b>then</b>
>             {@{F&nbsp;:= F ∪ { {u, v} }<!-- flashcard separator -->}@}
>             {@{UNION(FIND-SET(u), FIND-SET(v))}@}
>     {@{<b>return</b> F}@}
> </pre> <!--SR:!2025-10-26,259,330!2025-08-09,192,310!2025-02-12,63,310!2025-02-17,67,310!2025-02-17,66,310!2025-02-12,63,310!2025-10-22,256,330!2025-02-16,66,310!2025-02-17,66,310-->

## complexity

For {@{a graph with _E_ edges and _V_ vertices}@}, Kruskal's algorithm can be shown to {@{run in time _O_\(_E_ log _E_\) time}@}, with {@{simple data structures}@}. Here, {@{_O_ expresses the time in [big O notation](Big%20O%20notation.md), and log is a [logarithm](logarithm.md) to any base \(since inside _O_-notation logarithms to all bases are equivalent, because they are the same up to a constant factor\)}@}. This time bound is {@{often written instead as _O_\(_E_ log _V_\)}@}, which is {@{equivalent for graphs with no isolated vertices}@}, because {@{for these graphs _V_/2 ≤ _E_ \< _V_<sup>2</sup>}@} and {@{the logarithms of _V_ and _E_ are again within a constant factor of each other}@}. <!--SR:!2025-10-03,239,330!2025-06-20,142,290!2025-02-17,66,310!2025-02-17,67,310!2025-05-28,125,290!2025-07-23,179,310!2025-02-17,67,310!2025-02-12,63,310-->

To {@{achieve this bound}@}, first {@{sort the edges by weight using a [comparison sort](comparison%20sort.md) in _O_\(_E_ log _E_\) time}@}. Once sorted, it is {@{possible to loop through the edges in sorted order in constant time per edge}@}. Next, {@{use a [disjoint-set data structure](disjoint-set%20data%20structure.md)}@}, with {@{a set of vertices for each component, to keep track of which vertices are in which components}@}. Creating {@{this structure, with a separate set for each vertex}@}, takes {@{_V_ operations and _O_\(_V_\) time}@}. {@{The final iteration through all edges}@} performs {@{two find operations and possibly one union operation per edge}@}. These operations take {@{[amortized time](amortized%20analysis.md) _O_\(_α_\(_V_\)\) time per operation}@}, giving {@{worst-case total time _O_\(_E_ _α_\(_V_\)\) for this loop}@}, where {@{_α_ is the extremely slowly growing [inverse Ackermann function](Ackermann%20function.md#inverse)}@}. {@{This part of the time bound}@} is {@{much smaller than the time for the sorting step}@}, so {@{the total time for the algorithm can be simplified to the time for the sorting step}@}. <!--SR:!2025-11-01,264,330!2025-08-14,185,310!2025-02-12,63,310!2025-02-11,62,310!2025-08-18,189,310!2025-10-27,260,330!2025-03-15,72,270!2025-10-23,257,330!2025-02-17,67,310!2025-02-18,67,310!2025-02-16,66,310!2025-02-18,67,310!2025-10-22,255,330!2025-02-17,67,310!2025-08-04,189,310-->

In cases {@{where the edges are already sorted}@}, or {@{where they have small enough integer weight to allow [integer sorting](integer%20sorting.md) algorithms such as [counting sort](counting%20sort.md) or [radix sort](radix%20sort.md) to sort them in linear time}@}, {@{the disjoint set operations are the slowest remaining part of the algorithm}@} and {@{the total time is _O_\(_E_ _α_\(_V_\)\)}@}. <!--SR:!2025-07-11,170,310!2025-05-29,126,290!2025-02-17,66,310!2025-02-16,66,310-->

## example

| __Image__                                                                                          | __Description__                                                                                                                                                                                                                                                                                                             |
| -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Kruskal's algorithm example step 1](../../archives/Wikimedia%20Commons/Kruskal%20Algorithm%201.svg) | {@{__AD__ and __CE__ are the shortest edges, with length 5}@}, and {@{__AD__ has been [arbitrarily](arbitrariness.md) chosen, so it is highlighted}@}.                                                                                                                                                                      |
| ![Kruskal's algorithm example step 2](../../archives/Wikimedia%20Commons/Kruskal%20Algorithm%202.svg) | {@{__CE__ is now the shortest edge that does not form a cycle, with length 5}@}, so {@{it is highlighted as the second edge}@}.                                                                                                                                                                                             |
| ![Kruskal's algorithm example step 3](../../archives/Wikimedia%20Commons/Kruskal%20Algorithm%203.svg) | {@{The next edge, __DF__ with length 6}@}, is {@{highlighted using much the same method}@}.                                                                                                                                                                                                                                 |
| ![Kruskal's algorithm example step 4](../../archives/Wikimedia%20Commons/Kruskal%20Algorithm%204.svg) | {@{The next-shortest edges are __AB__ and __BE__, both with length 7}@}. __AB__ is {@{chosen arbitrarily, and is highlighted}@}. The edge __BD__ has been {@{highlighted in red}@}, because {@{there already exists a path \(in green\) between __B__ and __D__, so it would form a cycle \(__ABD__\) if it were chosen}@}. |
| ![Kruskal's algorithm example step 5](../../archives/Wikimedia%20Commons/Kruskal%20Algorithm%205.svg) | The process {@{continues to highlight the next-smallest edge, __BE__ with length 7}@}. Many more edges are {@{highlighted in red at this stage}@}: __BC__ because {@{it would form the loop __BCE__}@}, __DE__ because {@{it would form the loop __DEBA__}@}, and __FE__ because {@{it would form __FEBAD__}@}.             |
| ![Kruskal's algorithm example step 6](../../archives/Wikimedia%20Commons/Kruskal%20Algorithm%206.svg) | Finally, the process {@{finishes with the edge __EG__ of length 9}@}, and {@{the minimum spanning tree is found}@}.                                                                                                                                                                                                         | <!--SR:!2025-10-15,251,330!2025-02-16,66,310!2025-10-09,244,330!2025-02-17,67,310!2025-02-12,63,310!2025-02-12,63,310!2025-02-16,66,310!2025-10-23,256,330!2025-02-11,62,310!2025-06-24,160,310!2025-10-09,245,330!2025-02-17,67,310!2025-02-16,66,310!2025-02-12,63,310!2025-10-12,247,330!2025-02-17,66,310!2025-02-21,66,330-->

## proof of correctness

The proof {@{consists of two parts}@}. First, it is proved that {@{the algorithm produces a [spanning tree](spanning%20tree.md)}@}. Second, it is proved that {@{the constructed spanning tree is of minimal weight}@}. <!--SR:!2025-10-24,257,330!2025-08-13,196,310!2025-10-25,259,330-->

### spanning tree

Let $G$ be {@{a connected, weighted graph}@} and let $Y$ be {@{the subgraph of $G$ produced by the algorithm}@}. $Y$ {@{cannot have a cycle}@}, as {@{by definition an edge is not added if it results in a cycle}@}. $Y$ {@{cannot be disconnected}@}, since {@{the first encountered edge that joins two components of $Y$ would have been added by the algorithm}@}. Thus, {@{$Y$ is a spanning tree of $G$}@}. <!--SR:!2025-02-16,66,310!2025-10-10,245,330!2025-02-17,67,310!2025-02-18,67,310!2025-02-17,67,310!2025-11-02,265,330!2025-02-12,63,310-->

### minimality

We show that {@{the following proposition ___P___ is true by [induction](mathematical%20induction.md)}@}: If {@{_F_ is the set of edges chosen at any stage of the algorithm}@}, then {@{there is some minimum spanning tree that contains _F_ and none of the edges rejected by the algorithm}@}. <!--SR:!2025-02-17,67,310!2025-08-03,188,310!2025-02-12,63,310-->

- Clearly {@{___P___ is true at the beginning, when _F_ is empty}@}: {@{any minimum spanning tree will do}@}, and {@{there exists one because a weighted connected graph always has a minimum spanning tree}@}.
- Now assume {@{___P___ is true for some non-final edge set _F_}@} and {@{let _T_ be a minimum spanning tree that contains _F_}@}.
  - If {@{the next chosen edge _e_ is also in _T_}@}, then {@{___P___ is true for _F_ + _e_}@}.
  - Otherwise, if {@{_e_ is not in _T_}@} then {@{_T_ + _e_ has a cycle _C_}@}. The cycle _C_ contains {@{edges which do not belong to _F_ + _e_}@}, since {@{_e_ does not form a cycle when added to _F_ but does in _T_}@}. Let {@{_f_ be an edge which is in _C_ but not in _F_ + _e_}@}. Note that {@{_f_ also belongs to _T_, since _f_ belongs to _T_ + _e_ but not _F_ + _e_}@}. By ___P___, {@{_f_ has not been considered by the algorithm}@}. _f_ {@{must therefore have a weight at least as large as _e_}@}. Then {@{_T_ − _f_ + _e_ is a tree, and it has the same or less weight as _T_}@}. However {@{since _T_ is a minimum spanning tree then _T_ − _f_ + _e_ has the same weight as _T_}@}, otherwise {@{we get a contradiction and _T_ would not be a minimum spanning tree}@}. So {@{_T_ − _f_ + _e_ is a minimum spanning tree containing _F_ + _e_}@} and {@{again ___P___ holds}@}.
- Therefore, by {@{the principle of induction}@}, {@{___P___ holds when _F_ has become a spanning tree}@}, which is {@{only possible if _F_ is a minimum spanning tree itself}@}. <!--SR:!2025-02-11,62,310!2025-10-24,257,330!2025-02-12,63,310!2025-02-17,67,310!2025-02-16,66,310!2025-10-15,250,330!2025-10-08,244,330!2025-02-17,67,310!2025-02-16,66,310!2025-02-17,66,310!2025-02-12,63,310!2025-10-11,246,330!2025-02-16,66,310!2025-02-17,67,310!2025-02-17,67,310!2025-06-14,137,290!2025-02-16,66,310!2025-07-22,178,310!2025-07-30,185,310!2025-02-12,63,310!2025-11-03,266,330!2025-02-17,67,310!2025-02-17,66,310-->

## parallel algorithm

Kruskal's algorithm is {@{inherently sequential and hard to parallelize}@}. It is, however, {@{possible to perform the initial sorting of the edges in parallel}@} or, alternatively, {@{to use a parallel implementation of a [binary heap](binary%20heap.md) to extract the minimum-weight edge in every iteration}@}.<sup>[\[5\]](#^ref-5)</sup> As {@{parallel sorting is possible in time $O(n)$ on $O(\log n)$ processors}@},<sup>[\[6\]](#^ref-6)</sup> {@{the runtime of Kruskal's algorithm}@} can be {@{reduced to _O_\(_E_ α\(_V_\)\)}@}, where {@{α again is the inverse of the single-valued [Ackermann function](Ackermann%20function.md)}@}. <!--SR:!2025-10-29,262,330!2025-10-18,253,330!2025-03-26,80,270!2025-03-20,76,270!2025-02-17,67,310!2025-06-16,139,290!2025-08-18,189,310-->

{@{A variant of Kruskal's algorithm, named Filter-Kruskal}@}, has been described by {@{Osipov et al.}@}<sup>[\[7\]](#^ref-7)</sup> and is {@{better suited for parallelization}@}. The basic idea behind Filter-Kruskal is to {@{partition the edges in a similar way to [quicksort](quicksort.md)}@} and {@{filter out edges that connect vertices of the same tree to reduce the cost of sorting}@}. The following [pseudocode](pseudocode.md) demonstrates this. <!--SR:!2025-03-25,79,270!2025-04-17,104,290!2025-08-17,188,310!2025-02-16,66,310!2025-02-12,63,310-->

<pre>
<b>function</b> filter_kruskal(G) <b>is</b>
    <b>if</b> |G.E| &lt; kruskal_threshold:
        <b>return</b> kruskal(G)
    pivot = choose_random(G.E)
    E<sub>≤</sub>, E<sub>&gt;</sub> = partition(G.E, pivot)
    A = filter_kruskal(E<sub>≤</sub>)
    E<sub>&gt;</sub> = filter(E<sub>&gt;</sub>)
    A = A ∪ filter_kruskal(E<sub>&gt;</sub>)
    <b>return</b> A

<b>function</b> partition(E, pivot) <b>is</b>
    E<sub>≤</sub> = ∅, E<sub>&gt;</sub> = ∅
    <b>foreach</b> (u, v) in E <b>do</b>
        <b>if</b> weight(u, v) ≤ pivot <b>then</b>
            E<sub>≤</sub> = E<sub>≤</sub> ∪ {(u, v)}
        <b>else</b>
            E<sub>&gt;</sub> = E<sub>&gt;</sub> ∪ {(u, v)}
    <b>return</b> E<sub>≤</sub>, E<sub>&gt;</sub>

<b>function</b> filter(E) <b>is</b>
    E<sub>f</sub> = ∅
    <b>foreach</b> (u, v) in E <b>do</b>
        <b>if</b> find_set(u) ≠ find_set(v) <b>then</b>
            E<sub>f</sub> = E<sub>f</sub> ∪ {(u, v)}
    <b>return</b> E<sub>f</sub>
</pre>

> [!info]- code
>
> ```psuedocode
> function filter_kruskal(G) is
>     if |G.E| < kruskal_threshold:
>         return kruskal(G)
>     pivot = choose_random(G.E)
>     E≤, E> = partition(G.E, pivot)
>     A = filter_kruskal(E≤)
>     E> = filter(E>)
>     A = A ∪ filter_kruskal(E>)
>     return A
> 
> function partition(E, pivot) is
>     E≤ = ∅, E> = ∅
>     foreach (u, v) in E do
>         if weight(u, v) ≤ pivot then
>             E≤ = E≤ ∪ {(u, v)}
>         else
>             E> = E> ∪ {(u, v)}
>     return E≤, E>
> 
> function filter(E) is
>     Ef = ∅
>     foreach (u, v) in E do
>         if find_set(u) ≠ find_set(v) then
>             Ef = Ef ∪ {(u, v)}
>     return Ef
> ```

<!-- markdownlint MD028 -->

> __code flashcards__
>
> <pre>
> {@{<b>function</b> filter_kruskal(G)}@} <b>is</b>
>     {@{<b>if</b> |G.E| &lt; kruskal_threshold}@}:
>         {@{<b>return</b> kruskal(G)}@}
>     {@{pivot = choose_random(G.E)}@}
>     {@{E<sub>≤</sub>, E<sub>&gt;</sub> = partition(G.E, pivot)}@}
>     {@{A = filter_kruskal(E<sub>≤</sub>)}@}
>     {@{E<sub>&gt;</sub> = filter(E<sub>&gt;</sub>)}@}
>     {@{A = A ∪ filter_kruskal(E<sub>&gt;</sub>)}@}
>     {@{<b>return</b> A}@}
>
> {@{<b>function</b> partition(E, pivot)}@} <b>is</b>
>     {@{E<sub>≤</sub> = ∅, E<sub>&gt;</sub> = ∅}@}
>     {@{<b>foreach</b> (u, v) in E}@} <b>do</b>
>         {@{<b>if</b> weight(u, v) ≤ pivot}@} <b>then</b>
>             {@{E<sub>≤</sub> = E<sub>≤</sub> ∪ {(u, v)}<!-- flashcard separator -->}@}
>         <b>else</b>
>             {@{E<sub>&gt;</sub> = E<sub>&gt;</sub> ∪ {(u, v)}<!-- flashcard separator -->}@}
>     {@{<b>return</b> E<sub>≤</sub>, E<sub>&gt;</sub>}@}
>
> {@{<b>function</b> filter(E)}@} <b>is</b>
>     {@{E<sub>f</sub> = ∅}@}
>     {@{<b>foreach</b> (u, v) in E}@} <b>do</b>
>         {@{<b>if</b> find_set(u) ≠ find_set(v)}@} <b>then</b>
>             {@{E<sub>f</sub> = E<sub>f</sub> ∪ {(u, v)}<!-- flashcard separator -->}@}
>     {@{<b>return</b> E<sub>f</sub>}@}
> </pre> <!--SR:!2025-10-28,261,330!2025-02-16,66,310!2025-10-16,251,330!2025-02-18,67,310!2025-05-09,114,290!2025-02-16,66,310!2025-02-12,63,310!2025-02-14,31,250!2025-11-04,267,330!2025-02-17,67,310!2025-10-24,258,330!2025-02-11,62,310!2025-10-23,257,330!2025-08-05,180,310!2025-02-11,62,310!2025-02-18,67,310!2025-02-12,63,310!2025-02-17,67,310!2025-02-16,66,310!2025-03-26,79,270!2025-02-17,66,310!2025-02-18,67,310-->

Filter-Kruskal {@{lends itself better to parallelization}@} as {@{sorting, filtering, and partitioning can easily be performed in parallel}@} by {@{distributing the edges between the processors}@}.<sup>[\[7\]](#^ref-7)</sup> <!--SR:!2025-02-12,63,310!2025-10-22,256,330!2025-02-12,63,310-->

Finally, {@{other variants of a parallel implementation of Kruskal's algorithm}@} have been explored. Examples include {@{a scheme that uses helper threads to remove edges that are definitely not part of the MST in the background}@},<sup>[\[8\]](#^ref-8)</sup> and a variant which {@{runs the sequential algorithm on _p_ subgraphs, then merges those subgraphs until only one, the final MST, remains}@}.<sup>[\[9\]](#^ref-9)</sup> <!--SR:!2025-02-16,66,310!2025-02-11,62,310!2025-10-10,246,330-->

## see also

- [Prim's algorithm](Prim's%20algorithm.md)
- [Dijkstra's algorithm](Dijkstra's%20algorithm.md)
- [Borůvka's algorithm](Borůvka's%20algorithm.md)
- [reverse-delete algorithm](reverse-delete%20algorithm.md)
- [single-linkage clustering](single-linkage%20clustering.md)
- [greedy geometric spanner](greedy%20geometric%20spanner.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Kruskal's_algorithm) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. Kleinberg, Jon \(2006\). [_Algorithm design_](https://www.worldcat.org/oclc/57422612). Éva Tardos. Boston: Pearson/Addison-Wesley. pp. 142–151. [ISBN](ISBN.md) [0-321-29535-8](https://en.wikipedia.org/wiki/Special:BookSources/0-321-29535-8). [OCLC](OCLC.md#OCLC) [57422612](https://search.worldcat.org/oclc/57422612). <a id="^ref-1"></a>^ref-1
2. Cormen, Thomas; Charles E Leiserson, Ronald L Rivest, Clifford Stein \(2009\). [_Introduction To Algorithms_](https://archive.org/details/introductiontoal00corm_805) \(Third ed.\). MIT Press. pp. [631](https://archive.org/details/introductiontoal00corm_805/page/n651). [ISBN](ISBN.md) [978-0262258104](https://en.wikipedia.org/wiki/Special:BookSources/978-0262258104). <a id="^ref-2"></a>^ref-2
3. [Kruskal, J. B.](Joseph%20Kruskal.md) \(1956\). ["On the shortest spanning subtree of a graph and the traveling salesman problem"](https://doi.org/10.1090%2FS0002-9939-1956-0078686-7). _[Proceedings of the American Mathematical Society](Proceedings%20of%20the%20American%20Mathematical%20Society.md)_. __7__ \(1\): 48–50. [doi](digital%20object%20identifier.md):[10.1090/S0002-9939-1956-0078686-7](https://doi.org/10.1090%2FS0002-9939-1956-0078686-7). [JSTOR](JSTOR.md) [2033241](https://www.jstor.org/stable/2033241). <a id="^ref-3"></a>^ref-3
4. Loberman, H.; Weinberger, A. \(October 1957\). ["Formal Procedures for connecting terminals with a minimum total wire length"](https://doi.org/10.1145%2F320893.320896). _Journal of the ACM_. __4__ \(4\): 428–437. [doi](digital%20object%20identifier.md):[10.1145/320893.320896](https://doi.org/10.1145%2F320893.320896). [S2CID](Semantic%20Scholar.md#S2CID) [7320964](https://api.semanticscholar.org/CorpusID:7320964). <a id="^ref-4"></a>^ref-4
5. Quinn, Michael J.; Deo, Narsingh \(1984\). ["Parallel graph algorithms"](https://doi.org/10.1145%2F2514.2515). _ACM Computing Surveys_. __16__ \(3\): 319–348. [doi](digital%20object%20identifier.md):[10.1145/2514.2515](https://doi.org/10.1145%2F2514.2515). [S2CID](Semantic%20Scholar.md#S2CID) [6833839](https://api.semanticscholar.org/CorpusID:6833839). <a id="^ref-5"></a>^ref-5
6. Grama, Ananth; Gupta, Anshul; Karypis, George; Kumar, Vipin \(2003\). _Introduction to Parallel Computing_. Addison-Wesley. pp. 412–413. [ISBN](ISBN.md) [978-0201648652](https://en.wikipedia.org/wiki/Special:BookSources/978-0201648652). <a id="^ref-6"></a>^ref-6
7. Osipov, Vitaly; Sanders, Peter; Singler, Johannes \(2009\). ["The filter-kruskal minimum spanning tree algorithm"](https://doi.org/10.1137%2F1.9781611972894.5). _Proceedings of the Eleventh Workshop on Algorithm Engineering and Experiments \(ALENEX\). Society for Industrial and Applied Mathematics_: 52–61. [doi](digital%20object%20identifier.md):[10.1137/1.9781611972894.5](https://doi.org/10.1137%2F1.9781611972894.5). [ISBN](ISBN.md) [978-0-89871-930-7](https://en.wikipedia.org/wiki/Special:BookSources/978-0-89871-930-7). <a id="^ref-7"></a>^ref-7
8. Katsigiannis, Anastasios; Anastopoulos, Nikos; Konstantinos, Nikas; Koziris, Nectarios \(2012\). "An Approach to Parallelize Kruskal's Algorithm Using Helper Threads". [_2012 IEEE 26th International Parallel and Distributed Processing Symposium Workshops & PhD Forum_](http://tarjomefa.com/wp-content/uploads/2017/10/7793-English-TarjomeFa.pdf) \(PDF\). pp. 1601–1610. [doi](digital%20object%20identifier.md):[10.1109/IPDPSW.2012.201](https://doi.org/10.1109%2FIPDPSW.2012.201). [ISBN](ISBN.md) [978-1-4673-0974-5](https://en.wikipedia.org/wiki/Special:BookSources/978-1-4673-0974-5). [S2CID](Semantic%20Scholar.md#S2CID) [14430930](https://api.semanticscholar.org/CorpusID:14430930). <a id="^ref-8"></a>^ref-8
9. Lončar, Vladimir; Škrbić, Srdjan; Balaž, Antun \(2014\). ["Parallelization of Minimum Spanning Tree Algorithms Using Distributed Memory Architectures"](https://www.researchgate.net/publication/235994104). _Transactions on Engineering Technologies_. pp. 543–554. [doi](digital%20object%20identifier.md):[10.1007/978-94-017-8832-8\_39](https://doi.org/10.1007%2F978-94-017-8832-8_39). [ISBN](ISBN.md) [978-94-017-8831-1](https://en.wikipedia.org/wiki/Special:BookSources/978-94-017-8831-1). <a id="^ref-9"></a>^ref-9

- [Thomas H. Cormen](Thomas%20H.%20Cormen.md), [Charles E. Leiserson](Charles%20E.%20Leiserson.md), [Ronald L. Rivest](Ron%20Rivest.md), and [Clifford Stein](Clifford%20Stein.md). _[Introduction to Algorithms](Introduction%20to%20Algorithms.md)_, Second Edition. MIT Press and McGraw-Hill, 2001. [ISBN](ISBN.md) [0-262-03293-7](https://en.wikipedia.org/wiki/Special:BookSources/0-262-03293-7). Section 23.2: The algorithms of Kruskal and Prim, pp. 567–574.
- [Michael T. Goodrich](Michael%20T.%20Goodrich.md) and [Roberto Tamassia](Roberto%20Tamassia.md). _Data Structures and Algorithms in Java_, Fourth Edition. John Wiley & Sons, Inc., 2006. [ISBN](ISBN.md) [0-471-73884-0](https://en.wikipedia.org/wiki/Special:BookSources/0-471-73884-0). Section 13.7.1: Kruskal's Algorithm, pp. 632..

## external links

- [Data for the article's example](https://github.com/carlschroedl/kruskals-minimum-spanning-tree-algorithm-example-data).
- [Gephi Plugin For Calculating a Minimum Spanning Tree](https://gephi.org/plugins/#/plugin/spanning-tree-plugin) [source code](https://github.com/carlschroedl/gephi-plugins/tree/minimum-spanning-tree-plugin/modules/MinimumSpanningTree).
- [Kruskal's Algorithm with example and program in c++](http://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-using-stl-in-c/)
- [Kruskal's Algorithm code in C++ as applied to random numbers](https://meyavuz.wordpress.com/2017/03/11/how-does-kruskals-algorithm-progress/)
- [Kruskal's Algorithm code in Python with explanation](https://gist.github.com/DanilAndreev/e519d77eff91f03f09616c9170db7941)
