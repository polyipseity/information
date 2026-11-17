---
aliases:
  - ELEC 2400 superposition principle
  - ELEC2400 superposition principle
  - HKUST ELEC 2400 superposition principle
  - HKUST ELEC2400 superposition principle
  - principle of superposition
  - superposition
  - superposition principle
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/superposition_principle
  - language/in/English
---

# superposition principle

The superposition principle splits a circuit with several sources into several circuits of one source each. Each source acts alone while the others are set to zero, and their sum is the response of the whole circuit.

The principle holds exactly for circuits of linear elements, so it applies to resistive networks with independent and dependent sources. It does not extend to power, which is quadratic in current and voltage.

---

Flashcards for this section are as follows:

- superposition principle: what do the several one-source circuits contribute to the output of the whole circuit? ::@:: Each independent source acting alone produces one response, and the output of the whole circuit is the sum of those responses, because every element is linear.

## linearity

A circuit can be treated as a function with an input and an output: the excitation in, the response out. Homogeneity is $f(kx) = kf(x)$ for every $k$, and the only function meeting it is the straight line through the origin, $f(x) = mx$.

Superposition is $f(x_1 + x_2) = f(x_1) + f(x_2)$. A circuit is linear when both hold at once, in the combined form $f(a x_1 + b x_2) = a f(x_1) + b f(x_2)$. That combined form is the one used when contributions are scaled and added.

Elements whose current is not a straight line in their voltage sit outside both properties. The diode is the usual example in circuit analysis.

---

Flashcards for this section are as follows:

- linearity: what single statement combines homogeneity and superposition for a circuit with two excitations? ::@:: A circuit is linear when it satisfies both homogeneity, $f(kx) = kf(x)$, and superposition, $f(x_1 + x_2) = f(x_1) + f(x_2)$, equivalently $f(a x_1 + b x_2) = a f(x_1) + b f(x_2)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- excitation and response: what are the input and the output of a circuit called when it is viewed as a function? ::@:: The input is the excitation and the output is the response.
- homogeneity: which form must the function $f$ of a homogeneous circuit take? ::@:: A straight line through the origin, $f(x) = mx$; no other function satisfies $f(kx) = kf(x)$.
- superposition property: state the property of $f$ that lets responses be added. ::@:: $f(x_1 + x_2) = f(x_1) + f(x_2)$: the response to a sum of excitations is the sum of the individual responses.
- the two properties: which two properties of $f$ together make a circuit linear? ::@:: Homogeneity and superposition, combining into $f(a x_1 + b x_2) = a f(x_1) + b f(x_2)$.
- non-linear element: which familiar element fails homogeneity and superposition, and why? ::@:: The diode, whose current is not a straight-line function of its voltage, so neither property holds in a circuit containing one.

## applying superposition

Each independent source is taken alone, with every other one set to zero: a voltage source becomes a short, because $V_{si} = 0\text{ V}$, and a current source becomes an open, because $I_{sj} = 0\text{ A}$.

The [dependent sources](dependent%20source.md) are not set to zero. They stay operative in each single-source circuit, with their controlling quantity recomputed there, so a circuit holding one gets solved afresh for every contribution.

In a worked resistive circuit a $6\text{ V}$ source gives $V_A = 0.5 V_s$ and $V_B = 0.25 V_s$, so $(V_A, V_B)$ is $(3\text{ V}, 1.5\text{ V})$ at $V_s = 6\text{ V}$ and $(6\text{ V}, 3\text{ V})$ at $V_s = 12\text{ V}$. The node voltages are proportional to the source, which is homogeneity at work.

Circuit lines in these notes follow one notation. `(X)` names a node, with `(GND)` the zero-volt ground node, and `[...]` holds one element, its value and marks spelled out in words. The dash `—` is a wire joining consecutive items, and `A ∥ B` puts two elements in parallel between the same pair of nodes. So the line `(A) — [2 Ω] — (B)` reads node $A$ feeding a $2\ \Omega$ resistor that reaches node $B$.

A branch can also escape one contribution altogether. The circuit is drawn `[6 V source, + up] — [2 Ω carrying I₁] — (Va) — [2 Ω] — (GND)` and `(Va) — [2 A source, up] — (X) — [2 Ω ∥ 4 V source] — (GND)`, holding a $6\text{ V}$ source, a $2\ \Omega$ resistor carrying $I_1$, a $2\ \Omega$ resistor to ground, a $2\text{ A}$ source, a further $2\ \Omega$ resistor, and a $4\text{ V}$ source. The $4\text{ V}$ source in parallel with its $2\ \Omega$ resistor sits in series with the $2\text{ A}$ source, so the combination plays no part in $I_1$. The contributions are $I_1|_{6\text{V}} = \frac{6\text{ V}}{2\ \Omega + 2\ \Omega} = 1.5\text{ A}$ and $I_1|_{2\text{A}} = \frac{2\ \Omega}{2\ \Omega + 2\ \Omega} \times 2\text{ A} = 1\text{ A}$, whose sum is $2.5\text{ A}$.

---

Flashcards for this section are as follows:

- applying superposition: what happens to each independent source in turn, and to the dependent sources? ::@:: Each independent source is considered alone with all others set to zero, a voltage source becoming a short and a current source an open, while dependent sources stay operative.
- setting a voltage source to zero: what does a voltage source $V_{si}$ become when its contribution is not being computed? ::@:: A short circuit, since $V_{si} = 0\text{ V}$.
- setting a current source to zero: what does a current source $I_{sj}$ become when its contribution is not being computed? ::@:: An open circuit, since $I_{sj} = 0\text{ A}$.
- dependent sources: are dependent sources set to zero along with the independent ones? ::@:: No: they remain operative in every partial circuit, with their controlling quantity recomputed for that circuit.
- homogeneity in a circuit: a resistive circuit is solved for $V_s = 6\text{ V}$ and again for $V_s = 12\text{ V}$, giving $V_A = 3\text{ V}$ and $6\text{ V}$; what property does that show? ::@:: Homogeneity: the node voltages $V_A = 0.5 V_s$ and $V_B = 0.25 V_s$ are proportional to the source.
- a branch outside a contribution: the circuit is `[6 V source, + up] — [2 Ω carrying I₁] — (Va) — [2 Ω] — (GND)` and `(Va) — [2 A source, up] — (X) — [2 Ω ∥ 4 V source] — (GND)`; the $4\text{ V}$ source in parallel with a $2\ \Omega$ resistor sits at (X) in series with the $2\text{ A}$ source; what part does that combination play in the current $I_1$? ::@:: None: the combination is in series with the current source, so it contributes nothing to $I_1$.
- worked superposition with a current source: the circuit is `[6 V source, + up] — [2 Ω carrying I₁] — (Va) — [2 Ω] — (GND)` and `(Va) — [2 A source, up] — (X) — [2 Ω ∥ 4 V source] — (GND)`; the $6\text{ V}$ source alone gives $I_1 = \frac{6\text{ V}}{2\ \Omega + 2\ \Omega}$ and the $2\text{ A}$ source alone gives $I_1 = \frac{2\ \Omega}{2\ \Omega + 2\ \Omega} \times 2\text{ A}$; find the total $I_1$. ::@:: $I_1 = 1.5\text{ A} + 1\text{ A} = 2.5\text{ A}$.
- reading a circuit line: in the notation `(X) — [elements] — (Y)`, what do the parentheses, the brackets, the dash, and `∥` mean? ::@:: `(X)` names a node, with `(GND)` the zero-volt ground node; `[...]` holds one element with its value and marks spelled out; `—` is a wire joining consecutive items; and `A ∥ B` puts A and B in parallel between the same pair of nodes.

## combining contributions

The single-source responses are added with their signs, so a source that opposes the others contributes a negative term. When only a partial analysis has been done, one analysis of the whole circuit is a cheap check on the signs.

A circuit of a $36\text{ V}$ source and a $6\text{ A}$ source gives $V_A = 12\text{ V}$ and $V_o = 4\text{ V}$ by nodal analysis. Superposition agrees. With the current source zeroed, the voltage source alone gives $V_o = 8\text{ V}$, and with the voltage source zeroed, the current source alone gives $V_o = -4\text{ V}$. The sum is $4\text{ V}$.

---

Flashcards for this section are as follows:

- combining contributions: how are the single-source responses combined into the output? ::@:: The single-source responses are added with their signs, a source acting in the opposite direction contributing a negative term to the output.
- sign of a contribution: how does a source whose direction opposes the others appear in the sum? ::@:: With a negative sign, so the contributions must be added algebraically rather than in magnitude.
- two-source check: in a circuit of a $36\text{ V}$ source and a $6\text{ A}$ source, the voltage source alone gives $V_o = 8\text{ V}$ and the current source alone gives $V_o = -4\text{ V}$; what is the total $V_o$? ::@:: $V_o = 8\text{ V} + (-4\text{ V}) = 4\text{ V}$, which agrees with nodal analysis of the whole circuit.
- checking the sum: how may a superposition result be checked cheaply? ::@:: By analyzing the whole circuit once by another method, such as nodal analysis, and comparing the outputs.

## power is not linear

Power is quadratic in voltage and current, $P \propto V^2$ and $P \propto I^2$, so it is not linear and superposition does not reach it. Power comes from the total voltage and current, never from adding the powers each source would produce alone.

A resistor of $3\ \Omega$ shows the failure. A source of $8\text{ V}$ drives $I_o = 2\text{ A}$ through it and dissipates $P = 2^2 \times 3 = 12\text{ W}$; $16\text{ V}$ drives $I_o = 4\text{ A}$ and dissipates $P = 4^2 \times 3 = 48\text{ W}$. Doubling the source doubles the current and multiplies the power by four.

---

Flashcards for this section are as follows:

- power is not linear: how does power depend on voltage and current, and what follows for superposition? ::@:: Power is quadratic in voltage and current, $P \propto V^2$ and $P \propto I^2$, so it is not linear and superposition does not apply to it. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why power fails: why may the powers produced by two sources not be added? ::@:: Power is a square function of voltage and current, so it is not linear in the excitation and does not obey superposition.
- scaling of power: a resistor of $3\ \Omega$ carries $I_o = 2\text{ A}$ under $8\text{ V}$ and $I_o = 4\text{ A}$ under $16\text{ V}$; what power does it dissipate and how does it scale? ::@:: $P = 2^2 \times 3 = 12\text{ W}$ and $P = 4^2 \times 3 = 48\text{ W}$: doubling the source quadruples the power.
- finding total power: how is the power in a multi-source circuit obtained? ::@:: From the total voltage and current of the complete circuit, since the separate contributions cannot be added as powers.

## in the phasor domain

The procedure carries over unchanged: one independent source at a time with the rest killed, the circuit solved with the impedances in place, and the contributions added with their signs. The frequencies need care. Every phasor in one circuit carries the single $\omega$ its impedances were computed at, so contributions at different frequencies are combined as waveforms. Each frequency is solved in its own phasor circuit ([phasor](phasor.md)).

---

Flashcards for this section are as follows:

- in the phasor domain / the procedure: how does superposition run on a phasor circuit? ::@:: One independent source at a time with the others killed, each solved with the impedances in place, then the phasor contributions added with their signs.
- in the phasor domain / different frequencies: how are contributions at different frequencies combined? ::@:: In the time domain: each frequency is solved in its own phasor circuit, and the resulting waveforms are added, never the phasors themselves.
