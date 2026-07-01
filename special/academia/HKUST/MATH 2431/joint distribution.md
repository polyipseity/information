---
aliases:
  - joint distribution
  - joint distributions
  - random vector
  - random vectors
tags:
  - flashcard/active/special/academia/HKUST/MATH_2431/joint_distribution
  - language/in/English
---

# joint distribution

A random vector keeps track of several observables simultaneously. Once one passes from one-dimensional laws to laws on $\mathbb R^2$ or $\mathbb R^n$, the fundamental new operations are marginalization, factorization, conditioning, convolution, and the study of extrema.

---

Flashcards for this section are as follows:

- overview ::@:: A joint distribution is the law of a random vector, so it records both the one-dimensional behavior of each coordinate and their dependence structure.
- necessity of joint distributions ::@:: Joint distributions capture the dependence between coordinates, going beyond what one-dimensional marginals can describe. They enable marginalization, conditioning, covariance, convolution, and the study of extremes.

## joint law and joint distribution function

The natural domain for the joint law of $n$ real random variables is $\mathbb R^n$ equipped with the Borel $\sigma$-algebra $$\mathcal B(\mathbb R^n)=\sigma(\{[a_1,b_1)\times\cdots\times[a_n,b_n):a_i<b_i\}).$$

The fundamental measurability fact is that a vector $(X_1,\dots,X_n)$ is $\mathcal F$-$\mathcal B(\mathbb R^n)$-measurable iff each coordinate $X_i$ is $\mathcal F$-$\mathcal B(\mathbb R)$-measurable. The proof has two directions:

- ($\Leftarrow$) If each $X_i$ is measurable, then for any rectangle $R=(-\infty,a_1]\times\cdots\times(-\infty,a_n]$, the preimage is $(X_1,\dots,X_n)^{-1}(R)=\bigcap_{i=1}^n X_i^{-1}((-\infty,a_i])\in\mathcal F$. Since rectangles of this form generate $\mathcal B(\mathbb R^n)$, the vector is measurable.
- ($\Rightarrow$) Conversely, if the vector is measurable, each coordinate satisfies $X_i=\pi_i\circ(X_1,\dots,X_n)$ where $\pi_i(x_1,\dots,x_n)=x_i$ is continuous (hence Borel measurable), so $X_i$ is measurable as a composition of measurable functions.

**Definition.** Let $X_1,\dots,X_n$ be random variables on $(\Omega,\mathcal F,P)$. The joint law of $X_1,\dots,X_n$ is the probability measure on $(\mathbb R^n,\mathcal B(\mathbb R^n))$ defined by $$P_{(X_1,\dots,X_n)}[B]=P[(X_1,\dots,X_n)^{-1}(B)],\qquad B\in\mathcal B(\mathbb R^n).$$

**Definition (joint CDF).** The joint cumulative distribution function of $X_1,\dots,X_n$ is the function $F_{X_1,\dots,X_n}:\mathbb R^n\to[0,1]$ defined by $$F_{X_1,\dots,X_n}(x_1,\dots,x_n)=P[X_1\le x_1,\dots,X_n\le x_n].$$

Properties:

- $F$ is non-decreasing in each argument.
- $F$ is right-continuous in each argument.
- Boundary behaviour: $F_{X_1,\dots,X_n}(x_1,\dots,x_n)\to0$ as any $x_i\to-\infty$, and $F_{X_1,\dots,X_n}(x_1,\dots,x_n)\to1$ as all $x_i\to\infty$.
- For $n\ge2$, the $n$-dimensional analogue of the non-decreasing condition is the rectangle increment condition: for any rectangle $[a_1,b_1]\times\cdots\times[a_n,b_n]$, the alternating sum $\sum_{(i_1,\dots,i_n)\in\{0,1\}^n}(-1)^{n-\sum_k i_k}F(b_{i_1},\dots,b_{i_n})\ge0$, where $b_{i_k}=a_k$ if $i_k=0$ and $b_{i_k}=b_k$ if $i_k=1$.

The joint CDF uniquely determines the joint law, analogously to the one-dimensional case. A rigorous justification uses the $\pi$-$\lambda$ theorem. The collection $\mathcal E=\{(-\infty,a_1]\times\cdots\times(-\infty,a_n]:a_1,\dots,a_n\in\mathbb R\}$ is a $\cap$-stable generator of $\mathcal B(\mathbb R^n)$: $\mathcal E$ is closed under finite intersections, and $\sigma(\mathcal E)=\mathcal B(\mathbb R^n)$. Two probability measures on $(\mathbb R^n,\mathcal B(\mathbb R^n))$ that agree on $\mathcal E$ must therefore be identical. Since $F_{X_1,\dots,X_n}(a_1,\dots,a_n)=P_{(X_1,\dots,X_n)}[(-\infty,a_1]\times\cdots\times(-\infty,a_n]]$, the joint CDF completely determines the joint law.

The existence of the joint law requires no additional construction: given random variables $X_1,\dots,X_n$ on $(\Omega,\mathcal F,P)$, the map $\omega\mapsto(X_1(\omega),\dots,X_n(\omega))$ is measurable (by the coordinate-wise criterion), so the pushforward $P_{(X_1,\dots,X_n)}$ is a well-defined probability measure on $(\mathbb R^n,\mathcal B(\mathbb R^n))$.

When $(X_1,\dots,X_n)$ is jointly continuous with density $f$, the joint CDF is obtained by integration: $F_{X_1,\dots,X_n}(x_1,\dots,x_n)=\int_{-\infty}^{x_1}\cdots\int_{-\infty}^{x_n}f_{X_1,\dots,X_n}(t_1,\dots,t_n)\,dt_n\cdots dt_1$.

---

Flashcards for this section are as follows:

- Borel $\sigma$-algebra on $\mathbb R^n$: How is $\mathcal B(\mathbb R^n)$ generated? ::@:: $\mathcal B(\mathbb R^n)=\sigma(\{[a_1,b_1)\times\cdots\times[a_n,b_n):a_i<b_i\})$.
- random vector measurability: When is $(X_1,\dots,X_n):\Omega\to\mathbb R^n$ measurable? ::@:: $(X_1,\dots,X_n)$ is measurable iff each coordinate $X_i$ is measurable. ($\Leftarrow$) Preimages of generating rectangles are intersections of coordinate preimages. ($\Rightarrow$) Each coordinate is $X_i=\pi_i\circ(X_1,\dots,X_n)$ with $\pi_i$ continuous (hence measurable).
- joint law definition: What is the joint law of $X_1,\dots,X_n$? ::@:: The joint law is the pushforward $P_{(X_1,\dots,X_n)}[B]=P[(X_1,\dots,X_n)^{-1}(B)]$, a probability measure on $(\mathbb R^n,\mathcal B(\mathbb R^n))$.
- joint CDF definition: What is the joint CDF $F_{X_1,\dots,X_n}(x_1,\dots,x_n)$? ::@:: $F_{X_1,\dots,X_n}(x_1,\dots,x_n)=P[X_1\le x_1,\dots,X_n\le x_n]$.
- joint CDF monotonicity: How does $F_{X_1,\dots,X_n}$ behave in each argument? ::@:: $F$ is non-decreasing in each argument.
- joint CDF right-continuity: What can you say about continuity of the joint CDF? ::@:: $F$ is right-continuous in each argument. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- joint CDF boundary behaviour: What are the limits of $F_{X_1,\dots,X_n}$ as arguments go to $\pm\infty$? ::@:: $F\to0$ as any $x_i\to-\infty$; $F\to1$ as all $x_i\to\infty$.
- joint CDF rectangle condition: What is the $n$-dimensional analogue of the non-decreasing condition for a joint CDF? ::@:: For any rectangle $[a_1,b_1]\times\cdots\times[a_n,b_n]$, the alternating sum $\sum_{(i_1,\dots,i_n)}(-1)^{n-\sum i_k}F(b_{i_1},\dots,b_{i_n})\ge0$, where $b_{i_k}=a_k$ or $b_k$ according to the vertex.
- $\pi$-$\lambda$ theorem and joint CDF uniqueness ::@:: The $\cap$-stable generator $\{(-\infty,a_1]\times\cdots\times(-\infty,a_n]:a_i\in\mathbb R\}$ generates $\mathcal B(\mathbb R^n)$, so two measures with the same values on these rectangles (i.e. the same joint CDF) must be identical by the $\pi$-$\lambda$ theorem.
- joint law existence via pushforward: Is an extension theorem needed to define $P_{(X_1,\dots,X_n)}$? ::@:: No. The joint law exists directly as $P_{(X_1,\dots,X_n)}[B]=P[(X_1,\dots,X_n)^{-1}(B)]$ once coordinate-wise measurability is verified; no Carath\u00e9odory or $\pi$-$\lambda$ argument is required for existence.

## joint probability mass functions

If $(X,Y)$ takes values in a countable set, its joint probability mass function is $p_{X,Y}(x,y)=P[X=x,Y=y]$. The law of $(X,Y)$ is recovered from this table by summing over subsets of the support. Every joint PMF must satisfy $p_{X,Y}(x,y)\ge 0$ and $\sum_{x,y}p_{X,Y}(x,y)=1$.

In finite examples, the joint law is best thought of as a matrix whose row and column sums produce the marginals. This makes it immediately clear that many different matrices can share the same row and column sums.

---

Flashcards for this section are as follows:

- joint PMF of a discrete pair: If $(X,Y)$ is discrete, how is $p_{X,Y}(x,y)$ defined? ::@:: $p_{X,Y}(x,y)=P[X=x,Y=y]$.
- normalization of a joint PMF: What conditions must $p_{X,Y}$ satisfy? ::@:: One must have $p_{X,Y}(x,y)\ge 0$ for all $(x,y)$ and $\sum_{x,y}p_{X,Y}(x,y)=1$.
- matrix model of a joint PMF: How can a joint PMF be interpreted as a matrix? ::@:: Entries are $p_{X,Y}(x,y)$, row sums give $p_X(x)$, column sums give $p_Y(y)$; many different matrices can share the same row and column sums. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- support of a discrete random vector ::@:: $\operatorname{supp}(X,Y)=\{(x,y):p_{X,Y}(x,y)>0\}$, a countable subset of $\mathbb R^2$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## joint probability densities

If $(X,Y)$ has a density $f_{X,Y}$ on $\mathbb R^2$, then probabilities are computed by integrating over planar regions: $P[(X,Y)\in A]=\iint_A f_{X,Y}(x,y)\,dx\,dy$.

Thus the density is not merely a formula: it is a rule assigning probability mass to regions of the plane. The support matters just as much as the formula itself. For example, a constant density on a triangle produces dependence even though the density is algebraically simple, because the region itself couples the coordinates.

---

Flashcards for this section are as follows:

- joint density on $\mathbb{R}^2$: If $(X,Y)$ has density $f_{X,Y}$, how do you compute $P[(X,Y)\in A]$? ::@:: $P[(X,Y)\in A]=\iint_A f_{X,Y}(x,y)\,dx\,dy$.
- why support matters in a joint density: Why can a simple formula for $f_{X,Y}$ still fail to imply independence? ::@:: Even if the algebraic formula for $f_{X,Y}$ is simple, a nonrectangular support can couple the coordinates and thereby create dependence.
- density as planar mass assignment ::@:: The joint density $f_{X,Y}$ assigns probability mass to regions of the plane; the shape of the support matters just as much as the algebraic formula. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- bivariate standard normal example: $f_{X,Y}(x,y)=\frac{1}{2\pi}e^{-(x^2+y^2)/2}$ ::@:: $X$ and $Y$ are independent $N(0,1)$ variables; the joint density factorizes as the product of two marginal $N(0,1)$ densities.

### differentiable joint CDF: the mixed partial condition

When a joint CDF $F$ on $\mathbb R^n$ is sufficiently smooth, the mixed partial derivative plays the role of the joint density, unifying the rectangle condition with the density picture.

**Key relation.** For $F$ differentiable enough (e.g. $C^n$), the alternating-sum rectangle probability equals the iterated integral of the mixed partial: $$\sum_{(i_1,\dots,i_n)}(-1)^{n-\sum i_k}F(b_{i_1},\dots,b_{i_n}) =\int_{a_1}^{b_1}\cdots\int_{a_n}^{b_n} \frac{\partial^nF}{\partial x_1\cdots\partial x_n}(x_1,\dots,x_n)\,dx_n\cdots dx_1.$$

Here $b_{i_k}=a_k$ (if $i_k=0$) or $b_k$ (if $i_k=1$), so the sum runs over all $2^n$ vertices of $[a_1,b_1]\times\cdots\times[a_n,b_n]$. For $n=2$, this says $P[a_1<X_1\le b_1,a_2<X_2\le b_2]=\int_{a_1}^{b_1}\int_{a_2}^{b_2}\frac{\partial^2F}{\partial x_1\partial x_2}(x_1,x_2)\,dx_2\,dx_1$.

**Relation to the joint density.** When $(X_1,\dots,X_n)$ is jointly continuous, the mixed partial coincides with the joint density wherever it exists: $$f_{X_1,\dots,X_n}(x_1,\dots,x_n)=\frac{\partial^nF}{\partial x_1\cdots\partial x_n}(x_1,\dots,x_n).$$

Thus the two key constraints on a joint CDF are unified: the mixed partial must be nonnegative and integrate to $1$.

---

Flashcards for this section are as follows:

- differentiable CDF condition: For a differentiable joint CDF $F$ on $\mathbb R^n$, what condition replaces the rectangle condition, and how does the alternating sum relate to the mixed partial? ::@:: $\frac{\partial^nF}{\partial x_1\cdots\partial x_n}\ge0$ everywhere; the alternating sum over any rectangle equals the iterated integral of that mixed partial. For $n=2$, $P[a_1<X_1\le b_1,a_2<X_2\le b_2]=\int_{a_1}^{b_1}\int_{a_2}^{b_2}\frac{\partial^2F}{\partial x_1\partial x_2}(x_1,x_2)\,dx_2\,dx_1$.
- mixed partial equals joint density: When a joint CDF $F$ is differentiable, how does the joint density relate to it? ::@:: $f_{X_1,\dots,X_n}=\partial^nF/(\partial x_1\cdots\partial x_n)$ at points where both exist, unifying the CDF and density perspectives.

### jointly continuous vs. each coordinate continuous

It is **not** true that a random vector $(X,Y)$ is jointly continuous whenever $X$ and $Y$ are each continuous. The counterexample is $X\sim N(0,1)$ and $Y=X$: then $(X,Y)$ lives on the diagonal $\Delta=\{(t,t):t\in\mathbb R\}$, so $P[(X,Y)\in\Delta]=1$, but $\iint_\Delta f\,dx\,dy=0$ for any density $f$ on $\mathbb R^2$. Hence no joint density exists. Joint continuity is a strictly stronger condition than coordinate-wise continuity.

**General principle.** A random vector $(X_1,\dots,X_n)$ is jointly continuous iff there exists a density $f:\mathbb R^n\to[0,\infty)$ such that $P[(X_1,\dots,X_n)\in A]=\int_A f\,d^nx$ for all Borel $A$. This is a global property of the vector, not a property of individual coordinates. Any degeneracy (concentration on a lower-dimensional manifold) destroys joint continuity.

---

Flashcards for this section are as follows:

- jointly continuous vs. coordinate continuous: Give a counterexample with $X\sim N(0,1),\,Y=X$ showing that continuous coordinates do not imply a continuous random vector. ::@:: $X\sim N(0,1)$ and $Y=X$: then $(X,Y)$ is concentrated on the diagonal $\Delta$, so $P[(X,Y)\in\Delta]=1$ but no density on $\mathbb R^2$ can assign mass $1$ to a line.
- general principle: joint continuity vs. coordinate continuity ::@:: Joint continuity is strictly stronger: $(X,Y)$ can fail to have a joint density even when $X$ and $Y$ individually have densities (e.g. $X\sim N(0,1),Y=X$ lives on the diagonal). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

---

## marginal distributions and marginal densities

Marginals are obtained by forgetting one coordinate. In the discrete case, $p_X(x)=\sum_y p_{X,Y}(x,y)$ and $p_Y(y)=\sum_x p_{X,Y}(x,y)$. In the continuous case, $f_X(x)=\int_{-\infty}^{\infty} f_{X,Y}(x,y)\,dy$ and $f_Y(y)=\int_{-\infty}^{\infty} f_{X,Y}(x,y)\,dx$.

**Proof.** For the continuous formula, fix a Borel set $B\subseteq\mathbb R$. Then $P[X\in B]=P[(X,Y)\in B\times \mathbb R]=\iint_{B\times \mathbb R} f_{X,Y}(x,y)\,dx\,dy$. Fubini's theorem rewrites this as $\int_B \left(\int_{-\infty}^{\infty}f_{X,Y}(x,y)\,dy\right)dx$, which identifies the marginal density of $X$. The proof for $Y$ is identical.

The key warning is that marginals do not determine the joint law. One can alter the dependence structure while keeping the same one-dimensional distributions.

---

Flashcards for this section are as follows:

- marginalization ::@:: Marginals are obtained from a joint law by summing or integrating out the unused coordinates.
- marginals do not determine the joint law ::@:: Different joint laws can have exactly the same marginals, because dependence information is lost when one coordinate is integrated out.
- marginal density via Fubini: How does Fubini's theorem derive $f_X(x)$ from the joint density? ::@:: $P[X\in B]=\iint_{B\times\mathbb R}f_{X,Y}(x,y)\,dx\,dy=\int_B(\int_{-\infty}^{\infty}f_{X,Y}(x,y)\,dy)\,dx$, so $f_X(x)=\int_{-\infty}^{\infty}f_{X,Y}(x,y)\,dy$.
- marginal PMF from joint PMF: How do you obtain $p_X(x)$ from $p_{X,Y}(x,y)$? ::@:: $p_X(x)=\sum_y p_{X,Y}(x,y)$; one sums over all values of $Y$.

### two joint densities with identical marginals

Consider two joint densities on $[0,1]^2$: $$f_1(x,y)=2x+2y-4xy,\qquad f_2(x,y)=1.$$

Both have $U([0,1])$ marginals: integrating out $y$ gives $f_X(x)=1$ for $x\in[0,1]$ in both cases. Yet the dependence structure differs. For instance, $P[X^2\le Y]$ is $19/30$ under $f_1$ but $2/3$ under $f_2$. This illustrates that marginals alone never determine the joint law.

---

Flashcards for this section are as follows:

- same marginals, different joint: Give two joint densities on $[0,1]^2$ with $U([0,1])$ marginals but different joint behavior. ::@:: $f_1(x,y)=2x+2y-4xy$ and $f_2(x,y)=1$ both have $U([0,1])$ marginals, but $P[X^2\le Y]$ equals $19/30$ vs $2/3$.
- main lesson from the identical-marginals example ::@:: Two different joint densities can produce exactly the same marginals; the joint law is not determined by its marginals alone.

## expectation of functions of a random vector

Let $g:\mathbb R^n\to\mathbb R$ be a measurable function. If $X_1,\dots,X_n$ are discrete with joint PMF $p_{X_1,\dots,X_n}$, then $$E[g(X_1,\dots,X_n)]=\sum_{x_1,\dots,x_n} g(x_1,\dots,x_n)\,p_{X_1,\dots,X_n}(x_1,\dots,x_n),$$

provided the sum converges absolutely. If $(X_1,\dots,X_n)$ is jointly continuous with density $f_{X_1,\dots,X_n}$, then $$E[g(X_1,\dots,X_n)]=\int_{\mathbb R^n} g(x_1,\dots,x_n)\,f_{X_1,\dots,X_n}(x_1,\dots,x_n)\,d^nx,$$

provided the integral converges absolutely.

**Proof sketch (continuous case).** Approximate $g$ by simple functions and use the definition of the density. The discrete case follows by the definition of the joint PMF.

**Additivity of expectation as a corollary.** Taking $g(x,y)=x+y$ gives $E[X+Y]=E[X]+E[Y]$ without any independence assumption. Similarly, $g(x,y)=\alpha x+\beta y$ gives linearity.

**Application to independence.** When $X$ and $Y$ are independent, taking $g(x,y)=xy$ yields $E[XY]=E[X]E[Y]$, provided the moments exist. (The proof uses that $p_{X,Y}=p_Xp_Y$ or $f_{X,Y}=f_Xf_Y$.)

---

Flashcards for this section are as follows:

- expectation of a function of discrete random vector: If $X_1,\dots,X_n$ are discrete with joint PMF $p$, how do you compute $E[g(X_1,\dots,X_n)]$? ::@:: $E[g(X_1,\dots,X_n)]=\sum_{x_1,\dots,x_n} g(x_1,\dots,x_n)\,p_{X_1,\dots,X_n}(x_1,\dots,x_n)$, provided absolute convergence.
- expectation of a function of continuous random vector: If $(X_1,\dots,X_n)$ is jointly continuous with density $f$, how do you compute $E[g(X_1,\dots,X_n)]$? ::@:: $E[g(X_1,\dots,X_n)]=\int_{\mathbb R^n} g(x_1,\dots,x_n)\,f_{X_1,\dots,X_n}(x_1,\dots,x_n)\,d^nx$, provided absolute convergence.
- additivity of expectation from joint formula ::@:: Taking $g(x,y)=x+y$ in the joint expectation formula yields $E[X+Y]=E[X]+E[Y]$ without any independence assumption, by linearity of sums/integrals. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- product expectation under independence: If $X$ and $Y$ are independent, what is $E[XY]$? ::@:: $E[XY]=E[X]E[Y]$, because the joint PMF/density factors and the double sum/integral separates.
- additivity of expectation: discrete proof sketch ::@:: $E[X+Y]=\sum_{x,y}(x+y)p_{X,Y}(x,y)=\sum_x x\sum_y p_{X,Y}(x,y)+\sum_y y\sum_x p_{X,Y}(x,y)=E[X]+E[Y]$, using marginalization of the joint PMF. The continuous proof is analogous via Fubini. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## joint moment generating function

The joint moment generating function (MGF) of a random vector $(X_1,\dots,X_n)$ is the function $M_{(X_1,\dots,X_n)}:\mathbb R^n\to\mathbb R\cup\{\infty\}$ defined by $$M_{(X_1,\dots,X_n)}(t_1,\dots,t_n)=E\!\left[e^{t_1X_1+\cdots+t_nX_n}\right],$$ for those $t=(t_1,\dots,t_n)$ where the expectation exists (a neighbourhood of the origin for the MGF to be useful).

**Connection to joint moments.** The joint MGF generates joint moments via partial differentiation at the origin: $$E[X_1^{k_1}\cdots X_n^{k_n}]=\left.\frac{\partial^{k_1+\cdots+k_n}}{\partial t_1^{k_1}\cdots\partial t_n^{k_n}}M_{(X_1,\dots,X_n)}(t_1,\dots,t_n)\right|_{t_1=\cdots=t_n=0},$$ provided the MGF exists in a neighbourhood of the origin. This extends the univariate relation $E[X^k]=M_X^{(k)}(0)$ to the multivariate setting.

**Factorization under independence.** If $X$ and $Y$ are independent and their individual MGFs exist in a neighbourhood of $0$, then the joint MGF factors: $$M_{(X,Y)}(s,t)=E[e^{sX+tY}]=E[e^{sX}]\,E[e^{tY}]=M_X(s)\,M_Y(t).$$ Conversely, if $M_{(X,Y)}(s,t)=M_X(s)M_Y(t)$ for all $(s,t)$ in a neighbourhood of $(0,0)$, then $X$ and $Y$ are independent — a consequence of the uniqueness of the joint MGF and the fact that product MGFs correspond to product measures.

**Joint MGF of a sum.** Setting $t_1=t_2=\cdots=t_n=t$ shows that the MGF of the sum is obtained by evaluating the joint MGF on the diagonal: $$M_{X+Y}(t)=E[e^{t(X+Y)}]=M_{(X,Y)}(t,t).$$ More generally, for a linear combination $a_1X_1+\cdots+a_nX_n$, $$M_{a_1X_1+\cdots+a_nX_n}(t)=M_{(X_1,\dots,X_n)}(a_1t,\dots,a_nt).$$

**Example — bivariate normal.** If $(X,Y)\sim N(\mu_X,\mu_Y,\sigma_X^2,\sigma_Y^2,\rho)$, the joint MGF is $$M_{(X,Y)}(s,t)=\exp\!\left(s\mu_X+t\mu_Y+\frac12\bigl(s^2\sigma_X^2+2\rho st\sigma_X\sigma_Y+t^2\sigma_Y^2\bigr)\right).$$ This can be derived by completing the square in the exponent of the bivariate normal density. Differentiating with respect to $s$ and $t$ and evaluating at $(0,0)$ recovers $E[X]=\mu_X$, $E[Y]=\mu_Y$, $E[XY]=\mu_X\mu_Y+\rho\sigma_X\sigma_Y$, etc.

---

Flashcards for this section are as follows:

- joint MGF definition: What is the joint MGF of $(X_1,\dots,X_n)$? ::@:: $M_{(X_1,\dots,X_n)}(t_1,\dots,t_n)=E[e^{t_1X_1+\cdots+t_nX_n}]$ for $t$ where the expectation exists.
- joint moments from joint MGF: How do you recover $E[X_1^{k_1}\cdots X_n^{k_n}]$ from the joint MGF? ::@:: $E[X_1^{k_1}\cdots X_n^{k_n}]=\frac{\partial^{k_1+\cdots+k_n}}{\partial t_1^{k_1}\cdots\partial t_n^{k_n}}M_{(X_1,\dots,X_n)}(0,\dots,0)$.
- joint MGF factorization under independence: What is the relationship between $M_{(X,Y)}(s,t)$ and $M_X(s),M_Y(t)$ when $X\perp Y$? ::@:: $M_{(X,Y)}(s,t)=M_X(s)M_Y(t)$ in a neighbourhood of $(0,0)$.
- joint MGF of a sum: How is $M_{X+Y}(t)$ obtained from the joint MGF? ::@:: $M_{X+Y}(t)=M_{(X,Y)}(t,t)$.
- joint MGF of a linear combination: How is $M_{a_1X_1+\cdots+a_nX_n}(t)$ expressed via the joint MGF? ::@:: $M_{a_1X_1+\cdots+a_nX_n}(t)=M_{(X_1,\dots,X_n)}(a_1t,\dots,a_nt)$.
- bivariate normal joint MGF: What is the joint MGF of a bivariate normal $(X,Y)\sim N(\mu_X,\mu_Y,\sigma_X^2,\sigma_Y^2,\rho)$? ::@:: $M_{(X,Y)}(s,t)=\exp(s\mu_X+t\mu_Y+\frac12(s^2\sigma_X^2+2\rho st\sigma_X\sigma_Y+t^2\sigma_Y^2))$.
- converse of MGF factorization implies independence: If $M_{(X,Y)}(s,t)=M_X(s)M_Y(t)$ in a neighbourhood of $(0,0)$, can we conclude $X\perp Y$? ::@:: Yes, because the joint MGF uniquely determines the joint law, and a product MGF corresponds to a product measure.

## independence via joint and marginal distributions

Two random variables are independent if and only if their joint law factors as the product of their marginals. Concretely, this means $p_{X,Y}(x,y)=p_X(x)p_Y(y)$ in the discrete case, $f_{X,Y}(x,y)=f_X(x)f_Y(y)$ for Lebesgue-almost all $(x,y)$ in the continuous case, and equivalently $F_{X,Y}(x,y)=F_X(x)F_Y(y)$ for all $x,y$.

**Proof sketch.** If the product formula holds for the density or PMF, then integrating or summing over rectangles immediately yields the factorization of rectangle probabilities, hence independence. Conversely, independence gives product probabilities on rectangles, and from those one recovers the factorized density or PMF wherever it exists.

Measurable transforms preserve independence. If $X_1,\dots,X_n$ are independent and each $h_i$ is measurable, then the random variables $h_1(X_1),\dots,h_n(X_n)$ are also independent. The proof is a direct preimage argument: events of the form $\{h_i(X_i)\in B_i\}$ are exactly $\{X_i\in h_i^{-1}(B_i)\}$.

**Remark (product measure construction).** The identity $P_{(X_1,\ldots,X_n)} = \bigotimes_{i=1}^n P_{X_i}$ is often taken as the definition of independence for random variables, but it requires justification that the product set-function $\mu_0(A_1\times\cdots\times A_n)=\prod_{i=1}^n P_{X_i}(A_i)$ extends from rectangles to a genuine probability measure on $(\mathbb R^n,\mathcal B(\mathbb R^n))$. One defines $\mu_0$ on the semiring of rectangles, verifies $\sigma$-additivity there, and then applies the Carathéodory extension theorem to obtain a unique measure on $\mathcal B(\mathbb R^n)$. The $\pi$-$\lambda$ theorem provides an alternative route: two measures that agree on the $\cap$-stable generator of rectangles must coincide on all of $\mathcal B(\mathbb R^n)$. Either way, an extension theorem from measure theory is essential for the construction.

---

Flashcards for this section are as follows:

- independence from a discrete joint law: If $X$ and $Y$ are independent, what equation must $p_{X,Y}(x,y)$ satisfy for all $(x,y)$? ::@:: $p_{X,Y}(x,y)=p_X(x)p_Y(y)$ for all $(x,y)$.
- independence from a joint density: If $X$ and $Y$ are independent, what equation must $f_{X,Y}(x,y)$ satisfy for almost all $(x,y)$? ::@:: $f_{X,Y}(x,y)=f_X(x)f_Y(y)$ for Lebesgue-almost all $(x,y)$.
- independence via joint CDF: If $X$ and $Y$ are independent, what identity must $F_{X,Y}(x,y)$ satisfy for all $x,y$? ::@:: $F_{X,Y}(x,y)=F_X(x)F_Y(y)$ for all $x,y$.
- measurable transforms preserve independence: If $X_1,\dots,X_n$ are independent and each $h_i$ is measurable, what can you conclude about $h_1(X_1),\dots,h_n(X_n)$? ::@:: The transformed random variables $h_1(X_1),\dots,h_n(X_n)$ are also independent.
- product set-function for independence definition ::@:: The identity $P_{(X_1,\ldots,X_n)} = \bigotimes_{i=1}^n P_{X_i}$ is defined by setting $\mu_0(A_1\times\cdots\times A_n)=\prod_{i=1}^n P_{X_i}(A_i)$ on rectangles and extending to a genuine measure. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Carathéodory extension for product measure ::@:: Define $\mu_0$ on the semiring of rectangles, verify $\sigma$-additivity there, then apply Carathéodory's extension theorem to obtain a unique measure on $\mathcal B(\mathbb R^n)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- $\pi$-$\lambda$ theorem alternative for product measure ::@:: Two measures that agree on the $\cap$-stable generator of rectangles must coincide on all of $\mathcal B(\mathbb R^n)$ by the $\pi$-$\lambda$ theorem, providing another route to the product measure.
- why extension theorems are essential for joint independence ::@:: Without an extension theorem, $\mu_0$ is only a pre-measure defined on rectangles; one needs Carathéodory or the $\pi$-$\lambda$ theorem to guarantee a genuine probability measure on all Borel sets, which is essential for a rigorous definition of independence of random variables. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- CDF factorization implies independence: proof idea ::@:: If $F_{X,Y}(x,y)=F_X(x)F_Y(y)$, then $P_{(X,Y)}$ and $P_X\otimes P_Y$ agree on the $\cap$-stable generator $\{(-\infty,a]\times(-\infty,b]:a,b\in\mathbb R\}$ of $\mathcal B(\mathbb R^2)$, so they coincide everywhere by $\pi$-$\lambda$, establishing independence. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## convolution and sums of independent variables

If $X$ and $Y$ are independent continuous random variables with densities $f_X$ and $f_Y$, then the density of $X+Y$ is the convolution $f_{X+Y}(z)=\int_{-\infty}^{\infty}f_X(z-y)f_Y(y)\,dy$.

**Proof.** Introduce the change of variables $(u,v)=(x+y,y)$. The joint density of $(X+Y,Y)$ is $f_X(u-v)f_Y(v)$, and integrating out $v$ produces the formula above.

This single identity explains familiar closure results:

- independent binomials with common success probability add to another binomial,
- independent Poisson laws add to another Poisson law,
- independent normal laws add to another normal law.

For discrete variables the same argument gives the summation formula $P[X+Y=z]=\sum_y P[X=z-y]P[Y=y]$.

---

Flashcards for this section are as follows:

- convolution formula for independent continuous sums: If $X$ and $Y$ are independent with densities $f_X$ and $f_Y$, what is $f_{X+Y}(z)$? ::@:: $f_{X+Y}(z)=\int_{-\infty}^{\infty}f_X(z-y)f_Y(y)\,dy$.
- discrete convolution formula for independent sums: If $X$ and $Y$ are independent discrete variables, what is $P[X+Y=z]$? ::@:: $P[X+Y=z]=\sum_y P[X=z-y]P[Y=y]$.
- convolution proof by change of variables: What change of variables proves the continuous convolution formula? ::@:: $(u,v)=(x+y,y)$ gives joint density $f_X(u-v)f_Y(v)$; integrating out $v$ yields $f_{X+Y}(z)=\int_{-\infty}^{\infty}f_X(z-y)f_Y(y)\,dy$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- convolution closure property ::@:: If $X$ and $Y$ are independent from a family closed under convolution (binomial with common $p$, Poisson, normal, gamma with common rate), then $X+Y$ also belongs to that family. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- explicit convolution stability: State the parameter formulas for a sum of two independent Binomial ($n,p$ and $m,p$), Poisson ($\lambda,\mu$), Normal ($\mu_1,\sigma_1^2$; $\mu_2,\sigma_2^2$), and Gamma ($\alpha_1,\lambda$; $\alpha_2,\lambda$) variables. ::@:: Binomial: $\operatorname{Bin}(n,p)*\operatorname{Bin}(m,p)=\operatorname{Bin}(n+m,p)$. Poisson: $\operatorname{Pois}(\lambda)*\operatorname{Pois}(\mu)=\operatorname{Pois}(\lambda+\mu)$. Normal: $N(\mu_1,\sigma_1^2)*N(\mu_2,\sigma_2^2)=N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$. Gamma: $\Gamma(\alpha_1,\lambda)*\Gamma(\alpha_2,\lambda)=\Gamma(\alpha_1+\alpha_2,\lambda)$.
- Vandermonde identity in Binomial convolution ::@:: $\binom{n+m}{k}=\sum_{\ell=0}^k\binom{n}{k-\ell}\binom{m}{\ell}$ is used to prove $\operatorname{Bin}(n,p)*\operatorname{Bin}(m,p)=\operatorname{Bin}(n+m,p)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Exponential sum to Gamma ::@:: $E(\lambda)*E(\lambda)=\Gamma(2,\lambda)$; more generally, $\Gamma(\alpha_1,\lambda)*\Gamma(\alpha_2,\lambda)=\Gamma(\alpha_1+\alpha_2,\lambda)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

---

### sum CDF derivation

The convolution formula can also be obtained without Jacobians. By the law of total probability and independence, $$\begin{aligned} F_Z(z)&=P[X+Y\le z]\\ &=\int_{-\infty}^{\infty}P[X\le z-y\mid Y=y]\,f_Y(y)\,dy\\ &=\int_{-\infty}^{\infty}F_X(z-y)\,f_Y(y)\,dy. \end{aligned}$$

Differentiating under the integral sign (Leibniz rule) recovers the convolution density: $$f_Z(z)=\frac{d}{dz}F_Z(z)=\int_{-\infty}^{\infty}f_X(z-y)\,f_Y(y)\,dy.$$

This CDF approach (matching Proposition 7.25 of the course notes) is often easier to justify formally than the change-of-variables method.

---

Flashcards for this section are as follows:

- convolution CDF derivation: How can $f_{X+Y}$ be derived using only CDF and differentiation? ::@:: $F_Z(z)=P[X+Y\le z]=\int_{-\infty}^{\infty}P[X\le z-y\mid Y=y]\,f_Y(y)\,dy=\int_{-\infty}^{\infty}F_X(z-y)\,f_Y(y)\,dy$ by total probability and independence.<p>Differentiate under the integral (Leibniz rule): $\frac{d}{dz}F_Z(z)=\int_{-\infty}^{\infty}\frac{\partial}{\partial z}F_X(z-y)\,f_Y(y)\,dy=\int_{-\infty}^{\infty}f_X(z-y)\,f_Y(y)\,dy$, recovering the convolution density.

---

### sum characteristic function

Let $\varphi_X(t)=E[e^{itX}]$ denote the characteristic function of $X$. For independent $X$ and $Y$, $$\varphi_{X+Y}(t)=E[e^{it(X+Y)}]=E[e^{itX}e^{itY}]=E[e^{itX}]\,E[e^{itY}]=\varphi_X(t)\,\varphi_Y(t),$$

where the third equality uses independence. Hence the characteristic function of the sum is the product of the marginal characteristic functions. By the Fourier inversion theorem, the density of $X+Y$ is uniquely determined by $\varphi_{X+Y}$, so $\varphi_{X+Y}=\varphi_X\varphi_Y$ provides an algebraic proof of the convolution formula.

For discrete variables the same idea applies using the probability-generating function $G_X(s)=E[s^X]$, giving $G_{X+Y}(s)=G_X(s)G_Y(s)$ for independent $X$, $Y$.

---

Flashcards for this section are as follows:

- convolution via characteristic functions: What is $\varphi_{X+Y}(t)$ in terms of $\varphi_X$ and $\varphi_Y$ under independence? ::@:: $\varphi_{X+Y}(t)=E[e^{it(X+Y)}]=E[e^{itX}e^{itY}]=E[e^{itX}]E[e^{itY}]=\varphi_X(t)\varphi_Y(t)$, factoring by independence.<p>Fourier inversion then uniquely determines the convolution density, giving an algebraic proof of convolution stability.
- probability-generating function for discrete sums: Under independence, how does $G_{X+Y}(s)$ relate to $G_X(s)$ and $G_Y(s)$? ::@:: $G_{X+Y}(s)=E[s^{X+Y}]=E[s^X s^Y]=E[s^X]E[s^Y]=G_X(s)G_Y(s)$, factoring by independence; $G_X(s)=E[s^X]$ for $s$ where the expectation exists.

---

### sum intuition

Why does convolution appear? The density $f_{X+Y}(z)$ at a point $z$ collects contributions from all pairs $(x,y)$ such that $x+y=z$. For each possible value $y$ of $Y$, the contribution is the density of $X$ being at $z-y$ times the density of $Y$ being at $y$, i.e. $f_X(z-y)f_Y(y)$. Summing (integrating) over all $y$ gives the total mass at $z$. Independence is essential: without it the joint density would not factor, and the integral would remain two-dimensional instead of reducing to a one-dimensional convolution.

---

Flashcards for this section are as follows:

- convolution intuition: Explain intuitively why $f_{X+Y}$ is a convolution. ::@:: Mass at $z$ comes from pairs $(x,y)$ with $x+y=z$: for each $y$, $X$ must be $z-y$, contributing $f_X(z-y)f_Y(y)\,dy$; integrating over all $y$ gives the total.

## ratio distribution

For $Z=X/Y$ with $X,Y$ independent continuous variables (defined when $Y>0$ almost surely, or more generally by splitting the integral), the density can be derived via the CDF method.

---

Flashcards for this section are as follows:

- ratio distribution overview: What approach gives the density of $Z=X/Y$ for independent continuous $X,Y$? ::@:: The CDF method: $F_Z(z)=\int_0^\infty F_X(zy)f_Y(y)\,dy$ when $Y>0$ a.s.; split by sign of $Y$ otherwise.

---

### ratio CDF derivation

Assume $Y>0$ a.s. (e.g., $Y\sim\operatorname{Exp}(\lambda)$ or $Y\sim\Gamma(\alpha,\lambda)$). Then $$\begin{aligned} F_Z(z)&=P[X/Y\le z]=P[X\le zY]\\ &=\int_0^{\infty}P[X\le zy\mid Y=y]\,f_Y(y)\,dy\\ &=\int_0^{\infty}F_X(zy)\,f_Y(y)\,dy. \end{aligned}$$

Differentiating under the integral (Leibniz rule) gives the density: $$f_Z(z)=\frac{d}{dz}F_Z(z)=\int_0^{\infty}y\,f_X(zy)\,f_Y(y)\,dy.$$

If $Y$ can take both signs, split the probability: $$F_Z(z)=P[X\le zY,\;Y>0]+P[X\ge zY,\;Y<0],$$

with each term handled by conditioning on $Y$.

---

Flashcards for this section are as follows:

- ratio distribution CDF derivation: Derive $f_{X/Y}$ using the CDF method, assuming $Y>0$ a.s. ::@:: $F_Z(z)=P[X/Y\le z]=\int_0^{\infty}P[X\le zy\mid Y=y]\,f_Y(y)\,dy=\int_0^{\infty}F_X(zy)\,f_Y(y)\,dy$, using total probability and independence.<p>Differentiate under the integral: $\frac{d}{dz}F_X(zy)=y f_X(zy)$, so $f_Z(z)=\frac{d}{dz}F_Z(z)=\int_0^{\infty}y f_X(zy)\,f_Y(y)\,dy$.
- ratio distribution sign-split formula: How does the CDF derivation change when $Y$ can take both signs? ::@:: When $Y$ can be negative, $X/Y\le z$ is not equivalent to $X\le zY$: for $Y>0$, $X/Y\le z\iff X\le zY$; for $Y<0$, division reverses the inequality: $X/Y\le z\iff X\ge zY$.<p>Hence $F_Z(z)=P[X\le zY,Y>0]+P[X\ge zY,Y<0]$, which evaluates as $\int_0^{\infty}F_X(zy)f_Y(y)\,dy+\int_{-\infty}^0[1-F_X(zy)]f_Y(y)\,dy$.

---

### ratio characteristic function

Unlike sums, the characteristic function does not simplify because $\varphi_{X/Y}(t)=E[e^{itX/Y}]$ does not factor. The Mellin transform $E[Z^{s}]=E[X^{s}]E[Y^{-s}]$ (for moments, not the full distribution) is the natural algebraic tool, but it only captures moments rather than the whole law when they exist.

---

Flashcards for this section are as follows:

- ratio distribution CF problem: Why doesn't the characteristic function simplify for $X/Y$? ::@:: $\varphi_{X/Y}(t)=E[e^{itX/Y}]=\iint e^{itx/y}f_X(x)f_Y(y)\,dx\,dy$ does not factor because $e^{itx/y}\neq g(x)h(y)$ in general — the denominator $y$ inside the exponent couples $x$ and $y$ inseparably, unlike $e^{it(x+y)}=e^{itx}e^{ity}$.
- Mellin transform for ratio: What is the Mellin transform of $Z=X/Y$ for independent nonnegative $X,Y$? ::@:: $\mathcal M_Z(s)=E[Z^s]=E[(X/Y)^s]=E[X^sY^{-s}]=E[X^s]E[Y^{-s}]=\mathcal M_X(s)\,\mathcal M_{Y^{-1}}(s)$, factoring into separate moments of $X$ and $Y^{-s}$ by independence (but only captures moments, not the full law).

---

### ratio examples <!-- check: ignore-line[section_example_heading]: conceptual examples, not a copy of course layout -->

- **Cauchy distribution:** If $X$ and $Y$ are independent $N(0,1)$, then $Z=X/Y$ is Cauchy with density $f_Z(z)=1/[\pi(1+z^2)]$. The Cauchy distribution has no finite moments — a striking consequence of the heavy tail produced by division near zero.
- **F-distribution:** If $U\sim\chi^2_p$ and $V\sim\chi^2_q$ are independent, then $F_{p,q}=(U/p)/(V/q)$ follows an F-distribution with $(p,q)$ degrees of freedom, the workhorse of ANOVA.
- **Ratio of Exponentials:** If $X,Y\sim\operatorname{Exp}(\lambda)$ independent, then $Z=X/Y$ has density $f_Z(z)=1/(1+z)^2$ for $z\ge0$, a special case of the F-distribution with $(2,2)$ degrees of freedom.

---

Flashcards for this section are as follows:

- Cauchy as ratio of Normals: What is the distribution of $X/Y$ when $X$ and $Y$ are independent $N(0,1)$? ::@:: Cauchy with density $f(z)=1/[\pi(1+z^2)]$, which has no finite moments.<p>Derivation: $f_Z(z)=\int_{-\infty}^\infty|y|\phi(zy)\phi(y)\,dy$ where $\phi$ is the $N(0,1)$ density; $f_Z(z)=\frac{1}{2\pi}\int_{-\infty}^\infty|y|e^{-y^2(z^2+1)/2}dy=\frac{1}{\pi}\int_0^\infty y e^{-y^2(z^2+1)/2}dy$.<p>Substituting $u=y^2(z^2+1)/2$ gives $f_Z(z)=\frac{1}{\pi(z^2+1)}\int_0^\infty e^{-u}\,du=\frac{1}{\pi(1+z^2)}$.
- ratio of independent Exponentials: If $X,Y\sim\operatorname{Exp}(\lambda)$ independent, what is the distribution of $X/Y$? ::@:: $f_Z(z)=1/(1+z)^2$ for $z\ge0$, an $F(2,2)$ distribution.<p>Derivation: $f_Z(z)=\int_0^\infty y\lambda e^{-\lambda z y}\lambda e^{-\lambda y}dy=\lambda^2\int_0^\infty y e^{-\lambda y(1+z)}dy$.<p>Evaluating $\int_0^\infty y e^{-ay}dy=1/a^2$ with $a=\lambda(1+z)$ gives $f_Z(z)=\lambda^2/[\lambda^2(1+z)^2]=1/(1+z)^2$.
- F-distribution as ratio of scaled chi-squares: If $U\sim\chi^2_p$ and $V\sim\chi^2_q$ are independent, what is the distribution of $(U/p)/(V/q)$? ::@:: $F_{p,q}$ with $(p,q)$ degrees of freedom, the workhorse of ANOVA.<p>Derivation: $F_{p,q}=\frac{U/p}{V/q}=\frac{q}{p}\cdot\frac{U}{V}$ is a scaled ratio of independent chi-squares.<p>Using the ratio density formula with $f_U(u)\propto u^{p/2-1}e^{-u/2}$ and $f_V(v)\propto v^{q/2-1}e^{-v/2}$ yields the F density $f_F(x)\propto x^{p/2-1}(1+\frac{p}{q}x)^{-(p+q)/2}$ for $x\ge0$.

---

### ratio intuition

Ratios arise naturally when normalising one random quantity by another (signal-to-noise ratio, Sharpe ratio, $t$- and $F$-statistics). The density of a ratio typically has heavier tails than the numerator because division by small denominator values amplifies the outcome — an effect that becomes more pronounced when the denominator has mass near zero. This is why the Cauchy (ratio of Normals) fails to have finite mean or variance.

---

Flashcards for this section are as follows:

- ratio distribution intuition: Why do ratios tend to have heavier tails than their numerators? ::@:: Division by small denominator values amplifies the outcome, so the density has more mass in the tails.

## product distribution

For $Z=XY$ with $X,Y$ independent continuous variables (or more generally, for any $(X,Y)$ with a known joint density), the density can be derived via the CDF method, paralleling the ratio distribution.

---

Flashcards for this section are as follows:

- product distribution overview: What approach gives the density of $Z=XY$ for independent continuous $X,Y$? ::@:: The CDF method: $F_Z(z)=\iint_{\{xy\le z\}}f_X(x)f_Y(y)\,dx\,dy$; differentiating gives $f_Z(z)=\int\frac{1}{|y|}f_X(z/y)f_Y(y)\,dy$.

---

### product CDF derivation

Assume $X,Y\ge0$ almost surely and independent. Then, for $z\ge0$, $$\begin{aligned} F_Z(z)&=P[XY\le z]=\int_0^{\infty}P[X\le z/y\mid Y=y]\,f_Y(y)\,dy\\ &=\int_0^{\infty}F_X(z/y)\,f_Y(y)\,dy, \end{aligned}$$ where the first equality conditions on $Y=y$ and uses independence. Differentiating under the integral (Leibniz rule) gives the density: $$f_Z(z)=\frac{d}{dz}F_Z(z)=\int_0^{\infty}\frac{1}{y}\,f_X\!\left(\frac{z}{y}\right)f_Y(y)\,dy.$$

If $X$ and $Y$ can take both signs, split the probability into four quadrants: $$F_Z(z)=P[XY\le z]=\iint_{\{xy\le z\}}f_X(x)f_Y(y)\,dx\,dy,$$ and evaluate by partitioning the integration region into $\{x\ge0,y\ge0\}$, $\{x\ge0,y<0\}$, $\{x<0,y\ge0\}$, $\{x<0,y<0\}$, carefully handling the inequality direction in each quadrant. The general density formula becomes $$f_Z(z)=\int_{-\infty}^{\infty}\frac{1}{|y|}\,f_X\!\left(\frac{z}{y}\right)f_Y(y)\,dy,$$ where the absolute value accounts for sign flips in the Jacobian of the transformation $(x,y)\mapsto(z,y)$.

**Proof sketch of the general formula.** Transform $(X,Y)\mapsto(Z,Y)$ with $Z=XY$. The inverse transformation is $(z,y)\mapsto(z/y,y)$ with Jacobian determinant $\partial(x,y)/\partial(z,y)=1/|y|$ (the absolute value appears because the density integrates over signed area). The joint density of $(Z,Y)$ is $f_{Z,Y}(z,y)=f_X(z/y)f_Y(y)/|y|$, and integrating out $y$ yields $f_Z(z)$.

---

Flashcards for this section are as follows:

- product distribution CDF derivation (nonnegative case): Derive the CDF and density of $Z=XY$ assuming $X,Y\ge0$ a.s. and independent. ::@:: $F_Z(z)=P[XY\le z]=\int_0^{\infty}P[X\le z/y\mid Y=y]\,f_Y(y)\,dy=\int_0^{\infty}F_X(z/y)\,f_Y(y)\,dy$, using total probability and independence.<p>Differentiate under the integral: $\frac{d}{dz}F_X(z/y)=(1/y)f_X(z/y)$, giving $f_Z(z)=\int_0^{\infty}\frac1y f_X(z/y)f_Y(y)\,dy$.
- product distribution general density formula: What is $f_{XY}(z)$ for independent $X,Y$ with possibly signed support? ::@:: $f_Z(z)=\int_{-\infty}^{\infty}\frac{1}{|y|}f_X(z/y)f_Y(y)\,dy$.<p>Derivation: partition $\mathbb R^2$ into four quadrants by the sign of $y$; in each, $XY\le z$ transforms to $X\le z/y$ or $X\ge z/y$ depending on the sign. The Jacobian of $(X,Y)\mapsto(Z,Y)$ is $1/|y|$, giving the absolute value.
- product distribution Jacobian derivation: What transformation gives the product density formula? ::@:: The change $(X,Y)\mapsto(Z,Y)$ has inverse $(z,y)\mapsto(z/y,y)$ with Jacobian $|1/y|$, giving $f_{Z,Y}(z,y)=f_X(z/y)f_Y(y)/|y|$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

---

### product characteristic function

Unlike sums, the characteristic function of a product does not simplify: $$\varphi_{XY}(t)=E[e^{itXY}]=\iint e^{itxy}\,f_X(x)f_Y(y)\,dx\,dy,$$ which does not factor into separate functions of $X$ and $Y$ because $txy$ couples the two variables multiplicatively within the exponential.

The Mellin transform is the natural tool for products: for a nonnegative random variable $Z$, its Mellin transform is $\mathcal M_Z(s)=E[Z^{s}]$, defined for $s$ where the expectation exists. For a product $Z=XY$ of independent nonnegative variables, $$\mathcal M_Z(s)=E[(XY)^s]=E[X^s]\,E[Y^s]=\mathcal M_X(s)\,\mathcal M_Y(s).$$ This factors just as the characteristic function factors for sums. The Mellin transform recovers moments directly ($E[Z^k]=\mathcal M_Z(k)$ for integer $k$) but does not uniquely determine the distribution without additional regularity conditions (unlike the characteristic function).

---

Flashcards for this section are as follows:

- product distribution CF problem: Why doesn't the characteristic function simplify for $XY$? ::@:: $\varphi_{XY}(t)=E[e^{itXY}]=\iint e^{itxy}f_X(x)f_Y(y)\,dx\,dy$ does not factor because $e^{itxy}\neq g(x)h(y)$ — the product $xy$ inside the exponent couples $x$ and $y$ multiplicatively, unlike $e^{it(x+y)}=e^{itx}e^{ity}$.
- Mellin transform for products: What is the Mellin transform of $Z=XY$ for independent nonnegative $X,Y$? ::@:: $\mathcal M_Z(s)=E[Z^s]=E[(XY)^s]=E[X^sY^s]=E[X^s]E[Y^s]=\mathcal M_X(s)\mathcal M_Y(s)$, factoring by independence, analogous to the CF for sums.

---

### product examples <!-- check: ignore-line[section_example_heading]: conceptual examples, not a copy of course layout -->

- **Product of two independent $U([0,1])$ variables.** Let $X,Y\sim U([0,1])$ independent. Then $Z=XY$ has density $f_Z(z)=-\log z$ for $0<z\le 1$, and $0$ otherwise. Derivation: $f_Z(z)=\int_z^{1}\frac{1}{y}\,dy=-\log z$ for $0<z\le 1$, using the general formula $f_Z(z)=\int_{0}^{1}\frac{1}{y}f_X(z/y)f_Y(y)\,dy$ with $f_X(x)=f_Y(y)=1$ and noting that $f_X(z/y)=1$ only when $z/y\le 1$, i.e. $y\ge z$.
- **Product of two independent $N(0,1)$ variables.** If $X,Y\sim N(0,1)$ independent, then $Z=XY$ follows a variance-gamma (also called normal product) distribution. Its density is $f_Z(z)=\frac{1}{\pi}K_0(|z|)$, where $K_0$ is the modified Bessel function of the second kind of order $0$. This distribution is symmetric about $0$, has mean $0$, and has infinite kurtosis relative to a normal.
- **Product under bivariate normality.** If $(X,Y)$ is bivariate normal with correlation $\rho$ (and zero means for simplicity), the distribution of $XY$ is a linear combination of independent chi-square variables: $XY\stackrel{d}{=}\sigma_X\sigma_Y\bigl(\rho U^2+(1-\rho^2)^{1/2}UV\bigr)$ where $U,V\sim N(0,1)$ independent, which follows a variance-gamma distribution with additional parameters.

---

Flashcards for this section are as follows:

- product of two independent uniforms: What is the density of $Z=XY$ when $X,Y\sim U([0,1])$ i.i.d.? ::@:: $f_Z(z)=-\log z$ for $0<z\le 1$, with $f_X(x)=f_Y(y)=1$ on $[0,1]$.<p>Derivation: $f_Z(z)=\int_0^1\frac1y\mathbf 1\{z/y\le1\}\,dy=\int_z^1\frac1y\,dy=[\log y]_z^1=-\log z$ for $0<z\le1$.
- product of two independent standard normals: What distribution does $Z=XY$ follow when $X,Y\sim N(0,1)$ i.i.d.? ::@:: Variance-gamma (normal product) distribution with density $f_Z(z)=\frac1\pi K_0(|z|)$, where $K_0$ is the modified Bessel function of the second kind.<p>Derivation: $f_Z(z)=\int_{-\infty}^\infty\frac1{|y|}\phi(z/y)\phi(y)\,dy=\frac1{2\pi}\int_{-\infty}^\infty\frac1{|y|}e^{-((z/y)^2+y^2)/2}dy$.<p>Substituting $t=y^2$ yields $f_Z(z)=\frac1\pi\int_0^\infty\frac1{\sqrt{t}}e^{-(z^2/t+t)/2}dt=\frac1\pi K_0(|z|)$.
- product under bivariate normality: How can $XY$ be expressed when $(X,Y)$ is bivariate normal with zero means? ::@:: $XY\stackrel{d}{=}\sigma_X\sigma_Y(\rho U^2+(1-\rho^2)^{1/2}UV)$ with $U,V\sim N(0,1)$ independent.<p>Derivation: standardize $X'=X/\sigma_X$, $Y'=Y/\sigma_Y$ and write $Y'=\rho X'+\sqrt{1-\rho^2}\,Z$ with $Z\sim N(0,1)$ independent of $X'$. Then $X'Y'=\rho X'^2+\sqrt{1-\rho^2}\,X'Z$, a linear combination of independent chi-square and normal-product terms.

---

### product intuition

Products arise naturally in scaling (multiplying a quantity by a random scale factor) and area computations (joint support of two coordinates). The density of a product involves an integral along hyperbolas $xy=z$ rather than lines $x+y=z$ (convolution) or rays $x/y=z$ (ratio). The factor $1/|y|$ in the integral reflects the changing spacing of the hyperbolas: as $y$ increases, the required $x=z/y$ shrinks, and the Jacobian adjusts for the density mass per unit area. This contrasts with the convolution where the additive structure gives a simple shift, and with the ratio where $|y|$ appears (rather than $1/|y|$) because the mapping $(x,y)\mapsto(z,y)$ with $z=x/y$ has Jacobian $|y|$.

---

Flashcards for this section are as follows:

- product distribution intuition: Compare the integral structure of product, sum, and ratio. ::@:: Product integrates along hyperbolas $xy=z$ with Jacobian $1/|y|$; sum (convolution) integrates along lines $x+y=z$ with Jacobian $1$; ratio integrates along rays $x/y=z$ with Jacobian $|y|$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## order statistics and extremes

A sequence of random variables $X_1,X_2,\dots$ is called **i.i.d.** (independent and identically distributed) if the variables are independent and each has the same marginal distribution. This is the most common setting for order statistics.

Let $X_1,\dots,X_n$ be random variables. The **order statistics** are the sorted values $$X_{(1)}\le X_{(2)}\le\cdots\le X_{(n)},$$ where $(X_{(1)},\dots,X_{(n)})$ is a permutation of $(X_1,\dots,X_n)$ that arranges them in non-decreasing order. The $k$-th order statistic $X_{(k)}$ is the $k$-th smallest value.

**Special cases.** The minimum is $X_{(1)}$, the maximum is $X_{(n)}$. The **median** (when $n$ is odd) is the middle order statistic $X_{((n+1)/2)}$; when $n$ is even, any value between $X_{(n/2)}$ and $X_{(n/2+1)}$ qualifies as a median. **Quartiles** split the ordered sample into four parts: the first quartile $Q_1\approx X_{(\lfloor n/4\rfloor)}$ (25th percentile) and the third quartile $Q_3\approx X_{(\lceil 3n/4\rceil)}$ (75th percentile).

### i.i.d. extremes

**Proposition.** Let $X_1,\dots,X_n$ be i.i.d. with cumulative distribution function $F$. Then the distribution functions of the maximum $X_{(n)}$ and the minimum $X_{(1)}$ are $$F_{X_{(n)}}(x)=F(x)^n,\qquad F_{X_{(1)}}(x)=1-(1-F(x))^n,\qquad x\in\mathbb R.$$

**Proof.** The event $\{X_{(n)}\le x\}$ is exactly $\bigcap_{i=1}^n\{X_i\le x\}$, and $\{X_{(1)}>x\}$ is $\bigcap_{i=1}^n\{X_i>x\}$. By independence, $$F_{X_{(n)}}(x)=P[X_{(n)}\le x]=P\!\left(\bigcap_{i=1}^n\{X_i\le x\}\right)=\prod_{i=1}^n P[X_i\le x]=F(x)^n,$$ $$F_{X_{(1)}}(x)=1-P[X_{(1)}>x]=1-P\!\left(\bigcap_{i=1}^n\{X_i>x\}\right)=1-(1-F(x))^n.$$

If $F$ is differentiable with density $f$, then differentiating gives the density of the maximum as $f_{X_{(n)}}(x)=nF(x)^{n-1}f(x)$, and similarly the density of the minimum as $f_{X_{(1)}}(x)=n(1-F(x))^{n-1}f(x)$.

These are the basic formulas for order-statistics extremes, used in extreme value theory and reliability analysis.

---

Flashcards for this section are as follows:

- cdf of the maximum: If $X_1,\dots,X_n$ are iid with CDF $F$, what is $P(\max_i X_i\le x)$? ::@:: $P(\max_i X_i\le x)=P(\bigcap_i\{X_i\le x\})=\prod_i P(X_i\le x)=F(x)^n$, using independence.<p>Derivation: $\{\max_i X_i\le x\}=\bigcap_i\{X_i\le x\}$ (the max is $\le x$ iff every observation is $\le x$). By independence, $P(\bigcap_i\{X_i\le x\})=\prod_i P(X_i\le x)$. Since i.i.d., each $P(X_i\le x)=F(x)$, so $\prod_i F(x)=F(x)^n$.
- cdf of the minimum: If $X_1,\dots,X_n$ are iid with CDF $F$, what is $F_{\min}(x)$? ::@:: $F_{\min}(x)=1-(1-F(x))^n$, since $P(\min_i X_i>x)=P(\bigcap_i\{X_i>x\})=(1-F(x))^n$.<p>Derivation: $F_{\min}(x)=P(\min_i X_i\le x)=1-P(\min_i X_i>x)$ (complement trick). $\{\min_i X_i>x\}=\bigcap_i\{X_i>x\}$ (the min exceeds $x$ iff every observation exceeds $x$). By independence, $P(\bigcap_i\{X_i>x\})=\prod_i P(X_i>x)$. Each $P(X_i>x)=1-F(x)$, so $F_{\min}(x)=1-(1-F(x))^n$.
- density of the maximum: If $X_1,\dots,X_n$ are iid with differentiable CDF $F$ and density $f$, what is $f_{\max}(x)$? ::@:: $f_{\max}(x)=d/dx[F(x)^n]=nF(x)^{n-1}f(x)$.<p>Derivation: $f_{\max}(x)=F_{\max}'(x)=\frac{d}{dx}[F(x)^n]$. By the chain rule, $\frac{d}{dx}[F(x)^n]=nF(x)^{n-1}\cdot F'(x)=nF(x)^{n-1}f(x)$, using $f(x)=F'(x)$.
- density of the minimum: If $X_1,\dots,X_n$ are iid with differentiable CDF $F$ and density $f$, what is $f_{\min}(x)$? ::@:: $f_{\min}(x)=d/dx[1-(1-F(x))^n]=n(1-F(x))^{n-1}f(x)$.<p>Derivation: $f_{\min}(x)=F_{\min}'(x)=\frac{d}{dx}[1-(1-F(x))^n]$. Apply the chain rule: $\frac{d}{dx}[1-(1-F(x))^n]=-n(1-F(x))^{n-1}\cdot(-F'(x))=n(1-F(x))^{n-1}f(x)$, using $F'(x)=f(x)$ and the two negatives canceling.
- i.i.d. definition: What does it mean for a sequence $X_1,X_2,\dots$ to be i.i.d.? ::@:: The random variables are independent and each has the same marginal distribution (identically distributed).
- Exponential extremes example: $\min_i X_i$ for $X_1,\dots,X_n\sim E(\lambda)$ i.i.d. ::@:: For i.i.d. $E(\lambda)$ variables, $\min_i X_i\sim E(\lambda n)$, i.e. the min is Exponential with rate $n\lambda$.<p>Derivation: $P(\min_i X_i>x)=\prod_i P(X_i>x)=\prod_i e^{-\lambda x}=e^{-n\lambda x}$, which is the survival function of $\operatorname{Exp}(n\lambda)$. Hence the CDF is $1-e^{-n\lambda x}$, confirming $\min_i X_i\sim E(n\lambda)$.
- order statistics definition: What are the order statistics $X_{(1)},\dots,X_{(n)}$ of a sample $X_1,\dots,X_n$? ::@:: The order statistics are the sorted values $X_{(1)}\le X_{(2)}\le\cdots\le X_{(n)}$, obtained by permuting $(X_1,\dots,X_n)$ into non-decreasing order. $X_{(k)}$ is the $k$-th smallest value.
- special cases of order statistics: What are $X_{(1)}, X_{(n)}$, median, and quartiles in terms of order statistics? ::@:: Min $=X_{(1)}$, max $=X_{(n)}$. Median (odd $n$): $X_{((n+1)/2)}$; median (even $n$): any value between $X_{(n/2)}$ and $X_{(n/2+1)}$. $Q_1\approx X_{(\lfloor n/4\rfloor)}$, $Q_3\approx X_{(\lceil 3n/4\rceil)}$.

---

### joint density of order statistics

Let $X_1,\dots,X_n$ be i.i.d. with density $f$ and CDF $F$. Denote the order statistics by $X_{(1)}\le\cdots\le X_{(n)}$. The joint density of all $n$ order statistics is $$f_{X_{(1)},\dots,X_{(n)}}(x_1,\dots,x_n)=n!\prod_{i=1}^n f(x_i),\qquad x_1<\dots<x_n.$$

**Heuristic derivation.** The unordered vector $(X_1,\dots,X_n)$ has joint density $\prod_{i=1}^n f(x_i)$. For a given ordered tuple $(x_1<\dots<x_n)$, there are exactly $n!$ permutations of the indices that map the unordered vector to this ordered list. Since each permutation corresponds to a distinct region of $\mathbb R^n$ (defined by the ordering of the coordinates), and the density is symmetric in the arguments, the total density on the ordered cone $\{x_1<\dots<x_n\}$ accumulates the probability from all $n!$ permutation regions, each contributing $\prod f(x_i)$. Hence the factor $n!$.

**Consequence — marginal density of the $k$-th order statistic.** Integrating the joint density over all variables except $x_k$ yields $$f_{X_{(k)}}(x)=\frac{n!}{(k-1)!\,(n-k)!}\,F(x)^{k-1}\,(1-F(x))^{n-k}\,f(x),$$ known as the $k$-th order statistic density. For the maximum ($k=n$) this reduces to $nF(x)^{n-1}f(x)$, and for the minimum ($k=1$) to $n(1-F(x))^{n-1}f(x)$, matching the earlier formulas.

---

Flashcards for this section are as follows:

- joint density of all order statistics: For i.i.d. $X_1,\dots,X_n$ with density $f$, what is $f_{X_{(1)},\dots,X_{(n)}}(x_1,\dots,x_n)$? ::@:: $f_{X_{(1)},\dots,X_{(n)}}(x_1,\dots,x_n)=n!\prod_{i=1}^n f(x_i)$ for $x_1<\dots<x_n$.<p>Derivation: $(X_1,\dots,X_n)$ has density $\prod_i f(x_i)$; each ordered tuple $x_1<\dots<x_n$ has $n!$ permutations mapping the unordered vector to it, so density on the ordered cone accumulates $n!\prod f(x_i)$.
- joint density of order statistics: heuristic derivation ::@:: There are $n!$ permutations mapping the unordered vector to ordered values, each with density $\prod f(x_i)$; summing over all regions on the ordered cone gives $n!\prod f(x_i)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- marginal density of the $k$-th order statistic: What is $f_{X_{(k)}}(x)$ for i.i.d. $X_1,\dots,X_n$ with density $f$? ::@:: $f_{X_{(k)}}(x)=\frac{n!}{(k-1)!(n-k)!}F(x)^{k-1}(1-F(x))^{n-k}f(x)$.<p>Integration derivation: integrate the joint density $n!\prod_{i=1}^n f(x_i)$ over $\{x_1<\dots<x_{k-1}<x<x_{k+1}<\dots<x_n\}$. The $k-1$ variables below $x$ integrate to $F(x)^{k-1}/(k-1)!$ and the $n-k$ above integrate to $(1-F(x))^{n-k}/(n-k)!$ (using the ordered-simplex identity $\int_{a<z_1<\dots<z_m<b}\prod g(z_i)\,dz_i=\frac1{m!}(\int_a^b g(z)\,dz)^m$). Multiplying by $n!f(x)$ and canceling factorials gives the result.

---

### distribution of the range

The range $R=X_{(n)}-X_{(1)}$ measures the spread of the sample. Its CDF and density can be derived from the joint distribution of $(X_{(1)},X_{(n)})$.

**Joint density of min and max.** For i.i.d. $X_1,\dots,X_n$ with density $f$, the joint density of $(X_{(1)},X_{(n)})$ is $$f_{X_{(1)},X_{(n)}}(u,v)=n(n-1)\,f(u)\,f(v)\,\bigl[F(v)-F(u)\bigr]^{n-2},\qquad u<v.$$

**Derivation.** The event that the minimum is near $u$ and the maximum near $v$ requires: one observation falls near $u$ (density $f(u)$), one near $v$ (density $f(v)$), and the remaining $n-2$ observations lie in $(u,v)$ (probability $[F(v)-F(u)]^{n-2}$). The combinatorial factor $n(n-1)$ accounts for choosing which observation is the minimum and which is the maximum.

**CDF of the range.** For $r\ge0$, $$F_R(r)=P[R\le r]=\int_{-\infty}^{\infty}\int_{u}^{u+r}f_{X_{(1)},X_{(n)}}(u,v)\,dv\,du.$$ Substituting the joint density and changing variables $v=u+w$ gives $$F_R(r)=\int_{-\infty}^{\infty}n f(u)\int_{0}^{r}(n-1)f(u+w)[F(u+w)-F(u)]^{n-2}\,dw\,du.$$ The inner integral can be evaluated explicitly by recognizing the derivative of $[F(u+w)-F(u)]^{n-1}$ with respect to $w$: $$\frac{d}{dw}[F(u+w)-F(u)]^{n-1}=(n-1)f(u+w)[F(u+w)-F(u)]^{n-2}.$$ Hence $$F_R(r)=\int_{-\infty}^{\infty}n f(u)\,[F(u+r)-F(u)]^{n-1}\,du.$$

**Density of the range.** Differentiating with respect to $r$, $$f_R(r)=\frac{d}{dr}F_R(r)=n(n-1)\int_{-\infty}^{\infty} f(u)\,f(u+r)\,[F(u+r)-F(u)]^{n-2}\,du,\qquad r\ge0.$$

**Special case — Exponential distribution.** For i.i.d. $X_i\sim\operatorname{Exp}(\lambda)$, the range $R$ has the same distribution as the maximum of $n-1$ i.i.d. $\operatorname{Exp}(\lambda)$ variables (a consequence of the memoryless property and the spacing representation of exponential order statistics). The density is $f_R(r)=(n-1)\lambda e^{-\lambda r}(1-e^{-\lambda r})^{n-2}$ for $r\ge0$.

---

Flashcards for this section are as follows:

- joint density of min and max: For i.i.d. $X_1,\dots,X_n$ with density $f$, what is $f_{X_{(1)},X_{(n)}}(u,v)$? ::@:: $f_{X_{(1)},X_{(n)}}(u,v)=n(n-1)f(u)f(v)[F(v)-F(u)]^{n-2}$ for $u<v$.<p>Derivation: pick one observation near $u$ ($n$ ways, density $f(u)$), one near $v$ ($n-1$ ways, density $f(v)$), remaining $n-2$ lie in $(u,v)$ with probability $F(v)-F(u)$.
- joint density of min and max: combinatorial derivation ::@:: One observation at $u$ (factor $n$), one at $v$ (factor $n-1$ for the remaining choice), the rest in $(u,v)$ (factor $[F(v)-F(u)]^{n-2}$), all multiplied by the density values. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- CDF of the range: What is $F_R(r)$ for i.i.d. $X_1,\dots,X_n$ with density $f$? ::@:: $F_R(r)=\int_{-\infty}^{\infty} n f(u)[F(u+r)-F(u)]^{n-1}\,du$.<p>Derivation: start from $f_{X_{(1)},X_{(n)}}(u,v)=n(n-1)f(u)f(v)[F(v)-F(u)]^{n-2}$. Then $F_R(r)=\iint_{u<v<u+r}f_{X_{(1)},X_{(n)}}(u,v)\,dv\,du$.<p>Change variable $w=v-u$ ($dv=dw$): $F_R(r)=\int_{-\infty}^{\infty}n f(u)\int_0^r (n-1)f(u+w)[F(u+w)-F(u)]^{n-2}\,dw\,du$.<p>Recognize $\frac{d}{dw}[F(u+w)-F(u)]^{n-1}=(n-1)f(u+w)[F(u+w)-F(u)]^{n-2}$, so the inner integral evaluates to $[F(u+r)-F(u)]^{n-1}$.<p>Hence $F_R(r)=\int_{-\infty}^{\infty}n f(u)[F(u+r)-F(u)]^{n-1}\,du$.
- density of the range: What is $f_R(r)$ for i.i.d. $X_1,\dots,X_n$ with density $f$? ::@:: $f_R(r)=n(n-1)\int_{-\infty}^{\infty} f(u)f(u+r)[F(u+r)-F(u)]^{n-2}\,du$ for $r\ge0$.<p>Derivation: differentiate $F_R(r)=\int_{-\infty}^{\infty}n f(u)[F(u+r)-F(u)]^{n-1}\,du$ under the integral sign: $f_R(r)=\frac{d}{dr}F_R(r)=\int_{-\infty}^{\infty}n f(u)\frac{d}{dr}[F(u+r)-F(u)]^{n-1}\,du$. By the chain rule, $\frac{d}{dr}[F(u+r)-F(u)]^{n-1}=(n-1)[F(u+r)-F(u)]^{n-2}\cdot f(u+r)$.<p>Substituting gives $f_R(r)=n(n-1)\int_{-\infty}^{\infty}f(u)f(u+r)[F(u+r)-F(u)]^{n-2}\,du$.
- range of i.i.d. Exponential variables: What is the distribution of $R$ when $X_i\sim\operatorname{Exp}(\lambda)$ i.i.d.? ::@:: $f_R(r)=(n-1)\lambda e^{-\lambda r}(1-e^{-\lambda r})^{n-2}$ for $r\ge0$, same as the $(n-1)$-th order statistic (max of $n-1$ Exponentials).<p>Derivation: substitute $F(x)=1-e^{-\lambda x}$ and $f(x)=\lambda e^{-\lambda x}$ into $f_R(r)=n(n-1)\int_0^\infty f(u)f(u+r)[F(u+r)-F(u)]^{n-2}\,du$. The integrand becomes $n(n-1)\lambda^2 e^{-\lambda(2u+r)}[e^{-\lambda u}-e^{-\lambda(u+r)}]^{n-2}=n(n-1)\lambda^2 e^{-\lambda n u}e^{-\lambda r}[1-e^{-\lambda r}]^{n-2}$.<p>Integrate over $u$: $\int_0^\infty n(n-1)\lambda^2 e^{-\lambda n u}\,du=n(n-1)\lambda^2\cdot\frac{1}{n\lambda}=(n-1)\lambda$.<p>Multiplying by $e^{-\lambda r}[1-e^{-\lambda r}]^{n-2}$ gives the result.

## covariance and correlation

The covariance measures the linear dependence between two random variables with finite second moments: $$\operatorname{Cov}(X,Y)=E[(X-E[X])(Y-E[Y])]=E[XY]-E[X]E[Y].$$

The correlation coefficient normalizes this to $[-1,1]$: $$\rho(X,Y)=\frac{\operatorname{Cov}(X,Y)}{\sqrt{\operatorname{Var}[X]\operatorname{Var}[Y]}}$$ when both variances are positive, and $\rho(X,Y)=0$ otherwise.

**Properties.**

- Covariance is symmetric and bilinear: $\operatorname{Cov}(a+\sum_i c_iX_i,\;b+\sum_j d_jY_j)=\sum_i\sum_j c_id_j\operatorname{Cov}(X_i,Y_j)$.
- $\operatorname{Var}[X]=\operatorname{Cov}(X,X)$.
- If $X$ and $Y$ are independent, then $\operatorname{Cov}(X,Y)=0$ (the converse is false).
- **Bienaymé formula:** $\operatorname{Var}\bigl(\sum_{i=1}^n X_i\bigr)=\sum_{i=1}^n\operatorname{Var}[X_i]+\sum_{i\neq j}\operatorname{Cov}(X_i,X_j)$.
- $|\rho(X,Y)|\le 1$, with equality $|\rho(X,Y)|=1$ iff $Y=aX+b$ almost surely for some $a\neq 0$. The sign of $\rho$ equals $\operatorname{sgn}(a)$.

**Proof of $|\rho|\le1$.** For any $X,Y$ with finite second moments, $0\le\operatorname{Var}(X/\sqrt{\operatorname{Var}[X]}\pm Y/\sqrt{\operatorname{Var}[Y]})=2(1\pm\rho(X,Y))$, so $\rho(X,Y)\ge-1$ (taking $+$) and $\rho(X,Y)\le1$ (taking $-$). Equality $|\rho|=1$ forces the variance to vanish, hence $X/\sqrt{\operatorname{Var}[X]}\mp Y/\sqrt{\operatorname{Var}[Y]}$ is constant a.s., giving a linear relation $Y=aX+b$.

---

Flashcards for this section are as follows:

- covariance definition: What is $\operatorname{Cov}(X,Y)$? ::@:: $\operatorname{Cov}(X,Y)=E[(X-E[X])(Y-E[Y])]=E[XY]-E[X]E[Y]$.
- correlation coefficient: How is $\rho(X,Y)$ defined? ::@:: $\rho(X,Y)=\operatorname{Cov}(X,Y)/\sqrt{\operatorname{Var}[X]\operatorname{Var}[Y]}$ when both variances are positive, and $0$ otherwise.
- bilinearity of covariance: Write the bilinearity identity for $\operatorname{Cov}(a+\sum c_iX_i,\;b+\sum d_jY_j)$. ::@:: $\operatorname{Cov}(a+\sum c_iX_i,\;b+\sum d_jY_j)=\sum_i\sum_j c_i d_j\operatorname{Cov}(X_i,Y_j)$.
- covariance under independence: If $X$ and $Y$ are independent, is $\operatorname{Cov}(X,Y)=0$? ::@:: Yes, but the converse is false --- zero covariance does not imply independence.
- Bienaymé formula: What is $\operatorname{Var}(\sum_{i=1}^n X_i)$ in terms of covariances? ::@:: $\operatorname{Var}(\sum_{i=1}^n X_i)=\sum_{i=1}^n\operatorname{Var}[X_i]+\sum_{i\neq j}\operatorname{Cov}(X_i,X_j)$.
- correlation bounds: What bounds does $\rho(X,Y)$ satisfy, and when is equality attained? ::@:: $|\rho(X,Y)|\le 1$, with equality iff $Y=aX+b$ almost surely for some $a\neq 0$.
- covariance matrix: What is the covariance matrix of $\boldsymbol X=(X_1,\dots,X_n)$? ::@::$\Sigma=(\operatorname{Cov}(X_i,X_j))_{i,j=1}^n$, symmetric and nonnegative definite, with $\operatorname{Var}[u\cdot\boldsymbol X]=u^\top\Sigma u$.
- proof of correlation bounds $|\rho|\le1$ ::@:: $0\le\operatorname{Var}(X/\sqrt{\operatorname{Var}[X]}\pm Y/\sqrt{\operatorname{Var}[Y]})=2(1\pm\rho(X,Y))$ gives both bounds.
- $\rho=\pm1$ iff linear relation: proof idea ::@:: $\rho=1$ implies $\operatorname{Var}(X/\sqrt{\operatorname{Var}[X]}-Y/\sqrt{\operatorname{Var}[Y]})=0$, so $Y=aX+b$ a.s. with $a>0$; $\rho=-1$ gives $a<0$.

### covariance matrix

For a random vector $\boldsymbol X=(X_1,\dots,X_n)^\top$ with mean vector $\boldsymbol\mu=(\mu_1,\dots,\mu_n)^\top$ where $\mu_i=E[X_i]$, the **covariance matrix** (or variance‑covariance matrix) is the $n\times n$ matrix $\Sigma$ whose $(i,j)$ entry is $\operatorname{Cov}(X_i,X_j)$: $$\Sigma=\bigl(\operatorname{Cov}(X_i,X_j)\bigr)_{i,j=1}^n      =E\bigl[(\boldsymbol X-\boldsymbol\mu)(\boldsymbol X-\boldsymbol\mu)^\top\bigr]      =\begin{pmatrix}        \operatorname{Var}[X_1] & \operatorname{Cov}(X_1,X_2) & \cdots & \operatorname{Cov}(X_1,X_n) \\        \operatorname{Cov}(X_2,X_1) & \operatorname{Var}[X_2] & \cdots & \operatorname{Cov}(X_2,X_n) \\        \vdots & \vdots & \ddots & \vdots \\        \operatorname{Cov}(X_n,X_1) & \operatorname{Cov}(X_n,X_2) & \cdots & \operatorname{Var}[X_n]        \end{pmatrix}.$$

**Properties.**

- **Symmetry:** $\Sigma^\top=\Sigma$ because $\operatorname{Cov}(X_i,X_j)=\operatorname{Cov}(X_j,X_i)$.
- **Positive semidefiniteness:** For any vector $u\in\mathbb R^n$, $u^\top\Sigma u=\operatorname{Var}[u^\top\boldsymbol X]\ge 0$, so $\Sigma$ is symmetric and non‑negative definite (positive semidefinite).
- **Diagonal entries:** $\Sigma_{ii}=\operatorname{Var}[X_i]$, the variance of the $i$-th coordinate.

**Remark.** If $\Sigma$ is singular ($\det\Sigma=0$), there exists $u\neq0$ such that $u^\top\Sigma u=0$, i.e. $\operatorname{Var}[u^\top\boldsymbol X]=0$, so $u^\top\boldsymbol X$ is constant almost surely. This means the components of $\boldsymbol X$ satisfy an almost‑sure linear relation, and the distribution of $\boldsymbol X$ concentrates on an affine subspace of $\mathbb R^n$.

---

Flashcards for this section are as follows:

- covariance matrix properties: What are the key properties of the covariance matrix $\Sigma$ of a random vector $\boldsymbol X$? ::@:: $\Sigma$ is symmetric ($\Sigma^\top=\Sigma$), positive semidefinite ($u^\top\Sigma u\ge0$ for all $u$), and its diagonal entries are variances ($\Sigma_{ii}=\operatorname{Var}[X_i]$). The quadratic form $u^\top\Sigma u=\operatorname{Var}[u^\top\boldsymbol X]$ gives the variance of any linear combination.
- covariance matrix matrix form: How is $\Sigma$ expressed as $E[(\boldsymbol X-\boldsymbol\mu)(\boldsymbol X-\boldsymbol\mu)^\top]$? ::@:: $\Sigma=E[(\boldsymbol X-\boldsymbol\mu)(\boldsymbol X-\boldsymbol\mu)^\top]$ where $\boldsymbol\mu=E[\boldsymbol X]$, with $(i,j)$ entry $\operatorname{Cov}(X_i,X_j)$. This compact form is the outer‑product expectation of the centered random vector.
- singular covariance matrix: What does it mean if $\det\Sigma=0$ for a covariance matrix $\Sigma$? ::@:: A singular covariance matrix means some linear combination $u^\top\boldsymbol X$ has zero variance, so $u^\top\boldsymbol X$ is constant almost surely. This indicates an almost‑sure linear relation among the components of $\boldsymbol X$, whose distribution then concentrates on an affine subspace of $\mathbb R^n$.

## multivariate normal distribution

The multivariate normal (MVN) distribution is the most important joint distribution in statistics. It is defined for a random vector $\boldsymbol X=(X_1,\dots,X_n)^\top$ by its density (when $\Sigma$ is positive definite) or more generally by its characteristic function.

**Definition via density.** For $\boldsymbol X\sim N(\boldsymbol\mu,\Sigma)$ with $\Sigma$ positive definite, the density is $$f_{\boldsymbol X}(\boldsymbol x)=\frac{1}{(2\pi)^{n/2}|\Sigma|^{1/2}}\exp\!\left(-\frac12(\boldsymbol x-\boldsymbol\mu)^\top\Sigma^{-1}(\boldsymbol x-\boldsymbol\mu)\right),$$ where $\boldsymbol\mu\in\mathbb R^n$ is the mean vector and $\Sigma\in\mathbb R^{n\times n}$ is the symmetric positive definite covariance matrix.

**Definition via characteristic function.** For any symmetric nonnegative definite $\Sigma$ (not necessarily full rank), the MVN distribution can be defined by its characteristic function: $$\varphi_{\boldsymbol X}(\boldsymbol t)=E[e^{i\boldsymbol t^\top\boldsymbol X}]=\exp\!\left(i\boldsymbol t^\top\boldsymbol\mu-\frac12\boldsymbol t^\top\Sigma\boldsymbol t\right),\qquad\boldsymbol t\in\mathbb R^n.$$ The real MGF (when it exists) is $M_{\boldsymbol X}(\boldsymbol t)=\exp(\boldsymbol t^\top\boldsymbol\mu+\frac12\boldsymbol t^\top\Sigma\boldsymbol t)$. This definition works even when $\Sigma$ is singular, in which case the distribution is concentrated on an affine subspace.

**Marginals are normal.** Each coordinate of a multivariate normal is univariate normal: $X_i\sim N(\mu_i,\Sigma_{ii})$. More generally, any sub-vector $(X_{i_1},\dots,X_{i_k})$ follows a $k$-dimensional normal with mean $(\mu_{i_1},\dots,\mu_{i_k})$ and covariance $(\Sigma_{ij})_{i,j\in\{i_1,\dots,i_k\}}$. This follows immediately from the MGF: the MGF of the sub-vector is obtained by setting all other $t$ components to $0$, which yields the form $\exp(\boldsymbol t_{sub}^\top\boldsymbol\mu_{sub}+\frac12\boldsymbol t_{sub}^\top\Sigma_{sub}\boldsymbol t_{sub})$.

**Zero covariance implies independence for MVN.** For a multivariate normal vector, if $\operatorname{Cov}(X_i,X_j)=0$ for $i\neq j$, then $X_i$ and $X_j$ are independent. This is unique to the multivariate normal: in general, zero covariance does not imply independence.

**Proof.** If $\Sigma$ is diagonal, the quadratic form in the density exponent becomes $\sum_i (x_i-\mu_i)^2/\Sigma_{ii}$, and the density factorizes as $\prod_i f_{X_i}(x_i)$. Hence the joint density is the product of the marginal densities, which is exactly independence. The same conclusion follows from the MGF: $M_{\boldsymbol X}(\boldsymbol t)=\prod_i\exp(t_i\mu_i+\frac12 t_i^2\Sigma_{ii})$, a product of univariate normal MGFs.

**Linear transformations.** If $\boldsymbol X\sim N(\boldsymbol\mu,\Sigma)$, then for any matrix $A\in\mathbb R^{m\times n}$ and vector $\boldsymbol b\in\mathbb R^m$, $$A\boldsymbol X+\boldsymbol b\sim N(A\boldsymbol\mu+\boldsymbol b,\,A\Sigma A^\top).$$

**Proof (MGF).** The MGF of $A\boldsymbol X+\boldsymbol b$ is $$M_{A\boldsymbol X+\boldsymbol b}(\boldsymbol t)=e^{\boldsymbol t^\top\boldsymbol b}E[e^{\boldsymbol t^\top A\boldsymbol X}]=e^{\boldsymbol t^\top\boldsymbol b}E[e^{(A^\top\boldsymbol t)^\top\boldsymbol X}]=e^{\boldsymbol t^\top\boldsymbol b}\exp\!\bigl((A^\top\boldsymbol t)^\top\boldsymbol\mu+\tfrac12(A^\top\boldsymbol t)^\top\Sigma(A^\top\boldsymbol t)\bigr).$$ Simplifying gives $\exp(\boldsymbol t^\top(A\boldsymbol\mu+\boldsymbol b)+\frac12\boldsymbol t^\top(A\Sigma A^\top)\boldsymbol t)$, which is the MGF of $N(A\boldsymbol\mu+\boldsymbol b,A\Sigma A^\top)$.

**Conditional distributions.** Partition $\boldsymbol X\sim N(\boldsymbol\mu,\Sigma)$ as $$\boldsymbol X=\begin{pmatrix}\boldsymbol X_1\\\boldsymbol X_2\end{pmatrix},\qquad \boldsymbol\mu=\begin{pmatrix}\boldsymbol\mu_1\\\boldsymbol\mu_2\end{pmatrix},\qquad \Sigma=\begin{pmatrix}\Sigma_{11}&\Sigma_{12}\\\Sigma_{21}&\Sigma_{22}\end{pmatrix},$$ where $\boldsymbol X_1$ is $p$-dimensional and $\boldsymbol X_2$ is $q$-dimensional ($p+q=n$). Then the conditional distribution of $\boldsymbol X_1$ given $\boldsymbol X_2=\boldsymbol x_2$ is multivariate normal: $$\boldsymbol X_1\mid\boldsymbol X_2=\boldsymbol x_2\sim N\!\left(\boldsymbol\mu_1+\Sigma_{12}\Sigma_{22}^{-1}(\boldsymbol x_2-\boldsymbol\mu_2),\;\Sigma_{11}-\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}\right),$$ assuming $\Sigma_{22}$ is invertible. The conditional mean is linear in $\boldsymbol x_2$, and the conditional variance does not depend on $\boldsymbol x_2$ (homoscedasticity).

**Proof sketch.** Consider the linear combination $\boldsymbol Y=\boldsymbol X_1-\Sigma_{12}\Sigma_{22}^{-1}\boldsymbol X_2$. By the linear transformation property, $\boldsymbol Y$ is normal. Compute $\operatorname{Cov}(\boldsymbol Y,\boldsymbol X_2)=\Sigma_{12}-\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{22}=0$, so $\boldsymbol Y$ and $\boldsymbol X_2$ are independent (zero covariance for MVN). Then $E[\boldsymbol X_1\mid\boldsymbol X_2]=\Sigma_{12}\Sigma_{22}^{-1}\boldsymbol X_2+E[\boldsymbol Y]$, and $\operatorname{Var}[\boldsymbol X_1\mid\boldsymbol X_2]=\operatorname{Var}[\boldsymbol Y]$. Substituting the explicit expressions yields the formulas above.

---

Flashcards for this section are as follows:

- MVN density definition: What is the density of $\boldsymbol X\sim N(\boldsymbol\mu,\Sigma)$ when $\Sigma$ is positive definite? ::@:: $f_{\boldsymbol X}(\boldsymbol x)=\frac{1}{(2\pi)^{n/2}|\Sigma|^{1/2}}\exp(-\frac12(\boldsymbol x-\boldsymbol\mu)^\top\Sigma^{-1}(\boldsymbol x-\boldsymbol\mu))$.
- MVN characteristic function: What is $\varphi_{\boldsymbol X}(\boldsymbol t)$ for $\boldsymbol X\sim N(\boldsymbol\mu,\Sigma)$? ::@:: $\varphi_{\boldsymbol X}(\boldsymbol t)=\exp(i\boldsymbol t^\top\boldsymbol\mu-\frac12\boldsymbol t^\top\Sigma\boldsymbol t)$.
- MVN MGF: What is $M_{\boldsymbol X}(\boldsymbol t)$ for $\boldsymbol X\sim N(\boldsymbol\mu,\Sigma)$? ::@:: $M_{\boldsymbol X}(\boldsymbol t)=\exp(\boldsymbol t^\top\boldsymbol\mu+\frac12\boldsymbol t^\top\Sigma\boldsymbol t)$.
- MVN marginals are normal: What can you say about the distribution of a sub-vector of a multivariate normal? ::@:: Any sub-vector is also multivariate normal with the corresponding mean and covariance sub-matrix.
- zero covariance implies independence in MVN: If $X_i$ and $X_j$ are components of a multivariate normal with $\operatorname{Cov}(X_i,X_j)=0$, are they independent? ::@:: Yes — for the MVN, zero covariance implies independence, because the density or MGF factorizes when $\Sigma$ is diagonal.
- linear transformations preserve MVN: If $\boldsymbol X\sim N(\boldsymbol\mu,\Sigma)$, what is the distribution of $A\boldsymbol X+\boldsymbol b$? ::@:: $A\boldsymbol X+\boldsymbol b\sim N(A\boldsymbol\mu+\boldsymbol b,\,A\Sigma A^\top)$.
- conditional distribution in MVN: Partition $\boldsymbol X\sim N(\boldsymbol\mu,\Sigma)$ into $(\boldsymbol X_1,\boldsymbol X_2)$. What is $\boldsymbol X_1\mid\boldsymbol X_2=\boldsymbol x_2$? ::@:: $\boldsymbol X_1\mid\boldsymbol X_2=\boldsymbol x_2\sim N(\boldsymbol\mu_1+\Sigma_{12}\Sigma_{22}^{-1}(\boldsymbol x_2-\boldsymbol\mu_2),\;\Sigma_{11}-\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21})$.
- conditional mean of MVN is linear ::@:: In a multivariate normal, $E[\boldsymbol X_1\mid\boldsymbol X_2=\boldsymbol x_2]=\boldsymbol\mu_1+\Sigma_{12}\Sigma_{22}^{-1}(\boldsymbol x_2-\boldsymbol\mu_2)$, which is linear in $\boldsymbol x_2$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- conditional variance of MVN is constant ::@:: In a multivariate normal, $\operatorname{Var}[\boldsymbol X_1\mid\boldsymbol X_2]=\Sigma_{11}-\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}$, which does not depend on the conditioning value. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- MVN conditional proof via uncorrelated linear combination ::@:: Set $\boldsymbol Y=\boldsymbol X_1-\Sigma_{12}\Sigma_{22}^{-1}\boldsymbol X_2$; then $\operatorname{Cov}(\boldsymbol Y,\boldsymbol X_2)=0$, so $\boldsymbol Y\perp\boldsymbol X_2$ for MVN, yielding the conditional formulas. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## triangle law and Buffon's needle

**Uniform law on a triangle.** Let $(X,Y)$ be uniform on $A=\{(x,y):0\le x\le 1,\ 0\le y\le 1-x\}$. Since the area of $A$ is $1/2$, the density is $f_{X,Y}(x,y)=2\mathbf 1_A(x,y)$. Marginalization gives $f_X(x)=\int_0^{1-x}2\,dy=2(1-x)$ for $0\le x\le 1$, and the same formula for $f_Y$ by symmetry. The coordinates are not independent because the support is triangular rather than rectangular. Indeed, the product $f_X(x)f_Y(y)$ is positive on much of the square $[0,1]^2$, whereas the joint density vanishes whenever $x+y>1$.

**Buffon's needle.** A plane is ruled with parallel lines spaced distance $a>0$ apart. A needle of length $\ell$ (with $\ell<a$) is dropped at random onto the plane. What is the probability that the needle crosses a line?

**Random variables.** Let $X$ be the distance from the needle's midpoint to the nearest line, and let $\Theta$ be the acute angle between the needle and the direction perpendicular to the lines — equivalently, the angle relative to the line normal. By the symmetry of the dropping mechanism, $X$ and $\Theta$ are independent and uniformly distributed: $$X\sim U\!\left(\left[0,\frac{a}{2}\right]\right),\qquad \Theta\sim U([0,\pi]),$$

so the joint density is constant on the rectangle $[0,a/2]\times[0,\pi]$: $$f_{X,\Theta}(x,\theta)=\frac{2}{a}\cdot\frac{1}{\pi}=\frac{2}{\pi a}.$$

**Hit condition.** The needle crosses a line exactly when the projection of half its length in the perpendicular direction exceeds the distance to the line: $$\frac{\ell}{2}\sin\Theta\ge X.$$

**Probability computation.** The event is a region under the curve $x\le\frac{\ell}{2}\sin\theta$. Because the joint density is constant, the probability is $2/(\pi a)$ times the area of that region: $$\begin{aligned} P[\text{hit}]&=\int_{\theta=0}^{\pi}\int_{x=0}^{\frac{\ell}{2}\sin\theta}\frac{2}{\pi a}\,dx\,d\theta\\ &=\frac{2}{\pi a}\int_{0}^{\pi}\frac{\ell}{2}\sin\theta\,d\theta\\ &=\frac{\ell}{\pi a}\int_{0}^{\pi}\sin\theta\,d\theta =\frac{\ell}{\pi a}\bigl[-\cos\theta\bigr]_{0}^{\pi} =\frac{2\ell}{\pi a}. \end{aligned}$$

**Interpretation.** This is a model example of geometric probability: a joint uniform distribution turns a probability question into a normalized area computation. The formula $P[\text{hit}]=2\ell/(\pi a)$ is historically notable because it provides a Monte Carlo method for estimating $\pi$: repeat the experiment many times, record the fraction of hits $h$, and solve $\pi\approx 2\ell/(a h)$. For $\ell>a$ the calculation is more involved (the integration region must account for multiple crossings).

---

Flashcards for this section are as follows:

- uniform law on a triangle: If $(X,Y)$ is uniform on $\{(x,y):0\le x\le 1,\ 0\le y\le 1-x\}$, what is the density? ::@:: The density is $f_{X,Y}(x,y)=2\mathbf 1_A(x,y)$ because the triangle has area $1/2$.
- Buffon's needle model: Describe the random variables and their joint density in the standard model. ::@:: $X$ = distance from needle midpoint to nearest line, $X\sim U([0,a/2])$; $\Theta$ = acute angle between needle and line normal, $\Theta\sim U([0,\pi])$; $X\perp\Theta$, so $f_{X,\Theta}(x,\theta)=2/(\pi a)$ on $[0,a/2]\times[0,\pi]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Buffon's needle hit condition: Express the crossing event in terms of $X$, $\Theta$, and $\ell$ (with $\ell<a$). ::@:: The needle crosses a line when $\frac{\ell}{2}\sin\Theta\ge X$: the projection of half the needle onto the line normal exceeds the distance to the nearest line.
- Buffon's needle probability computation: Set up and evaluate $P[\text{hit}]$ for the standard model. ::@:: $P[\text{hit}]=\int_0^{\pi}\int_0^{\frac{\ell}{2}\sin\theta}\frac{2}{\pi a}\,dx\,d\theta=\frac{2}{\pi a}\int_0^{\pi}\frac{\ell}{2}\sin\theta\,d\theta=\frac{2\ell}{\pi a}$ (probability equals area under $\frac{\ell}{2}\sin\theta$ scaled by the constant joint density).
- Buffon's needle result: What is $P[\text{hit}]$ when $\ell<a$ and why is it significant? ::@:: $P[\text{hit}]=2\ell/(\pi a)$. It is a landmark example of geometric probability (probability = normalized area in the $(X,\Theta)$ plane) and yields a Monte Carlo estimate for $\pi$: $\pi\approx 2\ell N/(a H)$ after $N$ drops with $H$ hits.
- Buffon's needle as Monte Carlo: How is Buffon's needle used to estimate $\pi$? ::@:: Drop the needle $N$ times, count hits $H$. From $P[\text{hit}]=2\ell/(\pi a)$, solving gives $\pi\approx 2\ell N/(a H)$. The estimate converges slowly but is historically important as a pre-computer Monte Carlo method.
- marginal of uniform triangle: If $(X,Y)$ is uniform on $\{(x,y):0\le x\le 1,\ 0\le y\le 1-x\}$, what is $f_X(x)$? ::@:: $f_X(x)=2(1-x)$ for $0\le x\le 1$, by integrating $f_{X,Y}(x,y)=2$ over $y$ from $0$ to $1-x$.
- dependence from triangular support: Why are $X$ and $Y$ dependent in the $(0,0)-(1,0)-(0,1)$ triangle example? ::@:: The product $f_X(x)f_Y(y)$ is positive where $x+y>1$, but the joint density vanishes there, so $f_{X,Y}\ne f_Xf_Y$.
