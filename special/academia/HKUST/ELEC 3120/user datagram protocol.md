---
aliases:
  - ELEC 3120 user datagram protocol
  - ELEC3120 user datagram protocol
  - HKUST ELEC 3120 user datagram protocol
  - HKUST ELEC3120 user datagram protocol
  - UDP
  - User Datagram Protocol
  - user datagram protocol
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/user_datagram_protocol
  - language/in/English
---

# user datagram protocol

The User Datagram Protocol (UDP) gives applications the multiplexing that the network layer lacks and stops there: no handshake, no delivery guarantee, no ordering, no pacing. RFC 768 defined it in 1980. A lost packet stays lost, and the application decides what that means. A server can answer thousands of queries a second without holding a connection open, since nothing about a datagram is remembered once it is sent.

---

Flashcards for this section are as follows:

- UDP: what does the User Datagram Protocol (UDP) provide above the network layer? ::@:: Multiplexing and demultiplexing for application processes, and nothing else.
- loss handling: who handles a lost packet in the User Datagram Protocol (UDP)? ::@:: The application, which decides what the loss means.
- the standard: which document defined the User Datagram Protocol (UDP), and in what year? ::@:: Request for Comments 768 (RFC 768), in 1980.
- what a server remembers: what does a User Datagram Protocol (UDP) server keep about a datagram once it has been sent? ::@:: Nothing, which lets one server answer thousands of queries a second without holding a connection open.

## header

The header is exactly eight bytes: four 16-bit fields in a fixed order, followed by the data.

| octets | field | width |
| --- | --- | --- |
| 0–1 | source port | 16 bits |
| 2–3 | destination port | 16 bits |
| 4–5 | length of header and data | 16 bits |
| 6–7 | checksum | 16 bits |
| 8 onwards | data | the rest of the datagram |

The destination port drives demultiplexing, and the length covers the header and the data together, so the smallest legal value is 8. <p> ![User Datagram Protocol header layout: two rows of two 16-bit fields, source port and destination port on the first and length and checksum on the second, with a full-width application data row below and bit columns 0, 15, 16 and 31 marked](../../../../archives/Wikimedia%20Commons/Header%20of%20UDP.svg)

Because the length field is 16 bits, the whole datagram is at most $65{,}535$ bytes. Inside Internet Protocol version 4 (IPv4) the enclosing packet also has to fit a 16-bit total length, and the 20-byte header is part of that total, so the datagram can be at most $65{,}535 - 20 = 65{,}515$ bytes and the data at most $65{,}507$. Inside Internet Protocol version 6 (IPv6) the payload length counts only what follows the 40-byte header, so nothing is taken from the datagram by the header in front of it and the data may reach $65{,}535 - 8 = 65{,}527$ bytes.

A query carrying 12 bytes of data has a length field of 20, and the datagram occupies 20 bytes on the wire. Taking port 1234 as the source and port 53 as the destination, the first six octets read `04 D2 00 35 00 14`: source port, destination port, and length.

---

Flashcards for this section are as follows:

- UDP header: which four fields make up the header of the User Datagram Protocol (UDP)? ::@:: The source port, the destination port, the length, and the checksum.
- header length: how long is a User Datagram Protocol (UDP) header, and does it carry options? ::@:: Exactly eight bytes, with no options.
- field order: in which order do the four fields of a User Datagram Protocol (UDP) header appear, and at which octets? ::@:: Source port at octets 0–1, destination port at 2–3, length at 4–5, checksum at 6–7, then the data.
- length arithmetic: a User Datagram Protocol (UDP) datagram carries $100$ bytes of data; what does its length field read? ::@:: $100 + 8 = 108$ bytes, because the length counts the eight-byte header as well as the data.
- maximum payload in IPv4: a User Datagram Protocol (UDP) datagram has a $16$-bit length field and travels inside a $20$-byte Internet Protocol version 4 (IPv4) header; what is the largest payload it can carry? ::@:: $65{,}507$ bytes: $2^{16} - 1 = 65{,}535$, less the $20$-byte Internet Protocol version 4 (IPv4) header and the $8$-byte User Datagram Protocol (UDP) header, so $65{,}535 - 20 - 8 = 65{,}507$.
- maximum payload in IPv6: the length field is at most $65{,}535$, the User Datagram Protocol (UDP) header is $8$ bytes and the $40$-byte Internet Protocol version 6 (IPv6) header sits outside the payload length; what is the largest payload? ::@:: $65{,}535 - 8 = 65{,}527$ bytes, because only the eight-byte User Datagram Protocol (UDP) header is subtracted from the datagram.
- the first six octets: a datagram leaves port $1234$ for port $53$ carrying $12$ bytes; which six octets open it? ::@:: `04 D2 00 35 00 14`: $1234 = 0x04D2$, $53 = 0x35$, and $12 + 8 = 20 = 0x14$.
- the header in a drawing: ![User Datagram Protocol header layout: two rows of two 16-bit fields, source port and destination port on the first and length and checksum on the second, with a full-width application data row below and bit columns 0, 15, 16 and 31 marked](../../../../archives/Wikimedia%20Commons/Header%20of%20UDP.svg) ::@:: Two rows of two 16-bit fields with bit columns 0, 15, 16 and 31 marked, source port beside destination port, length below source port, checksum below destination port, and one full-width row of application data underneath.
- drawing the header: how is a User Datagram Protocol (UDP) header drawn, and where do the bit numbers fall? ::@:: As a block 32 bits wide, split into a left half at bits 0 to 15 and a right half at bits 16 to 31, with source port and length on the left and destination port and checksum on the right, and the data spanning the full width below. <p> ![User Datagram Protocol header layout: two rows of two 16-bit fields, source port and destination port on the first and length and checksum on the second, with a full-width application data row below and bit columns 0, 15, 16 and 31 marked](../../../../archives/Wikimedia%20Commons/Header%20of%20UDP.svg)
- demultiplexing field: which header field decides the application that receives a User Datagram Protocol (UDP) datagram? ::@:: The destination port, held in octets 2 and 3.
- the largest datagram: the length field of a User Datagram Protocol (UDP) header is $16$ bits; what is the largest whole datagram, header included? ::@:: $2^{16} - 1 = 65{,}535$ bytes, counting the eight-byte header and the data together.

### byte order

Every 16-bit field is big-endian: the more significant byte comes first on the wire. The standards call this network byte order, and both headers in the transport layer use it.

Port 1234 is $0x04D2$ in hexadecimal, so its two octets are `04` then `D2`. A receiver that read them the other way round would get $0xD204 = 53{,}764$, which is a different port. The sequence numbers of the Transmission Control Protocol (TCP) follow the same rule, so $0x1A2B3C4D$ travels as `1A 2B 3C 4D`. A field whose two bytes are equal, such as a window of $65{,}535$, reads `FF FF` in either order, so it cannot reveal a byte-order mistake; the checksum covers the octets as they are, so a swapped field changes it.

---

Flashcards for this section are as follows:

- byte order: in which order do the multi-byte fields of a transport header travel? ::@:: Big-endian, the more significant byte first, which the standards call network byte order.
- port in hex: port $1234$ is $0x04D2$; which two octets carry it, and what would a little-endian reader see? ::@:: `04` then `D2`; read the other way round, the octets `D2 04` would say $0xD204 = 13 \times 4096 + 2 \times 256 + 4 = 53{,}248 + 512 + 4 = 53{,}764$.
- a sequence number in hex: which four octets carry the sequence number $0x1A2B3C4D$? ::@:: `1A 2B 3C 4D`, most significant byte first.
- why byte order matters: which two faults does a receiver make if it reads a header in the wrong byte order? ::@:: It sends the data to a different port and misreads the length.
- a symmetric field: why can a User Datagram Protocol (UDP) length of $0xFFFF$ not reveal a byte-order mistake? ::@:: Both of its octets are `FF`, so the value reads the same in either order.

### checksum

A checksum is a small value computed from a block of data so that transmission errors can be detected. The simplest scheme exclusive-ors every 32-bit word of the packet and appends the result; the receiver recomputes and compares it, and a mismatch means some data was corrupted on the way. UDP computes its check differently: the one's complement of the one's complement sum of the 16-bit words of the datagram. In UDP the check is optional, and a checksum field of zero tells the receiver not to verify it.

The datagram alone does not say where it came from, so the sum also covers a pseudo-header built from the addresses. For Internet Protocol version 4 (IPv4) it is 12 bytes: the source address, the destination address, a zero byte, the protocol number 17, and the UDP length. For Internet Protocol version 6 (IPv6) it is 40 bytes: the two 16-byte addresses, the 4-byte UDP length, three zero bytes, and the next-header value. The pseudo-header is never transmitted; both hosts rebuild it from the packet they already have, which is what rejects a datagram delivered to the wrong host or a misdelivered protocol. A receiver adds the pseudo-header and the datagram, and a correct sum is all ones.

Internet Protocol version 4 (IPv4) lets a sender leave the field at zero; Internet Protocol version 6 (IPv6) requires the checksum.

---

Flashcards for this section are as follows:

- checksum: what is a checksum? ::@:: A small value derived from a block of data so that errors introduced in transmission or storage can be detected.
- simplest scheme: how does exclusive-or checksumming work? ::@:: Exclusive-or every 32-bit word together, append the result, and let the receiver recompute and compare.
- optional check: what does a checksum field of zero mean in the User Datagram Protocol (UDP)? ::@:: That the receiver should not verify the checksum.
- checksum coverage: besides the header and the data, what does the User Datagram Protocol (UDP) checksum cover? ::@:: A pseudo-header holding the source and destination addresses, the protocol number and the UDP length, so a datagram delivered to the wrong host is rejected too.
- pseudo-header sizes: the pseudo-header of Internet Protocol version 4 (IPv4) holds two 4-byte addresses, a zero byte, a one byte and a 2-byte length, and that of version 6 (IPv6) holds two 16-byte addresses, a 4-byte length, three zero bytes and a one byte; how long is each? ::@:: 12 bytes for IPv4 and 40 bytes for IPv6.
- why a pseudo-header: how do two hosts agree on a pseudo-header that is never transmitted? ::@:: Each rebuilds it from the addresses and length already in the packet, so nothing extra travels.
- the receiver's check: what value does a correct one's complement sum reach at the receiver? ::@:: All ones, which is why a correct sum is told apart from a corrupted one.
- checksum computation: how does the User Datagram Protocol (UDP) compute the checksum of a datagram? ::@:: As the one's complement of the one's complement sum of the 16-bit words of the datagram and its pseudo-header.
- a zero checksum by version: in which Internet Protocol version may a sender leave the User Datagram Protocol (UDP) checksum at zero? ::@:: Internet Protocol version 4 (IPv4) only, since Internet Protocol version 6 (IPv6) requires the checksum.

## applications without recovery

Real-time traffic often prefers a dropped packet to a late one: a retransmitted voice sample arrives after the moment it described. A Voice over IP (VoIP) call commonly sends 20 ms of audio per packet, and a lost packet is covered from the samples around it rather than retransmitted. Applications that build their own reliability also start here, which is how QUIC runs over UDP. Some senders add error-correcting codes beside the samples, so the receiver can rebuild a lost one without asking for a retransmission. A datagram that reaches a port no process has bound goes to no application; the host may answer with an Internet Control Message Protocol (ICMP) port unreachable message, and a firewall that discards it leaves the sender waiting for a reply that never comes.

---

Flashcards for this section are as follows:

- real-time traffic: why does voice and video chat tolerate a dropped packet? ::@:: The moment it described has passed, so a retransmission would arrive too late to be used.
- building on UDP: why would an application start from UDP rather than TCP? ::@:: It can then implement its own reliability, ordering, and pacing, as QUIC does.
- unreachable port: what happens to a datagram that arrives at a port no process has bound? ::@:: It reaches no application; the host may answer with an Internet Control Message Protocol (ICMP) port unreachable message.
- voice packetization: how much audio does a Voice over IP (VoIP) call send per packet, and how is a lost packet covered? ::@:: 20 ms of audio per packet, and the receiver rebuilds the gap from the samples on either side instead of retransmitting.
- a discarding firewall: what does a firewall that discards a datagram leave the sender doing? ::@:: Waiting for a reply that never comes, since no application receives the datagram and no Internet Control Message Protocol (ICMP) port unreachable message returns.

## uses

The Domain Name System (DNS) and the Dynamic Host Configuration Protocol (DHCP) run on UDP, since each exchange is one small question and answer. A query for the address of `www.example.com` leaves the client as one datagram to port 53, and the answer returns in a second datagram. A host with no address yet broadcasts a datagram to 255.255.255.255, and the offer comes back to port 68. The DHCP exchange takes four datagrams: a discover broadcast, an offer, a request, and an acknowledge. A time query to port 123, the Network Time Protocol (NTP), is one datagram out and one datagram back.

---

Flashcards for this section are as follows:

- named users: which two common protocols run on the User Datagram Protocol (UDP)? ::@:: The Domain Name System (DNS) and the Dynamic Host Configuration Protocol (DHCP).
- name service query: which port does a Domain Name System (DNS) query for `www.example.com` go to? ::@:: Port 53, and the answer returns to the client in a second datagram.
- DHCP exchange: how many datagrams does a Dynamic Host Configuration Protocol (DHCP) exchange take, and what are they? ::@:: Four: a discover broadcast, an offer, a request, and an acknowledge.
- DHCP broadcast: which address does a host with no address send its Dynamic Host Configuration Protocol (DHCP) discover to, and which port does the offer return to? ::@:: The broadcast address 255.255.255.255, with the offer returning to port 68.
- time service: which port does a Network Time Protocol (NTP) query use, and how many datagrams does the exchange take? ::@:: Port 123, one datagram out and one datagram back.
