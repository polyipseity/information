---
aliases:
  - Fresnel coefficient
  - Fresnel coefficients
  - Fresnel equation
  - Fresnel equations
tags:
  - flashcard/active/general/eng/Fresnel_equations
  - language/in/English
---

# Fresnel equations

- This article is about {@{the Fresnel equations describing reflection and refraction of light at uniform planar interfaces}@}. For {@{the diffraction of light through an aperture}@}, see {@{[Fresnel diffraction](Fresnel%20diffraction.md)}@}. For {@{the thin lens and mirror technology}@}, see {@{[Fresnel lens](Fresnel%20lens.md)}@}.

> {@{![Partial transmission and reflection of a pulse travelling from a low to a high refractive index medium.](../../archives/Wikimedia%20Commons/Partial%20transmittance.gif)}@}
>
> {@{Partial transmission and reflection}@} of {@{a pulse travelling from a low to a high refractive index medium}@}.

<!-- markdownlint MD028 -->

> {@{![Hospital corridor... where my mother is now.](../../archives/Wikimedia%20Commons/Hospital%20corridor%202.jpg)}@}
>
> {@{![Sea and Sun](../../archives/Wikimedia%20Commons/Sea%20and%20Sun%20%28cropped%29%202.jpg)}@}
>
> At {@{[near-grazing](angle%20of%20incidence%20(optics).md#grazing%20angle) incidence}@}, media interfaces {@{appear mirror-like especially}@} due to {@{reflection of the _s_ polarization}@}, despite {@{being poor reflectors at normal incidence}@}. {@{[Polarized sunglasses](polarized%20sunglasses.md#polarized%20sunglasses)}@} {@{block the _s_ polarization}@}, greatly {@{reducing glare from horizontal surfaces}@}.

The {@{__Fresnel equations__ \(or __Fresnel coefficients__\)}@} describe {@{the reflection and transmission of [light](light.md) \(or [electromagnetic radiation](electromagnetic%20radiation.md) in general\) when incident on an interface between different optical [media](medium%20(optics).md)}@}. They were deduced by {@{French engineer and [physicist](physicist.md) [Augustin-Jean Fresnel](Augustin-Jean%20Fresnel.md)}@} \({@{[/freɪˈnɛl/](https://en.wikipedia.org/wiki/Help:IPA/English)}@}\) who was {@{the first to understand that light is a [transverse wave](transverse%20wave.md)}@}, when no one {@{realized that the waves were electric and magnetic fields}@}. For the first time, {@{[polarization](polarization%20(waves).md) could be understood quantitatively}@}, as Fresnel's equations {@{correctly predicted the differing behaviour of waves of the _s_ and _p_ polarizations incident upon a material interface}@}.

## overview

When {@{light strikes the interface between a medium with [refractive index](refractive%20index.md) _n_<sub>1</sub> and a second medium with refractive index _n_<sub>2</sub>}@}, both {@{[reflection](reflection%20(physics).md) and [refraction](refraction.md) of the light}@} may occur. The Fresnel equations give {@{the ratio of the _reflected_ wave's electric field to the incident wave's electric field}@}, and {@{the ratio of the _transmitted_ wave's electric field to the incident wave's electric field}@}, for {@{each of two components of polarization}@}. \({@{The _magnetic_ fields}@} can also be {@{related using similar coefficients}@}.\) These ratios are {@{generally complex}@}, describing {@{not only the relative amplitudes but also the [phase shifts](reflection%20phase%20change.md) at the interface}@}.

The equations assume {@{the interface between the media is flat and that the media are homogeneous and [isotropic](isotropy.md)}@}.<sup>[\[1\]](#^ref-1)</sup> The incident light is assumed {@{to be a [plane wave](plane%20wave.md)}@}, which is {@{sufficient to solve any problem}@} since {@{any incident light field can be decomposed into plane waves and polarizations}@}.

### S and P polarizations

- Main article: ::@:: [Plane of incidence](plane%20of%20incidence.md)

> {@{![The plane of incidence is defined by the incoming radiation's propagation vector and the normal vector of the surface.](../../archives/Wikimedia%20Commons/Plane%20of%20incidence.svg)}@}
>
> {@{The plane of incidence}@} is defined by {@{the incoming radiation's propagation vector and the normal vector of the surface}@}.

There are {@{two sets of Fresnel coefficients}@} for {@{two different linear [polarization](polarization%20(waves).md) components of the incident wave}@}. Since {@{any [polarization state](polarization%20(waves).md#polarization%20state) can be resolved into a combination of two orthogonal linear polarizations}@}, this is {@{sufficient for any problem}@}. Likewise, {@{[unpolarized](polarization%20(waves).md#unpolarized%20and%20partially%20polarized%20light) \(or "randomly polarized"\) light}@} has {@{an equal amount of power in each of two linear polarizations}@}.

{@{The s polarization}@} refers to {@{polarization of a wave's electric field _[normal](normal%20vector.md)_ to the [plane of incidence](plane%20of%20incidence.md)}@} \(the _z_ direction in the derivation below\); then {@{the magnetic field is _in_ the plane of incidence}@}. The p polarization refers to {@{polarization of the electric field _in_ the plane of incidence}@} \(the _xy_ plane in the derivation below\); then {@{the magnetic field is _normal_ to the plane of incidence}@}. The {@{names "s" and "p" for the polarization components}@} refer to {@{German "senkrecht" \(perpendicular or normal\) and "parallel" \(parallel to the plane of incidence\)}@}.

Although {@{the reflection and transmission are dependent on polarization}@}, at {@{normal incidence \(_θ_ = 0\)}@} there is {@{no distinction between them}@} so {@{all polarization states are governed by a single set of Fresnel coefficients}@} \(and {@{another special case is mentioned [below](#equal%20refractive%20indices) in which that is true}@}\).

## configuration

> {@{![Variables used in the Fresnel equations](../../archives/Wikimedia%20Commons/Fresnel1.svg)}@}
>
> {@{Variables used in the Fresnel equations}@}

In {@{the diagram on the right}@}, {@{an incident [plane wave](plane%20wave.md) in the direction of the ray __IO__}@} {@{strikes the interface between two media of refractive indices _n_<sub>1</sub> and _n_<sub>2</sub> at point __O__}@}. Part of the wave is {@{reflected in the direction __OR__}@}, and part {@{refracted in the direction __OT__}@}. The angles that {@{the incident, reflected and refracted rays make to the [normal](surface%20normal.md) of the interface}@} are given as {@{_θ_<sub>i</sub>, _θ_<sub>r</sub> and _θ_<sub>t</sub>, respectively}@}. The relationship between these angles is given by {@{the [law of reflection](law%20of%20reflection.md): $$\theta _{\mathrm {i} }=\theta _{\mathrm {r} },$$}@} and {@{[Snell's law](Snell's%20law.md): $$n_{1}\sin \theta _{\mathrm {i} }=n_{2}\sin \theta _{\mathrm {t} }.$$}@}

{@{The behavior of light striking the interface}@} is explained by considering {@{the electric and magnetic fields that constitute an [electromagnetic wave](electromagnetic%20wave.md), and the laws of [electromagnetism](Maxwell's%20equations.md)}@}, as shown [below](#theory). {@{The ratio of waves' electric field \(or magnetic field\) amplitudes}@} are obtained, but in practice one is more often {@{interested in formulae which determine _power_ coefficients}@}, since {@{power \(or [irradiance](irradiance.md)\) is what can be directly measured at optical frequencies}@}. {@{The power of a wave}@} is generally {@{proportional to the square of the electric \(or magnetic\) field amplitude}@}.

## power \(intensity\) reflection and transmission coefficients

> {@{![Power coefficients: air to glass](../../archives/Wikimedia%20Commons/Fresnel%20power%20air-to-glass.svg)}@}
>
> {@{Power coefficients: air to glass}@}

<!-- markdownlint MD028 -->

> {@{![Power coefficients: glass to air](../../archives/Wikimedia%20Commons/Fresnel%20power%20glass-to-air.svg)}@}
>
> {@{Power coefficients: glass to air}@} \({@{Total internal reflection starts from 42°}@} making {@{reflection coefficient 1}@}\)

We call {@{the fraction of the incident [power](power%20(physics).md) that is reflected from the interface}@} {@{the _[reflectance](reflectance.md)_ \(or __reflectivity__, or __power reflection coefficient__\) _R_}@}, and {@{the fraction that is refracted into the second medium}@} is called {@{the _[transmittance](transmittance.md)_ \(or __transmissivity__, or __power transmission coefficient__\) _T_}@}. Note that these are {@{what would be measured right _at_ each side of an interface}@} and do not {@{account for attenuation of a wave in an absorbing medium _following_ transmission or reflection}@}.<sup>[\[2\]](#^ref-2)</sup>

{@{The reflectance for [s-polarized light](s-polarized%20light.md#s%20and%20p)}@} is {@{$$R_{\mathrm {s} }=\left|{\frac {Z_{2}\cos \theta _{\mathrm {i} }-Z_{1}\cos \theta _{\mathrm {t} } }{Z_{2}\cos \theta _{\mathrm {i} }+Z_{1}\cos \theta _{\mathrm {t} } } }\right|^{2},$$ \(annotation: If you use wave admittance $Y = 1 / Z = \sqrt{\epsilon / \mu}$, $Z_1$ becomes $Y_2$ and $Z_2$ becomes $Y_1$.\)}@} while {@{the reflectance for [p-polarized light](p-polarized%20light.md#s%20and%20p)}@} is {@{$$R_{\mathrm {p} }=\left|{\frac {Z_{2}\cos \theta _{\mathrm {t} }-Z_{1}\cos \theta _{\mathrm {i} } }{Z_{2}\cos \theta _{\mathrm {t} }+Z_{1}\cos \theta _{\mathrm {i} } } }\right|^{2},$$}@} where {@{_Z_<sub>1</sub> and _Z_<sub>2</sub> are the [wave impedances](wave%20impedance.md) of media 1 and 2, respectively}@}.

We assume that {@{the media are non-magnetic \(i.e., _μ_<sub>1</sub> = _μ_<sub>2</sub> = [_μ_<sub>0</sub>](permeability%20of%20free%20space.md)\)}@}, which is typically {@{a good approximation at optical frequencies \(and for transparent media at other frequencies\)}@}.<sup>[\[3\]](#^ref-3)</sup> Then {@{the wave impedances}@} are {@{determined solely by the refractive indices _n_<sub>1</sub> and _n_<sub>2</sub>: $$Z_{i}={\frac {Z_{0} }{n_{i} } }\,,$$}@} where {@{_Z_<sub>0</sub> is the [impedance of free space](impedance%20of%20free%20space.md) and _i_ = 1, 2}@}. Making this substitution, we obtain {@{equations using the refractive indices}@}: {@{$$R_{\mathrm {s} }=\left|{\frac {n_{1}\cos \theta _{\mathrm {i} }-n_{2}\cos \theta _{\mathrm {t} } }{n_{1}\cos \theta _{\mathrm {i} }+n_{2}\cos \theta _{\mathrm {t} } } }\right|^{2}=\left|{\frac {n_{1}\cos \theta _{\mathrm {i} }-n_{2}{\sqrt {1-\left({\frac {n_{1} }{n_{2} } }\sin \theta _{\mathrm {i} }\right)^{2} } } }{n_{1}\cos \theta _{\mathrm {i} }+n_{2}{\sqrt {1-\left({\frac {n_{1} }{n_{2} } }\sin \theta _{\mathrm {i} }\right)^{2} } } } }\right|^{2}\!,$$ $$R_{\mathrm {p} }=\left|{\frac {n_{1}\cos \theta _{\mathrm {t} }-n_{2}\cos \theta _{\mathrm {i} } }{n_{1}\cos \theta _{\mathrm {t} }+n_{2}\cos \theta _{\mathrm {i} } } }\right|^{2}=\left|{\frac {n_{1}{\sqrt {1-\left({\frac {n_{1} }{n_{2} } }\sin \theta _{\mathrm {i} }\right)^{2} } }-n_{2}\cos \theta _{\mathrm {i} } }{n_{1}{\sqrt {1-\left({\frac {n_{1} }{n_{2} } }\sin \theta _{\mathrm {i} }\right)^{2} } }+n_{2}\cos \theta _{\mathrm {i} } } }\right|^{2}\!.$$}@}

{@{The second form of each equation}@} is {@{derived from the first}@} by {@{eliminating _θ_<sub>t</sub> using [Snell's law](Snell's%20law.md) and [trigonometric identities](trigonometric%20identity.md)}@}.

As a consequence of {@{[conservation of energy](conservation%20of%20energy.md)}@}, one can find {@{the transmitted power \(or more correctly, [irradiance](irradiance.md): power per unit area\)}@} simply as {@{the portion of the incident power that isn't reflected}@}:&hairsp;<sup>[\[4\]](#^ref-4)</sup> {@{$$T_{\mathrm {s} }=1-R_{\mathrm {s} }$$ and $$T_{\mathrm {p} }=1-R_{\mathrm {p} }$$}@}

Note that all such intensities are {@{measured in terms of a wave's irradiance in the direction normal to the interface}@}; this is also {@{what is measured in typical experiments}@}. That number could be obtained from {@{irradiances _in the direction of an incident or reflected wave_ \(given by the magnitude of a wave's [Poynting vector](Poynting%20vector.md)\)}@} multiplied by {@{cos <!-- markdown separator -->_θ_ for a wave at an angle _θ_ to the normal direction}@} \(or equivalently, taking the {@{[dot product](dot%20product.md) of the Poynting vector with the unit vector normal to the interface}@}\). This complication can be {@{ignored in the case of the reflection coefficient}@}, since {@{cos <!-- markdown separator -->_θ_<sub>i</sub> = cos <!-- markdown separator -->_θ_<sub>r</sub>}@}, so that {@{the ratio of reflected to incident irradiance in the wave's direction is the same as in the direction normal to the interface}@}. \(annotation: In the case of {@{the transmission coefficient}@}, it seems like {@{by reconsidering the cosine geometric factors, the ratio can change so that $T + R \ne 1$}@}, seemingly {@{violating conservation of energy}@}. This is resolved once you use {@{the correct interpretation of irradiance instead of transmitted power}@}, and further realize that we have been assuming {@{electromagnetic waves are idealized rays with zero "thickness" \(area\) when in reality, they have finite "thickness" \(area\)}@}. Then, energy is still conserved once you consider that {@{this "thickness" \(area\) changes proportionally after transmission}@}.\)

Although these relationships {@{describe the basic physics}@}, in many practical applications one is concerned with {@{"natural light" that can be described as unpolarized}@}. That means that there is {@{an equal amount of power in the _s_ and _p_ polarizations}@}, so that {@{the _effective_ reflectivity of the material is just the average of the two reflectivities}@}: {@{$$R_{\mathrm {eff} }={\frac {1}{2} }\left(R_{\mathrm {s} }+R_{\mathrm {p} }\right).$$}@}

For {@{low-precision applications involving unpolarized light}@}, such as {@{[computer graphics](computer%20graphics.md)}@}, rather than {@{rigorously computing the effective reflection coefficient for each angle}@}, {@{[Schlick's approximation](Schlick's%20approximation.md)}@} is often used.

### special cases

#### normal incidence

For the case of {@{[normal incidence](normal%20incidence.md)}@}, {@{_θ_<sub>i</sub> = _θ_<sub>t</sub> = 0}@}, and there is {@{no distinction between s and p polarization}@}. Thus, the reflectance simplifies to {@{$$R_{0}=\left|{\frac {n_{1}-n_{2} }{n_{1}+n_{2} } }\right|^{2}\,.$$}@}

For {@{common glass \(_n_<sub>2</sub> ≈ 1.5\) surrounded by air \(_n_<sub>1</sub> = 1\)}@}, the power reflectance at normal incidence can be seen to be {@{about 4%, or 8% accounting for both sides of a glass pane}@}.

#### Brewster's angle

- Main article: ::@:: [Brewster's angle](Brewster's%20angle.md)

At {@{a dielectric interface from _n_<sub>1</sub> to _n_<sub>2</sub>}@}, there is {@{a particular angle of incidence at which _R_<sub>p</sub> goes to zero and a p-polarised incident wave is purely refracted}@}, thus {@{all reflected light is s-polarised}@}. This angle is known as {@{[Brewster's angle](Brewster's%20angle.md)}@}, and is {@{around 56° for _n_<sub>1</sub> = 1 and _n_<sub>2</sub> = 1.5}@} \(typical glass\).

#### total internal reflection

- Main article: ::@:: [Total internal reflection](total%20internal%20reflection.md)

When {@{light travelling in a denser medium strikes the surface of a less dense medium \(i.e., _n_<sub>1</sub> \> _n_<sub>2</sub>\)}@}, beyond {@{a particular incidence angle known as the _critical angle_}@}, {@{all light is reflected and _R_<sub>s</sub> = _R_<sub>p</sub> = 1}@}. This phenomenon, known as {@{[total internal reflection](total%20internal%20reflection.md)}@}, occurs at {@{incidence angles for which Snell's law predicts that the sine of the angle of refraction would exceed unity}@} \(whereas in fact {@{sin <!-- markdown separator -->_θ_ ≤ 1 for all real _θ_}@}\). For {@{glass with _n_ = 1.5 surrounded by air}@}, the critical angle is {@{approximately 42°}@}.

#### 45° incidence

{@{Reflection at 45° incidence}@} is very commonly used for {@{making 90° turns}@}. For {@{the case of light traversing from a less dense medium into a denser one at 45° incidence \(_θ_ = 45°\)}@}, it follows {@{algebraically from the above equations}@} that {@{_R_<sub>p</sub> equals the square of _R_<sub>s</sub>: $$R_{\text{p} }=R_{\text{s} }^{2}$$}@}

This can be used to {@{either verify the consistency of the measurements of _R_<sub>s</sub> and _R_<sub>p</sub>}@}, or to {@{derive one of them when the other is known}@}. This relationship is only valid for {@{the simple case of a single plane interface between two homogeneous materials}@}, not for {@{films on substrates, where a more complex analysis is required}@}.

{@{Measurements of _R_<sub>s</sub> and _R_<sub>p</sub> at 45°}@} can be used to {@{estimate the reflectivity at normal incidence}@}.<sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup> {@{The "average of averages" obtained}@} by calculating {@{first the arithmetic as well as the geometric average of _R_<sub>s</sub> and _R_<sub>p</sub>, and then averaging these two averages again arithmetically}@}, gives a value for {@{_R_<sub>0</sub> with an error of less than about 3% for most common optical materials}@}.<sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup> This is useful because {@{measurements at normal incidence can be difficult to achieve in an experimental setup}@} since {@{the incoming beam and the detector will obstruct each other}@}. However, since {@{the dependence of _R_<sub>s</sub> and _R_<sub>p</sub> on the angle of incidence for angles below 10° is very small}@}, {@{a measurement at about 5° will usually be a good approximation for normal incidence}@}, while allowing for {@{a separation of the incoming and reflected beam}@}.

## complex amplitude reflection and transmission coefficients

{@{The above equations relating powers}@} \(which could be measured with {@{a [photometer](photometer.md)}@} for instance\) are derived from {@{the Fresnel equations}@} which solve the physical problem in terms of {@{[electromagnetic field](electromagnetic%20field.md) [complex amplitudes](complex%20amplitude.md)}@}, i.e., considering {@{[phase](phase%20(waves).md) shifts in addition to their [amplitudes](absolute%20value.md#complex%20numbers)}@}. Those underlying equations supply {@{generally [complex-valued](complex-valued.md) ratios of those EM fields}@} and may {@{take several different forms, depending on the formalism used}@}. {@{The complex amplitude coefficients for reflection and transmission}@} are usually represented by {@{lower case _r_ and _t_ \(whereas the power coefficients are capitalized\)}@}. As before, we are assuming {@{the magnetic permeability, _µ_ of both media to be equal to the permeability of free space _µ_<sub>0</sub>}@} as is essentially true of {@{all dielectrics at optical frequencies}@}.

> {@{![Amplitude coefficients: air to glass](../../archives/Wikimedia%20Commons/Fresnel%20amplitudes%20air-to-glass.svg)}@}
>
> {@{Amplitude coefficients: air to glass}@}

<!-- markdownlint MD028 -->

> {@{![Amplitude coefficients: glass to air](../../archives/Wikimedia%20Commons/Fresnel%20amplitudes%20glass-to-air.svg)}@}
>
> {@{Amplitude coefficients: glass to air}@}

In {@{the following equations and graphs}@}, we adopt {@{the following conventions}@}. For {@{_s_ polarization}@}, {@{the reflection coefficient _r_}@} is defined as {@{the ratio of the reflected wave's complex electric field amplitude to that of the incident wave}@}, whereas for {@{_p_ polarization}@} _r_ is {@{the ratio of the waves complex _magnetic_ field amplitudes}@} \(or equivalently, {@{the _negative_ of the ratio of their electric field amplitudes}@}\). {@{The transmission coefficient _t_}@} is {@{the ratio of the transmitted wave's complex electric field amplitude to that of the incident wave}@}, for {@{either polarization}@}. {@{The coefficients _r_ and _t_}@} are generally {@{different between the _s_ and _p_ polarizations}@}, and even at {@{normal incidence \(where the designations _s_ and _p_ do not even apply!\)}@} {@{the sign of _r_ is reversed depending on whether the wave is considered to be _s_ or _p_ polarized}@}, an artifact of {@{the adopted sign convention}@} \(see graph for {@{an air-glass interface at 0° incidence}@}\).

The equations consider a plane wave {@{incident on a plane interface at [angle of incidence](angle%20of%20incidence%20(optics).md) $\theta _{\mathrm {i} }$}@}, a wave {@{reflected at angle $\theta _{\mathrm {r} }=\theta _{\mathrm {i} }$}@}, and a wave {@{transmitted at angle $\theta _{\mathrm {t} }$}@}. In the case of {@{an interface into an absorbing material \(where _n_ is complex\) or total internal reflection}@}, {@{the angle of transmission does not generally evaluate to a real number}@}. In that case, however, {@{meaningful results can be obtained}@} using {@{formulations of these relationships in which trigonometric functions and geometric angles are avoided}@}; {@{the [inhomogeneous waves](inhomogeneous%20wave.md) launched into the second medium}@} cannot be {@{described using a single propagation angle}@}.

Using {@{this convention}@},<sup>[\[5\]](#^ref-5)</sup><sup>[\[6\]](#^ref-6)</sup> {@{$${\begin{aligned}r_{\text{s} }&={\frac {n_{1}\cos \theta _{\text{i} }-n_{2}\cos \theta _{\text{t} } }{n_{1}\cos \theta _{\text{i} }+n_{2}\cos \theta _{\text{t} } } },\\[3pt]t_{\text{s} }&={\frac {2n_{1}\cos \theta _{\text{i} } }{n_{1}\cos \theta _{\text{i} }+n_{2}\cos \theta _{\text{t} } } },\\[3pt]r_{\text{p} }&={\frac {n_{2}\cos \theta _{\text{i} }-n_{1}\cos \theta _{\text{t} } }{n_{2}\cos \theta _{\text{i} }+n_{1}\cos \theta _{\text{t} } } },\\[3pt]t_{\text{p} }&={\frac {2n_{1}\cos \theta _{\text{i} } }{n_{2}\cos \theta _{\text{i} }+n_{1}\cos \theta _{\text{t} } } }.\end{aligned} }$$}@}

For the case where {@{the magnetic permeabilities are non-negligible}@}, the equations change such that {@{every appearance of $n_{i}$ is replaced by $n_{i}/\mu _{i}$ \(for both $i=1,2$\)}@}.<sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup>

One can see that {@{_t_<sub>s</sub> = _r_<sub>s</sub> + 1<sup>[\[7\]](#^ref-7)</sup> and \(⁠_n_<sub>2</sub>/_n_<sub>1</sub>\)⁠_t_<sub>p</sub> = _r_<sub>p</sub> + 1}@}. One can write {@{very similar equations applying to the ratio of the waves' magnetic fields}@}, but {@{comparison of the electric fields is more conventional}@}.

Because {@{the reflected and incident waves}@} propagate {@{in the same medium and make the same angle with the normal to the surface}@}, {@{the power reflection coefficient _R_}@} is just {@{the squared magnitude of _r_:&hairsp;<sup>[\[8\]](#^ref-8)</sup> $$R=|r|^{2}.$$}@}

On the other hand, calculation of {@{the power transmission coefficient _T_ is less straightforward}@}, since {@{the light travels in different directions in the two media}@}. What's more, {@{the wave impedances in the two media differ}@}; {@{power \([irradiance](irradiance.md)\)}@} is given by {@{the square of the electric field amplitude _divided by_ the [characteristic impedance](wave%20impedance.md) of the medium}@} \(or by {@{the square of the magnetic field _multiplied by_ the characteristic impedance}@}\). This results in:<sup>[\[9\]](#^ref-9)</sup> {@{$$T={\frac {n_{2}\cos \theta _{\text{t} } }{n_{1}\cos \theta _{\text{i} } } }|t|^{2}$$}@} using {@{the above definition of _t_}@}. {@{The introduced factor of ⁠_n_<sub>2</sub>/_n_<sub>1</sub>}@}⁠ is {@{the reciprocal of the ratio of the media's wave impedances \(annotation: $n_2 / n_1 = Y_2 / Y_1 = Z_1 / Z_2$\)}@}. {@{The cos\(_θ_\) factors}@} adjust {@{the waves' powers so they are reckoned _in the direction_ normal to the interface}@}, for {@{both the incident and transmitted waves}@}, so that {@{full power transmission corresponds to _T_ = 1}@}.

In the case of {@{[total internal reflection](total%20internal%20reflection.md) where the power transmission _T_ is zero}@}, _t_ nevertheless describes {@{the electric field \(including its phase\) just beyond the interface}@}. This is {@{an [evanescent field](evanescent%20field.md)}@} which {@{does not propagate as a wave \(thus _T_ = 0\) but has nonzero values very close to the interface}@}. {@{The phase shift of the reflected wave on total internal reflection}@} can similarly be {@{obtained from the [phase angles](argument%20(complex%20analysis).md) of _r_<sub>p</sub> and _r_<sub>s</sub>}@} \(whose {@{magnitudes are unity in this case}@}\). These phase shifts are {@{different for _s_ and _p_ waves}@}, which is the well-known principle by which {@{total internal reflection is used to effect [polarization transformations](fresnel%20rhomb.md)}@}.

### alternative forms

In {@{the above formula for _r_<sub>s</sub>}@}, if we {@{put $n_{2}=n_{1}\sin \theta _{\text{i} }/\sin \theta _{\text{t} }$ \(Snell's law\)}@} and {@{multiply the numerator and denominator by \(⁠1/_n_<sub>1</sub>\)⁠ sin _θ_<sub>t</sub>}@}, we obtain&hairsp;<sup>[\[10\]](#^ref-10)</sup><sup>[\[11\]](#^ref-11)</sup> {@{$$r_{\text{s} }=-{\frac {\sin(\theta _{\text{i} }-\theta _{\text{t} })}{\sin(\theta _{\text{i} }+\theta _{\text{t} })} }.$$}@}

If we {@{do likewise with the formula for _r_<sub>p</sub>}@}, the result is easily shown to be equivalent to&hairsp;<sup>[\[12\]](#^ref-12)</sup><sup>[\[13\]](#^ref-13)</sup> {@{$$r_{\text{p} }={\frac {\tan(\theta _{\text{i} }-\theta _{\text{t} })}{\tan(\theta _{\text{i} }+\theta _{\text{t} })} }.$$}@}

{@{These formulas}@}&hairsp;<sup>[\[14\]](#^ref-14)</sup><sup>[\[15\]](#^ref-15)</sup><sup>[\[16\]](#^ref-16)</sup> are known respectively as {@{_Fresnel's sine law_ and _Fresnel's tangent law_}@}.<sup>[\[17\]](#^ref-17)</sup> Although at {@{normal incidence these expressions reduce to 0/0}@}, one can see that they {@{yield the correct results in the [limit](limit%20(mathematics).md) as _θ_<sub>i</sub> → 0}@}.

## multiple surfaces

When {@{light makes multiple reflections between two or more parallel surfaces}@}, {@{the multiple beams of light}@} generally {@{[interfere](interference%20(wave%20propagation).md) with one another}@}, resulting in {@{net transmission and reflection amplitudes that depend on the light's wavelength}@}. The interference, however, is seen only when {@{the surfaces are at distances comparable to or smaller than the light's [coherence length](coherence%20length.md)}@}, which for {@{ordinary white light is few micrometers}@}; it can be {@{much larger for light from a [laser](laser.md)}@}.

An example of {@{interference between reflections}@} is {@{the [iridescent](iridescence.md) colours seen in a [soap bubble](soap%20bubble.md) or in thin oil films on water}@}. Applications include {@{[Fabry–Pérot interferometers](Fabry–Pérot%20interferometer.md), [antireflection coatings](antireflection%20coating.md), and [optical filters](optical%20filter.md)}@}. {@{A quantitative analysis of these effects}@} is based on {@{the Fresnel equations, but with additional calculations to account for interference}@}.

{@{The [transfer-matrix method](transfer-matrix%20method%20(optics).md), or the recursive Rouard method}@}&hairsp;<sup>[\[18\]](#^ref-18)</sup> can be used to {@{solve multiple-surface problems}@}.

## history

- Further information: ::@:: [Augustin-Jean Fresnel](Augustin-Jean%20Fresnel.md)

In 1808, [Étienne-Louis Malus](Étienne-Louis%20Malus.md) discovered that when a ray of light was reflected off a non-metallic surface at the appropriate angle, it behaved like _one_ of the two rays emerging from a [doubly-refractive](birefringence.md) calcite crystal.<sup>[\[19\]](#^ref-19)</sup> He later coined the term _polarization_ to describe this behavior.  In 1815, the dependence of the polarizing angle on the refractive index was determined experimentally by [David Brewster](David%20Brewster.md).<sup>[\[20\]](#^ref-20)</sup> But the _reason_ for that dependence was such a deep mystery that in late 1817, [Thomas Young](Thomas%20Young%20(scientist).md) was moved to write:

> \[T\]he great difficulty of all, which is to assign a sufficient reason for the reflection or nonreflection of a polarised ray, will probably long remain, to mortify the vanity of an ambitious philosophy, completely unresolved by any theory.<sup>[\[21\]](#^ref-21)</sup>

In 1821, however, [Augustin-Jean Fresnel](Augustin-Jean%20Fresnel.md) derived results equivalent to his sine and tangent laws \(above\), by modeling light waves as [transverse elastic waves](S-wave.md) with vibrations perpendicular to what had previously been called the [plane of polarization](plane%20of%20polarization.md). Fresnel promptly confirmed by experiment that the equations correctly predicted the direction of polarization of the reflected beam when the incident beam was polarized at 45° to the plane of incidence, for light incident from air onto glass or water; in particular, the equations gave the correct polarization at Brewster's angle.<sup>[\[22\]](#^ref-22)</sup> The experimental confirmation was reported in a "postscript" to the work in which Fresnel first revealed his theory that light waves, including "unpolarized" waves, were _purely_ transverse.<sup>[\[23\]](#^ref-23)</sup>

Details of Fresnel's derivation, including the modern forms of the sine law and tangent law, were given later, in a memoir read to the [French Academy of Sciences](French%20Academy%20of%20Sciences.md) in January 1823.<sup>[\[24\]](#^ref-24)</sup> That derivation combined conservation of energy with continuity of the _tangential_ vibration at the interface, but failed to allow for any condition on the _normal_ component of vibration.<sup>[\[25\]](#^ref-25)</sup> The first derivation from _electromagnetic_ principles was given by [Hendrik Lorentz](Hendrik%20Lorentz.md) in 1875.<sup>[\[26\]](#^ref-26)</sup>

In the same memoir of January 1823,<sup>[\[24\]](#^ref-24)</sup> Fresnel found that for angles of incidence greater than the critical angle, his formulas for the reflection coefficients \(_r_<sub>s</sub> and _r_<sub>p</sub>\) gave complex values with unit magnitudes. Noting that the magnitude, as usual, represented the ratio of peak amplitudes, he guessed that the [argument](argument%20(complex%20analysis).md) represented the phase shift, and verified the hypothesis experimentally.<sup>[\[27\]](#^ref-27)</sup> The verification involved

- calculating the angle of incidence that would introduce a total phase difference of 90° between the s and p components, for various numbers of total internal reflections at that angle \(generally there were two solutions\),
- subjecting light to that number of total internal reflections at that angle of incidence, with an initial linear polarization at 45° to the plane of incidence, and
- checking that the final polarization was [circular](circular%20polarization.md).<sup>[\[28\]](#^ref-28)</sup>

Thus he finally had a quantitative theory for what we now call the _Fresnel rhomb_ — a device that he had been using in experiments, in one form or another, since 1817 \(see _[Fresnel rhomb § History](Fresnel%20rhomb.md#history)_\).

The success of the complex reflection coefficient inspired [James MacCullagh](James%20MacCullagh.md) and [Augustin-Louis Cauchy](Augustin-Louis%20Cauchy.md), beginning in 1836, to analyze reflection from metals by using the Fresnel equations with a [complex refractive index](refractive%20index.md#complex%20refractive%20index).<sup>[\[29\]](#^ref-29)</sup>

Four weeks before he presented his completed theory of total internal reflection and the rhomb, Fresnel submitted a memoir&hairsp;<sup>[\[30\]](#^ref-30)</sup> in which he introduced the needed terms _[linear polarization](linear%20polarization.md)_, _[circular polarization](circular%20polarization.md)_, and _[elliptical polarization](elliptical%20polarization.md)_,<sup>[\[31\]](#^ref-31)</sup> and in which he explained [optical rotation](optical%20rotation.md) as a species of [birefringence](birefringence.md): linearly-polarized light can be resolved into two circularly-polarized components rotating in opposite directions, and if these propagate at different speeds, the phase difference between them — hence the orientation of their linearly-polarized resultant — will vary continuously with distance.<sup>[\[32\]](#^ref-32)</sup>

Thus Fresnel's interpretation of the complex values of his reflection coefficients marked the confluence of several streams of his research and, arguably, the essential completion of his reconstruction of physical optics on the transverse-wave hypothesis \(see _[Augustin-Jean Fresnel](Augustin-Jean%20Fresnel.md)_\).

## derivation

Here we systematically {@{derive the above relations from electromagnetic premises}@}.

### material parameters

In order to {@{compute meaningful Fresnel coefficients}@}, we must assume that {@{the medium is \(approximately\) [linear](linearity.md) and [homogeneous](homogeneity%20(physics).md)}@}. If {@{the medium is also [isotropic](isotropy.md)}@}, {@{the four field vectors __E__, <!-- markdown separator -->__B__, <!-- markdown separator -->__D__, <!-- markdown separator -->__H__  are [related](constitutive%20equation.md#electromagnetism)}@} by {@{$${\begin{aligned}\mathbf {D} &=\epsilon \mathbf {E} \\\mathbf {B} &=\mu \mathbf {H} \,,\end{aligned} }$$}@} where {@{_ϵ_ and _μ_ are scalars, known respectively as the \(electric\) _[permittivity](permittivity.md)_ and the \(magnetic\) _[permeability](permeability%20(electromagnetism).md)_ of the medium}@}. For vacuum, these have {@{the values _ϵ_<sub>0</sub> and _μ_<sub>0</sub>, respectively}@}. Hence we define {@{the _relative_ permittivity \(or [dielectric constant](dielectric%20constant.md#terminology)\) _ϵ_<sub>rel</sub> = _ϵ_<!-- markdown separator -->/<!-- markdown separator -->_ϵ_<sub>0</sub>}@}, and {@{the _relative_ permeability _μ_<sub>rel</sub> = _μ_<!-- markdown separator -->/<!-- markdown separator -->_μ_<sub>0</sub>}@}.

In optics it is common to {@{assume that the medium is non-magnetic}@}, so that {@{_μ_<sub>rel</sub> = 1}@}. For {@{[ferromagnetic](ferromagnetic.md) materials at radio/microwave frequencies}@}, {@{larger values of _μ_<sub>rel</sub>}@} must be taken into account. But, for {@{optically transparent media, and for all other materials at optical frequencies \(except possible [metamaterials](metamaterial.md)\)}@}, _μ_<sub>rel</sub> is {@{indeed very close to 1; that is, _μ_ ≈ _μ_<sub>0</sub>}@}.

In optics, one usually knows {@{the [refractive index](refractive%20index.md) _n_ of the medium}@}, which is {@{the ratio of the speed of light in vacuum \(_c_\) to the speed of light in the medium}@}. In the analysis of {@{partial reflection and transmission}@}, one is also interested in {@{the electromagnetic [wave impedance](wave%20impedance.md) _Z_}@}, which is {@{the ratio of the amplitude of __E__ to the amplitude of __H__}@}. It is therefore desirable to {@{express _n_ and _Z_ in terms of _ϵ_ and _μ_, and thence to relate _Z_ to _n_}@}. The last-mentioned relation, however, will make it convenient to {@{derive the reflection coefficients in terms of the wave _admittance_ _Y_}@}, which is {@{the reciprocal of the wave impedance _Z_}@}.

In the case of {@{_uniform [plane](plane%20wave.md) [sinusoidal](sine%20wave.md)_ waves}@}, {@{the wave impedance or admittance}@} is known as {@{the _intrinsic_ impedance or admittance of the medium}@}. This case is the one for which {@{the Fresnel coefficients are to be derived}@}.

### electromagnetic plane waves

In {@{a uniform plane sinusoidal [electromagnetic wave](electromagnetic%20radiation.md)}@}, {@{the [electric field](electric%20field.md) __E__}@} has the form {@{$$\mathbf {E_{k} } e^{i(\mathbf {k\cdot r} -\omega t)},$$}@} __<a id="math 1">(1)</a>__ <p> where {@{__E<sub>k</sub>__ is the \(constant\) complex amplitude vector}@}, _i_ is {@{the [imaginary unit](imaginary%20unit.md)}@}, __k__ is {@{the [wave vector](wave%20vector.md) \(whose magnitude _k_ is the angular [wavenumber](wavenumber.md)\)}@}, __r__ is {@{the [position vector](position%20(vector).md)}@}, _ω_ is {@{the [angular frequency](angular%20frequency.md)}@}, _t_ is {@{time}@}, and it is understood that {@{the _real part_ of the expression is the physical field}@}.<sup>[\[Note 1\]](#^ref-note-1)</sup>  The value of the expression is unchanged if {@{the position __r__ varies in a direction normal to __k__}@}; hence {@{__k__ _is normal to the wavefronts_}@}.

To {@{advance the [phase](phase%20(waves).md) by the angle _ϕ_}@}, we {@{replace _ωt_ by _ωt_ + _ϕ_ \(that is, we replace −<!-- markdown separator -->_ωt_ by −<!-- markdown separator -->_ωt_ − _ϕ_\)}@}, with the result that {@{the \(complex\) field is multiplied by _e<sup>−iϕ</sup>_}@}. So a phase _advance_ is equivalent to {@{multiplication by a complex constant with a _negative_ [argument](argument%20(complex%20analysis).md)}@}. This becomes more obvious when {@{the field \(__[1](#math%201)__\) is factored as __E<sub>k</sub>__<!-- markdown separator -->&hairsp;<!-- markdown separator -->_e_<sup>_i_<!-- markdown separator -->__k__<!-- markdown separator -->⋅<!-- markdown separator -->__r__</sup>_e_<sup>_−iωt_</sup>}@}, where {@{the last factor contains the time-dependence}@}. That factor also implies that {@{differentiation w.r.t. time}@} corresponds to {@{multiplication by _−iω_}@}.&hairsp;<sup>[\[Note 2\]](#^ref-note-2)</sup>

If {@{_ℓ_ is the component of __r__ in the direction of __k__}@}, the field \(__[1](#math%201)__\) can be written {@{__E<sub>k</sub>__<!-- markdown separator -->&hairsp;<!-- markdown separator -->_e_<sup>_i_\(_kℓ_<!-- markdown separator -->−<!-- markdown separator -->_ωt_\)</sup>}@}.  If {@{the argument of _e_<sup>_i_\(⋯\)</sup> is to be constant \(annotation: That is, we select a point of the wave and move along with it at phase velocity.\)}@},  _ℓ_ must {@{increase at the velocity $\omega /k\,,\,$}@} known as {@{the _[phase velocity](phase%20velocity.md)_ \(_v_<sub>p</sub>\)}@}. This in turn is {@{equal to $c/n$}@}. Solving for _k_ gives {@{$$k=n\omega /c\,.$$}@} __<a id="math 2">(2)</a>__ <p>

As usual, we {@{drop the time-dependent factor _e_<sup>−<!-- markdown separator -->_iωt_</sup>}@}, which is understood to {@{multiply every complex field quantity}@}. {@{The electric field for a uniform plane sine wave}@} will then be {@{represented by the location-dependent _[phasor](phasor.md)_}@} {@{$$\mathbf {E_{k} } e^{i\mathbf {k\cdot r} }.$$}@} __<a id="math 3">(3)</a>__ <p>

For {@{fields of that form}@}, {@{[Faraday's law](Faraday's%20law%20of%20induction.md) and the [Maxwell-Ampère law](Ampère's%20circuital%20law.md)}@} respectively reduce to&hairsp;<sup>[\[33\]](#^ref-33)</sup> {@{$${\begin{aligned}\omega \mathbf {B} &=\mathbf {k} \times \mathbf {E} \\\omega \mathbf {D} &=-\mathbf {k} \times \mathbf {H} \,.\end{aligned} }$$ \(annotation: The derivation steps are the same as that for electromagnetic waves.\)}@}

Putting {@{__B__ = _μ_<!-- markdown separator -->__H__ and __D__ = _ϵ_<!-- markdown separator -->__E__}@}, as above, we can {@{eliminate __B__ and __D__ to obtain equations in only __E__ and __H__}@}: {@{$${\begin{aligned}\omega \mu \mathbf {H} &=\mathbf {k} \times \mathbf {E} \\\omega \epsilon \mathbf {E} &=-\mathbf {k} \times \mathbf {H} \,.\end{aligned} }$$}@} If {@{the material parameters _ϵ_ and _μ_ are real \(as in a lossless dielectric\)}@}, these equations show that {@{__k__, __E__, __H__ form a _right-handed orthogonal triad_}@}, so that {@{the same equations apply to the magnitudes of the respective vectors}@}. Taking {@{the magnitude equations and substituting from \(__[2](#math%202)__\)}@}, we obtain {@{$${\begin{aligned}\mu cH&=nE\\\epsilon cE&=nH\,,\end{aligned} }$$}@} where {@{_H_ and _E_ are the magnitudes of __H__ and __E__}@}. {@{Multiplying the last two equations}@} gives {@{$$n=c\,{\sqrt {\mu \epsilon } }\,.$$}@} __<a id="math 4">(4)</a>__ <p> {@{Dividing \(or cross-multiplying\) the same two equations}@} gives {@{_H_ = _YE_, where $$Y={\sqrt {\epsilon /\mu } }\,.$$}@} __<a id="math 5">(5)</a>__ <p> This is {@{the _intrinsic admittance_}@}.

From \(__[4](#math%204)__\) we obtain {@{the phase velocity $c/n=1{\big /}\!{\sqrt {\mu \epsilon \,} }$}@}. For {@{vacuum}@} this reduces to {@{$c=1{\big /}\!{\sqrt {\mu _{0}\epsilon _{0} } }$}@}. {@{Dividing the second result by the first}@} gives {@{$$n={\sqrt {\mu _{\text{rel} }\epsilon _{\text{rel} } } }\,.$$}@} For {@{a _non-magnetic_ medium \(the usual case\)}@}, this becomes {@{⁠$n={\sqrt {\epsilon _{\text{rel} } } }$}@}⁠. \(Taking {@{the reciprocal of \(__[5](#math%205)__\)}@}, we find that {@{the intrinsic _impedance_ is $Z={\sqrt {\mu /\epsilon } }$}@}. In {@{vacuum}@} this takes {@{the value $Z_{0}={\sqrt {\mu _{0}/\epsilon _{0} } }\,\approx 377\,\Omega \,$}@}, known as {@{the [impedance of free space](impedance%20of%20free%20space.md)}@}. By division, {@{$Z/Z_{0}={\sqrt {\mu _{\text{rel} }/\epsilon _{\text{rel} } } }$}@}. For {@{a _non-magnetic_ medium}@}, this becomes {@{$Z=Z_{0}{\big /}\!{\sqrt {\epsilon _{\text{rel} } } }=Z_{0}/n$}@}.\)

### wave vectors

> {@{![Incident, reflected, and transmitted wave vectors \(__k__<sub>i</sub>, __k__<sub>r</sub>, and __k__<sub>t</sub>\), for incidence from a medium with refractive index _n_<sub>1</sub> to a medium with refractive index _n_<sub>2</sub>. The red arrows are perpendicular to the wave vectors.](../../archives/Wikimedia%20Commons/Wave%20vectors%20n1%20to%20n2.svg)}@}
>
> {@{Incident, reflected, and transmitted wave vectors \(__k__<sub>i</sub>, __k__<sub>r</sub>, and __k__<sub>t</sub>\)}@}, for {@{incidence from a medium with refractive index _n_<sub>1</sub> to a medium with refractive index _n_<sub>2</sub>}@}. {@{The red arrows}@} are {@{perpendicular to the wave vectors}@}.

In {@{Cartesian coordinates \(_x_, _y_, _z_\)}@}, let {@{the region _y_ \< 0 have refractive index _n_<sub>1</sub>, intrinsic admittance _Y_<sub>1</sub>, etc.}@}, and let {@{the region _y_ \> 0 have refractive index _n_<sub>2</sub>, intrinsic admittance _Y_<sub>2</sub>, etc.}@} Then {@{the _xz_ plane is the interface}@}, and {@{the _y_ axis is normal to the interface}@} \(see diagram\). Let {@{__i__ and __j__ \(in bold [roman type](roman%20type.md)\)}@} be {@{the unit vectors in the _x_ and _y_ directions, respectively}@}. Let {@{the plane of incidence be the _xy_ plane \(the plane of the page\)}@}, with {@{the angle of incidence _θ_<sub>i</sub> measured from __j__ towards __i__}@}. Let {@{the angle of refraction, measured in the same sense}@}, be {@{_θ_<sub>t</sub>, where the subscript _t_ stands for _transmitted_ \(reserving _r_ for _reflected_\)}@}.

In {@{the absence of [Doppler shifts](Doppler%20effect.md)}@}, {@{_ω_ does not change on reflection or refraction}@}. Hence, by \(__[2](#math%202)__\), {@{the magnitude of the wave vector is proportional to the refractive index}@}.

So, for {@{a given _ω_}@}, if we {@{_redefine_ _k_ as the magnitude of the wave vector in the _reference_ medium \(for which _n_ = 1\)}@}, then the wave vector has {@{magnitude _n_<sub>1</sub>_k_ in the first medium \(region _y_ \< 0 in the diagram\) and magnitude _n_<sub>2</sub>_k_ in the second medium}@}. From {@{the magnitudes and the geometry}@}, we find that the wave vectors are {@{$${\begin{aligned}\mathbf {k} _{\text{i} }&=n_{1}k(\mathbf {i} \sin \theta _{\text{i} }+\mathbf {j} \cos \theta _{\text{i} })\\[.5ex]\mathbf {k} _{\text{r} }&=n_{1}k(\mathbf {i} \sin \theta _{\text{i} }-\mathbf {j} \cos \theta _{\text{i} })\\[.5ex]\mathbf {k} _{\text{t} }&=n_{2}k(\mathbf {i} \sin \theta _{\text{t} }+\mathbf {j} \cos \theta _{\text{t} })\\&=k(\mathbf {i} \,n_{1}\sin \theta _{\text{i} }+\mathbf {j} \,n_{2}\cos \theta _{\text{t} })\,,\end{aligned} }$$}@} where {@{the last step uses Snell's law}@}. {@{The corresponding [dot products](dot%20product.md) in the phasor form \(__[3](#math%203)__\)}@} are {@{$${\begin{aligned}\mathbf {k} _{\text{i} }\mathbf {\cdot r} &=n_{1}k(x\sin \theta _{\text{i} }+y\cos \theta _{\text{i} })\\\mathbf {k} _{\text{r} }\mathbf {\cdot r} &=n_{1}k(x\sin \theta _{\text{i} }-y\cos \theta _{\text{i} })\\\mathbf {k} _{\text{t} }\mathbf {\cdot r} &=k(n_{1}x\sin \theta _{\text{i} }+n_{2}y\cos \theta _{\text{t} })\,.\end{aligned} }$$}@} __<a id="math 6">(6)</a>__ <p>

Hence:

At {@{$y=0\,,~~~\mathbf {k} _{\text{i} }\mathbf {\cdot r} =\mathbf {k} _{\text{r} }\mathbf {\cdot r} =\mathbf {k} _{\text{t} }\mathbf {\cdot r} =n_{1}kx\sin \theta _{\text{i} }\,$}@}. __<a id="math 7">(7)</a>__ <p> \(annotation: This can be used to {@{derive the law of reflection and refraction \(Snell's law\)}@}. {@{The time-varying component of the phasors}@} can be {@{ignored, since it is understood to be the same for the waves being considered}@}. What remains is {@{the location-varying component of the phasors should equal each other by continuity}@}. So we have {@{$\mathbf k_i \cdot \mathbf r = \mathbf k_r \cdot \mathbf r = \mathbf k_t \cdot \mathbf r$}@}. Setting $y = 0$, we obtain {@{$n_1 k x \sin \theta_i = n_1 k x \sin \theta_r = n_2 k x \sin \theta_t$}@}. Then the law of reflection is {@{$\theta_i = \theta_r$}@} and the law of refraction is {@{$n_1 \sin \theta_i = n_2 \sin \theta_t$}@}.\)

### _s_ components

For {@{the _s_ polarization}@}, {@{the __E__ field is parallel to the _z_ axis}@} and may therefore be {@{described by its component in the _z_ direction}@}. Let {@{the reflection and transmission coefficients}@} be {@{_r_<sub>s</sub> and _t_<sub>s</sub>, respectively}@}. Then, if {@{the incident __E__ field is taken to have unit amplitude}@}, {@{the phasor form \(__[3](#math%203)__\) of its _z_-component}@} is {@{$$E_{\text{i} }=e^{i\mathbf {k} _{\text{i} }\mathbf {\cdot r} },$$}@} __<a id="math 8">(8)</a>__ <p>

and {@{the reflected and transmitted fields, in the same form}@}, are {@{$${\begin{aligned}E_{\text{r} }&=r_{s\,}e^{i\mathbf {k} _{\text{r} }\mathbf {\cdot r} }\\E_{\text{t} }&=t_{s\,}e^{i\mathbf {k} _{\text{t} }\mathbf {\cdot r} }.\end{aligned} }$$}@} __<a id="math 9">(9)</a>__ <p>

Under {@{the sign convention used in this article}@}, {@{a positive reflection or transmission coefficient}@} is {@{one that preserves the direction of the _transverse_ field \(annotation: This is implicitly used when we make the tangential components continuous.\), meaning \(in this context\) the field normal to the plane of incidence}@}. For {@{the _s_ polarization, that means the __E__ field}@}. If {@{the incident, reflected, and transmitted __E__ fields \(in the above equations\)}@} are {@{in the _z_-direction \("out of the page"\)}@}, then {@{the respective __H__ fields}@} are {@{in the directions of the red arrows}@}, since {@{__k__, __E__, __H__ form a right-handed orthogonal triad}@}. The __H__ fields may therefore be {@{described by their components in the directions of those arrows}@}, denoted by {@{_H_<sub>i</sub>, _H_<sub>r</sub>, _H_<sub>t</sub>}@}. Then, since {@{_H_ = _YE_}@}, {@{$${\begin{aligned}H_{\text{i} }&=\,Y_{1}e^{i\mathbf {k} _{\text{i} }\mathbf {\cdot r} }\\H_{\text{r} }&=\,Y_{1}r_{s\,}e^{i\mathbf {k} _{\text{r} }\mathbf {\cdot r} }\\H_{\text{t} }&=\,Y_{2}t_{s\,}e^{i\mathbf {k} _{\text{t} }\mathbf {\cdot r} }.\end{aligned} }$$}@} __<a id="math 10">(10)</a>__ <p>

At {@{the interface}@}, by {@{the usual [interface conditions for electromagnetic fields](interface%20conditions%20for%20electromagnetic%20fields.md)}@}, {@{the tangential components of the __E__ and __H__ fields must be continuous}@}; that is, {@{$$\left.{\begin{aligned}E_{\text{i} }+E_{\text{r} }&=E_{\text{t} }\\H_{\text{i} }\cos \theta _{\text{i} }-H_{\text{r} }\cos \theta _{\text{i} }&=H_{\text{t} }\cos \theta _{\text{t} }\end{aligned} }~~\right\}~~~{\text{at} }~~y=0\,.$$ \(annotation: Positive _H_ points to the right.\)}@} __<a id="math 11">(11)</a>__ <p>

When we {@{substitute from equations \(__[8](#math%208)__\) to \(__[10](#math%2010)__\) and then from \(__[7](#math%207)__\)}@}, {@{the exponential factors cancel out}@}, so that the interface conditions reduce to the simultaneous equations {@{$${\begin{aligned}1+r_{\text{s} }&=\,t_{\text{s} }\\Y_{1}\cos \theta _{\text{i} }-Y_{1}r_{\text{s} }\cos \theta _{\text{i} }&=\,Y_{2}t_{\text{s} }\cos \theta _{\text{t} }\,,\end{aligned} }$$}@} __<a id="math 12">(12)</a>__ <p> which are {@{easily solved for _r_<sub>s</sub> and _t_<sub>s</sub>}@}, yielding {@{$$r_{\text{s} }={\frac {Y_{1}\cos \theta _{\text{i} }-Y_{2}\cos \theta _{\text{t} } }{Y_{1}\cos \theta _{\text{i} }+Y_{2}\cos \theta _{\text{t} } } }$$}@} __<a id="math 13">(13)</a>__ <p> and {@{$$t_{\text{s} }={\frac {2Y_{1}\cos \theta _{\text{i} } }{Y_{1}\cos \theta _{\text{i} }+Y_{2}\cos \theta _{\text{t} } } }\,.$$}@} __<a id="math 14">(14)</a>__ <p>

At {@{_normal incidence_ \(_θ_<sub>i</sub> = _θ_<sub>t</sub> = 0\)}@}, indicated by {@{an additional subscript 0}@}, these results become {@{$$r_{\text{s0} }={\frac {Y_{1}-Y_{2} }{Y_{1}+Y_{2} } }$$}@} __<a id="math 15">(15)</a>__ <p> and {@{$$t_{\text{s0} }={\frac {2Y_{1} }{Y_{1}+Y_{2} } }\,.$$}@} __<a id="math 16">(16)</a>__ <p>

At {@{_grazing incidence_ \(_θ_<sub>i</sub> → 90°\)}@}, we have {@{cos _θ_<sub>i</sub> → 0}@}, hence {@{_r_<sub>s</sub> → −1 and _t_<sub>s</sub> → 0}@}.

### _p_ components

For {@{the _p_ polarization}@}, {@{the incident, reflected, and transmitted __E__ fields}@} are {@{parallel to the red arrows and may therefore be described by their components in the directions of those arrows}@}. Let those components be {@{_E_<sub>i</sub>, _E_<sub>r</sub>, _E_<sub>t</sub>}@}&hairsp; \(redefining {@{the symbols for the new context}@}\). Let {@{the reflection and transmission coefficients}@} be {@{_r_<sub>p</sub> and _t_<sub>p</sub>}@}. Then, if {@{the incident __E__ field is taken to have unit amplitude}@}, we have {@{$${\begin{aligned}E_{\text{i} }&=e^{i\mathbf {k} _{\text{i} }\mathbf {\cdot r} }\\E_{\text{r} }&=r_{p\,}e^{i\mathbf {k} _{\text{r} }\mathbf {\cdot r} }\\E_{\text{t} }&=t_{p\,}e^{i\mathbf {k} _{\text{t} }\mathbf {\cdot r} }.\end{aligned} }$$}@} __<a id="math 17">(17)</a>__ <p>

If {@{the __E__ fields are in the directions of the red arrows}@}, then, in order for {@{__k__, __E__, __H__ to form a right-handed orthogonal triad}@}, {@{the respective __H__ fields must be in the −<!-- markdown separator -->_z_-direction \("into the page"\)}@} and may therefore be {@{described by their components in that direction}@}. This is {@{consistent with the adopted sign convention}@}, namely that {@{a positive reflection or transmission coefficient is one that preserves the direction of the transverse field \(annotation: This is implicitly used when we make the tangential components continuous.\)}@} \({@{the __H__ field in the case of the _p_ polarization}@}\). The agreement of {@{the _other_ field \(annotation: the __E__ field in the case of the _p_ polarization\) with the red arrows}@} reveals {@{an alternative definition of the sign convention}@}: that {@{a positive reflection or transmission coefficient}@} is {@{one for which the field vector in the plane of incidence points towards the same medium before and after reflection or transmission}@}.<sup>[\[34\]](#^ref-34)</sup>

So, for {@{the incident, reflected, and transmitted __H__ fields}@}, let the respective components in the −<!-- markdown separator -->_z_-direction be {@{_H_<sub>i</sub>, _H_<sub>r</sub>, _H_<sub>t</sub>}@}. Then, since {@{_H_ = _YE_}@}, {@{$${\begin{aligned}H_{\text{i} }&=\,Y_{1}e^{i\mathbf {k} _{\text{i} }\mathbf {\cdot r} }\\H_{\text{r} }&=\,Y_{1}r_{p\,}e^{i\mathbf {k} _{\text{r} }\mathbf {\cdot r} }\\H_{\text{t} }&=\,Y_{2}t_{p\,}e^{i\mathbf {k} _{\text{t} }\mathbf {\cdot r} }.\end{aligned} }$$}@} __<a id="math 18">(18)</a>__ <p>

At {@{the interface}@}, {@{the tangential components of the __E__ and __H__ fields must be continuous}@}; that is, {@{$$\left.{\begin{aligned}E_{\text{i} }\cos \theta _{\text{i} }-E_{\text{r} }\cos \theta _{\text{i} }&=E_{\text{t} }\cos \theta _{\text{t} }\\H_{\text{i} }+H_{\text{r} }&=H_{\text{t} }\end{aligned} }~~\right\}~~~{\text{at} }~~y=0\,.$$ (annotation: Positive _E_ points to the right.\)}@} __<a id="math 19">(19)</a>__ <p>

When we {@{substitute from equations \(__[17](#math%2017)__\) and \(__[18](#math%2018)__\) and then from \(__[7](#math%207)__\)}@}, {@{the exponential factors again cancel out}@}, so that the interface conditions reduce to {@{$${\begin{aligned}\cos \theta _{\text{i} }-r_{\text{p} }\cos \theta _{\text{i} }&=\,t_{\text{p} }\cos \theta _{\text{t} }\\Y_{1}+Y_{1}r_{\text{p} }&=\,Y_{2}t_{\text{p} }\,.\end{aligned} }$$}@} __<a id="math 20">(20)</a>__ <p>

Solving for {@{_r_<sub>p</sub> and _t_<sub>p</sub>}@}, we find {@{$$r_{\text{p} }={\frac {Y_{2}\cos \theta _{\text{i} }-Y_{1}\cos \theta _{\text{t} } }{Y_{2}\cos \theta _{\text{i} }+Y_{1}\cos \theta _{\text{t} } } }$$}@} __<a id="math 21">(21)</a>__ <p> and {@{$$t_{\text{p} }={\frac {2Y_{1}\cos \theta _{\text{i} } }{Y_{2}\cos \theta _{\text{i} }+Y_{1}\cos \theta _{\text{t} } } }\,.$$}@} __<a id="math 22">(22)</a>__ <p>

At {@{_normal incidence_ \(_θ_<sub>i</sub> = _θ_<sub>t</sub> = 0\)}@} indicated by {@{an additional subscript 0}@}, these results become {@{$$r_{\text{p0} }={\frac {Y_{2}-Y_{1} }{Y_{2}+Y_{1} } }$$}@} __<a id="math 23">(23)</a>__ <p> and {@{$$t_{\text{p0} }={\frac {2Y_{1} }{Y_{2}+Y_{1} } }\,.$$}@} __<a id="math 24">(24)</a>__ <p>

At {@{_grazing incidence_ \(_θ_<sub>i</sub> → 90°\)}@}, we again have {@{cos _θ_<sub>i</sub> → 0}@}, hence {@{_r_<sub>p</sub> → −1 and _t_<sub>p</sub> → 0}@}.

Comparing {@{\(__[23](#math%2023)__\) and \(__[24](#math%2024)__\) with \(__[15](#math%2015)__\) and \(__[16](#math%2016)__\)}@}, we see that {@{at _normal_ incidence, under the adopted sign convention}@}, {@{the transmission coefficients for the two polarizations are equal}@}, whereas {@{the reflection coefficients have equal magnitudes but opposite signs}@}. While {@{this clash of signs is a disadvantage of the convention}@}, the attendant advantage is that {@{the signs agree at _grazing_ incidence}@}.

### power ratios \(reflectivity and transmissivity\)

{@{The _[Poynting vector](Poynting%20vector.md)_ for a wave}@} is {@{a vector whose component in any direction}@} is {@{the _[irradiance](irradiance.md)_ \(power per unit area\) of that wave on a surface perpendicular to that direction}@}. For {@{a plane sinusoidal wave}@} the Poynting vector is ⁠{@{\(1/2\)⁠Re{__E__ × __H__<sup>∗</sup>}<!-- flashcard separator -->}@}, where {@{__E__ and __H__ are due _only_ to the wave in question}@}, and {@{the asterisk denotes complex conjugation}@}. Inside {@{a lossless dielectric \(the usual case\)}@}, {@{__E__ and __H__ are in phase}@}, and {@{at right angles to each other and to the wave vector __k__}@}; so, for {@{s polarization}@}, using {@{the _z_ and _xy_ components of __E__ and __H__ respectively}@} \(or for {@{p polarization}@}, using {@{the _xy_ and −<!-- markdown separator -->_z_ components of __E__ and __H__}@}\), {@{the [irradiance](irradiance.md) in the direction of __k__}@} is given {@{simply by _EH_<!-- markdown separator -->/2}@}, which is {@{_E_<sup>2</sup>/2<!-- markdown separator -->_Z_}@} in {@{a medium of intrinsic impedance _Z_<!-- markdown separator --> = 1/<!-- markdown separator -->_Y_}@}. To compute {@{the irradiance in the direction normal to the interface}@}, as we shall {@{require in the definition of the power transmission coefficient}@}, we could use only {@{the _x_ component \(rather than the full _xy_ component\) of __H__ or __E__}@} or, equivalently, simply {@{multiply _EH_<!-- markdown separator -->/2 by the proper geometric factor}@}, obtaining {@{\(_E_<sup>2</sup>/2<!-- markdown separator -->_Z_\)cos _θ_}@}.

From {@{equations \(__[13](#math%2013)__\) and \(__[21](#math%2021)__\)}@}, taking {@{squared magnitudes}@}, we find that {@{the _[reflectivity](reflectivity.md#reflectivity)_ \(ratio of reflected power to incident power\)}@} is {@{$$R_{\text{s} }=\left|{\frac {Y_{1}\cos \theta _{\text{i} }-Y_{2}\cos \theta _{\text{t} } }{Y_{1}\cos \theta _{\text{i} }+Y_{2}\cos \theta _{\text{t} } } }\right|^{2}$$}@} __<a id="math 25">(25)</a>__ <p> for {@{the s polarization}@}, and {@{$$R_{\text{p} }=\left|{\frac {Y_{2}\cos \theta _{\text{i} }-Y_{1}\cos \theta _{\text{t} } }{Y_{2}\cos \theta _{\text{i} }+Y_{1}\cos \theta _{\text{t} } } }\right|^{2}$$}@} __<a id="math 26">(26)</a>__ <p> for {@{the p polarization}@}. Note that when comparing {@{the powers of two such waves in the same medium and with the same cos _θ_}@}, {@{the impedance and geometric factors mentioned above}@} are {@{identical and cancel out}@}. But in {@{computing the power _transmission_ \(below\)}@}, {@{these factors must be taken into account}@}.

{@{The simplest way to obtain the power transmission coefficient \(_[transmissivity](transmittance.md)_}@}, the ratio of {@{transmitted power to incident power _in the direction normal to the interface_, i.e. the _y_ direction\)}@} is to {@{use _R_ + _T_ = 1 \(conservation of energy\)}@}. In this way we find {@{$$T_{\text{s} }=1-R_{\text{s} }=\,{\frac {4\,{\text{Re} }\{Y_{1}Y_{2}\cos \theta _{\text{i} }\cos \theta _{\text{t} }\} }{\left|Y_{1}\cos \theta _{\text{i} }+Y_{2}\cos \theta _{\text{t} }\right|^{2} } }$$}@} __<a id="math 25T">(25T)</a>__ <p> for {@{the s polarization}@}, and {@{$$T_{\text{p} }=1-R_{\text{p} }=\,{\frac {4\,{\text{Re} }\{Y_{1}Y_{2}\cos \theta _{\text{i} }\cos \theta _{\text{t} }\} }{\left|Y_{2}\cos \theta _{\text{i} }+Y_{1}\cos \theta _{\text{t} }\right|^{2} } }$$}@} __<a id="math 26T">(26T)</a>__ <p> for {@{the p polarization}@}.

In the case of {@{an interface between two lossless media}@} \(for which {@{ϵ and μ are _real_ and positive}@}\), one can {@{obtain these results \(annotation: the above results\) directly}@} using {@{the squared magnitudes of the amplitude transmission coefficients that we found earlier in equations \(__[14](#math%2014)__\) and \(__[22](#math%2022)__\)}@}. But, for {@{given amplitude \(as noted above\)}@}, {@{the component of the Poynting vector in the _y_ direction}@} is {@{proportional to the geometric factor cos <!-- markdown separator -->_θ_}@} and {@{inversely proportional to the wave impedance _Z_}@}. Applying {@{these corrections to each wave}@}, we obtain {@{two ratios multiplying the square of the amplitude transmission coefficient}@}: {@{$$T_{\text{s} }=\left({\frac {2Y_{1}\cos \theta _{\text{i} } }{Y_{1}\cos \theta _{\text{i} }+Y_{2}\cos \theta _{\text{t} } } }\right)^{2}{\frac {\,Y_{2}\,}{Y_{1} } }\,{\frac {\cos \theta _{\text{t} } }{\cos \theta _{\text{i} } } }={\frac {4Y_{1}Y_{2}\cos \theta _{\text{i} }\cos \theta _{\text{t} } }{\left(Y_{1}\cos \theta _{\text{i} }+Y_{2}\cos \theta _{\text{t} }\right)^{2} } }$$}@} __<a id="math 27">(27)</a>__ <p> for {@{the s polarization}@}, and {@{$$T_{\text{p} }=\left({\frac {2Y_{1}\cos \theta _{\text{i} } }{Y_{2}\cos \theta _{\text{i} }+Y_{1}\cos \theta _{\text{t} } } }\right)^{2}{\frac {\,Y_{2}\,}{Y_{1} } }\,{\frac {\cos \theta _{\text{t} } }{\cos \theta _{\text{i} } } }={\frac {4Y_{1}Y_{2}\cos \theta _{\text{i} }\cos \theta _{\text{t} } }{\left(Y_{2}\cos \theta _{\text{i} }+Y_{1}\cos \theta _{\text{t} }\right)^{2} } }$$}@} __<a id="math 28">(28)</a>__ <p> for {@{the p polarization}@}. {@{The last two equations}@} apply only to {@{lossless dielectrics}@}, and only at {@{incidence angles smaller than the critical angle}@} \(beyond which, {@{of course, _T_ = 0}@}\).

For {@{unpolarized light}@}: {@{$$T={1 \over 2}(T_{s}+T_{p})$$ $$R={1 \over 2}(R_{s}+R_{p})$$}@} where {@{$R+T=1$}@}.

### equal refractive indices

From {@{equations \(__[4](#math%204)__\) and \(__[5](#math%205)__\)}@}, we see that {@{two dissimilar media}@} will have {@{the same refractive index, but different admittances}@}, if {@{the ratio of their permeabilities is the inverse of the ratio of their permittivities}@}. In {@{that unusual situation}@} we have {@{_θ_<sub>t</sub> = _θ_<sub>i</sub>}@} \(that is, {@{the transmitted ray is undeviated}@}\), so that {@{the cosines in equations \(__[13](#math%2013)__\), \(__[14](#math%2014)__\), \(__[21](#math%2021)__\), \(__[22](#math%2022)__\), and \(__[25](#math%2025)__\) to \(__[28](#math%2028)__\) cancel out}@}, and {@{all the reflection and transmission ratios}@} become {@{independent of the angle of incidence}@}; in other words, {@{the ratios for normal incidence}@} become {@{applicable to all angles of incidence}@}.<sup>[\[35\]](#^ref-35)</sup> When extended to {@{spherical reflection or scattering}@}, this results in {@{the Kerker effect for [Mie scattering](Mie%20scattering.md)}@}.

### non-magnetic media

Since {@{the Fresnel equations were developed for optics}@}, they are usually {@{given for non-magnetic materials}@}. {@{Dividing \(__[4](#math%204)__\) by \(__[5](#math%205)__\)}@} yields {@{$$Y={\frac {n}{\,c\mu \,} }\,.$$}@} For {@{non-magnetic media}@} we can {@{substitute the [vacuum permeability](vacuum%20permeability.md) _μ_<sub>0</sub> for _μ_}@}, so that {@{$$Y_{1}={\frac {n_{1} }{\,c\mu _{0} } }~~;~~~Y_{2}={\frac {n_{2} }{\,c\mu _{0} } }\,;$$}@} that is, the admittances are simply {@{proportional to the corresponding refractive indices}@}. When {@{we make these substitutions}@} in {@{equations \(__[13](#math%2013)__\) to \(__[16](#math%2016)__\) and equations \(__[21](#math%2021)__\) to \(__[26](#math%2026)__\)}@}, {@{the factor _cμ_<sub>0</sub> cancels out}@}. For {@{the amplitude coefficients}@} we obtain:<sup>[\[5\]](#^ref-5)</sup><sup>[\[6\]](#^ref-6)</sup> {@{$$r_{\text{s} }={\frac {n_{1}\cos \theta _{\text{i} }-n_{2}\cos \theta _{\text{t} } }{n_{1}\cos \theta _{\text{i} }+n_{2}\cos \theta _{\text{t} } } }$$}@} __<a id="math 29">(29)</a>__ <p> {@{$$t_{\text{s} }={\frac {2n_{1}\cos \theta _{\text{i} } }{n_{1}\cos \theta _{\text{i} }+n_{2}\cos \theta _{\text{t} } } }\,$$}@} __<a id="math 30">(30)</a>__ <p> {@{$$r_{\text{p} }={\frac {n_{2}\cos \theta _{\text{i} }-n_{1}\cos \theta _{\text{t} } }{n_{2}\cos \theta _{\text{i} }+n_{1}\cos \theta _{\text{t} } } }$$}@} __<a id="math 31">(31)</a>__ <p> {@{$$t_{\text{p} }={\frac {2n_{1}\cos \theta _{\text{i} } }{n_{2}\cos \theta _{\text{i} }+n_{1}\cos \theta _{\text{t} } } }\,.$$}@} __<a id="math 32">(32)</a>__ <p>

For {@{the case of normal incidence}@} these reduce to: {@{$$r_{\text{s0} }={\frac {n_{1}-n_{2} }{n_{1}+n_{2} } }$$}@} __<a id="math 33">(33)</a>__ <p> {@{$$t_{\text{s0} }={\frac {2n_{1} }{n_{1}+n_{2} } }$$}@} __<a id="math 34">(34)</a>__ <p> {@{$$r_{\text{p0} }={\frac {n_{2}-n_{1} }{n_{2}+n_{1} } }$$}@} __<a id="math 35">(35)</a>__ <p> {@{$$t_{\text{p0} }={\frac {2n_{1} }{n_{2}+n_{1} } }\,.$$}@} __<a id="math 36">(36)</a>__ <p>

{@{The power reflection coefficients}@} become: {@{$$R_{\text{s} }=\left|{\frac {n_{1}\cos \theta _{\text{i} }-n_{2}\cos \theta _{\text{t} } }{n_{1}\cos \theta _{\text{i} }+n_{2}\cos \theta _{\text{t} } } }\right|^{2}$$}@} __<a id="math 37">(37)</a>__ <p> {@{$$R_{\text{p} }=\left|{\frac {n_{2}\cos \theta _{\text{i} }-n_{1}\cos \theta _{\text{t} } }{n_{2}\cos \theta _{\text{i} }+n_{1}\cos \theta _{\text{t} } } }\right|^{2}\,.$$}@} __<a id="math 38">(38)</a>__ <p>

{@{The power transmissions}@} can then be found from {@{_T_<!-- markdown separator --> = 1 − <!-- markdown separator -->_R_}@}.

<!-- markdownlint-disable-next-line MD024 -->
### Brewster's angle

For {@{equal permeabilities \(e.g., non-magnetic media\)}@}, if {@{_θ_<sub>i</sub> and _θ_<sub>t</sub> are _[complementary](complementary%20angles.md#combining%20angle%20pairs)_}@}, we can {@{substitute sin _θ_<sub>t</sub> for cos _θ_<sub>i</sub>, and sin _θ_<sub>i</sub> for cos _θ_<sub>t</sub>}@}, so that {@{the numerator in equation \(__[31](#math%2031)__\) becomes _n_<sub>2</sub>sin _θ_<sub>t</sub> − _n_<sub>1</sub>sin _θ_<sub>i</sub>}@}, which is {@{zero \(by Snell's law\)}@}. Hence {@{_r_<sub>p</sub> = 0  and only the s-polarized component is reflected}@}. This is {@{what happens at the [Brewster angle](Brewster%20angle.md)}@}. Substituting {@{cos _θ_<sub>i</sub> for sin _θ_<sub>t</sub> in Snell's law \(annotation: to make _θ_<sub>i</sub> and _θ_<sub>t</sub> complementary\)}@}, we readily obtain {@{$$\theta _{\text{i} }=\arctan(n_{2}/n_{1})$$}@} __<a id="math 39">(39)</a>__ <p> for {@{Brewster's angle}@}.

### equal permittivities

Although {@{it is not encountered in practice}@}, the equations can also apply to the case of {@{two media with a common permittivity but different refractive indices due to different permeabilities}@}. From {@{equations \(__[4](#math%204)__\) and \(__[5](#math%205)__\)}@}, if {@{_ϵ_ is fixed instead of _μ_}@}, then {@{_Y_ becomes _inversely_ proportional to _n_}@}, with the result that {@{the subscripts 1 and 2 in equations \(__[29](#math%2029)__\) to \(__[38](#math%2038)__\) are interchanged}@} \(due to the additional step of {@{multiplying the numerator and denominator by _n_<sub>1</sub>_n_<sub>2</sub>}@}\). Hence, in {@{\(__[29](#math%2029)__\) and \(__[31](#math%2031)__\)}@}, {@{the expressions for _r_<sub>s</sub> and _r_<sub>p</sub> in terms of refractive indices will be interchanged}@}, so that {@{Brewster's angle \(__[39](#math%2039)__\) will give _r_<sub>s</sub> = 0 instead of _r_<sub>p</sub> = 0}@}, and any beam reflected at that angle will be {@{p-polarized instead of s-polarized}@}.<sup>[\[36\]](#^ref-36)</sup> Similarly, {@{Fresnel's sine law}@} will {@{apply to the p polarization instead of the s polarization}@}, and {@{his tangent law}@} to {@{the s polarization instead of the p polarization}@}.

{@{This switch of polarizations}@} has an analog in {@{the old mechanical theory of light waves}@} \(see _[§ History](#history)_, above\). One could predict {@{reflection coefficients that agreed with observation}@} by supposing \(like {@{Fresnel}@}\) that {@{different refractive indices were due to different _densities_}@} and that {@{the vibrations were _normal_ to what was then called the [plane of polarization](plane%20of%20polarization.md)}@}, or by supposing \(like {@{[MacCullagh](James%20MacCullagh.md) and [Neumann](Franz%20Ernst%20Neumann.md)}@}\) that {@{different refractive indices were due to different _elasticities_}@} and that {@{the vibrations were _parallel_ to that plane}@}.<sup>[\[37\]](#^ref-37)</sup> Thus the condition of {@{equal permittivities and unequal permeabilities}@}, although {@{not realistic}@}, is of {@{some historical interest}@}.

## see also

- [Jones calculus](Jones%20calculus.md)
- [Polarization mixing](polarization%20mixing.md)
- [Index-matching material](index-matching%20material.md)
- [Field and power quantities](field%20and%20power%20quantities.md)
- [Fresnel rhomb](fresnel%20rhomb.md), ::@:: Fresnel's apparatus to produce circularly polarised light
- [Reflection loss](reflection%20loss.md)
- [Specular reflection](specular%20reflection.md)
- [Schlick's approximation](Schlick's%20approximation.md)
- [Snell's window](Snell's%20window.md)
- [X-ray reflectivity](X-ray%20reflectivity.md)
- [Plane of incidence](plane%20of%20incidence.md)
- [Reflections of signals on conducting lines](reflections%20of%20signals%20on%20conducting%20lines.md)

## notes

1. The above form \(__[1](#math%201)__\) is typically {@{used by physicists}@}. {@{[Electrical engineers](electrical%20engineering.md)}@} typically prefer {@{the form __E<sub>k</sub>__<!-- markdown separator -->&hairsp;<!-- markdown separator -->_e_<sup>_j_\(_ωt_<!-- markdown separator -->−<!-- markdown separator -->__k⋅r__\)</sup>}@}; that is, they not only {@{use _j_ instead of _i_ for the imaginary unit}@}, but also {@{change the sign of the exponent}@}, with the result that {@{the whole expression is replaced by its [complex conjugate](complex%20conjugate.md)}@}, leaving {@{the real part unchanged}@} \[Cf. \(e.g.\) Collin, 1966, p.&hairsp;41, eq. \(2.81\)\]. {@{The electrical engineers' form and the formulas derived therefrom}@} may be {@{converted to the physicists' convention}@} by {@{substituting _−i_ for _j_}@}. <a id="^ref-note-1"></a>^ref-note-1
2. In {@{the electrical engineering convention}@}, {@{the time-dependent factor}@} is {@{_e_<sup>_jωt_</sup>}@}, so that {@{a phase advance}@} corresponds to {@{multiplication by a complex constant with a _positive_ argument}@}, and {@{differentiation w.r.t. time}@} corresponds to {@{multiplication by +_jω_}@}. This article, however, uses {@{the physics convention}@}, whose {@{time-dependent factor}@} is {@{_e_<sup>−<!-- markdown separator -->_iωt_</sup>}@}. Although {@{the imaginary unit does not appear explicitly in the results given here}@}, {@{the time-dependent factor}@} affects {@{the interpretation of any results that turn out to be complex}@}. <a id="^ref-note-2"></a>^ref-note-2

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Fresnel_equations) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. Born & Wolf, 1970, p. 38. <a id="^ref-1"></a>^ref-1
2. Hecht, 1987, p. 100. <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFDriggersHoffmanDriggers2011"></a> Driggers, Ronald G.; Hoffman, Craig; Driggers, Ronald \(2011\). _Encyclopedia of Optical Engineering_. [doi](doi%20(identifier).md):[10.1081/E-EOE](https://doi.org/10.1081%2FE-EOE). [ISBN](ISBN%20(identifier).md) [978-0-8247-0940-2](https://en.wikipedia.org/wiki/Special:BookSources/978-0-8247-0940-2). <a id="^ref-3"></a>^ref-3
4. Hecht, 1987, p. 102. <a id="^ref-4"></a>^ref-4
5. Lecture notes by Bo Sernelius, [main site](http://www.ifm.liu.se/courses/TFYY67/) [Archived](https://web.archive.org/web/20120222125421/http://www.ifm.liu.se/courses/TFYY67/) 2012-02-22 at the [Wayback Machine](Wayback%20Machine.md), see especially [Lecture 12](http://www.ifm.liu.se/courses/TFYY67/Lect12.pdf) . <a id="^ref-5"></a>^ref-5
6. Born & Wolf, 1970, p.&hairsp;40, eqs. \(20\),&hairsp;\(21\). <a id="^ref-6"></a>^ref-6
7. Hecht, 2002, p.&hairsp;116, eqs. \(4.49\),&hairsp;\(4.50\). <a id="^ref-7"></a>^ref-7
8. Hecht, 2002, p.&hairsp;120, eq.&hairsp;\(4.56\). <a id="^ref-8"></a>^ref-8
9. Hecht, 2002, p.&hairsp;120, eq.&hairsp;\(4.57\). <a id="^ref-9"></a>^ref-9
10. Fresnel, 1866, p.&hairsp;773. <a id="^ref-10"></a>^ref-10
11. Hecht, 2002, p.&hairsp;115, eq.&hairsp;\(4.42\). <a id="^ref-11"></a>^ref-11
12. Fresnel, 1866, p.&hairsp;757. <a id="^ref-12"></a>^ref-12
13. Hecht, 2002, p.&hairsp;115, eq.&hairsp;\(4.43\). <a id="^ref-13"></a>^ref-13
14. E. Verdet, in Fresnel, 1866, p.&hairsp;789n. <a id="^ref-14"></a>^ref-14
15. Born & Wolf, 1970, p.&hairsp;40, eqs.&hairsp;\(21a\). <a id="^ref-15"></a>^ref-15
16. Jenkins & White, 1976, p.&hairsp;524, eqs.&hairsp;\(25a\). <a id="^ref-16"></a>^ref-16
17. Whittaker, 1910, p.&hairsp;134; Darrigol, 2012, p. 213. <a id="^ref-17"></a>^ref-17
18. <a id="CITEREFHeavens1955"></a> Heavens, O. S. \(1955\). _Optical Properties of Thin Films_. Academic Press. chapt. 4. <a id="^ref-18"></a>^ref-18
19. Darrigol, 2012, pp. 191–2. <a id="^ref-19"></a>^ref-19
20. D. Brewster, ["On the laws which regulate the polarisation of light by reflexion from transparent bodies"](http://rstl.royalsocietypublishing.org/content/105/125.full.pdf), _Philosophical Transactions of the Royal Society_, vol. 105, pp. 125–59, read 16 March 1815. <a id="^ref-20"></a>^ref-20
21. T. Young, "Chromatics" \(written Sep–Oct 1817\), _Supplement to the Fourth, Fifth, and Sixth Editions of the Encyclopædia Britannica_, vol. 3 \(first half, issued February 1818\), pp. 141–63, [concluding sentence](https://archive.org/stream/gri_33125011196801#page/n264/mode/1up). <a id="^ref-21"></a>^ref-21
22. Buchwald, 1989, pp. 390–91; Fresnel, 1866, pp. 646–8. <a id="^ref-22"></a>^ref-22
23. A. Fresnel, "Note sur le calcul des teintes que la polarisation développe dans les lames cristallisées" et seq., _Annales de Chimie et de Physique_, vol. 17, pp. 102–11 \(May 1821\), 167–96 \(June 1821\), 312–15 \("Postscript", July 1821\); reprinted in Fresnel, 1866, pp. 609–48; translated as "On the calculation of the tints that polarization develops in crystalline plates, & postscript", [Zenodo](zenodo.md): [4058004](https://zenodo.org/record/4058004) / [doi](doi%20(identifier).md):[10.5281/zenodo.4058004](https://doi.org/10.5281%2Fzenodo.4058004), 2021. <a id="^ref-23"></a>^ref-23
24. A. Fresnel, "Mémoire sur la loi des modifications que la réflexion imprime à la lumière polarisée" \("Memoir on the law of the modifications that reflection impresses on polarized light"\), read 7 January 1823; reprinted in Fresnel, 1866, pp. 767–99 \(full text, published 1831\), pp. 753–62 \(extract, published 1823\). See especially pp. 773 \(sine law\), 757 \(tangent law\), 760–61 and 792–6 \(angles of total internal reflection for given phase differences\). <a id="^ref-24"></a>^ref-24
25. Buchwald, 1989, pp. 391–3; Whittaker, 1910, pp. 133–5. <a id="^ref-25"></a>^ref-25
26. Buchwald, 1989, p.&hairsp;392. <a id="^ref-26"></a>^ref-26
27. Lloyd, 1834, pp. 369–70; Buchwald, 1989, pp. 393–4, 453; Fresnel, 1866, pp. 781–96. <a id="^ref-27"></a>^ref-27
28. Fresnel, 1866, pp. 760–61, 792–6; Whewell, 1857, p. 359. <a id="^ref-28"></a>^ref-28
29. Whittaker, 1910, pp. 177–179. <a id="^ref-29"></a>^ref-29
30. A. Fresnel, "Mémoire sur la double réfraction que les rayons lumineux éprouvent en traversant les aiguilles de cristal de roche suivant les directions parallèles à l'axe" \("Memoir on the double refraction that light rays undergo in traversing the needles of quartz in the directions parallel to the axis"\), read 9 December 1822; printed in Fresnel, 1866, pp. 731–751 \(full text\), pp. 719–729 \(_extrait_, first published in _Bulletin de la Société philomathique_ for 1822, pp. 191–8\). <a id="^ref-30"></a>^ref-30
31. Buchwald, 1989, pp. 230–231; Fresnel, 1866, p.&hairsp;744. <a id="^ref-31"></a>^ref-31
32. Buchwald, 1989, p.&hairsp;442; Fresnel, 1866, pp. 737–739, 749.  Cf. Whewell, 1857, pp. 356–358; Jenkins & White, 1976, pp. 589–590. <a id="^ref-32"></a>^ref-32
33. Compare M.V. Berry and M.R. Jeffrey, "Conical diffraction: Hamilton's diabolical point at the heart of crystal optics", in E. Wolf \(ed.\), _Progress in Optics_, vol. 50, Amsterdam: Elsevier, 2007, pp. 13–50, [doi](doi%20(identifier).md):[10.1016/S0079-6638\(07\)50002-8](https://doi.org/10.1016%2FS0079-6638%2807%2950002-8), at p.&hairsp;18, eq. \(2.2\). <a id="^ref-33"></a>^ref-33
34. This agrees with Born & Wolf, 1970, p.&hairsp;38, Fig. 1.10. <a id="^ref-34"></a>^ref-34
35. <a id="CITEREFGilesWild1982"></a> Giles, C.L.; Wild, W.J. \(1982\). "Fresnel Reflection and Transmission at a Planar Boundary from Media of Equal Refractive Indices". _Applied Physics Letters_. __40__ \(3\): 210–212. [Bibcode](bibcode%20(identifier).md):[1982ApPhL..40..210G](https://ui.adsabs.harvard.edu/abs/1982ApPhL..40..210G). [doi](doi%20(identifier).md):[10.1063/1.93043](https://doi.org/10.1063%2F1.93043). [S2CID](S2CID%20(identifier).md#S2CID) [118838757](https://api.semanticscholar.org/CorpusID:118838757). <a id="^ref-35"></a>^ref-35
36. More general Brewster angles, for which the angles of incidence and refraction are not necessarily complementary, are discussed in C.L. Giles and W.J. Wild, ["Brewster angles for magnetic media"](http://clgiles.ist.psu.edu/pubs/Brewster-magnetic.pdf), _International Journal of Infrared and Millimeter Waves_, vol. 6, no. 3 \(March 1985\), pp. 187–97. <a id="^ref-36"></a>^ref-36
37. Whittaker, 1910, pp. 133, 148–149; Darrigol, 2012, pp. 212, 229–231. <a id="^ref-37"></a>^ref-37

## sources

- M. Born and E. Wolf, 1970, _[Principles of Optics](Principles%20of%20Optics.md)_, 4th Ed., Oxford: Pergamon Press.
- J.Z. Buchwald, 1989, _The Rise of the Wave Theory of Light: Optical Theory and Experiment in the Early Nineteenth Century_, University of Chicago Press, [ISBN](ISBN%20(identifier).md) [0-226-07886-8](https://en.wikipedia.org/wiki/Special:BookSources/0-226-07886-8).
- R.E. Collin, 1966, _Foundations for Microwave Engineering_, Tokyo: McGraw-Hill.
- O. Darrigol, 2012, _A History of Optics: From Greek Antiquity to the Nineteenth Century_, Oxford, [ISBN](ISBN%20(identifier).md) [978-0-19-964437-7](https://en.wikipedia.org/wiki/Special:BookSources/978-0-19-964437-7).
- A. Fresnel, 1866 \(ed. H. de Senarmont, E. Verdet, and L. Fresnel\), _Oeuvres complètes d'Augustin Fresnel_, Paris: Imprimerie Impériale \(3 vols., 1866–70\), [vol. 1 \(1866\)](https://books.google.com/books?id=1l0_AAAAcAAJ).
- <a id="CITEREFGriffiths2017"></a> Griffiths, David J. \(2017\). "Chapter 9.3: Electromagnetic Waves in Matter". _Introduction to Electrodynamics_ \(4th ed.\). Cambridge University Press. [ISBN](ISBN%20(identifier).md) [978-1-108-42041-9](https://en.wikipedia.org/wiki/Special:BookSources/978-1-108-42041-9).
- E. Hecht, 1987, _Optics_, 2nd Ed., Addison Wesley, [ISBN](ISBN%20(identifier).md) [0-201-11609-X](https://en.wikipedia.org/wiki/Special:BookSources/0-201-11609-X).
- E. Hecht, 2002, _Optics_, 4th Ed., Addison Wesley, [ISBN](ISBN%20(identifier).md) [0-321-18878-0](https://en.wikipedia.org/wiki/Special:BookSources/0-321-18878-0).
- F.A. Jenkins and H.E. White, 1976, _Fundamentals of Optics_, 4th Ed., New York: McGraw-Hill, [ISBN](ISBN%20(identifier).md) [0-07-032330-5](https://en.wikipedia.org/wiki/Special:BookSources/0-07-032330-5).
- H. Lloyd, 1834, ["Report on the progress and present state of physical optics"](https://books.google.com/books?id=mtU4AAAAMAAJ&pg=PA295), _Report of the Fourth Meeting of the British Association for the Advancement of Science_ \(held at Edinburgh in 1834\), London: J. Murray, 1835, pp. 295–413.
- W. Whewell, 1857, _History of the Inductive Sciences: From the Earliest to the Present Time_, 3rd Ed., London: J.W. Parker & Son, [vol. 2](https://archive.org/details/bub_gb_cBSrVEkaR8EC).
- [E. T. Whittaker](E.%20T.%20Whittaker.md), 1910, [_A History of the Theories of Aether and Electricity: From the Age of Descartes to the Close of the Nineteenth Century_](A%20History%20of%20the%20Theories%20of%20Aether%20and%20Electricity.md), London: Longmans, Green, & Co.

## external links

- [Fresnel Equations](http://scienceworld.wolfram.com/physics/FresnelEquations.html) – Wolfram.
- [Fresnel equations calculator](http://www.fxsolver.com/solve/share/0E2w3XC71x0z_Wu9eQ7SPw==/)
- [FreeSnell](http://people.csail.mit.edu/jaffer/FreeSnell) – Free software computes the optical properties of multilayer materials.
- [Thinfilm](http://thinfilm.hansteen.net/) – Web interface for calculating optical properties of thin films and multilayer materials \(reflection & transmission coefficients, ellipsometric parameters Psi & Delta\).
- [Simple web interface for calculating single-interface reflection and refraction angles and strengths](http://www.calctool.org/CALC/phys/optics/reflec_refrac).
- [Reflection and transmittance for two dielectrics](http://wm.eecs.umich.edu/webMathematica/eecs434/f08/ideliz/final.jsp)<sup>\[_[permanent dead link](https://en.wikipedia.org/wiki/Wikipedia:Link%20rot)_\]</sup> – Mathematica interactive webpage that shows the relations between index of refraction and reflection.
- [A self-contained first-principles derivation](http://www.jedsoft.org/physics/notes/multilayer.pdf) of the transmission and reflection probabilities from a multilayer with complex indices of refraction.

> __[Portal](https://en.wikipedia.org/wiki/Wikipedia:Contents/Portals):__
>
> - __![icon](../../archives/Wikimedia%20Commons/Stylised%20atom%20with%20three%20Bohr%20model%20orbits%20and%20stylised%20nucleus.svg) [Physics](https://en.wikipedia.org/wiki/Portal:Physics)__

<!-- markdownlint MD028 -->

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Eponymous equations of physics](https://en.wikipedia.org/wiki/Category:Eponymous%20equations%20of%20physics)
> - [Light](https://en.wikipedia.org/wiki/Category:Light)
> - [Geometrical optics](https://en.wikipedia.org/wiki/Category:Geometrical%20optics)
> - [Physical optics](https://en.wikipedia.org/wiki/Category:Physical%20optics)
> - [Polarization \(waves\)](https://en.wikipedia.org/wiki/Category:Polarization%20%28waves%29)
> - [History of physics](https://en.wikipedia.org/wiki/Category:History%20of%20physics)
