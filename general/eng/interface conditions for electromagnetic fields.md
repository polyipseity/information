---
aliases:
  - interface condition for electromagnetic field
  - interface condition for electromagnetic fields
  - interface conditions for electromagnetic field
  - interface conditions for electromagnetic fields
tags:
  - flashcard/active/general/eng/interface_conditions_for_electromagnetic_fields
  - language/in/English
---

# interface conditions for electromagnetic fields

<!-- | [papers](https://www.google.com/search?&q=%22Interface+conditions+for+electromagnetic+fields%22&tbs=bkt:s&tbm=bks) __·__ [books](https://www.google.com/search?tbs=bks:1&q=%22Interface+conditions+for+electromagnetic+fields%22+-wikipedia) __·__ [scholar](https://scholar.google.com/scholar?q=%22Interface+conditions+for+electromagnetic+fields%22) __·__ [JSTOR](https://www.jstor.org/action/doBasicSearch?Query=%22Interface+conditions+for+electromagnetic+fields%22&acc=on&wc=on) _\(September 2023\)__\([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ | -->

{@{Interface conditions}@} describe {@{the behaviour of [electromagnetic fields](electromagnetic%20fields.md); [electric field](electric%20field.md), [electric displacement field](electric%20displacement%20field.md), and the [magnetic field](magnetic%20field.md) at the interface of two materials}@}. {@{The differential forms of these equations}@} require that {@{there is always an [open neighbourhood](open%20neighbourhood.md#open%20neighbourhood) around the point to which they are applied}@}, otherwise {@{the vector fields and __H__ are not [differentiable](differentiable%20function.md)}@}. <!-- In other words, the medium must be continuous\[no need to be continuous\]\[This paragraph need to be revised, the wrong concept of "continuous" need to be corrected\]. --> On the interface of {@{two different media}@} with {@{different values for electrical [permittivity](permittivity.md) and magnetic [permeability](permeability%20(electromagnetism).md)}@}, that {@{condition does not apply}@}. <!--SR:!2025-09-13,60,318!2025-09-18,64,318!2025-09-24,69,318!2025-09-12,59,318!2025-09-24,69,318!2025-09-12,59,318!2025-09-12,59,318!2025-09-12,59,318-->

However, {@{the interface conditions for the electromagnetic field vectors}@} can be derived from {@{the integral forms of [Maxwell's equations](Maxwell's%20equations.md)}@}. <!--SR:!2025-09-13,60,318!2025-09-13,60,318-->

## interface conditions for electric field vectors

### electric field strength

\(annotation: $\mathbf E$\) ::@:: $$\mathbf {n} _{12}\times (\mathbf {E} _{2}-\mathbf {E} _{1})=\mathbf {0}$$ <!--SR:!2025-09-24,69,318!2026-01-08,133,298-->

where: <br/>
$\mathbf {n} _{12}$ <!-- flashcard ID: 89355df4-5adb-4753-a348-713d05c62a3b -->::@:: is [normal vector](normal%20vector.md) from medium 1 to medium 2. <!--SR:!2025-09-25,70,338!2026-03-27,211,338-->

Therefore, {@{the [tangential component](tangential%20component.md) of __E__}@} is {@{continuous across the interface}@}. <!--SR:!2025-09-23,68,318!2025-09-18,64,318-->

> Outline of proof from {@{[Faraday's law](Faraday's%20law%20of%20induction.md)}@}
>
> We begin with {@{the integral form of Faraday's law}@}: {@{$$\oint _{\partial \Sigma }\mathbf {E} \cdot d{\boldsymbol {\ell } }=-\int _{\Sigma }{\frac {\partial \mathbf {B} }{\partial t} }\cdot d\mathbf {A}$$}@}
>
> Choose {@{$\Sigma$ as a small square across the interface}@}. Then, have {@{the sides perpendicular to the interface shrink to infinitesimal length}@}. {@{The area of integration}@} now {@{looks like a line, which has zero area}@}. In other words: {@{$$\lim _{\text{line length}\to 0}\mathbf {A} =0$$}@}
>
> Since {@{$\partial \mathbf {B} /\partial t$ remains finite in this limit}@}, {@{the whole right hand side goes to zero}@}. All that is left is: {@{$$\oint _{\partial \Sigma }\mathbf {E} \cdot d{\boldsymbol {\ell } }=0$$}@}
>
> Two of {@{our sides are infinitesimally small}@}, leaving only {@{$$\int _{\text{medium 1} }\mathbf {E} \cdot d{\boldsymbol {\ell } }+\int _{\text{medium 2} }\mathbf {E} \cdot d{\boldsymbol {\ell } }=0$$}@}
>
> Assuming we made {@{our square small enough that E is roughly constant}@}, its magnitude can be {@{pulled out of the integral}@}. As {@{the remaining sides to our original loop, the $d{\boldsymbol {\ell } }$ in each region}@} {@{run in opposite directions}@}, so we define {@{one of them as the tangent unit vector ${\boldsymbol {t} }$}@} and the other as {@{$-{\boldsymbol {t} }$}@} {@{$$(\mathbf {E} _{2}\cdot {\boldsymbol {t} })l-(\mathbf {E} _{1}\cdot {\boldsymbol {t} })l=\mathbf {0}$$}@}
>
> After {@{dividing by l, and rearranging}@}, {@{$$(\mathbf {E} _{2}-\mathbf {E} _{1})\cdot {\boldsymbol {t} }=\mathbf {0}$$}@}
>
> This argument works {@{for any tangential direction}@}. {@{The difference in electric field dotted into _any_ tangential vector is zero}@}, meaning {@{only the components of $\mathbf {E}$ parallel to the normal vector can change between mediums}@}. Thus, the difference in electric field vector is {@{parallel to the normal vector}@}. {@{Two parallel vectors}@} always {@{have a cross product of zero}@}. {@{$$\mathbf {n} _{12}\times (\mathbf {E} _{2}-\mathbf {E} _{1})=\mathbf {0}$$}@} <!--SR:!2025-09-12,59,318!2025-09-24,69,318!2025-09-19,65,318!2025-09-18,64,318!2025-09-19,65,318!2025-09-18,64,318!2025-09-12,59,318!2025-09-24,69,318!2025-09-12,59,318!2025-09-19,65,318!2025-09-13,60,318!2025-09-19,65,318!2025-09-13,60,318!2025-09-24,69,318!2025-09-13,60,318!2025-09-19,65,318!2025-09-18,64,318!2025-09-13,60,318!2025-09-18,64,318!2025-09-19,65,318!2025-09-12,59,318!2025-09-19,65,318!2026-05-05,239,330!2025-09-18,64,318!2025-09-23,68,318!2025-09-19,65,318!2025-09-12,59,318!2025-09-24,69,318!2025-09-23,68,318-->

### electric displacement field

\(annotation: $\mathbf D$\) ::@:: $$(\mathbf {D} _{2}-\mathbf {D} _{1})\cdot \mathbf {n} _{12}=\sigma _{s}$$ <!--SR:!2025-09-18,64,318!2025-09-13,60,318-->

$\mathbf {n} _{12}$ ::@:: is the unit [normal vector](normal%20vector.md) from medium 1 to medium 2. <br/> <!--SR:!2025-09-28,73,338!2025-09-28,73,338-->
$\sigma _{s}$ ::@:: is the [surface charge](surface%20charge.md) [density](charge%20density.md) between the media \(unbounded charges only, not coming from polarization of the materials\). <!--SR:!2025-09-24,69,318!2025-09-24,69,318-->

This can be deduced by {@{using Gauss's law and similar reasoning as above}@}. <!--SR:!2025-09-24,69,318-->

Therefore, {@{the normal component of __D__}@} has {@{a step of surface charge on the interface surface}@}. If {@{there is no surface charge on the interface}@}, {@{the normal component of __D__ is continuous}@}. <!--SR:!2025-09-24,69,318!2025-09-18,64,318!2025-09-18,64,318!2025-09-19,65,318-->

## interface conditions for magnetic field vectors

### for magnetic flux density

\(annotation: $\mathbf B$\) ::@:: $$(\mathbf {B} _{2}-\mathbf {B} _{1})\cdot \mathbf {n} _{12}=0$$ <!--SR:!2025-09-24,69,318!2025-09-10,57,310-->

where: <br/>
$\mathbf {n} _{12}$ <!-- flashcard ID: 60a2ea19-b133-459c-889e-e4e159632daa -->::@:: is [normal vector](normal%20vector.md) from medium 1 to medium 2. <!--SR:!2025-09-27,72,338!2025-09-27,72,338-->

Therefore, {@{the normal component of __B__}@} is {@{continuous across the interface \(the same in both media\)}@}. <!--SR:!2025-09-13,60,318!2025-09-24,69,318-->

### for magnetic field strength

\(annotation: $\mathbf H$\) ::@:: $$\mathbf {n} _{12}\times (\mathbf {H} _{2}-\mathbf {H} _{1})=\mathbf {j} _{s}$$ <!--SR:!2025-09-13,60,318!2025-09-19,65,318-->

where: <br/>
$\mathbf {n} _{12}$ <!-- flashcard ID: 88bd7276-524c-48b2-b4d0-224cd3b21e56 -->::@:: is the unit [normal vector](normal%20vector.md) from medium 1 to medium 2. <br/> <!--SR:!2025-09-26,71,338!2025-09-25,70,338-->
$\mathbf {j} _{s}$ ::@:: is the surface [current density](current%20density.md) between the two media \(unbounded current only, not coming from polarisation of the materials\). <!--SR:!2025-09-18,63,310!2025-09-18,64,318-->

Therefore, {@{the [tangential component](tangential%20component.md) of __H__}@} is {@{discontinuous across the interface by an amount equal to the magnitude of the surface current density}@}. {@{The normal components of __H__ in the two media}@} are {@{in the ratio of the permeabilities}@}.<sup>[\[1\]](#^ref-1)</sup> <!--SR:!2025-09-12,59,318!2025-09-18,64,318!2025-09-24,69,318!2025-09-13,60,318-->

## discussion according to the media beside the interface

### if medium 1 & 2 are perfect [dielectrics](dielectrics.md)

There are {@{no charges nor surface currents at the interface}@}, and so {@{the tangential component of __H__ and the normal component of __D__ are both continuous}@}. <!--SR:!2025-09-12,59,318!2025-09-19,65,318-->

### if medium 1 is a perfect [dielectric](dielectric.md) and medium 2 is a perfect [metal](metal.md)

There are {@{charges and surface currents at the interface}@}, and so {@{the tangential component of __H__ and the normal component of __D__ are not continuous}@}.<sup>[\[1\]](#^ref-1)</sup> <!--SR:!2025-09-24,69,318!2025-09-19,65,318-->

## boundary conditions

{@{The [boundary conditions](boundary%20conditions.md)}@} must {@{not be confused with the interface conditions}@}. For {@{numerical calculations}@}, {@{the space where the calculation of the electromagnetic field is achieved}@} must {@{be restricted to some boundaries}@}. This is done by {@{assuming conditions at the boundaries}@} which are {@{physically correct and numerically solvable in finite time}@}. In some cases, the boundary conditions {@{resume to a simple interface condition}@}. The most usual and simple example is {@{a fully reflecting \(electric wall\) boundary}@} - {@{the outer medium is considered as a perfect conductor}@}. In some cases, it is more complicated: for example, {@{the reflection-less \(i.e. open\) boundaries}@} are {@{simulated as [perfectly matched layer](perfectly%20matched%20layer.md) or magnetic wall}@} that {@{do not resume to a single interface}@}. <!--SR:!2025-09-13,60,318!2025-09-12,59,318!2025-09-24,69,318!2025-09-19,65,318!2025-09-17,63,310!2025-09-18,64,318!2025-09-13,60,318!2025-09-19,65,318!2025-09-12,59,318!2025-09-13,60,318!2025-09-19,64,310!2025-09-24,69,318!2025-09-19,65,318-->

## see also

- [Maxwell's equations](Maxwell's%20equations.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/interface_conditions_for_electromagnetic_fields) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. [Kinayman & Aksun 2005](#CITEREFKinaymanAksun2005), p. 19-23. <a id="^ref-1"></a>^ref-1

<!-- markdownlint-disable-next-line MD036 -->
__Sources__

- <a id="CITEREFKinaymanAksun2005"></a> Kinayman, Noyan; [Aksun, M. I.](İrşadi%20Aksun.md) \(2005\). _Modern Microwave Circuits_. Norwood: [Artech House](Artech%20House.md). [ISBN](ISBN%20(identifier).md) [9781844073832](https://en.wikipedia.org/wiki/Special:BookSources/9781844073832).

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Electromagnetism concepts](https://en.wikipedia.org/wiki/Category:Electromagnetism%20concepts)
> - [Boundary conditions](https://en.wikipedia.org/wiki/Category:Boundary%20conditions)
