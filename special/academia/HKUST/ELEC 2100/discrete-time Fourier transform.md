---
aliases:
  - DTFT
  - ELEC 2100 DTFT
  - ELEC 2100 discrete-time Fourier transform
  - ELEC2100 DTFT
  - HKUST ELEC 2100 DTFT
  - discrete-time Fourier transform
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/discrete-time_Fourier_transform
  - language/in/English
---

# discrete-time Fourier transform

- HKUST ELEC 2100

<!-- check: ignore-file[two_sided_calc_warning]: concept-focused prompts intentionally use descriptive wording rather than repeating every symbol on the left-hand side -->

---

The discrete-time Fourier transform (DTFT) is the frequency-domain representation of a sequence. It is best understood in two complementary ways: as a transform formula for discrete-time data and as the spectrum of the sampled impulse train associated with that data. That second viewpoint is especially important because it explains immediately why the DTFT is periodic and why aliasing and normalized frequency belong naturally to discrete-time signal analysis.

This note covers the general-sequence DTFT. DTFS/DFS discussion lives mainly in [discrete Fourier transform](discrete%20Fourier%20transform.md), especially [§ relation between DTFS and DFT](discrete%20Fourier%20transform.md#relation%20between%20DTFS%20and%20DFT), [§ periodic sequences and discrete-time Fourier series](discrete%20Fourier%20transform.md#periodic%20sequences%20and%20discrete-time%20Fourier%20series), and [§ normalization map between DTFS and DFT](discrete%20Fourier%20transform.md#normalization%20map%20between%20DTFS%20and%20DFT), because DTFS/DFS and DFT both use finite harmonic coefficient lists for period-$N$ data. We keep enough periodic-sequence discussion here to show how a periodic sequence appears inside the DTFT as a line spectrum and to link the two notes.

This note is the general discrete-time spectral note. For continuous-time periodic and aperiodic signals, see [Fourier series](Fourier%20series.md) and [Fourier transform](Fourier%20transform.md). For finite-grid computation or explicit period-$N$ coefficient work, see [discrete Fourier transform](discrete%20Fourier%20transform.md).

---

Flashcards for this section are as follows:

- What core problem does the DTFT solve? ::@:: It describes a discrete-time sequence by a continuous periodic digital-frequency spectrum so the sequence's frequency content can be analyzed before any finite-grid sampling.
- Why is the DTFT linked to sampling theory? ::@:: Because it derives from the Fourier transform of the sampled impulse train $\sum_n x[n]\delta(t-nT)$ rather than being introduced as an isolated formula.
- Why is DTFS/DFS discussion grouped with the DFT note? ::@:: Because DTFS/DFS and DFT both use one finite harmonic coefficient cycle for period-$N$ data, while the general DTFT uses the continuous digital-frequency variable $\Omega=\omega T$ and represents periodic sequences by a line spectrum.
- How should this note be positioned among the main Fourier notes in ELEC 2100? ::@:: This note is the general discrete-time spectral description on a continuous digital-frequency axis. Fourier series and Fourier transform are the continuous-time periodic and aperiodic notes, while the DFT note is the finite-grid computational note for period-$N$ or finite-record discrete data.

## deriving the DTFT from a sampled signal

Let $x[n]=x(nT)$ be samples of a continuous-time signal. The associated sampled impulse train is $x_s(t)=\sum_{n=-\infty}^{\infty}x[n]\delta(t-nT)$. Taking its Fourier transform gives $X_s(\omega)=\int_{-\infty}^{\infty}x_s(t)e^{-j\omega t}\,dt=\int_{-\infty}^{\infty}\sum_{n=-\infty}^{\infty}x[n]\delta(t-nT)e^{-j\omega t}\,dt$. Using the sifting property of the delta function term by term yields $X_s(\omega)=\sum_{n=-\infty}^{\infty}x[n]e^{-j\omega nT}$.

The notation needs to be kept straight. $X(\omega)$ is the Fourier transform of the original signal $x(t)$. $X_s(\omega)$ is the Fourier transform of the sampled impulse train $x_s(t)$. $X(e^{j\Omega})$ is that same sampled-spectrum object rewritten in normalized digital frequency $\Omega=\omega T$. So $X(\omega)$ belongs to the original continuous-time signal, while $X_s(\omega)$ and $X(e^{j\Omega})$ belong to the sampled signal, written in analog-frequency and digital-frequency coordinates respectively.

The symbol $X(e^{j\Omega})$ should not be read as applying $e^{j\Omega}$ to the Fourier transform $X$, nor as exponentiating $X$. It means: evaluate a frequency-domain function called $X(\cdot)$ at the point $e^{j\Omega}$, exactly the same way $f(2)$ means evaluate $f$ at $2$. This notation comes from the broader transform viewpoint in which one first considers a function of a complex variable $z$ and then looks only on the unit circle $z=e^{j\Omega}$. Either $X(e^{j\Omega})$ or a new symbol like $X_d(\Omega)$ is mathematically correct, but the former is kept here for compatibility with the later unit-circle viewpoint.

The same expression becomes $X(e^{j\Omega})=\sum_{n=-\infty}^{\infty}x[n]e^{-j\Omega n}$, which is the DTFT. This step is not cosmetic. It changes the unit from radians per second to radians per sample, which is exactly the right unit for sequences indexed by sample number.

There is also a second derivation route that is very useful in engineering work. Write the sequence in impulse-decomposition form as $x[n]=\sum_{k=-\infty}^{\infty}x[k]\delta[n-k]$. If one knows the basic DTFT pair $\delta[n]\longleftrightarrow 1$, then the time-shift property gives $\delta[n-k]\longleftrightarrow e^{-j\Omega k}$. By linearity, the whole sequence therefore has DTFT $X(e^{j\Omega})=\sum_{k=-\infty}^{\infty}x[k]e^{-j\Omega k}$. So the sampled-signal derivation explains _why_ DTFT exists naturally, while the impulse-decomposition route explains _how_ engineers often compute it quickly.

---

Flashcards for this section are as follows:

- Starting from the sampled impulse train, how do you derive the DTFT formula? ::@:: Start with $x_s(t)=\sum_n x[n]\delta(t-nT)$. <br/> Take its Fourier transform: $X_s(\omega)=\int \sum_n x[n]\delta(t-nT)e^{-j\omega t}\,dt$. <br/> Use the delta sifting rule to get $X_s(\omega)=\sum_n x[n]e^{-j\omega nT}$. <br/> Define $\Omega=\omega T$ and rewrite as $X(e^{j\Omega})=\sum_n x[n]e^{-j\Omega n}$. <br/> Here $X(e^{j\Omega})$ means the DTFT value at digital frequency $\Omega$, not exponentiation of $X$.
- What is the DTFT formula for a sequence $x[n]$? ::@:: It is $X(e^{j\Omega})=\sum_{n=-\infty}^{\infty}x[n]e^{-j\Omega n}$. <br/> Here $\Omega=\omega T$ is digital angular frequency, equivalently $\Omega/(2\pi)$ cycles per sample, and one usually works on $[-\pi,\pi]$.
- What is the difference among $X(\omega)$, $X_s(\omega)$, and $X(e^{j\Omega})$? ::@:: $X(\omega)$ is the Fourier transform of the original signal $x(t)$. $X_s(\omega)$ is the Fourier transform of the sampled impulse train $x_s(t)$. $X(e^{j\Omega})$ is that same sampled-spectrum object rewritten in normalized digital frequency $\Omega=\omega T$. <br/> So $X(e^{j\Omega})$ is a relabeled sampled spectrum, not a new transform.
- Does the notation $X(e^{j\Omega})$ make sense here, and what does it mean? ::@:: Yes. It does __not__ mean exponentiating $X$. It means evaluating a frequency-domain function $X(\cdot)$ at the point $e^{j\Omega}$. In practice, one may read it simply as the DTFT at digital frequency $\Omega$. <br/> So the only exponential here is the point $e^{j\Omega}$, not the transform symbol $X$.
- If one has not yet introduced a broader complex-variable transform, is $X(e^{j\Omega})$ still a sensible notation? ::@:: Yes, but then it is best read as standard course notation for the DTFT as a function of $\Omega$. A course could equally have written $X_d(\Omega)$ or $\widetilde X(\Omega)$; the notation $X(e^{j\Omega})$ is kept because it stays compatible with the later unit-circle viewpoint.
- Why is $\Omega$ rather than $\omega$ the natural DTFT frequency variable? ::@:: Because a sequence is indexed by sample number, not by seconds, so its natural frequency unit is radians per sample. The sampling period $T$ is what converts between analog frequency $\omega$ and digital frequency $\Omega$.
- Why does the notation $X(e^{j\Omega})$ hint at a unit-circle viewpoint? ::@:: Because the complex number $e^{j\Omega}$ lies on the unit circle, so the notation can be read as evaluating a function $X(z)$ at points $z=e^{j\Omega}$ on that circle rather than along a straight nonperiodic frequency axis.
- How does the time-shift property give an engineering derivation of the DTFT formula? ::@:: Write $x[n]=\sum_k x[k]\delta[n-k]$. <br/> Use the basic pair $\delta[n]\longleftrightarrow 1$. <br/> Apply the shift rule: $\delta[n-k]\longleftrightarrow e^{-j\Omega k}$. <br/> By linearity, $X(e^{j\Omega})=\sum_k x[k]e^{-j\Omega k}$.
- How should you compare the ordinary Fourier transform with the DTFT? ::@:: The ordinary Fourier transform is $X(\omega)=\int_{-\infty}^{\infty}x(t)e^{-j\omega t}\,dt$, while the DTFT is $X(e^{j\Omega})=\sum_{n=-\infty}^{\infty}x[n]e^{-j\Omega n}$. <br/> The continuous-time integral becomes a sum over sample indices because a sequence exists only at discrete instants.

## periodicity and inverse DTFT

The DTFT is periodic with period $2\pi$ because $e^{-j(\Omega+2\pi)n}=e^{-j\Omega n}e^{-j2\pi n}=e^{-j\Omega n}$ for every integer $n$. Therefore each term in the DTFT sum is unchanged when $\Omega$ is replaced by $\Omega+2\pi$, and so $X(e^{j(\Omega+2\pi)})=X(e^{j\Omega})$.

This is one of the deepest differences between discrete-time and continuous-time Fourier analysis. In continuous time, different angular frequencies correspond to genuinely different exponentials. In discrete time, frequencies that differ by integer multiples of $2\pi$ per sample produce exactly the same sequence values, so the spectrum must wrap around modulo $2\pi$.

The inverse DTFT therefore needs only one full period, usually $[-\pi,\pi]$: $x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X(e^{j\Omega})e^{j\Omega n}\,d\Omega$. The point of this formula is not just recovery. It says one period of the DTFT already contains all distinct information, and everything outside that interval is repetition.

The inverse DTFT can be derived explicitly from the forward DTFT formula. Start with $\frac{1}{2\pi}\int_{-\pi}^{\pi}X(e^{j\Omega})e^{j\Omega m}\,d\Omega$ and substitute $X(e^{j\Omega})=\sum_{n=-\infty}^{\infty}x[n]e^{-j\Omega n}$. This gives $\sum_{n=-\infty}^{\infty}x[n]\frac{1}{2\pi}\int_{-\pi}^{\pi}e^{j\Omega(m-n)}\,d\Omega$. The integral is $1$ when $m=n$ and $0$ otherwise, so only one term survives and the result is $x[m]$. This is the discrete-frequency orthogonality behind the inverse DTFT.

Comparing with the ordinary inverse Fourier transform: in continuous time, $x(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}X(\omega)e^{j\omega t}\,d\omega$ integrates over the whole nonperiodic analog-frequency axis. In discrete time, $x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X(e^{j\Omega})e^{j\Omega n}\,d\Omega$ needs only one period because the DTFT repeats modulo $2\pi$.

Because $X(e^{j\Omega})$ is $2\pi$-periodic in $\Omega$, it can be expanded as a complex Fourier series: $F(\Omega)=\sum_{n=-\infty}^{\infty}c_n e^{-jn\Omega}$ with $c_n=\frac{1}{2\pi}\int_{-\pi}^{\pi}F(\Omega)e^{jn\Omega}\,d\Omega$. Comparing with the DTFT pair shows that $X(e^{j\Omega})$ is the Fourier-series synthesis and $x[n]$ are exactly the Fourier-series coefficients. So the DTFT can be viewed as Fourier series in reverse analysis: instead of starting with a periodic waveform in time and extracting line-spectrum coefficients, one starts with a sequence and synthesizes a periodic function of digital frequency.

The forward DTFT $X(e^{j\Omega})=\sum_n x[n]e^{-jn\Omega}$ is Fourier-series synthesis in the variable $\Omega$, and the inverse DTFT $x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X(e^{j\Omega})e^{jn\Omega}\,d\Omega$ is Fourier-series coefficient extraction. The important warning is convention. Different books place the sign or the $1/(2\pi)$ factor differently. In this course the negative sign appears in the synthesis-like DTFT formula and the factor $1/(2\pi)$ appears in the inverse-like coefficient formula, so one must match the course convention before invoking the Fourier-series correspondence from memory.

For a periodic sequence $\tilde x[n]$ with period $N$ and fundamental digital angular frequency $\Omega_0=2\pi/N$, the DTFT becomes a line spectrum: $X(e^{j\Omega})=2\pi\sum_{k=0}^{N-1}\tilde X[k]\sum_{m=-\infty}^{\infty}\delta(\Omega-k\Omega_0-2\pi m)$. The detailed periodic-sequence theory is housed mainly in [discrete Fourier transform](discrete%20Fourier%20transform.md). If the task is to work with period-$N$ coefficient formulas, circular rules, or the exam distinction between explicit periodicity and implicit periodic extension, the DFT note is the canonical home.

---

Flashcards for this section are as follows:

- Why is the DTFT periodic with period $2\pi$? ::@:: Because for every integer $n$, $e^{-j(\Omega+2\pi)n}=e^{-j\Omega n}$, so adding $2\pi$ to the digital frequency changes none of the DTFT terms.
- What is the inverse DTFT formula? ::@:: It is $x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X(e^{j\Omega})e^{j\Omega n}\,d\Omega$. Only one principal period $[-\pi,\pi]$ is needed.
- Why is one interval enough for the inverse DTFT? ::@:: Because the DTFT repeats every $2\pi$, so one complete period contains all distinct spectral information.
- What is the conceptual difference between the DTFT and the continuous-time Fourier transform? ::@:: The continuous-time transform uses a nonperiodic frequency axis, while the DTFT wraps frequency modulo $2\pi$ because discrete time only distinguishes frequency up to integer multiples of $2\pi$.
- Why is DTFT periodicity the spectral version of alias equivalence? ::@:: Because the sequences $e^{j\Omega n}$ and $e^{j(\Omega+2\pi m)n}$ are identical for every integer $m$, so discrete time cannot tell those analog frequencies apart after normalization.
- Worked example: What DTFT should you expect for $x[n]=\delta[n]$? ::@:: Substitute $x[n]=\delta[n]$ into $X(e^{j\Omega})=\sum_n x[n]e^{-j\Omega n}$. <br/> Only the $n=0$ term survives, so $X(e^{j\Omega})=1$ for every $\Omega$. <br/> This shows one sample at the origin spreads uniformly across all digital frequencies.
- How do you derive the inverse DTFT from the forward DTFT formula? ::@:: Start with $\frac{1}{2\pi}\int_{-\pi}^{\pi}X(e^{j\Omega})e^{j\Omega m}\,d\Omega$. <br/> Substitute $X(e^{j\Omega})=\sum_n x[n]e^{-j\Omega n}$. <br/> Swap the sum and the integral. <br/> Use $\frac{1}{2\pi}\int_{-\pi}^{\pi}e^{j\Omega(m-n)}\,d\Omega=1$ when $m=n$ and $0$ otherwise. <br/> Only the $n=m$ term survives, giving $x[m]$.
- How should you compare the ordinary inverse Fourier transform with the inverse DTFT? ::@:: The ordinary inverse Fourier transform is $x(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}X(\omega)e^{j\omega t}\,d\omega$, while the inverse DTFT is $x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X(e^{j\Omega})e^{j\Omega n}\,d\Omega$. <br/> The continuous-time inverse integrates over the whole nonperiodic analog-frequency axis, but the inverse DTFT needs only one digital-frequency period.
- Why can the DTFT pair be viewed as a Fourier-series pair in the variable $\Omega$? ::@:: Because $X(e^{j\Omega})$ is $2\pi$-periodic in $\Omega$, so it can be expanded as a complex Fourier series. The sequence values $x[n]$ are exactly the Fourier-series coefficients of the periodic spectral function.
- What does "DTFT is Fourier series in reverse analysis" mean? ::@:: It means one starts with the sequence coefficients $x[n]$ and synthesizes the periodic function $X(e^{j\Omega})$ of digital frequency, whereas in ordinary Fourier-series analysis one starts with a periodic function and extracts its coefficients.
- Why must you be careful about conventions when linking DTFT with Fourier series? ::@:: Because different texts place the sign in the exponential and the factor $1/(2\pi)$ in different places. In this course the negative sign is in $X(e^{j\Omega})=\sum_n x[n]e^{-jn\Omega}$ and the factor $1/(2\pi)$ is in $x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X(e^{j\Omega})e^{jn\Omega}\,d\Omega$.
- How should you distinguish the DTFT Fourier-series viewpoint from DTFS? ::@:: In DTFT, the periodic object is the spectrum $X(e^{j\Omega})$ as a function of $\Omega$, and the sequence values $x[n]$ play the role of Fourier-series coefficients. In DTFS, the periodic object is the sequence itself in $n$, and the harmonic coefficients are indexed by $k$.
- If a sequence is periodic in time, how does it appear in the DTFT? ::@:: Its DTFT becomes a periodic line spectrum: impulses appear at the harmonic frequencies $\Omega=k\Omega_0$ and repeat every $2\pi$. A finite harmonic description is usually cleaner than carrying the impulse train explicitly.
- Why does the DTFT note hand most periodic-sequence details over to the DFT note? ::@:: Because once a sequence is period $N$, the most natural language is the finite harmonic coefficient list used by DTFS/DFS and DFT. The continuous-variable DTFT still exists, but packages those same harmonics inside a line spectrum, so the algebraically closer home is the DFT note.

## analog frequency, digital frequency, and Nyquist range

The three common frequency variables are ordinary frequency $f$ in hertz, continuous-time angular frequency $\omega=2\pi f$ in radians per second, and digital angular frequency $\Omega=\omega T=2\pi f/f_s$ in radians per sample. The DTFT belongs naturally to the last one.

When $\Omega=\pi$, we have $f=f_s/2$, the Nyquist frequency. So the principal DTFT interval $[-\pi,\pi]$ corresponds to $[-f_s/2,f_s/2]$.

The mapping from analog to digital frequency is many-to-one. If two analog frequencies differ by an integer multiple of $f_s$, their digital angular frequencies differ by an integer multiple of $2\pi$ and represent the same discrete-time oscillation. This is why normalized frequency is the right language for sequences and why aliasing is unavoidable once sampling has already taken place.

---

Flashcards for this section are as follows:

- How are $f$, $\omega$, and $\Omega$ related? ::@:: They satisfy $\omega=2\pi f$ and $\Omega=\omega T=2\pi f/f_s$. <br/> So $\Omega$ is digital angular frequency, and $\Omega/(2\pi)=f/f_s$ is cycles per sample.
- Why is $\Omega$ the natural DTFT variable? ::@:: Because the DTFT describes sequences indexed by sample number, so frequency is measured in radians per sample rather than radians per second.
- What physical frequency corresponds to $\Omega=\pi$? ::@:: It corresponds to $f=f_s/2$, the Nyquist frequency.
- What physical frequency range corresponds to the principal DTFT interval $[-\pi,\pi]$? ::@:: It corresponds to the ordinary-frequency range $[-f_s/2,f_s/2]$.
- Why can different analog frequencies correspond to the same digital frequency? ::@:: Because $\Omega=2\pi f/f_s=\omega T$ is periodic modulo $2\pi$, so adding integer multiples of $f_s$ to the analog frequency adds integer multiples of $2\pi$ to the digital frequency and leaves the discrete-time sequence unchanged.
- Worked example: Why do analog frequencies $f=f_s/4$ and $f=5f_s/4$ give the same digital frequency? ::@:: Their digital frequencies are $\Omega=2\pi(f_s/4)/f_s=\pi/2$ and $\Omega=2\pi(5f_s/4)/f_s=5\pi/2=\pi/2\pmod{2\pi}$. So the corresponding discrete-time complex exponentials are identical.

## sampled-spectrum interpretation of the DTFT

From sampling theory, $X_s(\omega)=\frac{1}{T}\sum_{k=-\infty}^{\infty}X(\omega-k\omega_s)$ with $\omega_s=2\pi/T$. But from the impulse-train derivation, $X_s(\omega)=\sum_{n=-\infty}^{\infty}x[n]e^{-j\omega nT}=X(e^{j\omega T})=X(e^{j\Omega})$. So the DTFT is exactly the sampled-signal spectrum written in normalized frequency.

Keep the symbols straight: $X(\omega)$ inside $\frac{1}{T}\sum_k X(\omega-k\omega_s)$ is the spectrum of the original signal before sampling. $X_s(\omega)$ is the spectrum after sampling, periodic in $\omega$ because sampling has created shifted copies. $X(e^{j\Omega})$ is just $X_s(\omega)$ after the axis substitution $\Omega=\omega T$. The chain is: original analog spectrum $X(\omega)$ $\to$ sampled analog spectrum $X_s(\omega)$ $\to$ the same spectrum in digital frequency $X(e^{j\Omega})$.

This viewpoint explains three facts: the copies are spaced by $\omega_s$ in analog frequency, their heights are scaled by $1/T$, and after the change of variable $\Omega=\omega T$, the copy spacing becomes $\omega_s T=2\pi$, which is exactly the DTFT period.

---

Flashcards for this section are as follows:

- How is the DTFT related to the continuous-time spectrum of the sampled impulse train? ::@:: They are the same object: $X_s(\omega)=\sum_n x[n]e^{-j\omega nT}=X(e^{j\omega T})=X(e^{j\Omega})$. <br/> $X(e^{j\Omega})$ is just the sampled spectrum rewritten using digital frequency $\Omega=\omega T$.
- What replicated-spectrum formula from sampling theory helps interpret the DTFT? ::@:: It is $X_s(\omega)=\frac{1}{T}\sum_{k=-\infty}^{\infty}X(\omega-k\omega_s)$, showing that the sampled spectrum is periodic in $\omega$ and therefore periodic in $\Omega$ as well.
- In the sampled-spectrum formula, what does $X(\omega)$ mean? ::@:: It is the Fourier transform of the original unsampled signal $x(t)$, whose shifted copies appear after sampling.
- Why does the sampled-spectrum viewpoint make DTFT periodicity obvious? ::@:: Because the sampled continuous-time spectrum repeats every $\omega_s$, and after scaling by $T$ that spacing becomes exactly $2\pi$ in digital frequency.
- What is the best quick intuition for the DTFT? ::@:: It is the normalized spectrum of the sampled impulse train.
- Why does increasing the sampling frequency spread the replicated spectra farther apart? ::@:: Because the copy spacing is $\omega_s=2\pi/T$. A smaller sampling interval $T$ means a larger $\omega_s$, so the spectral replicas are separated by a wider gap before normalization.

## existence and basic symmetry

A standard sufficient condition for the DTFT to exist as an ordinary convergent sum is absolute summability: $\sum_{n=-\infty}^{\infty}|x[n]|<\infty$. This is the discrete-time analogue of absolute integrability for the continuous-time Fourier transform. Any finite-length sequence satisfies this condition automatically, which is one reason finite-duration examples are so easy to transform directly.

If the sequence is real valued, the DTFT satisfies conjugate symmetry: $X(e^{-j\Omega})=X^*(e^{j\Omega})$. Consequently the magnitude is even and the phase is odd when tracked on a consistent branch. These are not just pretty identities; they are fast plausibility tests for sketches and algebra.

More structure appears when parity is also known. A real even sequence gives a real even DTFT, while a real odd sequence gives an imaginary odd DTFT. In practice, these symmetry rules often reveal the answer before any sum is fully evaluated.

---

Flashcards for this section are as follows:

- What is a standard sufficient condition for a DTFT to converge? ::@:: It is $\sum_{n=-\infty}^{\infty}|x[n]|<\infty$. Any finite-length sequence satisfies this automatically.
- What conjugate-symmetry rule does the DTFT of a real sequence satisfy? ::@:: It satisfies $X(e^{-j\Omega})=X^*(e^{j\Omega})$.
- If a sequence is real, what symmetry do the DTFT magnitude and phase have? ::@:: The magnitude is even and the phase is odd on a consistent branch.
- Why are symmetry checks useful in DTFT work? ::@:: Because they reveal quickly whether an algebraic result or spectral sketch is compatible with the reality and parity of the original sequence.
- Why do finite-length sequences automatically have a well-defined DTFT as an ordinary sum? ::@:: Because only finitely many terms are nonzero, so the sum is automatically absolutely summable.
- What extra parity rules hold when the sequence is real and even or real and odd? ::@:: A real even sequence gives a real even DTFT, while a real odd sequence gives an imaginary odd DTFT.
- How do reality and parity together sharpen DTFT expectations before you calculate anything? ::@:: Realness gives conjugate symmetry, then parity sharpens that further: a real even sequence leads you to expect a real even DTFT, while a real odd sequence leads you to expect an imaginary odd DTFT.
