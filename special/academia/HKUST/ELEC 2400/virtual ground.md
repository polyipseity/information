---
aliases:
  - ELEC 2400 virtual ground
  - ELEC2400 virtual ground
  - HKUST ELEC 2400 virtual ground
  - HKUST ELEC2400 virtual ground
  - virtual ground
  - virtual short
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/virtual_ground
  - language/in/English
---

# virtual ground

A virtual ground is a node that holds a reference potential without a wire to the reference. Operational amplifier circuits make one out of feedback: negative feedback pins the inverting input to the potential the non-inverting input sits at, and the ideal device draws no current at either terminal to disturb it.

---

Flashcards for this section are as follows:

- the two assumptions behind ideal operational amplifier analysis of $V_+$, $V_-$, $I_+$ and $I_-$ ::@:: The virtual short $V_+ = V_-$, and the zero-input-current assumption $I_+ = I_- = 0$.
- what kind of node the virtual short creates ::@:: One input holds the potential of the other with no wire between them.

## virtual short and zero-input-current assumptions

Ideal operational amplifier analysis rests on two named assumptions: the virtual short, $V_+ = V_-$, and the zero-input-current assumption, $I_+ = I_- = 0$.

Both hold only while the device stays in its linear region instead of saturating, and only under a negative feedback connection that leaves the output finite. The virtual short therefore comes with a check to make every time: $-V_{ss} < V_+, V_-, V_o < V_{dd}$.

Zero input current concerns the input terminals alone. The output current $I_o$ need not be zero.

---

Flashcards for this section are in the following format:

- the two assumptions ::@:: The virtual short assumption, $V_+ = V_-$, and the zero-input-current assumption, $I_+ = I_- = 0$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- validity of the virtual short: before applying the virtual short $V_+ = V_-$ in an operational amplifier, what operating conditions must hold, and what voltage check comes with them? ::@:: The device must work in its linear region rather than in positive or negative saturation, under proper negative feedback with a finite output, and $-V_{ss} < V_+, V_-, V_o < V_{dd}$ must be checked every time.
- output current: does the zero-input-current assumption $I_+ = I_- = 0$ force the output current of an operational amplifier to vanish? ::@:: No: it covers the input terminals only, and the output current $I_o$ is not necessarily zero.
