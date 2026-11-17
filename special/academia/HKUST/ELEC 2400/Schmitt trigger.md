---
aliases:
  - ELEC 2400 Schmitt trigger
  - ELEC2400 Schmitt trigger
  - HKUST ELEC 2400 Schmitt trigger
  - HKUST ELEC2400 Schmitt trigger
  - Schmitt trigger
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/Schmitt_trigger
  - language/in/English
---

# Schmitt trigger

A Schmitt trigger is a comparator with hysteresis. Wire the output back to the non-inverting input and the circuit gains a second threshold. A noisy input then crosses the reference once instead of chattering across it. The same positive feedback underlies the bistable circuit. With an RC circuit attached, that bistable becomes a square waveform generator.

---

Flashcards for this section are as follows:

- what gives a Schmitt trigger two thresholds instead of one? ::@:: Positive feedback from the output back to the non-inverting input. A noisy input then crosses once instead of chattering at the reference.

## comparator chatter

A comparator built from an operational amplifier in open loop compares $V_{in}$ with a reference $V_{ref}$. Noise riding on $V_{in}$ drags the input back and forth across $V_{ref} = 0\text{ V}$. A fast comparator answers each crossing on the spot, so $V_o$ makes multiple crossings before it settles at the required value.

---

Flashcards for this section are in the following format:

- noisy input: a comparator built from an operational amplifier in open loop compares $V_{in}$ with $V_{ref} = 0\text{ V}$ while noise rides on $V_{in}$; what does a very fast comparator do at the crossings? ::@:: It flips on the noise near $V_{ref}$ at once, so the output $V_o$ makes multiple crossings before settling at the required value.

## circuit

A bistable circuit has two stable states. Positive feedback around an operational amplifier produces one. Take the [non-inverting amplifier](non-inverting%20amplifier.md) and swap its $V_+$ and $V_-$ connections. The feedback turns positive, and the divider now sits on the non-inverting terminal: $R_1$ to ground, $R_2$ to the output. No input can then hold the output in between. It saturates at the positive power rail $V_{dd}$ or the negative power rail $-V_{ss}$.

![Schmitt trigger circuit: an operational amplifier with V in arriving at its inverting input, and a rail above the triangle carrying the R 1 R 2 divider from ground into the non-inverting input, R 2 returning down to the output node beside V o](attachments/schmitt_trigger.svg)

Those two rails are the two stable solutions that positive feedback admits. The [negative feedback](negative%20feedback.md) note counts on the same two. Both come from the amplifier's own characteristic, which is flat at $V_{dd}$ and at $-V_{ss}$. The divider returns $V_+ = \frac{R_1}{R_1+R_2}V_o$ while $V_{in}$ holds $V_-$, so the feedback line runs with slope $\frac{R_1}{R_1+R_2}$ and cuts the characteristic three times. Two crossings sit on the flat rails, and both are stable: those are the two states. The middle crossing satisfies the loop too, but nothing rests there. Any deviation, however small, grows instead of dying away. The output leaves for one of the two rails instead of settling halfway.

---

Flashcards for this section are in the following format:

- bistable circuit: how does a non-inverting amplifier built from an operational amplifier become a bistable circuit, and where does its output sit? ::@:: Swap the $V_+$ and $V_-$ connections and the feedback turns from negative into positive, giving two stable states. The output saturates at either the positive power rail $V_{dd}$ or the negative power rail $-V_{ss}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- three solutions and two states: a bistable circuit outputs $V_{dd}$ or $-V_{ss}$ in its two states; which solutions of positive feedback are those, and what is the third? ::@:: The two stable ones: the crossings on the flat rails at $V_{dd}$ and $-V_{ss}$. The third, the crossing on the steep middle, is unstable and never a resting place.
- the unstable solution in practice: the third crossing of the positive-feedback line is a solution, so why can the output never stay there? ::@:: A deviation from it grows instead of dying away, so the smallest disturbance sends the output to one of the two stable rails; the middle satisfies the loop too, but cannot hold the output.
- how is a Schmitt trigger built from a comparator and the divider $R_1$, $R_2$ of a non-inverting amplifier, and what separates it from a plain comparator? ::@:: Take a comparator and the non-inverting amplifier's divider of $R_1$ and $R_2$, and move the divider from the inverting terminal to the non-inverting one so the feedback turns positive. Those two resistors are the whole difference.
- the Schmitt trigger drawing: where does the divider hang from, and where does $V_{in}$ arrive? <p> ![Schmitt trigger circuit: an operational amplifier with V in arriving at its inverting input, and a rail above the triangle carrying the R 1 R 2 divider from ground into the non-inverting input, R 2 returning down to the output node beside V o](attachments/schmitt_trigger.svg) ::@:: It hangs from a rail above the triangle: ground through $R_1$ into the tap on the non-inverting input, then $R_2$ from that tap down to the output node. $V_{in}$ arrives at the inverting input below.
- draw a Schmitt trigger around an operational amplifier: where do $R_1$, $R_2$, $V_{in}$ and $V_o$ go? ::@:: $V_{in}$ into the inverting input, $R_1$ from the non-inverting input to ground, $R_2$ from the output to that same input, and $V_o$ taken at the output node. <p> ![Schmitt trigger circuit: an operational amplifier with V in arriving at its inverting input, and a rail above the triangle carrying the R 1 R 2 divider from ground into the non-inverting input, R 2 returning down to the output node beside V o](attachments/schmitt_trigger.svg)

## thresholds

The tap sits at $V_+$, and $V_{in}$ stays outside the loop, so the output alone decides what the tap sees. Set $V_{ss} = V_{dd}$ for simplicity and start from $V_o = V_{dd}$. The divider then puts the tap at $V_H = \frac{R_1}{R_1+R_2}V_{dd}$, the high threshold, and the output stays there as long as $V_{in} < V_H$.

Raise $V_{in}$ past $V_H$ and the output trips to $-V_{dd}$. The divider drags the tap down to $V_L = -\frac{R_1}{R_1+R_2}V_{dd}$, and the output holds $-V_{dd}$ as long as $V_{in} > V_L$, the low threshold.

The sense is inverted throughout, because $V_{in}$ works on the inverting terminal: a high input drives the output low, and a low input drives it high.

Each threshold is where one of those stable crossings disappears. Above $V_H$ the crossing at $+V_{dd}$ no longer exists, and the low rail is the only solution left. Below $V_L$ the crossing at $-V_{dd}$ is gone instead. In between, both crossings exist, so the output holds whichever state it is in.

---

Flashcards for this section are in the following format:

- thresholds: a Schmitt trigger built from an operational amplifier holds $R_1$ from the non-inverting terminal to ground, $R_2$ from the output to that terminal, $V_{in}$ at the inverting terminal and $V_{ss} = V_{dd}$; what are its thresholds $V_H$ and $V_L$? ::@:: The divider gives $V_H = \frac{R_1}{R_1+R_2}V_{dd}$ when $V_o = +V_{dd}$, and $V_L = -\frac{R_1}{R_1+R_2}V_{dd}$ when $V_o = -V_{dd}$.
- trip and hold: in that Schmitt trigger with $V_o = +V_{dd}$ and the non-inverting terminal at $V_H$, what happens as $V_{in}$ rises past $V_H$, and what keeps $V_o$ at $-V_{dd}$ afterwards? ::@:: Once $V_{in} > V_H$ the output trips to $-V_{dd}$ and the divider moves to $V_L$. As long as $V_{in}$ stays above $V_L$, the low threshold, $V_o$ remains at $-V_{dd}$.
- why the switch happens at $V_H$ and $V_L$: why does the output switch exactly at $V_H$ and $V_L$ rather than anywhere between them? ::@:: Past $V_H$ the crossing at $+V_{dd}$ no longer exists, so the low rail is the only solution left. Below $V_L$ the crossing at $-V_{dd}$ is gone instead, and between the two both crossings exist.
- inverted sense: a Schmitt trigger built from an operational amplifier has $V_{in}$ at the inverting terminal; what does a high $V_{in}$ do to $V_o$, and what does a low one do? ::@:: A high $V_{in}$ drives $V_o$ low, and a low $V_{in}$ drives it high: the output moves opposite to the input.

## hysteresis

Picture the circuit holding its output. It switches only when the input is pushed too far, then holds the other state. Push just as far the other way and it switches back. Between the two thresholds the input wanders freely. Neither state is in danger, so the output stays put.

Plotting $V_o$ against $V_{in}$ gives the direct-current (DC) transfer characteristic of the Schmitt trigger. The output sits at $+V_{dd}$ until $V_{in}$ climbs to $V_H = \frac{R_1}{R_1+R_2}V_{dd}$. There it drops to $-V_{dd}$ and stays low until $V_{in}$ falls to $V_L = -\frac{R_1}{R_1+R_2}V_{dd}$. It climbs back to $+V_{dd}$ there, and the curve never retraces itself.

$\Delta V_{hys} = V_H - V_L$ is the hysteresis window. $R_1$ and $R_2$ adjust it.

![Schmitt trigger transfer characteristic: the output sits at V dd until the input rises to the high threshold V H, drops to minus V dd there, stays low until the input falls to the low threshold V L, and returns to V dd there, the two thresholds spanning the hysteresis window](attachments/schmitt_hysteresis.svg)

With $V_{ref} = 0$, a suitably sized hysteresis window keeps out the multiple crossings that a noisy input brings to a plain comparator. The cost is a shifted output waveform, since $V_H \neq V_L \neq 0$.

---

Flashcards for this section are in the following format:

- hysteresis window: what quantity measures the hysteresis of a Schmitt trigger with thresholds $V_H$ and $V_L$, and what adjusts it? ::@:: $\Delta V_{hys} = V_H - V_L$ is the hysteresis window, and $R_1$ and $R_2$ adjust it.
- transfer characteristic: what does the direct-current (DC) transfer characteristic of a Schmitt trigger with $V_{ss} = V_{dd}$ look like as $V_{in}$ sweeps? ::@:: $V_o$ sits at $+V_{dd}$, jumps to $-V_{dd}$ at $V_{in} = V_H = \frac{R_1}{R_1+R_2}V_{dd}$, and jumps back at $V_{in} = V_L = -\frac{R_1}{R_1+R_2}V_{dd}$. The curve does not retrace itself. <p> ![Schmitt trigger transfer characteristic: the output sits at V dd until the input rises to the high threshold V H, drops to minus V dd there, stays low until the input falls to the low threshold V L, and returns to V dd there, the two thresholds spanning the hysteresis window](attachments/schmitt_hysteresis.svg)
- draw the Schmitt trigger's transfer characteristic on $V_o$-against-$V_{in}$ axes: which way does the trace run, and what do the two vertical segments mark? ::@:: The trace runs right along $+V_{dd}$ to $V_H$, drops to $-V_{dd}$, carries on right, then comes back along $-V_{dd}$ to $V_L$ and jumps up again. Those two vertical segments are the jumps, and $\Delta V_{hys}$ is the gap between them. <p> ![Schmitt trigger transfer characteristic: the output sits at V dd until the input rises to the high threshold V H, drops to minus V dd there, stays low until the input falls to the low threshold V L, and returns to V dd there, the two thresholds spanning the hysteresis window](attachments/schmitt_hysteresis.svg)
- noise rejection: with $V_{ref} = 0$, what does sizing the hysteresis window of a Schmitt trigger do against a noisy input, and what does it cost? ::@:: It keeps out the multiple crossings, but the output waveform shifts since $V_H \neq V_L \neq 0$.
- state keeping: what does a Schmitt trigger do with the state it is in, and what makes it change? ::@:: It holds that state until the input is pushed past a threshold, then switches to the other state. A push past the second threshold sends it back.
- input between the thresholds: why can the input of a Schmitt trigger wander between the thresholds without moving the output? ::@:: Neither state is in danger between the thresholds, so the circuit keeps its current state and the output stays put.

## square waveform generator

Two changes turn a Schmitt trigger into a square waveform generator: make the hysteresis window $\Delta V_{hys}$ large, and drive an RC circuit from the comparator output. The comparator output then swings square between $V_{dd}$ and $-V_{dd}$, while the RC voltage charges and discharges between $V_H$ and $V_L$. That rectangle is the ideal picture. A real comparator spends a finite time changing its output, so each vertical jump is a short transition rather than a step. Make the RC time constant much larger than the period and the capacitor cannot follow the edge. It keeps charging at its own slow rate while the output moves, stretching each corner into a visible ramp. When those ramps fill the cycle, the same circuit puts out a triangle.

---

Flashcards for this section are in the following format:

- construction: how do you turn a Schmitt trigger built from an operational amplifier into a square waveform generator? ::@:: Two changes: make the hysteresis window $\Delta V_{hys}$ large, and drive an RC circuit from the comparator output. The comparator output then swings square between $V_{dd}$ and $-V_{dd}$, while the RC voltage moves between $V_H$ and $V_L$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- triangular waveform: under what condition on the RC circuit of a square waveform generator does a triangular waveform come out instead? ::@:: With the RC time constant much larger than the period, the waveform comes out triangular.
- the jumps of a real generator: the ideal picture has the output jump from $V_{dd}$ to $-V_{dd}$; what happens at those edges in a real circuit? ::@:: A real comparator spends a finite time changing its output, so each jump is a short transition rather than an instantaneous step.
- a slow RC in the square waveform generator: what does an RC time constant much larger than the period do to the corners of the square, and what waveform comes out? ::@:: The capacitor cannot follow the edge and keeps charging at its own slow rate while the output moves, so each corner is drawn out into a visible ramp, and a triangle comes out instead of a square.
