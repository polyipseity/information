---
aliases:
  - GM model
  - Glosten-Milgrom model
  - Glosten–Milgrom model
  - adverse selection spread model
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/Glosten–Milgrom_model
  - language/in/English
---

# Glosten–Milgrom model

The [Roll model](Roll%20model.md) takes the spread and the order flow as given and derives what they do to the price. This [market microstructure](market%20microstructure.md) model asks where the spread itself comes from, and answers with asymmetric information: the trader who arrives may know the asset's value, so the quote has to cover the expected loss to that trader. Lawrence Glosten and Paul Milgrom (1985, Journal of Financial Economics (JFE)) proposed it. The informational explanation of a [bid-ask spread](bid-ask%20spread.md) is one of three candidates for why the spread exists at all.

Order flow stays exogenous here. What drives it is a separate question. Inside the information story, Albert S. Kyle (1985, Econometrica (ECTA)) models the strategic behaviour of an insider and how information affects liquidity; outside it, order flow comes from endowment shocks, from risk diversification for risk sharing, and from noise-trader risk. Nothing here turns on any of those: the model uses only that some traders know $v$ and some do not.

The one-period version is enough to pin down the ask, the bid and the spread between them. Making those prices move from trade to trade takes the multi-period version, where the model speaks to [price discovery](price%20discovery.md).

---

Flashcards for this section are as follows:

- what the Glosten–Milgrom model derives, and from what ::@:: The bid-ask spread, derived from asymmetric information between the traders and the market makers instead of taken as given.
- the explanation of a positive bid-ask spread that the Glosten–Milgrom model works out ::@:: Information friction: the market maker's quote has to cover the expected loss to a counterparty who may know the asset's value, one of three candidate explanations of why a spread exists.
- what the information strand attributes order flow to, with the order flow left exogenous in the Glosten–Milgrom model ::@:: The strategic behaviour of an insider, whose trades are worked into the price, and how that information affects liquidity.
- which one-period model with competitive market makers derives a positive spread from adverse selection alone, every maker earning zero expected profit at $A^{*}=\mu$ and $B^{*}=-\mu$? ::@:: Lawrence R. Glosten and Paul Milgrom, 1985, Journal of Financial Economics (JFE), the paper behind the Glosten–Milgrom model.
- which model works a strategic insider's order flow into the price through a competitive market maker, and is the reference for the information strand of order flow? ::@:: Albert S. Kyle, 1985, Econometrica (ECTA).
- the three non-information motives for order flow that sit beside the information story ::@:: Endowment shocks, risk diversification for risk sharing, and noise-trader risk.
- what the one-period Glosten–Milgrom model leaves to a multi-period version ::@:: The bid, the ask and the execution prices as they evolve from trade to trade; the one-period version yields only a static spread.

## trading game

The game trades one risky asset once. Its fundamental value is $v=+1$ with probability $\frac{1}{2}$ and $v=-1$ with probability $\frac{1}{2}$, so the prior expectation is $\operatorname{E}[v]=0$. The two values need not be symmetric: $v=v_H$ with probability $\rho$ and $v=v_L$ with probability $1-\rho$ runs the same argument.

A trade runs in three steps. Market makers place limit orders for one share, quoting a bid $B$ and an ask $A$ from their current belief about $v$. One trader then arrives and sends a market order to buy or to sell one unit, informed with probability $\mu$. Observing the trade, the market makers update their belief about $v$.

Two frictions meet in the book. One is the information friction; the other is ex-ante commitment, because the quote stands before the market maker learns who takes it. A trade carries a type, informed or uninformed, and a direction, buy or sell, and the market maker prices both before seeing either. Every informed trader here knows $v$ at no cost, so nobody has paid for the information the quote is charged against. Whether costly information can survive in the price at all is the [Grossman–Stiglitz paradox](Grossman%E2%80%93Stiglitz%20paradox.md).

---

Flashcards for this section are as follows:

- the prior on the asset value in the one-period Glosten–Milgrom game, before $v$ is known ::@:: $v=+1$ with probability $\frac{1}{2}$ and $v=-1$ with probability $\frac{1}{2}$, so $\operatorname{E}[v]=0$.
- how the two-point prior generalises away from $\pm1$ ::@:: $v=v_H$ with probability $\rho$ and $v=v_L$ with probability $1-\rho$; nothing in the argument needs the two values to be symmetric.
- the three steps of a trade in the Glosten–Milgrom game, from the quotes $B$ and $A$ to the arriving market order ::@:: Market makers quote a bid $B$ and an ask $A$ for one share from their belief about $v$; one trader arrives and sends a market order for one unit, informed with probability $\mu$; the market makers update on the trade.
- the two frictions a trade in the limit-order book carries ::@:: The information friction and ex-ante commitment: the quote is placed before the market maker learns whether an informed or an uninformed trader takes it.
- how a trade is described in the Glosten–Milgrom game, given the true value $v=\pm1$ ::@:: By the trader's type, informed or uninformed, and by the order direction, buy or sell.

### players

The [market makers](market%20maker.md) of the book are competitively many, and each places one share on each side: a bid $B$ and an ask $A$ quoted from their belief about $v$. They hold no information about $v$ and know only the structure of the game, including the mass $\mu$ of informed traders, so they cannot tell an informed trader from a noise trader.

Informed traders are a mass $\mu$ of the [market's participants](financial%20market%20participants.md), so picking one trader from the crowd gives an informed one with probability $\mu$. Each knows whether $v=+1$ or $v=-1$ and trades one unit through a [market order](market%20order.md) to make a profit, which means buying only when $v=+1$ and $A<+1$, and selling only when $v=-1$ and $B>-1$. A quote on the wrong side of the value is a loss, so the informed trader stays out. Insiders, sophisticated investors and high-frequency traders are the real-world versions of such a trader.

Uninformed, or noise, traders are the remaining mass $1-\mu$, small retail investors in need of a trade. They do not know $v$ and their trades are unrelated to it: each buys or sells one unit with probability $\frac{1}{2}$ at the best available prices, for non-fundamental reasons such as hedging or an immediate need for cash.

---

Flashcards for this section are as follows:

- what the market makers in the Glosten–Milgrom game know about $v$ when they quote ::@:: Nothing; they know the structure of the game, including the mass $\mu$ of informed traders, and cannot tell an informed trader from a noise trader.
- the asks at which an informed trader buys, given $v=+1$ ::@:: Any $A<+1$; at $A\ge+1$ buying is unprofitable, so the informed trader does not buy.
- the bids at which an informed trader sells, given $v=-1$ ::@:: Any $B>-1$; at $B\le-1$ selling is unprofitable, so the informed trader does not sell.
- what the informed mass $\mu$ of the Glosten–Milgrom game means for a randomly picked trader ::@:: The trader is informed with probability $\mu$.
- how the uninformed (noise) traders of the Glosten–Milgrom game trade, with mass $1-\mu$ ::@:: They do not know $v$; each buys or sells one unit with probability $\frac{1}{2}$ at the best available prices, for reasons unrelated to $v$ such as hedging or an immediate need for cash.
- who the informed traders are in practice ::@:: Insiders, sophisticated investors and high-frequency traders.

## learning from order flow

A buy can come from two places: an informed trader who knows $v=+1$, or a noise trader who happened to draw buy. Telling the two apart is what the market maker has to do, and the weights come from how precisely the order flow signals the value. The value is discrete here, so those weights are probabilities; where the value is normal the same update becomes the [precision-weighted average](Bayes'%20theorem.md#posterior%20mean%20as%20a%20precision-weighted%20average), and prior and signal split the belief by precision instead.

---

Flashcards for this section are as follows:

- what an arriving buy order can be in the Glosten–Milgrom game, with $v=\pm1$ and informed mass $\mu$ ::@:: An informed trader who knows $v=+1$, or a noise trader who drew buy; the market maker has to weigh the two.
- how a market maker in the Glosten–Milgrom game handles an order it cannot identify, with quotes $A$ and $B$ and informed mass $\mu$ ::@:: It cannot tell an informed buy from a noise buy, so it assigns the two probabilities implied by $\mu$ and updates its belief about $v$.

### precision of a buy order

The signal is the direction of the arriving order. When $v=+1$, an informed trader buys for sure and a noise trader buys with probability $\frac{1}{2}$; the informed share of the population is $\mu$, so $\operatorname{Pr}(\text{Buy}\mid v=+1)=\mu\cdot 1+(1-\mu)\cdot\frac{1}{2}=\frac{1+\mu}{2}$. The signal is wrong with the complementary probability, $\operatorname{Pr}(\text{Buy}\mid v=-1)=\frac{1-\mu}{2}$, and the sell side mirrors it: $\operatorname{Pr}(\text{Sell}\mid v=-1)=\frac{1+\mu}{2}$ and $\operatorname{Pr}(\text{Sell}\mid v=+1)=\frac{1-\mu}{2}$.

Written as $\frac{1}{2}+\frac{\mu}{2}$, the buy probability sits between the coin flip of a market that knows nothing and the certainty of a market where everyone does. A noise trader buys half the time whatever $v$ is. An informed trader buys where a noise trader would only have tossed a coin, so each unit of informed mass adds half a buy rather than a whole one. At $\mu=0$ a buy is a coin flip at either value and tells the market maker nothing. At $\mu=1$ it happens only when the asset is up and proves it.

How much a filled order tells the maker depends on the share of the crowd that knows the value: in a market of noise traders a filled buy is almost worthless as evidence, and in a market of insiders it settles the question.

---

Flashcards for this section are as follows:

- what the order-flow signal is in the Glosten–Milgrom game, as a function of $v$ ::@:: The direction of the arriving market order, a buy or a sell, whose probability depends on $v$ and on the informed mass $\mu$.
- the probability of a buy when $v=+1$, with informed mass $\mu$ and the noise trader buying with probability $\frac{1}{2}$ ::@:: $\operatorname{Pr}(\text{Buy}\mid v=+1)=\mu\cdot 1+(1-\mu)\cdot\frac{1}{2}=\frac{1+\mu}{2}$: the informed trader buys for sure and the noise trader buys half the time.
- the probability of a buy when $v=-1$, with informed mass $\mu$ ::@:: $\operatorname{Pr}(\text{Buy}\mid v=-1)=\frac{1-\mu}{2}$: only a noise trader buys, with probability $\frac{1}{2}$, and the mass of noise traders is $1-\mu$.
- the precision of the order-flow signal on the sell side, with informed mass $\mu$ ::@:: $\operatorname{Pr}(\text{Sell}\mid v=-1)=\frac{1+\mu}{2}$ and $\operatorname{Pr}(\text{Sell}\mid v=+1)=\frac{1-\mu}{2}$, the mirror image of the buy side.
- what the buy probability $\operatorname{Pr}(\text{Buy}\mid v=+1)=\frac{1+\mu}{2}$ says when written as $\frac{1}{2}+\frac{\mu}{2}$, in the Glosten–Milgrom game with informed mass $\mu$ ::@:: Each unit of informed mass adds half a buy, because an informed trader buys where a noise trader only tosses a coin: at $\mu=0$ a buy is a coin flip at either value, and at $\mu=1$ it happens only when the asset is up.
- how much a buy tells the market maker about the value, without symbols, in the Glosten–Milgrom game with informed mass $\mu$ ::@:: As much as the share of the crowd that knows the value, so a maker facing mostly noise traders learns almost nothing from a filled order and one facing mostly insiders learns nearly all of it.

### posterior after a buy

[Bayes' theorem](Bayes'%20theorem.md) splits an observed buy into the two ways it can happen, weighting the correct buy against the false one: $$\operatorname{Pr}(+1\mid\text{Buy})=\frac{\operatorname{Pr}(+1)\operatorname{Pr}(\text{Buy}\mid+1)}{\operatorname{Pr}(+1)\operatorname{Pr}(\text{Buy}\mid+1)+\operatorname{Pr}(-1)\operatorname{Pr}(\text{Buy}\mid-1)}=\frac{\frac{1}{2}\cdot\frac{1+\mu}{2}}{\frac{1}{2}\cdot\frac{1+\mu}{2}+\frac{1}{2}\cdot\frac{1-\mu}{2}}=\frac{1+\mu}{2},$$ and the same denominator applied to $\operatorname{Pr}(-1)$ leaves $\frac{1-\mu}{2}$.

The conditional expectation weights the two values by that posterior: $\operatorname{E}[v\mid\text{Buy}]=\frac{1+\mu}{2}(+1)+\frac{1-\mu}{2}(-1)=\mu$. A buy of one unit moves the market maker's valuation from the prior $0$ to $\mu$, the informed share itself. Only one of the two possible buyers says anything about $v$: a noise trader buys whatever the value is, and the informed trader's buy is certain at $v=+1$, so the signal carries exactly the mass of traders who know. The posterior $\frac{1\pm\mu}{2}$ is the even prior moved by $\frac{\mu}{2}$ toward the side of the order, and because the two states carry opposite signs, those two half-shifts add, so the expectation moves by the full $\mu$. More informed traders lift the valuation toward $+1$; a population that is mostly noise barely moves it at all.

---

Flashcards for this section are as follows:

- the posterior on $v=+1$ after a buy, given the prior $\operatorname{Pr}(v=\pm1)=\frac{1}{2}$ and the precisions $\operatorname{Pr}(\text{Buy}\mid v=\pm1)=\frac{1\pm\mu}{2}$ ::@:: $\operatorname{Pr}(+1\mid\text{Buy})=\frac{\frac{1}{2}\cdot\frac{1+\mu}{2}}{\frac{1}{2}\cdot\frac{1+\mu}{2}+\frac{1}{2}\cdot\frac{1-\mu}{2}}=\frac{1+\mu}{2}$.
- the posterior on $v=-1$ after a buy, given the prior $\operatorname{Pr}(v=\pm1)=\frac{1}{2}$ and the precisions $\operatorname{Pr}(\text{Buy}\mid v=\pm1)=\frac{1\pm\mu}{2}$ ::@:: $\operatorname{Pr}(-1\mid\text{Buy})=\frac{1-\mu}{2}$.
- the conditional expectation $\operatorname{E}[v\mid\text{Buy}]$ in the Glosten–Milgrom game, with $v=\pm1$ and informed mass $\mu$ ::@:: $\operatorname{E}[v\mid\text{Buy}]=\frac{1+\mu}{2}(+1)+\frac{1-\mu}{2}(-1)=\mu$.
- how $\operatorname{E}[v\mid\text{Buy}]$ responds to a larger informed mass $\mu$, and to a population that is mostly noise ::@:: It rises with $\mu$, since a buy is better news when more traders know $v$, and it falls toward $0$ as the noise share $1-\mu$ grows.
- why a buy displaces the market maker's valuation by exactly the informed mass $\mu$ in the Glosten–Milgrom game, with $v=\pm1$ at probability $\frac{1}{2}$ each and informed mass $\mu$ ::@:: A noise trader buys whatever $v$ is, so it carries no information, while the informed trader's buy is certain at $v=+1$. The signal carries exactly the mass of traders who know. The posterior $\frac{1\pm\mu}{2}$ is the even prior moved by $\frac{\mu}{2}$ each way, and the opposite signs of the two states add those half-shifts into the full $\mu$.

## competitive quote

A market maker whose ask $A$ is taken by one arriving trader earns $A-v$: the price received less the value given up. Its expected profit from the ask side is $\pi_{ask}(A)=\operatorname{E}[A-v\mid\text{Buy}]=A-\operatorname{E}[v\mid\text{Buy}]=A-\mu$, and the conditional expectation does the work, since the market maker learns $v$ only from the side of the order it fills. The price is received for certain and the value given up is not, so the whole risk of the quote sits in that second term. A filled ask settles at $\operatorname{E}[v\mid\text{Buy}]$, so breaking even means charging exactly the expected value of the asset conditional on being hit.

---

Flashcards for this section are as follows:

- the expected profit from an ask quote $A$ taken by one arriving trader, given $v$ and the market maker's belief ::@:: $\pi_{ask}(A)=\operatorname{E}[A-v\mid\text{Buy}]=A-\operatorname{E}[v\mid\text{Buy}]$: the price received less the value given up.
- the expected ask-side profit in the Glosten–Milgrom game, with ask $A$ and informed mass $\mu$ ::@:: $\pi_{ask}(A)=A-\operatorname{E}[v\mid\text{Buy}]=A-\mu$.
- how the ask-side profit $\pi_{ask}(A)=A-\mu$ behaves as a function of $A$ ::@:: It is negative below $A=\mu$, zero at $A=\mu$, and positive above it; past $A=+1$ it jumps to $\pi_{ask}=A$, higher by $\mu$, and that region is not an equilibrium because competition removes it.
- where the risk of an ask quote $A$ taken by an arriving trader sits, between the price received and the value given up ::@:: In the value given up: $A$ is received for certain, so $\pi_{ask}(A)=\operatorname{E}[A-v\mid\text{Buy}]=A-\operatorname{E}[v\mid\text{Buy}]$ prices the fill at the expected value of the asset conditional on being hit.

### ask side

At $A<\mu$ the quote loses money in expectation, so no market maker quotes there: $A\ge\mu$ is the floor.

Above $+1$ the calculation changes. Informed traders never buy at $A\ge+1$, since the asset is worth at most $+1$, so every trade that fills the quote is noise, and $\pi_{ask}(A)=A-\operatorname{E}[v\mid\text{Buy},T=U]=A-0>0$. That profit is available to whoever gets filled, and a noise trader takes one unit at the best quote on the book: against your $A=1.10$ a rival posts $1.09$ and takes the trade, you answer at $1.08$, and the sequence repeats.

Undercutting does not stop at $+1$. Against a rival quoting $A=1$ you can post $0.99$, where informed traders do buy and the profit is $\pi_{ask}=0.99-\mu$; the rival replies at $0.98$, and the same reply is available at every $A>\mu$. Competition stops where no undercut pays, at $A=\mu$.

As a function of $A$, the profit $\pi_{ask}=A-\mu$ is a line rising through zero at $A=\mu$: negative to its left, positive to its right. Past $+1$ the line is a different one, $\pi_{ask}=A$, sitting $\mu$ higher, and the region above $+1$ is not an equilibrium because competition removes it.

The particular numbers do not matter. With many market makers, a quote $\tilde A$ earning $\pi_{ask}(\tilde A)>0$ invites a rival to undercut it and take the profit, so every market maker breaks even in equilibrium, as in Bertrand competition. The ask $A^{*}$ solves $\pi_{ask}(A)=A-\mu=0$, giving $A^{*}=\mu$.

The ask is the expected value of the asset given that the ask was hit, $A^{*}=\operatorname{E}[v\mid\text{Buy}]=\mu$, not a markup on a cost. Zero expected profit says the two kinds of fill cancel: the gain on noise buyers exactly covers the loss on informed ones. That loss is the informed trader's edge, $1-\mu$ on a unit bought at $\mu$.

---

Flashcards for this section are as follows:

- why a market maker in the one-period Glosten–Milgrom game never quotes $A<\mu$ ::@:: The expected profit $A-\mu$ is negative there, so no quote below $\mu$ survives.
- why $A>1$ is not an equilibrium in the one-period Glosten–Milgrom game, although $\pi_{ask}(A)=A>0$ there ::@:: Informed traders never buy at $A\ge+1$, so every fill is a noise trade at the best quote, and a rival undercuts to take it.
- how undercutting proceeds in the one-period Glosten–Milgrom game, with informed mass $\mu$, once a rival quotes $A=1$ ::@:: A quote of $0.99$ earns $\pi_{ask}=0.99-\mu$, a rival replies at $0.98$, and the replies continue at every $A>\mu$, stopping at $A=\mu$.
- the equilibrium ask price $A^{*}$ in the one-period Glosten–Milgrom game, with informed mass $\mu$ and $\pi_{ask}(A)=A-\mu$ ::@:: $A^{*}=\mu$, the solution of $\pi_{ask}(A)=A-\mu=0$: every market maker breaks even, as in Bertrand competition.
- what the equilibrium ask $A^{*}=\mu$ is, read as an expected value rather than as a markup, in the one-period Glosten–Milgrom game with informed mass $\mu$ ::@:: The expected value of the asset given that the ask was hit, $A^{*}=\operatorname{E}[v\mid\text{Buy}]=\mu$, at which the gain on noise buyers exactly covers the loss on informed ones.

### bid side

The bid side runs the same logic with the signs reversed. A sell that fills the bid $B$ leaves the market maker with $\operatorname{E}[v\mid\text{Sell}]-B$, and $\operatorname{E}[v\mid\text{Sell}]=\mu\cdot(-1)+(1-\mu)\cdot 0=-\mu$, since an informed seller of a $v=-1$ asset takes the bid and a noise seller conveys nothing. So $\pi_{bid}=-\mu-B$, and the break-even bid satisfies $0=-\mu-B$, giving $B=-\mu$. The bid reads the same way as the ask: it is the expected value of the asset given that the bid was hit, $B^{*}=\operatorname{E}[v\mid\text{Sell}]=-\mu$, so the seller is paid what a seller's information says the asset is worth. The symmetry is exact: every quantity on this side is the ask side with the sign flipped, which is why the spread comes out as twice one side's charge.

---

Flashcards for this section are as follows:

- the expected profit from a bid quote $B$ in the one-period Glosten–Milgrom game, with informed mass $\mu$ and $v=\pm1$ ::@:: $\pi_{bid}=\operatorname{E}[v\mid\text{Sell}]-B=\mu\cdot(-1)+(1-\mu)\cdot 0-B=-\mu-B$.
- the conditional expectation $\operatorname{E}[v\mid\text{Sell}]$ in the Glosten–Milgrom game, with informed mass $\mu$ and $v=\pm1$ ::@:: $\operatorname{E}[v\mid\text{Sell}]=\mu\cdot(-1)+(1-\mu)\cdot0=-\mu$: the informed seller knows $v=-1$, the noise seller conveys nothing.
- the equilibrium bid $B^{*}$ in the one-period Glosten–Milgrom game, with informed mass $\mu$ and $\pi_{bid}=-\mu-B$ ::@:: $B^{*}=-\mu$, from $0=\pi_{bid}=-\mu-B$.
- why the equilibrium bid equals $\operatorname{E}[v\mid\text{Sell}]$ in the one-period Glosten–Milgrom game, with informed mass $\mu$ ::@:: The market maker receives $B$ and gives up a unit worth $\operatorname{E}[v\mid\text{Sell}]=-\mu$, so breaking even means $B^{*}=\operatorname{E}[v\mid\text{Sell}]=-\mu$: the seller is paid what a seller's information says the asset is worth.

## adverse selection

The quote earns differently against the two kinds of counterparty. An informed buyer takes the ask only when $v=+1$ and $A<+1$, so the market maker's expectation against that trader is $\operatorname{E}[A-v\mid I,\text{Buy}]=A-1<0$: this loss is the adverse selection cost of standing in the market. A noise trader conveys nothing, because $\operatorname{E}[v\mid U,\text{Buy}]=\operatorname{E}[v]=0$, so the same quote earns $\operatorname{E}[A-v\mid U,\text{Buy}]=A-0>0$.

Split by counterparty, $\pi_{ask}=A-\mu$ reads $A-1$ against an informed buyer and $A$ against a noise buyer, and the equilibrium quote is the point where the two balance. Above $A=\mu$ the gain from noise strictly exceeds the loss to informed traders, which is why the undercutting stops only at $\mu$. So the equilibrium ask $A^{*}=\mu$ rises with $\mu$, which is both the frequency of informed trading and the degree of adverse selection.

The bookkeeping runs the same way on both sides. At $A^{*}=\mu$ and $B^{*}=-\mu$ the market maker's profit per trade falls into four cells: $A^{*}-1=-(1-\mu)$ against an informed buyer, $v-B^{*}=-1+\mu=-(1-\mu)$ against an informed seller, $A^{*}-0=\mu$ against a noise buyer, and $0-B^{*}=\mu$ against a noise seller. The maker loses $1-\mu$ on either informed trade and gains $\mu$ on either noise trade. On the ask, informed mass $\mu$ times $-(1-\mu)$ cancels noise mass $1-\mu$ times $\mu$, and the bid mirrors it, so expected profit is zero on both sides while the risk of the quote stays with the maker.

The informed trader keeps the difference. At $v=+1$ it buys at $A^{*}=\mu$ and holds something worth $1$, keeping $1-\mu$ per unit; at $v=-1$ it sells at $B^{*}=-\mu$ and keeps $-\mu-(-1)=1-\mu$. Informed mass $\mu$ at $1-\mu$ apiece gives the informed side $\mu(1-\mu)$ per round.

The noise trader pays the mirror amount. A noise buyer pays $A^{*}=\mu$ for an asset worth $0$ in expectation and loses $\mu$; a noise seller gives up that asset for $B^{*}=-\mu$ and loses $\mu$ as well. Noise mass $1-\mu$ at $\mu$ apiece gives the noise side $\mu(1-\mu)$ per round.

The two totals agree, $\mu(1-\mu)=\mu(1-\mu)$, so the noise traders' losses fund the informed traders' gains exactly. The market maker is the conduit between them: it charges each side the value of the asset conditional on the order it receives, pays out on the other side, breaks even in expectation, and bears the variance of quoting those prices. The cost of adverse selection is that transfer, and the noise traders pay it.

---

Flashcards for this section are as follows:

- the market maker's expected profit against an informed buyer at ask $A$, when $v=+1$ ::@:: $\operatorname{E}[A-v\mid I,\text{Buy}]=A-1<0$: the adverse selection cost of the quote.
- the market maker's expected profit against a noise buyer at ask $A$ ::@:: $\operatorname{E}[A-v\mid U,\text{Buy}]=A-0>0$, because $\operatorname{E}[v\mid U,\text{Buy}]=\operatorname{E}[v]=0$: noise conveys nothing about $v$.
- how the expected ask-side profit $\pi_{ask}=A-\mu$ splits by counterparty, and where the equilibrium quote sits ::@:: $A-1$ against an informed buyer, which is negative, and $A$ against a noise buyer, which is positive; the equilibrium quote $A=\mu$ is where the two balance.
- why the equilibrium ask $A^{*}=\mu$ rises with the informed mass $\mu$ ::@:: $\mu$ is the frequency of informed trading and with it the degree of adverse selection, so the quote must cover a larger expected loss.
- why undercutting continues while $A>\mu$ in the one-period Glosten–Milgrom game ::@:: The gain from noise, $A$, strictly exceeds the loss to informed traders, $A-1$, so a rival quote below $A$ still earns a profit.
- the market maker's profit per trade at $A^{*}=\mu$ and $B^{*}=-\mu$ in the one-period Glosten–Milgrom game, with informed mass $\mu$ and $v=\pm1$, against an informed buyer, an informed seller, a noise buyer and a noise seller ::@:: $A^{*}-1=-(1-\mu)$, $v-B^{*}=-1+\mu=-(1-\mu)$, $A^{*}-0=\mu$ and $0-B^{*}=\mu$: a loss of $1-\mu$ on either informed trade and a gain of $\mu$ on either noise trade.
- why the market maker's expected profit is zero on each side of the book at $A^{*}=\mu$ and $B^{*}=-\mu$ in the one-period Glosten–Milgrom game, with informed mass $\mu$ ::@:: On the ask, informed mass $\mu$ times $-(1-\mu)$ cancels noise mass $1-\mu$ times $\mu$, and the bid mirrors it: the loss to informed traders equals the gain from noise, while the variance of the quote stays with the maker.
- the informed trader's profit per unit at $A^{*}=\mu$ and $B^{*}=-\mu$ in the one-period Glosten–Milgrom game, with informed mass $\mu$ and $v=\pm1$ ::@:: $1-\mu$: at $v=+1$ it buys at $\mu$ and keeps $1-\mu$, and at $v=-1$ it sells at $-\mu$ and keeps $-\mu-(-1)=1-\mu$.
- the noise trader's loss per trade at $A^{*}=\mu$ and $B^{*}=-\mu$ in the one-period Glosten–Milgrom game ::@:: $\mu$: a noise buyer pays $\mu$ for an asset worth $0$ in expectation, and a noise seller gives up that asset for $-\mu$.
- why the informed traders' total gain equals the noise traders' total loss in the one-period Glosten–Milgrom game, with informed mass $\mu$ and $A^{*}=\mu$, $B^{*}=-\mu$ ::@:: Both equal $\mu(1-\mu)$: informed mass $\mu$ gains $1-\mu$ each and noise mass $1-\mu$ loses $\mu$ each, so the noise traders' losses fund the informed traders' gains.
- what the market maker does between informed and noise traders in the one-period Glosten–Milgrom game, at $A^{*}=\mu$ and $B^{*}=-\mu$ ::@:: It acts as a conduit: it charges each side the value of the asset conditional on the order it receives, breaks even in expectation, and bears the variance of the quote while the noise traders' losses pass through to the informed traders.

## spread

The ask sits at $A^{*}=\mu$ and the bid at $B^{*}=-\mu$, so the equilibrium bid-ask spread is $S=A-B=2\mu$. The informed share is charged once for each side of the book: a buyer pays $\mu$ above the prior value and a seller receives $\mu$ below it, and both charges come from the same asymmetry. Neither an order-processing cost nor an inventory position enters the model, so none of $S$ is a transaction cost. The spread is positive because of information asymmetry: the market maker charges $S$ to counteract the adverse selection it suffers against informed traders. It also widens as the number of informed traders increases, $\mu\uparrow$.

What the [Roll model](Roll%20model.md) assumed is now derived: a positive spread $A>B$ has a cause inside the game, the asymmetry of information between the traders and the market makers.

---

Flashcards for this section are as follows:

- the equilibrium bid-ask spread in the one-period Glosten–Milgrom model, with $A^{*}=\mu$ and $B^{*}=-\mu$ ::@:: $S=A-B=2\mu$.
- why the Glosten–Milgrom spread $S$ is positive ::@:: Because of information asymmetry: the market maker charges $S>0$ to counteract the adverse selection cost it suffers against informed traders.
- how the spread $S=2\mu$ responds to more informed trading ::@:: It widens: $S$ increases with $\mu$, the mass of informed traders.
- what the Glosten–Milgrom model endogenises, in place of a spread $S$ taken as given ::@:: The positive spread $A>B$, derived from asymmetric information between the traders and the market makers.
- why the spread $S=2\mu$ counts the informed share twice in the one-period Glosten–Milgrom model ::@:: Once for each side of the book: the buyer pays $\mu$ above the prior value and the seller receives $\mu$ below it, and both charges come from the same asymmetry.

## degree of uncertainty

The frequency of informed trading is not the only input to the spread. Let the value be $v=+\sigma$ or $v=-\sigma$ with probability $\frac{1}{2}$ each. The prior mean is still $\operatorname{E}[v]=0$, and the ex-ante uncertainty is $\operatorname{Var}(v)=\frac{1}{2}(\sigma^{2}+\sigma^{2})=\sigma^{2}$.

The signal is unchanged. An informed trader still buys for sure when $v=+\sigma$ and sells when $v=-\sigma$, and a noise trader still picks a side with probability $\frac{1}{2}$. The precision is $\operatorname{Pr}(\text{Buy}\mid v=\sigma)=\operatorname{Pr}(\text{Sell}\mid v=-\sigma)=\frac{1+\mu}{2}$ and $\operatorname{Pr}(\text{Buy}\mid v=-\sigma)=\operatorname{Pr}(\text{Sell}\mid v=+\sigma)=\frac{1-\mu}{2}$. The posterior after a buy is again $\operatorname{Pr}(+\sigma\mid\text{Buy})=\frac{1+\mu}{2}$, and the conditional expectation scales with the value: $\operatorname{E}[v\mid\text{Buy}]=\operatorname{Pr}(+\sigma\mid\text{Buy})\sigma+\operatorname{Pr}(-\sigma\mid\text{Buy})(-\sigma)=\left(\frac{1+\mu}{2}-\frac{1-\mu}{2}\right)\sigma=\mu\sigma$.

The expectation $\operatorname{E}[v\mid\text{Buy}]=\mu\sigma+(1-\mu)\cdot0$ is a weighted average: $\mu$ sits on the value and $1-\mu$ on the prior mean. At $\mu=0$ the quote stays where the market started. At $\mu=1$ it lands on the value. In between it covers the fraction $\mu$ of the distance from the prior mean to the value, so one buy moves the quote by the informed share of the crowd. How far that is depends on how wide the gap between the two possible values is. The weights are probabilities, and a precision-weighted reading is not available here. A normal posterior weights each input by precision because the prior mean and the signal are two estimates of one quantity. A value with two possible outcomes leaves nothing to estimate between them, so each outcome enters with the probability the order assigns it.

Equilibrium follows the $v=\pm1$ case with $\sigma$ in place of $1$: $A^{*}=\mu\sigma$, $B^{*}=-\mu\sigma$, and $S=A^{*}-B^{*}=2\mu\sigma$. The spread is a product of two quantities, $\sigma$ and $\mu$. Doubling either one doubles $S$, so the spread impounds both how much there is to know and how often someone knows it. As $\sigma\to0$ the two values converge and the informed trader knows nothing a noise trader does not, so the spread closes with them; at $\mu=0$ it is already closed, since every trade is then noise.

---

Flashcards for this section are as follows:

- the prior and its variance when the asset value is $v=+\sigma$ or $v=-\sigma$ with probability $\frac{1}{2}$ each ::@:: $\operatorname{E}[v]=0$ and $\operatorname{Var}(v)=\frac{1}{2}(\sigma^{2}+\sigma^{2})=\sigma^{2}$.
- the conditional expectation $\operatorname{E}[v\mid\text{Buy}]$ with $v=\pm\sigma$ at probability $\frac{1}{2}$ each, informed mass $\mu$, and $\operatorname{Pr}(\text{Buy}\mid v=\sigma)=\operatorname{Pr}(\text{Sell}\mid v=-\sigma)=\frac{1+\mu}{2}$ ::@:: $\operatorname{E}[v\mid\text{Buy}]=\frac{1+\mu}{2}\sigma+\frac{1-\mu}{2}(-\sigma)=\mu\sigma$.
- what $\operatorname{E}[v\mid\text{Buy}]=\mu\sigma$ says read as a weighted average, with $v=+\sigma$ or $v=-\sigma$ at probability $\frac{1}{2}$ each and informed mass $\mu$ ::@:: The value carries weight $\mu$ and the prior mean $0$ carries $1-\mu$, so the quote sits the fraction $\mu$ of the way from the prior mean to the value: at $\mu=0$ it stays at the prior mean and at $\mu=1$ it lands on the value.
- how far one buy moves the quote, in words, when $v=+\sigma$ or $v=-\sigma$ with probability $\frac{1}{2}$ each and the informed mass is $\mu$ ::@:: By the share of the crowd that knows the value, across the gap between the two possible values: more informed traders move it further, and a wider gap gives more room to move.
- why the weights in $\operatorname{E}[v\mid\text{Buy}]=\mu\sigma+(1-\mu)\cdot0$ are probabilities rather than precisions, when $v=+\sigma$ or $v=-\sigma$ with probability $\frac{1}{2}$ each and informed mass $\mu$ ::@:: The value has only two possible outcomes, so each enters with its own probability. A normal posterior weights by precision instead, because the prior mean and the signal are two estimates of one quantity rather than two distinct outcomes.
- the equilibrium ask, bid and spread when $v=\pm\sigma$ in the one-period Glosten–Milgrom model, with informed mass $\mu$ and $\operatorname{E}[v\mid\text{Buy}]=\mu\sigma$ ::@:: $A^{*}=\mu\sigma$, $B^{*}=-\mu\sigma$ and $S=A^{*}-B^{*}=2\mu\sigma$.
- what $\sigma$ measures when the asset value is $v=\pm\sigma$ in the Glosten–Milgrom model ::@:: The informational advantage of an informed trader, so that $\sigma\to0$ makes the two values converge and leaves information with no value.
- the two factors the spread $S=2\mu\sigma$ impounds ::@:: How much there is to know, $\sigma$, the distance between the two possible values, and how often someone knows it, $\mu$, the frequency of informed trading; doubling either doubles $S$.

### value of the asset

Read $\sigma$ as the value of the asset. The two states are $v=+\sigma$ and $v=-\sigma$, each $\sigma$ from the prior mean $\operatorname{E}[v]=0$, so the pair lies $2\sigma$ apart. A larger $\sigma$ is an asset whose good and bad states are further apart, and the informed trader who knows which state has arrived holds knowledge worth $\sigma$ before the quote is charged for it.

---

Flashcards for this section are as follows:

- the value reading of $\sigma$ when $v=+\sigma$ or $v=-\sigma$ with probability $\frac{1}{2}$ each in the Glosten–Milgrom model ::@:: $\sigma$ is the size of the asset's possible value: each state sits $\sigma$ from the prior mean, the pair lies $2\sigma$ apart, and a larger $\sigma$ is an asset whose good and bad states are further apart.

### uncertainty of the asset

The same symbol is the asset's uncertainty. The prior variance is $\operatorname{Var}(v)=\sigma^{2}$, so $\sigma$ is the standard deviation of the prior and measures how unpinned the value is before any order arrives. A larger $\sigma$ is a value nobody has settled.

---

Flashcards for this section are as follows:

- the uncertainty reading of $\sigma$ when $v=\pm\sigma$ with probability $\frac{1}{2}$ each in the Glosten–Milgrom model ::@:: The prior variance is $\operatorname{Var}(v)=\sigma^{2}$, so $\sigma$ is how unpinned the value is before any order arrives, and a larger $\sigma$ is a value nobody has settled.

### amount of the asset

It is also the amount of the asset at stake. At $v=+\sigma$ the informed trader pays $A^{*}=\mu\sigma$ for something worth $\sigma$ and keeps $\sigma-\mu\sigma=(1-\mu)\sigma$, so $\sigma$ scales the stake one informed trade carries. A larger $\sigma$ is a larger position riding on the same information.

---

Flashcards for this section are as follows:

- the amount reading of $\sigma$ when $v=\pm\sigma$ and the informed mass is $\mu$ in the one-period Glosten–Milgrom model ::@:: The informed trader's profit at $v=+\sigma$ is $\sigma-A^{*}=(1-\mu)\sigma$, so $\sigma$ scales the stake one informed trade carries, and a larger $\sigma$ is a larger position riding on the information.

### product of the readings

Only the product reaches the prices. The quote carries $\mu\sigma$ and the spread carries $2\mu\sigma$, so a small value gap traded in size, a wide prior, and a large informed position can all land on the same $\sigma$ and with it the same $S$, and the quotation cannot tell which of the three grew. That is what the product form buys the model: one symbol covers all three, and no result needs to know which of them moved, only that the product did.

---

Flashcards for this section are as follows:

- why value size, uncertainty and position size all read into the spread $2\mu\sigma$ in the one-period Glosten–Milgrom model ::@:: Only the product reaches the prices: the quote carries $\mu\sigma$ and the spread $2\mu\sigma$, so a small value gap traded in size, a wide prior, and a large informed position can all land on the same $\sigma$ and with it the same $S$.
- what the product form $\mu\sigma$ buys the Glosten–Milgrom model ::@:: One symbol covers the size of the value, the uncertainty about it, and the quantity at stake, so no result needs to know which of the three grew, only that the product did.
