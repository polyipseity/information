---
aliases:
  - ELEC 3120 media segmentation
  - ELEC3120 media segmentation
  - HKUST ELEC 3120 media segmentation
  - HKUST ELEC3120 media segmentation
  - HTTP chunking
  - chunking
  - video chunk
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/media_segmentation
  - language/in/English
---

# media segmentation

Media segmentation cuts a video into pieces and fetches each piece as an ordinary HTTP object, so on-demand video runs over the Web instead of over a protocol built for streaming it. The term for it is HTTP chunking, and a chunk is one of the pieces.

---

Flashcards for this section are as follows:

- what is media segmentation? ::@:: Cutting a video into chunks and fetching them over HTTP one at a time, in order, so the browser can play them back to back as one long video
- HTTP chunking: what is it, and what are the pieces called? ::@:: The same thing as media segmentation. The pieces are called chunks

## from custom protocols to HTTP

Video delivery in the late 1990s and early 2000s made the viewer sort out the connection before anything played. A line speed is how fast the viewer's own link carries bits. Windows Media Player asked for one up front. Its "Select your connection speed" dialog offered three: 28.8, 56.6 and T1. Nothing played until one of them was chosen.

That was the wrong number to ask for. A viewer needs the bitrate the video will arrive at, and a line speed only guesses at it. A YouTube viewer chooses nothing of the kind.

The stack behind that dialog was built around its own application. QuickTime, Windows Media Player, RealNetworks and WebTV all shipped as programs of their own, separate from the browser. Each talked to a media server over a custom protocol such as RTSP. RTSP was stateful, so client and server had to agree on session state before any video moved. The protocol took more machinery than HTTP does. Every component was customised to fit the others. That is what "tight" integration names.

A web browser first asks a web server for the presentation description and hands it to the media player. From then on the player and the media server run four requests around one stream:

1. __SETUP__, to create the session
2. __PLAY__, to start it
3. the media stream itself, running one way from the media server to the player
4. __PAUSE__, to stop the stream and hold it
5. __TEARDOWN__, to end the session

Each of the four requests is answered separately, so the two ends have to stay in step.

---

Flashcards for this section are as follows:

- what had a viewer of Windows Media Player do before video would play? ::@:: Pick their own line speed from a "Select your connection speed" dialog offering 28.8, 56.6 and T1
- which protocol did that generation of media players speak to their media server? ::@:: RTSP
- what does stateful cost a custom media protocol? ::@:: Client and server have to agree on session state before video moves, so every request needs its own reply and the two ends have to stay in step
- what does "tight" integration name in that generation? ::@:: Every component being customised to fit the others, servers, clients and protocols alike
- where does the presentation description come from? ::@:: A web server, fetched by the web browser over HTTP and then handed to the media player
- an RTSP session: what is the order of the steps once the player has the presentation description? ::@:: SETUP, PLAY, the one-way media stream from the server to the player, then PAUSE and TEARDOWN

## chunking

A chunk has a size and a duration. The size is 2 MB, and the duration a few seconds, with Netflix's running $4$ s. Neither number is a property of HTTP. Both are the service's own choice.

---

Flashcards for this section are as follows:

- chunk size and length: a chunk is 2 MB and Netflix's run is $4$ s, so who decides both? ::@:: The service does, not the protocol

## why HTTP took over

Four things follow from a chunk being an ordinary file over HTTP.

1. __Playback moves into the browser.__ A client needs no new software: the browser already fetches and plays objects.
2. __Servers are "stupid" again.__ A media server hands out small chunks of video over ordinary stateless HTTP, and holds no session state for anyone. Compare [state management](HTTP.md#state%20management).
3. __Caches and CDNs work again.__ A chunk is a file downloaded over HTTP, so it can be stored in a cache or pushed out through a CDN. That is where the scalability comes from.
4. __The send rate $C$ can change mid-stream.__ Each chunk is fetched separately, so the client can ask for a faster one after a fast period and a slower one after a slow period. A single stream over a stateful session cannot do this. It fixes its rate when the session is set up, so a network that slows down leaves the client nothing to do but wait. This is adaptive bitrate (ABR) streaming. [adaptive bitrate streaming](adaptive%20bitrate%20streaming.md) and [buffer-based rate adaptation](buffer-based%20rate%20adaptation.md) take over from here.

---

Flashcards for this section are as follows:

- what does a chunk being an ordinary file over HTTP do for the client? ::@:: Playback moves into the browser, so the client needs no new software
- what does a chunk being an ordinary file over HTTP do for the server? ::@:: It is "stupid" again, offering up small chunks of video over stateless HTTP and holding no session state
- what does a chunk being an ordinary file over HTTP do for caching? ::@:: Chunks can be stored in caches and CDNs, which is where the scalability comes from
- what does segmentation allow the client to change? ::@:: Its choice of download rate, once per chunk.<br/>
That is what makes adaptive bitrate streaming possible.
- why could a single stateful session not change its rate mid-stream? ::@:: Because it fixes the rate when the session is set up, so a network that slows down leaves the client nothing to do but wait
