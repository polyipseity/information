---
aliases:
  - matching engine
  - matching system
  - order matching system
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/order_matching_system
  - language/in/English
---

# order matching system

An _order matching system_ is the electronic system at the core of a modern exchange: it matches buy and sell orders, and the platform around it exists to feed the engine orders in a fixed arrival order and to publish what the engine does. A trading order expresses a trading intent, such as wanting to buy Apple Inc. (AAPL) stock, and the matching system decides when the order is filled and when it is done. Most undergraduate computer science students could code the limit-order book protocol behind the matching, a short list of comparisons against a price-ordered book; running that algorithm on a large volume of time-varying messages with extremely low latency and zero system downtime is harder. The run is where the exchange's promise is kept or broken: every participant has to be shown the same order of arrival and the same book, at the moment the engine acts on it, without the engine stopping. A match that arrives late, or a book that stops updating, turns price-time priority into a lottery.

An order arrives as a message and goes through several steps: it enters the exchange's matching engine, is matched with counterparty orders and executed or cancelled, and is then settled, including delivery and storage. The settlement step is covered in [settlement (finance)](settlement%20(finance).md).

Most exchanges keep the details of their systems to themselves; the London Stock Exchange (LSE), Deutsche Börse, and the Chicago Mercantile Exchange (CME) are exceptions. The LSE infrastructure, documented by Aquilina et al. (2020), lays out the standard circuit. Orders flow from the traders through a firewall into the gateways, and a gateway passes each message to the sequencer. The sequencer fixes the order of the messages and hands a single string of information to the matching engine. The engine's outcome messages then travel to the distribution server, back out through the gateways to the traders, and through the market data processor to the public data feeds.

---

Flashcards for this section are as follows:

- what an order matching system does at an exchange ::@:: It is the core of the exchange system: it matches buy and sell orders by running the limit-order book protocol.
- the hard part of running an exchange platform ::@:: Processing a large volume of time-varying messages with extremely low latency and zero system downtime.
- why the limit-order book protocol is easy while running it is hard ::@:: The protocol is a short list of comparisons on a price-ordered book; the difficulty is showing every participant the same arrival order and the same book without stopping, since a late match or a stale book makes priority arbitrary.
- the steps an order message goes through ::@:: It enters the exchange's matching engine, is matched with counterparty orders and executed or cancelled, and is then settled, including delivery and storage.
- exchanges that make their system details public ::@:: The London Stock Exchange (LSE), Deutsche Börse, and the Chicago Mercantile Exchange (CME).
- the route an order message travels at the London Stock Exchange (LSE) ::@:: Traders send it through a firewall into the gateways, a gateway passes it to the sequencer, the sequencer fixes the message order for the matching engine, and the engine's outcome messages go to the distribution server and on to the market data processor.
- the study whose description of the London Stock Exchange (LSE) infrastructure supplies the gateway, sequencer, engine, and data-feed circuit of a matching system ::@:: Aquilina et al., 2020.

## gateways and validation

Market participants do not interact with the matching engine directly. Every message first passes through a firewall and enters the gateways, and a gateway passes the message on to the sequencer. Along the way the gateways verify that each message is valid: all required information is included, a limit order carries a limit price, and the message breaks no exchange rule.

---

Flashcards for this section are as follows:

- where a trader's message enters the exchange ::@:: Through the firewall and then the gateways; market participants never hand orders to the matching engine directly.
- what the gateways check before a message moves on ::@:: That all required information is included, such as a limit price for a limit order, and that the message violates no exchange rule.

## arrival order and the sequencer

The sequencer receives input from all the gateways, decides the order of the messages, and passes a single sequence of information to the matching engine. Details vary across exchanges, but the typical arrangement is round-robin processing: the gateways are served one after another in rotation, so the engine receives one agreed order of arrival instead of the competing claims of several gateways at once.

By default a trader can place orders at only one gateway, and a trader who wants to reduce the risk of unlucky sequencing can subscribe to multiple gateways. The risk is real: on the London Stock Exchange (LSE), about 6% of orders arrive at the gateways faster than some competing order but are processed or executed after the competing order. This randomness is a sizable risk in [high-frequency trading](high-frequency%20trading.md) (HFT).

Rotation decides which message the engine sees first, so a trader cannot buy priority by reaching a gateway sooner than a rival. That is what the 6% measures: those orders reached a gateway ahead of a competitor and still lost the race, because the sequencer settled it on the exchange's schedule. Speed spent on the trip to the gateway can be wasted before the engine ever compares the two orders. Subscribing to more gateways spreads a strategy's exposure over more rotations, and it leaves the choice with the sequencer.

---

Flashcards for this section are as follows:

- what the sequencer does with input from the gateways ::@:: It determines the order of the messages and passes a single sequence of information to the matching engine.
- how round-robin processing serves the gateways ::@:: One after another in rotation, so the engine receives one agreed order of arrival; the exchange's schedule, not a trader's speed at a gateway, decides which message comes first.
- why arriving first at a gateway does not ensure executing first ::@:: The sequencer's rotation decides the order the engine sees, so a trader's lead on the way to a gateway can be reversed before the two orders are ever compared.
- how a trader reduces the risk of unlucky gateway sequencing ::@:: By subscribing to multiple gateways; by default a trader can place orders at only one gateway.
- the share of jumbled orders observed at the London Stock Exchange (LSE) ::@:: About 6% of orders arrive at the gateways faster than some competing order but are processed or executed after the competing order.
- what that 6% means for a fast trader ::@:: The race is settled by the exchange's rotation rather than by the trader, so speed can be wasted and a high-frequency trading (HFT) strategy carries a risk it cannot spend away.

## matching engine

The matching engine is the core of the exchange system. It executes the limit-order book protocol, processes messages serially in the order it receives them, and disseminates information about each outcome. An incoming limit order meets a fixed routine. The engine checks whether it trades immediately against the existing limit orders; if it does, it is matched with the standing orders and executed. If it does not, it is added to the limit-order book, and either way the engine disseminates the result, the updated book included.

Which standing order an incoming order trades against is settled by price-time priority: better prices execute first, and among same-priced orders the first to arrive is served first (see [continuous trading](continuous%20trading.md) and [limit order](limit%20order.md)). Price outranks time. An early order keeps its place only against later orders at its own price, and anyone willing to quote better steps in front of that whole queue. Arriving early is worth paying for, and it is worth less than a single tick. Take a book with standing sell orders of 100 units at 101 dollars and 100 units at 100 dollars, and a standing buy order of 200 units at 99 dollars. An incoming buy limit order for 100 units at 100 dollars takes the offer at 100 dollars, the better-priced sell order, before the one at 101 dollars. The 101-dollar offer is worse for the incoming buyer by a dollar per unit, so the engine fills from the cheaper side and leaves the dearer offer resting. The seller at 101 dollars may have arrived first and still waits, which is what price priority costs a resting order.

---

Flashcards for this section are as follows:

- the routine an incoming limit order follows in the matching engine ::@:: The engine checks whether it trades immediately against the existing limit orders; if so it is matched and executed, if not it joins the limit-order book, and the result and updated book are disseminated either way.
- how the matching engine processes messages ::@:: Serially, in the order it receives them.
- the rule that decides which standing order an incoming order trades against ::@:: Price-time priority: better prices execute first, and among same-priced orders the first to arrive is served first.
- where an incoming buy limit order of 100 units at 100 dollars lands on a book with standing sell orders of 100 units at 101 dollars and 100 units at 100 dollars and a standing buy order of 200 units at 99 dollars ::@:: It executes against the 100 units at 100 dollars, the better-priced sell order, before the one at 101 dollars.
- which standing order in that book is worse for the incoming buyer, and why ::@:: The 100 units at 101 dollars, dearer by a dollar per unit than the offer at 100 dollars; the engine takes the cheaper offer first and leaves the dearer one resting.
- why better price beats earlier arrival ::@:: Price is compared before time, so an order quoting a better price is served ahead of the whole queue at a worse one, and arrival order separates only orders at the same price.
- what price-time priority costs a trader who is early ::@:: Priority within their own price only: an order that arrived later but quotes one tick better jumps the entire queue, so the wait is protected against same-price rivals and against nothing else.

## market data dissemination

The matching engine passes its outcome messages to the distribution server and to the market data processor, and that round trip delays how quickly traders can react to what the engine has done. Two flavors of market data access come out of this arrangement: processed data reaches the public data feeds, while direct data feeds provide the raw data without going through the processor. The two are compared in [securities information processor](securities%20information%20processor.md).

---

Flashcards for this section are as follows:

- the two destinations of the matching engine's outcome messages ::@:: The distribution server and the market data processor.
- how the dissemination process affects traders ::@:: It delays their reaction to the engine's outcomes.
- how direct data feeds differ from processed market data ::@:: Direct data feeds provide the raw data without going through the market data processor.

## why speed matters

The engineering of the platform is what matters once trading speed is a first-order priority, and price-time priority is why speed pays: among same-priced orders the first to arrive at the engine is served first, so processing order turns milliseconds into priority. The sharpest case is the sniping race. A standing limit sell order rests at 100 dollars, new information arrives saying the stock value should be 101 dollars, and the 100-dollar quote is now stale. Takers rush to take the stale limit order and makers rush to cancel it, and latency rather than price decides the race (see [quote sniping](quote%20sniping.md)). The stale quote is a loss already made, and the race decides only who pays it. A taker who reaches it first buys for 100 dollars what is now worth 101, and a maker who has not cancelled yet sells a dollar per unit below value. Either the taker gets the unit and the maker's loss is realized, or the maker cancels in time and the taker gets nothing, so the two sides contest the same dollar and only their reaction times differ.

How traders increase their speed, whether through reaction time, data processing time, or order entry time, is an open question, as is what speed services exchange platforms provide and whether a fast exchange structure improves market quality (see [market microstructure](market%20microstructure.md)). An exchange can also sit on both sides of speed: it provides speed services, such as a direct data feed, and tries to slow down incoming orders at the same time. Those measures are called speed bumps.

---

Flashcards for this section are as follows:

- why price-time priority makes speed valuable ::@:: Among same-priced orders the first to arrive at the engine is served first, so processing order turns milliseconds into priority.
- the sniping race for a stale quote: a standing limit sell order rests at 100 dollars and new information says the stock value should be 101 dollars ::@:: The 100-dollar quote is now stale; takers rush to take the stale limit order and makers rush to cancel it, and latency rather than price decides the race.
- what the stale 100-dollar quote against a 101-dollar value guarantees, and to whom ::@:: A loss to whoever is slow: the taker who arrives first buys a dollar per unit below value, and the maker who has not cancelled sells a dollar per unit below value.
- what speed bumps are ::@:: Measures by which an exchange tries to slow down incoming orders while still providing speed services, such as a direct data feed.
- open questions about speed and exchange structure ::@:: How traders increase speed, through reaction time, data processing time, or order entry time; what speed services exchange platforms provide; and whether a fast exchange structure improves market quality.
