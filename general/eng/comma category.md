---
aliases:
  - comma categories
  - comma category
  - co-slice categories
  - co-slice category
  - coslice categories
  - coslice category
  - slice categories
  - slice category
tags:
  - flashcard/active/general/eng/comma_category
  - language/in/English
---

# comma category

<!-- | ![](../../archives/Wikimedia%20Commons/Text%20document%20with%20red%20question%20mark.svg) | This article includes a list of [general references](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources#General%20references), but __it lacks sufficient corresponding [inline citations](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources#Inline%20citations)__. Please help to [improve](https://en.wikipedia.org/wiki/Wikipedia:WikiProject%20Reliability) this article by [introducing](https://en.wikipedia.org/wiki/Wikipedia:When%20to%20cite) more precise citations. _\(March 2016\)__\([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ | -->

In {@{[mathematics](mathematics.md)}@}, {@{a __comma category__}@} \(a special case being {@{a __slice category__}@}\) is {@{a construction in [category theory](category%20theory.md)}@}. It provides {@{another way of looking at [morphisms](morphism.md)}@}: instead of {@{simply relating objects of a [category](category%20(mathematics).md) to one another}@}, morphisms {@{become objects in their own right}@}. {@{This notion was introduced}@} {@{in 1963 by [F. W. Lawvere](William%20Lawvere.md) \(Lawvere, 1963 p. 36\)}@}, although the technique {@{did not<sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup> become generally known until many years later}@}. {@{Several mathematical concepts}@} can be {@{treated as comma categories}@}. Comma categories also {@{guarantee the existence of some [limits](limit%20(category%20theory).md) and [colimits](colimit.md)}@}. The name comes from {@{the notation originally used by Lawvere}@}, which {@{involved the [comma](comma.md) punctuation mark}@}. The name {@{persists even though standard notation has changed}@}, since {@{the use of a comma as an operator is potentially confusing}@}, and even {@{Lawvere dislikes the uninformative term "comma category" \(Lawvere, 1963 p. 13\)}@}.

## definition

{@{The most general comma category construction}@} {@{involves two [functors](functor.md) with the same codomain}@}. Often {@{one of these will have domain __1__ \(the one-object one-morphism category\)}@}. {@{Some accounts of category theory}@} {@{consider only these special cases}@}, but the term comma category is {@{actually much more general}@}.

### general form

Suppose that {@{${\mathcal {A} }$, ${\mathcal {B} }$, and ${\mathcal {C} }$ are categories, and $S$ and $T$ \(for source and target\) are [functors](functor.md)}@}: {@{$${\mathcal {A} }{\xrightarrow {\;\;S\;\;} }{\mathcal {C} }{\xleftarrow {\;\;T\;\;} }{\mathcal {B} }$$}@} We can {@{form the comma category $(S\downarrow T)$}@} as follows:

- The objects ::@:: are all triples $(A,B,h)$ with $A$ an object in ${\mathcal {A} }$, $B$ an object in ${\mathcal {B} }$, and $h:S(A)\rightarrow T(B)$ a morphism in ${\mathcal {C} }$.
- The morphisms from $(A,B,h)$ to $(A',B',h')$ ::@:: are all pairs $(f,g)$ where $f:A\rightarrow A'$ and $g:B\rightarrow B'$ are morphisms in ${\mathcal {A} }$ and ${\mathcal {B} }$ respectively, such that the following diagram [commutes](commutative%20diagram.md): <p> &emsp; ![Comma Diagram](../../archives/Wikimedia%20Commons/Comma%20Diagram.svg)

{@{Morphisms are composed}@} by {@{taking $(f',g')\circ (f,g)$ to be $(f'\circ f,g'\circ g)$, whenever the latter expression is defined}@}. {@{The identity morphism on an object $(A,B,h)$}@} is {@{$(\mathrm {id} _{A},\mathrm {id} _{B})$}@}.

### slice category

- Main article: [Overcategory](overcategory.md)

{@{The first special case occurs}@} when {@{${\mathcal {C} }={\mathcal {A} }$, the functor $S$ is the [identity functor](identity%20functor.md#identity%20functor), and ${\mathcal {B} }={\textbf {1} }$ \(the category with one object $*$ and one morphism\)}@}. Then {@{$T(*)=A_{*}$ for some object $A_{*}$ in ${\mathcal {A} }$}@}. {@{$${\mathcal {A} }\xrightarrow {\;\;\mathrm {id} _{\mathcal {A} }\;\;} {\mathcal {A} }\xleftarrow {\;\;A_{*}\;\;} {\textbf {1} }$$}@} In this case, the comma category is written {@{$({\mathcal {A} }\downarrow A_{*})$}@}, and is often called {@{the _slice category_ over $A_{*}$ or the category of _objects over_ $A_{*}$}@}. {@{The objects $(A,*,h)$}@} can be {@{simplified to pairs $(A,h)$, where $h:A\rightarrow A_{*}$}@}. Sometimes, $h$ is denoted by {@{$\pi _{A}$}@}. {@{A morphism $(f,\mathrm {id} _{*})$ from $(A,\pi _{A})$ to $(A',\pi _{A'})$ in the slice category}@} can then be {@{simplified to an arrow $f:A\rightarrow A'$}@} making {@{the following diagram commute: <p> &emsp; ![Slice Diagram](../../archives/Wikimedia%20Commons/Slice%20Diagram.svg)}@}

### coslice category

- Main article: [Overcategory](overcategory.md)

{@{The [dual](dual%20(category%20theory).md) concept to a slice category}@} is {@{a coslice category}@}. Here, {@{${\mathcal {C} }={\mathcal {B} }$, $S$ has domain ${\textbf {1} }$ and $T$ is an identity functor}@}. {@{$${\textbf {1} }\xrightarrow {\;\;B_{*}\;\;} {\mathcal {B} }\xleftarrow {\;\;\mathrm {id} _{\mathcal {B} }\;\;} {\mathcal {B} }$$}@} In this case, the comma category is often written {@{$(B_{*}\downarrow {\mathcal {B} })$}@}, where {@{$B_{*}=S(*)$ is the object of ${\mathcal {B} }$ selected by $S$}@}. It is called {@{the _coslice category_ with respect to $B_{*}$, or the category of _objects under_ $B_{*}$}@}. The objects are {@{pairs $(B,\iota _{B})$ with $\iota _{B}:B_{*}\rightarrow B$}@}. Given {@{$(B,\iota _{B})$ and $(B',\iota _{B'})$}@}, {@{a morphism in the coslice category is a map $g:B\rightarrow B'$}@} making {@{the following diagram commute: <p> &emsp; ![Coslice Diagram](../../archives/Wikimedia%20Commons/Coslice%20Diagram.svg)}@}

### arrow category

$S$ and $T$ are {@{[identity functors](identity%20functor.md#identity%20functor) on ${\mathcal {C} }$ \(so ${\mathcal {A} }={\mathcal {B} }={\mathcal {C} }$\)}@}. {@{$${\mathcal {C} }\xrightarrow {\;\;\mathrm {id} _{\mathcal {C} }\;\;} {\mathcal {C} }\xleftarrow {\;\;\mathrm {id} _{\mathcal {C} }\;\;} {\mathcal {C} }$$}@} In this case, the comma category is {@{the arrow category ${\mathcal {C} }^{\rightarrow }$}@}. Its objects are {@{the morphisms of ${\mathcal {C} }$}@}, and its morphisms are {@{commuting squares in ${\mathcal {C} }$.<sup>[\[1\]](#^ref-1)</sup> <p> &emsp; ![Arrow Diagram](../../archives/Wikimedia%20Commons/Arrow%20Diagram.png)}@}

### other variations

In the case of {@{the slice or coslice category}@}, the identity functor {@{may be replaced with some other functor}@}; this yields {@{a family of categories particularly useful in the study of [adjoint functors](adjoint%20functor.md)}@}. For example, if {@{$T$ is the [forgetful functor](forgetful%20functor.md) mapping an [abelian group](abelian%20group.md) to its [underlying set](algebraic%20structure.md)}@}, and {@{$s$ is some fixed [set](set%20(mathematics).md) \(regarded as a functor from __1__\)}@}, then {@{the comma category $(s\downarrow T)$}@} has {@{objects that are maps from $s$ to a set underlying a group}@}. This relates to {@{the left adjoint of $T$}@}, which is {@{the functor that maps a set to the [free abelian group](free%20abelian%20group.md) having that set as its basis}@}. In particular, {@{the [initial object](initial%20object.md) of $(s\downarrow T)$}@} is {@{the canonical injection $s\rightarrow T(G)$, where $G$ is the free group generated by $s$}@}.

{@{An object of $(s\downarrow T)$}@} is called {@{a _morphism from $s$ to $T$<!-- LaTeX separator -->_ or a _<!-- LaTeX separator -->$T$-structured arrow with domain $s$<!-- LaTeX separator -->_}@}.<sup>[\[1\]](#^ref-1)</sup> {@{An object of $(S\downarrow t)$}@} is called {@{a _morphism from $S$ to $t$<!-- LaTeX separator -->_ or a _<!-- LaTeX separator -->$S$-costructured arrow with codomain $t$<!-- LaTeX separator -->_}@}.<sup>[\[1\]](#^ref-1)</sup>

Another special case occurs when {@{both $S$ and $T$ are functors with domain ${\textbf {1} }$}@}. If {@{$S(*)=A$ and $T(*)=B$}@}, then {@{the comma category $(S\downarrow T)$, written $(A\downarrow B)$}@}, is {@{the [discrete category](discrete%20category.md) whose objects are morphisms from $A$ to $B$}@}.

{@{An [inserter category](inserter%20category.md)}@} is {@{a \(non-full\) subcategory of the comma category where ${\mathcal {A} }={\mathcal {B} }$ and $f=g$ are required}@}. \(annotation: {@{The two functors}@} {@{have the same domain}@}. {@{Each morphism in the subcategory}@} has {@{the same morphism in the domain category as the two morphisms}@}.\) The comma category can also be seen as {@{the inserter of $S\circ \pi _{1}$ and $T\circ \pi _{2}$}@} \(annotation: {@{the two functors}@} have {@{the same domain $\mathcal A \times \mathcal B$ and codomain $\mathcal C$}@}\), where {@{$\pi _{1}$ and $\pi _{2}$ are the two projection functors out of the [product category](product%20category.md) ${\mathcal {A} }\times {\mathcal {B} }$}@}.

## properties

For {@{each comma category}@} there are {@{forgetful functors from it (annotation: they are the domain, codomain, and arrow functor)}@}.

- Domain functor, ::@:: $S\downarrow T\to {\mathcal {A} }$, which maps:
  - (annotation: domain functor) objects: ::@:: $(A,B,h)\mapsto A$;
  - (annotation: domain functor) morphisms: ::@:: $(f,g)\mapsto f$;
- Codomain functor, ::@:: $S\downarrow T\to {\mathcal {B} }$, which maps:
  - (annotation: codomain functor) objects: ::@:: $(A,B,h)\mapsto B$;
  - (annotation: codomain functor) morphisms: ::@:: $(f,g)\mapsto g$.
- Arrow functor, ::@:: $S\downarrow T\to {\mathcal {C} }^{\rightarrow }$, which maps:
  - (annotation: arrow functor) objects: ::@:: $(A,B,h)\mapsto h$;
  - (annotation: arrow functor) morphisms: ::@:: $(f,g)\mapsto (Sf,Tg)$;

## examples of use

### some notable categories

{@{Several interesting categories}@} have {@{a natural definition in terms of comma categories}@}.

- {@{The category of [pointed sets](pointed%20set.md)}@} is {@{a comma category, $\scriptstyle {(\bullet \downarrow \mathbf {Set} )}$ with $\scriptstyle {\bullet }$ being \(a functor selecting\) any [singleton set](singleton%20set.md), and $\scriptstyle {\mathbf {Set} }$ \(the identity functor of\) the [category of sets](category%20of%20sets.md)}@}. {@{Each object of this category}@} is {@{a set, together with a function selecting some element of the set: the "basepoint"}@}. {@{Morphisms}@} are {@{functions on sets which map basepoints to basepoints}@}. In a similar fashion one can form {@{the category of [pointed spaces](pointed%20space.md) $\scriptstyle {(\bullet \downarrow \mathbf {Top} )}$}@}.

- {@{The category of associative algebras over a ring $R$}@} is {@{the coslice category $\scriptstyle {(R\downarrow \mathbf {Ring} )}$}@}, since {@{any ring homomorphism $f:R\to S$ induces an associative $R$-algebra structure on $S$, and vice versa}@}. {@{Morphisms}@} are then {@{maps $h:S\to T$ that make the diagram commute}@}.

- {@{The category of [graphs](graph%20(discrete%20mathematics).md)}@} is {@{$\scriptstyle {(\mathbf {Set} \downarrow D)}$, with $\scriptstyle {D:\,\mathbf {Set} \rightarrow \mathbf {Set} }$ the functor taking a set $s$ to $s\times s$}@}. {@{The objects $(a,b,f)$}@} then {@{consist of two sets and a function}@}; {@{$a$ is an indexing set, $b$ is a set of nodes, and $f:a\rightarrow (b\times b)$ chooses pairs of elements of $b$ for each input from $a$}@}. That is, {@{$f$ picks out certain edges from the set $b\times b$ of possible edges}@}. {@{A morphism in this category}@} is {@{made up of two functions, one on the indexing set and one on the node set}@}. They must {@{"agree" according to the general definition above}@}, meaning that {@{$(g,h):(a,b,f)\rightarrow (a',b',f')$ must satisfy $f'\circ g=D(h)\circ f$}@}. In other words, {@{the edge corresponding to a certain element of the indexing set}@}, when translated, {@{must be the same as the edge for the translated index}@}.

- {@{Many "augmentation" or "labelling" operations}@} can be {@{expressed in terms of comma categories}@}. Let $S$ be {@{the functor taking each graph to the set of its edges}@}, and let $A$ be {@{\(a functor selecting\) some particular set}@}: then {@{$(S\downarrow A)$ is the category of graphs whose edges are labelled by elements of $A$}@}. This form of comma category is often called {@{_objects $S$-over $A$<!-- LaTeX separator -->_ - closely related to the "objects over $A$" discussed above}@}. Here, {@{each object}@} takes {@{the form $(B,\pi _{B})$, where $B$ is a graph and $\pi _{B}$ a function from the edges of $B$ to $A$}@}. {@{The nodes of the graph}@} could be {@{labelled in essentially the same way}@}.

- {@{A category is said to be _locally cartesian closed_}@} {@{if every slice of it is [cartesian closed](Cartesian%20closed.md) \(see above for the notion of _slice_\)}@}. {@{Locally cartesian closed categories}@} are {@{the [classifying categories](classifying%20category.md) of [dependent type theories](dependent%20type%20theory.md)}@}.

### limits and universal morphisms

{@{[Limits](limit%20(category%20theory).md) and [colimits](limit%20(category%20theory).md) in comma categories}@} {@{may be "inherited"}@}. If {@{${\mathcal {A} }$ and ${\mathcal {B} }$ are [complete](complete%20category.md), $T:{\mathcal {B} }\rightarrow {\mathcal {C} }$ is a [continuous functor](limit%20(category%20theory).md#preservation%20of%20limits), and $S\colon {\mathcal {A} }\rightarrow {\mathcal {C} }$ is another functor \(not necessarily continuous\)}@}, then {@{the comma category $(S\downarrow T)$ produced is complete,<sup>[\[2\]](#^ref-2)</sup> and the projection functors $(S\downarrow T)\rightarrow {\mathcal {A} }$ and $(S\downarrow T)\rightarrow {\mathcal {B} }$ are continuous}@}. Similarly, if {@{${\mathcal {A} }$ and ${\mathcal {B} }$ are cocomplete, and $S:{\mathcal {A} }\rightarrow {\mathcal {C} }$ is [cocontinuous](limit%20(category%20theory).md#preservation%20of%20limits)}@}, then {@{$(S\downarrow T)$ is cocomplete, and the projection functors are cocontinuous}@}.

For example, note that in {@{the above construction of the category of graphs as a comma category}@}, {@{the category of sets is complete and cocomplete}@}, and {@{the identity functor is continuous and cocontinuous}@}. Thus, {@{the category of graphs is complete and cocomplete}@}.

{@{The notion of a [universal morphism](universal%20property.md) to a particular colimit, or from a limit}@}, can be {@{expressed in terms of a comma category}@}. Essentially, we {@{create a category whose objects are cones, and where the limiting cone is a [terminal object](terminal%20object.md)}@}; then, {@{each universal morphism for the limit is just the morphism to the terminal object}@}. This works in {@{the dual case, with a category of cocones having an initial object}@}. For example, let ${\mathcal {C} }$ be {@{a category with $F:{\mathcal {C} }\rightarrow {\mathcal {C} }\times {\mathcal {C} }$ the functor taking each object $c$ to $(c,c)$ and each arrow $f$ to $(f,f)$ (annoation: diagonal functor for the coproduct)}@}. {@{A universal morphism from $(a,b)$ to $F$}@} consists, by definition, of {@{an object $(c,c)$ and morphism $\rho :(a,b)\rightarrow (c,c)$}@} with {@{the universal property that for any morphism $\rho ':(a,b)\rightarrow (d,d)$ there is a unique morphism $\sigma :c\rightarrow d$ with $F(\sigma )\circ \rho =\rho '$}@}. In other words, it is {@{an object in the comma category $((a,b)\downarrow F)$}@} having {@{a morphism to any other object in that category; it is initial}@}. This serves to {@{define the [coproduct](coproduct.md) in ${\mathcal {C} }$, when it exists}@}.

### adjunctions

{@{[William Lawvere](William%20Lawvere.md)}@} showed that {@{the functors $F:{\mathcal {C} }\rightarrow {\mathcal {D} }$ and $G:{\mathcal {D} }\rightarrow {\mathcal {C} }$ are [adjoint](adjoint%20functors.md)}@} {@{if and only if the comma categories $(F\downarrow id_{\mathcal {D} })$ and $(id_{\mathcal {C} }\downarrow G)$, with $id_{\mathcal {D} }$ and $id_{\mathcal {C} }$ the identity functors on ${\mathcal {D} }$ and ${\mathcal {C} }$ respectively, are isomorphic}@}, and {@{equivalent elements in the comma category can be projected onto the same element of ${\mathcal {C} }\times {\mathcal {D} }$}@}. This allows {@{adjunctions to be described without involving sets}@}, and was {@{in fact the original motivation for introducing comma categories}@}.

### natural transformations

If {@{the domains of $S,T$ are equal}@}, then {@{the diagram which defines morphisms in $S\downarrow T$ with $A=B,A'=B',f=g$}@} (annotation: the two objects in the comma category are {@{$(A, B, h) = (A, A, h)$ and $(A', B', h') = (A', A', h')$, and then $f = g$ forces $h$ and $h'$ to be respectively the component of the natural transformation at $A$ and $A'$}@}) is {@{identical to the diagram which defines a [natural transformation](natural%20transformation.md) $S\to T$}@}. {@{The difference between the two notions}@} is that {@{a natural transformation}@} is {@{a particular collection of morphisms of type of the form $S(A)\to T(A)$}@}, while {@{objects of the comma category}@} contains {@{_all_ morphisms of type of such form \(annotation: not just those in a natural transformation\)}@}. {@{A functor to the comma category}@} {@{selects that particular collection of morphisms}@}. This is {@{described succinctly by an observation by S.A. Huq}@}<sup>[\[3\]](#^ref-3)</sup> that {@{a natural transformation $\eta :S\to T$, with $S,T:{\mathcal {A} }\to {\mathcal {C} }$}@}, corresponds to {@{a functor ${\mathcal {A} }\to (S\downarrow T)$ which maps each object $A$ to $(A,A,\eta _{A})$ and maps each morphism $f=g$ to $(f,g)$}@}. This is {@{a [bijective](bijection.md) correspondence between natural transformations $S\to T$ and functors ${\mathcal {A} }\to (S\downarrow T)$}@} which are {@{[sections](section%20(category%20theory).md) of both forgetful functors \(annotation: domain functor, codomain functor\) from $S\downarrow T$}@}.

## references

This text incorporates [content](https://en.wikipedia.org/wiki/comma_category) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFAdámekHerrlichStrecker1990"></a> Adámek, Jiří; Herrlich, Horst; Strecker, George E. \(1990\). [_Abstract and Concrete Categories_](http://katmat.math.uni-bremen.de/acc/acc.pdf) \(PDF\). John Wiley & Sons. [ISBN](ISBN%20(identifier).md) [0-471-60922-6](https://en.wikipedia.org/wiki/Special:BookSources/0-471-60922-6). <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFRydheardBurstall1988"></a> Rydheard, David E.; Burstall, Rod M. \(1988\). [_Computational category theory_](http://www.cs.man.ac.uk/~david/categories/book/book.pdf) \(PDF\). Prentice Hall. <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFMac Lane1998"></a> [Mac Lane, Saunders](Saunders%20Mac%20Lane.md) \(1998\), _[Categories for the Working Mathematician](Categories%20for%20the%20Working%20Mathematician.md)_, Graduate Texts in Mathematics __5__ \(2nd ed.\), Springer-Verlag, p. 48, [ISBN](ISBN%20(identifier).md) [0-387-98403-8](https://en.wikipedia.org/wiki/Special:BookSources/0-387-98403-8) <a id="^ref-3"></a>^ref-3

- [Comma category](https://ncatlab.org/nlab/show/comma+category) at the [_n_<!-- markdown separator -->Lab](nLab.md)
- Lawvere, W \(1963\). "Functorial semantics of algebraic theories" and "Some algebraic problems in the context of functorial semantics of algebraic theories". [http://www.tac.mta.ca/tac/reprints/articles/5/tr5.pdf](http://www.tac.mta.ca/tac/reprints/articles/5/tr5.pdf)

## external links

- J. Adamek, H. Herrlich, G. Stecker, [Abstract and Concrete Categories-The Joy of Cats](http://katmat.math.uni-bremen.de/acc/acc.pdf)
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

> [Category](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Categories in category theory](https://en.wikipedia.org/wiki/Category:Categories%20in%20category%20theory)
