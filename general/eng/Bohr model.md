---
aliases:
  - Bohr model
  - Rutherford–Bohr model
tags:
  - flashcard/active/general/eng/Bohr_model
  - language/in/English
---

# Bohr model

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

The __Bohr model__ or __{@{Rutherford–Bohr}@} model__ is {@{an [atom](atom.md) model}@} where {@{a small, dense [nucleus](nucleus.md) is orbited by [electrons](electron.md)}@}. They are attracted by {@{electrostatic forces}@}. It was presented by {@{[Niels Bohr](Niels%20Bohr.md)}@} and {@{[Ernest Rutherford](Ernest%20Rutherford.md) in 1913}@}. <!--SR:!2026-12-03,998,290!2026-06-04,964,330!2026-01-27,565,190!2029-11-29,1767,310!2027-10-02,984,232!2026-02-12,826,332-->

The model gives almost exact results only when {@{two charged points orbit each other much slower than light}@}, like {@{an atom where one electron is far away from everything else}@}. <!--SR:!2028-04-16,1209,290!2029-08-28,1689,292-->

## postulates

The model is based on three postulates:

1. The electron revolves at {@{certain orbits only with certain distances from the nucleus called stationary orbits}@} {@{without radiating energy}@}. <a id="^23e80f"></a>^23e80f
2. The stationary orbits have distances {@{for which the revolving electron has an [angular momentum](angular%20momentum.md) of an integer multiple of the reduced [Planck constant](Planck%20constant.md): $m_\mathrm{e} v r = \hbar n$}@}, where {@{$n\in\mathbb{Z}^+$ is called the [principal quantum number](principal%20quantum%20number.md)}@}. The orbits have definite energies called {@{[energy levels](energy%20level.md), energy shells, or energy states}@}. <a id="^f5a73f"></a>^f5a73f
3. Electrons only gain or lose energy by {@{jumping from one stationary orbit to another}@}. [Electromagnetic radiation](electromagnetic%20radiation.md) of frequency $\nu$ is respectively {@{absorbed or emitted}@} according to the {@{[Planck relation](Planck%20relation.md): $\Delta{}E=E_2-E_1=h\nu$}@}, where {@{$h$ is the [Planck constant](Planck%20constant)}@}. <!--SR:!2027-11-05,1102,250!2027-03-08,821,270!2028-11-11,1256,230!2028-04-12,1375,290!2028-03-28,1364,290!2029-04-04,1586,272!2026-03-28,918,332!2028-11-05,1555,292!2027-07-06,1198,332-->

## electron energy levels

By the [first postulate](#^23e80f), {@{the [centripetal force](centripetal%20force.md) equals the [Coulomb force](Coulomb%20force.md)}@}. Assuming {@{the nucleus mass is much larger than the electron mass}@}:
{@{$$\frac{m_\mathrm{e}v^2}r=\frac{Zk_\mathrm{e}\mathrm{e}^2}{r^2}$$}@}
where {@{$m_\mathrm{e}$ is the electron mass, $\mathrm{e}$ is the [elementary charge](elementary%20charge.md), $k_\mathrm{e}$ is the [Coulomb constant](Coulomb%20constant.md), and $Z$ is the atomic number of the atom}@}. Rearranging, this equation determines the electron's speed from its radius:
{@{$$v=\sqrt{\frac{Zk_\mathrm{e}\mathrm{e}^2}{m_\mathrm{e}r} }$$}@}
Substitute the equation into {@{the equation from the [second postulate](#^f5a73f)}@}:
{@{$$m_\mathrm{e} \sqrt{\frac {Z k_\mathrm{e} \mathrm{e}^2} {m_\mathrm{e} r} } r = \hbar n$$}@}
We can get the radius in terms of $n$:
{@{$$r_n=\frac{\hbar^2 n^2}{Zk_\mathrm{e}\mathrm{e}^2m_\mathrm{e} }$$}@}
and energy in terms of $n$:
{@{$$E_n=-\frac12m_\mathrm{e}v^2=-\frac{Zk_\mathrm{e}\mathrm{e}^2}{2r_n}=-\frac{Z^2 k_\mathrm{e}^2 \mathrm{e}^4 m_\mathrm{e} }{2 \hbar^2 n^2} \approx \frac{-13.6 Z^2} {n^2} ~ \mathrm{eV}$$}@} <!--SR:!2034-08-06,3239,334!2025-12-17,809,314!2030-12-04,1913,274!2028-01-14,818,294!2027-12-16,1234,294!2030-07-28,1842,274!2029-07-22,1528,274!2026-01-31,144,130!2028-09-29,1170,254-->

From the energy equation, an electron of [hydrogen](hydrogen.md) ($Z=1$) in the [ground state](ground%20state.md) ($n=1$) {@{has about 13.6 eV less energy than a motionless electron infinitely far away}@}, which is also {@{the atom's [ionization energy](ionization%20energy.md)}@}. <!--SR:!2032-12-02,2596,299!2030-05-23,2007,319-->

## Rydberg formula

The combination of natural constants in the energy formula is the {@{Rydberg energy $R_\mathrm{E}$}@}:
{@{$$\begin{aligned}R_\mathrm{E}&=\frac{k_\mathrm{e}^2\mathrm{e}^4m_\mathrm{e} }{2\hbar^2}\\&=2.179\,872\,361\,1035(42)\times10^{-18}~\mathrm{J}\\&=13.605\,693\,122\,944(26)~\mathrm{eV}\end{aligned}$$}@} <!--SR:!2028-11-27,1485,302!2026-05-27,376,222-->

The energy of a photon emitted by a hydrogen atom is:
{@{$$E=E_i-E_f=R_\mathrm{E}\left(\frac1{n_f^2}-\frac1{n_i^2}\right)$$}@}, where {@{$n_f$ is the final energy level and $n_i$ is the initial energy level}@}. Since the energy of a photon is $E=\frac{hc}\lambda$, by {@{making inverse of the wavelength $\frac1\lambda$ the subject}@}, the resulting constant is the {@{[Rydberg constant](Rydberg%20constant.md) $R_\infty$}@}:
{@{$$\frac1\lambda=R_\infty\left(\frac1{n_f^2}-\frac1{n_i^2}\right)$$}@} The constant is {@{$R_\infty=\frac{R_\mathrm{E} }{hc}=10\,973\,731.568\,157(12)~\mathrm{m}^{-1}$}@}. <!--SR:!2028-04-21,1338,302!2035-01-17,3387,342!2026-01-26,836,322!2031-12-25,2428,322!2029-01-09,1489,302!2025-11-25,128,150-->

## limitations

```Python
# pytextgen generate data
return await memorize_table(
  __env__.cwf_sects('0692', '3810',),
  ('name', 'description',),
  (
    ('brightness', 'relative brightness of spectral lines',),
    ('multiple [electrons](electron.md)', 'spectra of [atoms](atom.md) with multiple [electrons](electron.md)',),
    (R'naturalness', 'reason why the [angular momentum](angular%20momentum.md) is a intergral multiple of the [reduced Planck constant](Planck%20constant.md#reduced%20Planck%20constant)',),
    ('structures', '[fine structure](fine%20structure.md) and [hyperfine structure](hyperfine%20structure.md) of spectral lines',),
  ),
  lambda datum: map(cloze, datum),
)
```

The Bohr model fails to explain:

<!--pytextgen generate section="0692"--><!-- The following content is generated at 2024-03-07T10:22:56.394226+08:00. Any edits will be overridden! -->

> | name | description |
> |-|-|
> | {@{brightness}@} | {@{relative brightness of spectral lines}@} |
> | {@{multiple [electrons](electron.md)}@} | {@{spectra of [atoms](atom.md) with multiple [electrons](electron.md)}@} |
> | {@{naturalness}@} | {@{reason why the [angular momentum](angular%20momentum.md) is a intergral multiple of the [reduced Planck constant](Planck%20constant.md#reduced%20Planck%20constant)}@} |
> | {@{structures}@} | {@{[fine structure](fine%20structure.md) and [hyperfine structure](hyperfine%20structure.md) of spectral lines}@} | <!--SR:!2030-04-10,1775,373!2029-05-07,1507,373!2027-05-17,908,353!2027-01-19,749,333!2029-10-14,1625,381!2027-02-10,807,341!2027-08-06,972,361!2027-03-21,798,341-->

<!--/pytextgen-->

<!--pytextgen generate section="3810"--><!-- The following content is generated at 2024-02-17T18:00:08.056049+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←brightness <!--SR:!2029-08-22,1749,344!2029-10-05,1627,373-->
- brightness→::@::←multiple [electrons](electron.md) <!--SR:!2028-02-10,1063,284!2027-08-23,868,293-->
- multiple [electrons](electron.md)→::@::←naturalness <!--SR:!2026-06-05,837,324!2030-07-31,1792,333-->
- naturalness→::@::←structures <!--SR:!2027-02-11,981,324!2029-05-26,1347,293-->
- structures→::@::←_(end)_ <!--SR:!2026-12-12,724,333!2025-11-11,436,333-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Bohr_model) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
