---
aliases:
  - biconnected component
  - biconnected components
tags:
  - flashcard/active/general/eng/biconnected_component
  - language/in/English
---

# biconnected component

- Not to be confused with {@{[vertex cut](vertex%20separator.md)}@}. <!--SR:!2029-11-23,1405,355-->

> {@{![Each color corresponds to a biconnected component. Multi-colored vertices are cut vertices, and thus belong to multiple biconnected components.](../../archives/Wikimedia%20Commons/Graph-Biconnected-Components.svg)}@}
>
> {@{Each color}@} corresponds to {@{a biconnected component}@}. {@{Multi-colored vertices}@} are {@{cut vertices, and thus belong to multiple biconnected components}@}. <!--SR:!2028-02-04,871,335!2029-12-10,1416,355!2027-06-25,498,330!2027-08-02,528,397!2027-06-17,490,397-->

In {@{[graph theory](graph%20theory.md)}@}, {@{a __biconnected component__ or __block__ \(sometimes known as a __2-connected component__\)}@} is {@{a maximal [biconnected](biconnected%20graph.md) [subgraph](glossary%20of%20graph%20theory.md#subgraphs)}@}. {@{Any [connected graph](connectivity%20(graph%20theory).md#connected%20graph)}@} {@{decomposes into a [tree](tree%20(graph%20theory).md) of biconnected components called the __block-cut tree__ of the graph}@}. The blocks are {@{attached to each other at shared [vertices](vertex%20(graph%20theory).md)}@} called {@{__cut vertices__ or __separating vertices__ or __articulation points__}@}. Specifically, a __cut vertex__ is {@{any vertex whose removal increases the number of [connected components](component%20(graph%20theory).md)}@}.<sup>[\[1\]](#^ref-1)</sup> {@{A block containing at most one cut vertex}@} is called {@{a __leaf block__}@}, it corresponds to {@{a [leaf vertex](vertex%20(graph%20theory).md#types%20of%20vertices) in the block-cut tree}@}. <!--SR:!2027-11-23,815,330!2027-05-19,618,315!2028-02-07,861,335!2028-02-10,875,335!2026-08-04,383,315!2028-11-17,1109,350!2029-02-25,1191,355!2029-03-13,1200,350!2029-02-14,1123,310!2029-03-16,1207,355!2027-01-31,565,315-->

## algorithms

### linear time depth-first search

{@{The classic [sequential algorithm](sequential%20algorithm.md) for computing biconnected components in a connected [undirected graph](graph%20(discrete%20mathematics).md#undirected%20graph)}@} is due to {@{[John Hopcroft](John%20Hopcroft.md) and [Robert Tarjan](Robert%20Tarjan.md) \(1973\)}@}.<sup>[\[2\]](#^ref-2)</sup> It runs in {@{[linear time](time%20complexity.md#linear%20time)}@}, and is {@{based on [depth-first search](depth-first%20search.md)}@}. This algorithm is also outlined as {@{Problem 22-2 of [Introduction to Algorithms](Introduction%20to%20Algorithms.md) \(both 2nd and 3rd editions\)}@}. <!--SR:!2026-03-23,333,290!2026-12-02,484,270!2028-11-09,1101,350!2027-10-01,775,335!2027-11-04,754,290-->

The idea is to {@{run a depth-first search while maintaining the following information}@}: <!--SR:!2029-01-24,1163,350-->

1. depth ::@:: the depth of each vertex in the depth-first-search tree \(once it gets visited\), and <!--SR:!2029-12-06,1412,355!2027-07-04,638,315-->
2. lowpoint ::@:: for each vertex _v_, the lowest depth of neighbors of all descendants of _v_ \(including _v_ itself\) in the depth-first-search tree, called the __lowpoint__. <!--SR:!2026-03-27,331,290!2026-09-30,486,315-->

The depth is {@{standard to maintain during a depth-first search}@}. The lowpoint of _v_ can be {@{computed after visiting all descendants of _v_ \(i.e., just before _v_ gets popped off the depth-first-search [stack](stack%20(abstract%20data%20type).md)\)}@} as {@{the minimum of the depth of _v_, the depth of all neighbors of _v_ \(other than the parent of _v_ in the depth-first-search tree\) and the lowpoint of all children of _v_ in the depth-first-search tree}@}. <!--SR:!2029-02-14,1178,350!2026-10-11,493,310!2026-08-14,367,255-->

The key fact is that {@{a nonroot vertex _v_ is a cut vertex \(or articulation point\) separating two biconnected components}@} {@{if and only if there is a child _y_ of _v_ such that lowpoint\(_y_\) ≥ depth\(_v_\)}@}. {@{This property can be tested}@} once {@{the depth-first search returned from every child of _v_ \(i.e., just before _v_ gets popped off the depth-first-search stack\)}@}, and if {@{__true__, _v_ separates the graph into different biconnected components}@}. This can be represented by {@{computing one biconnected component out of every such _y_ \(a component which contains _y_ will contain the subtree of _y_, plus _v_\)}@}, and {@{then erasing the subtree of _y_ from the tree}@}. <!--SR:!2028-06-02,904,295!2027-05-01,655,330!2027-03-23,625,330!2027-05-05,564,275!2028-04-24,921,335!2026-04-08,337,295!2026-10-14,498,315-->

{@{The root vertex must be handled separately}@}: it is {@{a cut vertex if and only if it has at least two children in the DFS tree}@}. Thus, it {@{suffices to simply build one component out of each child subtree of the root \(including the root\)}@}. <!--SR:!2029-08-16,1313,355!2028-02-26,871,330!2026-11-05,512,315-->

### pseudocode

<pre>
<u>GetArticulationPoints(i, d)</u>
    visited[i]&nbsp;:= <b>true</b>
    depth[i]&nbsp;:= d
    low[i]&nbsp;:= d
    childCount&nbsp;:= 0
    isArticulation&nbsp;:= <b>false</b>

    <b>for each</b> ni <b>in</b> adj[i] <b>do</b>
        <b>if</b> <b>not</b> visited[ni] <b>then</b>
            parent[ni]&nbsp;:= i
            GetArticulationPoints(ni, d + 1)
            childCount&nbsp;:= childCount + 1
            <b>if</b> low[ni] ≥ depth[i] <b>then</b>
                isArticulation&nbsp;:= <b>true</b>
            low[i]&nbsp;:= Min (low[i], low[ni])
        <b>else if</b> ni ≠ parent[i] <b>then</b>
            low[i]&nbsp;:= Min (low[i], depth[ni])
    <b>if</b> (parent[i] ≠ <b>null</b> <b>and</b> isArticulation) <b>or</b> (parent[i] = <b>null</b> <b>and</b> childCount &gt; 1) <b>then</b>
        Output i as articulation point
</pre>

> [!info]- code
>
> ```pseudocode
> GetArticulationPoints(i, d)
>     visited[i] := true
>     depth[i] := d
>     low[i] := d
>     childCount := 0
>     isArticulation := false
>
>     for each ni in adj[i] do
>         if not visited[ni] then
>             parent[ni] := i
>             GetArticulationPoints(ni, d + 1)
>             childCount := childCount + 1
>             if low[ni] ≥ depth[i] then
>                 isArticulation := true
>             low[i] := Min (low[i], low[ni])
>         else if ni ≠ parent[i] then
>             low[i] := Min (low[i], depth[ni])
>     if (parent[i] ≠ null and isArticulation) or (parent[i] = null and childCount > 1) then
>         Output i as articulation point
> ```

<!-- markdownlint MD028 -->

> __code flashcards__
>
> <pre>
> {@{<u>GetArticulationPoints(i, d)</u>}@}
>     {@{visited[i]&nbsp;:= <b>true</b>}@}
>     {@{depth[i]&nbsp;:= d}@}
>     {@{low[i]&nbsp;:= d}@}
>     {@{childCount&nbsp;:= 0}@}
>     {@{isArticulation&nbsp;:= <b>false</b>}@}
>
>     {@{<b>for each</b> ni <b>in</b> adj[i]}@} <b>do</b>
>         {@{<b>if</b> <b>not</b> visited[ni]}@} <b>then</b>
>             {@{parent[ni]&nbsp;:= i}@}
>             {@{GetArticulationPoints(ni, d + 1)}@}
>             {@{childCount&nbsp;:= childCount + 1}@}
>             <b>if</b> {@{low[ni] ≥ depth[i]}@} <b>then</b>
>                 {@{isArticulation&nbsp;:= <b>true</b>}@}
>             {@{low[i]&nbsp;:= Min (low[i], low[ni])}@}
>         {@{<b>else if</b> ni ≠ parent[i]}@} <b>then</b>
>             {@{low[i]&nbsp;:= Min (low[i], depth[ni])}@}
>     {@{<b>if</b> (parent[i] ≠ <b>null</b> <b>and</b> isArticulation) <b>or</b> (parent[i] = <b>null</b> <b>and</b> childCount &gt; 1)}@} <b>then</b>
>         {@{Output i as articulation point}@}
> </pre> <!--SR:!2029-11-12,1395,355!2029-03-15,1207,355!2029-08-19,1316,355!2026-10-18,501,315!2029-08-24,1321,355!2029-10-08,1366,355!2028-04-03,865,335!2029-03-22,1212,355!2029-03-30,1219,355!2027-11-23,769,290!2026-09-10,467,310!2027-04-17,552,275!2028-01-31,855,330!2027-06-20,628,315!2026-10-19,501,315!2026-09-04,416,295!2026-09-22,426,295!2026-09-24,480,310-->

<!-- markdownlint MD028 -->

> {@{![A demo of Tarjan's algorithm to find cut vertices. __D__ denotes depth and __L__ denotes lowpoint.](../../archives/Wikimedia%20Commons/TarjanAPDemoDepth.gif)}@}
>
> {@{A demo of Tarjan's algorithm to find cut vertices. __D__ denotes depth and __L__ denotes lowpoint.}@} <!--SR:!2026-07-01,381,295!2027-01-28,526,275-->

### other algorithms

{@{A simple alternative to the above algorithm}@} uses {@{[chain decompositions](Dilworth's%20theorem.md)}@}, which are {@{special ear decompositions depending on [DFS](depth-first%20search.md)-trees}@}.<sup>[\[3\]](#^ref-3)</sup> Chain decompositions can be {@{computed in linear time by this [traversing rule](bridge%20(graph%20theory).md#bridge-finding%20with%20chain%20decompositions)}@}. Let {@{_C_ be a chain decomposition of _G_}@}. Then {@{_G_ is 2-vertex-connected}@} {@{if and only if _G_ has minimum [degree](degree%20(graph%20theory).md) 2 and _C_<sub>1</sub> is the only [cycle](cycle%20(graph%20theory).md) in _C_}@}. This gives immediately {@{a linear-time 2-connectivity test}@} and can be {@{extended to list all cut vertices of _G_ in linear time using the following statement}@}: {@{A vertex _v_ in a connected graph _G_ \(with minimum degree 2\) is a cut vertex}@} {@{if and only if _v_ is incident to a [bridge](bridge%20(graph%20theory).md) or _v_ is the first vertex of a cycle in _C_ – _C_<sub>1</sub>}@}. {@{The list of cut vertices}@} can be used to {@{create the [block-cut tree](#block-cut%20tree) of _G_ in linear time}@}. <!--SR:!2029-07-06,1293,355!2029-06-23,1283,355!2029-03-19,1209,355!2027-11-29,820,330!2026-09-16,473,310!2029-10-03,1361,355!2028-05-21,893,295!2028-01-13,857,335!2029-09-08,1290,315!2026-09-12,468,310!2026-08-22,370,255!2027-11-19,812,330!2026-04-01,334,290-->

In {@{the [online](online%20algorithm.md) version of the problem}@}, {@{vertices and edges are added \(but not removed\) dynamically}@}, and {@{a data structure must maintain the biconnected components}@}. {@{[Jeffery Westbrook](Jeffery%20Westbrook.md) and [Robert Tarjan](Robert%20Tarjan.md) \(1992\)}@} <sup>[\[4\]](#^ref-4)</sup> developed {@{an efficient data structure for this problem based on [disjoint-set data structures](disjoint-set%20data%20structure.md)}@}. Specifically, it {@{processes _n_ vertex additions and _m_ edge additions in _O_\(_m_ _α_\(_m_, _n_\)\) total time}@}, where {@{_α_ is the [inverse Ackermann function](Ackermann%20function.md#inverse)}@}. This time bound is {@{proved to be optimal}@}. <!--SR:!2029-10-22,1377,355!2029-03-26,1216,355!2027-07-15,710,330!2027-11-14,767,295!2029-05-16,1189,310!2028-02-09,832,295!2028-08-26,958,295!2028-10-09,999,335-->

{@{[Uzi Vishkin](Uzi%20Vishkin.md) and [Robert Tarjan](Robert%20Tarjan.md) \(1985\)}@} <sup>[\[5\]](#^ref-5)</sup> designed {@{a [parallel algorithm](parallel%20algorithm.md) on CRCW [PRAM](parallel%20RAM.md)}@} that {@{runs in _O_\(log _n_\) time with _n_ + _m_ processors}@}. <!--SR:!2027-03-04,520,255!2027-12-29,844,335!2028-10-12,971,275-->

## related structures

### equivalence relation

One can define {@{a [binary relation](binary%20relation.md) on the edges of an arbitrary undirected graph}@}, according to {@{which two edges _e_ and _f_ are related if and only if either _e_ = _f_ or the graph contains a [simple cycle](cycle%20(graph%20theory).md) through both _e_ and _f_}@}. Every edge is {@{related to itself}@}, and an edge _e_ is {@{related to another edge _f_ if and only if _f_ is related in the same way to _e_}@}. Less obviously, this is {@{a [transitive relation](transitive%20relation.md)}@}: if {@{there exists a simple cycle containing edges _e_ and _f_, and another simple cycle containing edges _f_ and _g_}@}, then {@{one can combine these two cycles to find a simple cycle through _e_ and _g_}@}. Therefore, {@{this is an [equivalence relation](equivalence%20relation.md)}@}, and it can be {@{used to partition the edges into equivalence classes}@}, {@{subsets of edges with the property}@} that {@{two edges are related to each other if and only if they belong to the same equivalence class}@}. {@{The subgraphs formed by the edges in each equivalence class}@} are {@{the biconnected components of the given graph}@}. Thus, {@{the biconnected components}@} {@{partition the edges of the graph}@}; however, they may share {@{vertices with each other}@}.<sup>[\[6\]](#^ref-6)</sup> <!--SR:!2029-06-02,1263,350!2029-02-19,1186,355!2026-10-15,496,310!2029-11-01,1386,355!2029-06-30,1288,355!2028-01-21,863,335!2027-01-10,548,310!2029-03-27,1216,355!2026-04-13,342,290!2029-06-28,1287,355!2029-06-10,1216,310!2029-08-20,1317,355!2029-10-14,1369,355!2029-03-29,1218,355!2026-11-12,517,310!2029-08-21,1318,355-->

### block graph

{@{The __block graph__ of a given graph _G_}@} is {@{the [intersection graph](intersection%20graph.md) of its blocks}@}. Thus, it has {@{one vertex for each block of _G_}@}, and {@{an edge between two vertices whenever the corresponding two blocks share a vertex}@}. {@{A graph _H_ is the block graph of another graph _G_}@} {@{exactly when all the blocks of _H_ are complete subgraphs}@}. (annotation: Consider {@{two vertices _a_ and _b_ in the same block of _H_}@}. Since they are in the same block, {@{there is a cycle _C_ in the block containing _a_ and _b_}@}. If {@{_a_ and _b_ are adjacent in _C_ then they already have an edge between them}@}. Otherwise, {@{assume there is no edge between them}@}. Let {@{_A_ and _B_}@} respectively be {@{the blocks in _G_ represented by _a_ and _b_ in _H_}@}. {@{The cycle _C_ without an edge between _a_ and _b_}@} means {@{_A_ is connected to one or more non-_B_ blocks via an articulation point, and then said non-_B_ blocks are connected to _B_ via another articulation point, and then similarly from _B_ to _A_}@}. But then {@{the articulation points mentioned above}@} are {@{not articulation points in the first place}@}, since {@{removing them does not make the graph disconnected}@}. This is {@{a contradiction, and so there must an edge between _a_ and _b_}@}. Thus, {@{blocks of _H_ are complete subgraphs}@}.) {@{The graphs _H_ with this property}@} are known as {@{the [block graphs](block%20graph.md)}@}.<sup>[\[7\]](#^ref-7)</sup> <!--SR:!2026-11-16,523,315!2029-03-02,1195,355!2026-10-05,490,315!2027-08-22,743,330!2028-08-14,946,295!2026-10-26,502,310!2027-06-19,697,335!2029-11-13,1396,355!2028-12-13,1127,356!2026-03-26,356,356!2028-02-09,823,336!2027-06-25,693,336!2027-01-21,522,316!2027-12-14,776,336!2027-11-03,746,336!2028-12-22,1139,356!2029-03-19,1189,356!2029-04-10,1207,356!2027-05-22,458,398!2027-06-16,479,398!2027-06-20,485,400-->

### block-cut tree

{@{A __cutpoint__, __cut vertex__, or __articulation point__ of a graph _G_}@} is {@{a vertex that is shared by two or more blocks}@}. {@{The structure of the blocks and cutpoints of a connected graph}@} can be described by {@{a [tree](tree%20(graph%20theory).md) called the __block-cut tree__ or __BC-tree__}@}. This tree has {@{a vertex for each block and for each articulation point of the given graph}@}. There is {@{an edge in the block-cut tree for each pair of a block and an articulation point that belongs to that block}@}.<sup>[\[8\]](#^ref-8)</sup> <!--SR:!2026-11-07,514,310!2029-08-25,1322,355!2028-01-14,857,335!2026-11-26,530,315!2026-09-01,413,295!2026-03-03,317,290-->

> {@{![A graph, and is block-cut tree.](../../archives/Wikimedia%20Commons/Block-cut%20tree2.svg)}@}
>
> {@{A graph, and its block-cut tree.}@} <br/>
> __Blocks__: <br/>
> _b_<sub>1</sub> = \[1,2\] <br/>
> _b_<sub>2</sub> = \[2,3,4\] <br/>
> _b_<sub>3</sub> = \[2,5,6,7\] <br/>
> _b_<sub>4</sub> = \[7,8,9,10,11\] <br/>
> _b_<sub>5</sub> = \[8,12,13,14,15\] <br/>
> _b_<sub>6</sub> = \[10,16\] <br/>
> _b_<sub>7</sub> = \[10,17,18\] <br/>
> __Cutpoints:___<br/>
> c_<sub>1</sub> = 2 <br/>
> _c_<sub>2</sub> = 7 <br/>
> _c_<sub>3</sub> = 8 <br/>
> _c_<sub>4</sub> = 10 <!--SR:!2027-10-02,775,335!2029-08-16,1313,355-->

## see also

- [Triconnected component](SPQR%20tree.md)
- [Bridge \(graph theory\)](bridge%20(graph%20theory).md)
- [Single-entry single-exit](single-entry%20single-exit.md) ::@:: Counter part of biconnected components in directed graphs <!--SR:!2026-10-06,491,315!2028-01-17,860,335-->

## notes

1. <a id="CITEREFAL-TAIE2019"></a> AL-TAIE, MOHAMMED ZUHAIR. KADRY, SEIFEDINE \(2019\). "3. Graph Theory". _PYTHON FOR GRAPH AND NETWORK ANALYSIS_. SPRINGER. [ISBN](ISBN.md) [978-3-319-85037-5](https://en.wikipedia.org/wiki/Special:BookSources/978-3-319-85037-5). [OCLC](OCLC.md#OCLC) [1047552679](https://search.worldcat.org/oclc/1047552679). A cut-vertex is a vertex that if removed, the number of network components increases. <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFHopcroftTarjan1973"></a> Hopcroft, J.; Tarjan, R. \(1973\). ["Algorithm 447: efficient algorithms for graph manipulation"](https://doi.org/10.1145%2F362248.362272). _Communications of the ACM_. __16__ \(6\): 372–378. [doi](digital%20object%20identifier.md):[10.1145/362248.362272](https://doi.org/10.1145%2F362248.362272). <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFSchmidt2013"></a> [Schmidt, Jens M.](Jens%20M.%20Schmidt.md) \(2013\), "A Simple Test on 2-Vertex- and 2-Edge-Connectivity", _Information Processing Letters_, __113__ \(7\): 241–244, [arXiv](ArXiv.md):[1209.0700](https://arxiv.org/abs/1209.0700), [doi](digital%20object%20identifier.md):[10.1016/j.ipl.2013.01.016](https://doi.org/10.1016%2Fj.ipl.2013.01.016). <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFWestbrookTarjan1992"></a> Westbrook, J.; Tarjan, R. E. \(1992\). "Maintaining bridge-connected and biconnected components on-line". _Algorithmica_. __7__ \(1–6\): 433–464. [doi](digital%20object%20identifier.md):[10.1007/BF01758773](https://doi.org/10.1007%2FBF01758773). <a id="^ref-4"></a>^ref-4
5. <a id="CITEREFTarjanVishkin1985"></a> Tarjan, R.; Vishkin, U. \(1985\). "An Efficient Parallel Biconnectivity Algorithm". _[SIAM J. Comput.](SIAM%20Journal%20on%20Computing.md)_ __14__ \(4\): 862–874. [CiteSeerX](CiteSeerX.md) [10.1.1.465.8898](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.465.8898). [doi](digital%20object%20identifier.md):[10.1137/0214061](https://doi.org/10.1137%2F0214061). <a id="^ref-5"></a>^ref-5
6. [Tarjan & Vishkin \(1985\)](#CITEREFTarjanVishkin1985) credit the definition of this equivalence relation to [Harary \(1969\)](#CITEREFHarary1969); however, Harary does not appear to describe it in explicit terms. <a id="^ref-6"></a>^ref-6
7. <a id="CITEREFHarary1969"></a> [Harary, Frank](Frank%20Harary.md) \(1969\), _Graph Theory_, Addison-Wesley, p. 29. <a id="^ref-7"></a>^ref-7
8. [Harary \(1969\)](#CITEREFHarary1969), p. 36. <a id="^ref-8"></a>^ref-8

## references

This text incorporates [content](https://en.wikipedia.org/wiki/biconnected_component) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- <a id="CITEREFEugene C. Freuder1985"></a> [Eugene C. Freuder](Eugene%20C.%20Freuder.md) \(1985\). ["A Sufficient Condition for Backtrack-Bounded Search"](https://doi.org/10.1145%2F4221.4225). _Journal of the Association for Computing Machinery_. __32__ \(4\): 755–761. [doi](digital%20object%20identifier.md):[10.1145/4221.4225](https://doi.org/10.1145%2F4221.4225).

## external links

- [C++ implementation of Biconnected Components](http://www.geeksforgeeks.org/biconnected-components/)

> [Category](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Graph connectivity](https://en.wikipedia.org/wiki/Category:Graph%20connectivity)
