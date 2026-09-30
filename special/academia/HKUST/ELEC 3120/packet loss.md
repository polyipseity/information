---
aliases:
  - ELEC 3120 packet loss
  - ELEC3120 packet loss
  - HKUST ELEC 3120 packet loss
  - HKUST ELEC3120 packet loss
  - data loss
  - loss rate
  - packet loss
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/packet_loss
  - language/in/English
---

# packet loss

A packet that never arrives is lost, and how often that happens depends on the medium carrying it: every medium has its own error rate, so the same data sent over two links is not equally likely to survive. Loss is not always a fault, and a transport protocol such as [TCP loss recovery](TCP%20loss%20recovery.md) has to detect what was lost and repair it without knowing why it went missing.

---

Flashcards for this section are as follows:

- overview ::@:: Packet loss is data that fails to reach its destination, and how often it happens follows from the medium's error rate.
- why do two links lose data at different rates? ::@:: Their media have different error rates.
- what happens to data a protocol loses? ::@:: The transport protocol detects it and sends it again, as TCP does.

## error rates

Media differ in more than bandwidth and latency. Each kind of medium has its own error rate, and errors are what a receiver sees as loss, so a link's loss rate is a property of its medium rather than of the data passing over it.

---

Flashcards for this section are as follows:

- which link property follows from a medium's error rate? ::@:: Its data loss rate.
- is a link's loss rate a property of the data? ::@:: No: it is a property of the medium, which has its own error rate.

## causes of random loss

Loss with no fault behind it comes from the medium and the surroundings. A solar flare disturbs a link; a microwave oven running nearby disturbs a wireless one; a cable plugged in wrong breaks a connection; and several transmitters sending at the same time talk over one another, as a crowd of people speaking at once does.

---

Flashcards for this section are as follows:

- four causes of random loss: which are they? ::@:: A solar flare, a nearby microwave oven, a cable plugged in wrong, and several transmitters sending at once.
- why do simultaneous transmitters lose data? ::@:: They interfere with one another, like people talking over each other in a crowded room.
- why is this loss called random? ::@:: Nothing in the protocol caused it: the medium or its surroundings did.
