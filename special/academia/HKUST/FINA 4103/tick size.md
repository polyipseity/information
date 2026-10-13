---
aliases:
  - minimum tick
  - price tick
  - sub-penny rule
  - tick size
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/tick_size
  - language/in/English
---

# tick size

A _tick_ is one of the discrete numbers a price is allowed to take, and the _tick size_ is the distance between neighbours.

In theory a price takes any value in $p \in \mathbb{R}_+$, but an algorithm cannot match against a continuum. The discreteness is a property of the matching engine rather than of the asset, and the grid is imposed by the venue. In a market that quotes in cents the tick size is one cent, so the price domain is the countable set $p \in \{p_0, p_1, p_2, \ldots, p_n\}$, with the first three ticks at 0.00, 0.01, and 0.02 dollars.

---

Flashcards for this section are as follows:

- what a tick is ::@:: One of the discrete numbers a price may take, with the tick size the distance between neighbours.
- why the price domain is discrete ::@:: A matching algorithm cannot match against a continuum, so the venue imposes a grid.

## minimum tick size

Rule 612 of [Regulation NMS](Regulation%20NMS.md), the sub-penny rule, fixes the minimum tick at one cent. A limit order cannot quote a price off the grid, so 101.255 dollars is not a price that can be sent.

A common grid is what makes two venues quoting the same stock comparable, so a trader can recognise the best price in the market. It is what allows the [order protection rule](trade%20through.md) to be checked at all. Why the rule is needed, and what would happen on a finer grid, is an open question.

---

Flashcards for this section are as follows:

- minimum tick size fixed by Rule 612 ::@:: One cent.
- price a limit order cannot quote under the sub-penny rule ::@:: 101.255 dollars, which is off the grid.
- what a common grid buys ::@:: Two venues quoting the same stock become comparable, and the order protection rule can be checked at all.
- open question about the sub-penny rule ::@:: Why the rule is needed, and what a finer grid would do.
