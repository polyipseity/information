---
aliases:
  - price discovery
  - price efficiency
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/price_discovery
  - language/in/English
---

# price discovery

Price discovery is the process by which a traded price comes to reflect available information: how quickly the price incorporates new information, and how far it departs from the price that information would justify.

---

Flashcards for this section are as follows:

- what price discovery is ::@:: The process by which a traded price comes to reflect available information.
- two things price discovery measures ::@:: How quickly the price incorporates new information, and how far it departs from the price that information justifies.

## efficient price

The efficient price of an asset with value $v$ is $p^{*} = \operatorname{E}[v \mid \text{available information}]$. Price discovery is the speed at which the traded price converges to it.

---

Flashcards for this section are as follows:

- formula for the efficient price $p^{*}$ of an asset with value $v$ ::@:: $p^{*} = \operatorname{E}[v \mid \text{available information}]$, the conditional expectation of the value given the information available to the market.
- relation between price discovery and the efficient price ::@:: Price discovery is how quickly the traded price converges to the efficient price.

## deviations from the efficient price

A traded price departs from the efficient price for three reasons. Without informed trading, information never reaches the price; information frictions delay it; structural frictions hold the price away from the value through the mechanics of trading.

---

Flashcards for this section are as follows:

- absence of informed trading ::@:: Information never reaches the price.
- information frictions ::@:: Information reaches the price only with delay.
- structural frictions ::@:: The mechanics of trading hold the price away from the value.
- three sources of deviation from the efficient price ::@:: Absence of informed trading, information frictions, and structural frictions.

## dark pools and price efficiency

Zhu (2014, _Review of Financial Studies_ (RFS)) finds that dark pools improve price efficiency by sorting informed and noise traders across venues. Informed traders face high execution risk in dark pools, because good news clusters them on the buy side, so they migrate to lit exchanges. Noise traders are randomly distributed and get the price improvement dark pools offer, leaving the lit exchange with more informative prices.

---

Flashcards for this section are as follows:

- how dark pools improve price efficiency ::@:: By sorting informed traders to lit exchanges and noise traders to dark pools.
- why informed traders prefer lit exchanges over dark pools ::@:: Good news clusters them on the buy side in dark pools, creating high execution risk; lit exchanges offer no such risk.
- why noise traders prefer dark pools ::@:: They get price improvement (midpoint trading) without the execution risk informed traders face.
- which paper shows informed traders leaving dark pools for lit venues because execution risk rations them in the dark, and the price-efficiency gain that this sorting produces? ::@:: Haoxiang Zhu, 2014, Review of Financial Studies (RFS), the paper behind the sorting argument for dark pools.

## weighted price contribution

_Weighted price contribution_ (WPC) measures how much each group of orders moves the price towards the efficient price. Li, Ye, and Zheng (2022, _Journal of Financial Economics_ (JFE)) compute it by order type on the New York Stock Exchange, and the contributions sum to 100%. The order types partition the price move between them rather than each claiming an overlapping part of it. A positive entry is the share of the move that ran towards the efficient price, and a negative entry is the share that ran away from it, so the type pushed the price against the value rather than contributing little.

| Order type | Share of taking volume | WPC |
| --- | --- | --- |
| Plain market | 6.77% | -4.56% |
| Plain IOC | 6.36% | 3.86% |
| ISO | 35.69% | 90.32% |
| DNS IOC | 25.87% | 27.10% |
| DAY limit | 16.37% | -13.78% |
| DNS limit | 5.30% | -2.34% |
| Reserve limit | 3.43% | -0.95% |
| Reserve DNS limit | 0.21% | 0.35% |

The orders that refuse to route carry more than the whole. The intermarket sweep, the two do-not-ship (DNS) immediate-or-cancel entries, and the DNS limit order add up to 115.43%, while the four routable types subtract 15.43%. With the move partitioned, more than 100% on one side forces a negative total on the other: the orders that refuse to route produce the whole move and the excess, and the orders that follow the routing rule hand that excess back. Those orders also make up most of the taking volume, so the premise that an order executes where the best quote is holds for a minority of executions.

The intermarket sweep is the clearest case. It carries 35.69% of the taking volume and 90.32% of the contribution, so a third of the volume does most of the price adjustment.

The day limit order runs the other way. It carries 16.37% of the taking volume and a contribution of -13.78%, the largest negative in the table. The DNS limit order is negative too, at -2.34%, even though it refuses to route. Its immediate-or-cancel counterpart carries the same routing instruction with a different time in force and scores +27.10%, so the routing instruction does not set the sign of the contribution. What separates the pair is whether the order waits on the book or executes on arrival.

A routable order arrives second. It is sent to whichever venue quotes the best price, by which time the news has usually been traded there, and its own volume pushes the price further past efficient. An order that refuses routing has nowhere else to go: it either rests on the book waiting or goes straight to one venue, and it meets the informed flow when it arrives. Those orders are also the ones that trade successfully on new information, which points to the high-speed informed traders as their users.

---

Flashcards for this section are as follows:

- why a negative weighted price contribution is a push away from the efficient price rather than a small contribution ::@:: The contributions partition the price move and sum to 100%, so a negative share is a move against the efficient price, with the sign giving the direction and the size the share.
- which paper computes the weighted price contribution of each order type on the New York Stock Exchange and finds that the orders which refuse to route contribute more than the whole price move? ::@:: Sida Li, Mao Ye and Miles Zheng, 2022, Journal of Financial Economics (JFE), the paper behind the order-type weighted price contribution.
- total contribution of the non-routable types against the routable ones ::@:: 115.43% against -15.43%.
- what most of the taking volume sitting in orders that refuse to route implies about the premise that an order executes where the best quote is ::@:: The premise holds for a minority of executions, because these orders execute at whichever venue receives them rather than at the best quote.
- share of taking volume and of contribution carried by the intermarket sweep ::@:: 35.69% of the volume and 90.32% of the contribution, so it does most of the price adjustment on a third of the volume.
- largest negative contribution in the table ::@:: The day limit order, at -13.78% on 16.37% of the taking volume.
- which traders the evidence points to as the users of the non-routable orders ::@:: High-speed informed traders, who trade successfully on new information.
