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

Superposition principle turns a circuit with several sources into several circuits with one source each. Each source acts alone while the others are set to zero, and the responses are added to give the response of the whole circuit.

The principle holds exactly for circuits of linear elements, so it applies to resistive networks with independent and dependent sources. It does not extend to power, which is quadratic in current and voltage.

---

Flashcards for this section are as follows:

- overview ::@:: Superposition sums the responses a linear circuit produces for each independent source acting alone, so the output of a circuit with several sources is the sum of the single-source responses.

## linearity

A circuit can be treated as a function with an input and an output: the excitation in, the response out. Homogeneity is $f(kx) = kf(x)$ for every $k$, and the only function meeting it is the straight line through the origin, $f(x) = mx$.

Superposition is $f(x_1 + x_2) = f(x_1) + f(x_2)$. A circuit is linear when both hold at once, $f(a x_1 + b x_2) = a f(x_1) + b f(x_2)$, the statement used when contributions are scaled and added.

Elements whose current is not a straight-line function of their voltage sit outside both properties; the diode is the common example in circuit analysis.

---

Flashcards for this section are as follows:

- overview ::@:: A circuit is linear when it satisfies both homogeneity, $f(kx) = kf(x)$, and superposition, $f(x_1 + x_2) = f(x_1) + f(x_2)$, equivalently $f(a x_1 + b x_2) = a f(x_1) + b f(x_2)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- excitation and response: what are the input and the output of a circuit called when it is viewed as a function? ::@:: The input is the excitation and the output is the response.
- homogeneity: which form must the function $f$ of a homogeneous circuit take? ::@:: A straight line through the origin, $f(x) = mx$; no other function satisfies $f(kx) = kf(x)$.
- superposition property: state the property of $f$ that lets responses be added. ::@:: $f(x_1 + x_2) = f(x_1) + f(x_2)$: the response to a sum of excitations is the sum of the individual responses.
- linearity: which two properties of $f$ together make a circuit linear? ::@:: Homogeneity and superposition, combining into $f(a x_1 + b x_2) = a f(x_1) + b f(x_2)$.
- non-linear element: which familiar element fails homogeneity and superposition, and why? ::@:: The diode, whose current is not a straight-line function of its voltage, so neither property holds in a circuit containing one.

## applying superposition

Each independent source is taken alone while every other is set to zero: a voltage source becomes a short, since $V_{si} = 0\text{ V}$, and a current source an open, since $I_{sj} = 0\text{ A}$.

The [dependent sources](dependent%20source.md) are not set to zero. They stay operative in each single-source circuit, with their controlling quantity recomputed there, so a circuit holding one must be solved afresh for every contribution.

In a worked resistive circuit a $6\text{ V}$ source gives $V_A = 0.5 V_s$ and $V_B = 0.25 V_s$, so $(V_A, V_B)$ is $(3\text{ V}, 1.5\text{ V})$ at $V_s = 6\text{ V}$ and $(6\text{ V}, 3\text{ V})$ at $V_s = 12\text{ V}$: the node voltages are proportional to the source, which is homogeneity at work.

A branch can also escape one contribution altogether. In a circuit of a $6\text{ V}$ source, a $2\ \Omega$ resistor carrying $I_1$, a $2\ \Omega$ resistor to ground, a $2\text{ A}$ source, a further $2\ \Omega$ resistor, and a $4\text{ V}$ source, the parallel combination of that last resistor with the $4\text{ V}$ source sits in series with the $2\text{ A}$ source and plays no part in $I_1$. The contributions are $I_1|_{6\text{V}} = \frac{6\text{ V}}{2\ \Omega + 2\ \Omega} = 1.5\text{ A}$ and $I_1|_{2\text{A}} = \frac{2\ \Omega}{2\ \Omega + 2\ \Omega} \times 2\text{ A} = 1\text{ A}$, whose sum is $2.5\text{ A}$.

---

Flashcards for this section are as follows:

- overview ::@:: Each independent source is considered alone with all others set to zero, a voltage source becoming a short and a current source an open, while dependent sources stay operative.
- setting a voltage source to zero: what does a voltage source $V_{si}$ become when its contribution is not being computed? ::@:: A short circuit, since $V_{si} = 0\text{ V}$.
- setting a current source to zero: what does a current source $I_{sj}$ become when its contribution is not being computed? ::@:: An open circuit, since $I_{sj} = 0\text{ A}$.
- dependent sources: are dependent sources set to zero along with the independent ones? ::@:: No: they remain operative in every partial circuit, with their controlling quantity recomputed for that circuit.
- homogeneity in a circuit: a resistive circuit is solved for $V_s = 6\text{ V}$ and again for $V_s = 12\text{ V}$, giving $V_A = 3\text{ V}$ and $6\text{ V}$; what property does that exhibit? ::@:: Homogeneity: the node voltages $V_A = 0.5 V_s$ and $V_B = 0.25 V_s$ are proportional to the source.
- a branch outside a contribution: a $4\text{ V}$ source stands in parallel with a $2\ \Omega$ resistor, and that combination sits in series with a $2\text{ A}$ source; what part does it play in the current $I_1$ of a neighbouring branch? ::@:: None: the combination is in series with the current source, so it contributes nothing to $I_1$.
- worked superposition with a current source: in that circuit the $6\text{ V}$ source alone gives $I_1 = \frac{6\text{ V}}{2\ \Omega + 2\ \Omega}$ and the $2\text{ A}$ source alone gives $I_1 = \frac{2\ \Omega}{2\ \Omega + 2\ \Omega} \times 2\text{ A}$; find the total $I_1$. ::@:: $I_1 = 1.5\text{ A} + 1\text{ A} = 2.5\text{ A}$.

## combining contributions

The single-source responses are added with their signs, so a source opposing the others contributes a negative term. Where only a partial analysis has been done, one analysis of the whole circuit is a cheap check on the signs.

A circuit of a $36\text{ V}$ source and a $6\text{ A}$ source gives $V_A = 12\text{ V}$ and $V_o = 4\text{ V}$ by nodal analysis. Superposition agrees: with the current source zeroed the voltage source alone gives $V_o = 8\text{ V}$, with the voltage source zeroed the current source alone gives $V_o = -4\text{ V}$, and the sum is $4\text{ V}$.

---

Flashcards for this section are as follows:

- overview ::@:: The single-source responses are added with their signs, a source acting in the opposite direction contributing a negative term to the output.
- sign of a contribution: how does a source whose direction opposes the others appear in the sum? ::@:: With a negative sign, so the contributions must be added algebraically rather than in magnitude.
- two-source check: in a circuit of a $36\text{ V}$ source and a $6\text{ A}$ source, the voltage source alone gives $V_o = 8\text{ V}$ and the current source alone gives $V_o = -4\text{ V}$; what is the total $V_o$? ::@:: $V_o = 8\text{ V} + (-4\text{ V}) = 4\text{ V}$, which agrees with nodal analysis of the whole circuit.
- checking the sum: how may a superposition result be checked cheaply? ::@:: By analyzing the whole circuit once by another method, such as nodal analysis, and comparing the outputs.

## power is not linear

Power is quadratic in voltage and current, $P \propto V^2$ and $P \propto I^2$, so it is not linear and does not obey superposition. It must be computed from the total voltage and current, never by adding the powers each source would produce alone.

A resistor of $3\ \Omega$ shows the failure: a source of $8\text{ V}$ drives $I_o = 2\text{ A}$ and dissipates $P = 2^2 \times 3 = 12\text{ W}$, while $16\text{ V}$ drives $I_o = 4\text{ A}$ and dissipates $P = 4^2 \times 3 = 48\text{ W}$. Doubling the source doubles the current and multiplies the power by four.

---

Flashcards for this section are as follows:

- overview ::@:: Power is quadratic in voltage and current, $P \propto V^2$ and $P \propto I^2$, so it is not linear and superposition does not apply to it. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why power fails: why may the powers produced by two sources not be added? ::@:: Power is a square function of voltage and current, so it is not linear in the excitation and does not obey superposition.
- scaling of power: a resistor of $3\ \Omega$ carries $I_o = 2\text{ A}$ under $8\text{ V}$ and $I_o = 4\text{ A}$ under $16\text{ V}$; what power does it dissipate and how does it scale? ::@:: $P = 2^2 \times 3 = 12\text{ W}$ and $P = 4^2 \times 3 = 48\text{ W}$: doubling the source quadruples the power.
- finding total power: how is the power in a multi-source circuit obtained? ::@:: From the total voltage and current of the complete circuit, since the separate contributions cannot be added as powers.
