---
aliases:
  - string vibration
  - string vibrations
  - string wave
  - string waves
tags:
  - flashcards/general/string_vibration
  - languages/in/English
---

# string vibration

## wave

### phase velocity

> __phase velocity for string vibration__
>
> {{$$\frac 1 c = v = \sqrt{\frac{T}\mu}$$}}
>
> where
> - [string](string%20(structure).md) properties: {{$T$ is [tension](tension%20(mechanics).md) and $\mu$ is [linear mass density](linear%20density.md), i.e. [mass](mass.md) per unit [length](length.md)}} <!--SR:!2024-01-05,7,250!2024-02-21,53,310-->

### power

> __power for string vibration__
>
> {{$$P(x, t) = \sqrt{\mu T} \omega^2 A^2 \cos^2(kx - \omega t + \phi)$$}}
>
> where
> - [function](function%20(mathematics).md) properties: {{$P$ is [power](power%20(physics).md) at [position](position%20(geometry).md) $x$ and [time](time.md) $t$}}
> - [string](string%20(structure).md) properties: {{$T$ is [tension](tension%20(mechanics).md) and $\mu$ is [linear mass density](linear%20density.md), i.e. [mass](mass.md) per unit [length](length.md)}}
> - [wave](wave.md) properties: {{$A$ is [amplitude](amplitude.md), $k$ is [angular wavenumber](wavenumber.md), $\omega$ is [angular frequency](angular%20frequency.md), $\phi$ is phase offset}} <!--SR:!2024-01-06,15,250!2024-02-29,58,310!2024-02-02,36,290!2024-02-09,43,290-->

#### derivation

$$\begin{aligned}
y(x, t) & = A \sin(kx - \omega t + \phi) + D \\
P(x, t) & = - T \frac{\partial y}{\partial x} \frac{\partial y}{\partial t} \\
& = T k A \cos(kx - \omega t + \phi) \omega A \cos(kx - \omega t + \phi) \\
& = T k \omega A^2 \cos^2(kx - \omega t + \phi) \\
& = T v^{-1} \omega^2 A^2 \cos^2(kx - \omega t + \phi) \\
& = \sqrt{\mu T} \omega^2 A^2 \cos^2(kx - \omega t + \phi)
\end{aligned}$$

## references

This text incorporates [content](https://en.wikipedia.org/wiki/string_vibration) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
