---
aliases:
  - ELEC 2400 integrator
  - ELEC2400 integrator
  - HKUST ELEC 2400 integrator
  - HKUST ELEC2400 integrator
  - integrator
  - op amp integrator
  - operational amplifier integrator
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/integrator
  - language/in/English
---

# integrator

An integrator adds up its input over time. Hold the input steady and the output ramps at a constant rate; a zero input leaves it where the ramp stopped. A reset switch pulls the output back to zero, so the circuit can be reset.

---

Flashcards for this section are as follows:

- how does an operational amplifier integrator turn an input voltage into a running total? ::@:: The input resistor turns the input voltage into a current, the feedback capacitor gathers that current, and the output is the negative time integral of the input.

## from the inverting amplifier

The [inverting amplifier](inverting%20amplifier.md) has gain $-\frac{R_2}{R_1}$, the feedback impedance over the input impedance. Swap $R_2$ for a capacitor and the gain is $A_{cl} = -\frac{1}{j\omega C_1 R_1}$: infinite at DC, smaller as the frequency rises. Hold the input steady and its gain is unbounded, so the output cannot settle: it ramps.

---

Flashcards for this section are in the following format:

- swapping the feedback resistor: the inverting amplifier's gain $-\frac{R_2}{R_1}$ becomes what when $R_2$ is replaced by a capacitor $C_1$, and how does that show up on the output? ::@:: $A_{cl} = -\frac{1}{j\omega C_1 R_1}$, which grows as the frequency falls and is infinite at DC, so a steady input ramps the output instead of settling at a level.
- why a steady input ramps: reading the gain $-\frac{1}{j\omega C_1 R_1}$, why does a constant input keep driving the output up? ::@:: An input that never changes is pure DC, and the gain there is infinite, so it keeps adding to the output at a fixed rate. That is a ramp.

## the integrator circuit

An operational amplifier becomes an integrator with a resistor $R$ in the input path and a capacitor $C_1$ in the feedback path. The non-inverting terminal goes to ground, so the virtual short holds the inverting terminal at $0\text{ V}$ too. The input voltage then sets the current through the input resistor, $I(t) = \frac{V_{in}(t)}{R}$.

Nothing enters the inverting terminal, so the feedback capacitor has to carry that same current. The capacitor's own relation, $I(t) = C_1\frac{dV_{c1}(t)}{dt}$, links the output to the input. Integrate it from $0$ to $t$ and you get $V_o(t) = -\frac{1}{C_1R}\int_0^t V_{in}(\lambda)\,d\lambda + V_o(0)$, where $V_o(0)$ is the output at $t = 0$. Apart from that constant, the output waveform is the integral of the input waveform.

The reset switch sits in parallel with $C_1$, on a rail of its own above the capacitor. Close it and $C_1$ is shorted: the capacitor discharges through the blade and $V_o$ drops to $0\text{ V}$. Open it again and a fresh integration starts from zero.

Without that switch the constant $V_o(0)$ is inherited rather than chosen. At zero input the output sits at whatever level the last ramp reached. The next run starts from there, already carrying the error of every earlier run. A reset puts the constant back to a known value.

With $R = 12.5\text{ k}\Omega$ and $C_1 = 0.1\ \mu\text{F}$, the time constant is $C_1R = 1.25\text{ ms}$. The output starts at $V_o(0) = 2\text{ V}$. An input of $5\text{ V}$ from $t = 0$ to $t = 1\text{ ms}$, then $0\text{ V}$, gives $V_o(t) = -\frac{1}{1.25\text{ ms}}\int_0^t V_{in}(\lambda)\,d\lambda + 2\text{ V}$. At $t = 1\text{ ms}$ the output reads $V_o = -4 + 2 = -2\text{ V}$. While the input is high, the output ramps linearly from $2\text{ V}$ down to $-2\text{ V}$. Once the input drops to $0\text{ V}$, it flattens out.

![operational amplifier integrator: the input source drives the inverting input through R, the capacitor C 1 returns from the output to that same node while the non-inverting input is grounded, one current I runs through both, and a reset switch sits on its own rail in parallel with C 1](attachments/integrator.svg)

---

Flashcards for this section are in the following format:

- integrator relations: an operational amplifier takes $V_{in}(t)$ through a resistor $R$ into its inverting terminal and returns a capacitor $C_1$ from its output; what is the output $V_o(t)$? ::@:: The inverting terminal holds $0\text{ V}$, so $I(t) = \frac{V_{in}(t)}{R} = C_1\frac{dV_{c1}(t)}{dt}$ and $V_o(t) = -\frac{1}{C_1R}\int_0^t V_{in}(\lambda)\,d\lambda + V_o(0)$: the output waveform is the integral of the input waveform apart from the integration constant.
- integrator example, pulse input: an integrator built from an operational amplifier runs $R = 12.5\text{ k}\Omega$, $C_1 = 0.1\ \mu\text{F}$ and $V_o(0) = 2\text{ V}$, with $V_{in}$ holding $5\text{ V}$ from $t = 0$ to $t = 1\text{ ms}$ then $0\text{ V}$; what is $V_o(1\text{ ms})$, and what shape does $V_o(t)$ take? ::@:: $V_o(t) = -\frac{1}{1.25\text{ ms}}\int_0^t V_{in}(\lambda)\,d\lambda + 2\text{ V}$, so $V_o(1\text{ ms}) = -4 + 2 = -2\text{ V}$: a linear ramp from $2\text{ V}$ down to $-2\text{ V}$ that flattens once the input drops to $0\text{ V}$.
- reset: where does the reset switch of an operational amplifier integrator sit, and what does closing it do to $V_o$? ::@:: In parallel with the feedback capacitor $C_1$, on a rail of its own; closing it shorts $C_1$: the capacitor discharges through the blade and $V_o$ drops to $0\text{ V}$, so the next integration starts from zero.
- why a reset switch is needed: what happens to the integration constant $V_o(0)$ of an operational amplifier integrator that has no reset switch? ::@:: Nothing sets it. At zero input the output sits at the level the last ramp reached, so the next run starts from there already carrying the error of every earlier run. The constant has to be reset to a known value.
- draw an operational amplifier integrator: where do the resistor $R$, the capacitor $C_1$, the reset switch and the non-inverting terminal connect? ::@:: The resistor $R$ sits in the input path, the capacitor $C_1$ in the feedback path, the reset switch in parallel with $C_1$ on a rail above it, and the non-inverting terminal goes to ground, so the virtual short holds the inverting terminal at $0\text{ V}$. <p> ![operational amplifier integrator: the input source drives the inverting input through R, the capacitor C 1 returns from the output to that same node while the non-inverting input is grounded, one current I runs through both, and a reset switch sits on its own rail in parallel with C 1](attachments/integrator.svg)
- why one current: an integrator puts $R$ in the input path and $C_1$ in the feedback path of an operational amplifier; why does the same $I(t)$ run through both? ::@:: Nothing enters the inverting terminal, so the current the input resistor delivers has nowhere to go but through the feedback capacitor.
