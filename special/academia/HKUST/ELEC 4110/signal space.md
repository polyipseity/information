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

{@{A __signal space__}@} is {@{an abstract vector-space representation used in digital communications}@} to model {@{transmitted waveforms as points within a multidimensional Euclidean (or Hilbert) space}@}. Using {@{an orthonormal set of basis functions}@} (often derived via {@{Gram–Schmidt orthogonalisation}@}), {@{time-domain signals}@} become {@{linear combinations whose coefficients are the coordinates}@}. <!--SR:!2026-11-27,267,345!2027-04-12,382,364!2026-12-30,280,344!2027-02-03,324,345!2027-02-03,324,345!2027-01-30,320,345!2027-03-31,373,364-->

{@{This geometric view}@} simplifies analysis of {@{modulation schemes, receiver design, and error performance}@}: visualize {@{constellations, compute Euclidean distances between symbols}@}, and build {@{matched filters that maximise SNR}@}. <!--SR:!2027-04-06,376,364!2027-02-03,324,345!2026-12-09,278,345!2027-02-21,339,345-->

## motivation

{@{The optimality of a demodulator}@} holds {@{only within the assumed receiver structure \(e.g. matched filter for LTI filters\)}@}. Changing {@{the signal space or receiver architecture}@} can yield {@{different performance for multilevel schemes}@}. <!--SR:!2027-01-25,315,345!2027-03-15,358,364!2026-12-13,281,345!2027-02-24,341,345-->

{@{Digital communication in general}@} can be analysed by representing {@{transmitted waveforms}@} as {@{vectors in a multidimensional space}@}, turning {@{complex algebra into visual intuition}@} and guiding {@{modulation, demodulation, and receiver optimisation}@}. <!--SR:!2027-03-26,368,364!2027-01-01,297,345!2027-04-09,379,364!2027-04-04,376,364!2026-12-09,277,345-->

## geometric domain

{@{A signal $s(t)$}@} can be described in {@{time domain, frequency domain, or geometric domain}@}; the first two are {@{special cases of the geometric domain}@}. <!--SR:!2027-03-28,370,364!2026-12-21,287,345!2027-02-14,333,345-->

{@{Time domain}@}: {@{A signal $s(t)$}@} is {@{a function of continuous time}@} showing {@{waveform shape, duration, and temporal features}@}. {@{Energy}@} is {@{$\int|s(t)|^{2}$ over the signal's support}@}. <!--SR:!2027-04-19,387,364!2026-12-01,271,345!2027-01-07,302,345!2027-01-24,315,345!2027-02-02,323,345!2027-01-02,298,345!2027-03-25,367,364!2027-02-02,323,345-->

{@{Frequency domain}@}: {@{The Fourier transform $S(f)=\int_{-\infty}^{\infty}s(t)e^{-j2\pi ft}\,dt$}@} maps {@{the waveform into sinusoidal components}@}, revealing {@{bandwidth and spectral occupancy}@}. {@{Parseval's theorem}@} gives {@{$\int|s(t)|^{2}dt=\int|S(f)|^{2}df$}@}, so {@{energy is preserved}@}. <!--SR:!2026-12-08,277,345!2027-02-20,337,345!2026-12-06,275,345!2027-04-05,376,364!2027-02-25,342,345!2027-02-19,337,345-->

{@{Geometric domain}@}: {@{Each waveform}@} is {@{a vector in an abstract Hilbert space}@} with {@{inner product}@} {@{$\langle u,v\rangle=\int_{0}^{T}u(t)v^{*}(t)\,dt$}@}. {@{Choosing a finite-dimensional orthonormal basis}@} converts {@{the signal into a coordinate vector}@}, letting {@{Euclidean geometry tools}@} analyze {@{constellations, design matched filters, and evaluate error probabilities}@}. <!--SR:!2027-02-15,334,345!2027-01-22,312,345!2027-02-11,330,345!2026-12-26,292,345!2026-12-17,284,345!2026-12-06,275,345!2026-12-19,286,345!2027-03-22,365,364!2027-02-08,328,345-->

{@{The time-domain waveform}@} uses {@{basis $\{\,\delta(t-t_k)\,\}$}@}, {@{the frequency domain}@} uses {@{complex exponentials $\{e^{j2\pi ft}\}$}@}; both are {@{orthonormal bases of the same Hilbert space}@} — merely {@{different coordinate systems}@} within {@{the same geometric framework}@}. <!--SR:!2027-01-06,301,345!2027-02-04,325,345!2027-02-21,338,345!2027-01-02,298,345!2026-12-05,275,345!2026-12-23,290,345!2026-12-25,291,345!2026-11-02,246,330!2026-11-09,251,330-->

## definition

Choose {@{a set of _orthonormal_ basis functions $\{\phi_k(t)\}$}@}. {@{Any finite-duration signal}@} can be written as {@{$$s(t)=\sum_{k=1}^N a_k\,\phi_k(t) \,.$$}@} {@{The coefficients $(a_1,\dots,a_N)$}@} are {@{the coordinates of the vector representing the waveform}@}. <!--SR:!2027-01-25,316,345!2027-01-28,318,345!2027-03-24,366,364!2027-01-30,320,345!2027-01-26,316,345-->

### inner product

{@{The _inner product_}@} is {@{a function $$\langle\,\cdot,\cdot\,\rangle : V\times V \longrightarrow \mathbb{F}$$}@} satisfying {@{these axioms}@} for {@{all vectors $u,v,w\in V$ and scalars $a\in\mathbb{F}$}@}: \(annotation: 3 items: {@{conjugate symmetry, linearity in the first argument, positive definiteness}@}\) <!--SR:!2027-01-29,319,345!2027-01-29,319,345!2027-04-07,378,364!2027-04-14,383,364!2027-01-29,319,345-->

1. Conjugate symmetry: ::@:: $\langle u,v\rangle = \overline{\langle v,u\rangle}$. <!--SR:!2027-02-01,322,345!2027-01-25,315,345-->
2. Linearity in the first argument ::@:: $\langle u+v,w\rangle = \langle u,w\rangle + \langle v,w\rangle$, and $\langle au,v\rangle = a\,\langle u,v\rangle$. <!--SR:!2027-02-02,323,345!2027-02-22,339,345-->
3. Positive definiteness: ::@:: $\langle u,u\rangle \ge 0$ with equality iff $u=0$. <!--SR:!2027-02-15,334,345!2027-02-16,334,345-->

These imply {@{the _induced norm_ $$\|v\|=\sqrt{\langle v,v\rangle}$$ (Euclidean length)}@}. {@{Two vectors}@} are {@{_orthogonal_}@} if {@{$\langle u,v\rangle=0$}@}; {@{_orthonormal_}@} when {@{also unit norm}@}. <!--SR:!2027-02-06,326,345!2026-12-22,288,345!2027-04-03,375,364!2027-01-05,300,345!2027-01-21,311,345!2026-10-22,237,330!2027-02-12,331,345!2027-01-25,316,345-->

For {@{continuous-time signals}@}: {@{$$\langle u,v\rangle = \int_{0}^{T}u(t)v^*(t)\,dt \,.$$}@} {@{A signal $s(t)$ has unit norm}@} when {@{energy equals one}@}: {@{$$\|s\|^2 = \langle s,s\rangle = \int_{0}^{T}|s(t)|^{2}\,dt = 1 \,.$$}@} <!--SR:!2027-02-19,337,345!2026-12-11,280,345!2027-01-08,303,345!2027-03-23,365,364!2026-11-29,269,345!2027-02-04,325,345!2027-01-28,318,345-->

### geometric concepts

- _Length_: ::@:: The magnitude of a vector is $\|v\| = \sqrt{\langle v,v\rangle}$. <!--SR:!2026-12-08,277,345!2027-02-23,340,345-->
- _Distance_: ::@:: Between $u$ and $v$ it is $\|u-v\|=\sqrt{\langle u-v,\,u-v\rangle}$. <!--SR:!2026-11-28,268,345!2027-01-23,313,345-->
- _Angle_: ::@:: The cosine of the angle between non-zero vectors $u$ and $v$ is $$\cos\theta = \frac{\langle u,v\rangle}{\|u\|\;\|v\|} \,.$$ <!--SR:!2027-03-27,369,364!2027-02-13,332,345-->
- _Orthogonality_: ::@:: Vectors are orthogonal if their inner product vanishes: $\langle u,v\rangle=0$. <!--SR:!2027-01-28,318,345!2027-03-20,363,364-->
- _Circles and spheres_: ::@:: The set $\{x\in V : \|x-x_c\| = r\}$ describes a circle (or hypersphere) centered at $x_c$ with radius $r$. <!--SR:!2027-02-24,341,345!2027-02-16,334,345-->

{@{A sequence $(v_n)$}@} {@{converges to $v$}@} iff {@{$\|v_n - v\|\to 0$}@}, i.e. for {@{every $\varepsilon>0$}@} there exists {@{$N$ such that $n>N\Rightarrow \|v_n-v\|<\varepsilon$}@}. <!--SR:!2027-01-24,314,345!2027-03-14,357,364!2027-02-05,325,345!2027-02-10,330,345!fsrs,2029-02-04T00:00:00.000Z,893,892.52825833,1,2,9,0,0,2026-08-26T00:00:00.000Z!2027-02-23,340,345-->

### energy

{@{Signal energy}@}: {@{$$E=\langle s,s\rangle \,.$$}@} Equivalently, {@{$\int|s(t)|^2 \, dt = \int |S(f)|^2 \,df$}@}; in {@{geometric space with an _orthonormal_ basis}@} it equals {@{the _squared_ Euclidean norm of the coordinate vector}@}. <!--SR:!2026-12-23,290,345!2026-10-24,238,330!2027-02-18,336,345!2027-01-30,320,345!2027-02-18,335,345!2026-11-13,255,330!2027-01-24,314,345!2027-02-17,335,345-->

### coordinates

To locate {@{a transmitted waveform $s(t)$}@} within {@{its signal-space representation}@}, select {@{an orthonormal basis $\{\phi_{k}(t)\}$}@} spanning {@{the subspace of interest}@}. {@{Coordinates}@} are {@{projection coefficients}@}: {@{$$a_k=\langle s(t),\,\phi_{k}(t)\rangle \;=\;\int_{0}^{T}s(t)\,\phi_{k}^{*}(t)\,dt \,.$$}@} <!--SR:!fsrs,2029-02-19T00:00:00.000Z,904,904.19353564,1,2,9,0,0,2026-08-30T00:00:00.000Z!2026-12-18,285,345!2027-02-01,322,345!2027-01-27,318,345!2027-02-03,324,345!2026-12-03,272,345!2027-07-25,448,325-->

{@{The vector $(a_1,a_2,\dots ,a_N)^T$}@} is {@{the Euclidean-space point representing the waveform}@}. {@{Coefficients}@} are {@{unique}@} because {@{the basis is orthonormal}@}. <!--SR:!2027-01-07,302,345!2027-01-21,311,345!2027-02-10,330,345!2027-01-23,314,345!2026-12-28,294,345!2027-02-17,335,345-->

## properties

### algebraic properties

For {@{any three signals $x(t),y(t),z(t)$}@}: {@{$$[x(t)+y(t)] + z(t)= x(t) + [y(t)+z(t)] \,.$$}@} {@{_Associativity_}@}: {@{addition order does not matter}@}. {@{_Commutativity_}@}: {@{$$x(t)+y(t)= y(t)+x(t) \,.$$}@} <!--SR:!2027-01-28,318,345!2027-02-09,329,345!2027-01-19,312,345!2027-01-04,299,345!2027-02-25,342,345!2027-01-06,301,345!2027-02-26,343,345!2026-12-12,280,345!2027-01-26,317,345!2027-03-24,367,364-->

{@{Distributivity}@}: {@{$$a\, [x(t)+y(t)] = a\,x(t)+ a\,y(t) \,.$$}@} and {@{$$(a+b)\,x(t)= a\,x(t)+ b\,x(t) \,.$$}@} <!--SR:!2027-04-06,377,364!2027-01-30,321,345!2026-12-22,289,345!2027-02-15,334,345!2026-12-11,279,345!2027-02-22,339,345!2026-11-12,254,330!2027-03-22,364,364!2027-01-31,321,345-->

{@{_Additive identity_ $0(t)$}@} leaves {@{any signal unchanged}@}: {@{$$x(t)+0(t)= x(t) \,.$$}@} {@{_Additive inverse_ $-x(t)$}@}: {@{$$x(t)+[-x(t)] = 0(t) \,.$$}@} <!--SR:!2027-02-04,325,345!2027-02-13,332,345!2027-02-19,337,345!2027-02-20,338,345!2026-11-11,253,330!2027-02-12,331,345!2027-02-04,325,345!2027-01-04,299,345!2027-01-05,300,345!2027-02-02,323,345!2027-02-02,323,345-->

{@{Associativity of scalar multiplication}@}: {@{$$a(b\,x(t)) = (ab)\,x(t) \,.$$}@} {@{Multiplicative identity (field element $1$)}@}: {@{$$1\,x(t)= x(t) \,.$$}@}

### basis

{@{An $n$-dimensional vector space $S$}@} is {@{the span of $n$ basis vectors $\{e_1,\dots,e_n\}$}@}: {@{$$S=\operatorname{span}(e_1,e_2,\dots ,e_n)$$}@} {@{Any $a\in S$}@} has {@{a unique linear combination}@}: {@{$$a=\sum_{i=1}^{n}c_i\,e_i \,.$$}@} {@{The _dimension_}@} equals {@{the maximum number of linearly independent vectors in $S$}@}. <!--SR:!2027-04-15,384,364!2027-04-02,374,364!2027-01-31,321,345!2027-02-01,322,345!2027-01-22,312,345!2027-04-16,385,364!2027-01-26,316,345!2026-12-24,290,345!2026-10-23,237,330!2027-02-01,322,345!2027-01-03,299,345-->

{@{A subspace}@} has {@{infinitely many orthonormal bases}@}; the choice is {@{arbitrary}@}. What matters is {@{the subspace itself}@}. {@{_Orthonormal_ bases}@} are preferred because they {@{simplify coordinate extraction}@} and preserve {@{energy without scaling factors}@}.

### coordinate representation

Given {@{a basis $\{e_i\}$}@}, {@{the _coordinate representation_}@} is {@{$$[a]_E=(c_1,c_2,\dots ,c_n)^T \,.$$}@} — a {@{one-to-one correspondence}@} between {@{vectors in $S$ and points in $\mathbb{R}^n$}@}. <!--SR:!2027-02-01,322,345!2026-11-07,250,330!2026-11-06,249,330!2027-01-22,314,345!2027-01-27,317,345!2027-01-30,321,345!2027-02-14,333,345-->

### orthogonality and orthonormality

{@{A set of vectors}@} is {@{_orthonormal_}@} if {@{each pair is _orthogonal_ ($e_i^\top e_j=0$ for $i\neq j$})}@} and {@{every vector has unit norm ($\|e_i\|=1$)}@}. Coordinates {@{equal inner products}@}: {@{$$c_i=\langle a,e_i\rangle \,.$$}@} <!--SR:!2027-04-07,378,364!2027-01-02,298,345!2027-03-16,359,364!2026-12-16,284,345!2027-03-30,372,364!2027-01-23,313,345!2026-11-29,269,345!2027-01-29,320,345!2026-12-08,276,345-->

### linear transformations

{@{A mapping $h:\mathbb{R}^n\to\mathbb{R}^m$}@} is {@{_linear_}@} if it {@{preserves addition and scalar multiplication}@}: {@{$$h(\alpha a+\beta b)=\alpha h(a)+\beta h(b), \qquad \forall\,\alpha,\beta\in\mathbb{R},\;a,b\in\mathbb{R}^n \,.$$}@} <!--SR:!2027-02-06,326,345!2027-02-08,328,345!2027-02-18,336,345!2027-04-10,380,364-->

### linear independence

{@{Vectors $a_1,\dots,a_n$}@} are {@{_linearly independent_}@} if {@{the only solution to $\sum_{i=1}^{n}\lambda_i a_i = 0$}@} is {@{$\lambda_i=0$ for all $i$}@}. <!--SR:!2026-10-19,234,330!2026-12-10,279,345!2026-12-15,283,345!2027-02-26,343,345!2027-02-20,338,345!2027-01-30,320,345-->

### triangle inequality

For {@{any vectors $a,b\in S$}@}, {@{$$\|a+b\|\leq \|a\|+\|b\|,$$}@} with {@{equality iff $a$ and $b$ are positively collinear}@}. <!--SR:!2027-02-08,328,345!2027-01-29,319,345!2026-11-28,268,345!2026-12-26,292,345!2027-02-09,329,345-->

### Cauchy–Schwarz inequality

{@{The inner product}@} satisfies {@{$$|\langle a,b\rangle|\leq \|a\|\,\|b\| \,,$$}@} with {@{equality iff $a$ and $b$ are linearly dependent}@}. <!--SR:!2027-01-08,303,345!2027-02-08,328,345!2027-02-05,325,345!2026-12-25,291,345-->

### Pythagorean relation

If {@{$a$ and $b$ are orthogonal}@} ({@{$\langle a,b\rangle=0$}@}), then {@{$$\|a+b\|^2=\|a\|^2+\|b\|^2 \,.$$}@} <!--SR:!2027-02-24,341,345!2026-12-05,274,345!2027-01-01,297,345!2027-02-04,325,345-->

## Gram–Schmidt process

Given {@{any linearly independent set $\{s_1,\dots,s_M\}$}@}, {@{the _Gram–Schmidt process_}@} constructs {@{an _orthonormal_ basis $\{\phi_1,\dots,\phi_P\}$}@} for {@{the subspace they span}@}. Start with {@{a normalised copy of $s_1$}@}; then {@{subtract projections onto prior basis vectors and normalise}@}. <!--SR:!2027-01-04,299,345!2027-01-31,321,345!2027-01-08,303,345!2027-03-21,363,364!2026-12-14,282,345!2027-02-04,325,345!2026-12-19,286,345!2027-01-26,316,345!2027-02-03,324,345-->

{@{The GS algorithm}@} is: \(annotation: 3 items: {@{first basis vector → remaining basis vectors → skip conditions}@}\) <!--SR:!2026-12-18,285,345-->

1. first basis vector ::@:: Set $\phi_1 = s_1/\|s_1\|$. <!--SR:!2026-12-27,293,345!2026-12-28,294,345-->
2. remaining basis vectors ::@:: For $k=2$ to $M$: compute the projection of $s_k$ onto the span of $\{\phi_1,\dots,\phi_{k-1}\}$; subtract this projection from $s_k$ and normalise the remainder to get $\phi_k$. <!--SR:!2027-02-14,333,345!fsrs,2029-02-03T00:00:00.000Z,893,892.52825833,1,2,9,0,0,2026-08-25T00:00:00.000Z-->
3. skip conditions ::@:: If a residual becomes zero, skip to the next signal; the dimension of the signal space is less than $M$. <!--SR:!2026-12-20,287,345!2027-01-29,320,345-->

\(__this course__: Whenever possible, {@{identify orthogonal signals}@} {@{by inspection}@} and {@{normalize them}@}, which is {@{usually much faster}@}. Only if {@{the problem is complex or explicitly asks for a Gram–Schmidt process}@}, then {@{use the Gram–Schmidt process}@}.\) <!--SR:!2027-02-18,336,345!2026-10-20,235,330!2027-01-07,302,345!2027-01-21,311,345!2027-02-10,330,345!2027-01-03,299,345-->

## examples

{@{Three unit-amplitude pulses}@} occupying {@{consecutive thirds of an interval}@} are {@{_orthogonal_ (distinct subintervals)}@}. Coordinates: {@{$(1,0,0)$, $(0,1,0)$, $(0, 0, 1)$}@}; basis functions are {@{the pulses _normalized_}@}. <!--SR:!2027-04-08,379,364!2026-12-04,274,345!2027-02-03,324,345!2027-04-11,381,364!2027-02-07,327,345!2026-10-27,240,330!2026-12-03,273,345!2027-01-20,312,345-->

### sinusoidal examples

{@{Two signals $$s_1(t)=A\cos(2\pi f_ct)$$ and $$s_2(t)=A\sin(2\pi f_ct)$$}@} over {@{$[0,T)$ where $f_c$ is a _multiple_ of $1 / T$}@} are {@{orthogonal (inner product integrates to zero)}@}. Basis: {@{two-dimensional, same signals _normalized_}@}. <!--SR:!2027-02-13,332,345!2027-02-11,330,345!2027-02-12,331,345!2027-03-17,360,364!2027-04-18,386,364!2027-01-26,317,345!2027-04-20,388,364!2027-01-27,317,345!2027-02-26,343,345-->

For {@{$$s_m'(t) = A\cos\left(2\pi f_ct + \frac {2 \pi (m - 1)} {M} \right)$$}@} with {@{$M \ge 3$ and $f_c$ as above}@}, {@{trigonometric identities}@} give {@{$$s_m'(t) = A\cos\left(\frac {2 \pi (m - 1)} {M} \right) \cos(2\pi f_c t) - A \sin\left(\frac {2 \pi (m - 1)} M \right) \sin(2\pi f_c t) \,.$$}@} {@{Same basis}@} as before. <!--SR:!2027-01-31,321,345!2027-02-03,324,345!2026-12-21,288,345!2026-11-08,251,330!2027-02-10,330,345!2027-01-28,319,345!2027-02-02,323,345-->

{@{Sinusoidal signals over $[0, T)$}@} always reduce to {@{a two-dimensional linear combination}@}, so {@{_M_-PSK and _M_-QAM constellations}@} are {@{two-dimensional}@}. {@{The _inphase_ signal $I(t)$}@} is {@{the amplitude of $\cos(2\pi f_c t)$}@}; {@{the _quadrature_ signal $Q(t)$}@} is {@{the amplitude of $-\sin(2\pi f_c t)$}@}. Represented as {@{$Z(t) = I(t) + j Q(t)$}@} or plotted on {@{the constellation plane as $(I(t), Q(t))$}@}. <!--SR:!2026-11-01,245,330!2027-02-23,340,345!2027-02-21,339,345!2027-02-01,322,345!2027-01-03,299,345!2027-01-03,299,345!2027-02-22,339,345!2027-01-01,297,345!2027-01-25,315,345!2026-12-02,272,345!2027-02-14,333,345-->

## applications

### receiver optimization

For {@{LTI filters}@}, {@{the matched filter}@} {@{maximises SNR}@}. In {@{signal space}@} this is equivalent to {@{projecting the received vector onto each basis function}@} and picking {@{the symbol whose coordinates}@} are {@{closest in Euclidean distance}@}. <!--SR:!2026-10-31,244,330!2027-02-25,342,345!2027-01-31,321,345!2027-02-06,326,345!2027-02-13,332,345!2027-02-04,325,345!2027-02-18,336,345-->

Raising {@{bit rate}@} by {@{adding dimensions}@} requires {@{higher bandwidth or power}@}. {@{The geometric view}@} guides {@{modulation choices}@} such as {@{QAM, PSK, and OFDM}@}. <!--SR:!2027-02-24,341,345!2027-03-26,369,364!2027-01-03,299,345!2026-11-30,270,345!2027-01-02,298,345!2027-02-11,330,345-->

{@{Frequency-domain representation}@} can {@{represent discrete signals of length _N_ exactly}@} but uses {@{_N_ dimensions}@} — {@{_inefficient_}@} when {@{the signals lie in a lower-dimensional subspace}@}. {@{The goal of geometric-domain representation}@} is to find {@{the _minimal_ dimensions}@} containing all {@{transmitted signals}@}. <!--SR:!2027-02-03,324,345!2027-01-02,298,345!2027-02-25,342,345!2027-01-01,297,345!2026-12-27,293,345!2026-12-04,273,345!2027-02-19,337,345!2026-12-12,280,345!2026-10-26,240,330!2027-03-19,362,364!2026-12-16,284,345!2027-02-07,327,345-->

### M-ary modulation

Assigning {@{distinct vectors to each symbol}@} transmits {@{more than one bit per symbol}@}. {@{Dimensionality}@} dictates {@{how many _orthogonal_ symbols can coexist}@}; higher dimensions enable {@{denser constellations}@}. <!--SR:!2027-02-09,329,345!2027-02-15,334,345!2027-03-18,361,364!2027-02-04,325,345!2026-10-21,237,344!2027-02-19,336,345!2027-01-21,313,345-->

### constellation diagram

Plotting {@{coordinate vectors}@} of {@{all allowed signals on a Euclidean plane}@} gives {@{the _constellation diagram_}@}. {@{Distances between points}@} determine {@{error probability under AWGN}@}. <!--SR:!2026-12-07,276,345!2027-01-05,300,345!2026-12-10,278,345!2027-01-27,317,345!2026-10-21,236,330!2027-02-14,333,345-->
