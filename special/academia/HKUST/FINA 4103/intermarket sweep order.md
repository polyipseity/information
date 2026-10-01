---
aliases:
  - ISO
  - intermarket sweep order
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/intermarket_sweep_order
  - language/in/English
---

# intermarket sweep order

An _intermarket sweep order_ (ISO) reaches several exchanges at once and must execute against the best available quote. It is exempt from the [order protection rule](trade%20through.md). Traders pair it with the immediate-or-cancel instruction most of the time, though a day ISO also exists.

The exemption rides on the order type. A venue receiving an ISO matches it against its own book like any other order. It does nothing further with it: no check of the other exchanges, no routing of the remainder. An ordinary marketable order is granted neither. It arrives, and the venue's router starts looking for liquidity it does not have.

Whoever sends the order pays for that exemption, and the price is a connection and a quote feed to every venue in the sweep. That is what lets the sender merge the books and settle the split before anything is released. A [do-not-ship order](do-not-ship%20order.md) discharges the same obligation from the other side, by switching the venue's router off.

Both types are exempt from the same duty and neither guarantees the market's best price. What separates them is whether the order goes to one venue with the rest refused, or to every venue at once.

---

Flashcards for this section are as follows:

- overview ::@:: An order released to several exchanges at once, which must execute against the best available quote and is exempt from the order protection rule.
- what a venue does on receiving an ISO ::@:: It matches it against its own book, with no intermarket check and no routing of the remainder.
- instruction an ISO is typically used with ::@:: Immediate-or-cancel; a day ISO also exists.
- what an ISO demands of whoever sends it ::@:: A connection and a quote feed to every venue in the sweep, before anything is released.
- how a sweep and a do-not-ship instruction differ ::@:: One is placed on every venue at once, the other on one venue with the rest refused.

## how a sweep is split

A broker that receives an order to buy 1000 shares merges the quote feeds into one book. The sweep has to consume the best prices available, so the broker walks that merged book from the top down until the order is filled. What the walk leaves behind is three child orders, one per venue, released in the same instant. Each child carries the immediate-or-cancel instruction, so a leg that fails to fill dies on that venue instead of resting there.

| Venue | Offers (dollars) |
| --- | --- |
| A | 100 at 99, 100 at 100, 300 at 101 |
| B | 500 at 99, 300 at 100, 200 at 101 |
| C | 300 at 99, 100 at 98, 300 at 100, 400 at 101 |

The best offer anywhere is 99 dollars, and 900 shares are on offer at that price across the three venues. The remaining 100 come from the 100 shares C offers at 98 dollars. The broker releases 100 shares to A, 500 to B, and 400 to C.

---

Flashcards for this section are as follows:

- how a broker turns one order into a sweep ::@:: It merges the quote feeds and walks the merged book from the best price down, releasing one child order per venue in the same instant.
- rule that governs the walk ::@:: It must consume the best prices available.
- what becomes of a leg of a sweep that does not fill ::@:: It is cancelled on that venue, because every child order carries the immediate-or-cancel instruction.
- shares on offer at 99 dollars across the three venues in the worked example ::@:: 900, being 100 at A, 500 at B, and 300 at C.
- where the last 100 shares of a 1000-share sweep come from ::@:: The 100 shares C offers at 98 dollars.
- split a broker releases for a 1000-share sweep in the worked example ::@:: 100 shares to A, 500 to B, and 400 to C.

## who carries the obligation

Under a routed order the exchange is answerable for the best price. It checks the other venues before it acts, and the check costs time. Under a sweep the broker is answerable, and the broker has already made that check by the time anything is released. The ISO has to consume the best price as it stood when the order was placed.

The exemption moves the exposure rather than removing it. Between the broker's snapshot of the books and the arrival of the child orders, the market can move, and no venue is obliged to notice. A routed order has the same gap, with the exchange answerable across it instead of the broker. What the sweep saves is the exchange-side check and the routing leg, and what it costs is a connection to every venue in it.

A broker-dealer normally has discretion over how it splits, as long as the split keeps the trading cost and the delay down.

---

Flashcards for this section are as follows:

- who is answerable for the best price when an ISO is used ::@:: The broker, not the exchange.
- what an ISO must consume ::@:: The best price, as it stood at the time the order was placed.
- when the sweep's best-price obligation is discharged ::@:: Before anything is released, since the broker has already made the check by then.
- what the exchanges need not do with an ISO ::@:: Check intermarket prices, or route it to another exchange.
- where the time is saved by a sweep ::@:: In the exchange-side check and the intermarket routing that a routed order needs.
- discretion a broker-dealer has over the split ::@:: How to divide the order, provided trading cost and delay are kept down.

## information leakage

A sweep is meant to execute a large block across several exchanges without leaking information or acting on stale prices. The leak comes from the routing path it is meant to avoid. A plain market order sent to exchange A reaches B and C as the routing works its way through them, and every execution prints. A rival reading those prints can infer that a large order is working through the market and that a remainder is still to come.

The prints carry the timing as well as the size. In the worked case, executions appear at A at 10:00:02 and at B at 10:00:03. A rival that reads them reaches C before the last leg arrives, at 10:00:06, and takes the fill it was going to get. That tactic is [front running](high-frequency%20trading.md). A [do-not-ship order](do-not-ship%20order.md) avoids the leak by never producing a route for a rival to read.

---

Flashcards for this section are as follows:

- problems a sweep is meant to solve ::@:: Information leakage and stale prices, when executing a large block across several exchanges.
- where the information leak on a routed order comes from ::@:: The pattern of executions as the order is routed from exchange to exchange.
- what a rival infers from that pattern ::@:: That a large order is working through the market and that a remainder is still to come.
- what a rival does with the inference ::@:: Trades ahead of the remainder.
- times in the worked front-running case ::@:: Executions at A at 10:00:02 and at B at 10:00:03, and the rival reaches C before 10:00:06.

## observed order sizes

An ISO is meant to help a large block execute across exchanges. The sizes recorded in the order-type data of Li, Ye, and Zheng (2022) are not large. The average ISO is 244 shares, against 268 for a plain immediate-or-cancel order and 278 for a plain market order. The main reasons for using one are probably not the ones it was designed for.

---

Flashcards for this section are as follows:

- average sizes of an intermarket sweep order, a plain immediate-or-cancel order, and a plain market order ::@:: 244 shares, 268 shares, and 278 shares respectively.
- comparison of the observed intermarket sweep order sizes with what the instrument was designed for ::@:: The sizes are not large, so the reasons for using one are probably not the ones it was designed for.
