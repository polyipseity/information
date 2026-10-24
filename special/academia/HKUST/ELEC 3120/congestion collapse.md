---
aliases:
  - ELEC 3120 congestion collapse
  - ELEC3120 congestion collapse
  - HKUST ELEC 3120 congestion collapse
  - HKUST ELEC3120 congestion collapse
  - congestion collapse
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/congestion_collapse
  - language/in/English
---

# congestion collapse

Congestion collapse is a fall in useful throughput far below what the links could carry, while the links themselves stay busy. Senders keep a full window in flight, so losses grow, and each lost packet returns as a copy that occupies the link that dropped it. Ordinary congestion costs delay and leaves the data arriving late; congestion collapse costs the data itself, so the useful throughput of the network falls.

---

Flashcards for this section are as follows:

- congestion collapse: what happens to a network in congestion collapse? ::@:: Retransmissions take up the capacity that fresh data needed, so throughput falls far below what the links can carry.
- the cost of ordinary congestion: how does ordinary congestion differ from congestion collapse in what each one costs? ::@:: Ordinary congestion costs delay, so the data still arrives, late; congestion collapse costs the data itself, so useful throughput falls.

## 1986 collapse

In October 1986 the National Science Foundation (NSF) network collapsed this way: throughput fell from 32 kbit/s to 40 bit/s while the links ran at full load. Senders were limited only by the receiver's window, so a drop made each of them resend a whole window, and the copies caused more drops.

With a maximum segment size of 1460 bytes, one segment carries 11,680 bits, and a link running at 32 kbit/s needs about 0.36 s to send it. At the collapsed rate of 40 bit/s the same segment takes about 292 s to arrive, so the network spent nearly five minutes on every segment of new data it delivered. The two rates differ by a factor of 800. A sender that resent a window of ten segments after each drop put 116,800 bits of copies into the network, which at 32 kbit/s is 3.65 s of link time carrying data it had already sent. At the collapsed rate of 40 bit/s the same copies took 2,920 s, about 49 minutes.

---

Flashcards for this section are as follows:

- the 1986 collapse: which two throughput figures mark the collapse of the National Science Foundation (NSF) network in October 1986? ::@:: From 32 kbit/s down to 40 bit/s.
- before congestion control: what was the only limit on a sender? ::@:: The receiver's advertised window, which is flow control.
- the ratio between the rates: the throughput of the National Science Foundation (NSF) network fell from $32\text{ kbit/s}$ to $40\text{ bit/s}$; by what factor did it fall? ::@:: $32{,}000 / 40 = 800$, since $32\text{ kbit/s}$ is $32{,}000\text{ bit/s}$.
- the segment time: a link runs at $32\text{ kbit/s}$ and sends a segment of $1460$ bytes; how long does that segment take to send? ::@:: About $0.36\text{ s}$: $1460 \times 8 = 11{,}680$ bits, and $11{,}680 / 32{,}000 = 0.365\text{ s}$.
- the cost of a copy at the collapsed rate: a sender resends a window of ten segments, $116{,}800$ bits, on a link running at $40\text{ bit/s}$; how long does that copy occupy the link? ::@:: About $2{,}920$ seconds, since $116{,}800 / 40 = 2{,}920$.
- the segment time at the collapsed rate: one segment of $11{,}680$ bits is sent over a link running at the collapsed rate of $40\text{ bit/s}$; how long does that segment take? ::@:: About $292\text{ s}$, nearly five minutes, since $11{,}680 / 40 = 292$.

## repair in the end hosts

Van Jacobson fixed it inside the end hosts. The sender's window became an estimate of the path's capacity, shrinking on loss and growing again without it. That took a few lines of code in each Transmission Control Protocol (TCP) implementation, with no change to routers or applications.

A sender holding a window of 20 segments that lost one packet no longer resends the whole window. It resends the missing segment and cuts the window to 10, so the copies on the link fall from a whole window to half a window, and the capacity they take is handed back to new data instead of to duplicates. On a 32 kbit/s link that is 233,600 bits, 7.3 s of link time, before the repair, and 116,800 bits, 3.65 s, after it. Jacobson set out the collapse and the fix in his 1988 paper _Congestion Avoidance and Control_, where the two throughput figures and the change to the end hosts appear together.

---

Flashcards for this section are as follows:

- who repaired it: which person is credited with the congestion control that ended the collapse? ::@:: Van Jacobson.
- where the repair went: which devices needed upgrading for the repair to work? ::@:: None: the change went into the sending hosts, so routers and applications stayed as they were.
- what replaced the fixed window: what did the sender's window become? ::@:: An estimate of the path's capacity, shrinking after a loss and growing while none arrives.
- the halved window: a sender with a window of $20$ segments loses a packet under the repaired rule; what window does it keep? ::@:: $10$ segments, since $20 / 2 = 10$.
- the paper: which paper describes the 1986 collapse and the congestion control that followed? ::@:: Van Jacobson's 1988 paper _Congestion Avoidance and Control_.
- the copies after the repair: a sender with a window of $20$ segments loses a packet on a $32\text{ kbit/s}$ link; how many bits of copies does the repaired rule put on that link? ::@:: $20 \times 11{,}680 = 233{,}600$ bits in a full window, so half is $116{,}800$ bits, which is $116{,}800 / 32{,}000 = 3.65\text{ s}$ instead of $7.3\text{ s}$.
- the copies before the repair: a sender with a window of $20$ segments of $11{,}680$ bits each resends the whole window on a $32\text{ kbit/s}$ link; how many bits of copies does that put on the link, and for how long? ::@:: $20 \times 11{,}680 = 233{,}600$ bits, which occupies the link for $233{,}600 / 32{,}000 = 7.3\text{ s}$.
