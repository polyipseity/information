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

{@{A __signal space__}@} is {@{an abstract vector-space representation used in digital communications}@} to model {@{transmitted waveforms as points within a multidimensional Euclidean (or Hilbert) space}@}. Using {@{an orthonormal set of basis functions}@} (often derived via {@{Gram–Schmidt orthogonalisation}@}), {@{time-domain signals}@} become {@{linear combinations whose coefficients are the coordinates}@}.

{@{This geometric view}@} simplifies analysis of {@{modulation schemes, receiver design, and error performance}@}: visualize {@{constellations, compute Euclidean distances between symbols}@}, and build {@{matched filters that maximise SNR}@}.

## motivation

{@{The optimality of a demodulator}@} holds {@{only within the assumed receiver structure \(e.g. matched filter for LTI filters\)}@}. Changing {@{the signal space or receiver architecture}@} can yield {@{different performance for multilevel schemes}@}.

{@{Digital communication in general}@} can be analysed by representing {@{transmitted waveforms}@} as {@{vectors in a multidimensional space}@}, turning {@{complex algebra into visual intuition}@} and guiding {@{modulation, demodulation, and receiver optimisation}@}.

## geometric domain

{@{A signal $s(t)$}@} can be described in {@{time domain, frequency domain, or geometric domain}@}; the first two are {@{special cases of the geometric domain}@}.

{@{Time domain}@}: {@{A signal $s(t)$}@} is {@{a function of continuous time}@} showing {@{waveform shape, duration, and temporal features}@}. {@{Energy}@} is {@{$\int|s(t)|^{2}$ over the signal's support}@}.

{@{Frequency domain}@}: {@{The Fourier transform $S(f)=\int_{-\infty}^{\infty}s(t)e^{-j2\pi ft}\,dt$}@} maps {@{the waveform into sinusoidal components}@}, revealing {@{bandwidth and spectral occupancy}@}. {@{Parseval's theorem}@} gives {@{$\int|s(t)|^{2}dt=\int|S(f)|^{2}df$}@}, so {@{energy is preserved}@}.

{@{Geometric domain}@}: {@{Each waveform}@} is {@{a vector in an abstract Hilbert space}@} with {@{inner product}@} {@{$\langle u,v\rangle=\int_{0}^{T}u(t)v^{*}(t)\,dt$}@}. {@{Choosing a finite-dimensional orthonormal basis}@} converts {@{the signal into a coordinate vector}@}, letting {@{Euclidean geometry tools}@} analyze {@{constellations, design matched filters, and evaluate error probabilities}@}.

{@{The time-domain waveform}@} uses {@{basis $\{\,\delta(t-t_k)\,\}$}@}, {@{the frequency domain}@} uses {@{complex exponentials $\{e^{j2\pi ft}\}$}@}; both are {@{orthonormal bases of the same Hilbert space}@} — merely {@{different coordinate systems}@} within {@{the same geometric framework}@}.

## definition

Choose {@{a set of _orthonormal_ basis functions $\{\phi_k(t)\}$}@}. {@{Any finite-duration signal}@} can be written as {@{$$s(t)=\sum_{k=1}^N a_k\,\phi_k(t) \,.$$}@} {@{The coefficients $(a_1,\dots,a_N)$}@} are {@{the coordinates of the vector representing the waveform}@}.

### inner product

{@{The _inner product_}@} is {@{a function $$\langle\,\cdot,\cdot\,\rangle : V\times V \longrightarrow \mathbb{F}$$}@} satisfying {@{these axioms}@} for {@{all vectors $u,v,w\in V$ and scalars $a\in\mathbb{F}$}@}: \(annotation: 3 items: {@{conjugate symmetry, linearity in the first argument, positive definiteness}@}\)

1. Conjugate symmetry: ::@:: $\langle u,v\rangle = \overline{\langle v,u\rangle}$.
2. Linearity in the first argument ::@:: $\langle u+v,w\rangle = \langle u,w\rangle + \langle v,w\rangle$, and $\langle au,v\rangle = a\,\langle u,v\rangle$.
3. Positive definiteness: ::@:: $\langle u,u\rangle \ge 0$ with equality iff $u=0$.

These imply {@{the _induced norm_ $$\|v\|=\sqrt{\langle v,v\rangle}$$ (Euclidean length)}@}. {@{Two vectors}@} are {@{_orthogonal_}@} if {@{$\langle u,v\rangle=0$}@}; {@{_orthonormal_}@} when {@{also unit norm}@}.

For {@{continuous-time signals}@}: {@{$$\langle u,v\rangle = \int_{0}^{T}u(t)v^*(t)\,dt \,.$$}@} {@{A signal $s(t)$ has unit norm}@} when {@{energy equals one}@}: {@{$$\|s\|^2 = \langle s,s\rangle = \int_{0}^{T}|s(t)|^{2}\,dt = 1 \,.$$}@}

### geometric concepts

- _Length_: ::@:: The magnitude of a vector is $\|v\| = \sqrt{\langle v,v\rangle}$.
- _Distance_: ::@:: Between $u$ and $v$ it is $\|u-v\|=\sqrt{\langle u-v,\,u-v\rangle}$.
- _Angle_: ::@:: The cosine of the angle between non-zero vectors $u$ and $v$ is $$\cos\theta = \frac{\langle u,v\rangle}{\|u\|\;\|v\|} \,.$$
- _Orthogonality_: ::@:: Vectors are orthogonal if their inner product vanishes: $\langle u,v\rangle=0$.
- _Circles and spheres_: ::@:: The set $\{x\in V : \|x-x_c\| = r\}$ describes a circle (or hypersphere) centered at $x_c$ with radius $r$.

{@{A sequence $(v_n)$}@} {@{converges to $v$}@} iff {@{$\|v_n - v\|\to 0$}@}, i.e. for {@{every $\varepsilon>0$}@} there exists {@{$N$ such that $n>N\Rightarrow \|v_n-v\|<\varepsilon$}@}.

### energy

{@{Signal energy}@}: {@{$$E=\langle s,s\rangle \,.$$}@} Equivalently, {@{$\int|s(t)|^2 \, dt = \int |S(f)|^2 \,df$}@}; in {@{geometric space with an _orthonormal_ basis}@} it equals {@{the _squared_ Euclidean norm of the coordinate vector}@}.

### coordinates

To locate {@{a transmitted waveform $s(t)$}@} within {@{its signal-space representation}@}, select {@{an orthonormal basis $\{\phi_{k}(t)\}$}@} spanning {@{the subspace of interest}@}. {@{Coordinates}@} are {@{projection coefficients}@}: {@{$$a_k=\langle s(t),\,\phi_{k}(t)\rangle \;=\;\int_{0}^{T}s(t)\,\phi_{k}^{*}(t)\,dt \,.$$}@}

{@{The vector $(a_1,a_2,\dots ,a_N)^T$}@} is {@{the Euclidean-space point representing the waveform}@}. {@{Coefficients}@} are {@{unique}@} because {@{the basis is orthonormal}@}.

## properties

### algebraic properties

For {@{any three signals $x(t),y(t),z(t)$}@}: {@{$$[x(t)+y(t)] + z(t)= x(t) + [y(t)+z(t)] \,.$$}@} {@{_Associativity_}@}: {@{addition order does not matter}@}. {@{_Commutativity_}@}: {@{$$x(t)+y(t)= y(t)+x(t) \,.$$}@}

{@{Distributivity}@}: {@{$$a\, [x(t)+y(t)] = a\,x(t)+ a\,y(t) \,.$$}@} and {@{$$(a+b)\,x(t)= a\,x(t)+ b\,x(t) \,.$$}@}

{@{_Additive identity_ $0(t)$}@} leaves {@{any signal unchanged}@}: {@{$$x(t)+0(t)= x(t) \,.$$}@} {@{_Additive inverse_ $-x(t)$}@}: {@{$$x(t)+[-x(t)] = 0(t) \,.$$}@}

{@{Associativity of scalar multiplication}@}: {@{$$a(b\,x(t)) = (ab)\,x(t) \,.$$}@} {@{Multiplicative identity (field element $1$)}@}: {@{$$1\,x(t)= x(t) \,.$$}@}

### basis

{@{An $n$-dimensional vector space $S$}@} is {@{the span of $n$ basis vectors $\{e_1,\dots,e_n\}$}@}: {@{$$S=\operatorname{span}(e_1,e_2,\dots ,e_n)$$}@} {@{Any $a\in S$}@} has {@{a unique linear combination}@}: {@{$$a=\sum_{i=1}^{n}c_i\,e_i \,.$$}@} {@{The _dimension_}@} equals {@{the maximum number of linearly independent vectors in $S$}@}.

{@{A subspace}@} has {@{infinitely many orthonormal bases}@}; the choice is {@{arbitrary}@}. What matters is {@{the subspace itself}@}. {@{_Orthonormal_ bases}@} are preferred because they {@{simplify coordinate extraction}@} and preserve {@{energy without scaling factors}@}.

### coordinate representation

Given {@{a basis $\{e_i\}$}@}, {@{the _coordinate representation_}@} is {@{$$[a]_E=(c_1,c_2,\dots ,c_n)^T \,.$$}@} — a {@{one-to-one correspondence}@} between {@{vectors in $S$ and points in $\mathbb{R}^n$}@}.

### orthogonality and orthonormality

{@{A set of vectors}@} is {@{_orthonormal_}@} if {@{each pair is _orthogonal_ ($e_i^\top e_j=0$ for $i\neq j$})}@} and {@{every vector has unit norm ($\|e_i\|=1$)}@}. Coordinates {@{equal inner products}@}: {@{$$c_i=\langle a,e_i\rangle \,.$$}@}

### linear transformations

{@{A mapping $h:\mathbb{R}^n\to\mathbb{R}^m$}@} is {@{_linear_}@} if it {@{preserves addition and scalar multiplication}@}: {@{$$h(\alpha a+\beta b)=\alpha h(a)+\beta h(b), \qquad \forall\,\alpha,\beta\in\mathbb{R},\;a,b\in\mathbb{R}^n \,.$$}@}

### linear independence

{@{Vectors $a_1,\dots,a_n$}@} are {@{_linearly independent_}@} if {@{the only solution to $\sum_{i=1}^{n}\lambda_i a_i = 0$}@} is {@{$\lambda_i=0$ for all $i$}@}.

### triangle inequality

For {@{any vectors $a,b\in S$}@}, {@{$$\|a+b\|\leq \|a\|+\|b\|,$$}@} with {@{equality iff $a$ and $b$ are positively collinear}@}.

### Cauchy–Schwarz inequality

{@{The inner product}@} satisfies {@{$$|\langle a,b\rangle|\leq \|a\|\,\|b\| \,,$$}@} with {@{equality iff $a$ and $b$ are linearly dependent}@}.

### Pythagorean relation

If {@{$a$ and $b$ are orthogonal}@} ({@{$\langle a,b\rangle=0$}@}), then {@{$$\|a+b\|^2=\|a\|^2+\|b\|^2 \,.$$}@}

## Gram–Schmidt process

Given {@{any linearly independent set $\{s_1,\dots,s_M\}$}@}, {@{the _Gram–Schmidt process_}@} constructs {@{an _orthonormal_ basis $\{\phi_1,\dots,\phi_P\}$}@} for {@{the subspace they span}@}. Start with {@{a normalised copy of $s_1$}@}; then {@{subtract projections onto prior basis vectors and normalise}@}.

{@{The GS algorithm}@} is: \(annotation: 3 items: {@{first basis vector → remaining basis vectors → skip conditions}@}\)

1. first basis vector ::@:: Set $\phi_1 = s_1/\|s_1\|$.
2. remaining basis vectors ::@:: For $k=2$ to $M$: compute the projection of $s_k$ onto the span of $\{\phi_1,\dots,\phi_{k-1}\}$; subtract this projection from $s_k$ and normalise the remainder to get $\phi_k$.
3. skip conditions ::@:: If a residual becomes zero, skip to the next signal; the dimension of the signal space is less than $M$.

\(__this course__: Whenever possible, {@{identify orthogonal signals}@} {@{by inspection}@} and {@{normalize them}@}, which is {@{usually much faster}@}. Only if {@{the problem is complex or explicitly asks for a Gram–Schmidt process}@}, then {@{use the Gram–Schmidt process}@}.\)

## examples

{@{Three unit-amplitude pulses}@} occupying {@{consecutive thirds of an interval}@} are {@{_orthogonal_ (distinct subintervals)}@}. Coordinates: {@{$(1,0,0)$, $(0,1,0)$, $(0, 0, 1)$}@}; basis functions are {@{the pulses _normalized_}@}.

### sinusoidal examples

{@{Two signals $$s_1(t)=A\cos(2\pi f_ct)$$ and $$s_2(t)=A\sin(2\pi f_ct)$$}@} over {@{$[0,T)$ where $f_c$ is a _multiple_ of $1 / T$}@} are {@{orthogonal (inner product integrates to zero)}@}. Basis: {@{two-dimensional, same signals _normalized_}@}.

For {@{$$s_m'(t) = A\cos\left(2\pi f_ct + \frac {2 \pi (m - 1)} {M} \right)$$}@} with {@{$M \ge 3$ and $f_c$ as above}@}, {@{trigonometric identities}@} give {@{$$s_m'(t) = A\cos\left(\frac {2 \pi (m - 1)} {M} \right) \cos(2\pi f_c t) - A \sin\left(\frac {2 \pi (m - 1)} M \right) \sin(2\pi f_c t) \,.$$}@} {@{Same basis}@} as before.

{@{Sinusoidal signals over $[0, T)$}@} always reduce to {@{a two-dimensional linear combination}@}, so {@{_M_-PSK and _M_-QAM constellations}@} are {@{two-dimensional}@}. {@{The _inphase_ signal $I(t)$}@} is {@{the amplitude of $\cos(2\pi f_c t)$}@}; {@{the _quadrature_ signal $Q(t)$}@} is {@{the amplitude of $-\sin(2\pi f_c t)$}@}. Represented as {@{$Z(t) = I(t) + j Q(t)$}@} or plotted on {@{the constellation plane as $(I(t), Q(t))$}@}.

## applications

### receiver optimization

For {@{LTI filters}@}, {@{the matched filter}@} {@{maximises SNR}@}. In {@{signal space}@} this is equivalent to {@{projecting the received vector onto each basis function}@} and picking {@{the symbol whose coordinates}@} are {@{closest in Euclidean distance}@}.

Raising {@{bit rate}@} by {@{adding dimensions}@} requires {@{higher bandwidth or power}@}. {@{The geometric view}@} guides {@{modulation choices}@} such as {@{QAM, PSK, and OFDM}@}.

{@{Frequency-domain representation}@} can {@{represent discrete signals of length _N_ exactly}@} but uses {@{_N_ dimensions}@} — {@{_inefficient_}@} when {@{the signals lie in a lower-dimensional subspace}@}. {@{The goal of geometric-domain representation}@} is to find {@{the _minimal_ dimensions}@} containing all {@{transmitted signals}@}.

### M-ary modulation

Assigning {@{distinct vectors to each symbol}@} transmits {@{more than one bit per symbol}@}. {@{Dimensionality}@} dictates {@{how many _orthogonal_ symbols can coexist}@}; higher dimensions enable {@{denser constellations}@}.

### constellation diagram

Plotting {@{coordinate vectors}@} of {@{all allowed signals on a Euclidean plane}@} gives {@{the _constellation diagram_}@}. {@{Distances between points}@} determine {@{error probability under AWGN}@}.
