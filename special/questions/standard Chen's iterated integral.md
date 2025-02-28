---
aliases:
  - standard Chen's iterated integral
tags:
  - date/2024/02/29
  - flashcard/active/special/questions/standard_Chen_s_iterated_integral
  - language/in/English
  - question/mathematics/calculus/integral
---

# standard Chen's iterated integral

- datetime: 2024-02-29T17:31:14.505+08:00

A standard Chen's iterated integral is as follows, where $n \in \mathbb{Z}_{\ge 0}$ and $f$ is an [operator](../../general/operator%20(mathematics).md) that forms an [abelian group](../../general/abelian%20group.md):

$$\int_a^b \!\mathrm{d}x_1 \int_a^{x_1} \!\mathrm{d}x_2 \cdots \int_a^{x_{n - 1} } \!\mathrm{d}x_n \, f(x_1) f(x_2) \cdots f(x_n)$$

Simplify it.

## strategy

- inspecting "$$\int_a^b \!\mathrm{d}x_1 \int_a^{x_1} \!\mathrm{d}x_2 \cdots \int_a^{x_{n - 1} } \!\mathrm{d}x_n \, f(x_1) f(x_2) \cdots f(x_n)$$" :@: Calculate the first few $n$ and see if any patterns can be found. <!--SR:!2026-09-03,552,310-->
- proving that the pattern holds :@: Use mathematical induction. <!--SR:!2025-07-30,295,330-->

## solution

$$\begin{aligned}
I_n(b) & := \int_a^b \!\mathrm{d}x_1 \int_a^{x_1} \!\mathrm{d}x_2 \cdots \int_a^{x_{n - 1} } \!\mathrm{d}x_n \, f(x_1) f(x_2) \cdots f(x_n) \\
\\
I_0(b) & = 1 \\
I_1(b) & = \int_a^b \!\mathrm{d}x_1 \, f(x_1) \\
I_2(b) & = \int_a^b \!\mathrm{d}x_1 \int_a^{x_1} \,\mathrm{d}x_2 \, f(x_1) f(x_2) \\
& = \int_a^b \!\mathrm{d}x_1 \, f(x_1) \int_a^{x_1} \!\mathrm{d}x_2 \, f(x_2) \\
& = \int_a^b \!\mathrm{d}x_1 \, I_1'(x_1) I_1(x_1) \\
& = \int_{x_1 = a}^{x_1 = b} \mathrm{d}I_1(x_1) \, I_1(x_1) \\
& = \frac 1 2 I_1^2(b) - \frac 1 2 I_1^2(a) \\
& = \frac 1 2 I_1^2(b) \\
I_3(b) & = \int_a^b \!\mathrm{d}x_1 \int_a^{x_1} \!\mathrm{d}x_2 \int_a^{x_2} \!\mathrm{d}x_3 \, f(x_1) f(x_2) f(x_3) \\
& = \int_a^b \!\mathrm{d}x_1 \, f(x_1) \int_a^{x_1} \!\mathrm{d}x_2 \int_a^{x_2} \!\mathrm{d}x_3 \, f(x_2) f(x_3) \\
& = \int_a^b \!\mathrm{d}x_1 \, f(x_1) I_2(x_1) \\
& = \frac 1 2 \int_a^b \!\mathrm{d}x_1 I_1'(x_1) I_1^2(x_1) \\
& = \frac 1 2 \int_{x_1 = a}^{x_1 = b} \!\mathrm{d}I_1(x_1) \, I_1^2(x_1) \\
& = \frac 1 6 I_1^3(b) - \frac 1 6 I_1^3(a) \\
& = \frac 1 6 I_1^3(b) \\
\\
I_n(b) & \overset ? = \frac 1 {n!} I_1^n(b) \\
\\
I_0(b) & = 1 = \frac 1 {0!} I_1^0(b) \\
I_1(b) & = \frac 1 {1!} I_1^1(b) \\
\\
\exists m \in \mathbb{Z}_{\ge 0} \qquad I_m(b) & = \frac 1 {m!} I_1^m(b) && (\text{assumption}) \\
I_{m + 1}(b) & = \int_a^b \!\mathrm{d}x_1 \int_a^{x_1} \!\mathrm{d}x_2 \cdots \int_a^{x_m} \!\mathrm{d}x_{m + 1} \, f(x_1) f(x_2) \cdots f(x_{m + 1}) \\
& = \int_a^b \!\mathrm{d}x_1 \, f(x_1) \int_a^{x_1} \!\mathrm{d}x_2 \cdots \int_a^{x_m} \!\mathrm{d}x_{m + 1} \, f(x_1) f(x_2) \cdots f(x_{m + 1}) \\
& = \int_a^b \!\mathrm{d}x_1 \, I_1'(x_1) I_m(x_1) \\
& = \int_{x_1 = a}^{x_1 = b} \!\mathrm{d}I_1(x_1) \, I_m(x_1) \\
& = \frac 1 {m!} \int_{x_1 = a}^{x_1 = b} \!\mathrm{d}I_1(x_1) \, I_1^m(x_1) \\
& = \frac 1 {m!(m + 1)} I_1^{m + 1}(b) - \frac 1 {m!(m + 1)} I_1^{m + 1}(a) \\
& = \frac 1 {(m + 1)!} I_1^{m + 1}(b) \\
\qquad I_m(b) = \frac 1 {m!} I_1^m(b) & \implies I_{m + 1}(b) = \frac 1 {(m + 1)!} I_1^{m + 1}(b) \\
\\
\forall n \in \mathbb{Z}_{\ge 0} \qquad I_n(b) & = \frac 1 {n!} I_1^n(b) = \frac 1 {n!} \left( \int_a^b \!\mathrm{d}x \, f(x) \right)^n && (\text{induction})
\end{aligned}$$
