---
aliases:
    - HKUST MATH 2431 problem set 1
    - HKUST MATH2431 problem set 1
    - MATH 2431 problem set 1
    - MATH2431 problem set 1
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/problem_set_1
    - language/in/English
---

# problem set 1

- HKUST MATH 2431

The questions on this page summarize the _official problem-set materials_ for problem set 1. As with the tutorial pages, each official question is kept as a markdown quote block and the clozes live inside the quoted Q&A block.

- topics: elementary combinatorics; set operations; de Morgan's rules; finite Laplace spaces; inclusion-exclusion.

> 1.a. Distribute $12$ indistinguishable coins to $5$ distinct persons.
>
> ---
>
> - solution: {@{$\binom{5+12-1}{12}=\binom{16}{12}=1820$}@}
> - explanation: {@{Stars and bars counts distributions of indistinguishable items into distinct boxes.}@}

<!-- markdownlint MD028 -->

> 1.b. Assign distinct colors from $9$ available colors to $5$ different courses.
>
> ---
>
> - solution: {@{$9\cdot8\cdot7\cdot6\cdot5=\dfrac{9!}{4!}=15120$}@}
> - explanation: The colors are {@{chosen in order for the $5$ different courses}@}, since {@{a color cannot be reused once assigned}@}. <br/>
>     {@{The first course has $9$ choices and each later one loses a color}@}, so {@{the count is the product $9\cdot8\cdot7\cdot6\cdot5$}@}.

<!-- markdownlint MD028 -->

> 1.c. Count the on/off configurations of $10$ independent lamps.
>
> ---
>
> - solution: {@{$2^{10}=1024$ configurations}@}
> - explanation: {@{Each lamp has $2$ states independently, so the product rule multiplies $10$ factors of $2$.}@}

<!-- markdownlint MD028 -->

> 1.d. In a $6$-out-of-$49$ lottery, count outcomes with exactly $3$ correct guesses and the corresponding probability.
>
> ---
>
> - solution: {@{$\binom{6}{3}\binom{43}{3}$ favorable tickets, with probability $\dfrac{\binom{6}{3}\binom{43}{3}}{\binom{49}{6}}\approx0.0176$}@}
> - explanation: Exactly {@{3 correct guesses}@} needs {@{3 of the $6$ winning numbers}@} and {@{$3$ of the $43$ losing numbers}@}. <br/>
>     That gives {@{$\binom{6}{3}\binom{43}{3}$ favorable tickets}@} out of {@{$\binom{49}{6}$ possible tickets}@}.

<!-- markdownlint MD028 -->

> 1.e. Form an $8$-person committee from $12$ female and $8$ male candidates with at least $3$ females and at most $5$ males.
>
> ---
>
> - solution: {@{$\sum_{j=3}^{8}\binom{12}{j}\binom{8}{8-j}=124025$}@}
> - explanation: If {@{$j$ females are chosen then $8-j$ males are chosen}@}, and "at least $3$ females, at most $5$ males" means {@{the range $j=3,4,\dots,8$}@}. <br/>
>     Summing {@{$\binom{12}{j}\binom{8}{8-j}$ over those $j$}@} gives {@{the total $124025$}@}.

<!-- markdownlint MD028 -->

> 1.f. Choose two of $n\ge2$ equally spaced points on the unit circle and find the probability that they are neighbors.
>
> ---
>
> - solution: {@{$p_2=1$, and $p_n=\dfrac{2}{n-1}$ for $n\ge3$}@}
> - explanation: {@{For $n=2$ the two chosen points}@} are {@{automatically neighbors}@}. <br/>
>     {@{When $n\ge3$}@} there are {@{$\binom{n}{2}$ unordered pairs}@} in total and {@{exactly $n$ neighboring pairs}@}, so {@{the probability $p_n=\dfrac{n}{\binom{n}{2}}=\dfrac{2}{n-1}$}@}.

<!-- markdownlint MD028 -->

> 1.g. Count anagrams and palindromes of "HANNAH".
>
> ---
>
> - solution: {@{$90$ anagrams and $6$ palindromes}@}
> - explanation: The letters form {@{a multiset with three repeated pairs}@}, so there are {@{$\dfrac{6!}{2!2!2!}=90$ anagrams}@}. <br/>
>     A palindrome is {@{fixed by its first half, since the second half mirrors it}@}, so {@{choosing $X_1,X_2,X_3$ from $\{A,H,N\}$ determines the whole word}@} and {@{there are $3!=6$ such choices}@}.

<!-- markdownlint MD028 -->

> 1.h. Order $n$ books when exactly $m$ of them are indistinguishable.
>
> ---
>
> - solution: {@{$\dfrac{n!}{m!}$ shelf orderings}@}
> - explanation: Treat {@{the identical books as repeated copies of one symbol}@}, since {@{permuting the $m$ indistinguishable copies creates no new arrangement}@}. <br/>
>     The $n!$ orderings {@{collapse by a factor of $m!$}@}, which leaves {@{the count $\dfrac{n!}{m!}$}@}.

<!-- markdownlint MD028 -->

> 2.a. A fair die is rolled $N$ times. Let $A_k$ be the event that roll $k$ is $3$, and $B_k$ the event that roll $k$ is $6$. Express the following events using the sets $A_k$, $B_k$, and elementary set operations:
>
> - (i) No $6$ ever appears.
> - (ii) A $3$ appears at least once.
> - (iii) A $6$ appears at least once and a $3$ appears at least twice.
>
> ---
>
> - solution: {@{$\bigcap_{k=1}^{N}B_k^c$; $\bigcup_{k=1}^{N}A_k$; $\left(\bigcup_{k=1}^{N}B_k\right)\cap\left(\bigcup_{\ell,m=1\,;\,\ell\ne m}^{N}(A_\ell\cap A_m)\right)$}@}
> - explanation: "No $6$ ever appears" says {@{every roll fails its own $B_k$}@}, so {@{the complements $B_k^c$ are intersected over all $N$ rolls}@}. <br/>
>     "A $3$ appears at least once" says {@{some $A_k$ occurs}@}, so {@{the events $A_k$ are united over $k$}@}. <br/>
>     "A $6$ at least once and a $3$ at least twice" needs {@{a union over the $B_k$}@}, {@{intersected with a union over the pairs of distinct $A_\ell$ and $A_m$}@}.

<!-- markdownlint MD028 -->

> 2.b. A fair die is rolled $N$ times. Let $A_k$ be the event that roll $k$ is $3$, and $B_k$ the event that roll $k$ is $6$. Describe in words the events below:
>
> - (i) $\left(\bigcup_{i=1}^{N}A_i^c\right)^c$
> - (ii) $\bigcup_{i=1}^{N-2}(A_i\cap A_{i+1}\cap B_{i+2})$
> - (iii) $\bigcap_{i=1}^{N-1}(A_i\cup B_{i+1})$
>
> ---
>
> - solution: {@{Every roll is a $3$; the pattern $3$-$3$-$6$ occurs somewhere in consecutive positions; for every adjacent pair of times, either the left roll is $3$ or the next roll is $6$}@}
> - explanation: The inner union is {@{the event that some roll is not a $3$}@}, so its complement says {@{every roll is a $3$}@}. <br/>
>     Each member of the second union says {@{rolls $i$ and $i+1$ are $3$ and roll $i+2$ is $6$}@}, and the union runs over {@{every starting position $i$}@}. <br/>
>     The intersection over $i$ says that at each adjacent pair {@{the left roll is $3$ or the next roll is $6$}@}.

<!-- markdownlint MD028 -->

> 2.c. A fair die is rolled $N$ times. Let $A_k$ be the event that roll $k$ is $3$, and $B_k$ the event that roll $k$ is $6$. Prove $\left(\bigcup_{i\in I}A_i\right)^c=\bigcap_{i\in I}A_i^c$.
>
> ---
>
> - solution: {@{The two sets are equal by an elementwise argument}@}
> - explanation: An outcome lies in $\left(\bigcup_{i\in I}A_i\right)^c$ iff {@{it belongs to no $A_i$}@}, which happens iff {@{it belongs to every $A_i^c$}@}. <br/>
>     {@{That second condition}@} is exactly {@{membership in $\bigcap_{i\in I}A_i^c$}@}.

<!-- markdownlint MD028 -->

> 2.d. A fair die is rolled $N$ times. Let $A_k$ be the event that roll $k$ is $3$, and $B_k$ the event that roll $k$ is $6$. Prove $\left(\bigcap_{i\in I}A_i\right)^c=\bigcup_{i\in I}A_i^c$.
>
> ---
>
> - solution: {@{Both de Morgan identities follow directly from membership logic}@}
> - explanation: An outcome lies in $\left(\bigcap_{i\in I}A_i\right)^c$ iff {@{it misses at least one $A_i$}@}, which happens iff {@{it belongs to at least one $A_i^c$}@}. <br/>
>     {@{That condition}@} is exactly {@{membership in $\bigcup_{i\in I}A_i^c$}@}.

<!-- markdownlint MD028 -->

> 3.a. A fair die is rolled twice, on the Laplace space $\Omega=\{1,2,3,4,5,6\}^2$ with $P(E)=|E|/36$. Calculate the probability that $6$ occurs exactly once.
>
> ---
>
> - solution: {@{$P=10/36=5/18$}@}
> - explanation: {@{One coordinate is $6$ and the other is not, giving $10$ outcomes.}@}

<!-- markdownlint MD028 -->

> 3.b. A fair die is rolled twice, on the Laplace space $\Omega=\{1,2,3,4,5,6\}^2$ with $P(E)=|E|/36$. Calculate the probability that both outcomes are odd.
>
> ---
>
> - solution: {@{$P=9/36=1/4$}@}
> - explanation: {@{Each roll lies in $\{1,3,5\}$, giving $3^2=9$ outcomes.}@}

<!-- markdownlint MD028 -->

> 3.c. A fair die is rolled twice, on the Laplace space $\Omega=\{1,2,3,4,5,6\}^2$ with $P(E)=|E|/36$. Calculate the probability that the sum is $4$.
>
> ---
>
> - solution: {@{$P=3/36=1/12$}@}
> - explanation: {@{The sum is $4$ exactly for $(1,3)$, $(2,2)$, and $(3,1)$.}@}

<!-- markdownlint MD028 -->

> 3.d. A fair die is rolled twice, on the Laplace space $\Omega=\{1,2,3,4,5,6\}^2$ with $P(E)=|E|/36$. Calculate the probability that the sum is a multiple of $3$.
>
> ---
>
> - solution: {@{$P=12/36=1/3$}@}
> - explanation: {@{A multiple of $3$ means the sum is $3$, $6$, $9$, or $12$, which yields $12$ ordered pairs.}@}

<!-- markdownlint MD028 -->

> 4.a. For events $A_1,\dots,A_n$ in a probability space, prove the full inclusion-exclusion formula $P\left[\bigcup_{j=1}^{n}A_j\right]=\sum_{k=1}^{n}(-1)^{k+1}\sum_{1\le i_1<\cdots<i_k\le n}P\left[A_{i_1}\cap\cdots\cap A_{i_k}\right]$.
>
> ---
>
> - solution: {@{The full inclusion-exclusion formula holds for every $n$}@}
> - explanation: The formula is proven by {@{induction on $n$}@}: {@{the case $n=1$}@} is trivial, and {@{the case $n=2$}@} is {@{the familiar identity $P(B\cup C)=P(B)+P(C)-P(B\cap C)$}@}. <br/>
>     Assume the alternating formula for {@{the events $A_1,\dots,A_n$}@} and write {@{$B=\bigcup_{j=1}^{n}A_j$ and $C=A_{n+1}$}@}. <br/>
>     Then {@{the union satisfies $P\left[\bigcup_{j=1}^{n+1}A_j\right]=P(B\cup C)=P(B)+P(C)-P(B\cap C)$}@}, where {@{the term $P(B)$}@} contributes {@{the intersections that do not involve $A_{n+1}$}@}. <br/>
>     Since {@{the intersection $B\cap C=\bigcup_{j=1}^{n}(A_j\cap A_{n+1})$}@}, the induction hypothesis on {@{that intersection}@} contributes {@{the intersections that do involve $A_{n+1}$}@}, {@{with the opposite sign from the leading minus}@}. <br/>
>     The alternating pattern therefore {@{extends from $n$ to $n+1$}@}: {@{add single-set terms}@}, {@{subtract pairwise intersections}@}, and {@{add triple intersections}@}, and so on.

<!-- markdownlint MD028 -->

> 4.b. For events $A_1,\dots,A_n$ in a probability space, prove the bounds
>
> - $P\left[\bigcup_{j=1}^{n}A_j\right]\le\sum_{j=1}^{n}P[A_j]-\sum_{j=1}^{n-1}P[A_j\cap A_{j+1}]$
> - $P\left[\bigcup_{j=1}^{n}A_j\right]\ge\sum_{j=1}^{n}P[A_j]-\sum_{1\le i<j\le n}P[A_i\cap A_j]$
>
> ---
>
> - solution: {@{The Bonferroni upper and lower bounds both follow}@}
> - explanation: Both bounds come from {@{truncating inclusion-exclusion after the first or second level of correction}@}. <br/>
>     With {@{$B=\bigcup_{j=1}^{n}A_j$ and $C=A_{n+1}$}@}, the starting point is always {@{the identity $P(B\cup C)=P(B)+P(C)-P(B\cap C)$}@}. <br/>
>     The upper bound wants {@{the subtraction as small as possible}@}, so {@{the crude bound $P(B\cap A_{n+1})\ge P(A_n\cap A_{n+1})$, since $A_n\cap A_{n+1}\subseteq B\cap A_{n+1}$}@} suffices. <br/>
>     The lower bound wants {@{the subtraction as large as possible}@}, so {@{the intersection $B\cap A_{n+1}$}@} is bounded above by {@{the union bound $P(B\cap A_{n+1})\le\sum_{j=1}^{n}P(A_j\cap A_{n+1})$}@}. <br/>
>     Substituting {@{the two estimates}@} gives {@{the stated Bonferroni upper and lower bounds}@}.
