---
aliases:
  - ELEC 3120 Mathis equation
  - ELEC3120 Mathis equation
  - HKUST ELEC 3120 Mathis equation
  - HKUST ELEC3120 Mathis equation
  - Mathis equation
  - Mathis's hypothesis
  - throughput equation
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/Mathis_equation
  - language/in/English
---

# Mathis equation

The Mathis equation predicts the throughput a TCP Reno connection settles into when segments are lost at a steady rate, from the segment size, the round-trip time, and the loss probability. The loss rate enters under a square root, so it must worsen greatly before throughput falls much.

---

Flashcards for this section are as follows:

- what it predicts: what does the Mathis equation predict, and from which quantities? ::@:: The Mathis equation predicts the throughput of a TCP Reno connection from the segment size, the round-trip time, and the loss probability.
- why the square root matters: what does the $1/\sqrt{p}$ term say about the cost of a lossy path? ::@:: That throughput falls only with the square root of the loss probability.

## equation and terms

The equation reads $\text{throughput} = \frac{MSS}{RTT} \cdot \frac{C}{\sqrt{p}}$ with $MSS$ the maximum segment size, $RTT$ the round-trip time, $p$ the loss probability, and $C$ a constant of proportionality. It holds at steady state, once the connection has settled into congestion avoidance, so $p$ is a rate rather than a count of losses. $C$ depends on how the protocol reacts to loss, and it is the only term left open. The answer is an upper bound, not a forecast: it assumes no retransmission timeout ever fires and no shortfall in the receiver window or the sender's supply of data, so a real connection gets less. No term in it stands for the link's bandwidth: only $MSS$, $RTT$, $C$ and $p$ appear.

A worked case: with $MSS = 1460$ bytes, $RTT = 0.1$ s, $p = 0.01$, and $C = 1.22$, the value usually taken for Reno, the term $MSS/RTT$ is $14600$ bytes per second and $C/\sqrt{p}$ is $12.2$, so the throughput is $178{,}120$ bytes per second. The same path with $p = 0.001$ gives $563{,}000$ bytes per second, 4.5 Mbit/s, so a tenfold fall in losses buys about three times the throughput. $p = 0.05$ on the same path gives $79{,}671$ bytes per second, 0.64 Mbit/s, since the loss term $C/\sqrt{p}$ falls to $5.457$.

---

Flashcards for this section are as follows:

- the equation relating throughput to $MSS$, $RTT$, $C$, and $p$ ::@:: $\text{throughput} = (MSS/RTT) \cdot (C/\sqrt{p})$.
- meaning of $p$: what does the loss probability $p$ measure? ::@:: The rate at which segments are lost.
- the constant $C$: what does its value depend on? ::@:: How the protocol reacts to loss.
- the other term in the numerator: which quantity other than $C$ sits in the numerator of the throughput expression? ::@:: The maximum segment size $MSS$.
- what the path sets: which of $MSS$, $RTT$, and $p$ does the path set? ::@:: The round-trip time $RTT$.
- steady state: what does treating the loss probability $p$ as a rate assume about the connection? ::@:: That it has settled into congestion avoidance.
- upper bound: what does the equation bound, and which two shortfalls does it assume away? ::@:: An upper bound on the transfer rate, assuming no retransmission timeout and that the receiver window and the sender's data never run short, so a real connection gets less.
- no term for the link rate: which quantity of the path does the equation not contain, and what follows for a faster link? ::@:: The link's bandwidth; a faster link alone does not raise the predicted throughput, which depends only on segment size, round trip, the constant and the loss probability.
- worked case: with the maximum segment size $MSS = 1460$ bytes, the round-trip time $RTT = 0.1$ s, the loss probability $p = 0.01$, and $C = 1.22$, what throughput does the Mathis equation give? ::@:: $14600 \times (1.22/0.1) = 178{,}120$ bytes per second, about 1.4 Mbit/s.
- a lower loss rate: with the maximum segment size $MSS = 1460$ bytes, the round-trip time $RTT = 0.1$ s, the loss probability $p = 0.001$, and $C = 1.22$, what throughput does the Mathis equation give? ::@:: $1.22/\sqrt{0.001} = 38.6$, so $14600 \times 38.6 \approx 563{,}000$ bytes per second, about 4.5 Mbit/s.
- a higher loss rate: with the maximum segment size $MSS = 1460$ bytes, the round-trip time $RTT = 0.1$ s, the loss probability $p = 0.05$, and $C = 1.22$, what throughput does the Mathis equation give? ::@:: $1.22/\sqrt{0.05} = 5.457$, so $14600 \times 5.457 \approx 79{,}671$ bytes per second, about 0.64 Mbit/s.
- the segment-to-round-trip term: in the worked case with the maximum segment size $MSS = 1460$ bytes and the round-trip time $RTT = 0.1$ s, what is the value of $MSS/RTT$? ::@:: $1460\text{ bytes} / 0.1\text{ s} = 14{,}600$ bytes per second.
- the loss term: with the constant $C = 1.22$ and the loss probability $p = 0.01$, what is the value of $C/\sqrt{p}$? ::@:: $12.2$, since $1.22$ divided by $\sqrt{0.01} = 0.1$.

## measuring the constant

$C$ can be measured rather than assumed. Holding the segment size and the round-trip time fixed, the sender varies the link's loss probability and measures the throughput each value produces. Throughput plotted against $1/\sqrt{p}$ should lie on a straight line through the origin with slope $(MSS/RTT) \cdot C$. With $MSS = 1460$ bytes and $RTT = 0.1$ s the fitted line has slope $14600 \times 1.22 = 17{,}812$ bytes per second, so a point at $1/\sqrt{p} = 10$ sits at $178{,}120$ bytes per second. The Pearson correlation coefficient says how closely the points follow that line. Each loss probability is averaged over many runs, since one run depends on where in its cycle the connection happened to be. Each transfer must also last long enough to get past slow start, before which the throughput reflects the growth of the window rather than the loss rate.

---

Flashcards for this section are as follows:

- measurement setup: to measure $C$, what varies, what stays fixed, and what is measured? ::@:: The loss probability varies while the segment size and round-trip time stay fixed, and the throughput is measured for each value.
- the slope: on a plot of throughput against $1/\sqrt{p}$, what does the slope of the fitted line equal? ::@:: $(MSS/RTT) \cdot C$.
- Pearson correlation: what does the Pearson coefficient between throughput and $1/\sqrt{p}$ measure? ::@:: How closely the measured points follow a straight line.
- repetition: why must each loss probability be measured many times? ::@:: A single run is dominated by where in its congestion cycle the connection happened to be.
- transfer length: why must each transfer run for several seconds before its throughput counts? ::@:: The connection has to get past slow start, since before that its throughput reflects the growth of the window rather than the loss rate.
- another point on the line: with the maximum segment size $MSS = 1460$ bytes and the round-trip time $RTT = 0.1$ s, what throughput does the fitted line of slope $17{,}812$ give at $1/\sqrt{p} = 20$? ::@:: $17{,}812 \times 20 = 356{,}240$ bytes per second.
- the fitted slope: with the maximum segment size $MSS = 1460$ bytes, the round-trip time $RTT = 0.1$ s, and $C = 1.22$, what slope does the fitted line have? ::@:: $14600 \times 1.22 = 17{,}812$ bytes per second.
- a point at $1/\sqrt{p} = 10$: on the fitted line of slope $17{,}812$ bytes per second, what throughput sits at $1/\sqrt{p} = 10$? ::@:: $17{,}812 \times 10 = 178{,}120$ bytes per second.
- a point at $1/\sqrt{p} = 5$: on the fitted line of slope $17{,}812$ bytes per second, what throughput sits at $1/\sqrt{p} = 5$? ::@:: $17{,}812 \times 5 = 89{,}060$ bytes per second.

## average window

With $W$ the window at which the loss occurred, congestion avoidance climbs from $W/2$ back to $W$ before halving again, so the window spends its time between those two values and averages $3W/4$ in flight. The average throughput is $\frac{3}{4} \cdot \frac{W}{RTT}$. A connection that loses a packet at a window of $W = 20$ segments averages 15 in flight, which is 22,500 bytes of 1500-byte segments, or 225,000 bytes per second over a 100 ms round trip, 1.8 Mbit/s. A window of 30 segments averages 22.5 segments in flight, which is 33,750 bytes and 337,500 bytes per second over the same round trip, 2.7 Mbit/s.

---

Flashcards for this section are as follows:

- average window: a TCP Reno connection loses a packet when its window is $W$; what is its average window in flight? ::@:: $3W/4$, halfway between the $W$ it reached and the $W/2$ it fell to.
- average throughput: with the window averaging $3W/4$ over a round trip of $RTT$, what throughput does the connection achieve? ::@:: $\frac{3}{4} \cdot \frac{W}{RTT}$ bytes per second.
- what the average assumes: which two parts of the connection does the average leave out? ::@:: Slow start, and any time the sender has nothing to send.
- worked average: with a window $W = 20$ segments of 1500 bytes and a round-trip time $RTT = 0.1$ s, what average throughput does the $3/4$ rule give? ::@:: $15 \times 1500 / 0.1 = 225{,}000$ bytes per second, 1.8 Mbit/s.
- a larger window: with a window $W = 30$ segments of 1500 bytes and a round-trip time $RTT = 0.1$ s, what average throughput does the $3/4$ rule give? ::@:: $22.5 \times 1500 / 0.1 = 337{,}500$ bytes per second, 2.7 Mbit/s.

## high bandwidth problem

More bandwidth alone does not raise the throughput the equation allows. Delivering 10 Gbps with 1500-byte segments over a 100 ms round trip needs 83,333 segments in flight, and the equation then requires a loss probability near $2.1 \times 10^{-10}$, one lost packet in about five billion. That count is the bandwidth-delay product: $10^{9}$ bits over the 12,000 bits in a segment is 83,333, or 85,616 with 1460-byte segments. At 1 Gbps over the same 100 ms round trip the count falls to 8,333 segments of 1500 bytes, or 8,562 of 1460 bytes. Since the loss probability enters under a square root, a tenth of the rate asks for a hundred times the loss probability, about $2.1 \times 10^{-8}$, one lost packet in about 47 million. No real path is that clean, so Reno cannot reach the rate at all.

The window is also slow to recover once cut. Halving from 10 Gbps leaves 5 Gbps, and the linear climb back takes 41,666 round trips, 1.2 hours, during which the connection runs at half the rate it could. Together these two failures make up TCP's high bandwidth problem.

---

Flashcards for this section are as follows:

- segments in flight: how many $1500$-byte segments must be in flight for $10\text{ Gbps}$ over a $100\text{ ms}$ round trip? ::@:: $10^{9}\text{ bits} / 12{,}000\text{ bits} = 83{,}333$ segments.
- segments for a smaller maximum segment size: how many segments of 1460 bytes must be in flight for $10\text{ Gbps}$ over a $100\text{ ms}$ round trip? ::@:: $10^{9}\text{ bits} / 11{,}680\text{ bits} = 85{,}616$ segments.
- a smaller rate: how many 1500-byte segments must be in flight for $1\text{ Gbps}$ over a $100\text{ ms}$ round trip? ::@:: $10^{8}\text{ bits} / 12{,}000\text{ bits} = 8{,}333$ segments.
- smaller segments at 1 Gbps: how many 1460-byte segments must be in flight for $1\text{ Gbps}$ over a $100\text{ ms}$ round trip? ::@:: $10^{8}\text{ bits} / 11{,}680\text{ bits} = 8{,}562$ segments.
- the loss probability for 1 Gbps: what loss probability does the Mathis equation demand for $1\text{ Gbps}$ with $1500$-byte segments and a $100\text{ ms}$ round trip? ::@:: $1.25 \times 10^{8}\text{ B/s} \times 0.1\text{ s} / 1500\text{ B} = 8{,}333$ segments, so $\sqrt{p} = 1.22/8{,}333 = 1.46 \times 10^{-4}$ and $p = 2.1 \times 10^{-8}$, one packet in about 47 million.
- required loss probability: what loss probability does the Mathis equation demand for $10\text{ Gbps}$ with $1500$-byte segments and a $100\text{ ms}$ round trip? ::@:: $1.25 \times 10^{9}\text{ B/s} \times 0.1\text{ s} / 1500\text{ B} = 83{,}333$ segments, so $\sqrt{p} = 1.22/83{,}333 = 1.46 \times 10^{-5}$ and $p = 2.1 \times 10^{-10}$, one packet in about five billion.
- recovery time: after the window halves from the $10\text{ Gbps}$ point of $83{,}333$ segments in flight, how long does the linear climb back take? ::@:: $83{,}333 / 2 = 41{,}666$ round trips of $0.1\text{ s}$, which is $4{,}167\text{ s}$ or about $1.2$ hours.
- what it forces: which change to Transmission Control Protocol (TCP) does TCP's high bandwidth problem call for? ::@:: Replacing the linear window growth with something faster, as CUBIC TCP does.
- the rate while it climbs: after a loss halves the window from the $10\text{ Gbps}$ point, at what rate does the connection run while it climbs back? ::@:: $5\text{ Gbps}$, half of what the path could carry.

## references

- Mathis, M., Semke, J., Mahdavi, J., & Ott, T. (1997). The macroscopic behavior of the TCP congestion avoidance algorithm. _ACM SIGCOMM Computer Communication Review_, _27_(3), 67-82. <https://doi.org/10.1145/263932.264023>
    - Source of the throughput equation.
