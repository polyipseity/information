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

Four generations of HTTP are in wide use, and they differ in three respects: how a connection is set up and reused, whether responses can arrive out of order on one connection, and what carries the bytes.

---

Flashcards for this section are as follows:

- what kind of protocol is HTTP? ::@:: An application-layer request-response protocol that retrieves hypermedia resources on the World Wide Web
- design trade-off ::@:: Text-based and variable-length: human-readable and extensible, but harder to parse than fixed-format protocols
- HTTP generations ::@:: HTTP 1.0, 1.1, 2.0, and 3.0 differ in connection reuse, ordering of responses on one connection, and transport: TCP for 1.0 through 2.0, QUIC over UDP for 3.0

## client-server model

HTTP follows a client-server model. The server is always on and well known; clients initiate contact by sending a request and receiving a reply.

The server keeps nothing about a client between requests, and it never has: HTTP is stateless from 1.0 onward. An application that needs state stores it elsewhere. Nothing has to be recovered between requests, so one server absorbs a high request rate and a restart loses nothing.

---

Flashcards for this section are as follows:

- who starts a contact in HTTP? ::@:: The client, since the server is always on and well known; the exchange is synchronous request-reply
- server state ::@:: The server retains nothing about a client between requests; this has held since HTTP 1.0
- statelessness / benefit ::@:: The server can scale and absorb a high request rate because nothing about a client survives its request

### state management

When applications need state (shopping carts, user profiles, authentication), it is stored either on the client or the server:

- __Client-side cookies__: the browser stores identifiers or state and returns them to the server with each request
- __Server-side databases__: the server stores client-related information and looks it up when it receives a request containing a cookie

---

Flashcards for this section are as follows:

- state management ::@:: Persistent state is stored on the client via cookies or on the server via databases
- client-side cookies ::@:: The browser holds the identifier or state and returns it with each request
- server-side databases ::@:: The server holds client-related information and looks it up on a request that carries a cookie

## request and response messages

A request message has a request line (method, resource path, protocol version), optional header lines, and an optional body. A blank line (CRLF) separates headers from body.

A response message has a status line (protocol version, status code, status phrase), optional response headers, and an optional body.

Common methods: GET retrieves a resource, POST sends data to the server. Common headers: `Host`, `User-agent`, `Connection`, `Accept-language`. The protocol version sits in the request line of every request and the status line of every response. HTTP 1.1 made `Host` mandatory, because one address can answer for many domain names at once.

---

Flashcards for this section are as follows:

- HTTP request message / structure ::@:: A request line (method, resource, protocol version), header lines, an optional body, and a blank CRLF separator
- HTTP response message / structure ::@:: A status line (protocol version, status code, status phrase), response headers, and an optional body
- `Host` header ::@:: Mandatory in every HTTP 1.1 request, since one address serves many domain names
- protocol version on the wire ::@:: Stated in the request line of every request and in the status line of every response

## persistent connections

Page load time (PLT) matters: 100 ms is the typical limit of human perception, and an Amazon study found every additional 100 ms of PLT costs 1% in profit.

HTTP 1.0 opens a new TCP connection per object: one RTT to initiate the connection, one RTT for the request and first response bytes, then file transmission time. For $n$ small objects, this costs $3n$ RTTs.

---

Flashcards for this section are as follows:

- page load time / 100 ms threshold ::@:: 100 ms is the typical limit of human perception; an Amazon study found every additional 100 ms of page load time costs 1% in profit
- RTT (round-trip time) ::@:: The time for a small packet to travel from client to server and back
- HTTP 1.0 response time: Given one object of known size, how many RTTs does HTTP 1.0 need? <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> ::@:: $2 \times \text{RTT} + \text{file transmission time}$, because one RTT opens the TCP connection and another carries the request and the first response bytes

### keep-alive in HTTP 1.0

HTTP 1.0 does have a way to reuse a connection. A client sends `Connection: Keep-Alive` (RFC 2068) and the server may confirm it, after which the same connection carries the next object. Old clients and old servers disagreed about when to stop, so in practice HTTP 1.0 behaves as non-persistent and every object pays for its own connection.

---

Flashcards for this section are as follows:

- HTTP 1.0 / `Connection: Keep-Alive` ::@:: An opt-in extension in which client and server agree to reuse the connection; poor interoperability left it unused in practice
- HTTP 1.0 / connection cost: Given a page of $n$ small objects over non-persistent HTTP 1.0, what does the page cost? ::@:: $3n$ RTTs, one new TCP connection for every object

### persistence as the default in HTTP 1.1

HTTP 1.1 made the connection persistent by default, so no keep-alive negotiation is needed first. A client sends several requests over one connection, and either side closes it when finished. The TCP handshake is then paid once per connection instead of once per object, so $n$ small objects cost $n + 2$ RTTs. The bandwidth-delay product measured on the first object carries over to the rest.

---

Flashcards for this section are as follows:

- HTTP 1.1 / persistent connections: Given a page of $n$ small objects on one persistent connection, what does the page cost? ::@:: $n + 2$ RTTs, against $3n$ without persistence, because the handshake is paid once per connection
- HTTP 1.1 / handshake cost ::@:: The TCP handshake is paid once per connection rather than once per object
- who closes a persistent connection ::@:: Either side may close it when finished, since HTTP 1.1 needs no keep-alive agreement first

## pipelining

Pipelining arrives with HTTP 1.1. The client writes several requests to one connection without waiting for the answers, and the server responds in the order it received the requests. The requests no longer wait a round trip each, so a page of $n$ small objects costs one round trip for the whole batch.

When all requested objects are immediately available, pipelining works well. When some take longer (e.g., a database query), later ready objects must wait behind the slow one, which is [head-of-line blocking](head-of-line%20blocking.md). The in-order rule is part of the protocol, so a server that can process requests in parallel still cannot send a later response first.

---

Flashcards for this section are as follows:

- HTTP 1.1 / pipelining ::@:: Introduced in 1.1: several requests are written to one connection without waiting, and the server answers them in request order
- pipelining / round trips: Given $n$ pipelined requests written at once on one connection, how many round trips do they cost? ::@:: One round trip for the batch, not one round trip per request
- pipelining / weakness ::@:: Responses keep request order, so a slow-to-produce object blocks later ready objects on the same connection

<!-- check: ignore-next-line[header_style]: HTTP is a proper noun -->
## HTTP/2

HTTP/2 keeps the persistent connection and replaces the text framing with a binary one. Each request and response is split into frames, every frame carries a stream ID, and many streams share the single TCP connection at once. Because a frame names its own stream, a response for a later request can be written before an earlier one is ready, so a fast object is delivered while a slow one is still being produced. This is what removes application-layer (Layer 7) head-of-line blocking.

The streams are prioritized. A client can say that a script or a stylesheet matters more than an image, and the server is expected to order its work to match. Header fields are compressed with HPACK, which removes much of the cost of the repeated header block that 1.1 sent on every request.

TCP still delivers bytes in order, so a lost packet for one stream holds the data for every other stream in the receive buffer until the retransmission arrives, and [head-of-line blocking](head-of-line%20blocking.md#transport-layer%20hol%20blocking%20in%20tcp) moves down to the transport layer (Layer 4).

---

Flashcards for this section are as follows:

- HTTP/2 / framing ::@:: Binary frames replace the text message, and every frame carries the stream ID of the request it belongs to
- HTTP/2 / streams ::@:: Many request-response pairs share one persistent TCP connection, and a response can be written before an earlier one is ready
- HTTP/2 / stream prioritization ::@:: The client marks which streams matter most, and the server is expected to schedule its work to match
- HTTP/2 / header compression ::@:: HPACK compresses the repeated header block that HTTP 1.1 sent on every request
- HTTP/2 / remaining limitation ::@:: Runs over TCP, so a lost packet blocks all streams at Layer 4 because TCP delivers bytes in order
- application-layer HOL blocking / HTTP/2 ::@:: Removed, because a response for a later request can be sent before an earlier one is ready

<!-- check: ignore-next-line[header_style]: HTTP is a proper noun -->
## HTTP/3

HTTP/3 replaces TCP with QUIC (Quick UDP Internet Connections), standardized as RFC 9000 in 2021, so HTTP runs over QUIC on UDP. QUIC is a multiplexed transport protocol: each stream is reliable on its own, so a lost packet on one stream is retransmitted without holding up the others. The application can read a stream's data as soon as that stream is complete, even while another stream is still waiting.

Both HOL cases go away. Nothing waits for a sibling stream, and nothing waits for a lost packet. A persistent connection and out-of-order streams came with HTTP/2 and carry over, so both belong to 2.0 and 3.0 rather than to 3.0 alone.

---

Flashcards for this section are as follows:

- HTTP/3 / transport ::@:: QUIC over UDP gives each stream independent reliability, so a lost packet on one stream does not block others
- HTTP/3 vs HTTP/2 ::@:: HTTP/2 fixes HOL at Layer 7 with streams; HTTP/3 fixes both Layer 7 and Layer 4 by running over QUIC
- QUIC ::@:: A multiplexed transport protocol over UDP (RFC 9000, 2021) with per-stream reliability
- HTTP/3 / inherited features ::@:: Keeps HTTP/2's persistent connection and out-of-order streams, so both are true of 2.0 and 3.0

## version comparison

Each version keeps what it inherits. A property belongs to every version that has it, so a question naming a property and asking for a version gets the earliest one, even when later versions keep it.

| Property | HTTP 1.0 | HTTP 1.1 | HTTP 2.0 | HTTP 3.0 |
| --- | --- | --- | --- | --- |
| connection | new per object | persistent | persistent | persistent |
| requests in flight | one per connection | pipelined | multiplexed streams | multiplexed streams |
| response order | one at a time | in request order | out of order | out of order |
| transport | TCP | TCP | TCP | QUIC over UDP |
| client state kept by the server | none | none | none | none |
| head-of-line blocking in the response queue | no | yes | no | no |
| head-of-line blocking in the transport | no | no | yes | no |
| message format | text | text | binary frames | binary frames |

Head-of-line blocking appears in two different rows, and the reason differs. In 1.1 the response queue is ordered by request order, so a large object holds up the small objects queued behind it. In 2.0 the transport is ordered, so one lost packet holds up every stream on the connection. HTTP 1.0 escapes both by giving each object its own connection, and HTTP 3.0 escapes both because QUIC repairs each stream on its own.

Statelessness begins at 1.0, persistence becomes the default at 1.1, pipelining arrives at 1.1, and out-of-order multiplexed streams arrive at 2.0.

---

Flashcards for this section are as follows:

- earliest-version rule ::@:: A property that several HTTP versions have is credited to the earliest version that has it
- head-of-line blocking / versions that cause it ::@:: HTTP 1.1 first, where pipelined responses keep request order so a large object holds up the small ones behind it; 1.0 gives each object its own connection
- separate TCP connection per request ::@:: HTTP 1.0, which opens a new connection for every object; 1.1, 2.0, and 3.0 keep one connection
- parallel prioritized streams on one TCP connection ::@:: HTTP 2.0, which multiplexes prioritized streams over a single persistent connection; HTTP 3.0 keeps the multiplexing over QUIC
- persistent connections avoid handshake overhead ::@:: HTTP 1.1, where the persistent connection is the default and the handshake is paid once per connection
- server keeps no state about the client ::@:: HTTP 1.0, and every version after it; applications needing state store it elsewhere
- pipelined requests reduce round trips ::@:: HTTP 1.1, where several requests are written at once and cost one round trip for the batch
- out-of-order delivery for different requests in one connection ::@:: HTTP 2.0, whose streams may be served in any order; HTTP 3.0 keeps it
