---
aliases:
  - P-peg
  - midpoint peg
  - pegged order
  - primary peg
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/pegged_order
  - language/in/English
---

# pegged order

A _pegged order_ adjusts its limit price dynamically according to a reference point on the order book. The two main types are primary peg and midpoint peg.

Pegged orders are price qualifiers: instructions that control the execution price beyond the basic limit/market distinction. Exchanges differ in which types they offer.

---

Flashcards for this section are as follows:

- what a pegged order does ::@:: Adjusts its limit price dynamically according to a reference point on the order book.
- two main types ::@:: Primary peg and midpoint peg.

## primary peg

A _primary peg (P-peg)_ limit buy sets its bid one tick below the national best bid; a P-peg limit sell sets its ask one tick above the national best offer. The reference is the national quote, not the venue's own quote. So a P-peg buy rests at a price worse than the best bid available anywhere, and a P-peg sell at a price worse than the best offer available anywhere. P-peg orders are hidden (not displayed on the LOB), which gives them lower execution priority than displayed orders at the same price.

The order then trades up to the national best. A P-peg buy executes at or below the national best bid, and a P-peg sell at or above the national best offer, never at a price worse than the best available on its own side. A counterorder aggressive enough to reach the national best therefore fills the order at the national best price rather than at its own worse resting price, and one that falls short does not trade with it at all.

A tick is the minimum unit of the price grid, e.g., \$0.01. Suppose the national best offer is \$10.04. A P-peg limit sell for 100 shares rests at \$10.05, one tick above the national best offer, and is not displayed. A limit buy for 100 shares at \$10.05 arrives: the arriving price equals the P-peg sell's own resting price, so the two match on equality. A limit buy at \$10.04 is at the national best offer, so the pegged sell steps down from \$10.05 to execute there. A limit buy at \$10.03 is worse than the national best offer and does not trade with the pegged order at all. If the national best offer moves to \$10.03, the resting price moves to \$10.04.

---

Flashcards for this section are as follows:

- how a P-peg limit buy sets its price ::@:: One tick below the national best bid.
- how a P-peg limit sell sets its price ::@:: One tick above the national best offer.
- what quote a P-peg order pegs to ::@:: The national quote, not the venue's own quote.
- how a P-peg resting price compares with the best price available on the same side ::@:: One tick worse: a buy rests below the national best bid, a sell above the national best offer.
- how a midpoint peg's resting price compares with the two national quotes ::@:: Strictly between them, better than the national best bid for a seller and better than the national best offer for a buyer.
- whether P-peg orders are displayed ::@:: No; they are hidden with lower priority than displayed orders at the same price.
- at what prices a P-peg order will execute ::@:: No worse than the national best on its own side: at or below the NBB for a buy, at or above the NBO for a sell.
- what happens when a counterorder is aggressive enough to reach the national best but not the resting price ::@:: The pegged order executes, at the national best price rather than its own worse resting price.
- what happens when a counterorder falls short of the national best ::@:: It does not trade with the pegged order at all.
- what happens when an arriving order's price equals the pegged order's resting price ::@:: They match and trade at that price, even though the pegged order is hidden.

## midpoint peg

A _midpoint peg_ sets its limit price at the midpoint of the NBBO, which falls strictly between the two national quotes: a better price than the national best bid for a seller, and a better price than the national best offer for a buyer. It faces the same display and priority rules as a P-peg, and never executes at a price worse than the midpoint. When the national best bid equals the national best ask, the midpoint is that same price, so a midpoint peg rests at the locked quote.

---

Flashcards for this section are as follows:

- how a midpoint peg sets its price ::@:: At the midpoint of the NBBO.
- advantage of midpoint peg over primary peg ::@:: Price improvement by trading at the midpoint.
- what a midpoint peg does when the NBBO bid equals the NBBO ask ::@:: The midpoint is that same price, so the order rests at the locked quote.
