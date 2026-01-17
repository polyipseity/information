---
aliases:
  - kernel
  - kernel (category theory)
  - kernels
  - kernels (category theory)
tags:
  - flashcard/active/general/eng/kernel__category_theory_
  - language/in/English
---

# kernel

- For other uses, see [Kernel \(disambiguation\)](kernel%20(disambiguation).md).

<!-- | ![](../../archives/Wikimedia%20Commons/Question%20book-new.svg) | This article __needs additional citations for [verification](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)__. Please help [improve this article](https://en.wikipedia.org/wiki/Special:EditPage/Kernel%20%28category%20theory%29) by [adding citations to reliable sources](https://en.wikipedia.org/wiki/Help:Referencing%20for%20beginners). Unsourced material may be challenged and removed._Find sources:_ ["Kernel" category theory](https://www.google.com/search?as_eq=wikipedia&q=%22Kernel%22+category+theory) – [news](https://www.google.com/search?tbm=nws&q=%22Kernel%22+category+theory+-wikipedia&tbs=ar:1) __·__ [newspapers](https://www.google.com/search?&q=%22Kernel%22+category+theory&tbs=bkt:s&tbm=bks) __·__ [books](https://www.google.com/search?tbs=bks:1&q=%22Kernel%22+category+theory+-wikipedia) __·__ [scholar](https://scholar.google.com/scholar?q=%22Kernel%22+category+theory) __·__ [JSTOR](https://www.jstor.org/action/doBasicSearch?Query=%22Kernel%22+category+theory&acc=on&wc=on) _\(December 2009\)__\([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ | -->

In {@{[category theory](category%20theory.md) and its applications to other branches of [mathematics](mathematics.md)}@}, {@{__kernels__}@} are a generalization of {@{the kernels of [group homomorphisms](group%20homomorphism.md), the kernels of [module homomorphisms](module%20homomorphism.md) and certain other [kernels from algebra](kernel%20(algebra).md)}@}. Intuitively, {@{the kernel of the [morphism](morphism.md) _f_ : _X_ → _Y_}@} is {@{the "most general" morphism _k_ : _K_ → _X_ that yields zero when composed with \(followed by\) _f_}@}. <!--SR:!2026-01-28,298,342!2026-02-10,308,342!2028-07-18,915,302!2028-09-13,1041,350!2026-02-16,313,342-->

Note that {@{[kernel pairs](kernel%20pair.md) and [difference kernels](difference%20kernel.md) \(also known as binary [equalisers](equaliser%20(mathematics).md)\)}@} sometimes {@{go by the name "kernel"}@}; while {@{related, these aren't quite the same thing and are not discussed in this article}@}. <!--SR:!2028-04-20,919,342!2026-03-14,333,342!2026-10-06,472,310-->

## definition

Let {@{__C__ be a [category](category%20theory.md)}@}. In order to {@{define a kernel in the general category-theoretical sense}@}, __C__ {@{needs to have [zero morphisms](zero%20morphism.md)}@}. In that case, if {@{_f_ : _X_ → _Y_ is an arbitrary [morphism](morphism.md) in __C__}@}, then {@{a kernel of _f_}@} is {@{an [equaliser](equaliser%20(mathematics).md) of _f_ and the zero morphism from _X_ to _Y_. In symbols}@}: <p> &emsp; {@{ker\(_f_\) = eq\(_f_, 0<sub>_XY_</sub>\)}@} <p> To be more explicit, {@{the following [universal property](universal%20property.md)}@} can be used. A kernel of _f_ is {@{an [object](object%20(category%20theory).md) _K_ together with a morphism _k_ : _K_ → _X_}@} such that: <!--SR:!2026-01-28,298,342!2026-03-17,336,342!2028-04-22,921,342!2028-04-29,925,342!2026-02-15,311,342!2027-05-15,632,322!2026-10-25,485,322!2028-11-16,1092,350!2026-02-14,311,342-->

- _f_<!-- markdown separator -->&hairsp;∘<!-- markdown separator -->_k_ is ::@:: the zero morphism from _K_ to _Y_; <p> ![This diagram visualises the first property of kernels in category theory.](../../archives/Wikimedia%20Commons/First%20property%20of%20the%20kernel.svg) <!--SR:!2027-03-30,554,310!2027-02-22,548,322-->
- Given any morphism _k′_ : _K′_ → _X_ such that _f_<!-- markdown separator -->&hairsp;∘<!-- markdown separator -->_k′_ is the zero morphism, ::@:: there is a unique morphism _u_ : _K′_ → _K_ such that _k_<!-- markdown separator -->∘<!-- markdown separator -->_u_ = _k′_. <p> ![This commutative diagram visualises the properties of kernels in category theory.](../../archives/Wikimedia%20Commons/Properties%20of%20a%20kernel.svg) <!--SR:!2026-02-13,259,282!2027-05-26,624,290-->

As for {@{every universal property}@}, there is {@{a unique isomorphism between two kernels of the same morphism}@}, and the morphism _k_ is {@{always a [monomorphism](monomorphism.md) \(in the categorical sense\)}@}. So, it is common to {@{talk of _the_ kernel of a morphism}@}. In {@{[concrete categories](concrete%20categories.md)}@}, one can thus {@{take a [subset](subset.md) of _K′_ for _K_}@}, in which case, {@{the morphism _k_ is the [inclusion map](inclusion%20map.md) (annotation: from _K_ to _X_; and _u_ is the inclusion map from _K'_ to _K_)}@}. This allows one to {@{talk of _K_ as the kernel, since _k_ is implicitly defined by _K_}@}. There are {@{non-concrete categories}@}, where one can {@{similarly define a "natural" kernel, such that _K_ defines _k_ implicitly}@}. <!--SR:!2029-01-16,1141,350!2027-09-22,759,342!2027-03-23,594,322!2026-03-14,333,342!2026-07-17,418,322!2026-02-16,312,342!2026-12-30,500,310!2026-03-13,332,342!2026-02-01,300,342!2027-07-15,695,330-->

{@{Not every morphism needs to have a kernel}@}, but {@{if it does, then all its kernels are isomorphic in a strong sense}@}: if {@{_k_ : _K_ → _X_ and _ℓ_ : _L_ → _X_ are kernels of _f_ : _X_ → _Y_}@}, then there {@{exists a unique [isomorphism](isomorphism.md) φ : _K_ → _L_ such that _ℓ_<!-- markdown separator -->∘φ = _k_}@}. <!--SR:!2028-07-06,966,342!2027-07-18,707,342!2027-09-18,756,342!2028-03-24,896,342-->

## examples

Kernels are familiar in {@{many categories from [abstract algebra](abstract%20algebra.md)}@}, such as {@{the category of [groups](group%20(algebra).md) or the category of \(left\) [modules](module%20(mathematics).md) over a fixed [ring](ring%20(mathematics).md) \(including [vector spaces](vector%20space.md) over a fixed [field](field%20(mathematics).md)\)}@}. To be explicit, if {@{_f_ : _X_ → _Y_ is a [homomorphism](homomorphism.md) in one of these categories}@}, and _K_ is {@{its [kernel in the usual algebraic sense](kernel%20(algebra).md)}@}, then {@{_K_ is a [subalgebra](subalgebra.md) of _X_}@} and {@{the inclusion homomorphism from _K_ to _X_ is a kernel in the categorical sense}@}. <!--SR:!2026-02-07,305,342!2026-05-25,303,250!2026-07-16,417,322!2026-02-14,310,342!2028-06-07,946,342!2027-10-04,768,342-->

Note that in {@{the category of [monoids](monoid.md)}@}, {@{category-theoretic kernels exist just as for groups}@}, but these kernels {@{don't carry sufficient information for algebraic purposes}@}. Therefore, {@{the notion of kernel studied in monoid theory is slightly different}@} \(see [\#Relationship to algebraic kernels](#relationship%20to%20algebraic%20kernels) below\). <!--SR:!2027-07-23,711,342!2026-05-25,360,302!2029-02-11,1162,350!2026-01-30,300,342-->

In {@{the [category of unital rings](category%20of%20rings.md)}@}, there are {@{no kernels in the category-theoretic sense; indeed, this category does not even have zero morphisms}@}. Nevertheless, there is {@{still a notion of kernel studied in ring theory that corresponds to kernels in the [category of non-unital rings](category%20of%20rings.md#rings%20without%20identity)}@}. <!--SR:!2028-04-30,926,342!2026-02-11,309,342!2026-01-29,284,302-->

In {@{the category of [pointed topological spaces](pointed%20space.md)}@}, if {@{_f_ : _X_ → _Y_ is a continuous pointed map}@}, then {@{the preimage of the distinguished point (annotation: in _Y_), _K_, is a subspace of _X_}@}. {@{The inclusion map of _K_ into _X_}@} is {@{the categorical kernel of _f_}@}. <!--SR:!2028-04-11,911,342!2026-01-28,298,342!2026-02-06,304,342!2026-03-15,334,342!2028-02-18,873,342-->

## relation to other categorical concepts

{@{The dual concept to that of kernel}@} is {@{that of [cokernel](cokernel.md)}@}. That is, the kernel of a morphism is {@{its cokernel in the [opposite category](opposite%20category.md), and vice versa}@}. <!--SR:!2026-01-26,296,342!2026-02-05,304,342!2026-03-16,335,342-->

As mentioned above, a kernel is {@{a type of binary equaliser, or [difference kernel](difference%20kernel.md)}@}. Conversely, in {@{a [preadditive category](preadditive%20category.md)}@}, {@{every binary equaliser can be constructed as a kernel}@}. To be specific, {@{the equaliser of the morphisms _f_ and _g_}@} is {@{the kernel of the [difference](subtraction.md) _g_ − _f_}@}. In symbols: <p> &emsp; {@{eq \(_f_, <!-- markdown separator -->_g_\) = ker \(_g_ − _f_\)}@}. <p> It is because of this fact that {@{binary equalisers are called "difference kernels"}@}, even in {@{non-preadditive categories where morphisms cannot be subtracted}@}. <!--SR:!2026-01-29,299,342!2026-05-24,359,302!2026-02-15,312,342!2028-06-08,947,342!2026-01-27,297,342!2027-06-29,686,330!2028-10-13,1064,350!2026-06-09,348,302-->

{@{Every kernel, like any other equaliser}@}, is {@{a [monomorphism](monomorphism.md)}@}. Conversely, {@{a monomorphism is called _[normal](normal%20morphism.md)_ if it is the kernel of some morphism}@}. A category is called {@{_normal_ if every monomorphism is normal}@}. <!--SR:!2026-01-29,299,342!2028-03-31,907,342!2027-02-06,528,310!2027-09-15,734,330-->

{@{[Abelian categories](abelian%20categories.md)}@}, in particular, are {@{always normal}@}. In this situation, {@{the kernel of the [cokernel](cokernel.md) of any morphism}@} \(which {@{always exists in an abelian category}@}\) turns out to be {@{the [image](image%20(category%20theory).md) of that morphism}@}; in symbols: <p> &emsp; {@{im _f_ = ker coker _f_ \(in an abelian category\)}@} <p> When {@{_m_ is a monomorphism}@}, it {@{must be its own image}@}; thus, not only are {@{abelian categories normal, so that every monomorphism is a kernel}@}, but we also know {@{_which_ morphism the monomorphism is a kernel of, to wit, its cokernel}@}. In symbols: &emsp; {@{_m_ = ker \(coker _m_\) \(for monomorphisms in an abelian category\)}@} <!--SR:!2029-02-12,1163,350!2028-02-28,881,342!2027-06-23,678,330!2026-01-30,300,342!2028-04-06,907,342!2028-03-29,900,342!2026-12-12,487,310!2026-02-21,317,342!2027-01-24,462,282!2028-05-24,860,290!2026-06-01,365,302-->

## relationship to algebraic kernels

{@{[Universal algebra](universal%20algebra.md)}@} defines {@{a [notion of kernel](kernel%20(universal%20algebra).md) for homomorphisms between two [algebraic structures](algebraic%20structure.md) of the same kind}@}. This concept of kernel measures {@{how far the given homomorphism is from being [injective](injective.md)}@}. There is {@{some overlap between this algebraic notion and the categorical notion of kernel}@} since {@{both generalize the situation of groups and modules mentioned above}@}. In general, however, the universal-algebraic notion of kernel is {@{more like the category-theoretic concept of [kernel pair](kernel%20pair.md)}@}. In particular, kernel pairs can be used to {@{interpret kernels in monoid theory or ring theory in category-theoretic terms}@}. <!--SR:!2026-03-12,331,342!2027-01-07,516,322!2028-10-24,1074,350!2028-05-29,949,342!2028-02-29,881,342!2027-09-09,686,322!2026-03-31,321,302-->

## sources

This text incorporates [content](https://en.wikipedia.org/wiki/kernel_(category_theory)) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- <a id="CITEREFAwodey2010"></a> [Awodey, Steve](Steve%20Awodey.md) \(2010\) \[2006\]. [_Category Theory_](https://web.archive.org/web/20180521155021/http://angg.twu.net/MINICATS/awodey__category_theory.pdf) \(PDF\). Oxford Logic Guides. Vol. 49 \(2nd ed.\). Oxford University Press. [ISBN](ISBN%20(identifier).md) [978-0-19-923718-0](https://en.wikipedia.org/wiki/Special:BookSources/978-0-19-923718-0). Archived from [the original](http://angg.twu.net/MINICATS/awodey__category_theory.pdf) \(PDF\) on 2018-05-21. Retrieved 2018-06-29.
- [Kernel](https://ncatlab.org/nlab/show/kernel) at the [_n_<!-- markdown separator -->Lab](nLab.md)

> [Category](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Category theory](https://en.wikipedia.org/wiki/Category:Category%20theory)
