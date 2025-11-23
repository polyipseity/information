---
aliases:
  - indicator function
  - indicator functions
tags:
  - flashcard/active/general/eng/indicator_function
  - language/in/English
---

# indicator function

- This article is about {@{the 0-1 indicator function}@}. For {@{the 0-infinity indicator function}@}, see {@{[characteristic function \(convex analysis\)](characteristic%20function%20(convex%20analysis).md)}@}. <!--SR:!2028-10-20,1078,350!2025-12-08,262,330!2025-12-17,269,330-->

<!-- | ![](../../archives/Wikimedia%20Commons/Text%20document%20with%20red%20question%20mark.svg) | This article includes a list of [general references](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources#General%20references), but __it lacks sufficient corresponding [inline citations](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources#Inline%20citations)__. Please help to [improve](https://en.wikipedia.org/wiki/Wikipedia:WikiProject%20Reliability) this article by [introducing](https://en.wikipedia.org/wiki/Wikipedia:When%20to%20cite) more precise citations. _\(December 2009\)__ \([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ | -->

> {@{![A three-dimensional plot of an indicator function, shown over a square two-dimensional domain \(set _X_\): the "raised" portion overlays those two-dimensional points which are members of the "indicated" subset \(_A_\).](../../archives/Wikimedia%20Commons/Indicator%20function%20illustration.png)}@}
>
> {@{A three-dimensional plot of an indicator function}@}, shown over {@{a square two-dimensional domain \(set _X_\)}@}: {@{the "raised" portion}@} {@{overlays those two-dimensional points which are members of the "indicated" subset \(_A_\)}@}. <!--SR:!2027-09-11,746,330!2025-12-08,262,330!2025-12-15,268,330!2025-12-25,276,330!2025-12-29,278,330-->

In {@{[mathematics](mathematics.md)}@}, {@{an __indicator function__ or a __characteristic function__}@} of {@{a [subset](subset.md) of a [set](set%20(mathematics).md) is a [function](function%20(mathematics).md) that maps elements of the subset to one, and all other elements to zero}@}. That is, if {@{_A_ is a subset of some set _X_}@}, then {@{$\mathbf {1} _{A}(x)=1$ if $x\in A$, and $\mathbf {1} _{A}(x)=0$ otherwise}@}, where {@{$\mathbf {1} _{A}$ is a common notation for the indicator function}@}. Other common notations are {@{$I_{A}$, and $\chi _{A}$}@}. <!--SR:!2028-11-22,1103,350!2028-11-18,1101,350!2027-09-24,756,330!2028-11-13,1097,350!2025-11-27,254,330!2025-12-14,267,330!2029-01-09,1143,350-->

{@{The indicator function of _A_}@} is {@{the [Iverson bracket](Iverson%20bracket.md) of the property of belonging to _A_}@}; that is, {@{$$\mathbf {1} _{A}(x)=[x\in A].$$}@} For example, {@{the [Dirichlet function](Dirichlet%20function.md)}@} is {@{the indicator function of the [rational numbers](rational%20number.md) as a subset of the [real numbers](real%20number.md)}@}. <!--SR:!2025-12-19,271,330!2025-12-06,260,330!2028-10-24,1081,350!2028-11-23,1104,350!2027-08-03,716,330-->

## definition

{@{The indicator function of a subset _A_ of a set _X_}@} is {@{a function $$\mathbf {1} _{A}\colon X\to \{0,1\}$$}@} defined {@{as [$$\mathbf {1} _{A}(x):={\begin{cases}1~&{\text{ if } }~x\in A~,\\0~&{\text{ if } }~x\notin A~.\end{cases} }$$](https://en.wikipedia.org/w/index.php?title=Special:MathWikibase&qid=Q371983)}@} {@{The [Iverson bracket](Iverson%20bracket.md)}@} provides {@{the equivalent notation, $[x\in A]$ or ⟦<!-- markdown separator -->_x_ ∈ _A_<!-- markdown separator -->⟧}@}, to be used instead of $\mathbf {1}_{A}(x)\,$. <!--SR:!2026-01-03,282,330!2026-01-14,291,330!2025-12-20,272,330!2026-01-16,293,330!2025-12-31,280,330-->

The function $\mathbf {1} _{A}$ is sometimes denoted {@{_I<sub>A</sub>_, _χ<sub>A</sub>_, _K<sub>A</sub>_, or even just _A_}@}.<sup>[\[a\]](#^ref-a)</sup><sup>[\[b\]](#^ref-b)</sup> <!--SR:!2025-12-15,268,330-->

## notation and terminology

{@{The notation $\chi _{A}$}@} is also used to {@{denote the [characteristic function](characteristic%20function%20(convex%20analysis).md) in [convex analysis](convex%20analysis.md)}@}, which is defined {@{as if using the [reciprocal](multiplicative%20inverse.md) of the standard definition of the indicator function}@}. <!--SR:!2025-12-11,264,330!2025-11-25,252,330!2025-12-13,266,330-->

{@{A related concept in [statistics](statistics.md)}@} is that of {@{a [dummy variable](dummy%20variable%20(statistics).md)}@}. \(This must not {@{be confused with "dummy variables" as that term is usually used in mathematics}@}, also called {@{a [bound variable](free%20variables%20and%20bound%20variables.md)}@}.\) <!--SR:!2026-01-05,284,330!2026-01-11,289,330!2027-12-05,813,330!2026-01-14,291,330-->

{@{The term "[characteristic function](characteristic%20function%20(probability%20theory).md)"}@} has {@{an unrelated meaning in [classic probability theory](probability%20theory.md)}@}. For this reason, {@{[traditional probabilists](list%20of%20mathematical%20probabilists.md)}@} use {@{the term __indicator function__ for the function defined here almost exclusively}@}, while {@{mathematicians in other fields are more likely to use the term _characteristic function_<sup>[\[a\]](#^ref-a)</sup> to describe the function that indicates membership in a set}@}. <!--SR:!2026-01-17,294,330!2028-09-25,1057,350!2028-11-29,1109,350!2028-01-19,838,330!2025-12-20,272,330-->

In {@{[fuzzy logic](fuzzy%20logic.md) and [modern many-valued logic](many-valued%20logic.md)}@}, {@{predicates}@} are {@{the [characteristic functions](characteristic%20function%20(probability%20theory).md) of a [probability distribution](probability%20distribution.md)}@}. That is, {@{the strict true/false valuation of the predicate}@} is replaced by {@{a quantity interpreted as the degree of truth}@}. <!--SR:!2027-11-11,794,330!2028-09-16,1050,350!2027-10-08,768,330!2025-11-27,254,330!2028-11-01,1087,350-->

## basic properties

{@{The _indicator_ or _characteristic_ [function](function%20(mathematics).md) of a subset _A_ of some set _X_}@} {@{[maps](map%20(mathematics).md) elements of _X_ to the [range](range%20of%20a%20function.md) $\{0,1\}$}@}. <!--SR:!2028-11-19,1101,350!2025-11-26,253,330-->

This mapping is {@{[surjective](surjective%20function.md) only when _A_ is a non-empty [proper subset](subset.md) of _X_}@}. If {@{$A\equiv X$, then $\mathbf {1} _{A}=1$}@}. By a similar argument, if {@{$A\equiv \emptyset$ then $\mathbf {1} _{A}=0$}@}. <!--SR:!2028-12-11,1121,350!2028-10-18,1077,350!2025-12-09,263,330-->

If {@{$A$ and $B$ are two subsets of $X$}@}, then {@{$${\begin{aligned}\mathbf {1} _{A\cap B}&=\min\{\mathbf {1} _{A},\mathbf {1} _{B}\}=\mathbf {1} _{A}\cdot \mathbf {1} _{B},\\\mathbf {1} _{A\cup B}&=\max\{ {\mathbf {1} _{A},\mathbf {1} _{B} }\}=\mathbf {1} _{A}+\mathbf {1} _{B}-\mathbf {1} _{A}\cdot \mathbf {1} _{B},\end{aligned} }$$}@} and {@{the indicator function of the [complement](complement%20(set%20theory).md) of $A$ i.e. $A^{C}$}@} is: {@{$$\mathbf {1} _{A^{\complement } }=1-\mathbf {1} _{A}.$$}@} More generally, suppose {@{$A_{1},\dotsc ,A_{n}$ is a collection of subsets of _X_}@}. For any {@{$x\in X:$ $$\prod _{k\in I}(1-\mathbf {1} _{A_{k} }(x))$$}@} is {@{clearly a product of 0s and 1s}@}. This product has {@{the value 1}@} at {@{precisely those $x\in X$ that belong to none of the sets $A_{k}$}@} and is {@{0 otherwise}@}. That is {@{$$\prod _{k\in I}(1-\mathbf {1} _{A_{k} })=\mathbf {1} _{X-\bigcup _{k}A_{k} }=1-\mathbf {1} _{\bigcup _{k}A_{k} }.$$}@} Expanding {@{the product on the left hand side}@}, {@{$$\mathbf {1} _{\bigcup _{k}A_{k} }=1-\sum _{F\subseteq \{1,2,\dotsc ,n\} }(-1)^{|F|}\mathbf {1} _{\bigcap _{F}A_{k} }=\sum _{\emptyset \neq F\subseteq \{1,2,\dotsc ,n\} }(-1)^{|F|+1}\mathbf {1} _{\bigcap _{F}A_{k} }$$}@} where {@{$|F|$ is the [cardinality](cardinality.md) of _F_}@}. This is one form of {@{the principle of [inclusion-exclusion](inclusion–exclusion%20principle.md)}@}. <!--SR:!2027-08-22,731,330!2025-12-22,273,330!2026-01-12,290,330!2026-01-17,294,330!2025-12-23,274,330!2026-01-02,281,330!2025-12-07,261,330!2028-12-17,1125,350!2027-12-02,811,330!2028-11-12,1097,350!2026-12-14,521,310!2025-11-25,252,330!2026-01-08,286,330!2025-12-16,25,370!2025-12-16,25,370-->

As suggested by the previous example, the indicator function is {@{a useful notational device in [combinatorics](combinatorics.md)}@}. The notation is {@{used in other places as well}@}, for instance in {@{[probability theory](probability%20theory.md)}@}: if {@{_X_ is a [probability space](probability%20space.md) with probability measure $\operatorname {P}$ and _A_ is a [measurable set](measure%20(mathematics).md)}@}, then {@{$\mathbf {1} _{A}$ becomes a [random variable](random%20variable.md) whose [expected value](expected%20value.md) is equal to the probability of _A_}@}: {@{$$\operatorname {E} (\mathbf {1} _{A})=\int _{X}\mathbf {1} _{A}(x)\,d\operatorname {P} =\int _{A}d\operatorname {P} =\operatorname {P} (A).$$}@} This identity is used in {@{a simple proof of [Markov's inequality](Markov's%20inequality.md)}@}. <!--SR:!2028-10-02,1062,350!2026-01-10,288,330!2025-12-21,272,330!2027-09-21,755,330!2026-01-15,292,330!2026-01-02,281,330!2027-07-29,711,330-->

In many cases, such as {@{[order theory](order%20theory.md)}@}, {@{the inverse of the indicator function (annotation: "inverse" means elements of the subset are mapped to 0 instead of 1, and vice versa) may be defined}@}. This is commonly called {@{the [generalized Möbius function](incidence%20algebra.md)}@}, as {@{a generalization of the inverse of the indicator function in elementary [number theory](number%20theory.md)}@}, {@{the [Möbius function](Möbius%20function.md)}@}. \(See paragraph below about {@{the use of the inverse in classical recursion theory}@}.\) <!--SR:!2028-12-23,1129,350!2028-12-20,1127,350!2026-01-04,283,330!2027-03-16,560,310!2025-11-28,255,330!2026-01-06,103,384-->

## mean, variance and covariance

Given {@{a [probability space](probability%20space.md) $\textstyle (\Omega ,{\mathcal {F} },\operatorname {P} )$ with $A\in {\mathcal {F} }$}@}, {@{the indicator random variable $\mathbf {1} _{A}\colon \Omega \rightarrow \mathbb {R}$}@} is defined by {@{$\mathbf {1} _{A}(\omega )=1$ if $\omega \in A$, otherwise $\mathbf {1} _{A}(\omega )=0$}@}. <!--SR:!2027-08-02,715,330!2028-12-06,1115,350!2028-11-07,1092,350-->

__[Mean](mean.md)__ <br/> ::@:: &emsp;&emsp; $\operatorname {E} (\mathbf {1} _{A}(\omega ))=\operatorname {P} (A)$ \(also called "Fundamental Bridge"\). <!--SR:!2025-12-09,263,330!2026-01-04,283,330-->

__[Variance](variance.md)__ <br/> ::@:: &emsp;&emsp; $\operatorname {Var} (\mathbf {1} _{A}(\omega ))=\operatorname {P} (A)(1-\operatorname {P} (A))$ <!--SR:!2026-04-30,343,290!2026-01-09,287,330-->

__[Covariance](covariance.md)__ <br/> ::@:: &emsp;&emsp; $\operatorname {Cov} (\mathbf {1} _{A}(\omega ),\mathbf {1} _{B}(\omega ))=\operatorname {P} (A\cap B)-\operatorname {P} (A)\operatorname {P} (B)$ <!--SR:!2026-01-22,249,270!2026-10-13,394,250-->

## characteristic function in recursion theory, Gödel's and Kleene's representing function

{@{[Kurt Gödel](Kurt%20Gödel.md)}@} described {@{the _representing function_}@} in {@{his 1934 paper "On undecidable propositions of formal mathematical systems"}@} \(the "¬" indicates {@{logical inversion, i.e. "NOT"}@}\):<sup>[\[1\]](#^ref-1)</sup><sup>:&hairsp;42&hairsp;</sup> <!--SR:!2026-01-07,285,330!2027-10-19,776,330!2027-12-09,818,330!2025-11-26,253,330-->

> There shall {@{correspond to each class or relation _R_}@} a representing function {@{$\phi (x_{1},\ldots x_{n})=0$ if $R(x_{1},\ldots x_{n})$ and $\phi (x_{1},\ldots x_{n})=1$ if $\neg R(x_{1},\ldots x_{n})$}@}. <!--SR:!2025-11-26,253,330!2026-01-17,294,330-->

{@{[Kleene](Stephen%20Cole%20Kleene.md)}@} offers up {@{the same definition in the context of the [primitive recursive functions](primitive%20recursive%20function.md)}@} as {@{a function _φ_ of a predicate _P_ takes on values 0 if the predicate is true and 1 if the predicate is false}@}.<sup>[\[2\]](#^ref-2)</sup> <!--SR:!2029-01-07,1142,350!2027-06-17,681,330!2028-12-28,1133,350-->

For example, because {@{the product of characteristic functions $\phi _{1}*\phi _{2}*\cdots *\phi _{n}=0$ whenever any one of the functions equals 0}@}, it {@{plays the role of logical OR}@}: {@{IF $\phi _{1}=0$ OR $\phi _{2}=0$ OR ... OR $\phi _{n}=0$ THEN their product is 0}@}. What appears to the modern reader as {@{the representing function's logical inversion}@}, i.e. {@{the representing function is 0}@} when {@{the function _R_ is "true" or satisfied"}@}, plays {@{a useful role in Kleene's definition}@} of {@{the logical functions OR, AND, and IMPLY}@},<sup>[\[2\]](#^ref-2)</sup><sup>:&hairsp;228&hairsp;</sup> {@{the bounded-<sup>[\[2\]](#^ref-2)</sup><sup>:&hairsp;228&hairsp;</sup> and unbounded-<sup>[\[2\]](#^ref-2)</sup><sup>:&hairsp;279 ff&hairsp;</sup> [mu operators](mu%20operator.md) and the CASE function}@}.<sup>[\[2\]](#^ref-2)</sup><sup>:&hairsp;229&hairsp;</sup> <!--SR:!2028-12-13,1122,350!2025-12-18,270,330!2026-01-11,289,330!2027-12-18,774,330!2025-12-07,261,330!2026-02-27,301,290!2025-12-05,23,367!2025-12-05,23,367!2025-12-10,23,368-->

## characteristic function in fuzzy set theory

In {@{classical mathematics}@}, characteristic functions of sets {@{only take values 1 \(members\) or 0 \(non-members\)}@}. In {@{_[fuzzy set theory](fuzzy%20set.md)_}@}, characteristic functions are {@{generalized to take value in the real unit interval \[0, 1\]}@}, or {@{more generally, in some [algebra](universal%20algebra.md) or [structure](structure%20(mathematical%20logic).md)}@} \(usually {@{required to be at least a [poset](partially%20ordered%20set.md) or [lattice](lattice%20(order).md)}@}\). Such generalized characteristic functions are more usually called {@{[membership functions](membership%20function%20(mathematics).md)}@}, and the corresponding "sets" are called {@{_fuzzy_ sets}@}. Fuzzy sets {@{model the gradual change in the membership [degree](degree%20of%20truth.md)}@} seen in {@{many real-world [predicates](predicate%20(mathematical%20logic).md) like "tall", "warm", etc.}@} <!--SR:!2025-12-13,266,330!2026-01-06,285,330!2027-10-11,770,330!2025-12-08,262,330!2026-01-03,282,330!2025-12-28,277,330!2025-12-19,271,330!2026-01-04,283,330!2025-11-27,254,330!2027-08-21,730,330-->

## smoothness

- See also: [Laplacian of the indicator](Laplacian%20of%20the%20indicator.md)

In general, the indicator function of a set is {@{not smooth}@}; it is {@{continuous if and only if its [support](support%20(mathematics).md) is a [connected component](connected%20space.md#connected%20components)}@}. In {@{the [algebraic geometry](algebraic%20geometry.md) of [finite fields](finite%20field.md)}@}, however, {@{every [affine variety](affine%20variety.md) admits a \([Zariski](Zariski%20topology.md)\) continuous indicator function}@}.<sup>[\[3\]](#^ref-3)</sup> Given {@{a [finite set](finite%20set.md) of functions $f_{\alpha }\in \mathbb {F} _{q}[x_{1},\ldots ,x_{n}]$ (annotation: $f_\alpha$ accepts $n$ arguments from a finite fields of order $q$)}@} let {@{$V=\left\{x\in \mathbb {F} _{q}^{n}:f_{\alpha }(x)=0\right\}$ be their vanishing locus (annotation: $\mathbb F_q^n$ is a Cartesian product of $n$ finite fields of order $q$)}@}. Then, {@{the function $P(x)=\prod \left(1-f_{\alpha }(x)^{q-1}\right)$}@} {@{acts as an indicator function for $V$}@}. If {@{$x\in V$ then $P(x)=1$}@}, otherwise, {@{for some $f_{\alpha }$, we have $f_{\alpha }(x)\neq 0$}@}, which {@{implies that $f_{\alpha }(x)^{q-1}=1$ (annotation: Looks like [Euler's theorem](Euler's%20theorem.md)...?), hence $P(x)=0$}@}. <!--SR:!2026-01-09,287,330!2026-05-26,344,290!2025-12-24,275,330!2027-05-27,611,290!2026-12-26,504,310!2026-10-22,480,310!2026-08-10,389,290!2028-01-20,838,330!2026-01-10,288,330!2027-09-11,737,330!2026-03-15,311,290-->

Although {@{indicator functions are not smooth}@}, they {@{admit [weak derivatives](weak%20derivative.md)}@}. For example, consider {@{[Heaviside step function](Heaviside%20step%20function.md) $$H(x):=\mathbf {1} _{x>0}$$}@} {@{The [distributional derivative](distribution%20(mathematics).md#differentiation%20of%20distributions) (annotation: a generalized function using the theory of distribution) of the Heaviside step function}@} is equal to {@{the [Dirac delta function](Dirac%20delta%20function.md), i.e. $${\frac {dH(x)}{dx} }=\delta (x)$$}@} and similarly {@{the distributional derivative of $$G(x):=\mathbf {1} _{x<0}$$ is $${\frac {dG(x)}{dx} }=-\delta (x)$$}@} Thus {@{the derivative of the Heaviside step function}@} can be seen as {@{the _inward normal derivative_ at the _boundary_ of the domain given by the positive half-line}@}. (annotation: Consider {@{the graph of a Heaviside step function}@}. The _positive half-line_ is {@{the graph on the positive real numbers (_not_ the part of the graph that has a value of 1)}@}. Then the _inward normal_ at the _boundary_ of the domain can be considered as {@{an arrow pointing inwards (into the domain)}@}. Finally, the _inward normal derivative_ is {@{simply the derivative evaluated in the direction of the inward normal}@}.) In {@{higher dimensions}@}, the derivative {@{naturally generalises to the inward normal derivative}@}, while the Heaviside step function {@{naturally generalises to the indicator function of some domain _D_}@}. The surface of _D_ will be denoted by {@{_S_}@}. Proceeding, it can be derived that {@{the [inward normal derivative of the indicator](laplacian%20of%20the%20indicator.md#dirac%20surface%20delta%20function) gives rise to a 'surface delta function'}@}, which can be indicated by {@{$\delta _{S}(\mathbf {x} )$}@}: {@{$$\delta _{S}(\mathbf {x} )=-\mathbf {n} _{x}\cdot \nabla _{x}\mathbf {1} _{\mathbf {x} \in D}$$}@} (annotation: The function is essentially {@{1 if $\mathbf x \in S$ and 0 otherwise}@}.) where {@{_n_ is the outward [normal](normal%20(geometry).md) of the surface _S_}@}. This 'surface delta function' has the following property:<sup>[\[4\]](#^ref-4)</sup> {@{$$-\int _{\mathbb {R} ^{n} }f(\mathbf {x} )\,\mathbf {n} _{x}\cdot \nabla _{x}\mathbf {1} _{\mathbf {x} \in D}\;d^{n}\mathbf {x} =\oint _{S}\,f(\mathbf {\beta } )\;d^{n-1}\mathbf {\beta } .$$}@} (annotation: This is saying {@{integrating $f(\mathbf x)$ multiplied by the indicator function of $S$, $\delta_S(\mathbf x)$, over the _n_ dimensional $\mathbb R^n$ equals integrating $f(\beta)$ over the _n_ − 1 dimensional $S$}@}.) By {@{setting the function _f_ equal to one}@}, it follows that {@{the [inward normal derivative of the indicator](laplacian%20of%20the%20indicator.md#dirac%20surface%20delta%20function) integrates to the numerical value of the [surface area](surface%20area.md) _S_}@}. <!--SR:!2026-01-08,286,330!2025-12-29,278,330!2025-12-14,267,330!2026-03-01,287,290!2028-10-30,1086,350!2027-10-20,769,330!2025-12-16,268,330!2026-01-01,281,330!2026-01-01,281,330!2025-12-23,274,330!2027-06-08,677,330!2028-02-12,855,330!2026-01-16,293,330!2027-11-30,808,330!2025-12-28,277,330!2025-11-25,252,330!2025-12-25,276,330!2026-01-15,292,330!2026-05-02,345,290!2027-10-03,755,330!2027-09-07,734,330!2027-01-11,506,270!2026-05-01,344,290!2027-11-27,807,330!2026-08-18,393,290-->

## see also

- [Dirac measure](Dirac%20measure.md)
- [Laplacian of the indicator](Laplacian%20of%20the%20indicator.md)
- [Dirac delta](Dirac%20delta%20function.md)
- [Extension \(predicate logic\)](extension%20(predicate%20logic).md)
- [Free variables and bound variables](free%20variables%20and%20bound%20variables.md)
- [Heaviside step function](Heaviside%20step%20function.md)
- [Identity function](identity%20function.md)
- [Iverson bracket](Iverson%20bracket.md)
- [Kronecker delta](Kronecker%20delta.md), ::@:: a function that can be viewed as an indicator for the [identity relation](equality%20(mathematics).md) <!--SR:!2025-12-12,265,330!2027-06-05,674,330-->
- [Macaulay brackets](Macaulay%20brackets.md)
- [Multiset](multiset.md)
- [Membership function](membership%20function%20(mathematics).md)
- [Simple function](simple%20function.md)
- [Dummy variable \(statistics\)](dummy%20variable%20(statistics).md)
- [Statistical classification](statistical%20classification.md)
- [Zero-one loss function](loss%20function.md#0-1%20loss%20function)

## notes

1. a. The [Greek letter](Greek%20alphabet.md) _χ_ appears because ::@:: it is the initial letter of the Greek word χαρακτήρ, which is the ultimate origin of the word _characteristic_. <a id="^ref-a"></a>^ref-a <!--SR:!2026-07-20,416,310!2025-11-28,255,330-->
2. b. The set of all indicator functions on _X_ can be {@{identified with ${\mathcal {P} }(X)$, the [power set](power%20set.md) of _X_}@}. Consequently, {@{both sets are sometimes denoted by $2^{X}$}@}. This is a special case {@{\( $Y=\{0,1\}=2$\) of the notation $Y^{X}$ for the set of all functions $f:X\to Y$}@}. <a id="^ref-b"></a>^ref-b <!--SR:!2026-01-16,293,330!2025-12-30,279,330!2028-11-06,1092,350-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/indicator_function) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFDavis1965"></a> [Davis, Martin](Martin%20Davis%20(mathematician).md), ed. \(1965\). _The Undecidable_. New York, NY: Raven Press Books. pp. 41–74. <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFKleene1971"></a> [Kleene, Stephen](Stephen%20Cole%20Kleene.md) \(1971\) \[1952\]. _Introduction to Metamathematics_ \(Sixth reprint, with corrections ed.\). Netherlands: Wolters-Noordhoff Publishing and North Holland Publishing Company. p. 227. <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFSerre"></a> Serre. _Course in Arithmetic_. p. 5. <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFLange2012"></a> Lange, Rutger-Jan \(2012\). "Potential theory, path integrals and the Laplacian of the indicator". _Journal of High Energy Physics_. __2012__ \(11\): 29–30. [arXiv](ArXiv.md):[1302.0864](https://arxiv.org/abs/1302.0864). [Bibcode](bibcode.md):[2012JHEP...11..032L](https://ui.adsabs.harvard.edu/abs/2012JHEP...11..032L). [doi](digital%20object%20identifier.md):[10.1007/JHEP11\(2012\)032](https://doi.org/10.1007%2FJHEP11%282012%29032). [S2CID](Semantic%20Scholar.md#S2CID) [56188533](https://api.semanticscholar.org/CorpusID:56188533). <a id="^ref-4"></a>^ref-4

## sources

- <a id="CITEREFFolland1999"></a> Folland, G.B. \(1999\). _Real Analysis: Modern Techniques and Their Applications_ \(Second ed.\). John Wiley & Sons, Inc. [ISBN](ISBN.md) [978-0-471-31716-6](https://en.wikipedia.org/wiki/Special:BookSources/978-0-471-31716-6).
- <a id="CITEREFCormenLeisersonRivestStein2001"></a> [Cormen, Thomas H.](Thomas%20H.%20Cormen.md); [Leiserson, Charles E.](Charles%20E.%20Leiserson.md); [Rivest, Ronald L.](Ron%20Rivest.md); [Stein, Clifford](Clifford%20Stein.md) \(2001\). "Section 5.2: Indicator random variables". [_Introduction to Algorithms_](Introduction%20to%20Algorithms.md) \(Second ed.\). MIT Press and McGraw-Hill. pp. [94](https://archive.org/details/introductiontoal00corm_691/page/n116)–99. [ISBN](ISBN.md) [978-0-262-03293-3](https://en.wikipedia.org/wiki/Special:BookSources/978-0-262-03293-3).
- <a id="CITEREFDavis1965"></a> [Davis, Martin](Martin%20Davis%20(mathematician).md), ed. \(1965\). _The Undecidable_. New York, NY: Raven Press Books.
- <a id="CITEREFKleene1971"></a> [Kleene, Stephen](Stephen%20Cole%20Kleene.md) \(1971\) \[1952\]. _Introduction to Metamathematics_ \(Sixth reprint, with corrections ed.\). Netherlands: Wolters-Noordhoff Publishing and North Holland Publishing Company.
- <a id="CITEREFBoolosBurgessJeffrey2002"></a> [Boolos, George](George%20Boolos.md); [Burgess, John P.](John%20P.%20Burgess.md); [Jeffrey, Richard C.](Richard%20Jeffrey.md) \(2002\). _Computability and Logic_. Cambridge UK: Cambridge University Press. [ISBN](ISBN.md) [978-0-521-00758-0](https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-00758-0).
- <a id="CITEREFZadeh1965"></a> [Zadeh, L.A.](Lotfi%20A.%20Zadeh.md) \(June 1965\). ["Fuzzy sets"](https://doi.org/10.1016%2FS0019-9958%2865%2990241-X). _[Information and Control](Information%20and%20Computation.md)_. __8__ \(3\). San Diego: 338–353. [doi](digital%20object%20identifier.md):[10.1016/S0019-9958\(65\)90241-X](https://doi.org/10.1016%2FS0019-9958%2865%2990241-X). [ISSN](ISSN.md) [0019-9958](https://search.worldcat.org/issn/0019-9958). [Zbl](ZbMATH%20Open.md) [0139.24606](https://zbmath.org/?format=complete&q=an:0139.24606). [Wikidata](wikidata.md) [Q25938993](d:Q25938993.md).
- <a id="CITEREFGoguen1967"></a> [Goguen, Joseph](Joseph%20Goguen.md) \(1967\). "_L_-fuzzy sets". _Journal of Mathematical Analysis and Applications_. __18__ \(1\): 145–174. [doi](digital%20object%20identifier.md):[10.1016/0022-247X\(67\)90189-8](https://doi.org/10.1016%2F0022-247X%2867%2990189-8). [hdl](Handle%20System.md):[10338.dmlcz/103980](https://hdl.handle.net/10338.dmlcz%2F103980).

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Measure theory](https://en.wikipedia.org/wiki/Category:Measure%20theory)
> - [Integral calculus](https://en.wikipedia.org/wiki/Category:Integral%20calculus)
> - [Real analysis](https://en.wikipedia.org/wiki/Category:Real%20analysis)
> - [Mathematical logic](https://en.wikipedia.org/wiki/Category:Mathematical%20logic)
> - [Basic concepts in set theory](https://en.wikipedia.org/wiki/Category:Basic%20concepts%20in%20set%20theory)
> - [Probability theory](https://en.wikipedia.org/wiki/Category:Probability%20theory)
> - [Types of functions](https://en.wikipedia.org/wiki/Category:Types%20of%20functions)
