---
aliases:
  - ELEC 2100 signal
  - ELEC 2100 signals
  - ELEC2100 signal
  - ELEC2100 signals
  - HKUST ELEC 2100 signal
  - HKUST ELEC 2100 signals
  - HKUST ELEC2100 signal
  - HKUST ELEC2100 signals
  - signal
  - signals
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/signal
  - language/in/English
---

# signal

- HKUST ELEC 2100

<!-- check: ignore-file[two_sided_calc_warning]: concept-focused prompts intentionally use descriptive wording rather than repeating every symbol on the left-hand side -->

---

Signals are mathematical descriptions of varying quantities. In ELEC 2100 they are the inputs and outputs on which systems act, so the course begins with signal definitions, representations, classifications, and basic transformations before introducing Fourier-, Laplace-, and LTI-system methods.

This note covers broad signal vocabulary, continuous-time intuition, and general transformation language. More specialized material lives in separate notes: [discrete-time signal](discrete-time%20signal.md) for the sequence toolkit, and [singular signal](singular%20signal.md) for the step-impulse-generalized-function toolkit used in convolution and transform methods.

---

Flashcards for this section are as follows:

- What is a signal in ELEC 2100? ::@:: A signal is a function of one or more independent variables that carries information about a physical quantity, message, or state.
- Why are signals introduced so early in ELEC 2100? ::@:: They are the inputs and outputs on which systems act, so later transform methods start from careful signal descriptions.
- What does `signal.md` cover? ::@:: Broad signal vocabulary, continuous-time intuition, and general transformation language. See `discrete-time signal.md` for sequences and `singular signal.md` for step-, impulse-, and generalized-function building blocks.

## signal meaning and representation

A _message_ is the underlying content to be conveyed (voice, text, images, data). A _signal_ is the physical or mathematical representation used to carry that content. The same message may appear as different signals at different stages: a spoken sentence may be an acoustic pressure wave, then a microphone voltage, then a digital bitstream.

A signal can be described graphically (waveform), analytically (formula), or numerically (table of values). These are different descriptions of the same signal, not different signals. Mathematically, a signal is a function of one or more independent variables, and one picks the most convenient description for the task.

Signal processing transforms a signal not to change the message, but to make useful structure easier to detect, measure, transmit, or interpret. Filtering unwanted noise from a music signal is a standard example.

Noise is still a signal in the mathematical sense: an unwanted random component added to a useful signal. One often works with the model useful signal plus noise rather than trying to separate signal from non-signal.

Signal shape does not guarantee meaning. The same waveform can represent different messages under different encoding rules, and the same message can be carried by very different waveforms.

---

Flashcards for this section are as follows:

- What is the difference between a message and a signal? ::@:: A message is the content to be conveyed; a signal is the representation that carries it.
- What are common examples of messages? ::@:: Voice, text, images, and data.
- What are common representation methods? ::@:: Waveform (graphical), formula (analytical), or table of values (numerical).
- How can the same message appear as different signals? ::@:: A spoken sentence may be an acoustic pressure wave, then a microphone voltage, then a digital bitstream.
- Why does the same waveform not always have the same meaning? ::@:: Meaning depends on the encoding rule, so different systems can interpret the same shape differently.
- Why process a signal? ::@:: To make useful structure easier to detect, measure, transmit, or interpret, not to change the message itself.
- How does noise reduction motivate signal processing? ::@:: Filtering suppresses unwanted noise so the useful signal becomes easier to hear or analyze.
- Why is noise still treated as a signal in ELEC 2100? ::@:: Because it is an unwanted random component carried by the same mathematical signal framework.

## signal classifications

The lecture introduces five parallel classification axes: deterministic vs random (predictability), continuous-time vs discrete-time (independent variable), periodic vs aperiodic (repetition), energy vs power (long-run accumulation), and one-dimensional vs multidimensional (number of independent variables).

A deterministic signal is specified exactly; a random signal is described statistically and cannot be predicted pointwise. A continuous-time signal $x(t)$ is defined for every relevant value of the independent variable; a discrete-time signal $x[n]$ is defined only at integer indices. A digital signal is both discrete in time and quantized in amplitude, so not every discrete-time signal is digital.

Noise illustrates the deterministic-random distinction: a clean test tone is deterministic, while thermal noise is random.

Many engineering signals depend on several variables (time, space, frequency). The Wi-Fi example shows signal strength sensed over a spatial arrangement rather than along one time axis.

These labels are parallel, not mutually exclusive. For example, $\cos t$ is deterministic, continuous-time, periodic, one-dimensional, and a power signal. A finite pulse is deterministic, continuous-time, aperiodic, one-dimensional, and typically an energy signal. A sampled noise sequence may be random, discrete-time, and aperiodic at once.

---

Flashcards for this section are as follows:

- What are the five signal-classification axes? ::@:: Deterministic vs random, continuous-time vs discrete-time, periodic vs aperiodic, energy vs power, one-dimensional vs multidimensional.
- What is a deterministic signal? ::@:: One that is specified exactly, so its value is fixed once the formula or waveform is known.
- What is a random signal? ::@:: One described statistically, not predictable pointwise.
- How does noise fit into the deterministic-vs-random classification? ::@:: Noise is usually modeled as random, while a prescribed waveform such as a test tone is deterministic.
- What is a continuous-time signal? ::@:: $x(t)$, defined for every relevant value of a continuous variable.
- What is a discrete-time signal? ::@:: $x[n]$, defined only at integer indices.
- What is a digital signal? ::@:: Discrete in time _and_ quantized in amplitude.
- What is the difference between a one-dimensional and a multidimensional signal? ::@:: A one-dimensional signal depends on one independent variable; a multidimensional signal depends on several (e.g. time and space).
- Why is the Wi-Fi visualization example multidimensional? ::@:: Signal strength is observed over a spatial arrangement rather than along one scalar axis.
- Why are signal classifications called parallel rather than hierarchical? ::@:: Labels such as deterministic, continuous-time, periodic, and one-dimensional answer different questions and may all apply simultaneously.
- How is $\cos t$ classified? ::@:: Deterministic, continuous-time, periodic, one-dimensional, power signal.
- How is a finite pulse typically classified? ::@:: Deterministic, continuous-time, aperiodic, one-dimensional, energy signal.
- How may a sampled noise sequence be classified? ::@:: Random, discrete-time, and aperiodic at the same time.

## periodicity, energy, and power

The fundamental period of a continuous-time signal is the smallest positive $T_0$ such that $x(t+T_0)=x(t)$ for all $t$. The fundamental angular frequency is $\omega_0=2\pi/T_0$ and the fundamental ordinary frequency is $f_0=1/T_0$, both positive. Unlike discrete time, continuous-time frequency is not identified modulo $2\pi$, so there is no aliasing-based maximum distinct frequency.

A sinusoid $A\cos(\omega t+\phi)$ has period $T=2\pi/|\omega|$ when $\omega\neq 0$. A sum of sinusoids is periodic only when the component periods are commensurate (equivalently, when the angular frequencies have rational ratios). For example, $x(t)=\cos 10t+\cos 30t$ has component periods $\pi/5$ and $\pi/15$, so the fundamental period is $\pi/5$.

A _period_ is any positive shift reproducing the signal; the _fundamental period_ is the smallest such shift. For example, $x(t)=\cos\!\bigl((2\pi/4)t\bigr)+\sin\!\bigl((2\pi/3)t\bigr)$ has component periods $4$ and $3$, so the fundamental period is $12$ (while $24$, $36$, etc. are also periods). If no common positive period exists, the sum is aperiodic even if it looks repetitive. For example, $\cos\!\bigl((2\pi/4)t\bigr)+\sin\!\bigl((2/3)t\bigr)$ has component periods $4$ and $3\pi$; since $4/(3\pi)$ is irrational, no finite common period exists.

Two equivalent workflows for commensurate sums: compute component periods and take their LCM, or compute component frequencies and take their GCD. Not every periodic signal is sinusoidal: a triangular wave is periodic because its shape repeats after a fixed interval.

Energy and power measure different long-run aspects. Energy is $E=\int_{-\infty}^{\infty}|x(t)|^2\,dt$ (total accumulated squared magnitude). Average power is $P=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}|x(t)|^2\,dt$ (long-term average rate).

A finite-duration pulse is usually an energy signal (finite energy, zero average power). A nonzero periodic signal is usually a power signal (infinite energy, finite average power). The zero signal has both energy and power equal to zero.

Worked examples: $x(t)=1$ for $0\le t\le 2$, zero otherwise: $E=2$, $P=0$ (energy signal). $x(t)=\cos t$: average of $\cos^2 t$ over one period is $1/2$, so $P=1/2$ (power signal).

---

Flashcards for this section are as follows:

- Is there a highest distinct continuous-time fundamental frequency? ::@:: No. Continuous-time frequencies are not identified modulo $2\pi$, so there is no aliasing-based maximum distinct fundamental frequency.
- When is a continuous-time signal periodic? ::@:: When there exists $T>0$ such that $x(t+T)=x(t)$ for all $t$. The smallest such $T$ is the fundamental period.
- Given fundamental period $T_0$, what are the fundamental frequencies? ::@:: $\omega_0=2\pi/T_0$ (angular) and $f_0=1/T_0$ (ordinary), both positive.
- For a continuous-time periodic signal with fundamental period $T_0$, what sign convention is used? ::@:: The fundamental angular frequency and ordinary frequency are taken as positive values.
- Given $A\cos(\omega t+\phi)$ with $\omega\neq 0$, what is its period? ::@:: $T=2\pi/|\omega|$.
- When is a sum of sinusoids periodic? ::@:: When the component periods are commensurate, i.e. the angular frequencies have rational ratios.
- Worked example: What is the fundamental period of $\cos 10t+\cos 30t$? ::@:: Component periods are $\pi/5$ and $\pi/15$. Since $\pi/5=3(\pi/15)$, the fundamental period is $\pi/5$.
- What is the difference between a period and the fundamental period? ::@:: A period is any positive shift that reproduces the signal; the fundamental period is the smallest such shift.
- Worked example: What is the fundamental period of $\cos\!\bigl((2\pi/4)t\bigr)+\sin\!\bigl((2\pi/3)t\bigr)$? ::@:: Component periods are $4$ and $3$, so the fundamental period is $12$.
- Why is $\cos\!\bigl((2\pi/4)t\bigr)+\sin\!\bigl((2/3)t\bigr)$ aperiodic? ::@:: Component periods are $4$ and $3\pi$; $4/(3\pi)$ is irrational, so no finite common period exists.
- Why is a triangular wave still a periodic signal even though it is not sinusoidal? ::@:: Because its full piecewise-linear shape repeats after a fixed interval, so periodicity is about exact repetition of the waveform, not about being sinusoidal.
- How can the fundamental oscillation of a commensurate sum be found from periods or frequencies? ::@:: Take the LCM of component periods, or equivalently the GCD of component ordinary frequencies.
- What is the energy formula? ::@:: $E=\int_{-\infty}^{\infty}|x(t)|^2\,dt$.
- What is the average-power formula? ::@:: $P=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}|x(t)|^2\,dt$.
- What is the difference between energy and power? ::@:: Energy is total squared magnitude over all time; power is the long-term average rate.
- Why is a finite-duration pulse usually an energy signal? ::@:: Finite total energy, but average power goes to zero over an infinite window.
- Why is a nonzero periodic signal usually a power signal? ::@:: Infinite total energy (keeps oscillating) but finite average power.
- Worked example: For $x(t)=1$ on $[0,2]$, zero otherwise, what are $E$ and $P$? ::@:: $E=\int_0^2 1\,dt=2$, $P=\lim_{T\to\infty}2/(2T)=0$. Energy signal.
- Worked example: For $x(t)=\cos t$, what is $P$? ::@:: Average of $\cos^2 t$ over one period is $1/2$, so $P=1/2$. Power signal.

## standard continuous-time signal families

The opening ELEC 2100 lectures present five standard signal families: exponentials, sinusoids, complex exponentials, sampling signals, and Gaussian pulses.

A real exponential $x(t)=Ae^{\alpha t}$ decays if $\alpha<0$, grows if $\alpha>0$, and is constant if $\alpha=0$. A one-sided decaying exponential $Ke^{-t/\tau}u(t)$ introduces the time constant $\tau>0$, which sets the decay rate and gives $x(\tau)=K/e$.

A sinusoid $A\sin(\omega t+\theta)$ or $A\cos(\omega t+\theta)$ is characterized by amplitude, angular frequency, and initial phase. Ordinary frequency is $f=\omega/(2\pi)$, period $T=2\pi/\omega$ when $\omega>0$. A damped sinusoid $Ke^{-\alpha t}\sin(\omega_0 t)u(t)$ combines oscillation with a shrinking envelope. Physical examples: mass-spring-damper response, electromagnetic wave in a conductor.

A complex exponential $Ke^{st}$ with $s=\sigma+j\omega$ unifies growth, decay, and oscillation: $Ke^{(\sigma+j\omega)t}=Ke^{\sigma t}e^{j\omega t}$. Here $\sigma$ controls growth/decay, $\omega$ controls oscillation.

The sampling signal is $\operatorname{Sa}(t)=\sin t/t$ with $\operatorname{Sa}(0)=1$ (removable singularity). It is even, has zeros at $t=\pm n\pi$ for integers $n\ge 1$, and decays toward $0$ as $|t|\to\infty$. The normalized sinc is $\operatorname{sinc}(t)=\sin(\pi t)/(\pi t)$, so $\operatorname{Sa}(t)=\operatorname{sinc}(t/\pi)$ and $\operatorname{sinc}(t)=\operatorname{Sa}(\pi t)$.

The Gaussian pulse $x(t)=E\exp\!\left(-(t/\tau)^2\right)$ is a smooth localized pulse with peak $E$ at $t=0$ and width set by $\tau$. Unlike the sampling signal, it stays positive and decays smoothly without side lobes.

Comparison: real exponential changes amplitude without oscillating; sinusoid oscillates with constant envelope; damped sinusoid oscillates inside a changing envelope; complex exponential unifies all three; sampling signal oscillates with regularly spaced zeros; Gaussian pulse is smooth and positive.

---

Flashcards for this section are as follows:

- Which standard signal families are highlighted? ::@:: Exponentials, sinusoids, complex exponentials, sampling signals, and Gaussian pulses.
- Given $x(t)=Ae^{\alpha t}$, how does $\alpha$ affect behavior? ::@:: $\alpha<0$: decay; $\alpha>0$: growth; $\alpha=0$: constant.
- In $Ke^{-t/\tau}u(t)$, what does $\tau$ control? ::@:: The decay rate; $x(\tau)=K/e$.
- What characterizes a sinusoid $A\sin(\omega t+\theta)$? ::@:: Amplitude, angular frequency, and initial phase.
- Given a sinusoid with angular frequency $\omega>0$, how are its ordinary frequency and period related to $\omega$? ::@:: They satisfy $f=\omega/(2\pi)$ and $T=2\pi/\omega$.
- What does a damped sinusoid combine? ::@:: It combines oscillation with exponential decay, so its envelope shrinks while it continues to oscillate.
- What are standard physical examples of damped sinusoidal signals? ::@:: A mass-spring-damper response and an electromagnetic wave attenuating in a conductor are standard examples, because both keep oscillating while their envelopes decay.
- Given $Ke^{st}$ with $s=\sigma+j\omega$, what kind of object is it? ::@:: A complex exponential with complex frequency $s$.
- What do $\sigma$ and $\omega$ control in $Ke^{(\sigma+j\omega)t}$? ::@:: $\sigma$: growth/decay rate; $\omega$: oscillation frequency.
- What are the main qualitative properties of $\operatorname{Sa}(t)$? ::@:: It is even, has zeros at $\pm n\pi$ for integers $n\ge 1$, and decays toward $0$ as $|t|\to\infty$.
- How is the sampling signal defined? ::@:: $\operatorname{Sa}(t)=\sin t/t$ for $t\neq 0$, with $\operatorname{Sa}(0)=1$.
- What is the normalized sinc function? ::@:: $\operatorname{sinc}(t)=\sin(\pi t)/(\pi t)$.
- How are $\operatorname{Sa}(t)$ and $\operatorname{sinc}(t)$ related? ::@:: $\operatorname{Sa}(t)=\operatorname{sinc}(t/\pi)$ and $\operatorname{sinc}(t)=\operatorname{Sa}(\pi t)$.
- Why can the sampling signal be assigned the finite value $\operatorname{Sa}(0)=1$ at the origin? ::@:: Because $\lim_{t\to0}\sin t/t=1$, so the apparent $0/0$ form is a removable singularity rather than a real divergence.
- Why is the sampling signal a natural interpolation kernel? ::@:: Its shifted copies can be large at one sampling location while vanishing at neighboring ideal zero locations.
- What does $E\exp(-(t/\tau)^2)$ look like? ::@:: A smooth localized pulse, peak $E$ at $t=0$, width set by $\tau$.
- Worked example: For $x(t)=e^{(-2+j3)t}$, what are the envelope and oscillation? ::@:: Envelope decays like $e^{-2t}$; oscillation frequency is $\omega=3$ rad/s.

## time transformations and basic operations

The lecture separates vertical operations (addition, multiplication, differentiation, integration) from horizontal ones (time shifting, reversal, scaling). Horizontal transformations act on the argument, changing the time axis.

Standard horizontal transformations: $x(t-t_0)$ delays (shift right by $t_0$); $x(t+t_0)$ advances (shift left by $t_0$); $x(-t)$ reflects about the vertical axis; $x(at)$ compresses if $|a|>1$, expands if $0<|a|<1$, and reverses if $a<0$.

The substitution trick handles complicated input transformations: introduce one substitution at a time and interpret each step literally. Feature tracking is faster: if a feature of $x(t)$ is at $t=t_1$, it appears in $x(at+b)$ where $at+b=t_1$, i.e. at $t=(t_1-b)/a$.

Affine transformations must be read carefully. $x(3t+5)=x(3(t+5/3))$: compress by $3$, then shift left by $5/3$. $x(-2t+4)=x(-2(t-2))$: reverse and compress by $2$, then shift right by $2$.

For graph-transformation problems, rewrite $x(at+b)$ into nested form and apply operations in that order. Feature tracking is often fastest: solve $at+b=t_1$ for the new location. If the original support is $0\le t\le 3$, the support of $x(-2t+2)$ comes from $0\le -2t+2\le 3$, giving $-1/2\le t\le 1$.

Do not confuse inside and outside operations: $x(t)+2$ is a vertical shift up, while $x(t+2)$ is a horizontal shift left. Differentiation and integration are vertical operations: differentiation emphasizes rapid change, integration accumulates area.

---

Flashcards for this section are as follows:

- What is the difference between dependent-variable and independent-variable operations? ::@:: Outside operations act on signal values; inside operations act on the argument (time axis).
- What do $x(t-t_0)$ and $x(t+t_0)$ do? ::@:: Shift right (delay) and shift left (advance), respectively.
- What does $x(-t)$ do? ::@:: Reflects the waveform across the vertical axis.
- How does $x(at)$ work? ::@:: $|a|>1$: compress; $0<|a|<1$: expand; $a<0$: also reverse.
- If a feature of $x(t)$ is at $t=t_1$, where is it in $x(at+b)$? ::@:: At $t=(t_1-b)/a$.
- Worked example: How should $x(3t+5)$ be interpreted? ::@:: $3t+5=3(t+5/3)$: compress by $3$, shift left by $5/3$.
- Worked example: How should $x(-2t+4)$ be interpreted? ::@:: $-2t+4=-2(t-2)$: reverse and compress by $2$, shift right by $2$.
- Worked example: If $x(t)$ has support $[0,3]$, what is the support of $x(-2t+2)$? ::@:: $0\le -2t+2\le 3$ gives $-1/2\le t\le 1$.
- What is the difference between $x(t)+2$ and $x(t+2)$? ::@:: $x(t)+2$ shifts up; $x(t+2)$ shifts left.
- What do differentiation and integration do to a signal conceptually? ::@:: Differentiation emphasizes rapid change, whereas integration accumulates area over time.

## complex numbers and orthogonal decompositions

Complex numbers appear early because oscillatory signals use complex exponentials. Rectangular form: $z=x+jy$. Polar form: $z=re^{j\theta}$, where $r=|z|$ and $\theta=\arg z$. Euler's relation: $e^{j\theta}=\cos\theta+j\sin\theta$, giving $\cos(\omega t)=\frac{e^{j\omega t}+e^{-j\omega t}}{2}$ and $\sin(\omega t)=\frac{e^{j\omega t}-e^{-j\omega t}}{2j}$.

Orthogonality starts from vectors: the dot product measures alignment and is zero for perpendicular directions. For signals, the inner product (integral or sum) generalizes this: orthogonality means the inner product is zero. Fourier-series formulas live in [Fourier series](Fourier%20series.md).

### atan2 and quadrant-aware phase

The robust phase extraction from rectangular coordinates uses $\operatorname{atan2}(y,x)$, which returns the principal argument of $x+jy$ in $(-\pi,\pi]$. Unlike $\arctan(y/x)$, it uses both signs to choose the correct quadrant and handles $x=0$. For Fourier analysis: $\phi(\omega)=\operatorname{atan2}(\Im\{F(\omega)\},\Re\{F(\omega)\})$. Recall cue: "$y$ first, $x$ second".

The same lecture uses DC-AC decomposition: $x(t)=x_{\mathrm{DC}}+x_{\mathrm{AC}}(t)$, where $x_{\mathrm{DC}}$ is the period average and $x_{\mathrm{AC}}$ has zero mean. Power splits additively because the cross term vanishes.

Even-odd decomposition: $x_e(t)=\frac{x(t)+x(-t)}{2}$, $x_o(t)=\frac{x(t)-x(-t)}{2}$. Over a symmetric interval, the cross term vanishes because even$\times$odd is odd.

Real-imaginary decomposition: $x_R(t)=\frac{x(t)+x^*(t)}{2}$, $x_I(t)=\frac{x(t)-x^*(t)}{2j}$. Since $|x(t)|^2=x_R^2(t)+x_I^2(t)$, power splits additively.

Worked examples: $x(t)=1+\sin t$: DC part $1$, AC part $\sin t$, average power $1+1/2=3/2$. Same signal: even part $1$, odd part $\sin t$, same power split. $x(t)=\cos t+j\sin t$: real-part power $1/2$, imaginary-part power $1/2$, total $1$. $x(t)=2e^{j2\pi t}=2\cos(2\pi t)+j2\sin(2\pi t)$: magnitude $2$, phase $2\pi t$ mod $2\pi$, conjugate $x^*(t)=2e^{-j2\pi t}$ flips phase sign.

---

Flashcards for this section are as follows:

- What is $\operatorname{atan2}(y,x)$? ::@:: It returns the principal argument of $x+jy$, usually in $(-\pi,\pi]$. Use it instead of $\arctan(y/x)$ because it preserves quadrant and handles $x=0$.
- What does $\operatorname{atan2}(y,x)$ do that $\arctan(y/x)$ cannot do reliably? ::@:: It uses the signs of both $x$ and $y$ to select the correct quadrant and still works when $x=0$, whereas $\arctan(y/x)$ only sees a ratio and loses quadrant information.
- How is $\operatorname{atan2}$ interpreted geometrically in complex-number language? ::@:: It is the directed angle from the positive real axis to the vector ending at $(x,y)$, i.e., the phase of $x+jy$.
- What is the robust Fourier phase formula? ::@:: $\phi(\omega)=\operatorname{atan2}(\Im\{F(\omega)\},\Re\{F(\omega)\})$.
- What are the rectangular and polar forms of a complex number? ::@:: $z=x+jy$ (rectangular) or $z=re^{j\theta}$ (polar), with $r=|z|$, $\theta=\arg z$.
- What is Euler's relation? ::@:: $e^{j\theta}=\cos\theta+j\sin\theta$.
- What is the relationship between the vector dot product and a signal inner product? ::@:: The dot product is the finite-dimensional vector measure of alignment, while the inner product is its signal-space generalization, usually built from an integral or a sum.
- What does orthogonality mean in signal language? ::@:: It means the relevant inner product of the two signals is zero, just as perpendicular vectors have zero dot product.
- How can $\cos(\omega t)$ and $\sin(\omega t)$ be written with complex exponentials? ::@:: $\cos(\omega t)=\frac{e^{j\omega t}+e^{-j\omega t}}{2}$, $\sin(\omega t)=\frac{e^{j\omega t}-e^{-j\omega t}}{2j}$.
- What is orthogonality in signal language? ::@:: The inner product of two signals is zero, like perpendicular vectors having zero dot product.
- How can a periodic signal be split into DC and AC? ::@:: $x(t)=x_{\mathrm{DC}}+x_{\mathrm{AC}}(t)$, where $x_{\mathrm{DC}}$ is the period average and $x_{\mathrm{AC}}$ has zero mean. Power splits additively.
- For a periodic signal, how is the DC component obtained? ::@:: It is the average of the signal over one period.
- Why does the DC-AC cross term vanish in the power split? ::@:: The AC component has zero average over one period, so the mixed term integrates to zero.
- What are the even and odd parts? ::@:: $x_e(t)=\frac{x(t)+x(-t)}{2}$, $x_o(t)=\frac{x(t)-x(-t)}{2}$.
- Why does the even-odd cross term vanish in the power split? ::@:: Over a symmetric interval, the product of an even function and an odd function is odd, so its integral is zero.
- What are the real and imaginary parts? ::@:: $x_R(t)=\frac{x(t)+x^*(t)}{2}$, $x_I(t)=\frac{x(t)-x^*(t)}{2j}$.
- Why does the power split additively into real and imaginary parts? ::@:: Because $|x(t)|^2=x_R^2(t)+x_I^2(t)$, so the real and imaginary parts contribute on orthogonal axes.
- Worked example: For $x(t)=1+\sin t$, what is the average power? ::@:: DC part $1$, AC part $\sin t$, power $1+1/2=3/2$.
- Worked example: For $x(t)=\cos t+j\sin t$, what is the total power? ::@:: Real-part power $1/2$, imaginary-part power $1/2$, total $1$.
- Worked example: For $x(t)=2e^{j2\pi t}$, what are the magnitude and phase? ::@:: Magnitude $2$, phase $2\pi t$ mod $2\pi$.
- Worked example: If $x(t)=2e^{j2\pi t}$, what changes and what stays the same in the conjugate signal $x^*(t)$? ::@:: Conjugation gives $x^*(t)=2e^{-j2\pi t}$. The magnitude stays $2$. The phase changes sign from $2\pi t$ to $-2\pi t$ modulo $2\pi$. The real part stays $2\cos(2\pi t)$, while the imaginary part flips from $2\sin(2\pi t)$ to $-2\sin(2\pi t)$.

## discrete-time sequences and periodicity

A discrete-time signal is a sequence indexed by integers, read sample by sample. Sampling bridges continuous time to discrete time; interpolation or reconstruction bridges back.

Discrete-time periodicity is stricter: the period must be a positive integer shift in the index. The fundamental period is the smallest positive integer $N_0$; the fundamental digital frequency is $2\pi/N_0$. A particular sinusoid may be a higher harmonic of that fundamental. To read one cycle from a stem plot, start at the smallest valid index and count $N_0$ consecutive samples.

Discrete-time frequency is periodic modulo $2\pi$: $e^{j(\omega+2\pi k)n}=e^{j\omega n}$. For real sinusoids, reduce mod $2\pi$ and fold into $0\le \omega\le \pi$ (or $0\le f\le 1/2$ cycle/sample). The largest distinct angular frequency is $\pi$ rad/sample.

The detailed treatment of discrete-time representations, standard families, and periodicity examples is in [`discrete-time signal`](discrete-time%20signal.md).

---

Flashcards for this section are as follows:

- What takes continuous time to discrete time? ::@:: Sampling. Interpolation or reconstruction reverses the process.
- Why is discrete-time periodicity stricter? ::@:: The period must be a positive integer shift in the sample index.
- What is the fundamental period of a sequence? ::@:: The smallest positive integer sample-index shift that reproduces the sequence.
- Why is discrete-time frequency periodic mod $2\pi$? ::@:: Because $e^{j(\omega+2\pi k)n}=e^{j\omega n}$ for every integer $k$.
- What is the largest distinct real discrete-time frequency? ::@:: $\pi$ rad/sample (or $1/2$ cycle/sample).
- How should one read one cycle from a stem plot? ::@:: Start at the smallest valid index and count $N_0$ consecutive samples.
