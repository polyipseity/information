---
aliases:
  - FINA 3103 option
  - FINA3103 option
  - HKUST FINA 3103 option
  - HKUST FINA3103 option
  - option
tags:
  - flashcard/active/special/academia/HKUST/FINA_3103/option
  - language/in/English
---

# option

- HKUST FINA 3103

---

- see: [general/option (finance)](../../../../general/option%20(finance).md)

An __option__ is a contract that gives the holder the right, but not the obligation, to trade an underlying asset at a pre‑specified price before or on its maturity date. The two basic types are _call_ options, which give the right to buy, and _put_ options, which give the right to sell.

## option rights

The two basic types are _call_ options, which give the right but not the obligation to buy, and _put_ options, which give the right but not the obligation to sell.

## option styles

Options may be exercised either only on their expiration date (_European_) or at any time up to that date (_American_). A European call can be exercised solely on maturity, whereas an American call could be exercised earlier if it is profitable.

## contract specification

To evaluate an option one typically constructs a replication portfolio. The contract is fully described by the underlying asset, its spot price $S_t$, the exercise or strike price $K$, the expiration date $T$, the style (European or American), and the premium $C$ or $P$.

Note, by convention, both "_long call_" and "_long puts_" refers to buying the option, whereas "_short call_" and "_short put_" refers to selling the option. This is not to be confused with long and short positions with respect to the stock price.

## payoff and profit

For a European call with strike $K$ and maturity $T$, the _payoff_ (not _profit_) at expiry for the _buyer_ is  $$\text{Payoff}= \max(S_T-K,0).$$ If one sells (writes) the option, the cash flow is the negative of this amount. Thus, with respect to the _stock price_ (not the option), the buyer is the short position while the seller is the long position.

A European put has _payoff_ (not _profit_) for the _buyer_ $$\text{Payoff}= \max(K-S_T,0),$$ and its seller (writer) receives the opposite cash flow. Thus, with respect to the _stock price_ (not the option), the buyer is the short position while the seller is the long position.

The _profit_ (not _payoff_) valued at time $T$ of a holder who bought an option at price $C$ or ($P$ for a put) and paid interest at rate $r$ over time $T$ is $$\text{Profit}= \max(S_T-K,0)-C(1+r)^T \quad\text{for a call},$$ and $$\text{Profit}= \max(K-S_T,0)-P(1+r)^T \quad\text{for a put}. $$ For a short position the signs of all terms are reversed. The _breakeven spot price_ is the value of $S_T$ such that profit equals zero.

_Example_: A European call on IBM with strike $100$ and maturity of one year has payoff $\max(S_{1y}-100,0)$. If at expiry the spot price is $S_{1y}=110$, exercising yields a profit of $10$; if $S_{1y}<100$ the option expires worthless. If the call has a premium of $5$. With an annual interest rate of $1\%$, the cost of holding the option is $5(1+0.01)=5.05$. The net payoff is $\max(S_{1y}-100,0)-5.05$. Setting this equal to zero gives a break‑even spot price of $S_{1y}=105.05$.

### moneyness

_Moneyness_ refers to the relationship between an option’s strike price and the underlying asset’s spot price at expiration.

When the spot price is below the strike, a call option is _out of the money_; when it equals the strike it is _at the money_; and when it exceeds the strike it is _in the money_. For a European call with premium $C$, the payoff at maturity depends on this relationship: if the spot price $S_T$ is less than $K$, the payoff is zero; if $S_T=K$, the payoff remains zero; and if $S_T>K$, the payoff equals $S_T-K$. The corresponding profit for a holder who paid the premium and financed it at an annual rate $r$ over the life of the option is $\max(S_T-K,0)-C(1+r)^T$. Thus, when the call is out or at the money the profit equals the negative future value of the premium $-C(1+r)^T$, while in‑the‑money payoffs yield a positive excess over that cost.

For puts the situation is reversed: if $S_T<K$ it is _in-the-money_ and the payoff is $K-S_T$, if $S_T=K$ it is _at-the-money_ and the payoff is zero, and if $S_T>K$ it is _out-of-the-money_ and the payoff is also zero; the profit follows by subtracting the future value of the premium $-P(1+r)^T$.

## trading strategies

Options can be combined in many ways to shape payoff profiles that suit a trader’s risk‑return preferences. It can draw any desired payoff using a portfolio of options, provided that liquidity exists for the needed options.

Typical combinations include the _protective put_, the _money spread_ (also called _bull call spread_) and the _straddle_. These constructions act as tools for managing exposure rather than pure speculation. These three strategies respectively illustrate how option combinations can be used to hedge, limit risk or capture volatility.

### protective put

A _protective put_ is formed by buying a share of the underlying asset together with a put option on that same asset. If the market falls, the put limits losses; if it rises, the stock’s gains are largely unhindered.  

For example, suppose an investor holds one share of a stock whose current price is $\$70$ and buys a put with strike $K=50$. The payoff diagram shows that when the final stock price falls below $\$50$, the holder receives the difference $K-S_T$; otherwise the payoff is zero. Thus the combined position behaves like owning the share plus an insurance contract that pays off whenever the price drops below the strike.

### money spread

A _money spread_ or _bull call spread_ is created by buying a call with a lower strike and simultaneously selling another call with a higher strike. The resulting payoff rises when the underlying moves up but is capped, limiting both upside potential and downside risk.

For instance, buying a call at $K_1=50$ while writing one at $K_2=60$ yields a net payoff that starts at zero, climbs linearly between $\$50$ and $\$60$, and then levels off after $\$60$. The maximum gain equals the difference of strikes minus the net premium paid.

### straddle

A straddle consists of buying both a call and a put with identical strike $K$. This strategy profits when the underlying moves significantly in either direction, regardless of the direction. If at maturity the price is far from $K$, one leg pays off while the other expires worthless; if it stays near $K$, both legs lose value. The payoff diagram for a long straddle therefore rises on both sides of the strike price.

## put–call parity

The _put–call parity_ links _European_ (not _American_) call and put options on the same underlying asset with identical strike price $K$ and maturity $T$. Two self‑financing portfolios generate the same payoff, so their costs must be equal in an efficient market.

A portfolio that buys a call and a zero‑coupon bond that pays $K$ at time $T$ has current cost $C+\dfrac{K}{(1+r)^T}$; the payoff at expiry is $K + \max(S_T - K, 0)$. The second portfolio that buys a put and the underlying asset yields current cost $P+S_0$; the payoff at expiry is also $S_T + \max(K - S_T, 0) = K + \max(S_T - K, 0)$. Because at expiry, the two portfolios result in owning the underlying asset _and_ have identical payoffs for every possible value of the spot price at expiry, their present values must be equal. Hence $$C+\frac{K}{(1+r)^T}=P+S_0 .$$ If this relationship fails, an arbitrage opportunity exists.

From the parity equation: $$C+\frac{K}{(1+r)^T}=P+S_0 \,,$$ one can see increasing the strike price $K$ increases the put premium $P$, because one can guarantee to sell for at least $K$. Increasing the spot price $S_0$ increases the call premium $C$, higher spot price typically implies higher future expected spot. And finally, fixing other parameters, increasing the premium of one of the option raises the premium of the other option, which can be interpreted as increased volatility.

### put–call arbitrage

Suppose a stock trades at $S_0=110$, the strike is $K=105$ and the maturity is one year.  The call premium is $C=17$ and the put premium is $P=5$; the risk‑free rate is $r=5\%$.Compute each side of the parity equation. For the call on the left‑hand side: $$C+\dfrac{K}{(1+r)} = 17+\dfrac{105}{1.05}=17+100=117 \,.$$ For the put on the right‑hand side: $$P+S_0 = 5+110=115 \,.$$ Because $117>115$, the call is too expensive relative to the put, so parity is violated.

When $C+\dfrac{K}{(1+r)^T}$ does not equal $P+S_0$, an arbitrageur can lock in a risk‑free profit by buying the cheaper side and selling the more expensive side. To derive the detailed steps, recall when deriving the put–call parity we have used two portfolios, one for the put and the other for the call. To buy one side, create the corresponding portfolio. To sell the other side, act as the counterparty for creating the other portfolio, i.e. buying the option becomes selling the option, investing into a bond becomes borrowing, and buying the underlying becomes shorting it.

## valuation

Unlike forwards and futures where the payoff is linear, and thus valuation is relatively simple; an option has nonlinear payoff, and thus valuation is much more complicated. There are three main ways: binomial options pricing model, Black–Scholes model, and Monte-Carlo simulation-based method.

### binomial options pricing model

The binomial model represents the price of an asset that can move to only two possible levels in one period, up by a factor $u$ (resulting in $u S_0$) or down by a factor $d$ (resulting in $d S_0$).  For a call with strike $K$ and maturity $T=1$, the payoff is $\max(S_T-K,0)$.  With a risk‑free rate $r$, a zero‑coupon bond pays $1+r$ at expiry.

To price a call, one lists the payoffs of the three assets: stock, bond and option in the two possible states. Then a portfolio that holds $w_A$ units of the stock and $w_B$ units of the bond is constructed so that its payoff equals the call’s payoff in both states. Solve the following to get $w_A$ and $w_B$: $$uS_0 w_A + (1+r)S_0 w_B = C_u , \qquad dS_0 w_A + (1+r)S_0 w_B = C_d \,,$$ where $C_u=\max(uS_0-K,0)$ and $C_d=\max(dS_0-K,0)$.  By no arbitrage, the cost of this portfolio must equal the call price, because two identical cash‑flow streams cannot have different values in an efficient market. Hence  $$C = S_0 (w_A+w_B) \,.$$ Similar steps hold for pricing a put.

At each period of the tree, we need to solve for $w_A$ and $w_B$: $$uS_0 w_A + (1+r)S_0w_B = C_u , \qquad dS_0 w_A + (1+r)S_0w_B = C_d \,,$$ where $C_u=\max(uS_0-K,0)$ and $C_d=\max(dS_0-K,0)$. Rewrite in matrix form: $$\begin{bmatrix} uS_0 & (1 + r) S_0 \\ dS_0 & (1 + r) S_0 \end{bmatrix} \begin{bmatrix} w_A \\ w_B \end{bmatrix} = \begin{bmatrix} C_u \\ C_d \end{bmatrix} \,,$$ and by Cramer's rule we obtain the _hedge ratio_ $w_A^*$: $$w_A^* = \frac {(C_u - C_d) (1 + r) S_0} {(u - d) (1 + r) S_0^2} = \frac {C_u - C_d} {(u - d) S_0} \,,$$ and similarly the bond holding $w_B^*$ is: $$w_B^* = \frac {S_0 (u C_d - d C_u)} {(u - d) (1 + r) S_0^2} = \frac {u C_d - d C_u} {(u - d) (1 + r) S_0} \,.$$ The call price can be written compactly as $$C = S_0(w_A^* + w_B^*) = \frac {(1 + r - d) C_u - (1 + r - u) C_d} {(u - d)(1 + r)} \,.$$ Similar calculations hold for pricing a put, or the put–call parity may be used.

An alternative method is to use _risk-neutral_ pricing. Recall that often in finance, the present value of a random cashflow in the future can be calculated as: $$\text{present value} = \frac {\operatorname E[\text{cashflow}]} {1 + r} \,,$$ which holds under _risk-neutral_ assumption. This approach is simply applying this relation given $S, S_u, S_d$. Consider a stock of price $S$, with next period price of either $S_u = uS$ or $S_d = dS$. Risk-neutral probabilities require the probability of going up $p$ to be $$S = \frac {p \cdot S_u + (1 - p) \cdot S_d} {1 + r} \,,$$ and manipulating the expression: $$\begin{aligned} S & = \frac {p \cdot S_u + (1 - p) \cdot S_d} {1 + r} \\ 1 & = \frac {pu + d - pd} {1 + r} \\ p & = \frac {1 + r - d} {u - d} \,, \end{aligned}$$ giving $$p = \frac {(1 + r) - d} {u - d} \qquad 1 - p = \frac {u - (1 + r)} {u - d} \,.$$ Finally, the call price may be calculated as $$C = \frac {p \cdot C_u+(1-p) \cdot C_d} {1 + r} \,,$$ recovering the same equation after substituting the variables. Similar calculations hold for pricing a put, or the put–call parity may be used.

#### recursive binomial options pricing model

For a European option, the second approach can be easily generalized to multi-period trees by repeating the above calculation recursively. For an American option, as the option can be exercised early, the actual call price is the _maximum_ between the European option call price and the payoff if the call is exercised now.

For a European option, in the _continuous limit_ when many increasingly small periods are stacked, the binomial price converges to the Black–Scholes–Merton value given by the Black–Scholes–Merton model.

### Black–Scholes model

For a European call on an asset with current price $S_t$ and standard deviation $\sigma$, strike $K$, risk‑free rate $r$ and time to maturity $\tau=T-t$, the BSM price is $$C = N(d_+)S_t-Ke^{-r\tau}N(d_-),$$ where $$d_+=\frac{\ln(S_t/K)+\bigl(r+\tfrac12\sigma^2\bigr)\tau}{\sigma\sqrt{\tau} }, \qquad d_-=d_+-\sigma\sqrt{\tau} \,.$$ The put–call parity may be used to price a put.

The model assumes that $S_t$ follows a log‑normal process: $\ln S_t$ is normally distributed, so the spot price $S_t$ follows a binomial normal walk. This yields smooth price paths but cannot capture extreme jumps or fat tails (i.e. tail events) observed in real markets. Consequently, extensions such as stochastic volatility models have been proposed, yet the BSM remains a standard benchmark for option valuation.

#### implied volatility

Because the volatility $\sigma$ of the asset is not directly observable, it is inferred from market option prices by solving the BSM equation for $\sigma$. The resulting value is called _implied volatility_ and reflects traders’ collective expectation of future price swings.

#### interpretation of the Black–Scholes model

Consider the BSM price is $$C = N(d_+)S_t-Ke^{-r\tau}N(d_-),$$ where $$d_+=\frac{\ln(S_t/K)+\bigl(r+\tfrac12\sigma^2\bigr)\tau}{\sigma\sqrt{\tau} }, \qquad d_-=d_+-\sigma\sqrt{\tau} \,.$$ A call's value rises with higher volatility; the partial derivative $\partial C/\partial\sigma$ is called _vega_. A call's value also rises with higher spot price; the partial derivative $\partial C/\partial S_t$ is called the _delta_.  An increase in time to maturity $\tau$ raises a European call, giving a positive _theta_ $\partial C/\partial\tau>0$.

## Long-Term Capital Management example

The _Nobel Prize in Economic Sciences_ of 1997 was awarded to Myron Scholes and Robert Merton for their work on option pricing. Their development of the BSM model provided the first systematic framework that links a derivative’s payoff to observable market variables, enabling rational valuation rather than speculation.

Two years after receiving the prize, Scholes and Merton have been part of the hedge fund _Long‑Term Capital Management_ (LTCM) when they received the prize. Two years after receiving the prize (1999), the hedge fund, which uses a highly leveraged strategy, collapsed during the 1999 Asian and Russian crises. The collapse illustrated that even models grounded in solid theory can fail when market assumptions break down or leverage becomes excessive.

From the LTCM example, we see even with a celebrated model such as BSM, predicting actual future prices remains impossible; financial economics focuses instead on _pricing_ uncertain cash flows today given a probabilistic description of the future.  The aim is to determine the rational price for an option under a chosen probability structure, not to forecast specific market outcomes.
