---
aliases:
  - HKUST MATH 1014 L1 assignment 3 submission
tags:
  - date/2024/03/15
  - language/in/English
---

# L1 assignment 3 submission

- HKUST MATH 1014

## 1

### 1.a

Let $m$ and $n$ be non-negative integers. Evaluate the following integrals, distinguishing all possible cases for $m$ and $n$.

#### 1.a.i

$$\int_{-\pi}^\pi \! \cos mx \cos nx \,\mathrm{d}x$$

> $$\begin{aligned}
> & \phantom{=} \int_{-\pi}^\pi \! \cos mx \cos nx \,\mathrm{d}x \\
> & = \frac 1 2 \int_{-\pi}^\pi \! (\cos((m + n)x) + \cos((m - n)x)) \,\mathrm{d}x \\
> & = \begin{cases} \frac 1 2 \int_{-\pi}^\pi \! ( 1 + 1 ) \,\mathrm{d}x & m + n = 0, m - n = 0 \\
> \frac 1 2 \int_{-\pi}^\pi \! (1 + \cos ((m - n) x) ) \,\mathrm{d}x & m + n = 0 \\
> \frac 1 2 \int_{-\pi}^\pi \! ( \cos ((m + n) x) + 1 ) \,\mathrm{d}x & m - n = 0 \\
> \frac 1 2 \int_{-\pi}^\pi \! ( \cos ((m + n) x) + \cos ((m - n) x) ) \,\mathrm{d}x & \text{otherwise} \end{cases} \\
> & = \begin{cases} \frac 1 2 [2x]_{x = -\pi}^{x = \pi} & m + n = 0, m - n = 0 \\
> \frac 1 2 \left[x + \frac 1 {m - n} \sin((m - n)x) \right]_{x = -\pi}^{x = \pi} & m + n = 0 \\
> \frac 1 2 \left[\frac 1 {m + n} \sin((m + n)x) + x \right]_{x = -\pi}^{x = \pi} & m - n = 0 \\
> \frac 1 2 \left[\frac 1 {m + n} \sin((m + n)x) + \frac 1 {m - n} \sin((m - n)x) \right]_{x = -\pi}^{x = \pi} & \text{otherwise} \end{cases} \\
> & = \begin{cases} 2\pi & m + n = 0, m - n = 0 \\
> \pi & m + n = 0 \\
> \pi & m - n = 0 \\
> 0 & \text{otherwise} \end{cases}
> \end{aligned}$$

#### 1.a.ii

$$\int_{-\pi}^\pi \! \sin mx \sin nx \,\mathrm{d}x$$

> $$\begin{aligned}
> & \phantom{=} \int_{-\pi}^\pi \! \sin mx \sin nx \\
> & = \frac 1 2 \int_{-\pi}^\pi \! ( \cos ((m + n) x) - \cos ((m - n) x) ) \,\mathrm{d}x \\
> & = \begin{cases} \frac 1 2 \int_{-\pi}^\pi \! ( 1 - 1 ) \,\mathrm{d}x & m + n = 0, m - n = 0 \\
> \frac 1 2 \int_{-\pi}^\pi \! (1 - \cos ((m - n) x) ) \,\mathrm{d}x & m + n = 0 \\
> \frac 1 2 \int_{-\pi}^\pi \! ( \cos ((m + n) x) - 1 ) \,\mathrm{d}x & m - n = 0 \\
> \frac 1 2 \int_{-\pi}^\pi \! ( \cos ((m + n) x) - \cos ((m - n) x) ) \,\mathrm{d}x & \text{otherwise} \end{cases} \\
> & = \begin{cases} 0 & m + n = 0, m - n = 0 \\
> \frac 1 2 \left[x - \frac 1 {m - n} \sin((m - n)x) \right]_{x = -\pi}^{x = \pi} & m + n = 0 \\
> \frac 1 2 \left[\frac 1 {m + n} \sin((m + n)x) - x \right]_{x = -\pi}^{x = \pi} & m - n = 0 \\
> \frac 1 2 \left[\frac 1 {m + n} \sin((m + n)x) - \frac 1 {m - n} \sin((m - n)x) \right]_{x = -\pi}^{x = \pi} & \text{otherwise} \end{cases} \\
> & = \begin{cases} 0 & m + n = 0, m - n = 0 \\
> \pi & m + n = 0 \\
> -\pi & m - n = 0 \\
> 0 & \text{otherwise} \end{cases}
> \end{aligned}$$

#### 1.a.iii

$$\int_{-\pi}^\pi \! \cos mx \sin nx \,\mathrm{d}x$$

> $$\begin{aligned}
> & \phantom{=} \int_{-\pi}^\pi \! \cos mx \sin nx \,\mathrm{d}x \\
> & = \int_0^\pi \! \cos mx \sin nx \,\mathrm{d}x + \int_{-\pi}^0 \! \cos mx \sin nx \,\mathrm{d}x \\
> & = \int_0^\pi \! \cos mx \sin nx \,\mathrm{d}x - \int_\pi^0 \! \cos (-mu) \sin (-nu) \,\mathrm{d}u && (u := -x) \\
> & = \int_0^\pi \! \cos mx \sin nx \,\mathrm{d}x - \int_0^\pi \! \cos mu \sin nu \,\mathrm{d}u \\
> & = 0
> \end{aligned}$$

## 2

Evaluate the following antiderivatives.

### 2.a

$$\int \! x^2 \arctan x \,\mathrm{d}x$$

> $$\begin{aligned}
> & \phantom{=} \int \! x^2 \arctan x \,\mathrm{d}x \\
> & = \frac 1 3 x^3 \arctan x - \frac 1 3 \int \! \frac {x^3} {1 + x^2} \,\mathrm{d}x \\
> & = \frac 1 3 x^3 \arctan x - \frac 1 6 \int \! \frac {x^2} {1 + x^2} \,\mathrm{d}x^2 \\
> & = \frac 1 3 x^3 \arctan x - \frac 1 6 \left( \int \! \mathrm{d}x^2 - \int \! \frac 1 {1 + x^2} \,\mathrm{d}x^2 \right) \\
> & = \frac 1 3 x^3 \arctan x - \frac 1 6 \left(x^2 - \ln \left( 1 + x^2 \right) \right) + C && \left( 1 + x^2 > 0 \right) \\
> & = \frac 1 3 x^3 \arctan x - \frac 1 6 x^2 + \frac 1 6 \ln \left( 1 + x^2 \right) + C
> \end{aligned}$$

### 2.d

$$\int \! \left( 2x^2 + 1 \right) e^{x^2} \,\mathrm{d}x$$

> $$\begin{aligned}
> \frac {\mathrm{d} } {\mathrm{d}x} e^{x^2} & = 2x e^{x^2} \\
> \frac {\mathrm{d} } {\mathrm{d}x} \left( 2x e^{x^2} \right) & = 2e^{x^2} + 4x^2 e^{x^2} \\
> & = 2(2x^2 + 1)e^{x^2} \\
> \int \! \left( 2x^2 + 1 \right) e^{x^2} \,\mathrm{d}x & = xe^{x^2} + C
> \end{aligned}$$

## 7

Let $f: [0, +\infty) \to \mathbb{R}$ be the function defined by $f(x) = xe^x$.

### 7.a

Show that $f$ is strictly increasing.

> $$\begin{aligned}
> f(x) & = x e^x \\
> f'(x) & = e^x + xe^x \\
> & = (1 + x)e^x \\
> \\
> \forall x \in [0, +\infty) \\
> 1 + x & \ge 1 \\
> e^x & \ge 1 \\
> \\
> (1 + x)e^x & \ge 1 \\
> f'(x) & \ge 1 \\
> & > 0 && \implies f(x) \text{ is strictly increasing}
> \end{aligned}$$

### 7.b

Now $f$ is one-to-one according to (a), so we let $g$ be the __inverse__ of $f$, i.e. $g = f^{-1}$.

#### 7.b.i

Write down the domain of $g$. Show that $$g'(x) = \frac 1 {x + e^{g(x)} }$$ for every $x$ in the interior of the domain of $g$.

> $$\begin{aligned}
> & \text{The domain of }g\text{ is }[0, +\infty)\text{.} \\
> \\
> & \phantom{\implies} f'(x) = (1 + x)e^x = e^x + f(x) \in C^0([0, +\infty), [0, +\infty)) \\
> & \implies f(x) \in C^1((0, +\infty), (0, +\infty)) \\
> & \implies g'(x) = \frac 1 {f'(g(x))} \qquad \forall x \in (0, +\infty) && (\text{inverse function theorem}) \\
> \\
> & \forall x \in (0, +\infty) \\
> & \phantom{=} g'(x) \\
> & = \frac 1 {f'(g(x))} \\
> & = \frac 1 {f(g(x)) + e^{g(x)} } \\
> & = \frac 1 {x + e^{g(x)} }
> \end{aligned}$$

#### 7.b.ii

Using the result from [7.b.i](#7.b.i) or otherwise, evaluate the antiderivative $\int \! g(x) \,\mathrm{d}x$, expressing your answer in terms of $g$ and other elementary functions only.

> $$\begin{aligned}
> & \forall x \in (0, +\infty) \\
> & \phantom{=} \int \! g(x) \,\mathrm{d}x \\
> & = xg(x) - \int \! x \,\mathrm{d}g(x) \\
> & = xg(x) - \int \! \frac x {x + e^{g(x)} } \,\mathrm{d}x \\
> & = xg(x) - \left( \int \! \mathrm{d}x - \int \! \frac {e^{g(x)} } {x + e^{g(x)} } \,\mathrm{d}x \right) \\
> & = xg(x) - \left( x - \int \! e^{g(x)} g'(x) \,\mathrm{d}x \right) \\
> & = xg(x) - x + \int \! e^{g(x)} \,\mathrm{d}g(x) \\
> & = xg(x) - x + e^{g(x)} + C
> \end{aligned}$$

#### 7.b.iii

Hence, or otherwise, evaluate the integral $\int_0^e \! g(x) \,\mathrm{d}x$.

> $$\begin{aligned}
> & f(1) = 1 e^1 = e \\
> & g(e) = 1 \\
> & f(0) = 0 e^0 = 0 \\
> & g(0) = 0 \\
> \\
> & \phantom{=} \int_0^e \! g(x) \,\mathrm{d}x \\
> & = \left[xg(x) - x + e^{g(x)} \right]_0^e \\
> & = eg(e) - e + e^{g(e)} - e^{g(0)} \\
> & = e - e + e^1 - e^0 \\
> & = e - 1
> \end{aligned}$$

## 10

For each non-negative integer $n$, let $$I_n = \int_0^1 \! t^n e^t \,\mathrm{d}t$$.

### 10.a

Show that $\frac 1 {n + 1} \le I_n \le \frac e {n + 1}$ for every non-negative integer $n$.

> $$\begin{aligned}
> \int_0^1 \! t^n e^0 \,\mathrm{d}t & \le \int_0^1 \! t^n e^t \,\mathrm{d}t \le \int_0^1 \! t^n e^1 \,\mathrm{d}t && \left((\forall t \in [0, 1])\left(e^0 \le e^t \le e^1\right)\right) \\
> \int_0^1 \! t^n \,\mathrm{d}t & \le I_n \le e \int_0^1 \! t^n \,\mathrm{d}t \\
> \left[\frac {t^{n + 1} } {n + 1} \right]_{t = 0}^{t = 1} & \le I_n \le e \left[\frac {t^{n + 1} } {n + 1} \right]_{t = 0}^{t = 1} \\
> \frac 1 {n + 1} & \le I_n \le \frac e {n + 1}
> \end{aligned}$$

### 10.b

Express $I_n$ in terms of $I_{n - 1}$ for each $n \ge 1$. Hence show that $$I_n = (-1)^{n + 1} n! + e \sum_{k = 0}^n (-1)^k \frac {n!} {(n - k)!}$$.

> $$\begin{aligned}
> & \phantom{=} I_n \\
> & = \int_0^1 \! t^n e^t \,\mathrm{d}t \\
> & = \left[t^n e^t\right]_{t = 0}^{t = 1} - n \int_0^1 \! t^{n - 1} e^t \,\mathrm{d}t \\
> & = e - n I_{n - 1} \\
> \\
> & I_0 = \int_0^1 \! t^0 e^t \,\mathrm{d}t = \left[e^t\right]_0^1 = e - 1 = (-1)^{0 + 1} 0! + e \sum_{k = 0}^0 (-1)^k \frac {0!} {(0 - k)!} \\
> & \text{Assume }I_m = (-1)^{m + 1} m! + e \sum_{k = 0}^m (-1)^k \frac {m!} {(m - k)!}\text{.} \\
> & \phantom{=} I_{m + 1} \\
> & = e - (m + 1) I_m && (m + 1 \ge 1) \\
> & = e - (m + 1) \left( (-1)^{m + 1} m! + e \sum_{k = 0}^m (-1)^k \frac {m!} {(m - k)!} \right) \\
> & = e \left(1 - (m + 1) \sum_{k = 0}^m (-1)^k \frac {m!} {(m - k)!} \right) + (-1)^{m + 2} (m + 1)! \\
> & = e \left(1 + \sum_{k = 0}^m (-1)^{k + 1} \frac {(m + 1)!} {(m - k)!} \right) + (-1)^{m + 2} (m + 1)! \\
> & = e \left((-1)^0 \frac {(m + 1)!} {(m + 1 - 0)!} + \sum_{k = 1}^{m + 1} (-1)^k \frac {(m + 1)!} {(m + 1 - k)!} \right) + (-1)^{m + 2} (m + 1)! \\
> & = e \sum_{k = 0}^{m + 1} (-1)^k \frac {(m + 1)!} {(m + 1 - k)!} + (-1)^{m + 2} (m + 1)! \\
> & = (-1)^{(m + 1) + 1} (m + 1)! + e \sum_{k = 0}^{m + 1} (-1)^k \frac {(m + 1)!} {((m + 1) - k)!} \\
> & \text{By induction, }\forall n \in \mathbb{Z}_{\ge 0} \\
> & I_n = (-1)^{n + 1} n! + e \sum_{k = 0}^n (-1)^k \frac {n!} {(n - k)!}
> \end{aligned}$$

### 10.c

Using [10.a](#10.a) and [10.b](#10.b), deduce that $e$ is an irrational number.

_Hint_: There is no integer in the open interval $(0, 1)$.

> $$\begin{aligned}
> & \text{Assume }e\text{ is rational, then }e = \frac a b\text{ where }a, b \in \mathbb{Z}, b \ne 0\text{.} \\
> & \begin{aligned} \forall n \in \mathbb{Z}_{\ge 0} \\
> I_n & = (-1)^{n + 1} n! + e \sum_{k = 0}^n (-1)^k \frac {n!} {(n - k)!} \\
> e & = \frac {I_n - (-1)^{n + 1} n!} {\sum_{k = 0}^n (-1)^k \frac {n!} {(n - k)!} } \\
> \frac a b & = \frac {I_n - (-1)^{n + 1} n!} {\sum_{k = 0}^n (-1)^k \frac {n!} {(n - k)!} } \\
> a \sum_{k = 0}^n (-1)^k \frac {n!} {(n - k)!} & = b \left(I_n - (-1)^{n + 1} n! \right) \\
> & = b I_n - b (-1)^{n + 1} n! \\
> c & = bI_n - d && (c, d \in \mathbb{Z}) \\
> bI_n & = c + d \\
> bI_n & \in \mathbb{Z} && (\mathbb{Z}\text{ is closed under addition}) \\
> \\
> \frac 1 {n + 1} & \le I_n \le \frac e {n + 1} \\
> \frac 1 {n + 1} & \le I_n < \frac 3 {n + 1} && (e < 3) \\
> \frac {\lvert b \rvert} {n + 1} & \le \lvert b \rvert I_n < \frac {3 \lvert b \rvert} {n + 1} \\
> \frac {\lvert b \rvert} {3\lvert b \rvert + 1} & \le \lvert bI_{3\lvert b \rvert} \rvert < \frac {3 \lvert b \rvert} {3\lvert b \rvert + 1} && (\text{set }n = 3 \lvert b \rvert) \\
> \lvert bI_{3\lvert b \rvert} \rvert & \notin \mathbb{Z} && (\lvert b \rvert < \lvert 3b + 1 \rvert, \lvert 3b \rvert < \lvert 3b + 1 \rvert) \\
> bI_{3\lvert b \rvert} & \notin \mathbb{Z} \end{aligned} \\
> \\
> & \phantom{\implies} (\forall n \in \mathbb{Z}_{\ge 0})(bI_n \notin \mathbb{Z}) \Rightarrow\Leftarrow bI_{3 \lvert b \rvert} \notin \mathbb{Z} \\
> & \implies e\text{ is irrational.}
> \end{aligned}$$

## 11

### 11.a

For every pair of non-negative integers $m$ and $n$, let $$B(m, n) = \int_0^1 \! x^m (1 - x)^n \,\mathrm{d}x$$.

Show that $B(m, n) = \frac n {m + 1} B(m + 1, n - 1)$ for every pair of integers $m \ge 0$ and $n \ge 1$.

Hence or otherwise, deduce that $B(m, n) = \frac {m!n!} {(m + n + 1)!}$.

> $$\begin{aligned}
> & \forall (m, n) \in \mathbb{Z}_{\ge 0} \times \mathbb{Z}_{\ge 1} \\
> & \phantom{=} B(m, n) \\
> & = \int_0^1 \! x^m (1 - x)^n \,\mathrm{d}x \\
> & = \left[\frac 1 {m + 1} x^{m + 1} (1 - x)^n \right]_{x = 0}^{x = 1} + \frac n {m + 1} \int_0^1 \! x^{(m + 1)} (1 - x)^{n - 1} \,\mathrm{d}x \\
> & = 0 + \frac n {m + 1} B(m + 1, n - 1) \\
> & = \frac n {m + 1} B(m + 1, n - 1) \\
> \\
> & \phantom{=} B(m, n) \\
> & = \frac n {m + 1} B(m + 1, n - 1) \\
> & = \frac n {m + 1} \frac {n - 1} {m + 2} B(m + 2, n - 2) \\
> & \vdots \\
> & = \frac {n!} {\frac {(m + n)!} {m!} } B(m + n, 0) \\
> & = \frac {m!n!} {(m + n)!} B(m + n, 0) \\
> & = \frac {m!n!} {(m + n)!} \int_0^1 \! x^{m + n} (1 - x)^0 \,\mathrm{d}x \\
> & = \frac {m!n!} {(m + n)!} \left[\frac 1 {m + n + 1} x^{m + n + 1} \right]_{x = 0}^{x = 1} \\
> & = \frac {m!n!} {(m + n)!} \frac 1 {m + n + 1} \\
> & = \frac {m!n!} {(m + n + 1)!}
> \end{aligned}$$

### 11.b

Show that $$\int_0^1 \! \frac {x^4 (x - 1)^4} {x^2 + 1} \,\mathrm{d}x = \frac {22} 7 - \pi$$.

Using this together with the result from [11.a](#11.a), deduce that $$\frac {22} 7 - \frac 1 {630} < \pi < \frac {22} 7 - \frac 1 {1260}$$.

> $$\begin{aligned}
> & \phantom{=} \int_0^1 \! \frac {x^4 (x - 1)^4} {x^2 + 1} \,\mathrm{d}x \\
> & = \int_0^1 \! \frac {x^4 \left(x^4 - 4x^3 + 6x^2 - 4x + 1\right)} {x^2 + 1} \,\mathrm{d}x \\
> & = \int_0^1 \! \frac {x^8 - 4x^7 + 6x^6 - 4x^5 + x^4} {x^2 + 1} \,\mathrm{d}x \\
> & = \int_0^1 \! \left(x^6 - 4x^5 + 5x^4 - 4x^2 + 4 - \frac 4 {x^2 + 1} \right) \,\mathrm{d}x \\
> & = \left[\frac 1 7 x^7 - \frac 2 3 x^6 + x^5 - \frac 4 3 x^3 + 4x - 4 \arctan x \right]_0^1 \\
> & = \frac 1 7 - \frac 2 3 + 1 - \frac 4 3 + 4 - \pi \\
> & = \frac {22} 7 - \pi \\
> \\
> \frac {x^4(x - 1)^4} {1^2 + 1} & < \frac {x^4 (x - 1)^4} {x^2 + 1} < \frac {x^4(x - 1)^4} {0^2 + 1} && (x \in (0, 1)) \\
> \int_0^1 \! \frac {x^4(x - 1)^4} {1^2 + 1} \,\mathrm{d}x & < \int_0^1 \! \frac {x^4 (x - 1)^4} {x^2 + 1} \,\mathrm{d}x < \int_0^1 \! \frac {x^4(x - 1)^4} {0^2 + 1} \,\mathrm{d}x \\
> \frac 1 2 \int_0^1 \! x^4(x - 1)^4 \,\mathrm{d}x & < \frac {22} 7 - \pi < \int_0^1 \! x^4(x - 1)^4 \,\mathrm{d}x \\
> \frac 1 2 B(4, 4) & < \frac {22} 7 - \pi < B(4, 4) \\
> \frac 1 2 \frac {4!4!} {9!} & < \frac {22} 7 - \pi < \frac {4!4!} {9!} \\
> \frac 1 {1260} & < \frac {22} 7 - \pi < \frac 1 {630} \\
> -\frac 1 {1260} & > \pi - \frac {22} 7 > -\frac 1 {630} \\
> \frac {22} 7 - \frac 1 {1260} & > \pi > \frac {22} 7 - \frac 1 {630} \\
> \frac {22} 7 - \frac 1 {630} & < \pi < \frac {22} 7 - \frac 1 {1260}
> \end{aligned}$$

## 13

Evaluate the following antiderivatives, using trigonometric substitutions when appropriate.

### 13.a

$$\int \! \frac {\sqrt{1 + x^2} + \sqrt{1 - x^2} } {\sqrt{1 - x^4} } \,\mathrm{d}x$$

> $$\begin{aligned}
> & \forall x \in (-1, 1) \\
> & \phantom{=} \int \! \frac {\sqrt{1 + x^2} + \sqrt{1 - x^2} } {\sqrt{1 - x^4} } \,\mathrm{d}x \\
> & = \int \! \frac {\sqrt{1 + x^2} + \sqrt{1 - x^2} } {\sqrt{1 - x^2} \sqrt{1 + x^2} } \,\mathrm{d}x \\
> & = \int \! \left( \frac 1 {\sqrt{1 - x^2} } + \frac 1 {\sqrt{1 + x^2} } \right) \,\mathrm{d}x \\
> & = \arcsin x + \int \! \frac 1 {\sqrt{1 + x^2} } \,\mathrm{d}x \\
> & = \arcsin x + \int \! \frac {\sec^2 \theta} {\sqrt{1 + \tan^2 \theta} } \,\mathrm{d}\theta && \left(x := \tan\theta, \theta \in \left(-\frac \pi 2, \frac \pi 2 \right) \right) \\
> & = \arcsin x + \int \! \sec\theta \,\mathrm{d}\theta \\
> % & = \arcsin x + \int \! \frac 1 {\cos\theta} \,\mathrm{d}\theta \\
> % & = \arcsin x + \int \! \frac 1 {\cos^2\theta} \,\mathrm{d}\sin\theta \\
> % & = \arcsin x + \int \! \frac 1 {1 - \sin^2\theta} \,\mathrm{d}\sin\theta \\
> % & = \arcsin x + \frac 1 2 \int \! \left(\frac 1 {1 + \sin\theta} + \frac 1 {1 - \sin\theta} \right) \mathrm{d}\sin\theta \\
> % & = \arcsin x + \frac 1 2 \ln \lvert 1 + \sin\theta \rvert - \frac 1 2 \ln \lvert 1 - \sin\theta \rvert + C \\
> % & = \arcsin x + \frac 1 2 \ln(1 + \sin\theta) - \frac 1 2 \ln(1 - \sin\theta) + C && (1 + \sin\theta > 0, 1 - \sin\theta > 0) \\
> % & = \arcsin x + \frac 1 2 \ln\left(1 + \operatorname{sgn}(x) \sqrt{\frac {x^2} {1 + x^2} }\right) + \ln\left(1 - \operatorname{sgn}(x) \sqrt{\frac {x^2} {1 + x^2} }\right) + C \\
> & = \arcsin x + \int \! \frac {(\sec\theta)(\sec\theta + \tan\theta)} {\sec\theta + \tan\theta} \,\mathrm{d}\theta \\
> & = \arcsin x + \int \! \frac {\sec^2\theta + \tan\theta \sec\theta} {\sec\theta + \tan\theta} \,\mathrm{d}\theta \\
> & = \arcsin x + \ln \lvert \tan\theta + \sec\theta \rvert + C \\
> & = \arcsin x + \ln \left\lvert x + \sqrt{1 + x^2} \right\rvert + C && \left(\sec\theta > 0 \quad \forall \theta \in \left(-\frac \pi 2, \frac \pi 2 \right)\right) \\
> & = \arcsin x + \ln\left(x + \sqrt{1 + x^2}\right) + C && \left(x + \sqrt{1 + x^2} > 0 \quad \forall x \in (-1, 1) \right)
> \end{aligned}

### 13.b

$$\int \! \frac {x + 1} {\left(x^2 + x + 1\right) \sqrt{x^2 + x + 1} } \,\mathrm{d}x$$

> $$\begin{aligned}
> & \phantom{=} \int \! \frac {x + 1} {\left(x^2 + x + 1\right) \sqrt{x^2 + x + 1} } \,\mathrm{d}x \\
> & = \frac 1 2 \int \! \frac {2x + 1} {\left(x^2 + x + 1\right) \sqrt{x^2 + x + 1} } \,\mathrm{d}x + \frac 1 2 \int \! \frac 1 {\left(x^2 + x + 1\right) \sqrt{x^2 + x + 1} } \,\mathrm{d}x \\
> & = \frac 1 2 \int \! \frac 1 {\left(x^2 + x + 1\right)^{1.5} } \,\mathrm{d}\left(x^2 + x + 1\right) \,\mathrm{d}x + \frac 1 2 \int \! \frac 1 {\left((x + 0.5)^2 + 0.75\right) \sqrt{(x + 0.5)^2 + 0.75} } \,\mathrm{d}x \\
> & = -\frac 1 {\sqrt{x^2 + x + 1} } + \frac 1 2 \sqrt{0.75} \int \! \frac {\sec^2\theta} {\left(0.75\tan^2\theta + 0.75\right) \sqrt{0.75\tan^2\theta + 0.75} } \,\mathrm{d}\theta && \left(x := \sqrt{0.75}\tan\theta - 0.5, \theta \in \left(-\frac \pi 2, \frac \pi 2\right)\right) \\
> & = -\frac 1 {\sqrt{x^2 + x + 1} } + \frac 1 2 \sqrt{0.75} \int \! \frac 1 {0.75 \sqrt{0.75} \sec\theta} \,\mathrm{d}\theta \\
> & = -\frac 1 {\sqrt{x^2 + x + 1} } + \frac 2 3 \int \! \cos\theta \,\mathrm{d}\theta \\
> & = -\frac 1 {\sqrt{x^2 + x + 1} } + \frac 2 3 \sin\theta + C \\
> & = -\frac 1 {\sqrt{x^2 + x + 1} } + \frac 2 3 \operatorname{sgn}(x + 0.5) \frac 1 {\sqrt{\frac 1 {\frac 4 3 (x + 0.5)^2} + 1} } + C \\
> & = -\frac 1 {\sqrt{x^2 + x + 1} } + \frac 2 3 \operatorname{sgn}(x + 0.5) \frac 1 {\sqrt{\frac {3 + 4 (x + 0.5)^2} {4 (x + 0.5)^2} } } + C \\
> & = -\frac 1 {\sqrt{x^2 + x + 1} } + \frac 2 3 \operatorname{sgn}(x + 0.5) \sqrt{\frac {4 (x + 0.5)^2} {4x^2 + 4x + 4} } + C \\
> & = -\frac 1 {\sqrt{x^2 + x + 1} } + \frac {2 (x + 0.5)} {3 \sqrt{x^2 + x + 1} } + C \\
> & = \frac {2x + 1 - 3} {3 \sqrt{x^2 + x + 1} } + C \\
> & = \frac {2x - 2} {3 \sqrt{x^2 + x + 1} } + C
> \end{aligned}$$

## 14

### 14.a

For each non-negative integer $n$, let $$I_n(x) = \int \! \frac {x^n} {\sqrt{x^2 + 1} } \,\mathrm{d}x$$ which is defined up to addition by a constant function. Find a reduction formula that connects $I_n$ and $I_{n - 2}$ for $n \ge 2$.

> $$\begin{aligned}
> \forall n \ge 2 \\
> I_n(x) & = \int \! \frac {x^n} {\sqrt{x^2 + 1} } \,\mathrm{d}x \\
> & = x^{n - 1} \sqrt{x^2 + 1} - (n - 1) \int \! x^{n - 2} \sqrt{x^2 + 1} \,\mathrm{d}x \\
> & = x^{n - 1} \sqrt{x^2 + 1} - (n - 1) \left( \int \! x^{n - 2} \left( \sqrt{x^2 + 1} - \frac 1 {\sqrt{x^2 + 1} } \right) \,\mathrm{d}x + I_{n - 2}(x) \right) \\
> & = x^{n - 1} \sqrt{x^2 + 1} - (n - 1) \left( \int \! x^{n - 2} \frac {x^2} {\sqrt{x^2 + 1} } \,\mathrm{d}x + I_{n - 2}(x) \right) \\
> & = x^{n - 1} \sqrt{x^2 + 1} - (n - 1) \left( \int \! \frac {x^n} {\sqrt{x^2 + 1} } \,\mathrm{d}x + I_{n - 2}(x) \right) \\
> & = x^{n - 1} \sqrt{x^2 + 1} - (n - 1) \left( I_n(x) + I_{n - 2}(x) \right) \\
> & = x^{n - 1} \sqrt{x^2 + 1} - (n - 1) I_n(x) - (n - 1)I_{n - 2}(x) \\
> nI_n(x) & = x^{n - 1} \sqrt{x^2 + 1} - (n - 1)I_{n - 2}(x) \\
> I_n(x) & = \frac 1 n x^{n - 1} \sqrt{x^2 + 1} - \frac {n - 1} n I_{n - 2}(x) \\
> \end{aligned}$$

### 14.b

Hence evaluate $$\int_0^1 \! \frac {x^5} {\sqrt{x^2 + 1} } \,\mathrm{d}x$$.

> $$\begin{aligned}
> & \phantom{=} I_1(x) \\
> & = \int \! \frac x {\sqrt{x^2 + 1} } \,\mathrm{d}x \\
> & = \frac 1 2 \int \! \frac 1 {\sqrt{x^2 + 1} } \,\mathrm{d}x^2 \\
> & = \frac 1 2 \left(2 \sqrt{x^2 + 1} \right) + C \\
> & = \sqrt{x^2 + 1} + C \\
> \\
> & \phantom{=} I_5(x) \\
> & = \frac 1 5 x^4 \sqrt{x^2 + 1} - \frac 4 5 I_3(x) \\
> & = \frac 1 5 x^4 \sqrt{x^2 + 1} - \frac 4 5 \frac 1 3 x^2 \sqrt{x^2 + 1} + \frac 4 5 \frac 2 3 I_1(x) \\
> & = \frac 1 5 x^4 \sqrt{x^2 + 1} - \frac 4 {15} x^2 \sqrt{x^2 + 1} + \frac 8 {15} \sqrt{x^2 + 1} + C \\
> \\
> & \phantom{=} \int_0^1 \! \frac {x^5} {\sqrt{x^2 + 1} } \,\mathrm{d}x \\
> & = I_5(1) - I_5(0) \\
> & = \left[ \frac 1 5 x^4 \sqrt{x^2 + 1} - \frac 4 {15} x^2 \sqrt{x^2 + 1} + \frac 8 {15} \sqrt{x^2 + 1} \right]_0^1 \\
> & = \frac 1 5 \sqrt 2 - \frac 4 {15} \sqrt 2 + \frac 8 {15} \sqrt 2 - \frac 8 {15} \\
> & = \frac 7 {15} \sqrt 2 - \frac 8 {15}
> \end{aligned}$$
