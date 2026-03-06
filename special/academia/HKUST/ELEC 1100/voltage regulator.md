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

- voltage regulator definition: What does it mean for $V_{\text{out}}$ to be regulated against changes in $V_{\text{in}}$ and load? ::@:: A circuit/component that maintains (approximately) constant $V_{\text{out}}$ despite changes in $V_{\text{in}}$ and load conditions (within its operating range).
- why voltage regulation matters in robots: Why convert a varying battery rail into rails like $12\text{ V}$ (motor) and $5\text{ V}$ (logic)? ::@:: Batteries are not ideal and their voltage varies; regulation provides predictable rails (e.g. $5\text{ V}$ logic) even when the motor supply (e.g. $12\text{ V}$) and load change.

## why regulation is needed

Real batteries discharge over time so their terminal voltage drops, and their performance depends on temperature. A practical source also has an internal resistance in series with the ideal source, so the output voltage decreases as output current increases. A simple model is $V_{\text{out}} = V_{S} - iR_{S}$, where $R_{S}$ is the internal resistance and $i$ is the drawn current.

---

Flashcards for this section are as follows:

- non-ideal battery model: State the series $R_S$ model and equation $V_{\text{out}} = V_{S} - iR_{S}$. ::@:: Model a real voltage source as an ideal source $V_S$ in series with internal resistance $R_S$, giving $V_{\text{out}} = V_{S} - iR_{S}$ under load.
- battery voltage variation causes ::@:: Battery terminal voltage varies due to discharge (losing charge), temperature effects, and internal resistance causing load-dependent droop.

## diode and zener diode as regulators

A diode conducts primarily in one direction. In the ideal model it is a short circuit when forward biased and an open circuit when reverse biased; in practice a forward-biased diode has an approximately constant forward drop (typically about $0.7\text{ V}$ for a silicon diode at modest currents).

A Zener diode behaves like a diode in forward bias, but in reverse bias it also conducts once the reverse voltage exceeds the Zener breakdown magnitude, clamping the voltage near its breakdown value. This enables a simple “clamp” regulator: a series resistor limits current, and the Zener shunts current to hold the load node near the Zener voltage when the input rises above a threshold. <p> ![Zener diode symbol](attachments/symbol_zener.svg)

In the lecture’s example the circuit is a voltage divider node with a shunt clamp: $V_{\text{in}}$ feeds a series resistor $R_S=1\text{ k}\Omega$ into a single node $V_{\text{node}}$; from that node a load resistor $R_L=3\text{ k}\Omega$ goes to ground; and a Zener diode is connected from the node to ground in reverse bias (cathode at the node, anode at ground). Without the Zener, the node is just a divider so $V_{\text{node}} = V_{\text{in}}\cdot\frac{R_L}{R_S+R_L} = 0.75V_{\text{in}}$. With a Zener of breakdown magnitude $|V_{BD}|=5.7\text{ V}$, reverse conduction begins when the divider would raise $V_{\text{node}}$ above about $5.7\text{ V}$, i.e. when $0.75V_{\text{in}} > 5.7\text{ V}$ so $V_{\text{in}} > 7.6\text{ V}$; beyond this, the Zener shunts current to keep $V_{\text{node}}$ approximately clamped near $5.7\text{ V}$ (with current limited by $R_S$). <p> ![Zener clamp regulator circuit](attachments/zener_clamp.svg)

---

Flashcards for this section are as follows:

- diode ideal equivalent ::@:: Ideal diode is a short when forward biased and an open circuit when reverse biased.
- diode forward drop (practical): What is the typical silicon diode forward drop (about $0.7\text{ V}$)? ::@:: A practical silicon diode has an approximately constant forward drop of about $0.7\text{ V}$ when forward biased (order-of-magnitude, depends on current and temperature).
- zener diode key property ::@:: A Zener diode conducts in reverse bias once reverse voltage exceeds the breakdown magnitude and clamps the voltage near its Zener breakdown value.
- schematic symbol: Zener diode (clamp near $V_Z$) <p> ![Zener diode symbol](attachments/symbol_zener.svg) ::@:: Zener diode symbol representing a diode intended to operate in reverse breakdown to clamp a voltage near $V_Z$ (when used with a series current-limiting resistor).
- zener clamp regulator idea: How does a shunt Zener clamp hold a node near $V_Z$ when $V_{\text{in}}$ rises? <p> ![Zener clamp regulator circuit](attachments/zener_clamp.svg) ::@:: Use a series resistor to limit current and a Zener diode as a shunt element to clamp the load node near $V_Z$ when $V_{\text{in}}$ is high enough.
- zener regulator threshold example: If $V_{\text{node}}=0.75V_{\text{in}}$ and $V_Z=5.7\text{ V}$, when does Zener reverse conduction begin (solve for $V_{\text{in}}$)? <p> ![Zener clamp regulator circuit](attachments/zener_clamp.svg) ::@:: If $V_{\text{node}}=0.75V_{\text{in}}$ and $V_Z=5.7\text{ V}$, Zener reverse conduction begins when $0.75V_{\text{in}}>5.7\text{ V}$, i.e. when $V_{\text{in}}>7.6\text{ V}$.

## integrated-circuit linear regulators (LM7805)

Zener diode regulators are simple but typically have poorer regulation than dedicated regulator ICs. For many projects it is more efficient to use standard integrated circuits (ICs) whose behavior is specified by manufacturer datasheets.

An integrated circuit (IC) is a compact chip that integrates many electronic components (e.g. transistors and passive elements) to implement a function such as voltage regulation. In this course, the key skill is to understand the IC’s *function and usage constraints* (pins, input/output requirements, recommended external components, and limits), rather than its internal transistor-level design. The manufacturer’s datasheet is the canonical reference for these details.

The LM7805 is a common fixed-output linear voltage regulator that provides a regulated $5\text{ V}$ output from a higher input voltage (within its allowed range). In the course project context, the battery’s $12\text{ V}$ rail can drive motors, while a regulated $5\text{ V}$ rail powers the remaining logic and control circuits. Capacitors are commonly placed at the input and output to help stabilize the regulator (reduce transients and improve stability). <p> ![3-pin regulator with input/output capacitors](attachments/three_pin_regulator.svg)

---

Flashcards for this section are as follows:

- integrated circuit (IC) meaning: What is an IC in this course context? ::@:: A compact chip integrating many components (e.g. transistors and passives) to implement a function such as voltage regulation; for this course, focus on function, pins, limits, and how to use it in circuits rather than internal design.
- IC datasheet role: Why do we read the datasheet when using a regulator IC? ::@:: The datasheet specifies the IC’s functional behavior and usage constraints (pinout, input/output range, recommended external components like capacitors, and absolute limits), so it is the authoritative guide for correct application.
- LM7805 purpose: What regulated rail does an LM7805 provide (nominally $5\text{ V}$)? ::@:: A fixed-output linear regulator IC that produces a regulated $5\text{ V}$ rail from a higher input voltage (within its operating range).
- why add capacitors around regulators: Why add capacitors to stabilize $V_{\text{in}}$ and $V_{\text{out}}$? ::@:: Input/output capacitors help stabilize $V_{\text{in}}$ and $V_{\text{out}}$ by reducing transients and supporting regulator stability.
- regulator wiring diagram recall (3-pin + $C_{in}$ / $C_{out}$) <p> ![3-pin regulator with input/output capacitors](attachments/three_pin_regulator.svg) ::@:: Typical 3-pin linear regulator wiring: connect $V_{in}$ to IN, take $V_{out}$ from OUT, connect GND to ground; add  $C_{in}$ from IN to GND and $C_{out}$ from OUT to GND for stability/transient suppression (per datasheet).
- robot power rails example: In the project, what rails are used for motors vs logic ($12\text{ V}$ and $5\text{ V}$)? ::@:: Use battery $12\text{ V}$ for the motor rail and a regulated $5\text{ V}$ rail (e.g. via LM7805) for other circuits.

## regulator performance metrics

Two common measures of regulator quality are line regulation and load regulation. Line regulation measures sensitivity of $V_{\text{out}}$ to changes in $V_{\text{in}}$, and load regulation measures sensitivity of $V_{\text{out}}$ to changes in output current. Ideal values are zero.

Definitions used in the lecture are: line regulation $=\Delta V_{O}/\Delta V_{I}$ and load regulation $=\Delta V_{O}/\Delta I_{O}$. In the LM7805 example, if $10\text{ V}\le V_{\text{in}}\le15\text{ V}$ produces $V_{\text{out}}$ changing from $4.98\text{ V}$ to $5.03\text{ V}$, then line regulation $=(5.03-4.98)/(15-10)=0.01$ (in $\text{V}/\text{V}$).

---

Flashcards for this section are as follows:

- line regulation definition: Define line regulation as $\Delta V_{O}/\Delta V_{I}$. ::@:: Line regulation quantifies how $V_{\text{out}}$ changes with $V_{\text{in}}$, defined as $\Delta V_{O}/\Delta V_{I}$ (ideal is $0$).
- load regulation definition: Define load regulation as $\Delta V_{O}/\Delta I_{O}$. ::@:: Load regulation quantifies how $V_{\text{out}}$ changes with output current, defined as $\Delta V_{O}/\Delta I_{O}$ (ideal is $0$).
- line regulation example computation: If $V_{\text{out}}$ changes from $4.98\text{ V}$ to $5.03\text{ V}$ as $V_{\text{in}}$ changes from $10\text{ V}$ to $15\text{ V}$, compute $\Delta V_O/\Delta V_I$. ::@:: If $V_{\text{out}}$ changes from $4.98\text{ V}$ to $5.03\text{ V}$ as $V_{\text{in}}$ changes from $10\text{ V}$ to $15\text{ V}$, line regulation is $(5.03-4.98)/(15-10)=0.01$.
