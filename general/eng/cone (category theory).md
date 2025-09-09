---
aliases:
  - cone
  - cone (category theory)
  - cone of a functor
  - cones
  - cones (category theory)
  - cones of a functor
tags:
  - flashcard/active/general/eng/cone__category_theory_
  - language/in/English
---

# cone

<!-- | ![](../../archives/Wikimedia%20Commons/Text%20document%20with%20red%20question%20mark.svg) | This article includes a [list of references](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources), [related reading](https://en.wikipedia.org/wiki/Wikipedia:Further%20reading), or [external links](https://en.wikipedia.org/wiki/Wikipedia:External%20links), __but its sources remain unclear because it lacks [inline citations](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources#Inline%20citations)__. Please help [improve](https://en.wikipedia.org/wiki/Wikipedia:WikiProject%20Reliability) this article by [introducing](https://en.wikipedia.org/wiki/Wikipedia:When%20to%20cite) more precise citations. _\(April 2022\)__\([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ | -->

In {@{[category theory](category%20theory.md), a branch of [mathematics](mathematics.md)}@}, {@{the __cone of a functor__}@} is {@{an abstract notion used to define the [limit](limit%20(category%20theory).md) of that [functor](functor.md)}@}. Cones {@{make other appearances in category theory}@} as well. <!--SR:!2026-01-05,273,330!2026-04-02,346,349!2026-04-10,353,352!2026-01-31,294,330-->

## definition

Let {@{_F_ : _J_ → _C_ be a [diagram](diagram%20(category%20theory).md) in _C_}@}. Formally, a diagram is {@{nothing more than a [functor](functor.md) from _J_ to _C_}@}. The change in terminology reflects the fact that {@{we think of _F_ as indexing a family of [objects](object%20(category%20theory).md) and [morphisms](morphism.md) in _C_}@}. {@{The [category](category%20(mathematics).md) _J_}@} is thought of {@{as an "index category"}@}. One should consider this in analogy with the concept of {@{an [indexed family](indexed%20family.md) of objects in [set theory](set%20theory.md)}@}. The primary difference is that {@{here we have morphisms as well}@}. Thus, for example, when {@{_J_ is a [discrete category](discrete%20category.md)}@}, it {@{corresponds most closely to the idea of an indexed family in set theory}@}. Another common and more interesting example {@{takes _J_ to be a [span](span%20(category%20theory).md)}@}. _J_ can also {@{be taken to be the empty category, leading to the simplest cones}@}. <!--SR:!2026-01-26,290,330!2026-01-31,294,330!2025-10-12,189,310!2026-04-04,348,352!2026-03-05,322,349!2025-11-29,244,330!2026-04-05,349,352!2026-04-08,351,352!2025-12-23,262,330!2026-01-29,292,330!2026-01-31,294,330-->

Let {@{_N_ be an object of _C_}@}. {@{A __cone__ from _N_ to _F_}@} is {@{a family of morphisms $$\psi _{X}\colon N\to F(X)\,$$ for each object _X_ of _J_}@}, such that {@{for every morphism _f_ : _X_ → _Y_ in _J_ the following diagram [commutes](commutative%20diagram.md): <p> ![Part of a cone from N to F](../../archives/Wikimedia%20Commons/Functor%20cone.svg)}@} <p> {@{The \(usually infinite\) collection of all these triangles}@} can be {@{\(partially\) depicted in the shape of a [cone](cone%20(geometry).md) with the apex _N_}@}. {@{The cone ψ}@} is sometimes said to {@{have __vertex__ _N_ and __base__ _F_}@}. <!--SR:!2027-11-26,795,330!2026-04-06,350,352!2026-04-12,355,352!2025-10-10,188,310!2026-03-29,343,352!2026-04-09,352,352!2026-04-03,347,352!2026-03-09,326,349-->

One can also define {@{the [dual](dual%20(category%20theory).md) notion of a __cone__ from _F_ to _N_ \(also called a __co-cone__\)}@} by {@{reversing all the arrows above}@}. Explicitly, {@{a co-cone from _F_ to _N_}@} is {@{a family of morphisms $$\psi _{X}\colon F(X)\to N\,$$ for each object _X_ of _J_}@}, such that {@{for every morphism _f_ : _X_ → _Y_ in _J_ the following diagram commutes: <p> ![Part of a cone from F to N](../../archives/Wikimedia%20Commons/Functor%20co-cone.svg)}@} <!--SR:!2026-03-19,336,352!2025-12-26,264,330!2026-04-11,354,352!2026-01-30,293,330!2025-10-09,201,332-->

## equivalent formulations

At first glance cones seem to be {@{slightly abnormal constructions in category theory}@}. They are {@{maps from an _object_ to a _functor_ \(or vice versa\)}@}. In keeping with {@{the spirit of category theory}@} we would like to {@{define them as morphisms or objects in some suitable category}@}. In fact, {@{we can do both}@}. <!--SR:!2026-01-31,294,330!2025-12-20,259,330!2026-03-16,333,352!2026-03-28,342,352!2026-01-30,293,330-->

Let {@{_J_ be a small category}@} and let {@{_C_<sup>_J_</sup> be the [category of diagrams](category%20of%20diagrams.md) of type _J_ in _C_ \(this is nothing more than a [functor category](functor%20category.md)\)}@}. Define {@{the [diagonal functor](diagonal%20functor.md) Δ : _C_ → _C_<sup>_J_</sup>}@} as follows: {@{Δ\(_N_\) : _J_ → _C_ is the [constant functor](constant%20functor.md#examples) to _N_ for all _N_ in _C_}@}. <!--SR:!2026-01-07,275,330!2025-12-22,261,330!2026-04-03,347,352!2025-12-27,265,330-->

If {@{_F_ is a diagram of type _J_ in _C_}@}, the following statements are equivalent: <!--SR:!2025-12-21,260,330-->

- (annotation: cone) ::@:: ψ is a cone from _N_ to _F_ <!--SR:!2026-04-10,353,352!2026-01-26,290,330-->
- (annotation: cone, natural transformation) ::@:: ψ is a [natural transformation](natural%20transformation.md) from Δ\(_N_\) to _F_ <!--SR:!2025-12-08,251,330!2026-04-06,350,352-->
- (annotation: cone, comma category) ::@:: \(_N_, ψ\) is an object in the [comma category](comma%20category.md) \(Δ ↓ _F_\) (annotation: note that this is actually a slice category, meaning the _F_ on the right is more accurately the functor that maps the only object in __1__ to the diagram _F_) <!--SR:!2025-10-18,194,310!2027-06-29,673,332-->

{@{The dual statements}@} are also equivalent: <!--SR:!2026-01-29,292,330-->

- (annotation: co-cone) ::@:: ψ is a co-cone from _F_ to _N_ <!--SR:!2026-01-29,292,330!2025-12-29,267,330-->
- (annotation: co-cone, natural transformation) ::@:: ψ is a [natural transformation](natural%20transformation.md) from _F_ to Δ\(_N_\) <!--SR:!2026-04-04,348,352!2026-01-31,294,330-->
- (annotation: co-cone, comma category) ::@:: \(_N_, ψ\) is an object in the [comma category](comma%20category.md) \(_F_ ↓ Δ\) (annotation: note that this is actually a co-slice category, meaning the _F_ on the left is more accurately the functor that maps the only object in __1__ to the diagram _F_) <!--SR:!2027-01-24,541,310!2026-01-30,293,330-->

{@{These statements can all be verified}@} by {@{a straightforward application of the definitions}@}. Thinking of {@{cones as natural transformations}@} we see that they are {@{just morphisms in _C_<sup>_J_</sup> with source \(or target\) a constant functor}@}. <!--SR:!2026-01-04,272,330!2025-12-22,260,330!2026-01-08,276,330!2025-12-28,266,330-->

## category of cones

By the above, we can define {@{the __category of cones to _F_<!-- markdown separator -->__}@} as {@{the comma category \(Δ ↓ _F_\)}@}. {@{Morphisms of cones}@} are then {@{just morphisms in this category}@}. This equivalence is rooted in the observation that {@{a natural map between constant functors Δ\(_N_\), Δ\(_M_\) corresponds to a morphism between _N_ and _M_}@}. In this sense, {@{the diagonal functor acts trivially on arrows}@}. In similar vein, writing down the definition of {@{a natural map from a constant functor Δ\(_N_\) to _F_}@} yields {@{the same diagram as the above}@}. As one might expect, {@{a morphism from a cone \(_N_, ψ\) to a cone \(_L_, φ\)}@} is {@{just a morphism _N_ → _L_ such that all the "obvious" diagrams commute}@} \(see the first diagram in the next section\). <!--SR:!2025-12-07,250,330!2026-01-03,271,330!2025-12-23,262,330!2026-01-30,293,330!2026-01-25,289,330!2026-01-02,270,330!2026-04-08,351,352!2025-12-23,261,330!2026-04-07,350,349!2025-09-24,187,310-->

Likewise, {@{the __category of co-cones from _F_<!-- markdown separator -->__}@} is {@{the comma category \(_F_ ↓ Δ\)}@}. <!--SR:!2026-03-06,323,349!2026-03-10,327,349-->

## universal cones

{@{[Limits and colimits](limit%20(category%20theory).md)}@} are {@{defined as __universal cones__}@}. That is, {@{cones through which all other cones factor}@}. {@{A cone φ from _L_ to _F_ is a universal cone}@} if {@{for any other cone ψ from _N_ to _F_ there is a unique morphism from ψ to φ}@}. <p> ![A commutative diagram depicting the universal cone over a functor.](../../archives/Wikimedia%20Commons/Functor%20cone%20%28extended%29.svg) <p> Equivalently, {@{a universal cone to _F_}@} is {@{a [universal morphism](universal%20morphism.md) from Δ to _F_}@} \(thought of {@{as an object in _C_<sup>_J_</sup>}@}\), or {@{a [terminal object](terminal%20object.md) in \(Δ ↓ _F_\)}@}. <!--SR:!2026-03-18,335,352!2026-02-15,310,349!2026-01-29,292,330!2026-03-07,324,349!2025-11-19,232,332!2025-12-12,255,330!2026-04-02,346,349!2026-01-06,274,330!2025-10-11,189,310-->

{@{Dually}@}, {@{a cone φ from _F_ to _L_ is a universal cone}@} if {@{for any other cone ψ from _F_ to _N_ there is a unique morphism from φ to ψ}@}. <p> ![A commutative diagram depicting a universal co-cone under a functor.](../../archives/Wikimedia%20Commons/Functor%20co-cone%20%28extended%29.svg) Equivalently, {@{a universal cone from _F_}@} is {@{a universal morphism from _F_ to Δ}@}, or {@{an [initial object](initial%20object.md) in \(_F_ ↓ Δ\)}@}. <!--SR:!2025-11-30,245,330!2026-04-01,346,352!2026-04-11,354,352!2025-12-24,262,330!2026-01-30,293,330!2026-04-07,350,352-->

The limit of _F_ is {@{a universal cone to _F_, and the colimit is a universal cone from _F_}@}. As with {@{all universal constructions}@}, {@{universal cones are not guaranteed to exist for all diagrams _F_}@}, but {@{if they do exist they are unique up to a unique isomorphism \(in the comma category \(Δ ↓ _F_\)\)}@}. <!--SR:!2026-01-24,288,330!2026-04-09,352,352!2026-04-10,353,352!2026-02-18,280,290-->

## see also

- [Inverse limit\#Cones](inverse%20limit.md#cones) – ::@:: Construction in category theory <!--SR:!2026-04-12,355,352!2025-10-10,188,310-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/cone_(category_theory)) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- <a id="CITEREFMac Lane1998"></a> [Mac Lane, Saunders](Saunders%20Mac%20Lane.md) \(1998\). _[Categories for the Working Mathematician](Categories%20for%20the%20Working%20Mathematician.md)_ \(2nd ed.\). New York: Springer. [ISBN](ISBN%20(identifier).md) [0-387-98403-8](https://en.wikipedia.org/wiki/Special:BookSources/0-387-98403-8).
- <a id="CITEREFBorceux1994"></a> Borceux, Francis \(1994\). "Limits". [_Handbook of categorical algebra_](https://archive.org/details/handbookofcatego0000borc). Encyclopedia of mathematics and its applications 50-51, 53 \[i.e. 52\]. Vol. 1. Cambridge University Press. [ISBN](ISBN%20(identifier).md) [0-521-44178-1](https://en.wikipedia.org/wiki/Special:BookSources/0-521-44178-1).

## external links

- [Cone](https://ncatlab.org/nlab/show/cone) at the [_n_<!-- markdown separator -->Lab](nLab.md)

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Category theory](https://en.wikipedia.org/wiki/Category:Category%20theory)
> - [Limits \(category theory\)](https://en.wikipedia.org/wiki/Category:Limits%20%28category%20theory%29)
