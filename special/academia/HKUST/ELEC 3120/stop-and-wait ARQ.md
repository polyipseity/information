---
aliases:
  - ELEC 3120 stop-and-wait ARQ
  - ELEC3120 stop-and-wait ARQ
  - HKUST ELEC 3120 stop-and-wait ARQ
  - HKUST ELEC3120 stop-and-wait ARQ
  - Stop-and-wait ARQ
  - alternating bit protocol
  - stop and wait
  - stop-and-wait ARQ
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/stop-and-wait_ARQ
  - language/in/English
---

# stop-and-wait ARQ

Stop-and-wait recovers from loss by sending one packet and waiting for its acknowledgement before the next. A timer covers that wait, and its expiry means the packet or the acknowledgement went missing.

---

Flashcards for this section are as follows:

- stop-and-wait: what does the sender do between packets? ::@:: It sends one packet and waits for that packet's acknowledgement.
- how a loss is noticed: which event tells the sender that something was lost? ::@:: Its timer expires before the acknowledgement arrives.

## sender rules

The sender numbers each packet, transmits it, and starts a timer. An acknowledgement for that packet moves it to the next one. Timer expiry resends the same packet and restarts the timer.

The timer has to outlast a round trip. With 100 ms of propagation delay each way, the crossing costs 200 ms, and pushing a 1460-byte packet onto a 50 Mbps link adds 0.23 ms once; the acknowledgement's own push time is negligible. That round trip is 200.23 ms, against the 200.46 ms that twice the one-way delay would give. A timer of 250 ms covers it and resends a lost packet.

---

Flashcards for this section are as follows:

- sender loop: what are the three steps a stop-and-wait sender repeats? ::@:: Label the packet with a sequence number, transmit it, and start a timer.
- on acknowledgement: what does the sender do when the acknowledgement arrives? ::@:: It sends the next packet.
- on expiry: what does the sender do when the timer goes off? ::@:: It resends that packet and restarts the timer.
- retransmission timer: on a path with $100\text{ ms}$ of propagation delay each way, how long must a stop-and-wait retransmission timer run before it can fire without retransmitting a packet still in flight? ::@:: Longer than the round trip: $100\text{ ms}$ out, $100\text{ ms}$ back, and the packet's push time once, so about $200\text{ ms}$.

## receiver rules

The receiver acknowledges every packet it accepts, naming it. It ignores a corrupted packet rather than ask for a resend, since the sender's timer resends it anyway.

A repeated packet is discarded on its sequence number and acknowledged again, so the application sees the data once. One lost packet costs one retransmission, because only one is ever in flight.

---

Flashcards for this section are as follows:

- receiver response: what does the receiver do with a packet it accepts? ::@:: It sends an acknowledgement naming that packet.
- corrupted packet: why does the receiver ignore a corrupted packet instead of asking for a resend? ::@:: The sender's timer will resend it anyway.
- repeated packet: what does the receiver do with a packet it has already accepted? ::@:: It discards it on its sequence number and acknowledges it again.
- retransmissions per loss: how many retransmissions does one lost packet cost in stop-and-wait, and what makes that enough? ::@:: One retransmission, since only one packet is ever in flight, so nothing else needs resending.

## transmission outcomes

One frame leaves the sender with four outcomes, only two of which it can tell apart. <p> ![stop-and-wait time diagram: two lifelines for sender and receiver, a frame 0 acknowledged by ACK 0, a frame 1 lost and sent again after the timer expires, and a frame 2 whose acknowledgement is lost, so the frame is sent again and the receiver discards the duplicate](attachments/stop_and_wait.svg)

---

Flashcards for this section are as follows:

- the four outcomes: what are the four outcomes of sending one frame? ::@:: The frame and its acknowledgement arrive, the frame is lost, the acknowledgement is lost, or the acknowledgement arrives after the timer has fired.
- the figure: what does the stop-and-wait time diagram show? <p> ![stop-and-wait time diagram: two lifelines for sender and receiver, a frame 0 acknowledged by ACK 0, a frame 1 lost and sent again after the timer expires, and a frame 2 whose acknowledgement is lost, so the frame is sent again and the receiver discards the duplicate](attachments/stop_and_wait.svg) ::@:: A sender and a receiver lifeline, a frame that is acknowledged, a frame that is lost and sent again after the timer expires, and a frame whose acknowledgement is lost, so the frame is sent again and the receiver discards the duplicate.

### delivered frame

The frame reaches the receiver, which acknowledges it, and the acknowledgement arrives before the timer expires, so the sender passes to the next frame. The link carried one frame and one acknowledgement, and the transfer took one round trip.

---

Flashcards for this section are as follows:

- delivered frame: what happens when the frame and its acknowledgement both arrive before the timer fires? ::@:: The sender passes to the next frame, and the link carried the frame once.
- the cost: how long does a delivered frame take from the sender's point of view? ::@:: One round trip.

### lost frame

The frame never reaches the receiver. No acknowledgement comes, the timer expires, and the sender sends the frame again. The receiver sees the frame for the first time and acknowledges it. One round trip is lost, and the frame is carried twice.

---

Flashcards for this section are as follows:

- lost frame: what happens when the frame never reaches the receiver? ::@:: The timer expires, the sender resends it, and the receiver accepts it then, so the frame is carried twice.
- the cost: what is lost when the frame is lost? ::@:: One round trip, plus the wait for the timer to expire.

### lost acknowledgement

The frame reaches the receiver, which acknowledges it, but the acknowledgement never reaches the sender. The timer expires and the frame is sent again. The receiver recognises the repeated sequence number, discards the copy, and acknowledges again; that second acknowledgement reaches the sender, which moves on. The data is delivered once, and the frame was carried twice.

---

Flashcards for this section are as follows:

- lost acknowledgement: what happens when the frame arrives but its acknowledgement does not? ::@:: The timer expires, the sender resends the frame, the receiver discards the duplicate and acknowledges again, and the data is still delivered once.
- frames per lost acknowledgement: when a frame's acknowledgement is lost, how many times does the link carry the frame, and what ends the exchange? ::@:: Twice; the receiver's second acknowledgement reaches the sender, which moves on.

### late acknowledgement

The frame reaches the receiver, which acknowledges it, but the acknowledgement arrives after the timer has already fired. The sender resends the frame, and the receiver discards it and repeats the acknowledgement, exactly as in the lost-acknowledgement case. The sender cannot tell this from a lost frame: in both cases no acknowledgement arrived before the timer.

---

Flashcards for this section are as follows:

- late acknowledgement: what happens when the acknowledgement arrives after the timer has fired? ::@:: The sender has already resent the frame, the receiver discards the copy and repeats the acknowledgement, and the sender moves on.
- the blind spot: which two outcomes can the sender not tell apart? ::@:: A lost frame and a lost or late acknowledgement, since in both cases no acknowledgement arrived before the timer fired.

## timer choice

The timer's length trades duplicates against idle time. Set too short, the timer resends a packet still in flight; set too long, it leaves the sender idle after a loss.

---

Flashcards for this section are as follows:

- the choice: what two mistakes can the length of the retransmission timer cause? ::@:: A timer below the round trip, which sends duplicates on a path that has lost nothing, and a timer far above it, which leaves the sender idle after a loss.
- the evidence: what is the sender's only evidence that a packet or its acknowledgement was lost? ::@:: Its timer expiring without an acknowledgement.

### timer shorter than the round trip

With a $200\text{ ms}$ round trip, a $150\text{ ms}$ timer expires while the frame is still in flight, so the sender resends it. The receiver delivers the first copy and discards the second, and the link has carried every frame twice.

---

Flashcards for this section are as follows:

- a short timer: a $150\text{ ms}$ timer on a path with a $200\text{ ms}$ round trip; what happens on a path that has lost nothing? ::@:: The timer expires while the frame is still in flight, so every frame is sent twice and the receiver discards the second copy.
- the waste: what is wasted when the timer is shorter than the round trip? ::@:: The link's capacity, since every frame is carried twice and the second copy is discarded.

### timer longer than the round trip

Set above the round trip, the timer costs only the idle wait after a loss, since every acknowledgement arrives before it fires.

---

Flashcards for this section are as follows:

- a long timer: what does a timer far above the round trip cost? ::@:: The sender stays idle after a loss for the whole timeout before it repairs it.
- the trade: what does a long timer buy? ::@:: No duplicate frames, because the acknowledgement always arrives before the timer fires.

### cost of a loss

A lost frame costs the timeout and then another round trip: a $250\text{ ms}$ timeout on a $200\text{ ms}$ path costs $450\text{ ms}$ before the data moves again. A lost acknowledgement costs the same, since the sender cannot tell the two apart. Every extra millisecond of timeout is paid on every loss.

---

Flashcards for this section are as follows:

- the price of a loss: a $250\text{ ms}$ timeout on a path with a $200\text{ ms}$ round trip; how long before the data moves again after a lost frame? ::@:: $250\text{ ms} + 200\text{ ms} = 450\text{ ms}$, the timeout and then another round trip for the retransmission.
- the price of a lost acknowledgement: does a lost acknowledgement cost the sender less than a lost frame? ::@:: No, it costs the same, since the sender cannot tell the two cases apart.

## sequence numbers

Numbers serve reliability, not reassembly. Reassembly could rest on a convention, such as filling rows in order; a retransmission cannot, since a copy of packet 3 looks like packet 4, or like a late copy of an earlier packet, unless the packet says which it is.

One bit is enough, because only one packet is ever in flight. It alternates between $0$ and $1$ and flips on every successful transfer, so a packet carrying the bit the sender waits for is a duplicate rather than new data.

---

Flashcards for this section are as follows:

- why numbers are needed: what breaks without sequence numbers? ::@:: A retransmitted packet cannot be told apart from a new one, so a duplicate is accepted as fresh data.
- why reassembly is not the reason: what could replace sequence numbers for reassembly? ::@:: A convention, such as writing each packet into the next row of the file.
- one bit: with at most two packets in flight, how many bits does the sequence number need, and which values does it take? <!-- check: ignore-line[two_sided_calc_warning]: conceptual, the givens are in words --> ::@:: One bit, alternating between $0$ and $1$.
- why one bit is enough: why does a single bit carry the whole job in stop-and-wait? ::@:: Only one packet is ever in flight, and the bit flips on every successful transfer, so a repeat of the current bit is a duplicate.

## throughput

The link sits idle for one round trip after every packet, so throughput tops out at one packet per round trip, $MSS/RTT$, with $MSS$ the maximum segment size and $RTT$ the round-trip time. A wider pipe does not help, because the sender waits rather than fills it. A window lets several packets travel before the first acknowledgement returns.

Take a path of $50\text{ Mbps}$ with a $200\text{ ms}$ round trip, carrying packets of $1460$ bytes: stop-and-wait moves one packet per round trip, which is $1460/0.2 = 7300$ bytes per second, or $7300 \times 8 = 58{,}400$ bits per second, about $58{,}400/50{,}000{,}000 \approx 0.12\%$ of the link, so filling the path needs about $6{,}250{,}000/7300 \approx 856$ packets in flight. A window of $8$ packets moves $8 \times 1460 = 11{,}680$ bytes per round trip, which is $58{,}400$ bytes per second.

---

Flashcards for this section are as follows:

- idle time: for how long does the link stay idle after each packet? ::@:: One round trip, which is the wait for the acknowledgement.
- best throughput: what is the highest throughput stop-and-wait can reach, in terms of the maximum segment size $MSS$ and the round-trip time $RTT$? ::@:: $MSS/RTT$, one packet per round trip.
- does a faster link help? ::@:: Little: the sender waits for an acknowledgement instead of filling the link, so the round trip sets the pace.
- what a window does: what does a window let the sender do that stop-and-wait does not? ::@:: Send several packets before the first acknowledgement returns, rather than one packet per round trip.
- time to send a file: how long does stop-and-wait take to send a $1\text{ MB}$ file as $1460$-byte packets over a $200\text{ ms}$ round trip? ::@:: $1\text{ MB} = 1{,}000{,}000$ bytes, so $1{,}000{,}000/1460 \approx 685$ packets, one round trip each, and $685 \times 0.2\text{ s} = 137\text{ s}$.
- what a window buys: over a $200\text{ ms}$ round trip, what does a window of $8$ packets of $1460$ bytes reach, and how long does a $1\text{ MB}$ file take? ::@:: $8 \times 1460 = 11{,}680$ bytes per round trip, so $11{,}680/0.2 = 58{,}400$ bytes per second, and $1{,}000{,}000/11{,}680 \approx 86$ round trips, about $86 \times 0.2 = 17.2\text{ s}$.
