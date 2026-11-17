---
aliases:
  - HKUST PHYS 2022 project 1 notes
  - HKUST PHYS2022 project 1 notes
  - PHYS 2022 project 1 notes
  - PHYS2022 project 1 notes
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/assignments/project_1/project_1
  - language/in/English
---

# project 1

- HKUST PHYS 2022 project 1
- parent: [project 1](index.md)

Project 1 offers two experiments, either of which suffices: a project carrying more than one simulation may choose freely. The double-slit pattern that light makes through two narrow openings is one; the relation between a gas's pressure, its temperature, and how its molecules move is the other. Each experiment sweeps one parameter across five values, plots the measured quantity against the swept one, and reads a formula off the plot. The full treatments live in [light](../../light.md) and [kinetic theory of gases](../../kinetic%20theory%20of%20gases.md).

---

Flashcards for this section are as follows:

- overview: the two experiments project 1 offers, and how many need doing ::@:: The double-slit interference pattern of light, and the relation between a gas's pressure, temperature, and molecular motion; one of the two suffices.
- the method each experiment of project 1 follows ::@:: Sweep one parameter across five values, plot the measured quantity against it, and read a formula off the plot.

## double slit

Light falls through two slits of width $a$ separated by a distance $d$ onto a distant screen, and bright bands appear at definite angles. Varying the slit separation, the slit width, or the wavelength moves those bands, and the first bright band is the one whose angle is measured.

Bright bands sit where the waves from the two slits arrive in step, at angles $\theta$ with $d\sin\theta = m\lambda$ for integer $m$; the first band is $m = 1$, so $\sin\theta_1 = \lambda/d$. The angle therefore shrinks as the separation grows and opens as the wavelength grows. Each slit of width $a$ also casts a single-slit envelope over the whole pattern, with its first dark minimum at $a\sin\theta = \lambda$. The envelope decides how bright each band is, and a narrower slit spreads it wider.

---

Flashcards for this section are as follows:

- the bright bands of a double-slit pattern of separation $d$ and light of wavelength $\lambda$: what decides where they sit ::@:: The slit separation $d$ and the wavelength $\lambda$, through $d\sin\theta = m\lambda$; the first bright band is $m = 1$.
- the bright-band condition for two slits separated by $d$ and light of wavelength $\lambda$ ::@:: $d\sin\theta = m\lambda$ for integer $m$.
- the position of the first bright band, in terms of the separation $d$ and the wavelength $\lambda$ ::@:: $\sin\theta_1 = \lambda/d$: the angle shrinks as the separation $d$ grows and opens as the wavelength $\lambda$ grows.
- increasing the slit separation $d$ at fixed wavelength $\lambda$: what happens to the first bright band's angle $\theta_1$ ::@:: It shrinks, since $\sin\theta_1 = \lambda/d$ falls as $d$ grows.
- increasing the wavelength $\lambda$ at fixed separation $d$: what happens to the first bright band's angle $\theta_1$ ::@:: It opens, since $\sin\theta_1 = \lambda/d$ grows with $\lambda$.
- the single-slit envelope cast by slits of width $a$: where its first dark minimum lies ::@:: At $a\sin\theta = \lambda$, so a narrower slit pushes the minimum out and spreads the envelope wider.
- changing the slit width $a$ while the separation $d$ stays fixed: which feature of the pattern moves ::@:: The envelope only; the interference bands stay at $d\sin\theta = m\lambda$ while the envelope's first minimum stays at $a\sin\theta = \lambda$.

## gas properties

A fixed volume holds $N$ particles of mass $m$ at temperature $T$. The kinetic theory of gases ties the pressure these particles exert and their average speed to those three quantities, and the experiment sweeps $N$ and $T$ for heavy particles and again for light ones.

The pressure follows $PV = Nk_BT$: at fixed volume it is proportional to the particle number and to the temperature, with no dependence on the particle mass once $N$ and $T$ are fixed. The average molecular speed is $v_{\text{rms}} = \sqrt{3k_BT/m}$: it grows with the square root of the temperature, ignores the particle number entirely, and falls with the square root of the mass. Heavy and light particles at the same $N$ and $T$ press on the walls equally, while the light ones move faster.

---

Flashcards for this section are as follows:

- overview: what the gas experiment sweeps and measures ::@:: Particle number and temperature across five values each, for heavy and light particles, measuring pressure and average speed.
- the pressure of $N$ particles of mass $m$ in volume $V$ at temperature $T$ ::@:: $P = Nk_BT/V$: proportional to $N$ and to $T$, independent of the particle mass $m$ at fixed $N$ and $T$.
- the average molecular speed $v_{\text{rms}}$ in terms of temperature $T$ and particle mass $m$ ::@:: $v_{\text{rms}} = \sqrt{3k_BT/m}$: it grows as $\sqrt{T}$, is independent of the particle number $N$, and falls as $1/\sqrt{m}$.
- heavy and light particles at the same particle number $N$ and temperature $T$: how their pressures and average speeds compare ::@:: Equal pressures, since pressure depends only on $N$ and $T$; the light particles have the higher average speed, since $v_{\text{rms}} \propto 1/\sqrt{m}$.
