---
aliases:
  - ELEC 2100 discrete signal
  - ELEC 2100 discrete signals
  - ELEC 2100 discrete-time signal
  - ELEC 2100 discrete-time signals
  - ELEC2100 discrete-time signal
  - ELEC2100 discrete-time signals
  - HKUST ELEC 2100 discrete-time signal
  - HKUST ELEC 2100 discrete-time signals
  - discrete signal
  - discrete signals
  - discrete-time signal
  - discrete-time signals
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/discrete-time_signal
  - language/in/English
---

# discrete-time signal

- HKUST ELEC 2100

<!-- check: ignore-file[two_sided_calc_warning]: concept-focused prompts intentionally use descriptive wording rather than repeating every symbol on the left-hand side -->

---

Discrete-time signals are indexed by integers instead of a continuous variable. In ELEC 2100 they arise both as sampled continuous-time signals and as native sequences, so the course covers their representation, common families, and periodicity rules.

This note is the sequence toolkit. Broader signal vocabulary stays in [signal](signal.md); continuous-time step/impulse machinery lives in [singular signal](singular%20signal.md).

---

Flashcards for this section are as follows:

- What is a discrete-time signal? ::@:: A signal indexed by integers, written as a sequence $x[n]$ rather than a continuous function $x(t)$.
- Why study discrete-time signals in ELEC 2100? ::@:: They arise from sampling continuous-time signals and as native sequences, so they need their own representation and periodicity rules.
- How does this note relate to `signal.md` and `singular signal.md`? ::@:: Use this note for the sequence toolkit. `signal.md` covers broader signal vocabulary; `singular signal.md` covers continuous-time generalized functions.

## representation methods

A discrete-time signal can be written as a sequence list, an explicit formula for $x[n]$, or a stem plot where the horizontal axis is integer index $n$ and each vertical stem height is the sample magnitude. The upward arrow in list notation marks the sample at $n=0$.

If sampled uniformly from a continuous signal $x_s(t)$ at interval $T_s$, the sequence is $x[n]=x_s(nT_s)$. The independent variable shifts from physical time $t$ to integer index $n$.

The lecture example $x[n]=2^n u[n]$ shows how the three forms fit together. List: $\{\ldots,0,0,0,1,2,4,8,\ldots\}$ with the arrow under $n=0$. Formula: the piecewise definition. Waveform: one stem per integer $n$, with heights $1,2,4,8,\ldots$ for $n\ge 0$ and zero stems for negative indices.

---

Flashcards for this section are as follows:

- What are the main representation methods for a discrete-time signal? ::@:: Sequence values, an explicit formula for $x[n]$, or a stem plot indexed by $n$.
- In a stem plot, what does each stem height represent? ::@:: The magnitude of the corresponding sample value.
- What does the upward arrow mean in sequence notation? ::@:: It marks the sample at $n=0$.
- How is a uniformly sampled continuous-time signal written as a sequence? ::@:: $x[n]=x_s(nT_s)$, where $T_s$ is the sampling interval.
- Why is $n$ the independent variable? ::@:: Because the signal is described at integer indices, not at every continuous instant.
- Worked example: If $x[n]=2^n u[n]$, how does its sequence begin around the origin? ::@:: $x[0]=1$, $x[1]=2$, $x[2]=4$, $x[3]=8$, with $x[n]=0$ for $n<0$. Sequence: $\{\ldots,0,0,0,1,2,4,8,\ldots\}$ with the arrow under $1$ at $n=0$.
- Worked example: How should the waveform of $x[n]=2^n u[n]$ be drawn? ::@:: Mark integer indices on the $n$ axis. For $n<0$, draw zero stems. For $n=0,1,2,3,\ldots$, draw stems with heights $1,2,4,8,\ldots$.

## support patterns

Sequences are classified by how far their nonzero samples extend. A __one-sided__ sequence is nonzero only for $n\ge 0$. A __two-sided__ sequence has nonzero values on both sides. A __finite-length__ sequence is nonzero only over a bounded set of indices.

Support patterns help read formulas quickly. A factor $u[n]$ signals a one-sided sequence. Finitely many shifted impulses means finite-length. $a^n$ without a gate is naturally two-sided.

---

Flashcards for this section are as follows:

- What is a one-sided sequence? ::@:: A sequence nonzero only for $n\ge 0$.
- What is a two-sided sequence? ::@:: A sequence with nonzero samples on both sides of the index axis.
- What is a finite-length sequence? ::@:: A sequence nonzero only over a bounded set of indices.
- Why do support patterns matter? ::@:: They help you quickly tell whether a sequence is one-sided, two-sided, or finite-length.
- What does $u[n]$ usually signal about a sequence? ::@:: The sequence is one-sided and starts at or after $n=0$.

## unit sample sequence

The unit sample sequence (Kronecker delta) is $\delta[n]=1$ for $n=0$ and $\delta[n]=0$ for $n\neq 0$. Unlike the continuous-time impulse, this is an ordinary sequence, not a generalized function.

Shifting gives $\delta[n-j]$, placing the unit sample at index $n=j$. Scaling gives $c\,\delta[n-j]$, setting the sample value at that index to $c$. The sampling property is $f[n]\delta[n]=f[0]\delta[n]$: multiplication by $\delta[n]$ kills all indices except the origin.

The unit sample is the building block for all sequences. Any sequence can be written as $x[n]=\sum_{m=-\infty}^{\infty}x[m]\delta[n-m]$ — the discrete-time analogue of building a signal from weighted shifted impulses.

For example, $x[-1]=-1.5$, $x[1]=1$, $x[3]=3$ (zeros elsewhere) becomes $x[n]=-1.5\delta[n+1]+\delta[n-1]+3\delta[n-3]$.

---

Flashcards for this section are as follows:

- What is the unit sample sequence? ::@:: $\delta[n]=1$ at $n=0$ and $0$ elsewhere; an ordinary sequence, not a generalized function.
- What does $\delta[n-j]$ represent? ::@:: A shifted unit sample at index $n=j$.
- What is the sampling property? ::@:: $f[n]\delta[n]=f[0]\delta[n]$: only the value at the origin survives.
- How can any sequence be written using unit samples? ::@:: $x[n]=\sum_{m=-\infty}^{\infty}x[m]\delta[n-m]$.
- Worked example: How is $x[-1]=-1.5$, $x[1]=1$, $x[3]=3$ written with unit samples? ::@:: $x[n]=-1.5\delta[n+1]+\delta[n-1]+3\delta[n-3]$, one term per nonzero sample.

## unit step and rectangular sequence

The discrete-time unit step is $u[n]=1$ for $n\ge 0$ and $u[n]=0$ for $n<0$. It switches on a sequence at the origin. As an infinite sum of unit samples: $u[n]=\sum_{k=0}^{\infty}\delta[n-k]$.

The step and sample are related by $\delta[n]=u[n]-u[n-1]$: a jump is isolated by taking a difference.

A rectangular sequence of length $N$ is $R_N[n]=1$ for $0\le n\le N-1$ and $0$ otherwise. The endpoint convention: $n=0$ is included, $n=N$ is excluded. Written as $R_N[n]=u[n]-u[n-N]$ or $R_N[n]=\sum_{k=0}^{N-1}\delta[n-k]$.

Three viewpoints: step view (switching on/off), impulse-sum view (finite support), graph view (flat run of ones).

---

Flashcards for this section are as follows:

- What is the discrete-time unit step? ::@:: $u[n]=1$ for $n\ge 0$, $u[n]=0$ for $n<0$.
- How can the unit step be written as a sum of unit samples? ::@:: $u[n]=\sum_{k=0}^{\infty}\delta[n-k]$.
- What is the relation between unit sample and unit step? ::@:: $\delta[n]=u[n]-u[n-1]$.
- What is a rectangular sequence of length $N$? ::@:: $R_N[n]=1$ for $0\le n\le N-1$ and $0$ otherwise ($n=0$ included, $n=N$ excluded).
- How is the rectangular sequence written with steps? ::@:: $R_N[n]=u[n]-u[n-N]$.
- How is the rectangular sequence written with unit samples? ::@:: $R_N[n]=\sum_{k=0}^{N-1}\delta[n-k]$.
- Why is the endpoint convention of $R_N[n]=u[n]-u[n-N]$ easy to misread? ::@:: The step form shows switch-on at $n=0$ and switch-off at $n=N$, so support includes $0$ through $N-1$ only.

## ramp and one-sided exponential sequences

The discrete-time ramp is $x[n]=nu[n]$: zero for negative indices, growing linearly for $n\ge 0$.

A one-sided exponential is $x[n]=a^n u[n]$. Behavior depends on $a$:

- $0<a<1$: positive, decays to zero.
- $a>1$: positive, grows without bound.
- $-1<a<0$: alternates sign, magnitude decays.
- $a<-1$: alternates sign, magnitude grows.

A negative $a$ flips the sign at every sample, not just once.

---

Flashcards for this section are as follows:

- What is the discrete-time ramp? ::@:: $x[n]=nu[n]$: zero for $n<0$, grows linearly for $n\ge 0$.
- What is a one-sided exponential? ::@:: $x[n]=a^n u[n]$.
- How does $a^n u[n]$ behave? ::@:: $|a|<1$ decays, $|a|>1$ grows. $a>0$ is monotone; $a<0$ alternates sign every sample. <br/> Examples: $a=0.5$ → $1,0.5,0.25,\ldots$; $a=-0.5$ → $1,-0.5,0.25,-0.125,\ldots$; $a=-1.5$ → $1,-1.5,2.25,-3.375,\ldots$.

## sinusoidal and complex exponential sequences

A discrete-time sinusoid is $x[n]=\sin(\omega n)$ or $x[n]=A\sin(\omega n+\phi)$, where $\omega$ is in radians per sample. If sampled from $x(t)=A\sin(\omega_0 t+\phi)$ at interval $T_s$, then $\omega=\omega_0 T_s=2\pi f_0/f_s$.

__Periodicity rule.__ A sinusoidal sequence is periodic only if $\omega/(2\pi)$ is rational. If rational, some integer period exists. If irrational, no integer period can make the samples repeat, so the sequence is aperiodic.

When $\omega/(2\pi)=m/N_0$ in lowest terms, $N_0$ is the fundamental period and $2\pi/N_0$ is the fundamental digital frequency. The sinusoid itself is the $m$-th harmonic on that grid. $x[n]=\sin((4\pi/11)n)$ repeats every $11$ samples: the fundamental period is $11$, and the sinusoid is the second harmonic relative to $2\pi/11$.

__Do not confuse the written angular parameter with fundamental digital frequency.__ Digital frequency is defined modulo $2\pi$, and for real sinusoids one often folds to $0\le \omega\le \pi$. __Key examples.__ $x[n]=2\cos(n/6)$: periodicity requires $N/6=2\pi m$, forcing $1/(12\pi)$ to be rational. Since $\pi$ is irrational, no period exists.

$x[n]=2\cos(11\pi n/4)$: regroup as $11\pi n/4=2\pi n+3\pi n/4$. The effective phase step is $3\pi/4$. The smallest $N$ with $3N/4=2m$ is $N=8$, so the fundamental period is $8$ and fundamental digital frequency is $\pi/4$. The displayed cosine is the third harmonic, not the fundamental.

To read a full period from a finite plot, start at the smallest displayed index and count $N_0$ consecutive samples.

More examples:

- $x[n]=\sin(0.2\pi n)$: $\omega=0.2\pi$, period $10$.
- $x[n]=\sin((4\pi/11)n)$: period $11$, two cycles per period.
- $x[n]=\sin(0.4n)$: $0.4/(2\pi)$ is irrational, so aperiodic.

Key point: irrationality destroys exact repetition.

The complex exponential is $x[n]=e^{j\omega n}=\cos(\omega n)+j\sin(\omega n)$, with $|x[n]|=1$ and $\arg x[n]=\omega n$. It is periodic iff $\omega/(2\pi)$ is rational — the same rule as the real sinusoid.

The real sinusoid gives one coordinate; the complex exponential packages cosine and sine into one rotating sequence. Both become building blocks in Fourier analysis. Irrationality has the same effect in both: an incommensurate rotation angle prevents exact repetition.

---

Flashcards for this section are as follows:

- What is a discrete-time sinusoid? ::@:: $x[n]=\sin(\omega n)$ or $x[n]=A\sin(\omega n+\phi)$, with $\omega$ in radians per sample.
- How is it obtained from sampling a continuous sinusoid? ::@:: $\omega=\omega_0 T_s=2\pi f_0/f_s$.
- What is the fundamental period when $\omega/(2\pi)=m/N_0$ (lowest terms)? ::@:: Period is $N_0$ samples; fundamental digital frequency is $2\pi/N_0$; the sinusoid is the $m$-th harmonic.
- Why can a discrete-time sinusoid be aperiodic? ::@:: Because $\omega/(2\pi)$ is irrational, so no integer period exists.
- Why is the written angular parameter not always the fundamental digital frequency? ::@:: Digital frequency is modulo $2\pi$; the written angle may be a higher harmonic.
- Worked example: $x[n]=2\cos(n/6)$ — is it periodic? ::@:: No. Periodicity requires $1/(12\pi)$ to be rational, which is false.
- Worked example: $x[n]=2\cos(11\pi n/4)$ — what is its fundamental frequency? ::@:: Regroup as $2\pi n+3\pi n/4$; effective step is $3\pi/4$; $N=8$; fundamental digital frequency is $\pi/4$.
- Worked example: $x[n]=\sin(0.4n)$ — periodic? ::@:: No, $0.4/(2\pi)$ is irrational.
- What is the discrete-time complex exponential? ::@:: $x[n]=e^{j\omega n}=\cos(\omega n)+j\sin(\omega n)$, magnitude $1$, phase $\omega n$.
- When is $e^{j\omega n}$ periodic? ::@:: If and only if $\omega/(2\pi)$ is rational.

## pointwise operations and index transformations

Pointwise operations act sample by sample at the same index: $z[n]=x[n]+y[n]$ (summation), $z[n]=x[n]y[n]$ (multiplication), $z[n]=ax[n]$ (scaling). Indices must be aligned before combining.

__Scaling vs. shifting.__ Scaling ($z[n]=2x[n]$) changes values but not positions. Shifting ($z[n]=x[n-m]$) moves positions but not values. For $m>0$: $x[n-m]$ shifts right, $x[n+m]$ shifts left. Time reversal $z[n]=x[-n]$ reflects the sequence about the origin.

Shifting preserves sample order; reversal flips it. For a sample originally at index $n_0$: reversal puts it at $-n_0$, right shift by $m$ puts it at $n_0+m$.

For example, if $x[n]=\{1,2,3,4\}$ and $y[n]=\{1,1,1,0\}$, then $x[n]+y[n]=\{2,3,4,4\}$ and $x[n]y[n]=\{1,2,3,0\}$. The same example also shows scaling: $2x[n]=\{2,4,6,8\}$.

---

Flashcards for this section are as follows:

- What are pointwise operations? ::@:: Operations that act sample by sample: $x[n]+y[n]$, $x[n]y[n]$, or $ax[n]$.
- Why must indices be aligned first? ::@:: Because operations combine values at the same index, not adjacent positions.
- How does scaling differ from shifting? ::@:: Scaling changes values without moving positions; shifting moves positions without changing values.
- What does $x[n-m]$ do ($m>0$)? ::@:: Shifts the sequence right by $m$ samples.
- What does time reversal do? ::@:: $z[n]=x[-n]$: reflects the sequence about the origin, flipping sample order.
- What is the difference between shifting and reversal? ::@:: Shifting preserves order; reversal flips it.
- Worked example: If $x[n]=\{1,2,3,4\}$ and $y[n]=\{1,1,1,0\}$, what are $x+y$ and $xy$? ::@:: $x[n]+y[n]=\{2,3,4,4\}$, $x[n]y[n]=\{1,2,3,0\}$.

## difference and running sum

Discrete differentiation uses differences. The __forward difference__ is $\Delta x[n]=x[n+1]-x[n]$ (look-ahead). The __backward difference__ is $\nabla x[n]=x[n]-x[n-1]$ (causal, looking past-to-present).

The __running sum__ is the discrete integral: $y[n]=\sum_{k=-\infty}^{n}x[k]$. Each output accumulates all past samples, making it a cumulative-memory operation.

Example: $x[0]=1$, $x[1]=2$, $x[2]=3$, $x[3]=4$ (zeros elsewhere) gives $y[0]=1$, $y[1]=3$, $y[2]=6$, $y[3]=10$.

---

Flashcards for this section are as follows:

- What is the forward difference? ::@:: $\Delta x[n]=x[n+1]-x[n]$ (compares current with next).
- What is the backward difference? ::@:: $\nabla x[n]=x[n]-x[n-1]$ (compares current with previous).
- What is the running sum? ::@:: $y[n]=\sum_{k=-\infty}^{n}x[k]$: accumulates all samples up to index $n$.
- Why is the running sum not pointwise? ::@:: Each output depends on all past samples, not just the sample at that index.
- Worked example: $x[0]=1$, $x[1]=2$, $x[2]=3$, $x[3]=4$ (zeros elsewhere) — what are the first four running-sum values? ::@:: $y[0]=1$, $y[1]=3$, $y[2]=6$, $y[3]=10$.

## decimation and interpolation

Reshaping operations change sampling density. __Decimation__ keeps fewer samples: for integer $N>0$, $x[Nn]$ keeps samples at multiples of $N$, compressing the sequence.

__Interpolation__ (zero-stuffing) inserts zeros between samples. Zero-insertion by factor $L$ places original samples at indices that are multiples of $L$ and fills gaps with zeros, spreading the sequence over a denser grid.

Unlike scaling or shifting, decimation and interpolation alter the sampling pattern itself.

Example: $x[2n]$ keeps only even-indexed samples. In zero-insertion by $2$, originals stay at even indices, odd indices become zero.

---

Flashcards for this section are as follows:

- What is decimation? ::@:: For integer $N>0$, $x[Nn]$ keeps samples at multiples of $N$.
- What is zero-insertion interpolation? ::@:: By factor $L$: original $x[n]$ maps to position $m=nL$; $L-1$ zeros inserted between samples. In frequency: $X_L(e^{j\Omega})=X(e^{jL\Omega})$, compressing the spectrum by $L$.
- Why do decimation and interpolation differ from shifting/scaling? ::@:: They change the sampling pattern itself, not just values or positions.
- What is the time-domain effect of zero-insertion by $2$? ::@:: $x=[1,2,3,4]$ becomes $x_2=[1,0,2,0,3,0,4,0]$.
- Zero-insertion vs. zero-padding? ::@:: __Zero-insertion__ (time domain): insert zeros between samples; compresses spectrum, creates images. __Zero-padding__ (before DFT): append zeros to get finer frequency grid; no new spectral info.
- Worked example: Zero-insertion by $2$ on $x[n]=\{1,3,2\}$? ::@:: $x_2[m]=\{1,0,3,0,2,0\}$. In frequency: $X_2(e^{j\Omega})=X(e^{j2\Omega})$ — two compressed copies on $[-\pi,\pi]$; a half-band LPF removes the upper image.
- Worked example: 8-point DFT via zero-padding on $x[n]=\{1,3,2\}$? ::@:: Pad to $\{1,3,2,0,0,0,0,0\}$. The 8-point DFT gives 8 samples of the DTFT at $\Omega_k=2\pi k/8$ — finer grid, no new spectral info. Rule: pad to the smallest power of 2 $\ge$ desired grid size.

## energy and power of sequences

The energy of a sequence over $-K\le n\le K$ is $E_K=\sum_{n=-K}^{K}|x[n]|^2$. Total energy is $E=\sum_{n=-\infty}^{\infty}|x[n]|^2$ when the sum converges.

Average power for an aperiodic sequence: $P=\lim_{K\to\infty}\frac{1}{2K+1}\sum_{n=-K}^{K}|x[n]|^2$. For a periodic sequence with period $N$: $P=\frac{1}{N}\sum_{n=0}^{N-1}|x[n]|^2$.

Finite-length sequences are typically energy sequences (finite total energy, zero average power). Nonzero periodic sequences are typically power sequences (finite average power, infinite total energy).

Example: nonzero values $1,2,3,4$ give energy $1^2+2^2+3^2+4^2=30$.

---

Flashcards for this section are as follows:

- What is the energy over $-K\le n\le K$? ::@:: $E_K=\sum_{n=-K}^{K}|x[n]|^2$.
- What is total energy? ::@:: $E=\sum_{n=-\infty}^{\infty}|x[n]|^2$ (when convergent).
- Average power for aperiodic sequence? ::@:: $P=\lim_{K\to\infty}\frac{1}{2K+1}\sum_{n=-K}^{K}|x[n]|^2$.
- Average power for periodic sequence (period $N$)? ::@:: $P=\frac{1}{N}\sum_{n=0}^{N-1}|x[n]|^2$.
- Energy vs. power sequences? ::@:: Finite-length → energy sequence (zero average power). Periodic → power sequence (infinite total energy).
- Worked example: nonzero samples $1,2,3,4$ — energy? ::@:: $1+4+9+16=30$.
