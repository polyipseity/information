---
aliases:
  - HKUST MATH 1014 L1 assignment 2 submission
tags:
  - date/2024/03/04
  - language/in/English
---

# L1 assignment 2 submission

- HKUST MATH 1014

## 1

Let $n$ be a positive integer. Evaluate each of the following limits.

### 1.a

$$\lim_{x \to 0} \frac 1 {x^n} \int_0^{x^n} \! \cos\left(t^2\right) \,\mathrm{d}t$$

> $$\begin{aligned}
> \lim_{x \to 0} \frac 1 {x^n} \int_0^{x^n} \! \cos\left(t^2\right) \,\mathrm{d}t & = \lim_{x \to 0} \int_0^1 \! \cos\left(x^{2n} t^2\right) \,\mathrm{d}t && \left( \text{change of variable } \frac t {x^n} \mapsto t \right) \\
> & = \int_0^1 \! \lim_{x \to 0} \cos\left(x^{2n} t^2\right) \,\mathrm{d}t && (\text{dominated convergence theorem; dominated by } f(x) = 1 \text{ on } [0, 1]) \\
> & = \int_0^1 \! \cos\left( \left( \lim_{x \to 0} x \right)^{2n} t \right) && \left( f(x) = \cos \left(x^{2n} t\right) \text{ is continuous at } 0 \right) \\
> & = \int_0^1 \! \cos 0 \,\mathrm{d}t && (n > 0) \\
> & = \int_0^1 \! \mathrm{d}t \\
> & = 1
> \end{aligned}$$

### 1.b

$$\lim_{x \to 0} \frac 1 {x^n} \int_0^{x^n} \! \cos \left( x^2 t \right) \,\mathrm{d}t$$

> $$\begin{aligned}
> \lim_{x \to 0} \frac 1 {x^n} \int_0^{x^n} \! \cos \left( x^2 t \right) \,\mathrm{d} & = \lim_{x \to 0} \int_0^1 \! \cos \left( x^{n + 2} t \right) \,\mathrm{d}t && \left( \text{change of variable } \frac t {x^n} \mapsto t \right) \\
> & = \int_0^1 \! \lim_{x \to 0} \cos \left( x^{n + 2} t \right) \,\mathrm{d}t && \left( \text{dominated convergence theorem; dominated by } f(x) = 1 \text{ on } [0, 1] \right) \\
> & = \int_0^1 \! \cos \left( \left(\lim_{x \to 0} x\right)^{n + 2} t \right) \,\mathrm{d}t && \left( f(x) = \cos \left( x^{n + 2} t \right) \text{ is continuous at } 0 \right) \\
> & = \int_0^1 \! \cos 0 \,\mathrm{d}t && (n + 2 > 0) \\
> & = \int_0^1 \! \mathrm{d}t \\
> & = 1
> \end{aligned}$$

## 2

Let $f, g: \mathbb{R} \to \mathbb{R}$ be __increasing__ continuous functions, and let $F: \mathbb{R} \to \mathbb{R}$ be the function defined by $$F(x) = x \int_0^x \! f(t) g(t) \,\mathrm{d}t - \left( \int_0^x \! f(t) \,\mathrm{d}t \right) \left( \int_0^x \! g(t) \,\mathrm{d}t \right)$$.

### 2.a

Show that $F$ is differentiable on $\mathbb{R}$ and $$F'(x) = \int_0^x \! (f(x) - f(t)) (g(x) - g(t)) \,\mathrm{d}t$$.

> $$\begin{aligned}
> & \begin{aligned} f(t) \in C(\mathbb{R}, \mathbb{R}) & \implies X(x) := \int_0^x \! f(t) \,\mathrm{d}t \in C^1(\mathbb{R}, \mathbb{R}) && (\text{first fundamental theorem of calculus}) \\
> g(t) \in C(\mathbb{R}, \mathbb{R}) & \implies Y(x) := \int_0^x \! g(t) \,\mathrm{d}t \in C^1(\mathbb{R}, \mathbb{R}) && (\text{first fundamental theorem of calculus}) \\
> f(t), g(t) \in C(\mathbb{R}, \mathbb{R}) & \implies f(t) g(t) \in C(\mathbb{R}, \mathbb{R}) \\
> & \implies Z(x) := \int_0^x \! f(t) g(t) \,\mathrm{d}t \in C^1(\mathbb{R}, \mathbb{R}) && (\text{first fundamental theorem of calculus}) \\
> x, Z(x) \in C^1(\mathbb{R}, \mathbb{R}) & \implies x Z(x) \in C^1(\mathbb{R}, \mathbb{R}) && (\text{product rule}) \\
> X(x), Y(x) \in C^1(\mathbb{R}, \mathbb{R}) & \implies X(x) Y(x) \in C^1(\mathbb{R}, \mathbb{R}) && (\text{product rule}) \\
> x Z(x), X(x) Y(x) \in C^1(\mathbb{R}, \mathbb{R}) & \implies F(x) = x Z(x) - X(x) Y(x) \in C^1(\mathbb{R}, \mathbb{R}) && (\text{linearity of differentiation}) \end{aligned} \\
> & \therefore F(x) \text{ is differentiable on } \mathbb{R} \text{.}
> \\
> & \begin{aligned} F(x) & = x \int_0^x \! f(t) g(t) \,\mathrm{d}t - \left( \int_0^x \! f(t) \,\mathrm{d}t \right) \left( \int_0^x \! g(t) \,\mathrm{d}t \right) \\
> & = x Z(x) - X(x) Y(x) \\
> F'(x) & = Z(x) + x Z'(x) - X'(x) Y(x) - X(x) Y'(x) \\
> & = \int_0^x \! f(t) g(t) \,\mathrm{d}t + x f(x) g(x) - f(x) \int_0^x \! g(t) \,\mathrm{d}t - g(x) \int_0^x \! f(t) \,\mathrm{d}t && (\text{first fundamental theorem of calculus}) \\
> & = \int_0^x \! f(t) g(t) \,\mathrm{d}t + \int_0^x \! f(x) g(x) \,\mathrm{d}t - \int_0^x \! f(x) g(t) \,\mathrm{d}t - \int_0^x \! f(t) g(x) \,\mathrm{d}t \\
> & = \int_0^x (f(t) g(t) + f(x) g(x) - f(x) g(t) - f(t) g(x)) \,\mathrm{d}t && (\text{linearity of integral}) \\
> & = \int_0^x (f(x) (g(x) - g(t)) + f(t) (g(t) - g(x))) \,\mathrm{d}t \\
> & = \int_0^x (f(x) - f(t)) (g(x) - g(t)) \,\mathrm{d}t \end{aligned}
> \end{aligned}$$

### 2.b

Using the result from [2.a](#2.a), find the global minimum of $F$ on $\mathbb{R}$.

> $$\begin{aligned}
> & \text{Solve for } F'(x) = 0 \text{.} \\
> & \text{When }x = 0\text{, obviously } F'(x) = 0 \text{.} \\
> & \text{When }x > 0\text{, }t \in [0, x] \text{, then} \\
> & \begin{aligned} x \ge t & \implies f(x) - f(t) \ge 0 && (f \text{ is increasing}) \\
> x \ge t & \implies g(x) - g(t) \ge 0 && (g \text{ is increasing}) \\
> f(x) - f(t) \ge 0 \land g(x) - g(t) \ge 0 & \implies (f(x) - f(t)) (g(x) - g(t)) \ge 0 \\
> & \implies \int_0^x \! (f(x) - f(t)) (g(x) - g(t)) \,\mathrm{d}t \ge 0 && (\text{integrand is nonnegative; } x > 0) \\
> & \implies F'(x) \ge 0 \end{aligned} \\
> & \text{When }x < 0\text{, }t \in [x, 0] \text{, then} \\
> & \begin{aligned} x \le t & \implies f(x) - f(t) \le 0 && (f \text{ is increasing}) \\
> x \le t & \implies g(x) - g(t) \le 0 && (g \text{ is increasing}) \\
> f(x) - f(t) \le 0 \land g(x) - g(t) \le 0 & \implies (f(x) - f(t)) (g(x) - g(t)) \ge 0 \\
> & \implies \int_x^0 \! (f(x) - f(t)) (g(x) - g(t)) \,\mathrm{d}t \ge 0 && (\text{integrand is nonnegative; } 0 > x) \\
> & \implies \int_0^x \! (f(x) - f(t)) (g(x) - g(t)) \,\mathrm{d}t \le 0 \\
> & \implies F'(x) \le 0 \end{aligned} \\
> & \text{The above shows that }F(x)\text{ is decreasing on }(-\infty, 0)\text{, stationary on }\set{0}\text{, and increasing on }(0, +\infty)\text{.} \\
> & \text{Then }x = 0\text{ is one of the global minima of }F(x)\text{.} \\
> & \text{So the global minimum value is }F(0) = 0\text{.}
> \end{aligned}$$

## 6

### 6.a

By considering the function $f(x) = x - \sin x$, show that $$\sin x \le x$$ for every $x \ge 0$.

> $\begin{aligned}
> f(x) & = x - \sin x \\
> f(x) & \in C^\infty(\mathbb{R}, \mathbb{R}) \\
> f(0) & = 0 - \sin 0 = 0 \\
> \\
> f'(x) & = 1 - \cos x \\
> & \ge 0 && (\cos x \le 1) \\
> f'(x) \ge 0 & \implies (x \ge y \implies f(x) \ge f(y)) && (\text{increasing}) \\
> \\
> \forall x \ge 0 \\
> x \ge 0 & \implies f(x) \ge f(0) \\
> & \implies f(x) \ge 0 \\
> f(x) & \ge 0 \\
> x - \sin x & \ge 0 \\
> x & \ge \sin x \\
> \sin x & \le x
> \end{aligned}$

### 6.b

Using the result of [6.a](#6.a) and integration, show that each of the following inequalities holds for every $x \ge 0$.

#### 6.b.i

$$\cos x \ge 1 - \frac {x^2} 2$$

> $$\begin{aligned}
> \forall x \ge 0 \\
> \sin x & \le x \\
> \int_0^x \! \sin \xi \,\mathrm{d}\xi & \le \int_0^x \! \xi \,\mathrm{d}\xi && (\text{the integrands are continuous and thus integrable by FTC I; }x \ge 0) \\
> [-\cos \xi]_0^x & \le \left[ \frac {\xi^2} 2 \right]_0^x \\
> \cos 0 - \cos x & \le \frac {x^2} 2 - \frac {0^2} 2 \\
> 1 - \cos x & \le \frac {x^2} 2 \\
> -\cos x & \le -1 + \frac {x^2} 2 \\
> \cos x & \ge 1 - \frac {x^2} 2
> \end{aligned}$$

#### 6.b.ii

$$\sin x \ge x - \frac {x^3} 6$$

> $$\begin{aligned}
> \forall x \ge 0 \\
> \cos x & \ge 1 - \frac {x^2} 2 \\
> \int_0^x \! \cos \xi \,\mathrm{d}\xi & \ge \int_0^x \! \left( 1 - \frac {\xi^2} 2 \right) \,\mathrm{d}\xi && (\text{the integrands are continuous and thus integrable by FTC I; } x \ge 0) \\
> [\sin \xi]_0^x & \ge \left[\xi - \frac {\xi^3} 6 \right]_0^x \\
> \sin x - \sin 0 & \ge x - \frac {x^3} 6 - 0 + \frac{0^3} 6 \\
> \sin x & \ge x - \frac {x^3} 6
> \end{aligned}$$

#### 6.b.iii

$$\cos x \le 1 - \frac {x^2} 2 + \frac {x^4} 24$$

> $$\begin{aligned}
> \forall x \ge 0 \\
> \sin x & \ge x - \frac {x^3} 6 \\
> \int_0^x \! \sin \xi \,\mathrm{d}\xi & \ge \int_0^x \! \left( \xi - \frac {\xi^3} 6 \right) \,\mathrm{d}\xi && (\text{the integrands are continuous and thus integrable by FTC I; }x \ge 0) \\
> [-\cos \xi]_0^x & \ge \left[ \frac {\xi^2} 2 - \frac {\xi^4} {24} \right]_0^x \\
> \cos 0 - \cos x & \ge \frac {x^2} 2 - \frac {x^4} {24} - \frac {0^2} 2 + \frac {0^4} {24} \\
> 1 - \cos x & \ge \frac {x^2} 2 - \frac {x^4} {24} \\
> -\cos x & \ge -1 + \frac {x^2} 2 - \frac {x^4} {24} \\
> \cos x & \le 1 - \frac {x^2} 2 + \frac {x^4} {24}
> \end{aligned}$$

## 7

### 7.a

Let $a < b$ be real numbers and let $f: [a, b] \to (0, +\infty)$ be a __positive__ continuous function. Using Cauchy-Schwarz inequality, show that $$\left( \int_a^b \! f(x) \,\mathrm{d}x \right) \left( \int_a^b \! \frac 1 {f(x)} \,\mathrm{d}x \right) \ge (b - a)^2$$.

> $$\begin{aligned}
> & \begin{aligned} g(x) & := \frac 1 {f(x)} \\
> F(x) & := \sqrt{f(x)} \\
> G(x) & := \sqrt{g(x)} = \frac 1 {\sqrt{f(x)} } \\
> f(x) & \text{ is integrable on }[a, b]\text{ because it is bounded and continuous.} \\
> g(x) & \text{ is integrable on }[a, b]\text{ because it is bounded and continuous.} && (f(x) > 0 \text{ and is bounded} \implies g(x) = \frac 1 {f(x)} > 0 \text{ and is bounded}) \\
> F(x) & \text{ is integrable on }[a, b]\text{ because it is bounded and continuous.} && (f(x) > 0 \text{ and is bounded} \implies F(x) = \sqrt{f(x)} > 0 \text{ and is bounded}) \\
> G(x) & \text{ is integrable on }[a, b]\text{ because it is bounded and continuous.} && (g(x) > 0 \text{ and is bounded} \implies G(x) = \sqrt{g(x)} > 0 \text{ and is bounded}) \end{aligned} \\
> \\
> & \text{By the Cauchy-Schwarz inequality,} \\
> & \begin{aligned} \left( \int_a^b \! (F(x))^2 \,\mathrm{d}x \right) \left( \int_a^b \! (G(x))^2 \,\mathrm{d}x \right) & \ge \left( \int_a^b \! F(x) G(x) \,\mathrm{d}x \right)^2 \\
> \left( \int_a^b \! \left(\sqrt{f(x)}\right)^2 \,\mathrm{d}x \right) \left( \int_a^b \! \left(\frac 1 {\sqrt{f(x)} }\right)^2 \,\mathrm{d}x \right) & \ge \left( \int_a^b \! \sqrt{f(x)} \frac 1 {\sqrt{f(x)} } \,\mathrm{d}x \right)^2 \\
> \left( \int_a^b \! \lvert f(x) \rvert \,\mathrm{d}x \right) \left( \int_a^b \! \frac 1 {\lvert f(x) \rvert} \,\mathrm{d}x \right) & \ge \left( \int_a^b \! \mathrm{d}x \right)^2 \\
> & \ge (b - a)^2 \\
> \left( \int_a^b \! f(x) \,\mathrm{d}x \right) \left( \int_a^b \! \frac 1 {f(x)} \,\mathrm{d}x \right) & \ge (b - a)^2 && (f(x) > 0) \end{aligned}
> \end{aligned}$$

### 7.b

Using the result from [7.a](#7.a) and Cauchy-Schwarz inequality again, show that $$\int_0^{2\pi} \frac 1 {\sqrt{1 - \frac 1 2 \cos x} } \,\mathrm{d}x \ge 2\pi$$.

> $$\begin{aligned}
> f(x) & := \sqrt{1 - \frac 1 2 \cos x} && x \in \mathbb{R} \\
> f(x) & \text{ is continuous and bounded.} \\
> \cos x & \in [-1, 1] \\
> 1 - \frac 1 2 \cos x & \in [0.5, 1.5] \\
> \sqrt{1 - \frac 1 2 \cos x} & > 0 \\
> f(x) & > 0 \\
> \\
> \left( \int_0^{2\pi} \! \mathrm{d}x \right) \left( \int_0^{2\pi} \! (f(x))^2 \,\mathrm{d}x \right) & \ge \left( \int_0^{2\pi} \! f(x) \,\mathrm{d}x \right)^2 && (\text{Cauchy-Schwarz inequality}) \\
> 2\pi \left( \int_0^{2\pi} \! \left(1 - \frac 1 2 \cos x \right) \,\mathrm{d}x \right) & \ge \left( \int_0^{2\pi} \! f(x) \,\mathrm{d}x \right)^2 \\
> 2\pi \left[x - \frac 1 2 \sin x \right]_0^{2\pi} & \ge \left( \int_0^{2\pi} \! f(x) \,\mathrm{d}x \right)^2 \\
> 2\pi \left(2\pi - \frac 1 2 \sin (2\pi) - 0 + \frac 1 2 \sin 0 \right) & \ge \left( \int_0^{2\pi} \! f(x) \,\mathrm{d}x \right)^2 \\
> 4 \pi^2 & \ge \left( \int_0^{2\pi} \! f(x) \,\mathrm{d}x \right)^2 \\
> 2 \pi & \ge \left\lvert \int_0^{2\pi} \! f(x) \,\mathrm{d}x \right\rvert \\
> 2 \pi & \ge \int_0^{2\pi} \! f(x) \,\mathrm{d}x && (f(x) > 0, 2\pi > 0) \\
> \\
> \left( \int_0^{2\pi} \! f(x) \,\mathrm{d}x \right) \left( \int_0^{2\pi} \! \frac 1 {f(x)} \,\mathrm{d}x \right) & \ge (2\pi - 0)^2 && (\text{7.a}) \\
> & \ge 4\pi^2 \\
> \int_0^{2\pi} \! \frac 1 {f(x)} \,\mathrm{d}x & \ge \frac {4\pi^2} {\int_0^{2\pi} \! f(x) \,\mathrm{d}x} \\
> & \ge \frac {4\pi^2} {2\pi} && \left( 2 \pi \ge \int_0^{2\pi} \! f(x) \,\mathrm{d}x \right) \\
> \int_0^{2\pi} \frac 1 {\sqrt{1 - \frac 1 2 \cos x} } \,\mathrm{d}x & \ge 2\pi
> \end{aligned}$$

## 8

Let $m \in (0, 1)$ be a fixed number, and let $f: \mathbb{R} \to \mathbb{R}$ be the function defined by $$f(x) = \int_0^x \! \frac 1 {\sqrt{1 - m \sin^2 t} } \,\mathrm{d}t$$.

### 8.a

Show that $f$ is strictly increasing on $\mathbb{R}$.

> $$\begin{aligned}
> \forall t \in \mathbb{R} \\
> \sin t & \in [-1, 1] \\
> \sin^2 t & \in [0, 1] \\
> m \sin^2 t & \in [0, 1) && (m \in (0, 1)) \\
> 1 - m \sin^2 t & \in (0, 1] \\
> \sqrt{1 - m \sin^2 t} & \in (0, 1] \\
> \frac 1 {\sqrt{1 - m \sin^2 t} } & \in [1, +\infty) \\
> & > 0 \\
> \\
> f(x) & = \int_0^x \! \frac 1 {\sqrt{1 - m \sin^2 t} } \,\mathrm{d}t \\
> f'(x) & = \frac 1 {\sqrt{1 - m \sin^2 x} } && (\text{first fundamental theorem of calculus}) \\
> & > 0 \\
> f'(x) > 0 & \implies f\text{ is strictly increasing on }\mathbb{R}\text{.}
> \end{aligned}$$

### 8.b

Show that $f(x) \ge x$ for every $x > 0$. Hence deduce that $$\lim_{x \to +\infty} f(x) = +\infty$$ and $$\lim_{x \to -\infty} f(x) = -\infty$$.

> $$\begin{aligned}
> \forall x > 0 \\
> \frac 1 {\sqrt{1 - m \sin^2 x} } & \in [1, +\infty) \\
> & \ge 1 \\
> \int_0^x \! \frac 1 {\sqrt{1 - m \sin^2 \xi} } \,\mathrm{d}\xi & \ge \int_0^x \,\mathrm{d}\xi && (\text{the integrands are continuous and thus integrable by FTC I; }x > 0) \\
> f(x) & \ge [\xi]_0^x \\
> & \ge x \\
> \\
> \text{When }x > 0\text{,} \\
> f(x) & \ge x \\
> \lim_{x \to +\infty} f(x) & \ge \lim_{x \to +\infty} x && (x > 0) \\
> & \ge +\infty \\
> \lim_{x \to +\infty} f(x) & = +\infty \\
> \\
> f(-x) & = \int_0^{-x} \! \frac 1 {\sqrt{1 - m \sin^2 x} } \,\mathrm{d}x \\
> & = -\int_0^x \frac 1 {\sqrt{1 - m \sin^2 (-x)} } \,\mathrm{d}x && (\text{change of variable }-x \mapsto x) \\
> & = -\int_0^x \frac 1 {\sqrt{1 - m \sin^2 x} } \,\mathrm{d}x \\
> & = -f(x) \\
> \\
> \text{When }x < 0\text{,} \\
> f(-x) & \ge -x \\
> \lim_{x \to -\infty} f(-x) & \ge \lim_{x \to -\infty} -x && (x < 0) \\
> -\lim_{x \to -\infty} f(x) & \ge +\infty \\
> \lim_{x \to -\infty} f(x) & \le -\infty \\
> \lim_{x \to -\infty} f(x) & = -\infty
> \end{aligned}$$

### 8.c

Using the results from (a) and (b), deduce that $f$ has an inverse which is defined on $\mathbb{R}$.

> $$\begin{aligned}
> & \text{The range of }f\text{ is }(-\infty, +\infty)\text{, i.e. }\mathbb{R}\text{.} && (\text{8.b}) \\
> & f\text{ is invertible as it is strictly increasing on all of its domain.} && (\text{8.a}) \\
> & \text{The domain of the inverse of }f\text{ is the range of }f\text{, which is }\mathbb{R}\text{.}
> \end{aligned}$$

### 8.d

For each $y \in \mathbb{R}$, let's write $x := f^{-1}(y)$ and define three functions $p, q, r: \mathbb{R} \to \mathbb{R}$ by $$\begin{cases} p(y) = \sin x \\ q(y) = \cos x \\ r(y) = \sqrt{1 - m \sin^2 x} \end{cases}$$.

Show that $$p'(y) = q(y)r(y)$$ for every $y \in \mathbb{R}$.

In a similar way, also compute $q'(y)$ and $r'(y)$ in terms of $p(y)$, $q(y)$, and $r(y)$.

> $$\begin{aligned}
> f(x) & = \int_0^x \! \frac 1 {\sqrt{1 - m \sin^2 t} } \,\mathrm{d}t \\
> f'(x) & = \frac 1 {\sqrt{1 - m \sin^2 x} } && (\text{first fundamental theorem of calculus}) \\
> & > 0 \\
> f(x) & \text{ is continuously differentiable with nonzero derivative everywhere on }\mathbb{R}\text{, thus} \\
> f^{-1}(y) & \text{ is continuously differentiable on }\mathbb{R}\text{ by the inverse function theorem.} \\
> \\
> p(y) & = \sin \left(f^{-1}(y)\right) \\
> p'(y) & = (\cos x) (f^{-1}(y))' && (\text{chain rule}) \\
> & = \frac {\cos x} {f'(x)} && (\text{inverse function theorem}) \\
> & = (\cos x) \left(\sqrt{1 - m \sin^2 x}\right) \\
> & = q(y) r(y) \\
> \\
> q(y) & = \cos \left(f^{-1}(y)\right) \\
> q'(y) & = (-\sin x) (f^{-1}(y))' && (\text{chain rule}) \\
> & = -\frac {\sin x} {f'(x)} && (\text{inverse function theorem}) \\
> & = -(\sin x) \left(\sqrt{1 - m \sin^2 x}\right) \\
> & = -p(y) r(y) \\
> \\
> r(y) & = \sqrt{1 - m \sin^2 \left(f^{-1}(y)\right)} \\
> r'(y) & = \frac {-2m \sin x \cos x \left(f^{-1}(y)\right)'} {2 \sqrt{1 - m \sin^2 x} } && (\text{chain rule}) \\
> r'(y) & = \frac {-2m \sin x \cos x} {2 \sqrt{1 - m \sin^2 x} f'(x) } && (\text{inverse function theorem}) \\
> r'(y) & = -m \sin x \cos x \\
> & = -m p(y) q(y)
> \end{aligned}$$

## 12

### 12.a

Let $x$ be a fixed non-negative number with $x \ne 1$. Evaluate the integral $$\int_0^\pi \! \frac {\sin t} {\sqrt{1 - 2x \cos t + x^2} } \,\mathrm{d}t$$ in terms of $x$.

> $$\begin{aligned}
> x \ne 0 \\
> \int_0^\pi \! \frac {\sin t} {\sqrt{1 - 2x \cos t + x^2} } \,\mathrm{d}t & = -\int_1^{-1} \! \frac 1 {\sqrt{1 - 2xt + x^2} } \,\mathrm{d}t && (\text{change of variable } \cos t \mapsto t) \\
> & = \int_{-1}^1 \! \frac 1 {\sqrt{1 + x^2 - 2xt} } \,\mathrm{d}t \\
> & = -\frac 1 {2x} \int_{1 + 2x + x^2}^{1 - 2x + x^2} \! \frac 1 {\sqrt t} \,\mathrm{d}t && (\text{change of variable } 1 + x^2 - 2xt \mapsto t, x \ne 0) \\
> & = \frac 1 x \left[\sqrt t \right]_{1 - 2x + x^2}^{1 + 2x + x^2} \\
> & = \frac 1 x \left[\sqrt t \right]_{(x - 1)^2}^{(x + 1)^2} \\
> & = \frac {\lvert x + 1 \rvert - \lvert x - 1 \rvert} x \\
> & = \begin{cases} \frac {(x + 1) - (x - 1)} x & x > 1 \\ \frac {(x + 1) - (1 - x)} x & 0 < x < 1 \end{cases} \\
> & = \begin{cases} \frac 2 x & x > 1 \\ 2 & 0 < x < 1 \end{cases} \\
> \\
> x = 0 \\
> \int_0^\pi \! \frac {\sin t} {\sqrt{1 - 2x \cos t + x^2} } \,\mathrm{d}t & = \int_0^\pi \! \sin t \,\mathrm{d}t \\
> & = [-\cos t]_0^\pi \\
> & = 2 \\
> \\
> \int_0^\pi \! \frac {\sin t} {\sqrt{1 - 2x \cos t + x^2} } \,\mathrm{d}t & = \begin{cases} \frac 2 x & x > 1 \\ 2 & 0 \le x < 1 \end{cases}
> \end{aligned}$$

### 12.b

Let $f: [0, +\infty) \to \mathbb{R}$ be the function defined by $$f(x) = \begin{cases} \int_0^\pi \! \frac {\sin t} {\sqrt{1 - 2x \cos t + x^2} } \,\mathrm{d}t & \text{if }x \ne 1 \\ a & \text{if }x = 1 \end{cases}$$.

Using the result from [12.a](#12.a), find the value of $a$ so that $f$ is a continuous function. Hence sketch the graph of $f$.

> $$\begin{aligned}
> & \text{Using the definition in 12.a,} \\
> & \lim_{x \to 1^-} f(x) = \lim_{x \to 1^-} 2 = 2 \\
> & \lim_{x \to 1^+} f(x) = \lim_{x \to 1^+} \frac 2 x = 2 \\
> & \therefore \lim_{x \to 1} f(x) = 2 \\
> & \therefore \text{To make }f\text{ continuous, }a = \lim_{x \to 1} f(x) = 2\text{.}
> \end{aligned}$$
>
> ![figure 12.b](attachments/Pasted%20image%2020240304171119.png)

## 13

### 13.a

Using the substitution $u = \frac 1 x$, show that $$\int_{\frac 1 2}^2 \! \frac {\ln x} {1 + x^2} \,\mathrm{d}x = 0$$.

> $$\begin{aligned}
> \int_{\frac 1 2}^2 \! \frac {\ln x} {1 + x^2} \,\mathrm{d}x & = -\int_{u = 2}^{u = \frac 1 2} \! \frac {\ln x} {1 + x^{-2} } \,\mathrm{d}u && (\text{change of variable}) \\
> & = \int_2^{\frac 1 2} \! \frac{\ln u} {1 + u^2} \,\mathrm{d}u \\
> & = \int_2^{\frac 1 2} \! \frac{\ln x} {1 + x^2} \,\mathrm{d}x && (\text{rename dummy variable}) \\
> & = -\int_{\frac 1 2}^2 \! \frac{\ln x} {1 + x^2} \,\mathrm{d}x \\
> 2 \int_{\frac 1 2}^2 \! \frac {\ln x} {1 + x^2} \,\mathrm{d}x & = 0 \\
> \int_{\frac 1 2}^2 \! \frac {\ln x} {1 + x^2} \,\mathrm{d}x & = 0
> \end{aligned}$$

### 13.b

Using [13.a](#13.a) or otherwise, evaluate the limit $$\lim_{n \to +\infty} \sum_{k = 1}^{3n} \frac 1 {2n} \frac {\ln \left( 2 \left( \frac 1 2 + \frac k {2n} \right) \right)} {1 + \left( \frac 1 2 + \frac k {2n} \right)^2}$$.

> $$\begin{aligned}
> \lim_{n \to +\infty} \sum_{k = 1}^{3n} \frac 1 {2n} \frac {\ln \left( 2 \left( \frac 1 2 + \frac k {2n} \right) \right)} {1 + \left( \frac 1 2 + \frac k {2n} \right)^2} & = \lim_{n \to +\infty} \sum_{k = 1}^{3n} \frac {\frac 3 2} {3n} \frac {\ln \left( 2 \left( \frac 1 2 + \frac k {2n} \right) \right)} {1 + \left( \frac 1 2 + \frac k {2n} \right)^2} \\
> & = \int_{\frac 1 2}^2 \! \frac {\ln 2x} {1 + x^2} \,\mathrm{d}x && \left( \text{the integrand is bounded and continuous on }\left[ \frac 1 2, 2 \right]\text{, so it is integrable} \right) \\
> & = \int_{\frac 1 2}^2 \! \frac {\ln 2 + \ln x} {1 + x^2} \,\mathrm{d}x \\
> & = (\ln 2) \int_{\frac 1 2}^2 \! \frac 1 {1 + x^2} \,\mathrm{d}x + \int_{\frac 1 2}^2 \! \frac {\ln x} {1 + x^2} \,\mathrm{d}x \\
> & = (\ln 2) [\arctan x]_{\frac 1 2}^2 + 0 \\
> & = (\ln 2) \left(\arctan 2 - \arctan \frac 1 2 \right) \\
> & = (\ln 2) \left(\arctan 2 - \left( \frac \pi 2 - \arctan 2 \right) \right) \\
> & = (\ln 2) \left( 2 \arctan 2 - \frac \pi 2 \right)
> \end{aligned}$$

## 16

### 16.a

Let $f: [0, \pi] \to \mathbb{R}$ be a continuous function such that $$f(\pi - x) = -f(x)$$ for every $x \in [0, \pi]$.

Using the substitution $u = \pi - x$, show that $$\int_0^\pi \! f(x) \ln \left(1 + e^{\cos x} \right) \,\mathrm{d}x = \frac 1 2 \int_0^\pi \! f(x) \cos x \,\mathrm{d}x$$.

> $$\begin{aligned}
> \int_0^\pi \! f(x) \ln \left(1 + e^{\cos x} \right) \,\mathrm{d}x & = -\int_\pi^0 \! f(\pi - u) \ln \left(1 + e^{\cos (\pi - u)} \right) \,\mathrm{d}u && (\text{change of variable}) \\
> & = -\int_0^\pi \! f(u) \ln \left(1 + e^{-\cos u} \right) \,\mathrm{d}u \\
> & = -\int_0^\pi \! f(x) \ln \left(1 + e^{-\cos x} \right) \,\mathrm{d}x && (\text{rename dummy variable}) \\
> 2 \int_0^\pi \! f(x) \ln \left(1 + e^{\cos x} \right) \,\mathrm{d}x & = \int_0^\pi \! f(x) \ln \left(1 + e^{\cos x} \right) \,\mathrm{d}x - \int_0^\pi \! f(x) \ln \left(1 + e^{-\cos x} \right) \,\mathrm{d}x \\
> & = \int_0^\pi \! f(x) \left( \ln \left(1 + e^{-\cos x} \right) - \ln \left(1 + e^{-\cos x} \right) \right) \,\mathrm{d}x \\
> & = \int_0^\pi \! f(x) \ln \left( \frac {1 + e^{\cos x} } {e^{-\cos x} + 1} \right) \,\mathrm{d}x \\
> & = \int_0^\pi \! f(x) \ln \left( e^{\cos x} \right) \,\mathrm{d}x \\
> & = \int_0^\pi \! f(x) \cos x \,\mathrm{d}x \\
> \int_0^\pi \! f(x) \ln \left(1 + e^{\cos x} \right) \,\mathrm{d}x & = \frac 1 2 \int_0^\pi \! f(x) \cos x \,\mathrm{d}x
> \end{aligned}$$

### 16.b

Compute the derivative of the function $g: [0, \pi] \to \mathbb{R}$ defined by $$g(x) = \frac {\cos x} {1 + \sin x}$$.

Using this together with the result from [16.a](#16.a), evaluate the integral $$\int_0^\pi \! \frac{(\cos x) \ln \left( 1 + e^{\cos x} \right)} {(1 + \sin x)^2} \,\mathrm{d}x$$.

> $$\begin{aligned}
> g(x) & = \frac {\cos x} {1 + \sin x} \\
> g'(x) & = \frac {-(\sin x) (1 + \sin x) - \cos^2 x} {(1 + \sin x)^2} && (\text{quotient rule}) \\
> & = \frac {-\sin x - \sin^2 x - \cos^2 x} {(1 + \sin x)^2} \\
> & = -\frac {1 + \sin x} {(1 + \sin x)^2} \\
> & = -\frac 1 {1 + \sin x} \\
> g''(x) & = -\frac {-\cos x} {(1 + \sin x)^2} && (\text{quotient rule}) \\
> & = \frac {\cos x} {(1 + \sin x)^2} \\
> \\
> f &: [0, \pi] \to \mathbb{R} \\
> f(x) & := \frac {\cos x} {(1 + \sin x)^2} \\
> f(x) & \text{ is continuous on }[0, \pi]\text{.} \\
> f(\pi - x) & = \frac{\cos (\pi - x)} {(1 + \sin (\pi - x))^2} \\
> & = -\frac{\cos x} {(1 + \sin x)^2} \\
> & = -f(x) \\
> \\
> \int_0^\pi \! \frac{(\cos x) \ln \left( 1 + e^{\cos x} \right)} {(1 + \sin x)^2} \,\mathrm{d}x & = \int_0^\pi \! f(x) \ln \left( 1 + e^{\cos x} \right) \,\mathrm{d}x \\
> & = \frac 1 2 \int_0^\pi \! f(x) \cos x \,\mathrm{d}x && (\text{16.a}) \\
> & = \frac 1 2 \int_0^\pi \! \frac {\cos^2 x} {(1 + \sin x)^2} \,\mathrm{d}x \\
> & = \frac 1 2 \int_0^\pi \! g''(x) \cos x \,\mathrm{d}x \\
> & = \frac 1 2 \int_{x = 0}^{x = \pi} \! \cos x \,\mathrm{d}g'(x) \\
> & = \frac 1 2 \left( [g'(x) \cos x]_0^\pi - \int_{x = 0}^{x = \pi} \! g'(x) \,\mathrm{d}(\cos x) \right) && (\text{integration by parts}) \\
> & = \frac 1 2 \left( -g'(\pi) - g'(0) + \int_0^\pi \! \frac {\sin x} {1 + \sin x} \,\mathrm{d}x \right) \\
> & = \frac 1 2 \left( 2 + \int_0^\pi \! g'(x) \sin x \,\mathrm{d}x \right) \\
> & = \frac 1 2 \left( 2 + \int_{x = 0}^{x = \pi} \! \sin x \,\mathrm{d}g(x) \right) \\
> & = \frac 1 2 \left( 2 + [g'(x) \sin x]_0^\pi - \int_{x = 0}^{x = \pi} \! g(x) \,\mathrm{d}(\sin x) \right) && (\text{integration by parts}) \\
> & = \frac 1 2 \left( 2 - \int_0^\pi \! g(x) \cos x \,\mathrm{d}x \right) \\
> & = \frac 1 2 \left( 2 - \int_0^\pi \! \frac {\cos^2 x} {1 + \sin x} \,\mathrm{d}x \right) \\
> & = \frac 1 2 \left( 2 - \int_0^\pi \! \frac {(1 - \sin x) (1 + \sin x)} {1 + \sin x} \,\mathrm{d}x \right) \\
> & = \frac 1 2 \left( 2 - \int_0^\pi \! (1 - \sin x) \,\mathrm{d}x \right) \\
> & = \frac 1 2 (2 - [x + \cos x]_0^\pi) \\
> & = \frac 1 2 (2 - \pi + 1 + 0 + 1) \\
> & = 2 - \frac \pi 2
> \end{aligned}$$
