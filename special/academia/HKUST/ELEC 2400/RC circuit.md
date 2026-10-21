---
aliases:
  - ELEC 2400 RC circuit
  - ELEC2400 RC circuit
  - HKUST ELEC 2400 RC circuit
  - HKUST ELEC2400 RC circuit
  - RC circuit
  - resistor–capacitor circuit
  - time constant
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/RC_circuit
  - language/in/English
---

# RC circuit

An RC circuit is one resistor and one capacitor in series with a source, with the output taken across the capacitor. Drive it with $v_s(t) = V_s\cos\omega t$. Kirchhoff's voltage law splits the source across the two elements, $v_s = v_R + v_C$. The resistor obeys [Ohm's law](Ohm's%20law.md), $v_R = Ri$, and the capacitor carries $i = C\,dv_C/dt$. Putting the second relation into the first removes the current and leaves one equation for $v_C$: $RC\frac{dv_C}{dt} + v_C = v_s(t)$. Dividing by $\tau = RC$ puts it in the standard form $\frac{dv_C}{dt} + \frac{v_C}{\tau} = \frac{v_s(t)}{\tau}$ ([Capacitor](capacitor.md)).

---

Flashcards for this section are as follows:

- the equation: with the output across the capacitor of an RC circuit driven by $V_s\cos\omega t$, what differential equation does $v_o$ satisfy? ::@:: $RC\,dv_o/dt + v_o = V_s\cos\omega t$, from Kirchhoff's voltage law with $i = C\,dv_o/dt$.

## solving the equation

A first-order linear equation needs two pieces: every solution of the homogeneous equation $\frac{dv_C}{dt} + \frac{v_C}{\tau} = 0$, and one particular solution that matches the drive. The homogeneous part describes the circuit with the drive removed, and separating the variables solves it. From $\frac{dv_C}{dt} = -\frac{v_C}{\tau}$ comes $\frac{dv_C}{v_C} = -\frac{dt}{\tau}$, then $\ln v_C = -t/\tau + \text{constant}$, so $v_C(t) = Ke^{-t/\tau}$. The constant $K$ stays free until the starting state fixes it.

The full equation still needs one particular solution, which undetermined coefficients supply for a sinusoidal drive. Guess $v_C = A\cos\omega t + B\sin\omega t$, whose derivative is $-A\omega\sin\omega t + B\omega\cos\omega t$. Substituting and collecting gives $\tau\frac{dv_C}{dt} + v_C = (A + \omega\tau B)\cos\omega t + (B - \omega\tau A)\sin\omega t$, and matching it against $V_s\cos\omega t$ leaves two equations, $A + \omega\tau B = V_s$ and $B - \omega\tau A = 0$. The second gives $B = \omega\tau A$, and the first then gives $A = \frac{V_s}{1 + \omega^2\tau^2}$ and $B = \frac{V_s\omega\tau}{1 + \omega^2\tau^2}$. The two combine into $v_{C,p}(t) = \frac{V_s}{\sqrt{1 + \omega^2\tau^2}}\cos(\omega t - \theta)$ with $\theta = \tan^{-1}(\omega\tau)$, since $\sqrt{A^2 + B^2}$ is the amplitude and $\tan^{-1}(B/A)$ the phase ([sine wave](sine%20wave.md)).

The impedance divider reaches the same result in one line, $\frac{\mathbf{V}_C}{\mathbf{V}_s} = \frac{1/(j\omega C)}{R + 1/(j\omega C)} = \frac{1}{1 + j\omega\tau}$, with magnitude $1/\sqrt{1 + \omega^2\tau^2}$ and angle $-\tan^{-1}(\omega\tau)$. Matching coefficients shows where the numbers come from; the phasor gets them without the algebra ([Electrical impedance](electrical%20impedance.md)).

---

Flashcards for this section are as follows:

- solving the equation / the homogeneous part: what is the solution of $\frac{dv_C}{dt} + \frac{v_C}{\tau} = 0$, and how is it found? ::@:: $v_C = Ke^{-t/\tau}$, by separating the variables and integrating $\int dv_C/v_C = -\int dt/\tau$.
- solving the equation / the guess: what does substituting the guess $v_C = A\cos\omega t + B\sin\omega t$ into $\tau\,dv_C/dt + v_C = V_s\cos\omega t$ produce? ::@:: The pair $A + \omega\tau B = V_s$ and $B - \omega\tau A = 0$, so $A = V_s/(1 + \omega^2\tau^2)$ and $B = V_s\omega\tau/(1 + \omega^2\tau^2)$.
- solving the equation / the phasor check: what is $\frac{\mathbf{V}_C}{\mathbf{V}_s}$ from the impedance divider, and how does it compare with matching coefficients? ::@:: $\frac{1}{1 + j\omega\tau}$, magnitude $1/\sqrt{1 + \omega^2\tau^2}$ and angle $-\tan^{-1}(\omega\tau)$: the same results, without the algebra.

## complete response

The general solution is the sum of the two, $v_C(t) = Ke^{-t/\tau} + \frac{V_s}{\sqrt{1 + \omega^2\tau^2}}\cos(\omega t - \theta)$, and the initial voltage fixes $K$. At $t = 0$ this gives $v_C(0) = K + \frac{V_s\cos\theta}{\sqrt{1 + \omega^2\tau^2}}$. Since $\cos\theta = 1/\sqrt{1 + \omega^2\tau^2}$, the second term is $\frac{V_s}{1 + \omega^2\tau^2}$, leaving $K = V_0 - \frac{V_s}{1 + \omega^2\tau^2}$ when the capacitor starts at $v_C(0) = V_0$.

$Ke^{-t/\tau}$ is the transient response. It carries $K$, the gap between the starting voltage and the steady state, and decays with the time constant until it is gone. The other term is the steady-state response: a sinusoid at the drive frequency, lagging the source by $\theta = \tan^{-1}(\omega\tau)$ and smaller by the factor $1/\sqrt{1 + \omega^2\tau^2}$. Nothing in it depends on the starting state.

Phasor analysis computes this steady-state part and nothing else: $\frac{\mathbf{V}_o}{\mathbf{V}_s} = \frac{1}{1 + j\omega CR}$ ([Electrical impedance](electrical%20impedance.md)). A decaying exponential has no phasor.

---

Flashcards for this section are as follows:

- complete response / the two pieces: which two responses make up $v_o(t) = Ke^{-t/\tau} + \frac{V_s}{\sqrt{1 + \omega^2\tau^2}}\cos(\omega t - \theta)$? ::@:: The transient response $Ke^{-t/\tau}$ and the steady-state response $\frac{V_s}{\sqrt{1 + \omega^2\tau^2}}\cos(\omega t - \theta)$.
- complete response / the constant: what fixes the constant $K$ in the transient term? ::@:: The initial voltage on the capacitor: the transient carries the circuit's starting state into the solution.
- complete response / the formula for the constant: what is $K$, given the initial voltage $v_C(0) = V_0$? ::@:: $K = V_0 - \frac{V_s}{1 + \omega^2\tau^2}$, the starting voltage minus the steady-state value at $t = 0$.
- complete response / the decay: how long does the transient term $Ke^{-t/\tau}$ last? ::@:: It decays exponentially with the time constant $\tau = RC$ and is gone after a few time constants.
- complete response / the steady-state part: what amplitude and phase does the steady-state response of the RC circuit carry? ::@:: The amplitude $V_s/\sqrt{1 + \omega^2\tau^2}$, smaller than the source, and the phase lag $\theta = \tan^{-1}(\omega\tau)$, both set by the circuit and the driving frequency alone. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- complete response / what phasors deliver: which part of the RC response does phasor analysis compute? ::@:: The steady-state sinusoid alone, through $\frac{\mathbf{V}_o}{\mathbf{V}_s} = \frac{1}{1 + j\omega CR}$; the decaying transient lies outside the phasor picture. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## the time constant

$\tau = RC$ sets the pace. Its units come out as seconds: $\Omega\cdot\text{F} = \frac{\text{V}}{\text{A}}\cdot\frac{\text{C}}{\text{V}} = \frac{\text{C}}{\text{A}} = \text{s}$. In $Ke^{-t/\tau}$ one time constant leaves $e^{-1} = 0.368$ of the starting gap, five leave $e^{-5} = 0.0067$, and beyond that the transient is spent.

---

Flashcards for this section are as follows:

- the time constant / the definition: what is the time constant $\tau$ of an RC circuit, and in what units is it measured? ::@:: $\tau = RC$, the product of the resistance and the capacitance, in seconds.
- the time constant / the units: why does $\tau = RC$ come out in seconds? ::@:: An ohm times a farad is $\frac{\text{V}}{\text{A}}\cdot\frac{\text{C}}{\text{V}} = \frac{\text{C}}{\text{A}}$, and a coulomb per ampere is one second.
- the time constant / one constant: what fraction of the starting gap is left after one time constant? ::@:: $e^{-1} = 0.368$, so 63.2% of the gap has closed. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the time constant / five constants: what fraction of the starting gap is left after five time constants? ::@:: $e^{-5} = 0.0067$, under 1%, which is why five time constants count as settled. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## step response

A constant source shows the time constant most plainly. With $v_s = V_s$ the particular solution is the constant $V_s$, since its derivative vanishes. So $v_C(t) = V_s + (V_0 - V_s)e^{-t/\tau}$, or with both endpoints written out, $v_C(t) = v_C(\infty) + [v_C(0) - v_C(\infty)]\,e^{-t/\tau}$.

Charging from rest is the case $V_0 = 0$, giving $v_C(t) = V_s(1 - e^{-t/\tau})$: $63.2\%$ of the source in one time constant and $99.3\%$ in five. Remove the source instead and it is $v_C(t) = V_0e^{-t/\tau}$, the charge draining through the same resistor.

The curve leaves $v_C(0)$ at the rate $[v_C(\infty) - v_C(0)]/\tau$, so the tangent drawn there meets the final value at exactly $t = \tau$. A straight line at that opening pace would arrive after one time constant; the exponential keeps slowing down and takes longer.

---

Flashcards for this section are as follows:

- step response / the general form: what is $v_C(t)$ for an RC circuit driven by a constant source, in terms of its endpoints? ::@:: $v_C(t) = v_C(\infty) + [v_C(0) - v_C(\infty)]e^{-t/\tau}$, an exponential from the starting value towards the final one.
- step response / charging from rest: a capacitor with no initial charge is connected to a constant source $V_s$; what is $v_C(t)$? ::@:: $v_C(t) = V_s(1 - e^{-t/\tau})$, reaching $63.2\%$ of $V_s$ after one time constant and $99.3\%$ after five.
- step response / discharging: the source is removed from a capacitor charged to $V_0$; what is $v_C(t)$? ::@:: $v_C(t) = V_0e^{-t/\tau}$, the charge draining through the resistor with the same time constant.
- step response / the tangent: where does the tangent drawn to $v_C(t)$ at $t = 0$ meet the final value? ::@:: At $t = \tau$: the curve leaves at the rate $[v_C(\infty) - v_C(0)]/\tau$, so a straight line at that pace arrives after one time constant.

## frequency response

$\frac{\mathbf{V}_C}{\mathbf{V}_s} = \frac{1}{1 + j\omega\tau}$ has magnitude $1/\sqrt{1 + \omega^2\tau^2}$ and phase $-\tan^{-1}(\omega\tau)$. The magnitude starts at 1 and falls as the frequency rises; the phase runs from $0$ towards $-90^\circ$. At $\omega = 1/\tau$ the magnitude is $1/\sqrt{2}$, the $-3\text{ dB}$ point, and the phase is $-45^\circ$. Above that the magnitude falls as $1/(\omega\tau)$, or $-20\text{ dB}$ per decade. Low frequencies pass and high ones do not: a low-pass filter with its corner at $\omega = 1/\tau$, the same constant that set the transient ([sine wave](sine%20wave.md)).

---

Flashcards for this section are as follows:

- frequency response / the corner: at what frequency does the RC low-pass response reach $-3\text{ dB}$, and what is its phase there? ::@:: At $\omega = 1/\tau$, where the magnitude is $1/\sqrt{2}$ of the source and the phase is $-45^\circ$.
- frequency response / the roll-off: how fast does the magnitude of $\frac{1}{1 + j\omega\tau}$ fall above the corner, and where does the phase head? ::@:: As $1/(\omega\tau)$, which is $-20\text{ dB}$ per decade, with the phase turning towards $-90^\circ$.
