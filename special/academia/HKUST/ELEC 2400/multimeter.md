---
aliases:
  - DMM
  - ELEC 2400 multimeter
  - ELEC2400 multimeter
  - HKUST ELEC 2400 multimeter
  - HKUST ELEC2400 multimeter
  - digital multimeter
  - multimeter
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/multimeter
  - language/in/English
---

# multimeter

A multimeter reads voltage, current, and resistance as single numbers. The digital multimeter (DMM) shows each reading on a numeric display, and every reading carries a bandwidth limit of its own.

---

Flashcards for this section are as follows:

- three quantities: which electrical quantities does a multimeter read as single numbers? ::@:: Voltage, current, and resistance.
- display form: how does a digital multimeter (DMM) show each reading? ::@:: On a numeric display, one number per reading.

## quantities from a voltage

Every quantity a digital multimeter (DMM) reports passes through a voltage first. A voltage is scaled and digitised directly; a resistance is read by injecting a known constant current into the device and measuring the voltage across it; a current is read as the voltage across a small fixed internal resistance.

---

Flashcards for this section are as follows:

- resistance reading: a digital multimeter (DMM) measures a resistance; how does it produce the number? ::@:: It injects a known constant current into the device, measures the voltage across the device, and converts that voltage into the displayed resistance.
- current reading: a digital multimeter (DMM) measures a current; what quantity does it actually measure? ::@:: The voltage across a small fixed internal resistance, scaled into the displayed current.
- one quantity underneath: which quantity do all of a digital multimeter (DMM)'s readings pass through? ::@:: A voltage, scaled and digitised before the number appears.

## alternating-current readings

The alternating-current voltage mode (ACV) reports a root mean square (RMS) value. Meters differ in how they arrive at one: a true-RMS meter works from the signal's power, while a meter that scales the peak by a sine-fitted factor agrees with the true value only for sine waves.

The waveform therefore decides whether a reading can be trusted. A square wave, a triangle wave, and a sine wave of the same amplitude carry different root mean square (RMS) values, $V_m$, $V_m/\sqrt{3}$, and $V_m/\sqrt{2}$, so one meter reads three different numbers from three equally scaled waveforms.

---

Flashcards for this section are as follows:

- ACV reading: what quantity does the alternating-current voltage mode (ACV) of a digital multimeter report? ::@:: A root mean square (RMS) value of the applied waveform.
- true-RMS meter: how does a true-RMS meter reach its reading? ::@:: It works from the signal's power, so the root mean square (RMS) value comes out right whatever the waveform's shape.
- sine-scaled meter: which waveform may a meter that scales the peak by a sine-fitted factor measure correctly? ::@:: A sine wave alone; any other shape makes the reading disagree with the true root mean square (RMS) value.
- same amplitude, three readings: a square wave, a triangle wave, and a sine wave share the amplitude $V_m$; which root mean square (RMS) value does each carry? ::@:: The square wave carries $V_m$, the triangle wave $V_m/\sqrt{3}$, and the sine wave $V_m/\sqrt{2}$.

## bandwidth

Readings hold their value only while the signal frequency stays well inside the meter's bandwidth. Around 10 kHz is a typical digital multimeter (DMM) figure: the reading stays flat below it, sags as the frequency climbs, and at the bandwidth itself stands at $0.707$ of its low-frequency value, the $1/\sqrt{2}$ factor an instrument specification quotes. Past that point the reading is attenuated rather than merely noisy, so a signal of a few hundred hertz and above is measured by an [oscilloscope](oscilloscope.md) instead.

---

Flashcards for this section are as follows:

- bandwidth criterion: where on a plot of reading against frequency does a digital multimeter's (DMM's) bandwidth sit? ::@:: At the frequency where the reading has fallen to $0.707$ of its low-frequency value. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- typical bandwidth: what order of bandwidth does a typical digital multimeter (DMM) have? ::@:: Around 10 kHz.
- beyond the bandwidth: a signal's frequency climbs past a digital multimeter's (DMM's) bandwidth; what happens to each reading? ::@:: It is attenuated rather than merely noisy, so the number no longer reports the signal's true value.
- which instrument: a signal of a few hundred hertz and above must be measured reliably; which instrument takes the measurement over from the digital multimeter (DMM)? ::@:: The oscilloscope, whose bandwidth reaches far higher.
