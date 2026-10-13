---
aliases:
  - HKUST PHYS 2022 tutorial 4 tutorial
  - PHYS 2022 tutorial 4 tutorial
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/tutorials/tutorial_4/tutorial
  - language/in/English
---

# tutorial

- HKUST PHYS 2022 tutorial 4
- parent: [tutorial 4](index.md)

---

- title: Tutorial 4
- points: 20
- grade: 20/20
- submitting: \[missing\]

---

No additional details were added for this assignment.

## problems

> Problem (Choose any 2):
>
> __1.__ Low Energy Electron Diffraction (LEED) pattern of a Cu(100) surface is shown. It is recorded using a beam energy (electron's energy) of $100\ \text{V}$. The nearest points are located $5\ \text{cm}$ from the centre of the screen. When decreasing the beam energy to $50\ \text{V}$, how far are the nearest points from the centre?
>
> Use approximation: Dot separation $r \propto \phi \propto \sin\phi$, where $\phi$ is diffraction angle.
>
> The screen photograph shows the dot pattern with a $5\ \text{cm}$ scale marking.
>
> - solution: the nearest points sit at {@{$r = 5\sqrt{2} \approx 7.07\ \text{cm}$ from the centre}@}
> - explanation: {@{The diffraction condition}@} is {@{$n\lambda = D\sin\phi$}@}, so {@{$\sin\phi$ tracks $\lambda$ directly}@}. {@{The approximation $r \propto \phi \propto \sin\phi$}@} carries that onto the screen: the spot separation {@{follows $\sin\phi$}@}. The electron wavelength is {@{$\lambda = h/\sqrt{2meV}$}@}, so {@{$\lambda \propto V^{-1/2}$}@}. {@{Dropping the beam energy from $100\ \text{V}$ to $50\ \text{V}$}@} {@{lengthens $\lambda$ by $\sqrt{2}$}@}, and {@{the nearest points}@} move {@{from $5\ \text{cm}$ out to $5\sqrt{2} \approx 7.07\ \text{cm}$}@}.

<!-- markdownlint MD028 -->

> __2.__ Graphs a to e are the real parts of five wavefunctions ($y = \mathrm{Re}(\Psi(x))$). Find out which are invalid wavefunctions and explain which rule(s) do they violate?
>
> - a: a semicircular arc resting on the $x$ axis, symmetric about the $y$ axis
> - b: a narrow symmetric spike, tall and sharply peaked at $x = 0$
> - c: a circle centred on the $x$ axis, crossing it at two points
> - d: a sigmoid descending from a positive plateau on the left to a negative plateau on the right
> - e: two branches meeting a vertical asymptote at $x = 0$, positive in the first quadrant and negative in the third
>
> - solution: the invalid wavefunctions are {@{all five graphs: none of a to e is a valid wave function}@}
> - explanation: All five graphs break {@{one of the [conditions on a valid wave function](../../wave%20function.md#conditions%20on%20a%20valid%20wave%20function)}@}. Graph c gives {@{two $y$ values to one $x$, so it is not single-valued}@}. Graph d {@{flattens at a nonzero plateau on each side, so it never vanishes at $x \to \pm\infty$ and cannot be normalised}@}. Graph e {@{diverges at the vertical asymptote $x = 0$, so it is not finite there}@}. Graphs a and b {@{break the slope condition instead}@}: {@{the first derivative has to stay continuous wherever the potential is finite}@}. Graph a carries {@{a vertical tangent at each end: the slope jumps from vertical to zero as the arc stops}@}, while graph b {@{turns through a cusp at $x = 0$, its slope flipping sign in one step}@}. {@{The infinite square well}@} {@{ignores this condition}@}: $\Psi$ {@{vanishes at the walls while its slope jumps}@}. {@{The exception holds only}@} because {@{the well itself is unphysical: no real barrier is infinitely tall}@}. Wherever {@{$V$ is finite, both $\Psi$ and $d\Psi/dx$ stay continuous}@}.

<!-- markdownlint MD028 -->

> __3.__ The normalized wavefunctions of a simple harmonic oscillator are:
>
> $$\psi_3(x) = \left(\frac{\alpha}{\pi}\right)^{1/4}\frac{1}{\sqrt{3}}(\sqrt{\alpha}x)(2\alpha x^2-3)e^{-\alpha x^2/2}$$
> $$\psi_2(x) = \left(\frac{\alpha}{\pi}\right)^{1/4}\frac{1}{\sqrt{2}}(2\alpha x^2-1)e^{-\alpha x^2/2}$$
> $$\psi_1(x) = \left(\frac{\alpha}{\pi}\right)^{1/4}\sqrt{2\alpha}\,x\,e^{-\alpha x^2/2}$$
> $$\psi_0(x) = \left(\frac{\alpha}{\pi}\right)^{1/4}e^{-\alpha x^2/2}$$
>
> where $\alpha^2 = \frac{m\kappa}{\hbar^2}$
>
> Calculate the energy $E$ and the expectation values of $x^2$ and $x$ of $\psi_1$. Later, calculate the standard deviation of the $x$.
>
> - solution: the energy is {@{$E = \frac{3}{2}\hbar\omega$, the $n = 1$ level of $E_n = (n+\frac{1}{2})\hbar\omega$}@}; $\langle x \rangle$ is {@{zero}@} and $\langle x^2 \rangle$ is {@{$\frac{3}{2\alpha} = \frac{3\hbar}{2m\omega}$}@}; the standard deviation is {@{$\Delta x = \sqrt{\langle x^2\rangle - \langle x\rangle^2} = \sqrt{3/(2\alpha)}$}@}
> - explanation: {@{The first excited state}@} carries {@{one quantum, so $n = 1$ in $E_n = (n+\frac{1}{2})\hbar\omega$}@}. $\psi_1$ is {@{odd, so $|\psi_1|^2$ is even and $\langle x\rangle$ vanishes by parity}@}. With {@{$\omega = \sqrt{\kappa/m}$ and $\alpha = m\omega/\hbar$}@}, {@{the virial relation}@} states for {@{forces derived from a potential that is a homogeneous function of degree $n$}@}, i.e. {@{$V(\lambda x) = \lambda^n V(x)$}@}, that {@{$\langle T\rangle = \frac{n}{2}\langle V\rangle$}@}. {@{The harmonic oscillator potential}@} is {@{$V = \frac{1}{2} m \omega^2 x^2$}@}, so {@{$n = 2$ and $\langle T\rangle = \langle V\rangle$}@}. From {@{total energy $E = \langle T\rangle + \langle V\rangle = 2\langle V\rangle$}@} we get {@{$\langle V\rangle = \frac 1 2 m \omega^2 \langle x^2 \rangle = \frac{1}{2}E$}@}, finally yielding {@{$\langle x^2\rangle = E/(m\omega^2) = \frac{3}{2\alpha}$}@}, which direct integration {@{confirms through $\int x^4 e^{-\alpha x^2}dx = 3\sqrt{\pi}/(4\alpha^{5/2})$}@}. With {@{$\langle x\rangle = 0$}@} the standard deviation is {@{just the square root of the variance, $\sqrt{\langle x^2\rangle} = \sqrt{3/(2\alpha)}$}@}.

<!-- markdownlint MD028 -->

> __4.__ (no need to do, but for you to see how the questions be asked in last year) Describe the following experimental techniques (specifying what are used to probe samples, what signals are measured, what properties are obtained, what are the physical processes and equations) of Rutherford Backscattering Spectrometry (RBS), Energy-Dispersive Spectroscopy (SEM-EDS), X-ray Photoelectron Spectroscopy (XPS), Low Energy Electron Diffraction (LEED), X-Ray Diffraction (XRD) and scanning tunnelling microscopy (STM). Input your answers in a table as follow as on your answer book.
>
> - solution: {@{RBS}@} {@{fires ions at a sample, measures the backscattered energy loss, and reads depth and mass from it}@}; {@{SEM-EDS}@} {@{reads characteristic X-ray energies for elemental composition}@}; {@{XPS}@} {@{reads photoelectron energies for binding energies and surface chemistry}@}; {@{LEED}@} {@{reads spot positions for surface periodicity}@}; {@{XRD}@} {@{reads peak angles for plane spacings and lattice parameters}@}; {@{STM}@} {@{reads tunnelling current for surface topography}@}
> - explanation: [Rutherford backscattering spectrometry](../../Rutherford%20backscattering%20spectrometry.md), [energy-dispersive X-ray spectroscopy](../../energy-dispersive%20X-ray%20spectroscopy.md), [X-ray photoelectron spectroscopy](../../X-ray%20photoelectron%20spectroscopy.md), [low-energy electron diffraction](../../low-energy%20electron%20diffraction.md), [X-ray crystallography](../../X-ray%20crystallography.md), and [scanning tunnelling microscopy](../../scanning%20probe%20microscopes.md#scanning%20tunnelling%20microscope) each carry the probe, the measured signal, and the equation that links the two.

<!-- markdownlint MD028 -->

> __5.__ (no need to do, but for you to see how the questions be asked in last year) Describe different processes when X-rays interact with the electrons in an atom, specifying the energy transferring mechanism of each process.
>
> - solution: {@{the photoelectric effect}@} transfers {@{the photon's whole energy to one bound electron, which leaves with the rest}@}; {@{Compton scattering}@} transfers {@{part of the energy to a loosely bound electron and scatters the rest as a longer-wavelength photon}@}; {@{pair production}@} converts {@{the photon near a nucleus into an electron and a positron, possible only above $1.022\ \text{MeV}$}@}; {@{Rayleigh scattering}@} leaves {@{the energy with the photon and changes nothing in the atom}@}
> - explanation: [photoelectric effect](../../photoelectric%20effect.md), [Compton effect](../../Compton%20effect.md), [annihilation](../../annihilation.md) and its [pair production](../../positron.md#pair%20production) partner, and [X-ray](../../X-ray.md) hold the transfer mechanism for each process.
