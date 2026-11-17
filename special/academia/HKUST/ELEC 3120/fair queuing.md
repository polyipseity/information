---
aliases:
  - ELEC 3120 fair queuing
  - ELEC3120 fair queuing
  - HKUST ELEC 3120 fair queuing
  - HKUST ELEC3120 fair queuing
  - WFQ
  - fair queueing
  - fair queuing
  - weighted fair queueing
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/fair_queuing
  - language/in/English
---

# fair queuing

Fair queuing is how a router enforces a fair division of its output link. A plain queue serves packets in arrival order, so a sender that sends more gets more. Fair queuing gives each flow its own queue and serves the queues in turn, approximating an ideal schedule that shares out link time. It is the device-level form of [max-min fairness](max-min%20fairness.md).

---

Flashcards for this section are as follows:

- fair queuing: what does fair queuing enforce at a router? ::@:: A fair division of the output link among competing flows.
- the problem it solves: what does a single first-come first-served queue do to shares? ::@:: It serves in arrival order, so a sender that sends more packets receives proportionally more of the link.
- device-level fairness: fair queuing is the device-level form of which fairness rule? ::@:: Max-min fairness.

## per-flow queues

A fair queuing router keeps one queue per flow, each in arrival order. <p> ![three coloured flows arriving at a router funnel, each into its own queue weighted w1, w2 or w3, with each queue served at rate R1, R2 or R3 into one link of rate R](../../../../archives/Wikimedia%20Commons/QoS%20weighted%20fair%20queuing.svg)

A packet that arrives for a full queue is dropped. The router stays work-conserving: the link is never idle while any queue holds a packet.

---

Flashcards for this section are as follows:

- queue per flow: how many queues does a fair queuing router keep? ::@:: One per flow.
- round robin: how does the scheduler choose among the queues? ::@:: It serves them in turn, one after another.
- full queue: what happens to a packet that arrives for a queue with no room? ::@:: It is dropped, as in any other queue.
- weighted queues, drawn: ![three coloured flows arriving at a router funnel, each into its own queue weighted w1, w2 or w3, with each queue served at rate R1, R2 or R3 into one link of rate R](../../../../archives/Wikimedia%20Commons/QoS%20weighted%20fair%20queuing.svg) ::@:: One queue per flow, a weight on each queue, each queue served at its own reserved rate into the one shared link.
- drawing the router: how is a fair queuing router drawn, from the arriving flows to the one link of rate $R$? ::@:: A funnel taking the flows, one queue per flow with its weight above it, a reserved rate out of each queue, and the one shared link. <p> ![three coloured flows arriving at a router funnel, each into its own queue weighted w1, w2 or w3, with each queue served at rate R1, R2 or R3 into one link of rate R](../../../../archives/Wikimedia%20Commons/QoS%20weighted%20fair%20queuing.svg)
- work conserving: with one queue per flow, when is the link idle? ::@:: Only when every queue is empty, so a busy flow fills the gaps an idle one leaves.

## packet sizes

Handing each flow one packet in turn gives every flow the same number of packets, not the same number of bits. A flow sending 1500-byte frames and a flow sending 500-byte frames each get one turn, so the first puts 12000 bits on the wire and the second 4000, three times the service.

A 1500-byte packet occupies a link of rate $R$ for $1500 \times 8/R$ seconds, which is $120\ \mu s$ on a 100 Mbps link, and a 500-byte packet for $40\ \mu s$. The ideal schedule then hands out turns of link time instead of turns of packets, switching after every bit, so each flow receives the same number of bits whatever sizes its packets are. A router cannot pause a packet that is on the wire, so the scheme is a standard to approximate, not a schedule to run.

On a 100 Mbps link with three active flows, each flow ends up with about 33 Mbps.

---

Flashcards for this section are as follows:

- why round robin fails: what makes round robin unfair between flows? ::@:: Packet sizes differ, so a flow with large packets carries more bits in the same number of turns.
- turn duration: a packet of $1500$ bytes crosses a link of rate $R$; how long does it occupy the link? ::@:: $1500 \times 8 = 12000$ bits, so $12000/R$ seconds; at $R = 100\text{ Mbps}$ that is $12000/10^8 = 120\ \mu s$.
- bit-by-bit round robin: what does the ideal schedule hand out in each turn? ::@:: One bit of link time, switching to the next flow after every bit.
- why it is imaginary: why can a real router not serve bit by bit? ::@:: Once a packet starts, the router cannot pause it and resume later.
- unequal packet sizes: two flows share one link and send packets of $1500\text{ bytes}$ and $500\text{ bytes}$; how many bits does each put on the wire in one turn of round robin? ::@:: $1500 \times 8 = 12000$ bits and $500 \times 8 = 4000$ bits, so the flow with the larger packets takes $12000/4000 = 3$ times the service.
- what packet size changes: two flows have the same reserved rate but different packet sizes; what does the size change, and what does it leave alone? ::@:: It changes the order in which the packets leave the router, not the share of bits each flow receives over a second.

## virtual time

The ideal is generalized processor sharing: every flow is served at the same time, each at a fixed fraction of the link. A router serves one packet at a time, so it takes the flows in turn and chooses each turn by a rule that reproduces those fractions. That rule needs a clock the flows share, which is virtual time.

---

Flashcards for this section are as follows:

- generalized processor sharing: how does the ideal behind fair queuing serve the flows? ::@:: Every flow is served at the same time, each at a fixed fraction of the link.
- one packet at a time: what stops a router from serving the flows as the ideal does? ::@:: The link carries one packet at a time, so the router serves the flows in turn.
- what the rule needs: what does the turn rule need so that the turns divide the link as the ideal does? ::@:: A clock that all the flows share, which is the virtual clock.

### virtual clock

The link's virtual clock $V(t)$ is the time the link has spent transmitting. It advances at the link rate while the link is busy and stops when the link idles. Each flow has a reserved rate $r_q$: $R/n$ for $n$ equal flows, and $R w_q / \sum_q w_q$ with weights.

A packet of $p_{q,i}$ bits occupies its flow's share for $p_{q,i}/r_q$ seconds of that flow's own time, so each packet gets a finish time, or tag, on the link's clock: the moment it would leave if its flow were served at exactly $r_q$. The tag is $F_{q,i} = \max(V(t), F_{q,i-1}) + p_{q,i}/r_q$, where $F_{q,i-1}$ is the tag of the packet ahead of it in the same queue. The maximum covers two waits: until the link's clock reaches the flow's own time, and until the packet ahead has finished.

---

Flashcards for this section are as follows:

- virtual clock: what does the link's virtual clock $V(t)$ measure, and when does it advance? ::@:: The time the link has spent transmitting: it advances while the link is busy and stops when the link idles.
- reserved rate: how is a flow's reserved rate $r_q$ set on a link of rate $R$ with $n$ equal flows, and with weights $w_q$? ::@:: $r_q = R/n$ for equal flows, and $r_q = R w_q/\sum_q w_q$ with weights.
- finish time: for packet $i$ of flow $q$, with $p_{q,i}$ bits at reserved rate $r_q$, previous finish time $F_{q,i-1}$ and link clock $V(t)$, how is its finish time $F_{q,i}$ computed? ::@:: $F_{q,i} = \max(V(t), F_{q,i-1}) + p_{q,i}/r_q$, the later of the two times plus $p_{q,i}/r_q$.

### earliest finish time

The scheduler sends the packet with the earliest finish time, which is the smallest tag. Every tag is a time on the same clock, so the tags compare. A flow's tag advances by exactly the time that flow has been served, so the earliest finish time belongs to the flow that has received the least service relative to its share.

A 1 Gbps link with three equal flows reserves about 333 Mbps each. A 1500-byte packet occupies its flow's share for $12000/333{,}333{,}333 \approx 36\ \mu s$ and a 500-byte packet for $4000/333{,}333{,}333 \approx 12\ \mu s$, so packets of different sizes leave the router with the same share of the bits.

---

Flashcards for this section are as follows:

- scheduling order: the packets waiting at a fair queuing router carry finish times $F_{q,i}$; which does it send next? ::@:: The one whose finish time is earliest, which is the smallest tag, since every tag is a time on the same clock.
- why the earliest finish time: what does the smallest tag say about the flow that holds it? ::@:: That flow has received the least service relative to its reserved rate, so it goes next.
- tag advance: by how much does a flow's tag grow when one of its packets of $p_{q,i}$ bits is served at reserved rate $r_q$? ::@:: By $p_{q,i}/r_q$, the time that packet takes out of the flow's share.
- tags on a 1 Gbps link: on a $1\text{ Gbps}$ link with three equal flows, how long does a $1500$-byte packet occupy its flow's share, and a $500$-byte packet? ::@:: The share is $r_q = 10^9/3 \approx 333{,}333{,}333$ bits per second, so $1500 \times 8 = 12000$ bits take $12000/333{,}333{,}333 \approx 36\ \mu s$ and $500 \times 8 = 4000$ bits take $4000/333{,}333{,}333 \approx 12\ \mu s$.
- the long-run share: under smallest-tag scheduling, what does the flow whose reserved rate is $r_q$ receive over time? ::@:: Its reserved rate $r_q$.
- the 1 Gbps reservation: a $1\text{ Gbps}$ link carries three equal flows; what rate does each flow reserve? ::@:: $1\text{ Gbps} = 1000\text{ Mbps}$, so $1000/3 \approx 333\text{ Mbps}$ each.

### comparison with CPU scheduling

The scheme is processor sharing in an operating system, and its practical form is stride scheduling. There each process carries a virtual runtime, the scheduler runs whichever virtual runtime is smallest, and after the run that process's runtime advances by its stride, the inverse of its weight. The router is one processor shared by the flows, a packet takes the place of a time slice, and the tag is the virtual runtime.

---

Flashcards for this section are as follows:

- the operating-system analogue: which central processing unit (CPU) scheduling rule does fair queuing reproduce, and which practical form of it? ::@:: Processor sharing, whose practical form is stride scheduling.
- stride scheduling: in stride scheduling, which process runs next, and how does its virtual runtime change after the run? ::@:: The process with the smallest virtual runtime runs, and its runtime then grows by its stride, the inverse of its weight.

## approximation

Transmission is not preemptive, so the schedule is approximate: if a packet is already going out and another arrives with a smaller tag, the router cannot stop it, and the order is wrong until that packet finishes. The error lasts at most the transmission time of one packet: a 1500-byte packet on a 1 Gbps link is on the wire for $12\,\mu s$.

---

Flashcards for this section are as follows:

- non-preemptive: which property of a real link makes the fair schedule approximate? ::@:: Transmission cannot be interrupted, so a packet already on the wire must finish.
- size of the error: how long can the approximation be wrong at a time? ::@:: For at most the transmission time of one packet.
- the error bound: a $1500$-byte packet crosses a $1\text{ Gbps}$ link; how long is it on the wire? ::@:: $1500 \times 8 = 12000$ bits, and $10^9$ bits pass each second, so $12000/10^9 = 12\ \mu s$, which bounds how long the order can be wrong.

## weights

Weighted fair queuing gives each queue a weight $w_q$, so its reserved rate is $r_q = R w_q/\sum_q w_q$ and its tags follow $F_{q,i} = \max(V(t), F_{q,i-1}) + p_{q,i}/r_q$. The weight divides the tag's advance: per packet, a queue of weight $N$ advances its virtual time $1/N$ as far as a queue of weight $1$, so its tags stay smaller and it is served $N$ times as often. Weights fix the share: weights 3 and 1 on an 80 Mbps link give 60 Mbps and 20 Mbps.

---

Flashcards for this section are as follows:

- weight: in weighted fair queuing, what does a queue's weight $w_q$ set? ::@:: Its reserved rate $r_q = R w_q/\sum_q w_q$, and so its share of the link.
- weighted tag: on a link of rate $R$ with weights $w_q$, what is the tag of packet $i$ of flow $q$? ::@:: $F_{q,i} = \max(V(t), F_{q,i-1}) + p_{q,i}/r_q$ with $r_q = R w_q/\sum_q w_q$.
- why a heavier weight wins: what does a heavier weight do to the queue's virtual time, and what follows for scheduling? ::@:: It divides the tag's advance, so the queue's virtual time runs slower, its tags stay smaller, and it is chosen more often.
- weight against weight one: a queue carries weight $N$ and another weight $1$; how fast does the first one's virtual time run against the second, and what rate does it get? ::@:: $N$ times slower, since the advance is divided by the weight, so it is served $N$ times as often and receives $N$ times the rate.
- weighted plan: three houses share a $1\text{ Gbps}$ link with weights $4$, $2$, and $10$; which link rates do they get? ::@:: $4 + 2 + 10 = 16$ and $r_q = R w_q/\sum_q w_q$, so $1000 \times 4/16 = 250\text{ Mbps}$, $1000 \times 2/16 = 125\text{ Mbps}$, and $1000 \times 10/16 = 625\text{ Mbps}$.
