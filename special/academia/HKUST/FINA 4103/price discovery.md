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

Zhu (2014, _Review of Financial Studies_) finds that dark pools improve price efficiency by sorting informed and noise traders across venues. Informed traders face high execution risk in dark pools, because good news clusters them on the buy side, so they migrate to lit exchanges. Noise traders are randomly distributed and get the price improvement dark pools offer, leaving the lit exchange with more informative prices.

---

Flashcards for this section are as follows:

- how dark pools improve price efficiency ::@:: By sorting informed traders to lit exchanges and noise traders to dark pools.
- why informed traders prefer lit exchanges over dark pools ::@:: Good news clusters them on the buy side in dark pools, creating high execution risk; lit exchanges offer no such risk.
- why noise traders prefer dark pools ::@:: They get price improvement (midpoint trading) without the execution risk informed traders face.
- what Zhu (2014) concludes ::@:: Dark pools benefit the market by cleansing the lit exchange of noise.

## weighted price contribution

_Weighted price contribution_ (WPC) measures how much each group of orders moves the price towards the efficient price. A positive WPC means the order type helped the price converge. A negative one means it pushed the price further away. Li, Ye, and Zheng (2022, _Journal of Financial Economics_) compute it by order type on the New York Stock Exchange, and the column sums to 100%.

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

The orders that refuse to route carry more than the whole. The intermarket sweep, the two DNS immediate-or-cancel entries, and the DNS limit order add up to 115.43%, while the four routable types subtract 15.43%.

The intermarket sweep is the clearest case. It carries 35.69% of the taking volume and 90.32% of the contribution.

The day limit order runs the other way. It carries 16.37% of the taking volume and a contribution of -13.78%, the largest negative in the table. The DNS limit order is negative too, at -2.34%, even though it refuses to route. Its immediate-or-cancel counterpart carries the same routing instruction with a different time in force and scores +27.10%.

A routable order arrives second. It is sent to whichever venue quotes the best price, by which time the news has usually been traded there, and its own volume pushes the price further past efficient. An order that refuses routing has nowhere else to go: it either rests on the book waiting or goes straight to one venue, and it meets the informed flow when it arrives. Those orders are also the ones that trade successfully on new information, which points to the high-speed informed traders as their users.

---

Flashcards for this section are as follows:

- what a negative weighted price contribution records ::@:: That the order type pushed the price further away from the efficient price.
- total contribution of the non-routable types against the routable ones ::@:: 115.43% against -15.43%.
- share of taking volume and of contribution carried by the intermarket sweep ::@:: 35.69% of the volume and 90.32% of the contribution.
- largest negative contribution in the table ::@:: The day limit order, at -13.78% on 16.37% of the taking volume.
- which traders the evidence points to as the users of the non-routable orders ::@:: High-speed informed traders, who trade successfully on new information.
