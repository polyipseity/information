---
aliases:
  - angle notation
  - angle notations
  - complex amplitude
  - complex amplitudes
  - complexor
  - complexors
  - phase vector
  - phase vectors
  - phasor
  - phasor diagram
  - phasor diagrams
  - phasor notation
  - phasor notations
  - phasors
  - sinor
  - sinors
tags:
  - flashcard/active/general/eng/phasor
  - language/in/English
---

# phasor

- For other uses, see [Phasor \(disambiguation\)](phasor%20(disambiguation).md).
- Not to be confused with {@{[phaser](phaser%20(disambiguation).md)}@}.
- {@{"Complex amplitude"}@} redirects here. For {@{the quantum-mechanical concept}@}, see {@{[Complex probability amplitude](complex%20probability%20amplitude.md)}@}.

> {@{![An example of series [RLC circuit](RLC%20circuit.md) and respective __phasor diagram__ for a specific _ω_.](../../archives/Wikimedia%20Commons/Wykres%20wektorowy%20by%20Zureks.svg)}@}
>
> An example of {@{series [RLC circuit](RLC%20circuit.md)}@} and respective {@{__phasor diagram__ for a specific _ω_}@}. {@{The arrows in the upper diagram}@} are {@{phasors}@}, drawn in {@{a phasor diagram \([complex plane](complex%20plane.md) without axis shown\)}@}, which must not be {@{confused with the arrows in the lower diagram}@}, which are {@{the reference polarity for the [voltages](voltage.md)}@} and {@{the reference direction for the [current](electric%20current.md)}@}.

In {@{[physics](physics.md) and [engineering](engineering.md)}@}, {@{a __phasor__}@} \({@{a [portmanteau](portmanteau.md) of __phase vector__}@}<sup>[\[1\]](#^ref-1)</sup><sup>[\[2\]](#^ref-2)</sup>\) is {@{a [complex number](complex%20number.md) representing a [sinusoidal function](sine%20wave.md)}@} whose {@{[amplitude](amplitude.md) _A_ and [initial phase](phase%20(waves).md) _θ_ are [time-invariant](time-invariant%20system.md) and whose [angular frequency](angular%20frequency.md) _ω_ is fixed}@}. It is related to {@{a more general concept called [analytic representation](analytic%20signal.md)}@},<sup>[\[3\]](#^ref-3)</sup> which {@{decomposes a sinusoid}@} into {@{the product of a complex constant and a factor depending on time and frequency}@}. {@{The complex constant}@}, which {@{depends on amplitude and phase}@}, is known as {@{a __phasor__, or __complex amplitude__,<sup>[\[4\]](#^ref-4)</sup><sup>[\[5\]](#^ref-5)</sup> and \(in older texts\) __sinor__<sup>[\[6\]](#^ref-6)</sup> or even __complexor__}@}.<sup>[\[6\]](#^ref-6)</sup>

{@{A common application}@} is in {@{the steady-state analysis of an [electrical network](electrical%20network.md)}@} powered by {@{[time varying current](alternating%20current.md)}@} where {@{all signals are assumed to be sinusoidal with a common frequency}@}. {@{Phasor representation}@} allows the analyst to {@{represent the amplitude and phase of the signal using a single complex number}@}. {@{The only difference in their analytic representations}@} is {@{the complex amplitude \(phasor\)}@}. {@{A linear combination of such functions}@} can be represented as {@{a linear combination of phasors}@} \(known as {@{__phasor arithmetic__ or __phasor algebra<sup>[\[7\]](#^ref-7)</sup><sup>:&hairsp;53&hairsp;</sup>__}@}\) and {@{the time/frequency dependent factor}@} that {@{they all have in common}@}.

{@{The origin of the term phasor}@} rightfully suggests that {@{a \(diagrammatic\) calculus somewhat similar to that possible for [vectors](Euclidean%20vector.md)}@} is {@{possible for phasors as well}@}.<sup>[\[6\]](#^ref-6)</sup> {@{An important additional feature}@} of {@{the phasor transform}@} is that {@{[differentiation](derivative.md) and [integration](integral.md)}@} of {@{sinusoidal signals \(having constant amplitude, period and phase\)}@} corresponds to {@{simple [algebraic operations](algebraic%20operation.md) on the phasors}@}; {@{the phasor transform}@} thus allows {@{the [analysis](network%20analysis%20(electrical%20circuits).md) \(calculation\) of the [AC](alternating%20current.md) [steady state](steady%20state%20(electronics).md) of [RLC circuits](RLC%20circuit.md)}@} by {@{solving simple [algebraic equations](algebraic%20equation.md) \(albeit with complex coefficients\) in the phasor domain}@} instead of {@{solving [differential equations](differential%20equation.md) \(with [real](real%20number.md) coefficients\) in the time domain}@}.<sup>[\[8\]](#^ref-8)</sup><sup>[\[9\]](#^ref-9)</sup><sup>[\[a\]](#^ref-a)</sup> {@{The originator of the phasor transform}@} was {@{[Charles Proteus Steinmetz](Charles%20Proteus%20Steinmetz.md) working at [General Electric](General%20Electric.md) in the late 19th century}@}.<sup>[\[10\]](#^ref-10)</sup><sup>[\[11\]](#^ref-11)</sup> He got his inspiration from {@{[Oliver Heaviside](Oliver%20Heaviside.md)}@}. {@{Heaviside's operational calculus}@} was {@{modified so that the variable p becomes jω}@}. {@{The complex number j}@} has {@{simple meaning: phase shift}@}.<sup>[\[12\]](#^ref-12)</sup>

Glossing over {@{some mathematical details}@}, {@{the phasor transform}@} can also be seen as {@{a particular case of the [Laplace transform](Laplace%20transform.md)}@} \(limited to {@{a single frequency}@}\), which, in contrast to {@{phasor representation}@}, can be used to {@{\(simultaneously\) derive the [transient response](transient%20response.md) of an RLC circuit}@}.<sup>[\[9\]](#^ref-9)</sup><sup>[\[11\]](#^ref-11)</sup> However, {@{the Laplace transform}@} is {@{mathematically more difficult to apply}@} and {@{the effort may be unjustified if only steady state analysis is required}@}.<sup>[\[11\]](#^ref-11)</sup>

## notation

- See also: ::@:: [Vector notation](vector%20notation.md)

> {@{![Fig 2. When function $A\cdot e^{i(\omega t+\theta )}$ is depicted in the complex plane, the vector formed by its [imaginary and real parts](complex%20number.md) rotates around the origin.](../../archives/Wikimedia%20Commons/Unfasor.gif)}@}
>
> Fig 2. When {@{function $A\cdot e^{i(\omega t+\theta )}$}@} is {@{depicted in the complex plane}@}, {@{the vector formed by its [imaginary and real parts](complex%20number.md)}@} {@{rotates around the origin}@}. {@{Its magnitude}@} is {@{_A_}@}, and it completes {@{one cycle every 2<!-- markdown separator -->_π_<!-- markdown separator -->/ω}@}. {@{_θ_}@} is {@{the angle it forms with the positive real axis at _t_ = 0}@} \(and at {@{_t_ = _n_ 2<!-- markdown separator -->_π_<!-- markdown separator -->/<!-- markdown separator -->_ω_ for all [integer](integer.md) values of _n_}@}\).

{@{__Phasor notation__ \(also known as __angle notation__\)}@} is {@{a [mathematical notation](mathematical%20notation.md) used in [electronics engineering](electronics%20engineering.md) and [electrical engineering](electrical%20engineering.md)}@}. {@{A vector whose [polar coordinates](polar%20coordinates.md#complex%20numbers)}@} are {@{magnitude $A$ and [angle](angle.md) $\theta$}@} is written {@{$A\angle \theta$}@}.<sup>[\[13\]](#^ref-13)</sup> {@{$1\angle \theta$}@} can represent either {@{the [vector](Euclidean%20vector.md) $(\cos \theta ,\,\sin \theta )$}@} or {@{the [complex number](complex%20number.md) $\cos \theta +i\sin \theta =e^{i\theta }$}@}, according to {@{[Euler's formula](Euler's%20formula.md) with $i^{2}=-1$}@}, both of which have {@{[magnitudes](magnitude%20(mathematics).md) of 1}@}.

{@{The angle}@} may be {@{stated in [degrees](degree%20(angle).md)}@} with {@{an implied conversion from degrees to [radians](radian.md)}@}. For example {@{$1\angle 90$}@} would be assumed to be {@{$1\angle 90^{\circ }$}@}, which is {@{the vector $(0,\,1)$ or the number $e^{i\pi /2}=i$}@}.

{@{Multiplication and division of complex numbers}@} become {@{straight forward through the phasor notation}@}. Given {@{the vectors $v_{1}=A_{1}\angle \theta _{1}$ and $v_{2}=A_{2}\angle \theta _{2}$}@}, the following is true:<sup>[\[14\]](#^ref-14)</sup>

- \(annotation: multiplication using phasor notation\) ::@:: $v_{1}\cdot v_{2}=A_{1}\cdot A_{2}\angle (\theta _{1}+\theta _{2})$,
- \(annotation: division using phasor notation\) ::@:: ${\frac {v_{1} }{v_{2} } }={\frac {A_{1} }{A_{2} } }\angle (\theta _{1}-\theta _{2})$.

## definition

{@{A real-valued sinusoid}@} with {@{constant amplitude, frequency, and phase}@} has the form: {@{$$A\cos(\omega t+\theta ),$$}@} where {@{only parameter $t$ is time-variant}@}. {@{The inclusion of an [imaginary component](imaginary%20part.md)}@}: {@{$$i\cdot A\sin(\omega t+\theta )$$}@} gives it, in accordance with {@{[Euler's formula](Euler's%20formula.md}@}), {@{the factoring property}@} described in the lead paragraph: {@{$$A\cos(\omega t+\theta )+i\cdot A\sin(\omega t+\theta )=Ae^{i(\omega t+\theta )}=Ae^{i\theta }\cdot e^{i\omega t},$$}@} whose {@{real part is the original sinusoid}@}. {@{The benefit of the complex representation}@} is that {@{linear operations with other complex representations}@} produces {@{a complex result}@} whose real part {@{reflects the same linear operations with the real parts of the other complex sinusoids}@}. Furthermore, {@{all the mathematics can be done}@} with {@{just the phasors $Ae^{i\theta }$}@}, and {@{the common factor $e^{i\omega t}$}@} is {@{reinserted prior to the real part of the result}@}.

{@{The function $Ae^{i(\omega t+\theta )}$}@} is {@{an _[analytic representation](analytic%20representation.md)_ of $A\cos(\omega t+\theta )$}@}. Figure 2 depicts it as {@{a rotating vector in the complex plane}@}. It is sometimes convenient to {@{refer to the entire function}@} as {@{a _phasor_,<sup>[\[15\]](#^ref-15)</sup> as we do in the next section}@}.

## arithmetic

- See also: ::@:: [Complex number § Relations and operations](complex%20number.md#relations%20and%20operations)

### multiplication by a constant \(scalar\)

{@{Multiplication of the phasor $Ae^{i\theta }e^{i\omega t}$}@} by {@{a complex constant, $Be^{i\phi }$}@}, produces {@{another phasor}@}. That means {@{its only effect}@} is to {@{change the amplitude and phase of the underlying sinusoid}@}: {@{$${\begin{aligned}&\operatorname {Re} \left(\left(Ae^{i\theta }\cdot Be^{i\phi }\right)\cdot e^{i\omega t}\right)\\={}&\operatorname {Re} \left(\left(ABe^{i(\theta +\phi )}\right)\cdot e^{i\omega t}\right)\\={}&AB\cos(\omega t+(\theta +\phi )).\end{aligned} }$$}@}

In {@{electronics}@}, {@{$Be^{i\phi }$}@} would {@{represent an [impedance](electrical%20impedance.md)}@}, which is {@{independent of time}@}. In particular it is {@{_not_ the shorthand notation for another phasor}@}. {@{Multiplying a phasor current by an impedance}@} produces {@{a phasor voltage}@}. But {@{the product of two phasors \(or squaring a phasor\)}@} would {@{represent the product of two sinusoids}@}, which is {@{a non-linear operation that produces new frequency components}@}. {@{Phasor notation}@} can {@{only represent systems with one frequency}@}, such as {@{a linear system stimulated by a sinusoid}@}.

### addition

> {@{![The sum of phasors as addition of rotating vectors](../../archives/Wikimedia%20Commons/Sumafasores.gif)}@}
>
> {@{The sum of phasors}@} as {@{addition of rotating vectors}@}

{@{The sum of multiple phasors}@} produces {@{another phasor}@}. That is because {@{the sum of sinusoids with the same frequency}@} is {@{also a sinusoid with that frequency}@}: {@{$${\begin{aligned}&A_{1}\cos(\omega t+\theta _{1})+A_{2}\cos(\omega t+\theta _{2})\\[3pt]={}&\operatorname {Re} \left(A_{1}e^{i\theta _{1} }e^{i\omega t}\right)+\operatorname {Re} \left(A_{2}e^{i\theta _{2} }e^{i\omega t}\right)\\[3pt]={}&\operatorname {Re} \left(A_{1}e^{i\theta _{1} }e^{i\omega t}+A_{2}e^{i\theta _{2} }e^{i\omega t}\right)\\[3pt]={}&\operatorname {Re} \left(\left(A_{1}e^{i\theta _{1} }+A_{2}e^{i\theta _{2} }\right)e^{i\omega t}\right)\\[3pt]={}&\operatorname {Re} \left(\left(A_{3}e^{i\theta _{3} }\right)e^{i\omega t}\right)\\[3pt]={}&A_{3}\cos(\omega t+\theta _{3}),\end{aligned} }$$}@} where: {@{$$A_{3}^{2}=(A_{1}\cos \theta _{1}+A_{2}\cos \theta _{2})^{2}+(A_{1}\sin \theta _{1}+A_{2}\sin \theta _{2})^{2},$$}@} and, if we take {@{$\theta _{3}\in \left[-{\frac {\pi }{2} },{\frac {3\pi }{2} }\right]$}@}, then $\theta _{3}$ is: \(annotation: 3 cases: {@{depending on the sign of $A_1 \cos \theta_1 + A_2 \cos \theta_2$}@}\)

- $\operatorname {sgn}(A_{1}\sin(\theta _{1})+A_{2}\sin(\theta _{2}))\cdot {\frac {\pi }{2} }$, ::@:: if $A_{1}\cos \theta _{1}+A_{2}\cos \theta _{2}=0$, with $\operatorname {sgn}$ the [signum function](signum%20function.md);
- $\arctan \left({\frac {A_{1}\sin \theta _{1}+A_{2}\sin \theta _{2} }{A_{1}\cos \theta _{1}+A_{2}\cos \theta _{2} } }\right)$, ::@:: if $A_{1}\cos \theta _{1}+A_{2}\cos \theta _{2}>0$;
- $\pi +\arctan \left({\frac {A_{1}\sin \theta _{1}+A_{2}\sin \theta _{2} }{A_{1}\cos \theta _{1}+A_{2}\cos \theta _{2} } }\right)$, ::@:: if $A_{1}\cos \theta _{1}+A_{2}\cos \theta _{2}<0$.

or, via {@{the [law of cosines](law%20of%20cosines.md) on the [complex plane](complex%20plane.md)}@} \(or {@{the [trigonometric identity for angle differences](trigonometric%20identity.md#angle%20sum%20and%20difference%20identities)}@}\): {@{$$A_{3}^{2}=A_{1}^{2}+A_{2}^{2}-2A_{1}A_{2}\cos(180^{\circ }-\Delta \theta )=A_{1}^{2}+A_{2}^{2}+2A_{1}A_{2}\cos(\Delta \theta ),$$}@} where {@{$\Delta \theta =\theta _{1}-\theta _{2}$}@}.

{@{A key point}@} is that {@{_A_<sub>3</sub> and _θ_<sub>3</sub> do not depend on _ω_ or _t_}@}, which is {@{what makes phasor notation possible}@}. {@{The time and frequency dependence}@} can be {@{suppressed and re-inserted into the outcome}@} as long as {@{the only operations used in between}@} are {@{ones that produce another phasor}@}. In {@{[angle notation](angle%20notation.md#notation)}@}, {@{the operation shown above}@} is written: {@{$$A_{1}\angle \theta _{1}+A_{2}\angle \theta _{2}=A_{3}\angle \theta _{3}.$$}@}

{@{Another way to view addition}@} is that {@{two __vectors__}@} with {@{coordinates \[_A_<sub>1</sub> cos\(_ωt_ + _θ_<sub>1</sub>\), _A_<sub>1</sub> sin\(_ωt_ + _θ_<sub>1</sub>\)\] and \[_A_<sub>2</sub> cos\(_ωt_ + _θ_<sub>2</sub>\), _A_<sub>2</sub> sin\(_ωt_ + _θ_<sub>2</sub>\)\]}@} are {@{[added vectorially](vector%20(geometric).md#addition%20and%20subtraction) to produce a resultant vector}@} with {@{coordinates \[_A_<sub>3</sub> cos\(_ωt_ + _θ_<sub>3</sub>\), _A_<sub>3</sub> sin\(_ωt_ + _θ_<sub>3</sub>\)\]}@} \(see animation\).

> {@{![Phasor diagram of three waves in perfect destructive interference](../../archives/Wikimedia%20Commons/Destructive%20interference.png)}@}
>
> {@{Phasor diagram}@} of {@{three waves in perfect destructive interference}@}

In {@{physics}@}, {@{this sort of addition occurs}@} when {@{sinusoids [interfere](interference%20(wave%20propagation).md) with each other}@}, {@{constructively or destructively}@}. {@{The static vector concept}@} provides {@{useful insight into questions like this}@}: "{@{What phase difference}@} would be {@{required between three identical sinusoids}@} for {@{perfect cancellation}@}?" In this case, simply imagine taking {@{three vectors of equal length}@} and {@{placing them head to tail such that the last head matches up with the first tail}@}. Clearly, {@{the shape which satisfies these conditions}@} is {@{an equilateral [triangle](triangle.md)}@}, so {@{the angle between each phasor to the next}@} is {@{120° \(2<!-- markdown separator -->_π_⁄3 radians\), or one third of a wavelength λ⁄3}@}. So {@{the phase difference between each wave}@} must {@{also be 120°}@}, as is the case in {@{[three-phase power](three-phase%20power.md)}@}.

In other words, what this shows is that: {@{$$\cos(\omega t)+\cos \left(\omega t+{\frac {2\pi }{3} }\right)+\cos \left(\omega t-{\frac {2\pi }{3} }\right)=0.$$}@}

In {@{the example of three waves}@}, {@{the phase difference between the first and the last wave}@} was {@{240°}@}, while for {@{two waves destructive interference happens at 180°}@}. In {@{the limit of many waves}@}, {@{the phasors must form a circle}@} for {@{destructive interference}@}, so that {@{the first phasor is nearly parallel with the last}@}. This means that for {@{many sources}@}, {@{destructive interference happens}@} when {@{the first and last wave differ by 360 degrees, a full wavelength $\lambda$}@}. This is why in {@{single slit [diffraction](diffraction.md)}@}, {@{the minima occur}@} when {@{[light](light.md) from the far edge}@} travels {@{a full wavelength further than the light from the near edge}@}.

<!-- As the single vector rotates in an anti-clockwise direction, its tip at point A will rotate one complete revolution of 360° or 2<i>π</i> radians representing one complete cycle. If the length of its moving tip is transferred at different angular intervals in time to a graph as shown above, a sinusoidal waveform would be drawn starting at the left with zero time. Each position along the horizontal axis indicates the time that has elapsed since zero time, _t_ = 0. When the vector is horizontal the tip of the vector represents the angles at 0°, 180°, and at 360°. -->

<!-- Likewise, when the tip of the vector is vertical it represents the positive peak value, \(+_A_<sub>max</sub>\) at 90° or _π_⁄2 and the negative peak value, \(−<i>A</i><sub>max</sub>\) at 270° or 3<i>π</i>⁄2. Then the time axis of the waveform represents the angle either in degrees or radians through which the phasor has moved. So we can say that a phasor represents a scaled voltage or current value of a rotating vector which is "frozen" at some point in time, \(_t_\) and in our example above, this is at an angle of 30°. -->

<!-- Sometimes when we are analysing alternating waveforms we may need to know the position of the phasor, representing the alternating quantity at some particular instant in time especially when we want to compare two different waveforms on the same axis. For example, voltage and current. We have assumed in the waveform above that the waveform starts at time _t_ = 0 with a corresponding phase angle in either degrees or radians. -->

<!-- But if a second waveform starts to the left or to the right of this zero point, or if we want to represent in phasor notation the relationship between the two waveforms, then we will need to take into account this phase difference, Φ of the waveform. Consider the diagram below from the previous Phase Difference tutorial. -->

### differentiation and integration

{@{The time [derivative](derivative.md) or [integral](integral.md)}@} of a phasor produces {@{another phasor}@}.<sup>[\[b\]](#^ref-b)</sup> For example: {@{$${\begin{aligned}&\operatorname {Re} \left({\frac {\mathrm {d} }{\mathrm {d} t} }{\mathord {\left(Ae^{i\theta }\cdot e^{i\omega t}\right)} }\right)\\={}&\operatorname {Re} \left(Ae^{i\theta }\cdot i\omega e^{i\omega t}\right)\\={}&\operatorname {Re} \left(Ae^{i\theta }\cdot e^{i\pi /2}\omega e^{i\omega t}\right)\\={}&\operatorname {Re} \left(\omega Ae^{i(\theta +\pi /2)}\cdot e^{i\omega t}\right)\\={}&\omega A\cdot \cos \left(\omega t+\theta +{\frac {\pi }{2} }\right).\end{aligned} }$$}@} Therefore, in {@{phasor representation}@}, {@{the time derivative of a sinusoid}@} becomes {@{just multiplication by the constant $i\omega =e^{i\pi /2}\cdot \omega$}@}.

Similarly, {@{integrating a phasor}@} corresponds to {@{multiplication by ${\frac {1}{i\omega } }={\frac {e^{-i\pi /2} }{\omega } }$}@}. {@{The time-dependent factor, $e^{i\omega t}$}@}, is {@{unaffected}@}.

When we solve {@{a [linear differential equation](linear%20differential%20equation.md) with phasor arithmetic}@}, we are {@{merely factoring $e^{i\omega t}$ out of all terms of the equation}@}, and {@{reinserting it into the answer}@}. For example, consider {@{the following differential equation for the voltage}@} across {@{the [capacitor](capacitor.md) in an [RC circuit](RC%20circuit.md)}@}: {@{$${\frac {\mathrm {d} \,v_{\text{C} }(t)}{\mathrm {d} t} }+{\frac {1}{RC} }v_{\text{C} }(t)={\frac {1}{RC} }v_{\text{S} }(t).$$}@}

When {@{the voltage source in this circuit is sinusoidal}@}: {@{$$v_{\text{S} }(t)=V_{\text{P} }\cdot \cos(\omega t+\theta ),$$}@} we may {@{substitute $v_{\text{S} }(t)=\operatorname {Re} \left(V_{\text{s} }\cdot e^{i\omega t}\right)$}@}. {@{$$v_{\text{C} }(t)=\operatorname {Re} \left(V_{\text{c} }\cdot e^{i\omega t}\right),$$}@} where {@{phasor $V_{\text{s} }=V_{\text{P} }e^{i\theta }$}@}, and {@{phasor $V_{\text{c} }$ is the unknown quantity to be determined}@}.

In {@{the phasor shorthand notation}@}, {@{the differential equation reduces}@} to: {@{$$i\omega V_{\text{c} }+{\frac {1}{RC} }V_{\text{c} }={\frac {1}{RC} }V_{\text{s} }.$$}@}

> {@{__Derivation__}@}
>
> {@{$${\frac {\mathrm {d} }{\mathrm {d} t} }\operatorname {Re} \left(V_{\text{c} }\cdot e^{i\omega t}\right)+{\frac {1}{RC} }\operatorname {Re} (V_{\text{c} }\cdot e^{i\omega t})={\frac {1}{RC} }\operatorname {Re} \left(V_{\text{s} }\cdot e^{i\omega t}\right)$$}@} __\([Eq.1](#math%20Eq.1)\)__
>
> Since {@{this must hold for all $t$}@}, specifically: {@{$t-{\frac {\pi }{2\omega } }$}@}, it follows that:
>
> {@{$${\frac {\mathrm {d} }{\mathrm {d} t} }\operatorname {Im} \left(V_{\text{c} }\cdot e^{i\omega t}\right)+{\frac {1}{RC} }\operatorname {Im} \left(V_{\text{c} }\cdot e^{i\omega t}\right)={\frac {1}{RC} }\operatorname {Im} \left(V_{\text{s} }\cdot e^{i\omega t}\right).$$}@} __\([Eq.2](#math%20Eq.2)\)__
>
> It is also readily seen that: {@{$${\begin{aligned}{\frac {\mathrm {d} }{\mathrm {d} t} }\operatorname {Re} \left(V_{\text{c} }\cdot e^{i\omega t}\right)&=\operatorname {Re} \left({\frac {\mathrm {d} }{\mathrm {d} t} }{\mathord {\left(V_{\text{c} }\cdot e^{i\omega t}\right)} }\right)=\operatorname {Re} \left(i\omega V_{\text{c} }\cdot e^{i\omega t}\right)\\{\frac {\mathrm {d} }{\mathrm {d} t} }\operatorname {Im} \left(V_{\text{c} }\cdot e^{i\omega t}\right)&=\operatorname {Im} \left({\frac {\mathrm {d} }{\mathrm {d} t} }{\mathord {\left(V_{\text{c} }\cdot e^{i\omega t}\right)} }\right)=\operatorname {Im} \left(i\omega V_{\text{c} }\cdot e^{i\omega t}\right).\end{aligned} }$$}@}
>
> {@{Substituting these}@} into {@{__[Eq.1](#math%20Eq.1)__ and __[Eq.2](#math%20Eq.2)__}@}, {@{multiplying __[Eq.2](#math%20Eq.2)__}@} by {@{$i$}@}, and {@{adding both equations}@} gives: {@{$${\begin{aligned}i\omega V_{\text{c} }\cdot e^{i\omega t}+{\frac {1}{RC} }V_{\text{c} }\cdot e^{i\omega t}&={\frac {1}{RC} }V_{\text{s} }\cdot e^{i\omega t}\\\left(i\omega V_{\text{c} }+{\frac {1}{RC} }V_{\text{c} }\right)\!\cdot e^{i\omega t}&=\left({\frac {1}{RC} }V_{\text{s} }\right)\cdot e^{i\omega t}\\i\omega V_{\text{c} }+{\frac {1}{RC} }V_{\text{c} }&={\frac {1}{RC} }V_{\text{s} }.\end{aligned} }$$}@}

Solving for {@{the phasor capacitor voltage}@} gives: {@{$$V_{\text{c} }={\frac {1}{1+i\omega RC} }\cdot V_{\text{s} }={\frac {1-i\omega RC}{1+(\omega RC)^{2} } }\cdot V_{\text{P} }e^{i\theta }.$$}@} \(annotation: Solve $$i\omega V_{\text{c} }+{\frac {1}{RC} }V_{\text{c} }={\frac {1}{RC} }V_{\text{s} }.$$\) As {@{we have seen}@}, {@{the factor multiplying $V_{\text{s} }$}@} represents {@{differences of the amplitude and phase}@} of {@{$v_{\text{C} }(t)$ relative to $V_{\text{P} }$ and $\theta$}@}.

In {@{polar coordinate form}@}, {@{the first term of the last expression \(annotation: $\frac {1-i\omega RC}{1+(\omega RC)^{2} }$\)}@} is: {@{$${\frac {1-i\omega RC}{1+(\omega RC)^{2} } }={\frac {1}{\sqrt {1+(\omega RC)^{2} } } }\cdot e^{-i\phi (\omega )},$$}@} \(annotation: The magnitude can be obtained by {@{multiplying the term by its conjugate to get its squared magnitude, and then take its square root}@}.\) where {@{$\phi (\omega )=\arctan(\omega RC)$}@}. \(annotation: The angle can be obtained by {@{considering the real and imaginary part of the term}@}.\) Therefore: {@{$$v_{\text{C} }(t)=\operatorname {Re} \left(V_{\text{c} }\cdot e^{i\omega t}\right)={\frac {1}{\sqrt {1+(\omega RC)^{2} } } }\cdot V_{\text{P} }\cos(\omega t+\theta -\phi (\omega )).$$}@}

### ratio of phasors

{@{A quantity called complex [impedance](electrical%20impedance.md)}@} is {@{the ratio of two phasors}@}, which is {@{not a phasor}@}, because {@{it does not correspond to a sinusoidally varying function}@}.

## applications

### circuit laws

With {@{phasors}@}, {@{the techniques for solving [DC](direct%20current.md) circuits}@} can be {@{applied to solve linear AC circuits}@}.<sup>[\[a\]](#^ref-a)</sup>

__Ohm's law for resistors__ <p> ::@:: A [resistor](resistor.md) has no time delays and therefore doesn't change the phase of a signal therefore _V_ = _IR_ remains valid.

__Ohm's law for resistors, inductors, and capacitors__ <p> ::@:: _V_ = _IZ_ where _Z_ is the complex [impedance](electrical%20impedance.md).

__[Kirchhoff's circuit laws](Kirchhoff's%20circuit%20laws.md)__ <p> ::@:: Work with voltages and current as complex phasors.

In {@{an AC circuit}@} we have {@{real power \(_P_\)}@} which is {@{a representation of the average power into the circuit}@} and {@{reactive power \(_Q_\)}@} which indicates {@{power flowing back and forth}@}. We can also define {@{the [complex power](complex%20power.md#complex%20power) _S_ = _P_ + _jQ_}@} and {@{the apparent power}@} which is {@{the magnitude of _S_}@}. {@{The power law for an AC circuit expressed in phasors}@} is then {@{_S_ = _VI_<sup>\*</sup>}@} \(where {@{_I_<sup>\*</sup> is the [complex conjugate](complex%20conjugate.md) of _I_}@}, and {@{the magnitudes of the voltage and current phasors _V_ and of _I_}@} are {@{the [RMS](root%20mean%20square.md#definition) values of the voltage and current, respectively}@}\).

Given this we can apply {@{the techniques of [analysis of resistive circuits](analysis%20of%20resistive%20circuits.md) with phasors}@} to analyze {@{single frequency linear AC circuits}@} containing {@{resistors, capacitors, and [inductors](inductor.md)}@}. {@{Multiple frequency linear AC circuits}@} and {@{AC circuits with different waveforms}@} can be {@{analyzed to find voltages and currents}@} by {@{transforming all waveforms to sine wave components \(using [Fourier series](Fourier%20series.md)\) with magnitude and phase}@} then {@{analyzing each frequency separately}@}, as allowed by {@{the [superposition theorem](superposition%20theorem.md)}@}. {@{This solution method}@} applies {@{only to inputs that are sinusoidal and for solutions that are in steady state}@}, i.e., {@{after all transients have died out}@}.<sup>[\[16\]](#^ref-16)</sup>

The concept is frequently involved in {@{representing an [electrical impedance](electrical%20impedance.md)}@}. In this case, {@{the phase angle}@} is {@{the [phase difference](phase%20difference.md#phase%20difference)}@} between {@{the voltage applied to the impedance and the current driven through it}@}.

### power engineering

- Main article: ::@:: [Phasor measurement unit](phasor%20measurement%20unit.md)

In analysis of {@{[three phase](three%20phase.md) AC power systems}@}, usually {@{a set of phasors}@} is defined as {@{the three complex [cube roots of unity](cube%20roots%20of%20unity.md)}@}, graphically represented as {@{unit magnitudes at angles of 0, 120 and 240 degrees}@}. By treating {@{polyphase AC circuit quantities as phasors}@}, {@{balanced circuits}@} can be {@{simplified}@} and {@{unbalanced circuits}@} can be treated as {@{an algebraic combination of [symmetrical components](symmetrical%20components.md)}@}. This approach {@{greatly simplifies the work required}@} in electrical calculations of {@{voltage drop, power flow, and short-circuit currents}@}. In the context of {@{power systems analysis}@}, {@{the phase angle}@} is often {@{given in [degrees](degree%20(angle).md)}@}, and {@{the magnitude in [RMS](root%20mean%20square.md) value}@} rather than {@{the peak amplitude of the sinusoid}@}.

{@{The technique of [synchrophasors](synchrophasor.md)}@} uses {@{digital instruments to measure the phasors}@} representing {@{transmission system voltages at widespread points in a transmission network}@}. {@{Differences among the phasors}@} indicate {@{power flow and system stability}@}.

### telecommunications: analog modulations

> {@{![Phasor diagrams for modulated signals](../../archives/Wikimedia%20Commons/Modulation%20phasors.svg)}@}
>
> A: {@{phasor representation of amplitude modulation}@}, B: {@{alternate representation of amplitude modulation}@}, C: {@{phasor representation of frequency modulation}@}, D: {@{alternate representation of frequency modulation}@}

{@{The rotating frame picture using phasor}@} can be {@{a powerful tool to understand analog modulations}@} such as {@{[amplitude modulation](amplitude%20modulation.md) \(and its variants<sup>[\[17\]](#^ref-17)</sup>\) and [frequency modulation](frequency%20modulation.md)}@}. {@{$$x(t)=\operatorname {Re} \left(Ae^{i\theta }\cdot e^{i2\pi f_{0}t}\right),$$}@} where {@{the term in brackets}@} is viewed as {@{a rotating vector in the complex plane}@}.

{@{The phasor}@} has {@{length $A$, rotates anti-clockwise at a rate of $f_{0}$ revolutions per second}@}, and at {@{time $t=0$ makes an angle of $\theta$ with respect to the positive real axis}@}.

{@{The waveform $x(t)$}@} can then be viewed as {@{a projection of this vector onto the real axis}@}. {@{A modulated waveform}@} is represented by {@{this phasor \(the carrier\) and two additional phasors \(the modulation phasors\)}@}. If {@{the modulating signal \(annotation: usually containing the data to be sent\)}@} is {@{a single tone of the form $Am\cos {2\pi f_{m}t}$}@}, where {@{$m$ is the modulation depth and $f_{m}$ is the frequency of the modulating signal}@}, then for {@{amplitude modulation}@} {@{the two modulation phasors}@} are given by, {@{$${1 \over 2}Ame^{i\theta }\cdot e^{i2\pi (f_{0}+f_{m})t},$$ $${1 \over 2}Ame^{i\theta }\cdot e^{i2\pi (f_{0}-f_{m})t}.$$}@} \(annotation: Literally just {@{decomposing the modulating signal into two phasors using Euler's formula}@}, then {@{multiply by the carrier initial phase $e^{i\theta}$ and its time-varying component $e^{\pm i 2\pi f_0 t}$}@}.\)

{@{The two modulation phasors are phased}@} such that {@{their vector sum is always in phase with the carrier phasor \(annotation: but not necessarily of the same magnitude\)}@}. {@{An alternative representation}@} is {@{two phasors counter rotating around the end of the carrier phasor}@} at {@{a rate $f_{m}$ relative to the carrier phasor}@}. That is, {@{$${1 \over 2}Ame^{i\theta }\cdot e^{i2\pi f_{m}t},$$ $${1 \over 2}Ame^{i\theta }\cdot e^{-i2\pi f_{m}t}.$$}@} \(annotation: {@{The common factor of $e^{i 2\pi f_0}$}@} is {@{extracted out compared to the previous representation}@}. Then we see {@{adding the above two modulation phasors}@} {@{gives the original modulating signal \(advanced by the carrier initial phase $\theta$\) by Euler's formula}@}.\)

{@{Frequency modulation}@} is {@{a similar representation}@} except that {@{the modulating phasors are not in phase with the carrier}@}. In this case {@{the vector sum of the modulating phasors}@} is {@{shifted 90° from the carrier phase}@}. {@{Strictly}@}, {@{frequency modulation representation}@} requires {@{additional small modulation phasors at $2f_{m},3f_{m}$ etc}@}, but for {@{most practical purposes}@} these are {@{ignored because their effect is very small}@}.

## see also

- [In-phase and quadrature components](in-phase%20and%20quadrature%20components.md)
  - [Constellation diagram](constellation%20diagram.md)
- [Analytic signal](analytic%20signal.md), ::@:: a generalization of phasors for time-variant amplitude, phase, and frequency.
  - [Complex envelope](complex%20envelope.md#complex%20envelope)
- [Phase factor](phase%20factor.md), ::@:: a phasor of unit magnitude

## footnotes

1. Including analysis of the AC circuits.<sup>[\[7\]](#^ref-7)</sup><sup>:&hairsp;53&hairsp;</sup> <a id="^ref-1"></a>^ref-1
2. This results from {@{${\frac {d}{dt} }e^{i\omega t}=i\omega e^{i\omega t}$}@}, which means that {@{the [complex exponential](complex%20exponential.md#complex%20exponential)}@} is {@{the [eigenfunction](eigenfunction.md) of the derivative operator}@}. <a id="^ref-2"></a>^ref-2

## references

This text incorporates [content](https://en.wikipedia.org/wiki/phasor) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFHuw FoxWilliam Bolton2002"></a> Huw Fox; William Bolton \(2002\). [_Mathematics for Engineers and Technologists_](https://archive.org/details/mathematicsforen00foxh_204). Butterworth-Heinemann. p. [30](https://archive.org/details/mathematicsforen00foxh_204/page/n36). [ISBN](ISBN%20(identifier).md) [978-0-08-051119-1](https://en.wikipedia.org/wiki/Special:BookSources/978-0-08-051119-1). <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFClay Rawlins2000"></a> Clay Rawlins \(2000\). [_Basic AC Circuits_](https://archive.org/details/basicaccircuits00mscl) \(2nd ed.\). Newnes. p. [124](https://archive.org/details/basicaccircuits00mscl/page/n134). [ISBN](ISBN%20(identifier).md) [978-0-08-049398-5](https://en.wikipedia.org/wiki/Special:BookSources/978-0-08-049398-5). <a id="^ref-2"></a>^ref-2
3. Bracewell, Ron. _The Fourier Transform and Its Applications_. McGraw-Hill, 1965. p269 <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFK. S. Suresh Kumar2008"></a> K. S. Suresh Kumar \(2008\). _Electric Circuits and Networks_. Pearson Education India. p. 272. [ISBN](ISBN%20(identifier).md) [978-81-317-1390-7](https://en.wikipedia.org/wiki/Special:BookSources/978-81-317-1390-7). <a id="^ref-4"></a>^ref-4
5. <a id="CITEREFKequian ZhangDejie Li2007"></a> Kequian Zhang; Dejie Li \(2007\). _Electromagnetic Theory for Microwaves and Optoelectronics_ \(2nd ed.\). Springer Science & Business Media. p. 13. [ISBN](ISBN%20(identifier).md) [978-3-540-74296-8](https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-74296-8). <a id="^ref-5"></a>^ref-5
6. <a id="CITEREFJ. Hindmarsh1984"></a> J. Hindmarsh \(1984\). _Electrical Machines & their Applications_ \(4th ed.\). Elsevier. p. 58. [ISBN](ISBN%20(identifier).md) [978-1-4832-9492-6](https://en.wikipedia.org/wiki/Special:BookSources/978-1-4832-9492-6). <a id="^ref-6"></a>^ref-6
7. <a id="CITEREFGross2012"></a> Gross, Charles A. \(2012\). _Fundamentals of electrical engineering_. Thaddeus Adam Roppel. Boca Raton, FL: CRC Press. [ISBN](ISBN%20(identifier).md) [978-1-4398-9807-9](https://en.wikipedia.org/wiki/Special:BookSources/978-1-4398-9807-9). [OCLC](OCLC%20(identifier).md#OCLC) [863646311](https://search.worldcat.org/oclc/863646311). <a id="^ref-7"></a>^ref-7
8. <a id="CITEREFWilliam J. Eccles2011"></a> William J. Eccles \(2011\). _Pragmatic Electrical Engineering: Fundamentals_. Morgan & Claypool Publishers. p. 51. [ISBN](ISBN%20(identifier).md) [978-1-60845-668-0](https://en.wikipedia.org/wiki/Special:BookSources/978-1-60845-668-0). <a id="^ref-8"></a>^ref-8
9. <a id="CITEREFRichard C. DorfJames A. Svoboda2010"></a> Richard C. Dorf; James A. Svoboda \(2010\). [_Introduction to Electric Circuits_](https://archive.org/details/introductiontoel00dorf_304) \(8th ed.\). John Wiley & Sons. p. [661](https://archive.org/details/introductiontoel00dorf_304/page/n680). [ISBN](ISBN%20(identifier).md) [978-0-470-52157-1](https://en.wikipedia.org/wiki/Special:BookSources/978-0-470-52157-1). <a id="^ref-9"></a>^ref-9
10. <a id="CITEREFAllan H. RobbinsWilhelm Miller2012"></a> Allan H. Robbins; Wilhelm Miller \(2012\). _Circuit Analysis: Theory and Practice_ \(5th ed.\). Cengage Learning. p. 536. [ISBN](ISBN%20(identifier).md) [978-1-285-40192-8](https://en.wikipedia.org/wiki/Special:BookSources/978-1-285-40192-8). <a id="^ref-10"></a>^ref-10
11. <a id="CITEREFWon Y. YangSeung C. Lee2008"></a> Won Y. Yang; Seung C. Lee \(2008\). _Circuit Systems with MATLAB and PSpice_. John Wiley & Sons. pp. 256–261. [ISBN](ISBN%20(identifier).md) [978-0-470-82240-1](https://en.wikipedia.org/wiki/Special:BookSources/978-0-470-82240-1). <a id="^ref-11"></a>^ref-11
12. <a id="CITEREFBasil Mahon2017"></a> Basil Mahon \(2017\). _The Forgotten Genius of Oliver Heaviside_ \(1st ed.\). Prometheus Books Learning. p. 230. [ISBN](ISBN%20(identifier).md) [978-1-63388-331-4](https://en.wikipedia.org/wiki/Special:BookSources/978-1-63388-331-4). <a id="^ref-12"></a>^ref-12
13. <a id="CITEREFNilssonRiedel2008"></a> Nilsson, James William; Riedel, Susan A. \(2008\). [_Electric circuits_](https://books.google.com/books?id=sxmM8RFL99wC) \(8th ed.\). Prentice Hall. p. 338. [ISBN](ISBN%20(identifier).md) [978-0-13-198925-2](https://en.wikipedia.org/wiki/Special:BookSources/978-0-13-198925-2)., [Chapter 9, page 338](https://books.google.com/books?id=sxmM8RFL99wC&pg=PA338) <a id="^ref-13"></a>^ref-13
14. <a id="CITEREFRawlins2000"></a> Rawlins, John C. \(2000\). [_Basic AC Circuits_](https://www.sciencedirect.com/science/article/pii/B9780750671736500146) \(Second ed.\). Newnes. pp. 427–452. [ISBN](ISBN%20(identifier).md) [9780750671736](https://en.wikipedia.org/wiki/Special:BookSources/9780750671736). <a id="^ref-14"></a>^ref-14
15. <a id="CITEREFSingh2009"></a> Singh, Ravish R \(2009\). "Section 4.5: Phasor Representation of Alternating Quantities". _Electrical Networks_. Mcgraw Hill Higher Education. p. 4.13. [ISBN](ISBN%20(identifier).md) [978-0070260962](https://en.wikipedia.org/wiki/Special:BookSources/978-0070260962). <a id="^ref-15"></a>^ref-15
16. <a id="CITEREFClayton2008"></a> Clayton, Paul \(2008\). _Introduction to electromagnetic compatibility_. Wiley. p. 861. [ISBN](ISBN%20(identifier).md) [978-81-265-2875-2](https://en.wikipedia.org/wiki/Special:BookSources/978-81-265-2875-2). <a id="^ref-16"></a>^ref-16
17. de Oliveira, H.M. and Nunes, F.D. _About the Phasor Pathways in Analogical Amplitude Modulations_. International Journal of Research in Engineering and Science \(IJRES\) Vol.2, N.1, Jan., pp.11-18, 2014. ISSN 2320-9364 <a id="^ref-17"></a>^ref-17

## further reading

- <a id="CITEREFDouglas C. Giancoli1989"></a> Douglas C. Giancoli \(1989\). _Physics for Scientists and Engineers_. Prentice Hall. [ISBN](ISBN%20(identifier).md) [0-13-666322-2](https://en.wikipedia.org/wiki/Special:BookSources/0-13-666322-2).
- <a id="CITEREFDorfTallarida1993"></a> Dorf, Richard C.; Tallarida, Ronald J. \(1993-07-15\). _Pocket Book of Electrical Engineering Formulas_ \(1 ed.\). Boca Raton, FL: CRC Press. pp. 152–155. [ISBN](ISBN%20(identifier).md) [0849344735](https://en.wikipedia.org/wiki/Special:BookSources/0849344735).

## external links

> ![Wikimedia Commons logo](../../archives/Wikimedia%20Commons/Commons-logo.svg) Wikimedia Commons has media related to ___[Phasors](https://commons.wikimedia.org/wiki/Category%3APhasors)___.

<!-- markdownlint MD028 -->

> ![Wikiversity logo](../../archives/Wikimedia%20Commons/Wikiversity%20logo%202017.svg) [Wikiversity](wikiversity.md) has a lesson on ___[Phasor algebra](https://en.wikiversity.org/wiki/Phasor%20algebra)___

- [Phasor Phactory](http://www.jhu.edu/~signals/phasorapplet2/phasorappletindex.htm)
- [Visual Representation of Phasors](http://resonanceswavesandfields.blogspot.com/2007/08/phasors.html)
- [Polar and Rectangular Notation](http://www.allaboutcircuits.com/vol_2/chpt_2/5.html)
- [Phasor in Telecommunication](http://www.de.ufpe.br/~hmo/AM_phasor_diagrams.html)

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Electrical circuits](https://en.wikipedia.org/wiki/Category:Electrical%20circuits)
> - [AC power](https://en.wikipedia.org/wiki/Category:AC%20power)
> - [Interference](https://en.wikipedia.org/wiki/Category:Interference)
> - [Trigonometry](https://en.wikipedia.org/wiki/Category:Trigonometry)
