---
aliases:
  - absolute coequaliser
  - absolute coequalisers
  - absolute coequalizer
  - absolute coequalizers
  - coequaliser
  - coequalisers
  - coequalizer
  - coequalizers
tags:
  - flashcard/active/general/eng/coequalizer
  - language/in/English
---

# coequalizer

In {@{[category theory](category%20theory.md)}@}, {@{a __coequalizer__ \(or __coequaliser__\)}@} is {@{a generalization of a [quotient](quotient%20set.md#quotient%20set) by an [equivalence relation](equivalence%20relation.md) to objects in an arbitrary [category](category%20(mathematics).md)}@}. It is the categorical construction {@{[dual](dual%20(category%20theory).md) to the [equalizer](equaliser%20(mathematics).md)}@}.

## definition

{@{A __coequalizer__}@} is {@{the [colimit](colimit.md) of a diagram consisting of two objects _X_ and _Y_ and two parallel [morphisms](morphism.md) _f_, _g_ : _X_ → _Y_}@}.

More explicitly, {@{a coequalizer of the parallel morphisms _f_ and _g_}@} can be defined as {@{an object _Q_ together with a morphism _q_ : _Y_ → _Q_ such that _q_ ∘ _f_ = _q_ ∘ _g_}@}. Moreover, {@{the pair \(_Q_, _q_\) must be [universal](universal%20property.md)}@} in the sense that {@{given any other such pair \(_Q_<!-- markdown separator -->′, _q_<!-- markdown separator -->′\) there exists a unique morphism _u_ : _Q_ → _Q_<!-- markdown separator -->′ such that _u_ ∘ _q_ = _q_<!-- markdown separator -->′}@}. This information can be captured by {@{the following [commutative diagram](commutative%20diagram.md): <p> &emsp; ![[w:Commutative diagram](commutative%20diagram.md) for [w:Coequalizer](coequalizer.md)](../../archives/Wikimedia%20Commons/Coequalizer-01.svg)}@}

As with {@{all [universal constructions](universal%20construction.md)}@}, {@{a coequalizer, if it exists, is unique [up to](up%20to.md) a unique [isomorphism](isomorphism.md)}@} \(this is why, {@{by abuse of language, one sometimes speaks of "the" coequalizer of two parallel arrows}@}\).

It can be shown that {@{a coequalizing arrow _q_}@} is {@{an [epimorphism](epimorphism.md) in any category}@}.

## examples

- In {@{the [category of sets](category%20of%20sets.md)}@}, {@{the coequalizer of two [functions](function%20(mathematics).md) _f_, _g_ : _X_ → _Y_}@} is {@{the [quotient](quotient%20set.md#quotient%20set) (annotation: the set of equivalence classes) of _Y_ by the smallest [equivalence relation](equivalence%20relation.md) ~}@} such that {@{for every _x_ ∈ _X_, we have _f_\(_x_\) ~ _g_\(_x_\)}@}.<sup>[\[1\]](#^ref-1)</sup> (annotation: If {@{_f_, _g_ sends _x_ to different elements in _Y_}@}, then {@{the coequalizer needs to send these different elements to the same element, or equivalently, to the same equivalence class}@}. The smallest equivalence relation means {@{the number of relations in the equivalence relation is the least}@}.) In particular, if {@{_R_ is an equivalence relation on a set _Y_}@}, and {@{_r_<sub>1</sub>, _r_<sub>2</sub> are the natural projections \(_R_ ⊂ _Y_ × _Y_\) → _Y_}@} then {@{the coequalizer of _r_<sub>1</sub> and _r_<sub>2</sub> is the quotient set _Y_ / _R_}@}. (annotation: Consider {@{each relation \(_y_<sub>1</sub>, _y_<sub>2</sub>\) in _R_}@}. Since {@{_R_ is an equivalence relation}@}, so {@{_y_<sub>1</sub> and _y_<sub>2</sub> are in the same equivalence class}@}. _r_<sub>1</sub> and _r_<sub>2</sub> {@{respectively extracts _y_<sub>1</sub> and _y_<sub>2</sub> from a relation}@}, and combined with the above, the coequalizer {@{should send _y_<sub>1</sub> and _y_<sub>2</sub> to the same equivalence class in _Y_ / _R_}@}.) \(See also: {@{[quotient by an equivalence relation](quotient%20by%20an%20equivalence%20relation.md)}@}.\)
- {@{The coequalizer in the [category of groups](category%20of%20groups.md)}@} is {@{very similar}@}. Here {@{if _f_, _g_ : _X_ → _Y_ are [group homomorphisms](group%20homomorphism.md)}@}, their coequalizer is {@{the [quotient](quotient%20group.md) of _Y_ by the [normal closure](normal%20closure%20(group%20theory).md) of the set $$S=\{f(x)g(x)^{-1}\mid x\in X\}$$}@}
- For {@{[abelian groups](abelian%20group.md)}@} {@{the coequalizer is particularly simple}@}. It is {@{just the [factor group](factor%20group.md) _Y_ / im\(_f_ – _g_\)}@}. \(This is {@{the [cokernel](cokernel.md) of the morphism _f_ – _g_}@}; see the next section\). (annotation: Think of {@{the cokernel in linear algebra}@} for better intuition.)
- In {@{the [category of topological spaces](category%20of%20topological%20spaces.md)}@}, {@{the circle object _S_<sup>1</sup>}@} can be viewed as {@{the coequalizer of the two inclusion maps from the standard 0-simplex to the standard 1-simplex}@}.
- {@{Coequalizers can be large}@}: There are {@{exactly two [functors](functor.md)}@} from {@{the category __1__ having one object and one identity arrow, to the category __2__ with two objects and one non-identity arrow going between them}@}. {@{The coequalizer of these two functors}@} is {@{the [monoid](monoid.md) of [natural numbers](natural%20number.md) under addition, considered as a one-object category (annotation: the object is an opaque object, each morphism is a natural number, and composition is addition)}@}. (annotation: A potential coequalizer in this context is {@{a functor}@}. By the definition of coequalizer, a potential coequalizer {@{must map both objects and their identity morphisms in __2__ to the same object and its identity morphism in the target category}@}. The remaining morphism is {@{mapped to any endomorphism of the object}@}. The coequalizer is {@{the potential coequalizer that is _universal_}@}. However, it is hard to say {@{why the coequalizer is a functor to the monoid of natural numbers under addition}@}...) In particular, this shows that {@{while every coequalizing arrow is [epic](epimorphism.md), it is not necessarily [surjective](surjective.md)}@}.

## properties

- Every coequalizer ::@:: is an epimorphism.
- In a [topos](topos.md), ::@:: every [epimorphism](epimorphism.md) is the coequalizer of its kernel pair.

## special cases

In {@{categories with [zero morphisms](zero%20morphism.md)}@}, one can {@{define a _[cokernel](cokernel.md)_ of a morphism _f_ as the coequalizer of _f_ and the parallel zero morphism}@}.

In {@{[preadditive categories](preadditive%20category.md)}@} it makes sense to {@{add and subtract morphisms \(the [hom-sets](hom-set.md#hom-set) actually form [abelian groups](abelian%20group.md)\)}@}. In such categories, one can define the coequalizer of two morphisms _f_ and _g_ as {@{the cokernel of their difference: <p> &emsp; coeq\(_f_, _g_\) = coker\(_g_ – _f_\)}@}.

A stronger notion is that of {@{an __absolute coequalizer__}@}, this is {@{a coequalizer that is preserved under all functors}@}. Formally, {@{an absolute coequalizer of a pair of parallel arrows _f_, _g_ : _X_ → _Y_ in a category _C_}@} is {@{a coequalizer as defined above}@}, but with the added property that {@{given any functor _F_ : _C_ → _D_, _F_\(_Q_\) together with _F_\(_q_\) is the coequalizer of _F_\(_f_\) and _F_\(_g_\) in the category _D_}@}. {@{[Split coequalizers](split%20coequalizer.md)}@} are {@{examples of absolute coequalizers}@}.

## see also

- [Coproduct](coproduct.md)
- [Pushout](pushout%20(category%20theory).md)

## notes

1. <a id="CITEREFBarrWells1998"></a> [Barr, Michael](Michael%20Barr%20(mathematician).md); [Wells, Charles](Charles%20Wells%20(mathematician).md) \(1998\). [_Category theory for computing science_](http://www.tac.mta.ca/tac/reprints/articles/22/tr22.pdf) \(PDF\). [Prentice Hall International Series in Computer Science](Prentice%20Hall%20International%20Series%20in%20Computer%20Science.md). p. 278. <a id="^ref-1"></a>^ref-1

## references

This text incorporates [content](https://en.wikipedia.org/wiki/coequalizer) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- <a id="CITEREFMac Lane1998"></a> [Mac Lane, Saunders](Saunders%20Mac%20Lane.md) \(1998\). _[Categories for the Working Mathematician](Categories%20for%20the%20Working%20Mathematician.md)_. [Graduate Texts in Mathematics](Graduate%20Texts%20in%20Mathematics.md). Vol. 5 \(2nd ed.\). [Springer-Verlag](Springer-Verlag.md#history). [ISBN](ISBN%20(identifier).md) [0-387-98403-8](https://en.wikipedia.org/wiki/Special:BookSources/0-387-98403-8). [Zbl](Zbl%20(identifier).md) [0906.18001](https://zbmath.org/?format=complete&q=an:0906.18001).
  - Coequalizers – page 65
  - Absolute coequalizers – page 149

## external links

- [Interactive Web page](https://web.archive.org/web/20080916162345/http://www.j-paine.org/cgi-bin/webcats/webcats.php), which generates examples of coequalizers in the category of finite sets. Written by [Jocelyn Paine](https://web.archive.org/web/20081223001815/http://www.j-paine.org/).

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
