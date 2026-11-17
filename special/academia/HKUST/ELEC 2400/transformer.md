---
aliases:
  - ELEC 2400 transformer
  - ELEC2400 transformer
  - HKUST ELEC 2400 transformer
  - HKUST ELEC2400 transformer
  - ideal transformer
  - transformer
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/transformer
  - language/in/English

---

# transformer

A transformer moves electrical energy from one circuit to another without a metallic connection. Two coils, the primary and the secondary, share a ferromagnetic core: the current in the primary drives a varying magnetic flux through the core, and that flux links the secondary, where it induces a voltage. For an ideal transformer all the flux passes through both coils.

The primary and secondary voltages scale with the number of turns, $V_S/V_P = N_S/N_P$, so a secondary wound with more turns than the primary raises the voltage and one with fewer turns lowers it. The magnetomotive forces of the two coils cancel in the ideal case, giving $N_PI_P = N_SI_S$ and hence $I_S/I_P = N_P/N_S$: the current scales the other way from the voltage, and the instantaneous power balance $V_PI_P = V_SI_S$ follows.

![ideal transformer: an alternating-voltage source drives the primary winding of turns N p with current I p, the dots mark the top of both windings on the shared core, and the secondary winding of turns N s drives the load Z L with current I s](attachments/transformer_ideal.svg)

---

Flashcards for this section are as follows:

- the ideal transformer: how does the drawing arrange the two windings and the dots? ::@:: The primary winding of $N_p$ turns and the secondary of $N_s$ turns sit on one shared core, a dot marks the same end of each winding, an alternating-voltage source drives the primary current $I_p$, and the load $Z_L$ carries the secondary current $I_s$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- sketch an ideal transformer between a source and a load: where do the dots sit, and what do they mark? ::@:: Two windings on one shared core, each with a dot at the same end, so the dots mark the terminals where the primary voltage $V_p$ and the secondary voltage $V_s$ share their sign. <p> ![ideal transformer: an alternating-voltage source drives the primary winding of turns N p with current I p, the dots mark the top of both windings on the shared core, and the secondary winding of turns N s drives the load Z L with current I s](attachments/transformer_ideal.svg) <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- what a transformer is: how does a transformer pass energy between circuits, and what do its two coils share? ::@:: It passes energy by induction rather than by a metallic connection: a primary and a secondary coil share a ferromagnetic core, and the varying flux driven by the primary current induces the secondary voltage.
- ideal coupling: what does the ideal transformer assume about the magnetic flux? ::@:: All of the flux passes through both coils, so none is lost between primary and secondary.
- voltage ratio: how do the primary and secondary voltages of an ideal transformer relate to the turns of each coil? ::@:: $V_S/V_P = N_S/N_P$: the voltage scales directly with the turns, so more secondary turns step the voltage up and fewer step it down. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- current ratio: how do the primary and secondary currents of an ideal transformer relate, and which way does the current scale? ::@:: $N_PI_P = N_SI_S$, so $I_S/I_P = N_P/N_S$: the current scales inversely with the turns, opposite to the voltage. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- power balance: what power balance does the ideal transformer satisfy, and what does it say about energy? ::@:: $V_PI_P = V_SI_S$ at every instant: the ideal transformer neither stores nor dissipates energy, only transfers it. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
