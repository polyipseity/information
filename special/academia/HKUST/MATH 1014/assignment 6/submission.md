---
aliases:
  - HKUST MATH 1014 L1 assignment 6 submission
tags:
  - date/2024/04/26
  - language/in/English
---

# L1 assignment 6 submission

- HKUST MATH 1014

MATH1014 Calculus II Problem Set 6<br/>
L01 (Spring 2024)

Problem Set 6

Note: The problem sets serve as additional exercise problems for your own practice. Problem Set 6 covers materials from §7.7 – §8.2.

## Q4

Compute the area of the region in $\mathbb{R}^2$ that is inside the curve with polar equation $$r = 1 + \cos\theta$$ but outside the curve with polar equation $$r = 3 \cos\theta$$.

_Hint_: Sketch the required region first.

> $$\begin{aligned}
> & \text{The 1st curve }[0, 2\pi)\text{ is a cardioid, with the cusp facing the left.} \\
> & \text{The 2nd curve on }\left[0, \frac\pi 2 \right)\text{ is the upper half of the circle, with the leftmost point of the circle touching the origin.} \\
> & \text{The 2nd curve on }\left[\frac {3\pi} 2, 2\pi \right)\text{ is the lower half of the circle, with the leftmost point of the circle touching the origin.} \\
> & \text{The 2nd curve on }\left[\frac \pi 2, \frac {3\pi} 2 \right)\text{ contains negative }r\text{ and is ignored.} \\
> & \text{For }\left[0, \frac \pi 2 \right)\text{, there is 1 and only 1 intersection point excluding the origin.} \\
> & \begin{aligned} 1 + \cos \theta & = 3 \cos \theta \\
> \cos \theta & = \frac 1 2 \\
> \theta & = \frac \pi 3 && \theta \in \left[0, \frac \pi 2 \right) \end{aligned} \\
> & \text{For }\left[\frac {3\pi} 2, 2\pi \right)\text{, there is 1 and only 1 intersection point excluding the origin.} \\
> & \begin{aligned}
> 1 + \cos \theta & = 3 \cos \theta \\
> \cos \theta & = \frac 1 2 \\
> \theta & = \frac {5 \pi} 3 && \theta \in \left[\frac {3\pi} 2, 2\pi \right) \end{aligned} \\
> & \text{For intersections at the origin,} \\
> & \begin{aligned} 1 + \cos \theta & = 0 \\
> \cos \theta & = - 1 \\
> \theta & = \pi && \theta \in [0, 2\pi) \\
> 3 \cos \theta & = 0 \\
> \cos \theta & = 0 \\
> \theta & \in \set{\frac \pi 2, \frac {3 \pi} 2} && \theta \in [0, 2\pi) \end{aligned} \\
> & \text{Therefore, the area is...} \\
> & \begin{aligned} & \phantom{=} \int \! (1 + \cos \theta)^2 \,\mathrm{d}\theta \\
> & = \int \! \left(1 + 2 \cos \theta + \cos^2 \theta \right) \,\mathrm{d}\theta \\
> & = \int \! \left(1 + 2 \cos \theta + \frac 1 2 \cos 2\theta + \frac 1 2 \right) \,\mathrm{d}\theta \\
> & = \frac 3 2 \theta + 2 \sin \theta + \frac 1 4 \sin 2\theta + C \\
> & \phantom{=} \int \! (3 \cos \theta)^2 \,\mathrm{d}\theta \\
> & = \int \! 9 \cos^2 \theta \,\mathrm{d}\theta \\
> & = \int \! \left(\frac 9 2 \cos 2\theta + \frac 9 2 \right) \,\mathrm{d}\theta \\
> & = \frac 9 2 \theta + \frac 9 4 \sin 2\theta + C \\
> & \phantom{=} \int \! ((1 + \cos \theta)^2 - (3 \cos \theta)^2) \,\mathrm{d}\theta \\
> & = \int \! (1 + \cos \theta)^2 \,\mathrm{d}\theta - \int \! (3 \cos \theta)^2 \,\mathrm{d}\theta \\
> & = \frac 3 2 \theta + 2 \sin \theta + \frac 1 4 \sin 2\theta - \frac 9 2 \theta - \frac 9 4 \sin 2\theta + C \\
> & = -3 \theta + 2 \sin \theta - 2 \sin 2\theta + C \\
> & \phantom{=} \text{area} \\
> & = \frac 1 2 \left( \int_{\frac \pi 3}^{\frac \pi 2} \! \left((1 + \cos \theta)^2 - (3 \cos \theta)^2 \right) \,\mathrm{d}\theta + \int_{\frac \pi 2}^{\frac {3\pi} 2} \! (1 + \cos \theta)^2 \,\mathrm{d}\theta + \int_{\frac {3\pi} 2}^{\frac {5\pi} 2} \! \left((1 + \cos \theta)^2 - (3 \cos \theta)^2 \right) \,\mathrm{d}\theta \right) \\
> & = \frac 1 2 \left([-3 \theta + 2 \sin \theta - 2 \sin 2\theta]_{\frac \pi 3}^{\frac \pi 2} + [-3 \theta + 2 \sin \theta - 2 \sin 2\theta]_{\frac {3\pi} 2}^{\frac {5\pi} 3} + \left[\frac 3 2 \theta + 2 \sin \theta + \frac 1 4 \sin 2\theta \right]_{\frac \pi 2}^{\frac {3 \pi} 2} \right) \\
> & = \frac 1 2 \left(-3 \left(\frac \pi 2 - \frac \pi 3 + \frac {5\pi} 3 - \frac {3\pi} 2 \right) + 2 \left(\sin \frac \pi 2 - \sin \frac \pi 3 + \sin \frac {5\pi} 3 - \sin \frac {3\pi} 2 \right) - 2 \left(\sin \pi - \sin \frac {2\pi} 3 + \sin \frac {10\pi} 3 - \sin 3\pi \right) \right. \\
> & \phantom{=} \left. + \frac 3 2 \left(\frac {3\pi} 2 - \frac \pi 2 \right) + 2 \left(\sin \frac {3\pi} 2 - \sin \frac \pi 2 \right) + \frac 1 4 (\sin 3\pi - \sin \pi) \right) \\
> & = \frac 1 2 \left(-3 \cdot \frac \pi 3 + 2 \left(1 - \frac {\sqrt 3} 2 - \frac {\sqrt 3} 2 + 1 \right) - 2 \left(0 - \frac {\sqrt 3} 2 - \frac {\sqrt 3} 2 - 0 \right) + \frac {3\pi} 2 + 2 (-1 - 1) + \frac 1 4 (0 - 0) \right) \\
> & = \frac 1 2 \left(-\pi + 4 - 2 \sqrt 3 + 2 \sqrt 3 + \frac {3 \pi} 2 - 4 \right) \\
> & = \frac 1 2 \cdot \frac \pi 2 \\
> & = \frac \pi 4 \end{aligned}
> \end{aligned}

<!--
> $$\begin{aligned}
> & \text{The integration domain for the 1st curve is }\left[\frac \pi 3, \frac {5\pi} 3\right]\text{.} \\
> & \text{The integration domain for the 2nd curve is }\left[\frac \pi 3, \frac \pi 2\right] \cup \left[\frac {3\pi} 2, \frac {5\pi} 3\right]\text{.} \\
> & \text{Therefore, the area is...} \\
> & \begin{aligned} & \phantom{=} \text{area} \\
> & = \frac 1 2 \int_0^{\frac {2\pi} 3} \! \left(\left(1 + \cos\left(\frac \pi 3 + \theta\right)\right)^2 - \left(3 \cos\left(\frac \pi 3 + \frac \theta 4\right)\right)^2 \right) \,\mathrm{d}\theta + \frac 1 2 \int_0^{\frac {2\pi} 3} \! \left(\left(1 + \cos (\pi + \theta)\right)^2 - \left(3 \cos\left(\frac {3\pi} 2 + \frac \theta 4\right)\right)^2 \right) \,\mathrm{d}\theta \\
> & = \int_0^{\frac {2\pi} 3} \! \left(\left(1 + \cos\left(\frac \pi 3 + \theta\right)\right)^2 - \left(3 \cos\left(\frac \pi 3 + \frac \theta 4\right)\right)^2 \right) \,\mathrm{d}\theta && (\text{symmetry}) \\
> & = \int_0^{\frac {2\pi} 3} \! \left(1 + 2 \cos\left(\frac \pi 3 + \theta \right) + \cos^2 \left(\frac \pi 3 + \theta \right) - 9 \cos^2 \left(\frac \pi 3 + \frac \theta 4 \right) \right) \,\mathrm{d}\theta \\
> & = \int_0^{\frac {2\pi} 3} \! \left(1 + 2 \cos\left(\frac \pi 3 + \theta \right) + \frac 1 2 \cos \left(\frac {2\pi} 3 + 2\theta \right) + \frac 1 2 - \frac 9 2 \cos \left(\frac {2\pi} 3 + \frac \theta 2 \right) - \frac 9 2 \right) \,\mathrm{d}\theta \\
> & = \int_0^{\frac {2\pi} 3} \! \left(-3 + 2 \cos\left(\frac \pi 3 + \theta \right) + \frac 1 2 \cos \left(\frac {2\pi} 3 + 2\theta \right) - \frac 9 2 \cos \left(\frac {2\pi} 3 + \frac \theta 2 \right) \right) \,\mathrm{d}\theta \\
> & = \left[-3\theta + 2 \sin\left(\frac \pi 3 + \theta \right) + \frac 1 4 \sin\left(\frac {2\pi} 3 + 2\theta \right) - 9 \sin \left(\frac {2\pi} 3 + \frac \theta 2 \right) \right]_0^{\frac {2\pi} 3} \\
> & = -2\pi + 2\left(\sin \pi - \sin \frac \pi 3 \right) + \frac 1 4 \left(\sin 2\pi - \sin \frac {2\pi} 3 \right) - 9 \left(\sin \pi - \sin \frac {2\pi} 3 \right) \\
> & = -2\pi + 2 \left(0 - \frac {\sqrt 3} 2\right) + \frac 1 4 \left(0 - \frac {\sqrt 3} 2 \right) - 9 \left(0 - \frac {\sqrt 3} 2 \right) \\
> & = -2\pi - \sqrt 3 - \frac {\sqrt 3} 8 + \frac {9 \sqrt 3} 2 \\
> & = -2\pi + \frac {27 \sqrt 3} {8} \end{aligned}
> \end{aligned}$$
-->

## Q5

Let $f: [0, \pi] \to [0, +\infty)$ be a continuously differentiable function, and consider the curve in $\mathbb{R}^2$ defined by the polar equation $$r = f(\theta)$$.

Such a curve can be viewed as a polar curve on the one hand, and as a parameterized curve on the other hand. Show that the area bounded between the curve and the $x$-axis evaluated using Theorem 7.98 (as a polar curve) is the same as that evaluated using Theorem 7.96 (as a parameterized curve).

> $$\begin{aligned}
> f(\theta) & \text{ is a nonnegative continuous function.} \\
> A_1 & := \frac 1 2 \int_0^\pi \! f(\theta)^2 \,\mathrm{d}\theta && (\text{theorem 7.98}) \\
> f(\theta) \in C^1([0, \pi]) & \implies \text{the curve is }C^1\text{ smooth} \\
> A_2 & := -\int_0^\pi \! (f(\theta) \sin \theta) (f(\theta) \cos \theta)' \,\mathrm{d}\theta && (\text{theorem 7.96}, f(\theta) \in C^1([0, \pi]) \\
> & = \int_0^\pi \! (f(\theta) \sin \theta)(f(\theta) \sin \theta - f'(\theta) \cos\theta) \,\mathrm{d}\theta && \left(f(\theta) \in C^1([0, \pi]) \right) \\
> & = \int_0^\pi \! \left(f(\theta)^2 \sin^2 \theta - f(\theta) f'(\theta) \sin \theta \cos \theta \right) \,\mathrm{d}\theta \\
> & = \int_0^\pi \! f(\theta)^2 \,\mathrm{d}\theta - \int_0^\pi \! \left(f(\theta)^2 \cos^2 \theta + f(\theta) f'(\theta) \sin\theta \cos\theta \right) \,\mathrm{d}\theta \\
> & = \int_0^\pi \! f(\theta)^2 \,\mathrm{d}\theta - \int_0^\pi \! (f(\theta) \cos \theta)\left(f(\theta) \cos \theta + f'(\theta) \sin \theta \right) \,\mathrm{d}\theta \\
> & = \int_0^\pi \! f(\theta)^2 \,\mathrm{d}\theta - \int_0^\pi \! (f(\theta) \cos\theta) (f(\theta) \sin\theta)' \,\mathrm{d}\theta \\
> & = \int_0^\pi \! f(\theta)^2 \,\mathrm{d}\theta - \left[f(\theta)^2 \sin \theta \cos \theta \right]_0^\pi + \int_0^\pi \! (f(\theta) \sin \theta) (f(\theta) \cos \theta)' \,\mathrm{d}\theta \\
> & = \int_0^\pi \! f(\theta)^2 \,\mathrm{d}\theta - \left[f(\theta)^2 \sin \theta \cos \theta \right]_0^\pi - A_2 \\
> 2 A_2 & = \int_0^\pi \! f(\theta)^2 \,\mathrm{d}\theta - \left[f(\theta)^2 \sin \theta \cos \theta \right]_0^\pi \\
> & = \int_0^\pi \! f(\theta)^2 \,\mathrm{d}\theta - (0 - 0) \\
> A_2 & = \frac 1 2 \int_0^\pi \! f(\theta)^2 \,\mathrm{d}\theta \\
> & = A_1
> \end{aligned}$$

## Q8

Consider the region in the coordinate plane bounded by the curve $$y = e^{-x}$$, the $x$- and $y$-axes, and the line $x = \ln 2$. Find the volume of the solid obtained by revolving this region about the line $x = \ln 2$.

> $$\begin{aligned}
> y & = e^{-0} \\
> & = 1 \\
> \\
> y & = e^{-\ln 2} \\
> & = \frac 1 2 \\
> \\
> y & = e^{-x} \\
> \ln y & = -x \\
> x & = -\ln y \\
> \\
> & \phantom{=} \int \! \ln y \,\mathrm{d}y \\
> & = y \ln y - \int \! \frac y y \,\mathrm{d}y \\
> & = y (\ln y - 1) + C \\
> \\
> & \phantom{=} \int \! (\ln y)^2 \,\mathrm{d}y \\
> & = y (\ln y)^2 - 2 \int \! \frac {y \ln y} y \,\mathrm{d}y \\
> & = y (\ln y)^2 - 2 \int \! \ln y \,\mathrm{d}y \\
> & = y (\ln y)^2 - 2 y(\ln y - 1) + C \\
> & = y \left((\ln y)^2 - 2 \ln y + 2 \right) + C \\
> \\
> & \phantom{=} \text{volume} \\
> & = \pi \left( \int_0^{\frac 1 2} \! \left(\ln 2 - 0 \right)^2 \,\mathrm{d}y + \int_{\frac 1 2}^1 \left((\ln 2 - 0)^2 - (\ln 2 + \ln y)^2 \right) \,\mathrm{d}y \right) \\
> & = \pi \left( \int_0^{\frac 1 2} \! (\ln 2)^2 \,\mathrm{d}y + \int_{\frac 1 2}^1 \! \left((\ln 2)^2 - (\ln 2)^2 - 2 \ln 2 \ln y - (\ln y)^2 \right) \,\mathrm{d}y \right) \\
> & = \pi \left( \frac 1 2 (\ln 2)^2 - 2 \ln 2 [y(\ln y - 1)]_{\frac 1 2}^1 - \left[y\left((\ln y)^2 - 2 \ln y + 2 \right) \right]_{\frac 1 2}^1 \right) \\
> & = \pi \left( 0.5 (\ln 2)^2 - 2 \ln 2 (1(0 - 1) - 0.5(-\ln 2 - 1)) - \left(1(0 - 0 + 2) - 0.5\left((\ln 2)^2 + 2 \ln 2 + 2 \right) \right) \right) \\
> & = \pi \left( 0.5 (\ln 2)^2 + 2 \ln 2 - \ln 2(\ln 2 + 1) - 2 + 0.5(\ln 2)^2 + \ln 2 + 1 \right) \\
> & = \pi \left( (\ln 2)^2 + 3 \ln 2 - 1 - (\ln 2)^2 - \ln 2 \right) \\
> & = \pi \left( 2 \ln 2 - 1 \right)
> \end{aligned}$$

## Q14

Let $f: [1, +\infty) \to [0, +\infty)$ be the function $$f(x) = \frac 1 x$$ and consider its graph in the plane.

### Q14.a

Consider the (unbounded) region under the graph of $f$ and above the $x$-axis. Show that the solid obtained by revolving this region about the $x$-axis has a finite volume.

> $$\begin{aligned}
> & \phantom{=} \text{volume} \\
> & = \pi \int_1^{+\infty} \! \left(\frac 1 x\right)^2 \,\mathrm{d}x \\
> & = \pi \int_1^{+\infty} \! \frac 1 {x^2} \,\mathrm{d}x \\
> & \text{By the }p\text{-test, the integral is convergent.} \\
> & \text{So the volume is finite.}
> \end{aligned}$$

### Q14.b

Show that the surface obtained revolving the graph of $f$ about the $x$-axis has an infinite surface area.

> $$\begin{aligned}
> & \phantom{=} \text{surface area} \\
> & = 2\pi \int_1^{+\infty} \! \frac 1 x \sqrt{1 + \left(\left(\frac 1 x \right)' \right)^2} \,\mathrm{d}x \\
> & = 2\pi \int_1^{+\infty} \! \frac 1 x \sqrt{1 + \left(- \frac 1 {x^2}\right)^2 } \,\mathrm{d}x \\
> & = 2\pi \int_1^{+\infty} \! \frac 1 x \sqrt{1 + \frac 1 {x^4} } \,\mathrm{d}x \\
> & > 2\pi \int_1^{+\infty} \! \frac 1 x \,\mathrm{d}x && \left(x \in [1, +\infty) \implies \sqrt{1 + \frac 1 {x^4} } > 1 \right) \\
> & \text{By the }p\text{-test, the integral one line above this line is divergent.} \\
> & \text{By the comparison test, the original integral is divergent.} \\
> & \text{So the surface area is infinite.}
> \end{aligned}

## Q15

Let $\mathbf{r}: [0, 2\pi] \to \mathbb{R}^2$ be the curve defined by $$\mathbf{r}(t) = \langle \cos^3 t, \sin^3 t \rangle$$.

### Q15.a

Find the arc-length of this curve.

> $$\begin{aligned}
> & \phantom{=} \mathbf{r}'(t) \\
> & = \left\langle -3 \cos^2 t \sin t, 3 \sin^2 t \cos t \right\rangle \\
> & \phantom{=} \text{arc-length} \\
> & = \int_0^{2\pi} \! \lVert \mathbf{r}'(t) \rVert \,\mathrm{d}t \\
> & = \int_0^{2\pi} \! \sqrt{9 \cos^4 t \sin^2 t + 9 \sin^4 t \cos^2 t} \,\mathrm{d}t \\
> & = 3 \int_0^{2\pi} \! \lvert \sin t \cos t \rvert \sqrt{\cos^2 + \sin^2 t} \,\mathrm{d}t \\
> & = 3 \int_0^{2\pi} \! \lvert \sin t \cos t \rvert \,\mathrm{d}t \\
> & = \frac 3 2 \int_0^{2\pi} \! \lvert \sin 2t \rvert \,\mathrm{d}t \\
> & = \frac 3 4 \int_0^{4\pi} \! \lvert \sin t \rvert \,\mathrm{d}t && (\text{change of variable }2t \mapsto t) \\
> & = 3 \int_0^\pi \! \sin t \,\mathrm{d}t && (\text{symmetry}, (\forall t \in [0, \pi])(\sin t \ge 0)) \\
> & = 3 [-\cos t]_0^\pi \\
> & = 6
> \end{aligned}$$

### Q15.b

Find the area of the region in $\mathbb{R}^2$ bounded by this curve.

> $$\begin{aligned}
> & \text{The curve is a smooth curve.} \\
> & \phantom{=} \text{area} \\
> & = \int_0^{2\pi} \! \cos^3 t \left(\sin^3 t \right)' \,\mathrm{d}t \\
> & = 3 \int_0^{2\pi} \! \cos^4 t \sin^2 t \,\mathrm{d}t \\
> & = \frac 3 8 \int_0^{2\pi} \! (\cos 2t + 1) \sin^2 2t \,\mathrm{d}t \\
> & = \frac 3 8 \int_0^{2\pi} \! (\cos 2t + 1) \sin^2 2t \,\mathrm{d}t \\
> & = \frac 3 {16} \int_0^{4\pi} \! (\cos t + 1) \sin^2 t \,\mathrm{d}t && (\text{change of variable }2t \mapsto t) \\
> & = \frac 3 {16} \left[\frac 1 3 \sin^3 t \right]_0^{4\pi} + \frac 3 {16} \int_0^{4\pi} \! \sin^2 t \,\mathrm{d}t \\
> & = \frac 3 {32} \int_0^{4\pi} \! (1 - \cos 2t) \,\mathrm{d}t \\
> & = \frac 3 {32} \left[\theta - \frac 1 2 \sin 2t \right]_0^{4\pi} \\
> & = \frac {3\pi} 8 - \frac 3 {64} (\sin 8\pi - \sin 0) \\
> & = \frac {3\pi} 8
> \end{aligned}$$

### Q15.c

Find the volume of the solid obtained by revolving this curve about the $x$-axis.

> $$\begin{aligned}
> & \text{The curve is a 4-folded symmetric star.} \\
> & \text{By symmetry, we only need to find the volume by considering one quadrant of the star.} \\
> & \text{Considering quadrant I,} \\
> x & = \cos^3 t \\
> y & = \sin^3 t \\
> & = \left(\sin^2 t \right)^{\frac 3 2} && (y \ge 0 \implies \sin t \ge 0) \\
> & = \left(1 - \cos^2 t \right)^{\frac 3 2} \\
> & = \left(1 - x^{\frac 2 3} \right)^{\frac 3 2} && (x \ge 0 \implies \cos t \ge 0) \\
> \\
> & \phantom{=} \text{volume} \\
> & = 2\pi \int_0^1 \! y^2 \,\mathrm{d}x \\
> & = 2\pi \int_0^1 \! \left(1 - x^{\frac 2 3} \right)^3 \,\mathrm{d}x \\
> & = 2\pi \int_0^1 \! \left(1 - 3x^{\frac 2 3} + 3x^{\frac 4 3} - x^2 \right) \,\mathrm{d}x \\
> & = 2\pi \left[x - \frac 9 5 x^{\frac 5 3} + \frac 9 7 x^{\frac 7 3} - \frac 1 3 x^3 \right]_0^1 \\
> & = 2\pi \left(1 - \frac 9 5 + \frac 9 7 - \frac 1 3 \right) \\
> & = 2\pi \cdot \frac {105 - 189 + 135 - 35} {105} \\
> & = 2\pi \cdot \frac {16} {105} \\
> & = \frac {32\pi} {105}
> \end{aligned}$$

### Q15.d

Find the area of the surface obtained by revolving this curve about the $x$-axis.

> $$\begin{aligned}
> & \text{The curve is a 4-folded symmetric star.} \\
> & \text{By symmetry, we only need to the surface area using one quadrant of the star.} \\
> & \text{Considering quadrant I,} \\
> x & = \cos^3 t \\
> y & = \sin^3 t \\
> & = \left(\sin^2 t \right)^{\frac 3 2} && (y \ge 0 \implies \sin t \ge 0) \\
> & = \left(1 - \cos^2 t \right)^{\frac 3 2} \\
> & = \left(1 - x^{\frac 2 3} \right)^{\frac 3 2} && (x \ge 0 \implies \cos t \ge 0) \\
> y' & = \frac 3 2 \left(1 - x^{\frac 2 3} \right)^{\frac 1 2} \left(- \frac 2 3 x^{-\frac 1 3} \right) \\
> & = -\left(1 - x^{\frac 2 3} \right)^{\frac 1 2} x^{-\frac 1 3}
> \\
> & \phantom{=} \text{surface area} \\
> & = 4\pi \int_0^1 \! y \sqrt{1 + (y')^2} \,\mathrm{d}x \\
> & = 4\pi \int_0^1 \! \left(1 - x^{\frac 2 3} \right)^{\frac 3 2} \sqrt{1 + \left(1 - x^{\frac 2 3} \right)x^{-\frac 2 3} } \,\mathrm{d}x \\
> & = 4\pi \int_0^1 \! \left(1 - x^{\frac 2 3} \right)^{\frac 3 2} x^{-\frac 1 3} \,\mathrm{d}x \\
> & = 6\pi \int_0^1 \! (1 - x)^{\frac 3 2} \,\mathrm{d}x && \left(\text{change of variable } x^{\frac 2 3} \to x\right) \\
> & = 6\pi \left[-\frac 2 5 (1 - x)^{\frac 5 2} \right]_0^1 \\
> & = \frac {12\pi} 5
> \end{aligned}$$

## Q16

Consider the cardioid in $\mathbb{R}^2$ defined by the polar equation $$r = 1 + \sin \theta$$.

_Hint_: The given cardioid is symmetric about the $y$-axis. To generate a solid or a surface by revolving about the $y$-axis, we only need the __right-half__ of the cardioid.

### Q16.a

Find the volume of the solid obtained by revolving this curve about the $y$-axis.

> $$\begin{aligned}
> & r\text{ is always nonnegative because }\sin \theta \ge -1\text{.} \\
> & \text{As the cardioid is symmetric about the }y\text{-axis,} \\
> & \text{only considering the right-half...} \\
> & \phantom{=} \text{volume} \\
> & = \pi \int_{-\frac \pi 2}^{\frac \pi 2} \! x^2 \mathrm{d}y \\
> & = \pi \int_{-\frac \pi 2}^{\frac \pi 2} \! x^2 y' \mathrm{d}\theta \\
> & = \pi \int_{-\frac \pi 2}^{\frac \pi 2} \! r^2 \cos^2 \theta (r' \sin \theta + r \cos \theta) \,\mathrm{d}\theta \\
> & = \pi \int_{-\frac \pi 2}^{\frac \pi 2} \! (1 + \sin \theta)^2 \cos^2 \theta (2 \cos \theta \sin \theta + \cos \theta) \,\mathrm{d}\theta \\
> & = \pi \int_{-\frac \pi 2}^{\frac \pi 2} \! (1 + \sin \theta)^2 \left(1 - \sin^2 \theta \right) (2 \sin \theta + 1) \cos \theta \,\mathrm{d}\theta \\
> & = \pi \int_{-1}^1 \! (1 + u)^3 (1 - u) (2u + 1) \,\mathrm{d}u && (\text{substitute }u := \sin \theta) \\
> & = \pi \int_0^2 \! u^3 (2 - u) (2u - 1) \,\mathrm{d}u && (\text{change of variable }1 + u \mapsto u) \\
> & = \pi \int_0^2 \! u^3 \left(4u - 2 - 2u^2 + u \right) \,\mathrm{d}u \\
> & = \pi \int_0^2 \! u^3 \left(-2u^2 + 5u - 2\right) \,\mathrm{d}u \\
> & = \pi \int_0^2 \! \left(-2u^5 + 5u^4 - 2u^3 \right) \,\mathrm{d}u \\
> & = \pi \left[-\frac 1 3 u^6 + u^5 - \frac 1 2 u^4 \right]_0^2 \\
> & = \pi \left(-\frac 1 3 (64) + 32 - \frac 1 2 (16) \right) \\
> & = \pi \left(-\frac {64} 3 + 32 - 8\right) \\
> & = \frac {8\pi} {3}
> \end{aligned}$$

### Q16.b

Find the area of the surface obtained by revolving this curve about the $y$-axis.

> $$\begin{aligned}
> & r\text{ is always nonnegative because }\sin \theta \ge -1\text{.} \\
> & \text{As the cardioid is symmetric about the }y\text{-axis,} \\
> & \text{only considering the right-half...} \\
> & \phantom{=} \text{surface area} \\
> & = 2\pi \int_{-\frac \pi 2}^{\frac \pi 2} \! x \sqrt{r^2 + r'^2} \,\mathrm{d}\theta \\
> & = 2\pi \int_{-\frac \pi 2}^{\frac \pi 2} \! \sqrt{r^2 - y^2} \sqrt{r^2 + r'^2} \,\mathrm{d}\theta && (x \ge 0) \\
> & = 2\pi \int_{-\frac \pi 2}^{\frac \pi 2} \! \sqrt{r^2 - r^2 \sin^2 \theta} \sqrt{r^2 + r'^2} \,\mathrm{d}\theta \\
> & = 2\pi \int_{-\frac \pi 2}^{\frac \pi 2} \! \lvert r \cos \theta \rvert \sqrt{r^2 + r'^2} \,\mathrm{d}\theta \\
> & = 2\pi \int_{-\frac \pi 2}^{\frac \pi 2} \! (1 + \sin \theta) \cos \theta \sqrt{1 + 2\sin \theta + \sin^2 \theta + \cos^2 \theta} \,\mathrm{d}\theta && \left(r \ge 0, \left(\forall \theta \in \left[-\frac \pi 2, \frac \pi 2\right]\right)(\cos \theta \ge 0)\right) \\
> & = 2\pi \int_{-\frac \pi 2}^{\frac \pi 2} \! (1 + \sin \theta) \cos \theta \sqrt{2 + 2 \sin \theta} \,\mathrm{d}\theta \\
> & = 2\pi \sqrt 2 \int_{-\frac \pi 2}^{\frac \pi 2} \! (1 + \sin \theta) \cos \theta \sqrt{1 + \sin \theta} \,\mathrm{d}\theta \\
> & = 2\pi \sqrt 2 \int_0^2 u^{\frac 3 2} \,\mathrm{d}u && (\text{substitute }u := \sin \theta + 1) \\
> & = 2\pi \sqrt 2 \left[\frac 2 5 u^{\frac 5 2} \right]_0^2 \\
> & = 2\pi \sqrt 2 \cdot \frac 2 5 \cdot 4 \sqrt 2 \\
> & = \frac {32 \pi} 5
> \end{aligned}$$

## Q17

Determine whether each of the following series of real numbers converges or diverges. Also compute its limit (i.e. the sum) if it converges.

### Q17.b

$$\sum_{k = 1}^{+\infty} \frac 2 {k (k + 1) (k + 2)}$$

> $$\begin{aligned}
> & \phantom{=} \sum_{k = 1}^n \frac 2 {k(k + 1) (k + 2)} && (n \in \mathbb{Z}_{\ge 1}) \\
> & = \sum_{k = 1}^n \left(\frac 1 {k (k + 1)} - \frac 1 {(k + 1) (k + 2)} \right) \\
> & = \frac 1 {1 \cdot 2} - \frac 1 {(n + 1) (n + 2)} && (\text{telescope}) \\
> & = \frac 1 2 - \frac 1 {(n + 1) (n + 2)} \\
> & \phantom{=} \sum_{k = 1}^{+\infty} \frac 2 {k (k + 1) (k + 2)} \\
> & = \lim_{n \to +\infty} \sum_{k = 1}^n \frac 2 {k(k + 1) (k + 2)} \\
> & = \lim_{n \to +\infty} \left(\frac 1 2 - \frac 1 {(n + 1) (n + 2)} \right) \\
> & = \frac 1 2 - 0 \\
> & = \frac 1 2 \\
> & \therefore \text{The limit converges.}
> \end{aligned}$$

### Q17.c

$$\sum_{k = 1}^{+\infty} \ln \left(1 + \frac 1 k\right)$$

> $$\begin{aligned}
> & \phantom{=} \sum_{k = 1}^n \ln \left(1 + \frac 1 k \right) && (n \in \mathbb{Z}_{\ge 1}) \\
> & = \ln \left(\prod_{k = 1}^n \left(1 + \frac 1 k \right) \right) \\
> & = \ln \left(\prod_{k = 1}^n \frac 1 k \left(k + 1 \right) \right) \\
> & = \ln \left(\frac {(n + 1)!} {n!} \right) \\
> & = \ln(n + 1) \\
> & \phantom{=} \sum_{k = 1}^{+\infty} \ln \left(1 + \frac 1 k\right) \\
> & = \lim_{n \to +\infty} \sum_{k = 1}^n \ln \left(1 + \frac 1 k \right) \\
> & = \lim_{n \to +\infty} \ln(n + 1) \\
> & = +\infty \\
> & \therefore \text{The limit diverges.}
> \end{aligned}$$

### Q17.e

$$\sum_{k = 2}^{+\infty} \frac k {2^{k - 1} }$$

_Hint_: $\frac{\mathrm{d} }{\mathrm{d}x} x^k = k x^{k - 1}$.

> $$\begin{aligned}
> f_k(x) & := x^k \\
> f_k'(x) & = kx^{k - 1} \\
> & \phantom{=} \sum_{k = 2}^n \frac k {2^{k - 1} } && (n \in \mathbb{Z}_{\ge 2}) \\
> & = \sum_{k = 2}^n k \left(\frac 1 2 \right)^{k - 1} \\
> & = \sum_{k = 2}^n f_k'\left(\frac 1 2 \right) \\
> & = \left. \left(\sum_{k = 2}^n f_k(x) \right)' \right|_{x = \frac 1 2} && (\text{linearity}) \\
> & = \left. \left(\sum_{k = 2}^n x^k \right)' \right|_{x = \frac 1 2} \\
> & = \left. \left(\frac {x^{n + 1} - x^2} {x - 1} \right)' \right|_{x = \frac 1 2} \\
> & = \left. \left( x^2 \left(\frac {x^{n - 1} - 1} { x - 1} \right) \right)' \right|_{x = \frac 1 2} \\
> & = \left. \left((2x) \frac {x^{n - 1} - 1} {x - 1} + x^2 \left(\frac {(n - 1) x^{n - 2} (x - 1) - \left(x^{n - 1} - 1 \right)} {(x - 1)^2} \right) \right) \right|_{x = \frac 1 2} \\
> & = 2(0.5) \frac {0.5^{n - 1} - 1} {0.5 - 1} + (0.5)^2 \left(\frac {(n - 1) (0.5)^{n - 2} (0.5 - 1) - \left(0.5^{n - 1} - 1 \right)} {(0.5 - 1)^2} \right) \\
> & = 2\left(1 - 0.5^{n - 1} \right) + \left(-(n - 1) (0.5)^{n - 1} + \left(1 - 0.5^{n - 1} \right) \right) \\
> & = 3\left(1 - 0.5^{n - 1} \right) - (n - 1) (0.5)^{n - 1} \\
> & = 3 - 3 (0.5)^{n - 1} - n (0.5)^{n - 1} + 0.5^{n - 1} \\
> & = 3 - 2^{1 - n}(n + 2) \\
> & \phantom{=} \sum_{k = 2}^{+\infty} \frac k {2^{k - 1} } \\
> & = \lim_{n \to +\infty} \sum_{k = 2}^n \frac k {2^{k - 1} } \\
> & = \lim_{n \to +\infty} \left(3 - 2^{1 - n}(n + 2) \right) \\
> & = 3 - 0 && (\text{exponential is faster growing than linear}) \\
> & = 3 \\
> & \therefore \text{The limit converges.}
> \end{aligned}$$
