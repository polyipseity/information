---
aliases:
  - HOL blocking
  - Head-of-line blocking
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/head-of-line_blocking
  - language/in/English
---

# head-of-line blocking

Head-of-line blocking (HOL blocking) happens when the first task in a queue is slow or blocked and everything behind it has to wait. Work is sitting there ready, and the system is idle anyway, so it is not work-conserving.

---

Flashcards for this section are as follows:

- what does head-of-line blocking do to a queue? ::@:: A slow or blocked first task holds every subsequent ready task, so the system idles with work still queued
- work-conserving vs non-work-conserving ::@:: A work-conserving system always serves the next available task; HOL blocking makes a system non-work-conserving

## application-layer HOL blocking in HTTP

A queue only forms once several objects share a connection, which is what [pipelining](HTTP.md#pipelining) does in HTTP 1.1. The client writes several requests at once and the server answers in the order they came in. A slow backend call, a database query say, then holds up the whole response stream: the objects behind it are already fetched and ready, but nothing goes out until the slow one is written. The order is the protocol's rule, not the server's choice, so this is HOL blocking at the application layer (Layer 7).

HTTP 1.0 never gets that far, because every object has a connection of its own and nothing is ever waiting behind anything. That makes 1.1 the first version where a large object can hold up the small ones queued behind it.

---

Flashcards for this section are as follows:

- what does pipelining do to a slow object? ::@:: Nothing helps it: responses keep request order, so a slow object holds every later one on the connection and the pipe idles
- what is application-layer HOL blocking? ::@:: Blocking the protocol itself imposes, such as HTTP 1.1 answering pipelined requests strictly in order
- which HTTP version first puts a queue of objects on one connection? ::@:: HTTP 1.1, whose pipelining shares a connection. HTTP 1.0 gives every object a connection of its own, so nothing queues

## transport-layer HOL blocking in TCP

TCP hands bytes over in order, so a lost packet holds up every byte queued behind it. [HTTP/2](HTTP.md#http/2) runs on TCP and inherits the whole problem: the receive buffer cannot hand stream 2 to the application while the packet carrying stream 1 is still missing, and the two streams have nothing to do with each other. A server can process them in parallel and the client still waits. This is HOL blocking at the transport layer (Layer 4), and nothing HTTP/2 does above the transport touches it.

---

Flashcards for this section are as follows:

- what does a lost packet cost on a TCP connection? ::@:: Every byte behind it, since TCP hands bytes over in order and the receive buffer waits for the retransmission
- what is still wrong with HTTP/2? ::@:: It clears the Layer 7 queue with streams, but TCP's in-order delivery still blocks every stream at Layer 4 when a packet is lost

## fixes across protocol generations

Three rounds of fixes, and each one takes out one of the two queues.

1. __Separate connections__: the client opens several TCP connections and spreads its requests across them, so a slow response only holds up its own connection. HTTP 1.0 does this because it has to, HTTP 1.1 does it as a workaround. The client and the content provider both come out ahead. The network does not, since each connection runs its own congestion control and they all want the same bandwidth.
2. __HTTP/2 streams__: many requests in flight on one persistent connection, each carrying a stream ID, with a response written as soon as that object is ready. The Layer 7 queue goes. The Layer 4 queue over TCP stays.
3. __HTTP/3 over QUIC__: QUIC runs on UDP and gives every stream its own reliability, so a lost packet is retransmitted for its own stream and for no other. Both queues go.

The [version comparison](HTTP.md#version%20comparison) says which queue each version leaves open.

---

Flashcards for this section are as follows:

- how do separate connections help, and what do they cost? ::@:: A slow response then blocks only its own connection. The network pays for it, since every connection runs its own congestion control
- what do HTTP/2 streams fix? ::@:: Multiplexing on one persistent connection with out-of-order responses takes out the Layer 7 queue, and the Layer 4 queue over TCP remains
- what does QUIC add? ::@:: Per-stream reliability over UDP takes out the Layer 4 queue as well, so a loss on one stream delays no other
