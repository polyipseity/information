---
aliases:
  - SIP
  - consolidated quotation
  - consolidated tape
  - securities information processor
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/securities_information_processor
  - language/in/English
---

# securities information processor

A _securities information processor_ (SIP) is what makes a fragmented market legible. Every exchange reports its limit-order book and its executed trades to it. It aggregates the reports of all the exchanges and publishes the aggregate to the public.

Nothing trades through it. Its only function is to say what the whole market looks like at a given moment, which no single venue can say for itself.

---

Flashcards for this section are as follows:

- what a securities information processor is ::@:: The intermediary that collects limit-order book and trade data from every exchange, aggregates them, and publishes the result to the public.
- what a securities information processor does and does not do ::@:: It reports what the whole market looks like; no trade executes through it.

## consolidated quotation and consolidated tape

The aggregate arrives in two forms. The _consolidated quotation_ is the limit-order book data: what orders and quotes are available anywhere. A trader needs it to know where liquidity sits. The _consolidated tape_ is the executed trades, with their price and quantity. A trader needs it to know what the market has just traded at.

Aggregating the best bid and the best offer across all the venues produces the National Best Bid and Offer. A fragmented market is quoted against that aggregate rather than against any one venue's book. The spread, and the aggregate that produces it, are described in [bid-ask spread](bid-ask%20spread.md).

---

Flashcards for this section are as follows:

- what each of the two forms of the aggregate is for ::@:: The consolidated quotation tells a trader where liquidity sits, and the consolidated tape tells a trader what the market has just traded at.
- what the consolidated quotation carries ::@:: The limit-order book data: what orders and quotes are available anywhere.
- what the consolidated tape carries ::@:: The executed trades, with price and quantity.
- what a fragmented market is quoted against ::@:: The National Best Bid and Offer, not any single venue's book.

## direct data feeds

Better information and communication technology turned the processor into the slow part of the arrangement. It has to aggregate before it can publish, so it is at least one step behind the exchanges it collects from.

Each exchange then began publishing its raw limit-order book straight to its customers, through what are called _direct data feeds_. They are much faster than the processor's output and much more expensive. What incentive an exchange has to supply one is an open question. The cost produces an uneven playing field, since the traders who can pay for the feed see the market sooner than the traders who cannot. If every trader used a direct feed, the consolidated information would be left with no readers, because nobody would act on it.

---

Flashcards for this section are as follows:

- why the processor became the slow part of the arrangement ::@:: It has to aggregate before it can publish, so it sits at least one step behind the exchanges it collects from.
- what a direct data feed is ::@:: An exchange publishing its raw limit-order book straight to its customers, bypassing the processor.
- two properties of a direct data feed ::@:: Much faster than the processor's output, and much more expensive.
- open question about why an exchange supplies a direct data feed ::@:: What incentive it has to provide one.
- how direct data feeds affect the playing field ::@:: Unevenly, because traders who can pay see the market sooner than traders who cannot.
- what would happen to the consolidated information if every trader used a direct feed ::@:: It would be left with no readers, since nobody would act on it.
