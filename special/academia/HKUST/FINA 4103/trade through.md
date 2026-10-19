---
aliases:
  - no trade through
  - order protection rule
  - trade through
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/trade_through
  - language/in/English
---

# trade through

A _trade through_ happens when a marketable order executes on one exchange while a better quote is available on another. Rule 611 of [Regulation NMS](Regulation%20NMS.md), the order protection rule, prohibits it. A marketable order has to be routed to the exchange that offers the best price. Whichever venue a trader happens to connect to, the order still reaches the best price available.

---

Flashcards for this section are as follows:

- what trade through is ::@:: Executing a marketable order on one exchange while a better quote is available on another, which Rule 611 of Regulation NMS prohibits. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- what a marketable order must do under the order protection rule ::@:: Be routed to the exchange that offers the best price. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- guarantee the order protection rule gives ::@:: Execution at the best price among the exchanges, no matter where the order was placed. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- why the venue a trader connects to stops mattering ::@:: The order is routed to the best price available wherever it was sent. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## the routing obligation

The obligation falls on the exchange that receives the order, not on the trader who sent it. That exchange has to check the prices at the other exchanges and route the order where the better quote is. A [smart order router](smart%20order%20routing.md) is what does that work.

Exchange A offers 100 shares for sale at 101 dollars and 100 more at 100 dollars. Exchange B offers 100 shares for sale at 99 dollars, the lowest offer in the market. A trader sends a buy order for 100 shares to A. A cannot fill it at its own 100 dollars, because that would be trading through B's 99. The order has to go to B, and the trader pays 99 instead of 100.

Rule 611 protects the price and nothing else. A complying order still pays the venue's fee and still consumes the venue's liquidity. Its fills also show how much of the order is still outstanding, which is the [information leakage](intermarket%20sweep%20order.md#information%20leakage) routing creates.

---

Flashcards for this section are as follows:

- who bears the routing obligation ::@:: The exchange that receives the order, not the trader who sent it. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- what that exchange must do to discharge it ::@:: Check the prices at the other exchanges and route the order where the better quote is. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- trade through in the worked example ::@:: Filling the buy at A's own 100 dollars, when B offers at 99. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- what the order protection rule does not cover ::@:: Fees, the liquidity a venue supplies, and the fact that the order reveals itself. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
