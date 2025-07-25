---
aliases:
  - co-limit
  - co-limit (category theory)
  - co-limits
  - co-limits (category theory)
  - colimit
  - colimit (category theory)
  - colimits
  - colimits (category theory)
  - limit
  - limit (category theory)
  - limits
  - limits (category theory)
  - weak co-limit
  - weak co-limits
  - weak colimit
  - weak colimits
  - weak limit
  - weak limits
tags:
  - flashcard/active/general/eng/limit__category_theory_
  - language/in/English
---

# limit

<!-- | ![](../../archives/Wikimedia%20Commons/Text%20document%20with%20red%20question%20mark.svg) | This article includes a list of [general references](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources#General%20references), but __it lacks sufficient corresponding [inline citations](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources#Inline%20citations)__. Please help to [improve](https://en.wikipedia.org/wiki/Wikipedia:WikiProject%20Reliability) this article by [introducing](https://en.wikipedia.org/wiki/Wikipedia:When%20to%20cite) more precise citations. _\(March 2013\)__\([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ | -->

In {@{[category theory](category%20theory.md), a branch of [mathematics](mathematics.md)}@}, {@{the abstract notion of a __limit__}@} {@{captures the essential properties of universal constructions}@} such as {@{[products](product%20(category%20theory).md), [pullbacks](pullback%20(category%20theory).md) and [inverse limits](inverse%20limit.md)}@}. {@{The [dual notion](duality%20(category%20theory).md) of a __colimit__}@} generalizes constructions such as {@{[disjoint unions](disjoint%20union.md), [direct sums](direct%20sum.md), [coproducts](coproduct.md), [pushouts](pushout%20(category%20theory).md) and [direct limits](direct%20limit.md)}@}.

{@{Limits and colimits}@}, like {@{the strongly related notions of [universal properties](universal%20property.md) and [adjoint functors](adjoint%20functors.md)}@}, {@{exist at a high level of abstraction}@}. In order to {@{understand them}@}, it is helpful to {@{first study the specific examples these concepts are meant to generalize}@}.

## definition

{@{Limits and colimits in a [category](category%20(mathematics).md) $C$}@} are defined by {@{means of diagrams in $C$}@}. Formally, {@{a __[diagram](diagram%20(category%20theory).md)__ of shape $J$ in $C$}@} is {@{a [functor](functor.md) from $J$ to $C$: $$F:J\to C.$$}@} The category $J$ is thought of {@{as an [index category](index%20category.md)}@}, and the diagram $F$ is thought of {@{as indexing a collection of objects and [morphisms](morphism.md) in $C$ patterned on $J$}@}.

One is most often interested in the case where {@{the category $J$ is a [small](small%20category.md#small%20and%20large%20categories) or even [finite](finite%20set.md) category}@}. A diagram is said to be {@{__small__ or __finite__ whenever $J$ is}@}.

### limits

- See also: [Inverse limit](inverse%20limit.md)

Let {@{$F:J\to C$ be a diagram of shape $J$ in a category $C$}@}. {@{A __[cone](cone%20(category%20theory).md)__ to $F$}@} is {@{an object $N$ of $C$ together with a family $\psi _{X}:N\to F(X)$ of morphisms indexed by the objects $X$ of $J$}@}, such that {@{for every morphism $f:X\to Y$ in $J$, we have $F(f)\circ \psi _{X}=\psi _{Y}$}@}.

{@{A __limit__ of the diagram $F:J\to C$}@} is {@{a cone $(L,\phi )$ to $F$}@} such that {@{for every cone $(N,\psi )$ to $F$ there exists a _unique_ morphism $u:N\to L$ such that $\phi _{X}\circ u=\psi _{X}$ for all $X$ in $J$}@}. <p> (annotation: commutative diagram) {@{![A universal cone](../../archives/Wikimedia%20Commons/Functor%20cone%20%28extended%29.svg)}@}

One says that the cone $(N,\psi )$ {@{factors through the cone $(L,\phi )$ with the unique factorization $u$}@}. {@{The morphism $u$}@} is sometimes called {@{the __mediating morphism__}@}.

Limits are also referred to as {@{_[universal cones](universal%20cone.md#universal%20cones)_}@}, since {@{they are characterized by a [universal property](universal%20property.md)}@} \(see below for more information\). As with {@{every universal property}@}, the above definition describes {@{a balanced state of generality}@}: The limit object $L$ has to {@{be general enough to allow any cone to factor through it}@}; on the other hand, $L$ has to {@{be sufficiently specific, so that only _one_ such factorization is possible for every cone}@}.

Limits may also be {@{characterized as [terminal objects](terminal%20object.md)}@} in {@{the [category of cones](category%20of%20cones.md#category%20of%20cones) to _F_}@}.

It is possible that {@{a diagram does not have a limit at all}@}. However, {@{if a diagram does have a limit then this limit is essentially unique}@}: it is {@{unique [up to](up%20to.md) a unique [isomorphism](isomorphism.md)}@}. For this reason one often {@{speaks of _the_ limit of _F_}@}.

### colimits

- See also: [Direct limit](direct%20limit.md)

{@{The [dual notions](dual%20(category%20theory).md) of limits and cones}@} are {@{colimits and co-cones}@}. Although it is {@{straightforward to obtain the definitions of these by inverting all morphisms in the above definitions}@}, we will {@{explicitly state them here}@}:

{@{A __[co-cone](co-cone.md)__ of a diagram $F:J\to C$}@} is {@{an object $N$ of $C$ together with a family of morphisms $$\psi _{X}:F(X)\to N$$ for every object $X$ of $J$}@}, such that {@{for every morphism $f:X\to Y$ in $J$, we have $\psi _{Y}\circ F(f)=\psi _{X}$}@}.

{@{A __colimit__ of a diagram $F:J\to C$}@} is {@{a co-cone $(L,\phi )$ of $F$}@} such that {@{for any other co-cone $(N,\psi )$ of $F$ there exists a unique morphism $u:L\to N$ such that $u\circ \phi _{X}=\psi _{X}$ for all $X$ in $J$}@}. <p> (annotation: commutative diagram) {@{![A universal co-cone](../../archives/Wikimedia%20Commons/Functor%20co-cone%20%28extended%29.svg)}@}

Colimits are also referred to as {@{_[universal co-cones](universal%20co-cone.md#universal%20cones)_}@}. They can be {@{characterized as [initial objects](initial%20object.md)}@} in {@{the [category of co-cones](category%20of%20co-cones.md#category%20of%20cones) from $F$}@}.

As with {@{limits}@}, {@{if a diagram $F$ has a colimit then this colimit is unique up to a unique isomorphism}@}.

### variations

Limits and colimits can also be {@{defined for collections of objects and morphisms without the use of diagrams}@}. The definitions are the same \(note that in definitions above {@{we never needed to use composition of morphisms in $J$}@}\). This variation, however, {@{adds no new information}@}. {@{Any collection of objects and morphisms}@} {@{defines a \(possibly large\) [directed graph](directed%20graph.md) $G$}@}. If we let {@{$J$ be the [free category](free%20category.md) generated by $G$}@}, there is {@{a universal diagram $F:J\to C$ whose image contains $G$}@}. {@{The limit \(or colimit\) of this diagram}@} is {@{the same as the limit \(or colimit\) of the original collection of objects and morphisms}@}.

{@{__Weak limit__ and __weak colimits__}@} are {@{defined like limits and colimits}@}, except that {@{the uniqueness property of the mediating morphism is dropped}@}.

## examples

<!-- markdownlint-disable-next-line MD024 -->
### limits

{@{The definition of limits is general enough}@} to {@{subsume several constructions useful in practical settings}@}. In the following we will consider {@{the limit \(_L_, _φ_\) of a diagram _F_ : _J_ → _C_}@}.

- {@{__[Terminal objects](terminal%20object.md)__}@}. If {@{_J_ is the empty category}@} there is {@{only one diagram of shape _J_: the empty one \(similar to the [empty function](empty%20function.md#standard%20functions) in set theory\)}@}. {@{A cone to the empty diagram}@} is {@{essentially just an object of _C_}@}. {@{The limit of _F_}@} is {@{any object that is uniquely factored through by every other object}@}. This is {@{just the definition of a _terminal object_}@}.
- {@{__[Products](product%20(category%20theory).md)__}@}. If {@{_J_ is a [discrete category](discrete%20category.md)}@} then {@{a diagram _F_ is essentially nothing but a [family](indexed%20family.md) of objects of _C_, indexed by _J_}@}. {@{The limit _L_ of _F_}@} is called {@{the _product_ of these objects}@}. {@{The cone _φ_}@} consists of {@{a family of morphisms _φ_<sub>_X_</sub> : _L_ → _F_\(_X_\) called the _projections_ of the product}@}. In {@{the [category of sets](category%20of%20sets.md)}@}, for instance, {@{the products are given by [Cartesian products](Cartesian%20product.md)}@} and {@{the projections are just the natural projections onto the various factors}@}.
  - {@{__Powers__}@}. {@{A special case of a product}@} is when {@{the diagram _F_ is a [constant functor](constant%20functor.md#examples) to an object _X_ of _C_ (annotation: that is, the product of _X_ with itself for a number of times that is the number of objects in the _discrete_ category _J_)}@}. {@{The limit of this diagram}@} is called {@{the _J<sup>th</sup> power_ of _X_ and denoted _X_<sup>_J_</sup>}@}.
- {@{__[Equalizers](equalizer%20(mathematics).md)__}@}. If {@{_J_ is a category with two objects and two parallel morphisms from one object to the other}@}, then {@{a diagram of shape _J_ is a pair of parallel morphisms in _C_}@}. {@{The limit _L_ of such a diagram}@} is called {@{an _equalizer_ of those morphisms (annotation: the equalizer is given by _φ_<sub>_X_</sub> where _F_(_X_) is the source of the two parallel morphisms; the other morphism _φ_<sub>_Y_</sub> enforces the equalizer requirements)}@}.
  - {@{__[Kernels](kernel%20(category%20theory).md)__}@}. A _kernel_ is {@{a special case of an equalizer where one of the morphisms is a [zero morphism](zero%20morphism.md)}@}.
- {@{__[Pullbacks](pullback%20(category%20theory).md)__}@}. Let {@{_F_ be a diagram that picks out three objects _X_, _Y_, and _Z_ in _C_}@}, where {@{the only non-identity morphisms (annotation: the other non-identity morphisms may be in the category but not in the diagram) are _f_ : _X_ → _Z_ and _g_ : _Y_ → _Z_}@}. {@{The limit _L_ of _F_}@} is called {@{a _pullback_ or a _fiber product_}@}. It can {@{nicely be visualized as a [commutative square](commutative%20diagram.md)}@}: <p> {@{![commutative diagram for a categorical pullback](../../archives/Wikimedia%20Commons/Pullback%20categories.svg) (annotation: _φ_<sub>_Z_</sub> = _f_ ∘ _φ_<sub>_X_</sub> = _g_ ∘  _φ_<sub>_Y_</sub>)}@}
- {@{__[Inverse limits](inverse%20limit.md)__}@}. Let {@{_J_ be a [directed set](directed%20set.md)}@} \(considered as {@{a small category by adding arrows _i_ → _j_ if and only if _i_ ≥ _j_ (annotation: note the order, which is the opposite of that when we categorize a poset)}@}\) and let {@{_F_ : _J_<sup>op</sup> → _C_ be a diagram}@}. {@{The limit of _F_}@} is called {@{an _inverse limit_ or _projective limit_}@}.
- If {@{_J_ = __1__, the category with a single object and morphism}@}, then {@{a diagram of shape _J_ is essentially just an object _X_ of _C_}@}. {@{A cone to an object _X_}@} is {@{just a morphism with codomain _X_}@}. {@{A morphism _f_ : _Y_ → _X_ is a limit of the diagram _X_}@} {@{if and only if _f_ is an [isomorphism](isomorphism.md)}@}. More generally, if {@{_J_ is any category with an [initial object](initial%20object.md) _i_}@}, then {@{any diagram of shape _J_ has a limit, namely any object isomorphic to _F_\(_i_\)}@}. Such an isomorphism {@{uniquely determines a universal cone to _F_ (annotation: cones unique up to isomorphism are considered the same in this context)}@}.
- {@{__Topological limits__}@}. {@{Limits of functions}@} are {@{a special case of [limits of filters](filters%20in%20topology.md)}@}, which are {@{related to categorical limits as follows}@}. Given {@{a [topological space](topological%20space.md) _X_}@}, denote by {@{_F_ the set of filters on _X_}@}, {@{_x_ ∈ _X_ a point}@}, {@{_V_\(_x_\) ∈ _F_ the [neighborhood filter](filter%20(mathematics).md#neighbourhood%20bases) of _x_}@}, {@{_A_ ∈ _F_ a particular filter}@} and {@{$F_{x,A}=\{G\in F\mid V(x)\cup A\subset G\}$ the set of filters finer than _A_ and that converge to _x_}@}. {@{The filters _F_ are given a small and thin category structure}@} by {@{adding an arrow _A_ → _B_ if and only if _A_ ⊆ _B_}@}. {@{The injection $I_{x,A}:F_{x,A}\to F$ (annotation: injection here means mapping each filter in $F_{x, A}$ to itself in $F$)}@} becomes {@{a functor and the following equivalence holds}@}: <p> &emsp; {@{_x_ is a topological limit of _A_ if and only if _A_ is a categorical limit of $I_{x,A}$}@} <p> (annotation: To somewhat understand this, consider {@{the set of filters $F_A = \set{G \in F \mid A \subset G}$ finer than $A$ and its corresponding injection $I_A: F_A \to F$ as a functor}@}. Then {@{$A$ is a categorical limit of $I_A$}@}. Compare this with the above statement.)

<!-- markdownlint-disable-next-line MD024 -->
### colimits

{@{Examples of colimits}@} are given by {@{the dual versions of the examples above}@}:

- __[Initial objects](initial%20object.md)__ ::@:: are colimits of empty diagrams.
- __[Coproducts](coproduct.md)__ ::@:: are colimits of diagrams indexed by discrete categories.
  - __Copowers__ ::@:: are colimits of constant diagrams from discrete categories.
- __[Coequalizers](coequalizer.md)__ ::@:: are colimits of a parallel pair of morphisms.
  - __[Cokernels](cokernel.md)__ ::@:: are coequalizers of a morphism and a parallel zero morphism.
- __[Pushouts](pushout%20(category%20theory).md)__ ::@:: are colimits of a pair of morphisms with common domain.
- __[Direct limits](direct%20limit.md)__ ::@:: are colimits of diagrams indexed by directed sets.

## properties

### existence of limits

{@{A given diagram _F_ : _J_ → _C_}@} {@{may or may not have a limit \(or colimit\) in _C_}@}. Indeed, there {@{may not even be a cone to _F_, let alone a universal cone}@}.

{@{A category _C_ is said to __have limits of shape _J_<!-- markdown separator -->__}@} if {@{every diagram of shape _J_ has a limit in _C_}@}. Specifically, a category _C_ is said to

- __have products__ ::@:: if it has limits of shape _J_ for every _small_ discrete category _J_ \(it need not have large products\),
- __have equalizers__ ::@:: if it has limits of shape $\bullet \rightrightarrows \bullet$ \(i.e. every parallel pair of morphisms has an equalizer\),
- __have pullbacks__ ::@:: if it has limits of shape $\bullet \rightarrow \bullet \leftarrow \bullet$ \(i.e. every pair of morphisms with common codomain has a pullback\).

{@{A __[complete category](complete%20category.md)__}@} is {@{a category that has all small limits}@} \(i.e. {@{all limits of shape _J_ for every small category _J_}@}\).

One can also make {@{the dual definitions}@}. {@{A category __has colimits of shape _J_<!-- markdown separator -->__}@} if {@{every diagram of shape _J_ has a colimit in _C_}@}. {@{A __[cocomplete category](cocomplete%20category.md)__}@} is {@{one that has all small colimits}@}.

{@{The __existence theorem for limits__}@} states that if {@{a category _C_ has equalizers and all products indexed by the classes Ob\(_J_\) and (annotation: the codomains of) Hom\(_J_\)}@}, then {@{_C_ has all limits of shape _J_}@}.<sup>[\[1\]](#^ref-1)</sup><sup>:&hairsp;§V.2 Thm.1&hairsp;</sup> In this case, {@{the limit of a diagram _F_ : _J_ → _C_}@} can be {@{constructed as the equalizer of the two morphisms}@}<sup>[\[1\]](#^ref-1)</sup><sup>:&hairsp;§V.2 Thm.2&hairsp;</sup> {@{$$s,t:\prod _{i\in \operatorname {Ob} (J)}F(i)\rightrightarrows \prod _{f\in \operatorname {Hom} (J)}F(\operatorname {cod} (f))$$}@} (annotation: Note that {@{the above products may repeat the same object in _C_ multiple times}@}. $s, t$ refers to {@{the two specific morphisms that will be specified below, not the above products}@}. The first product may be interpreted as {@{the sources of morphisms mapped by _F_, one for each object in _J_}@}. The second product may be interpreted as {@{the targets of morphisms mapped by _F_, one for each morphism in _J_}@}. Then morphisms between the above two products {@{can be interpreted after reading below}@}.) given {@{\(in component form\) by $${\begin{aligned}s&={\bigl (}F(f)\circ \pi _{\operatorname {dom} (f)}{\bigr )}_{f\in \operatorname {Hom} (J)}\\t&={\bigl (}\pi _{\operatorname {cod} (f)}{\bigr )}_{f\in \operatorname {Hom} (J)}.\end{aligned} }$$}@} (annotation: Both $s, t$ {@{describes a unique product of morphisms, each mapped from each morphism _f_ in _J_}@}. To understand them, consider {@{the equalizer morphism, denoted _ϕ_ here}@}, which can {@{also be described as a unique product of morphisms, each is _ϕ_<sub>_X_</sub> of a cone for each object _X_ in _J_}@}. For {@{each morphism _f_: _X_ → _Y_ in _J_, we can trace out two ways to compose functions}@}. The two ways are respectively {@{_F_(_f_) ∘ _ϕ_<sub>_X_</sub> = _F_(_f_) ∘ _π_<sub>dom(_f_)</sub> ∘ _ϕ_ and _ϕ_<sub>_Y_</sub> = _π_<sub>cod(_f_)</sub> ∘ _ϕ_}@}. We can see these two ways are {@{essentially the cone commutative diagram, by interpreting the projection morphisms as selecting _X_ or _Y_ from one of the two products above}@}. The universal property {@{of the equalizer makes the above cone the limit}@}.) There is {@{a dual __existence theorem for colimits__ in terms of coequalizers and coproducts}@}. {@{Both of these theorems}@} give {@{sufficient and necessary conditions for the existence of all \(co\)limits of shape _J_}@}.

### universal property

{@{Limits and colimits}@} are {@{important special cases of [universal constructions](universal%20construction.md)}@}.

Let {@{_C_ be a category and let _J_ be a small index category}@}. {@{The [functor category](functor%20category.md) _C_<sup>_J_</sup>}@} may be thought of as {@{the category of all diagrams of shape _J_ in _C_}@}. {@{The _[diagonal functor](diagonal%20functor.md)_ $$\Delta :{\mathcal {C} }\to {\mathcal {C} }^{\mathcal {J} }$$}@} is {@{the functor that maps each object _N_ in _C_ to the constant functor Δ\(_N_\) : _J_ → _C_ to _N_}@}. That is, {@{Δ\(_N_\)\(_X_\) = _N_ for each object _X_ in _J_ and Δ\(_N_\)\(_f_\) = id<sub>_N_</sub> for each morphism _f_ in _J_}@}.

Given {@{a diagram _F_: _J_ → _C_}@} \(thought of {@{as an object in _C_<sup>_J_</sup>}@}\), {@{a [natural transformation](natural%20transformation.md) _ψ_ : Δ\(_N_\) → _F_ \(which is just a morphism in the category _C_<sup>_J_</sup>\)}@} is {@{the same thing as a cone from _N_ to _F_}@}. To see this, first note that {@{Δ\(_N_\)\(_X_\) = _N_ for all X}@} implies that {@{the components of _ψ_ are morphisms _ψ_<sub>_X_</sub> : _N_ → _F_\(_X_\), which all share the domain _N_}@}. Moreover, {@{the requirement that the cone's diagrams commute is true}@} {@{simply because this _ψ_ is a natural transformation}@}. \({@{Dually}@}, {@{a natural transformation _ψ_ : _F_ → Δ\(_N_\)}@} is {@{the same thing as a co-cone from _F_ to _N_}@}.\)

Therefore, {@{the definitions of limits and colimits}@} can then be {@{restated in the form}@}:

- A limit of _F_ ::@:: is a universal morphism from Δ to _F_.
- A colimit of _F_ ::@:: is a universal morphism from _F_ to Δ.

### adjunctions

Like {@{all universal constructions}@}, {@{the formation of limits and colimits is functorial in nature}@}. In other words, if {@{every diagram of shape _J_ has a limit in _C_ \(for _J_ small\)}@} there {@{exists a __limit functor__ $$\lim :{\mathcal {C} }^{\mathcal {J} }\to {\mathcal {C} }$$}@} which assigns {@{each diagram its limit}@} and {@{each [natural transformation](natural%20transformation.md) η : _F_ → _G_ the unique morphism lim η : lim _F_ → lim _G_ commuting with the corresponding universal cones}@}. This functor is {@{[right adjoint](right%20adjoint.md) to the diagonal functor Δ : _C_ → _C_<sup>_J_</sup>}@}. {@{This adjunction gives a bijection}@} between {@{the set of all morphisms from _N_ (annotation: _N_ is an object in _C_) to lim _F_ and the set of all cones from _N_ to _F_ $$\operatorname {Hom} (N,\lim F)\cong \operatorname {Cone} (N,F)$$}@} (annotation: Note that {@{$\operatorname{Cone}(N, F) \equiv \operatorname{Hom}(\Delta(N), F)$}@}. This is saying {@{the number of cones from any object _N_ to _F_ equals the number of morphisms from _N_ to the limit object of _F_}@}, which makes sense since {@{each cone has an unique morphism to the limit object of _F_}@}.) which is {@{natural in the variables _N_ and _F_}@}. {@{The counit of this adjunction}@} is {@{simply the universal cone from lim _F_ to _F_ (annotation: or the universal morphism in _C_<sup>_J_</sup> from Δ(lim _F_) to _F_)}@}. If {@{the index category _J_ is [connected](connected%20category.md) (annotation: i.e. every two objects are connected by a chain of morphisms ignoring their directions) \(and nonempty\)}@} then {@{the unit of the adjunction (annotation: which is _not_ the universal co-cone from _F_ to lim _F_, but is the universal morphism in _C_ from _N_ to lim Δ(_N_))}@} is {@{an isomorphism so that lim is a left inverse of Δ (annotation: i.e. _N_ ≅ lim Δ(_N_))}@}. (annotation: This is saying {@{the limit of the constant functor of _J_ to any object _N_ is isomorphic to _N_}@}.) This {@{fails if _J_ is not connected}@}. For example, if {@{_J_ is a discrete category}@}, {@{the components of the unit (annotation: referring to the components of the natural transformation η : 1<sub>_C_</sub> → lim Δ)}@} are {@{the [diagonal morphisms](diagonal%20morphism.md) δ : _N_ → _N_<sup>_J_</sup>}@}. (annotation: That is, {@{the limit of the constant functor of _J_ to any object _N_ is _N_<sup>_J_</sup>, latter of which is the product object of _N_ with itself repeated for the number of objects in _J_}@}. To see this, {@{find the limit of the constant functor of _J_ to an object _N_ in your mind and make use of the universal property of products}@}.)

{@{Dually}@}, if {@{every diagram of shape _J_ has a colimit in _C_ \(for _J_ small\)}@} there {@{exists a __colimit functor__ $$\operatorname {colim} :{\mathcal {C} }^{\mathcal {J} }\to {\mathcal {C} }$$}@} which {@{assigns each diagram its colimit}@}. This functor is {@{[left adjoint](left%20adjoint.md) to the diagonal functor Δ : _C_ → _C_<sup>_J_</sup>}@}, and one has {@{a natural isomorphism $$\operatorname {Hom} (\operatorname {colim} F,N)\cong \operatorname {Cocone} (F,N).$$}@} (annotation: Note that {@{$\operatorname{Cocone}(F, N) \equiv \operatorname{Hom}(F, \Delta(N))$}@}. This is saying {@{the number of co-cones from _F_ to any object _N_ equals the number of morphisms from the co-limit object of _F_ to _N_}@}, which makes sense since {@{each co-cone has an unique morphism from the co-limit object of _F_}@}.) {@{The unit of this adjunction}@} is {@{the universal cocone from _F_ to colim _F_ (annotation: or the universal morphism in _C_<sup>_J_</sup> from _F_ to Δ(colim _F_))}@}. If {@{_J_ is connected (annotation: i.e. every two objects are connected by a chain of morphisms ignoring their directions) \(and nonempty\)}@} then {@{the counit (annotation: which is _not_ the universal cone from colim _F_ to _F_, but is the universal morphism in _C_ from colim Δ(_N_) to _N_)}@} is {@{an isomorphism, so that colim is a left inverse of Δ (annotation: i.e. _N_ ≅ colim Δ(_N_))}@}. (annotation: This is saying {@{the colimit of the constant functor of _J_ to any object _N_ is isomorphic to _N_}@}.)

Note that {@{both the limit and the colimit functors}@} are {@{[_covariant_](covariant%20functor.md#covariance%20and%20contravariance) functors}@}.

### as representations of functors

- See also: [Limit and colimit of presheaves](limit%20and%20colimit%20of%20presheaves.md)

One can use {@{[Hom functors](hom%20functor.md)}@} to {@{relate limits and colimits in a category _C_ to limits in __Set__, the [category of sets](category%20of%20sets.md)}@}. This follows, {@{in part, from the fact the covariant Hom functor Hom\(_N_, –\) : _C_ → __Set__ [preserves all limits](#preservation%20of%20limits) in _C_}@}. By {@{duality}@}, {@{the contravariant Hom functor must take colimits to limits}@}.

If {@{a diagram _F_ : _J_ → _C_ has a limit in _C_, denoted by lim _F_}@}, there is {@{a [canonical isomorphism](canonical%20isomorphism.md) $$\operatorname {Hom} (N,\lim F)\cong \lim \operatorname {Hom} (N,F-)$$}@} (annotation: The covariant Hom functor {@{sends the limit object $\lim F$ to $\operatorname{Hom}(N, \lim F)$}@}. As the covariant Hom functor preserves limits, it is {@{also the limit object of $\operatorname{Hom}(N, F-)$}@}.) which is {@{natural in the variable _N_}@}. Here {@{the functor Hom\(_N_, _F_<!-- markdown separator -->–\) is the composition of the Hom functor Hom\(_N_, –\) with _F_ (annotation: i.e. Hom\(_N_, –\) ∘ _F_: _J_ → __Set__, composable since _J_ → _C_ → __Set__)}@}. This isomorphism is {@{the unique one which respects the limiting cones}@}.

One can {@{use the above relationship to define the limit of _F_ in _C_}@}. The first step is to observe that {@{the limit of the functor Hom\(_N_, _F_<!-- markdown separator -->–\) can be identified with the set of all cones from _N_ to _F_}@}: {@{$$\lim \operatorname {Hom} (N,F-)=\operatorname {Cone} (N,F).$$ \(annotation: we know Hom(_N_, lim _F_) ≡ Cone(_N_, _F_) from above\)}@} {@{The limiting cone}@} \(annotation: that is, {@{the limiting cone of the functor Hom\(_N_, _F_–\): _J_ → __Set__ in the Hom category Hom<sub>_C_</sub>\(_N_, –\)}@}, which is {@{sent from _C_ by the Hom functor Hom\(_N_, –\): _C_ → __Set__}@}\) is given by {@{the family of maps π<sub>_X_</sub> : Cone\(_N_, _F_\) → Hom\(_N_, _FX_\) where _π_<sub>_X_</sub>\(_ψ_\) = _ψ_<sub>_X_</sub>}@} \(annotation: lim Hom\(_N_, _F_–\) is {@{a set of morphisms}@}. Each morphism {@{can be identified with a cone in the set of cones Cone\(_N_, _F_\)}@}, in the way as previously explained. But also, there is {@{a limiting cone of Hom\(_N_, _F_–\) in the Hom category where the above set of morphisms belong to}@}, which has {@{the same shape as the limiting cone of _F_ in _C_}@}. Then, {@{the component at _X_ of _J_ in the limiting cone of _F_ in _C_}@}, which is {@{a morphism _f_<sub>_X_</sub> : lim _F_ → _F_(_X_) in _C_}@}, is mapped to {@{the component at _X_ of _J_ in the limiting cone of Hom\(_N_, _F_–\)}@}, which is {@{a function composition _f_<sub>_X_</sub> ∘ – : Hom\(_N_, lim _F_\) → Hom\(_N_, _FX_\)}@}. This function composition can be identified with {@{π<sub>_X_</sub> : Cone\(_N_, _F_\) → Hom\(_N_, _FX_\)}@}, which given {@{a cone from _N_ to _F_}@}, returns {@{its component of _F_ at _X_, a morphism from _N_ to _FX_}@}.\). If one is given {@{an object _L_ of _C_ together with a [natural isomorphism](natural%20isomorphism.md#natural%20isomorphism) _Φ_ : Hom\(–, _L_\) → Cone\(–, _F_\)}@}, {@{the object _L_ will be a limit of _F_ with the limiting cone given by _Φ_<sub>_L_</sub>\(id<sub>_L_</sub>\)}@} \(annotation: In a way similar to {@{proving the Yoneda lemma}@}, {@{the natural isomorphism at each component is uniquely determined once we choose that _Φ_<sub>_L_</sub>\(id<sub>_L_</sub>\) maps to a \(the\) limiting cone in Cone(_L_, _F_)}@}.\). In fancy language, this amounts to saying that {@{a limit of _F_ is a \(annotation: co-\)[representation](representable%20functor.md) of the functor Cone\(–, _F_\) : _C_ → __Set__ (annotation: the cone functor sends each object _N_ to the set of cones from _N_ to _F_)}@}.

{@{Dually}@}, if {@{a diagram _F_ : _J_ → _C_ has a colimit in _C_, denoted colim _F_}@}, there is {@{a unique canonical isomorphism $$\operatorname {Hom} (\operatorname {colim} F,N)\cong \lim \operatorname {Hom} (F-,N)$$}@} \(annotation: The contravariant Hom functor {@{sends the colimit object $\operatorname{colim} F$ to $\operatorname{Hom}(\operatorname{colim} F, N)$}@}. As the contravariant Hom functor sends colimits to limits, it is {@{also the limit object of $\operatorname{Hom}(F-, N)$}@}.\) which is {@{natural in the variable _N_ and respects the colimiting cones}@}. Identifying {@{the limit of Hom\(_F_<!-- markdown separator -->–, _N_\) with the set Cocone\(_F_, _N_\) \(annotation: we know Hom(colim _F_, _N_) ≡ Cocone(_F_, _N_) from above\)}@}, this relationship can be used to {@{define the colimit of the diagram _F_ as a representation of the functor Cocone\(_F_, –\) \(annotation: i.e. the colimit object _L_ together with a natural isomorphism _Φ_ : Hom\(_L_, –\) → Cocone\(_F_, –\)\)}@}. \(annotation: In a way similar to {@{proving the Yoneda lemma}@}, {@{the isomorphism at each component is uniquely determined once we choose that _Φ_<sub>_L_</sub>\(id<sub>_L_</sub>\) maps to a \(the\) limiting cocone in Cocone(_F_, _L_)}@}.\)

### interchange of limits and colimits of sets

Let {@{_I_ be a finite category and _J_ be a small [filtered category](filtered%20category.md)}@}. For {@{any [bifunctor](bifunctor.md#bifunctors%20and%20multifunctors) $$F:I\times J\to \mathbf {Set} ,$$}@} there is {@{a [natural isomorphism](natural%20isomorphism.md#natural%20isomorphism) $$\operatorname {colim} \limits _{J}\lim _{I}F(i,j)\rightarrow \lim _{I}\operatorname {colim} \limits _{J}F(i,j).$$}@} In words, {@{filtered colimits in __Set__ commute with finite limits}@}. It also holds that {@{small colimits commute with small limits}@}.<sup>[\[2\]](#^ref-2)</sup>

## functors and limits

If {@{_F_ : _J_ → _C_ is a diagram in _C_ and _G_ : _C_ → _D_ is a [functor](functor.md)}@} then {@{by composition \(recall that a diagram is just a functor\) one obtains a diagram _GF_ : _J_ → _D_}@}. A natural question is then: <p> &emsp; "{@{How are the limits of _GF_ related to those of _F_?}@}"

### preservation of limits

{@{A functor _G_ : _C_ → _D_}@} {@{induces a map from Cone\(_F_\) to Cone\(_GF_\)}@}: {@{if _Ψ_ is a cone from _N_ to _F_ then _GΨ_ is a cone from _GN_ to _GF_}@}. {@{The functor _G_ is said to __preserve the limits of _F_<!-- markdown separator -->__}@} if {@{\(_GL_, _Gφ_\) is a limit of _GF_ whenever \(_L_, _φ_\) is a limit of _F_ (annotation: this is similar to lifting of limits, but the "whenever" clauses swap places)}@}. \(Note that {@{if the limit of _F_ does not exist, then _G_ [vacuously](vacuous%20truth.md) preserves the limits of _F_}@}.\)

{@{A functor _G_ is said to __preserve all limits of shape _J_<!-- markdown separator -->__}@} if {@{it preserves the limits of all diagrams _F_ : _J_ → _C_}@}. For example, one can say that {@{_G_ preserves products, equalizers, pullbacks, etc.}@} {@{A __continuous functor__}@} is {@{one that preserves all _small_ limits}@}.

One can make {@{analogous definitions for colimits}@}. For instance, {@{a functor _G_ preserves the colimits of _F_}@} if {@{_G_\(_L_, _φ_\) is a colimit of _GF_ whenever \(_L_, _φ_\) is a colimit of _F_}@}. {@{A __cocontinuous functor__}@} is {@{one that preserves all _small_ colimits}@}.

If {@{_C_ is a [complete category](complete%20category.md)}@}, then, by {@{the above existence theorem for limits}@}, a functor _G_ : _C_ → _D_ is {@{continuous if and only if it preserves \(small\) products and equalizers}@}. {@{Dually}@}, _G_ is {@{cocontinuous if and only if it preserves \(small\) coproducts and coequalizers}@}.

{@{An important property of [adjoint functors](adjoint%20functors.md)}@} is that {@{every right adjoint functor is continuous and every left adjoint functor is cocontinuous}@}. Since {@{adjoint functors exist in abundance}@}, this gives {@{numerous examples of continuous and cocontinuous functors}@}.

For {@{a given diagram _F_ : _J_ → _C_ and functor _G_ : _C_ → _D_}@}, if {@{both _F_ and _GF_ have specified limits}@} there is {@{a unique canonical morphism $$\tau _{F}:G\lim F\to \lim GF$$}@} which {@{respects the corresponding limit cones}@}. {@{The functor _G_ preserves the limits of _F_}@} {@{if and only if this map is an isomorphism}@}. If {@{the categories _C_ and _D_ have all limits of shape _J_}@} then {@{lim is a functor (annotation: lim : _C_<sup>_J_</sup> → _C_ for the left one below and lim : _D_<sup>_J_</sup> → _D_ for the right one below)}@} and {@{the morphisms τ<sub>_F_</sub> form the components of a [natural transformation](natural%20transformation.md) $$\tau :G\lim \to \lim G^{J}.$$ (annotation: _G_<sup>_J_</sup> : _C_<sup>_J_</sup> → _D_<sup>_J_</sup>)}@} {@{The functor _G_ preserves all limits of shape _J_}@} {@{if and only if τ is a natural isomorphism}@}. In this sense, the functor _G_ can be said to {@{_commute with limits_ \([up to](up%20to.md) a canonical natural isomorphism\)}@}.

{@{Preservation of limits and colimits}@} is {@{a concept that only applies to _[covariant](covariant%20functor.md#covariance%20and%20contravariance)_ functors}@}. For {@{[contravariant functors](contravariant%20functor.md#covariance%20and%20contravariance)}@} the corresponding notions would be {@{a functor that takes colimits to limits, or one that takes limits to colimits}@}.

### lifting of limits

{@{A functor _G_ : _C_ → _D_}@} is said to {@{__lift limits__ for a diagram _F_ : _J_ → _C_}@} if {@{whenever \(_L_, _φ_\) is a limit of _GF_ there exists a limit \(_L_<!-- markdown separator -->′, _φ_<!-- markdown separator -->′\) of _F_ such that _G_\(_L_<!-- markdown separator -->′, _φ_<!-- markdown separator -->′\) = \(_L_, _φ_\) (annotation: this is similar to preservation of limits, but the "whenever" clauses swap places; note there can be multiple preimage cones, and _at least_ one is a limit)}@}. {@{A functor _G_ __lifts limits of shape _J_<!-- markdown separator -->__}@} if {@{it lifts limits for all diagrams of shape _J_}@}. One can therefore talk about {@{lifting products, equalizers, pullbacks, etc.}@} Finally, one says that {@{_G_ __lifts limits__ if it lifts all limits}@}. There are {@{dual definitions for the lifting of colimits}@}.

{@{A functor _G_ __lifts limits uniquely__ for a diagram _F_}@} if {@{there is a unique preimage cone \(_L_<!-- markdown separator -->′, _φ_<!-- markdown separator -->′\) such that \(_L_<!-- markdown separator -->′, _φ_<!-- markdown separator -->′\) is a limit of _F_ and _G_\(_L_<!-- markdown separator -->′, _φ_<!-- markdown separator -->′\) = \(_L_, _φ_\) \(annotation: "unique" means there can be multiple preimage cones, and _exactly_ one is a limit\)}@}. One can show that {@{_G_ lifts limits uniquely if and only if it lifts limits and is [amnestic](amnestic%20functor.md) (annotation: if _Ff_ is an identity morphism then _f_ is an identity morphism)}@}.

Lifting of limits is clearly {@{related to preservation of limits}@}. If {@{_G_ lifts limits for a diagram _F_ and _GF_ has a limit}@}, then {@{_F_ also has a limit and _G_ preserves the limits of _F_ (annotation: note that limits are essentially unique up to unique isomorphisms)}@}. It follows that:

- If _G_ lifts limits of all shape _J_ and _D_ has all limits of shape _J_, ::@:: then _C_ also has all limits of shape _J_ and _G_ preserves these limits.
- If _G_ lifts all small limits and _D_ is complete, ::@:: then _C_ is also complete and _G_ is continuous.

The dual statements {@{for colimits are equally valid}@}.

### creation and reflection of limits

Let {@{_F_ : _J_ → _C_ be a diagram}@}. {@{A functor _G_ : _C_ → _D_}@} is said to

- __create limits__ for _F_ ::@:: if whenever \(_L_, _φ_\) is a limit of _GF_ there exists a unique cone \(_L_<!-- markdown separator -->′, _φ_<!-- markdown separator -->′\) to _F_ such that _G_\(_L_<!-- markdown separator -->′, _φ_<!-- markdown separator -->′\) = \(_L_, _φ_\), and furthermore, this cone is a limit of _F_. \(annotation: i.e. there is _exactly_ one preimage cone and it is a limit\)
- __reflect limits__ for _F_ ::@:: if each cone to _F_ whose image under _G_ is a limit of _GF_ is already a limit of _F_. \(annotation: preimage cones are all limits\)

Dually, one can {@{define creation and reflection of colimits}@}.

The following statements are {@{easily seen to be equivalent}@}: (annotation: the 2 statements are: {@{the functor _G_ creates limits; the functor _G_ lifts limits uniquely and reflects limits}@})

- The functor _G_ creates limits.
- The functor _G_ lifts limits uniquely and reflects limits.

There are examples of {@{functors which lift limits uniquely but neither create nor reflect them}@}.

<!-- markdownlint-disable-next-line MD024 -->
### examples

- {@{Every [representable functor](representable%20functor.md) _C_ → __Set__}@} {@{preserves limits \(but not necessarily colimits\)}@}. In particular, for {@{any object _A_ of _C_}@}, this is true of {@{the covariant [Hom functor](hom%20functor.md) Hom\(_A_,–\) : _C_ → __Set__}@}.
- {@{The [forgetful functor](forgetful%20functor.md) _U_ : __Grp__ → __Set__}@} {@{creates \(and preserves\) all small limits and [filtered colimits](filtered%20colimit.md)}@}; however, {@{_U_ does not preserve coproducts}@}. This situation is {@{typical of algebraic forgetful functors}@}.
- {@{The [free functor](free%20functor.md#free%20functor) _F_ : __Set__ → __Grp__ \(which assigns to every set _S_ the [free group](free%20group.md) over _S_\)}@} is {@{left adjoint to forgetful functor _U_ and is, therefore, cocontinuous}@}. This explains why {@{the [free product](free%20product.md) of two free groups _G_ and _H_}@} is {@{the free group generated by the [disjoint union](disjoint%20union.md) of the generators of _G_ and _H_}@}.
- {@{The inclusion functor __Ab__ → __Grp__}@} {@{creates limits but does not preserve coproducts}@} \({@{the coproduct of two abelian groups}@} being {@{the [direct sum](direct%20sum%20of%20abelian%20groups.md#direct%20sum%20of%20abelian%20groups)}@}\).
- {@{The forgetful functor __Top__ → __Set__}@} {@{lifts limits and colimits uniquely but creates neither}@}.
- Let {@{__Met__<sub>_c_</sub>}@} be {@{the category of [metric spaces](metric%20space.md) with [continuous functions](continuous%20function.md) for morphisms}@}. {@{The forgetful functor __Met__<sub>_c_</sub> → __Set__}@} {@{lifts finite limits but does not lift them uniquely}@}.

## a note on terminology

{@{Older terminology}@} referred to {@{limits as "inverse limits" or "projective limits"}@}, and to {@{colimits as "direct limits" or "inductive limits"}@}. This has been {@{the source of a lot of confusion}@}.

There are {@{several ways to remember the modern terminology}@}. First of all,

- cokernels,
- coproducts,
- coequalizers, and
- codomains

(annotation: {@{cokernels, coproducts, coequalizers, codomains}@}) are {@{types of colimits}@}, whereas

- kernels,
- products
- equalizers, and
- domains

(annotation: {@{kernels, products, equalizers, domains}@}) are {@{types of limits}@}. Second, {@{the prefix "co"}@} {@{implies "first variable of the $\operatorname {Hom}$"}@}. {@{Terms like "cohomology" and "cofibration"}@} all have {@{a slightly stronger association with the first variable}@}, i.e., {@{the contravariant variable, of the $\operatorname {Hom}$ bifunctor}@}.

## see also

- [Cartesian closed category](Cartesian%20closed%20category.md) – ::@:: Type of category in category theory
- [Equaliser \(mathematics\)](equaliser%20(mathematics).md) – ::@:: Set of arguments where two or more functions have the same value
- [Inverse limit](inverse%20limit.md) – ::@:: Construction in category theory
- [Product \(category theory\)](product%20(category%20theory).md) – ::@:: Generalized object in category theory

## references

This text incorporates [content](https://en.wikipedia.org/wiki/limit_(category_theory)) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFMac Lane1998"></a> [Mac Lane, Saunders](Saunders%20Mac%20Lane.md) \(1998\). _[Categories for the Working Mathematician](Categories%20for%20the%20Working%20Mathematician.md)_. [Graduate Texts in Mathematics](Graduate%20Texts%20in%20Mathematics.md). Vol. 5 \(2nd ed.\). [Springer-Verlag](Springer-Verlag.md#history). [ISBN](ISBN%20(identifier).md) [0-387-98403-8](https://en.wikipedia.org/wiki/Special:BookSources/0-387-98403-8). [Zbl](Zbl%20(identifier).md) [0906.18001](https://zbmath.org/?format=complete&q=an:0906.18001). <a id="^ref-1"></a>^ref-1
2. [commutativity of limits and colimits](https://ncatlab.org/nlab/show/commutativity+of+limits+and+colimits) at the [_n_<!-- markdown separator -->Lab](nLab.md) <a id="^ref-2"></a>^ref-2

## further reading

- <a id="CITEREFAdámekHorst HerrlichGeorge E. Strecker1990"></a> Adámek, Jiří; Horst Herrlich; George E. Strecker \(1990\). [_Abstract and Concrete Categories_](http://katmat.math.uni-bremen.de/acc/acc.pdf) \(PDF\). John Wiley & Sons. [ISBN](ISBN%20(identifier).md) [0-471-60922-6](https://en.wikipedia.org/wiki/Special:BookSources/0-471-60922-6).
- <a id="CITEREFMac Lane1998"></a> [Mac Lane, Saunders](Saunders%20Mac%20Lane.md) \(1998\). _[Categories for the Working Mathematician](Categories%20for%20the%20Working%20Mathematician.md)_. [Graduate Texts in Mathematics](Graduate%20Texts%20in%20Mathematics.md). Vol. 5 \(2nd ed.\). [Springer-Verlag](Springer-Verlag.md#history). [ISBN](ISBN%20(identifier).md) [0-387-98403-8](https://en.wikipedia.org/wiki/Special:BookSources/0-387-98403-8). [Zbl](Zbl%20(identifier).md) [0906.18001](https://zbmath.org/?format=complete&q=an:0906.18001).
- <a id="CITEREFBorceux1994"></a> Borceux, Francis \(1994\). "Limits". [_Handbook of categorical algebra_](https://archive.org/details/handbookofcatego0000borc). Encyclopedia of mathematics and its applications 50-51, 53 \[i.e. 52\]. Vol. 1. Cambridge University Press. [ISBN](ISBN%20(identifier).md) [0-521-44178-1](https://en.wikipedia.org/wiki/Special:BookSources/0-521-44178-1).

## external links

- [Interactive Web page](https://web.archive.org/web/20080916162345/http://www.j-paine.org/cgi-bin/webcats/webcats.php) which generates examples of limits and colimits in the category of finite sets. Written by [Jocelyn Paine](https://web.archive.org/web/20081223001815/http://www.j-paine.org/).
- [Limit](https://ncatlab.org/nlab/show/limit) at the [_n_<!-- markdown separator -->Lab](nLab.md)

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

<!-- markdownlint MD028 -->

> [Category](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Limits \(category theory\)](https://en.wikipedia.org/wiki/Category:Limits%20%28category%20theory%29)
