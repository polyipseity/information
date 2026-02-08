---
aliases:
  - star-mesh transform
  - star-mesh transformation
  - star-mesh transformations
  - star-mesh transforms
  - star-polygon transform
  - star-polygon transformation
  - star-polygon transformations
  - star-polygon transforms
tags:
  - flashcard/active/general/eng/star-mesh_transform
  - language/in/English
---

# star-mesh transform

The {@{__star-mesh transform__, or __star-polygon transform__}@}, is {@{a mathematical [circuit analysis](circuit%20analysis.md) technique to transform a [resistive network](network%20analysis%20(electrical%20circuits).md) into an equivalent network with one less node}@}. The equivalence follows from {@{the [Schur complement](Schur%20complement.md) identity applied to the [Kirchhoff matrix](Kirchhoff%20matrix.md) of the network}@}. <!--SR:!2026-02-16,259,330!2026-02-25,266,330!2028-01-04,776,330-->

> {@{![star-mesh transform](../../archives/Wikimedia%20Commons/Star-mesh%20transform.svg)}@} <!--SR:!2029-01-29,1097,350-->

{@{The equivalent impedance betweens nodes A and B}@} is given by: {@{$$z_{\text{AB} }=z_{\text{A} }z_{\text{B} }\sum {\frac {1}{z} },$$}@} where {@{$z_{\text{A} }$ is the impedance between node A and the central node being removed}@}. <!--SR:!2026-03-25,286,330!2026-03-26,287,330!2028-03-22,786,330-->

The transform {@{replaces _N_ resistors with ${\frac {1}{2} }N(N-1)$ resistors}@}. For {@{$N>3$, the result is an increase in the number of resistors}@}, so {@{the transform has no general inverse without additional constraints}@}. <!--SR:!2029-01-28,1096,350!2026-02-21,263,330!2029-02-25,1118,350-->

It is {@{possible, though not necessarily efficient}@}, to {@{transform an arbitrarily complex two-terminal resistive network into a single equivalent resistor}@} by {@{repeatedly applying the star-mesh transform to eliminate each non-terminal node}@}. <!--SR:!2026-03-04,272,330!2026-03-27,288,330!2026-03-09,276,330-->

## special cases

When _N_ is:

1. For a single dangling resistor, ::@:: the transform eliminates the resistor. <!--SR:!2028-03-06,826,330!2029-02-01,1100,350-->
2. For two resistors, ::@:: the "star" is simply the two resistors in series, and the transform yields a single equivalent resistor. <!--SR:!2029-04-09,1156,350!2028-06-14,883,330-->
3. The special case of three resistors ::@:: is better known as the [Y-Δ transform](Y-Δ%20transform.md). Since the result also has three resistors, this transform has an inverse Δ-Y transform. <!--SR:!2029-03-31,1149,350!2026-04-02,294,330-->

## see also

- [Topology of electrical circuits](topology%20(electrical%20circuits).md)
- [Network analysis \(electrical circuits\)](network%20analysis%20(electrical%20circuits).md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/star-mesh_transform) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- <a id="CITEREFvan LierOtten1973"></a> van Lier, M.; Otten, R. \(March 1973\). "Planarization by transformation". _IEEE Transactions on Circuit Theory_. __20__ \(2\): 169–171. [doi](doi%20(identifier).md):[10.1109/TCT.1973.1083633](https://doi.org/10.1109%2FTCT.1973.1083633).
- <a id="CITEREFBedrosian1961"></a> Bedrosian, S. \(December 1961\). "Converse of the Star-Mesh Transformation". _IRE Transactions on Circuit Theory_. __8__ \(4\): 491–493. [doi](doi%20(identifier).md):[10.1109/TCT.1961.1086832](https://doi.org/10.1109%2FTCT.1961.1086832).
- E.B. Curtis, D. Ingerman, J.A. Morrow. Circular planar graphs and resistor networks. Linear Algebra and its Applications. Volume 283, Issues 1–3, 1 November 1998, pp. 115–150\| doi = [https://doi.org/10.1016/S0024-3795\(98\)10087-3](https://doi.org/10.1016/S0024-3795(98)10087-3).

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Electrical circuits](https://en.wikipedia.org/wiki/Category:Electrical%20circuits)
> - [Circuit theorems](https://en.wikipedia.org/wiki/Category:Circuit%20theorems)
> - [Transforms](https://en.wikipedia.org/wiki/Category:Transforms)
