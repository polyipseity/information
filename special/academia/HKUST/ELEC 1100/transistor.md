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

A transistor is a three-terminal semiconductor device that can amplify or switch current. In this course we focus on bipolar junction transistors (BJTs) of types NPN and PNP, which are constructed by adding a third layer to a PN junction. The three terminals are called collector (C), base (B), and emitter (E). In practical ELEC 1100 circuits, transistors appear as motor-control switches (on/off control of current) in the [H-bridge](H-bridge.md) and as current "gainers" that allow a small sensor or logic current at the base to control a much larger current at the collector.

---

Flashcards for this section are as follows:

- transistor definition: What is a transistor in terms of terminals and function? ::@:: A transistor is a three-terminal semiconductor device (collector, base, emitter) that can amplify or switch current between two terminals under control of the third. <!--SR:!2026-06-10,65,310!2026-05-17,43,290-->
- BJT types: What are the two standard BJT types? ::@:: The two common BJTs are NPN and PNP, distinguished by the order of N and P semiconductor regions. <!--SR:!2026-06-06,62,310!2026-06-07,63,310-->
- controlled path in a BJT: Which path does the base current control in this course's circuits? ::@:: In our NPN/PNP examples the small base current (between base and emitter) controls a much larger current between collector and emitter. <!--SR:!2026-05-30,56,310!2026-06-04,60,310-->
- transistor use in this course: switching ::@:: In ELEC 1100 we use BJTs as on/off switches to control current through motors and other loads. <!--SR:!2026-06-01,58,310!2026-05-30,56,310-->
- transistor use in this course: current gain ::@:: In ELEC 1100 we also use BJTs for current gain: a small base current from logic/sensors can control a much larger collector current. <!--SR:!2026-06-02,58,310!2026-06-02,58,310-->

## structure

A BJT can be viewed as a [PN junction diode](diode.md#pn%20junction%20and%20biasing) with an additional layer added, forming either NPN or PNP structures. The base region is thin and lightly doped, while the emitter and collector are more heavily doped to support current injection and collection. Qualitatively, the emitter is the "source" of carriers, the collector is where they are collected, and the base controls how easily carriers move across the structure. <p> ![NPN BJT symbol](attachments/symbol_npn.svg) <p> ![PNP BJT symbol](attachments/symbol_pnp.svg)

In the common symbol convention, for an NPN transistor the emitter terminal is the one with an arrow pointing *out* of the device (from emitter to base), while for a PNP transistor the emitter arrow points *into* the device (toward the base). In both symbols the base is the middle leg, and the collector is the remaining terminal without an arrow. Remember that schematic symbols depict current directions and layers, not physical pin ordering on a package; the actual pinout is given by the datasheet.

For analysis, a simple equivalent circuit models the base–emitter junction as a diode and the collector–emitter path as a dependent current source $I_C=\beta I_B$. For an **NPN** transistor the B–E diode has its anode at the base and cathode at the emitter (forward when $V_{BE}>0.7\text{ V}$), and the dependent current source drives current from collector to emitter. For a **PNP** transistor the E–B diode has its anode at the emitter and cathode at the base (forward when the emitter is more positive than the base), and the dependent current source drives current from emitter to collector. <p> ![NPN BJT equivalent: diode and dependent current source](attachments/equivalent_npn.svg) <p> ![PNP BJT equivalent: diode and dependent current source](attachments/equivalent_pnp.svg)

---

Flashcards for this section are as follows:

- BJT terminals ::@:: The three BJT terminals are collector (C), base (B), and emitter (E); in the schematic symbol the base is the middle leg, the emitter is the leg with the arrow, and the collector is the remaining leg without an arrow. <!--SR:!2026-06-09,64,310!2026-05-28,54,310-->
- npn vs pnp arrow direction ::@:: In the standard symbols the NPN emitter arrow points out of the transistor (from emitter to base), while the PNP emitter arrow points into the transistor (toward the base); a mnemonic is "NPN: arrow Not Pointing iN". <!--SR:!2026-06-11,66,310!2026-06-04,60,310-->
- emitter vs collector role ::@:: The emitter is heavily doped and acts as the source of carriers, the collector gathers those carriers, and the base is a thin control region that regulates how much emitter current reaches the collector. <!--SR:!2026-06-10,65,310!2026-05-29,55,310-->
- schematic symbol: NPN BJT <p> ![NPN BJT symbol](attachments/symbol_npn.svg) ::@:: NPN transistor symbol with emitter arrow pointing out; terminals are base (B), collector (C), emitter (E). <!--SR:!2026-06-12,67,310!2026-06-03,59,310-->
- schematic symbol: PNP BJT <p> ![PNP BJT symbol](attachments/symbol_pnp.svg) ::@:: PNP transistor symbol with emitter arrow pointing in; terminals are base (B), collector (C), emitter (E). <!--SR:!2026-06-11,66,310!2026-06-05,61,310-->
- equivalent circuit (diode + $\beta I_B$): what does it model? ::@:: The base–emitter junction is modelled as a diode; the collector–emitter path is modelled as a dependent current source $I_C=\beta I_B$ placed on the collector side. <!--SR:!2026-05-17,43,290!2026-06-10,65,310-->
- equivalent schematic: NPN <p> ![NPN BJT equivalent](attachments/equivalent_npn.svg) ::@:: NPN equivalent: B–E diode (anode at B, cathode at E) and dependent current source $\beta I_B$ from collector to emitter on the collector side. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-06-05,61,310!2026-06-11,66,310-->
- equivalent schematic: PNP <p> ![PNP BJT equivalent](attachments/equivalent_pnp.svg) ::@:: PNP equivalent: E–B diode (anode at E, cathode at B) and dependent current source $\beta I_B$ from emitter to collector on the collector side. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-17,43,290!2026-06-09,64,310-->

## historical context

Historically, the first working transistor was demonstrated at Bell Labs in 1947 by John Bardeen, Walter Brattain, and William Shockley. Transistors became the fundamental building blocks of modern electronics, enabling compact integrated circuits and the development of computers, mobile phones, and many other devices. Shockley later founded a semiconductor company in Palo Alto, triggering the growth of Silicon Valley.

---

Flashcards for this section are as follows:

- transistor historical significance ::@:: The transistor, invented at Bell Labs in 1947, is the key component enabling modern electronics (computers, phones, etc.) and helped launch Silicon Valley through Shockley's semiconductor company and his hires. <!--SR:!2026-06-11,66,310!2026-05-24,48,290-->

## transistor operation modes

For an NPN BJT, the base–emitter (B–E) junction behaves like a diode with an approximate forward drop of $0.7\text{ V}$. When $V_{BE}<0.7\text{ V}$, the transistor is off and there is essentially no base current ($I_B\approx0$) or collector current ($I_C\approx0$). When $V_{BE}>0.7\text{ V}$ and the transistor is biased appropriately, it can operate in amplification mode where the collector current is approximately proportional to the base current: $I_C\approx\beta I_B$, where $\beta$ is the current gain (typically in the range $20$ – $300$).

Two voltages appear often in BJT circuits:

- $V_{CC}$: the DC supply voltage feeding the collector/load network (e.g. the " $5\text{ V}$ rail").
- $V_{CE}$: the collector-to-emitter voltage, defined as $V_{CE}=V_C-V_E$ (for an NPN low-side switch, $V_E$ is usually $0\text{ V}$ so $V_{CE}\approx V_C$).

[Kirchhoff's current law](Kirchhoff%27s%20circuit%20laws.md#kirchhoff%27s%20current%20law) at the transistor gives $I_E=I_C+I_B$ when all three currents are defined as **leaving** the transistor; in practice we often draw NPN currents flowing *into* the device at C and B and *out* at E, or the opposite for PNP, but the magnitude relation "emitter current equals base plus collector" still holds in either case.

In amplification (sometimes called "active") mode, the transistor behaves like a controlled current source: a small change in $I_B$ produces a much larger change in $I_C$ while $V_{CE}$ stays somewhere between $0.2\text{ V}$ and the supply voltage. In saturation mode, $I_C$ is limited by the external circuit rather than by $\beta I_B$, and the collector–emitter voltage drops to a small value (about $0.2\text{ V}$) similar to a closed switch.

In the lecture example, an NPN transistor with current gain $\beta\approx100$ has its collector connected through a $1\text{ k}\Omega$ resistor to a $5\text{ V}$ supply, and its base driven through a $10\text{ k}\Omega$ resistor from an input $V_{\text{IN}}$. For $V_{\text{IN}}=0.8\text{ V}$, the base current in active mode is approximately $I_B\approx(0.8\text{ V}-0.7\text{ V})/10\text{ k}\Omega=10\,\mu\text{A}$, giving a collector current $I_C\approx\beta I_B\approx1\text{ mA}$ and a collector voltage $V_{\text{out}}\approx5\text{ V}-I_C\cdot1\text{ k}\Omega\approx4\text{ V}$. For $V_{\text{IN}}=1\text{ V}$, $I_B\approx30\,\mu\text{A}$, $I_C\approx3\text{ mA}$ and $V_{\text{out}}\approx2\text{ V}$. When $V_{\text{IN}}=3\text{ V}$, the naive active-mode calculation would predict $I_C\approx23\text{ mA}$, but the $5\text{ V}$ supply and $1\text{ k}\Omega$ resistor can only provide about $(5\text{ V}-0.2\text{ V})/1\text{ k}\Omega\approx4.8\text{ mA}$ in saturation, so the transistor saturates and $V_{CE}$ drops to about $0.2\text{ V}$.

The three basic operating modes discussed in this course are:

- OFF mode: $I_B\approx0$, transistor does not conduct; $I_C\approx0$.
- AMPLIFICATION mode: small changes in $I_B$ cause proportional changes in $I_C$ via $I_C\approx\beta I_B$.
- SATURATION mode: $I_C$ has reached its maximum (set by the external circuit), and additional base current does not significantly increase $I_C$; $V_{CE}$ is small (about $0.2\text{ V}$).

---

Flashcards for this section are as follows:

- base–emitter diode behaviour ($V_{BE}<0.7\text{ V}$ vs $>0.7\text{ V}$): NPN B–E junction? ::@:: The B–E junction of an NPN transistor behaves like a diode: for $V_{BE}<0.7\text{ V}$ it is off with negligible base current; for $V_{BE}>0.7\text{ V}$ it conducts and allows base current to flow. <!--SR:!2026-05-30,56,310!2026-06-04,60,310-->
- meaning of $V_{CC}$ and $V_{CE}$ ($V_{CE}=V_C-V_E$): what are they? ::@:: $V_{CC}$ is the DC supply rail that feeds the collector/load network (e.g. $5\text{ V}$). $V_{CE}$ is the voltage from collector to emitter: $V_{CE}=V_C-V_E$. <!--SR:!2026-06-11,66,310!2026-06-05,61,310-->
- transistor current gain relation ($I_C\approx\beta I_B$): in which mode? ::@:: In amplification mode the collector current is approximately $I_C\approx\beta I_B$, where $\beta$ is the transistor's current gain (typically $20$ – $300$). <!--SR:!2026-05-17,43,290!2026-06-12,67,310-->
- transistor operation modes (OFF, AMP with $I_C\approx\beta I_B$, SAT): list them. ::@:: The three main BJT modes are OFF (no base or collector current), AMPLIFICATION ($I_C\approx\beta I_B$), and SATURATION (collector current at maximum with small $V_{CE}$ and further base current having little effect). <!--SR:!2026-05-31,57,310!2026-05-28,54,310-->
- emitter current relation ($I_E=I_C+I_B$): what does KCL at the BJT give? ::@:: For suitably chosen current directions, Kirchhoff's current law at the transistor gives $I_E=I_C+I_B$; in magnitude this means the emitter current is approximately the sum of the base and collector currents, so in normal operation $I_E$ is only slightly larger than $I_C$ for both NPN and PNP devices. <!--SR:!2026-06-04,60,310!2026-05-31,57,310-->
- active vs saturation check: compute $\beta I_B$ and $I_{C,\max}$ first ::@:: Compute $I_B$ from the base drive, then compute $\beta I_B$ (active-mode capability) and compute $I_{C,\max}$ from the collector/load network (circuit-limited maximum). <!--SR:!2026-06-06,62,310!2026-06-05,61,310-->
- active vs saturation check: decide which mode and $I_C$ formula ::@:: If $\beta I_B \ge I_{C,\max}$, the transistor can be in saturation so $I_C\approx I_{C,\max}$ and $V_{CE}$ is small. If $\beta I_B < I_{C,\max}$, it stays in active mode so $I_C\approx\beta I_B$. <!--SR:!2026-05-29,55,310!2026-06-10,65,310-->
- beta typical range meaning ($\beta$ typically $20$ – $300$): what does it imply? ::@:: A typical BJT has current gain $\beta$ in the range $20$ – $300$, meaning the collector current can be tens to hundreds of times larger than the base current in active mode. <!--SR:!2026-06-07,63,310!2026-06-12,67,310-->
- lecture numeric case (given $R_B=10\text{ k}\Omega$, $R_C=1\text{ k}\Omega$, $V_{CC}=5\text{ V}$, $\beta\approx100$): if $V_{\text{IN}}=0.8\text{ V}$, find $I_B$, $I_C$, and $V_{\text{out}}(=V_C)$. ::@:: $I_B\approx(0.8\text{ V}-0.7\text{ V})/10\text{ k}\Omega=10\,\mu\text{A}$. In active mode $I_C\approx\beta I_B\approx100\times10\,\mu\text{A}=1\text{ mA}$. Then $V_{\text{out}}=V_C\approx V_{CC}-I_C R_C=5\text{ V}-1\text{ mA}\cdot1\text{ k}\Omega=4\text{ V}$. <!--SR:!2026-05-20,45,290!2026-05-18,43,290-->
- lecture numeric case (given $R_B=10\text{ k}\Omega$, $R_C=1\text{ k}\Omega$, $V_{CC}=5\text{ V}$, $\beta\approx100$): if $V_{\text{IN}}=1\text{ V}$, find $I_B$, $I_C$, and $V_{\text{out}}(=V_C)$. ::@:: $I_B\approx(1.0\text{ V}-0.7\text{ V})/10\text{ k}\Omega=30\,\mu\text{A}$. In active mode $I_C\approx\beta I_B\approx3\text{ mA}$. Then $V_{\text{out}}=V_C\approx5\text{ V}-3\text{ mA}\cdot1\text{ k}\Omega=2\text{ V}$ (still not saturated). <!--SR:!2026-06-02,58,310!2026-05-17,43,290-->
- lecture numeric case (given $R_B=10\text{ k}\Omega$, $R_C=1\text{ k}\Omega$, $V_{CC}=5\text{ V}$, $\beta\approx100$, $V_{CE,\text{sat}}\approx0.2\text{ V}$): if $V_{\text{IN}}=3\text{ V}$, decide active vs saturation and find $I_C$ and $V_{CE}$. ::@:: Drive gives $I_B\approx(3.0\text{ V}-0.7\text{ V})/10\text{ k}\Omega=230\,\mu\text{A}$ so $\beta I_B\approx23\text{ mA}$. But the collector network limits current to $I_{C,\max}\approx(V_{CC}-V_{CE,\text{sat}})/R_C\approx(5.0-0.2)/1\text{ k}\Omega=4.8\text{ mA}$. Since $\beta I_B \gg I_{C,\max}$, the transistor saturates: $I_C\approx I_{C,\max}\approx4.8\text{ mA}$ and $V_{CE}\approx V_{CE,\text{sat}}\approx0.2\text{ V}$. <!--SR:!2026-05-19,44,290!2026-05-02,31,270-->
- saturation idea (use $I_{C,\max}$ and $V_{CE,\text{sat}}\approx0.2\text{ V}$): what defines saturation? ::@:: In saturation, base drive is strong enough that the collector current is limited by the external circuit, so $I_C$ is approximately the maximum allowed by the collector/load network: $I_C\approx I_{C,\max}$, and the collector–emitter voltage is small: $V_{CE}\approx V_{CE,\text{sat}}\approx0.2\text{ V}$. <!--SR:!2026-06-03,59,310!2026-05-22,46,290-->
- maximum collector current $I_{C,\max}$ (given $V_{CC}$, $R_C$, $V_{CE,\text{sat}}$): how to compute? ::@:: For a collector resistor $R_C$ to a supply $V_{CC}$, when saturated the transistor has $V_{CE}\approx V_{CE,\text{sat}}$ so the resistor sees about $V_{CC}-V_{CE,\text{sat}}$. Thus $I_{C,\max}\approx(V_{CC}-V_{CE,\text{sat}})/R_C$ (with $V_{CE,\text{sat}}\approx0.2\text{ V}$). <!--SR:!2026-06-01,58,310!2026-04-24,19,270-->
- saturation vs amplification ($I_C\approx I_{C,\max}$ vs $I_C\approx\beta I_B$): which formula applies when? ::@:: In active (amplification) mode, $I_C\approx\beta I_B$ and $V_{CE}$ is not forced small. In saturation, the circuit forces $I_C\approx I_{C,\max}$ and $V_{CE}\approx0.2\text{ V}$, so typically $I_C<\beta I_B$. <!--SR:!2026-06-10,65,310!2026-06-11,66,310-->
- why drive into saturation for switching ($V_{CE,\text{sat}}\approx0.2\text{ V}$): why? ::@:: Saturation makes the transistor behave like a closed switch: $V_{CE}$ is small (about $0.2\text{ V}$) so most of $V_{CC}$ appears across the load, giving near-maximum load current and low voltage drop across the transistor. <!--SR:!2026-06-09,64,310!2026-06-07,63,310-->

## transistor as inverter

The same NPN resistor-loaded circuit (collector to $V_{CC}$ through $R_C$, base driven through $R_B$) behaves as a **logic inverter**. Logical HIGH and LOW are determined by comparing collector voltage $V_C$ and emitter voltage $V_E$.

When the input is low (below about $0.7\text{ V}$), the transistor is off. Then $V_C$ stays high (near $V_{CC}$) and $V_E$ is at ground, so the difference $V_C - V_E$ is large: that is **logical HIGH**. When the input is high enough to saturate the transistor, $V_C$ drops to only slightly above $V_E$ (about $0.2\text{ V}$ difference), so the output is **logical LOW**. So input LOW gives output HIGH, and input HIGH gives output LOW.

The input voltage at which the transistor just enters saturation is called $V_{\text{sat}}$. It is found by equating the active-mode current $\beta I_B$ to the maximum current the collector circuit can deliver, $I_{C,\max}$. Base current is $I_B = (V_{\text{sat}} - 0.7\text{ V})/R_B$; the circuit limit is $I_{C,\max} = (V_{CC} - 0.2\text{ V})/R_C$. Setting $\beta I_B = I_{C,\max}$ and solving gives $V_{\text{sat}} = 0.7\text{ V} + R_B(V_{CC} - 0.2\text{ V})/(\beta R_C)$. For the lecture example ($R_B = 10\text{ k}\Omega$, $R_C = 1\text{ k}\Omega$, $V_{CC} = 5\text{ V}$, $\beta = 100$) this yields $V_{\text{sat}} = 1.18\text{ V}$: for inputs above that, the transistor is in saturation and the output is low.

---

Flashcards for this section are as follows:

- inverter: how are logical HIGH and logical LOW defined? ($V_C$, $V_E$) ::@:: By comparing $V_C$ and $V_E$: large $V_C - V_E$ is logical HIGH; small difference (about $0.2\text{ V}$) is logical LOW. <!--SR:!2026-05-16,42,290!2026-06-09,64,310-->
- NPN circuit as inverter: what is the logic behaviour? (input LOW vs HIGH; $V_C$, $V_E$, output level) ::@:: Input LOW (transistor off): $V_C$ high, $V_E$ at ground, so output is logical HIGH. Input HIGH (transistor saturated): $V_C$ only slightly above $V_E$, so output is logical LOW. <!--SR:!2026-06-12,67,310!2026-05-30,56,310-->
- saturation voltage $V_{\text{sat}}$: how is it found? (equate $\beta I_B$ and $I_{C,\max}$) ::@:: Set $\beta I_B = I_{C,\max}$. Use $I_B = (V_{\text{sat}} - 0.7\text{ V})/R_B$ and $I_{C,\max} = (V_{CC} - 0.2\text{ V})/R_C$; solve for $V_{\text{sat}}$. <!--SR:!2026-06-06,62,310!2026-05-17,43,290-->
- lecture $V_{\text{sat}}$ example: $R_B = 10\text{ k}\Omega$, $R_C = 1\text{ k}\Omega$, $V_{CC} = 5\text{ V}$, $\beta = 100$. What is $V_{\text{sat}}$? ::@:: $V_{\text{sat}} = 1.18\text{ V}$; for input above that the transistor is saturated and output is low. <!--SR:!2026-05-17,43,290!2026-06-03,59,310-->
- logical LOW in inverter: why is the small $V_C - V_E$ (about $0.2\text{ V}$) treated as logic LOW? ::@:: The logic level is defined by $V_C$ relative to $V_E$; when that difference is small, it is accepted as logical LOW. <!--SR:!2026-06-01,58,310!2026-05-17,43,290-->

## transistor as a switch

In digital or motor-control circuits, a BJT is often used as an on–off switch. A **low-side switch** is one where the switching device sits between the load and ground (the "low" side of the supply); current flows from the positive supply through the load, then through the transistor to ground. (A high-side switch would sit between the supply and the load instead.) For an NPN transistor used as a low-side switch, the emitter is tied to ground, the collector connects to the load and then to a positive supply, and a base resistor $R_B$ limits the base current from a control voltage $V_{\text{IN}}$. When $V_{\text{IN}}$ is below about $0.7\text{ V}$, the transistor is off and no significant collector current flows. When $V_{\text{IN}}$ is driven high enough to provide sufficient base current, the transistor saturates, pulling the collector near ground (with $V_{CE}\approx0.2\text{ V}$) and turning the load on. <p> ![NPN low-side switch schematic](attachments/npn_low_side_switch.svg)

A typical design procedure for a switch is: (1) determine the desired collector current from the load and supply, (2) pick a conservative $\beta_{\text{forced}}$ (smaller than the datasheet $\beta$) and compute the required base current $I_B=I_C/\beta_{\text{forced}}$, (3) choose $R_B$ so that when the input is at its high level the base–emitter junction sees about $0.7\text{ V}$ and the resulting $I_B$ meets or exceeds the required value, and (4) verify that $V_{CE}$ will drop to $\approx0.2\text{ V}$ and that the transistor's power rating is not exceeded.

A base resistor is essential to limit $I_B$; a typical analysis computes $I_B\approx(V_{\text{IN}}-0.7\text{ V})/R_B$ in the on state, estimates the required $I_C$ from the load and supply, and checks whether $I_C\le\beta I_B$ (amplification region) or whether the transistor must be in saturation with $I_C$ limited by the external circuit.

---

Flashcards for this section are as follows:

- low-side switch (vs high-side): what is it? ::@:: A low-side switch is between the load and ground: current flows from supply → load → switch → ground. The transistor is on the "low" (ground) side of the load. High-side would put the switch between supply and load. <!--SR:!2026-06-10,65,310!2026-05-31,57,310-->
- low-side NPN switch connections (E, C, base, load) ::@:: For an NPN low-side switch: emitter to ground, collector to the load, and the other side of the load to the positive supply; the base is driven from the control signal through a resistor. <p> ![NPN low-side switch schematic](attachments/npn_low_side_switch.svg) <!--SR:!2026-05-20,45,290!2026-05-17,43,290-->
- low-side NPN switch behaviour ($V_{BE}\approx0.7\text{ V}$, $V_{CE}\approx0.2\text{ V}$) <p> ![NPN low-side switch schematic](attachments/npn_low_side_switch.svg) ::@:: Low input gives $V_{BE}<0.7\text{ V}$ so the transistor is OFF and $I_C\approx0$. High enough input provides base current; with sufficient drive the transistor saturates and pulls the collector near ground with $V_{CE}\approx0.2\text{ V}$. <!--SR:!2026-06-12,67,310!2026-06-03,59,310-->
- need for base resistor ($I_B\approx(V_{\text{IN}}-0.7\text{ V})/R_B$ when on): why use $R_B$? ::@:: A base resistor limits base current so the transistor is not overdriven; $I_B\approx(V_{\text{IN}}-0.7\text{ V})/R_B$ when on. <!--SR:!2026-05-29,55,310!2026-05-28,54,310-->
- saturation collector–emitter voltage (about $0.2\text{ V}$): what is $V_{CE}$ in saturation? ::@:: In saturation a BJT typically has a small collector–emitter voltage, about $0.2\text{ V}$, even though the collector current is at its maximum set by the load and supply. <!--SR:!2026-06-12,67,310!2026-06-09,64,310-->
- sizing base resistor for switch ($R_B\approx(V_{\text{IN}}-0.7\text{ V})/I_B$): steps? ::@:: To size $R_B$ for a saturated NPN switch, estimate the needed collector current from the load, choose a conservative $\beta_{\text{forced}}$ and compute $I_B=I_C/\beta_{\text{forced}}$, then use $R_B\approx(V_{\text{IN}}-0.7\text{ V})/I_B$ when the input is high. <!--SR:!2026-06-09,64,310!2026-05-19,44,290-->
