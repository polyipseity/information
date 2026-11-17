---
aliases:
  - ADC
  - ELEC 2400 analog-to-digital converter
  - ELEC2400 analog-to-digital converter
  - HKUST ELEC 2400 analog-to-digital converter
  - HKUST ELEC2400 analog-to-digital converter
  - analog-to-digital converter
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/analog-to-digital_converter
  - language/in/English
---

# analog-to-digital converter

An analog-to-digital converter (ADC) stamps a varying voltage with a binary word, and a [digital-to-analog converter](digital-to-analog%20converter.md) turns the word back into a voltage. Two limits come before any circuit is chosen: the word can only land on a fixed set of levels, and it is refreshed once per sample interval.

---

Flashcards for this section are as follows:

- an analog-to-digital converter stamps a varying voltage with a binary word; which two limits apply before any circuit is chosen? ::@:: The word can only land on a fixed set of levels, and it is refreshed once per sample interval.

## digitizing an analog signal

Signals such as voice and temperature vary continuously with time. These are analog signals. Computers work on numbers, so the analog signal is digitized for processing (analog-to-digital conversion, A/D conversion), then converted back to an analog signal at the output (digital-to-analog conversion, D/A conversion). The circuit doing A/D conversion is the analog-to-digital converter (ADC); the one doing D/A conversion is the digital-to-analog converter (DAC). A digital signal processor (DSP) takes the ADC's output and feeds the DAC's input.

Digitizing an analog signal $V_{in}(t)$ to 3-bit resolution quantizes it against eight levels stepped by $\frac{V_{ref}}{8}$: $0\text{ V}$, $\frac{V_{ref}}{8}$, $\frac{V_{ref}}{4}$, $\frac{3V_{ref}}{8}$, $\frac{V_{ref}}{2}$, $\frac{5V_{ref}}{8}$, $\frac{3V_{ref}}{4}$, $\frac{7V_{ref}}{8}$ and $V_{ref}$, each level carrying its 3-bit word from $000$ up to $111$. Sampling stamps the waveform with one word per sample interval. The highest-frequency component the digital signal can carry is $\frac{f_s}{2}$; $f_s$ is the sampling frequency.

---

Flashcards for this section are in the following format:

- voice and temperature vary continuously with time in a digital signal processing chain; what does an analog-to-digital converter (ADC) do on the way in, and a digital-to-analog converter (DAC) on the way out? ::@:: The analog-to-digital converter digitizes the signal for processing, and the digital-to-analog converter turns the processed signal back into an analog output.
- an analog signal $V_{in}(t)$ is digitized to 3-bit resolution against a reference $V_{ref}$; which quantization levels step through the range, and which words carry them? ::@:: Eight levels stepped by $\frac{V_{ref}}{8}$: $0\text{ V}$, $\frac{V_{ref}}{8}$, $\frac{V_{ref}}{4}$, $\frac{3V_{ref}}{8}$, $\frac{V_{ref}}{2}$, $\frac{5V_{ref}}{8}$, $\frac{3V_{ref}}{4}$, $\frac{7V_{ref}}{8}$ and $V_{ref}$, carrying the 3-bit words $000$ through $111$.
- an analog signal is sampled at sampling frequency $f_s$ before digitization; what is the highest-frequency component the digital signal can represent? ::@:: $\frac{f_s}{2}$, the Nyquist frequency: no component above half the sampling frequency survives the conversion.

## flash analog-to-digital converter

A 2-bit flash analog-to-digital converter (ADC) pairs comparators (CMP) with logic gates; a comparator is an operational amplifier run in open loop. A resistor chain of four equal resistances $R$ drops $V_{ref}$ into the references $\frac{V_{ref}}{4}$, $\frac{V_{ref}}{2}$ and $\frac{3V_{ref}}{4}$, and three comparators stamp $V_{in}$ against them. A binary encoder turns the three comparator outputs $A$, $B$ and $C$ into the word $b_1b_0$: $V_i < \frac{1}{4}V_{ref}$ gives $00$, $\frac{1}{4}V_{ref} < V_i < \frac{1}{2}V_{ref}$ gives $01$, $\frac{1}{2}V_{ref} < V_i < \frac{3}{4}V_{ref}$ gives $10$, and $\frac{3}{4}V_{ref} < V_i$ gives $11$.

![flash analog-to-digital converter circuit: a chain of four equal resistors divides V ref into the three references, three comparators take V in on the plus input and one reference on the minus input, and their outputs A, B and C enter a binary encoder that prints b 1 and b 0](attachments/flash_adc.svg)

The chain sets the spacing. Four equal $R$ split $V_{ref}$ into steps of $\frac{V_{ref}}{4}$. Consecutive taps, and the comparators wired to them, sit one step apart.

All three comparators decide at one instant, with no clocking sequence between them. A conversion therefore takes one clock cycle, not several. Their outputs pile up in a thermometer pattern: as $V_i$ climbs, one more comparator turns on at each step, so the trio reads $000$, then $001$, then $011$, then $111$. Nothing else appears, because a higher tap can only turn on after every tap below it has.

The encoder turns that pattern into the word, since it only has to find how far the run of ones has climbed. The truth table leaves the rest as "don't care". That drops the logic down to an inverter on $B$, an OR gate pairing it with $A$, and an AND gate with $C$: $b_1 = B$ and $b_0 = (A+\bar{B})C$.

The price is the comparator count. A 2-bit flash ADC needs $3 = 2^2 - 1$ comparators, an $n$-bit flash ADC needs $2^n - 1$. Every extra bit roughly doubles that count.

---

Flashcards for this section are in the following format:

- how is a 2-bit flash analog-to-digital converter built, from which comparator references to which binary encoder outputs? ::@:: A resistor chain of four equal resistances $R$ drops $V_{ref}$ into $\frac{V_{ref}}{4}$, $\frac{V_{ref}}{2}$ and $\frac{3V_{ref}}{4}$. Three comparators (operational amplifiers in open loop) stamp $V_{in}$ against them, and a binary encoder turns the comparator outputs $A$, $B$ and $C$ into the word $b_1b_0$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- a 2-bit flash analog-to-digital converter compares an input $V_i$ against $\frac{1}{4}V_{ref}$, $\frac{1}{2}V_{ref}$ and $\frac{3}{4}V_{ref}$; which 2-bit word $b_1b_0$ does each range of $V_i$ produce? ::@:: $V_i < \frac{1}{4}V_{ref}$ gives $00$, $\frac{1}{4}V_{ref} < V_i < \frac{1}{2}V_{ref}$ gives $01$, $\frac{1}{2}V_{ref} < V_i < \frac{3}{4}V_{ref}$ gives $10$, and $\frac{3}{4}V_{ref} < V_i$ gives $11$.
- a flash analog-to-digital converter runs at one conversion per clock cycle; how many comparators does a 2-bit flash ADC need, and how many does an $n$-bit flash ADC need? ::@:: A 2-bit flash analog-to-digital converter needs $3 = 2^2 - 1$ comparators, and an $n$-bit flash ADC needs $2^n - 1$ comparators.
- the binary encoder of a 2-bit flash analog-to-digital converter takes comparator outputs $A$, $B$ and $C$; what do the "don't care" conditions reduce its outputs $b_1$ and $b_0$ to? ::@:: $b_1 = B$ and $b_0 = (A+\bar{B})C$: an inverter on $B$, an OR gate pairing it with $A$, and an AND gate with $C$.
- the flash analog-to-digital converter drawing with $V_{ref}$ at the top of a four-$R$ chain: where do the three references come from, and what does each comparator compare? <p> ![flash analog-to-digital converter circuit: a chain of four equal resistors divides V ref into the three references, three comparators take V in on the plus input and one reference on the minus input, and their outputs A, B and C enter a binary encoder that prints b 1 and b 0](attachments/flash_adc.svg) ::@:: From a chain of four equal resistors across $V_{ref}$, which leaves three taps one step of $\frac{V_{ref}}{4}$ apart; each comparator takes $V_{in}$ on its plus input and one tap on its minus input.
- a 2-bit flash analog-to-digital converter with $V_{ref}$ across four $R$: what sits on the reference side, what on the input side, and where do the comparator outputs $A$, $B$ and $C$ go? ::@:: Four equal $R$ across $V_{ref}$ give the three taps. Three comparators each take $V_{in}$ on plus and a tap on minus, and $A$, $B$ and $C$ go into a binary encoder that outputs $b_1$ and $b_0$. <p> ![flash analog-to-digital converter circuit: a chain of four equal resistors divides V ref into the three references, three comparators take V in on the plus input and one reference on the minus input, and their outputs A, B and C enter a binary encoder that prints b 1 and b 0](attachments/flash_adc.svg)
- the thermometer pattern: a flash analog-to-digital converter raises $V_i$ across its taps; which patterns do the comparator outputs $A$, $B$ and $C$ take, and why is no other pattern possible? ::@:: $000$, $001$, $011$, then $111$: each step turns on one more comparator, and a higher tap cannot turn on before every tap below it has.
- an $n$-bit flash analog-to-digital converter: why does it need only one clock cycle per conversion, and how many comparators does the speed cost? ::@:: Every comparator decides at one instant, with no clocking sequence between them; the price is $2^n - 1$ comparators for $n$ bits, roughly double for each extra bit.
