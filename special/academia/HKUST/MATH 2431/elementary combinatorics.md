---
aliases:
  - combinatorics
  - counting
  - elementary combinatorics
tags:
  - flashcard/active/special/academia/HKUST/MATH_2431/elementary_combinatorics
  - language/in/English
---

# elementary combinatorics

When all finitely many outcomes of a random experiment are equally likely, the probability of an event $A$ is $P[A] = |A|/|\Omega|$. Thus we need effective methods to count outcomes in $\Omega$ and in events $A \subseteq \Omega$. Elementary combinatorics provides these counting rules.

## cartesian product and product rule

If $N$ experiments with finite sample spaces $\Omega_1, \ldots, \Omega_N$ are performed successively, the natural sample space for the combined experiment is the Cartesian product $\Omega = \Omega_1 \times \cdots \times \Omega_N = \{(\omega_1, \ldots, \omega_N) : \omega_j \in \Omega_j,\ 1 \le j \le N\}$. The cardinality is $|\Omega| = \prod_{j=1}^N |\Omega_j| = |\Omega_1| \cdots |\Omega_N|$.

---

Flashcards for this section are as follows:

- elementary combinatorics / combined experiment space ::@:: Cartesian product $\Omega = \Omega_1 \times \cdots \times \Omega_N$; outcomes are $N$-tuples $(\omega_1, \ldots, \omega_N)$ with $\omega_j \in \Omega_j$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- elementary combinatorics / product rule ::@:: $|\Omega_1 \times \cdots \times \Omega_N| = |\Omega_1| \cdots |\Omega_N|$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- elementary combinatorics / password: Four symbols: first two letters (26 each), last two digits (10 each). How many passwords? ::@:: $\Omega = \Omega_1 \times \Omega_2 \times \Omega_3 \times \Omega_4$ with $|\Omega_1|=|\Omega_2|=26$, $|\Omega_3|=|\Omega_4|=10$; $|\Omega| = 26 \cdot 26 \cdot 10 \cdot 10 = 67600$. <!-- check: ignore-line[two_sided_calc_warning]: left has givens 26, 10 -->

## samples of size r from n elements

Consider choosing a sample of size $r \in \mathbb{N}$ from $\{1, 2, \ldots, n\}$. Four cases arise: ordered or unordered, and with or without repetition. We assume $r \le n$ when repetitions are not allowed. Let $k! = k(k-1)\cdots 1$ for $k \in \mathbb{N}$ with $0! = 1$, and $\binom{n}{k} = n!/(k!(n-k)!)$ for $0 \le k \le n$. This binomial coefficient is the special case of the multinomial coefficient with two groups, $\binom{n}{k} = \binom{n}{k,n-k}$. Then:

|           | with repetitions   | without repetitions |
| --------- | ------------------ | ------------------- |
| ordered   | $n^r$              | $n!/(n-r)!$         |
| unordered | $\binom{n+r-1}{r}$ | $\binom{n}{r}$      |

Ordered with repetition: each of $r$ positions independently chosen from $n$ options, so $n^r$. Ordered without repetition: $n(n-1)\cdots(n-r+1) = n!/(n-r)!$. Unordered without repetition: each $r$-element subset corresponds to $r!$ orderings, so $\binom{n}{r} = n!/(r!(n-r)!)$. Unordered with repetition: count non-decreasing $r$-tuples in $\{1,\ldots,n\}$ via stars-and-bars: choose $r$ positions (dots) among $n+r-1$ symbols (dots and $n-1$ bars), giving $\binom{n+r-1}{r}$.

---

Flashcards for this section are as follows:

- elementary combinatorics / ordered with repetition ::@:: Number of ordered $r$-tuples from $\{1,\ldots,n\}$ with repetition: $n^r$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- elementary combinatorics / ordered without repetition ::@:: Number of ordered $r$-tuples from $\{1,\ldots,n\}$ with distinct entries: $n(n-1)\cdots(n-r+1) = n!/(n-r)!$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- elementary combinatorics / unordered without repetition ::@:: Number of $r$-element subsets of $\{1,\ldots,n\}$: $\binom{n}{r} = n!/(r!(n-r)!)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- elementary combinatorics / unordered with repetition ::@:: Number of multisets of size $r$ from $\{1,\ldots,n\}$ (non-decreasing $r$-tuples): $\binom{n+r-1}{r}$ (stars-and-bars). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- elementary combinatorics / binomial coefficient ::@:: $\binom{n}{k} = n!/(k!(n-k)!)$ for $0 \le k \le n$; number of $k$-element subsets of an $n$-element set. Equivalently, it is the multinomial coefficient with two groups, written as $\binom{n}{k,n-k}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- elementary combinatorics / committee: Subcommittee of 5 from 12: 1 from A (3), 2 from B (4), 2 from C (5). How many? ::@:: $\binom{3}{1} \binom{4}{2} \binom{5}{2} = 3 \cdot 6 \cdot 10 = 180$. <!-- check: ignore-line[two_sided_calc_warning]: left has group sizes 3,4,5 -->

## multinomial coefficient and division into groups

Suppose $n \in \mathbb{N}$ items are to be divided into $k$ distinct groups of sizes $n_1, \ldots, n_k \in \mathbb{N}$ with $n_1 + \cdots + n_k = n$. Choose the first group: $\binom{n}{n_1}$; then the second from the remaining: $\binom{n-n_1}{n_2}$; and so on. The total number is $\binom{n}{n_1} \binom{n-n_1}{n_2} \cdots = n!/(n_1! n_2! \cdots n_k!)$. This is the _multinomial coefficient_ $\binom{n}{n_1, n_2, \ldots, n_k} = n!/(n_1! \cdots n_k!)$ for $n_j \in \mathbb{N}_0$ with $\sum n_j = n$. For $k=2$ this reduces to the binomial coefficient $\binom{n}{k} = \binom{n}{k,n-k}$. Example: assign 10 employees to tasks A (5), B (3), C (2): $10!/(5!\,3!\,2!) = 2520$, which is also the number of permutations of the "word" AAAAABBBCC.

---

Flashcards for this section are as follows:

- elementary combinatorics / division into k groups ::@:: Number of ways to partition $n$ items into $k$ labeled groups of sizes $n_1, \ldots, n_k$: $n!/(n_1! \cdots n_k!)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- elementary combinatorics / multinomial coefficient ::@:: $\binom{n}{n_1, \ldots, n_k} = n!/(n_1! \cdots n_k!)$ with $n_1 + \cdots + n_k = n$; generalizes $\binom{n}{k}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- elementary combinatorics / employees to tasks: 10 employees, 5 for A, 3 for B, 2 for C. How many assignments? ::@:: $10!/(5!\,3!\,2!) = 2520$ (same as permutations of AAAAABBBCC). <!-- check: ignore-line[two_sided_calc_warning]: left has 10, 5, 3, 2 -->

## multinomial and binomial theorems

For $x_1, \ldots, x_k \in \mathbb{R}$ and $n \in \mathbb{N}$, $(x_1 + \cdots + x_k)^n = \sum \binom{n}{n_1, \ldots, n_k} x_1^{n_1} \cdots x_k^{n_k}$, where the sum is over $(n_1, \ldots, n_k) \in \mathbb{N}_0^k$ with $n_1 + \cdots + n_k = n$. The binomial theorem is the case $k=2$: $(x+y)^n = \sum_{k=0}^n \binom{n}{k} x^k y^{n-k}$.

---

Flashcards for this section are as follows:

- elementary combinatorics / multinomial theorem ::@:: $(x_1 + \cdots + x_k)^n = \sum_{n_1+\cdots+n_k=n} \binom{n}{n_1,\ldots,n_k} x_1^{n_1} \cdots x_k^{n_k}$; for $k=2$ this reduces to the binomial theorem. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- elementary combinatorics / binomial theorem ::@:: $(x+y)^n = \sum_{k=0}^n \binom{n}{k} x^k y^{n-k}$ for $x, y \in \mathbb{R}$, $n \in \mathbb{N}$; special case of the multinomial theorem with two variables. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
