---
aliases:
  - PR
  - PageRank
tags:
  - flashcard/active/general/PageRank
  - language/in/English
---

# PageRank

## algorithm

The PageRank algorithm outputs {{a [probability distribution](probability%20distribution.md) representing the likelihood of a person randomly clicking on links would arrive at any particular page}}. <!--SR:!2025-01-29,172,310-->

The probability is expressed as {{a numeric value between 0 and 1}}. <!--SR:!2025-07-04,297,330-->

### simplified algorithm

Assume there are {{$N$ pages $p_1, \ldots, p_N$ and links between them}} to consider. {{Links that connect a page to itself}} may be discarded, and usually are, so that {{a page cannot artificially increase its own PageRank by linking to itself}}. Define {{$\operatorname{PR}_t(p)$ to be the PageRank of page $p$ at time $t$}}. Define {{$L(p)$ to be the number of links outgoing from $p$}}. Define {{$B(p)$ to be the set of pages linking to page $p$}}. <!--SR:!2025-04-28,243,330!2025-03-28,218,330!2025-06-16,280,330!2025-06-15,278,330!2025-01-21,152,290!2025-01-08,142,290-->

Earlier versions of PageRank initialize {{all PageRank to $1$, i.e. $\operatorname{PR}_0(p_i) = 1 \quad \forall i \in \set{1, \ldots, N}$}}. This however, means {{the probability is the PageRank divided by the number of pages}}. Later versions, and thereafter in this section, initialize {{all PageRank to $1 / N$, i.e. $\operatorname{PR}_0(p_i) = 1 / N \quad \forall i \in \set{1, \ldots, N}$}}, so that {{adding all PageRanks together results in 1, making the probability directly equal to the PageRank}}. <!--SR:!2024-10-15,88,290!2024-10-13,86,290!2024-12-11,121,290!2025-01-23,166,310-->

On each iteration, the PageRank of each page is {{divided equally among the outbound links and given to them}}. Mathematically, {{$$\operatorname{PR}_t(p) = \sum_{r \in B(p)} \frac {\operatorname{PR}_{t - 1}(r)} {L(r)}$$}}. <!--SR:!2025-03-05,200,310!2024-12-16,126,290-->

The above operation can also be represented {{using vectors and matrices}}. Define {{a [stochastic matrix](stochastic%20matrix.md) $\mathbf{M}$ where an element $\mathbf{M}_{i, j} \quad \forall i, j \in \set{1, \ldots, N}$ is the probability of a person going to $p_i$ given they have randomly clicked a link on $p_j$}}. We assume that the probability {{is equal between all unique outbound links of a page, so $\mathbf{M}_{i, j} = \frac 1 {L(p_j)}$}}. The matrix is {{a left stochastic matrix because each column sums up to 1, i.e. $\sum_{i = 1}^N \mathbf{M}_{i, j} = 1 \quad \forall j \in \set{1, \ldots, N}$}}. This property also means {{left multiplying a column vector (the PageRank column vector in this case) by $\mathbf{M}$ preserves the sum of vector elements}}. Also, define {{the PageRank column vector at time $t$ as $\mathbf{R}_t = \begin{bmatrix} p_1 & \ldots & p_N \end{bmatrix}^\intercal$}}. Then the operation above is {{simply a [matrix multiplication](matrix%20multiplication.md)}}: {{$$\mathbf{R}_t = \mathbf{M} \mathbf{R}_{t - 1}$$}}. <!--SR:!2025-03-28,193,290!2024-10-16,89,290!2024-11-25,112,290!2025-03-01,178,270!2025-03-13,205,310!2025-02-09,178,310!2024-12-06,118,290!2025-07-17,282,290-->

Also, note that there are {{2 variants of the above algorithm}}: {{sync iteration and async iteration}}. The former is discussed above. The latter is similar, the only difference is that {{PageRank of a page is updated instantly after calculation instead of after iterating through all pages first}}. This means {{the PageRanks used for calculating the new PageRanks is a mix of old and new PageRanks, as opposed to only old PageRanks in sync iteration}}. In that case, the calculated PageRank is {{dependent on the iteration order}}. In this article, only the sync iteration is discussed. <!--SR:!2025-08-19,321,310!2025-01-14,155,310!2024-12-13,123,290!2024-12-22,143,310!2025-04-11,196,270-->

### damping factor

The PageRank theory also additional holds that {{a surfer randomly clicking on links will eventually stop clicking}}. The probability that {{the person continues clicking is the _damping factor_ $d$}}. The probability that {{they jump to a random page is $1 - d$}}. Additionally, each page has {{a equal chance of being jumped to, so the probability of jumping to a _particular_ page is $(1 - d) / N$}}. The factor is generally set {{around 0.85}}. <!--SR:!2025-02-04,176,310!2025-03-06,201,310!2025-03-01,195,310!2024-12-20,130,290!2024-11-25,109,290-->

Furthermore, damping factor mitigates the {{sink ([spider trap](spider%20trap.md)) problem}}. If there is {{a group of pages that has no outbound links to other pages not in the group}}, then {{that group of pages will eventually accumulate all the PageRank, making that group a sink}}. Examples include {{2 pages only linking to each other, or a page linking to itself if self-links are not excluded}}. The damping factor mitigates this by {{simulating a random jump with probability of $1 - d$, which helps jumping out of that sink}}. <!--SR:!2025-01-16,159,310!2025-01-02,152,310!2024-11-09,105,290!2025-01-28,171,310!2024-12-15,136,310-->

With the above additional assumptions, the PageRank algorithm is modified as follows: {{The incoming PageRank scores are multiplied by $d$, and $(1 - d) / N$ is added to the PageRank of a page per iteration}}. Mathematically, {{$$\operatorname{PR}_t(p) = \frac {1 - d} N + d \sum_{r \in B(p)} \frac {\operatorname{PR}_{t - 1}(r)} {L(r)}$$}}. The equation using {{vectors and matrices}} is: {{$$\mathbf{R}_t = \begin{bmatrix} \frac {1 - d} N \\ \stackrel {\vdots} {\scriptstyle \times N} \end{bmatrix} + d \mathbf{M} \mathbf{R}_{t - 1}$$}} <!--SR:!2024-11-25,120,290!2025-05-04,208,270!2025-07-03,284,310!2024-10-25,88,270-->

However, the original paper, {{gave a slightly different formula, leading to some confusion}}: {{$$\operatorname{PR}_t(p) = 1 - d + d \sum_{r \in B(p)} \frac {\operatorname{PR}_{t - 1}(r)} {L(r)}$$}}. The difference is that {{$1 - d$ is added per iteration instead of $(1 - d) / N$}}. This would make {{all PageRank multiplied by $N$ and the PageRank sum becomes $N$}}. This variation should only be used if {{the PageRank values are initialized with all $1$ instead of $1 / N$}}. Otherwise, the first equation is {{more commonly used and more "correct"}}. <!--SR:!2025-04-14,231,330!2025-04-30,243,330!2025-01-09,158,310!2025-03-11,201,310!2025-03-15,205,310!2025-01-13,160,310-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/PageRank) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
