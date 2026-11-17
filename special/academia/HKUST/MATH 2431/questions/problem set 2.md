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

> 1.a. The birthday problem. For $2\le n\le N=365$, let $A_n$ be the event that at least two people in a group of $n$ share a birthday. Set up a probability space and describe $A_n^c$.
>
> ---
>
> - solution: {@{$\Omega=\{1,2,\dots,N\}^n$ with $P(E)=|E|/N^n$, and $A_n^c=\{\omega\in\Omega:\omega_i\ne\omega_j\text{ for all }i\ne j\}$}@}
> - explanation: Take {@{the uniform product space of birthday assignments}@}, so {@{$\Omega=\{1,2,\dots,N\}^n$ and $P(E)=|E|/N^n$}@}. <br/>
>     No shared birthday is then {@{the event $A_n^c=\{\omega\in\Omega:\omega_i\ne\omega_j\text{ for all }i\ne j\}$ of assignments with distinct coordinates}@}.

<!-- markdownlint MD028 -->

> 1.b. The birthday problem. For $2\le n\le N=365$, let $A_n$ be the event that at least two people in a group of $n$ share a birthday. Show that any fixed pair of people shares a birthday with probability $1/N$.
>
> ---
>
> - solution: {@{Any fixed pair shares a birthday with probability $1/N$}@}
> - explanation: For a fixed pair $(i,j)$, {@{once person $i$'s birthday is fixed, person $j$ matches it on exactly one of the $N$ days}@}, so {@{the match has probability $1/N$}@}.

<!-- markdownlint MD028 -->

> 1.c. The birthday problem. For $2\le n\le N=365$, let $A_n$ be the event that at least two people in a group of $n$ share a birthday. Prove $1-\dfrac{n(n-1)}{2N}\le P(A_n^c)\le\exp\!\left(-\dfrac{n(n-1)}{2N}\right)$.
>
> ---
>
> - solution: {@{Both bounds hold, $1-\dfrac{n(n-1)}{2N}\le P(A_n^c)\le\exp\!\left(-\dfrac{n(n-1)}{2N}\right)$}@}
> - explanation: The collision-free assignments are the ones to count: {@{the first person may have any of the $N$ days}@}, {@{the second must avoid the $1$ day already used}@}, {@{the third must avoid the $2$ days already used}@}, and so on. <br/>
>     This gives {@{the count $P(A_n^c)=\dfrac{N!}{(N-n)!N^n}=\prod_{j=0}^{n-1}\left(1-\dfrac{j}{N}\right)$}@}. <br/>
>     The upper bound comes from {@{applying $1-x\le e^{-x}$ to each factor}@}, which yields {@{the estimate $P(A_n^c)\le\exp\!\left(-\dfrac{n(n-1)}{2N}\right)$}@}. <br/>
>     For the lower bound {@{let $B_{ij}$ be the event that persons $i$ and $j$ collide, so that $A_n=\bigcup_{i<j}B_{ij}$}@}. <br/>
>     With {@{the pairwise probability $P(B_{ij})=1/N$}@}, the union bound gives {@{the estimate $P(A_n)\le\binom{n}{2}/N=\dfrac{n(n-1)}{2N}$}@}, hence {@{the lower bound $P(A_n^c)\ge1-\dfrac{n(n-1)}{2N}$}@}. <br/>
>     Intuitively, {@{a collision is at most as likely as the sum of the pairwise collision chances}@}.

<!-- markdownlint MD028 -->

> 1.d. The birthday problem. For $2\le n\le N=365$, let $A_n$ be the event that at least two people in a group of $n$ share a birthday. Use the approximation to find the smallest $n$ with $P(A_n)\ge1/2$.
>
> ---
>
> - solution: {@{The smallest such $n$ is $23$}@}
> - explanation: The approximation asks for {@{the threshold where the no-collision probability is about $1/2$, namely $\exp\!\left(-\dfrac{n(n-1)}{2N}\right)\approx1/2$}@}, and with {@{the value $N=365$}@} the smallest integer reached is {@{the value $n=23$}@}. <!--SR:!fsrs,2027-06-03T00:00:00.000Z,317,317.09832588,1,2,7,0,0,2026-07-21T00:00:00.000Z!fsrs,2027-08-11T00:00:00.000Z,364,364.00954593,1,2,7,0,0,2026-08-12T00:00:00.000Z!fsrs,2027-05-18T00:00:00.000Z,304,304.30256839,1,2,7,0,0,2026-07-18T00:00:00.000Z!fsrs,2027-05-24T00:00:00.000Z,309,308.57643926,1,2,7,0,0,2026-07-19T00:00:00.000Z!fsrs,2027-06-08T00:00:00.000Z,321,321.346657,1,2,7,0,0,2026-07-22T00:00:00.000Z!fsrs,2027-08-22T00:00:00.000Z,373,372.79099428,1,2,7,0,0,2026-08-14T00:00:00.000Z!fsrs,2027-08-06T00:00:00.000Z,360,359.60705616,1,2,7,0,0,2026-08-11T00:00:00.000Z!fsrs,2027-08-06T00:00:00.000Z,360,359.60705616,1,2,7,0,0,2026-08-11T00:00:00.000Z!fsrs,2027-06-03T00:00:00.000Z,317,317.09832588,1,2,7,0,0,2026-07-21T00:00:00.000Z!fsrs,2027-08-16T00:00:00.000Z,368,368.40415449,1,2,7,0,0,2026-08-13T00:00:00.000Z!fsrs,2027-08-11T00:00:00.000Z,364,364.00954593,1,2,7,0,0,2026-08-12T00:00:00.000Z!fsrs,2027-08-16T00:00:00.000Z,368,368.40415449,1,2,7,0,0,2026-08-13T00:00:00.000Z!fsrs,2027-08-27T00:00:00.000Z,377,377.17020207,1,2,7,0,0,2026-08-15T00:00:00.000Z!fsrs,2027-06-08T00:00:00.000Z,321,321.346657,1,2,7,0,0,2026-07-22T00:00:00.000Z!fsrs,2027-08-06T00:00:00.000Z,360,359.60705616,1,2,7,0,0,2026-08-11T00:00:00.000Z!fsrs,2027-01-31T00:00:00.000Z,142,142.42562933,1,2,2,0,0,2026-09-11T00:00:00.000Z!fsrs,2027-01-31T00:00:00.000Z,142,142.42562933,1,2,2,0,0,2026-09-11T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> 2.a. Bayes' theorem and total probability. Age groups $X,Y,Z$ make up $37\%$, $52\%$, and $11\%$ of respondents, and the probabilities of using a certain app regularly are $0.50$, $0.72$, and $0.89$ in those groups. Find the overall probability that a random respondent uses the app regularly.
>
> ---
>
> - solution: {@{The overall regular-use probability is $P(A)=0.6573$}@}
> - explanation: {@{The three age groups partition the respondents}@}, so by {@{the law of total probability}@} the overall chance is {@{the weighted average of the three group-specific probabilities, $P(A)=0.37\cdot0.50+0.52\cdot0.72+0.11\cdot0.89=0.6573$}@}.

<!-- markdownlint MD028 -->

> 2.b. Bayes' theorem and total probability. Age groups $X,Y,Z$ make up $37\%$, $52\%$, and $11\%$ of respondents, and the probabilities of using a certain app regularly are $0.50$, $0.72$, and $0.89$ in those groups. Let $A$ be the event of regular app use. Given that a respondent uses the app regularly, find the probability that the respondent belongs to group $X$.
>
> ---
>
> - solution: {@{The posterior probability is $P(X\mid A)=\dfrac{0.37\cdot0.50}{0.6573}\approx0.28145$}@}
> - explanation: Once someone is known to be a regular user, the groups are {@{reweighted by how likely each one was to produce that evidence}@}. <br/>
>     Bayes' theorem then gives {@{the posterior probability $P(X\mid A)=\dfrac{0.37\cdot0.50}{0.6573}\approx0.28145$}@}.

<!-- markdownlint MD028 -->

> 2.c. Bayes' theorem and total probability. Age groups $X,Y,Z$ make up $37\%$, $52\%$, and $11\%$ of respondents, and the probabilities of using a certain app regularly are $0.50$, $0.72$, and $0.89$ in those groups. Let $A$ be the event of regular app use, with $P(A)=0.6573$. Assuming an effectively unlimited respondent pool and independent responses, find how many responses are needed so that with probability at least $99.9\%$ at least one respondent is found who does _not_ use the app regularly.
>
> ---
>
> - solution: {@{The smallest such number is $17$ responses}@}
> - explanation: Each response is {@{independent with regular-use probability $p=0.6573$}@}, so the requirement fails only when {@{all $n$ respondents are still regular users, an event of probability $p^n$}@}. <br/>
>     The requirement is therefore {@{the inequality $1-p^n\ge0.999$, equivalently $p^n\le0.001$}@}, which solves to {@{the least integer $n\ge\dfrac{\log(0.001)}{\log(0.6573)}\approx16.46$}@}, namely {@{the answer $n=17$}@}. <!--SR:!fsrs,2027-08-22T00:00:00.000Z,373,372.79099428,1,2,7,0,0,2026-08-14T00:00:00.000Z!fsrs,2027-08-22T00:00:00.000Z,373,372.79099428,1,2,7,0,0,2026-08-14T00:00:00.000Z!fsrs,2027-08-27T00:00:00.000Z,377,377.17020207,1,2,7,0,0,2026-08-15T00:00:00.000Z!fsrs,2027-06-14T00:00:00.000Z,326,325.58679272,1,2,7,0,0,2026-07-23T00:00:00.000Z!fsrs,2027-06-19T00:00:00.000Z,330,329.81882824,1,2,7,0,0,2026-07-24T00:00:00.000Z!fsrs,2027-07-26T00:00:00.000Z,351,350.77791814,1,2,7,0,0,2026-08-09T00:00:00.000Z!fsrs,2027-08-06T00:00:00.000Z,360,359.60705616,1,2,7,0,0,2026-08-11T00:00:00.000Z!fsrs,2027-05-29T00:00:00.000Z,313,312.84164192,1,2,7,0,0,2026-07-20T00:00:00.000Z!fsrs,2027-08-06T00:00:00.000Z,360,359.60705616,1,2,7,0,0,2026-08-11T00:00:00.000Z!fsrs,2027-08-16T00:00:00.000Z,368,368.40415449,1,2,7,0,0,2026-08-13T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> 3.a. Rolling dice a random number of times. A fair die is rolled $N$ times, where $P(N=n)=2^{-n}$ for $n\in\mathbb N$. Let $A_n=\{N=n\}$ and let $S_M$ be the event that the total sum of all rolled faces equals $M$. Construct a probability space realizing these assumptions.
>
> ---
>
> - solution: {@{$\Omega=\{(\omega_1,\dots,\omega_n):n\in\mathbb N,\ \omega_i\in\{1,\dots,6\}\}$ with mass $12^{-n}$ on each path of length $n$}@}
> - explanation: Take {@{the set of finite die-roll sequences, $\Omega=\{(\omega_1,\dots,\omega_n):n\in\mathbb N,\ \omega_i\in\{1,\dots,6\}\}$}@}. <br/>
>     Assigning {@{each path of length $n$ the mass $12^{-n}$}@} gives {@{total mass $2^{-n}$ over the paths of that length, since there are $6^n$ of them}@}, and {@{the masses sum to $\sum_{n\ge1}2^{-n}=1$}@}.

<!-- markdownlint MD028 -->

> 3.b. Rolling dice a random number of times. A fair die is rolled $N$ times, where $P(N=n)=2^{-n}$ for $n\in\mathbb N$. Let $A_n=\{N=n\}$ and let $S_M$ be the event that the total sum of all rolled faces equals $M$. Compute $P(A_2\mid S_4)$.
>
> ---
>
> - solution: {@{P(A_2\mid S_4)=\dfrac{432}{2197}\approx0.1966}@}
> - explanation: A total of {@{exactly $4$}@} forces {@{the die to have been rolled only $1$, $2$, $3$, or $4$ times}@}. <br/>
>     Counting the ways to write $4$ as a sum of that many positive faces gives {@{one way for length $1$, three ways for length $2$, three ways for length $3$, and one way for length $4$}@}, hence {@{the four conditional probabilities $P(S_4\mid A_1)=1/6$, $P(S_4\mid A_2)=3/6^2=1/12$, $P(S_4\mid A_3)=3/6^3=1/72$, and $P(S_4\mid A_4)=1/6^4$}@}. <br/>
>     Averaging with {@{the prior weights $P(A_n)=2^{-n}$}@} gives {@{the marginal $P(S_4)=\frac{2197}{20736}$}@}, and Bayes then gives {@{the answer $P(A_2\mid S_4)=\dfrac{432}{2197}\approx0.1966$}@}. <br/>
>     Intuitively, {@{a total of $4$ favors short games, but not exclusively}@}.

<!-- markdownlint MD028 -->

> 3.c. Rolling dice a random number of times. A fair die is rolled $N$ times, where $P(N=n)=2^{-n}$ for $n\in\mathbb N$. Let $A_n=\{N=n\}$ and let $S_M$ be the event that the total sum of all rolled faces equals $M$. If $A_e$ is the event that $N$ is even, compute $P(S_4\mid A_e)$.
>
> ---
>
> - solution: {@{P(S_4\mid A_e)=\dfrac{433}{6912}\approx0.0626}@}
> - explanation: Conditioning on {@{an even number of rolls}@} keeps {@{only the lengths $2$ and $4$}@}, since {@{every odd length is thrown away before renormalizing}@}. <br/>
>     With {@{the even-roll probability $P(A_e)=\sum_{k\ge1}2^{-2k}=1/3$}@}, the result is {@{the value $P(S_4\mid A_e)=\dfrac{(1/12)(1/4)+(1/6^4)(1/16)}{1/3}=\dfrac{433}{6912}\approx0.0626$}@}. <!--SR:!fsrs,2027-04-08T00:00:00.000Z,258,258.1896513,1.32990818,2,7,0,0,2026-07-24T00:00:00.000Z!fsrs,2027-07-26T00:00:00.000Z,351,350.77791814,1,2,7,0,0,2026-08-09T00:00:00.000Z!fsrs,2027-08-22T00:00:00.000Z,373,372.79099428,1,2,7,0,0,2026-08-14T00:00:00.000Z!fsrs,2027-08-27T00:00:00.000Z,377,377.17020207,1,2,7,0,0,2026-08-15T00:00:00.000Z!fsrs,2027-08-22T00:00:00.000Z,373,372.79099428,1,2,7,0,0,2026-08-14T00:00:00.000Z!fsrs,2027-07-26T00:00:00.000Z,351,350.77791814,1,2,7,0,0,2026-08-09T00:00:00.000Z!fsrs,2027-08-16T00:00:00.000Z,368,368.40415449,1,2,7,0,0,2026-08-13T00:00:00.000Z!fsrs,2027-05-24T00:00:00.000Z,309,308.57643926,1,2,7,0,0,2026-07-19T00:00:00.000Z!fsrs,2027-08-11T00:00:00.000Z,364,364.00954593,1,2,7,0,0,2026-08-12T00:00:00.000Z!fsrs,2027-08-27T00:00:00.000Z,377,377.17020207,1,2,7,0,0,2026-08-15T00:00:00.000Z!fsrs,2027-08-27T00:00:00.000Z,377,377.17020207,1,2,7,0,0,2026-08-15T00:00:00.000Z!fsrs,2027-05-23T00:00:00.000Z,309,308.57643926,1,2,7,0,0,2026-07-18T00:00:00.000Z!fsrs,2027-08-16T00:00:00.000Z,368,368.40415449,1,2,7,0,0,2026-08-13T00:00:00.000Z!fsrs,2027-06-19T00:00:00.000Z,330,329.81882824,1,2,7,0,0,2026-07-24T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> 4\. Sample size vs. signal strength. An urn initially contains $3$ red and $3$ blue balls. One ball $A$ is removed uniformly at random and hidden. Peter then draws with replacement $6$ times from the remaining urn and sees red every time; Paula draws with replacement $600$ times and sees $303$ red and $297$ blue. Let $R$ be the event that the removed hidden ball was red, let $P_1$ denote Peter's data, and let $P_2$ denote Paula's data. Compute $P(R)$, $P(R\mid P_1)$, and $P(R\mid P_2)$, and interpret the result.
>
> ---
>
> - solution: {@{$P(R)=1/2$, $P(R\mid P_1)=\dfrac{1}{1+(3/2)^6}\approx0.0807$, and $P(R\mid P_2)=\dfrac{1}{1+(3/2)^6}$, so both datasets give the same posterior}@}
> - explanation: The hidden ball is initially {@{equally likely to be red or blue}@}, so {@{the prior is $P(R)=1/2$}@}. <br/>
>     If the hidden ball was red the urn is {@{biased toward blue}@}, so {@{Peter's six-red observation has likelihood $(2/5)^6$}@}, while a blue hidden ball gives {@{the competing likelihood $(3/5)^6$}@}. <br/>
>     Bayes therefore gives {@{the posterior $P(R\mid P_1)=\dfrac{(2/5)^6(1/2)}{(2/5)^6(1/2)+(3/5)^6(1/2)}=\dfrac{1}{1+(3/2)^6}\approx0.0807$}@}. <br/>
>     For Paula {@{the two binomial likelihoods differ only through the excess of red over blue observations, and here that excess is again $6$}@}, so {@{the same likelihood ratio $(3/2)^6$ appears, giving $P(R\mid P_2)=\dfrac{1}{1+(3/2)^6}$}@}. <br/>
>     The lesson is that {@{Bayes cares about the likelihood ratio, and here both datasets provide the same red-minus-blue evidence}@}.
