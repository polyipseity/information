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

Lab sessions in ELEC 1100 use a breadboard to build circuits without soldering. Core instruments include a DC power supply, digital multimeter (DMM), function generator, and digital storage oscilloscope (DSO). This note summarises breadboard layout and safe use of equipment so you can complete Lab 1 and later labs.

---

Flashcards for this section are as follows:

- lab equipment overview ::@:: In ELEC 1100 labs you build circuits on a breadboard using a DC supply, DMM, function generator, and DSO. <!--SR:!fsrs,2027-05-12T08:38:15.346Z,333,332.56124433,1,2,7,0,0,2026-06-13T08:38:15.346Z!fsrs,2027-04-06T01:15:36.625Z,304,303.62086325,1,2,7,0,0,2026-06-06T01:15:36.625Z-->
- lab 1 relevance ::@:: Lab 1 covers setup and component check; see also [electronic component](electronic%20component.md). <!--SR:!fsrs,2027-04-06T01:21:18.740Z,304,304.04690879,1,2,7,0,0,2026-06-06T01:21:18.740Z!fsrs,2027-04-01T01:21:11.511Z,299,298.72647102,1,2,7,0,0,2026-06-06T01:21:11.511Z-->

## equipment overview

A __DC power supply__ (one or two channels) provides constant voltage to the breadboard rails; set output voltage and current limit, never short the outputs. A __function generator__ produces AC waveforms (sine, square, triangle) with adjustable amplitude and frequency; used in later labs, viewed on the DSO. Reset the function generator at the start of each experiment and connect the probe to the __FUNCTION__ output (not TTL or sync). A __DMM__ measures voltage, current, or resistance. A __DSO__ displays voltage versus time, showing amplitude, period, and frequency. The breadboard is where components and jumper wires form circuits. For regulated $5\text{ V}$ (and $12\text{ V}$ motor) rails see [voltage regulator](voltage%20regulator.md).

---

Flashcards for this section are as follows:

- core instruments ::@:: DC power supply, DMM, function generator, and DSO; the breadboard is where you build circuits. <!--SR:!fsrs,2027-02-14T01:15:38.677Z,253,253.31932065,1.98030797,2,6,0,0,2026-06-06T01:15:38.677Z!fsrs,2027-05-09T08:38:31.252Z,330,329.54847456,1,2,7,0,0,2026-06-13T08:38:31.252Z-->
- DC power supply ::@:: Provides constant voltage (one or two channels) to power the breadboard rails; set voltage and current limit, never short the outputs. <!--SR:!fsrs,2027-04-09T01:15:40.014Z,307,307.08504834,1,2,7,0,0,2026-06-06T01:15:40.014Z!fsrs,2027-04-06T01:21:02.612Z,304,303.62086325,1,2,7,0,0,2026-06-06T01:21:02.612Z-->
- function generator ::@:: Produces AC waveforms (sine, square, triangle) with adjustable amplitude and frequency; used in later labs, viewed on the DSO. <!--SR:!fsrs,2027-04-07T01:21:06.993Z,305,305.20736891,1,2,7,0,0,2026-06-06T01:21:06.993Z!fsrs,2027-05-10T08:38:15.865Z,331,331.0632816,1,2,7,0,0,2026-06-13T08:38:15.865Z-->
- function generator setup ::@:: Reset the function generator at the start of each experiment (e.g. _default setup_) and connect the probe or BNC lead to the FUNCTION output, not TTL or sync. <!--SR:!fsrs,2027-04-09T01:21:01.028Z,307,307.08504834,1,2,7,0,0,2026-06-06T01:21:01.028Z!fsrs,2027-05-09T08:38:49.756Z,330,329.54847456,1,2,7,0,0,2026-06-13T08:38:49.756Z-->
- DMM ::@:: Measures voltage, current, or resistance depending on mode and connection. <!--SR:!fsrs,2027-04-16T08:11:59.290Z,313,312.84164192,1,2,7,0,0,2026-06-07T08:11:59.290Z!fsrs,2027-05-09T08:38:47.649Z,330,329.54847456,1,2,7,0,0,2026-06-13T08:38:47.649Z-->
- DSO ::@:: Displays voltage versus time; shows amplitude, period, and frequency of signals. <!--SR:!fsrs,2027-05-10T08:38:11.482Z,331,331.0632816,1,2,7,0,0,2026-06-13T08:38:11.482Z!fsrs,2027-05-07T08:38:12.394Z,328,328.01615794,1,2,7,0,0,2026-06-13T08:38:12.394Z-->

## breadboard structure and connections

Breadboards use a plastic body with internal metal strips as conductors. Row holes are grouped in sets of five, connected internally; long power-rail columns along the edges are connected along their length. Adjacent columns are not connected; use jumper wires to bridge between rows or columns.

---

Flashcards for this section are as follows:

- breadboard construction ::@:: Plastic body with internal metal strips; historically wooden boards with nailed components. <!--SR:!fsrs,2027-04-16T08:12:01.150Z,313,312.84164192,1,2,7,0,0,2026-06-07T08:12:01.150Z!fsrs,2027-04-01T01:15:33.888Z,299,298.72647102,1,2,7,0,0,2026-06-06T01:15:33.888Z-->
- row connections ::@:: Groups of five holes in a row are internally connected; components in the same row share a node. <!--SR:!fsrs,2027-05-10T08:41:12.056Z,331,331.0632816,1,2,7,0,0,2026-06-13T08:41:12.056Z!fsrs,2027-05-10T08:41:12.800Z,331,331.0632816,1,2,7,0,0,2026-06-13T08:41:12.800Z-->
- power rails ::@:: Long columns along the edges; all holes in one column are connected. <!--SR:!fsrs,2027-04-07T01:18:28.929Z,305,305.20736891,1,2,7,0,0,2026-06-06T01:18:28.929Z!fsrs,2027-04-06T01:21:07.686Z,304,304.04690879,1,2,7,0,0,2026-06-06T01:21:07.686Z-->
- adjacent columns ::@:: Not connected; use jumper wires to bridge between rows or columns. <!--SR:!fsrs,2027-04-02T01:21:13.131Z,300,300.38138884,1,2,7,0,0,2026-06-06T01:21:13.131Z!fsrs,2027-04-01T01:15:35.985Z,299,298.72647102,1,2,7,0,0,2026-06-06T01:15:35.985Z-->

## component symbols and power rails

Schematic symbols on lab handouts indicate power rails ($+5\text{ V}$, GND), voltage sources, resistors, capacitors, and LEDs. On the breadboard you assign one rail to $+5\text{ V}$ (or the supply voltage) and another to ground; all points connected to the same rail are at the same potential. See [electronic component](electronic%20component.md) for resistor, capacitor, and ground symbols.

---

Flashcards for this section are as follows:

- power rail assignment ::@:: One rail to positive supply (e.g. $+5\text{ V}$), another to ground; all holes on that rail share the same voltage. <!--SR:!fsrs,2027-04-04T01:21:03.369Z,302,302.01253197,1,2,7,0,0,2026-06-06T01:21:03.369Z!fsrs,2027-05-07T08:38:50.887Z,328,328.01615794,1,2,7,0,0,2026-06-13T08:38:50.887Z-->
- schematic symbols ::@:: Handouts use symbols for voltage sources, resistors, capacitors, LEDs, and connections; see [electronic component](electronic%20component.md). <!--SR:!fsrs,2027-05-12T08:38:48.325Z,333,332.56124433,1,2,7,0,0,2026-06-13T08:38:48.325Z!fsrs,2027-05-12T08:40:14.127Z,333,332.56124433,1,2,7,0,0,2026-06-13T08:40:14.127Z-->

## resistor colour code

Axial resistors use coloured bands to indicate resistance value and tolerance. On a __4-band__ resistor, read from the end that has the tolerance band (usually gold or silver) at one end: the __first two bands__ are digits (0–9), the __third band__ is the multiplier (power of 10), and the __fourth band__ is the tolerance. In __5-band__ code (tutorial slides), the __first three bands__ are digits, the __fourth__ is the multiplier, and the __fifth__ is the tolerance.

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

Examples (4-band): __brown–black–orange–gold__ = 1, 0, $\times1\text{ k}$, $\pm5\%$ → $10\text{ k}\Omega$ $\pm5\%$. __Red–red–brown–gold__ = 2, 2, $\times10$, $\pm5\%$ → $220\,\Omega$ $\pm5\%$. __Yellow–violet–orange–gold__ = 4, 7, $\times1\text{ k}$, $\pm5\%$ → $47\text{ k}\Omega$ $\pm5\%$.

__5-band code__ (used in the tutorial slides): use the table above; band positions are three digits, then multiplier, then tolerance. __5-band example 2–3–7–1%:__ digits 2, 3, 7, multiplier $\times1$ (black), tolerance $\pm1\%$ (brown) → $R=237\times1\,\Omega=237\,\Omega$ $\pm1\%$. So red–orange–violet–black–brown (5-band) = $237\,\Omega$ $\pm1\%$. __5-band example brown–black–black–brown–brown:__ = 1, 0, 0, $\times10$, $\pm1\%$ → $1\text{ k}\Omega$ $\pm1\%$.

To identify the correct reading direction, first look for the tolerance band: in 4-band resistors it is usually gold or silver and sits at one end, so you read from the _opposite_ end toward the tolerance band. In 5-band resistors the tolerance band is often brown, red, green, blue, or violet, so color alone is not always enough; the safer cues are that the tolerance band is the _last_ band, it is often separated by a slightly larger physical gap, and the resistor should decode into the pattern "digits, then multiplier, then tolerance" rather than something impossible such as gold or silver in a digit position.

Tricky examples help. If you see a resistor that visually looks like __gold–orange–black–brown__, you should _not_ read from the gold side because gold cannot be the first digit; the correct reading is the reverse direction, __brown–black–orange–gold__, which gives $10\text{ k}\Omega\,\pm5\%$. For a 5-band resistor such as __brown–black–black–red–brown__, both ends may look plausible because brown appears at both ends. The correct reading is still left-to-right here because the final brown is the tolerance band, giving digits 1–0–0, multiplier $\times100$, and resistance $10\text{ k}\Omega\,\pm1\%$. Reading it backwards would place a tolerance color in a digit position and break the normal 5-band pattern.

---

Flashcards for this section are as follows:

- resistor colour code: 4-band order ::@:: Band 1–2 = digits, band 3 = multiplier, band 4 = tolerance. Read from the end where the tolerance band (e.g. gold/silver) sits. <!--SR:!fsrs,2027-02-14T01:15:30.639Z,253,253.31932065,1.98030797,2,6,0,0,2026-06-06T01:15:30.639Z!fsrs,2027-04-11T01:21:04.602Z,309,308.57643926,1,2,7,0,0,2026-06-06T01:21:04.602Z-->
- resistor colour code: 5-band order ::@:: Bands 1–3 = digits, band 4 = multiplier, band 5 = tolerance. Same table; used in the tutorial slides. <!--SR:!fsrs,2027-04-06T01:21:18.042Z,304,303.62086325,1,2,7,0,0,2026-06-06T01:21:18.042Z!fsrs,2027-04-06T01:15:42.613Z,304,303.62086325,1,2,7,0,0,2026-06-06T01:15:42.613Z-->
- resistor reading direction: how do you decide which end to start from for a 4-band or 5-band resistor? ::@:: Read so that the bands fit the pattern "digits, then multiplier, then tolerance". In 4-band code the tolerance band is usually gold or silver and is last, so start from the opposite end. In 5-band code the tolerance band may be brown or another nonmetallic color, so also use the larger end-gap and the fact that the last band should be tolerance, not a significant digit. <!--SR:!fsrs,2028-01-30T00:00:00.000Z,532,532.38903993,1,2,8,0,0,2026-08-16T00:00:00.000Z!fsrs,2028-01-30T00:00:00.000Z,532,532.38903993,1,2,8,0,0,2026-08-16T00:00:00.000Z-->
- resistor reading direction: why is the tolerance band the key clue? ::@:: Because the tolerance band belongs at the end of the code, not among the significant digits. If reading one way would put gold, silver, or another tolerance-only role into a digit position, that direction is wrong. <!--SR:!fsrs,2028-02-05T00:00:00.000Z,537,537.28725381,1,2,8,0,0,2026-08-17T00:00:00.000Z!fsrs,2028-02-05T00:00:00.000Z,537,537.28725381,1,2,8,0,0,2026-08-17T00:00:00.000Z-->
- resistor colour code: digit column (table) ::@:: Black 0 through white 9 (order: black, brown, red, orange, yellow, green, blue, violet, grey, white). Pink, silver, gold have no digit (—). <!--SR:!fsrs,2027-07-10T00:00:00.000Z,346,346.36826182,2.98092302,2,7,0,0,2026-07-29T00:00:00.000Z!fsrs,2027-04-08T01:15:33.223Z,306,305.57546247,1,2,7,0,0,2026-06-06T01:15:33.223Z-->
- resistor colour code: multiplier column (e.g. pink $\times0.001$, gold $\times0.1$, black $\times1$) ::@:: Pink $\times0.001$, silver $\times0.01$, gold $\times0.1$; black $\times1$ through white $\times10^9$ (same order as digits). Use the table for the exact multiplier. <!--SR:!fsrs,2027-05-07T08:38:16.622Z,328,328.01615794,1,2,7,0,0,2026-06-13T08:38:16.622Z!fsrs,2027-02-17T01:21:01.846Z,256,255.52482907,1.98030797,2,6,0,0,2026-06-06T01:21:01.846Z-->
- resistor colour code: tolerance column (e.g. silver $\pm10\%$, gold $\pm5\%$, brown $\pm1\%$) ::@:: Silver $\pm10\%$, gold $\pm5\%$; brown $\pm1\%$, red $\pm2\%$, orange $\pm0.05\%$, yellow $\pm0.02\%$, green $\pm0.5\%$, blue $\pm0.25\%$, violet $\pm0.1\%$, grey $\pm0.01\%$. Black, white, pink: no tolerance (—). <!--SR:!fsrs,2027-02-18T01:18:33.583Z,257,256.93605699,1.98030797,2,7,0,0,2026-06-06T01:18:33.583Z!fsrs,2027-05-09T08:38:30.650Z,330,329.54847456,1,2,7,0,0,2026-06-13T08:38:30.650Z-->
- resistor colour code 4-band example: brown–black–orange–gold (1, 0, $\times1000$, $\pm5\%$) → $R$? ::@:: $R=10\text{ k}\Omega$ $\pm5\%$. <!--SR:!fsrs,2027-04-02T01:21:20.032Z,300,300.38138884,1,2,7,0,0,2026-06-06T01:21:20.032Z!fsrs,2027-02-18T01:21:14.043Z,257,257.3715178,1.98030797,2,7,0,0,2026-06-06T01:21:14.043Z-->
- resistor colour code 4-band example: red–red–brown–gold (2, 2, $\times10$, $\pm5\%$) → $R$? ::@:: $R=220\,\Omega$ $\pm5\%$. <!--SR:!fsrs,2027-04-08T01:18:34.425Z,306,305.57546247,1,2,7,0,0,2026-06-06T01:18:34.425Z!fsrs,2027-02-16T01:18:32.859Z,255,255.14407914,1.98030797,2,7,0,0,2026-06-06T01:18:32.859Z-->
- resistor reading direction tricky 4-band case: A resistor appears as gold–orange–black–brown from left to right. If you reverse it to brown–black–orange–gold, what resistance and tolerance does that valid 4-band code represent? ::@:: Do not read from the gold side, because gold cannot be a digit band. Read it in the reverse direction as brown–black–orange–gold, giving $10\text{ k}\Omega\,\pm5\%$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2028-01-30T00:00:00.000Z,532,532.38903993,1,2,8,0,0,2026-08-16T00:00:00.000Z!fsrs,2028-02-05T00:00:00.000Z,537,537.28725381,1,2,8,0,0,2026-08-17T00:00:00.000Z-->
- resistor colour code 5-band example: red–orange–violet–black–brown (2,3,7, $\times1$, $\pm1\%$) → $R$? ::@:: $R=237\,\Omega$ $\pm1\%$. <!--SR:!fsrs,2027-04-04T01:15:34.694Z,302,302.01253197,1,2,7,0,0,2026-06-06T01:15:34.694Z!fsrs,2027-02-15T01:18:31.796Z,254,253.64311137,1.98030797,2,6,0,0,2026-06-06T01:18:31.796Z-->
- resistor colour code 5-band example: brown–black–black–brown–brown (1,0,0, $\times10$, $\pm1\%$) → $R$? ::@:: $R=1\text{ k}\Omega$ $\pm1\%$. <!--SR:!fsrs,2027-05-09T08:38:14.815Z,330,329.54847456,1,2,7,0,0,2026-06-13T08:38:14.815Z!fsrs,2027-04-07T01:18:31.017Z,305,305.20736891,1,2,7,0,0,2026-06-06T01:18:31.017Z-->
- resistor reading direction tricky 5-band example: Why is brown–black–black–red–brown read left-to-right as $10\text{ k}\Omega\,\pm1\%$ instead of right-to-left? ::@:: In a 5-band resistor the last band is tolerance. Reading left-to-right gives digits 1–0–0, multiplier $\times100$, and final brown tolerance $\pm1\%$, so the value is $10\text{ k}\Omega\,\pm1\%$. Reading it backward would misuse the tolerance band as a leading digit band. <!--SR:!fsrs,2028-02-05T00:00:00.000Z,537,537.28725381,1,2,8,0,0,2026-08-17T00:00:00.000Z!fsrs,2028-01-30T00:00:00.000Z,532,532.38903993,1,2,8,0,0,2026-08-16T00:00:00.000Z-->

## reading the DSO

The digital storage oscilloscope (DSO) displays __voltage on the vertical axis__ and __time on the horizontal axis__. Before taking any reading, check the __scale__ (and units) for each axis.

- __Vertical axis (voltage):__ Each division on the screen corresponds to a voltage step set by the vertical scale (e.g. $1\text{ V}/\text{div}$, $500\text{ mV}/\text{div}$). The on-screen display usually shows the scale in V or mV. To read __peak-to-peak voltage__ $V_{\text{pp}}$: count the number of vertical divisions from the minimum to the maximum of the waveform and multiply by the volts-per-division. For a __DC level__ or __mean value__, read the vertical position of the flat part (or use the DSO's built-in mean/DC measurement if available).
- __Horizontal axis (time):__ Each division corresponds to a time step (e.g. $1\text{ ms}/\text{div}$, $100\,\mu\text{s}/\text{div}$). Units may be s, ms, or $\mu\text{s}$. To find the __period__ $T$ of a periodic waveform: count the number of horizontal divisions for one complete cycle and multiply by the time-per-division. __Frequency__ is $f=1/T$ (unit Hz or kHz); many DSOs display frequency directly, but always verify the scale so you know whether the reading is in Hz, kHz, or MHz.
- __Trigger:__ The trigger stabilises the display so that a repeating waveform appears stationary. Set the trigger source (e.g. channel 1), trigger level, and slope (rising or falling) as indicated in the tutorial; if the trace is running or jumping, adjust the trigger level until the waveform locks.
- __Interpret units:__ Always note whether the vertical scale is in V or mV and whether the horizontal scale is in s, ms, or $\mu\text{s}$ so that peak-to-peak, period, and frequency are read with the correct magnitude.
- __Probe connections:__ In the lab, always connect the DSO probe clip (negative) to the circuit's reference node marked GND in the schematic, and touch the probe tip to the metal at the bottom of component leads instead of pushing it directly into breadboard holes so the contacts are not damaged.

---

Flashcards for this section are as follows:

- DSO vertical axis ::@:: Voltage; each division = volts (or mV) per division; check on-screen scale before reading. <!--SR:!fsrs,2027-04-16T08:12:00.621Z,313,312.84164192,1,2,7,0,0,2026-06-07T08:12:00.621Z!fsrs,2027-05-07T08:38:49.155Z,328,328.01615794,1,2,7,0,0,2026-06-13T08:38:49.155Z-->
- DSO horizontal axis ::@:: Time; each division = time per division (s/ms/μs); use to read period $T$. <!--SR:!fsrs,2027-04-09T01:21:05.260Z,307,307.08504834,1,2,7,0,0,2026-06-06T01:21:05.260Z!fsrs,2027-04-06T01:18:29.703Z,304,304.04690879,1,2,7,0,0,2026-06-06T01:18:29.703Z-->
- DSO peak-to-peak ($V_{\text{pp}}$) ::@:: Count vertical divisions from minimum to maximum, multiply by volts-per-division. <!--SR:!fsrs,2027-04-08T01:15:37.248Z,306,305.57546247,1,2,7,0,0,2026-06-06T01:15:37.248Z!fsrs,2027-04-06T01:15:40.926Z,304,304.04690879,1,2,7,0,0,2026-06-06T01:15:40.926Z-->
- DSO period and frequency ::@:: $T$ = horizontal divisions for one cycle × time-per-division; $f=1/T$ (Hz or kHz). <!--SR:!fsrs,2027-04-02T01:15:39.354Z,300,300.38138884,1,2,7,0,0,2026-06-06T01:15:39.354Z!fsrs,2027-04-01T01:21:10.870Z,299,298.72647102,1,2,7,0,0,2026-06-06T01:21:10.870Z-->
- DSO trigger ::@:: Stabilises the display so a repeating waveform appears stationary; set source, level, and slope. <!--SR:!fsrs,2027-04-08T01:15:35.363Z,306,305.57546247,1,2,7,0,0,2026-06-06T01:15:35.363Z!fsrs,2027-05-12T08:38:05.985Z,333,332.56124433,1,2,7,0,0,2026-06-13T08:38:05.985Z-->
- DSO units reminder ::@:: Check on-screen units for vertical (V/mV) and horizontal (s/ms/μs) before reading $V_{\text{pp}}$, period, or frequency. <!--SR:!fsrs,2027-04-07T01:15:38.012Z,305,305.20736891,1,2,7,0,0,2026-06-06T01:15:38.012Z!fsrs,2027-04-11T01:18:30.384Z,309,308.57643926,1,2,7,0,0,2026-06-06T01:18:30.384Z-->
- DSO probe connection ::@:: Connect probe clip (negative) to GND in the schematic; touch probe tip to component lead bottoms, not breadboard holes. <!--SR:!fsrs,2027-04-02T01:21:21.192Z,300,300.38138884,1,2,7,0,0,2026-06-06T01:21:21.192Z!fsrs,2027-04-04T01:21:16.741Z,302,302.01253197,1,2,7,0,0,2026-06-06T01:21:16.741Z-->

## LED <!-- check: ignore-line[header_style]: proper noun -->

An LED must be used with a series resistor (typically about $1\text{ k}\Omega$ at $5\text{ V}$) to limit current and avoid damage; see [simple diode circuit analysis and safety](diode.md#simple%20diode%20circuit%20analysis%20and%20safety) in the diode topic. Resistor values are read from the [resistor colour code](#resistor%20colour%20code); the DSO is used as in [reading the DSO](#reading%20the%20DSO).

---

Flashcards for this section are as follows:

- LED series resistor ::@:: Always use a series resistor (e.g. $1\text{ k}\Omega$ at $5\text{ V}$) with an LED to limit current. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- 5-band colour code example ::@:: Red–orange–violet–black–brown: digits 2–3–7, multiplier ×1, tolerance ±1% → $R=237\,\Omega$ $\pm1\%$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- DSO scales ::@:: Vertical divisions are voltage, horizontal divisions are time; check units before reading. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## lab safety

Never short the power rails or reverse power and ground. Before rewiring, turn off or disable the DC supply and use the current-limit knob. Ignore the bench supply's GND binding post; treat the circuit's negative terminal as the reference node (GND) for DMM, DSO, and function generator leads. If readings look wrong or you smell burning, turn off immediately and ask a TA.

---

Flashcards for this section are as follows:

- lab safety rules ::@:: Do not short rails or reverse power/ground; turn off the supply and ask a TA if readings look wrong or you smell burning. <!--SR:!fsrs,2027-04-06T01:18:28.146Z,304,303.62086325,1,2,7,0,0,2026-06-06T01:18:28.146Z!fsrs,2027-04-04T01:15:31.363Z,302,302.01253197,1,2,7,0,0,2026-06-06T01:15:31.363Z-->
- DC supply safety ::@:: Turn off or disable output before rewiring; use the current limit to protect circuits; use the circuit's GND node as reference, not the bench supply chassis GND. <!--SR:!fsrs,2027-04-09T01:21:06.278Z,307,307.08504834,1,2,7,0,0,2026-06-06T01:21:06.278Z!fsrs,2027-04-11T01:21:09.611Z,309,308.57643926,1,2,7,0,0,2026-06-06T01:21:09.611Z-->
