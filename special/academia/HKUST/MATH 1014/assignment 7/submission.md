---
aliases:
  - HKUST MATH 1014 L1 assignment 7 submission
tags:
  - date/2024/04/27/from
  - date/2024/05/02/to
  - language/in/English
---

# L1 assignment 7 submission

- HKUST MATH 1014

MATH1014 Calculus II Problem Set 7<br/>
L01 (Spring 2024)

Problem Set 7

Note: The problem sets serve as additional exercise problems for your own practice. Problem Set 7 covers materials from §8.2 – §8.4.

## Q3

Let $(a_n)$ be a sequence of positive real numbers.

### Q3.a

Show that if $\sum_{k = 1}^{+\infty} a_k$ converges, then $\sum_{k = 1}^{+\infty} \frac 1 {a_k}$ diverges.

> $$\begin{aligned}
> & \phantom{\implies} \sum_{k = 1}^{+\infty} a_k\text{ converges} \\
> & \implies \lim_{k \to +\infty} a_k = 0 && (\text{tail test}) \\
> & \implies \lim_{k \to +\infty} \frac 1 {a_k} = +\infty && (a_k > 0, \text{algebraic limit theorem}) \\
> & \implies \sum_{k = 1}^{+\infty} \frac 1 {a_k}\text{ diverges by the tail test}
> \end{aligned}$$

### Q3.b

Show that if $\lim_{n \to +\infty} na_n = L > 0$, then $\sum_{k = 1}^{+\infty} a_k$ diverges.

> $$\begin{aligned}
> & \phantom{\implies} \sum_{k = 1}^{+\infty} \frac 1 k \text{ diverges by the }p\text{-test} \\
> \\
> & \phantom{\implies} \lim_{n \to +\infty} n a_n = L > 0 \\
> & \implies \lim_{n \to +\infty} \frac{a_n} {\frac 1 n} = L > 0 \\
> & \implies \sum_{k = 1}^{+\infty} a_k\text{ diverges by the limit comparison test} && \left(a_n > 0, \frac 1 n > 0\right)
> \end{aligned}$$

### Q3.c

Show that if $\sum_{k = 1}^{+\infty} a_k$ converges, then $\sum_{k = 1}^{+\infty} a_k^2$ converges. Is the converse true?

> $$\begin{aligned}
> & \phantom{\implies} \sum_{k = 1}^{+\infty} a_k\text{ converges} \\
> & \implies \lim_{k \to +\infty} a_k = 0 \\
> & \\
> & \lim_{n \to +\infty} \frac {a_k^2} {a_k} = \lim_{n \to +\infty} a_k = 0 \\
> & \implies \sum_{k = 1}^{+\infty} a_k^2\text{ converges by the limit comparison test} && \left(a_k^2 > 0, a_k > 0\right) \\
> \\
> & \text{The converse is not true. Let }a_k = \frac 1 k\text{.} \\
> & \text{Then }\sum_{k = 1}^{+\infty} a_k^2 = \sum_{k = 1}^{+\infty} \frac 1 {k^2}\text{ converges by the }p\text{-test,} \\
> & \text{But }\sum_{k = 1}^{+\infty} a_k = \sum_{k = 1}^{+\infty} \frac 1 k \text{ diverges by the }p\text{-test.}
> \end{aligned}$$

### Q3.d

Show that if $\sum_{k = 1}^{+\infty} a_k^2$ converges, then $\sum_{k = 1}^{+\infty} \frac {a_k} k$ converges.

_Hint_: AM-GM inequality.

> $$\begin{aligned}
> & \phantom{\implies} \sum_{k = 1}^{+\infty} \frac 1 k\text{ diverges by the }p\text{-test}\text{ and }\sum_{k = 1}^{+\infty} a_k^2\text{ converges} \\
> & \implies \lim_{k \to +\infty} \frac {a_k^2} {\frac 1 k} = 0 && \left(a_k^2 > 0, \frac 1 k > 0, \text{contrapositive of the limit comparison test} \right) \\
> & \implies \lim_{k \to +\infty} \frac {a_k} {\frac 1 {\sqrt k} } = \sqrt 0 && \left(a_k^2 > 0, \frac 1 k > 0, \text{algebraic limit theorem}\right) \\
> & \implies \lim_{k \to +\infty} \frac {\frac 1 k} {\frac 1 k} \cdot \frac {a_k} {\frac 1 {\sqrt k} } = \lim_{k \to +\infty} \frac {\frac {a_k} k} {\frac 1 {k^{\frac 3 2} } } = 0 \\
> \\
> & \phantom{\implies} \sum_{k = 1}^{+\infty} \frac 1 {k^{\frac 3 2} }\text{ converges by the }p\text{-test} \\
> & \implies \sum_{k = 1}^{+\infty} \frac {a_k} k\text{ converges by the limit comparison test} && \left(\frac 1 {k^{\frac 3 2} } > 0, \frac {a_k} k > 0 \right)
> \end{aligned}$$

## Q7

For each of the following series, find all the values of $p \in \mathbb{R}$ such that the series converges.

### Q7.a

$$\sum_{k = 1}^{+\infty} k^2 \sin^p \frac 1 k$$

> $$\begin{aligned}
> & \phantom \implies \frac 1 k \in (0, 1] \\
> & \implies \sin^p \frac 1 k > 0 \\
> & \implies k^2 \sin^p \frac 1 k > 0 \\
> \\
> & \phantom \implies k > 0 \\
> & \implies k^{2 - p} > 0 \\
> \\
> & \phantom = \lim_{k \to +\infty} \frac {k^2 \sin^p \frac 1 k} {k^{2 - p} } \\
> & = \lim_{k \to +\infty} \frac {\sin^p \frac 1 k} {k^{-p} } \\
> & = \lim_{k \to +\infty} \left(\frac {\sin \frac 1 k} {\frac 1 k}\right)^p \\
> & = 1^p \\
> & = 1 \\
> \\
> & \phantom \implies \sum_{k = 1}^{+\infty} k^{2 - p}\text{ converges by the }p\text{-test iff }p \in (3, +\infty) \\
> & \phantom \implies \sum_{k = 1}^{+\infty} k^2 \sin^p \frac 1 k\text{ converges by the limit comparison test iff }p \in (3, +\infty) && \left(k^{2 - p} > 0, \frac 1 k \in (0, 1] \implies k^2 \sin^p \frac 1 k > 0 \right)
> \end{aligned}$$

### Q7.b

$$\sum_{k = 2}^{+\infty} \frac 1 {(\ln \ln k)^{p \ln k}@}$$

> $$\begin{aligned}
> & \phantom = \sum_{k = 2}^{+\infty} \frac 1 {(\ln \ln k)^{p \ln k} } && \cdots (1) \\
> \\
> & \phantom = \int_2^{+\infty} \! \frac 1 {(\ln \ln k)^{p \ln k} } \,\mathrm{d}k && \cdots (2) \\
> & = \int_{\ln 2}^{+\infty} \! \frac {e^k} {(\ln k)^{p k} } \,\mathrm{d}k && \cdots (3) \quad (\text{change of variable: }\ln k \mapsto k) \\
> \\
> & \phantom = \sum_{k = 1}^{+\infty} \frac {e^k} {(\ln k)^{pk} } && \cdots (4) \\
> & = \sum_{k = 1}^{+\infty} \left(\frac e {(\ln k)^p} \right)^k && \cdots (5) \\
> \\
> & \phantom = \lim_{k \to +\infty} \sqrt[k]{\left\lvert \left(\frac e {(\ln k)^p} \right)^k \right\rvert} && \cdots (6) \\
> & = \lim_{k \to +\infty} \sqrt[k]{\left(\frac e {(\ln k)^p} \right)^k} && \left(k > 1 \implies \frac e {\ln k} > 0 \right) \\
> & = \lim_{k \to +\infty} \frac e {(\ln k)^p} \\
> & = \begin{cases} 0, & p > 0 \\ e, & p = 0 \\ +\infty, & p < 0 \end{cases} \\
> \\
> & \phantom \implies (6) < 1\text{ iff }p \in (0, +\infty) \\
> & \implies (5)\text{ is convergent iff }p \in (0, +\infty)\text{ by the root test} \\
> & \implies (4)\text{ is convergent iff }p \in (0, +\infty) \\
> & \implies (3)\text{ is convergent iff }p \in (0, +\infty)\text{ by the integral test} \\
> & \implies (2)\text{ is convergent iff }p \in (0, +\infty) \\
> & \implies (1)\text{ is convergent iff }p \in (0, +\infty)\text{ by the integral test}
> \end{aligned}$$

### Q7.c

$$\sum_{k = 3}^{+\infty} \frac 1 {k (\ln k)(\ln \ln k)^p}$$

> $$\begin{aligned}
> & \phantom = \sum_{k = 3}^{+\infty} \frac 1 {k (\ln k) (\ln \ln k)^p} && \cdots (1) \\
> \\
> & \phantom = \int_3^{+\infty} \frac 1 {k (\ln k) (\ln \ln k)^p} \,\mathrm{d}k && \cdots (2) \\
> & = \int_{\ln 3}^{+\infty} \frac 1 {k (\ln k)^p} \,\mathrm{d}k && (\text{change of variable: }\ln k \mapsto k) \\
> & = \int_{\ln \ln 3}^{+\infty} \frac 1 {k^p} \,\mathrm{d}k && \cdots (3) \quad (\text{change of variable: }\ln k \mapsto k) \\
> \\
> & \phantom \implies (3)\text{ is convergent iff }p \in (1, +\infty)\text{ by the }p\text{-test} \\
> & \implies (2)\text{ is convergent iff }p \in (1, +\infty) \\
> & \implies (1)\text{ is convergent iff }p \in (1, +\infty)\text{ by the integral test}
> \end{aligned}$$

## Q8

Let $(a_n)$ be a sequence of real numbers, and define $$a_n^+ := \max\{a_n, 0\} \qquad \text{and} \qquad a_n^- := \max\{-a_n, 0\}$$ for every $n$. Show that

### Q8.a

If $\sum_{k = 1}^{+\infty} a_k$ __converges absolutely__, then both $\sum_{k = 1}^{+\infty} a_k^+$ and $\sum_{k = 1}^{+\infty} a_k^-$ converge.

> $$\begin{aligned}
> & \phantom \implies \sum_{k = 1}^{+\infty} a_k\text{ converges absolutely} \\
> & \implies \sum_{k = 1}^{+\infty} \lvert a_k \rvert\text{ converges} \\
> \\
> & \phantom \implies a_n \ge 0 \\
> & \implies a_n^+ = a_n = \lvert a_n \rvert \\
> & \phantom \implies a_n < 0 \\
> & \implies a_n^+ = 0 < \lvert a_n \rvert \\
> \\
> & \phantom \implies a_n^+ \le \lvert a_n \rvert \\
> & \implies \sum_{k = 1}^{+\infty} a_n^+\text{ converges by the direct comparison test} && \left(a_n^+ \ge 0, \lvert a_n \rvert \ge 0 \right) \\
> \\
> & \phantom \implies a_n \le 0 \\
> & \implies a_n^- = -a_n = \lvert a_n \rvert \\
> & \phantom \implies a_n > 0 \\
> & \implies a_n^- = 0 < \lvert a_n \rvert \\
> \\
> & \phantom \implies a_n^- \le \lvert a_n \rvert \\
> & \implies \sum_{k = 1}^{+\infty} a_n^-\text{ converges by the direct comparison test} && \left(a_n^- \ge 0, \lvert a_n \rvert \ge 0 \right)
> \end{aligned}$$

### Q8.b

If $\sum_{k = 1}^{+\infty} a_k$ __converges conditionally__, then both $\sum_{k = 1}^{+\infty} a_k^+$ and $\sum_{k = 1}^{+\infty} a_k^-$ diverge.

> $$\begin{aligned}
> & \phantom \implies \sum_{k = 1}^{+\infty} a_k\text{ converges conditionally} \\
> & \implies \sum_{k = 1}^{+\infty} \lvert a_k \rvert\text{ diverges} \\
> \\
> & \phantom \implies a_n \ge 0 \\
> & \implies a_n^+ = a_n \\
> & \phantom \implies a_n < 0 \\
> & \implies a_n^- = -a_n \implies a_n = -a_n^- \\
> & \therefore (a_n)\text{ can be rewritten as a sequence in terms of }a_n^+\text{ and }-a_n^-\text{ only.} \\
> & \phantom \therefore (\lvert a_n \rvert)\text{ can be rewritten as a sequence in terms of }a_n^+\text{ and }a_n^-\text{ only.} \\
> \\
> & \phantom \implies a_k^+ \ge 0 \implies a_k^+ = \lvert a_k^+ \rvert \\
> & \phantom \implies a_k^- \ge 0 \implies a_k^- = \lvert a_k^- \rvert \\
> \\
> & \phantom \implies \text{assume both }\sum_{k = 1}^{+\infty} a_k^+ = L^+\text{ and }\sum_{k = 1}^{+\infty} a_k^- = L^-\text{ converge} \\
> & \implies \text{both }\sum_{k = 1}^{+\infty} a_k^+\text{ and }\sum_{k = 1}^{+\infty} a_k^-\text{ converge absolutely} \\
> & \implies\sum_{k = 1}^{+\infty} \lvert a_n \rvert = L^+ + L^- \text{ converges} \\
> & \phantom \implies \text{...since absolutely converging sequences can be rearranged} \\
> & \phantom \implies \text{without changing their sums.} \\
> & \phantom \implies \text{the above conclusion contradicts that }\sum_{k = 1}^{+\infty} \lvert a_k \rvert\text{ diverges} \\
> & \implies \text{both }\sum_{k = 1}^{+\infty} a_k^+\text{ and }\sum_{k = 1}^{+\infty} a_k^-\text{ cannot converge simultaneously} && \cdots (1) \\
> \\
> & \text{Without loss of generality,} \\
> & \text{assume one of the sum converges while the other diverges:} \\
> & \text{Assume }\sum_{k = 1}^{+\infty} a_k^+ = L^+\text{ converges and }\sum_{k = 1}^{+\infty} a_k^-\text{ diverges.} \\
> & \text{Then, }\sum_{k = 1}^{n \in \mathbb{Z}_{\ge 1} } a_k^+ \le L^+\text{ by the monotone convergence theorem.} \\
> & \text{Consider }\sum_{k = 1}^{n \in \mathbb{Z}_{\ge 1} } a_k = \sum_{k = 1}^n a_k^+ - \sum_{k = 1}^n a_k^-\text{.} \\
> & \begin{aligned} \sum_{k = 1}^{n \in \mathbb{Z}_{\ge 1} } a_k & = \sum_{k = 1}^n a_k^+ - \sum_{k = 1}^n a_k^-\text{.} \\
> & \le L^+ - \sum_{k = 1}^n a_k^- \end{aligned} && \cdots (2) \\
> \\
> & \phantom \implies a_k^- \ge 0\text{ and }\sum_{k = 1}^{+\infty} a_k^-\text{ diverges} \\
> & \implies \sum_{k = 1}^{+\infty} a_k^- = +\infty\text{ as the partial sums are increasing}
> \\
> & \phantom \implies \sum_{k = 1}^{+\infty} a_k^- = +\infty\text{ diverges} \\
> & \implies L^+ - \sum_{k = 1}^{+\infty} a_k^- = -\infty\text{ diverges by the algebraic limit theorem} \\
> & \implies \sum_{k = 1}^{+\infty} a_k \le -\infty\text{ diverges by (2)} \\
> & \phantom \implies \text{the above conclusion contradicts that }\sum_{k = 1}^{+\infty} a_k \text{ converges} \\
> & \implies \sum_{k = 1}^{+\infty} a_k^+\text{ cannot converge and }\sum_{k = 1}^{+\infty} a_k^-\text{ cannot diverge simultaneously} && \cdots (3) \\
> & \text{Similarly, }\sum_{k = 1}^{+\infty} a_k^-\text{ cannot converge and }\sum_{k = 1}^{+\infty} a_k^+\text{ cannot diverge simultaneously} && \cdots (4) \\
> \\
> & (1), (3), (4)\text{ combined implies that both integrals must diverge simultaneously.}
> \end{aligned}$$

## Q9

For each of the following series, determine whether it diverges, converges absolutely or converges conditionally.

### Q9.b

$$\sum_{k = 0}^{+\infty} (-1)^{k + 1} \left(\sqrt{k + 1} - \sqrt k \right)$$

> $$\begin{aligned}
> & \phantom = \sum_{k = 0}^{+\infty} (-1)^{k + 1} \left(\sqrt{k + 1} - \sqrt k \right) && \cdots (1) \\
> \\
> a_k & := \sqrt{k + 1} - \sqrt k \qquad k \ge 0 \\
> a_{k + 1} & = \sqrt{k + 2} - \sqrt{k + 1} \\
> \\
> a_k & > 0 && (\sqrt{*}\text{ is increasing}) \\
> \\
> & \phantom = \lvert a_k \rvert - \lvert a_{k + 1} \rvert \\
> & = \left\lvert \sqrt{k + 1} - \sqrt k \right\rvert - \left\lvert \sqrt{k + 2} - \sqrt{k + 1} \right\rvert \\
> & = \sqrt{k + 1} - \sqrt k + \sqrt{k + 2} - \sqrt{k + 1} \\
> & = \sqrt{k + 2} - \sqrt k \\
> & > 0 \\
> & \therefore \lvert a_k \rvert \ge \lvert a_{k + 1} \rvert && \cdots (2) \\
> \\
> & \phantom = \lim_{k \to +\infty} a_k \\
> & = \lim_{k \to +\infty} \left(\sqrt{k + 1} - \sqrt k \right) \\
> & = \lim_{k \to +\infty} \frac {(k + 1) - k} {\sqrt{k + 1} + \sqrt k } \\
> & = \lim_{k \to +\infty} \frac 1 {\sqrt{k + 1} + \sqrt k } \\
> & = 0 && \cdots (3) \\
> \\
> & (1)\text{ is an alternating series in terms of }a_k\text{.} \\
> & (1)\text{ converges by the alternating series test due to }(2), (3)\text. \\
> \\
> & \phantom = \sum_{k = 0}^{+\infty} \left\lvert (-1)^{k + 1} \left(\sqrt{k + 1} - \sqrt k \right) \right\rvert && \cdots (4) \\
> & = \sum_{k = 0}^{+\infty} \left(\sqrt {k + 1} - \sqrt k \right) && \left(\left\lvert (-1)^{k + 1} \right\rvert = 1, \sqrt{k + 1} - \sqrt k > 0 \right) \\
> & = \lim_{n \to +\infty} \sum_{k = 0}^n \left(\sqrt {k + 1} - \sqrt k \right) \\
> & = \lim_{n \to +\infty} \sqrt{n + 1} && (\text{telescope}) \\
> & = +\infty \\
> & \therefore (4)\text{ diverges} \\
> \\
> & \because (1)\text{ converges but }(4)\text{ diverges} \\
> & \therefore (1)\text{ converges conditionally}
> \end{aligned}$$

### Q9.d

$$\sum_{k = 2}^{+\infty} \frac {(-1)^k} {\sqrt k + (-1)^k}$$

> $$\begin{aligned}
> & \phantom = \sum_{k = 2}^{+\infty} \frac {(-1)^k} {\sqrt k + (-1)^k} && \cdots (1) \\
> & = \sum_{k = 2}^{+\infty} \frac {(-1)^k \left(\sqrt{k} - (-1)^k \right)} {k - 1} \\
> & = \sum_{k = 2}^{+\infty} \frac {(-1)^k \sqrt k - 1} {k - 1} \\
> & = \sum_{k = 2}^{+\infty} \left( \frac {(-1)^k \sqrt k} {k - 1} - \frac 1 {k - 1} \right) && \cdots (2) \\
> \\
> & \text{Consider the sum }\sum_{k = 2}^{+\infty} \frac {(-1)^k \sqrt k} {k - 1}\text{.} \\
> & \text{It is alternating series with }a_k = \frac {\sqrt k} {k - 1}\text{.} \\
> & \text{Also, }\frac {\mathrm{d} a_k} {\mathrm{d}k} = \frac {0.5 k^{-0.5}(k - 1) - \sqrt k} {(k - 1)^2} = \frac {-0.5 \sqrt k - 0.5k^{-0.5} } {(k - 1)^2} < 0\text{.} \\
> & \text{Thus }a_k\text{ is strictly decreasing when }k \ge 2\text{.} \\
> & \text{Furthermore,} \lim_{k \to +\infty} \frac {\sqrt k} {k - 1} = \lim_{k \to +\infty} \frac {\sqrt {\frac k {k^2} } } {1 - \frac 1 k} = 0 \text{.} \\
> & \text{By the alternating series test,} \\
> & \text{the sum being considered converges.} \\
> \\
> & \text{Consider the sum}\sum_{k = 2}^{+\infty} \frac 1 {k - 1} = \sum_{k = 1}^{+\infty} \frac 1 k\text{.} \\
> & \text{The sum diverges by the }p\text{-test.} \\
> \\
> & \text{Finally, by above and the algebraic limit theorem,} \\
> & (2)\text{ equals } \sum_{k = 2}^{+\infty} \frac {(-1)^k \sqrt k} {k - 1} - \sum_{k = 2}^{+\infty} \frac 1 {k - 1}\text{ and diverges.} \\
> & \text{Thus }(1)\text{ diverges.}
> \end{aligned}$$
>
> <!-- $$\begin{aligned}
> & \text{When }k > 2\text{, }\sqrt{k} > (-1)^k\text{, so }\sqrt k + (-1)^k > 0\text{.} \\
> & \phantom = \sum_{k = 2}^{+\infty} \left\lvert \frac {(-1)^k} {\sqrt k + (-1)^k} \right\rvert \\
> & = \sum_{k = 2}^{+\infty} \frac 1 {\sqrt k + (-1)^k} \\
> & \ge \sum_{k = 2}^{+\infty} \frac 1 {\sqrt k + 1} && \cdots (3) \\
> & \\
> & \phantom = \lim_{k \to +\infty} \frac {\frac 1 {\sqrt k} } {\frac 1 {\sqrt k + 1} } \\
> & = \lim_{k \to +\infty} \frac {\sqrt k + 1} {\sqrt k} \\
> & = 1 \\
> \\
> & \sum_{k = 2}^{+\infty} \frac 1 {\sqrt k}\text{ diverges by the }p\text{-test.} \\
> & \text{Thus, }(3)\text{ diverges by the limit comparison test.} \\
> \end{aligned}$$ -->

## Q11

Find the radius and interval of convergence for each of the following power series.

### Q11.b

$$\sum_{k = 1}^{+\infty} \frac {x^k} {2^k k^2}$$

> $$\begin{aligned}
> & \text{The center of the power series is }x = 0\text{.} \\
> & \text{The coefficient of the power series is }c_k = \frac 1 {2^k k^2}\text{.} \\
> \\
> & \phantom = \text{radius of convergence} \\
> & = \lim_{k \to +\infty} \left\lvert \frac {c_k} {c_{k + 1} } \right\rvert \\
> & = \lim_{k \to +\infty} \left\lvert \frac {2^{k + 1} (k + 1)^2} {2^k k^2} \right\rvert \\
> & = 2 \lim_{k \to +\infty} \left\lvert \frac {k^2 + 2k + 1} {k^2} \right\rvert \\
> & = 2 \lim_{k \to +\infty} \left\lvert \frac {1 + 2k^{-1} + k^{-2} } {1} \right\rvert \\
> & = 2 \\
> \\
> & \text{When }x = 2\text{,} \\
> & \phantom = \sum_{k = 1}^{+\infty} \frac {2^k} {2^k k^2} \\
> & = \sum_{k = 1}^{+\infty} \frac 1 {k^2} \\
> & \text{which converges by the }p\text{-test.} \\
> & \text{As }k \ge 1 \implies \frac 1 {k^2} > 0\text{,} \\
> & \text{The integral converges absolutely.} \\
> & \text{Then its alternating series counterpart,} \\
> & \phantom = \sum_{k = 1}^{+\infty} \frac {(-1)^k 2^k} {2^k k^2} \\
> & = \sum_{k = 1}^{+\infty} \frac {(-2)^k} {2^k k^2} \\
> & \text{also converges by the absolute convergence test,} \\
> & \text{and is the expression when }x = -2\text{.} \\
> & \text{interval of convergence} = [-2, 2]
> \end{aligned}$$

## Q14

For each of the following power series, evaluate its sum whenever it converges. What happens at the end-points of its interval of convergence?

_Hint_: In each part, apply term-wise differentiation or integration on some power series whose sum is well-known.

### Q14.b

$$\sum_{k = 2}^{+\infty} \frac 1 {k (k - 1)} (x - 1)^k$$

> $$\begin{aligned}
> & \text{The center of the power series is } \\
> & x = 1\text{.} \\
> & \text{The coefficients of the power series are } \\
> & c_k = \frac 1 {k (k - 1)}\text{.} \\
> \\
> & \phantom = \text{radius of convergence} \\
> & = \lim_{k \to +\infty} \left\lvert \frac {c_k} {c_{k + 1} } \right\rvert \\
> & = \lim_{k \to +\infty} \left\lvert \frac {\frac 1 {k (k - 1)} } {\frac 1 {(k + 1) k} } \right\rvert \\
> & = \lim_{k \to +\infty} \left\lvert \frac {k + 1} {k - 1} \right\rvert \\
> & = \lim_{k \to +\infty} \frac {k + 1} {k - 1} && (k \to +\infty) \\
> & = \lim_{k \to +\infty} \frac {1 + \frac 1 k} {1 - \frac 1 k} \\
> & = 1 \\
> \\
> & \text{When }x = 2\text{,} \\
> & \phantom = \sum_{k = 2}^{+\infty} \frac 1 {k (k - 1)} (2 - 1)^k \\
> & = \sum_{k = 2}^{+\infty} \frac 1 {k (k - 1)} \\
> & = \sum_{k = 2}^{+\infty} \left(\frac 1 {k - 1} - \frac 1 k \right) \\
> & = \lim_{k \to +\infty} \left(1 - \frac 1 k \right) && (\text{telescope}) \\
> & = 1 \\
> & \text{The sum converges.} \\
> & \text{When }x = 0\text{,} \\
> & \phantom = \sum_{k = 2}^{+\infty} \frac 1 {k (k - 1)} (0 - 1)^k \\
> & = \sum_{k = 2}^{+\infty} \frac 1 {k (k - 1)} (-1)^k \\
> & = \sum_{k = 2}^{+\infty} \frac {(-1)^k} {k (k - 1)} (2 - 1)^k \\
> & \text{... which is the alternating counterpart of the series } \\
> & \text{when }x = 2\text{.} \\
> & \text{Thus, the sum converges by the absolute convergence test.} \\
> & \text{interval of convergence} = [0, 2] \\
> \\
> S(x) & := \sum_{k = 2}^{+\infty} \frac 1 {k (k - 1)} (x - 1)^k \qquad x \in [0, 2] \\
> S(2) & = 1 \\
> S'(x) & = \frac {\mathrm{d} } {\mathrm{d}x} \sum_{k = 2}^{+\infty} \frac 1 {k (k - 1)} (x - 1)^k \qquad x \in (0, 2) \\
> & = \sum_{k = 2}^{+\infty} \frac {\mathrm{d} } {\mathrm{d}x} \frac 1 {k (k - 1)} (x - 1)^k && (\text{power series can be differentiated term-wise}) \\
> & = \sum_{k = 2}^{+\infty} \frac 1 {k - 1} (x - 1)^{k - 1} \\
> S'(1) & = \sum_{k = 2}^{+\infty} \frac 1 {k - 1} (1 - 1)^{k - 1} \\
> & = \sum_{k = 2}^{+\infty} 0 && (k - 1 > 0) \\
> & = 0 \\
> S''(x) & = \frac {\mathrm{d}^2 } {\mathrm{d}x^2} \sum_{k = 2}^{+\infty} \frac 1 {k (k - 1)} (x - 1)^k \qquad x \in (0, 2) \\
> & = \sum_{k = 2}^{+\infty} \frac {\mathrm{d}^2 } {\mathrm{d}x^2} \frac 1 {k (k - 1)} (x - 1)^k && (\text{power series can be differentiated term-wise}) \\
> & = \sum_{k = 2}^{+\infty} (x - 1)^{k - 2} \\
> & = \lim_{k \to +\infty} \frac {(x - 1)^{k - 1} - (x - 1)^0} {(x - 1) - 1} \\
> & = \lim_{k \to +\infty} \frac {(x - 1)^{k - 1} - 1} {x - 2} \\
> & = \frac {-1} {x - 2} && (x \in (0, 2) \implies \lvert x - 1\rvert < 1) \\
> & = \frac 1 {2 - x} \\
> S'(x) & = \int \! S''(x) \,\mathrm{d}x \\
> & = \int \! \frac 1 {2 - x} \,\mathrm{d}x \\
> & = -\ln \lvert 2 - x \rvert + C \\
> S'(1) & = -\ln \lvert 2 - 1 \rvert + C \\
> 0 & = C \\
> C & = 0 \\
> S'(x) & = -\ln \lvert 2 - x \rvert \qquad x \in (0, 2) \\
> S(x) & = \int \! S'(x) \,\mathrm{d}x \\
> & = - \int \! \ln \lvert 2 - x \rvert \,\mathrm{d}x \\
> & = \int \! \ln \lvert u \rvert \,\mathrm{d}u && (u := 2 - x) \\
> & = u \ln \lvert u \rvert - \int \! \frac u u \,\mathrm{d}u \\
> & = u \ln \lvert u \rvert - u + C \\
> & = (2 - x) \ln \lvert 2 - x \rvert - 2 + x + C \\
> \\
> & \phantom = \lim_{x \to 2^-} (2 - x) \ln \lvert 2 - x \rvert \\
> & = \lim_{x \to 2^-} \frac {\ln \lvert 2 - x \rvert} {\frac 1 {2 - x} } \\
> & = \lim_{x \to 2^-} \frac {-\frac 1 {2 - x} } {\frac 1 {(2 - x)^2} } && (\text{L'Hopital rule}) \\
> & = \lim_{x \to 2^-} (x - 2) \\
> & = 0 \\
> \\
> S(2) & = \lim_{x \to 2^-} ((2 - x) \ln \lvert 2 - x \rvert - 2 + x + C ) && (\text{make }S(x)\text{ continuous}) \\
> 1 & = C && (\text{algebraic limit theorem}) \\
> C & = 1 \\
> S(x) & = \begin{cases}(2 - x) \ln \lvert 2 - x \rvert + x - 1, & x \in [0, 2) \\
> 1, & x = 2 \end{cases} \\
> & = \begin{cases}(2 - x) \ln(2 - x) + x - 1, & x \in [0, 2) \\
> 1, & x = 2 \end{cases} && (2 - x > 0) \\
> & \text{The sum converges on the endpoints of } \\
> & \text{the interval of convergence.}
> \end{aligned}$$

### Q14.e

$$\sum_{k = 1}^{+\infty} \frac k {k + 1} x^k$$

> $$\begin{aligned}
> & \text{The center of the power series is } \\
> & x = 0\text{.} \\
> & \text{The coefficients of the power series are } \\
> & c_k = \frac k {k + 1}\text{.} \\
> \\
> & \phantom = \text{radius of convergence} \\
> & = \lim_{k \to +\infty} \left\lvert \frac {c_k} {c_{k + 1} } \right\rvert \\
> & = \lim_{k \to +\infty} \left\lvert \frac {\frac k {k + 1} } {\frac {k + 1} {k + 2} } \right\rvert \\
> & = \lim_{k \to +\infty} \left\lvert \frac {k (k + 2)} {(k + 1)^2} \right\rvert \\
> & = \lim_{k \to +\infty} \left\lvert \frac {(k + 1)^2 - 1} {(k + 1)^2} \right\rvert \\
> & = \lim_{k \to +\infty} \left\lvert 1 - \frac 1 {(k + 1)^2} \right\rvert \\
> & = 1 \\
> \\
> & \text{When }x = -1\text{,} \\
> & \sum_{k = 1}^{+\infty} \frac k {k + 1} (-1)^k \\
> & \text{Consider }a_k = \frac k {k + 1} (-1)^k\text{.} \\
> & \text{Consider the subsequence given by }b_k = a_{2k} = \frac {2k} {2k + 1} (-1)^{2k}\text{.} \\
> & \lim_{k \to +\infty} \frac {2k} {2k + 1} (-1)^{2k} = \lim_{k \to +\infty} \frac 2 {2 + \frac 1 k} = 1 \\
> & \text{Consider the subsequence given by }c_k = a_{2k - 1} = \frac {2k - 1} {2k} (-1)^{2k - 1}\text{.} \\
> & \lim_{k \to +\infty} \frac {2k - 1} {2k} (-1)^{2k - 1} = \lim_{k \to +\infty} \left( -\frac {2 - \frac 1 k} 2 \right) = -1 \\
> & \text{As the two subsequences of }(a_k)_{k \in \mathbb{N} }\text{ approaches different values } \\
> & \text{as }k \to +\infty\text{,} \\
> & \lim_{k \to +\infty} \frac k {k + 1} (-1)^k\text{ does not exist.} \\
> & \text{Thus, }\sum_{k = 1}^{+\infty} \frac k {k + 1} (-1)^k\text{ diverges by the tail test.} \\
> & \text{When }x = 1\text{,} \\
> & \phantom = \sum_{k = 1}^{+\infty} \frac k {k + 1} 1^k \\
> & \phantom = \lim_{k \to +\infty} \frac k {k + 1} 1^k \\
> & = \lim_{k \to +\infty} \frac 1 {1 + \frac 1 k} \\
> & = 1 \\
> & \text{Thus, }\sum_{k = 1}^{+\infty} \frac k {k + 1} 1^k\text{ diverges by the tail test.} \\
> & \text{interval of convergence} = (-1, 1) \\
> \\
> & \phantom = \sum_{k = 1}^{+\infty} x^k \qquad x \in (-1, 1) \\
> & = \lim_{k \to +\infty} \frac {x^{k + 1} - x} {x - 1} \\
> & = \frac x {1 - x} && (\lvert x \rvert < 1) \\
> \\
> S(x) & := \sum_{k = 1}^{+\infty} \frac k {k + 1} x^k \qquad x \in (-1, 1) \\
> S(0) & = \sum_{k = 1}^{+\infty} \frac k {k + 1} 0^k \\
> & = \sum_{k = 1}^{+\infty} 0 \\
> & = 0 \\
> S(x) & = \sum_{k = 1}^{+\infty} \frac k {k + 1} x^k \\
> & = \sum_{k = 1}^{+\infty} \left(1 - \frac 1 {k + 1}\right) x^k \\
> & = \sum_{k = 1}^{+\infty} x^k + \sum_{k = 1}^{+\infty} \left(1 - \frac 1 {k + 1}\right) x^k - \sum_{k = 1}^{+\infty} x^k \\
> & = \sum_{k = 1}^{+\infty} x^k - \sum_{k = 1}^{+\infty} \frac 1 {k + 1} x^k && (\text{algebraic limit theorem}) \\
> & = \frac x {1 - x} - \sum_{k = 1}^{+\infty} \frac 1 {k + 1} x^k \\
> \end{aligned}$$
>
> Not using differential equations:
>
> $$\begin{aligned}
> T(x) & := \sum_{k = 1}^{+\infty} \frac 1 {k + 1} x^k \qquad x \in (-1, 1) \\
> & = \begin{cases} \frac 1 x \sum_{k = 1}^{+\infty} \frac 1 {k + 1} x^{k + 1}, & x \in (-1, 0) \cup (0, 1) \\
> 0, & x = 0 \end{cases} \\
> \\
> U(x) & := \sum_{k = 1}^{+\infty} \frac 1 {k + 1} x^{k + 1} \qquad x \in (-1, 1) \\
> U'(x) & = \frac {\mathrm{d} } {\mathrm{d}x} \sum_{k = 1}^{+\infty} \frac 1 {k + 1} x^{k + 1} \\
> & = \sum_{k = 1}^{+\infty} \frac {\mathrm{d} } {\mathrm{d}x} \frac 1 {k + 1} x^{k + 1} && (\text{power series can be differentiated term-wise}) \\
> & = \sum_{k = 1}^{+\infty} x^k \\
> & = \frac x {1 - x} \\
> U(0) & = \sum_{k = 1}^{+\infty} \frac 1 {k + 1} 0^{k + 1} \\
> & = \sum_{k = 1}^{+\infty} 0 && (k + 1 > 0) \\
> & = 0 \\
> U(x) & = \int \! U'(x) \,\mathrm{d}x \\
> & = \int \! \frac x {1 - x} \,\mathrm{d}x \\
> & = \int \! \frac {u - 1} u \,\mathrm{d}u \qquad u := 1 - x \\
> & = u - \ln \lvert u \rvert + C \\
> & = 1 - x - \ln \lvert 1 - x \rvert + C \\
> & = -x - \ln \lvert 1 - x \rvert + C && (C\text{ is arbitrary}) \\
> U(0) & = -0 - \ln \lvert 1 - 0 \rvert + C \\
> C & = 0 \\
> U(x) & = -x - \ln \lvert 1 - x\rvert \qquad x \in (-1, 1) \\
> \\
> T(x) & = \begin{cases} \frac 1 x \sum_{k = 1}^{+\infty} \frac 1 {k + 1} x^{k + 1}, & x \in (-1, 0) \cup (0, 1) \\
> 0, & x = 0 \end{cases} \\
> & = \begin{cases} \frac 1 x U(x), & x \in (-1, 0) \cup (0, 1) \\
> 0, & x = 0 \end{cases} \\
> & = \begin{cases} - 1 - \frac {\ln \lvert 1 - x \rvert} x, & x \in (-1, 0) \cup (0, 1) \\
> 0, & x = 0 \end{cases} \\
> \\
> S(x) & = \frac x {1 - x} - \sum_{k = 1}^{+\infty} \frac 1 {k + 1} x^k \\
> & = \frac x {1 - x} - T(x) \\
> & = \begin{cases} \frac x {1 - x} + 1 + \frac {\ln \lvert 1 - x \rvert} x, & x \in (-1, 0) \cup (0, 1) \\
> \frac 0 {1 - 0}, & x = 0 \end{cases} \\
> & = \begin{cases} \frac {x + 1 - x} {1 - x} + \frac {\ln \lvert 1 - x \rvert} x, & x \in (-1, 0) \cup (0, 1) \\
> 0, & x = 0 \end{cases} \\
> & = \begin{cases} \frac 1 {1 - x} + \frac {\ln \lvert 1 - x \rvert} x, & x \in (-1, 0) \cup (0, 1) \\
> 0, & x = 0 \end{cases} \\
> & \text{The sum diverges on the endpoints of } \\
> & \text{the interval of convergence.}
> \end{aligned}$$
>
> Alternatively, using differential equations:
>
> $$\begin{aligned}
> S'(x) & = \frac {\mathrm{d} } {\mathrm{d}x} \left(\frac x {1 - x} - \sum_{k = 1}^{+\infty} \frac 1 {k + 1} x^k \right) \\
> & = \frac {(1 - x) + x} {(1 - x)^2} - \sum_{k = 1}^{+\infty} \frac {\mathrm{d} } {\mathrm{d}x} \frac 1 {k + 1} x^k && (\text{power series can be differentiated term-wise}) \\
> & = \begin{cases} \frac 1 {(1 - x)^2} - \sum_{k = 1}^{+\infty} \frac k {k + 1} x^{k - 1}, & x \in (-1, 0) \cup (0, 1) \\
> 1 - \frac 1 2, & x = 0 \end{cases} \\
> & = \begin{cases} \frac 1 {(1 - x)^2} - \frac 1 x \sum_{k = 1}^{+\infty} \frac k {k + 1} x^k, & x \in (-1, 0) \cup (0, 1) \\
> \frac 1 2, & x = 0 \end{cases} \\
> & = \begin{cases} \frac 1 {(1 - x)^2} - \frac {S(x)} x, & x \in (-1, 0) \cup (0, 1) \\
> \frac 1 2, & x = 0 \end{cases} \\
> \\
> y & := S(x) \qquad x \in (-1, 0) \cup (0, 1) \\
> y' & = \frac 1 {(1 - x)^2} - \frac y x \\
> & \text{The above is a linear ordinary differential equation.} \\
> & \text{An unique solution exists on each of }(-1, 0)\text{ and }(0, 1)\text{.} \\
> \\
> & \text{Solve the homogeneous equation.} \\
> y' & = -\frac y x \qquad x \in (-1, 0) \cup (0, 1) \\
> \frac {\mathrm{d}y} {\mathrm{d}x} & = - \frac y x \\
> \frac 1 y \,\mathrm{d}y & =  - \frac 1 x \,\mathrm{d}x \\
> \int \! \frac 1 y \,\mathrm{d}y & = -\int \! \frac 1 x \,\mathrm{d}x \\
> \ln \lvert y \rvert & = -\ln \lvert x \rvert + C \\
> e^{\ln \lvert y \rvert} & = e^{-\ln \lvert x \rvert + C} \\
> \lvert y \rvert & = \frac {e^C} {\lvert x \rvert} \\
> y & = \pm \frac {e^C} {\lvert x \rvert} \\
> y & = \frac {c_1} x \qquad c_1 \in \mathbb{R}_{\ne 0} \\
> & \text{When }c_1 = 0\text{,} \\
> y & = \frac 0 x \qquad x \in (-1, 0) \cup (0, 1) \\
> y & = 0 \\
> y' & = 0 \\
> & \text{... which satisfies the homogeneous equation.} \\
> y & = \frac {c_1} x \qquad c_1 \in \mathbb{R} \\
> & \text{Different }c_1\text{ can be chosen on each of }(-1, 0)\text{ and }(0, 1)\text{.} \\
> \\
> & \text{Solve the inhomogeneous equation.} \\
> y & = \frac 1 x \int \! \frac {\det \begin{bmatrix} \frac 1 {(1 - x)^2} \end{bmatrix} } {\det \begin{bmatrix} \frac 1 x \end{bmatrix} } \,\mathrm{d}x \qquad x \in (-1, 0) \cup (0, 1) && (\text{variation of parameters}) \\
> & = \frac 1 x \int \frac x {(1 - x)^2} \,\mathrm{d}x \\
> & = -\frac 1 x \int \frac {-u + 1} {u^2} \,\mathrm{d}u \qquad u := 1 - x \\
> & = -\frac 1 x \left(- \ln \lvert u \rvert - \frac 1 u + c_1 \right) \qquad c_1 \in \mathbb{R} \\
> & = \frac {\ln \lvert 1 - x \rvert} x + \frac 1 {x (1 - x)} - \frac {c_1} x \\
> & \text{Different }c_1\text{ can be chosen on each of }(-1, 0)\text{ and }(0, 1)\text{,} \\
> & \text{which will be denoted }c_1^-\text{ and }c_1^+\text{ respectively below.} \\
> \\
> & \phantom = \lim_{x \to 0^+} \frac {\ln \lvert 1 - x \rvert} x \\
> & = \lim_{x \to 0^+} \frac {\ln(1 - x)} x && (1 - x \ge 0) \\
> & = \lim_{x \to 0^+} \frac {-\frac 1 {1 - x} } 1 && (\text{L'Hopital rule}) \\
> & = -1 \\
> & \phantom = \lim_{x \to 0^-} \frac {\ln \lvert 1 - x \rvert} x \\
> & = \lim_{x \to 0^-} \frac {\ln(x - 1)} x && (1 - x \le 0) \\
> & = \lim_{x \to 0^-} \frac {\frac 1 {x - 1} } 1 && (\text{L'Hopital rule}) \\
> & = -1 \\
> & \lim_{x \to 0} \frac {\ln \lvert 1 - x \rvert} x = -1 \\
> \\
> S(0) & = \lim_{x \to 0^+} \left( \frac {\ln \lvert 1 - x \rvert} x + \frac 1 {x (1 - x)} - \frac {c_1^+} x \right) && (\text{make }S(x)\text{ continuous}) \\
> 0 & = -1 + \lim_{x \to 0^+} \frac {1 - c_1^+ + c_1^+ x} {x (1 - x)} && (\text{algebraic limit theorem}) \\
> 1 & = \lim_{x \to 0^+} \frac {c_1^+} {(1 - x) - x} && (\text{L'Hoptial rule}) \\
> 1 & = c_1^+ \\
> c_1^+ & = 1 \\
> S(0) & = \lim_{x \to 0^-} \left( \frac {\ln \lvert 1 - x \rvert} x + \frac 1 {x (1 - x)} - \frac {c_1^-} x \right) && (\text{make }S(x)\text{ continuous}) \\
> 0 & = -1 + \lim_{x \to 0^-} \frac {1 - c_1^- + c_1^- x} {x (1 - x)} && (\text{algebraic limit theorem}) \\
> 1 & = \lim_{x \to 0^-} \frac {c_1^-} {(1 - x) - x} && (\text{L'Hopital rule}) \\
> 1 & = c_1^- \\
> c_1^- & = 1 \\
> \\
> & \text{Therefore,} \\
> S(x) & = \begin{cases}\frac {\ln \lvert 1 - x \rvert} x + \frac 1 {x (1 - x)} - \frac 1 x, & x \in (-1, 0) \cup (0, 1) \\
> 0, & x = 0 \end{cases} \\
> & = \begin{cases}\frac {\ln \lvert 1 - x \rvert} x + \frac {1 - 1 + x} {x (1 - x)}, & x \in (-1, 0) \cup (0, 1) \\
> 0, & x = 0 \end{cases} \\
> & = \begin{cases}\frac {\ln \lvert 1 - x \rvert} x + \frac 1 {1 - x}, & x \in (-1, 0) \cup (0, 1) \\
> 0, & x = 0 \end{cases} \\
> & \text{The sum diverges on the endpoints of } \\
> & \text{the interval of convergence.}
> \end{aligned}$$
