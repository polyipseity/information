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

Caching is the most reused trick in computer systems: a small, fast store holds copies of what a large, slow store is most likely to be asked for next. Operating systems use it for memory, address translation, file blocks, file names, file directories, and network routes, so the same few ideas recur at every level: hit or miss, the hit ratio, and locality of reference.

An access first checks whether the requested information is already in the cache. If it is, that is a __hit__ and the information is used directly, which is fast. If not, that is a __miss__, and the data is copied from the slower storage into the cache and used there.

Caching pays off whenever the frequent case becomes much faster and the infrequent case becomes much less dominant. The same structure appears at every level of the [memory hierarchy](memory%20hierarchy.md), from the caches in the processor down to those the operating system keeps for files and directories.

---

Flashcards for this section are as follows:

- caching definition ::@:: Copying a subset of information from slower, larger storage to faster, smaller storage, so frequent cases become faster and infrequent ones less dominant.
- levels at which caching is performed ::@:: Caching is performed at many levels, including memory, address translation, file blocks, file names, file directories, and network routes.
- caching inside an operating system ::@:: Whenever a subset of content needs to be stored in a faster device, caching applies; part of a file directory stored on a hard disk can also be cached in memory.
- cache versus cached storage size ::@:: The cache is usually much smaller than the storage it caches.
- cache hit ::@:: The information is already inside the cache, so it is used directly, which is fast.
- cache miss ::@:: The information is not in the cache, so the data is copied in from the slower storage and used there.

## cache management and performance

Because the cache is much smaller than the storage it caches, the system must choose what to keep: cache management is choosing the cache size and the replacement policy.

A cache's quality is summarized by the __cache hit ratio__, the percentage of content found in the cache. The hit ratio gives the average access time, $\text{average access time} = (\text{hit ratio} \times \text{hit time}) + (\text{miss ratio} \times \text{miss time})$, where the miss ratio is the complement of the hit ratio.

---

Flashcards for this section are as follows:

- cache management ::@:: Because the cache is much smaller than the storage being cached, the design must decide the cache size and the replacement policy.
- cache hit ratio ::@:: The percentage of content found in the cache; the major criterion used to judge a cache.
- average access time: how do $\text{hit ratio}$, $\text{hit time}$, $\text{miss ratio}$, and $\text{miss time}$ combine? ::@:: $\text{average access time} = (\text{hit ratio} \times \text{hit time}) + (\text{miss ratio} \times \text{miss time})$.

## locality of reference

Caching works only because programs do not touch memory uniformly. __Temporal locality__, or locality in time, means recently accessed items are likely to be accessed again. __Spatial locality__, or locality in space, means the contiguous blocks near a recently accessed item are likely to be accessed shortly, for both data and program code.

Without locality caching would not work: if every item were equally likely to be accessed, the cache would hold a uniformly random subset of the storage, and the hit chance would not improve.

---

Flashcards for this section are as follows:

- temporal locality ::@:: Locality in time: items that were accessed recently are likely to be accessed again.
- spatial locality ::@:: Locality in space: the contiguous blocks near a recently accessed item are likely to be accessed shortly, for both data and program.
- why caching works at all ::@:: Caching works because of locality of reference; without an access-locality pattern it would never work.
- equal-probability counterexample ::@:: If all items were equally likely to be accessed, the chance of finding a needed item would not improve.
