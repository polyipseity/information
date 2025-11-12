---
aliases:
  - universal construction
  - universal constructions
  - universal properties
  - universal property
tags:
  - flashcard/active/general/eng/universal_property
  - language/in/English
---

# universal property

- For other uses, see [Universal \(disambiguation\)](universal%20(disambiguation).md).

> {@{![The typical diagram of the definition of a universal morphism.](../../archives/Wikimedia%20Commons/Universal%20morphism%20definition.svg)}@}
>
> The typical diagram of {@{the definition of a universal morphism}@}. (annotation: In the diagram, {@{$u$ is an universal morphism from $X$ to $F$}@}. The intuition is annotated below.)

In {@{[mathematics](mathematics.md), more specifically in [category theory](category%20theory.md)}@}, {@{a __universal property__}@} is {@{a property that characterizes [up to](up%20to.md) an [isomorphism](isomorphism.md) the result of some constructions}@}. Thus, universal properties can be used for {@{defining some objects independently from the method chosen for constructing them}@}. For example, the definitions of {@{the [integers](integer.md) from the [natural numbers](natural%20number.md)}@}, of {@{the [rational numbers](rational%20number.md) from the integers}@}, of {@{the [real numbers](real%20number.md) from the rational numbers}@}, and of {@{[polynomial rings](polynomial%20ring.md) from the [field](field%20(mathematics).md) of their coefficients}@} can {@{all be done in terms of universal properties}@}. In particular, {@{the concept of universal property}@} allows {@{a simple proof that all [constructions of real numbers](constructions%20of%20real%20numbers.md) are equivalent}@}: it {@{suffices to prove that they satisfy the same universal property}@}.

Technically, {@{a universal property}@} is defined {@{in terms of [categories](category%20(mathematics).md) and [functors](functor.md) by means of a __universal morphism__}@} \(see [§ Formal definition](#formal%20definition), below\). Universal morphisms can also be {@{thought more abstractly as [initial or terminal objects](initial%20and%20terminal%20objects.md) of a [comma category](comma%20category.md)}@} \(see {@{[§ Connection with comma categories](#connection%20with%20comma%20categories)}@}, below\).

Universal properties {@{occur almost everywhere in mathematics}@}, and the use of the concept allows the use of {@{general properties of universal properties for easily proving some properties that would need boring verifications otherwise}@}. For example, given {@{a [commutative ring](commutative%20ring.md) _R_}@}, {@{the [field of fractions](field%20of%20fractions.md) of the [quotient ring](quotient%20ring.md) of _R_ by a [prime ideal](prime%20ideal.md) _p_}@} can be identified with {@{the [residue field](residue%20field.md) of the [localization](localization%20(commutative%20algebra).md) of _R_ at _p_}@}; that is {@{$R_{p}/pR_{p}\cong \operatorname {Frac} (R/p)$}@} \(all these constructions can be {@{defined by universal properties}@}\).

Other objects that can be {@{defined by universal properties}@} include: all [free objects](free%20object.md), [direct products](direct%20product.md) and [direct sums](direct%20sum.md), [free groups](free%20group.md), [free lattices](free%20lattice.md), [Grothendieck group](Grothendieck%20group.md), [completion of a metric space](completion%20of%20a%20metric%20space.md#completion), [completion of a ring](completion%20of%20a%20ring.md), [Dedekind–MacNeille completion](Dedekind–MacNeille%20completion.md), [product topologies](product%20topology.md), [Stone–Čech compactification](Stone–Čech%20compactification.md), [tensor products](tensor%20product.md), [inverse limit](inverse%20limit.md) and [direct limit](direct%20limit.md), [kernels](kernel%20(linear%20algebra).md) and [cokernels](cokernel.md), [quotient groups](quotient%20group.md), [quotient vector spaces](quotient%20vector%20space.md), and other [quotient spaces](quotient%20space%20(disambiguation).md).

## motivation

Before {@{giving a formal definition of universal properties}@}, we {@{offer some motivation for studying such constructions}@}. (annotation: they are {@{simplification, isomorphism, functoriality, ubiquity}@})

- {@{The concrete details of a given construction may be messy}@}, but if {@{the construction satisfies a universal property}@}, one can {@{forget all those details: all there is to know about the construction is already contained in the universal property}@}. Proofs {@{often become short and elegant if the universal property is used rather than the concrete details}@}. For example, {@{the [tensor algebra](tensor%20algebra.md) of a [vector space](vector%20space.md)}@} is {@{slightly complicated to construct}@}, but {@{much easier to deal with by its universal property}@}.
- Universal properties {@{define objects uniquely up to a unique [isomorphism](isomorphism.md)}@}.<sup>[\[1\]](#^ref-1)</sup> Therefore, {@{one strategy to prove that two objects are isomorphic}@} is to {@{show that they satisfy the same universal property}@}.
- Universal constructions are {@{functorial in nature}@}: if {@{one can carry out the construction for every object in a category _C_}@} then one {@{obtains a [functor](functor.md) on _C_}@}. Furthermore, this functor is {@{a [right or left adjoint](adjoint%20functors.md) to the functor _U_ used in the definition of the universal property}@}.<sup>[\[2\]](#^ref-2)</sup>
- Universal properties {@{occur everywhere in mathematics}@}. By {@{understanding their abstract properties}@}, one obtains {@{information about all these constructions and can avoid repeating the same analysis for each individual instance}@}.

## formal definition

To {@{understand the definition of a universal construction}@}, it is {@{important to look at examples}@}. Universal constructions were {@{not defined out of thin air, but were rather defined after mathematicians began noticing a pattern in many mathematical constructions}@} \(see Examples below\). Hence, the definition {@{may not make sense to one at first}@}, but will {@{become clear when one reconciles it with concrete examples}@}.

Let {@{$F:{\mathcal {C} }\to {\mathcal {D} }$ be a functor between categories ${\mathcal {C} }$ and ${\mathcal {D} }$}@}. In what follows, let {@{$X$ be an object of ${\mathcal {D} }$, $A$ and $A'$ be objects of ${\mathcal {C} }$, and $h:A\to A'$ be a morphism in ${\mathcal {C} }$}@}.

Then, the functor $F$ {@{maps $A$, $A'$ and $h$ in ${\mathcal {C} }$ to $F(A)$, $F(A')$ and $F(h)$ in ${\mathcal {D} }$}@}.

{@{A __universal morphism from $X$ to $F$<!-- LaTeX separator -->__}@} is {@{a unique pair $(A,u:X\to F(A))$ in ${\mathcal {D} }$}@} which has {@{the following property, commonly referred to as a __universal property__}@}:

For {@{any morphism of the form $f:X\to F(A')$ in ${\mathcal {D} }$}@}, there exists {@{a _unique_ morphism $h:A\to A'$ in ${\mathcal {C} }$ \(annotation: the uniqueness requirement is imposed on $h$, _not_ $F(h)$\) such that the following diagram [commutes](commutative%20diagram.md)}@}: <p> {@{![The typical diagram of the definition of a universal morphism.](../../archives/Wikimedia%20Commons/Universal%20morphism%20definition.svg)}@} <p> (annotation: To interpret this, we start with {@{interpreting the functor $F$}@}. The functor {@{"embeds" the category $\mathcal C$ into $\mathcal D$}@}. \(annotation: Note that functors are {@{not required to be injective or surjective}@}.\) Now consider {@{an object mapped to by the functor, $F(A)$}@}. The object has {@{classes of morphisms to all objects mapped to by the same functor, e.g. $F(A)$, $F(A')$}@}. Then the universal morphism is saying that {@{the object $X$ in $\mathcal D$, which may or may not be mapped to by $F$}@}, can {@{"take place" in the role of $F(A)$ in the "embedding" of $\mathcal C$ in $\mathcal D$ via $F$}@} by {@{right composing with the morphism $u$}@}, since $X$ has {@{classes of morphisms to all objects mapped to by $F$ that are "structurally" the same as that for $F(A)$}@}. <p> Given {@{a functor $F: \mathcal C \to \mathcal D$, its source and target categories}@}, and {@{any object $X$ in $\mathcal D$}@}, we can _try_ to {@{repeat the above construction}@} by choosing {@{any other object mapped to by $F$ and then any other morphism from $X$ to said object}@}. This explains why an universal morphism is {@{defined using a pair $(A, u: X \to F(A))$}@}. But as we will see below, {@{this pair, if it exists}@}, is actually {@{_unique_ up to an _unique_ isomorphism}@}, but {@{the object itself}@} is {@{only _unique_ up to \(not necessarily _unique_\) isomorphism}@}, giving another reason for {@{defining an universal morphism using a pair}@}.)

We can {@{[dualize](dual%20(category%20theory).md) this categorical concept}@}. {@{A __universal morphism from $F$ to $X$<!-- LaTeX separator -->__}@} is {@{a unique pair $(A,u:F(A)\to X)$ that satisfies the following universal property}@}:

For {@{any morphism of the form $f:F(A')\to X$ in ${\mathcal {D} }$}@}, there {@{exists a _unique_ morphism $h:A'\to A$ in ${\mathcal {C} }$ (annotation: the uniqueness requirement is imposed on $h$, _not_ $F(h)$) such that the following diagram commutes}@}: <p> {@{![The most important arrow here is $u: F(A) \to X$ which establishes the universal property.](../../archives/Wikimedia%20Commons/Universal%20definition%20dualized.svg)}@} <p> (annotation: The dual concept has {@{an intuition analogous to that for the above}@}.)

Note that {@{in each definition, the arrows are reversed}@}. Both definitions are {@{necessary to describe universal constructions which appear in mathematics}@}; but they also {@{arise due to the inherent duality present in category theory}@}. In either case, we say that {@{the pair $(A,u)$ which behaves as above satisfies a universal property}@}.

## connection with comma categories

Universal morphisms can be {@{described more concisely as initial and terminal objects in a [comma category](comma%20category.md)}@} \(i.e. one where {@{morphisms are seen as objects in their own right}@}\).

Let {@{$F:{\mathcal {C} }\to {\mathcal {D} }$ be a functor and $X$ an object of ${\mathcal {D} }$}@}. Then recall that {@{the comma category $(X\downarrow F)$ is the category where (annotation: $X$, more accurately, should be the selection functor from __1__ to $\mathcal D$, mapping the only object in __1__ to $X$)}@}

- (annotation: $(X \downarrow F)$, object) ::@:: Objects are pairs of the form $(B,f:X\to F(B))$, where $B$ is an object in ${\mathcal {C} }$
- (annotation: $(X \downarrow F)$, morphism) ::@:: A morphism from $(B,f:X\to F(B))$ to $(B',f':X\to F(B'))$ is given by a morphism $h:B\to B'$ in ${\mathcal {C} }$ such that the diagram commutes: <p> ![A morphism in the comma category is given by the morphism $h: B \to B'$ which also makes the diagram commute.](../../archives/Wikimedia%20Commons/Definition%20of%20a%20morphism%20in%20a%20comma%20category.svg)

Now suppose that {@{the object $(A,u:X\to F(A))$ in $(X\downarrow F)$ is initial}@}. Then for {@{every object $(A',f:X\to F(A'))$, there exists a unique morphism $h:A\to A'$ (annotation: this is from the definition of initial object) such that the following diagram commutes. <p> ![This demonstrates the connection between a universal diagram being an initial object in a comma category.](../../archives/Wikimedia%20Commons/Connection%20between%20universal%20diagrams%20and%20comma%20categories.svg)}@} <p> Note that {@{the equality here simply means the diagrams are the same}@}. Also note that {@{the diagram on the right side of the equality}@} is {@{the exact same as the one offered in defining a __universal morphism from $X$ to $F$<!-- LaTeX separator -->__}@}. Therefore, we see that {@{a universal morphism from $X$ to $F$ is equivalent to an initial object in the comma category $(X\downarrow F)$}@}.

Conversely, recall that {@{the comma category $(F\downarrow X)$ is the category (annotation: $X$, more accurately, should be the selection functor from __1__ to $\mathcal D$, mapping the only object in __1__ to $X$)}@} where

- (annotation: $(F \downarrow X)$, object) ::@:: Objects are pairs of the form $(B,f:F(B)\to X)$ where $B$ is an object in ${\mathcal {C} }$
- (annotation: $(F \downarrow X)$, morphism) ::@:: A morphism from $(B,f:F(B)\to X)$ to $(B',f':F(B')\to X)$ is given by a morphism $h:B\to B'$ in ${\mathcal {C} }$ such that the diagram commutes: <p> ![This simply demonstrates the definition of a morphism in a comma category.](../../archives/Wikimedia%20Commons/Definition%20of%20a%20morphism%20in%20a%20comma%20category%201.svg)

Suppose {@{$(A,u:F(A)\to X)$ is a terminal object in $(F\downarrow X)$}@}. Then for {@{every object $(A',f:F(A')\to X)$, there exists a unique morphism $h:A'\to A$ (annotation: this is from the definition of terminal object) such that the following diagrams commute. <p> ![This shows that a terminal object in a specific comma category corresponds to a universal morphism.](../../archives/Wikimedia%20Commons/Connection%20between%20comma%20category%20and%20universal%20properties.svg)}@} <p> The diagram on the right side of the equality is {@{the same diagram pictured when defining a __universal morphism from $F$ to $X$<!-- LaTeX separator -->__}@}. Hence, {@{a universal morphism from $F$ to $X$ corresponds with a terminal object in the comma category $(F\downarrow X)$}@}.

## examples

Below are {@{a few examples, to highlight the general idea}@}. The reader can {@{construct numerous other examples by consulting the articles mentioned in the introduction}@}.

### tensor algebras

Let ${\mathcal {C} }$ be {@{the [category of vector spaces](category%20of%20vector%20spaces.md) __<!-- LaTeX separator -->$K$<!-- LaTeX separator -->-Vect__ over a [field](field%20(mathematics).md) $K$}@} and let ${\mathcal {D} }$ be {@{the category of [algebras](algebra%20over%20a%20field.md) __<!-- LaTeX separator -->$K$<!-- LaTeX separator -->-Alg__ over $K$ \(assumed to be [unital](unital%20algebra.md#unital%20algebra) and [associative](associative%20algebra.md)\)}@}. Let <p> &emsp; {@{$U$ : __<!-- LaTeX separator -->$K$<!-- LaTeX separator -->-Alg__ → __<!-- LaTeX separator -->$K$<!-- LaTeX separator -->-Vect__ (annotation: the direction is reversed, from $\mathcal D$ to $\mathcal C$)}@} <p> be {@{the [forgetful functor](forgetful%20functor.md) which assigns to each algebra its underlying vector space}@}.

Given {@{any [vector space](vector%20space.md) $V$ over $K$}@} we can {@{construct the [tensor algebra](tensor%20algebra.md) $T(V)$}@}. \(annotation: As we will see below, $T$ can be treated as {@{a functor from $\mathcal C \equiv \mathbf{Vect}_K$ to $\mathcal D \equiv \mathbf{Alg}_K$}@}\) The tensor algebra is {@{characterized by the fact}@}:

> "{@{Any linear map from $V$ to an algebra $A$ (annotation: a morphism $f: V \to U(A)$ in $\mathcal C \equiv \mathbf{Vect}_K$)}@} can be {@{uniquely extended to (annotation: this act of extension is $u: V \to U(T(V))$ in $\mathcal C \equiv \mathbf {Vect}_K$, part of a universal morphism)}@} {@{an [algebra homomorphism](algebra%20homomorphism.md#algebra%20homomorphisms) from $T(V)$ to $A$ (annotation: an unique morphism $h: T(V) \to A$ in $\mathcal D \equiv \mathbf{Alg}_K$, mapped by $U$ to a morphism $U(h): U(T(V)) \to U(A)$ in $\mathcal C \equiv \mathbf{Vect}_K$)}@}."

This statement is {@{an initial property of the tensor algebra}@} since it expresses the fact that {@{the pair $(T(V),i)$, where $i:V\to U(T(V))$ is the inclusion map (annotation: noting $i$ is $u$ above, part of a universal morphism)}@}, is {@{a universal morphism (annotation: the first definition given above) from the vector space $V$ to the functor $U$}@}.

Since {@{this construction works for any vector space $V$}@}, we conclude that {@{$T$ is a functor from __<!-- LaTeX separator -->$K$<!-- LaTeX separator -->-Vect__ to __<!-- LaTeX separator -->$K$<!-- LaTeX separator -->-Alg__}@}. This means that $T$ is {@{_left adjoint_ to the forgetful functor $U$ \(see the section below on [relation to adjoint functors](#relation%20to%20adjoint%20functors)\)}@}.

### products

{@{A [categorical product](categorical%20product.md)}@} can be {@{characterized by a universal construction}@}. For {@{concreteness}@}, one may consider {@{the [Cartesian product](Cartesian%20product.md) in __[Set](set%20(category%20theory).md)__, the [direct product](direct%20product.md) in __[Grp](grp%20(category%20theory).md)__, or the [product topology](product%20topology.md) in __[Top](top%20(category%20theory).md)__}@}, where {@{products exist}@}.

Let {@{$X$ and $Y$ be objects of a category ${\mathcal {C} }$ with finite products}@}. {@{The product of $X$ and $Y$}@} is {@{an object $X$ × $Y$ together with two morphisms $$\begin{aligned} & \pi _{1} : X\times Y\to X \\ & \pi _{2} : X\times Y\to Y \end{aligned}$$}@} such that {@{for any other object $Z$ of ${\mathcal {C} }$ and (annotation: pair of) morphisms $f:Z\to X$ and $g:Z\to Y$ there exists a unique morphism $h:Z\to X\times Y$ such that $f=\pi _{1}\circ h$ and $g=\pi _{2}\circ h$}@}.

To {@{understand this characterization as a universal property}@}, take {@{the category ${\mathcal {D} }$ to be the [product category](product%20category.md) ${\mathcal {C} }\times {\mathcal {C} }$}@} and define {@{the [diagonal functor](diagonal%20functor.md) $$\Delta :{\mathcal {C} }\to {\mathcal {C} }\times {\mathcal {C} }$$}@} by {@{$\Delta (X)=(X,X)$ and $\Delta (f:X\to Y)=(f,f)$}@}. Then {@{$(X\times Y,(\pi _{1},\pi _{2}))$ is a universal morphism (annotation: the second definition given above) from $\Delta$ to the object $(X,Y)$ of ${\mathcal {C} }\times {\mathcal {C} }$}@}: if {@{$(f,g)$ is any morphism from $(Z,Z)$ to $(X,Y)$ (annotation: the pair of morphisms above become an actual pair)}@}, then it {@{must equal a unique morphism $\Delta (h:Z\to X\times Y)=(h,h)$ from $\Delta (Z)=(Z,Z)$ to $\Delta (X\times Y)=(X\times Y,X\times Y)$ followed by $(\pi _{1},\pi _{2})$}@}. As a commutative diagram: <p> {@{![Commutative diagram showing how products have a universal property.](../../archives/Wikimedia%20Commons/Universal-property-products.svg)}@} <p> (annotation: Compare it with {@{the commutative diagram for the product of two objects in the original category}@}. You can see {@{by "folding in half" the "triangle" of said commutative diagram, you get the above commutative diagram}@}.)

For the example of {@{the Cartesian product in __Set__}@}, the morphism $(\pi _{1},\pi _{2})$ comprises {@{the two projections $\pi _{1}(x,y)=x$ and $\pi _{2}(x,y)=y$}@}. Given {@{any set $Z$ and functions $f,g$}@} {@{the unique map such that the required diagram commutes}@} is given by {@{$h=\langle x,y\rangle (z)=(f(z),g(z))$ (annotation: that is, evaluating the two functions $f, g$ on the same element $z$ and returning them as a pair)}@}.<sup>[\[3\]](#^ref-3)</sup>

### limits and colimits

{@{Categorical products}@} are {@{a particular kind of [limit](limit%20(category%20theory).md) in category theory}@}. One can {@{generalize the above example to arbitrary limits and colimits}@}.

Let {@{${\mathcal {J} }$ and ${\mathcal {C} }$ be categories with ${\mathcal {J} }$ a [small](small%20category.md#small%20and%20large%20categories) [index category](index%20category.md)}@} (annotation: In the case of products, {@{$\mathcal J$ is a discrete category, consisting of exactly two objects and the two identity morphisms}@}.) and let {@{${\mathcal {C} }^{\mathcal {J} }$ be the corresponding [functor category](functor%20category.md)}@}. {@{The _[diagonal functor](diagonal%20functor.md)_ $$\Delta :{\mathcal {C} }\to {\mathcal {C} }^{\mathcal {J} }$$}@} is the functor that maps {@{each object $N$ in ${\mathcal {C} }$ to the constant functor $\Delta (N):{\mathcal {J} }\to {\mathcal {C} }$ \(i.e. $\Delta (N)(X)=N$ for each $X$ in ${\mathcal {J} }$ and $\Delta (N)(f)=1_{N}$ for each $f:X\to Y$ in ${\mathcal {J} }$\)}@} and {@{each morphism $f:N\to M$ in ${\mathcal {C} }$ to the natural transformation $\Delta (f):\Delta (N)\to \Delta (M)$ in ${\mathcal {C} }^{\mathcal {J} }$}@} defined as, {@{for every object $X$ of ${\mathcal {J} }$, the component $$\Delta (f)(X):\Delta (N)(X)\to \Delta (M)(X)=f:N\to M$$ at $X$}@}. In other words, the natural transformation is the one defined by {@{having constant component $f:N\to M$ for every object of ${\mathcal {J} }$}@}.

Given {@{a functor $F:{\mathcal {J} }\to {\mathcal {C} }$ \(thought of as an object in ${\mathcal {C} }^{\mathcal {J} }$\)}@}, {@{the _limit_ of $F$}@}, {@{if it exists, is nothing but a universal morphism from $\Delta$ to $F$}@}. (annotation: In the case of products, {@{the functor $F: \mathcal J \to \mathcal C$ maps from the discrete category $\mathcal J$, consisting of exactly two objects and the two identity morphisms}@}. Clearly this {@{indexes a pair of objects (may be the same) in $\mathcal C$}@}.) Dually, {@{the _colimit_ of $F$ is a universal morphism from $F$ to $\Delta$}@}.

## properties

### existence and uniqueness

Defining {@{a quantity does not guarantee its existence}@}. Given {@{a functor $F:{\mathcal {C} }\to {\mathcal {D} }$ and an object $X$ of ${\mathcal {D} }$}@}, there {@{may or may not exist a universal morphism from $X$ to $F$}@}. If, however, {@{a universal morphism $(A,u)$ does exist}@}, then {@{it is essentially unique}@}. Specifically, it is {@{unique [up to](up%20to.md) a _unique_ [isomorphism](isomorphism.md)}@}: if {@{$(A',u')$ is another pair, then there exists a unique isomorphism $k:A\to A'$ such that $u'=F(k)\circ u$}@}. This is easily seen by {@{substituting $(A,u')$ in the definition of a universal morphism}@}.

It is {@{the pair $(A,u)$ which is essentially unique in this fashion}@}. {@{The object $A$ itself}@} is {@{only unique up to isomorphism}@}. Indeed, if {@{$(A,u)$ is a universal morphism and $k:A\to A'$ is any isomorphism}@} then {@{the pair $(A',u')$, where $u'=F(k)\circ u$ is also a universal morphism}@}.

### equivalent formulations

{@{The definition of a universal morphism}@} can be {@{rephrased in a variety of ways}@}. Let {@{$F:{\mathcal {C} }\to {\mathcal {D} }$ be a functor and let $X$ be an object of ${\mathcal {D} }$}@}. Then the following statements are equivalent: (annotation: they are respectively related to {@{universal morphism, comma category, representable functor}@})

- (annotation: universal morphism) ::@:: $(A,u)$ is a universal morphism from $X$ to $F$
- (annotation: comma category) ::@:: $(A,u)$ is an [initial object](initial%20object.md) of the [comma category](comma%20category.md) $(X\downarrow F)$
- (annotation: representable functor $\text{Hom}_{\mathcal C}(A, -) \to \text{Hom}_{\mathcal D}(X, F(-))$) ::@:: $(A,F(\bullet )\circ u)$ is a [representation](representable%20functor.md) of ${\text{Hom} }_{\mathcal {D} }(X,F(-))$, where its components $(F(\bullet )\circ u)_{B}:{\text{Hom} }_{\mathcal {C} }(A,B)\to {\text{Hom} }_{\mathcal {D} }(X,F(B))$ are defined by $$(F(\bullet )\circ u)_{B}(f:A\to B):X\to F(B)=F(f)\circ u:X\to F(B)$$ for each object $B$ in ${\mathcal {C} }$.

The dual statements are {@{also equivalent}@}: (annotation: they are respectively related to {@{universal morphism, comma category, representable functor}@})

- (annotation: universal morphism, dual) ::@:: $(A,u)$ is a universal morphism from $F$ to $X$
- (annotation: comma category, dual) ::@:: $(A,u)$ is a [terminal object](terminal%20object.md) of the comma category $(F\downarrow X)$
- (annotation: representable functor $\text{Hom}_{\mathcal C}(-, A) \to \text{Hom}_{\mathcal D}(F(-), X)$) ::@:: $(A,u\circ F(\bullet ))$ is a representation of ${\text{Hom} }_{\mathcal {D} }(F(-),X)$, where its components $(u\circ F(\bullet ))_{B}:{\text{Hom} }_{\mathcal {C} }(B,A)\to {\text{Hom} }_{\mathcal {D} }(F(B),X)$ are defined by $$(u\circ F(\bullet ))_{B}(f:B\to A):F(B)\to X=u\circ F(f):F(B)\to X$$ for each object $B$ in ${\mathcal {C} }$.

### relation to adjoint functors

Suppose {@{$(A_{1},u_{1})$ is a universal morphism from $X_{1}$ to $F$ and $(A_{2},u_{2})$ is a universal morphism from $X_{2}$ to $F$}@}. By {@{the universal property of universal morphisms, given any morphism $h:X_{1}\to X_{2}$}@} there {@{exists a unique morphism $g:A_{1}\to A_{2}$ such that the following diagram commutes: <p> ![Universal morphisms can behave like a natural transformation between functors under suitable conditions.](../../archives/Wikimedia%20Commons/Connection%20between%20universal%20elements%20inducing%20a%20functor.svg)}@} <p> If {@{_every_ object $X_{i}$ of ${\mathcal {D} }$ admits a universal morphism to $F$}@}, then {@{the assignment $X_{i}\mapsto A_{i}$ and $h\mapsto g$ defines a functor $G:{\mathcal {D} }\to {\mathcal {C} }$}@}. {@{The maps <!-- $u_{i}$ -->$u_i: X_i \to F(A_i)$}@} then {@{define a [natural transformation](natural%20transformation.md) from $1_{\mathcal {D} }$ \(the identity functor on ${\mathcal {D} }$\) to $F\circ G$ (annotation: Noting the action of $F \circ G$ on any object in $\mathcal D$: $X_i \to A_i \to F(A_i)$.)}@}. The functors $(F,G)$ (annotation: the pair {@{ordering, i.e. $F$ is before $G$ in the pair, does not mean anything in this context}@}) are then {@{a pair of [adjoint functors](adjoint%20functor.md), with $G$ left-adjoint to $F$ and $F$ right-adjoint to $G$}@}.

Similar statements apply to {@{the dual situation of terminal morphisms from <!-- $F$ -->$F: \mathcal D \to \mathcal C$}@}. If {@{such morphisms exist for every $X$ in ${\mathcal {C} }$}@} one obtains {@{a functor $G:{\mathcal {C} }\to {\mathcal {D} }$}@} which is {@{right-adjoint to $F$ \(so $F$ is left-adjoint to $G$\)}@}. (annotation: Similarly, {@{the maps $u_i: F(A_i) \to X_i$}@} then {@{define a natural transformation from $F \circ G$ to $1_{\mathcal C}$, noting the action of $F \circ G$ on any object in $\mathcal C$: $X_i \to A_i \to F(A_i)$}@}.)

Indeed, {@{all pairs of adjoint functors arise from universal constructions in this manner}@}. Let {@{$F$ and $G$ be a pair of adjoint functors with unit $\eta$ and co-unit $\epsilon$}@} \(see the article on [adjoint functors](adjoint%20functors.md) for the definitions\). Then we have {@{a universal morphism for each object in ${\mathcal {C} }$ and ${\mathcal {D} }$}@}:

- For each object $X$ in ${\mathcal {C} }$, $(F(X),\eta _{X})$ is a universal morphism from $X$ to $G$. ::@:: That is, for all $f:X\to G(Y)$ there exists a unique $g:F(X)\to Y$ for which the following diagrams commute.
- For each object $Y$ in ${\mathcal {D} }$, $(G(Y),\epsilon _{Y})$ is a universal morphism from $F$ to $Y$. ::@:: That is, for all $g:F(X)\to Y$ there exists a unique $f:X\to G(Y)$ for which the following diagrams commute.

&emsp; {@{![The unit and counit of an adjunction, which are natural transformations between functors, are an important example of universal morphisms.](../../archives/Wikimedia%20Commons/Universal%20morphisms%20appear%20as%20the%20unit%20and%20counit%20of%20adjunctions.svg)}@} (annotation: {@{commutative diagrams for left-adjoint functor $F$, right-adjoint functor $G$, unit $\eta$, and co-unit $\varepsilon$}@})

Universal constructions (annotation: i.e. universal properties) are {@{more general than adjoint functor pairs}@}: a universal construction is {@{like an optimization problem}@}; it {@{gives rise to an adjoint pair}@} {@{if and only if this problem has a solution for every object of ${\mathcal {C} }$ \(equivalently, every object of ${\mathcal {D} }$\)}@}.

## history

{@{Universal properties of various topological constructions}@} were {@{presented by [Pierre Samuel](Pierre%20Samuel.md) in 1948}@}. They were later used {@{extensively by [Bourbaki](Nicolas%20Bourbaki.md)}@}. {@{The closely related concept of adjoint functors}@} was {@{introduced independently by [Daniel Kan](Daniel%20Kan.md) in 1958}@}.

## see also

> __![icon](../../archives/Wikimedia%20Commons/Nuvola%20apps%20edu%20mathematics%20blue-p.svg) [Mathematics portal](https://en.wikipedia.org/wiki/Portal:Mathematics)__

- [Free object](free%20object.md)
- [Natural transformation](natural%20transformation.md)
- [Adjoint functor](adjoint%20functor.md)
- [Monad \(category theory\)](monad%20(category%20theory).md)
- [Variety of algebras](variety%20of%20algebras.md)
- [Cartesian closed category](Cartesian%20closed%20category.md)

## notes

1. Jacobson \(2009\), Proposition 1.6, p. 44. <a id="^ref-1"></a>^ref-1
2. See for example, Polcino & Sehgal \(2002\), p. 133. exercise 1, about the universal property of [group rings](group%20ring.md). <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFFongSpivak2018"></a> Fong, Brendan; Spivak, David I. \(2018-10-12\). "Seven Sketches in Compositionality: An Invitation to Applied Category Theory". [arXiv](ArXiv%20(identifier).md):[1803.05316](https://arxiv.org/abs/1803.05316) \[[math.CT](https://arxiv.org/archive/math.CT)\]. <a id="^ref-3"></a>^ref-3

## references

This text incorporates [content](https://en.wikipedia.org/wiki/universal_property) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- [Paul Cohn](Paul%20Cohn.md), _Universal Algebra_ \(1981\), D.Reidel Publishing, Holland. [ISBN](ISBN%20(identifier).md) [90-277-1213-1](https://en.wikipedia.org/wiki/Special:BookSources/90-277-1213-1).
- <a id="CITEREFMac Lane1998"></a> [Mac Lane, Saunders](Saunders%20Mac%20Lane.md) \(1998\). _Categories for the Working Mathematician_. Graduate Texts in Mathematics 5 \(2nd ed.\). Springer. [ISBN](ISBN%20(identifier).md) [0-387-98403-8](https://en.wikipedia.org/wiki/Special:BookSources/0-387-98403-8).
- Borceux, F. _Handbook of Categorical Algebra: vol 1 Basic category theory_ \(1994\) Cambridge University Press, \(Encyclopedia of Mathematics and its Applications\) [ISBN](ISBN%20(identifier).md) [0-521-44178-1](https://en.wikipedia.org/wiki/Special:BookSources/0-521-44178-1)
- N. Bourbaki, _Livre II : Algèbre_ \(1970\), Hermann, [ISBN](ISBN%20(identifier).md) [0-201-00639-1](https://en.wikipedia.org/wiki/Special:BookSources/0-201-00639-1).
- Milies, César Polcino; Sehgal, Sudarshan K.. _An introduction to group rings_. Algebras and applications, Volume 1. Springer, 2002. [ISBN](ISBN%20(identifier).md) [978-1-4020-0238-0](https://en.wikipedia.org/wiki/Special:BookSources/978-1-4020-0238-0)
- Jacobson. Basic Algebra II. Dover. 2009. [ISBN](ISBN%20(identifier).md) [0-486-47187-X](https://en.wikipedia.org/wiki/Special:BookSources/0-486-47187-X)

## external links

- [nLab](http://ncatlab.org/nlab), a wiki project on mathematics, physics and philosophy with emphasis on the _n_-categorical point of view
- [André Joyal](André%20Joyal.md), [CatLab](http://ncatlab.org/nlab), a wiki project dedicated to the exposition of categorical mathematics
- <a id="CITEREFHillman2001"></a> Hillman, Chris \(2001\). _A Categorical Primer_. [CiteSeerX](CiteSeerX%20(identifier).md) [10.1.1.24.3264](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.24.3264): formal introduction to category theory.
- J. Adamek, H. Herrlich, G. Stecker, [Abstract and Concrete Categories-The Joy of Cats](http://katmat.math.uni-bremen.de/acc/acc.pdf)
- [Stanford Encyclopedia of Philosophy](Stanford%20Encyclopedia%20of%20Philosophy.md): "[Category Theory](http://plato.stanford.edu/entries/category-theory/)"—by Jean-Pierre Marquis. Extensive bibliography.
- [List of academic conferences on category theory](http://www.mta.ca/~cat-dist/)
- Baez, John, 1996,"[The Tale of _n_-categories.](http://math.ucr.edu/home/baez/week73.html)" An informal introduction to higher order categories.
- [WildCats](http://wildcatsformma.wordpress.com/) is a category theory package for [Mathematica](Mathematica.md). Manipulation and visualization of objects, [morphisms](morphism.md), categories, [functors](functor.md), [natural transformations](natural%20transformation.md), [universal properties](universal%20properties.md).
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

<!-- markdownlint MD028 -->

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Category theory](https://en.wikipedia.org/wiki/Category:Category%20theory)
> - [Mathematical terminology](https://en.wikipedia.org/wiki/Category:Mathematical%20terminology)
