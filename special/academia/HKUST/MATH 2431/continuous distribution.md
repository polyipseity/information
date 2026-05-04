---
aliases:
  - continuous distribution
  - continuous distributions
  - probability density function
  - probability density functions
tags:
  - flashcard/active/special/academia/HKUST/MATH_2431/continuous_distribution
  - language/in/English
---

# continuous distribution

A continuous distribution, in the density-based sense used here, is an absolutely continuous probability measure on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$. Here _absolutely continuous_ means that Lebesgue-null sets have probability $0$: if $\lambda(A)=0$, then $\mu(A)=0$. In contrast with discrete laws, probabilities are assigned to intervals by integration and single points have probability $0$. The associated cumulative distribution functions are treated separately in [cumulative distribution function](cumulative%20distribution%20function.md).

More naturally phrased: specifying an absolutely continuous probability measure is equivalent to specifying a probability density function, up to almost-everywhere equality. The derivation can be written in a very concrete course-level way.

Starting from a PDF $f\ge0$ with $\int_{-\infty}^{\infty}f(x)\,dx=1$, define interval probabilities by $\mu_f((a,b])=\int_a^b f(x)\,dx$. By additivity of the integral, these values are compatible with disjoint unions of half-open intervals, and the total mass is $1$. So they determine a probability measure on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$, still denoted by $\mu_f$, satisfying $\mu_f(A)=\int_A f\,d\lambda$ for Borel sets $A$.

Conversely, start from an absolutely continuous probability measure $\mu$ and let $F(x)=\mu(( -\infty,x])$ be its cumulative distribution function. In this case the corresponding CDF is absolutely continuous, so there exists an integrable function $f\ge0$ such that $F(x)=\int_{-\infty}^x f(t)\,dt$ for all $x$. Then for every $a<b$, $\mu((a,b])=F(b)-F(a)=\int_a^b f(x)\,dx$. Thus the density recovers the measure on all half-open intervals, and those intervals generate $\mathcal{B}(\mathbb{R})$, so they recover the whole measure. This also explains why densities are determined only almost everywhere: if two functions give the same interval integrals, then they define the same probability measure.

---

Flashcards for this section are as follows:

- overview ::@:: In the density-based sense, a continuous distribution is an absolutely continuous probability measure on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$; it assigns probabilities to intervals by integration against a probability density function. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-13,17,315!2026-05-13,17,315-->
- absolutely continuous probability measure ::@:: A probability measure $\mu$ on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$ is absolutely continuous if $\lambda(A)=0$ implies $\mu(A)=0$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-14,17,315!2026-05-11,15,298-->
- absolutely continuous probability measures versus PDFs ::@:: Specifying an absolutely continuous probability measure is equivalent to specifying a probability density function, up to almost-everywhere equality. <!--SR:!2026-05-13,16,298!2026-05-13,16,298-->
- derivation of absolutely continuous probability measure-PDF correspondence ::@:: Forward direction: from a PDF $f$, define $\mu_f((a,b])=\int_a^b f(x)\,dx$, hence a probability measure. Reverse direction: from an absolutely continuous probability measure $\mu$ with CDF $F$, absolute continuity of $F$ gives a function $f\ge0$ with $F(x)=\int_{-\infty}^x f(t)\,dt$, so $\mu((a,b])=F(b)-F(a)=\int_a^b f(x)\,dx$. Since half-open intervals generate $\mathcal{B}(\mathbb{R})$, the two constructions are inverse up to almost-everywhere equality of densities. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-10,14,290!2026-05-14,17,315-->

## probability density functions

A function $f \colon \mathbb{R} \to [0,\infty)$ is a _probability density function_ if it is measurable and satisfies $\int_{-\infty}^{\infty} f(x)\,dx = 1$. The guiding idea is that a small interval $[a,b)$ should have probability approximately equal to the area under the graph of $f$ over that interval, and in the exact model we define $P[[a,b)] = \int_a^b f(x)\,dx$ for every $a < b$. By additivity over disjoint intervals and the normalization condition on $f$, this determines a unique probability measure on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$.

The intuition is that the density is not itself a probability at a point; rather, it is a rate of probability per unit length. That is why values of $f(x)$ may exceed $1$ without contradiction, while the integral over the whole line must equal $1$. For a short interval of width $\Delta x$, the probability is approximately $f(x)\,\Delta x$, so one should think of density as describing how probability mass is spread continuously rather than atom by atom.

The lecture introduced this idea through a minibus-arrival example. Suppose the arrival time is uniformly distributed between 1 PM and 1:15 PM, and normalize this time window to $[0,1)$. If we split $[0,1)$ into $n$ half-open intervals $[j/n,(j+1)/n)$ of equal length, then each interval should have probability $1/n$. For $0 \le a < b < 1$, this suggests $P[[a,b)] \approx \sum_{a\le j/n < b} 1/n$, and as the partition gets finer this Riemann sum tends to $\int_a^b 1\,dx$. So the constant density $f(x)=1$ on $[0,1)$ is the continuous analogue of equally likely outcomes in a finite partition.

The same example also shows how non-constant densities arise. If the minibus is more likely to arrive near 1:15 PM than near 1 PM, then the rightmost partition intervals should receive larger probabilities than the leftmost ones. A simple way to encode that is to make the interval $[j/n,(j+1)/n)$ receive probability proportional to its position index $j$, namely $2j/(n(n-1))$ for $0 \le j \le n-1$. This really is a probability distribution because $\sum_{j=0}^{n-1}\frac{2j}{n(n-1)}=\frac{2}{n(n-1)}\sum_{j=0}^{n-1}j=\frac{2}{n(n-1)}\cdot\frac{n(n-1)}{2}=1$.

For $0 \le a < b < 1$, the interval probability is then approximated by $P[[a,b)]\approx\sum_{a\le j/n < b}\frac{2j}{n(n-1)}\approx\sum_{a\le j/n < b}2\bigl(\frac{j}{n}\bigr)\frac1n\to\int_a^b 2x\,dx$. So the density $f(x)=2x$ on $[0,1)$ is not a mysterious formula pulled from nowhere: it is the continuous limit of the rule "intervals farther to the right get proportionally larger weights."

---

Flashcards for this section are as follows:

- probability density function ::@:: A probability density function is a measurable map $f\colon\mathbb{R}\to[0,\infty)$ with $\int_{-\infty}^{\infty} f(x)\,dx = 1$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-14,17,315!2026-05-14,17,315-->
- interval probability from density ::@:: If a probability measure is characterized by a density $f$, then $P[[a,b)] = \int_a^b f(x)\,dx$ for every $a < b$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-13,17,315!2026-05-13,17,315-->
- density versus point probability ::@:: A density value $f(x)$ is not the probability of the single point $x$; it is probability per unit length, so probabilities arise only after integrating over intervals. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-11,15,298!2026-05-13,16,298-->
- why a density may exceed $1$ ::@:: A density may be larger than $1$ because only its integral must equal $1$; pointwise values describe concentration, not direct probabilities. <!--SR:!2026-05-13,17,315!2026-05-12,16,298-->
- minibus example with uniform arrival on $[0,1)$ ::@:: If the 1 PM–1:15 PM window is normalized to $[0,1)$ and split into intervals $[j/n,(j+1)/n)$ of equal length, assigning each interval probability $1/n$ leads to $P[[a,b)]\approx \sum_{a\le j/n < b}1/n \to \int_a^b 1\,dx$, so the motivating density is $f(x)=1$ on $[0,1)$. <!--SR:!2026-05-11,15,298!2026-05-13,16,298-->
- minibus example with later arrivals favored ::@:: In the non-uniform minibus model, interval $[j/n,(j+1)/n)$ is weighted by its position index $j$, so its probability is $2j/(n(n-1))$. These weights sum to $1$ because $\sum_{j=0}^{n-1}j=n(n-1)/2$. As $n\to\infty$, the index ratio $j/n$ becomes the continuous position $x$, so $\sum 2(j/n)(1/n)\to\int_a^b 2x\,dx$. Thus the increasing density $f(x)=2x$ is the continuous limit of "intervals farther right are more likely." <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-14,17,315!2026-05-13,17,315-->
- why the minibus examples motivate densities ::@:: Both minibus models follow the same two-step idea: first assign probabilities to intervals in a fine partition, then let the mesh size go to $0$. In that limit the discrete weighted sum becomes an integral $\int f(x)\,dx$, and the function $f$ records how those interval weights were distributed. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-13,17,315!2026-05-10,14,298-->

## interval probabilities

A probability measure $P$ on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ is called _continuous_ if it is characterized by a density $f$, meaning $P[A] = \int_A f(x)\,dx$ for Borel sets $A$. Then for every $a \in \mathbb{R}$ one has $P[\{a\}] = 0$, and if $a<b$ then

- $P[[a,b]] = P[(a,b]] = P[(a,b)] = \int_a^b f(x)\,dx$,
- $P[(-\infty,a]] = P[(-\infty,a)] = \int_{-\infty}^a f(x)\,dx$,
- $P[[a,\infty)] = P[(a,\infty)] = \int_a^{\infty} f(x)\,dx$.

The proof begins with the singleton claim. Let $\varepsilon>0$. Since $\{a\}\subseteq [a,a+\varepsilon)$, we have $P[\{a\}]\le P[[a,a+\varepsilon)] = \int_a^{a+\varepsilon} f(x)\,dx$. If $f$ is continuous at $a$, then this last integral clearly tends to $0$ as $\varepsilon\downarrow 0$. The same conclusion still holds without continuity at $a$: for example, one may allow an integrable blow-up such as $f(x)=\frac{1}{2\sqrt{x}}\mathbf{1}_{(0,1]}(x)$ at $a=0$. In general, because $f\ge 0$ is integrable on every bounded interval, the tail integral $\int_{a+\varepsilon}^{a+1} f(x)\,dx$ increases to $\int_a^{a+1} f(x)\,dx$ as $\varepsilon\downarrow 0$. If we write $c:=\int_a^{a+1} f(x)\,dx$, then

- $\int_{a+\varepsilon}^{a+1} f(x)\,dx \uparrow c$ as $\varepsilon\downarrow 0$,
- and $\int_a^{a+\varepsilon} f(x)\,dx = c - \int_{a+\varepsilon}^{a+1} f(x)\,dx$.

Therefore the small-interval integral must go to $0$. So even if $f(x)$ becomes very large near $a$, the total area over a shrinking interval $[a,a+\varepsilon)$ still vanishes, which is exactly what we need to conclude $P[\{a\}]=0$.

Once point masses vanish, the other identities are immediate from set decompositions. For instance, $[a,b] = \{a\}\cup(a,b]$ and $(a,b] = (a,b)\cup\{b\}$, so all three interval probabilities are equal because adding or removing finitely many singleton endpoints changes the probability by $0$. The half-line formulas follow the same way from $(-\infty,a] = (-\infty,a)\cup\{a\}$ and $[a,\infty) = \{a\}\cup(a,\infty)$.

This is the key contrast with discrete distributions. In a discrete model, individual points contribute positive masses that must be added up. In a continuous model, intervals matter and isolated points do not. The formulas above explain why continuous probabilities are insensitive to endpoint conventions: the difference between closed, open, and half-open intervals is only finitely many singleton sets, each of which has probability $0$.

Returning to the minibus example, once we pass from the finite partition model to the density description, it becomes unnatural to ask for the probability of arrival at one exact instant. In the uniform case on $[0,1)$ the probability of arriving during a short interval is approximately its length, but the probability of any single point is $0$. In the increasing-density case $f(x)=2x$ on $[0,1)$, intervals near 1:15 PM are more likely than intervals near 1 PM, yet any exact arrival time still has probability $0$. This is the basic intuition behind continuous distributions: probability is spread over intervals, not stored at isolated points.

---

Flashcards for this section are as follows:

- definition via a density ::@:: A continuous distribution on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ is a probability measure characterized by a density $f$, so probabilities are computed by integrating $f$ over Borel sets. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-13,17,315!2026-05-13,16,298-->
- point mass in continuous distribution ::@:: If $P$ is characterized by a density, then $P[\{a\}] = 0$ for every $a \in \mathbb{R}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-14,17,315!2026-05-12,16,298-->
- interval endpoints do not matter ::@:: For a continuous distribution and $a < b$, one has $P[[a,b]] = P[(a,b]] = P[(a,b)] = \int_a^b f(x)\,dx$, because adding or removing finitely many endpoints changes probability by $0$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-14,17,315!2026-05-11,15,298-->
- left half-line probability ::@:: For a continuous distribution with density $f$, one has $P[(-\infty,a]] = P[(-\infty,a)] = \int_{-\infty}^a f(x)\,dx$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-13,17,315!2026-05-13,17,315-->
- right half-line probability ::@:: For a continuous distribution with density $f$, one has $P[[a,\infty)] = P[(a,\infty)] = \int_a^{\infty} f(x)\,dx$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-10,14,298!2026-05-13,17,315-->
- proof that singletons have probability zero ::@:: For $\varepsilon>0$, $\{a\}\subseteq[a,a+\varepsilon)$ gives $P[\{a\}]\le \int_a^{a+\varepsilon} f(x)\,dx$; this integral tends to $0$ as $\varepsilon\downarrow 0$, so $P[\{a\}]=0$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-13,16,298!2026-05-14,17,315-->
- why the singleton proof still works when $f$ blows up at an endpoint ::@:: Even if $f$ is unbounded near $a$, integrability of $f\ge 0$ implies the tail integrals $\int_{a+\varepsilon}^{a+1} f(x)\,dx$ increase to $\int_a^{a+1} f(x)\,dx$, so $\int_a^{a+\varepsilon} f(x)\,dx = \int_a^{a+1} f(x)\,dx - \int_{a+\varepsilon}^{a+1} f(x)\,dx \to 0$; for example $f(x)=\frac{1}{2\sqrt{x}}\mathbf{1}_{(0,1]}(x)$ is unbounded at $0$ but still integrable. <!--SR:!2026-05-13,16,290!2026-05-10,14,298-->
- continuous versus discrete viewpoint ::@:: In a discrete law, probabilities are assembled from point masses; in a continuous law, isolated points have probability $0$ and interval probabilities are obtained by integration. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-13,16,298!2026-05-13,17,315-->
- minibus example and point probabilities ::@:: In the non-uniform minibus model with density $f(x)=2x$, rightward intervals are more likely because the density is larger on the right, but any one exact arrival time still has probability $0$. Continuous distributions spread probability across intervals, not individual points. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-12,16,298!2026-05-10,14,298-->
- minibus example and interval comparison ::@:: In the non-uniform minibus model with density $f(x)=2x$, intervals farther to the right get larger probability because $\int_s^t 2x\,dx$ grows when the whole interval is shifted rightward. This is the continuous version of the original discrete rule that gave larger weights to larger indices $j$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-10,14,290!2026-05-14,17,315-->

## exponential and normal laws

Two especially important examples of continuous distributions are the exponential and normal laws. They illustrate two recurring themes: the exponential distribution models waiting times and is characterized by memorylessness, while the normal distribution models bell-shaped fluctuations around a center and is the canonical continuous law in probability and statistics.

---

Flashcards for this section are as follows:

- continuous distributions / example overview ::@:: Two fundamental examples of continuous distributions are the exponential distribution, which models waiting times, and the normal distribution, which models bell-shaped fluctuations around a center. <!--SR:!2026-05-11,15,290!2026-05-13,16,298-->
- exponential versus normal distribution ::@:: The exponential law is distinguished by memorylessness, whereas the normal law is distinguished by its symmetric bell-shaped density centered at $\mu$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-14,17,315!2026-05-12,16,298-->

### uniform distribution

For $a<b$, the uniform distribution on $[a,b]$ is the continuous distribution with constant density $f(x)=\frac{1}{b-a}\mathbf{1}_{[a,b]}(x)$. Thus every interval of a given length inside $[a,b]$ has the same probability, and for $a\le s<t\le b$ one has $P[[s,t)] = \frac{t-s}{b-a}$. This is the continuous analogue of equally likely outcomes on a finite sample space: probability is spread evenly across the whole interval.

The lecture's minibus example is exactly of this type after normalization. If the arrival time is uniform on the 15-minute window from 1:00 PM to 1:15 PM, then after rescaling that window to $[0,1)$ the density is simply $f(x)=1$ on $[0,1)$. So interval probabilities are proportional to length, which is why the corresponding Riemann sums converge to $\int_a^b 1\,dx$.

---

Flashcards for this section are as follows:

- uniform distribution on $[a,b]$ ::@:: For $a<b$, the uniform distribution on $[a,b]$ has density $f(x)=\frac{1}{b-a}\mathbf{1}_{[a,b]}(x)$. <!--SR:!2026-05-13,16,298!2026-05-13,16,298-->
- uniform interval probability on $[a,b]$: If $X$ is uniform on $[a,b]$ and $a\le s<t\le b$, what is $P[[s,t)]$? ::@:: $P[[s,t)] = \frac{t-s}{b-a}$; probability is proportional to interval length. <!--SR:!2026-05-13,16,298!2026-05-13,17,315-->
- intuition for the uniform distribution ::@:: A uniform distribution spreads probability evenly across an interval, so intervals of equal length have equal probability. <!--SR:!2026-05-13,16,298!2026-05-12,16,298-->
- minibus example as a uniform distribution ::@:: In the normalized minibus-arrival model on $[0,1)$, the density is $f(x)=1$, so the law is the uniform distribution on $[0,1)$ and interval probabilities equal interval lengths. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-13,16,298!2026-05-14,17,315-->

### exponential distribution

For $\lambda > 0$, the _exponential distribution_ $\mathrm{E}(\lambda)$ has density $f(x) = \lambda e^{-\lambda x}\mathbf{1}_{[0,\infty)}(x)$, that is, $f(x)=\lambda e^{-\lambda x}$ for $x\ge 0$ and $f(x)=0$ for $x<0$. It is a valid density because $\int_{-\infty}^{\infty} f(x)\,dx = \int_0^{\infty} \lambda e^{-\lambda x}\,dx = 1$. A standard interpretation is waiting time: the lifetime of a radioactive isotope or the waiting time until a random event occurs is often modeled by an exponential law.

Its most distinctive property is _memorylessness_. If $X \sim \mathrm{E}(\lambda)$ and $s,t \ge 0$, then $P[X > s+t \mid X > s] = P[X > t]$. The intuition is that once one already knows the process has survived until time $s$, the remaining waiting time behaves as if one were starting afresh. This makes the exponential distribution the continuous analogue of the geometric distribution's lack-of-memory property.

---

Flashcards for this section are as follows:

- exponential distribution ::@:: For $\lambda > 0$, the exponential distribution $\mathrm{E}(\lambda)$ has density $f(x)=\lambda e^{-\lambda x}\mathbf{1}_{[0,\infty)}(x)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-10,14,298!2026-05-12,16,298-->
- why the exponential density integrates to $1$ ::@:: The exponential density is valid because $\int_0^{\infty} \lambda e^{-\lambda x}\,dx = 1$. <!--SR:!2026-05-10,14,298!2026-05-13,17,315-->
- exponential distribution interpretation ::@:: The exponential distribution is a standard model for waiting times or lifetimes, such as radioactive decay times. <!--SR:!2026-05-13,17,315!2026-05-12,16,298-->
- memoryless property ::@:: If $X\sim \mathrm{E}(\lambda)$ and $s,t\ge 0$, then $P[X>s+t\mid X>s]=P[X>t]$; surviving up to time $s$ does not change the distribution of the remaining waiting time. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-13,17,315!2026-05-11,15,298-->
- exponential versus geometric memorylessness ::@:: The exponential distribution is the continuous analogue of the geometric distribution because both are characterized by a memoryless property. <!--SR:!2026-05-13,16,298!2026-05-12,16,298-->

### normal distribution

For parameters $\mu \in \mathbb{R}$ and $\sigma^2 > 0$, the _normal distribution_ $\mathrm{N}(\mu, \sigma^2)$ has density $f(x) = \dfrac{1}{\sqrt{2\pi\sigma^2}}\exp\!\left(-\dfrac{(x-\mu)^2}{2\sigma^2}\right)$. Here $\mu$ is the center of the bell curve and $\sigma^2$ controls its spread. The standard normal distribution is the special case $\mathrm{N}(0,1)$ with density $\varphi(x) = \dfrac{1}{\sqrt{2\pi}}e^{-x^2/2}$.

The normal density is symmetric about $\mu$, concentrated more tightly when $\sigma$ is small, and more spread out when $\sigma$ is large. Because the integral of the Gaussian density over the real line is $1$, it defines a probability measure. The associated cumulative distribution function and the standard notation $\Phi$ are discussed in [cumulative distribution function](cumulative%20distribution%20function.md).

---

Flashcards for this section are as follows:

- normal distribution ::@:: The normal distribution $\mathrm{N}(\mu,\sigma^2)$ has density $f(x)=\dfrac{1}{\sqrt{2\pi\sigma^2}}\exp\!\left(-\dfrac{(x-\mu)^2}{2\sigma^2}\right)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-12,16,298!2026-05-11,15,290-->
- role of $\mu$ and $\sigma^2$ ::@:: In $\mathrm{N}(\mu,\sigma^2)$, $\mu$ is the center of the bell curve and $\sigma^2$ controls its spread. <!--SR:!2026-05-13,17,315!2026-05-13,16,298-->
- standard normal density ::@:: The standard normal distribution $\mathrm{N}(0,1)$ has density $\varphi(x)=\dfrac{1}{\sqrt{2\pi}}e^{-x^2/2}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-10,14,298!2026-05-13,16,298-->

<!-- check: ignore-next-line[header_style]: proper noun -->
### Cauchy distribution

For a location parameter $m\in\mathbb{R}$ and scale parameter $a>0$, the _Cauchy distribution_ has density $f(x)=\dfrac{1}{\pi}\dfrac{a}{a^2+(x-m)^2}$ on $\mathbb{R}$.

In the centered case $m=0$, this becomes $f(x)=\dfrac{a}{\pi(a^2+x^2)}$. The tutorial derived this law from a simple geometry model: if a light source sits at distance $a$ from a line, emits rays with angle $\theta\sim\mathrm{U}((-\pi/2,\pi/2))$, and $X=a\tan\theta$ records the hit position on the line, then $X$ has exactly this density. The reason is that the inverse map is $\theta=\arctan(x/a)$ and the derivative factor is $\dfrac{d}{dx}\arctan(x/a)=\dfrac{a}{a^2+x^2}$.

This example is a good reminder that not all familiar continuous laws are bell-shaped or exponentially decaying. The Cauchy density has much heavier tails than the normal density because the tangent map blows up near $\pm\pi/2$: angles close to parallel with the line create very large displacements.

---

Flashcards for this section are as follows:

- Cauchy distribution ::@:: For location $m\in\mathbb{R}$ and scale $a>0$, the Cauchy distribution has density $f(x)=\dfrac{1}{\pi}\dfrac{a}{a^2+(x-m)^2}$ on $\mathbb{R}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-13,17,315!2026-05-13,16,298-->
- centered Cauchy distribution ::@:: In the centered case $m=0$, the Cauchy density is $f(x)=\dfrac{a}{\pi(a^2+x^2)}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-07,10,270!2026-05-13,16,290-->
- light-source model for the Cauchy law ::@:: If $\theta\sim\mathrm{U}((-\pi/2,\pi/2))$ and $X=a\tan\theta$, then $X$ has the centered Cauchy density $f(x)=\dfrac{a}{\pi(a^2+x^2)}$. The derivation is: write $X=a\tan\theta$, invert as $\theta=\arctan(x/a)$, compute the CDF $F_X(x)=P(\theta\le\arctan(x/a))=\dfrac{\arctan(x/a)+\pi/2}{\pi}$, and differentiate to get $f_X(x)=F_X'(x)=\dfrac{a}{\pi(a^2+x^2)}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-13,16,298!2026-05-13,16,298-->
- light-source model derivation for the Cauchy law ::@:: Step 1: use the monotone change of variables $x=a\tan\theta$ with inverse $\theta(x)=\arctan(x/a)$. Step 2: CDF route gives $F_X(x)=P(\theta\le\theta(x))$ and then differentiate. Step 3 (alternative): apply change-of-variables density formula directly, $f_X(x)=f_\Theta(\theta(x))\left|\frac{d\theta}{dx}\right|$ with $f_\Theta=1/\pi$ and $\frac{d\theta}{dx}=\frac{a}{a^2+x^2}$, yielding $f_X(x)=\frac{a}{\pi(a^2+x^2)}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-14,17,315!2026-05-13,16,298-->
- heavy tails of the Cauchy law ::@:: The Cauchy density has heavy tails because $\tan\theta$ blows up near $\pm\pi/2$, so small angular changes near grazing rays produce very large spatial displacements. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-11,15,298!2026-05-14,17,315-->
