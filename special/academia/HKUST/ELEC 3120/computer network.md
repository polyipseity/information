---
aliases:
  - ELEC 3120 computer network
  - ELEC3120 computer network
  - HKUST ELEC 3120 computer network
  - HKUST ELEC3120 computer network
  - computer network
  - internetwork
  - network
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/computer_network
  - language/in/English
---

# computer network

A network is two or more endpoints joined by a communication medium. Joining two or more networks gives an internetwork, and the Internet is the largest one. A laptop and a printer joined by a single cable make a network of two endpoints.

---

Flashcards for this section are as follows:

- network: what is a network made of? ::@:: Two or more endpoints joined by a communication medium.
- internetwork: what does joining two or more networks give? ::@:: An internetwork.
- deployments: which deployments of networks are in use? ::@:: Datacenters, enterprise and university campuses, cellular networks, provider access networks, content delivery networks, vehicle and industrial controller networks, and low Earth orbit satellite constellations.
- largest internetwork: which internetwork is the largest? ::@:: The Internet.
- two-endpoint network: what network do a laptop and a printer joined by a single cable form? ::@:: A network of two endpoints.

## parts of a network

Endpoints are the devices that send and receive: workstations, servers, and printers. A hub or switch joins them on a segment, and the transmission medium carries the signals.

The shape of a network decides what those three parts look like. A home network is a small wireless local area network around a router, with a laptop and a phone as endpoints and a fibre or cable link to the provider. A campus network joins thousands of endpoints through switched Ethernet, with a wireless network alongside it for portable devices. A datacentre network is built from racks of servers joined by short high-speed links, and its traffic runs in tens of gigabits per second. A cellular network has no cable reaching the user at all: devices attach by radio to base stations, which hand their traffic to a core network that connects them to the rest of the Internet. A satellite constellation is the same arrangement with the base stations in orbit, which adds a long propagation delay to every packet. An ad hoc network has no fixed infrastructure at all, and the endpoints relay for each other, which is what a mesh of wearable devices or a group of vehicles in the same area forms. Overlays run over other networks instead of replacing them, so a virtual private network carries private traffic across the public Internet.

Real networks take these shapes in practice. A hospital puts bedside monitors and infusion pumps on a wired segment and staff phones on a wireless one. A factory floor hangs its sensors off a controller over a fieldbus, a wired bus that carries its readings on a fixed cycle. A shop's point-of-sale terminals share a small wired segment behind the counter. A university laboratory keeps its instruments on wired Ethernet beside the workstations that log their readings. A car runs a controller area network (CAN) bus with nodes for the engine, the brakes and the airbag, at up to 1 Mbit/s over 40 m of twisted pair. A bank's branch office runs a server for its tellers and reaches the head office over a leased line. An Internet service provider gives each customer a router, and a digital subscriber line access multiplexer (DSLAM) in the exchange aggregates hundreds of customer lines onto one uplink. A content delivery network keeps copies of the same site in several cities and answers each client from the nearest one.

---

Flashcards for this section are as follows:

- endpoints: which devices are the endpoints of a small wired network? ::@:: Workstations, servers, and printers.
- segment: what joins the endpoints on one segment? ::@:: A hub or switch.
- what are the three parts of a small wired network? ::@:: Endpoints, a joining device, and the transmission medium.
- vehicle network: which bus joins the engine, brakes and airbag controllers in a car? ::@:: A controller area network (CAN) bus, which carries messages at up to 1 Mbit/s over 40 m of twisted pair.
- access network: what does a digital subscriber line access multiplexer (DSLAM) in an Internet service provider's exchange do? ::@:: It aggregates hundreds of customer lines onto one uplink.
- transmission medium: what carries the signals that the endpoints of a segment exchange? ::@:: The transmission medium.
- network shape: what does the shape of a network decide? ::@:: What each of its three parts, the endpoints, the joining device and the transmission medium, looks like.
- home network: which parts make up a home network? ::@:: A small wireless local area network around a router, with a laptop and a phone as endpoints and a fibre or cable link to the Internet service provider.
- campus network: how is a campus network built? ::@:: Thousands of endpoints joined through switched Ethernet, with a wireless local area network alongside for portable devices.
- datacentre network: how is a datacentre network built, and at what rate does its traffic run? ::@:: Racks of servers joined by short high-speed links, with traffic running in tens of gigabits per second.
- cellular network: how does a device on a cellular network reach the rest of the Internet? ::@:: It attaches by radio to a base station, which hands its traffic to a core network that connects it to the rest of the Internet.
- satellite constellation: what does moving the base stations of a cellular network into orbit add to every packet? ::@:: A long propagation delay.
- ad hoc network: how does an ad hoc network move traffic with no fixed infrastructure? ::@:: Its endpoints relay for each other, as in a mesh of wearable devices or a group of vehicles in the same area.
- overlay network: how does an overlay such as a virtual private network relate to the networks under it? ::@:: It runs over them instead of replacing them, so a virtual private network carries private traffic across the public Internet.
- hospital network: which parts of a hospital's network are wired and which are wireless? ::@:: Bedside monitors and infusion pumps sit on a wired segment, and staff phones on a wireless one.
- fieldbus: what does the fieldbus on a factory floor do? ::@:: It is a wired bus over which a controller collects its sensors' readings on a fixed cycle.
- point-of-sale terminals: what network do a shop's point-of-sale terminals share? ::@:: A small wired segment behind the counter.
- laboratory network: how are a university laboratory's instruments networked? ::@:: On wired Ethernet beside the workstations that log their readings.
- leased line: how does a bank's branch office reach the head office? ::@:: Over a leased line, from a server that serves its tellers.
- content delivery network: how does a content delivery network answer each client? ::@:: It keeps copies of the same site in several cities and answers each client from the nearest one.

<!-- check: ignore-next-line[header_generic_article]: proper noun -->
## the Internet

The Internet is a lattice of networks, not one network. Clients and servers sit at its edges, including high-volume server farms. Local, regional, and backbone Internet service providers carry traffic between them, and backbone providers meet at exchange points. The links joining the networks include Ethernet local area networks at 10 Mbps and 100 Mbps, satellite links, and wireless local area networks.

A phone on a cellular network reaches a server held by another provider through more than one network. The packet crosses its own operator's backbone to an exchange point, where the provider hosting the server takes it over and carries it along that provider's own backbone to the server.

---

Flashcards for this section are as follows:

- what sits at the Internet's edges? ::@:: Clients and servers, including high-volume server farms.
- internet service providers: which providers carry traffic in the core of the Internet? ::@:: Local, regional, and backbone Internet service providers.
- exchange point: where do backbone Internet service providers meet? ::@:: At exchange points.
- link types: which links join the networks of an internetwork? ::@:: Ethernet local area networks at 10 Mbps and 100 Mbps, satellite links, and wireless local area networks.
- a phone's path: which parts of the network carry a packet from a phone on a cellular network to a server held by another provider? ::@:: Its own operator's backbone to an exchange point, and then the backbone of the provider that holds the server.
- lattice: is the Internet one network? ::@:: No, it is a lattice of networks that Internet service providers and exchange points join.

## interconnection challenges

Vinton Cerf and Robert Kahn listed four problems in 1974. Each network may address its hosts differently, accept a different maximum size of data, lose or corrupt data inside itself, and report status, routing, and faults in its own way. Their answer was one layer above the networks rather than a merger of them, and that layer's first job is a form of address every network can read.

Two mismatches show what a join costs. Ethernet frames carry 1500 bytes of payload, while a link running the Point-to-Point Protocol (PPP) over Ethernet (PPPoE) leaves 1492 of them, because eight bytes of each frame go to the PPPoE header, so a packet sized for the larger network is split before it crosses the smaller one. A network may also deliver packets out of order: a satellite link does so when two packets take different ground routes to the gateway, and a router that switches between two paths can reorder them too. The Internet Protocol promises neither that a packet will fit the next link nor that packets arrive in order, so the layer above has to cope with both.

---

Flashcards for this section are as follows:

- the two authors: which two people listed the problems of joining networks in 1974? ::@:: Vinton Cerf and Robert Kahn, who went on to define the Internet Protocol.
- distinct addressing: why does joining two networks raise an addressing problem? ::@:: Each network may address its hosts in its own form, so an address from one means nothing in the other.
- maximum size: what does a network's maximum data size do to traffic from another network? ::@:: A packet larger than the limit cannot be carried, so the second network has to refuse or split it.
- disrupted communication: which two faults may a network suffer inside itself? ::@:: Unrecoverable mutation of the data and missing data.
- status and routing: what does each network report in its own way? ::@:: Status information, routing, fault detection, and isolation.
- the answer: what did Vinton Cerf and Robert Kahn propose instead of merging the networks? ::@:: One layer above them, so each network keeps its own ways and still joins the internetwork.
- maximum transmission unit: how many payload bytes does a link running the Point-to-Point Protocol (PPP) over Ethernet (PPPoE) leave in a frame, against Ethernet's 1500? ::@:: 1492, because eight bytes of the frame go to the PPPoE header.
- reordering: what happens when a network delivers packets out of order? ::@:: The layer above has to restore the order, since the Internet Protocol does not promise one.
- the four problems: which four problems did Vinton Cerf and Robert Kahn list in 1974? ::@:: Each network may address its hosts differently, accept a different maximum size of data, lose or corrupt data inside itself, and report status, routing and faults in its own way.
- the layer's first job: what is the first job of the layer that Vinton Cerf and Robert Kahn put above the networks? ::@:: A form of address that every network can read.
- causes of reordering: which two conditions make a network deliver packets out of order? ::@:: Two packets taking different ground routes to a satellite gateway, and a router switching between two paths.
