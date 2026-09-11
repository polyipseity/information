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

A robot needs sensors because control without measurement is blind. Broad families include chemical sensors, accelerometers, gyroscopes, image sensors, microphones, and biosensors, but what matters is that sensors convert a physical quantity into an electrical signal a controller can read. In the robot-car project the key physical cue is light reflected from the floor.

---

Flashcards for this section are as follows:

- sensor role ::@:: Converts a physical quantity into an electrical signal the controller can read.
- why sensors matter ::@:: Without them the controller has no environmental measurement.
- sensor families ::@:: Chemical sensors, accelerometers, gyroscopes, image sensors, microphones, biosensors — course focuses on light sensing.
- ELEC 1100 focus ::@:: Light sensing for line tracking.

## lumens and lux

Two related brightness measures matter in light sensing. Lumens measure luminous flux: the total light emitted in all directions by a source. Lux measures illuminance: the total light falling on a surface. Both measure brightness, but lumens describe emitted light while lux describe light received on a surface.

---

Flashcards for this section are as follows:

- lumens vs lux ::@:: Lumens: total light emitted. Lux: total light falling on a surface.
- lumen ::@:: Luminous flux; total light emitted.
- lux ::@:: Illuminance; total light falling on a surface.

<!-- check: ignore-next-line[header_style]: acronym -->
## LDR, photodiode, phototransistor, and thresholding

Common light-sensing devices include the LDR, photodiode, and phototransistor. An LDR (photoresistor) has high resistance in darkness and lower resistance in brighter light; the examples use a dark resistance around $10\text{ M}\Omega$ and a bright resistance around $100\Omega$ to show how strongly the divider voltage changes with illumination. Photodiodes and phototransistors use semiconductor junctions to respond to light in detection circuits. Thresholding then converts a changing sensor voltage into a clean digital LOW or HIGH.

---

Flashcards for this section are as follows:

- LDR behavior ::@:: High resistance in darkness, lower in bright light.
- LDR resistance scale ::@:: Dark ~10 MΩ, bright ~100Ω; explains why bias voltage changes strongly.
- thresholding purpose ::@:: Converts analog sensor voltage into clean digital LOW or HIGH.
- photodiode/phototransistor ::@:: Semiconductor light-sensing devices converting light into electrical response.

## dark and bright sensing circuits

Two transistor-based templates show how the same NPN stage works as a dark detector or a bright detector. In a __dark-sensing__ circuit, the fixed resistor is on the high side from $+5\text{ V}$ to the base node and the LDR is on the low side from the base node to ground. In darkness the LDR resistance becomes large, so the base node is pulled upward through the fixed resistor, the transistor turns on, and the LED lights. In a __bright-sensing__ circuit, the positions are swapped: the LDR is on the high side and the fixed resistor is on the low side. Bright light then lowers the LDR resistance, pulls the base node upward, turns the transistor on, and lights the LED. The transistor stage is the same; moving the LDR between the low side and the high side decides which condition turns it on.

---

Flashcards for this section are as follows:

- dark-sensing topology ::@:: Fixed resistor on high side, LDR on low side to ground.
- bright-sensing topology ::@:: LDR on high side, fixed resistor on low side to ground.
- dark sensing LED ::@:: LED on in darkness; low-side LDR goes high resistance, letting base rise.
- bright sensing LED ::@:: LED on in bright light; high-side LDR goes low resistance, pulling base up.

## infrared sensing for line tracking

The course then narrows to the reflective IR hardware the robot uses for line following.

<!-- check: ignore-next-line[header_style]: acronym -->
### IR discovery and history

William Herschel discovered infrared radiation accidentally in 1800. He separated visible light with a prism, placed thermometers in the different colors, and observed that the temperature increased from blue toward red; he then found an even warmer reading just beyond the red end of the visible spectrum. Anything giving off heat emits infrared radiation, even though human eyes cannot see it.

---

Flashcards for this section are as follows:

- Herschel and IR ::@:: Accidentally discovered infrared in 1800 while measuring temperatures across the prism spectrum.
- key observation ::@:: Temperature rose toward red and was even warmer beyond the red end.
- IR and heat ::@:: Anything giving off heat emits infrared, invisible to human eyes.

<!-- check: ignore-next-line[header_style]: acronym -->
### IR line sensor module and calibration

The project hardware uses a reflective IR sensor module. An IR emitter sends light toward the floor; the receiver responds to the reflected amount. A variable resistor lets you tune the switching threshold for the sensor height and the brightness contrast between the white line and the dark mat. In this robot setup, the tuned module outputs approximately $0\text{ V}$ on white and approximately $5\text{ V}$ on black.

Because the module includes thresholding and exposes one digital output, treat it as a binary line sensor, not a continuous distance sensor. At the controller interface, the tuned setup behaves like a __dark-sensing__ output: the black mat gives less reflected light but the module reports HIGH, while the white line reports LOW. That behavior is not universal across IR sensors; it comes from this specific module and its threshold/output logic.

---

Flashcards for this section are as follows:

- IR sensor principle ::@:: Emitter shines toward floor; receiver detects reflected light.
- calibration ::@:: Adjust variable resistor for sensor height and white-vs-black reflectance difference.
- output convention ::@:: ~0 V on white, ~5 V on black.
- sensor type ::@:: Reflective IR module with emitter, receiver, and onboard thresholding.
- digital sensor treatment ::@:: Thresholded switch reporting black-or-white, not a continuous ranging device.
- dark-sensing behavior ::@:: Black mat → HIGH, white line → LOW; a dark-detecting binary signal.

## sensor patterns for line following

Two front line sensors decide whether the robot is centered, drifting left, or drifting right. The bumper sensor provides a memory-triggering event for the start line and white wall. The sensor pair feeds the logic that sets `L_DIR`, `R_DIR`, `L_PWM`, and `R_PWM`. When both line sensors see the same color, code alone cannot tell whether the robot is at the start line or a later junction; the bumper sensor and a counter like `countBumper` provide the missing state.

---

Flashcards for this section are as follows:

- two line sensors ::@:: Distinguish centered motion from left/right deviation; one sensor cannot resolve error direction.
- bumper sensor role ::@:: State-changing event for start-line and wall-contact detection.
- `countBumper` need ::@:: Same sensor pattern in different contexts requires stored state.
- sensor-to-motor mapping ::@:: Sensor states → `L_DIR`, `R_DIR`, `L_PWM`, `R_PWM`.
