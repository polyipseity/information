---
aliases:
  - harmonic oscillator
  - harmonic oscillators
tags:
  - flashcards/general/harmonic_oscillator
  - languages/in/English
---

# harmonic oscillator

## simple harmonic oscillator

- see: [simple harmonic motion](simple%20harmonic%20motion.md)

## damped harmonic oscillator

- see: [damping](damping.md)

## driven harmonic oscillator

The [ordinary differential equation](ordinary%20differential%20equation.md) for a driven harmonic oscillator with a externally applied force $F(t)$ can be derived from {{[Newton's second law](Newton's laws of motion.md#second law), [Hooke's law](Hooke's law.md), and a _viscous [damping](damping.md) coefficient_}}:

> __ordinary differential equation__
>
> {{$$\begin{aligned} F_\mathrm{net} = m\frac{\mathrm{d}^2x}{\mathrm{d}t^2} & = F(t) -k x - c \frac{\mathrm{d}x}{\mathrm{d}t} \\ \frac{\mathrm{d}^2x}{\mathrm{d}t^2} + \frac{c}m \frac{\mathrm{d}x}{\mathrm{d}t} + \frac{k}m x & = \frac{F(t)}m \end{aligned}$$}}
>
> - where
>     - {{[function](function%20(mathematics).md) properties: $F_\mathrm{net}$ is the [net force](net%20force.md), $x$ is the [displacement](displacement%20(geometry).md) from equilibrium, and $t$ is the [time](time.md)}}
>     - {{[oscillator](oscillation.md) properties: $k$ is the [spring constant](Hooke's%20law.md) and $m$ vis the [mass](mass.md), $c$ is the _viscous damping coefficient_, and $F(t)$ is the driving [force](force.md)}}

For better physical meaning, it can be rewritten as:

> __ordinary differential equation, rewritten__
>
> {{$$\frac{\mathrm{d}^2x}{\mathrm{d}t^2} + 2 \zeta \omega_n \frac{\mathrm{d}x}{\mathrm{d}t} + \omega_n^2 x = \frac{F(t)}m$$}}
>
> - where
>     - {{[function](function%20(mathematics).md) properties: $x$ is the [displacement](displacement%20(geometry).md) from equilibrium and $t$ is the [time](time.md)}}
>     - {{[oscillator](oscillation.md) properties: $\omega_n = \sqrt{\frac{k}m}$ is the natural (undamped) [angular frequency](angular%20frequency.md), $\zeta = \frac{c}{2\sqrt{km} }$ is the _damping ratio_, $k$ is the [spring constant](Hooke's%20law.md), $m$ is the [mass](mass.md), $c$ is the _viscous damping coefficient_, and $F(t)$ is the driving [force](force.md)}}
