---
aliases:
  - concrete categories
  - concrete category
tags:
  - flashcard/active/general/eng/concrete_category
  - language/in/English
---

# concrete category

In {@{[mathematics](mathematics.md)}@}, {@{a __concrete category__}@} is {@{a [category](category%20(category%20theory).md) that is equipped with a [faithful functor](faithful%20functor.md) (annotation: hom-classes are injective for every pair of objects; this does _not_ imply morphisms are injective) to the [category of sets](category%20of%20sets.md) \(or sometimes to another category\)}@}. This functor makes it {@{possible to think of the objects of the category as sets with additional [structure](mathematical%20structure.md), and of its [morphisms](morphism.md) as structure-preserving functions}@}. Many important categories have {@{obvious interpretations as concrete categories}@}, for example {@{the [category of topological spaces](category%20of%20topological%20spaces.md) and the [category of groups](category%20of%20groups.md)}@}, and trivially also {@{the category of sets itself}@}. On the other hand, {@{the [homotopy category of topological spaces](homotopy%20category%20of%20topological%20spaces.md)}@} is {@{not __concretizable__, i.e. it does not admit a faithful functor to the category of sets}@}. <!--SR:!2025-09-23,189,310!2026-01-25,293,330!2026-04-13,326,290!2025-10-02,201,324!2026-02-19,315,344!2027-01-15,522,324!2026-05-13,326,290!2026-01-22,290,330!2025-09-06,19,364-->

A concrete category, when {@{defined without reference to the notion of a category}@}, consists of {@{a [class](class%20(set%20theory).md) of _objects_, each equipped with an _underlying set_}@}; and {@{for any two objects _A_ and _B_ a set of functions, called _homomorphisms_, from the underlying set of _A_ to the underlying set of _B_}@}. Furthermore, {@{for every object _A_, the identity function on the underlying set of _A_ must be a homomorphism from _A_ to _A_}@}, and {@{the composition of a homomorphism from _A_ to _B_ followed by a homomorphism from _B_ to _C_ must be a homomorphism from _A_ to _C_}@}.<sup>[\[1\]](#^ref-1)</sup> <!--SR:!2027-07-03,688,330!2026-04-09,322,290!2026-12-05,483,310!2026-06-10,357,304!2026-03-18,337,344-->

## definition

{@{A __concrete category__}@} is {@{a pair \(_C_,_U_\)}@} such that <!--SR:!2025-12-12,258,330!2025-12-08,255,330-->

- _C_ ::@:: is a category, and <!--SR:!2025-12-16,261,330!2025-12-02,251,330-->
- _U_ : _C_ → __Set__ \(the category of sets and functions\) ::@:: is a [faithful functor](faithful%20functor.md). <!--SR:!2025-11-09,215,324!2027-06-24,680,330-->

{@{The functor _U_}@} is to be {@{thought of as a [forgetful functor](forgetful%20functor.md)}@}, which {@{assigns to every object of _C_ its "underlying set", and to every morphism in _C_ its "underlying function"}@}. <!--SR:!2025-10-19,197,310!2025-12-07,255,330!2025-12-17,262,330-->

It is customary to call {@{the morphisms in a concrete category _homomorphisms_ \(e.g., group homomorphisms, ring homomorphisms, etc.\)}@} Because of {@{the faithfulness of the functor _U_}@}, {@{the homomorphisms of a concrete category}@} may be {@{formally identified with their underlying functions \(i.e., their images under _U_\)}@}; the homomorphisms then {@{regain the usual interpretation as "structure-preserving" functions}@}. <!--SR:!2025-09-17,185,310!2026-03-18,337,344!2027-04-28,639,330!2026-10-29,489,324!2026-02-16,313,344-->

{@{A category _C_ is __concretizable__}@} if {@{there exists a concrete category \(_C_,_U_\); i.e., if there exists a faithful functor _U_: _C_ → __Set__}@}. {@{All small categories are concretizable}@}: define _U_ so that its object part maps {@{each object _b_ of _C_ to the set of all morphisms of _C_ whose [codomain](codomain.md) is _b_ \(i.e. all morphisms of the form _f_: _a_ → _b_ for any object _a_ of _C_\)}@}, and its morphism part maps {@{each morphism _g_: _b_ → _c_ of _C_ to the function _U_\(_g_\): _U_\(_b_\) → _U_\(_c_\) which maps each member _f_: _a_ → _b_ of _U_\(_b_\) to the composition _gf_: _a_ → _c_, a member of _U_\(_c_\)}@}. (annotation: this is {@{_not_ the [hom functor](hom%20functor.md), but more like a _flattened_ (coproduct) version of it, which may be seen in item 6 below}@}) \(Item 6 under [Further examples](#further%20examples) expresses {@{the same _U_ in less elementary language via presheaves}@}.\) The [Counter-examples](#counter-examples) section exhibits {@{two large categories that are not concretizable}@}. <!--SR:!2026-03-17,336,344!2025-12-25,268,330!2025-11-17,237,330!2027-06-10,672,330!2026-12-21,496,284!2025-12-20,247,324!2026-11-20,496,310!2026-01-17,285,330-->

## remarks

Contrary to intuition, concreteness is {@{not a [property](property%20(philosophy).md) that a category may or may not satisfy}@}, but {@{rather a structure with which a category may or may not be equipped}@}. In particular, a category _C_ may {@{admit several faithful functors into __Set__}@}. Hence there may be {@{several concrete categories \(_C_, _U_\) all corresponding to the same category _C_}@}. <!--SR:!2026-03-17,336,344!2027-06-16,676,330!2025-11-16,236,330!2026-02-18,315,344-->

In practice, however, {@{the choice of faithful functor is often clear}@} and in this case we {@{simply speak of the "concrete category _C_"}@}. For example, "{@{the concrete category __Set__}@}" means {@{the pair \(__Set__, _I_\) where _I_ denotes the [identity functor](identity%20functor.md#identity%20functor) __Set__ → __Set__}@}. <!--SR:!2026-03-20,337,344!2026-01-03,276,330!2026-01-31,301,344!2026-03-20,337,344-->

{@{The requirement that _U_ be faithful}@} means that {@{it maps different morphisms between the same objects to different functions}@}. However, _U_ may {@{map different objects to the same set}@} and, {@{if this occurs, it will also map different morphisms to the same function}@}. <!--SR:!2027-10-05,769,344!2026-01-07,277,330!2025-12-24,267,330!2026-03-16,335,344-->

For example, if {@{_S_ and _T_ are two different topologies on the same set _X_}@}, then {@{\(_X_, _S_\) and \(_X_, _T_\) are distinct objects in the category __Top__ of topological spaces and continuous maps}@}, but {@{mapped to the same set _X_ by the forgetful functor __Top__ → __Set__}@}. Moreover, {@{the identity morphism \(_X_, _S_\) → \(_X_, _S_\) and the identity morphism \(_X_, _T_\) → \(_X_, _T_\) are considered distinct morphisms in __Top__}@}, but {@{they have the same underlying function, namely the identity function on _X_}@}. <!--SR:!2027-10-10,776,344!2026-03-24,341,344!2026-03-19,338,344!2026-01-07,277,330!2026-03-24,341,344-->

Similarly, {@{any set with four elements can be given two non-isomorphic group structures}@}: one {@{isomorphic to $\mathbb {Z} /2\mathbb {Z} \times \mathbb {Z} /2\mathbb {Z}$, and the other isomorphic to $\mathbb {Z} /4\mathbb {Z}$}@}. <!--SR:!2027-06-02,665,330!2026-01-26,294,330-->

## further examples

1. {@{Any group _G_}@} may be regarded as {@{an "abstract" category with one arbitrary object, $\ast$, and one morphism for each element of the group}@}. This would {@{not be counted as concrete according to the intuitive notion described at the top of this article}@}. But {@{every faithful [_G_-set](group%20action%20(mathematics).md) \(equivalently, every representation of _G_ as a [group of permutations](permutation%20group.md)\)}@} determines {@{a faithful functor _G_ → __Set__}@}. (annotation: this is a {@{[hom functor](hom%20functor.md) $\hom(\ast, -)$}@}, which sends {@{the object $*$ to $\hom_G(\ast, \ast)$ and a morphism $f: \ast \to \ast$ to $f \circ -: (\ast \to \ast) \to (\ast \to \ast)$}@}.) Since {@{every group acts faithfully on itself}@}, {@{_G_ can be made into a concrete category in at least one way}@}. <!--SR:!2025-12-02,251,330!2026-03-21,338,344!2027-01-10,534,310!2026-01-30,251,284!2026-03-22,339,344!2026-02-13,311,344!2026-11-15,504,324!2027-06-14,674,330!2027-05-09,648,330-->

2. Similarly, {@{any [poset](poset.md) _P_}@} may be regarded as {@{an abstract category with a unique arrow _x_ → _y_ whenever _x_ ≤ _y_}@}. This can be {@{made concrete by defining a functor _D_ : _P_ → __Set__}@} which maps {@{each object _x_ to $D(x)=\{a\in P:a\leq x\}$ \(annotation: the subset of poset not greater than $x$\)}@} and {@{each arrow _x_ → _y_ to the inclusion map $D(x)\hookrightarrow D(y)$ \(annotation: note that $D(x) \subseteq D(y)$, and the inclusion map is defined as $f: D(x) \to D(y) := x \mapsto x$, i.e. the identity function from $D(x)$ to $D(y)$\)}@}. <!--SR:!2025-12-08,255,330!2026-03-25,342,344!2026-03-21,338,344!2026-12-06,469,304!2025-09-02,4,345-->

3. {@{The category __[Rel](category%20of%20relations.md)__}@} whose {@{objects are [sets](set%20(mathematics).md) and whose morphisms are [relations](relation%20(mathematics).md)}@} can be {@{made concrete by taking _U_}@} to map {@{each set _X_ to its power set $2^{X}$}@} and {@{each relation $R\subseteq X\times Y$ to the function $\rho :2^{X}\rightarrow 2^{Y}$ defined by $\rho (A)=\{y\in Y\mid \exists \,x\in A:xRy\}$ (annotation: intuitively, relations can be treated as multi-input multi-output functions)}@}. Noting that {@{power sets are [complete lattices](complete%20lattice.md) under inclusion}@}, {@{those functions between them arising from some relation _R_ in this way}@} are {@{exactly the [supremum-preserving maps](complete%20lattice.md#morphisms%20of%20complete%20lattices)}@}. Hence __Rel__ is {@{equivalent to a full subcategory of the category __Sup__ of [complete lattices](complete%20lattices.md) and their sup-preserving maps}@}. Conversely, starting from this equivalence we can {@{recover _U_ as the composite __Rel__ → __Sup__ → __Set__}@} of {@{the forgetful functor for __Sup__ with this embedding of __Rel__ in __Sup__ (annotation: embed __Rel__ into __Sup__, and then use the forgetful functor from __Sup__ to __Set__)}@}. <!--SR:!2027-07-10,693,330!2026-03-15,334,344!2025-10-26,216,324!2026-02-08,306,344!2026-12-02,467,304!2026-10-31,497,324!2027-01-05,542,324!2026-07-21,421,324!2026-11-01,453,270!2025-10-08,190,310!2025-12-30,222,270-->

4. {@{The category __Set__<sup>op</sup> can be embedded into __Rel__}@} by representing {@{each set as itself}@} and {@{each function _f_: _X_ → _Y_ as the relation from _Y_ to _X_ formed as the set of pairs \(_f_\(_x_\), _x_\) for all _x_ ∈ _X_}@}; hence {@{__Set__<sup>op</sup> is concretizable}@}. {@{The forgetful functor which arises in this way}@} is {@{the [contravariant powerset functor](functor.md#examples) __Set__<sup>op</sup> → __Set__}@} (annotation: keeping in mind that {@{the functor __Rel__ → __Set__ sends each set to its power set from the previous example}@}, explaining why it is the contravariant power set functor). <!--SR:!2026-02-07,306,344!2027-05-04,645,330!2026-02-01,278,290!2026-03-23,340,344!2026-06-09,341,290!2026-03-25,342,344!2025-12-21,248,324-->

5. It follows from the previous example that {@{the opposite of any concretizable category _C_ is again concretizable}@}, since if {@{_U_ is a faithful functor _C_ → __Set__}@} then {@{_C_<sup>op</sup> may be equipped with the composite _C_<sup>op</sup> → __Set__<sup>op</sup> → __Set__}@}. <!--SR:!2025-10-03,199,324!2025-10-08,190,310!2026-02-20,316,344-->

6. If {@{_C_ is any small category}@}, then there {@{exists a faithful functor _P_ : __Set__<sup>_C_<sup>op</sup></sup> → __Set__ which maps a presheaf _X_ to the coproduct $\coprod _{c\in \mathrm {ob} C}X(c)$}@}. (annotation: Intuitively, the presheaf _X_ {@{is a functor _C_<sup>op</sup> → __Set__ that indexes __Set__ using _C_<sup>op</sup>}@}. Then the functor {@{flattens this indexing using the coproduct}@}.) By {@{composing this with the [Yoneda embedding](Yoneda%20embedding.md#the%20Yoneda%20embedding) _Y_:_C_ → __Set__<sup>_C_<sup>op</sup></sup>}@} one {@{obtains a faithful functor _C_ → __Set__}@}. <!--SR:!2026-01-18,286,330!2026-02-09,258,284!2027-07-14,699,330!2026-12-07,487,310!2026-04-26,343,304!2025-12-22,249,324-->

7. For {@{technical reasons}@}, {@{the category __Ban__<sub>1</sub> of [Banach spaces](Banach%20spaces.md) and [linear contractions](contraction%20(operator%20theory).md)}@} is often {@{equipped not with the "obvious" forgetful functor}@} but {@{the functor _U_<sub>1</sub> : __Ban__<sub>1</sub> → __Set__ which maps a Banach space to its \(closed\) [unit ball](unit%20ball.md)}@}. <!--SR:!2026-03-16,335,344!2026-04-25,342,304!2026-03-23,340,344!2026-09-27,455,310-->

8. {@{The category __Cat__ whose objects are small categories and whose morphisms are functors}@} can be {@{made concrete by sending}@} {@{each category __C__ to the set containing its objects and morphisms}@}. Functors can be {@{simply viewed as functions acting on the objects and morphisms}@}. <!--SR:!2027-05-06,645,330!2026-01-07,277,330!2025-11-15,235,330!2026-03-25,342,344-->

## counter-examples

{@{The category __[hTop](homotopy%20category%20of%20topological%20spaces.md)__}@}, where {@{the objects are [topological spaces](topological%20space.md) and the morphisms are [homotopy classes](homotopy.md) of continuous functions}@}, is {@{an example of a category that is not concretizable}@}. While {@{the objects are sets \(with additional structure\)}@}, {@{the morphisms are not actual functions between them, but rather classes of functions}@}. The fact that {@{there does not exist _any_ faithful functor from __hTop__ to __Set__}@} was first {@{proven by [Peter Freyd](Peter%20Freyd.md)}@}. In the same article, Freyd cites an earlier result that {@{the category of "small categories and [natural equivalence](natural%20equivalence.md)-classes of functors" also fails to be concretizable}@}. <!--SR:!2027-06-11,669,330!2027-04-19,596,290!2026-03-22,339,344!2025-12-11,257,330!2025-10-21,212,324!2025-10-25,215,324!2025-12-25,255,290!2025-10-24,188,270-->

## implicit structure of concrete categories

Given {@{a concrete category \(_C_, _U_\) and a [cardinal number](cardinal%20number.md) _N_}@}, let {@{_U<sup>N</sup>_ be the functor _C_ → __Set__ determined by _U<sup>N</sup>\(c\) = \(U\(c\)\)<sup>N</sup>_ (annotation: duplicate the result of $U$ for $N$ many times)}@}. Then {@{a [subfunctor](subfunctor.md) of _U<sup>N</sup>_}@} is called {@{an _N-ary predicate_}@} and {@{a [natural transformation](natural%20transformation.md) _U<sup>N</sup>_ → _U_}@} {@{an _N-ary operation_}@}. <!--SR:!2026-03-24,341,344!2027-04-30,642,330!2027-05-18,634,324!2026-09-23,451,310!2025-09-07,177,310!2026-11-27,499,310-->

The class of {@{all _N_-ary predicates and _N_-ary operations of a concrete category \(_C_,_U_\)}@}, with {@{_N_ ranging over the class of all cardinal numbers}@}, forms {@{a [large](proper%20class.md) [signature](signature%20(logic).md)}@}. {@{The category of models (annotation: model theory...?) for this signature}@} then {@{contains a full subcategory which is [equivalent](equivalence%20of%20categories.md) to _C_}@}. <!--SR:!2026-08-17,401,304!2027-06-10,668,330!2026-02-17,313,344!2025-10-18,210,324!2025-10-09,66,361-->

## relative concreteness

In {@{some parts of category theory, most notably [topos theory](topos%20theory.md)}@}, it is common to {@{replace the category __Set__ with a different category _X_}@}, often called {@{a _base category_}@}. For this reason, it makes sense to {@{call a pair \(_C_, _U_\) where _C_ is a category and _U_ a faithful functor _C_ → _X_}@} {@{a __concrete category over__ _X_}@}. For example, it may be useful to think of {@{the models (annotation: model theory...?) of a theory [with _N_ sorts](structure%20(mathematical%20logic).md#many-sorted%20structures)}@} as {@{forming a concrete category over __Set__<sup>_N_</sup>}@}. <!--SR:!2027-07-14,694,330!2025-12-13,259,330!2026-08-26,440,310!2026-02-17,314,344!2025-12-07,255,330!2025-10-11,192,310!2027-07-07,693,330-->

In this context, {@{a concrete category over __Set__}@} is sometimes called {@{a _construct_}@}. <!--SR:!2026-02-09,307,344!2025-12-07,255,330-->

## notes

1. <a id="CITEREFMac LaneBirkhoff1999"></a> [Mac Lane, Saunders](Saunders%20Mac%20Lane.md); [Birkhoff, Garrett](Garrett%20Birkhoff.md) \(1999\), _Algebra_ \(3rd ed.\), AMS Chelsea, [ISBN](ISBN%20(identifier).md) [978-0-8218-1646-2](https://en.wikipedia.org/wiki/Special:BookSources/978-0-8218-1646-2) <a id="^ref-1"></a>^ref-1

## references

This text incorporates [content](https://en.wikipedia.org/wiki/concrete_category) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- Adámek, Jiří, Herrlich, Horst, & Strecker, George E.; \(1990\). [_Abstract and Concrete Categories_](http://katmat.math.uni-bremen.de/acc/acc.pdf) \(4.2MB PDF\). Originally publ. John Wiley & Sons. [ISBN](ISBN%20(identifier).md) [0-471-60922-6](https://en.wikipedia.org/wiki/Special:BookSources/0-471-60922-6). \(now free on-line edition\).
- Freyd, Peter; \(1970\). [_Homotopy is not concrete_](http://www.tac.mta.ca/tac/reprints/articles/6/tr6abs.html). Originally published in: The Steenrod Algebra and its Applications, Springer Lecture Notes in Mathematics Vol. 168. Republished in a free on-line journal: Reprints in Theory and Applications of Categories, No. 6 \(2004\), with the permission of Springer-Verlag.
- Rosický, Jiří; \(1981\). _Concrete categories and infinitary languages_. [_Journal of Pure and Applied Algebra_](http://www.sciencedirect.com/science/journal/00224049), Volume 22, Issue 3.

> [Category](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Category theory](https://en.wikipedia.org/wiki/Category:Category%20theory)
