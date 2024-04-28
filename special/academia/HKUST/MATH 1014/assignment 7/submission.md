---
aliases:
  - HKUST MATH 1014 L1 assignment 7 submission
tags:
  - date/2024/04/27/from
  - language/in/English
---

# HKUST MATH 1014 L1 assignment 7 submission

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
> & \implies \lim_{k \to +\infty} a_k = 0 \\
> & \implies \lim_{k \to +\infty} \frac 1 {a_k} = +\infty && (a_k > 0, \text{algebraic limit theorem}) \\
> & \implies \sum_{k = 1}^{+\infty} \frac 1 {a_k}\text{ diverges}
> \end{aligned}$$

### Q3.b

Show that if $\lim_{n \to +\infty} na_n = L > 0$, then $\sum_{k = 1}^{+\infty} a_k$ diverges.

> $$\begin{aligned}
> & \phantom{\implies} \sum_{k = 1}^{+\infty} \frac 1 k \text{ diverges by the }p\text{-test} \\
> \\
> & \phantom{\implies} \lim_{n \to +\infty} n a_n = L > 0 \\
> & \implies \lim_{n \to +\infty} \frac{a_n} {\frac 1 n} = L > 0 \\
> & \implies \sum_{k = 1}^{+\infty} a_k\text{ diverges by the limit comparison test} && (a_k > 0)
> \end{aligned}$$

### Q3.c

Show that if $\sum_{k = 1}^{+\infty} a_k$ converges, then $\sum_{k = 1}^{+\infty} a_k^2$ converges. Is the converse true?

> $$\begin{aligned}
> & \phantom{\implies} \sum_{k = 1}^{+\infty} a_k\text{ converges} \\
> & \implies \lim_{k \to +\infty} a_k = 0 \\
> & \\
> & \lim_{n \to +\infty} \frac {a_k^2} {a_k} = \lim_{n \to +\infty} a_k = 0 \\
> & \implies \sum_{k = 1}^{+\infty} a_k^2\text{ converges by the limit comparison test} && (a_k > 0) \\
> \\
> & \text{The converse is not true. Let }a_k = \frac 1 k\text{.} \\
> & \text{Then }\sum_{k = 1}^{+\infty} a_k^2\text{ converges by the }p\text{-test,} \\
> & \text{But }\sum_{k = 1}^{+\infty} a_k\text{ diverges by the }p\text{-test.}
> \end{aligned}$$

### Q3.d

Show that if $\sum_{k = 1}^{+\infty} a_k^2$ converges, then $\sum_{k = 1}^{+\infty} \frac {a_k} k$ converges.

_Hint_: AM-GM inequality.

> $$\begin{aligned}
> & \phantom{\implies} \sum_{k = 1}^{+\infty} \frac 1 k\text{ diverges by the }p\text{-test}\text{ and }\sum_{k = 1}^{+\infty} a_k^2\text{ converges} \\
> & \implies \lim_{k \to +\infty} \frac {a_k^2} {\frac 1 k} = 0 && \left(a_k^2 > 0, k > 0, \text{contrapositive of the limit comparison test} \right) \\
> & \implies \lim_{k \to +\infty} \frac {a_k} {\frac 1 {\sqrt k} } = 0 && (a_k > 0, k > 0, \text{algebraic limit theorem}) \\
> & \implies \lim_{k \to +\infty} \frac {\frac 1 k} {\frac 1 k} \cdot \frac {a_k} {\frac 1 {\sqrt k} } = \lim_{k \to +\infty} \frac {\frac {a_k} k} {\frac 1 {k^{\frac 3 2} } } = 0 \\
> \\
> & \phantom{\implies} \sum_{k = 1}^{+\infty} \frac 1 {k^{\frac 3 2} }\text{ converges by the }p\text{-test} \\
> & \implies \sum_{k = 1}^{+\infty} \frac {a_k} k\text{ converges by the limit comparison test} && (a_k > 0)
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
> & \phantom \implies \sum_{k = 1}^{+\infty} k^2 \sin^p \frac 1 k\text{ converges by the limit comparison test iff }p \in (3, +\infty)
> \end{aligned}$$

### Q7.b

$$\sum_{k = 2}^{+\infty} \frac 1 {(\ln \ln k)^{p \ln k}}$$

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

### Q8.a

### Q8.b

## Q9

### Q9.b

### Q9.d

## Q11

### Q11.b

## Q14

### Q14.b

### Q14.e
