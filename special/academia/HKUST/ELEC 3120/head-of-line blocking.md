---
aliases:
  - HOL blocking
  - Head-of-line blocking
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/head-of-line_blocking
  - language/in/English
---

# head-of-line blocking

Head-of-line blocking (HOL blocking) occurs when the first task in a queue is slow or blocked, forcing every subsequent ready task to wait. The system sits idle while work remains queued — it is not work-conserving.

---

Flashcards for this section are as follows:

- overview ::@:: A slow or blocked first task in a queue forces all subsequent ready tasks to wait, leaving the system idle
- work-conserving vs non-work-conserving ::@:: A work-conserving system always serves the next available task; HOL blocking makes a system non-work-conserving

## application-layer HOL blocking in HTTP

In HTTP pipelining, the client sends multiple requests on a single connection and the server responds in order. A slow backend operation (e.g., a database query) delays all subsequent responses even though those objects are ready. The network pipe sits empty while the slow request blocks the queue.

This is application-layer (Layer 7) HOL blocking: the protocol enforces in-order delivery, so a slow-to-produce object blocks the entire response stream.

---

Flashcards for this section are as follows:

- HTTP pipelining / HOL blocking ::@:: A slow-to-produce object blocks all subsequent responses in the pipeline, leaving the network pipe idle
- application-layer HOL blocking ::@:: HOL blocking at the application protocol layer (Layer 7), such as HTTP pipelining requiring in-order responses

## transport-layer HOL blocking in TCP

HTTP/2 introduces streams to fix application-layer HOL blocking: responses can arrive out of order, so fast objects are delivered immediately. However, HTTP/2 still runs over TCP, which delivers bytes in order. When a packet for stream 1 is lost, the TCP receive buffer holds all subsequent data (including stream 2) until the missing packet is retransmitted. The application cannot read stream 2's data even though it has arrived.

This is transport-layer (Layer 4) HOL blocking: TCP's in-order delivery means one lost packet blocks all higher-layer data on the connection.

---

Flashcards for this section are as follows:

- TCP / HOL blocking ::@:: TCP delivers bytes in order, so a lost packet blocks all subsequent data — the receive buffer cannot deliver stream 2 until the missing packet for stream 1 is retransmitted
- HTTP/2 / HOL limitation ::@:: HTTP/2 fixes HOL at Layer 7 with streams, but TCP in-order delivery still causes HOL at Layer 4 when packets are lost

## fixes across protocol generations

Three generations of fixes:

1. __Concurrent/parallel connections__: multiple TCP connections in parallel, each with its own requests. Partially addresses HOL but multiplies overhead. The client and content provider benefit, but the network is disadvantaged — multiple connections compete for bandwidth with independent congestion control.
2. __HTTP/2 streams__: multiplex streams over one persistent connection with out-of-order delivery. Fixes Layer 7 HOL but retains Layer 4 HOL over TCP.
3. __HTTP/3 over QUIC__: UDP with per-stream reliability. A lost packet for one stream does not block others, eliminating HOL at both layers.

---

Flashcards for this section are as follows:

- concurrent connections / tradeoff ::@:: Faster for client and content provider, but disadvantages the network because multiple TCP connections compete for bandwidth with independent congestion control
- HOL blocking / fix progression ::@:: Generation 1: parallel TCP connections (partial fix); Generation 2: HTTP/2 streams (fixes Layer 7); Generation 3: HTTP/3 over QUIC (fixes both Layer 7 and Layer 4)
