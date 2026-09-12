---
aliases:
  - ELEC 1100 sensors
  - sensor
  - sensors
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1100/sensor
  - language/in/English
---

# sensor

Sensors are the robot's interface to the physical world. In ELEC 1100 they are introduced first as a general robotics idea and then narrowed to the light- and line-sensing hardware used in the robot car.

## sensor role and categories

A robot needs sensors because control without measurement is blind. Broad families include chemical sensors, accelerometers, gyroscopes, image sensors, microphones, and biosensors, but the durable lesson is functional: sensors convert a physical quantity into an electrical signal that a controller can read. In the robot-car project the key physical cue is light reflected from the floor.

---

Flashcards for this section are as follows:

- sensor role in a robot ::@:: A sensor converts a physical quantity into an electrical signal so the controller can observe the environment. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- why a robot needs sensors ::@:: Without sensors the controller has no measurement of the environment and cannot react intelligently. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- sensor families briefly surveyed in ELEC 1100 ::@:: The note briefly surveys chemical sensors, accelerometers, gyroscopes, image sensors, microphones, and biosensors before focusing on light sensing. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- ELEC 1100 sensor focus ::@:: The course surveys many sensor types but focuses mainly on light sensing for line tracking. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

## lumens and lux

Two related brightness measures are important in light sensing. Lumens measure luminous flux, which is the total amount of light emitted in all directions by a source. Lux measures illuminance, which is the total amount of light falling on a surface. They are both about brightness, but one describes emitted light and the other describes received light on an area.

---

Flashcards for this section are as follows:

- lumens vs lux: what is the core difference? ::@:: Lumens measure the total light emitted in all directions, while lux measures the total light falling on a surface. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- lumen definition ::@:: A lumen is a measure of luminous flux, the total amount of light emitted in all directions. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- lux definition ::@:: A lux is a measure of illuminance, the total amount of light that falls on a surface. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

<!-- check: ignore-next-line[header_style]: acronym -->
## LDR, photodiode, phototransistor, and thresholding

Common light-sensing devices include the LDR, photodiode, and phototransistor. An LDR (photoresistor) has high resistance in darkness and lower resistance in brighter light; the simple sensing examples use a dark resistance around $10\text{ M}\Omega$ and a bright resistance around $100\Omega$ to show how strongly the divider voltage can change with illumination. Photodiodes and phototransistors use semiconductor junction behavior to respond to light and can be used in detection circuits. The next step is thresholding: a changing sensor voltage is compared with a threshold so the output becomes a clean digital LOW or HIGH.

---

Flashcards for this section are as follows:

- LDR behavior ::@:: An LDR has high resistance in darkness and lower resistance in brighter light. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- LDR resistance scale in the simple examples: what dark and bright resistances are used (about $10\text{ M}\Omega$ and $100\Omega$)? ::@:: The simple examples use a very high dark resistance (around $10\text{ M}\Omega$) and a much lower bright resistance (around $100\Omega$) to explain why the bias voltage changes strongly with illumination. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- why ELEC 1100 introduces thresholding after analog light sensing ::@:: Thresholding converts a changing analog sensor voltage into a clean digital LOW or HIGH that logic and Arduino code can use directly. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- photodiode and phototransistor role in the note ::@:: They are semiconductor light-sensing devices used to convert light exposure into an electrical response. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

## dark and bright sensing circuits

Two transistor-based light-sensor templates show how the same NPN stage can be turned into either a dark detector or a bright detector. In a __dark-sensing__ circuit, the fixed resistor is on the high side from $+5\text{ V}$ to the base node and the LDR is on the low side from the base node to ground. In darkness the LDR resistance becomes large, so the base node is pulled upward through the fixed resistor, the transistor turns on, and the LED lights. In a __bright-sensing__ circuit, the positions are swapped: the LDR is on the high side and the fixed resistor is on the low side. Bright light then lowers the LDR resistance, pulls the base node upward, turns the transistor on, and lights the LED. The transistor stage is the same in both cases; moving the LDR between the low side and the high side decides which lighting condition produces enough base voltage to switch the transistor on.

---

Flashcards for this section are as follows:

- dark-sensing topology ::@:: In the dark-sensing circuit the fixed resistor is on the high side and the LDR is on the low side to ground. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- bright-sensing topology ::@:: In the bright-sensing circuit the LDR is on the high side and the fixed resistor is on the low side to ground. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- dark-sensing circuit with an NPN and LDR: when does the LED turn on? ::@:: The LED turns on in darkness because the low-side LDR becomes high resistance and lets the base node rise. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- bright-sensing circuit with an NPN and LDR: when does the LED turn on? ::@:: The LED turns on in bright light because the high-side LDR becomes low resistance and pulls the base node upward. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

## infrared sensing for line tracking

The course next narrows from generic light-sensitive components to the reflective infrared hardware that the robot actually uses for line following.

<!-- check: ignore-next-line[header_style]: acronym -->
### IR discovery and history

Infrared radiation was accidentally discovered in 1800 by the astronomer William Herschel. He separated visible light with a prism, placed thermometers in the different colors, and observed that the temperature increased from blue toward red; he then found an even warmer reading just beyond the red end of the visible spectrum. This is a useful reminder that anything giving off heat also emits infrared radiation even though the human eye cannot see it directly.

---

Flashcards for this section are as follows:

- William Herschel and IR: what did he discover in 1800? ::@:: William Herschel accidentally discovered infrared radiation while measuring temperatures across the prism-separated visible spectrum. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- Herschel prism experiment: what key observation revealed IR? ::@:: The temperature kept rising toward red and became even warmer just beyond the red end of the visible spectrum. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- why IR is associated with heat ::@:: Anything that gives off heat emits infrared radiation, even though human eyes cannot see those waves directly. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

<!-- check: ignore-next-line[header_style]: acronym -->
### IR line sensor module and calibration

The project hardware uses a reflective IR sensor module. An IR emitter sends light toward the floor and the receiver responds to the reflected amount. The module includes a variable resistor so the switching threshold can be tuned for the actual distance to the ground and for the brightness contrast between the white line and the dark mat. In this robot setup, the tuned module outputs approximately $0\text{ V}$ on white and approximately $5\text{ V}$ on black.

Because the module includes thresholding and exposes one main digital output, it should be treated as a binary line sensor rather than as a precise continuous distance sensor. Operationally, the tuned setup behaves like a __dark-sensing__ output at the controller interface: the darker black mat gives less reflected light yet the module reports HIGH, while the brighter white line reports LOW. That behavior is not a law of all IR sensors; it comes from this specific reflective module plus its onboard threshold and output logic.

---

Flashcards for this section are as follows:

- IR line sensor principle ::@:: An IR emitter shines toward the floor and the receiver detects how much light is reflected back. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- IR line sensor calibration: why adjust the variable resistor? ::@:: To tune the switching threshold for the actual sensor height and the white-vs-black reflectance difference. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- ELEC 1100 line sensor output convention: which surface gives about $0\text{ V}$ and which gives about $5\text{ V}$? ::@:: The tuned module outputs about $0\text{ V}$ on white and about $5\text{ V}$ on black. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- what type of IR sensor the robot car uses ::@:: The robot uses a reflective IR sensor module with an emitter, a receiver, and onboard thresholding. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- why the IR module should be treated as a digital sensor ::@:: It is used as a thresholded switch with one main digital output that reports black-or-white states, not as a precise continuous ranging device. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- why the IR sensor behaves like a dark-sensing output in the car ::@:: In the tuned setup the black mat makes the module output HIGH and the white line makes it output LOW, so the controller sees it as a dark-detecting binary signal. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

## sensor patterns for line following

Two front line sensors are enough to decide whether the robot is centered, drifting left, or drifting right, while the bumper sensor adds a simple memory-triggering event for the start line and white wall. The left and right sensor pair therefore feeds the logic that chooses `L_DIR`, `R_DIR`, `L_PWM`, and `R_PWM`. When both line sensors see the same color, code alone may not tell you whether the robot is at the start line or at a later junction; the bumper sensor and a counter such as `countBumper` provide the needed state information.

---

Flashcards for this section are as follows:

- why ELEC 1100 uses two front line sensors instead of one ::@:: Two sensors can distinguish centered motion from left/right deviation, while one sensor cannot resolve the direction of the error as reliably. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- bumper sensor role in the final project ::@:: The bumper sensor provides a state-changing event that helps distinguish the start line or wall contact from later line-sensor patterns. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- why `countBumper` or similar memory is needed ::@:: The same left/right sensor pattern can occur in different contexts, so stored state is needed to tell those situations apart. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- line sensors and motor commands: what do the sensor states ultimately control? ::@:: They are converted into motor direction and speed commands such as `L_DIR`, `R_DIR`, `L_PWM`, and `R_PWM`. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
