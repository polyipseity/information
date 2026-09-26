---
aliases:
  - ask order
  - bid order
  - limit buy
  - limit order
  - limit sell
  - marketable limit order
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/limit_order
  - language/in/English
---

# limit order

A _limit order_ is an order to buy or sell a security at a specified price or better. A buy limit order sets the most a buyer will pay (the bid price); a sell limit order sets the least a seller will accept (the ask price). A limit order is a commitment to trade that may never find a counterparty; it stays unfilled until the market reaches its price.

Starting from an empty book, a limit sell for 100 shares at $100 places 100 shares on the ask side. A limit buy for 50 shares at $99 places 50 shares on the bid side. A buy at $101 instead would cross the best ask and execute immediately.

---

Flashcards for this section are as follows:

- what a limit order specifies ::@:: The most a buyer will pay (buy limit) or the least a seller will accept (sell limit).
- what happens to an unfilled limit order ::@:: It stays on the book, waiting for a counterparty, and may never find one.
- who limit orders are for ::@:: Patient but price-sensitive traders who want to control execution price.
- what a limit buy at 101 dollars does against a best ask of 100 dollars ::@:: It crosses the spread and executes immediately.

## liquidity provision

Standing limit orders supply liquidity: they sit on the book and wait for incoming orders, and together they are the set of trading opportunities in the market.

---

Flashcards for this section are as follows:

- how limit orders relate to liquidity ::@:: They supply it: standing orders wait on the book for incoming orders.
- what the collection of limit orders is ::@:: The set of trading opportunities in the market.

### marketable limit orders

A _marketable limit order_ has a bid at or above the best ask, or an ask at or below the best bid, so it takes liquidity rather than providing it. Once fully executed it is indistinguishable from a market order, but ex ante the trader still names a price that a market order leaves open.

---

Flashcards for this section are as follows:

- what a marketable limit order is ::@:: A limit order with a bid at or above the best ask, or an ask at or below the best bid, so it takes liquidity.
- how a marketable limit order compares to a market order ::@:: Identical once fully executed, but the trader still names a price, so the unfilled part never executes beyond that bound.

## price-time priority

When multiple limit orders compete for execution, _price-time priority_ decides the order: better prices first, and among same-price orders, first come first served. Two competing limit sell orders of 100 shares: the one with the lower ask sits higher on the book, and if both quote the same price, arrival time breaks the tie. Enforcing such a rule is a severe problem for modern markets.

---

Flashcards for this section are as follows:

- what price-time priority means ::@:: Better prices execute first, and among same-price orders, first come first served.
- why a limit-order book needs a priority rule ::@:: To order competing executions.
- when price beats time in priority ::@:: A better price executes even if it arrived later.

## execution quality

Limit and market orders differ in two ways that push against each other: execution risk and execution price.

---

Flashcards for this section are as follows:

- two dimensions on which limit and market orders differ ::@:: Execution risk and execution price.

### execution risk

A limit order does not guarantee execution: the market may never reach the specified price, or the order may fill only partially. A market order executes immediately upon submission, so its trading need is almost always fulfilled.

---

Flashcards for this section are as follows:

- what execution risk a limit order carries ::@:: It may not fill at all, or may fill only partially.
- how a market order compares on execution risk ::@:: It executes immediately upon submission, so its need is almost always fulfilled.
- what a partial fill leaves behind ::@:: A smaller order still resting on the book.

### execution price

A market order is likely to execute at an inferior price, because it gives up price control. A limit order always trades at a price at least as good as the one it names.

---

Flashcards for this section are as follows:

- why a market order may execute at an inferior price ::@:: It gives up price control.
- how a limit order compares on execution price ::@:: It always trades at a price at least as good as the one it names.
