---
aliases:
  - canonical projection
  - canonical projections
  - inclusion function
  - inclusion functions
  - inclusion map
  - inclusion maps
  - insertion
  - insertions
  - natural injection
  - natural injections
tags:
  - flashcard/active/general/eng/inclusion_map
  - language/in/English
---

# inclusion map

> {@{![$A$ is a [subset](subset.md) of $B$, and $B$ is a [superset](subset.md) of $A$.](../../archives/Wikimedia%20Commons/Venn%20A%20subset%20B.svg)}@}
>
> $A$ is {@{a [subset](subset.md) of $B$}@}, and $B$ is {@{a [superset](subset.md) of $A$}@}. <!--SR:!2025-12-18,263,330!2026-01-01,274,330!2026-01-19,287,330-->

In {@{[mathematics](mathematics.md)}@}, if {@{$A$ is a [subset](subset.md) of $B$}@}, then {@{the __inclusion map__}@} is {@{the [function](function%20(mathematics).md) [$\iota$](ι.md) that sends each element $x$ of $A$ to $x$, treated as an element of $B$}@}: {@{$$\iota :A\rightarrow B,\qquad \iota (x)=x.$$}@} An inclusion map may also be referred to as {@{an __inclusion function__, an __insertion__,<sup>[\[1\]](#^ref-1)</sup> or a __canonical injection__}@}. <!--SR:!2025-12-21,264,330!2025-12-26,269,330!2025-12-19,262,330!2025-12-28,271,330!2026-01-24,292,330!2025-12-12,258,330-->

{@{A "hooked arrow"}@} \([U+](Unicode.md){@{21AA ↪ RIGHTWARDS ARROW WITH HOOK}@}\)<sup>[\[2\]](#^ref-2)</sup> is sometimes {@{used in place of the function arrow above to denote an inclusion map}@}; thus: {@{$$\iota :A\hookrightarrow B.$$}@} \(However, some authors {@{use this hooked arrow for any [embedding](embedding.md)}@}.\) <!--SR:!2025-12-29,272,330!2025-09-20,174,270!2025-09-14,183,310!2025-10-13,194,310!2025-12-17,262,330-->

{@{This and other analogous [injective](injective.md) functions<sup>[\[3\]](#^ref-3)</sup> from [substructures](substructure%20(mathematics).md)}@} are sometimes called {@{__natural injections__}@}. <!--SR:!2026-11-12,488,310!2026-01-24,292,330-->

Given {@{any [morphism](morphism.md) $f$ between [objects](object%20(category%20theory).md) $X$ and $Y$}@}, if {@{there is an inclusion map $\iota :A\to X$ into the [domain](domain%20of%20a%20function.md) $X$}@}, then one can form {@{the [restriction](restriction%20(mathematics).md) $f\circ \iota$ of $f$}@}. In many instances, one can also construct {@{a canonical inclusion into the [codomain](codomain.md) $R\to Y$}@} known as {@{the [range](range%20of%20a%20function.md) of $f$}@}. <!--SR:!2026-01-21,289,330!2025-12-13,258,330!2025-12-08,255,330!2025-10-10,191,310!2026-01-22,290,330-->

## applications of inclusion maps

Inclusion maps tend to be {@{[homomorphisms](homomorphism.md) of [algebraic structures](algebraic%20structure.md)}@}; thus, such inclusion maps are {@{[embeddings](embedding.md)}@}. More precisely, given {@{a substructure closed under some operations}@}, the inclusion map will be {@{an embedding for tautological reasons}@}. For example, for {@{some binary operation $\star$}@}, to {@{require that $$\iota (x\star y)=\iota (x)\star \iota (y)$$}@} is simply to say that {@{$\star$ is consistently computed in the sub-structure and the large structure}@}. The case of {@{a [unary operation](unary%20operation.md) is similar}@}; but one should also {@{look at [nullary](nullary.md#nullary) operations, which pick out a _constant_ element}@}. Here the point is that {@{[closure](closure%20(mathematics).md) means such constants must already be given in the substructure}@}. <!--SR:!2027-10-17,768,330!2025-12-03,251,330!2026-01-20,288,330!2026-01-26,294,330!2025-12-08,255,330!2025-12-18,261,330!2027-09-21,748,330!2025-12-13,259,330!2025-12-14,259,330!2025-09-18,186,310-->

Inclusion maps are seen in {@{[algebraic topology](algebraic%20topology.md)}@} where if {@{$A$ is a [strong deformation retract](strong%20deformation%20retract.md) of $X$}@}, the inclusion map yields {@{an [isomorphism](group%20isomorphism.md) between all [homotopy groups](homotopy%20groups.md) \(that is, it is a [homotopy equivalence](homotopy.md)\)}@}. <!--SR:!2026-01-15,283,330!2026-04-29,338,290!2026-10-12,438,270-->

{@{Inclusion maps in [geometry](geometry.md)}@} come in {@{different kinds}@}: for example {@{[embeddings](embedding.md) of [submanifolds](submanifold.md)}@}. {@{[Contravariant](covariance%20and%20contravariance%20of%20functors.md#covariance%20and%20contravariance) objects}@} \(which is to say, {@{objects that have [pullbacks](pullback.md)}@}; these are called {@{[covariant](covariance%20and%20contravariance%20of%20vectors.md) in an older and unrelated terminology}@}\) such as {@{[differential forms](differential%20form.md)}@} _restrict_ to {@{submanifolds, giving a mapping in the _other direction_}@}. Another example, more sophisticated, is that of {@{[affine schemes](affine%20scheme.md)}@}, for which {@{the inclusions $$\operatorname {Spec} \left(R/I\right)\to \operatorname {Spec} (R)$$ and $$\operatorname {Spec} \left(R/I^{2}\right)\to \operatorname {Spec} (R)$$}@} may be {@{different [morphisms](morphism.md)}@}, where {@{$R$ is a [commutative ring](commutative%20ring.md) and $I$ is an [ideal](ideal%20(ring%20theory).md) of $R$}@}. <!--SR:!2025-12-27,270,330!2025-10-12,193,310!2025-09-25,191,310!2027-09-15,743,330!2025-12-20,263,330!2026-01-02,275,330!2026-06-22,345,290!2026-02-25,294,290!2027-05-28,661,330!2026-06-16,389,310!2026-01-25,293,330!2025-09-21,189,310-->

## see also

- [Cofibration](cofibration.md) – ::@:: continuous mapping between topological spaces <!--SR:!2025-09-13,169,270!2027-10-12,764,330-->
- [Identity function](identity%20function.md) – ::@:: In mathematics, a function that always returns the same value that was used as its argument <!--SR:!2025-12-08,255,330!2025-12-15,260,330-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/inclusion_map) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFMacLaneBirkhoff1967"></a> MacLane, S.; Birkhoff, G. \(1967\). _Algebra_. Providence, RI: AMS Chelsea Publishing. p. 5. [ISBN](ISBN%20(identifier).md) [0-8218-1646-2](https://en.wikipedia.org/wiki/Special:BookSources/0-8218-1646-2). Note that "insertion" is a function _S_ → _U_ and "inclusion" a relation _S_ ⊂ _U_; every inclusion relation gives rise to an insertion function. <a id="^ref-1"></a>^ref-1
2. ["Arrows – Unicode"](https://www.unicode.org/charts/PDF/U2190.pdf) \(PDF\). [Unicode Consortium](Unicode%20Consortium.md). Retrieved 2017-02-07. <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFChevalley1956"></a> Chevalley, C. \(1956\). [_Fundamental Concepts of Algebra_](https://archive.org/details/fundamentalconce00chev_0). New York, NY: Academic Press. p. [1](https://archive.org/details/fundamentalconce00chev_0/page/1). [ISBN](ISBN%20(identifier).md) [0-12-172050-0](https://en.wikipedia.org/wiki/Special:BookSources/0-12-172050-0). <a id="^ref-3"></a>^ref-3

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Basic concepts in set theory](https://en.wikipedia.org/wiki/Category:Basic%20concepts%20in%20set%20theory)
> - [Functions and mappings](https://en.wikipedia.org/wiki/Category:Functions%20and%20mappings)
