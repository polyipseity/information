---
aliases:
  - Gaussian surface
  - Gaussian surfaces
tags:
  - flashcard/active/general/eng/Gaussian_surface
  - language/in/English
---

# Gaussian surface

> {@{![A cylindrical Gaussian surface is commonly used to calculate the electric charge of an infinitely long, straight, 'ideal' wire.](../../archives/Wikimedia%20Commons/Gaussian2.jpg)}@}
>
> {@{A cylindrical Gaussian surface is commonly used}@} to {@{calculate the electric charge of an infinitely long, straight, 'ideal' wire}@}.

{@{A __Gaussian surface__}@} is {@{a [closed surface](closed%20surface.md#closed%20surfaces) in three-dimensional space through which the [flux](flux.md) of a [vector field](vector%20field.md) is calculated}@}; usually {@{the [gravitational field](gravitational%20field.md), [electric field](electric%20field.md), or [magnetic field](magnetic%20field.md)}@}.<sup>[\[1\]](#^ref-1)</sup> It is {@{an arbitrary [closed surface](closed%20surface.md#closed%20surfaces) _S_ = ∂<!-- markdown separator -->_V_ \(the [boundary](boundary%20of%20a%20manifold.md#manifold%20with%20boundary) of a 3-dimensional region _V_\)}@} used {@{in conjunction with Gauss's law for the corresponding field \([Gauss's law](Gauss's%20law.md), [Gauss's law for magnetism](Gauss's%20law%20for%20magnetism.md), or [Gauss's law for gravity](Gauss's%20law%20for%20gravity.md)\)}@} by {@{performing a [surface integral](surface%20integral.md), in order to calculate the total amount of the source quantity enclosed}@}; e.g., {@{amount of [gravitational mass](gravitational%20mass.md#inertial%20vs.%20gravitational%20mass) as the source of the gravitational field}@} or {@{amount of [electric charge](electric%20charge.md) as the source of the electrostatic field}@}, or {@{vice versa: calculate the fields for the source distribution}@}.

For {@{concreteness}@}, {@{the electric field is considered in this article}@}, as {@{this is the most frequent type of field the surface concept is used for}@}.

Gaussian surfaces are usually {@{carefully chosen to exploit [symmetries](symmetry.md) of a situation to simplify the calculation of the [surface integral](surface%20integral.md)}@}. If {@{the Gaussian surface is chosen such that for every point on the surface the component of the electric field along the [normal vector](normal%20vector.md) is constant}@}, then {@{the calculation will not require difficult integration as the constants which arise can be taken out of the integral}@}. It is defined as {@{the closed surface in three dimensional space by which the flux of vector field be calculated}@}.

## common Gaussian surfaces

- See also: ::@:: [Charge density](charge%20density.md)

> {@{![Examples of valid \(left\) and invalid \(right\) Gaussian surfaces.](../../archives/Wikimedia%20Commons/SurfacesWithAndWithoutBoundary.svg)}@}
>
> Examples of {@{valid \(left\) and invalid \(right\) Gaussian surfaces}@}. __Left:__ {@{Some valid Gaussian surfaces}@} include {@{the surface of a sphere, surface of a torus, and surface of a cube}@}. They are {@{[closed surfaces](closed%20surface.md#closed%20surfaces) that fully enclose a 3D volume}@}. __Right:__ Some surfaces that {@{__CANNOT__ be used as Gaussian surfaces}@}, such as {@{the [disk surface](disk%20(mathematics).md), square surface, or hemisphere surface}@}. They {@{do not fully enclose a 3D volume, and have boundaries \(red\)}@}. Note that {@{infinite planes can approximate Gaussian surfaces}@}.

{@{Most calculations using Gaussian surfaces}@} begin by {@{implementing [Gauss's law](Gauss's%20law.md) \(for electricity\)}@}:<sup>[\[2\]](#^ref-2)</sup> {@{$$\Phi _{E} = \oiint_S \mathbf {E} \;\cdot \mathrm {d} \mathbf {A} ={\frac {Q_{\text{enc} } }{\varepsilon _{0} } } \,.$$}@} Thereby {@{_Q_<sub>enc</sub> is the electrical charge enclosed by the Gaussian surface}@}.

This is {@{Gauss's law}@}, combining {@{both the [divergence theorem](divergence%20theorem.md) and [Coulomb's law](Coulomb's%20law.md)}@}.

### spherical surface

{@{A [spherical](sphere.md) Gaussian surface is used}@} when {@{finding the electric field or the flux produced by any of the following}@}:<sup>[\[3\]](#^ref-3)</sup> (annotation: essentially, {@{charge distributions with spherical symmetry, e.g. point charges, spherical shells, spheres, etc.}@})

- a [point charge](point%20charge.md#point%20charge)
- a uniformly distributed [spherical shell](spherical%20shell.md) of charge
- any other charge distribution with [spherical symmetry](circular%20symmetry.md)

{@{The spherical Gaussian surface is chosen}@} so that {@{it is concentric with the charge distribution}@}.

As an example, consider {@{a charged spherical shell _S_ of negligible thickness, with a uniformly distributed charge _Q_ and radius _R_}@}. We can {@{use Gauss's law}@} to {@{find the magnitude of the resultant electric field _E_ at a distance _r_ from the center of the charged shell}@}. It is immediately apparent that {@{for a spherical Gaussian surface of radius _r_ \< _R_ the enclosed charge is zero}@}: hence {@{the net flux is zero and the magnitude of the electric field on the Gaussian surface is also 0}@} \(by letting {@{_Q_<sub>_A_</sub> = 0 in Gauss's law, where _Q_<sub>_A_</sub> is the charge enclosed by the Gaussian surface}@}\).

With the same example, using {@{a larger Gaussian surface outside the shell where _r_ \> _R_}@}, Gauss's law will {@{produce a non-zero electric field}@}. This is determined as follows.

{@{The flux out of the spherical surface _S_}@} is: {@{$$\Phi _{E} = \oiint_{\partial S} \mathbf {E} \cdot d\mathbf {A} =\iint _{c}EdA\cos 0^{\circ }=E\iint _{S}dA$$}@}

{@{The [surface area of the sphere](surface%20area.md#common%20formulas) of radius _r_}@} is {@{$$\iint _{S}dA=4\pi r^{2}$$ which implies $$\Phi _{E}=E4\pi r^{2}$$}@}

By {@{Gauss's law}@} {@{the flux is also $$\Phi _{E}={\frac {Q_{A} }{\varepsilon _{0} } }$$}@} finally {@{equating the expression for Φ<sub>_E_</sub> gives the magnitude of the __E__-field at position _r_}@}: {@{$$E4\pi r^{2}={\frac {Q_{A} }{\varepsilon _{0} } }\quad \Rightarrow \quad E={\frac {Q_{A} }{4\pi \varepsilon _{0}r^{2} } }.$$}@}

{@{This non-trivial result}@} shows that {@{any spherical distribution of charge _acts as a point charge_ when observed from the outside of the charge distribution}@}; this is in fact {@{a verification of [Coulomb's law](Coulomb's%20law.md)}@}. And, as mentioned, {@{any exterior charges do not count}@}.

### cylindrical surface

{@{A [cylindrical](cylinder%20(geometry).md) Gaussian surface is used}@} when {@{finding the electric field or the flux produced by any of the following}@}:<sup>[\[3\]](#^ref-3)</sup> (annotation: 3 items: {@{infinitely long cylinder, infinitely long line, infinite plane}@})

- an infinitely long [line](line%20(geometry).md) of uniform charge
- an infinite [plane](plane%20(geometry).md) of uniform charge
- an infinitely long [cylinder](cylinder%20(geometry).md) of uniform charge

As example "field near infinite line charge" is given below;

Consider {@{a point _P_ at a distance _r_ from an infinite line charge having [charge density](charge%20density.md) \(charge per unit length\) λ}@}. Imagine {@{a closed surface in the form of cylinder whose axis of rotation is the line charge}@}. If {@{_h_ is the length of the cylinder}@}, then {@{the charge enclosed in the cylinder is $$q=\lambda h,$$}@} where {@{_q_ is the charge enclosed in the Gaussian surface}@}. There are {@{three surfaces _a_, _b_ and _c_ as shown in the figure}@}. {@{The [differential](differential%20of%20a%20function.md) [vector area](vector%20area.md)}@} is {@{_d_<!-- markdown separator -->__A__, on each surface _a_, _b_ and _c_}@}.

> {@{![Closed surface in the form of a cylinder having line charge in the center and showing differential areas _d_<!-- markdown separator -->__A__ of all three surfaces.](../../archives/Wikimedia%20Commons/Gaussian%20surface.jpg)}@}
>
> Closed surface in {@{the form of a cylinder having line charge in the center}@} and showing {@{differential areas _d_<!-- markdown separator -->__A__ of all three surfaces}@}.

{@{The flux passing}@} consists of {@{the three contributions}@}: {@{$$\Phi _{E} = \oiint_A \mathbf {E} \cdot d\mathbf {A} =\iint _{a}\mathbf {E} \cdot d\mathbf {A} +\iint_{b}\mathbf {E} \cdot d\mathbf {A} +\iint _{c}\mathbf {E} \cdot d\mathbf {A}$}@}

For {@{surfaces a and b}@}, {@{__E__ and _d_<!-- markdown separator -->__A__will be [perpendicular](perpendicular.md)}@}. For {@{surface c}@}, {@{__E__ and _d_<!-- markdown separator -->__A__ will be [parallel](parallel%20(geometry).md)}@}, as shown in the figure.
 {@{$${\begin{aligned}\Phi _{E}&=\iint _{a}EdA\cos 90^{\circ }+\iint _{b}EdA\cos 90^{\circ }+\iint _{c}EdA\cos 0^{\circ }\\&=E\iint _{c}dA\end{aligned} }$$}@}

{@{The [surface area of the cylinder](surface%20area.md#common%20formulas)}@} is {@{$$\iint _{c}dA=2\pi rh$$which implies $$\Phi _{E}=E2\pi rh.$$}@}

By {@{Gauss's law}@} {@{$$\Phi _{E}={\frac {q}{\varepsilon _{0} } }$$}@} {@{equating for Φ<sub>_E_</sub>}@} yields {@{$$E2\pi rh={\frac {\lambda h}{\varepsilon _{0} } }\quad \Rightarrow \quad E={\frac {\lambda }{2\pi \varepsilon _{0}r} }$$}@}

### Gaussian pillbox

This surface is most often used to {@{determine the electric field due to an infinite sheet of charge with uniform charge density, or a slab of charge with some finite thickness}@}. The pillbox has {@{a cylindrical shape}@}, and can be thought of as {@{consisting of three components}@}: {@{the [disk](disk%20(mathematics).md) at one end of the cylinder with area _πR_<sup>2</sup>, the disk at the other end with equal area, and the side of the cylinder}@}. {@{The sum of the [electric flux](electric%20flux.md) through each component of the surface}@} is {@{proportional to the enclosed charge of the pillbox}@}, as {@{dictated by Gauss's Law}@}. Because {@{the field close to the sheet can be approximated as constant}@}, {@{the pillbox is oriented in a way}@} so that {@{the field lines penetrate the disks at the ends of the field at a perpendicular angle and the side of the cylinder are parallel to the field lines}@}.

## see also

- [Area](area.md)
- [Surface area](surface%20area.md)
- [Vector calculus](vector%20calculus.md)
- [Integration](integration%20(calculus).md)
- [Divergence theorem](divergence%20theorem.md)
- [Faraday cage](Faraday%20cage.md)
- [Field theory](classical%20field%20theory.md)
- [Field line](field%20line.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Gaussian_surface) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. Essential Principles of Physics, P.M. Whelan, M.J. Hodgeson, 2nd Edition, 1978, John Murray, [ISBN](ISBN%20(identifier).md) [0-7195-3382-1](https://en.wikipedia.org/wiki/Special:BookSources/0-7195-3382-1) <a id="^ref-1"></a>^ref-1
2. Introduction to electrodynamics \(4th Edition\), D. J. Griffiths, 2012, [ISBN](ISBN%20(identifier).md) [978-0-321-85656-2](https://en.wikipedia.org/wiki/Special:BookSources/978-0-321-85656-2) <a id="^ref-2"></a>^ref-2
3. Physics for Scientists and Engineers - with Modern Physics \(6th Edition\), P. A. Tipler, G. Mosca, Freeman, 2008, [ISBN](ISBN%20(identifier).md) [0-7167-8964-7](https://en.wikipedia.org/wiki/Special:BookSources/0-7167-8964-7) <a id="^ref-3"></a>^ref-3

- <a id="CITEREFPurcell, Edward M.1985"></a> Purcell, Edward M. \(1985\). _Electricity and Magnetism_. McGraw-Hill. [ISBN](ISBN%20(identifier).md) [0-07-004908-4](https://en.wikipedia.org/wiki/Special:BookSources/0-07-004908-4).
- <a id="CITEREFJackson, John D.1998"></a> Jackson, John D. \(1998\). _Classical Electrodynamics \(3rd ed.\)_. Wiley. [ISBN](ISBN%20(identifier).md) [0-471-30932-X](https://en.wikipedia.org/wiki/Special:BookSources/0-471-30932-X).

## further reading

- _Electromagnetism \(2nd Edition\)_, I.S. Grant, W.R. Phillips, Manchester Physics, John Wiley & Sons, 2008, [ISBN](ISBN%20(identifier).md) [978-0-471-92712-9](https://en.wikipedia.org/wiki/Special:BookSources/978-0-471-92712-9)

## external links

- [Fields](http://www.lightandmatter.com/html_books/0sn/ch10/ch10.html) [Archived](https://web.archive.org/web/20100527194640/http://www.lightandmatter.com/html_books/0sn/ch10/ch10.html) 2010-05-27 at the [Wayback Machine](Wayback%20Machine.md) - a chapter from an online textbook

| <!-- hide <p> - [v](https://en.wikipedia.org/wiki/Template:Carl%20Friedrich%20Gauss) <br/> - [t](https://en.wikipedia.org/wiki/Template%20talk:Carl%20Friedrich%20Gauss) <br/> - [e](https://en.wikipedia.org/wiki/Special:EditPage/Template%3ACarl%20Friedrich%20Gauss) <p>  <p>  <br/> --> [Carl Friedrich Gauss](Carl%20Friedrich%20Gauss.md)                                                                                                                                                                                                                                                                                      |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| - [Gauss composition law](Gauss%20composition%20law.md) <br/> - [Gauss map](Gauss%20map.md) <br/> - [Gauss notation](Gauss%20notation.md) <br/> - [Gauss's method](Gauss's%20method.md) <br/> - [Gaussian brackets](Gaussian%20brackets.md) <br/> - [Gaussian curvature](gaussian%20curvature.md) <br/> - [Gaussian period](gaussian%20period.md) <br/> - [Gaussian surface](Gaussian%20surface.md) <br/> - [Gaussian units](Gaussian%20units.md) <br/> - [Gauss's law for gravity](Gauss's%20law%20for%20gravity.md) <br/> - [Gauss's law](Gauss's%20law.md) <br/> - [Gauss's law for magnetism](Gauss's%20law%20for%20magnetism.md) |
| - ![category icon](../../archives/Wikimedia%20Commons/Symbol%20category%20class.svg) <p>  __[Category](https://en.wikipedia.org/wiki/Category:Carl%20Friedrich%20Gauss)__                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Surfaces](https://en.wikipedia.org/wiki/Category:Surfaces)
> - [Electrostatics](https://en.wikipedia.org/wiki/Category:Electrostatics)
> - [Carl Friedrich Gauss](https://en.wikipedia.org/wiki/Category:Carl%20Friedrich%20Gauss)
