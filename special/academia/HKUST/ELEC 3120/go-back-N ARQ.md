---
aliases:
  - ELEC 3120 go-back-N ARQ
  - ELEC3120 go-back-N ARQ
  - Go-Back-N
  - Go-Back-N ARQ
  - HKUST ELEC 3120 go-back-N ARQ
  - HKUST ELEC3120 go-back-N ARQ
  - go-back-N ARQ
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/go-back-N_ARQ
  - language/in/English
---

# go-back-N ARQ

Go-back-N keeps a window of packets in flight and recovers from a loss by resending everything from the lost packet onwards. The receiver holds no out-of-order data, so one buffer slot is enough. One loss costs a whole window of retransmissions.

---

Flashcards for this section are as follows:

- go-back-N recovery: which packets does the sender resend after a loss? ::@:: The lost packet and every packet after it in the window.
- receiver buffer: how much out-of-order data does the receiver hold? ::@:: None, since anything other than the next expected packet is discarded.

## pipelining

Sending without waiting keeps the link busy. The window has to cover a round trip, else the sender runs dry before the first acknowledgement returns.

On a $50\text{ Mbps}$ path with $100\text{ ms}$ of propagation delay each way, so a round trip of about $200\text{ ms}$, a window of $8$ packets of $1460$ bytes moves $58{,}400$ bytes per second, eight times what [stop-and-wait](stop-and-wait%20ARQ.md) reaches on the same path.

---

Flashcards for this section are as follows:

- the gain: what does go-back-N buy over stop-and-wait? ::@:: Several packets travel at once, so the link stays busy while acknowledgements come back.
- window size: what must the window cover for the link to stay full? ::@:: One round trip of transmission at the link's rate.
- throughput with a window of $8$: on a $50\text{ Mbps}$ path with a $200\text{ ms}$ round trip, what does go-back-N reach with a window of $8$ packets of $1460$ bytes? ::@:: $8 \times 1460 = 11{,}680$ bytes per round trip, so $11{,}680 \div 0.2\text{ s} = 58{,}400$ bytes per second. The link carries $50\text{ Mbps} = 6{,}250{,}000\text{ bytes/s}$, so that is $58{,}400 \div 6{,}250{,}000 \approx 0.9\%$ of it.
- window to fill the path: on a $50\text{ Mbps}$ path with a $200\text{ ms}$ round trip, how many packets of $1460$ bytes fill the path? ::@:: The bandwidth-delay product is $50\text{ Mbps} \times 0.2\text{ s} = 10\text{ Mbit} = 1.25\text{ MB} = 1{,}250{,}000\text{ bytes}$, and $1{,}250{,}000 \div 1460 \approx 856$ packets.
- stop-and-wait on the same path: on a $50\text{ Mbps}$ path with $100\text{ ms}$ of propagation delay each way, so a round trip of about $200\text{ ms}$, what does stop-and-wait reach with packets of $1460$ bytes? ::@:: One packet per round trip, $1460 \div 0.2 = 7300$ bytes per second, and $7300 \times 8 = 58{,}400$ bytes per second with a window of $8$ packets.

## sender rules

The sender sends up to $N$ packets without an acknowledgement, with a timer on each. An acknowledgement slides the window forward. When a timer expires, the sender resends that packet and everything after it in the window.

---

Flashcards for this section are as follows:

- in flight: in go-back-N with window size $N$, how many unacknowledged packets may be outstanding? ::@:: Up to $N$, one timer per packet.
- cost of one loss: on a path with $100\text{ ms}$ of propagation delay each way and a $250\text{ ms}$ timer, a window of $8$ packets is in flight and the first packet is lost; how many packets does go-back-N resend? ::@:: All $8$, the lost packet and the $7$ after it: $8 \times 1460 = 11{,}680$ bytes, once the timer expires.

## cumulative acknowledgement

An acknowledgement carries the number of the next packet the receiver expects, and the number counts from the start of the stream, so it is cumulative. An acknowledgement of $n$ means that every packet before $n$ arrived, and in order. One acknowledgement therefore retires many timers at once.

The sender reads the same number two ways: everything below it is safely held, and everything from it upwards is either lost or was discarded on arrival.

---

Flashcards for this section are as follows:

- cumulative acknowledgement: what does an acknowledgement of $n$ mean in go-back-N? ::@:: Every packet before $n$ arrived, and in order.
- one acknowledgement, many timers: what does a single cumulative acknowledgement retire? ::@:: Every timer for the packets before the number it carries.
- the two readings: what does the number in a cumulative acknowledgement tell the sender? ::@:: Which packets are safely held, and which are still missing or were discarded.
- where the number counts from: what does the sequence number in a cumulative acknowledgement count from? ::@:: The start of the stream, not the start of the current window, which is what makes one number cover every earlier packet.

## partial acknowledgement

A partial acknowledgement covers some of the outstanding packets and not others: an acknowledgement that says packet $5$ arrived while packet $3$ is still missing. In go-back-N that case cannot arise.

The receiver accepts only the next expected packet and discards everything else, so it cannot hold packet $5$ and acknowledge it while packet $3$ is still missing. Its acknowledgement therefore always names the first missing packet, and the sender learns the state of the whole window from that one number: what it has, and what it has to send again. A partial acknowledgement belongs to [selective repeat](selective%20repeat%20ARQ.md), where the receiver keeps the packets that arrive early and acknowledges them one by one.

---

Flashcards for this section are as follows:

- partial acknowledgement: what is a partial acknowledgement? ::@:: An acknowledgement that covers some of the outstanding packets and not others, saying a later packet arrived while an earlier one is still missing.
- impossible in go-back-N: why can a partial acknowledgement not arise in go-back-N? ::@:: The receiver discards any packet that is not the next one it expects, so it never holds a later packet while an earlier one is missing.
- where partial acknowledgements live: which protocol acknowledges packets that arrived early, one by one? ::@:: Selective repeat, whose receiver stores the early packets and acknowledges each on arrival.

## timers

The timers decide when a loss is noticed, and how a loss is repaired depends on how they are set.

---

Flashcards for this section are as follows:

- what the timers decide: what do the timers decide? ::@:: When a loss is noticed, since no acknowledgement arrives while a packet or its acknowledgement is lost.
- one timer per packet: what is the textbook rule for timers in go-back-N? ::@:: One timer for each packet in the window, all running for the same length.

### equal timers

The textbook rule is one timer per packet, all of the same length. The oldest outstanding packet's timer was started first, so it expires first, and the recovery resends that packet and everything after it, which covers every packet whose timer would have fired later.

---

Flashcards for this section are as follows:

- equal timers: which expiry triggers the recovery when every timer has the same length? ::@:: The oldest outstanding packet's, because it was started first.
- why it covers the rest: why does the oldest expiry settle the whole window? ::@:: The recovery resends that packet and every packet behind it, so the packets whose timers would have fired later are sent again anyway.

### single timer

Many implementations keep one timer for the oldest unacknowledged packet instead of one for each. When an acknowledgement moves the window, that timer is restarted for the new oldest packet. The behaviour matches the per-packet rule, because the packets are sent in order and the oldest is always the first to expire.

---

Flashcards for this section are as follows:

- single timer: what does an implementation that keeps one timer for the oldest unacknowledged packet restart when an acknowledgement arrives? ::@:: That timer, for the new oldest unacknowledged packet.
- the same behaviour: why does a single timer behave like one timer per packet? ::@:: The packets are sent in order, so the oldest unacknowledged packet is always the first one to expire.

### unequal timers

Timers may differ in length. The shortest one fires first, and the recovery starts from that packet. The loss is not repaired: the receiver is still waiting for the earlier missing packet, so it discards the retransmitted packets again as out of order. The repair happens only when the timer of the earliest missing packet fires, and the bandwidth spent in between is wasted, since those packets are carried a second time and thrown away a second time.

---

Flashcards for this section are as follows:

- unequal timers: the timers differ in length and a later packet's timer fires first; what happens? ::@:: The recovery starts from that later packet, the receiver discards the retransmission as out of order, and the real loss is repaired only when the earliest missing packet's timer fires.
- the waste: what is wasted when a later packet's timer fires before the earliest missing packet's? ::@:: The bandwidth of that retransmission, since the receiver is still waiting for the earlier packet and discards it again.
- the unchanged answer: what does the receiver send while the earlier packet is still missing? ::@:: The same acknowledgement as before, naming the packet it is still waiting for.

### spurious timeout

A timer can fire when nothing was lost. The frame and its acknowledgement both arrived, and the acknowledgement was merely late. The sender cannot know that, so it resends, and the receiver discards the duplicate and repeats the acknowledgement. Karn's algorithm refuses to take a round-trip time sample from a retransmitted packet, because the sample may belong to the first transmission or to the retransmission, and the two differ.

---

Flashcards for this section are as follows:

- spurious timeout: what does the sender do when its timer fires although the frame and its acknowledgement both arrived? ::@:: It resends, and the receiver discards the duplicate and repeats the acknowledgement.
- Karn's algorithm: why is no round-trip time sample taken from a retransmitted packet? ::@:: The sample is ambiguous, because it may belong to the first transmission or to the retransmission, and the two differ.
- why the resend happens anyway: why does the sender resend when the acknowledgement was only late? ::@:: It cannot tell that the frame and its acknowledgement both arrived, so it takes the expired timer for a loss and resends.

### timer restart

When a cumulative acknowledgement arrives, the timer of the oldest unacknowledged packet is restarted, not every timer. The packets behind it keep the deadlines they were given when they were sent, since they have been travelling longer and their remaining time is smaller.

---

Flashcards for this section are as follows:

- timer restart: which timer is restarted when a cumulative acknowledgement arrives? ::@:: The timer of the oldest unacknowledged packet, not the timers of the packets behind it.
- the reason: why do the timers of the packets behind it keep their deadlines? ::@:: They were set when those packets were sent, and they have been travelling longer, so their remaining time is smaller.

## recovery

When the timer for packet $k$ expires, the sender resends packet $k$ and every packet after it in the window. The receiver had discarded the packets that arrived after $k$ was lost, because it accepts only the next expected packet, so those packets are carried a second time and accepted one at a time. <p> ![go-back-N sliding window: the sender's row shows packets 0 to 4 sent, 5 to 8 acknowledged and 9 to 12 in flight, while the receiver's row shows packets 0 to 4 received, packet 5 lost and packets 6 to 8 discarded as out of order](../../../../archives/Wikimedia%20Commons/Gobackn.svg)

The numbers for one loss: a window of $8$ packets of $1460$ bytes on a $50\text{ Mbps}$ path with a $200\text{ ms}$ round trip, and a timer of $250\text{ ms}$, with packet $3$ lost. The timer for packet $3$ fires, and the sender resends packets $3$ to $8$, which is $6$ packets and $6 \times 1460 = 8760$ bytes. The receiver takes them one at a time and answers each, and the six acknowledgements retire the six timers.

---

Flashcards for this section are as follows:

- the recovery: which packets does the sender resend when the timer for packet $k$ expires? ::@:: Packet $k$ and every packet after it in the window.
- why they are sent again: why does the receiver need the packets behind the loss again? ::@:: It discarded them when they arrived out of order, since it accepts only the next expected packet.
- one loss in numbers: a window of $8$ packets of $1460$ bytes, a $250\text{ ms}$ timer and a $200\text{ ms}$ round trip, with packet $3$ lost; how much is resent? ::@:: Packets $3$ to $8$, which is $8 - 3 + 1 = 6$ packets and $6 \times 1460 = 8760$ bytes.
- the acknowledgements: what do the receiver's acknowledgements do after the retransmission? ::@:: One per packet as each is accepted, and they retire the timers of the retransmitted packets.
- the figure: what does the go-back-N sliding window diagram show, and which packet is lost? <p> ![go-back-N sliding window: the sender's row shows packets 0 to 4 sent, 5 to 8 acknowledged and 9 to 12 in flight, while the receiver's row shows packets 0 to 4 received, packet 5 lost and packets 6 to 8 discarded as out of order](../../../../archives/Wikimedia%20Commons/Gobackn.svg) ::@:: Two rows of numbered slots: the sender has packets 0 to 4 sent, 5 to 8 acknowledged and 9 to 12 in flight, while the receiver has received 0 to 4, lost packet 5 and discarded packets 6 to 8 as out of order.
- draw the go-back-N window: what does the diagram show about the sender and the receiver after a loss? ::@:: The sender holds packets in three states, sent, acknowledged and in flight, while the receiver has a hole where the lost packet was and has discarded the packets that arrived behind it.

## receiver rules

The receiver acknowledges the next sequence number it expects, and only that one. A packet with an unexpected number is dropped, duplicate or early arrival alike, since the sender will send it again.

If the receiver expects packet 3 and packets 4 to 8 arrive first, each is discarded, and the acknowledgement it sends back is for 3.

---

Flashcards for this section are as follows:

- acknowledgement: which sequence number does a go-back-N receiver acknowledge? ::@:: The next one it expects.
- early arrival: what does the receiver do with a packet that skips ahead? ::@:: It discards it, since the sender will resend it in order.
- duplicate: what does the receiver do with a repeated packet? ::@:: It discards it and acknowledges the next expected number again.
- packets behind the loss: a go-back-N receiver expects packet 3 and packets 4 to 8 arrive first; what does it do with them? ::@:: It discards each one and acknowledges 3 again, so the sender has to send them all again.
