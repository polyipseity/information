---
aliases:
  - factorial, power, and modular arithmetic
tags:
  - date/2024/03/02/from
  - date/2024/03/04/to
  - flashcard/active/special/questions/factorial__power__and_modular_arithmetic
  - language/in/English
  - question/mathematics/modular_arithmetic
  - question/mathematics/number_theory
  - question/mathematics/perfect_power
---

# factorial, power, and modular arithmetic

- credit: [Older Amateur](https://math.stackexchange.com/a/4836664), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), via Mathematics Stack Exchange
- datetime: 2024-03-02T17:55:20.242+08:00

Prove that $$\sqrt{ \sum_{n = 1}^{N \ge 12} n!^m } \notin \mathbb{Z} \qquad m \in \mathbb{Z}_{\ge 1}$$.

## strategy

- inspecting "$$\sqrt{ \sum_{n = 1}^{N \ge 12} n!^m } \notin \mathbb{Z} \qquad m \in \mathbb{Z}_{\ge 1}$$" :@: Problems involving integers may be solvable using modular arithmetic... In this specific case, consider square numbers modulus some numbers. Then consider the formula in question, ignoring the square root, modulus the same numbers. <!--SR:!2025-09-03,259,250-->
- modular arithmetic tricks :@: Modular exponentiation cycles (e.g. $2^n \pmod m$) are your friends when dealing with exponentiation in modular arithmetic. And modular power cycles (e.g. $n^2 \pmod m$), but this is relatively trivial. <!--SR:!2025-01-20,135,290-->
- numbers to modulus :@: Start checking from 2. The solution below uses $m = 3, 5, 9, 13$. <!--SR:!2025-04-03,185,270-->
- desired outcome of modular arithmetic :@: Prove that under modular arithmetic, the formula in question without the square root does not equal all possible square numbers. <!--SR:!2025-10-19,318,290-->

## solution

- credit: [Older Amateur](https://math.stackexchange.com/a/4836664), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), via Mathematics Stack Exchange

First, it is helpful to visualize the above sum as the following form:

$$\begin{aligned}
\text{height of } m \begin{cases} \begin{matrix} 1 \\ 1 \\ \vdots \\ 1 \end{matrix} + \begin{matrix} 1 & 2 \\ 1 & 2 \\ \vdots & \vdots \\ 1 & 2 \end{matrix} + \begin{matrix} 1 & 2 & 3 \\ 1 & 2 & 3 \\ \vdots & \vdots & \vdots \\ 1 & 2 & 3 \end{matrix} + \begin{matrix} 1 & 2 & 3 & 4 \\ 1 & 2 & 3 & 4 \\ \vdots & \vdots & \vdots & \vdots \\ 1 & 2 & 3 & 4 \end{matrix} + \cdots + \begin{matrix} 1 & 2 & \cdots & N \\ 1 & 2 & \cdots & N \\ \vdots & \vdots & \ddots & N \\ 1 & 2 & \cdots & N \end{matrix} \end{cases}
\end{aligned}$$

Consider square numbers modulus 3. They are congruent modulus 3 to:

$$\begin{aligned}
0^2 & \equiv 0 \pmod 3 \\
1^2 & \equiv 1 \pmod 3 \\
2^2 & \equiv 1 \pmod 3
\end{aligned}$$

It is impossible for a square number and 2 to be congruent modulus 3. Now consider the sum. Using the visualization above, one realize that the terms $n!^m \quad \forall n \ge 3$ does not change the sum modulus 3. So we only need to consider the first two terms: $1!^m + 2!^m = 1^m + 2^m$. The first two terms are congruent modulus 3 to:

$$\begin{aligned}
1^1 + 2^1 & \equiv 0 \pmod 3 \\
1^2 + 2^2 & \equiv 2 \pmod 3 \\
1^3 + 2^3 & \equiv 0 \pmod 3 \\
1^4 + 2^4 & \equiv 2 \pmod 3 \\
& \vdots
\end{aligned}$$

One can show that the above $0, 2, 0, 2, \ldots$ pattern holds by considering the modulus cycle for each term individually, which will be left as an exercise to the reader. This applies to below as well. Anyway, the sum cannot be a square number if $N \ge 2, m \equiv 0 \pmod 2$.

Now we repeat the above steps, but for modulus 5, 9, and 13.

$$\begin{aligned}
0^2 & \equiv 0 \pmod 5 \\
1^2 & \equiv 1 \pmod 5 \\
2^2 & \equiv 4 \pmod 5 \\
3^2 & \equiv 4 \pmod 5 \\
4^2 & \equiv 1 \pmod 5 \\
\\
\sum_{n = 1}^4 n!^1 & \equiv 3 \pmod 5 \\
\sum_{n = 1}^4 n!^2 & \equiv 2 \pmod 5 \\
\sum_{n = 1}^4 n!^3 & \equiv 4 \pmod 5 \\
\sum_{n = 1}^4 n!^4 & \equiv 4 \pmod 5 \\
\sum_{n = 1}^4 n!^5 & \equiv 3 \pmod 5 \\
\sum_{n = 1}^4 n!^6 & \equiv 2 \pmod 5 \\
\sum_{n = 1}^4 n!^7 & \equiv 4 \pmod 5 \\
\sum_{n = 1}^4 n!^8 & \equiv 4 \pmod 5 \\
& \vdots
\end{aligned}$$

Therefore, the sum cannot be a square number if $N \ge 4, m \equiv 1, 2 \pmod 4$.

$$\begin{aligned}
0^2 & \equiv 0 \pmod 9 \\
1^2 & \equiv 1 \pmod 9 \\
2^2 & \equiv 4 \pmod 9 \\
3^2 & \equiv 0 \pmod 9 \\
4^2 & \equiv 7 \pmod 9 \\
5^2 & \equiv 7 \pmod 9 \\
6^2 & \equiv 0 \pmod 9 \\
7^2 & \equiv 4 \pmod 9 \\
8^2 & \equiv 1 \pmod 9 \\
\\
\sum_{n = 1}^8 n!^1 & \equiv 0 \pmod 9 \\
\sum_{n = 1}^8 n!^2 & \equiv 5 \pmod 9 \\
\sum_{n = 1}^8 n!^3 & \equiv 0 \pmod 9 \\
\sum_{n = 1}^8 n!^4 & \equiv 8 \pmod 9 \\
\sum_{n = 1}^8 n!^5 & \equiv 6 \pmod 9 \\
\sum_{n = 1}^8 n!^6 & \equiv 2 \pmod 9 \\
\sum_{n = 1}^8 n!^7 & \equiv 3 \pmod 9 \\
\sum_{n = 1}^8 n!^8 & \equiv 5 \pmod 9 \\
\sum_{n = 1}^8 n!^9 & \equiv 0 \pmod 9 \\
\sum_{n = 1}^8 n!^{10} & \equiv 8 \pmod 9 \\
\sum_{n = 1}^8 n!^{11} & \equiv 6 \pmod 9 \\
\sum_{n = 1}^8 n!^{12} & \equiv 2 \pmod 9 \\
\sum_{n = 1}^8 n!^{13} & \equiv 3 \pmod 9 \\
& \vdots
\end{aligned}$$

It is normal for the first $N$ term modulus pattern to break when $m$ is small as some terms are not in the modulus cycle yet. Anyway, the sum cannot be a square number if $N \ge 8, m \ge 2, m \equiv 0, 1, 2, 4, 5 \pmod 6$.

$$\begin{aligned}
0^2 & \equiv 0 \pmod{13} \\
1^2 & \equiv 1 \pmod{13} \\
2^2 & \equiv 4 \pmod{13} \\
3^2 & \equiv 9 \pmod{13} \\
4^2 & \equiv 3 \pmod{13} \\
5^2 & \equiv 12 \pmod{13} \\
6^2 & \equiv 10 \pmod{13} \\
7^2 & \equiv 10 \pmod{13} \\
8^2 & \equiv 12 \pmod{13} \\
9^2 & \equiv 3 \pmod{13} \\
10^2 & \equiv 9 \pmod{13} \\
11^2 & \equiv 4 \pmod{13} \\
12^2 & \equiv 1 \pmod{13} \\
\\
\sum_{n = 1}^{12} n!^1 & \equiv 9 \pmod{13} \\
\sum_{n = 1}^{12} n!^2 & \equiv 4 \pmod{13} \\
\sum_{n = 1}^{12} n!^3 & \equiv 11 \pmod{13} \\
\sum_{n = 1}^{12} n!^4 & \equiv 0 \pmod{13} \\
\sum_{n = 1}^{12} n!^5 & \equiv 1 \pmod{13} \\
\sum_{n = 1}^{12} n!^6 & \equiv 11 \pmod{13} \\
\sum_{n = 1}^{12} n!^7 & \equiv 4 \pmod{13} \\
\sum_{n = 1}^{12} n!^8 & \equiv 0 \pmod{13} \\
\sum_{n = 1}^{12} n!^9 & \equiv 8 \pmod{13} \\
\sum_{n = 1}^{12} n!^{10} & \equiv 4 \pmod{13} \\
\sum_{n = 1}^{12} n!^{11} & \equiv 12 \pmod{13} \\
\sum_{n = 1}^{12} n!^{12} & \equiv 12 \pmod{13} \\
\sum_{n = 1}^{12} n!^{13} & \equiv 9 \pmod{13} \\
\sum_{n = 1}^{12} n!^{14} & \equiv 4 \pmod{13} \\
\sum_{n = 1}^{12} n!^{15} & \equiv 11 \pmod{13} \\
\sum_{n = 1}^{12} n!^{16} & \equiv 0 \pmod{13} \\
\sum_{n = 1}^{12} n!^{17} & \equiv 1 \pmod{13} \\
\sum_{n = 1}^{12} n!^{18} & \equiv 11 \pmod{13} \\
\sum_{n = 1}^{12} n!^{19} & \equiv 4 \pmod{13} \\
\sum_{n = 1}^{12} n!^{20} & \equiv 0 \pmod{13} \\
\sum_{n = 1}^{12} n!^{21} & \equiv 8 \pmod{13} \\
\sum_{n = 1}^{12} n!^{22} & \equiv 4 \pmod{13} \\
\sum_{n = 1}^{12} n!^{23} & \equiv 12 \pmod{13} \\
\sum_{n = 1}^{12} n!^{24} & \equiv 12 \pmod{13} \\
& \vdots
\end{aligned}$$

Therefore, the sum cannot be a square number if $N \ge 12, m \equiv 3, 6, 9 \pmod{12}$.

Now we combine the above conclusions:

$$\begin{aligned}
& m \in \mathbb{Z}_{\ge 1} \\
& \text{The sum cannot be a square number if...} \\
& N \ge 2, m \equiv 0 \pmod 2 && (N \ge 2, m \equiv 0 \pmod 2) \\
& N \ge 4, m \equiv 0, 1, 2 \pmod 4  && (N \ge 4, m \equiv 1, 2 \pmod 4) \\
& N \ge 8, m \equiv 0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11 \pmod{12} && (N \ge 8, m \ge 2, m \equiv 0, 1, 2, 4, 5 \pmod 6) \\
& N \ge 12, m \equiv 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 \pmod{12} && (N \ge 12, m \equiv 3, 6, 9 \pmod{12}) \\
& N \ge 12
\end{aligned}$$

Therefore:

$$\sqrt{ \sum_{n = 1}^{N \ge 12} n!^m } \notin \mathbb{Z} \qquad m \in \mathbb{Z}_{\ge 1}$$

∎
