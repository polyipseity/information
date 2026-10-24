---
aliases:
  - ELEC 3120 transport layer
  - ELEC3120 transport layer
  - HKUST ELEC 3120 transport layer
  - HKUST ELEC3120 transport layer
  - end-to-end layer
  - layer 4
  - transport layer
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/transport_layer
  - language/in/English
---

# transport layer

The network layer delivers data from one host to another. A host runs many applications at once, so each packet needs an owner: the process that should read it. The transport layer supplies that owner, and on request adds what the network leaves out, such as reliable in-order delivery and pacing. It runs on the two end hosts only; routers between them forward packets at the network layer and below. The destination port keeps a browser and a mail client on one laptop from reading each other's packets: a browser reaches a web server on port 443, a mail client reaches a mail server on port 25, and each reply returns to the port its sender holds.

---

Flashcards for this section are as follows:

- transport layer: what does the transport layer add over the network layer? ::@:: A way to address application processes instead of hosts, and optionally reliable, in-order, and paced delivery.
- where does the transport layer run? ::@:: On the two end hosts only; routers between them stop at the network layer.
- web and mail ports: which destination port does a web browser use to reach a web server, and a mail client to reach a mail server? ::@:: Port 443 for the web server and port 25 for the mail server.

## limits of the network layer

The network layer promises best-effort delivery and nothing more. A packet can be corrupted, delayed, dropped, reordered, or duplicated on the way, and the layer says nothing about how fast to send. A router whose output queue fills during a burst drops the excess packets, and the sender learns of a loss only when an acknowledgement fails to arrive. Two packets sent one after the other can reach the receiver in the opposite order when one of them takes a shorter path, and a packet forwarded twice leaves the receiver holding two copies of the same data. Each application would otherwise repeat the same recovery code, so the transport layer carries it once for all of them.

---

Flashcards for this section are as follows:

- network layer promise: what delivery does the network layer guarantee? ::@:: Best-effort delivery between hosts, with no guarantee about corruption, delay, loss, ordering, or duplicates.
- why not leave recovery to applications? ::@:: Every application would repeat the same code, so the transport layer carries it once for all of them.
- reordering: how can two packets sent in order reach the receiver in the opposite order? ::@:: One of them takes a shorter path through the network and arrives first.
- rate guidance: does the network layer say how fast a sender should send? ::@:: No; it gives no rate guidance at all, so pacing is left to the transport layer.
- loss from a burst: what happens to packets that arrive while a router's output queue is full, and how does the sender learn of the loss? ::@:: The router drops the excess packets, and the sender learns only when an acknowledgement fails to arrive.
- duplication: how can one packet reach the receiver twice? ::@:: The network forwards it twice, so the receiver holds two copies of the same data.

## multiplexing and demultiplexing

One host runs a browser, a mail client, a file transfer, and a media player over one network interface. Demultiplexing hands each arriving packet to the process it belongs to; multiplexing marks each outgoing packet for the process that sent it. Both work by port number. A lookup of `www.example.com` yields an Internet Protocol (IP) address for the network layer to route and a port number for the transport layer to deliver to a process. The browser then opens a connection to port 443, and the destination host hands the arriving segments to the process bound to that port. A datagram that reaches a port no process has bound goes to no application; the host may answer with an Internet Control Message Protocol (ICMP) port unreachable message, and a firewall that discards it leaves the sender waiting for a reply that never comes.

---

Flashcards for this section are as follows:

- demultiplexing: what does the receiving host do with an arriving packet? ::@:: It hands the packet to the application process it belongs to.
- multiplexing: what does the sending host do with outgoing data? ::@:: It marks each packet with the process that sent it and sends it out through the shared interface.
- unbound port: what happens to a datagram that arrives at a port no process has bound? ::@:: It reaches no application; the host may answer with an Internet Control Message Protocol (ICMP) port unreachable message.
- address from a name: resolving a host name such as `www.example.com` yields an Internet Protocol (IP) address as well as a port number; what does the network layer do with the address? ::@:: It routes the packet to the destination host, where the transport layer uses the port to pick the process.
- discarded unreachable: a firewall discards the Internet Control Message Protocol (ICMP) port unreachable message from the destination host; what does the sender observe? ::@:: Nothing; it keeps waiting for a reply that never comes.

### ports

A port is a number, not a piece of hardware. The destination port in the packet header names the process that should receive the data. The Internet Assigned Numbers Authority (IANA) splits the 16-bit port space into three ranges. Well-known ports 0 to 1023 carry the services everyone agrees on, such as 22 for the Secure Shell Protocol (SSH) and 53 for the Domain Name System (DNS). Registered ports 1024 to 49151 are held by particular applications, such as port 5060 for the Session Initiation Protocol (SIP), and dynamic ports 49152 to 65535 are the ones a host hands out to its own outgoing connections. A well-known port names the process on the server, so the browser on the laptop takes a number from the dynamic range for its own side of the connection. RFC 6335 (2011) records the split.

The boundaries are powers of two, which is why they fall at 1023 and 49151 rather than at round decimals. A 16-bit field holds $2^{16} = 65{,}536$ numbers. The well-known range takes the first $2^{10} = 1024$, which is $1/64$ of the space, or $1.5625\%$. The dynamic range takes the last $2^{14} = 16{,}384$, which is $16{,}384/65{,}536 = 1/4$, so ports $0$ to $49{,}151$ are exactly the other $75\%$: $49{,}152 = 3 \times 16{,}384$. The registered range is what remains between them, $49{,}152 - 1024 = 48{,}128$ numbers, which is $47$ blocks of $1024$.

The quarter given to dynamic ports is a budget on how many connections one host can have open at once. Each outbound connection takes one port from that range, so one source address supports $16{,}384$ connections to any combination of destinations. A proxy opening $20{,}000$ connections to one server runs out after $16{,}384$ and has to add a second source address, since the server tells the connections apart by the source address and port together. A connection also keeps its port for a while after it closes, so the budget is spent per unit time: over the $240\text{ s}$ a closed connection lingers, $16{,}384/240 \approx 68$ new connections per second is the ceiling on one address.

---

Flashcards for this section are as follows:

- port: what is a port? ::@:: A number the host uses to route arriving data to an application process, not a physical device.
- which field names the recipient? ::@:: The destination port in the transport header.
- port ranges: which three ranges does the Internet Assigned Numbers Authority (IANA) split the port space into? ::@:: Well-known ports 0 to 1023, registered ports 1024 to 49151, and dynamic ports 49152 to 65535.
- size of the port space: a port field is $16$ bits wide; how many port numbers does that give? ::@:: $2^{16} = 65{,}536$ numbers.
- why 1023: why does the well-known range end at $1023$ rather than at a round decimal? ::@:: The first $2^{10} = 1024$ numbers: $1024/65{,}536 = 1/64 = 1.5625\%$ of the space.
- why 49151: why does the registered range end at $49{,}151$? ::@:: The last $2^{14} = 16{,}384$ numbers go to the dynamic range, so it starts at $65{,}536 - 16{,}384 = 49{,}152 = 3 \times 16{,}384$, and the $3/4 = 75\%$ below it is registered.
- size of the registered range: the registered range runs from $1024$ to $49{,}151$; how many numbers does it hold, and how does that divide? ::@:: $49{,}152 - 1024 = 48{,}128$, and $48{,}128/1024 = 47$ blocks of $1024$.
- port exhaustion: a host has one source address and $16{,}384$ dynamic ports; how many simultaneous connections to the same server can it open? ::@:: $16{,}384$, so a $20{,}000$-connection proxy falls $20{,}000 - 16{,}384 = 3{,}616$ short and needs a second source address.
- rate of new connections: a closed connection holds its port for $240\text{ s}$ and one address has $16{,}384$ dynamic ports; what is the ceiling on new connections per second? ::@:: $16{,}384/240 \approx 68$ per second.
- SSH and DNS ports: which well-known ports carry the Secure Shell Protocol (SSH) and the Domain Name System (DNS)? ::@:: Port 22 for the Secure Shell Protocol (SSH) and port 53 for the Domain Name System (DNS).
- SIP port: which registered port does the Session Initiation Protocol (SIP) use? ::@:: Port 5060.
- split record: which Request for Comments (RFC) document records the three-range split of the port space, and in which year? ::@:: RFC 6335, in 2011.

## sockets

An application reaches the transport layer through a socket, opened with a type and then used with `sendto` and `recvfrom`. The type selects the protocol: `SOCK_DGRAM` for a User Datagram Protocol (UDP) socket and `SOCK_STREAM` for a Transmission Control Protocol (TCP) socket. A read on a stream socket blocks until at least one byte arrives, and then returns however many bytes have come in; a read on a datagram socket blocks until a whole datagram arrives, and returns that one datagram whole. A program that asks a stream socket for 100 bytes gets the 40 that have arrived and reads the rest on the next call, while a datagram socket hands back one whole datagram of 1000 bytes or nothing at all. A DNS query leaves the host as one datagram to port 53 and comes back to the same socket.

---

Flashcards for this section are as follows:

- socket: what is a socket? ::@:: The software abstraction through which an application process exchanges network messages with the transport layer inside the operating system.
- socket type: which socket type selects the User Datagram Protocol (UDP), and which selects the Transmission Control Protocol (TCP)? ::@:: `SOCK_DGRAM` for UDP and `SOCK_STREAM` for TCP.
- socket calls: which call sends a message, and which receives one? ::@:: `sendto` sends and `recvfrom` receives.
- blocking read: what does a read on a stream socket do when no byte has arrived yet? ::@:: It blocks until at least one byte arrives, and then returns however many bytes have come in.
- datagram read: what does a read on a datagram socket do when no datagram has arrived? ::@:: It blocks until a whole datagram arrives, and then returns that one datagram whole.
- DNS datagram: how does a Domain Name System (DNS) query leave the host and come back? ::@:: As one User Datagram Protocol (UDP) datagram to port 53, with the reply arriving at the same socket.

## service model

Two services matter most: reliable, in-order delivery of the bytes, and pacing that sends fast enough to fill the path without overwhelming the network. TCP offers both and promises nothing about delay or bandwidth; UDP offers neither. A file transfer wants the path kept full, while a voice call wants each sample to arrive before the conversation moves on. The receiver advertises a window that says how many bytes it can still take, and the sender may not keep more bytes in flight than that window allows. When the receiver's buffer fills, the window falls to zero and the sender waits until the receiver has read enough to make room.

---

Flashcards for this section are as follows:

- pacing: which two ways can pacing go wrong? ::@:: Sending too fast overloads the network, and sending too slowly wastes it.
- what TCP leaves open: which two quantities does TCP not guarantee? ::@:: Delay and bandwidth.
- full receiver buffer: what does a sender do when the window the receiver advertises falls to zero? ::@:: It stops sending until the receiver's buffer has room again.
- UDP service: which of the two transport services does the User Datagram Protocol (UDP) offer? ::@:: Neither reliable in-order delivery nor pacing.
- file transfer and voice call: which pacing does a file transfer want, and which does a voice call want? ::@:: A file transfer wants the path kept full, and a voice call wants each sample to arrive before the conversation moves on.

## protocol family

TCP and UDP carry almost all Internet traffic. A few others serve narrower needs, among them the Stream Control Transmission Protocol (SCTP) and the Datagram Congestion Control Protocol (DCCP). SCTP keeps message boundaries inside a reliable transport, so a signaling message and a data payload stay apart where a TCP byte stream would merge them. DCCP adds congestion control to a datagram service.

---

Flashcards for this section are as follows:

- common transport protocols: which two transport protocols carry almost all Internet traffic? ::@:: The Transmission Control Protocol (TCP) and the User Datagram Protocol (UDP).
- other transport protocols: which two transport protocols besides TCP and UDP exist for narrower needs? ::@:: The Stream Control Transmission Protocol (SCTP) and the Datagram Congestion Control Protocol (DCCP).
- SCTP message boundaries: what does the Stream Control Transmission Protocol (SCTP) preserve that a Transmission Control Protocol (TCP) byte stream would merge? ::@:: Message boundaries, so a signaling message and a data payload stay apart inside a reliable transport.
- DCCP: what does the Datagram Congestion Control Protocol (DCCP) add to a datagram service? ::@:: Congestion control.
