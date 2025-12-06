---
aliases:
  - ELEC 4110 channel access method
  - ELEC4110 channel access method
  - channel access method
tags:
  - flashcard/active/special/academia/HKUST/ELEC_4110/channel_access_method
  - language/in/English
---

# channel access method

- see: [general/channel access method](../../../../general/channel%20access%20method.md)

## orthogonal resource partitioning

In a multi‑user wireless system the _orthogonal resource partitioning_ principle ensures that each user occupies a distinct slice of the shared medium so that signals can be separated at the receiver.  The base station observes only the superposed signal $$y(t)=\sum_{k=1}^{K} x_k(t)+n(t),$$ where $x_k(t)$ is the contribution from user $k$ and $n(t)$ denotes additive noise.  Because all users transmit simultaneously, some form of coordination is required to guarantee that their signals remain orthogonal at the receiver; otherwise separation would be ambiguous.

The base station must _separate_ the individual user streams from the aggregate observation $y(t)$.  This separation is feasible only if the users employ distinct, mutually orthogonal resources.  Consequently, the network protocol must coordinate resource allocation among the $K$ users—assigning them different frequencies, time slots, or spreading codes.

Three widely adopted orthogonal multiple‑access strategies partition the shared medium in different domains:

1. _Frequency Division Multiple Access (FDMA)_ ::@:: – the spectrum is divided into non‑overlapping frequency bands; each user occupies a unique band.  
2. _Time Division Multiple Access (TDMA)_ ::@:: – users are assigned distinct time slots within a repeating frame; the same frequency channel is reused in successive slots.  
3. _Code Division Multiple Access (CDMA)_ ::@:: – users transmit simultaneously over the full bandwidth but use orthogonal (or almost orthogonal) spreading codes to distinguish their signals.

These schemes embody the principle that each user's resource allocation must be _orthogonal_ to those of all others, enabling clean signal separation at the base station.

## time division multiple access

In a TDMA system the base station schedules users cyclically.  A single radio front end at the base transceiver can serve all scheduled users: after finishing one slot it immediately switches to the next.  The maximum data rate that a user experiences is therefore determined by its share of the cycle; if the cycle length is $T$ and each user receives a fraction $\frac{1}{N}$ of that time, the _physical_ peak rate for a user equals $$R_{\text{peak} } = N\, R_{\text{data} } \,,$$ where $R_{\text{data} }$ is the nominal data rate required per user.

Because each user's transmission occupies only a short burst of time, the channel can be reused rapidly.  This allows many users to share the same frequency band with minimal hardware complexity at the base station—only one transceiver is needed regardless of $N$.

The TDMA approach favours compactness: a single transceiver suffices for all users, making the base‑station equipment smaller and cheaper.   However, the _peak_ rate seen by a user can be much higher than its average data rate; if the modulation scheme is not robust to such peaks, an equaliser may be required at the receiver.

## frequency division multiple access

Frequency Division Multiple Access is a radio‑access method in which the total allocated spectrum $W$ is partitioned into _N_ non‑overlapping frequency slots. Each slot therefore carries a channel of bandwidth $\frac{W}{N}$ and is assigned to one mobile terminal.  Because every user transmits on a distinct frequency band, the channels are _orthogonal_; no two users interfere with one another's signals.

The allocation scheme is static: once a mobile has been granted a particular slot it continues to use that same frequency until its session ends or the network reconfigures the partitioning.  This contrasts with time‑division schemes where the same spectrum is shared in successive time slots rather than across separate frequencies.

FDMA typically requires a separate radio front end for each occupied channel at the base station.  Consequently, the number of transceivers grows linearly with _N_, which can lead to bulky hardware when many users are served simultaneously.  On the other hand, because each user's signal occupies its own frequency band, the receiver does not need a complex equaliser; the link‑level processing is comparatively simple.

## FDMA vs. TDMA

Comparing _FDMA_ and _TDMA_ in a 15&nbsp;MHz band where each user needs 25&nbsp;kbps with one bit per symbol: _FDMA_ allocates a fixed bandwidth (~25&nbsp;kHz) to each user; up to about 600 users could be served if the spectrum is perfectly divided. _TDMA_ shares the full 15&nbsp;MHz among all users in separate time slots; under the average rate constraint of 25&nbsp;kbps, 600 users could be served as at most 600 time slots can be created, matching the FDMA result. We see under identical assumptions, FDMA and TDMA support roughly the same number of users; neither is inherently "better" in capacity.

The choice between FDMA and TDMA usually hinges on implementation factors: FDMA underlies first‑generation analog mobile systems, while TDMA (e.g., GSM) forms the basis of 2G digital networks. Real‑world performance differences arise from protocol overhead, synchronization, and hardware constraints rather than raw channel count.

Real filters have non‑ideal roll‑off, requiring guard bands between FDMA channels. TDMA needs guard times to accommodate different propagation delays among users. These overheads reduce the theoretical maximum number of usable channels and must be accounted for during network planning.

## hybrid TDMA/FDMA

Assume a channel coherence bandwidth of 200&nbsp;kHz and prohibits equalizers. Each subchannel must therefore stay ≤200&nbsp;kHz to remain flat‑fading. Splitting the 15&nbsp;MHz band into at least 75 such subchannels, the design uses a _hybrid TDMA/FDMA_ scheme: _Carriers_ (groups of subchannels) are formed; each carrier is then divided in time by TDMA. This hybrid arrangement allows fewer RF units at the base station while respecting the flat‑fading constraint and avoiding equalization.

## code division multiple access

_CDMA_ (Code Division Multiple Access) is a spread‑spectrum technique in which each user's data are multiplied by a unique pseudorandom noise (PN) sequence before transmission. There are two types of CDMA: deterministic CDMA and random CDMA.

CDMA underpins modern cellular systems such as GSM's 2G and UMTS's 3G architectures, where it forms the basis of both uplink and downlink signalling.

### deterministic CDMA

In deterministic CDMA the PN sequences form an orthogonal set, i.e. $$\langle c_i(t),c_j(t)\rangle = \frac 1 N \sum_t c_i(t) c_j^*(t) = 0 \quad (i\neq j)\,,$$ where $N$ is the number of chips in a symbol. The _spreading factor_ is the _maximum_ number of simultaneous users that can be supported, which is the _upper limit_ to the size of this orthogonal code set.

With deterministic CDMA, the system is _code-limited_: capacity depends on how many orthogonal codes can be generated.

A necessary condition is perfect _synchronisation_ between the transmitters and receivers; otherwise the orthogonality is lost.   Because of these constraints deterministic CDMA is usually applied only on the _forward link_ or _downlink_ (from base station to mobile) because synchrony is easy to maintain. Mobile must know propagation delay $\tau$ and send a pilot so the base station can estimate it each frame. The required accuracy is within a fraction of a chip (~1&nbsp;µs), far tighter than typical millisecond estimates; thus many pilots are needed. The extra uplink pilot overhead scales with the number of users, which does not scale well with many users.

For example, a base station transmits two users simultaneously, each with a distinct orthogonal code (using deterministic CDMA), and ensures both chip sequences start at the same instant. Mobile receivers use a pilot signal to find the correct timing accurate within a fraction of a chip (~1&nbsp;µs); once aligned, despreading with their own code (using random CDMA) reconstructs the intended symbol while the other user's contribution cancels out (thanks to orthogonality).

### random CDMA

Random CDMA relaxes the requirement of strict orthogonality.  The PN sequences are chosen randomly and independently, so $$\langle c_i(t),c_j(t)\rangle = \frac 1 N \sum_t c_i(t) c_j^*(t) \approx 0 \quad (i \neq j) \,,$$ where $N$ is the number of chips in a symbol. The _normalized_ cross-correlation has an _expected value_ of zero and a _variance_ that diminishes as $N$ grows: $$\operatorname{Var}(\langle c_i(t), c_j(t)\rangle) = \frac 1 {\sqrt N} \,.$$ Actually, it can be proved that the normalized cross-correlation is almost surely bounded as $N$ grows: $$\lvert \langle c_i(t), c_j(t) \rangle \rvert \le \sqrt{\frac {2 \log \log N} N} \;\text{a.s.} \,.$$

With random CDMA, the number of usable codes is no longer limited; you can generate thousands of distinct sequences. Cross‑correlation remains small even with timing offsets, so R‑CDMA works naturally in asynchronous uplink.

Although the channels are not perfectly orthogonal and/or synchronous, each user's signal is still _despread_ by correlating with its own PN code. However, there is residual interference from other users, which makes it _interference-limited_. The interference is reduced by the _processing gain_ $$G_{\text{proc} } = \frac{T_{\text{samp} } }{T_{\text{chip} } },$$ where $T_{\text{samp} }$ the symbol period and $T_{\text{chip} }$ is the chip duration. Random CDMA therefore supports far more users than deterministic schemes; it is the preferred choice for the _reverse link_ or _uplink_ (mobile to base station) because the system can support many more users without costly timing advance.

Because channels are not perfectly orthogonal, a user transmitting at high power can drown out weaker users—a phenomenon called the _near–far problem_.  The optimal operating point is achieved when all users' _received powers_ are equal.  This is enforced by a _power control_ algorithm that adjusts each transmitter's output to compensate for path loss and fading.

### effective SINR of random CDMA

Random CDMA uses DSSS. The spread spectrum introduces a _processing gain_ $\text{PG} = W_{\text{spread} }/W_{\text{non-spread} }$.  The _signal‑to‑interference‑plus‑noise ratio_ (SINR) _per bit_ at each finger is multiplied by this factor: $$\text{SINR}_{\text{effective} } = \frac {\lvert a_i \rvert^2 E_b} {N_0 + \frac {(\text{\# users}) \cdot \lvert a_i \rvert^2 E_b} {\text{PG} } } \approx \frac {\text{PG} } {\text{\# users} } \,,$$ where $E_b$ is the energy per bit, $N_0$ is the noise spectral density, and $(\text{\# users})$ refers to number of _other_ users (excluding self) that can _interfere_ with the current user. The final approximation holds well for high SNR situations (so $N_0$ is small relative to $E_b$) in which the error rate becomes interference-limited, and the _BER floor_ from ISI becomes the limiting factor.

In an interference‑limited regime ($s \gg \sigma^2$) and for large number of users $K$, the above formula also gives the maximum number of users random CDMA can support: $$K_{\max} \approx \frac{N}{\gamma_{\text{req} } }$$ where $\gamma_{\text{req} }$ is the minimum SINR needed by the physical‑layer (set by modulation, coding, fading).

## random access

In a random‑access or contention‑based channel access method, each device independently decides when to transmit without coordination from a central scheduler. The most widely deployed example is Wi‑Fi's CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance), where a node first senses the medium; if it detects no ongoing transmission it proceeds, otherwise it defers and retries after a random back‑off period. This "listen‑before‑talk" discipline mirrors everyday conversation etiquette—people wait until others finish speaking before interjecting—and it allows multiple users to share the same channel without explicit time or frequency allocation.

Random access contrasts with centralized schemes such as TDMA, FDMA, CDMA and OFDMA, where a base station or controller assigns distinct time slots, frequencies, spreading codes or subcarriers to each user. While these coordinated methods can offer higher spectral efficiency in environments with predictable traffic patterns, they require dedicated signaling and scheduling infrastructure. In decentralized random access, the trade‑off is lower coordination overhead at the expense of potentially higher collision probability and reduced capacity when many users contend simultaneously.
