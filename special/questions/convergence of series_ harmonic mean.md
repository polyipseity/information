---
aliases:
  - 'convergence of series: harmonic mean'
tags:
  - date/2024/07/01/from
  - date/2024/07/02/to
  - flashcard/active/special/questions/convergence_of_series__harmonic_mean
  - language/in/English
  - question/mathematics/series
---

# convergence of series: harmonic mean

- datetime: 2024-07-01T23:12:08.913+08:00

Prove or disprove: If $a_n > 0$ for $n \gg 0$ and $\sum a_n$ diverges, then $\sum \frac 1 {\frac 1 {a_n} + n}$ diverges.

## strategy

- inspecting "Prove or disprove: If $a_n > 0$ for $n \gg 0$ and $\sum a_n$ diverges, then $\sum \frac 1 {\frac 1 {a_n} + n}$ diverges." :@: Guess whether it is true. Consider the growth rate of $a_n$ that makes $\sum a_n$ diverges. The lower limit of its growth rate is approximately (can be faster or slower than) $\frac 1 n$ by the $p$-test. Then the upper limit of growth rate of $\frac 1 {a_n}$ is approximately (can also be faster or slower than) $n$. $\sum \frac 1 {2n}$ obviously diverges by the $p$-test. So it seems like this statement _may_ be true... However, this does not work. <!--SR:!2026-08-03,476,272-->
- reason to not consider growth rates :@: Considering growth rates ignores that $a_n$ may not be always decreasing and can have sudden jumps for certain $n$-es, making it not well-described by growth rates. Indeed, we can construct a sequence of $a_n$ that disprove the statement. <!--SR:!2026-04-02,405,270-->
- inspecting "$\sum \frac 1 {\frac 1 {a_n} + n}$" :@: This is the harmonic mean of $a_n$ and $1 / n$, scaled by 0.5. Consider inequalities related to it. <!--SR:!2026-04-09,405,270-->

## solution

$$\begin{aligned}
& \phantom = \sum \frac 1 {\frac 1 {a_n} + n} \\
& = \frac 1 2 \sum \frac 2 {\frac 1 {a_n} + \frac 1 {\frac 1 n} } \\
& \le \frac 1 2 \sum 2 \min\set{a_n, 1 / n} && (\text{harmonic mean inequality}, \text{assuming }n \gg 0\text{ such that }a_n > 0) \\
& = \sum \min\set{a_n, 1 / n} && \cdots \text{(1)} \\
\\
a_n & := \begin{cases} 1, & \log_2 n \in \mathbb{Z} \\ \frac 1 {n^2}, & \text{otherwise} \end{cases} \\
& \text{The partial sums of the above sequence diverges obviously.} \\
& \text{It also satisfies }a_n > 0\text{ for }n \gg 0\text{.} \\
\\
& \text{Consider (1).} \\
& \phantom = \sum \min\set{a_n, 1 / n} \\
& = \sum \begin{cases} \frac 1 n , & \log_2 n \in \mathbb{Z} \\ \frac 1 {n^2}, & \text{otherwise} \end{cases} \\
& = \sum \begin{cases} \frac 1 {2^m} \quad m:= \log_2 n, & \log_2 n \in \mathbb{Z} \\ \frac 1 {n^2}, & \text{otherwise} \end{cases} \\
\\
& \text{Calculate the partial sums of each case separately.} \\
0 & \le \sum^N \frac 1 {2^m} \\
& = L_1 \in \mathbb{R}\text{ as }N \to +\infty \\
& \text{...as it is a geometric series.} \\
\\
0 & \le \sum^N \begin{cases} 0, & \log_2 n \in \mathbb{Z} \\ \frac 1 {n^2}, & \text{otherwise} \end{cases} \\
& \le \sum^N \frac 1 {n^2} \\
& = L_2 \in \mathbb{R}\text{ as }N \to +\infty \\
& \text{...by }p\text{-test.} \\
\\
& \text{Both partial sums are convergent.} \\
& \text{Therefore (1) is convergent as a sum of two convergent sums} \\
& \text{by the algebraic limit theorem.} \\
& \text{Further, the original integral is convergent} \\
& \text{by the direct comparison test.} \\
\\
& \text{Thus, the statement is disproved.}
\end{aligned}$$
