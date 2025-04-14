---
aliases:
  - dual
  - dual (category theory)
  - duality
  - duality (category theory)
tags:
  - flashcard/active/general/eng/dual__category_theory_
  - language/in/English
---

# dual

- For {@{general notions of duality in mathematics}@}, see {@{[Duality \(mathematics\)](duality%20(mathematics).md)}@}. <!--SR:!2026-01-22,294,330!2026-01-16,288,330-->

In {@{[category theory](category%20theory.md), a branch of [mathematics](mathematics.md)}@}, {@{__duality__}@} is {@{a correspondence between the properties of a category _C_ and the dual properties of the [opposite category](opposite%20category.md) _C_<sup>op</sup>}@}. Given {@{a statement regarding the category _C_}@}, by {@{interchanging the [source](domain%20of%20a%20function.md) and [target](codomain.md) of each [morphism](morphism.md) as well as interchanging the order of [composing](function%20composition.md) two morphisms}@}, {@{a corresponding dual statement is obtained regarding the opposite category _C_<sup>op</sup>}@}. Duality, as such, is the assertion that {@{truth is invariant under this operation on statements}@}. In other words, if {@{a statement is true about _C_}@}, then {@{its dual statement is true about _C_<sup>op</sup>}@}. Also, if {@{a statement is false about _C_}@}, then {@{its dual has to be false about _C_<sup>op</sup>}@}. <!--SR:!2026-01-18,290,330!2026-01-16,288,330!2026-01-15,287,330!2026-01-08,280,330!2026-01-09,281,330!2026-01-11,283,330!2025-09-28,197,310!2026-01-08,280,330!2026-01-13,285,330!2026-01-14,286,330!2026-01-19,291,330-->

Given {@{a [concrete category](concrete%20category.md) _C_}@}, it is often the case that {@{the opposite category _C_<sup>op</sup> per se is abstract}@}. _C_<sup>op</sup> need not be {@{a category that arises from mathematical practice}@}. In this case, {@{another category _D_ is also termed to be in duality with _C_}@} if {@{_D_ and _C_<sup>op</sup> are [equivalent as categories](equivalence%20of%20categories.md)}@}. <!--SR:!2026-01-20,292,330!2026-01-11,283,330!2026-01-17,289,330!2026-01-19,291,330!2026-01-17,289,330-->

In the case when {@{_C_ and its opposite _C_<sup>op</sup> are equivalent}@}, {@{such a category is self-dual}@}.<sup>[\[1\]](#^ref-1)</sup> <!--SR:!2026-01-13,285,330!2026-01-15,287,330-->

## formal definition

We define {@{the elementary language of category theory}@} as {@{the two-sorted [first order language](first%20order%20language.md) with objects and morphisms as distinct sorts}@}, together with {@{the relations of an object being the source or target of a morphism and a symbol for composing two morphisms}@}. <!--SR:!2025-06-18,112,290!2026-01-18,290,330!2026-01-22,294,330-->

Let {@{σ be any statement in this language}@}. We form {@{the dual σ<sup>op</sup>}@} as follows: <!--SR:!2026-01-10,282,330!2026-01-15,287,330-->

1. (annotation: morphism) ::@:: Interchange each occurrence of "source" in σ with "target". <!--SR:!2026-01-11,283,330!2026-01-22,294,330-->
2. (annotation: composition) ::@:: Interchange the order of composing morphisms. That is, replace each occurrence of $g\circ f$ with $f\circ g$ <!--SR:!2026-01-20,292,330!2026-01-12,284,330-->

Informally, these conditions state that {@{the dual of a statement is formed by reversing [arrows](morphism.md) and [compositions](function%20composition.md)}@}. <!--SR:!2026-01-10,282,330-->

_Duality_ is the observation that {@{σ is true for some category _C_ if and only if σ<sup>op</sup> is true for _C_<sup>op</sup>}@}.<sup>[\[2\]](#^ref-2)</sup><sup>[\[3\]](#^ref-3)</sup> <!--SR:!2026-01-18,290,330-->

## examples

- {@{A morphism $f\colon A\to B$}@} is {@{a [monomorphism](monomorphism.md) if $f\circ g=f\circ h$ implies $g=h$}@}. Performing the dual operation, we get the statement that {@{$g\circ f=h\circ f$ implies $g=h$}@}. For {@{a morphism $f\colon B\to A$, this is precisely what it means for _f_ to be an [epimorphism](epimorphism.md)}@}. In short, the property of {@{being a monomorphism is dual to the property of being an epimorphism}@}. <!--SR:!2026-01-16,288,330!2025-10-29,209,310!2026-01-17,289,330!2026-01-12,284,330!2026-01-16,288,330-->

Applying duality, this means that {@{a morphism in some category _C_ is a monomorphism}@} {@{if and only if the reverse morphism in the opposite category _C_<sup>op</sup> is an epimorphism}@}. <!--SR:!2026-01-13,285,330!2026-01-12,284,330-->

- An example comes from {@{reversing the direction of inequalities in a [partial order](partial%20order.md#partial%20order)}@}. So if {@{_X_ is a [set](set%20(mathematics).md) and ≤ a partial order relation}@}, we can {@{define a new partial order relation ≤<sub>new</sub>}@} by <p> &emsp; {@{_x_ ≤<sub>new</sub> _y_ if and only if _y_ ≤ _x_}@}. <!--SR:!2026-01-13,285,330!2026-01-21,293,330!2026-01-14,286,330!2026-01-14,286,330-->

{@{This example on orders}@} is a special case, since {@{partial orders correspond to a certain kind of category in which Hom\(_A_,_B_\) can have at most one element}@}. In {@{applications to logic}@}, this then looks like {@{a very general description of negation \(that is, proofs run in the opposite direction\)}@}. For example, if {@{we take the opposite of a [lattice](lattice%20theory.md)}@}, we will find that {@{_meets_ and _joins_ have their roles interchanged}@}. This is an abstract form of {@{[De Morgan's laws](De%20Morgan's%20laws.md), or of [duality](duality%20(order%20theory).md) applied to lattices}@}. <!--SR:!2026-01-12,284,330!2026-01-21,293,330!2026-01-19,291,330!2025-08-10,162,310!2026-01-21,293,330!2026-01-18,290,330!2026-01-17,289,330-->

- [Limits](limit%20(category%20theory).md) and [colimits](limit%20(category%20theory).md) ::@:: are dual notions. <!--SR:!2026-01-20,292,330!2026-01-09,281,330-->
- [Fibrations](fibration.md) and [cofibrations](cofibration.md) ::@:: are examples of dual notions in [algebraic topology](algebraic%20topology.md) and [homotopy theory](homotopy%20theory.md). In this context, the duality is often called [Eckmann–Hilton duality](Eckmann–Hilton%20duality.md). <!--SR:!2025-11-09,209,270!2025-06-01,104,290-->

## see also

- [Adjoint functor](adjoint%20functor.md)
- [Dual object](dual%20object.md)
- [Duality \(mathematics\)](duality%20(mathematics).md)
- [Opposite category](opposite%20category.md)
- [Pulation square](pulation%20square.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/dual_(category_theory)) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFJiří AdámekJ. Rosicky1994"></a> Jiří Adámek; J. Rosicky \(1994\). [_Locally Presentable and Accessible Categories_](https://books.google.com/books?id=iXh6rOd7of0C&pg=PA62). Cambridge University Press. p. 62. [ISBN](ISBN%20(identifier).md) [978-0-521-42261-1](https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-42261-1). <a id="^ref-1"></a>^ref-1
2. [Mac Lane 1978](#CITEREFMac%20Lane1978), p. 33. <a id="^ref-2"></a>^ref-2
3. [Awodey 2010](#CITEREFAwodey2010), p. 53-55. <a id="^ref-3"></a>^ref-3

- ["Dual category"](https://www.encyclopediaofmath.org/index.php?title=Dual_category), _[Encyclopedia of Mathematics](Encyclopedia%20of%20Mathematics.md)_, [EMS Press](European%20Mathematical%20Society.md), 2001 \[1994\]
- ["Duality principle"](https://www.encyclopediaofmath.org/index.php?title=Duality_principle), _[Encyclopedia of Mathematics](Encyclopedia%20of%20Mathematics.md)_, [EMS Press](European%20Mathematical%20Society.md), 2001 \[1994\]
- ["Duality"](https://www.encyclopediaofmath.org/index.php?title=Duality), _[Encyclopedia of Mathematics](Encyclopedia%20of%20Mathematics.md)_, [EMS Press](European%20Mathematical%20Society.md), 2001 \[1994\]
- <a id="CITEREFMac Lane1978"></a> Mac Lane, Saunders \(1978\). _Categories for the Working Mathematician_ \(Second ed.\). New York, NY: Springer New York. p. 33. [ISBN](ISBN%20(identifier).md) [1441931236](https://en.wikipedia.org/wiki/Special:BookSources/1441931236). [OCLC](OCLC%20(identifier).md#OCLC) [851741862](https://search.worldcat.org/oclc/851741862).
- <a id="CITEREFAwodey2010"></a> Awodey, Steve \(2010\). _Category theory_ \(2nd ed.\). Oxford: Oxford University Press. pp. 53–55. [ISBN](ISBN%20(identifier).md) [978-0199237180](https://en.wikipedia.org/wiki/Special:BookSources/978-0199237180). [OCLC](OCLC%20(identifier).md#OCLC) [740446073](https://search.worldcat.org/oclc/740446073).

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
> - [Duality theories](https://en.wikipedia.org/wiki/Category:Duality%20theories)
