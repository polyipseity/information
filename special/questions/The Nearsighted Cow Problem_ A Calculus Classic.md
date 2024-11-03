---
aliases:
  - 'The Nearsighted Cow Problem: A Calculus Classic'
tags:
  - date/2023/11/08
  - flashcard/active/special/questions/The_Nearsighted_Cow_Problem__A_Calculus_Classic
  - language/in/English
  - question/mathematics/calculus/differential
---

# The Nearsighted Cow Problem: A Calculus Classic

- datetime: 2023-11-08T10:57:15.171+08:00

A rectangular billboard $H$ meters in height stands in a field. A nearsighted cow with eye level at $Y$ meters below the bottom of the billboard stands $x$ meters from the billboard. Express the vertical angle subtended by the billboard at her eye $\theta$ in terms of $x$. Hence, find the distance $x_0$ the cow must stand from the billboard to maximize $\theta$.

## solution

$$\begin{aligned}
\theta&=\arctan{\frac{Y+H}x}-\arctan{\frac{Y}x}\\
\theta'&=\frac{-\left(Y+H\right)x^{-2} }{\left(\frac{Y+H}x\right)^2+1}-\frac{-Yx^{-2} }{\left(\frac{Y}x\right)^2+1}\\
&=\frac{-Yx^{-2}-Hx^{-2} }{\frac{Y^2+2YH+H^2}{x^2}+1}+\frac{Yx^{-2} }{\frac{Y^2}{x^2}+1}\\
&=-\frac{Y+H}{Y^2+2YH+H^2+x^2}+\frac{Y}{Y^2+x^2}\\
0&=-\frac{Y+H}{Y^2+2YH+H^2+x_0^2}+\frac{Y}{Y^2+x_0^2}\\
\frac{Y+H}{Y^2+2YH+H^2+x_0^2}&=\frac{Y}{Y^2+x_0^2}\\
(Y+H)\left(Y^2+x_0^2\right)&=Y\left(Y^2+2YH+H^2+x_0^2\right)\\
Y^3+Yx_0^2+Y^2H+Hx_0^2&=Y^3+2Y^2H+YH^2+Yx_0^2\\
Hx_0^2&=Y^2H+YH^2\\
x_0^2&=Y^2+YH\\
x_0&=\pm\sqrt{Y^2+YH}\\
\end{aligned}$$
