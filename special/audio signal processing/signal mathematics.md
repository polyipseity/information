---
aliases:
  - signal math
  - signal maths
  - signal mathematic
  - signal mathematics
tags:
  - flashcard/active/special/audio_signal_processing/signal_mathematics
  - language/in/English
---

# signal mathematics

## sine wave

- see: [general/sine wave](../../general/sine%20wave.md)

{@{A continuous [sine wave](../../general/sine%20wave.md)}@} (cosine in the below equation) in its most general form has the equation: <!--SR:!2025-05-09,218,330-->

> __continuous (co)sine wave__
>
> {@{$$f(x, t) = A \cos(kx \pm \omega t + \phi) + D$$}@}
>
> - where
>   - $f(x, t)$ is {@{displacement at position $x$ and time $t$}@}.
>   - $A$ is {@{amplitude, i.e. maximum displacement}@}.
>   - $k$ is {@{angular wavenumber or angular spatial frequency}@}.
>   - $\omega$ is {@{angular frequency, which equals 2 pi times normal (linear) frequency $\omega = 2\pi f$}@}.
>   - $\phi$ is {@{initial phase offset}@}.
>   - $D$ is {@{equilibrium offset}@}. <!--SR:!2026-02-15,381,290!2025-05-13,222,330!2025-07-01,264,330!2025-07-31,287,330!2025-05-24,228,330!2025-05-30,234,330!2025-07-31,287,330-->

In signal processing, apart from analog signals (continuous signals), we also deal with {@{digital signals (discrete signals)}@}. In that case, usually {@{the time is discretized}@}. So the equation becomes: <!--SR:!2025-06-16,251,330!2025-07-31,287,330-->

> __discrete (co)sine wave__
>
> {@{$$f(x)[n] = A \cos(kx \pm \omega T n + \phi) + D$$}@} <!-- markdownlint-disable-line MD011 -->
>
> - where
>   - $f(x)[n]$ is {@{displacement at position $x$ and sample (discrete time step) $n$}@}. <!-- markdownlint-disable-line MD011 -->
>   - $T$ is {@{sampling interval, which equals the reciprocal of sampling frequency $T = 1 / f_s$}@}.
>   - $A$ is {@{amplitude, i.e. maximum displacement}@}.
>   - $k$ is {@{angular wavenumber or angular spatial frequency}@}.
>   - $\omega$ is {@{angular frequency, which equals 2 pi times normal (linear) frequency $\omega = 2\pi f$}@}.
>   - $\phi$ is {@{initial phase offset}@}.
>   - $D$ is {@{equilibrium offset}@}. <!--SR:!2026-07-29,498,310!2025-05-24,215,310!2025-05-11,204,310!2025-06-01,236,330!2025-08-17,301,330!2025-05-12,221,330!2025-05-23,227,330!2027-04-01,746,330-->

For the two equations above, we will ignore {@{the $kx$ term and the $\pm$ operator as we care about time more}@}. <!--SR:!2025-08-17,301,330-->

To generate a discrete cosine wave using Numpy, make use of {@{the above equations, `np.arange`, and `np.cos`}@}: <!--SR:!2025-09-19,328,330-->

```Python
import numpy as np
(A, w, phi, D), (start, end, T) = (0.8, 2, 0, 0), (-1, 1, 0.001)
wave = A * np.cos(w * T * np.arange(start, end, T) + phi) + D
```

## complex number

- see: [general/complex number](../../general/complex%20number.md)

Note that the [complex number](../../general/complex%20number.md) described here is {@{colloquial, and not necessarily mathematically rigorous}@}. <!--SR:!2025-06-04,237,330-->

The numbers (with decimals) we are familiar are {@{the _real numbers_}@}. Now, we extend it by {@{defining the _imaginary unit_ $j = \sqrt{-1}$ ($j$ is more commonly used than $i$ in electrical engineering)}@}. Then the _complex numbers_ are {@{all numbers in the form of $a + bj$, where $a$ and $b$ are real numbers}@}. Visually, we can think of each complex number as {@{a point on a 2D plane, with the x-coordinate being the _real part_ ($x = \operatorname{Re}(a + bj) = a$) and the y-coordinate being the _imaginary part_ ($y = \operatorname{Im}(a + bj) = b$)}@}. <!--SR:!2025-08-12,298,330!2025-07-31,287,330!2025-06-02,237,330!2025-05-27,231,330-->

With the point on a 2D plane visualization in mind, we call the $a + bj$ form {@{the _rectangular form_, because the coordinates specify a rectangle from the origin to the 2D point}@}. An alternative form is {@{the _polar form_ $(A, \phi)$, where $A$ is the distance from the origin to the 2D point and $\phi$ is the angle formed with the right direction, increasing counterclockwise}@}. <!--SR:!2025-06-20,253,330!2025-05-24,215,310-->

We can {@{convert}@} in between rectangular form and polar form. From rectangular form to polar form: {@{$$(A, \phi) = \left( \sqrt{a^2 + b^2}, \operatorname{atan2}\left(b, a\right) \right)$$}@}, where [`atan2`](../../general/atan2.md) produces the angle formed with the right direction, constrained between {@{$(-\pi, \pi]$}@}, and is defined as: {@{$$\operatorname{atan2}(y, x) = \begin{cases} \arctan\left(\frac y x \right) & \text{if }x > 0 \\ \arctan\left(\frac y x \right) + \pi & \text{if }x < 0\text{ and }y \ge 0 \\ \arctan\left(\frac y x \right) - \pi & \text{if }x < 0\text{ and }y < 0 \\ \text{(3 special values omitted; use intuition)} & \text{otherwise} \end{cases}$$}@}. From polar form to rectangular form: {@{$$a + bj = A \cos \phi + j A \sin \phi$$}@}. <!--SR:!2025-06-07,240,330!2026-10-04,550,310!2025-06-04,239,330!2025-04-21,139,210!2025-05-11,220,330-->

## Euler's formula

- see: [general/Euler's formula](../../general/Euler's%20formula.md)

[Euler's formula](../../general/Euler's%20formula.md) is: {@{$$e^{j\varphi} = \cos \varphi + j \sin \varphi$$, where $\varphi$ is a [complex number](#complex%20number)}@}. The above implies alternative formulas for {@{$\sin$ and $\cos$}@}: {@{$$\begin{aligned} \cos \varphi & = \frac {e^{j\varphi} + e^{-j\varphi} } 2 \\ \sin \varphi & = \frac {e^{j\varphi} - e^{-j\varphi} } {2j} \end{aligned}$$}@}. <!--SR:!2025-08-12,298,330!2025-04-29,194,310!2027-07-30,841,330-->

Using Euler's formula, we can express waves {@{using exponentiation instead}@}. For example, the discrete sine wave {@{$$f(x) [n] = A \cos(kx \pm \omega T n + \phi) + D$$}@} can also be expressed as {@{$$f(x) [n] = \operatorname{Re}\left(A e^{j(kx \pm \omega Tn + \phi)}\right) + D = \operatorname{Re}\left(A e^{j \phi} e^{j(kx \pm \omega Tn)}\right) + D = \operatorname{Re}\left(X e^{j(kx \pm \omega Tn)} \right) + D \qquad X := A e^{j \phi}$$}@}. The latter expression has the advantage that {@{exponentiation is much easier to manipulate than trigonometric functions}@}. <!--SR:!2026-01-09,409,361!2025-05-28,223,341!2025-04-13,172,321!2025-12-16,389,361-->

## dot product

- see: [general/dot product § complex vectors](../../general/dot%20product.md#complex%20vectors)

The __dot product__ or __scalar product__ of two sequences $x$ and $y$ is defined as: {@{$$\langle x, y \rangle = \sum_{n = 0}^{N - 1} x[n] y^*[n]$$ (the variant that is linear in the 1st argument)}@}. Geometrically, two sequences are {@{orthogonal iff their dot product is $0$, i.e. $\langle x, y \rangle = 0$}@}. <!--SR:!2025-07-27,272,341!2025-12-17,390,361-->

## even and odd sequences

- see: [general/even and odd functions](../../general/even%20and%20odd%20functions.md)

A sequence is {@{even or symmetric}@} iff {@{$f[-n] = f[n]$}@}. A sequence is {@{odd or antisymmetric}@} iff {@{$f[-n] = -f[n]$}@}. <!--SR:!2025-09-20,320,361!2025-12-11,385,361!2026-01-04,405,361!2025-11-07,359,361-->

## convolution

- see: [general/convolution](../../general/convolution.md)

The convolution of 2 sequences $x$ and $y$ is denoted {@{$x[n] * y[n]$ or $x * y$}@}. It is defined as {@{$$(x * y) [n] = \sum_{m = 0}^{N - 1} x[m] y[n - m]$$}@}. <!--SR:!2025-08-26,295,341!2025-08-01,276,341-->

It can be visualized as follows. Take 2 sequences $x$ and $y$. Then, {@{reflect the 2nd argument $y$ across $0$, i.e. $$y'[n] = y[-n]$$}@}. Then the convolution $x * y$ {@{at argument $n = 0$ is the dot product of $x$ and $y'$ ($y$ reflected), i.e. $$(x * y) [0] = \sum_{m = 0}^{N - 1} x[m] y'[m] = \sum_{m = 0}^{N - 1} x[m] y[-m]$$}@}. When the argument $n$ is not $0$, then {@{the argument specifies how much $y'$ is shifted, with positive values shifting to the right, i.e. $$y'_n[m] = y'[m - n] = y[n - m]$$}@}. Then the convolution $x * y$ {@{at nonzero argument is the dot product of $x$ and $y'_n$ ($y$ reflected and shifted by $n$), i.e. $$(x * y) [n] = \sum_{m = 0}^{N - 1} x[m] y'_n[m] = \sum_{m = 0}^{N - 1} x[m] y'[m - n] = \sum_{m = 0}^{N - 1} x[m] y[n - m]$$}@}. <!--SR:!2025-11-23,371,361!2026-01-13,412,361!2025-10-03,331,361!2025-10-07,333,361-->
