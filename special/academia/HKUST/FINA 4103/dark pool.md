---
aliases:
  - alternative trading system
  - crossing network
  - dark pool
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/dark_pool
  - language/in/English
---

# dark pool

A _dark pool_ is an alternative trading system (ATS) where all orders are completely hidden. Trades execute at the midpoint of the NBBO: if the NBO is 101 dollars and the NBB is 99 dollars, dark pool trades execute at 100 dollars.

Dark pools offer better prices than lit exchanges, but regulators worry about their volume share and effect on price discovery.

---

Flashcards for this section are as follows:

- what a dark pool is ::@:: An alternative trading system where all orders are hidden.
- at what price dark pool trades execute ::@:: The midpoint of the NBBO.
- regulatory concern about dark pools ::@:: Their volume share and potential harm to price discovery.

## dark pools and price efficiency

Zhu (2014, _Review of Financial Studies_) compares two worlds: a lit exchange with a dark pool, and a lit exchange alone. Informed traders learn the asset value and trade on it, contributing to price discovery. Noise traders buy and sell at random, driven by exogenous needs.

The asset value is either high ($v_H$) or low ($v_L$) and is not publicly observable. With a dark pool alongside the lit exchange, informativeness rises and the mean-squared error of the price relative to the true value falls.

---

Flashcards for this section are as follows:

- two worlds Zhu (2014) compares ::@:: A lit exchange with a dark pool, and a lit exchange alone.
- what informed traders do in Zhu's model ::@:: Learn the asset value and trade on it, contributing to price discovery.
- what noise traders do in Zhu's model ::@:: Buy and sell at random, driven by exogenous needs.
- two effects of dark pools on price efficiency ::@:: Price informativeness rises and mean-squared error of price relative to true value falls.

## price improvement versus execution risk

Dark pools execute on a pro-rata basis (a crossing network). Each trader buys or sells one unit. The probability of execution for a buyer is $P = \min\!\left(1, \frac{n_s}{n_b}\right)$, where $n_s$ is the number of sellers and $n_b$ the number of buyers.

Informed traders face high execution risk: good news clusters them on the buy side, so they are more likely to be rationed. Noise traders, randomly distributed, face roughly equal probability.

This asymmetry drives informed traders to lit exchanges, which carry no execution risk, and noise traders to dark pools, which offer price improvement. The result assumes a single informed trader; a monopolistic informed trader may act differently.

---

Flashcards for this section are as follows:

- <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->how dark pools execute orders ::@:: On a pro-rata basis: each buyer's execution probability is $P = \min\!\left(1, \frac{n_s}{n_b}\right)$, where $n_s$ is the number of sellers and $n_b$ the number of buyers.
- why informed traders face higher execution risk in dark pools ::@:: Good news clusters them on the buy side, making rationing more likely.
- why noise traders face lower execution risk ::@:: They are randomly distributed, so execution probability is near 0.5.
- how dark pools affect the lit exchange ::@:: Informed traders migrate there, making its prices more informative.
