---
aliases:
  - FINA 3203 option
  - FINA3203 option
  - HKUST FINA 3203 option
  - HKUST FINA3203 option
  - option
tags:
  - flashcard/active/special/academia/HKUST/FINA_3203/option
  - language/in/English
---

# option

- HKUST FINA 3203

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

## option types

_Stock options_ trade on exchanges such as CBOE, AMEX, PHLX, NYSE Arca, BATS, ISE, among others. A standard contract usually represents $100$ shares of the underlying stock, though the exact convention varies and must be verified for each ticker. These contracts are American‑style: they can be exercised at any time up to expiration. Most U.S. equity options expire on the day after the third Friday of a month; the next two months’ contracts are usually listed together with two more months further out in the cycle. Because dividends do not affect option pricing directly, the contracts are not adjusted for dividend payments but they _are_ adjusted when the underlying undergoes a stock split, similar to forward and futures adjustments.

_Index options_ are almost always European‑style: exercise is only possible on expiration day. Typical indexes that have liquid option markets include DJIA, S&P 100, S&P 500, Nasdaq 100, and Russell 2000 (traded mainly on CBOE). Their values depend on the level of the underlying index rather than any single company.

_Foreign currency options_ are primarily traded on PHLX. The contract specifies a fixed amount of one currency that can be exchanged for another at an agreed rate. Because currencies move in pairs, the payoff depends on the relative change between the two.

_Options on futures_ are options written on commodity or financial futures contracts—agricultural, oil, livestock, metals, currency, and stock‑index futures. A common example is an option on the 30‑year Treasury Bond Futures traded at CBOT. The option’s value derives from the price movement of the underlying future.

## trading

The timing of option expirations influences market behaviour. For instance, on a day when many contracts expire—such as the S&P 500 “OpEx” event in late October 2022—large volumes of puts or calls can be exercised or rolled. In that case, about $13{,}000$ S&P 500 puts with a strike near 3,900 were traded, causing implied volatility to fall by almost two points within two hours. Dealers often buy shares to stay delta‑neutral when clients sell options, which can move the underlying index.

For example, Apple Inc. (AAPL) offers a wide range of strike prices and expiration dates. For example, on 12 October 2018 there were calls at strikes $200$, $202.5$, $205$, $207.5$, $210$, $212.5$, $215$, $217.5$, and $220$. Each contract lists the last trade price, bid–ask spread, trading volume, and open interest.

## trading strategies

Options can be combined in many ways to shape payoff profiles that suit a trader’s risk‑return preferences. It can draw any desired payoff using a portfolio of options, provided that liquidity exists for the needed options.

Typical combinations include the _protective put_, the _money spread_ (also called _bull call spread_) and the _straddle_. These constructions act as tools for managing exposure rather than pure speculation. These three strategies respectively illustrate how option combinations can be used to hedge, limit risk or capture volatility.

Option trading strategies can be split into two broad families, a natural split is _directional_ versus _neutral_.  Bull spreads and bear spreads belong to the directional group, while butterflies, straddles, strangles and covered positions fall into the neutral group because their payoff depends mainly on volatility rather than on a particular price direction.

### protective put

A _protective put_ is formed by buying a share of the underlying asset together with a put option on that same asset. If the market falls, the put limits losses; if it rises, the stock’s gains are largely unhindered.  

For example, suppose an investor holds one share of a stock whose current price is $\$70$ and buys a put with strike $K=50$. The payoff diagram shows that when the final stock price falls below $\$50$, the holder receives the difference $K-S_T$; otherwise the payoff is zero. Thus the combined position behaves like owning the share plus an insurance contract that pays off whenever the price drops below the strike.

Compared to shorting a forward of forward price $F_{0, T} = K$, it costs something to buy a protective put. This is because longing a put allows us to keep the gain if the stock rises, whereas shorting a forward does not.

### covered call

A _covered call_ is constructed by holding one share of the underlying asset and writing (selling) a call option on that same asset. The net payoff at maturity $T$ is $$\text{Covered Call}=S_T-\max(S_T-K,0),$$ where $S_T$ is the stock price at expiry and $K$ is the strike of the written call.  
The position behaves like owning the share for as long as the price stays below the strike; once $S_T>K$, the excess above $K$ is surrendered to the option holder, leaving the payoff flat at $K$. Thus the upside potential is capped while a small premium is earned when the call is written.

The payoff diagram shows a line rising with slope one up to $S_T=K$, after which it levels off. This shape reflects that the stock’s gains beyond the strike are exchanged for the call premium received. It is called a covered call because a higher spot price than the strike price makes the seller lose, so the seller buys the underlying itself to cover the call.

A covered call is typically used when an investor expects a flat or mildly bullish market: the investor receives the option premium immediately, and if the stock stays below $K$ at expiry the payoff equals the original share price plus that premium. If the stock surges past $K$, the upside beyond the strike is lost, but the earned premium partially cushions the overall return. This trade‑off makes covered calls a popular income‑generation technique in portfolio management.

### synthetic forward

A _synthetic forward_ is built by combining a long call and a short put with the same strike $K$ and maturity $T$. The payoff of this position equals $$C_T - P_T = S_T-K,$$ which matches exactly the payoff of a conventional forward that obligates delivery of one share at price $K$ on date $T$.  

Because the call and put are priced according to the put‑call parity, choosing the strike equal to the desired forward price makes the initial cost of the synthetic position zero. If the chosen strike differs from the true forward price $F_{0,T}$, an amount $(K-F_{0,T})e^{-rT}$ is paid or received at inception.

_Examples_: For a lower strike such as $K=60$, the synthetic position yields a steep linear increase in value once the stock price rises above 60, mirroring a long forward at that strike. At an intermediate strike $K=100$ the payoff is identical to a standard forward with forward price $F_{0,T}=100$. With a higher strike like $K=140$, the synthetic position still follows the linear relation $S_T-K$, but because $K$ exceeds the market‑implied forward, the holder pays an upfront premium.

These examples show that by adjusting $K$ one can replicate forwards of different prices while keeping the same maturity. For retail investors who wish to hold a forward but cannot access OTC contracts, constructing a synthetic forward with options offers a flexible alternative that avoids large contract sizes and daily mark‑to‑market requirements.

### bull spread

A _bull spread_ is built by taking a position that profits when the underlying rises and limits the maximum gain.

A _money spread_ or _bull call spread_ is created by buying a call with a lower strike and simultaneously selling another call with a higher strike. The resulting payoff rises when the underlying moves up but is capped, limiting upside potential without downside risk, and the net premium is cheaper.

For instance, buying a call at $K_1=50$ while writing one at $K_2=60$ yields a net payoff that starts at zero, climbs linearly from $\$50$ to $\$60$, and then levels off after $\$60$. The maximum gain equals the difference of strikes minus the net premium paid.

A _bull put spread_ is essentially the counterparty to _bear put spread_, and the profit come from the premium instead of the puts being exercised.

### bear spread

A _bear spread_ is built by taking a position that profits when the underlying falls and limits the maximum loss.

A _bear put spread_ is created by selling a put with a lower strike and simultaneously buying another put with a higher strike. The resulting payoff rises when the underlying falls up but is capped, limiting upside potential without downside risk, and the net premium is cheaper.

For instance, selling a put at $K_1=50$ while writing one at $K_2=60$ yields a net payoff that starts at zero, climbs linearly from $\$60$ to $\$50$, and then levels off after $\$50$. The maximum gain equals the difference of strikes minus the net premium paid.

A _bear call spread_ is essentially the counterparty to _bull call spread_, and the profit come from the premium instead of the calls being exercised.

### straddle

A straddle consists of buying both a call and a put with identical strike $K$. This strategy profits when the underlying moves significantly in either direction, regardless of the direction. If at maturity the price is far from $K$, one leg pays off while the other expires worthless; if it stays near $K$, both legs lose value. The payoff diagram for a long straddle therefore rises on both sides of the strike price.

### strangle

A _strangle_ consists of buying a put and a call with different strikes, the put having the lower strike $K_{0}$ and the call the higher strike $K_{1}$. The strategy profits when the underlying asset moves far enough in either direction to make one leg exceed the cost of both legs. If at expiry the price lies between $K_{0}$ and $K_{1}$, both options expire worthless and the trader loses the premiums paid; if the price is below $K_{0}$ or above $K_{1}$, the losing leg is offset by a gain in the winning leg.

For example, with $K_{0}=80$ and $K_{1}=120$, the payoff diagram shows that the net profit starts at zero when $S_T=100$, and rises linearly as $S_T$ falls below 80 or climbs above 120. The break‑even points are found by adding the total premium to each strike: $K_{0}+\text{premium}$ on the upside and $K_{1}-\text{premium}$ on the downside.

Because the payoff of a strangle is never higher than that of a straddle, a strangle is cheaper than a straddle that uses the same middle price as both legs; the lower cost reflects the wider payoff interval but also reduces the maximum attainable profit.

### butterfly spread

A _butterfly spread_ uses three options of the same type with different strikes, arranged so that the middle strike equals the arithmetic mean of the outer strikes: $K_{1}=(K_{0}+K_{2})/2$.  For a call‑based butterfly the payoff is  $$
-\,2C(K_{1})+C(K_{0})+C(K_{2}),$$ which rises from zero when the stock price is below $K_{0}$, reaches a maximum of $K_{1}-K_{0}$ at $S_T=K_{1}$, and falls back to zero when $S_T$ exceeds $K_{2}$.  The same payoff applies for a put-based butterfly: $$-2P(K_1) + P(K_0) + P(K_2) \,.$$

Because the position is neutral with respect to direction—its payoff is highest when the underlying stays near $K_{1}$—it is typically employed when an investor expects low volatility or a narrow trading range.

## put–call parity

The _put–call parity_ links _European_ (not _American_) call and put options on the same underlying asset with identical strike price $K$ and maturity $T$. Two self‑financing portfolios generate the same payoff, so their costs must be equal in an efficient market.

A portfolio that buys a call and a zero‑coupon bond that pays $K$ at time $T$ has current cost $C+\dfrac{K}{(1+r)^T}$; the payoff at expiry is $K + \max(S_T - K, 0)$. The second portfolio that buys a put and the underlying asset yields current cost $P+S_0$; the payoff at expiry is also $S_T + \max(K - S_T, 0) = K + \max(S_T - K, 0)$. Because at expiry, the two portfolios result in owning the underlying asset _and_ have identical payoffs for every possible value of the spot price at expiry, their present values must be equal. Hence $$C+\frac{K}{(1+r)^T}=P+S_0 .$$ If this relationship fails, an arbitrage opportunity exists.

An alternative portfolio: long put and short call, and the payoff at expiry is $\max(K - S_T, 0) - \max(S_T - K, 0) = K - S_T$, which looks like short forward of forward price $K$. Then long forward at forward price $F_{0, T} = S_0 e^{rT}$. Now, payoff at expiry is always $(K - S_T) + (S_T - F_{0, T}) = K - S_0 e^{rT}$. Thus, this payoff discounted to the present must be how much the price of a put exceeds a call: $$P - C = K e^{-rT} - S_0 \,,$$ yielding the same relation as above (but this one uses the continuously compounded $r$).

From the parity equation: $$C+\frac{K}{(1+r)^T}=P+S_0 \,,$$ one can see increasing the strike price $K$ increases the put premium $P$, because one can guarantee to sell for at least $K$. Increasing the spot price $S_0$ increases the call premium $C$, higher spot price typically implies higher future expected spot. And finally, fixing other parameters, increasing the premium of one of the option raises the premium of the other option, which can be interpreted as increased volatility.

### put–call arbitrage

Suppose a stock trades at $S_0=110$, the strike is $K=105$ and the maturity is one year.  The call premium is $C=17$ and the put premium is $P=5$; the risk‑free rate is $r=5\%$.Compute each side of the parity equation. For the call on the left‑hand side: $$C+\dfrac{K}{(1+r)} = 17+\dfrac{105}{1.05}=17+100=117 \,.$$ For the put on the right‑hand side: $$P+S_0 = 5+110=115 \,.$$ Because $117>115$, the call is too expensive relative to the put, so parity is violated.

When $C+\dfrac{K}{(1+r)^T}$ does not equal $P+S_0$, an arbitrageur can lock in a risk‑free profit by buying the cheaper side and selling the more expensive side. To derive the detailed steps, recall when deriving the put–call parity we have used two portfolios, one for the put and the other for the call. To buy one side, create the corresponding portfolio. To sell the other side, act as the counterparty for creating the other portfolio, i.e. buying the option becomes selling the option, investing into a bond becomes borrowing, and buying the underlying becomes shorting it.

## valuation

Unlike forwards and futures where the payoff is linear, and thus valuation is relatively simple; an option has nonlinear payoff, and thus valuation is much more complicated. There are three main ways: binomial options pricing model, Black–Scholes model, and Monte-Carlo simulation-based method.

### no-arbitrage bounds

The price of an option must satisfy simple inequalities that prevent arbitrage opportunities: nonnegative premium

A call or put cannot have a negative premium, so for any maturity $t$: $$C_{t}\ge 0 , \qquad P_{t}\ge 0 .$$ If market data ever show a negative premium, it is an obvious arbitrage opportunity to long that option: you gain from the negative premium and you will never lose at expiry.

For European options on non‑dividend stocks, the call price is bounded above by the spot value of the underlying: $$C_{t}\le S_{t}.$$ It can be derived from the put–call parity: $P + S_0 = C + K e^{-rT}$. To maximize $C$, set the strike price $K$ to the minimum 0. Since $K$ is 0, a put would never gain or loss, so its premium $P = 0$. Hence $C = S_0$ is the maximum. If an observed call exceeded $S_{t}$, arbitrage would be possible by selling the call for being overpriced and buying the stock at $S_0$ now in case the call is exercised in the future.

Similarly, a European put cannot exceed the present value of the strike price discounted at the risk‑free rate: $$P_{t}\le K\,e^{-r(T-t)} .$$ It can also be derived from the put–call parity: $P + S_0 = C + Ke^{-rT}$. To maximize $P$, set the spot price $S_0$ to the minimum 0. Since $S_0$ is 0, a call would never gain or loss, so its premium $C = 0$. Hence $P = Ke^{-rT}$ is the maximum. A put that is more expensive than this bound would allow an arbitrage by selling the put for being overpriced and investing $Ke^{-r(T-t)}$ in case the put is exercised in the future.

Beyond these simple limits, an option’s value is never lower than the payoff of a corresponding forward position of the same maturity and a forward price of $F_{t,T} = K$. A long call (or short put) behaves like the forward described above without the negative payoffs; a short call (or long put) behaves like the forward described above without the negative payoffs. Consequently, the option must be at least as valuable as the forward described above.

Additionally, there are bull spread inequality and calendar spread inequality, which are crucial for market makers: they ensure that quotes for different strikes and maturities cannot be exploited by a _static arbitrage_ strategy, in which one execute option trades such that one may gain in the future at a negative price today. If a violation appears, it signals an inconsistency in the quoted prices or in the underlying model assumptions. Ensuring the inequalities hold keeps the option surface free of risk‑free profits.

#### bull spread inequality  

For European calls the price of a call with strike $K_{1}$ cannot exceed the price of a call with a higher strike $K_{2}>K_{1}$ by more than the present value of the strike difference: $$\operatorname{Call}(K_{1},T)-\operatorname{Call}(K_{2},T)\le e^{-rT}(K_{2}-K_{1}) .$$ The proof follows from a simple payoff comparison.  If $S_T<K_1$ the portfolio of long $\text{call}(K_{1})$ and short $\text{call}(K_{2})$ pays zero;  if $K_{1}\le S_T < K_{2}$ it yields $S_T-K_{1}$;  if $S_T\ge K_{2}$ it yields $K_{2}-K_{1}$.   Thus the terminal payoff never exceeds $K_{2}-K_{1}$, and after discounting we obtain the inequality above.  This bound guarantees that a bull‑spread—long a lower‑strike call and short a higher‑strike call—cannot cost more than the discounted strike spread, preventing an arbitrage opportunity.

#### calendar spread inequality

A _calendar spread_ involves taking opposite positions in calls of different maturities but similar strikes. If we write a short call with maturity $T_{1}$ and strike $K_{1}$, and long a call with maturity $T_{2}>T_{1}$ and strike $K_{2}=K_{1}e^{r(T_{2}-T_{1})}$, then the no‑arbitrage condition is  $$\operatorname{Call}(K_{1},T_{1})\le \operatorname{Call}(K_{2},T_{2}) .$$  If this inequality does not hold, an arbitrage can be realised by selling the overpriced short‑term call and buying the cheaper long‑term call. At maturity $T_{1}$ the short call obliges us to deliver $\max(S_{T_{1} }-K_1, 0)$. Meanwhile, the present value of the long call is at least $S_{T_{1} } - K_2 e^{-rT(T_2 - T_1)} = S_{T_1} - K_1$ from the value of a forward of the same maturity and forward price $F_{T_1, T_2} = K_2$, which can always cover the short call.

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

## Barings Bank example  

The collapse of Barings Bank in February 1995 is a textbook illustration of how derivatives can amplify risk. A rogue trader, Nick Leeson, had accumulated huge positions in Nikkei 225 futures and other instruments while hiding the losses from the back-office controls (as he was both the head of settlement and the only trader at the front-office).

When the 17 January 1995 Kobe earthquake knocked the index down, Leeson continued buying futures rather than cutting his exposure. By 30 January the market recovered partially with small accumulated loss for Leeson, but he persisted, hoping the recovery would continue to erase the accumulated shortfall; instead the position blew up as the market continues to drop.

To cover the mounting margin calls, Leeson sold both call and put contracts—effectively writing _straddles_ and _strangles_—and collected the premiums. The strategy was aimed at profiting from volatility while still betting on an upward move in the Nikkei. However, it was inconsistent: selling options would lose money if the index rise, yet he also wanted a rise to recover losses. This combination of speculative behaviour, lack of risk limits and insufficient supervision led to the bank’s failure.

## ancient option example  

In Aristotle’s writings one finds what can be read as an early form of an option. Thales, a Greek philosopher, secured the right to rent olive‑presses for the upcoming season in exchange for his savings. The agreement allowed him to use the presses at the normal rate if the harvest turned out good; otherwise he would simply pay that rate and forgo the extra benefit. In modern terms this is a _call_ with underlying set to the _right_ to use the presses (not the presses themselves), strike equal to the standard rental price, maturity set to the end of the season, and an initial premium represented by Thales’s savings. The payoff is zero if the harvest (and thus the rent) stays below the agreed level, but it becomes positive when the harvest exceeds expectations. Thus the story illustrates the basic structure of a call option even though no formal contract existed at that time.
