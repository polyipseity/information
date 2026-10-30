---
aliases:
  - ELEC 3120 round-trip time
  - ELEC3120 round-trip time
  - HKUST ELEC 3120 round-trip time
  - HKUST ELEC3120 round-trip time
  - RTT
  - round trip time
  - round-trip time
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/round-trip_time
  - language/in/English
---

# round-trip time

Round-trip time (RTT) is the time for a segment to reach the far end plus the time for its acknowledgement to come back. The two halves cost different things. Outward, the segment waits for its bits to enter the link and then for the last of them to cross. Backward, an acknowledgement is a header with almost nothing in it, so pushing it into the link costs close to nothing and the return is the crossing alone. A round trip pays the propagation delay twice and the segment's transmission delay once.

The Transmission Control Protocol (TCP) uses it to set the retransmission timer, which has to outlast a round trip. A segment crossing 3,000 km of fiber spends about 30 ms on the two crossings, and one through a geostationary satellite about 240 ms.

---

Flashcards for this section are as follows:

- round-trip time: what does the round-trip time measure? ::@:: The time for a segment to reach the far end plus the time for its acknowledgement to return.
- what a round trip pays: which delays does one round trip pay, and why is the return the cheaper half? ::@:: The propagation delay twice and the segment's transmission delay once; the acknowledgement holds a header and almost no data, so its push time is negligible.
- fiber crossing: light crosses $3000$ km of fiber at two thirds of its speed in a vacuum; what does one crossing cost, and what do the two cost together? ::@:: $3000\text{ km} / 200\,000\text{ km/s} = 15\text{ ms}$ each way, so $2 \times 15 = 30$ ms for the two crossings.
- satellite crossings: a geostationary satellite sits $35\,786$ km up and the signal crosses at $300\,000\text{ km/s}$; what do the two crossings cost? ::@:: $2 \times 35\,786\text{ km} = 71\,572\text{ km}$ at $300\,000\text{ km/s}$ takes $239\text{ ms}$, about $240$ ms.

## one-way delay against round trip

A one-way delay counts every cost between the segment leaving the sender and reaching the receiver: the transmission delay that pushes its bits into the link, the propagation delay of the path, and any queueing it meets. The round trip adds the acknowledgement's journey back, and that journey carries a packet of a different size.

An acknowledgement is a few dozen bytes of header, so on any link fast enough to matter its transmission delay rounds to nothing and the return leg is pure propagation. Doubling the one-way delay over-counts: it charges the segment's transmission delay twice, though the return never spends it.

A 1500-byte segment on a 10 Mbps satellite path with 125 ms of propagation each way shows the error. Pushing the segment in takes 12,000 bits at 10 Mbps, which is 1.2 ms, so the one-way delay is 126.2 ms. The round trip is 126.2 + 125 = 251.2 ms. Twice the one-way delay would say 252.4 ms, 1.2 ms too long, and that 1.2 ms is the segment's push time charged a second time.

---

Flashcards for this section are as follows:

- one-way delay: which delays make up a one-way delay? ::@:: The transmission delay that pushes the packet into the link, the propagation delay of the path, and any queueing on the way.
- return leg: why is the return leg of a round trip cheaper than the outward leg? ::@:: An acknowledgement holds a few dozen bytes of header, so its transmission delay rounds to nothing and it pays propagation alone.
- worked satellite round trip: a $1500$-byte segment crosses a $10\text{ Mbps}$ satellite path with $125\text{ ms}$ of propagation each way; what is the one-way delay, and what is the round trip? ::@:: $12\,000$ bits at $10\text{ Mbps}$ take $1.2\text{ ms}$ to push in, so the one-way delay is $126.2\text{ ms}$; the round trip is $126.2 + 125 = 251.2\text{ ms}$.
- doubled one-way delay: a $1500$-byte segment crosses a $10\text{ Mbps}$ satellite path with $125\text{ ms}$ of propagation each way; what does twice the one-way delay of $126.2\text{ ms}$ give, and what does it charge twice? ::@:: $252.4\text{ ms}$, $1.2\text{ ms}$ too long: it charges the segment's push time a second time.

## measuring a round trip

A sample round-trip time is one measurement: the time from sending a segment to receiving its acknowledgement. Segments that were retransmitted are left out, because their acknowledgement may belong to either copy. A path with 20 ms of propagation delay each way spends 40 ms crossing, and pushing a 1500-byte segment onto a 1 Gbps link adds 12 microseconds once, so the round trip is 40.012 ms. The sample carries whatever the path did to the segment, so a path with a queue gives a longer sample than an empty one.

---

Flashcards for this section are as follows:

- sample round-trip time: how is one measurement taken? ::@:: The time from sending a segment to receiving the acknowledgement for it.
- retransmissions: why are retransmitted segments left out of the measurement? ::@:: Their acknowledgement may answer either copy, and which one cannot be told.
- path round trip: a path has $20\text{ ms}$ of propagation delay each way and a $1\text{ Gbps}$ link; what is its round-trip time before any queueing? ::@:: $40\text{ ms}$: $20\text{ ms}$ out and $20\text{ ms}$ back, plus the $12\,\mu\text{s}$ it takes to push a $1500$-byte segment in, paid once.
- what the sample holds: does a measured round-trip time include the queueing the segment met on the way? ::@:: Yes: the sample measures the whole round trip under the load the segment met, not the propagation delay alone.
- sender link time: how long does a sender take to push a $1500$-byte segment onto a $1\text{ Gbps}$ link, and how often does a round trip pay that time? ::@:: $1500 \times 8 = 12\,000$ bits, which at $10^{9}$ bits per second take $12\,\mu\text{s}$; the round trip pays it once, since an acknowledgement spends almost none.

## smoothing

One segment's round trip says little about the next, so the timer runs on an estimate, a weighted average that leans on the newest sample and fades older ones exponentially: $\text{EstimatedRTT} = (1 - \alpha)\text{EstimatedRTT} + \alpha\,\text{SampleRTT}$, with a weight of $0.125$ on the sample. A sample of 120 ms against an estimate of 100 ms moves the estimate to 102.5 ms, an eighth of the way.

---

Flashcards for this section are as follows:

- estimated round-trip time: how is $\text{EstimatedRTT}$ updated from a new $\text{SampleRTT}$, with weight $\alpha$? ::@:: $\text{EstimatedRTT} = (1 - \alpha)\text{EstimatedRTT} + \alpha\,\text{SampleRTT}$.
- why smooth: what does smoothing protect the timer from? ::@:: A single unusual sample, which would otherwise move the timeout too far in one step.
- worked estimate: with $\text{EstimatedRTT} = 100\text{ ms}$ and a new $\text{SampleRTT} = 120\text{ ms}$, what does the update with $\alpha = 0.125$ give? ::@:: $0.875 \times 100 + 0.125 \times 120 = 102.5\text{ ms}$, an eighth of the way.
- a second sample: with $\text{EstimatedRTT} = 102.5\text{ ms}$ and a new $\text{SampleRTT} = 90\text{ ms}$, what does the update with $\alpha = 0.125$ give? ::@:: $0.875 \times 102.5 + 0.125 \times 90 = 100.9\text{ ms}$, a step of $1.6\text{ ms}$.
- a third sample: with $\text{EstimatedRTT} = 100.9375\text{ ms}$, the unrounded value behind $100.9\text{ ms}$, and a new $\text{SampleRTT} = 110\text{ ms}$, what does the update with $\alpha = 0.125$ give? ::@:: $0.875 \times 100.9375 + 0.125 \times 110 = 102.1\text{ ms}$, about $1.1\text{ ms}$ above the previous estimate.

## deviation

A margin is added on top of the estimate, sized by how far the samples stray. That spread is smoothed the same way, $\text{DevRTT} = (1 - \beta)\text{DevRTT} + \beta\,|\text{SampleRTT} - \text{EstimatedRTT}|$, with a weight of $0.25$ on the newest deviation. A path that settles at one round trip drives its deviation toward zero: with a deviation of 10 ms and a sample sitting exactly on the estimate, the new deviation is 7.5 ms, and it keeps falling while the samples hold still.

---

Flashcards for this section are as follows:

- deviation: what does the smoothed deviation measure? ::@:: How far the sample round-trip times stray from the estimate.
- deviation update: how is $\text{DevRTT}$ updated from $\text{SampleRTT}$, $\text{EstimatedRTT}$, and a weight $\beta$? ::@:: $\text{DevRTT} = (1 - \beta)\text{DevRTT} + \beta\,|\text{SampleRTT} - \text{EstimatedRTT}|$, with $\beta$ typically $0.25$.
- why a margin: what does a wide spread in sample round-trip times demand of the timer's margin? ::@:: A wider margin, since the next round trip is less predictable.
- worked deviation: with $\text{EstimatedRTT} = 100\text{ ms}$, $\text{DevRTT} = 10\text{ ms}$, and $\text{SampleRTT} = 120\text{ ms}$, what is the new $\text{DevRTT}$ with $\beta = 0.25$? ::@:: $0.75 \times 10 + 0.25 \times 20 = 12.5\text{ ms}$.
- a path that settles: what happens to $\text{DevRTT}$ over successive updates once every sample sits on the estimate? ::@:: It keeps falling: each update keeps three quarters of the old deviation and adds nothing.

## timeout interval

The timer is the estimate plus four times the deviation, so a steady path gets a tight timer and a jumpy one a loose one: $\text{TimeoutInterval} = \text{EstimatedRTT} + 4\,\text{DevRTT}$. Request for Comments 6298 (2011) gives these rules and floors the timer at 1 second.

A path with a 40 ms round trip and a smoothed deviation of 12.5 ms gets a timer of 90 ms, and a path with an 80 ms round trip gets 130 ms. The estimate follows a changed path only slowly. With a weight of 0.125 the gap between the estimate and the new round trip shrinks to about a third of what it was after eight samples, so the timer stays fitted to the old path and fires before an acknowledgement on the longer one arrives.

---

Flashcards for this section are as follows:

- timeout interval: how is the timer computed from $\text{EstimatedRTT}$ and $\text{DevRTT}$? ::@:: $\text{TimeoutInterval} = \text{EstimatedRTT} + 4\,\text{DevRTT}$.
- too short: what happens when the timer is set below the true round-trip time? ::@:: It fires early, so segments are retransmitted before they are actually lost.
- too long: what happens when the timer is set far above the true round-trip time? ::@:: A loss takes that much longer to repair, so the connection reacts slowly.
- worked timer: with $\text{EstimatedRTT} = 102.5\text{ ms}$ and $\text{DevRTT} = 12.5\text{ ms}$, what is $\text{TimeoutInterval}$? ::@:: $102.5 + 4 \times 12.5 = 152.5\text{ ms}$.
- path timer: with a round-trip time of $40\text{ ms}$ and a smoothed deviation of $12.5\text{ ms}$, what timer does the path get? ::@:: $40 + 4 \times 12.5 = 90\text{ ms}$.
- the floor: what is the smallest retransmission timer Request for Comments 6298 (2011) allows? ::@:: One second, however small the estimate is.
- the specification: which document states the smoothing and timeout rules for the retransmission timer, and in which year? ::@:: Request for Comments 6298, published in 2011.
- fitting a changed path: with $\alpha = 0.125$, what happens to the gap between the estimate and a new round trip after eight samples? ::@:: It shrinks to about a third of its original size, since $0.875^{8} \approx 0.34$, so the timer stays fitted to the old path for the first few round trips.
