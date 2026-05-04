---
aliases:
    - HKUST MATH 2431 problem set 3
    - HKUST MATH2431 problem set 3
    - MATH 2431 problem set 3
    - MATH2431 problem set 3
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/problem_set_3
    - language/in/English
---

# problem set 3

- HKUST MATH 2431

The questions on this page summarize the _official problem-set materials_ for problem set 3. As with the tutorial pages, each official question is kept as a markdown quote block and the clozes live inside the quoted Q&A block.

- topics: Monty Hall; countable sums; discrete distributions; Poisson thinning; simple random walk; ballot theorem.

> The Monty Hall problem. In the standard three-door game show:
>
> - (a) If the host always opens a different door with a goat behind it, should you switch?
> - (b) If the two goats are named Bill and Nan and, whenever the host has a choice, the host shows Bill with probability $b$, what is the winning probability of the switching strategy after Bill is shown?
> - (c) If instead the host opens one of the other doors uniformly at random and it happens to reveal a goat, what is the best strategy?
>
> Solution:
>
> - (a) Fix your original choice as {@{$D_1$}@}. There are three equally likely car locations. If the car is behind {@{$D_1$}@} (probability {@{$1/3$}@}), then switching loses. If the car is behind {@{$D_2$ or $D_3$}@} (total probability {@{$2/3$}@}), then the host is forced to open the only other goat door, so switching wins. In other words, {@{the switch strategy wins exactly when the original guess was wrong}@}, and that happens with probability {@{$2/3$}@}. Therefore {@{switching is optimal}@}.
> - (b) Keep the same setup: you first choose {@{$D_1$}@}, Bill is behind {@{$D_2$}@}, and Nan is behind {@{$D_3$}@}. If the car is behind {@{$D_1$}@}, then the host may reveal Bill with probability {@{$b$}@}. If the car is behind {@{$D_3$}@}, the host has no choice and must reveal Bill, so the probability is {@{$1$}@}. The case car behind {@{$D_2$}@} is impossible because Bill is known to be a goat. Therefore {@{$P(D_3=\text{car}\mid D_2=\text{Bill})=\dfrac{(1/3)\cdot1}{(1/3)\cdot b+(1/3)\cdot1}=\dfrac{1}{b+1}$}@}. Since {@{switching wins exactly when the car is behind $D_3$}@}, the switching probability is {@{$1/(b+1)$}@}. So {@{the host's preference changes the posterior odds even though the game still looks like Monty Hall}@}.
> - (c) Now the host chooses randomly from the two unchosen doors, so seeing a goat is less informative. Condition only on the event that {@{a goat was revealed}@}. If the car is behind your original door {@{$D_1$}@}, this event happens with probability {@{$1$}@}. If the car is behind one of the other two doors, it happens with probability {@{$1/2$}@}, because the host might accidentally pick the car door instead. Thus the conditional weights are proportional to {@{$1/3,1/6,1/6$}@}, so after normalization the original door and the remaining unopened door each have probability {@{$1/2$}@}. Hence {@{switching and staying are equally good in the random-host version}@}. <!--SR:!2026-05-17,16,290!2026-05-16,15,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-17,16,290!2026-05-16,15,290!2026-05-17,16,290!2026-05-17,16,290!2026-05-15,14,290!2026-05-17,16,290!2026-05-16,15,290!2026-05-17,16,290!2026-05-16,15,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-16,15,290!2026-05-17,16,290!2026-05-15,14,290!2026-05-17,16,290!2026-05-17,16,290!2026-05-15,14,290!2026-05-17,16,290!2026-05-15,14,290!2026-05-17,16,290!2026-05-16,15,290!2026-05-15,14,290-->

<!-- markdownlint MD028 -->

> Countable sums. Let $\Omega$ be a countable set and let $f\colon\Omega\to[0,\infty)$.
>
> - (a) Show that if $\Omega=\{\omega_1,\omega_2,\dots\}$ is any enumeration, then $\sum_{\omega\in\Omega}f(\omega)=\sum_{j=1}^{\infty}f(\omega_j)=\lim_{N\to\infty}\sum_{j=1}^{N}f(\omega_j)$, and deduce that the value does not depend on the enumeration.
> - (b) If $\Omega=\bigsqcup_{j\ge1}A_j$ is a partition into pairwise disjoint sets, show that $\sum_{\omega\in\Omega}f(\omega)=\sum_{j=1}^{\infty}\sum_{\omega\in A_j}f(\omega)$.
>
> Solution:
>
> - By definition, {@{$\sum_{\omega\in\Omega}f(\omega)$ is the supremum of finite subsums}@}.
> - (a) Because the terms are {@{nonnegative, every finite set of points is contained in some initial segment $\{\omega_1,\dots,\omega_N\}$}@}, so {@{every finite subsum is bounded above by $\sum_{j=1}^{N}f(\omega_j)$}@}, and therefore {@{$\sum_{\omega\in\Omega}f(\omega)\le\sum_{j\ge1}f(\omega_j)$}@}. Conversely, each {@{partial sum $\sum_{j=1}^{N}f(\omega_j)$ is itself one of the finite subsums appearing in the definition of $\sum_{\omega\in\Omega}f(\omega)$}@}, so {@{$\sum_{j=1}^{N}f(\omega_j)\le\sum_{\omega\in\Omega}f(\omega)$ for every $N$}@}; {@{letting $N\to\infty$ gives equality}@}, and {@{the value does not depend on the enumeration}@}.
> - (b) Partitioning {@{$\Omega$ into the disjoint pieces $A_j$ means that every point belongs to exactly one block, so any finite subsum can be regrouped uniquely as $\sum_{\omega\in F}f(\omega)=\sum_{j\ge1}\sum_{\omega\in A_j\cap F}f(\omega)$}@}, which immediately gives {@{$\sum_{\omega\in\Omega}f(\omega)\le\sum_{j\ge1}\sum_{\omega\in A_j}f(\omega)$}@}. {@{For the reverse direction, choose finite sets $F_j\subseteq A_j$ so that $\sum_{\omega\in A_j}f(\omega)-\sum_{\omega\in F_j}f(\omega)<\varepsilon/2^j$}@}; then {@{a finite union of these $F_j$<!-- LaTeX separator -->'s shows that the blockwise sum is at most $\sum_{\omega\in\Omega}f(\omega)+\varepsilon$}@}, and since {@{$\varepsilon>0$ is arbitrary}@}, {@{$\sum_{\omega\in\Omega}f(\omega)=\sum_{j\ge1}\sum_{\omega\in A_j}f(\omega)$}@}. <!--SR:!2026-05-15,14,290!2026-05-15,14,290!2026-05-16,15,290!2026-05-12,11,270!2026-05-11,10,270!2026-05-16,15,309!2026-05-18,17,309!2026-05-17,16,309!2026-05-18,17,309!2026-05-18,17,309!2026-05-12,11,289!2026-05-18,17,309!2026-05-16,15,309!2026-05-18,17,309-->

<!-- markdownlint MD028 -->

> Discrete distributions.
>
> - (a) Roll a fair die until the first $6$ appears; find the probability that more than $9$ rolls are needed.
> - (b) If each of $100$ chips is defective independently with probability $0.01$, compute the exact probability of at least $2$ defects and compare it with the Poisson approximation.
> - (c) Show that the hypergeometric pmf $H(N,M,n)$ converges to the binomial pmf $\mathrm{Bin}(n,p)$ when $N,M\to\infty$ with $M/N\to p$.
> - (d) If the number of penalty kicks in a match is $\mathrm{Pois}(\lambda)$ and each kick becomes a goal independently with probability $p$, determine the distribution of the number of penalty-kick goals.
>
> Solution:
>
> - (a) The waiting time for the first six is {@{geometric with success parameter $1/6$}@}, so {@{$P(T>9)=(5/6)^9\approx0.1938$}@}.
> - (b) The defect count is {@{$\mathrm{Bin}(100,0.01)$}@}, hence {@{$P(X\ge2)=1-0.99^{100}-100(0.01)0.99^{99}\approx0.2642$}@}; the Poisson approximation uses {@{$\lambda=np=1$}@}, giving {@{$P(Y\ge2)=1-e^{-1}-e^{-1}=1-2/e\approx0.2642$}@}, which matches to three decimal places.
> - (c) The intuitive point is that {@{sampling without replacement becomes almost the same as sampling with replacement when the population is huge and the sample size $n$ is fixed}@}. Start from the exact hypergeometric formula {@{$P(X=k)=\dfrac{\binom{M}{k}\binom{N-M}{n-k}}{\binom{N}{n}}$}@}. Rewrite it as {@{$\binom{n}{k}\dfrac{M(M-1)\cdots(M-k+1)\,(N-M)(N-M-1)\cdots(N-M-n+k+1)}{N(N-1)\cdots(N-n+1)}$}@}. For fixed {@{$n$ and $k$}@}, every success factor in the numerator divided by its denominator is close to {@{$M/N\to p$}@}, every failure factor is close to {@{$(N-M)/N\to1-p$}@}, and the finite denominator corrections tend to {@{$1$}@}. So the whole expression tends to {@{$\binom{n}{k}p^k(1-p)^{n-k}$}@}, which is exactly the {@{binomial pmf}@}.
> - (d) Condition first on the total number of kicks {@{$N=n$}@}. Then the number of goals given {@{$N=n$}@} is {@{$\mathrm{Bin}(n,p)$}@}, so {@{$P(G=k\mid N=n)=\binom{n}{k}p^k(1-p)^{n-k}$}@}. Averaging over the Poisson law gives {@{$P(G=k)=\sum_{n=k}^{\infty}\binom{n}{k}p^k(1-p)^{n-k}\dfrac{\lambda^n e^{-\lambda}}{n!}$}@}. Now pull out the factors that do not depend on {@{$n-k$}@}: {@{$P(G=k)=e^{-\lambda}\dfrac{(\lambda p)^k}{k!}\sum_{n=k}^{\infty}\dfrac{(\lambda(1-p))^{n-k}}{(n-k)!}$}@}. Reindex with {@{$m=n-k$}@} to obtain {@{$e^{-\lambda}\dfrac{(\lambda p)^k}{k!}\sum_{m=0}^{\infty}\dfrac{(\lambda(1-p))^{m}}{m!}=e^{-\lambda}\dfrac{(\lambda p)^k}{k!}e^{\lambda(1-p)}=e^{-\lambda p}\dfrac{(\lambda p)^k}{k!}$}@}. So thinning a Poisson count by keeping each event with probability {@{$p$}@} leaves another {@{Poisson law, now with mean $\lambda p$}@}. <!--SR:!2026-05-15,14,290!2026-05-16,15,290!2026-05-16,15,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-17,16,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-16,15,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-17,16,290!2026-05-17,16,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-16,15,290!2026-05-16,15,290!2026-05-15,14,290!2026-05-17,16,290!2026-05-16,15,290!2026-05-16,15,290!2026-05-17,16,290!2026-05-15,14,290!2026-05-15,14,290-->

<!-- markdownlint MD028 -->

> $n$-step simple random walk and the ballot theorem. Let $\Omega_n=\{(\omega_j)_{j=0}^{n}:\omega_0=0,\ |\omega_j-\omega_{j-1}|=1\}$ with the uniform law $P_0$, and let $A_k=\{\omega\in\Omega_n:\omega_n=k\}$.
>
> - (a) Compute $|\Omega_n|$ and explain its random-walk interpretation.
> - (b) Compute $P_0(A_k)$.
> - (c) If a motion passes by exactly $k\in\{1,\dots,n\}$ votes after $n$ ballots, compute the conditional probability that it stays strictly ahead throughout the count.
>
> Solution:
>
> - (a) Every path is determined by its sequence of $n$ increments in $\{-1,+1\}$, so there is a bijection between $\Omega_n$ and $\{-1,+1\}^n$; hence {@{$|\Omega_n|=2^n$}@}. This is exactly the path space of an {@{$n$-step simple random walk starting from $0$}@}.
> - (b) To end at $k$, the walk must have $(n+k)/2$ upward steps and $(n-k)/2$ downward steps, so parity matters: {@{$P_0(A_k)=0$ unless $n$ and $k$ have the same parity, and otherwise $P_0(A_k)=2^{-n}\binom{n}{(n+k)/2}$}@}.
> - (c) Translate the ballot count into a walk by letting {@{a vote for the motion contribute $+1$ and a vote against contribute $-1$}@}. Then ending ahead by {@{$k$ votes}@} means ending at height {@{$k$}@}, and staying strictly ahead means the walk never comes back to $0$ after it starts. So we want to count {@{paths from $(0,0)$ to $(n,k)$ that stay strictly above $0$ after time $0$}@}. First count all terminal-{@{$k$}@} paths: this is {@{$\binom{n}{(n+k)/2}$}@}, since we must choose which of the {@{$n$ steps are upward}@}. Now count the good paths. Such a path must begin with an up-step, so deleting that first step reduces the problem to counting paths from {@{$(0,0)$ to $(n-1,k-1)$}@}; there are {@{$\binom{n-1}{(n+k-2)/2}$}@} of them. Among these, the bad paths are exactly those that hit {@{$-1$}@} somewhere. By the {@{reflection principle}@}, reflecting the path up to its first hit of {@{$-1$}@} gives a bijection with all paths from {@{$(0,0)$ to $(n-1,-k-1)$}@}, whose number is {@{$\binom{n-1}{(n-k-2)/2}$}@}. Therefore the number of good paths is {@{$\binom{n-1}{(n+k-2)/2}-\binom{n-1}{(n-k-2)/2}$}@}. Finally, divide by the total number of terminal-{@{$k$}@} paths and use the elementary binomial identity {@{$\binom{n-1}{(n+k-2)/2}-\binom{n-1}{(n-k-2)/2}=\dfrac{k}{n}\binom{n}{(n+k)/2}$}@}. This yields the ballot-theorem probability {@{$P_0(\omega_j>0\ \forall j\mid A_k)=k/n$}@}. <!--SR:!2026-05-15,14,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-16,15,290!2026-05-15,14,290!2026-05-16,15,290!2026-05-16,15,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-16,15,290!2026-05-15,14,290!2026-05-17,16,290!2026-05-16,15,290!2026-05-15,14,290!2026-05-17,16,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-17,16,290!2026-05-15,14,290!2026-05-11,10,270!2026-05-15,14,290-->
