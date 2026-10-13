---
aliases:
  - BBA
  - BBA-0
  - ELEC 3120 buffer-based rate adaptation
  - ELEC3120 buffer-based rate adaptation
  - HKUST ELEC 3120 buffer-based rate adaptation
  - HKUST ELEC3120 buffer-based rate adaptation
  - buffer-based rate adaptation
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/buffer-based_rate_adaptation
  - language/in/English
---

# buffer-based rate adaptation

Buffer-based rate adaptation (BBA) is a family of methods for choosing the bitrate of each chunk of a video stream. Each one reads the client's buffer and turns that occupancy into the rate to request next. Playback drains the buffer at a steady rate, so the occupancy falls. Unless the network replaces what is played, it falls to a stall. The simplest version, BBA-0, ignores everything else about the network and about playback.

---

Flashcards for this section are as follows:

- what one quantity does BBA-0 read to pick a bitrate? ::@:: The occupancy of the client's buffer, and nothing else
- what does BBA-0 leave out? ::@:: Variability in the rate of video payout. Variability in network load it does handle
- which is the simplest version of buffer-based rate adaptation? ::@:: BBA-0

## one parameter

One parameter is enough to choose a bitrate: the occupancy of the buffer at the receiver. Te-Yuan Huang, an engineer at Netflix, built the BBA-n algorithms on that claim. Independent studies as of 2022 suggest BBA continues to outperform all other known algorithms, even ones that are much more complicated.

Here the occupancy is a measurement, not the guarantee it was when the buffer size was chosen in [progressive download](progressive%20download.md). Read at the moment a request is made, it reports how much video the client already holds.

---

Flashcards for this section are as follows:

- what do independent studies say about BBA as of 2022? ::@:: That it keeps outperforming every other known algorithm, including ones that are much more complicated
- is the buffer occupancy used here as a guarantee or as a measurement? ::@:: A measurement, read when the next request is made and turned into a bitrate

## the rule

The rule is a curve. Buffer occupancy runs along the horizontal axis, marked at $b_{\max}$. The bitrate to choose runs up the vertical axis, marked at $R_{\min}$ and $R_{\max}$. A full buffer means the highest possible bitrate, and an empty buffer means the lowest. The obvious shape joining the two is a straight line from the $R_{\min}$ point on the vertical axis up to the top of the plot.

That line is wrong at its top end. The client only reaches $R_{\max}$ when the buffer is already full, and there is no room to pull in a few segments at that rate. The fix is an upper reservoir, a stretch of occupancy at which playback runs at $R_{\max}$ with room left over to keep pulling segments in.

The line is also wrong at its bottom end, where a sudden drop in the network stalls playback while the buffer is low but not yet empty. The fix is a lower reservoir, a stretch that stores lots of time at low bitrate, so the network drains it slowly and does not stall.

Three regions of the occupancy axis carry the rule. The lower reservoir, of size $r$, runs up from an empty buffer. The cushion of size $cu$ follows it. From $r + cu$ upward lies the upper reservoir. The chosen rate is $R_{\min}$ through the lower reservoir, rises across the cushion, and is $R_{\max}$ through the upper reservoir. <p> ![bitrate to choose against buffer occupancy: a low flat piece from the vertical axis to the first tick under it, a straight ramp, and a high flat piece running on to a tick at full buffer, with three double-headed arrows under the axis marking the widths of the lower reservoir, the cushion, and the upper reservoir](attachments/bba0_bitrate_selection.svg)

---

Flashcards for this section are as follows:

- for a bitrate selection curve marked at $b_{\max}$, $R_{\min}$, and $R_{\max}$: which axis is which, and what quantity does each one measure? ::@:: Buffer occupancy on the horizontal axis, marked at $b_{\max}$, against bitrate to choose on the vertical axis, marked at $R_{\min}$ and $R_{\max}$
- what does the straight line from the $R_{\min}$ point to $R_{\max}$ at the top of the plot get wrong? ::@:: The client reaches $R_{\max}$ only with a full buffer, so it never actually gets its maximum bitrate and has no room to pull in segments at that rate
- what is the danger zone at the bottom of the occupancy axis? ::@:: The network suddenly drops while the buffer is low but not empty, and playback stalls
- what does the lower reservoir store, and what is it for? ::@:: Lots of time at low bitrate, which keeps a network drop from causing a stall
- for a buffer occupancy axis with a reservoir of size $r$ and a cushion of size $cu$, what are the three regions from low to high? ::@:: The lower reservoir below $r$, the cushion of size $cu$, and the upper reservoir from $r + cu$ upward
- which of $R_{\min}$ and $R_{\max}$ is chosen in the lower reservoir, in the cushion, and in the upper reservoir? ::@:: $R_{\min}$ through the lower reservoir, rising across the cushion, and $R_{\max}$ through the upper reservoir
- draw the bitrate selection curve for a buffer holding at most $b_{\max}$, with a reservoir of size $r$ and a cushion of size $cu$: what shape does it have against buffer occupancy, and what does each part mean? ::@:: A flat piece at $R_{\min}$ up to $r$, a straight ramp across the cushion of size $cu$, then a flat piece at $R_{\max}$ running on to $b_{\max}$.

## what the rule leaves open

A region is not a measurement. What it protects is the client's freedom to change rate, and the rule holds at every occupancy inside the region. A region's width comes from analysis, not from the occupancy at the moment of reading.

Two things follow from that. The upper reservoir's extent is drawn as a brace but given no symbol. And the corner where the cushion meets the upper reservoir is drawn as a curve, with no rule in its place: a sharp corner there would mean that one extra second of buffer buys an arbitrary jump in bitrate, and nothing in the curve supports that.

---

Flashcards for this section are as follows:

- what does a reservoir protect? ::@:: The client's freedom to change rate, not a measurement
- what sets the width of a reservoir? ::@:: Analysis, not the occupancy at the moment of reading
- how far does the upper reservoir extend in the notation? ::@:: It has no symbol. The brace is drawn, but the extent is never named
- why is the corner where the cushion meets the upper reservoir drawn as a curve? ::@:: Because a sharp corner there would mean one extra second of buffer buys an arbitrary jump in bitrate, and nothing in the curve supports that

## discrete rates

The available bitrates are a discrete ladder, $R_{\min}$, $R_1$, $R_2$, $R_3$, $R_{\max}$. By default the client stays at the current bitrate, and switches only when the rule crosses above or below the boundary for a neighbouring bitrate. $f$ is the bitrate selection curve above: it maps the buffer occupancy to the rate the rule would choose. The whole selection is:

```text
Input:  Rate_prev  the previously used video rate
        Buf_now   the current buffer occupancy
        r         the size of reservoir
        cu        the size of cushion
Output: Rate_next the next video rate

Rate_+ = R_max  if Rate_prev = R_max, else the smallest available rate above Rate_prev
Rate_- = R_min  if Rate_prev = R_min, else the largest available rate below Rate_prev

if      Buf_now <= r         then Rate_next = R_min
else if Buf_now >= (r + cu) then Rate_next = R_max
else if f(Buf_now) >= Rate_+ then Rate_next = max{R_i : R_i < f(Buf_now)}
else if f(Buf_now) <= Rate_- then Rate_next = min{R_i : R_i > f(Buf_now)}
else                          Rate_next = Rate_prev
return Rate_next
```

The full BBA adds three things on top of this selection. It has a startup phase analogous to slow start, handles variable bitrate encoding, and works out how large to make the reservoirs.

---

Flashcards for this section are as follows:

- which bitrates, from $R_{\min}$ to $R_{\max}$, does the BBA-0 rule choose between? ::@:: The discrete ladder from $R_{\min}$ through $R_1$, $R_2$ and $R_3$ to $R_{\max}$
- when does the client switch away from its current bitrate? ::@:: Only when the rule crosses above or below the boundary for a neighbouring bitrate. Otherwise it stays where it is
- what does the function f do in the BBA-0 selection? ::@:: It is the bitrate selection curve, mapping the current buffer occupancy to the rate the rule would choose
- when is the rate above the current one set to $R_{\max}$? ::@:: When the current rate is already $R_{\max}$. Otherwise it is the smallest available rate above the current one
- what three extensions does the full BBA add to the BBA-0 selection? ::@:: A startup phase analogous to slow start, handling of variable bitrate encoding, and analysis of how large to make the reservoirs

## how BBA performed in the 2020 Puffer study

The Stanford Puffer Project gives people TV for free, so its researchers can test rate adaptation algorithms on live traffic.

Their 2020 study compared many such algorithms and found BBA among the best, though they argue their own algorithm Fugu is better.

The results are drawn as two panels of error-bar scatter. Both plot the same two measures: time spent stalled in percent, and average SSIM in dB. A grey "Better QoE" arrow points up and to the right, and the stall axis is reversed, so lower values plot further right.

- "All sessions": "244,028 streams / 3.8 stream-years"
- "Slow network paths (< 6 Mbit/s)": "33,817 streams / 0.5 stream-years"

The two panels do not compare against each other: different traffic mix, different scale. Read off the plotted points, BBA sits at roughly 0.23 % stalled and 16.5 dB on the left panel, and roughly 2.8 % stalled and 14.5 dB on the right.

Fugu is further right on stall in both panels, and both Pensieve variants sit far down on both measures.

---

Flashcards for this section are as follows:

- what did the 2020 Puffer study find about BBA? ::@:: That it stayed among the best of the many algorithms compared. The study argues its own Fugu is better
- what two measures does the Puffer comparison plot? ::@:: Time spent stalled in percent, and average SSIM in dB
- why does the time-spent-stalled axis of the Puffer comparison run backwards? ::@:: Less time stalled is better, so the better values are plotted to the right
- why do the two panels of the Puffer comparison not compare against each other? ::@:: They cover different traffic and a different scale, all sessions against network paths below 6 Mbit/s
- read off the left panel: roughly where does BBA sit? ::@:: Roughly 0.23 % stalled and 16.5 dB
- read off the right panel: roughly where does BBA sit? ::@:: Roughly 2.8 % stalled and 14.5 dB
- how do Fugu and the Pensieve variants compare with BBA? ::@:: Fugu is further right on stall in both panels, and both Pensieve variants sit far down on both measures

## references

- Huang, T.-Y., et al. (2014). A buffer-based approach to rate adaptation: evidence from a large video streaming service. In _Proc. ACM SIGCOMM_.
