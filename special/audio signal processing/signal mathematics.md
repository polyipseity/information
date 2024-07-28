---
aliases:
  - signal math
  - signal maths
  - signal mathematic
  - signal mathematics
tags:
  - flashcard/special/audio_signal_processing/signal_mathematics
  - language/in/English
---

# signal mathematics

## sine wave

- see: [general/sine wave](../../general/sine%20wave.md)

{{A continuous [sine wave](../../general/sine%20wave.md)}} (cosine in the below equation) in its most general form has the equation: <!--SR:!2024-08-09,13,290-->

> __continuous (co)sine wave__
>
> {{$$f(x, t) = A \cos(kx \pm \omega t + \phi) + D$$}}
>
> - where
>   - $f(x, t)$ is {{displacement at position $x$ and time $t$}}.
>   - $A$ is {{amplitude, i.e. maximum displacement}}.
>   - $k$ is {{angular wavenumber or angular spatial frequency}}.
>   - $\omega$ is {{angular frequency, which equals 2 pi times normal (linear) frequency $\omega = 2\pi f$}}.
>   - $\phi$ is {{initial phase offset}}.
>   - $D$ is {{equilibrium offset}}. <!--SR:!2024-08-08,12,270!2024-08-09,13,290!2024-08-11,15,290!2024-08-12,16,290!2024-08-09,13,290!2024-08-10,14,290!2024-08-12,16,290-->

In signal processing, apart from analog signals (continuous signals), we also deal with {{digital signals (discrete signals)}}. In that case, usually {{the time is discretized}}. So the equation becomes: <!--SR:!2024-08-11,15,290!2024-08-12,16,290-->

> __discrete (co)sine wave__
>
> {{$$f(x)[n] = A \cos(kx \pm \omega T n + \phi) + D$$}} <!-- markdownlint-disable-line MD011 -->
>
> - where
>   - $f(x)[n]$ is {{displacement at position $x$ and sample (discrete time step) $n$}}. <!-- markdownlint-disable-line MD011 -->
>   - $T$ is {{sampling interval, which equals the reciprocal of sampling frequency $T = 1 / f_s$}}.
>   - $A$ is {{amplitude, i.e. maximum displacement}}.
>   - $k$ is {{angular wavenumber or angular spatial frequency}}.
>   - $\omega$ is {{angular frequency, which equals 2 pi times normal (linear) frequency $\omega = 2\pi f$}}.
>   - $\phi$ is {{initial phase offset}}.
>   - $D$ is {{equilibrium offset}}. <!--SR:!2024-08-10,14,290!2024-08-13,17,290!2024-08-13,17,290!2024-08-09,13,290!2024-08-13,17,290!2024-08-10,14,290!2024-08-09,13,290!2024-08-08,12,270-->

For the two equations above, we will ignore {{the $kx$ term and the $\pm$ operator as we care about time more}}. <!--SR:!2024-08-13,17,290-->

To generate a discrete cosine wave using Numpy, make use of {{the above equations, `np.arange`, and `np.cos`}}: <!--SR:!2024-08-13,17,290-->

```Python
import numpy as np
(A, w, phi, D), (start, end, T) = (0.8, 2, 0, 0), (-1, 1, 0.001)
wave = A * np.cos(w * T * np.arange(start, end, T) + phi) + D
```

## complex number

- see: [general/complex number](../../general/complex%20number.md)

Note that the [complex number](../../general/complex%20number.md) described here is {{colloquial, and not necessarily mathematically rigorous}}. <!--SR:!2024-08-11,15,290-->

The numbers (with decimals) we are familiar are {{the _real numbers_}}. Now, we extend it by {{defining the _imaginary unit_ $j = \sqrt{-1}$ ($j$ is more commonly used than $i$ in electrical engineering)}}. Then the _complex numbers_ are {{all numbers in the form of $a + bj$, where $a$ and $b$ are real numbers}}. Visually, we can think of each complex number as {{a point on a 2D plane, with the x-coordinate being the _real part_ ($x = \operatorname{Re}(a + bj) = a$) and the y-coordinate being the _imaginary part_ ($y = \operatorname{Im}(a + bj) = b$)}}. <!--SR:!2024-08-12,16,290!2024-08-12,16,290!2024-08-10,14,290!2024-08-10,14,290-->

With the point on a 2D plane visualization in mind, we call the $a + bj$ form {{the _rectangular form_, because the coordinates specify a rectangle from the origin to the 2D point}}. An alternative form is {{the _polar form_ $(A, \phi)$, where $A$ is the distance from the origin to the 2D point and $\phi$ is the angle formed with the right direction, increasing counterclockwise}}. <!--SR:!2024-08-11,15,290!2024-08-13,17,290-->

We can {{convert}} in between rectangular form and polar form. From rectangular form to polar form: {{$$(A, \phi) = \left( \sqrt{a^2 + b^2}, \operatorname{atan2}\left(b, a\right) \right)$$}}, where [`atan2`](../../general/atan2.md) produces the angle formed with the right direction, constrained between {{$(-\pi, \pi]$}}, and is defined as: {{$$\operatorname{atan2}(y, x) = \begin{cases} \arctan\left(\frac y x \right) & \text{if }x > 0 \\ \arctan\left(\frac y x \right) - \pi & \text{if }x < 0 \\ \text{(omitted, use intuition)} & \text{otherwise} \end{cases}$$}}. From polar form to rectangular form: {{$$a + bj = A \cos \phi + j A \sin \phi$$}}. <!--SR:!2024-08-11,15,290!2024-08-10,14,290!2024-08-11,15,290!2024-07-30,2,210!2024-08-09,13,290-->

## Euler's formula

- see: [general/Euler's%20formula](../../general/Euler's%20formula.md)

[Euler's formula](../../general/Euler's%20formula.md) is: {{$$e^{j\varphi} = \cos x + j \sin \varphi$$, where $\varphi$ is a [complex number](#complex%20number)}}. The above implies alternative formulas for {{$\sin$ and $\cos$}}: {{$$\begin{aligned} \cos \varphi & = \frac {e^{j\varphi} + e^{-j\varphi} } 2 \\ \sin \varphi & = \frac {e^{j\varphi} - e^{-j\varphi} } {2j} \end{aligned}$$}}. <!--SR:!2024-08-12,16,290!2024-08-11,15,290!2024-08-08,12,270-->
