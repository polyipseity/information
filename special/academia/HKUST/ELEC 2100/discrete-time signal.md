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

Discrete-time signals are signals indexed by integers rather than by a continuous independent variable. In ELEC 2100 they arise both as sampled versions of continuous-time signals and as native sequences in their own right, so the course treats their representation methods, common signal families, and periodicity rules as a durable toolkit rather than as one-off examples.

---

Flashcards for this section are as follows:

- What is a discrete-time signal? ::@:: It is a signal indexed by integers, so it is written as a sequence such as $x[n]$ rather than as a continuous-time function $x(t)$.
- Why are discrete-time signals important in ELEC 2100? ::@:: They arise both from sampling continuous-time signals and from native sequence models, so they need their own representation methods, common signal families, and periodicity rules.

## representation methods

A discrete-time signal can be represented in several equivalent ways. One may list its values as a sequence, one may write an explicit formula for $x[n]$, and one may draw a waveform or stem plot in which the horizontal axis is the integer index $n$ and the length of each vertical line segment represents the magnitude of the corresponding sample value. The upward arrow in sequence notation marks the sample at $n=0$.

If the samples come from uniform sampling of a continuous-time signal $x_s(t)$ at interval $T_s$, then the sequence is written as $x[n]=x_s(nT_s)$. This is why discrete-time sequences are often described as evenly spaced samples of a continuous-time waveform. The independent variable has changed from physical time $t$ to the integer sample index $n$.

The lecture's example $x[n]=2^n$ for $n\ge 0$ and $x[n]=0$ for $n<0$ shows how sequence form, formula form, and waveform form fit together. In list form one writes $\{\ldots,0,0,0,1,2,4,8,\ldots\}$ with the arrow under the value at $n=0$. In formula form one writes the piecewise definition. In waveform form one draws one stem at each integer $n$, with heights $1,2,4,8,\ldots$ for $n=0,1,2,3,\ldots$ and zero stems for negative indices.

---

Flashcards for this section are as follows:

- What are the main representation methods for a discrete-time signal? ::@:: A discrete-time signal may be represented by its sequence values, by an explicit formula for $x[n]$, or by a waveform/stem plot indexed by $n$.
- In a discrete-time waveform, what does the length of each line segment represent? ::@:: It represents the magnitude of the corresponding sequence value.
- What does the upward arrow mean in sequence notation? ::@:: It marks the sample at $n=0$.
- How is a uniformly sampled continuous-time signal represented as a discrete-time sequence? ::@:: If the sampling interval is $T_s$, then the sequence is $x[n]=x_s(nT_s)$.
- Why is $n$ the independent variable in a discrete-time sequence? ::@:: Because the signal is described sample by sample at integer indices rather than at every continuous-time instant.
- Worked example: If $x[n]=2^n$ for $n\ge 0$ and $x[n]=0$ for $n<0$, how does its sequence begin around the origin? ::@:: It is $\{\ldots,0,0,0,1,2,4,8,\ldots\}$ with the arrow under the value $1$ at $n=0$.
- Worked example: How should the waveform of $x[n]=2^n u[n]$ be drawn? ::@:: Draw stems at integer indices, with zero height for negative $n$ and heights $1,2,4,8,\ldots$ for $n=0,1,2,3,\ldots$.

## support patterns

The lecture classifies sequences by how far their nonzero samples extend. A one-sided sequence is nonzero only on one side of the index axis, most commonly for $n\ge 0$. A two-sided sequence may have nonzero values for both negative and positive indices. A finite-length sequence is nonzero only over a bounded set of consecutive or isolated indices.

These support patterns matter because they help one read formulas quickly. A factor such as $u[n]$ usually signals a one-sided sequence. A sequence described only by finitely many shifted impulses is finite-length. A sequence like $a^n$ without a one-sided gate is naturally two-sided if one allows all integer $n$.

---

Flashcards for this section are as follows:

- What is a one-sided sequence? ::@:: It is a sequence whose nonzero samples lie only on one side of the index axis, typically for $n\ge 0$.
- What is a two-sided sequence? ::@:: It is a sequence that may have nonzero samples for both negative and positive indices.
- What is a finite-length sequence? ::@:: It is a sequence that is nonzero only over a bounded set of indices.
- Why do support patterns matter? ::@:: They help you read quickly whether a sequence extends indefinitely, starts at one side, or is confined to a finite window.
- What does a factor such as $u[n]$ usually signal about a sequence? ::@:: It usually signals that the sequence is one-sided and starts at or after $n=0$.

## unit sample sequence

The unit sample sequence, also called the discrete-time impulse or Kronecker delta, is defined by $\delta[n]=1$ for $n=0$ and $\delta[n]=0$ for $n\neq 0$. Unlike the continuous-time impulse, this is an ordinary sequence, not a generalized function. Its graph is a single stem of height $1$ at the origin.

Time shifting gives $\delta[n-j]$, which places the unit sample at index $n=j$. Scaling gives $c\,\delta[n-j]$, which changes the sample value at that one index from $1$ to $c$. The discrete-time sampling property is $f[n]\delta[n]=f[0]\delta[n]$: once multiplication by the unit sample has killed all other indices, only the value at the origin remains.

The unit sample is the basic building block for arbitrary sequences. Any sequence can be written as $x[n]=\sum_{m=-\infty}^{\infty}x[m]\delta[n-m]$. This is the discrete-time analogue of building a signal from weighted shifted impulses, but here everything remains within ordinary sequence algebra.

For example, the sequence with values $x[-1]=-1.5$, $x[1]=1$, and $x[3]=3$ and zeros elsewhere can be written as $x[n]=-1.5\delta[n+1]+\delta[n-1]+3\delta[n-3]$. The weights tell you the sample values, and the shifts tell you the positions.

---

Flashcards for this section are as follows:

- What is the unit sample sequence? ::@:: It is the discrete-time impulse $\delta[n]$, equal to $1$ at $n=0$ and $0$ for all other indices.
- Why is the discrete-time impulse different from the continuous-time impulse? ::@:: The discrete-time impulse is an ordinary sequence, whereas the continuous-time impulse is a generalized function.
- What does $\delta[n-j]$ represent? ::@:: It is a shifted unit sample located at index $n=j$.
- What does $c\,\delta[n-j]$ represent? ::@:: It is a shifted unit sample at index $n=j$ with value $c$ instead of $1$.
- What is the sampling property of the discrete-time impulse at the origin? ::@:: It is $f[n]\delta[n]=f[0]\delta[n]$.
- How can an arbitrary discrete-time sequence be represented using shifted unit samples? ::@:: It can be written as $x[n]=\sum_{m=-\infty}^{\infty}x[m]\delta[n-m]$.
- Worked example: How is the sequence with $x[-1]=-1.5$, $x[1]=1$, and $x[3]=3$ represented using shifted unit samples? ::@:: It is $x[n]=-1.5\delta[n+1]+\delta[n-1]+3\delta[n-3]$.
- Why is the unit sample called the basic building block of arbitrary sequences? ::@:: Because weighted shifted unit samples can reconstruct every sample value at its correct index.

## unit step and rectangular sequence

The discrete-time unit step is $u[n]=1$ for $n\ge 0$ and $u[n]=0$ for $n<0$. It is the discrete-time analogue of switching on a sequence at the origin. Because it stays equal to $1$ for all nonnegative indices, it can be expressed as an infinite sum of shifted unit samples: $u[n]=\sum_{k=0}^{\infty}\delta[n-k]$.

The unit step and unit sample are closely related. Their difference satisfies $\delta[n]=u[n]-u[n-1]$. This is the discrete-time version of the idea that a jump can be isolated by taking a difference.

A rectangular sequence or rectangular window of length $N$ is defined by $R_N[n]=1$ for $0\le n\le N-1$ and $R_N[n]=0$ otherwise. The endpoint convention matters: the left endpoint $n=0$ is included, while the first excluded index is $n=N$. Equivalently, the support is exactly the set $\{0,1,\ldots,N-1\}$. It can be written in step form as $R_N[n]=u[n]-u[n-N]$, and it can also be written as a finite sum of shifted unit samples: $R_N[n]=\sum_{k=0}^{N-1}\delta[n-k]$.

These formulas show three useful viewpoints at once: the step view emphasizes switching on and off, the impulse-sum view emphasizes finite support, and the graph view emphasizes that the sequence is a flat run of ones over a fixed index interval.

---

Flashcards for this section are as follows:

- What is the discrete-time unit step sequence? ::@:: It is $u[n]=1$ for $n\ge 0$ and $u[n]=0$ for $n<0$.
- How can the discrete-time unit step be written as a sum of unit samples? ::@:: It can be written as $u[n]=\sum_{k=0}^{\infty}\delta[n-k]$.
- What is the relation between the unit sample and the unit step in discrete time? ::@:: They satisfy $\delta[n]=u[n]-u[n-1]$.
- What is a rectangular sequence of length $N$, including its endpoint convention? ::@:: It is $R_N[n]=1$ for $0\le n\le N-1$ and $0$ otherwise, so $n=0$ is included and $n=N$ is excluded.
- How can the rectangular sequence be written using unit steps? ::@:: It can be written as $R_N[n]=u[n]-u[n-N]$.
- How can the rectangular sequence be written using unit samples? ::@:: It can be written as $R_N[n]=\sum_{k=0}^{N-1}\delta[n-k]$.
- Why is the endpoint convention of $R_N[n]=u[n]-u[n-N]$ easy to misread? ::@:: Because the step form shows switch-on at $n=0$ and switch-off starting at $n=N$, so the support includes $0$ through $N-1$ but excludes $N$.
- What three viewpoints are useful for understanding the rectangular sequence? ::@:: The step view emphasizes switching on and off, the impulse-sum view emphasizes finite support, and the graph view emphasizes a flat run of ones over a fixed index interval.

## ramp and one-sided exponential sequences

The discrete-time ramp sequence is $x[n]=nu[n]$. It is zero for negative indices and then grows linearly with slope $1$ sample by sample for $n\ge 0$. It is the direct discrete-time analogue of a one-sided ramp, with the important difference that only integer sample values are present.

A one-sided exponential sequence has the form $x[n]=a^n u[n]$. Its behavior depends strongly on the value of $a$. If $0<a<1$, the sequence is positive and decays toward zero. If $a>1$, it grows without bound. If $-1<a<0$, the samples alternate sign while their magnitude decays. If $a<-1$, the samples alternate sign while their magnitude grows.

This comparison is worth making explicitly because students often focus only on the magnitude behavior and forget the sign alternation caused by a negative base. A negative value of $a$ does not merely "flip the graph once"; it flips the sign at every successive sample.

---

Flashcards for this section are as follows:

- What is the discrete-time ramp sequence? ::@:: It is $x[n]=nu[n]$, so it is zero for negative indices and then grows linearly with index for $n\ge 0$.
- How does the discrete-time ramp differ visually from the continuous-time ramp? ::@:: It has values only at integer indices, so it appears as stems rather than a continuous line.
- What is a one-sided exponential sequence? ::@:: It is a sequence of the form $x[n]=a^n u[n]$.
- How does $x[n]=a^n u[n]$ behave when $0<a<1$? ::@:: It stays positive and decays toward zero.
- How does $x[n]=a^n u[n]$ behave when $a>1$? ::@:: It stays positive and grows without bound.
- How does $x[n]=a^n u[n]$ behave when $-1<a<0$? ::@:: It alternates sign while its magnitude decays toward zero.
- How does $x[n]=a^n u[n]$ behave when $a<-1$? ::@:: It alternates sign while its magnitude grows.
- Why is the sign of $a$ important in a one-sided exponential sequence? ::@:: A negative base causes the sample sign to flip at every index, not just once.

## sinusoidal and complex exponential sequences

A discrete-time sinusoidal sequence is written as $x[n]=\sin(\omega n)$ or more generally $x[n]=A\sin(\omega n+\phi)$. Here the discrete-time angular frequency is written with lowercase $\omega$ and is measured in radians per sample. If the sequence comes from sampling a continuous-time sinusoid $x(t)=A\sin(\omega_0 t+\phi)$ with sampling interval $T_s$, then $x[n]=A\sin(\omega_0 T_s n+\phi)=A\sin(\omega n+\phi)$, where $\omega=\omega_0 T_s=2\pi f_0/f_s$.

The periodicity rule for discrete-time sinusoids is stricter than in continuous time. A sinusoidal sequence is periodic only if there exists a positive integer $N$ such that $x[n+N]=x[n]$ for all $n$. This requires $\omega N=2\pi m$ for some integer $m$, equivalently $\omega/(2\pi)$ must be rational. The rational-versus-irrational split is the real deciding factor. If $\omega/(2\pi)$ is rational, then some positive integer period exists. If $\omega/(2\pi)$ is irrational, then no positive integer $N$ can ever make the samples line up exactly again, so the sequence is aperiodic even if the plotted stems may look oscillatory.

The lecture's examples illustrate the three main cases. If $x[n]=\sin(0.2\pi n)$, then $\omega=0.2\pi$ and $N=10$ works, so the sequence has period $10$ and completes one full cycle every $10$ samples. If $x[n]=\sin((4\pi/11)n)$, then one may take $m=2$ and $N=11$, so the sequence has period $11$ and completes two full cycles in that period. If $x[n]=\sin(0.4n)$, then $0.4/(2\pi)$ is irrational, so the sequence is aperiodic. The crucial lesson is that irrationality destroys exact sample-by-sample repetition, not just the existence of a simple-looking period.

The complex exponential sequence is $x[n]=e^{j\omega n}=\cos(\omega n)+j\sin(\omega n)$. In polar form its magnitude is $|x[n]|=1$, and its phase is $\arg x[n]=\omega n$. Its periodicity obeys exactly the same rationality rule as the real sinusoid: it is periodic if and only if $\omega/(2\pi)$ is rational. If that ratio is irrational, then the phasor never returns to exactly the same complex value after an integer number of samples, so the sequence is aperiodic.

The comparison between the real sinusoid and the complex exponential is important. The sinusoid gives one real oscillatory coordinate, while the complex exponential packages cosine and sine together into one rotating complex sequence. This is why complex exponentials become the algebraically convenient building blocks in later Fourier analysis. It also explains why irrationality has the same effect in both settings: if the sampled rotation angle is incommensurate with $2\pi$, neither the real projection nor the full complex phasor can repeat exactly after a finite integer shift.

---

Flashcards for this section are as follows:

- What is a discrete-time sinusoidal sequence? ::@:: It is a sequence such as $x[n]=\sin(\omega n)$ or more generally $x[n]=A\sin(\omega n+\phi)$.
- How does sampling a continuous-time sinusoid produce a discrete-time sinusoid? ::@:: Sampling $x(t)=A\sin(\omega_0 t+\phi)$ at interval $T_s$ gives $x[n]=A\sin(\omega_0 T_s n+\phi)=A\sin(\omega n+\phi)$.
- What is the digital angular frequency $\omega$? ::@:: It is the discrete-time angular frequency in radians per sample, with $\omega=\omega_0 T_s=2\pi f_0/f_s$ for a sampled sinusoid.
- When is a discrete-time sinusoidal sequence periodic? ::@:: It is periodic only if there exists a positive integer $N$ such that $\omega N=2\pi m$ for some integer $m$, equivalently if $\omega/(2\pi)$ is rational.
- Why can a discrete-time sinusoid be aperiodic even though a continuous-time sinusoid is always periodic? ::@:: Because discrete time requires an integer period in samples, so periodicity depends on whether $\omega/(2\pi)$ is rational or irrational.
- What is the effect of irrationality on the periodicity of a discrete-time sinusoid? ::@:: If $\omega/(2\pi)$ is irrational, then no positive integer sample shift can make the sequence repeat exactly, so the sequence is aperiodic.
- Worked example: Given $x[n]=\sin(0.2\pi n)$, what is its period? ::@:: Its period is $10$ because $0.2\pi\cdot 10=2\pi$.
- Worked example: Given $x[n]=\sin((4\pi/11)n)$, what is its period and how many cycles occur in that period? ::@:: Its period is $11$, and the sequence completes two full cycles in that period.
- Worked example: Why is $x[n]=\sin(0.4n)$ aperiodic? ::@:: Because $0.4/(2\pi)$ is irrational, so no positive integer $N$ can satisfy $0.4N=2\pi m$.
- What is the discrete-time complex exponential sequence? ::@:: It is $x[n]=e^{j\omega n}=\cos(\omega n)+j\sin(\omega n)$.
- What are the magnitude and phase of $e^{j\omega n}$? ::@:: Its magnitude is $1$, and its phase is $\omega n$.
- When is a discrete-time complex exponential sequence periodic? ::@:: It is periodic if and only if $\omega/(2\pi)$ is rational.
- What is the effect of irrationality on the periodicity of $e^{j\omega n}$? ::@:: If $\omega/(2\pi)$ is irrational, the phasor never returns exactly to the same complex value after any positive integer number of samples, so the sequence is aperiodic.

## pointwise operations and index transformations

The simplest operations on discrete-time signals are pointwise operations. If two sequences are defined on the same index axis, then summation forms $z[n]=x[n]+y[n]$, multiplication forms $z[n]=x[n]y[n]$, and scaling by a constant forms $z[n]=ax[n]$. These operations are applied sample by sample at the same index. In practice this means that one must align the sample indices first before combining values.

The distinction between pointwise operations and index transformations is important. In $z[n]=2x[n]$, the factor $2$ changes the sample values but does not move any sample positions. By contrast, in $z[n]=x[n-m]$ or $z[n]=x[n+m]$, the sequence values are preserved but their positions on the index axis are moved.

Shifting follows the same right-versus-left rule as in continuous time, but now the shift amount is an integer number of samples. For $m>0$, $x[n-m]$ is a right shift by $m$ samples and $x[n+m]$ is a left shift by $m$ samples. Time reversal gives $z[n]=x[-n]$, which reflects the sequence about the origin of the index axis.

It is worth comparing shifting and reversal carefully. Shifting changes the location of every sample without changing their order, while reversal flips the order around the origin. In discrete time this can be checked directly by following where the sample originally at index $n_0$ ends up: under reversal it appears at $-n_0$, whereas under a right shift by $m$ it appears at $n_0+m$.

As a simple arithmetic example, if $x[n]=\{1,2,3,4\}$ and $y[n]=\{1,1,1,0\}$, then $x[n]+y[n]=\{2,3,4,4\}$ and $x[n]y[n]=\{1,2,3,0\}$. The same example also shows scaling: $2x[n]=\{2,4,6,8\}$.

---

Flashcards for this section are as follows:

- What is pointwise summation of two sequences? ::@:: It forms $z[n]=x[n]+y[n]$ by adding samples at the same index.
- What is pointwise multiplication of two sequences? ::@:: It forms $z[n]=x[n]y[n]$ by multiplying samples at the same index.
- What is scaling of a discrete-time sequence? ::@:: It forms $z[n]=ax[n]$, multiplying every sample value by the same constant $a$.
- Why must indices be aligned before adding or multiplying sequences? ::@:: Because pointwise operations combine values at the same index rather than values that merely appear next to each other in a list.
- What is the difference between scaling and shifting? ::@:: Scaling changes sample values without moving their positions, whereas shifting moves sample positions without changing the underlying sample values.
- For $m>0$, what do $x[n-m]$ and $x[n+m]$ do? ::@:: $x[n-m]$ shifts the sequence right by $m$ samples, whereas $x[n+m]$ shifts it left by $m$ samples.
- What does time reversal do to a discrete-time sequence? ::@:: It forms $z[n]=x[-n]$, reflecting the sequence about the index origin.
- What is the difference between shifting and reversal? ::@:: Shifting moves every sample without changing their order, whereas reversal flips the order around the origin.
- Worked example: If $x[n]=\{1,2,3,4\}$ and $y[n]=\{1,1,1,0\}$, what are $x[n]+y[n]$ and $x[n]y[n]$? ::@:: They are $\{2,3,4,4\}$ and $\{1,2,3,0\}$ respectively.
- Worked example: If $x[n]=\{1,2,3,4\}$, what is $2x[n]$? ::@:: It is $\{2,4,6,8\}$.

## difference and running sum

Discrete differentiation is expressed by differences. The forward difference is $\Delta x[n]=x[n+1]-x[n]$, and the backward difference is $\nabla x[n]=x[n]-x[n-1]$. Both measure sample-to-sample change, but they anchor that change at slightly different indices.

The distinction is important. The forward difference compares the current sample with the next one, so it is naturally associated with a look-ahead viewpoint. The backward difference compares the current sample with the previous one, so it is the more common causal-looking difference formula when one wants to work from past to present.

The running sum is the discrete-time analogue of integration. It is defined by $y[n]=\sum_{k=-\infty}^{n}x[k]$, so each new value of $y[n]$ accumulates all samples of $x[k]$ up to the current index. This makes the running sum a cumulative-memory operation rather than a pointwise one.

For example, if $x[n]=0$ for $n<0$ and $x[0]=1$, $x[1]=2$, $x[2]=3$, $x[3]=4$, then the running sum is $y[0]=1$, $y[1]=3$, $y[2]=6$, and $y[3]=10$, after which it stays at $10$ if later samples are zero. The sequence of partial sums makes the accumulation interpretation very concrete.

---

Flashcards for this section are as follows:

- What is the forward difference of a sequence? ::@:: It is $\Delta x[n]=x[n+1]-x[n]$.
- What is the backward difference of a sequence? ::@:: It is $\nabla x[n]=x[n]-x[n-1]$.
- What is the difference between forward and backward difference? ::@:: Forward difference compares the current sample with the next one, whereas backward difference compares the current sample with the previous one.
- What is the running sum of a discrete-time sequence? ::@:: It is $y[n]=\sum_{k=-\infty}^{n}x[k]$, the cumulative sum of all samples up to index $n$.
- Why is the running sum not a pointwise operation? ::@:: Because each output value depends on many past samples rather than only on the sample at the same index.
- Worked example: If $x[0]=1$, $x[1]=2$, $x[2]=3$, and $x[3]=4$ with earlier samples zero, what are the first four running-sum values? ::@:: They are $y[0]=1$, $y[1]=3$, $y[2]=6$, and $y[3]=10$.

## decimation and interpolation

Reshaping operations change the sampling density of a sequence. Decimation keeps fewer samples. For a positive integer $N$, the sequence $x[Nn]$ keeps every sample whose original index is a multiple of $N$. This compresses the sequence along the index axis in the sense that the retained samples are described by a shorter index progression.

Interpolation, in the elementary zero-stuffing sense used in the lecture, inserts additional index locations between existing samples. A standard idealized description is to place the original sample values at indices that are multiples of $N$ and fill the newly created intermediate indices with zeros. The resulting sequence has the same original values, but spread out over a denser index grid.

The lecture warns that one may have to remove points or insert zeros depending on the reshaping task. This makes decimation and interpolation conceptually different from simple scaling or shifting: they alter the sampling pattern itself rather than just the values or positions of existing samples.

For example, if one forms $x[2n]$, the result keeps only the even-indexed samples of the original sequence. In zero-insertion interpolation by a factor of $2$, the original samples remain at even indices of the new sequence, while odd indices are filled with zeros.

---

Flashcards for this section are as follows:

- What is decimation of a discrete-time sequence? ::@:: For a positive integer $N$, decimation keeps the samples whose original indices are multiples of $N$, producing the sequence $x[Nn]$.
- What does decimation by a factor of $2$ do? ::@:: It keeps only the even-indexed samples of the original sequence.
- What is interpolation in the zero-insertion sense? ::@:: It places the original sample values at indices that are multiples of the interpolation factor and fills the new intermediate indices with zeros.
- Why are decimation and interpolation different from ordinary shifting or scaling? ::@:: They alter the sampling pattern itself rather than merely changing sample values or moving already existing sample positions.
- In zero-insertion interpolation by factor $2$, where do the original samples go? ::@:: They stay at the even indices of the new sequence, while the odd indices are filled with zeros.

## energy and power of sequences

The energy of a discrete-time sequence over a finite symmetric interval $-K\le n\le K$ is $E_K=\sum_{n=-K}^{K}|x[n]|^2$. The total energy is $E=\sum_{n=-\infty}^{\infty}|x[n]|^2$ when this infinite sum converges. As in continuous time, energy measures total accumulated squared magnitude.

Average power is the long-run average squared magnitude. For an aperiodic sequence it is defined by $P=\lim_{K\to\infty}\frac{1}{2K+1}\sum_{n=-K}^{K}|x[n]|^2$. For a periodic sequence with period $N$, one may average over one full period: $P=\frac{1}{N}\sum_{n=0}^{N-1}|x[n]|^2$.

The same energy-versus-power distinction from continuous time appears again here. A finite-length sequence is typically an energy sequence because the total squared magnitude is finite and the long-run average power is zero. A nonzero periodic sequence is typically a power sequence because its average over one period is finite but its total energy diverges when repeated forever.

The lecture's sample energy calculation uses a sequence with nonzero values $1,2,3,4$. Its energy is $1^2+2^2+3^2+4^2=30$. This example is simple, but it makes the sum-of-squares viewpoint explicit.

---

Flashcards for this section are as follows:

- What is the energy of a discrete-time sequence over the finite interval $-K\le n\le K$? ::@:: It is $E_K=\sum_{n=-K}^{K}|x[n]|^2$.
- What is the total energy of a discrete-time sequence? ::@:: It is $E=\sum_{n=-\infty}^{\infty}|x[n]|^2$ when the infinite sum converges.
- What is the average power of an aperiodic discrete-time sequence? ::@:: It is $P=\lim_{K\to\infty}\frac{1}{2K+1}\sum_{n=-K}^{K}|x[n]|^2$.
- What is the average power of a periodic sequence with period $N$? ::@:: It is $P=\frac{1}{N}\sum_{n=0}^{N-1}|x[n]|^2$.
- How do energy sequences and power sequences differ in discrete time? ::@:: A finite-length sequence is typically an energy sequence with zero average power, whereas a nonzero periodic sequence is typically a power sequence with infinite total energy.
- Worked example: If the nonzero samples of a sequence are $1,2,3,4$, what is its energy? ::@:: Its energy is $1^2+2^2+3^2+4^2=30$.
