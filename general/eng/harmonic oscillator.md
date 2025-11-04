---
aliases:
  - harmonic oscillator
  - harmonic oscillators
tags:
  - flashcard/active/general/eng/harmonic_oscillator
  - language/in/English
---

# harmonic oscillator

## simple harmonic oscillator

- see: [simple harmonic motion](simple%20harmonic%20motion.md)

## damped harmonic oscillator

- see: [damping](damping.md)

## driven, damped harmonic oscillator

The [ordinary differential equation](ordinary%20differential%20equation.md) for a driven harmonic oscillator with an externally applied force $F(t)$ can be derived from {@{[Newton's second law](Newton's%20laws%20of%20motion.md#second%20law), [Hooke's law](Hooke's%20law.md), and a _viscous [damping](damping.md) coefficient_}@}: <!--SR:!2027-05-20,889,332-->

> __ordinary differential equation__
>
> {@{$$\begin{aligned} F_\mathrm{net} = m\frac{\mathrm{d}^2x}{\mathrm{d}t^2} & = F(t) -k x - c \frac{\mathrm{d}x}{\mathrm{d}t} \\ \frac{\mathrm{d}^2x}{\mathrm{d}t^2} + \frac{c}m \frac{\mathrm{d}x}{\mathrm{d}t} + \frac{k}m x & = \frac{F(t)}m \end{aligned}$$}@}
>
> - where
>   - [function](function%20(mathematics).md) properties: {@{$F_\mathrm{net}$ is the [net force](net%20force.md), $x$ is the [displacement](displacement%20(geometry).md) from equilibrium, and $t$ is the [time](time.md)}@}
>   - [oscillator](oscillation.md) properties: {@{$k$ is the [spring constant](Hooke's%20law.md) and $m$ is the [mass](mass.md), $c$ is the _viscous damping coefficient_, and $F(t)$ is the driving [force](force.md)}@} <!--SR:!2025-11-28,489,312!2027-10-28,1092,352!2027-02-17,855,332-->

For better physical meaning, it can be rewritten as:

> __ordinary differential equation, rewritten__
>
> {@{$$\frac{\mathrm{d}^2x}{\mathrm{d}t^2} + 2 \zeta \omega_n \frac{\mathrm{d}x}{\mathrm{d}t} + \omega_n^2 x = \frac{F(t)}m$$}@}
>
> - where
>   - [function](function%20(mathematics).md) properties: {@{$x$ is the [displacement](displacement%20(geometry).md) from equilibrium and $t$ is the [time](time.md)}@}
>   - [oscillator](oscillation.md) properties: {@{$\omega_n = \sqrt{\frac{k}m}$ is the natural (undamped) [angular frequency](angular%20frequency.md), $\zeta = \frac{c}{2\sqrt{km} }$ is the _damping ratio_, $k$ is the [spring constant](Hooke's%20law.md), $m$ is the [mass](mass.md), $c$ is the _viscous damping coefficient_, and $F(t)$ is the driving [force](force.md)}@} <!--SR:!2026-05-25,604,312!2027-05-18,960,352!2028-06-23,1108,270-->

The above [inhomogeneous ordinary differential equation](ordinary%20differential%20equation.md#^nonhomogeneous) can always {@{be solved exactly for any driving [force](force.md), usually by first solving the homogeneous counterpart of the above equation}@}. <!--SR:!2026-03-29,561,312-->

### step input

- see: [step response](step%20response.md)

Consider a system {@{with $\zeta < 1$, [initial values](initial%20value%20problem.md) $x(0) = x'(0) = 0$, and the following driving [force](force.md): $$\frac{F(t)}m = \begin{cases} \omega_n^2 x_F & t \ge 0 \\ 0 & t < 0 \end{cases}$$}@}. Physically, we expect {@{the system to oscillate around the new equilibrium with decaying [amplitude](amplitude.md)}@}. Solve the equation: <!--SR:!2026-02-04,131,170!2026-09-21,713,332-->

> [!info]- details
>
> $$\begin{aligned}
> x_c''(t) + 2 \zeta \omega_n x_c'(t) + \omega_n^2 x_c(t) & = 0 \\
> x_c(t) & = Ae^{-\lambda t} \cos(\omega t + \varphi) && (\text{by memorization}) \\
> x''(t) + 2 \zeta \omega_n x'(t) + \omega_n^2 x(t) & = \omega_n^2 x_F && (t \ge 0) \\
> x_p(t) & = x_F && (\text{by inspection}) \\
> x(t) & = x_p(t) + x_c(t) \\
> & = x_F + A e^{-\lambda t} \cos(\omega t + \varphi) \\
> v(t) & = -\lambda A e^{-\lambda t} \cos(\omega t + \varphi) - \omega A e^{-\lambda t} \sin(\omega t + \varphi) \\
> \\
> x(0) & = x_F + Ae^{-\lambda \cdot 0} \cos(\omega \cdot 0 + \varphi) \\
> A & = -\frac{x_F}{\cos \varphi} \\
> v(0) & = -\lambda A e^{-\lambda \cdot 0} \cos(\omega \cdot 0 + \varphi) - \omega A e^{-\lambda \cdot 0} \sin(\omega \cdot 0 + \varphi) \\
> 0 & = \lambda \cos \varphi + \omega \sin \varphi \\
> \tan \varphi & = -\frac \lambda \omega \\
> & = -\frac{\omega_n \zeta}{\omega_n \sqrt{1 - \zeta^2} } \\
> & = -\frac{\zeta}{\sqrt{1 - \zeta^2} } \\
> \sin \varphi & = -\zeta && (\text{by constructing a triangle}) \\
> \varphi & = -\arcsin \zeta && (\text{consider }\operatorname{sgn} (\tan \varphi) = -\operatorname{sgn} \zeta) \\
> \\
> x(t) & = x_F \left(1 - e^{-\lambda t} \frac{\cos(\omega t + \varphi)}{\cos \varphi} \right)
> \end{aligned}$$

The solution is as below, which matches with our physical intuition:

> __driven, damped harmonic oscillator with step input__
>
> {@{$$x(t) = x_F \left(1 - e^{-\lambda t}\frac{\cos(\omega t + \varphi)}{\cos \varphi} \right)$$}@}
>
> - conditions: {@{$\lvert\zeta\rvert < 1, x(0) = x'(0) = 0$}@}
> - where
>   - [spring](spring%20(device).md) properties: {@{$k$ is the [spring constant](Hooke's%20law.md), $m$ is the [mass](mass.md), and $c$ is the vicious damping coefficient}@}
>   - derived properties: {@{$\omega_n = \sqrt{\frac{k}m}$ is the natural (undamped) [angular frequency](angular%20frequency.md), $\zeta = \frac{c}{2\sqrt{km} }$ is the damping ratio, $\omega = \omega_n\sqrt{1 - \zeta^2}$ is the [angular frequency](angular%20frequency.md), and $\lambda = \omega_n \zeta$ is the decay rate}@}
>   - [phase space](phase%20space.md): {@{$x_F = \frac{F(t)}{m \omega_n^2} = \frac{F(t)}k$ is steady-state equilibrium position with the driving [force](force.md) $F(t)$ and $\varphi = -\arcsin \zeta$ is the initial [phase](phase%20(waves).md)}@}
> - sine variant: {@{all $\cos$ in the main expression are replaced by $\sin$ and $\varphi = \arccos \zeta$}@} <!--SR:!2025-12-28,227,212!2027-05-10,884,312!2028-07-14,1290,352!2026-01-11,470,272!2026-03-13,284,232!2027-01-02,828,332-->

<!-- markdownlint MD028 -->

> [!tip] tips
>
> - why $\cos(\omega t + \varphi)$ increases (for negative $\zeta$, decreases) initially ::@:: One may note that initially, $\cos(\omega t + \varphi)$ increases (decreases) while $e^{-\lambda t}$ decreases (increases). These effects cancel out to give a [derivative](derivative.md) of 0 at $t = 0$, matching the given initial values. <!--SR:!2027-08-10,1026,356!2027-10-10,951,348-->

### sinusoidal driving force

Consider a system with {@{a sinusoidal driving [force](force.md) with max force $F_\mathrm{max}$ and [angular frequency](angular%20frequency.md) $\omega_d$: $$F(t) = F_\mathrm{max}\cos(\omega_d t)$$}@}. Solve the equation using the [exponential response formula](exponential%20response%20formula.md): <!--SR:!2026-04-09,531,272-->

> [!info]- details
>
> $$\begin{aligned}
> & \begin{aligned} x''(t) + 2 \zeta \omega_n x'(t) + \omega_n^2 x(t) & = \frac{F_\mathrm{max} }m \cos(\omega_d t) \\
> & = \frac{F_\mathrm{max} }m \left(\cos(\omega_d t) + i \sin(\omega_d t)\right) && (\text{add a temporary imaginary part}) \\
> & = \frac{F_\mathrm{max} }m e^{i \omega_d t} \\
> -\omega_d^2 Ae^{i (\omega_d t + \varphi)} + 2 i \zeta \omega_n \omega_d A e^{i (\omega_d t + \varphi)} + \omega_n^2 A e^{i (\omega_d t + \varphi)} & = \frac{F_\mathrm{max} }m e^{i \omega_d t} && (\text{assume }x(t) = A e^{i (\omega_d t + \varphi)}) \\
> -\omega_d^2 A + 2 i \zeta \omega_n \omega_d A + \omega_n^2 A & = \frac{F_\mathrm{max} }m e^{-i \varphi} \\
> \left(\omega_n^2 - \omega_d^2\right)A + 2i \zeta \omega_n \omega_d A & = \frac{F_\mathrm{max} }m (\cos \varphi - i \sin \varphi) \end{aligned} \\
> & \begin{cases} \left(\omega_n^2 - \omega_d^2\right)A & = \frac{F_\mathrm{max} }m \cos \varphi \\
> 2 \zeta \omega_n \omega_d A & = -\frac{F_\mathrm{max} }m \sin \varphi \end{cases} \\
> & \begin{aligned} \left(\omega_n^2 - \omega_d^2\right)^2 A^2 + (2 \zeta \omega_n \omega_d)^2 A^2 = \frac{F_\mathrm{max}^2}{m^2} \left(\cos^2 \varphi + \sin^2 \varphi\right) \\
> A & = \frac{F_\mathrm{max} }{m \sqrt{(2 \zeta \omega_n \omega_d)^2 + \left(\omega_n^2 - \omega_d^2\right)^2} } \\
> & = \frac{F_\mathrm{max} }{m \omega_d \sqrt{(2 \zeta \omega_n)^2 + \frac1{\omega_d^2} \left(\omega_n^2 - \omega_d^2 \right)} } \\
> \frac{-\frac{F_\mathrm{max} }m \sin \varphi}{\frac{F_\mathrm{max} }m \cos \varphi} & = \frac{2 \zeta \omega_n \omega_d A}{\left(\omega_n^2 - \omega_d^2\right) A} \\
> \tan \varphi & = \frac{2 \zeta \omega_n \omega_d}{\omega_d^2 - \omega_n^2} \\
> \varphi & = \arctan \left(\frac{2 \zeta \omega_n \omega_d}{\omega_d^2 - \omega_n^2}\right) + n \pi && (n \in \mathbb{Z}) \\
> x(t) & = A e^{i (\omega_d t + \varphi)} \\
> & = A (\cos(\omega_d t + \varphi) + i \sin(\omega_d t + \varphi)) \\
> & = A \cos(\omega_d t + \varphi) && (\text{drop the imaginary part}) \end{aligned}
> \end{aligned}$$

The transient solution can be found {@{from the homogeneous equation}@}. The steady-state solution is as below: <!--SR:!2026-03-30,564,312-->

> __driven, damped harmonic oscillator with sinusoidal driving force, {@{steady-state solution}@}__
>
> {@{$$x(t) = A \cos(\omega_d t + \varphi)$$}@}
>
> - where
>   - [spring](spring%20(device).md) properties: {@{$k$ is the [spring constant](Hooke's%20law.md), $m$ is the [mass](mass.md), and $c$ is the vicious damping coefficient}@}
>   - derived properties: {@{$\omega_n = \sqrt{\frac{k}m}$ is the natural (undamped) [angular frequency](angular%20frequency.md), $\zeta = \frac{c}{2\sqrt{km} }$ is the damping ratio, $\omega = \omega_n\sqrt{1 - \zeta^2}$ is the [angular frequency](angular%20frequency.md), and $\lambda = \omega_n \zeta$ is the decay rate}@}
>   - [force](force.md) properties: {@{$F(t) = F_\mathrm{max} \cos(\omega_d t)$ is the driving [force](force.md) with max value $F_\mathrm{max}$ and [angular frequency](angular%20frequency.md) $\omega_d$, and $Z_m = \sqrt{(2 \zeta \omega_n)^2 + \frac1{\omega_d^2} \left( \omega_n^2 - \omega_d^2 \right)^2}$ is the [mechanical impedance](mechanical%20impedance.md) or [linear response function](linear%20response%20function.md)}@}
>   - [phase space](phase%20space.md): {@{$A = \frac{F_\mathrm{max} }{m \omega_d Z_m}$ is steady-state [amplitude](amplitude.md) and $\varphi = \arctan \left(\frac{2 \zeta \omega_n \omega_d}{\omega_d^2 - \omega_n^2}\right) + n \pi$ is the initial [phase](phase%20(waves).md) for any [integer](integer.md) $n$, which is usually chosen such that $\varphi \in (-\pi, 0]$ to always represent a phase lag}@}
> - [resonance](resonance.md): {@{Resonance happens when the [amplitude](amplitude.md) is maximum. The resonant [angular frequency](angular%20frequency.md) is $\omega_r = \omega_n \sqrt{1 - 2 \zeta^2}$, thus resonance only occurs for significantly underdamped systems where $\zeta < 1 / \sqrt 2 \approx 0.707\,106\,781$.}@}
> - transient solution: In the full solution, the transient solution is {@{added onto the steady-state solution and can be found from solving the homogeneous equation}@}. Adding the transient solution is required to {@{match any [initial values](initial%20value%20problem.md)}@}. It represents {@{the system's response to the prior state before being applied the driving [force](force.md)}@}. Usually, {@{it can be ignored as it decays quickly if the system is [damped](damping.md)}@}. <!--SR:!2030-11-30,1896,332!2027-10-09,908,292!2028-08-28,1323,350!2029-07-14,1476,312!2026-02-26,165,172!2026-10-26,347,192!2026-04-22,504,252!2026-02-21,548,312!2027-02-04,813,332!2026-03-28,572,312!2026-02-05,576,336-->

<!-- markdownlint MD028 -->

> [!info]- details
>
> - deriving the [resonant](resonance.md) [angular frequency](angular%20frequency.md) $\omega_r$: $$\begin{aligned}
Z(\omega_d) & = \sqrt{(2 \zeta \omega_n \omega_d)^2 + \left(\omega_n^2 - \omega_d^2\right)^2} \\
Z'(\omega_d) & = \frac12 \left((2 \zeta \omega_n \omega_d)^2 + \left(\omega_n^2 - \omega_d^2\right)^2\right)^{-\frac12} \cdot \left( 2(2 \zeta \omega_n \omega_d) \cdot 2 \zeta \omega_n - 2\left(\omega_n^2 - \omega_d^2\right) \cdot 2 \omega_d \right) \\
0 & = 2 \left((2 \zeta \omega_n \omega_r)^2 + \left(\omega_n^2 - \omega_r^2\right)^2\right)^{-\frac12} \cdot \left( 2 \zeta^2 \omega_n^2 - \left(\omega_n^2 - \omega_r^2\right) \right) \omega_r \\
& = 2 \zeta^2 \omega_n^2 - \omega_n^2+ \omega_r^2 \\
\omega_r^2 & = \omega_n^2 - 2 \zeta^2 \omega_n^2 \\
\omega_r & = \omega_n \sqrt{1 - 2 \zeta^2}
\end{aligned}$$

## universal oscillator equation

Through [nondimensionalization](nondimensionalization.md), the equation below {@{known as the __universal oscillator equation__ can be obtained. It is named so because all second-order oscillatory system can be reduced into this form}@}. <!--SR:!2027-09-01,1041,352-->

> __universal oscillator equation__
>
> {@{$$\frac{\mathrm{d}^2 q}{\mathrm{d}\tau^2} + 2 \zeta \frac{\mathrm{d} q}{\mathrm{d}\tau} + q = f(\tau)$$}@}
>
> - where
>   - properties: {@{$\tau$ is the [independent variable](dependent%20and%20independent%29variables.md), $q$ is the [dependent variable](dependent%20and%20independent%29variables.md), $\zeta$ is the damping ratio, and $f(\tau)$ is the [forcing function](forcing%20function%20(differential%20equations).md)}@} <!--SR:!2027-01-31,820,332!2026-11-19,758,332-->

In terms of properties, the universal oscillator equation is {@{the same as the equation for a [driven, damped harmonic oscillator](#driven,%20damped%20harmonic%20oscillator) but with less [constants](constant%20(mathematics).md)}@}. <!--SR:!2027-06-03,898,332-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/harmonic_oscillator) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
