---
aliases:
  - HKUST MATH 1014 L1 assignment 1 submission
tags:
  - date/2024/02/19
  - language/in/English
---

# L1 assignment 1 submission

- HKUST MATH 1014

Please do not use the [fundamental theorem of calculus](../../../../../general/fundamental%20theorem%20of%20calculus.md) in this assignment.

## 1

Evaluate each of the following integrals by considering some simple geometric shape.

_Hint_: First sketch the graph of each integrand.

### 1.a

$\int_0^3 \! \lfloor x \rfloor \,\mathrm{d}x$

> ![sketch 1.a](attachments/Pasted%20image%2020240218160236.png)
>
> $$\begin{aligned}
> \int_0^3 \! \lfloor x \rfloor \,\mathrm{d}x & = 0 (1 - 0) + 1 (2 - 1) + 2 (3 - 2) \\
> & = 0 + 1 + 2 \\
> & = 3
> \end{aligned}$$

### 1.b

$\int_0^3 \! (3 - \lvert x - 1 \rvert - \lvert x - 2 \rvert) \,\mathrm{d}x$

> ![sketch 1.b](attachments/Pasted%20image%2020240218161035.png)
>
> $$\begin{aligned}
> \int_0^3 \! (3 - \lvert x - 1 \rvert - \lvert x - 2 \rvert) \,\mathrm{d}x & = \int_0^3 \! 3 \,\mathrm{d}x - \int_0^3 \! \lvert x - 1 \rvert \,\mathrm{d}x - \int_0^3 \! \lvert x - 2 \rvert \,\mathrm{d}x \\
> & = 3(3 - 0) - \left( \frac {1(1 - 0)} 2 + \frac {2(3 - 1)} 2 \right) - \left( \frac {2(2 - 0)} 2 + \frac {1(3 - 2)} 2 \right) \\
> & = 9 - \left( \frac 1 2 + 2 \right) - \left( 2 + \frac 1 2 \right) \\
> & = 4
> \end{aligned}$$

### 1.c

$\int_0^a \! \sqrt{4 - x^2} \,\mathrm{d}x$, where $0 \le a \le 2$

> ![sketch 1.c](attachments/Pasted%20image%2020240218162228.png)
>
> $$\begin{aligned}
> \int_0^a \! \sqrt{4 - x^2} \,\mathrm{d}x & = \pi \cdot 2^2 \cdot \frac {\arcsin \frac a 2} {2 \pi} + \frac { a \sqrt{4 - a^2} } 2 \\
> & = 2 \arcsin \frac a 2 + \frac 1 2 a \sqrt{4 - a^2}
> \end{aligned}$$

## 2

Find the pair of real numbers $a, b \in [0, 2\pi]$ with $a < b$ such that the integral

$$\int_a^b \! (\sin x - \cos x) \,\mathrm{d}x$$

...

Give justifications to your answers.

### 2.a

... attains its maximum possible value.

> $$\begin{aligned}
> & \begin{aligned} \sin x - \cos x & = 0 \\
> \sin x & = \cos x \end{aligned} \\
> & \text{Case 1. } \cos x = 0 \\
> & \begin{aligned} \sin^2 x + \cos^2 x & = 1 \\
> \sin^2 x & = 1 \\
> \sin x & = \pm 1 \\
> & \ne \cos x \end{aligned} \\
> & \text{There are no solutions for }x\text{ when }\cos x = 0\text{.} \\
> & \text{Case 2. } \cos x \ne 0 \\
> & \begin{aligned} \sin x & = \cos x \\
> \frac {\sin x} {\cos x} & = 1 && (\cos x \ne 0) \\
> \tan x & = 1 \\
> x & = \frac \pi 4 + n \pi && n \in \mathbb{Z} \end{aligned} \\
> & \text{Within }[0, 2\pi]\text{, }x = \frac \pi 4 \text{ or }x = \frac {5 \pi} 4\text{.} \\
> & \text{Using }\sin x - \cos x\text{ is continuous on }[0, 2\pi]\text{,} \\
> & \text{by the intermediate value theorem,} \\
> & \sin x - \cos x\text{ does not change its sign on }\left[ 0, \frac \pi 4 \right), \left( \frac \pi 4, \frac {5 \pi} 4 \right), \left( \frac {5 \pi} 4, 2 \pi \right]\text{.} \\
> & \text{By evaluating }\sin x - \cos x\text{ in each of the above intervals, we get} \\
> & \operatorname{sgn}(\sin x - \cos x) = \begin{cases} -1 & x \in \left[0, \frac \pi 4 \right) \\
> 0 & x = \frac \pi 4 \\
> 1 & x \in \left( \frac \pi 4, \frac {5 \pi} 4 \right) \\
> 0 & x = \frac {5 \pi} 4 \\
> -1 & x \in \left( \frac {5 \pi} 4, 2 \pi \right] \end{cases} \\
> & \text{To attain the maximum value for the integral,} \\
> & \text{select an interval such that the integrand} \\
> & \text{has the most area for positive values} \\
> & \text{and the least area in negative values.} \\
> & \text{In this case, }(a, b) = \left( \frac \pi 4, \frac {5 \pi} 4 \right)
> \end{aligned}$$

### 2.b

... attains its minimum possible value.

> ![sketch 2.b](attachments/Pasted%20image%2020240218172043.png)
>
> $$\begin{aligned}
> & \text{Continuing from 2.a.} \\
> & \text{To attain the maximum value for the integral,} \\
> & \text{select an interval such that the integrand} \\
> & \text{has the least area for positive values} \\
> & \text{and the most area in negative values.} \\
> & \text{In this case, }(a, b) = \left( \frac {5 \pi} 4, 2 \pi \right) \\
> & \text{We can confirm this by inspecting the sketch above.}
> \end{aligned}$$

## 3

Let $f(x) = \cos \left( x^2 \right)$ and $g(x) = \cos \left( x^3 \right)$. For each of the following pairs of integrals, explain which one has a greater value.

### 3.a

$\int_0^1 \! f(x) \,\mathrm{d}x$ and $\int_0^1 \! g(x) \,\mathrm{d}x$

> $$\begin{aligned}
> & \text{Considering }x \in (0, 1) \\
> & \begin{aligned} x^2 & > x^3 \\
> \cos \left( x^2 \right) & < \cos \left( x^3 \right) && (\cos * \text{ is strictly decreasing on } (0, 1)) \\
> f(x) & < g(x) \\
> \int_0^1 \! f(x) \,\mathrm{d}x & < \int_0^1 \! g(x) \,\mathrm{d}x && (\text{the values of } f(0), f(1), g(0), g(1) \text{ do not affect the inequality as }\set{0, 1}\text{ has zero Lebesgue measure}) \end{aligned}
> \end{aligned}

### 3.b

$\int_0^1 \! f(x) \,\mathrm{d}x$ and $\int_{\cos 1}^1 f^{-1} (x) \,\mathrm{d}x$

(Note that $f$ has an inverse defined on $[\cos 1, 1]$ because $f: [0, 1] \to [\cos 1, 1]$ is strictly decreasing.)

> ![sketch 3.b](attachments/Pasted%20image%2020240218174815.png)
>
> $$\begin{aligned}
> & \text{Refer to the sketch above.} \\
> & \text{The red area is the value of the first integral,} \\
> & \text{and the green area is the value of the second integral.} \\
> & \text{The colored arrows shows the integration orientation,} \\
> & \text{showing that both orientation are both positive} \\
> & \text{to check that the red and green area are indeed the values of the integral}. \\
> & \text{It can be seen that the red area is greater than the green area.} \\
> &\text{Hence, } \int_0^1 \! f(x) \,\mathrm{d}x > \int_{\cos 1}^1 \! f^{-1} (x) \,\mathrm{d}x \text{.}
> \end{aligned}$$

## 5

### 5.a

Let $a \ge 2$ be a real number. By considering appropriate trapeziums, show that

$$\int_{a - \frac 1 2}^{a + \frac 1 2} \! \ln x \,\mathrm{d}x \le \ln a \qquad \text{ and } \qquad \int_{a - 1}^a \! \ln x \,\mathrm{d}x \ge \frac {\ln (a - 1) + \ln a} 2$$

> $$\begin{aligned}
> & \text{Considering }a \ge 2\text{, all operations below involving }\ln *\text{ produces nonnegative results.} \\
> \\
> & \text{Consider the rectangle under by }y = \ln a\text{ on }\left[ a - \frac 1 2, a + \frac 1 2 \right]\text{.} \\
> & \text{Its area is }\left( a + \frac 1 2 - \left( a - \frac 1 2 \right) \right) \ln a = \ln a\text{.} \\
> & \text{Rotate the graph of }y = \ln a\text{ with }(a, \ln a)\text{ as the pivot} \\
> & \text{such that the graph becomes tangent to}\ln x\text{ at }(a, \ln a)\text{,} \\
> & \text{i.e. }y = \left( \frac{\mathrm{d} }{\mathrm{d}u}\Bigr|_{u = a} \ln u \right) (x - a) + \ln a\text{.} \\
> & \text{The rectangle becomes a trapezium.} \\
> & \text{The area of the trapezium is the same as the rectangle because} \\
> & \text{the left side decreases by as much as the right side increases.} \\
> & \text{Since }\ln x\text{ is a concave function,} \\
> & \text{the tangent line is always higher than }\ln x\text{ except at }a\text{,} \\
> & \text{where they meet.} \\
> & \text{Then,} \\
> & \begin{aligned} \ln x & \le \left( \frac{\mathrm{d} }{\mathrm{d}u}\Bigr|_{u = a} \ln u \right) (x - a) + \ln a && \left( x \in \left[ a - \frac 1 2, a + \frac 1 2 \right] \right) \\
> \int_{a - \frac 1 2}^{a + \frac 1 2} \! \ln x \,\mathrm{d}x & \le \int_{a - \frac 1 2}^{a + \frac 1 2} \! \left( \left( \frac{\mathrm{d} }{\mathrm{d}u}\Bigr|_{u = a} \ln u \right) (x - a) + \ln a \right) \,\mathrm{d}x \\
> & \le \int_{a - \frac 1 2}^{a + \frac 1 2} \! \ln a \,\mathrm{d}x && (\text{the trapezium and the rectangle have the same area}) \\
> & \le \left( a + \frac 1 2 - \left( a - \frac 1 2 \right) \right) \ln a \\
> & \le \ln a \end{aligned} \\
> \\
> & \frac {\ln (a - 1) + \ln a} 2 \text{ is the area of the trapezium enclosed by} \\
> & \text {the line segment joining }(a - 1, \ln(a - 1))\text{ and }(a, \ln a)\text{, } \\
> & x = a - 1\text{, }x = a\text{, and the }x\text{-axis.} \\
> & \text{The equation of the line segment extended to infinity is } \\
> & y = (\ln a - \ln (a - 1)) (x - a) + \ln a \text{.} \\
> & \text{Since }\ln x\text{ is a concave function,} \\
> & \text{all points in a line segment connecting two points on }\ln x \\
> & \text{are always lower than }\ln x\text{ except for the end points, where they meet.} \\
> & \text{Then,} \\
> & \begin{aligned} \ln x & \ge (\ln a - \ln (a - 1))(x - a) + \ln a && (x \in \left[ a - 1, a \right]) \\
> \int_{a - 1}^a \! \ln x \,\mathrm{d}x & \ge \int_{a - 1}^a \! ((\ln a - \ln (a - 1))(x - a) + \ln a) \,\mathrm{d}x \\
> & \ge \frac {\ln (a - 1) + \ln a} 2 && (\text{area of the trapezium}) \end{aligned}
> \end{aligned}$$

### 5.b

Using the result from [5.a](#5.a), deduce that

$$\int_{\frac 3 2}^n \! \ln x \,\mathrm{d}x \le \ln(n!) - \frac 1 2 \ln n \le \int_1^n \! \ln x \,\mathrm{d}x$$

for every integer $n \ge 2$.

> $$\begin{aligned}
> \ln(n!) - \frac 1 2 \ln n & = \sum_{i = 1}^n \ln i - \frac 1 2 \ln n \\
> & = \sum_{i = 2}^n \ln i - \frac 1 2 \ln n \\
> & \ge \sum_{i = 2}^n \int_{i - \frac 1 2}^{i + \frac 1 2} \! \ln x \,\mathrm{d}x - \frac 1 2 \ln n && (\text{5.a}) \\
> & = \int_{\frac 3 2}^n \! \ln x \,\mathrm{d}x + \int_n^{n + \frac 1 2} \! \ln x \,\mathrm{d}x - \frac 1 2 \ln n \\
> & \ge \int_{\frac 3 2}^n \! \ln x \,\mathrm{d}x + \left( n + \frac 1 2 - n \right) \ln x - \frac 1 2 \ln x && (\ln *\text{ is strictly increasing}) \\
> & = \int_{\frac 3 2}^n \! \ln x \,\mathrm{d}x \\
> \ln(n!) - \frac 1 2 \ln n & = \sum_{i = 1}^n \ln i - \frac 1 2 \ln n \\
> & = \sum_{i = 2}^n \ln i - \frac 1 2 \ln n \\
> & = \sum_{i = 2}^n \frac {\ln (i - 1) + \ln i} 2 - \frac 1 2 \ln 1 + \frac 1 2 \ln n - \frac 1 2 \ln n \\
> & = \sum_{i = 2}^n \frac {\ln (i - 1) + \ln i} 2 \\
> & \le \sum_{i = 2}^n \int_{i - 1}^i \! \ln x \,\mathrm{d}x && (\text{5.a}) \\
> & = \int_1^n \! \ln x \,\mathrm{d}x \\
> \int_{\frac 3 2}^n \! \ln x \,\mathrm{d}x & \le \ln(n!) - \frac 1 2 \ln n \le \int_1^n \! \ln x \,\mathrm{d}x
> \end{aligned}$$

## 8

Evaluate the following limits. Do not use the [fundamental theorem of calculus](../../../../../general/fundamental%20theorem%20of%20calculus.md) when computing any integral.

### 8.a

$$\lim_{n \to +\infty} \sum_{k = 1}^n \frac { \sqrt{n^2 - k^2} } {n^2}$$

> $$\begin{aligned}
> \lim_{n \to +\infty} \sum_{k = 1}^n \frac { \sqrt{n^2 - k^2} } {n^2} & = \lim_{n \to +\infty} \frac 1 n \sum_{k = 1}^n \frac{ \sqrt{n^2 - k^2} } n \\
> & = \lim_{n \to +\infty} \frac 1 n \sum_{k = 1}^n \sqrt{1 - \left( \frac k n \right)^2} \\
> & = \int_0^1 \! \sqrt{1 - x^2} \,\mathrm{d}x && (\text{the integrand is bounded and continuous, so it is integrable}) \\
> & = \frac \pi 4 && (\text{area of quarter of circle of radius }1)
> \end{aligned}$$

### 8.b

$$\lim_{n \to +\infty} \frac 1 {n^2} \left( \sqrt{n - 1} + \sqrt{2n - 4} + \sqrt{3n - 9} + \cdots + \sqrt{n^2 - n^2} \right)$$

> $$\begin{aligned}
> \lim_{n \to +\infty} \frac 1 n \sum_{k = 1}^n \sqrt{\frac k n - \left( \frac k n \right)^2} & = \int_0^1 \! \sqrt{x - x^2} \,\mathrm{d}x && (\text{the integrand is bounded and continuous, so it is integrable}) \\
> & = \int_0^1 \! \sqrt{x(1 - x)} \,\mathrm{d}x \\
> & = 2 \int_0^{\frac 1 2} \! \sqrt{x(1 - x)} \,\mathrm{d}x && (\text{symmetry}) \\
> & = 2 \int_0^{\frac 1 2} \! \sqrt{\left( \frac 1 2 + x \right) \left( \frac 1 2 - x \right)} \,\mathrm{d}x && (\text{integrate in reverse direction}) \\
> & = 2 \int_0^{\frac 1 2} \! \sqrt{\frac 1 4 - x^2} \,\mathrm{d}x \\
> & = 2 \cdot \frac \pi 4 \left( \frac 1 2 \right)^2 && \left( \text{area of quarter of circle of radius } \frac 1 2 \right) \\
> & = \frac \pi 8
> \end{aligned}$$

## 10

### 10.a

Let $t$ be a real number such that $\sin \frac t 2 \ne 0$ and let $n$ be a positive integer. Show that

$$\sum_{k = 1}^n \sin kt = \frac {\cos \frac t 2 - \cos \left( n + \frac 1 2 \right) t} {2 \sin \frac t 2}$$

> $$\begin{aligned}
> & \begin{aligned} \sum_{k = 1}^n \sin kt & = \frac 1 {\sin \frac t 2} \sum_{k = 1}^n \sin \frac t 2 \sin kt \\
> & = \frac 1 {2 \sin \frac t 2} \sum_{k = 1}^n \left( \cos \left( k - \frac 1 2 \right) t - \cos \left(k + \frac 1 2 \right) t \right) \\
> & = \frac 1 {2 \sin \frac t 2} \left( \cos \left( 1 - \frac 1 2 \right) t - \cos \left( n + \frac 1 2 \right) t \right) \\
> & = \frac {\cos \frac t 2 - \cos \left( n + \frac 1 2 \right) t} {2 \sin \frac t 2} \end{aligned} \\
> \\
> & \text{Alternatively,} \\
> & \begin{aligned} \sum_{k = 1}^n \sin kt & = \sum_{k = 1}^n \operatorname{Im} \left\{ e^{kti} \right\} \\
> & = \operatorname{Im} \left\{ \sum_{k = 1}^n e^{kti} \right\} \\
> & = \operatorname{Im} \left\{ \frac {e^{(n + 1)ti} - e^{ti} } {e^{ti} - 1} \right\} \\
> & = \operatorname{Im} \left\{ \frac {e^{\left( n + \frac 1 2 \right) ti} - e^{\frac t 2 i} } {e^{\frac t 2 i} - e^{-\frac t 2 i} } \right\} \\
> & = \operatorname{Im} \left\{ \frac {e^{\left( n + \frac 1 2 \right) ti} - e^{\frac t 2 i} } {2i \sin \frac t 2} \right\} \\
> & = \operatorname{Im} \left\{ \frac {\cos \left( n + \frac 1 2 \right) t + i \sin \left( n + \frac 1 2 \right) t - \cos \frac t 2 - i \sin \frac t 2} {2i \sin \frac t 2} \right\} \\
> & = \operatorname{Im} \left\{ \frac {-i \cos \left( n + \frac 1 2 \right) t + \sin \left( n + \frac 1 2 \right) t + i \cos \frac t 2 - \sin \frac t 2} {2 \sin \frac t 2} \right\} \\
> & = \frac {\cos \frac t 2 - \cos \left( n + \frac 1 2 \right) t} {2 \sin \frac t 2} \end{aligned}
> \end{aligned}$$

### 10.b

Hence for each $a > 0$, evaluate

$$\int_0^a \! \sin t \,\mathrm{d}t$$

from the definition of a Riemann integral.

> $$\begin{aligned}
> \int_0^a \! \sin t \,\mathrm{d}t & = \lim_{n \to +\infty} \frac a n \sum_{k = 1}^n \sin k \frac a n \\
> & = \lim_{n \to +\infty} \frac a n \frac {\cos \frac a {2n} - \cos \left( n + \frac 1 2 \right) \frac a n } {2 \sin \frac a {2n} } && \left( (\forall a \in \mathbb{R}_{> 0})(\exists N \in \mathbb{N}_{\ne 0})(\forall n \in \mathbb{N}_{\ne 0}) \left( n \ge N \implies \sin \frac a {2n} \ne 0 \right) \right) \\
> & = \lim_{n \to +\infty} \frac a n \frac {2 \sin \frac {n + 1} 2 \frac a n \sin \frac n 2 \frac a n} { 2 \sin \frac a {2n} } \\
> & = \lim_{n \to +\infty} \frac a n \frac {\sin \frac {na + a} {2n} \sin \frac a 2} { \sin \frac a {2n} } \\
> & = \lim_{n \to +\infty} \frac a n \left( \sin \frac a 2 \right) \frac {\sin \frac a 2 \cos \frac a {2n} + \sin \frac a {2n} \cos \frac a 2} { \sin \frac a {2n} } \\
> & = \lim_{n \to +\infty} \frac a n \left( \sin^2 \frac a 2 \cot \frac a {2n} + \sin \frac a 2 \cos \frac a 2 \right) \\
> & = \lim_{n \to +\infty} \left(2 \sin^2 \frac a 2 \frac {\frac a {2n} } {\tan \frac a {2n} } + \frac a n \sin \frac a 2 \cos \frac a 2 \right) \\
> & = 2 \sin^2 \frac a 2 \\
> & = 1 - \cos a
> \end{aligned}$$

## 13

Let $m$ be a non-negative real number.

### 13.a

Let $g: [0, 1] \to [0, +\infty)$ be a non-negative integrable function such that

$$g(x) \le mx \qquad \text{ and } \qquad g(x) \le m(1 - x)$$

for every $x \in [0, 1]$. Show that

$$\int_0^1 \! g(x) \,\mathrm{d}x \le \frac m 4$$

> $$\begin{aligned}
> \int_0^1 \! g(x) \,\mathrm{d}x & = \int_0^{\frac 1 2} \! g(x) \,\mathrm{d}x + \int_{\frac 1 2}^1 \! g(x) \,\mathrm{d}x \\
> & \le \int_0^{\frac 1 2} mx \,\mathrm{d}x + \int_{\frac 1 2}^1 m(1 - x) \,\mathrm{d}x \\
> & = 2 \cdot \frac 1 2 \cdot \frac 1 2 \cdot \frac m 2 && \left( \text{two triangles of base }\frac 1 2\text{ and height }\frac m 2 \right) \\
> & = \frac m 4
>\end{aligned}$$

### 13.b

Let $f: [0, 1] \to \mathbb{R}$ be a function that is continuous on $[0, 1]$ and differentiable on $(0, 1)$. Suppose that $f(0) = f(1) = 0$ and $\lvert f'(x) \rvert \le m$ for every $x \in (0, 1)$. Using the result from [13.a](#13.a), show that

$$\int_0^1 \! \lvert f(x) \rvert \,\mathrm{d}x \le \frac m 4$$

> $$\begin{aligned}
> & \begin{aligned} \forall x \in (0, 1] \\
> \frac{f(x) - f(0)} {x - 0} & = f'(a) \quad \exists a \in (0, x) && (\text{mean value theorem}) \\
> \frac {f(x)} x & = f'(a) \\
> f(x) & = x f'(a) && (x > 0) \\
> \lvert f(x) \rvert & = x \lvert f'(a) \rvert && (x > 0) \\
> & \le mx \\
> f(x) & \le mx \quad \forall x \in [0, 1] && (f(0) = 0) \\
> \\
> \forall x \in [0, 1) \\
> \frac{f(1) - f(x)} {1 - x} & = f'(a) \quad \exists a \in (x, 1) && (\text{mean value theorem}) \\
> -\frac {f(x)} {1 - x} & = f'(a) \\
> -f(x) & = (1 - x) f'(a) && (x < 1) \\
> \lvert f(x) \rvert & = (1 - x) \lvert f'(a) \rvert && (x < 1) \\
> & \le m (1 - x) \\
> f(x) & \le m (1 - x) \quad \forall x \in [0, 1] && (f(1) = 0) \end{aligned} \\
> \\
> & \text{Obviously }\lvert f(x) \rvert\text{ is nonnegative.} \\
> & \because f(x)\text{ is bounded and continuous on }[0, 1] \\
> & \therefore \lvert f(x) \rvert\text{ is bounded and continuous on }[0, 1] \\
> & \therefore \lvert f(x) \rvert\text{ is (Riemann) integrable on }[0, 1] \\
> \\
> & \because \lvert f(x) \rvert \text{ satisfies all conditions for }g(x)\text{ in 13.a,} \\
> & \therefore \int_0^1 \! \lvert f(x) \rvert \,\mathrm{d}x \le \frac m 4
> \end{aligned}$$

### 13.c

Using the result from [13.b](#13.b), show that

$$\int_0^1 \! \lvert \sin(mx(x - 1)) \rvert \,\mathrm{d}x \le \frac m 4$$

> $$\begin{aligned}
> & h(x) := \sin(mx(x - 1)) \\
> & \text{By inspection, }h(x)\text{ is continuous and differentiable on }\mathbb{R}\text{.} \\
> \\
> & \begin{aligned} h(0) & = \sin(m (0) (0 - 1)) \\
> & = 0 \\
> h(1) & = \sin(m (1) (1 - 1)) \\
> & = 0 \\
> \\
> \forall x \in [0, 1] \\
> h'(x) & = \cos(mx(x - 1)) m (2x - 1) \\
> \lvert h'(x) \rvert & = m \lvert \cos(mx(x - 1)) (2x - 1) \rvert && (m \ge 0) \\
> & \le m \lvert 2x - 1 \rvert && (\lvert \cos * \rvert \le 1) \\
> & \le m && (\lvert 2x - 1 \rvert \le 1) \end{aligned} \\
> \\
> & \because \text{The restriction of }h(x)\text{ to }[0, 1]\text{ satisfies all conditions for }f(x)\text{ in 13.b,} \\
> & \therefore \int_0^1 \! \lvert \sin(mx(x - 1)) \rvert \,\mathrm{d}x \le \frac m 4
> \end{aligned}$$

## 15

Let $a < b$ be real numbers, let $f: [a, b] \to (0, +\infty)$ be a __positive__ continuous function, and let $g: [a, b] \to \mathbb{R}$ be the function

$$g(x) = \int_a^x \! f(t) \,\mathrm{d}t + \int_b^x \frac 1 {f(t)} \,\mathrm{d}t$$

### 15.a

Show from definition (Definition 5.49) that $g$ is __strictly__ increasing on $[a, b]$.

> $$\begin{aligned}
> & \forall x \in [a, b] \\
> & \because f(x) > 0 \\
> & \therefore \frac 1 {f(x)} > 0 \\
> & \\
> & \forall x, y \in [a, b], \text{where } x > y \\
> & \begin{aligned} g(x) & = \int_a^x \! f(t) \,\mathrm{d}t + \int_b^x \frac 1 {f(t)} \,\mathrm{d}t \\
> & = \int_a^y \! f(t) \,\mathrm{d}t + \int_b^y \! \frac 1 {f(t)} \,\mathrm{d}t + \int_y^x \! f(t) \,\mathrm{d}t + \int_y^x \! \frac 1 {f(t)} \,\mathrm{d}t \\
> & = g(y) + \int_y^x \! f(t) \,\mathrm{d}t + \int_y^x \! \frac 1 {f(t)} \,\mathrm{d}t \\
> & > g(y) + \int_y^x \! 0 \,\mathrm{d}t + \int_y^x \! 0 \,\mathrm{d}t && \left( x > y, f(t) > 0, \frac 1 {f(t)} > 0 \right) \\
> & > g(y) \end{aligned}
> \end{aligned}$$

### 15.b

Suppose it is given that $g$ is continuous on $[a, b]$ (This fact actually follows immediately from Lemma 5.50 in §5.4). Show that $g$ has one and only one root in $[a, b]$.

> $$\begin{aligned}
> & \begin{aligned} g(a) & = \int_a^a \! f(t) \,\mathrm{d}t + \int_b^a \! \frac 1 {f(t)} \,\mathrm{d}t \\
> & = \int_b^a \! \frac 1 {f(t)} \,\mathrm{d}t \\
> & = \int_a^b \! -\frac 1 {f(t)} \,\mathrm{d}t \\
> & < \int_a^b \! 0 \,\mathrm{d}t && \left(a < b, -\frac 1 {f(t)} < 0 \right) \\
> g(b) & = \int_a^b \! f(t) \,\mathrm{d}t + \int_b^b \! \frac 1 {f(t)} \,\mathrm{d}t \\
> & = \int_a^b \! f(t) \,\mathrm{d}t \\
> & > \int_a^b \! 0 \,\mathrm{d}t && (a < b, f(t) > 0) \end{aligned} \\
> \\
> & \because g\text{ is continuous on }[a, b]\text{,} \\
> & \therefore (\exists x \in [a, b])(g(x) = 0) \text{ by the intermediate value theorem.} \\
> \\
> & \because g\text{ is strictly increasing on }[a, b]\text{,} \\
> & \therefore g\text{ is injective on }[a, b]\text{.} \\
> & \therefore g(x) = g(y) \implies x = y \\
> & \text{Let }x, y\text{ be roots of }g\text{ that may or may not be distinct.} \\
> & \because g(x) = g(y) = 0 \\
> & \therefore x = y \\
> & \therefore g\text{ has at most one root.} \\
> \\
> & \because g\text{ has at least one root and at most one root,} \\
> & \therefore g\text{ has one and only one root.}
> \end{aligned}$$
