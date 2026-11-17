---
aliases:
  - AC power
  - ELEC 2400 AC power
  - ELEC2400 AC power
  - HKUST ELEC 2400 AC power
  - HKUST ELEC2400 AC power
  - complex power
  - power factor
  - reactive power
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/AC_power
  - language/in/English
---

# AC power

Under sinusoidal excitation the power itself swings in time, so one value cannot describe it ([electric power](electric%20power.md)). Three quantities share the job. The root-mean-square (RMS) value turns a sinusoid into a single number, the average power counts the net energy flow per cycle, and the complex power keeps the stored energy beside the spent energy.

---

Flashcards for this section are as follows:

- why one value cannot describe it: which quantities describe power in an alternating current (AC) circuit, and why is the instantaneous power not enough? ::@:: The root-mean-square (RMS) value, the average power, and the complex power; the instantaneous power swings through each cycle, so the swing is summarized instead of quoted instant by instant.

## root-mean-square value

The root-mean-square (RMS) value of a signal is the square root of the mean of its square. For the sinusoid $V_p\cos(\omega t + \theta)$ with $V_p \geq 0$ the definition gives $V_\text{rms} = \sqrt{\frac{1}{T}\int_t^{t+T} V_p^2\cos^2(\omega t + \theta)\,dt}$, and the integral of $\cos^2$ over a full cycle leaves half the squared amplitude behind, so $V_\text{rms} = \sqrt{V_p^2/2} = V_p/\sqrt{2} = 0.707V_p$.

An alternating voltage is quoted by its RMS value: the single-phase supply in Hong Kong reads $V_\text{rms} = 220\text{ V}$, which is the peak value $V_p = 311\text{ V}$ and the peak-to-peak value $V_{p\text{-}p} = 2V_p = 622\text{ V}$.

---

Flashcards for this section are as follows:

- root-mean-square value / definition: how is the root-mean-square (RMS) value of a signal defined? ::@:: The square root of the mean of the squared signal: square the signal, average it over a period, then take the square root.
- root-mean-square value / the sinusoid: what RMS value does the sinusoid $V_p\cos(\omega t + \theta)$ have, and how does it compare with the peak? ::@:: $V_\text{rms} = V_p/\sqrt{2} = 0.707V_p$, since the mean of $\cos^2$ over a cycle is one half.
- root-mean-square value / the supply: what do the $220\text{ V}$ of the Hong Kong single-phase supply mean, and what peak and peak-to-peak values follow? ::@:: $220\text{ V}$ is the root-mean-square (RMS) value: the peak is $V_p = \sqrt{2}\times220 = 311\text{ V}$ and the peak-to-peak value $2V_p = 622\text{ V}$.

## power quantities

### average power and the power factor

Averaging the product of a voltage $V_p\cos(\omega t + \theta)$ and a current $I_p\cos(\omega t + \varphi)$ over a cycle gives the average AC power $P_\text{ave} = \frac{V_pI_p}{2}\cos(\theta - \varphi) = V_\text{rms}I_\text{rms}\cos(\theta - \varphi)$. The factor $\cos(\theta - \varphi)$ is the power factor. It depends only on the phase difference between the voltage and the current, and equals one when the two are in step, shrinking as they pull apart.

A resistor keeps its voltage and current in step, $\theta = \varphi$, so it takes $P_\text{ave} = V_\text{rms}I_\text{rms} = I_\text{rms}^2R = V_\text{rms}^2/R = V_pI_p/2$: the direct current (DC) formulas, with root-mean-square values standing in for the constants. A capacitor or an inductor holds its voltage and current a quarter cycle apart, so $\cos(\theta - \varphi) = \cos(\pm90^\circ) = 0$: it consumes zero average power. What it stores over one half of the period comes back over the other half. A source delivers the negative of what its elements take.

---

Flashcards for this section are as follows:

- average power and the power factor / the average: what is the average AC power drawn by a voltage $V_p\cos(\omega t + \theta)$ and a current $I_p\cos(\omega t + \varphi)$? ::@:: $P_\text{ave} = \frac{V_pI_p}{2}\cos(\theta - \varphi) = V_\text{rms}I_\text{rms}\cos(\theta - \varphi)$.
- average power and the power factor / the power factor: what is the power factor of an alternating current (AC) circuit, and what fixes it? ::@:: $\cos(\theta - \varphi)$, the cosine of the phase difference between the voltage and the current; it is one when the two are in step and shrinks as they pull apart. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- average power and the power factor / the resistor: what average power does a resistor $R$ take under $V_\text{rms}$ and $I_\text{rms}$, and why is the power factor absent? ::@:: $P_\text{ave} = V_\text{rms}I_\text{rms} = I_\text{rms}^2R = V_\text{rms}^2/R$, since the resistor's voltage and current are in step and their power factor is one.
- average power and the power factor / storage elements: why do a capacitor and an inductor consume zero average power? ::@:: Their voltage and current sit a quarter cycle apart, so $\cos(\theta - \varphi) = \cos(\pm90^\circ) = 0$: energy stored in one half period is released in the other. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### instantaneous power

The average power and the reactive power both fall out of multiplying the two real waveforms. With $v(t) = V_p\cos\omega t$ and $i(t) = I_p\cos(\omega t - \phi)$, the identity $\cos A\cos B = \frac{1}{2}[\cos(A - B) + \cos(A + B)]$ gives $p(t) = v(t)i(t) = \frac{V_pI_p}{2}[\cos\phi + \cos(2\omega t - \phi)]$, one steady term and one ripple at twice the supply frequency. Expanding the ripple turns this into $p(t) = P_\text{ave}(1 + \cos2\omega t) + Q\sin2\omega t$, where $P_\text{ave} = V_\text{rms}I_\text{rms}\cos\phi$ and $Q = V_\text{rms}I_\text{rms}\sin\phi$.

$P_\text{ave}(1 + \cos2\omega t)$ stays between zero and twice the average, so energy moves towards the load only, in bursts, and none of it comes back. $Q\sin2\omega t$ swings either side of zero and gives back during each cycle exactly what it took, so a storage element spends nothing net. The current that carries it is still real: it heats the wire and counts against the rating of the source. A purely resistive load has no second term, and its power wave touches zero only at the zero crossings of the wave. With reactive parts present, the total falls below zero for part of every cycle, and during that part the fields return energy to the source.

---

Flashcards for this section are as follows:

- instantaneous power / the expansion: what is the instantaneous power $p(t)$ of a voltage $V_p\cos\omega t$ across an element carrying $I_p\cos(\omega t - \phi)$? ::@:: $p(t) = \frac{V_pI_p}{2}[\cos\phi + \cos(2\omega t - \phi)]$, which rearranges to $P_\text{ave}(1 + \cos2\omega t) + Q\sin2\omega t$ with $P_\text{ave} = V_\text{rms}I_\text{rms}\cos\phi$ and $Q = V_\text{rms}I_\text{rms}\sin\phi$.
- instantaneous power / the ripple frequency: at what frequency does the instantaneous power of a sinusoidally driven circuit ripple, and where does that frequency come from? ::@:: At $2\omega$, twice the supply frequency, because the product of two sinusoids at $\omega$ leaves a term at $2\omega$ beside the constant one. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- instantaneous power / the average term: how far does the term $P_\text{ave}(1 + \cos2\omega t)$ swing, and can it turn negative? ::@:: Between zero and twice the average power; it never turns negative, so energy travels towards the load only.
- instantaneous power / the reactive term: what average does $Q\sin2\omega t$ leave over a cycle, and what does its amplitude measure? ::@:: An average of zero, since its positive and negative parts cancel exactly; its amplitude is the reactive power $Q$, whose current still heats the wire without being spent.
- instantaneous power / the zero crossing: when does the instantaneous power of a circuit dip below zero? ::@:: When the load has a reactive part: a purely resistive load only touches zero at the crossings of the wave, while a reactive load lets the total go negative for part of each cycle as the fields return energy.

### complex power

Complex power packs the whole swing into one number, $\mathbf{S} = \frac{1}{2}\mathbf{V}\mathbf{I}^*$, built from the peak-value phasors with the current conjugated. Expanded with $\mathbf{V} = V_p\angle\theta$ and $\mathbf{I} = I_p\angle\varphi$ it comes to $\mathbf{S} = \frac{V_pI_p}{2}\cos(\theta - \varphi) + j\frac{V_pI_p}{2}\sin(\theta - \varphi) = V_\text{rms}I_\text{rms}\cos(\theta - \varphi) + jV_\text{rms}I_\text{rms}\sin(\theta - \varphi)$.

The conjugate turns the phase difference into the angle of the product. $\mathbf{V}\mathbf{I}^*$ carries the angle $\theta - \varphi$, by which the voltage leads the current, and the impedance carries the same one, since $\mathbf{Z} = \mathbf{V}/\mathbf{I}$ has angle $\theta - \varphi$ as well. A single angle therefore fixes both the power factor and the phase of the load.

The real part is the average power, $P_\text{ave} = \frac{1}{2}\operatorname{Re}(\mathbf{V}\mathbf{I}^*) = V_\text{rms}I_\text{rms}\cos(\theta - \varphi)$, the power an element actually spends, quoted in watts. The imaginary part is the reactive power, $Q = \frac{1}{2}\operatorname{Im}(\mathbf{V}\mathbf{I}^*) = V_\text{rms}I_\text{rms}\sin(\theta - \varphi)$: the power that reaches a storage element and comes back within the cycle without being spent. It is quoted in volt-amperes reactive (var), the same coherent unit as the volt-ampere under the name the IEC gives it. That magnitude, $|\mathbf{S}| = V_\text{rms}I_\text{rms}$, is the apparent power, quoted in volt-amperes (VA): what a source has to be rated to carry, at whatever phase the current arrives. The three satisfy the power triangle, $|\mathbf{S}|^2 = P_\text{ave}^2 + Q^2$ while $\tan(\theta - \varphi) = Q/P_\text{ave}$.

The sign of $Q$ names the load that produces it. A current lagging the voltage gives $\theta - \varphi > 0$ and a positive $Q$, the inductive case; a current leading gives a negative $Q$, the capacitive one. A pure resistor puts all of $\mathbf{S}$ on the real axis, while a pure capacitor or inductor puts all of it on the imaginary axis with magnitude $|\mathbf{S}| = V_\text{rms}I_\text{rms} = V_\text{rms}^2/|X| = I_\text{rms}^2|X|$.

Write the voltage and the current as rotating phasors, $\mathbf{v}(t) = V_pe^{j(\omega t + \theta)}$ and $\mathbf{i}(t) = I_pe^{j(\omega t + \varphi)}$. Both turn at $\omega$. Their plain product turns at $2\omega$ with the two angles added, and nothing steady comes out of it. Conjugate the current and it turns the other way, so multiplying cancels the $\omega t$ terms and leaves $V_pI_pe^{j(\theta - \varphi)}$, which depends on the phase difference alone. A phasor is shorthand for a real waveform, so this agrees with the time-domain product.

The factor in front of $\mathbf{S}$ follows from the size of the phasors. With amplitudes, $\mathbf{V} = V_p\angle\theta$ and $\mathbf{I} = I_p\angle\varphi$, the product $\mathbf{V}\mathbf{I}^*$ has magnitude $V_pI_p$, twice what an average power needs, and the factor $\frac{1}{2}$ brings it back down. That half belongs to the product of two sinusoids: $\cos(\omega t + \theta)\cos(\omega t + \varphi)$ expands into a term $\frac{1}{2}\cos(\theta - \varphi)$ plus one that averages to zero over a cycle.

Build the phasors on root-mean-square (RMS) values instead, $\mathbf{V} = V_\text{rms}\angle\theta$ and $\mathbf{I} = I_\text{rms}\angle\varphi$, and the product already carries $V_\text{rms}I_\text{rms} = V_pI_p/2$. Then $\mathbf{S} = \mathbf{V}\mathbf{I}^*$ takes no factor at all, and neither does any formula derived from it. The two conventions never mix inside one calculation: a factor $\frac{1}{2}$ beside RMS magnitudes halves a correct answer, and omitting it beside peak magnitudes doubles one. The phasors in these notes carry peak values throughout, so $\frac{1}{2}$ stays wherever complex power appears.

---

Flashcards for this section are as follows:

- complex power / the definition: how is complex power built from the voltage and current phasors, and what convention do those phasors follow? ::@:: $\mathbf{S} = \frac{1}{2}\mathbf{V}\mathbf{I}^*$, with the current conjugated; the phasors carry peak values, which is why the factor $\frac{1}{2}$ appears. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- complex power / the parts: what do the real and imaginary parts of $\mathbf{S} = \frac{1}{2}\mathbf{V}\mathbf{I}^*$ count, and in which units is each quoted? ::@:: The real part is the average power in watts and the imaginary part the reactive power, quoted in volt-amperes reactive (var).
- complex power / average power from phasors: what formula reads the average power straight off the phasors? ::@:: $P_\text{ave} = \frac{1}{2}\operatorname{Re}(\mathbf{V}\mathbf{I}^*)$, the real part of the complex power. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- complex power / why the current is conjugated: what angle does $\mathbf{V}\mathbf{I}^*$ carry, and which quantity of the load shares it? ::@:: The angle $\theta - \varphi$ by which the voltage leads the current; the impedance $\mathbf{Z} = \mathbf{V}/\mathbf{I}$ carries the same angle, so one angle fixes both the power factor and the phase of the load.
- complex power / apparent power and the power triangle: what is the apparent power of a load, and how does it relate to the average and reactive powers? ::@:: $|\mathbf{S}| = V_\text{rms}I_\text{rms}$, the magnitude of the complex power, quoted in volt-amperes (VA); $|\mathbf{S}|^2 = P_\text{ave}^2 + Q^2$, with $\tan(\theta - \varphi) = Q/P_\text{ave}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- complex power / the sign of the reactive power: what does the sign of $Q$ say about the load? ::@:: A current lagging the voltage gives a positive $Q$, the inductive load; a current leading the voltage gives a negative $Q$, the capacitive load.
- complex power / pure elements: what complex power does a pure resistor take, and what does a pure capacitor or inductor take? ::@:: The resistor takes a purely real $\mathbf{S}$ of $P_\text{ave} = V_\text{rms}^2/R$; a pure capacitor or inductor takes a purely imaginary $\mathbf{S}$ of magnitude $V_\text{rms}^2/|X| = I_\text{rms}^2|X|$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- complex power / where the factor of one half comes from: with phasors of amplitude $V_p$ and $I_p$, what fixes the $\frac{1}{2}$ in $\mathbf{S} = \frac{1}{2}\mathbf{V}\mathbf{I}^*$? ::@:: $\mathbf{V}\mathbf{I}^*$ has magnitude $V_pI_p$, twice the average power, and the mean of the product of two sinusoids is half the product of their amplitudes, so the factor restores the size.
- complex power / peak against root-mean-square phasors: what changes in $\mathbf{S}$ when the phasors are built on root-mean-square (RMS) values instead of amplitudes? ::@:: Nothing but the factor: with $\mathbf{V} = V_\text{rms}\angle\theta$ and $\mathbf{I} = I_\text{rms}\angle\varphi$, $\mathbf{S} = \mathbf{V}\mathbf{I}^*$ takes no $\frac{1}{2}$, since $V_\text{rms}I_\text{rms}$ already carries the half.
- complex power / mixing the conventions: what goes wrong when the two phasor conventions meet inside one calculation? ::@:: The answer doubles or halves: a $\frac{1}{2}$ kept beside root-mean-square (RMS) magnitudes halves a correct result, and one omitted beside amplitudes doubles it. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- complex power / the rotating view: with the rotating phasors $\mathbf{v}(t) = V_pe^{j(\omega t + \theta)}$ and $\mathbf{i}(t) = I_pe^{j(\omega t + \varphi)}$, why is the current conjugated rather than the voltage? ::@:: The plain product spins at $2\omega$ with the angles added and stays unsteady; conjugating the current reverses its rotation, the $\omega t$ terms cancel, and $V_pI_pe^{j(\theta - \varphi)}$ keeps the phase gap alone.

## power from circuit elements

### power from the impedance

Complex power follows from the impedance alone. With the current phasor $\mathbf{I} = I_p\angle\varphi$ and $Z = R + jX$, the voltage is $\mathbf{V} = \mathbf{I}Z$, so $\mathbf{S} = \frac{1}{2}\mathbf{V}\mathbf{I}^* = \frac{1}{2}|\mathbf{I}|^2Z = \frac{1}{2}I_p^2R + j\frac{1}{2}I_p^2X$. The real part counts the resistance and the imaginary part the reactance, so $P_\text{ave} = I_\text{rms}^2R$ and $Q = I_\text{rms}^2X$, while the apparent power is $|\mathbf{S}| = I_\text{rms}^2|Z| = I_\text{rms}V_\text{rms}$.

Read from the voltage side instead, $\mathbf{S} = \frac{1}{2}|\mathbf{V}|^2/Z^*$ carries a conjugate, and the average power becomes $\frac{1}{2}|\mathbf{V}|^2R/|Z|^2$. A large reactance then costs twice over: it raises $|Z|$, which lowers the current at a fixed voltage, and it lowers the fraction $R/|Z|$ of the apparent power that reaches the resistance.

---

Flashcards for this section are as follows:

- power from the impedance / complex power: with $Z = R + jX$ and current phasor $\mathbf{I}$, what is the complex power? ::@:: $\mathbf{S} = \frac{1}{2}|\mathbf{I}|^2Z = \frac{1}{2}I_p^2R + j\frac{1}{2}I_p^2X$, whose real part is the resistance's power and imaginary part the reactance's.
- power from the impedance / the two parts: how are the average and reactive powers read from the impedance and the current? ::@:: $P_\text{ave} = I_\text{rms}^2R$ and $Q = I_\text{rms}^2X$, with the apparent power $|\mathbf{S}| = I_\text{rms}^2|Z| = I_\text{rms}V_\text{rms}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- power from the impedance / from the voltage: what is the complex power when it is written with the voltage phasor and the impedance? ::@:: $\mathbf{S} = \frac{1}{2}|\mathbf{V}|^2/Z^*$, so the average power is $\frac{1}{2}|\mathbf{V}|^2R/|Z|^2$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- power from the impedance / the cost of reactance: why does a large reactance lower the average power twice over at a fixed voltage? ::@:: It raises $|Z|$, which lowers the current, and it lowers the fraction $R/|Z|$ of the apparent power that lands on the resistance. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### resistor formulas under phasors

$P_\text{ave} = \frac{V_\text{rms}^2}{R} = I_\text{rms}^2R = V_\text{rms}I_\text{rms}$ holds for a pure resistance, with root-mean-square values throughout. Written with peak values the same statements carry the half: $P_\text{ave} = \frac{V_p^2}{2R} = \frac{I_p^2R}{2}$.

For anything with a reactance the substitutions fail, and two of them fail quietly. $V_\text{rms}^2/|Z|$ is the apparent power rather than the average, and $V_\text{rms}^2/R$ is larger than either. A $3 + j4\ \Omega$ impedance across $10\text{ V}$ RMS shows how far: $|Z| = 5\ \Omega$ draws $2\text{ A}$ RMS, so the resistance takes $P_\text{ave} = 2^2\times3 = 12\text{ W}$, while $V_\text{rms}^2/|Z| = 20\text{ VA}$ and $V_\text{rms}^2/R = 33.3\text{ W}$ are both wrong, the second because the whole voltage does not sit across $R$.

---

Flashcards for this section are as follows:

- the resistor formulas under phasors / the formulas: which power formulas hold for a resistance, and with which values? ::@:: $P_\text{ave} = \frac{V_\text{rms}^2}{R} = I_\text{rms}^2R = V_\text{rms}I_\text{rms}$, all with root-mean-square values. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the resistor formulas under phasors / the peak forms: how do the same formulas read with peak values? ::@:: $P_\text{ave} = \frac{V_p^2}{2R} = \frac{I_p^2R}{2}$, each with the factor $\frac{1}{2}$ that the peak values leave out. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the resistor formulas under phasors / what fails: what do $V_\text{rms}^2/|Z|$ and $V_\text{rms}^2/R$ return for a reactive element? ::@:: $V_\text{rms}^2/|Z|$ is the apparent power, not the average, and $V_\text{rms}^2/R$ is larger still, because the whole voltage does not sit across the resistance.
- the resistor formulas under phasors / worked numbers: a $3 + j4\ \Omega$ impedance sits across $10\text{ V}$ RMS; what average power does it take? ::@:: $|Z| = 5\ \Omega$ draws $2\text{ A}$ RMS, so $P_\text{ave} = 2^2\times3 = 12\text{ W}$; $V_\text{rms}^2/|Z| = 20\text{ VA}$ and $V_\text{rms}^2/R = 33.3\text{ W}$ are not the answer.

### load at a lagging power factor

A load drawing $1\text{ kW}$ at a power factor of $0.8$ lagging from a $220\text{ V}$ RMS supply has $\cos\phi = 0.8$ and $\sin\phi = 0.6$. The apparent power is $S = P_\text{ave}/\cos\phi = 1.25\text{ kVA}$, the reactive power $Q = S\sin\phi = 750\text{ var}$, and the RMS current $I = S/V = 5.68\text{ A}$.

The same numbers name the element that would do the job: $R = P_\text{ave}/I^2 = 31\ \Omega$ in series with $X = Q/I^2 = 23.2\ \Omega$ of inductive reactance, positive because the current lags. Raising the power factor toward one shrinks $S$ and $I$ for the same $P_\text{ave}$, which is what a correction capacitor does.

---

Flashcards for this section are as follows:

- a load at a lagging power factor / apparent power: a load takes $1\text{ kW}$ at a power factor of $0.8$ from a $220\text{ V}$ RMS supply; what apparent power does the source carry? ::@:: $S = P_\text{ave}/\cos\phi = 1000/0.8 = 1.25\text{ kVA}$.
- a load at a lagging power factor / reactive power: with $\sin\phi = 0.6$, what reactive power goes with that load? ::@:: $Q = S\sin\phi = 1250\times0.6 = 750\text{ var}$, positive because the current lags.
- a load at a lagging power factor / the current: what RMS current does a $1.25\text{ kVA}$ load draw from a $220\text{ V}$ RMS supply? ::@:: $I = S/V = 1250/220 = 5.68\text{ A}$.
- a load at a lagging power factor / the equivalent element: what series resistance and reactance show the same behaviour? ::@:: $R = P_\text{ave}/I^2 = 31\ \Omega$ and $X = Q/I^2 = 23.2\ \Omega$, inductive because the current lags. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- a load at a lagging power factor / why correct it: what does raising the power factor toward one do at the same average power? ::@:: It shrinks the apparent power and the RMS current, so the source and the wiring carry less for the same energy delivered.

## conservation of alternating current power

Instantaneous power is conserved element by element, and so is its average, because the average of a sum is the sum of the averages. A balance that holds at every instant still holds once every term is averaged over a cycle. Complex power splits that single statement in two. The real parts balance among themselves and the imaginary parts balance among themselves, so the average power and the reactive power each close on their own.

A series circuit of $R = 2\ \Omega$ with an inductor and a capacitor, driven at $v(t) = 100\cos(1000t)\text{ V}$, sits at a net inductive reactance of $X_L - X_C = 1\ \Omega$. Its impedance is $2 + j1 = 2.236\angle26.57^\circ\ \Omega$, so $\mathbf{V} = 100\angle0^\circ\text{ V}$ drives $\mathbf{I} = 44.72\angle{-26.57^\circ}\text{ A}$, the current lagging the voltage.

The resistor takes $P_\text{ave} = \frac{1}{2}I_p^2R = \frac{44.72^2\times2}{2} = 2000\text{ W}$. The capacitor and the inductor sit a quarter cycle from their own current, so each takes zero average power. The source delivers $-\frac{100\times44.72}{2}\cos(0^\circ - (-26.57^\circ)) = -2000\text{ W}$, since $\cos(26.57^\circ) = 0.8944$ leaves $50\times44.72\times0.8944 = 2000\text{ W}$ for the resistor to spend. The average powers close.

The reactive account closes the same way, and the example carries reactive power even though neither storage element spends anything. The pair absorbs $\frac{1}{2}I_p^2(X_L - X_C) = \frac{44.72^2\times1}{2} = 1000\text{ VA}$, and the source supplies exactly that on top of the 2000 W: $\frac{100\times44.72}{2}\sin(26.57^\circ) = 1000\text{ VA}$. In complex form the whole account reads $\mathbf{S}_\text{source} = -\frac{1}{2}\mathbf{V}\mathbf{I}^* = -2236\angle26.57^\circ\text{ VA} = -2000 - j1000$, matched by $+2000\text{ W}$ in the resistor and $+j1000\text{ VA}$ in the two storage elements.

The sign says which way the energy goes: a negative average power marks an element that delivers rather than takes. That is why the source's term enters with a minus, and the account still closes with an element on the delivering side.

Dependent sources join the same accounting. In one network a $2\ \Omega$ resistor takes $0.5\text{ W}$, an independent source of $-4\text{ V}$ delivers $-1\text{ W}$, and a dependent source takes $0.5\text{ W}$, again summing to zero. A dependent source is an element like any other, and whatever it hands over is drawn somewhere else. The balance also checks a finished solution, since computing each element's average power from its own phasors exposes any term that does not close.

---

Flashcards for this section are as follows:

- conservation of alternating current power / the series network: in the circuit with $R = 2\ \Omega$, a net inductive reactance $X_L - X_C = 1\ \Omega$, $\mathbf{V} = 100\angle0^\circ\text{ V}$, and $\mathbf{I} = 44.72\angle{-26.57^\circ}\text{ A}$, what average power does each element take? ::@:: The resistor takes $\frac{1}{2}I_p^2R = 2000\text{ W}$, the capacitor and the inductor zero, and the source delivers $-2000\text{ W}$, so the average powers close.
- conservation of alternating current power / the source term: how is the average power delivered by the source in that circuit computed? ::@:: $P_\text{ave} = -\frac{V_pI_p}{2}\cos(\theta - \varphi) = -\frac{100\times44.72}{2}\cos(26.57^\circ) = -2000\text{ W}$, the minus mark because the source delivers rather than takes. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- conservation of alternating current power / the reactive books: in that same circuit, what reactive power does each element take, though neither storage element spends average power? ::@:: The capacitor and the inductor absorb $\frac{1}{2}I_p^2(X_L - X_C) = 1000\text{ VA}$ between them while spending nothing, and the source supplies $\frac{100\times44.72}{2}\sin(26.57^\circ) = 1000\text{ VA}$ on top of its 2000 W. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- conservation of alternating current power / the complex form: how does the whole account of that circuit read as one complex-power equation? ::@:: $\mathbf{S}_\text{source} = -\frac{1}{2}\mathbf{V}\mathbf{I}^* = -2236\angle26.57^\circ\text{ VA} = -2000 - j1000$, matched by $+2000\text{ W}$ in the resistor and $+j1000\text{ VA}$ in the storage elements. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- conservation of alternating current power / why the average balances: why does average power balance element by element as the instantaneous power does? ::@:: The average of a sum is the sum of the averages, so a balance that holds at every instant still holds once every term is averaged over a cycle.
- conservation of alternating current power / the two balances: what does complex power turn the conservation of power into? ::@:: Two balances instead of one: the real parts, the average power, close among themselves, and so do the imaginary parts, the reactive power.
- conservation of alternating current power / the sign: what does a negative average power say about an element, and how does that show in the source's term? ::@:: The element delivers rather than takes; the source's own average power carries a minus mark for that reason.
- conservation of alternating current power / with a dependent source: a $2\ \Omega$ resistor takes $0.5\text{ W}$, an independent source of $-4\text{ V}$ delivers $-1\text{ W}$, and a dependent source takes $0.5\text{ W}$; what does the total come to? ::@:: $0.5 - 1 + 0.5 = 0$: dependent sources take part in the same conservation as every other element.
- conservation of alternating current power / as a check: how does the conservation of average power serve as a check on a finished solution? ::@:: Compute each element's average power from its own phasors and add them up; a total that does not close marks an error in one of the terms.
