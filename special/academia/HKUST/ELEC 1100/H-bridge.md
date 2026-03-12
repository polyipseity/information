---
aliases:
  - H bridge
  - H-bridge
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1100/H-bridge
  - language/in/English
---

# H-bridge

An H-bridge is a circuit that allows reversible control of a [brushed DC motor](brushed%20DC%20electric%20motor.md) (or other DC load): by closing the right pair of switches, current through the motor flows in one direction (forward) or the opposite (backward), so the motor can be driven in either sense from a single supply. In robot applications this is used to make a wheel or tread turn forward or reverse. The name comes from the typical schematic layout: the supply and ground form two vertical rails, and the load sits horizontally between them with four switches at the corners, resembling the letter “H”.

---

Flashcards for this section are as follows:

- H-bridge purpose: What does an H-bridge let you do with a DC motor? ::@:: Control the direction of current through the motor so it can spin forward or backward; reversible drive from a single supply without switching wires.
- H-bridge single supply: Why is “one supply” useful? ::@:: You do not need two power sources or to physically swap motor leads; one supply and the right switch pattern give either direction.
- H-bridge name origin ::@:: The circuit layout looks like an “H”: supply and ground are the two vertical rails, the load is the horizontal bar, and four switches sit at the corners.
- H-bridge robot use: How is the H-bridge used in a robot? ::@:: To drive a wheel or tread forward or reverse (e.g. left and right wheels) so the robot can move in either direction.

## four-switch topology and direction control

### switches and current path

The basic H-bridge uses four switches (S1–S4) arranged around the motor: one pair connects the motor to the positive supply and ground on one side, the other pair on the opposite side. The motor has two terminals (e.g. $+$ and $-$). To drive in one direction, close S1 and S3 (the two “diagonal” switches on one diagonal); current flows from supply through S1, through the motor (e.g. $+$ to $-$), through S3 to ground. To reverse direction, open S1 and S3 and instead close S2 and S4; current then flows the other way through the motor. <p> ![H-bridge schematic (four switches S1–S4 and motor)](attachments/h_bridge.svg)

---

Flashcards for this section are as follows:

- schematic: H-bridge (four switches S1–S4, motor) <p> ![H-bridge schematic](attachments/h_bridge.svg) ::@:: H-bridge: four switches S1–S4 at the corners, motor between the two mid nodes; Vcc at top, GND at bottom; close one diagonal to drive the motor one way.
- H-bridge four switches (S1–S4): which pair for one direction? ::@:: Close one diagonal pair (e.g. S1 and S3) for one direction; close the other diagonal (S2 and S4) for the opposite direction.
- H-bridge current path (one direction): With S1 and S3 closed, how does current flow? (supply, motor, ground) ::@:: From supply through S1, through the motor (e.g. $+$ to $-$ terminal), through S3 to ground. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### hazards

Only one diagonal pair must be closed at a time. Closing both diagonals would short the supply to ground. Never close all four or the two switches on the same side (e.g. S1 and S2) at once, as that shorts the supply.

---

Flashcards for this section are as follows:

- H-bridge short hazard: Why must only one diagonal be closed at a time? ::@:: Closing both diagonals or two switches on the same rail would short the supply to ground and damage the circuit.
- H-bridge same-side hazard: What happens if you close two switches on the same side (e.g. S1 and S2)? ::@:: That shorts the supply to ground; only one diagonal pair must be closed at a time.

## building an H-bridge with transistors

### saturation, transistor types, and layout

In practice the four switches are implemented with transistors. Brushed DC motors often need high current, so transistors are operated in saturation (fully on) to allow maximum collector current. In the course H-bridge layout the **top** side of the H (between supply and motor) uses **both PNP** transistors, and the **bottom** side (between motor and ground) uses **both NPN** transistors. Equivalently, the left leg of the H has one PNP and one NPN, and the right leg has one PNP and one NPN.

An **NPN** bipolar junction transistor (BJT) has three terminals: collector (C), base (B), and emitter (E). In the symbol the emitter has an arrow pointing *out* of the device. The base current controls a larger current from collector to emitter; when used as a switch, a HIGH base (relative to emitter) turns the transistor on (saturation), so current flows from collector to emitter. A **PNP** BJT also has C, B, and E; its emitter arrow points *into* the device. For a PNP, a LOW base (relative to emitter) turns it on, and current flows from emitter to collector. So the top row switches the positive rail to the motor (PNPs turn on when base is LOW), and the bottom row switches the motor to ground (NPNs turn on when base is HIGH). For one direction we turn on one diagonal: one PNP on the top and one NPN on the bottom (e.g. top-left PNP and bottom-right NPN), giving a path supply $\rightarrow$ PNP $\rightarrow$ motor $\rightarrow$ NPN $\rightarrow$ ground. For the other direction we turn on the other diagonal (the other top PNP and the other bottom NPN). See [transistor](transistor.md) for full definitions and symbols.

---

Flashcards for this section are as follows:

- H-bridge transistors: why use saturation? ::@:: Brushed motors need high current; operating the transistors in saturation (fully on) gives maximum collector current for driving the motor.
- H-bridge layout (course): Where are the PNP and NPN transistors in the course H-bridge? ::@:: Top side of the H (supply to motor): both PNP. Bottom side (motor to ground): both NPN. Left leg has one PNP and one NPN; right leg has one PNP and one NPN.
- H-bridge why NPN and PNP: Why use two NPN and two PNP (not four of one type)? ::@:: One current path goes from supply (through a PNP on top) to the motor to ground (through an NPN on the bottom). So we need both types: top row PNPs switch the positive rail, bottom row NPNs switch to ground.
- NPN in H-bridge: What is an NPN and where is it in the course H-bridge? (C, B, E; bottom) ::@:: NPN: three terminals C, B, E; emitter arrow out. Base HIGH (vs emitter) turns it on; current flows C $\rightarrow$ E. In the course H-bridge both transistors on the **bottom** side (motor to ground) are NPN. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- PNP in H-bridge: What is a PNP and where is it in the course H-bridge? (C, B, E; top) ::@:: PNP: three terminals C, B, E; emitter arrow in. Base LOW (vs emitter) turns it on; current flows E $\rightarrow$ C. In the course H-bridge both transistors on the **top** side (supply to motor) are PNP. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- H-bridge one diagonal path: For one motor direction, what is the current path? (top PNP, bottom NPN) ::@:: Supply $\rightarrow$ PNP (top) $\rightarrow$ motor $\rightarrow$ NPN (bottom) $\rightarrow$ ground. One diagonal (one top PNP and one bottom NPN) is on; the other diagonal is off. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### base voltage pattern

The control voltages at the bases (Va, Vb, Vc, Vd) are set as follows: for one direction, Va and Vd receive $5\text{ V}$ (or HIGH) and Vb, Vc receive $0\text{ V}$ (GND); for the opposite direction, Vb and Vc receive $5\text{ V}$ and Va, Vd receive $0\text{ V}$. So two complementary pairs of signals are needed to steer current through the motor.

---

Flashcards for this section are as follows:

- H-bridge base voltages (Va, Vb, Vc, Vd) for one direction vs opposite: what pattern? ($5\text{ V}$ / $0\text{ V}$) ::@:: One direction: Va and Vd HIGH ($5\text{ V}$), Vb and Vc LOW ($0\text{ V}$). Opposite direction: Vb and Vc HIGH, Va and Vd LOW.
- H-bridge complementary pairs: What do the four bases need? ::@:: Two complementary pairs of signals: one pair at $5\text{ V}$ / $0\text{ V}$ and the other at $0\text{ V}$ / $5\text{ V}$, so one diagonal is on and the other off. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## single direction (DIR) signal and the need for an inverter

### direction (DIR) signal and inverter solution

To control the H-bridge with a single **direction (DIR)** signal (e.g. $5\text{ V}$ for one way and $0\text{ V}$ for the other), one diagonal’s bases get the DIR value directly but the other diagonal needs the inverted value. A single DIR line provides only one logic level, so the four bases (which need two complementary pairs) cannot be driven from DIR alone. An **inverter** is used: when DIR is $5\text{ V}$, one pair of bases sees $5\text{ V}$ and $0\text{ V}$ (from the inverter output); when DIR is $0\text{ V}$, the inverter outputs $5\text{ V}$ so the other pair is driven. One DIR line plus one inverter thus produce both $5\text{ V}$ and $0\text{ V}$ for the four transistors.

---

Flashcards for this section are as follows:

- why inverter in H-bridge: Why is an inverter needed when controlling the H-bridge with one DIR signal? (one DIR = $5\text{ V}$ or $0\text{ V}$) ::@:: One DIR value drives one diagonal pair; the other diagonal needs the opposite logic level. A single DIR line gives only one level, so an inverter is used to produce the complementary level from that same DIR.
- DIR signal meaning: What do the two values of DIR ($5\text{ V}$ and $0\text{ V}$) represent? ::@:: DIR = $5\text{ V}$ selects one motor direction; DIR = $0\text{ V}$ selects the opposite direction (current through the motor flows the other way).
- inverter role with DIR: What does the inverter output feed? ::@:: When DIR goes to one diagonal's bases, the inverter output (the opposite logic level) goes to the other diagonal's bases, so both $5\text{ V}$ and $0\text{ V}$ are available from one DIR line. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## 74HC14 hex inverter

### function and logic

The course uses the **74HC14** integrated circuit, a hex inverter: it contains six independent inverters in one package. Each inverter has one input and one output; the logic is INPUT LOW $\Rightarrow$ OUTPUT HIGH, INPUT HIGH $\Rightarrow$ OUTPUT LOW. Any of the six inverters can be used; choose pins that suit the breadboard layout (e.g. one inverter for the left motor DIR, another for the right motor DIR).

---

Flashcards for this section are as follows:

- 74HC14 what it is: What is the 74HC14? (hex, inverters) ::@:: A hex inverter IC: six independent inverters in one package; each converts LOW $\Rightarrow$ HIGH and HIGH $\Rightarrow$ LOW at its output. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- 74HC14 logic: What does each inverter do to its input? (LOW, HIGH) ::@:: INPUT LOW $\Rightarrow$ OUTPUT HIGH; INPUT HIGH $\Rightarrow$ OUTPUT LOW. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- 74HC14 how many inverters needed for two motors: For left and right motor DIR, how many of the six inverters do you use? ::@:: Two (one per motor); the remaining four are unused; choose any two that suit the breadboard layout.

### power and pinout

The IC does not generate power: **VCC** (pin 14 for the standard 14-pin package) connects to the positive supply voltage (in our course robot, $5\text{ V}$ is used); **GND** (pin 7) connects to ground. Pin 1 is at the top left when the “U” shape or notch at the top is identified; pins run down the left side (1–7) and up the right side (8–14). <p> ![74HC14 pinout (14-pin DIP)](attachments/74hc14_pinout.svg)

---

Flashcards for this section are as follows:

- schematic: 74HC14 pinout <p> ![74HC14 pinout](attachments/74hc14_pinout.svg) ::@:: 74HC14 hex inverter: 14-pin DIP; pin $7$ = GND, pin $14$ = VCC; pins 1A/1Y, 2A/2Y, etc. for the six inverters. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- 74HC14 power: Does the 74HC14 generate its own power? What must be connected? (VCC, GND, $5\text{ V}$ in course) ::@:: No; VCC connects to the positive supply (in our course robot, $5\text{ V}$); GND connects to ground. The IC does not generate power.
- 74HC14 VCC and GND: Can VCC be any voltage? What about GND? ($5\text{ V}$ in course) ::@:: VCC can be connected to any valid supply voltage for the IC (in our course we use $5\text{ V}$); GND must be connected to ground.
- 74HC14 pin numbering: How are pins identified on the 74HC14? ::@:: Identify the top (e.g. “U” notch); pin 1 is top left; pins run down the left (1–7) and up the right (8–14).

## dual H-bridge motor driver (L293)

### function and pins

The **L293** is an integrated circuit that contains two complete H-bridges, so one IC can drive two DC motors (e.g. left and right wheels of a robot car). Each H-bridge has enable (EN), input (IN_1, IN_2), and output (OUT_1, OUT_2) pins. For each motor, the two IN pins set the direction (and the inverter, if used, provides the complementary signal from a single DIR line); the EN pin enables that half of the chip. <p> ![L293 dual H-bridge IC pinout (16-pin DIP)](attachments/l293_block.svg)

---

Flashcards for this section are as follows:

- schematic: L293 pinout <p> ![L293 pinout](attachments/l293_block.svg) ::@:: L293 dual H-bridge: 16-pin DIP; pin 8 = VS (motor supply), pin 16 = VCC (logic); EN_12, IN_1, OUT_1, OUT_2, IN_2 for bridge 1; EN_34, IN_3, OUT_3, OUT_4, IN_4 for bridge 2.
- L293 function: What is the L293 used for? ::@:: Dual H-bridge IC: it contains two complete H-bridges so one chip can drive two DC motors (e.g. left and right robot wheels).
- L293 enable and inputs: What do EN and IN_1, IN_2 do per motor? ::@:: EN enables that H-bridge (that half of the chip); IN_1 and IN_2 set the direction (with an inverter, one DIR line can drive both so they are complementary).
- L293 outputs: What do OUT_1 and OUT_2 connect to? ::@:: The two outputs of each H-bridge connect to the two terminals of that motor.

### supplies and bypass

The L293 needs two supply voltages: **VS** (pin 8) for the motor supply (e.g. $12\text{ V}$) and **VCC** (pin 16) for the logic inputs (e.g. $5\text{ V}$). Ground pins and bypass capacitors (e.g. $0.1\,\mu\text{F}$) near the IC are required for stable operation.

---

Flashcards for this section are as follows:

- L293 two supplies: What are VS and VCC on the L293? (pin 8, pin 16; $12\text{ V}$, $5\text{ V}$) ::@:: VS (e.g. pin 8) is the motor supply (e.g. $12\text{ V}$); VCC (e.g. pin 16) is the logic supply (e.g. $5\text{ V}$). Both must be connected for the IC to work.
- L293 bypass capacitors: Why use capacitors (e.g. $0.1\,\mu\text{F}$) near the L293? ::@:: For stable operation; they help filter supply noise and provide local charge when the motors draw current.

## connecting L293, 74HC14, and LM7805

### power sources ($12\text{ V}$ and $5\text{ V}$)

In the course project the $12\text{ V}$ motor supply and regulated $5\text{ V}$ logic supply come from the **LM7805** regulator circuit (see [voltage regulator](voltage%20regulator.md)): a $12\text{ V}$ battery (or similar) feeds the LM7805 input, and the regulator output provides $5\text{ V}$ for the 74HC14 and L293 logic (VCC). The L293 motor supply (VS) is connected to the unregulated $12\text{ V}$ (before or from the same source as the regulator input). So one battery/input provides both $12\text{ V}$ for motors and $5\text{ V}$ (via LM7805) for logic.

---

Flashcards for this section are as follows:

- where 12V and 5V come from in the project: In the robot car circuit, where do $12\text{ V}$ and $5\text{ V}$ come from? ::@:: The LM7805 circuit: unregulated $12\text{ V}$ (e.g. battery) feeds the regulator and the L293 motor supply (VS); the LM7805 output provides regulated $5\text{ V}$ for the 74HC14 and L293 VCC.
- how many 74HC14 inverters for two motors: How many inverters are needed for left and right motor DIR, and how many 74HC14 ICs? ::@:: Two inverters (one per motor); one 74HC14 package has six inverters, so one physical IC is enough.

### wiring DIR and inverters

Two **74HC14** inverters are needed for the two motors (left and right DIR). Connect each motor’s DIR line to one inverter input; the inverter output goes to the appropriate L293 IN pins so that the two inputs to each H-bridge are complementary.

---

Flashcards for this section are as follows:

- connecting DIR to L293: How is each motor’s DIR signal wired to the L293? ::@:: The DIR line goes to one inverter input; the inverter output goes to the appropriate L293 IN pins so that the two inputs to that H-bridge are complementary (one HIGH, one LOW).

## breadboard layout

### rail labels and 74HC14 power

When building the circuit on a breadboard, keep the $12\text{ V}$ and $5\text{ V}$ rails clearly identified so that nothing is accidentally connected to the wrong supply. Always connect VCC (to the positive supply; $5\text{ V}$ in the course robot) and GND (to ground) on the 74HC14; without them the inverter outputs are undefined. In the ELEC 1100 lab sequence you normally build the LM7805, L293 and 74HC14 circuits once on the provided breadboard and keep them for later labs rather than dismantling and rebuilding each time.

---

Flashcards for this section are as follows:

- breadboard $12\text{ V}$ vs $5\text{ V}$: Why label the two rails on the breadboard? ::@:: To avoid connecting logic pins to the motor supply or vice versa; wrong connections can damage the ICs.
- 74HC14 power on breadboard: What must be connected to the 74HC14 for it to work? (VCC, GND, $5\text{ V}$ in course) ::@:: VCC to the positive supply (in our course, $5\text{ V}$) and GND to ground; without them the outputs are undefined.
- keeping H-bridge circuits across labs: Why does the lab ask you to keep the LM7805, L293 and 74HC14 circuits on the same breadboard for future labs? ::@:: Reusing the existing LM7805, L293 and 74HC14 layout avoids repeated rewiring, reduces mistakes, and ensures a stable, known‑good motor‑driver circuit for later labs.

### pin counts and placement

The L293 has 8 pins on each side (16 pins total); the 74HC14 has 7 pins on each side (14 pins total). Place the LM7805, L293, and 74HC14 so that wiring is short and the left/right motor connections are easy to trace.

---

Flashcards for this section are as follows:

- breadboard pin counts: How many pins does the L293 have on each side? The 74HC14? ::@:: L293: 8 pins on each side (16 total). 74HC14: 7 pins on each side (14 total).
