---
aliases:
  - DNS
  - Domain Name System
  - ELEC 3120 Domain Name System
  - ELEC3120 Domain Name System
  - HKUST ELEC 3120 Domain Name System
  - HKUST ELEC3120 Domain Name System
  - domain name
  - domain name system
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/Domain_Name_System
  - language/in/English
---

# Domain Name System

The Domain Name System (DNS) maps human-readable names to Internet Protocol addresses. Names are easier to remember than numbers, and they hide the numbers changing, but a single list of every name stopped working once the Internet grew. A hierarchy of names, administrators, and servers replaced it, each level answering only for the names below it.

---

Flashcards for this section are as follows:

- DNS: what does the Domain Name System (DNS) map? ::@:: Human-readable names to Internet Protocol (IP) addresses.
- why names: which two benefits do names give over bare addresses? ::@:: They are easier to remember, and they can be changed without telling anyone the new address.
- the shape of the system: what replaces the single list of names and addresses? ::@:: A hierarchy of names, a hierarchy of administrations, and a hierarchy of name servers.

## names instead of numbers

`ust.hk` is easier to keep than `143.89.13.184`, and a name lets the address behind it change. For a while one institution kept the whole mapping in a text file called `hosts`, which every machine downloaded as it changed. A trimmed copy still sits at `/etc/hosts` on most systems. That list could not carry millions of names and lookups, or the constant edits, so something scalable, highly available, correct, and fast replaced it.

---

Flashcards for this section are as follows:

- the original list: how were names mapped to addresses before the Domain Name System (DNS)? ::@:: A single text file called `hosts`, downloaded from one central server whenever it changed.
- the leftover: where does a copy of that original list still sit on a modern system? ::@:: At `/etc/hosts` on Linux and `C:\Windows\System32\drivers\etc\hosts` on Windows.
- why it stopped: which four requirements did the single list fail? ::@:: Scalability, high availability, correctness, and fast lookups.

## hierarchical namespace

`www.ece.ust.hk` reads from the right: the host `www` sits in `ece`, `ece` in `ust`, and `ust` under the top-level domain `hk`, each part a subdomain of the part after it. Each node of the tree holds the names that end with the same suffix, and the suffix is the path back up to the root. Above the top-level domain the tree ends at a node with no label. The root's name is the empty string, written as one dot, and every name ends there, so `www.ece.ust.hk.` and `www.ece.ust.hk` are the same name. The dot marks a name as complete, and inside a zone file it has to be there: a name without it is relative, and the server appends the zone's origin, so `www` becomes `www.<origin>` while `www.` stays as written. Ordinary use drops it because every name would otherwise end in it, and a resolver adds it back before asking.

---

Flashcards for this section are as follows:

- reading a name: in which direction is a domain name read, and what does each part add? ::@:: From the right: each part names a subdomain of the part to its right, down to the host.
- the tree node: what does each node of the namespace hold? ::@:: The names that end with the same suffix.
- an example: in `www.ece.ust.hk`, which part is the top-level domain, and what does the leftmost part name? ::@:: `hk` is the top-level domain, and `www` names the server that runs the website.
- the root's name: what is the top of the name tree called, and why do `www.ece.ust.hk.` and `www.ece.ust.hk` name the same host? ::@:: Its label is empty, written as a single dot, and every name ends there, so the two spell the same name.
- the dot inside a zone file: what does a name ending in a dot mean in a zone file, and what happens without it? ::@:: It is complete as written; without the dot the name is relative, so the server appends the zone's origin and `www` becomes `www.<origin>`.
- why the dot is normally left out: why do URLs and ordinary writing drop the final dot? ::@:: Because every name ends in the root, so it would sit after every name, and a resolver adds it back before asking.

### top-level domains

A top-level domain is registered with the authority that manages it, usually through a registrar. Some state a country or a purpose: `.uk` for the United Kingdom, `.edu` for education, `.arpa` for infrastructure. Others are generic and open to anyone. Below that, a domain's owner creates subdomains freely: `ece.ust.hk` and `cse.ust.hk` separate two academic units, while `www` marks the machine that runs the website rather than another unit.

---

Flashcards for this section are as follows:

- top-level domain: what is the rightmost part of a domain name? ::@:: The top-level domain the name is registered under, such as `hk` or `edu`.
- registrar: who does a domain owner deal with to register a name? ::@:: A registrar acting for the authority that manages the top-level domain.
- subdomains: which two purposes do the subdomains below a registered domain serve? ::@:: Separating organisational units, such as `ece` and `cse`, and marking the role of a machine, such as `www`.
- country or purpose: which top-level domains name a country or a purpose, and which do not? ::@:: `uk` names the United Kingdom, `edu` education, and `arpa` infrastructure, while generic top-level domains are open to anyone.

## zones

A zone is one subtree of the name space, served whole by one set of authoritative name servers. Its records sit on those servers in a zone file, so each organisation can run the servers for its own part.

A domain name is one node, while a zone is a whole subtree. `ust.hk` is a name, and a zone named `ust.hk` holds `www.ust.hk` and every other node below it that has not been cut away to a child zone. <p> ![domain name tree: the root at the top, the top-level domains com, org and fr below it, then domain names such as debian and chicoree, then hosts such as www and mail, with a dashed ellipse marking the zone debian.org. and two coloured paths running from the root down to two hosts](../../../../archives/Wikimedia%20Commons/DNS%20Tree.svg)

---

Flashcards for this section are as follows:

- zone: what is a zone in the Domain Name System (DNS)? ::@:: One subtree of the name space, served whole by one set of authoritative name servers.
- name against zone: how does a domain name differ from a zone? ::@:: A name is one node of the tree, while a zone is the subtree that one set of servers answers for, cut where child zones take over.
- why zones exist: what does dividing the namespace into zones allow? ::@:: Each organisation can run the servers for its own part of the tree.
- the tree in a drawing: ![domain name tree: the root at the top, the top-level domains com, org and fr below it, then domain names such as debian and chicoree, then hosts such as www and mail, with a dashed ellipse marking the zone debian.org. and two coloured paths running from the root down to two hosts](../../../../archives/Wikimedia%20Commons/DNS%20Tree.svg) ::@:: The root at the top, the top-level domains com, org and fr below, names such as `debian` and `chicoree` under those, hosts such as `www` and `mail` at the bottom, a dashed ellipse around `debian.org.` marking one zone, and two paths from the root to two hosts.
- marking a zone on the tree: how is a zone marked on a drawing of the domain name tree? ::@:: As a dashed ellipse around the name and the nodes below it, such as `debian.org.` with the hosts under it. <p> ![domain name tree: the root at the top, the top-level domains com, org and fr below it, then domain names such as debian and chicoree, then hosts such as www and mail, with a dashed ellipse marking the zone debian.org. and two coloured paths running from the root down to two hosts](../../../../archives/Wikimedia%20Commons/DNS%20Tree.svg)

### zone cuts and delegation

Where a parent zone hands a subtree to a child zone, the parent carries `NS` records naming the child's servers, and the child carries everything below that point. The parent's operator writes the delegation, and the child's operator serves the names underneath. A new owner reaches the parent's operator through a registrar, which writes the delegation when the name is registered.

A child often runs its servers inside its own zone, as `ust.hk` does with `ns1.ust.hk`, and then the parent must also hold their addresses. A resolver that has just been referred to `ns1.ust.hk` cannot resolve that name through the child, because reaching the child needs the address it has not been given yet. The parent's copy of the address breaks that circle, and the extra address records are called glue.

---

Flashcards for this section are as follows:

- delegation: what does the parent zone hold where it hands a subtree to a child zone? ::@:: `NS` records naming the child's servers, so the parent only points downwards.
- who administers which zone: which operator writes the delegation, and which serves the names below it? ::@:: The operator of the parent zone writes the delegation, and the operator of the child zone serves the names below it.
- registrar: who writes a new owner's delegation into the parent zone? ::@:: The registrar, acting for the operator of the parent zone.
- glue: why must the parent zone hold the addresses of a child's name servers that sit inside the child zone? ::@:: Because a resolver cannot look those names up until it reaches the child, and it cannot reach the child without the addresses; the parent's copies are glue.

### root servers

Thirteen root server identities, labelled `A` to `M`, serve the root zone. One organisation runs each identity, with many machines under it, so a letter names an operator rather than a single computer. Twelve organisations run the thirteen identities between them, and one of them runs two.

Every machine of an identity announces the same address, and routers send each query to the nearest one, which is anycast routing. The map below dates from 2006 and marks 123 instances of the thirteen identities; the deployment has grown since. <p> ![world map marked with the locations of the Domain Name System (DNS) root server instances, with the letters A to M around the map naming the thirteen root servers](../../../../archives/Wikimedia%20Commons/Root-current.svg)

A resolver starts from a bootstrap list of addresses compiled into its software, the root hints, not from the Domain Name System itself.

The root zone holds only the delegations to the top-level domains, with glue for their servers, and no host records at all. It is signed with Domain Name System Security Extensions (DNSSEC), so the root's key-signing key is the trust anchor that a validating resolver starts from.

---

Flashcards for this section are as follows:

- root servers: how many root server identities are there, and how are they labelled? ::@:: Thirteen, from `A` to `M`.
- who runs them: how is one root server identity related to the machines that serve it, and how many organisations are involved? ::@:: One organisation runs each identity with many machines under it; twelve organisations run the thirteen identities between them, and one of them runs two.
- anycast: how does one root server address reach a query from anywhere? ::@:: Every machine of the identity announces the same address, and routers send the query to the nearest one, which is anycast routing.
- root hints: where does a resolver get the addresses of the root servers? ::@:: From a bootstrap list of addresses compiled into its software, named the root hints, not from the Domain Name System (DNS) itself.
- root zone contents: what does the root zone hold? ::@:: Only the delegations to the top-level domains with glue for their servers, and no host records at all.
- trust anchor: what is the trust anchor of a validating resolver? ::@:: The key-signing key of the root zone, which is signed with Domain Name System Security Extensions (DNSSEC).
- the root server map: ![world map marked with the locations of the Domain Name System (DNS) root server instances, with the letters A to M around the map naming the thirteen root servers](../../../../archives/Wikimedia%20Commons/Root-current.svg) ::@:: The places where the thirteen identities answer, 123 instances on a map dated 2006.
- drawing the root server deployment: how would a map of the root server instances be drawn, and what did the 2006 version count? ::@:: Sites spread over the world, the letters `A` to `M` labelling the thirteen identities, 123 instances in 2006. <p> ![world map marked with the locations of the Domain Name System (DNS) root server instances, with the letters A to M around the map naming the thirteen root servers](../../../../archives/Wikimedia%20Commons/Root-current.svg)

## resolution

A root server does not know the address of `potato.ece.ust.hk`. It knows which servers hold the zone below its own and returns their names instead of an address. Every server down the tree answers the same way, and only the servers authoritative for a zone return that zone's mappings.

To resolve `www.ece.ust.hk`, the resolver asks a root server, which refers it to the `.hk` servers and usually attaches their addresses as glue. It asks one of those, which refers it to the servers for `ust.hk`, and one of those refers it to the servers for `ece.ust.hk`. Those servers are authoritative for the name, so one of them returns `192.0.2.10`. <p> ![domain name hierarchy: the root at the top, then the top-level domains com, org, net and pl, then second-level names such as wikipedia and fsf, then third-level names, with the path of the name ru.wikipedia.org. traced in red from the root through org and wikipedia](../../../../archives/Wikimedia%20Commons/DNS%20schema.svg)

The client receives one address, whatever number of hops the walk took. The Dynamic Host Configuration Protocol (DHCP) supplies the resolver's address along with the client's own.

---

Flashcards for this section are as follows:

- authoritative servers: which servers hold the actual name-to-address mappings? ::@:: The authoritative servers for the zone that contains the name.
- the walk: which servers does a resolver consult in turn to find the address of `www.ece.ust.hk`? ::@:: A root server, then the `.hk` servers, then the `ust.hk` servers, then the servers authoritative for `ece.ust.hk`.
- the answer: what does the client receive from its resolver once the walk is done? ::@:: One address, whatever number of referrals the walk took.
- the address at the end: which address does a server authoritative for `ece.ust.hk` return for `www.ece.ust.hk`? ::@:: `192.0.2.10`.
- finding the resolver: how does a client learn the address of its local resolver? ::@:: The Dynamic Host Configuration Protocol (DHCP) supplies it along with the client's own address.
- the hierarchy in a drawing: ![domain name hierarchy: the root at the top, then the top-level domains com, org, net and pl, then second-level names such as wikipedia and fsf, then third-level names, with the path of the name ru.wikipedia.org. traced in red from the root through org and wikipedia](../../../../archives/Wikimedia%20Commons/DNS%20schema.svg) ::@:: The root, the top-level domains below it, second-level names such as `wikipedia` and `fsf`, third-level names below those, and one path traced in red from the root through `org` and `wikipedia` to `ru.wikipedia.org.`.
- drawing one lookup path: how is the path of one name drawn on a picture of the hierarchy? ::@:: As a line running from the root down through each label of the name, here in red from the root through `org` and `wikipedia` to `ru.wikipedia.org.`. <p> ![domain name hierarchy: the root at the top, then the top-level domains com, org, net and pl, then second-level names such as wikipedia and fsf, then third-level names, with the path of the name ru.wikipedia.org. traced in red from the root through org and wikipedia](../../../../archives/Wikimedia%20Commons/DNS%20schema.svg)

### recursion and iteration

A recursive query puts the whole job on the server: it must return the address or an error, and it walks the tree itself. An iterative query puts one step on it: the server returns the best answer it holds, usually a referral to the servers of the zone below, and whoever asked continues from there.

A client asks its local resolver, and that one query is recursive: the resolver does the walking. Authoritative servers normally refuse recursion and answer only for their own zone, so a client must ask a resolver rather than a root server.

---

Flashcards for this section are as follows:

- recursive query: what does a server promise when a query is recursive? ::@:: The final answer, an address or an error; it walks the tree itself.
- iterative query: what does a server return when a query is iterative? ::@:: The best answer it holds, usually a referral to the servers of the zone below, and the asker continues the walk.
- who recurses: which server does the walking for a client, and why not an authoritative server? ::@:: A local resolver, because authoritative servers normally refuse recursion and answer only for their own zone.
- the two queries: a client asks its local resolver, and the resolver asks the tree; which query is recursive and which iterative? ::@:: The client's query to the resolver is recursive, and the resolver's queries down the tree are iterative.

### caching

Every server caches the answers it passes on, and each answer carries a time to live that says how long it may be kept. The cache works because the top of the tree changes rarely and popular names are asked for often.

If the address of `www.ece.ust.hk` comes back with a time to live of 3600 seconds, the resolver serves the same address to every client that asks during that hour and sends no query outside its own network. When the hour is over, the resolver asks the authoritative servers again, and a moved address replaces the old one in the cache.

A failure is cached too, in two shapes. A name that does not exist returns `NXDOMAIN`, and a name that exists without the requested type returns an empty answer. Neither reply carries a time to live of its own, so the minimum field of the zone's start of authority record sets the limit.

---

Flashcards for this section are as follows:

- caching: what does a name server do with the answers it receives? ::@:: It caches them and reuses them for later queries.
- time to live: what does the time to live on a cached answer control? ::@:: How long the server may keep it before asking again.
- cached answer: a resolver holds an address for 3600 seconds; what does it do with a query that arrives after that? ::@:: It asks the authoritative servers again and caches the address they return.
- inside the cached hour: a resolver caches an address with a time to live of $3600$ s; what happens to each query that arrives within that hour? ::@:: $3600\text{ s} = 3600/3600 = 1$ hour, during which each query receives the cached address and no query leaves the resolver's own network.
- negative answers: which two failures does a resolver cache, and what sets their time to live? ::@:: A name that does not exist, which returns `NXDOMAIN`, and a name that exists without the requested type, which returns an empty answer; the minimum field of the zone's start of authority record sets the time to live.

## resource records

A record is a tuple of five fields: the owner name it belongs to, its time to live, its class, its type, and its data. The type decides what the data means, and a zone file writes the five in that order.

---

Flashcards for this section are as follows:

- resource record: which five fields does one record hold, and in what order? ::@:: The owner name, the time to live, the class, the type, and the data.
- type field: what does the type field of a record decide? ::@:: What its data means, such as an address, a name, or a mail exchanger.

### record types

The common types:

- `A`: an Internet Protocol version 4 address.
- `AAAA`: an Internet Protocol version 6 address.
- `NS`: the authoritative servers of a zone.
- `CNAME`: an alias, paired with the canonical name it stands for.
- `MX`: a mail exchanger, with a preference number that orders several of them.
- `PTR`: a name, for a reverse lookup from an address.
- `TXT`: free text attached to a name.
- `SOA`: the zone's authority record.

The question picks the type: an address lookup asks for `A`, and an Internet Protocol version 6 lookup asks for `AAAA`. Finding the mail server of `ust.hk` takes two queries, one for the `MX` record of `ust.hk`, which names `mail.ust.hk`, and one for the `A` record of `mail.ust.hk`. A `CNAME` is followed: the `CNAME` record of `www.ust.hk` names `web.ece.ust.hk` as the canonical name, and the resolver looks up that name's address instead. A name that holds a `CNAME` record cannot hold other records of its own.

---

Flashcards for this section are as follows:

- type A: what does an `A` record map? ::@:: A host name to its Internet Protocol version 4 address.
- type AAAA: what does an `AAAA` record map? ::@:: A host name to its Internet Protocol version 6 address.
- type NS: what does an `NS` record name? ::@:: The authoritative name servers for a zone.
- type CNAME: what does a `CNAME` record map? ::@:: An alias name to the canonical name it stands for.
- type MX: what does an `MX` record name? ::@:: A mail exchanger for a domain, with a preference number that orders several of them.
- type PTR: what does a `PTR` record answer? ::@:: A reverse lookup, from an address back to a name.
- type TXT: what does a `TXT` record hold? ::@:: Free text attached to a name.
- mail exchanger: which two record types does a resolver look up to find the mail server of a domain? ::@:: The `MX` record, which names the mail exchanger, and then the `A` record of that name.
- canonical name: what does a resolver do with a `CNAME` record? ::@:: It follows the alias to the canonical name and looks up the address of that name.
- an alias carries nothing else: which other records can a name that holds a `CNAME` record carry? ::@:: None, so an alias never carries an address of its own.
- the mail example: which two records find the mail server of `ust.hk`, and what does the first one name? ::@:: The `MX` record of `ust.hk`, which names `mail.ust.hk`, and then the `A` record of that name.

### zone file syntax

A zone file is written in the presentation syntax, where each line is one record. One for `ece.ust.hk` reads as follows.

<!-- check: ignore-begin[math_in_code_fence]: $ORIGIN and $TTL are zone file directives written with dollar signs, not LaTeX -->

```text
$ORIGIN ece.ust.hk.
$TTL 3600
@        IN  SOA ns1.ust.hk. hostmaster.ust.hk. (
                 2026101201 ; serial
                 7200       ; refresh
                 3600       ; retry
                 1209600    ; expire
                 3600 )     ; minimum
@        IN  NS   ns1.ust.hk.
@        IN  NS   ns2.ust.hk.
ns1      IN  A    192.0.2.53
ns2      IN  A    192.0.2.54
www      IN  A    192.0.2.10
```

<!-- check: ignore-end[math_in_code_fence]: end of the zone file -->

The origin directive sets the zone's name: the suffix that relative names take, and the name that `@` stands for. The default time to live directive sets the time to live that a record without one of its own takes. The start of authority record names the primary server `ns1.ust.hk`, then the responsible mailbox with the `@` written as a dot, then the zone's serial number and its four timers, labelled refresh, retry, expire and minimum. The two name server records make `ns1` and `ns2` authoritative for the zone, and the address records give the two servers and the host `www` their addresses.

The time to live and the class may be left out of any line, and the class is `IN` for Internet in nearly every record. A time to live of zero tells a resolver not to cache the record, and the value may be written in units such as `1h` or `1d`.

---

Flashcards for this section are as follows:

- origin directive: what does the origin directive at the top of a zone file set? ::@:: The zone's own name, which is the suffix that relative names take and the name that `@` stands for.
- default time to live: what does the default time to live directive of a zone file set? ::@:: The time to live that a record without one of its own takes.
- start of authority: which parts does the start of authority record carry? ::@:: The primary server, the responsible mailbox with the `@` written as a dot, a serial number, and four timers: refresh, retry, expire and minimum.
- optional fields: which two fields of a zone file line may be left out? ::@:: The time to live and the class.
- time to live values: what does a time to live of zero mean, and in what units may a time to live be written? ::@:: Zero tells a resolver not to cache the record, and it may be written in units such as `1h` or `1d`.
- the start of authority values: the start of authority record of `ece.ust.hk` writes its four timers in seconds; which five numbers does it carry, and what do the timers come to at $3600$ s per hour and $86400$ s per day? ::@:: A serial of `2026101201`; a refresh of $7200/3600 = 2$ hours; a retry of $3600/3600 = 1$ hour; an expire of $1209600/86400 = 14$ days; and a minimum of `3600` s.
- the zone file addresses: which address does each `A` record of `ece.ust.hk` give? ::@:: `ns1` gets `192.0.2.53`, `ns2` gets `192.0.2.54`, and `www` gets `192.0.2.10`.

### delegation in the parent zone

The delegation for `ece.ust.hk` sits in the zone that holds `ust.hk`, and it names the child's servers rather than its hosts.

```text
ece.ust.hk.   172800  IN  NS  ns1.ust.hk.
ece.ust.hk.   172800  IN  NS  ns2.ust.hk.
ns1.ust.hk.   172800  IN  A   192.0.2.53
```

The first two lines name the servers that answer for `ece.ust.hk`, and the third gives the address of `ns1.ust.hk`, so a resolver referred there already holds what it needs.

---

Flashcards for this section are as follows:

- delegation records: which records does the zone `ust.hk` hold for its child `ece.ust.hk`? ::@:: Two `NS` records naming `ns1.ust.hk` and `ns2.ust.hk`, and an `A` record giving the address of `ns1.ust.hk`.
- delegation time to live: the three lines that delegate `ece.ust.hk` each carry a time to live of `172800`, the two `NS` records and the glue `A` record; how many days is that at $86400$ s per day? ::@:: $172800/86400 = 2$ days on each of them.

## message format

A query and its answer share one message format, which opens with a fixed 12-byte header and continues with four sections. The header holds an identification, a set of flags, and a count for each section: the questions, the answers, the authority records, and any additional records that may help.

---

Flashcards for this section are as follows:

- header size: how long is the fixed part of a Domain Name System (DNS) message header? ::@:: 12 bytes.
- the four sections: which four sections follow the header? ::@:: The questions, the answers, the authority records, and additional information.
- identification: what is the identification field for? ::@:: Matching a response to the request that caused it.
- flags: which four facts do the flag bits report? ::@:: Whether the message is a query or a response, whether the answer is authoritative, whether recursion is requested, and whether recursion is supported.

## indirection

A name may map to several addresses, and an address may carry several names. Several addresses behind one name spread load across servers, send each client to a nearby one, or move a service to new hardware without changing the name. Several names behind one address let one machine host many websites, since each request names the site it wants.

---

Flashcards for this section are as follows:

- one name many addresses: which three uses does one name pointing at several addresses serve? ::@:: Spreading load, sending clients to a nearer server, and moving a service to new hardware without changing the name.
- one address many names: what does one address carrying several names allow? ::@:: One machine to host many websites, each request naming the site it wants.
