---
aliases:
  - circuit breaker
  - trading curb
  - volatility interruption
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/trading_curb
  - language/in/English
---

# trading curb

A _trading curb_, also called a circuit breaker, halts trading when the market becomes extremely volatile, whether the volatility comes from significant news or from a severe order imbalance.

---

Flashcards for this section are as follows:

- overview ::@:: A halt in trading when the market becomes extremely volatile, whether from significant news or from a severe order imbalance.
- second name for a trading curb ::@:: A circuit breaker.

## halting and reopening

An exchange publishes the details of an interruption before trading resumes: the reopening time, the indicative price, and the order imbalance. It then runs an auction that sets the price at which normal trading resumes.

---

Flashcards for this section are as follows:

- what is published before a halted market reopens ::@:: The reopening time, the indicative price, and the order imbalance.
- sequence from a halt to normal trading ::@:: The reopening time and indicative information are published, an auction runs, and then normal trading reopens.

## effects of halts

Whether a halt helps is contested. Chen et al. (2024, Journal of Finance), "The Dark Side of Circuit Breakers", finds that a trading halt makes the market more volatile and more fragile.

Trading collapses during the halt and rebounds past its usual level immediately afterwards. Average trades per share per minute on the London Stock Exchange fall to nearly zero for hybrid investment banks, high-frequency traders, and other algorithmic firms alike while the halt's call auction runs, and every group then spikes above its pre-halt peak: hybrid investment banks from about 85 to about 133, high-frequency traders from about 29 to about 34, and other algorithmic firms from about 4 to about 13. Hybrid investment banks trade more than the high-frequency traders, who trade more than the other algorithmic firms, at every point around the halt, and each series decays back towards its baseline over the following hour.

Volatility behaves the same way. Plotted on a logarithmic scale it climbs into the halt, collapses to near zero through the call auction, and then spikes to about 0.0053 on the London Stock Exchange and 0.0031 on multilateral trading facilities before decaying.

---

Flashcards for this section are as follows:

- finding of Chen et al. (2024, Journal of Finance), "The Dark Side of Circuit Breakers" ::@:: A trading halt makes the market more volatile and more fragile.
- what happens to trading while a halt's call auction runs ::@:: Average trades per share per minute fall to nearly zero for hybrid investment banks, high-frequency traders, and other algorithmic firms alike.
- hybrid investment bank trading around a halt ::@:: About 85 trades per share per minute before the halt, nearly zero through the call auction, and about 133 just after it.
- high-frequency trading around a halt ::@:: About 29 trades per share per minute before the halt, nearly zero through the call auction, and about 34 just after it.
- other algorithmic trading around a halt ::@:: About 4 trades per share per minute before the halt, nearly zero through the call auction, and about 13 just after it.
- ranking of the three groups by trades per share per minute ::@:: Hybrid investment banks first, high-frequency traders second, other algorithmic firms last, at every point around the halt.
- what volatility does around a halt ::@:: It climbs into the halt, collapses to near zero through the call auction, spikes to about 0.0053 on the London Stock Exchange and 0.0031 on multilateral trading facilities just after it, then decays.
