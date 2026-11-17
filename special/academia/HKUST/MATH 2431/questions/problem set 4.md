---
aliases:
    - HKUST MATH 2431 problem set 4
    - HKUST MATH2431 problem set 4
    - MATH 2431 problem set 4
    - MATH2431 problem set 4
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/problem_set_4
    - language/in/English
---

# problem set 4

- HKUST MATH 2431

The questions on this page summarize the _official problem-set materials_ for problem set 4. As with the tutorial pages, each official question is kept as a markdown quote block and the clozes live inside the quoted Q&A block.

- topics: Benford's law; generated sigma-algebras; Borel sets; exponential and Laplace distributions; probability density functions.

> 1.a. Benford's law and sigma-algebras. Let $M_t=\bigcup_{n\in\mathbb Z}10^n[1,t)$ for $1<t<10$, let $\mathcal M=\sigma(\{M_t:1<t<10\})$, and define $P(M_t)=\log_{10}(t)$. Show that $\alpha M_t\in\mathcal M$ for all $\alpha>0$.
>
> ---
>
> - solution: {@{Every rescaling stays in the sigma-algebra, $\alpha M_t\in\mathcal M$ for all $\alpha>0$}@}
> - explanation: {@{Multiplying by $10$ does not change the shape of these sets}@}, because {@{the definition already contains all decimal scales $10^n$}@}, so it is enough to study {@{the range $\alpha\in(1,10)$}@}. <br/>
>     If {@{the product satisfies $\alpha t<10$}@}, multiplying shifts {@{$[1,t)$ to $[\alpha,\alpha t)$}@}, which is {@{exactly $M_{\alpha t}\setminus M_{\alpha}$}@}. <br/>
>     If {@{the product satisfies $\alpha t>10$}@}, the scaled interval {@{crosses the digit boundary at $10$}@}, so split {@{it there and rewrite each piece in the same generator form}@}. <br/>
>     In either case {@{the conclusion $\alpha M_t\in\mathcal M$ holds}@}.

<!-- markdownlint MD028 -->

> 1.b. Benford's law and sigma-algebras. Let $M_t=\bigcup_{n\in\mathbb Z}10^n[1,t)$ for $1<t<10$, let $\mathcal M=\sigma(\{M_t:1<t<10\})$, and define $P(M_t)=\log_{10}(t)$. Show that $P(\alpha M_t)=P(M_t)$.
>
> ---
>
> - solution: {@{The rescaling leaves the probability unchanged, $P(\alpha M_t)=P(M_t)$}@}
> - explanation: In the first case {@{the logarithms cancel}@}, giving {@{the value $P(\alpha M_t)=\log_{10}(\alpha t)-\log_{10}(\alpha)=\log_{10}(t)$}@}; in the second case {@{the same cancellation still applies}@}, giving {@{the same value $P(\alpha M_t)=\log_{10}(t)$}@}.

<!-- markdownlint MD028 -->

> 1.c. Benford's law and sigma-algebras. Let $M_t=\bigcup_{n\in\mathbb Z}10^n[1,t)$ for $1<t<10$, let $\mathcal M=\sigma(\{M_t:1<t<10\})$, and define $P(M_t)=\log_{10}(t)$. Deduce that the first-digit distribution is Benford's law, i.e. $P(\text{first digit}=k)=\log_{10}(1+1/k)$.
>
> ---
>
> - solution: {@{The first-digit law is Benford's, $P(\text{first digit}=k)=\log_{10}(1+1/k)$}@}
> - explanation: A number has {@{first digit $k$}@} exactly when it lies in {@{one of the intervals $10^n[k,k+1)$}@}. <br/>
>     So the event is {@{the union $\bigcup_{n\in\mathbb Z}10^n[k,k+1)$, the slice between $M_k$ and $M_{k+1}$}@}. <br/>
>     Therefore its probability is {@{the difference $P(\text{first digit}=k)=P(M_{k+1})-P(M_k)=\log_{10}(k+1)-\log_{10}(k)=\log_{10}(1+1/k)$}@}.

<!-- markdownlint MD028 -->

> 1.d. Benford's law and sigma-algebras. Let $M_t=\bigcup_{n\in\mathbb Z}10^n[1,t)$ for $1<t<10$, let $\mathcal M=\sigma(\{M_t:1<t<10\})$, and define $P(M_t)=\log_{10}(t)$. Extend the scaling properties from the generating family to all of $\mathcal M$.
>
> ---
>
> - solution: {@{Both scaling properties hold on all of $\mathcal M$: $\alpha A\in\mathcal M$ and $P(\alpha A)=P(A)$ for every $A\in\mathcal M$}@}
> - explanation: The two scaling properties now extend {@{from the generators to all of $\mathcal M$}@} in two steps. <br/>
>     {@{Step 1}@}: prove that {@{$\mathcal M$ itself is closed under scaling by $\alpha$}@}. <br/>
>     Fix {@{the scale $\alpha>0$ and the family $\mathcal M'=\{A\in\mathcal M:\alpha A\in\mathcal M\}$}@}, the collection of sets in {@{$\mathcal M$ whose scaled copies still belong to $\mathcal M$}@}. <br/>
>     Because {@{multiplication by $\alpha$ is a bijection of $(0,\infty)$}@}, it preserves {@{the whole space, complements, and countable unions}@}: {@{$\alpha(0,\infty)=(0,\infty)$, $\alpha(A^c)=(\alpha A)^c$, and $\alpha(\bigcup_{n}A_n)=\bigcup_n \alpha A_n$}@}. <br/>
>     Therefore {@{$\mathcal M'$ is a sigma-algebra}@}, and part (a) shows {@{every generator $M_t$ lies in $\mathcal M'$}@}. <br/>
>     Since {@{$\mathcal M=\sigma(\{M_t:1<t<10\})$ is the smallest sigma-algebra containing those generators}@}, {@{the inclusion $\mathcal M\subseteq\mathcal M'$ holds}@}, while by definition {@{the reverse inclusion $\mathcal M'\subseteq\mathcal M$ holds}@}, so {@{the two families agree, $\mathcal M'=\mathcal M$}@}. <br/>
>     Hence {@{every set $A\in\mathcal M$ satisfies $\alpha A\in\mathcal M$}@}. <br/>
>     {@{Step 2}@}: prove that {@{$P(\alpha A)=P(A)$ for every $A\in\mathcal M$}@}. <br/>
>     Define {@{the family $\mathcal M''=\{A\in\mathcal M:P(\alpha A)=P(A)\}$}@}, and show {@{that it is a Dynkin system}@} before using {@{the $\pi$-$\lambda$ theorem}@}. <br/>
>     First, {@{$(0,\infty)\in\mathcal M''$ because $P(\alpha(0,\infty))=P((0,\infty))=1$}@}. <br/>
>     Second, if {@{the set $A$ lies in $\mathcal M''$}@}, then {@{the complement satisfies $\alpha(A^c)=(\alpha A)^c$}@}, so {@{the chain $P(\alpha A^c)=P((\alpha A)^c)=1-P(\alpha A)=1-P(A)=P(A^c)$}@} and thus {@{the complement $A^c\in\mathcal M''$}@}. <br/>
>     Third, if {@{$A_1,A_2,\ldots\in\mathcal M''$ are pairwise disjoint}@}, then {@{scaling preserves disjointness}@}, and countable additivity gives {@{the chain $P\!\left(\alpha\left(\bigcup_i A_i\right)\right)=P\!\left(\bigcup_i \alpha A_i\right)=\sum_i P(\alpha A_i)=\sum_i P(A_i)=P\!\left(\bigcup_i A_i\right)$}@}. <br/>
>     So {@{$\mathcal M''$ is a Dynkin system}@}, and by part (b) {@{every generator $M_t$ lies in $\mathcal M''$}@}. <br/>
>     Also {@{$\{M_t:1<t<10\}$ is a $\pi$-system because $M_s\cap M_t=M_{\min\{s,t\}}$}@}, so {@{the $\pi$-$\lambda$ theorem gives $\mathcal M=\sigma(\{M_t:1<t<10\})\subseteq\mathcal M''$}@}. <br/>
>     Since {@{$\mathcal M''\subseteq\mathcal M$ by definition}@}, we conclude {@{the two families agree, $\mathcal M''=\mathcal M$}@}, hence for every {@{set $A\in\mathcal M$}@} both {@{$\alpha A\in\mathcal M$ and $P(\alpha A)=P(A)$ hold}@}.

<!-- markdownlint MD028 -->

> 2.a. More on sigma-algebras. Give an example showing that the union of two sigma-algebras on the same space need not be a sigma-algebra.
>
> ---
>
> - solution: {@{On $\Omega=\{1,2,3,4\}$ the union of $\mathcal F_1=\{\varnothing,\{1\},\{2,3,4\},\Omega\}$ and $\mathcal F_2=\{\varnothing,\{2\},\{1,3,4\},\Omega\}$ is not a sigma-algebra}@}
> - explanation: Take {@{the space $\Omega=\{1,2,3,4\}$}@} with {@{$\mathcal F_1=\{\varnothing,\{1\},\{2,3,4\},\Omega\}$ and $\mathcal F_2=\{\varnothing,\{2\},\{1,3,4\},\Omega\}$}@}. <br/>
>     Their union contains {@{$\{1\}$ and $\{2\}$}@} but not {@{the set $\{1,2\}$}@}, so it {@{fails closure under unions and is not a sigma-algebra}@}.

<!-- markdownlint MD028 -->

> 2.b. More on sigma-algebras. Starting from the definition $\mathcal B(\mathbb R)=\sigma(\{[a,b):a<b\})$, show that $[a,b]\in\mathcal B(\mathbb R)$ and $(-\infty,a]\in\mathcal B(\mathbb R)$.
>
> ---
>
> - solution: {@{Both $[a,b]$ and $(-\infty,a]$ are Borel sets}@}
> - explanation: Every {@{$[a,b+1/n)$ is in $\mathcal B(\mathbb R)$}@}, so {@{the intersection $[a,b]=\bigcap_{n\ge1}[a,b+1/n)$}@} is {@{Borel by countable intersection}@}. <br/>
>     Similarly, {@{the union $(-\infty,a]=\bigcup_{n\ge1}(a-n,a]$}@} is {@{Borel by countable union}@}.

<!-- markdownlint MD028 -->

> 2.c. More on sigma-algebras. Show that $\mathcal B(\mathbb R)$ is also generated by the half-lines $(-\infty,b]$ and by the collection of all open sets.
>
> ---
>
> - solution: {@{Both families generate the same Borel sigma-algebra, $\mathcal B(\mathbb R)=\sigma(\{(-\infty,b]:b\in\mathbb R\})=\sigma(\text{open sets})$}@}
> - explanation: Let {@{the family $\mathcal B_2=\sigma(\{(-\infty,b]:b\in\mathbb R\})$}@}. <br/>
>     Then {@{the intersection $(-\infty,b)=\bigcap_{n\ge1}(-\infty,b+1/n]$}@} belongs to {@{the family $\mathcal B_2$}@}, and therefore each half-open interval satisfies {@{the identity $[a,b)=(-\infty,b)\setminus(-\infty,a)$}@}, so {@{the inclusion $\mathcal B(\mathbb R)\subseteq\mathcal B_2$ holds}@}. <br/>
>     Also each half-line satisfies {@{the identity $(-\infty,b]=(b,\infty)^c$}@}, so {@{the sigma-algebra generated by open sets contains $\mathcal B_2$}@}. <br/>
>     Conversely, {@{every open set is a countable union of disjoint open intervals}@}, and each {@{open interval $(a,b)$}@} can be written as {@{the union $\bigcup_{n\ge1}[a+1/n,b)$}@}; thus {@{every open set is Borel}@}. <br/>
>     Therefore all three generating families yield {@{the same Borel sigma-algebra}@}.

<!-- markdownlint MD028 -->

> 3.a. Calculations with continuous distributions. A lightbulb lifetime is exponentially distributed with parameter $\lambda>0$. Compute the probability that it lasts between $2$ and $3$ years, and find the half-life.
>
> ---
>
> - solution: {@{The probability is $P([2,3])=e^{-2\lambda}-e^{-3\lambda}$, and the half-life is $t_{1/2}=\dfrac{\ln 2}{\lambda}$}@}
> - explanation: For {@{the exponential law with density $\lambda e^{-\lambda x}\mathbf1_{(0,\infty)}(x)$}@}, {@{the interval probability is $P([2,3])=\int_2^3\lambda e^{-\lambda x}\,dx=e^{-2\lambda}-e^{-3\lambda}$}@}, which at {@{the value $\lambda=1$}@} becomes {@{the number $e^{-2}(1-e^{-1})\approx0.0855$}@}. <br/>
>     {@{The half-life $t_{1/2}$}@} solves {@{the survival equation $P(X\ge t_{1/2})=e^{-\lambda t_{1/2}}=1/2$}@}, so {@{it equals $\dfrac{\ln 2}{\lambda}$}@}.

<!-- markdownlint MD028 -->

> 3.b. Calculations with continuous distributions. Show that the exponential distribution is memoryless.
>
> ---
>
> - solution: {@{The exponential law is memoryless, $P(X>s+t\mid X>s)=P(X>t)$}@}
> - explanation: The exponential law is memoryless because {@{the inclusion $(s+t,\infty)\subseteq(s,\infty)$ holds for every $s,t\ge0$}@}, since conditioning on {@{the later time $s$ that has already elapsed}@} gives {@{the ratio $P(X>s+t\mid X>s)=\dfrac{e^{-\lambda(s+t)}}{e^{-\lambda s}}=e^{-\lambda t}=P(X>t)$}@}, and this identity is {@{the memoryless property}@}.

<!-- markdownlint MD028 -->

> 3.c. Calculations with continuous distributions. For the continuous Laplace-$2$ distribution with density $f(x)=c_\lambda e^{-|x|/\lambda}$, determine $c_\lambda$, the CDF, and $P([-1,1])$.
>
> ---
>
> - solution: {@{$c_\lambda=\dfrac{1}{2\lambda}$, $F(x)=\frac12e^{x/\lambda}$ for $x\le0$ and $F(x)=1-\frac12e^{-x/\lambda}$ for $x>0$, and $P([-1,1])=1-e^{-1/\lambda}$}@}
> - explanation: Normalization yields {@{the identity $1=2c_\lambda\int_0^{\infty}e^{-x/\lambda}\,dx=2c_\lambda\lambda$}@}, so {@{the constant is $c_\lambda=1/(2\lambda)$}@}. <br/>
>     The CDF is {@{piecewise because the density is symmetric about $0$ but changes formula at the origin}@}: {@{$F(x)=\frac12e^{x/\lambda}$ for $x\le0$ and $F(x)=1-\frac12e^{-x/\lambda}$ for $x>0$}@}. <br/>
>     Hence {@{the probability is $P([-1,1])=F(1)-F(-1)=1-e^{-1/\lambda}$}@}. <!--SR:!fsrs,2027-01-24T00:00:00.000Z,216,216.23934371,1.98030797,2,7,0,0,2026-06-22T00:00:00.000Z!fsrs,2027-04-26T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-09T00:00:00.000Z!fsrs,2027-04-26T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-09T00:00:00.000Z!fsrs,2027-06-08T00:00:00.000Z,326,325.58679272,1,2,7,0,0,2026-07-17T00:00:00.000Z!fsrs,2027-04-07T00:00:00.000Z,278,278.46760619,1,2,7,0,0,2026-07-03T00:00:00.000Z!fsrs,2027-02-07T00:00:00.000Z,205,204.60152316,3.24197837,2,7,0,0,2026-07-17T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> 4.a. On probability density functions. For which $k\in\mathbb R$, if any, is $f(x)=x^{-k}\mathbf1_{[1,\infty)}(x)$ a probability density function?
>
> ---
>
> - solution: {@{Only the exponent $k=2$ produces a probability density function}@}
> - explanation: Integrability requires {@{the exponent range $k>1$}@}, and then {@{the integral is $\int_1^{\infty}x^{-k}\,dx=1/(k-1)$}@}; {@{setting it equal to $1$}@} forces {@{the unique choice $k=2$}@}. <br/>
>     Thus {@{the only exponent producing a PDF is $k=2$}@}.

<!-- markdownlint MD028 -->

> 4.b. On probability density functions. Give a density $f$ such that $c\sqrt f$ cannot be a density for any $c>0$.
>
> ---
>
> - solution: {@{The density $f(x)=x^{-2}\mathbf1_{[1,\infty)}(x)$ works, since $c\sqrt f$ is not integrable for any $c>0$}@}
> - explanation: Taking {@{exactly that density $f(x)=x^{-2}\mathbf1_{[1,\infty)}(x)$}@} works, because {@{the square root $\sqrt f(x)=x^{-1}\mathbf1_{[1,\infty)}(x)$}@} is {@{not integrable on $[1,\infty)$}@}, so {@{no positive constant can normalize $c\sqrt f$ into a density}@}.

<!-- markdownlint MD028 -->

> 4.c. On probability density functions. For $f(x)=2|x|(1-x^2)\mathbf1_{\{|x|\le1\}}$, find the cumulative distribution function and compute $P(( -\infty,-1/2))$ and $P([-1/2,1/2])$.
>
> ---
>
> - solution: {@{The CDF is $F(x)=0$ for $x<-1$, $F(x)=\dfrac{(1-x^2)^2}{2}$ for $-1\le x<0$, $F(x)=1-\dfrac{(1-x^2)^2}{2}$ for $0\le x<1$, and $F(x)=1$ for $x\ge1$, with $P(( -\infty,-1/2))=\dfrac{9}{32}$ and $P([-1/2,1/2])=\dfrac{7}{16}$}@}
> - explanation: {@{The support is $[-1,1]$}@}, and integrating {@{separately on the negative and positive halves}@} gives {@{the CDF $F(x)=0$ for $x<-1$, $F(x)=\dfrac{(1-x^2)^2}{2}$ for $-1\le x<0$, $F(x)=1-\dfrac{(1-x^2)^2}{2}$ for $0\le x<1$, and $F(x)=1$ for $x\ge1$}@}. <br/>
>     Since {@{the law has a density}@}, {@{single points have probability $0$}@}, so {@{the left value is $P(( -\infty,-1/2))=F(-1/2)=\dfrac{9}{32}$}@} and {@{the middle value is $P([-1/2,1/2])=F(1/2)-F(-1/2)=\dfrac{7}{16}$}@}. <!--SR:!fsrs,2027-05-12T00:00:00.000Z,304,304.30256839,1,2,7,0,0,2026-07-12T00:00:00.000Z!fsrs,2027-04-16T00:00:00.000Z,283,282.79716409,1,2,7,0,0,2026-07-07T00:00:00.000Z!fsrs,2027-05-23T00:00:00.000Z,313,312.84164192,1,2,7,0,0,2026-07-14T00:00:00.000Z!fsrs,2027-04-02T00:00:00.000Z,274,274.1280869,1,2,7,0,0,2026-07-02T00:00:00.000Z!fsrs,2027-05-18T00:00:00.000Z,309,308.57643926,1,2,7,0,0,2026-07-13T00:00:00.000Z!fsrs,2027-05-12T00:00:00.000Z,304,304.30256839,1,2,7,0,0,2026-07-12T00:00:00.000Z!fsrs,2027-04-05T00:00:00.000Z,274,274.1280869,1,2,7,0,0,2026-07-05T00:00:00.000Z!fsrs,2027-05-18T00:00:00.000Z,309,308.57643926,1,2,7,0,0,2026-07-13T00:00:00.000Z-->
