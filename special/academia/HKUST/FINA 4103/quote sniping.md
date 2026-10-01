---
aliases:
  - quote sniping
  - sniping
  - sniping race
  - stale quote
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/quote_sniping
  - language/in/English
---

# quote sniping

A _sniping_ race is a race to take a resting limit order whose price has gone stale. The winner is settled before the owner of that order manages to cancel it. Once the market has moved away from a resting price, that price is free money for whoever arrives first. The race is decided on latency rather than on price.

The buyer and the seller each have a way to avoid losing. A non-routable order does not announce its arrival, so the other side is not warned. The buyer sends one to reach a stale price before the seller can cancel it. The seller sends one to cancel a stale price before a buyer can take it.

---

Flashcards for this section are as follows:

- overview ::@:: A race to take a resting limit order whose price has gone stale, before its owner cancels it.
- what decides a sniping race ::@:: Latency rather than price.
- how a buyer and a seller each avoid losing the race ::@:: Both send a non-routable order, which does not announce its arrival.

## who wins the race

Li, Ye, and Zheng (2022, _Journal of Financial Economics_) count the races between the three immediate-or-cancel types on the New York Stock Exchange. Rows are the winners and columns the losers. Where $q > 1$ orders win or lose the same race, each is counted as $1/q$ of it. Every number is averaged at the stock-day level.

| Winner | Loses to plain IOC | Loses to ISO | Loses to DNS IOC | Total wins | Winning rate |
| --- | --- | --- | --- | --- | --- |
| Plain IOC | 5.96 | 4.47 | 2.99 | 13.42 | 5.46% |
| ISO | 7.03 | 86.35 | 47.33 | 140.71 | 57.26% |
| DNS IOC | 4.38 | 43.69 | 43.56 | 91.63 | 37.28% |
| Total losses | 17.37 | 134.51 | 93.88 | 244.76 | |

A routed order announces its arrival, and the other side races against that announcement.

---

Flashcards for this section are as follows:

- winning rates of the three immediate-or-cancel types, plain, intermarket sweep, and do-not-ship ::@:: 5.46%, 57.26%, and 37.28% respectively.
- when $q > 1$ orders win or lose the same race, what is each order counted as ::@:: $1/q$ of the race, with the numbers averaged at the stock-day level.
- why a routed order is exposed in the race ::@:: Its arrival is announced, and the other side races against that announcement.

## escaping the race

A seller whose quotes rest on the book faces two races. One is how quickly a stale quote can be cancelled. The other is who can reach the front of the queue at that price first. The non-routable limit order wins both, against the routable one.

The cancellation race decides whether a stale quote survives. A DNS limit order manages to cancel 42% of the time in sniping events, while a routable limit order rarely escapes at all. The queue race is described in [limit order](limit%20order.md). The speed that gives these races their edge is described in [high-frequency trading](high-frequency%20trading.md).

---

Flashcards for this section are as follows:

- two races a seller with resting quotes faces ::@:: Cancelling a stale quote quickly, and reaching the front of the queue at that price first.
- how often a DNS limit order cancels in time in a sniping event ::@:: 42% of the time.
- how often a routable limit order escapes a sniping event ::@:: Rarely.
- which order type wins the two maker-side races ::@:: The non-routable limit order, against the routable one.
