---
aliases:
  - HKUST MATH 1014 L1 assignment 8 submission
tags:
  - date/2024/05/12/from
  - date/2024/05/15/to
  - language/in/English
---

# L1 assignment 8 submission

- HKUST MATH 1014

MATH1014 Calculus II Problem Set 8<br/>
L01 (Spring 2024)

Problem Set 8

Note: The problem sets serve as additional exercise problems for your own practice. Problem Set 8 covers materials from chapter 9.

## Q2

Find the 6<sup>th</sup> order approximation of each of the following functions at 0.

### Q2.b

$$g(x) = e^{\cos x}$$

---

$$\begin{aligned}
i(x) & := \cos x - 1 \\
& \text{As }x \to 0\text{,} \\
i(x) & = \cos 0 - 1 + \frac {-\sin 0} {1!} x^1 + \frac {-\cos 0} {2!} x^2 + \frac {\sin 0} {3!} x^3 + \frac {\cos 0} {4!} x^4 + \frac {-\sin 0} {5!} x^5 + \frac {-\cos 0} {6!} x^6 + \frac {\sin 0} {7!} x^7 + O\left(x^8\right) \\
& = - \frac {x^2} 2 + \frac {x^4} {24} - \frac {x^6} {720} + O\left(x^8\right) \\
& \text{Note that }i(x) = O\left(x^2\right)\text{.} \\
\\
j(x) & := e^x \\
& \text{As }x \to 0\text{,} \\
j(x) & = e^0 + \frac {e^0} {1!} x^1 + \frac {e^0} {2!} x^2 + \frac {e^0} {3!} x^3 + O\left(x^4\right) \\
& = 1 + x + \frac {x^2} 2 + \frac {x^3} 6 + O\left(x^4\right) \\
\\
& \text{As }x \to 0\text{,} \\
g(x) & = e^{\cos x} \\
& = e \cdot e^{\cos x - 1} \\
& = e \cdot j(i(x)) \\
& = e \left(1 + i(x) + \frac {i(x)^2} 2 + \frac {i(x)^3} 6 + O\left(i(x)^4\right)\right) \\
& = e \left(1 - \frac {x^2} 2 + \frac {x^4} {24} - \frac {x^6} {720} + \frac 1 2 \left(\frac {x^4} 4 - \frac {x^6} {24} \right) + \frac 1 6 \left(-\frac {x^6} 8 \right) + O\left(x^8 \right) \right) \\
& = e \left(1 - \frac {x^2} 2 + \frac {x^4} 6 - \frac {31 x^6} {720} + O\left(x^8 \right) \right) \\
& = e - \frac {e x^2} {2} + \frac {ex^4} 6 - \frac {31ex^6} {720} + O\left(x^8 \right) \\
\end{aligned}$$

### Q2.c

$$h(x) = \sec x$$

---

$$\begin{aligned}
& \text{Using the same }i(x)\text{ as in (b),} \\
& \text{As }x \to 0\text{,} \\
i(x) & = - \frac {x^2} 2 + \frac {x^4} {24} - \frac {x^6} {720} + O\left(x^8\right) \\
& \text{Note that }i(x) = O\left(x^2\right)\text{.} \\
\\
k(x) & := \frac 1 {1 - x} \\
& \text{As }x \to 0\text{,} \\
k(x) & = (1 - x)^{-1} + \frac {1! (1 - 0)^{-2} } {1!} x^1 + \frac {2! (1 - 0)^{-3} } {2!} x^2 + \frac {3! (1 - 0)^{-4} } {3!} x^3 + O\left(x^4 \right) \\
& = 1 + x + x^2 + x^3 + O\left(x^4 \right) \\
\\
h(x) & = \sec x \\
& = \frac 1 {\cos x} \\
& = \frac 1 {1 + i(x)} \\
& = k(-i(x)) \\
& = 1 - i(x) + i(x)^2 - i(x)^3 + O\left((-i(x))^4 \right) \\
& = 1 - \left(-\frac {x^2} 2 + \frac {x^4} {24} - \frac {x^6} {720} \right) + \left(\frac {x^4} 4 - \frac {x^6} {24} \right) - \left(-\frac {x^6} 8 \right) + O\left(x^8 \right) \\
& = 1 + \frac {x^2} 2 + \frac {5x^4} {24} + \frac {61x^6} {720} + O\left(x^8 \right)
\end{aligned}$$

## Q3

Evaluate teach of the following limits using polynomial approximations.

### Q3.b

$$\lim_{x \to 0} \frac {\sin^2 x - \sin\left(x^2\right) + \frac 1 3 x^4} {x^6}$$

---

$$\begin{aligned}
f(x) & := \sin x \\
& \text{As }x \to 0\text{,} \\
f(x) & = \sin 0 + \frac {\cos 0} {1!} x + \frac {-\sin 0} {2!} x^2 + \frac {-\cos 0} {3!} x^3 + \frac {\sin 0} {4!} x^4 + \frac {\cos 0} {5!} x^5 + O\left(x^6 \right) \\
& = x - \frac {x^3} 6 + \frac {x^5} {120} + O\left(x^6 \right) \\
& \text{Note that }f(x) = O(x)\text{.} \\
\\
& \text{As }x \to 0\text{,} \\
\sin^2 x & = f(x)^2 \\
& = x^2 - \frac {x^4} 6 + \frac {x^6} {120} - \frac {x^4} 6 + \frac {x^6} {36} + \frac {x^6} {120} + O\left(x^7 \right) \\
& = x^2 - \frac {x^4} 3 + \frac {4 x^6} {90} + O\left(x^7 \right) \\
\\
& \text{As }x \to 0\text{,} \\
\sin\left(x^2 \right) & = f\left(x^2 \right) \\
& = x^2 - \frac {x^6} {6} + O\left(x^{10} \right) \\
\\
& \phantom = \lim_{x \to 0} \frac {\sin^2 x - \sin\left(x^2\right) + \frac 1 3 x^4} {x^6} \\
& = \lim_{x \to 0} \frac {\left( x^2 - \frac {x^4} 3 + \frac {4 x^6} {90} + O\left(x^7 \right) \right) - \left(x^2 - \frac {x^6} {6} + O\left(x^{10} \right) \right) + \frac {x^4} 3} {x^6} \\
& = \lim_{x \to 0} \frac {\frac {19 x^6} {90} } {x^6} && \left(\lim_{x \to 0} \frac {O(x^y)} {x^6} = 0 \quad \forall y > 6 \right) \\
& = \lim_{x \to 0} \frac {19} {90} \\
& = \frac {19} {90}
\end{aligned}$$

### Q3.c

$$\lim_{x \to +\infty} x^2 \left(e - \frac e {2x} - \left(1 + \frac 1 x \right)^x \right)$$

---

$$\begin{aligned}
f(x) & := \ln(1 + x) \\
& \text{As }x \to 0\text{,} \\
f(x) & = \ln(1 + 0) + \frac {(1 + 0)^{-1} } {1!} x - \frac {1!(1 + 0)^{-2} } {2!} x^2 + \frac {2!(1 + 0)^{-3} } {3!} x^3 + O\left(x^4\right) \\
& = x - \frac {x^2} 2 + \frac {x^3} 3 + O\left(x^4\right) \\
\frac 1 x f(x) & = 1 - \frac x 2 + \frac {x^2} 3 + O\left(x^3 \right) \\
\frac 1 x f(x) - 1 & = -\frac x 2 + \frac {x^2} 3 + O\left(x^3 \right) \\
& \text{Note that }\frac 1 x f(x) - 1 = O(x) \text{.} \\
\\
g(x) & := \exp x \\
& \text{As }x \to 0\text{,} \\
g(x) & = \exp 0 + \frac {\exp 0} {1!} x^1 + \frac {\exp 0} {2!} x^2 + O\left(x^4\right) \\
& = 1 + x + \frac {x^2} 2 + O\left(x^3\right) \\
\\
& \text{As }x \to 0\text{,} \\
& \phantom = \exp\left(\frac 1 x \ln (1 + x) \right) \\
& = \exp\left( \frac 1 x f(x) - 1 + 1 \right) \\
& = e \cdot g\left(\frac 1 x f(x) - 1 \right) \\
& = e \left(1 + \left(-\frac x 2 + \frac {x^2} 3 \right) + \frac 1 2 \left(\frac {x^2} 4 \right) + O\left(x^3 \right) \right) \\
& = e \left(1 - \frac x 2 + \frac {11x^2} {24} + O\left(x^3 \right) \right) \\
& = e - \frac {ex} 2 + \frac {11e x^2} {24} + O\left(x^3 \right) \\
\\
& \phantom = \lim_{x \to +\infty} x^2 \left(e - \frac e {2x} - \left(1 + \frac 1 x \right)^x \right) \\
& = \lim_{x \to 0^+} \frac {e - \frac {ex} 2 - (1 + x)^{\frac 1 x} } {x^2} && \left(\text{change of variables: } \frac 1 x \mapsto x \right) \\
& = \lim_{x \to 0^+} \frac {e - \frac {ex} 2 - \exp\left(\frac 1 x \ln \left(1 + x \right) \right)} {x^2} \\
& = \lim_{x \to 0^+} \frac {e - \frac {ex} 2 - e + \frac {ex} 2 - \frac {11e x^2} {24} + O\left(x^3 \right)} {x^2} \\
& = \lim_{x \to 0^+} \frac {e - \frac {ex} 2 - e + \frac {ex} 2 - \frac {11e x^2} {24} } {x^2} && \left(\lim_{x \to 0} \frac {O(x^y)} {x^2} = 0 \quad \forall y > 2 \right) \\
& = \lim_{x \to 0^+} -\frac {11e} {24} \\
& = -\frac {11e} {24}
\end{aligned}$$

## Q5

In Examples 9.31 and 9.32, we have seen that in some cases, Lagrange's remainder formula is not strong enough to show that $\lim_{n \to +\infty} R_n(x) = 0$. Let's develop another remainder formula.

### Q5.a

Let $a$ be real number and let $x > a$, let $n$ be a non-negative integer and let $f$ be a function such that $f^{(n)}$ is continuous on $[a, x]$ and differentiable on $(a, x)$.

#### Q5.a.i

Let $g: [a, x] \to \mathbb{R}$ be the function $$g(t) = f(x) - \sum_{k = 0}^n \frac {f^{(k)}(t)} {k!} (x - t)^k$$.

Compute $g'(t)$ for $t \in (a, x)$

---

$$\begin{aligned}
& \phantom = g(t) \\
& = f(x) - \sum_{k = 0}^n \frac {f^{(k)}(t)} {k!} (x - t)^k \\
& = f(x) - f(t) - \sum_{k = 1}^n \frac {f^{(k)}(t)} {k!} (x - t)^k \\
& \phantom = g'(t) \\
& = -f'(t) -\sum_{k = 1}^n \frac 1 {k!} \left( f^{(k + 1)}(t) (x - t)^k - k f^{(k)}(t) (x - t)^{k - 1} \right) \\
& = -f'(t) -\sum_{k = 1}^n \frac {f^{(k + 1)}(t)} {k!} (x - t)^k + \sum_{k = 1}^n \frac {f^{(k)}(t)} {(k - 1)!} (x - t)^{(k - 1)} \\
& = -f'(t) - \sum_{k = 1}^n \frac {f^{(k + 1)}(t)} {k!} (x - t)^k + \sum_{k = 0}^{n - 1} \frac {f^{(k + 1)}(t)} {k!} (x - t)^k \\
& = -f'(t) - \frac {f^{(n + 1)}(t)} {n!} (x - t)^n + f'(t) \\
& = -\frac {f^{(n + 1)}(t)} {n!} (x - t)^n
\end{aligned}$$

#### Q5.a.ii

__(Cauchy's remainder formula)__ By applying Mean Value Theorem to the function $g$, show that there exists a  number $c \in (a, x)$ such that $$f(x) = \sum_{k = 0}^n \frac {f^{(k)}(a)} {k!} (x - a)^k + \frac {f^{(n + 1)}(c)} {n!} (x - c)^n (x - a)$$.

_Remark_: If we assume further that $f^{(n + 1)}$ is integrable on $[a, x]$, then another way of obtaining [(a) (ii)](#Q5.a.ii) is to use [Q4(a)](#Q4.a) and then the MVT for integrals.

---

$$\begin{aligned}\
& f^{(n)}(t)\text{ is continuous on }[a, x]\text{.} \\
& \implies f^{(k)}(t)\text{ is continuous on }[a, x]\text{ for all }k \in \mathbb{Z}_{[0, n]}\text{.} \\
& g(t)\text{ is continuous on }[a, x]\text{.} \\
\\
& \text{Additionally, }f^{(n + 1)}(t)\text{ exists on }(a, x)\text{.} \\
& g(t)\text{ is differentiable on }(a, x)\text{.} \\
\\
& \text{By the mean value theorem,} \\
& \exists c \in (a, x) \\
g'(c) & = \frac {g(x) - g(a)} {x - a} \\
-\frac {f^{(n + 1)}(c)} {n!} (x - c)^n & = \frac {f(x) - \sum_{k = 0}^n \frac {f^{(k)}(x)} {k!} (x - x)^k - f(x) + \sum_{k = 0}^n \frac {f^{(k)}(a)} {k!} (x - a)^k} {x - a} \\
& = \frac {-f(x) + \sum_{k = 0}^n \frac {f^{(k)}(a)} {k!} (x - a)^k} {x - a} && \left(0^0 = 1\text{ in this context} \right) \\
-\frac {f^{(n + 1)}(c)} {n!} (x - c)^n (x - a) & = -f(x) + \sum_{k = 0}^n \frac {f^{(k)}(a)} {k!} (x - a)^k \\
f(x) & = \sum_{k = 0}^n \frac {f^{(k)}(a)} {k!} (x - a)^k + \frac {f^{(n + 1)}(c)} {n!} (x - c)^n (x - a)
\end{aligned}$$

### Q5.b

Using the result from [(a) (ii)](#Q5.a.ii) (which obviously still holds if $x < a$), show that for each of the following functions, the remainder term at $0$ satisfies $$\lim_{n \to +\infty} R_n(x) = 0 \qquad \text{for each fixed }x \in (-1, 1)$$.

#### Q5.b.i

__(Example 9.31)__ $$f(x) = \ln(1 + x)$$

---

$$\begin{aligned}
f(x) & \in C^\infty((-1, 1], \mathbb{R}) \\
& \text{By Q5.a.ii...} \\
& \text{Set }a = 0\text{.} \\
& (\forall x \in (0, 1])(\exists c \in (0, x)) \\
f(x) & = \sum_{k = 0}^n \frac {f^{(k)}(0)} {k!} (x - 0)^k + \frac {f^{(n + 1)}(c)} {n!} (x - c)^n (x - 0) \\
& = \sum_{k = 0}^n \frac {f^{(k)}(0)} {k!} x^k + \frac {f^{(n + 1)}(c)} {n!} (x - c)^n x \\
& (\forall x \in (-1, 0))(\exists c \in (x, 0)) \\
f(x) & = \sum_{k = 0}^n \frac {f^{(k)}(0)} {k!} x^k + \frac {f^{(n + 1)}(c)} {n!} (x - c)^n x \\
\\
& \phantom = \lim_{n \to +\infty} R_n(x) \\
& = \lim_{n \to +\infty} \left( f(x) - \sum_{k = 0}^n \frac {f^{(k)}(0)} {k!} x^k \right) \\
\\
& \text{When }x = 0\text{,} \\
& \phantom = \lim_{n \to +\infty} R_n(0) \\
& = \lim_{n \to +\infty} \left( f(0) - \sum_{k = 0}^n \frac {f^{(k)}(0)} {k!} 0^k \right) \\
& = \lim_{n \to +\infty} (f(0) - f(0)) && \left(0^0 = 1\text{ in this context}\right) \\
& = \lim_{n \to +\infty} 0 \\
& = 0 \\
\\
& \text{When }x \in (-1, 1) \setminus \set{0}\text{,} \\
& \exists c\text{ in between }0\text{ and }x \\
& \phantom = \lim_{n \to +\infty} R_n(x) \\
& = \lim_{n \to +\infty} \left( f(x) - \sum_{k = 0}^n \frac {f^{(k)}(0)} {k!} x^k \right) \\
& = \lim_{n \to +\infty} \left(\sum_{k = 0}^n \frac {f^{(k)}(0)} {k!} x^k + \frac {f^{(n + 1)}(c)} {n!} (x - c)^n x - \sum_{k = 0}^n \frac {f^{(k)}(0)} {k!} x^k \right) && (n\text{ in the above formula is arbitrary}) \\
& = \lim_{n \to +\infty} \frac {f^{(n + 1)}(c)} {n!} (x - c)^n x \\
& = \lim_{n \to +\infty} \frac {n! (-1)^{n + 1} (1 + c)^{-(n + 1)}} {n!} (x - c)^n x \\
& = \lim_{n \to +\infty} (-1)^{n + 1} \left(\frac {x - c} {1 + c} \right)^n \frac x {1 + x} \\
& = \frac x {1 + x} \lim_{n \to +\infty} (-1)^{n + 1} \left(\frac {x - c} {1 + c} \right)^n \\
\\
& \text{When }x \in (0, 1)\text{, }c \in (0, x)\text{, and} \\
& \phantom = \left\lvert \frac {x - c} {1 + c} \right\rvert \\
& = \frac {x - c} {1 + c} && (x > c, c > 0) \\
& < \frac {1 - c} {1 + c} && (x < 1, c > 0) \\
& < 1 && (c < x < 1) \\
& \text{When }x \in (-1, 0)\text{, }c \in (x, 0)\text{ and} \\
& \phantom = \left\lvert \frac {x - c} {1 + c} \right\rvert \\
& = \frac {c - x} {1 + c} && (x < c, c > x > -1) \\
& < \frac {c + 1} {1 + c} && (-x < 1, c > x > -1) \\
& = 1 \\
\\
& \text{Therefore...} \\
& \text{When }x \in (0, 1)\text{, }c \in (0, x)\text{, and} \\
& \phantom = \lim_{n \to +\infty} R_n(x) \\
& = \frac x {1 + x} \lim_{n \to +\infty} (-1)^{n + 1} \left(\frac {x - c} {1 + c} \right)^n \\
& = \frac x {1 + x} \cdot 0 && \left(\left\lvert \frac {x - c} {1 + c} \right\rvert < 1 \right) \\
& = 0 \\
\\
& \forall x \in (-1, 1) \\
& \phantom = \lim_{n \to +\infty} R_n(x) \\
& = 0
\end{aligned}$$

## Q7

For each of the following, compute its Maclaurin series and find its radius of convergence.

### Q7.b

$$f(x) = \int_0^x \! \frac {\sin t} t \,\mathrm{d}t$$

---

$$\begin{aligned}
& \phantom = f'(x) \\
& = \frac {\sin x} x \\
\\
& \phantom = \sin x \\
& = \sum_{k = 0}^{+\infty} \left(\frac {\sin 0} {(4k)!} x^{4k} + \frac {\cos 0} {(4k + 1)!} x^{4k + 1} + \frac {-\sin 0} {(4k + 2)!} x^{4k + 2} + \frac {-\cos 0} {(4k + 3)!} x^{4k + 3} \right) \\
& = \sum_{k = 0}^{+\infty} \left(\frac {x^{4k + 1} } {(4k + 1)!} - \frac {x^{4k + 3} } {(4k + 3)!} \right) \\
& = \sum_{k = 0}^{+\infty} (-1)^{k} \frac {x^{2k + 1} } {(2k + 1)!} \\
\\
& \phantom = f'(x) \\
& = \frac {\sin x} x \\
& = \sum_{k = 0}^{+\infty} (-1)^{k} \frac {x^{2k} } {(2k + 1)!} \\
\\
& \phantom = f(x) \\
& = \int_0^x \! f'(x) \,\mathrm{d}x \\
& = \int_0^x \! \left( \sum_{k = 0}^{+\infty} (-1)^k \frac {x^{2k} } {(2k + 1)!} \right) \,\mathrm{d}x \\
& = \sum_{k = 0}^{+\infty} \frac {(-1)^k} {(2k + 1)!} \int_0^x \! x^{2k} \,\mathrm{d}x && (\text{Maclaurin series can be integrated term-wise}) \\
& = \sum_{k = 0}^{+\infty} \frac {(-1)^k} {(2k + 1)!(2k + 1)} x^{2k + 1} \\
\\
& \phantom = f(x) \\
& = x \sum_{k = 0}^{+\infty} \frac {(-1)^k} {(2k + 1)!(2k + 1)} \left(x^2\right)^k \\
& \text{The center of the power series is }x^2 = 0\text{.} \\
& \text{The coefficients are }c_k = \frac {(-1)^k} {(2k + 1)!(2k + 1)}\text{.} \\
\\
& \phantom = \text{radius of convergence of the power series} \\
& = \lim_{k \to +\infty} \left\lvert \frac {\frac {(-1)^k} {(2k + 1)!(2k + 1)} } {\frac {(-1)^{k + 1} } {(2k + 3)!(2k + 3)} } \right\rvert \\
& = \lim_{k \to +\infty} \left\lvert \frac {(2k + 3)!(2k + 3)} {(2k + 1)!(2k + 1)} \right\rvert \\
& = \lim_{k \to +\infty} \left\lvert \frac {(2k + 2)(2k + 3)^2} {2k + 1} \right\vert \\
& = +\infty \\
\\
& \phantom = \text{radius of convergence of the Maclurin series of }f(x) \\
& = \sqrt{+\infty} \\
& = +\infty
\end{aligned}$$

### Q7.d

$$f(x) = \ln \left(x + \sqrt{1 + x^2} \right)$$

_Hint_: In [(d)](#Q7.d), first consider $f'$.

---

$$\begin{aligned}
& \phantom = f'(x) \\
& = \frac {1 + \frac x {\sqrt{1 + x^2} } } {x + \sqrt{1 + x^2} } \\
& = \frac {\frac {x + \sqrt{1 + x^2} } {\sqrt{1 + x^2} } } {x + \sqrt{1 + x^2} } \\
& = \frac 1 {\sqrt{1 + x^2} } \\
\\
& \phantom = g(x) \\
& := \frac 1 {\sqrt{1 + x} } \\
& \phantom = \text{Maclaurin series of }g(x) \\
& = \sum_{k = 0}^{+\infty} \frac {g^{(k)}(0)} {k!} x^k \\
& = \sum_{k = 0}^{+\infty} \frac {(-1)^k \left( \prod_{i = 0}^{k - 1} \frac {2i + 1} 2 \right) (1 + 0)^{-\frac {2k + 1} 2} } {k!} x^k \\
& = \sum_{k = 0}^{+\infty} (-1)^k \frac {\prod_{i = 0}^{k - 1} (2i + 1)} {k! 2^k } x^k \\
\\
& \phantom = f'(x) \\
& = \frac 1 {\sqrt{1 + x^2} } \\
& = g(x^2) \\
& \phantom = \text{Maclaurin series of }f'(x) \\
& = \sum_{k = 0}^{+\infty} (-1)^k \frac {\prod_{i = 0}^{k - 1} (2i + 1)} {k! 2^k } x^{2k} \\
\\
& \phantom = f(x) \\
& = \int \! f'(x) \,\mathrm{d}x \\
& \phantom = \text{Maclaurin series of }f(x) \\
& = \int \! \left( \sum_{k = 0}^{+\infty} (-1)^k \frac {\prod_{i = 0}^{k - 1} (2i + 1)} {k! 2^k } x^{2k} \right) \,\mathrm{d}x \\
& = \sum_{k = 0}^{+\infty} (-1)^k \frac {\prod_{i = 0}^{k - 1} (2i + 1)} {k! 2^k } \int \! x^{2k} \,\mathrm{d}x && (\text{Maclaurin series can be integrated term-wise}) \\
& = \sum_{k = 0}^{+\infty} (-1)^k \frac {\prod_{i = 0}^{k - 1} (2i + 1)} {k! 2^k (2k + 1)} x^{2k + 1} \\
\\
& \phantom = \text{Maclaurin series of }f(x) \\
& = x \sum_{k = 0}^{+\infty} (-1)^k \frac {\prod_{i = 0}^{k - 1} (2i + 1)} {k! 2^k (2k + 1)} \left(x^2\right)^k \\
& \text{The center of the power series is }x^2 = 0\text{.} \\
& \text{The coefficients are }c_k = (-1)^k \frac {\prod_{i = 0}^{k - 1} (2i + 1)} {k! 2^k (2k + 1)}\text{.} \\
\\
& \text{radius of convergence of the power series} \\
& = \lim_{k \to +\infty} \left\lvert \frac {(-1)^k \frac {\prod_{i = 0}^{k - 1} (2i + 1)} {k! 2^k (2k + 1)} } {(-1)^{k + 1} \frac {\prod_{i = 0}^k (2i + 1)} {(k + 1)! 2^{k + 1} (2k + 3)} } \right\rvert \\
& = \lim_{k \to +\infty} \left\lvert \frac {2 (k + 1) (2k + 3)} {(2k + 1)^2} \right\rvert \\
& = \lim_{k \to +\infty} \left\lvert \frac {\left(1 + \frac 1 k \right) \left(1 + \frac 3 {2k} \right)} {(1 + \frac 1 {2k} )^2} \right\rvert \\
& = 1 \\
\\
& \text{radius of convergence of the Maclaurin series of }f(x) \\
& = \sqrt 1 \\
& = 1
\end{aligned}$$

## Q9

Let $f(x) = x^3 e^x$. Using the Taylor series of $f$, compute...

for every positive integer $n$. (Do not try to really differentiate for $n$ times!)

### Q9.a

... $$f^{(n)}(0)$$ and

---

$$\begin{aligned}
& \phantom = \exp x \\
& \phantom = \text{Maclaurin series of }\exp x \\
& = \sum_{n = 0}^{+\infty} \frac {\exp 0} {n!} x^n \\
& = \sum_{n = 0}^{+\infty} \frac {x^n} {n!} \\
\\
& \phantom = f(x) \\
& = x^3 \exp x \\
& \phantom = \text{Maclaurin series of }f(x) \\
& = x^3 \sum_{n = 0}^{+\infty} \frac {x^n} {n!} \\
& = \sum_{n = 0}^{+\infty} \frac {x^{n + 3} } {n!} \\
& = \sum_{n = 3}^{+\infty} \frac {x^n} {(n - 3)!} \\
\\
& \phantom = f(x) \\
& \phantom = \text{Maclaurin series of }f(x) \\
& = \sum_{k = 0}^{+\infty} \frac {f^{(n)}(0)} {n!} x^n \\
\\
& \text{Since Taylor (Macluarin) series is unique for a }C^\infty\text{ function,} \\
& \text{by comparing coefficients:} \\
& \text{When }0 \le n < 3\text{,} \\
& \begin{aligned} \frac {f^{(n)}(0)} {n!} & = 0 \\
f^{(n)}(0) & = 0 \end{aligned} \\
& \text{When }n \ge 3\text{,} \\
& \begin{aligned} \frac {f^{(n)}(0)} {n!} & = \frac 1 {(n - 3)!} \\
f^{(n)}(0) & = \frac {n!} {(n - 3)!} \\
& = n (n - 1) (n - 2) \end{aligned}
\end{aligned}$$

### Q9.b

$$f^{(n)}(1)$$

---

$$\begin{aligned}
& \phantom = \exp x \\
& \phantom = \text{Taylor series of }\exp x\text{ at }1 \\
& = \sum_{n = 0}^{+\infty} \frac {\exp 1} {n!} (x - 1)^n \\
& = e \sum_{n = 0}^{+\infty} \frac {(x - 1)^n} {n!} \\
\\
& \phantom = f(x) \\
& = x^3 \exp x \\
& = \left(\left(x^3 - 3 x^2 + 3 x - 1\right) + 3x^2 - 3x + 1 \right) \exp x \\
& = \left(\left(x^3 - 3 x^2 + 3 x - 1\right) + 3\left(x^2 - 2x + 1\right) + 3x - 2 \right) \exp x \\
& = \left(\left(x^3 - 3 x^2 + 3 x - 1\right) + 3\left(x^2 - 2x + 1\right) + 3(x - 1) + 1 \right) \exp x \\
& = \left((x - 1)^3 + 3 (x - 1)^2 + 3 (x - 1) + 1 \right) \exp x \\
& \phantom = \text{Taylor series of }f(x)\text{ at }1 \\
& = e \left((x - 1)^3 + 3 (x - 1)^2 + 3 (x - 1) + 1 \right) \sum_{n = 0}^{+\infty} \frac {(x - 1)^n} {n!} \\
& = e \left( \sum_{n = 0}^{+\infty} \frac {(x - 1)^{n + 3} } {n!} + 3 \sum_{n = 0}^{+\infty} \frac {(x - 1)^{n + 2} } {n!} + 3 \sum_{n = 0}^{+\infty} \frac {(x - 1)^{n + 1} } {n!} + \sum_{n = 0}^{+\infty} \frac {(x - 1)^n} {n!} \right) \\
& = e \left( \sum_{n = 3}^{+\infty} \frac {(x - 1)^n} {(n - 3)!} + 3 \sum_{n = 2}^{+\infty} \frac {(x - 1)^n} {(n - 2)!} + 3 \sum_{n = 1}^{+\infty} \frac {(x - 1)^n} {(n - 1)!} + \sum_{n = 0}^{+\infty} \frac {(x - 1)^n} {n!} \right) \\
\\
& \phantom = f(x) \\
& \phantom = \text{Taylor series of }f(x)\text{ at }1 \\
& = \sum_{k = 0}^{+\infty} \frac {f^{(n)}(1)} {n!} (x - 1)^n \\
\\
& \text{Since Taylor series is unique for a }C^\infty\text{ function,} \\
& \text{by comparing coefficients:} \\
& \begin{aligned} \frac {f^{(n)}(1)} {n!} & = \begin{cases} \frac e {n!}, & n = 0 \\
\frac e {n!} + \frac {3e} {(n - 1)!}, & n = 1 \\
\frac e {n!} + \frac {3e} {(n - 1)!} + \frac {3e} {(n - 2)!}, & n = 2 \\
\frac e {n!} + \frac {3e} {(n - 1)!} + \frac {3e} {(n - 2)!} + \frac e {(n - 3)!}, & n \ge 3 \end{cases} \\
f^{(n)}(1) & = \begin{cases} e, & n = 0 \\
e + 3e n, & n = 1 \\
e + 3e n + 3e n (n - 1), & n = 2 \\
e + 3e n + 3e n (n - 1) + e n (n - 1)(n - 2), & n \ge 3 \end{cases} \\
& = \begin{cases} e, & n = 0 \\
4e, & n = 1 \\
13e, & n = 2 \\
e + 3e n + 3e n (n - 1) + e n (n - 1)(n - 2), & n \ge 3 \end{cases} \end{aligned}
\end{aligned}$$

## Q11

Let $a_0, a_1, \ldots, a_n, b_1, \ldots, b_n$ be real numbers and let $$f(x) = \frac {a_0} 2 + \sum_{k = 1}^n \left(a_k \cos kx + b_k \sin kx \right)$$ be a trigonometric polynomial. (Note that $f$ is a finite sum.) Show that $$\frac 1 \pi \int_{-\pi}^\pi \! f(x)^2 \,\mathrm{d}x = \frac {a_0^2} 2 + \sum_{k = 1}^n \left(a_k^2 + b_k^2 \right)$$.

---

$$\begin{aligned}
& \text{Let }m, n\text{ be two integers.} \\
\\
& \phantom{=} \int_{-\pi}^\pi \! \cos mx \cos nx \,\mathrm{d}x \\
& = \frac 1 2 \int_{-\pi}^\pi \! (\cos((m + n)x) + \cos((m - n)x)) \,\mathrm{d}x \\
& = \begin{cases} \frac 1 2 \int_{-\pi}^\pi \! ( 1 + 1 ) \,\mathrm{d}x & m + n = 0, m - n = 0 \\
\frac 1 2 \int_{-\pi}^\pi \! (1 + \cos ((m - n) x) ) \,\mathrm{d}x & m + n = 0 \\
\frac 1 2 \int_{-\pi}^\pi \! ( \cos ((m + n) x) + 1 ) \,\mathrm{d}x & m - n = 0 \\
\frac 1 2 \int_{-\pi}^\pi \! ( \cos ((m + n) x) + \cos ((m - n) x) ) \,\mathrm{d}x & \text{otherwise} \end{cases} \\
& = \begin{cases} \frac 1 2 [2x]_{x = -\pi}^{x = \pi} & m + n = 0, m - n = 0 \\
\frac 1 2 \left[x + \frac 1 {m - n} \sin((m - n)x) \right]_{x = -\pi}^{x = \pi} & m + n = 0 \\
\frac 1 2 \left[\frac 1 {m + n} \sin((m + n)x) + x \right]_{x = -\pi}^{x = \pi} & m - n = 0 \\
\frac 1 2 \left[\frac 1 {m + n} \sin((m + n)x) + \frac 1 {m - n} \sin((m - n)x) \right]_{x = -\pi}^{x = \pi} & \text{otherwise} \end{cases} \\
& = \begin{cases} 2\pi & m + n = 0, m - n = 0 \\
\pi & m + n = 0 \\
\pi & m - n = 0 \\
0 & \text{otherwise} \end{cases} \\
& = \begin{cases} 2\pi & m = n = 0 \\
\pi & m = -n \\
\pi & m = n \\
0 & \text{otherwise} \end{cases} \\
\\
& \phantom{=} \int_{-\pi}^\pi \! \sin mx \sin nx \\
& = \frac 1 2 \int_{-\pi}^\pi \! ( \cos ((m - n) x) - \cos ((m + n) x) ) \,\mathrm{d}x \\
& = \begin{cases} \frac 1 2 \int_{-\pi}^\pi \! ( 1 - 1 ) \,\mathrm{d}x & m + n = 0, m - n = 0 \\
\frac 1 2 \int_{-\pi}^\pi \! ( \cos ((m - n) x) - 1 ) \,\mathrm{d}x & m + n = 0 \\
\frac 1 2 \int_{-\pi}^\pi \! (1 - \cos ((m + n) x) ) \,\mathrm{d}x & m - n = 0 \\
\frac 1 2 \int_{-\pi}^\pi \! ( \cos ((m - n) x) - \cos ((m + n) x) ) \,\mathrm{d}x & \text{otherwise} \end{cases} \\
& = \begin{cases} 0 & m + n = 0, m - n = 0 \\
\frac 1 2 \left[\frac 1 {m - n} \sin((m - n)x) - x \right]_{x = -\pi}^{x = \pi} & m + n = 0 \\
\frac 1 2 \left[x - \frac 1 {m + n} \sin((m + n)x) \right]_{x = -\pi}^{x = \pi} & m - n = 0 \\
\frac 1 2 \left[\frac 1 {m - n} \sin((m - n)x) - \frac 1 {m + n} \sin((m + n)x) \right]_{x = -\pi}^{x = \pi} & \text{otherwise} \end{cases} \\
& = \begin{cases} 0 & m + n = 0, m - n = 0 \\
-\pi & m + n = 0 \\
\pi & m - n = 0 \\
0 & \text{otherwise} \end{cases} \\
& = \begin{cases} 0 & m = n = 0 \\
-\pi & m = -n \\
\pi & m = n \\
0 & \text{otherwise} \end{cases} \\
\\
& \phantom{=} \int_{-\pi}^\pi \! \cos mx \sin nx \,\mathrm{d}x \\
& = \int_0^\pi \! \cos mx \sin nx \,\mathrm{d}x + \int_{-\pi}^0 \! \cos mx \sin nx \,\mathrm{d}x \\
& = \int_0^\pi \! \cos mx \sin nx \,\mathrm{d}x - \int_\pi^0 \! \cos (-mu) \sin (-nu) \,\mathrm{d}u && (u := -x) \\
& = \int_0^\pi \! \cos mx \sin nx \,\mathrm{d}x - \int_0^\pi \! \cos mu \sin nu \,\mathrm{d}u \\
& = 0 \\
\\
& \text{(The above is adapted from my own work in assignment 3 Q1.)} \\
\\
& \phantom = \int_{-\pi}^\pi \! f(x) \,\mathrm{d}x \\
& = \int_{-\pi}^\pi \! \left(  \frac {a_0} 2 + \sum_{k = 1}^n \left(a_k \cos kx + b_k \sin kx \right) \right) \,\mathrm{d}x \\
& = \int_{-\pi}^\pi \! \frac {a_0} 2 \,\mathrm{d}x + \sum_{k = 1}^n a_k \int_{-\pi}^\pi \cos kx \,\mathrm{d}x + \sum_{k = 1}^n b_k \int_{-\pi}^\pi \! \sin kx \,\mathrm{d}x && (\text{linearity}) \\
& = \pi a_0 + \sum_{k = 1}^n \frac {a_k} k \left[\sin kx \right]_{x = -\pi}^\pi - \sum_{k = 1}^n \frac {b_k} k \left[\cos kx \right]_{x = -\pi}^\pi \\
& = \pi a_0 + 0 - 0 \\
& = \pi a_0 \\
\\
& \phantom = \frac 1 \pi \int_{-\pi}^\pi \! f(x)^2 \,\mathrm{d}x \\
& = \frac 1 \pi \int_{-\pi}^\pi \! \left( \frac {a_0} 2 + \sum_{k = 1}^n \left(a_k \cos kx + b_k \sin kx \right) \right)^2 \,\mathrm{d}x \\
& = \frac 1 \pi \int_{-\pi}^\pi \! \left(a_0 f(x) - \frac {a_0^2} 4 + \sum_{1 \le i, j \le n} \left(a_i \cos ix + b_i \sin ix \right) \left(a_j \cos jx + b_j \sin jx \right) \right) \,\mathrm{d}x \\
& = \frac 1 \pi \int_{-\pi}^\pi \! \left( a_0 f(x) - \frac {a_0^2} 4 + \sum_{1 \le i, j \le n} (a_i a_j \cos ix \cos jx + a_i b_j \cos ix \sin jx + \right. \\
& \phantom = \left. \phantom {\sum_{} } b_i a_j \sin ix \cos jx + b_i b_j \sin ix \sin jx) \right) \,\mathrm{d}x \\
& = \frac {a_0} \pi \int_{-\pi}^\pi \! \left( f(x) - \frac {a_0} 4 \right) \,\mathrm{d}x + \frac 1 \pi \sum_{1 \le i, j \le n} a_i a_j \int_{-\pi}^\pi \! \cos ix \cos jx \,\mathrm{d}x && (\text{linearity}) \\
& \phantom = + \frac 1 \pi \sum_{1 \le i, j \le n} a_i b_j \int_{-\pi}^\pi \! \cos ix \sin jx \,\mathrm{d}x \\
& \phantom = + \frac 1 \pi \sum_{1 \le i, j \le n} b_i a_j \int_{-\pi}^\pi \! \sin ix \cos jx \,\mathrm{d}x \\
& \phantom = + \frac 1 \pi \sum_{1 \le i, j \le n} b_i b_j \int_{-\pi}^\pi \! \sin ix \sin jx \,\mathrm{d}x \\
& = \frac {a_0} \pi \int_{-\pi}^\pi \! f(x) \,\mathrm{d}x - \frac {a_0^2} 2 + \sum_{k = 1}^n a_k^2 + 0 + 0 + \sum_{k = 1}^n b_k^2 && (\text{apply equations above}) \\
& = a_0^2 - \frac {a_0^2} 2 + \sum_{k = 1}^n \left(a_k^2 + b_k^2 \right) \\
& = \frac {a_0^2} 2 + \sum_{k = 1}^n \left(a_k^2 + b_k^2 \right)
\end{aligned}$$

## Q13

Let $a$ be a real number which is not an integer. Let $f(x) = \cos ax$ be defined on $[-\pi, \pi]$ and extended periodically to become a function with period $2\pi$.

### Q13.a

Compute the Fourier series of $f$.

---

$$\begin{aligned}
& \because f\text{ is a periodic function of period }2\pi \\
& \phantom \because f\text{ is continuously differentiable on }\mathbb{R} \\
& \therefore f\text{ equals its Fourier series on }\mathbb{R} \\
\\
& \phantom = f(x) \\
& = \frac 1 {2\pi} \! \int_{-\pi}^\pi \! f(x) \,\mathrm{d}x + \sum_{n = 1}^{+\infty} \left( \cos(nx) \frac 1 \pi \int_{-\pi}^\pi \! f(x) \cos(nx) \,\mathrm{d}x + \sin(nx) \frac 1 \pi \int_{-\pi}^\pi \! f(x) \sin(nx) \,\mathrm{d}x \right) \\
& = \frac 1 {2\pi} \! \int_{-\pi}^\pi \! \cos(ax) \,\mathrm{d}x + \sum_{n = 1}^{+\infty} \left( \cos(nx) \frac 1 \pi \int_{-\pi}^\pi \! \cos(ax) \cos(nx) \,\mathrm{d}x + \sin(nx) \frac 1 \pi \int_{-\pi}^\pi \! \cos(ax) \sin(nx) \,\mathrm{d}x \right) \\
& = \frac 1 {2a\pi} [\sin(ax)]_{x = -\pi}^\pi + \sum_{n = 1}^{+\infty} \left(\cos(nx) \frac 1 {2\pi} \int_{-\pi}^\pi \left(\cos((a - n)x) + \cos((a + n)x) \right) \,\mathrm{d}x \right. \\
& \phantom = \left. + \sin(nx) \frac 1 {2\pi} \int_{-\pi}^\pi \! \left(\sin((a + n)x) - \sin((a - n)x) \right) \,\mathrm{d}x \right) \\
& = \frac {\sin(a\pi)} {a\pi} + \sum_{n = 1}^{+\infty} \left(\frac {\cos(nx)} {2\pi} \left[\frac {\sin((a - n)x)} {a - n} + \frac {\sin((a + n)x)} {a + n} \right]_{x = -\pi}^\pi \right. && (a \notin \mathbb{Z}) \\
& \phantom = \left. - \frac {\sin(nx)} {2\pi} \left[\frac {\cos((a + n)x)} {a + n} - \frac {\cos((a - n)x)} {a - n} \right]_{x = -\pi}^\pi \right) \\
& = \frac {\sin(a\pi)} {a\pi} + \frac 1 \pi \sum_{n = 1}^{+\infty} \cos(nx) \left(\frac {\sin((a - n)\pi)} {a - n} + \frac {\sin((a + n)\pi)} {a + n} \right) \\
& = \frac {\sin(a\pi)} {a\pi} + \frac 1 \pi \sum_{n = 1}^{+\infty} \cos(nx) \frac {(a + n)\sin((a - n)\pi) + (a - n)\sin((a + n)\pi)} {a^2 - n^2} \\
& = \frac {\sin(a\pi)} {a\pi} + \frac 1 \pi \sum_{n = 1}^{+\infty} \cos(nx) \frac {2a \sin\left(a\pi\right) \cos (n\pi) + 2n \sin(n\pi) \cos(a\pi)} {a^2 - n^2} \\
& = \frac {\sin(a\pi)} {a\pi} + \frac {2a} \pi \sum_{n = 1}^{+\infty} \cos(nx) \frac {(-1)^n \sin(a\pi)} {a^2 - n^2} \\
& = \frac {\sin(a\pi)} {a\pi} + \frac {2a\sin(a\pi)} \pi \sum_{n = 1}^{+\infty} (-1)^n \frac {\cos(nx)} {a^2 - n^2}
\end{aligned}$$

### Q13.b

Using [(a)](#Q13.a), prove that $$\sum_{k = 1}^{+\infty} \frac {(-1)^{k - 1} } {k^2 - a^2} = - \frac 1 {2a^2} + \frac \pi {2a \sin(a\pi)}$$.

and in a similar way also compute $$\sum_{k = 1}^{+\infty} \frac 1 {k^2 - a^2}$$.

---

$$\begin{aligned}
f(x) & = \frac {\sin(a\pi)} {a\pi} + \frac {2a\sin(a\pi)} \pi \sum_{n = 1}^{+\infty} (-1)^n \frac {\cos(nx)} {a^2 - n^2} && (\text{Q13.a}) \\
\\
f(0) & = \frac {\sin(a\pi)} {a\pi} + \frac {2a\sin(a\pi)} \pi \sum_{n = 1}^{+\infty} (-1)^n \frac {\cos(0n)} {a^2 - n^2} \\
\cos(0a) & = \frac {\sin(a\pi)} {a\pi} + \frac {2a\sin(a\pi)} \pi \sum_{k = 1}^{+\infty} \frac {(-1)^{k - 1} } {k^2 - a^2} \\
1 - \frac {\sin(a\pi)} {a\pi} & = \frac {2a\sin(a\pi)} \pi \sum_{k = 1}^{+\infty} \frac {(-1)^{k - 1} } {k^2 - a^2} \\
\sum_{k = 1}^{+\infty} \frac {(-1)^{k - 1} } {k^2 - a^2} & = - \frac {1} {2a^2} + \frac \pi {2a\sin(a\pi)} \\
\\
f(\pi) & = \frac {\sin(a\pi)} {a\pi} + \frac {2a\sin(a\pi)} \pi \sum_{n = 1}^{+\infty} (-1)^n \frac {\cos(n\pi)} {a^2 - n^2} \\
\cos(a\pi) & = \frac {\sin(a\pi)} {a\pi} + \frac {2a\sin(a\pi)} \pi \sum_{k = 1}^{+\infty} \frac 1 {a^2 - k^2} \\
\cos(a\pi) - \frac {\sin(a\pi)} {a\pi} & = -\frac {2a\sin(a\pi)} \pi \sum_{k = 1}^{+\infty} \frac 1 {k^2 - a^2} \\
\sum_{k = 1}^{+\infty} \frac 1 {k^2 - a^2} & = \frac {1} {2a^2} - \frac {\pi\cos(a\pi)} {2a \sin(a\pi)} \\
& = \frac 1 {2a^2} - \frac \pi {2a} \cot(a\pi)
\end{aligned}$$
