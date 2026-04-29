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

- combined experiment space ::@:: Cartesian product $\Omega = \Omega_1 \times \cdots \times \Omega_N$; outcomes are $N$-tuples $(\omega_1, \ldots, \omega_N)$ with $\omega_j \in \Omega_j$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- product rule ::@:: $|\Omega_1 \times \cdots \times \Omega_N| = |\Omega_1| \cdots |\Omega_N|$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- password: Four symbols: first two letters (26 each), last two digits (10 each). How many passwords? ::@:: $\Omega = \Omega_1 \times \Omega_2 \times \Omega_3 \times \Omega_4$ with $|\Omega_1|=|\Omega_2|=26$, $|\Omega_3|=|\Omega_4|=10$; $|\Omega| = 26 \cdot 26 \cdot 10 \cdot 10 = 67600$. <!-- check: ignore-line[two_sided_calc_warning]: left has givens 26, 10 -->

## samples of size r from n elements

Consider choosing a sample of size $r \in \mathbb{N}$ from $\{1, 2, \ldots, n\}$. Four cases arise: ordered or unordered, and with or without repetition. We assume $r \le n$ when repetitions are not allowed. Let $k! = k(k-1)\cdots 1$ for $k \in \mathbb{N}$ with $0! = 1$, let $\binom{n}{k} = n!/(k!(n-k)!)$ for $0 \le k \le n$, and let the falling factorial be $n^{\underline r}:=n(n-1)\cdots(n-r+1)$ for $r\ge1$ with $n^{\underline 0}:=1$. The binomial coefficient is the special case of the multinomial coefficient with two groups, $\binom{n}{k} = \binom{n}{k,n-k}$. Then:

|           | with repetitions   | without repetitions |
| --------- | ------------------ | ------------------- |
| ordered   | $n^r$              | $n!/(n-r)!$         |
| unordered | $\binom{n+r-1}{r}$ | $\binom{n}{r}$      |

Ordered with repetition has only one standard expression: each of the $r$ positions is chosen independently from $n$ possibilities, so the answer is $n^r$.

Ordered without repetition is commonly written in three equivalent ways:

- $n(n-1)\cdots(n-r+1)$,
- $n^{\underline r}$,
- $n!/(n-r)!$.

The product or falling-factorial form is the most informative starting point because it shows the successive choice process directly. It also handles the boundary case $r=0$ cleanly through the empty-product convention $n^{\underline 0}=1$. With the standard discrete convention $n^{\underline r}=0$ for integers $r>n$, it also records the impossible case automatically.

Unordered without repetition can also be written in several equivalent ways:

- $\binom{n}{r}$,
- $\binom{n}{n-r}$,
- $\dfrac{n^{\underline r}}{r!}$,
- $\dfrac{n!}{r!(n-r)!}$.

Here the best default expression is $\binom{n}{r}$, because it makes the symmetry $\binom{n}{r}=\binom{n}{n-r}$ visible and handles the boundary cases $\binom{n}{0}=\binom{n}{n}=1$ transparently. With the usual extension $\binom{n}{r}=0$ for integers $r>n$, it also encodes the degenerate impossible case in the cleanest way.

Unordered with repetition is the stars-and-bars case. It has two standard binomial forms:

- $\binom{n+r-1}{r}$,
- $\binom{n+r-1}{n-1}$.

They are equal by binomial symmetry. The form $\binom{n+r-1}{r}$ emphasizes choosing the $r$ dot positions, so it is the most natural default when the sample size $r$ is the main parameter. The symmetric form $\binom{n+r-1}{n-1}$ emphasizes choosing the $n-1$ bar positions, which is especially convenient when the number of types $n$ is the point of view and immediately explains the one-type case $n=1$.

These four formulas are not four unrelated facts. Start from the most rigid model, ordered without repetition, whose count is the direct product-rule expression $n^{\underline r}$. If order should no longer matter, divide by $r!$ because each unordered sample was counted once for each ordering. If repetition is allowed, the product-rule picture changes: one no longer counts decreasing numbers of available choices, and in the unordered case the problem becomes a stars-and-bars encoding problem. So the pair of modelling decisions — whether order matters and whether repetition is allowed — determines the formula systematically rather than by memorizing four isolated rules.

The edge case $r=0$ is a good consistency check. In every one of the four models there is exactly one sample of size $0$, namely the empty sample, and every formula agrees with that: $n^0=1$, $n^{\underline0}=1$, $\binom{n}{0}=1$, and $\binom{n-1}{0}=1$.

For unordered with repetition, the stars-and-bars picture is worth visualizing. If, for instance, one chooses a multiset of size $5$ from $\{1,2,3\}$ and the result is $\{1,1,2,3,3\}$, then the encoding is `..|.|..`: the dots before the first bar record the two copies of $1$, the dots between the bars record the one copy of $2$, and the dots after the second bar record the two copies of $3$. The same picture can be counted in two equivalent ways: choose which $5$ of the $7$ symbol positions are dots, or choose which $2$ of the $7$ positions are bars. That is exactly why both $\binom{n+r-1}{r}$ and $\binom{n+r-1}{n-1}$ appear naturally.

---

Flashcards for this section are as follows:

- ordered with repetition ::@:: Number of ordered $r$-tuples from $\{1,\ldots,n\}$ with repetition: $n^r$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- ordered without repetition ::@:: Number of ordered $r$-tuples from $\{1,\ldots,n\}$ with distinct entries: $n(n-1)\cdots(n-r+1)=n^{\underline r}=n!/(n-r)!$. The most informative default form is the falling-factorial/product view because it shows the successive choices directly, gives $n^{\underline0}=1$, and can be extended by the convention $n^{\underline r}=0$ for integers $r>n$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- unordered without repetition ::@:: Number of $r$-element subsets of $\{1,\ldots,n\}$: $\binom{n}{r}=\binom{n}{n-r}=\dfrac{n^{\underline r}}{r!}=\dfrac{n!}{r!(n-r)!}$. The best default form is $\binom{n}{r}$ because it displays symmetry and makes the boundary cases $\binom{n}{0}=\binom{n}{n}=1$ transparent. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- unordered with repetition ::@:: Number of multisets of size $r$ from $\{1,\ldots,n\}$ (non-decreasing $r$-tuples): $\binom{n+r-1}{r}=\binom{n+r-1}{n-1}$. The default form $\binom{n+r-1}{r}$ tracks the chosen sample size, while the symmetric form makes the one-type case $n=1$ immediate. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why unordered without repetition divides by $r!$ ::@:: If one first counts ordered selections without repetition, then each unordered $r$-element sample is counted once for each of its $r!$ orderings, so dividing by $r!$ removes the overcounting.
- all four sample-counting formulas at $r=0$ ::@:: Every model gives exactly one sample of size $0$, namely the empty sample, so $n^0=1$, $n^{\underline0}=1$, $\binom{n}{0}=1$, and $\binom{n-1}{0}=1$.
- stars-and-bars encoding ::@:: A multiset of size $r$ from $\{1,\ldots,n\}$ can be encoded by $r$ dots and $n-1$ bars, where the dot counts between consecutive bars record how many copies of each value are chosen. So one may count either the $r$ dot positions or the $n-1$ bar positions among $n+r-1$ symbols, giving $\binom{n+r-1}{r}=\binom{n+r-1}{n-1}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- binomial coefficient ::@:: $\binom{n}{k} = n!/(k!(n-k)!) = \binom{n}{n-k}$ for $0 \le k \le n$; it counts $k$-element subsets of an $n$-element set and is also the multinomial coefficient with two groups, $\binom{n}{k,n-k}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- committee: Subcommittee of 5 from 12: 1 from A (3), 2 from B (4), 2 from C (5). How many? ::@:: $\binom{3}{1} \binom{4}{2} \binom{5}{2} = 3 \cdot 6 \cdot 10 = 180$. <!-- check: ignore-line[two_sided_calc_warning]: left has group sizes 3,4,5 -->

## multinomial coefficient and division into groups

Suppose $n \in \mathbb{N}$ items are to be divided into $k$ distinct groups of sizes $n_1, \ldots, n_k \in \mathbb{N}$ with $n_1 + \cdots + n_k = n$. Choose the first group: $\binom{n}{n_1}$; then the second from the remaining: $\binom{n-n_1}{n_2}$; and so on. The total number is $\binom{n}{n_1} \binom{n-n_1}{n_2} \cdots = n!/(n_1! n_2! \cdots n_k!)$. This is the _multinomial coefficient_ $\binom{n}{n_1, n_2, \ldots, n_k} = n!/(n_1! \cdots n_k!)$ for $n_j \in \mathbb{N}_0$ with $\sum n_j = n$. For $k=2$ this reduces to the binomial coefficient $\binom{n}{k} = \binom{n}{k,n-k}$. Example: assign 10 employees to tasks A (5), B (3), C (2): $10!/(5!\,3!\,2!) = 2520$, which is also the number of permutations of the "word" AAAAABBBCC.

The denominator has a clear meaning. If one first writes all $n$ items in order, then permuting the members inside group 1 does not change the final division into labeled groups, and the same is true inside every other group. So the factors $n_1!,\ldots,n_k!$ divide out the internal reorderings that do not create a genuinely new grouping.

---

Flashcards for this section are as follows:

- division into k groups ::@:: Number of ways to partition $n$ items into $k$ labeled groups of sizes $n_1, \ldots, n_k$: $n!/(n_1! \cdots n_k!)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- multinomial coefficient ::@:: $\binom{n}{n_1, \ldots, n_k} = n!/(n_1! \cdots n_k!)$ with $n_1 + \cdots + n_k = n$; generalizes $\binom{n}{k}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why the multinomial denominator appears ::@:: After ordering all $n$ items, permutations within the same labeled group do not change the final division, so one divides by $n_1!\cdots n_k!$ to remove those internal reorderings. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- employees to tasks: 10 employees, 5 for A, 3 for B, 2 for C. How many assignments? ::@:: $10!/(5!\,3!\,2!) = 2520$ (same as permutations of AAAAABBBCC). <!-- check: ignore-line[two_sided_calc_warning]: left has 10, 5, 3, 2 -->

## multinomial and binomial theorems

For $x_1, \ldots, x_k \in \mathbb{R}$ and $n \in \mathbb{N}$, $(x_1 + \cdots + x_k)^n = \sum \binom{n}{n_1, \ldots, n_k} x_1^{n_1} \cdots x_k^{n_k}$, where the sum is over $(n_1, \ldots, n_k) \in \mathbb{N}_0^k$ with $n_1 + \cdots + n_k = n$. The binomial theorem is the case $k=2$: $(x+y)^n = \sum_{k=0}^n \binom{n}{k} x^k y^{n-k}$.

---

Flashcards for this section are as follows:

- multinomial theorem ::@:: $(x_1 + \cdots + x_k)^n = \sum_{n_1+\cdots+n_k=n} \binom{n}{n_1,\ldots,n_k} x_1^{n_1} \cdots x_k^{n_k}$; for $k=2$ this reduces to the binomial theorem. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- binomial theorem ::@:: $(x+y)^n = \sum_{k=0}^n \binom{n}{k} x^k y^{n-k}$ for $x, y \in \mathbb{R}$, $n \in \mathbb{N}$; special case of the multinomial theorem with two variables. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
