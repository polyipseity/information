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

Signals are mathematical descriptions of varying quantities. In ELEC 2100 they are the objects acted on by systems, so the course starts by clarifying what a signal is, how it is represented, how it is classified, and how its basic transformations should be interpreted before later Fourier-, Laplace-, and LTI-system methods are introduced.

---

Flashcards for this section are as follows:

- What is a signal? ::@:: A signal is a function of one or more independent variables that carries information about a physical quantity, message, or state.
- Why are signals introduced so early in ELEC 2100? ::@:: They are the inputs and outputs on which systems act, so later transform methods start from careful signal descriptions.

## signal meaning and representation

The lecture distinguishes between a _message_ and a _signal_. A message is the underlying content to be conveyed, such as voice, text, images, or data. A signal is the physical or mathematical representation used to encode and carry that content. The same message may therefore appear as different signals at different stages of a communication chain: for example, a spoken sentence may exist as an acoustic pressure wave, then as a microphone voltage, and then as a digital bitstream.

The same signal may also be described in several different ways. The lecture highlights graphical representation by waveform plotting, analytical representation by an explicit formula, and numerical representation by a table of values. These are different descriptions of the same signal, not different signals. The common mathematical viewpoint is that a signal is a function of one or more independent variables, and one chooses the most convenient description for plotting, calculation, communication, or storage.

This representational flexibility explains why signal processing matters. A signal is often transformed not to change the underlying message, but to make useful structure easier to detect, measure, transmit, or interpret. Noise reduction is a standard example: if a music signal is contaminated by unwanted noise, filtering is used to suppress the unwanted component so that the useful content becomes clearer. More generally, signals are processed so that important parameters or patterns become easier to analyze or estimate.

It is also important not to confuse signal shape with meaning. Two different systems may assign different meanings to the same waveform shape, because interpretation depends on the encoding rule. Conversely, the same message may be carried by very different waveforms. The right comparison is therefore message versus representation, not content versus graph shape alone.

---

Flashcards for this section are as follows:

- What is the difference between a message and a signal? ::@:: A message is the underlying content to be conveyed, while a signal is the physical or mathematical representation used to encode and carry that content.
- What are common examples of messages? ::@:: Voice, text, images, and data are examples of messages that signals can represent and transmit.
- What are the main representation methods for a signal? ::@:: A signal may be represented graphically by a waveform, analytically by a formula, or numerically by a table of values.
- How can the same signal appear in different forms? ::@:: The same signal may be shown as a waveform plot, a formula, or a table, depending on which description is most convenient.
- How can the same message appear as different signals? ::@:: The same message may be carried successively by an acoustic wave, a microphone voltage, and a digital bitstream.
- Why does the same waveform not necessarily imply the same meaning? ::@:: Meaning depends on the encoding rule used by the system, so the same waveform shape can represent different messages in different contexts.
- Why process a signal at all? ::@:: A signal is processed so that useful structure becomes easier to detect, measure, transmit, or interpret rather than to change the underlying message itself.
- How does noise reduction motivate signal processing? ::@:: Filtering suppresses the unwanted noise component so that the useful signal becomes easier to hear or analyze.

## signal classifications

The lecture introduces several classification axes, and they should be kept separate rather than mixed into one ladder. Deterministic versus random describes predictability. Continuous-time versus discrete-time describes the independent variable. Periodic versus aperiodic describes exact repetition. Energy versus power describes how squared magnitude accumulates over long observation windows. One-dimensional versus multidimensional describes how many independent variables are needed.

A deterministic signal is specified exactly, whereas a random signal is described statistically and cannot be predicted pointwise in advance. A continuous-time signal is written as $x(t)$ and is defined for every relevant value of the time variable. A discrete-time signal is written as $x[n]$ and is defined only at indexed instants. A digital signal is a more specific notion: it is discrete in time _and_ quantized in amplitude, so not every discrete-time signal is digital.

The lecture also emphasizes that many engineering signals are not just one waveform on one time axis. A multidimensional signal may depend on several variables such as time, space, or frequency coordinates. The Wi-Fi visualization example is meant to make this point concrete: signal strength is sensed over a richer spatial arrangement rather than only along one scalar time axis.

These labels are parallel, not mutually exclusive. For example, $\cos t$ is deterministic, continuous-time, periodic, one-dimensional, and a power signal. A finite pulse is deterministic, continuous-time, aperiodic, one-dimensional, and typically an energy signal. A sampled noise sequence may be random, discrete-time, and aperiodic at the same time. The point is not to force one master label, but to know which question each label answers.

---

Flashcards for this section are as follows:

- What are the main signal-classification axes introduced in Chapter 1? ::@:: They are deterministic vs random, continuous-time vs discrete-time, periodic vs aperiodic, energy vs power, and one-dimensional vs multidimensional.
- What is a deterministic signal? ::@:: A deterministic signal is specified exactly, so its value is fixed once the formula or waveform is known.
- What is a random signal? ::@:: A random signal is described statistically and cannot be predicted pointwise in advance.
- What is a continuous-time signal? ::@:: A continuous-time signal is written as $x(t)$ and is defined for every relevant value of a continuous variable.
- What is a discrete-time signal? ::@:: A discrete-time signal is written as $x[n]$ and is defined only at indexed instants.
- What is the difference between a discrete-time signal and a digital signal? ::@:: A discrete-time signal becomes digital only when its amplitude is also quantized, so discrete-time and digital are not synonymous.
- What is the difference between a one-dimensional and a multidimensional signal? ::@:: A one-dimensional signal depends on one independent variable, whereas a multidimensional signal depends on several variables such as time and space.
- Why is the Wi-Fi visualization example multidimensional? ::@:: Signal strength is observed over a richer spatial arrangement rather than along one scalar axis only.
- Why are signal classifications called parallel rather than hierarchical? ::@:: Labels such as deterministic, continuous-time, periodic, and one-dimensional answer different questions and may all apply to the same signal simultaneously.
- How is $\cos t$ classified? ::@:: It is deterministic, continuous-time, periodic, one-dimensional, and a power signal.
- How is a finite pulse typically classified? ::@:: It is deterministic, continuous-time, aperiodic, one-dimensional, and typically an energy signal.
- How may a sampled noise sequence be classified? ::@:: It may be random, discrete-time, and aperiodic at the same time.

## periodicity, energy, and power

For a continuous-time signal, periodicity means exact repetition after a positive real shift. A signal $x(t)$ is periodic if there exists $T>0$ such that $x(t+T)=x(t)$ for all $t$. The smallest such positive value is the fundamental period, and the corresponding fundamental angular frequency is $\omega_0=2\pi/T$.

This definition matters most when comparing a single sinusoid with sums of oscillations. A sinusoid such as $A\cos(\omega t+\phi)$ has period $T=2\pi/|\omega|$ when $\omega\neq 0$. A sum of sinusoids is periodic only when the component periods are commensurate, or equivalently when their angular frequencies have rational ratios. For example, $x(t)=\cos 10t+\cos 30t$ is periodic because the component periods are $\pi/5$ and $\pi/15$, so the fundamental period is $\pi/5$. If no common positive period exists, the oscillation may look repetitive but is still aperiodic or quasi-periodic rather than truly periodic.

Energy and power are different long-run measurements. The energy of a continuous-time signal is $E=\int_{-\infty}^{\infty}|x(t)|^2\,dt$, while the average power is $P=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}|x(t)|^2\,dt$. Energy asks for the total accumulated squared magnitude over all time. Power asks for the long-term average rate of squared magnitude.

A finite-duration pulse is usually an energy signal: it accumulates finite total energy, but its average power becomes zero when spread across an infinite observation window. A nonzero periodic signal is usually a power signal: its total energy diverges because the oscillation continues forever, but its average power over the long run is finite. The zero signal is the edge case for which both energy and power are zero.

Two standard worked examples capture the distinction. If $x(t)=1$ for $0\le t\le 2$ and $x(t)=0$ otherwise, then $E=2$ and $P=0$, so the signal is an energy signal. If $x(t)=\cos t$, then the average of $\cos^2 t$ over one period is $1/2$, so the signal has average power $1/2$ and is a power signal.

---

Flashcards for this section are as follows:

- When is a continuous-time signal periodic? ::@:: It is periodic if there exists $T>0$ such that $x(t+T)=x(t)$ for all $t$; the smallest such positive $T$ is the fundamental period.
- Given a continuous-time signal with fundamental period $T$, what is its fundamental angular frequency? ::@:: Its fundamental angular frequency is $\omega_0=2\pi/T$.
- Given a sinusoid $A\cos(\omega t+\phi)$ with $\omega\neq 0$, what is its period? ::@:: Its period is $T=2\pi/|\omega|$.
- When is a sum of sinusoids periodic? ::@:: It is periodic only when the component periods are commensurate, equivalently when the component angular frequencies have rational ratios.
- Worked example: Given $x(t)=\cos 10t+\cos 30t$, what is the fundamental period? ::@:: Step 1: compute the component periods $T_1=2\pi/10=\pi/5$ and $T_2=2\pi/30=\pi/15$. <br/> Step 2: look for the smallest common positive multiple. <br/> Step 3: since $\pi/5=3(\pi/15)$, the common fundamental period is $\pi/5$.
- What is the continuous-time energy formula for a signal $x(t)$? ::@:: It is $E=\int_{-\infty}^{\infty}|x(t)|^2\,dt$.
- What is the continuous-time average-power formula for a signal $x(t)$? ::@:: It is $P=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}|x(t)|^2\,dt$.
- What is the difference between signal energy and signal power? ::@:: Energy measures total accumulated squared magnitude over all time, whereas power measures long-term average squared magnitude.
- Why is a finite-duration pulse usually an energy signal? ::@:: It has finite total energy, but its average power goes to zero when spread over an infinite observation window.
- Why is a nonzero bounded periodic signal usually a power signal? ::@:: It has finite average power but infinite total energy because it keeps oscillating forever.
- Worked example: Given $x(t)=1$ for $0\le t\le 2$ and $x(t)=0$ otherwise, what are its energy, average power, and classification? ::@:: Step 1: compute the energy $E=\int_{-\infty}^{\infty}|x(t)|^2dt=\int_0^2 1\,dt=2$. <br/> Step 2: compute the long-run average power $P=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}|x(t)|^2dt=\lim_{T\to\infty}\frac{2}{2T}=0$. <br/> Step 3: finite nonzero energy and zero average power mean it is an energy signal.
- Worked example: Given $x(t)=\cos t$, what are its average power and classification? ::@:: Step 1: use $\cos^2 t=\tfrac{1+\cos 2t}{2}$. <br/> Step 2: average over one period to get $P=\frac{1}{2\pi}\int_0^{2\pi}\cos^2 t\,dt=\tfrac12$. <br/> Step 3: a nonzero periodic signal has infinite total energy but finite average power, so it is a power signal.

## standard continuous-time signal families

Chapter 1 groups several standard signal families as reusable building blocks: exponentials, sinusoids, complex exponentials, sampling signals, and Gaussian pulses. Each family highlights a different recurring pattern that later reappears in transform methods and system responses.

A real exponential has the form $x(t)=Ae^{\alpha t}$. If $\alpha<0$, it decays; if $\alpha>0$, it grows; if $\alpha=0$, it reduces to a constant. A one-sided decaying exponential such as $Ke^{-t/\tau}u(t)$ introduces the time constant $\tau>0$, which controls the decay rate and satisfies $x(\tau)=K/e$.

A sinusoid such as $A\sin(\omega t+\theta)$ or $A\cos(\omega t+\theta)$ is characterized by amplitude, angular frequency, and initial phase. The ordinary frequency is $f=\omega/(2\pi)$, and the period is $T=1/f=2\pi/\omega$ when $\omega>0$. A damped sinusoid such as $Ke^{-\alpha t}\sin(\omega_0 t)u(t)$ combines oscillation with an exponentially shrinking envelope.

A complex exponential has the form $Ke^{st}$ with complex frequency $s=\sigma+j\omega$. Writing it as $Ke^{(\sigma+j\omega)t}=Ke^{\sigma t}e^{j\omega t}$ makes the roles clear: $\sigma$ controls growth or decay, while $\omega$ controls oscillation. Real exponentials and pure complex oscillations are therefore special cases of one unified family.

The sampling signal is introduced in the unnormalized form $\operatorname{Sa}(t)=\sin t/t$, with limiting value $\operatorname{Sa}(0)=1$. It is even, has zeros at $t=\pm n\pi$ for integers $n\ge 1$, and decays toward $0$ as $|t|\to\infty$. Its graph consists of a dominant main lobe near the origin together with decaying side lobes. The normalized sinc function is $\operatorname{sinc}(t)=\sin(\pi t)/(\pi t)$, so $\operatorname{Sa}(t)=\operatorname{sinc}(t/\pi)$ and $\operatorname{sinc}(t)=\operatorname{Sa}(\pi t)$. The zero crossings and peaked center explain why this family later becomes a natural interpolation kernel in sampling theory.

The Gaussian pulse $x(t)=E\exp\!\left(-(t/\tau)^2\right)$ is another localized building block. Its peak value is $E$ at $t=0$, and $\tau$ controls its width. Unlike the sampling signal, it does not oscillate or cross zero repeatedly; it stays positive and decays smoothly.

Comparisons help keep the families straight. A real exponential changes amplitude without oscillating. A sinusoid oscillates with constant envelope. A damped sinusoid oscillates inside a changing envelope. A complex exponential unifies growth, decay, and oscillation in one formula. The sampling signal and Gaussian pulse are both centered near the origin, but only the sampling signal has oscillatory side lobes and regularly spaced zero crossings.

---

Flashcards for this section are as follows:

- Which standard continuous-time signal families are highlighted in Chapter 1? ::@:: Exponentials, sinusoids, complex exponentials, sampling signals, and Gaussian pulses are presented as standard continuous-time building blocks.
- Given the real exponential family $x(t)=Ae^{\alpha t}$, how does the sign of $\alpha$ affect its behavior? ::@:: It decays when $\alpha<0$, grows when $\alpha>0$, and becomes a constant when $\alpha=0$.
- In the one-sided exponential $Ke^{-t/\tau}u(t)$, what does the time constant $\tau$ tell you? ::@:: It controls the decay rate and gives the amplitude value $K/e$ at $t=\tau$.
- Given a sinusoid such as $A\sin(\omega t+\theta)$ or $A\cos(\omega t+\theta)$, what parameters characterize it? ::@:: It is characterized by amplitude, angular frequency, and initial phase.
- Given a sinusoid with angular frequency $\omega>0$, how are its ordinary frequency and period related to $\omega$? ::@:: They satisfy $f=\omega/(2\pi)$ and $T=2\pi/\omega$.
- What does a damped sinusoid combine? ::@:: It combines oscillation with exponential decay, so its envelope shrinks while it continues to oscillate.
- Given the signal family $Ke^{st}$ with $s=\sigma+j\omega$, what kind of object is it? ::@:: It is a complex exponential with complex frequency $s=\sigma+j\omega$.
- In the complex exponential $Ke^{(\sigma+j\omega)t}$, what do $\sigma$ and $\omega$ control? ::@:: $\sigma$ controls growth or decay, while $\omega$ controls oscillation.
- How is the sampling signal defined, including its limiting value at the origin? ::@:: It is $\operatorname{Sa}(t)=\sin t/t$ for $t\neq 0$, with limiting value $\operatorname{Sa}(0)=1$.
- What are the main qualitative properties of $\operatorname{Sa}(t)$? ::@:: It is even, has zeros at $\pm n\pi$ for integers $n\ge 1$, and decays toward $0$ as $|t|\to\infty$.
- What is the normalized sinc function? ::@:: It is $\operatorname{sinc}(t)=\sin(\pi t)/(\pi t)$.
- How are $\operatorname{Sa}(t)$ and the normalized sinc function related? ::@:: They differ only by argument scaling: $\operatorname{Sa}(t)=\operatorname{sinc}(t/\pi)$ and $\operatorname{sinc}(t)=\operatorname{Sa}(\pi t)$.
- Why is the sampling signal a natural interpolation kernel? ::@:: Its shifted copies can be large at one sampling location while vanishing at neighboring ideal zero locations.
- What does the Gaussian pulse $E\exp\!\left(-(t/\tau)^2\right)$ look like conceptually? ::@:: It is a smooth localized pulse with peak value $E$ at $t=0$ and width controlled by $\tau$.
- What is the difference between a real exponential and a sinusoid? ::@:: A real exponential changes amplitude without oscillating, whereas a sinusoid oscillates with a constant envelope.
- What is the difference between the sampling signal and the Gaussian pulse? ::@:: The sampling signal oscillates and crosses zero repeatedly, whereas the Gaussian pulse stays positive and decays smoothly without side lobes.
- Worked example: Given $x(t)=e^{(-2+j3)t}$, what are its envelope behavior and oscillation parameter? ::@:: Step 1: split the exponent as $e^{(-2+j3)t}=e^{-2t}e^{j3t}$. <br/> Step 2: the real part $-2$ controls the envelope, so it decays like $e^{-2t}$. <br/> Step 3: the imaginary part $3$ is the oscillation parameter, so $\omega=3$.

## time transformations and basic operations

The lecture separates vertical operations from horizontal ones. Dependent-variable operations such as addition, multiplication, differentiation, and integration act on the signal value after the function has been evaluated. Independent-variable transformations such as time shifting, reversal, and scaling act on the argument of the signal, so they change the time axis itself and are often more difficult to interpret.

The basic horizontal transformations are standard. A signal $x(t-t_0)$ is delayed, so the waveform shifts right by $t_0$. A signal $x(t+t_0)$ is advanced, so the waveform shifts left by $t_0$. A signal $x(-t)$ is reflected about the vertical axis. A signal $x(at)$ is compressed when $|a|>1$, expanded when $0<|a|<1$, and also reversed when $a<0$.

The safest way to interpret a complicated input transformation is the substitution trick. Start from the original signal and introduce one substitution at a time until the desired expression appears, interpreting each step literally. A complementary method is feature tracking: if a recognizable feature of $x(t)$ originally occurs at $t=t_1$, then in $x(at+b)$ the same feature appears where $at+b=t_1$, namely at $t=(t_1-b)/a$.

This is why affine transformations must be read carefully. For example, $x(3t+5)=x(3(t+5/3))$ should be interpreted as compression by a factor of $3$ followed by a shift left by $5/3$. Likewise, $x(-2t+4)=x(-2(t-2))$ is a reversal together with compression by $2$, followed by a shift right by $2$. A feature originally at $t=t_1$ therefore appears at $t=2-t_1/2$.

Comparing inside and outside operations prevents a common mistake. The expressions $x(t)+2$ and $x(t+2)$ both contain `+2`, but they mean entirely different things: the first is a vertical upward shift, while the second is a horizontal left shift. Differentiation and integration belong to the vertical side of this comparison: differentiation emphasizes rapid change, whereas integration accumulates area.

---

Flashcards for this section are as follows:

- What is the difference between dependent-variable and independent-variable signal operations? ::@:: Operations outside the function act on the signal value directly, whereas operations inside the function act on the argument and therefore reshape the time axis.
- What do $x(t-t_0)$ and $x(t+t_0)$ do geometrically? ::@:: $x(t-t_0)$ delays a signal by shifting it right, whereas $x(t+t_0)$ advances it by shifting it left.
- What does time reversal do? ::@:: $x(-t)$ reflects the waveform across the vertical axis.
- How does time scaling work in $x(at)$? ::@:: If $|a|>1$ it compresses time, if $0<|a|<1$ it expands time, and if $a<0$ it also introduces reversal.
- What is the substitution trick for input transformations? ::@:: Introduce one substitution at a time and interpret each intermediate expression literally until the desired transformed argument is reached.
- If a feature of $x(t)$ occurs at $t=t_1$, where does it appear in $x(at+b)$? ::@:: It appears at $t=(t_1-b)/a$.
- Worked example: How should $x(3t+5)$ be interpreted geometrically? ::@:: Step 1: factor the argument as $3t+5=3(t+5/3)$. <br/> Step 2: the factor $3$ inside compresses time by $3$. <br/> Step 3: the $+5/3$ inside shifts the waveform left by $5/3$. <br/> Step 4: so the transformation is compress, then shift left.
- Worked example: How should $x(-2t+4)$ be interpreted geometrically? ::@:: Step 1: factor the argument as $-2t+4=-2(t-2)$. <br/> Step 2: the negative sign gives time reversal. <br/> Step 3: the magnitude $2$ compresses time by $2$. <br/> Step 4: the $(t-2)$ term shifts the transformed waveform right by $2$.
- Worked example: If a feature of $x(t)$ occurs at $t=t_1$, where does it appear in $x(-2t+4)$? ::@:: Step 1: preserve the feature by solving $-2t+4=t_1$. <br/> Step 2: rearrange to $-2t=t_1-4$. <br/> Step 3: divide by $-2$ to get $t=2-t_1/2$.
- What is the difference between $x(t)+2$ and $x(t+2)$? ::@:: $x(t)+2$ is a vertical upward shift by $2$, whereas $x(t+2)$ is a horizontal shift left by $2$.
- What do differentiation and integration do to a signal conceptually? ::@:: Differentiation emphasizes rapid change, whereas integration accumulates area over time.

## complex numbers and orthogonal decompositions

Complex numbers appear early because oscillatory signals are written naturally with complex exponentials. Any complex number may be written in rectangular form $z=x+jy$ or polar form $z=re^{j\theta}$, where $r=|z|$ is magnitude and $\theta=\arg z$ is phase. Euler's relation $e^{j\theta}=\cos\theta+j\sin\theta$ connects the exponential and trigonometric viewpoints, which is why identities such as $\cos(\omega t)=\frac{e^{j\omega t}+e^{-j\omega t}}{2}$ and $\sin(\omega t)=\frac{e^{j\omega t}-e^{-j\omega t}}{2j}$ are so important.

### atan2 and quadrant-aware phase extraction

When phase is recovered from rectangular coordinates, the robust definition is the two-argument angle function $\operatorname{atan2}(y,x)$.  By definition, $\operatorname{atan2}(y,x)$ returns the principal argument of the vector $(x,y)$ or complex number $x+jy$, typically in the range $(-\pi,\pi]$.  Unlike $\arctan(y/x)$, it uses the signs of both inputs and therefore chooses the correct quadrant and remains meaningful when $x=0$.

In signal and spectrum work, this appears whenever a complex quantity is available in rectangular form.  If $z=x+jy$, then $|z|=\sqrt{x^2+y^2}$ and a robust phase is $\arg z=\operatorname{atan2}(y,x)$.  For Fourier analysis this is used as $\phi(\omega)=\operatorname{atan2}(\Im\{F(\omega)\},\Re\{F(\omega)\})$.  Intuitively, `atan2(y, x)` is "the directed angle from the positive real axis to the point with horizontal coordinate $x$ and vertical coordinate $y$".

The easiest recall cue is argument order plus picture: say "`y`, then `x`" while visualizing rise and run on the complex plane.  If a result from plain $\arctan(y/x)$ disagrees with the expected quadrant from signs, $\operatorname{atan2}$ is the correction mechanism that restores the physically meaningful phase.

---

Flashcards for this section are as follows:

- What is the definition of $\operatorname{atan2}(y,x)$ and what range does it usually return? ::@:: $\operatorname{atan2}(y,x)$ returns the principal argument of the point $(x,y)$ or complex number $x+jy$, usually in $(-\pi,\pi]$.
- What does $\operatorname{atan2}(y,x)$ do that $\arctan(y/x)$ cannot do reliably? ::@:: It uses the signs of both $x$ and $y$ to select the correct quadrant and still works when $x=0$, whereas $\arctan(y/x)$ only sees a ratio and loses quadrant information.
- How is $\operatorname{atan2}$ interpreted geometrically in complex-number language? ::@:: It is the directed angle from the positive real axis to the vector ending at $(x,y)$, i.e., the phase of $x+jy$.
- For a Fourier transform written as $F(\omega)=R(\omega)+jX(\omega)$, what is the robust phase-extraction formula? ::@:: $\phi(\omega)=\operatorname{atan2}(X(\omega),R(\omega))=\operatorname{atan2}(\Im\{F(\omega)\},\Re\{F(\omega)\})$.
- What intuitive recall cue helps avoid argument-order mistakes in $\operatorname{atan2}$? ::@:: Remember "`y` first, `x` second" and picture vertical over horizontal coordinates in the complex plane.
- Worked example: For $z=-1+j\sqrt{3}$, why is $\arg z$ correctly found by $\operatorname{atan2}(\sqrt{3},-1)$ rather than plain $\arctan(-\sqrt{3})$? ::@:: The signs ($x<0$, $y>0$) place $z$ in quadrant II. <br/> Plain $\arctan(y/x)$ gives only a reference angle and cannot preserve the quadrant by itself. <br/> $\operatorname{atan2}(\sqrt{3},-1)$ returns the correct principal angle in quadrant II.

The same lecture also uses decomposition as an organizing idea. A periodic signal may be written as the sum of a DC part and an AC part. If $x(t)=x_{\mathrm{DC}}+x_{\mathrm{AC}}(t)$, where $x_{\mathrm{DC}}$ is the average over one period and $x_{\mathrm{AC}}$ has zero mean, then the average power splits into a DC part plus an AC part. The cross term vanishes because the AC component has zero average, so the DC and AC parts are orthogonal under the averaging integral.

An analogous split holds for even and odd parts. Every signal can be written as $x(t)=x_e(t)+x_o(t)$ with $x_e(t)=\frac{x(t)+x(-t)}{2}$ and $x_o(t)=\frac{x(t)-x(-t)}{2}$. Over a symmetric interval, the cross term in the power integral vanishes because the product of an even function and an odd function is odd. This is the symmetry-based analogue of the DC-AC decomposition.

Complex-valued signals admit a third decomposition into real and imaginary parts. Writing $x(t)=x_R(t)+jx_I(t)$ with $x_R(t)=\frac{x(t)+x^*(t)}{2}$ and $x_I(t)=\frac{x(t)-x^*(t)}{2j}$ yields $|x(t)|^2=x_R^2(t)+x_I^2(t)$, so power or energy also splits additively into orthogonal components. The geometric intuition is the same as in the complex plane: the real and imaginary axes are perpendicular directions.

Worked examples make the pattern concrete. If $x(t)=1+\sin t$, then the DC part is $1$, the AC part is $\sin t$, and the average power is $1+1/2=3/2$. The same signal also has even part $1$ and odd part $\sin t$, so the even-odd power split gives the same result. For $x(t)=\cos t+j\sin t$, the real-part power is $1/2$, the imaginary-part power is $1/2$, and the total power is $1$.

---

Flashcards for this section are as follows:

- How may a complex number be written in rectangular and polar forms? ::@:: It may be written as $z=x+jy$ in rectangular form or $z=re^{j\theta}$ in polar form.
- In the polar form $z=re^{j\theta}$, what do $r$ and $\theta$ represent? ::@:: $r=|z|$ is the magnitude and $\theta=\arg z$ is the phase.
- What is Euler's relation? ::@:: It is $e^{j\theta}=\cos\theta+j\sin\theta$.
- How can $\cos(\omega t)$ be written using complex exponentials? ::@:: $\cos(\omega t)=\frac{e^{j\omega t}+e^{-j\omega t}}{2}$.
- How can $\sin(\omega t)$ be written using complex exponentials? ::@:: $\sin(\omega t)=\frac{e^{j\omega t}-e^{-j\omega t}}{2j}$.
- What function should be used for quadrant-aware phase extraction from rectangular coordinates? ::@:: Use $\operatorname{atan2}(y,x)$, which returns the principal angle using the signs of both coordinates.
- Why is $\operatorname{atan2}$ safer than $\arctan(y/x)$ in signal-processing phase calculations? ::@:: Because $\operatorname{atan2}$ preserves quadrant and handles $x=0$, while $\arctan(y/x)$ loses quadrant information.
- How can a periodic signal be decomposed into DC and AC parts? ::@:: It can be written as a DC part plus an AC part, where the AC part has zero mean.
- For a periodic signal, how is the DC component obtained? ::@:: It is the average of the signal over one period.
- Why does the DC-AC cross term vanish in the power split? ::@:: The AC component has zero average over one period, so the mixed term integrates to zero.
- What is the formula for the even part of a signal? ::@:: It is $x_e(t)=\frac{x(t)+x(-t)}{2}$.
- What is the formula for the odd part of a signal? ::@:: It is $x_o(t)=\frac{x(t)-x(-t)}{2}$.
- Why does the even-odd cross term vanish in the power split? ::@:: Over a symmetric interval, the product of an even function and an odd function is odd, so its integral is zero.
- How are the real and imaginary parts of a complex signal obtained from conjugation? ::@:: They satisfy $x_R(t)=\frac{x(t)+x^*(t)}{2}$ and $x_I(t)=\frac{x(t)-x^*(t)}{2j}$.
- Why does the power split additively into real and imaginary parts? ::@:: Because $|x(t)|^2=x_R^2(t)+x_I^2(t)$, so the real and imaginary parts contribute on orthogonal axes.
- Worked example: Given $x(t)=1+\sin t$, what are its DC part, AC part, and average power? ::@:: Step 1: the average of $x(t)$ over one period is $1$, so the DC part is $1$. <br/> Step 2: subtract the average to get the AC part $\sin t$. <br/> Step 3: compute power as $1^2+\text{avg}(\sin^2 t)=1+1/2=3/2$.
- Worked example: Given $x(t)=1+\sin t$, what are its even part, odd part, and power split? ::@:: Step 1: compute $x_e(t)=\tfrac{x(t)+x(-t)}{2}=\tfrac{1+\sin t+1-\sin t}{2}=1$. <br/> Step 2: compute $x_o(t)=\tfrac{x(t)-x(-t)}{2}=\tfrac{1+\sin t-(1-\sin t)}{2}=\sin t$. <br/> Step 3: the cross term vanishes, so the power split is $P_e+P_o=1+1/2=3/2$.
- Worked example: Given $x(t)=\cos t+j\sin t$, what are the real-part power, imaginary-part power, and total power? ::@:: Step 1: the real part is $\cos t$, whose average power is $1/2$. <br/> Step 2: the imaginary part is $\sin t$, whose average power is also $1/2$. <br/> Step 3: add the orthogonal contributions to get total power $1/2+1/2=1$.

## discrete-time sequences and periodicity

A discrete-time signal is a sequence indexed by integers, so it must be read as a sample-by-sample object rather than as a continuously defined waveform. Its periodicity condition is therefore stricter than the continuous-time one: the period itself must be a positive integer shift in the index. This is why sampling can change apparent periodicity and why discrete-time sinusoidal sequences need an arithmetic rationality test instead of the continuous-time "every sinusoid is periodic" rule.

In ELEC 2100, the detailed treatment of representation methods, support patterns, unit sample and unit step sequences, rectangular windows, ramps, one-sided exponentials, discrete-time sinusoids, and complex exponential sequences is centralized in [`discrete-time signal`](discrete-time%20signal.md). That topic note also holds the main discrete-time periodicity examples so the material has one durable home instead of being duplicated across multiple notes.

---

Flashcards for this section are as follows:

- What is the key conceptual difference between a discrete-time signal and a continuous-time signal? ::@:: A discrete-time signal is indexed sample by sample by integers, whereas a continuous-time signal is defined over a continuous independent variable.
- Why is discrete-time periodicity stricter than continuous-time periodicity? ::@:: Continuous-time periodicity allows any positive real period, whereas discrete-time periodicity requires a positive integer shift in the sample index.
- Why can sampling change apparent periodicity? ::@:: Sampling may convert a continuous-time waveform into a sequence whose values satisfy a different repetition pattern, or even collapse it into a much simpler sequence.
- Where is the detailed ELEC 2100 treatment of common discrete-time signals centralized? ::@:: It is centralized in [`discrete-time signal`](discrete-time%20signal.md), which collects the representation methods, standard signal families, and periodicity examples in one durable note.
