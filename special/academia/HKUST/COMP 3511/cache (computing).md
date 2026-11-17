---
aliases:
  - COMP 3511 cache
  - cache
  - cache (computing)
  - caching
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/cache_(computing)
  - language/in/English
---

# cache (computing)

A cache keeps copies of what a large, slow store is most likely to be asked for next, in a small, fast store. Operating systems use one for memory, address translation, file blocks, file names, file directories, and network routes. Each level asks the same questions: whether an access hits, what fraction hit, which items are requested again.

An access checks the cache first. A __hit__ means the information is there, and the data is used directly, which is fast. A __miss__ means it is absent: the data is copied from the slower storage into the cache, then used.

Caching pays off when the frequent case gets much faster, so the infrequent case stops dominating the average. The [memory hierarchy](memory%20hierarchy.md) repeats this at every level, from the caches inside the processor down to the ones the operating system keeps for files and directories.

---

Flashcards for this section are as follows:

- what is caching? ::@:: Caching copies a subset of information from slower, larger storage into faster, smaller storage, so the frequent case gets faster and pulls the average down.
- caching levels ::@:: Caching happens at memory, address translation, file blocks, file names, file directories, and network routes.
- where an operating system caches ::@:: Caching applies wherever a subset of content must sit in a faster device, so part of a file directory on disk can be cached in memory.
- cache size versus storage size ::@:: A cache is usually much smaller than the storage it caches.
- cache hit ::@:: The requested information is already in the cache, so it is used directly.
- cache miss ::@:: The information is not in the cache, so the data is copied in from the slower storage and used.

## cache management and performance

The cache is much smaller than the storage it caches, so the system must choose what to keep; cache management is that choice of cache size and replacement policy.

The __cache hit ratio__ is the percentage of content found in the cache. It gives the average access time, $\text{average access time} = (\text{hit ratio} \times \text{hit time}) + (\text{miss ratio} \times \text{miss time})$, where the miss ratio is the complement of the hit ratio.

---

Flashcards for this section are as follows:

- what does cache management decide? ::@:: Cache management sets the cache size and the replacement policy, which matter because the cache is smaller than the storage it caches.
- cache hit ratio ::@:: The percentage of content found in the cache, and the main criterion for judging a cache.
- average access time: how do $\text{hit ratio}$, $\text{hit time}$, $\text{miss ratio}$, and $\text{miss time}$ combine? ::@:: $\text{average access time} = (\text{hit ratio} \times \text{hit time}) + (\text{miss ratio} \times \text{miss time})$.

## locality of reference

Caching works because programs do not touch memory uniformly. __Temporal locality__, locality in time, means an item accessed recently is likely to be accessed again. __Spatial locality__, locality in space, is the other half: contiguous blocks near a recently accessed item are likely to be accessed soon, in both data and program code.

Without locality a cache would not help: if every item were equally likely to be accessed, it would hold a uniformly random subset of storage and the hit chance would not improve.

---

Flashcards for this section are as follows:

- what is temporal locality? ::@:: An item accessed recently is likely to be accessed again.
- what is spatial locality? ::@:: Contiguous blocks near a recently accessed item are likely to be accessed soon, in both data and program code.
- why does caching work at all? ::@:: Caching works because of locality of reference; without an access pattern it would not work.
- what happens if all items are equally likely to be accessed? ::@:: The chance of finding a needed item would not improve.
