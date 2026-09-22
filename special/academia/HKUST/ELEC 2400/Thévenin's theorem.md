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

Thévenin's theorem replaces a whole linear network, seen from a pair of terminals, by one ideal voltage source in series with one resistor. However complicated the network, the terminal pair behaves like that two-element circuit for every load.

The two numbers are the network's open-circuit voltage and its resistance seen from the terminals. The equivalent is unique, so two networks with the same pair of numbers are interchangeable, and a load can be reattached without re-analyzing the network behind it.

---

Flashcards for this section are as follows:

- overview ::@:: A linear network seen from a terminal pair can be replaced by an ideal voltage source $V_{oc}$ in series with a resistor $R_{\text{eq}}$, where $V_{oc}$ is its open-circuit voltage and $R_{\text{eq}}$ its resistance seen from the terminals with independent sources set to zero. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## one-port equivalence

Two resistive one-port networks are equivalent when they have the same current-voltage characteristic across their terminals for all loads, sources included: if $I_A = I_B$ and $V_A = V_B$ for every load $L$, either can replace the other.

Agreement on one load proves nothing. A network of $4\text{ V}$ with $2\ \Omega$ and one of $8\text{ V}$ with $6\ \Omega$ agree at a $2\ \Omega$ load, both giving $V_o = 2\text{ V}$ and $I_o = 1\text{ A}$, and disagree at $6\ \Omega$, where the first gives $V_o = 3\text{ V}$ and $I_o = 0.5\text{ A}$ against $V_o = 4\text{ V}$ and $I_o = 0.67\text{ A}$.

Two extreme loads suffice to test equality: a short fixes the short-circuit current and an open fixes the open-circuit voltage, and those two points determine the straight-line characteristic of a linear one-port.

---

Flashcards for this section are as follows:

- overview ::@:: Two one-port networks are equivalent when their current-voltage characteristics agree across the terminals for every load, including sources.
- definition of equivalence: what must the terminal currents $I_A$ and $I_B$ and voltages $V_A$ and $V_B$ of two resistive one-port networks share to be equivalent? ::@:: The same terminal current-voltage characteristic for all loads, that is $I_A = I_B$ and $V_A = V_B$ for every load.
- insufficient test: two networks agree at a $2\ \Omega$ load but differ at a $6\ \Omega$ load; are they equivalent? ::@:: No: equivalence requires agreement for all loads, so a single matching load proves nothing.
- extreme loads: which two loads suffice to test a linear one-port's equivalence? ::@:: A short circuit, which fixes the short-circuit current, and an open circuit, which fixes the open-circuit voltage.

## the equivalent circuit

A linear circuit with a terminal pair is replaced by an ideal voltage source $V_{oc}$ in series with a resistor $R_{\text{eq}}$. $V_{oc}$ is the open-circuit voltage, also called Thévenin's equivalent source, and $R_{\text{eq}}$ is the resistance looking into the network with all independent sources set to zero, the network's output resistance.

Dependent sources stay operative while $R_{\text{eq}}$ is computed. Only the network needs to be linear; the load may hold non-linear components, which is what lets the theorem separate a linear source network from whatever hangs on it.

---

Flashcards for this section are as follows:

- overview ::@:: The equivalent circuit is $V_{oc}$ in series with $R_{\text{eq}}$, $V_{oc}$ being the open-circuit voltage and $R_{\text{eq}}$ the resistance seen at the terminals with independent sources zeroed and dependent sources left operative. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- naming: what are the two elements $V_{oc}$ and $R_{\text{eq}}$ of a Thévenin equivalent called? ::@:: $V_{oc}$ is Thévenin's equivalent source and $R_{\text{eq}}$ is Thévenin's equivalent resistance, or the output resistance of the network.
- dependent sources: what happens to dependent sources when $R_{\text{eq}}$ is computed? ::@:: They remain operative; only the independent sources are set to zero.
- linearity requirement: which part of the circuit must be linear for the theorem to apply? ::@:: The network at the terminals; the attached load may contain non-linear components.

## computing the equivalent

The load is set aside and the two numbers computed in turn: $V_{oc}$ with the terminals open, then $R_{\text{eq}}$ by zeroing every independent source, voltage sources shorted and current sources opened, and reducing the dead network to a single resistance.

A network of $4\ \Omega$, $36\text{ V}$, $3\ \Omega$, and $6\text{ A}$ gives $V_{oc} = 36 - 6 \times 3 + 0 \times 4 = 18\text{ V}$ with the terminals open, the $4\ \Omega$ branch carrying no current, and $R_{\text{eq}} = 4\ \Omega + 3\ \Omega = 7\ \Omega$ once the sources are zeroed.

Changing the load then needs no second solution. A network holding $4\text{ mA}$, $12\text{ V}$, $2\text{ mA}$, and $6\text{ V}$ sources with $1\text{ k}\Omega$ and $2\text{ k}\Omega$ resistors gives $V_{oc} = V_a - V_b = 6\text{ V} + 12\text{ V} + 2\text{ V} = 20\text{ V}$, the $2\text{ V}$ term being the drop the $2\text{ mA}$ source produces across a $1\text{ k}\Omega$ resistor, and $R_{\text{eq}} = 2\text{ k}\Omega$ once the sources are zeroed, so $I_{sc} = \frac{20\text{ V}}{2\text{ k}\Omega} = 10\text{ mA}$ and a $2\text{ k}\Omega$ load in place of a $1\text{ k}\Omega$ one carries $I_o = \frac{20\text{ V}}{2\text{ k}\Omega + 2\text{ k}\Omega} = 5\text{ mA}$.

---

Flashcards for this section are as follows:

- overview ::@:: $V_{oc}$ is found with the terminals open, and $R_{\text{eq}}$ by zeroing every independent source and reducing the dead network to one resistance. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- setting sources to zero: what does each source become when $R_{\text{eq}}$ is computed? ::@:: A voltage source becomes a short circuit and a current source becomes an open circuit.
- open-circuit condition: in the network of $4\ \Omega$, $36\text{ V}$, $3\ \Omega$, and $6\text{ A}$, why does the $4\ \Omega$ resistor contribute nothing to $V_{oc}$? ::@:: The terminals are open, so no current flows through that branch and its voltage drop is $0\text{ V}$; $V_{oc} = 36 - 6 \times 3 = 18\text{ V}$.
- equivalent resistance: the same network has $R_{\text{eq}} = 7\ \Omega$; show how. ::@:: With the $36\text{ V}$ source shorted and the $6\text{ A}$ source opened, the $4\ \Omega$ and $3\ \Omega$ resistors remain in series, giving $R_{\text{eq}} = 4\ \Omega + 3\ \Omega = 7\ \Omega$.
- reattaching a load: a network has $V_{oc} = 4\text{ V}$; with a $1\text{ k}\Omega$ load the output is $1\text{ V}$ and with a $3\text{ k}\Omega$ load it is $2\text{ V}$; what is $R_{\text{eq}}$ and what does the second load show? ::@:: From $V_o = V_{oc}\frac{R_L}{R_{\text{eq}}+R_L}$, the $1\text{ k}\Omega$ load gives $R_{\text{eq}} = 3\text{ k}\Omega$; the $3\text{ k}\Omega$ load then gives $V_o = 2\text{ V}$, as required.
- all three numbers of a network: a network at terminals a-b holds $4\text{ mA}$, $12\text{ V}$, $2\text{ mA}$, and $6\text{ V}$ sources with $1\text{ k}\Omega$ and $2\text{ k}\Omega$ resistors; find $V_{oc}$, $R_{\text{eq}}$, $I_{sc}$, and the current into a $2\text{ k}\Omega$ load. ::@:: $V_{oc} = V_a - V_b = 6\text{ V} + 12\text{ V} + 2\text{ V} = 20\text{ V}$, $R_{\text{eq}} = 2\text{ k}\Omega$, $I_{sc} = \frac{V_{oc}}{R_{\text{eq}}} = 10\text{ mA}$, and $I_o = \frac{20\text{ V}}{2\text{ k}\Omega + 2\text{ k}\Omega} = 5\text{ mA}$.

## shortcuts

A resistor in parallel with an ideal voltage source can be neglected when other circuit variables are computed, since the source fixes the voltage across it. A network of $8\text{ V}$ with $2\ \Omega$ in parallel is therefore a bare $8\text{ V}$ source, with $V_{oc} = 8\text{ V}$ and $R_{\text{eq}} = 0\ \Omega$.

The dual holds for the other equivalent circuit: a resistor in series with an ideal current source can be neglected, since the source fixes the branch current whatever the resistance.

---

Flashcards for this section are as follows:

- overview ::@:: A resistor in parallel with an ideal voltage source may be neglected in computing other circuit variables, and a resistor in series with an ideal current source may be neglected likewise.
- parallel with a voltage source: a network of $8\text{ V}$ with $2\ \Omega$ in parallel is reduced to a Thévenin equivalent; what are $V_{oc}$ and $R_{\text{eq}}$? ::@:: $V_{oc} = 8\text{ V}$ and $R_{\text{eq}} = 0\ \Omega$: the parallel resistor is shorted out by the ideal source.
- why the parallel branch drops out: why may a resistor across an ideal voltage source be ignored? ::@:: The source fixes the voltage across the resistor regardless of its value, so the resistor cannot change any other branch voltage or current.
- dual case: which resistor may be ignored when a network is being reduced for a Norton equivalent? ::@:: One in series with an ideal current source, since the source fixes the branch current whatever the resistance.

## dependent sources

With dependent sources present, zeroing the independent ones leaves them operative, so $R_{\text{eq}}$ cannot be read off by series and parallel reduction. A test source is applied instead: apply a test voltage $V_T$ and find the current $I_T$ entering a terminal, or apply a test current $I_T$ and find $V_T$, and take $R_{\text{eq}} = \frac{V_T}{I_T}$; $V_T = 1\text{ V}$ or $I_T = 1\text{ A}$ simplifies the arithmetic.

The short-circuit current gives the same resistance: compute $V_{oc}$ and $I_{sc}$ separately and take $R_{\text{eq}} = \frac{V_{oc}}{I_{sc}}$. For a network of $10\text{ V}$, $2\ \Omega$, and $3\text{ A}$ with a dependent source $2I$, the open terminals give $I = -3\text{ A}$, $V_a = 16\text{ V}$, $V_b = -6\text{ V}$, and $V_{oc} = 22\text{ V}$, while shorting them gives $V_a = V_b = 10 - 2I = 2I$, so $I = 2.5\text{ A}$, $I_{sc} = I + 3 = 5.5\text{ A}$, and $R_{\text{eq}} = \frac{22\text{ V}}{5.5\text{ A}} = 4\ \Omega$. A $1\text{ A}$ test current confirms it: $I = -1\text{ A}$, the outer loop gives $2I + V_{ab} + 2I = 0$, so $V_{ab} = -4I = 4\text{ V}$ and $R_{\text{eq}} = 4\ \Omega$.

---

Flashcards for this section are as follows:

- overview ::@:: With dependent sources present, $R_{\text{eq}}$ is found by applying a test source and taking $R_{\text{eq}} = \frac{V_T}{I_T}$, or by combining $V_{oc}$ with the short-circuit current as $R_{\text{eq}} = \frac{V_{oc}}{I_{sc}}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why sources cannot simply be zeroed: why does zeroing independent sources not give $R_{\text{eq}}$ directly when dependent sources are present? ::@:: The dependent sources stay operative, so the dead network is not a passive resistor network and cannot be reduced by series and parallel rules.
- test source method: how is $R_{\text{eq}}$ obtained from a test source? ::@:: Apply a test voltage $V_T$ and measure the current $I_T$ entering the terminal, or apply a test current $I_T$ and measure $V_T$, then compute $R_{\text{eq}} = \frac{V_T}{I_T}$.
- test-source values: which values of $V_T$ and $I_T$ simplify the arithmetic of the test-source method? ::@:: $V_T = 1\text{ V}$ with the current measured, or $I_T = 1\text{ A}$ with the voltage measured.
- short-circuit route: how is $R_{\text{eq}}$ found from an open-circuit and a short-circuit measurement? ::@:: Compute $V_{oc}$ with the terminals open and $I_{sc}$ with them shorted, then take $R_{\text{eq}} = \frac{V_{oc}}{I_{sc}}$.
- worked resistance: a network with a dependent source has $V_{oc} = 22\text{ V}$ and $I_{sc} = 5.5\text{ A}$; what is $R_{\text{eq}}$? ::@:: $R_{\text{eq}} = \frac{22\text{ V}}{5.5\text{ A}} = 4\ \Omega$, which the $1\text{ A}$ test current confirms with $V_{ab} = 4\text{ V}$.

## general proof

Take a resistive linear network with $M$ independent voltage sources, $N$ independent current sources, and any number of dependent sources, and connect an external current source $I_{\text{ext}}$ to a chosen port.

By superposition the port voltage is the sum of the contributions of the independent sources and of the external source, $V_{AB} = \sum_{m=1}^{M} A_m V_m + \sum_{n=1}^{N} B_n I_n + I_{\text{ext}} R_{\text{eq}}$, with dependent sources left operative. The two sums are what appears when $I_{\text{ext}} = 0$, that is, the open-circuit voltage, so the characteristic reduces to $V_{AB} = V_{oc} + I_{\text{ext}} R_{\text{eq}}$.

That is the characteristic of $V_{oc}$ in series with $R_{\text{eq}}$, and it holds for every $I_{\text{ext}}$ and $V_{AB}$, so the two circuits are equivalent.

---

Flashcards for this section are as follows:

- overview ::@:: Superposition writes the port voltage as the independent sources' contributions plus $I_{\text{ext}} R_{\text{eq}}$; the first part is the open-circuit voltage, giving $V_{AB} = V_{oc} + I_{\text{ext}} R_{\text{eq}}$, which is the characteristic of the Thévenin circuit. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- superposition form: how does superposition express the port voltage of a linear network with an external current source $I_{\text{ext}}$? ::@:: $V_{AB} = \sum_m A_m V_m + \sum_n B_n I_n + I_{\text{ext}} R_{\text{eq}}$, with dependent sources left operative.
- identifying the open-circuit voltage: which terms of $V_{AB} = \sum_m A_m V_m + \sum_n B_n I_n + I_{\text{ext}} R_{\text{eq}}$ form the open-circuit voltage, and why? ::@:: The sums over the independent sources, since they are what remains when $I_{\text{ext}} = 0$, that is, when the port is open.
- conclusion: what does the proof derive about the port voltage $V_{AB}$ and the external current $I_{\text{ext}}$, and what does it establish? ::@:: $V_{AB} = V_{oc} + I_{\text{ext}} R_{\text{eq}}$, the characteristic of a voltage source $V_{oc}$ in series with $R_{\text{eq}}$; it holds for all $I_{\text{ext}}$ and $V_{AB}$, so the two circuits are equivalent.
