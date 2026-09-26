---
aliases:
  - IOC order
  - immediate-or-cancel order
  - phantom liquidity
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/immediate-or-cancel_order
  - language/in/English
---

# immediate-or-cancel order

An _immediate-or-cancel (IOC)_ order must be filled immediately or cancelled. An IOC limit buy for 500 shares at \$50 against a book with 200 shares at \$50.00 fills 200 and cancels the remaining 300.

---

Flashcards for this section are as follows:

- what an IOC order requires ::@:: Immediate execution or cancellation.
- what "immediate" means in IOC ::@:: Filled at submission against available liquidity; any remainder is cancelled.

<!-- check: ignore-next-line[header_style]: IOC is an acronym -->
## IOC and phantom liquidity

High-frequency traders use IOC orders to probe the book without committing. Two equally fast rivals want to buy 100 units at \$115 immediately, but \$116 is too expensive, and neither wants to commit to a standing limit order due to price risk. A market order commits at an uncertain price; a standing limit order can be picked off; an IOC takes what is available and disappears. The share of IOC orders has grown since the 2000s (Cao et al., 2022, _Journal of Financial Economics_).

Why not place a marketable limit and cancel it manually? A marketable limit takes liquidity the moment it arrives, and at HFT speed a manual cancel comes too late. IOC does both at once.

_Phantom liquidity_ is a quote that appears in the LOB data feed but disappears when an order arrives to take it. Speed differences cause it, in data feeds, processing, and order placement. NYSE runs two data access types: a direct data feed (raw, fast) and a consolidated data feed (aggregate, slow). Flash Boys by Michael Lewis (2014) describes these speed advantages.

---

Flashcards for this section are as follows:

- why high-frequency traders use IOC orders ::@:: To probe the book without committing, avoiding the risk of a standing limit order being picked off.
- why two equally fast IOC rivals each execute first with probability one half ::@:: They are equally fast, so arrival at the venue is a tie broken at random.
- what phantom liquidity is ::@:: A quote that appears in the LOB data feed but disappears when an order arrives to take it.
- what causes phantom liquidity ::@:: Speed differences in data feeds, processing, and order placement.
- two types of data access at NYSE ::@:: Direct data feed (raw, fast) and consolidated data feed (aggregate, slow).
- what "Flash Boys" (Michael Lewis, 2014) is about ::@:: High-frequency trading and the speed advantages that produce phantom liquidity.
