---
aliases:
  - buy order
  - market order
  - sell order
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/market_order
  - language/in/English
---

# market order

A _market order_ is an order to buy or sell a security immediately at the best available price. It does not specify a price: the trader takes whatever the market offers. A market buy sweeps the ask side of the book; a market sell sweeps the bid side. Market orders are limit orders with ask = $-\infty$ and bid = $+\infty$.

A market buy for 150 shares, against a book with 100 at $50.00 and 50 at $50.01, fills 100 at the best ask and 50 at the next level, for a weighted-average execution price.

---

Flashcards for this section are as follows:

- what a market order specifies ::@:: The trading direction and quantity, but not the price. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->how a market order compares to a limit order ::@:: It is a limit order with ask = $-\infty$ and bid = $+\infty$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- what a market buy order does to the book ::@:: Sweeps the ask side, taking the best available asks until the quantity is filled. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- what a market sell order does to the book ::@:: Sweeps the bid side, taking the best available bids until the quantity is filled. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- how the execution price of a multi-level sweep is set ::@:: As a weighted average of the levels it swept. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## liquidity taking

A market order takes liquidity, consuming the standing limit orders on the other side of the book. It suits price-insensitive but impatient traders. A marketable limit order is the alternative when the trader still wants a price bound.

---

Flashcards for this section are as follows:

- what liquidity market orders take ::@:: They consume standing limit orders on the other side of the book. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- who market orders suit ::@:: Price-insensitive but impatient traders who need to execute immediately. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- what alternative a trader has when a price bound is still wanted ::@:: A marketable limit order. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## execution price

Market orders tend to execute at worse prices since the trader has no control. The order sweeps through multiple levels, so a large order can fill far worse than the quoted best price.

---

Flashcards for this section are as follows:

- what the cost of immediacy consists of ::@:: The spread plus price impact. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- what price impact is ::@:: The extra cost of sweeping past the best quote into worse ones. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- when a market order's execution price is far worse than the quoted best price ::@:: When the order is large relative to the resting quantity. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
