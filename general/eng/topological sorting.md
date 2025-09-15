---
aliases:
  - topological sort
  - topological sorting
  - topological sortings
  - topological sorts
tags:
  - flashcard/active/general/eng/topological_sorting
  - language/in/English
---

# topological sorting

- {@{"Dependency resolution"}@} redirects here. For other uses, see {@{[dependency \(disambiguation\)](dependency.md)}@}. <!--SR:!2026-03-01,361,358!2026-03-22,377,358-->

In {@{[computer science](computer%20science.md)}@}, {@{a __topological sort__ or __topological ordering__}@} of {@{a [directed graph](directed%20graph.md) is a [linear ordering](total%20order.md) of its [vertices](vertex%20(graph%20theory).md) such that for every directed edge _\(u,v\)_ from vertex _u_ to vertex _v_, _u_ comes before _v_ in the ordering}@}. For instance, {@{the vertices of the graph may represent tasks to be performed}@}, and {@{the edges may represent constraints that one task must be performed before another}@}; in this application, {@{a topological ordering is just a valid sequence for the tasks}@}. Precisely, a topological sort is {@{a graph traversal in which each node _v_ is visited only after all its dependencies are visited}@}. A topological ordering is {@{possible if and only if the graph has no [directed cycles](cycle%20(graph%20theory).md)}@}, that is, if {@{it is a [directed acyclic graph](directed%20acyclic%20graph.md) \(DAG\)}@}. Any DAG has {@{at least one topological ordering}@}, and [algorithms](algorithm.md) are {@{known for constructing a topological ordering of any DAG in [linear time](time%20complexity.md#linear%20time)}@}. Topological sorting has {@{many applications}@}, especially in {@{ranking problems such as [feedback arc set](feedback%20arc%20set.md)}@}. Topological sorting is also possible when {@{the DAG has [disconnected components](connectivity%20(graph%20theory).md)}@}. <!--SR:!2026-04-08,396,371!2026-01-28,318,359!2026-05-04,417,371!2028-06-16,1010,358!2026-05-28,437,379!2026-04-27,411,371!2028-04-01,942,347!2026-01-03,313,359!2026-01-08,318,359!2026-04-09,397,371!2026-01-05,315,359!2026-04-08,396,371!2026-01-09,319,359!2026-05-04,417,371-->

## examples

> {@{![a directed acyclic graph](../../archives/Wikimedia%20Commons/Directed%20acyclic%20graph%202.svg)}@}
>
> This graph has {@{many valid topological sorts}@}, including:
>
> - {@{5, 7, 3, 11, 8, 2, 9, 10}@} \({@{visual left-to-right, top-to-bottom}@}\)
> - {@{3, 5, 7, 8, 11, 2, 9, 10}@} \({@{smallest-numbered available vertex first}@}\)
> - {@{3, 5, 7, 8, 11, 2, 10, 9}@} \({@{[lexicographic by incoming neighbors](Coffman–Graham%20algorithm.md)}@}\)
> - {@{5, 7, 3, 8, 11, 2, 10, 9}@} \({@{fewest edges first}@}\)
> - {@{7, 5, 11, 3, 10, 8, 9, 2}@} \({@{largest-numbered available vertex first}@}\)
> - {@{5, 7, 11, 2, 3, 8, 9, 10}@} \({@{attempting top-to-bottom, left-to-right}@}\)
> - 3, 7, 8, 5, 11, 10, 2, 9 \({@{arbitrary}@}\) <!--SR:!2026-04-28,412,371!2026-02-10,349,371!2026-02-24,356,358!2026-02-25,361,371!2026-10-14,508,319!2028-06-09,1004,358!2025-12-22,261,298!2025-10-29,265,359!2026-02-22,359,371!2026-01-06,316,359!2028-11-01,1131,371!2027-08-12,768,347!2026-06-22,458,379!2026-06-13,450,379!2026-06-15,452,379-->

{@{The canonical application of topological sorting}@} is {@{in [scheduling](job-shop%20scheduling.md) a sequence of jobs or tasks based on their [dependencies](dependency%20graph.md)}@}. The jobs are {@{represented by vertices}@}, and {@{there is an edge from _x_ to _y_ if job _x_ must be completed before job _y_ can be started}@} \(for example, when {@{washing clothes}@}, {@{the washing machine must finish before we put the clothes in the dryer}@}\). Then, {@{a topological sort gives an order in which to perform the jobs}@}. A closely-related application of topological sorting algorithms was {@{first studied in the early 1960s}@} in {@{the context of the [PERT](program%20evaluation%20and%20review%20technique.md) technique for scheduling in [project management](project%20management.md)}@}.<sup>[\[1\]](#^ref-1)</sup> In this application, {@{the vertices of a graph represent the milestones of a project}@}, and {@{the edges represent tasks that must be performed between one milestone and another}@}. Topological sorting forms {@{the basis of linear-time algorithms for finding the [critical path](critical%20path%20method.md) of the project}@}, {@{a sequence of milestones and tasks that controls the length of the overall project schedule}@}. <!--SR:!2026-06-10,448,379!2026-04-10,398,371!2026-06-13,450,379!2026-06-14,451,379!2026-06-08,446,379!2026-05-26,435,379!2026-05-31,440,379!2025-10-10,247,338!2026-05-18,428,379!2025-12-28,309,347!2026-04-28,411,371!2026-04-02,388,358!2027-05-16,690,338-->

In computer science, applications of this type arise in [instruction scheduling](instruction%20scheduling.md), {@{ordering of formula cell evaluation}@} when {@{recomputing formula values in [spreadsheets](spreadsheet.md)}@}, [logic synthesis](logic%20synthesis.md), determining {@{the order of compilation tasks to perform}@} in {@{[makefiles](make%20(software).md#makefile)}@}, data {@{[serialization](serialization.md)}@}, and {@{resolving symbol dependencies}@} in {@{[linkers](linker%20(computing).md)}@}. It is also used to {@{decide in which order}@} to {@{load tables with foreign keys in databases}@}. <!--SR:!2025-12-26,308,354!2026-01-04,314,359!2027-10-16,805,351!2026-05-04,417,371!2025-10-19,252,351!2026-01-02,312,359!2026-02-26,358,358!2026-05-18,429,379!2026-02-05,342,358-->

## algorithms

{@{The usual algorithms for topological sorting}@} have running time {@{linear in the number of nodes plus the number of edges, asymptotically, $O(\left|{V}\right|+\left|{E}\right|).$}@} <!--SR:!2026-06-06,445,379!2026-03-07,367,371-->

### Kahn's algorithm

- Not to be confused with {@{[Kuhn's algorithm](Hungarian%20algorithm.md)}@}. <!--SR:!2026-04-21,406,371-->

One of these algorithms, first described by {@{[Kahn \(1962\)](#^ref-2)}@}, works by {@{choosing vertices in the same order as the eventual topological sort}@}.<sup>[\[2\]](#^ref-2)</sup> First, find {@{a list of "start nodes" that have no incoming edges and insert them into a set S}@}; {@{at least one such node must exist in a non-empty \(finite\) acyclic graph}@}. Then: <!--SR:!2026-01-06,316,359!2026-04-09,397,371!2026-01-18,328,358!2026-01-07,317,359-->

<pre>
<i>L</i> ← Empty list that will contain the sorted elements
<i>S</i> ← Set of all nodes with no incoming edge

<b>while</b> <i>S</i> <b>is not</b> empty <b>do</b>
    remove a node <i>n</i> from <i>S</i>
    add <i>n</i> to <i>L</i>
    <b>for each</b> node <i>m</i> with an edge <i>e</i> from <i>n</i> to <i>m</i> <b>do</b>
        remove edge <i>e</i> from the graph
        <b>if</b> <i>m</i> has no other incoming edges <b>then</b>
            insert <i>m</i> into <i>S</i>

<b>if</b> <i>graph</i> has edges <b>then</b>
    <b>return</b> error   <i>(graph has at least one cycle)</i>
<b>else</b>
    <b>return</b> <i>L</i>   <i>(a topologically sorted order)</i>
</pre>

> [!info]- code
>
> ```pseudocode
> L ← Empty list that will contain the sorted elements
> S ← Set of all nodes with no incoming edge
> 
> while S is not empty do
>     remove a node n from S
>     add n to L
>     for each node m with an edge e from n to m do
>         remove edge e from the graph
>         if m has no other incoming edges then
>             insert m into S
> 
> if graph has edges then
>     return error   (graph has at least one cycle)
> else 
>     return L   (a topologically sorted order)
> ```

<!-- markdownlint MD028 -->

> __code flashcards__
>
> <pre>
> {@{<i>L</i> ← Empty list that will contain the sorted elements}@}
> {@{<i>S</i> ← Set of all nodes with no incoming edge}@}
>
> {@{<b>while</b> <i>S</i> <b>is not</b> empty}@} <b>do</b>
>     {@{remove a node <i>n</i> from <i>S</i>}@}
>     {@{add <i>n</i> to <i>L</i>}@}
>     {@{<b>for each</b> node <i>m</i> with an edge <i>e</i> from <i>n</i> to <i>m</i>}@} <b>do</b>
>         {@{remove edge <i>e</i> from the graph}@}
>         {@{<b>if</b> <i>m</i> has no other incoming edges}@} <b>then</b>
>             {@{insert <i>m</i> into <i>S</i>}@}
>
> {@{<b>if</b> <i>graph</i> has edges}@} <b>then</b>
>     {@{<b>return</b> error   <i>(graph has at least one cycle)</i>}@}
> <b>else</b>
>     {@{<b>return</b> <i>L</i>   <i>(a topologically sorted order)</i>}@}
> </pre> <!--SR:!2026-06-17,454,379!2026-04-29,412,371!2026-03-30,385,358!2026-03-16,373,358!2028-04-13,941,347!2026-01-05,315,359!2026-04-30,413,371!2026-04-19,404,371!2026-01-26,316,359!2026-05-25,435,379!2026-05-31,439,379!2026-04-13,398,371-->

If {@{the graph is a [DAG](directed%20acyclic%20graph.md)}@}, {@{a solution will be contained in the list L \(although the solution is not necessarily unique\)}@}. Otherwise, {@{the graph must have at least one cycle and therefore a topological sort is impossible}@}. <!--SR:!2026-06-21,457,379!2026-04-05,393,371!2027-09-20,784,339-->

Reflecting {@{the non-uniqueness of the resulting sort}@}, {@{the structure S can be simply a set or a queue or a stack}@}. Depending on {@{the order that nodes n are removed from set S}@}, {@{a different solution is created}@}. {@{A variation of Kahn's algorithm that breaks ties [lexicographically](lexicographic%20order.md)}@} forms {@{a key component of the [Coffman–Graham algorithm](Coffman–Graham%20algorithm.md) for parallel scheduling and [layered graph drawing](layered%20graph%20drawing.md)}@}. <!--SR:!2026-01-17,327,358!2026-05-20,431,379!2025-12-05,289,339!2025-12-10,293,339!2027-03-21,632,334!2026-09-02,466,318-->

### depth-first search

{@{An alternative algorithm for topological sorting}@} is {@{based on [depth-first search](depth-first%20search.md)}@}. The algorithm {@{loops through each node of the graph, in an arbitrary order}@}, initiating {@{a depth-first search that terminates when it hits any node that has already been visited}@} since {@{the beginning of the topological sort or the node has no outgoing edges \(i.e., a leaf node\)}@}: <!--SR:!2025-11-05,271,359!2026-01-09,319,359!2026-04-07,395,371!2028-10-26,1124,371!2025-10-30,266,359-->

<pre>
<i>L</i> ← Empty list that will contain the sorted nodes
<b>while</b> exists nodes without a permanent mark <b>do</b>
    select an unmarked node <i>n</i>
    visit(<i>n</i>)

<b>function</b> visit(node <i>n</i>)
    <b>if</b> <i>n</i> has a permanent mark <b>then</b>
        <b>return</b>
    <b>if</b> <i>n</i> has a temporary mark <b>then</b>
        <b>stop</b>   <i>(graph has at least one cycle)</i>

    mark <i>n</i> with a temporary mark

    <b>for each</b> node <i>m</i> with an edge from <i>n</i> to <i>m</i> <b>do</b>
        visit(<i>m</i>)

    mark <i>n</i> with a permanent mark
    add <i>n</i> to head of <i>L</i>
</pre>

> [!info]- code
>
> ```pseudocode
> L ← Empty list that will contain the sorted nodes
> while exists nodes without a permanent mark do
>     select an unmarked node n
>     visit(n)
> 
> function visit(node n)
>     if n has a permanent mark then
>         return
>     if n has a temporary mark then
>         stop   (graph has at least one cycle)
> 
>     mark n with a temporary mark
> 
>     for each node m with an edge from n to m do
>         visit(m)
> 
>     mark n with a permanent mark
>     add n to head of L
> ```

<!-- markdownlint MD028 -->

> __code flashcards__
>
> <pre>
> {@{<i>L</i> ← Empty list that will contain the sorted nodes}@}
> {@{<b>while</b> exists nodes without a permanent mark}@} <b>do</b>
>     {@{select an unmarked node <i>n</i>}@}
>     {@{visit(<i>n</i>)}@}
>
> <b>function</b> {@{visit(node <i>n</i>)}@}
>     {@{<b>if</b> <i>n</i> has a permanent mark}@} <b>then</b>
>         {@{<b>return</b>}@}
>     {@{<b>if</b> <i>n</i> has a temporary mark}@} <b>then</b>
>         {@{<b>stop</b>   <i>(graph has at least one cycle)</i>}@}
>
>     {@{mark <i>n</i> with a temporary mark}@}
>
>     {@{<b>for each</b> node <i>m</i> with an edge from <i>n</i> to <i>m</i>}@} <b>do</b>
>         {@{visit(<i>m</i>)}@}
>
>     {@{mark <i>n</i> with a permanent mark}@}
>     {@{add <i>n</i> to head of <i>L</i>}@}
> </pre> <!--SR:!2026-02-10,346,354!2026-05-17,428,379!2027-04-30,618,331!2026-03-28,386,371!2026-03-30,388,371!2026-05-13,424,379!2026-01-26,334,358!2027-05-28,685,338!2026-02-26,362,371!2026-06-18,455,379!2026-04-14,399,371!2026-06-10,448,379!2026-06-21,457,379!2026-05-12,423,379-->

{@{Each node _n_}@} gets {@{_prepended_ to the output list L only after considering all other nodes that depend on _n_ \(all descendants of _n_ in the graph\)}@}. Specifically, when {@{the algorithm adds node _n_}@}, we are guaranteed that {@{all nodes that depend on _n_ are already in the output list L}@}: they were {@{added to L either by the recursive call to visit\(\) that ended before the call to visit _n_, or by a call to visit\(\) that started even before the call to visit _n_}@}. Since {@{each edge and node is visited once}@}, {@{the algorithm runs in linear time}@}. {@{This depth-first-search-based algorithm}@} is {@{the one described by [Cormen et al. \(2001\)](#^ref-3)}@};<sup>[\[3\]](#^ref-3)</sup> it seems to {@{have been first described}@} {@{in print by Tarjan in 1976}@}.<sup>[\[4\]](#^ref-4)</sup> <!--SR:!2026-02-28,360,358!2026-04-23,407,371!2026-05-29,438,379!2026-03-20,376,358!2026-06-07,446,379!2026-05-14,425,379!2026-03-21,377,358!2026-12-05,542,319!2027-12-25,857,351!2026-03-08,368,358!2027-11-17,830,351-->

### parallel algorithms

On {@{a [parallel random-access machine](Parallel%20RAM.md)}@}, {@{a topological ordering can be constructed in _O_\(\(log _n_\)<sup>2</sup>\) time}@} using {@{a polynomial number of processors}@}, {@{putting the problem into the complexity class __[NC](NC%20(complexity).md)<sup>2</sup>__}@}.<sup>[\[5\]](#^ref-5)</sup> One method for doing this is to {@{repeatedly square the [adjacency matrix](adjacency%20matrix.md) of the given graph}@}, {@{logarithmically many times, using [min-plus matrix multiplication](min-plus%20matrix%20multiplication.md) with maximization in place of minimization}@}. The resulting matrix describes {@{the [longest path](longest%20path%20problem.md) distances in the graph}@}. {@{Sorting the vertices by the lengths of their longest incoming paths}@} produces {@{a topological ordering}@}.<sup>[\[6\]](#^ref-6)</sup> <!--SR:!2026-04-03,389,358!2027-10-16,794,338!2026-05-24,433,379!2026-09-08,450,314!2026-10-13,475,319!2026-02-14,314,339!2026-06-20,456,379!2026-04-26,410,371!2026-03-18,374,358-->

{@{An algorithm for parallel topological sorting on [distributed memory](distributed%20memory.md) machines}@} {@{parallelizes the algorithm of Kahn for a [DAG](directed%20acyclic%20graph.md) $G=(V,E)$}@}.<sup>[\[7\]](#^ref-7)</sup> On a high level, the algorithm of Kahn {@{repeatedly removes the vertices of indegree 0 and adds them to the topological sorting in the order in which they were removed}@}. Since {@{the outgoing edges of the removed vertices are also removed}@}, {@{there will be a new set of vertices of indegree 0}@}, where {@{the procedure is repeated until no vertices are left}@}. This algorithm {@{performs $D+1$ iterations}@}, where {@{_D_ is the longest path in _G_}@}. {@{Each iteration can be parallelized}@}, which is {@{the idea of the following algorithm}@}. <!--SR:!2027-09-23,782,338!2026-01-01,310,339!2026-01-12,322,358!2025-11-10,275,359!2026-03-03,363,358!2025-10-11,248,338!2025-12-19,302,354!2026-05-21,431,379!2026-04-05,393,371!2026-04-06,394,371-->

In the following, it is assumed that {@{the graph partition is stored on _p_ processing elements \(PE\)}@}, which are {@{labeled $0,\dots ,p-1$}@}. Each PE _i_ {@{initializes a set of local vertices $Q_{i}^{1}$ with [indegree](directed%20graph.md#indegree%20and%20outdegree) 0}@}, where the upper index {@{represents the current iteration}@}. Since {@{all vertices in the local sets $Q_{0}^{1},\dots ,Q_{p-1}^{1}$ have indegree 0}@}, i.e., they are {@{not adjacent}@}, they {@{can be given in an arbitrary order for a valid topological sorting}@}. To {@{assign a global index to each vertex}@}, {@{a [prefix sum](prefix%20sum.md) is calculated over the sizes of $Q_{0}^{1},\dots ,Q_{p-1}^{1}$}@}. So, each step, there are {@{$\sum _{i=0}^{p-1}|Q_{i}|$ vertices added to the topological sorting}@}. <!--SR:!2026-02-01,339,358!2026-01-27,317,359!2025-11-14,259,351!2026-01-25,333,358!2025-12-16,298,347!2026-06-04,443,379!2026-02-06,343,358!2026-06-11,449,379!2026-04-25,409,371!2026-03-02,362,358-->

> ![Execution of the parallel topological sorting algorithm on a DAG with two processing elements.](../../archives/Wikimedia%20Commons/Parallel%20Topological%20Sorting.gif)
>
> {@{Execution of the parallel topological sorting algorithm on a DAG with two processing elements.}@} <!--SR:!2026-03-17,374,358-->

In the first step, PE _j_ assigns {@{the $\lvert Q_j^1 \rvert$ indices $\sum _{i=0}^{j-1}|Q_{i}^{1}|,\dots ,\left(\sum _{i=0}^{j}|Q_{i}^{1}|\right)-1$ (the summation sign is for producing a prefix sum) to the $\lvert Q_j^1 \rvert$ local vertices in $Q_{j}^{1}$}@}. {@{These vertices in $Q_{j}^{1}$}@} are {@{removed, together with their corresponding outgoing edges}@}. For {@{each outgoing edge $(u,v)$ with endpoint _v_ in another PE $l,j\neq l$}@}, {@{the message $(u,v)$ is posted to PE _l_}@}. After {@{all vertices in $Q_{j}^{1}$ are removed}@}, {@{the posted messages are sent to their corresponding PE}@}. {@{Each message $(u,v)$ received}@} {@{updates the indegree of the local vertex _v_}@}. If {@{the indegree drops to zero}@}, {@{_v_ is added to $Q_{j}^{2}$}@}. Then {@{the next iteration starts}@}. <!--SR:!2028-04-04,935,351!2026-06-01,441,379!2026-02-25,357,358!2026-05-19,429,379!2026-04-27,411,371!2027-10-04,796,339!2026-04-24,408,371!2026-04-08,396,371!2026-04-04,393,371!2026-03-31,386,358!2025-12-14,280,338!2026-04-01,387,358-->

In step _k_, PE _j_ assigns {@{the $\lvert Q_j^k \rvert$ indices $a_{k-1}+\sum _{i=0}^{j-1}|Q_{i}^{k}|,\dots ,a_{k-1}+\left(\sum _{i=0}^{j}|Q_{i}^{k}|\right)-1$}@}, where {@{$a_{k-1}$ is the total number of processed vertices after step ⁠$k-1$⁠}@}. This procedure {@{repeats until there are no vertices left to process}@}, {@{hence $\sum _{i=0}^{p-1}|Q_{i}^{D+1}|=0$ (_D_ is the longest path in _G_)}@}. Below is {@{a high level, [single program, multiple data](single%20program,%20multiple%20data.md)}@} pseudo-code overview of this algorithm. <!--SR:!2026-01-08,318,359!2025-12-10,294,351!2025-12-12,296,347!2028-05-24,972,347!2026-04-24,407,371-->

Note that {@{the [prefix sum](prefix%20sum.md#parallel%20algorithms)}@} for {@{the local offsets $a_{k-1}+\sum _{i=0}^{j-1}|Q_{i}^{k}|,\dots ,a_{k-1}+\left(\sum _{i=0}^{j}|Q_{i}^{k}|\right)-1$}@} can be {@{efficiently calculated in parallel}@}. <!--SR:!2026-02-09,345,358!2027-02-13,601,319!2026-06-18,455,379-->

<pre>
<b>p</b> processing elements with IDs from 0 to <i>p</i>-1
<b>Input:</b> G = (V, E) DAG, distributed to PEs, PE index j = 0, ..., p - 1
<b>Output:</b> topological sorting of G

<b>function</b> traverseDAGDistributed
    δ incoming degree of local vertices <i>V</i>
    <span class="texhtml"><i>Q</i> = {<i>v</i> ∈ <i>V</i> | δ[<i>v</i>] = 0}</span>                     // All vertices with indegree 0
    nrOfVerticesProcessed = 0

    <b>do</b>
        <b>global</b> build prefix sum over size of <i>Q</i>     // get offsets and total number of vertices in this step
        offset = nrOfVerticesProcessed + sum(Q<sub>i</sub>, i = 0 to j - 1)          // <i>j</i> is the processor index
        <b>foreach</b> u <b>in</b> Q
            localOrder[u] = index++;
            <b>foreach</b> (u,v) in E <b>do</b> post message (<i>u, v</i>) to PE owning vertex <i>v</i>
        nrOfVerticesProcessed += sum(|Q<sub>i</sub>|, i = 0 to p - 1)
        deliver all messages to neighbors of vertices in Q
        receive messages for local vertices V
        remove all vertices in Q
        <b>foreach</b> message (<i>u, v</i>) received:
            <b>if</b> --δ[v] = 0
                add <i>v</i> to <i>Q</i>
    <b>while</b> global size of <i>Q</i> &gt; 0

    <b>return</b> localOrder
</pre>

> [!info]- code
>
> ```pseudocode
> p processing elements with IDs from 0 to p-1
> Input: G = (V, E) DAG, distributed to PEs, PE index j = 0, ..., p - 1
> Output: topological sorting of G
> 
> function traverseDAGDistributed
>     δ incoming degree of local vertices V
>     Q = {v ∈ V | δ[v] = 0}                     // All vertices with indegree 0
>     nrOfVerticesProcessed = 0
> 
>     do
>         global build prefix sum over size of Q     // get offsets and total number of vertices in this step
>         offset = nrOfVerticesProcessed + sum(Qi, i = 0 to j - 1)          // j is the processor index
>         foreach u in Q
>             localOrder[u] = index++;
>             foreach (u,v) in E do post message (u, v) to PE owning vertex v
>         nrOfVerticesProcessed += sum(|Qi|, i = 0 to p - 1)
>         deliver all messages to neighbors of vertices in Q
>         receive messages for local vertices V
>         remove all vertices in Q
>         foreach message (u, v) received:
>             if --δ[v] = 0
>                 add v to Q
>     while global size of Q > 0
> 
>     return localOrder
> ```

<!-- markdownlint MD028 -->

> __code flashcards__
>
> <pre>
> <b>p</b> {@{processing elements with IDs from 0 to <i>p</i>-1}@}
> <b>Input:</b> {@{G = (V, E) DAG, distributed to PEs, PE index j = 0, ..., p - 1}@}
> <b>Output:</b> {@{topological sorting of G}@}
>
> <b>function</b> {@{traverseDAGDistributed}@}
>     δ {@{incoming degree of local vertices <i>V</i>}@}
>     {@{<span class="texhtml"><i>Q</i> = {<i>v</i> ∈ <i>V</i> | δ[<i>v</i>] = 0}</span>                     // All vertices with indegree 0}@}
>     {@{nrOfVerticesProcessed = 0}@}
>
>     <b>do</b>
>         <b>global</b> {@{build prefix sum over size of <i>Q</i>     // get offsets and total number of vertices in this step}@}
>         {@{offset = nrOfVerticesProcessed + sum(Q<sub>i</sub>, i = 0 to j - 1)          // <i>j</i> is the processor index}@}
>         {@{<b>foreach</b> u <b>in</b> Q}@}
>             {@{localOrder[u] = offset + index++;}@}
>             {@{<b>foreach</b> (u,v) in E}@} <b>do</b> {@{post message (<i>u, v</i>) to PE owning vertex <i>v</i>}@}
>         {@{nrOfVerticesProcessed += sum(|Q<sub>i</sub>|, i = 0 to p - 1)}@}
>         {@{deliver all messages to neighbors of vertices in Q}@}
>         {@{receive messages for local vertices V}@}
>         {@{remove all vertices in Q}@}
>         {@{<b>foreach</b> message (<i>u, v</i>) received}@}:
>             {@{<b>if</b> --δ[v] = 0}@}
>                 {@{add <i>v</i> to <i>Q</i>}@}
>     <b>while</b> {@{global size of <i>Q</i> &gt; 0}@}
>
>     {@{<b>return</b> localOrder}@}
> </pre> <!--SR:!2026-05-22,432,379!2025-10-25,242,351!2026-05-04,417,371!2026-01-30,337,354!2026-05-23,433,379!2026-06-23,459,379!2026-04-10,398,371!2026-06-15,452,379!2026-10-22,516,331!2028-04-29,966,347!2026-02-03,323,359!2026-01-07,318,354!2026-01-19,328,358!2026-03-17,373,358!2026-06-16,453,379!2025-10-06,241,351!2026-06-19,455,379!2026-05-30,438,379!2026-06-09,447,379!2028-05-22,971,347!2026-03-24,380,358!2026-04-18,403,371-->

{@{The communication cost}@} depends {@{heavily on the given graph partition}@}. As for {@{runtime}@}, on {@{a [CRCW-PRAM](parallel%20RAM.md) model that allows fetch-and-decrement in constant time}@}, this algorithm {@{runs in ${\mathcal {O} }\left({\frac {m+n}{p} }+D(\Delta +\log n)\right)$}@}, where {@{_m_ is the number of edges, _n_ is the number of vertices, _D_ is again the longest path in _G_ and _Δ_ the maximum degree}@}.<sup>[\[7\]](#^ref-7)</sup> <!--SR:!2026-02-16,354,371!2027-11-05,808,338!2025-12-10,293,339!2025-11-08,248,298!2026-04-14,224,218!2026-11-14,538,331-->

## application to shortest path finding

{@{The topological ordering}@} can also be used to {@{quickly compute [shortest paths](shortest%20path%20problem.md) through a [weighted](glossary%20of%20graph%20theory.md#weighted%20graph) directed acyclic graph}@}. Let {@{_V_ be the list of vertices in such a graph, in topological order}@}. Then {@{the following algorithm computes the shortest path from some source vertex _s_ to all other vertices}@}:<sup>[\[3\]](#^ref-3)</sup> <!--SR:!2026-06-11,449,379!2026-01-10,320,359!2026-06-24,460,379!2026-03-25,383,371-->

> __outgoing edge variant__
>
> - Let {@{_d_ be an array of the same length as _V_}@}; this will {@{hold the shortest-path distances from _s_}@}. Set {@{_d_\[_s_\] = 0, all other _d_\[_u_\] = ∞}@}.
> - Let {@{_p_ be an array of the same length as _V_, with all elements initialized to nil}@}. Each _p_\[_u_\] will {@{hold the predecessor of _u_ in the shortest path from _s_ to _u_}@}.
> - Loop over {@{the vertices _u_ as ordered in _V_, starting from _s_}@}:
>   - For {@{each vertex _v_ directly following _u_ \(i.e., there exists an edge from _u_ to _v_\)}@}:
>     - Let {@{_w_ be the weight of the edge from _u_ to _v_}@}.
>     - Relax {@{the edge: if _d_\[_v_\] \> _d_\[_u_\] + _w_}@}, set
>       - {@{_d_\[_v_\] ← _d_\[_u_\] + _w_}@},
>       - {@{_p_\[_v_\] ← _u_}@}. <!--SR:!2026-04-04,393,371!2025-10-30,259,351!2026-06-22,458,379!2026-06-07,446,379!2026-06-12,450,379!2026-02-12,330,359!2026-04-07,395,371!2026-01-27,335,358!2025-10-01,218,319!2026-04-16,401,371!2027-03-05,621,334-->

Equivalently:

> __incoming edge variant__
>
> - Let {@{_d_ be an array of the same length as _V_}@}; this will {@{hold the shortest-path distances from _s_}@}. Set {@{_d_\[_s_\] = 0, all other _d_\[_u_\] = ∞}@}.
> - Let {@{_p_ be an array of the same length as _V_, with all elements initialized to nil}@}. Each _p_\[_u_\] will {@{hold the predecessor of _u_ in the shortest path from _s_ to _u_}@}.
> - Loop over {@{the vertices _u_ as ordered in _V_, starting from _s_}@}:
>   - For {@{each vertex _v_ into _u_ \(i.e., there exists an edge from _v_ to _u_\)}@}:
>     - Let {@{_w_ be the weight of the edge from _v_ to _u_}@}.
>     - Relax {@{the edge: if _d_\[_u_\] \> _d_\[_v_\] + _w_}@}, set
>       - {@{_d_\[_u_\] ← _d_\[_v_\] + _w_}@},
>       - {@{_p_\[_u_\] ← _v_}@}. <!--SR:!2026-05-16,427,379!2026-04-09,397,371!2026-02-27,359,358!2026-04-15,400,371!2026-03-26,384,371!2026-02-19,335,359!2026-02-11,347,358!2026-04-28,412,371!2026-03-04,364,358!2026-06-02,441,379!2026-04-27,411,371-->

On {@{a graph of _n_ vertices and _m_ edges}@}, this algorithm {@{takes Θ\(_n_ + _m_\), i.e., [linear](time%20complexity.md#linear%20time), time}@}.<sup>[\[3\]](#^ref-3)</sup> <!--SR:!2026-03-27,382,358!2026-05-27,436,379-->

## uniqueness

If {@{a topological sort has the property that all pairs of consecutive vertices in the sorted order are connected by edges}@}, then {@{these edges form a directed [Hamiltonian path](Hamiltonian%20path.md) in the [DAG](directed%20acyclic%20graph.md)}@}. If {@{a Hamiltonian path exists}@}, {@{the topological sort order is unique; no other order respects the edges of the path}@}. Conversely, if {@{a topological sort does not form a Hamiltonian path}@}, {@{the DAG will have two or more valid topological orderings}@}, for {@{in this case it is always possible to form a second valid ordering by swapping two consecutive vertices that are not connected by an edge to each other}@}. Therefore, it is possible to {@{test in linear time whether a unique ordering exists, and whether a Hamiltonian path exists}@}, despite {@{the [NP-hardness](NP-hardness.md) of the Hamiltonian path problem for more general directed graphs \(i.e., cyclic directed graphs\)}@}.<sup>[\[8\]](#^ref-8)</sup> <!--SR:!2026-06-14,451,379!2026-05-15,426,379!2026-06-03,442,379!2026-06-05,444,379!2026-02-16,354,371!2025-11-09,274,359!2026-03-14,371,358!2026-04-22,407,371!2026-10-12,506,331-->

## relation to partial orders

Topological orderings are also closely related to {@{the concept of a [linear extension](linear%20extension.md) of a [partial order](partially%20ordered%20set.md#partial%20order) in mathematics}@}. {@{A partially ordered set}@} is {@{just a set of objects together with a definition of the "≤" inequality relation}@}, satisfying {@{the axioms of reflexivity \(_x_ ≤ _x_\), antisymmetry \(if _x_ ≤ _y_ and _y_ ≤ _x_ then _x_ = _y_\) and [transitivity](transitive%20relation.md) \(if _x_ ≤ _y_ and _y_ ≤ _z_, then _x_ ≤ _z_\)}@}. A [total order](total%20order.md) is {@{a partial order in which, for every two objects _x_ and _y_ in the set, either _x_ ≤ _y_ or _y_ ≤ _x_}@}. Total orders are {@{familiar in computer science}@} as {@{the comparison operators needed to perform [comparison sorting](comparison%20sort.md) algorithms}@}. For {@{finite sets}@}, total orders may be identified with {@{linear sequences of objects, where the "≤" relation is true whenever the first object precedes the second object in the order}@}; {@{a comparison sorting algorithm}@} may be used to {@{convert a total order into a sequence in this way}@}. {@{A linear extension of a partial order}@} is {@{a total order that is compatible with it}@}, in the sense that, {@{if _x_ ≤ _y_ in the partial order, then _x_ ≤ _y_ in the total order as well}@}. <!--SR:!2026-02-21,358,371!2026-01-24,333,358!2026-05-25,434,379!2026-03-31,389,371!2026-03-19,375,358!2026-01-29,319,359!2026-01-10,320,359!2026-05-19,430,379!2026-03-27,385,371!2026-02-26,358,358!2026-03-26,381,358!2026-03-05,365,358!2026-04-06,394,371!2026-04-20,405,371-->

One can {@{define a partial ordering from any DAG}@} by {@{letting the set of objects be the vertices of the DAG}@}, and {@{defining _x_ ≤ _y_ to be true, for any two vertices _x_ and _y_}@}, whenever {@{there exists a [directed path](path%20(graph%20theory).md) from _x_ to _y_}@}; that is, {@{whenever _y_ is [reachable](reachability.md) from _x_}@}. With these definitions, {@{a topological ordering of the DAG}@} is {@{the same thing as a linear extension of this partial order}@}. Conversely, {@{any partial ordering may be defined as the reachability relation in a DAG}@}. One way of doing this is to {@{define a DAG that has a vertex for every object in the partially ordered set}@}, and {@{an edge _xy_ for every pair of objects for which _x_ ≤ _y_}@}. An alternative way of doing this is to {@{use the [transitive reduction](transitive%20reduction.md) of the partial ordering}@}; in general, this produces {@{DAGs with fewer edges, but the reachability relation in these DAGs is still the same partial order}@}. By {@{using these constructions}@}, one can use {@{topological ordering algorithms to find linear extensions of partial orders}@}. <!--SR:!2026-04-07,395,371!2025-12-05,289,339!2025-12-12,296,347!2026-06-12,450,379!2026-04-10,398,371!2026-02-27,363,371!2026-02-08,347,371!2026-01-23,332,358!2025-12-17,303,359!2026-06-01,440,379!2025-11-09,249,327!2026-03-23,379,358!2025-12-14,297,347!2025-10-20,236,338-->

## relation to scheduling optimisation

By {@{definition}@}, {@{the solution of a scheduling problem that includes a precedence graph}@} is {@{a valid solution to topological sort \(irrespective of the number of machines\)}@}, however, topological sort {@{in itself is _not_ enough to optimally solve a scheduling optimisation problem}@}. {@{Hu's algorithm}@} is {@{a popular method used to solve scheduling problems}@} that {@{require a precedence graph and involve processing times \(where the goal is to minimise the largest completion time amongst all the jobs\)}@}. Like {@{topological sort}@}, {@{Hu's algorithm is not unique and can be solved using DFS \(by finding the largest path length and then assigning the jobs\)}@}. <!--SR:!2026-02-23,356,358!2026-01-04,314,359!2026-02-25,358,358!2026-01-07,317,359!2025-12-10,294,351!2026-03-29,387,371!2026-03-02,362,371!2026-01-11,321,358!2026-02-12,330,359-->

## see also

- [tsort](tsort.md), ::@:: a Unix program for topological sorting <!--SR:!2025-12-07,292,330!2025-11-14,275,330-->
- [feedback arc set](feedback%20arc%20set.md), ::@:: a set of edges whose removal allows the remaining subgraph to be topologically sorted <!--SR:!2027-09-28,792,330!2025-12-02,288,330-->
- [Tarjan's strongly connected components algorithm](Tarjan's%20strongly%20connected%20components%20algorithm.md), ::@:: an algorithm that gives the topologically sorted list of strongly connected components in a graph <!--SR:!2027-10-15,746,290!2026-10-17,508,310-->
- [pre-topological order](pre-topological%20order.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/topological_sorting) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. Jarnagin, M. P. \(1960\), _Automatic machine methods of testing PERT networks for consistency_, Technical Memorandum No. K-24/60, Dahlgren, Virginia: U. S. Naval Weapons Laboratory <a id="^ref-1"></a>^ref-1
2. Kahn, Arthur B. \(1962\), "Topological sorting of large networks", _Communications of the ACM_, __5__ \(11\): 558–562, [doi](digital%20object%20identifier.md):[10.1145/368996.369025](https://doi.org/10.1145%2F368996.369025), [S2CID](Semantic%20Scholar.md#S2CID) [16728233](https://api.semanticscholar.org/CorpusID:16728233) <a id="^ref-2"></a>^ref-2
3. [Cormen, Thomas H.](Thomas%20H.%20Cormen.md); [Leiserson, Charles E.](Charles%20E.%20Leiserson.md); [Rivest, Ronald L.](Ron%20Rivest.md); [Stein, Clifford](Clifford%20Stein.md) \(2001\), "Section 22.4: Topological sort", [_Introduction to Algorithms_](Introduction%20to%20Algorithms.md) \(2nd ed.\), MIT Press and McGraw-Hill, pp. 549–552, [ISBN](ISBN.md) [0-262-03293-7](https://en.wikipedia.org/wiki/Special:BookSources/0-262-03293-7) <a id="^ref-3"></a>^ref-3
4. [Tarjan, Robert E.](Robert%20Tarjan.md) \(1976\), "Edge-disjoint spanning trees and depth-first search", _Acta Informatica_, __6__ \(2\): 171–185, [doi](digital%20object%20identifier.md):[10.1007/BF00268499](https://doi.org/10.1007%2FBF00268499), [S2CID](Semantic%20Scholar.md#S2CID) [12044793](https://api.semanticscholar.org/CorpusID:12044793) <a id="^ref-4"></a>^ref-4
5. [Cook, Stephen A.](Stephen%20Cook.md) \(1985\), "A Taxonomy of Problems with Fast Parallel Algorithms", _Information and Control_, __64__ \(1–3\): 2–22, [doi](digital%20object%20identifier.md):[10.1016/S0019-9958\(85\)80041-3](https://doi.org/10.1016%2FS0019-9958%2885%2980041-3) <a id="^ref-5"></a>^ref-5
6. Dekel, Eliezer; Nassimi, David; Sahni, Sartaj \(1981\), "Parallel matrix and graph algorithms", _SIAM Journal on Computing_, __10__ \(4\): 657–675, [doi](digital%20object%20identifier.md):[10.1137/0210049](https://doi.org/10.1137%2F0210049), [MR](Mathematical%20Reviews.md) [0635424](https://mathscinet.ams.org/mathscinet-getitem?mr=0635424) <a id="^ref-6"></a>^ref-6
7. Sanders, Peter; Mehlhorn, Kurt; Dietzfelbinger, Martin; Dementiev, Roman \(2019\), [_Sequential and Parallel Algorithms and Data Structures: The Basic Toolbox_](https://www.springer.com/gp/book/9783030252083), Springer International Publishing, [ISBN](ISBN.md) [978-3-030-25208-3](https://en.wikipedia.org/wiki/Special:BookSources/978-3-030-25208-3) <a id="^ref-7"></a>^ref-7
8. Vernet, Oswaldo; Markenzon, Lilian \(1997\), ["Hamiltonian problems for reducible flowgraphs"](http://pantheon.ufrj.br/bitstream/11422/2585/4/02_97_000575787.pdf) \(PDF\), _Proceedings: 17th International Conference of the Chilean Computer Science Society_, pp. 264–267, [doi](digital%20object%20identifier.md):[10.1109/SCCC.1997.637099](https://doi.org/10.1109%2FSCCC.1997.637099), [hdl](Handle%20System.md):[11422/2585](https://hdl.handle.net/11422%2F2585), [ISBN](ISBN.md) [0-8186-8052-0](https://en.wikipedia.org/wiki/Special:BookSources/0-8186-8052-0), [S2CID](Semantic%20Scholar.md#S2CID) [206554481](https://api.semanticscholar.org/CorpusID:206554481) <a id="^ref-8"></a>^ref-8

## further reading

- [D. E. Knuth](Donald%20Knuth.md), [The Art of Computer Programming](The%20Art%20of%20Computer%20Programming.md), Volume 1, section 2.2.3, which gives an algorithm for topological sorting of a partial ordering, and a brief history.
- [Bertrand Meyer](Bertrand%20Meyer.md), _Touch of Class: Learning to Program Well with Objects and Contracts_, [Springer](Springer%20Science+Business%20Media.md), 2099, chapter 15, _Devising and engineering an algorithm: topological sort_, using a modern programming language, for a detailed pedagogical presentation of topological sort \(using a variant of Kahn's algorithm\) with consideration of data structure design, API design, and software engineering concerns.

## external links

- [NIST Dictionary of Algorithms and Data Structures: topological sort](https://xlinux.nist.gov/dads/HTML/topologicalSort.html)
- [Weisstein, Eric W.](Eric%20W.%20Weisstein.md), ["Topological Sort"](https://mathworld.wolfram.com/TopologicalSort.html), _[MathWorld](MathWorld.md)_
