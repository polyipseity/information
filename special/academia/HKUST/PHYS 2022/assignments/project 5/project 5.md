---
aliases:
  - HKUST PHYS 2022 project 5 notes
  - HKUST PHYS2022 project 5 notes
  - PHYS 2022 project 5 notes
  - PHYS2022 project 5 notes
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/assignments/project_5/project_5
  - language/in/English
---

# project 5

- HKUST PHYS 2022 project 5
- parent: [project 5](index.md)

Project 5 puts one particle into one square potential well and reads its energy levels. The simulated well has a tall but finite barrier, so its levels are measured at five widths and then compared with the levels of an ideal well whose walls are infinitely high. The comparison is the point of the project: the gap between the two is what a finite barrier does that an infinite one cannot. The full treatments live in [particle in a box](../../particle%20in%20a%20box.md) and [finite potential well](../../finite%20potential%20well.md).

---

Flashcards for this section are as follows:

- overview: what project 5 measures and compares ::@:: The energy levels of a finite square well at five widths, against the levels an infinite square well of the same widths would hold. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the difference the project turns on ::@:: A finite barrier binds the particle more weakly than infinite walls of the same width, and that shortfall is what the comparison exposes. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## energy levels against width

A single square well sits at the tallest barrier the simulation offers, and its width is swept through $0.10$, $0.20$, $0.30$, $0.40$, and $0.50\ \text{nm}$. At each width every bound level is recorded, and the lowest level $E_1$ is plotted against the width.

The ideal reference is the infinite square well, whose levels are $E_n = n^2h^2/(8mL^2)$ at width $L$: the ground state falls as $1/L^2$, so narrowing the well from $0.50$ to $0.10\ \text{nm}$, a factor of five, raises $E_1$ twenty-five-fold. The measured levels fall with width in the same spirit, and the plotted curve is read for the formula that binds them.

---

Flashcards for this section are as follows:

- overview: the sweep project 5 records, widths $L$ from $0.10$ to $0.50\ \text{nm}$ ::@:: One square well at the tallest barrier, widths from $0.10$ to $0.50\ \text{nm}$, every bound level recorded and $E_1$ plotted against the width. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the levels of an infinite square well of width $L$ ::@:: $E_n = n^2h^2/(8mL^2)$, so the ground state falls as $1/L^2$ when the well widens. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- narrowing an infinite square well from $0.50$ to $0.10\ \text{nm}$: what happens to its ground-state energy ::@:: It rises twenty-five-fold, since $E_1 \propto 1/L^2$ and the width shrank by a factor of five. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## finite barrier against infinite walls

Solving the same five widths with infinite walls gives levels that sit above the simulated ones at every width. The reason is the barrier's finiteness: the wave function does not stop at the wall but decays into the barrier over a penetration depth $\delta = \hbar/\sqrt{2m(V_0 - E)}$, so the particle is effectively confined across a box wider than $L$ and its energy drops below the infinite-well value.

A finite well also binds only finitely many levels, because every bound level must lie below the barrier height $V_0$, while the infinite well's ladder $E_n = n^2h^2/(8mL^2)$ climbs without ceiling. The shortfall against the infinite-well value grows as the well narrows: the penetration depth $\delta$ is set by the barrier, not the width, so it claims a larger share of a narrow well than a wide one.

---

Flashcards for this section are as follows:

- overview: how the finite well's levels $E_n$ stand against the infinite well's at the same width $L$ ::@:: Lower at every width, because the wave function leaks into the barrier over a penetration depth $\delta$ and the particle is effectively confined across a box wider than $L$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the penetration depth of a particle of energy $E$ into a barrier of height $V_0$ ::@:: $\delta = \hbar/\sqrt{2m(V_0 - E)}$: the distance over which the wave function decays outside the well. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- why a finite well supports only finitely many bound levels $E_n$ ::@:: Every bound level lies below the barrier height $V_0$, while the infinite well's levels $n^2h^2/(8mL^2)$ climb without ceiling. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- as a finite well of width $L$ narrows: how its levels shift against the infinite-well values ::@:: The fractional shortfall grows, since the penetration depth $\delta$ is fixed by the barrier and claims a larger share of a narrower well. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
