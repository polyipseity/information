---
aliases:
  - DC voltage regulator
  - linear regulator
  - voltage regulator
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1100/voltage_regulator
  - language/in/English
---

# voltage regulator

A voltage regulator is a circuit (discrete components or an integrated circuit) that attempts to keep an output voltage approximately constant even when the input voltage, load current, and operating conditions change. In battery-powered robot systems this is essential because the battery is not an ideal source, yet the logic/control electronics often require a predictable rail such as $5\text{ V}$.

---

Flashcards for this section are as follows:

- voltage regulator definition: What does it mean for $V_{\text{out}}$ to be regulated against changes in $V_{\text{in}}$ and load? ::@:: A circuit/component that maintains (approximately) constant $V_{\text{out}}$ despite changes in $V_{\text{in}}$ and load conditions (within its operating range). <!--SR:!2027-02-18,260,332!fsrs,2027-05-19T15:29:42.112Z,339,339.38014296,1,2,7,0,0,2026-06-14T15:29:42.112Z-->
- why voltage regulation matters in robots: Why convert a varying battery rail into rails like $12\text{ V}$ (motor) and $5\text{ V}$ (logic)? ::@:: Batteries are not ideal and their voltage varies; regulation provides predictable rails (e.g. $5\text{ V}$ logic) even when the motor supply (e.g. $12\text{ V}$) and load change. <!--SR:!2027-02-15,257,332!fsrs,2027-04-24T02:06:44.454Z,320,319.54766452,1,2,7,0,0,2026-06-08T02:06:44.454Z-->

## why regulation is needed

Real batteries discharge over time so their terminal voltage drops, and their performance depends on temperature. A practical source also has an internal resistance in series with the ideal source, so the output voltage decreases as output current increases. A simple model is $V_{\text{out}} = V_{S} - iR_{S}$, where $R_{S}$ is the internal resistance and $i$ is the drawn current.

---

Flashcards for this section are as follows:

- non-ideal battery model: State the series $R_S$ model and equation $V_{\text{out}} = V_{S} - iR_{S}$. ::@:: Model a real voltage source as an ideal source $V_S$ in series with internal resistance $R_S$, giving $V_{\text{out}} = V_{S} - iR_{S}$ under load. <!--SR:!fsrs,2027-05-19T15:29:56.146Z,339,339.38014296,1,2,7,0,0,2026-06-14T15:29:56.146Z!fsrs,2027-04-24T02:06:47.380Z,320,319.54766452,1,2,7,0,0,2026-06-08T02:06:47.380Z-->
- battery voltage variation causes ::@:: Battery terminal voltage varies due to discharge (losing charge), temperature effects, and internal resistance causing load-dependent droop. <!--SR:!2027-02-16,258,332!2027-02-16,259,332-->

## diode and zener diode as regulators

A [diode](diode.md) conducts primarily in one direction. In the ideal model it is a short circuit when forward biased and an open circuit when reverse biased; in practice a forward-biased diode has an approximately constant forward drop (typically about $0.7\text{ V}$ for a silicon diode at modest currents).

A Zener diode behaves like a diode in forward bias, but in reverse bias it also conducts once the reverse voltage exceeds the Zener breakdown magnitude, clamping the voltage near its breakdown value. This enables a simple "clamp" regulator: a series resistor limits current, and the Zener shunts current to hold the load node near the Zener voltage when the input rises above a threshold. <p> ![Zener diode symbol](attachments/symbol_zener.svg)

In the lecture's example the circuit is a voltage divider node with a shunt clamp: $V_{\text{in}}$ feeds a series resistor $R_S=1\text{ k}\Omega$ into a single node $V_{\text{node}}$; from that node a load resistor $R_L=3\text{ k}\Omega$ goes to ground; and a Zener diode is connected from the node to ground in reverse bias (cathode at the node, anode at ground). Without the Zener, the node is just a divider so $V_{\text{node}} = V_{\text{in}}\cdot\frac{R_L}{R_S+R_L} = 0.75V_{\text{in}}$. With a Zener of breakdown magnitude $|V_{BD}|=5.7\text{ V}$, reverse conduction begins when the divider would raise $V_{\text{node}}$ above about $5.7\text{ V}$, i.e. when $0.75V_{\text{in}} > 5.7\text{ V}$ so $V_{\text{in}} > 7.6\text{ V}$; beyond this, the Zener shunts current to keep $V_{\text{node}}$ approximately clamped near $5.7\text{ V}$ (with current limited by $R_S$). On a graph of $V_Z$ versus $V_{\text{in}}$ for this circuit, the curve initially follows the rising divider line $V_Z = 0.75V_{\text{in}}$; at the input where this straight line first reaches the clamp level (about $5.7\text{ V}$), the plotted curve bends over and becomes almost horizontal near $V_Z\approx5.7\text{ V}$. The Zener breakdown voltage is read off as the flat "plateau" value of $V_Z$ in this clamped region. <p> ![Zener clamp regulator circuit](attachments/zener_clamp.svg)

---

Flashcards for this section are as follows:

- diode ideal equivalent ::@:: Ideal diode is a short when forward biased and an open circuit when reverse biased. <!--SR:!2027-02-19,261,332!2027-02-17,259,332-->
- diode forward drop (practical): What is the typical silicon diode forward drop (about $0.7\text{ V}$)? ::@:: A practical silicon diode has an approximately constant forward drop of about $0.7\text{ V}$ when forward biased (order-of-magnitude, depends on current and temperature). <!--SR:!fsrs,2027-04-24T02:06:50.708Z,320,319.54766452,1,2,7,0,0,2026-06-08T02:06:50.708Z!fsrs,2027-04-24T02:06:51.637Z,320,319.54766452,1,2,7,0,0,2026-06-08T02:06:51.637Z-->
- zener diode key property ::@:: A Zener diode conducts in reverse bias once reverse voltage exceeds the breakdown magnitude and clamps the voltage near its Zener breakdown value. <!--SR:!2027-02-17,259,332!fsrs,2027-05-19T15:29:54.089Z,339,339.38014296,1,2,7,0,0,2026-06-14T15:29:54.089Z-->
- schematic symbol: Zener diode (clamp near $V_Z$) <p> ![Zener diode symbol](attachments/symbol_zener.svg) ::@:: Zener diode symbol representing a diode intended to operate in reverse breakdown to clamp a voltage near $V_Z$ (when used with a series current-limiting resistor). <!--SR:!fsrs,2027-05-19T15:29:46.788Z,339,339.38014296,1,2,7,0,0,2026-06-14T15:29:46.788Z!2027-02-14,256,332-->
- zener clamp regulator idea: How does a shunt Zener clamp hold a node near $V_Z$ when $V_{\text{in}}$ rises? <p> ![Zener clamp regulator circuit](attachments/zener_clamp.svg) ::@:: Use a series resistor to limit current and a Zener diode as a shunt element to clamp the load node near $V_Z$ when $V_{\text{in}}$ is high enough. <!--SR:!2027-02-16,258,332!fsrs,2027-04-24T02:06:39.330Z,320,319.54766452,1,2,7,0,0,2026-06-08T02:06:39.330Z-->
- zener regulator threshold example: If $V_{\text{node}}=0.75V_{\text{in}}$ and $V_Z=5.7\text{ V}$, when does Zener reverse conduction begin (solve for $V_{\text{in}}$)? <p> ![Zener clamp regulator circuit](attachments/zener_clamp.svg) ::@:: If $V_{\text{node}}=0.75V_{\text{in}}$ and $V_Z=5.7\text{ V}$, Zener reverse conduction begins when $0.75V_{\text{in}}>5.7\text{ V}$, i.e. when $V_{\text{in}}>7.6\text{ V}$. <!--SR:!2027-02-18,260,332!2027-02-18,261,332-->
- zener clamp graph reading: Given a plot of $V_Z$ against $V_{\text{in}}$ for this circuit, how do you estimate the Zener breakdown voltage from the graph? <p> ![Zener clamp regulator circuit](attachments/zener_clamp.svg) ::@:: Look for the input where the $V_Z$ curve bends from the rising divider line into a near-horizontal plateau; the plateau level of $V_Z$ in this clamped region (around $5.7\text{ V}$ in the example) is the Zener breakdown voltage. <!--SR:!fsrs,2027-05-19T15:29:54.688Z,339,339.38014296,1,2,7,0,0,2026-06-14T15:29:54.688Z!2026-12-09,193,312-->

## integrated-circuit linear regulators (LM7805)

Zener diode regulators are simple but typically have poorer regulation than dedicated regulator ICs. For many projects it is more efficient to use standard integrated circuits (ICs) whose behavior is specified by manufacturer datasheets.

An integrated circuit (IC) is a compact chip that integrates many electronic components (e.g. transistors and passive elements) to implement a function such as voltage regulation. In this course, the key skill is to understand the IC's _function and usage constraints_ (pins, input/output requirements, recommended external components, and limits), rather than its internal transistor-level design. The manufacturer's datasheet is the canonical reference for these details.

The LM7805 is a common fixed-output linear voltage regulator that provides a regulated $5\text{ V}$ output from a higher input voltage (within its allowed range). In the course project context, the battery's $12\text{ V}$ rail can drive motors, while a regulated $5\text{ V}$ rail powers the remaining logic and control circuits (including the [H-bridge](H-bridge.md) driver logic, e.g. L293 VCC and 74HC14). Capacitors are commonly placed at the input and output to help stabilize the regulator (reduce transients and improve stability). Physically, with the number side of the TO‑220 package facing you, the three LM7805 pins from left to right are IN, GND, and OUT; miswiring these will defeat regulation and can overheat the device. In lab the LM7805 can become warm or hot in normal operation, so you avoid touching the package directly; if you ever notice a bad smell or suspect overheating you immediately turn off the supply and ask a TA to inspect the circuit. To check that regulation is working you slowly increase $V_{\text{in}}$ from the lab supply into the allowed range and confirm that the measured $V_{\text{out}}$ on the DMM sits close to $5\text{ V}$ instead of tracking $V_{\text{in}}$; if the reading follows $V_{\text{in}}$ (e.g. still near $8\text{ V}$) you turn off the supply and re-check wiring before trying again. <p> ![3-pin regulator with input/output capacitors](attachments/three_pin_regulator.svg)

---

Flashcards for this section are as follows:

- integrated circuit (IC) meaning: What is an IC in this course context? ::@:: A compact chip integrating many components (e.g. transistors and passives) to implement a function such as voltage regulation; for this course, focus on function, pins, limits, and how to use it in circuits rather than internal design. <!--SR:!fsrs,2027-04-24T02:06:43.681Z,320,319.54766452,1,2,7,0,0,2026-06-08T02:06:43.681Z!fsrs,2027-04-24T02:06:40.490Z,320,319.54766452,1,2,7,0,0,2026-06-08T02:06:40.490Z-->
- IC datasheet role: Why do we read the datasheet when using a regulator IC? ::@:: The datasheet specifies the IC's functional behavior and usage constraints (pinout, input/output range, recommended external components like capacitors, and absolute limits), so it is the authoritative guide for correct application. <!--SR:!2027-02-13,256,332!2026-10-18,160,312-->
- LM7805 purpose: What regulated rail does an LM7805 provide (nominally $5\text{ V}$)? ::@:: A fixed-output linear regulator IC that produces a regulated $5\text{ V}$ rail from a higher input voltage (within its operating range). <!--SR:!fsrs,2027-05-19T15:29:56.756Z,339,339.38014296,1,2,7,0,0,2026-06-14T15:29:56.756Z!2026-11-27,181,312-->
- why add capacitors around regulators: Why add capacitors to stabilize $V_{\text{in}}$ and $V_{\text{out}}$? ::@:: Input/output capacitors help stabilize $V_{\text{in}}$ and $V_{\text{out}}$ by reducing transients and supporting regulator stability. <!--SR:!fsrs,2027-05-19T15:29:49.063Z,339,339.38014296,1,2,7,0,0,2026-06-14T15:29:49.063Z!2027-02-17,260,332-->
- regulator wiring diagram recall (3-pin + $C_{in}$ / $C_{out}$) <p> ![3-pin regulator with input/output capacitors](attachments/three_pin_regulator.svg) ::@:: Typical 3-pin linear regulator wiring: connect $V_{in}$ to IN, take $V_{out}$ from OUT, connect GND to ground; add  $C_{in}$ from IN to GND and $C_{out}$ from OUT to GND for stability/transient suppression (per datasheet). <!--SR:!2027-02-14,256,332!fsrs,2027-04-24T02:06:46.192Z,320,319.54766452,1,2,7,0,0,2026-06-08T02:06:46.192Z-->
- robot power rails example: In the project, what rails are used for motors vs logic ($12\text{ V}$ and $5\text{ V}$)? ::@:: Use battery $12\text{ V}$ for the motor rail and a regulated $5\text{ V}$ rail (e.g. via LM7805) for other circuits. <!--SR:!fsrs,2027-05-19T15:29:51.301Z,339,339.38014296,1,2,7,0,0,2026-06-14T15:29:51.301Z!fsrs,2027-05-19T15:29:40.322Z,339,339.38014296,1,2,7,0,0,2026-06-14T15:29:40.322Z-->
- LM7805 lab safety: In lab, what should you do if the LM7805 feels hot or you notice a bad smell from the regulator area? ::@:: Do not keep touching the regulator; immediately turn off the DC supply and ask a TA to help inspect the circuit for wiring or loading faults. <!--SR:!fsrs,2027-04-24T02:06:49.105Z,320,319.54766452,1,2,7,0,0,2026-06-08T02:06:49.105Z!fsrs,2027-05-19T15:29:53.292Z,339,339.38014296,1,2,7,0,0,2026-06-14T15:29:53.292Z-->
- LM7805 regulation check in lab: When slowly increasing $V_{\text{in}}$ in lab, what multimeter behaviour shows that the LM7805 is regulating correctly vs miswired? ::@:: Correct behaviour: as $V_{\text{in}}$ rises into range, the measured $V_{\text{out}}$ sits close to $5\text{ V}$ instead of following $V_{\text{in}}$; if the reading stays close to $V_{\text{in}}$ (e.g. near $8\text{ V}$) the circuit is miswired and you should turn off the supply and re-check connections. <!--SR:!fsrs,2027-04-24T02:06:42.911Z,320,319.54766452,1,2,7,0,0,2026-06-08T02:06:42.911Z!2027-02-15,257,332-->
- LM7805 pin identification in lab: For a TO‑220 LM7805 with the numbered face towards you, what are the functions of pins 1, 2, and 3 (from left to right)? ::@:: Pin 1 (left) is IN, pin 2 (middle) is GND, and pin 3 (right) is OUT; wiring these correctly is essential for safe operation and proper $5\text{ V}$ regulation. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-12-03,187,312!fsrs,2027-05-19T15:29:45.542Z,339,339.38014296,1,2,7,0,0,2026-06-14T15:29:45.542Z-->

## regulator performance metrics

Two common measures of regulator quality are line regulation and load regulation. Line regulation measures sensitivity of $V_{\text{out}}$ to changes in $V_{\text{in}}$, and load regulation measures sensitivity of $V_{\text{out}}$ to changes in output current. Ideal values are zero.

Definitions used in the lecture are: line regulation $=\Delta V_{O}/\Delta V_{I}$ and load regulation $=\Delta V_{O}/\Delta I_{O}$. In the LM7805 example, if $10\text{ V}\le V_{\text{in}}\le15\text{ V}$ produces $V_{\text{out}}$ changing from $4.98\text{ V}$ to $5.03\text{ V}$, then line regulation $=(5.03-4.98)/(15-10)=0.01$ (in $\text{V}/\text{V}$).

The motivation for defining them this way is important. For _line regulation_, we want to know how stable the regulator output is against changes coming from the _input source side_ — for example battery variation, adapter variation, or upstream supply ripple. So the input quantity used is _input voltage_, not input current. Input current is not a clean independent variable here because it depends strongly on what the regulator is feeding and how the load behaves; using $\Delta V_I$ isolates the source-side disturbance we actually want to test.

For _load regulation_, we instead ask how well the regulator holds the output voltage steady when the _load demand_ changes. The natural independent variable is therefore _output current_, not output voltage, because the whole purpose of the regulator is to keep output voltage approximately fixed. If output current increases because the robot logic or motor-driver circuitry demands more power, a good regulator should let $V_O$ move only slightly. So line regulation is about stability against _input changes_, while load regulation is about stability against _output-demand changes_.

---

Flashcards for this section are as follows:

- line regulation definition: Define line regulation as $\Delta V_{O}/\Delta V_{I}$. ::@:: Line regulation quantifies how much the regulated output voltage changes when the _input voltage_ changes, with the load condition held fixed as much as practical. It is defined as $\Delta V_{O}/\Delta V_{I}$, and a smaller value means better immunity to source-side voltage variation. <!--SR:!2026-07-20,68,343!2026-08-08,87,363-->
- why line regulation uses $\Delta V_I$ instead of input current ::@:: Line regulation is meant to measure stability against changes coming from the source side, such as battery droop or input-supply variation, so the disturbance variable is input _voltage_. Input current is less suitable because it depends on the load and the regulator's operation, so it does not isolate source variation cleanly. <!--SR:!2026-08-09,88,363!2026-08-13,92,363-->
- load regulation definition: Define load regulation as $\Delta V_{O}/\Delta I_{O}$. ::@:: Load regulation quantifies how much the regulated output voltage changes when the _output current demand_ changes. It is defined as $\Delta V_{O}/\Delta I_{O}$, and a smaller value means the regulator holds the output rail steadier as the load changes. <!--SR:!2026-08-14,93,363!2026-08-14,93,363-->
- why load regulation uses output current ::@:: Load regulation studies stability against output-side demand changes. Since the regulator is supposed to keep output voltage approximately constant, the varying quantity is naturally the output _current_ drawn by the load, while the response of interest is the small resulting change in output voltage. <!--SR:!2026-08-14,93,363!2026-08-11,90,363-->
- line vs load regulation: what does each one test? ::@:: Line regulation tests stability of $V_O$ against _input-voltage_ changes from the source side. Load regulation tests stability of $V_O$ against _output-current_ changes from the load side. <!--SR:!2026-08-14,93,363!2026-08-12,91,363-->
- line regulation example computation: If $V_{\text{out}}$ changes from $4.98\text{ V}$ to $5.03\text{ V}$ as $V_{\text{in}}$ changes from $10\text{ V}$ to $15\text{ V}$, compute $\Delta V_O/\Delta V_I$. ::@:: If $V_{\text{out}}$ changes from $4.98\text{ V}$ to $5.03\text{ V}$ as $V_{\text{in}}$ changes from $10\text{ V}$ to $15\text{ V}$, line regulation is $(5.03-4.98)/(15-10)=0.01$. <!--SR:!2026-08-14,93,363!2026-08-14,93,363-->
