---
aliases:
  - ELEC 3120 flow control (data)
  - ELEC3120 flow control (data)
  - HKUST ELEC 3120 flow control (data)
  - HKUST ELEC3120 flow control (data)
  - advertised window
  - flow control
  - flow control (data)
  - receive window
  - receive window size
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/flow_control_(data)
  - language/in/English
---

# flow control (data)

Flow control keeps a fast sender from overrunning the receiver's buffer. The receiver states how much room it has left, and the sender limits its sending window to that value.

---

Flashcards for this section are as follows:

- overview ::@:: Flow control keeps a fast sender within the buffer room the receiver has left.
- what sets the limit: what decides how much a sender may have outstanding under flow control? ::@:: The receiver's own resources, through the room left in its buffer.
- what happens without it: what happens to a receiver that the sender outruns? ::@:: Its buffer overflows, because data arrives faster than it is drained.

## receive window

The receive window, also called the advertised window, is the buffer room the receiver has left, and it travels in the header of the packets the receiver sends back. Its size follows from the buffer size, the CPU processing ability, and the system memory size. A receiver whose $64$ MSS buffer holds $30$ MSS advertises the remaining $34$ MSS. That room changes as the application reads data, so the advertised window differs from one reply to the next.

---

Flashcards for this section are as follows:

- receive window: what is it, and where does the sender learn it? ::@:: The buffer room the receiver has left, published in the headers the receiver sends back.
- setting the receive window: which receiver properties decide it? ::@:: The buffer size, the CPU processing ability, and the system memory size.
- remaining buffer: a buffer of $64$ MSS holds $30$ MSS; what does the receiver advertise? ::@:: $34$ MSS, the room left.
- why it changes: why is the advertised window different in each reply? ::@:: The free buffer space changes as the application reads data.

## sending window

The sender takes the advertised window $RWND$ as a limit on its sending window and re-reads it from every reply. Its outstanding bytes also stay within the congestion window $CWND$, so the sending window is $\min(RWND, CWND)$. When the receiver's free buffer shrinks, the sender brings its window down at once; otherwise it keeps transmitting into buffer room that no longer exists.

---

Flashcards for this section are as follows:

- sending window: what is the sending window when the advertised window is $RWND$ and the congestion window is $CWND$? ::@:: $\min(RWND, CWND)$: it never exceeds the smaller of the two.
- shrinking: the advertised window shrinks while the sender has a full window outstanding; what must the sender do? ::@:: Bring its sending window down to the new value at once, since the receiver no longer has room.
