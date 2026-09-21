---
aliases:
  - ELEC 3120 sliding window protocol
  - ELEC3120 sliding window protocol
  - HKUST ELEC 3120 sliding window protocol
  - HKUST ELEC3120 sliding window protocol
  - sliding window
  - sliding window protocol
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/sliding_window_protocol
  - language/in/English
---

# sliding window protocol

A sliding window protocol lets a sender keep several segments in flight instead of stopping after each one. It holds a window of consecutive segments, sends them all, and moves the window forward as acknowledgements come back. The receiver bounds that window with an advertised window, and the network with a congestion window. With one segment the protocol is stop-and-wait: send one, wait for its acknowledgement, send the next.

---

Flashcards for this section are as follows:

- overview ::@:: A sliding window protocol lets a sender keep several unacknowledged segments in flight: it sends every segment inside a window and slides the window forward as acknowledgements arrive.
- how it differs from stop-and-wait: what does a sliding window protocol do that stop-and-wait does not? ::@:: It keeps more than one segment outstanding.
- window of one segment: which protocol is it when the window holds one segment? ::@:: Stop-and-wait.
- what bounds the window: which two values bound the sending window? ::@:: The advertised window and the congestion window.

## sequence numbers

Each segment carries a sequence number naming the first byte of the stream it holds. The receiver uses it to place out-of-order segments, to notice a byte that never arrived, and to discard a duplicate.

---

Flashcards for this section are as follows:

- sequence number: what does a segment's sequence number name? ::@:: The first byte of the stream it carries.
- what the receiver does with it: how does the receiver use a segment's sequence number? ::@:: To place out-of-order segments, to notice a missing byte, and to discard duplicates.

## acknowledgement numbers

The acknowledgement number names the next byte the receiver expects. It is cumulative, so acknowledging byte $n$ also states that every byte before $n$ has arrived.

---

Flashcards for this section are as follows:

- acknowledgement number: what does a segment's acknowledgement number name? ::@:: The next byte the receiver expects.
- cumulative acknowledgement: a receiver acknowledges the byte $n$; what does that say about the bytes before $n$? ::@:: That every one of them has arrived.

## sliding window

The window covers the segments sent but not yet acknowledged; its size bounds how many bytes may be outstanding. When an acknowledgement arrives, the window's left edge moves up to the acknowledged byte, leaving room for new segments. The sender may only transmit segments still inside the window.

---

Flashcards for this section are as follows:

- what the window covers: which segments lie inside the sending window? ::@:: Those sent but not yet acknowledged.
- sliding forward: what happens to the window when an acknowledgement arrives? ::@:: Its left edge moves up to the acknowledged byte, leaving room for new segments.
- transmission rule: which segments is the sender allowed to transmit? ::@:: Only those inside the window.
- duplicate segment: a repeat of already-acknowledged bytes arrives; what does the receiver do? ::@:: Discards it as a duplicate, since it lies below the window.
