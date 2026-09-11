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

A voltage regulator holds an output voltage approximately constant despite changes in input voltage, load current, or operating conditions. In battery-powered robot systems this matters because batteries are not ideal sources, yet logic electronics need a predictable $5\text{ V}$ rail.

---

Flashcards for this section are as follows:

- voltage regulator definition: what does it mean for $V_{\text{out}}$ to be regulated? ::@:: A circuit that maintains approximately constant $V_{\text{out}}$ despite changes in $V_{\text{in}}$ and load conditions.
- why regulation matters in robots: why convert a varying battery rail into $12\text{ V}$ (motor) and $5\text{ V}$ (logic)? ::@:: Batteries are not ideal and their voltage varies; regulation provides predictable rails even when the motor supply and load change.

## why regulation is needed

Real batteries discharge over time so their terminal voltage drops, and their performance depends on temperature. A practical source also has an internal resistance in series with the ideal source, so the output voltage decreases as output current increases. A simple model is $V_{\text{out}} = V_{S} - iR_{S}$, where $R_{S}$ is the internal resistance and $i$ is the drawn current.

---

Flashcards for this section are as follows:

- non-ideal battery model: State the series $R_S$ model and equation $V_{\text{out}} = V_{S} - iR_{S}$. ::@:: Model a real voltage source as an ideal source $V_S$ in series with internal resistance $R_S$, giving $V_{\text{out}} = V_{S} - iR_{S}$ under load.
- battery voltage variation causes ::@:: Battery terminal voltage varies due to discharge (losing charge), temperature effects, and internal resistance causing load-dependent droop.

## diode and Zener diode as regulators

A [diode](diode.md) conducts primarily in one direction. In the ideal model it is a short circuit when forward biased and an open circuit when reverse biased; in practice a forward-biased diode has an approximately constant forward drop (typically about $0.7\text{ V}$ for a silicon diode at modest currents).

A Zener diode behaves like a normal diode in forward bias, but in reverse bias it conducts once the voltage exceeds the Zener breakdown magnitude, clamping the voltage near its breakdown value. This gives a simple clamp regulator: a series resistor limits current, and the Zener shunts current to hold the load node near the Zener voltage when the input is high enough. <p> ![Zener diode symbol](attachments/symbol_zener.svg)

In the lecture's example the circuit is a voltage divider node with a shunt clamp: $V_{\text{in}}$ feeds a series resistor $R_S=1\text{ k}\Omega$ into a single node $V_{\text{node}}$; from that node a load resistor $R_L=3\text{ k}\Omega$ goes to ground; and a Zener diode is connected from the node to ground in reverse bias (cathode at the node, anode at ground). Without the Zener, the node is just a divider so $V_{\text{node}} = V_{\text{in}}\cdot\frac{R_L}{R_S+R_L} = 0.75V_{\text{in}}$. With a Zener of breakdown magnitude $|V_{BD}|=5.7\text{ V}$, reverse conduction begins when the divider would raise $V_{\text{node}}$ above about $5.7\text{ V}$, i.e. when $0.75V_{\text{in}} > 5.7\text{ V}$ so $V_{\text{in}} > 7.6\text{ V}$; beyond this, the Zener shunts current to keep $V_{\text{node}}$ approximately clamped near $5.7\text{ V}$ (with current limited by $R_S$). On a $V_Z$ vs $V_{\text{in}}$ graph, the curve initially follows the rising divider line $V_Z = 0.75V_{\text{in}}$; where this line reaches the clamp level (about $5.7\text{ V}$), the curve bends over and becomes nearly horizontal. The Zener breakdown voltage is the flat plateau value of $V_Z$ in this clamped region. <p> ![Zener clamp regulator circuit](attachments/zener_clamp.svg)

---

Flashcards for this section are as follows:

- diode ideal equivalent ::@:: Ideal diode is a short when forward biased and an open circuit when reverse biased.
- diode forward drop (practical): What is the typical silicon diode forward drop (about $0.7\text{ V}$)? ::@:: A practical silicon diode has an approximately constant forward drop of about $0.7\text{ V}$ when forward biased (order-of-magnitude, depends on current and temperature).
- Zener diode key property ::@:: A Zener diode conducts in reverse bias once reverse voltage exceeds the breakdown magnitude and clamps the voltage near its Zener breakdown value.
- schematic symbol: Zener diode (clamp near $V_Z$) <p> ![Zener diode symbol](attachments/symbol_zener.svg) ::@:: Zener diode symbol representing a diode intended to operate in reverse breakdown to clamp a voltage near $V_Z$ (when used with a series current-limiting resistor).
- Zener clamp regulator idea: How does a shunt Zener clamp hold a node near $V_Z$ when $V_{\text{in}}$ rises? <p> ![Zener clamp regulator circuit](attachments/zener_clamp.svg) ::@:: Use a series resistor to limit current and a Zener diode as a shunt element to clamp the load node near $V_Z$ when $V_{\text{in}}$ is high enough.
- Zener regulator threshold example: If $V_{\text{node}}=0.75V_{\text{in}}$ and $V_Z=5.7\text{ V}$, when does Zener reverse conduction begin (solve for $V_{\text{in}}$)? <p> ![Zener clamp regulator circuit](attachments/zener_clamp.svg) ::@:: If $V_{\text{node}}=0.75V_{\text{in}}$ and $V_Z=5.7\text{ V}$, Zener reverse conduction begins when $0.75V_{\text{in}}>5.7\text{ V}$, i.e. when $V_{\text{in}}>7.6\text{ V}$.
- Zener clamp graph reading: how do you estimate $V_Z$ from a $V_Z$ vs $V_{\text{in}}$ plot? <p> ![Zener clamp regulator circuit](attachments/zener_clamp.svg) ::@:: Look for where the $V_Z$ curve bends from the rising divider line into a near-horizontal plateau; the plateau level is the Zener breakdown voltage.

## integrated-circuit linear regulators (LM7805)

Zener regulators are simple but have poorer regulation than dedicated ICs. Standard ICs are usually the better choice.

An integrated circuit (IC) packs many components onto one chip to perform a function like voltage regulation. Focus on the IC's pins, input/output requirements, recommended external components, and limits — not its internal transistor-level design. The datasheet covers all of these.

The LM7805 is a common fixed-output linear regulator that produces a regulated $5\text{ V}$ output from a higher input voltage. In the project, the battery's $12\text{ V}$ rail drives motors while a regulated $5\text{ V}$ rail powers logic and control circuits (including the [H-bridge](H-bridge.md) driver logic, e.g. L293 VCC and 74HC14). Capacitors at the input and output reduce transients and stabilize the regulator. With the number side of the TO‑220 package facing you, the three LM7805 pins from left to right are IN, GND, and OUT; miswiring defeats regulation and can overheat the device. In lab the LM7805 can get warm or hot in normal operation, so avoid touching it directly; if you notice a bad smell or suspect overheating, turn off the supply and ask a TA to check the circuit. To check regulation, slowly increase $V_{\text{in}}$ from the lab supply and confirm that $V_{\text{out}}$ on the DMM sits close to $5\text{ V}$ instead of tracking $V_{\text{in}}$; if the reading follows $V_{\text{in}}$, turn off the supply and re-check wiring. <p> ![3-pin regulator with input/output capacitors](attachments/three_pin_regulator.svg)

---

Flashcards for this section are as follows:

- integrated circuit (IC) meaning: what is an IC? ::@:: A chip that packs many components (transistors, passives) onto one die to perform a function like voltage regulation; focus on pins, limits, and circuit use rather than internal design.
- IC datasheet role: why read the datasheet? ::@:: The datasheet specifies the IC's pinout, input/output range, recommended external components, and absolute limits — the reference for correct use.
- LM7805 purpose: What regulated rail does an LM7805 provide (nominally $5\text{ V}$)? ::@:: A fixed-output linear regulator IC that produces a regulated $5\text{ V}$ rail from a higher input voltage (within its operating range).
- why add capacitors around regulators: Why add capacitors to stabilize $V_{\text{in}}$ and $V_{\text{out}}$? ::@:: Input/output capacitors help stabilize $V_{\text{in}}$ and $V_{\text{out}}$ by reducing transients and supporting regulator stability.
- regulator wiring diagram recall (3-pin + $C_{in}$ / $C_{out}$) <p> ![3-pin regulator with input/output capacitors](attachments/three_pin_regulator.svg) ::@:: Typical 3-pin linear regulator wiring: connect $V_{in}$ to IN, take $V_{out}$ from OUT, connect GND to ground; add  $C_{in}$ from IN to GND and $C_{out}$ from OUT to GND for stability/transient suppression (per datasheet).
- robot power rails example: In the project, what rails are used for motors vs logic ($12\text{ V}$ and $5\text{ V}$)? ::@:: Use battery $12\text{ V}$ for the motor rail and a regulated $5\text{ V}$ rail (e.g. via LM7805) for other circuits.
- LM7805 lab safety: In lab, what should you do if the LM7805 feels hot or you notice a bad smell from the regulator area? ::@:: Do not keep touching the regulator; immediately turn off the DC supply and ask a TA to help inspect the circuit for wiring or loading faults.
- LM7805 regulation check in lab: When slowly increasing $V_{\text{in}}$ in lab, what multimeter behaviour shows that the LM7805 is regulating correctly vs miswired? ::@:: Correct behaviour: as $V_{\text{in}}$ rises into range, the measured $V_{\text{out}}$ sits close to $5\text{ V}$ instead of following $V_{\text{in}}$; if the reading stays close to $V_{\text{in}}$ (e.g. near $8\text{ V}$) the circuit is miswired and you should turn off the supply and re-check connections.
- LM7805 pin identification in lab: for a TO‑220 LM7805 with the numbered face towards you, what are the functions of pins 1, 2, and 3 (from left to right)? ::@:: Pin 1 (left) is IN, pin 2 (middle) is GND, and pin 3 (right) is OUT; wiring these correctly is essential for safe operation and proper $5\text{ V}$ regulation. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## regulator performance metrics

Two common measures of regulator quality are line regulation and load regulation. Line regulation measures how $V_{\text{out}}$ changes with $V_{\text{in}}$; load regulation measures how $V_{\text{out}}$ changes with output current. Ideal values are zero.

Definitions used in the lecture are: line regulation $=\Delta V_{O}/\Delta V_{I}$ and load regulation $=\Delta V_{O}/\Delta I_{O}$. In the LM7805 example, if $10\text{ V}\le V_{\text{in}}\le15\text{ V}$ produces $V_{\text{out}}$ changing from $4.98\text{ V}$ to $5.03\text{ V}$, then line regulation $=(5.03-4.98)/(15-10)=0.01$ (in $\text{V}/\text{V}$).

Line regulation tests how stable the output is against changes from the input side — battery variation, adapter variation, or supply ripple. The input quantity is therefore input voltage, not input current. Input current depends on the load and regulator operation, so it does not isolate source variation cleanly; $\Delta V_I$ does.

Load regulation asks how well the regulator holds $V_{\text{out}}$ steady when the load changes. The independent variable is output current, because the regulator's job is to keep output voltage fixed. If the robot logic or motor-driver circuitry draws more current, a good regulator lets $V_O$ move only slightly. In short, line regulation tests stability against input changes; load regulation tests stability against load changes.

---

Flashcards for this section are as follows:

- line regulation definition: define line regulation. ::@:: Line regulation is $\Delta V_{O}/\Delta V_{I}$: how much $V_{\text{out}}$ changes when input voltage changes, with load held fixed. Smaller is better.
- why line regulation uses $\Delta V_I$ instead of input current ::@:: Line regulation is meant to measure stability against changes coming from the source side, such as battery droop or input-supply variation, so the disturbance variable is input _voltage_. Input current is less suitable because it depends on the load and the regulator's operation, so it does not isolate source variation cleanly.
- load regulation definition: define load regulation. ::@:: Load regulation is $\Delta V_{O}/\Delta I_{O}$: how much $V_{\text{out}}$ changes when output current demand changes. Smaller is better.
- why load regulation uses output current ::@:: Load regulation studies stability against output-side demand changes. Since the regulator is supposed to keep output voltage approximately constant, the varying quantity is naturally the output _current_ drawn by the load, while the response of interest is the small resulting change in output voltage.
- line vs load regulation: what does each test? ::@:: Line regulation tests $V_O$ stability against input-voltage changes. Load regulation tests $V_O$ stability against output-current changes. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- line regulation example computation: If $V_{\text{out}}$ changes from $4.98\text{ V}$ to $5.03\text{ V}$ as $V_{\text{in}}$ changes from $10\text{ V}$ to $15\text{ V}$, compute $\Delta V_O/\Delta V_I$. ::@:: If $V_{\text{out}}$ changes from $4.98\text{ V}$ to $5.03\text{ V}$ as $V_{\text{in}}$ changes from $10\text{ V}$ to $15\text{ V}$, line regulation is $(5.03-4.98)/(15-10)=0.01$.
