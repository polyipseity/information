---
aliases:
  - no trade theorem
  - no-trade theorem
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/no-trade_theorem
  - language/in/English
---

# no-trade theorem

Private information is a motive to trade in [financial markets](financial%20system.md). Costly analysis produces knowledge about an asset's worth that other traders cannot see, and its holder hopes to trade with a counterpart for profit. [Bayes' theorem](Bayes%27%20theorem.md) closes that motive off. Applying the update to the trading game gives the no-trade theorem of Stokey and Milgrom (1982, Journal of Economic Theory (JET)): no trade happens motivated by asymmetric information, that is, by speculative motives.

---

Flashcards for this section are as follows:

- what the no-trade theorem states ::@:: No trade happens motivated by asymmetric information, that is, speculative motives.
- the theorem showing that no trade happens from asymmetric information alone, because a counterparty who is willing to trade reveals information that stops the trade ::@:: Nancy Stokey and Paul Milgrom, 1982, Journal of Economic Theory (JET).
- why private information motivates a trade before the counterparties reason about each other ::@:: Costly analysis produces knowledge about an asset's worth that other traders cannot see, and its holder hopes to trade with a counterpart for profit.

## speculative trade

The model has two steps. The first fixes a price $p$ and works out which side each trader takes at that price, which says nothing about where $p$ came from or which prices a market produces. The second drops the fixed price and asks for one at which both traders are willing to take opposite sides at the same time. This section takes the first step, and [§ equilibrium price](#equilibrium%20price) takes the second.

Two traders, A and B, trade one asset between themselves, each holding a private signal about what it will pay. The asset pays a random final payoff $V$ in dollars: $V_H = 120$ with probability $\frac{1}{2}$ and $V_L = 0$ with probability $\frac{1}{2}$. Each trader observes a signal $s_i \in \{s_H, s_L\}$, and the signals are right more often than wrong: $\operatorname{Pr}(s_H \mid V_H) = \operatorname{Pr}(s_L \mid V_L) = \frac{2}{3}$ and $\operatorname{Pr}(s_L \mid V_H) = \operatorname{Pr}(s_H \mid V_L) = \frac{1}{3}$. The traders trade one unit of the asset each. Accuracy $\frac{2}{3}$ is all a signal is worth. With the two payoffs equally likely, the likelihood ratio is $\frac{2/3}{1/3} = 2$, so the signal doubles the odds of the state it names: even odds become two to one, and the posterior becomes $\frac{2}{3}$. Read the other way, the signal is wrong once in three, so a trader who acts on it holds the worthless payoff that often.

A trader who observes $s_H$ updates by [Bayes' theorem](Bayes%27%20theorem.md): $\operatorname{Pr}(V_H \mid s_H) = \frac{\operatorname{Pr}(V_H)\operatorname{Pr}(s_H \mid V_H)}{\operatorname{Pr}(V_H)\operatorname{Pr}(s_H \mid V_H) + \operatorname{Pr}(V_L)\operatorname{Pr}(s_H \mid V_L)} = \frac{2}{3}$, so $\operatorname{E}[V \mid s_H] = \frac{2}{3}V_H + \frac{1}{3}V_L = 80$ dollars. The good signal shifts the expectation up from the prior $\operatorname{E}[V] = 60$ dollars, and the symmetric argument gives $\operatorname{E}[V \mid s_L] = 40$ dollars. Each posterior is the payoff range $V_H - V_L = 120$ dollars weighted by the probability it puts on the high payoff, so the $\frac{2}{3}$ posterior gives 80 and the $\frac{1}{3}$ posterior gives 40. Call the accuracy $q = \frac{2}{3}$. The 20-dollar move away from the prior is the accuracy above a coin flip, $q - \frac{1}{2} = \frac{1}{6}$, times that 120-dollar range. The gap between the two traders is the same range times how far apart the posteriors sit, $(2q-1)(V_H - V_L) = 40$ dollars.

Facing a price $p$, trader $i$ chooses a position $d_i \in \{+1, -1\}$: buying means $d_i = +1$, the trader receives $V$ and pays $p$, and $d_i = -1$ means selling. The trader maximizes the position's payoff, $R_i = \operatorname{E}[d_i(V - p) \mid s_i, p] = d_i(\operatorname{E}[V \mid s_i, p] - p)$, which earns $\operatorname{E}[V \mid s_i, p] - p$ on a buy and $p - \operatorname{E}[V \mid s_i, p]$ on a sell. So the trader buys when $\operatorname{E}[V \mid s_i, p] > p$ and sells when $\operatorname{E}[V \mid s_i, p] < p$. The expectation conditions on the trader's own signal $s_i$ and on the price $p$, which itself conveys information. The position is one unit and enters linearly, so the only choice left is the sign of the edge $\operatorname{E}[V \mid s_i, p] - p$. In the market the rule is simpler: a trader buys when the asset is worth more to them than the price and sells when it is worth less. Nobody trades a larger or smaller quantity, so the whole decision the model allows is which side, and a trader whose expectation equals the price has nothing to do.

---

Flashcards for this section are as follows:

- what the first step of the speculative-trade model fixes about a price $p$, and what it leaves open ::@:: A price $p$ is fixed, and the model works out which side each trader takes at that price; that says nothing about where $p$ came from or which prices a market produces.
- the final payoff $V$, in dollars, of the asset in the one-unit speculative-trade game of traders A and B ::@:: $V$ takes $V_H = 120$ with probability $\frac{1}{2}$ and $V_L = 0$ with probability $\frac{1}{2}$.
- the private signals $s_i$ each trader observes in the one-unit game and their accuracy ::@:: Each trader observes $s_i \in \{s_H, s_L\}$ with $\operatorname{Pr}(s_H \mid V_H) = \operatorname{Pr}(s_L \mid V_L) = \frac{2}{3}$ and $\operatorname{Pr}(s_L \mid V_H) = \operatorname{Pr}(s_H \mid V_L) = \frac{1}{3}$, and the traders trade one unit each.
- with $\operatorname{Pr}(V_H) = \operatorname{Pr}(V_L) = \frac{1}{2}$, $V_H = 120$ dollars, $V_L = 0$ dollars, and $\operatorname{Pr}(V_H \mid s_H) = \frac{2}{3}$, compute $\operatorname{E}[V \mid s_H]$ ::@:: $\operatorname{E}[V \mid s_H] = \frac{2}{3}V_H + \frac{1}{3}V_L = 80$ dollars, a shift up from the prior $\operatorname{E}[V] = 60$ dollars.
- what a signal accuracy of $\operatorname{Pr}(s_H \mid V_H) = \operatorname{Pr}(s_L \mid V_L) = \frac{2}{3}$ is worth when $V_H = 120$ dollars and $V_L = 0$ dollars are equally likely ::@:: A likelihood ratio of 2, so the signal doubles the odds of the state it names: even odds become two to one, the posterior becomes $\frac{2}{3}$, and the expectation moves to 80 dollars.
- what a $\frac{2}{3}$-accurate signal means for a trader who acts on it, in words ::@:: The signal is right twice as often as wrong, so acting on it still means holding the worthless payoff one time in three.
- why the 20-dollar move from the prior $\operatorname{E}[V] = 60$ dollars to $\operatorname{E}[V \mid s_H] = 80$ dollars is that size, with payoff range $V_H - V_L = 120$ dollars and accuracy $q = \frac{2}{3}$ ::@:: The move is the accuracy above a coin flip times the payoff range, $\left(q - \frac{1}{2}\right)(V_H - V_L) = \frac{1}{6} \times 120$: a sharper signal moves the valuation closer to the payoff it points at.
- why $\operatorname{E}[V \mid s_H] = 80$ dollars and $\operatorname{E}[V \mid s_L] = 40$ dollars are 40 dollars apart, with $V_H = 120$ dollars, $V_L = 0$ dollars and accuracy $q = \frac{2}{3}$ ::@:: Each is the payoff range times the posterior probability it carries, $\frac{2}{3} \times 120$ and $\frac{1}{3} \times 120$, so the gap is the range times the distance between the posteriors, $(2q - 1)(V_H - V_L) = 40$ dollars.
- what a 40-dollar gap between two traders' valuations means for a trade, in words ::@:: The two disagree about what the asset is worth by 40 dollars around a prior of 60, so any trade has to bridge that disagreement, and a signal of that accuracy cannot open a wider gap.
- the payoff $R_i$ trader $i$ maximizes by choosing a position $d_i \in \{+1, -1\}$ at price $p$ ::@:: $R_i = \operatorname{E}[d_i(V - p) \mid s_i, p] = d_i(\operatorname{E}[V \mid s_i, p] - p)$, which earns $\operatorname{E}[V \mid s_i, p] - p$ on a buy and $p - \operatorname{E}[V \mid s_i, p]$ on a sell.
- the action a trader $i$ takes at price $p$, given the expectation $\operatorname{E}[V \mid s_i, p]$ ::@:: The trader buys when $\operatorname{E}[V \mid s_i, p] > p$ and sells when $\operatorname{E}[V \mid s_i, p] < p$.
- why $R_i = d_i(\operatorname{E}[V \mid s_i, p] - p)$ over $d_i \in \{+1, -1\}$ leaves the trader only a sign to choose, with price $p$ ::@:: The position is one unit and the payoff is linear in it, so the trader chooses only the sign of the edge $\operatorname{E}[V \mid s_i, p] - p$: $+1$ when the edge is positive, $-1$ when it is negative, and the payoff is the size of the edge.
- when a trader buys and when they sell at price $p$, with expectation $\operatorname{E}[V \mid s_i, p]$ and one unit to trade ::@:: Buys when the asset is worth more to them than the price and sells when it is worth less, with the size fixed at one unit, so the whole decision is which side and a trader whose expectation equals the price is indifferent.

## equilibrium price

This section takes the second step, where the price stops being given. A market price has to be one at which A is willing to buy and B is willing to sell at the same time. A price held fixed settles only what a trader does there; a real price has to clear. The first step, with the price held fixed, is in [§ speculative trade](#speculative%20trade).

One trader buys what the other sells, so the positions clear the market when $d_A + d_B = 0$. Substituting the two positions into the payoff gives $(d_A + d_B)(V - p) = 0$, so the traders' realized gains sum to zero whatever the asset pays: a trade here only moves the payoff from one trader to the other, and the price decides how it is split. If A observes $s_H$ and B observes $s_L$, A expects 80 dollars and B expects 40 dollars. Every price in $40 < p < 80$ makes buying worth more than selling for A and selling worth more than buying for B.

Identical information rules out trade at every price. Two traders conditioning on the same information set hold the same expectation: both on $s_H$ expect 80 dollars, so below 80 both buy, above 80 both sell, and at 80 both stand aside. A tie counts as no trade, so the two never take opposite sides. Both want the same side at every price, so they do not disagree about which price is right, and no price makes the trade happen.

Differing signals leave the whole interval between the two valuations open: A buys only below 80 and B sells only above 40. Both ends are open because at exactly a valuation the trader on that side is indifferent and the trade earns nothing. The width of the interval is the disagreement. At an accuracy of $\frac{2}{3}$ that is 40 dollars. It closes to zero when the signals agree and widens toward the full 120 dollars as the signals sharpen. No trade happens at any price in that band once the reasoning runs one step further: a counterpart's willingness to take the other side is evidence of what that counterpart knows, and once both traders absorb it, the disagreement the trade needed is gone ([§ higher-order beliefs](#higher-order%20beliefs)).

---

Flashcards for this section are as follows:

- what the second step of the no-trade model does with the price, and why ::@:: It drops the fixed price, because a market price has to be one at which the buyer is willing to buy and the seller is willing to sell at the same time.
- the market-clearing condition, in terms of the positions $d_A$ and $d_B$, for a trade between traders A and B ::@:: The positions clear the market when $d_A + d_B = 0$: one trader buys and the other sells.
- the price range for $p$, in dollars, that both traders accept when A expects 80 dollars and B expects 40 dollars ::@:: Every price in $40 < p < 80$ makes buying worth more than selling for A and selling worth more than buying for B.
- why identical information rules out trade at every price, in the one-unit game of traders A and B ::@:: Both traders condition on the same information set and hold the same expectation, so at any price both want to buy, both want to sell, or both stand aside; a tie counts as no trade, so they never take opposite sides.
- why the same-information failure is not a matter of the traders picking the wrong price ::@:: Every price fails for one reason, since both traders want the same side whatever the price is: no price exists that makes the trade happen, and the two do not disagree about which price is right.
- what the clearing condition $d_A + d_B = 0$ implies about the two traders' realized gains, with payoff $V$ and price $p$ ::@:: Their gains sum to zero at every outcome, $(d_A + d_B)(V - p) = 0$: one trader's gain is exactly the other's loss, so a trade only moves the asset's payoff between them and the price splits it.
- why the acceptable price band $40 < p < 80$ dollars is open at both ends, given $\operatorname{E}[V \mid s_H] = 80$ dollars and $\operatorname{E}[V \mid s_L] = 40$ dollars ::@:: A buys only below 80 and B sells only above 40, and at exactly a valuation the trader on that side is indifferent, so the trade earns nothing and the inequality is strict.
- what the width of the price band measures, with $\operatorname{E}[V \mid s_H] = 80$ dollars and $\operatorname{E}[V \mid s_L] = 40$ dollars ::@:: The disagreement between the two traders: it runs from what the seller thinks the asset is worth to what the buyer thinks it is worth, it closes to zero when the signals agree, and it widens as the signals sharpen.

## higher-order beliefs

A trade at price $p$ conveys more than the clearing of the market. Suppose A observes $s_H$ and buys, so $d_A = +1$. The trade happens only because B finds selling at $p$ profitable and A finds buying at $p$ profitable. Each trader reads the other's willingness as a statement about the other's information, and each knows the other reasons the same way: one trader knows what the other believes, and knows that the other knows it. The chain of beliefs does not stop at one link. This is higher-order belief formation, and it comes from the traders being rational.

A reads the trade as revealing B's signal: A concludes that B received $s_L$. The inference runs both ways, since B reads A's buy in the same way and concludes that A received $s_H$. Each round of that reasoning hands over one piece of the counterpart's information, and the rounds stop once both traders condition on $s_H$ and $s_L$, because a further round reveals nothing new. The subscript $i$ then drops out of $\operatorname{E}[V \mid s_i, p]$: the conditioning set no longer depends on who is conditioning. Both traders work from $\operatorname{E}[V \mid s_H, s_L]$, and each maximizes $R_i = d_i(\operatorname{E}[V \mid s_H, s_L] - p)$.

The end point is the case already closed in [§ equilibrium price](#equilibrium%20price). Both traders then hold the same information set, so both hold the same expectation, and no price leaves one buying while the other sells. They start out disagreeing, and each round of reasoning about the counterpart's willingness hands over one more piece of their information, so the process converges on the same information set and the disagreement closes with it. The trade stops there.

In market terms, a trade refutes itself. The only counterparty willing to sell to a trader just told the asset is worth 80 dollars is someone told it is worth 40. That is the trader a buyer should least want to face, and A's gain is paid by exactly that counterpart: willingness to take the other side is the evidence the gain is gone. The trade hands the information over as it happens.

[Price discovery](price%20discovery.md) measures how much information about the signals $s_i$ a traded price carries.

The reasoning has the shape of a payoff matrix worked down to equilibrium. Dropping an action that cannot be a best response leaves a smaller game, and the dropping repeats until the action left is a best response to itself, which is a Nash equilibrium. The traders eliminate in the same way: an action goes because the counterpart's willingness to take the other side shows the action cannot pay, and each round of inference removes the trades one side would refuse. What remains is the no-trade outcome. That point follows from the inference, with no separate assumption about prices.

---

Flashcards for this section are as follows:

- what each trader learns from the fact that a trade happened at price $p$ ::@:: The counterpart is willing to trade at $p$: A finds buying profitable there and B finds selling profitable there, and each trader reads that willingness as a statement about the counterpart's information.
- what higher-order beliefs are in the one-unit speculative-trade game ::@:: Each trader conditions expectations on what the counterpart believes and knows the counterpart does the same, so belief formation runs in chains such as A knowing that B believes that the trade is profitable for B.
- the signal trader A concludes B received once A sees B sell at price $p$ ::@:: A concludes that B received $s_L$.
- the maximization both traders reach once each incorporates both signals $s_H$ and $s_L$ ::@:: Each maximizes $R_i = d_i(\operatorname{E}[V \mid s_H, s_L] - p)$.
- why the trade cannot happen once both traders condition on both $s_H$ and $s_L$ ::@:: Both then hold the same $\operatorname{E}[V \mid s_H, s_L]$, so no price leaves one buying while the other sells: the disagreement the trade needs is exactly what the trade has removed.
- why the subscript $i$ disappears from $\operatorname{E}[V \mid s_i, p]$ once a trade at price $p$ reveals the counterpart's signal ::@:: The conditioning set stops depending on who is doing the conditioning: $p$ tells A that B holds $s_L$ and tells B that A holds $s_H$, so both traders condition on the same two signals and one expectation replaces two.
- why a profitable speculative trade cannot survive its own revelation, in words ::@:: The only trader willing to sell to someone told the asset is worth 80 dollars is one told it is worth 40. That willingness is the evidence the buyer's edge is gone, so acting on the trade destroys the disagreement the trade needed.
- how reasoning about a counterpart's willingness converges, with signals $s_H$ and $s_L$ ::@:: Each round hands over one piece of the counterpart's information, so the traders end on the same information set $s_H, s_L$; there both hold the same expectation, so no price leaves one buying while the other sells.
- how the no-trade inference compares with eliminating actions from a payoff matrix ::@:: Both narrow until no one wants to change their action: an action is dropped because the counterpart's willingness shows it cannot pay, and what is left is a best response to itself, a Nash equilibrium; the no-trade outcome sits at that point, and the inference enforces it.

## assumptions behind the result

The result rests on assumptions. The traders share a common prior about the game structure, and that prior is common knowledge. The traders are rational. No trader holds an endowment, so risk-sharing never motivates a trade. The result turns on the price fully revealing private information: then no traders want to trade.

An endowment is a position the trader already holds. The decision is how much of that position to keep, so a trade can adjust an existing holding instead of acting on an edge. A trader who owns a concentrated block and wants less of it sells part of that block while holding no view on $V$ at all.

The sale serves risk-sharing. Two traders with different exposures or different tolerances for risk can both gain by splitting the exposure, and the gain comes from the split rather than from either trader's information. A second trader with less exposure, or a higher tolerance for risk, buys part of that block, and both end up better off. With the motive present, a trade happens even when neither trader's information says anything the other does not know, so the no-trade conclusion fails; ruling the motive out leaves the informational one.

Trading does happen, so these assumptions fail somewhere in practice. An endowment gives traders risk-sharing motives to trade on, biased beliefs take the place of the rationality the inference chain needs, and without a common prior about the game structure the traders no longer reason from shared knowledge. Information frictions of this kind contribute to the [spread](bid-ask%20spread.md) and trade dynamics in [market microstructure](market%20microstructure.md).

---

Flashcards for this section are as follows:

- the assumptions the no-trade theorem hinges on ::@:: A common prior about the game structure, common knowledge among the traders; rational traders; and no trader holding an endowment, so risk-sharing never motivates a trade.
- the point the no-trade theorem turns on ::@:: The price fully reveals private information; then no traders want to trade.
- what an endowment is in the no-trade model, where the asset pays $V$, and how it changes a trader's decision ::@:: A position the trader already holds. The decision is how much of that position to keep, so a trade can adjust an existing holding instead of acting on an edge: a trader owning a concentrated block they want less of sells part of it with no view on $V$.
- why risk-sharing is a motive for trade that carries no information, and what the no-trade result looks like with it ::@:: Two traders with different exposures or different tolerances for risk both gain by splitting the exposure, and the gain comes from the split rather than from either signal. A second trader with less exposure buys part of a concentrated block, so a trade happens even when neither trader's information says anything the other does not know. The no-trade conclusion fails until the motive is ruled out.
- why trading activity observed in reality does not contradict the no-trade theorem ::@:: The observed trade means the assumptions fail in reality: endowments give risk-sharing motives, traders can hold biased beliefs, and the game structure need not be common knowledge.
