---
aliases:
  - difference kernel
  - difference kernels
  - equaliser
  - equaliser (mathematics)
  - equalisers
  - equalizer
  - equalizer (mathematics)
  - equalizers
tags:
  - flashcard/active/general/eng/equaliser__mathematics_
  - language/in/English
---

# equaliser

<!-- | ![](../../archives/Wikimedia%20Commons/Question%20book-new.svg) | This article __needs additional citations for [verification](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)__. Please help [improve this article](https://en.wikipedia.org/wiki/Special:EditPage/Equaliser%20%28mathematics%29) by [adding citations to reliable sources](https://en.wikipedia.org/wiki/Help:Referencing%20for%20beginners). Unsourced material may be challenged and removed._Find sources:_ ["Equaliser" mathematics](https://www.google.com/search?as_eq=wikipedia&q=%22Equaliser%22+mathematics) – [news](https://www.google.com/search?tbm=nws&q=%22Equaliser%22+mathematics+-wikipedia&tbs=ar:1) __·__ [newspapers](https://www.google.com/search?&q=%22Equaliser%22+mathematics&tbs=bkt:s&tbm=bks) __·__ [books](https://www.google.com/search?tbs=bks:1&q=%22Equaliser%22+mathematics+-wikipedia) __·__ [scholar](https://scholar.google.com/scholar?q=%22Equaliser%22+mathematics) __·__ [JSTOR](https://www.jstor.org/action/doBasicSearch?Query=%22Equaliser%22+mathematics&acc=on&wc=on) _\(August 2024\)__\([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ | -->

In {@{[mathematics](mathematics.md)}@}, {@{an __equaliser__}@} is {@{a set of arguments where two or more [functions](function%20(mathematics).md) have [equal](equality%20(math).md) values}@}. An equaliser is {@{the [solution set](solution%20set.md) of an [equation](equation.md)}@}. In {@{certain contexts}@}, {@{a __difference kernel__ is the equaliser of exactly two functions}@}.

## definitions

Let {@{_X_ and _Y_ be [sets](set%20(mathematics).md)}@}. Let {@{_f_ and _g_ be [functions](function%20(mathematics).md), both from _X_ to _Y_}@}. Then {@{the _equaliser_ of _f_ and _g_}@} is {@{the set of elements _x_ of _X_ such that _f_\(_x_\) equals _g_\(_x_\) in _Y_}@}. Symbolically: {@{$$\operatorname {Eq} (f,g):=\{x\in X\mid f(x)=g(x)\}.$$}@} The equaliser may be denoted {@{Eq\(_f_, _g_\) or a variation on that theme \(such as with lowercase letters "eq"\)}@}. In informal contexts, {@{the notation {_f_ = _g_} is common}@}.

The definition above {@{used two functions _f_ and _g_}@}, but {@{there is no need to restrict to only two functions, or even to only [finitely](finite%20set.md) many functions}@}. In general, if {@{__F__ is a [set](set%20(mathematics).md) of functions from _X_ to _Y_}@}, then {@{the _equaliser_ of the members of __F__}@} is {@{the set of elements _x_ of _X_ such that, given any two members _f_ and _g_ of __F__, _f_\(_x_\) equals _g_\(_x_\) in _Y_}@}. Symbolically: {@{$$\operatorname {Eq} ({\mathcal {F} }):=\{x\in X\mid \forall f,g\in {\mathcal {F} },\;f(x)=g(x)\}.$$}@} This equaliser may be written as {@{Eq\(_f_, _g_, _h_, ...\) if ${\mathcal {F} }$ is the set {_f_, _g_, _h_, ...}<!-- flashcard separator -->}@}. In the latter case, one may also {@{find {_f_ = _g_ = _h_ = ···}<!-- flashcard separator -->}@} in informal contexts.

As {@{a [degenerate](degenerate%20(math).md) case of the general definition}@}, let {@{__F__ be a [singleton](singleton%20(set%20theory).md) {_f_}<!-- flashcard separator -->}@}. Since {@{_f_\(_x_\) always equals itself}@}, {@{the equaliser must be the entire domain _X_}@}. As {@{an even more degenerate case}@}, let {@{__F__ be the [empty set](empty%20set.md)}@}. Then {@{the equaliser is again the entire domain _X_}@}, since {@{the [universal quantification](universal%20quantification.md) in the definition is [vacuously true](vacuously%20true.md)}@}.

## difference kernels

{@{A binary equaliser \(that is, an equaliser of just two functions\)}@} is also called {@{a _difference kernel_}@}. This may also be denoted {@{DiffKer\(_f_, _g_\), Ker\(_f_, _g_\), or Ker\(_f_ − _g_\)}@}. The last notation shows {@{where this terminology comes from, and why it is most common in the context of [abstract algebra](abstract%20algebra.md)}@}: {@{The difference kernel of _f_ and _g_ is simply the [kernel](kernel%20(algebra).md) of the difference _f_ − _g_}@}. Furthermore, {@{the kernel of a single function _f_}@} can be {@{reconstructed as the difference kernel Eq\(_f_, 0\)}@}, where {@{0 is the [constant function](constant%20function.md) with value [zero](0%20(number).md)}@}.

Of course, all of this presumes {@{an algebraic context where the kernel of a function is the [preimage](preimage.md#inverse%20image) of zero under that function}@}; that is {@{not true in all situations}@}. However, {@{the terminology "difference kernel" has no other meaning}@}.

## in category theory

Equalisers can be defined by {@{a [universal property](universal%20property.md)}@}, which allows {@{the notion to be generalised from the [category of sets](category%20of%20sets.md) to arbitrary [categories](category%20theory.md)}@}.

In the general context, {@{_X_ and _Y_ are objects}@}, while {@{_f_ and _g_ are morphisms from _X_ to _Y_}@}. These {@{objects and morphisms}@} form {@{a [diagram](commutative%20diagram.md) in the category in question}@}, and the equaliser is {@{simply the [limit](limit%20(category%20theory).md) of that diagram}@}.

In more explicit terms, the equaliser consists of {@{an object _E_ and a morphism _eq_ : _E_ → _X_ satisfying $f\circ eq=g\circ eq$}@}, and such that, given {@{any object _O_ and morphism _m_ : _O_ → _X_, if $f\circ m=g\circ m$}@}, then there {@{exists a [unique](unique%20(mathematics).md) morphism _u_ : _O_ → _E_ such that $eq\circ u=m$}@}. {@{![commutative diagram for equalizer](../../archives/Wikimedia%20Commons/Equalizer-01.png)}@} {@{A morphism $m:O\rightarrow X$ is said to __equalise__ $f$ and $g$}@} if {@{$f\circ m=g\circ m$}@}.<sup>[\[1\]](#^ref-1)</sup>

In {@{any [universal algebraic](universal%20algebra.md) category}@}, including {@{the categories where difference kernels are used, as well as the category of sets itself}@}, the object _E_ {@{can always be taken to be the ordinary notion of equaliser}@}, and the morphism _eq_ can {@{in that case be taken to be the [inclusion function](inclusion%20function.md) of _E_ as a [subset](subset.md) of _X_}@}.

{@{The generalisation of this to more than two morphisms}@} is {@{straightforward}@}; simply {@{use a larger diagram with more morphisms in it}@}. {@{The degenerate case of only one morphism}@} is {@{also straightforward}@}; then {@{_eq_ can be any [isomorphism](isomorphism.md) from an object _E_ to _X_}@}.

{@{The correct diagram for the degenerate case with _no_ morphisms}@} is {@{slightly subtle}@}: one might {@{initially draw the diagram as consisting of the objects _X_ and _Y_ and no morphisms}@}. This is {@{incorrect}@}, however, since {@{the limit of such a diagram is the [product](product%20(category%20theory).md) of _X_ and _Y_, rather than the equaliser}@}. \(And indeed {@{products and equalisers are different concepts}@}: the set-theoretic definition of {@{product doesn't agree with the set-theoretic definition of the equaliser mentioned above}@}, hence {@{they are actually different}@}.\) Instead, {@{the appropriate insight}@} is that {@{every equaliser diagram is fundamentally concerned with _X_}@}, {@{including _Y_ only because _Y_ is the [codomain](codomain.md) of morphisms which appear in the diagram}@}. With this view, we see that if {@{there are no morphisms involved}@}, {@{_Y_ does not make an appearance and the equaliser diagram consists of _X_ alone}@}. {@{The limit of this diagram}@} is then {@{any isomorphism between _E_ and _X_}@}.

It can be proved that {@{any equaliser in any category is a [monomorphism](monomorphism.md)}@}. If {@{the [converse](converse%20(logic).md) holds in a given category}@}, then {@{that category is said to be _regular_ \(in the sense of monomorphisms\)}@}. More generally, {@{a [regular monomorphism](regular%20monomorphism.md#related%20concepts) in any category}@} is {@{any morphism _m_ that is an equaliser of some set of morphisms}@}. Some authors require {@{more strictly that _m_ be a _binary_ equaliser, that is an equaliser of exactly two morphisms}@}. However, if {@{the category in question is [complete](complete%20category.md)}@}, then {@{both definitions agree}@}.

{@{The notion of difference kernel}@} also makes sense in {@{a category-theoretic context}@}. {@{The terminology "difference kernel"}@} is {@{common throughout category theory for any binary equaliser}@}. In the case of {@{a [preadditive category](preadditive%20category.md) \(a category [enriched](enriched%20category.md) over the category of [Abelian groups](abelian%20group.md)\)}@}, the term "difference kernel" may be {@{interpreted literally, since subtraction of morphisms makes sense}@}. That is, {@{Eq\(_f_, _g_\) = Ker\(_f_ - _g_\)}@}, where {@{Ker denotes the [category-theoretic kernel](kernel%20(category%20theory).md)}@}.

Any category {@{with [fibre products](pullback%20(category%20theory).md) \(pullbacks\) and products}@} {@{has equalisers}@}.

## see also

- [Coequaliser](coequalizer.md), ::@:: the [dual](dual%20(category%20theory).md) notion, obtained by reversing the arrows in the equaliser definition.
- [Coincidence theory](coincidence%20theory.md), ::@:: a topological approach to equaliser sets in [topological spaces](topological%20space.md).
- [Pullback](pullback%20(category%20theory).md), ::@:: a special [limit](limit%20(category%20theory).md) that can be constructed from equalisers and products.

## notes

1. <a id="CITEREFBarrWells1998"></a> [Barr, Michael](Michael%20Barr%20(mathematician).md); [Wells, Charles](Charles%20Wells%20(mathematician).md) \(1998\). [_Category theory for computing science_](http://www.tac.mta.ca/tac/reprints/articles/22/tr22.pdf) \(PDF\). [Prentice Hall International Series in Computer Science](Prentice%20Hall%20International%20Series%20in%20Computer%20Science.md). p. 266. <a id="^ref-1"></a>^ref-1

## references

This text incorporates [content](https://en.wikipedia.org/wiki/equaliser_(mathematics)) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- [Equalizer](https://ncatlab.org/nlab/show/equalizer) at the [_n_<!-- markdown separator -->Lab](nLab.md)

## external links

- [Interactive Web page](https://web.archive.org/web/20080916162345/http://www.j-paine.org/cgi-bin/webcats/webcats.php)which generates examples of equalisers in the category of finite sets. Written by [Jocelyn Paine](https://web.archive.org/web/20081223001815/http://www.j-paine.org/).

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
> - [Set theory](https://en.wikipedia.org/wiki/Category:Set%20theory)
> - [Limits \(category theory\)](https://en.wikipedia.org/wiki/Category:Limits%20%28category%20theory%29)
