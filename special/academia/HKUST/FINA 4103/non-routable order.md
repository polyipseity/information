---
aliases:
  - non-routable order
  - non-routable orders
  - order routing
  - routing refusal
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/non-routable_order
  - language/in/English
---

# non-routable order

A _non-routable order_ is one that refuses the routing [Regulation NMS](Regulation%20NMS.md) requires. It comes in two types, an [intermarket sweep order](intermarket%20sweep%20order.md) and a [do-not-ship order](do-not-ship%20order.md), each in an immediate-or-cancel or a limit form. Either type accepts that the best price may be somewhere else.

Li, Ye, and Zheng (2022, _Journal of Financial Economics_) work from proprietary trade-by-trade order-type data on the New York Stock Exchange. They find that 57% of the orders in their sample refused the routing stipulated by Reg NMS. The reason is not obvious from the rulebook.

---

Flashcards for this section are as follows:

- overview ::@:: An order that refuses the routing Regulation NMS requires, accepting that the best price may be elsewhere.
- two order types that are non-routable ::@:: The intermarket sweep order and the do-not-ship order.
- share of orders in the sample that refused the routing stipulated by Reg NMS ::@:: 57%.
- data the finding rests on ::@:: Proprietary trade-by-trade order-type data from the New York Stock Exchange.

## how an order is classified

The study sorts every order along four factors.

1. Price qualifier: a limit price, a stop price, or no price condition.
2. Time in force: immediate-or-cancel, day, or good-till-cancel.
3. Routing decision: a do-not-ship instruction, an intermarket sweep, or no routing instruction.
4. Display decision: a hidden percentage, or no display instruction.

The first and fourth are the classes already described in [order (exchange)](order%20(exchange).md) and [hidden order](hidden%20order.md). The third produces the non-routable types, in the two cells that carry an instruction.

---

Flashcards for this section are as follows:

- four factors along which the study classifies every order ::@:: Price qualifier, time in force, routing decision, and display decision.
- values the price qualifier takes ::@:: A limit price, a stop price, or no price condition.
- values the time in force takes ::@:: Immediate-or-cancel, day, or good-till-cancel.
- values the routing decision takes ::@:: A do-not-ship instruction, an intermarket sweep, or no routing instruction.
- values the display decision takes ::@:: A hidden percentage, or no display instruction.

## order size

The table covers the six order types that make up most New York Stock Exchange volume. Two columns measure size: how many trades each type produced, and the average order size in shares. Fill rate is the share of each order that executed. The last three columns split those executions three ways: the percentage taken from the local book, the percentage routed to another exchange, and the percentage that provided liquidity instead of consuming it.

The routing instruction shows up in the route column. The three non-routable types all read 0.00%: the intermarket sweep, the DNS immediate-or-cancel order, and the DNS limit order never leave the venue. The plain market order routes a third of its executions, and the day limit order 14.28%.

The two limit orders sit at opposite ends of the maker-taker balance. The DNS limit order takes 11.43% of its executions and provides 88.57%, so it overwhelmingly supplies liquidity. The day limit order is mixed: 55.94% provided, 29.78% taken locally, and 14.28% routed.

The most-traded type is the DNS limit order at 44,243,300 trades, just ahead of the day limit order at 43,360,100. Both send small orders, 182.38 and 220.50 shares on average, the two lowest figures in the table. The large average sizes belong to the types that take liquidity and expect to fill at once, the DNS immediate-or-cancel order at 307.09 being the largest of the six.

| Order type | Trades | Average order size | Fill rate | Take local liquidity | Route | Make liquidity |
| --- | --- | --- | --- | --- | --- | --- |
| Plain market | 6,364,008 | 278.96 | 100.00% | 66.34% | 33.64% | 0.00% |
| Plain IOC | 4,196,808 | 268.63 | 19.48% | 98.07% | 1.93% | 0.00% |
| ISO | 25,410,600 | 244.30 | 22.48% | 100.00% | 0.00% | 0.00% |
| DNS IOC | 14,652,500 | 307.09 | 31.86% | 100.00% | 0.00% | 0.00% |
| DAY limit | 43,360,100 | 220.50 | 2.71% | 29.78% | 14.28% | 55.94% |
| DNS limit | 44,243,300 | 182.38 | 3.72% | 11.43% | 0.00% | 88.57% |

---

Flashcards for this section are as follows:

- route column of the three non-routable order types ::@:: 0.00% for all three: the intermarket sweep, the DNS immediate-or-cancel order, and the DNS limit order.
- how the DNS limit order splits its executions against the day limit order ::@:: DNS limit provides 88.57% and takes 11.43%; day limit is mixed at 55.94% provided, 29.78% taken, and 14.28% routed.
- which order type trades most, and its average size ::@:: The DNS limit order, at 44,243,300 trades and 182.38 shares per order.
- where the largest average order sizes sit ::@:: With the types that take liquidity and expect to fill at once, the DNS immediate-or-cancel order at 307.09 shares being the largest.

## who uses them

A do-not-ship order is not faster than a plain order in itself, so the question is who chooses to send one. High-frequency traders are the ones suspected of choosing them.

An intermarket sweep order demands a fast connection to every exchange, because the broker has to see them all to split the order. A do-not-ship order demands nothing comparable, and the compliance requirements differ between the two types.

What these orders contribute to the price is a separate question, and the evidence for it is in [price discovery](price%20discovery.md).

---

Flashcards for this section are as follows:

- why the question is who chooses to send one ::@:: A do-not-ship order is not faster than a plain order in itself.
- traders suspected of choosing these orders ::@:: High-frequency traders.
- what using an intermarket sweep order demands of its user ::@:: A fast connection to every exchange, because the broker has to see them all to split the order.
- what a do-not-ship order demands of its user ::@:: No comparable requirement, where an intermarket sweep needs a fast connection to every exchange.
