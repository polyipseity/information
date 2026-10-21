---
aliases:
  - ELEC 2400 oscilloscope
  - ELEC2400 oscilloscope
  - HKUST ELEC 2400 oscilloscope
  - HKUST ELEC2400 oscilloscope
  - oscilloscope
  - scope
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/oscilloscope
  - language/in/English
---

# oscilloscope

An oscilloscope displays voltage against time. Voltage is the only quantity it reads directly, so any other quantity must first become a voltage before the instrument can show it. Each channel probes its own node, the waveforms appear against one shared time axis, and the display keeps its accuracy far above the frequencies a digital multimeter (DMM) can follow.

---

Flashcards for this section are as follows:

- what the display shows: which quantity does an oscilloscope display, and against what? ::@:: Voltage against time.
- voltage-only instrument: any other quantity is to appear on an oscilloscope display; what must happen first? ::@:: It must become a voltage, because voltage is the only quantity the oscilloscope reads directly.
- shared axis: several channels probe their own nodes on one oscilloscope display; what do their waveforms share? ::@:: One time axis, against which every channel's waveform appears.

## probes

Each channel reaches its node through a probe. A ×10 probe divides the signal by ten before the input, and the matching ×10 setting on the oscilloscope restores the displayed scale; the same probe raises the oscilloscope's input resistance tenfold, so the channel loads the circuit less than a direct ×1 probe does.

---

Flashcards for this section are as follows:

- probe pair: a channel probes a node through a ×10 probe with the oscilloscope's ×10 setting engaged; what does the pair do to the signal? ::@:: The probe divides the signal by ten before the input and the matching setting restores the displayed scale.
- loading through a probe: how does a ×10 probe change the input resistance a channel brings to its node? ::@:: It raises the oscilloscope's input resistance tenfold above the ×1-probe value, so the channel draws less current from the node.
- direct probe: which channel loads its node more, one behind a ×1 probe or one behind a ×10 probe with the matching oscilloscope setting? ::@:: The ×1-probe channel, whose input resistance is a tenth of the ×10 probe's.

<!-- check: ignore-next-line[header_style]: established display mode -->
## X-Y display

An X-Y display drops the shared time axis and lets two channels position one dot: channel A's voltage sets the horizontal coordinate and channel B's voltage the vertical one. Two sinusoids of equal frequency separated by a phase offset trace an ellipse as the dot travels.

Two distances off that ellipse give the offset directly: $a$, where the ellipse crosses the vertical axis, and $b$, its greatest height above the horizontal axis, with $\sin\theta = a/b$.

---

Flashcards for this section are as follows:

- coordinate assignment: which channel sets which coordinate of the dot in an X-Y display? ::@:: Channel A's voltage sets the horizontal coordinate and channel B's voltage the vertical coordinate.
- trace shape: two sinusoids of equal frequency separated by a phase offset drive an X-Y display; what shape does the dot trace? ::@:: An ellipse, drawn dot by dot as each sample arrives.
- phase from the ellipse: an X-Y display traces an ellipse that crosses the vertical axis at height $a$ and reaches its greatest height $b$ above the horizontal axis; what is the phase offset? ::@:: $\sin\theta = a/b$, so the offset is the arcsine of that ratio.

## math mode

Math mode combines the channels sample by sample. Adding a steady level to a periodic waveform lifts it by that much without stretching it in time, so the repetition rate survives the sum unchanged.

---

Flashcards for this section are as follows:

- adding a constant: channel A carries a periodic waveform and channel B a steady level; what does the A + B display show? ::@:: The same waveform lifted by the steady level, repeating at its unchanged rate.
- period under a sum: a constant offset is added to a periodic waveform sample by sample; what happens to its period? ::@:: Nothing: the offset moves the waveform up without changing the period.
