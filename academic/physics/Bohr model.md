---
aliases: ['Rutherford–Bohr model',]
---

#flashcards/physics/Bohr_model #academic/physics

# Bohr model

The __Bohr model__ or __{{Rutherford–Bohr}} model__ is {{an [atom](atom.md) model}} where {{a small, dense [nucleus](nucleus.md) is orbited by [electrons](electron.md)}}. They are attracted by {{electrostatic forces}}. It was presented by {{[Niels Bohr](Niels%20Bohr.md)}} and {{[Ernest Rutherford](Ernest%20Rutherford.md)}} in {{1913}}. <!--SR:!2022-12-28,10,250!2023-01-04,16,290!2022-12-26,2,210!2022-12-30,12,270!2022-12-27,9,252!2023-01-02,14,292!2022-12-30,9,272-->

The model gives almost exact results only when {{two charged points orbit each other much slower than light}}, like {{an atom where one electron is far away from everything else}}. <!--SR:!2022-12-28,10,252!2022-12-30,11,272-->

## postulates

The model is based on three postulates:

1. The electron revolves at {{certain orbits only with certain distances from the nucleus called stationary orbits}} {{without radiating energy}}. ^23e80f
2. The stationary orbits have distances {{for which the revolving electron has an [angular momentum](angular%20momentum.md) of an integer multiple of the reduced [Planck constant](Planck%20constant.md): $m_\mathrm{e}vr=n\hbar$}}, where {{$n\in\mathbb{Z}^+$ is called the [principal quantum number](principal%20quantum%20number.md)}}. The orbits have definite energies called {{[energy levels](energy%20level.md), energy shells, or energy states}}. ^f5a73f
3. Electrons only gain or lose energy by {{jumping from one stationary orbit to another}}. [Electromagnetic radiation](electromagnetic%20radiation.md) of frequency $\nu$ is respectively {{absorbed or emitted}} according to the {{[Planck relation](Planck%20relation.md): $\Delta{}E=E_2-E_1=h\nu$}}, where {{$h$ is the [Planck constant](Planck%20constant)}}. <!--SR:!2022-12-26,6,230!2022-12-31,12,270!2022-12-25,5,230!2022-12-27,7,250!2022-12-28,8,250!2022-12-28,10,252!2022-12-31,13,272!2022-12-25,5,232!2023-01-05,17,292-->

## electron energy levels

By the [first postulate](#^23e80f), {{the [centripetal force](centripetal%20force.md) equals the [Coulomb force](Coulomb%20force.md)}}. Assuming {{the nucleus mass is much larger than the electron mass}}:
{{$$\frac{m_\mathrm{e}v^2}r=\frac{Zk_\mathrm{e}\mathrm{e}^2}{r^2}$$}}
where {{$m_\mathrm{e}$ is the electron mass, $\mathrm{e}$ is the [elementary charge](elementary%20charge.md), $k_\mathrm{e}$ is the [Coulomb constant](Coulomb%20constant.md), and $Z$ is the atomic number of the atom}}. Rearranging, this equation determines the electron's speed from its radius:
{{$$v=\sqrt{\frac{Zk_\mathrm{e}\mathrm{e}^2}{m_\mathrm{e}r} }$$}}
Substitute the equation into {{the equation from the [second postulate](#^f5a73f)}}:
{{$$m_\mathrm{e}\sqrt{\frac{Zk_\mathrm{e}\mathrm{e}^2}{m_\mathrm{e}r} }r=n\hbar$$}}
We can get the radius in terms of $n$:
{{$$r_n=\frac{n^2\hbar^2}{Zk_\mathrm{e}\mathrm{e}^2m_\mathrm{e} }$$}}
and energy in terms of $n$:
{{$$E_n=-\frac12m_\mathrm{e}v^2=-\frac{Zk_\mathrm{e}\mathrm{e}^2}{2r_n}=-\frac{Z^2k_\mathrm{e}^2\mathrm{e}^4m_\mathrm{e} }{2\hbar^2n^2}\approx\frac{-13.6Z^2}{n^2}~\mathrm{eV}$$}} <!--SR:!2023-01-03,11,274!2023-01-02,10,274!2023-01-08,16,294!2023-01-05,13,294!2023-01-03,11,274!2023-01-01,9,274!2023-01-01,9,274!2022-12-25,2,254!2022-12-25,2,254-->

From the energy equation, an electron of [hydrogen](hydrogen.md) ($Z=1$) in the [ground state](ground%20state.md) ($n=1$) {{has about 13.6 eV less energy than a motionless electron infinitely far away}}, which is also {{the atom's [ionization energy](ionization%20energy.md)}}. <!--SR:!2023-01-02,10,279!2023-01-03,11,279-->

## Rydberg formula

The combination of natural constants in the energy formula is the {{Rydberg energy $R_\mathrm{E}$}}:
{{$$\begin{aligned}R_\mathrm{E}&=\frac{k_\mathrm{e}^2\mathrm{e}^4m_\mathrm{e}}{2\hbar^2}\\&=2.179\,872\,361\,1035(42)\times10^{-18}~\mathrm{J}\\&=13.605\,693\,122\,944(26)~\mathrm{eV}\end{aligned}$$}}

The energy of a photon emitted by a hydrogen atom is:
{{$$E=E_i-E_f=R_\mathrm{E}\left(\frac1{n_f^2}-\frac1{n_i^2}\right)$$}}, where {{$n_f$ is the final energy level and $n_i$ is the initial energy level}}. Since the energy of a photon is $E=\frac{hc}\lambda$, by {{making inverse of the wavelength $\frac1\lambda$ the subject}}, the resulting constant is the {{[Rydberg constant](Rydberg%20constant.md) $R_\infty$}}:
{{$$\frac1\lambda=R_\infty\left(\frac1{n_f^2}-\frac1{n_i^2}\right)$$}} The constant is {{$R_\infty=\frac{R_\mathrm{E}}{hc}=10\,973\,731.568\,160(21)~\mathrm{m}^{-1}$}}.
