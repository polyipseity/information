---
aliases:
    - HKUST MATH 2431 week 2 tutorial
    - HKUST MATH2431 week 2 tutorial
    - MATH 2431 week 2 tutorial
    - MATH2431 week 2 tutorial
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/week_2_tutorial
    - language/in/English
---

# week 2 tutorial

- HKUST MATH 2431

The questions on this page summarize the _official tutorial materials_ for week 2. Because they come from course materials rather than repository-authored review prompts, each question is kept as a markdown quote block and the clozes live inside that quoted Q&A block.

- topics: elementary combinatorics; sample spaces; events; sigma-algebras.

> Find the number of non-negative integer solutions of $x_1+\cdots+x_n=r$.
>
> Solution: Use {@{stars-and-bars}@}: model each solution as {@{$r$ stars}@} and {@{$n-1$ separators}@}, note the {@{bijection between arrangements and non-negative integer tuples}@}, then count arrangements by choosing separator (or star) positions among {@{$n+r-1$ slots}@}, giving {@{$\binom{n+r-1}{r}=\binom{n+r-1}{n-1}$}@}. Thus {@{counting solutions is equivalent to counting slot arrangements of stars and bars}@}.

<!-- markdownlint MD028 -->

> Expand $(x_1+x_2+x_3)^5$.
>
> Solution: Apply the {@{multinomial theorem}@}: collect terms by exponent triple {@{$(i,j,k)$}@} with {@{$i,j,k\ge 0$ and $i+j+k=5$}@}, use coefficient {@{$\binom{5}{i,j,k}=\frac{5!}{i!j!k!}$}@} from {@{counting permutations of repeated factors}@}, and obtain {@{$(x_1+x_2+x_3)^5=\sum_{i+j+k=5}\binom{5}{i,j,k}x_1^ix_2^jx_3^k$}@}. The key memory aid is that {@{the exponents record how often each variable is chosen among the 5 factors}@}.

<!-- markdownlint MD028 -->

> Find the number of arrangements of `MIIIISSSSPP`.
>
> Solution: Treat the word as a {@{multiset permutation problem}@} with {@{$11$ total symbols}@} and repeated counts {@{$1,4,4,2$}@}. You can count it by {@{direct multinomial reasoning}@}: choose which {@{position is the unique $M$}@}, then choose which {@{$4$ of the remaining 10 positions are $I$}@}, which {@{$4$ positions of what remains are $S$}@}, and the rest are {@{$P$}@}; equivalently, divide $11!$ by {@{factorials of repeated groups}@} to remove overcounting, yielding {@{$\dfrac{11!}{4!4!2!}=\binom{11}{1,4,4,2}$}@}.

<!-- markdownlint MD028 -->

> In an archer session, each round has three arrows and the session ends when one round hits the target three times. Build a sample space and identify $\bigcap_{n=1}^{\infty}A_n$, where $A_n$ is the event that the session lasts longer than $n$ rounds.
>
> Solution: Model each arrow by {@{$\{S,F\}$}@}, each round by {@{$\{S,F\}^3$}@}, and the whole experiment by {@{$(\{S,F\}^3)^{\mathbb{N}}$}@} with {@{stopping at first `SSS`}@}; this space contains {@{some extra infinite paths}@}, but that is {@{fine because it still describes every possible round-by-round history}@} and the stopping rule simply {@{ignores the impossible extra ones}@}. Since {@{$A_n$ means duration exceeds $n$ rounds}@}, the intersection over all $n$ is exactly the {@{infinite-duration event}@} {@{$\bigcap_{n=1}^{\infty}A_n=\{\text{no round is ever `SSS`}\}$}@}, i.e. the session {@{never terminates}@}.

<!-- markdownlint MD028 -->

> In the repeating coin-flip game where A, B, C flip in order and the first head wins, describe the events "A wins", "B wins", and the complement $(A\cup B)^c$ using the sample space $S=\{1,01,001,0001,\ldots,000\cdots\}$.
>
> Solution: Encode outcomes by {@{index of first head}@} (or the infinite all-tail sequence), observe winner is determined by {@{$\ell\bmod 3$}@}, so {@{$A=\{x\in S:\operatorname{len}(x)\equiv1\pmod3\}$}@} and {@{$B=\{x\in S:\operatorname{len}(x)\equiv2\pmod3\}$}@}; importantly, the process space includes {@{infinite sequences}@} as legitimate outcomes, so if no head ever appears that path is still an outcome, hence {@{$(A\cup B)^c$}@} is {@{`C wins' together with the no-winner infinite-tail outcome}@}.

<!-- markdownlint MD028 -->

> Five people $A,B,C,D,E$ are arranged in a line and then in a circle. How many arrangements are possible in each case?
>
> Solution: For a line use {@{all permutations of 5 distinct people}@} giving {@{$5!=120$}@}; for a circle identify rotations as equivalent, {@{fix one anchor person}@} to quotient rotations, and count remaining arrangements as {@{$(5-1)!=4!=24$}@}.

<!-- markdownlint MD028 -->

> A committee of 5 is chosen from 6 men and 4 women. Count the committees in the following cases:
>
> - (a) There is no restriction.
> - (b) One particular person must be included.
> - (c) There must be 3 men and 2 women.
> - (d) There must be a majority of women.
>
> Solution:
>
> - (a) {@{No restriction}@} gives {@{$\binom{10}{5}=252$}@}.
> - (b) {@{Include the designated person first}@}, then choose 4 of the remaining 9, giving {@{$\binom{9}{4}=126$}@}.
> - (c) {@{Exactly 3 men and 2 women}@} gives {@{$\binom{6}{3}\binom{4}{2}=120$}@}.
> - (d) {@{Majority women means either 3W2M or 4W1M}@}, so the total is {@{$\binom{4}{3}\binom{6}{2}+\binom{4}{4}\binom{6}{1}=60+6=66$}@}.

<!-- markdownlint MD028 -->

> Ten Oreo pieces are sprinkled onto 3 distinguishable scoops of ice cream. How many distributions are possible?
>
> Solution: Let {@{$u_i$}@} denote {@{pieces on scoop $i$}@} so the constraint is {@{$u_1+u_2+u_3=10$ with $u_i\ge0$}@}; apply {@{stars-and-bars}@} using {@{$10$ stars and $2$ bars}@} to count non-negative solutions, obtaining {@{$\binom{10+3-1}{3-1}=\binom{12}{2}=66$}@}.

<!-- markdownlint MD028 -->

> Let $\Omega=\mathbb{Z}$ and let $\mathcal{F}$ be the collection of subsets of $\Omega$ that are finite or cofinite. Is $\mathcal{F}$ a sigma-algebra?
>
> Solution: Although {@{complements are closed}@} (finite $\leftrightarrow$ cofinite), a sigma-algebra also requires {@{countable-union closure}@}: each singleton {@{$\{n\}$}@} is in $\mathcal{F}$, but their union {@{$\bigcup_{n\ge1}\{n\}=\mathbb{N}$}@} is {@{neither finite nor cofinite in $\mathbb{Z}$}@}, so {@{$\mathcal{F}$ is not a sigma-algebra}@}.

<!-- markdownlint MD028 -->

> If $\mathcal{F}$ is a sigma-algebra on $\Omega$ and $B\in\mathcal{F}$, show that $\mathcal{G}=\{A\cap B:A\in\mathcal{F}\}$ is a sigma-algebra on $B$.
>
> Solution: Verify {@{the three sigma-algebra axioms on space $B$}@}: whole space is {@{$B=\Omega\cap B\in\mathcal{G}$}@}; relative complement of {@{$E=A\cap B$}@} is {@{$B\setminus E=A^c\cap B\in\mathcal{G}$}@} since {@{$A^c\in\mathcal{F}$}@}; and countable unions satisfy {@{$\bigcup_n(A_n\cap B)=(\bigcup_n A_n)\cap B\in\mathcal{G}$}@} because {@{$\bigcup_n A_n\in\mathcal{F}$}@}, hence {@{$\mathcal{G}$ is a sigma-algebra on $B$}@}.
