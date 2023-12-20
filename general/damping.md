---
aliases:
  - damping
tags:
  - flashcards/general/damping
  - languages/in/English
---

# damping

## derivation

The [ordinary differential equation](ordinary%20differential%20equation.md) for damped harmonic oscillator can be derived from {{[Newton's second law](Newton's%20laws%20of%20motion.md#second%20law), [Hooke's law](Hooke's%20law.md), and a _viscous damping coefficient_}}:

> __ordinary differential equation__
>
> {{$$\begin{aligned} F_\mathrm{net} = m\frac{\mathrm{d}^2x}{\mathrm{d}t^2} & = -k x - c \frac{\mathrm{d}x}{\mathrm{d}t} \\ \frac{\mathrm{d}^2x}{\mathrm{d}t^2} + \frac{c}m \frac{\mathrm{d}x}{\mathrm{d}t} + \frac{k}m x & = 0 \end{aligned}$$}}
>
> - where
>     - {{[function](function%20(mathematics).md) properties: $F_\mathrm{net}$ is the [net force](net%20force.md), $x$ is the [displacement](displacement%20(geometry).md) from equilibrium, and $t$ is the [time](time.md)}}
>     - {{[oscillator](oscillation.md) properties: $k$ is the [spring constant](Hooke's%20law.md) and $m$ is the [mass](mass.md), and $c$ is the _viscous damping coefficient_}}

For better physical meaning, it can be rewritten as:

> __ordinary differential equation, rewritten__
>
> {{$$\frac{\mathrm{d}^2x}{\mathrm{d}t^2} + 2 \zeta \omega_n \frac{\mathrm{d}x}{\mathrm{d}t} + \omega_n^2 x = 0$$}}
>
> - where
>     - {{[function](function%20(mathematics).md) properties: $x$ is the [displacement](displacement%20(geometry).md) from equilibrium and $t$ is the [time](time.md)}}
>     - {{[oscillator](oscillation.md) properties: $\omega_n = \sqrt{\frac{k}m}$ is the natural (undamped) [angular frequency](angular%20frequency.md), $\zeta = \frac{c}{2\sqrt{km}}$ is the _damping ratio_, $k$ is the [spring constant](Hooke's%20law.md), $m$ is the [mass](mass.md), and $c$ is the _viscous damping coefficient_}}

Solving the [ordinary differential equation](orindary%20differential%20equation.md):

$$\begin{aligned}
\frac{\mathrm{d}^2x}{\mathrm{d}t^2} + 2 \zeta \omega_n \frac{\mathrm{d}x}{\mathrm{d}t} + \omega_n^2 x & = 0 \\
r^2 + 2 \zeta \omega_n r + \omega_n^2 & = 0 \\
r & = \frac{-2 \zeta \omega_n \pm \sqrt{(2 \zeta \omega_n)^2 - 4 \omega_n^2}}2 \\
& = -\zeta\omega_n \pm \sqrt{\zeta^2 \omega_n^2 - \omega_n^2} \\
& = -\zeta\omega_n \pm \omega_n \sqrt{\zeta^2 - 1} \\
& = -\omega_n \left(\zeta \pm i\sqrt{1-\zeta^2} \right) \\
x(t) & = \begin{cases}e^{-\omega_n \zeta t} \left(c_1 \cos\left(\omega_n \sqrt{1 - \zeta^2} t\right) + c_2 \sin\left(\omega_n \sqrt{1 - \zeta^2} t\right)\right) & \text{if } \zeta < 1 \\
e^{-\omega_n \zeta t} (c_1 + c_2 t) & \text{if } \zeta = 1 \\
e^{-\omega_n \zeta t} \left(c_1 e^{\omega_n \sqrt{\zeta^2 - 1}} + c_2 e^{-\omega_n \sqrt{\zeta^2 - 1}}\right) & \text{if } \zeta > 1 \\
\end{cases}
\end{aligned}$$
