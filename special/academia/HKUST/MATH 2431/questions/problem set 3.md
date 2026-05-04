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
> - (a) Fix your {@{original choice as $D_1$}@}. There are {@{three equally likely car locations}@}. If {@{the car is behind $D_1$, switching loses}@}; if {@{the car is behind $D_2$ or $D_3$}@}, the host is {@{forced to open the only other goat door, so switching wins}@}. Therefore {@{the switch strategy wins exactly when the initial choice was wrong, so its winning probability is $2/3$}@}. Hence {@{switching is optimal in the standard Monty Hall setting}@}.
> - (b) Keep the same setup: you pick {@{$D_1$, Bill is behind $D_2$, Nan behind $D_3$}@}, and you are told {@{Bill was shown}@}. If {@{the car is behind $D_1$, Bill is shown with probability $b$}@}; if {@{the car is behind $D_3$, Bill is shown with probability $1$ (host has no choice)}@}; car behind {@{$D_2$ is impossible because Bill is a goat}@}. Therefore by Bayes, {@{$P(D_3=\text{car}\mid D_2=\text{Bill})=\dfrac{(1/3)\cdot1}{(1/3)\cdot b+(1/3)\cdot1}=\dfrac{1}{b+1}$}@}. Since switching {@{wins exactly when the car is behind $D_3$}@}, the switching {@{success probability after observing Bill is $1/(b+1)$}@}, so host {@{preference changes the posterior odds}@}.
> - (c) Now the host opens {@{one of the two unchosen doors uniformly at random}@}, and it {@{happens to reveal a goat}@}. Condition {@{on this event}@}. If the car is {@{behind your original door, the event occurs with probability $1$}@}; if the car is {@{behind either other door}@}, the event occurs with {@{probability $1/2$ because the host might reveal the car instead}@}. Hence {@{posterior weights are proportional to $1/3,1/6,1/6$}@}, so after {@{normalization, staying has probability $1/2$ and switching has probability $1/2$}@}. Therefore {@{switching and staying are equally good in the random-host variant}@}. <!--SR:!2026-05-17,16,290!2026-05-16,15,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-17,16,290!2026-05-16,15,290!2026-05-17,16,290!2026-05-17,16,290!2026-05-15,14,290!2026-05-17,16,290!2026-05-16,15,290!2026-05-17,16,290!2026-05-16,15,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-16,15,290!2026-05-17,16,290!2026-05-15,14,290!2026-05-17,16,290!2026-05-17,16,290!2026-05-15,14,290!2026-05-17,16,290!2026-05-15,14,290!2026-05-17,16,290-->

<!-- markdownlint MD028 -->

> Countable sums. Let $\Omega$ be a countable set and let $f\colon\Omega\to[0,\infty)$.
>
> - (a) Show that if $\Omega=\{\omega_1,\omega_2,\dots\}$ is any enumeration, then $\sum_{\omega\in\Omega}f(\omega)=\sum_{j=1}^{\infty}f(\omega_j)=\lim_{N\to\infty}\sum_{j=1}^{N}f(\omega_j)$, and deduce that the value does not depend on the enumeration.
> - (b) If $\Omega=\bigsqcup_{j\ge1}A_j$ is a partition into pairwise disjoint sets, show that $\sum_{\omega\in\Omega}f(\omega)=\sum_{j=1}^{\infty}\sum_{\omega\in A_j}f(\omega)$.
>
> Solution:
>
> - By definition, {@{$\sum_{\omega\in\Omega}f(\omega)$}@} is {@{the supremum of finite subsums}@}.
> - (a) Let {@{$S:=\sup\{\sum_{\omega\in F}f(\omega):F\subset\Omega,\ F\text{ finite}\}$}@} and for the enumeration define {@{$s_N:=\sum_{j=1}^N f(\omega_j)$}@}. Because {@{$f\ge0$, the sequence $(s_N)$ is increasing}@}, so {@{$\lim_{N\to\infty}s_N=\sup_N s_N$}@}. For any {@{finite set $F\subset\Omega$, choose $N(F):=\max\{j:\omega_j\in F\}$}@}; then {@{$\sum_{\omega\in F}f(\omega)\le\sum_{j=1}^{N(F)}f(\omega_j)\le\lim_{N\to\infty}s_N$}@}, so $S\le\lim_{N\to\infty}s_N$.
>
>   Conversely, each {@{partial sum $s_N$ is itself a finite subsum}@}, hence {@{$s_N\le S$ for every $N$, so $\lim_{N\to\infty}s_N\le S$}@}. Therefore {@{$\sum_{\omega\in\Omega}f(\omega)=S=\sum_{j=1}^{\infty}f(\omega_j)=\lim_{N\to\infty}\sum_{j=1}^{N}f(\omega_j)$}@}. Applying {@{the same argument to any other enumeration}@} shows {@{the countable sum does not depend on ordering}@} because both {@{series equal the same supremum over finite subsums}@}.
>
>   {@{The proof pattern intuition}@} is that, given we have {@{two different expressions to be proven equal}@}, we can show {@{each is bounded above by the other}@}, which implies {@{they are equal}@}. For each direction, {@{the lesser expression}@} is {@{a supremum over a smaller family of finite subsums}@}. Proving that every {@{finite subsum in the lesser family is bounded by the greater expression}@} implies {@{the supremum over the lesser family is bounded by the greater expression}@}, and then {@{reversing the roles of the two expressions gives the opposite inequality}@}. In particular case, {@{the definitions of the countable sum and the limit of partial sums}@} are already both {@{suprema over finite subsums}@}.
> - (b) Write {@{$S:=\sum_{\omega\in\Omega}f(\omega)$ and $S_j:=\sum_{\omega\in A_j}f(\omega)$}@}. First prove {@{$\sum_{j\ge1}S_j\le S$}@}: for fixed {@{$m$, choose finite $E_j\subset A_j$ ($1\le j\le m$)}@}. Since {@{the blocks are disjoint}@}, {@{$\sum_{j=1}^m\sum_{\omega\in E_j}f(\omega)=\sum_{\omega\in\cup_{j=1}^mE_j}f(\omega)\le S$}@}. Taking {@{suprema over $E_j$}@} gives {@{$\sum_{j=1}^m S_j\le S$}@}, and then {@{$m\to\infty$ yields $\sum_{j\ge1}S_j\le S$}@}
>
>   For the reverse inequality, let {@{$F\subset\Omega$ be finite and set $F_j:=F\cap A_j$}@}; then {@{$\sum_{\omega\in F}f(\omega)=\sum_{j\ge1}\sum_{\omega\in F_j}f(\omega)\le\sum_{j\ge1}S_j$}@}. Taking {@{supremum over finite $F$}@} gives {@{$S\le\sum_{j\ge1}S_j$}@}. Combining {@{both directions}@}, {@{$\sum_{\omega\in\Omega}f(\omega)=\sum_{j=1}^{\infty}\sum_{\omega\in A_j}f(\omega)$}@}. 
>
>   {@{The proof pattern intuition}@} is {@{the same as the previous subpart}@}. In this particular case, {@{the suprema are less straightforward}@}. In the first direction, we need to take {@{two nested suprema}@}: one over {@{the finite subsets of each block $A_j$ and one over the number of blocks $m$ to be included}@}. In the second direction, we need to take {@{a single supremum over finite subsets of $\Omega$}@}, but we need to additionally {@{decompose each finite subset into its intersections with the blocks $A_j$}@}. <!--SR:!2026-05-15,14,290!2026-05-15,14,290!2026-05-16,15,290!2026-05-12,11,270!2026-05-11,10,270!2026-05-16,15,309!2026-05-18,17,309!2026-05-17,16,309!2026-05-18,17,309!2026-05-18,17,309!2026-05-12,11,289!2026-05-18,17,309!2026-05-16,15,309!2026-05-18,17,309!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311-->

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
> - (a) {@{The waiting time for the first six}@} is {@{geometric with success probability $1/6$}@}, so {@{$P(T>9)=(1-1/6)^9=(5/6)^9\approx0.1938$}@}. In words, this is the probability of {@{nine consecutive non-six outcomes before the first six appears}@}.
> - (b) The defect count is {@{$\mathrm{Bin}(100,0.01)$, so $P(X\ge2)=1-0.99^{100}-100(0.01)0.99^{99}\approx0.2642$}@}. For comparison, {@{the Poisson approximation}@} uses {@{rate $\lambda=np=1$, giving $P(Y\ge2)=1-2/e\approx0.2642$}@}, so the two values {@{agree to three decimals}@}.
> - (c) Start from the exact hypergeometric probability {@{$P(X=k)=\dfrac{\binom{M}{k}\binom{N-M}{n-k}}{\binom{N}{n}}$}@}. Rewrite it as {@{$\binom{n}{k}\dfrac{M(M-1)\cdots(M-k+1)\,(N-M)(N-M-1)\cdots(N-M-n+k+1)}{N(N-1)\cdots(N-n+1)}$}@}. For fixed {@{$n,k$ and $N,M\to\infty$ with $M/N\to p$}@}, each {@{success ratio tends to $p$, each failure ratio tends to $1-p$}@}, and finite {@{denominator corrections tend to $1$}@}. Hence {@{$P(X=k)\to\binom{n}{k}p^k(1-p)^{n-k}$}@}, i.e. {@{the hypergeometric pmf converges to the binomial pmf when sampling fraction is negligible}@}.
> - (d) Condition on {@{the total kicks}@}. Given {@{$N=n$, goals follow a binomial law}@}, so {@{$P(G=k\mid N=n)=\binom{n}{k}p^k(1-p)^{n-k}$}@} and therefore {@{$P(G=k)=\sum_{n=k}^{\infty}\binom{n}{k}p^k(1-p)^{n-k}\dfrac{\lambda^n e^{-\lambda}}{n!}$}@}. Pull out {@{factors independent of $n-k$ and reindex by $m=n-k$}@} to get {@{$P(G=k)=e^{-\lambda}\dfrac{(\lambda p)^k}{k!}\sum_{m=0}^{\infty}\dfrac{(\lambda(1-p))^m}{m!}=e^{-\lambda p}\dfrac{(\lambda p)^k}{k!}$}@}. So {@{Poisson thinning}@} keeps {@{a Poisson distribution and scales the mean from $\lambda$ to $\lambda p$}@}. <!--SR:!2026-05-15,14,290!2026-05-16,15,290!2026-05-16,15,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-17,16,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-16,15,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-17,16,290!2026-05-17,16,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-16,15,290!2026-05-16,15,290!2026-05-15,14,290!2026-05-17,16,290!2026-05-16,15,290!2026-05-16,15,290-->

<!-- markdownlint MD028 -->

> $n$-step simple random walk and the ballot theorem. Let $\Omega_n=\{(\omega_j)_{j=0}^{n}:\omega_0=0,\ |\omega_j-\omega_{j-1}|=1\}$ with the uniform law $P_0$, and let $A_k=\{\omega\in\Omega_n:\omega_n=k\}$.
>
> - (a) Compute $|\Omega_n|$ and explain its random-walk interpretation.
> - (b) Compute $P_0(A_k)$.
> - (c) If a motion passes by exactly $k\in\{1,\dots,n\}$ votes after $n$ ballots, compute the conditional probability that it stays strictly ahead throughout the count.
>
> Solution:
>
> - (a) Every path is determined by {@{its $n$ increments in $\{-1,+1\}$}@}, so there is {@{a bijection between $\Omega_n$ and $\{-1,+1\}^n$}@}. Hence {@{$|\Omega_n|=2^n$, meaning one path for each length-$n$ increment sequence of a simple random walk starting at $0$}@}.
> - (b) To {@{end at level $k$}@}, the walk must have {@{$(n+k)/2$ up-steps and $(n-k)/2$ down-steps}@}, so {@{parity is necessary}@}. Therefore {@{$P_0(A_k)=0$ if $n$ and $k$ have different parity, and otherwise $P_0(A_k)=2^{-n}\binom{n}{(n+k)/2}$}@}.
> - (c) Encode each {@{ballot as $+1$ (motion) or $-1$ (against)}@}. Then ending {@{ahead by $k$ votes is the endpoint condition $\omega_n=k$}@}, and staying {@{strictly ahead means $\omega_j>0$ for all $j\ge1$}@}. {@{Total terminal-$k$ paths}@} are {@{$\binom{n}{(n+k)/2}$}@}. For {@{good paths}@}, delete {@{the first forced up-step, giving paths from $(0,0)$ to $(n-1,k-1)$}@}, so there are {@{$\binom{n-1}{(n+k-2)/2}$}@}. {@{Bad paths among these}@} are {@{exactly those that hit $-1$}@}; by {@{reflection at the first hit, these correspond bijectively to paths from $(0,0)$ to $(n-1,-k-1)$}@}, counted by {@{$\binom{n-1}{(n-k-2)/2}$}@}. Hence good paths equal {@{$\binom{n-1}{(n+k-2)/2}-\binom{n-1}{(n-k-2)/2}$}@}, and dividing by {@{total terminal-$k$ paths}@} gives {@{$P_0(\omega_j>0\ \forall j\mid A_k)=k/n$}@}. In words, {@{the ballot theorem}@} says {@{the conditional chance of always leading equals the final margin ratio $k/n$}@}. <!--SR:!2026-05-15,14,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-16,15,290!2026-05-15,14,290!2026-05-16,15,290!2026-05-16,15,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-16,15,290!2026-05-15,14,290!2026-05-17,16,290!2026-05-16,15,290!2026-05-15,14,290!2026-05-17,16,290!2026-05-15,14,290!2026-05-15,14,290!2026-05-17,16,290!2026-05-15,14,290!2026-05-11,10,270!2026-05-15,14,290!2026-05-08,4,311!2026-05-08,4,311!2026-05-08,4,311-->
