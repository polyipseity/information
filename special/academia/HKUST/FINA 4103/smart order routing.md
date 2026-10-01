---
aliases:
  - SOR
  - smart order router
  - smart order routing
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/smart_order_routing
  - language/in/English
---

# smart order routing

_Smart order routing_ (SOR) is the automated handling of an order across venues, looking at where the liquidity is and placing the order where it can be filled best. It is how the [order protection rule](trade%20through.md) is discharged, since the exchange that receives an order is the party obliged to find the better quote elsewhere.

It exists because a large order cannot be filled in one venue: even a modest block runs out of size at the best price, and the remainder has to go somewhere at a worse price, so the decision of how to divide it is worth automating.

---

Flashcards for this section are as follows:

- overview ::@:: The automated handling of an order across venues, placing it where it can be filled best.
- which rule a smart order router exists to discharge ::@:: The order protection rule, Rule 611.
- why a large order needs routing at all ::@:: It runs out of size at the best price, and the remainder must go somewhere at a worse price.

## how a routed order is split

Once an order has to be spread over several venues, the routing algorithm decides how much goes where. Three patterns are used, and a pro-rata allocation is the most popular of them: it sends a share of the order to each venue in proportion to the liquidity each one shows. A time-priority rule sends the whole remainder to one venue at a time, in the order the venues are ranked. A round robin sends it to each venue in turn.

---

Flashcards for this section are as follows:

- what a routing algorithm has to decide once an order spans several venues ::@:: How much of the order goes to each venue.
- most popular way a routing algorithm splits an order ::@:: Pro-rata allocation, sending a share to each venue in proportion to the liquidity it shows.
- two other routing patterns ::@:: A time-priority rule that fills one venue at a time in rank order, and a round robin that takes the venues in turn.

## routing latency

An exchange's router can be slower than a broker's own technology. A broker-dealer that sees the market faster may complete the routing itself, or may prefer not to route at all, for reasons the rule does not give.

Routing has a disclosure cost. The venue, the size, and the time of each fill together say how much of a large order is still to come. A trader fast enough to read the pattern trades ahead of the remainder. The order types that give up routing to avoid this are covered in [intermarket sweep order](intermarket%20sweep%20order.md) and [do-not-ship order](do-not-ship%20order.md).

---

Flashcards for this section are as follows:

- why a broker-dealer may route the order itself ::@:: The exchange's own router can be slower than the broker's technology.
- what a visible pattern of fills discloses ::@:: How much of a large order is still to come.
