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

There are four versions in use today. They differ over three things: whether a connection is reused, whether a response can overtake an earlier one, and what carries the bytes.

---

Flashcards for this section are as follows:

- what kind of protocol is HTTP? ::@:: An application-layer request-response protocol that retrieves hypermedia resources on the World Wide Web
- design trade-off ::@:: Text-based and variable-length: human-readable and extensible, but harder to parse than fixed-format protocols

## client-server model

HTTP follows a client-server model. The server is always on and well known; clients initiate contact by sending a request and receiving a reply.

The server keeps nothing about a client between requests. HTTP has been stateless since 1.0, so an application that needs state keeps it somewhere else. With nothing to remember between requests, one server can handle a high request rate.

---

Flashcards for this section are as follows:

- who starts the exchange? ::@:: The client. The server is always on and well known, and each request is answered before the next one goes out
- does the server remember a client between requests? ::@:: No, and it never has: HTTP has been stateless since 1.0
- why is statelessness worth having? ::@:: The server has nothing to rebuild between requests, so one server can handle a high request rate

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

The two common methods are GET, which fetches a resource, and POST, which sends data to the server. The common headers are `Host`, `User-agent`, `Connection`, and `Accept-language`. Every message states the version, in the request line or the status line. HTTP 1.1 made `Host` mandatory, since one address can serve many domain names at once.

---

Flashcards for this section are as follows:

- HTTP request message / structure ::@:: A request line (method, resource, protocol version), header lines, an optional body, and a blank CRLF separator
- HTTP response message / structure ::@:: A status line (protocol version, status code, status phrase), response headers, and an optional body
- `Host` header ::@:: Mandatory in every HTTP 1.1 request, since one address serves many domain names
- where does a message state the HTTP version? ::@:: In the request line of a request, and in the status line of a response

## persistent connections

Page load time (PLT) matters: 100 ms is the typical limit of human perception, and an Amazon study found every additional 100 ms of PLT costs 1% in profit.

HTTP 1.0 opens a new TCP connection per object: one RTT to initiate the connection, one RTT for the request and first response bytes, then file transmission time. For $n$ small objects, this costs $3n$ RTTs.

---

Flashcards for this section are as follows:

- page load time / 100 ms threshold ::@:: 100 ms is the typical limit of human perception; an Amazon study found every additional 100 ms of page load time costs 1% in profit
- RTT (round-trip time) ::@:: The time for a small packet to travel from client to server and back
- HTTP 1.0 response time: Given one object of known size, how many RTTs does HTTP 1.0 need? <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> ::@:: $2 \times \text{RTT} + \text{file transmission time}$, because one RTT opens the TCP connection and another carries the request and the first response bytes

### keep-alive in HTTP 1.0

HTTP 1.0 could reuse a connection, but only if both ends agreed to it. The client sent `Connection: Keep-Alive` (RFC 2068) and the server answered with the same header, after which the connection carried the next object too. Clients and servers disagreed often enough about when to stop that nobody relied on it, so in practice HTTP 1.0 is non-persistent and every object pays for a connection of its own.

---

Flashcards for this section are as follows:

- HTTP 1.0 / `Connection: Keep-Alive` ::@:: Reuse had to be asked for and agreed to, and the two ends disagreed about when to stop, so nobody used it
- HTTP 1.0 / page cost: A page has $n$ small objects and the connection is not persistent. How many RTTs? ::@:: $3n$, one new TCP connection for every object

### persistence as the default in HTTP 1.1

HTTP 1.1 dropped the negotiation and made the connection persistent by default. A client sends every request it has over one connection, and either side closes it when it is done. The TCP handshake is paid once per connection instead of once per object, so $n$ small objects cost $n + 2$ RTTs. Whatever bandwidth-delay product the first object measured still holds for the rest.

---

Flashcards for this section are as follows:

- HTTP 1.1 / page cost: A page has $n$ small objects on one persistent connection. How many RTTs? ::@:: $n + 2$, against $3n$ without persistence, since the handshake is paid once per connection
- when is the TCP handshake paid under HTTP 1.1? ::@:: Once per connection, not once per object
- who closes a persistent connection? ::@:: Either side, when it is finished with it

## pipelining

HTTP 1.1 added pipelining. The client writes several requests to one connection without waiting for the answers, and the server replies in the order the requests came in. A page of $n$ small objects then costs one round trip for the whole batch instead of one per object.

Pipelining works well when everything is ready at once. It falls apart when one object takes longer to produce than the others, say a page that queries a database. A ready object then waits behind the slow one, which is [head-of-line blocking](head-of-line%20blocking.md). The rule is in the protocol, not in the server: a server that could answer out of order is still not allowed to.

---

Flashcards for this section are as follows:

- what is pipelining, and which version added it? ::@:: Writing several requests to one connection without waiting for the answers, added in HTTP 1.1; the server answers in request order
- pipelining / round trips: $n$ requests are pipelined on one connection. How many round trips? ::@:: One, for the whole batch, not one per request
- what goes wrong with pipelining? ::@:: Responses keep request order, so a slow object holds up the ready ones behind it

<!-- check: ignore-next-line[header_style]: HTTP is a proper noun -->
## HTTP/2

HTTP/2 keeps the persistent connection and swaps the text messages for binary frames. Every frame names the stream it belongs to, and many streams share the one TCP connection. Because a frame names its own stream, a later response can go out before an earlier one is ready, so a fast object arrives while a slow one is still being made. That is what kills application-layer (Layer 7) head-of-line blocking.

Streams carry a priority too. A client can say that a script matters more than an image, and the server is meant to schedule its work to match. Headers go out compressed with HPACK, which matters because HTTP 1.1 sent the same header block on every request.

TCP still hands bytes over in order. A lost packet holds up every other stream in the receive buffer until the retransmission turns up, so [head-of-line blocking](head-of-line%20blocking.md#transport-layer%20hol%20blocking%20in%20tcp) moves down to the transport layer (Layer 4).

---

Flashcards for this section are as follows:

- what does HTTP/2 put on the wire? ::@:: Binary frames instead of the text message, each frame carrying the stream ID of the request it belongs to
- how do HTTP/2 streams clear the response queue? ::@:: Many requests share one persistent connection, and a response can be written before an earlier one is ready
- how are HTTP/2 streams prioritized? ::@:: The client marks which streams matter most, and the server schedules its work to match
- how does HTTP/2 shrink the header cost? ::@:: HPACK compresses the repeated header block that HTTP 1.1 sent on every request
- what is still wrong with HTTP/2? ::@:: It runs on TCP, which hands bytes over in order, so one lost packet blocks every stream at Layer 4

<!-- check: ignore-next-line[header_style]: HTTP is a proper noun -->
## HTTP/3

HTTP/3 runs on QUIC (Quick UDP Internet Connections) over UDP instead of TCP. QUIC became RFC 9000 in 2021. Each of its streams is reliable on its own, so a lost packet is retransmitted for that stream alone and the others keep moving. The application reads a stream as soon as that stream is complete, whatever the others are doing.

That clears both kinds of head-of-line blocking. Nothing waits on a sibling stream and nothing waits on a retransmission. The persistent connection and the out-of-order streams came with HTTP/2 and are still here, so both belong to 2.0 as well as 3.0.

---

Flashcards for this section are as follows:

- what does HTTP/3 run on? ::@:: QUIC over UDP, where each stream is reliable on its own, so a lost packet on one stream does not block the others
- how do HTTP/2 and HTTP/3 differ on head-of-line blocking? ::@:: HTTP/2 clears the Layer 7 queue with streams and keeps the Layer 4 one over TCP; HTTP/3 clears both by running on QUIC
- what is QUIC? ::@:: A multiplexed transport over UDP, RFC 9000 in 2021, where each stream is reliable on its own
- what does HTTP/3 inherit from HTTP/2? ::@:: The persistent connection and the out-of-order streams, so both are true of 2.0 and 3.0

## version comparison

Every version keeps what it inherited. So when a property shows up in several versions, the earliest one is the answer, even though the later ones still have it.

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

Head-of-line blocking sits in two rows because there are two ways to get stuck. In 1.1 the queue of responses is ordered, so a large object holds up the small ones behind it. In 2.0 the transport is ordered, so one lost packet holds up every stream on the connection. 1.0 has neither problem because every object has a connection of its own, and 3.0 has neither because QUIC repairs each stream on its own.

The short version: statelessness from 1.0, persistent connections and pipelining from 1.1, out-of-order multiplexed streams from 2.0.

---

Flashcards for this section are as follows:

- a property shows up in several versions; which one is the answer? ::@:: The earliest version that has it, even when the later ones keep it
- which version first has head-of-line blocking? ::@:: HTTP 1.1, where pipelined responses keep request order so a large object holds up the small ones behind it. 1.0 gives every object its own connection, so nothing queues
- which version opens a new TCP connection for every request? ::@:: HTTP 1.0. 1.1, 2.0, and 3.0 reuse one connection
- which version multiplexes prioritized streams over one TCP connection? ::@:: HTTP 2.0. 3.0 keeps the multiplexing, but runs it over QUIC
- which version made the persistent connection the default? ::@:: HTTP 1.1, where the TCP handshake is paid once per connection rather than once per object
- which version first had a stateless server? ::@:: HTTP 1.0, and every version after it. An application that needs state keeps it elsewhere
- which version added pipelining? ::@:: HTTP 1.1, where several requests are written at once and cost one round trip for the batch
- which version can answer two requests on one connection out of order? ::@:: HTTP 2.0, whose streams may be served in any order. 3.0 keeps it
