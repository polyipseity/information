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

The [ordinary differential equation](ordinary%20differential%20equation.md) for simple harmonic motion can be derived from {{[Newton's second law](Newton's%20laws%20of%20motion.md#second%20law) and [Hooke's law](Hooke's%20law.md)}}: <!--SR:!2024-01-05,11,309-->

> __ordinary differential equation__
>
> {{$$\begin{aligned} F_\mathrm{net} = m \frac{\mathrm{d}^2x}{\mathrm{d}t^2} & = -kx \\ \frac{\mathrm{d}^2x}{\mathrm{d}t^2} +\frac{k}m x & = 0 \end{aligned}$$}}
>
> - where
>     - [function](function%20(mathematics).md) properties: {{$F_\mathrm{net}$ is the [net force](net%20force.md), $x$ is the [displacement](displacement%20(geometry).md) from equilibrium, and $t$ is the [time](time.md)}}
>     - [oscillator](oscillation.md) properties: {{$k$ is the [spring constant](Hooke's%20law.md) and $m$ is the [mass](mass.md)}} <!--SR:!2024-01-13,19,329!2024-01-11,17,329!2024-01-12,18,329-->

For better physical meaning, it can be rewritten as:

> __ordinary differential equation, rewritten__
>
> {{$$\frac{\mathrm{d}^2x}{\mathrm{d}t^2} + \omega x = 0$$}}
>
> - where
>     - [function](function%20(mathematics).md) properties: {{$x$ is the [displacement](displacement%20(geometry).md) from equilibrium and $t$ is the [time](time.md)}}
>     - [oscillator](oscillation.md) properties: {{$\omega = \sqrt{\frac{k}m}$ is the [angular frequency](angular%20frequency.md), $k$ is the [spring constant](Hooke's%20law.md), and $m$ is the [mass](mass.md)}} <!--SR:!2024-01-12,18,329!2024-01-07,13,309!2024-01-13,19,329-->

Solving the [ordinary differential equation](ordinary%20differential%20equation.md):

$$\begin{aligned}
\frac{\mathrm{d}^2x}{\mathrm{d}t^2} + \omega^2 x & = 0 \\
r^2 + \omega^2 & = 0\\
r^2 & = -\omega^2 \\
r & = \pm\omega i \\
x(t) & = c_1 e^{\omega t i} + c_2 e^{-\omega t i} \\
& = C_1 e^0 \cos(\omega t) + C_2 e^0 \sin(\omega t) \\
& = C_1 \cos(\omega t) + C_2 \sin(\omega t) \\
v(t) & = x'(t) \\
& = -C_1 \omega \sin(\omega t) + C_2 \omega \cos(\omega t) \\
\\
x_0 & = C_1 \cos(\omega \cdot 0) + C_2 \sin(\omega \cdot 0) \\
& = C_1 \\
C_1 & = x_0 \\
v_0 & = -C_1 \omega \sin(\omega \cdot 0) + C_2 \omega \cos(\omega \cdot 0) \\
& = C_2 \omega \\
C_2 & = \frac{v_0}\omega \\
\\
x(t) & = x_0 \cos(\omega t) + \frac{v_0}\omega \sin(\omega t) \\
& = \sqrt{x_0^2 + \left(\frac{v_0}\omega\right)^2} \cos\left(\omega t + \operatorname{atan2}\left(-\frac{v_0}\omega, x_0\right)\right)
\end{aligned}$$

The solution yields the [position](position%20(geometry).md) of a simple harmonic motion as a [function](function%20(mathematics).md) of [time](time.md):

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
> - {{$\phi=\arg{c}$ is the initial [phase](phase%20(waves).md)}} <!--SR:!2024-02-14,103,310!2024-03-12,69,270!2024-04-05,112,270!2024-01-27,57,320!2024-02-08,66,320!2024-02-12,70,320!2024-01-31,60,320!2024-04-10,104,300!2024-01-29,55,300-->

> [!tip] tip
>
> - [mnemonic](mnemonic.md): {{The trajectory of simple harmonic motion over [time](time.md) in a [phase space](phase%20space.md) with [position](position%20(vector).md) $x$ as the $x$-axis and negate of [velocity](velocity.md) divided by the [angular frequency](angular%20frequency.md) $-\frac{v}\omega$ as the $y$-axis is a [circle](circle.md). The circular trajectory is uniquely defined by its [radius](radius.md), which is [amplitude](amplitude.md) $A=\sqrt{x_0^2+\left(\frac{v_0^2}\omega\right)^2}$, and its [angular frequency](angular%20frequency.md) $\omega=\sqrt{\frac{k}m}$. The initial phase can be found by finding the initial position of the system in the [phase space](phase%20space.md).}} <!--SR:!2024-01-31,40,273-->

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
> - {{$\phi=\arg{c}$ is the initial [phase](phase%20(waves).md)}} <!--SR:!2024-01-04,14,316!2024-01-08,18,316!2024-01-07,17,316!2024-02-21,50,316!2024-01-07,17,316!2024-01-06,16,316!2024-01-07,17,316-->

For [kinetic energy](kinetic%20energy.md) $K$ at [time](time.md) $t$:

$$\begin{aligned}
K(t) & = \frac12 m v^2 \\
& = \frac12 k \omega^{-2} (-\omega A \sin(\omega t + \phi))^2 \\
& = \frac12 k A^2 \sin^2(\omega t + \phi)
\end{aligned}$$

For [potential energy](potential%20energy.md) $U$ at [time](time.md) $t$:

$$\begin{aligned}
U(t) & = \frac12 k x^2 \\
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
>     - output properties: {{$\vec{F}$ is the [force](force.md), $\omega$ is the [angular velocity](angular%20velocity.md), and $T$ is the period}}
>     - [spring](spring%20(device).md) properties: {{$m$ is the [mass](mass.md), $g$ is the [gravitational acceleration](gravitational%20acceleration.md), and $k$ is the [spring constant](Hooke's%20law.md)}} <!--SR:!2024-01-11,16,276!2024-01-05,15,316-->

### mass of a simple pendulum

> __mass of a simple pendulum for small angles__
>
> {{$$\begin{aligned} \vec{\tau} & = -mgl \hat{n} \sin \theta \approx -mgl \theta \hat{n} \\ \omega_\mathrm{approx} & = \sqrt{\frac {mgl} {ml^2} } = \sqrt{\frac g l} \\ T_\mathrm{approx} & = 2\pi \sqrt{\frac l g} \end{aligned}$$}}
>
> - where
>     - output properties: {{$\vec{\tau}$ is the [torque](torque.md), $\omega_\mathrm{approx}$ is the approximate [angular velocity](angular%20velocity.md), and $T_\mathrm{approx}$ is the approximate period}}
>     - [pendulum](pendulum.md) properties: {{$m$ is the [mass](mass.md), $g$ is the [gravitational acceleration](gravitational%20acceleration.md), and $l$ is the pendulum length}} <!--SR:!2024-01-08,6,276!2024-01-08,18,316-->
>     - intermediate variables: {{$\hat{n}$ is the [unit vector](unit%20vector.md) of $\vec{\tau}$ and $\theta$ is the pendulum angle from equilibrium}}

### mass of a physical pendulum

> __mass of a physical pendulum for small angles__
>
> {{$$\begin{aligned} \vec{\tau} & = -mgl \hat{n} \sin \theta \approx -mgl \theta \hat{n} \\ \omega_\mathrm{approx} & = \sqrt{\frac {mgl} I} \\ T_\mathrm{approx} & = 2\pi \sqrt{\frac I {mgl} } \end{aligned}$$}}
>
> - where
>     - output properties: {{$\vec{\tau}$ is the [torque](torque.md), $\omega_\mathrm{approx}$ is the approximate [angular velocity](angular%20velocity.md), and $T_\mathrm{approx}$ is the approximate period}}
>     - [pendulum](pendulum.md) properties: {{$m$ is the [mass](mass.md), $l$ is the pendulum length, $I$ is the [moment of inertia](moment%20of%20inertia.md) of the pendulum including the load}} <!--SR:!2024-01-10,15,276!2024-02-22,50,316-->
>     - intermediate variables: {{$\hat{n}$ is the [unit vector](unit%20vector.md) of $\vec{\tau}$ and $\theta$ is the pendulum angle from equilibrium}}

## references

This text incorporates [content](https://en.wikipedia.org/wiki/simple_harmonic_motion) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
