---
aliases:
  - batch trading
  - continuous limit-order market
  - continuous market
  - continuous trading
  - discrete trading
  - frequent batch auction
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/continuous_trading
  - language/in/English
---

# continuous trading

In a _continuous market_ each incoming order is handled when it arrives, so an order that arrives at a moment is dealt with at that moment, up to latency, instead of waiting for a batch. The alternative is discrete trading, which collects orders over an interval and executes them together. Continuous trading is the mechanism that runs on the limit-order book of most modern exchanges.

---

Flashcards for this section are as follows:

- overview ::@:: Handling each incoming order at the moment it arrives, up to latency, instead of collecting orders into a batch.
- what the alternative to continuous trading does ::@:: Discrete trading collects orders over an interval and executes them together.

## price-time priority

Continuous trading runs on the limit-order book under price-time priority: orders with better prices are executed first, and among orders offering the same price the first to arrive is served first. The trades the market produces are still discrete in the data, because they are recorded one at a time even though orders are accepted continuously.

---

Flashcards for this section are as follows:

- two components of price-time priority ::@:: Orders with better prices are executed first, and among orders at the same price the first to arrive is served first.
- when trades happen in a continuous market ::@:: In discrete steps in the data, even though orders are accepted continuously.

## discrete trading

A discrete market, also called batch trading or periodic trading, collects orders over a certain time interval and executes them as a batch. Opening auctions and trading on a blockchain are examples. A batch runs in stages: orders are submitted during a submission stage, the auction runs at the end of it, and the results are broadcast before the submission stage for the next batch begins.

---

Flashcards for this section are as follows:

- discrete market ::@:: A market that collects orders over a time interval and executes them as a batch; also called batch trading or periodic trading.
- two examples of discrete trading ::@:: Opening auctions, and trading on a blockchain.
- how a batch runs ::@:: Orders are submitted during a submission stage, the auction runs at the end of it, and the results are broadcast before the next submission stage begins.

### frequent batch auction

A frequent batch auction collects orders over a short interval and executes them as a batch, and it has been proposed as a solution to the arms race in high-frequency trading (Budish et al., 2015, QJE). Whether it works, and whether any market has implemented one, are open questions.

---

Flashcards for this section are as follows:

- frequent batch auction ::@:: A batch of orders collected over a short interval and executed together.
- what a frequent batch auction was proposed to address ::@:: The arms race in high-frequency trading (Budish et al., 2015, Quarterly Journal of Economics).
- what remains open about frequent batch auctions ::@:: Whether they work, and whether any market has implemented one.

## advantages and drawbacks

The case for continuous trading rests on price efficiency, because the market reflects new information promptly, and on liquidity, because market makers provide it continuously and investors can fill a trading need immediately; its effect on the bid-ask spread is ambiguous. The case against continuous trading is that it adds speed as a dimension on which information can be acquired: how fast information is acquired, processed, and reacted to becomes worth investing in, which drives the arms race in high-frequency trading and the phantom liquidity that comes with it. Two rivals receive the same news at the same time, and the one that can trade on it faster wins, so the link between Chicago and New York keeps being rebuilt to shave milliseconds. The fiber route built in 2010 to shave three milliseconds off the trip is estimated to have cost 300 million dollars. Spending of that kind is special-purpose investment, and it can be wasteful.

---

Flashcards for this section are as follows:

- argument for continuous trading from price efficiency ::@:: The market reflects new information promptly.
- argument for continuous trading from liquidity ::@:: Market makers provide liquidity continuously and investors can fill a trading need immediately.
- effect of continuous trading on the bid-ask spread ::@:: Ambiguous.
- central drawback of continuous trading ::@:: Speed becomes a further dimension on which information can be acquired, so the speed of acquiring, processing, and reacting to information becomes worth investing in.
- two consequences of that drawback ::@:: The arms race in high-frequency trading and phantom liquidity.
- what decides the winner when two rivals receive the same news at the same time ::@:: Whoever can trade on it faster.
- why the link between Chicago and New York keeps being rebuilt ::@:: To shave milliseconds, because being faster decides who trades.
- why spending on speed can be wasteful ::@:: It is special-purpose investment.
