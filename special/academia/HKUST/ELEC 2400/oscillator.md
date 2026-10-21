---
aliases:
  - ELEC 2400 oscillator
  - ELEC2400 oscillator
  - HKUST ELEC 2400 oscillator
  - HKUST ELEC2400 oscillator
  - electronic oscillator
  - oscillator
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/oscillator
  - language/in/English
---

# oscillator

An oscillator makes its own periodic signal from the DC supply, where an amplifier only follows an input. This one wires two [integrators](integrator.md) and an inverting amplifier into a loop, and the $R$'s and $C$'s set the frequency it oscillates at.

---

Flashcards for this section are as follows:

- how does an oscillator differ from an amplifier, and what equation do the integrator outputs $V_A$, $V_B$ and $V_C$ obey when $\omega_o^2 = \frac{1}{C_1R_1C_2R_2}$? ::@:: An oscillator produces a periodic signal from the supply alone. Two integrators closed through an inverting amplifier give $\frac{d^2V_B(t)}{dt^2} + \omega_o^2 V_B(t) = 0$, whose solution $V_B(t) = \alpha\cos(\omega_o t + \beta)$ is a sinusoid.

## double-integrator oscillator

The oscillator has three stages. Each one fixes a relation. The first is an inverting integrator: it turns $V_C(t)$ into $V_A(t) = -\frac{1}{R_1C_1}\int V_C(t)\,dt$, so $\frac{dV_A}{dt} = -\frac{V_C}{R_1C_1}$. The second integrates $V_A$ the same way: $V_B(t) = -\frac{1}{R_2C_2}\int V_A(t)\,dt$, so $\frac{dV_B}{dt} = -\frac{V_A}{R_2C_2}$.

The inverting amplifier closes the ring. Its input resistor and its feedback resistor both have value $R$, so the gain is $-\frac{R}{R} = -1$ and $V_C(t) = -V_B(t)$. The ring hands back what it got, sign flipped.

The loop closes on itself, so the three relations have to collapse into one. Differentiate $V_C = -V_B$ to get $\frac{dV_C}{dt} = -\frac{dV_B}{dt}$. The first stage then gives $\frac{dV_A}{dt} = \frac{V_B}{R_1C_1}$. Differentiate the second stage instead and $\frac{dV_A}{dt} = -R_2C_2\frac{d^2V_B}{dt^2}$. The two expressions for $\frac{dV_A}{dt}$ are the same quantity, so $-R_2C_2\frac{d^2V_B}{dt^2} = \frac{V_B}{R_1C_1}$. Move the terms to one side and $\frac{d^2V_B(t)}{dt^2} + \frac{1}{R_1R_2C_1C_2}V_B(t) = 0$.

The coefficient is the square of the natural frequency, so $\omega_o = \frac{1}{\sqrt{R_1R_2C_1C_2}}$. The two $R$'s and two $C$'s set it between them; no matching is needed.

Matching the two time constants is a design choice, not a condition. Set $C_1R_1 = C_2R_2 = \tau$ and the product becomes $\tau^2$, so $\omega_o = \frac{1}{\tau}$. One $RC$ then sets the frequency; that is what the matching buys. Either way the solution keeps the same form, $V_B(t) = \alpha\cos(\omega_o t + \beta)$, an undamped sinusoid. Whatever starts the loop fixes its amplitude $\alpha$ and its phase $\beta$.

![double-integrator oscillator: three blocks in a ring, the voltage V C entering the first integrator, its output V A entering the second, that output V B entering the inverting amplifier, and the amplifier's output V C returning to the first integrator](attachments/oscillator_loop.svg)

No input is needed. Noise usually starts the circuit, and the loop keeps it running. Evaluate the loop at a sinusoid. Each integrator multiplies by $-\frac{1}{j\omega RC}$, so the pair gives $-\frac{1}{\omega^2R_1C_1R_2C_2}$. The inverter's $-1$ flips the sign to $+\frac{1}{\omega^2R_1R_2C_1C_2}$. At $\omega_o$ that equals $1$: positive feedback that reproduces whatever the loop started with. The same sign builds the comparator family, from the [Schmitt trigger](Schmitt%20trigger.md) to the square waveform generator.

---

Flashcards for this section are in the following format:

- the three blocks: what relation does each stage impose on $V_A$, $V_B$ and $V_C$? ::@:: Integrator 1 gives $\frac{dV_A}{dt} = -\frac{V_C}{R_1C_1}$, integrator 2 gives $\frac{dV_B}{dt} = -\frac{V_A}{R_2C_2}$, and the inverting amplifier gives $V_C(t) = -V_B(t)$.
- the inverting amplifier's two resistors: why does the ring close with $V_C(t) = -V_B(t)$ and not with some other multiple of $V_B$? ::@:: Its input resistor and its feedback resistor both carry $R$, so its gain is $-\frac{R}{R} = -1$: the ring returns the same size it received, sign flipped.
- substituting through the loop: how do those three relations collapse into one equation for $V_B$? ::@:: $V_C = -V_B$ gives $\frac{dV_A}{dt} = \frac{V_B}{R_1C_1}$, while the second stage gives $\frac{dV_A}{dt} = -R_2C_2\frac{d^2V_B}{dt^2}$, so $\frac{d^2V_B(t)}{dt^2} + \frac{1}{R_1R_2C_1C_2}V_B(t) = 0$.
- natural frequency without matching the time constants: what $\omega_o$ does the coefficient of $V_B$ give? ::@:: $\omega_o = \frac{1}{\sqrt{R_1R_2C_1C_2}}$, so the two $R$'s and two $C$'s set it between them and nothing has to be matched.
- equal time constants: what does $C_1R_1 = C_2R_2 = \tau$ simplify $\omega_o$ to, and what is it for? ::@:: $\omega_o = \frac{1}{\tau}$: one $RC$ sets the frequency. It is a design choice, not a condition for oscillating.
- the oscillator's solution: what form does $V_B(t)$ take, and where do the two constants come from? ::@:: $V_B(t) = \alpha\cos(\omega_o t + \beta)$, an undamped sinusoid whose amplitude and phase are fixed by whatever starts the loop, such as noise.
- draw the double-integrator oscillator as three boxes: which of $V_C$, $V_A$ and $V_B$ labels each arrow, and how does the last box close the ring? ::@:: Integrator 1, integrator 2 and the inverting amplifier, in a row. $V_C$ enters the first and $V_A$ comes out. The second turns $V_A$ into $V_B$, which feeds the amplifier, and the amplifier hands back $V_C$ along the bottom into the first box. Nothing enters from outside. <p> ![double-integrator oscillator: three blocks in a ring, the voltage V C entering the first integrator, its output V A entering the second, that output V B entering the inverting amplifier, and the amplifier's output V C returning to the first integrator](attachments/oscillator_loop.svg)
- self-oscillation: why does the double-integrator oscillator need no input signal, and what is its loop gain at $\omega_o$? ::@:: Each integrator multiplies a sinusoid by $-\frac{1}{j\omega RC}$ and the inverter by $-1$, leaving $+\frac{1}{\omega^2R_1R_2C_1C_2}$. At $\omega_o$ that is $1$: positive feedback of unity gain, so noise alone keeps it running.
