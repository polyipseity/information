---
aliases:
  - HKUST MATH 1014 L1 assignment 8 submission
tags:
  - date/2024/05/12/from
  - date/2024/05/15/to
  - language/in/English
---

# HKUST MATH 1014 L1 assignment 8 submission

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

### Q5.a

#### Q5.a.i

#### Q5.a.ii

### Q5.b

#### Q5.b.i

## Q7

### Q7.b

### Q7.d

## Q9

### Q9.a

### Q9.b

## Q11

## Q13

### Q13.a

### Q13.b
