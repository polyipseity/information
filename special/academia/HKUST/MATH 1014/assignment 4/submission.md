---
aliases:
  - HKUST MATH 1014 L1 assignment 4 submission
tags:
  - date/2024/03/26
  - language/in/English
---

# L1 assignment 4 submission

- HKUST MATH 1014

MATH1014 Calculus II Problem Set 4<br/>
L01 (Spring 2024)

Problem Set 4

Note: The problem sets serve as additional exercise problems for your own practice. Problem Set 4 covers materials from §6.4 – §6.6.

## Q2

Evaluate the following antiderivatives.

## Q2.b

$$\int \! \ln\left( x^3 + 1 \right) \,\mathrm{d}x$$

> $$\begin{aligned}
> & \phantom{=} \int \! \ln\left( x^3 + 1 \right) \,\mathrm{d}x \\
> & = \int \! \ln \left( (x + 1) \left(x^2 - x + 1 \right) \right) \,\mathrm{d}x \\
> & = \int \! \left( \ln(x + 1) + \ln\left(x^2 - x + 1\right) \right) \,\mathrm{d}x \\
> & = \int \! \ln(x + 1) \,\mathrm{d}x + \int \! \ln\left(x^2 - x + 1 \right) \,\mathrm{d}x \\
> & = \int \! \ln(x + 1) \,\mathrm{d}(x + 1) + \int \! \ln\left(x^2 - x + 1 \right) \,\mathrm{d}x \\
> & = (x + 1)\ln(x + 1) - \int \! (x + 1) \,\mathrm{d}\ln(x + 1) + x\ln\left(x^2 - x + 1\right) - \int \! x \,\mathrm{d}\ln\left(x^2 - x + 1\right) \\
> & = (x + 1)\ln(x + 1) - \int \,\mathrm{d}x + x\ln\left(x^2 - x + 1\right) - \int \! \frac {2x^2 - x} {x^2 - x + 1} \,\mathrm{d}x \\
> & = (x + 1)\ln(x + 1) - x + x\ln\left(x^2 - x + 1\right) - \int \! \left(2 + \frac 1 2 \frac {2x - 1} {x^2 - x + 1} - \frac 3 2 \frac 1 {\left(x - \frac 1 2\right)^2 + \frac 3 4} \right) \\
> & = (x + 1)\ln(x + 1) - x + x\ln\left(x^2 - x + 1\right) - 2x - \frac 1 2 \ln\left(x^2 - x + 1\right) + \frac 3 2 \frac {\sqrt 3} 2 \frac 4 3 \arctan\left(\left(x - \frac 1 2\right) \frac 2 {\sqrt 3} \right) + C \\
> & = (x + 1)\ln(x + 1) - 3x + \left(x - \frac 1 2\right)\ln\left(x^2 - x + 1\right) + \sqrt 3 \arctan\left(\frac {2x - 1} {\sqrt 3} \right) + C && (x > -1) \\
> \end{aligned}$$

## Q3

### Q3.a

Using the factorization $x^4 + 1 = \left(x^2 - \sqrt 2 x + 1\right) \left(x^2 - \sqrt 2 x + 1\right)$, evaluate $$\int \! \frac {x^2} {x^4 + 1} \,\mathrm{d}x$$.

> $$\begin{aligned}
> & \phantom{=} \int \! \frac {x^2} {x^4 + 1} \,\mathrm{d}x \\
> & = \int \! \frac {x^2} {\left(x^2 - \sqrt 2 x + 1\right) \left(x^2 + \sqrt 2 x + 1\right)} \,\mathrm{d}x \\
> & = \frac 1 {2\sqrt 2} \int \! \left(\frac x {x^2 - \sqrt 2 x + 1} - \frac x {x^2 + \sqrt 2 x + 1} \right) \,\mathrm{d}x \\
> & = \frac 1 {2\sqrt 2} \int \! \left(\frac 1 2 \frac {2x - \sqrt 2} {x^2 - \sqrt 2 x + 1} + \frac {\sqrt 2} 2 \frac 1 {x^2 - \sqrt 2 x + 1} - \frac 1 2 \frac {2x + \sqrt 2} {x^2 + \sqrt 2 x + 1} + \frac {\sqrt 2} 2 \frac 1 {x^2 + \sqrt 2 x + 1} \right) \,\mathrm{d}x \\
> & = \frac 1 {4\sqrt 2} \left(\ln\left\lvert x^2 - \sqrt 2 x + 1 \right\rvert - \ln\left\lvert x^2 + \sqrt 2 x + 1\right\rvert \right) + \frac 1 4 \int \! \left(\frac 1 {x^2 - \sqrt 2 x + 1} + \frac 1 {x^2 + \sqrt 2 x + 1} \right) \,\mathrm{d}x \\
> & = \frac 1 {4\sqrt 2} \left(\ln\left\lvert x^2 - \sqrt 2 x + 1 \right\rvert - \ln\left\lvert x^2 + \sqrt 2 x + 1\right\rvert \right) + \frac 1 4 \int \! \left(\frac 1 {\left(x - \frac 1 {\sqrt 2}\right)^2 + \frac 1 2} + \frac 1 {\left(x + \frac 1 {\sqrt 2}\right)^2 + \frac 1 2} \right) \,\mathrm{d}x \\
> & = \frac 1 {4\sqrt 2} \left(\ln\left\lvert x^2 - \sqrt 2 x + 1 \right\rvert - \ln\left\lvert x^2 + \sqrt 2 x + 1\right\rvert \right) + \frac 1 4 \left( \frac 1 {\sqrt 2} (2) \arctan\left(\left(x - \frac 1 {\sqrt 2}\right) \sqrt 2 \right) + \frac 1 {\sqrt 2} (2) \arctan\left(\left(x + \frac 1 {\sqrt 2}\right) \sqrt 2 \right) \right) + C \\
> & = \frac 1 {4\sqrt 2} \left(\ln\left\lvert x^2 - \sqrt 2 x + 1 \right\rvert - \ln\left\lvert x^2 + \sqrt 2 x + 1\right\rvert \right) + \frac 1 4 \left( \sqrt 2 \arctan\left(\sqrt 2 x - 1\right) + \sqrt 2 \arctan\left(\sqrt 2 x + 1\right) \right) + C \\
> & = \frac 1 {4\sqrt 2}\ln\left\lvert x^2 - \sqrt 2 x + 1 \right\rvert - \frac 1 {4\sqrt 2} \ln\left\lvert x^2 + \sqrt 2 x + 1\right\rvert + \frac 1 {2\sqrt 2} \arctan\left(\sqrt 2 x - 1\right) + \frac 1 {2\sqrt 2} \arctan\left(\sqrt 2 x + 1\right) + C
> \end{aligned}$$

### Q3.b

Using [(a)](#Q3.a) and the substitution $u = \sqrt{\tan x}$, evaluate $$\int_0^{\frac \pi 4} \sqrt{\tan x} \,\mathrm{d}x$$.

> $$\begin{aligned}
> & \phantom{=} \int_0^{\frac \pi 4} \! \sqrt{\tan x} \,\mathrm{d}x \\
> & = 2 \int_{\sqrt{\tan x} = 0}^{\sqrt{\tan x} = 1} \! \frac {\tan x} {\sec^2 x} \,\mathrm{d}\sqrt{\tan x} \\
> & = 2 \int_{\sqrt{\tan x} = 0}^{\sqrt{\tan x} = 1} \! \frac {\tan x} {\tan^2 x + 1} \,\mathrm{d}\sqrt{\tan x} \\
> & = 2 \int_0^1 \! \frac {u^2} {u^4 + 1} \,\mathrm{d}u \\
> & = 2 \left[\frac 1 {4\sqrt 2}\ln\left\lvert u^2 - \sqrt 2 u + 1 \right\rvert - \frac 1 {4\sqrt 2} \ln\left\lvert u^2 + \sqrt 2 u + 1\right\rvert + \frac 1 {2\sqrt 2} \arctan\left(\sqrt 2 u - 1\right) + \frac 1 {2\sqrt 2} \arctan\left(\sqrt 2 u + 1\right)\right]_0^1 \\
> & = 2 \left(\frac 1 {4\sqrt 2}\ln\left\lvert 1 - \sqrt 2 + 1 \right\rvert - \frac 1 {4\sqrt 2} \ln\left\lvert 1 + \sqrt 2 + 1\right\rvert + \frac 1 {2\sqrt 2} \arctan\left(\sqrt 2 - 1\right) + \frac 1 {2\sqrt 2} \arctan\left(\sqrt 2 + 1\right)\right) \\
> & = \frac 1 {2\sqrt 2}\ln\left\lvert 2 - \sqrt 2 \right\rvert - \frac 1 {2\sqrt 2} \ln\left\lvert 2 + \sqrt 2\right\rvert + \frac 1 {\sqrt 2} \arctan\left(\sqrt 2 - 1\right) + \frac 1 {\sqrt 2} \arctan\left(\frac 1 {\sqrt 2 - 1} \right) \\
> & = \frac 1 {2\sqrt 2}\ln\left\lvert 2 - \sqrt 2 \right\rvert - \frac 1 {2\sqrt 2} \ln\left\lvert 2 + \sqrt 2\right\rvert + \frac \pi {2\sqrt 2}
> \end{aligned}$$

## Q7

Let $a$ be a positive real number. Evaluate $$\int \! \frac 1 {1 - a \sin x} \,\mathrm{d}x$$ for each of the following cases:

### Q7.a

$0 < a < 1$ (for $x \in (-\pi, \pi)$),

> $$\begin{aligned}
> & \phantom{=} \int \! \frac 1 {1 - a \sin x} \,\mathrm{d}x \\
> & = \int \! \frac 1 {1 - a \frac {2t} {1 + t^2} } \frac {2 \,\mathrm{d}t} {1 + t^2} && \left(t := \tan\frac x 2, x \in (-\pi, \pi)\right) \\
> & = \int \! \frac 1 {\frac {1 + t^2 - 2at} {1 + t^2} } \frac {2 \,\mathrm{d}t} {1 + t^2} \\
> & = 2 \int \! \frac 1 {1 + t^2 - 2at} \,\mathrm{d}t \\
> & = 2 \int \! \frac 1 {(t - a)^2 + \left(1 - a^2\right)} \,\mathrm{d}t \\
> & = 2 \int \! \frac 1 {(t - a)^2 + \left(1 - a^2\right)} \,\mathrm{d}t && \left(0 < a < 1 \implies 1 - a^2 > 0\right) \\
> & = 2 \sqrt{1 - a^2} \frac 1 {1 - a^2} \arctan\left((t - a) \frac 1 {\sqrt{1 - a^2} } \right) + C \\
> & = \frac 2 {\sqrt{1 - a^2} } \arctan\left(\frac {t - a} {\sqrt{1 - a^2} }\right) + C \\
> & = \frac 2 {\sqrt{1 - a^2} } \arctan\left(\frac {\tan \frac x 2 - a} {\sqrt{1 - a^2} }\right) + C, x \in (-\pi, \pi)
> \end{aligned}$$

### Q7.b

$a = 1$,

> $$\begin{aligned}
> & \phantom{=} \int \! \frac 1 {1 - a \sin x} \,\mathrm{d}x \\
> & = \int \! \frac 1 {1 - \sin x} \,\mathrm{d}x && (a = 1) \\
> & = \int \! \frac 1 {1 - \frac {2t} {1 + t^2} } \frac {2 \,\mathrm{d}t} {1 + t^2} && \left(t := \tan\frac x 2, x \in (-\pi, \pi)\right) \\
> & = \int \! \frac 1 {\frac {1 + t^2 - 2t} {1 + t^2} } \frac {2 \,\mathrm{d}t} {1 + t^2} \\
> & = 2 \int \! \frac 1 {1 + t^2 - 2t} \,\mathrm{d}t \\
> & = 2 \int \! \frac 1 {(t - 1)^2} \,\mathrm{d}t \\
> & = -\frac 2 {t - 1} + C \\
> & = -\frac 2 {\tan \frac x 2 - 1} + C && (x \in (-\pi, \pi)) \\
> & \text{Notice that the integrand }\frac 1 {1 - \sin x}\text{ is periodic with a period of }2\pi\text{.} \\
> & \text{Further, the integrand has vertical asymptotes when }x = \frac \pi 2 + 2n\pi, n \in \mathbb{Z}\text{,} \\
> & \text{which separates each cycle, so we can extend the domain:} \\
> & \begin{cases} -\frac 2 {\tan \frac x 2 - 1} + C & x \ne \pi + 2n\pi \\
> \lim_{t \to \pm\infty} -\frac 2 {t - 1} = 0 & x = \pi + 2n\pi \end{cases}, x \ne \frac \pi 2 + 2n\pi, n \in \mathbb{Z}
> \end{aligned}$$

### Q7.c

$a > 1$.

> $$\begin{aligned}
> & \phantom{=} \int \! \frac 1 {1 - a \sin x} \,\mathrm{d}x \\
> & = \int \! \frac 1 {1 - a \frac {2t} {1 + t^2} } \frac {2 \,\mathrm{d}t} {1 + t^2} && \left(t := \tan\frac x 2, x \in (-\pi, \pi)\right) \\
> & = \int \! \frac 1 {\frac {1 + t^2 - 2at} {1 + t^2} } \frac {2 \,\mathrm{d}t} {1 + t^2} \\
> & = 2 \int \! \frac 1 {1 + t^2 - 2at} \,\mathrm{d}t \\
> & = 2 \int \! \frac 1 {(t - a)^2 + \left(1 - a^2\right)} \,\mathrm{d}t \\
> & = 2 \int \! \frac 1 {(t - a)^2 - \sqrt{a^2 - 1}^2} \,\mathrm{d}t && \left(a > 1 \implies a^2 - 1 > 0\right) \\
> & = 2 \int \! \frac 1 {\left(t - a - \sqrt{a^2 - 1}\right) \left(t - a + \sqrt{a^2 - 1}\right)} \,\mathrm{d}t \\
> & = \frac 1 {\sqrt{a^2 - 1} } \int \! \left(\frac 1 {t - a - \sqrt{a^2 - 1} } - \frac 1 {t - a + \sqrt{a^2 - 1} } \right) \,\mathrm{d}t \\
> & = \frac 1 {\sqrt{a^2 - 1} } \left(\ln \left\lvert t - a - \sqrt{a^2 - 1} \right\rvert + \ln \left\lvert t - a + \sqrt{a^2 - 1} \right\rvert \right) + C \\
> & = \frac 1 {\sqrt{a^2 - 1} } \ln \left\lvert \tan \frac x 2 - a - \sqrt{a^2 - 1} \right\rvert + \frac 1 {\sqrt{a^2 - 1} } \ln \left\lvert \tan \frac x 2 - a + \sqrt{a^2 - 1} \right\rvert + C, \\
> & \phantom{=} x \ne \pi + 2n\pi, \tan \frac x 2 \ne a + \sqrt{a^2 - 1}, \tan \frac x 2 \ne a - \sqrt{a^2 - 1}
> \end{aligned}$$

## Q10

Let $f: [0, +\infty) \to \mathbb{R}$ be the function $$f(x) = \int_1^{\sqrt x} \! e^{-t^2} \,\mathrm{d}t$$.

### Q10.a

Find $f'(x)$ for every $x \in (0, +\infty)$.

> $$\begin{aligned}
> & \phantom{=} f'(x) \\
> & = \frac {\mathrm{d} } {\mathrm{d}x} \int_1^{\sqrt x} \! e^{-t^2} \,\mathrm{d}t \\
> & = \frac 1 2 \frac {\mathrm{d} } {\mathrm{d}x} \int_1^x \! \frac {e^{-u} } {\sqrt u} \,\mathrm{d}u && (u := t^2, u > 0) \\
> & = \frac {e^{-u} } {2 \sqrt u} && (\text{FTC}) \\
> & = \frac {e^{-t^2} } {2t} && (u > 0)
> \end{aligned}$$

### Q10.b

Evaluate the improper integral $$\int_0^1 \! \frac {f(x)} {\sqrt x} \,\mathrm{d}x$$.

> $$\begin{aligned}
> & \phantom{=} \int_0^1 \! \frac {f(x)} {\sqrt x} \,\mathrm{d}x \\
> & = 2 \int_0^1 \! f(x) \,\mathrm{d}\sqrt{x} \\
> & = 2 \left[f(x) \sqrt x\right]_0^1 - 2 \int_0^1 \! \sqrt{x} \,\mathrm{d}f(x) \\
> & = 2 \left(0 - 0\right) - 2 \int_0^1 \! \sqrt{x} f'(x) \,\mathrm{d}x \\
> & = -\int_0^1 \! \frac {e^{-t^2} } {\sqrt x} \,\mathrm{d}x \\
> & = -2 \int_0^1 \! e^{-u} \,\mathrm{d}u && (u := \sqrt x, u > 0) \\
> & = -2 \left[e^{-u}\right]_0^1 \\
> & = -2 \left(e^{-1} - 1\right) \\
> & = 2 - \frac 2 e
> \end{aligned}$$

## Q15

For each of the following improper integrals, determine whether it converges or not.

### Q15.a

$$\int_1^{+\infty} \frac {2 + \cos x} {\sqrt{x + 5} } \,\mathrm{d}x$$

> $$\begin{aligned}
> & \phantom{=} \int_1^{+\infty} \frac {2 + \cos x} {\sqrt{x + 5} } \,\mathrm{d}x \\
> & \ge \int_1^{+\infty} \frac 1 {\sqrt{x + 5} } \,\mathrm{d}x && (2 + \cos x \ge 1) \\
> & = \int_6^{+\infty} \frac 1 {\sqrt{x} } \,\mathrm{d}x && (\text{change of variables: }x + 5 \mapsto x) \\
> & \text{By }p\text{-test, the last integral is divergent.} \\
> & \text{By comparison test, the original integral is divergent.}
> \end{aligned}$$

### Q15.b

$$\int_0^1 \! \frac 1 {\sqrt{x + \sqrt{x + \sqrt x} } } \,\mathrm{d}x$$

> $$\begin{aligned}
> & \phantom{=} \lim_{x \to 0^+} \frac {\frac 1 {\sqrt{x + \sqrt{x + \sqrt x} } } } {\frac 1 {\sqrt x} } \\
> & = \lim_{x \to 0^+} \frac {\sqrt x} {\sqrt{x + \sqrt{x + \sqrt x} } } \\
> & = \lim_{x \to 0^+} \frac {\sqrt {\frac x {x^{\frac 1 4} } } } {\sqrt{\frac x {x^{\frac 1 4} } + \sqrt{\frac x {\sqrt x} + \sqrt {\frac x x } } } } \\
> & = \lim_{x \to 0^+} \frac {x^{\frac 3 8} } {\sqrt{x^{\frac 3 4} + \sqrt{\sqrt x + 1} } } \\
> & = \frac 0 {\sqrt{0 + \sqrt{0 + 1} } } \\
> & = 0 \\
> & \text{By }p\text{-test, }\int_0^1 \! \frac 1 {\sqrt x} \,\mathrm{d}x\text{ is convergent.} \\
> & \text{By limit comparison test, the original integral is convergent.}
> \end{aligned}$$

### Q15.c

$$\int_0^{+\infty} \! \frac x {1 + x^2 \sin^2 x} \,\mathrm{d}x$$

> $$\begin{aligned}
> & \phantom{=} \int_0^{+\infty} \! \frac x {1 + x^2 \sin^2 x} \,\mathrm{d}x \\
> & \ge \int_0^{+\infty} \! \frac x {1 + x^2} \,\mathrm{d}x && (\sin^2 x \le 1) \\
> & = \frac 1 2 \int_1^{+\infty} \! \frac 1 x \,\mathrm{d}x && (\text{change of variables: } 1 + x^2 \mapsto x) \\
> & \text{By }p\text{-test, the last integral is divergent.} \\
> & \text{By comparison test, the original integral is divergent.}
> \end{aligned}$$

### Q15.d

$$\int_0^{+\infty} \frac {\sin x} x \,\mathrm{d}x$$

> $$\begin{aligned}
> & \phantom{=} \int_0^{+\infty} \! \frac {\sin x} x \,\mathrm{d}x \\
> & \le \int_0^{+\infty} \left\lvert \frac {\sin x} x \right\rvert \,\mathrm{d}x && (\text{triangle inequality}) \\
> & \le \int_0^{+\infty} \left\lvert \frac 1 x \right\rvert \,\mathrm{d}x \\
> & = \int_0^{+\infty} \frac 1 x \,\mathrm{d}x && (x \ge 0) \\
> & \text{By }p\text{-test, the last integral is divergent.} \\
> & \text{By absolute convergence test, the second last integral is convergent.} \\
> & \text{By comparison test, the original integral is convergent.}
> \end{aligned}$$

## Q17

Let $f: [0, +\infty) \to [0, +\infty)$ be a decreasing continuous function.

### Q17.a

Show that if $\int_0^{+\infty} \! f(x) \,\mathrm{d}x$ converges, then $\lim_{x \to +\infty} x f(x) = 0$.

_Hint_: Show that $0 \le x f(x) \le 2 \int_{\frac x 2}^x \! f(t) \,\mathrm{d}t$ and apply Squeeze Theorem.

> $$\begin{aligned}
> & \text{Assume that if }\int_0^{+\infty} \! f(x) \,\mathrm{d}x\text{ is convergent, then }\lim_{x \to +\infty} x f(x) \ne 0\text{.} \\
> & \int_1^{+\infty} \! \frac 1 x \,\mathrm{d}x \text{ is divergent by }p\text{-test.} \\
> & \phantom{=} \lim_{x \to +\infty} \frac {f(x)} {\frac 1 x} \\
> & = \lim_{x \to +\infty} x f(x) \\
> & > 0 && (\text{assumption}, f(x) \ge 0, x > 0) \\
> & \text{By limit comparison test, }\int_1^{+\infty} \! f(x) \,\mathrm{d}x\text{ diverges.} && \left(f(x) \ge 0, \frac 1 x > 0\right) \\
> & \text{By comparison test, }\int_0^{+\infty} \! f(x) \,\mathrm{d}x \ge \int_1^{+\infty} \! f(x) \,\mathrm{d}x \text{ diverges.} && (f(x) \ge 0) \\
> & \text{This contradicts our initial assumption that }\int_0^{+\infty} \! f(x) \,\mathrm{d}x\text{ is convergent.} \\
> & \text{By contradiction, if }\int_0^{+\infty} \! f(x) \,\mathrm{d}x\text{ is convergent, then }\lim_{x \to +\infty} x f(x) = 0\text{.}
> \end{aligned}$$

### Q17.b

Show that the converse of the result from (a) is not true, i.e. give an example of $f(x)$ so that $\lim_{x \to +\infty} x f(x) = 0$ but $\int_0^{+\infty} f(x) \,\mathrm{d}x$ diverges.

> $$\begin{aligned}
> f(x) & := \begin{cases} \frac 1 {x \ln x} & x \ge e \\
> \frac 1 e & x \in [0, e] \end{cases} \\
> & \text{Because }x \ln x\text{ is increasing and nonnegative,} \\
> & f(x)\text{ is decreasing and nonnegative.} \\
> \lim_{x \to e^+} \frac 1 {x \ln x} & = \frac 1 {e \ln e} \\
> & = \frac 1 e \\
> & f(x)\text{ is continuous.} \\
> \\
> \int_0^{+\infty} \! f(x) \,\mathrm{d}x & = \int_0^e \frac 1 e \,\mathrm{d}x + \int_e^{+\infty} \frac 1 {x \ln x} \,\mathrm{d}x \\
> & = 1 + \int_e^{+\infty} \frac 1 {x \ln x} \,\mathrm{d}x \\
> & = 1 + \int_e^{+\infty} \frac 1 {\ln x} \,\mathrm{d}(\ln x) \\
> & = 1 + \left[\ln(\ln x) \right]_e^{+\infty} \\
> & = 1 + \lim_{x \to +\infty} \ln(\ln x) \\
> & = +\infty \\
> & \text{So }\int_0^{+\infty} \! f(x) \,\mathrm{d}x\text{ diverges.} \\
> \\
> & \text{However,} \\
> \lim_{x \to +\infty} x f(x) & = \lim_{x \to +\infty} \frac x {x \ln x} \\
> & = \lim_{x \to +\infty} \frac 1 {\ln x} \\
> & = 0 \\
> \\
> & \text{Thus it is proved.}
> \end{aligned}$$

Now let $g: [1, +\infty) \to [e, +\infty)$ be an increasing continuous function.

### Q17.c

If $\lim_{x \to +\infty} \frac x {\ln\left(g\left(e^x\right)\right)} = 0$, show that for every sufficiently large $x > 0$ we have $\frac {e^x} {g\left(e^x\right)} < e^{-x}$.

_Hint_: In the definition of limit (Definition 2.91), take $\epsilon = \frac 1 2$.

> $$\begin{aligned}
> & \begin{aligned} \lim_{x \to +\infty} \frac x {\ln\left(g\left(e^x\right)\right)} & = 0 \\
> \lim_{x \to +\infty} \left(e^x - g\left(e^x\right)\right) & = e^0 \\
> & = 1 \end{aligned} \\
> & \text{By limit definition, for large sufficiently }x > 0\text{,} \\
> & \begin{aligned}\frac x {\ln\left(g\left(e^x\right)\right)} & < \frac 1 2 \\
> x & < \frac 1 2 \ln\left(g\left(e^x\right)\right) \\
> x - \ln\left(g\left(e^x\right)\right) & < -\frac 1 2 \ln\left(g\left(e^x\right)\right) \\
> x - \ln\left(g\left(e^x\right)\right) & < -x && \left(\frac x {\ln\left(g\left(e^x\right)\right)} < \frac 1 2 \implies -x > -\frac 1 2 \ln\left(g\left(e^x\right)\right) \right) \\
> \frac {e^x} {g\left(e^x\right)} & < e^{-x} && \left(e^*\text{ is strictly increasing}\right) \end{aligned}
> \end{aligned}$$

### Q17.d

Using the results from [(a)](#Q17.a) and [(c)](#Q17.c), show that if $\int_1^{+\infty} \frac 1 {g(x)} \,\mathrm{d}x$ diverges, then $\int_1^{+\infty} \frac 1 {x \ln g(x)} \,\mathrm{d}x$ also diverges.

> $$\begin{aligned}
> \int_1^{+\infty} \! \frac 1 {g(x)} \,\mathrm{d}x & = \int_0^{+\infty} \! \frac {e^x} {g\left(e^x\right)} \,\mathrm{d}x && (\text{change of variables: } \ln x \mapsto x) \\
> \\
> \int_0^{+\infty} \! e{^{-x} } \,\mathrm{d}x & = \left[-e^{-x}\right]_0^{+\infty} \\
> & = 1 \\
> \\
> \int_0^{+\infty} \! e{^{-x} } \,\mathrm{d}x&\text{ is convergent but} \\
> \int_0^{+\infty} \! \frac {e^x} {g\left(e^x\right)} \,\mathrm{d}x&\text{ is divergent,} \\
> & \text{By contraposition of comparison test,} \\
> & \text{ for large enough }x \ge X > 0\text{,} \\
> & \frac {e^x} {g\left(e^x\right)} > e^{-x} \\
> \\
> \lim_{x \to +\infty} \frac x {\ln\left(g\left(e^x\right)\right)} & > 0 && (\text{contraposition of (c)}, x > 0, \ln * > 0) \\
> \int_0^{+\infty} \! \frac 1 {\ln\left(g\left(e^x\right)\right)} \,\mathrm{d}x & \text{ diverges by contraposition of (a).} \\
> \int_0^{+\infty} \! \frac 1 {\ln\left(g\left(e^x\right)\right)} \,\mathrm{d}x & = \int_1^{+\infty} \! \frac 1 {x \ln g(x)} \,\mathrm{d}x && \left(\text{change of variables: } e^x \mapsto x \right) \\
> \int_1^{+\infty} \! \frac 1 {x \ln g(x)} \,\mathrm{d}x & \text{ diverges.}
> \end{aligned}$$
