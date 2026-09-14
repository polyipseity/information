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

- diode definition ::@:: A two-terminal device that allows current to flow primarily in one direction (forward bias) and blocks it in reverse bias. <!--SR:!2027-02-13,255,330!2026-11-03,170,310-->
- diode course role ::@:: The PN junction is the core building block inside BJTs and Zener regulators; diode I–V and biasing ideas transfer directly. <!--SR:!2027-02-13,255,330!2026-11-25,179,310-->
- schematic symbol: diode <p> ![diode symbol](attachments/symbol_diode.svg) ::@:: Diode symbol showing the one-way conduction element; current is intended to flow from anode to cathode when forward biased. <!--SR:!2027-01-24,239,330!fsrs,2027-05-09T08:41:43.251Z,330,329.54847456,1,2,7,0,0,2026-06-13T08:41:43.251Z-->

## pn junction and biasing

A PN junction diode is made by joining P-type and N-type semiconductor regions; at the junction a depletion region forms with a built-in barrier potential of about $0.7\text{ V}$ for silicon. The diode terminals are called anode (P side) and cathode (N side). When the anode is at a higher potential than the cathode (forward bias), the barrier is reduced and current can flow; when the anode is at a lower potential (reverse bias), the barrier increases and only a very small leakage current flows. On the physical diodes used in ELEC 1100, the cathode is marked by a stripe (often black) on the package, so "black strip is negative"; the small-signal diode is a thinner body, while the Zener diode used for regulation is a slightly fatter package but still uses the stripe to mark the cathode.

Biasing refers to how an external voltage connects to the diode. Conventional current flows from anode (+) to cathode (−) when forward biased. When reverse biased, the diode is modelled as an open circuit.

---

Flashcards for this section are as follows:

- pn junction formation ::@:: Joining P-type and N-type semiconductor regions; a depletion region forms at the junction. <!--SR:!fsrs,2027-05-09T08:41:30.969Z,330,329.54847456,1,2,7,0,0,2026-06-13T08:41:30.969Z!fsrs,2027-05-09T08:41:38.008Z,330,329.54847456,1,2,7,0,0,2026-06-13T08:41:38.008Z-->
- silicon barrier potential ::@:: About $0.7\text{ V}$ for a silicon PN junction. <!--SR:!fsrs,2027-05-12T08:41:45.700Z,333,332.56124433,1,2,7,0,0,2026-06-13T08:41:45.700Z!fsrs,2027-05-08T08:41:35.846Z,329,329.12637049,1,2,7,0,0,2026-06-13T08:41:35.846Z-->
- diode terminals ::@:: P side = anode; N side = cathode. <!--SR:!2027-02-03,247,330!2027-02-19,260,330-->
- forward vs reverse bias ::@:: Forward: anode at higher potential than cathode (current flows). Reverse: anode at lower potential (current blocked except leakage). <!--SR:!2027-01-25,240,330!fsrs,2027-05-10T08:41:40.686Z,331,331.0632816,1,2,7,0,0,2026-06-13T08:41:40.686Z-->
- conventional current direction ::@:: From anode (+) to cathode (−) when forward biased. <!--SR:!fsrs,2027-05-10T08:41:41.892Z,331,331.0632816,1,2,7,0,0,2026-06-13T08:41:41.892Z!2027-01-19,234,330-->
- lab diode orientation ::@:: Black stripe marks the cathode (negative end); connect it to the more negative node. <!--SR:!2027-02-04,248,330!fsrs,2027-04-11T01:11:13.939Z,309,308.57643926,1,2,7,0,0,2026-06-06T01:11:13.939Z-->

## diode i–v characteristic and models

The exact I–V curve is nonlinear, but circuit analysis uses simplified piecewise models. The ideal-diode model is a short circuit when forward biased and open when reverse biased. The constant-voltage model adds a $V_{\text{on}}\approx0.7\text{ V}$ drop when conducting: ON gives $V_D\approx0.7\text{ V}$, OFF gives $I_D\approx0$.

Analysis proceeds by assuming a diode state (ON or OFF), replacing it with the corresponding equivalent circuit, solving with [Kirchhoff's circuit laws](Kirchhoff%27s%20circuit%20laws.md) and Ohm's law, and checking consistency (whether $V_D$ and $I_D$ match the assumed region).

---

Flashcards for this section are as follows:

- ideal diode model ::@:: In the ideal model the diode is a short circuit when forward biased and an open circuit when reverse biased. <!--SR:!fsrs,2027-05-12T08:41:38.946Z,333,332.56124433,1,2,7,0,0,2026-06-13T08:41:38.946Z!2027-01-29,244,330-->
- constant-voltage model ::@:: $V_D\approx0.7\text{ V}$ for a conducting silicon diode. <!--SR:!2027-02-18,259,330!fsrs,2027-05-12T08:41:31.912Z,333,332.56124433,1,2,7,0,0,2026-06-13T08:41:31.912Z-->
- diode assumption method ::@:: Assume ON or OFF, replace with equivalent circuit (ON: $0.7\text{ V}$ drop; OFF: open), solve, check consistency. <!--SR:!fsrs,2027-05-09T08:41:32.812Z,330,329.54847456,1,2,7,0,0,2026-06-13T08:41:32.812Z!fsrs,2027-04-09T01:11:12.406Z,307,307.08504834,1,2,7,0,0,2026-06-06T01:11:12.406Z-->
- diode assumption check ::@:: If $V_D$ and $I_D$ are inconsistent with the assumed region, flip the assumption and re-solve. <!--SR:!2027-02-09,253,330!2027-01-18,233,330-->

## simple diode circuit analysis

For a series source–resistor–diode circuit, we can use the constant-drop model to find the current. If the supply voltage $V_S$ is less than about $0.7\text{ V}$, the diode is off and no current flows; the circuit behaves like an open switch. If $V_S$ exceeds $0.7\text{ V}$ and the diode is forward biased, we approximate $V_D\approx0.7\text{ V}$ and find $I_D\approx(V_S-0.7\text{ V})/R$ and $V_R\approx V_S-0.7\text{ V}$. <p> ![series source–resistor–diode circuit](attachments/series_diode_resistor.svg)

---

Flashcards for this section are as follows:

- series diode current <p> ![series source–resistor–diode circuit](attachments/series_diode_resistor.svg) ::@:: $I_D\approx(V_S-0.7\text{ V})/R$ when $V_S>0.7\text{ V}$ and forward biased. <!--SR:!fsrs,2027-05-10T08:41:36.969Z,331,331.0632816,1,2,7,0,0,2026-06-13T08:41:36.969Z!fsrs,2027-05-15T00:00:00.000Z,243,243.31710887,6.00214877,2,8,0,0,2026-09-14T00:00:00.000Z-->
- diode off condition <p> ![series source–resistor–diode circuit](attachments/series_diode_resistor.svg) ::@:: When $V_S<0.7\text{ V}$, the diode is off and $I_D\approx0$. <!--SR:!2027-02-08,252,330!fsrs,2027-04-11T01:11:13.223Z,309,308.57643926,1,2,7,0,0,2026-06-06T01:11:13.223Z-->

## diode safety in the lab

Include a series resistor (typically around $1\text{ k}\Omega$ in lab circuits) with a diode or LED; otherwise the current can become very large when the diode turns on, potentially damaging the diode, LED, or other components.

---

Flashcards for this section are as follows:

- series resistor with diode/LED ::@:: Limits current; without it, forward-biased current can become very large and damage components. <!--SR:!fsrs,2027-05-08T08:41:29.961Z,329,329.12637049,1,2,7,0,0,2026-06-13T08:41:29.961Z!fsrs,2027-04-09T01:09:04.603Z,307,307.08504834,1,2,7,0,0,2026-06-06T01:09:04.603Z-->
