---
aliases:
  - HKUST PHYS 2022 project 10 notes
  - HKUST PHYS2022 project 10 notes
  - PHYS 2022 project 10 notes
  - PHYS2022 project 10 notes
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/assignments/project_10/project_10
  - language/in/English
---

# project 10

- HKUST PHYS 2022 project 10
- parent: [project 10](index.md)

Project 10 reads half-lives off decay curves. Tritium and carbon-14 decay by beta decay, polonium-211 and a tunable custom nucleus by alpha decay, and the alpha-decay half-life is then traced back to the energy the escaping particle carries. One of the two simulations is enough: a project carrying more than one may choose freely.

---

Flashcards for this section are as follows:

- which nuclei project 10 measures, and the decay type of each ::@:: Tritium and carbon-14 by beta decay, polonium-211 and a custom nucleus by alpha decay.
- the two quantities project 10 extracts from each decay measurement ::@:: The half-life, read from the decay curve, and for alpha decay its dependence on the total energy.
- how many of project 10's two simulations need to be done ::@:: One: a project carrying more than one simulation may choose between them freely.

## the decay curve and the half-life

A radioactive sample thins out exponentially because each nucleus decays at a rate set only by itself: $\mathrm{d}N/\mathrm{d}t = -\lambda N$ integrates to $N(t) = N_0 e^{-\lambda t}$. Each nucleus draws its waiting time from one probability distribution, the exponential density $p(t) = \lambda e^{-\lambda t}$: the shortest waits are the most likely, the mode sitting at $t = 0$, while the mean sits at $\tau = \int_0^\infty t\,\lambda e^{-\lambda t}\,\mathrm{d}t = 1/\lambda$. The slow decayers in the tail drag that mean to $1/\ln 2 \approx 1.44$ times the half-life. The decayed fraction $1 - e^{-\lambda t}$ is that distribution's cumulative probability, counted over $N_0$ nuclei. The half-life follows by asking when the intact fraction reaches one half: $e^{-\lambda T_{1/2}} = 1/2$ gives $T_{1/2} = \ln 2/\lambda$. The rate depends only on what remains, not on how long it has survived, so the sample holds no memory and every fresh half takes the same $T_{1/2}$.

The two modes of the measurement trade smoothness against detail. One nucleus watched alone shows a single draw from $p(t)$: a scatter of waiting times whose running average creeps towards $\tau = 1/\lambda$. Many nuclei watched together average many draws at once, and the decayed count concentrates around its expectation $N_0(1 - e^{-\lambda t})$; the half-life is read where that curve reaches one half.

The textbook half-lives differ widely: $12.3$ years for tritium, $5730$ years for carbon-14, and about $0.52$ seconds for polonium-211, more than eleven orders of magnitude apart.

---

Flashcards for this section are as follows:

- the fraction of a radioactive sample decayed at time $t$, with decay constant $\lambda$ ::@:: $1 - e^{-\lambda t}$, the waiting-time distribution's cumulative probability counted over $N_0$ nuclei; the intact fraction is $e^{-\lambda t}$.
- the probability distribution $p(t)$ a nucleus's waiting time follows ::@:: The exponential density $p(t) = \lambda e^{-\lambda t}$: the mode sits at $t = 0$, the shortest waits are the most likely, and the mean sits at $\tau = 1/\lambda$.
- the half-life $T_{1/2}$ of a sample with decay constant $\lambda$ ::@:: $T_{1/2} = \ln 2/\lambda$, the time in which half the nuclei decay.
- how $T_{1/2} = \ln 2/\lambda$ follows from $N(t) = N_0 e^{-\lambda t}$ ::@:: Ask when the intact fraction reaches one half: $e^{-\lambda T_{1/2}} = 1/2$, so $T_{1/2} = \ln 2/\lambda$.
- what makes every successive half-life $T_{1/2}$ of a sample equal ::@:: The decay rate depends only on what remains, not on how long it survived: the sample holds no memory, so each fresh half takes the same $T_{1/2}$.
- the mean lifetime $\tau$ of the single-atom waiting times, and its size against $T_{1/2}$ ::@:: $\tau = \int_0^\infty t\,\lambda e^{-\lambda t}\,\mathrm{d}t = 1/\lambda$, longer than $T_{1/2} = \ln 2/\lambda$ by $1/\ln 2 \approx 1.44$, the slow decayers in the tail dragging the mean out.
- what a single-atom decay run and a multiple-atom decay run hand over, at decay constant $\lambda$ ::@:: The single-atom mode shows one draw at a time from $p(t) = \lambda e^{-\lambda t}$, a scatter whose running average approaches $\tau = 1/\lambda$; the many-atom mode averages many draws, and the decayed count concentrates around $N_0(1 - e^{-\lambda t})$.
- the textbook half-lives $T_{1/2}$ of tritium, carbon-14, and polonium-211 ::@:: $12.3$ years for tritium, $5730$ years for carbon-14, and about $0.52$ seconds for polonium-211.

## half-life against decay energy

An alpha particle escaping a nucleus faces a Coulomb barrier far above its own energy, so it leaves only by [tunnelling](../../quantum%20tunnelling.md#alpha%20decay). The barrier's outer edge is the classical turning point $r_2$, where the Coulomb energy equals the particle's total energy; a higher total energy pulls $r_2$ inward and shortens the region the wave must cross. The tunnelling probability rises steeply, and the decay rate with it.

The rate factorises as $\lambda = fP$: $f$ is how often the alpha strikes the barrier from inside, and $P$ the probability of getting through. $P$ is an exponential in the barrier, $P = e^{-2\gamma}$ with $\gamma = \int_{r_1}^{r_2} \kappa(r)\,\mathrm{d}r$ and $\kappa(r) = \sqrt{2m(V(r)-E)}/\hbar$ the local decay constant, integrated between the inner turning point $r_1$ and the outer one $r_2$. The half-life inherits that exponential: $T_{1/2} = \ln 2/\lambda = (\ln 2/f)\,e^{2\gamma}$.

For the Coulomb barrier $V(r) = k/r$ with $k = Z_1Z_2e^2/(4\pi\varepsilon_0)$, $Z_1$ and $Z_2$ the charges of the alpha and the daughter nucleus, every step is visible. The outer turning point $r_2$ is where the barrier falls to the particle's energy, so $k/r_2 = E$ and $r_2 = k/E$. Outside that radius the particle is classically allowed and inside it the barrier stands above $E$. Substituting $V$ and pulling out $E$ turns the exponent's integrand into $\kappa(r) = \sqrt{2mE}/\hbar\cdot\sqrt{r_2/r - 1}$, since $k/r - E = E(r_2/r - 1)$. The pure Coulomb form has no inner turning point, so the lower limit runs to the origin, and writing $r = r_2 t$ turns the integral into a pure number: $\gamma = \sqrt{2mE}\,r_2/\hbar\cdot\int_0^1\sqrt{1/t - 1}\,\mathrm{d}t$, and that integral is $\pi/2$. So $\gamma = \pi\sqrt{2mE}\,r_2/(2\hbar) = \pi k\sqrt{2m}/(2\hbar\sqrt{E})$: the root's argument was reduced to $r_2/r - 1$ and $r_2 = k/E$ carries the whole energy and charge dependence, which is why $\gamma \propto Z_1Z_2/\sqrt{E}$.

The half-life inherits that dependence through $T_{1/2} = (\ln 2/f)e^{2\gamma}$. Taking logarithms, $\ln T_{1/2} = \ln(\ln 2/f) + 2\gamma$, and the first term is a fixed offset that barely moves as $E$ sweeps while $2\gamma$ runs in the tens, so the slope carries the physics. Putting the result in, $\ln T_{1/2} = \ln(\ln 2/f) + \pi k\sqrt{2m}/(\hbar\sqrt{E})$, and a plot of $\ln T_{1/2}$ against $1/\sqrt{E}$ is straight, with slope $\pi k\sqrt{2m}/\hbar$ proportional to $Z_1Z_2$. Sweeping the total energy until the half-life runs from one second to a billion years traces this Gamow relation between half-life and tunnelling probability.

---

Flashcards for this section are as follows:

- the barrier an alpha particle faces when leaving a nucleus, and how it crosses ::@:: A Coulomb barrier far above the alpha's energy; it crosses by tunnelling, through a forbidden region that narrows as the decay energy rises.
- how the alpha-decay half-life moves as the decay energy rises ::@:: It collapses exponentially: more energy means a narrower barrier, a higher tunnelling probability, and a shorter life.
- where the alpha barrier's outer turning point $r_2$ sits, and what raising the total energy does to it ::@:: At the classical turning point $r_2$, where the Coulomb energy equals the total energy; more energy pulls it inward, shortens the forbidden region, and raises the tunnelling probability.
- the factorisation $\lambda = fP$ of the alpha decay rate in the Gamow picture ::@:: $f$ is how often the alpha strikes the barrier from inside, $P$ the probability of getting through, so $T_{1/2} = \ln 2/(fP)$.
- the tunnelling probability $P$ through the barrier in the Wentzel–Kramers–Brillouin (WKB) form ::@:: $P = e^{-2\gamma}$ with $\gamma = \int_{r_1}^{r_2} \kappa(r)\,\mathrm{d}r$ and $\kappa(r) = \sqrt{2m(V(r)-E)}/\hbar$, integrated between the turning points $r_1$ and $r_2$.
- how $\gamma$ scales with the decay energy $E$ for the Coulomb barrier $V(r) = Z_1Z_2e^2/(4\pi\varepsilon_0 r)$ ::@:: As $Z_1Z_2/\sqrt{E}$: with $k = Z_1Z_2e^2/(4\pi\varepsilon_0)$, $\gamma = \pi k\sqrt{2m}/(2\hbar\sqrt{E})$, so $\ln T_{1/2}$ grows like $Z_1Z_2/\sqrt{E}$ and a plot of $\ln T_{1/2}$ against $1/\sqrt{E}$ is straight.
- where the Coulomb barrier's outer turning point $r_2$ sits, in terms of the strength $k = Z_1Z_2e^2/(4\pi\varepsilon_0)$ and the energy $E$ ::@:: At $r_2 = k/E$: the barrier height $k/r_2$ equals the particle's energy there, allowed outside and forbidden inside.
- the exponent's integrand $\kappa(r)$ at the Coulomb barrier $V(r) = k/r$, in terms of $r_2 = k/E$ ::@:: $\kappa(r) = \sqrt{2mE}/\hbar\cdot\sqrt{r_2/r - 1}$: $k/r - E = E(r_2/r - 1)$ factors the energy out of the root.
- the number the exponent's integral $\int_0^1\sqrt{1/t - 1}\,\mathrm{d}t$ comes to, after the substitution $r = r_2 t$ ::@:: $\pi/2$, so $\gamma = \pi\sqrt{2mE}\,r_2/(2\hbar)$ at the Coulomb barrier.
- the logarithm of the Coulomb-tunnelling half-life, $\ln T_{1/2}$, in terms of $\gamma$ and the attempt rate $f$ ::@:: $\ln T_{1/2} = \ln(\ln 2/f) + 2\gamma$: the first term is a fixed offset, so the slope of $\ln T_{1/2}$ against $1/\sqrt{E}$ is $\pi k\sqrt{2m}/\hbar$, proportional to $Z_1Z_2$.
- why the alpha half-life spans decades over a small stretch of energy ::@:: The tunnelling probability enters the decay rate through an exponential exponent, so the half-life, its inverse, moves by decades: the Gamow relation between half-life and tunnelling probability.
- what plotting the half-life against the total energy, swept until the half-life runs from one second to a billion years, traces ::@:: The exponential law of alpha decay, the Gamow relation between half-life and tunnelling probability.
