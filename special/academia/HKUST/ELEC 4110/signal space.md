---
aliases:
  - ELEC 4110 signal space
  - ELEC4110 signal space
  - binary modulation
tags:
  - flashcard/active/special/academia/HKUST/ELEC_4110/signal_space
  - language/in/English
---

# signal space

A {@{__signal space__}@} is {@{an abstract vector-space representation used in digital communications}@} to {@{model transmitted waveforms as points or vectors within a multidimensional Euclidean (or Hilbert) space}@}. By selecting {@{an orthonormal set of basis functions}@}—often derived via {@{Gram–Schmidt orthogonalisation}@}—{@{the time-domain signals}@} are expressed as {@{linear combinations whose coefficients serve as coordinates}@}.

{@{This geometric view}@} simplifies the analysis of {@{modulation schemes, receiver design, and error performance}@}, enabling designers to visualize {@{constellations, compute Euclidean distances between symbols}@}, and construct {@{matched filters that maximise signal-to-noise ratio}@}.

## motivation

{@{The optimality of a demodulator}@} holds {@{only within the assumed receiver structure \(e.g. matched filter for LTI filters\)}@}. {@{Altering the signal space or receiver architecture}@} can yield {@{different, potentially better performance for multilevel schemes}@}.

{@{Digital communication in general \(not limited to LTI filters\)}@} can be analysed by representing {@{transmitted waveforms}@} as {@{vectors in a multidimensional space}@}. This perspective turns {@{complex algebra into visual intuition}@} and yields {@{design rules}@} for {@{modulation, demodulation, and receiver optimisation}@}.

## geometric domain

A signal $s(t)$ can be described in {@{time domain, frequency domain, or geometric domain}@}. Actually, {@{time domain and frequency domain}@} are {@{special cases of the geometric domain}@}.

{@{A signal $s(t)$}@} is typically {@{expressed as a function of continuous time}@}, revealing {@{its waveform shape, duration, and temporal features}@} such as {@{rise/fall times or modulation patterns}@}. {@{Analysis in this domain}@} focuses on {@{causality, stability}@}, and {@{the physical realization}@} of {@{transmitters and receivers}@}. {@{Energy in the time domain}@} is obtained by {@{integrating $|s(t)|^{2}$ over the signal's support}@}.

{@{The Fourier transform $S(f)=\int_{-\infty}^{\infty}s(t)e^{-j2\pi ft}\,dt$}@} maps {@{the time waveform into a spectrum of sinusoidal components}@}. This representation exposes {@{bandwidth requirements, spectral occupancy, and filtering behavior}@}. Importantly, {@{Parseval’s theorem}@} guarantees that {@{$\int|s(t)|^{2}dt=\int|S(f)|^{2}df$ \(under the unitary convention\)}@}, so {@{total energy is preserved}@}.

In {@{signal space}@}, {@{each waveform}@} is regarded as {@{a vector in an abstract Hilbert space}@} whose {@{inner product}@} is defined by {@{$\langle u,v\rangle=\int_{0}^{T}u(t)v^{*}(t)\,dt$}@}. {@{Choosing a finite-dimensional orthonormal basis}@} turns {@{the continuous-time signal into a finite-dimensional coordinate vector}@}, enabling {@{Euclidean geometry tools—distances, angles, and projections}@}—to analyze {@{modulation constellations, design matched filters, and evaluate error probabilities}@}.

From the view of {@{geometric domain}@}, {@{the time-domain waveform}@} is simply {@{a coordinate representation using the basis $\{\,\delta(t-t_k)\,\}$}@}, while {@{the frequency domain}@} uses {@{complex exponentials $\{e^{j2\pi ft}\}$}@}; both are {@{specific orthonormal bases of the same signal Hilbert space}@}. Thus, {@{time and frequency views}@} are merely {@{different coordinate systems}@} within {@{the overarching geometric (vector-space) framework}@}.

## definition

Choose {@{a set of _orthonormal_ basis functions $\{\phi_k(t)\}$}@}. {@{Any finite-duration signal}@} can be written as {@{$$s(t)=\sum_{k=1}^N a_k\,\phi_k(t) \,.$$}@} {@{The coefficients $(a_1,\dots,a_N)$}@} are {@{the coordinates of the vector representing the waveform}@}.

### inner product

{@{The _inner product_}@} is a function {@{$$\langle\,\cdot,\cdot\,\rangle : V\times V \longrightarrow \mathbb{F}$$}@} satisfying {@{the following axioms}@} for {@{all vectors $u,v,w\in V$ and scalars $a\in\mathbb{F}$}@}: \(annotation: 3 items: {@{conjugate symmetry, linearity in the first argument, positive definiteness}@}\)

1. Conjugate symmetry: ::@:: $\langle u,v\rangle = \overline{\langle v,u\rangle}$.
2. Linearity in the first argument ::@:: $\langle u+v,w\rangle = \langle u,w\rangle + \langle v,w\rangle$, and $\langle au,v\rangle = a\,\langle u,v\rangle$.
3. Positive definiteness: ::@:: $\langle u,u\rangle \ge 0$ with equality iff $u=0$.

{@{These properties}@} guarantee that {@{the _induced norm_ $$\|v\|=\sqrt{\langle v,v\rangle}$$}@} behaves like {@{a Euclidean length}@}. {@{Two vectors}@} are {@{_orthogonal_}@} if {@{their inner product equals zero}@}; they are {@{_orthonormal_}@} when {@{each also has unit norm}@}.

{@{The inner product}@} for {@{continuous-time signals}@} is {@{$$\langle u,v\rangle = \int_{0}^{T}u(t)v^*(t)\,dt \,.$$}@} With {@{this definition}@} {@{a signal $s(t)$ has unit norm}@} when {@{its energy equals one}@}: {@{$$\|s\|^2 = \langle s,s\rangle = \int_{0}^{T}|s(t)|^{2}\,dt = 1 \,.$$}@}

### geometric concepts

- _Length_: ::@:: The magnitude of a vector is $\|v\| = \sqrt{\langle v,v\rangle}$.
- _Distance_: ::@:: Between $u$ and $v$ it is $\|u-v\|=\sqrt{\langle u-v,\,u-v\rangle}$.
- _Angle_: ::@:: The cosine of the angle between non-zero vectors $u$ and $v$ is $$\cos\theta = \frac{\langle u,v\rangle}{\|u\|\;\|v\|} \,.$$
- _Orthogonality_: ::@:: Vectors are orthogonal if their inner product vanishes: $\langle u,v\rangle=0$.
- _Circles and spheres_: ::@:: The set $\{x\in V : \|x-x_c\| = r\}$ describes a circle (or hypersphere) centered at $x_c$ with radius $r$.

{@{A sequence $(v_n)$}@} {@{converges to $v$ in an inner product space}@} iff {@{$\|v_n - v\|\to 0$}@}. Equivalently, for {@{every $\varepsilon>0$}@} there exists {@{$N$ such that $n>N\Rightarrow \|v_n-v\|<\varepsilon$}@}, ensuring {@{the familiar topological notion of limits}@} within {@{this geometric framework}@}.

### energy

{@{The signal energy}@} is {@{$$E=\langle s,s\rangle \,.$$}@} In {@{time domain}@} it is {@{$$\int|s(t)|^2 \, dt \,;$$}@} in {@{frequency domain}@} it becomes {@{$$\int |S(f)|^2 \,df \,;$$}@} in {@{geometric space with _orthonormal_ \(not just _orthogonal_\) basis}@} it equals {@{the _squared_ Euclidean norm of the coordinate vector}@}.

### coordinates

To locate {@{a transmitted waveform $s(t)$}@} within {@{its signal-space representation}@} you first select {@{an orthonormal set of basis functions $\{\phi_{k}(t)\}$}@} that spans {@{the subspace of interest (often obtained via the Gram–Schmidt process)}@}. {@{The coordinates of $s(t)$}@} are then simply {@{the projection coefficients onto these basis functions}@}: {@{$$a_k=\langle s(t),\,\phi_{k}(t)\rangle \;=\;\int_{0}^{T}s(t)\,\phi_{k}^{*}(t)\,dt \,.$$}@}

{@{The vector $(a_1,a_2,\dots ,a_N)^T$}@} is {@{the point in Euclidean space that represents the waveform}@}. {@{These coefficients}@} are {@{unique}@} because {@{the basis is orthonormal}@}, and they provide {@{a compact, geometrically meaningful description of $s(t)$}@}.

## properties

### algebraic properties

For {@{any three signals $x(t),y(t),z(t)$}@} in the space, {@{adding them in any grouping}@} yields {@{the same result}@}: {@{$$[x(t)+y(t)] + z(t)= x(t) + [y(t)+z(t)] \,.$$}@} {@{This _associative_ property}@} guarantees that {@{concatenating or regrouping signal additions}@} does not {@{affect the final waveform}@}. It is also {@{_commutative_ \(i.e. order-independent\)}@}; {@{swapping operands leaves the sum unchanged}@}: {@{$$x(t)+y(t)= y(t)+x(t) \,.$$}@}

{@{Multiplying a signal by a scalar $a$}@} and then {@{adding two scaled versions}@} is equivalent to {@{scaling the sum}@}: {@{$$a\, [x(t)+y(t)] = a\,x(t)+ a\,y(t) \,.$$}@} Thus, {@{linear combinations}@} can be {@{distributed across addition}@}. Further, if {@{$a,b$ are scalars and $x(t)$ is a signal}@}, then {@{$$(a+b)\,x(t)= a\,x(t)+ b\,x(t) \,.$$}@} This axiom ensures that {@{scalar arithmetic behaves coherently}@} when {@{applied to signals}@}.

There exists {@{an _additive identity_ \(unique "zero" signal\) $0(t)$}@} that leaves {@{any other signal unchanged when added}@}: {@{$$x(t)+0(t)= x(t) \,.$$}@} {@{The zero waveform}@} has {@{all samples equal to zero}@} and represents {@{the absence of energy in the system}@}. For {@{every signal $x(t)$}@}, there is {@{a corresponding _additive inverse_ $-x(t)$}@} such that {@{their sum equals the additive identity}@}: {@{$$x(t)+[-x(t)] = 0(t) \,.$$}@} This allows {@{subtraction of signals}@} by {@{adding their inverses}@}.

{@{Multiplying by two scalars sequentially}@} is equivalent to {@{multiplying by their product}@}: {@{$$a(b\,x(t)) = (ab)\,x(t) \,.$$}@} It reflects the fact that {@{scalar multiplication}@} respects {@{field multiplication within the vector space}@}. There also exists {@{a _multiplicative identity_ in the underlying field}@}—usually {@{$1$}@}—such that {@{scaling any signal by it leaves the signal unchanged}@}: {@{$$1\,x(t)= x(t) \,.$$}@}

Consequently, {@{the vector space's additive structure}@} behaves like {@{ordinary arithmetic on real or complex numbers}@}.

### basis

{@{An $n$-dimensional vector space $S$}@} is generated by {@{a set of $n$ basis vectors $\{e_1,e_2,\dots ,e_n\}$}@}. {@{The space}@} is {@{the span of these vectors}@}: {@{$$S=\operatorname{span}(e_1,e_2,\dots ,e_n)$$}@} {@{Any vector $a\in S$}@} can be {@{expressed uniquely as a linear combination of the basis}@}, i.e. {@{$$a=\sum_{i=1}^{n}c_i\,e_i \,.$$}@} {@{The number $n$}@} is called {@{the _dimension_ of the space}@} and equals {@{the maximum number of linearly independent vectors it contains}@}.

For {@{a particular subspace}@}, there are {@{infinitely many basis and infinitely many orthonormal basis}@}; for {@{the purpose of signal processing}@}, the choice is {@{arbitrary}@}. What matters for signal representation is {@{the subspace itself}@}, not {@{the particular basis vectors chosen}@}. One may pick {@{any convenient basis}@}, even if it {@{looks different from another}@}.

{@{_Orthonormal_ bases}@} are preferred because they {@{simplify coordinate extraction}@} and {@{preserve energy without multiplying by additionally factors}@}.

### coordinate representation

Given {@{a basis $\{e_i\}$}@}, {@{the _coordinate representation_ of a vector $a$}@} is {@{the ordered list of its expansion coefficients}@}: {@{$$[a]_E=(c_1,c_2,\dots ,c_n)^T \,.$$}@} {@{These coordinates}@} provide {@{a one-to-one correspondence}@} between {@{vectors in $S$ and points in $\mathbb{R}^n$}@}.

### orthogonality and orthonormality

{@{A set of vectors}@} is {@{_orthonormal_}@} if {@{each pair is _orthogonal_}@} ({@{$e_i^\top e_j=0$ for $i\neq j$}@}) and {@{every vector has unit norm ($\|e_i\|=1$)}@}. {@{Orthonormal bases}@} simplify {@{coordinate calculations}@} because {@{the coordinates equal inner products}@}: {@{$$c_i=\langle a,e_i\rangle \,.$$}@}

### linear transformations

{@{A mapping $h:\mathbb{R}^n\to\mathbb{R}^m$}@} is {@{_linear_}@} if it {@{preserves addition and scalar multiplication}@}: {@{$$h(\alpha a+\beta b)=\alpha h(a)+\beta h(b), \qquad \forall\,\alpha,\beta\in\mathbb{R},\;a,b\in\mathbb{R}^n \,.$$}@}

### linear independence

{@{Vectors $a_1,a_2,\dots ,a_n$}@} are {@{_linearly independent_}@} if {@{no vector}@} can be {@{expressed as a linear combination of the others}@}. Equivalently, {@{the only solution to $\sum_{i=1}^{n}\lambda_i a_i = 0$}@} is {@{$\lambda_i=0$ for all $i$}@}.

### triangle inequality

For {@{any vectors $a,b\in S$}@}, {@{$$\|a+b\|\leq \|a\|+\|b\|,$$}@} with {@{equality}@} {@{if and only if $a$ and $b$ are positively collinear}@} (one is {@{a non-negative scalar multiple of the other}@}).

### Cauchy–Schwarz inequality

{@{The inner product}@} satisfies {@{$$|\langle a,b\rangle|\leq \|a\|\,\|b\| \,,$$}@} with {@{equality precisely}@} when {@{$a$ and $b$ are linearly dependent}@}.

### Pythagorean relation

If {@{two vectors $a$ and $b$ are orthogonal}@} ({@{$\langle a,b\rangle=0$}@}), then {@{$$\|a+b\|^2=\|a\|^2+\|b\|^2 \,,$$}@} which generalises {@{the classical Pythagorean theorem to arbitrary inner product spaces}@}.

## Gram–Schmidt process

Given {@{any linearly independent set of signals $\{s_1,\dots,s_M\}$}@}, {@{the _Gram–Schmidt process_}@} constructs {@{an _orthonormal_ basis $\{\phi_1,\dots,\phi_P\}$}@} for {@{the subspace they span}@}. {@{The first basis vector}@} is a {@{normalised copy of $s_1$}@}. {@{Subsequent vectors are obtained}@} by {@{subtracting from each new signal}@} its {@{projections onto previously found basis vectors}@} and then {@{normalising}@}.

The algorithm is: \(annotation: 3 items: {@{first basis vector → remaining basis vectors → skip conditions}@}\)

1. first basis vector ::@:: Set $\phi_1 = s_1/\|s_1\|$.
2. remaining basis vectors ::@:: For $k=2$ to $M$: compute the projection of $s_k$ onto the span of $\{\phi_1,\dots,\phi_{k-1}\}$; subtract this projection from $s_k$ and normalise the remainder to get $\phi_k$.
3. skip conditions ::@:: If a residual becomes zero, skip to the next signal; the dimension of the signal space is less than $M$.

\(__this course__: Whenever possible, {@{identify orthogonal signals}@} {@{by inspection}@} and {@{normalize them}@}, which is {@{usually much faster}@}. Only if {@{the problem is complex or explicitly asks for a Gram–Schmidt process}@}, then {@{use the Gram–Schmidt process}@}.\)

## examples

{@{Three unit-amplitude pulses}@} occupying {@{consecutive thirds of an interval}@} are {@{_orthogonal_}@} as each pulse {@{occupies a distinct subinterval}@}. {@{Their coordinates}@} are simply {@{$(1,0,0)$, $(0,1,0)$, and $(0, 0, 1)$}@}, and {@{the basis functions}@} are {@{the three unit-amplitude pulses, but _normalized_}@}.

### sinusoidal examples

{@{Two signals $$s_1(t)=A\cos(2\pi f_ct)$$ and $$s_2(t)=A\sin(2\pi f_ct)$$}@} over {@{$[0,T)$ where $f_c$ is a _multiple_ of $1 / T$}@}, are {@{orthogonal}@} because {@{their inner product integrates to zero}@}. {@{The resulting basis}@} is {@{two-dimensional}@}, matching {@{the number of signals}@}. {@{The basis functions}@} are {@{the same but _normalized_}@}.

Extending {@{the previous two signals $$s_1(t)=A\cos(2\pi f_ct)$$ and $$s_2(t)=A\sin(2\pi f_ct)$$}@} over {@{$[0,T)$ where $f_c$ is a _multiple_ of $1 / T$}@}, consider {@{$$s_m'(t) = A\cos\left(2\pi f_ct + \frac {2 \pi (m - 1)} {M} \right)$$}@} where {@{$M \ge 3$ is the number of signals and $f_c$ has the same restriction as above}@}. Using {@{trigonometric identities}@} we can always {@{express $s_m'(t)$ as a sum of $s_1(t)$ and $s_2(t)$}@}: {@{$$s_m'(t) = A\cos\left(\frac {2 \pi (m - 1)} {M} \right) \cos(2\pi f_c t) - A \sin\left(\frac {2 \pi (m - 1)} M \right) \sin(2\pi f_c t) \,.$$}@} Hence, {@{the resulting basis}@} is {@{the same as the previous case}@}.

These examples show that {@{sinusoidal signals over a fixed interval $[0, T)$}@} can always be {@{represented by a linear combination of two signals only}@}. This fact is used in {@{_M_-PSK \(including QPSK\) and _M_-QAM}@}, so {@{their constellation diagrams}@} are {@{two-dimensional}@}. {@{The amplitude of the basis $\cos (2\pi f_c t)$}@} is called {@{the _inphase_ signal $I(t)$}@}, while {@{the amplitude of the basis $-\sin(2\pi f_c t)$ \(note the _negative_ sign\)}@} is called {@{the _quadrature_ signal $Q(t)$}@}. They may be represented as {@{a complex number $Z(t) = I(t) + j Q(t)$}@} or plotted {@{on an constellation plane as $(I(t), Q(t))$}@}.

## applications

### receiver optimization

For {@{linear time invariant \(LTI\) filters}@}, {@{the matched filter}@} {@{maximises signal-to-noise ratio}@}. In {@{signal space}@} this is equivalent to {@{projecting the received vector onto each basis function}@} and deciding on {@{the symbol whose projected coordinates}@} are {@{closest in Euclidean distance}@}.

{@{Increasing bit rate}@} by {@{adding dimensions}@} usually requires {@{higher bandwidth or power}@}. {@{The geometric view}@} helps visualise {@{these trade-offs}@} and guides {@{practical modulation choices}@} such as {@{quadrature amplitude modulation \(QAM\), phase-shift keying \(PSK\), orthogonal frequency-division multiplexing \(OFDM\), etc.}@}

For example, {@{frequency-domain representation}@} as {@{a special case of geometric-domain representation}@}, can {@{represent discrete signals of length _N_ _perfectly_}@}, but {@{the resulting dimension}@} also {@{has _N_ dimensions}@}, which is {@{_inefficient_}@} as it {@{does not exploit any _simplicity_ in the signals to be transmitted}@}. It may be possible that {@{the signals to be transmitted}@} lie in {@{a subspace that has less than _N_ dimensions}@}. The goal of {@{a geometric-domain representation}@} is to find {@{the _minimal_ dimensions}@} that still {@{contains all signals to be transmitted}@}.

### M-ary modulation

By assigning {@{distinct vectors in signal space to each symbol}@}, {@{more than one bit per symbol}@} can be {@{transmitted}@}. {@{The dimensionality of the space}@} dictates {@{how many _orthogonal_ symbols can coexist}@}; {@{higher dimensions}@} enable {@{denser constellations}@}.

### constellation diagram

Plotting {@{the coordinate vectors}@} of {@{all allowed signals on a Euclidean plane (or higher-dimensional hyperplane)}@} gives {@{the _constellation diagram_}@}. {@{Distances between points}@} determine {@{error probability, typically under some assumptions}@}, such as {@{additive white Gaussian noise}@}.
