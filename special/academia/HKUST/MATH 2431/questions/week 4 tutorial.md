---
aliases:
    - HKUST MATH 2431 week 4 tutorial
    - HKUST MATH2431 week 4 tutorial
    - MATH 2431 week 4 tutorial
    - MATH2431 week 4 tutorial
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/week_4_tutorial
    - language/in/English
---

# week 4 tutorial

- HKUST MATH 2431

The questions on this page summarize the _official tutorial materials_ for week 4. Because they come from course materials rather than repository-authored review prompts, each question is kept as a markdown quote block and the clozes live inside that quoted Q&A block.

- topics: probability measures; conditional probability; Bayes' theorem; independence; inclusion-exclusion.

> If $P[A_i]=1$ for all $i\in\mathbb{N}$, show the following:
>
> - (a) $P[\bigcap_{i=1}^N A_i]=1$ for every $N$.
> - (b) $P[\bigcap_{i=1}^{\infty}A_i]=1$.
>
> Solution:
>
> - (a) One approach is {@{induction plus inclusion-exclusion using $P(A\cap B)=P(A)+P(B)-P(A\cup B)$: if $P(A)=P(B)=1$, then $P(A\cap B)=1$, so $P(\bigcap_{i=1}^N A_i)=1$ for every finite $N$}@}.
> - (b) Let {@{$C_N=\bigcap_{i=1}^N A_i$}@}. Then {@{the decreasing-limit relation $C_N\downarrow\bigcap_{i=1}^{\infty}A_i$ lets continuity from above give $P(\bigcap_{i=1}^{\infty}A_i)=1$}@}. Equivalently, one can use {@{de Morgan on complements}@}: since {@{$P(A_i^c)=0$}@}, countable subadditivity {@{yields $P((\bigcap_i A_i)^c)=P(\bigcup_i A_i^c)\le\sum_iP(A_i^c)=0$}@}. <!--SR:!2000-01-01,1,250!2026-04-12,4,270!2000-01-01,1,250!2000-01-01,1,250!2026-04-12,4,270!2000-01-01,1,250-->

<!-- markdownlint MD028 -->

> A family has two children. What is the probability that both are boys under the following conditions?
>
> - (a) At least one child is a boy.
> - (b) The younger child is a boy.
>
> Solution:
>
> - (a) Use the {@{ordered equally likely sample space $\Omega=\{BB,BG,GB,GG\}$}@}. Conditioning on {@{at least one boy reduces the space to $\{BB,BG,GB\}$, so $P(BB\mid\text{at least one boy})=1/3$}@}.
> - (b) Conditioning on {@{the younger child being a boy reduces the space to $\{BB,BG\}$, so $P(BB\mid\text{younger boy})=1/2$}@}. The difference from part (a) is that {@{the statement "younger child is a boy" singles out a specific coordinate, whereas "at least one boy" does not}@}.

<!-- markdownlint MD028 -->

> In the Monty Hall problem, after you choose door $D_1$ and the host opens goat door $D_3$, should you switch to $D_2$?
>
> Solution: {@{Switch to $D_2$}@}. Before any reveal, $P(\text{car at }D_1)=1/3$ and $P(\text{car in }\{D_2,D_3\})=2/3$. The host's rule is informative: {@{he never opens your chosen door and never opens a car door}@}, so after he opens $D_3$ the full $2/3$ probability on the unchosen pair concentrates on $D_2$. Equivalently, the posterior probabilities are {@{$P(\text{car at }D_1\mid H=D_3)=1/3$ and $P(\text{car at }D_2\mid H=D_3)=2/3$}@}. <!--SR:!2026-04-12,4,270!2000-01-01,1,250!2026-04-12,4,270-->

<!-- markdownlint MD028 -->

> There are 15 tennis balls in a box, of which 9 are new. Three are chosen, played with, and returned; later another 3 are chosen. Find the probability that none of the second batch has ever been used before.
>
> Solution: Let $U$ be the {@{number of new balls used in the first sample of size 3}@} so that $P(U=u)=\dfrac{\binom{9}{u}\binom{6}{3-u}}{\binom{15}{3}}$ for $u=0,1,2,3$. Conditional on $U=u$, the second sample is all new with probability {@{$\dfrac{\binom{9-u}{3}}{\binom{15}{3}}$}@} because {@{only $9-u$ unused new balls remain available}@}. Therefore, by {@{conditioning and total probability}@}, {@{$P(\text{second sample all new})=\sum_{u=0}^3\frac{\binom{9}{u}\binom{6}{3-u}}{\binom{15}{3}}\cdot\frac{\binom{9-u}{3}}{\binom{15}{3}}\approx0.0893$}@}.

<!-- markdownlint MD028 -->

> A bin contains flashlight types 1, 2, 3 with proportions $0.2$, $0.3$, $0.5$, and probabilities of lasting more than 100 hours $0.7$, $0.4$, $0.3$. Let $T_i$ be event "selected flashlight is type $i$" and $F$ be event "selected flashlight lasts more than 100 hours." Find $P(F)$ and the posterior probabilities of each type given $F$.
>
> Solution: {@{Total probability gives the overall success probability}@} {@{$P(F)=\sum_{i=1}^3P(F\mid T_i)P(T_i)=0.41$}@}. Then Bayes' theorem gives {@{$P(T_i\mid F)=\dfrac{P(F\mid T_i)P(T_i)}{P(F)}$}@}, so the posterior probabilities are {@{$P(T_1\mid F)=\frac{14}{41}\approx0.3415$, $P(T_2\mid F)=\frac{12}{41}\approx0.2927$, and $P(T_3\mid F)=\frac{15}{41}\approx0.3659$}@}. In words, {@{conditioning on long life reweights the type probabilities toward the more reliable flashlight types}@}. <!--SR:!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2026-04-12,4,270!2026-04-12,4,270-->

<!-- markdownlint MD028 -->

> If each of the $N$ coupon types is equally likely on each independent draw and $D_n$ is the number of distinct types seen in the first $n$ draws, find $P(D_n=k)$.
>
> Solution: Break the count into two steps: first choose {@{which $k$ labels are actually observed}@} in {@{$\binom Nk$}@} ways; then, for that fixed set of $k$ labels, count length-$n$ sequences that use {@{every one of those $k$ labels at least once}@}. Start from {@{$k^n$}@} total sequences and apply {@{inclusion-exclusion}@} on missing labels to get {@{$\sum_{j=0}^k(-1)^j\binom{k}{j}(k-j)^n$}@}. Since all $N^n$ draw sequences are equally likely, divide by {@{$N^n$}@}: {@{$P(D_n=k)=\frac{\binom Nk}{N^n}\sum_{j=0}^k(-1)^j\binom{k}{j}(k-j)^n$}@}. <!--SR:!2026-04-12,4,270!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250-->
