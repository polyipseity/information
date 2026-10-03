---
aliases:
  - ELEC 3120 worse is better
  - ELEC3120 worse is better
  - HKUST ELEC 3120 worse is better
  - HKUST ELEC3120 worse is better
  - KISS
  - worse is better
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/worse_is_better
  - language/in/English
---

# worse is better

A design with less in it can beat a more elaborate one. On-demand video is one such case, where a file server handing out files over ordinary requests won.

---

Flashcards for this section are as follows:

- on-demand video: which arrangement won the "worse is better" case, and what did it beat? ::@:: A file server handing out files over ordinary requests won, over a media server keeping a session in step with a player application

## tight integration and weak integration

What lost was a media server keeping a session in step with a player application. Tight integration means every component is built to fit the others. A custom media player is built that way: a dedicated application, a custom protocol such as RTSP, and a media server, all written against each other.

The session runs through a fixed sequence:

1. __SETUP__, to create the session
2. __PLAY__, to start it
3. the media stream, running one way from the media server to the player
4. __PAUSE__, to hold the stream
5. __TEARDOWN__, to end the session

Each of the four requests carries its own reply, so both ends have to agree at every step about what state the session is in. The stream carries nothing back, which makes it the one item on the list running a single way. Replace the protocol with HTTP and the whole list disappears, because an HTTP request does not carry state from the one before it.

Weak integration gives up the fit between the components. A web browser fetches a presentation description from a web server and hands it to the player. Any server can serve any client, the player plays whatever it fetches, and a cache can hold the pieces. Each piece does one job and knows nothing about the others.

---

Flashcards for this section are as follows:

- tight integration: what does fitting every component to the others cost? ::@:: Each component has to be rebuilt whenever another one changes
- RTSP session: why must client and server agree at every step? ::@:: Each of the four requests carries its own reply, so both ends track the session state together
- HTTP: why does it need none of the RTSP steps? ::@:: An HTTP request carries no state from the one before it

## three reasons the simpler design won

1. __Backwards-compatible.__ What already runs keeps running. A scheme that breaks what came before pays for it in everyone who would have to change.
2. __Less complex.__ Fewer moving parts means a smaller thing to get wrong, and a small thing is easier to replace when it does go wrong.
3. __Easy to scale.__ Growing by adding more of the same ordinary server lets a design handle more load. Adding a new kind of server does not let it handle more load.

---

Flashcards for this section are as follows:

- which three properties let the simpler design win? ::@:: Being backwards-compatible, less complex, and easy to scale
