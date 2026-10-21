---
aliases:
  - settlement
  - settlement (finance)
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/settlement_(finance)
  - language/in/English
---

# settlement (finance)

Every trade in the financial system is agreed at one moment and completed at another (see [financial system](financial%20system.md)). A trade is executed when the buyer and the seller agree on the terms of trade, the price and the quantity. It is settled when the asset is delivered and the cash is transferred, and settlement is where ownership passes. An exchange's [order matching system](order%20matching%20system.md) fixes those terms; delivery and payment follow at settlement.

---

Flashcards for this section are as follows:

- what execution of a trade means ::@:: The buyer and the seller have agreed on the terms of trade, the price and the quantity.
- what settlement of a trade means ::@:: The asset is delivered and the cash is transferred, so ownership passes.
- how execution and settlement are ordered in time ::@:: A trade is executed when the terms are agreed and settled later, when the asset and the cash change hands.

## settlement cycle

Assets and cash do not change hands immediately after a trade executes. The $T+2$ rule stipulates the timing of settlement: $T$ is the transaction date, and $+2$ means waiting two days for the transfer of ownership or cash. Stocks, bonds, municipal securities, and mutual funds settle at $T+2$, while Treasury bills and short-term secured bonds settle at $T+1$.

The two days are a window of exposure. Through it the buyer holds cash the seller has not been paid, and the seller holds an asset the buyer has not received, so each side trusts the other to perform. A price move or a missing delivery inside that window falls on whichever side is still waiting. Treasury bills and short-term secured bonds sit at $T+1$, which halves that time.

---

Flashcards for this section are as follows:

- what the $T+2$ settlement rule stipulates ::@:: The timing of settlement: $T$ is the transaction date, and $+2$ means waiting two days for the transfer of ownership or cash.
- the settlement cycle for stocks, bonds, municipal securities, and mutual funds, where $T$ is the transaction date ::@:: $T+2$.
- the settlement cycle for Treasury bills and short-term secured bonds, where $T$ is the transaction date ::@:: $T+1$.
- what the settlement window exposes each side to ::@:: The buyer holds cash the seller has not been paid, and the seller holds an asset the buyer has not received, so a price move or a failure inside the window falls on whichever side is still waiting.
- why a shorter settlement cycle carries less risk ::@:: Less time passes before the asset and the cash change hands, so fewer things can go wrong while each side waits on the other.

## why settlement takes time

Futures markets use a $T+0$ rule instead. Settlement elsewhere is held back by the number of different parties involved, by default risk, and by historical reasons. Most markets are moving toward same-day settlement, or at least shorter delays, but confirmation still takes a lot of manual work.

Less liquid markets with structured securities, such as over-the-counter markets (see [over-the-counter (finance)](over-the-counter%20(finance).md)), tend to settle orders immediately: only a few parties with established connections are involved, and the terms are tailored to each trade.

The reasons for the wait come down to who has to be trusted. A trade that passes through many parties needs each step confirmed before the next can complete, and default risk means nobody hands over the asset before the cash is confirmed. Futures at one end settle on the trade date, and over-the-counter structured products at the other end settle at once, because a short chain of parties who already know each other needs no confirmation step to protect it.

---

Flashcards for this section are as follows:

- how futures markets differ on settlement timing, where $T$ is the transaction date ::@:: They use a $T+0$ rule.
- three reasons a settlement is not instant ::@:: The number of different parties involved, default risk, and historical reasons.
- the direction most markets are moving on settlement timing ::@:: Toward same-day settlement, or at least shorter delays, though confirmation still takes a lot of manual work.
- why less liquid markets with structured securities tend to settle immediately ::@:: Only a few parties with established connections are involved, and the terms are tailored to each trade.
- why a chain of many parties delays settlement ::@:: Each link has to be confirmed before the next can complete, so the transfer waits on every step between the buyer and the seller.
- what the two ends of the settlement range show about the delay ::@:: Futures settle on the trade date and over-the-counter structured products settle at once, so the wait covers the parties and their default risk rather than the mechanics of the transfer.

## storage costs

Most settlements involve electronic transfers of a security, but sometimes a physical asset is delivered: an in-kind commodity, or the asset underlying a futures or forward contract. Physical delivery raises costs of its own: storage and delivery can be expensive, and the wait between trade and settlement requires markets for temporary storage, for substitute assets, and for cash.

Storage is why the cash and the asset need not move at the same moment. Whoever holds the physical good across the wait pays to put it somewhere and to finance it, and the buyer who waits needs something standing in for the good until it arrives. Markets for temporary storage, for substitute assets, and for cash price that interval, so the side left holding the asset pays for settling late.

---

Flashcards for this section are as follows:

- when settlement involves the delivery of a physical asset ::@:: Sometimes, for an in-kind commodity or the asset underlying a futures or forward contract, though most settlements involve electronic transfers of a security.
- the costs physical delivery raises between trade and settlement ::@:: Storage and delivery can be expensive, and the wait requires markets for temporary storage, substitute assets, and cash.
- why the cash and the asset need not move at the same moment under physical delivery ::@:: Holding the good across the wait costs storage and financing, so markets for temporary storage, substitute assets, and cash price the interval, and the side left holding the asset pays for it.

## clearing and post-trade services

Settlement and delivery are post-trade services: they take place after the trade, outside the exchange platform, which is not responsible when they fail. A party that fails to settle is penalized with trade restrictions.

The central securities depository (CSD) keeps track of ownership and custody. When one party fails to trade, the CSD completes the trade. It collects fees from both sides and builds buffers with them.

The depository's guarantee keeps one failure from spreading. The party that performed still receives the asset or the cash, and the fees taken from both sides fund that guarantee. A failure then costs the defaulter its access to trading rather than handing the loss to its counterparty.

---

Flashcards for this section are as follows:

- what makes settlement and delivery post-trade services ::@:: They take place after the trade, outside the exchange platform, which is not responsible for their failures.
- the penalty for failing to settle a trade ::@:: Trade restrictions.
- what the central securities depository (CSD) keeps track of ::@:: Ownership and custody.
- what the central securities depository (CSD) does when one party fails to trade ::@:: It completes the trade.
- how the central securities depository (CSD) builds buffers ::@:: By collecting fees from both sides.
- why a failed trade costs the defaulter rather than its counterparty ::@:: The central securities depository (CSD) completes the trade out of the buffers those fees fund, so the side that performed still receives the asset or the cash and the defaulter faces trade restrictions.

## what a trader sees

A trader sends an order through a broker and watches it fill at once. The broker then shows the new position and the changed cash balance, so the trade looks finished. Nothing has moved between the buyer and the seller at that point. The order has been matched, and the broker has written down what it owes the trader and what the trader owes it. The transfer between the two brokers, through the clearing house, waits for the settlement date. An institution sees the same gap with one more party in it, because its custodian reports the position and the transfer runs between two custodians through the depository.

---

Flashcards for this section are as follows:

- what a broker's account shows a trader once an order fills, and what has happened ::@:: The new position and the changed cash, booked by the broker. Only the match has happened; delivery and payment between the two brokers follow on the settlement date.
- how an institutional trade shows the same gap as a retail one ::@:: The custodian reports the position at once, and the transfer runs between the two custodians through the depository on the settlement date.

### speed of the fill

A market order can fill faster than the trader can react to it, and the broker reports the position and the cash at once. The easy conclusion is that the trade is complete. What is complete is the match. Two orders have met in the matching engine, and the price is fixed. The shares still sit at the seller's broker and the cash at the buyer's broker, and the two brokers settle with each other through the clearing house on the settlement date.

What the trader holds until then is a claim on the broker. The broker owes shares to a buyer or cash to a seller, and it has to deliver its own leg whatever the client does. Its two legs cancel, so the price is not where its risk sits; the client is, which is why a broker checks the client's cash or holdings before it accepts an order and can close a position the client cannot cover.

---

Flashcards for this section are as follows:

- what an instant fill does and does not complete ::@:: It completes the match between two orders and fixes the price. Delivery and payment between the two brokers wait for the settlement date.
- what a trader holds between a fill and its settlement ::@:: A claim on the broker, which owes the shares to a buyer and the cash to a seller.
- what a broker carries between a client's fill and its settlement ::@:: The client's failure to pay or to deliver, since the broker must settle its own leg with the clearing house whatever the client does. Its two legs cancel, so the price is not its exposure.
- what moves on the trade date and what moves on the settlement date of a stock trade under the $T+2$ rule ::@:: On the trade date the order is matched and each broker books the trade for its client. Two days later the shares and the cash move between the brokers through the clearing house.
- the mistaken belief that a trade has settled once its order fills ::@:: The fill completes only the match between two orders. The shares and the cash stay with the two brokers until they settle through the clearing house on the settlement date.

### ownership before settlement

The account shows the shares as the trader's and lets the trader act on them. The position can be sold, and it counts toward the margin the broker requires. The account makes the position look like settled property, but it is not: the trader holds beneficial ownership, the claim the broker recognises, while legal title moves in the depository's record when the trade settles.

The gap shows in what cannot be done before then. The shares cannot leave the broker until the purchase settles, and the cash a sale produced cannot be withdrawn until the sale does. A resale is the exception, and it hides the difference: the broker nets the purchase against the sale and delivers only the difference to the clearing house, so the second trade succeeds on the broker's books rather than on a title the trader holds.

---

Flashcards for this section are as follows:

- what a trader holds in a position between the purchase and its settlement ::@:: Beneficial ownership, the broker's record of the position as the client's. Legal title moves in the depository's record on the settlement date.
- what a trader can do with a position before its purchase settles ::@:: Sell it, since the broker nets the purchase against the sale and only the difference reaches the clearing house, and count it toward the margin the broker requires.
- what a trader cannot do with a position before its purchase settles ::@:: Move the shares out of the broker, or withdraw the cash a sale produced before that sale settles.
- the mistaken belief that a purchase puts legal title to the shares in the buyer's hands at the match ::@:: The broker records the position as the client's at once, which is beneficial ownership, while legal title moves in the depository's record on the settlement date.

### what the settlement date binds

A purchase lands in the account at once, while the settlement date appears only on the trade confirmation. The date then reads as a formality. It is where the trader's obligations come due.

Proceeds from a sale are not settled cash until the sale settles, so a trader who spends them first is borrowing from the broker for the days in between. A purchase and a resale before the purchase settles leave the broker holding both legs until their dates arrive, and whether the trader may run that pair at all depends on the credit the broker extends. The delivering side faces a sharper constraint. A seller that fails to deliver on the settlement date does more than delay the buyer: the clearing house completes the trade for the other side, and the party that fails to settle is penalised with trade restrictions.

---

Flashcards for this section are as follows:

- the mistaken belief that the settlement date is a formality after the trade is done ::@:: Proceeds are not settled cash before the settlement date; a resale before the purchase settles leaves the broker holding both legs; and a side that fails to deliver faces the clearing house's remedy and trade restrictions.
- what a trader who spends sale proceeds before the settlement date is doing ::@:: Borrowing from the broker until the sale settles.
- whose credit a resale before the purchase settles depends on ::@:: The broker's, which holds both legs until their settlement dates arrive.
- what the side that fails to deliver on the settlement date faces ::@:: The clearing house completes the trade for the other side, and the defaulter is penalised with trade restrictions.

### counterparty to a cleared trade

The wait puts each side's performance in doubt. A trader whose order matches against someone else's reads that trader as the counterparty. The clearing house takes that place instead: it becomes the buyer to every seller and the seller to every buyer, so a trader's obligation runs to it and not to the person whose order was matched. In exchange, the trader gets a guarantee of performance: if one party fails, the clearing house stands in and completes the trade, and the side that performed still receives the asset or the cash.

That guarantee does not reach the price. The price was fixed at the match, and the clearing house delivers that price and that asset. A position that loses value between the trade and its settlement keeps the loss with the trader, because the guarantee covers completion rather than value.

---

Flashcards for this section are as follows:

- the mistaken belief that the trader on the other side of a matched order is the counterparty ::@:: The clearing house becomes the buyer to every seller and the seller to every buyer, so each side's obligation runs to it rather than to the matched trader.
- what the clearing house's guarantee covers ::@:: Performance: if one side fails, the side that performed still receives the asset or the cash.
- what the clearing house's guarantee leaves with the trader ::@:: Price risk between the trade and its settlement, because the price was fixed at the match and the guarantee covers performance rather than value.

### limits of faster settlement

Speed looks like the fix: settle at the same instant as the trade and nothing can go wrong in between. A shorter cycle narrows the window without emptying it. A default can arrive in the last hour as easily as in the last day, and the price can move in that hour too, so speed alone cannot make a trade riskless. Settlement that does remove the window needs the cash and the asset ready at the same moment. Delivery versus payment releases each leg only when the other is there, so a failure on one side leaves the other side whole.

Markets that settle instantly meet that condition already. Where both parties and both assets sit on one ledger, the cash and the security change hands in a single step, and no interval remains for either side to default in or for the price to move across. Where the cash sits on a bank's books, the security on a depository's, and the two sides at different brokers, the legs still have to be brought together, so the wait shrinks instead of disappearing.

---

Flashcards for this section are as follows:

- the mistaken belief that instant settlement would remove the risk from a trade ::@:: It removes the interval, not the risk. A default or a price move can arrive in a short interval as well as a long one.
- what a shorter settlement cycle changes about the risk of a trade ::@:: The length of the interval between the trade and its settlement, not the presence of default risk or price risk inside it.
- what delivery versus payment requires of the two legs ::@:: That the cash and the asset be ready at the same moment, each released only when the other is there.
- where a trade can settle in a single step ::@:: Where both parties and both assets sit on one ledger, so the cash and the security change hands at once.
