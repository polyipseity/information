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

The _bid-ask spread_ is the difference between the best ask and the best bid on the limit-order book. A trader pays it once per round trip of one unit: buy then sell, or sell then buy. A buyer takes the ask and a seller takes the bid, so the round trip enters at the higher price and leaves at the lower one, and the difference goes to whoever stood on the other side of both trades. Since the cost falls once per round trip rather than once per order, it sets how often a strategy can afford to trade: a trip that does not expect to gain more than the spread loses money. Frequent trading then needs a large edge every time, while a narrow spread lets a small edge be collected again and again.

A small spread means a liquid market: a trader can enter and leave close to the fair price, and can do it often.

Several prices are quoted for the same asset at once. A stock ticker tape usually shows the last execution price, the middle of the limit-order book gives the mid-point quote, and the best bid and offer (BBO) gives the best bid and the best ask. When someone says "AAPL is now 100 dollars", they usually mean the last trade, not the current BBO.

---

Flashcards for this section are as follows:

- definition of the bid-ask spread ::@:: The difference between the best ask and the best bid on the limit-order book.
- why a round trip pays the spread once rather than once per order ::@:: Buying takes the ask and selling takes the bid, so the trader enters at the higher price and leaves at the lower one; the difference is handed over once, to the maker who stood on the other side of both trades.
- what the spread costs a round-trip trader ::@:: The difference between the two prices, on one unit bought then sold, or sold then bought.
- what the spread implies about how often a trader can afford to trade ::@:: Every round trip starts down by the spread, so a strategy pays only if its expected gain per trip beats it; frequent trading needs a large edge on each trip, while a narrow spread lets a small edge be collected repeatedly.
- what the spread measures ::@:: Market liquidity: a small spread means a trader can enter and leave close to the fair price, and can trade often.

## best bid and offer

The _best bid_ is the highest bid in the standing limit orders, and the _best ask_ (or offer) is the lowest ask. Together they form the _Best Bid and Offer (BBO)_. Aggregated across all markets, they form the _National Best Bid and Offer (NBBO)_.

---

Flashcards for this section are as follows:

- what the best bid is ::@:: The highest bid in the standing limit orders.
- what the best ask is ::@:: The lowest ask in the standing limit orders.
- what NBBO stands for ::@:: National Best Bid and Offer: the aggregate BBO across all markets.

## why the spread exists

Three explanations say why a quote carries a spread rather than a single price: the price of immediacy, inventory cost, and information friction.

The three are not rival estimates of one number: each answers a different question about the same quote. Immediacy says what the market maker is paid for, inventory cost says what it risks while holding the position the quote forces on it, and information friction says what it loses to someone who knows more. A single observed spread is consistent with all three at once, which is why they are hard to separate in data.

---

Flashcards for this section are as follows:

- the three explanations for why a quote carries a spread ::@:: The price of immediacy, inventory cost, and information friction.
- why the three explanations of the spread are hard to separate in data ::@:: They answer different questions about one quote: what the market maker is paid for, what it risks while holding the position the quote forces on it, and what it loses to a better-informed counterparty.

### immediacy

Demsetz (1968, Quarterly Journal of Economics (QJE)) prices the spread as _immediacy_: the compensation a [market maker](market%20maker.md) receives for providing immediate trading services. The spread reflects the market maker's order-processing cost and time value. On this reading the quote is a fee for a service: the trader who wants to trade now pays for the wait it saves.

---

Flashcards for this section are as follows:

- what the spread compensates a market maker for under the immediacy explanation ::@:: Providing immediate trading services.
- who pays the spread under the immediacy explanation ::@:: The trader who wants to trade now, paying for the wait that a resting order would have had to sit through.
- what the spread reflects about a market maker under the immediacy explanation ::@:: The market maker's order-processing cost and time value.
- which explanation of the spread treats it as a fee for immediate execution, traced to order-processing cost and time value? ::@:: Harold Demsetz, 1968, Quarterly Journal of Economics (QJE).

### inventory cost

Smidt (1971, Financial Analysts Journal (FAJ)) and Stoll (1978, Journal of Finance (JF)) give inventory cost as the spread's source. A market maker has to take a position, and holding that inventory carries price risk. The spread is then a charge for the position the quote creates: the price risk of the inventory has to be earned back on the trades the dealer makes.

---

Flashcards for this section are as follows:

- what serving as a market maker forces a dealer to do under the inventory-cost explanation ::@:: Take a position.
- what risk a dealer's inventory carries under the inventory-cost explanation ::@:: Price risk.
- which paper sources the spread in the position a dealer must take by standing ready to trade? ::@:: Seymour Smidt, 1971, Financial Analysts Journal (FAJ).
- which paper sources the spread in the price risk of the inventory that position leaves a dealer holding? ::@:: Hans R. Stoll, 1978, Journal of Finance (JF).

### information

Glosten and Milgrom (1985, Journal of Financial Economics (JFE)) name information friction, developed in the [Glosten–Milgrom model](Glosten–Milgrom%20model.md): here the market maker loses to a counterparty who knows more. The model carries no order-processing cost and no inventory position, so the spread it derives comes from the asymmetry alone. The maker cannot tell an informed trade from an uninformed one, so the quote has to be wide enough that the loss on the informed trades is recovered from the uninformed ones. An uninformed trader pays for the informed traders' presence, and a market with more informed flow carries a wider spread.

---

Flashcards for this section are as follows:

- the source of the spread under its information explanation ::@:: Information friction.
- the model in which the spread's information friction is developed ::@:: The Glosten–Milgrom model.
- why the information explanation of the spread needs neither an order-processing cost nor an inventory position ::@:: The Glosten–Milgrom model carries neither, so the spread it derives comes from the asymmetric information alone: the loss to a better-informed counterparty is enough by itself.
- how the information explanation recovers the market maker's loss ::@:: The maker cannot tell an informed trade from an uninformed one, so the spread has to be wide enough that the loss on informed trades is recovered from the uninformed ones; an uninformed trader pays for the informed traders' presence.
- which paper sources the spread in the market maker's loss to a counterparty who knows more about the value? ::@:: Lawrence R. Glosten and Paul Milgrom, 1985, Journal of Financial Economics (JFE).

## mid-point quote

The _mid-point quote_ (mid price) is the average of the best ask and the best bid. Neither input is a transaction price: both are quotes that someone is willing to trade at, one on each side of the market. The average says where the two sides sit relative to each other, so it is used as a "fair" price of the asset and as the reference for marking a position. A trader never gets the mid, since a buyer pays the ask and a seller receives the bid, and each price sits half the spread away from it. Across several exchanges the reference is the NBBO rather than a single venue's quote.

---

Flashcards for this section are as follows:

- formula for the mid-point quote ::@:: The average of the best ask and the best bid.
- why the mid-point quote is not a transaction price ::@:: Both inputs are quotes that someone is willing to trade at, one on each side, so the mid records where the two sides sit rather than what anyone paid.
- what the mid-point quote represents ::@:: A "fair" price of the asset, used to mark a position.
- how far a trade sits from the mid-point quote ::@:: Half the spread away: a buyer pays the ask above the mid, and a seller receives the bid below it.
- what the mid-point quote is in a multi-exchange market ::@:: The midpoint of the national best bid and offer (NBBO), not of a single venue's quote.

## near side and far side

When a trader buys, the best bid is the _near side_ of the spread (the side the trader is on) and the best ask is the _far side_. When a trader sells, the best ask is the near side and the best bid is the far side. The near side takes its name from what the trader would post: a buyer bids and a seller offers. To trade now the trader crosses to the far side and accepts the price standing there, so the near quote is what waiting earns and the far quote is what impatience costs. Each trader gives up the distance from the mid to the quote they cross, and with the quotes placed evenly around the mid the two sides give up the same amount.

---

Flashcards for this section are as follows:

- near side for a buyer ::@:: The best bid.
- far side for a buyer ::@:: The best ask.
- near side for a seller ::@:: The best ask.
- far side for a seller ::@:: The best bid.
- which side of the spread a trader actually trades at ::@:: The far side: a buyer pays the best ask and a seller receives the best bid, so each crosses away from the side where their own order would rest.
- what decides how much of the spread a trader gives up ::@:: The distance from the mid to the quote they cross, which is half the spread when the quotes sit evenly around the mid.

## locked and crossed markets

A market is _locked_ when the best bid equals the best ask, and _crossed_ when the best bid exceeds the best ask. A lock leaves no spread at all, so nobody is paid to stand between a buyer and a seller, and the next order on either side can trade at once. A cross describes a buyer willing to pay more than a seller is asking, which cannot survive contact with a single book: the matching engine would have paired those two orders already. In a single-exchange environment neither state arises, and neither is a bargain when one does appear. Both are relevant in multi-exchange markets and in limit-order book (LOB) data, where the quotes come from separate venues that have not yet traded with each other, or from a record taken before the match finished.

Across exchanges the states are prohibited outright. Rule 610 of [Regulation NMS](Regulation%20NMS.md), the access rule, forbids a venue from accepting an order that would lock or cross the market on another venue. It requires the venue to route such an order to the exchange holding that price instead. The prohibition does not reach hidden quotes.

The two rules divide by order type. Rule 611, the [order protection rule](trade%20through.md), covers marketable orders, the ones that execute. Rule 610 covers liquidity-provision orders, the ones that rest. A resting order at a price another venue is already quoting does not trade, so it cannot violate the price protection, but it can freeze the book.

---

Flashcards for this section are as follows:

- when a market is locked ::@:: When the best bid equals the best ask.
- when a market is crossed ::@:: When the best bid exceeds the best ask.
- what a locked quote says about the book ::@:: The best bid equals the best ask, so no spread is left and nobody is paid to stand between a buyer and a seller; the next order on either side trades at once.
- why a crossed market is a failure of the tape or the routing rather than a bargain ::@:: A buyer willing to pay more than a seller asks would already have traded on a single book, so a cross means the quotes come from venues that have not met, or from data recorded before the match, and no free profit waits there.
- whether locked or crossed markets exist in a single-exchange environment ::@:: No; they are relevant only in multi-exchange markets and in limit-order book (LOB) data.
- which rule forbids a locked or crossed market across exchanges ::@:: Rule 610, the access rule.
- what a venue must do with a limit order that would lock or cross another venue's market ::@:: Route it to the venue holding that price.
- whether the prohibition reaches hidden quotes ::@:: No.
- which order type each rule protects ::@:: Rule 611 the marketable orders that execute, and Rule 610 the liquidity-provision orders that rest.

## executions inside and outside the quotes

Trades do not always execute at the quoted prices. A buy that fills below the best ask, or a sell that fills above the best bid, executes _inside the spread_. A buy that fills above the best ask, or a sell below the best bid, executes _outside_ it. Trade prices in data are not confined to the quotes, and an execution price cannot be computed from the quotes alone.

---

Flashcards for this section are as follows:

- how a trade executes inside the spread ::@:: A buy fills at a price lower than the best ask, or a sell at a price higher than the best bid.
- how a trade executes outside the spread ::@:: A buy fills at a price higher than the best ask, or a sell at a price lower than the best bid.
- why trade prices in data are not confined to the quotes ::@:: Trades execute inside and outside the best bid and offer (BBO), so an execution price cannot be computed from National Best Bid and Offer (NBBO) data alone.

### inside the spread

Broker-dealers may internalize incoming orders and execute them off the book; floor traders at the New York Stock Exchange (NYSE) are one example, and internalization must comply with [Regulation NMS](Regulation%20NMS.md). [Hidden orders](hidden%20order.md) can rest at prices inside the spread, and [midpoint peg orders](pegged%20order.md), offered at venues such as IEX, execute at the midpoint of the national quotes. The terms these trades execute on are available, but not in the limit-order book (LOB) data, so execution prices do not always follow the best quote data.

An execution inside the spread is _price improvement_: the taker pays less than the ask, or receives more than the bid, and the difference is money a liquidity provider chose to give up. A hidden order prices inside to win the trade without showing its size: an incoming order reaches the price inside the spread before the displayed quote, and the quantity stays off the book.

---

Flashcards for this section are as follows:

- three mechanisms that execute trades inside the spread ::@:: Broker-dealer internalization of incoming orders, which must comply with Regulation National Market System (NMS); hidden orders resting inside the spread; and midpoint peg orders executing at the midpoint of the national quotes.
- why inside-spread executions do not follow the best quote data ::@:: The terms they execute on are available but not on the limit-order book (LOB) data, so the recorded quotes do not show where they traded.
- what price improvement is, and who gives it up ::@:: An execution inside the spread, where the taker pays less than the ask or receives more than the bid; the difference is the part of the spread a liquidity provider gives up to win the trade.
- what a hidden order gains by resting inside the spread ::@:: A price better than the displayed quote on its side, so an incoming order reaches it first, while its size stays hidden.

### outside the spread

An [intermarket sweep order](intermarket%20sweep%20order.md) (ISO) can execute at its local exchange at prices worse than the NBBO, and the [securities information processor](securities%20information%20processor.md) records the outside-spread execution. Reading executions then needs a consolidated view across multiple limit-order books.

Large trades can be negotiated directly between buyer and seller instead of executed on the continuous limit-order book. A block trade priced by negotiation is closed to regular traders, so it is called "inaccessible liquidity". It is not displayed, but it must comply with reporting regulation. The NYSE offers "upstair" block trading via specialists. _Upstair_ (usually written _upstairs_) names the brokered market that sits off the exchange floor: a desk takes the block order, finds the other side by working the phones or the dealer network rather than by resting it on the book, and the specialists on that desk arrange the trade. The upstairs market is where size trades when the public book cannot absorb it without moving the price, so the block prints away from the NBBO rather than inside it. Prices far from the NBBO incorporate potential liquidity, adverse selection, and price impact, among other things. The price impact a large order pays is described in [market liquidity](market%20liquidity.md).

Price data records execution prices but often misses the trade data: the side of the trade, the quantity, and more. Take a block sell order executed at 3:30pm at the volume weighted average price (VWAP) after negotiation. The data record shows a trade at 3:30pm at the VWAP, with the best ask at 3:30pm below that price. The trade printed above the best ask looks like a buy order crossing the quote. The order was selling.

---

Flashcards for this section are as follows:

- how an intermarket sweep order (ISO) executes outside the quotes ::@:: At its local exchange it can trade at worse prices than the National Best Bid and Offer (NBBO), and the securities information processor (SIP) records the execution.
- where a negotiated block trade executes and who can reach it ::@:: Off the continuous limit-order book, between a negotiated buyer and seller; regular traders cannot reach it, so it is called "inaccessible liquidity".
- what an undisplayed negotiated block trade still must comply with ::@:: Reporting regulation, despite never appearing on the continuous limit-order book.
- what prices far from the National Best Bid and Offer (NBBO) in negotiated block trades incorporate ::@:: Potential liquidity, adverse selection, and price impact, among other things.
- what the "upstair" (upstairs) market is, in the New York Stock Exchange block-trading sense ::@:: The brokered market off the exchange floor, where a desk takes a block order and finds the other side through dealers and phone calls instead of resting it on the public book, so specialists arrange trades that the book could not absorb without moving the price.
- why a block trade arranged upstairs prints away from the NBBO rather than at the quotes ::@:: The public book cannot absorb the size without a price move, so the trade is negotiated at a price that compensates whoever takes the other side, which puts it outside the quoted market.
- how a block sell order's execution can be misread in trade data ::@:: Executed at 3:30pm at the volume weighted average price (VWAP) after negotiation, it prints above the best ask at 3:30pm, which looks like a buy order crossing the quote while the order was in fact selling.
