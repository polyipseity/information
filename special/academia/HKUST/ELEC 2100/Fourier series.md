---
aliases:
  - CT Fourier series
  - ELEC 2100 Fourier series
  - ELEC 2100 continuous-time Fourier series
  - ELEC2100 Fourier series
  - Fourier series
  - HKUST ELEC 2100 Fourier series
  - continuous-time Fourier series
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/Fourier_series
  - language/in/English
---

# Fourier series

- HKUST ELEC 2100

<!-- check: ignore-file[two_sided_calc_warning]: concept-focused prompts intentionally use descriptive wording rather than repeating every symbol on the left-hand side -->

---

Fourier series decomposes a periodic signal into harmonically related sinusoids or complex exponentials, displaying the result as a discrete spectrum. It reveals how coefficient patterns reflect symmetry, bandwidth, and approximation quality. Together with the Fourier transform, it forms the Fourier analysis framework.

This note covers periodic continuous-time signals. For aperiodic signals, see [Fourier transform](Fourier%20transform.md). For discrete sequences, see [discrete-time Fourier transform](discrete-time%20Fourier%20transform.md) or [discrete Fourier transform](discrete%20Fourier%20transform.md) for finite-record computation.

---

Flashcards for this section are as follows:

- What core problem does the Fourier series note solve in ELEC 2100? ::@:: It decomposes a continuous-time periodic signal into harmonically related sinusoidal or complex-exponential components so the periodic waveform can be analyzed and reconstructed from its line spectrum. <!--SR:!fsrs,2027-09-16T00:00:00.000Z,394,394.37099029,1,2,7,0,0,2026-08-18T00:00:00.000Z!fsrs,2027-06-03T00:00:00.000Z,304,304.30256839,1,2,7,0,0,2026-08-03T00:00:00.000Z-->
- Why is the Fourier-series viewpoint useful beyond formula manipulation? ::@:: It turns waveform shape into a structured list of frequency components, which makes symmetry, bandwidth, harmonic content, and physical interpretation easier to see. <!--SR:!fsrs,2027-06-18T00:00:00.000Z,317,317.09832588,1,2,7,0,0,2026-08-05T00:00:00.000Z!fsrs,2027-09-16T00:00:00.000Z,394,394.37099029,1,2,7,0,0,2026-08-18T00:00:00.000Z-->
- How should this note be positioned among the four main Fourier descriptions? ::@:: This note covers the continuous-time periodic case. The Fourier transform handles aperiodic signals, the DTFT handles general sequences on a continuous digital-frequency axis, and the DFT handles finite-record data on a finite frequency grid. <!--SR:!fsrs,2027-07-05T00:00:00.000Z,330,329.81882824,1,2,7,0,0,2026-08-09T00:00:00.000Z!fsrs,2027-09-30T00:00:00.000Z,407,407.37620449,1,2,7,0,0,2026-08-19T00:00:00.000Z-->

## spectrum concept and frequency-domain viewpoint

Many physical systems are frequency-selective: vocal tracts, ears, communication channels, resonators, and musical instruments respond differently to different oscillation rates. A time waveform shows how a signal evolves; a spectrum shows which oscillatory components are present and how strong they are.

A periodic waveform can be redescribed as a collection of spectral lines in frequency. The time picture emphasizes shape and switching; the frequency picture emphasizes harmonic content, dominant bands, and phase relationships. Neither is more "real"; they are two coordinate systems for the same signal.

For a periodic signal with period $T$, the fundamental angular frequency is $\omega_0=2\pi/T$, and every Fourier-series component appears at an integer multiple $k\omega_0$. The spectrum is a line spectrum, not a continuous curve. Periodicity forces the allowed frequencies onto a harmonic lattice.

In exponential notation $f(t)=\sum_{k=-\infty}^{\infty}F_k e^{jk\omega_0 t}$, each coefficient $F_k$ corresponds to the impulse $2\pi F_k\,\delta(\omega-k\omega_0)$ in the Fourier transform. The full transform is $F(\omega)=2\pi\sum_{k=-\infty}^{\infty}F_k\delta(\omega-k\omega_0)$.

Two standard plotting conventions differ in axis choice and $2\pi$ placement:

__Coefficient plot:__ $F_k$ on the y-axis, harmonic number $k$ on the x-axis. No $2\pi$ factors.

__Transform-style line spectrum:__ $|2\pi F_k|$ on the y-axis, angular frequency $\omega=k\omega_0$ on the x-axis. The $2\pi$ is included in the line weight.

__Phase:__ Both representations show phase similarly. In the coefficient plot, show $\angle F_k$ versus $k$. In the frequency plot, show $\angle F_k$ versus $\omega=k\omega_0$ (the $2\pi$ factor does not change the angle).

__Dirac-delta notation (alternative):__ One can also plot $F_k\,\delta(\omega-k\omega_0)$ without the extra $2\pi$ factor. This is nonstandard for Fourier-series analysis because it adds notational confusion; the harmonic-index plot is preferred.

Musical examples illustrate why Fourier series matters in practice. A pure tone is close to one dominant sinusoid; a richer note contains a fundamental plus harmonics. The fundamental sets the perceived pitch; harmonic amplitudes and phases shape the timbre. Two instruments can play the same note yet sound different because their harmonic recipes differ.

Amplitude and phase should be kept distinct. The amplitude spectrum records how large each harmonic is. The phase spectrum records how each harmonic is shifted. Amplitude gives the coarse shape of a waveform, but phase alignment matters for reconstruction. Two spectra with the same magnitudes but different phases can produce very different waveforms.

Periodic signals give discrete spectral lines (Fourier series). Aperiodic signals give continuous spectra (Fourier transform). The second note builds that bridge; this note focuses on the periodic side.

---

Flashcards for this section are as follows:

- Why is frequency-domain analysis useful in the first place? ::@:: Because many physical systems are frequency-selective, so a spectrum makes dominant oscillatory components, passbands, harmonics, and resonant behavior easier to see than a waveform alone.
- What is the difference between a waveform and a spectrum? ::@:: A waveform emphasizes how the signal evolves in time, whereas a spectrum emphasizes which frequency components are present and how strongly they contribute.
- Why is the spectrum of a periodic signal discrete? ::@:: If a signal repeats with period $T$, its allowed Fourier-series frequencies are locked to integer multiples of the fundamental frequency $\omega_0=2\pi/T$, so the spectrum becomes a line spectrum.
- In exponential Fourier-series notation, what Fourier-transform spectral line corresponds to one coefficient $F_k$? ::@:: It corresponds to the impulse $2\pi F_k\,\delta(\omega-k\omega_0)$, where $\omega_0=2\pi/T$. So the full periodic-signal transform is $F(\omega)=2\pi\sum_k F_k\delta(\omega-k\omega_0)$.
- When sketching the spectrum of a periodic signal, what is the difference between a Fourier-series coefficient plot and a Fourier-transform-style line spectrum? ::@:: A Fourier-series coefficient plot is indexed by harmonic number $k$ and shows the list $F_k$, whereas a Fourier-transform-style line spectrum is indexed by angular frequency $\omega$ and shows impulses $2\pi F_k\,\delta(\omega-k\omega_0)$.
- What do the fundamental frequency and harmonics mean physically for a periodic signal? ::@:: The fundamental gives the base repetition rate, while the harmonics are integer-multiple frequency components that refine the waveform shape.
- In musical interpretation, what do the fundamental and harmonic amplitudes control? ::@:: The fundamental mainly sets pitch, while the harmonic amplitudes and phases shape timbre and waveform detail.
- What is the difference between amplitude spectrum and phase spectrum? ::@:: The amplitude spectrum shows how large each harmonic component is, whereas the phase spectrum shows the relative phase shift of each component.
- Why can two signals with the same amplitude spectrum still look different in time? ::@:: Because phase alignment changes how the harmonic components add together, so the reconstructed waveform depends on phase as well as magnitude.
- What are the two standard ways to plot a Fourier-series spectrum? ::@:: __Coefficient plot__ (preferred): $F_k$ versus harmonic index $k$. __Transform-style plot__: $|2\pi F_k|$ versus angular frequency $\omega=k\omega_0$. Same information, different axis variables and $2\pi$ placement.

## orthogonal decomposition, completeness, and Parseval's theorem

The mathematical backbone of Fourier series is orthogonal decomposition. Just as a vector can be projected onto orthogonal basis directions, a signal can be projected onto orthogonal basis functions. Over one period $T$, the standard inner product is $\langle f,g\rangle=\frac{1}{T}\int_{t_0}^{t_0+T} f(t)g^*(t)\,dt$.

Two functions are orthogonal when this inner product is zero. Orthogonality means extracting one coefficient does not contaminate another. This is Hilbert-space geometry in miniature: signals live in an inner-product space (typically a subspace of $L^2[0,T]$), and orthogonal basis functions are perpendicular coordinate axes.

If one approximates a signal by an orthogonal family $\{g_r(t)\}$ as $f(t)\approx \sum_r c_r g_r(t)$, the mean square error is minimized by the projection formula $c_m=\frac{\langle f,g_m\rangle}{\langle g_m,g_m\rangle}$. If the basis is normalized, the denominator is $1$ and the coefficient is just the inner product.

The real periodic Fourier basis consists of $1$, $\cos(k\omega_0 t)$, and $\sin(k\omega_0 t)$ for $k\ge 1$. It is orthogonal over any full period, but not orthonormal: $\int_0^T 1\cdot 1\,dt=T$, $\int_0^T \cos^2(k\omega_0 t)dt=T/2$, and $\int_0^T \sin^2(k\omega_0 t)dt=T/2$. Think of the constant, cosines, and sines as perpendicular directions: one DC axis, one cosine axis per harmonic, and one sine axis per harmonic.

The trigonometric orthogonality proof uses product-to-sum identities. Over $[0,T]$ with $\omega_0=2\pi/T$:

$\sin(n\omega_0 t)\sin(m\omega_0 t)=\frac12\big[\cos((n-m)\omega_0 t)-\cos((n+m)\omega_0 t)\big]$

$\cos(n\omega_0 t)\cos(m\omega_0 t)=\frac12\big[\cos((n-m)\omega_0 t)+\cos((n+m)\omega_0 t)\big]$

$\sin(n\omega_0 t)\cos(m\omega_0 t)=\frac12\big[\sin((n+m)\omega_0 t)+\sin((n-m)\omega_0 t)\big]$

When $n\neq m$, every resulting sine or cosine completes an integer number of cycles over $[0,T]$, so the integral is $0$. When $n=m$, the same-type integrals give $\int_0^T \sin^2(n\omega_0 t)dt=T/2$ and $\int_0^T \cos^2(n\omega_0 t)dt=T/2$.

The complex Fourier basis $\{e^{jk\omega_0 t}\}_{k\in\mathbb{Z}}$ is orthogonal because $\int_0^T e^{jn\omega_0 t}\,e^{-jm\omega_0 t}dt=\int_0^T e^{j(n-m)\omega_0 t}dt$, which equals $T$ when $n=m$ and $0$ when $n\neq m$. The off-diagonal case vanishes because $e^{j(n-m)\omega_0 T}=e^{j2\pi(n-m)}=1$, so the antiderivative's endpoint values cancel.

The real and complex bases describe the same geometry in two styles. The real basis shows cosine and sine as separate coordinates. The complex basis uses one indexed family to handle positive frequencies, negative frequencies, and phase at once. The complex basis is cleaner for operator algebra; the real basis is often cleaner for physical interpretation.

The Fourier basis is complete as well as orthogonal. Completeness means no nonzero signal in the target class is orthogonal to every basis function. In Hilbert-space terms, the orthogonal family spans the relevant subspace, so every signal can be resolved into components along those basis directions.

The conjugate in $\langle f,g\rangle=\frac{1}{T}\int f(t)g^*(t)dt$ is what makes the complex inner product produce real nonnegative norms. Without it, $\langle f,f\rangle$ would not be real and positive, so lengths and energies would not behave correctly.

Parseval's theorem is the energy/power bookkeeping law. For a periodic signal, average power in time equals total power from the coefficients. In trigonometric form:

$P=\frac{1}{T}\int_{t_0}^{t_0+T}|f(t)|^2dt=a_0^2+\frac12\sum_{k=1}^{\infty}(a_k^2+b_k^2)$

In exponential form: $P=\sum_{k=-\infty}^{\infty}|F_k|^2$.

Orthogonality removes cross terms, so total average power is the sum of separate harmonic powers. The exponential form is most natural because it adds the two-sided spectral-line powers $|F_k|^2$ directly.

The $1/2$ in the trigonometric form comes from folding two conjugate spectral lines into one real harmonic. A nonzero real harmonic appears as a pair at $+k\omega_0$ and $-k\omega_0$. If the real harmonic has amplitude $c_k$, each complex line has $|F_k|=c_k/2$, so total power is $(c_k/2)^2+(c_k/2)^2=c_k^2/2$. Since $c_k^2=a_k^2+b_k^2$, the contribution is $(a_k^2+b_k^2)/2$.

---

Flashcards for this section are as follows:

- What is the key mathematical idea behind Fourier series? ::@:: It is orthogonal decomposition: represent a signal by projecting it onto mutually orthogonal basis functions.
- What is a standard inner product for periodic signal decomposition over one period $T$? ::@:: A standard choice is $\langle f,g\rangle=\frac{1}{T}\int_{t_0}^{t_0+T} f(t)g^*(t)\,dt$.
- When are two signal functions orthogonal? ::@:: They are orthogonal when their inner product is zero, meaning one basis direction does not interfere with the extraction of the other.
- Why is orthogonality so useful for signal decomposition? ::@:: Because it separates the basis directions, so each coefficient can be extracted independently without contamination from the others.
- How should you picture the real trigonometric basis geometrically? ::@:: Think of $1$, $\cos(k\omega_0 t)$, and $\sin(k\omega_0 t)$ as perpendicular coordinate axes in signal space: one DC axis and, for each harmonic index $k$, one cosine axis and one sine axis.
- Given an orthogonal family $\{g_r\}$, what coefficient minimizes the mean square error in the approximation $f\approx\sum_r c_r g_r$? ::@:: The minimizing coefficient is $c_m=\langle f,g_m\rangle/\langle g_m,g_m\rangle$ because differentiating the mean square error with respect to $c_m$ produces the orthogonal projection formula.
- What is the projection coefficient formula conceptually? ::@:: It is the function-space analogue of vector projection: measure how much of the signal points along one orthogonal basis direction, then divide by that direction's own size if the basis is not normalized.
- Worked example: Prove over one full period $[0,T]$ with $\omega_0=2\pi/T$ that $\{1,\cos(k\omega_0 t),\sin(k\omega_0 t)\}_{k\ge 1}$ is an orthogonal real function set. ::@:: Step 1: use product-to-sum identities: $\sin n\sin m=\frac12[\cos((n-m)\omega_0 t)-\cos((n+m)\omega_0 t)]$, $\cos n\cos m=\frac12[\cos((n-m)\omega_0 t)+\cos((n+m)\omega_0 t)]$, and $\sin n\cos m=\frac12[\sin((n+m)\omega_0 t)+\sin((n-m)\omega_0 t)]$. <br/> Step 2: when $n\neq m$, every resulting sine or cosine completes an integer number of cycles over $[0,T]$, so each integral is $0$. <br/> Step 3: when $n=m$, the same-type integrals reduce to $\int_0^T \sin^2(n\omega_0 t)dt=T/2$ or $\int_0^T \cos^2(n\omega_0 t)dt=T/2$. <br/> Step 4: also $\int_0^T \sin(k\omega_0 t)dt=0$ and $\int_0^T \cos(k\omega_0 t)dt=0$ for $k\ge 1$, so the constant function is orthogonal to all nonzero harmonics. <br/> Step 5: therefore the trigonometric set is orthogonal over one period.
- What does it mean for an orthogonal function set to be complete? ::@:: No nonzero signal in the target class is orthogonal to every basis function. In other words, the span of the basis already fills the whole signal subspace, so every admissible signal can be decomposed into those orthogonal components.
- What are the two main Fourier bases used in the lecture? ::@:: The real basis uses $1$, $\cos(k\omega_0 t)$, and $\sin(k\omega_0 t)$, while the complex basis uses $e^{jk\omega_0 t}$ for all integers $k$.
- What is the complex orthogonal function set and why is it attractive? ::@:: It is the set $\{e^{jk\omega_0 t}\}_{k\in\mathbb{Z}}$, and it is attractive because one indexed family simultaneously handles positive frequencies, negative frequencies, and phase, so operator algebra becomes cleaner.
- Worked example: Prove over $[0,T]$ with $\omega_0=2\pi/T$ that $\{e^{jk\omega_0 t}\}_{k\in\mathbb{Z}}$ is an orthogonal complex function set. ::@:: Step 1: take two basis functions $g_n(t)=e^{jn\omega_0 t}$ and $g_m(t)=e^{jm\omega_0 t}$. <br/> Step 2: compute the inner product integral $\int_0^T g_n(t)g_m^*(t)dt=\int_0^T e^{j(n-m)\omega_0 t}dt$. <br/> Step 3: if $n=m$, the integrand is $1$, so the integral is $T$. <br/> Step 4: if $n\neq m$, then the antiderivative gives $\frac{e^{j(n-m)\omega_0 T}-1}{j(n-m)\omega_0}$, and since $\omega_0T=2\pi$, we get $e^{j2\pi(n-m)}=1$, so the numerator is $0$. <br/> Step 5: therefore the integral is $0$ when $n\neq m$, so the set is orthogonal.
- How should you compare the real and complex orthogonal bases? ::@:: The real basis separates cosine and sine into visually meaningful coordinates, while the complex basis compresses them into one two-sided exponential family that is algebraically cleaner for shifts, derivatives, and phase.
- Why does the complex inner product use conjugation? ::@:: The conjugate makes $\langle f,f\rangle=\frac{1}{T}\int |f(t)|^2dt$ real and nonnegative, so norms, energies, and projections behave correctly in complex signal space.
- Why is it helpful to mention Hilbert spaces here at all? ::@:: Because the whole story is geometry in an inner-product space of signals: orthogonality, projection, norm, completeness, and Parseval are the signal-space analogues of perpendicular vectors, shadows, lengths, spanning sets, and Pythagorean energy addition.
- What is Parseval's theorem for a periodic signal in trigonometric form? ::@:: It states $P=\frac{1}{T}\int_{t_0}^{t_0+T}|f(t)|^2dt=a_0^2+\frac12\sum_{k=1}^{\infty}(a_k^2+b_k^2)=a_0^2+\frac12\sum_{k=1}^{\infty}c_k^2$.
- What is Parseval's theorem for a periodic signal in exponential form? ::@:: It states $P=\sum_{k=-\infty}^{\infty}|F_k|^2$.
- Why does Parseval's theorem work intuitively? ::@:: Because the harmonic directions are orthogonal, the cross terms vanish when you square the expansion and average over one period, so the total power behaves like a Pythagorean sum of harmonic contributions.
- Why is there a factor of $1/2$ in Parseval's theorem for the trigonometric or harmonic form? ::@:: Step 1: a nonzero real harmonic corresponds in the exponential form to two conjugate spectral lines, one at $+k\omega_0$ and one at $-k\omega_0$. <br/> Step 2: folding those two lines into one real harmonic doubles the amplitude description to $c_k=2|F_k|$. <br/> Step 3: naively squaring that doubled amplitude would overcount power, because the real harmonic actually came from two lines rather than one. <br/> Step 4: the true two-line power is $(c_k/2)^2+(c_k/2)^2=c_k^2/2=(a_k^2+b_k^2)/2$. <br/> Step 5: so the factor $1/2$ is the correction required after folding the positive- and negative-frequency pair into one real harmonic.
- Worked example: Why does Parseval split power additively across harmonics? ::@:: Step 1: substitute the orthogonal expansion of $f(t)$ into the average-power integral $P=\frac{1}{T}\int |f(t)|^2dt$. <br/> Step 2: expand the square magnitude into self terms and cross terms. <br/> Step 3: every cross term contains the inner product of two different orthogonal harmonics, so those terms integrate to $0$. <br/> Step 4: only the self terms survive, giving $a_0^2+\frac12\sum_{k\ge 1}(a_k^2+b_k^2)$ in the real form, or $\sum_{k=-\infty}^{\infty}|F_k|^2$ in the complex form. <br/> Step 5: so Parseval is the power version of Pythagoras in signal space.
- Why is the exponential form of Parseval the most natural? ::@:: Because it adds the actual two-sided spectral-line powers $|F_k|^2$ directly, without first folding the positive- and negative-frequency pair into one real harmonic.

## trigonometric Fourier series and harmonic form

For a real periodic signal of period $T$, the trigonometric Fourier series is:

$f(t)=a_0+\sum_{k=1}^{\infty}\big[a_k\cos(k\omega_0 t)+b_k\sin(k\omega_0 t)\big]$ with $\omega_0=\frac{2\pi}{T}$.

Each harmonic adds one more layer of shape refinement to the DC term.

The coefficient formulas come directly from orthogonality:

$a_0=\frac{1}{T}\int_{t_0}^{t_0+T} f(t)\,dt$, $a_k=\frac{2}{T}\int_{t_0}^{t_0+T} f(t)\cos(k\omega_0 t)\,dt$, $b_k=\frac{2}{T}\int_{t_0}^{t_0+T} f(t)\sin(k\omega_0 t)\,dt$.

These are projection coefficients: multiply by the target basis function, integrate over one period, and orthogonality isolates the desired term.

The $a_0$ term is special. It is the DC component (average value), not an oscillation. Zero frequency is its own negative, unlike every nonzero harmonic $\pm k\omega_0$. The two-sided frequency picture has $\ldots,-2\omega_0,-\omega_0,0,\omega_0,2\omega_0,\ldots$. For a real signal, each nonzero pair $\pm k\omega_0$ collapses into one real harmonic because $F_{-k}=F_k^*$, so the pair is encoded together in $a_k$ and $b_k$. But zero frequency has no separate negative-frequency partner, so the DC term stands alone and is not doubled when folding a two-sided spectrum into a one-sided description.

Dirichlet conditions are sufficient conditions for convergence to the intended periodic signal. They rule out signals that are too singular, too jumpy, or too oscillatory within one period.

Over $[t_0,t_0+T]$: $f$ must be absolutely integrable, have only finitely many finite discontinuities, and have only finitely many local maxima and minima. These are sufficient rather than necessary, but they cover common piecewise smooth periodic waveforms.

__Condition 1 (absolute integrability):__ $\int_{t_0}^{t_0+T}|f(t)|\,dt<\infty$. Example: any bounded piecewise-continuous waveform (square wave, triangular wave) has finite area on a finite interval. Counterexample: the period-1 extension of $f(t)=1/t$ on $0<t\le 1$, since $\int_0^1 \frac{1}{t}dt=\infty$.

__Condition 2 (finite jumps):__ Within one period, the number of discontinuity points must be finite, with only finite jumps allowed. Example: a rectangular wave has only a few jumps per period. Counterexample: a staircase whose step widths and heights keep halving (e.g., jumps at $4,6,7,7.5,\ldots$ within period $8$); its area stays finite but discontinuity count is infinite.

__Condition 3 (finite extrema):__ Within one period, the number of local maxima and minima must be finite. Example: $\sin(2\pi t/T)$ has one max and one min per period. Counterexample: the period-1 extension of $f(t)=t\sin(2\pi/t)$ on $0<t\le 1$ with $f(0)=0$; it oscillates infinitely often near $t=0$.

Together, the three conditions exclude non-integrable singularity, infinitely many jumps, and infinitely many oscillations.

Under those conditions, the Fourier series converges pointwise. If $f$ is continuous at $t_0$, then $S_N(t_0)\to f(t_0)$ as $N\to\infty$. If $f$ has a jump at $t_0$, the series converges to the midpoint $\frac{f(t_0^-)+f(t_0^+)}{2}$.

The midpoint rule makes sense because a Fourier series is built from smooth sinusoids. Near a jump, the left and right oscillatory approximations balance each other, and the symmetric kernel behind partial sums averages the two sides. For example, a square wave jumping from $-1$ to $1$ converges there to $0$, the midpoint.

The trigonometric form can be merged into a cosine-phase (harmonic) form: $a_k\cos(k\omega_0 t)+b_k\sin(k\omega_0 t)=c_k\cos(k\omega_0 t+\phi_k)$, where $c_k=\sqrt{a_k^2+b_k^2}$ and $\phi_k=\operatorname{atan2}(-b_k,a_k)$. Equivalently, $a_k=c_k\cos\phi_k$ and $b_k=-c_k\sin\phi_k$. This form puts each harmonic into the intuitive language of amplitude plus phase.

The normalized pair $(a_k/c_k,-b_k/c_k)$ lies on the unit circle because $(a_k/c_k)^2+(-b_k/c_k)^2=1$. So $\phi_k$ is the angle of the harmonic phasor, while $c_k$ is its length. In other words, $(a_k,b_k)$ are rectangular coordinates, while $(c_k,\phi_k)$ are polar coordinates for the same harmonic.

---

Flashcards for this section are as follows:

- What is the trigonometric Fourier series of a real periodic signal? ::@:: It is $f(t)=a_0+\sum_{k=1}^{\infty}[a_k\cos(k\omega_0 t)+b_k\sin(k\omega_0 t)]$ with $\omega_0=2\pi/T$.
- What are the trigonometric Fourier-series coefficient formulas? ::@:: They are $a_0=\frac{1}{T}\int f(t)dt$, $a_k=\frac{2}{T}\int f(t)\cos(k\omega_0 t)dt$, and $b_k=\frac{2}{T}\int f(t)\sin(k\omega_0 t)dt$ over any full period.
- Why is $a_0$ special in the trigonometric Fourier series? ::@:: The full two-sided picture has $\ldots,-\omega_0,0,\omega_0,\ldots$. For a real signal, each nonzero pair $\pm k\omega_0$ collapses into one real harmonic ($F_{-k}=F_k^*$). But zero frequency has no negative-frequency partner, so the DC term stands alone and is not doubled.
- What do Dirichlet conditions guarantee? ::@:: They ensure convergence for piecewise smooth periodic signals: absolute integrability, finitely many finite jumps, and finitely many extrema per period. At continuity points the series converges to $f(t_0)$; at jumps it converges to the midpoint $\frac{f(t_0^-)+f(t_0^+)}{2}$.
- What is Dirichlet Condition 1? ::@:: Absolute integrability over one period: $\int_{t_0}^{t_0+T}|f(t)|dt<\infty$. Example: bounded periodic waveforms. Counterexample: period-1 $f(t)=1/t$.
- What is Dirichlet Condition 2? ::@:: Finitely many finite jumps per period. Example: rectangular wave. Counterexample: staircase with infinitely many accumulating jump points.
- What is Dirichlet Condition 3? ::@:: Finitely many local maxima and minima per period. Example: $\sin(2\pi t/T)$. Counterexample: period-1 $f(t)=t\sin(2\pi/t)$.
- Why does the Fourier series converge to the midpoint at a jump? ::@:: A Fourier partial sum is built from smooth sinusoids, so near a jump the oscillations from both sides balance each other, and the symmetric partial-sum kernel averages the two sides. The limiting value becomes the midpoint of the jump.
- What is the cosine-phase form of one harmonic? ::@:: $a_k\cos(k\omega_0 t)+b_k\sin(k\omega_0 t)=c_k\cos(k\omega_0 t+\phi_k)$.
- Given $a_k$ and $b_k$, how do you get $c_k$ and $\phi_k$? ::@:: $c_k=\sqrt{a_k^2+b_k^2}$, $\phi_k=\operatorname{atan2}(-b_k,a_k)$. Intuitively, $(a_k,-b_k)$ is the rectangular-coordinate phasor, $c_k$ is its length, and $\phi_k$ is its angle.
- Why does Gibbs phenomenon not contradict the minimum-mean-square property? ::@:: Because minimum mean square error minimizes the global average $\frac{1}{T}\int_0^T |f(t)-f_N(t)|^2dt$, whereas Gibbs overshoot is a local pointwise effect concentrated near a jump. The approximation can be globally optimal in mean-square error while still showing visible ringing near discontinuities.
- Why is the cosine-phase form more intuitive than separate cosine-sine coefficients? ::@:: Because it describes each harmonic directly by amplitude, frequency, and phase shift.
- Worked example: Given $f(t)=\sin(\omega_0 t)+3\cos(\omega_0 t)$, what are the merged first-harmonic amplitude and phase? ::@:: Step 1: identify $a_1=3$ and $b_1=1$, so $a_1\cos(\omega_0 t)+b_1\sin(\omega_0 t)=3\cos(\omega_0 t)+\sin(\omega_0 t)$. <br/> Step 2: compute the amplitude $c_1=\sqrt{a_1^2+b_1^2}=\sqrt{10}$. <br/> Step 3: compute the normalized coordinates $a_1/c_1=3/\sqrt{10}$ and $-b_1/c_1=-1/\sqrt{10}$. <br/> Step 4: therefore $\cos\phi_1=3/\sqrt{10}$ and $\sin\phi_1=-1/\sqrt{10}$, so the quadrant-correct phase is $\phi_1=\operatorname{atan2}(-1,3)$ (equivalently $-\arctan(1/3)$ in this specific quadrant-IV case). <br/> Step 5: hence $3\cos(\omega_0 t)+\sin(\omega_0 t)=\sqrt{10}\cos\big(\omega_0 t+\operatorname{atan2}(-1,3)\big)$.
- Worked example: Why does multiplying by $\cos(m\omega_0 t)$ isolate $a_m$? ::@:: Step 1: start from $f(t)=a_0+\sum_{k=1}^{\infty}[a_k\cos(k\omega_0 t)+b_k\sin(k\omega_0 t)]$. <br/> Step 2: multiply both sides by $\cos(m\omega_0 t)$ and integrate over one full period $[0,T]$. <br/> Step 3: this gives $\int_0^T f(t)\cos(m\omega_0 t)dt=a_0\int_0^T \cos(m\omega_0 t)dt+\sum_{k=1}^{\infty}a_k\int_0^T \cos(k\omega_0 t)\cos(m\omega_0 t)dt+\sum_{k=1}^{\infty}b_k\int_0^T \sin(k\omega_0 t)\cos(m\omega_0 t)dt$. <br/> Step 4: orthogonality kills the DC integral, every sine-cosine integral, and every cosine-cosine integral with $k\neq m$. <br/> Step 5: only the $k=m$ cosine term survives, giving $\int_0^T f(t)\cos(m\omega_0 t)dt=a_m\int_0^T \cos^2(m\omega_0 t)dt=a_m(T/2)$. <br/> Step 6: solve for $a_m$ to obtain $a_m=\frac{2}{T}\int_0^T f(t)\cos(m\omega_0 t)dt$. <br/> Step 7: the reason this works is geometric: multiplying by the basis function and integrating computes the projection onto that one orthogonal direction.

## exponential Fourier series, symmetry, and discrete spectra

The exponential Fourier series rewrites the same signal as $f(t)=\sum_{k=-\infty}^{\infty}F_k e^{jk\omega_0 t}$, with $F_k=\frac{1}{T}\int_{t_0}^{t_0+T} f(t)e^{-jk\omega_0 t}\,dt$.

This form is algebraically cleaner: one family $e^{jk\omega_0 t}$ handles positive frequencies, negative frequencies, and phase in one stroke. It is also the cleanest place to state the bridge to the Fourier transform: if the signal is periodic with period $T$, the Fourier transform is $F(\omega)=2\pi\sum_{k=-\infty}^{\infty}F_k\delta(\omega-k\omega_0)$ with $\omega_0=2\pi/T$.

For a real signal, the trigonometric and exponential forms carry the same information. The conversion for $k>0$ is $F_k=\frac{a_k-jb_k}{2}$, $F_{-k}=\frac{a_k+jb_k}{2}$, and $F_0=a_0$. This follows from Euler's formulas: substituting $\cos(k\omega_0 t)=\frac{e^{jk\omega_0 t}+e^{-jk\omega_0 t}}{2}$ and $\sin(k\omega_0 t)=\frac{e^{jk\omega_0 t}-e^{-jk\omega_0 t}}{2j}$ into the trigonometric series groups the coefficient of $e^{jk\omega_0 t}$ into $\frac{a_k-jb_k}{2}$. For a real signal, $F_{-k}=F_k^*$, and recovering $a_k$ and $b_k$ is quick: $a_k=F_k+F_k^*=2\operatorname{Re}F_k$ and $b_k=j(F_k-F_k^*)=-2\operatorname{Im}F_k$.

Single-harmonic examples make the coefficient-to-line-spectrum bridge concrete. For period $T_0=2\pi/\omega_0$:

$\cos(\omega_0 t)$ has only $F_1=F_{-1}=1/2$, so its transform-style spectrum is $\pi\bigl[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)\bigr]$.

$\sin(\omega_0 t)$ has only $F_1=1/(2j)$ and $F_{-1}=-1/(2j)$, so its spectrum is $\frac{\pi}{j}\bigl[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)\bigr]$.

These remind us that Fourier-series coefficients are indexed by $k$, while the transform-style line spectrum is indexed by $\omega$ and carries the extra $2\pi$ factor.

If $F_k=|F_k|e^{j\angle F_k}$, the cosine-phase amplitude is $c_k=2|F_k|$ and the phase is inherited from the complex coefficient.

__Negative frequencies__ are not separate oscillators. They are the conjugate partners needed by the complex representation so the final reconstructed signal is real. For a real signal, $F_k$ and $F_{-k}$ carry the same information in conjugate-symmetric form.

When sketching the spectrum, remember which object is being drawn. The common engineering sketch is the transform-style line spectrum, so impulses at $\omega=\pm k\omega_0$ have weights $2\pi F_{\pm k}$. The $2\pi$ factor scales magnitudes but not phases.

The single-sided spectrum only makes sense for real signals. Since $F_{-k}=F_k^*$, the two-sided spectrum is conjugate symmetric. For magnitude, nonzero negative lines duplicate the positive side, so a single-sided magnitude doubles the nonzero positive lines but leaves DC unchanged. For phase, the negative side is the sign-negated mirror of the positive side, so folding keeps only the positive-frequency phase data with the undoubled DC term.

Symmetry in the time domain gives coefficient shortcuts. Here $T$ is the full period, so $T/2$ is half a cycle.

- __Even signal:__ All sine coefficients vanish ($b_k=0$), exponential coefficients are real and even. An even waveform is mirror-symmetric about $t=0$, so sine (odd) contributions cancel.
- __Odd signal:__ DC and cosine coefficients vanish ($a_0=a_k=0$), exponential coefficients are purely imaginary and odd. An odd waveform changes sign across the origin, so its average is zero and cosine (even) contributions cancel.
- __Half-wave antisymmetry:__ $f(t+T/2)=-f(t)$ gives zero DC and only odd harmonics. After half a period the waveform flips sign, so only harmonics that pick up a minus sign under a $T/2$ shift survive. Odd harmonics do that; even harmonics do not.
- __Half-wave symmetry:__ $f(t+T/2)=f(t)$ gives only even harmonics. The waveform reproduces itself after half a period, so only harmonics that keep the same sign under that shift survive.

The half-wave antisymmetry derivation is short. Start from $f(t+T/2)=-f(t)$ and substitute $f(t)=\sum_k F_k e^{jk\omega_0 t}$. Then $f(t+T/2)=\sum_k F_k(-1)^k e^{jk\omega_0 t}$. Equating with $-\sum_k F_k e^{jk\omega_0 t}$ gives $F_k(-1)^k=-F_k$, so $F_k=0$ for even $k$ (including $k=0$). Only odd harmonics survive.

For half-wave symmetry $f(t+T/2)=f(t)$, the same substitution gives $F_k((-1)^k-1)=0$, forcing $F_k=0$ for odd $k$. Only even harmonics remain.

These rules explain why certain waveforms cannot produce certain spectral ingredients. An even waveform has no odd-function content, so it cannot generate sine coefficients. A half-wave antisymmetric waveform flips sign after half a period, so even harmonics cannot match that pattern.

---

Flashcards for this section are as follows:

- What is the exponential Fourier series of a periodic signal? ::@:: It is $f(t)=\sum_{k=-\infty}^{\infty}F_k e^{jk\omega_0 t}$ with $F_k=\frac{1}{T}\int_{t_0}^{t_0+T} f(t)e^{-jk\omega_0 t}\,dt$. <!--SR:!fsrs,2027-09-30T00:00:00.000Z,407,407.37620449,1,2,7,0,0,2026-08-19T00:00:00.000Z!fsrs,2027-05-29T00:00:00.000Z,313,312.84164192,1,2,7,0,0,2026-07-20T00:00:00.000Z-->
- Why is the exponential Fourier series often algebraically cleaner than the trigonometric form? ::@:: Because one complex-exponential family handles positive frequencies, negative frequencies, and phase in one compact basis. <!--SR:!fsrs,2027-09-24T00:00:00.000Z,403,402.83580244,1,2,7,0,0,2026-08-17T00:00:00.000Z!fsrs,2027-09-30T00:00:00.000Z,407,407.37620449,1,2,7,0,0,2026-08-19T00:00:00.000Z-->
- In the Fourier-transform picture of a periodic signal, what does one exponential Fourier-series coefficient $F_k$ become? ::@:: It becomes the spectral line $2\pi F_k\,\delta(\omega-k\omega_0)$, so the whole periodic-signal transform is $F(\omega)=2\pi\sum_k F_k\delta(\omega-k\omega_0)$ with $\omega_0=2\pi/T$. <!--SR:!fsrs,2027-09-30T00:00:00.000Z,407,407.37620449,1,2,7,0,0,2026-08-19T00:00:00.000Z!fsrs,2027-05-18T00:00:00.000Z,304,304.30256839,1,2,7,0,0,2026-07-18T00:00:00.000Z-->
- How are the exponential and trigonometric coefficients related for a real signal? ::@:: For $k>0$, $F_k=(a_k-jb_k)/2$, $F_{-k}=(a_k+jb_k)/2$, and $F_0=a_0$. <br/> To remember this, write $2\cos(k\omega_0 t)=e^{jk\omega_0 t}+e^{-jk\omega_0 t}$ and $2\sin(k\omega_0 t)=-j\left(e^{jk\omega_0 t}-e^{-jk\omega_0 t}\right)$. These are the signals projected onto by $a_k$ and $b_k$. <br/> To find the coefficient of $e^{jk\omega_0 t}$, find a linear combination such that the signal is projected onto its conjugate $e^{-jk\omega_0 t}$. The coefficient becomes $\frac{a_k-jb_k}{2}$ and the coefficient of $e^{-jk\omega_0 t}$ becomes $\frac{a_k+jb_k}{2}$. <p> For a real signal, $F_{-k}=F_k^*$, so adding the conjugate pair cancels the imaginary sine part and gives $a_k=F_k+F_k^*=2\operatorname{Re}F_k$, while subtracting isolates the sine part and gives $b_k=j(F_k-F_k^*)=-2\operatorname{Im}F_k$. <br/> Intuitively, $a_k$ is recovered by combining the pair so that only the even cosine contribution survives, while $b_k$ is recovered by combining them so that the odd sine contribution survives. <!--SR:!fsrs,2026-12-28T00:00:00.000Z,191,191.3492133,1.98030797,2,6,0,0,2026-06-20T00:00:00.000Z!fsrs,2027-04-26T00:00:00.000Z,287,287.11697064,1,2,7,0,0,2026-07-13T00:00:00.000Z-->
- What are the exponential Fourier-series coefficients and the Fourier-transform-style line spectrum of $\cos(\omega_0 t)$? ::@:: For period $T_0=2\pi/\omega_0$, the only nonzero exponential Fourier-series coefficients are $F_1=F_{-1}=1/2$. <br/> Therefore the Fourier-transform-style periodic spectrum is $2\pi\left[\frac12\delta(\omega-\omega_0)+\frac12\delta(\omega+\omega_0)\right]=\pi\bigl[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)\bigr]$. <!--SR:!fsrs,2027-04-10T00:00:00.000Z,274,274.1280869,1,2,7,0,0,2026-07-10T00:00:00.000Z!fsrs,2027-09-30T00:00:00.000Z,407,407.37620449,1,2,7,0,0,2026-08-19T00:00:00.000Z-->
- What are the exponential Fourier-series coefficients and the Fourier-transform-style line spectrum of $\sin(\omega_0 t)$? ::@:: For period $T_0=2\pi/\omega_0$, the only nonzero exponential Fourier-series coefficients are $F_1=1/(2j)$ and $F_{-1}=-1/(2j)$. <br/> Therefore the Fourier-transform-style periodic spectrum is $2\pi\left[\frac{1}{2j}\delta(\omega-\omega_0)-\frac{1}{2j}\delta(\omega+\omega_0)\right]=\frac{\pi}{j}\bigl[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)\bigr]$. <!--SR:!fsrs,2027-05-18T00:00:00.000Z,304,304.30256839,1,2,7,0,0,2026-07-18T00:00:00.000Z!fsrs,2027-04-21T00:00:00.000Z,283,282.79716409,1,2,7,0,0,2026-07-12T00:00:00.000Z-->
- If $F_k$ is known in polar form, how do you recover the cosine-phase amplitude of harmonic $k$? ::@:: For a real signal the cosine-phase amplitude is $c_k=2|F_k|$ because the positive- and negative-frequency conjugate pair combine into one real harmonic. <!--SR:!fsrs,2027-09-07T00:00:00.000Z,389,389.16804405,1,2,7,0,0,2026-08-14T00:00:00.000Z!fsrs,2027-09-18T00:00:00.000Z,398,398.28771618,1,2,7,0,0,2026-08-16T00:00:00.000Z-->
- Why do negative frequencies appear in the exponential Fourier series? ::@:: They are the conjugate partners needed by the complex representation so that a real time-domain waveform can be reconstructed correctly. <!--SR:!fsrs,2027-05-24T00:00:00.000Z,309,308.57643926,1,2,7,0,0,2026-07-19T00:00:00.000Z!fsrs,2027-09-30T00:00:00.000Z,407,407.37620449,1,2,7,0,0,2026-08-19T00:00:00.000Z-->
- For a real signal, what symmetry relation do the exponential Fourier-series coefficients satisfy? ::@:: They satisfy $F_{-k}=F_k^*$, so the two-sided spectrum is conjugate symmetric. <!--SR:!fsrs,2027-08-25T00:00:00.000Z,377,376.50017085,1,2,7,0,0,2026-08-13T00:00:00.000Z!fsrs,2027-09-16T00:00:00.000Z,394,394.37099029,1,2,7,0,0,2026-08-18T00:00:00.000Z-->
- When plotting the magnitude or phase spectrum of a periodic signal from its exponential Fourier-series coefficients, what quantity is commonly drawn? ::@:: The common engineering sketch uses the Fourier-transform line-spectrum convention, so it draws impulses at $\omega=k\omega_0$ with magnitudes $|2\pi F_k|$. The phases are still the angles of $F_k$, because multiplying by the positive real factor $2\pi$ changes magnitude but not phase. <!--SR:!fsrs,2027-08-19T00:00:00.000Z,372,372.01284157,1,2,7,0,0,2026-08-12T00:00:00.000Z!fsrs,2027-05-18T00:00:00.000Z,304,304.30256839,1,2,7,0,0,2026-07-18T00:00:00.000Z-->
- Why does the single-sided spectrum only make sense for a real signal? ::@:: Because only a real signal guarantees the conjugate symmetry $F_{-k}=F_k^*$ needed to fold the negative-frequency side onto the positive-frequency side. <br/> In magnitude, the nonzero positive lines are doubled after folding, while the DC line is not doubled because it has no distinct negative counterpart. <br/> In phase, the negative side is the sign-negated mirror of the positive side, so one keeps only the positive-frequency phase data together with the undoubled DC term. <!--SR:!fsrs,2027-09-13T00:00:00.000Z,394,393.73185196,1,2,7,0,0,2026-08-15T00:00:00.000Z!fsrs,2027-09-29T00:00:00.000Z,407,407.37620449,1,2,7,0,0,2026-08-18T00:00:00.000Z-->
- What happens to the Fourier series of an even signal? ::@:: All sine coefficients vanish, so $b_k=0$, and the exponential coefficients become real and even. <!--SR:!fsrs,2027-08-14T00:00:00.000Z,368,367.51741581,1,2,7,0,0,2026-08-11T00:00:00.000Z!fsrs,2027-04-13T00:00:00.000Z,278,278.46760619,1,2,7,0,0,2026-07-09T00:00:00.000Z-->
- What happens to the Fourier series of an odd signal? ::@:: The DC term and all cosine coefficients vanish, so $a_0=a_k=0$, and the exponential coefficients are purely imaginary and odd. <!--SR:!fsrs,2027-06-23T00:00:00.000Z,321,321.346657,1,2,7,0,0,2026-08-06T00:00:00.000Z!fsrs,2027-06-08T00:00:00.000Z,309,308.57643926,1,2,7,0,0,2026-08-03T00:00:00.000Z-->
- What is the intuition for why an even signal has only cosine terms? ::@:: An even signal is mirror-symmetric about $t=0$, while sine is odd. <br/> In the sine projection integral, the contribution from the left half cancels the contribution from the right half, so $b_k=0$. <br/> Cosine has the same mirror symmetry as the signal, so cosine projections can survive. <br/> Memory rule: even goes with even, so even signals keep cosine and kill sine. <!--SR:!fsrs,2027-04-21T00:00:00.000Z,283,282.79716409,1,2,7,0,0,2026-07-12T00:00:00.000Z!fsrs,2027-09-24T00:00:00.000Z,403,402.83580244,1,2,7,0,0,2026-08-17T00:00:00.000Z-->
- What is the intuition for why an odd signal has only sine terms and zero DC? ::@:: An odd signal changes sign across the origin, so its positive and negative halves cancel in the average, giving zero DC. <br/> Cosine is even, so odd times even stays odd and integrates to zero over a symmetric interval. <br/> Sine is odd, so odd times odd becomes even and can survive averaging. <br/> Memory rule: odd goes with odd, so odd signals keep sine and kill cosine plus DC. <!--SR:!fsrs,2027-09-14T00:00:00.000Z,394,393.73185196,1,2,7,0,0,2026-08-16T00:00:00.000Z!fsrs,2027-06-13T00:00:00.000Z,313,312.84164192,1,2,7,0,0,2026-08-04T00:00:00.000Z-->
- What does half-wave antisymmetry $f(t+T/2)=-f(t)$ imply? ::@:: Substitute the exponential series to get $F_k(-1)^k=-F_k$, so every even-index coefficient (including DC) vanishes. Only odd harmonics remain. <!--SR:!fsrs,2027-09-24T00:00:00.000Z,403,402.83580244,1,2,7,0,0,2026-08-17T00:00:00.000Z!fsrs,2027-05-02T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-15T00:00:00.000Z-->
- What does half-wave symmetry $f(t+T/2)=f(t)$ imply? ::@:: Substitution gives $F_k(-1)^k=F_k$, so every odd-index coefficient vanishes. Only even harmonics remain. <!--SR:!fsrs,2027-04-10T00:00:00.000Z,274,274.1280869,1,2,7,0,0,2026-07-10T00:00:00.000Z!fsrs,2027-05-08T00:00:00.000Z,296,295.72812302,1,2,7,0,0,2026-07-16T00:00:00.000Z-->
- What is the intuition for half-wave antisymmetry keeping only odd harmonics? ::@:: The second half is the negative of the first. The $k$-th harmonic picks up $(-1)^k$ under a $T/2$ shift. Odd harmonics match the flip; even harmonics contradict it. <!--SR:!fsrs,2027-09-30T00:00:00.000Z,407,407.37620449,1,2,7,0,0,2026-08-19T00:00:00.000Z!fsrs,2027-09-24T00:00:00.000Z,403,402.83580244,1,2,7,0,0,2026-08-17T00:00:00.000Z-->
- What is the intuition for half-wave symmetry keeping only even harmonics? ::@:: The waveform repeats after half a period. Even harmonics give $+1$ under the $T/2$ shift, matching the repetition; odd harmonics give $-1$ and must disappear. <!--SR:!fsrs,2027-09-18T00:00:00.000Z,398,398.28771618,1,2,7,0,0,2026-08-16T00:00:00.000Z!fsrs,2027-05-01T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-14T00:00:00.000Z-->
- Why do time-domain symmetries give coefficient shortcuts? ::@:: Symmetry constrains which basis functions can be present, so many integrals vanish before calculation. <!--SR:!fsrs,2027-09-02T00:00:00.000Z,385,384.59618721,1,2,7,0,0,2026-08-13T00:00:00.000Z!fsrs,2026-12-27T00:00:00.000Z,172,171.53328362,3.24197837,2,7,0,0,2026-07-08T00:00:00.000Z-->
- Worked example: Given a real even periodic signal, which Fourier coefficients are automatically zero and what does the two-sided spectrum look like? ::@:: Step 1: even symmetry means $f(-t)=f(t)$. <br/> Step 2: in the trigonometric series, every sine term is odd, so its projection integral vanishes: $b_k=\frac{2}{T}\int_0^T f(t)\sin(k\omega_0 t)dt=0$. <br/> Step 3: only cosine terms and the DC term remain, so the trigonometric expansion is cosine-only. <br/> Step 4: in exponential form this means $F_{-k}=F_k$ and each coefficient is real, so the two-sided spectrum has equal real spectral lines at $\pm k\omega_0$. <!--SR:!fsrs,2027-06-23T00:00:00.000Z,321,321.346657,1,2,7,0,0,2026-08-06T00:00:00.000Z!fsrs,2027-08-27T00:00:00.000Z,380,380.01613721,1,2,7,0,0,2026-08-12T00:00:00.000Z-->
- Worked example: How do you reason that a half-wave antisymmetric waveform contains only odd harmonics? ::@:: Step 1: start from $f(t+T/2)=-f(t)$, where $T$ is the full period. <br/> Step 2: substitute the exponential series to get $\sum_k F_k(-1)^k e^{jk\omega_0 t}=-\sum_k F_k e^{jk\omega_0 t}$. <br/> Step 3: compare coefficients of the common basis functions $e^{jk\omega_0 t}$ to obtain $F_k(-1)^k=-F_k$. <br/> Step 4: if $k$ is even, then $(-1)^k=1$, so the equation becomes $F_k=-F_k$, forcing $F_k=0$. <br/> Step 5: if $k$ is odd, then $(-1)^k=-1$, so the equation is automatically satisfied. <br/> Step 6: therefore only odd harmonics remain, and because $k=0$ is even, the DC term vanishes too. <!--SR:!fsrs,2027-08-27T00:00:00.000Z,380,380.01613721,1,2,7,0,0,2026-08-12T00:00:00.000Z!fsrs,2027-09-02T00:00:00.000Z,385,384.59618721,1,2,7,0,0,2026-08-13T00:00:00.000Z-->
- Worked example: How do you reason that a half-wave symmetric waveform contains only even harmonics? ::@:: Step 1: start from $f(t+T/2)=f(t)$, where $T$ is the full period. <br/> Step 2: substitute the exponential series to get $\sum_k F_k(-1)^k e^{jk\omega_0 t}=\sum_k F_k e^{jk\omega_0 t}$. <br/> Step 3: compare coefficients to obtain $F_k (-1)^k = F_k$. <br/> Step 4: if $k$ is odd, then $(-1)^k=-1$, so the factor becomes $-2$ and therefore $F_k=0$. <br/> Step 5: if $k$ is even, then the equation is automatically satisfied. <br/> Step 6: therefore only even harmonics remain. <!--SR:!fsrs,2027-09-30T00:00:00.000Z,407,407.37620449,1,2,7,0,0,2026-08-19T00:00:00.000Z!fsrs,2027-08-14T00:00:00.000Z,368,367.51741581,1,2,7,0,0,2026-08-11T00:00:00.000Z-->

## periodic summation and transform sampling

Fourier series and Fourier transform are two directions of one bridge. Letting the period grow makes discrete harmonic lines densify into a continuous transform. Imposing periodic repetition samples a continuous transform on the harmonic grid, turning it back into Fourier-series lines.

The Dirac comb $\operatorname{III}_T(t)=\sum_{n=-\infty}^{\infty}\delta(t-nT)$ is the ideal impulse train of spacing $T$. In the time domain, convolving with $\operatorname{III}_T$ creates periodic copies. In the frequency domain, multiplying by a comb samples a continuous spectrum on a lattice.

At the special spacing $T_*=\sqrt{2\pi}$, the comb is self-reciprocal: $\operatorname{III}_{\sqrt{2\pi}}(t)\longleftrightarrow \sqrt{2\pi}\,\operatorname{III}_{\sqrt{2\pi}}(\omega)$. The general pair follows from scaling: $\operatorname{III}_T(t)\longleftrightarrow \frac{2\pi}{T}\operatorname{III}_{2\pi/T}(\omega)=\omega_0\operatorname{III}_{\omega_0}(\omega)$ with $\omega_0=2\pi/T$.

Let $f_0(t)$ be an aperiodic prototype with transform $F_0(\omega)$, and form its periodic summation $p(t)=\sum_{n=-\infty}^{\infty}f_0(t-nT)=f_0*\operatorname{III}_T(t)$. Using the comb transform $\operatorname{III}_T(t)\longleftrightarrow \omega_0\sum_{k=-\infty}^{\infty}\delta(\omega-k\omega_0)$ with $\omega_0=2\pi/T$, the convolution theorem gives $P(\omega)=\omega_0\sum_{k=-\infty}^{\infty}F_0(k\omega_0)\delta(\omega-k\omega_0)$.

But the Fourier transform of a periodic signal with exponential coefficients $F_k$ is also $P(\omega)=2\pi\sum_{k=-\infty}^{\infty}F_k\delta(\omega-k\omega_0)$. Comparing impulse weights: $F_k=\frac{1}{T}F_0(k\omega_0)$. A Fourier-series coefficient is a sampled Fourier-transform value multiplied by $1/T$.

Intuitively, $F_0(\omega)$ is a spectral density. To turn a density into one discrete harmonic line weight, multiply by the harmonic spacing $\Delta\omega=\omega_0$ and account for the $1/(2\pi)$ normalization.

This also proves that frequency-domain sampling corresponds to periodic repetition in time. The comb in frequency is the transform of the time comb, so its inverse-domain operation is convolution with $\operatorname{III}_T(t)$, namely $\sum_n f_0(t-nT)$.

As $T\to\infty$, $\omega_0=2\pi/T\to 0$, the samples become denser, and the discrete spectrum approaches a continuous transform. The reverse direction is a sampling operation.

---

Flashcards for this section are as follows:

- Why should Fourier series and Fourier transform be viewed as two directions of one bridge rather than as unrelated tools? ::@:: Because letting the period grow makes discrete harmonic lines densify into a continuous transform, while imposing periodic repetition samples a continuous transform on the harmonic grid and turns it back into Fourier-series lines. <br/> Memory cue: infinite period gives transform; periodic repetition gives series. <!--SR:!fsrs,2027-09-30T00:00:00.000Z,407,407.37620449,1,2,7,0,0,2026-08-19T00:00:00.000Z!fsrs,2027-09-18T00:00:00.000Z,398,398.28771618,1,2,7,0,0,2026-08-16T00:00:00.000Z-->
- What is the Dirac comb $\operatorname{III}_T(t)$, and what two intuitions should you attach to it? ::@:: It is the ideal impulse train $\operatorname{III}_T(t)=\sum_{n=-\infty}^{\infty}\delta(t-nT)$: infinitely many unit impulses, equally spaced by $T$. <br/> Time-domain intuition: convolving with it makes periodic copies every $T$ seconds. <br/> Frequency-domain intuition: multiplying by a comb samples a continuous spectrum on a lattice. <!--SR:!fsrs,2027-08-14T00:00:00.000Z,368,367.51741581,1,2,7,0,0,2026-08-11T00:00:00.000Z!fsrs,2027-08-27T00:00:00.000Z,380,380.01613721,1,2,7,0,0,2026-08-12T00:00:00.000Z-->
- What is the self-reciprocal Dirac-comb pair in this Fourier-transform convention? ::@:: At $T_*=\sqrt{2\pi}$, one has $\operatorname{III}_{\sqrt{2\pi}}(t)\longleftrightarrow \sqrt{2\pi}\,\operatorname{III}_{\sqrt{2\pi}}(\omega)$. <br/> So the comb is an eigenfunction of the Fourier transform at that special spacing. <!--SR:!fsrs,2027-08-30T00:00:00.000Z,381,380.97951917,1,2,7,0,0,2026-08-14T00:00:00.000Z!fsrs,2027-09-29T00:00:00.000Z,407,407.37620449,1,2,7,0,0,2026-08-18T00:00:00.000Z-->
- How can you recover the general comb pair from the self-reciprocal one using scaling? ::@:: First write $\operatorname{III}_T(t)=\frac{\sqrt{2\pi}}{T}\operatorname{III}_{\sqrt{2\pi}}\bigl((\sqrt{2\pi}/T)t\bigr)$. <br/> Then use the scaling rule $f(at)\longleftrightarrow \frac{1}{|a|}F(\omega/a)$. <br/> This yields $\operatorname{III}_T(t)\longleftrightarrow \frac{2\pi}{T}\operatorname{III}_{2\pi/T}(\omega)=\omega_0\operatorname{III}_{\omega_0}(\omega)$ with $\omega_0=2\pi/T$. <!--SR:!fsrs,2027-05-01T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-14T00:00:00.000Z!fsrs,2027-09-02T00:00:00.000Z,385,384.59618721,1,2,7,0,0,2026-08-13T00:00:00.000Z-->
- If $p(t)=\sum_{n=-\infty}^{\infty}f_0(t-nT)=f_0*\operatorname{III}_T(t)$ with $\operatorname{III}_T(t)=\sum_n\delta(t-nT)$, what is the transform of the comb and therefore of $p(t)$? ::@:: The comb transform is $\operatorname{III}_T(t)\longleftrightarrow \frac{2\pi}{T}\sum_{k=-\infty}^{\infty}\delta(\omega-k\omega_0)=\omega_0\sum_{k=-\infty}^{\infty}\delta(\omega-k\omega_0)$ with $\omega_0=2\pi/T$. <br/> Therefore $P(\omega)=F_0(\omega)\,\omega_0\sum_{k=-\infty}^{\infty}\delta(\omega-k\omega_0)=\omega_0\sum_{k=-\infty}^{\infty}F_0(k\omega_0)\delta(\omega-k\omega_0)$. <!--SR:!fsrs,2027-04-15T00:00:00.000Z,278,278.46760619,1,2,7,0,0,2026-07-11T00:00:00.000Z!fsrs,2026-12-22T00:00:00.000Z,187,187.15626924,1.98030797,2,6,0,0,2026-06-18T00:00:00.000Z-->
- If the periodic summation of $f_0$ has exponential Fourier-series coefficients $F_k$, how do you derive $F_k$ from samples of $F_0(\omega)$ step by step? ::@:: Step 1: periodize $f_0$ to get $p(t)=\sum_n f_0(t-nT)=f_0*\operatorname{III}_T(t)$. <br/> Step 2: transform that convolution to get $P(\omega)=\omega_0\sum_k F_0(k\omega_0)\delta(\omega-k\omega_0)$. <br/> Step 3: because $p(t)$ is periodic with exponential Fourier-series coefficients $F_k$, the periodic-signal formula also gives $P(\omega)=2\pi\sum_k F_k\delta(\omega-k\omega_0)$. <br/> Step 4: now compare the coefficient of the same impulse $\delta(\omega-k\omega_0)$ in the two expansions, so $2\pi F_k=\omega_0F_0(k\omega_0)$. <br/> Step 5: solve for the coefficient to get $F_k=\frac{\omega_0}{2\pi}F_0(k\omega_0)=\frac{1}{T}F_0(k\omega_0)$. <!--SR:!fsrs,2027-08-25T00:00:00.000Z,377,376.50017085,1,2,7,0,0,2026-08-13T00:00:00.000Z!fsrs,2027-08-19T00:00:00.000Z,372,372.01284157,1,2,7,0,0,2026-08-12T00:00:00.000Z-->
- Why is the factor in $F_k=\frac{\omega_0}{2\pi}F_0(k\omega_0)=\frac{1}{T}F_0(k\omega_0)$ exactly what you should expect intuitively? ::@:: Because $F_0(\omega)$ is a spectral density with respect to $d\omega$, whereas $F_k$ is the weight of one discrete harmonic line. <br/> To turn a density into one line weight, you multiply by the harmonic spacing $\Delta\omega=\omega_0$ and then account for the course normalization by dividing by $2\pi$. <!--SR:!fsrs,2027-09-13T00:00:00.000Z,394,393.73185196,1,2,7,0,0,2026-08-15T00:00:00.000Z!fsrs,2027-08-14T00:00:00.000Z,368,367.51741581,1,2,7,0,0,2026-08-11T00:00:00.000Z-->
- Why does multiplying a continuous transform by the comb $\omega_0\sum_k\delta(\omega-k\omega_0)$ correspond to repeating the waveform every $T$ seconds? ::@:: That multiplication samples the transform at the harmonic frequencies. <br/> But the same comb is the transform of the time-domain comb $\operatorname{III}_T(t)=\sum_n\delta(t-nT)$. <br/> Therefore the inverse-domain operation is convolution with $\operatorname{III}_T(t)$, namely $f_0*\operatorname{III}_T=\sum_n f_0(t-nT)$. <br/> So frequency sampling and time periodic summation are the same bridge seen from opposite sides. <!--SR:!fsrs,2027-05-13T00:00:00.000Z,300,300.01984473,1,2,7,0,0,2026-07-17T00:00:00.000Z!fsrs,2027-04-26T00:00:00.000Z,287,287.11697064,1,2,7,0,0,2026-07-13T00:00:00.000Z-->
- How do the two bridge directions differ operationally? ::@:: Fourier series to Fourier transform is a densifying limit: as $T\to\infty$, the spacing $\omega_0=2\pi/T$ shrinks to zero and the lines merge into a continuum. <br/> Fourier transform to Fourier series is a sampling operation: periodic repetition multiplies the continuous transform by a comb and keeps only the harmonic-grid values. <!--SR:!fsrs,2027-05-29T00:00:00.000Z,313,312.84164192,1,2,7,0,0,2026-07-20T00:00:00.000Z!fsrs,2027-06-02T00:00:00.000Z,304,304.30256839,1,2,7,0,0,2026-08-02T00:00:00.000Z-->

## approximation, Gibbs phenomenon, and periodic pulse-train spectra

A truncated Fourier series $f_N(t)=a_0+\sum_{k=1}^{N}[a_k\cos(k\omega_0 t)+b_k\sin(k\omega_0 t)]$ is the best mean-square approximation among all combinations of those retained orthogonal basis functions. Truncation simply discards higher-order orthogonal directions.

Mean-square optimality minimizes average squared error, but does not guarantee pointwise perfection. Near discontinuities, the approximation may still overshoot.

The error $\varepsilon(t)=f(t)-f_N(t)$ is itself a signal. Squaring and averaging measures the average power of the residual.

Fourier-series synthesis rebuilds the waveform from its coefficients. The centered rectangular pulse train is the simplest non-sinusoidal periodic switching waveform: it models repeated on-off signaling, duty cycle, and rectangular gating.

The exponential reconstruction is $f(t)=\sum_{k=-\infty}^{\infty}F_k e^{jk\omega_0 t}$. For a centered rectangular pulse train, the waveform is real and even, so $F_k$ is real and $F_{-k}=F_k$. Pairing $+k$ and $-k$ terms: $F_k e^{jk\omega_0 t}+F_{-k}e^{-jk\omega_0 t}=2F_k\cos(k\omega_0 t)$. So $f(t)=F_0+2\sum_{k=1}^{\infty}F_k\cos(k\omega_0 t)$.

For a centered pulse train of height $E$, width $\tau$, period $T$:

The phase of this centered pulse-train spectrum is simple. Because the waveform is real and even, every $F_k$ is real and even. The phase is $0$ when $F_k>0$, $\pi$ (or $-\pi$) when $F_k<0$, and undefined at spectral zeros. Sign changes of the $\operatorname{Sa}$ envelope can be read as alternating signed amplitudes or as positive amplitudes with $\pi$ phase flips.

This synthesis view explains the duty-cycle examples. For $50\%$ duty cycle, $\tau/T=1/2$, so $F_k=\frac{E}{2}\operatorname{Sa}(k\pi/2)$. Even harmonics vanish because $\sin(k\pi/2)=0$, while odd harmonics alternate in sign: $f(t)=\frac{E}{2}+\frac{2E}{\pi}\left(\cos(\omega_0 t)-\frac{1}{3}\cos(3\omega_0 t)+\frac{1}{5}\cos(5\omega_0 t)-\cdots\right)$.

__Gibbs phenomenon:__ Near a jump, adding more harmonics squeezes oscillations into a narrower neighborhood, but the peak overshoot does not vanish. Instead it approaches about $9\%$ of the jump height. This is a warning that mean-square convergence and pointwise convergence differ.

The Gibbs phenomenon arises from ideal low-pass filtering. Truncating the Fourier series keeps only spectral lines inside a finite band. In the time domain, that sharp spectral cutoff behaves like convolution with a sinc-like oscillatory kernel that rings on both sides of a jump.

Graphically, the phenomenon looks like this: away from a jump, higher partial sums track the target more closely; near the jump, oscillatory ripples pack into a thinner region, but the tallest overshoot and deepest undershoot do not fully vanish.

Gibbs phenomenon does not contradict the minimum-mean-square property of Fourier truncation. Minimum mean square error minimizes the global average $\frac{1}{T}\int_0^T |f(t)-f_N(t)|^2dt$, whereas Gibbs overshoot is a local pointwise effect concentrated near a jump. The approximation can be globally optimal in mean-square error while still showing visible ringing near discontinuities.

The periodic rectangular pulse train is the central spectral case study. Let $E$ be the pulse height, $\tau$ the pulse width, $T$ the period, and $\omega_0=2\pi/T$. The spectral lines occur at $\omega=k\omega_0$.

For one period, $f(t)=E$ for $|t|<\tau/2$ and $f(t)=0$ for $\tau/2<|t|<T/2$. The coefficients are:

$F_k=\frac{1}{T}\int_{-\tau/2}^{\tau/2} E e^{-jk\omega_0 t}dt=\frac{E}{T}\left[\frac{e^{-jk\omega_0 t}}{-jk\omega_0}\right]_{-\tau/2}^{\tau/2}=\frac{E\tau}{T}\operatorname{Sa}\!\left(\frac{k\omega_0\tau}{2}\right)=\frac{E\tau}{T}\operatorname{sinc}_{\pi}\!\left(\frac{k\omega_0\tau}{2\pi}\right)$,

where $\operatorname{sinc}_{\pi}(x)=\frac{\sin(\pi x)}{\pi x}$.

For $k\neq 0$: using $e^{-j\theta}-e^{j\theta}=-2j\sin\theta$, the integral gives $F_k=\frac{E}{T}\frac{2\sin(k\omega_0\tau/2)}{k\omega_0}=\frac{E\tau}{T}\frac{\sin(k\omega_0\tau/2)}{k\omega_0\tau/2}$. For $k=0$: $F_0=\frac{1}{T}\int_{-\tau/2}^{\tau/2}E\,dt=E\tau/T$.

Alternatively, from the transform table: one centered pulse $E\operatorname{rect}(t/\tau)$ has transform $E\tau\operatorname{Sa}(\omega\tau/2)$. Periodizing with period $T$ gives Fourier-series coefficients that are the transform samples at $\omega=k\omega_0$ divided by $T$, yielding the same result.

The prefactor $E\tau/T$ is the DC component (average value over one period), not just a scale factor. When $k=0$, the sinc factor is $1$, so $F_0=E\tau/T$. The $\operatorname{Sa}$ term then shapes how that DC-level is distributed across nonzero harmonics.

The $\operatorname{Sa}$ envelope: for a single aperiodic pulse $E\operatorname{rect}(t/\tau)$, increasing $\tau$ compresses the transform, so the first zero moves inward. The first zero of $\operatorname{Sa}(\omega\tau/2)$ is at $\omega=\pm 2\pi/\tau$.

For the periodic pulse train, increasing $T$ decreases $\omega_0=2\pi/T$, so the harmonic samples become more closely spaced under the same envelope. The envelope itself is governed by $\tau$, not $T$.

The coefficient magnitudes form discrete spectral lines under a smooth sinc-shaped envelope. The center line at $k=0$ has height $F_0=E\tau/T$. Moving away, lines oscillate in sign and decay in magnitude according to the sinc envelope.

Several bandwidth rules follow:

- $\uparrow E$: every line scales proportionally, envelope unchanged.
- $\downarrow \tau$: pulse narrower in time, envelope wider in frequency. First zero at $\omega\approx 2\pi/\tau$.
- $\uparrow T$: line spacing $\omega_0=2\pi/T$ decreases, lines become denser under the same envelope.

The bandwidth is often defined by the first zero of the envelope: $\omega_B=2\pi/\tau$. The main lobe is $|\omega|<2\pi/\tau$, or in harmonic-index language, $|k|<T/\tau$.

The total average power is $P=\frac{1}{T}\int_{-\tau/2}^{\tau/2}E^2\,dt=E^2\tau/T$. The main-lobe power is a partial sum $P_{\text{main}}=\sum_{k\in\text{main lobe}}|F_k|^2$. For a $20\%$ duty cycle, $\tau/T=0.2$, the first zero is at $k=\pm 5$, and $P_{\text{main}}/P\approx 0.9$, so about $90\%$ of the power is in the main lobe. This is the practical meaning of bandwidth: it tells how much signal power is retained if we keep only a limited frequency range.

The listed engineering bandwidth ranges are representative scales: telephone speech $\approx 300$ to $3400\text{ Hz}$, higher-quality audio $\approx 50$ to $15{,}000\text{ Hz}$, human hearing $\approx 15$ to $20{,}000\text{ Hz}$. Different systems preserve different fractions of the spectrum depending on fidelity, cost, and perceptual goals.

The same section is also the natural home for Fourier synthesis. Reconstructing the waveform by summing harmonics shows how richer waveforms are built. One harmonic gives a pure tone; more harmonics sharpen edges or enrich timbre.

Most musical tones are approximately periodic because vibrating systems repeat a basic cycle: strings, air columns, and voiced-speech mechanisms create waveforms close to $x(t+T)=x(t)$ over short windows. A musical tone is often written as $x(t)=\sum_{k=1}^{\infty} A_k\sin(k\omega_0 t+\phi_k)$, where $A_k$ is the $k$-th harmonic amplitude, $k\omega_0$ is the harmonic angular frequency, $\omega_0=2\pi f_0$, and $f_0$ is the perceived pitch in hertz.

Different instruments playing the same note sound different because their harmonic recipes differ. A flute is often close to sinusoidal with weak higher harmonics; a violin has stronger higher harmonics.

The spectrum of a periodic musical signal is a discrete line spectrum. Each line at $k\omega_0$ records how strongly that harmonic contributes. Adding only the fundamental produces a nearly pure tone; adding more harmonics makes the waveform richer.

Audio engineering uses this in both synthesis and analysis. A synthesizer chooses pitch $f_0$, assigns harmonic amplitudes (e.g., $A_1=1$, $A_2=0.6$, $A_3=0.4$, $A_4=0.3$), and sums those sinusoids. Spectral analysis reads harmonic structure back out of recorded sound. Fourier-series ideas appear in electronic instruments, speech and music processing, and compression systems.

---

Flashcards for this section are as follows:

- Why is a finite Fourier series the best mean-square approximation? ::@:: The retained harmonics are orthogonal, so truncation keeps the orthogonal projection onto that finite subspace, minimizing mean square error.
- What is the difference between mean-square optimality and pointwise perfection? ::@:: Mean-square optimality minimizes average squared error, but does not guarantee pointwise accuracy near discontinuities.
- What are the exponential coefficients of a centered rectangular pulse train ($E$, $\tau$, $T$)? ::@:: $F_k=\frac{E\tau}{T}\operatorname{Sa}(k\omega_0\tau/2)=\frac{E\tau}{T}\operatorname{sinc}_{\pi}(k\omega_0\tau/2\pi)$ with $\omega_0=2\pi/T$.
- How should you interpret $E\tau/T$? ::@:: It is the DC component (average value). When $k=0$, the sinc factor is $1$, so $F_0=E\tau/T$.
- If $\tau$ increases, what happens to the $\operatorname{Sa}$ envelope? ::@:: The first zero moves inward from $\omega=\pm 2\pi/\tau$, so the envelope narrows in frequency.
- If $\tau$ decreases with $T$ fixed? ::@:: The envelope spreads wider while line spacing stays the same.
- If $T$ increases with $\tau$ fixed? ::@:: The envelope stays the same but lines become more closely spaced ($\omega_0=2\pi/T$ decreases).
- How can the transform table derive the pulse-train coefficients? ::@:: One pulse $E\operatorname{rect}(t/\tau)$ has transform $E\tau\operatorname{Sa}(\omega\tau/2)$. Periodizing with period $T$ samples the transform at $\omega=k\omega_0$ and divides by $T$.
- What is the bandwidth of a rectangular pulse train? ::@:: The first zero of $\operatorname{Sa}(\omega\tau/2)$ is at $\omega=2\pi/\tau$, so $\omega_B=2\pi/\tau$.
- What is the main lobe? ::@:: The central part of the $\operatorname{Sa}$ envelope between its first zeros: $|\omega|<2\pi/\tau$, or $|k|<T/\tau$ in harmonic index.
- How do you compute main-lobe power? ::@:: Sum $|F_k|^2$ over lines in the main lobe. For $20\%$ duty cycle, $P_{\text{main}}/P\approx 0.9$.
- Why is the main-lobe power ratio useful? ::@:: It tells what fraction of total signal power is captured in the low-frequency band, guiding bandwidth allocation.
- Why does a $50\%$ duty-cycle pulse train have only odd harmonics? ::@:: When $\tau/T=1/2$, $F_k=\frac{E}{2}\operatorname{Sa}(k\pi/2)$, and $\sin(k\pi/2)=0$ for even $k$.
- Why is Fourier synthesis useful for audio? ::@:: A periodic waveform can be built by adding harmonics, so pitch comes from the fundamental while timbre comes from the harmonic recipe.
- Why are musical signals approximately periodic? ::@:: Vibrating systems (strings, air columns) repeat a basic cycle, creating waveforms close to $x(t+T)=x(t)$.
- How is a musical tone written? ::@:: $x(t)=\sum_{k=1}^{\infty}A_k\sin(k\omega_0 t+\phi_k)$, with $A_k$ the harmonic amplitude, $\omega_0=2\pi f_0$, $f_0$ the pitch.
- Why can a flute and violin play the same pitch yet sound different? ::@:: Their harmonic amplitudes and phases differ, producing different timbre.
- What does the frequency spectrum of a musical tone look like? ::@:: A discrete line spectrum at $k\omega_0$, each line height recording that harmonic's contribution.
