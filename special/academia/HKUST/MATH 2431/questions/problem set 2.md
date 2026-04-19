---
aliases:
    - HKUST MATH 2431 problem set 2
    - HKUST MATH2431 problem set 2
    - MATH 2431 problem set 2
    - MATH2431 problem set 2
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/problem_set_2
    - language/in/English
---

# problem set 2

- HKUST MATH 2431

The questions on this page summarize the _official problem-set materials_ for problem set 2. As with the tutorial pages, each official question is kept as a markdown quote block and the clozes live inside the quoted Q&A block.

- topics: birthday problem; Bayes' theorem; law of total probability; random sample spaces; conditional probability; Bayesian evidence.

> The birthday problem. For $2\le n\le N=365$, let $A_n$ be the event that at least two people in a group of $n$ share a birthday.
>
> - (a) Set up a probability space and describe $A_n^c$.
> - (b) Show that any fixed pair of people shares a birthday with probability $1/N$.
> - (c) Prove $1-\dfrac{n(n-1)}{2N}\le P(A_n^c)\le\exp\!\left(-\dfrac{n(n-1)}{2N}\right)$.
> - (d) Use the approximation to find the smallest $n$ with $P(A_n)\ge 1/2$.
>
> Solution:
>
> - (a) Use the {@{uniform product space of birthday assignments}@} with $\Omega=\{1,2,\dots,N\}^n$ and $P(E)=|E|/N^n$; then {@{the event of no shared birthdays is $A_n^c=\{\omega\in\Omega: \omega_i\ne\omega_j\text{ for all }i\ne j\}$}@}.
> - (b) For a fixed pair $(i,j)$, {@{once person $i$ is assigned a day, person $j$ matches it with probability $1/N$}@}.
> - (c) The no-collision event is especially simple to count: the first person can have any birthday, the second must avoid 1 used day, the third must avoid 2 used days, and so on. So {@{$P(A_n^c)=\dfrac{N!}{(N-n)!N^n}=\prod_{j=0}^{n-1}\left(1-\dfrac{j}{N}\right)$}@}. For the upper bound, use {@{$1-x\le e^{-x}$}@} term-by-term to get {@{$P(A_n^c)\le\exp\!\left(-\sum_{j=0}^{n-1}\dfrac{j}{N}\right)=\exp\!\left(-\dfrac{n(n-1)}{2N}\right)$}@}. For the lower bound, let {@{$B_{ij}$}@} be the event that persons $i$ and $j$ collide. Then {@{$A_n=\bigcup_{i<j}B_{ij}$}@}, so by the union bound and {@{$P(B_{ij})=1/N$}@}, {@{$P(A_n)\le\binom{n}{2}/N=n(n-1)/(2N)$}@}. Therefore {@{$P(A_n^c)\ge1-\dfrac{n(n-1)}{2N}$}@}. Intuitively, the lower bound says {@{a collision is at most as likely as the sum of the pairwise collision chances}@}.
> - (d) The approximation says to look for the point where {@{the no-collision probability is about $1/2$, i.e. $\exp\!\left(-\dfrac{n(n-1)}{2N}\right)\approx1/2$}@}; with {@{$N=365$}@}, the first integer crossing that threshold is {@{$n=23$}@}. <!--SR:!2026-04-12,4,270!2026-04-12,4,283!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,283!2026-04-12,4,283!2026-04-12,4,283!2026-04-12,4,270!2026-04-12,4,283!2026-04-12,4,283!2026-04-12,4,283!2026-04-12,4,283!2026-04-12,4,270!2026-04-12,4,283-->

<!-- markdownlint MD028 -->

> Bayes' theorem and total probability. Age groups $X,Y,Z$ make up $37\%$, $52\%$, and $11\%$ of respondents, and the probabilities of using a certain app regularly are $0.50$, $0.72$, and $0.89$ in those groups.
>
> - (a) Find the overall probability that a random respondent uses the app regularly.
> - (b) Given that a respondent uses the app regularly, find the probability that the respondent belongs to group $X$.
> - (c) Assuming an effectively unlimited respondent pool and independent responses, find how many responses are needed so that with probability at least $99.9\%$ at least one respondent is found who does _not_ use the app regularly.
>
> Solution:
>
> - Let $A$ be the event {@{regular app use}@}.
> - (a) By the {@{law of total probability}@}, the overall regular-use chance is the {@{weighted average of the three group-specific probabilities}@}: {@{$P(A)=0.37\cdot0.50+0.52\cdot0.72+0.11\cdot0.89=0.6573$}@}.
> - (b) Once we know someone is a regular user, we reweight the groups by how likely each group was to produce that evidence. Bayes' theorem gives {@{the posterior probability $P(X\mid A)=\dfrac{0.37\cdot0.50}{0.6573}\approx0.28145$}@}.
> - (c) If each response is independent and has regular-use probability {@{$p=0.6573$}@}, then the only way to fail the requirement is that {@{every one of the $n$ respondents is still a regular user, which has probability $p^n$}@}. So we need {@{the inequality $1-p^n\ge0.999$, equivalently $p^n\le0.001$}@}. Solving gives {@{$n\ge\dfrac{\log(0.001)}{\log(0.6573)}\approx16.46$}@}, so the smallest integer is {@{$17$}@}. <!--SR:!2026-04-12,4,283!2026-04-12,4,283!2026-04-12,4,283!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,283!2026-04-12,4,283!2026-04-12,4,270!2026-04-12,4,283!2026-04-12,4,283-->

<!-- markdownlint MD028 -->

> Rolling dice a random number of times. A fair die is rolled $N$ times, where $P(N=n)=2^{-n}$ for $n\in\mathbb N$. Let $A_n=\{N=n\}$ and let $S_M$ be the event that the total sum of all rolled faces equals $M$.
>
> - (a) Construct a probability space realizing these assumptions.
> - (b) Compute $P(A_2\mid S_4)$.
> - (c) If $A_e$ is the event that $N$ is even, compute $P(S_4\mid A_e)$.
>
> Solution:
>
> - (a) A convenient sample space is $\Omega=\{(\omega_1,\dots,\omega_n):n\in\mathbb N,\ \omega_i\in\{1,\dots,6\}\}$. Assign each path of length $n$ the mass {@{$12^{-n}$}@}; then {@{summing over all paths of length $n$ gives total mass $2^{-n}$}@}, and {@{$\sum_{n\ge1}2^{-n}=1$}@}.
> - (b) If the total sum is {@{$4$}@}, then the die can only have been rolled {@{$1,2,3,$ or $4$ times}@}. For each possible length, count the ways to write 4 as a sum of that many positive die faces: one way for length 1, three ways for length 2, three ways for length 3, and one way for length 4. That gives {@{the four conditional probabilities $P(S_4\mid A_1)=1/6$, $P(S_4\mid A_2)=3/6^2=1/12$, $P(S_4\mid A_3)=3/6^3=1/72$, and $P(S_4\mid A_4)=1/6^4$}@}. Averaging with the prior weights {@{$P(A_n)=2^{-n}$}@} gives {@{$P(S_4)=\frac{2197}{20736}$}@}, and then Bayes gives {@{$P(A_2\mid S_4)=\dfrac{432}{2197}\approx0.1966$}@}. Intuitively, {@{sum 4 favors short games, but not exclusively}@}.
> - (c) If we condition on {@{'the number of rolls is even'}@}, then only lengths {@{$2$ and $4$}@} survive; all odd lengths are thrown away before renormalizing. Since {@{$P(A_e)=\sum_{k\ge1}2^{-2k}=1/3$}@}, we get {@{$P(S_4\mid A_e)=\dfrac{(1/12)(1/4)+(1/6^4)(1/16)}{1/3}=\dfrac{433}{6912}\approx0.0626$}@}. <!--SR:!2026-04-12,4,283!2026-04-12,4,283!2026-04-12,4,283!2026-04-12,4,283!2026-04-12,4,283!2026-04-12,4,283!2026-04-12,4,283!2026-04-12,4,270!2026-04-12,4,283!2026-04-12,4,283!2026-04-12,4,283!2026-04-12,4,270!2026-04-12,4,283!2026-04-12,4,270-->

<!-- markdownlint MD028 -->

> Sample size vs. signal strength. An urn initially contains $3$ red and $3$ blue balls. One ball $A$ is removed uniformly at random and hidden. Peter then draws with replacement $6$ times from the remaining urn and sees red every time; Paula draws with replacement $600$ times and sees $303$ red and $297$ blue. Let $R$ be the event that the removed hidden ball was red, let $P_1$ denote Peter's data, and let $P_2$ denote Paula's data. Compute $P(R)$, $P(R\mid P_1)$, and $P(R\mid P_2)$, and interpret the result.
>
> Solution: Initially the hidden ball is equally likely to be red or blue, so {@{$P(R)=1/2$}@}. If the hidden ball was red, the remaining urn is biased toward blue, so {@{Peter's six-red observation has likelihood $(2/5)^6$}@}; if the hidden ball was blue, the urn is biased toward red, so {@{the competing likelihood is $(3/5)^6$}@}. Bayes therefore gives {@{$P(R\mid P_1)=\dfrac{(2/5)^6(1/2)}{(2/5)^6(1/2)+(3/5)^6(1/2)}=\dfrac{1}{1+(3/2)^6}\approx0.0807$}@}. For Paula, the same idea applies: the two binomial likelihoods differ only through the excess of red over blue observations, and here that excess is again {@{$6$}@}. So {@{the same likelihood ratio $(3/2)^6$ appears, giving $P(R\mid P_2)=\dfrac{1}{1+(3/2)^6}$}@}. The lesson is that {@{Bayes cares about the likelihood ratio, and here both datasets provide the same red-minus-blue evidence}@}. <!--SR:!2026-04-12,4,283!2026-04-12,4,283!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,283!2026-04-12,4,283!2026-04-12,4,283-->
