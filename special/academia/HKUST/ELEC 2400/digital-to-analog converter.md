---
aliases:
  - DAC
  - ELEC 2400 digital-to-analog converter
  - ELEC2400 digital-to-analog converter
  - HKUST ELEC 2400 digital-to-analog converter
  - HKUST ELEC2400 digital-to-analog converter
  - digital-to-analog converter
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/digital-to-analog_converter
  - language/in/English
---

# digital-to-analog converter

A digital-to-analog converter (DAC) turns a binary word into a voltage. The [summing amplifier](summing%20amplifier.md) builds one: each bit closes its own switch into a weighted input branch, and the word's value appears as a sum. The reverse direction is the [analog-to-digital converter](analog-to-digital%20converter.md).

---

Flashcards for this section are as follows:

- how does a digital-to-analog converter turn a binary word into a voltage? ::@:: Each bit closes its own switch into a weighted input branch of a summing amplifier, and the word's value appears as a sum.

## 4-bit converter

A 4-bit digital-to-analog converter (DAC) is a summing amplifier with one switched branch per bit: $b_i = 0$ leaves the switch open and $b_i = 1$ closes it. The feedback path holds $R$. The Most Significant Bit (MSB) $b_3$ enters through $2R$, then $b_2$ through $4R$, $b_1$ through $8R$, and the Least Significant Bit (LSB) $b_0$ through $16R$.

![digital-to-analog converter circuit: four switched branches from V ref through 2 R, 4 R, 8 R and 16 R into the summing node of an inverting amplifier with feedback R, whose output passes through R a into a second inverting amplifier with R a in its feedback to the output V o](attachments/dac_converter.svg)

That summing amplifier inverts, so its output carries a minus sign. A second inverting amplifier cancels the sign: $R_a$ on its input and the same $R_a$ in its feedback give a gain of $-1$. Two inverting stages are the usual arrangement. The output then leaves the converter with the sign of the word: $V_o = \left(\frac{b_3}{2} + \frac{b_2}{4} + \frac{b_1}{8} + \frac{b_0}{16}\right)V_{ref}$.

Take $V_{ref} = 2\text{ V}$ and the word $b_3b_2b_1b_0 = 1010$: $V_o = \left(\frac{1}{2} + \frac{1}{8}\right) \times 2\text{ V} = 1.25\text{ V}$. CD players rely on this arrangement.

---

Flashcards for this section are in the following format:

- how does a summing amplifier become a 4-bit digital-to-analog converter, and what does each bit's switch do? ::@:: Each bit switches its own input branch: $b_i = 0$ leaves the switch open and $b_i = 1$ closes it. Every closed branch feeds the summing amplifier through its weighted resistance. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- a 4-bit digital-to-analog converter built from a summing amplifier weighs the Most Significant Bit $b_3$ to the Least Significant Bit $b_0$ by $2R$, $4R$, $8R$ and $16R$ against feedback $R$; what is its output $V_o$? ::@:: $V_o = \left(\frac{b_3}{2} + \frac{b_2}{4} + \frac{b_1}{8} + \frac{b_0}{16}\right)V_{ref}$: each bit's share is $R$ over its branch resistance.
- a 4-bit digital-to-analog converter built from a summing amplifier runs at $V_{ref} = 2\text{ V}$ with bits $b_3b_2b_1b_0 = 1010$; what is its output $V_o$? ::@:: $V_o = \left(\frac{1}{2} + \frac{1}{8}\right) \times 2\text{ V} = 1.25\text{ V}$.
- why two inverting amplifiers: a digital-to-analog converter whose summing amplifier has feedback $R$ would come out inverted; what follows it, and why does that restore the sign? ::@:: A second inverting amplifier follows, $R_a$ on its input and the same $R_a$ in its feedback. Its gain is $R_a/R_a = -1$, so it flips the minus sign and the word's sign leaves the converter.
- the digital-to-analog converter drawing with $2R$, $4R$, $8R$ and $16R$ on the branches: which resistance weights which bit, and what does the stage after the summing amplifier carry? <p> ![digital-to-analog converter circuit: four switched branches from V ref through 2 R, 4 R, 8 R and 16 R into the summing node of an inverting amplifier with feedback R, whose output passes through R a into a second inverting amplifier with R a in its feedback to the output V o](attachments/dac_converter.svg) ::@:: $2R$, $4R$, $8R$ and $16R$ against the feedback $R$, from $b_3$ down to $b_0$; the stage after it carries $R_a$ on the input and $R_a$ in the feedback.
- a 4-bit digital-to-analog converter with branches $2R$, $4R$, $8R$ and $16R$: where do the switches sit, what does each branch hold, and how does $V_o$ leave? ::@:: Four switches hang off $V_{ref}$, each followed by its own $2R$, $4R$, $8R$ or $16R$ into the summing node, with $R$ in the feedback. The summing output runs through $R_a$ into a second inverting amplifier whose feedback is $R_a$, so $V_o$ comes out with the word's sign. <p> ![digital-to-analog converter circuit: four switched branches from V ref through 2 R, 4 R, 8 R and 16 R into the summing node of an inverting amplifier with feedback R, whose output passes through R a into a second inverting amplifier with R a in its feedback to the output V o](attachments/dac_converter.svg)
