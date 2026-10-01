---
aliases:
  - DNS
  - DNS order
  - NMS IOC
  - do-not-ship
  - do-not-ship order
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/do-not-ship_order
  - language/in/English
---

# do-not-ship order

A _do-not-ship order_ (DNS) carries an instruction that the order must not be routed to another exchange. The instruction holds even where another exchange is offering a better price, and the venue holding the order is not free to send it there regardless.

The instruction removes the routing step and nothing else. A DNS order executes against the venue's own book, and a limit form rests there, both exactly as any other order would. What never happens is the [router](smart%20order%20routing.md) picking it up and carrying it to a second exchange, either when it arrives or at any later point in its life.

The protection Rule 611 gives is a price. A venue receiving a marketable order has to route it to whichever venue holds the best protected quote, and that routing is the only mechanism that gets a customer the market's best price. A do-not-ship order is exempt from the duty, so it may execute at a price the market beat somewhere else. Nothing then requires anyone to send it to the better quote afterwards.

The instruction is one value of the routing decision and it excludes the [intermarket sweep order](intermarket%20sweep%20order.md), which is the other. The price qualifier and the time in force are separate factors, so a do-not-ship instruction attaches to either a limit price or an immediate-or-cancel time. The six order types that combination produces are tabulated in [non-routable order](non-routable%20order.md).

---

Flashcards for this section are as follows:

- overview ::@:: An instruction that the order must not be routed to another exchange, even where a better price is offered there.
- what the instruction does not stop ::@:: Trading on the venue that received the order; it executes and rests there as any other order would.
- what giving up the protection means concretely ::@:: The order may execute at a price the market beat elsewhere, and no rule then requires it to be rerouted to the better quote.
- can a do-not-ship instruction be combined with an intermarket sweep ::@:: No; they are alternative values of the same routing decision.
- what a do-not-ship instruction does combine with ::@:: The price qualifier and the time in force, giving the limit form and the immediate-or-cancel form.

## a do-not-ship limit order

The check a DNS limit order goes through runs in two stages, and the second one decides its fate.

The first stage is ordinary matching. The order takes the liquidity on the local book priced at or better than the protected best offer. That is the best quote on another exchange that is immediately and automatically accessible. A buyer with a limit of 100 dollars takes everything the local book offers at 99 and below. The do-not-ship instruction changes nothing about that.

The second stage looks at the remainder. Filling it would mean trading worse than the protected best offer, which locks or crosses it. The locking and crossing prohibition in Rule 610 stops a venue from quoting a price that does so, and Rule 611 catches the same case for an execution. The venue cannot send the remainder to the better quote, because the instruction forbids it, so the remainder is cancelled. Only the offending part dies. Whatever already traded on the local book stands, and one DNS order can fill half its size and still be cancelled.

When the order is not marketable at all, there is no remainder to test. It rests, on one venue's book and nowhere else, and no router will ever lift it. That is why these orders make liquidity rather than take it.

A resting order is still exposed. Once the market moves away from its price, it becomes a stale quote, and a trader who arrives first takes it for an old price. That race is [quote sniping](quote%20sniping.md), and a do-not-ship order is no more shielded from it than any other resting limit order. DNS limit orders escape it more often than routable limit orders do.

---

Flashcards for this section are as follows:

- the two stages a DNS limit order goes through ::@:: Match against the local book first, taking liquidity at or better than the protected best offer, then check the remainder against that quote.
- what the protected best offer is ::@:: The best quote on another exchange that is immediately and automatically accessible.
- what happens to a remainder that would have to trade worse than the protected best offer ::@:: It is cancelled, since Rule 610 forbids the locked or crossed quote and the instruction forbids the routing that would fix it.
- is the whole order cancelled or only the offending part ::@:: Only the offending part; whatever already traded on the local book stands, so one order can fill half its size and still die.
- what a DNS limit order does when it is not marketable at all ::@:: It rests on one venue's book and nowhere else, making liquidity rather than taking it.
- how DNS limit orders fare against routable limit orders in a sniping race ::@:: DNS limit orders escape more often; routable limit orders rarely escape at all.

## a do-not-ship immediate-or-cancel order

The immediate-or-cancel form runs the same two checks and has two fates where the limit form has three. The missing fate is resting. The order takes what the local book offers at the limit price or better and cancels the remainder in the same instant, with no window in between. The time in force has already settled the question of cancellation, so the instruction has nothing left to settle there.

What the instruction changes is where the remainder would have gone. The order takes local liquidity first, exactly as the limit form does. What is left is cancelled where it stands, instead of being routed to the venue holding the better quote as Rule 611 would otherwise require. No second venue is contacted. The variant named for meeting the national market system this way is a _RegNMS-compliance IOC_, which the New York Stock Exchange calls an NMS IOC.

A limit price is optional throughout. Either way the unfilled part goes untaken, and so does any better price across the market.

---

Flashcards for this section are as follows:

- how many fates a DNS immediate-or-cancel order has, and what they are ::@:: Two: it executes against the local book, and whatever is left over is cancelled.
- why such an order never rests ::@:: The immediate-or-cancel time in force cancels the remainder in the same instant, so there is no window in which it could sit on the book.
- what the do-not-ship instruction actually changes for it ::@:: The fate of the remainder, which is cancelled on arrival instead of being routed to the venue with the better quote.
- whether a DNS immediate-or-cancel order needs a limit price ::@:: No; the instruction works with or without one.
- name of the compliant immediate-or-cancel variant, and its NYSE name ::@:: A RegNMS-compliance IOC, called an NMS IOC on the New York Stock Exchange.
