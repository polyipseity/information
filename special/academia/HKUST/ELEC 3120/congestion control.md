---
aliases:
  - ELEC 3120 congestion control
  - ELEC3120 congestion control
  - HKUST ELEC 3120 congestion control
  - HKUST ELEC3120 congestion control
  - congestion control
  - congestion control algorithm
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/congestion_control
  - language/in/English
---

# congestion control

Congestion control is how a sender decides how much data it may keep in flight on a path whose capacity nothing reports. The algorithm is the rule that sets that window and revises it as evidence arrives.

---

Flashcards for this section are as follows:

- congestion control: what question does a congestion control algorithm answer? ::@:: How large a window the sender may keep in flight over a path whose capacity it cannot see.
- why it cannot be computed: which two quantities does the network never report to the sender? ::@:: Its bandwidth and its round-trip time.
- the moving target: what makes a fixed window wrong? ::@:: The sender's share of the bottleneck depends on the other senders, which start and stop.

## hidden capacity

Three limits make the rule hard to fix. The window can only be inferred from how the network treats the traffic already sent. A sender's share depends on the other senders on the link, so no window stays right for long. Routers also queue rather than drop, so a small overshoot draws no warning.

A path of 50 Mbit/s with a 200 ms round trip needs 1.25 MB in flight to run at full rate, and nothing in the protocol reports that figure. A window of 625 KB, half of what is needed, leaves half the link idle, and only the return of acknowledgements shows that the sender is short. Where a router can hold 625 KB of queue, an extra 100 ms of traffic fits without a drop, so an overshoot of that size draws no warning. The queue holds the surplus instead of dropping it, and that wait is the delay counted under costs of congestion.

---

Flashcards for this section are as follows:

- unseen capacity: what must the sender infer, since the network will not report it? ::@:: The right window size, from how its packets are treated on the way.
- shared bottleneck: what happens to a sender's share when another sender stops? ::@:: It grows, so the window has to be discovered again rather than set once.
- the window for a rate: how much data must be in flight to send at $10\text{ Mbit/s}$ over a path whose round trip is $50\text{ ms}$? ::@:: $10\text{ Mbit/s} \times 0.05\text{ s} = 500\,000$ bits, which is $62{,}500$ bytes.
- the full window: a path carries $50\text{ Mbit/s}$ and its round trip is $200\text{ ms}$; how much data must be in flight to run it at full rate? ::@:: $50\text{ Mbit/s} \times 0.2\text{ s} = 10$ Mbit $= 1.25$ MB, a figure no part of the protocol hands to the sender.
- a queue that hides overshoot: a $50\text{ Mbit/s}$ path lets a router hold $625$ KB of queue; how much extra traffic does that absorb, and what does the sender learn? ::@:: $625\text{ KB} / 50\text{ Mbit/s} = 0.1$ s, so $100$ ms of traffic fits without a drop and an overshoot of that size returns no warning.

## signal from the network

The only feedback is loss. A drop is evidence of sending too fast, so the window shrinks. A long stretch without a drop is evidence of sending short of the path's capacity, so the window grows. A timeout counts as worse evidence than duplicate acknowledgements, since it suggests an overshoot big enough to lose many packets at once.

The loss rate also says how far past the capacity the sender is running. One loss in every 100 segments means the offered load runs about one segment in a hundred past the capacity of the path; one loss in 10,000 means it runs past by a hundredth of a per cent. The [Mathis equation](Mathis%20equation.md) turns that rate into a sending rate, and since the loss probability enters under a square root, quadrupling the loss rate from 1 segment in 100 to 1 in 25 halves the throughput the path delivers.

---

Flashcards for this section are as follows:

- what loss means: what does a dropped packet tell the sender? ::@:: That it is sending faster than the path can carry.
- the surplus load: a $50\text{ Mbit/s}$ path reports one loss in every $100$ segments; how much load does the sender offer past the capacity of the path? ::@:: $1/100 = 1\%$ of $50\text{ Mbit/s} = 0.5\text{ Mbit/s}$, so about $50.5\text{ Mbit/s}$ in total.
- what a quiet path means: what does a long stretch without loss tell the sender? ::@:: That it is probably sending below the path's capacity, so the window may grow.
- timeout against duplicate acknowledgements: why does a timeout draw a harsher response than three duplicate acknowledgements? ::@:: A timeout suggests a large overshoot and many lost packets, so the sender starts over rather than halving.
- the rare loss: a $50\text{ Mbit/s}$ path reports one loss in every $10{,}000$ segments; how far past the capacity of the path does the sender run? ::@:: $1/10{,}000 = 0.01\%$ of $50\text{ Mbit/s} = 5\text{ kbit/s}$, so about $50.005\text{ Mbit/s}$ in total.
- the square root: a path reports one loss in every $100$ segments, and the loss rate then quadruples to one loss in $25$; how does the loss probability enter the sending rate, and what happens to throughput? ::@:: It enters under a square root, and $\sqrt{4} = 2$, so the quadrupling halves the throughput the path delivers.

## algorithm space

An algorithm picks two rules: how the window grows while packets survive, and how far it falls on a loss. Each rule is either additive, a fixed step, or multiplicative, a fixed factor, so the space holds four families:

- additive increase with additive decrease (AIAD): step up, step down
- additive increase with multiplicative decrease (AIMD): step up, halve
- multiplicative increase with additive decrease (MIAD): double, step down
- multiplicative increase with multiplicative decrease (MIMD): double, halve

From a window of $10$ maximum segment sizes, additive increase reaches $11$ after a round trip without loss where multiplicative increase reaches $20$, and additive decrease leaves $9$ after a loss where multiplicative decrease leaves $5$. Only AIMD finds the capacity of a path gently enough not to overshoot it, and hands a share back in proportion to what the flow held.

Over further rounds the two increases separate: from the same window of $10$, additive increase gives $12$, $13$, and $14$ after 2, 3, and 4 round trips, while multiplicative increase gives $40$, $80$, and $160$.

Additive increase on a path with a 100 ms round trip adds one maximum segment size every 100 ms, so a sender at 100 maximum segment sizes needs 100 round trips, 10 s, to reach 200. A multiplicative decrease at that window removes 50 maximum segment sizes at once, which undoes 5 s of climbing in a single step.

---

Flashcards for this section are as follows:

- the two rules: which two decisions define a window-based congestion control algorithm? ::@:: How the window grows without loss, and how far it falls on a loss.
- the four families: which four rule pairs fill the space of a window-based algorithm, and by which acronyms are they known? ::@:: Additive increase with additive decrease (AIAD), additive increase with multiplicative decrease (AIMD), multiplicative increase with additive decrease (MIAD), and multiplicative increase with multiplicative decrease (MIMD).
- additive growth: what does additive increase do per round trip? ::@:: It adds a fixed amount, one maximum segment size in the Transmission Control Protocol (TCP) case.
- multiplicative growth: what does multiplicative increase do per round trip? ::@:: It doubles the window.
- multiplicative decrease in numbers: a sender holds $10$ maximum segment sizes and a packet is lost; what does multiplicative decrease give it? ::@:: $10 / 2 = 5$ maximum segment sizes.
- growth over four round trips: a sender holds $10$ maximum segment sizes and no loss is reported for 4 round trips; what does additive increase give it? ::@:: $10 + 4 = 14$ maximum segment sizes, one more for each round trip.
- the rate of increase against the rate of decrease: a sender on a path with a $100\text{ ms}$ round trip holds $100$ maximum segment sizes; how long does additive increase take to reach $200$, and how much does a multiplicative decrease remove? ::@:: $200 - 100 = 100$ round trips of $100\text{ ms}$, $10$ seconds, to reach $200$, while the halving removes $100 / 2 = 50$ maximum segment sizes at once, which undoes $5$ seconds of growth.
- additive decrease in numbers: a sender holds $10$ maximum segment sizes and a packet is lost; what does additive decrease give it? ::@:: $10 - 1 = 9$ maximum segment sizes.
- multiplicative growth over four round trips: a sender holds $10$ maximum segment sizes and no loss is reported for 4 round trips; what does multiplicative increase give it? ::@:: $10 \times 2 = 20$, then $40$, $80$, and $160$ maximum segment sizes after 2, 3, and 4 round trips.
- growth in a second: a sender holds $10$ maximum segment sizes on a path whose round trip is $100\text{ ms}$; how much does additive increase gain in one second, and how much does multiplicative increase gain? ::@:: $1\text{ s} / 100\text{ ms} = 10$ round trips, so additive increase gains $10$ maximum segment sizes a second; multiplicative increase goes $10 \times 2^{10} = 10\,240$, a gain of $10{,}230$ in its first second.
- giving a share back in proportion: which decrease rule returns a flow's share in proportion to the share it held? ::@:: Multiplicative decrease, which halves the window; an additive decrease removes the same fixed step whatever the window, so it hands back a larger fraction of a small share than of a large one.

### convergence

Chiu and Jain asked in 1989 what a good algorithm must do, and named four properties: use the available capacity, share it fairly, converge to that sharing without oscillating, and work from the ends alone. The four families differ in what one loss cycle does to the gap between two senders' shares:

- AIAD leaves the gap alone: adding and subtracting the same step moves both windows together, so an unfair pair stays unfair.
- MIAD widens it: doubling doubles the gap, and the fixed step down never closes it.
- MIMD swings it: halving halves the gap, doubling opens it again, and the pair never settles.
- AIMD closes it: the halving halves the gap and the additive step leaves it unchanged, so every loss brings the pair nearer the equal share.

Only AIMD gives all four properties.

Two senders on a link that carries 100 packets per round trip hold 60 and 40, so the pair sits exactly at the capacity of the link. Each sender adds a packet per round trip, so after 20 round trips they hold 80 and 60, which is more than the link carries, and the link drops packets. A multiplicative decrease halves both windows and gives 40 and 30, so the gap between the two senders falls from 20 packets to 10 while the link carries 70 packets and drops nothing. The pair climbs again, and every loss halves the gap a second time, so the two shares end up within a packet or two of the equal share of 50 packets each.

Efficiency holds while the pair fills the link, fairness once both hold the equal share, and convergence is the halving closing the gap. Distributedness holds because each sender reacts only to its own losses, and neither needs to know what the other is doing.

---

Flashcards for this section are as follows:

- four properties: which four properties did Chiu and Jain require of a congestion control algorithm in 1989? ::@:: Efficiency, fairness, convergence, and distributedness.
- distributedness: what does the distributedness property forbid? ::@:: Any need for the users or the network to cooperate; the algorithm must work from the ends alone.
- what each family does to the gap: a pair of senders is unfair, and one cycle is one loss and the recovery after it; what does the gap do under AIAD, MIAD, MIMD, and AIMD? ::@:: AIAD leaves it unchanged, since both windows move by the same step; MIAD doubles it; MIMD halves it and opens it again, so the pair oscillates; AIMD halves it and keeps it closed.
- the family the properties select: of additive increase with additive decrease, additive increase with multiplicative decrease, multiplicative increase with additive decrease, and multiplicative increase with multiplicative decrease, which family satisfies all four required properties? ::@:: Additive increase with multiplicative decrease (AIMD), the only one of the four.
- the senders climb: two senders hold $60$ and $40$ packets on a link that carries $100$ packets per round trip, and each adds one packet per round trip; what do they hold after $20$ round trips? ::@:: $60 + 20 = 80$ and $40 + 20 = 60$ packets, $140$ in total, which is more than the link carries, so the link drops packets.
- the gap closing: two senders' shares differ by $20$ packets, and each loss halves both windows; how does the gap shrink and where does it stop? ::@:: $20 / 2 = 10$ packets, then $10 / 2 = 5$, so the two shares end within a packet or two of $100 / 2 = 50$ packets each.

## costs of congestion

Congestion costs more than the packets it drops. Where routers have room to queue, delay climbs as the arrival rate approaches capacity. Where buffers are small, a retransmission takes the place of a packet that could have been delivered, so goodput falls while the offered load rises. A packet dropped late in its journey has already used capacity on every link behind it, and none of that work delivers anything. Another flow's retransmissions can crowd a flow's packets out of a shared queue until its throughput falls to zero.

At 50 Mbit/s, every 625 KB that queues ahead of a packet adds 100 ms to its delay, so a queue holding a quarter of a second of traffic adds 250 ms to the last packet in it. Every packet the flow sends afterwards pays that delay, and so do the packets of the flows sharing the queue. A window of 2 MB on that path exceeds the 1.25 MB it takes to fill the link by 750 KB, so a queue of 750 KB forms in front of the bottleneck and every packet behind it waits 120 ms. A window of 1.25 MB leaves the queue empty.

---

Flashcards for this section are as follows:

- queueing cost: what happens to delay as the arrival rate approaches a link's capacity? ::@:: It grows large, since the queue in front of the link lengthens.
- retransmission cost: with limited buffers, what does a retransmission displace? ::@:: A packet that could have been delivered, so goodput falls as more data is offered.
- upstream waste: why is a packet dropped late more expensive than one dropped early? ::@:: It has already used capacity on every link it crossed, and none of that work delivers anything.
- starvation: how can one flow be starved by another? ::@:: If the other flow's retransmissions crowd its packets out of a shared queue, its throughput can fall to zero.
- the queue above the product: a sender holds $2$ MB in flight on a $50\text{ Mbit/s}$ path whose round trip is $200\text{ ms}$; how much queue forms and what does it add? ::@:: $2\text{ MB} - 1.25\text{ MB} = 750$ KB of queue, and $750\text{ KB} / 50\text{ Mbit/s} = 0.12$ s, which adds $120$ ms to every packet that crosses it.
- the price of one queue: a $50\text{ Mbit/s}$ path queues $625$ KB ahead of a packet, and another holds a quarter of a second of traffic; how much delay does each add? ::@:: $625\text{ KB} / 50\text{ Mbit/s} = 0.1$ s, so $100$ ms; a quarter of a second is $50\text{ Mbit/s} \times 0.25\text{ s} = 1.5625$ MB of traffic and adds $250$ ms.

## approaches

Reno and its successor NewReno are the classic algorithms. CUBIC is the default on Linux and macOS, and its [CUBIC TCP](CUBIC%20TCP.md) curve replaces the linear climb of Reno. BBR (Bottleneck Bandwidth and Round-trip propagation time) replaces the loss signal with a measurement of the bottleneck bandwidth and the minimum round trip, so it paces the sender near the capacity of the path instead of probing for it by overrunning the queue. PCC, LEDBAT, Compound, FastTCP, DCTCP, and TIMELY cover other settings, such as datacenters, satellite links, and peer-to-peer transfers.

---

Flashcards for this section are as follows:

- classic algorithms: which two algorithms are the originals of Transmission Control Protocol (TCP) congestion control? ::@:: TCP Reno and NewReno.
- default on Linux and macOS: which congestion control algorithm do Linux and macOS ship as the default? ::@:: CUBIC.
- datacenter algorithms: which algorithms were designed for datacenters? ::@:: Data Center TCP (DCTCP) and TIMELY, alongside network-assisted schemes such as random early detection (RED).
- peer-to-peer: which algorithm was designed for peer-to-peer traffic? ::@:: Low Extra Delay Background Transport (LEDBAT), used by BitTorrent.
- measurement instead of loss: which algorithm replaces the loss signal with a measurement of the bottleneck bandwidth and the minimum round trip? ::@:: Bottleneck Bandwidth and Round-trip propagation time (BBR), which paces the sender near the capacity of the path instead of probing for it by overrunning the queue.
- curve against line: how does the growth of CUBIC differ from that of the Reno algorithm? ::@:: CUBIC grows along a curve, where the Reno algorithm climbs linearly.
