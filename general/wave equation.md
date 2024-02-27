---
aliases:
  - wave equation
  - wave equations
tags:
  - flashcard/general/wave_equation
  - language/in/English
---

# wave equation

## introduction

> __scalar wave equation__
>
> {{$$\frac{\partial^2 u}{\partial t^2} = c^2 \sum_{i=1}^n \frac{\partial^2 u}{\partial x_i^2}$$}}
>
> where
>
> - [function](function%20(mathematics).md) properties: {{$u$ is [displacement](displacement%20(geometry).md) from equilibrium at $n$-[dimensional](dimension.md) [position](position%20(geometry).md) $x$ and [time](time.md) $t$}}
> - [wave](wave.md) properties: {{$c$ is a non-negative [real](real%20number.md) [coefficient](coefficient.md)}} <!--SR:!2024-05-10,99,270!2024-02-28,59,310!2024-03-09,66,310-->

## wave equation in one dimension

> __general solution of scalar wave equation in one dimension__
>
> {{$$u(x, t) = F(x - ct) + G(x + ct)$$}}
>
> where
>
> - [function](function%20(mathematics).md) properties: {{$u$ is [displacement](displacement%20(geometry).md) from equilibrium at $n$-[dimensional](dimension.md) [position](position%20(geometry).md) $x$ and [time](time.md) $t$}}
> - [wave](wave.md) properties: {{$c$ is a non-negative [real](real%20number.md) [coefficient](coefficient.md), and $F$ and $G$ are arbitrary [generalized functions](generalized%20function.md) representing respectively the right and left-traveling [waveforms](waveform.md)}} <!--SR:!2024-08-12,170,310!2024-08-07,176,310!2024-03-12,69,310-->

### algebraic approach

$$\begin{aligned}
\xi & \overset{\text{def} }= x - ct \\
\eta & \overset{\text{def} }= x + ct \\
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

> [!tip] tips
>
> - reason why one can swap [partial derivatives](partial%20derivative.md): {{Think of $\frac{\partial}{\partial t}$ as an [operator](operator%20(mathematics).md). Then for [functions](function%20(mathematics).md) of class $C^2$, $\frac{\partial}{\partial x}\frac{\partial}{\partial y}=\frac{\partial}{\partial y}\frac{\partial}{\partial x}$. The interpretation is that [differentiation](derivative.md) does not depend on the order of operation for sufficiently [smooth](smoothness.md) functions. This is known as [Schwarz's theorem](symmetry%20of%20second%20derivatives.md#Schwarz's%20theorem).}} <!--SR:!2024-03-07,51,250-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/wave_equation) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
