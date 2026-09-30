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

Congestion control keeps a sender from pushing more traffic into the network than the path can carry. Nothing tells the sender how much room the network has, so it infers it from the acknowledgements it gets back: quick acknowledgements mean room to send more, and acknowledgements that stop mean the path is overloaded. The sender keeps that estimate in a congestion window and revises it on each event.

---

Flashcards for this section are as follows:

- overview ::@:: Congestion control limits a sender to what the path can carry, inferring that limit from the acknowledgements it receives.
- who infers the limit: what does the sender use to estimate the path's room? ::@:: The acknowledgements it receives.
- overload signal: what do acknowledgements that stop arriving tell the sender? ::@:: That the path is overloaded.

## congestion window

The congestion window $CWND$ is the sender's estimate of how much it may have outstanding, kept apart from the receive window that flow control supplies. The sender starts it at one MSS and keeps a slow-start threshold alongside; the two decide how the window grows. The sending window is $\min(RWND, CWND)$ (see [sending window](flow%20control%20(data).md#sending%20window)), so congestion control bounds the connection from the network side and flow control from the receiver side.

---

Flashcards for this section are as follows:

- congestion window: what does $CWND$ estimate? ::@:: How much the sender may have outstanding, given the network's capacity.
- starting value: what value does $CWND$ start from? ::@:: One MSS.
- slow-start threshold: what does $ssthresh$ decide? ::@:: When the window stops doubling and starts growing linearly.

## slow start

Slow start grows the window exponentially: it starts at $CWND = 1$ MSS and adds one MSS for every acknowledgement. One round trip brings back about as many acknowledgements as the window holds segments, so the window doubles per round trip. Once $CWND$ reaches the slow-start threshold, the window grows linearly instead.

---

Flashcards for this section are as follows:

- slow start growth: how much does $CWND$ rise per acknowledgement? ::@:: One MSS per acknowledgement.
- doubling per round trip: $CWND$ grows by one MSS for each acknowledgement; why does that double the window once per round trip? ::@:: A round trip brings back about as many acknowledgements as the window holds segments.
- leaving slow start: once $CWND$ reaches the slow-start threshold, what happens to the window's growth? ::@:: It grows linearly instead of doubling.

## congestion avoidance

Congestion avoidance grows the window linearly once $CWND$ has reached the slow-start threshold. Each acknowledgement adds $MSS/CWND$ to $CWND$, about one MSS per round trip rather than a doubling, since the growth is spread over every acknowledgement of the window. The window keeps growing while no loss is reported, looking for more room a round trip at a time.

---

Flashcards for this section are as follows:

- growth per acknowledgement: how much does $CWND$ rise per acknowledgement during congestion avoidance? ::@:: $MSS/CWND$, about one MSS per round trip.
- why it is linear: why does congestion avoidance add $MSS/CWND$ per acknowledgement instead of one MSS? ::@:: The growth of one MSS per round trip is spread over every acknowledgement of the window.
- probing for room: what does the window do while no loss is reported? ::@:: It keeps growing, looking for more room a round trip at a time.

## fast recovery

Fast recovery replaces the return to slow start when duplicate acknowledgements, rather than a timeout, report the loss. On the third one the sender halves the slow-start threshold and sets $CWND$ to that threshold plus the three segments the duplicate acknowledgements account for, so the window drops by about half instead of to one MSS. Each further duplicate acknowledgement adds one MSS while the missing segment is retransmitted.

---

Flashcards for this section are as follows:

- fast recovery values: the third duplicate acknowledgement arrives while the window is $CWND$; what does the sender set? ::@:: The slow-start threshold to $CWND/2$, and the congestion window to that plus $3$ MSS.
- three segments: why does fast recovery add $3$ MSS to the halved threshold? ::@:: Each duplicate acknowledgement means one more segment has left the network, so the sender counts that room in.
- further duplicate acknowledgements: what does the sender do to $CWND$ for each duplicate acknowledgement after the third? ::@:: It adds one MSS.
- fast recovery versus slow start: the pre-loss window is $CWND$; how far does each reaction drop it? ::@:: Fast recovery to about $CWND/2$, a return to slow start to one MSS.
- ending fast recovery: what does the sender do when the acknowledgement for the retransmitted segment arrives? ::@:: It sets the congestion window to the slow-start threshold and returns to congestion avoidance.

## reno state machine

The transitions also use the duplicate-acknowledgement counter and the slow-start threshold.

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

---

Flashcards for this section are as follows:

- initial state: which state does the sender start in, and what are the default $ssthresh$ and counter values? ::@:: Slow start, with $ssthresh = 64$ KB and the counter at $0$.
- slow start to congestion avoidance: a new acknowledgement arrives with $cwnd \ge ssthresh$; which state does the sender move to? ::@:: Congestion avoidance.
- duplicate-acknowledgement counter reset: which events set the counter back to $0$? ::@:: A new acknowledgement in slow start or congestion avoidance, a timeout, and leaving fast recovery.
- entering fast recovery: from which two states, and on which event, does the sender enter fast recovery? ::@:: From slow start or congestion avoidance, on the third duplicate acknowledgement.
- timeout transitions: which state does a timeout lead to from any of the three states, and what becomes of $cwnd$ and $ssthresh$? ::@:: Slow start, with $ssthresh = cwnd/2$, $cwnd = 1$ MSS, and the counter reset.
