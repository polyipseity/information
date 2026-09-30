---
aliases:
  - HTTP
  - Hypertext Transfer Protocol
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/HTTP
  - language/in/English
---

# HTTP

HTTP (Hypertext Transfer Protocol) is an application-layer request-response protocol. A client sends a request and a server returns a response, usually carrying an HTML document or other resource. HTTP is text-based and variable-length with no fixed byte offsets, making it human-readable and extensible but harder to parse in software.

---

Flashcards for this section are as follows:

- overview ::@:: A request-response protocol that retrieves hypermedia resources on the World Wide Web
- design trade-off ::@:: Text-based and variable-length: human-readable and extensible, but harder to parse than fixed-format protocols

## client-server model

HTTP follows a client-server model. The server is always on and well known; clients initiate contact by sending a request and receiving a reply. This is a synchronous request-reply protocol.

HTTP is stateless: the server does not retain information between requests. This improves scalability, simplifies failure handling, and allows higher request rates, but some applications need persistent state stored elsewhere.

### state management

When applications need state (shopping carts, user profiles, authentication), it is stored either on the client or the server:

- __Client-side cookies__: the browser stores identifiers or state and returns them to the server with each request
- __Server-side databases__: the server stores client-related information and looks it up when it receives a request containing a cookie

---

Flashcards for this section are as follows:

- overview ::@:: The server does not retain information between requests; each request-response pair is independent
- state management ::@:: Persistent state is stored on the client via cookies or on the server via databases
- client-server ::@:: A synchronous request-reply model: the server is always on and well known, and clients initiate contact

## request and response messages

A request message has a request line (method, resource path, protocol version), optional header lines, and an optional body. A blank line (CRLF) separates headers from body.

A response message has a status line (protocol version, status code, status phrase), optional response headers, and an optional body.

Common methods: GET retrieves a resource, POST sends data to the server. Common headers: `Host`, `User-agent`, `Connection`, `Accept-language`.

---

Flashcards for this section are as follows:

- HTTP request message / structure ::@:: A request line (method, resource, protocol version), header lines, an optional body, and a blank CRLF separator
- HTTP response message / structure ::@:: A status line (protocol version, status code, status phrase), response headers, and an optional body

## persistent connections

Page load time (PLT) matters: 100 ms is the typical limit of human perception, and an Amazon study found every additional 100 ms of PLT costs 1% in profit.

HTTP 1.0 opens a new TCP connection per object: one RTT to initiate the connection, one RTT for the request and first response bytes, then file transmission time. For $n$ small objects, this costs $3n$ RTTs.

Persistent connections (keep-alive) maintain a single TCP connection across multiple requests. Either side can tear down the connection. With persistent connections, $n$ small objects cost $n + 2$ RTTs, avoiding repeated setup/teardown overhead and reusing previously discovered bandwidth.

---

Flashcards for this section are as follows:

- HTTP 1.0 response time: Given one object of known size, how many RTTs does HTTP 1.0 need? <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> ::@:: $2 \times \text{RTT} + \text{file transmission time}$, because one RTT opens the TCP connection and another carries the request and the first response bytes
- page load time / 100 ms threshold ::@:: 100 ms is the typical limit of human perception; an Amazon study found every additional 100 ms of page load time costs 1% in profit
- RTT (round-trip time) ::@:: The time for a small packet to travel from client to server and back
- persistent connection / RTT savings: Given $n$ small objects, how many RTTs does each version cost? ::@:: $n + 2$ RTTs with persistent connections, versus $3n$ RTTs without

## pipelining

Pipelining sends multiple HTTP requests on a single connection without waiting for each response. The server responds in order as it processes each request, filling the pipe more efficiently.

When all requested objects are immediately available, pipelining works well. When some take longer (e.g., a database query), later ready objects must wait behind the slow one — head-of-line blocking.

---

Flashcards for this section are as follows:

- HTTP pipelining ::@:: Sending multiple requests on a single connection without waiting for each response, with the server responding in order
- pipelining / weakness ::@:: A slow-to-produce object blocks all subsequent ready objects in the queue

<!-- check: ignore-next-line[header_style]: HTTP/2 is a proper noun -->
## HTTP/2

HTTP/2 keeps persistent connections and pipelining but adds streams: each request-response pair gets a stream ID and can be processed independently. The server may send responses out of order, so fast objects are delivered immediately while slow ones continue. This avoids application-layer (Layer 7) head-of-line blocking.

HTTP/2 also compresses headers. However, it still runs over TCP, so a lost packet for one stream blocks all streams at the transport layer (Layer 4) — the receive buffer cannot pass data for stream 2 until the missing packet for stream 1 is retransmitted.

---

Flashcards for this section are as follows:

- HTTP/2 / streams ::@:: Each request-response pair gets a stream ID and can be served out of order, avoiding application-layer HOL blocking
- HTTP/2 / remaining limitation ::@:: Runs over TCP, so a lost packet blocks all streams at Layer 4 because TCP delivers bytes in order
- HTTP/2 vs HTTP 1.0 ::@:: HTTP/2 multiplexes streams over one persistent connection; HTTP 1.0 opens a new TCP connection per object

<!-- check: ignore-next-line[header_style]: HTTP/3 is a proper noun -->
## HTTP/3

HTTP/3 replaces TCP with QUIC (Quick UDP Internet Connections), standardized as RFC 9000 in 2021. QUIC is a multiplexed transport protocol over UDP: each stream has independent reliability, so a lost packet for one stream does not block others.

This eliminates head-of-line blocking at both Layer 7 and Layer 4. The application can read a stream's data as soon as it is complete, even if other streams have lost packets. HTTP/3 retains persistent connections, pipelining, and re-orderable streams from HTTP/2.

---

Flashcards for this section are as follows:

- HTTP/3 / transport ::@:: QUIC over UDP gives each stream independent reliability, so a lost packet for one stream does not block others
- HTTP/3 vs HTTP/2 ::@:: HTTP/2 fixes HOL at Layer 7 with streams; HTTP/3 fixes both Layer 7 and Layer 4 by running over QUIC
- QUIC ::@:: A multiplexed transport protocol over UDP (RFC 9000, 2021) with per-stream reliability
