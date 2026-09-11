---
aliases:
  - H bridge
  - H-bridge
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1100/H-bridge
  - language/in/English
---

# H-bridge

An H-bridge is a circuit that lets you reverse the direction of current through a [brushed DC motor](brushed%20DC%20electric%20motor.md) (or other DC load) from a single supply. Closing one diagonal pair of switches drives current one way; the other pair reverses it. In robot applications this makes a wheel turn forward or reverse. The name comes from the schematic layout: supply and ground form two vertical rails, the load sits horizontally between them, and four switches sit at the corners, resembling the letter "H".

---

Flashcards for this section are as follows:

- H-bridge purpose ::@:: Reverses the direction of current through a DC motor from a single supply, so the motor spins forward or backward without swapping wires.
- why one supply matters ::@:: No need for two power sources or physically swapping motor leads; one supply and the right switch pattern give either direction.
- H-bridge name origin ::@:: The schematic looks like an "H": supply and ground are the vertical rails, the load is the horizontal bar, and four switches sit at the corners.
- H-bridge robot use ::@:: Drives a wheel or tread forward or reverse so the robot can move in either direction.

## four-switch topology and direction control

### switches and current path

The basic H-bridge uses four switches (S1–S4) arranged around the motor: one pair connects the motor to the positive supply and ground on one side, the other pair on the opposite side. The motor has two terminals (e.g. $+$ and $-$). To drive in one direction, close S1 and S3 (the two "diagonal" switches on one diagonal); current flows from supply through S1, through the motor (e.g. $+$ to $-$), through S3 to ground. To reverse direction, open S1 and S3 and instead close S2 and S4; current then flows the other way through the motor. <p> ![H-bridge schematic (four switches S1–S4 and motor)](attachments/h_bridge.svg)

---

Flashcards for this section are as follows:

- schematic: H-bridge (four switches S1–S4, motor) <p> ![H-bridge schematic](attachments/h_bridge.svg) ::@:: H-bridge: four switches S1–S4 at the corners, motor between the two mid nodes; Vcc at top, GND at bottom; close one diagonal to drive the motor one way.
- switch pairs for direction ::@:: Close one diagonal pair (e.g. S1 and S3) for one direction; close the other diagonal (S2 and S4) for the opposite.
- current path with S1 and S3 closed ::@:: Supply → S1 → motor ($+$ to $−$) → S3 → ground. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### hazards

Only one diagonal pair must be closed at a time. Closing both diagonals would short the supply to ground. Never close all four or the two switches on the same side (e.g. S1 and S2) at once, as that shorts the supply.

---

Flashcards for this section are as follows:

- short hazard ::@:: Closing both diagonals or two same-side switches shorts the supply to ground and damages the circuit.

## building an H-bridge with transistors

### saturation, transistor types, and layout

In practice the four switches are transistors. Brushed DC motors need high current, so transistors operate in saturation (fully on). The __top__ side (supply to motor) uses __both PNP__ transistors; the __bottom__ side (motor to ground) uses __both NPN__ transistors. Each leg has one PNP and one NPN.

An __NPN__ BJT has terminals collector (C), base (B), emitter (E); the emitter arrow points _out_. HIGH base turns it on; current flows C → E. A __PNP__ BJT has the same terminals; emitter arrow points _in_. LOW base turns it on; current flows E → C. The top row (PNPs) switches the positive rail to the motor; the bottom row (NPNs) switches to ground. One diagonal on: supply → PNP → motor → NPN → ground. See [transistor](transistor.md) for full definitions.

---

Flashcards for this section are as follows:

- why saturation for H-bridge transistors ::@:: Brushed motors need high current; saturation (fully on) gives maximum collector current.
- course H-bridge layout ::@:: Top side (supply to motor): both PNP. Bottom side (motor to ground): both NPN. Each leg has one PNP and one NPN.
- why both NPN and PNP ::@:: The top row PNPs switch the positive rail; the bottom row NPNs switch to ground. One current path goes supply → PNP → motor → NPN → ground.
- NPN in H-bridge ::@:: Three terminals C, B, E; emitter arrow out. Base HIGH turns it on; current flows C → E. Both bottom-side transistors are NPN. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- PNP in H-bridge ::@:: Three terminals C, B, E; emitter arrow in. Base LOW turns it on; current flows E → C. Both top-side transistors are PNP. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- one-diagonal current path ::@:: Supply → PNP (top) → motor → NPN (bottom) → ground. One diagonal is on; the other is off. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### base voltage pattern

The control voltages at the bases (Va, Vb, Vc, Vd) are set as follows: for one direction, Va and Vd receive $5\text{ V}$ (or HIGH) and Vb, Vc receive $0\text{ V}$ (GND); for the opposite direction, Vb and Vc receive $5\text{ V}$ and Va, Vd receive $0\text{ V}$. So two complementary pairs of signals are needed to steer current through the motor.

---

Flashcards for this section are as follows:

- base voltage pattern ::@:: One direction: Va, Vd HIGH; Vb, Vc LOW. Opposite: Vb, Vc HIGH; Va, Vd LOW.
- complementary pairs ::@:: Two complementary signal pairs steer one diagonal on and the other off. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## single direction (DIR) signal and the need for an inverter

### direction (DIR) signal and inverter solution

A single __DIR__ signal ($5\text{ V}$ or $0\text{ V}$) drives one diagonal directly; the other diagonal needs the inverted value. An __inverter__ produces the complementary level from the same DIR line, giving both logic levels to the four transistors.

---

Flashcards for this section are as follows:

- why an inverter is needed ::@:: One DIR signal drives one diagonal; the other diagonal needs the opposite level. An inverter produces that complementary level from the same DIR.
- DIR signal meaning ::@:: DIR = $5\text{ V}$ selects one direction; DIR = $0\text{ V}$ selects the opposite.
- inverter output ::@:: Feeds the opposite diagonal's bases, so both logic levels are available from one DIR line. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## 74HC14 hex inverter

### function and logic

The course uses the __74HC14__ integrated circuit, a hex inverter: it contains six independent inverters in one package. Each inverter has one input and one output; the logic is INPUT LOW $\Rightarrow$ OUTPUT HIGH, INPUT HIGH $\Rightarrow$ OUTPUT LOW. Any of the six inverters can be used; choose pins that suit the breadboard layout (e.g. one inverter for the left motor DIR, another for the right motor DIR).

---

Flashcards for this section are as follows:

- 74HC14 identity ::@:: Hex inverter IC: six independent inverters in one package; each inverts its input. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- 74HC14 logic ::@:: INPUT LOW → OUTPUT HIGH; INPUT HIGH → OUTPUT LOW. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- inverters needed for two motors ::@:: Two (one per motor); four remain unused.

### power and pinout

The IC does not generate power: __VCC__ (pin 14 for the standard 14-pin package) connects to the positive supply voltage (in our course robot, $5\text{ V}$ is used); __GND__ (pin 7) connects to ground. Pin 1 is at the top left when the "U" shape or notch at the top is identified; pins run down the left side (1–7) and up the right side (8–14). <p> ![74HC14 pinout (14-pin DIP)](attachments/74hc14_pinout.svg)

---

Flashcards for this section are as follows:

- 74HC14 pinout <p> ![74HC14 pinout](attachments/74hc14_pinout.svg) ::@:: 14-pin DIP; pin 7 = GND, pin 14 = VCC; pins 1A/1Y, 2A/2Y, etc. for the six inverters. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- 74HC14 power ::@:: VCC connects to the positive supply (5 V in the course); GND to ground. The IC does not generate its own power.
- 74HC14 pin numbering ::@:: Identify the top notch; pin 1 is top left; pins run down the left (1–7) and up the right (8–14).

## dual H-bridge motor driver (L293)

### function and pins

The __L293__ contains two complete H-bridges, driving two DC motors (e.g. left and right wheels). Each bridge has enable (EN), input (IN_1, IN_2), and output (OUT_1, OUT_2) pins. IN pins set direction; EN enables/disables the bridge. PWM on EN controls speed: keep direction fixed on IN pins, pulse EN to vary average motor voltage. <p> ![L293 dual H-bridge IC pinout (16-pin DIP)](attachments/l293_block.svg)

---

Flashcards for this section are as follows:

- schematic: L293 pinout <p> ![L293 pinout](attachments/l293_block.svg) ::@:: L293 dual H-bridge: 16-pin DIP; pin 8 = VS (motor supply), pin 16 = VCC (logic); EN_12, IN_1, OUT_1, OUT_2, IN_2 for bridge 1; EN_34, IN_3, OUT_3, OUT_4, IN_4 for bridge 2.
- L293 function ::@:: Dual H-bridge IC: two complete H-bridges in one chip, driving two DC motors (e.g. left and right wheels).
- L293 enable and inputs ::@:: IN_1 and IN_2 set direction; EN enables or disables that bridge half. EN can be tied HIGH (always on) or driven by PWM for speed control while IN pins keep the direction.
- L293 outputs ::@:: OUT_1 and OUT_2 connect to the two motor terminals.
- why PWM on EN ::@:: EN turns the bridge on/off without changing direction logic, so PWM at EN controls average voltage and speed.

### supplies and bypass

The L293 needs two supplies: __VS__ (pin 8) for the motor (e.g. $12\text{ V}$) and __VCC__ (pin 16) for logic (e.g. $5\text{ V}$). The $12\text{ V}$ rail goes only to the motor output stage; all logic-level connections (EN, IN pins, 74HC14 interface) use the $5\text{ V}$ rail. Bypass capacitors (e.g. $0.1\,\mu\text{F}$) near the IC filter noise; logic and motor supplies must share a common ground.

---

Flashcards for this section are as follows:

- L293 two supplies ::@:: VS (pin 8) is the motor supply (e.g. 12 V) for the output stage only. VCC (pin 16) is the logic supply (e.g. 5 V) for the input/control side.
- bypass capacitors near L293 ::@:: Filter supply noise and provide local charge when motors draw current.
- why common ground between 12 V and 5 V ::@:: Logic levels are referenced to ground; a common ground gives one shared voltage reference so the driver interprets inputs correctly.

## connecting L293, 74HC14, and LM7805

### power sources ($12\text{ V}$ and $5\text{ V}$)

The $12\text{ V}$ motor supply and regulated $5\text{ V}$ logic supply come from the __LM7805__ (see [voltage regulator](voltage%20regulator.md)). A $12\text{ V}$ battery feeds the LM7805 input; the output provides $5\text{ V}$ for 74HC14 and L293 VCC. The L293 VS pin connects to the unregulated $12\text{ V}$. The $12\text{ V}$ rail goes only to motor-side pins (VS, motor path); logic-side pins stay on the regulated $5\text{ V}$ rail.

---

Flashcards for this section are as follows:

- 12 V and 5 V sources ::@:: The unregulated battery rail feeds the motor supply (VS) and the LM7805 input. The LM7805 generates the regulated 5 V rail for logic (74HC14, L293 VCC).
- inverters needed ::@:: Two (one per motor); one 74HC14 package has six, so one IC suffices.

### wiring DIR and inverters

Two __74HC14__ inverters handle the two motors. Each motor's DIR feeds one inverter input; the original DIR and inverted output go to the two L293 direction inputs, giving $(\text{IN}_1,\text{IN}_2)=(\text{DIR},\overline{\text{DIR}})$. Flipping DIR swaps the two logic levels. Apply PWM to EN for speed control, not to DIR.

---

Flashcards for this section are as follows:

- DIR wiring to L293 ::@:: DIR feeds one 74HC14 inverter input; the original DIR and the inverted output go to the two L293 direction inputs, giving $(\text{IN}_1,\text{IN}_2)=(\text{DIR},\overline{\text{DIR}})$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## breadboard layout

### rail labels and 74HC14 power

Label the $12\text{ V}$ and $5\text{ V}$ rails clearly to avoid wrong connections. On the 74HC14, connect VCC to $5\text{ V}$ and GND to ground; without both, inverter outputs are undefined. Build the LM7805, L293, and 74HC14 circuits once and keep them for later labs.

---

Flashcards for this section are as follows:

- 12 V vs 5 V rails ::@:: Label both rails to avoid connecting logic pins to the motor supply or vice versa; wrong connections can damage ICs.
- 74HC14 power connections ::@:: VCC to the regulated 5 V rail, GND to the common ground. Without both, inverter outputs are undefined.
- why keep circuits across labs ::@:: Reusing the existing layout avoids rewiring, reduces mistakes, and ensures a known-good motor-driver circuit for later labs.

### pin counts and placement

The L293 has 8 pins on each side (16 pins total); the 74HC14 has 7 pins on each side (14 pins total). Place the LM7805, L293, and 74HC14 so that wiring is short and the left/right motor connections are easy to trace.

---

Flashcards for this section are as follows:

- pin counts ::@:: L293: 8 pins per side (16 total). 74HC14: 7 pins per side (14 total).
