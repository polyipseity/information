---
aliases:
  - HFT
  - high-frequency trading
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/high-frequency_trading
  - language/in/English
---

# high-frequency trading

High-frequency trading is automated trading at speeds a human trader cannot match. Where the market is fragmented and trading is electronic, being the quickest decides who trades.

---

Flashcards for this section are as follows:

- what high-frequency trading is ::@:: Automated trading at speeds a human trader cannot match, made possible by electronic trading in a fragmented market.

## speed and latency

High-frequency traders operate at speeds of microseconds, millionths of a second, down to nanoseconds, billionths of a second. For scale, light travelling in a vacuum covers the distance from New York to Chicago in about 5 milliseconds. Fragmentation across venues, together with electronic trading, is what makes speed pay. A stock is quoted at many venues at once, so a quote that has gone stale at one venue can still be picked off at another until the rest of the market reacts, and the fastest firm gets there first.

---

Flashcards for this section are as follows:

- range of speeds at which high-frequency traders operate ::@:: From microseconds, millionths of a second, down to nanoseconds, billionths of a second.
- time light travelling in a vacuum takes from New York to Chicago ::@:: About 5 milliseconds.
- why speed is worth paying for ::@:: A stale quote at one venue can still be picked off at another while the rest of the market has not reacted to it.

## arms race and overinvestment

Because speed decides who wins, firms invest enormous sums in special-purpose technology and ever-faster connections, a scale of spending large enough to be called overinvestment. The race also leaves behind _phantom liquidity_: quotes that appear in the book and are gone before anyone can trade against them. Whether faster trading and execution is good for the market at all is an open question.

The race is visible in the route between Chicago and New York, where each generation of the link bought a fraction of a millisecond. The original cable, buried in the mid 1980s along the rail lines, ran about 1,000 miles and took 14.5 milliseconds. Spread Networks' buried fiber of August 2010 took a new right of way over 825 miles for 13.1 milliseconds. McKay Brothers and Tradeworx then left fiber for microwave, which is faster than photons in fiber, reaching 744 miles in 9 milliseconds in July 2012 and 731 miles in 8.5 milliseconds in the winter of 2012. For comparison, a photon needs roughly 5 milliseconds in a vacuum to cover the same ground.

---

Flashcards for this section are as follows:

- name for the heavy spending on speed ::@:: Overinvestment.
- what firms invest in to win the speed race ::@:: Special-purpose technology and ever-faster connections.
- phantom liquidity ::@:: Quotes that appear in the book and disappear before anyone can trade against them, produced by the race for speed.
- unresolved question about faster execution ::@:: Whether faster trading and execution is good for the market at all.
- what each generation of the Chicago to New York link bought ::@:: A fraction of a millisecond: 14.5 milliseconds by cable in the mid 1980s, 13.1 by fiber in 2010, then 9 and 8.5 by microwave in 2012.
- why microwave replaced fiber in the speed race ::@:: Microwaves travel faster than photons in fiber, so the signal arrives sooner.

## market manipulation

Speed also enables manipulation. _Spoofing_ works in three steps: the spoofer stacks the book in one direction with orders it does not intend to execute, takes that fake supply back out, and then sweeps the market with a large order on the other side. Real cases are large and long-running: in May 2024 the Commodity Futures Trading Commission (CFTC) fined J.P. Morgan Securities, a Fed primary dealer, 100 million dollars for failing to surveil potential spoofing and high-frequency trading for eight years (Pam Martens and Russ Martens, 28 May 2024).

A second pattern is _quote stuffing_: bursts of orders to buy and sell that are quickly cancelled. In Abbott Laboratories stock on the morning of 17 August, one second at 10:07:27 carried 11,557 orders (source: Nanex). Normal trading in the same stock runs at 38 orders per second on average, and a separate burst reached 10,704 orders in one second and 5,483 in the next, with all but 14 cancelled within one second.

A third pattern needs no manipulation of the book, and it is front running. A large order working through a fragmented market leaves a trail of prints, and a trader fast enough to read those prints can infer that the order is still to come and trade ahead of the remainder. It comes from the same speed the arms race rewards. The order types that exist to defeat it are the ones that refuse to be routed, described in [quote sniping](quote%20sniping.md).

---

Flashcards for this section are as follows:

- three steps of spoofing ::@:: Build up fake orders in one direction, cancel them, then sweep the market with a large order on the other side.
- relation between the spoofer's fake orders and its own trade ::@:: They sit on opposite sides: the stacked orders are placed in one direction, and the sweep goes the other way.
- why the spoofed orders are cancelled ::@:: They were never meant to execute.
- Commodity Futures Trading Commission (CFTC) fine on J.P. Morgan Securities for failing to surveil potential spoofing over eight years ::@:: 100 million dollars.
- what quote stuffing is ::@:: Bursts of orders to buy and sell that are quickly cancelled.
- orders carried by one second at the peak of the Abbott Laboratories burst ::@:: 11,557 orders, at 10:07:27.
- order rate at Abbott Laboratories in normal times against the burst ::@:: 38 orders per second on average, then 10,704 orders in one second and 5,483 in the next, with all but 14 cancelled within one second.
- what front running requires ::@:: A trail of prints left by a large order, and the speed to trade ahead of the remainder.
- which order types were designed to defeat front running ::@:: The ones that refuse to be routed.

## message data

To quantify high-frequency trading activity and its possible profits and costs, researchers read limit-order-book (LOB) datasets, available from exchange direct feeds and from consolidated datasets like Trades and Quotes (TAQ) and MIDAS. They carry a complete play-by-play of the books: every new limit order adding liquidity, every new market order taking liquidity, and every trade, with very precise millisecond timestamps. What they miss is every order that failed.

In a [sniping](quote%20sniping.md) race the trader who places an [immediate-or-cancel order](immediate-or-cancel%20order.md) (IOC) to take a stale quote may win the race and execute, or lose it and be cancelled. The owner of the stale quote may revoke it in time, or be too late to cancel. These failed orders are not recorded on LOB data, so when several traders race, conventional LOB data records the winners and not the losers.

Exchanges keep electronic records of these attempts. _Message data_ records every attempted order, time-stamped at the gateway, so the speed of arrival can be measured accurately. It is hard to obtain, at least for students and junior scholars. Researchers can request London Stock Exchange (LSE) data under Section 165 of the Financial Service and Markets Act. Including the failed messages significantly improves knowledge about high-frequency trading.

---

Flashcards for this section are as follows:

- what limit-order-book (LOB) datasets record ::@:: Every new limit order adding liquidity, every new market order taking liquidity, and every trade, with very precise millisecond timestamps.
- what conventional limit-order-book (LOB) data misses about a sniping race ::@:: The losers: an immediate-or-cancel (IOC) order that loses the race and is cancelled, and a stale quote whose cancellation arrives too late, leave no trace.
- what message data records ::@:: Every attempted order, time-stamped at the gateway, so the speed of arrival can be measured accurately.
- how researchers can request London Stock Exchange (LSE) message data ::@:: Under Section 165 of the Financial Service and Markets Act.
- research value of the failed messages in message data ::@:: Including them significantly improves knowledge about high-frequency trading.
