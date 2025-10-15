---
aliases:
  - bond
  - bond (graph theory)
  - bonds
  - bonds (graph theory)
  - cut
  - cut (graph theory)
  - cut space
  - cut spaces
  - cut-set
  - cut-sets
  - cuts
  - cuts (graph theory)
  - s-t cut
  - s-t cuts
  - sparse cut problem
  - sparse cut problems
  - s–t cut
  - s–t cuts
tags:
  - flashcard/active/general/eng/cut__graph_theory_
  - language/in/English
---

# cut

In {@{[graph theory](graph%20theory.md)}@}, a __cut__ is {@{a [partition](partition%20of%20a%20set.md) of the [vertices](vertex%20(graph%20theory).md) of a [graph](graph%20(discrete%20mathematics).md) into two [disjoint subsets](disjoint%20sets.md)}@}.<sup>[\[1\]](#^ref-1)</sup> {@{Any cut}@} determines {@{a __cut-set__, the set of edges that have one endpoint in each subset of the partition}@}. {@{These edges}@} are {@{said to __cross__ the cut}@}. In {@{a [connected graph](connectivity%20(graph%20theory).md#connected%20vertices%20and%20graphs)}@}, {@{each cut-set}@} determines {@{a unique cut, and in some cases cuts are identified with their cut-sets rather than with their vertex partitions}@}. <!--SR:!2025-11-25,303,330!2025-11-17,296,330!2029-04-27,1274,350!2025-11-16,295,330!2025-12-05,310,330!2025-12-06,311,330!2025-12-06,311,330!2025-12-01,306,330!2025-11-20,299,330-->

In {@{a [flow network](flow%20network.md)}@}, {@{an __s–t cut__}@} is {@{a cut that requires the [_source_](glossary%20of%20graph%20theory.md#direction) and the [_sink_](glossary%20of%20graph%20theory.md#direction) to be in different subsets}@}, and its _cut-set_ only consists of {@{edges going from the source's side to the sink's side}@}. {@{The _capacity_ of an s–t cut}@} is defined as {@{the sum of the capacity of each edge in the _cut-set_}@}. <!--SR:!2025-12-09,314,330!2025-12-07,312,330!2027-03-30,674,330!2027-10-27,832,330!2025-12-02,307,330!2025-12-08,313,330-->

## definition

{@{A __cut__ _C_ = (_S_, _T_)}@} is {@{a partition of _V_ of a graph _G_ = (_V_, _E_) into two subsets _S_ and _T_}@}. {@{The __cut-set__ of a cut _C_ = (_S_, _T_)}@} is {@{the set {(_u_, _v_) ∈ _E_ | _u_ ∈ _S_, _v_ ∈ _T_} of edges that have one endpoint in _S_ and the other endpoint in _T_}@}. If {@{_s_ and _t_ are specified vertices of the graph _G_}@}, then {@{an ___s_–_t_ cut__}@} is {@{a cut in which _s_ belongs to the set _S_ and _t_ belongs to the set _T_}@}. <!--SR:!2025-12-11,316,330!2026-11-16,543,310!2027-11-17,849,330!2025-12-03,308,330!2025-11-25,303,330!2026-12-05,562,310!2026-12-24,573,310-->

In {@{an unweighted undirected graph}@}, {@{the _size_ or _weight_ of a cut}@} is {@{the number of edges crossing the cut}@}. In {@{a [weighted graph](graph%20(discrete%20mathematics).md#weighted%20graph)}@}, {@{the __value__ or __weight__}@} is {@{defined by the sum of the weights of the edges crossing the cut}@}. <!--SR:!2025-11-25,303,330!2025-12-03,308,330!2025-11-30,307,330!2028-04-23,958,330!2025-12-11,316,330!2028-04-04,941,330-->

{@{A __bond__}@} is {@{a cut-set that does not have any other cut-set as a proper subset}@}. <!--SR:!2025-12-02,307,330!2025-12-04,309,330-->

## minimum cut

- see: [minimum cut](minimum%20cut.md)

> {@{![a minimum cut](../../archives/Wikimedia%20Commons/Min-cut.svg)}@}
>
> {@{A minimum cut.}@} <!--SR:!2025-12-09,314,330!2025-12-11,316,330-->

{@{A cut is _minimum_}@} if {@{the size or weight of the cut is not larger than the size of any other cut}@}. The illustration on the right shows {@{a minimum cut: the size of this cut is 2}@}, and {@{there is no cut of size 1 because the graph is [bridgeless](bridge%20(graph%20theory).md)}@}. <!--SR:!2025-11-25,303,330!2025-12-05,310,330!2028-04-14,950,330!2027-03-24,669,330-->

{@{The [max-flow min-cut theorem](max-flow%20min-cut%20theorem.md)}@} proves that {@{the maximum [network flow](flow%20network.md) and the sum of the cut-edge weights of any minimum cut that separates the source and the sink are equal}@}. There are {@{[polynomial-time](time%20complexity.md#polynomial%20time) methods to solve the min-cut problem}@}, notably {@{the [Edmonds–Karp algorithm](Edmonds–Karp%20algorithm.md)}@}.<sup>[\[2\]](#^ref-2)</sup> <!--SR:!2025-11-09,289,330!2026-12-08,563,310!2025-11-30,307,330!2026-11-13,540,310-->

## maximum cut

- see: [maximum cut](maximum%20cut.md)

> {@{![a maximum cut](../../archives/Wikimedia%20Commons/Max-cut.svg)}@}
>
> {@{A maximum cut.}@} <!--SR:!2026-03-08,370,310!2025-12-10,315,330-->

{@{A cut is _maximum_}@} if {@{the size of the cut is not smaller than the size of any other cut}@}. The illustration on the right shows {@{a maximum cut: the size of the cut is equal to 5}@}, and {@{there is no cut of size 6, or |_E_| (the number of edges), because the graph is not [bipartite](bipartite%20graph.md) (there is an [odd cycle](cycle%20graph.md#terminology))}@}. <!--SR:!2025-12-11,316,330!2025-12-06,312,330!2027-12-17,858,330!2025-12-11,316,330-->

In general, {@{finding a maximum cut}@} is {@{computationally hard}@}.<sup>[\[3\]](#^ref-3)</sup> {@{The max-cut problem}@} is {@{one of [Karp's 21 NP-complete problems](Karp's%2021%20NP-complete%20problems.md)}@}.<sup>[\[4\]](#^ref-4)</sup> The max-cut problem is {@{also [APX-hard](APX.md), meaning that there is no polynomial-time approximation scheme for it unless [P = NP](P%20versus%20NP%20problem.md)}@}.<sup>[\[5\]](#^ref-5)</sup> However, it can be {@{approximated to within a constant [approximation ratio](approximation%20algorithm.md) using [semidefinite programming](semidefinite%20programming.md)}@}.<sup>[\[6\]](#^ref-6)</sup> <!--SR:!2025-12-11,316,330!2029-04-15,1265,350!2025-12-04,309,330!2028-02-15,905,330!2027-08-04,695,310!2028-05-03,965,330-->

Note that {@{min-cut and max-cut}@} are {@{_not_ [dual](linear%20programming.md#duality) problems in the [linear programming](linear%20programming.md) sense}@}, even though {@{one gets from one problem to other by changing min to max in the [objective function](loss%20function.md)}@}. {@{The max-flow problem}@} is {@{the dual of the min-cut problem}@}.<sup>[\[7\]](#^ref-7)</sup> <!--SR:!2025-11-01,281,330!2025-12-06,312,330!2025-11-10,290,330!2028-03-25,935,330!2028-04-24,958,330-->

## sparsest cut

{@{The __sparsest cut problem__}@} is to {@{bipartition the vertices}@} so as to {@{minimize the ratio of the number of edges across the cut divided by the number of vertices in the smaller half of the partition}@}. {@{This objective function}@} favors {@{solutions that are both sparse (few edges crossing the cut) and balanced (close to a bisection)}@}. The problem is {@{known to be NP-hard}@}, and {@{the best known approximation algorithm}@} is {@{an $O({\sqrt {\log n} })$ approximation due to [Arora, Rao & Vazirani (2009)](#^ref-8)}@}.<sup>[\[8\]](#^ref-8)</sup> <!--SR:!2027-04-16,686,330!2025-12-31,112,290!2025-12-07,312,330!2026-11-23,550,310!2025-11-30,307,330!2029-04-12,1263,350!2026-02-25,295,250!2026-01-17,101,384-->

## cut space

{@{The family of all cut sets of an undirected graph}@} is known as {@{the __cut space__ of the graph}@}. It forms {@{a [vector space](vector%20space.md) over the two-element [finite field](finite%20field.md) of arithmetic [modulo](modular%20arithmetic.md) two}@}, with {@{the [symmetric difference](symmetric%20difference.md) of two cut sets as the vector addition operation}@}, and is {@{the [orthogonal complement](orthogonal%20complement.md) of the [cycle space](cycle%20space.md)}@}.<sup>[\[9\]](#^ref-9)</sup><sup>[\[10\]](#^ref-10)</sup> If {@{the edges of the graph are given positive weights}@}, {@{the minimum weight [basis](basis%20(linear%20algebra).md) of the cut space}@} can be {@{described by a [tree](tree%20(graph%20theory).md) on the same vertex set as the graph, called the [Gomory–Hu tree](Gomory–Hu%20tree.md)}@}.<sup>[\[11\]](#^ref-11)</sup> {@{Each edge of this tree}@} is {@{associated with a bond in the original graph (a bond may be associated with multiple edges)}@}, and {@{the minimum cut between two nodes _s_ and _t_ (the cut separates _s_ and _t_)}@} is {@{the minimum weight bond among the ones associated with the path from _s_ to _t_ in the tree}@}. <!--SR:!2025-12-10,315,330!2027-01-18,596,310!2026-11-17,544,310!2027-10-18,824,330!2027-04-08,678,330!2026-11-10,537,310!2028-09-06,1044,310!2026-07-22,465,310!2027-11-01,836,330!2027-04-12,682,330!2026-12-22,571,310!2027-11-10,782,290-->

## see also

- [connectivity (graph theory)](connectivity%20(graph%20theory).md)
- [graph cuts in computer vision](graph%20cuts%20in%20computer%20vision.md)
- [split (graph theory)](split%20(graph%20theory).md)
- [vertex separator](vertex%20separator.md)
- [bridge (graph theory)](bridge%20(graph%20theory).md)
- [cutwidth](cutwidth.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/cut_(graph_theory)) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. ["NetworkX 2.6.2 documentation"](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.cuts.cut_size.html#networkx.algorithms.cuts.cut_size). _networkx.algorithms.cuts.cut_size_. [Archived](https://web.archive.org/web/20211118095812/https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.cuts.cut_size.html#networkx.algorithms.cuts.cut_size) from the original on 2021-11-18. Retrieved 2021-12-10. A cut is a partition of the nodes of a graph into two sets. The cut size is the sum of the weights of the edges "between" the two sets of nodes. <a id="^ref-1"></a>^ref-1
2. [Cormen, Thomas H.](Thomas%20H.%20Cormen.md); [Leiserson, Charles E.](Charles%20E.%20Leiserson.md); [Rivest, Ronald L.](Ron%20Rivest.md); [Stein, Clifford](Clifford%20Stein.md) (2001), _[Introduction to Algorithms](Introduction%20to%20Algorithms.md)_ (2nd ed.), MIT Press and McGraw-Hill, p. 563,655,1043, [ISBN](ISBN.md) [0-262-03293-7](https://en.wikipedia.org/wiki/Special:BookSources/0-262-03293-7). <a id="^ref-2"></a>^ref-2
3. [Garey, Michael R.](Michael%20Garey.md); [Johnson, David S.](David%20S.%20Johnson.md) (1979), _[Computers and Intractability: A Guide to the Theory of NP-Completeness](Computers%20and%20Intractability.md)_, W.H. Freeman, [A2.2: ND16, p. 210](https://archive.org/details/computersintract0000gare/page/), [ISBN](ISBN.md) [0-7167-1045-5](https://en.wikipedia.org/wiki/Special:BookSources/0-7167-1045-5). <a id="^ref-3"></a>^ref-3
4. [Karp, R. M.](Richard%20M.%20Karp.md) (1972), "Reducibility among combinatorial problems", in Miller, R. E.; Thacher, J. W. (eds.), _Complexity of Computer Computation_, New York: Plenum Press, pp. 85–103. <a id="^ref-4"></a>^ref-4
5. [Khot, S.](Subhash%20Khot.md); Kindler, G.; Mossel, E.; O’Donnell, R. (2004), ["Optimal inapproximability results for MAX-CUT and other two-variable CSPs?"](https://www.cs.cmu.edu/~odonnell/papers/maxcut.pdf) (PDF), _Proceedings of the 45th IEEE Symposium on Foundations of Computer Science_, pp. 146–154, [archived](https://web.archive.org/web/20190715031206/http://www.cs.cmu.edu/~odonnell/papers/maxcut.pdf) (PDF) from the original on 2019-07-15, retrieved 2019-08-29. <a id="^ref-5"></a>^ref-5
6. [Goemans, M. X.](Michel%20Goemans.md); [Williamson, D. P.](David%20P.%20Williamson.md) (1995), "Improved approximation algorithms for maximum cut and satisfiability problems using semidefinite programming", _[Journal of the ACM](Journal%20of%20the%20ACM.md)_, __42__ (6): 1115–1145, [doi](digital%20object%20identifier.md):[10.1145/227683.227684](https://doi.org/10.1145%2F227683.227684). <a id="^ref-6"></a>^ref-6
7. [Vazirani, Vijay V.](Vijay%20Vazirani.md) (2004), _Approximation Algorithms_, Springer, pp. 97–98, [ISBN](ISBN.md) [3-540-65367-8](https://en.wikipedia.org/wiki/Special:BookSources/3-540-65367-8). <a id="^ref-7"></a>^ref-7
8. [Arora, Sanjeev](Sanjeev%20Arora.md); Rao, Satish; [Vazirani, Umesh](Umesh%20Vazirani.md) (2009), "Expander flows, geometric embeddings and graph partitioning", _J. ACM_, __56__ (2), ACM: 1–37, [doi](digital%20object%20identifier.md):[10.1145/1502793.1502794](https://doi.org/10.1145%2F1502793.1502794), [S2CID](Semantic%20Scholar.md#S2CID) [263871111](https://api.semanticscholar.org/CorpusID:263871111). <a id="^ref-8"></a>^ref-8
9. Gross, Jonathan L.; Yellen, Jay (2005), "4.6 Graphs and Vector Spaces", [_Graph Theory and Its Applications_](https://books.google.com/books?id=-7Q_POGh-2cC&pg=PA197) (2nd ed.), CRC Press, pp. 197–207, [ISBN](ISBN.md) [9781584885054](https://en.wikipedia.org/wiki/Special:BookSources/9781584885054). <a id="^ref-9"></a>^ref-9
10. Diestel, Reinhard (2012), "1.9 Some linear algebra", [_Graph Theory_](https://books.google.com/books?id=eZi8AAAAQBAJ&pg=PA23), Graduate Texts in Mathematics, vol. 173, Springer, pp. 23–28. <a id="^ref-10"></a>^ref-10
11. [Korte, B. H.](Bernhard%20Korte.md); Vygen, Jens (2008), "8.6 Gomory–Hu Trees", _Combinatorial Optimization: Theory and Algorithms_, Algorithms and Combinatorics, vol. 21, Springer, pp. 180–186, [ISBN](ISBN.md) [978-3-540-71844-4](https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-71844-4). <a id="^ref-11"></a>^ref-11
