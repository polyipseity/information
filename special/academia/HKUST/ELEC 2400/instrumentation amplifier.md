---
aliases:
  - ELEC 2400 instrumentation amplifier
  - ELEC2400 instrumentation amplifier
  - HKUST ELEC 2400 instrumentation amplifier
  - HKUST ELEC2400 instrumentation amplifier
  - in-amp
  - instrumentation amplifier
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/instrumentation_amplifier
  - language/in/English
---

# instrumentation amplifier

An instrumentation amplifier is a difference amplifier whose two inputs are buffered, so it amplifies $V_2 - V_1$ without drawing current from either source and without needing matched source resistances. Two [operational amplifiers](operational%20amplifier.md) take $V_1$ and $V_2$ directly at their non-inverting terminals, and one $R_1$ returns each output to its own inverting terminal. The two inverting terminals join through $R$, the gain resistor, so the virtual short that pins them at $V_1$ and $V_2$ leaves $I = \frac{V_2 - V_1}{R}$ flowing through $R$ and on through both $R_1$ resistors. Adding the drops along that path gives $V_o = I(R + 2R_1) = \left(1+\frac{2R_1}{R}\right)(V_2-V_1)$.

Start on the middle resistor, because the difference ends up there. The virtual short holds its two ends at $V_2$ and $V_1$, so the current through it is exactly $\frac{V_2-V_1}{R}$. The input difference has become a current. Nothing enters the op-amp inputs, so both $R_1$ resistors carry that same current outwards, and each output sits one $R_1$ drop beyond its own tap. Add those two drops to the drop across $R$ and the current is a voltage again, larger than the difference by $1+\frac{2R_1}{R}$.

Two properties follow from the buffered inputs. The input resistance is very high, so no current is drawn from the sources, unlike the plain [difference amplifier](differential%20amplifier.md#difference%20amplifier) that loads them with its own two matched input resistors. And the gain moves with $R$ alone, where the four-resistor version needs matching changes to pairs. The output here is a differential voltage, which is the one drawback.

![instrumentation amplifier: two operational amplifiers whose non-inverting inputs carry V 2 and V 1, a string of R 1, R, and R 1 between the two outputs with each inverting input tapping the string, and the output read between the two op-amp outputs](attachments/instrumentation_amplifier.svg)

---

Flashcards for this section are as follows:

- the instrumentation amplifier: what does the resistor string between the two outputs consist of? ::@:: $R_1$, then the gain resistor $R$, then another $R_1$, with each inverting input tapping the string between neighbours, and the differential output read across the two op-amp outputs. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- read the instrumentation amplifier as a current first: which resistor $R$ carries the input difference, and where does that current go? ::@:: $R$ carries $\frac{V_2-V_1}{R}$ because the virtual short holds its ends at $V_2$ and $V_1$; each $R_1$ carries that same current outward to its own output, so the output difference picks it up over $R$ and again over both $R_1$ resistors.
- why do the two $R_1$ resistors of the instrumentation amplifier not load either source? ::@:: Both signals enter non-inverting terminals, so each source faces an open circuit, and the difference current is made inside the amplifier, between the two $R_1$ resistors.
- draw a differential-output instrumentation amplifier: where do the two signals enter, and where does the gain resistor sit? ::@:: The signals $V_2$ and $V_1$ enter the two non-inverting inputs, and the gain resistor $R$ sits mid-string between the two matched $R_1$ resistors hanging between the outputs. <p> ![instrumentation amplifier: two operational amplifiers whose non-inverting inputs carry V 2 and V 1, a string of R 1, R, and R 1 between the two outputs with each inverting input tapping the string, and the output read between the two op-amp outputs](attachments/instrumentation_amplifier.svg) <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- instrumentation amplifier gain: two operational amplifiers take $V_1$ and $V_2$ at their non-inverting terminals, join their inverting terminals through $R$, and return each output to its own inverting terminal through $R_1$. What differential output $V_o$ results? ::@:: $V_o = \left(1+\frac{2R_1}{R}\right)(V_2-V_1)$.
- instrumentation amplifier trade-offs: which two advantages does the differential-output instrumentation amplifier hold over the difference amplifier? ::@:: The input resistance is very high, so no current is drawn from the sources, and one resistor $R$ adjusts the gain. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the trade-off that remains ::@:: The output is a differential voltage.

## built from two non-inverting amplifiers

Each input gets its own [non-inverting amplifier](non-inverting%20amplifier.md), and the two dividers meet instead of returning to ground. Each output returns $R_1$ to its own tap, and the two taps share the gain resistor $R$, so one amplifier's divider ends where the other's begins.

---

Flashcards for this section are in the following format:

- how is the instrumentation amplifier built from two non-inverting amplifiers, and which resistor $R$ do their dividers share? ::@:: Two non-inverting amplifiers, one per input, whose dividers share the gain resistor $R$ instead of each returning to ground; the voltage across that shared resistor is the input difference, and the pair gives $1 + \frac{2R_1}{R}$.
- build the single-ended instrumentation amplifier in order, the added parts being $R_2$, $R_2$ and $R_G$: what comes first, then second, then third? ::@:: Join two non-inverting amplifiers by a resistor between their inverting terminals, so the input difference becomes a current. Add the two $R_1$ resistors so both amplifiers keep negative feedback. Then add $R_2$, a second $R_2$ and $R_G$ only where the two nodes need separating.

## single-ended output

A differential output exists only between the two op-amp outputs: each one carries the common-mode level plus half the amplified difference. The stage that follows, a filter or an analog-to-digital converter, has a ground-referenced input, so it would read that half and pick up the common mode with it. Taking $V_o$ at the top output alone fixes this, and it costs the bottom output its job: that output is no longer a signal, only an internal node that a divider holds.

The conversion adds three resistors around the two $R_1$ resistors already in the circuit. $R_2$ drops from the top output to the $V_2$ tap, a second $R_2$ runs from the bottom output to ground, and $R_G$ goes from the $V_2$ tap across to that bottom output. Read from $V_o$ down to ground, the string is now $R_2$, $R_1$, $R_1$, $R_2$, and the two $R_1$ resistors still carry the input difference, as $I_a$ and $I_b$.

Build it from nothing in three steps. Join two non-inverting amplifiers with a resistor between their inverting terminals, and that resistor then carries the input difference as a current. Give each amplifier its negative feedback in the usual way, which means returning its output to its own inverting terminal through $R_1$. Last, add the parts that give the two ends a level of their own: $R_2$ above the $V_2$ tap, a second $R_2$ from the bottom output to ground, and $R_G$ across the pair.

The derivation starts from the same sum as the differential version. The virtual short still pins the taps at $V_2$ and $V_1$, so the drops across the two $R_1$ resistors add to the whole input difference, $\frac{V_2-V_1}{R_1} = I_a + I_b$. It treats $R_G$ as dropping that whole difference, which adds $\frac{V_2-V_1}{R_G}$ to both branches, so its share counts twice. Writing each branch current against the $R_2$ that feeds it and collecting terms gives $\frac{V_o}{R_2} = \left(\frac{1}{R_1}+\frac{1}{R_2}+\frac{2}{R_G}\right)(V_2-V_1)$, and multiplying by $R_2$ gives $V_o = \left(1+\frac{R_2}{R_1}+\frac{2R_2}{R_G}\right)(V_2-V_1)$.

The terms say where the gain comes from. The $1$ passes the difference through unchanged, $\frac{R_2}{R_1}$ is the scaling the $R_2/R_1$ divider applies to it, and $\frac{2R_2}{R_G}$ is $R_G$'s share counted twice, once at each $R_1$ branch. All three properties the differential version wanted survive: very high input resistance, a gain trimmed by $R_G$, and an output taken against ground.

![instrumentation amplifier with a single-ended output: the top operational amplifier's output becomes V o, and a string of R 2, R 1, R 1 and R 2 runs down from it to ground, with the V 2 tap feeding the top inverting input, the V 1 tap feeding the bottom one, R G hanging to the right from the V 2 tap down to the bottom output node, and the bottom operational amplifier driving that node](attachments/instrumentation_amplifier_single_ended.svg)

---

Flashcards for this section are as follows:

- why does the differential instrumentation amplifier need a single-ended version, and what becomes of the bottom output? ::@:: The next stage is referenced to ground and would see only one output, so $V_o$ is taken at the top one and the bottom output becomes an internal node that the added divider holds. <p> ![instrumentation amplifier with a single-ended output: the top operational amplifier's output becomes V o, and a string of R 2, R 1, R 1 and R 2 runs down from it to ground, with the V 2 tap feeding the top inverting input, the V 1 tap feeding the bottom one, R G hanging to the right from the V 2 tap down to the bottom output node, and the bottom operational amplifier driving that node](attachments/instrumentation_amplifier_single_ended.svg) <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the single-ended instrumentation amplifier: which parts does the drawing add, and where do they sit? ::@:: $R_2$ from the top output to the $V_2$ tap, a second $R_2$ from the bottom output to ground, and $R_G$ from the $V_2$ tap across to that output, so the string reads $R_2$, $R_1$, $R_1$, $R_2$ from $V_o$ to ground. <p> ![instrumentation amplifier with a single-ended output: the top operational amplifier's output becomes V o, and a string of R 2, R 1, R 1 and R 2 runs down from it to ground, with the V 2 tap feeding the top inverting input, the V 1 tap feeding the bottom one, R G hanging to the right from the V 2 tap down to the bottom output node, and the bottom operational amplifier driving that node](attachments/instrumentation_amplifier_single_ended.svg) <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- single-ended-output instrumentation amplifier: with $R_G$ dropping the whole input difference, what does the derivation sum? ::@:: The taps stay at $V_2$ and $V_1$, so the two $R_1$ drops add to $\frac{V_2-V_1}{R_1}=I_a+I_b$.
- why $R_G$'s share appears twice in that derivation ::@:: $R_G$ carries $\frac{V_2-V_1}{R_G}$ on both branches, giving $V_o = \left(1+\frac{R_2}{R_1}+\frac{2R_2}{R_G}\right)(V_2-V_1)$. <p> ![instrumentation amplifier with a single-ended output: the top operational amplifier's output becomes V o, and a string of R 2, R 1, R 1 and R 2 runs down from it to ground, with the V 2 tap feeding the top inverting input, the V 1 tap feeding the bottom one, R G hanging to the right from the V 2 tap down to the bottom output node, and the bottom operational amplifier driving that node](attachments/instrumentation_amplifier_single_ended.svg)
