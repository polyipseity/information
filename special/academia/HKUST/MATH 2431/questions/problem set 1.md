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

> Elementary combinatorics. Solve the following:
>
> - (a) Distribute $12$ indistinguishable coins to $5$ distinct persons.
> - (b) Assign distinct colors from $9$ available colors to $5$ different courses.
> - (c) Count the on/off configurations of $10$ independent lamps.
> - (d) In a $6$-out-of-$49$ lottery, count outcomes with exactly $3$ correct guesses and the corresponding probability.
> - (e) Form an $8$-person committee from $12$ female and $8$ male candidates with at least $3$ females and at most $5$ males.
> - (f) Choose two of $n\ge 2$ equally spaced points on the unit circle and find the probability that they are neighbors.
> - (g) Count anagrams and palindromes of "HANNAH".
> - (h) Order $n$ books when exactly $m$ of them are indistinguishable.
>
> Solution:
>
> - (a) {@{Stars and bars}@} gives {@{$\binom{5+12-1}{12}=\binom{16}{12}=1820$}@}.
> - (b) Choosing {@{ordered distinct colors}@} gives {@{$9\cdot8\cdot7\cdot6\cdot5=\dfrac{9!}{4!}=15120$}@}, since {@{the courses are different and a color cannot be reused once assigned}@}.
> - (c) Each lamp has {@{2 states independently}@}, so by the {@{product rule}@} the count is {@{$2^{10}=1024$}@}.
> - (d) Exact-$3$ lottery guesses require choosing {@{$3$ winning numbers out of $6$ and $3$ losing numbers out of $43$}@}, so the number of favorable outcomes is {@{$\binom{6}{3}\binom{43}{3}$}@} and the probability is {@{$\dfrac{\binom{6}{3}\binom{43}{3}}{\binom{49}{6}}\approx0.0176$}@}.
> - (d) To have exactly {@{3 correct guesses}@}, first choose {@{$3$ of the $6$ winning numbers}@}, then choose {@{$3$ of the $43$ losing numbers}@}. This gives {@{$\binom{6}{3}\binom{43}{3}$ favorable tickets}@} out of {@{$\binom{49}{6}$ possible tickets}@}, so the probability is {@{$\dfrac{\binom{6}{3}\binom{43}{3}}{\binom{49}{6}}\approx0.0176$}@}.
> - (e) If {@{$j$ females are chosen then $8-j$ males are chosen}@}, and the condition 'at least 3 females, at most 5 males' means {@{$j=3,4,\dots,8$}@}, so the total is {@{$\sum_{j=3}^{8}\binom{12}{j}\binom{8}{8-j}=124025$}@}.
> - (f) For {@{$n=2$}@} the two chosen points are automatically neighbors, so {@{$p_2=1$}@}; for {@{$n\ge3$}@} there are {@{$\binom{n}{2}$ unordered pairs}@} in total and exactly {@{$n$ neighboring pairs}@}, hence {@{$p_n=\dfrac{n}{\binom{n}{2}}=\dfrac{2}{n-1}$}@}.
> - (g) The letters of "HANNAH" form a {@{multiset with three repeated pairs}@}, so the number of anagrams is {@{$\dfrac{6!}{2!2!2!}=90$}@}; a palindrome must look like {@{$X_1X_2X_3X_3X_2X_1$ with $X_1,X_2,X_3\in\{A,H,N\}$ distinct}@}, so {@{choosing the first half determines the whole word}@}, giving {@{$3!=6$ palindromes}@}.
> - (h) Treat the identical books as repeated copies of one symbol, so the number of shelf orderings is {@{$\dfrac{n!}{m!}$}@} because {@{permuting the $m$ indistinguishable copies does not create a new arrangement}@}. <!--SR:!2026-05-07,16,308!2026-05-09,17,308!2026-05-07,16,308!2026-05-06,14,290!2026-05-06,15,290!2026-05-06,15,290!2026-05-07,15,290!2026-05-08,17,308!2026-05-09,17,308!2026-05-06,15,308!2026-05-07,15,290!2026-05-09,17,308!2026-05-06,15,290!2026-05-07,16,290!2026-06-14,42,290!2026-05-09,17,308!2026-05-06,14,290!2026-05-08,17,308!2026-05-06,14,290!2026-05-07,16,290!2026-05-06,14,290!2026-05-08,17,308!2026-05-05,14,290!2026-05-08,17,308!2026-05-08,17,308!2026-05-06,14,290!2026-05-08,17,308!2026-05-08,17,308!2026-05-08,16,290!2026-05-08,16,308!2026-05-06,15,290!2026-05-08,16,308!2026-05-08,17,308-->

<!-- markdownlint MD028 -->

> Set operations and de Morgan's rules. A fair die is rolled $N$ times. Let $A_k$ be the event that roll $k$ is $3$, and $B_k$ the event that roll $k$ is $6$.
>
> - (a) Express the following events using the sets $A_k$, $B_k$, and elementary set operations:
>   - (i) No $6$ ever appears.
>   - (ii) A $3$ appears at least once.
>   - (iii) A $6$ appears at least once and a $3$ appears at least twice.
> - (b) Describe in words the events below:
>   - (i) $\left(\bigcup_{i=1}^{N}A_i^c\right)^c$
>   - (ii) $\bigcup_{i=1}^{N-2}(A_i\cap A_{i+1}\cap B_{i+2})$
>   - (iii) $\bigcap_{i=1}^{N-1}(A_i\cup B_{i+1})$
> - (c) Prove $\left(\bigcup_{i\in I}A_i\right)^c=\bigcap_{i\in I}A_i^c$.
> - (d) Prove $\left(\bigcap_{i\in I}A_i\right)^c=\bigcup_{i\in I}A_i^c$.
>
> Solution:
>
> - (a) The required set formulas are:
>   - (i) {@{$\bigcap_{k=1}^{N}B_k^c$}@}
>   - (ii) {@{$\bigcup_{k=1}^{N}A_k$}@}
>   - (iii) {@{$\left(\bigcup_{k=1}^{N}B_k\right)\cap\left(\bigcup_{\ell,m=1\,;\,\ell\ne m}^{N}(A_\ell\cap A_m)\right)$}@}
> - (b) The three events mean:
>   - (i) {@{Every roll is a $3$}@}.
>   - (ii) {@{The pattern $3$-$3$-$6$ occurs somewhere in consecutive positions}@}.
>   - (iii) {@{For every adjacent pair of times, either the left roll is $3$ or the next roll is $6$}@}.
> - (c) Argue elementwise: {@{$\omega\in\left(\bigcup_iA_i\right)^c$ iff $\omega\notin A_i$ for every $i$ iff $\omega\in A_i^c$ for every $i$ iff $\omega\in\bigcap_iA_i^c$}@}.
> - (d) Similarly, {@{$\omega\in\left(\bigcap_iA_i\right)^c$ iff $\omega\notin A_i$ for at least one $i$ iff $\omega\in A_i^c$ for at least one $i$ iff $\omega\in\bigcup_iA_i^c$}@}. Thus both {@{de Morgan identities follow directly from membership logic}@}. <!--SR:!2026-05-07,16,290!2026-05-06,15,290!2026-05-06,15,290!2026-05-08,17,308!2026-05-07,16,290!2026-05-06,14,290!2026-05-05,14,290!2026-05-07,15,308!2026-05-05,14,290-->

<!-- markdownlint MD028 -->

> Rolling dice twice. A fair die is rolled twice. Write down the probability space explicitly and calculate the following probabilities:
>
> - (a) $6$ occurs exactly once.
> - (b) Both outcomes are odd.
> - (c) The sum is $4$.
> - (d) The sum is a multiple of $3$.
>
> Solution:
>
> - Use the {@{Laplace space of ordered pairs}@} with {@{$\Omega=\{1,2,3,4,5,6\}^2$ and $P(E)=|E|/36$}@}.
> - (a) Exact-one-$6$ means {@{one coordinate is $6$ and the other is not}@}, so there are {@{$10$ outcomes}@} and {@{$P=10/36=5/18$}@}.
> - (b) Both odd means each roll lies in {@{$\{1,3,5\}$}@}, so there are {@{$3^2=9$ outcomes}@} and {@{$P=9/36=1/4$}@}.
> - (c) Sum $4$ corresponds to {@{$(1,3),(2,2),(3,1)$}@}, hence {@{$P=3/36=1/12$}@}.
> - (d) A multiple of $3$ means sum {@{$3,6,9,$ or $12$}@}, yielding {@{$12$ ordered pairs}@} in total and therefore {@{$P=12/36=1/3$}@}. <!--SR:!2026-05-07,15,308!2026-05-06,15,290!2026-05-06,15,290!2026-05-05,14,290!2026-05-07,16,290!2026-05-08,17,308!2026-05-06,15,290!2026-05-05,14,290!2026-05-09,17,308!2026-05-05,14,290!2026-05-07,15,290!2026-05-08,16,308!2026-05-06,14,290-->

<!-- markdownlint MD028 -->

> Inclusion-exclusion. For events $A_1,\dots,A_n$ in a probability space, prove the following:
>
> - (a) The full inclusion-exclusion formula
>   $P\left[\bigcup_{j=1}^{n}A_j\right]=\sum_{k=1}^{n}(-1)^{k+1}\sum_{1\le i_1<\cdots<i_k\le n}P\left[A_{i_1}\cap\cdots\cap A_{i_k}\right]$.
> - (b) The bounds
>   - $P\left[\bigcup_{j=1}^{n}A_j\right]\le\sum_{j=1}^{n}P[A_j]-\sum_{j=1}^{n-1}P[A_j\cap A_{j+1}]$
>   - $P\left[\bigcup_{j=1}^{n}A_j\right]\ge\sum_{j=1}^{n}P[A_j]-\sum_{1\le i<j\le n}P[A_i\cap A_j]$
>
> Solution:
>
> - (a) The formula to prove is {@{$P\left[\bigcup_{j=1}^{n}A_j\right]=\sum_{k=1}^{n}(-1)^{k+1}\sum_{1\le i_1<\cdots<i_k\le n}P\left[A_{i_1}\cap\cdots\cap A_{i_k}\right]$}@}. Proceed by {@{induction on $n$}@}. The case {@{$n=1$}@} is trivial, and the case {@{$n=2$}@} is exactly the familiar identity {@{$P(B\cup C)=P(B)+P(C)-P(B\cap C)$}@}. Now assume the full alternating formula is known for {@{$A_1,\dots,A_n$}@}. Write {@{$B=\bigcup_{j=1}^{n}A_j$ and $C=A_{n+1}$}@}. Then {@{$P\left[\bigcup_{j=1}^{n+1}A_j\right]=P(B\cup C)=P(B)+P(C)-P(B\cap C)$}@}. The term {@{$P(B)$}@} contributes exactly the intersections that do {@{not involve $A_{n+1}$}@}. Also {@{$B\cap C=\bigcup_{j=1}^{n}(A_j\cap A_{n+1})$}@}, so applying the induction hypothesis to {@{$B\cap C$}@} contributes exactly the intersections that {@{do involve $A_{n+1}$}@}, and they appear with the opposite sign because of the leading minus sign. Therefore the same alternating pattern extends from {@{$n$ to $n+1$}@}: add single-set terms, subtract pairwise intersections, add triple intersections, and so on.
> - (b) The two inequalities come from {@{truncating inclusion-exclusion after the first or second level of correction}@}. Using the same notation {@{$B=\bigcup_{j=1}^{n}A_j$ and $C=A_{n+1}$}@}, we always start from {@{$P(B\cup C)=P(B)+P(C)-P(B\cap C)$}@}. For the upper bound, we want to make the subtraction as small as possible, so it is enough to use a crude lower bound such as {@{$P(B\cap A_{n+1})\ge P(A_n\cap A_{n+1})$}@}, since {@{$A_n\cap A_{n+1}\subseteq B\cap A_{n+1}$}@}. For the lower bound, we want to make the subtraction as large as possible, so we bound {@{$B\cap A_{n+1}$}@} from above by the union bound: {@{$P(B\cap A_{n+1})=P\left[\bigcup_{j=1}^{n}(A_j\cap A_{n+1})\right]\le\sum_{j=1}^{n}P(A_j\cap A_{n+1})$}@}. Substituting these estimates gives the stated {@{Bonferroni upper and lower bounds}@}. <!--SR:!2026-05-08,17,308!2026-05-09,17,308!2026-05-08,17,308!2026-05-07,16,308!2026-05-08,17,308!2026-05-07,16,308!2026-05-08,17,308!2026-05-05,14,290!2026-05-08,16,290!2026-05-07,15,290!2026-05-07,16,308!2026-05-05,14,290!2026-05-05,14,290!2026-05-08,17,308!2026-05-07,16,290!2026-05-06,15,290!2026-05-05,14,290!2026-05-07,15,290!2026-05-07,16,308!2026-05-08,17,308!2026-05-05,14,290!2026-05-06,15,290-->
