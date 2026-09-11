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

A microcontroller is a small computer embedded inside a device to run one control program efficiently. In this robot platform, it replaces a large fixed gate network and acts as the logic, memory, timing, and input/output hub between sensors and actuators.

<!-- check: ignore-next-line[header_style]: acronym -->
## MCU role and integrated architecture

A microcontroller unit (MCU) integrates the central processing unit (CPU), memory, timer resources, and input/output (I/O) ports on one integrated circuit. It reads inputs, evaluates logic, stores state, and drives outputs while using much less space and power than a general-purpose computer. That makes it appropriate for battery-powered embedded systems that repeat the same control task continuously.

---

Flashcards for this section are as follows:

- MCU meaning ::@:: MCU stands for microcontroller unit.
- what is integrated inside an MCU ::@:: An MCU integrates the CPU, memory, timer resources, and I/O ports on one integrated circuit.
- why an MCU suits an embedded robot controller ::@:: It repeatedly runs one control program while using much less space and power than a general-purpose computer.

## programmable control versus fixed logic

A simple truth table can be implemented directly with gates, but a more complicated robot controller quickly becomes difficult to build, test, and debug entirely from fixed-purpose logic ICs. A programmable microcontroller keeps the same control ideas — truth tables, conditions, stored state, and output assignment — while making the behavior easier to modify in code. On this platform the specific MCU board is an Arduino Nano, but the design lesson is general: programmable control scales better than hand-built gate networks when the required behavior becomes more complex.

---

Flashcards for this section are as follows:

- why programmable control replaces a large fixed gate network ::@:: A programmable controller is easier to modify, test, debug, and extend when the required behavior becomes more complex.
- what control ideas remain the same after moving from gates to an MCU ::@:: The system still depends on truth tables, conditions, stored state, and output assignment; the implementation just moves into code.
- which MCU board is used on this robot platform ::@:: The robot platform uses an Arduino Nano as the MCU board.

## logic-power and motor-power split

The microcontroller lives in the logic domain, not in the motor-power domain. The Nano, the 74HC14, and the logic side of the L293 run from the regulated $5\text{ V}$ rail, while the motor-power side uses the higher battery voltage. The design principle is stable: the MCU decides, the driver translates, and the motor stage supplies the large current.

---

Flashcards for this section are as follows:

- which hardware belongs on the $5\text{ V}$ logic rail ::@:: The Arduino Nano, the 74HC14, and the logic side of the L293 belong on the regulated $5\text{ V}$ rail.
- which hardware belongs on the higher motor-power rail ::@:: The motor-driving side of the L293 and the motors belong on the higher motor-power rail.
- logic-power versus motor-power split: what is the design lesson? ::@:: The MCU makes decisions in the low-power logic domain, the driver translates those commands, and the motor stage supplies the large current.
