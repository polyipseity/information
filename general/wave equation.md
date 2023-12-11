---
aliases:
  - wave equation
  - wave equations
tags:
  - flashcards/general/wave_equation
---

# wave equation

## introduction

> __scalar wave equation__
>
> {{$$\frac{\partial^2 u}{\partial t^2} = c^2 \sum_{i=1}^n \frac{\partial^2 u}{\partial x_i^2}$$}}
>
> where
> - {{$t$ is time}}
> - {{$x$ is $n$-dimensional position}}
> - {{$u$ is the displacement from equilibrium}}
> - {{$c$ is a non-negative constant}}

## wave equation in one dimension

> __general solution of scalar wave equation in one dimension__
>
> {{$$u(x, t) = F(x - ct) + G(x + ct)$$}}
>
> where
> - {{$t$ is time}}
> - {{$x$ is $n$-dimensional position}}
> - {{$u$ is the displacement from equilibrium}}
> - {{$c$ is a non-negative constant}}
> - {{$F$ and $G$ are arbitrary [generalized functions](generalized%20function.md) representing respectively the right and left-traveling waveforms}}

### algebraic approach

$$\begin{aligned}
\xi & \overset{\text{def}}= x - ct \\
\eta & \overset{\text{def}}= x + ct \\
\frac{\partial}{\partial x} & = \frac{\partial \xi}{\partial x} \frac{\partial}{\partial \xi} + \frac{\partial \eta}{\partial x} \frac{\partial}{\partial \eta} \\
& = \frac{\partial}{\partial \xi} + \frac{\partial}{\partial \eta} \\
\frac{\partial}{\partial t} &= \frac{\partial \xi}{\partial t} \frac{\partial}{\partial \xi} + \frac{\partial \eta}{\partial t} \frac{\partial}{\partial \eta} \\
& = -c \frac{\partial}{\partial \xi} + c \frac{\partial}{\partial \eta} \\
\frac{\partial^2 u}{\partial t^2} &= c^2 \frac{\partial^2 u}{\partial x^2} \\
\left( -c \frac{\partial}{\partial \xi} + c \frac{\partial}{\partial \eta} \right)^2 u & = c^2 \left( \frac{\partial}{\partial \xi} + \frac{\partial}{\partial \eta} \right)^2 u \\
\left( - \frac{\partial}{\partial \xi} + \frac{\partial}{\partial \eta} \right)^2 u & = \left( \frac{\partial}{\partial \xi} + \frac{\partial}{\partial \eta} \right)^2 u \\
-2 \frac{\partial^2}{\partial \xi \partial \eta} u &= 2 \frac{\partial^2}{\partial \xi \partial \eta} u \\
\frac{\partial^2}{\partial \xi \partial \eta} u &= 0 \\
u(\xi, \eta) &= F(\xi) + G(\eta) \\
u(x, t) &= F(x - ct) + G(x + ct)
\end{aligned}$$

> [!tip]
>
> - reason why one can swap partial derivatives: {{Think of $\frac{\partial}{\partial t}$ as an operator. Then for functions of class $C^2$, $\frac{\partial}{\partial x}\frac{\partial}{\partial y}=\frac{\partial}{\partial y}\frac{\partial}{\partial x}$. The interpretation is that differentiation does not depend on the order of operation for sufficiently smooth functions.}}
