---
aliases:
  - ABR
  - ABR streaming
  - ELEC 3120 adaptive bitrate streaming
  - ELEC3120 adaptive bitrate streaming
  - HKUST ELEC 3120 adaptive bitrate streaming
  - HKUST ELEC3120 adaptive bitrate streaming
  - adaptive bitrate streaming
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/adaptive_bitrate_streaming
  - language/in/English
---

# adaptive bitrate streaming

Adaptive bitrate streaming varies the quality of the video to match what the network can carry, instead of sending one fixed encoding to every client. A 100 Mbps link gets high-quality video and a 10 Mbps link lower-quality video. An ABR algorithm runs throughout playback rather than choosing once at the start, so the quality follows the network as it varies.

---

Flashcards for this section are as follows:

- what does ABR change over the course of one playback, and when? ::@:: The video quality, and it keeps changing throughout playback rather than being fixed at the start

## matching quality to capacity

A multi-bitrate (MBR) server carries the same video at several quality levels. Suppose the client knows its own network capacity $N$. It then picks the largest send rate $C$ on offer such that $C < N$, which keeps the playback rate $R$ under what the network can deliver.

The client cannot measure $N$, so that selection rule is not one it can apply directly.

---

Flashcards for this section are as follows:

- in the idealised MBR picture where the client knows its capacity $N$, which send rate $C$ does it select from a quality ladder? ::@:: The largest $C$ on offer such that $C < N$
- what breaks the idealised selection rule in which the client picks the largest send rate $C$ below its capacity $N$? ::@:: The client cannot measure $N$

## what the algorithm sees

Write the algorithm as a function producing a bitrate, $$\mathit{bitrate} = f(x, y, z\ldots)$$. The obvious arguments are five: the average of past network capacity, the loss rate, the network latency, the change in network latency, and the bandwidth variance. ABR has a wide literature and no settled answer about which arguments are the right ones.

None of the five is one the client can measure directly. What it can read is the occupancy of its own buffer. So the client picks a target occupancy and lets a rule turn that occupancy into a bitrate. One parameter is enough, and that is the claim of [buffer-based rate adaptation](buffer-based%20rate%20adaptation.md).

---

Flashcards for this section are as follows:

- in $\mathit{bitrate} = f(x, y, z\ldots)$, which five arguments are the obvious ones? ::@:: The average of past network capacity, the loss rate, the network latency, the change in network latency, and the bandwidth variance
- the five obvious arguments to $f$ are all unmeasurable; what single quantity does the client read instead? ::@:: The occupancy of its own buffer, which a rule turns into a bitrate

## what the algorithm chooses

The output of the algorithm is the rate $C[t]$ at which the client requests the next chunk. With a ladder of quality levels in place, the expectation is that the playback rate $R$ now equals $C$. That does not hold, because the link delivers at whatever rate it can. The level off the ladder bounds $R$ from above instead of pinning it down.

---

Flashcards for this section are as follows:

- what is the output of an ABR algorithm? ::@:: The rate $C[t]$ at which the client requests the next chunk <!-- check: ignore-line[two_sided_calc_warning]: conceptual, the card names a rate rather than computing one -->
- with a ladder of quality levels on offer, does choosing a level pin the playback rate $R$ to the chosen send rate $C$? ::@:: No. It bounds $R$ from above without pinning it to a value

## where the decisions run

The ABR logic sits on the client, beside the buffer and the playhead, and not on the server. The request runs through four steps:

1. The client requests a chunk.
2. The ABR logic sets the rate $C[t]$ of that request.
3. The link delivers at $N[t]$ into the buffer.
4. The player reads the buffer out at $R[t]$.

The arrangement is the same as the [progressive download](progressive%20download.md) pipeline, with one more part at the client end: the logic that sets $C[t]$.

---

Flashcards for this section are as follows:

- in the streaming arrangement with ABR, what are $C[t]$, $N[t]$ and $R[t]$? ::@:: $C[t]$ is the rate the client requests the next chunk at, $N[t]$ is the rate the link delivers into the buffer, and $R[t]$ is the rate the player reads the buffer out at
