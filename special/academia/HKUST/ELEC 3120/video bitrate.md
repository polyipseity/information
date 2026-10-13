---
aliases:
  - ELEC 3120 video bitrate
  - ELEC3120 video bitrate
  - HKUST ELEC 3120 video bitrate
  - HKUST ELEC3120 video bitrate
  - bitrate
  - video bitrate
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/video_bitrate
  - language/in/English
---

# video bitrate

Video bitrate is the number of bits the file has to store for one second of playback. More bits per second buys better quality, and that holds while every second on screen shows the same kind of picture.

The client plays out of a buffer, which is the store of video it has already fetched and not yet played. Only the network fills that buffer, so the bitrate is also the rate the network has to deliver. [Progressive download](progressive%20download.md#bitrate%20against%20network%20capacity) fills the buffer before playback starts rather than during it.

---

Flashcards for this section are as follows:

- too high or too low: which side stalls playback, and what happens on the other? ::@:: Above what the network delivers, the buffer drains faster than it fills and playback stalls; below it, network capacity goes unused and the picture is worse than it needed to be
- video bitrate: bits per second of what? ::@:: Playback

## variable bitrate encoding

A provider encodes to an average or target bitrate, and that one number has to cover a whole video. Segments differ in how many bits they need. An action scene changes every bit on the screen from frame to frame and takes a lot of bits per second. A character asleep on screen is the same picture second after second and produces almost no new data. An average taken over the whole video understates the action scene and overstates the sleeping one.

Variable bitrate encoding gives each segment a rate of its own.

---

Flashcards for this section are as follows:

- why does one target bitrate serve an action scene badly and a sleeping scene badly? ::@:: It is an average over the whole video, so it is too low for a scene that changes every bit and too high for one that repeats the same picture
- variable bitrate encoding: what does the per-segment rate achieve? ::@:: The action scene gets the bits it needs, and the sleeping scene does not spend them
