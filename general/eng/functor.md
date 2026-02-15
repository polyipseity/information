---
aliases:
  - functor
  - functor (category theory)
  - functorialities
  - functoriality
  - functors
  - functors (category theory)
tags:
  - flashcard/active/general/eng/functor
  - language/in/English
---

# functor

- This article is about {@{the mathematical concept}@}. For other uses, see [Functor \(disambiguation\)](functor%20(disambiguation).md).
- {@{"Functoriality"}@} redirects here. For {@{the Langlands functoriality conjecture in number theory}@}, see {@{[Langlands program § Functoriality](Langlands%20program.md#functoriality)}@}. <!--SR:!2026-02-23,322,346!2030-02-02,1456,366!2026-04-09,360,357!2026-04-10,361,357-->

In {@{[mathematics](mathematics.md), specifically [category theory](category%20theory.md)}@}, {@{a __functor__}@} is {@{a [mapping](map%20(mathematics).md) between [categories](category%20(mathematics).md)}@}. Functors were first {@{considered in [algebraic topology](algebraic%20topology.md)}@}, where {@{algebraic objects \(such as the [fundamental group](fundamental%20group.md)\) are associated to [topological spaces](topological%20space.md)}@}, and {@{maps between these algebraic objects are associated to [continuous](continuous%20function.md) maps between spaces}@}. Nowadays, functors are {@{used throughout modern mathematics to relate various categories}@}. Thus, functors are {@{important in all areas within mathematics to which [category theory](category%20theory.md) is applied}@}. <!--SR:!2026-03-19,344,357!2026-04-09,360,357!2026-04-03,355,357!2026-04-13,364,357!2026-03-11,337,357!2030-02-08,1461,366!2026-03-19,343,357!2026-02-26,323,346-->

{@{The words _category_ and _functor_}@} were {@{borrowed by mathematicians from the philosophers [Aristotle](Aristotle.md) and [Rudolf Carnap](Rudolf%20Carnap.md), respectively}@}.<sup>[\[1\]](#^ref-1)</sup> The latter used {@{_functor_ in a [linguistic](linguistics.md) context;<sup>[\[2\]](#^ref-2)</sup> see [function word](function%20word.md)}@}. <!--SR:!2030-02-10,1462,366!2026-08-25,440,317!2030-04-12,1513,366-->

## definition

<!-- | ![](../../archives/Wikimedia%20Commons/Edit-clear.svg) | This article __may be too technical for most readers to understand__. Please [help improve it](https://en.wikipedia.org/w/index.php?title=Functor&action=edit) to [make it understandable to non-experts](https://en.wikipedia.org/wiki/Wikipedia:Make%20technical%20articles%20understandable), without removing the technical details. _\(November 2023\)__ \([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ | -->

> {@{![A category with objects X, Y, Z and morphisms f, g, g ∘ f](../../archives/Wikimedia%20Commons/Commutative%20diagram%20for%20morphism.svg)}@}
>
> {@{A category with objects X, Y, Z and morphisms f, g, g ∘ f}@} <!--SR:!2029-09-24,1340,350!2026-03-22,345,357-->

<!-- markdownlint MD028 -->

> {@{![Functor $F$ must preserve the composition of morphisms $g$ and $f$](../../archives/Wikimedia%20Commons/Commutative%20diagram%20of%20a%20functor.svg)}@}
>
> {@{Functor $F$ must preserve the composition of morphisms $g$ and $f$}@} <!--SR:!2026-04-04,356,357!2026-04-04,356,357-->

Let {@{_C_ and _D_ be [categories](category%20(mathematics).md)}@}. {@{A __functor__ _F_ from _C_ to _D_}@} is a mapping that<sup>[\[3\]](#^ref-3)</sup> <!--SR:!2026-02-21,319,346!2026-03-16,341,357-->

- (annotation: object) ::@:: associates each [object](mathematical%20object.md) $X$ in _C_ to an object $F(X)$ in _D_, <!--SR:!2029-09-19,1335,350!2026-04-03,355,357-->
- (annotation: morphism) ::@:: associates each [morphism](morphism.md) $f\colon X\to Y$ in _C_ to a morphism $F(f)\colon F(X)\to F(Y)$ in _D_ such that the following two conditions hold: (annotation: identity, composition) <!--SR:!2026-02-20,319,346!2027-02-17,565,310-->
  - (annotation: identity) ::@:: $F(\mathrm {id} _{X})=\mathrm {id} _{F(X)}\,\!$ for every object $X$ in _C_, <!--SR:!2029-09-16,1332,350!2026-04-07,359,357-->
  - (annotation: composition) ::@:: $F(g\circ f)=F(g)\circ F(f)$ for all morphisms $f\colon X\to Y\,\!$ and $g\colon Y\to Z$ in _C_. <!--SR:!2026-03-18,342,357!2029-09-17,1333,350-->
- (annotation: functor, notes) ::@:: (annotation: The object and morphism mappings are _not_ required to be injective or surjective. For example, see [constant functor](constant%20functor.md#examples), which maps every object to the same object and every morphism to the identity morphism of that object.) <!--SR:!2026-05-30,403,367!2026-05-26,399,367-->

That is, functors must {@{preserve [identity morphisms](morphism.md#definition) and [composition](function%20composition.md) of morphisms}@}. <!--SR:!2026-04-03,354,357-->

### covariance and contravariance

- See also: [Covariance and contravariance \(computer science\)](covariance%20and%20contravariance%20(computer%20science).md)

There are {@{many constructions in mathematics that would be functors}@} but for the fact that they {@{"turn morphisms around" and "reverse composition"}@}. We then define {@{a __contravariant functor__ _F_ from _C_ to _D_}@} as a mapping that <!--SR:!2030-04-03,1506,366!2028-08-21,1008,346!2026-03-25,348,357-->

- (annotation: contravariant, object) ::@:: associates each object $X$ in _C_ with an object $F(X)$ in _D_, <!--SR:!2030-03-05,1482,366!2028-08-14,1014,346-->
- (annotation: contravariant, morphism) ::@:: associates each morphism $f\colon X\to Y$ in _C_ with a morphism $F(f)\colon F(Y)\to F(X)$ in _D_ such that the following two conditions hold: (annotation: identity, composition) <!--SR:!2026-04-13,364,357!2026-03-22,346,357-->
  - (annotation: contravariant, identity) ::@:: $F(\mathrm {id} _{X})=\mathrm {id} _{F(X)}\,\!$ for every object $X$ in _C_, <!--SR:!2026-03-14,340,357!2030-04-09,1511,366-->
  - (annotation: contravariant, morphism) ::@:: $F(g\circ f)=F(f)\circ F(g)$ for all morphisms $f\colon X\to Y$ and $g\colon Y\to Z$ in _C_. <!--SR:!2026-04-06,357,357!2029-09-26,1342,350-->

Variance of functor ::@:: \(composite\)<sup>[\[4\]](#^ref-4)</sup> <!--SR:!2029-09-29,1345,350!2029-09-27,1343,350-->

- The composite of two functors of the same variance: ::@:: (annotation: composite is covariant) <!--SR:!2026-02-25,323,346!2026-03-13,339,357-->
  - $\mathrm {Covariant} \circ \mathrm {Covariant} \to \mathrm {Covariant}$
  - $\mathrm {Contravariant} \circ \mathrm {Contravariant} \to \mathrm {Covariant}$
- The composite of two functors of opposite variance: ::@:: (annotation: composite is contravariant) <!--SR:!2026-03-06,332,357!2026-03-30,352,357-->
  - $\mathrm {Covariant} \circ \mathrm {Contravariant} \to \mathrm {Contravariant}$
  - $\mathrm {Contravariant} \circ \mathrm {Covariant} \to \mathrm {Contravariant}$

Note that contravariant functors {@{reverse the direction of composition}@}. <!--SR:!2029-09-26,1342,350-->

Ordinary functors are also called {@{__covariant functors__ in order to distinguish them from contravariant ones}@}. Note that one can also define a contravariant functor as {@{a _covariant_ functor on the [opposite category](opposite%20category.md) $C^{\mathrm {op} }$}@}.<sup>[\[5\]](#^ref-5)</sup> Some authors {@{prefer to write all expressions covariantly}@}. That is, instead of {@{saying $F\colon C\to D$ is a contravariant functor}@}, they {@{simply write $F\colon C^{\mathrm {op} }\to D$ \(or sometimes $F\colon C\to D^{\mathrm {op} }$\) and call it a functor}@}. <!--SR:!2026-04-12,363,357!2029-09-29,1345,350!2026-03-26,349,357!2026-03-17,341,357!2026-03-27,350,357-->

{@{Contravariant functors}@} are also occasionally called {@{_cofunctors_}@}.<sup>[\[6\]](#^ref-6)</sup> <!--SR:!2030-03-14,1489,366!2026-04-04,355,357-->

There is a convention which refers to {@{"vectors"—i.e., [vector fields](vector%20field.md), elements of the space of sections $\Gamma (TM)$ of a [tangent bundle](tangent%20bundle.md) $TM$—as "contravariant"}@} and to {@{"covectors"—i.e., [1-forms](1-forms.md), elements of the space of sections $\Gamma {\mathord {\left(T^{*}M\right)} }$ of a [cotangent bundle](cotangent%20bundle.md) $T^{*}M$—as "covariant"}@}. This terminology {@{originates in physics}@}, and its rationale has to do with {@{the position of the indices \("upstairs" and "downstairs"\) in [expressions](Einstein%20summation.md)}@} such as {@{${x'}^{\,i}=\Lambda _{j}^{i}x^{j}$ for $\mathbf {x} '={\boldsymbol {\Lambda } }\mathbf {x}$ or $\omega '_{i}=\Lambda _{i}^{j}\omega _{j}$ for ${\boldsymbol {\omega } }'={\boldsymbol {\omega } }{\boldsymbol {\Lambda } }^{\textsf {T} }$}@}. (annotation: The top index {@{refers to the row index while the bottom index refers to the column index}@}. The notation omits {@{the summation sign over $j$ on the right hand side}@}.) In this formalism it is observed that {@{the coordinate transformation symbol $\Lambda _{i}^{j}$ \(representing the matrix ${\boldsymbol {\Lambda } }^{\textsf {T} }$\)}@} {@{acts on the "covector coordinates" "in the same way" as on the basis vectors: $\mathbf {e} _{i}=\Lambda _{i}^{j}\mathbf {e} _{j}$}@}—whereas it {@{acts "in the opposite way" on the "vector coordinates" \(but "in the same way" as on the basis covectors: $\mathbf {e} ^{i}=\Lambda _{j}^{i}\mathbf {e} ^{j}$\)}@}. This terminology is {@{contrary to the one used in category theory}@} because {@{it is the covectors that have _pullbacks_ in general and are thus _contravariant_}@}, whereas {@{vectors in general are _covariant_ since they can be _pushed forward_}@}. See also {@{[Covariance and contravariance of vectors](covariance%20and%20contravariance%20of%20vectors.md)}@}. <!--SR:!2026-04-17,337,306!2026-04-25,317,297!2026-11-20,517,326!2026-04-10,361,357!2027-01-22,466,266!2029-09-25,1341,350!2026-03-20,344,357!2026-02-27,296,290!2027-10-03,703,286!2028-01-18,779,290!2026-03-25,348,357!2027-03-27,556,317!2026-05-11,357,306!2026-04-07,359,357-->

### opposite functor

{@{Every functor $F\colon C\to D$}@} induces {@{the __opposite functor__ $F^{\mathrm {op} }\colon C^{\mathrm {op} }\to D^{\mathrm {op} }$}@}, where {@{$C^{\mathrm {op} }$ and $D^{\mathrm {op} }$ are the [opposite categories](opposite%20category.md) to $C$ and $D$}@}.<sup>[\[7\]](#^ref-7)</sup> By definition, {@{$F^{\mathrm {op} }$ maps objects and morphisms in the identical way as does $F$}@}. Since {@{$C^{\mathrm {op} }$ does not coincide with $C$ as a category, and similarly for $D$}@}, {@{$F^{\mathrm {op} }$ is distinguished from $F$}@}. For example, when {@{composing $F\colon C_{0}\to C_{1}$ with $G\colon C_{1}^{\mathrm {op} }\to C_{2}$}@}, one should {@{use either $G\circ F^{\mathrm {op} }$ or $G^{\mathrm {op} }\circ F$}@}. Note that, following {@{the property of [opposite category](opposite%20category.md), $\left(F^{\mathrm {op} }\right)^{\mathrm {op} }=F$}@}. <!--SR:!2026-02-26,324,346!2030-04-10,1511,366!2026-04-10,361,357!2030-03-28,1501,366!2026-04-06,358,357!2026-04-05,357,357!2026-04-10,361,357!2026-03-19,343,357!2026-02-25,324,346-->

### bifunctors and multifunctors

{@{A __bifunctor__ \(also known as a __binary functor__\)}@} is {@{a functor whose domain is a [product category](product%20category.md)}@}. For example, {@{the [Hom functor](hom%20functor.md) is of the type _C<sup>op</sup>_ × _C_ → __Set__}@}. It can be seen as {@{a functor in _two_ arguments; it is contravariant in one argument, covariant in the other}@}. <!--SR:!2026-04-06,358,357!2026-03-16,341,357!2026-02-26,325,357!2026-04-11,362,357-->

{@{A __multifunctor__}@} is {@{a generalization of the functor concept to _n_ variables}@}. So, for example, {@{a bifunctor is a multifunctor with _n_ = 2}@}. <!--SR:!2029-09-20,1336,350!2026-04-09,360,357!2026-04-05,357,357-->

## properties

{@{Two important consequences}@} of the functor [axioms](axiom.md) are: <!--SR:!2026-02-21,320,346-->

- (annotation: commutative diagram) ::@:: _F_ transforms each [commutative diagram](commutative%20diagram.md) in _C_ into a commutative diagram in _D_; <!--SR:!2026-03-20,345,357!2026-04-02,355,357-->
- (annotation: isomorphism) ::@:: if _f_ is an [isomorphism](isomorphism.md) in _C_, then _F_\(_f_\) is an isomorphism in _D_. <!--SR:!2026-11-04,461,337!2029-09-26,1342,350-->

One can {@{compose functors}@}, i.e. if _F_ is a functor from _A_ to _B_ and {@{_G_ is a functor from _B_ to _C_ then one can form the composite functor _G_ ∘ _F_ from _A_ to _C_}@}. {@{Composition of functors}@} is {@{associative where defined}@}. {@{Identity of composition of functors}@} is {@{the identity functor}@}. This shows that {@{functors can be considered as morphisms in categories of categories}@}, for example in {@{the [category of small categories](category%20of%20small%20categories.md)}@}. <!--SR:!2026-03-23,346,357!2026-03-26,349,357!2030-03-30,1502,366!2026-04-11,362,357!2029-08-13,1306,350!2026-02-24,322,346!2026-03-12,338,357!2026-03-29,351,357-->

{@{A small category with a single object}@} is {@{the same thing as a [monoid](monoid.md)}@}: the morphisms of {@{a one-object category can be thought of as elements of the monoid}@}, and composition {@{in the category is thought of as the monoid operation}@}. {@{Functors between one-object categories}@} correspond to {@{monoid [homomorphisms](homomorphism.md)}@}. So in a sense, {@{functors between arbitrary categories}@} are {@{a kind of generalization of monoid homomorphisms to categories with more than one object}@}. <!--SR:!2026-04-08,360,357!2030-03-22,1496,366!2026-03-21,345,357!2026-02-23,321,346!2026-03-07,333,357!2028-12-07,1115,357!2026-02-21,320,346!2030-03-08,1484,366-->

## examples

__[Diagram](diagram%20(category%20theory).md)__ <p> ::@:: &emsp; For categories _C_ and _J_, a diagram of type _J_ (annotation: the categorical analogue of an indexed family in set theory) in _C_ is a covariant functor $D\colon J\to C$. <!--SR:!2027-03-01,591,337!2026-03-10,335,357-->

__[\(Category theoretical\) presheaf](presheaf%20(category%20theory).md)__ <p> ::@:: &emsp; For categories _C_ and _J_, a _J_-presheaf on _C_ is a contravariant (annotation: _not_ covariant) functor $D\colon C\to J$. <p> In the special case when J is __Set__, the category of sets and functions, _D_ is called a [presheaf](presheaf%20(category%20theory).md) on _C_. <!--SR:!2026-03-22,294,297!2028-04-09,894,330-->

__Presheaves \(over a topological space\)__

&emsp; If {@{_X_ is a [topological space](topological%20space.md)}@}, then {@{the [open sets](open%20set.md) in _X_ form a [partially ordered set](partially%20ordered%20set.md) Open\(_X_\) under inclusion}@}. Like {@{every partially ordered set}@}, {@{Open\(_X_\) forms a small category}@} by {@{adding a single arrow _U_ → _V_ if and only if $U\subseteq V$}@}. {@{Contravariant functors on (annotation: i.e. from) Open\(_X_\)}@} are called {@{_[presheaves](presheaf.md#presheaves)_ on _X_}@}. For instance, by {@{assigning to every open set _U_ the [associative algebra](associative%20algebra.md) of real-valued continuous functions on _U_}@}, one obtains {@{a presheaf of algebras on _X_}@}. <!--SR:!2029-09-25,1341,350!2026-03-24,347,357!2029-09-29,1345,350!2026-02-23,321,346!2030-03-27,1500,366!2029-01-17,1071,346!2026-03-27,350,357!2027-11-09,782,337!2029-06-16,1213,317-->

__Constant functor__ <p> ::@:: &emsp; The functor _C_ → _D_ which maps every object of _C_ to a fixed object _X_ in _D_ and every morphism in _C_ to the identity morphism on _X_. Such a functor is called a _constant_ or _selection_ functor. (annotation: note that functors are not required to be injective or surjective) <!--SR:!2026-03-28,350,357!2026-03-06,331,346-->

__Endofunctor__ <p> ::@:: &emsp; A functor that maps a category to that same category; e.g., [polynomial functor](polynomial%20functor.md). <!--SR:!2027-07-18,697,330!2027-04-24,638,330-->

__Identity functor__ <p> ::@:: &emsp; In category _C_, written 1<sub>_C_</sub> or id<sub>_C_</sub>, maps an object to itself and a morphism to itself. The identity functor is an endofunctor. <!--SR:!2029-09-28,1344,350!2026-04-11,362,357-->

__Diagonal functor__ <p> ::@:: &emsp; The [diagonal functor](diagonal%20functor.md) is defined as the functor from _D_ to the functor category _D_<sup>_C_</sup> which sends each object in _D_ to the constant functor at that object. <!--SR:!2026-02-28,326,346!2026-04-07,358,357-->

<!-- markdownlint-disable-next-line MD036 -->
__Limit functor__

&emsp; For {@{a fixed [index category](index%20category.md) _J_}@}, if {@{every functor _J_ → _C_ has a [limit](limit%20(category%20theory).md) \(for instance if _C_ is complete\)}@}, then {@{the limit functor _C_<sup>_J_</sup> → _C_ assigns to each functor its limit}@}. {@{The existence of this functor}@} can be {@{proved by realizing that it is the [right-adjoint](adjoint%20functors.md) to the [diagonal functor](diagonal%20functor.md)}@} and invoking {@{the [Freyd adjoint functor theorem](Freyd%20adjoint%20functor%20theorem.md)}@}. This requires {@{a suitable version of the [axiom of choice](axiom%20of%20choice.md)}@}. Similar remarks apply to {@{the colimit functor \(which assigns to every functor its colimit, and is covariant\)}@}. <!--SR:!2026-04-08,359,357!2029-09-29,1345,350!2026-04-13,364,357!2026-03-25,348,357!2026-12-13,480,270!2026-09-27,442,317!2026-04-12,363,357!2028-03-19,830,337-->

<!-- markdownlint-disable-next-line MD036 -->
__Power sets functor__

&emsp; {@{The power set functor _P_ : __Set__ → __Set__}@} maps {@{each set to its [power set](power%20set.md)}@} and {@{each function $f\colon X\to Y$ to the map which sends $U\in {\mathcal {P} }(X)$ to its image $f(U)\in {\mathcal {P} }(Y)$}@}. One can also consider {@{the __contravariant power set functor__}@} which {@{sends $f\colon X\to Y$ to the map which sends $V\subseteq Y$ to its [inverse image](inverse%20image.md#inverse%20image) $f^{-1}(V)\subseteq X$}@}. <!--SR:!2030-02-11,1463,366!2026-03-16,341,357!2026-03-21,345,357!2026-09-29,436,317!2029-09-25,1341,350-->

&emsp; For example, if {@{$X=\{0,1\}$ then $F(X)={\mathcal {P} }(X)=\{\{\},\{0\},\{1\},X\}$}@}. Suppose {@{$f(0)=\{\}$ and $f(1)=X$}@}. Then $F(f)$ is {@{the function which sends any subset $U$ of $X$ to its image $f(U)$}@}, which in this case means {@{$\{\}\mapsto f(\{\})=\{\}$, where $\mapsto$ denotes the mapping under $F(f)$}@}, so this could also be {@{written as $(F(f))(\{\})=\{\}$}@}. For the other values, {@{$\{0\}\mapsto f(\{0\})=\{f(0)\}=\{\{\}\},\ {}$ $\{1\}\mapsto f(\{1\})=\{f(1)\}=\{X\},\ {}$ $\{0,1\}\mapsto f(\{0,1\})=\{f(0),f(1)\}=\{\{\},X\}$}@}. Note that $f(\{0,1\})$ consequently {@{generates the [trivial topology](trivial%20topology.md) on $X$}@}. Also note that {@{although the function $f$ in this example mapped to the power set of $X$}@}, that {@{need not be the case in general}@}. <!--SR:!2026-02-24,323,346!2026-04-05,356,357!2026-02-27,325,346!2026-03-20,344,357!2026-04-11,362,357!2029-01-22,1074,346!2030-03-04,1481,366!2026-03-16,341,357!2026-02-22,321,346-->

__Dual vector space__ <p> ::@:: &emsp; The map which assigns to every [vector space](vector%20space.md) its [dual space](dual%20space.md) and to every [linear map](linear%20operator.md) its dual or transpose is a contravariant (annotation: _not_ covariant) functor from the category of all vector spaces over a fixed [field](field%20(mathematics).md) to itself. <!--SR:!2028-06-21,985,357!2028-02-13,801,290-->

<!-- markdownlint-disable-next-line MD036 -->
__Fundamental group__

&emsp; Consider {@{the category of [pointed topological spaces](pointed%20topological%20space.md), i.e. topological spaces with distinguished points}@}. The objects are {@{pairs \(_X_, _x_<sub>0</sub>\), where _X_ is a topological space and _x_<sub>0</sub> is a point in _X_}@}. {@{A morphism from \(_X_, _x_<sub>0</sub>\) to \(_Y_, _y_<sub>0</sub>\)}@} is given by {@{a [continuous](continuous%20function%20(topology).md#continuous%20functions%20between%20topological%20spaces) map _f_ : _X_ → _Y_ with _f_\(_x_<sub>0</sub>\) = _y_<sub>0</sub>}@}. <!--SR:!2028-02-15,886,357!2029-09-29,1345,350!2026-04-13,364,357!2026-03-25,348,357-->

&emsp; To {@{every topological space _X_ with distinguished point _x_<sub>0</sub>}@}, one can define {@{the [fundamental group](fundamental%20group.md) based at _x_<sub>0</sub>, denoted π<sub>1</sub>\(_X_, _x_<sub>0</sub>\)}@}. This is {@{the [group](group%20(mathematics).md) of [homotopy](homotopy.md) classes of loops based at _x_<sub>0</sub>}@}, with {@{the group operation of concatenation}@}. If {@{_f_ : _X_ → _Y_ is a morphism of [pointed spaces](pointed%20space.md)}@}, then {@{every loop in _X_ with base point _x_<sub>0</sub> can be composed with _f_ to yield a loop in _Y_ with base point _y_<sub>0</sub>}@}. This operation is {@{compatible with the homotopy [equivalence relation](equivalence%20relation.md) and the composition of loops}@}, and we get {@{a [group homomorphism](group%20homomorphism.md) from π\(_X_, _x_<sub>0</sub>\) to π\(_Y_, _y_<sub>0</sub>\)}@}. We thus obtain {@{a functor from the category of pointed topological spaces to the [category of groups](category%20of%20groups.md)}@}. <!--SR:!2030-03-24,1498,366!2026-04-06,357,357!2029-09-21,1337,350!2028-05-03,913,330!2026-02-20,319,346!2026-03-31,353,357!2028-01-08,789,337!2028-07-29,1003,346!2029-01-01,1058,346-->

&emsp; In {@{the category of topological spaces \(without distinguished point\)}@}, one considers {@{homotopy classes of generic curves}@}, but {@{they cannot be composed unless they share an endpoint}@}. Thus one has {@{the __fundamental [groupoid](groupoid.md)__ instead of the fundamental group}@}, and {@{this construction is functorial}@}. <!--SR:!2026-02-22,320,346!2028-01-12,839,330!2030-02-19,1470,366!2030-02-01,1455,366!2026-04-12,363,357-->

<!-- markdownlint-disable-next-line MD036 -->
__Algebra of continuous functions__

&emsp; {@{A contravariant (annotation: _not_ covariant) functor}@} from {@{the category of [topological spaces](topology.md) \(with continuous maps as morphisms\) to the category of real [associative algebras](associative%20algebra.md)}@} is given by {@{assigning to every topological space _X_ the algebra C\(_X_\) of all real-valued continuous functions on that space}@}. {@{Every continuous map _f_ : _X_ → _Y_}@} induces {@{an [algebra homomorphism](algebra%20homomorphism.md#algebra%20homomorphisms) C\(_f_\) : C\(_Y_\) → C\(_X_\)}@} by {@{the rule C\(_f_\)\(_φ_\) = _φ_ ∘ _f_ for every _φ_ in C\(_Y_\)}@}. <!--SR:!2026-03-05,331,357!2026-06-29,373,306!2027-10-23,724,326!2026-03-10,337,357!2029-01-27,1142,357!2026-05-10,356,306-->

<!-- markdownlint-disable-next-line MD036 -->
__Tangent and cotangent bundles__

&emsp; The map which {@{sends every [differentiable manifold](differentiable%20manifold.md) to its [tangent bundle](tangent%20bundle.md) and every [smooth map](smooth%20map.md) to its [derivative](derivative.md)}@} is {@{a covariant functor from the category of differentiable manifolds to the category of [vector bundles](vector%20bundle.md)}@}. <!--SR:!2026-09-10,237,206!2027-08-28,673,286-->

&emsp; {@{Doing this constructions pointwise}@} gives {@{the [tangent space](tangent%20space.md)}@}, {@{a covariant functor from the category of pointed differentiable manifolds to the category of real vector spaces}@}. Likewise, {@{[cotangent space](cotangent%20space.md)}@} is {@{a contravariant functor, essentially the composition of the tangent space with the [dual space](#dual%20vector%20space) above}@}. <!--SR:!2027-03-15,610,337!2026-07-03,399,317!2027-06-06,490,230!2027-09-04,751,346!2026-09-13,407,290-->

<!-- markdownlint-disable-next-line MD036 -->
__Group actions/representations__

&emsp; {@{Every [group](group%20(mathematics).md) _G_}@} can be {@{considered as a category with a single object whose morphisms are the elements of _G_}@}. {@{A functor from _G_ to __Set__}@} is then {@{nothing but a [group action](group%20action%20(mathematics).md) of _G_ on a particular set, i.e. a _G_-set}@}. Likewise, {@{a functor from _G_ to the [category of vector spaces](category%20of%20vector%20spaces.md), __Vect__<sub>_K_</sub>}@}, is {@{a [linear representation](linear%20representation.md) of _G_}@}. In general, {@{a functor _G_ → _C_}@} can be considered as {@{an "action" of _G_ on an object in the category _C_}@}. If {@{_C_ is a group}@}, then {@{this action is a group homomorphism}@}. <!--SR:!2026-03-29,351,357!2028-08-19,947,330!2026-04-01,354,357!2026-03-22,346,357!2030-03-18,1493,366!2026-02-27,324,346!2029-09-24,1340,350!2027-02-28,596,337!2026-02-25,322,346!2026-03-15,341,357-->

__Lie algebras__ <p> ::@:: &emsp; Assigning to every real \(complex\) [Lie group](Lie%20group.md) its real \(complex\) [Lie algebra](Lie%20algebra.md) defines a functor. <!--SR:!2027-02-04,553,310!2026-11-03,469,317-->

__Tensor products__ <p> ::@:: &emsp; If _C_ denotes the category of vector spaces over a fixed field, with [linear maps](linear%20operator.md) as morphisms, then the [tensor product](tensor%20product.md) $V\otimes W$ defines a functor _C_ × _C_ → _C_ which is covariant in both arguments.<sup>[\[8\]](#^ref-8)</sup> <!--SR:!2026-04-07,358,357!2027-02-14,563,310-->

<!-- markdownlint-disable-next-line MD036 -->
__Forgetful functors__

&emsp; {@{The functor _U_ : __Grp__ → __Set__}@} which {@{maps a [group](group%20(mathematics).md) to its underlying set and a [group homomorphism](group%20homomorphism.md) to its underlying function of sets is a functor}@}.<sup>[\[9\]](#^ref-9)</sup> {@{Functors like these, which "forget" some structure}@}, are termed {@{_[forgetful functors](forgetful%20functor.md)_}@}. Another example is {@{the functor __Rng__ → __Ab__ which maps a [ring](ring%20(algebra).md) to its underlying additive [abelian group](abelian%20group.md)}@}. {@{Morphisms in __Rng__ \([ring homomorphisms](ring%20homomorphism.md)\)}@} become {@{morphisms in __Ab__ \(abelian group homomorphisms\)}@}. <!--SR:!2026-03-28,350,357!2027-10-28,774,337!2029-09-29,1345,350!2026-04-02,355,357!2026-06-20,367,306!2026-04-05,357,357!2026-04-12,363,357-->

<!-- markdownlint-disable-next-line MD036 -->
__Free functors__

&emsp; {@{Going in the opposite direction of forgetful functors}@} are {@{free functors}@}. {@{The free functor _F_ : __Set__ → __Grp__}@} {@{sends every set _X_ to the [free group](free%20group.md) generated by _X_}@}. Functions get {@{mapped to group homomorphisms between free groups}@}. Free constructions {@{exist for many categories based on structured sets. See [free object](free%20object.md)}@}. <!--SR:!2030-02-18,1469,366!2026-03-26,349,357!2029-09-28,1344,350!2026-03-03,330,357!2029-09-29,1345,350!2026-04-08,307,297-->

<!-- markdownlint-disable-next-line MD036 -->
__Homomorphism groups__

&emsp; {@{To every pair _A_, _B_ of [abelian groups](group%20(mathematics).md)}@} one can {@{assign the abelian group Hom\(_A_, _B_\) consisting of all [group homomorphisms](group%20homomorphism.md) from _A_ to _B_}@}. This is {@{a functor which is contravariant in the first and covariant in the second argument, i.e. it is a functor __Ab__<sup>op</sup> × __Ab__ → __Ab__ \(where __Ab__ denotes the [category of abelian groups](category%20of%20abelian%20groups.md) with group homomorphisms\)}@}. If {@{_f_ : _A_<sub>1</sub> → _A_<sub>2</sub> and _g_ : _B_<sub>1</sub> → _B_<sub>2</sub> are morphisms in __Ab__}@}, then {@{the group homomorphism Hom\(_f_, _g_\): Hom\(_A_<sub>2</sub>, _B_<sub>1</sub>\) → Hom\(_A_<sub>1</sub>, _B_<sub>2</sub>\)}@} is given by {@{_φ_ ↦ _g_ ∘ _φ_ ∘ _f_. See [Hom functor](hom%20functor.md)}@}. <!--SR:!2026-03-27,350,357!2026-03-21,345,357!2027-05-14,647,337!2026-03-30,352,357!2029-09-22,1338,350!2026-07-16,409,317-->

<!-- markdownlint-disable-next-line MD036 -->
__Representable functors__

&emsp; We can {@{generalize the previous example to any category _C_}@}. To {@{every pair _X_, _Y_ of objects in _C_}@} one can {@{assign the set Hom\(_X_, _Y_\) of morphisms from _X_ to _Y_}@}. This defines {@{a functor to __Set__ which is contravariant in the first argument and covariant in the second, i.e. it is a functor _C_<sup>op</sup> × _C_ → __Set__}@}. If {@{_f_ : _X_<sub>1</sub> → _X_<sub>2</sub> and _g_ : _Y_<sub>1</sub> → _Y_<sub>2</sub> are morphisms in _C_}@}, then {@{the map Hom\(_f_, _g_\) : Hom\(_X_<sub>2</sub>, _Y_<sub>1</sub>\) → Hom\(_X_<sub>1</sub>, _Y_<sub>2</sub>\)}@} is given by {@{_φ_ ↦ _g_ ∘ _φ_ ∘ _f_}@}. <!--SR:!2026-03-16,341,357!2026-04-01,354,357!2026-04-08,360,357!2029-09-27,1343,350!2029-09-27,1343,350!2026-04-04,356,357!2026-03-01,326,346-->

&emsp; Functors like these are called {@{[representable functors](representable%20functor.md)}@}. {@{An important goal in many settings}@} is to {@{determine whether a given functor is representable}@}. <!--SR:!2026-04-09,360,357!2030-04-08,1510,366!2026-03-16,341,357-->

## relation to other categorical concepts

Let {@{_C_ and _D_ be categories}@}. {@{The collection of all functors from _C_ to _D_}@} forms {@{the objects of a category: the [functor category](functor%20category.md)}@}. {@{Morphisms in this category}@} are {@{[natural transformations](natural%20transformation.md) between functors}@}. <!--SR:!2030-03-03,1481,366!2026-03-18,343,357!2026-02-20,318,346!2029-09-18,1334,350!2026-04-08,359,357-->

Functors are often {@{defined by [universal properties](universal%20property.md)}@}; examples are {@{the [tensor product](tensor%20product.md), the [direct sum](direct%20sum%20of%20modules.md) and [direct product](direct%20product.md) of groups or vector spaces}@}, {@{construction of free groups and modules, [direct](direct%20limit.md) and [inverse](inverse%20limit.md) limits}@}. {@{The concepts of [limit and colimit](limit%20(category%20theory).md)}@} {@{generalize several of the above}@}. <!--SR:!2026-03-31,353,357!2027-11-12,784,337!2026-07-28,419,317!2026-03-18,342,357!2026-02-28,325,346-->

{@{Universal constructions}@} often {@{give rise to pairs of [adjoint functors](adjoint%20functors.md)}@}. <!--SR:!2026-04-01,354,357!2026-03-26,349,357-->

## computer implementations

- Main article: [Functor \(functional programming\)](functor%20(functional%20programming).md)

Functors sometimes {@{appear in [functional programming](functional%20programming.md)}@}. For instance, {@{the programming language [Haskell](Haskell%20(programming%20language).md)}@} has {@{a [class](type%20class.md) `Functor`}@} where {@{[`fmap`](map%20(higher-order%20function).md#generalization) is a [polytypic function](polytypic%20function.md#polytypism)}@} used to {@{map [functions](function%20(computer%20programming).md) \(_morphisms_ on _Hask_, the category of Haskell types\)<sup>[\[10\]](#^ref-10)</sup> between existing types to functions between some new types}@}.<sup>[\[11\]](#^ref-11)</sup> <!--SR:!2026-03-22,346,357!2026-02-22,321,346!2029-09-23,1339,350!2027-09-05,732,337!2026-04-02,355,357-->

## see also

> __![icon](../../archives/Wikimedia%20Commons/Nuvola%20apps%20edu%20mathematics%20blue-p.svg) [Mathematics portal](https://en.wikipedia.org/wiki/Portal:Mathematics)__

- [Anafunctor](anafunctor.md)
- [Profunctor](profunctor.md)
- [Functor category](functor%20category.md)
- [Kan extension](Kan%20extension.md)
- [Pseudofunctor](pseudofunctor.md)

## notes

1. <a id="CITEREFMac Lane1971"></a> [Mac Lane, Saunders](Saunders%20Mac%20Lane.md) \(1971\), _Categories for the Working Mathematician_, New York: Springer-Verlag, p. 30, [ISBN](ISBN%20(identifier).md) [978-3-540-90035-1](https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-90035-1) <a id="^ref-1"></a>^ref-1
2. [Carnap, Rudolf](Rudolf%20Carnap.md) \(1937\). _The Logical Syntax of Language_, Routledge & Kegan, pp. 13–14. <a id="^ref-2"></a>^ref-2
3. [Jacobson \(2009\)](#CITEREFJacobson2009), p. 19, def. 1.2. <a id="^ref-3"></a>^ref-3
4. [Simmons \(2011\)](#CITEREFSimmons2011), Exercise 3.1.4. <a id="^ref-4"></a>^ref-4
5. [Jacobson \(2009\)](#CITEREFJacobson2009), pp. 19–20. <a id="^ref-5"></a>^ref-5
6. <a id="CITEREFPopescuPopescu1979"></a> Popescu, Nicolae; Popescu, Liliana \(1979\). [_Theory of categories_](https://books.google.com/books?id=YnHwCAAAQBAJ&q=cofunctor+covariant&pg=PA12). Dordrecht: Springer. p. 12. [ISBN](ISBN%20(identifier).md) [9789400995505](https://en.wikipedia.org/wiki/Special:BookSources/9789400995505). Retrieved 23 April 2016. <a id="^ref-6"></a>^ref-6
7. <a id="CITEREFMac LaneMoerdijk1992"></a> [Mac Lane, Saunders](Saunders%20Mac%20Lane.md); [Moerdijk, Ieke](Ieke%20Moerdijk.md) \(1992\), _Sheaves in geometry and logic: a first introduction to topos theory_, Springer, [ISBN](ISBN%20(identifier).md) [978-0-387-97710-2](https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-97710-2) <a id="^ref-7"></a>^ref-7
8. <a id="CITEREFHazewinkelGubareniGubareniKirichenko2004"></a> [Hazewinkel, Michiel](Michiel%20Hazewinkel.md); [Gubareni, Nadezhda Mikhaĭlovna](Nadezhda%20Mikhaĭlovna.md); [Gubareni, Nadiya](Nadiya%20Gubareni.md); [Kirichenko, Vladimir V.](Vladimir%20V.%20Kirichenko.md) \(2004\), _Algebras, rings and modules_, Springer, [ISBN](ISBN%20(identifier).md) [978-1-4020-2690-4](https://en.wikipedia.org/wiki/Special:BookSources/978-1-4020-2690-4) <a id="^ref-8"></a>^ref-8
9. [Jacobson \(2009\)](#CITEREFJacobson2009), p. 20, ex. 2. <a id="^ref-9"></a>^ref-9
10. It's {@{not entirely clear that Haskell datatypes truly form a category}@}. See [https://wiki.haskell.org/Hask](https://wiki.haskell.org/Hask) for more details. <a id="^ref-10"></a>^ref-10
11. See [https://wiki.haskell.org/Category\_theory/Functor\#Functors\_in\_Haskell](https://wiki.haskell.org/Category_theory/Functor#Functors_in_Haskell) for more information. <a id="^ref-11"></a>^ref-11 <!--SR:!2026-05-22,396,367-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/functor) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- <a id="CITEREFJacobson2009"></a> [Jacobson, Nathan](Nathan%20Jacobson.md) \(2009\), _Basic algebra_, vol. 2 \(2nd ed.\), Dover, [ISBN](ISBN%20(identifier).md) [978-0-486-47187-7](https://en.wikipedia.org/wiki/Special:BookSources/978-0-486-47187-7).
- <a id="CITEREFSimmons2011"></a> Simmons, Harold \(2011\), "Functors and natural transformations", [_An Introduction to Category Theory_](https://books.google.com/books?id=VOCQUC_uiWgC&pg=PA74), pp. 72–107, [doi](doi%20(identifier).md):[10.1017/CBO9780511863226.004](https://doi.org/10.1017%2FCBO9780511863226.004), [ISBN](ISBN%20(identifier).md) [978-1-107-01087-1](https://en.wikipedia.org/wiki/Special:BookSources/978-1-107-01087-1)

## external links

> ![Wiktionary logo](../../archives/Wikimedia%20Commons/Wiktionary-logo-en-v2.svg) Look up ___[functor](https://en.wiktionary.org/wiki/functor)___ in Wiktionary, the free dictionary.

- ["Functor"](https://www.encyclopediaofmath.org/index.php?title=Functor), _[Encyclopedia of Mathematics](Encyclopedia%20of%20Mathematics.md)_, [EMS Press](European%20Mathematical%20Society.md), 2001 \[1994\]
- see [functor](https://ncatlab.org/nlab/show/functor) at the [_n_<!-- markdown separator -->Lab](nLab.md) and the variations discussed and linked to there.
- [André Joyal](André%20Joyal.md), [CatLab](http://ncatlab.org/nlab), a wiki project dedicated to the exposition of categorical mathematics
- <a id="CITEREFHillman2001"></a> Hillman, Chris \(2001\). ["A Categorical Primer"](https://web.archive.org/web/19970503051012/http://www.math.washington.edu:80/~hillman/PUB/categorical.ps). [CiteSeerX](CiteSeerX%20(identifier).md) [10.1.1.24.3264](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.24.3264). Archived from [the original](http://www.math.washington.edu/~hillman/PUB/categorical.ps) on 1997-05-03.
- J. Adamek, H. Herrlich, G. Stecker, [Abstract and Concrete Categories-The Joy of Cats](http://katmat.math.uni-bremen.de/acc/acc.pdf) [Archived](https://web.archive.org/web/20150421081851/http://katmat.math.uni-bremen.de/acc/acc.pdf) 2015-04-21 at the [Wayback Machine](Wayback%20Machine.md)
- [Stanford Encyclopedia of Philosophy](Stanford%20Encyclopedia%20of%20Philosophy.md): "[Category Theory](http://plato.stanford.edu/entries/category-theory/)" — by Jean-Pierre Marquis. Extensive bibliography.
- [List of academic conferences on category theory](http://www.mta.ca/~cat-dist/)
- Baez, John, 1996,"[The Tale of _n_-categories.](http://math.ucr.edu/home/baez/week73.html)" An informal introduction to higher order categories.
- [WildCats](http://wildcatsformma.wordpress.com/) is a [category theory](category%20theory.md) package for [Mathematica](mathematica.md). Manipulation and visualization of objects, [morphisms](morphism.md), categories, functors, [natural transformations](natural%20transformation.md), [universal properties](universal%20properties.md).
- [The catsters](https://www.youtube.com/user/TheCatsters), a YouTube channel about category theory.
- [Video archive](http://categorieslogicphysics.wikidot.com/events) of recorded talks relevant to categories, logic and the foundations of physics.
- [Interactive Web page](https://web.archive.org/web/20080916162345/http://www.j-paine.org/cgi-bin/webcats/webcats.php) which generates examples of categorical constructions in the category of finite sets.

> <!-- hide <p> - [v](https://en.wikipedia.org/wiki/Template:Category%20theory) <br/> - [t](https://en.wikipedia.org/wiki/Template%20talk:Category%20theory) <br/> - [e](https://en.wikipedia.org/wiki/Special:EditPage/Template%3ACategory%20theory) <p>  <p>  <br/> -->
> __[Category theory](category%20theory.md)__
>
> | Key concepts                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
> | ----------------------------------------------------------:| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | __Key concepts__                                           | - [Category](category%20(mathematics).md)  <br/>     - [Abelian](abelian%20category.md) <br/>     - [Additive](additive%20category.md) <br/>     - [Concrete](concrete%20category.md) <br/>     - [Pre-abelian](pre-abelian%20category.md) <br/>     - [Preadditive](preadditive%20category.md) <br/>     - [Bicategory](bicategory.md) <p>  <p> - [Adjoint functors](adjoint%20functors.md) <br/> - [CCC](Cartesian%20closed%20category.md) <br/> - [Commutative diagram](commutative%20diagram.md) <br/> - [End](end%20(category%20theory).md) <br/> - [Exponential](exponential%20object.md) <br/> - [Functor](functor.md) <br/> - [Kan extension](Kan%20extension.md) <br/> - [Morphism](morphism.md) <br/> - [Natural transformation](natural%20transformation.md) <br/> - [Universal property](universal%20property.md) <br/> - [Yoneda lemma](Yoneda%20lemma.md) |
> | __[Universal constructions](universal%20construction.md)__ | __[Limits](limit%20(category%20theory).md)__ <br/> - [Terminal objects](initial%20and%20terminal%20objects.md) <br/> - [Products](product%20(category%20theory).md) <br/> - [Equalizers](equaliser%20(mathematics).md)  <br/>     - [Kernels](kernel%20(category%20theory).md) <p>  <p> - [Pullbacks](pullback%20(category%20theory).md) <br/> - [Inverse limit](inverse%20limit.md) <p> __[Colimits](colimit.md)__ <br/> - [Initial objects](initial%20and%20terminal%20objects.md) <br/> - [Coproducts](coproduct.md) <br/> - [Coequalizers](coequalizer.md)  <br/>     - [Cokernels and quotients](cokernel.md) <p>  <p> - [Pushout](pushout%20(category%20theory).md) <br/> - [Direct limit](direct%20limit.md)                                                                                                                                                     |
> | __[Algebraic categories](algebraic%20category.md)__        | - [Sets](category%20of%20sets.md) <br/> - [Relations](category%20of%20relations.md) <br/> - [Magmas](category%20of%20magmas.md#category%20of%20magmas) <br/> - [Groups](category%20of%20groups.md) <br/> - [Abelian groups](category%20of%20abelian%20groups.md) <br/> - [Rings](category%20of%20rings.md) \([Fields](category%20of%20rings.md#category%20of%20fields)\) <br/> - [Modules](category%20of%20modules.md) \([Vector spaces](category%20of%20modules.md#example%20the%20category%20of%20vector%20spaces)\)                                                                                                                                                                                                                                                                                                                                                  |
> | __Constructions on categories__                            | - [Free category](free%20category.md) <br/> - [Functor category](functor%20category.md) <br/> - [Kleisli category](Kleisli%20category.md) <br/> - [Opposite category](opposite%20category.md) <br/> - [Quotient category](quotient%20category.md) <br/> - [Product category](product%20category.md) <br/> - [Comma category](comma%20category.md) <br/> - [Subcategory](subcategory.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
>
> | [Higher category theory](higher%20category%20theory.md) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> | -------------------------------------------------------:| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | __Key concepts__                                        | - [Categorification](categorification.md) <br/> - [Enriched category](enriched%20category.md) <br/> - [Higher-dimensional algebra](higher-dimensional%20algebra.md) <br/> - [Homotopy hypothesis](homotopy%20hypothesis.md) <br/> - [Model category](model%20category.md) <br/> - [Simplex category](simplex%20category.md) <br/> - [String diagram](string%20diagram.md) <br/> - [Topos](topos.md)                                                                                                                                                |
> | __n-categories__                                        | __[Weak n-categories](weak%20n-category.md)__ <br/> - [Bicategory](bicategory.md) \([pseudofunctor](pseudo-functor.md)\) <br/> - [Tricategory](tricategory.md) <br/> - [Tetracategory](tetracategory.md) <br/> - [Kan complex](quasi-category.md) <br/> - [∞-groupoid](∞-groupoid.md) <br/> - [∞-topos](∞-topos.md) <p> __[Strict n-categories](strict%20n-category.md#strict%20higher%20categories)__ <br/> - [2-category](strict%202-category.md) \([2-functor](2-functor.md)\) <br/> - [3-category](3-category.md#strict%20higher%20categories) |
> | __[Categorified](categorification.md) concepts__        | - [2-group](2-group.md) <br/> - [2-ring](2-ring.md) <br/> - [_E<sub>n</sub>_-ring](en-ring.md) <br/> - \([Traced](traced%20monoidal%20category.md)\)\([Symmetric](symmetric%20monoidal%20category.md)\) [monoidal category](monoidal%20category.md) <br/> - [n-group](n-group%20(category%20theory).md) <br/> - [n-monoid](n-monoid.md)                                                                                                                                                                                                            |
>
> [![A simple triangular commutative diagram](../../archives/Wikimedia%20Commons/Commutative%20diagram%20for%20morphism.svg)](commutative%20diagram.md)
>
> - ![category icon](../../archives/Wikimedia%20Commons/Symbol%20category%20class.svg) __[Category](https://en.wikipedia.org/wiki/Category:Category%20theory)__
> - ![list icon](../../archives/Wikimedia%20Commons/Symbol%20list%20class.svg) __[Outline](outline%20of%20category%20theory.md)__
> - ![list icon](../../archives/Wikimedia%20Commons/Symbol%20list%20class.svg) __[Glossary](glossary%20of%20category%20theory.md)__

|                                                                                                                                                                                                                <!-- hide <p> - [v](https://en.wikipedia.org/wiki/Template:Functors) <br/> - [t](https://en.wikipedia.org/wiki/Template%20talk:Functors) <br/> - [e](https://en.wikipedia.org/wiki/Special:EditPage/Template%3AFunctors) <p>  <p>  <br/> --> [Functor](functor.md) types                                                                                                                                                                                                                |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| - [Additive](additive%20functor.md#additive%20functors) <br/> - [Adjoint](adjoint%20functors.md) <br/> - [Conservative](conservative%20functor.md) <br/> - [Derived](derived%20functor.md) <br/> - [Diagonal](diagonal%20functor.md) <br/> - [Enriched](enriched%20functor.md) <br/> - [Essentially surjective](essentially%20surjective%20functor.md) <br/> - [Exact](exact%20functor.md) <br/> - [Forgetful](forgetful%20functor.md) <br/> - [Full and faithful](full%20and%20faithful%20functors.md) <br/> - [Logical](logical%20functor.md#logical%20functors) <br/> - [Monoidal](monoidal%20functor.md) <br/> - [Representable](representable%20functor.md) <br/> - [Smooth](smooth%20functor.md) |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

|                                  | <!-- hide <p> - [v](https://en.wikipedia.org/wiki/Template:Functions%20navbox) <br/> - [t](https://en.wikipedia.org/wiki/Template%20talk:Functions%20navbox) <br/> - [e](https://en.wikipedia.org/wiki/Special:EditPage/Template%3AFunctions%20navbox) <p>  <p>  <br/> --> [Function](function%20(mathematics).md)                                                                                                                                                                                                                                          |
| -------------------------------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                  | - [History](history%20of%20the%20function%20concept.md) <br/> - [List of specific functions](list%20of%20mathematical%20functions.md)                                                                                                                                                                                                                                                                                                                                                                                                                       |
| __Types by domain and codomain__ | - [X → 𝔹](Boolean-valued%20function.md) <br/> - [𝔹 → X](ordered%20pair.md) <br/> - [𝔹ⁿ → X](Boolean%20function.md) <br/> - [X → ℤ](integer-valued%20function.md) <br/> - [ℤ → X](sequence.md) <br/> - [X → ℝ](real-valued%20function.md) <br/> - [ℝ → X](function%20of%20a%20real%20variable.md) <br/> - [ℝⁿ → X](function%20of%20several%20real%20variables.md) <br/> - [X → ℂ](complex-valued%20function.md) <br/> - [ℂ → X](function%20of%20a%20complex%20variable.md) <br/> - [ℂⁿ → X](function%20of%20several%20complex%20variables.md)                |
|           __Classes/properties__ | - [Constant](constant%20function.md) <br/> - [Identity](identity%20function.md) <br/> - [Linear](linear%20map.md) <br/> - [Polynomial](polynomial.md) <br/> - [Rational](rational%20function.md) <br/> - [Algebraic](algebraic%20function.md) <br/> - [Analytic](analytic%20function.md) <br/> - [Smooth](smooth%20function.md) <br/> - [Continuous](continuous%20function.md) <br/> - [Measurable](measurable%20function.md) <br/> - [Injective](injective%20function.md) <br/> - [Surjective](surjective%20function.md) <br/> - [Bijective](bijection.md) |
|                __Constructions__ | - [Restriction](restriction%20(mathematics).md) <br/> - [Composition](function%20composition.md) <br/> - [λ](lambda%20calculus.md) <br/> - [Inverse](inverse%20function.md)                                                                                                                                                                                                                                                                                                                                                                                 |
|              __Generalizations__ | - [Relation](relation%20(mathematics).md) \([Binary relation](binary%20relation.md)\) <br/> - [Set-valued](set-valued%20function.md) <br/> - [Multivalued](multivalued%20function.md) <br/> - [Partial](partial%20function.md) <br/> - [Implicit](implicit%20function.md) <br/> - [Space](function%20space.md) <br/> - [Higher-order](higher-order%20function.md) <br/> - [Morphism](morphism.md) <br/> - [Functor](functor.md)                                                                                                                             |
|                                  | - ![category icon](../../archives/Wikimedia%20Commons/Symbol%20category%20class.svg) <p>  [Category](https://en.wikipedia.org/wiki/Category:Functions)                                                                                                                                                                                                                                                                                                                                                                                                      |

> [Category](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Functors](https://en.wikipedia.org/wiki/Category:Functors)
