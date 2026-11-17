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

> 1.a. The Monty Hall problem. In the standard three-door game show, if the host always opens a different door with a goat behind it, should you switch?
>
> ---
>
> - solution: {@{Yes, switching wins with probability $2/3$ and is optimal}@}
> - explanation: Fix {@{the original choice as $D_1$}@}, so there are {@{three equally likely car locations}@}. <br/>
>     If {@{the car is behind $D_1$}@} then {@{switching loses}@}, while if {@{the car is behind $D_2$ or $D_3$}@} the host is {@{forced to open the only other goat door, so switching wins}@}. <br/>
>     The switch strategy therefore wins exactly when {@{the initial choice was wrong}@}, which gives {@{the winning probability $2/3$}@}, so {@{switching is optimal in the standard game}@}.

<!-- markdownlint MD028 -->

> 1.b. The Monty Hall problem. In the standard three-door game show, the two goats are named Bill and Nan, and whenever the host has a choice the host shows Bill with probability $b$. What is the winning probability of the switching strategy after Bill is shown?
>
> ---
>
> - solution: {@{The switching strategy wins with probability $1/(b+1)$}@}
> - explanation: Keep the setup with {@{the original pick $D_1$, Bill behind $D_2$, and Nan behind $D_3$}@}, and suppose {@{Bill was shown}@}. <br/>
>     If {@{the car is behind $D_1$}@} then {@{Bill is shown with probability $b$}@}, and if {@{the car is behind $D_3$}@} then {@{Bill is shown with probability $1$, since the host has no choice}@}; the car cannot be {@{behind $D_2$, because Bill is a goat}@}. <br/>
>     Bayes therefore gives {@{the posterior $P(D_3=\text{car}\mid D_2=\text{Bill})=\dfrac{(1/3)\cdot1}{(1/3)\cdot b+(1/3)\cdot1}=\dfrac{1}{b+1}$}@}. <br/>
>     Switching {@{wins exactly when the car is behind $D_3$}@}, so it succeeds with {@{probability $1/(b+1)$ after Bill is shown}@}, and {@{the host's preference changes the posterior odds}@}.

<!-- markdownlint MD028 -->

> 1.c. The Monty Hall problem. In the standard three-door game show, the host instead opens one of the other doors uniformly at random and it happens to reveal a goat. What is the best strategy?
>
> ---
>
> - solution: {@{Switching and staying are equally good, each winning with probability $1/2$}@}
> - explanation: Now the host opens {@{one of the two unchosen doors uniformly at random}@} and it {@{happens to reveal a goat}@}, so the analysis conditions {@{on that event}@}. <br/>
>     If the car is {@{behind the original door}@} the event occurs with {@{probability $1$}@}, while if the car is {@{behind either other door}@} it occurs with {@{probability $1/2$, because the host might reveal the car instead}@}. <br/>
>     The posterior weights are therefore proportional to {@{the three weights $1/3$, $1/6$, and $1/6$}@}, so after {@{normalizing, staying has probability $1/2$ and switching has probability $1/2$}@}. <br/>
>     Hence {@{switching and staying are equally good in the random-host variant}@}.

<!-- markdownlint MD028 -->

> 2.a. Countable sums. Let $\Omega$ be a countable set and let $f\colon\Omega\to[0,\infty)$. Show that if $\Omega=\{\omega_1,\omega_2,\dots\}$ is any enumeration, then $\sum_{\omega\in\Omega}f(\omega)=\sum_{j=1}^{\infty}f(\omega_j)=\lim_{N\to\infty}\sum_{j=1}^{N}f(\omega_j)$, and deduce that the value does not depend on the enumeration.
>
> ---
>
> - solution: {@{The sum equals the limit of partial sums along any enumeration, and the value does not depend on the enumeration}@}
> - explanation: By definition, {@{$\sum_{\omega\in\Omega}f(\omega)$ is the supremum of finite subsums}@}. <br/>
>     Write {@{the sum $S:=\sup\{\sum_{\omega\in F}f(\omega):F\subset\Omega,\ F\text{ finite}\}$}@} and, for the enumeration, {@{the partial sum $s_N:=\sum_{j=1}^N f(\omega_j)$}@}. <br/>
>     Because {@{the summands satisfy $f\ge0$}@}, the sequence $(s_N)$ is {@{increasing}@}, so {@{its limit is $\lim_{N\to\infty}s_N=\sup_N s_N$}@}. <br/>
>     For any {@{finite set $F\subset\Omega$}@}, choosing {@{the index $N(F):=\max\{j:\omega_j\in F\}$}@} gives {@{the bound $\sum_{\omega\in F}f(\omega)\le\sum_{j=1}^{N(F)}f(\omega_j)\le\lim_{N\to\infty}s_N$}@}, hence {@{the inequality $S\le\lim_{N\to\infty}s_N$}@}. <br/>
>     Conversely, each {@{partial sum $s_N$ is itself a finite subsum}@}, hence {@{$s_N\le S$ for every $N$, so $\lim_{N\to\infty}s_N\le S$}@}. <br/>
>     Therefore {@{the three expressions agree, $\sum_{\omega\in\Omega}f(\omega)=S=\sum_{j=1}^{\infty}f(\omega_j)=\lim_{N\to\infty}\sum_{j=1}^{N}f(\omega_j)$}@}. <br/>
>     Applying {@{the same argument to any other enumeration}@} shows {@{the countable sum does not depend on ordering}@}, because {@{both series equal the same supremum over finite subsums}@}. <br/>
>     The proof pattern is that, given {@{two expressions to be proven equal}@}, one shows {@{each is bounded above by the other}@}, which implies {@{they are equal}@}. <br/>
>     For each direction, {@{the lesser expression}@} is {@{a supremum over a smaller family of finite subsums}@}. <br/>
>     Proving that every {@{finite subsum in the lesser family is bounded by the greater expression}@} implies {@{the supremum over the lesser family is bounded by the greater expression}@}, and then {@{reversing the roles of the two expressions gives the opposite inequality}@}. <br/>
>     In this case, {@{the definitions of the countable sum and of the limit of partial sums}@} are already both {@{suprema over finite subsums}@}.

<!-- markdownlint MD028 -->

> 2.b. Countable sums. Let $\Omega$ be a countable set and let $f\colon\Omega\to[0,\infty)$. If $\Omega=\bigsqcup_{j\ge1}A_j$ is a partition into pairwise disjoint sets, show that $\sum_{\omega\in\Omega}f(\omega)=\sum_{j=1}^{\infty}\sum_{\omega\in A_j}f(\omega)$.
>
> ---
>
> - solution: {@{The sum over $\Omega$ equals the double sum over the blocks, $\sum_{\omega\in\Omega}f(\omega)=\sum_{j=1}^{\infty}\sum_{\omega\in A_j}f(\omega)$}@}
> - explanation: By definition, {@{$\sum_{\omega\in\Omega}f(\omega)$ is the supremum of finite subsums}@}. <br/>
>     Write {@{the sum $S:=\sum_{\omega\in\Omega}f(\omega)$ and the block sums $S_j:=\sum_{\omega\in A_j}f(\omega)$}@}. <br/>
>     First prove {@{the inequality $\sum_{j\ge1}S_j\le S$}@}: for fixed {@{$m$, choose finite $E_j\subset A_j$ for $1\le j\le m$}@}. <br/>
>     Since {@{the blocks are disjoint}@}, {@{the identity $\sum_{j=1}^m\sum_{\omega\in E_j}f(\omega)=\sum_{\omega\in\cup_{j=1}^mE_j}f(\omega)\le S$}@}. <br/>
>     Taking {@{suprema over $E_j$}@} gives {@{the bound $\sum_{j=1}^m S_j\le S$}@}, and then {@{$m\to\infty$ yields $\sum_{j\ge1}S_j\le S$}@}. <br/>
>     For the reverse inequality, let {@{$F\subset\Omega$ be finite and set $F_j:=F\cap A_j$}@}; then {@{the identity $\sum_{\omega\in F}f(\omega)=\sum_{j\ge1}\sum_{\omega\in F_j}f(\omega)\le\sum_{j\ge1}S_j$}@}. <br/>
>     Taking {@{the supremum over finite $F$}@} gives {@{the bound $S\le\sum_{j\ge1}S_j$}@}, and combining {@{both directions}@} yields {@{the identity $\sum_{\omega\in\Omega}f(\omega)=\sum_{j=1}^{\infty}\sum_{\omega\in A_j}f(\omega)$}@}. <br/>
>     The proof pattern is {@{the same as the previous subpart}@}, although here {@{the suprema are less straightforward}@}. <br/>
>     The first direction needs {@{two nested suprema}@}: one over {@{the finite subsets of each block $A_j$ and one over the number of blocks $m$ to be included}@}. <br/>
>     The second direction needs {@{a single supremum over finite subsets of $\Omega$}@}, but it must additionally {@{decompose each finite subset into its intersections with the blocks $A_j$}@}. <!--SR:!fsrs,2027-04-10T00:00:00.000Z,274,274.1280869,1,2,7,0,0,2026-07-10T00:00:00.000Z!fsrs,2027-04-26T00:00:00.000Z,287,287.11697064,1,2,7,0,0,2026-07-13T00:00:00.000Z!fsrs,2027-05-23T00:00:00.000Z,309,308.57643926,1,2,7,0,0,2026-07-18T00:00:00.000Z!fsrs,2027-01-08T00:00:00.000Z,200,199.69543576,1.98030797,2,6,0,0,2026-06-22T00:00:00.000Z!fsrs,2026-12-22T00:00:00.000Z,187,187.15626924,1.98030797,2,6,0,0,2026-06-18T00:00:00.000Z!fsrs,2027-07-12T00:00:00.000Z,354,353.98120439,1,2,7,0,0,2026-07-23T00:00:00.000Z!fsrs,2027-09-16T00:00:00.000Z,394,394.37099029,1,2,7,0,0,2026-08-18T00:00:00.000Z!fsrs,2027-08-04T00:00:00.000Z,372,372.01284157,1,2,7,0,0,2026-07-28T00:00:00.000Z!fsrs,2027-09-05T00:00:00.000Z,385,385.45102701,1,2,7,0,0,2026-08-16T00:00:00.000Z!fsrs,2027-09-16T00:00:00.000Z,394,394.37099029,1,2,7,0,0,2026-08-18T00:00:00.000Z!fsrs,2027-02-21T00:00:00.000Z,238,238.09221327,1.02972367,2,7,0,0,2026-06-28T00:00:00.000Z!fsrs,2027-08-26T00:00:00.000Z,377,376.50017085,1,2,7,0,0,2026-08-14T00:00:00.000Z!fsrs,2027-07-06T00:00:00.000Z,349,349.45203011,1,2,7,0,0,2026-07-22T00:00:00.000Z!fsrs,2027-08-31T00:00:00.000Z,381,380.97951917,1,2,7,0,0,2026-08-15T00:00:00.000Z!fsrs,2027-11-10T00:00:00.000Z,445,444.50018208,1,2,7,0,0,2026-08-22T00:00:00.000Z!fsrs,2027-09-18T00:00:00.000Z,401,401.35825892,1,2,7,0,0,2026-08-13T00:00:00.000Z!fsrs,2027-11-15T00:00:00.000Z,449,449.25344976,1,2,7,0,0,2026-08-23T00:00:00.000Z!fsrs,2027-12-02T00:00:00.000Z,463,463.46776757,1,2,7,0,0,2026-08-26T00:00:00.000Z!fsrs,2027-09-30T00:00:00.000Z,411,411.0041104,1,2,7,0,0,2026-08-15T00:00:00.000Z!fsrs,2027-12-02T00:00:00.000Z,463,463.46776757,1,2,7,0,0,2026-08-26T00:00:00.000Z!fsrs,2027-11-21T00:00:00.000Z,454,453.99902328,1,2,7,0,0,2026-08-24T00:00:00.000Z!fsrs,2027-12-08T00:00:00.000Z,468,468.19113519,1,2,7,0,0,2026-08-27T00:00:00.000Z!fsrs,2027-11-15T00:00:00.000Z,449,449.25344976,1,2,7,0,0,2026-08-23T00:00:00.000Z!fsrs,2027-10-17T00:00:00.000Z,425,425.40863484,1,2,7,0,0,2026-08-18T00:00:00.000Z!fsrs,2027-11-10T00:00:00.000Z,445,444.50018208,1,2,7,0,0,2026-08-22T00:00:00.000Z!fsrs,2027-11-15T00:00:00.000Z,449,449.25344976,1,2,7,0,0,2026-08-23T00:00:00.000Z!fsrs,2027-11-10T00:00:00.000Z,445,444.50018208,1,2,7,0,0,2026-08-22T00:00:00.000Z!fsrs,2027-10-06T00:00:00.000Z,416,415.8140518,1,2,7,0,0,2026-08-16T00:00:00.000Z!fsrs,2027-12-08T00:00:00.000Z,468,468.19113519,1,2,7,0,0,2026-08-27T00:00:00.000Z!fsrs,2027-09-13T00:00:00.000Z,397,396.52206787,1,2,7,0,0,2026-08-12T00:00:00.000Z!fsrs,2027-12-08T00:00:00.000Z,468,468.19113519,1,2,7,0,0,2026-08-27T00:00:00.000Z!fsrs,2027-11-10T00:00:00.000Z,445,444.50018208,1,2,7,0,0,2026-08-22T00:00:00.000Z!fsrs,2027-11-27T00:00:00.000Z,459,458.73712151,1,2,7,0,0,2026-08-25T00:00:00.000Z!fsrs,2027-09-24T00:00:00.000Z,406,406.18556417,1,2,7,0,0,2026-08-14T00:00:00.000Z!fsrs,2027-11-10T00:00:00.000Z,445,444.50018208,1,2,7,0,0,2026-08-22T00:00:00.000Z!fsrs,2027-11-27T00:00:00.000Z,459,458.73712151,1,2,7,0,0,2026-08-25T00:00:00.000Z!fsrs,2027-12-02T00:00:00.000Z,463,463.46776757,1,2,7,0,0,2026-08-26T00:00:00.000Z!fsrs,2027-11-21T00:00:00.000Z,454,453.99902328,1,2,7,0,0,2026-08-24T00:00:00.000Z!fsrs,2027-12-08T00:00:00.000Z,468,468.19113519,1,2,7,0,0,2026-08-27T00:00:00.000Z!fsrs,2027-11-15T00:00:00.000Z,449,449.25344976,1,2,7,0,0,2026-08-23T00:00:00.000Z!fsrs,2027-09-24T00:00:00.000Z,406,406.18556417,1,2,7,0,0,2026-08-14T00:00:00.000Z!fsrs,2027-09-13T00:00:00.000Z,397,396.52206787,1,2,7,0,0,2026-08-12T00:00:00.000Z!fsrs,2027-10-12T00:00:00.000Z,421,420.6155009,1,2,7,0,0,2026-08-17T00:00:00.000Z!fsrs,2027-10-12T00:00:00.000Z,421,420.6155009,1,2,7,0,0,2026-08-17T00:00:00.000Z!fsrs,2027-09-13T00:00:00.000Z,397,396.52206787,1,2,7,0,0,2026-08-12T00:00:00.000Z!fsrs,2027-12-08T00:00:00.000Z,468,468.19113519,1,2,7,0,0,2026-08-27T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> 3.a. Discrete distributions. Roll a fair die until the first $6$ appears; find the probability that more than $9$ rolls are needed.
>
> ---
>
> - solution: {@{The probability is $P(T>9)=(5/6)^9\approx0.1938$}@}
> - explanation: {@{The waiting time for the first six}@} is {@{geometric with success probability $1/6$}@}, so {@{the answer is $P(T>9)=(1-1/6)^9=(5/6)^9\approx0.1938$}@}. <br/>
>     In words, this is the probability of {@{nine consecutive non-six outcomes before the first six appears}@}.

<!-- markdownlint MD028 -->

> 3.b. Discrete distributions. Each of $100$ chips is defective independently with probability $0.01$. Compute the exact probability of at least $2$ defects and compare it with the Poisson approximation.
>
> ---
>
> - solution: {@{The exact probability is $P(X\ge2)=1-0.99^{100}-100(0.01)0.99^{99}\approx0.2642$, which the Poisson approximation matches}@}
> - explanation: The defect count is {@{the binomial law $\mathrm{Bin}(100,0.01)$, so $P(X\ge2)=1-0.99^{100}-100(0.01)0.99^{99}\approx0.2642$}@}. <br/>
>     For comparison, {@{the Poisson approximation}@} uses {@{the rate $\lambda=np=1$, giving $P(Y\ge2)=1-2/e\approx0.2642$}@}, so the two values {@{agree to three decimals}@}.

<!-- markdownlint MD028 -->

> 3.c. Discrete distributions. Show that the hypergeometric pmf $H(N,M,n)$ converges to the binomial pmf $\mathrm{Bin}(n,p)$ when $N,M\to\infty$ with $M/N\to p$.
>
> ---
>
> - solution: {@{The hypergeometric pmf converges to the binomial pmf once the sampling fraction is negligible}@}
> - explanation: Start from {@{the exact probability $P(X=k)=\dfrac{\binom{M}{k}\binom{N-M}{n-k}}{\binom{N}{n}}$}@}, and rewrite it as {@{the ratio $\binom{n}{k}\dfrac{M(M-1)\cdots(M-k+1)\,(N-M)(N-M-1)\cdots(N-M-n+k+1)}{N(N-1)\cdots(N-n+1)}$}@}. <br/>
>     For fixed {@{$n,k$ and $N,M\to\infty$ with $M/N\to p$}@}, each {@{success ratio tends to $p$, each failure ratio tends to $1-p$}@}, and finite {@{denominator corrections tend to $1$}@}. <br/>
>     Hence {@{the limit $P(X=k)\to\binom{n}{k}p^k(1-p)^{n-k}$}@}, so {@{the hypergeometric pmf converges to the binomial pmf when the sampling fraction is negligible}@}.

<!-- markdownlint MD028 -->

> 3.d. Discrete distributions. The number of penalty kicks in a match is $\mathrm{Pois}(\lambda)$ and each kick becomes a goal independently with probability $p$. Determine the distribution of the number of penalty-kick goals.
>
> ---
>
> - solution: {@{The goal count is itself Poisson, with parameter $\lambda p$}@}
> - explanation: Condition on {@{the total number of kicks}@}. <br/>
>     Given {@{the count $N=n$}@}, the goals follow {@{a binomial law}@}, so {@{the goal probability is $P(G=k\mid N=n)=\binom{n}{k}p^k(1-p)^{n-k}$}@} and therefore {@{the marginal is $P(G=k)=\sum_{n=k}^{\infty}\binom{n}{k}p^k(1-p)^{n-k}\dfrac{\lambda^n e^{-\lambda}}{n!}$}@}. <br/>
>     Pulling out {@{the factors independent of $n-k$ and reindexing by $m=n-k$}@} gives {@{the value $P(G=k)=e^{-\lambda}\dfrac{(\lambda p)^k}{k!}\sum_{m=0}^{\infty}\dfrac{(\lambda(1-p))^m}{m!}=e^{-\lambda p}\dfrac{(\lambda p)^k}{k!}$}@}. <br/> <!--SR:!fsrs,2027-04-21T00:00:00.000Z,283,282.79716409,1,2,7,0,0,2026-07-12T00:00:00.000Z!fsrs,2027-05-07T00:00:00.000Z,296,295.72812302,1,2,7,0,0,2026-07-15T00:00:00.000Z!fsrs,2027-05-28T00:00:00.000Z,313,312.84164192,1,2,7,0,0,2026-07-19T00:00:00.000Z!fsrs,2027-04-10T00:00:00.000Z,274,274.1280869,1,2,7,0,0,2026-07-10T00:00:00.000Z!fsrs,2027-04-21T00:00:00.000Z,283,282.79716409,1,2,7,0,0,2026-07-12T00:00:00.000Z!fsrs,2027-05-29T00:00:00.000Z,313,312.84164192,1,2,7,0,0,2026-07-20T00:00:00.000Z!fsrs,2027-05-01T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-14T00:00:00.000Z!fsrs,2027-04-21T00:00:00.000Z,283,282.79716409,1,2,7,0,0,2026-07-12T00:00:00.000Z!fsrs,2027-05-17T00:00:00.000Z,304,304.30256839,1,2,7,0,0,2026-07-17T00:00:00.000Z!fsrs,2027-04-15T00:00:00.000Z,278,278.46760619,1,2,7,0,0,2026-07-11T00:00:00.000Z!fsrs,2027-04-15T00:00:00.000Z,278,278.46760619,1,2,7,0,0,2026-07-11T00:00:00.000Z!fsrs,2027-05-01T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-14T00:00:00.000Z!fsrs,2027-05-01T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-14T00:00:00.000Z!fsrs,2027-06-03T00:00:00.000Z,317,317.09832588,1,2,7,0,0,2026-07-21T00:00:00.000Z!fsrs,2027-06-03T00:00:00.000Z,317,317.09832588,1,2,7,0,0,2026-07-21T00:00:00.000Z!fsrs,2027-05-01T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-14T00:00:00.000Z!fsrs,2027-04-15T00:00:00.000Z,278,278.46760619,1,2,7,0,0,2026-07-11T00:00:00.000Z!fsrs,2027-05-28T00:00:00.000Z,313,312.84164192,1,2,7,0,0,2026-07-19T00:00:00.000Z!fsrs,2027-05-12T00:00:00.000Z,300,300.01984473,1,2,7,0,0,2026-07-16T00:00:00.000Z!fsrs,2027-05-01T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-14T00:00:00.000Z!fsrs,2027-06-03T00:00:00.000Z,317,317.09832588,1,2,7,0,0,2026-07-21T00:00:00.000Z!fsrs,2027-05-23T00:00:00.000Z,309,308.57643926,1,2,7,0,0,2026-07-18T00:00:00.000Z!fsrs,2027-05-12T00:00:00.000Z,300,300.01984473,1,2,7,0,0,2026-07-16T00:00:00.000Z-->
>     So {@{Poisson thinning}@} keeps {@{a Poisson distribution and scales the mean from $\lambda$ to $\lambda p$}@}.

<!-- markdownlint MD028 -->

> 4.a. $n$-step simple random walk and the ballot theorem. Let $\Omega_n=\{(\omega_j)_{j=0}^{n}:\omega_0=0,\ |\omega_j-\omega_{j-1}|=1\}$ with the uniform law $P_0$, and let $A_k=\{\omega\in\Omega_n:\omega_n=k\}$. Compute $|\Omega_n|$ and explain its random-walk interpretation.
>
> ---
>
> - solution: {@{The count is $|\Omega_n|=2^n$, one path per increment sequence}@}
> - explanation: Every path is determined by {@{its $n$ increments in $\{-1,+1\}$}@}, so there is {@{a bijection between $\Omega_n$ and $\{-1,+1\}^n$}@}. <br/>
>     Hence {@{the count is $|\Omega_n|=2^n$, one path for each length-$n$ increment sequence of a simple random walk starting at $0$}@}.

<!-- markdownlint MD028 -->

> 4.b. $n$-step simple random walk and the ballot theorem. Let $\Omega_n=\{(\omega_j)_{j=0}^{n}:\omega_0=0,\ |\omega_j-\omega_{j-1}|=1\}$ with the uniform law $P_0$, and let $A_k=\{\omega\in\Omega_n:\omega_n=k\}$. Compute $P_0(A_k)$.
>
> ---
>
> - solution: {@{$P_0(A_k)=0$ when $n$ and $k$ have different parity, and $P_0(A_k)=2^{-n}\binom{n}{(n+k)/2}$ otherwise}@}
> - explanation: To {@{end at level $k$}@}, the walk must have {@{$(n+k)/2$ up-steps and $(n-k)/2$ down-steps}@}, so {@{parity is necessary}@}. <br/>
>     Therefore {@{the probability is $P_0(A_k)=0$ when $n$ and $k$ have different parity, and $P_0(A_k)=2^{-n}\binom{n}{(n+k)/2}$ otherwise}@}.

<!-- markdownlint MD028 -->

> 4.c. $n$-step simple random walk and the ballot theorem. Let $\Omega_n=\{(\omega_j)_{j=0}^{n}:\omega_0=0,\ |\omega_j-\omega_{j-1}|=1\}$ with the uniform law $P_0$, and let $A_k=\{\omega\in\Omega_n:\omega_n=k\}$. If a motion passes by exactly $k\in\{1,\dots,n\}$ votes after $n$ ballots, compute the conditional probability that it stays strictly ahead throughout the count.
>
> ---
>
> - solution: {@{The conditional probability is $P_0(\omega_j>0\ \forall j\mid A_k)=k/n$}@}
> - explanation: Encode each {@{ballot as $+1$ (motion) or $-1$ (against)}@}. <br/>
>     Then {@{ending ahead by $k$ votes is the endpoint condition $\omega_n=k$}@}, and staying {@{strictly ahead means $\omega_j>0$ for all $j\ge1$}@}. <br/>
>     {@{The total terminal-$k$ paths}@} are {@{the count $\binom{n}{(n+k)/2}$}@}. <br/>
>     For {@{good paths}@}, deleting {@{the first forced up-step}@} gives {@{paths from $(0,0)$ to $(n-1,k-1)$, of which there are $\binom{n-1}{(n+k-2)/2}$}@}. <br/>
>     {@{Bad paths among these}@} are {@{exactly those that hit $-1$}@}; by {@{reflection at the first hit, these correspond bijectively to paths from $(0,0)$ to $(n-1,-k-1)$}@}, counted by {@{the number $\binom{n-1}{(n-k-2)/2}$}@}. <br/>
>     Hence good paths equal {@{the difference $\binom{n-1}{(n+k-2)/2}-\binom{n-1}{(n-k-2)/2}$}@}, and dividing by {@{the total terminal-$k$ paths}@} gives {@{the ratio $P_0(\omega_j>0\ \forall j\mid A_k)=k/n$}@}. <br/>
>     In words, {@{the ballot theorem}@} says {@{the conditional chance of always leading equals the final margin ratio $k/n$}@}.
