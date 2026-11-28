- For the theorem about infinite graphs, see [Kőnig's lemma](Kőnig's%20lemma.md). For other uses, see [König's theorem \(disambiguation\)](König's%20theorem%20(disambiguation).md).

> ![Graph illustrating König's theorem](../../archives/Wikimedia%20Commons/Koenigs-theorem-graph.svg)
>
> An example of a bipartite graph, with a maximum matching \(blue\) and minimum vertex cover \(red\) both of size six.

In the [mathematical](mathematics.md) area of [graph theory](graph%20theory.md), __Kőnig's theorem__, proved by [Dénes Kőnig](Dénes%20Kőnig.md) \([1931](#CITEREFKőnig1931)\), describes an equivalence between the [maximum matching](maximum%20matching.md) problem and the minimum [vertex cover problem](vertex%20cover%20problem.md) in [bipartite graphs](bipartite%20graph.md). It was discovered independently, also in 1931, by [Jenő Egerváry](Jenő%20Egerváry.md) in the more general case of [weighted graphs](weighted%20graph.md#weighted%20graph).

## setting

A [vertex cover](vertex%20cover.md) in a graph is a set of vertices that includes at least one endpoint of every edge, and a vertex cover is _minimum_ if no other vertex cover has fewer vertices.<sup>[\[1\]](#^ref-1)</sup> A [matching](matching%20(graph%20theory).md) in a graph is a set of edges no two of which share an endpoint, and a matching is _maximum_ if no other matching has more edges.<sup>[\[2\]](#^ref-2)</sup>

It is obvious from the definition that any vertex-cover set must be at least as large as any matching set \(since for every edge in the matching, at least one vertex is needed in the cover\). In particular, the [minimum vertex cover](minimum%20vertex%20cover.md) set is at least as large as the [maximum matching](maximum%20matching.md) set. Kőnig's theorem states that, in any [bipartite graph](bipartite%20graph.md), the minimum vertex cover set and the maximum matching set have in fact the same size.<sup>[\[3\]](#^ref-3)</sup>

## statement of the theorem

_In any [bipartite graph](bipartite%20graph.md), the number of edges in a [maximum matching](maximum%20matching.md) equals the number of vertices in a [minimum vertex cover](minimum%20vertex%20cover.md).<sup>[\[3\]](#^ref-3)</sup>_

### example

The bipartite graph shown in the above illustration has 14 vertices; a matching with six edges is shown in blue, and a vertex cover with six vertices is shown in red. There can be no smaller vertex cover, because any vertex cover has to include at least one endpoint of each matched edge \(as well as of every other edge\), so this is a minimum vertex cover. Similarly, there can be no larger matching, because any matched edge has to include at least one endpoint in the vertex cover, so this is a maximum matching. Kőnig's theorem states that the equality between the sizes of the matching and the cover \(in this example, both numbers are six\) applies more generally to any bipartite graph.

## proofs

### constructive proof

> ![Illustration to how maximum flow/minimum cut looks in bipartite graphs](../../archives/Wikimedia%20Commons/Minimum%20cut%20in%20a%20bipartite%20graph.svg)
>
> Minimum cut $(S, T)$ in the flow network $G'_\infty$

The following proof provides a way of constructing a minimum vertex cover from a maximum matching. Let $G=(V,E)$ be a bipartite graph and let $A,B$ be the two parts of the vertex set $V$. Suppose that $M$ is a maximum matching for $G$.

Construct the [flow network](flow%20network.md) $G'_\infty$ derived from $G$ in such way that there are edges of capacity $1$ from the source $s$ to every vertex $a \in A$ and from every vertex $b \in B$ to the sink $t$, and of capacity $+\infty$ from $a$ to $b$ for any $(a, b) \in E$.

The size $|M|$ of the maximum matching in $G$ is the size of a [maximum flow](maximum%20flow%20problem.md) in $G'_\infty$, which, in turn, is the size of a [minimum cut](minimum%20cut.md) in the network $G'_\infty$, as follows from the [max-flow min-cut theorem](max-flow%20min-cut%20theorem.md).

Let $(S, T)$ be a minimum cut. Let $A = A_S \cup A_T$ and $B = B_S \cup B_T$, such that $A_S, B_S \subset S$ and $A_T, B_T \subset T$. Then the minimum cut is composed only of edges going from $s$ to $A_T$ or from $B_S$ to $t$, as any edge from $A_S$ to $B_T$ would make the size of the cut infinite.

Therefore, the size of the minimum cut is equal to $|A_T|+|B_S|$. On the other hand, $A_T \cup B_S$ is a vertex cover, as any edge that is not incident to vertices from $A_T$ and $B_S$ must be incident to a pair of vertices from $A_S$ and $B_T$, which would contradict the fact that there are no edges between $A_S$ and $B_T$.

Thus, $A_T \cup B_S$ is a minimum vertex cover of $G$.<sup>[\[4\]](#^ref-4)</sup>

### constructive proof without flow concepts

No vertex in a vertex cover can cover more than one edge of $M$ \(because the edge half-overlap would prevent $M$ from being a matching in the first place\), so if a vertex cover with $|M|$ vertices can be constructed, it must be a minimum cover.<sup>[\[5\]](#^ref-5)</sup>

To construct such a cover, let $U$ be the set of unmatched vertices in $A$ \(possibly empty\), and let $Z$ be the set of vertices that are either in $U$ or are connected to $U$ by alternating paths \(paths that alternate between edges that are in the matching and edges that are not in the matching\). Let

$$K=(A\setminus Z)\cup (B\cap Z).$$

Every edge $e$ in $E$ either belongs to an alternating path \(and has a right endpoint in $K$\), or it has a left endpoint in $K$. For, if $e$ is matched but not in an alternating path, then its left endpoint cannot be in an alternating path \(because two matched edges can not share a vertex\) and thus belongs to $A\setminus Z$. Alternatively, if $e$ is unmatched but not in an alternating path, then its left endpoint cannot be in an alternating path, for such a path could be extended by adding $e$ to it. Thus, $K$ forms a vertex cover.<sup>[\[6\]](#^ref-6)</sup>

Additionally, every vertex in $K$ is an endpoint of a matched edge. For, every vertex in $A\setminus Z$ is matched because $Z$ is a superset of $U$, the set of unmatched left vertices. And every vertex in $B\cap Z$ must also be matched, for if there existed an alternating path to an unmatched vertex then changing the matching by removing the matched edges from this path and adding the unmatched edges in their place would increase the size of the matching. However, no matched edge can have both of its endpoints in $K$. Thus, $K$ is a vertex cover of [cardinality](cardinality.md) equal to $M$, and must be a minimum vertex cover.<sup>[\[6\]](#^ref-6)</sup>

### proof using linear programming duality

To explain this proof, we first have to extend the notion of a matching to that of a [fractional matching](fractional%20matching.md) - an assignment of a weight in \[0,1\] to each edge, such that the sum of weights near each vertex is at most 1 \(an integral matching is a special case of a fractional matching in which the weights are in {0,1}\). Similarly we define a fractional vertex-cover - an assignment of a non-negative weight to each vertex, such that the sum of weights in each edge is at least 1 \(an integral vertex-cover is a special case of a fractional vertex-cover in which the weights are in {0,1}\).

The maximum fractional matching size in a graph $G=(V,E)$ is the solution of the following [linear program](linear%20program.md):

Maximize __1__<sub>_E_</sub> _·_ __x__

Subject to: __x__ ≥ __0__<!-- markdown separator -->_<sub>E</sub>_

\_\_\_\_\_\_\_\_\_\_ __A__<sub>_G_</sub> · __x__ _≤ __1__<sub>V</sub>._

where __x__ is a vector of size \|_E_\| in which each element represents the weight of an edge in the fractional matching. __1__<sub>E</sub> is a vector of \|_E_\| ones, so the first line indicates the size of the matching. __0__<!-- markdown separator -->_<sub>E</sub>_ is a vector of \|_E_\| zeros, so the second line indicates the constraint that the weights are non-negative. __1__<sub>V</sub> is a vector of \|_V_\| ones and __A__<sub>_G_</sub> is the [incidence matrix](incidence%20matrix.md) of _G,_ so the third line indicates the constraint that the sum of weights near each vertex is at most 1. Similarly, the minimum fractional vertex-cover size in $G=(V,E)$ is the solution of the following LP:

Minimize __1__<sub>_V_</sub> _·_ __y__

Subject to: __y__ ≥ __0__<!-- markdown separator -->_<sub>V</sub>_

\_\_\_\_\_\_\_\_\_\_ __A__<sub>_G_</sub><sup>T</sup> · __y__ ≥ ___1__<sub>E</sub>._

where __y__ is a vector of size \|V\| in which each element represents the weight of a vertex in the fractional cover. Here, the first line is the size of the cover, the second line represents the non-negativity of the weights, and the third line represents the requirement that the sum of weights near each edge must be at least 1. Now, the minimum fractional cover LP is exactly the [dual linear program](dual%20linear%20program.md) of the maximum fractional matching LP. Therefore, by the LP duality theorem, both programs have the same solution. This fact is true not only in bipartite graphs but in arbitrary graphs:

_In any graph, the largest size of a fractional matching equals the smallest size of a fractional vertex cover._

What makes bipartite graphs special is that, in bipartite graphs, both these linear programs have optimal solutions in which all variable values are integers. This follows from the fact that in the [fractional matching polytope](matching%20polytope.md) of a bipartite graph, all extreme points have only [integer](integer.md) coordinates, and the same is true for the fractional vertex-cover polytope. Therefore, the above theorem implies:<sup>[\[7\]](#^ref-7)</sup>

_In any bipartite graph, the largest size of a matching equals the smallest size of a vertex cover._

## algorithm

The [constructive proof](constructive%20proof.md) described above provides an algorithm for producing a minimum vertex cover given a maximum matching. Thus, the [Hopcroft–Karp algorithm](Hopcroft–Karp%20algorithm.md) for finding maximum matchings in bipartite graphs may also be used to solve the vertex cover problem efficiently in these graphs.<sup>[\[8\]](#^ref-8)</sup>

Despite the equivalence of the two problems from the point of view of exact solutions, they are not equivalent for [approximation algorithms](approximation%20algorithm.md). Bipartite maximum matchings can be approximated arbitrarily accurately in constant time by [distributed algorithms](distributed%20algorithm.md); in contrast, approximating the minimum vertex cover of a bipartite graph requires at least logarithmic time.<sup>[\[9\]](#^ref-9)</sup>

<!-- markdownlint-disable-next-line MD024 -->
### example

In the graph shown in the introduction take $L$ to be the set of vertices in the bottom layer of the diagram and $R$ to be the set of vertices in the top layer of the diagram. From left to right label the vertices in the bottom layer with the numbers 1, ..., 7 and label the vertices in the top layer with the numbers 8, ..., 14. The set $U$ of unmatched vertices from $L$ is {1}. The alternating paths starting from $U$ are 1–10–3–13–7, 1–10–3–11–5–13–7, 1–11–5–13–7, 1–11–5–10–3–13–7, and all subpaths of these starting from 1. The set $Z$ is therefore {1,3,5,7,10,11,13}, resulting in $L\setminus Z=\{2,4,6\}$, $R\cap Z=\{10,11,13\}$ and the minimum vertex cover $K=\{2,4,6,10,11,13\}$.

## non-bipartite graphs

For graphs that are not bipartite, the minimum vertex cover may be larger than the maximum matching. Moreover, the two problems are very different in complexity: maximum matchings can be found in [polynomial time](polynomial%20time.md#polynomial%20time) for any graph, while minimum vertex cover is [NP-complete](NP-complete.md).

The complement of a vertex cover in any graph is an [independent set](independent%20set%20(graph%20theory).md), so a minimum vertex cover is complementary to a maximum independent set; finding maximum independent sets is another NP-complete problem. The equivalence between matching and covering articulated in Kőnig's theorem allows minimum vertex covers and maximum independent sets to be computed in polynomial time for bipartite graphs, despite the NP-completeness of these problems for more general graph families.<sup>[\[10\]](#^ref-10)</sup>

## history

Kőnig's theorem is named after the Hungarian mathematician [Dénes Kőnig](Dénes%20Kőnig.md). Kőnig had announced in 1914 and published in 1916 the results that every [regular](regular%20graph.md) bipartite graph has a [perfect matching](perfect%20matching.md),<sup>[\[11\]](#^ref-11)</sup> and more generally that the [chromatic index](chromatic%20index.md#definitions) of any bipartite graph \(that is, the minimum number of matchings into which it can be partitioned\) equals its [maximum degree](degree%20(graph%20theory).md)<sup>[\[12\]](#^ref-12)</sup> – the latter statement is known as __Kőnig's line coloring theorem__.<sup>[\[13\]](#^ref-13)</sup> However, [Bondy & Murty \(1976\)](#CITEREFBondyMurty1976) attribute Kőnig's theorem itself to a later paper of Kőnig \(1931\).

According to [Biggs, Lloyd & Wilson \(1976\)](#CITEREFBiggsLloydWilson1976), Kőnig attributed the idea of studying matchings in bipartite graphs to his father, mathematician [Gyula Kőnig](Gyula%20Kőnig.md). In Hungarian, Kőnig's name has a [double acute accent](double%20acute%20accent.md), but his theorem is sometimes spelled \(incorrectly\) in German characters, with an [umlaut](umlaut%20(diacritic).md).

## related theorems

Kőnig's theorem is equivalent to many other min-max theorems in graph theory and [combinatorics](combinatorics.md), such as [Hall's marriage theorem](Hall's%20marriage%20theorem.md) and [Dilworth's theorem](Dilworth's%20theorem.md). Since bipartite matching is a special case of [maximum flow](maximum%20flow%20problem.md), the theorem also results from the [max-flow min-cut theorem](max-flow%20min-cut%20theorem.md).<sup>[\[14\]](#^ref-14)</sup>

## connections with perfect graphs

A graph is said to be [perfect](perfect%20graph.md) if, in every [induced subgraph](induced%20subgraph.md), the [chromatic number](chromatic%20number.md#chromatic%20number) equals the size of the largest [clique](clique%20(graph%20theory).md). Any bipartite graph is perfect,<sup>[\[15\]](#^ref-15)</sup> because each of its subgraphs is either bipartite or independent; in a bipartite graph that is not independent the chromatic number and the size of the largest clique are both two while in an independent set the chromatic number and clique number are both one.

A graph is perfect if and only if its complement is perfect,<sup>[\[16\]](#^ref-16)</sup> and Kőnig's theorem can be seen as equivalent to the statement that the complement of a bipartite graph is perfect. For, each color class in a coloring of the complement of a bipartite graph is of size at most 2 and the classes of size 2 form a matching, a clique in the complement of a graph _G_ is an independent set in _G_, and as we have already described an independent set in a bipartite graph _G_ is a complement of a vertex cover in _G_. Thus, any matching _M_ in a bipartite graph _G_ with _n_ vertices corresponds to a coloring of the complement of _G_ with _n_&hairsp;−\|_M_\| colors, which by the perfection of complements of bipartite graphs corresponds to an independent set in _G_ with _n_&hairsp;−\|_M_\| vertices, which corresponds to a vertex cover of _G_ with _M_ vertices. Conversely, Kőnig's theorem proves the perfection of the complements of bipartite graphs, a result proven in a more explicit form by [Gallai \(1958\)](#CITEREFGallai1958).

One can also connect Kőnig's line coloring theorem to a different class of perfect graphs, the [line graphs](line%20graph.md) of bipartite graphs. If _G_ is a graph, the line graph _L_\(_G_\) has a vertex for each edge of _G_, and an edge for each pair of adjacent edges in _G_. Thus, the chromatic number of _L_\(_G_\) equals the chromatic index of _G_. If _G_ is bipartite, the cliques in _L_\(_G_\) are exactly the sets of edges in _G_ sharing a common endpoint. Now Kőnig's line coloring theorem, stating that the chromatic index equals the maximum vertex degree in any bipartite graph, can be interpreted as stating that the line graph of a bipartite graph is perfect.<sup>[\[17\]](#^ref-17)</sup>

Since line graphs of bipartite graphs are perfect, the complements of line graphs of bipartite graphs are also perfect. A clique in the complement of the line graph of _G_ is just a matching in _G_. And a coloring in the complement of the line graph of _G_, when _G_ is bipartite, is a partition of the edges of _G_ into subsets of edges sharing a common endpoint; the endpoints shared by each of these subsets form a vertex cover for _G_. Therefore, Kőnig's theorem itself can also be interpreted as stating that the complements of line graphs of bipartite graphs are perfect.<sup>[\[17\]](#^ref-17)</sup>

## weighted variants

Konig's theorem can be extended to [weighted graphs](weighted%20graph.md#weighted%20graph).

### [Egerváry](Jenő%20Egerváry.md)'s theorem for edge-weighted graphs

[Jenő Egerváry](Jenő%20Egerváry.md) \(1931\) considered graphs in which each edge _e_ has a non-negative integer weight _w<sub>e</sub>_. The weight vector is denoted by __w__. The __w-__<!-- markdown separator -->_weight of a matching_ is the sum of weights of the edges participating in the matching. A ___w-__<!-- markdown separator -->vertex-cover_ is a multiset of vertices \("multiset" means that each vertex may appear several times\), in which each edge _e_ is adjacent to at least _w<sub>e</sub>_ vertices. [Egerváry](Jenő%20Egerváry.md)'s theorem says:

_In any edge-weighted bipartite graph, the maximum __w-__<!-- markdown separator -->weight of a matching equals the smallest number of vertices in a __w-__<!-- markdown separator -->vertex-cover._

The maximum ___w-___<!-- markdown separator -->weight of a fractional matching is given by the LP:<sup>[\[18\]](#^ref-18)</sup>

Maximize ___w___ _·_ __x__

Subject to: __x__ ≥ __0__<!-- markdown separator -->_<sub>E</sub>_

\_\_\_\_\_\_\_\_\_\_ __A__<sub>_G_</sub> · __x__ _≤ __1__<sub>V</sub>._

And the minimum number of vertices in a fractional ___w-___<!-- markdown separator -->vertex-cover is given by the dual LP:

Minimize __1__<sub>_V_</sub> _·_ __y__

Subject to: __y__ ≥ __0__<!-- markdown separator -->_<sub>V</sub>_

\_\_\_\_\_\_\_\_\_\_ __A__<sub>_G_</sub><sup>T</sup> · __y__ ≥ ___w__._

As in the proof of Konig's theorem, the LP duality theorem implies that the optimal values are equal \(for any graph\), and the fact that the graph is bipartite implies that these programs have optimal solutions in which all values are integers.

### theorem for vertex-weighted graphs

One can consider a graph in which each vertex _v_ has a non-negative integer weight _b<sub>v</sub>_. The weight vector is denoted by __b__. The ___b__-weight_ of a vertex-cover is the sum of _b<sub>v</sub>_ for all _v_ in the cover. A ___b__-matching_ is an assignment of a non-negative integral weight to each edge, such that the sum of weights of edges adjacent to any vertex _v_ is at most _b<sub>v</sub>_. Egerváry's theorem can be extended, using a similar argument, to graphs that have both edge-weights __w__ and vertex-weights __b__:<sup>[\[18\]](#^ref-18)</sup>

_In any edge-weighted vertex-weighted bipartite graph, the maximum __w-__<!-- markdown separator -->weight of a __b__-matching equals the minimum __b__-weight of vertices in a __w-__<!-- markdown separator -->vertex-cover._

## see also

- [Kőnig's property in hypergraphs](matching%20in%20hypergraphs.md#Kőnig's%20property)

## notes

1. Called a _covering_ and a _minimum covering_ respectively by [Bondy & Murty \(1976\)](#CITEREFBondyMurty1976), p. 73. <a id="^ref-1"></a>^ref-1
2. [Bondy & Murty \(1976\)](#CITEREFBondyMurty1976), p. 70. <a id="^ref-2"></a>^ref-2
3. [Bondy & Murty \(1976\)](#CITEREFBondyMurty1976), Theorem 5.3, p. 74; [Cook et al. \(2011\)](#CITEREFCookCunninghamPulleyblankSchrijver2011). <a id="^ref-3"></a>^ref-3
4. [Cesa-Bianchi \(2020\)](#CITEREFCesa-Bianchi2020). <a id="^ref-4"></a>^ref-4
5. [Bondy & Murty \(1976\)](#CITEREFBondyMurty1976), Lemma 5.3, p. 74. <a id="^ref-5"></a>^ref-5
6. [Bondy & Murty \(1976\)](#CITEREFBondyMurty1976), pp. 74–75. <a id="^ref-6"></a>^ref-6
7. [Lovász & Plummer \(1986\)](#CITEREFLovászPlummer1986), p. 270. <a id="^ref-7"></a>^ref-7
8. For this algorithm, see [Storer \(2001\)](#CITEREFStorer2001), p 319, and for the connection to vertex cover see p. 342. <a id="^ref-8"></a>^ref-8
9. [Göös & Suomela \(2014\)](#CITEREFGöösSuomela2014). <a id="^ref-9"></a>^ref-9
10. [Storer \(2001\)](#CITEREFStorer2001), [Exercise 261, p. 342](https://books.google.com/books?id=S-tXjl1hsUYC&pg=PA342). <a id="^ref-10"></a>^ref-10
11. In a poster displayed at the 1998 [International Congress of Mathematicians](International%20Congress%20of%20Mathematicians.md) in Berlin and again at the Bled'07 International Conference on Graph Theory, Harald Gropp has pointed out that the same result already appears in the language of [configurations](projective%20configuration.md) in the 1894 thesis of [Ernst Steinitz](Ernst%20Steinitz.md). <a id="^ref-11"></a>^ref-11
12. [Biggs, Lloyd & Wilson \(1976\)](#CITEREFBiggsLloydWilson1976). <a id="^ref-12"></a>^ref-12
13. [Lovász & Plummer \(1986\)](#CITEREFLovászPlummer1986), Theorem 1.4.17, pp. 37ff.. <a id="^ref-13"></a>^ref-13
14. [Cook et al. \(2011\)](#CITEREFCookCunninghamPulleyblankSchrijver2011). <a id="^ref-14"></a>^ref-14
15. "Trivially", according to [Lovász \(1974\)](#CITEREFLovász1974). <a id="^ref-15"></a>^ref-15
16. This is the [perfect graph theorem](perfect%20graph%20theorem.md) of [Lovász \(1972\)](#CITEREFLovász1972) <a id="^ref-16"></a>^ref-16
17. [Lovász \(1974\)](#CITEREFLovász1974). <a id="^ref-17"></a>^ref-17
18. [Lovász & Plummer \(1986\)](#CITEREFLovászPlummer1986), p. 271. <a id="^ref-18"></a>^ref-18

## references

- <a id="CITEREFBiggsLloydWilson1976"></a> [Biggs, N. L.](Norman%20L.%20Biggs.md); Lloyd, E. K.; [Wilson, R. J.](Robin%20Wilson%20(mathematician).md) \(1976\), [_Graph Theory 1736–1936_](Graph%20Theory,%201736–1936.md), Oxford University Press, pp. 203–207, [ISBN](ISBN%20(identifier).md) [0-19-853916-9](https://en.wikipedia.org/wiki/Special:BookSources/0-19-853916-9).
- <a id="CITEREFCesa-Bianchi2020"></a> [Cesa-Bianchi, Nicolò](Nicolò%20Cesa-Bianchi.md) \(April 11, 2020\), [_Matchings and the max-flow min-cut theorem_](https://cesa-bianchi.di.unimi.it/GraphTheory/Notes/matchings.pdf) \(PDF\)
- <a id="CITEREFCookCunninghamPulleyblankSchrijver2011"></a> [Cook, William J.](William%20J.%20Cook.md); Cunningham, William H.; [Pulleyblank, William R.](William%20R.%20Pulleyblank.md); [Schrijver, Alexander](Alexander%20Schrijver.md) \(2011\), [_Combinatorial Optimization_](https://books.google.com/books?id=tarLTNwM3gEC&pg=PA48), Wiley Series in Discrete Mathematics and Optimization, vol. 33, John Wiley & Sons, pp. 48–49, [ISBN](ISBN%20(identifier).md) [9781118031391](https://en.wikipedia.org/wiki/Special:BookSources/9781118031391).
- <a id="CITEREFBondyMurty1976"></a> [Bondy, J. A.](J.%20A.%20Bondy.md); [Murty, U. S. R.](U.%20S.%20R.%20Murty.md) \(1976\), [_Graph Theory with Applications_](https://archive.org/details/graphtheorywitha0000bond), North Holland, [ISBN](ISBN%20(identifier).md) [0-444-19451-7](https://en.wikipedia.org/wiki/Special:BookSources/0-444-19451-7).
- <a id="CITEREFGallai1958"></a> [Gallai, Tibor](Tibor%20Gallai.md) \(1958\), "Maximum-minimum Sätze über Graphen", _[Acta Mathematica Academiae Scientiarum Hungaricae](Acta%20Mathematica%20Hungarica.md)_, __9__ \(3–4\): 395–434, [doi](doi%20(identifier).md):[10.1007/BF02020271](https://doi.org/10.1007%2FBF02020271), [MR](MR%20(identifier).md) [0124238](https://mathscinet.ams.org/mathscinet-getitem?mr=0124238).
- <a id="CITEREFGöösSuomela2014"></a> Göös, Mika; Suomela, Jukka \(2014\), "No sublogarithmic-time approximation scheme for bipartite vertex cover", _Distributed Computing_, __27__ \(6\): 435–443, [arXiv](ArXiv%20(identifier).md):[1205.4605](https://arxiv.org/abs/1205.4605), [doi](doi%20(identifier).md):[10.1007/s00446-013-0194-z](https://doi.org/10.1007%2Fs00446-013-0194-z), [MR](MR%20(identifier).md) [3280546](https://mathscinet.ams.org/mathscinet-getitem?mr=3280546), [S2CID](S2CID%20(identifier).md#S2CID) [13513566](https://api.semanticscholar.org/CorpusID:13513566)
- <a id="CITEREFKőnig1916"></a> [Kőnig, Dénes](Dénes%20Kőnig.md) \(1916\), "Gráfok és alkalmazásuk a determinánsok és a halmazok elméletére", _Matematikai és Természettudományi Értesítő_, __34__: 104–119.
- <a id="CITEREFKőnig1931"></a> [Kőnig, Dénes](Dénes%20Kőnig.md) \(1931\), "Gráfok és mátrixok", _Matematikai és Fizikai Lapok_, __38__: 116–119.
- <a id="CITEREFLovász1972"></a> [Lovász, László](László%20Lovász.md) \(1972\), "Normal hypergraphs and the perfect graph conjecture", _[Discrete Mathematics](Discrete%20Mathematics%20(journal).md)_, __2__ \(3\): 253–267, [doi](doi%20(identifier).md):[10.1016/0012-365X\(72\)90006-4](https://doi.org/10.1016%2F0012-365X%2872%2990006-4), [MR](MR%20(identifier).md) [0302480](https://mathscinet.ams.org/mathscinet-getitem?mr=0302480).
- <a id="CITEREFLovász1974"></a> [Lovász, László](László%20Lovász.md) \(1974\), "Minimax theorems for hypergraphs", _Hypergraph Seminar \(Proc. First Working Sem., Ohio State Univ., Columbus, Ohio, 1972; dedicated to Arnold Ross\)_, Lecture Notes in Mathematics, vol. 411, Berlin: Springer, pp. 111–126, [doi](doi%20(identifier).md):[10.1007/BFb0066186](https://doi.org/10.1007%2FBFb0066186), [ISBN](ISBN%20(identifier).md) [978-3-540-06846-4](https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-06846-4), [MR](MR%20(identifier).md) [0406862](https://mathscinet.ams.org/mathscinet-getitem?mr=0406862).
- <a id="CITEREFLovászPlummer1986"></a> [Lovász, László](László%20Lovász.md); [Plummer, M. D.](Michael%20D.%20Plummer.md) \(1986\), _Matching Theory_, Annals of Discrete Mathematics, vol. 29, North-Holland, [ISBN](ISBN%20(identifier).md) [0-444-87916-1](https://en.wikipedia.org/wiki/Special:BookSources/0-444-87916-1), [MR](MR%20(identifier).md) [0859549](https://mathscinet.ams.org/mathscinet-getitem?mr=0859549)
- <a id="CITEREFStorer2001"></a> Storer, J. A. \(2001\), _An Introduction to Data Structures and Algorithms_, Progress in Computer Science and Applied Logic Series, Springer, [ISBN](ISBN%20(identifier).md) [9780817642532](https://en.wikipedia.org/wiki/Special:BookSources/9780817642532).

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Theorems in graph theory](https://en.wikipedia.org/wiki/Category:Theorems%20in%20graph%20theory)
> - [Perfect graphs](https://en.wikipedia.org/wiki/Category:Perfect%20graphs)
> - [Matching \(graph theory\)](https://en.wikipedia.org/wiki/Category:Matching%20%28graph%20theory%29)
> - [Bipartite graphs](https://en.wikipedia.org/wiki/Category:Bipartite%20graphs)
