---
aliases:
  - ELEC 3120 token bucket
  - ELEC3120 token bucket
  - HKUST ELEC 3120 token bucket
  - HKUST ELEC3120 token bucket
  - token bucket
  - token bucket shaping
  - traffic shaping
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/token_bucket
  - language/in/English
---

# token bucket

A token bucket caps a sender's average rate while letting it burst. Tokens arrive at a fixed rate, and the bucket holds only so many, so an idle sender banks credit it can spend later. Every bit sent costs one token, which makes the long-run average exactly the token rate and the burst at most the bucket's size.

---

Flashcards for this section are as follows:

- token bucket: what does a token bucket limit, and what does it allow? ::@:: It caps the average rate at the rate tokens arrive, and allows a burst no larger than the bucket.
- the mechanism: for a bucket refilled at rate $r$ with room $b$, how does it meter traffic? ::@:: Tokens are added at rate $r$ up to $b$, the scheduler spends one token per bit sent, and it cannot send while it has too few tokens.
- an idle sender: what does an idle sender bank in a token bucket, and what does it do with it? ::@:: Tokens, up to the bucket's capacity, which it spends later as a burst.

## traffic envelope

A traffic envelope is an upper bound on how much data a sender may put on the wire over time. Pacing to a fixed rate is the simplest envelope, a straight line, and a token bucket raises that line by a constant: faster for a while, then slower to stay under the same average. A bucket of rate 1 Mbps and burst 100 kB gives the envelope $A(t) = 10^6 t + 800{,}000$ bits, taking a kilobyte as 1000 bytes.

---

Flashcards for this section are as follows:

- traffic envelope: what is a traffic envelope? ::@:: An upper bound on the total amount of data a sender may transmit over time.
- shaping against pacing: how does a token bucket differ from plain pacing at the same rate? ::@:: It allows a burst above the rate for a while and evens out afterwards, while the average stays the same.
- envelope shape: for a bucket of rate $r$ and burst $b$, what shape does its envelope have on a plot of data against time? ::@:: A line of slope $r$ raised by $b$, since the bucket counts as full at its worst.
- the envelope of a bucket: a token bucket of rate $1\text{ Mbps}$ and burst $100\text{ kB}$, which is $800{,}000$ bits, gives which arrival curve? ::@:: $A(t) = 10^6 t + 800{,}000$ bits, a line of slope $10^6$ raised by $800{,}000$.
- kilobytes to bits: how many bits does a $100\text{ kB}$ burst hold when a kilobyte is taken as $1000$ bytes? ::@:: $100\text{ kB} = 100{,}000\text{ bytes} \times 8\text{ bits/byte} = 800{,}000$ bits.

## burst size

The burst size decides how far ahead of the average a sender may run. An unbounded bucket would let one flow send everything it has queued, filling the bottleneck and stalling every flow behind it. A small bucket keeps the queue short, at the price of smoothing traffic that arrives in clumps. The bucket refills from empty in $b/r$ seconds, so a 100 kB bucket at 1 Mbps refills in 0.8 seconds. A 300 kB burst is 2,400,000 bits, and a full bucket holds only 800,000 of them, so the rest wait 1.6 seconds for tokens at 1 Mbps.

---

Flashcards for this section are as follows:

- burst size: what does the bucket's capacity $b$ decide? ::@:: How far above the average rate a sender may send before it must slow down.
- an unlimited bucket: what happens when the bucket is made very large? ::@:: One flow's burst fills the bottleneck and delays every other flow behind it.
- small bucket and queue length: what does a small burst allowance keep short? ::@:: The queue, because a sender cannot inject more than the bucket's capacity at once.
- the trade: what does a small bucket cost? ::@:: Traffic that arrives in clumps is held back and smoothed, so the sender loses the ability to send a burst when it has one.
- refill time: a token bucket of rate $r$ and burst $b$ takes how long to refill from empty? ::@:: $b$ tokens at $r$ tokens per second gives $b/r$ seconds.
- refilling a $100\text{ kB}$ bucket: a token bucket of rate $1\text{ Mbps}$ and burst $100\text{ kB}$ starts empty; how long until it is full? ::@:: $800{,}000\text{ bits} / 10^6\text{ bits/s} = 0.8$ seconds.
- a 300 kB burst: a sender with a token bucket of rate $1\text{ Mbps}$ and burst $100\text{ kB}$ sends $300\text{ kB}$, which is $2{,}400{,}000$ bits; how long must the rest of the burst wait? ::@:: $2{,}400{,}000 - 800{,}000 = 1{,}600{,}000$ bits to wait for, and $1{,}600{,}000 / 10^6 = 1.6$ seconds.

## deployment

Internet service plans are usually enforced with a shaper rather than by installing a link of the plan's exact speed: each subscriber's traffic is paced to the plan's rate and given a burst allowance. Weighted fair queuing and token buckets are common in service provider and enterprise networks, while most switches still schedule first come first served. A 100 kB burst on a 1 Gbps link goes out in $800{,}000$ bits divided by $10^9$ bits per second, which is $0.8$ ms.

---

Flashcards for this section are as follows:

- how a plan is enforced: how does a service provider give a subscriber a slower link than the cable can carry? ::@:: A shaper paces that subscriber's traffic to the plan's rate and allows a burst on top.
- scheduling in most switches: which scheduling policy do most switches actually run? ::@:: First come first served.
- a burst on a fast link: a $100\text{ kB}$ burst on a $1\text{ Gbps}$ link takes how long to transmit? ::@:: $800{,}000\text{ bits} / 10^9\text{ bits/s} = 0.8$ ms.
