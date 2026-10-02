---
aliases:
  - HOL blocking
  - Head-of-line blocking
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/head-of-line_blocking
  - language/in/English
---

# head-of-line blocking

Head-of-line blocking (HOL blocking) occurs when the first task in a queue is slow or blocked, forcing every subsequent ready task to wait. The system sits idle while work remains queued, so it is not work-conserving.

---

Flashcards for this section are as follows:

- what does head-of-line blocking do to a queue? ::@:: A slow or blocked first task holds every subsequent ready task, so the system idles with work still queued
- work-conserving vs non-work-conserving ::@:: A work-conserving system always serves the next available task; HOL blocking makes a system non-work-conserving

## application-layer HOL blocking in HTTP

The queue forms as soon as several objects share a connection, which is what [pipelining](HTTP.md#pipelining) in HTTP 1.1 does. The client writes several requests at once and the server answers in the order it received them. A slow backend operation, such as a database query, then holds the whole response stream: later objects are already fetched and ready, yet the pipe stays empty until the slow one is written. The protocol enforces in-order delivery, so this is HOL blocking at the application layer (Layer 7).

HTTP 1.0 cannot form such a queue, because every object arrives on its own connection and nothing is ever waiting behind anything. That makes 1.1 the earliest version with application-layer HOL blocking: a large object holds up the small objects queued behind it.

---

Flashcards for this section are as follows:

- HTTP 1.1 pipelining / HOL blocking ::@:: Pipelined responses keep request order, so a slow-to-produce object holds every later object on the connection and the pipe idles
- application-layer HOL blocking ::@:: HOL blocking imposed by the application protocol itself, such as HTTP 1.1 answering pipelined requests strictly in order
- which HTTP version first puts a queue of objects on one connection? ::@:: HTTP 1.1, whose pipelining shares a connection; HTTP 1.0 gives every object a connection of its own, so nothing queues

## transport-layer HOL blocking in TCP

TCP delivers bytes in order, so a lost packet holds every byte queued behind it. [HTTP/2](HTTP.md#http/2) runs on TCP and inherits this: the receive buffer cannot hand stream 2 to the application while the packet carrying stream 1 is still missing, even though the two streams have nothing to do with each other. A server can process streams in parallel and still have the client wait. This is HOL blocking at the transport layer (Layer 4), and it survives every change HTTP/2 makes above the transport.

---

Flashcards for this section are as follows:

- TCP / HOL blocking ::@:: TCP delivers bytes in order, so one lost packet holds every byte behind it in the receive buffer until the retransmission arrives
- HTTP/2 / HOL limitation ::@:: Fixes the Layer 7 queue with streams, but TCP's in-order delivery still blocks every stream at Layer 4 when a packet is lost

## fixes across protocol generations

Each generation removes one of the two queues.

1. __Separate connections__: the client opens several TCP connections and spreads requests across them, so a slow response holds only its own connection. HTTP 1.0 does this by necessity and HTTP 1.1 by workaround. The client and the content provider both gain. The network loses, since each connection runs its own congestion control and they compete for the same bandwidth.
2. __HTTP/2 streams__: many requests in flight on one persistent connection, each carrying a stream ID, with responses written as soon as each is ready. The Layer 7 queue goes; the Layer 4 queue over TCP stays.
3. __HTTP/3 over QUIC__: QUIC runs on UDP and gives every stream its own reliability, so a lost packet is retransmitted for its own stream and no other. Both queues go.

The [version comparison](HTTP.md#version%20comparison) tabulates which queue each version leaves open.

---

Flashcards for this section are as follows:

- separate connections / fix ::@:: Several TCP connections in parallel, so a slow response blocks only its own connection; the network pays, since each connection runs its own congestion control
- HTTP/2 streams / fix ::@:: Multiplexed streams on one persistent connection with out-of-order responses remove the Layer 7 queue, and the Layer 4 queue over TCP remains
- QUIC / fix ::@:: Per-stream reliability over UDP removes the Layer 4 queue as well, so a loss on one stream delays no other
