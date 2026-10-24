---
aliases:
  - ELEC 3120 max-min fairness
  - ELEC3120 max-min fairness
  - HKUST ELEC 3120 max-min fairness
  - HKUST ELEC3120 max-min fairness
  - max-min fair allocation
  - max-min fairness
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/max-min_fairness
  - language/in/English
---

# max-min fairness

Max-min fairness divides a link so that the smallest share is as large as it can be, which is not the same as splitting it equally. A flow that wants little gets only what it asks for, and the rest goes to the flows that want more, so no share grows without shrinking one that is already smaller.

---

Flashcards for this section are as follows:

- max-min fairness: what does max-min fairness maximise? ::@:: The smallest share any flow receives.
- equal shares against max-min: how does max-min fairness differ from splitting a link equally? ::@:: A flow gets only what it demands, and the rest is divided among the flows that still want more.
- the defining property: when is an allocation max-min fair? ::@:: When no flow's share can be increased without decreasing the share of a flow that already has less.

## mice and elephants

A mouse is a flow that wants little, such as a video stream needing 40 Mbps from a 1 Gbps link. An elephant is a flow that would use the whole gigabit, such as a large download. Split equally, the mouse gets 500 Mbps it cannot use and the elephant 500 Mbps, so most of the mouse's half sits idle. Under max-min fairness on a 100 Mbps link, flows demanding 10 Mbps and 90 Mbps each get what they asked for, and a flow demanding 200 Mbps is held to 90 Mbps while the other keeps its 10 Mbps.

---

Flashcards for this section are as follows:

- mouse and elephant: which two flow shapes do the names describe? ::@:: A mouse wants little and never uses more, while an elephant would take the whole link if allowed.
- equal-split arithmetic: splitting a $1\text{ Gbps}$ link equally between a $40\text{ Mbps}$ video stream and a download, how much is used and how much sits idle? ::@:: $1\text{ Gbps} = 1000\text{ Mbps}$, so $1000 / 2 = 500\text{ Mbps}$ each; used $40 + 500 = 540\text{ Mbps}$, leaving $1000 - 540 = 460\text{ Mbps}$ idle.
- the demand: what is a flow's demand $r_i$? ::@:: The most bandwidth it would use if it were given as much as it asked for.
- a mouse and an elephant on a 100 Mbps link: one flow demands $10\text{ Mbps}$ and another demands $90\text{ Mbps}$; what does max-min fairness give them? ::@:: $10\text{ Mbps}$ and $90\text{ Mbps}$, since the level rises to $100 - 10 = 90\text{ Mbps}$ and the shares fill the link.
- an elephant that overshoots the level: on a $100\text{ Mbps}$ link two flows demand $10\text{ Mbps}$ and $200\text{ Mbps}$; what does max-min fairness give each? ::@:: $10\text{ Mbps}$ to the small flow and $100 - 10 = 90\text{ Mbps}$ to the other, since the small flow stops at its demand and the level settles at $90$.

## water filling

Write $a_i = \min(f, r_i)$ for the share flow $i$ receives, where $f$ is the level such that the shares add up to the link's capacity $C$. Pouring water into the flows' buckets at the same rate gives the same answer: fill every bucket equally, stop one when it is full, and carry on until the water runs out. With $C = 10$, demands $8$, $6$, and $2$, the level settles at $f = 4$ and the shares are $4$, $4$, and $2$. With $C = 20$ and demands $12$, $6$, and $4$, the level settles at $f = 10$: the flows wanting 6 and 4 are already full, and the flow wanting 12 takes the remaining 10.

---

Flashcards for this section are as follows:

- the allocation rule: given demands $r_i$ and capacity $C$, what share does flow $i$ receive under max-min fairness? ::@:: $a_i = \min(f, r_i)$, where $f$ is the level at which the shares add up to $C$.
- water filling: how does the water-filling procedure find the level $f$? ::@:: Fill every flow's bucket at the same rate, stop each one when it is full, and continue with the others until the capacity is used.
- worked case: with capacity $10$ and demands $8$, $6$, and $2$, what level and what shares does max-min fairness give? ::@:: $f = 4$, giving shares $4$, $4$, and $2$, since $4 + 4 + 2 = 10$.
- finding the level beside a full flow: with capacity $20\text{ Mbps}$ and demands $12\text{ Mbps}$, $6\text{ Mbps}$, and $4\text{ Mbps}$, why does the level settle at $10\text{ Mbps}$? ::@:: The flows demanding $6\text{ Mbps}$ and $4\text{ Mbps}$ are already full and hold $6 + 4 = 10\text{ Mbps}$, so the flow demanding $12\text{ Mbps}$ takes the remaining $20 - 10 = 10\text{ Mbps}$ alone.

## work conservation

A scheduler is work-conserving when it never leaves the resource idle while something is queued for it. Max-min fairness has that property by construction: the level rises until the capacity is used, so no bandwidth goes unspent while a flow wants more, and every flow whose demand reaches the level receives the same share as the others that reach it. When a flow goes idle its share is released and the level rises for the rest: with $C = 10$ and demands $8$, $6$, and $2$, the level rises to 5 once the flow wanting 2 stops.

---

Flashcards for this section are as follows:

- work conservation: when is a scheduler work-conserving? ::@:: When it never leaves the resource idle while a job is waiting to use it.
- why max-min is work-conserving: what does the water-filling level guarantee about the capacity? ::@:: The level rises until the shares use all of it, so none goes unspent while a flow wants more.
- the fairness claim: what does a flow receive relative to the others when its demand is at least the level $f$? ::@:: The same share as every other flow at or above the level.
- an idle flow: with capacity $10\text{ Mbps}$ and demands $8\text{ Mbps}$, $6\text{ Mbps}$, and $2\text{ Mbps}$, the flow demanding $2\text{ Mbps}$ goes idle; what do the two remaining flows receive? ::@:: $5\text{ Mbps}$ each, since the level rises to $10 / 2 = 5\text{ Mbps}$ once two flows share the capacity.
