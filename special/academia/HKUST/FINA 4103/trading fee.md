---
aliases:
  - inverted maker-taker fee
  - make and take fee
  - maker-taker fee
  - order-routing fee
  - rebate
  - trading fee
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/trading_fee
  - language/in/English
---

# trading fee

An exchange earns from the orders that cross its book, and it charges the two sides differently. A liquidity-taking order pays a take fee $f_{\mathrm{take}}$. A liquidity-making order receives a rebate $f_{\mathrm{make}} < f_{\mathrm{take}}$. The exchange's profit on the pair is $f_{\mathrm{take}} - f_{\mathrm{make}}$. The New York Stock Exchange, for instance, charged $f_{\mathrm{take}} = \text{¢}0.21$ and $f_{\mathrm{make}} = \text{¢}0.13$ per share.

The exchange sets those fees, not the regulator, and the rulebook takes no account of them. Rule 611 can force an order onto a venue that charges for the trade, and the rule never mentions the charge.

---

Flashcards for this section are as follows:

- the take fee, the make rebate, and the exchange's share ::@:: A take fee paid by liquidity-taking orders, a smaller rebate received by liquidity-making orders, and the difference kept by the exchange.
- take and make fees at the New York Stock Exchange ::@:: Take 0.21 cents and make 0.13 cents per share.
- who sets the fees, and whether the rulebook accounts for them ::@:: The exchange sets them; the rulebook takes no account of them at all.
- exchange profit on a matched take and make ::@:: $f_{\mathrm{take}} - f_{\mathrm{make}}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- relation between the take fee and the make rebate ::@:: The rebate is always the smaller of the two, $f_{\mathrm{make}} < f_{\mathrm{take}}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## make and take fees

Exchanges differ in the level they charge and in the structure they use. The usual structure charges the taker and pays the maker. An inverted structure does the reverse: the exchange pays the taker and charges the maker, so liquidity-taking becomes the profitable side of the book.

Fees change what an order is. The fee schedule is a statement about which behaviour the venue wants to see.

---

Flashcards for this section are as follows:

- what an inverted maker-taker structure does ::@:: Pays the taker rather than the maker.
- two ways exchanges differ in their fees ::@:: The level they charge, and the structure they use.
- what a venue's fee schedule reveals about the venue ::@:: Which behaviour it wants: taking liquidity or making it.

## order-routing fees

A routed order carries a second fee, the routing fee $f_{\mathrm{route}}$. The exchange that does the routing charges it, and Rule 610 caps it at 0.3 cents per share. The New York Stock Exchange charges exactly that cap, so it loses nothing when it routes an order out.

Rule 610 is the access rule, and it covers liquidity-provision orders, the ones that rest. So an order posted to make liquidity can be sent to another exchange. A make order at the New York Stock Exchange that goes to Nasdaq arrives there as a taker. It pays the take fee instead of receiving the rebate. The fee follows the role, not where the order was posted.

---

Flashcards for this section are as follows:

- what an order-routing fee is ::@:: A fee charged by the exchange that routes the order out.
- symbol for the order-routing fee ::@:: $f_{\mathrm{route}}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- cap Rule 610 places on the routing fee ::@:: 0.3 cents per share.
- routing fee the New York Stock Exchange charges ::@:: Exactly that cap, so it loses nothing when it routes an order out.
- how Rule 610 blurs making and taking ::@:: A make order routed to another venue arrives as a taker there, and pays the take fee instead of receiving the rebate.
- what the fee follows ::@:: The role the order plays on arrival, not where it was posted.

## price improvement from routing

Price improvement is measured against the best quote available when the order arrived. Li, Ye, and Zheng (2022, _Journal of Financial Economics_) report it for routed orders on the New York Stock Exchange.

| Price improvement (dollars) | Plain market | Plain IOC | DAY limit | Reserve |
| --- | --- | --- | --- | --- |
| None | 26.99% | 0.00% | 77.49% | 79.51% |
| 0.01 | 48.58% | 70.49% | 12.93% | 9.43% |
| 0.02 | 13.87% | 12.00% | 2.74% | 3.52% |
| 0.03 | 5.11% | 4.52% | 1.35% | 1.68% |
| 0.04 | 2.09% | 2.46% | 0.96% | 1.32% |
| 0.05 | 0.98% | 1.59% | 0.95% | 1.33% |
| 0.06 | 0.52% | 1.00% | 0.34% | 0.63% |
| 0.07 | 0.32% | 0.81% | 0.26% | 0.36% |
| 0.08 | 0.22% | 0.69% | 0.21% | 0.21% |
| 0.09 | 0.15% | 1.13% | 0.16% | 0.15% |
| 0.10 | 0.04% | 0.66% | 0.07% | 0.05% |
| 0.10 or more | 1.12% | 4.65% | 2.56% | 1.82% |

48.58% of routed plain market orders and 70.49% of routed plain immediate-or-cancel orders filled exactly a cent better than the quote they chased. Liquidity-making orders get nothing. 77.49% of routed day limit orders and 79.51% of routed reserve orders received no improvement at all, and they still paid the routing fee.

---

Flashcards for this section are as follows:

- what price improvement is measured against ::@:: The best quote available when the order arrived.
- what routing is worth to each side ::@:: A liquidity-taking order usually fills better than the quote it chased; a liquidity-making one usually fills at that same quote.
- routed day limit orders receiving no price improvement ::@:: 77.49%, against 79.51% for routed reserve orders.
- what a routed liquidity-making order still pays ::@:: The routing fee, with no price improvement in return.
- what sets the price of routing ::@:: The fee schedule alone: Reg NMS does not take the fees into account.
