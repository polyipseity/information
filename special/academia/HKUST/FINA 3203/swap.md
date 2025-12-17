---
aliases:
  - FINA 3203 swap
  - FINA3203 swap
  - HKUST FINA 3203 swap
  - HKUST FINA3203 swap
  - swap
tags:
  - flashcard/active/special/academia/HKUST/FINA_3203/swap
  - language/in/English
---

# swap

- HKUST FINA 3203

---

- see: [general/swap (finance)](../../../../general/swap%20(finance).md)

A __swap__ is an over‑the‑counter agreement in which two parties exchange a series of cash flows at predetermined dates $T_{1}<\dots <T_{m}$ up to a terminal date $T$. Unlike a forward contract, which exchanges assets or cash flows on a single pre‑specified date, a swap can hedge a stream of risky payments. Thus a forward is simply a one‑payment swap. The initial cost of establishing a swap is zero; the contract may be settled either physically or in cash and involves counterparty risk.

## types

Swaps encompass many varieties: commodity swaps, interest‑rate swaps, currency swaps, credit‑default swaps, total‑return swaps, variance swaps, inflation swaps, and more. Each type exchanges different underlying cash flows but follows the same basic structure of a sequence of payments.

_Example_: An industrial producer that must purchase $N_{0}=100{,}000$ barrels of oil at dates $T_{1}=1$ year and $T_{2}=2$ years may enter a commodity swap. The spot price today is $S_{0}=18.5$ USD/bbl. The implied forward curve $$F_{0,t}=S_{0}e^{r_{0,t}t}$$ shows that the market expects the oil price to rise from 18.5 to about 20–21 over the next two years. These forward prices are quoted as $F_{0,1}\approx 20$ USD/bbl for one‑year delivery and $F_{0,2}\approx21$ USD/bbl for two‑years. The swap price is $x=20.483$ USD/bbl. If _physical settlement_ is used: on each delivery date the buyer receives a barrel of oil at price $x$. If _cash settlement_: on each date the buyer pays the counterparty
$N_{0}\bigl(x-S_{T_{i} }\bigr)$; if this difference is negative, the buyer receives the amount. In both cases the effective purchase price equals $x$.

## market sizes

Bank of International Settlement (BIS) semi‑annual OTC derivative statistics (2024‑S2) show that swaps are a large portion of the market: interest‑rate swaps alone account for about 46% of all contract notional, while currency and commodity swaps also represent significant volumes. Forward contracts form a smaller share compared with total swaps.

## settlement

A swap may be settled physically or in cash. In physical settlement the buyer obtains the underlying asset at the agreed price; in cash settlement the parties exchange the difference between the fixed swap price and the market spot on each payment date, thereby achieving the same effective price while avoiding delivery logistics.

## valuation

The value of a commodity swap can be found by replicating it with forwards and zero‑coupon bonds.  At time $t=0$ the long side receives at each payment date $T_{i}$ the amount $(S_{i}-x)$, where $S_{i}$ is the spot price of the commodity and $x$ is the fixed swap rate to be determined.  A replicating portfolio consists of a forward contract for each maturity together with a short position in an appropriate zero‑coupon bond so that the cash flows at every payment date match those of the long swap.

For the two‑period example the replication uses a one‑year forward, a two‑year forward and two zero‑coupon bonds.  The present value of this portfolio is  $$(20-x)e^{-r_{0,1} }+(21-x)e^{-2r_{0,2} }$$ and must equal zero because the long swap has no initial cost.  Solving for $x$ gives $$x=\frac{20e^{-r_{0,1} }+21e^{-2r_{0,2} } }{e^{-r_{0,1} }+e^{-2r_{0,2} } } \,,$$ and in general gives $$x = \frac{\sum_{i=1}^{m}F_{0,T_i}\,e^{-r_{0,T_i}T_i} }              {\sum_{i=1}^{m}e^{-r_{0,T_i}T_i} } = \sum_{i=1}^m w_i F_{0,T_i} \,.$$ The numerator is the discounted forward price of each payment and the denominator is the sum of discount factors.  The result is a weighted average of the forwards, where the weight for maturity $T_i$ equals $$w_i=\frac{e^{-r_{0,T_i}T_i} }          {\sum_{j=1}^{m}e^{-r_{0,T_j}T_j} } .$$ For the oil swap in the lecture notes the forward curve implied a price of $x=20.483$ USD per barrel.

### valuation after inception

A swap that has already started no longer has zero market value.  The value at an intermediate time $t_e<T_1$ is the expected present value of the remaining cash flows, discounted from each future payment date back to $t_e$.

To find this value we construct a new portfolio that exactly replicates the remaining payments: long a fresh swap with maturity dates $T_{i}>t_e$ with new fixed swap rate $x_{t_e}$; buy $(x_{t_e}-x)$ units of a zero‑coupon bond maturing at each $T_i$. Using the two-period example again, the present value of this replication is $$(x_{t_e}-x)e^{-r_{t_e,1}(T_1-t_e)}+(x_{t_e}-x)e^{-r_{t_e,2}(T_2-t_e)} \,.$$ Because the new swap has zero initial cost, the market value of the original long position equals this expression. In general, the expression is $$(x_{t_e} - x) \sum_{j = 1}^m e^{-r_{t_e,t_j}(T_j - t_e)} \,.$$  The required inputs to find the new fixed swap rate $x_{t,e}$ are therefore the current forward prices $F_{0,T_i}$ (or equivalently the discount factors and the fixed rate $x$) and the prevailing short‑rate curve $\{r_{t_e,T_i}\}$.

If $T_1<t_e<T_2$, only the payment at $T_2$ remains; the replication uses a one‑year forward maturing at $T_2-t_e$ and a zero‑coupon bond of that maturity.  The value is then $(x_{t_e}-x)e^{-r_{t_e,1}(T_2-t_e)}$.

Thus the swap’s market price evolves with changes in forwards, discount factors and the original fixed rate, reflecting new information about commodity prices and interest rates.

## interest-rate swaps

An _interest‑rate swap_ (IRS) is an over‑the‑counter contract in which two parties agree to exchange a series of interest payments on a fixed notional amount.  One party, the _receiver_, receives the fixed rate, and is the _short_ position because it is protected against decreasing floating rate; the other, the _payer_, makes the fixed payments and receives floating rates that are linked to a short‑term benchmark (usually LIBOR or an equivalent), and is the _long_ position because it gains from increasing floating rate.

An IRS is characterised by: notional principle, swap rate, maturity, and payment frequencies.

- _Notional principle_ ::@:: – the notional amount on which interest payments are calculated.  
- _Swap rate_ $R$ ::@:: – the fixed annualised rate agreed at inception.  (annotation: __this course__: The rate is continuously compounded by default, i.e. the equations below should use $e^r$ rather than $r$)
- _Maturity (swap tenor)_ ::@:: – the last payment date, denoted $T_m$.  
- _Payment frequencies_ ::@:: – the floating leg usually follows money‑market conventions (e.g., quarterly 3‑month LIBOR); the fixed leg often uses a corporate‑bond convention (e.g., semi‑annual).  

The swap is settled in cash: at each payment date $T_i$ the net amount paid by the _payer_ (the _long_ position) is $$N_{i}= \bigl(r_{\text{fixed} }-r_{\text{float},\,i}\bigr)\,P ,$$ where $P$ is the notional principal.  The floating leg (the _receiver_, the _short_) pays $P\, r_{\text{float},\,i}$, while the fixed leg (the _payer_, the _long_) pays $P\, r_{\text{fixed} }$. The two legs are _netted_: at each date the counterparty that owes the larger payment makes the net transfer.  Thus, in a single settlement cash is exchanged rather than the underlying asset. Because only the difference matters, the contract has no initial cost; its value evolves with changes in the forward curve and the short‑rate term structure.

### interest-rate swap examples

_Managing duration mismatch_: A bank that lends at fixed rates but borrows on floating terms faces a gap between asset and liability durations. By paying fixed and receiving floating, the bank can align its cash‑flow profile with the cost of funds.

_Speculation on economic cycles_: In a recessionary environment where LIBOR is expected to fall, a hedge fund may enter an IRS as a _receiver_, hoping that fixed payments will exceed floating ones.

_Synthetic corporate bonds_: A company that can only issue short‑term bank debt (corporate bonds are very expensive if low credit rating) may use an IRS to transform its floating liabilities into a long‑dated fixed‑rate obligation.  The swap replaces the rolling cost of short loans with a single fixed payment stream, reducing credit exposure and borrowing costs. For instance, in 2006 a firm bought a three‑year IRS with fixed rate $R=6.95\%$.  With the observed one‑year rates $r_{10,11}=5.83\%,\, r_{11,12}=4.88\%,\, r_{12,13}=7.70\%$, the net cash flows to the firm over the three years are $$\begin{aligned} \text{Dec 2011}&: \;1\,M(e^{0.0583}-e^{0.0695})=60\,000-72\,000=-12\,000,\\ \text{Dec 2012}&: \;1\,M(e^{0.0488}-e^{0.0695})=50\,000-22\,000=-8\,000,\\ \text{Dec 2013}&: \;1\,M(e^{0.0770}-e^{0.0695})=80\,000+72\,000=152\,000 . \end{aligned}$$ The net result is a conversion of a three‑year floating loan into an effective fixed‑rate debt, giving the firm certainty about future payments.

### valuation of interest-rate swaps

The fixed‑rate leg of an interest‑rate swap can be replicated by holding a fixed‑coupon bond and shorting a floating‑rate bond that both mature at the same date.  

For example, for a swap with maturity $T_m = 13$ the cash flows to the party that is _short_ the swap (_receive_ fixed payments) are  $$0,\; e^{R}-e^{r_{10,11} },\; e^{R}-e^{r_{11,12} },\; e^{R}-e^{r_{12,13} },$$ where $R$ is the swap rate and $r_{i,j}$ denotes the one‑year forward rate observed at time $i$ for a loan ending in year $j$.  To replicate these cash flows we buy a fixed‑coupon bond that pays the coupon $(e^{R}-1)$ each year and sell a floating‑rate bond whose payment at the end of year $t$ is $e^{r_{t-1,t} }-1$.  The current cost to buy and sell said bonds is $$\text{cost}=B_{\text{fix} }(0)-B_{\text{float} }(0).$$ Because the floating‑rate bond can be decomposed into a series of one‑year zero‑coupon bonds, its price equals its par value: $$B_{\text{float} }(0)=1.$$ The fixed‑rate bond’s price is the discounted sum of its coupon payments plus the principal at maturity, $$B_{\text{fix} }(0)=(e^{R}-1)e^{-r_{10,11} } + (e^{R}-1)e^{-r_{10,12}\!\times 2} + ((e^{R}-1)+1) e^{-r_{10,13}\!\times 3}.$$ No‑arbitrage requires $B_{\text{fix} }(0)=B_{\text{float} }(0)$, hence $$e^{R}=\frac{1 + e^{-r_{10, 11} } + e^{-r_{10,12} \times 2} }{e^{-r_{10,11} } + e^{-r_{10,12}\!\times 2} + e^{-r_{10,13}\!\times 3} } \,,$$ which is easily generalized. With the observed one‑year rates $r_{10,11}=5.83\%$, $r_{10,12}=6.50\%$ and $r_{10,13}=7.00\%$ we obtain $R=6.95\%$. Thus the swap rate is determined by the discount factors implied by the forward curve.

## total-return swaps

A total‑return swap (TRS) exchanges the return of an asset for a fixed or variable payment. Typically, the payment is a return on a risk‑free benchmark plus a fixed spread. For example, one party pays the _total return_ of, say, a junk‑rated corporate bond; the counterparty pays the total return of a Treasury bond plus a fixed spread.

The contract lets the holder of the risk bond insure the risky asset on its balance sheet, while the other party obtains exposure to the asset's return and can benefit from regulatory or funding advantages without recording it on the balance sheet.

## volatility and variance swaps

A volatility swap is an agreement to exchange realized variance (or volatility) of an underlying over a set period for a fixed strike $K_{\text{vol} }$.  The payoff to the long side is  $$(\sigma_{\text{realized} }-K_{\text{vol} })\,N,$$ where $\sigma_{\text{realized} }$ is the realized volatility and $N$ is the notional.

Because only volatility enters the payoff, a volatility swap gives pure exposure to changes in volatility, unlike an option whose payoff also depends on the underlying price.  Traders use them for directional bets on future volatility, for trading the spread between implied and realised volatility, or for hedging portfolio tracking‑error that grows with market turbulence.  

A variance swap is analogous but exchanges realized variance instead of volatility.

## largest losses

A number of institutions have suffered multibillion‑dollar losses in the past decade through derivatives such as credit default swaps, equity futures and total‑return swaps.  For example, Archegos Capital Management incurred a loss of about USD 10 billion in 2021 on total‑return swaps; Morgan Stanley lost roughly USD 9 billion on credit‑default swaps in 2008; JPMorgan Chase suffered around USD 9 billion in credit‑default losses in 2012.  Other notable events include a USD 8.5 billion loss to Deutsche Bank on copper futures in 1996, and a USD 4.1 billion hit to UBS from the collapse of the leveraged bond positions of Pershing Square in 2020.  These cases illustrate how concentrated exposure and leverage can amplify losses.

## Archegos example

Archegos was a family office founded in 2013 by former hedge‑fund manager Bill Hwang.  Family offices manage wealth for a single family; they are exempt from SEC registration and disclosure, allowing them to keep their portfolios private.  In 2020–21 Archegos built a portfolio of more than USD 100 billion worth of equity positions, often with exposure exceeding 10% of the underlying shares.  The firm largely used total‑return swaps (TRS) to take long positions without purchasing the stocks outright; the banks that acted as prime brokers recorded the securities on their own balance sheets and received a fee while Archegos retained only the P&L.

In March 2021, the collapse began when Viacom’s share price fell about 20% after an aborted public offering.  Then Discovery and Iqiyi also dropped. The drop triggered margin calls, and after a failed emergency meeting on 25 March 2021 with the banks to coordinate an orderly sale of its portfolio, Archegos defaulted.

After Archegos defaulted, banks faced a prisoner's dilemma: if no one sells and Archegos's TRS portfolio rebounded, then all banks will be fine. But if any bank starts selling then the prices would plummet.  In the end, banks sold off the positions at steep discounts—Morgan Stanley liquidated USD 5 billion of holdings that day, Goldman Sachs sold USD 10 billion the next morning, and other banks followed suit, creating a $30 billion sell‑off that left Credit Suisse and Nomura with large losses.

### responses to the Archegos episode

The U.S. Securities and Exchange Commission charged Hwang with 11 criminal offences, alleging that he entered TRS contracts without economic purpose to inflate stock prices and misled counterparties about exposure and liquidity.  The case highlights the risks of opaque derivatives and the importance of counterparty risk management.

In reaction to the Archegos episode, banks that funded Elon Musk's $44&nbsp;billion X (formerly Twitter) deal such as Morgan Stanley, Barclays and Bank of America, shocked by X's deteriorating finance, negotiated a joint “sell‑down” agreement that restricts each bank from accepting offers for its loans without giving the others a pro‑rata right.  This arrangement prevents a single lender from offloading assets independently, reducing the chance that a chain reaction will force multiple institutions into distress.
