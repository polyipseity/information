---
aliases:
  - ELEC 3120 TCP loss recovery
  - ELEC3120 TCP loss recovery
  - HKUST ELEC 3120 TCP loss recovery
  - HKUST ELEC3120 TCP loss recovery
  - TCP loss recovery
  - fast retransmit
  - loss recovery
  - retransmission timeout
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/TCP_loss_recovery
  - language/in/English
---

# TCP loss recovery

A TCP sender has to notice that a segment never arrived and send it again. Two signals report the loss: a timer that expires with no acknowledgement, and duplicate acknowledgements from a receiver missing the same byte. They differ in how long the sender waits before retransmitting.

---

Flashcards for this section are as follows:

- overview ::@:: A TCP sender detects a lost segment from a timeout or from three duplicate acknowledgements, and retransmits it.
- two signals: which two events tell a sender that a segment was lost? ::@:: The retransmission timer running out, and three duplicate acknowledgements.
- what both signals lead to: what does the sender do after either signal? ::@:: Retransmits the missing segment.

## duplicate acknowledgements

A receiver that gets a segment out of order cannot acknowledge it, since the byte it waits for is still missing, so it sends another acknowledgement naming the same next-expected byte. That repeat is a duplicate acknowledgement: a segment arrived and left a gap before it. One or two can come from ordinary reordering, which leaves a gap a later segment fills. A third cannot, so the missing segment is taken to be lost rather than late.

---

Flashcards for this section are as follows:

- duplicate acknowledgement: the receiver names the same next-expected byte again; what does that report? ::@:: That a segment arrived out of order and left a gap before it.
- out-of-order segment: what does a receiver send when a segment arrives out of order? ::@:: Another acknowledgement naming the same next-expected byte.
- one or two duplicate acknowledgements: what can still explain them? ::@:: Ordinary reordering, which leaves a temporary gap.
- third duplicate acknowledgement: what does it establish? ::@:: That the missing segment is lost, not merely late.

## fast retransmit

The duplicate acknowledgements arrive before the timer would expire. On the third one the sender retransmits the missing segment at once, without waiting for the timer, so a single loss does not stall the connection for a whole timeout.

---

Flashcards for this section are as follows:

- fast retransmit rule: what does the sender do when the third duplicate acknowledgement arrives? ::@:: It retransmits the missing segment at once, without waiting for the timer.

## timeouts

The sender starts a timer when it sends a segment and resends the oldest unacknowledged segment when the timer expires. A loss with no later segment behind it produces no duplicate acknowledgements, so the timer covers that case. It reports a loss later than duplicate acknowledgements do, since it must allow a full round trip plus the time the reply may take. A timeout also drops the congestion window to its initial value, undoing more than a fast retransmit.

---

Flashcards for this section are as follows:

- timer rule: what does the sender retransmit when its retransmission timer expires? ::@:: The oldest unacknowledged segment.
- when only the timer can help: why does the timer still matter when duplicate acknowledgements exist? ::@:: A loss with no later segment behind it produces no duplicate acknowledgements.
- why the timer is slower: why does the timer signal a loss later than duplicate acknowledgements do? ::@:: It must allow a full round trip plus the time the reply may take.
- extra cost: what else does a timeout cost, compared with a fast retransmit? ::@:: It also drops the congestion window to its initial value, so the connection rebuilds its sending rate.
