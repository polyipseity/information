---
aliases:
  - BBO
  - NBBO
  - bid-ask
  - bid-ask spread
  - crossed market
  - far side
  - locked market
  - mid price
  - mid-point quote
  - near side
  - spread
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/bid-ask_spread
  - language/in/English
---

# bid-ask spread

The _bid-ask spread_ is the difference between the best ask and the best bid on the limit-order book, and a trader pays it on a round trip: buy then sell, or sell then buy, of one unit. A small spread means a liquid market. How the spread is set, and what impact it has on trading behaviour, are questions for the second half of the course.

Several prices are quoted for the same asset at once. A stock ticker tape usually shows the last execution price, the middle of the limit-order book gives the mid-point quote, and the BBO gives the best bid and the best ask. When someone says "AAPL is now 100 dollars", they usually mean the last trade, not the current BBO.

---

Flashcards for this section are as follows:

- definition of the bid-ask spread ::@:: The difference between the best ask and the best bid on the limit-order book.
- what the spread costs a round-trip trader ::@:: Buying then selling one unit, or selling then buying it.
- what the spread measures ::@:: Market liquidity: small means liquid, large means illiquid.

## best bid and offer

The _best bid_ is the highest bid in the standing limit orders, and the _best ask_ (or offer) is the lowest ask. Together they form the _Best Bid and Offer (BBO)_. Aggregated across all markets, they form the _National Best Bid and Offer (NBBO)_.

---

Flashcards for this section are as follows:

- what the best bid is ::@:: The highest bid in the standing limit orders.
- what the best ask is ::@:: The lowest ask in the standing limit orders.
- what NBBO stands for ::@:: National Best Bid and Offer: the aggregate BBO across all markets.

## mid-point quote

The _mid-point quote_ (mid price) is the average of the best ask and the best bid. It is typically used as a "fair" price of the asset. Across several exchanges the reference is the NBBO rather than a single venue's quote.

---

Flashcards for this section are as follows:

- formula for the mid-point quote ::@:: The average of the best ask and the best bid.
- what the mid-point quote represents ::@:: A "fair" price of the asset.
- what the mid-point quote is in a multi-exchange market ::@:: The midpoint of the NBBO, not of a single venue's quote.

## near side and far side

When a trader buys, the best bid is the _near side_ of the spread (the side the trader is on) and the best ask is the _far side_. When a trader sells, the best ask is the near side and the best bid is the far side.

---

Flashcards for this section are as follows:

- near side for a buyer ::@:: The best bid.
- far side for a buyer ::@:: The best ask.
- near side for a seller ::@:: The best ask.
- far side for a seller ::@:: The best bid.

## locked and crossed markets

A market is _locked_ when the best bid equals the best ask, and _crossed_ when the best bid exceeds the best ask. In a single-exchange environment these states do not arise, but they are relevant in multi-exchange markets and in LOB data.

Across exchanges the states are prohibited rather than merely possible. Rule 610 of [Regulation NMS](Regulation%20NMS.md), the access rule, forbids a venue from accepting an order that would lock or cross the market on another venue. It requires the venue to route such an order to the exchange holding that price instead. The prohibition does not reach hidden quotes.

The two rules divide by order type. Rule 611, the [order protection rule](trade%20through.md), covers marketable orders, the ones that execute. Rule 610 covers liquidity-provision orders, the ones that rest. A resting order at a price another venue is already quoting does not trade, so it cannot violate the price protection, but it can freeze the book.

---

Flashcards for this section are as follows:

- when a market is locked ::@:: When the best bid equals the best ask.
- when a market is crossed ::@:: When the best bid exceeds the best ask.
- whether locked or crossed markets exist in a single-exchange environment ::@:: No; they are relevant only in multi-exchange markets and in LOB data.
- which rule forbids a locked or crossed market across exchanges ::@:: Rule 610, the access rule.
- what a venue must do with a limit order that would lock or cross another venue's market ::@:: Route it to the venue holding that price.
- whether the prohibition reaches hidden quotes ::@:: No.
- which order type each rule protects ::@:: Rule 611 the marketable orders that execute, and Rule 610 the liquidity-provision orders that rest.
