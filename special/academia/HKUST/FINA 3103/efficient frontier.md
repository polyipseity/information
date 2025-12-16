---
aliases:
  - FINA 3103 efficient frontier
  - FINA3103 efficient frontier
  - HKUST FINA 3103 efficient frontier
  - HKUST FINA3103 efficient frontier
  - efficient frontier
tags:
  - flashcard/active/special/academia/HKUST/FINA_3103/efficient_frontier
  - language/in/English
---

# efficient frontier

- HKUST FINA 3103

---

- see: [general/efficient frontier](../../../../general/efficient%20frontier.md)

The __efficient frontier__ is the set of portfolios that offers the highest expected return for a given level of risk, or equivalently the lowest risk for a given expected return.

## mathematical representation

For assets $i=1,\dots,n$ let $\mu_i$, $\sigma_i$ be mean return and standard deviation, and $\rho_{ij}$ the correlation between assets $i$ and $j$. With portfolio weights $w=(w_1,\ldots,w_n)$ constrained to sum to one, $$r_p=\sum_{i=1}^{n} w_i\,\mu_i ,\qquad \sigma_p^2=\sum_{i=1}^{n}\sum_{j=1}^{n} w_i w_j \rho_{ij}\sigma_i\sigma_j .$$ If a risk‑free asset with return $r_f$ is available, the portfolio return and standard deviation become $$r_C=w_A\,\mu_A+(1-w_A)\,r_f,\qquad \sigma_C=|w_A|\,\sigma_A .$$ The line connecting $(0,r_f)$ to any risky portfolio is the Capital Allocation Line.

## visualization

To explore the opportunity set we generate many random weight vectors. In Excel, `=RAND()` produces a uniform number on $[0,1]$. For two assets $A$ and $B$, `w_A = RAND()` and `w_B = 1 - w_A` create one feasible portfolio; repeating this procedure many times ($m=1000$) yields a cloud of points $(r_p,s_p)$, which can be plotted to visualise the frontier.

### visualizing opportunity set

The opportunity set is the collection of all risk‑return combinations that can be achieved by allocating weights between two risky assets. By generating many random weight vectors in Excel and plotting each portfolio’s mean return against its standard deviation, one obtains a cloud of points that represents this set. The shape of the cloud depends strongly on the correlation \(\rho_{AB}\) between the two assets.  

When $\rho_{AB}=1$, all portfolios lie on the straight line connecting the individual asset points; diversification offers no benefit. When $\rho_{AB}=-1$, the set collapses to two straight lines that extends to the y-axis and touch it at the same point, allowing perfect risk‑return trade‑offs.  As $\rho_{AB}$ moves between these extremes, the opportunity set expands from a narrow band into a broader, more circular shape, illustrating how lower correlation enhances diversification benefits.

### visualizing CAL

When the risk‑free rate is $r_f$, the slope of the Capital Allocation Line equals the Sharpe ratio of the chosen risky portfolio: $$m_{\text{CAL} }=\frac{\mu_p-r_f}{\sigma_p}$$ Plotting $(\sigma_C,r_C)$ for many portfolios produces a straight line from $(0,r_f)$ outward, representing all attainable risk‑return combinations with borrowing or lending at the risk‑free rate.

### visualizing short selling and leverage

Allowing short selling ($w_A<0$) or leverage ($w_A>1$) expands the frontier. In Excel one can generate such weights by `w_A = RAND()*2-1` (gives $-1\le w_A\le 1$) or by using `=RANDBETWEEN(min,max)` for arbitrary limits. These additional portfolios lie outside the original convex set, creating a frontier that extends beyond the risk‑free point.
