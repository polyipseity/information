---
aliases:
  - H bridge
  - H-bridge
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1100/H-bridge
  - language/in/English
---

# H-bridge

An H-bridge is a circuit that lets you reverse the direction of current through a [brushed DC motor](brushed%20DC%20electric%20motor.md) (or other DC load) from a single supply. Closing one diagonal pair of switches drives current one way; the other pair reverses it. In robot applications this makes a wheel turn forward or reverse. The name comes from the schematic layout: supply and ground form two vertical rails, the load sits horizontally between them, and four switches sit at the corners — resembling the letter "H".

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

In practice the four switches are implemented with transistors. Brushed DC motors often need high current, so transistors are operated in saturation (fully on) to allow maximum collector current. In the course H-bridge layout the __top__ side of the H (between supply and motor) uses __both PNP__ transistors, and the __bottom__ side (between motor and ground) uses __both NPN__ transistors. Equivalently, the left leg of the H has one PNP and one NPN, and the right leg has one PNP and one NPN.

An __NPN__ bipolar junction transistor (BJT) has three terminals: collector (C), base (B), and emitter (E). In the symbol the emitter has an arrow pointing _out_ of the device. The base current controls a larger current from collector to emitter; when used as a switch, a HIGH base (relative to emitter) turns the transistor on (saturation), so current flows from collector to emitter. A __PNP__ BJT also has C, B, and E; its emitter arrow points _into_ the device. For a PNP, a LOW base (relative to emitter) turns it on, and current flows from emitter to collector. So the top row switches the positive rail to the motor (PNPs turn on when base is LOW), and the bottom row switches the motor to ground (NPNs turn on when base is HIGH). For one direction we turn on one diagonal: one PNP on the top and one NPN on the bottom (e.g. top-left PNP and bottom-right NPN), giving a path supply $\rightarrow$ PNP $\rightarrow$ motor $\rightarrow$ NPN $\rightarrow$ ground. For the other direction we turn on the other diagonal (the other top PNP and the other bottom NPN). See [transistor](transistor.md) for full definitions and symbols.

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

To control the H-bridge with a single __direction (DIR)__ signal (e.g. $5\text{ V}$ for one way and $0\text{ V}$ for the other), one diagonal's bases get the DIR value directly but the other diagonal needs the inverted value. A single DIR line provides only one logic level, so the four bases (which need two complementary pairs) cannot be driven from DIR alone. An __inverter__ is used: when DIR is $5\text{ V}$, one pair of bases sees $5\text{ V}$ and $0\text{ V}$ (from the inverter output); when DIR is $0\text{ V}$, the inverter outputs $5\text{ V}$ so the other pair is driven. One DIR line plus one inverter thus produce both $5\text{ V}$ and $0\text{ V}$ for the four transistors.

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

The __L293__ is an integrated circuit that contains two complete H-bridges, so one IC can drive two DC motors (e.g. left and right wheels of a robot car). Each H-bridge has enable (EN), input (IN_1, IN_2), and output (OUT_1, OUT_2) pins. For each motor, the two IN pins set the direction (and the inverter, if used, provides the complementary signal from a single DIR line). The EN pin plays a different role: if EN is LOW, that H-bridge is disabled; if EN is HIGH, that H-bridge responds to its two IN pins. This also makes EN the natural place to apply PWM for speed control: keep the direction logic fixed on IN_1 and IN_2, and pulse EN on and off rapidly to vary the average motor voltage. <p> ![L293 dual H-bridge IC pinout (16-pin DIP)](attachments/l293_block.svg)

---

Flashcards for this section are as follows:

- schematic: L293 pinout <p> ![L293 pinout](attachments/l293_block.svg) ::@:: L293 dual H-bridge: 16-pin DIP; pin 8 = VS (motor supply), pin 16 = VCC (logic); EN_12, IN_1, OUT_1, OUT_2, IN_2 for bridge 1; EN_34, IN_3, OUT_3, OUT_4, IN_4 for bridge 2.
- L293 function ::@:: Dual H-bridge IC: two complete H-bridges in one chip, driving two DC motors (e.g. left and right wheels).
- L293 enable and inputs ::@:: IN_1 and IN_2 set direction; EN enables or disables that bridge half. EN can be tied HIGH (always on) or driven by PWM for speed control while IN pins keep the direction.
- L293 outputs ::@:: OUT_1 and OUT_2 connect to the two motor terminals.
- why PWM on EN ::@:: EN turns the bridge on/off without changing direction logic, so PWM at EN controls average voltage and speed.

### supplies and bypass

The L293 needs two supply voltages: __VS__ (pin 8) for the motor supply (e.g. $12\text{ V}$) and __VCC__ (pin 16) for the logic inputs (e.g. $5\text{ V}$). The distinction matters: the $12\text{ V}$ motor supply is only for the motor-driving output stage and the motor pins, whereas the logic/control side of the chip uses $5\text{ V}$ on VCC. So every logic-level connection — EN, IN_1, IN_2, IN_3, IN_4, and the 74HC14 interface — belongs to the $5\text{ V}$ logic domain, not to the $12\text{ V}$ motor rail. Ground pins and bypass capacitors (e.g. $0.1\,\mu\text{F}$) near the IC are required for stable operation, and the logic and motor supplies must share a common reference ground.

---

Flashcards for this section are as follows:

- L293 two supplies ::@:: VS (pin 8) is the motor supply (e.g. 12 V) for the output stage only. VCC (pin 16) is the logic supply (e.g. 5 V) for the input/control side.
- bypass capacitors near L293 ::@:: Filter supply noise and provide local charge when motors draw current.
- why common ground between 12 V and 5 V ::@:: Logic levels are referenced to ground; a common ground gives one shared voltage reference so the driver interprets inputs correctly.

## connecting L293, 74HC14, and LM7805

### power sources ($12\text{ V}$ and $5\text{ V}$)

In the course project the $12\text{ V}$ motor supply and regulated $5\text{ V}$ logic supply come from the __LM7805__ regulator circuit (see [voltage regulator](voltage%20regulator.md)): a $12\text{ V}$ battery (or similar) feeds the LM7805 input, and the regulator output provides $5\text{ V}$ for the 74HC14 and L293 logic (VCC). The L293 motor supply (VS) is connected to the unregulated $12\text{ V}$ (before or from the same source as the regulator input). So one battery/input provides both $12\text{ V}$ for motors and $5\text{ V}$ (via LM7805) for logic. The key separation is: the $12\text{ V}$ rail should go only to the motor-supply side (VS and the motor current path), while the logic/control side of the L293 and the 74HC14 should stay on the regulated $5\text{ V}$ rail.

---

Flashcards for this section are as follows:

- 12 V and 5 V sources ::@:: The unregulated battery rail feeds the motor supply (VS) and the LM7805 input. The LM7805 generates the regulated 5 V rail for logic (74HC14, L293 VCC).
- inverters needed ::@:: Two (one per motor); one 74HC14 package has six, so one IC suffices.

### wiring DIR and inverters

Two __74HC14__ inverters are needed for the two motors (left and right DIR). Connect each motor's DIR line to one inverter input. Then use the original DIR signal and the inverter output as the two complementary logic inputs for that motor's L293 half: for example, DIR may go directly to one L293 input and the inverted DIR to the other. In that way each motor gets one HIGH and one LOW direction input, and flipping DIR swaps those two logic levels. If PWM speed control is needed later, apply PWM to the corresponding EN pin rather than to the DIR line.

---

Flashcards for this section are as follows:

- DIR wiring to L293 ::@:: DIR feeds one 74HC14 inverter input; the original DIR and the inverted output go to the two L293 direction inputs, giving $(\text{IN}_1,\text{IN}_2)=(\text{DIR},\overline{\text{DIR}})$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## breadboard layout

### rail labels and 74HC14 power

When building the circuit on a breadboard, keep the $12\text{ V}$ and $5\text{ V}$ rails clearly identified so that nothing is accidentally connected to the wrong supply. Always connect VCC (to the positive supply; $5\text{ V}$ in the course robot) and GND (to the common ground of that $5\text{ V}$ logic supply) on the 74HC14; GND is _not_ another $5\text{ V}$ pin. Without VCC and a proper ground reference the inverter outputs are undefined. In the ELEC 1100 lab sequence you normally build the LM7805, L293 and 74HC14 circuits once on the provided breadboard and keep them for later labs rather than dismantling and rebuilding each time.

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
