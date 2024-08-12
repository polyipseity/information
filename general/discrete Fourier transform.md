---
aliases:
  - DFT
  - discrete Fourier transform
  - discrete Fourier transforms
tags:
  - flashcard/general/discrete_Fourier_transform
  - language/in/English
---

# discrete Fourier transform

_Not to be confused with the [discrete-time Fourier transform](discrete-time%20Fourier%20transform.md)._

In [mathematics](mathematics.md), {{the __discrete Fourier transform__ (__DFT__)}} {{converts a finite sequence of equally-spaced [samples](sampling%20(signal%20processing).md) of a [function](function%20(mathematics).md) into a same-length sequence of equally-spaced samples of the [discrete-time Fourier transform](discrete-time%20Fourier%20transform.md) (DTFT)}}, which is {{a [complex-valued](complex%20number.md) function of frequency}}. The interval at which the DTFT is sampled is {{the reciprocal of the duration of the input sequence}}. {{An inverse DFT (IDFT)}} is {{a [Fourier series](fourier%20series.md), using the DTFT samples as coefficients of [complex](complex%20number.md) [sinusoids](sine%20wave.md) at the corresponding DTFT frequencies}}. It has {{the same sample-values as the original input sequence}}. The DFT is therefore said to be {{a [frequency domain](frequency%20domain.md) representation of the original input sequence}}. If {{the original sequence spans all the non-zero values of a function (i.e. the function has one copy of the original sequence and zero everywhere else)}}, its DTFT is {{continuous (and periodic), and the DFT provides discrete samples of one cycle}}. If {{the original sequence is one cycle of a periodic function}}, {{the DFT provides all the non-zero values of one DTFT cycle}}. <!--SR:!2024-08-27,15,290!2024-08-25,13,270!2024-08-24,14,290!2024-08-26,16,290!2024-08-28,16,290!2024-08-20,10,270!2024-08-22,10,270!2024-08-18,6,250!2024-08-23,11,270!2024-08-22,10,270!2024-08-24,14,290!2024-08-27,17,290-->

## definition

The _discrete Fourier transform_ transforms {{a [sequence](sequence.md) of _N_ [complex numbers](complex%20number.md) $\set{\mathbf x_n} := x_0, x_1, \ldots, x_{N−1}$ into another sequence of complex numbers, $\set{\mathbf X_k} := X_0, X_1, \ldots, X_{N−1}$, which is defined by:

> {{__discrete Fourier transform (Eq. 1)__}}
>
> {{$$X_k = \sum_{n = 0}^{N - 1} x_n \cdot e^{-i2\pi \frac k N n}$$}} <!--SR:!2024-08-26,16,290!2024-08-25,13,270-->

The transform is sometimes denoted by {{$\mathcal F$, as in $\mathbf X = \mathcal F\set{\mathbf x}$ or $\mathcal F(\mathbf x)$ or $\mathcal F \mathbf x$}}. <!--SR:!2024-08-28,16,290-->

__Eq.1__ can be {{interpreted or derived in various ways}}, for example: <!--SR:!2024-08-22,10,270-->

- discrete Fourier transform & discrete-time Fourier transform ::: It completely describes the [discrete-time Fourier transform](discrete-time%20Fourier%20transform.md) (DTFT) of an $N$-periodic sequence, which comprises only discrete frequency components. ([Using the DTFT with periodic data](discrete-time%20Fourier%20transform.md#periodic%20data)) <!--SR:!2024-08-22,12,270!2024-08-27,15,290-->
- discrete Fourier transform & sampling ::: It can also provide uniformly spaced samples of the continuous DTFT of a finite length sequence. The sampling interval is the reciprocal of the duration of the input sequence. ([§ sampling the DTFT](discrete-time%20Fourier%20transform.md#sampling%20the%20DTFT)) <!--SR:!2024-08-22,10,270!2024-08-24,14,290-->
- discrete Fourier transform & complex sinusoid ::: It is the [cross correlation](cross-correlation.md) of the _input_ sequence, $x_n$, and a complex sinusoid at frequency $k / N$ (angular frequency $2 \pi k / N$). Thus it acts like a [matched filter](matched%20filter.md) for that frequency. <!--SR:!2024-08-22,12,270!2024-08-24,12,270-->
- discrete Fourier transform & Fourier series ::: It is the discrete analog of the formula for the coefficients of a [Fourier series](fourier%20series.md): $$C_k = \frac 1 P \int_P \! x(t) e^{-i2\pi \frac k P t} \,\mathrm{d}t$$. <!--SR:!2024-08-17,7,250!2024-08-21,11,270-->

__Eq.1__ can also be evaluated {{outside the domain $k \in [0 , N - 1]$, and that extended sequence is $N$-[periodic](periodic%20sequence.md)}}. Accordingly, other sequences of $N$ indices are sometimes used, such as {{$\left[-\frac N 2,\frac N 2 - 1 \right]$ (if $N$ is even) and $\left[-\frac {N - 1} 2,\frac {N - 1} 2 \right]$ (if $N$ is odd)}}, which amounts to {{swapping the left and right halves of the result of the transform}}. <!--SR:!2024-08-25,13,270!2024-08-21,9,270!2024-08-24,12,270-->

The inverse transform is given by:

> {{__inverse discrete Fourier transform (Eq.2)__}}
>
> {{$$x_n = \frac 1 N \sum_{k = 0}^{N - 1} X_k \cdot e^{i 2\pi \frac k N n}$$}} <!--SR:!2024-08-17,7,250!2024-08-19,9,270-->

__Eq.2__ is {{also $N$-periodic (in index $n$)}}. In __Eq.2__, each $X_k$ is {{a complex number whose polar coordinates are the amplitude and phase of a complex sinusoidal component $\left(e^{i 2\pi \frac k N n}\right)$ of function $x_n$}}. (see [discrete Fourier series](discrete%20Fourier%20series.md)) The sinusoid's [frequency](frequency.md) is {{$k$ cycles per $N$ samples}}. <!--SR:!2024-08-25,15,290!2024-08-23,11,270!2024-08-27,17,290-->

{{The normalization factor multiplying the DFT and IDFT (here $1$ and $\frac 1 N$) and the signs of the exponents}} are {{the most common [conventions](sign%20convention.md)}}. The only actual requirements of these conventions are that {{the DFT and IDFT have opposite-sign exponents and that the product of their normalization factors be $\frac 1 N$}}. {{An uncommon normalization of $\sqrt{\frac 1 N}$ for both the DFT and IDFT}} makes {{the transform-pair unitary}}. <!--SR:!2024-08-25,15,290!2024-08-27,15,290!2024-08-29,17,290!2024-08-26,16,290!2024-08-24,14,290-->

## properties

### expressing the inverse DFT in terms of the DFT

A useful property of the DFT is that {{the inverse DFT can be easily expressed in terms of the (forward) DFT, via several well-known "tricks"}}. (For example, in {{computations}}, it is {{often convenient to only implement a fast Fourier transform corresponding to one transform direction and then to get the other transform direction from the first}}.) <!--SR:!2024-08-26,16,290!2024-08-27,17,290!2024-08-27,17,290-->

First, we can compute the inverse DFT by {{reversing all but one of the inputs (Duhamel _et al._, 1988)}}: {{$$\mathcal F^{-1}(\set{x_n}) = \frac 1 N \mathcal F(\set{x_{N - n} })$$}}. (As usual, the subscripts are {{interpreted [modulo](modular%20arithmetic.md) _N_; thus, for $n = 0$, we have $x_{N - 0} = x_0$}}.) <!--SR:!2024-08-24,14,290!2024-08-19,9,270!2024-08-29,17,290-->

Second, one can also {{conjugate the inputs and outputs}}: {{$$\mathcal F^{-1}(\mathbf x) = \frac 1 N \mathcal F(\mathbf x^*)^*$$}}. <!--SR:!2024-08-26,14,290!2024-08-28,16,290-->

Third, {{a variant of this conjugation trick}}, which is {{sometimes preferable because it requires no modification of the data values}}, involves {{swapping real and imaginary parts (which can be done on a computer simply by modifying [pointers](pointer%20(computer%20programming).md))}}. Define {{$\operatorname {swap} (x_{n})$ as $x_{n}$ with its real and imaginary parts swapped—that is, if $x_{n}=a+bi$ then $\operatorname {swap} (x_{n})$ is $b+ai$}}. Equivalently, {{$\operatorname {swap} (x_{n})$ equals $ix_{n}^{*}$}}. Then {{$${\mathcal {F} }^{-1}(\mathbf {x} )={\frac {1}{N} }\operatorname {swap} ({\mathcal {F} }(\operatorname {swap} (\mathbf {x} )))$$}}. That is, the inverse transform is {{the same as the forward transform with the real and imaginary parts swapped for both input and output, up to a normalization (Duhamel _et al._, 1988)}}. <!--SR:!2024-08-23,13,290!2024-08-27,17,290!2024-08-22,12,270!2024-08-22,10,270!2024-08-27,15,290!2024-08-29,17,290!2024-08-22,12,270-->

The conjugation trick can also be used to {{define a new transform, closely related to the DFT, that is [involutory](involution%20(mathematics).md)—that is, which is its own inverse}}. In particular, {{$T(\mathbf {x} )={\mathcal {F} }\left(\mathbf {x} ^{*}\right)/{\sqrt {N} }$ is clearly its own inverse: $T(T(\mathbf {x} ))=\mathbf {x} $}}. A closely related involutory transformation {{(by a factor of ${\frac {1+i}{\sqrt {2} }}$) is $H(\mathbf {x} )={\mathcal {F} }\left((1+i)\mathbf {x} ^{*}\right)/{\sqrt {2N} }$}}, since {{the $(1+i)$ factors in $H(H(\mathbf {x} ))$ cancel the 2}}. For {{real inputs $\mathbf {x} $}}, {{the real part of $H(\mathbf {x} )$ is none other than the [discrete Hartley transform](discrete%20Hartley%20transform.md), which is also involutory}}. <!--SR:!2024-08-21,11,270!2024-08-16,6,250!2024-08-18,8,250!2024-08-21,9,270!2024-08-14,4,230!2024-08-18,6,250-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/discrete_Fourier_transform) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

## further reading

- P. Duhamel; B. Piron; J. M. Etcheto (1988). "On computing the inverse DFT". _IEEE Transactions on Acoustics, Speech, and Signal Processing_. __36__ (2): 285–286. [doi](digital%20object%20identifier.md):[10.1109/29.1519](https://doi.org/10.1109%2F29.1519).
