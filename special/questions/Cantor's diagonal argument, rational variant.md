---
aliases:
  - Cantor's diagonal argument, rational variant
tags:
  - date/2024/03/01
  - flashcard/active/special/questions/Cantor_s_diagonal_argument__rational_variant
  - language/in/English
  - question/mathematics/elementary_set_theory
  - status/incomplete
---

# Cantor's diagonal argument, rational variant

- credit: [Ashlee Dick](https://math.stackexchange.com/q/4833515), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), via Mathematics Stack Exchange
- datetime: 2024-03-01T12:53:25.724+08:00

Is it possible to list of all the rationals in $[0, 1]$, written in base $b \ge 2$, such that the real given by combining the digits along the diagonal is rational?

_Note that for a real with a finite representation in base $b \ge 2$, we can always pad it with infinite number of 0s to get an infinite representation. For example, $1 = 1.000\ldots$._

## strategy

- inspecting "Is it possible to list of all the rationals in $[0, 1]$, written in base $b \ge 2$, such that the real given by combining the digits along the diagonal is rational?" :@: Let $x$ be the real given by combining the digits along the diagonal. <!--SR:!2025-07-18,241,270-->
- tips when considering $x$ :@: Consider $1 - x$. $x$ is rational iff $1 - x$ is rational. Consider the digits of $1 - x$. <!--SR:!2026-08-03,564,310-->
- pitfalls when considering digits :@: Some real numbers admit multiple decimal representations. For example, $1.000\ldots = 0.999\ldots$ in base 10. This needs to be considered. In particular, this is the reason for the answer in a certain base. <!--SR:!2025-07-01,233,270-->

## solution

- credit: [Sharky Kesa](https://math.stackexchange.com/a/4833531), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), via Mathematics Stack Exchange

Let $x$ be the real given by combining the digits along the diagonal. Let $*_n$ be the $n$-th digit of $*$.

We show that $x$ cannot have an infinite trail of the same digit in all bases except base 2. Let that same digit be $d$. If $x$ is indeed such a number, then there exists a finite natural number $N$ such that all digits after the $N$-th digit are $d$. Then, the list used to construct $x$ can only have a finite number of rationals that do not have the digit $d$. Such a list is impossible, as it is always possible to construct an infinite number of rationals that do not have the digit $d$ except in base 2. It fails in base 2 because there is only one rational that do not have the digit $d$. Finally, $x$ cannot have infinite trail of the same digit in all bases except base 2.

We show that $1 - x$ differs from each rational in the list by at least one digit in even bases. Consider the digits of $1 - x$. Note that $(1 - x)_n = b - 1 - x_n$ after the decimal point. In even bases, $(1 - x)_n \ne x_n$. By considering the construction of $x$, it is clear that $1 - x$ differs from each rational in the list by at least one digit.

We show that $1 - x$ is irrational in even bases that are not base 2. Note that some rationals have two representations, one with infinite trailing 0s and the other with infinite trailing $(b - 1)$<!-- LaTeX separator -->s, such as $1 = 1.000\ldots = 0.999\ldots$ in base 10, so it is still possible for $1 - x$ to be an alternative representation of a rational in the list. But this possibility can be eliminated except in base 2, as $x$ cannot have an infinite trail of the same digit, thus $1 - x$ also cannot have an infinite trail of the same digit. Finally, $1 - x$ is not in the list of all rationals and cannot be an alternative representation of a rational in the list, so $1 - x$ is irrational in even bases that are not base 2.

The irrationality of $1 - x$ implies the irrationality of $x$. So $x$ is irrational in even bases that are not base 2. The question answer is no in even bases that are not base 2.

For base 2, we can answer the question by constructing a rational. For example, to construct $0 = 0.000\ldots$, generate the list of all rationals one by one by taking the rational that constructs $0.000\ldots$, with the smallest denominator, then the smallest numerator, that is not already in the list. This gives the following list:

$$\begin{aligned}
\frac 0 1 & = \underline{0}.0000000\ldots_2 \\
\frac 1 1 & = 1.\underline{0}000000\ldots_2 \\
\frac 1 2 & = 0.1\underline{0}00000\ldots_2 \\
\frac 1 3 & = 0.01\underline{0}1010\ldots_2 \\
\frac 2 3 & = 0.101\underline{0}101\ldots_2 \\
\frac 1 4 & = 0.0100\underline{0}00\ldots_2 \\
\frac 3 4 & = 0.11000\underline{0}0\ldots_2 \\
\frac 3 5 & = 0.100110\underline{0}\ldots_2 \\
& \vdots
\end{aligned}$$

We show that every rationals eventually appear in the list. Every rational can be represented by infinitely many 0s in base 2. Consider a rational with 0 as the $N$-th digit and all 1s after the $N$-th digit. Then the rational is the same as the rational with 1 as the $N$-th digit and all 0s after the $N$-th digit, like $0.111\ldots_2 = 1.000\ldots_2$. Since every rational has infinitely many 0s and there is a finite number of rational preceding it by the rules, it must eventually appear in the list, showing the list contains all rationals. The constructed real $x$ is $0.000\ldots_2 = 0$, which is rational.

In fact, since the only reason why it fails for base 2 is because $1 - x$ admits the alternative representation of a rational in the list. This also implies $x$ must have two representations, one of them with trailing 0s, the other with trailing 1s. Thus, $x$ must have a finite binary expansion. The question answer is yes in base 2.

For odd bases, we are not sure of the answer.
