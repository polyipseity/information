---
aliases:
  - ELEC 2400 inductor
  - ELEC2400 inductor
  - HKUST ELEC 2400 inductor
  - HKUST ELEC2400 inductor
  - coil
  - inductance
  - inductor
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/inductor
  - language/in/English
---

# inductor

An inductor is the circuit element that stores energy in a magnetic field, and a coil of wire makes one. The current $i_\ell(t)$ through the coil sets up a magnetic flux linkage $\phi(t) = L\,i_\ell(t)$, with $L$ the inductance, measured in henrys (H).

On a circuit diagram the coil is a run of arcs. The analysis marks one end $+$ and the other $-$, draws the current arrow, and writes the voltage $v_\ell(t)$, following the same reference-direction convention as any two-terminal element.

---

Flashcards for this section are as follows:

- the inductor symbol: which reference directions does the drawing fix? <p> ![inductor symbol: a coil in a vertical branch, with the current arrow i of ell of t into the terminal marked plus and the plus and minus marks of the voltage v of ell of t](attachments/symbol_inductor.svg) ::@:: The current arrow $i_\ell(t)$ points into the terminal marked $+$, and the marks fix the sign of the voltage $v_\ell(t)$ across the inductance $L$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- draw an inductance L on a circuit diagram: what marks come with it? ::@:: A coil in the branch, labelled $L$, with the current arrow $i_\ell(t)$ into the terminal marked $+$ and the voltage $v_\ell(t)$ written across the coil. <p> ![inductor symbol: a coil in a vertical branch, with the current arrow i of ell of t into the terminal marked plus and the plus and minus marks of the voltage v of ell of t](attachments/symbol_inductor.svg) <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- what an inductor is: which circuit element stores energy in a magnetic field, and what physical form does it take? ::@:: An inductor, built as a coil of wire; current through the coil stores energy in the magnetic field the coil sets up.
- flux linkage: how does the magnetic flux linkage of an inductor relate to the current through it, and in what units is the constant measured? ::@:: $\phi(t) = L\,i_\ell(t)$, with $L$ the inductance measured in henrys (H). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the circuit symbol: how is an inductor drawn on a circuit diagram? ::@:: A run of arcs (a coil), with the usual $+$ and $-$ marks and current arrow chosen as reference directions for the analysis. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## voltage and current

The voltage across an inductor tracks how fast its current changes, $v_\ell(t) = L\,di_\ell(t)/dt$. Read the other way, $i_\ell(t) = i_\ell(0) + \frac{1}{L}\int_0^t v_\ell(\tau)\,d\tau$.

Three consequences follow, and each has a capacitor counterpart with voltage and current exchanged. A constant current gives no voltage, so an inductor carries direct current (DC) as a short circuit once its current settles. A steadily ramping current gives a constant voltage. The current also cannot jump: a jump would demand infinite voltage.

An inductance of $L = 2\text{ H}$ carrying $i_\ell(t) = 2t\text{ A}$ develops $v_\ell(t) = L\,di_\ell/dt = 2\times2 = 4\text{ V}$ and holds the flux linkage $\phi(t) = L\,i_\ell(t) = 4t\text{ Wb}$.

![inductor symbol: a coil in a vertical branch, with the current arrow i of ell of t into the terminal marked plus and the plus and minus marks of the voltage v of ell of t](attachments/symbol_inductor.svg)

---

Flashcards for this section are as follows:

- voltage and current / defining relation: how does the voltage across an inductor relate to the current through it? ::@:: $v_\ell(t) = L\,di_\ell(t)/dt$: the voltage is the inductance times the rate of change of the current. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- voltage and current / integral form: the voltage across an inductor is $v_\ell(t)$; how is the current recovered from it? ::@:: $i_\ell(t) = i_\ell(0) + \frac{1}{L}\int_0^t v_\ell(\tau)\,d\tau$, fixed up to its initial current.
- voltage and current / direct current (DC): why does an inductor behave as a short circuit under a constant current? ::@:: $v_\ell = L\,di_\ell/dt$ vanishes once the current stops changing, so no voltage drops across it. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- voltage and current / ramp example: a $2\text{ H}$ inductor carries $i_\ell(t) = 2t\text{ A}$; what voltage develops across it, and what flux linkage does it hold? ::@:: $v_\ell(t) = L\,di_\ell/dt = 2\times2 = 4\text{ V}$, and $\phi(t) = L\,i_\ell(t) = 4t\text{ Wb}$.
- voltage and current / continuity: can the current through an inductor jump discontinuously? ::@:: No: a jump would need $di_\ell/dt$, and hence the voltage, to be infinite. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## stored energy

Establishing the current takes work against the voltage the inductor develops, and that work is held as energy in the magnetic field. The power flowing in is $p = v_\ell i_\ell = L i_\ell\frac{di_\ell}{dt}$, the derivative of $\frac{1}{2}Li_\ell^2$. Integrating that power while the current climbs from zero to $I$ adds up the work, $E_\ell = \int_0^I Li\,di = \frac{1}{2}LI^2$, and $\frac{1}{2}\phi I = \frac{\phi^2}{2L}$ restates the result in terms of the flux linkage.

---

Flashcards for this section are as follows:

- stored energy / formula: what is the energy stored in an inductor carrying the current $I$, and where does it sit? ::@:: $E_\ell = \frac{1}{2}LI^2$, stored in the magnetic field of the coil.
- stored energy / the derivation: starting from the power into an inductor, how is $E_\ell = \frac{1}{2}LI^2$ derived? ::@:: $p = v_\ell i_\ell = L i_\ell\frac{di_\ell}{dt} = \frac{d}{dt}\left(\frac{1}{2}Li_\ell^2\right)$, so integrating from zero current to $I$ gives $E_\ell = \int_0^I Li\,di = \frac{1}{2}LI^2$.
- stored energy / ramping example: an inductor of $L = 2\text{ H}$ carries $i_\ell(t) = 2t\text{ A}$; what energy does it store at time $t$? ::@:: $E_\ell(t) = \frac{1}{2}Li_\ell(t)^2 = \frac{1}{2}\times2\times(2t)^2 = 4t^2\text{ J}$.

## inductance of a coil

A long coil wound densely on a core of permeability $\mu$ has $L = \mu N^2A/l$. The inductance grows with the square of the number of turns $N$ and with the cross-sectional area $A$ of the coil, and it shrinks with the length $l$ of the winding. The permeability of free space is $\mu_0 = 4\pi\times10^{-7}\text{ H/m}$, and a ferromagnetic core raises $\mu$ far above it.

---

Flashcards for this section are as follows:

- inductance of a coil / formula: in terms of the number of turns, the cross-sectional area, the winding length, and the permeability, what is the inductance of a long coil? ::@:: $L = \mu N^2A/l$, with $\mu_0 = 4\pi\times10^{-7}\text{ H/m}$ the permeability of free space. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- inductance of a coil / turns: the number of turns on a coil is doubled with all else fixed; how does the inductance change? ::@:: It grows fourfold, since $L$ is proportional to $N^2$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- inductance of a coil / core: how does a ferromagnetic core compare with an air core for the same coil? ::@:: Its far larger permeability raises the inductance in proportion, $L = \mu N^2A/l$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## series and parallel connections

Inductors in series share one current and their voltages add, so the inductances add: $L_\text{eq} = L_1 + L_2 + \dots + L_N$.

Join the two windings end to end and they become one longer coil. At a fixed number of turns per unit length the turns and the length grow together, and $L = \mu N^2A/l$ with $N = nl$ reduces to $\mu n^2Al$. The inductance grows with the length, so the inductances add.

Inductors in parallel share the two nodes and their currents add, which inverts the rule: $\frac{1}{L_\text{eq}} = \frac{1}{L_1} + \frac{1}{L_2} + \dots + \frac{1}{L_N}$, with the shorthand $L_1\|L_2 = \frac{L_1L_2}{L_1+L_2}$.

Set the two windings side by side across the same pair of terminals and they share one voltage while the current splits between them. Each winding then carries only its share of the current the pair draws. For the same voltage the pair takes more current than either winding would, and it behaves as a single winding of smaller inductance.

The pair of rules is the mirror image of the capacitor's: what capacitors add in parallel, inductors add in series. The geometric reading exchanges with it. A capacitor merges across its plates with the gap fixed, so the area grows, while an inductor merges along its winding with the area fixed, so the length grows.

---

Flashcards for this section are as follows:

- series and parallel connections / series rule: how does the equivalent inductance of inductors connected in series relate to the individual inductances? ::@:: The inductances add, $L_\text{eq} = L_1 + L_2 + \dots + L_N$, because they share one current and their voltages add. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- series and parallel connections / the series merge: two windings are joined end to end into one longer coil; which part of the geometry changes, and what follows? ::@:: The length and the turns grow together at a fixed number of turns per unit length. $L = \mu n^2Al$ grows with the length, so the inductances add. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- series and parallel connections / parallel rule: how does the equivalent inductance of inductors connected in parallel relate to the individual inductances? ::@:: The reciprocals add, $\frac{1}{L_\text{eq}} = \frac{1}{L_1} + \frac{1}{L_2} + \dots + \frac{1}{L_N}$, because they share the two nodes and their currents add. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- series and parallel connections / the parallel merge: two windings sit side by side across the same two terminals; why is the pair less inductive than either winding? ::@:: They share one voltage and split the current, so each carries only part of it. The pair takes more current for the same voltage, and the reciprocals add.
- series and parallel connections / two-inductor shorthand: what does $L_1\|L_2$ evaluate to? ::@:: $L_1\|L_2 = \frac{L_1L_2}{L_1+L_2}$, the same $a\|b = \frac{ab}{a+b}$ arithmetic the capacitor rules use.
- series and parallel connections / duality with capacitors: how do the inductor rules line up with the capacitor rules? ::@:: They swap ends: capacitors add in parallel and invert in series, while inductors add in series and invert in parallel.

## response to a sinusoidal voltage

An inductance $L$ driven by $v_\ell(t) = V_p\cos\omega t$ draws $i_\ell(t) = \frac{1}{L}\int v_\ell\,dt = \frac{V_p}{\omega L}\sin\omega t = \frac{V_p}{\omega L}\cos(\omega t - \pi/2)$. The current is a sinusoid of the same frequency whose phase lags the voltage by $\pi/2$, a quarter cycle or $90^\circ$.

The current amplitude $V_p/\omega L$ falls as the frequency rises. At a low frequency the current is large and the inductor behaves as a short circuit; at a high frequency it is negligible and the inductor behaves as an open circuit. A $10\ \mu\text{H}$ inductor across a $10\text{ V}$ amplitude source draws $i_\ell(t) = +159\sin(2\pi\cdot1\text{k}t)\text{ A}$ at $1\text{ kHz}$, $+15.9\sin(2\pi\cdot10\text{k}t)\text{ A}$ at $10\text{ kHz}$, and $+1.59\sin(2\pi\cdot100\text{k}t)\text{ A}$ at $100\text{ kHz}$.

The voltage and the current are a quarter cycle out of step, so their product averages to zero over a cycle, and an inductor consumes no average power. It stores energy over one half of the cycle and releases it over the other half ([AC power](AC%20power.md)).

---

Flashcards for this section are as follows:

- response to a sinusoidal voltage / lag: an inductor with $v_\ell(t) = V_p\cos\omega t$ across it; what does its current look like, and how does its phase compare with the voltage's? ::@:: $i_\ell(t) = \frac{V_p}{\omega L}\cos(\omega t - \pi/2)$, a sinusoid of the same frequency lagging the voltage by $90^\circ$.
- response to a sinusoidal voltage / direction of the lag: does the inductor current lead or lag its voltage, and by how much? ::@:: It lags, by $\pi/2$ radians, that is $90^\circ$ or a quarter cycle. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- response to a sinusoidal voltage / frequency trend: under a fixed sinusoidal voltage the current amplitude falls with frequency; what does the inductor look like at the two extremes? ::@:: A short circuit at low frequency and an open circuit at high frequency.
- response to a sinusoidal voltage / worked amplitudes: a $10\ \mu\text{H}$ inductor carries a $10\text{ V}$ amplitude sinusoid at $1\text{ kHz}$, $10\text{ kHz}$, and $100\text{ kHz}$; what current flows at each frequency? ::@:: $i_\ell(t) = +159\sin(2\pi\cdot1\text{k}t)\text{ A}$, $+15.9\sin(2\pi\cdot10\text{k}t)\text{ A}$, and $+1.59\sin(2\pi\cdot100\text{k}t)\text{ A}$ respectively.
- response to a sinusoidal voltage / average power: why does an ideal inductor consume no average power under sinusoidal excitation? ::@:: Its current lags its voltage by $90^\circ$, so the product $v(t)i(t)$ averages to zero over a cycle: energy is stored in one half cycle and released in the other. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## why the frequency ends open and closed

The impedance of an inductor is $Z_L = j\omega L$, and its magnitude $|Z_L| = \omega L$ carries the whole frequency story. Let $\omega \to 0$: the magnitude falls to zero, so at any finite current the voltage across the inductor falls to zero, which is what a short circuit does. Let $\omega \to \infty$: the magnitude rises without bound, so at any finite voltage the current $\mathbf{I}_L = \mathbf{V}_L/Z_L$ falls to zero, which is what an open circuit does.

The time-domain amplitude says the same thing. An inductor driven by $V_p\cos\omega t$ carries a current of amplitude $V_p/(\omega L)$: a slowly varying voltage leaves the current plenty of time to build, while a fast one never lets it get far. A capacitor's $Z_C = 1/(j\omega C)$ runs the other way, so the two elements swap their extremes ([Capacitor](capacitor.md)).

---

Flashcards for this section are as follows:

- why the frequency ends open and closed / low frequency: with $Z_L = j\omega L$, what does an inductor become as $\omega \to 0$? ::@:: A short circuit: $|Z_L| = \omega L$ falls to zero, so the voltage across it falls to zero at a finite current.
- why the frequency ends open and closed / high frequency: with $Z_L = j\omega L$, what does an inductor become as $\omega \to \infty$? ::@:: An open circuit: $|Z_L| = \omega L$ grows without bound, so the current falls to zero at a finite voltage.
- why the frequency ends open and closed / the time-domain cross-check: which time-domain amplitude carries both limits, and how does it move? ::@:: The current amplitude $V_p/(\omega L)$: it grows without bound as $\omega \to 0$ and vanishes as $\omega \to \infty$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why the frequency ends open and closed / the capacitor contrast: how does a capacitor's $Z_C = 1/(j\omega C)$ differ at the two extremes? ::@:: It runs the other way: $|Z_C| = 1/(\omega C)$ grows without bound at low frequency, so the capacitor is an open there and a short at high frequency.
