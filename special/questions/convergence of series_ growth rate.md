---
aliases:
  - 'convergence of series: growth rate'
tags:
  - date/2024/07/01/from
  - date/2024/07/02/to
  - flashcard/active/special/questions/convergence_of_series__growth_rate
  - language/in/English
  - question/mathematics/series
---

# convergence of series: growth rate

- datetime: 2024-07-01T23:12:04.682+08:00

Prove or disprove: If $a_n > 0$ for $n \gg 0$ and $\lim_{n \to +\infty} n a_n = 0$, then $\sum (-1)^n a_n$ converges.

## strategy

- inspecting "Prove or disprove: If $a_n > 0$ for $n \gg 0$ and $\lim_{n \to +\infty} n a_n = 0$, then $\sum (-1)^n a_n$ converges." :@: First, guess whether it converges. One can probably think of the alternating series test. <!--SR:!2026-12-12,558,270-->
- considering the alternating series test :@: It turns out we can make the series $(a_n)_{n \in \mathbb{Z}_{\ge 0} }$ violate the conditions. One may think of a way to violate it and hopefully it makes a divergent series... <!--SR:!2026-03-09,406,290-->
- making a sequence that diverges while satisfying $\lim_{n \to +\infty} n a_n = 0$ :@: Try multiplying $1 / n$ by $1 / \ln n$, which increases the denominator slow enough that it does not affect the divergence while satisfying the limit. <!--SR:!2025-06-14,224,270-->

## solution

$$\begin{aligned}
a_n & := \begin{cases} \frac 1 {n^2}, & n\text{ is odd} \\ \frac 1 {n \ln n}, & n\text{ is even} \end{cases} \\
\\
& \text{Consider the odd sequence.} \\
& \phantom = \lim_{n \to +\infty} (2n + 1) a_{2n + 1} \\
& = \lim_{n \to +\infty} \frac {2n + 1} {(2n + 1)^2} \\
& = \lim_{n \to +\infty} \frac 1 {2n + 1} \\
& = 0 \\
& \text{Consider the even sequence.} \\
& \phantom = \lim_{n \to +\infty} 2n a_{2n} \\
& = \lim_{n \to +\infty} \frac {2n} {2n \ln {2n} } \\
& = \lim_{n \to +\infty} \frac 1 {\ln {2n} } \\
& = 0 \\
& \text{So the combined sequence satisfies }\lim_{n \to +\infty} n a_n = 0\text{.} \\
& \text{Also, the sequence obviously satisfies }a_n > 0\text{ for }n \gg 0\text{.} \\
\\
& \text{Consider the partial sums up to }2N\text{.} \\
& \phantom = \sum_{n = 1}^{2N} (-1)^n a_n \\
& = \sum_{n = 1}^N \left( (-1)^{2n - 1} a_{2n - 1} + (-1)^{2n} a_{2n} \right) \\
& = \sum_{n = 1}^N \left( -\frac 1 {4n^2} + \frac 1 {2n \ln 2n} \right) && \cdots (1) \\
\\
& \text{Evaluate the negative part.} \\
& \phantom = \sum_{n = 1}^N \left(-\frac 1 {4n^2}\right) \\
& = L \in \mathbb{R}\text{ as }N \to +\infty && \text{by }p\text{-test} \\
\\
& \text{Evaluate the positive part.} \\
& \phantom = \sum_{n = 1}^N \frac 1 {2n \ln 2n} \\
& = \frac 1 2 \sum_{n = 1}^N \frac 1 {n \ln 2n} \\
& \ge \frac 1 2 \sum_{n = 0}^{\lfloor \log_2(N + 1) \rfloor - 1} \frac {2^n} {2^n \ln 2^{n + 1} } && \text{the same trick to prove the divergence of the harmonic series} \\
& = \frac 1 2 \sum_{n = 0}^{\lfloor \log_2(N + 1) \rfloor - 1} \frac 1 {\ln 2^{n + 1} } \\
& = \frac 1 {2 \ln 2} \sum_{n = 0}^{\lfloor \log_2(N + 1) \rfloor - 1} \frac 1 {n + 1} \\
& = +\infty\text{ as }N \to +\infty \\
\\
& \text{Therefore }(1)\text{ diverges by the algebraic limit theorem,} \\
& \text{as it is the sum of a convergent and divergent series.} \\
\\
& \text{Thus, the statement is disproved.}
\end{aligned}$$
