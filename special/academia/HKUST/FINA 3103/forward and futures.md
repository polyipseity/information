---
aliases:
  - FINA 3103 forward and futures
  - FINA3103 forward and futures
  - HKUST FINA 3103 forward and futures
  - HKUST FINA3103 forward and futures
  - forward and futures
tags:
  - flashcard/active/special/academia/HKUST/FINA_3103/forward_and_futures
  - language/in/English
---

# forward and futures

- HKUST FINA 3103

---

- see: [general/forward contract](../../../../general/forward%20contract.md), [general/futures contract](../../../../general/futures%20contract.md)

__Forwards__ and __forwards__ are contracts to exchange an asset at a specified price and time in the future. They are a type of _derivatives_, which are financial contracts whose payoff depends on another security or underlying asset; they are also known as _contingent claims_. Their cash flows differ from those of ordinary stocks and bonds, and their prices arise through payoff replication and non‑arbitrage arguments.

They may be extended by _options_, which are instruments granting the holder the right, but not the obligation, to buy (call) or sell (put) an asset at a predetermined strike price.

## derivatives

A derivative’s value is derived from the behavior of its underlying. In practice, derivatives come in many forms—interest‑rate swaps, equity options, commodity forwards, among others. The market for interest‑rate derivatives (IRD) dominates the over‑the‑counter (OTC) space, with notional amounts measured in hundreds of trillions of dollars. This size reflects the broad use of IRD for hedging and speculation.

## motivation

Forward contracts are private agreements to exchange an asset at a future date for a fixed price, while futures are standardized versions traded on exchanges with daily settlement. A common motivation is to _reserve_ an asset: buying gold today at \$100 versus purchasing a forward contract that delivers the same amount in the future. At maturity both strategies deliver the same quantity of gold, but the forward requires no out‑of‑pocket cash until delivery, allowing traders to speculate on price movements without holding the underlying.

## history

The first organized futures market dates back to 1730 with Japan’s Dojima Rice Exchange in Osaka, and it is still operating today. Traders traded contracts for future rice crops, setting benchmark prices and establishing a membership and clearing system that resembles modern exchanges. These early practices laid the groundwork for today’s global derivatives markets.

## forward

A forward contract is a private agreement to buy or sell an asset at a fixed price on a specified future date. The _forward price_ is the value agreed today, and the contract is customized and traded over‑the‑counter (OTC). No cash flows occur until maturity.

The buyer of the contract, which receives the underlying, is the long position, and the seller, which delivers the underlying, is the short position. The long and short position respectively benefits and loses if the market price rises, and vice versa if the market price falls.

For example, a tofu producer who needs 0.5 tons of soybeans in three months can lock in a price by buying a forward at \$750 per ton when the spot price is \$700. The long position obligates the producer to receive 0.5 tons from the counterparty (the short position) on maturity; the short side delivers them at \$750 on maturity.

## futures

A futures contract is a standardized version of a forward that trades on an exchange such as CME, NYMEX, or OSE. It is generally only available for major underlying assets with standardized maturity and units. Similar to forwards, the buyer is the long position and the seller is the short position. Unlikely forwards, taking a position requires a _margin account_ with _initial_ and _maintenance_ margin.

Futures differ from forwards mainly in standardization: contract size, maturity, and settlement rules are fixed, allowing trading on exchanges, e.g. CME, CBOE, NYBOT (ICE), HKFE, etc. with a clearing house that guarantees settlement. This reduces _counterparty risk_ compared with an OTC forward, where the risk is borne by the two parties directly. Futures also require daily margin posting, whereas forwards have no such requirement.

### mark-to-market mechanism

Futures are _marked to market_ daily: each day the profit or loss from the change in the underlying’s price is posted to the trader’s margin account, and the account must stay above a _maintenance_ level; if not, a _margin call_ occurs, and additional deposits are needed so that the balance equals the _initial_ margin again. Otherwise, the positions are sold. In many exchanges, right before posting the profit or loss, the margin account's balance earns interest using the risk-free rate. (annotation: __this course__: Neglect earning interest on the margin account's balance.)

Consider a gold future with 100‑ounce size at \$1&nbsp;600/ounce and an initial margin of \$11&nbsp;000. If the price falls to \$1&nbsp;590/ounce on day 1, the daily loss for the _long_ position is $$10 \times 100 = \$1\,000,$$ reducing the account balance to \$10 000; no margin call occurs because it remains above the maintenance level of \$8&nbsp;000. Subsequent declines causing the balance to be _below_ the maintenance level require additional deposits so that the balance equals the initial margin again.

## counterparty risk and clearing houses

In an OTC forward, the buyer’s profit or loss depends on the counterpart’s ability to deliver; if the counterparty defaults, the trade may not settle even though the trader has earned a profit. A clearing house—an independent entity linked to a futures exchange—interposes between buyers and sellers in futures markets. It holds collateral (margin) and settles each contract, thereby eliminating counterparty risk for participants. For example, Chicago's Options Clearing Corporation (OCC) specializes in equity derivatives clearing for 15 US exchanges.

## pricing

The value of a forward or futures contract is obtained by replicating its payoff with a portfolio that does not involve the contract itself.

We assume the price of a forward $F_{t, T}$ approximately equals to a future $H_{t, T}$ with the same underlying and maturity. In practice, they are different due to mark-to-market and other market features, as pointed out in John Hull's "_Options, Futures, and Other Derivatives_".

### payoffs

The payoff of a long position is $S_T-F$, where $S_t$ is the spot price at time $t$ and $F$ is the agreed‑for‑future price. A short position receives negative of that, $-\, (S_T-F)$. Because these payoffs are linear in the underlying, the contract can be priced by setting up a self‑financing strategy (e.g., borrowing to buy the asset) that delivers the same payoff.

_Example_: For an oil forward with forward price $F=101$, the long position yields negative payoff when the spot is below 101 and positive when above 101, and forms a linear relationship. The short position is symmetric: it pays negative payoff if the spot is above 101 and positive if below 101, and is also linear.

### replicating portfolio

At time $t=0$ two equivalent strategies can be built: enter a forward or futures contract with maturity $T$; or buy the underlying asset today, borrow $S_0$, hold until $T$, then repay the loan at $(1+r)^T$.

Let $V_{t,T}(c, y)$ denote the value at maturity $T$ of any holding cost $c$ and convenience yield $y$ from $t$ to $T$.  A positive value means the future value at $T$ of the holding cost exceeds the convenience yield. The _future_ net cost of strategy 2 (borrow to buy the underlying) at time $T$ is $$S_0(1+r)^T+V_{0,T}(c, y).$$ Because the two strategies must be priced equally, the forward price, which is the _future_ net cost of strategy 1, satisfies $$H_{0,T}\approx F_{0,T}=S_0(1+r)^T+V_{0,T}(c, y),$$ and at a later time $t$, $$H_{t,T}\approx F_{t,T}=S_t(1+r)^{\,T-t}+V_{t,T}(c,y)\,,$$ which implies that when the maturity approaches, the forward price converges to the spot price: $F_{T,T} = S_T$.

### holding cost and convenience yield

When an investor keeps a physical commodity, two opposing effects influence the forward price. The _holding (carry) cost_ $c$ represents expenses such as storage fees, insurance, and finance charges that accrue over time. The _convenience yield_ $y$ captures benefits from actually possessing the asset—e.g., the ability to meet sudden demand or to use the commodity in production.

These factors enter the pricing relation through the term $V_{t,T}(c,y)$. A high carrying cost raises the forward price, while a large convenience yield lowers it. In commodities where storage is expensive and market tightness is low (i.e. supply exceeds demand, so hard to sell the underlying), a positive net carry ($r+c>y$) produces _contango_; when the reverse holds, the market exhibits _backwardation_.

### pricing examples

Gold can be stored cheaply and yields negligible benefits. The non‑arbitrage condition gives $$F_{t,T} = S_t(1+r)^{\,T-t},$$ so for a positive risk‑free rate $r>0$, gold futures trade at a premium: $F>T>S_T$.

Oil incurs storage cost $c$ per period; and, as a critical input to many industries, provides convenience yield $y$ per period.  The pricing relation becomes  $$F_{t,T} = S_t(1+r+c-y)^{\,T-t}.$$ If the net carry $r+c>y$, contango occurs; otherwise, backwardation arises.

For a stock index that pays dividends at rate $d$, treated as convenience yield, and has no storage cost,  $$F_{t,T}= S_t(1+r-d)^{\,T-t}.$$ Because $d>r$ in many cases, the forward price may lie below the expected spot, producing backwardation.

### implied rates

The price of a forward or futures contract can be inverted to recover the underlying economic variables that determine its value.  

First, the annualized _implied interest rate_ $r$ follows from the cost‑of‑carry equation $F_{t,T}=S_t(1+r)^{\,T-t}$. For instance, if a 2‑month gold forward trades at \$269 while the spot is \$267, then $$r=\left(\frac{F}{S}\right)^{12/2}-1=4.58\%.$$

Second, the annualized _implied net convenience yield_ $y$ measures the benefit of physically holding a commodity relative to cash. When futures prices fall below what a pure carry model would predict, the difference is interpreted as a positive $y$. In a 6‑month gasoline market with a forward price of \$0.733 and a spot of \$0.776 under a 3.40% risk‑free rate, the implied yield is $$y=1+r-\left(\frac{F}{S}\right)^{12/6}=14.18\%.$$

Third, the annualized _implied dividend yield_ $d$ applies to assets that distribute income. Using the relation $F_{t,T}=S_t(1+r-d)^{\,T-t}$, a 4‑month S&P 500 future at \$1\,233.50 against a spot of \$1\,220.75 and an interest rate of 3.50% yields $$d=1+r-\left(\frac{F}{S}\right)^{12/4}=0.33\%.$$

## contango and backwardation

If the future price exceeds the _expected_ spot (not _current_ spot), the market is in _contango_; if it falls below, it is in _backwardation_.  The difference reflects storage costs and convenience yields. As mentioned above, assuming the same maturity _date_ (a point in time!), as the maturity date comes to a close, the future price approaches the spot price.

Note if the _current_ spot price is used, the future price exceeding the current spot price would be called _negative basis_; and falling below would be called _positive basis_.

## basis trading  

_Basis trading_ exploits the difference between the price of a forward or futures contract and the spot price of its underlying asset. The _net basis_ is defined as  $$B_t = S_t(1+r)^{\,T-t}-F_{t,T},$$ where $S_t$ is the current spot price, $r$ the risk‑free rate, and $F_{t,T}$ the forward (or futures) price at time $t$ maturing at time $T$. When $B_t \neq 0$, a trader can construct an arbitrage: buy the cheaper side and sell the more expensive one, locking in a risk‑free profit at maturity. For example, Salomon Brothers in the 1970s did so in the bond future market.

In bond‑future markets the appropriate discount factor is often based on the _repo_ rate, because the future is used as collateral for borrowing. The calculation then involves a conversion factor that adjusts for differences between the underlying bond’s coupon schedule and the futures contract’s delivery date, and it must also accommodate uncertainty in interest rates and varying maturities.

## hedging

A forward contract can provide a hedge only if the traded asset matches the risk profile of the exposure. Since forwards are over‑the‑counter contracts, they may lack liquidity; their size, maturity, and quantity are fixed by the parties. Futures, being standardized and exchange‑traded, offer greater liquidity but still cannot match every possible hedging need perfectly.

Perfect hedges across all dimensions—price, timing, quantity, and asset class—are rarely achievable in practice. Traders therefore use a combination of forwards, futures, and other instruments to approximate the desired hedge while accepting some residual risk.  
