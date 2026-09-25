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

- transistor definition: what is a transistor in terms of terminals and function? ::@:: A transistor is a three-terminal semiconductor device (collector, base, emitter) that can amplify or switch current between two terminals under control of the third. <!--SR:!fsrs,2027-05-12T10:13:49.801Z,332,332.24027195,1,2,7,0,0,2026-06-14T10:13:49.801Z!2026-11-05,172,310-->
- BJT types: what are the two standard BJT types? ::@:: The two common BJTs are NPN and PNP, distinguished by the order of N and P semiconductor regions. <!--SR:!fsrs,2027-04-18T02:05:41.368Z,314,314.10478149,1,2,7,0,0,2026-06-08T02:05:41.368Z!fsrs,2027-04-20T02:05:43.727Z,316,315.61032191,1,2,7,0,0,2026-06-08T02:05:43.727Z-->
- controlled path in a BJT: which path does the base current control? ::@:: In our NPN/PNP examples the small base current (between base and emitter) controls a much larger current between collector and emitter. <!--SR:!2027-01-30,245,330!2027-02-21,262,330-->
- transistor use: switching ::@:: In ELEC 1100 we use BJTs as on/off switches to control current through motors and other loads. <!--SR:!2027-02-10,254,330!2027-01-28,243,330-->
- transistor use: current gain ::@:: In ELEC 1100 we also use BJTs for current gain: a small base current from logic/sensors can control a much larger collector current. <!--SR:!2027-02-08,250,330!2027-02-13,255,330-->

## structure

A BJT is a [PN junction diode](diode.md#pn%20junction%20and%20biasing) with an additional layer, forming either NPN or PNP structures. The base is thin and lightly doped; the emitter and collector are more heavily doped for current injection and collection. The emitter is the carrier source, the collector gathers them, and the base controls how easily carriers cross the structure. <p> ![NPN BJT symbol](attachments/symbol_npn.svg) <p> ![PNP BJT symbol](attachments/symbol_pnp.svg)

In the NPN symbol the emitter arrow points _out_; in PNP it points _in_. The base is the middle leg; the collector has no arrow. Symbols depict current directions, not physical pin ordering; the datasheet gives the actual pinout.

The equivalent circuit models the base–emitter junction as a diode and the collector–emitter path as a dependent current source $I_C=\beta I_B$. For __NPN__, the B–E diode has anode at base, cathode at emitter (forward when $V_{BE}>0.7\text{ V}$); current flows collector to emitter. For __PNP__, the E–B diode has anode at emitter, cathode at base; current flows emitter to collector. <p> ![NPN BJT equivalent: diode and dependent current source](attachments/equivalent_npn.svg) <p> ![PNP BJT equivalent: diode and dependent current source](attachments/equivalent_pnp.svg)

---

Flashcards for this section are as follows:

- BJT terminals ::@:: The three terminals are collector (C), base (B), and emitter (E); in the schematic symbol the base is the middle leg, the emitter has the arrow, and the collector has no arrow. <!--SR:!fsrs,2027-05-11T10:12:24.644Z,331,330.69254451,1,2,7,0,0,2026-06-14T10:12:24.644Z!2027-01-22,237,330-->
- npn vs pnp arrow direction ::@:: The NPN emitter arrow points out (from emitter to base); the PNP arrow points in (toward the base). Mnemonic: "NPN: arrow Not Pointing iN". <!--SR:!fsrs,2027-05-14T10:14:47.658Z,334,333.77014777,1,2,7,0,0,2026-06-14T10:14:47.658Z!2027-02-20,261,330-->
- emitter vs collector role ::@:: The emitter is heavily doped and acts as the carrier source, the collector gathers carriers, and the base is a thin region that regulates how much emitter current reaches the collector. <!--SR:!fsrs,2027-05-12T10:14:04.491Z,332,332.24027195,1,2,7,0,0,2026-06-14T10:14:04.491Z!2027-01-25,240,330-->
- schematic symbol: NPN BJT <p> ![NPN BJT symbol](attachments/symbol_npn.svg) ::@:: NPN transistor symbol with emitter arrow pointing out; terminals are base (B), collector (C), emitter (E). <!--SR:!fsrs,2027-05-15T10:14:53.483Z,335,335.28290091,1,2,7,0,0,2026-06-14T10:14:53.483Z!2027-02-12,254,330-->
- schematic symbol: PNP BJT <p> ![PNP BJT symbol](attachments/symbol_pnp.svg) ::@:: PNP transistor symbol with emitter arrow pointing in; terminals are base (B), collector (C), emitter (E). <!--SR:!fsrs,2027-05-14T10:14:37.544Z,334,333.77014777,1,2,7,0,0,2026-06-14T10:14:37.544Z!fsrs,2027-04-05T05:23:27.017Z,304,304.30256839,1,2,7,0,0,2026-06-05T05:23:27.017Z-->
- equivalent circuit (diode + $\beta I_B$): what does it model? ::@:: The base–emitter junction is a diode; the collector–emitter path is a dependent current source $I_C=\beta I_B$. <!--SR:!2026-11-04,171,310!fsrs,2027-05-12T10:13:45.041Z,332,332.24027195,1,2,7,0,0,2026-06-14T10:13:45.041Z-->
- equivalent schematic: NPN <p> ![NPN BJT equivalent](attachments/equivalent_npn.svg) ::@:: NPN equivalent: B–E diode (anode at B, cathode at E) and dependent current source $\beta I_B$ from collector to emitter. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2027-04-05T05:24:13.460Z,304,304.30256839,1,2,7,0,0,2026-06-05T05:24:13.460Z!fsrs,2027-05-14T10:14:02.673Z,334,333.77014777,1,2,7,0,0,2026-06-14T10:14:02.673Z-->
- equivalent schematic: PNP <p> ![PNP BJT equivalent](attachments/equivalent_pnp.svg) ::@:: PNP equivalent: E–B diode (anode at E, cathode at B) and dependent current source $\beta I_B$ from emitter to collector. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-11-06,173,310!fsrs,2027-05-11T10:14:40.395Z,331,330.69254451,1,2,7,0,0,2026-06-14T10:14:40.395Z-->

## historical context

Historically, the first working transistor was demonstrated at Bell Labs in 1947 by John Bardeen, Walter Brattain, and William Shockley. Transistors enabled compact integrated circuits and eventually computers, mobile phones, and other devices. Shockley later founded Shockley Semiconductor Laboratory in Palo Alto.

---

Flashcards for this section are as follows:

- transistor historical significance ::@:: The transistor, invented at Bell Labs in 1947, enabled compact integrated circuits and modern electronics. Shockley later founded a semiconductor company in Palo Alto. <!--SR:!fsrs,2027-05-14T10:14:50.376Z,334,333.77014777,1,2,7,0,0,2026-06-14T10:14:50.376Z!2026-12-13,197,310-->

## transistor operation modes

For an NPN BJT, the base–emitter junction behaves like a diode with forward drop ~$0.7\text{ V}$. Depending on bias, the device appears as an open switch, a current amplifier, or a saturated switch.

### key voltages and current relation

Two voltages appear often in BJT circuits:

- $V_{CC}$: the DC supply voltage feeding the collector/load network (e.g. the " $5\text{ V}$ rail").
- $V_{CE}$: the collector-to-emitter voltage, defined as $V_{CE}=V_C-V_E$ (for an NPN low-side switch, $V_E$ is usually $0\text{ V}$ so $V_{CE}\approx V_C$).

[Kirchhoff's current law](Kirchhoff%27s%20circuit%20laws.md#kirchhoff%27s%20current%20law) at the transistor gives $I_E=I_C+I_B$. In practice NPN currents flow into C and B and out at E (opposite for PNP), but the magnitude relation holds either way.

---

Flashcards for this section are as follows:

- $V_{CC}$ and $V_{CE}$: what are they? ::@:: $V_{CC}$ is the DC supply rail feeding the collector/load network. $V_{CE}=V_C-V_E$ is the collector-to-emitter voltage. <!--SR:!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z-->
- emitter current relation: what does KCL at the BJT give? ::@:: KCL at the transistor gives $I_E=I_C+I_B$; in normal operation $I_E$ is only slightly larger than $I_C$ for both NPN and PNP. <!--SR:!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z-->

### off mode

When $V_{BE}<0.7\text{ V}$, the transistor is off and there is essentially no base current ($I_B\approx0$) or collector current ($I_C\approx0$).

---

Flashcards for this section are as follows:

- base–emitter diode behaviour: NPN B–E junction? ::@:: The B–E junction acts like a diode: off below $0.7\text{ V}$ with negligible base current; conducting above $0.7\text{ V}$. <!--SR:!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z-->

### amplification mode

When $V_{BE}>0.7\text{ V}$ and the transistor is biased appropriately, it operates in amplification mode: $I_C\approx\beta I_B$, where $\beta$ is typically $20$ – $300$. The transistor behaves like a controlled current source; a small $I_B$ change produces a much larger $I_C$ change while $V_{CE}$ stays between $0.2\text{ V}$ and the supply.

---

Flashcards for this section are as follows:

- transistor current gain: in which mode? ::@:: In amplification mode $I_C\approx\beta I_B$, where $\beta$ is typically $20$ – $300$. <!--SR:!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z-->
- beta typical range: what does $\beta\approx 20$ – $300$ mean? ::@:: The collector current can be tens to hundreds of times the base current in active mode. <!--SR:!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z-->

### saturation mode

In saturation mode, $I_C$ is limited by the external circuit rather than $\beta I_B$; $V_{CE}$ drops to ~$0.2\text{ V}$, similar to a closed switch.

---

Flashcards for this section are as follows:

- saturation: what defines it? ::@:: In saturation, base drive is strong enough that the collector current is limited by the external circuit: $I_C\approx I_{C,\max}$ and $V_{CE}\approx V_{CE,\text{sat}}\approx0.2\text{ V}$. <!--SR:!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z-->
- transistor operation modes: list them. ::@:: OFF (no base or collector current), AMPLIFICATION ($I_C\approx\beta I_B$), and SATURATION ($I_C$ at maximum, small $V_{CE}$, additional base current has little effect). <!--SR:!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z-->

### worked mode check

In the lecture example, an NPN transistor with current gain $\beta\approx100$ has its collector connected through a $1\text{ k}\Omega$ resistor to a $5\text{ V}$ supply, and its base driven through a $10\text{ k}\Omega$ resistor from an input $V_{\text{IN}}$. For $V_{\text{IN}}=0.8\text{ V}$, the base current in active mode is approximately $I_B\approx(0.8\text{ V}-0.7\text{ V})/10\text{ k}\Omega=10\,\mu\text{A}$, giving a collector current $I_C\approx\beta I_B\approx1\text{ mA}$ and a collector voltage $V_{\text{out}}\approx5\text{ V}-I_C\cdot1\text{ k}\Omega\approx4\text{ V}$. For $V_{\text{IN}}=1\text{ V}$, $I_B\approx30\,\mu\text{A}$, $I_C\approx3\text{ mA}$ and $V_{\text{out}}\approx2\text{ V}$. When $V_{\text{IN}}=3\text{ V}$, the naive active-mode calculation would predict $I_C\approx23\text{ mA}$, but the $5\text{ V}$ supply and $1\text{ k}\Omega$ resistor can only provide about $(5\text{ V}-0.2\text{ V})/1\text{ k}\Omega\approx4.8\text{ mA}$ in saturation, so the transistor saturates and $V_{CE}$ drops to about $0.2\text{ V}$.

The three basic operating modes:

- OFF mode: $I_B\approx0$, transistor does not conduct; $I_C\approx0$.
- AMPLIFICATION mode: small changes in $I_B$ cause proportional changes in $I_C$ via $I_C\approx\beta I_B$.
- SATURATION mode: $I_C$ has reached its maximum (set by the external circuit), and additional base current does not significantly increase $I_C$; $V_{CE}$ is small (about $0.2\text{ V}$).

---

Flashcards for this section are as follows:

- active vs saturation check: first compute $\beta I_B$ and $I_{C,\max}$ ::@:: Compute $I_B$ from the base drive, then compute $\beta I_B$ (active-mode capability) and compute $I_{C,\max}$ from the collector/load network (circuit-limited maximum). <!--SR:!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z-->
- active vs saturation check: which mode applies? ::@:: If $\beta I_B \ge I_{C,\max}$, the transistor saturates: $I_C\approx I_{C,\max}$ and $V_{CE}$ is small. If $\beta I_B < I_{C,\max}$, it stays in active mode: $I_C\approx\beta I_B$. <!--SR:!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z-->
- lecture numeric case (given $R_B=10\text{ k}\Omega$, $R_C=1\text{ k}\Omega$, $V_{CC}=5\text{ V}$, $\beta\approx100$): if $V_{\text{IN}}=0.8\text{ V}$, find $I_B$, $I_C$, and $V_{\text{out}}(=V_C)$. ::@:: $I_B\approx(0.8\text{ V}-0.7\text{ V})/10\text{ k}\Omega=10\,\mu\text{A}$. In active mode $I_C\approx\beta I_B\approx100\times10\,\mu\text{A}=1\text{ mA}$. Then $V_{\text{out}}=V_C\approx V_{CC}-I_C R_C=5\text{ V}-1\text{ mA}\cdot1\text{ k}\Omega=4\text{ V}$. <!--SR:!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z-->
- lecture numeric case (given $R_B=10\text{ k}\Omega$, $R_C=1\text{ k}\Omega$, $V_{CC}=5\text{ V}$, $\beta\approx100$): if $V_{\text{IN}}=1\text{ V}$, find $I_B$, $I_C$, and $V_{\text{out}}(=V_C)$. ::@:: $I_B\approx(1.0\text{ V}-0.7\text{ V})/10\text{ k}\Omega=30\,\mu\text{A}$. In active mode $I_C\approx\beta I_B\approx3\text{ mA}$. Then $V_{\text{out}}=V_C\approx5\text{ V}-3\text{ mA}\cdot1\text{ k}\Omega=2\text{ V}$ (still not saturated). <!--SR:!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z-->
- lecture numeric case (given $R_B=10\text{ k}\Omega$, $R_C=1\text{ k}\Omega$, $V_{CC}=5\text{ V}$, $\beta\approx100$, $V_{CE,\text{sat}}\approx0.2\text{ V}$): if $V_{\text{IN}}=3\text{ V}$, decide active vs saturation and find $I_C$ and $V_{CE}$. ::@:: Drive gives $I_B\approx(3.0\text{ V}-0.7\text{ V})/10\text{ k}\Omega=230\,\mu\text{A}$ so $\beta I_B\approx23\text{ mA}$. But the collector network limits current to $I_{C,\max}\approx(V_{CC}-V_{CE,\text{sat}})/R_C\approx(5.0-0.2)/1\text{ k}\Omega=4.8\text{ mA}$. Since $\beta I_B \gg I_{C,\max}$, the transistor saturates: $I_C\approx I_{C,\max}\approx4.8\text{ mA}$ and $V_{CE}\approx V_{CE,\text{sat}}\approx0.2\text{ V}$. <!--SR:!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z-->
- maximum collector current: how to compute $I_{C,\max}$? ::@:: For a collector resistor $R_C$ to supply $V_{CC}$, when saturated $V_{CE}\approx V_{CE,\text{sat}}$, so $I_{C,\max}\approx(V_{CC}-V_{CE,\text{sat}})/R_C$. <!--SR:!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z-->
- saturation vs amplification: which formula applies? ::@:: In active mode, $I_C\approx\beta I_B$ and $V_{CE}$ is not forced small. In saturation, $I_C\approx I_{C,\max}$ and $V_{CE}\approx0.2\text{ V}$, so $I_C<\beta I_B$. <!--SR:!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z-->
- why drive into saturation for switching? ::@:: Saturation makes the transistor act like a closed switch: $V_{CE}\approx0.2\text{ V}$, so most of $V_{CC}$ appears across the load. <!--SR:!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z!fsrs,2027-01-03T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-10-29T00:00:00.000Z-->

## transistor as inverter

The same NPN resistor-loaded circuit behaves as a __logic inverter__. Input LOW (below ~$0.7\text{ V}$): transistor off, $V_C$ near $V_{CC}$, output HIGH. Input HIGH (saturating): $V_C$ drops to ~$0.2\text{ V}$ above $V_E$, output LOW.

The saturation threshold $V_{\text{sat}}$ is found by equating $\beta I_B$ to $I_{C,\max}$. With $I_B = (V_{\text{sat}} - 0.7\text{ V})/R_B$ and $I_{C,\max} = (V_{CC} - 0.2\text{ V})/R_C$, solving gives $V_{\text{sat}} = 0.7\text{ V} + R_B(V_{CC} - 0.2\text{ V})/(\beta R_C)$. For the lecture example ($R_B = 10\text{ k}\Omega$, $R_C = 1\text{ k}\Omega$, $V_{CC} = 5\text{ V}$, $\beta = 100$), $V_{\text{sat}} = 1.18\text{ V}$.

---

Flashcards for this section are as follows:

- inverter: how are logical HIGH and LOW defined? ::@:: By comparing $V_C$ and $V_E$: large $V_C - V_E$ is logical HIGH; small difference (about $0.2\text{ V}$) is logical LOW. <!--SR:!2026-10-30,167,310!fsrs,2027-05-11T10:14:48.351Z,331,330.69254451,1,2,7,0,0,2026-06-14T10:14:48.351Z-->
- NPN circuit as inverter: what is the logic behaviour? ::@:: Input LOW (transistor off): $V_C$ high, $V_E$ at ground, so output is logical HIGH. Input HIGH (transistor saturated): $V_C$ only slightly above $V_E$, so output is logical LOW. <!--SR:!fsrs,2027-05-15T10:14:49.135Z,335,335.28290091,1,2,7,0,0,2026-06-14T10:14:49.135Z!2027-01-29,244,330-->
- saturation voltage $V_{\text{sat}}$: how is it found? ::@:: Set $\beta I_B = I_{C,\max}$. Use $I_B = (V_{\text{sat}} - 0.7\text{ V})/R_B$ and $I_{C,\max} = (V_{CC} - 0.2\text{ V})/R_C$; solve for $V_{\text{sat}}$. <!--SR:!fsrs,2027-04-18T02:05:43.220Z,314,314.10478149,1,2,7,0,0,2026-06-08T02:05:43.220Z!2026-11-03,170,310-->
- lecture $V_{\text{sat}}$ example: what is $V_{\text{sat}}$? ::@:: $V_{\text{sat}} = 1.18\text{ V}$; for input above that the transistor is saturated and output is low. <!--SR:!2026-11-04,171,310!2027-02-15,257,330-->
- logical LOW in inverter: why is small $V_C - V_E$ treated as logic LOW? ::@:: The logic level is defined by $V_C$ relative to $V_E$; when that difference is small, it is logical LOW. <!--SR:!2027-02-11,255,330!2026-11-05,172,310-->

## transistor as a switch

A __low-side switch__ sits between the load and ground: current flows supply → load → transistor → ground. For an NPN low-side switch, emitter ties to ground, collector connects to the load, and a base resistor $R_B$ limits base current from $V_{\text{IN}}$. Below ~$0.7\text{ V}$ the transistor is off; above, it saturates and pulls the collector near ground ($V_{CE}\approx0.2\text{ V}$). <p> ![NPN low-side switch schematic](attachments/npn_low_side_switch.svg)

Design procedure: (1) determine $I_C$ from load and supply, (2) pick conservative $\beta_{\text{forced}}$ and compute $I_B=I_C/\beta_{\text{forced}}$, (3) choose $R_B$ for ~$0.7\text{ V}$ at the high input with sufficient $I_B$, (4) verify $V_{CE}\approx0.2\text{ V}$ and power rating. $I_B\approx(V_{\text{IN}}-0.7\text{ V})/R_B$ when on; check whether $I_C\le\beta I_B$ (active) or the transistor saturates.

---

Flashcards for this section are as follows:

- low-side switch (vs high-side): what is it? ::@:: A low-side switch is between the load and ground: current flows from supply → load → switch → ground. The transistor is on the "low" (ground) side of the load. High-side would put the switch between supply and load. <!--SR:!fsrs,2027-05-12T10:13:46.653Z,332,332.24027195,1,2,7,0,0,2026-06-14T10:13:46.653Z!2027-02-03,247,330-->
- low-side NPN switch connections (E, C, base, load) ::@:: For an NPN low-side switch: emitter to ground, collector to the load, and the other side of the load to the positive supply; the base is driven from the control signal through a resistor. <p> ![NPN low-side switch schematic](attachments/npn_low_side_switch.svg) <!--SR:!2026-12-01,185,310!2026-11-03,170,310-->
- low-side NPN switch behaviour ($V_{BE}\approx0.7\text{ V}$, $V_{CE}\approx0.2\text{ V}$) <p> ![NPN low-side switch schematic](attachments/npn_low_side_switch.svg) ::@:: Low input gives $V_{BE}<0.7\text{ V}$ so the transistor is OFF and $I_C\approx0$. High enough input provides base current; with sufficient drive the transistor saturates and pulls the collector near ground with $V_{CE}\approx0.2\text{ V}$. <!--SR:!fsrs,2027-05-15T10:14:54.576Z,335,335.28290091,1,2,7,0,0,2026-06-14T10:14:54.576Z!2026-12-07,187,310-->
- need for base resistor: why use $R_B$? ::@:: A base resistor limits base current so the transistor is not overdriven; $I_B\approx(V_{\text{IN}}-0.7\text{ V})/R_B$ when on. <!--SR:!2027-01-26,241,330!2027-01-17,232,330-->
- saturation $V_{CE}$: what is $V_{CE}$ in saturation? ::@:: In saturation a BJT has $V_{CE}$ around $0.2\text{ V}$, even though collector current is at its maximum set by the load and supply. <!--SR:!fsrs,2027-05-15T10:12:27.126Z,335,335.28290091,1,2,7,0,0,2026-06-14T10:12:27.126Z!fsrs,2027-05-11T10:14:41.825Z,331,330.69254451,1,2,7,0,0,2026-06-14T10:14:41.825Z-->
- sizing base resistor for switch: steps? ::@:: Estimate $I_C$ from the load, choose a conservative $\beta_{\text{forced}}$ and compute $I_B=I_C/\beta_{\text{forced}}$, then use $R_B\approx(V_{\text{IN}}-0.7\text{ V})/I_B$ when the input is high. <!--SR:!fsrs,2027-05-11T10:12:25.823Z,331,330.69254451,1,2,7,0,0,2026-06-14T10:12:25.823Z!2026-11-23,177,310-->
