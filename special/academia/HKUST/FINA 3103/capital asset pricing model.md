---
aliases:
  - FINA 3103 capital asset pricing model
  - FINA3103 capital asset pricing model
  - HKUST FINA 3103 capital asset pricing model
  - HKUST FINA3103 capital asset pricing model
  - capital asset pricing model
tags:
  - flashcard/active/special/academia/HKUST/FINA_3103/capital_asset_pricing_model
  - language/in/English
---

# capital asset pricing model

- HKUST FINA 3103

---

- see: [general/capital asset pricing model](../../../../general/capital%20asset%20pricing%20model.md)

The __capital asset pricing model__ (__CAPM__) is a foundational framework in modern portfolio theory that links an asset’s expected return to its systematic risk relative to the market. It was introduced by William Sharpe and formalised in the early 1960s, providing a benchmark for evaluating investment performance and for estimating required returns on risky assets.

CAPM offers a benchmark for pricing securities, constructing portfolios, and estimating the cost of capital. It implies that only systematic risk is rewarded in equilibrium; idiosyncratic risk can be diversified away. In practice, analysts compute $\beta$ from historical returns and use the CAPM equation to evaluate whether an asset trades at a fair price relative to its risk.

## history

William Sharpe first presented the model in 1964, later receiving the Nobel Prize in Economics in 1990 for his contributions to financial economics. The CAPM remains a core teaching tool and is widely applied in corporate finance, asset‑pricing research, and portfolio management.

## background

### market portfolio

The _market portfolio_ contains every tradable risky asset weighted by its market‑capitalization share. The weights in the market portfolio are simply proportional to the asset' market caps, e.g. for three assets $A,B,C$ with market caps 100 M, 1.5 B, and 600 M, the market weights are $(4.55\%,68.2\%,27.3\%)$.

### tangent portfolio

When all investors are rational, risk‑averse and hold the same expectations, they converge to the same efficient frontier; the point of tangency between this frontier and the line from the risk‑free rate is called the _tangent portfolio_. In equilibrium the market portfolio coincides with the tangent portfolio because each investor allocates capital only between a risk‑free asset and that common risky mix.

## assumptions

CAPM rests on a handful of simplifying assumptions: perfect competition, one-period horizon, full market participation, and homogeneous expectations.

1. _Perfect competition_ ::@:: – many price‑taking investors.
2. _One-period horizon_ ::@:: – all decisions occur in a single period; long‑term effects are ignored (myopic behavior).
3. _Full market participation_ ::@:: – every relevant asset, including risk‑free securities, is tradable and can be borrowed or lent at the same rate without taxes or transaction costs.
4. _Homogeneous expectations_ ::@:: – investors agree on expected returns, variances, and covariances of all assets.

These assumptions guarantee that each investor holds an identical portfolio of risky assets (the tangent portfolio) while varying only in their mix with a risk‑free asset.

## derivation

Starting from the market portfolio’s return $r_{T}= \sum _{i} w_{M,i}\, r_{i},$ a small shift in weight $w_{A}$ by an infinitesimal amount $dw_{A}$ changes the return to  
$r_{\text{new} }=r_{M}+dw_{A}(r_{A}-r_{f})$.  The expected excess return then shifts as $$d\mu _{M}= \bigl(\mu _{A}-r_{f}\bigr)\,dw_{A},$$ while the variance changes to $$\sigma_{\text{new} }^{2}   = \sigma _{M}^{2}+ (dw_{A})^{2}\sigma _{A}^{2}     + 2\,dw_{A}\operatorname{Cov}(r_{M},r_{A}).$$ Neglecting the squared‑term $ (dw_{A})^{2}$ because it is infinitesimal and applying the chain rule, we obtain $$d\sigma _{M}= \frac{\operatorname{Cov}(r_{M},r_{A})}{\sigma _{M} }\,dw_{A} \,.$$

The ratio of the marginal expected return to the marginal risk (return-to-risk ratio, RRR) equals $$\frac{d\mu _{M} }{d\sigma _{M} }   = \frac{\mu _{A}-r_{f} }{\operatorname{Cov}(r_{M},r_{A})/\sigma _{M} } \,.$$ In equilibrium all risky assets must offer the same RRR; otherwise an investor could move weight toward a higher‑RRR asset and increase the market portfolio’s Sharpe ratio, contradicting efficiency. If such an inefficiency did exist, arbitrage and rebalancing by investors would quickly bid up the prices of the underpriced (high‑RRR) assets and bid down the prices of overpriced (low‑RRR) assets, driving returns back into alignment. Consequently the market portfolio itself shares this common RRR.

Rearranging the equality for any asset $i$ yields $$\frac{\mu _{i}-r_{f} }{\operatorname{Cov}(r_{i},r_{M})/\sigma _{M} }   = \frac{\mu _{M}-r_{f} }{\sigma _{M}^{2} / \sigma_M },$$ or, after substituting the definition of beta, $$E[r_{i}]-r_{f}= \beta _{i}\bigl(E[r_{M}] - r_{f}\bigr) \,,$$ where the _beta_ of asset $A$ is $$\beta _{A}= \frac{\operatorname{Cov}(r_{A},r_{M})}{\sigma _{M}^{2} } .$$ This is the CAPM equation that links an asset’s expected excess return to its systematic risk.

## CAPM equation

The CAPM equation is $$E[r_{i}]= r_f + \beta _{i}\bigl(E[r_{M}] - r_{f}\bigr) \,,$$ where the _beta_ of asset $A$ is $$\beta _{A}= \frac{\operatorname{Cov}(r_{A},r_{M})}{\sigma _{M}^{2} } .$$

Using the S&P 500 as the market, let $\mu _{\text{SP} }=5\%$ and $r_{f}=1\%$.  With a covariance of $0.02$ between HSBC and the index and $\sigma _{\text{SP} }^{2}=0.01$, the beta is $$\beta_{\text{HSBC,SP} }   = \frac{0.02}{0.01}=2.$$ The CAPM then gives $E[r_{\text{HSBC} }]= r_{f}+ \beta_{\text{HSBC,SP} }\bigl(\mu _{\text{SP} }-r_{f}\bigr)   = 1\% + 2\times 4\%=9\%$.  Hence the model predicts a $9\%$ expected return for HSBC.

### beta

The term $\mu_M-r_f$ is the _market risk premium_, the reward for bearing systematic risk; the factor $\beta_{i,M}$ measures how much of that risk an asset carries. Different assets may have identical volatility but distinct betas if their covariances with the market differ.

- A beta larger than one ::@:: means the asset amplifies market swings.  
- A beta equal to one ::@:: coincides with the market portfolio itself; its expected excess return equals the market premium.  
- A zero beta ::@:: implies no correlation with the market, so its expected excess return is zero—its risk can be diversified away.  
- A negative beta ::@:: indicates that the asset moves opposite to the market; it earns a negative risk premium and would be priced below the risk‑free rate.

The Sharpe ratio $SR = \frac{\bar r_p-r_f}{\sigma _p}$ measures excess return per unit of total risk, whereas beta measures excess return per unit of systematic risk.  Using both metrics gives a more complete view: an asset can have a high Sharpe ratio but a low beta, implying that most of its return comes from diversifiable idiosyncrasy.

## portfolio CAPM

For any portfolio $p$ built from assets $\{i\}$, $$\mu_p=\sum_i w_i\,\mu_i      =r_f+\Bigl(\sum_i w_i\,\beta_{i,M}\Bigr)(\mu_M-r_f)      = r_f+\beta_{p,M}(\mu_M-r_f),$$ where the portfolio beta is simply the weighted sum of component betas: $$\beta_{p,M}=\sum_i w_i\,\beta_{i,M}.$$ Thus a portfolio’s expected excess return depends only on its total systematic exposure, not on idiosyncratic risk.

When an investor wishes to neutralise market risk, the target beta is zero.  Let $w$ be the fraction invested in asset $H$ with $\beta_H$ and the remaining $(1-w)$ in asset $I$ with $\beta_I$. The portfolio beta satisfies $$0 = w\,\beta_H+(1-w)\,\beta_I,$$ so $$ w=\frac{-\beta_I}{\beta_H-\beta_I}. $$ For example, if $\beta_H=2.0$ and $\beta_I=-0.5$, then $w=1/5$. The resulting portfolio is _market‑immunised_: its systematic risk cancels out while the expected return equals the risk‑free rate.

## security market line

Plotting expected returns (not excess returns) against beta gives a straight line called the _Security Market Line_ (SML): $$E[r_i] = r_f + \beta_{i,M}\,(\mu_M-r_f).$$ On this graph the point $\beta=1$ lies on the market portfolio and yields $E[r]=\mu_M$. Assets above the SML earn a higher return than implied by their beta, and thus underpriced; those below are overpriced. Because the slope equals the market risk premium, the SML is a visual tool for assessing whether an asset’s price reflects its systematic risk.

## empirical testing

Once a dataset of asset returns and the market index is available, the CAPM can be tested by estimating the CAPM equation with ordinary least squares.  If the model holds, the intercept $\alpha _i$ should not differ from zero. A statistically significant positive $\alpha _i$ indicates that the asset delivers a higher return than implied by its systematic risk, and thus underpriced; a negative value signals an overpriced security.

Empirical studies generally find that many assets have non‑zero alphas, suggesting that CAPM fails to capture all systematic drivers of returns.  The persistence of abnormal returns motivates extensions such as multi‑factor models (Fama–French three‑factor model, Carhart four‑factor model) which add size, value, momentum and other characteristics.

### alpha

For a portfolio $p$, the CAPM predicts an expected return $r_{p}^{*}= r_f+\beta _{p,M}( \mu_M-r_f)$.  Jensen’s alpha is defined as $$\alpha _p = \bar r_p-\bigl(r_f+\beta _{p,M}(\bar r_M-r_f)\bigr),$$ where the bars denote sample averages.  A positive value means that the portfolio outperformed its systematic‑risk expectation; a negative value signals underperformance.

### sigma

In CAPM each asset return is decomposed into a systematic component that moves with the market and an idiosyncratic part that does not.  For asset $i$, $$r_i-r_f=\beta_{i,M}\,(r_M-r_f)+\varepsilon _i ,\qquad \mathbb{E}[\varepsilon _i]=0,\;\operatorname{Cov}(r_M,\varepsilon _i)=0 .$$ The _sigma_ of the idiosyncratic term, $\sigma_{\varepsilon_i}^{2}= \operatorname{Var}(\varepsilon _i)$, measures risk that can be diversified away.  The total variance is then $$\sigma_i^{2}= \beta_{i,M}^{2}\sigma_M^{2}+\sigma_{\varepsilon_i}^{2},$$ so the proportion of systematic risk equals $\beta_{i,M}^{2}\sigma_M^{2}/\sigma_i^{2}$.  Assets with identical total variance may have very different betas; a higher beta means that a larger share of its volatility is driven by market movements, whereas a low or negative beta concentrates risk in the idiosyncratic component.  

In practice, estimating $\beta_{i,M}$ from historical returns and computing $\sigma_{\varepsilon_i}^{2}=\sigma_i^{2}-\beta_{i,M}^{2}\sigma_M^{2}$ lets investors decide whether a high‑volatility asset is truly risky or merely exposed to the market.  When an asset’s idiosyncratic variance dominates, its excess return can be earned without bearing systematic risk, which is why many portfolios aim for low beta through diversification.

## validity

The empirical evidence on the CAPM is mixed.  Studies such as Fisher Black (1993) and Fama & French (1992) report that, over long periods, the market‑beta factor explains a substantial portion of cross‑sectional returns but leaves residual variation.  When the data are split into pre‑1966 and post‑1966 samples, CAPM explains the former well but the latter poorly, suggesting time‑varying betas or additional risk sources.  The "size" factor—market capitalization—and the book‑to‑market ratio also appear to affect expected returns, leading to multi‑factor extensions of CAPM.

Because the true market portfolio is unobservable, any empirical test must approximate it with a broad index such as the S&P 500 or MSCI World.  Even with this proxy, estimates of β and α differ across studies and time horizons, indicating that the simple CAPM does not fully capture all systematic risk drivers.  Nonetheless, the model’s clarity and tractability make it useful for estimating cost‑of‑capital, pricing securities, and benchmarking performance.

## advantages and disadvantages

The CAPM is parsimonious; it links a single measure of systematic exposure—beta—to expected excess return.  Its assumptions derive from modern portfolio theory, so the model offers an intuitive explanation for why diversified investors should only be compensated for market risk.  Many firms and fund managers (74% according to Graham and Harvey (2001)) still use CAPM to estimate discount rates or to assess alpha.

The linear specification ignores non‑market factors that empirical work repeatedly identifies.  Moreover, the choice of a proxy for the market portfolio introduces uncertainty, and estimated betas can be unstable over time.  Because the model predicts zero intercept, any systematic deviation in α signals either mispricing or violations of the CAPM assumptions (e.g., heterogeneous expectations, transaction costs, or illiquidity).  Consequently researchers have proposed extensions such as the Consumption‑CAPM, Fama–French three‑factor model, and other multi‑factor frameworks that add size, value, momentum, and liquidity terms.

In practice, CAPM remains a foundational benchmark.  It is widely adopted for cost‑of‑capital calculations in corporate finance, for portfolio performance evaluation by asset managers, and for risk‑control in pension plans.  While it is not a complete description of reality, its simplicity makes it a valuable starting point before moving to richer models.
