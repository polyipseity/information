---
aliases:
  - ELEC 3120 progressive download
  - ELEC3120 progressive download
  - HKUST ELEC 3120 progressive download
  - HKUST ELEC3120 progressive download
  - progressive HTTP download
  - progressive download
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/progressive_download
  - language/in/English
---

# progressive download

Downloading the whole file before playing it makes the client wait a long time to start, and it needs the whole video on disk. It does not need gigabytes of storage, only the next few seconds of video, with the rest of the file arriving while those seconds play.

---

Flashcards for this section are as follows:

- progressive download: what does the client keep on disk, and what happens to the rest of the file? ::@:: Only the next few seconds of video, with the rest of the file arriving while those play.

## the client buffer

The client holds the next few seconds of video in a buffer. The server sends data to it at a rate $C$, and the client reads from it and plays video at a rate $R$. The buffer absorbs the difference between the two, and how much difference there is decides whether the video stalls.

---

Flashcards for this section are as follows:

- progressive download: what do the arrival rate $C$ and the playback rate $R$ stand for? ::@:: $C$ is the rate the server sends data to the buffer at, and $R$ is the rate the client reads from the buffer and plays video at.
- which way do the two rates push on the client buffer? ::@:: The difference between them accumulates in the buffer, so a server slower than the player drains it towards empty and a stall follows.

## buffer occupancy

Buffer occupancy is the gap between two lines on one set of axes: $$A(t) = Ct + b$$, the data the server has delivered by time $t$, and $$S(t) = Rt$$, the data the player has shown by then. While $C < R$ the arrival line climbs faster than the playback line, and the gap between them shrinks as playback continues.

Take $t = 0$ as the moment playing starts. Downloading began $k$ seconds earlier, so the arrival line starts at $(-k, 0)$ and reaches $b$ at $t = 0$. That height is $b$: the data fetched during those first $k$ seconds, waiting in the buffer when the first frame plays. The playback line starts at the origin instead, since nothing has been shown when playing begins.

The buffer is designed to be empty exactly at $f$, the time the video ends. By then the playback line carries the whole video and the arrival line has reached the same height, so the client has downloaded everything it needed and nothing more. A stall is the moment the gap hits zero before $f$.

---

Flashcards for this section are as follows:

- in the buffer-occupancy plot, what do $A(t) = Ct + b$ and $S(t) = Rt$ each count? ::@:: $A(t) = Ct + b$ counts data the server has delivered by time $t$, and $S(t) = Rt$ counts data the player has shown by then.
- what is buffer occupancy, read as $$A(t) - S(t)$$ on that plot? ::@:: The gap between the two lines, $$A(t) - S(t)$$.
- what does $b$ mean in the arrival curve $A(t) = Ct + b$? ::@:: The buffer occupancy at the moment playing starts, so the intercept of $A(t)$ at $t = 0$ and not at $t = -k$.
- why is the buffer designed to be empty at $t = f$? ::@:: So the client has downloaded nothing it did not need and nothing is left over when the video ends.
- in this plot, what is a stall, and when does it happen before $f$? ::@:: The moment occupancy, the gap between the two lines, reaches zero before $f$.

## bitrate against network capacity

The network capacity $N$ is the rate the connection is guaranteed to deliver.

Take a Firebuds video running at a bitrate of $8$ Mbps over a connection guaranteed at $6$ Mbps, with $3$ GB in total. Playing $3$ GB at $8$ Mbps takes $$t = f = \frac{3 \times 8 \times 10^{9}}{8 \times 10^{6}} = 3000 \text{ s}$$. Over those $3000$ s the connection delivers $6 \times 3000 = 18000$ Mb where the player needs $8 \times 3000 = 24000$ Mb, so the buffer must hold the difference the network will not deliver in time: $$b = (R - C) f = (8 - 6) \times 3000 = 6000 \text{ Mb} = 750 \text{ MB}$$.

Priming the buffer means accumulating those $750$ MB at $6$ Mbps, which takes $$k = \frac{b}{C} = \frac{6 \times 10^{9}}{6 \times 10^{6}} = 1000 \text{ s} = 16.67 \text{ minutes}$$. A bitrate above the network capacity $N$ costs that much buffering before playback can start.

A bitrate on either side of the network capacity is a mistake, and each side costs something. A bitrate well below the network capacity costs quality instead. On a playback curve such as $$S(t) = 2\text{Mb} \cdot t$$, well below the arrival curve, the buffer needs less space and less time to build. Its occupancy there is a second and much smaller one, $b'$, not the $b$ above. What is left is poor quality video.

Serving several quality levels and switching between them removes both errors. [adaptive bitrate streaming](adaptive%20bitrate%20streaming.md) is where that belongs, and [buffer-based rate adaptation](buffer-based%20rate%20adaptation.md) is the version that picks the bitrate from the buffer occupancy.

---

Flashcards for this section are as follows:

- worked case, $3$ GB at $R = 8$ Mbps over $C = 6$ Mbps: how long is the playback? ::@:: $f = 3000$ s, since 3 GB is $24 \times 10^{9}$ bits at $8 \times 10^{6}$ bits per second.
- worked case, $3$ GB at $R = 8$ Mbps over $C = 6$ Mbps: how large must the buffer be to finish stall-free? ::@:: $b = (R - C) f = (8 - 6) \times 3000 = 6000$ Mb, which is 750 MB.
- worked case, $3$ GB at $R = 8$ Mbps over $C = 6$ Mbps: how long does priming the buffer take? ::@:: $k = b / C = 6000$ Mb at $6$ Mbps $= 1000$ s, which is 16.67 minutes.
- what does a bitrate a lot higher than the network capacity force? ::@:: A big buffer and a lot of buffering time, so playback can be guaranteed stall-free.
- what does a bitrate a lot smaller than the network capacity give up? ::@:: Poor quality video, in exchange for less buffer space and less time to build it up.
- undershoot against overshoot: how does the occupancy $b'$ in the undershoot case differ from the occupancy $b$ in the overshoot case? ::@:: It is a second and much smaller occupancy, $b'$, rather than the $b$ the overshoot case needs.

## buffers against variability

The argument against buffers holds when it comes to memory. If $C < N$, the client can set the send rate equal to the playback rate and keep the buffer at a constant level, so no extra capacity is needed.

What that reasoning leaves out is that it holds only if the data really does arrive at the client at a fixed rate.

Network capacities vary, for three reasons: new users joining the network or existing ones leaving, link failures and re-routes, and WiFi interference.

Give the client a tiny buffer and "just in time" fails. The client measures the capacity once, as $N[t = 0]$, and playback starts. At $t = 1$ the bandwidth drops, the buffer holds nothing to give, and playback stops.

A larger buffer survives the same moments. The buffer is full at $t = 0$ and playback begins. At $t = 1$ the bandwidth drops and the buffer starts to drain, at $t = 2$ it is drained further, and at $t = 3$ further again. At $t = 4$ the network recovers and the buffer refills.

The buffer lets playback run at the average available bandwidth rather than the instantaneous rate. A client on a high-variance network needs a larger buffer than a client on a low-variance one.

The variability does not stop at the network either. The playback rate is variable too, and the bitrate the client reads is $R[t]$ against a capacity of $N[t]$. That is the subject of [video bitrate](video%20bitrate.md).

---

Flashcards for this section are as follows:

- what is the argument for a buffer of a sliver only, when $C < N$? ::@:: Data can go in just in time at the rate it is read out, so no extra capacity is needed and the memory is not wasted.
- what does that argument assume? ::@:: That the data arrives at the client at a fixed rate.
- what makes a network capacity vary? ::@:: New users joining or existing ones leaving, link failures and re-routes, and WiFi interference.
- tiny buffer, capacity measured as $N[t = 0]$: what happens when the bandwidth drops at $t = 1$? ::@:: The buffer is empty, so playback stops.
- larger buffer, bandwidth dropping at $t = 1$, $t = 2$, and $t = 3$ before recovering at $t = 4$: what does the buffer do? ::@:: It drains across the drops, a little less at each one, and starts refilling once the network recovers.
- what rate does a buffered player run at? ::@:: A rate corresponding to the average available bandwidth, not the instantaneous one.
- which client needs the larger buffer? ::@:: The client on the high-variance network.
- in a client whose playback rate is variable as well as its network capacity, what is the bitrate the client reads? ::@:: $R[t]$, against a capacity of $N[t]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual, the card names the two varying quantities rather than computing one -->
