---
aliases:
  - co-terminal object
  - co-terminal objects
  - coterminal object
  - coterminal objects
  - final object
  - final objects
  - initial and terminal object
  - initial and terminal objects
  - initial element
  - initial elements
  - initial object
  - initial objects
  - null object
  - null objects
  - pointed categories
  - pointed category
  - terminal element
  - terminal elements
  - terminal object
  - terminal objects
  - universal object
  - universal objects
  - zero object
  - zero objects
tags:
  - flashcard/active/general/eng/initial_and_terminal_objects
  - language/in/English
---

# initial and terminal objects

- "{@{Zero object}@}" redirects here. For {@{zero object in an algebraic structure}@}, see {@{[zero object \(algebra\)](zero%20object%20(algebra).md)}@}.
- "{@{Terminal element}@}" redirects here. For {@{the project management concept}@}, see {@{[work breakdown structure](work%20breakdown%20structure.md)}@}. <!--SR:!2025-04-18,75,332!2025-04-11,69,317!2025-04-06,65,317!2025-04-06,65,317!2025-04-17,74,332!2025-04-26,82,339-->

In {@{[category theory](category%20theory.md), a branch of [mathematics](mathematics.md)}@}, {@{an __initial object__}@} of {@{a [category](category%20(mathematics).md) _C_ is an object _I_ in _C_ such that for every object _X_ in _C_, there exists precisely one [morphism](morphism.md) _I_ → _X_}@}. <!--SR:!2025-04-05,64,317!2025-03-31,60,317!2025-04-11,69,317-->

{@{The [dual](dual%20(category%20theory).md) notion}@} is that of {@{a __terminal object__ \(also called __terminal element__\)}@}: _T_ is {@{terminal if for every object _X_ in _C_ there exists exactly one morphism _X_ → _T_}@}. Initial objects are also called {@{__coterminal__ or __universal__}@}, and terminal objects are also called {@{__final__}@}. <!--SR:!2025-03-31,60,317!2025-04-18,75,332!2025-04-09,67,310!2025-04-06,65,317!2025-04-05,64,317-->

If {@{an object is both initial and terminal}@}, it is called {@{a __zero object__ or __null object__}@}. {@{A __pointed category__}@} is {@{one with a zero object}@}. <!--SR:!2025-04-11,69,317!2025-03-30,59,317!2025-03-30,59,317!2025-04-20,77,337-->

{@{A [strict initial object](strict%20initial%20object.md) _I_}@} is one {@{for which every morphism into _I_ is an [isomorphism](isomorphism.md)}@}. <!--SR:!2025-04-19,76,332!2025-02-10,8,297-->

## examples

- {@{The [empty set](empty%20set.md)}@} is {@{the unique initial object in __Set__, the [category of sets](category%20of%20sets.md)}@}. {@{Every one-element set \([singleton](singleton%20(mathematics).md)\)}@} is {@{a terminal object in this category}@}; there are {@{no zero objects}@}. Similarly, {@{the empty space}@} is {@{the unique initial object in __Top__, the [category of topological spaces](category%20of%20topological%20spaces.md)}@} and {@{every one-point space is a terminal object in this category}@}.
- In the category __[Rel](category%20of%20relations.md)__ of sets and relations, ::@:: the empty set is the unique initial object, the unique terminal object, and hence the unique zero object. <!--SR:!2025-04-19,76,332!2025-04-11,69,317-->

> {@{![Center: the zero object. <br/> Left half: all elements of an object maps to zero, the terminal morphism. <br/> Right half: 0 maps to 0, the initial monomorphism.](../../archives/Wikimedia%20Commons/Terminal%20and%20initial%20object.svg)}@}
>
> {@{Morphisms of pointed sets}@}. The image also {@{applies to algebraic zero objects}@} <!--SR:!2025-03-31,60,317!2025-04-06,65,317!2025-04-20,77,337-->

- In {@{the category of [pointed sets](pointed%20set.md)}@} \(whose {@{objects are non-empty sets together with a distinguished element; a morphism from \(_A_, <!-- markdown separator -->_a_\) to \(_B_, <!-- markdown separator -->_b_\) being a function _f_ : _A_ → _B_ with _f_\(_a_\) = _b_}@}\), {@{every singleton is a zero object}@}. Similarly, in {@{the category of [pointed topological spaces](pointed%20space.md)}@}, {@{every singleton is a zero object}@}.
- In {@{__Grp__, the [category of groups](category%20of%20groups.md)}@}, {@{any [trivial group](trivial%20group.md) is a zero object}@}. The trivial object is also {@{a zero object in __Ab__, the [category of abelian groups](category%20of%20abelian%20groups.md), __Rng__ the [category of pseudo-rings](category%20of%20pseudo-rings.md#rings%20without%20identity), ___R_-Mod__, the [category of modules](category%20of%20modules.md) over a ring, and ___K_-Vect__, the [category of vector spaces](category%20of%20vector%20spaces.md) over a field}@}. See {@{_[Zero object \(algebra\)](zero%20object%20(algebra).md)_}@} for details. This is {@{the origin of the term "zero object"}@}.
- In {@{__Ring__, the [category of rings](category%20of%20rings.md) with unity and unity-preserving morphisms}@}, {@{the ring of [integers](integer.md) __Z__}@} is {@{an initial object}@}. {@{The [zero ring](zero%20ring.md) consisting only of a single element 0 = 1}@} is {@{a terminal object}@}.
- In {@{__Rig__, the category of [rigs](rig%20(mathematics).md#terminology) with unity and unity-preserving morphisms}@}, {@{the rig of [natural numbers](natural%20number.md) __N__}@} is {@{an initial object}@}. {@{The zero rig, which is the [zero ring](zero%20ring.md), consisting only of a single element 0 = 1}@} is {@{a terminal object}@}.
- In {@{__Field__, the [category of fields](category%20of%20fields.md#category%20of%20fields)}@}, there are {@{no initial or terminal objects}@}. However, in {@{the subcategory of fields of fixed characteristic}@}, {@{the [prime field](prime%20field.md#prime%20field) is an initial object}@}.
- {@{Any [partially ordered set](partially%20ordered%20set.md) \(_P_, ≤\)}@} can be {@{interpreted as a category}@}: {@{the objects are the elements of _P_, and there is a single morphism from _x_ to _y_ [if and only if](if%20and%20only%20if.md) _x_ ≤ _y_}@}. This category has {@{an initial object if and only if _P_ has a [least element](least%20element.md)}@}; it has {@{a terminal object if and only if _P_ has a [greatest element](greatest%20element.md)}@}.
- {@{__Cat__, the [category of small categories](category%20of%20small%20categories.md) with [functors](functor.md) as morphisms}@} has {@{the empty category, __0__ \(with no objects and no morphisms\), as initial object}@} and {@{the terminal category, __1__ \(with a single object with a single identity morphism\), as terminal object}@}.
- In {@{the category of [schemes](scheme%20(mathematics).md)}@}, {@{Spec\(__Z__\), the [prime spectrum](spectrum%20of%20a%20ring.md) of the ring of integers}@}, is {@{a terminal object}@}. {@{The empty scheme \(equal to the prime spectrum of the [zero ring](zero%20ring.md)\)}@} is {@{an initial object}@}.
- {@{A [limit](limit%20(category%20theory).md) of a [diagram](diagram%20(category%20theory).md) _F_}@} may be {@{characterised as a terminal object in the [category of cones](category%20of%20cones.md#category%20of%20cones) to _F_}@}. Likewise, {@{a colimit of _F_}@} may be characterised as {@{an initial object in the category of co-cones from _F_}@}.
- In the category __Ch<sub>_R_</sub>__ of chain complexes over a commutative ring _R_, ::@:: the zero complex is a zero object. <!--SR:!2025-03-11,40,290!2025-02-28,32,277-->
- In a [short exact sequence](exact%20sequence.md) of the form 0 → _a_ → _b_ → _c_ → 0, ::@:: the initial and terminal objects are the anonymous zero object. This is used frequently in [cohomology theories](cohomology.md). <!--SR:!2025-04-21,78,339!2025-04-20,77,337-->

## properties

### existence and uniqueness

{@{Initial and terminal objects}@} are {@{not required to exist in a given category}@}. However, {@{if they do exist, they are essentially unique}@}. Specifically, if {@{_I_<sub>1</sub> and _I_<sub>2</sub> are two different initial objects}@}, then {@{there is a unique [isomorphism](isomorphism.md) between them}@}. Moreover, {@{if _I_ is an initial object then any object isomorphic to _I_ is also an initial object}@}. The same is {@{true for terminal objects}@}. <!--SR:!2025-04-19,76,332!2025-04-11,69,317!2025-04-19,76,332!2025-04-11,69,317!2025-03-31,60,317!2025-04-10,68,317!2025-04-18,75,332-->

For {@{[complete categories](complete%20category.md)}@} there is {@{an existence theorem for initial objects}@}. Specifically, {@{a \([locally small](locally%20small%20category.md#small%20and%20large%20categories)\) complete category _C_ has an initial object}@} {@{if and only if there exist a set _I_ \(not a [proper class](proper%20class.md)\) and an _I_-[indexed family](indexed%20family.md) \(_K_<sub>_i_</sub>\) of objects of _C_}@} such that {@{for any object _X_ of _C_, there is at least one morphism _K_<sub>_i_</sub> → _X_ for some _i_ ∈ _I_}@}. <!--SR:!2025-03-31,60,317!2025-04-20,77,337!2025-03-10,30,297!2025-04-06,65,317!2025-02-09,18,257-->

### equivalent formulations

{@{Terminal objects in a category _C_}@} may also be defined as {@{[limits](limit%20(category%20theory).md) of the unique empty [diagram](diagram%20(category%20theory).md) __0__ → _C_}@}. Since {@{the empty category is vacuously a [discrete category](discrete%20category.md)}@}, a terminal object can be thought of {@{as an [empty product](empty%20product.md) \(a product is indeed the limit of the discrete diagram {_X_<sub>_i_</sub>}, in general\)}@}. Dually, {@{an initial object is a [colimit](limit%20(category%20theory).md) of the empty diagram __0__ → _C_}@} and can be thought of as {@{an [empty](empty%20sum.md) [coproduct](coproduct.md) or categorical sum}@}. <!--SR:!2025-04-11,69,317!2025-03-30,59,317!2025-04-11,69,317!2025-02-16,25,277!2025-04-03,62,310!2025-03-02,33,277-->

It follows that {@{any [functor](functor.md) which preserves limits will take terminal objects to terminal objects}@}, and {@{any functor which preserves colimits will take initial objects to initial objects}@}. For example, {@{the initial object in any [concrete category](concrete%20category.md) with [free objects](free%20object.md)}@} will be {@{the free object generated by the empty set}@} \(since {@{the [free functor](free%20functor.md#free%20functor)}@}, being {@{[left adjoint](left%20adjoint.md) to the [forgetful functor](forgetful%20functor.md) to __Set__}@}, {@{preserves colimits}@}\). <!--SR:!2025-04-10,68,317!2025-03-23,50,297!2025-03-02,33,277!2025-03-18,46,290!2025-04-19,76,332!2025-02-27,25,237!2025-04-11,69,317-->

Initial and terminal objects may also {@{be characterized in terms of [universal properties](universal%20property.md) and [adjoint functors](adjoint%20functors.md)}@}. Let {@{__1__ be the discrete category with a single object \(denoted by •\)}@}, and let {@{_U_ : _C_ → __1__ be the unique \(constant\) functor to __1__}@}. Then <!--SR:!2025-03-30,59,317!2025-04-11,69,317!2025-04-19,76,332-->

- An initial object _I_ in _C_ is ::@:: a [universal morphism](universal%20morphism.md) from • to _U_. (annotation: That every object has an unique morphism from the initial object corresponds to the unique morphism requirement in a universal morphism.) The functor which sends • to _I_ is left adjoint to _U_. <!--SR:!2025-02-10,19,257!2025-03-01,32,277-->
- A terminal object _T_ in _C_ is ::@:: a universal morphism from _U_ to •. (annotation: That every object has an unique morphism to the terminal object corresponds to the unique morphism requirement in a universal morphism.) The functor which sends • to _T_ is right adjoint to _U_. <!--SR:!2025-02-28,32,277!2025-02-10,19,277-->

### relation to other categorical constructions

{@{Many natural constructions in category theory}@} can be {@{formulated in terms of finding an initial or terminal object in a suitable category}@}. <!--SR:!2025-04-10,68,317!2025-03-25,51,312-->

- {@{A [universal morphism](universal%20morphism.md) from an object _X_ to a functor _U_}@} can be defined as {@{an initial object in the [comma category](comma%20category.md) \(_X_ ↓ _U_\)}@}. Dually, {@{a universal morphism from _U_ to _X_}@} is {@{a terminal object in \(_U_ ↓ _X_\)}@}.
- {@{The limit of a diagram _F_}@} is {@{a terminal object in Cone\(_F_\), the [category of cones](category%20of%20cones.md#category%20of%20cones) to _F_}@}. Dually, {@{a colimit of _F_}@} is {@{an initial object in the category of cones from _F_}@}.
- A [representation of a functor](representable%20functor.md) _F_ to __Set__ is ::@:: an initial object in the [category of elements](category%20of%20elements.md) of _F_. <!--SR:!2025-02-24,19,272!2025-02-17,16,217-->
- The notion of [final functor](final%20functor.md) \(respectively, initial functor\) is ::@:: a generalization of the notion of final object \(respectively, initial object\). <!--SR:!2025-04-18,75,332!2025-04-11,69,317-->

### other properties

- The [endomorphism monoid](endomorphism%20monoid.md) of an initial or terminal object _I_ is trivial: ::@:: End\(_I_\) = Hom\(_I_, _I_\) = { id<sub>_I_</sub> }. <!--SR:!2025-04-10,68,317!2025-03-30,59,317-->
- If a category _C_ has a zero object 0, ::@:: then for any pair of objects _X_ and _Y_ in _C_, the unique composition _X_ → 0 → _Y_ is a [zero morphism](zero%20morphism.md) from _X_ to _Y_. <!--SR:!2025-02-26,18,277!2025-04-02,58,319-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/initial_and_terminal_objects) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- <a id="CITEREFAdámekHerrlichStrecker1990"></a> Adámek, Jiří; Herrlich, Horst; Strecker, George E. \(1990\). [_Abstract and Concrete Categories. The joy of cats_](https://web.archive.org/web/20150421081851/http://katmat.math.uni-bremen.de/acc/acc.pdf) \(PDF\). John Wiley & Sons. [ISBN](ISBN%20(identifier).md) [0-471-60922-6](https://en.wikipedia.org/wiki/Special:BookSources/0-471-60922-6). [Zbl](Zbl%20(identifier).md) [0695.18001](https://zbmath.org/?format=complete&q=an:0695.18001). Archived from [the original](http://katmat.math.uni-bremen.de/acc/acc.pdf) \(PDF\) on 2015-04-21. Retrieved 2008-01-15.
- <a id="CITEREFPedicchioTholen2004"></a> Pedicchio, Maria Cristina; Tholen, Walter, eds. \(2004\). _Categorical foundations. Special topics in order, topology, algebra, and sheaf theory_. Encyclopedia of Mathematics and Its Applications. Vol. 97. Cambridge: [Cambridge University Press](Cambridge%20University%20Press.md). [ISBN](ISBN%20(identifier).md) [0-521-83414-7](https://en.wikipedia.org/wiki/Special:BookSources/0-521-83414-7). [Zbl](Zbl%20(identifier).md) [1034.18001](https://zbmath.org/?format=complete&q=an:1034.18001).
- <a id="CITEREFMac Lane1998"></a> [Mac Lane, Saunders](Saunders%20Mac%20Lane.md) \(1998\). _[Categories for the Working Mathematician](Categories%20for%20the%20Working%20Mathematician.md)_. [Graduate Texts in Mathematics](Graduate%20Texts%20in%20Mathematics.md). Vol. 5 \(2nd ed.\). [Springer-Verlag](Springer-Verlag.md#history). [ISBN](ISBN%20(identifier).md) [0-387-98403-8](https://en.wikipedia.org/wiki/Special:BookSources/0-387-98403-8). [Zbl](Zbl%20(identifier).md) [0906.18001](https://zbmath.org/?format=complete&q=an:0906.18001).
- _This article is based in part on [PlanetMath](https://www.planetmath.org/)'s [article on examples of initial and terminal objects](https://planetmath.org/encyclopedia/TerminalObjectsAndZeroObjectsExamplesOfInitialObjects.html)._

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
> - [Limits \(category theory\)](https://en.wikipedia.org/wiki/Category:Limits%20%28category%20theory%29)
> - [Objects \(category theory\)](https://en.wikipedia.org/wiki/Category:Objects%20%28category%20theory%29)
