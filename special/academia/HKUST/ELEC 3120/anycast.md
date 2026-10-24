---
aliases:
  - ELEC 3120 anycast
  - ELEC3120 anycast
  - HKUST ELEC 3120 anycast
  - HKUST ELEC3120 anycast
  - anycast
  - anycasting
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/anycast
  - language/in/English
---

# anycast

Anycast puts the same address on several machines and lets the network decide which one serves a packet. The copies can be spread across the world.

---

Flashcards for this section are as follows:

- anycast: what does anycast do with one address? ::@:: It assigns the address to several machines, so a packet reaches whichever is nearest.
- the deciding party: who chooses which copy serves a packet? ::@:: The network, since each router forwards along the shortest path to the shared address.
- what it needs from routing: how much does anycast change the routing protocols? ::@:: Nothing; they already forward toward the nearest instance of an address.

## mechanism

Routing seeks the shortest path to a destination address. When several machines advertise that address, the shortest path ends at the nearest of them.

Each copy advertises the same prefix, so a router holds one entry for the shared address, with a path to each copy, and it chooses between those paths by its own metrics, which usually means the nearest instance. A flow's path is chosen the same way, packet by packet, so two packets of one connection can leave by different routes and reach different copies if the route changes between them. The reply leaves from the copy that received the request, so the path back can be a different length from the path out.

A content delivery network uses anycast for its entry point. It announces one address from every city it serves, so a client opens a connection to the nearest point of presence and the network carries the request there, rather than to a site the client chose.

---

Flashcards for this section are as follows:

- the gain: which two things does serving from the nearest copy improve? ::@:: The delay of the trip and the load on any one machine.
- advertising: what does each machine hold for anycast to work? ::@:: The same address, advertised into the routing system.
- routing table: how many routing table entries does a set of $n$ anycast copies of one address produce? ::@:: $n$ copies announce $1$ shared prefix, so each router holds $1$ entry for it, with a path to each of the $n$ copies: $1$ entry, not $n$.
- path choice: how does a router choose between the paths to several anycast copies of one address? ::@:: By its own metrics, which usually select the nearest copy.
- the return path: where does a reply leave from when a request reaches one of several anycast copies? ::@:: From the copy that received the request, so the return path can be a different length from the path out.
- who picks the site: under a content delivery network entry point, which site does the client choose? ::@:: None; the client opens a connection to the nearest point of presence and the network carries the request to that copy.

## root servers

The root servers use anycast. Each of the thirteen identities is replicated across many locations, so a query reaches a nearby copy and a failed copy costs nothing. The `a-root-servers.net` identity answers at `198.41.0.4` from every location that hosts a copy of it, and the root system runs more than a thousand instances of the thirteen identities.

Before anycast, each identity stood at one fixed place on the map, and a letter marked a particular machine. Anycast turned each of those fixed places into a set of sites that answer for the same identity, so the letter no longer picks out one server. <p> ![world map of the Domain Name System (DNS) root servers before anycast, with the letters A to M marking the thirteen locations each root server then had](../../../../archives/Wikimedia%20Commons/Root-historic.svg)

---

Flashcards for this section are as follows:

- the root: how are the thirteen root server identities spread across the world? ::@:: Each identity is replicated at many locations, so queries reach a nearby copy.
- root server address: at which address does the `a-root-servers.net` identity answer from every location that hosts a copy? ::@:: At `198.41.0.4`.
- root servers before anycast: what does the map of the root system before anycast show? <p> ![world map of the Domain Name System (DNS) root servers before anycast, with the letters A to M marking the thirteen locations each root server then had](../../../../archives/Wikimedia%20Commons/Root-historic.svg) ::@:: Thirteen letters, one for each root server identity, each standing at a single fixed place.
- draw the root map before anycast: what does it show, and what did anycast change? ::@:: A world map with the letters A to M, one for each of the thirteen root server identities, each at a single fixed location; anycast replaced each fixed location with a set of sites that answer for the same identity.
- count of instances: how many instances of the thirteen root server identities does the root system run? ::@:: More than a thousand instances of the thirteen identities.

## trade-offs

A service reached by anycast keeps no state that only one instance holds. A shop that holds a customer's basket in the memory of one server loses it when the next request lands on another copy, so the state has to sit somewhere both copies can reach.

---

Flashcards for this section are as follows:

- route changes: what happens to a connection when the route to a shared address changes? ::@:: Later packets may reach a different copy of the service.
- what a service must not rely on: what kind of state is unsafe for a service reached by anycast? ::@:: State held on only one instance, since the next packet may arrive at another.
- the reason: why does anycast pick a copy per packet rather than once per connection? ::@:: The choice is a by-product of routing, which the end hosts do not control and which can change.
- where shared state lives: where must the state sit for a service reached by anycast? ::@:: Somewhere every copy can reach, so whichever copy receives the next request can read it.
