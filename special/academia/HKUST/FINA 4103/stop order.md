---
aliases:
  - stop order
  - stop-limit order
  - stop-market order
  - trigger price
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/stop_order
  - language/in/English
---

# stop order

A _stop order_ specifies a trigger (stop) price $P_S$ and stays dormant until the last execution price reaches that level. A buy stop triggers when the price rises to $P_S$; a sell stop triggers when it falls to $P_S$ or below. Once triggered, the order becomes either a limit order (stop-limit) or a market order (stop-market).

---

Flashcards for this section are as follows:

- what a stop order specifies ::@:: A trigger price at which the order activates.
- when a buy stop order triggers ::@:: When the last execution price rises to the stop price or above.
- when a sell stop order triggers ::@:: When the last execution price falls to the stop price or below.
- why a stop order does not execute before its trigger ::@:: It stays dormant, holding the position rather than selling early.
- what a sell stop does when the price prints exactly at the stop price ::@:: It activates, and the stop-limit sell is placed on the book at its ask.

## stop-limit and stop-market

A stop-limit sell for 100 shares at ask = 113 dollars with stop price 115 dollars holds the stock until the price reaches the stop.

If the price falls to 115 dollars, the stop-limit sell is placed on the book at 113 dollars. At 117 dollars instead, it is placed at 117, above the market, and waits for a buyer to reach it. A stop-market sell, by contrast, executes as a market order once the stop is triggered.

Exercise: in the same situation, set the ask at \$117. What does the LOB look like after the stop triggers? What if the order is stop-market sell?

---

Flashcards for this section are as follows:

- difference between stop-limit and stop-market ::@:: A stop-limit places a limit order on the book; a stop-market executes immediately as a market order.
- what a stop-limit with a limit above the current price does when triggered ::@:: It rests on the book above the market instead of filling at once.
- why a trader uses a stop order ::@:: To hold a position while the price stays favorable, and exit when it turns.
