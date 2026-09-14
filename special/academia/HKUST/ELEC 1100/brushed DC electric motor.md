---
aliases:
  - DC brushed motor
  - DC brushed motors
  - brushed DC electric motor
  - brushed DC electric motors
  - brushed DC motor
  - brushed DC motors
  - brushed motor
  - brushed motors
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1100/brushed_DC_electric_motor
  - language/in/English
---

# brushed DC electric motor

A brushed DC electric motor is an electromechanical device that converts electrical energy into mechanical energy (rotation). It uses a mechanical commutator and carbon brushes to switch the current direction in the rotor windings so that a single DC supply can produce continuous rotation. The reverse conversion (mechanical to electrical) is a generator. For a concise treatment of the general concept see [brushed DC electric motor](../../../../general/brushed%20DC%20electric%20motor.md). This note covers motor definition, classification, magnetic basics, stator–rotor interaction, commutation, direction and speed control, and the link to the H-bridge and PWM.

---

Flashcards for this section are as follows:

- motor definition ::@:: Converts electrical energy into mechanical energy (rotation). <!--SR:!fsrs,2027-04-20T02:02:24.728Z,316,315.61032191,1,2,7,0,0,2026-06-08T02:02:24.728Z!fsrs,2027-05-12T10:11:11.893Z,332,332.24027195,1,2,7,0,0,2026-06-14T10:11:11.893Z-->
- generator ::@:: Converts mechanical energy into electrical energy; same principle, opposite energy flow. <!--SR:!fsrs,2027-05-15T10:11:12.941Z,335,335.28290091,1,2,7,0,0,2026-06-14T10:11:12.941Z!fsrs,2027-05-14T10:03:15.084Z,334,333.77014777,1,2,7,0,0,2026-06-14T10:03:15.084Z-->
- power equivalence ::@:: $P_{\text{elec}}=VI$; $P_{\text{mech}}=\omega\times\tau$ (speed × torque). <!--SR:!2027-01-23,238,330!fsrs,2027-05-15T10:11:15.773Z,335,335.28290091,1,2,7,0,0,2026-06-14T10:11:15.773Z-->
- ELEC 1100 motor type ::@:: Brushed DC motors in labs and the robot project. <!--SR:!2027-02-17,258,330!2027-01-31,246,330-->

## what are motors and classification

### what is a motor and applications

A motor converts electrical power (voltage $\times$ current) into mechanical power (rotating speed $\times$ torque). Applications include fans, pumps, cars, and subway systems.

---

Flashcards for this section are as follows:

- motor energy conversion ::@:: Electrical power (voltage × current) → mechanical power (speed × torque). <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2027-05-14T10:03:19.859Z,334,333.77014777,1,2,7,0,0,2026-06-14T10:03:19.859Z!fsrs,2027-05-12T10:03:19.039Z,332,332.24027195,1,2,7,0,0,2026-06-14T10:03:19.039Z-->
- motor applications ::@:: Vacuum cleaners, fans, pumps, manufacturing, cars, subway systems, and many others. <!--SR:!2027-02-17,259,330!2027-02-08,251,330-->

### classification by power source

Electric motors are classified by power source: __DC motors__ are powered by direct current; __AC motors__ by alternating current. DC motors are further divided into brushed motors (commutator and brushes), brushless motors (electronic commutation), and stepper motors. AC motors include induction and synchronous types. In ELEC 1100 labs and the project we use __brushed DC motors__, which drive with an H-bridge and a single DC supply.

---

Flashcards for this section are as follows:

- power-source classification ::@:: DC motors: direct current. AC motors: alternating current. <!--SR:!2027-01-17,232,330!fsrs,2027-05-15T10:11:19.543Z,335,335.28290091,1,2,7,0,0,2026-06-14T10:11:19.543Z-->
- DC motor types ::@:: Brushed (commutator/brushes), brushless (electronic commutation), stepper. <!--SR:!fsrs,2027-04-20T02:05:04.877Z,316,315.61032191,1,2,7,0,0,2026-06-08T02:05:04.877Z!2027-02-10,252,330-->
- why brushed DC in ELEC 1100 ::@:: Simple to drive with an H-bridge and a single DC supply. <!--SR:!2027-01-28,243,330!fsrs,2027-05-14T10:03:23.515Z,334,333.77014777,1,2,7,0,0,2026-06-14T10:03:23.515Z-->

## origin and history

The first DC motor was demonstrated by Michael Faraday in 1821, one year after Hans Christian Oersted discovered electromagnetism; at that time only DC sources were available. AC motors became practical in the 1890s when AC power distribution was available; Nikola Tesla identified the principle of the rotating magnetic field, enabling industrial AC motor development.

---

Flashcards for this section are as follows:

- first DC motor ::@:: Faraday, 1821, one year after Oersted's discovery of electromagnetism. <!--SR:!fsrs,2027-05-12T10:03:17.711Z,332,332.24027195,1,2,7,0,0,2026-06-14T10:03:17.711Z!fsrs,2027-05-15T10:11:00.813Z,335,335.28290091,1,2,7,0,0,2026-06-14T10:11:00.813Z-->
- AC motors ::@:: Practical from the 1890s with AC power; Tesla identified the rotating magnetic field principle. <!--SR:!2027-02-12,255,330!fsrs,2027-04-11T01:08:45.478Z,309,308.57643926,1,2,7,0,0,2026-06-06T01:08:45.478Z-->

## magnetic basics

Most electric motors rely on magnetic fields.

### poles and forces

A magnet has two poles, north (N) and south (S); like poles repel and opposite poles attract. Magnetic poles always come in pairs. __Magnetic monopoles__ (isolated N or S poles) are predicted by some theories but have no experimental evidence; all known magnets have paired poles. The __Earth's magnetic field__ behaves as if a giant bar magnet lay inside the planet: the magnetic south sits near geographic north, so a compass (N-seeking) points north.

---

Flashcards for this section are as follows:

- magnet poles ::@:: North and south; like poles repel, opposite poles attract. <!--SR:!2027-02-11,254,330!2027-02-04,247,330-->
- magnetic monopoles ::@:: Isolated N or S poles with no partner; predicted by some theories but no experimental evidence. <!--SR:!2027-02-11,253,330!2027-02-09,252,330-->
- Earth's magnetic field ::@:: Like a giant bar magnet inside the planet; the magnetic south is near geographic north, so a compass (N-seeking) points north. <!--SR:!2027-01-26,241,330!2027-01-20,235,330-->

### permanent magnet

A __permanent magnet__ has fixed N and S positions and produces a magnetic field from N to S; it is effectively always "on" and cannot be turned off.

---

Flashcards for this section are as follows:

- permanent magnet ::@:: Fixed N and S poles with a field from N to S; cannot be turned off. <!--SR:!2027-01-30,245,330!fsrs,2027-04-05T11:18:54.909Z,304,304.30256839,1,2,7,0,0,2026-06-05T11:18:54.909Z-->

### electromagnet and right-hand rule

An __electromagnet__ is made by passing current through a wire (often wound as a solenoid). The direction of current determines which end is N and which is S; the poles reverse if the current direction is reversed. The direction of the magnetic field around a current-carrying wire can be found using the __right-hand rule__. ____Straight wire:__ point right thumb in current direction; fingers curl in the field direction. __Solenoid:__ grip coil so fingers follow current along turns; thumb points toward the north pole. Electromagnets switch on/off and reverse polarity by changing the current.

---

Flashcards for this section are as follows:

- electromagnet ::@:: N/S poles set by current direction; can be turned on/off and polarity reversed. <!--SR:!fsrs,2027-05-12T10:10:53.333Z,332,332.24027195,1,2,7,0,0,2026-06-14T10:10:53.333Z!fsrs,2027-04-11T01:08:46.473Z,309,308.57643926,1,2,7,0,0,2026-06-06T01:08:46.473Z-->
- right-hand rule purpose ::@:: Find the magnetic field direction around a current-carrying wire or solenoid. <!--SR:!fsrs,2027-04-11T01:08:44.507Z,309,308.57643926,1,2,7,0,0,2026-06-06T01:08:44.507Z!2027-02-10,253,330-->
- right-hand rule (straight wire) ::@:: Thumb in current direction; fingers curl in the magnetic field direction. <!--SR:!fsrs,2027-04-05T11:18:52.151Z,304,304.30256839,1,2,7,0,0,2026-06-05T11:18:52.151Z!fsrs,2027-04-11T01:08:48.501Z,309,308.57643926,1,2,7,0,0,2026-06-06T01:08:48.501Z-->
- right-hand rule (solenoid) ::@:: Fingers follow current along turns; thumb points toward the north pole. <!--SR:!2027-02-14,255,330!2027-01-22,237,330-->

## stator and rotor interaction

### stator and rotor roles

An electric motor operates through the interaction of the magnetic fields of a __stator__ (fixed part) and a __rotor__ (moving part). In a simple brushed DC motor the stator may be a permanent magnet and the rotor an electromagnet (solenoid).

---

Flashcards for this section are as follows:

- stator and rotor ::@:: Stator = fixed part; rotor = moving part. <!--SR:!2027-02-16,258,330!fsrs,2027-05-12T10:11:01.623Z,332,332.24027195,1,2,7,0,0,2026-06-14T10:11:01.623Z-->

### attraction, repulsion, and continuous rotation

When power is applied, current in the rotor creates a magnetic field; the rotor's N and S poles are attracted to the opposite poles of the stator and repelled by the like poles, so the rotor turns until opposite poles align. Because of inertia the rotor overshoots; if we then __reverse the current__ in the rotor, its N and S poles flip, and the forces again push it in the same rotational direction. Repeating this polarity reversal keeps the rotor spinning in one direction; the mechanical commutator and brushes perform this reversal automatically when the motor is driven by a DC source.

---

Flashcards for this section are as follows:

- why rotor turns ::@:: Rotor and stator fields interact; opposite poles attract, like poles repel, producing torque. <!--SR:!fsrs,2027-04-20T02:05:02.096Z,316,315.61032191,1,2,7,0,0,2026-06-08T02:05:02.096Z!fsrs,2027-04-20T02:05:03.340Z,316,315.61032191,1,2,7,0,0,2026-06-08T02:05:03.340Z-->
- why reverse rotor polarity ::@:: After overshoot (inertia), reversing polarity keeps torque in the same direction. <!--SR:!fsrs,2027-04-05T11:18:56.646Z,304,304.30256839,1,2,7,0,0,2026-06-05T11:18:56.646Z!fsrs,2027-05-15T10:11:14.660Z,335,335.28290091,1,2,7,0,0,2026-06-14T10:11:14.660Z-->
- inertia role ::@:: Rotor overshoots the aligned position; polarity reversal keeps it spinning. <!--SR:!2027-01-21,236,330!fsrs,2027-05-12T10:10:52.388Z,332,332.24027195,1,2,7,0,0,2026-06-14T10:10:52.388Z-->

## commutation and brushed construction

### commutation and the commutator and brushes

The switching of the magnetic field in the rotor (reversing current direction) is called __commutation__. A DC source cannot by itself reverse the current in the rotor. In a __brushed DC motor__ this is done mechanically: a __commutator__ (e.g. a copper sleeve split into segments) rotates with the rotor, and __carbon brushes__ (fixed) slide on the commutator and make contact with different segments. As the rotor turns, the brushes contact different segments so that the current through the rotor windings is effectively reversed at the right moments, keeping rotation in one direction. At the brushes the DC current is one direction; the commutator switches segments so the rotor winding current reverses as it rotates.

---

Flashcards for this section are as follows:

- commutation ::@:: Switching the rotor's magnetic field by reversing current direction at the right moments. <!--SR:!fsrs,2027-05-15T10:11:03.519Z,335,335.28290091,1,2,7,0,0,2026-06-14T10:11:03.519Z!fsrs,2027-05-14T10:11:02.572Z,334,333.77014777,1,2,7,0,0,2026-06-14T10:11:02.572Z-->
- why mechanical commutation ::@:: A DC source provides current in one direction; the commutator and brushes switch which rotor segments see which polarity. <!--SR:!2027-02-05,248,330!fsrs,2027-04-11T01:08:47.299Z,309,308.57643926,1,2,7,0,0,2026-06-06T01:08:47.299Z-->
- commutator and brushes ::@:: Commutator: rotating copper sleeve with segments. Brushes: fixed carbon contacts that slide on the commutator. <!--SR:!2027-01-24,239,330!2027-01-26,241,330-->
- current path ::@:: At the brushes, DC current is one direction; the commutator switches segments so rotor winding current reverses as it rotates. <!--SR:!2026-12-01,185,310!fsrs,2027-05-14T10:11:16.389Z,334,333.77014777,1,2,7,0,0,2026-06-14T10:11:16.389Z-->

## direction control with H-bridge

To change the rotation direction of a brushed DC motor we change the direction of current through the motor: reversing the applied voltage (or swapping which terminal is positive and which is negative) reverses the current and thus the direction of the magnetic field in the rotor. An [H-bridge](H-bridge.md) does this electronically: a single direction (DIR) signal ($5\text{ V}$ or $0\text{ V}$), often with an inverter to obtain the complementary logic levels, drives the four transistors so that one diagonal pair is on for one direction and the other diagonal for the opposite direction. One polarity gives clockwise, the other anti-clockwise.

---

Flashcards for this section are as follows:

- reversing motor direction ::@:: Reverse the current direction (voltage polarity); the rotor field opposes the stator in the opposite sense. <!--SR:!fsrs,2027-05-12T10:11:10.993Z,332,332.24027195,1,2,7,0,0,2026-06-14T10:11:10.993Z!2027-01-30,245,330-->
- H-bridge direction control ::@:: Reverses voltage across the motor by closing one diagonal pair for one direction, the other for the opposite. <!--SR:!fsrs,2027-04-20T02:02:25.812Z,316,315.61032191,1,2,7,0,0,2026-06-08T02:02:25.812Z!2027-02-15,256,330-->
- DIR signal ::@:: Selects which H-bridge diagonal is on, controlling current direction and thus rotation direction. <!--SR:!2027-02-12,255,330!2027-01-16,231,330-->

## speed control and limitations of variable resistor

### factors affecting speed

Besides direction, we need to control __motor speed__. Speed can be influenced by the strength of the magnetic field: more coils in the solenoid or a higher voltage (larger current) generally give higher speed. In a built motor the number of coils is fixed, so speed control is usually done by changing the __voltage__ (and thus current) supplied to the motor.

---

Flashcards for this section are as follows:

- speed factors ::@:: Magnetic field strength (more coils or higher voltage/current → higher speed). <!--SR:!2027-02-18,259,330!2027-02-06,249,330-->
- why voltage for speed control ::@:: Coil count is fixed in a built motor; changing supply voltage is the practical way to vary speed. <!--SR:!fsrs,2027-04-05T11:18:50.640Z,304,304.30256839,1,2,7,0,0,2026-06-05T11:18:50.640Z!fsrs,2027-05-14T10:03:21.380Z,334,333.77014777,1,2,7,0,0,2026-06-14T10:03:21.380Z-->

### variable resistor, drawbacks, and PWM

A __variable resistor__ in series with the motor changes its voltage and speed, but it wastes energy as heat (especially at low speeds), is imprecise, and requires mechanical adjustment. The course uses __pulse-width modulation (PWM)__ instead, covered in the next lecture.

---

Flashcards for this section are as follows:

- variable resistor effect ::@:: Smaller resistor → more voltage across motor → faster. Larger resistor → slower. <!--SR:!fsrs,2027-05-14T10:11:08.994Z,334,333.77014777,1,2,7,0,0,2026-06-14T10:11:08.994Z!2027-01-25,240,330-->
- variable resistor drawbacks ::@:: Inefficient (heat waste at low speeds), imprecise, requires mechanical adjustment. <!--SR:!fsrs,2027-04-05T11:18:49.328Z,304,304.30256839,1,2,7,0,0,2026-06-05T11:18:49.328Z!2027-01-29,244,330-->
- PWM ::@:: Used in the course for efficient, precise, software-controllable speed control. <!--SR:!fsrs,2027-05-15T10:11:17.097Z,335,335.28290091,1,2,7,0,0,2026-06-14T10:11:17.097Z!2026-11-20,174,310-->
