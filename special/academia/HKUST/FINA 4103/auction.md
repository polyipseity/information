---
aliases:
  - auction
  - auction market
  - auction theory
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/auction
  - language/in/English
---

# auction

An _auction_ is a mechanism that collects bids and has a market institution set the price, usually to allocate an asset. Auctions are rarely the only way an asset trades: they run alongside continuous markets in primary markets such as newly issued United States government bonds, and outside finance for art, commodities, and airport slots, because they handle high volume and volatility efficiently. In financial markets the two forms that matter are the single-sided auction, in which one side of the market is fixed, and the double auction, in which buyers and sellers both propose prices and quantities. Auction theory makes the structure of each form precise.

---

Flashcards for this section are as follows:

- overview ::@:: A mechanism that collects bids and has a market institution set the price, usually to allocate an asset.
- why auctions suit primary markets ::@:: They handle high volume and volatility efficiently.
- assets and goods auctioned besides newly issued securities ::@:: Art, commodities, and airport slots.
- the two auction forms that matter in financial markets ::@:: The single-sided auction, in which one side of the market is fixed, and the double auction, in which both sides propose prices and quantities.

## single-sided auctions

In a single-sided auction, demand or supply is solicited at each price while the other side of the market is fixed. The standard variants are the first-price auction, which in its Dutch form runs as a descending clock, the second-price auction, which in its English form runs as an ascending outcry, and the all-pay auction. A Dutch auction is strategically equivalent to the sealed-bid first-price auction and an English auction to the sealed-bid second-price auction, under independent private values. The revenue equivalence theorem links what these variants raise. The leading example is the primary market for United States Treasury securities, which runs as a first-price one-sided auction and turns over trillions of dollars a quarter.

---

Flashcards for this section are as follows:

- single-sided auction ::@:: One side of the market is fixed, and demand or supply is solicited at each price.
- Dutch auction ::@:: The descending-clock form of a first-price auction, strategically equivalent to its sealed-bid version under independent private values.
- English auction ::@:: The ascending-outcry form of a second-price auction, strategically equivalent to its sealed-bid version under independent private values.
- third variant of a single-sided auction ::@:: The all-pay auction.
- revenue equivalence theorem ::@:: A theorem relating what the forms of a single-sided auction raise.
- leading example of a single-sided auction ::@:: The primary market for United States Treasury securities, a first-price one-sided auction turning over trillions of dollars a quarter.

## double auctions

In a double auction many traders on both sides propose prices and quantities, and the market institution chooses one price that clears the market: sellers who asked below that price sell, buyers who bid above it buy, and anyone who bid or asked exactly that price takes part. The single-sided and double auctions are drawn on the same axes: with one side fixed, a vertical demand line meets the rising stepped supply curve, and the crossing sets the price, while with both sides active the falling stepped bid curve meets the rising stepped offer curve, and the crossing sets both the price and the quantity that trades.

---

Flashcards for this section are as follows:

- double auction ::@:: Multiple buyers and sellers submit bids and asks, and the market institution chooses one price that clears the market.
- who trades at the clearing price of a double auction ::@:: Sellers who asked below it, buyers who bid above it, and anyone who bid or asked exactly it.
- what the single and double auction curves show ::@:: With one side fixed, a vertical demand line meets the rising stepped supply curve; with both sides active, the falling stepped bid curve meets the rising stepped offer curve, and the crossing sets the price and the traded quantity.

<!-- check: ignore-next-line[header_style]: Walras is a proper noun -->
### Walrasian clearing mechanism

Walras proposed the mechanism by which a double auction clears. An auctioneer announces a tentative price, bidders and sellers state how much they are willing to trade at it, and the auctioneer raises the price while demand exceeds supply and lowers it while supply exceeds demand until the two are equal, at which point the market clears.

---

Flashcards for this section are as follows:

- Walrasian clearing mechanism ::@:: An auctioneer announces a tentative price, traders state the quantities they will trade at it, and the auctioneer raises the price while demand exceeds supply and lowers it while supply exceeds demand until the two are equal.

### limits of the clearing mechanism

The algorithm is not what a real market does. With friction, such as non-linear preferences or trading costs, the clearing problem is NP-hard, and several prices may clear the same market at once. Traders can also deviate by waiting, sealed bids and offers are available, and auctions can be run one at a time, so mispricing may persist. How to design a mechanism that does not is a mechanism-design question.

---

Flashcards for this section are as follows:

- why the clearing algorithm breaks down with friction ::@:: The problem becomes NP-hard, because of non-linear preferences and trading costs, and several prices may clear the same market.
- how real traders deviate from the clearing algorithm ::@:: They wait, they use sealed bids and offers, and auctions are run one at a time.
- what can persist because of that deviation ::@:: Mispricing, which is a mechanism-design question.

## fixing

A _fixing_ is an auction-like mechanism that sets a single reference price rather than allocating an asset, and only a limited number of participants take part. The London fixing members solicit buy and sell orders from clients and set a price that clears demand and supply; for gold the price is set and announced twice a day, at 10:30 and 15:00, and it is the reference price for gold trading. Because a small group sets a price that everyone else relies on, a fixing can be collusive, which is illegal.

---

Flashcards for this section are as follows:

- fixing ::@:: An auction-like mechanism that sets a single reference price instead of allocating an asset.
- who takes part in a fixing ::@:: A limited number of participants, who submit buy and sell orders on behalf of clients.
- how a London fixing sets its price ::@:: Members solicit buy and sell orders from clients and set a price that clears demand and supply.
- how often the gold fixing price is announced, and when ::@:: Twice a day, at 10:30 and 15:00.
- what the gold fixing price is used for ::@:: As a reference price for gold trading.
- why a fixing can be illegal ::@:: A limited group of participants sets a price that others rely on, which can be collusive.

## opening and closing auctions

Stock exchanges hold auctions to start and close a trading day, and the same machinery reopens trading after an interruption. The call auction phase collects quotes and quantities, essentially limit and market orders, and displays only limited information, such as an indicative execution price and quantity rather than the full book, depending on the exchange; it ends at a random time. The price determination phase then determines the price that maximizes the volume traded, and the market balancing phase lets market makers absorb the excess demand or supply at the clearing price.

The opening price is the reference point that starts a trading session, and the closing price is used to compute the net asset values of mutual funds, margin requirements, and mark-to-market flows, to set prices for index inclusion and exclusion, and to execute derivative contracts.

---

Flashcards for this section are as follows:

- three phases of an opening or closing auction ::@:: Call auction, price determination, and market balancing.
- what the call auction phase collects, and what it displays ::@:: It collects quotes and quantities, essentially limit and market orders, and displays only limited information such as an indicative execution price and quantity.
- what the price determination phase determines ::@:: The price that maximizes the volume traded.
- what the market balancing phase does ::@:: Market makers absorb the excess demand or supply at the clearing price.
- what the opening price is used for ::@:: As the reference point that starts a trading session.
- uses of the closing price ::@:: Net asset values of mutual funds, margin requirements, mark-to-market flows, index inclusion and exclusion, and the execution of derivative contracts.

## gaming an auction

Publishing real-time indicative information lets traders game a close auction. The London Stock Exchange publishes that information during its closing auctions, and for less liquid securities the end time is known, so a trader can post and cancel orders to flush out other traders before the end time at no penalty. The result was volatile closings and price inefficiency, and in 2003 a random end time was introduced in response.

Sniping at the close shows up in the data. On the Hong Kong Stock Exchange, whose standard closing call auction ran from 2008 until it was suspended ten months later over suspected manipulation, huge sell orders arrived at 4:09:57 in the afternoon, in the auction's final seconds, and the indicative closing price plunged from 37 dollars to 33 dollars (Park, Suen, and Wan, 2022, Journal of Financial Markets). The attacks clustered around derivative expirations, which supplied the incentive, and prices tended to revert the following day.

---

Flashcards for this section are as follows:

- what makes a close auction gameable ::@:: The exchange publishes real-time indicative information, and for less liquid securities the end time is known.
- how a trader flushes out other traders in a close auction ::@:: By posting and cancelling orders before the end time, which carries no penalty.
- what that gaming produced ::@:: Volatile closings and price inefficiency.
- change introduced by the London Stock Exchange in 2003 ::@:: A random end time for the close auction.
- what sniping at the close looks like in the data ::@:: On the Hong Kong Stock Exchange, huge sell orders arrived at 4:09:57 in the afternoon, in the closing call auction's final seconds, and the indicative closing price plunged from 37 dollars to 33 dollars (Park, Suen, and Wan, 2022, Journal of Financial Markets).
- when the sniping attacks occurred, and what followed ::@:: They clustered around derivative expirations, which supplied the incentive, and prices tended to revert the following day.
- what happened to the standard closing call auction behind this data ::@:: The Hong Kong Stock Exchange ran it from 2008 and suspended it ten months later over suspected manipulation.
