---
aliases:
  - ELEC 3120 transmission control protocol
  - ELEC3120 transmission control protocol
  - HKUST ELEC 3120 transmission control protocol
  - HKUST ELEC3120 transmission control protocol
  - TCP
  - Transmission Control Protocol
  - transmission control protocol
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/transmission_control_protocol
  - language/in/English
---

# transmission control protocol

The Transmission Control Protocol (TCP) turns the network's unreliable best-effort delivery into a reliable, ordered stream of bytes. An application writes bytes and reads bytes; TCP cuts them into segments, numbers them, retransmits what is lost, and delivers them in order. It also decides how fast to send, bounded by the receiver's buffer and the network's capacity. It is the transport protocol of the web, mail, and file transfer. A 1 GB file over a path of 10 Mbit/s takes about 800 seconds, and TCP spends that time filling the path and waiting for the acknowledgements that say the bytes arrived.

---

Flashcards for this section are as follows:

- what TCP offers: what abstraction does the Transmission Control Protocol (TCP) give an application? ::@:: A reliable, ordered stream of bytes, carried over an unreliable best-effort network.
- what the application sees: what unit does an application write and read with TCP? ::@:: Bytes; TCP alone decides where the segment boundaries fall.
- recovery: which mechanism repairs a lost segment? ::@:: Retransmission after the sender's timer expires or duplicate acknowledgements report the gap.

## byte stream

The stream has no message boundaries. TCP packs as many consecutive bytes as fit into one segment, and sends it when it reaches the maximum segment size or when a timer expires on a partly filled one. The maximum segment size is set by the path, commonly 1460 bytes, so header and data together still fit the network layer's limit. On such a path a 5000-byte file reaches the receiver as segments of 1460, 1460, 1460, and 620 bytes.

To fill a path of 10 Mbit/s with a round-trip time of 40 ms, the sender needs 50 kB in flight at once, and a 1 MB file transfer is about 20 such windows. Two windows limit the sender at once: the receiver's advertised window, which reports the room left in its buffer, and the congestion window, which the sender grows while acknowledgements keep arriving. The smaller of the two decides how many bytes may be in flight. The sender puts 50 kB on the path, the receiver acknowledges what has arrived and says how much room is left, and the sender replaces the acknowledged bytes with the next 50 kB of the file, so the path stays full until the file ends.

---

Flashcards for this section are as follows:

- stream service: what does TCP do with the bytes an application writes? ::@:: It packs consecutive bytes into segments, ignoring what the application called a message.
- when a segment leaves: which two events send a segment? ::@:: The segment reaches the maximum segment size, or its timer expires on a partly filled segment.
- maximum segment size: what does the maximum segment size limit? ::@:: The data in one segment, commonly 1460 bytes, so header and data fit the path.
- segment sizes: a file of $5000$ bytes travels over a path whose maximum segment size is $1460$ bytes; how is it cut into segments? ::@:: $5000 = 3 \times 1460 + 620$, so three segments of $1460$ bytes and a last one of $620$ bytes.
- window to fill a path: a path carries $10\,\text{Mbit/s}$ with a round-trip time of $40\,\text{ms}$; how much data must be in flight to fill it? ::@:: $10\,\text{Mbit/s} \times 0.04\,\text{s} = 400\,\text{kbit} = 50\,\text{kB}$.
- two windows: which two windows limit how many bytes a Transmission Control Protocol (TCP) sender may keep in flight, and which one decides? ::@:: The receiver's advertised window and the sender's congestion window; the smaller of the two decides.

## header

The header is at least 20 bytes, and the fixed part sits at fixed offsets, so both hosts read it without negotiation. Options may follow, padded to a multiple of four bytes, and the whole header is at most 60 bytes.

| octets | field | width |
| --- | --- | --- |
| 0–1 | source port | 16 bits |
| 2–3 | destination port | 16 bits |
| 4–7 | sequence number | 32 bits |
| 8–11 | acknowledgement number | 32 bits |
| 12, high nibble | data offset | 4 bits |
| 12, low nibble | reserved, zero | 4 bits |
| 13 | the eight control flags | 8 bits |
| 14–15 | window | 16 bits |
| 16–17 | checksum | 16 bits |
| 18–19 | urgent pointer | 16 bits |
| 20 onwards | options, padded to a multiple of four bytes | 0 to 40 bytes |

The widths add up: two 2-byte ports take 4 octets, the two 4-byte numbers take 8, the octet pair of data offset, reserved bits and flags takes 2, and the three remaining 2-byte fields take 6, which is 20. <p> ![Transmission Control Protocol header layout: bit columns marked 0, 15, 16 and 31 across a 32-bit wide diagram, with source port beside destination port, a full-width sequence number row, a full-width acknowledgement number row, a row holding data offset, reserved, the six flag bits URG ACK PSH RST SYN FIN and the window, then checksum beside urgent pointer, with options and data spanning the full width below and a bracket marking the first 20 bytes](../../../../archives/Wikimedia%20Commons/TCP%20header.png)

The data offset counts 32-bit words rather than bytes, so its value of 5 means 20 bytes and its maximum of 15 means 60. A segment with no options stores `0101` in those four bits, and the data begins at octet 20.

A `SYN` from port 49152 to port 80, with sequence number `0x1A2B3C4D` and the largest window, opens `C0 00 00 50 1A 2B 3C 4D 00 00 00 00 50 02 FF FF ?? ?? 00 00`. Octets 12 and 13 carry `50` and `02`: the `5` is the data offset in words and the `2` is the `SYN` bit. The two question marks stand for the checksum the sender computes over the segment, and the acknowledgement number is zero because the `ACK` flag is clear.

---

Flashcards for this section are as follows:

- header size: how long is the fixed part of a Transmission Control Protocol (TCP) header, and how long can the whole header become? ::@:: At least 20 bytes, at most 60 bytes with 40 bytes of options.
- which field demultiplexes: which two fields route a segment to the right application process? ::@:: The source port and the destination port, at octets 0 to 1 and 2 to 3.
- field offsets: at which octets does a Transmission Control Protocol (TCP) header keep its sequence number, its acknowledgement number and its window? ::@:: The sequence number at 4 to 7, the acknowledgement number at 8 to 11, and the window at 14 to 15.
- header arithmetic: how do the field widths of a Transmission Control Protocol (TCP) header add up to $20$ bytes? ::@:: Two 2-byte ports, two 4-byte numbers, one octet pair holding the data offset, reserved bits and flags, and three 2-byte fields, which is $4 + 8 + 2 + 6 = 20$.
- data offset: what does the data offset field of a Transmission Control Protocol (TCP) header measure, and in which unit? ::@:: The distance from the start of the segment to the data, counted in 32-bit words.
- data offset value: a header with no options has a data offset of $5$; how many bytes is that, and where does the data start? ::@:: $5 \times 4 = 20$ bytes, so the data starts at octet 20.
- maximum header: a data offset field of $4$ bits holds at most $15$ words; how long is that header? ::@:: $15 \times 4 = 60$ bytes.
- the header in a drawing: ![Transmission Control Protocol header layout: bit columns marked 0, 15, 16 and 31 across a 32-bit wide diagram, with source port beside destination port, a full-width sequence number row, a full-width acknowledgement number row, a row holding data offset, reserved, the six flag bits URG ACK PSH RST SYN FIN and the window, then checksum beside urgent pointer, with options and data spanning the full width below and a bracket marking the first 20 bytes](../../../../archives/Wikimedia%20Commons/TCP%20header.png) with bit columns from $0$ to $31$, which field sits in which row? ::@:: Source port beside destination port, then a full-width sequence number row, a full-width acknowledgement number row, then data offset, reserved, the six flags and the window, then checksum beside urgent pointer, and options and data across the full width below a bracket marking $20$ bytes.
- options field: where do the optional octets of a Transmission Control Protocol (TCP) header begin, how long may they run, and how are they padded? ::@:: They begin after the 20 fixed octets, run from 0 to 40 bytes since the whole header is 60 at most, and are padded to a multiple of four bytes.
- checksum and urgent pointer: at which octets do the checksum and the urgent pointer of a Transmission Control Protocol (TCP) header sit, and how wide is each? ::@:: The checksum at octets 16 to 17 and the urgent pointer at octets 18 to 19, each 16 bits wide.
- reserved bits: which bits of a Transmission Control Protocol (TCP) header are reserved, and what value do they hold? ::@:: The low nibble of octet 12, four bits wide, which is set to zero.
- the whole SYN transcript: which field does each group of octets carry in `C0 00 00 50 1A 2B 3C 4D 00 00 00 00 50 02 FF FF ?? ?? 00 00`? ::@:: `C0 00` is the source port 49152, `00 50` the destination port 80, `1A 2B 3C 4D` the sequence number, `00 00 00 00` the acknowledgement number, `50` the data offset and reserved bits, `02` the `SYN` flag, `FF FF` the largest window, `?? ??` the checksum, and `00 00` the urgent pointer.

### flag bits

Eight control bits sit in octet 13, one per flag, most significant first: `CWR`, `ECE`, `URG`, `ACK`, `PSH`, `RST`, `SYN` and `FIN`. Each is one bit, so the octet reads as a hexadecimal value and a combination of flags is the sum of its bits.

| flag | bit value | meaning |
| --- | --- | --- |
| `CWR` | `0x80` | congestion window reduced, sent in answer to `ECE` |
| `ECE` | `0x40` | the receiver saw congestion on the path |
| `URG` | `0x20` | the urgent pointer field is valid |
| `ACK` | `0x10` | the acknowledgement number field is valid |
| `PSH` | `0x08` | hand the data to the application at once |
| `RST` | `0x04` | abort the connection |
| `SYN` | `0x02` | synchronise sequence numbers, opening a connection |
| `FIN` | `0x01` | the sender has no more data |

An acknowledgement of a `SYN` sets both bits, so its octet 13 reads `0x10 + 0x02 = 0x12`; the third segment of the handshake, which carries only `ACK`, reads `0x10`; and the last segment of a close, a `FIN` that also acknowledges, reads `0x11`. The original specification reserved six bits and defined six flags, and `CWR` and `ECE` later took two of those reserved bits, which is why a drawing that labels six flags matches an older header.

---

Flashcards for this section are as follows:

- flag count: how many control flags does a Transmission Control Protocol (TCP) header carry, and where? ::@:: Eight, in octet 13, one bit each.
- flag order: in which order do the eight flags sit in octet 13? ::@:: CWR, ECE, URG, ACK, PSH, RST, SYN, FIN, most significant bit first.
- the two later flags: which two flags were added after the original specification, and what do they carry? ::@:: `CWR` and `ECE`, which report congestion to the sender and which took two of the reserved bits.
- combined flags: a segment that both synchronises and acknowledges has which value in octet 13, and why? ::@:: `0x12`, which is the `SYN` bit `0x02` plus the `ACK` bit `0x10`.
- closing segment: the `FIN` bit is $0x01$ and the `ACK` bit is $0x10$; what value does octet 13 hold in a segment that closes one direction and acknowledges the other? ::@:: $0x01 + 0x10 = 0x11$.
- acknowledgement only: a segment carries only the `ACK` flag, as in the third segment of the handshake; which value does octet 13 hold? ::@:: `0x10`, the `ACK` bit alone.

### byte order

Every multi-byte field is big-endian, with the most significant byte first on the wire. The standards call this network byte order, and the header of the User Datagram Protocol (UDP) follows the same rule.

Port 80 is `0x0050`, so its octets are `00` then `50`; read the other way round they would say `0x5000 = 20{,}480`. The sequence number `0x1A2B3C4D` travels as `1A 2B 3C 4D`. A field whose two octets are equal, such as a window of `0xFFFF`, reads the same in either order and so hides a byte-order mistake. The checksum covers the octets as they are, so a swapped field makes it fail.

---

Flashcards for this section are as follows:

- byte order: in which order do the multi-byte fields of a Transmission Control Protocol (TCP) header travel? ::@:: Big-endian, the most significant byte first, which the standards call network byte order.
- port in hex: port $80$ is $0x0050$; which octets carry it, and what would a little-endian reader see? ::@:: `00` then `50`; read the other way round, `50 00` would say $0x5000 = 20{,}480$.
- sequence number in hex: which four octets carry the sequence number $0x1A2B3C4D$? ::@:: `1A 2B 3C 4D`, most significant byte first.
- a symmetric field: why can a window of $0xFFFF$ not reveal a byte-order mistake? ::@:: Both octets are `FF`, so the value reads the same in either order.
- why byte order matters: what happens to a segment whose header is read in the wrong byte order? ::@:: The ports, sequence numbers and windows are all misread, so the data reaches the wrong process or the wrong place in the stream.

## sequence numbers

A segment whose first byte sits $k$ bytes past the initial sequence number $ISN$ has sequence number $ISN + k$, and the acknowledgement it draws names the byte after its last, $ISN + k + \text{length}$, with length counting the bytes the segment carries. Numbering bytes rather than packets means a retransmission can start at the exact byte the receiver is missing. A segment that carries 1000 bytes and starts at sequence number $ISN+5000$ is acknowledged with $ISN+6000$.

When a segment is lost, the sender's timer expires and it retransmits from the first byte the receiver has not acknowledged, and the duplicate bytes the receiver already holds are dropped by the sequence numbers. A segment of 1460 bytes that starts at sequence number $ISN+1460$ and is lost is therefore sent again from $ISN+1460$, and the receiver answers with $ISN+2920$ once it has it. A receiver that is missing a segment sends the same acknowledgement again for each later segment that arrives, and after three such duplicate acknowledgements the sender retransmits the gap without waiting for its timer.

---

Flashcards for this section are as follows:

- numbering: what does a Transmission Control Protocol (TCP) sequence number count? ::@:: Bytes of the stream, not packets: a segment's number is that of its first byte.
- segment sequence number: a segment starts $k$ bytes after the initial sequence number $ISN$ and carries data; which sequence number does it hold? ::@:: $ISN + k$, the number of its first byte.
- acknowledgement value: for a segment of $L$ bytes starting at sequence number $S$, what acknowledgement does the receiver send? ::@:: $S + L$, the number of the next byte it expects.
- why bytes rather than packets: what does numbering bytes allow that numbering packets does not? ::@:: A retransmission can start at the exact missing byte rather than repeating a whole packet.
- retransmission after a timeout: a segment of $1460$ bytes that starts at sequence number $ISN+1460$ is lost and the sender's timer expires; from which sequence number does the sender retransmit, and which number does the receiver acknowledge? ::@:: The sender retransmits from $ISN+1460$, and the receiver acknowledges $ISN + 1460 + 1460 = ISN+2920$, since the lost segment carried $1460$ bytes.
- duplicate acknowledgements: after how many duplicate acknowledgements does a Transmission Control Protocol (TCP) sender retransmit a gap without waiting for its timer? ::@:: After three.

### sequence space consumption

Data takes one number per byte, and two control segments take one number each: a `SYN` takes the number it starts the connection at, and a `FIN` takes the number after the last byte of data. Everything else takes none, since `ACK`, `PSH`, `URG`, `RST`, `CWR` and `ECE` sit in the header and leave the numbering untouched.

The two exceptions exist so that an opening and a closing can be acknowledged and retransmitted like data. An acknowledgement names the next byte the receiver expects, so a segment that carried no byte at all could not be acknowledged, and a lost `SYN` or `FIN` could not be retransmitted without an ambiguity between the original and the copy.

A connection that starts at number 1000, sends 500 bytes, then closes consumes 502 numbers: 1000 for the `SYN`, 1001 to 1500 for the data, and 1501 for the `FIN`, so the last acknowledgement reads 1502.

---

Flashcards for this section are as follows:

- which segments consume a number: which kinds of traffic consume a sequence number? ::@:: Data takes one per byte, a `SYN` takes one, and a `FIN` takes one.
- which segments do not consume a number: which flags leave the sequence space unchanged? ::@:: `ACK`, `PSH`, `URG`, `RST`, `CWR` and `ECE`.
- why SYN and FIN consume one: why does a `SYN` or a `FIN` take up a sequence number? ::@:: So it can be acknowledged and retransmitted like data, since an acknowledgement names the next byte and a segment carrying no byte could not be acknowledged.
- counting a connection: a connection starts at sequence number $1000$, sends $500$ bytes, then closes; how many numbers does it consume, and what does the last acknowledgement read? ::@:: $502$ numbers, $1$ for the `SYN` plus $500$ for the data plus $1$ for the `FIN`, so the last acknowledgement reads $1502$.
- where SYN and FIN sit: which number does a `SYN` take, and which number does a `FIN` take? ::@:: The `SYN` takes the number the connection starts at, and the `FIN` takes the number after the last byte of data.

### wraparound

The space is $2^{32} = 4{,}294{,}967{,}296$ bytes, a little over 4 GB, so the numbers repeat once a stream passes that many bytes. On a 10 Gbit/s link a stream that never stops sending wraps in $4{,}294{,}967{,}296 \times 8 / 10^{10} \approx 3.4$ seconds.

Comparisons across the wrap use serial number arithmetic, which compares the modular difference rather than the unsigned value, so the number after $2^{32}-1$ is 0 and a difference below $2^{31}$ counts as forward. The window stays below $2^{31}$ for the same reason, since a window above half the space would make a new segment and a very old one indistinguishable.

---

Flashcards for this section are as follows:

- size of the space: the sequence number field is $32$ bits wide; how many bytes does it cover before it wraps? ::@:: $2^{32} = 4{,}294{,}967{,}296$ bytes, a little over 4 GB.
- wrap time: a stream fills a $10\,\text{Gbit/s}$ link without stopping; how long does one wrap of the sequence space take? ::@:: $4{,}294{,}967{,}296 \times 8 = 34{,}359{,}738{,}368$ bits, and $34{,}359{,}738{,}368 / 10^{10} \approx 3.4$ seconds.
- after the wrap: which number follows $2^{32}-1$ in the sequence space? ::@:: $0$, since the space wraps around.
- comparing across the wrap: two numbers sit on either side of a wrap in a space of $2^{32}$; how does a receiver compare them? ::@:: By serial number arithmetic, which compares the modular difference so that a value below $2^{31}$ counts as forward.
- window limit: why is the window kept below $2^{31}$? ::@:: A window above half the space would make a new segment indistinguishable from a very old one.

### initial sequence number

The first byte's number is chosen rather than fixed. A connection is identified by its addresses and ports, and those are reused after a connection closes, so a very old segment can still be travelling when a new connection inherits them. Starting each connection at a fresh number means the straggler no longer fits the new connection's numbering and is discarded. A connection that opened at 1000 and closed at once leaves segments numbered 1000 and 1001 on the path; a later connection between the same addresses and ports that starts at 7,000,000 ignores them both, since neither number falls inside its window.

---

Flashcards for this section are as follows:

- why not zero: why does the Transmission Control Protocol (TCP) not start every connection at sequence number $0$? ::@:: Addresses and ports are reused, so a segment from an earlier connection could still be in flight and would be taken for valid data.
- what a connection is: which four values identify a connection? ::@:: The source and destination addresses and the source and destination ports.
- exchange: when do the two hosts learn each other's initial sequence numbers? ::@:: During connection setup, each host sending its own.

## connection setup

A connection opens with a three-way handshake, so that both hosts learn the other's initial sequence number and agree that the connection exists. Two segments would not do: each side has to send its own number and see it acknowledged, and only the third segment acknowledges the server's. <p> ![Transmission Control Protocol handshake: a client lifeline on the left and a server lifeline on the right, with an arrow labelled SYN seq=x running down to the server, an arrow labelled SYN-ACK ack=x+1 seq=y running back up to the client, and an arrow labelled ACK ack=y+1 seq=x+1 running down to the server beneath a grey band labelled data](../../../../archives/Wikimedia%20Commons/Tcp-handshake.svg)

The client may send data once it has the `SYN` and `ACK`; the server may once it has the final `ACK`. On a path that drops the first `SYN`, the client retransmits the same `SYN` with the same $x$, and the server answers the retransmission with `SYN` and `ACK` carrying $y$ and acknowledging $x+1$, so the handshake completes with the same numbers as on a path that lost nothing. If it is the server's `SYN` and `ACK` that is lost, the client's timer expires and it repeats the `SYN`, and the server answers again with the same $y$ and the same acknowledgement of $x+1$. If the client's final `ACK` is the one that is lost, the server retransmits its `SYN` and `ACK`, which reach a client that has already sent its `ACK`, and the client repeats the same acknowledgement.

---

Flashcards for this section are as follows:

- three-way handshake: which three segments open a Transmission Control Protocol (TCP) connection? ::@:: A `SYN` with the client's initial sequence number, a `SYN` and `ACK` from the server, and an `ACK` from the client.
- why three and not two: why does the handshake need a third segment? ::@:: Each side must send its own initial number and see it acknowledged, and only the third segment acknowledges the server's.
- when data may flow: after which segment may each side start sending data? ::@:: The client after the `SYN` and `ACK`, and the server after the final `ACK`.
- what the handshake establishes: which two facts does the handshake settle? ::@:: Each host learns the other's initial sequence number, and both agree that the connection exists.
- lossy handshake: on a path that drops the first `SYN`, which numbers $x$ and $y$ does the completed handshake use? ::@:: The client's $x$ and the server's $y$, with the server acknowledging $x+1$ and the client acknowledging $y+1$, exactly as on a path that lost nothing.
- the handshake in a drawing: ![Transmission Control Protocol handshake: a client lifeline on the left and a server lifeline on the right, with an arrow labelled SYN seq=x running down to the server, an arrow labelled SYN-ACK ack=x+1 seq=y running back up to the client, and an arrow labelled ACK ack=y+1 seq=x+1 running down to the server beneath a grey band labelled data](../../../../archives/Wikimedia%20Commons/Tcp-handshake.svg) with the client at $x$ and the server at $y$, which numbers sit on each arrow? ::@:: Two lifelines, a `SYN` arrow down carrying $x$, a `SYN` and `ACK` arrow back up carrying $y$ and acknowledging $x+1$, an `ACK` arrow down acknowledging $y+1$, and a grey band of data below it.

### handshake numbers

| # | direction | sequence number | acknowledgement | flags |
| --- | --- | --- | --- | --- |
| 1 | client to server | $x$ | none | `SYN` |
| 2 | server to client | $y$ | $x+1$ | `SYN`, `ACK` |
| 3 | client to server | $x+1$ | $y+1$ | `ACK` |

With $x = 1000$ and $y = 5000$ the three segments read `seq=1000`, `seq=5000 ack=1001`, and `seq=1001 ack=5001`. The first byte of data carries 1001, not 1000, because the `SYN` has already spent that number.

---

Flashcards for this section are as follows:

- handshake numbers: the client starts at $x$ and the server at $y$; which numbers do the second and third segments acknowledge? ::@:: The server acknowledges $x+1$ and the client acknowledges $y+1$.
- the first data byte: a client's initial sequence number is $1000$; which number does its first data byte carry? ::@:: $1000 + 1 = 1001$, because the `SYN` has already consumed $1000$.
- worked handshake: with $x = 1000$ and $y = 5000$, which three segments does the handshake carry? ::@:: `seq=1000`, then `seq=5000 ack=1001`, then `seq=1001 ack=5001`.

<!-- check: ignore-next-line[header_style]: SYN is an acronym -->
### SYN loss

A lost `SYN` produces no answer, so the client waits on a timer and retransmits. That timer cannot be estimated from a round-trip time the client has not measured yet, so the standard fixes a default of 3 seconds, with some implementations using 6. The delay is long enough that a user may reload the page; that aborts the pending connection and sends a new `SYN` at once. Each further retransmission of a `SYN` waits longer than the last, so a client that keeps trying backs off, and a client that gives up after three attempts spends $3 + 6 + 12 = 21$ seconds before it reports the failure.

---

Flashcards for this section are as follows:

- lost SYN: what does the client do when no `SYN` and `ACK` arrives? ::@:: The client waits for its timer and retransmits the `SYN`.
- default timer: how long does the standard say to wait before retransmitting a `SYN`? ::@:: 3 seconds, though some implementations use 6.
- why the wait is a guess: why can the client not time the retransmission as it times ordinary data? ::@:: The client has not measured a round-trip time on this connection yet, so it has nothing to base the timer on.
- the reload effect: what does reloading the page do when a `SYN` is lost? ::@:: The reload aborts the pending connection and sends a fresh `SYN` at once, which often works.
- backoff: a client retransmits a `SYN` after $3$, then $6$, then $12$ seconds; how long before it reports a failure? ::@:: $3 + 6 + 12 = 21$ seconds.

## connection teardown

Each direction of the connection closes on its own, and a `FIN` closes only the direction that carries it. A `FIN` occupies one byte of the sequence space, so it is acknowledged like data and retransmitted if it is lost.

---

Flashcards for this section are as follows:

- half close: after one host sends a `FIN` and it is acknowledged, what may each host still do? ::@:: The sender has finished writing; the other host may still send.
- FIN in the sequence space: how much of the sequence space does a `FIN` occupy? ::@:: One byte, so it is acknowledged like data and retransmitted if lost.
- two directions: how many `FIN` segments does a full close take? ::@:: Two, one for each direction.

### maximum segment lifetime

The maximum segment lifetime is the longest time a segment can survive inside the network before routers discard it. No field carries it, so it belongs to the network rather than to the protocol, and the standard fixes it at 2 minutes as an engineering choice.

The host that closes first, not the one that closes second, stays in `TIME_WAIT` for twice that lifetime, $2 \times 120 = 240$ seconds. The doubling covers one round of the exchange: the first lifetime lets the final acknowledgement reach the peer, and the second lets a retransmitted `FIN` arrive back and be acknowledged again. Without the second, a duplicate `FIN` would meet a connection that no longer exists, draw a `RST`, and the peer would report an error on a connection that closed cleanly.

Implementations shorten the wait: Linux and macOS keep a closed connection for about 60 seconds, and Windows defaults to 240 seconds and allows 30 to 300. The cost is that a closed socket holds its port for the whole wait, so the closing state, not the transfer, decides how fast a server spends its ports. On a 40 ms path a whole request takes one round trip for the handshake, one for the exchange and two for the close, which is 160 ms, so `TIME_WAIT` is $240/240.16 \approx 99.9\%$ of the socket's life.

---

Flashcards for this section are as follows:

- maximum segment lifetime: what is the maximum segment lifetime? ::@:: The longest time a segment can survive inside the network before routers discard it.
- default value: which value does the standard take for the maximum segment lifetime, and is it measured or chosen? ::@:: 2 minutes, an engineering choice rather than a measurement.
- TIME_WAIT length: the maximum segment lifetime is $120\,\text{s}$; how long does the host that closes first stay in `TIME_WAIT`, and why twice that? ::@:: $2 \times 120 = 240$ seconds: one lifetime for the final acknowledgement to arrive and one for a retransmitted `FIN` to come back.
- without the doubling: what would a duplicate `FIN` meet if the wait were only one lifetime? ::@:: A connection that no longer exists, so it would draw a `RST` and the peer would report an error on a connection that closed cleanly.
- real values: how long do Linux, macOS and Windows keep a connection in `TIME_WAIT`? ::@:: Linux and macOS about 60 seconds, and Windows 240 seconds by default with 30 to 300 allowed.
- share of a connection's life: on a $40\,\text{ms}$ path a whole request takes $160\,\text{ms}$ and `TIME_WAIT` takes $240\,\text{s}$; what fraction of the socket's life is spent closing? ::@:: $240\,\text{s} / (240\,\text{s} + 0.16\,\text{s}) = 240/240.16 \approx 99.9\%$.

### four segments

With the client closing first, the client's next byte is $c$ and the server's is $s$, and the exchange takes four segments:

| # | direction | sequence number | acknowledgement | flags | state after |
| --- | --- | --- | --- | --- | --- |
| 1 | client to server | $c$ | $s$ | `FIN`, `ACK` | client `FIN_WAIT_1`, server `CLOSE_WAIT` |
| 2 | server to client | $s$ | $c+1$ | `ACK` | client `FIN_WAIT_2` |
| 3 | server to client | $s$ | $c+1$ | `FIN`, `ACK` | server `LAST_ACK` |
| 4 | client to server | $c+1$ | $s+1$ | `ACK` | client `TIME_WAIT`, server `CLOSED` |

Segments 2 and 3 travel as one segment when the server's application has already closed, and as two when it has not: the acknowledgement of the client's `FIN` and the server's own `FIN` are separate events, and the second waits for the application. <p> ![Transmission Control Protocol close sequence drawn as two lanes, an initiator on the left in green and a passively closed peer on the right in pink, each split into an application lane and a kernel lane, with FIN and ACK arrows between the kernels, the states ESTABLISHED, FIN-WAIT-1, FIN-WAIT-2 and TIME-WAIT down the left and ESTABLISHED, CLOSE-WAIT and LAST-ACK down the right, a note that the connection is half closed once the first FIN is acknowledged, a note that a read on the passive side returns zero, and a wait of 240 seconds marked under TIME-WAIT](../../../../archives/Wikimedia%20Commons/TCP%20close%28%29%20-%20sequence%20diagram.svg)

---

Flashcards for this section are as follows:

- four segments: which four segments close a connection when the client closes first? ::@:: The client's `FIN`, the server's `ACK`, the server's `FIN`, and the client's `ACK`.
- teardown numbers: the client's next byte is $c$ and the server's is $s$ when the client closes; which sequence number and acknowledgement does each of the four segments carry? ::@:: `(c, s)` for the `FIN`, `(s, c+1)` for the `ACK`, `(s, c+1)` for the server's `FIN`, and `(c+1, s+1)` for the last `ACK`.
- states during a close: which states does the closing client pass through, and which the server? ::@:: The client goes `FIN_WAIT_1`, `FIN_WAIT_2`, `TIME_WAIT`; the server goes `CLOSE_WAIT`, `LAST_ACK`, `CLOSED`.
- the close in a drawing: ![Transmission Control Protocol close sequence drawn as two lanes, an initiator on the left in green and a passively closed peer on the right in pink, each split into an application lane and a kernel lane, with FIN and ACK arrows between the kernels, the states ESTABLISHED, FIN-WAIT-1, FIN-WAIT-2 and TIME-WAIT down the left and ESTABLISHED, CLOSE-WAIT and LAST-ACK down the right, a note that the connection is half closed once the first FIN is acknowledged, a note that a read on the passive side returns zero, and a wait of 240 seconds marked under TIME-WAIT](../../../../archives/Wikimedia%20Commons/TCP%20close%28%29%20-%20sequence%20diagram.svg) ::@:: Two lanes split into application and kernel, `FIN` and `ACK` arrows between the kernels, the states of the closing side down the left and of the passive side down the right, and a 240-second wait marked under `TIME_WAIT`.
- flags on the four segments: the client closes first; which flags does each of the four segments carry? ::@:: `FIN` and `ACK` on the client's `FIN`, `ACK` on the server's acknowledgement, `FIN` and `ACK` on the server's `FIN`, and `ACK` on the client's last segment.
- one segment or two: when does the server's acknowledgement of the client's `FIN` travel in the same segment as the server's own `FIN`? ::@:: Only when the server's application has already closed its side; otherwise the two are separate segments, and the second waits for that application.

### simultaneous close

Both hosts may close at once. Each sends a `FIN` while the connection is established, so each enters `FIN_WAIT_1` with its own `FIN` outstanding. Each then receives the other's `FIN` before any acknowledgement, so neither moves to `FIN_WAIT_2`; both enter `CLOSING` instead, and each leaves it for `TIME_WAIT` when the acknowledgement of its own `FIN` arrives. The states `CLOSE_WAIT` and `LAST_ACK` never appear, since neither side closes second, and both hosts hold the connection for the full 240 seconds.

---

Flashcards for this section are as follows:

- simultaneous close: both hosts send a `FIN` at once; which state does each enter after its `FIN_WAIT_1`? ::@:: `CLOSING`, because each receives the other's `FIN` before the acknowledgement of its own.
- leaving CLOSING: which segment moves a host from `CLOSING` to `TIME_WAIT`? ::@:: The acknowledgement of its own `FIN`.
- missing states: which two states never appear in a simultaneous close? ::@:: `CLOSE_WAIT` and `LAST_ACK`, since neither side closes second.

### lost teardown segments

Each of the four segments can be lost, and each loss is repaired by a timer, since a segment that carries no acknowledgement of its own is discovered only by waiting.

A lost `FIN` is retransmitted on its timer, because it occupies a sequence number and is acknowledged like data; the receiver has seen nothing, so no other state changes. A lost acknowledgement of a `FIN` leaves the sender in `FIN_WAIT_1` or `LAST_ACK` with its timer running, so it retransmits the same `FIN` with the same sequence number, and the receiver answers it again.

A lost final `ACK` is the case the doubling exists for. The second side sits in `LAST_ACK`, times out, and retransmits its `FIN`; the first side is in `TIME_WAIT`, which still holds the connection, so it answers the duplicate `FIN` with another `ACK` and restarts the 240-second timer.

---

Flashcards for this section are as follows:

- lost FIN: how is a lost `FIN` repaired? ::@:: The sender retransmits it on its timer, since a `FIN` occupies a sequence number and is acknowledged like data.
- lost ACK of a FIN: what does a host in `FIN_WAIT_1` or `LAST_ACK` do when the acknowledgement of its `FIN` does not arrive? ::@:: It retransmits the same `FIN` with the same sequence number, and the receiver acknowledges it again.
- lost final ACK: which state answers a duplicate `FIN`, and why does that matter? ::@:: `TIME_WAIT` still holds the connection, so it answers with another `ACK` and restarts the timer; without it the duplicate would draw a `RST`.

### half close

A `FIN` closes one direction only. The host that sent it may not send again, but it may still receive, and the peer may keep sending for as long as its application has data. This is what `FIN_WAIT_2` is for: the host has closed its own side and waits for the peer's `FIN`, while the peer sits in `CLOSE_WAIT` until its application finally closes.

A read on the peer at that moment returns zero bytes rather than blocking, which is how an application learns that its peer has finished. A host whose application never closes leaves the socket in `FIN_WAIT_2` for ever, so Linux bounds it with a 60-second timeout. A client that finishes its request early uses the same mechanism: it sends its `FIN` after the request and keeps reading the reply, which arrives on what is now a one-way connection.

---

Flashcards for this section are as follows:

- FIN_WAIT_2: what is a host in `FIN_WAIT_2` waiting for? ::@:: The peer's `FIN`, having already closed its own side.
- the read that returns zero: what does a read return once the peer has closed its side? ::@:: Zero bytes, which tells the application that the peer has finished.
- an application that never closes: what happens to a connection whose application never closes after the peer's `FIN`? ::@:: The closing host waits in `FIN_WAIT_2` while the peer holds `CLOSE_WAIT`, and Linux bounds the wait with a 60-second timeout.
- early close: why would a client send its `FIN` before reading the reply? ::@:: It has finished writing, so it half-closes and keeps reading the one-way reply.

### reset

A host that cannot continue sends `RST` instead of `FIN`, for instance because its application process crashed. The other host does not acknowledge a reset, so the reset is not delivered reliably, and any data still in flight is lost. Sending anything more on the connection draws another `RST`. A host that receives a segment for a connection it does not have answers with a `RST` of its own, so a client that opens a connection to a port where nothing is listening learns at once instead of waiting for a reply. The `RST` comes back in answer to the client's `SYN`, and the client reports the connection as refused.

A reset takes no sequence number, since it never becomes part of the stream. The segment it answers sets its numbers instead: a `RST` sent in reply to a segment that had `ACK` set carries that segment's acknowledgement number as its own sequence number, and a `RST` sent for a segment without `ACK` carries zero in that field and leaves its acknowledgement field at zero.

---

Flashcards for this section are as follows:

- reset: which segment ends a connection abruptly, and what becomes of data still in flight? ::@:: A `RST`, after which the data in flight is lost.
- reliability of a reset: why is a `RST` not delivered reliably? ::@:: The receiving host does not acknowledge it.
- continuing after a reset: what happens if one host keeps sending on a reset connection? ::@:: Each further segment draws another `RST`.
- reset for an unknown connection: what does a host send when it receives a segment for a connection it does not have? ::@:: A `RST`, so the sender learns at once instead of waiting for a reply.
- reset numbering: how much of the sequence space does a `RST` take? ::@:: None, since it never becomes part of the stream.
- reset numbers: which sequence number does a `RST` carry when it answers a segment that had `ACK` set? ::@:: That segment's acknowledgement number, so the peer can match the reset to its connection.

## connection states

The connection is a state machine, and every segment that arrives or leaves moves it. It starts at `CLOSED`, which is not a state the protocol can be observed in but the absence of a connection: no transfer control block exists, so the standard calls it fictional. Eleven states are defined, and each one names what that host is waiting for before it can move on.

---

Flashcards for this section are as follows:

- connection states: how many states does the Transmission Control Protocol (TCP) define? ::@:: Eleven.
- CLOSED: why does the standard call `CLOSED` fictional? ::@:: It means no transfer control block exists at all, so no connection can be observed in it.

### eleven states

| state | which host | waits for | can carry data |
| --- | --- | --- | --- |
| `CLOSED` | neither | an open or a listen | no |
| `LISTEN` | the server | a `SYN` from a client | no |
| `SYN_SENT` | the client | a `SYN` and `ACK` from the server | no |
| `SYN_RECEIVED` | the server | the final `ACK` of the handshake | no |
| `ESTABLISHED` | both | data in either direction | yes |
| `FIN_WAIT_1` | the closer | the `ACK` of its `FIN`, or the peer's `FIN` | no |
| `FIN_WAIT_2` | the closer | the peer's `FIN` | receives only |
| `CLOSE_WAIT` | the peer | its own application to close | receives only |
| `CLOSING` | the closer | the `ACK` of its own `FIN` | no |
| `LAST_ACK` | the peer | the `ACK` of its `FIN` | no |
| `TIME_WAIT` | the closer | $2 \times 120 = 240$ seconds to pass | no |

---

Flashcards for this section are as follows:

- LISTEN: which host waits in `LISTEN`, and what is it waiting for? ::@:: The server, waiting for a `SYN` from a client.
- SYN_SENT: which host waits in `SYN_SENT`, and what is it waiting for? ::@:: The client, waiting for a `SYN` and `ACK` from the server.
- SYN_RECEIVED: which host waits in `SYN_RECEIVED`, and what is it waiting for? ::@:: The server, waiting for the final `ACK` of the handshake.
- ESTABLISHED: in which state may either host send data? ::@:: `ESTABLISHED` only.
- FIN_WAIT_1: what is a host in `FIN_WAIT_1` waiting for? ::@:: The acknowledgement of its `FIN`, or the peer's own `FIN`.
- CLOSE_WAIT: what is a host in `CLOSE_WAIT` waiting for? ::@:: Its own application to close the connection.
- LAST_ACK: what is a host in `LAST_ACK` waiting for? ::@:: The acknowledgement of its `FIN`.
- data in a closed half: which states may still receive data, and which may send it? ::@:: `FIN_WAIT_2` and `CLOSE_WAIT` may receive; only `ESTABLISHED` may send.

### opening transitions

Five transitions open a connection, and a `SYN` or an `ACK` is the only segment that causes any of them. A server goes from `CLOSED` to `LISTEN` when its application asks to listen, to `SYN_RECEIVED` when a `SYN` arrives, and to `ESTABLISHED` when the final `ACK` arrives. A client goes from `CLOSED` to `SYN_SENT` when its application connects, and to `ESTABLISHED` when the `SYN` and `ACK` arrive.

A simultaneous open runs both paths at once: each host sends a `SYN` from `SYN_SENT`, each receives one that has no `ACK`, and both move to `SYN_RECEIVED` before reaching `ESTABLISHED`.

---

Flashcards for this section are as follows:

- server opening: which three states does a server pass through to open a connection? ::@:: `LISTEN`, `SYN_RECEIVED`, and `ESTABLISHED`.
- client opening: which two states does a client pass through to open a connection? ::@:: `SYN_SENT` and `ESTABLISHED`.
- simultaneous open: which state do both hosts enter when they send a `SYN` at the same time? ::@:: `SYN_RECEIVED`.
- what causes an opening transition: which segments can cause one of the five transitions that open a connection? ::@:: Only a `SYN` or an `ACK`; no other segment causes any of them.

### closing transitions

A host that closes first goes from `ESTABLISHED` to `FIN_WAIT_1` on sending its `FIN`. An `ACK` moves it to `FIN_WAIT_2`, and the peer's `FIN` moves it from there to `TIME_WAIT`; a `FIN` that arrives before the `ACK` sends it through `CLOSING` instead. The peer goes from `ESTABLISHED` to `CLOSE_WAIT` when the `FIN` arrives, to `LAST_ACK` when its application closes, and to `CLOSED` when its own `FIN` is acknowledged.

`TIME_WAIT` leaves only on the timer, so that one transition is the only one in the machine that no segment can cause.

---

Flashcards for this section are as follows:

- closing first: which state follows `ESTABLISHED` on the host that sends the first `FIN`? ::@:: `FIN_WAIT_1`.
- FIN_WAIT_1 exits: which two segments can move a host out of `FIN_WAIT_1`, and to which state? ::@:: An `ACK` moves it to `FIN_WAIT_2`, and a `FIN` moves it to `CLOSING`.
- leaving TIME_WAIT: which segment moves a host out of `TIME_WAIT`? ::@:: None; only the 240-second timer takes it to `CLOSED`.
- FIN_WAIT_2 exit: which segment moves a host from `FIN_WAIT_2` to `TIME_WAIT`? ::@:: The peer's `FIN`.
- the peer's transitions: which events move the host that closes second from `ESTABLISHED` all the way to `CLOSED`? ::@:: The arriving `FIN` moves it to `CLOSE_WAIT`, its own application closing moves it to `LAST_ACK`, and the acknowledgement of its `FIN` moves it to `CLOSED`.

### state diagram

The diagram draws all eleven states and every transition on one page, with the client's path in red, the server's in blue and the unusual events as dotted arrows. <p> ![Transmission Control Protocol state diagram: CLOSED at the top right beside a start marker, LISTEN below it, SYN RECEIVED on the left and SYN SENT on the right below those, ESTABLISHED in the middle below a note that data exchange occurs there, then an active close box holding FIN WAIT 1, CLOSING, FIN WAIT 2 and TIME WAIT, a passive close box holding CLOSE WAIT and LAST ACK, and CLOSED again at the bottom, with red arrows for the client path, blue arrows for the server path, dotted arrows for unusual events, and the three handshake steps numbered alongside their arrows](../../../../archives/Wikimedia%20Commons/Tcp%20state%20diagram%20fixed%20new.svg)

A client that opens and closes normally runs `CLOSED`, `SYN_SENT`, `ESTABLISHED`, `FIN_WAIT_1`, `FIN_WAIT_2`, `TIME_WAIT`, `CLOSED`; a server that opens and closes second runs `CLOSED`, `LISTEN`, `SYN_RECEIVED`, `ESTABLISHED`, `CLOSE_WAIT`, `LAST_ACK`, `CLOSED`. The dotted arrows are the events that need a loss or a crash: a `RST` in either direction, a simultaneous open, and a `FIN` that arrives while a `FIN` is already outstanding.

---

Flashcards for this section are as follows:

- reading the diagram: which colour marks the client's path and which the server's? ::@:: Red for the client and blue for the server, with dotted arrows for unusual events.
- client path: which seven states does a client pass through when it opens and closes normally? ::@:: `CLOSED`, `SYN_SENT`, `ESTABLISHED`, `FIN_WAIT_1`, `FIN_WAIT_2`, `TIME_WAIT`, and `CLOSED`.
- server path: which seven states does a server pass through when it opens and closes second? ::@:: `CLOSED`, `LISTEN`, `SYN_RECEIVED`, `ESTABLISHED`, `CLOSE_WAIT`, `LAST_ACK`, and `CLOSED`.
- dotted arrows: which events does the diagram draw as dotted arrows? ::@:: A `RST` in either direction, a simultaneous open, and a `FIN` that arrives while a `FIN` is already outstanding.
- the diagram: ![Transmission Control Protocol state diagram: CLOSED at the top right beside a start marker, LISTEN below it, SYN RECEIVED on the left and SYN SENT on the right below those, ESTABLISHED in the middle below a note that data exchange occurs there, then an active close box holding FIN WAIT 1, CLOSING, FIN WAIT 2 and TIME WAIT, a passive close box holding CLOSE WAIT and LAST ACK, and CLOSED again at the bottom, with red arrows for the client path, blue arrows for the server path, dotted arrows for unusual events, and the three handshake steps numbered alongside their arrows](../../../../archives/Wikimedia%20Commons/Tcp%20state%20diagram%20fixed%20new.svg) ::@:: `CLOSED` and a start marker at the top, `LISTEN` below, `SYN RECEIVED` and `SYN SENT` below that, `ESTABLISHED` in the middle, an active close box with `FIN WAIT 1`, `CLOSING`, `FIN WAIT 2` and `TIME WAIT`, a passive close box with `CLOSE WAIT` and `LAST ACK`, and `CLOSED` at the bottom.

### whole conversation

One complete connection, from the first `SYN` to the last `ACK`: the client starts at $x = 1000$ and the server at $y = 5000$, the client sends a request of 100 bytes, the server replies with 500, and the client closes first.

| # | from | flags | sequence number | acknowledgement | what it does |
| --- | --- | --- | --- | --- | --- |
| 1 | client | `SYN` | $1000$ | none | opens; consumes 1000; client to `SYN_SENT` |
| 2 | server | `SYN`, `ACK` | $5000$ | $1001$ | server to `SYN_RECEIVED` |
| 3 | client | `ACK` | $1001$ | $5001$ | both to `ESTABLISHED` |
| 4 | client | `ACK` | $1001$ | $5001$ | request bytes 1001 to 1100 |
| 5 | server | `ACK` | $5001$ | $1101$ | request received, nothing to send yet |
| 6 | server | `ACK` | $5001$ | $1101$ | reply bytes 5001 to 5500 |
| 7 | client | `ACK` | $1101$ | $5501$ | reply received |
| 8 | client | `FIN`, `ACK` | $1101$ | $5501$ | closes; consumes 1101; client to `FIN_WAIT_1` |
| 9 | server | `ACK` | $5501$ | $1102$ | client to `FIN_WAIT_2`, server to `CLOSE_WAIT` |
| 10 | server | `FIN`, `ACK` | $5501$ | $1102$ | consumes 5501; server to `LAST_ACK` |
| 11 | client | `ACK` | $1102$ | $5502$ | client to `TIME_WAIT`, server to `CLOSED` |

The client consumes $1000$ for the `SYN`, $1001$ to $1100$ for its data and $1101$ for the `FIN`, $102$ numbers, so its next byte is $1000 + 102 = 1102$; the server consumes $5000$, $5001$ to $5500$ and $5501$, $502$ numbers, so its next byte is $5000 + 502 = 5502$. Segments 4 to 7 carry `PSH` as well when the sender wants the data handed over at once; the flag changes nothing about the numbering.

---

Flashcards for this section are as follows:

- data numbering: the client sends $100$ bytes starting at $1001$; which bytes does it cover, and which acknowledgement does the server return? ::@:: $1001 + 100 - 1 = 1100$, so bytes $1001$ to $1100$, acknowledged with $1100 + 1 = 1101$.
- the closing FIN: after $100$ bytes from sequence number $1001$, which number does the client's `FIN` carry? ::@:: $1100 + 1 = 1101$, the number after its last data byte.
- both sides at once: in one connection the client consumes $102$ numbers from $1000$ and the server $502$ from $5000$; which numbers do their last segments carry? ::@:: The client's last `ACK` carries $1000 + 102 = 1102$ and the server's `FIN` carries $5000 + 502 - 1 = 5501$.
- PSH: a data segment carries `PSH` as well as `ACK`; how does that change the sequence numbers? ::@:: It does not; `PSH` takes no sequence number and only asks the receiver to hand the data over at once.
- the server's reply: the client's request covers bytes $1001$ to $1100$; which two segments does the server send, and what does each carry? ::@:: First an `ACK` with sequence number $5001$ and acknowledgement $1100 + 1 = 1101$ carrying no data, then the reply of $500$ bytes from sequence number $5001$ to $5001 + 500 - 1 = 5500$.
- the client's acknowledgement of the reply: the server sent $500$ bytes from sequence number $5001$; which sequence number and acknowledgement does the client's next segment carry? ::@:: Sequence number $1100 + 1 = 1101$ and acknowledgement $5500 + 1 = 5501$.
- the client's close: the client's next byte is $1101$ and the server's is $5501$; which flags, sequence number and acknowledgement does the client's `FIN` carry, and which state does the client enter? ::@:: `FIN` and `ACK`, sequence number $1101$, acknowledgement $5501$, and the client enters `FIN_WAIT_1`.
- the server's close: the client's `FIN` carried sequence number $1101$; which two segments does the server send, and which state does each one leave it in? ::@:: An `ACK` with sequence number $5501$ and acknowledgement $1101 + 1 = 1102$, which moves the client to `FIN_WAIT_2` and the server to `CLOSE_WAIT`; then a `FIN` and `ACK` with sequence number $5501$ and acknowledgement $1102$, which moves the server to `LAST_ACK`.
