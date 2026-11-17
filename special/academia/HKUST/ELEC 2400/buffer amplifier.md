---
aliases:
  - ELEC 2400 buffer amplifier
  - ELEC2400 buffer amplifier
  - HKUST ELEC 2400 buffer amplifier
  - HKUST ELEC2400 buffer amplifier
  - buffer amplifier
  - unity-gain buffer
  - voltage follower
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/buffer_amplifier
  - language/in/English
---

# buffer amplifier

A buffer amplifier copies a voltage from one circuit to the next without letting either side load the other. Its gain is one, so the voltage that leaves equals the voltage that arrives.

---

Flashcards for this section are as follows:

- what does a buffer amplifier change as a signal passes through it, and what does it leave alone? ::@:: It changes the impedance each side sees, because its input draws no current and its output holds the voltage under load; the voltage itself passes through at gain one.

## unity-gain buffer

The output is wired straight back to the inverting input, and the signal drives the non-inverting input, so the ideal rules fix the gain at 1. The output is tied to $V_-$, so $V_{\text{out}} = V_-$, while the source sets $V_+ = V_{\text{in}}$; the rule $V_+ \approx V_-$ then gives $V_{\text{out}} = V_{\text{in}}$.

The circuit needs no resistors. The output is already wired back to the inverting input, so the virtual short has nothing left to choose. Whatever voltage the source puts at the non-inverting terminal turns up at the output. The stage passes that signal through unchanged, and the source sees the operational amplifier's very high input resistance $R_i$ while the load sees its very low output resistance $R_o$; that isolation is what a buffer is there for. What it costs is design freedom, since the gain is 1 and no divider sits there to change it.

![unity-gain buffer: the source drives the non-inverting input directly and the output is wired back to the inverting input, so no feedback divider is needed](attachments/buffer_amplifier.svg)

---

Flashcards for this section are in the following format:

- the unity-gain buffer: what does the drawing connect to the inverting input? ::@:: The output itself, wired straight back, so the feedback factor is one and the output follows the input.
- sketch a unity-gain buffer driven by a source: where does the source attach, and what returns to the inverting input? ::@:: The source attaches to the non-inverting input, and the output returns directly to the inverting input with no divider. <p> ![unity-gain buffer: the source drives the non-inverting input directly and the output is wired back to the inverting input, so no feedback divider is needed](attachments/buffer_amplifier.svg)
- why does a unity-gain buffer need no resistors to hold $V_{\text{out}} = V_{\text{in}}$, and what does that cost? ::@:: The output $V_{\text{out}}$ is already tied to the inverting input, so the virtual short leaves nothing to choose and it follows $V_{\text{in}}$ by itself; the cost is a gain fixed at 1 with no divider to change it.
- in a unity-gain buffer, what is the virtual short comparing $V_{\text{out}}$ with? ::@:: Its own output: $V_-$ is $V_{\text{out}}$, so the loop settles only where $V_{\text{in}}$ sits.
- unity-gain buffer: how is a unity-gain buffer built from an operational amplifier, and what gain does the ideal analysis give? ::@:: The output is fed back directly to the inverting input while the signal drives the non-inverting input; since $V_{\text{out}} = V_-$ and $V_+ = V_{\text{in}}$, the rule $V_+ \approx V_-$ gives $V_{\text{out}} = V_{\text{in}}$, a gain of 1. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- what the buffer presents: what does a unity-gain buffer do to the signal, and what resistances does it present at its input and output? ::@:: It passes the signal from input to output unchanged with gain 1, presenting the operational amplifier's input resistance $R_i$ at its input and its output resistance $R_o$ at its output. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## unity-gain buffer driving a resistive load

A wire between input and output would carry the same voltage, but a unity-gain buffer can also drive a resistive load. A divider of two $1\text{ k}\Omega$ resistors off $2\text{ V}$ sits at $1\text{ V}$ with nothing attached. Connect a $100\ \Omega$ load straight to its tap and $V_o$ moves away from $1\text{ V}$, because the divider cannot drive the resistor. The same load behind a unity-gain buffer leaves $V_o = 1\text{ V}$.

No current enters the buffer, $I = 0\text{ A}$, so the tap stays undisturbed, and the operational amplifier's internal controlled voltage source supplies the load current.

---

Flashcards for this section are in the following format:

- divider under load: a divider of two $1\text{ k}\Omega$ resistors off $2\text{ V}$ sits at $1\text{ V}$ unloaded; what happens to its tap when a $100\ \Omega$ load connects straight to it, and what does a unity-gain buffer built from an operational amplifier give under the same load? ::@:: Straight to the tap the divider cannot drive the resistor and $V_o$ moves away from $1\text{ V}$; behind a unity-gain buffer the load leaves $V_o = 1\text{ V}$.
- why the buffer holds: why can a unity-gain buffer hold $V_o$ at its input voltage under a $100\ \Omega$ load while a plain wire from the loaded tap cannot? ::@:: No current enters the buffer, $I = 0\text{ A}$, so its input leaves the upstream circuit undisturbed while the operational amplifier's internal controlled voltage source delivers the load current; a wire leaves the load to pull the tap down.
