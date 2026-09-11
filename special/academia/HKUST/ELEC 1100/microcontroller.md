---
aliases:
  - ELEC 1100 microcontroller
  - MCU
  - microcontroller
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1100/microcontroller
  - language/in/English
---

# microcontroller

A microcontroller is a small computer embedded inside a device that runs one control program. In this robot platform, it replaces a large fixed gate network and acts as the logic, memory, timing, and I/O hub between sensors and actuators.

<!-- check: ignore-next-line[header_style]: acronym -->
## MCU role and integrated architecture

A microcontroller unit (MCU) integrates the central processing unit (CPU), memory, timer resources, and input/output (I/O) ports on one integrated circuit. It reads inputs, evaluates logic, stores state, and drives outputs using less space and power than a general-purpose computer. This suits battery-powered embedded systems that repeat the same control task.

---

Flashcards for this section are as follows:

- MCU meaning ::@:: MCU stands for microcontroller unit.
- what is integrated inside an MCU ::@:: An MCU integrates the CPU, memory, timer resources, and I/O ports on one integrated circuit.
- why an MCU suits an embedded robot controller ::@:: It repeatedly runs one control program while using much less space and power than a general-purpose computer.

## programmable control versus fixed logic

A simple truth table can be built from gates, but a more complex robot controller is hard to build, test, and debug with fixed-purpose logic ICs alone. A programmable microcontroller keeps the same control ideas (truth tables, conditions, stored state, output assignment) while making the behavior easier to modify in code. On this platform the MCU board is an Arduino Nano; programmable control scales better than hand-built gates as behavior gets more complex.

---

Flashcards for this section are as follows:

- why programmable control replaces fixed gate networks ::@:: A programmable controller is easier to modify and extend than hand-built gates as behavior gets complex.
- what control ideas remain the same after moving from gates to an MCU ::@:: The system still depends on truth tables, conditions, stored state, and output assignment; the implementation just moves into code.
- which MCU board is used ::@:: The robot platform uses an Arduino Nano.

## logic-power and motor-power split

The microcontroller lives in the logic domain, not in the motor-power domain. The Nano, the 74HC14, and the logic side of the L293 run from the regulated $5\text{ V}$ rail, while the motor-power side uses the higher battery voltage. The split: the MCU decides, the driver translates, and the motor stage supplies the current.

---

Flashcards for this section are as follows:

- which hardware belongs on the $5\text{ V}$ logic rail ::@:: The Arduino Nano, the 74HC14, and the logic side of the L293 belong on the regulated $5\text{ V}$ rail.
- which hardware belongs on the higher motor-power rail ::@:: The motor-driving side of the L293 and the motors belong on the higher motor-power rail.
- logic-power vs motor-power split: what is the design lesson? ::@:: The MCU operates in the low-power logic domain; the driver and motor stage handle the high-current side.
