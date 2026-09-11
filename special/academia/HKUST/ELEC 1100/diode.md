---
aliases:
  - diode
  - pn junction diode
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1100/diode
  - language/in/English
---

# diode

A diode is a two-terminal semiconductor device that allows current to flow primarily in one direction. It serves as a nonlinear element (rectifying or limiting voltages) and as the building block for [Zener regulators](voltage%20regulator.md#diode%20and%20zener%20diode%20as%20regulators) and [bipolar junction transistors](transistor.md). <p> ![diode symbol](attachments/symbol_diode.svg)

---

Flashcards for this section are as follows:

- diode definition ::@:: A two-terminal device that allows current to flow primarily in one direction (forward bias) and blocks it in reverse bias.
- diode course role ::@:: The PN junction is the core building block inside BJTs and Zener regulators; diode I–V and biasing ideas transfer directly.
- schematic symbol: diode <p> ![diode symbol](attachments/symbol_diode.svg) ::@:: Diode symbol showing the one-way conduction element; current is intended to flow from anode to cathode when forward biased.

## pn junction and biasing

A PN junction diode is made by joining P-type and N-type semiconductor regions; at the junction a depletion region forms with a built-in barrier potential of about $0.7\text{ V}$ for silicon. The diode terminals are called anode (P side) and cathode (N side). When the anode is at a higher potential than the cathode (forward bias), the barrier is reduced and current can flow; when the anode is at a lower potential (reverse bias), the barrier increases and only a very small leakage current flows. On the physical diodes used in ELEC 1100, the cathode is marked by a stripe (often black) on the package, so "black strip is negative"; the small-signal diode is a thinner body, while the Zener diode used for regulation is a slightly fatter package but still uses the stripe to mark the cathode.

Biasing refers to how an external voltage connects to the diode. Conventional current flows from anode (+) to cathode (−) when forward biased. When reverse biased, the diode is modelled as an open circuit.

---

Flashcards for this section are as follows:

- pn junction formation ::@:: Joining P-type and N-type semiconductor regions; a depletion region forms at the junction.
- silicon barrier potential ::@:: About $0.7\text{ V}$ for a silicon PN junction.
- diode terminals ::@:: P side = anode; N side = cathode.
- forward vs reverse bias ::@:: Forward: anode at higher potential than cathode (current flows). Reverse: anode at lower potential (current blocked except leakage).
- conventional current direction ::@:: From anode (+) to cathode (−) when forward biased.
- lab diode orientation ::@:: Black stripe marks the cathode (negative end); connect it to the more negative node.

## diode i–v characteristic and models

The exact I–V curve is nonlinear, but circuit analysis uses simplified piecewise models. The ideal-diode model is a short circuit when forward biased and open when reverse biased. The constant-voltage model adds a $V_{\text{on}}\approx0.7\text{ V}$ drop when conducting: ON gives $V_D\approx0.7\text{ V}$, OFF gives $I_D\approx0$.

Analysis proceeds by assuming a diode state (ON or OFF), replacing it with the corresponding equivalent circuit, solving with [Kirchhoff's circuit laws](Kirchhoff%27s%20circuit%20laws.md) and Ohm's law, and checking consistency (whether $V_D$ and $I_D$ match the assumed region).

---

Flashcards for this section are as follows:

- ideal diode model ::@:: In the ideal model the diode is a short circuit when forward biased and an open circuit when reverse biased.
- constant-voltage model ::@:: $V_D\approx0.7\text{ V}$ for a conducting silicon diode.
- diode assumption method ::@:: Assume ON or OFF, replace with equivalent circuit (ON: $0.7\text{ V}$ drop; OFF: open), solve, check consistency.
- diode assumption check ::@:: If $V_D$ and $I_D$ are inconsistent with the assumed region, flip the assumption and re-solve.

## simple diode circuit analysis

For a series source–resistor–diode circuit, we can use the constant-drop model to find the current. If the supply voltage $V_S$ is less than about $0.7\text{ V}$, the diode is off and no current flows; the circuit behaves like an open switch. If $V_S$ exceeds $0.7\text{ V}$ and the diode is forward biased, we approximate $V_D\approx0.7\text{ V}$ and find $I_D\approx(V_S-0.7\text{ V})/R$ and $V_R\approx V_S-0.7\text{ V}$. <p> ![series source–resistor–diode circuit](attachments/series_diode_resistor.svg)

---

Flashcards for this section are as follows:

- series diode current <p> ![series source–resistor–diode circuit](attachments/series_diode_resistor.svg) ::@:: $I_D\approx(V_S-0.7\text{ V})/R$ when $V_S>0.7\text{ V}$ and forward biased.
- diode off condition <p> ![series source–resistor–diode circuit](attachments/series_diode_resistor.svg) ::@:: When $V_S<0.7\text{ V}$, the diode is off and $I_D\approx0$.

## diode safety in the lab

Include a series resistor (typically around $1\text{ k}\Omega$ in lab circuits) with a diode or LED; otherwise the current can become very large when the diode turns on, potentially damaging the diode, LED, or other components.

---

Flashcards for this section are as follows:

- series resistor with diode/LED ::@:: Limits current; without it, forward-biased current can become very large and damage components.
