---
aliases:
  - HKUST PHYS 2022 project 3 notes
  - HKUST PHYS2022 project 3 notes
  - PHYS 2022 project 3 notes
  - PHYS2022 project 3 notes
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/assignments/project_3/project_3
  - language/in/English
---

# project 3

- HKUST PHYS 2022 project 3
- parent: [project 3](index.md)

Project 3 follows alpha particles scattered by a single atomic nucleus. Two quantities control every trajectory: the impact parameter $b$, the distance by which the alpha would miss the nucleus, and the scattering angle $\theta$ it leaves with. Both are read off the traced trajectories, and the Rutherford relation between them turns each set of readings into a measurement of the alpha particle's kinetic energy. The full treatment lives in [Rutherford scattering experiments](../../Rutherford%20scattering%20experiments.md).

---

Flashcards for this section are as follows:

- overview: what project 3 measures on each scattered alpha trajectory, the impact parameter $b$ and the scattering angle $\theta$ ::@:: The impact parameter $b$ and the scattering angle $\theta$, read off the traced path around a single nucleus.
- the two quantities $b$ and $\theta$ that control an alpha particle's trajectory past a nucleus ::@:: The impact parameter $b$, the miss distance, and the scattering angle $\theta$.

## impact parameter and scattering angle

Ten trajectories are traced at the largest available beam energy. The Rutherford relation $b = \frac{Z_1Z_2e^2}{8\pi\varepsilon_0 K}\cot\frac{\theta}{2}$, with $K = mv_0^2/2$ the alpha particle's kinetic energy, $Z_1$ its atomic number, and $Z_2$ the target's, makes $b$ against $\cot(\theta/2)$ a straight line through the origin. Its slope $Z_1Z_2e^2/(8\pi\varepsilon_0 K)$ carries the wanted energy: solve the slope for $K$ and the beam energy falls out. Small impact parameters scatter to large angles, and a head-on hit, $b = 0$, scatters straight back.

---

Flashcards for this section are as follows:

- overview: the impact-parameter relation $b$ against $\cot(\theta/2)$ that project 3 turns into a straight-line plot ::@:: $b = \frac{Z_1Z_2e^2}{8\pi\varepsilon_0 K}\cot\frac{\theta}{2}$ with $K = mv_0^2/2$, which makes $b$ against $\cot(\theta/2)$ a line through the origin.
- the Rutherford impact-parameter relation, naming $b$, $Z_1$, $Z_2$, $K$, and $\theta$ ::@:: $b = \frac{Z_1Z_2e^2}{8\pi\varepsilon_0 K}\cot\frac{\theta}{2}$ with $K = mv_0^2/2$: the impact parameter falls as the scattering angle opens.
- a plot of $b$ against $\cot(\theta/2)$ at fixed $Z_1$, $Z_2$, and $K$: what its slope gives ::@:: The slope is $Z_1Z_2e^2/(8\pi\varepsilon_0 K)$, which solved for $K$ returns the alpha particle's kinetic energy.
- the trajectory with the largest scattering angle $\theta$: which impact parameter $b$ produces it ::@:: $b = 0$: a head-on hit scatters straight back, and $\cot(\theta/2)$ falls to zero as $\theta$ reaches $180°$.

## atomic number dependence

The target's proton number is then swept across five values from $Z_2 = 20$ to $Z_2 = 100$, one traced trajectory at each. Every $Z_2$ gives its own straight $b$ against $\cot(\theta/2)$ line, steeper for the lighter targets, and plotting $Z_2$ against $b/\cot(\theta/2)$ gathers them into one line through the origin whose slope $Z_1e^2/(8\pi\varepsilon_0 K)$ again returns $K$.

Both routes return the same energy because the relation is exactly linear in $Z_2$ and exactly inverse in $K$: the two plots constrain the same two constants from different directions. At fixed $b$ and $K$ a larger $Z_2$ bends the trajectory harder, since holding $b$ fixed while $Z_2$ grows means $\cot(\theta/2)$ must fall and $\theta$ open.

---

Flashcards for this section are as follows:

- overview: the second route to the beam energy, sweeping $Z_2$ and plotting it against $b/\cot(\theta/2)$ ::@:: Sweeping the target's proton number $Z_2$ and plotting $Z_2$ against $b/\cot(\theta/2)$, a line through the origin whose slope $Z_1e^2/(8\pi\varepsilon_0 K)$ again returns $K$.
- a plot of $Z_2$ against $b/\cot(\theta/2)$: what its slope gives and why it passes through the origin ::@:: The slope is $Z_1e^2/(8\pi\varepsilon_0 K)$, returning $K$; it passes through the origin because $b \propto Z_2$ at fixed $\theta$ and $K$.
- why the two plots return the same kinetic energy $K$ ::@:: The Rutherford relation is exactly linear in $Z_2$ and exactly inverse in $K$, so each plot constrains the same constants from a different direction.
- at fixed impact parameter $b$ and energy $K$, raising the target's proton number $Z_2$: what happens to the scattering angle ::@:: It opens, since $b \propto Z_2\cot(\theta/2)$ holds the product fixed and $\cot(\theta/2)$ must fall.
