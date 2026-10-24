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

The bandwidth-delay product (BDP) is the rate of a path multiplied by its round-trip time. A sender needs that much data in flight to keep the path busy. A window below it leaves the link partly idle; a window above it builds queues. The delay is the round trip rather than the one-way time, because the sender holds the data until the acknowledgement returns.

---

Flashcards for this section are as follows:

- bandwidth-delay product: what is the bandwidth-delay product? ::@:: The path's rate multiplied by its round-trip time.
- window below it: what is lost when the window is smaller than the bandwidth-delay product? ::@:: Link capacity, because the sender runs dry before acknowledgements return.
- window above it: what does a window larger than the bandwidth-delay product do to the path? ::@:: The path builds queues, because more data is in flight than the path can hold.

## pipe volume

In the [pipe picture](network%20delay.md#pipe%20model) of a link, the bandwidth is the width and the delay is the length, so their product is the pipe's volume, the bits it holds when full. A window of that size keeps the whole path in use.

A $1\text{ Gbps}$ path with a $250\text{ ms}$ round trip holds $31.25$ MB, about 21,400 segments of $1460$ bytes.

A $1\text{ Gbps}$ path with a $50\text{ ms}$ round trip holds $6.25$ MB, a quarter of what the same rate holds over a $250\text{ ms}$ satellite round trip.

---

Flashcards for this section are as follows:

- pipe volume: in the pipe picture of a link, what does the product of width and length give? ::@:: The volume of the pipe, the number of bits it holds when full.
- window equal to the volume: what does a window the size of the pipe's volume achieve? ::@:: The whole path stays in use.
- satellite volume: how much data does a $10\text{ Mbps}$ path with a $250\text{ ms}$ round trip hold when it is full? ::@:: $10\text{ Mbps} \times 250\text{ ms} = 10^{7} \times 0.25 = 2.5 \times 10^{6}$ bits $= 312.5$ KB.
- pipe picture roles: in the pipe picture, what do the width and the length of the pipe stand for? ::@:: The bandwidth is the width and the delay is the length.
- full satellite volume in segments: how much data does a $1\text{ Gbps}$ path with a $250\text{ ms}$ round trip hold when full, and how many $1460$-byte segments is that? ::@:: $1\text{ Gbps} \times 250\text{ ms} = 10^{9} \times 0.25 = 2.5 \times 10^{8}$ bits $= 31.25$ MB, and $31.25\text{ MB} / 1460\text{ B} \approx 21{,}400$ segments.
- shorter path, same rate: how much does a $1\text{ Gbps}$ path with a $50\text{ ms}$ round trip hold when full, against the $31.25$ MB of a $250\text{ ms}$ round trip? ::@:: $1\text{ Gbps} \times 50\text{ ms} = 10^{9} \times 0.05 = 5 \times 10^{7}$ bits $= 6.25$ MB, a quarter of $31.25$ MB.

## window sizing

For a path of rate $R$ with round-trip time $RTT$, sending at $R$ needs $R \times RTT$ bits outstanding, so that product is the window to aim for. Sending at 50 Mbps across a path with a 200 ms round trip needs $50\text{ Mbps} \times 200\text{ ms} = 1.25$ MB in flight. The window also has to fit inside the receiver's advertised window, which is [flow control](flow%20control%20(data).md). Fitting the bandwidth-delay product is congestion control.

---

Flashcards for this section are as follows:

- the window for a rate: which window size sustains a rate $R$ over a path with round-trip time $RTT$? ::@:: $R \times RTT$ bytes in flight.
- worked case: how much data must be in flight to send $50\text{ Mbps}$ over a path whose round trip is $200\text{ ms}$? ::@:: $50\text{ Mbps} \times 200\text{ ms} = 1.25$ MB.
- oversized advertised window: what happens when the receiver advertises far more than the path can carry? ::@:: The sender outruns the slow link, packets queue at it, and the queue overflows.

### worked sizes

A $10\text{ Mbps}$ path with a $100\text{ ms}$ round trip needs $10\text{ Mbps} \times 100\text{ ms} = 125$ KB, twice the $62.5$ KB of the same rate over $50\text{ ms}$, because the data stays in the network longer.

---

Flashcards for this section are as follows:

- narrow path: how much data must be in flight to send at $10\text{ Mbps}$ over a path whose round trip is $50\text{ ms}$? ::@:: $10\text{ Mbps} \times 50\text{ ms} = 62.5$ KB.
- a longer round trip: how much data must be in flight to send at $10\text{ Mbps}$ over a path whose round trip is $100\text{ ms}$? ::@:: $10\text{ Mbps} \times 100\text{ ms} = 125$ KB.
- why a longer round trip needs more: why does a $10\text{ Mbps}$ path with a $100\text{ ms}$ round trip need twice the window of the same rate over $50\text{ ms}$? ::@:: The data stays in the network twice as long, so twice as much must be outstanding.

## round trip against one-way delay

The choice turns on where the data sits: a sender cannot release the bytes it has written into the path until the acknowledgement comes home, so they stay in the network for a whole round trip. Multiplying the rate by the one-way delay counts only the outbound half, so the window would be too small and the sender would run dry before the first acknowledgement arrived.

A path of 50 Mbps with a 100 ms one-way delay and a 200 ms round trip shows the difference: the correct product is $50\text{ Mbps} \times 200\text{ ms} = 1.25$ MB, the wrong one $50\text{ Mbps} \times 100\text{ ms} = 625$ KB. A window of 625 KB fills the path to half its rate, because the link idles for the second half of the round trip waiting for the first acknowledgement.

The satellite path holds the same difference at a larger scale, with a one-way delay of about $125\text{ ms}$ and a round trip about $250\text{ ms}$, so a $1\text{ Gbps}$ link needs $31.25$ MB in flight, and a window sized on the one-way delay holds only $15.625$ MB of it. That halved window costs half the rate: $15.625\text{ MB} / 250\text{ ms} = 62.5$ MB per second, which is $500$ Mbps.

---

Flashcards for this section are as follows:

- which delay: which delay does the bandwidth-delay product use? ::@:: The round-trip time, not the one-way delay.
- why the round trip: why does the sender still hold the data after it has been delivered to the receiver? ::@:: Because the acknowledgement that releases it has not come back yet, so the data is still in the network.
- wrong product: for a $50\text{ Mbps}$ path with a $100\text{ ms}$ one-way delay and a $200\text{ ms}$ round trip, what does the one-way product give? ::@:: $50\text{ Mbps} \times 100\text{ ms} = 625$ KB, half of what the path needs.
- satellite one-way product: for a $1\text{ Gbps}$ satellite path with a one-way delay of about $125\text{ ms}$ and a round trip of about $250\text{ ms}$, what does the one-way product give? ::@:: $1\text{ Gbps} \times 125\text{ ms} = 15.625$ MB, half of the $31.25$ MB the path needs.
- the halved satellite window: a $1\text{ Gbps}$ satellite path with a $250\text{ ms}$ round trip is given a window of $15.625$ MB; what rate does it reach? ::@:: $15.625\text{ MB} / 250\text{ ms} = 62.5\text{ MB/s} = 500$ Mbps, half of $1$ Gbps.
- refilling the pipe: why does the round trip set how fast the sender can refill the pipe? ::@:: Room for new data is freed only by acknowledgements, which arrive one round trip after the data went out.

## congestion window

The window that congestion control grows is meant to track the bandwidth-delay product. With $c$ bytes in flight and a round trip of $RTT$, the sending rate is $c / RTT$ bytes per second, so a path of rate $R$ runs at full rate only when $c = R \times RTT$, which is the bandwidth-delay product. A window below that value leaves the link partly idle, because the sender waits for acknowledgements that return only after a whole round trip. A window above it fills the queues at the bottleneck, and full queues overflow into loss.

Half the window gives half the rate: on the $10\text{ Mbps}$ path with a $50\text{ ms}$ round trip, a window of $31.25$ KB gives $625{,}000$ bytes per second, or $5$ Mbps, while the path itself carries $10$ Mbps.

The window also sets the sending rate, and the sender follows the acknowledgements rather than a timer of its own. [TCP congestion control](TCP%20congestion%20control.md) grows and shrinks the window under that rule, and [congestion control](congestion%20control.md) is the wider statement of it.

Reaching the product costs round trips. Slow start doubles the window each round trip, so a sender starting from one $1460$-byte segment holds $93{,}440$ bytes after six round trips, enough for the $62.5$ KB that the $10\text{ Mbps}$ path needs. Over a $50\text{ ms}$ round trip those six round trips take $300\text{ ms}$, so the link stays partly idle for the first third of a second.

---

Flashcards for this section are as follows:

- rate from the window: with $c$ bytes in flight and a round trip of $RTT$, what sending rate does the window allow? ::@:: $c / RTT$ bytes per second.
- half window rate: with $31.25$ KB in flight over a $50\text{ ms}$ round trip, what sending rate does the window allow? ::@:: $31.25\text{ KB} / 50\text{ ms} = 625{,}000$ bytes per second, or $5$ Mbps.
- which mechanism moves the window: which mechanism grows and shrinks the congestion window under the rate rule, and what is the wider statement of it? ::@:: Transmission Control Protocol (TCP) congestion control; congestion control is the wider statement.
- slow start growth: starting from one $1460$-byte segment and doubling the window every round trip, how much data does the sender have in flight after six round trips? ::@:: $1460 \times 2^6 = 93{,}440$ bytes, enough for the $62.5$ KB the $10\text{ Mbps}$ path needs.
- slow start time: on a path with a $50\text{ ms}$ round trip, how long do six doubling round trips take, and what does the link do meanwhile? ::@:: $6 \times 50\text{ ms} = 300$ ms, so the link stays partly idle for the first third of a second.

<!-- check: ignore-next-line[header_style]: ACK is an acronym -->
## ACK clocking

With the window set to the bandwidth-delay product, acknowledgements return spaced as the segments went out. Each arrival frees room for one more segment, so the sender keeps transmitting at the link's rate. The acknowledgements, not a timer, then set the rate, which is why the effect is called ACK clocking.

On the $10\text{ Mbps}$ path with a $50\text{ ms}$ round trip, a window of $62.5$ KB holds about $42$ segments of $1460$ bytes, and the acknowledgements come back one every $50\text{ ms} / 42 \approx 1.2\text{ ms}$. The sender then puts $1460$ bytes on the wire every $1.2\text{ ms}$, which is $10$ Mbps. Halving the window leaves the rate at $5$ Mbps.

On the satellite path the clock is faster: the $31.25$ MB window of a $1\text{ Gbps}$ path with a $250\text{ ms}$ round trip holds about $21{,}400$ segments of $1460$ bytes, so the acknowledgements come back one every $250\text{ ms} / 21{,}400 \approx 11.7\,\mu\text{s}$, and the sender puts $1460$ bytes on the wire every $11.7\,\mu\text{s}$, which is $1$ Gbps. Halving the window stretches that interval to $23.4\,\mu\text{s}$ and leaves the rate at $500$ Mbps.

A window above the product does not clock faster, because the bottleneck still serves one segment at a time. Only the queue absorbs the surplus: doubling the window on the $10\text{ Mbps}$ path to $125$ KB leaves $125 - 62.5 = 62.5$ KB standing in the queue, which is $62{,}500 / 1{,}250{,}000 = 0.05$ s of traffic, so every packet waits an extra $50$ ms while the acknowledgements keep arriving at the link's rate. Above the product a wider window buys delay rather than rate.

---

Flashcards for this section are as follows:

- acknowledgement (ACK) clocking: what happens when the window equals the bandwidth-delay product? ::@:: Acknowledgements return at the rate the segments went out, each freeing room for exactly one more, so the sender holds the link's rate.
- segments in flight: how many $1460$-byte segments fit in the $62.5$ KB window of a $10\text{ Mbps}$ path with a $50\text{ ms}$ round trip? ::@:: $10\text{ Mbit/s} \times 0.05\text{ s} = 500{,}000\text{ bit} = 62{,}500$ bytes, and $62{,}500 / 1460 \approx 42.8$, so about $42$ segments.
- the satellite clock: on a $1\text{ Gbps}$ path with a $250\text{ ms}$ round trip and a window of $31.25$ MB, how far apart do the acknowledgements arrive? ::@:: $31.25\text{ MB} / 1460\text{ B} \approx 21{,}400$ segments, so $250\text{ ms} / 21{,}400 \approx 11.7\,\mu\text{s}$ apart, one per $1460$-byte segment.
- the clock's rate: the sender puts one $1460$-byte segment on the wire every $1.2\text{ ms}$; what rate does that give? ::@:: $1460\text{ B} / 1.2\text{ ms} \approx 1.2\text{ MB/s} \approx 10$ Mbps.
- the halved satellite clock: the $31.25$ MB window of a $1\text{ Gbps}$ path with a $250\text{ ms}$ round trip is halved; what interval and rate result? ::@:: $2 \times 11.7\,\mu\text{s} \approx 23.4\,\mu\text{s}$ apart, and $1\text{ Gbps} / 2 = 500$ Mbps.
- a window above the product: the $62.5$ KB window of the $10\text{ Mbps}$ path with a $50\text{ ms}$ round trip doubles to $125$ KB and the queue holds the surplus; what rate does the clock keep, and what does the surplus cost? ::@:: Still $10\text{ Mbps}$, since the bottleneck serves one segment at a time; $125 - 62.5 = 62.5$ KB stands in the queue, which is $62\,500 / 1\,250\,000 = 0.05$ s, so every packet waits an extra $50$ ms.
