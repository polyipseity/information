---
aliases:
  - chain rule
tags:
  - flashcard/active/general/chain_rule
  - language/in/English
---

# chain rule

## statement

> __chain rule for {{[real-valued functions](real-valued%20function.md) of one [real](real%20number.md) variable}}__
>
> 1. Given {{$f, g: \mathbb{R} \to \mathbb{R}$ and $c \in \mathbb{R}$, if $g'(c)$ and $f'(g(c))$ exists}},
> 2. then {{$(f \circ g)'(c)$ exists and $(f \circ g)'(c) = f'(g(c)) \cdot g'(c)$}}. <!--SR:!2026-01-30,501,312!2024-11-07,199,312!2024-10-21,188,312-->

<!-- markdownlint MD028 -->

> [!example] examples
>
> - $f(x) := x^{2^x}, f'(x) = ?$ :: $f'(x) = x^{2^x} 2^x \left(\frac 1 x + \ln x \ln 2 \right)$ <!--SR:!2025-02-18,133,232-->
> - $a(3) = 27, a(12) = 3, a'(3) = 12, a'(12) = 5, b(2) = 12, b(5) = 12, b'(2) = 27, b'(5) = 3, (a \circ b)'(5) = ?$ :: $(a \circ b)'(5) = a'(b(5)) \cdot b'(5) = a'(12) \cdot b'(5) = 5 \cdot 3 = 15$ <!--SR:!2025-07-12,350,290-->
> - $\frac {\mathrm{d}} {\mathrm{d}\xi} \frac {\mathrm{d}\xi} {\mathrm{d}\eta} = ?$ :: $\frac {\mathrm{d}} {\mathrm{d}\xi} \frac {\mathrm{d}\xi} {\mathrm{d}\eta} = \frac {\mathrm{d}} {\mathrm{d}\eta}$ <!--SR:!2024-12-08,241,332-->
> - $\frac \partial {\partial \alpha} \frac {\partial \alpha} {\partial \beta} = ?$ :: The above form of chain rule does not apply. See [§ multivariable case](#multivariable%20case). [Counterexample](counterexample.md): $x + y + z = 0 \implies \frac {\partial x} {\partial y} = \frac {\partial y} {\partial z} = \frac {\partial z} {\partial x} = -1 \implies -1 = \frac {\partial x} {\partial y} \frac {\partial y} {\partial z} \frac {\partial z} {\partial x} \ne \frac {\partial x} {\partial x} = 1$ <!--SR:!2025-10-24,474,312-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/chain_rule) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
