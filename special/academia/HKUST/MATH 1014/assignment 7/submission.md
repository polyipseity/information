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

### Q7.a

### Q7.b

### Q7.c

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
