---
aliases:
  - damping
tags:
  - flashcard/active/general/eng/damping
  - language/in/English
---

# damping

## derivation

The [ordinary differential equation](ordinary%20differential%20equation.md) for damped harmonic oscillator can be derived from {@{[Newton's second law](Newton's%20laws%20of%20motion.md#second%20law), [Hooke's law](Hooke's%20law.md), and a _viscous damping coefficient_}@}: <!--SR:!2028-06-05,1262,350-->

> __ordinary differential equation__
>
> {@{$$\begin{aligned} F_\mathrm{net} = m\frac{\mathrm{d}^2x}{\mathrm{d}t^2} & = -k x - c \frac{\mathrm{d}x}{\mathrm{d}t} \\ \frac{\mathrm{d}^2x}{\mathrm{d}t^2} + \frac{c}m \frac{\mathrm{d}x}{\mathrm{d}t} + \frac{k}m x & = 0 \end{aligned}$$}@}
>
> where
>
> - [function](function%20(mathematics).md) properties: $F_\mathrm{net}$ is {@{the [net force](net%20force.md)}@}, $x$ is {@{the [displacement](displacement%20(geometry).md) from equilibrium}@}, and $t$ is {@{the [time](time.md)}@}
> - [oscillator](oscillation.md) properties: $k$ is {@{the [spring constant](Hooke's%20law.md)}@} and $m$ is {@{the [mass](mass.md)}@}, and $c$ is {@{the _viscous damping coefficient_}@} <!--SR:!2029-08-20,1415,310!2027-03-01,874,330!2031-07-17,2072,330!2026-01-14,79,349!2026-01-21,85,349!2026-01-20,84,349!2026-01-14,79,349-->

For better physical meaning, it can be rewritten as:

> __ordinary differential equation, rewritten__
>
> {@{$$\frac{\mathrm{d}^2x}{\mathrm{d}t^2} + 2 \zeta \omega_n \frac{\mathrm{d}x}{\mathrm{d}t} + \omega_n^2 x = 0$$}@}
>
> where
>
> - [function](function%20(mathematics).md) properties: $x$ is {@{the [displacement](displacement%20(geometry).md) from equilibrium}@} and $t$ is {@{the [time](time.md)}@}
> - [oscillator](oscillation.md) properties: {@{$\omega_n = \sqrt{\frac{k}m}$}@} is {@{the natural \(undamped\) [angular frequency](angular%20frequency.md)}@}, {@{$\zeta = \frac{c}{2\sqrt{km} }$}@} is {@{the _damping ratio_}@}, $k$ is {@{the [spring constant](Hooke's%20law.md)}@}, $m$ is {@{the [mass](mass.md)}@}, and $c$ is {@{the _viscous damping coefficient_}@} <!--SR:!2026-02-07,544,310!2028-08-23,1327,350!2027-11-20,940,290!2026-01-14,79,349!2026-01-19,83,349!2026-01-13,78,349!2026-01-14,79,349!2026-01-21,85,349!2026-01-12,77,349!2026-01-18,82,349-->

Solving the [ordinary differential equation](orindary%20differential%20equation.md):

> [!info]- details
> $$\begin{aligned}
> \frac{\mathrm{d}^2x}{\mathrm{d}t^2} + 2 \zeta \omega_n \frac{\mathrm{d}x}{\mathrm{d}t} + \omega_n^2 x & = 0 \\
> r^2 + 2 \zeta \omega_n r + \omega_n^2 & = 0 \\
> r & = \frac{-2 \zeta \omega_n \pm \sqrt{(2 \zeta \omega_n)^2 - 4 \omega_n^2} }2 \\
> & = -\zeta\omega_n \pm \sqrt{\zeta^2 \omega_n^2 - \omega_n^2} \\
> & = -\zeta\omega_n \pm \omega_n \sqrt{\zeta^2 - 1} \\
> & = -\omega_n \left(\zeta \pm i\sqrt{1-\zeta^2} \right) \\
> x(t) & = \begin{cases} e^{-t \omega_n \zeta} \left(c_1 \cos\left(t \omega_n \sqrt{1 - \zeta^2}\right) + c_2 \sin\left(t \omega_n \sqrt{1 - \zeta^2}\right)\right) & \text{if } \lvert \zeta \rvert < 1 \\
> e^{-t \omega_n \zeta} (c_1 + t c_2) & \text{if } \lvert \zeta \rvert = 1 \\
> e^{-t \omega_n \zeta} \left(c_1 e^{t \omega_n \sqrt{\zeta^2 - 1} } + c_2 e^{-t \omega_n \sqrt{\zeta^2 - 1} }\right) & \text{if } \lvert \zeta \rvert > 1 \end{cases} \\
> \\
> v(t) & = x'(t) \\
> & = \begin{cases} -e^{-t \omega_n \zeta} \omega_n \zeta \left(c_1 \cos\left(t \omega_n \sqrt{1 - \zeta^2}\right) + c_2 \sin\left(t \omega_n \sqrt{1 - \zeta^2}\right)\right) + e^{-t \omega_n \zeta} \omega_n \sqrt{1 - \zeta^2} \left(-c_1 \sin\left(t \omega_n \sqrt{1 - \zeta^2} \right) + c_2 \cos\left(t \omega_n \sqrt{1 - \zeta^2} \right)\right) & \text{if } \lvert \zeta \rvert < 1 \\
> -e^{-t \omega_n \zeta} \omega_n \zeta (c_1 + t c_2) + e^{-t \omega_n \zeta} c_2 & \text{if } \lvert \zeta \rvert = 1 \\
> -e^{-t \omega_n \zeta} \omega_n \zeta \left(c_1 e^{t \omega_n \sqrt{\zeta^2 - 1} } + c_2 e^{-t \omega_n \sqrt{\zeta^2 - 1} }\right) + e^{-t \omega_n \zeta} \omega_n \sqrt{\zeta^2 - 1} \left(c_1 e^{t \omega_n \sqrt{\zeta^2 - 1} } - c_2 e^{-t \omega_n \sqrt{\zeta^2 - 1} }\right) & \text{if } \lvert \zeta \rvert > 1 \end{cases} \\
> \\
> x_0 & = \begin{cases} e^{-0 \omega_n \zeta} \left(c_1 \cos\left(0 \omega_n \sqrt{1 - \zeta^2}\right) + c_2 \sin\left(0 \omega_n \sqrt{1 - \zeta^2}\right)\right) & \text{if } \lvert \zeta \rvert < 1 \\
> e^{-0 \omega_n \zeta} (c_1 + 0 c_2) & \text{if } \lvert \zeta \rvert = 1 \\
> e^{-0 \omega_n \zeta} \left(c_1 e^{0 \omega_n \sqrt{\zeta^2 - 1} } + c_2 e^{-0 \omega_n \sqrt{\zeta^2 - 1} }\right) & \text{if } \lvert \zeta \rvert > 1 \end{cases} \\
> & = \begin{cases} c_1 & \text{if } \lvert \zeta \rvert \le 1 \\
> c_1 + c_2 & \text{if } \lvert \zeta \rvert > 1 \end{cases} \\
> \\
> v_0 & = \begin{cases} -e^{-0 \omega_n \zeta} \omega_n \zeta \left(c_1 \cos\left(0 \omega_n \sqrt{1 - \zeta^2}\right) + c_2 \sin\left(0 \omega_n \sqrt{1 - \zeta^2}\right)\right) + e^{-0 \omega_n \zeta} \omega_n \sqrt{1 - \zeta^2} \left(-c_1 \sin\left(0 \omega_n \sqrt{1 - \zeta^2} \right) + c_2 \cos\left(0 \omega_n \sqrt{1 - \zeta^2} \right)\right) & \text{if } \lvert \zeta \rvert < 1 \\
> -e^{-0 \omega_n \zeta} \omega_n \zeta (c_1 + 0 c_2) + e^{-0 \omega_n \zeta} c_2 & \text{if } \lvert \zeta \rvert = 1 \\
> -e^{-0 \omega_n \zeta} \omega_n \zeta \left(c_1 e^{0 \omega_n \sqrt{\zeta^2 - 1} } + c_2 e^{-0 \omega_n \sqrt{\zeta^2 - 1} }\right) + e^{-0 \omega_n \zeta} \omega_n \sqrt{\zeta^2 - 1} \left(c_1 e^{0 \omega_n \sqrt{\zeta^2 - 1} } - c_2 e^{-0 \omega_n \sqrt{\zeta^2 - 1} }\right) & \text{if } \lvert \zeta \rvert > 1 \end{cases} \\
> & = \begin{cases} -c_1 \omega_n \zeta + c_2 \omega_n \sqrt{1 - \zeta^2} & \text{if } \lvert \zeta \rvert < 1 \\
> -c_1 \omega_n \zeta + c_2 & \text{if } \lvert \zeta \rvert = 1 \\
> -\omega_n \zeta (c_1 + c_2) + \omega_n \sqrt{\zeta^2 - 1} (c_1 - c_2) & \text{if } \lvert \zeta \rvert > 1 \end{cases} \\
> & = \begin{cases} -x_0 \omega_n \zeta + c_2 \omega_n \sqrt{1 - \zeta^2} & \text{if } \lvert \zeta \rvert < 1 \\
> -x_0 \omega_n \zeta + c_2 & \text{if } \lvert \zeta \rvert = 1 \\
> -x_0 \omega_n \zeta + \omega_n \sqrt{\zeta^2 - 1} (x_0 - 2c_2) & \text{if } \lvert \zeta \rvert > 1 \end{cases} \\
> c_2 & = \begin{cases} \frac{v_0 + x_0 \omega_n \zeta}{\omega_n \sqrt{1 - \zeta^2} } & \text{if } \lvert \zeta \rvert < 1 \\
> v_0 + x_0 \omega_n \zeta & \text{if } \lvert \zeta \rvert = 1 \\
> \frac{x_0}2 - \frac{v_0 + x_0 \omega_n \zeta}{2 \omega_n \sqrt{\zeta^2 - 1} } & \text{if } \lvert \zeta \rvert > 1 \end{cases} \\
> & = \begin{cases} \frac\zeta{\sqrt{1 - \zeta^2} } x_0 + \frac1{\omega_n \sqrt{1 - \zeta^2} } v_0 & \text{if } \lvert \zeta \rvert < 1 \\
> \omega_n \zeta x_0 + v_0 & \text{if } \lvert \zeta \rvert = 1 \\
> \frac{\sqrt{\zeta^2 - 1} - \zeta}{2 \sqrt{\zeta^2 - 1} } x_0 - \frac1{2 \omega_n \sqrt{\zeta^2 - 1} } v_0 & \text{if } \lvert \zeta \rvert > 1 \end{cases} \\
> \\
> x_0 & = \begin{cases} c_1 & \text{if } \lvert \zeta \rvert \le 1 \\
> c_1 + c_2 & \text{if } \lvert \zeta \rvert > 1 \end{cases} \\
> & = \begin{cases} c_1 & \text{if } \lvert \zeta \rvert \le 1 \\
> c_1 + \frac{\sqrt{\zeta^2 - 1} - \zeta}{2 \sqrt{\zeta^2 - 1} } x_0 - \frac1{2 \omega_n \sqrt{\zeta^2 - 1} } v_0 & \text{if } \lvert \zeta \rvert > 1 \end{cases} \\
> c_1 & = \begin{cases}x_0 & \text{if } \lvert \zeta \rvert \le 1 \\
> \frac{2\sqrt{\zeta^2 - 1} - \sqrt{\zeta^2 - 1} + \zeta}{2 \sqrt{\zeta^2 - 1} } x_0 + \frac1{2 \omega_n \sqrt{\zeta^2 - 1} } v_0 & \text{if } \lvert \zeta \rvert > 1 \end{cases} \\
> & = \begin{cases}x_0 & \text{if } \lvert \zeta \rvert \le 1 \\
> \frac{\sqrt{\zeta^2 - 1} + \zeta}{2 \sqrt{\zeta^2 - 1} } x_0 + \frac1{2 \omega_n \sqrt{\zeta^2 - 1} } v_0 & \text{if } \lvert \zeta \rvert > 1 \end{cases}
> \end{aligned}$$

There are four regimes depending on the value of the damping ratio $\zeta$:

> __undamped__
>
> When $\zeta = 0$, {@{this is equivalent to [simple harmonic motion](simple%20harmonic%20motion.md)}@}. This is {@{rare in the natural world due to [dissipation](dissipation.md)}@}. <!--SR:!2028-07-21,1300,350!2029-03-11,1490,363-->

<!-- markdownlint MD028 -->

> __underdamped__
>
> When $0 < \zeta < 1$, {@{the system resembles [simple harmonic motion](simple%20harmonic%20motion.md) with its _maximum_ [amplitude](amplitude.md) [modulated](modulation.md) by $e^{-\lambda t}$}@}. This is {@{common in the natural world due to small amounts of [dissipation](dissipation.md)}@}. The equation is:
>
> {@{$$x(t) = A_{\text{max} } e^{-\lambda t} \cos(\omega t + \varphi)$$}@}
>
> where
>
> - [spring](spring%20(device).md) properties: $k$ is {@{the [spring constant](Hooke's%20law.md)}@}, $m$ is {@{the [mass](mass.md)}@}, and $c$ is {@{the vicious damping coefficient}@}
> - derived properties: {@{$\omega_n = \sqrt{\frac{k}m}$}@} is {@{the natural \(undamped\) [angular frequency](angular%20frequency.md)}@}, {@{$\zeta = \frac{c}{2\sqrt{km} }$}@} is {@{the damping ratio}@}, {@{$\omega = \omega_n\sqrt{1 - \zeta^2}$}@} is {@{the [angular frequency](angular%20frequency.md)}@}, and {@{$\lambda = \omega_n \zeta$}@} is {@{the decay rate}@}
> - initial properties: {@{$A_{\text{max} } = \sqrt{A_0^2 + \left(\frac {v_0 + \lambda A} \omega \right)^2}$}@} is {@{the _maximum_ [amplitude](amplitude.md)}@} and {@{$\varphi = \operatorname{atan2}\left(-\frac{v_0+\lambda A}\omega, A\right) \approx \operatorname{atan2}\left(-\frac{v_0}\omega, A\right)$}@} is {@{the initial phase}@} <!--SR:!2029-04-12,1411,310!2026-04-03,634,330!2026-06-16,573,270!2027-01-18,744,290!2026-10-02,642,270!2026-05-01,174,183!2026-01-20,84,349!2026-01-12,77,349!2026-01-21,85,349!2026-01-21,85,349!2026-01-12,77,349!2026-01-15,80,349!2026-01-19,83,349!2026-01-20,84,349!2025-12-07,30,309!2025-11-21,25,309!2026-01-20,84,349!2026-01-20,64,362-->

<!-- markdownlint MD028 -->

> __critically damped__
>
> When $\zeta = 1$, {@{the system returns to equilibrium as quickly as possible without [oscillation](oscillation.md). Overshooting can occur for once if the initial [velocity](velocity.md) is high enough}@}. This type of damping is {@{desirable in many engineering designs when a damped oscillator is needed, like door closing}@}. The equation is:
>
> {@{$$x(t) = e^{-\lambda t} (A + \nu t)$$}@}
>
> where
>
> - [spring](spring%20(device).md) properties: $k$ is {@{the [spring constant](Hooke's%20law.md)}@}, $m$ is {@{the [mass](mass.md)}@}, and {@{$c = 2 \sqrt{km}$}@} is {@{the vicious damping coefficient}@}
> - derived properties: {@{$\omega_n = \sqrt{\frac{k}m}$}@} is {@{the natural \(undamped\) [angular frequency](angular%20frequency.md)}@}, {@{$\zeta = \frac{c}{2\sqrt{km} } = 1$}@} is {@{the damping ratio}@}, and {@{$\lambda = \omega_n \zeta = \omega_n$}@} is {@{the decay rate}@}
> - initial properties: $A$ is {@{the initial [amplitude](amplitude.md)}@} and {@{$\nu = v_0 + \lambda A \approx v_0$}@} is {@{approximately the initial [velocity](velocity.md) $v_0$}@} <!--SR:!2027-03-17,845,330!2026-05-28,564,270!2027-05-21,592,290!2026-09-25,639,270!2026-07-10,326,230!2029-05-11,1363,283!2026-01-12,77,349!2026-01-13,78,349!2026-01-19,83,349!2026-01-15,80,349!2026-01-18,82,349!2026-01-13,78,349!2026-01-20,84,349!2025-12-07,47,329!2026-01-14,79,349!2025-12-06,46,329-->

<!-- markdownlint MD028 -->

> __overdamped__
>
> When $\zeta > 1$, {@{the systems return to equilibrium [exponentially](exponential%20decay.md) without [oscillation](oscillation.md), increasingly slowly with larger $\zeta$. Overshooting can occur for once if the initial [velocity](velocity.md) is high enough}@}. This type of damping is {@{desirable if overshooting has tragic outcomes, usually electrical rather than mechanical, such as critical [control systems](control%20system.md)}@}. The equation is:
>
> {@{$$x(t) = e^{-\lambda t} \left(c_+ e^{\omega t} + c_- e^{-\omega t}\right)$$}@}
>
> where
>
> - [spring](spring%20(device).md) properties: $k$ is {@{the [spring constant](Hooke's%20law.md)}@}, $m$ is {@{the [mass](mass.md)}@}, and $c$ is {@{the vicious damping coefficient}@}
> - derived properties: {@{$\omega_n = \sqrt{\frac{k}m}$}@} is {@{the natural \(undamped\) [angular frequency](angular%20frequency.md)}@}, {@{$\zeta = \frac{c}{2\sqrt{km} }$}@} is {@{the damping ratio}@}, {@{$\omega = \omega_n\sqrt{\zeta^2 - 1}$}@} is {@{the [angular frequency](angular%20frequency.md)}@}, and {@{$\lambda = \omega_n \zeta$}@} is {@{the decay rate}@}
> - initial properties: {@{$c_+ = \frac{\omega + \lambda}{2 \omega} x_0 + \frac1{2 \omega} v_0, c_- = \frac{\omega - \lambda}{2 \omega} x_0 - \frac1{2 \omega} v_0$}@} from {@{the initial [displacement](displacement%20(geometry).md) $x_0$ and the initial [velocity](velocity.md) $v_0$}@}; {@{the $c_-$ term}@} is {@{negligible for large [time](time.md) $t$}@} <!--SR:!2026-02-10,545,310!2027-07-20,954,310!2026-02-21,499,270!2029-07-01,1380,310!2026-04-03,186,210!2025-11-29,127,163!2025-12-05,45,329!2026-01-13,78,349!2026-01-20,84,349!2026-01-20,84,349!2026-01-20,84,349!2026-01-15,80,349!2026-01-12,77,349!2026-01-15,80,349!2026-01-18,68,289!2026-01-15,80,349!2025-11-24,34,309!2026-01-13,78,349-->

Additionally, for negative damping ratios:

> __negative damping__
>
> If $\zeta < 0$, {@{then the system is driven rather than damped. The driving [force](force.md) increases as the [velocity](velocity.md) increases. Therefore, the [amplitude](amplitude.md) increases without bound as $e^{\lvert \lambda \rvert t}$. It is very similar (but not exactly equivalent) to the regime with the corresponding positive damping ratio $\lvert \zeta \rvert$ but going back in [time](time.md)}@}. This is {@{unnatural in the natural world, but can happen under some circumstances}@}, such as {@{the swaying of the [Millennium Bridge in London](Millennium%20Bridge,%20London.md) when it was first opened}@} and {@{the collapse of the [1940 Tacoma Narrows Bridge](Tacoma%20Narrows%20Bridge%20(1940).md)}@}. The equations in the above regimes applies to negative damping as well. Choose the equation that applies to the [absolute value](absolute%20value.md) of the damping ratio $\lvert \zeta \rvert$. <!--SR:!2027-07-28,789,250!2028-05-21,1031,263!2026-10-19,349,366!2026-10-24,354,366-->

## _Q_ factor and decay rate

- see: [_Q_ factor](Q%20factor.md)

> ___Q_ factor__
>
> {@{$$Q = \frac{1}{2 \zeta}$$}@}
>
> where
>
> - {@{$Q$}@} is {@{the [_Q_ factor](Q%20factor.md) of an [oscillator](osccillation.md)}@} with {@{damping ratio $\zeta$}@} <!--SR:!2029-05-04,1310,303!2028-12-16,1424,363-->

<!-- markdownlint MD028 -->

> __exponential decay rate__
>
> {@{$$\lambda = \omega_n \zeta$$}@}
>
> where
>
> - {@{$\lambda$}@} is {@{the decay rate of an [oscillator](oscillation.md)}@} with {@{natural frequency $\omega_n$ and damping ratio $\zeta$}@} <!--SR:!2026-10-23,717,323!2026-11-08,727,323-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/damping) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
