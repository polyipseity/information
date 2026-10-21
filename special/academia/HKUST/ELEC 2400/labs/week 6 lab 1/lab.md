---
aliases:
  - ELEC 2400 week 6 lab 1 lab
  - ELEC2400 week 6 lab 1 lab
  - HKUST ELEC 2400 week 6 lab 1 lab
  - HKUST ELEC2400 week 6 lab 1 lab
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/labs/week_6_lab_1/lab
  - language/in/English
---

# lab

- HKUST ELEC 2400 week 6 lab 1
- parent: [week 6 lab 1](index.md)

## simulation workflow

Every circuit of the session is drawn in PSpice Schematics 9.1 and saved before it runs. `Draw >> Get New Part` opens the part browser, where the part name picks the element: `VSRC` for an independent voltage source, `VSIN` for a sinusoidal one, `ISRC` for a current source, `E` for a voltage-controlled voltage source, and `R`, `C`, and `L` for the passives. Ground is part `GND_EARTH`. Double-clicking a placed part opens its Property Editor, where a value such as a resistance or a source amplitude is typed without units, and `Edit >> Rotate` turns a part. `Draw >> Wire` joins terminals with the pencil cursor.

`Markers >> Mark Voltage/Level` plants the probes whose node voltages appear in the plots, and `Markers >> Mark Current into Pin` selects a pin current. `Analysis >> Setup` chooses the analysis: a Bias Point Detail run for the DC operating point, a Transient run for waveforms against time, or an AC Sweep for response against frequency. `Analysis >> Simulate` executes it, the bias voltage and bias current display icons print the operating-point values straight onto the schematic, and waveform results open in the OrCAD PSpice A/D window.

---

Flashcards for this section are as follows:

- part names: which PSpice part names place the sources and passives of the session's circuits? ::@:: `VSRC` for a voltage source, `VSIN` for a sinusoidal source, `ISRC` for a current source, `E` for a voltage-controlled voltage source, and `R`, `C`, `L` for the passives, with `GND_EARTH` for ground.
- property values: how is a part's value set in PSpice, and what is left out of the entry? ::@:: Double-click the part and type the value in the Property Editor's Value field, with no unit typed.
- what the markers decide: two simulation runs of the same schematic plant different markers; what changes between them? ::@:: The markers decide which node voltages or pin currents the simulation reports and plots.
- analysis choice: which analysis setup returns the DC operating point printed on the schematic? ::@:: The Bias Point Detail analysis, with the bias voltage and bias current display icons showing the values on the schematic.
- before simulate: what must happen to a schematic before `Analysis >> Simulate` runs it? ::@:: The schematic is saved: the simulation runs the saved design.
- results window: where do transient and AC waveforms appear after a run? ::@:: In the OrCAD PSpice A/D window opened by `Analysis >> Simulate`.

## verifying Kirchhoff's laws

Two operating-point circuits put simulated numbers behind [Kirchhoff's circuit laws](../../Kirchhoff%27s%20circuit%20laws.md). The current-law circuit runs three branches down from a top node labelled $V_1$: a 3 A current source in series with a $4\ \Omega$ resistor on the left, a $5\ \Omega$ resistor in the middle with $I_2$ defined upward through it, and a $2\ \Omega$ resistor on the right with $I_1$ defined upward through it, its foot grounded. A 4 A current source lies on the bottom wire between the middle and right branches, pointing left. The Bias Point Detail run returns $I_1$, $I_2$, and $V_1$.

The voltage-law circuit is a single loop. Up the left branch sit a $4\ \Omega$ resistor and a 2 V source, with node $V_2$ above the source. Across the top sit a 3 V source and a $10\ \Omega$ resistor in series, and down the right branch a 5 V source carries $I_3$ defined upward through it. The bottom wire closes the loop at ground. The same analysis returns $I_3$ and $V_2$.

Summed at the node and round the loop with their marked directions, the simulated currents and voltages close the way the two laws state, which is what the verification checks.

---

Flashcards for this section are as follows:

- what the operating point returns: which quantities does the Bias Point Detail run give for the two verification circuits? ::@:: For the current-law circuit the currents $I_1$ and $I_2$ and the node voltage $V_1$; for the voltage-law circuit the current $I_3$ and the node voltage $V_2$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- current-law directions: how are the branch currents marked in the current-law circuit? ::@:: $I_1$ points upward through the $2\ \Omega$ right branch and $I_2$ upward through the $5\ \Omega$ middle branch, with the 4 A source pointing left along the bottom wire. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- voltage-law loop: which elements sit in series around the single loop of the voltage-law circuit? ::@:: A $4\ \Omega$ resistor and a 2 V source up the left branch, a 3 V source and a $10\ \Omega$ resistor across the top, and a 5 V source down the right branch, closed by the bottom wire at ground. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- what the check compares: the simulation returns branch currents and node voltages at the DC operating point; what do they verify? ::@:: They let the currents at a node be summed against Kirchhoff's current law and the voltages round the loop against Kirchhoff's voltage law.

<!-- check: ignore-next-line[header_style]: proper noun -->
## Thévenin equivalent by simulation

The circuit at the terminal pair $ab$ carries five elements. On the left a 4 A current source points down through a $2\ \Omega$ resistor to ground, and an $8\ \Omega$ resistor crosses the top to a central node. A central branch holds a $4\ \Omega$ resistor above a 4 V source with its plus mark up. A $4\ \Omega$ resistor lies on the bottom wire back to the grounded left corner, and a $3\ \Omega$ resistor runs from the central node to terminal $a$. The $2\ \Omega$ load runs from $a$ down to $b$ on the bottom wire, with $I_o$ defined downward through it, and [Thévenin's theorem](../../Th%C3%A9venin%27s%20theorem.md) predicts that this whole network collapses to one source and one resistance at that pair.

Three runs build the equivalent. With the load in place the run returns the load voltage $V_{ab}$. Removing the $2\ \Omega$ load and replacing the $3\ \Omega$ resistor with a wire, which keeps the simulation from erroring, returns the open-circuit voltage $V_{OC}$ at terminals $a$ and $b$. Replacing the load itself with a wire, with the $3\ \Omega$ back in place, returns the short-circuit current $I_{SC}$ from $a$ to $b$, and the ratio $R_{eq} = V_{OC} / I_{SC}$ is the equivalent resistance.

The equivalent circuit carries the result: $V_{OC}$ in series with $R_{eq}$ across the same $2\ \Omega$ load. The computed $I_o$ and $V_{ab}$ from that one-source circuit reproduce the simulated values of the full circuit, which is the theorem checked end to end.

---

Flashcards for this section are as follows:

- equivalent resistance: which two simulated quantities give the Thévenin equivalent resistance? ::@:: $R_{eq} = V_{OC} / I_{SC}$, the open-circuit voltage at the terminal pair over the short-circuit current through it. <!-- check: ignore-line[two_sided_calc_warning]: formula flashcard -->
- the two removals: how are $V_{OC}$ and $I_{SC}$ produced from the one schematic? ::@:: Removing the $2\ \Omega$ load, with the $3\ \Omega$ replaced by a wire, gives $V_{OC}$ at open terminals $a$ and $b$; replacing the load with a wire, with the $3\ \Omega$ back in place, gives $I_{SC}$ from $a$ to $b$.
- the wire in the load path: the $3\ \Omega$ resistor is shorted for the open-circuit run but present for the short-circuit run; why does each run want it that way? ::@:: The open-circuit run needs no dangling branch to trip the simulation, while the short-circuit run must keep the $3\ \Omega$ in the path so $I_{SC}$ flows through the real circuit.
- what the verification shows: the equivalent circuit's computed $I_o$ and $V_{ab}$ are compared with the full circuit's simulated ones; what does their agreement establish? ::@:: The single source $V_{OC}$ in series with $R_{eq}$ reproduces the original network at the load terminals, which is Thévenin's theorem for this circuit.

## circuit with a dependent source

The dependent-source circuit ties a source's value to a voltage elsewhere in its own circuit. Node $V_4$ is the top node. An $8\ \Omega$ resistor leaves it to the left and drops to ground, and a central branch of a $3\ \Omega$ resistor above a dependent source of value $4V_3$ lands on the grounded bottom node. A 6 V source with its plus mark up drops from $V_4$ to the bottom wire on the right. A $5\ \Omega$ resistor lies on that bottom wire between the central branch's foot and the right branch's foot, and $V_3$, minus at the left and plus at the right, is its voltage. The controlled source is part `E` with gain 4, so the branch source equals four times the resistor's voltage.

A Bias Point Detail run returns the node voltages, $V_4$ among them. The loop currents set $V_3$ across the $5\ \Omega$ resistor, and the dependent source multiplies whatever they set, so [a voltage-controlled voltage source](../../dependent%20source.md#voltage-controlled%20voltage%20source) in the simulation keeps its value and its controlling voltage tied together at the operating point.

---

Flashcards for this section are as follows:

- controlling quantity: the gain-4 dependent source is set by the voltage across the $5\ \Omega$ resistor on the bottom wire; which voltage is that, and where does it appear? ::@:: $V_3$, minus at the left and plus at the right.
- part and gain: how is the voltage-controlled voltage source entered in PSpice for this circuit? ::@:: As part `E` with gain 4, so the central branch's source equals $4V_3$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- what reaches node V4: which branches leave the top node of the dependent-source circuit? ::@:: The $8\ \Omega$ resistor dropping to ground on the left, the $3\ \Omega$ resistor above the $4V_3$ dependent source in the centre, and the 6 V source on the right. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- operating point: which quantities does the Bias Point Detail run report for the dependent-source circuit? ::@:: The node voltages at the operating point, $V_4$ among them, with $V_3$ across the $5\ \Omega$ resistor setting the dependent source. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## transient simulation and resonance

The AC circuit drives a parallel tank. The source $v_4(t) = 4\sin(2\pi \cdot 50\text{k} \cdot t)\ \text{V}$ sits with its lower terminal grounded, a $1\ \text{k}\Omega$ resistor links its top to the output node, and three elements hang from that node to ground in parallel: a $1\ \text{k}\Omega$ resistor, a $1\ \mu\text{F}$ capacitor, and a $1\ \text{mH}$ inductor. The output voltage $v_o(t)$ is the tank's voltage.

A Transient run of the circuit needs its `VSIN` part carrying the DC value, the amplitude (VAMPL), the frequency (FREQ), and the offset (VOFF), and the run's No-PRINT delay, final time, and step ceiling are set for a readable waveform. The simulated output keeps the driving shape, $v_o(t) = V_m \sin(2\pi \cdot 50\text{k} \cdot t + \theta_v)$, with the amplitude $V_m$ and the phase offset $\theta_v$ read off the plot. The drive at 50 kHz sits far above the tank's resonance, where the capacitor's reactance is a few ohms, far below the inductor's, so the tank's impedance and with it $v_o$ stay a small fraction of the source.

An AC Sweep run takes over for the frequency axis. The source's AC value is set to $2.828 = 4/\sqrt{2}$, the 4 V amplitude's root mean square (RMS) value, and the sweep runs by decades from 1 kHz to 1 MHz with 100 points per decade. The output peaks where the inductor and capacitor resonate at $f_0 = 1/(2\pi\sqrt{LC})$, about $5\ \text{kHz}$ for $1\ \text{mH}$ and $1\ \mu\text{F}$, and with the ideal tank open at that frequency the two $1\ \text{k}\Omega$ resistors split the source evenly, putting the maximum at half the AC value.

---

Flashcards for this section are as follows:

- VSIN properties: which properties of the sinusoidal source are typed before the Transient run? ::@:: The DC value, the amplitude (VAMPL), the frequency (FREQ), and the offset (VOFF).
- transient settings: which Transient settings shape the saved waveform of the parallel-tank circuit? ::@:: The No-PRINT delay deciding when data starts being saved, the final time, and the step ceiling setting the step size.
- output form: what shape does the Transient simulation give for $v_o(t)$? ::@:: $v_o(t) = V_m \sin(2\pi \cdot 50\text{k} \cdot t + \theta_v)$, the driving sine with its own amplitude and phase offset.
- why 2.828: the AC Sweep setup sets the source's AC value to $2.828$ for a $4\text{ V}$ sine; what is that number? ::@:: The root mean square (RMS) value of the $4\text{ V}$ amplitude sine, $4/\sqrt{2} \approx 2.828$.
- resonant frequency: which frequency peaks in the sweep, in terms of the parallel $L$ and $C$? For $L = 1\ \text{mH}$ and $C = 1\ \mu\text{F}$, which frequency is that? ::@:: $f_0 = 1/(2\pi\sqrt{LC})$, about $5\ \text{kHz}$ for those values.
- maximum at resonance: why does the output reach half the AC source value at resonance, with two $1\ \text{k}\Omega$ resistors in the circuit? ::@:: The ideal parallel inductor and capacitor draw no net current at $f_0$, so the tank opens and the two $1\ \text{k}\Omega$ resistors split the source evenly.
- sweep range: how is the AC Sweep of the parallel-tank circuit configured? ::@:: Decade scaling from 1 kHz to 1 MHz with 100 points per decade, sourced at the RMS value $2.828\ \text{V}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
