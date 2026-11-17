---
aliases:
  - ELEC 2400 week 5 lab 1 lab
  - ELEC2400 week 5 lab 1 lab
  - HKUST ELEC 2400 week 5 lab 1 lab
  - HKUST ELEC2400 week 5 lab 1 lab
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/labs/week_5_lab_1/lab
  - language/in/English
---

# lab

- HKUST ELEC 2400 week 5 lab 1
- parent: [week 5 lab 1](index.md)

## waveforms on two channels

A triangle wave swinging $-1.5\text{ V}$ to $1.5\text{ V}$ at 1 kHz from the function generator reaches channel A of the oscilloscope through a ×10 probe in direct-current (DC) mode. Channel B, behind a ×10 probe in DC mode as well, takes the steady output of a battery box holding three AA cells, about $4.5\text{ V}$; a DC power supply set to $4.5\text{ V}$ does the same job.

Displayed on its own, the triangle wave repeats at the 1 kHz its generator setting promises, which the oscilloscope reading confirms before the channels combine. A labelled sketch carries the record.

The oscilloscope's math mode adds the two channels: the `A + B` option sums them sample by sample. A steady $4.5\text{ V}$ on channel B lifts the channel-A triangle by that much without stretching it in time, so the resultant keeps the 1 kHz repetition rate while riding at the higher level. The result is sketched with its labels and its frequency read off the display.

---

Flashcards for this section are as follows:

- channel setup: the 1 kHz triangle wave of $\pm 1.5\text{ V}$ and the battery box's steady $4.5\text{ V}$ reach the two channels of the oscilloscope; which channel takes which signal, and behind which probe? ::@:: The triangle wave reaches channel A and the steady level reaches channel B, both through ×10 probes in direct-current (DC) mode.
- sum of a triangle and a constant: channel A carries a 1 kHz triangle wave and channel B a steady $4.5\text{ V}$; what does the `A + B` display show? ::@:: The same triangle lifted by $4.5\text{ V}$, repeating at the unchanged 1 kHz rate.
- frequency of a sum: a 1 kHz triangle wave and a direct-current (DC) level are added sample by sample; what happens to the repetition rate? ::@:: It stays at 1 kHz: a constant offset moves the waveform up without changing its period.
- battery box: the steady channel-B signal reads about $4.5\text{ V}$; how is it produced? ::@:: Three AA cells in the battery box with their terminals joined by the crocodile clip cable, or a DC power supply set to $4.5\text{ V}$.

## alternating-current readings on a multimeter

A square wave, a triangle wave, and a sine wave, each swinging $-1.5\text{ V}$ to $1.5\text{ V}$ at 1 kHz, are set on the oscilloscope in direct-current (DC) mode and then read at the function generator's output by the digital multimeter in alternating-current voltage mode (ACV).

Every ACV reading is a root mean square (RMS) value, and the meters differ in how honestly they report one: a true-RMS meter works from the signal's power, while a meter that scales the peak by a sine-fitted factor is right for sines alone. [multimeter § alternating-current readings](../../multimeter.md#alternating-current%20readings)

The three waveforms share an amplitude yet carry different RMS values: $V_m$ for the square wave, $V_m/\sqrt{3}$ for the triangle wave, and $V_m/\sqrt{2}$ for the sine wave. The three meter readings separate in that same order, and each measured value is set against its waveform's formula.

---

Flashcards for this section are as follows:

- RMS by waveform: three waveforms share the amplitude $V_m$; which root mean square (RMS) value does each carry? ::@:: The square wave carries $V_m$, the triangle wave $V_m/\sqrt{3}$, and the sine wave $V_m/\sqrt{2}$.
- meter mode: which multimeter mode reads the AC output of the function generator? ::@:: The alternating-current voltage mode (ACV), whose reading is a root mean square (RMS) value.
- same amplitude, different readings: a square wave, a triangle wave, and a sine wave of the same $\pm 1.5\text{ V}$ amplitude at 1 kHz are each read on the alternating-current voltage mode (ACV); why do the readings differ? ::@:: Each waveform carries a different root mean square (RMS) value for the same amplitude, and the meter reports that value.
- sine-scaled meters: why can a reading of a square wave on the alternating-current voltage mode (ACV) disagree with the true value? ::@:: A meter that scales the peak by a sine-fitted factor is right only for sines, while a true root mean square (RMS) meter works from the signal's power instead.

## loading effect

Two dividers run side by side off one supply, the pattern [loading a divider](../../voltage%20divider.md#loading%20a%20divider) describes. A battery box with four AA cells, about $6\text{ V}$, or a DC power supply set to $6\text{ V}$, feeds node C. The first divider, $R_1 = R_2 = 1\ \text{M}\Omega$, carries node A between its resistors; the second, $R_3 = R_4 = 1\ \text{k}\Omega$, carries node B. The instrument stands at whichever node is being read, its input resistance landing in parallel with that divider's lower resistor, and the drawing shows it at node B. <p> ![two dividers off one source: R1 and R2 in series with node A between them, R3 and R4 in series with node B between them, and the instrument drawn as its input resistance Rin across node B](attachments/loading_effect_circuit.svg)

Three readings follow in turn. The digital multimeter in direct-current voltage mode (DCV) reads node C, then node A, then node B. The oscilloscope with a direct ×1 probe repeats nodes A and B, and the ×10 probe, switched at the probe and matched by the ×10 setting on the scope, repeats them once more.

A reading equals the divider's arithmetic only while the instrument draws no current of its own. Every instrument brings an input resistance to the node, and that resistance in parallel with the lower divider resistor pulls the combination below $R_2$ or $R_4$, so the reading falls with it. The $1\ \text{M}\Omega$ divider feels the effect most, because an instrument's input resistance stands comparable to its own resistances, while $1\ \text{k}\Omega$ lies far below any of them and barely moves. The ×10 probe lifts the oscilloscope's input resistance tenfold, so its reading sits closer to the unloaded value than the ×1-probe reading does.

Whichever values the session recorded, the causal chain orders them: an instrument whose input resistance sits far above the divider's resistances reads close to the unloaded voltage, one whose input resistance is comparable pulls the reading down, and the ×10 probe moves a sagging reading back up.

---

Flashcards for this section are as follows:

- loading-effect hookup: in the circuit shown, two dividers with $R_1 = R_2$ and $R_3 = R_4$ share one supply; which nodes does the circuit define, and where does the instrument stand? ::@:: Node C at the supply, node A between $R_1$ and $R_2$, and node B between $R_3$ and $R_4$; the instrument stands at the node being read, drawn at node B with its input resistance across that divider.
- draw the loading-effect hookup: what are the two dividers and the instrument connection of the loading-effect circuit, fed at about $6\text{ V}$? ::@:: ![two dividers off one source: R1 and R2 in series with node A between them, R3 and R4 in series with node B between them, and the instrument drawn as its input resistance Rin across node B](attachments/loading_effect_circuit.svg) Two dividers share the supply: $R_1 = R_2 = 1\ \text{M}\Omega$ with node A between, $R_3 = R_4 = 1\ \text{k}\Omega$ with node B between, and the instrument's input resistance stands at the node being read, drawn across node B. The supply is about $6\text{ V}$, from four AA cells in the battery box or a DC power supply at node C.
- why readings fall: a meter reading a divider node draws some current of its own; what does that do to the reading? ::@:: The meter's input resistance lands in parallel with the divider's lower resistor, so the effective resistance and the node voltage both fall below the unloaded value.
- which divider suffers: one divider uses $R_1 = R_2 = 1\ \text{M}\Omega$ at node A and the other $R_3 = R_4 = 1\ \text{k}\Omega$ at node B; where does an instrument load most? ::@:: At node A: the instrument's input resistance is comparable to $1\ \text{M}\Omega$, while $1\ \text{k}\Omega$ at node B lies far below it.
- ×10 probe: how does the ×10 probe change a loading-affected reading? ::@:: It raises the oscilloscope's input resistance tenfold, so less current is drawn and the reading sits closer to the unloaded divider voltage.

## bandwidth of a multimeter

A $4\text{ V}$ peak-to-peak sine wave starts at $100\text{ Hz}$ on the function generator, and the digital multimeter in alternating-current voltage mode (ACV) reads the generator's output. The frequency then climbs through the tabulated steps, $500\text{ Hz}$, $1\text{ kHz}$, $1.2\text{ kHz}$ and onward to $20\text{ kHz}$, with the meter's reading recorded at each one.

The results go onto semi-logarithmic graph paper by hand, frequency on the logarithmic axis. The reading holds flat while the frequency sits well inside the meter's [bandwidth](../../multimeter.md#bandwidth) and sags as the frequency approaches it.

The bandwidth is read off the plot where the reading has fallen to $0.707$ of its low-frequency value, the same criterion an instrument's specification uses. A typical multimeter bandwidth is around 10 kHz, and the plot estimates this meter's own figure against that typical value.

---

Flashcards for this section are as follows:

- sweep settings: the frequency sweep runs from $100\text{ Hz}$ through the tabulated steps to $20\text{ kHz}$, read at each step on the alternating-current voltage mode (ACV); which signal is stepped across it? ::@:: A $4\text{ V}$ peak-to-peak sine wave.
- plotting the roll-off: the meter's readings are tabulated against frequency from $100\text{ Hz}$ to $20\text{ kHz}$; how is the graph drawn? ::@:: By hand on semi-logarithmic graph paper, with the frequency on the logarithmic axis.
- bandwidth from the plot: the meter's readings are plotted by hand against frequency; how is the estimated bandwidth read off the curve? ::@:: At the frequency where the reading has fallen to $0.707$ of its low-frequency value. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- what the roll-off means: the reading on the alternating-current voltage mode (ACV) sags as the driving frequency climbs; what does that indicate about the meter? ::@:: The frequency has approached the meter's bandwidth, beyond which its readings are attenuated rather than reliable.
- typical figure: what order of bandwidth does a digital multimeter usually have? ::@:: Around 10 kHz, so a signal of a few hundred hertz and above is measured on the oscilloscope instead.
