---
aliases:
  - ELEC 2400 decibel
  - ELEC2400 decibel
  - HKUST ELEC 2400 decibel
  - HKUST ELEC2400 decibel
  - decibel
  - decibel gain
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/decibel
  - language/in/English
---

# decibel

A decibel (dB) is one tenth of a bel. Quoting gain in decibels puts it on a logarithmic scale, where the stages of a chain add up instead of multiplying.

---

Flashcards for this section are as follows:

- why quote a gain in decibels instead of as a plain ratio? ::@:: A decibel is a logarithmic measure of a ratio, so cascaded gains add rather than multiply, and a very large or very small ratio becomes a short number.

## decibel gain

Voltage gain is quoted in decibels: $\text{dB} = 20\log_{10}(\text{gain})$. The [temperature-sensor chain](operational%20amplifier.md#loading%20chain%20of%20a%20practical%20voltage%20amplifier) had to turn $100\text{ mV}$ into $1\text{ V}$, which takes $11.96\text{ V/V}$ once both dividers are counted, and that gain reads $21.6\text{ dB}$. An operational amplifier with gain above $10000\text{ V/V}$ reaches $80\text{ dB}$, and a practical device at $10^5\text{ V/V}$ reaches $100\text{ dB}$.

---

Flashcards for this section are in the following format:

- decibel gain: how is the voltage gain of an amplifier converted into decibels (dB), and what is $11.96\text{ V/V}$ in decibels? ::@:: $\text{dB} = 20\log_{10}(\text{gain})$, so $20\log_{10}(11.96) = 21.6\text{ dB}$.
- gain figures in decibels: what do the voltage gains $10000\text{ V/V}$ and $10^5\text{ V/V}$ of an operational amplifier equal in decibels (dB)? ::@:: $20\log_{10}(10000) = 80\text{ dB}$ and $20\log_{10}(10^5) = 100\text{ dB}$.
