---
aliases:
  - ELEC 3120 selective repeat ARQ
  - ELEC3120 selective repeat ARQ
  - HKUST ELEC 3120 selective repeat ARQ
  - HKUST ELEC3120 selective repeat ARQ
  - Selective Repeat
  - Selective Repeat ARQ
  - selective repeat ARQ
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/selective_repeat_ARQ
  - language/in/English
---

# selective repeat ARQ

Selective repeat keeps the window of go-back-N but lets the receiver hold what arrives early. Only the lost packet is resent, so one loss costs one retransmission instead of a window. The receiver keeps a buffer the size of the window and acknowledges every packet it stores.

---

Flashcards for this section are as follows:

- selective repeat recovery: which packets does the sender resend after a loss? ::@:: Only the packet that timed out.
- the shared window: what does selective repeat keep from go-back-N? ::@:: The sliding window; only the receiver's handling of early arrivals changes.

## sender rules

The sender sends whatever lies inside the window, with a timer on each packet. Acknowledgements for the left edge of the window slide it forward and let new packets in. A timeout resends that one packet.

The window, not the recovery rule, sets the rate when nothing is lost: a window of $8$ packets of $1460$ bytes over a $200\text{ ms}$ round trip moves $58{,}400$ bytes per second, the same as go-back-N.

---

Flashcards for this section are as follows:

- sending: which packets does the sender transmit at any moment? ::@:: Those inside the window, each with its own timer.
- sliding: which acknowledgements move the window? ::@:: Those for the packets at the window's left edge.
- on expiry: what does the sender resend when the timer for packet $n$ expires? ::@:: Packet $n$ alone.
- throughput with a window of $8$: over a $200\text{ ms}$ round trip, what does selective repeat reach with a window of $8$ packets of $1460$ bytes, and does it differ from go-back-N? ::@:: $8 \times 1460 = 11{,}680$ bytes per round trip, and $11{,}680\text{ bytes} / 0.2\text{ s} = 58{,}400$ bytes per second, the same as go-back-N, since the window sets the rate.

## partial acknowledgement

The receiver acknowledges every packet as it arrives, including the packets that arrived early. An acknowledgement for packet $m$ says that packet $m$ arrived and says nothing about the packets before it.

The sender may slide its window only over the positions that are acknowledged, so the window stops at the lowest missing packet. The acknowledgements for the packets behind the hole are held rather than acted on. A timeout resends that packet, and the hole is filled when it arrives.

One loss: packets $3$ to $8$ are sent and packet $3$ is lost. The acknowledgements for $4$ to $8$ arrive and the receiver stores them, but the window stays at $3$, because the slide needs the left edge. The retransmitted packet $3$ arrives and is accepted, and the window then jumps from $3$ to $9$, past the six packets it had already stored, so the sender sends six new packets to fill that space.

---

Flashcards for this section are as follows:

- the acknowledgement: what does an acknowledgement for packet $m$ say about the packets before it? ::@:: Nothing; it says that packet $m$ arrived and nothing about the rest.
- the hole: where does the window stop while a packet is missing? ::@:: At the lowest missing packet, since the slide needs the left edge.
- the trade: what does the partial acknowledgement cost the sender? ::@:: The window cannot slide past the hole, so the sender's rate stays at what the window allows until the missing packet arrives.
- acknowledgements behind the hole: what does the sender do with the acknowledgements for packets that arrived behind a missing one? ::@:: It holds them instead of acting on them, because the window slides only over an acknowledged left edge.

## receiver buffer

The receiver buffers out-of-order packets instead of discarding them, and acknowledges each one as it arrives. No more than a window can arrive ahead of the gap, so a buffer of that size is enough. <p> ![selective repeat sliding window: the sender's row shows packets 0 to 4 sent, 5 to 8 acknowledged and 9 to 12 in flight, while the receiver's row shows packets 0 to 4 received, packet 5 lost and packets 6 to 8 buffered as out of order](../../../../archives/Wikimedia%20Commons/Selectiverepeat.svg)

A window of $8$ packets needs $11{,}680$ bytes of buffer, against the single packet a go-back-N receiver keeps. A retransmission of a packet the receiver already holds is discarded, and the acknowledgement is repeated.

---

Flashcards for this section are as follows:

- acknowledging: when does the receiver acknowledge an out-of-order packet? ::@:: As soon as it arrives and is stored.
- why the buffer can be that small: why can no more than a window of data arrive ahead of a missing packet? ::@:: The sender never has more than a window of packets outstanding.
- buffer space for a window of $8$: with a window of $8$ packets of $1460$ bytes, how much buffer does a selective repeat receiver need? ::@:: $8 \times 1460 = 11{,}680$ bytes, one slot for each position in the window.
- a repeated packet: what does the receiver do with a retransmission of a packet it already holds? ::@:: It discards it and repeats the acknowledgement.
- the figure: what does the selective repeat sliding window diagram show? <p> ![selective repeat sliding window: the sender's row shows packets 0 to 4 sent, 5 to 8 acknowledged and 9 to 12 in flight, while the receiver's row shows packets 0 to 4 received, packet 5 lost and packets 6 to 8 buffered as out of order](../../../../archives/Wikimedia%20Commons/Selectiverepeat.svg) ::@:: Two rows of numbered slots: the sender's window with packets sent, acknowledged and in flight, and the receiver's window with a lost packet and the packets behind it kept in the buffer instead of discarded.
- buffer against go-back-N: how much buffer does a selective repeat receiver keep, and how much does a go-back-N receiver keep? ::@:: A buffer the size of the window, one slot per window position, against the single packet a go-back-N receiver holds.

## sequence number space

The sequence numbers have to outnumber the window, or a new packet cannot be told apart from an old one. With $k$ bits of sequence number there are $2^k$ values, and the sender's window must be at most half of them, because the receiver may still be holding a packet whose number a new packet reuses. With $3$-bit numbers there are $8$ values, so the window is at most $4$. A window of $8$ needs $4$ bits, which give $16$ values.

Go-back-N does not need that margin, since its receiver discards the packets that arrive early and never has two packets with the same number in hand at once.

---

Flashcards for this section are as follows:

- the constraint: with $k$ bits of sequence number, how many values exist, how many may the window cover, and why only half? ::@:: $2^k$ values, so the window covers at most $2^k / 2 = 2^{k-1}$, half the space; the receiver may still hold a packet whose number a new packet reuses, and the two must not be confused.
- three bits: with $3$-bit sequence numbers, what is the largest window a selective repeat sender may use? ::@:: $2^3 = 8$ values, half of which is $8 / 2 = 4$.
- a window of $8$: how many bits of sequence number does a window of $8$ packets need? ::@:: A window of $8$ needs $2 \times 8 = 16$ values, and $2^4 = 16$, so $4$ bits.
- the difference from go-back-N: why does go-back-N not need the same margin? ::@:: Its receiver discards the packets that arrive early, so it never holds two packets with the same number at once.

## stuck window

After a loss, later packets are acknowledged and stored, but the window cannot slide past the gap. The application cannot read past it either, since the receive buffer hands the reader bytes in order and everything behind the hole waits.

The hole costs time rather than data: on a $200\text{ ms}$ round trip the window stays stuck until the retransmitted packet arrives, and selective repeat resends $1460$ bytes where go-back-N resends $11{,}680$.

---

Flashcards for this section are as follows:

- application progress: what does the missing packet do to the application reading the stream? ::@:: The application stalls, since the receive buffer delivers bytes in order and everything behind the hole waits.
- recovery order: in which order does data reach the application after the missing packet arrives? ::@:: In order, with the buffered packets flushed out behind it.
- how long the window stays stuck: on a path with $100\text{ ms}$ of propagation delay each way and a $250\text{ ms}$ timer, how long does a selective repeat window stay stuck after one packet is lost? ::@:: The timer fires at $250\text{ ms}$, then the retransmission takes a round trip of $100\text{ ms}$ out and $100\text{ ms}$ back, so the window is stuck for about $250 + 200 = 450\text{ ms}$.
- bytes saved against go-back-N: with a window of $8$ packets of $1460$ bytes, how much data does selective repeat avoid resending when one packet is lost? ::@:: Go-back-N resends the window, $8 \times 1460 = 11{,}680$ bytes; selective repeat resends only $1460$, so it saves $11{,}680 - 1460 = 7 \times 1460 = 10{,}220$ bytes, $7$ packets.
