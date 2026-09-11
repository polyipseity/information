---
aliases:
  - BJT
  - bipolar junction transistor
  - transistor
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1100/transistor
  - language/in/English
---

# transistor

A transistor is a three-terminal semiconductor device that can amplify or switch current. This course focuses on bipolar junction transistors (BJTs), types NPN and PNP, which add a third layer to a PN junction. The three terminals are collector (C), base (B), and emitter (E). In ELEC 1100 circuits, transistors act as motor-control switches in the [H-bridge](H-bridge.md) and as current amplifiers where a small base current controls a much larger collector current.

---

Flashcards for this section are as follows:

- transistor definition: what is a transistor in terms of terminals and function? ::@:: A transistor is a three-terminal semiconductor device (collector, base, emitter) that can amplify or switch current between two terminals under control of the third.
- BJT types: what are the two standard BJT types? ::@:: The two common BJTs are NPN and PNP, distinguished by the order of N and P semiconductor regions.
- controlled path in a BJT: which path does the base current control? ::@:: In our NPN/PNP examples the small base current (between base and emitter) controls a much larger current between collector and emitter.
- transistor use: switching ::@:: In ELEC 1100 we use BJTs as on/off switches to control current through motors and other loads.
- transistor use: current gain ::@:: In ELEC 1100 we also use BJTs for current gain: a small base current from logic/sensors can control a much larger collector current.

## structure

A BJT is a [PN junction diode](diode.md#pn%20junction%20and%20biasing) with an additional layer, forming either NPN or PNP structures. The base is thin and lightly doped; the emitter and collector are more heavily doped for current injection and collection. The emitter is the carrier source, the collector gathers them, and the base controls how easily carriers cross the structure. <p> ![NPN BJT symbol](attachments/symbol_npn.svg) <p> ![PNP BJT symbol](attachments/symbol_pnp.svg)

In the common symbol convention, for an NPN transistor the emitter arrow points _out_ of the device (from emitter to base); for PNP it points _in_ (toward the base). In both symbols the base is the middle leg and the collector has no arrow. Schematic symbols depict current directions and layers, not physical pin ordering; the datasheet gives the actual pinout.

For analysis, the equivalent circuit models the base–emitter junction as a diode and the collector–emitter path as a dependent current source $I_C=\beta I_B$. For __NPN__ the B–E diode has its anode at the base and cathode at the emitter (forward when $V_{BE}>0.7\text{ V}$), and the dependent current source drives current from collector to emitter. For __PNP__ the E–B diode has its anode at the emitter and cathode at the base (forward when the emitter is more positive than the base), and the dependent current source drives current from emitter to collector. <p> ![NPN BJT equivalent: diode and dependent current source](attachments/equivalent_npn.svg) <p> ![PNP BJT equivalent: diode and dependent current source](attachments/equivalent_pnp.svg)

---

Flashcards for this section are as follows:

- BJT terminals ::@:: The three terminals are collector (C), base (B), and emitter (E); in the schematic symbol the base is the middle leg, the emitter has the arrow, and the collector has no arrow.
- npn vs pnp arrow direction ::@:: The NPN emitter arrow points out (from emitter to base); the PNP arrow points in (toward the base). Mnemonic: "NPN: arrow Not Pointing iN".
- emitter vs collector role ::@:: The emitter is heavily doped and acts as the carrier source, the collector gathers carriers, and the base is a thin region that regulates how much emitter current reaches the collector.
- schematic symbol: NPN BJT <p> ![NPN BJT symbol](attachments/symbol_npn.svg) ::@:: NPN transistor symbol with emitter arrow pointing out; terminals are base (B), collector (C), emitter (E).
- schematic symbol: PNP BJT <p> ![PNP BJT symbol](attachments/symbol_pnp.svg) ::@:: PNP transistor symbol with emitter arrow pointing in; terminals are base (B), collector (C), emitter (E).
- equivalent circuit (diode + $\beta I_B$): what does it model? ::@:: The base–emitter junction is a diode; the collector–emitter path is a dependent current source $I_C=\beta I_B$.
- equivalent schematic: NPN <p> ![NPN BJT equivalent](attachments/equivalent_npn.svg) ::@:: NPN equivalent: B–E diode (anode at B, cathode at E) and dependent current source $\beta I_B$ from collector to emitter. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- equivalent schematic: PNP <p> ![PNP BJT equivalent](attachments/equivalent_pnp.svg) ::@:: PNP equivalent: E–B diode (anode at E, cathode at B) and dependent current source $\beta I_B$ from emitter to collector. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## historical context

Historically, the first working transistor was demonstrated at Bell Labs in 1947 by John Bardeen, Walter Brattain, and William Shockley. Transistors enabled compact integrated circuits and eventually computers, mobile phones, and other devices. Shockley later founded Shockley Semiconductor Laboratory in Palo Alto.

---

Flashcards for this section are as follows:

- transistor historical significance ::@:: The transistor, invented at Bell Labs in 1947, enabled compact integrated circuits and modern electronics. Shockley later founded a semiconductor company in Palo Alto.

## transistor operation modes

For an NPN BJT, the base–emitter (B–E) junction behaves like a diode with an approximate forward drop of $0.7\text{ V}$. The same device can therefore appear as an open switch, a current amplifier, or a saturated switch depending on its bias point and the surrounding circuit.

### key voltages and current relation

Two voltages appear often in BJT circuits:

- $V_{CC}$: the DC supply voltage feeding the collector/load network (e.g. the " $5\text{ V}$ rail").
- $V_{CE}$: the collector-to-emitter voltage, defined as $V_{CE}=V_C-V_E$ (for an NPN low-side switch, $V_E$ is usually $0\text{ V}$ so $V_{CE}\approx V_C$).

[Kirchhoff's current law](Kirchhoff%27s%20circuit%20laws.md#kirchhoff%27s%20current%20law) at the transistor gives $I_E=I_C+I_B$ when all three currents are defined as __leaving__ the transistor; in practice we often draw NPN currents flowing _into_ the device at C and B and _out_ at E, or the opposite for PNP, but the magnitude relation "emitter current equals base plus collector" still holds in either case.

---

Flashcards for this section are as follows:

- $V_{CC}$ and $V_{CE}$: what are they? ::@:: $V_{CC}$ is the DC supply rail feeding the collector/load network. $V_{CE}=V_C-V_E$ is the collector-to-emitter voltage.
- emitter current relation: what does KCL at the BJT give? ::@:: KCL at the transistor gives $I_E=I_C+I_B$; in normal operation $I_E$ is only slightly larger than $I_C$ for both NPN and PNP.

### off mode

When $V_{BE}<0.7\text{ V}$, the transistor is off and there is essentially no base current ($I_B\approx0$) or collector current ($I_C\approx0$).

---

Flashcards for this section are as follows:

- base–emitter diode behaviour: NPN B–E junction? ::@:: The B–E junction acts like a diode: off below $0.7\text{ V}$ with negligible base current; conducting above $0.7\text{ V}$.

### amplification mode

When $V_{BE}>0.7\text{ V}$ and the transistor is biased appropriately, it can operate in amplification mode where the collector current is approximately proportional to the base current: $I_C\approx\beta I_B$, where $\beta$ is the current gain (typically in the range $20$ – $300$). In amplification (sometimes called "active") mode, the transistor behaves like a controlled current source: a small change in $I_B$ produces a much larger change in $I_C$ while $V_{CE}$ stays somewhere between $0.2\text{ V}$ and the supply voltage.

---

Flashcards for this section are as follows:

- transistor current gain: in which mode? ::@:: In amplification mode $I_C\approx\beta I_B$, where $\beta$ is typically $20$ – $300$.
- beta typical range: what does $\beta\approx 20$ – $300$ mean? ::@:: The collector current can be tens to hundreds of times the base current in active mode.

### saturation mode

In saturation mode, $I_C$ is limited by the external circuit rather than by $\beta I_B$, and the collector–emitter voltage drops to a small value (about $0.2\text{ V}$) similar to a closed switch.

---

Flashcards for this section are as follows:

- saturation: what defines it? ::@:: In saturation, base drive is strong enough that the collector current is limited by the external circuit: $I_C\approx I_{C,\max}$ and $V_{CE}\approx V_{CE,\text{sat}}\approx0.2\text{ V}$.
- transistor operation modes: list them. ::@:: OFF (no base or collector current), AMPLIFICATION ($I_C\approx\beta I_B$), and SATURATION ($I_C$ at maximum, small $V_{CE}$, additional base current has little effect).

### worked mode check

In the lecture example, an NPN transistor with current gain $\beta\approx100$ has its collector connected through a $1\text{ k}\Omega$ resistor to a $5\text{ V}$ supply, and its base driven through a $10\text{ k}\Omega$ resistor from an input $V_{\text{IN}}$. For $V_{\text{IN}}=0.8\text{ V}$, the base current in active mode is approximately $I_B\approx(0.8\text{ V}-0.7\text{ V})/10\text{ k}\Omega=10\,\mu\text{A}$, giving a collector current $I_C\approx\beta I_B\approx1\text{ mA}$ and a collector voltage $V_{\text{out}}\approx5\text{ V}-I_C\cdot1\text{ k}\Omega\approx4\text{ V}$. For $V_{\text{IN}}=1\text{ V}$, $I_B\approx30\,\mu\text{A}$, $I_C\approx3\text{ mA}$ and $V_{\text{out}}\approx2\text{ V}$. When $V_{\text{IN}}=3\text{ V}$, the naive active-mode calculation would predict $I_C\approx23\text{ mA}$, but the $5\text{ V}$ supply and $1\text{ k}\Omega$ resistor can only provide about $(5\text{ V}-0.2\text{ V})/1\text{ k}\Omega\approx4.8\text{ mA}$ in saturation, so the transistor saturates and $V_{CE}$ drops to about $0.2\text{ V}$.

The three basic operating modes:

- OFF mode: $I_B\approx0$, transistor does not conduct; $I_C\approx0$.
- AMPLIFICATION mode: small changes in $I_B$ cause proportional changes in $I_C$ via $I_C\approx\beta I_B$.
- SATURATION mode: $I_C$ has reached its maximum (set by the external circuit), and additional base current does not significantly increase $I_C$; $V_{CE}$ is small (about $0.2\text{ V}$).

---

Flashcards for this section are as follows:

- active vs saturation check: first compute $\beta I_B$ and $I_{C,\max}$ ::@:: Compute $I_B$ from the base drive, then compute $\beta I_B$ (active-mode capability) and compute $I_{C,\max}$ from the collector/load network (circuit-limited maximum).
- active vs saturation check: which mode applies? ::@:: If $\beta I_B \ge I_{C,\max}$, the transistor saturates: $I_C\approx I_{C,\max}$ and $V_{CE}$ is small. If $\beta I_B < I_{C,\max}$, it stays in active mode: $I_C\approx\beta I_B$.
- lecture numeric case (given $R_B=10\text{ k}\Omega$, $R_C=1\text{ k}\Omega$, $V_{CC}=5\text{ V}$, $\beta\approx100$): if $V_{\text{IN}}=0.8\text{ V}$, find $I_B$, $I_C$, and $V_{\text{out}}(=V_C)$. ::@:: $I_B\approx(0.8\text{ V}-0.7\text{ V})/10\text{ k}\Omega=10\,\mu\text{A}$. In active mode $I_C\approx\beta I_B\approx100\times10\,\mu\text{A}=1\text{ mA}$. Then $V_{\text{out}}=V_C\approx V_{CC}-I_C R_C=5\text{ V}-1\text{ mA}\cdot1\text{ k}\Omega=4\text{ V}$.
- lecture numeric case (given $R_B=10\text{ k}\Omega$, $R_C=1\text{ k}\Omega$, $V_{CC}=5\text{ V}$, $\beta\approx100$): if $V_{\text{IN}}=1\text{ V}$, find $I_B$, $I_C$, and $V_{\text{out}}(=V_C)$. ::@:: $I_B\approx(1.0\text{ V}-0.7\text{ V})/10\text{ k}\Omega=30\,\mu\text{A}$. In active mode $I_C\approx\beta I_B\approx3\text{ mA}$. Then $V_{\text{out}}=V_C\approx5\text{ V}-3\text{ mA}\cdot1\text{ k}\Omega=2\text{ V}$ (still not saturated).
- lecture numeric case (given $R_B=10\text{ k}\Omega$, $R_C=1\text{ k}\Omega$, $V_{CC}=5\text{ V}$, $\beta\approx100$, $V_{CE,\text{sat}}\approx0.2\text{ V}$): if $V_{\text{IN}}=3\text{ V}$, decide active vs saturation and find $I_C$ and $V_{CE}$. ::@:: Drive gives $I_B\approx(3.0\text{ V}-0.7\text{ V})/10\text{ k}\Omega=230\,\mu\text{A}$ so $\beta I_B\approx23\text{ mA}$. But the collector network limits current to $I_{C,\max}\approx(V_{CC}-V_{CE,\text{sat}})/R_C\approx(5.0-0.2)/1\text{ k}\Omega=4.8\text{ mA}$. Since $\beta I_B \gg I_{C,\max}$, the transistor saturates: $I_C\approx I_{C,\max}\approx4.8\text{ mA}$ and $V_{CE}\approx V_{CE,\text{sat}}\approx0.2\text{ V}$.
- maximum collector current: how to compute $I_{C,\max}$? ::@:: For a collector resistor $R_C$ to supply $V_{CC}$, when saturated $V_{CE}\approx V_{CE,\text{sat}}$, so $I_{C,\max}\approx(V_{CC}-V_{CE,\text{sat}})/R_C$.
- saturation vs amplification: which formula applies? ::@:: In active mode, $I_C\approx\beta I_B$ and $V_{CE}$ is not forced small. In saturation, $I_C\approx I_{C,\max}$ and $V_{CE}\approx0.2\text{ V}$, so $I_C<\beta I_B$.
- why drive into saturation for switching? ::@:: Saturation makes the transistor act like a closed switch: $V_{CE}\approx0.2\text{ V}$, so most of $V_{CC}$ appears across the load.

## transistor as inverter

The same NPN resistor-loaded circuit (collector to $V_{CC}$ through $R_C$, base driven through $R_B$) behaves as a __logic inverter__. Logical HIGH and LOW come from comparing $V_C$ and $V_E$.

When the input is low (below about $0.7\text{ V}$), the transistor is off. $V_C$ stays high (near $V_{CC}$) and $V_E$ is at ground, so $V_C - V_E$ is large: __logical HIGH__. When the input is high enough to saturate the transistor, $V_C$ drops to only slightly above $V_E$ (about $0.2\text{ V}$ difference): __logical LOW__. Input LOW gives output HIGH; input HIGH gives output LOW.

The input voltage at which the transistor just enters saturation is called $V_{\text{sat}}$. It is found by equating $\beta I_B$ to the collector circuit's maximum current $I_{C,\max}$. Base current is $I_B = (V_{\text{sat}} - 0.7\text{ V})/R_B$; the circuit limit is $I_{C,\max} = (V_{CC} - 0.2\text{ V})/R_C$. Setting $\beta I_B = I_{C,\max}$ and solving gives $V_{\text{sat}} = 0.7\text{ V} + R_B(V_{CC} - 0.2\text{ V})/(\beta R_C)$. For the lecture example ($R_B = 10\text{ k}\Omega$, $R_C = 1\text{ k}\Omega$, $V_{CC} = 5\text{ V}$, $\beta = 100$), $V_{\text{sat}} = 1.18\text{ V}$; inputs above that saturate the transistor and give a low output.

---

Flashcards for this section are as follows:

- inverter: how are logical HIGH and LOW defined? ::@:: By comparing $V_C$ and $V_E$: large $V_C - V_E$ is logical HIGH; small difference (about $0.2\text{ V}$) is logical LOW.
- NPN circuit as inverter: what is the logic behaviour? ::@:: Input LOW (transistor off): $V_C$ high, $V_E$ at ground, so output is logical HIGH. Input HIGH (transistor saturated): $V_C$ only slightly above $V_E$, so output is logical LOW.
- saturation voltage $V_{\text{sat}}$: how is it found? ::@:: Set $\beta I_B = I_{C,\max}$. Use $I_B = (V_{\text{sat}} - 0.7\text{ V})/R_B$ and $I_{C,\max} = (V_{CC} - 0.2\text{ V})/R_C$; solve for $V_{\text{sat}}$.
- lecture $V_{\text{sat}}$ example: what is $V_{\text{sat}}$? ::@:: $V_{\text{sat}} = 1.18\text{ V}$; for input above that the transistor is saturated and output is low.
- logical LOW in inverter: why is small $V_C - V_E$ treated as logic LOW? ::@:: The logic level is defined by $V_C$ relative to $V_E$; when that difference is small, it is logical LOW.

## transistor as a switch

In digital or motor-control circuits, a BJT is often used as an on–off switch. A __low-side switch__ is one where the switching device sits between the load and ground (the "low" side of the supply); current flows from the positive supply through the load, then through the transistor to ground. (A high-side switch would sit between the supply and the load instead.) For an NPN transistor used as a low-side switch, the emitter is tied to ground, the collector connects to the load and then to a positive supply, and a base resistor $R_B$ limits the base current from a control voltage $V_{\text{IN}}$. When $V_{\text{IN}}$ is below about $0.7\text{ V}$, the transistor is off and no significant collector current flows. When $V_{\text{IN}}$ is driven high enough to provide sufficient base current, the transistor saturates, pulling the collector near ground (with $V_{CE}\approx0.2\text{ V}$) and turning the load on. <p> ![NPN low-side switch schematic](attachments/npn_low_side_switch.svg)

A typical design procedure: (1) determine the desired collector current from the load and supply, (2) pick a conservative $\beta_{\text{forced}}$ and compute $I_B=I_C/\beta_{\text{forced}}$, (3) choose $R_B$ so the base–emitter junction sees about $0.7\text{ V}$ at the high input level with sufficient $I_B$, and (4) verify $V_{CE}$ drops to $\approx0.2\text{ V}$ and the transistor's power rating is not exceeded.

A base resistor limits $I_B$: $I_B\approx(V_{\text{IN}}-0.7\text{ V})/R_B$ when on. Then check whether $I_C\le\beta I_B$ (amplification) or the transistor saturates with $I_C$ limited by the external circuit.

---

Flashcards for this section are as follows:

- low-side switch (vs high-side): what is it? ::@:: A low-side switch is between the load and ground: current flows from supply → load → switch → ground. The transistor is on the "low" (ground) side of the load. High-side would put the switch between supply and load.
- low-side NPN switch connections (E, C, base, load) ::@:: For an NPN low-side switch: emitter to ground, collector to the load, and the other side of the load to the positive supply; the base is driven from the control signal through a resistor. <p> ![NPN low-side switch schematic](attachments/npn_low_side_switch.svg)
- low-side NPN switch behaviour ($V_{BE}\approx0.7\text{ V}$, $V_{CE}\approx0.2\text{ V}$) <p> ![NPN low-side switch schematic](attachments/npn_low_side_switch.svg) ::@:: Low input gives $V_{BE}<0.7\text{ V}$ so the transistor is OFF and $I_C\approx0$. High enough input provides base current; with sufficient drive the transistor saturates and pulls the collector near ground with $V_{CE}\approx0.2\text{ V}$.
- need for base resistor: why use $R_B$? ::@:: A base resistor limits base current so the transistor is not overdriven; $I_B\approx(V_{\text{IN}}-0.7\text{ V})/R_B$ when on.
- saturation $V_{CE}$: what is $V_{CE}$ in saturation? ::@:: In saturation a BJT has $V_{CE}$ around $0.2\text{ V}$, even though collector current is at its maximum set by the load and supply.
- sizing base resistor for switch: steps? ::@:: Estimate $I_C$ from the load, choose a conservative $\beta_{\text{forced}}$ and compute $I_B=I_C/\beta_{\text{forced}}$, then use $R_B\approx(V_{\text{IN}}-0.7\text{ V})/I_B$ when the input is high.
