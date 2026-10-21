---
aliases:
  - ELEC 2400 loading effect
  - ELEC2400 loading effect
  - HKUST ELEC 2400 loading effect
  - HKUST ELEC2400 loading effect
  - loading
  - loading effect
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/loading_effect
  - language/in/English
---

# loading effect

A load takes current from whatever drives it, and that current crosses the source resistance, so the voltage reaching the load falls short of what the source delivers on its own. A meter loads the circuit the same way, so its reading is the loaded voltage rather than the voltage the circuit had before the meter was connected.

---

Flashcards for this section are as follows:

- what does a load do to the voltage a source delivers, and why does a voltmeter make the same error? ::@:: The load draws current through the source resistance, which drops part of the source voltage; a voltmeter does exactly that to the circuit it measures, and its own input resistance sets how much.

## measuring a sensor with a voltmeter

A sensor outputs a sensed voltage of $5\text{ mV}$ behind an internal resistance of $25\text{ k}\Omega$. A voltmeter of input resistance $100\text{ k}\Omega$ connected straight across it reads $V_{\text{measured}} = \frac{100\text{ k}\Omega}{25\text{ k}\Omega + 100\text{ k}\Omega} \times 5\text{ mV} = 4\text{ mV}$. That is $20\%$ below the sensed voltage, and the meter's own resistance causes the drop.

A [unity-gain buffer](buffer%20amplifier.md) between the sensor and the meter restores the reading. Its input resistance is infinite, so $I = 0\text{ A}$ and no current crosses the sensor resistance. The buffered input terminals then hold $V_- = V_+ = 5\text{ mV}$, and the meter reads the sensed value.

---

Flashcards for this section are in the following format:

- direct reading: a sensor outputs $V_{\text{sensed}} = 5\text{ mV}$ behind a sensor resistance of $25\text{ k}\Omega$, and a voltmeter of input resistance $100\text{ k}\Omega$ connects directly across it; what voltage does the voltmeter read? ::@:: $V_{\text{measured}} = \frac{100\text{ k}\Omega}{25\text{ k}\Omega + 100\text{ k}\Omega} \times 5\text{ mV} = 4\text{ mV}$, off and lowered by $20\%$.
- buffered reading: a sensor outputs $5\text{ mV}$ behind $25\text{ k}\Omega$ and feeds a voltmeter of input resistance $100\text{ k}\Omega$ through a unity-gain buffer built from an operational amplifier; what does the voltmeter read, and why? ::@:: It reads $5\text{ mV}$: the buffer's input resistance is infinite, so $I = 0\text{ A}$, no current flows through the sensor resistance, the input terminals hold $V_- = V_+ = 5\text{ mV}$, and the measured value equals the sensed value.
