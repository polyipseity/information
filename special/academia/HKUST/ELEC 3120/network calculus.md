---
aliases:
  - ELEC 3120 network calculus
  - ELEC3120 network calculus
  - HKUST ELEC 3120 network calculus
  - HKUST ELEC3120 network calculus
  - arrival curve
  - network calculus
  - service curve
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/network_calculus
  - language/in/English
---

# network calculus

Network calculus bounds a queue's worst case without simulating any traffic. One curve caps how much data may arrive and another says how fast the router can serve it.

---

Flashcards for this section are as follows:

- network calculus: what does network calculus compute? ::@:: Worst-case bounds on queue length, waiting time, and drain time, from curves that bound arrival and service.
- the two curves: which two functions does it combine? ::@:: An arrival curve that bounds the incoming traffic and a service curve that describes the router's capability.
- why not simulate: what does the method avoid needing? ::@:: A simulation or a trace of real traffic; the bounds follow from the curves alone.

## arrival curve

An arrival curve $A(t)$, also called a traffic envelope, is an upper bound on how much data may have arrived by time $t$. A token bucket of rate $r$ and burst $b$ produces the straight line $A(t) = rt + b$, taking the worst case that the bucket is full when the measurement starts. A sender of rate 10 Mbps with a burst of 200 kB has the arrival curve $A(t) = 10^7 t + 1.6 \times 10^6$ bits.

---

Flashcards for this section are as follows:

- arrival curve: what does the arrival curve $A(t)$ bound? ::@:: The total data that may have arrived from a sender by time $t$.
- token bucket curve: which arrival curve does a token bucket of rate $r$ and burst $b$ produce? ::@:: $A(t) = rt + b$, a line of slope $r$ raised by $b$.
- the worst case: which state of the bucket does the line $A(t) = rt + b$ assume? ::@:: That the bucket is full when the burst begins.
- a rate and a burst: which arrival curve does a sender of rate $10\text{ Mbps}$ and burst $200\text{ kB}$ produce? ::@:: $A(t) = 10^7 t + 1.6 \times 10^6$ bits, since $200\text{ kB}$ is $1{,}600{,}000$ bits.

## service curve

A service curve $S(t)$ is the exact amount of data the router can serve in time $t$. A router with an output link of rate $r_2$ and nothing else to do serves $S(t) = r_2 t$, since the link is the only limit. At 10 Mbps the link delivers $10^7$ bits in one second, which is 1.25 MB.

---

Flashcards for this section are as follows:

- service curve: what does the service curve $S(t)$ state? ::@:: The exact amount of data the router can serve within time $t$.
- a link of rate $r_2$: which service curve does an output link of rate $r_2$ give? ::@:: $S(t) = r_2 t$.
- one second at 10 megabits per second: how much data does a link of rate $10$ megabits per second deliver in one second? ::@:: $10^7 \times 1 = 10^7$ bits in one second, which is $10^7 / 8 = 1{,}250{,}000$ bytes $= 1.25$ megabytes.

## reading the gap

The vertical gap between $A(t)$ and $S(t)$ at a time $t_n$ is the data still queued at that moment, $z_a - z_b$. The horizontal gap is how long a packet waits before it leaves. Where the curves meet, the queue has finally drained. With $A(t) = 20t + 12$ and $S(t) = 30t$ the backlog is $12 - 10t$ bits, shrinking by 10 bits each second.

---

Flashcards for this section are as follows:

- vertical gap: what does the vertical distance between the arrival curve and the service curve give? ::@:: The amount of data still sitting in the queue at that time.
- horizontal gap: what does the horizontal distance between the two curves give? ::@:: How long a packet waits in the queue before it leaves.
- the backlog: with arrival curve $A(t) = 20t + 12$ and service curve $S(t) = 30t$, how much is queued at $t = 1$ second? ::@:: $A(1) = 20 \times 1 + 12 = 32$ and $S(1) = 30 \times 1 = 30$, so $32 - 30 = 2$ bits.
- two senders: how are two senders' envelopes combined before drawing them against the router? ::@:: By adding them, which adds their rates and their bursts.

## worked bound

Two shaped senders each with rate $10$ bits per second and bursts $2$ and $10$ bits give a combined curve $A(t) = 20t + 12$. A router serving $30$ bits per second has $S(t) = 30t$. The queue runs dry when the two are equal, $30t = 20t + 12$, so at $t = 1.2$ seconds. A sender with the curve $A(t) = 10^7 t + 1.6 \times 10^6$ bits on a router serving 20 Mbps drains at $t = 0.16$ seconds, since $2 \times 10^7 t = 10^7 t + 1.6 \times 10^6$, and the worst wait is the burst over the service rate, $0.08$ seconds.

---

Flashcards for this section are as follows:

- combined curve: for two token buckets of rate $10$ bits per second with bursts $2$ and $10$ bits, what is the combined arrival curve? ::@:: Rates $10 + 10 = 20$ and bursts $2 + 10 = 12$, so $A(t) = 20t + 12$.
- drain time: with arrival curve $A(t) = 20t + 12$ and a router serving $30$ bits per second, when does the queue empty? ::@:: $30t = 20t + 12$ gives $10t = 12$, so $t = 1.2$ seconds.
- the method: given an arrival curve $A(t)$ and a service curve $S(t)$, which equation solves for the drain time? ::@:: Setting them equal, $S(t) = A(t)$.
- a second bound: an arrival curve $A(t) = 10^7 t + 1.6 \times 10^6$ and a service curve $S(t) = 2 \times 10^7 t$ empty the queue when? ::@:: $2 \times 10^7 t = 10^7 t + 1.6 \times 10^6$ gives $10^7 t = 1.6 \times 10^6$, so $t = 0.16$ seconds.
- the worst wait: with arrival curve $A(t) = 10^7 t + 1.6 \times 10^6$ and service curve $S(t) = 2 \times 10^7 t$, how long can a packet wait at most? ::@:: $1.6 \times 10^6 / (2 \times 10^7) = 0.08$ seconds, the burst over the service rate.
- worst wait formula: for a burst of $b$ bits and a service rate $r_2$ bits per second, how is the worst packet wait computed? ::@:: As the burst divided by the service rate, $b / r_2$ seconds.
