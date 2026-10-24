---
aliases:
  - ELEC 3120 IP address
  - ELEC3120 IP address
  - HKUST ELEC 3120 IP address
  - HKUST ELEC3120 IP address
  - IP address
  - IPv4 address
  - IPv6 address
  - Internet Protocol address
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/IP_address
  - language/in/English
---

# IP address

An Internet Protocol address names a host on an internetwork. Each network may address its own machines however it likes, but a packet crossing between them has to carry an address the whole internetwork understands. The protocol supplies that common form and no other detail of the host.

---

Flashcards for this section are as follows:

- IP address: what does an Internet Protocol (IP) address identify? ::@:: A host on the internetwork.
- why a common form is needed: what does an internetwork need before its member networks can exchange packets? ::@:: An address for each host that means the same thing on every network.
- what the address does not say: which part of a host does an Internet Protocol (IP) address not identify? ::@:: The application process; the port number identifies that.

<!-- check: ignore-next-line[header_style]: IPv4 is a protocol name -->
## IPv4

The fourth version of the protocol numbers hosts with a 32-bit address, written as four decimal octets separated by dots, such as `128.2.42.10`. Each octet holds 8 bits, so its decimal runs from 0 to 255, and the whole space holds $2^{32} = 4{,}294{,}967{,}296$ addresses, a little over four billion.

Under the classful allocation that predates the current one, the leading octet gives the address its shape. A first octet from 1 to 126 gave class A with a default mask of /8, 128 to 191 gave class B with a default mask of /16, and 192 to 223 gave class C with a default mask of /24. The mask length sets how much of the address belongs to the network, so a class A block holds $2^{24} = 16{,}777{,}216$ addresses, a class B block $2^{16} = 65{,}536$, and a class C block $2^8 = 256$.

A first octet from 224 to 239 marks a multicast group, and 224.0.0.1 reaches every host on the local link. A first octet of 127 marks the loopback address 127.0.0.1, which means the host itself, and 255.255.255.255 reaches every host of the local network.

Three blocks are reserved for private use and are never routed on the public Internet: 10.0.0.0/8, 172.16.0.0/12 and 192.168.0.0/16. They hold $2^{24} + 2^{20} + 2^{16} = 16{,}777{,}216 + 1{,}048{,}576 + 65{,}536 = 17{,}891{,}328$ addresses, about one address in every 240 of the space. A home router uses an address in one of them and rewrites the source address of the packets it forwards, so the private address never appears on the public Internet.

---

Flashcards for this section are as follows:

- IPv4 size: how many bits does an Internet Protocol version 4 address have? ::@:: 32 bits.
- IPv4 notation: how is an Internet Protocol version 4 address written? ::@:: Four decimal octets separated by dots, such as `128.2.42.10`.
- an octet: an octet holds $8$ bits; which decimals does that allow? ::@:: $2^8 = 256$ values, running 0 to 255.
- size of the space: an address field is $32$ bits wide; how many addresses does that hold? ::@:: $2^{32} = 4{,}294{,}967{,}296$, a little over four billion.
- classful first octets: which first-octet ranges gave classes A, B and C, and which mask did each carry? ::@:: 1 to 126 for class A at /8, 128 to 191 for class B at /16, and 192 to 223 for class C at /24.
- class sizes: a class A block has a $/8$ mask, a class B one $/16$ and a class C one $/24$; how many addresses does each hold? ::@:: $2^{24} = 16{,}777{,}216$, $2^{16} = 65{,}536$, and $2^8 = 256$.
- multicast: which first-octet range marks a multicast group, and which address reaches every host on the local link? ::@:: 224 to 239, with 224.0.0.1 reaching every host of the local link.
- loopback: which addresses mean the host itself, and which one is used? ::@:: The 127 block, of which 127.0.0.1 is the usual one.
- private blocks: which three Internet Protocol version 4 blocks are reserved for private networks? ::@:: 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16.
- private space size: the three private blocks are $/8$, $/12$ and $/16$; how many addresses do they hold together? ::@:: $2^{24} + 2^{20} + 2^{16} = 16{,}777{,}216 + 1{,}048{,}576 + 65{,}536 = 17{,}891{,}328$.
- limited broadcast: which Internet Protocol version 4 address reaches every host of the local network? ::@:: 255.255.255.255.

## masks

The mask is a second 32-bit number that says where the network part of an address ends. It is written either as an address of its own, 255.255.255.192, or as the number of leading 1 bits, /26.

The mask is a run of 1 bits followed by a run of 0 bits, never a mixture: a 1 bit marks the network, a 0 bit the host. Bitwise and-ing an address with its mask clears the host bits and leaves the network address, which is the address of the whole block:

| step | value |
| --- | --- |
| address | `11000000.10101000.00000001.10000010` = 192.168.1.130 |
| mask /26 | `11111111.11111111.11111111.11000000` = 255.255.255.192 |
| address and mask | `11000000.10101000.00000001.10000000` = 192.168.1.128 |

The block that mask carves out holds $2^{32-n}$ addresses for a prefix of length $n$, so /24 gives $2^8 = 256$, /26 gives $2^6 = 64$, and /27 gives $2^5 = 32$. Two of the addresses in a block are spoken for, the network address itself and the broadcast address that reaches every host in it, so /24 offers 254 usable hosts and /26 offers 62. A /31 on a point-to-point link is the exception, with two usable ends, and a /32 is a single host.

Splitting a block means borrowing bits from the host part. A /24 block of 256 addresses split into /27s borrows three bits, so it yields $2^3 = 8$ subnets of $2^{32-27} = 32$ addresses each, 30 of them usable, starting at .0, .32, .64 and so on.

The mask also decides whether the destination is reachable directly. A host ands its own address with its mask and the destination with the same mask. Equal results put both on one subnet, and the host sends the frame straight to the destination; different results mean the destination is elsewhere, so the frame goes to the gateway instead. A host at 192.168.1.130/26 reaches 192.168.1.150 directly, since both fall in 192.168.1.128/26, and sends to the gateway for 192.168.1.200, which falls in 192.168.1.192/26.

A router may hold several masks that match one destination, and the longest wins: 192.168.1.0/24 beats 192.168.0.0/16 for 192.168.1.5, because its block is smaller. The masks have to be contiguous for that to work at all, so 255.0.255.0 is not a prefix and cannot be written as /n.

---

Flashcards for this section are as follows:

- mask: what does the mask of an Internet Protocol version 4 (IPv4) address say? ::@:: Where the network part of the address ends and the host part begins.
- two forms: which two forms name the mask /26? ::@:: 255.255.255.192 and /26, the number of leading 1 bits.
- mask shape: which bit patterns can a mask hold? ::@:: A run of 1 bits followed by a run of 0 bits, never a 0 between 1s.
- and-ing: how does a host find the network address of a block? ::@:: By and-ing the address with its mask, which clears the host bits.
- worked mask: which network address does $192.168.1.130$ fall in under the mask $255.255.255.192$, and why? ::@:: $192.168.1.128$, because the last octet $130$ is `10000010` and the mask keeps the top two bits `10`, worth $2 \times 64 = 128$.
- block size: a prefix of length $n$ covers how many addresses? ::@:: $2^{32-n}$; a $/26$ leaves $32 - 26 = 6$ host bits, so $2^6 = 64$ addresses.
- usable hosts: how many usable hosts do a $/24$ block and a $/26$ block offer? ::@:: $2^8 - 2 = 256 - 2 = 254$ and $2^6 - 2 = 64 - 2 = 62$, since the network address and the broadcast address are taken in each.
- subnet arithmetic: a $/24$ block is split into blocks of $/27$; how many subnets does that give, and how many addresses each? ::@:: $2^3 = 8$ subnets of $2^5 = 32$ addresses, $32 - 2 = 30$ usable.
- on-link decision: how does a host decide whether a destination is on its own subnet? ::@:: It ands both its own address and the destination with its mask; equal results mean on-link, unequal mean the gateway.
- worked on-link: a host is 192.168.1.130/26; is 192.168.1.150 on its subnet, and is 192.168.1.200? ::@:: 192.168.1.150 is, since both are in 192.168.1.128/26; 192.168.1.200 is not, since it is in 192.168.1.192/26.
- longest prefix: a router holds 192.168.0.0/16 and 192.168.1.0/24 and a packet names 192.168.1.5; which route wins? ::@:: The /24, because the longer prefix is the more specific match.
- binary mask: how is the $/26$ mask written as four binary octets, and which dotted decimal is that? ::@:: `11111111.11111111.11111111.11000000`, which is 255.255.255.192.
- point-to-point and single host: how many usable ends do a $/31$ and a $/32$ offer? ::@:: A $/31$ on a point-to-point link has two usable ends, and a $/32$ is a single host.

<!-- check: ignore-next-line[header_style]: IPv6 is a protocol name -->
## IPv6

The sixth version uses 128 bits, written as eight groups of four hexadecimal digits separated by colons, such as `2001:0db8:85a3:0000:0000:8a2e:0370:7334`. Each group is 16 bits and each hex digit is 4. The space holds $2^{128} \approx 3.4 \times 10^{38}$ addresses, which is $2^{96}$ times the Internet Protocol version 4 space.

The full form is rarely written, because three rules shorten it and they are applied in order. The first rule drops leading zeros inside each group: `0db8` becomes `db8`, `0000` becomes `0`, and `0370` becomes `370`, giving `2001:db8:85a3:0:0:8a2e:370:7334`. The second rule replaces the longest run of consecutive all-zero groups with a double colon, so the two zero groups collapse and the address reads `2001:db8:85a3::8a2e:370:7334`. The third rule writes the letters in lowercase.

The loopback address comes out of the same rules. Its full form is `0000:0000:0000:0000:0000:0000:0000:0001`, which the first rule reduces to `0:0:0:0:0:0:0:1`, and the second rule then collapses the seven zero groups to `::`, leaving `::1`. The address with no group set at all is `::`, the unspecified address that a host uses before it has one.

Only one double colon may appear in an address. A second one would leave the reader unable to tell how many groups each stands for, so `1::2::3` is not an address. A run of one zero group stays written out, since the shortening rules cover only a run of two or more, and when two runs are equally long the first is the one collapsed. The last 32 bits may also be written as a dotted quad, which is how an Internet Protocol version 4 address is carried inside one: `::ffff:192.0.2.1`.

A prefix length works as it does in the fourth version, and /64 is the usual one for a subnet, since the low 64 bits are the interface identifier, taken from the hardware address or generated at random. One /64 therefore holds $2^{64} \approx 1.8 \times 10^{19}$ addresses. The `fe80::/10` prefix marks a link-local address, which reaches only the local link and is present on every interface.

Roughly two in five Internet users reach the network over it.

---

Flashcards for this section are as follows:

- IPv6 size: how many bits does an Internet Protocol version 6 address have? ::@:: 128 bits.
- IPv6 notation: how is an Internet Protocol version 6 address written? ::@:: Eight groups of four hexadecimal digits separated by colons.
- bits per group: one colon-separated group holds four hex digits of $4$ bits each; how many bits does the group hold? ::@:: $4 \times 4 = 16$ bits.
- size of the space: an address field is $128$ bits wide; how many addresses does that hold? ::@:: $2^{128} \approx 3.4 \times 10^{38}$, which is $2^{128-32} = 2^{96}$ times the Internet Protocol version 4 space.
- first rule: what does the first shortening rule of Internet Protocol version 6 do to each group? ::@:: It drops leading zeros inside the group, so `0db8` becomes `db8` and `0000` becomes `0`.
- second rule: what does the second shortening rule replace, and with what? ::@:: The longest run of consecutive all-zero groups, replaced by a double colon.
- shortened form: how may the Internet Protocol version 6 address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 be written in full shortened form? ::@:: `2001:db8:85a3::8a2e:370:7334`.
- loopback: which full form does the loopback address `::1` come from, and which rule leaves one group? ::@:: `0000:0000:0000:0000:0000:0000:0000:0001`, where the seven zero groups collapse to `::` and the final `0001` becomes `1`.
- unspecified address: which Internet Protocol version 6 address means no address at all? ::@:: `::`, the all-zero address.
- one double colon: why may an address not hold two double colons? ::@:: The reader could not tell how many zero groups each stands for, so `1::2::3` is not an address.
- embedded IPv4: how is an Internet Protocol version 4 address carried inside an Internet Protocol version 6 one? ::@:: As a dotted quad in the last 32 bits, such as `::ffff:192.0.2.1`.
- subnet prefix: a $/64$ prefix leaves which number of addresses for hosts, and why is that the usual choice? ::@:: $128 - 64 = 64$ host bits, so $2^{64} \approx 1.8 \times 10^{19}$, since the low 64 bits are the interface identifier.
- link-local: which prefix marks a link-local Internet Protocol version 6 address, and where does that address reach? ::@:: `fe80::/10`, which reaches only the local link.
- one zero group: what happens to a run of exactly one all-zero group? ::@:: It stays written as `0`, since the double colon covers a run of two or more.
- interface identifier: which bits of an Internet Protocol version 6 address form the interface identifier, and where do they come from? ::@:: The low 64 bits, taken from the hardware address or generated at random.

## obtaining an address

A host does not usually keep a fixed address. It asks the network for one when it joins, and the Dynamic Host Configuration Protocol (DHCP) hands out the address together with the gateway and the address of a local name server.

The exchange takes four steps. The host broadcasts a discover message, the server offers one address, the host requests that address, and the server acknowledges it. The acknowledgement carries the address and the settings, and the host installs a default route through the gateway, so packets for another network leave by it.

---

Flashcards for this section are as follows:

- how a host gets an address: which protocol gives a joining host its Internet Protocol (IP) address? ::@:: The Dynamic Host Configuration Protocol (DHCP).
- what else DHCP supplies: which two other settings does the Dynamic Host Configuration Protocol (DHCP) hand out with the address? ::@:: The gateway and the address of a local name server.
- why not fixed: why is a fixed address unusual for an ordinary host? ::@:: It asks the network for one on joining, so the network can reuse addresses as machines come and go.
- the four messages: which four messages does the Dynamic Host Configuration Protocol (DHCP) exchange use? ::@:: Discover, Offer, Request, and Acknowledge.
