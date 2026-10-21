---
aliases:
  - ELEC 2400 Thévenin's theorem
  - ELEC2400 Thévenin's theorem
  - HKUST ELEC 2400 Thévenin's theorem
  - HKUST ELEC2400 Thévenin's theorem
  - Thevenin's theorem
  - Thévenin equivalent circuit
  - Thévenin's theorem
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/Thévenin_s_theorem
  - language/in/English
---

# Thévenin's theorem

Seen from a pair of terminals, any linear network behaves like one ideal voltage source in series with one resistor. Thévenin's theorem says so, and the claim holds however complicated the network is, for every load attached to those terminals.

The source is the network's open-circuit voltage, the resistor its resistance seen from the terminals. Those two numbers are fixed by the network alone, so two networks that share them can replace each other, and a load can be reattached without solving the network behind it again.

---

Flashcards for this section are as follows:

- Thévenin's theorem: what two-element circuit replaces a linear network seen from a terminal pair? ::@:: A linear network seen from a terminal pair can be replaced by an ideal voltage source $V_{oc}$ in series with a resistor $R_{\text{eq}}$, where $V_{oc}$ is its open-circuit voltage and $R_{\text{eq}}$ its resistance seen from the terminals with independent sources set to zero. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## one-port equivalence

Two resistive one-ports are equivalent when their terminal current-voltage characteristics agree for every load, sources included. Written out, that means $I_A = I_B$ and $V_A = V_B$ for every load $L$. Either network can then take the other's place.

One matching load proves nothing. A $4\text{ V}$ network with $2\ \Omega$ and an $8\text{ V}$ network with $6\ \Omega$ agree at a $2\ \Omega$ load, where both give $V_o = 2\text{ V}$ and $I_o = 1\text{ A}$. At $6\ \Omega$ they part: the first gives $V_o = 3\text{ V}$ and $I_o = 0.5\text{ A}$, the second $V_o = 4\text{ V}$ and $I_o = 0.67\text{ A}$.

Testing equality takes only the two extreme loads. A short fixes the short-circuit current and an open fixes the open-circuit voltage, and two points fix the straight line that is a linear one-port's characteristic.

---

Flashcards for this section are as follows:

- two one-port networks: what must their current-voltage characteristics share, and across which loads? ::@:: Two one-port networks are equivalent when their current-voltage characteristics agree across the terminals for every load, including sources.
- definition of equivalence: which condition on the terminal currents $I_A$, $I_B$ and voltages $V_A$, $V_B$ makes two resistive one-ports equivalent? ::@:: The same terminal current-voltage characteristic for all loads, that is $I_A = I_B$ and $V_A = V_B$ for every load.
- insufficient test: two networks agree at a $2\ \Omega$ load but differ at a $6\ \Omega$ load; are they equivalent? ::@:: No: equivalence requires agreement for all loads, so a single matching load proves nothing.
- extreme loads: which two loads are enough to test a linear one-port for equivalence? ::@:: A short circuit, which fixes the short-circuit current, and an open circuit, which fixes the open-circuit voltage.

## equivalent circuit

A linear circuit seen from its terminal pair becomes an ideal voltage source $V_{oc}$ in series with a resistor $R_{\text{eq}}$. The source is the open-circuit voltage, also called Thévenin's equivalent source. The resistor is the network's output resistance: what is left looking into the terminals once every independent source is set to zero.

Dependent sources stay operative while $R_{\text{eq}}$ is computed; only the independent ones are zeroed. Only the network has to be linear. The load may hold non-linear parts, which is how the theorem separates a linear source network from whatever hangs on it.

---

Flashcards for this section are as follows:

- the equivalent circuit: which two elements does it hold, and how does each come out of the network? ::@:: The equivalent circuit is $V_{oc}$ in series with $R_{\text{eq}}$, $V_{oc}$ being the open-circuit voltage and $R_{\text{eq}}$ the resistance seen at the terminals with independent sources zeroed and dependent sources left operative. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- naming: what are $V_{oc}$ and $R_{\text{eq}}$, the two elements of a Thévenin equivalent, called? ::@:: $V_{oc}$ is Thévenin's equivalent source and $R_{\text{eq}}$ is Thévenin's equivalent resistance, or the output resistance of the network.
- dependent sources: what becomes of them while $R_{\text{eq}}$ is computed? ::@:: They remain operative; only the independent sources are set to zero.
- linearity: which part of the circuit has to be linear for the theorem to apply? ::@:: The network at the terminals; the attached load may contain non-linear components.

### computing the equivalent

Set the load aside and compute the two numbers in turn. $V_{oc}$ comes first, with the terminals open. Then zero every independent source, shorting the voltage sources and opening the current ones, and reduce the dead network to a single resistance for $R_{\text{eq}}$.

Circuit lines here follow one notation. `(X)` names a node, with `(GND)` the zero-volt ground node; `[...]` holds one element, its value and marks spelled out in words; `—` is a wire joining consecutive items; and `A ∥ B` puts two elements in parallel between the same pair of nodes. The line `(A) — [2 Ω] — (B)` reads node $A$ feeding a $2\ \Omega$ resistor that reaches node $B$.

A worked network is drawn `(GND) — [36 V source, + up] — (P) — [4 Ω] — (a)` and `(GND) — [3 Ω ∥ 6 A source, up] — (b)`. It holds a $36\text{ V}$ source between ground and a node $P$, a $4\ \Omega$ resistor from $P$ to terminal $a$, and terminal $b$ reaching ground through a $3\ \Omega$ resistor that a $6\text{ A}$ source feeds in parallel. With the terminals open no current crosses the $4\ \Omega$ resistor, so its drop is $0\text{ V}$ and $V_{oc} = 36 - 6 \times 3 + 0 \times 4 = 18\text{ V}$. Zeroing the $36\text{ V}$ source and opening the $6\text{ A}$ source leaves the two resistors in series across the terminals, $R_{\text{eq}} = 4\ \Omega + 3\ \Omega = 7\ \Omega$.

Changing the load then needs no second solution. A network holding $4\text{ mA}$, $12\text{ V}$, $2\text{ mA}$, and $6\text{ V}$ sources with $1\text{ k}\Omega$ and $2\text{ k}\Omega$ resistors gives $V_{oc} = V_a - V_b = 6\text{ V} + 12\text{ V} + 2\text{ V} = 20\text{ V}$, where the $2\text{ V}$ term is the drop the $2\text{ mA}$ source produces across a $1\text{ k}\Omega$ resistor. Zeroing the sources leaves $R_{\text{eq}} = 2\text{ k}\Omega$, so $I_{sc} = \frac{20\text{ V}}{2\text{ k}\Omega} = 10\text{ mA}$. A $2\text{ k}\Omega$ load in place of a $1\text{ k}\Omega$ one then carries $I_o = \frac{20\text{ V}}{2\text{ k}\Omega + 2\text{ k}\Omega} = 5\text{ mA}$.

---

Flashcards for this section are as follows:

- computing the equivalent: how is each of the two numbers obtained? ::@:: $V_{oc}$ is found with the terminals open, and $R_{\text{eq}}$ by zeroing every independent source and reducing the dead network to one resistance. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- setting sources to zero: what does each source become when $R_{\text{eq}}$ is computed? ::@:: A voltage source becomes a short circuit and a current source becomes an open circuit.
- open-circuit condition: the worked network is `(GND) — [36 V source, + up] — (P) — [4 Ω] — (a)` and `(GND) — [3 Ω ∥ 6 A source, up] — (b)`; with $a$ and $b$ open, why does the $4\ \Omega$ resistor contribute nothing to $V_{oc}$? ::@:: No current flows through the $4\ \Omega$ branch, so its voltage drop is $0\text{ V}$; $V_{oc} = 36 - 6 \times 3 = 18\text{ V}$.
- equivalent resistance: the worked network is `(GND) — [36 V source, + up] — (P) — [4 Ω] — (a)` and `(GND) — [3 Ω ∥ 6 A source, up] — (b)`; what is $R_{\text{eq}}$ seen from a-b once the sources are zeroed? ::@:: With the $36\text{ V}$ source shorted and the $6\text{ A}$ source opened, the $4\ \Omega$ and $3\ \Omega$ resistors remain in series, giving $R_{\text{eq}} = 4\ \Omega + 3\ \Omega = 7\ \Omega$.
- reattaching a load, finding the resistance: a network has $V_{oc} = 4\text{ V}$; with a $1\text{ k}\Omega$ load the output is $1\text{ V}$; what is $R_{\text{eq}}$? ::@:: From $V_o = V_{oc}\frac{R_L}{R_{\text{eq}}+R_L}$, the $1\text{ k}\Omega$ load gives $R_{\text{eq}} = 3\text{ k}\Omega$.
- reattaching a load, predicting the output: a network has $V_{oc} = 4\text{ V}$ and $R_{\text{eq}} = 3\text{ k}\Omega$; what does a $3\text{ k}\Omega$ load see? ::@:: $V_o = 4\text{ V} \times \frac{3\text{ k}\Omega}{3\text{ k}\Omega + 3\text{ k}\Omega} = 2\text{ V}$.
- three numbers of a network: between terminals a-b sit, in series, `[a] — [6 V source, + up] — [12 V source, + up] — [1 kΩ with 2 mA down it, a 2 V rise] — (b)`, and the network has $R_{\text{eq}} = 2\text{ k}\Omega$ once its sources are zeroed; find $V_{oc}$ and $I_{sc}$. ::@:: $V_{oc} = 6\text{ V} + 12\text{ V} + 2\text{ V} = 20\text{ V}$ and $I_{sc} = \frac{20\text{ V}}{2\text{ k}\Omega} = 10\text{ mA}$.
- load after the reduction: a network has $V_{oc} = 20\text{ V}$ and $R_{\text{eq}} = 2\text{ k}\Omega$; what current does a $2\text{ k}\Omega$ load carry? ::@:: $I_o = \frac{20\text{ V}}{2\text{ k}\Omega + 2\text{ k}\Omega} = 5\text{ mA}$.
- reading a circuit line: in the notation `(X) — [elements] — (Y)`, what do the parentheses, the brackets, the dash, and `∥` mean? ::@:: `(X)` names a node, with `(GND)` the zero-volt ground node; `[...]` holds one element with its value and marks spelled out; `—` is a wire joining consecutive items; and `A ∥ B` puts A and B in parallel between the same pair of nodes.

### shortcuts

A resistor across an ideal voltage source can be dropped when the other circuit variables are computed: the source fixes the voltage across it, so the resistor changes nothing else. A network of $8\text{ V}$ with $2\ \Omega$ across it is therefore a bare $8\text{ V}$ source, with $V_{oc} = 8\text{ V}$ and $R_{\text{eq}} = 0\ \Omega$.

The dual case is a resistor in series with an ideal current source. It can be dropped too, since the source fixes the branch current whatever the resistance is.

---

Flashcards for this section are as follows:

- shortcuts: which resistor may be left out when the other circuit variables are computed? ::@:: A resistor in parallel with an ideal voltage source may be neglected in computing other circuit variables, and a resistor in series with an ideal current source may be neglected likewise.
- parallel with a voltage source: a network of $8\text{ V}$ with $2\ \Omega$ in parallel is reduced to a Thévenin equivalent; what are $V_{oc}$ and $R_{\text{eq}}$? ::@:: $V_{oc} = 8\text{ V}$ and $R_{\text{eq}} = 0\ \Omega$: the parallel resistor is shorted out by the ideal source.
- why the parallel branch drops out: why may a resistor across an ideal voltage source be ignored? ::@:: The source fixes the voltage across the resistor regardless of its value, so the resistor cannot change any other branch voltage or current.
- dual case: which resistor may be ignored when a network is being reduced for a Norton equivalent? ::@:: One in series with an ideal current source, since the source fixes the branch current whatever the resistance.

## dependent sources

A dependent source stays operative when the independent ones are zeroed, so the dead network is not passive and series and parallel reduction no longer gives $R_{\text{eq}}$. Apply a test source instead. Put a test voltage $V_T$ on the terminal and measure the current $I_T$ entering it, or push a test current $I_T$ in and measure $V_T$, then take $R_{\text{eq}} = \frac{V_T}{I_T}$. Either $V_T = 1\text{ V}$ or $I_T = 1\text{ A}$ keeps the arithmetic simple.

The short-circuit current gives the same resistance: compute $V_{oc}$ and $I_{sc}$ separately and take $R_{\text{eq}} = \frac{V_{oc}}{I_{sc}}$. A worked network with a dependent source gives $V_{oc} = 22\text{ V}$ and $I_{sc} = 5.5\text{ A}$, so $R_{\text{eq}} = 4\ \Omega$. A $1\text{ A}$ test current confirms it, with $V_{ab} = 4\text{ V}$.

---

Flashcards for this section are as follows:

- dependent sources: what stands in for the series and parallel reduction when it cannot be used? ::@:: With dependent sources present, $R_{\text{eq}}$ is found by applying a test source and taking $R_{\text{eq}} = \frac{V_T}{I_T}$, or by combining $V_{oc}$ with the short-circuit current as $R_{\text{eq}} = \frac{V_{oc}}{I_{sc}}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why zeroing is not enough: why does zeroing the independent sources fail to give $R_{\text{eq}}$ while dependent sources remain? ::@:: The dependent sources stay operative, so the dead network is not a passive resistor network and cannot be reduced by series and parallel rules.
- test source method: how is $R_{\text{eq}}$ obtained from a test source? ::@:: Apply a test voltage $V_T$ and measure the current $I_T$ entering the terminal, or apply a test current $I_T$ and measure $V_T$, then compute $R_{\text{eq}} = \frac{V_T}{I_T}$.
- test-source values: which values of $V_T$ and $I_T$ simplify the arithmetic of the test-source method? ::@:: $V_T = 1\text{ V}$ with the current measured, or $I_T = 1\text{ A}$ with the voltage measured.
- short-circuit route: how is $R_{\text{eq}}$ found from an open-circuit and a short-circuit measurement? ::@:: Compute $V_{oc}$ with the terminals open and $I_{sc}$ with them shorted, then take $R_{\text{eq}} = \frac{V_{oc}}{I_{sc}}$.
- worked resistance: a network with a dependent source has $V_{oc} = 22\text{ V}$ and $I_{sc} = 5.5\text{ A}$; what is $R_{\text{eq}}$? ::@:: $R_{\text{eq}} = \frac{22\text{ V}}{5.5\text{ A}} = 4\ \Omega$, which the $1\text{ A}$ test current confirms with $V_{ab} = 4\text{ V}$.

## general proof

Take a resistive linear network with $M$ independent voltage sources, $N$ independent current sources, and any number of dependent sources. Connect an external current source $I_{\text{ext}}$ to a chosen port.

Superposition writes the port voltage as the independent sources' contributions plus the external source's, $V_{AB} = \sum_{m=1}^{M} A_m V_m + \sum_{n=1}^{N} B_n I_n + I_{\text{ext}} R_{\text{eq}}$, with dependent sources left operative. The two sums are what remains when $I_{\text{ext}} = 0$, the open-circuit condition, so they add up to $V_{oc}$ and the characteristic reduces to $V_{AB} = V_{oc} + I_{\text{ext}} R_{\text{eq}}$.

That characteristic belongs to $V_{oc}$ in series with $R_{\text{eq}}$, and it holds for every $I_{\text{ext}}$ and $V_{AB}$, so the two circuits are equivalent.

---

Flashcards for this section are as follows:

- general proof: why does the port characteristic of the network match that of a voltage source in series with a resistor? ::@:: Superposition writes the port voltage as the independent sources' contributions plus $I_{\text{ext}} R_{\text{eq}}$; the first part is the open-circuit voltage, giving $V_{AB} = V_{oc} + I_{\text{ext}} R_{\text{eq}}$, which is the characteristic of the Thévenin circuit. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- superposition form: how does superposition express the port voltage of a linear network with an external current source $I_{\text{ext}}$? ::@:: $V_{AB} = \sum_m A_m V_m + \sum_n B_n I_n + I_{\text{ext}} R_{\text{eq}}$, with dependent sources left operative.
- identifying the open-circuit voltage: which terms of $V_{AB} = \sum_m A_m V_m + \sum_n B_n I_n + I_{\text{ext}} R_{\text{eq}}$ form the open-circuit voltage, and why? ::@:: The sums over the independent sources, since they are what remains when $I_{\text{ext}} = 0$, that is, when the port is open.
- conclusion: what does the proof derive about the port voltage $V_{AB}$ and the external current $I_{\text{ext}}$, and what does it establish? ::@:: $V_{AB} = V_{oc} + I_{\text{ext}} R_{\text{eq}}$, the characteristic of a voltage source $V_{oc}$ in series with $R_{\text{eq}}$; it holds for all $I_{\text{ext}}$ and $V_{AB}$, so the two circuits are equivalent.

## in the phasor domain

At one frequency, any linear one-port becomes an open-circuit voltage phasor in series with the impedance looking into the port with the sources deactivated: $\mathbf{V}_{th}$ and $\mathbf{Z}_{th}$. The impedance comes from the same deactivate-and-combine steps. A test source driven into the dead port gives it as well, as $\mathbf{V}_{test}/\mathbf{I}_{test}$. The equivalent holds only at the frequency its impedances were computed at ([phasor](phasor.md)).

---

Flashcards for this section are as follows:

- in the phasor domain / the equivalent: what plays the part of $V_{th}$ and $R_{th}$ in a phasor circuit? ::@:: The open-circuit voltage phasor $\mathbf{V}_{th}$ and the impedance $\mathbf{Z}_{th}$ seen looking into the port with every source deactivated.
- in the phasor domain / the test source: how is $\mathbf{Z}_{th}$ found with a test source, and what does complex arithmetic change? ::@:: Drive the dead port with a test source and take $\mathbf{V}_{test}/\mathbf{I}_{test}$; the division is complex, so the result comes back with a magnitude and a phase.
- in the phasor domain / the frequency bound: at how many frequencies does a phasor Thévenin equivalent hold? ::@:: One: $\mathbf{Z}_{th}$ is built from $1/(j\omega C)$ and $j\omega L$, which change with the frequency. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
