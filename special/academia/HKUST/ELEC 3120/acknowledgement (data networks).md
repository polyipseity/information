---
aliases:
  - ACK
  - ELEC 3120 acknowledgement (data networks)
  - ELEC3120 acknowledgement (data networks)
  - HKUST ELEC 3120 acknowledgement (data networks)
  - HKUST ELEC3120 acknowledgement (data networks)
  - acknowledgement
  - acknowledgement (data networks)
  - acknowledgment
  - cumulative acknowledgement
  - selective acknowledgement
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/acknowledgement_(data_networks)
  - language/in/English
---

# acknowledgement (data networks)

An acknowledgement tells the sender that its data arrived, so the sender keeps its copy until one returns. A lost report looks like lost data, so the sender resends on a timer, and what that resend costs depends on what a report covers: a single packet, everything up to a point, or the ranges held past a gap.

---

Flashcards for this section are as follows:

- acknowledgement: what does an acknowledgement tell the sender? ::@:: That the data it names arrived at the receiver.
- why keep a copy: why does the sender keep its copy until an acknowledgement returns? ::@:: Because the data or the report can be lost, and only a resend repairs it.
- a lost report: how does a sender read an acknowledgement that never arrives? ::@:: As lost data: it cannot tell a lost report from lost data, so it resends after a timer.

## basic acknowledgement

A basic acknowledgement names the packet just received and nothing else: "packet 3". With packets 1, 2 and 3 in flight, a sender that hears about 1 and 3 but never 2 takes 2 as missing and resends it. If packet 2 arrived and only its report was lost, the receiver holds two copies and drops one.

---

Flashcards for this section are as follows:

- basic acknowledgement: what does a basic acknowledgement name? ::@:: The packet just received, and nothing else.
- reading the report: a sender hears about packets $1$ and $3$ but not $2$; what does it conclude, and what does it do? ::@:: A report names one packet, so $1$ and $3$ say nothing of $2$; when its timer expires, $2$ goes again.

## cumulative acknowledgement

A cumulative acknowledgement names the next byte it expects, so every byte before it has arrived: $4000$ means bytes $0$ to $3999$ are present. A lost report costs nothing, because the next one carries a higher number and covers the same bytes and more. A repeated number says the receiver still waits there, so a byte before it is missing. The Transmission Control Protocol (TCP) acknowledges its sequence numbers this way.

---

Flashcards for this section are as follows:

- cumulative acknowledgement: what does the number in a cumulative acknowledgement name? ::@:: The next byte the receiver expects; every byte before it has arrived.
- reading the number: what does a cumulative acknowledgement of $4000$ report? ::@:: Bytes $0$ to $3999$ have arrived, that is $4000 - 1 = 3999$, so byte $4000$ is next.
- a lost report: why does a lost cumulative acknowledgement cost nothing? ::@:: The next one carries a higher number and covers the same bytes and more.
- reading a repeat: what does the same acknowledgement number arriving twice report? ::@:: That the receiver is still waiting at that byte, so a byte before it is missing.

## cost of a gap

The receiver cannot report the bytes it holds past a gap, so one loss costs everything after it. With bytes $0$ to $3999$ arrived, $4000$ to $4999$ missing and $5000$ to $8999$ arrived, the report stays $4000$, so the sender resends the gap and everything past it. A page of $100$ KB is $102{,}400$ bytes, about $70$ segments of $1460$ bytes, and one lost segment in the middle can repeat up to those $70$ segments to deliver one.

---

Flashcards for this section are as follows:

- what the report says: bytes $0$ to $3999$ arrived, $4000$ to $4999$ missing and $5000$ to $8999$ arrived; what does the receiver report? ::@:: $4000$: the count runs while bytes are contiguous, stops at the first missing byte, and cannot name the $5000$ to $8999$ range it holds past it.
- what the sender resends: from which byte does a sender resume when the receiver keeps reporting $4000$? ::@:: From byte $4000$: it cannot tell which bytes past the gap arrived, so every segment it had sent after $4000$ goes again.
- the cost of one loss: on a page of $100$ KB in segments of $1460$ bytes, what can one lost segment in the middle cost? ::@:: $100$ KB is $102{,}400$ bytes, that is $102{,}400 / 1460 \approx 70$ segments, so up to $70$ segments are repeated for one lost segment.

## selective acknowledgement

A selective acknowledgement keeps the cumulative number and adds the ranges the receiver holds past the gap, so the sender resends the gap alone. The ranges travel in the options field of the header, and several fit in one segment. On the same page, one lost segment costs $1 \times 1460 = 1460$ bytes, and two losses with an arrived block between them cost $2 \times 1460 = 2920$ bytes, the block being named and kept. Request for Comments 2018 (RFC 2018) defines the option.

---

Flashcards for this section are as follows:

- selective acknowledgement: what does a selective acknowledgement add to the cumulative number? ::@:: The ranges of bytes the receiver holds past the gap.
- what the sender resends: with a selective acknowledgement, what does the sender resend after a loss? ::@:: The gap alone: the blocks say which bytes past it arrived, so it is not repeated with them.
- one loss: a page of $100$ KB in segments of $1460$ bytes loses one segment; how much does a selective acknowledgement make the sender resend? ::@:: $1 \times 1460 = 1460$ bytes: the blocks name the rest, so only the lost segment goes again.
- two losses: a page of $100$ KB in segments of $1460$ bytes loses two segments with an arrived block between them; how much does the sender resend? ::@:: $2 \times 1460 = 2920$ bytes, one segment per loss, since the block between them is named and kept.
- the standard: which document defines selective acknowledgement? ::@:: Request for Comments 2018 (RFC 2018).

## page fetch

A browser sends `GET /index.html HTTP/1.1` with the required `Host:` header, and the receiver counts the request bytes and the response bytes with one cumulative number. A response carrying `Content-Length: 1024` is complete when the number passes the $1024$ body bytes plus the status line and the headers. A response with no `Content-Length` sends the body in chunks, each preceded by its size in hexadecimal and the last of size zero, and those size lines count in the same number.

---

Flashcards for this section are as follows:

- the request bytes: which number confirms that a Hypertext Transfer Protocol version 1.1 (HTTP/1.1) request arrived? ::@:: The cumulative byte count of the request.
- body against message: a response carries `Content-Length: 1024`, so its body is $1024$ bytes; when is the response complete, and what does the cumulative number count? ::@:: The count starts at the status line and runs through the headers into the body, so the $1024$ body bytes end at $1024$ plus the status line and the headers.

## later refinements

A duplicate selective acknowledgement reports data the receiver has seen twice, so the retransmission was wasted. The recent-acknowledgement scheme replaces counting with time and treats a segment as lost once a later segment has been acknowledged for long enough.

---

Flashcards for this section are as follows:

- a duplicate selective acknowledgement: what does a duplicate selective acknowledgement report? ::@:: Data the receiver has seen twice, so the retransmission was wasted.
- detecting loss by time: how does the recent-acknowledgement scheme decide that a segment is lost? ::@:: By time: a segment counts as lost once a later segment has been acknowledged for long enough.
