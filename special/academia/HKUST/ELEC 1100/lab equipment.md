---
aliases:
  - ELEC 1100 breadboard
  - breadboard
  - breadboards
  - lab equipment
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1100/lab_equipment
  - language/in/English
---

# lab equipment

Lab sessions in ELEC 1100 use a breadboard to build circuits without soldering. Core instruments include a DC power supply, digital multimeter (DMM), function generator, and digital storage oscilloscope (DSO). This note summarises breadboard layout and safe use of equipment so you can complete Lab 1 and later labs confidently.

---

Flashcards for this section are as follows:

- breadboard and lab equipment purpose ::@:: In ELEC 1100 labs you build circuits on a breadboard and use a DC supply, DMM, function generator, and DSO as the main instruments.
- lab 1 relevance ::@:: Lab 1 focuses on setup and component check; breadboard structure and equipment usage are covered in this topic and in [electronic component](electronic%20component.md).

## equipment overview

The standard lab bench provides a **DC power supply** (one or two channels) for constant voltage to power the breadboard rails; you set the output voltage and often a current limit—never short the supply outputs. A **function generator** produces AC waveforms (sine, square, triangle) with adjustable amplitude (e.g. peak-to-peak voltage) and frequency (e.g. Hz or kHz); you use it in later labs for diode and rectifier circuits and view the waveform on the DSO. In lab you normally press the function generator's reset or _default setup_ key at the start of an experiment to clear any hidden user settings, and you connect the probe or BNC cable to the **FUNCTION** output (not the TTL or sync output). A **digital multimeter** (DMM) measures voltage, current, or resistance depending on mode and connection. A **digital storage oscilloscope** (DSO) displays voltage versus time and can show amplitude, period, and frequency of signals. The breadboard is the platform on which you plug components and jumper wires to form circuits. For regulated $5\text{ V}$ (and $12\text{ V}$ motor) rails in the project see [voltage regulator](voltage%20regulator.md).

---

Flashcards for this section are as follows:

- lab equipment list ::@:: DC power supply, digital multimeter (DMM), function generator, and digital storage oscilloscope (DSO) are the core lab instruments; the breadboard is where you build the circuit.
- DC power supply role ::@:: The DC power supply provides constant voltage (one or two channels) to power the breadboard rails; set voltage and current limit and never short the outputs.
- function generator role ::@:: The function generator produces AC waveforms (sine, square, triangle) with adjustable amplitude and frequency; used in later labs for diode/rectifier circuits and viewed on the DSO.
- function generator lab setup ::@:: At the start of a lab you normally reset the function generator (e.g. _default setup_) to clear old settings and connect the probe or BNC lead to the FUNCTION output, not the TTL or sync output.
- digital multimeter (DMM) role ::@:: The digital multimeter measures voltage, current, or resistance depending on mode and connection.
- digital storage oscilloscope (DSO) role ::@:: The digital storage oscilloscope displays voltage versus time and can show amplitude, period, and frequency of signals.

## breadboard structure and connections

Historically, experimenters used literal wooden bread boards and nailed components to them; modern breadboards use a plastic (insulating) body with internal metal strips that act as conductors. Row holes are grouped in sets of five that are connected internally; long power-rail columns run along the edges and are connected along their length. Adjacent columns are not connected, so you must use jumper wires to connect different rows or columns. Knowing which holes share a connection is essential to avoid short circuits and to build circuits correctly.

---

Flashcards for this section are as follows:

- breadboard materials ::@:: Modern breadboards use plastic (insulator) and internal metal strips (conductor); historically wooden boards were used.
- breadboard row connections ::@:: Groups of five holes in a row are internally connected; components or wires in the same row share a node.
- breadboard power rails ::@:: Long columns along the edges are power rails; all holes in one column are connected along its length.
- breadboard adjacent columns ::@:: Adjacent columns are not connected; use jumper wires to connect between rows or columns.

## component symbols and power rails

Schematic symbols on lab handouts indicate power rails ($+5\text{ V}$, GND), voltage sources, resistors, capacitors, and LEDs. On the breadboard you assign one rail to $+5\text{ V}$ (or the supply voltage) and another to ground; all points connected to the same rail are at the same potential. See [electronic component](electronic%20component.md) for resistor, capacitor, and ground symbols.

---

Flashcards for this section are as follows:

- power rails on breadboard ($+5\text{ V}$, GND) ::@:: One rail is tied to the positive supply (e.g. $+5\text{ V}$) and another to ground (GND); all holes on that rail share the same voltage.
- schematic symbols in lab ::@:: Handouts use symbols for voltage sources, resistors, capacitors, LEDs, and connections; see the electronic component topic for definitions.

## resistor colour code

Axial resistors use coloured bands to indicate resistance value and tolerance. On a **4-band** resistor, read from the end that has the tolerance band (usually gold or silver) at one end: the **first two bands** are digits (0–9), the **third band** is the multiplier (power of 10), and the **fourth band** is the tolerance. In **5-band** code (tutorial slides), the **first three bands** are digits, the **fourth** is the multiplier, and the **fifth** is the tolerance.

| Colour | Digit | Multiplier                      | Tolerance   |
| ------ | ----- | ------------------------------- | ----------- |
| Pink   | —     | $\times0.001$ ($\times10^{-3}$) | —           |
| Silver | —     | $\times0.01$ ($\times10^{-2}$)  | $\pm10\%$   |
| Gold   | —     | $\times0.1$ ($\times10^{-1}$)   | $\pm5\%$    |
| Black  | 0     | $\times1$ ($\times10^0$)        | —           |
| Brown  | 1     | $\times10$ ($\times10^1$)       | $\pm1\%$    |
| Red    | 2     | $\times100$ ($\times10^2$)      | $\pm2\%$    |
| Orange | 3     | $\times1000$ ($\times10^3$)     | $\pm0.05\%$ |
| Yellow | 4     | $\times10^4$                    | $\pm0.02\%$ |
| Green  | 5     | $\times10^5$                    | $\pm0.5\%$  |
| Blue   | 6     | $\times10^6$                    | $\pm0.25\%$ |
| Violet | 7     | $\times10^7$                    | $\pm0.1\%$  |
| Grey   | 8     | $\times10^8$                    | $\pm0.01\%$ |
| White  | 9     | $\times10^9$                    | —           |

Examples (4-band): **brown–black–orange–gold** = 1, 0, $\times1\text{ k}$, $\pm5\%$ → $10\text{ k}\Omega$ $\pm5\%$. **Red–red–brown–gold** = 2, 2, $\times10$, $\pm5\%$ → $220\,\Omega$ $\pm5\%$. **Yellow–violet–orange–gold** = 4, 7, $\times1\text{ k}$, $\pm5\%$ → $47\text{ k}\Omega$ $\pm5\%$.

**5-band code** (used in the tutorial slides): use the table above; band positions are three digits, then multiplier, then tolerance. **5-band example 2–3–7–1%:** digits 2, 3, 7, multiplier $\times1$ (black), tolerance $\pm1\%$ (brown) → $R=237\times1\,\Omega=237\,\Omega$ $\pm1\%$. So red–orange–violet–black–brown (5-band) = $237\,\Omega$ $\pm1\%$. **5-band example brown–black–black–brown–brown:** = 1, 0, 0, $\times10$, $\pm1\%$ → $1\text{ k}\Omega$ $\pm1\%$.

---

Flashcards for this section are as follows:

- resistor colour code: 4-band order ::@:: Band 1–2 = digits, band 3 = multiplier, band 4 = tolerance. Read from the end where the tolerance band (e.g. gold/silver) sits.
- resistor colour code: 5-band order ::@:: Bands 1–3 = digits, band 4 = multiplier, band 5 = tolerance. Same table; used in the tutorial slides.
- resistor colour code: digit column (table) ::@:: Black 0 through white 9 (order: black, brown, red, orange, yellow, green, blue, violet, grey, white). Pink, silver, gold have no digit (—).
- resistor colour code: multiplier column (e.g. pink $\times0.001$, gold $\times0.1$, black $\times1$) ::@:: Pink $\times0.001$, silver $\times0.01$, gold $\times0.1$; black $\times1$ through white $\times10^9$ (same order as digits). Use the table for the exact multiplier.
- resistor colour code: tolerance column (e.g. silver $\pm10\%$, gold $\pm5\%$, brown $\pm1\%$) ::@:: Silver $\pm10\%$, gold $\pm5\%$; brown $\pm1\%$, red $\pm2\%$, orange $\pm0.05\%$, yellow $\pm0.02\%$, green $\pm0.5\%$, blue $\pm0.25\%$, violet $\pm0.1\%$, grey $\pm0.01\%$. Black, white, pink: no tolerance (—).
- resistor colour code 4-band example: brown–black–orange–gold (1, 0, $\times1000$, $\pm5\%$) → $R$? ::@:: $R=10\text{ k}\Omega$ $\pm5\%$.
- resistor colour code 4-band example: red–red–brown–gold (2, 2, $\times10$, $\pm5\%$) → $R$? ::@:: $R=220\,\Omega$ $\pm5\%$.
- resistor colour code 5-band example: red–orange–violet–black–brown (2,3,7, $\times1$, $\pm1\%$) → $R$? ::@:: $R=237\,\Omega$ $\pm1\%$.
- resistor colour code 5-band example: brown–black–black–brown–brown (1,0,0, $\times10$, $\pm1\%$) → $R$? ::@:: $R=1\text{ k}\Omega$ $\pm1\%$.

## reading the DSO

The digital storage oscilloscope (DSO) displays **voltage on the vertical axis** and **time on the horizontal axis**. Before taking any reading, check the **scale** (and units) for each axis.

- **Vertical axis (voltage):** Each division on the screen corresponds to a voltage step set by the vertical scale (e.g. $1\text{ V}/\text{div}$, $500\text{ mV}/\text{div}$). The on-screen display usually shows the scale in V or mV. To read **peak-to-peak voltage** $V_{\text{pp}}$: count the number of vertical divisions from the minimum to the maximum of the waveform and multiply by the volts-per-division. For a **DC level** or **mean value**, read the vertical position of the flat part (or use the DSO's built-in mean/DC measurement if available).
- **Horizontal axis (time):** Each division corresponds to a time step (e.g. $1\text{ ms}/\text{div}$, $100\,\mu\text{s}/\text{div}$). Units may be s, ms, or $\mu\text{s}$. To find the **period** $T$ of a periodic waveform: count the number of horizontal divisions for one complete cycle and multiply by the time-per-division. **Frequency** is $f=1/T$ (unit Hz or kHz); many DSOs display frequency directly, but always verify the scale so you know whether the reading is in Hz, kHz, or MHz.
- **Trigger:** The trigger stabilises the display so that a repeating waveform appears stationary. Set the trigger source (e.g. channel 1), trigger level, and slope (rising or falling) as indicated in the tutorial; if the trace is running or jumping, adjust the trigger level until the waveform locks.
- **Interpret units:** Always note whether the vertical scale is in V or mV and whether the horizontal scale is in s, ms, or $\mu\text{s}$ so that peak-to-peak, period, and frequency are read with the correct magnitude.
- **Probe connections:** In the lab, always connect the DSO probe clip (negative) to the circuit's reference node marked GND in the schematic, and touch the probe tip to the metal at the bottom of component leads instead of pushing it directly into breadboard holes so the contacts are not damaged.

---

Flashcards for this section are as follows:

- DSO vertical axis (volts/div, V/mV, $V_{\text{pp}}$) ::@:: Voltage; each division = volts (or mV) per division; check on-screen scale (V/mV) before reading amplitude or $V_{\text{pp}}$.
- DSO horizontal axis (time/div, s/ms/μs, period $T$) ::@:: Time; each division = time per division (s/ms/μs); use it to read period $T$ of one cycle.
- DSO peak-to-peak ($V_{\text{pp}}$): how to read? ::@:: Count vertical divisions from waveform minimum to maximum and multiply by volts-per-division; units V or mV.
- DSO period and frequency ($T$, $f=1/T$, units) ::@:: Period $T$ = horizontal divisions for one cycle $\times$ time-per-division; frequency $f=1/T$ (Hz or kHz); check time scale units (s/ms/μs).
- DSO trigger purpose ::@:: Trigger stabilises the display so a repeating waveform appears stationary; set source, level, and slope as in the tutorial.
- DSO units reminder (vertical V/mV, horizontal s/ms/μs, Hz/kHz; $V_{\text{pp}}$, period, frequency) ::@:: Always check on-screen units for vertical (V/mV) and horizontal (s/ms/μs, Hz/kHz) when reading $V_{\text{pp}}$, period, or frequency.
- DSO probe connection and ground ::@:: In ELEC 1100 labs, connect the DSO probe clip (negative) to the circuit reference node marked GND in the diagram and touch the probe tip to the bottom of component leads rather than jamming it into breadboard holes to avoid damaging contacts.

## LED <!-- check: ignore-line[header_style]: proper noun -->

An LED must be used with a series resistor (typically about $1\text{ k}\Omega$ at $5\text{ V}$) to limit current and avoid damage; see [simple diode circuit analysis and safety](diode.md#simple%20diode%20circuit%20analysis%20and%20safety) in the diode topic. Resistor values are read from the [resistor colour code](#resistor%20colour%20code); the DSO is used as in [reading the DSO](#reading%20the%20DSO).

---

Flashcards for this section are as follows:

- LED series resistor (e.g. $1\text{ k}\Omega$ at $5\text{ V}$) ::@:: Always use a series resistor (e.g. $1\text{ k}\Omega$ at $5\text{ V}$) with an LED to limit current and prevent damage.
- resistor colour code example 5-band (e.g. 2–3–7–1% → $R=237\,\Omega$) ::@:: 5-band: bands 2–3–7–1% (red–orange–violet–black–brown) give $R=237\,\Omega$ $\pm1\%$.
- DSO scales ::@:: On the DSO, vertical divisions are voltage and horizontal divisions are time; check on-screen units (V/mV, s/ms, Hz/kHz) when reading values.

## lab safety

Never short the power rails or reverse power and ground. When you finish a measurement or are about to rewire a circuit, turn off the DC power supply or disable its output and use the current-limit knob as described in lab to protect your circuit from accidental overcurrent. In ELEC 1100 experiments you normally ignore the bench supply's GND binding post: treat the negative terminal in the circuit diagram as the reference node (GND) and connect the negative leads of the DMM, DSO probes, and function generator there instead of to the supply's chassis ground. If readings look wrong or you smell burning, turn off the supply immediately and ask a TA.

---

Flashcards for this section are as follows:

- lab safety rules ::@:: Do not short the rails or reverse power and ground; turn off the supply and ask a TA if something smells or readings are wrong.
- DC supply and reference node safety ::@:: After measurements or before rewiring, turn off or disable the DC supply output and rely on the current limit to protect circuits; in ELEC 1100 labs use the circuit's GND node as the common reference for negative leads rather than the bench supply's chassis GND terminal.
