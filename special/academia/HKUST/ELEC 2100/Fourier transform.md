---
aliases:
  - CT Fourier transform
  - ELEC 2100 Fourier transform
  - ELEC 2100 continuous-time Fourier transform
  - ELEC2100 Fourier transform
  - Fourier transform
  - HKUST ELEC 2100 Fourier transform
  - continuous-time Fourier transform
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/Fourier_transform
  - language/in/English
---

# Fourier transform

- HKUST ELEC 2100

<!-- check: ignore-file[two_sided_calc_warning]: concept-focused prompts intentionally use descriptive wording rather than repeating every symbol on the left-hand side -->

---

The Fourier transform extends frequency analysis from periodic to aperiodic signals. It produces a continuous spectral density plus a toolkit for shifting, scaling, modulation, differentiation, integration, and convolution.

This is the continuous-time aperiodic member of the Fourier family. It builds on [Fourier series](Fourier%20series.md) for periodic signals. For discrete-time counterparts, see [discrete-time Fourier transform](discrete-time%20Fourier%20transform.md) and [discrete Fourier transform](discrete%20Fourier%20transform.md). For system interpretation, see [frequency response](frequency%20response.md).

---

Flashcards for this section are as follows:

- How does this note relate to other Fourier notes? ::@:: This covers continuous-time aperiodic signals. Fourier series handles periodic, DTFT handles general discrete, DFT handles finite-record discrete.

## from Fourier series to Fourier transform

The lecture derives the Fourier transform from Fourier series by approximating an aperiodic signal with a periodic one, then letting the period grow.  Suppose $f(t)$ is aperiodic.  Truncate it on $[-T/2, T/2]$ and periodically repeat to get $f_T(t)$.  Its exponential Fourier series is $f_T(t)=\sum_{k=-\infty}^{\infty} F_k^{(T)} e^{jk\omega_0 t}$ with $\omega_0=\frac{2\pi}{T}$ and $F_k^{(T)}=\frac{1}{T}\int_{-T/2}^{T/2} f(\tau)e^{-jk\omega_0 \tau}\,d\tau$.

As $T$ grows, the harmonic spacing $\Delta\omega=2\pi/T$ shrinks.  Define $F_T(\omega)=\int_{-T/2}^{T/2} f(\tau)e^{-j\omega\tau}\,d\tau$.  Then $F_k^{(T)}=\frac{\Delta\omega}{2\pi}F_T(\omega_k)$.  The rescaled quantity $T F_k^{(T)}=F_T(\omega_k)$ tends to $F(\omega)$.

Substituting: $f_T(t)=\frac{1}{2\pi}\sum_{k=-\infty}^{\infty}F_T(\omega_k)e^{j\omega_k t}\,\Delta\omega$.

As $T\to\infty$: (1) $f_T(t)\to f(t)$ on finite intervals, (2) $\Delta\omega\to 0$ filling $\mathbb{R}$, (3) $F_T(\omega)\to F(\omega)=\int_{-\infty}^{\infty} f(\tau)e^{-j\omega\tau}\,d\tau$.  The Riemann sum converges: $\frac{1}{2\pi}\sum F_T(\omega_k)e^{j\omega_k t}\,\Delta\omega \to \frac{1}{2\pi}\int_{-\infty}^{\infty}F(\omega)e^{j\omega t}\,d\omega$.

This yields $f(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}F(\omega)e^{j\omega t}\,d\omega$ (inverse) and $F(\omega)=\int_{-\infty}^{\infty} f(t)e^{-j\omega t}\,dt$ (forward).

$F(\omega)$ is a spectral density, unlike discrete Fourier-series coefficients which are amplitudes of spectral lines.  The $1/(2\pi)$ factor comes from $1/T=\Delta\omega/(2\pi)$ in the passage from discrete sum to continuum.

The lecture uses the periodic rectangular pulse to make this concrete.  One pulse has amplitude $E$ and width $\tau$, with period $T_1$.  Then $F_k^{(T_1)}=\frac{E\tau}{T_1}\operatorname{Sa}(\omega_k\tau/2)$.

The __spectral density function__ multiplies the line coefficient by the period: $F(\omega)=\lim_{T_1\to\infty,\,k\omega_1\to\omega} T_1 F_k^{(T_1)}=E\tau\operatorname{Sa}(\omega\tau/2)$.

The inverse transform follows similarly.  From $f(t)=\sum F_k^{(T_1)}e^{j\omega_k t}$, rewrite as $\frac{1}{2\pi}\sum (T_1F_k^{(T_1)})e^{j\omega_k t}\omega_1$.  As $T_1\to\infty$: $\omega_1\to d\omega$, $T_1F_k\to F(\omega)$, giving $f(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}F(\omega)e^{j\omega t}\,d\omega$.

The core distinction: periodic signals have discrete harmonic spectra, aperiodic signals have continuous spectra.

---

Flashcards for this section are as follows:

- If an aperiodic signal $f(t)$ is approximated by a period-$T$ repetition $f_T(t)$, what exponential Fourier series and coefficient formula do we use before taking $T\to\infty$? ::@:: The exponential Fourier series is $f_T(t)=\sum_{k=-\infty}^{\infty}F_k^{(T)}e^{jk\omega_0 t}$ with $\omega_0=2\pi/T$ and $F_k^{(T)}=\frac{1}{T}\int_{-T/2}^{T/2}f(\tau)e^{-jk\omega_0\tau}\,d\tau$. <br/> The Fourier transform appears by letting $T\to\infty$.
- If $F_k^{(T)}=\frac{1}{T}\int_{-T/2}^{T/2}f(\tau)e^{-jk\omega_0\tau}\,d\tau$ and $F_T(\omega)=\int_{-T/2}^{T/2}f(\tau)e^{-j\omega\tau}\,d\tau$, how do you rewrite $F_k^{(T)}$ so the transform scaling becomes visible? ::@:: Define $F_T(\omega)=\int_{-T/2}^{T/2}f(\tau)e^{-j\omega\tau}\,d\tau$. <br/> Then at $\omega_k=k\omega_0$ one has $F_k^{(T)}=\frac{1}{T}F_T(\omega_k)$. <br/> Since $1/T=\omega_0/(2\pi)=\Delta\omega/(2\pi)$, this becomes $F_k^{(T)}=\frac{\Delta\omega}{2\pi}F_T(\omega_k)$.
- Start from the period-$T$ approximation $f_T(t)=\sum F_k^{(T)}e^{j\omega_k t}$ with $F_k^{(T)}=\frac{\Delta\omega}{2\pi}F_T(\omega_k)$.  Show how this becomes the inverse Fourier transform. ::@:: Substitute: $f_T(t)=\frac{1}{2\pi}\sum F_T(\omega_k)e^{j\omega_k t}\,\Delta\omega$. <br/> As $T\to\infty$: $\Delta\omega\to 0$, $f_T\to f$, $F_T\to F$. <br/> Riemann sum $\to$ integral: $f(t)=\frac{1}{2\pi}\int F(\omega)e^{j\omega t}\,d\omega$.
- If $F_k^{(T)}=\frac{\Delta\omega}{2\pi}F_T(\omega_k)$ and $\Delta\omega\to 0$ as $T\to\infty$, why do the coefficients shrink, and what rescaled quantity stays meaningful? ::@:: Each coefficient shrinks because $\Delta\omega=2\pi/T\to 0$. <br/> The meaningful object is $T F_k^{(T)}=F_T(\omega_k)\to F(\omega)$.
- What periodic signal is used before taking the limit to the Fourier transform? ::@:: A periodic rectangular pulse train with amplitude $E$, width $\tau$, and period $T_1$.
- For the period-$T_1$ rectangular pulse train, what are the Fourier-series coefficients? ::@:: $F_k^{(T_1)}=\frac{E\tau}{T_1}\operatorname{Sa}(\omega_k\tau/2)$, scaling like $1/T_1$.
- Why multiply the coefficient by $T_1$ when deriving the Fourier transform? ::@:: Because line coefficients shrink like $1/T_1$.  Multiplying removes that factor, giving the spectral density $F(\omega)=\lim T_1 F_k^{(T_1)}$.
- Derive the rectangular-pulse Fourier transform from the periodic coefficients. ::@:: From $F_k^{(T_1)}=\frac{E\tau}{T_1}\operatorname{Sa}(\omega_k\tau/2)$, define $F(\omega)=\lim T_1 F_k^{(T_1)}$. <br/> Then $F(\omega)=E\tau\operatorname{Sa}(\omega\tau/2)$.
- Derive the inverse Fourier transform from the Fourier series of the period-$T_1$ approximation. ::@:: From $f(t)=\sum F_k^{(T_1)}e^{j\omega_k t}$, rewrite as $\frac{1}{2\pi}\sum (T_1F_k^{(T_1)})e^{j\omega_k t}\omega_1$. <br/> As $T_1\to\infty$: $\omega_1\to d\omega$, $T_1F_k\to F(\omega)$. <br/> Get $f(t)=\frac{1}{2\pi}\int F(\omega)e^{j\omega t}\,d\omega$.
- Why does the inverse transform have $1/(2\pi)$? ::@:: Because $F_k^{(T)}=\frac{\Delta\omega}{2\pi}F_T(\omega_k)$ in the derivation, so the Riemann-sum measure is $\Delta\omega/(2\pi)$.
- What is the key difference between Fourier-series coefficients and the Fourier transform? ::@:: Fourier-series coefficients are amplitudes at discrete harmonic frequencies for periodic signals.  The Fourier transform is a continuous density for aperiodic signals.
- Why do aperiodic signals need a continuous spectrum? ::@:: Because they have no exact period, so no single harmonic spacing applies.  Letting $T\to\infty$ makes $\Delta\omega\to 0$, giving a continuum.
- How should you think about $F(\omega)$? ::@:: It gives the density of the complex exponential at frequency $\omega$ in the signal.

## representations, physical meaning, and existence

Once the transform exists, it may be represented in several equivalent ways.  In rectangular form, $F(\omega)=R(\omega)+jX(\omega)$, where $R(\omega)$ is the real part and $X(\omega)$ is the imaginary part.  In polar form, $F(\omega)=|F(\omega)|e^{j\phi(\omega)}$,

where $|F(\omega)|$ is the magnitude spectrum and $\phi(\omega)$ is the phase spectrum.  These are different coordinate descriptions of the same complex-valued spectral object.

The physical interpretation is synthesis by continuous superposition.  The inverse transform says that the signal is reconstructed by adding infinitesimal contributions from all angular frequencies.  The quantity $F(\omega)d\omega/(2\pi)$ is the infinitesimal spectral contribution associated with the small frequency band near $\omega$.  This is the continuous-spectrum analogue of adding one more harmonic term in a Fourier series.

For quadrant-aware phase extraction details, see the `signal` note section on complex numbers and `atan2`; in this note we use $\operatorname{atan2}$ directly when converting rectangular spectral components to phase.

Existence conditions are presented mainly as sufficient conditions.  A standard one is absolute integrability: $\int_{-\infty}^{\infty}|f(t)|\,dt<\infty$.

The lecture also uses a fuller Dirichlet-style package for pointwise Fourier-transform discussion: in every finite interval the signal has only finitely many extrema and finitely many finite discontinuities, and globally it is absolutely integrable.  The comparison is important for recall: absolute integrability alone is a powerful sufficient condition for defining $F(\omega)$ by the direct integral, while the fuller Dirichlet package adds regularity assumptions that support cleaner pointwise behavior statements and inversion interpretation.

But many engineering signals still sit outside that strict classical envelope.  Energy-limited signals with $\int_{-\infty}^{\infty}|f(t)|^2dt<\infty$ are treated in the finite-energy Fourier-analysis framework (mean-square / $L^2$ sense), and generalized signals such as $1$, $\delta(t)$, and $\operatorname{sgn}(t)$ are treated distributionally.

This distinction matters because "transform exists" can mean different levels of existence in practice.  In the strict classical sense, the defining integral converges absolutely.  In the finite-energy sense, the transform exists as an $L^2$ object and is still physically meaningful for spectrum analysis.  In the generalized-function sense, the transform is defined by action on test functions, which expands the scope dramatically to include constants and periodic signals via Dirac impulses in frequency.

---

Flashcards for this section are as follows:

- What are the rectangular and polar representations of the Fourier transform? ::@:: $F(\omega)=R(\omega)+jX(\omega)$ and $F(\omega)=|F(\omega)|e^{j\phi(\omega)}$.  Magnitude records strength at each frequency; phase records the phase shift.
- How should the inverse Fourier transform be interpreted physically? ::@:: It reconstructs the signal by superposing infinitesimal complex-exponential contributions from all frequencies.  The quantity $F(\omega)d\omega/(2\pi)$ is the infinitesimal spectral contribution from the narrow band near $\omega$.
- What is a standard sufficient condition for the Fourier transform to exist, and how does it compare with the Dirichlet condition? ::@:: Absolute integrability $\int|f(t)|dt<\infty$ is sufficient.  The Dirichlet package adds finitely many extrema and discontinuities per finite interval for cleaner pointwise behavior.  If a signal is energy-limited with $\int|f(t)|^2dt<\infty$ but not absolutely integrable, the transform exists in the $L^2$ (mean-square) sense, which keeps frequency-domain interpretation valid.
- Why does the lecture discuss signals like $1$, $\delta(t)$, and $\operatorname{sgn}(t)$ even though they are not absolutely integrable? ::@:: Because engineering Fourier analysis uses broader generalized-function interpretations.  Classical means the integral converges directly; engineering also allows limits, symmetry, finite-energy, or generalized-function interpretations.
- Why should you not treat magnitude and phase as unrelated? ::@:: Together they encode the full transform; changing phase while keeping magnitude fixed can change the waveform.  An aperiodic signal has no discrete harmonic lattice, so its frequency content spans a continuum, requiring an integral for reconstruction.

## typical Fourier transforms of aperiodic signals

This lecture block studies six representative aperiodic signals: centered rectangular pulse, one-sided exponential, DC signal, signum function, unit impulse, and doublet impulse.  The goal is to preserve the derivation pattern, amplitude/phase interpretation, and limiting logic that appears in later system analysis.

---

Flashcards for this section are as follows:

- Which six canonical signals are developed with derivations? ::@:: Centered rectangular pulse, one-sided exponential, DC signal, signum function, unit impulse, and doublet impulse.  Rectangular pulse and one-sided exponential: direct integration.  DC and signum: regularization limits.  Impulse: sifting.  Doublet: distribution differentiation.
- Why study amplitude, phase, and limiting logic together with transform pairs? ::@:: Because rote memorization is not enough; you need to see how the transform is derived, what its shape means, and when it is classical vs. generalized.

### rectangular pulse signal

Let $f(t)=E$ for $|t|<\tau/2$ and $0$ otherwise.  Direct integration gives $F(\omega)=\int_{-\tau/2}^{\tau/2}E e^{-j\omega t}dt=E\tau\operatorname{Sa}(\omega\tau/2)$, equivalently $E\tau\operatorname{sinc}_{\pi}(\omega\tau/(2\pi))$.  This matches the earlier limit-from-series derivation.

The amplitude spectrum is $|F(\omega)|=E\tau|\operatorname{Sa}(\omega\tau/2)|$, and the first nonzero zeros satisfy $\omega=\pm 2\pi/\tau$.  The central-lobe width is inversely proportional to $\tau$, and the one-sided first-null bandwidth is $2\pi/\tau$.  For this even real pulse, the transform is real-even, so phase is $0$ where $F(\omega)>0$, $\pi$ where it is negative, and undefined at zeros.

Two consistency checks: (1) $F(0)=\int f(t)dt=E\tau$, matching $\operatorname{Sa}(0)=1$; (2) since $f(t)$ is real-even, $F(\omega)$ must be real-even.

---

Flashcards for this section are as follows:

- For the centered rectangular pulse $f(t)=E$ on $|t|<\tau/2$, what is its Fourier transform? ::@:: Compute $F(\omega)=\int_{-\tau/2}^{\tau/2}E e^{-j\omega t}dt=E\tau\operatorname{Sa}(\omega\tau/2)=E\tau\operatorname{sinc}_{\pi}(\omega\tau/(2\pi))$.  Check dc value: $F(0)=E\tau$.  Check symmetry: real-even $f(t)$ means real-even $F(\omega)$.
- For $F(\omega)=E\tau\operatorname{Sa}(\omega\tau/2)$, what are the first nonzero zeros and first-null bandwidth? ::@:: Zeros at $\omega=\pm2\pi/\tau$.  One-sided first-null bandwidth is $2\pi/\tau$.  Amplitude is $E\tau|\operatorname{Sa}(\omega\tau/2)|$.  Phase is $0$ where $F(\omega)>0$, $\pi$ where $F(\omega)<0$, undefined at zeros.
- For $F(\omega)=\frac{E}{\alpha+j\omega}$, what explicit real-imaginary decomposition is useful for symmetry and phase checks? ::@:: Rationalize to get $F(\omega)=\frac{E(\alpha-j\omega)}{\alpha^2+\omega^2}$. <br/> Thus $\Re\{F\}=\frac{E\alpha}{\alpha^2+\omega^2}$ (even) and $\Im\{F\}=-\frac{E\omega}{\alpha^2+\omega^2}$ (odd).
- For the one-sided exponential magnitude $|F(\omega)|=\frac{E}{\sqrt{\alpha^2+\omega^2}}$, what three checkpoints summarize its low-pass behavior? ::@:: $|F(0)|=E/\alpha$, $|F(\alpha)|=E/(\sqrt{2}\alpha)$, and $|F(\omega)|\to0$ as $|\omega|\to\infty$. <br/> So low frequencies dominate.
- For the one-sided exponential phase $\phi(\omega)=-\operatorname{atan2}(\omega,\alpha)$, what limiting behavior helps you sketch the phase quickly? ::@:: The phase is $0$ at $\omega=0$, tends to $-\pi/2$ as $\omega\to+\infty$, and tends to $+\pi/2$ as $\omega\to-\infty$. <br/> This sign change matches the odd imaginary part of the transform.
- What time-width versus frequency-width rule does the rectangular-pulse transform illustrate? ::@:: A wider pulse gives a narrower main lobe, and vice versa.

### one-sided exponential signal

For $f(t)=Ee^{-\alpha t}u(t)$ with $\alpha>0$, direct evaluation gives $F(\omega)=\int_0^{\infty}Ee^{-(\alpha+j\omega)t}dt=\frac{E}{\alpha+j\omega}$.  Writing $\alpha+j\omega=re^{j\theta}$ with $r=\sqrt{\alpha^2+\omega^2}$ and $\theta=\operatorname{atan2}(\omega,\alpha)$ yields $F(\omega)=\frac{E}{r}e^{-j\theta}$.

Hence $|F(\omega)|=\frac{E}{\sqrt{\alpha^2+\omega^2}}$ and $\phi(\omega)=-\operatorname{atan2}(\omega,\alpha)$ (equivalently $-\arctan(\omega/\alpha)$ when $\alpha>0$).  The magnitude satisfies $|F(0)|=E/\alpha$, $|F(\alpha)|=E/(\sqrt{2}\alpha)$, and $|F(\omega)|\to 0$ as $|\omega|\to\infty$, so the spectrum is low-pass shaped.  The phase tends to $0$ at $\omega=0$, to $-\pi/2$ as $\omega\to+\infty$, and to $+\pi/2$ as $\omega\to-\infty$ (principal branch).

---

Flashcards for this section are as follows:

- For $f(t)=Ee^{-\alpha t}u(t)$ with $\alpha>0$, what is the transform? ::@:: $F(\omega)=\int_0^{\infty}Ee^{-(\alpha+j\omega)t}dt=\frac{E}{\alpha+j\omega}$.
- For $F(\omega)=\frac{E}{\alpha+j\omega}$, what polar form gives amplitude and phase? ::@:: Write $\alpha+j\omega=re^{j\theta}$ with $r=\sqrt{\alpha^2+\omega^2}$, $\theta=\operatorname{atan2}(\omega,\alpha)$. <br/> Then $|F|=\frac{E}{\sqrt{\alpha^2+\omega^2}}$, $\phi=-\operatorname{atan2}(\omega,\alpha)$.

### dc (direct current) signal

For $f(t)=1$, the direct integral does not converge absolutely.  The lecture derives its generalized transform by approximation: define $f_{\tau}(t)=1$ for $|t|<\tau/2$ and $0$ otherwise, so $F_{\tau}(\omega)=\int_{-\tau/2}^{\tau/2}e^{-j\omega t}\,dt=\tau\operatorname{Sa}(\omega\tau/2)$.  Then in the distribution sense $F(\omega)=\lim_{\tau\to\infty}F_{\tau}(\omega)=\lim_{\tau\to\infty}\tau\operatorname{Sa}(\omega\tau/2)=2\pi\delta(\omega)$.

The area explanation is why the coefficient is $2\pi$.  One has $\int_{-\infty}^{\infty}F_{\tau}(\omega)\,d\omega=\tau\int_{-\infty}^{\infty}\operatorname{Sa}(\omega\tau/2)\,d\omega=2\pi$, so as $\tau$ grows, the spectrum compresses toward $\omega=0$ while preserving total area $2\pi$.  The peak grows and the width shrinks, so the generalized limit is an impulse at zero frequency with weight $2\pi$.  In frequency-in-hertz notation this corresponds to $2\pi\delta(2\pi f)=\delta(f)$ using scaling of delta.

This is also the aperiodic counterpart of line-spectrum concentration from Fourier series: the entire dc content is at zero frequency.  So $1\longleftrightarrow2\pi\delta(\omega)$ is the natural generalized representation of "all energy at frequency zero".

---

Flashcards for this section are as follows:

- For the dc signal $f(t)=1$, how does the lecture derive its transform? ::@:: Use $f_{\tau}(t)=1$ for $|t|<\tau/2$, so $F_{\tau}(\omega)=\tau\operatorname{Sa}(\omega\tau/2)$. <br/> Taking $\tau\to\infty$ gives $1\longleftrightarrow2\pi\delta(\omega)$.
- In the dc derivation, why is the limiting impulse weighted by $2\pi$? ::@:: Because the spectrum narrows toward $\omega=0$ while preserving total area $\int F_{\tau}(\omega)d\omega=2\pi$.  So the limit is $2\pi\delta(\omega)$.
- For the dc transform $1\longleftrightarrow2\pi\delta(\omega)$, what is the physical interpretation? ::@:: All spectral mass is at zero frequency: only a constant non-oscillatory component.  Using delta scaling, $2\pi\delta(2\pi f)=\delta(f)$, so all content sits at $f=0$.

### signum function

The signum function $\operatorname{sgn}(t)$ is also not absolutely integrable, so the lecture regularizes it by $f_{\alpha}(t)=\operatorname{sgn}(t)e^{-\alpha|t|}$ with $\alpha>0$ and then lets $\alpha\to0^+$.  Splitting at $t=0$ gives $F_{\alpha}(\omega)=\int_0^{\infty}e^{-(\alpha+j\omega)t}dt-\int_{-\infty}^{0}e^{(\alpha-j\omega)t}dt=-\frac{2j\omega}{\alpha^2+\omega^2}$.

Taking the limit yields the principal-value generalized transform $\operatorname{sgn}(t)\longleftrightarrow \frac{2}{j\omega}$.  The magnitude behaves like $2/|\omega|$ away from zero, and the phase is $-\pi/2$ for $\omega>0$ and $+\pi/2$ for $\omega<0$.

Another route is the derivative identity $\frac{d}{dt}\operatorname{sgn}(t)=2\delta(t)$.  Using differentiation in frequency gives $j\omega F_{\operatorname{sgn}}(\omega)=2$, hence $F_{\operatorname{sgn}}(\omega)=\frac{2}{j\omega}$ in principal value form.  This cross-check links generalized derivatives and transform properties directly.

There is also a linearity derivation once the unit-step transform is known.  Since $\operatorname{sgn}(t)=2u(t)-1$ and $u(t)\longleftrightarrow \pi\delta(\omega)+\frac{1}{j\omega}$ while $1\longleftrightarrow2\pi\delta(\omega)$, linearity gives $F_{\operatorname{sgn}}(\omega)=2\left(\pi\delta(\omega)+\frac{1}{j\omega}\right)-2\pi\delta(\omega)=\frac{2}{j\omega}$.  The delta terms cancel because the signum function has no dc component: its positive and negative halves balance each other.

---

Flashcards for this section are as follows:

- For the signum signal, what regularization does the lecture use? ::@:: Use $f_{\alpha}(t)=\operatorname{sgn}(t)e^{-\alpha|t|}$ with $\alpha>0$, compute its transform, then let $\alpha\to0^+$.
- For $f_{\alpha}(t)=\operatorname{sgn}(t)e^{-\alpha|t|}$, what is the transform before the limit? ::@:: Split at $t=0$: $F_{\alpha}(\omega)=\int_0^{\infty}e^{-(\alpha+j\omega)t}dt-\int_{-\infty}^{0}e^{(\alpha-j\omega)t}dt=-\frac{2j\omega}{\alpha^2+\omega^2}$.
- What generalized transform is obtained as $\alpha\to0^+$? ::@:: $\operatorname{sgn}(t)\longleftrightarrow \frac{2}{j\omega}$ in principal-value sense.
- Using linearity and $\operatorname{sgn}(t)=2u(t)-1$, how can you derive the signum transform? ::@:: From $u(t)\longleftrightarrow \pi\delta(\omega)+\frac{1}{j\omega}$ and $1\longleftrightarrow2\pi\delta(\omega)$, linearity gives $2(\pi\delta+\frac{1}{j\omega})-2\pi\delta=\frac{2}{j\omega}$.
- For the signum transform $\frac{2}{j\omega}$, what are magnitude and phase? ::@:: Magnitude $\approx 2/|\omega|$ away from zero.  Phase: $-\pi/2$ for $\omega>0$, $+\pi/2$ for $\omega<0$.

Sampling gives the transform immediately: $F(\omega)=\int_{-\infty}^{\infty}\delta(t)e^{-j\omega t}dt=1$, so $\delta(t)\longleftrightarrow 1$.  This is the extreme time-frequency spread tradeoff: maximally concentrated in time, completely spread in frequency.

Shifted impulses generalize this immediately: $\delta(t-t_0)\longleftrightarrow e^{-j\omega t_0}$.  So shifting an impulse in time does not change magnitude (still $1$) but adds linear phase, exactly matching the general time-shift property.

The same pair also follows from duality.  The explicit duality rule used in this note is: if $f(t)\longleftrightarrow F(\omega)$, then $F(t)\longleftrightarrow2\pi f(-\omega)$.  Apply that rule to the dc pair $1\longleftrightarrow2\pi\delta(\omega)$.  Here $F(t)=2\pi\delta(t)$ and $2\pi f(-\omega)=2\pi$, so the rule gives $2\pi\delta(t)\longleftrightarrow2\pi$, hence $\delta(t)\longleftrightarrow1$.  The impulse-flat-spectrum pair is the dual of the dc-zero-frequency-impulse pair.

---

Flashcards for this section are as follows:

- For the unit impulse, what sampling integral proves $\delta(t)\longleftrightarrow1$? ::@:: $F(\omega)=\int_{-\infty}^{\infty}\delta(t)e^{-j\omega t}dt=1$ by the sifting property.
- Starting from $1\longleftrightarrow2\pi\delta(\omega)$, how does duality give $\delta(t)\longleftrightarrow1$? ::@:: Apply $F(t)\longleftrightarrow2\pi f(-\omega)$ to get $2\pi\delta(t)\longleftrightarrow2\pi$, then divide by $2\pi$.
- For $\delta(t)\longleftrightarrow1$, what time-frequency interpretation should you remember? ::@:: Maximally concentrated in time, completely spread in frequency.
- For a shifted impulse $\delta(t-t_0)$, what is its transform and what does it do to magnitude and phase? ::@:: $\delta(t-t_0)\longleftrightarrow e^{-j\omega t_0}$.  Magnitude stays $1$, phase becomes linear in $\omega$.

### doublet impulse signal (impulse pair)

For the doublet $\delta'(t)$, use distribution differentiation: $F(\omega)=\int_{-\infty}^{\infty}\delta'(t)e^{-j\omega t}dt=-\left.\frac{d}{dt}e^{-j\omega t}\right|_{t=0}=j\omega$.  So $\delta'(t)\longleftrightarrow j\omega$, matching the general rule that time differentiation multiplies the spectrum by $j\omega$.

Because $\delta'(t)$ is real and odd, its transform being purely imaginary and odd is what symmetry theory predicts.  This gives a quick structural check: if a derivation produces a non-odd real part, a sign or differentiation error has occurred.

Across all six examples, the pattern is: direct integral when possible, regularization-and-limit when not, and then amplitude/phase interpretation.

---

Flashcards for this section are as follows:

- For the doublet $\delta'(t)$, what derivation gives its transform? ::@:: $F(\omega)=\int_{-\infty}^{\infty}\delta'(t)e^{-j\omega t}dt=-\left.\frac{d}{dt}e^{-j\omega t}\right|_{t=0}=j\omega$, so $\delta'(t)\longleftrightarrow j\omega$.
- For $\delta'(t)\longleftrightarrow j\omega$, what symmetry pattern should appear and why is it a useful error check? ::@:: Since $\delta'(t)$ is real and odd, $F(\omega)$ should be purely imaginary and odd.  A non-odd real part signals an algebra error.
- For the doublet impulse transform $j\omega$, what amplitude and phase picture should you remember? ::@:: Magnitude $\propto|\omega|$ (higher frequencies emphasized).  Phase: $+\pi/2$ for $\omega>0$, $-\pi/2$ for $\omega<0$.
- Across the six examples, what template helps preserve derivations? ::@:: (1) Determine existence: direct integral if absolutely integrable; otherwise regularization or duality. (2) Execute algebra. (3) Check symmetry.  The six cases: rectangular pulse, one-sided exponential, DC, signum, impulse, doublet.
- Why does $1\longleftrightarrow2\pi\delta(\omega)$ agree with the inverse transform? ::@:: Substitute $F(\omega)=2\pi\delta(\omega)$ into $f(t)=\frac{1}{2\pi}\int F(\omega)e^{j\omega t}d\omega$: get $\frac{1}{2\pi}\cdot2\pi\cdot1=1$.

## symmetry, scaling, and shifting properties

The basic transform properties show how simple geometric operations in time are encoded in the frequency domain.  Linearity is the umbrella rule: $af_1(t)+bf_2(t)\longleftrightarrow aF_1(\omega)+bF_2(\omega)$.

This makes transform tables reusable: once a signal is decomposed into simpler pieces, the transform follows piece by piece.

Duality swaps the roles of time and frequency, up to sign and the $2\pi$ factor.  The explicit rule used throughout this note is: if $f(t)\longleftrightarrow F(\omega)$, then $F(t)\longleftrightarrow 2\pi f(-\omega)$.  Both the sign flip in $f(-\omega)$ and the factor $2\pi$ matter.  The lecture uses this to move efficiently between rectangular functions, sinc functions, constants, and impulses.

Conjugation symmetry explains what real-valued time-domain signals look like spectrally.  If $f(t)$ is real, then $F(-\omega)=F^*(\omega)$.

Equivalently, the magnitude spectrum is even and the phase spectrum is odd wherever the phase is defined continuously.  If $f(t)$ is also even, then $F(\omega)$ is real and even.  If $f(t)$ is real and odd, then $F(\omega)$ is purely imaginary and odd.  These are the continuous-spectrum analogues of the Fourier-series symmetry shortcuts.

The time-scaling property is $f(at)\longleftrightarrow \frac{1}{|a|}F\!\left(\frac{\omega}{a}\right)$ for $a\neq 0$.

This formula encodes the width tradeoff precisely.  Time compression by $|a|>1$ produces spectral expansion.  Time expansion produces spectral compression.  If $a<0$, a time reversal is included as well.

There is a very compact way to remember both shifting properties from one starting pair.  A pure complex exponential $e^{j\omega_0 t}$ is intuitively a single-frequency signal at angular frequency $\omega_0$, so its Fourier transform should be concentrated at that one frequency.  In generalized-function form this is exactly $e^{j\omega_0 t}\longleftrightarrow 2\pi\delta(\omega-\omega_0)$.

Now the frequency-shifting or modulation property follows from the multiplication theorem.  The explicit multiplication rule is: if $f_1(t)\longleftrightarrow F_1(\omega)$ and $f_2(t)\longleftrightarrow F_2(\omega)$, then $f_1(t)f_2(t)\longleftrightarrow \frac{1}{2\pi}(F_1*F_2)(\omega)$.  Apply it with $f_1(t)=e^{j\omega_0 t}$ and $F_1(\omega)=2\pi\delta(\omega-\omega_0)$, and with $f_2(t)=f(t)$ and $F_2(\omega)=F(\omega)$.  Then $e^{j\omega_0 t}f(t)\longleftrightarrow \frac{1}{2\pi}\bigl(2\pi\delta(\omega-\omega_0)*F(\omega)\bigr)=F(\omega-\omega_0)$.  Multiplying by a complex sinusoid in time therefore shifts the spectrum rigidly along the frequency axis.  For real cosine modulation, the spectrum splits into two shifted copies.  This is the mathematical skeleton behind amplitude modulation and windowed-frequency placement.

The time-shifting property follows from the same idea after applying duality and convolution.  First use the explicit duality rule: if $f(t)\longleftrightarrow F(\omega)$, then $F(t)\longleftrightarrow2\pi f(-\omega)$.  Apply it to $e^{j\omega_0 t}\longleftrightarrow 2\pi\delta(\omega-\omega_0)$ and rename the parameter to obtain $\delta(t-t_0)\longleftrightarrow e^{-j\omega t_0}$.  Next use the explicit convolution rule: if $f_1(t)\longleftrightarrow F_1(\omega)$ and $f_2(t)\longleftrightarrow F_2(\omega)$, then $(f_1*f_2)(t)\longleftrightarrow F_1(\omega)F_2(\omega)$.  Since delaying a signal means convolving it with a shifted impulse, $f(t-t_0)=f(t)*\delta(t-t_0)$, the rule gives $f(t-t_0)\longleftrightarrow F(\omega)e^{-j\omega t_0}$.

So the two rules are best remembered as one chain: pure exponential $\to$ shifted delta in frequency; multiplication gives frequency shift; duality converts that exponential-delta pair into the shifted-impulse/phase-ramp pair; convolution then gives time shift.  Memory cue: __single tone $\leftrightarrow$ single spectral line__, then use multiplication, convolution, and duality to generate both shifting properties.

The lecture's first worked example in this block is a three-pulse signal built from one prototype pulse.  Let $f_0(t)$ be a centered rectangular pulse of amplitude $E$ and width $\tau$, so $F_0(\omega)=E\tau\operatorname{Sa}(\omega\tau/2)$.  Form the three-pulse signal by shifting copies left and right: $f(t)=f_0(t+T)+f_0(t)+f_0(t-T)$.  Use linearity together with the time-shifting rule $f(t-t_0)\longleftrightarrow e^{-j\omega t_0}F(\omega)$.  Then $f_0(t+T)=f_0(t-(-T))\longleftrightarrow e^{j\omega T}F_0(\omega)$ and $f_0(t-T)\longleftrightarrow e^{-j\omega T}F_0(\omega)$, so $F(\omega)=F_0(\omega)\bigl(e^{j\omega T}+1+e^{-j\omega T}\bigr)=F_0(\omega)\bigl(1+2\cos(\omega T)\bigr)=E\tau\operatorname{Sa}(\omega\tau/2)\bigl(1+2\cos(\omega T)\bigr)$.  The factor $1+2\cos(\omega T)$ changes the detailed interference pattern, but the overall spectral envelope is still set by $F_0(\omega)=E\tau\operatorname{Sa}(\omega\tau/2)$.  So adding more separated pulses changes spectral ripples and line-up, yet the envelope and bandwidth remain governed by the shape of one pulse.

The same idea becomes more revealing when the number of pulses keeps increasing.  If one takes $2N+1$ copies, $f_N(t)=\sum_{n=-N}^{N}f_0(t-nT)$, then linearity and time shifting give $F_N(\omega)=F_0(\omega)\sum_{n=-N}^{N}e^{-jn\omega T}=F_0(\omega)\left(1+2\sum_{n=1}^{N}\cos(n\omega T)\right)$.  The bracket is the Dirichlet-kernel factor, equivalently $\frac{\sin((2N+1)\omega T/2)}{\sin(\omega T/2)}$.  As $N$ grows, the spectral ripples become narrower and taller around the harmonic frequencies $\omega=k\omega_0$, where $\omega_0=2\pi/T$.

In the limit $N\to\infty$, one no longer has a finite pulse cluster but a periodic summation $p(t)=\sum_{n=-\infty}^{\infty}f_0(t-nT)=f_0*\operatorname{III}_T(t)$, where $\operatorname{III}_T(t)=\sum_{n=-\infty}^{\infty}\delta(t-nT)$ is the Dirac comb of period $T$.  Since $\operatorname{III}_T(t)\longleftrightarrow \frac{2\pi}{T}\sum_{k=-\infty}^{\infty}\delta(\omega-k\omega_0)=\omega_0\sum_{k=-\infty}^{\infty}\delta(\omega-k\omega_0)$, the convolution theorem gives $P(\omega)=F_0(\omega)\,\omega_0\sum_{k=-\infty}^{\infty}\delta(\omega-k\omega_0)=\omega_0\sum_{k=-\infty}^{\infty}F_0(k\omega_0)\delta(\omega-k\omega_0)$.  So an infinite periodic repetition samples the continuous transform only at the harmonic lattice and turns the continuum into a line spectrum.

This is exactly the reverse of the derivation at the start of the note.  There, one starts from a periodic line spectrum and lets $T\to\infty$, so the lines get denser and merge into a continuous Fourier transform.  Here, one starts from a single aperiodic waveform with continuous transform and repeats it every $T$ seconds, so the continuous transform is sampled at spacing $\omega_0=2\pi/T$ and collapses back into Fourier-series lines.  The intuition therefore runs both ways: letting the period blow up turns series into transform, while imposing periodic repetition turns transform back into series.

The lecture then combines time shifting and scaling in one formula.  Start from the explicit scaling rule $f(at)\longleftrightarrow \frac{1}{|a|}F(\omega/a)$ and the time-shifting rule $g(t-t_0)\longleftrightarrow e^{-j\omega t_0}G(\omega)$.  Write $f(at+b)=f(a(t+b/a))$, so if $g(t)=f(at)$, then $f(at+b)=g(t-(-b/a))$.  Therefore $f(at+b)\longleftrightarrow \frac{1}{|a|}e^{j\omega b/a}F(\omega/a)$.  A useful memory example is $g(t)=f(2t-5)$.  Here $a=2$ and $b=-5$, so $G(\omega)=\frac{1}{2}e^{-j5\omega/2}F(\omega/2)$.  The phase factor comes from the shift, while the amplitude scaling and spectral stretching come from the time scaling.  Consequently the power spectral density is $|G(\omega)|^2=\frac{1}{4}|F(\omega/2)|^2$: the time shift contributes only phase and therefore does not affect the power spectrum, while the scaling changes the spectral width and amplitude factor.

The next worked example uses the frequency-shifting property on a rectangular pulse modulated by a cosine.  Let $f(t)=f_0(t)\cos(\omega_0 t)$, where $f_0(t)$ is the centered rectangular pulse with transform $F_0(\omega)=E\tau\operatorname{Sa}(\omega\tau/2)$.  By Euler's formula, $f(t)=\frac{1}{2}f_0(t)e^{-j\omega_0 t}+\frac{1}{2}f_0(t)e^{j\omega_0 t}$.  Now apply the explicit frequency-shifting rules $e^{-j\omega_0 t}f(t)\longleftrightarrow F(\omega+\omega_0)$ and $e^{j\omega_0 t}f(t)\longleftrightarrow F(\omega-\omega_0)$ to obtain $F(\omega)=\frac{1}{2}F_0(\omega+\omega_0)+\frac{1}{2}F_0(\omega-\omega_0)$.  Substituting the rectangular-pulse spectrum gives $F(\omega)=\frac{E\tau}{2}\operatorname{Sa}\bigl((\omega+\omega_0)\tau/2\bigr)+\frac{E\tau}{2}\operatorname{Sa}\bigl((\omega-\omega_0)\tau/2\bigr)$.  So the original sinc spectrum centered at $\omega=0$ is split into two copies centered at $\omega=\pm\omega_0$, each scaled by $1/2$.  This is the lecture's cleanest picture of amplitude modulation in the transform domain.

---

Flashcards for this section are as follows:

- What is the linearity property of the Fourier transform? ::@:: If $f_1\longleftrightarrow F_1$ and $f_2\longleftrightarrow F_2$, then $af_1+bf_2\longleftrightarrow aF_1+bF_2$.  It lets you decompose a signal into simpler pieces, transform each, and recombine.
- What duality rule is used in this note? ::@:: If $f(t)\longleftrightarrow F(\omega)$, then $F(t)\longleftrightarrow2\pi f(-\omega)$.
- What conjugation symmetry does a real-valued time-domain signal satisfy? ::@:: $F(-\omega)=F^*(\omega)$.  If $f(t)$ is also even, $F(\omega)$ is real and even.  If $f(t)$ is real and odd, $F(\omega)$ is purely imaginary and odd.
- What is the time-scaling property? ::@:: $f(at)\longleftrightarrow \frac{1}{|a|}F(\omega/a)$ for nonzero real $a$.  Compressing in time spreads in frequency, and vice versa.
- What is the time-shifting property? ::@:: $f(t-t_0)\longleftrightarrow e^{-j\omega t_0}F(\omega)$.  Magnitude unchanged, adds linear phase $e^{-j\omega t_0}$.
- Why is $e^{j\omega_0 t}\longleftrightarrow 2\pi\delta(\omega-\omega_0)$ a good starting point for shifting properties? ::@:: A pure exponential is one frequency, so its transform is a single spectral line at $\omega_0$. <br/> From this pair, multiplication, convolution, and duality generate both shifting rules.
- What is the frequency-shifting property? ::@:: $e^{j\omega_0 t}f(t)\longleftrightarrow F(\omega-\omega_0)$.  Because time-domain modulation moves a spectrum to a new frequency location, which is the core idea behind spectral translation and modulation systems.
- If $f(t)=f_0(t+T)+f_0(t)+f_0(t-T)$ and $F_0(\omega)=E\tau\operatorname{Sa}(\omega\tau/2)$, what is $F(\omega)$? ::@:: $F(\omega)=F_0(\omega)(e^{j\omega T}+1+e^{-j\omega T})=F_0(\omega)(1+2\cos(\omega T))=E\tau\operatorname{Sa}(\omega\tau/2)(1+2\cos(\omega T))$. <br/> The envelope is set by $F_0(\omega)=E\tau\operatorname{Sa}(\omega\tau/2)$.  The factor $1+2\cos(\omega T)$ changes the ripple pattern, but the envelope and bandwidth remain those of one pulse.
- If $f_N(t)=\sum_{n=-N}^{N}f_0(t-nT)$, what is its transform, and what happens as $N$ increases? ::@:: $F_N(\omega)=F_0(\omega)\sum_{n=-N}^{N}e^{-jn\omega T}=F_0(\omega)(1+2\sum_{n=1}^{N}\cos(n\omega T))$. <br/> As $N$ increases, the interference factor becomes a sharper Dirichlet-kernel pattern.  When $N\to\infty$, it becomes $p(t)=f_0*\operatorname{III}_T(t)$. <br/> In frequency: $P(\omega)=\omega_0\sum_{k}F_0(k\omega_0)\delta(\omega-k\omega_0)$ with $\omega_0=2\pi/T$. <br/> The continuous transform is sampled on the harmonic grid, giving a line spectrum.
- How is the many-pulse limit the reverse of the earlier derivation from Fourier series to Fourier transform? ::@:: Letting $T\to\infty$ makes discrete lines merge into a continuous transform.  Repeating every $T$ seconds samples the continuous transform into Fourier-series lines.  Memory: infinite period turns series into transform; infinite repetition turns transform into series.
- If $f(t)\longleftrightarrow F(\omega)$, what combined time-scaling and time-shifting rule gives the transform of $f(at+b)$? ::@:: Use $f(at)\longleftrightarrow \frac{1}{|a|}F(\omega/a)$ and then shift by $-b/a$. <br/> The result is $f(at+b)\longleftrightarrow \frac{1}{|a|}e^{j\omega b/a}F(\omega/a)$.
- Worked example: If $g(t)=f(2t-5)$ and $f(t)\longleftrightarrow F(\omega)$, what are $G(\omega)$ and the power spectral density $|G(\omega)|^2$? ::@:: Here $a=2$ and $b=-5$, so $G(\omega)=\frac{1}{2}e^{-j5\omega/2}F(\omega/2)$. <br/> Therefore $|G(\omega)|^2=\frac{1}{4}|F(\omega/2)|^2$. <br/> Memory point: the shift contributes only phase, so it does not affect the power spectral density.
- Why is the frequency-shifting property important physically? ::@:: Because time-domain modulation moves a spectrum to a new frequency location, which is the core idea behind spectral translation and modulation systems.
- Worked example: Why does delaying a signal not change its magnitude spectrum? ::@:: A delay multiplies the transform by $e^{-j\omega t_0}$, which has magnitude $1$ for every $\omega$.  Therefore only phase changes, and the magnitude spectrum stays exactly the same.
- Example 6: If $f(t)=f_0(t)\cos(\omega_0 t)$ and $F_0(\omega)=E\tau\operatorname{Sa}(\omega\tau/2)$, what spectrum follows from Euler's formula and frequency shifting? ::@:: Write $f(t)=\frac{1}{2}f_0(t)e^{j\omega_0 t}+\frac{1}{2}f_0(t)e^{-j\omega_0 t}$. <br/> Then $F(\omega)=\frac{1}{2}F_0(\omega-\omega_0)+\frac{1}{2}F_0(\omega+\omega_0)$. <br/> Hence $F(\omega)=\frac{E\tau}{2}\operatorname{Sa}\!\bigl((\omega-\omega_0)\tau/2\bigr)+\frac{E\tau}{2}\operatorname{Sa}\!\bigl((\omega+\omega_0)\tau/2\bigr)$.  The original sinc spectrum centered at $\omega=0$ is split into two copies centered at $\omega=+\omega_0$ and $\omega=-\omega_0$, each scaled by $1/2$.  This is the standard transform-domain picture of amplitude modulation.

## differentiation, integration, and convolution theorems

Differentiation in time corresponds to multiplication by $j\omega$ in frequency: $\frac{d}{dt}f(t)\longleftrightarrow j\omega F(\omega)$, and more generally $f^{(n)}(t)\longleftrightarrow (j\omega)^n F(\omega)$.

Differentiation emphasizes high frequencies, because the multiplier grows in magnitude with $|\omega|$.

In actual transform problems, these property rules are often much faster than direct integration.  A practical workflow is: first use linearity to split a signal into table-known pieces, next check whether differentiation or running integration turns the signal into a simpler known one, and only then fall back to raw integration if nothing cleaner appears.  For example, linearity gives $3e^{-t}u(t)-2e^{-2t}u(t)\longleftrightarrow \frac{3}{1+j\omega}-\frac{2}{2+j\omega}$ immediately.  Differentiation gives $\delta'(t)\longleftrightarrow j\omega$ from $\delta(t)\longleftrightarrow1$.  Running integration gives $u(t)=\int_{-\infty}^{t}\delta(\tau)\,d\tau$, so $u(t)\longleftrightarrow \frac{1}{j\omega}+\pi\delta(\omega)$.

Multiplication by $t$ in the time domain corresponds to differentiation in frequency: $tf(t)\longleftrightarrow j\frac{dF}{d\omega}$.  This rule is easiest to remember by deriving it directly from the transform kernel.  Start from $F(\omega)=\int_{-\infty}^{\infty}f(t)e^{-j\omega t}\,dt$.  Differentiate with respect to $\omega$ to get $\frac{dF}{d\omega}=\int_{-\infty}^{\infty}f(t)(-jt)e^{-j\omega t}\,dt=-j\,\mathcal{F}\{tf(t)\}$.  Hence $\mathcal{F}\{tf(t)\}=j\frac{dF}{d\omega}$.  This is the frequency-domain mirror of time differentiation: differentiating with respect to $t$ pulls down $-j\omega$, while differentiating with respect to $\omega$ pulls down $-jt$.  For recall, it is also the dual companion of $f'(t)\longleftrightarrow j\omega F(\omega)$: the differentiation operator in one domain corresponds to multiplication by the variable in the other domain, and vice versa.

More generally, time-domain polynomial weighting corresponds to higher-order spectral derivatives.  The conceptual message is that time-domain spreading and frequency-domain smoothing, or vice versa, are linked through differentiation.

Integration in time is subtler because a constant of integration may appear.  For the running integral $y(t)=\int_{-\infty}^{t}f(\tau)\,d\tau$, the lecture gives the transform $Y(\omega)=\frac{F(\omega)}{j\omega}+\pi F(0)\delta(\omega)$.  For an absolutely integrable transient signal, $F(0)=\int_{-\infty}^{\infty}f(t)\,dt$ is the total signed area of the input.

The factor $\pi$ instead of $2\pi$ is easiest to remember with the half-portion intuition over the whole time axis.  If a transient input has total area $A=F(0)$, then its running integral tends to $0$ as $t\to-\infty$ and to $A$ as $t\to+\infty$.  Over an increasingly long time interval, those two endpoint plateau values each occupy asymptotically one half of the timeline, while the intermediate transition region occupies zero fraction of the timeline.  So the constant part seen by the transform is the midpoint level $A/2$, and since $1\longleftrightarrow2\pi\delta(\omega)$, that midpoint contributes $2\pi(A/2)\delta(\omega)=\pi A\delta(\omega)$.  The remaining nonconstant part contributes the $F(\omega)/(j\omega)$ term.

This also explains why the extra impulse term is the bookkeeping device for the DC behavior.  It records the constant midpoint level hidden inside the accumulated step created by the total area of the transient input.

If the input already contains a steady-state bias $C$, then the ordinary number $F(0)$ is no longer finite; instead the spectrum already contains the singular term $2\pi C\delta(\omega)$ at the origin.  It is therefore important to separate the signal into its transient finite-area part and its steady-state polynomial part.  If $f(t)=g(t)+C$ with $A=\int_{-\infty}^{\infty}g(t)\,dt$ finite, then integrating $f$ gives one contribution from the transient part and another from the bias: the transient part contributes the step-offset term $\pi A\delta(\omega)$, while the dc bias integrates to a ramp $Ct$ and contributes $j2\pi C\delta'(\omega)$.  So a signal may produce both a $\delta(\omega)$ term and a promoted $\delta'(\omega)$ term in the integrated transform, and they come from different pieces of the input.

This promotion language can be made systematic.  The polynomial family satisfies $t^n\longleftrightarrow 2\pi j^n\delta^{(n)}(\omega)$ in the two-sided generalized sense, so each integration in time raises the polynomial degree by one and simultaneously increases the derivative order of the Dirac delta by one, while also introducing one more factor of $j$.  That is the slightly ironic point: integrating in time makes the origin singularity more differentiated in frequency. The phrase _origin singularity_ matters: only singular terms sitting at $\omega=0$ need this promotion rule. A shifted line such as $c\,\delta(\omega-\omega_1)$ with $\omega_1\neq0$ is not divided by zero when one forms $F(\omega)/(j\omega)$; it simply becomes $c\,\delta(\omega-\omega_1)/(j\omega_1)$ by ordinary scaling, so no promotion is needed away from the origin.

The opposite happens under time differentiation.  Since differentiation lowers polynomial degree in time, it demotes the Dirac singularity at the origin: multiplying by $j\omega$ reduces the derivative order by one and removes one factor of $j$ (equivalently, divides by $j$ in the coefficient pattern).  This is consistent with identities such as $\omega\delta'(\omega)=-\delta(\omega)$ and, more generally, $\omega\delta^{(n)}(\omega)=-n\delta^{(n-1)}(\omega)$.  These identities should be proved, not just quoted.  Testing against a smooth probe $g(\omega)$ gives $\langle \omega\delta'(\omega),g\rangle=\langle \delta'(\omega),\omega g(\omega)\rangle=-(\omega g(\omega))'\rvert_{\omega=0}=-g(0)=\langle -\delta(\omega),g\rangle$.  More generally, $\langle \omega\delta^{(n)}(\omega),g\rangle=\langle \delta^{(n)}(\omega),\omega g(\omega)\rangle=(-1)^n(\omega g)^{(n)}(0)=(-1)^n n g^{(n-1)}(0)=\langle -n\delta^{(n-1)}(\omega),g\rangle$, because only the first derivative of $\omega$ survives in the Leibniz expansion.  So differentiation is a demotion operator, while integration is a promotion operator.

Partial-fraction decomposition is another high-payoff shortcut, especially when a rational spectrum is given and one wants to move quickly back to the time domain using known first-order pairs.  A simple example is $F(\omega)=\frac{3}{(1+j\omega)(2+j\omega)}=\frac{3}{1+j\omega}-\frac{3}{2+j\omega}$, so $f(t)=3e^{-t}u(t)-3e^{-2t}u(t)$.  A more complicated repeated-pole example is $F(\omega)=\frac{1}{(1+j\omega)^2(2+j\omega)}=-\frac{1}{1+j\omega}+\frac{1}{(1+j\omega)^2}+\frac{1}{2+j\omega}$, so $f(t)=\bigl(-e^{-t}+te^{-t}+e^{-2t}\bigr)u(t)$.  The point is that once the rational expression is split into standard pieces, transform lookup becomes much cleaner than handling the whole fraction as one block.

---

Flashcards for this section are as follows:

- What is the time-domain differentiation property? ::@:: $f'(t)\longleftrightarrow j\omega F(\omega)$, and $f^{(n)}(t)\longleftrightarrow (j\omega)^nF(\omega)$.  Differentiation emphasizes high frequencies, because the multiplier grows in magnitude with $|\omega|$.
- Why are linearity, differentiation, and integration often better than direct integration? ::@:: Because they reduce a difficult transform to table-known signals, derivatives, or running integrals.  For example, linearity gives $3e^{-t}u(t)-2e^{-2t}u(t)\longleftrightarrow \frac{3}{1+j\omega}-\frac{2}{2+j\omega}$ immediately.
- What is the frequency-domain differentiation property? ::@:: $tf(t)\longleftrightarrow j\,dF/d\omega$.  Start from $F(\omega)=\int f(t)e^{-j\omega t}dt$.  Differentiate: $dF/d\omega=\int f(t)(-jt)e^{-j\omega t}dt=-j\mathcal{F}\{tf(t)\}$.  Hence $\mathcal{F}\{tf(t)\}=j\,dF/d\omega$.
- How does the differentiation property give the transform of $\delta'(t)$? ::@:: From $\delta(t)\longleftrightarrow 1$, differentiate in time to get $\delta'(t)\longleftrightarrow j\omega$.
- What is the transform of the running integral $y(t)=\int_{-\infty}^{t}f(\tau)\,d\tau$, and what is $F(0)$ for a transient signal? ::@:: $Y(\omega)=\frac{F(\omega)}{j\omega}+\pi F(0)\delta(\omega)$.  For a transient, $F(0)=\int f(t)dt$, the total signed area.
- How does the running-integral property give the transform of $u(t)$ from $\delta(t)$? ::@:: Write $u(t)=\int_{-\infty}^{t}\delta(\tau)d\tau$.  Use $F_{\delta}=1$, $F_{\delta}(0)=1$.  Get $u(t)\longleftrightarrow \frac{1}{j\omega}+\pi\delta(\omega)$. <br/> The extra $\pi F(0)\delta(\omega)$ term records the constant midpoint level hidden inside the accumulated step from the transient's total area.
- Why does differentiating $\delta(t)$ produce the transform $j\omega$? ::@:: Start from $\delta(t)\longleftrightarrow 1$, apply the time-domain differentiation rule to get $\delta'(t)\longleftrightarrow j\omega$.  In the transform integral, weighting by $t$ appears as differentiation with respect to $\omega$ because $\partial e^{-j\omega t}/\partial\omega=-jt e^{-j\omega t}$.  Rearranging gives $tf(t)\longleftrightarrow j\,dF/d\omega$.

### singularity promotion and demotion at the origin

For transients, the first promotion step is special because of the half-area intuition: a finite-area pulse integrates to a step, and the constant half of that step contributes $\pi F(0)\delta(\omega)$.  This is the only stage where the half-level picture is the right mnemonic.  Higher promotion stages correspond instead to genuine polynomial growth and therefore to higher derivatives of the Dirac delta.

For signals with mixed content, separate the pieces before applying the rule.  If $f(t)=g(t)+C+Kt$ with $A=\int g(t)\,dt$ finite, then integrating once gives three distinct singular behaviors at the origin: the transient part $g$ contributes $\pi A\delta(\omega)$, the dc bias $C$ contributes $j2\pi C\delta'(\omega)$, and the ramp term $Kt$ contributes $\frac{j}{2}\cdot j2\pi K\delta''(\omega)=-\pi K\delta''(\omega)$.  The transient-area delta and the promoted bias delta-prime must therefore not be conflated.

Low-order examples can look simple because the extra promotion/demotion factors may collapse to $1$ or to a small integer.  For example, promoting $\delta(\omega)$ gives $j\delta'(\omega)$, so there is no visible division by a number larger than $1$; demoting $\delta'(\omega)$ gives $-j\delta(\omega)$, so the arithmetic still looks mild.  But for higher-order singularities the full factors matter: promoting $\delta^{(n)}(\omega)$ multiplies by $j/(n+1)$, while demoting $\delta^{(n)}(\omega)$ multiplies by $-jn$.  So integration and differentiation of Dirac-delta derivatives are never just "add or remove one prime"; the coefficient must also be updated.

---

Flashcards for this section are as follows:

- If a signal has a DC bias $C$, what singular term appears after one more time integration, and why? ::@:: The existing $2\pi C\delta(\omega)$ term is promoted to $j2\pi C\delta'(\omega)$ because integrating a constant creates a ramp $Ct$.  If $f(t)=g(t)+C+Kt$ with transient area $A=\int g(t)dt$, the transient contributes $\pi A\delta(\omega)$, the DC bias contributes $j2\pi C\delta'(\omega)$, and the ramp contributes $-2\pi K\delta''(\omega)$.  These must be tracked separately.
- What is the relationship between time-domain polynomial growth and frequency-domain delta derivatives at $\omega=0$? ::@:: Each integration increases the polynomial order in time and raises the derivative order of the Dirac delta at the origin.  Constants $\to\delta(\omega)$, ramps $\to\delta'(\omega)$, quadratic growth $\to\delta''(\omega)$, etc.  The derivative order of the Dirac delta increases by one and the coefficient gains the extra factor required by the promotion rule.  In the polynomial family $t^n\longleftrightarrow 2\pi j^n\delta^{(n)}(\omega)$, integrating once raises both the time-domain polynomial degree and the frequency-domain delta-derivative order by one.
- Why is time differentiation considered a demoter of Dirac-delta singularities, and how do you derive the basic identities? ::@:: Because multiplying by $j\omega$ lowers the derivative order at the origin.  For the first step: $\langle \omega\delta'(\omega),g\rangle=\langle \delta'(\omega),\omega g(\omega)\rangle=-(\omega g)'(0)=-g(0)$, so $\omega\delta'(\omega)=-\delta(\omega)$.  More generally, $\omega\delta^{(n)}(\omega)=-n\delta^{(n-1)}(\omega)$.
- Why can low-order delta examples be deceptive when learning promotion and demotion? ::@:: Because for low orders the coefficient factors can hide.  Promoting $\delta(\omega)$ gives $j\delta'(\omega)$ and demoting $\delta'(\omega)$ gives $-j\delta(\omega)$, so it can look as if one only adds or removes a prime.  For higher orders, promotion uses $j/(n+1)$ and demotion uses $-jn$, so the coefficient must be updated as well.
- Worked example: For the mixed signal $f(t)=e^{-|t|}+5$, what are the two distinct singular components in the transform of its running integral? ::@:: The pulse part $e^{-|t|}$ has total area $2$, so its running integral contributes $\pi(2)\delta(\omega)=2\pi\delta(\omega)$. <br/> The DC bias $5$ integrates to a ramp $5t$, contributing $j2\pi(5)\delta'(\omega)=j10\pi\delta'(\omega)$.

### mechanical singularity arithmetic

For actual calculations, it is useful to strip away the outer coefficient and remember only the factorless operator acting on the bare Dirac derivative.  Starting from a pure $\delta^{(n)}(\omega)$ term with no extra scalar attached, the promotion and demotion rules are:

- __promotion under running integration__: $\delta^{(n)}(\omega)\mapsto \frac{j}{n+1}\delta^{(n+1)}(\omega)$
- __demotion under time differentiation__: $\delta^{(n)}(\omega)\mapsto -jn\,\delta^{(n-1)}(\omega)$

These are the coefficient-only forms of the polynomial transform family $t^n\longleftrightarrow 2\pi j^n\delta^{(n)}(\omega)$.  In practice, carry any existing scalar coefficient along unchanged and apply only the operator factor $\frac{j}{n+1}$ or $-jn$ to the singular part.

This gives a mechanical recipe for the running integral $y(t)=\int_{-\infty}^{t}f(\tau)\,d\tau$.  First, divide the ordinary non-singular part of $F(\omega)$ by $j\omega$.  Second, if the transient part of the input has finite area $A$, add the half-area contribution $\pi A\delta(\omega)$.  Third, promote only those existing singular terms that are already located at the origin: each term $c\,\delta^{(n)}(\omega)$ at $\omega=0$ becomes $c\,\frac{j}{n+1}\delta^{(n+1)}(\omega)$. Shifted singular terms away from the origin are not promoted; they are just divided by the nonzero number $j\omega_1$ at their support point.

There is an equally mechanical recipe for time differentiation $g(t)=\frac{d}{dt}f(t)$.  First, multiply the ordinary non-singular part of $F(\omega)$ by $j\omega$.  Second, for each singular term $c\,\delta^{(n)}(\omega)$, demote it to $c\,(-jn)\delta^{(n-1)}(\omega)$.  The special case $n=0$ vanishes because $\omega\delta(\omega)=0$, so a plain $\delta(\omega)$ term is killed by one more demotion.

The promotion/demotion pattern can be summarized compactly:

| Time Domain Operation | Singularity at $\omega=0$ | Polynomial Degree |
| :--- | :--- | :--- |
| __Differentiation__ | __Demotes__ ($\delta^{(n)} \to \delta^{(n-1)}$) | Decreases ($t^n \to t^{n-1}$) |
| __Integration__ | __Promotes__ ($\delta^{(n)} \to \delta^{(n+1)}$) | Increases ($t^n \to t^{n+1}$) |

---

Flashcards for this section are as follows:

- What is the direct promotion operator for a factorless $\delta^{(n)}(\omega)$ term? ::@:: $\delta^{(n)}(\omega)\mapsto \frac{j}{n+1}\delta^{(n+1)}(\omega)$.
- What is the direct demotion operator for a factorless $\delta^{(n)}(\omega)$ term? ::@:: $\delta^{(n)}(\omega)\mapsto -jn\,\delta^{(n-1)}(\omega)$.
- Why are the simple examples $\delta(\omega)\mapsto j\delta'(\omega)$ and $\delta'(\omega)\mapsto -j\delta(\omega)$ not enough to remember singularity arithmetic safely? ::@:: Because they hide the general coefficient update.  The real rules are $\delta^{(n)}(\omega)\mapsto \frac{j}{n+1}\delta^{(n+1)}(\omega)$ for promotion and $\delta^{(n)}(\omega)\mapsto -jn\delta^{(n-1)}(\omega)$ for demotion.
- What mechanical steps should you follow when finding the transform of a running integral? ::@:: Step 1: divide the ordinary non-singular part by $j\omega$. <br/> Step 2: if the transient part has finite area $A$, add $\pi A\delta(\omega)$. <br/> Step 3: promote only the singular terms already sitting at the origin — the ones that would otherwise be divided by zero. So each origin term $c\,\delta^{(n)}(\omega)$ becomes $c\,\frac{j}{n+1}\delta^{(n+1)}(\omega)$.
- What mechanical steps should you follow when finding the transform after time differentiation? ::@:: Step 1: multiply the ordinary non-singular part by $j\omega$. <br/> Step 2: demote every singular term $c\,\delta^{(n)}(\omega)$ to $c\,(-jn)\delta^{(n-1)}(\omega)$. <br/> Step 3: note that a plain $\delta(\omega)$ term disappears after one more demotion because $\omega\delta(\omega)=0$.
- Worked example: If a spectrum contains $c\,\delta''(\omega)$ and you integrate once in time, what happens to that singular term? ::@:: Apply the promotion rule with $n=2$: $\delta''(\omega)\mapsto \frac{j}{3}\delta'''(\omega)$. <br/> So $c\,\delta''(\omega)$ becomes $c\,\frac{j}{3}\delta'''(\omega)$.
- Worked example: If a spectrum contains $c\,\delta'''(\omega)$ and you differentiate once in time, what happens to that singular term? ::@:: Apply the demotion rule with $n=3$: $\delta'''(\omega)\mapsto -j3\,\delta''(\omega)$. <br/> So $c\,\delta'''(\omega)$ becomes $-j3c\,\delta''(\omega)$.
- Worked example: Using the promotion rule, what singular terms appear in the transform of the integral of $f(t)=2t+3$? ::@:: The constant $3$ is promoted from $2\pi\cdot 3\,\delta(\omega)$ to $j2\pi\cdot 3\,\delta'(\omega)=j6\pi\delta'(\omega)$. <br/> The ramp $2t$ is promoted from $2\cdot j2\pi\delta'(\omega)$ to $2\cdot \frac{j}{2}\cdot j2\pi\delta''(\omega)=-2\pi\delta''(\omega)$. <br/> So the integrated signal contains both a $\delta'(\omega)$ term and a $\delta''(\omega)$ term.
- Worked example: Integrate $f(t)=t^{100}$ using the promotion operator. ::@:: Start from $\mathcal{F}\{t^{100}\}=2\pi j^{100}\delta^{(100)}(\omega)=2\pi\delta^{(100)}(\omega)$. <br/> Apply the factorless promotion operator $\delta^{(100)}(\omega)\mapsto \frac{j}{101}\delta^{(101)}(\omega)$. <br/> Therefore the integrated transform is $j\frac{2\pi}{101}\delta^{(101)}(\omega)$, matching $\mathcal{F}\{t^{101}/101\}$.
- Why is partial-fraction decomposition useful in Fourier-transform problems involving rational spectra? ::@:: Because it splits a complicated rational expression into standard first-order or repeated-pole pieces that can be matched directly to known transform pairs.
- Worked example: How does partial-fraction decomposition simplify $F(\omega)=\frac{3}{(1+j\omega)(2+j\omega)}$? ::@:: Step 1: decompose it as $\frac{3}{1+j\omega}-\frac{3}{2+j\omega}$. <br/> Step 2: use the pair $1/(a+j\omega)\longleftrightarrow e^{-at}u(t)$ for $a>0$. <br/> Step 3: obtain $f(t)=3e^{-t}u(t)-3e^{-2t}u(t)$.
- Worked example: How does partial-fraction decomposition simplify the repeated-pole spectrum $F(\omega)=\frac{1}{(1+j\omega)^2(2+j\omega)}$? ::@:: Step 1: decompose it as $-\frac{1}{1+j\omega}+\frac{1}{(1+j\omega)^2}+\frac{1}{2+j\omega}$. <br/> Step 2: use $1/(a+j\omega)\longleftrightarrow e^{-at}u(t)$ and $1/(a+j\omega)^2\longleftrightarrow te^{-at}u(t)$. <br/> Step 3: obtain $f(t)=\bigl(-e^{-t}+te^{-t}+e^{-2t}\bigr)u(t)$.

### convolution and multiplication in system analysis

The convolution theorem is one of the course's main structural payoffs: if $f_1(t)\longleftrightarrow F_1(\omega)$ and $f_2(t)\longleftrightarrow F_2(\omega)$, then $(f_1*f_2)(t)\longleftrightarrow F_1(\omega)F_2(\omega)$.  Time-domain convolution becomes frequency-domain multiplication.  The dual multiplication theorem is: if $f_1(t)\longleftrightarrow F_1(\omega)$ and $f_2(t)\longleftrightarrow F_2(\omega)$, then $f_1(t)f_2(t)\longleftrightarrow \frac{1}{2\pi}(F_1*F_2)(\omega)$.

Multiplication in one domain corresponds to convolution in the other, with the normalization factor required by the course convention.  The safest memory rule is asymmetric on purpose: __time-domain multiplication__ requires the factor $1/(2\pi)$ after frequency-domain convolution, but __time-domain convolution__ corresponds to plain frequency-domain multiplication with no extra $1/(2\pi)$.  That asymmetry is exactly the course normalization, and forgetting which side carries the factor is one of the most common transform mistakes.

These theorems are not isolated property-table entries.  They are the bridge from waveform calculus to system analysis.  A linear time-invariant zero-state response is $y=h*x$, so in the frequency domain it becomes $Y(\omega)=H(\omega)X(\omega)$.  A running integral is convolution with $u(t)$, so its transform law can be understood through the convolution theorem as well as through direct property derivation.

---

Flashcards for this section are as follows:

- What explicit convolution theorem is used in this note? ::@:: If $f_1(t)\longleftrightarrow F_1(\omega)$ and $f_2(t)\longleftrightarrow F_2(\omega)$, then $(f_1*f_2)(t)\longleftrightarrow F_1(\omega)F_2(\omega)$.
- What explicit multiplication theorem is used, including the factor that is easy to forget? ::@:: If $f_1(t)\longleftrightarrow F_1(\omega)$ and $f_2(t)\longleftrightarrow F_2(\omega)$, then $f_1(t)f_2(t)\longleftrightarrow \frac{1}{2\pi}(F_1*F_2)(\omega)$.
- What is the safest way to remember the course normalization in the convolution and multiplication theorems? ::@:: Time-domain multiplication needs $1/(2\pi)$ after frequency convolution; time-domain convolution becomes plain frequency multiplication with no extra factor.
- Why are the convolution and multiplication theorems important in systems? ::@:: Because they turn LTI zero-state response from time-domain convolution into $Y=HX$ in frequency.  It is convolution with the unit step, so its frequency-domain rule can be understood as a convolution-theorem consequence as well as an integration property.
- Why does $y=h*x$ become $Y=HX$ in the Fourier domain? ::@:: The zero-state response of an LTI system is the time-domain convolution of the input with the impulse response.  Applying the convolution theorem gives $Y(\omega)=H(\omega)X(\omega)$.

## Parseval's theorem and energy spectral density

Parseval's theorem relates the total energy of a signal in the time domain to its total energy in the frequency domain.  For a signal $f(t)$ with Fourier transform $F(\omega)$, the theorem states $\int_{-\infty}^{\infty}|f(t)|^2dt=\frac{1}{2\pi}\int_{-\infty}^{\infty}|F(\omega)|^2d\omega$.  The $1/(2\pi)$ factor comes from the course convention for the inverse transform.

The quantity $|F(\omega)|^2$ is the energy spectral density.  It tells how much energy per unit angular frequency interval is present at frequency $\omega$.  Integrating $|F(\omega)|^2/(2\pi)$ over all frequencies gives the total energy, matching the time-domain integral of $|f(t)|^2$.

Parseval's theorem follows from the convolution theorem applied to $f*f^*(-t)$ evaluated at $t=0$, or equivalently from Plancherel's theorem for $L^2$ functions.  The proof uses the fact that $(f*f^*)(0)=\int f(\tau)f^*(\tau)d\tau=\int|f(\tau)|^2d\tau$, while by the convolution theorem $\mathcal{F}\{f*f^*\}=F(\omega)F^*(\omega)=|F(\omega)|^2$, so the inverse transform at $t=0$ gives $(f*f^*)(0)=\frac{1}{2\pi}\int|F(\omega)|^2d\omega$.

---

Flashcards for this section are as follows:

- What is Parseval's theorem for the Fourier transform? ::@:: $\int_{-\infty}^{\infty}|f(t)|^2dt=\frac{1}{2\pi}\int_{-\infty}^{\infty}|F(\omega)|^2d\omega$.  The total energy in the time domain equals the total energy in the frequency domain (up to the $1/(2\pi)$ factor).
- What is the energy spectral density? ::@:: $|F(\omega)|^2$ is the energy spectral density.  It tells how much energy per unit frequency interval is present at frequency $\omega$.
- Why does Parseval's theorem hold? ::@:: It follows from the convolution theorem applied to $f*f^*(-t)$ evaluated at $t=0$, or equivalently from Plancherel's theorem for $L^2$ functions.

## periodic signals in the Fourier-transform view

At first glance, Fourier transform seems to belong only to aperiodic signals and Fourier series only to periodic ones.  The lecture resolves that apparent separation by showing that periodic signals can also be described in the Fourier-transform framework, but their spectra appear as impulses rather than as ordinary continuous curves.  This section is the reverse bridge of the opening derivation: there we let Fourier-series lines densify into a continuous transform, whereas here we take a continuous-frequency picture and show how periodic repetition turns it back into discrete harmonic lines.  Together, the two notes form one Fourier analysis viewpoint, sometimes grouped under names such as the __Fourier transform analysis method__.

For the cosine and sine signals, Euler's formulas give the derivations immediately.  Since $\cos(\omega_0 t)=\frac{1}{2}e^{j\omega_0 t}+\frac{1}{2}e^{-j\omega_0 t}$ and $e^{\pm j\omega_0 t}\longleftrightarrow 2\pi\delta(\omega\mp\omega_0)$, linearity yields $\cos(\omega_0 t)\longleftrightarrow \pi\big[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)\big]$.  Likewise, $\sin(\omega_0 t)=\frac{1}{2j}e^{j\omega_0 t}-\frac{1}{2j}e^{-j\omega_0 t}$ gives $\sin(\omega_0 t)\longleftrightarrow \frac{\pi}{j}\big[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)\big]$.

The interpretation is important for recall.  A real cosine is an equal-weight superposition of the positive- and negative-frequency complex exponentials, so its spectrum is two equal impulses at $\pm\omega_0$ with the same sign.  A real sine is also built from the same two frequencies, but with opposite signs (equivalently a relative phase shift of $\pm\pi/2$), so the two impulses appear with opposite weights.  Memory cue: cosine is the even combination of $\pm\omega_0$, while sine is the odd combination.

The impulse train is the next decisive example.  Let $\operatorname{III}_T(t)=\sum_{n=-\infty}^{\infty}\delta(t-nT)$, the Dirac comb of spacing $T$.  It is an ideal periodic signal made of infinitely many equally spaced unit impulses.  It is also the most important bridge object between Fourier series and Fourier transform: in time, convolving with $\operatorname{III}_T$ creates periodic repetition; in frequency, multiplying by its transform creates sampling on a harmonic lattice.

To say "derive the impulse-train transform from Fourier-series coefficients" means the following three-step argument.  First, treat $\operatorname{III}_T(t)$ as an ordinary periodic signal of period $T$.  Second, compute its exponential Fourier-series coefficient $F_k$ over one period.  For example, over $[-T/2,T/2)$ only the impulse at $t=0$ lies inside the interval, so $F_k=\frac{1}{T}\int_{-T/2}^{T/2}\operatorname{III}_T(t)e^{-jk\omega_0 t}dt=\frac{1}{T}\int_{-T/2}^{T/2}\delta(t)e^{-jk\omega_0 t}dt=\frac{1}{T}$.  Third, substitute this constant coefficient into the periodic-signal transform formula $F(\omega)=2\pi\sum_{k=-\infty}^{\infty}F_k\delta(\omega-k\omega_0)$.  This gives $\operatorname{III}_T(t)\longleftrightarrow 2\pi\sum_{k=-\infty}^{\infty}\frac{1}{T}\delta(\omega-k\omega_0)=\frac{2\pi}{T}\sum_{k=-\infty}^{\infty}\delta(\omega-k\omega_0)=\omega_0\sum_{k=-\infty}^{\infty}\delta(\omega-k\omega_0)$, where $\omega_0=2\pi/T$.  The factor $2\pi/T$ is exactly the fundamental angular frequency $\omega_0$.

This is one of the cleanest time-frequency duality pictures in the course: periodic point concentration in one domain produces periodic point concentration in the other.  The spacing in time is $T$, the spacing in angular frequency is $\omega_0=2\pi/T$, and their product is fixed at $T\omega_0=2\pi$.  A dense comb in time gives a sparse comb in frequency, and vice versa.

The same comb pair also gives a very compact memory aid through scaling.  The self-reciprocal spacing is $T_*=\sqrt{2\pi}$, for which $\operatorname{III}_{\sqrt{2\pi}}(t)\longleftrightarrow \sqrt{2\pi}\,\operatorname{III}_{\sqrt{2\pi}}(\omega)$.  One can recall the general pair from this one by writing $\operatorname{III}_T(t)=\frac{\sqrt{2\pi}}{T}\operatorname{III}_{\sqrt{2\pi}}\!\bigl((\sqrt{2\pi}/T)t\bigr)$ and then applying the explicit scaling rule $f(at)\longleftrightarrow \frac{1}{|a|}F(\omega/a)$.  That derivation yields $\operatorname{III}_T(t)\longleftrightarrow \frac{2\pi}{T}\operatorname{III}_{2\pi/T}(\omega)=\omega_0\operatorname{III}_{\omega_0}(\omega)$ with $\omega_0=2\pi/T$.  So the comb reproduces itself exactly at the self-reciprocal scale, and all other comb pairs follow from scaling.

For a general periodic signal with exponential Fourier-series coefficients $F_k$, $F(\omega)=2\pi\sum_{k=-\infty}^{\infty}F_k\,\delta(\omega-k\omega_0)$.  This formula is the precise bridge between the Fourier series and the Fourier transform.  The Fourier-series coefficients become the weights of the spectral impulses, and the harmonic frequencies become the impulse locations.

It is worth stating this in the most atomic way possible: one single Fourier-series coefficient $F_k$ corresponds to one Fourier-transform line $2\pi F_k\,\delta(\omega-k\omega_0)$, where $\omega_0=2\pi/T$ and $T$ is the repeat period.  The factor $2\pi$ is essential.  Without it, the inverse-transform reconstruction and the coefficient comparison with Fourier series would be off by the course normalization.

One can make the bridge even more explicit by starting from an aperiodic prototype $f_0(t)$ with transform $F_0(\omega)$ and forming the periodic summation $p(t)=\sum_{n=-\infty}^{\infty}f_0(t-nT)=f_0*\operatorname{III}_T(t)$.  Since $\operatorname{III}_T(t)\longleftrightarrow \omega_0\sum_{k=-\infty}^{\infty}\delta(\omega-k\omega_0)$, convolution gives $P(\omega)=F_0(\omega)\,\omega_0\sum_{k=-\infty}^{\infty}\delta(\omega-k\omega_0)=\omega_0\sum_{k=-\infty}^{\infty}F_0(k\omega_0)\delta(\omega-k\omega_0)$.  Comparing this with $P(\omega)=2\pi\sum_{k=-\infty}^{\infty}F_k\delta(\omega-k\omega_0)$ yields $F_k=\frac{\omega_0}{2\pi}F_0(k\omega_0)=\frac{1}{T}F_0(k\omega_0)$.  The Fourier-series coefficients are samples of the continuous Fourier transform, multiplied by the explicit factor $1/T=\omega_0/(2\pi)$.

This also clarifies the two standard plotting conventions for periodic signals.  A __raw Fourier-series coefficient plot__ shows $F_k$ (y-axis) versus $k$ (x-axis).  The __Fourier-transform-style frequency plot__ shows the weighted impulses $2\pi F_k\,\delta(\omega-k\omega_0)$ or equivalently plots magnitudes $|2\pi F_k|$ (y-axis) versus $\omega=k\omega_0$ (x-axis).  Both are correct and contain the same information, but they differ in axis choice, $2\pi$ placement, and visual style.  When sketching the magnitude or phase spectrum of a periodic signal in engineering notes, the usual convention is the Fourier-transform impulse style because it emphasizes the frequency locations and allows direct comparison with aperiodic-signal spectra on the same frequency axis.  For phase, both styles carry the same phase information: $\angle F_k=\angle(2\pi F_k)$ because the factor $2\pi$ is positive and real.

This also gives the intuitive proof that frequency-domain sampling corresponds to time-domain periodic repetition.  Multiplying a continuous transform by the frequency comb $\omega_0\sum_{k=-\infty}^{\infty}\delta(\omega-k\omega_0)$ samples it on the harmonic grid.  Since that comb is itself the transform of $\operatorname{III}_T(t)$, the inverse picture is convolution with $\operatorname{III}_T(t)$, namely periodic summation every $T$ seconds: $f(t)*\operatorname{III}_T(t)=\sum_{n=-\infty}^{\infty}f(t-nT)$.  Periodicity in time and sampling in frequency are the same operation seen from opposite domains.

This is why the periodic-signal transform is not a contradiction.  A periodic signal does not have a continuous ordinary function as its Fourier transform.  Instead, it has a generalized transform made of weighted impulses.  The transform is still meaningful; it is simply more singular because exact infinite-time repetition forces the spectrum onto a harmonic lattice.

---

Flashcards for this section are as follows:

- How does the Fourier transform represent a periodic signal? ::@:: It represents a periodic signal as a weighted impulse train in frequency rather than as an ordinary continuous spectral curve.  At the beginning of the note, one starts from a periodic line spectrum and lets the period grow, so the lines become denser and approach a continuous transform.  Here one does the reverse: periodic repetition forces a continuous transform to be sampled on the harmonic grid, so the spectrum collapses back into impulses.
- What is the Fourier transform of $\cos(\omega_0 t)$? ::@:: $\pi[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)]$.
- What is the Fourier transform of $\sin(\omega_0 t)$? ::@:: $\frac{\pi}{j}[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)]$.
- Starting from Euler's formulas, how do you derive the Fourier transforms of $\cos(\omega_0 t)$ and $\sin(\omega_0 t)$? ::@:: Use $\cos(\omega_0 t)=\frac{1}{2}e^{j\omega_0 t}+\frac{1}{2}e^{-j\omega_0 t}$ and $\sin(\omega_0 t)=\frac{1}{2j}e^{j\omega_0 t}-\frac{1}{2j}e^{-j\omega_0 t}$. <br/> Then apply $e^{\pm j\omega_0 t}\longleftrightarrow 2\pi\delta(\omega\mp\omega_0)$ and linearity to obtain the two impulse pairs.
- Why do cosine and sine transform into impulses at $\pm\omega_0$? ::@:: Because an undamped sinusoid has energy at only one oscillation rate, so its spectral content is concentrated exactly at the corresponding positive and negative angular frequencies.  Cosine is the even combination of the two complex exponentials at $\pm\omega_0$, so its two impulses have equal positive weights.  Sine is the odd combination, so the two impulses carry opposite weights, equivalently a relative phase difference of $\pm\pi/2$.
- What is the Fourier transform of the periodic impulse train $\sum_n\delta(t-nT)$, and how can the prefactor be rewritten? ::@:: $\frac{2\pi}{T}\sum_k\delta(\omega-k\omega_0)=\omega_0\sum_k\delta(\omega-k\omega_0)$ with $\omega_0=2\pi/T$.
- What is the Dirac comb $\operatorname{III}_T(t)$, and how should you interpret it? ::@:: It is the impulse train $\operatorname{III}_T(t)=\sum_{n=-\infty}^{\infty}\delta(t-nT)$: infinitely many unit impulses, equally spaced by $T$. <br/> In time: convolving with it repeats a prototype every $T$ seconds. <br/> In frequency: its transform is another comb, so it acts as a perfect sampler on the harmonic lattice.
- How do you derive the impulse-train transform from Fourier-series coefficients? ::@:: Treat $\operatorname{III}_T(t)$ as periodic with period $T$.  Over $[-T/2,T/2)$ only the impulse at $t=0$ appears, so $F_k=\frac{1}{T}$.  Substitute into $F(\omega)=2\pi\sum_k F_k\delta(\omega-k\omega_0)$ to get $\operatorname{III}_T(t)\longleftrightarrow \frac{2\pi}{T}\sum_k\delta(\omega-k\omega_0)=\omega_0\sum_k\delta(\omega-k\omega_0)$.
- What is the key interpretation of the impulse-train transform pair? ::@:: Periodic point concentration in time becomes periodic point concentration in frequency, with reciprocal spacing between the impulses.
- At what spacing is the Dirac comb an eigenfunction of the Fourier transform in this convention? ::@:: When the comb spacing is self-reciprocal, so $T=\omega_0$ with $\omega_0=2\pi/T$. <br/> This gives $T=\sqrt{2\pi}$, and then $\operatorname{III}_{\sqrt{2\pi}}(t)\longleftrightarrow \sqrt{2\pi}\,\operatorname{III}_{\sqrt{2\pi}}(\omega)$.
- How does the scaling property recover the general comb pair from the self-reciprocal comb pair? ::@:: Start from the self-reciprocal pair $\operatorname{III}_{\sqrt{2\pi}}(t)\longleftrightarrow \sqrt{2\pi}\,\operatorname{III}_{\sqrt{2\pi}}(\omega)$. <br/> Write $\operatorname{III}_T(t)=\frac{\sqrt{2\pi}}{T}\operatorname{III}_{\sqrt{2\pi}}\!\bigl((\sqrt{2\pi}/T)t\bigr)$ and apply $f(at)\longleftrightarrow \frac{1}{|a|}F(\omega/a)$ with $a=\sqrt{2\pi}/T$. <br/> Then $\operatorname{III}_T(t)\longleftrightarrow \frac{2\pi}{T}\operatorname{III}_{2\pi/T}(\omega)=\omega_0\operatorname{III}_{\omega_0}(\omega)$.
- How is the Fourier transform of a general periodic signal related to its Fourier-series coefficients? ::@:: If the periodic signal has exponential Fourier-series coefficients $F_k$, then its transform is $F(\omega)=2\pi\sum_k F_k\delta(\omega-k\omega_0)$.
- What does one Fourier-series coefficient $F_k$ become inside the Fourier-transform picture of a periodic signal? ::@:: It becomes the spectral line $2\pi F_k\,\delta(\omega-k\omega_0)$, where $\omega_0=2\pi/T$. So the factor $2\pi$ is part of the actual transform line weight, not an optional decoration.
- When drawing the magnitude or phase spectrum of a periodic signal, what convention is commonly used in engineering sketches? ::@:: The usual sketch is the Fourier-transform impulse spectrum: impulses are placed at $\omega=k\omega_0$ with magnitudes $|2\pi F_k|$. The underlying Fourier-series coefficients are still $F_k$, and the phases are the same as $\angle F_k$ because the factor $2\pi$ is positive and real.
- If $p(t)=\sum_{n=-\infty}^{\infty}f_0(t-nT)$ is the periodic summation of an aperiodic prototype with transform $F_0(\omega)$, what relation connects the Fourier-series coefficients to samples of $F_0$? ::@:: Since $p(t)=f_0*\operatorname{III}_T(t)$ and $\operatorname{III}_T(t)\longleftrightarrow \omega_0\sum_k\delta(\omega-k\omega_0)$, one gets $P(\omega)=\omega_0\sum_k F_0(k\omega_0)\delta(\omega-k\omega_0)$. <br/> Comparing with $P(\omega)=2\pi\sum_k F_k\delta(\omega-k\omega_0)$ gives $F_k=\frac{\omega_0}{2\pi}F_0(k\omega_0)=\frac{1}{T}F_0(k\omega_0)$.
- Why does multiplying a continuous transform by the frequency comb $\omega_0\sum_k\delta(\omega-k\omega_0)$ correspond to repeating the signal every $T$ seconds in time? ::@:: Multiplication by that comb samples the transform on the harmonic grid.  But the same comb is the Fourier transform of the time-domain Dirac comb $\operatorname{III}_T(t)$.  Therefore the inverse-domain operation is convolution with $\operatorname{III}_T(t)$, namely $f*\operatorname{III}_T=\sum_n f(t-nT)$.  Frequency-domain sampling and time-domain periodic summation are the same bridge seen from opposite sides.
- Why is the transform of a periodic signal more singular than the transform of an aperiodic signal? ::@:: Exact infinite-time repetition concentrates spectral content at isolated harmonic frequencies, so the spectrum collapses into impulses rather than an ordinary continuous curve.  A periodic signal repeats forever, so only harmonic frequencies $k\omega_0$ are allowed, and each carries a discrete coefficient rather than a continuous density.
- How do Fourier series and Fourier transform describe the same periodic signal in two compatible ways? ::@:: Write the periodic signal as the exponential Fourier series $f(t)=\sum_{k=-\infty}^{\infty}F_k e^{jk\omega_0 t}$. <br/> Use the basic pair $e^{jk\omega_0 t}\longleftrightarrow 2\pi\delta(\omega-k\omega_0)$ and apply linearity term by term to get $F(\omega)=2\pi\sum_{k=-\infty}^{\infty}F_k\delta(\omega-k\omega_0)$. <br/> The Fourier transform is exactly the Fourier-series coefficient list rewritten as weighted impulses on the harmonic lattice.
