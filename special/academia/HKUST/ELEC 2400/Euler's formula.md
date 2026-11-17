---
aliases:
  - ELEC 2400 Euler's formula
  - ELEC2400 Euler's formula
  - Euler's formula
  - HKUST ELEC 2400 Euler's formula
  - HKUST ELEC2400 Euler's formula
  - complex exponential
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/Euler_s_formula
  - language/in/English
---

# Euler's formula

Leonhard Euler (1707-1783) showed that the complex exponential and the trigonometric functions are the same thing, $e^{j\theta} = \cos\theta + j\sin\theta$ for every real $\theta$. So the unit-magnitude exponential $e^{j\theta}$ holds a whole sinusoid, with the cosine as its real part and the sine as its imaginary part, $\cos\theta = \operatorname{Re}(e^{j\theta})$ and $\sin\theta = \operatorname{Im}(e^{j\theta})$.

As $\theta$ grows, $e^{j\theta}$ runs around the unit circle of the complex plane. The angle notation is shorthand for that same object, $\angle\theta \equiv e^{j\theta}$, and a complex number in polar form is a magnitude times one exponential, $z = re^{j\theta}$.

---

Flashcards for this section are as follows:

- the statement: what does Euler's formula say, and when does it hold? ::@:: $e^{j\theta} = \cos\theta + j\sin\theta$, for every real $\theta$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- extracting the trigonometric parts: how do $\cos\theta$ and $\sin\theta$ come out of $e^{j\theta}$? ::@:: $\cos\theta = \operatorname{Re}(e^{j\theta})$ and $\sin\theta = \operatorname{Im}(e^{j\theta})$, the real and imaginary parts.
- the unit circle: what path does $e^{j\theta}$ trace as $\theta$ increases? ::@:: The unit circle: every $e^{j\theta}$ has magnitude $1$ and angle $\theta$, so it runs around the origin at unit radius.
- the angle notation: what does $\angle\theta$ stand for? ::@:: $\angle\theta \equiv e^{j\theta}$, the unit-magnitude complex number at angle $\theta$; $r\angle\theta$ is $re^{j\theta}$.
- common values: what are $e^{j0}$, $e^{j\pi/2}$, $e^{j\pi}$, and $e^{j3\pi/2}$? ::@:: $e^{j0} = 1$, $e^{j\pi/2} = j$, $e^{j\pi} = -1$, and $e^{j3\pi/2} = -j$, the four unit-circle points on the axes.
- Euler's identity: what does Euler's formula become at $\theta = \pi$, and what is that case called? ::@:: $e^{j\pi} = -1$, that is $e^{j\pi} + 1 = 0$, known as Euler's identity.

## power series derivation

The exponential is defined by its series, $e^x = \sum_{n=0}^{\infty}\frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$, which converges for every $x$. It converges absolutely for every complex argument too, since $\sum\frac{|x|^n}{n!}$ is the same series at $|x|$. Substituting $x = j\theta$ is therefore legitimate, and the terms may be rearranged.

With $j^2 = -1$ the powers of $j$ repeat in a four-step cycle, $j^{2k} = (-1)^k$ and $j^{2k+1} = j(-1)^k$. The even terms of the series therefore turn real and the odd ones imaginary, $e^{j\theta} = \left(1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \dots\right) + j\left(\theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \dots\right)$.

The two brackets are the Taylor series of $\cos\theta$ and $\sin\theta$, so $e^{j\theta} = \cos\theta + j\sin\theta$. They also say which part of the exponential each trigonometric function is: the even part of the series and the odd part. That is why one is symmetric about zero and the other antisymmetric.

---

Flashcards for this section are as follows:

- power series derivation / the exponential series: what series defines $e^x$, and why may a complex argument be put into it? ::@:: $e^x = \sum_{n=0}^{\infty}\frac{x^n}{n!}$; the same series at $|x|$ converges for every value, its absolute convergence carries to every complex argument, and the terms of the result may be rearranged.
- power series derivation / the powers of $j$: what are $j^{2k}$ and $j^{2k+1}$ for a whole number $k$? ::@:: $j^{2k} = (-1)^k$ and $j^{2k+1} = j(-1)^k$, a four-step cycle through $1$, $j$, $-1$, and $-j$.
- power series derivation / splitting the series: how does $e^{j\theta}$ split into a real and an imaginary part? ::@:: The even powers of $j\theta$ turn real and the odd ones imaginary, giving $e^{j\theta} = \left(1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \dots\right) + j\left(\theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \dots\right)$.
- power series derivation / recognising the brackets: which two series are the brackets, and what follows for Euler's formula? ::@:: The real bracket is the Taylor series of $\cos\theta$ and the imaginary one that of $\sin\theta$, so $e^{j\theta} = \cos\theta + j\sin\theta$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- power series derivation / even and odd parts: what does the derivation make of $\cos\theta$ and $\sin\theta$ inside the exponential? ::@:: They are the even and the odd part of the exponential series, which is why $\cos$ is symmetric about zero and $\sin$ antisymmetric.

## two trigonometric series

Read backwards, the same substitution writes the trigonometric functions with exponentials. The even and odd parts of $e^{j\theta}$ are $\cos\theta = \frac{e^{j\theta} + e^{-j\theta}}{2}$ and $\sin\theta = \frac{e^{j\theta} - e^{-j\theta}}{2}$, each one a conjugate pair.

---

Flashcards for this section are as follows:

- the two trigonometric series / cosine from exponentials: how is $\cos\theta$ written with complex exponentials? ::@:: $\cos\theta = \frac{e^{j\theta} + e^{-j\theta}}{2}$, the even part: the two conjugates add and the imaginary terms cancel.
- the two trigonometric series / sine from exponentials: how is $\sin\theta$ written with complex exponentials? ::@:: $\sin\theta = \frac{e^{j\theta} - e^{-j\theta}}{2}$, the odd part: the difference of the two conjugates leaves twice the imaginary part.
