Approach to general relativity

- This article is about general tetrads. For orthonormal tetrads, see [Frame fields in general relativity](frame%20fields%20in%20general%20relativity.md).

The __tetrad formalism__ is an approach to [general relativity](general%20relativity.md) that generalizes the choice of [basis](basis%20(linear%20algebra).md) for the [tangent bundle](tangent%20bundle.md) from a [coordinate basis](coordinate%20basis.md) to the less restrictive choice of a local basis, i.e. a locally defined set of four<sup>[\[a\]](#^ref-a)</sup> linearly independent [vector fields](vector%20field.md) called a _[tetrad](tetrad%20(general%20relativity).md)_ or _vierbein_.<sup>[\[1\]](#^ref-1)</sup> It is a special case of the more general idea of a _vielbein formalism_, which is set in [\(pseudo-\)](pseudo-Riemannian%20manifold.md)[Riemannian geometry](Riemannian%20geometry.md). This article as currently written makes frequent mention of general relativity; however, almost everything it says is equally applicable to [\(pseudo-\)](pseudo-Riemannian%20manifold.md)[Riemannian manifolds](Riemannian%20manifold.md) in general, and even to [spin manifolds](spin%20manifold.md#spin%20structures%20on%20vector%20bundles). Most statements hold by substituting arbitrary $n$ for $n=4$. In German, "_vier_" translates to "four", "_viel_" to "many", and "_bein_" to "leg".

The general idea is to write the [metric tensor](metric%20tensor.md) as the product of two _vielbeins_, one on the left, and one on the right. The effect of the vielbeins is to change the coordinate system used on the [tangent manifold](tangent%20manifold.md) to one that is simpler or more suitable for calculations. It is frequently the case that the vielbein coordinate system is orthonormal, as that is generally the easiest to use. Most tensors become simple or even trivial in this coordinate system; thus the complexity of most expressions is revealed to be an artifact of the choice of coordinates, rather than a innate property or physical effect<sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup>. That is, as a formalism, it does not alter predictions; it is rather a calculational technique.

The advantage of the tetrad formalism over the standard coordinate-based approach to general relativity lies in the ability to choose the tetrad basis to reflect important physical aspects of the spacetime. The [abstract index notation](abstract%20index%20notation.md) denotes tensors as if they were represented by their coefficients with respect to a fixed local tetrad. Compared to a [completely coordinate free notation](connection%20form.md), which is often conceptually clearer, it allows an easy and computationally explicit way to denote contractions.

The significance of the tetradic formalism appear in the [Einstein–Cartan](Einstein–Cartan%20theory.md) formulation of general relativity. The tetradic formalism of the theory is more fundamental than its metric formulation as one can _not_ convert between the tetradic and metric formulations of the fermionic actions despite this being possible for bosonic actions <sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup>. This is effectively because Weyl spinors can be very naturally defined on a Riemannian manifold<sup>[\[2\]](#^ref-2)</sup><sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup> and their natural setting leads to the [spin connection](spin%20connection.md). Those spinors take form in the vielbein coordinate system, and not in the manifold coordinate system.

The privileged tetradic formalism also appears in the _[dimensional deconstruction](dimensional%20deconstruction.md)_ of _higher dimensional_[Kaluza–Klein](Kaluza–Klein%20theory.md) gravity theories<sup>[\[3\]](#^ref-3)</sup><sup>[\[4\]](#^ref-4)</sup> and [massive gravity](massive%20gravity.md) theories, in which the extra-dimension\(s\) is/are replaced by series of N [lattice](lattice%20gauge%20theory.md) sites such that the higher dimensional metric is replaced by a set of interacting metrics that depend only on the 4D components.<sup>[\[5\]](#^ref-5)</sup> Vielbeins commonly appear in other general settings in physics and mathematics. Vielbeins can be understood as [solder forms](solder%20form.md).

## mathematical formulation

The tetrad formulation is a special case of a more general formulation, known as the vielbein or n-bein formulation, with n=4. Vielbein is spelled with an "l", not an "r": in German, "viel" means "many", not to be confused with "vier", meaning "four".

In the vielbein formalism,<sup>[\[6\]](#^ref-6)</sup> an [open cover](open%20cover.md#open%20cover) of the [spacetime](spacetime.md) manifold $M$ and a local basis for each of those open sets is chosen: a set of $n$ independent [vector fields](vector%20field.md)

$$e_{a}=e_{a}{}^{\mu }\partial _{\mu }$$
for $a=1,\ldots ,n$ that together span the $n$-dimensional [tangent bundle](tangent%20bundle.md) at each point in the set. Dually, a vielbein \(or tetrad in 4 dimensions\) determines \(and is determined by\) a dual co-vielbein \(co-tetrad\) — a set of $n$ independent [1-forms](1-form.md).

$$e^{a}=e^{a}{}_{\mu }dx^{\mu }$$
such that

$$e^{a}(e_{b})=e^{a}{}_{\mu }e_{b}{}^{\mu }=\delta _{b}^{a},$$
where $\delta _{b}^{a}$ is the [Kronecker delta](Kronecker%20delta.md). A vielbein is usually specified by its coefficients $e^{\mu }{}_{a}$ with respect to a coordinate basis, despite the choice of a set of \(local\) coordinates $x^{\mu }$ being unnecessary for the specification of a tetrad. Each covector is a [solder form](solder%20form.md).

From the point of view of the [differential geometry](differential%20geometry.md) of [fiber bundles](fiber%20bundles.md), the n vector fields $\{e_{a}\}_{a=1\dots n}$ define a section of the [frame bundle](frame%20bundle.md)_i.e._ a [parallelization](parallelization%20(mathematics).md) of $U\subset M$ which is equivalent to an isomorphism $TU\cong U\times {\mathbb {R} ^{n} }$. Since not every manifold is parallelizable, a vielbein can generally only be chosen locally \(_i.e._ only on a [coordinate chart](coordinate%20chart.md#coordinate%20charts)<!-- markdown separator -->$U$ and not all of $M$.\)

All tensors of the theory can be expressed in the vector and covector basis, by expressing them as linear combinations of members of the \(co\)vielbein. For example, the spacetime metric tensor can be transformed from a coordinate basis to the [tetrad](tetrad%20(general%20relativity).md)[basis](basis%20(mathematics).md).

Popular tetrad bases in general relativity include [orthonormal tetrads](frame%20fields%20in%20general%20relativity.md) and null tetrads. Null tetrads are composed of four [null vectors](null%20vector.md), so are used frequently in problems dealing with radiation, and are the basis of the [Newman–Penrose formalism](Newman–Penrose%20formalism.md) and the [GHP formalism](GHP%20formalism.md).

## relation to standard formalism

The standard formalism of [differential geometry](differential%20geometry.md) \(and general relativity\) consists of using the __coordinate tetrad__ in the tetrad formalism. The coordinate tetrad is the canonical set of vectors associated with the [coordinate chart](coordinate%20chart.md#coordinate%20charts). The coordinate tetrad is commonly denoted $\{\partial _{\mu }\}$ whereas the dual cotetrad is denoted $\{dx^{\mu }\}$. These [tangent vectors](tangent%20space.md) are usually defined as [directional derivative](directional%20derivative.md) operators: given a chart ${\varphi =(\varphi ^{1},\ldots ,\varphi ^{n})}$ which maps a subset of the [manifold](manifold.md) into coordinate space $\mathbb {R} ^{n}$, and any [scalar field](scalar%20field.md)<!-- markdown separator -->$f$, the coordinate vectors are such that:

$$\partial _{\mu }[f]\equiv {\frac {\partial (f\circ \varphi ^{-1})}{\partial x^{\mu } } }.$$
The definition of the cotetrad uses the usual abuse of notation $dx^{\mu }=d\varphi ^{\mu }$ to define covectors \(1-forms\) on $M$. The involvement of the coordinate tetrad is not usually made explicit in the standard formalism. In the tetrad formalism, instead of writing tensor equations out fully \(including tetrad elements and [tensor products](tensor%20products.md) $\otimes$ as above\) only _components_ of the tensors are mentioned. For example, the metric is written as "$g_{ab}$". When the tetrad is unspecified this becomes a matter of specifying the type of the tensor called [abstract index notation](abstract%20index%20notation.md). It allows to easily specify contraction between tensors by repeating indices as in the Einstein summation convention.

Changing tetrads is a routine operation in the standard formalism, as it is involved in every coordinate transformation \(i.e., changing from one coordinate tetrad basis to another\). Switching between multiple coordinate charts is necessary because, except in trivial cases, it is not possible for a single coordinate chart to cover the entire manifold. Changing to and between general tetrads is much similar and equally necessary \(except for [parallelizable manifolds](parallelizable%20manifold.md)\). Any [tensor](tensor.md) can locally be written in terms of this coordinate tetrad or a general \(co\)tetrad.

For example, the [metric tensor](metric%20tensor.md) $\mathbf {g}$ can be expressed as:

$$\mathbf {g} =g_{\mu \nu }dx^{\mu }dx^{\nu }\qquad {\text{where} }~g_{\mu \nu }=\mathbf {g} (\partial _{\mu },\partial _{\nu }).$$
\(Here we use the [Einstein summation convention](Einstein%20summation%20convention.md)\). Likewise, the metric can be expressed with respect to an arbitrary \(co\)tetrad as

$$\mathbf {g} =g_{ab}e^{a}e^{b}\qquad {\text{where} }~g_{ab}=\mathbf {g} \left(e_{a},e_{b}\right).$$
Here, we use choice of alphabet \([Latin](Latin%20alphabet.md) and [Greek](Greek%20alphabet.md)\) for the index variables to distinguish the applicable basis.

We can translate from a general co-tetrad to the coordinate co-tetrad by expanding the covector $e^{a}=e^{a}{}_{\mu }dx^{\mu }$. We then get

$$\mathbf {g} =g_{ab}e^{a}e^{b}=g_{ab}e^{a}{}_{\mu }e^{b}{}_{\nu }dx^{\mu }dx^{\nu }=g_{\mu \nu }dx^{\mu }dx^{\nu }$$
from which it follows that $g_{\mu \nu }=g_{ab}e^{a}{}_{\mu }e^{b}{}_{\nu }$. Likewise expanding $dx^{\mu }=e^{\mu }{}_{a}e^{a}$ with respect to the general tetrad, we get

$$\mathbf {g} =g_{\mu \nu }dx^{\mu }dx^{\nu }=g_{\mu \nu }e^{\mu }{}_{a}e^{\nu }{}_{b}e^{a}e^{b}=g_{ab}e^{a}e^{b}$$
which shows that $g_{ab}=g_{\mu \nu }e^{\mu }{}_{a}e^{\nu }{}_{b}$.

### manipulation of indices

The manipulation with tetrad coefficients shows that abstract index formulas can, in principle, be obtained from tensor formulas with respect to a coordinate tetrad by "replacing greek by latin indices". However care must be taken that a coordinate tetrad formula defines a genuine tensor when differentiation is involved. Since the coordinate vector fields have vanishing [Lie bracket](Lie%20bracket%20of%20vector%20fields.md) \(i.e. commute: $\partial _{\mu }\partial _{\nu }=\partial _{\nu }\partial _{\mu }$\), naive substitutions of formulas that correctly compute tensor coefficients with respect to a coordinate tetrad may not correctly define a tensor with respect to a general tetrad because the Lie bracket is non-vanishing: $[e_{a},e_{b}]\neq 0$. Thus, it is sometimes said that tetrad coordinates provide a [non-holonomic basis](holonomic%20basis.md).

For example, the [Riemann curvature tensor](Riemann%20curvature%20tensor.md) is defined for general vector fields $X,Y$ by

$$R(X,Y)=\left(\nabla _{X}\nabla _{Y}-\nabla _{Y}\nabla _{X}-\nabla _{[X,Y]}\right)\,.$$
In a coordinate tetrad this gives tensor coefficients

$$R_{\ \nu \sigma \tau }^{\mu }=dx^{\mu }\left((\nabla _{\sigma }\nabla _{\tau }-\nabla _{\tau }\nabla _{\sigma })\partial _{\nu }\right).$$
The naive "Greek to Latin" substitution of the latter expression

$$R_{\ bcd}^{a}=e^{a}\left((\nabla _{c}\nabla _{d}-\nabla _{d}\nabla _{c})e_{b}\right)\qquad {\text{(wrong!)} }$$
is incorrect because for fixed _c_ and _d_, $\left(\nabla _{c}\nabla _{d}-\nabla _{d}\nabla _{c}\right)$ is, in general, a first order differential operator rather than a zeroth order operator which defines a tensor coefficient. Substituting a general tetrad basis in the abstract formula we find the proper definition of the curvature in abstract index notation, however:

$$R_{\ bcd}^{a}=e^{a}\left((\nabla _{c}\nabla _{d}-\nabla _{d}\nabla _{c}-f_{cd}{}^{e}\nabla _{e})e_{b}\right)$$
where $[e_{a},e_{b}]=f_{ab}{}^{c}e_{c}$. Note that the expression $\left(\nabla _{c}\nabla _{d}-\nabla _{d}\nabla _{c}-f_{cd}{}^{e}\nabla _{e}\right)$ is indeed a zeroth order operator, hence \(the \(_c__d_\)-component of\) a tensor. Since it agrees with the coordinate expression for the curvature when specialised to a coordinate tetrad it is clear, even without using the abstract definition of the curvature, that it defines the same tensor as the coordinate basis expression.

## example: Lie groups

Given a vector \(or covector\) in the tangent \(or cotangent\) manifold, the [exponential map](exponential%20map%20(Riemannian%20geometry).md) describes the corresponding [geodesic](geodesic.md) of that tangent vector. Writing $X\in TM$, the [parallel transport](parallel%20transport.md) of a differential corresponds to

$$e^{-X}de^{X}=dX-{\frac {1}{2!} }\left[X,dX\right]+{\frac {1}{3!} }[X,[X,dX]]-{\frac {1}{4!} }[X,[X,[X,dX]]]+\cdots$$
The above can be readily verified simply by taking $X$ to be a matrix.

For the special case of a [Lie algebra](Lie%20algebra.md), the $X$ can be taken to be an element of the algebra, the exponential is the [exponential map of a Lie group](exponential%20map%20(Lie%20group).md), and group elements correspond to the geodesics of the tangent vector. Choosing a basis $e_{i}$ for the Lie algebra and writing $X=X^{i}e_{i}$ for some functions $X^{i}$, the commutators can be explicitly written out. One readily computes that

$$e^{-X}de^{X}=dX^{i}e_{i}-{\frac {1}{2!} }X^{i}dX^{j}{f_{ij} }^{k}e_{k}+{\frac {1}{3!} }X^{i}X^{j}dX^{k}{f_{jk} }^{l}{f_{il} }^{m}e_{m}-\cdots$$
for $[e_{i},e_{j}]={f_{ij} }^{k}e_{k}$ the [structure constants](structure%20constant.md) of the Lie algebra. The series can be written more compactly as

$$e^{-X}de^{X}=e_{i}{W^{i} }_{j}dX^{j}$$
with the infinite series

$$W=\sum _{n=0}^{\infty }{\frac {(-1)^{n}M^{n} }{(n+1)!} }=(I-e^{-M})M^{-1}.$$
Here, $M$ is a matrix whose matrix elements are ${M_{j} }^{k}=X^{i}{f_{ij} }^{k}$. The matrix $W$ is then the vielbein; it expresses the differential $dX^{j}$ in terms of the "flat coordinates" \(orthonormal, at that\) $e_{i}$.

Given some map $N\to G$ from some manifold $N$ to some Lie group $G$, the metric tensor on the manifold $N$ becomes the pullback of the metric tensor $B_{mn}$ on the Lie group $G$:

$$g_{ij}={W_{i} }^{m}B_{mn}{W^{n} }_{j}$$
The metric tensor $B_{mn}$ on the Lie group is the Cartan metric, aka the [Killing form](Killing%20form.md). Note that, as a matrix, the second W is the transpose. For $N$ a \(pseudo-\)[Riemannian manifold](Riemannian%20manifold.md), the metric is a \(pseudo-\)[Riemannian metric](Riemannian%20metric.md#Riemannian%20metrics%20and%20Riemannian%20manifolds). The above generalizes to the case of [symmetric spaces](symmetric%20space.md).<sup>[\[7\]](#^ref-7)</sup> These vielbeins are used to perform calculations in [sigma models](sigma%20model.md), of which the [supergravity theories](supergravity.md) are a special case.<sup>[\[8\]](#^ref-8)</sup>

## see also

- [Frame bundle](frame%20bundle.md)
- [Orthonormal frame bundle](orthonormal%20frame%20bundle.md#orthonormal%20frame%20bundle)
- [Principal bundle](principal%20bundle.md)
- [Spin bundle](spin%20bundle.md)
- [Connection \(mathematics\)](connection%20(mathematics).md)
- [G-structure](G-structure.md)
- [Spin manifold](spin%20manifold.md#spin%20structures%20on%20vector%20bundles)
- [Spin structure](spin%20structure.md)
- [Dirac equation in curved spacetime](Dirac%20equation%20in%20curved%20spacetime.md)

## notes

1. The same approach can be used for a spacetime of arbitrary dimension, where the frame of the [frame bundle](frame%20bundle.md) is referred to as an _n-bein_ or _vielbein_. <a id="^lower-alpha-1"></a>^lower-alpha-1

## citations

1. <a id="CITEREFDe FeliceClarke1990"></a> De Felice, F.; Clarke, C. J. S. \(1990\), _Relativity on Curved Manifolds_, Cambridge University Press, p. 133, [ISBN](ISBN%20(identifier).md) [0-521-26639-4](https://en.wikipedia.org/wiki/Special:BookSources/0-521-26639-4) <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFJost1995"></a> [Jost, Jürgen](Jürgen%20Jost.md) \(1995\), _Riemannian Geometry and Geometric Analysis_, Springer, [ISBN](ISBN%20(identifier).md) [3-540-57113-2](https://en.wikipedia.org/wiki/Special:BookSources/3-540-57113-2) <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFArkani-HamedCohenGeorgi2001"></a> Arkani-Hamed, Nima; Cohen, Andrew G.; Georgi, Howard \(May 2001\). ["\(De\)Constructing Dimensions"](https://link.aps.org/doi/10.1103/PhysRevLett.86.4757). _Physical Review Letters_. __86__ \(21\): 4757–4761. [arXiv](ArXiv%20(identifier).md):[hep-th/0104005](https://arxiv.org/abs/hep-th/0104005). [Bibcode](bibcode%20(identifier).md):[2001PhRvL..86.4757A](https://ui.adsabs.harvard.edu/abs/2001PhRvL..86.4757A). [doi](doi%20(identifier).md):[10.1103/PhysRevLett.86.4757](https://doi.org/10.1103%2FPhysRevLett.86.4757). [ISSN](ISSN%20(identifier).md) [0031-9007](https://search.worldcat.org/issn/0031-9007). [PMID](PMID%20(identifier).md#PubMed%20identifier) [11384341](https://pubmed.ncbi.nlm.nih.gov/11384341). [S2CID](S2CID%20(identifier).md#S2CID) [4540121](https://api.semanticscholar.org/CorpusID:4540121). <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFHillPokorskiWang2001"></a> Hill, Christopher T.; Pokorski, Stefan; Wang, Jing \(2001-10-11\). "Gauge invariant effective Lagrangian for Kaluza-Klein modes". _Physical Review D_. __64__ \(10\) 105005. American Physical Society \(APS\). [arXiv](ArXiv%20(identifier).md):[hep-th/0104035](https://arxiv.org/abs/hep-th/0104035). [Bibcode](bibcode%20(identifier).md):[2001PhRvD..64j5005H](https://ui.adsabs.harvard.edu/abs/2001PhRvD..64j5005H). [doi](doi%20(identifier).md):[10.1103/physrevd.64.105005](https://doi.org/10.1103%2Fphysrevd.64.105005). [ISSN](ISSN%20(identifier).md) [0556-2821](https://search.worldcat.org/issn/0556-2821). [S2CID](S2CID%20(identifier).md#S2CID) [7377062](https://api.semanticscholar.org/CorpusID:7377062). <a id="^ref-4"></a>^ref-4
5. <a id="CITEREFde Rham2014"></a> de Rham, Claudia \(December 2014\). ["Massive Gravity"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5256007). _Living Reviews in Relativity_. __17__ \(1\): 7. [arXiv](ArXiv%20(identifier).md):[1401.4173](https://arxiv.org/abs/1401.4173). [Bibcode](bibcode%20(identifier).md):[2014LRR....17....7D](https://ui.adsabs.harvard.edu/abs/2014LRR....17....7D). [doi](doi%20(identifier).md):[10.12942/lrr-2014-7](https://doi.org/10.12942%2Flrr-2014-7). [ISSN](ISSN%20(identifier).md) [2367-3613](https://search.worldcat.org/issn/2367-3613). [PMC](PMC%20(identifier).md#PMCID) [5256007](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5256007). [PMID](PMID%20(identifier).md#PubMed%20identifier) [28179850](https://pubmed.ncbi.nlm.nih.gov/28179850). <a id="^ref-5"></a>^ref-5
6. Tohru Eguchi, Peter B. Gilkey and Andrew J. Hanson, "[Gravitation, Gauge Theories and Differential Geometry](https://www.researchgate.net/publication/234195796_Gravitation_Gauge_Theories_And_Differential_Geometry)", _Physics Reports___66__ \(1980\) pp 213-393. <a id="^ref-6"></a>^ref-6
7. Nejat Tevfik Yilmaz, \(2007\) "On the Symmetric Space Sigma-Model Kinematics" arXiv:0707.2150 \[hep-th\] <a id="^ref-7"></a>^ref-7
8. Arjan Keurentjes \(2003\) "The group theory of oxidation", arXiv:0210178 \[hep-th\] <a id="^ref-8"></a>^ref-8

## references

- <a id="mwAA"></a> De Felice, F.; Clarke, C.J.S. \(1990\), _Relativity on Curved Manifolds_ \(first published 1990 ed.\), Cambridge University Press, [ISBN](ISBN%20(identifier).md) [0-521-26639-4](https://en.wikipedia.org/wiki/Special:BookSources/0-521-26639-4)
- <a id="CITEREFBennTucker1987"></a> Benn, I.M.; Tucker, R.W. \(1987\), _An introduction to Spinors and Geometry with Applications in Physics_ \(first published 1987 ed.\), Adam Hilger, [ISBN](ISBN%20(identifier).md) [0-85274-169-3](https://en.wikipedia.org/wiki/Special:BookSources/0-85274-169-3)

## external links

- [General Relativity with Tetrads](https://web.archive.org/web/20091229024331/http://casa.colorado.edu/~ajsh/phys5770_08/grtetrad.pdf)
