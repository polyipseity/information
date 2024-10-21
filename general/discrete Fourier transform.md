---
aliases:
  - DFT
  - discrete Fourier transform
  - discrete Fourier transforms
tags:
  - flashcard/active/general/discrete_Fourier_transform
  - language/in/English
---

# discrete Fourier transform

_Not to be confused with the [discrete-time Fourier transform](discrete-time%20Fourier%20transform.md)._

In [mathematics](mathematics.md), {{the __discrete Fourier transform__ (__DFT__)}} {{converts a finite sequence of equally-spaced [samples](sampling%20(signal%20processing).md) of a [function](function%20(mathematics).md) into a same-length sequence of equally-spaced samples of the [discrete-time Fourier transform](discrete-time%20Fourier%20transform.md) (DTFT)}}, which is {{a [complex-valued](complex%20number.md) function of frequency}}. The interval at which the DTFT is sampled is {{the reciprocal of the duration of the input sequence}}. {{An inverse DFT (IDFT)}} is {{a [Fourier series](fourier%20series.md), using the DTFT samples as coefficients of [complex](complex%20number.md) [sinusoids](sine%20wave.md) at the corresponding DTFT frequencies}}. It has {{the same sample-values as the original input sequence}}. The DFT is therefore said to be {{a [frequency domain](frequency%20domain.md) representation of the original input sequence}}. If {{the original sequence spans all the non-zero values of a function (i.e. the function has one copy of the original sequence and zero everywhere else)}}, its DTFT is {{continuous (and periodic), and the DFT provides discrete samples of one cycle}}. If {{the original sequence is one cycle of a periodic function}}, {{the DFT provides all the non-zero values of one DTFT cycle}}. <!--SR:!2025-04-02,174,310!2025-02-08,131,290!2025-06-09,236,330!2025-02-04,119,290!2024-10-30,63,310!2024-11-20,67,270!2025-03-05,156,310!2024-11-19,73,290!2024-12-08,77,270!2024-12-23,97,290!2025-01-22,112,290!2024-11-01,65,310-->

> [!tip] tips
>
> - interpretation of the DFT of a sequence ::: The modulus (length) of the complex number for each frequency is the amplitude (e.g. loudness) of that frequency. The argument (angle) of the complex number for each frequency is the phase (e.g. time offset) of that frequency. <!--SR:!2024-11-28,80,346!2024-10-24,51,326-->

## definition

The _discrete Fourier transform_ {{transforms a [sequence](sequence.md) of _N_ [complex numbers](complex%20number.md) $\set{\mathbf x_n} := x_0, x_1, \ldots, x_{N−1}$ into another sequence of complex numbers, $\set{\mathbf X_k} := X_0, X_1, \ldots, X_{N−1}$}}, which is defined by: <!--SR:!2024-11-10,61,326-->

> {{__discrete Fourier transform (Eq. 1)__}}
>
> {{$$X_k = \sum_{n = 0}^{N - 1} x_n \cdot e^{-i2\pi \frac k N n}$$}} <!--SR:!2024-11-02,68,310!2025-03-21,155,290-->

The transform is sometimes denoted by {{$\mathcal F$, as in $\mathbf X = \mathcal F\set{\mathbf x}$ or $\mathcal F(\mathbf x)$ or $\mathcal F \mathbf x$}}. <!--SR:!2024-10-28,61,310-->

__Eq.1__ can be {{interpreted or derived in various ways}}, for example: <!--SR:!2025-03-12,162,310-->

- discrete Fourier transform & discrete-time Fourier transform ::: It completely describes the [discrete-time Fourier transform](discrete-time%20Fourier%20transform.md) (DTFT) of an $N$-periodic sequence, which comprises only discrete frequency components. ([Using the DTFT with periodic data](discrete-time%20Fourier%20transform.md#periodic%20data)) <!--SR:!2025-01-14,114,290!2025-03-17,160,310-->
- discrete Fourier transform & sampling ::: It can also provide uniformly spaced samples of the continuous DTFT of a finite length sequence. The sampling interval is the reciprocal of the duration of the input sequence. ([§ sampling the DTFT](discrete-time%20Fourier%20transform.md#sampling%20the%20DTFT)) <!--SR:!2025-01-01,98,290!2025-03-02,152,310-->
- discrete Fourier transform & complex sinusoid ::: It is the [cross correlation](cross-correlation.md) of the _input_ sequence, $x_n$, and a complex sinusoid at frequency $k / N$ (angular frequency $2 \pi k / N$). Thus it acts like a [matched filter](matched%20filter.md) for that frequency. <!--SR:!2024-12-17,85,270!2024-12-25,90,270-->
- discrete Fourier transform & Fourier series ::: It is the discrete analog of the formula for the coefficients of a [Fourier series](fourier%20series.md): $$C_k = \frac 1 P \int_P \! x(t) e^{-i2\pi \frac k P t} \,\mathrm{d}t$$.  The above equation corresponds to the discrete analog in the following ways: $x(0), x(1 / N), \ldots, x(1 - 1 / N)$ corresponds to $x_0, x_1, \ldots, x_{N - 1}$. $P$ corresponds to $1$. $t$ corresponds to $n / N$. The $k / P$ expression also hints at why the sampling interval of the frequency domain is the reciprocal of the duration of the input sequence. <!--SR:!2024-11-07,19,210!2024-12-03,75,270-->

__Eq.1__ can also be evaluated {{outside the domain $k \in [0 , N - 1]$, and that extended sequence is $N$-[periodic](periodic%20sequence.md)}}. Accordingly, other sequences of $N$ indices are sometimes used, such as {{$\left[-\frac N 2,\frac N 2 - 1 \right]$ (if $N$ is even) and $\left[-\frac {N - 1} 2,\frac {N - 1} 2 \right]$ (if $N$ is odd)}}, which amounts to {{swapping the left and right halves of the result of the transform}}. <!--SR:!2025-05-02,199,310!2024-11-11,58,270!2025-01-09,109,290-->

The inverse transform is given by:

> {{__inverse discrete Fourier transform (Eq.2)__}}
>
> {{$$x_n = \frac 1 N \sum_{k = 0}^{N - 1} X_k \cdot e^{i 2\pi \frac k N n}$$}} <!--SR:!2024-11-03,61,270!2024-11-16,65,270-->

__Eq.2__ is {{also $N$-periodic (in index $n$)}}. In __Eq.2__, each $X_k$ is {{a complex number whose polar coordinates are the amplitude and phase of a complex sinusoidal component $\left(e^{i 2\pi \frac k N n}\right)$ of function $x_n$}}. (see [discrete Fourier series](discrete%20Fourier%20series.md)) The sinusoid's [frequency](frequency.md) is {{$k$ cycles per $N$ samples}}. <!--SR:!2024-10-28,63,310!2025-02-09,124,290!2024-11-02,66,310-->

{{The normalization factor multiplying the DFT and IDFT (here $1$ and $\frac 1 N$) and the signs of the exponents}} are {{the most common [conventions](sign%20convention.md)}}. The only actual requirements of these conventions are that {{the DFT and IDFT have opposite-sign exponents and that the product of their normalization factors be $\frac 1 N$}}. {{An uncommon normalization of $\sqrt{\frac 1 N}$ for both the DFT and IDFT}} makes {{the transform-pair unitary}}. <!--SR:!2024-10-25,60,310!2024-10-26,59,310!2024-11-02,65,310!2025-03-08,144,290!2025-01-26,115,290-->

## properties

### linearity

The DFT is {{a linear transform}}, i.e. if {{${\mathcal {F} }(\{x_{n}\})_{k}=X_{k}$ and ${\mathcal {F} }(\{y_{n}\})_{k}=Y_{k}$}}, then {{for any complex numbers $a,b$: $${\mathcal {F} }(\{ax_{n}+by_{n}\})_{k}=aX_{k}+bY_{k}$$}}. <!--SR:!2024-11-03,64,336!2024-11-15,74,336!2024-11-17,75,336-->

### time and frequency reversal

Reversing the time (i.e. {{replacing $n$ by $N-n$}}) in $x_{n}$ corresponds to {{reversing the frequency (i.e. $k$ by $N-k$)}}. Mathematically, if $\{x_{n}\}$ represents the vector __x__ then {{$${\mathcal {F} }(\{x_{n}\})_{k}=X_{k} \implies {\mathcal {F} }(\{x_{N-n}\})_{k}=X_{N-k}$$}}. <!--SR:!2025-06-13,235,336!2024-10-25,56,316!2024-11-23,81,336-->

### conjugation in time

Mathematically: {{$${\mathcal {F} }(\{x_{n}\})_{k}=X_{k} \implies {\mathcal {F} }(\{x_{n}^{*}\})_{k}=X_{N-k}^{*}$$}}. <!--SR:!2025-04-26,193,316-->

### real and imaginary part

This table shows {{some mathematical operations on $x_{n}$ in the time domain and the corresponding effects on its DFT $X_{k}$ in the frequency domain}}. <!--SR:!2025-03-26,169,336-->

| property                    | time domain $x_{n}$                                | frequency domain $X_{k}$                           |
| --------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| real part in time           | $$\operatorname {Re} {\left(x_{n}\right)}$$        | $${\frac {1}{2} }\left(X_{k}+X_{N-k}^{*}\right)$$  |
| imaginary part in time      | $$\operatorname {Im} {\left(x_{n}\right)}$$        | $${\frac {1}{2i} }\left(X_{k}-X_{N-k}^{*}\right)$$ |
| real part in frequency      | $${\frac {1}{2} }\left(x_{n}+x_{N-n}^{*}\right)$$  | $$\operatorname {Re} {\left(X_{k}\right)}$$        |
| imaginary part in frequency | $${\frac {1}{2i} }\left(x_{n}-x_{N-n}^{*}\right)$$ | $$\operatorname {Im} {\left(X_{k}\right)}$$        |

- real part in time ::: frequency: $$\frac 1 2 (X_k + X^*_{N - k})$$ <!--SR:!2024-10-24,55,316!2024-10-26,57,316-->
- imaginary part in time ::: frequency: $$\frac 1 {2i} (X_k - X^*_{N - k})$$ <!--SR:!2024-11-04,53,276!2024-11-20,78,336-->
- real part in frequency ::: time: $$\frac 1 2 (x_n + x^*_{N - n})$$ <!--SR:!2024-12-19,91,296!2024-11-08,69,336-->
- imaginary part in frequency ::: time: $$\frac 1 {2i} (x_n - x^*_{N - n})$$ <!--SR:!2025-03-08,144,316!2024-10-30,61,336-->

### orthogonality

The vectors {{$u_{k}=\left[\left.e^{ {\frac {i2\pi }{N} }kn}\;\right|\;n=0,1,\ldots ,N-1\right]^{\mathsf {T} }$}} form {{an [orthogonal basis](orthogonal%20basis.md) over the set of _N_-dimensional complex vectors}}: {{$$u_{k}^{\mathsf {T} }u_{k'}^{*}=\sum _{n=0}^{N-1}\left(e^{ {\frac {i2\pi }{N} }kn}\right)\left(e^{ {\frac {i2\pi }{N} }(-k')n}\right)=\sum _{n=0}^{N-1}e^{ {\frac {i2\pi }{N} }(k-k')n}=N~\delta _{kk'}$$}} where {{$\delta _{kk'}$ is the [Kronecker delta](kronecker%20delta.md)}}. (In the last step, {{the summation is trivial if $k=k'$, where it is 1 + 1 + ⋯ = _N_}}, and {{otherwise is a [geometric series](geometric%20series.md) that can be explicitly summed to obtain zero}}.) This orthogonality condition can be used to {{derive the formula for the IDFT from the definition of the DFT}}, and is {{equivalent to the unitary property below}}. <!--SR:!2024-11-09,56,276!2024-10-30,58,316!2024-10-25,54,316!2024-11-04,65,336!2025-04-08,182,336!2024-11-09,70,336!2025-05-27,222,336!2024-11-30,60,276-->

### The Plancherel theorem and Parseval's theorem

If {{$X_{k}$ and $Y_{k}$ are the DFTs of $x_{n}$ and $y_{n}$ respectively}} then {{[Parseval's theorem](parseval's%20theorem.md)}} states: {{$$\sum _{n=0}^{N-1}x_{n}y_{n}^{*}={\frac {1}{N} }\sum _{k=0}^{N-1}X_{k}Y_{k}^{*}$$}} where the star denotes [complex conjugation](complex%20conjugate.md). {{The [Plancherel theorem](plancherel%20theorem.md)}} is {{a special case of Parseval's theorem}} and states: {{$$\sum _{n=0}^{N-1}|x_{n}|^{2}={\frac {1}{N} }\sum _{k=0}^{N-1}|X_{k}|^{2}$$}}. <!--SR:!2024-10-22,54,316!2025-03-08,144,316!2024-11-10,26,296!2024-12-08,76,276!2025-04-10,182,336!2024-11-02,64,336-->

These theorems are {{also equivalent to the unitary condition below}}. <!--SR:!2025-03-25,157,316-->

### periodicity

The periodicity can be {{shown directly from the definition}}: {{$$X_{k+N}\ \triangleq \ \sum _{n=0}^{N-1}x_{n}e^{-{\frac {i2\pi }{N} }(k+N)n}=\sum _{n=0}^{N-1}x_{n}e^{-{\frac {i2\pi }{N} }kn}\underbrace {e^{-i2\pi n} } _{1}=\sum _{n=0}^{N-1}x_{n}e^{-{\frac {i2\pi }{N} }kn}=X_{k}$$}}. <!--SR:!2024-10-24,56,316!2024-11-08,68,336-->

Similarly, it can be {{shown that the IDFT formula leads to a periodic extension}}. <!--SR:!2024-10-22,54,316-->

### shift theorem

Multiplying {{$x_{n}$ by a _linear phase_ $e^{ {\frac {i2\pi }{N} }nm}$ for some integer _m_}} corresponds to {{a _circular shift_ of the output $X_{k}$: $X_{k}$ is replaced by $X_{k-m}$ (shifted to the right, with warping, by _m_)}}, where {{the subscript is interpreted [modulo](modular%20arithmetic.md) _N_ (i.e., periodically)}}. Similarly, {{a circular shift of the input $x_{n}$ (e.g. shifted to the right, with warping, by _m_) corresponds to multiplying the output $X_{k}$ by a linear phase (with an opposite exponent sign, e.g. $e^{-\frac {i 2\pi} N km}$)}}. Mathematically, if $\{x_{n}\}$ represents the vector __x__ then {{$$\begin{aligned} {\mathcal {F} }(\{x_{n}\})_{k}=X_{k} & \implies {\mathcal {F} }\left(\left\{x_{n}\cdot e^{ {\frac {i2\pi }{N} }nm}\right\}\right)_{k}=X_{k-m} \\ \cdots & \implies {\mathcal {F} }\left(\left\{x_{n-m}\right\}\right)_{k}=X_{k}\cdot e^{-{\frac {i2\pi }{N} }km} \end{aligned}$$}}. <!--SR:!2025-03-20,156,316!2024-11-26,68,276!2024-10-29,56,316!2024-12-08,77,276!2025-01-01,101,296-->

> [!tip] tips
>
> - interpretation of the shift theorem ::: The Fourier shift theorem from the time domain to the frequency domain has an intuitive interpretation. Interpret the argument (angle) of the complex number for each frequency as its time offset. Shifting a signal to the right (with warping) in the time domain increases the time offset for all frequencies. This means the complex number for each frequency is multiplied (rotated) by $e^{-\frac {i 2\pi} N km}$, changing its argument (angle) while keeping its modulus (length) unchanged. This corresponds to shifting its corresponding complex sinusoid in the time domain to the right (with warping). <!--SR:!2024-12-03,70,287!2024-10-25,52,327-->

### circular convolution theorem

- seee: [convolution theorem § functions of a discrete variable (sequences)](convolution%20theorem.md#functions%20of%20a%20discrete%20variable%20(sequences))

{{The [convolution theorem](discrete-time%20Fourier%20transform.md#convolution) for the [discrete-time Fourier transform](discrete-time%20Fourier%20transform.md) (DTFT)}} indicates that {{a convolution of two sequences can be obtained as the inverse transform of the product of the individual transforms}}. An important simplification occurs when {{one of sequences is N-periodic, denoted here by $y_{_{N} }$}}, because {{$\scriptstyle {\text{DTFT} }\displaystyle \{y_{_{N} }\}$ is non-zero at only discrete frequencies (see [DTFT § periodic data](discrete-time%20Fourier%20transform.md#periodic%20data)), and therefore so is its product with the continuous function $\scriptstyle {\text{DTFT} }\displaystyle \{x\}$}}. That leads to {{a considerable simplification of the inverse transform}}: {{$$x*y_{_{N} }\ =\ \scriptstyle {\rm {DTFT} }^{-1}\displaystyle \left[\scriptstyle {\rm {DTFT} }\displaystyle \{x\}\cdot \scriptstyle {\rm {DTFT} }\displaystyle \{y_{_{N} }\}\right]\ =\ \scriptstyle {\rm {DFT} }^{-1}\displaystyle \left[\scriptstyle {\rm {DFT} }\displaystyle \{x_{_{N} }\}\cdot \scriptstyle {\rm {DFT} }\displaystyle \{y_{_{N} }\}\right]$$}}, where {{$x_{_{N} }$ is a [periodic summation](periodic%20summation.md) of the $x$ sequence: $(x_{_{N} })_{n}\ \triangleq \sum _{m=-\infty }^{\infty }x_{(n-mN)}$}}. <!--SR:!2024-11-08,58,327!2024-11-28,79,347!2024-12-06,86,347!2024-12-25,94,307!2024-11-17,71,347!2025-02-16,131,307!2024-11-23,75,347-->

Customarily, the DFT and inverse DFT summations are taken {{over the domain $[0, N - 1]$}}. Defining those DFTs as $X$ and $Y$, the result is: {{$$(x*y_{_{N} })_{n}\triangleq \sum _{\ell =-\infty }^{\infty }x_{\ell }\cdot (y_{_{N} })_{n-\ell }=\underbrace { {\mathcal {F} }^{-1} } _{\rm {DFT^{-1} } }\left\{X\cdot Y\right\}_{n}$$}}. <!--SR:!2024-11-14,68,347!2024-11-18,57,287-->

In practice, {{the $x$ sequence is usually length _N_ or less}}, and $y_{_{N} }$ is {{a periodic extension of an N-length $y$-sequence, which can also be expressed as a _circular function_}}: {{$$(y_{_{N} })_{n}=\sum _{p=-\infty }^{\infty }y_{(n-pN)}=y_{(n\operatorname {mod} N)},\quad n\in \mathbb {Z}$$}}. Then the convolution can be written as: {{$${\mathcal {F} }^{-1}\left\{X\cdot Y\right\}_{n}=\sum _{\ell =0}^{N-1}x_{\ell }\cdot y_{_{(n-\ell )\operatorname {mod} N} } \triangleq (x*y_{_{N} })_{n}$$}} which gives rise to the interpretation as {{a _circular_ convolution of $x$ and $y$}}. It is often used to {{efficiently compute their linear convolution}}. (see [circular convolution](circular%20convolution.md#example), {{[fast convolution algorithms](convolution.md#fast%20convolution%20algorithms), and [overlap-save](overlap–save%20method.md)}}) <!--SR:!2024-11-29,80,347!2025-02-07,130,327!2024-11-06,58,327!2024-10-24,50,327!2024-12-09,89,347!2024-11-26,78,347!2025-02-06,119,307-->

> [!tip] tips
>
> - intuition of the convolution theorem for [discrete-time Fourier transform](discrete-time%20Fourier%20transform.md) (DTFT) ::: The theorem says that the convolution of two signals in the time domain is the product of the two signals in the frequency domain. To understand this, imagine two signals decomposed into two linear combinations of complex sinusoids $e^{i 2\pi ft}$ with different frequencies $f$. Convolution of the two signals can also be expressed as the _sliding dot product_ of one signal and the other signal going backwards in time. That means the complex sinusoids are multiplied into terms like $A_0 A_1 \int_\infty \! e^{i 2\pi f_0 \tau} e^{i 2\pi f_1 (t - \tau)} \,\mathrm{d}\tau$. Notice said terms can be rewritten as: $$\begin{aligned} A_0 A_1 \int_\infty \! e^{i 2\pi f_0 \tau} e^{i 2\pi f_1 (t - \tau)} \,\mathrm{d}\tau & = A_0 A_1 e^{i 2\pi f_1 t} \int_\infty \! e^{i 2\pi f_0 \tau} e^{-i 2\pi f_1 \tau} \,\mathrm{d}\tau \\ & = A_0 A_1 e^{i 2\pi f_1 t} \int_\infty \! e^{i 2\pi f_0 \tau} \left(e^{i 2\pi f_1 \tau}\right)^* \,\mathrm{d}\tau \\ & = A_0 A_1 e^{i 2\pi f_1 t} \left\langle e^{i 2\pi f_0 \tau}, e^{i 2\pi f_1 \tau} \right\rangle && (\text{using the dot product that is linear in the 1st argument}) \end{aligned}$$. Intuitively (__not rigorous__), the dot product between two complex sinusoids of different frequencies ($f_0 \ne f_1$) cancels out while that of the same frequency ($f_0 = f_1$) has their amplitudes multiplied together ($A_0 A_1$; $e^{i 2\pi f_1 t}$ modifies the phase only). So the product of the two signals in the frequency domain is the DTFT of their convolution in the time domain. <!--SR:!2024-12-30,88,287!2024-10-25,48,327-->
> - intuition of the convolution theorem for discrete Fourier transform (DFT) ::: Discrete Fourier transform (DFT) makes (or requires) the signal in both the time and frequency domains discrete and periodic. The intuition for DFT is similar to that for DTFT. Simply repeat the chain of reasoning, but with periodic discrete signals in mind. Note that the above reasoning becomes mathematically rigorous for the DFT case. <!--SR:!2024-11-21,73,347!2025-05-20,214,347-->
> - reason why only one instead of both sequences is needed to be periodic to simplify DTFT operations into DFT operations ::: To simplify DTFT operations into DFT operations, both the time and frequency domain needs to be discrete and periodic. Both signals are already given to be discrete in the time domain, so their convolution is discrete, and the DTFT of their convolution is periodic. Now, consider that convolution at at particular input argument depends on the time shift (i.e. input argument) between the two signals. If one of the signal is periodic, then time shifting by a period (i.e. input argument is one period) is indistinguishable from zero time shifting (i.e. input argument is zero). So the resulting convolution is also periodic. This also means the convolution after DTFT is discrete. <!--SR:!2024-11-15,57,287!2025-03-09,152,327-->
> - reason why periodic summation preserves the convolution after windowing the summation ::: Consider convoluting two signals, with one being _P_-periodic. Convolution is performed over the entire input domain. We can split both signals into infinitely many _P_-length chunks. For the periodic signal, the chunks are all the same. Then the convolution of the two signals equals the sum of convolutions of a period of the _P_-periodic signal and each of the infinite _P_-length chunks of the other signal. By linearity, the latter equals to the convolution of a period of the _P_-periodic signal and the sum of the infinite _P_-length chunks. So we can sum up the infinite _P_-length chunks together and convert the infinite aperiodic signal into a _P_-length signal. Finally, after windowing the summation to _P_-length (instead of from negative infinity to positive infinity), the convolution is preserved. <!--SR:!2025-02-28,136,327!2024-12-05,85,347-->

### cross-correlation theorem

Similar to above, by {{applying the [circular convolution theorem](#ciruclar%20convolution%20theorem)}}, {{the [cross-correlation](cross-correlation.md) of $x$ and $y_{_{N} }$}} is given by: {{$$(x\star y_{_{N} })_{n}\triangleq \sum _{\ell =-\infty }^{\infty }x_{\ell }^{*}\cdot (y_{_{N} })_{n+\ell } = \sum_{\ell =-\infty }^{\infty} x_{-\ell }^{*} \cdot (y_{_N })_{n-\ell} = (x^*_{-n} * y_{_N })_n ={\mathcal {F} }^{-1}\left\{X^{*}\cdot Y\right\}_{n}$$}}, considering that {{the DFT of $\{x^*_{-n} \}$ is $X^*$ by [time and frequency reversal](#time%20and%20frequency%20reversal), and [conjugation in time](#conjugation%20in%20time)}}. <!--SR:!2025-01-20,104,307!2025-03-22,153,327!2024-11-06,57,327!2024-11-02,52,332-->

### uniqueness of the discrete Fourier transform

As seen above, the discrete Fourier transform has {{the fundamental property of carrying convolution into componentwise product}}. A natural question is {{whether it is the only one with this ability}}. It has been shown that {{any linear transform that turns convolution into pointwise product is the DFT up to a permutation of coefficients}}. Since {{the number of permutations of n elements equals n!}}, there exists {{exactly n! linear and invertible maps with the same fundamental property as the DFT with respect to convolution}}. <!--SR:!2024-11-07,59,332!2024-12-11,88,352!2024-11-06,55,332!2025-03-26,162,332!2024-12-05,82,352-->

### convolution theorem duality

It can also be shown that: $$\begin{aligned} \mathcal F\{\mathbf x \cdot \mathbf y \}_k & \triangleq \sum_{n = 0}^{N - 1} x_n \cdot y_n \cdot e^{-i\frac {2\pi} N kn} \\ & = \frac 1 N (\mathbf {X * Y_N})_k \end{aligned}$$, which is {{the circular convolution of $\mathbf X$ and $\mathbf Y$}}. <!--SR:!2025-01-29,106,312-->

By [expressing the inverse DFT in terms of the DFT](#expressing%20the%20inverse%20DFT%20in%20terms%20of%20the%20DFT), we can easily prove the above from the (forward) [convolution theorem](#circular%20convolution%20theorem): {{$$\begin{aligned} \mathcal F^{-1}\{\mathbf {X * Y_N} \}_k & = \frac 1 N \mathcal F\{\mathbf {X^* * Y_N^*} \}_k^* \\ & = \frac 1 N \cdot \mathcal F\{\mathbf {X^*}\}_k^* \cdot \mathcal F\{\mathbf {Y_N^*}\}_k^* \\ & = \frac 1 N \cdot N \cdot \mathcal F^{-1}\{\mathbf {X}\}_k \cdot N \cdot \mathcal F^{-1}\{\mathbf {Y_N}\}_k \\ & = N \cdot \mathbf x_k \cdot \mathbf {y_{_N} }_k \\ \frac 1 N (\mathbf {X * Y_N})_k & = \mathcal F\{\mathbf x \cdot \mathbf {y_{_N} }\}_k \end{aligned}$$}}. <!--SR:!2025-02-28,134,312-->

### expressing the inverse DFT in terms of the DFT

A useful property of the DFT is that {{the inverse DFT can be easily expressed in terms of the (forward) DFT, via several well-known "tricks"}}. (For example, in {{computations}}, it is {{often convenient to only implement a fast Fourier transform corresponding to one transform direction and then to get the other transform direction from the first}}.) <!--SR:!2024-10-31,66,310!2024-11-03,67,310!2024-11-04,68,310-->

First, we can compute the inverse DFT by {{reversing all but one of the inputs (Duhamel _et al._, 1988)}}: {{$$\mathcal F^{-1}(\set{x_n}) = \frac 1 N \mathcal F(\set{x_{N - n} })$$}}. (As usual, the subscripts are {{interpreted [modulo](modular%20arithmetic.md) _N_; thus, for $n = 0$, we have $x_{N - 0} = x_0$}}.) <!--SR:!2025-06-25,249,330!2024-12-26,95,290!2024-11-06,69,310-->

Second, one can also {{conjugate the inputs and outputs}}: {{$$\mathcal F^{-1}(\mathbf x) = \frac 1 N \mathcal F(\mathbf x^*)^*$$}}. <!--SR:!2025-04-16,178,310!2024-10-31,64,310-->

Third, {{a variant of this conjugation trick}}, which is {{sometimes preferable because it requires no modification of the data values}}, involves {{swapping real and imaginary parts (which can be done on a computer simply by modifying [pointers](pointer%20(computer%20programming).md))}}. Define {{$\operatorname {swap} (x_{n})$ as $x_{n}$ with its real and imaginary parts swapped—that is, if $x_{n}=a+bi$ then $\operatorname {swap} (x_{n})$ is $b+ai$}}. Equivalently, {{$\operatorname {swap} (x_{n})$ equals $ix_{n}^{*}$}}. Then {{$${\mathcal {F} }^{-1}(\mathbf {x} )={\frac {1}{N} }\operatorname {swap} ({\mathcal {F} }(\operatorname {swap} (\mathbf {x} )))$$}}. That is, the inverse transform is {{the same as the forward transform with the real and imaginary parts swapped for both input and output, up to a normalization (Duhamel _et al._, 1988)}}. <!--SR:!2025-05-17,214,330!2024-11-05,69,310!2025-04-10,184,310!2025-03-08,159,310!2024-10-25,58,310!2024-11-03,66,310!2024-12-13,82,270-->

The conjugation trick can also be used to {{define a new transform, closely related to the DFT, that is [involutory](involution%20(mathematics).md)—that is, which is its own inverse}}. In particular, {{$T(\mathbf {x} )={\mathcal {F} }\left(\mathbf {x} ^{*}\right)/{\sqrt {N} }$ is clearly its own inverse: $T(T(\mathbf {x} ))=\mathbf {x}$}}. A closely related involutory transformation {{(by a factor of $\frac {1+i}{\sqrt {2} }$) is $H(\mathbf {x} )={\mathcal {F} }\left((1+i)\mathbf {x} ^{*}\right)/{\sqrt {2N} }$}}, since {{the $(1+i)$ factors in $H(H(\mathbf {x} ))$ cancel the 2}}. For {{real inputs $\mathbf {x}$}}, {{the real part of $H(\mathbf {x} )$ is none other than the [discrete Hartley transform](discrete%20Hartley%20transform.md), which is also involutory}}. <!--SR:!2024-12-12,81,270!2025-02-14,129,270!2024-11-29,75,270!2025-01-31,129,310!2025-01-12,108,270!2025-01-29,106,250-->

### DFT of real and purely imaginary signals

If {{$x_{0}, \ldots, x_{N-1}$ are [real numbers](real%20number.md), as they often are in practical applications}}, then {{the DFT $X_{0}, \ldots, X_{N-1}$ is [even conjugate symmetric](even%20and%20odd%20functions.md)}}: {{$$x_{n}\in \mathbb {R} \quad \forall n\in \{0, \ldots, N-1\}\implies X_{k}=X_{-k\mod N}^{*}\quad \forall k\in \{0, \ldots, N-1\}$$}}, where {{$X^{*}$ denotes [complex conjugation](complex%20conjugate.md)}}. It follows that {{for even $N$}} {{$X_{0}$ and $X_{N/2}$ are real-valued, and the remainder of the DFT is completely specified by just $N/2-1$ complex numbers}}. Furthermore, if {{$x_{0}, \ldots, x_{N - 1}$ is _additionally_ even, i.e. $x_{0} = x_{-k \mod N}$}}, then {{the DFT $X_{0}, \ldots, X_{N-1}$ is further constrained by $X_k = X_{-k \mod N}$ by [time and frequency reversal](#time%20and%20frequency%20reversal)}}. Combined with the above property, {{the DFT have no imaginary components for all frequencies}}. <!--SR:!2024-11-28,79,347!2024-11-01,58,327!2024-12-02,68,287!2024-11-29,80,347!2025-01-24,108,307!2024-12-03,84,347!2025-02-06,129,327!2025-02-13,121,307!2025-01-14,103,307-->

If {{$x_{0}, \ldots, x_{N-1}$ are purely imaginary numbers}}, then {{the DFT $X_{0} ,\ldots, X_{N-1}$ is [odd conjugate symmetric](even%20and%20odd%20functions.md)}}: {{$$x_{n}\in i\mathbb {R} \quad \forall n\in \{0, \ldots, N-1\}\implies X_{k}=-X_{-k\mod N}^{*}\quad \forall k\in \{0, \ldots, N-1\}$$}}, where {{$X^{*}$ denotes [complex conjugation](complex%20conjugate.md)}}. {{Additional properties analogous to the previous paragraph}} also apply. <!--SR:!2024-11-03,55,327!2024-10-30,52,327!2024-11-14,64,327!2024-11-05,61,327!2024-11-02,54,327-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/discrete_Fourier_transform) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

## further reading

- P. Duhamel; B. Piron; J. M. Etcheto (1988). "On computing the inverse DFT". _IEEE Transactions on Acoustics, Speech, and Signal Processing_. __36__ (2): 285–286. [doi](digital%20object%20identifier.md):[10.1109/29.1519](https://doi.org/10.1109%2F29.1519).
