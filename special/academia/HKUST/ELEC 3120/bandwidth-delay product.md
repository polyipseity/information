---
aliases:
  - BDP
  - ELEC 3120 bandwidth-delay product
  - ELEC3120 bandwidth-delay product
  - HKUST ELEC 3120 bandwidth-delay product
  - HKUST ELEC3120 bandwidth-delay product
  - bandwidth delay product
  - bandwidth-delay product
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/bandwidth-delay_product
  - language/in/English
---

# bandwidth-delay product

The bandwidth-delay product (BDP) is the rate of a path multiplied by its round-trip time: the data a sender needs in flight to keep the path busy. A window below it leaves the link partly idle; a window above it builds queues. The delay is the round trip, not the one-way delay, because the sender holds the data until the acknowledgement returns. That wait is not twice the one-way delay either: the return carries an acknowledgement, which pays its crossing but almost no push time.

---

Flashcards for this section are as follows:

- bandwidth-delay product: what is the bandwidth-delay product? ::@:: The path's rate multiplied by its round-trip time.
- window below it: what is lost when the window is smaller than the bandwidth-delay product? ::@:: Link capacity, because the sender runs dry before acknowledgements return.
- window above it: what does a window larger than the bandwidth-delay product do to the path? ::@:: The path builds queues, because more data is in flight than the path can hold.

## pipe volume

In the [pipe picture](network%20delay.md#pipe%20model) of a link, the bandwidth is the width and the delay is the length, so their product is the pipe's volume, the bits it holds when full.

A $1\text{ Gbps}$ path holds $31.25$ MB over a $250\text{ ms}$ satellite round trip, about 21,400 segments of $1460$ bytes, and $6.25$ MB over $50\text{ ms}$, a quarter of that.

---

Flashcards for this section are as follows:

- pipe volume: in the pipe picture of a link, what does the product of width and length give? ::@:: The volume of the pipe, the number of bits it holds when full.
- window equal to the volume: what does a window the size of the pipe's volume achieve? ::@:: The whole path stays in use.
- satellite volume: how much data does a $10\text{ Mbps}$ path with a $250\text{ ms}$ round trip hold when it is full? ::@:: $10\text{ Mbps} \times 250\text{ ms} = 10^{7} \times 0.25 = 2.5 \times 10^{6}$ bits $= 312.5$ KB.
- pipe picture roles: in the pipe picture, what do the width and the length of the pipe stand for? ::@:: The bandwidth is the width and the delay is the length.
- full satellite volume in segments: how much data does a $1\text{ Gbps}$ path with a $250\text{ ms}$ round trip hold when full, and how many $1460$-byte segments is that? ::@:: $1\text{ Gbps} \times 250\text{ ms} = 10^{9} \times 0.25 = 2.5 \times 10^{8}$ bits $= 31.25$ MB, and $31.25\text{ MB} / 1460\text{ B} \approx 21{,}400$ segments.
- shorter path, same rate: how much does a $1\text{ Gbps}$ path with a $50\text{ ms}$ round trip hold when full, against the $31.25$ MB of a $250\text{ ms}$ round trip? ::@:: $1\text{ Gbps} \times 50\text{ ms} = 10^{9} \times 0.05 = 5 \times 10^{7}$ bits $= 6.25$ MB, a quarter of $31.25$ MB.

## window sizing

A path of rate $R$ with round-trip time $RTT$ needs $R \times RTT$ bits outstanding to send at $R$, so that product is the window to aim for. Sending at 50 Mbps across a 200 ms round trip needs $50\text{ Mbps} \times 200\text{ ms} = 1.25$ MB in flight. The window must also fit inside the receiver's advertised window, which is [flow control](flow%20control%20(data).md); sizing it to the bandwidth-delay product is congestion control.

---

Flashcards for this section are as follows:

- the window for a rate: which window size sustains a rate $R$ over a path with round-trip time $RTT$? ::@:: $R \times RTT$ bytes in flight.
- worked case: how much data must be in flight to send $50\text{ Mbps}$ over a path whose round trip is $200\text{ ms}$? ::@:: $50\text{ Mbps} \times 200\text{ ms} = 1.25$ MB.
- oversized advertised window: what happens when the receiver advertises far more than the path can carry? ::@:: The sender outruns the slow link, packets queue at it, and the queue overflows.

### worked sizes

A $10\text{ Mbps}$ path with a $100\text{ ms}$ round trip needs $10\text{ Mbps} \times 100\text{ ms} = 125$ KB, twice the $62.5$ KB of the same rate over $50\text{ ms}$.

---

Flashcards for this section are as follows:

- narrow path: how much data must be in flight to send at $10\text{ Mbps}$ over a path whose round trip is $50\text{ ms}$? ::@:: $10\text{ Mbps} \times 50\text{ ms} = 62.5$ KB.
- a longer round trip: how much data must be in flight to send at $10\text{ Mbps}$ over a path whose round trip is $100\text{ ms}$? ::@:: $10\text{ Mbps} \times 100\text{ ms} = 125$ KB.
- why a longer round trip needs more: why does a $10\text{ Mbps}$ path with a $100\text{ ms}$ round trip need twice the window of the same rate over $50\text{ ms}$? ::@:: The data stays in the network twice as long, so twice as much must be outstanding.

## round trip against one-way delay

A sender cannot release the bytes it has written into the path until the acknowledgement comes home, so they stay in the network for a whole round trip. Sizing the window on the one-way delay counts only the outbound half, and the sender runs dry before the first acknowledgement arrives.

The round trip is not twice the one-way delay. Going out, the segment pays its transmission delay and one propagation delay. Coming back, the acknowledgement pays one propagation delay and a transmission delay small enough to ignore, since it holds a few dozen bytes. The wait is twice the propagation delay plus the segment's transmission delay once.

A 50 Mbps path with 100 ms of propagation each way and 1460-byte packets makes the three counts concrete. Pushing a packet in takes 11,680 bits at 50 Mbps, which is 0.23 ms, so the one-way delay is 100.23 ms and the round trip is 200.23 ms. The product that counts is $50\text{ Mbps} \times 200.23\text{ ms} \approx 1.25$ MB. The one-way product gives $50\text{ Mbps} \times 100.23\text{ ms} \approx 626$ KB, half of what the path needs, because the link idles through the return crossing waiting for the first acknowledgement. Twice the one-way delay gives 200.46 ms and 1.253 MB, 0.23 ms too much, and the excess is the segment's push time charged a second time.

The satellite path holds the same difference at a larger scale: about 125 ms of propagation each way and 12 microseconds to push a segment onto a 1 Gbps link make the round trip about 250 ms. The path then needs $1\text{ Gbps} \times 250\text{ ms} = 31.25$ MB in flight, and a window sized on the outbound half holds only $15.625$ MB. That halved window costs half the rate: $15.625\text{ MB} / 250\text{ ms} = 62.5$ MB per second, which is $500$ Mbps.

---

Flashcards for this section are as follows:

- which delay: which delay does the bandwidth-delay product use? ::@:: The round-trip time, not the one-way delay.
- why the round trip: why does the sender still hold the data after it has been delivered to the receiver? ::@:: Because the acknowledgement that releases it has not come back yet, so the data is still in the network.
- why not twice: why is the round trip shorter than twice the one-way delay? ::@:: The return leg carries an acknowledgement of a few dozen bytes, so it pays the crossing and almost no push time, and the segment's transmission delay is charged once.
- worked counts: a $50\text{ Mbps}$ path with $100\text{ ms}$ of propagation each way carries $1460$-byte packets; what are the one-way delay, the round trip, and twice the one-way delay? ::@:: $11\,680$ bits at $50\text{ Mbps}$ take $0.23\text{ ms}$ to push in, so the one-way delay is $100.23\text{ ms}$, the round trip $200.23\text{ ms}$, and twice the one-way delay $200.46\text{ ms}$.
- wrong product: on a $50\text{ Mbps}$ path with $100\text{ ms}$ of propagation each way, what does sizing the window on the $100.23\text{ ms}$ one-way delay give against the $1.25$ MB the path needs? ::@:: $50\text{ Mbps} \times 100.23\text{ ms} \approx 626$ KB, half of what the path needs.
- doubled product: on a $50\text{ Mbps}$ path with $100\text{ ms}$ of propagation each way, what does sizing the window on twice the one-way delay give, and how far off is it? ::@:: $50\text{ Mbps} \times 200.46\text{ ms} \approx 1.253$ MB, $0.23\text{ ms}$ too much, since it charges the segment's push time twice.
- satellite one-way product: for a $1\text{ Gbps}$ satellite path with $125\text{ ms}$ of propagation each way and a round trip of about $250\text{ ms}$, what does the outbound half give? ::@:: $1\text{ Gbps} \times 125\text{ ms} = 15.625$ MB, half of the $31.25$ MB the path needs.
- the halved satellite window: a $1\text{ Gbps}$ satellite path with a $250\text{ ms}$ round trip is given a window of $15.625$ MB; what rate does it reach? ::@:: $15.625\text{ MB} / 250\text{ ms} = 62.5\text{ MB/s} = 500$ Mbps, half of $1$ Gbps.
- refilling the pipe: why does the round trip set how fast the sender can refill the pipe? ::@:: Room for new data is freed only by acknowledgements, which arrive one round trip after the data went out.

## congestion window

The window that congestion control grows is meant to track the bandwidth-delay product. With $c$ bytes in flight and a round trip of $RTT$, the sending rate is $c / RTT$ bytes per second, so a path of rate $R$ runs at full rate only when $c = R \times RTT$, which is the bandwidth-delay product. Above that value the surplus stands in the bottleneck queue and then overflows into loss.

Half the window gives half the rate: on the $10\text{ Mbps}$ path with a $50\text{ ms}$ round trip, a window of $31.25$ KB gives $625{,}000$ bytes per second, or $5$ Mbps, while the path itself carries $10$ Mbps.

The sender follows the acknowledgements rather than a timer of its own. [TCP congestion control](TCP%20congestion%20control.md) grows and shrinks the window under that rule, and [congestion control](congestion%20control.md) is the wider statement of it.

Slow start doubles the window each round trip, so a sender starting from one $1460$-byte segment holds $93{,}440$ bytes after six round trips, enough for the $62.5$ KB that the $10\text{ Mbps}$ path needs. Over a $50\text{ ms}$ round trip those six round trips take $300\text{ ms}$, so the link stays partly idle for the first third of a second.

---

Flashcards for this section are as follows:

- rate from the window: with $c$ bytes in flight and a round trip of $RTT$, what sending rate does the window allow? ::@:: $c / RTT$ bytes per second.
- half window rate: with $31.25$ KB in flight over a $50\text{ ms}$ round trip, what sending rate does the window allow? ::@:: $31.25\text{ KB} / 50\text{ ms} = 625{,}000$ bytes per second, or $5$ Mbps.
- which mechanism moves the window: which mechanism grows and shrinks the congestion window under the rate rule, and what is the wider statement of it? ::@:: Transmission Control Protocol (TCP) congestion control; congestion control is the wider statement.
- slow start growth: starting from one $1460$-byte segment and doubling the window every round trip, how much data does the sender have in flight after six round trips? ::@:: $1460 \times 2^6 = 93{,}440$ bytes, enough for the $62.5$ KB the $10\text{ Mbps}$ path needs.
- slow start time: on a path with a $50\text{ ms}$ round trip, how long do six doubling round trips take, and what does the link do meanwhile? ::@:: $6 \times 50\text{ ms} = 300$ ms, so the link stays partly idle for the first third of a second.

<!-- check: ignore-next-line[header_style]: ACK is an acronym -->
## ACK clocking

With the window set to the bandwidth-delay product, acknowledgements return spaced as the segments went out. Each arrival frees room for one more segment, so the sender keeps transmitting at the link's rate. The acknowledgements, not a timer, set that rate, which is why the effect is called ACK clocking.

On the $10\text{ Mbps}$ path with a $50\text{ ms}$ round trip, a window of $62.5$ KB holds about $42$ segments of $1460$ bytes, and the acknowledgements come back one every $50\text{ ms} / 42 \approx 1.2\text{ ms}$. The sender puts $1460$ bytes on the wire every $1.2\text{ ms}$, which is $10$ Mbps. Halving the window leaves the rate at $5$ Mbps.

On the satellite path the clock is faster: the $31.25$ MB window of a $1\text{ Gbps}$ path with a $250\text{ ms}$ round trip holds about $21{,}400$ segments of $1460$ bytes, so the acknowledgements come back one every $250\text{ ms} / 21{,}400 \approx 11.7\,\mu\text{s}$, and the sender puts $1460$ bytes on the wire every $11.7\,\mu\text{s}$, which is $1$ Gbps. Halving the window stretches that interval to $23.4\,\mu\text{s}$ and leaves the rate at $500$ Mbps.

A window above the product does not clock faster, because the bottleneck still serves one segment at a time. Only the queue absorbs the surplus: doubling the window on the $10\text{ Mbps}$ path to $125$ KB leaves $125 - 62.5 = 62.5$ KB standing in the queue, which is $62{,}500 / 1{,}250{,}000 = 0.05$ s of traffic, so every packet waits an extra $50$ ms. Above the product a wider window buys delay rather than rate.

---

Flashcards for this section are as follows:

- acknowledgement (ACK) clocking: what happens when the window equals the bandwidth-delay product? ::@:: Acknowledgements return at the rate the segments went out, each freeing room for exactly one more, so the sender holds the link's rate.
- segments in flight: how many $1460$-byte segments fit in the $62.5$ KB window of a $10\text{ Mbps}$ path with a $50\text{ ms}$ round trip? ::@:: $10\text{ Mbit/s} \times 0.05\text{ s} = 500{,}000\text{ bit} = 62{,}500$ bytes, and $62{,}500 / 1460 \approx 42.8$, so about $42$ segments.
- the satellite clock: on a $1\text{ Gbps}$ path with a $250\text{ ms}$ round trip and a window of $31.25$ MB, how far apart do the acknowledgements arrive? ::@:: $31.25\text{ MB} / 1460\text{ B} \approx 21{,}400$ segments, so $250\text{ ms} / 21{,}400 \approx 11.7\,\mu\text{s}$ apart, one per $1460$-byte segment.
- the clock's rate: the sender puts one $1460$-byte segment on the wire every $1.2\text{ ms}$; what rate does that give? ::@:: $1460\text{ B} / 1.2\text{ ms} \approx 1.2\text{ MB/s} \approx 10$ Mbps.
- the halved satellite clock: the $31.25$ MB window of a $1\text{ Gbps}$ path with a $250\text{ ms}$ round trip is halved; what interval and rate result? ::@:: $2 \times 11.7\,\mu\text{s} \approx 23.4\,\mu\text{s}$ apart, and $1\text{ Gbps} / 2 = 500$ Mbps.
- a window above the product: the $62.5$ KB window of the $10\text{ Mbps}$ path with a $50\text{ ms}$ round trip doubles to $125$ KB; what rate does the clock keep, and what does the surplus cost? ::@:: Still $10\text{ Mbps}$, since the bottleneck serves one segment at a time; $125 - 62.5 = 62.5$ KB stands in the queue, which is $62\,500 / 1\,250\,000 = 0.05$ s, so every packet waits an extra $50$ ms.
