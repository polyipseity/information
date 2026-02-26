---
aliases:
  - FINA 3103 arbitrage pricing theory
  - FINA3103 arbitrage pricing theory
  - HKUST FINA 3103 arbitrage pricing theory
  - HKUST FINA3103 arbitrage pricing theory
  - arbitrage pricing theory
tags:
  - flashcard/active/special/academia/HKUST/FINA_3103/arbitrage_pricing_theory
  - language/in/English
---

# arbitrage pricing theory

- HKUST FINA 3103

---

- see: [general/arbitrage pricing theory](../../../../general/arbitrage%20pricing%20theory.md)

{@{__Arbitrage Pricing Theory__ (__APT__)}@} was introduced by {@{Prof. Stephan Ross in 1976}@} and gives {@{a different route to the security‑market line}@}.  Its foundation rests on {@{three realistic assumptions}@}: prices {@{follow a factor model}@}; firm‑specific {@{risk can be diversified away}@}; and persistent {@{arbitrage opportunities cannot exist}@}.  It addresses {@{practical limitations of the Capital Asset Pricing Model (CAPM)}@}. It rests on a {@{multi‑factor framework}@} that extends {@{the single‑index idea while remaining tractable}@}. <!--SR:!2026-03-21,16,317!2026-03-22,17,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-20,15,317!2026-03-20,15,317-->

## single index model

{@{A _single index model_}@} posits that {@{each asset’s excess return can be decomposed into a linear exposure to one common macro factor}@}, typically {@{a market index $r_{M,t}$, and an idiosyncratic shock}@}: {@{$$r_{i,t}-r_f = a_i + b_i(r_{M,t}-r_f)+\varepsilon_{i,t} \,,$$}@} where $a_i$ {@{captures any asset‑specific intercept}@}, $b_i$ is {@{the market exposure (beta)}@}, and $\varepsilon_{i,t}$ {@{has mean zero}@}. The model assumes that all {@{systematic risk is conveyed by the single factor}@} and that firm‑specific {@{shocks are uncorrelated across assets}@}. <!--SR:!2026-03-20,15,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-22,17,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-22,17,317!2026-03-20,15,317-->

### variance and covariance under SIM

From {@{the SIM model}@}, {@{the total variance of asset $i$}@} decomposes {@{into systematic and idiosyncratic parts}@}: {@{$$\sigma_i^2 = b_i^{\,2}\sigma_M^2 + \sigma_{\varepsilon,i}^2.$$}@} Similarly, {@{the covariance between two assets}@} reduces to {@{$$\sigma_{ij}=b_ib_j\sigma_M^2,$$}@} so that only {@{the market exposure parameters $b_i,b_j$ and the variance of the index are needed}@}. This dramatically {@{lowers the estimation burden compared with a full Markowitz covariance matrix}@}. <!--SR:!2026-03-20,15,317!2026-03-20,15,317!2026-03-20,15,317!2026-03-21,16,317!2026-03-21,16,317!2026-03-21,16,317!2026-03-22,17,317!2026-03-21,16,317-->

### CAPM and SIM

When the intercept term {@{in the single‑index equation is set to zero}@}, the model collapses {@{to the standard CAPM}@}: {@{$$r_{i,t}-r_f = \beta_{i,M}(r_{M,t}-r_f)+\varepsilon_{i,t},$$}@} with {@{$\beta_{i,M}=b_i=\sigma_{i,M}/\sigma_M^2$}@}. Thus, CAPM can be viewed {@{as a SIM in which the constant term is zero}@}. {@{The relationship between expected excess returns}@} follows {@{$$\mu_i-r_f = \beta_{i,M}(\mu_M-r_f),$$}@} matching {@{the familiar CAPM expression}@}. <!--SR:!2026-03-22,17,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-21,16,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-21,16,317-->

{@{Markowitz portfolio theory}@} requires estimating {@{$n$ variance and $n(n - 1) / 2$ covariance}@}, for a total of {@{$n(n+1)/2$ variance‑covariance terms}@}, which becomes {@{infeasible when $n$ is large (e.g., 5 000 assets imply 12.5 million parameters)}@}. {@{The single‑index model and CAPM avoid this}@} by summarising {@{risk with a few factor loadings (only the factor loadings need to be estimated)}@}, thereby reducing {@{estimation error and computational cost}@}. <!--SR:!2026-03-21,16,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-21,16,317!2026-03-22,17,317-->

### SIM limitations

{@{The single‑factor assumption}@} may be {@{too restrictive because many macro variables}@}—{@{GDP growth, inflation, interest rates}@}—could {@{influence returns}@}. {@{Introducing additional factors}@} leads to {@{_multi‑factor models_, the foundation of APT}@}. These models retain {@{the linear factor structure}@} while allowing for {@{a richer set of systematic drivers}@}. <!--SR:!2026-03-22,17,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-21,16,317-->

In practice, estimating {@{$b_i$ and $\sigma_{\varepsilon,i}$ from historical data}@} can still {@{suffer from sampling noise}@}, but {@{the reduced dimensionality of SIM and CAPM}@} mitigates {@{this problem relative to full covariance estimation}@}. The theory remains {@{useful as a first‑order approximation}@}, with multi‑factor {@{extensions providing greater realism when warranted}@}. <!--SR:!2026-03-20,15,317!2026-03-21,16,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-20,15,317!2026-03-21,16,317-->

## multiple factors model

{@{A _multiple factors model_}@} generalises {@{the single‑index framework}@} by {@{allowing $K$ common factors to explain asset returns}@}.  For each {@{security $i$, excess return}@} is written as {@{$$r_{i,t}= \bar r_i+\sum_{k=1}^{K}b_{ik}\,f_{k,t}+u_{i,t},$$}@} where $\bar r_i$ is {@{the sample mean of $r_i$}@}, $f_{k,t}$ denotes {@{the _surprise_ on factor $k$ (the deviation of that factor from its expectation)}@}, and $u_{i,t}$ is {@{an idiosyncratic shock with zero mean}@}. {@{The coefficient $b_{ik}$}@} is called {@{the _factor loading_ or _sensitivity_ to factor $k$}@}.  By construction {@{$\mathbb E[f_{k,t}]=\mathbb E[u_{i,t}]=0$}@} for {@{all $i$ and $k$}@}. <!--SR:!2026-03-20,15,317!2026-03-21,16,317!2026-03-21,16,317!2026-03-21,16,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-22,17,317!2026-03-20,15,317!2026-03-20,15,317-->

Suppose {@{two macro variables}@} drive the returns of {@{a regulated utility (CLP) and an airline (Cathay)}@}.  If {@{GDP rises unexpectedly while the central bank hikes rates}@}, CLP’s {@{cash flows are discounted more heavily}@}, so its {@{exposure to _interest rate_ is negative and large in magnitude}@}.  Cathay benefits {@{from a growing economy}@} but suffers {@{only slightly from higher borrowing costs}@}; thus it has {@{a large positive loading on GDP}@} and {@{a small negative one on interest rate}@}. <!--SR:!2026-03-21,16,317!2026-03-20,15,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-22,17,317-->

### factor-mimicking portfolio

{@{A _factor‑mimicking portfolio_}@} is constructed so that its {@{return equals the excess return of a particular factor}@}.  For {@{factor $k$}@} we seek {@{weights $\mathbf w_k=(w_{1},\dots ,w_{N})$}@} such that  {@{$$r_{k,t}=\bar r_k+f_{k,t},\qquad b_{ik}= \sum_{j=1}^{N}w_j\,b_{jk},$$}@} with {@{$b_{kk}=1$ and $b_{hk}=0$ for $h\neq k$}@}.  {@{The expected excess return of the factor portfolio}@} is {@{its _factor premium_, $r_k-\!r_f$}@}, which rewards {@{investors for bearing that specific systematic risk}@}. <!--SR:!2026-03-22,17,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-21,16,317!2026-03-20,15,317!2026-03-20,15,317!2026-03-21,16,317!2026-03-22,17,317!2026-03-22,17,317-->

Using data on {@{United Airlines (UA) and Shell (S)}@}, suppose their {@{loadings on GDP ($b_{\text{GDP} }$) and inflation ($b_{\text{INF} }$)}@} are known.  To build {@{a portfolio that loads only on GDP}@}, solve {@{$$0.3\,w_{UA}+0.057\,w_S =1,\qquad-0.79\,w_{UA}-1.22\,w_S=0 .$$}@} The solution is {@{$w_{UA}=3.8$, $w_S=-2.46$}@}; {@{the short position in Shell}@} balances {@{the long position in United Airlines}@}.  {@{The residual weight on a risk‑free asset}@} is {@{$w_F=1-(w_{UA}+w_S)=-0.34$}@}, indicating that an investor would {@{borrow at the risk‑free rate to finance the factor portfolio}@}. <!--SR:!2026-03-22,17,317!2026-03-21,16,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-20,15,317-->

### interpretation of multiple factors model

Rewriting {@{the multi‑factor equation in excess terms}@} yields {@{$$r_{i,t}-r_f=(\bar r_i-r_f)-\sum_{k=1}^{K}b_{ik}\,(\bar r_k-r_f)+\sum_{k=1}^{K}b_{ik}(f_{k,t}-\!r_F)+u_{i,t}. $$}@} The right‑hand side {@{contains three components}@}: {@{a constant term $a_i=(\bar r_i-r_f)-\sum_{k}b_{ik}(\bar r_k-r_f)$}@}, {@{the product of each factor’s _excess return_ and its loading on asset $i$}@}, and {@{an idiosyncratic shock $u_{i,t}$}@}. <!--SR:!2026-03-21,16,317!2026-03-07,2,277!2026-03-07,2,257!2026-03-17,12,277!2026-03-22,17,317!2026-03-22,17,317-->

Thus, {@{excess returns}@} are driven by {@{a constant, systematic factors, and firm‑specific noise}@}.  The model remains {@{_empirical_; it does not impose _theoretical_ equilibrium conditions as CAPM does}@}, but rather is supported by {@{arbitrage pricing theory}@}. <!--SR:!2026-03-22,17,317!2026-03-21,16,317!2026-03-21,16,317!2026-03-22,17,317-->

## background

{@{Arbitrage Pricing Theory (APT)}@} was introduced by {@{Prof. Stephan Ross in 1976}@} and gives {@{a different route to the security‑market line}@}. Its foundation rests on {@{three realistic assumptions}@}: prices {@{follow a factor model}@}; firm‑specific {@{risk can be diversified away}@}; and persistent {@{arbitrage opportunities cannot exist}@}. <!--SR:!2026-03-20,15,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-22,17,317-->  

{@{The idea of _no free lunch_}@} means that there is {@{no way to earn a guaranteed profit with zero net investment or risk}@}.  If {@{such an opportunity existed}@}, traders would {@{exploit it until prices adjusted and the advantage disappeared}@}, as illustrated by the anecdote in which {@{a large sum was accidentally dropped on a highway}@}, temporarily creating {@{a fleeting arbitrage that vanished when traffic resumed}@}. <!--SR:!2026-03-20,15,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-20,15,317!2026-03-21,16,317!2026-03-21,16,317-->

Arbitrage requires {@{simultaneously zero cost and zero risk}@}.  {@{The law of one price}@} says {@{identical assets must trade at equal prices}@}; otherwise an investor could {@{buy low and sell high}@}.  In practice, {@{price adjustments are rapid}@}, so {@{persistent arbitrage is implausible}@}. <!--SR:!2026-03-22,17,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-20,15,317!2026-03-20,15,317!2026-03-20,15,317-->

## APT formula

Under {@{the factor model, taking expectations}@} yields {@{$$\bar r_i-r_F=\sum_{k=1}^{K}b_{ik}\bigl(\bar r_k-r_F\bigr),$$}@} which is the APT assertion that {@{an asset’s risk premium depends only on its loadings on systematic factors}@}.  In {@{the multi‑factor mode}@}l we would have {@{an extra constant $a_i$}@}; if {@{no arbitrage exists}@}, {@{this constant must be zero}@}. <!--SR:!2026-03-22,17,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-21,16,317!2026-03-22,17,317!2026-03-20,15,317-->

## arbitrage

{@{Mispricing}@} leads to {@{arbitrage}@}.  Consider {@{a diversified portfolio $A$}@} with {@{factor loadings $b_{\text{GDP} }=0.5,\; b_{\text{IR} }=0.75$}@}.  The risk‑free rate is {@{$r_F=4\%$}@}, the mean returns of GDP and interest rate are {@{$10\%$ and $12\%$}@}.  APT predicts {@{$$E[r_A]=0.04+0.5(0.10-0.04)+0.75(0.12-0.04)=13\%,$$}@} but market data show {@{a lower return of $12\%$}@}, revealing {@{overpricing so one would want to sell it}@} by setting {@{$x_A = -1$}@}.  To eliminate {@{exposure to each systematic factor}@}, one chooses {@{weights equal to the asset’s loadings}@}: {@{$x_k=b_{ik}$}@}, and {@{interest-free weight $x_F$ equal the residual weight}@} such that there is {@{no initial investment}@}: {@{$$x_A + x_F + \sum_k x_k = 0 \. $$}@}  In that case {@{the portfolio return}@} simplifies to {@{$-a_i$}@}; if {@{$a_i<0$}@} the arbitrage profit is {@{$-a_i>0$}@}.  The construction involves {@{shorting the mispriced asset}@}, {@{long factor‑mimicking portfolios}@}, and possibly {@{borrowing or lending at the risk‑free rate}@}. <!--SR:!2026-03-22,17,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-21,16,317!2026-03-21,16,317!2026-03-18,13,297!2026-03-07,2,277!2026-03-07,2,257!2026-03-21,16,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-21,16,317-->

{@{Relative mispricing}@} also leads to {@{arbitrage}@}. If {@{two well‑diversified portfolios}@} have {@{different loadings or betas (thus relative mispricing exists)}@}, an arbitrage can be constructed by shorting {@{the less attractive one}@} and taking {@{a weighted position in the more attractive portfolio plus risk‑free savings}@}.  For example, with {@{$r_F=4\%$}@}, {@{$\bar r_A=10\%$ ($b_A=1.0$)}@} and {@{$\bar r_B=6\%$ ($b_B=0.5$)}@}, {@{selling $B$ and buying half of $A$}@} plus the rest on {@{the risk‑free asset}@} yields {@{an excess return of $1\%$}@}.  The profit comes from {@{relative mispricing rather than a single‑asset anomaly}@}. <!--SR:!2026-03-22,17,317!2026-03-22,17,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-21,16,317-->

### law of one price

{@{The law of one price}@} states that {@{identical payoffs must trade at the same price}@}.  If two portfolios {@{produce the same state‑by‑state payoff}@}, their {@{market values must coincide}@}.  {@{Any deviation}@} would allow {@{a riskless profit}@}: {@{buy the cheaper portfolio and sell the more expensive one}@}, earning {@{the difference today while the future cash flows are equal}@}. <!--SR:!2026-03-22,17,317!2026-03-22,17,317!2026-03-20,15,317!2026-03-20,15,317!2026-03-21,16,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-22,17,317-->

{@{An Arrow–Debreu security}@} pays {@{\$1 in a single state and \$0 elsewhere}@}; its price is called {@{the _state price_ of that state}@}.  A portfolio can be used to {@{replicate any other asset’s payoff}@}, and {@{the price of a more complex payoff}@} is simply {@{the weighted sum of the relevant state prices}@}.  {@{The law of one price and Arrow–Debreu securities}@} provide {@{a systematic way to value contingent claims}@} without {@{relying on a particular pricing model}@}. <!--SR:!2026-03-21,16,317!2026-03-21,16,317!2026-03-20,15,317!2026-03-20,15,317!2026-03-20,15,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-22,17,317-->

## APT and multiple factors model

{@{The multi‑factor model (MFM)}@} contains {@{an extra intercept $a_i$}@}; when {@{no arbitrage exists}@} {@{this term must vanish}@}, making MFM {@{equivalent to APT}@}.  Thus APT can be seen as a {@{special case of the more general factor framework}@} that imposes {@{the no‑arbitrage condition}@}. <!--SR:!2026-03-21,16,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-20,15,317!2026-03-22,17,317-->

## advantages and disadvantages

APT offers {@{a reasonable description of returns with plausible factors}@} without requiring {@{knowledge of the market portfolio or equilibrium assumptions (a stronger assumption)}@}.  It only assumes {@{no‑arbitrage condition (a weaker assumption)}@}.  Its {@{main limitations}@} are {@{the lack of guidance on which factors to use}@}, {@{potential time variation in those factors}@}, and {@{the higher data demand for estimation}@}. <!--SR:!2026-03-20,15,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-22,17,317!2026-03-22,17,317-->

## factors

Multi‑factor models, including the APT, do not {@{prescribe which systematic drivers to use}@}.  Researchers often {@{start from economic intuition}@}, but empirically chosen factors may {@{lack a clear theoretical basis}@} and can {@{shift over time}@}.  Statistical techniques are therefore employed to {@{extract factor returns that explain expected asset prices}@}, yet these extracted factors sometimes behave {@{like noise or change when data vintages are updated}@}. <!--SR:!2026-03-21,16,317!2026-03-21,16,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-20,15,317!2026-03-21,16,317-->

Multi‑factor approaches generally outperform the {@{single‑factor CAPM}@} because they {@{incorporate additional systematic drivers}@}.  Their success relies on {@{empirical fit rather than a unifying theory}@}, leaving open questions about {@{which factors are fundamental and how stable they remain over time}@}. <!--SR:!2026-03-22,17,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-20,15,317-->

### hypothesis testing

To test whether {@{a set of factors explains an individual stock’s price dynamics}@}, one formulates {@{a linear regression}@} {@{$$r_{i,t}-r_{F,t}= \alpha_i+\sum_{k=1}^{n}\beta_{ik}(r_{k,t}-r_{F,t})+u_{i,t},$$}@} and estimates {@{the intercept $\hat{\alpha}_i$ and loadings with ordinary least squares}@}.  If {@{$\hat{\alpha}_i=0$}@}, {@{the APT holds for that asset}@}.  {@{The usual inference tools—p‑values, confidence intervals}@}—determine whether {@{a non‑zero $\alpha_i$ can be rejected at conventional levels}@}. <!--SR:!2026-03-20,15,317!2026-03-22,17,317!2026-03-20,15,317!2026-03-21,16,317!2026-03-21,16,317!2026-03-20,15,317!2026-03-20,15,317!2026-03-21,16,317-->

In {@{a regression test}@} {@{the estimated intercept $\hat{\alpha}_i$}@} is treated as {@{a random variable whose sampling distribution can be approximated by a normal curve}@} under standard assumptions.  {@{A p‑value}@} measures {@{how likely it would be to observe an estimate at least as extreme as $\hat{\alpha}_i$}@} if {@{the true value were zero}@}; {@{a small p‑value (e.g., < 0.05 or < 0.01)}@} suggests that {@{the null hypothesis $H_0:\alpha_i=0$ is unlikely}@}, so we {@{reject the APT for that asset}@}.  {@{A confidence interval}@} provides {@{an interval that would contain the true $\alpha_i$ in a large number of samples}@}; if {@{zero lies outside this interval}@}, {@{the same conclusion follows}@}.  For example, {@{a 95 % confidence interval of $[-0.005,\,-0.001]$}@} excludes zero, indicating {@{evidence against the APT hypothesis}@} for that security. <!--SR:!2026-03-20,15,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-20,15,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-20,15,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-22,17,317-->

### Fama–French three-factor model

{@{The three‑factor specification}@} was introduced {@{in _Common Risk Factors in the Returns on Stocks and Bonds_ (Fama & French, 1993)}@}.  It expands {@{the CAPM}@} by adding {@{size and value drivers that are derived from market‑cap and book‑to‑market data}@}.  The model writes {@{the excess return of stock $i$}@} as {@{$$r_{i,t}-r_{F,t}=\alpha_i+\beta_{iM}\,r_{M,t}+\beta_{iSMB}\,r_{SMB,t}+\beta_{iHML}\,r_{HML,t}+e_{i,t},$$}@} where <!--SR:!2026-03-21,16,317!2026-03-20,15,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-22,17,317-->

- $r_{M,t}=r_{SP,t}-r_{F,t}$ ::@:: is the market excess return (e.g. using S&P&nbsp;500), <!--SR:!2026-03-28,58,310!2026-03-28,58,310-->
- $r_{SMB,t}=r_{S,t}-r_{B,t}$ ::@:: captures the small‑minus‑big size effect (by market capitalization), and <!--SR:!2026-03-28,58,310!2026-03-28,58,310-->
- $r_{HML,t}=r_{H,t}-r_{L,t}$ ::@:: measures high‑minus‑low book‑to‑market. <!--SR:!2026-03-28,58,310!2026-03-28,58,310-->

{@{The Fama–French framework}@} was motivated mainly by {@{empirical regularities rather than a single economic theory}@}, which explains why {@{the size ($\text{SMB}$) and value ($\text{HML}$) loadings}@} capture {@{return differences so well yet lack a unifying rationale}@}.  The puzzle remains: why does {@{a portfolio of small firms outperform large ones}@}, and why do {@{high‑book‑to‑market companies earn higher returns than low‑book‑to‑market ones}@}?  {@{A notable contribution}@} to the literature is {@{Lettau and Wachter’s 2007 paper in _The Journal of Finance_}@}, which investigates {@{these patterns from a microstructural perspective}@}. <!--SR:!2026-03-22,17,317!2026-03-22,17,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-20,15,317!2026-03-21,16,317-->

{@{Empirical work on a manufacturing‑industry}@} sample spanning 1926–2023 shows that {@{the intercept $\hat\alpha_i$ is only -1 %}@} and {@{statistically insignificant}@}, implying that the three factors explain {@{almost all systematic variation (about 90%)}@}; CAPM explains roughly {@{seventy percent of the same variance}@}. <!--SR:!2026-03-22,17,317!2026-03-20,15,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-22,17,317-->

{@{The Fama–French factors}@} are {@{standard tools in both industry practice and scholarly work}@}, distributed through {@{Kenneth French’s website and the Wharton Research Data Service}@}.  The site occasionally {@{revises its factor series}@}; WRDS notes that {@{“Research Portfolios incorporate any revisions in the historical underlying data”}@} and that such {@{adjustments are usually minor}@}, so most researchers rely on {@{the same datasets without noticing significant changes}@}. {@{A key study by Akey et al. (2024)}@} examined how {@{revisions to the construction of Fama‑French factors alter their returns}@}.  They found that {@{many changes stem from methodological updates rather than underlying data edits}@}, and that {@{newer vintages do not necessarily improve model performance}@}.  The results raise concerns about {@{the reliability of published factor series}@}. <!--SR:!2026-03-21,16,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-20,15,317!2026-03-21,16,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-21,16,317!2026-03-20,15,317!2026-03-22,17,317-->

### Carhart four-factor model

{@{Mark Carhart extended the Fama‑French framework}@} in his {@{1997 paper _On Persistence in Mutual Fund Performance_}@}.  He added {@{a momentum factor $r_{MMT}$}@}, defined from {@{past performance rankings}@}, to capture {@{serial correlation in returns}@}.  {@{The four‑factor regression}@} becomes {@{$$r_i-r_F=\beta_{iM}(r_M-r_F)+\beta_{iSMB}r_{SMB}+\beta_{iHML}r_{HML}+\beta_{iMMT}r_{MMT},$$}@} and {@{empirical evidence}@} shows that including {@{momentum reduces unexplained risk and improves the fit relative to the three‑factor model}@}.  {@{The factor portfolios}@} are constructed {@{from market data}@}, and the additional term captures {@{the tendency of winners to continue outperforming losers}@}. <!--SR:!2026-03-20,15,317!2026-03-21,16,317!2026-03-20,15,317!2026-03-21,16,317!2026-03-22,17,317!2026-03-21,16,317!2026-03-21,16,317!2026-03-20,15,317!2026-03-20,15,317!2026-03-22,17,317!2026-03-22,17,317!2026-03-22,17,317-->
