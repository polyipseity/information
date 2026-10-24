---
aliases:
  - ELEC 3120 TCP congestion control
  - ELEC3120 TCP congestion control
  - HKUST ELEC 3120 TCP congestion control
  - HKUST ELEC3120 TCP congestion control
  - TCP Reno
  - TCP congestion control
  - congestion avoidance
  - congestion control
  - congestion window
  - fast recovery
  - slow start
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/TCP_congestion_control
  - language/in/English
---

# TCP congestion control

Congestion control keeps a sender from pushing more traffic into the network than the path can carry. Nothing tells the sender the path's capacity, so it reads that capacity from the acknowledgements: quick ones mean room for more, ones that stop mean the path is overloaded. The sender keeps the estimate in a congestion window and revises it on each event.

---

Flashcards for this section are as follows:

- core idea: what does congestion control limit a sender to? ::@:: What the path can carry.
- who infers the limit: what does the sender use to estimate the path's room? ::@:: The acknowledgements it receives.
- quick acknowledgements: what do acknowledgements that keep returning quickly tell the sender? ::@:: That the path has room to send more.

## congestion window

The congestion window $CWND$ is the sender's estimate of how much it may have outstanding. Flow control supplies a separate receive window, which bounds the connection from the receiver side. The sending window is $\min(RWND, CWND)$ (see [sending window](flow%20control%20(data).md#sending%20window)). The sender also keeps a slow-start threshold, which marks where the window stops doubling.

On a path of 50 Mbit/s with a 200 ms round trip, the [bandwidth-delay product](bandwidth-delay%20product.md) is 1.25 MB, so a window of 1.25 MB keeps the link at its full rate. Cut the window to 625 KB and the same path runs at 25 Mbit/s, because the sender has nothing to send during the second half of every round trip. That window holds 856 segments of 1460 bytes, each replaced as its acknowledgement returns, so a segment goes on the wire every 0.23 ms, which is 50 Mbit/s.

---

Flashcards for this section are as follows:

- congestion window: what does $CWND$ estimate? ::@:: How much the sender may have outstanding, given the network's capacity.
- starting value: what value does $CWND$ start from? ::@:: Four maximum segment sizes.
- slow-start threshold: what does $ssthresh$ decide? ::@:: When the window stops doubling and starts growing linearly.
- the rate a window sustains: a sender holds $1.25$ MB in flight on a path whose round trip is $200\text{ ms}$; what rate does that window sustain? ::@:: $1.25\text{ MB} / 0.2\text{ s} = 6.25\text{ MB/s}$, and $6.25 \times 8 = 50$ Mbit/s.
- the segments in a window: a window of $1.25$ MB holds how many segments of $1460$ bytes? ::@:: $1.25\text{ MB} / 1460\text{ bytes} \approx 856$ segments.
- network side against receiver side: the congestion window $CWND$ and the receive window $RWND$ both bound one connection; which one comes from which side? ::@:: $CWND$ from the network side and $RWND$ from the receiver side.
- the sending window: how is the sending window formed from the receive window $RWND$ and the congestion window $CWND$? ::@:: As $\min(RWND, CWND)$, the smaller of the two.
- a window that halves the rate: a path of $50\text{ Mbit/s}$ with a $200\text{ ms}$ round trip carries $1.25$ MB in flight at full rate; what rate does a window of $625$ KB sustain? ::@:: $625\text{ KB} / 0.2\text{ s} = 3.125\text{ MB/s} = 25$ Mbit/s, half the rate of the full window.
- the gap between segments: a window of $1.25$ MB holds $856$ segments on a path whose round trip is $200\text{ ms}$; how often does the sender put a segment on the wire? ::@:: $0.2\text{ s} / 856 \approx 0.23$ ms, and $1460\text{ bytes} / 0.23\text{ ms} \approx 50$ Mbit/s.

## slow start

Slow start grows the window exponentially. The sender starts at $CWND = 4$ MSS and adds one MSS per acknowledgement. A round trip returns about as many acknowledgements as the window holds segments, so the window doubles once per round trip. Once $CWND$ reaches the slow-start threshold, the window grows linearly instead. The name is historical, since senders used to open with a window so large that starting small was the slower option.

Starting from 4 MSS, the window holds 8, 16, 32, 64, 128, and 256 MSS after 1, 2, 3, 4, 5, and 6 round trips. A path of 50 Mbit/s with a 200 ms round trip needs 1.25 MB in flight, which is 856 MSS of 1460 bytes each, so a sender in slow start passes that mark on its 8th round trip, when the window reaches 1024 MSS. Those 8 round trips take 1.6 s on that path.

---

Flashcards for this section are as follows:

- slow start growth: how much does $CWND$ rise per acknowledgement? ::@:: One MSS per acknowledgement.
- doubling per round trip: $CWND$ grows by one MSS for each acknowledgement; why does that double the window once per round trip? ::@:: A round trip brings back about as many acknowledgements as the window holds segments.
- leaving slow start: once $CWND$ reaches the slow-start threshold, what happens to the window's growth? ::@:: It grows linearly instead of doubling.
- the window after four round trips: a sender starts slow start with a window of $4$ MSS; what does it hold after 4 round trips? ::@:: $4 \times 2^{4} = 64$ MSS, one doubling per round trip.
- the name slow start: why is exponential growth from four maximum segment sizes (MSS) called slow start? ::@:: Senders once opened with a window so large that starting small was the slower option.
- passing the bandwidth-delay product: a $50\text{ Mbit/s}$ path with a $200\text{ ms}$ round trip needs $856$ maximum segment sizes (MSS) in flight, and slow start starts at $4$ MSS and doubles every round trip; on which round trip does the window pass $856$ MSS, and how long do those round trips take? ::@:: $4 \times 2^{8} = 1024$ MSS on the 8th round trip, the first past $856$, and $8 \times 200\text{ ms} = 1.6$ s.

## congestion avoidance

Congestion avoidance grows the window linearly once $CWND$ has reached the slow-start threshold. Each acknowledgement adds $MSS/CWND$ to $CWND$, so the window rises by about one MSS per round trip instead of doubling. While no loss is reported the window keeps growing, which is how a sender finds room it did not know it had.

From a window of 512 MSS, adding one MSS per round trip reaches 856 MSS in 344 round trips, 69 s on a path with a 200 ms round trip and spent entirely below the rate the path could carry.

---

Flashcards for this section are as follows:

- growth per acknowledgement: how much does $CWND$ rise per acknowledgement during congestion avoidance? ::@:: $MSS/CWND$, about one MSS per round trip.
- why it is linear: why does congestion avoidance add $MSS/CWND$ per acknowledgement instead of one MSS? ::@:: The growth of one MSS per round trip is spread over every acknowledgement of the window.
- probing for room: what does the window do while no loss is reported? ::@:: It keeps growing, looking for more room a round trip at a time.
- a slow climb to $856$ MSS: from $512$ maximum segment sizes (MSS), congestion avoidance adds one MSS per round trip; how many round trips reach $856$ MSS, and how many seconds on a path whose round trip is $200\text{ ms}$? ::@:: $856 - 512 = 344$ MSS at one MSS per round trip, so $344$ round trips, and $344 \times 200\text{ ms} = 68.8\text{ s} \approx 69$ s.

### sawtooth

Plotted against time, the window climbs exponentially during slow start, then linearly by one MSS per round trip, then drops and climbs again: a repeating sawtooth. Halving on a duplicate acknowledgement keeps the drop shallow. The linear climb then holds the window just below the point where the path last dropped a packet.

The slope of the linear part follows the round trip: a sender on a 10 ms path gains 100 MSS every second, while one on a 100 ms path gains 10. Two flows on one link therefore grow at different rates, and the faster one reaches the link's capacity first and takes the larger share.

A connection that leaves slow start at 20 MSS climbs to 40 MSS in 20 round trips and then loses a segment, so the trace runs 20, 40, 20, 40, and each climb takes 2 s on a path with a 100 ms round trip.

The cycle runs between $W/2$ and $W$, so the average window is $3W/4$ and the average rate three quarters of the peak, while the only loss is the path overflowing. A queue moves the peak without moving the bottleneck: a deeper buffer lets the window climb past the bandwidth-delay product before a drop, so $W$ grows with the buffer. The bottleneck's own rate then also caps the average, and the surplus stands in the queue as delay.

The trace shows a drop at every loss. <p> ![congestion window against time: a rising line through the slow-start region up to the threshold, then a slower rise in the congestion-avoidance region, with a drop to four segments at each timeout and a halving at each duplicate acknowledgement](../../../../archives/Wikimedia%20Commons/TCP%20Slow-Start%20and%20Congestion%20Avoidance.svg)

---

Flashcards for this section are as follows:

- the sawtooth: what does a plot of the congestion window against time look like over a long Transmission Control Protocol (TCP) connection? ::@:: An exponential rise, then a linear climb, then a drop, repeating.
- the climb: which growth does the long linear part of the sawtooth correspond to? ::@:: Congestion avoidance, one maximum segment size per round trip.
- what the shape means: what does the window doing most of its work near the drop point tell you about the path? ::@:: The connection runs at about the capacity where the path starts losing packets.
- one cycle of the sawtooth: a connection leaves slow start at $20$ MSS, climbs to $40$ MSS, loses a segment, and halves back to $20$ MSS; how long does the climb take? ::@:: $40 - 20 = 20$ MSS at one MSS per round trip, so $20$ round trips, and $20 \times 100\text{ ms} = 2$ s.
- the window against time: what does a trace of the congestion window against time show, and what happens at each drop? <p> ![congestion window against time: a rising line through the slow-start region up to the threshold, then a slower rise in the congestion-avoidance region, with a drop to four segments at each timeout and a halving at each duplicate acknowledgement](../../../../archives/Wikimedia%20Commons/TCP%20Slow-Start%20and%20Congestion%20Avoidance.svg) ::@:: A rise through slow start, then a slower straight climb through congestion avoidance, with a drop at every timeout or repeated acknowledgement.
- the slope of the climb: congestion avoidance adds one maximum segment size (MSS) per round trip; how fast does the window grow on paths whose round trips are $10\text{ ms}$ and $100\text{ ms}$? ::@:: $1\text{ s} / 10\text{ ms} = 100$ round trips, so $100$ MSS per second; $1\text{ s} / 100\text{ ms} = 10$ round trips, so $10$ MSS per second.
- average over a cycle: a sawtooth runs between $W/2$ and $W$; what is the average window, and what is the average rate when the only loss is the path overflowing? ::@:: $3W/4$, so three quarters of the peak, $\frac{3}{4} \cdot W/RTT$.
- what a queue does to the peak: how does a queue change the peak window, and what then caps the average rate? ::@:: The buffer lets the window climb past the bandwidth-delay product, so the peak grows with the queue while the bottleneck serves no faster, and the average rate is capped by the bottleneck's own rate.

<!-- check: ignore-next-line[header_style]: AIMD is an acronym -->
### AIMD convergence

Additive increase is cautious on the way up and multiplicative decrease is abrupt on the way down. Each flow gives back a share proportional to what it held, so a heavy flow yields the most room.

A flow that holds 2 MB of the window when it loses a segment falls to 1 MB and gives 1 MB back to the path, while a flow holding 0.5 MB falls to 0.25 MB and gives 0.25 MB back. The heavy flow returns four times as much room, so the light flow can climb back into the capacity the heavy one vacated. One sender on a link holds 60 packets and another 40; after a loss the first falls to 30 and the second to 20, so the heavy sender returns 30 packets of room and the light one 20.

---

Flashcards for this section are as follows:

- cautious and abrupt: which direction of additive increase with multiplicative decrease is deliberately the slower one? ::@:: Growth is slow, one maximum segment size per round trip, and reduction is abrupt.
- why halve: what does halving on loss do for the other flows on the path? ::@:: It returns room in proportion to what the flow held, so a heavy flow gives back the most.
- careless alternative: what would happen with a large initial window and no reduction? ::@:: The flows would push the network back into the collapse that congestion control was introduced to end.
- two senders: what does additive increase with multiplicative decrease do to two flows sharing one link? ::@:: It brings their shares toward equality, since the larger share loses more on each reduction.
- the room a heavy flow returns: two flows hold $2$ MB and $0.5$ MB when a loss halves both; how much room does each return? ::@:: $2\text{ MB} / 2 = 1$ MB returned and $0.5\text{ MB} / 2 = 0.25$ MB returned, so $1 / 0.25 = 4$ times as much comes from the heavy flow.

## fast recovery

Fast recovery replaces the return to slow start when duplicate acknowledgements, rather than a timeout, report the loss. On the third one the sender halves the slow-start threshold and sets $CWND$ to that threshold plus the three segments the duplicate acknowledgements account for. The window drops by about half instead of to one MSS. Each further duplicate acknowledgement adds one MSS while the missing segment is retransmitted.

A sender whose window was 20 MSS when the third duplicate acknowledgement arrived sets the slow-start threshold to 10 MSS and the congestion window to 13 MSS, so the loss costs 7 MSS where a return to slow start would cost 19. From 13 MSS the window climbs back to 20 at one MSS per round trip, which takes 7 round trips, 700 ms on a path with a 100 ms round trip.

---

Flashcards for this section are as follows:

- fast recovery values: the third duplicate acknowledgement arrives while the window is $CWND$; what does the sender set? ::@:: The slow-start threshold to $CWND/2$, and the congestion window to that plus $3$ MSS.
- three segments: why does fast recovery add $3$ MSS to the halved threshold? ::@:: Each duplicate acknowledgement means one more segment has left the network, so the sender counts that room in.
- further duplicate acknowledgements: what does the sender do to $CWND$ for each duplicate acknowledgement after the third? ::@:: It adds one MSS.
- fast recovery versus slow start: the pre-loss window is $CWND$; how far does each reaction drop it? ::@:: Fast recovery to about $CWND/2$, a return to slow start to one MSS.
- the climb back: a sender in fast recovery holds $13$ MSS after a loss halved a $20$ MSS window; how long does it take to reach $20$ MSS again? ::@:: $20 - 13 = 7$ MSS at one MSS per round trip, so $7$ round trips, and $7 \times 100\text{ ms} = 700$ ms.
- the cost of a loss: a $20$ MSS window loses a segment that three duplicate acknowledgements report; how many maximum segment sizes (MSS) does fast recovery cost, against a return to slow start? ::@:: $20 / 2 = 10$ and $10 + 3 = 13$, so $20 - 13 = 7$ MSS, where a return to slow start drops to $1$ MSS and costs $20 - 1 = 19$.

## limits

Reno rests on four assumptions that modern networks break. Filling a large bandwidth-delay product takes too long, since the window grows by one segment per round trip. Every loss is read as congestion, which is wrong on a wireless link where corruption also drops packets. Two flows with round trips of 10 ms and 50 ms settle at $5/6$ and $1/6$ of the link. The 10 ms flow takes 100 round trips a second against 20 for the 50 ms flow, so its window grows five times faster and fills the link first. Reno also fills the queue in front of the bottleneck, delaying every packet that passes it.

A window of 1.5 MB on a path of 50 Mbit/s with a 200 ms round trip puts 250 KB in the queue, and at that rate the queue adds 40 ms to every packet crossing it. A window of 1.25 MB fills the path and queues nothing at all.

The [Mathis equation](Mathis%20equation.md) puts a number on the same problem from the loss rate. On a path with 1460-byte segments and a 100 ms round trip, its first term gives 14,600 bytes per second. With $C = 1.22$, a target of 10 Mbit/s needs the loss term to supply a factor of about 86, so a loss rate of about 1 segment in 5,000.

[CUBIC TCP](CUBIC%20TCP.md), Compound TCP, and HighSpeed TCP attack the large-bandwidth problem. BBR and Copa attack the queue filling. Random early detection, DCTCP, and TIMELY move the decision into the network, where the switch acts.

---

Flashcards for this section are as follows:

- large bandwidth: why does TCP Reno take too long on a path with a large bandwidth-delay product? ::@:: Its window grows by one maximum segment size per round trip, so reaching a huge window takes many round trips.
- loss means congestion: which assumption fails on a wireless link? ::@:: That every loss means congestion, since a corrupted packet is dropped there too.
- RTT unfairness: two TCP Reno flows share a link with round trips of $10\text{ ms}$ and $50\text{ ms}$; what share does each receive? ::@:: $1\text{ s} / 10\text{ ms} = 100$ round trips against $1\text{ s} / 50\text{ ms} = 20$, a ratio of $5 : 1$, so the $10\text{ ms}$ flow takes $5/6$ and the $50\text{ ms}$ flow $1/6$.
- why the round trip matters: why does a shorter round trip win under TCP Reno? ::@:: The window grows by one maximum segment size per round trip, so the flow with more round trips per second grows faster.
- queue filling: what does TCP Reno do to the queue at the bottleneck? ::@:: It fills it, so every packet passing through waits longer.
- the queue past the bandwidth-delay product: a sender holds $1.5$ MB in flight on a $50\text{ Mbit/s}$ path whose round trip is $200\text{ ms}$; how much queue does it build? ::@:: $50\text{ Mbit/s} \times 0.2\text{ s} = 1.25$ MB, so $1.5\text{ MB} - 1.25\text{ MB} = 250$ KB, and $250\text{ KB} / 50\text{ Mbit/s} = 40$ ms of delay.
- the loss rate for a rate: on a path with $1460$-byte segments and a $100\text{ ms}$ round trip, what loss rate does the Mathis equation need for a throughput of $10\text{ Mbit/s}$? ::@:: $1460\text{ bytes} / 0.1\text{ s} = 14{,}600$ B/s, and $10\text{ Mbit/s} = 1.25\text{ MB/s}$, so $1.25\text{ MB/s} / 14{,}600\text{ B/s} \approx 86$ and $\sqrt{p} = 1.22 / 86$ gives $p \approx 1/5{,}000$.
- a window that fills the path: a path of $50\text{ Mbit/s}$ with a $200\text{ ms}$ round trip has a bandwidth-delay product of $1.25$ MB; what does a window of exactly that size do to the queue? ::@:: It fills the path and queues nothing at all.

<!-- check: ignore-next-line[header_style]: Reno is a proper noun -->
## Reno state machine

The transitions below also depend on the duplicate-acknowledgement counter and the slow-start threshold.

| from                 | event                                       | action                                                                              | to                   |
| -------------------- | ------------------------------------------- | ----------------------------------------------------------------------------------- | -------------------- |
| slow start           | duplicate acknowledgement                   | `dupACKcount++`                                                                     | slow start           |
| slow start           | new acknowledgement                         | `cwnd = cwnd + MSS`; `dupACKcount = 0`; transmit new segments as allowed            | slow start           |
| slow start           | timeout                                     | `ssthresh = cwnd/2`; `cwnd = 1 MSS`; `dupACKcount = 0`; retransmit missing segment  | slow start           |
| slow start           | new acknowledgement with `cwnd >= ssthresh` | none                                                                                | congestion avoidance |
| slow start           | `dupACKcount == 3`                          | `ssthresh = cwnd/2`; `cwnd = ssthresh + 3*MSS`; retransmit missing segment          | fast recovery        |
| congestion avoidance | duplicate acknowledgement                   | `dupACKcount++`                                                                     | congestion avoidance |
| congestion avoidance | new acknowledgement                         | `cwnd = cwnd + MSS*(MSS/cwnd)`; `dupACKcount = 0`; transmit new segments as allowed | congestion avoidance |
| congestion avoidance | timeout                                     | `ssthresh = cwnd/2`; `cwnd = 1 MSS`; `dupACKcount = 0`; retransmit missing segment  | slow start           |
| congestion avoidance | `dupACKcount == 3`                          | `ssthresh = cwnd/2`; `cwnd = ssthresh + 3*MSS`; retransmit missing segment          | fast recovery        |
| fast recovery        | duplicate acknowledgement                   | `cwnd = cwnd + MSS`; transmit new segments as allowed                               | fast recovery        |
| fast recovery        | new acknowledgement                         | `cwnd = ssthresh`; `dupACKcount = 0`                                                | congestion avoidance |
| fast recovery        | timeout                                     | `ssthresh = cwnd/2`; `cwnd = 1 MSS`; `dupACKcount = 0`; retransmit missing segment  | slow start           |

Reading the table as one run: a sender in congestion avoidance with a window of 20 MSS receives three duplicate acknowledgements, so it sets the slow-start threshold to 10 MSS and the window to 13 MSS. It stays in fast recovery as each further duplicate acknowledgement adds one MSS, and when the acknowledgement for the retransmitted segment arrives the window falls back to the threshold of 10 MSS and the sender returns to congestion avoidance. A sender in slow start with a window of 8 MSS that receives three duplicate acknowledgements sets the threshold to 4 MSS and the window to 7 MSS, and it enters fast recovery.

---

Flashcards for this section are as follows:

- initial state: which state does the sender start in, and what are the default $ssthresh$ and counter values? ::@:: Slow start, with $ssthresh = 64$ KB and the counter at $0$.
- slow start to congestion avoidance: a new acknowledgement arrives with $cwnd \ge ssthresh$; which state does the sender move to? ::@:: Congestion avoidance.
- entering fast recovery: from which two states, and on which event, does the sender enter fast recovery? ::@:: From slow start or congestion avoidance, on the third duplicate acknowledgement.
- timeout transitions: which state does a timeout lead to from any of the three states, and what becomes of $cwnd$ and $ssthresh$? ::@:: Slow start, with $ssthresh = cwnd/2$, $cwnd = 1$ MSS, and the counter reset.
- a loss in slow start: a sender in slow start holds $8$ MSS and receives three duplicate acknowledgements; what does it set? ::@:: $ssthresh = 8 / 2 = 4$ MSS and $cwnd = 4 + 3 = 7$ MSS, and it enters fast recovery.
- one run through the table: a sender in congestion avoidance holds $20$ maximum segment sizes (MSS) when three duplicate acknowledgements arrive; what does it set, and what does the acknowledgement for the retransmitted segment do? ::@:: $ssthresh = 20 / 2 = 10$ MSS and $cwnd = 10 + 3 = 13$ MSS, then that acknowledgement sets $cwnd = ssthresh = 10$ MSS and returns the sender to congestion avoidance.
