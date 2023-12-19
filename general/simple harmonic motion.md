---
aliases:
  - SHM
  - simple harmonic motion
tags:
  - flashcards/general/simple_harmonic_motion
  - languages/in/English
---

# simple harmonic motion

## dynamics

The position of a simple harmonic motion as a function of time can be written as:

> {{__position as a function of time__}}
>
> 1. {{$x(t)=x_0\cos(\omega{}t)+\frac{v_0}\omega\sin(\omega{}t)$}}
> 2. {{$x(t)=A\cos(\omega{t}+\phi)$}}
>
> where
> - {{$k$ is the [spring constant](Hooke's%20law.md)}}
> - {{$m$ is the object [mass](mass.md)}}
> - {{$\omega=\sqrt{\frac{k}m}$ is the [angular frequency](angular%20frequency.md)}}
> - {{$c=x_0-\frac{v_0}\omega{}i$ is the initial [phase space](phase%20space.md) position}}
> - {{$A=|c|$ is the [amplitude](amplitude.md)}}
> - {{$\phi=\arg{c}$ is the initial [phase](phase%20(waves).md)}} <!--SR:!2024-02-14,103,310!2024-01-03,20,250!2024-04-05,112,270!2024-01-27,57,320!2024-02-08,66,320!2024-02-12,70,320!2024-01-31,60,320!2023-12-28,27,280!2024-01-29,55,300-->

> [!tip]
>
> - [mnemonic](mnemonic.md): {{The trajectory of simple harmonic motion over [time](time.md) in a [phase space](phase%20space.md) with [position](position%20(vector).md) $x$ as the $x$-axis and negate of [velocity](velocity.md) divided by the [angular frequency](angular%20frequency.md) $-\frac{v}\omega$ as the $y$-axis is a [circle](circle.md). The circular trajectory is uniquely defined by its [radius](radius.md), which is [amplitude](amplitude.md) $A=\sqrt{x_0^2+\left(\frac{v_0^2}\omega\right)^2}$, and its [angular frequency](angular%20frequency.md) $\omega=\sqrt{\frac{k}m}$. The initial phase can be found by finding the position of the system in the [phase space](phase%20space.md) initially.}} <!--SR:!2023-12-22,15,273-->

## energy

> __kinetic energy, potential energy, and mechanical energy energy__
>
> {{$$\begin{aligned} K(t) & = \frac12 k A^2 \sin^2(\omega t + \phi) \\ U(t) & = \frac12 k A^2 \cos^2(\omega t + \phi) \\ E = K + U & = \frac12 k A^2 \end{aligned}$$}}
>
> where
> - {{$k$ is the spring constant}}
> - {{$m$ is the object [mass](mass.md)}}
> - {{$\omega=\sqrt{\frac{k}m}$ is the [angular frequency](angular%20frequency.md)}}
> - {{$c=x_0-\frac{v_0}\omega{}i$ is the initial [phase space](phase%20space.md) position}}
> - {{$A=|c|$ is the [amplitude](amplitude.md)}}
> - {{$\phi=\arg{c}$ is the initial [phase](phase%20(waves).md)}} <!--SR:!2023-12-21,4,296!2023-12-21,4,296!2023-12-21,4,296!2023-12-21,4,296!2023-12-21,4,296!2023-12-21,4,296!2023-12-21,4,296-->

For [kinetic energy](kinetic%20energy.md) $K$ at [time](time.md) $t$:

$$\begin{aligned}
K & = \frac12 m v^2 \\
& = \frac12 k \omega^{-2} (-\omega A \sin(\omega t + \phi))^2 \\
& = \frac12 k A^2 \sin^2(\omega t + \phi)
\end{aligned}$$

For [potential energy](potential%20energy.md) $U$ at [time](time.md) $t$:

$$\begin{aligned}
U & = \frac12 k x^2 \\
& = \frac12 k (A \cos(\omega t + \phi))^2 \\
& = \frac12 k A^2 \cos^2(\omega t + \phi)
\end{aligned}$$

Without energy loss, the [mechanical energy](mechanical%20energy.md) $E$ is constant:

$$\begin{aligned}
E & = K + U \\
& = \frac12 k A^2 \sin^2(\omega t + \phi) + \frac12 k A^2 \cos^2(\omega t + \phi) \\
& = \frac12 k A^2 \left(\sin^2(\omega t + \phi) + \cos^2(\omega t + \phi)\right) \\
& = \frac12 k A^2
\end{aligned}$$

## examples

### mass on a string

> __mass on a string__
>
> {{$$\begin{aligned} \vec{F} & = -k \vec{x} \\ \omega & = \sqrt{\frac k m} \\ T & = 2\pi \sqrt{\frac m k} \end{aligned}$$}}
>
> - where
>     - {{[string](string%20(structure).md) properties: $k$ is the [spring constant](Hooke's%20law.md)}} <!--SR:!2023-12-20,3,276!2023-12-21,4,296-->

### mass of a simple pendulum

> __mass of a simple pendulum for small angles__
>
> {{$$\begin{aligned} \vec{\tau} & = -mgl \hat{n} \sin \theta \approx -mgl \theta \hat{n} \\ \omega_\mathrm{approx} & = \sqrt{\frac {mgl} {ml^2} } = \sqrt{\frac g l} \\ T_\mathrm{approx} & = 2\pi \sqrt{\frac l g} \end{aligned}$$}}
>
> - where
>     - {{[pendulum](pendulum.md) properties: $l$ is the pendulum length}} <!--SR:!2023-12-21,4,296!2023-12-21,4,296-->

### mass of a physical pendulum

> __mass of a physical pendulum for small angles__
>
> {{$$\begin{aligned} \vec{\tau} & = -mgl \hat{n} \sin \theta \approx -mgl \theta \hat{n} \\ \omega_\mathrm{approx} & = \sqrt{\frac {mgl} I} \\ T_\mathrm{approx} & = 2\pi \sqrt{\frac I {mgl} } \end{aligned}$$}}
>
> - where
>     - {{[pendulum](pendulum.md) properties: $l$ is the pendulum length, $I$ is the [moment of inertia](moment%20of%20inertia.md) of the pendulum including the load}} <!--SR:!2023-12-20,3,276!2023-12-21,4,296-->
