---
aliases:
  - FINA 3103 fixed income
  - FINA3103 fixed income
  - HKUST FINA 3103 fixed income
  - HKUST FINA3103 fixed income
  - fixed income
tags:
  - flashcard/active/special/academia/HKUST/FINA_3103/fixed_income
  - language/in/English
---

# fixed income

- HKUST FINA 3103

---

- see: [general/fixed income](../../../../general/fixed%20income.md)

__Fixed income__ securities are financial claims that promise cash flows of a predetermined amount at fixed dates.  They include instruments such as government bonds, which pay a pre‑determined coupon and return the face value when the bond matures.

## definition

A fixed‑income security is specified by its _bond value_, _principal (face value)_, _maturity_, and _coupon_.  The bond value refers to the market price or the yield that equates the price with future cash flows.  The principal is the amount repaid at maturity, the maturity indicates when redemption occurs, and the coupon is the periodic payment made by the issuer.

Consider a five‑year bond with a face value of $\$1{,}000$ and an annual coupon rate of $5\%$.  The cash flows are: five coupon payments of $\$50$ each year, followed by a final payment of the face value $\$1{,}000$.

## valuation

To determine the current price $P$ of a bond that pays coupons and redeems principal, one discounts all future cash flows at an appropriate interest rate.  With a constant discount rate $r$, $$P=\sum_{t=1}^{T}\frac{C}{(1+r)^t}+\frac{\text{FV} }{(1+r)^T},$$ where $C$ is the coupon payment, $\text{FV}$ the face value and $T$ the maturity in years.  In practice, market prices may differ from this theoretical value because of risk or changes in expectations.

### zero-coupon bonds

A bond with no coupon ($C=0$) is called a _zero‑coupon_ (or discount) bond.  It trades below face value and repays the principal only at maturity: $$P_{0,T}=\frac{\text{FV} }{(1+r)^T}.$$ Such bonds are also known as STRIPS (_Separate Trading of Registered Interest and Principal of Securities_).

### coupon bonds

A coupon payment can be viewed as the redemption of a zero‑coupon bond with face value $C$.  Therefore, the price of a coupon bond equals the sum of the prices of corresponding discount bonds: $$P=\sum_{t=1}^{T} C\,P_{0,t}+ \text{FV}\,P_{0,T},$$ where $P_{0,t}$ is the price of a zero‑coupon bond maturing at time $t$.  

For example, a three‑year coupon bond with $C=5\%$ and $\text{FV}=100$ can be replicated by holding five one‑year and two‑year discount bonds plus 105 three‑year discount bonds, all of these each with face value $\$1$.

### yield to maturity

When a bond’s price $P$ is observed but the discount rate is unknown, the _yield to maturity_ (YTM) is the constant interest rate that makes the present value of all future payments equal to the market price.  Formally the YTM $y$ solves $$P=\sum_{t=1}^{T}\frac{C}{(1+y)^t}+\frac{\text{FV} }{(1+y)^T},$$ where $C$ is the coupon, $\text{FV}$ the face value and $T$ the maturity.  Because the equation is nonlinear in $y$, no closed‑form solution usually exists; it is found numerically or with spreadsheet functions such as Excel’s RATE.  If a bond trades below par, its YTM exceeds the coupon rate, and vice versa.

_Example_: A twenty‑year bond has $\text{FV}=1{,}000$, an annual coupon of \$35 (3.5 %) and is priced at \$950.  Solving $$950=\sum_{t=1}^{20}\frac{35}{(1+y)^t}+\frac{1{,}000}{(1+y)^{20} }$$ gives $y\approx3.86\%$.  The lower price therefore yields a higher return.

### yield curve

The _yield curve_ plots the YTM against maturity for bonds of identical credit quality (typically sovereign).  When the market is arbitrage‑free, the relationship between short‑term and long‑term rates determines the shape of the curve.  An upward‑sloping curve means that longer maturities command higher yields; a downward or inverted curve indicates expectations of falling short‑term rates and often precedes recessions.

_Example_: Suppose a two‑year zero‑coupon bond has yield $y(2)$ and a one‑year bond has yield $y(1)=1\%$.  If the government signals that the one‑year rate in 2026 will rise to $5\%$, no‑arbitrage requires $$(1+y(2))^2=(1+y(1))(1+5\%) ,$$ implying $y(2)>y(1)$.  The curve must therefore be upward sloping.

When the market reports that short‑term rates are rising or falling, bond prices move in the opposite direction because the discount factor becomes larger or smaller.  In a _bullish_ environment investors buy bonds, pushing prices up and yields down; conversely, in a bearish setting prices fall while yields rise.  Analysts often describe how quickly the yield curve steepens or flattens.  A _steep_ curve means long‑term rates are markedly higher than short‑term ones, whereas a _flat_ curve indicates little difference between short‑ and long‑term yields; these terms help summarize whether the market expects rapid changes in future interest rates. For example, both _bull steep_ and _bull flat_ describe lowering yield curve, but the former results in a steeper slope than before whereas the latter results in the opposite.

### spot rate

The current $T$-year spot rate $r_{0,T}$ aggregates the short‑term rates prevailing at each year from the present to maturity.  If $r_t = r_{t - 1, t}$ denotes the one‑period rate observed at time $t-1$, then $$(1+r_{0,T})^T=(1+r_1)(1+r_2)\cdots(1+r_T),$$ so that $r_{0,T}$ is effectively the geometric mean of the successive short rates.  Consequently, a rise in any one‑year spot rate from time $t-1$ to $t$ lifts all future spot rates that include that period, thereby increasing the overall $T$-year spot rate and reducing the price of bonds maturing at or after $t$.

Because future rates are unobservable, i.e. $r_{t_1, t_2}$ for which $t_1 > 0$, spot rates are inferred from current zero‑coupon prices. A _T_-year _spot rate_ $r_{0, T}$ is the implied return on a zero‑coupon bond maturing in a specific year _T_.  For a bond of maturity $T$ with face value $\text{FV}$, the spot rate $r_{0,T}$ satisfies $$P=\frac{\text{FV} }{(1+r_{0,T})^T}.$$

For example, if a five‑year bond with $\text{FV}=1$ trades at \$0.797, the 5‑year spot rate is $$r_{0,5}=\left(\frac{1}{0.797}\right)^{1/5}-1=4.64\%.$$

#### spot rate versus YTM

A bond’s price can be expressed either with its YTM or with the sequence of spot rates that match each coupon payment.  For a two‑year bond with $\text{FV}=100$, coupon $8\%$ and YTM $11.9\%$, $$P_A=\frac{8}{1.119}+\frac{108}{(1.119)^2}\approx\$93.4.$$ Using the spot rates $(r_{0,1},r_{0,2})=(10\%,12\%)$ yields the same price: $$P_A=\frac{8}{1.10}+\frac{108}{(1.12)^2}\approx\$93.4.$$

### forward rate

Forward rates $f_t$ can be extracted from observable zero‑coupon bond prices.  For two successive maturities with the same future value, $$P_{0,t-1}=\frac{\text{FV} }{(1+f_{1})\cdots (1+f_{t-1})},\qquad P_{0,t}=\frac{\text{FV} }{(1+f_{1})\cdots (1+f_{t})},$$ hence $$\frac{P_{0,t-1} }{P_{0,t} }=1+f_{t}.$$ The factor $f_{t}$ is the implied one‑year forward rate from time $t-1$ to $t$, derived entirely from market prices and reflecting expectations of future short‑term rates.

Given zero‑coupon bond prices $P_{0,1}=0.9524,\; P_{0,2}=0.8900,\; P_{0,3}=0.8278,\; P_{0,4}=0.7629$ and corresponding spot rates $r_{0,1}=5\%$, $r_{0,2}=6\%$, $r_{0,3}=6.5\%$, $r_{0,4}=7\%$, the forward rate for borrowing 20 million dollars from year 3 to year 4 is $$f_{4}=\frac{P_{0,3} }{P_{0,4} }-1      =\frac{0.8278}{0.7629}-1 \approx 8.5\%.$$ It could also be calculated from the corresponding spot rates: $$f_4 = \frac {(1 + r_{0, 4})^4} {(1 + r_{0, 3})^3} - 1 = \frac {1.070^4} {1.065^3} - 1 \approx 8.5\% \,.$$ A bank would quote an interest rate of about $8.5\%$ for that one‑year forward loan three years from now.

The _expectation hypothesis_ states that a forward rate equals the market’s forecast of the future spot rate:  $f_{t}=E[r_{t}] = E[r_{t - 1, t}]$.  Thus the shape of the yield curve depends on investors’ expectations.  If the market anticipates _increasing_ short‑term rates, forward rates—and therefore long‑term yields—rise, producing an upward‑sloping curve; _decreasing_ expected short rates produces a downward or inverted curve.  The hypothesis _ignores_ risk premia, focusing only on expectations that shape the term structure.

## risks

The _liquidity hypothesis_ states that a forward rate contains an extra term for the difficulty of trading a bond:  $$f_t = E[r_t] + \text{LP} \,.$$ Because most bonds are traded over‑the‑counter, finding a counterparty costs time and effort. The longer the maturity, the less liquid the market; investors therefore demand a higher return to compensate for liquidity risk, so $f_t > E[r_t]$.

A _default_ occurs when an issuer cannot make its promised coupon or principal payment. Rating agencies such as Moody’s, S&P and Fitch summarize default probability in a letter grade: _Highest_ (e.g., Aaa), _High_ (Aa), _Upper Medium Grade_ (A), _Upper Medium_ (Baa); these four are considered _investment grades_. The remaining grades down to _Default_ (C) are considered _non-investment grades_. The risk of loss is reflected in the spread between a corporate bond yield and that of a comparable risk‑free Treasury.

### yield decomposition

The total yield can be broken into parts. The _default premium_ is the extra yield that compensates investors for the expected loss if a bond defaults, whereas the _risk premium_ is the additional yield required to compensate for the overall uncertainty (volatility) of returns around that expected value.

Let $y_{\text{prom} }$ be the yield a borrower would earn if no default occurred, and $y_{\text{exp} }$ the expected yield after accounting for the probability of default. The difference $y_{\text{prom} }-y_{\text{exp} }$ is the _default premium_; the difference between $y_{\text{exp} }$ and the risk‑free Treasury yield is the _risk premium_.

_Example_: a 10‑year Treasury \$1000 ZCB trades at \$463.19, yielding 8%. A corporate ZCB with the same maturity sells for \$321.97 but is expected to be redeemed only at \$762.22, i.e. 76.222% chance of redemption. Solving $\frac{321.97}{(1+y_{\text{prom} })^{10} }=1000$ gives $y_{\text{prom} }\approx12\%$. Using the expected redemption, $\frac{321.97}{(1+y_{\text{exp} })^{10} }=762.22$ yields $y_{\text{exp} }\approx9\%$. Thus the default premium is 3% and the risk premium relative to Treasury is 1%.

## interest rate risk and duration

The _Macaulay duration_ $D$ can be defined as the weighted average time at which cash flows are received: $$D=\sum_{t=1}^{T} w_t\,t$$ where the weights $w_t=\frac{PV(CF_t)}{P}$ are by present value. The Macaulay duration $D$ measures the proportional change in price for a small _percentage_ change in one plus the yield $1 + y$: $$\frac {\Delta P} P = -D \frac {\Delta(1 + y)} {1 + y} \,.$$ This motivates the _modified duration_, defined as $$D_{\text{mod} }=D/(1+y) \,,$$ which gives the proportional change in price for a small _absolute_ change in yield: $$\Delta P/P=-D_{\text{mod} }\Delta y \,.$$

To derive the two durations, consider that the price of a bond with cash flows $\{CF_t\}$ is $$P=\sum_{t=1}^{T}\frac{CF_t}{(1+y)^t} \,.$$ A small change $dy$ in yield gives $$\frac{dP}{dy} = -\sum_{t=1}^{T}\left(\frac{CF_t}{(1+y)^t }\frac{t}{1+y}\right) =-\frac {PD} {1 + y} \,,$$ where the _Macaulay duration_ $D$ is $$D=\frac{1}{P}\sum_{t=1}^{T}\frac{t\,CF_t}{(1+y)^t} \,.$$ The _modified duration_ $D_{\text{mod} }=D/(1+y)$ gives the proportional change in price for a small _absolute_ change in yield: $\Delta P/P=-D_{\text{mod} }\Delta y$.

_Example_. For a 5‑year \$1000 bond with \$40 coupons, the _Macaulay_ duration is about 4.63 years. If instead the five cash flows were spread evenly over five years, the average time would be $\frac{1+2+\dots+5}{5}=3$ years; hence for a bond, $D \le T$, with equality only for a zero‑coupon bond.

Because $D_{\text{mod} } = D / (1 + y)$ is the price sensitivity to an _absolute_ change in yield, longer‑maturity bonds are more exposed. When the market shifts from 1% to 2%, a one‑year bond with $D_{\text{mod} } = 1 / 1.01$ drops by roughly 1% of its price, whereas a ten‑year bond with $D_{\text{mod} } = 10 / 1.01$ falls by about 10%. The percentage change calculated from $D_{\text{mod} }$ is an _underestimate_ due to convexity; see the section below.

Thus duration captures how much the contract’s value moves when interest rates change and is an essential tool for managing fixed‑income risk.

### convexity correction

The relationship between bond prices and yields is not strictly linear; it is convex (bends upward), so the duration rule—$\Delta P/P=-D^{*}\,\Delta y$—provides a good approximation only for very small yield changes. When $\Delta y$ becomes sizable, the assumption that $dy\approx\Delta y$ breaks down and a correction for convexity is required. That is, for a large increase in yield, the price drops less than the estimate from modified duration; and for a large decrease in yield, the price increases more than the estimate.

Convexity is defined as $$C=\frac{1}{P(1+y)^2}\sum_{t=1}^{T}\frac{CF_t\,t(t+1)}{(1+y)^{\,t} },$$ (if one is good enough with mathematics, it is clear that this is obtained by the second derivative of price) and the corrected price sensitivity becomes $$\frac{\Delta P}{P}=-D^{*}\,\Delta y+\frac{(\Delta y)^2}{2}\,C .$$ The second‑order term, involving convexity $C$, adjusts the linear estimate and captures the curvature of the price–yield curve. (annotation: __this course__: Although it is unnecessary to memorize this formula for this course, understanding that duration alone does not fully describe a bond’s interest‑rate risk is essential when larger yield movements are anticipated.)

### portfolio duration  

When a single fixed‑income security has an individual Macaulay or modified duration $D_i$, the investor cannot alter that value.  A portfolio of $N$ bonds with weights $w_i$ yields a weighted average duration $$D_{\text{p} }=\sum_{i=1}^{N} w_i D_i ,$$ so the overall interest‑rate sensitivity can be tuned by allocating capital across securities.  

For example, suppose an investor holds two bonds: Bond A with $D_A = 5$ years and weight $w_A=0.6$, and Bond B with $D_B = 12$ years and weight $w_B=0.4$.  The portfolio duration is  $$D_{\text{p} }=0.6\times 5+0.4\times 12=8.8 \text{ years}.$$ A higher weighted average length exposes the position to larger rate movements, whereas a lower $D_{\text{p} }$ reduces sensitivity.

### immunization

Financial institutions use duration to control interest‑rate exposure.  In business operations they must match asset and liability durations so that changes in rates do not affect net worth; this practice is known as _asset–liability management_ (ALM).  _Basel regulations_ require banks, insurance firms, pension funds and central banks to maintain a target risk‑equity ratio, which is often achieved by balancing the duration of assets against liabilities.

Commercial banks typically hold long‑dated loans (assets) and short‑dated deposits (liabilities), creating a _positive duration gap_.  If market rates rise, the present value of loan income falls significantly while deposit outflows falls slightly, decreasing the net present value; the reverse holds if market rates fall. Hence, _Basel regulations_ require banks, insurance firms, pension funds and central banks to maintain a target risk‑equity ratio.

The reverse situation applies to pension funds and life insurers face long‑dated policy liabilities, creating a _negative duration gap_.  Their asset portfolios are usually shorter than liabilities, producing a negative duration gap.  Over time the mismatch can shrink as new policies are written and older ones lapse, but it remains a key risk that regulators monitor through solvency margin rules.

#### limitations of immunization

Immunisation relies on the assumption that the yield curve moves parallelly and that interest‑rate changes are small.  In reality, residual maturity drift, shifting credit spreads, transaction costs, and the convexity of bonds can alter duration calculations.  Consequently, continuous rebalancing is required to keep the portfolio immunised; otherwise the protection erodes. There may be costs like attention costs, commissions and fees, and computation errors.

## portfolio strategies

Investors may adopt passive or active approaches.  A _passive_ strategy replicates a broad index, accepting market risk, including interest rate risk, but avoiding trading costs.  An _active_ manager seeks to outperform the benchmark by exploiting mispriced bonds, often using duration targeting and convexity analysis to anticipate yield changes.  Immunization, which establishes a virtually zero-risk bond portfolio, falls in between and is sometimes called a _quasi-passive_ strategy.
