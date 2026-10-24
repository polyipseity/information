---
aliases:
  - CUBIC
  - CUBIC TCP
  - ELEC 3120 CUBIC TCP
  - ELEC3120 CUBIC TCP
  - HKUST ELEC 3120 CUBIC TCP
  - HKUST ELEC3120 CUBIC TCP
  - TCP CUBIC
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/CUBIC_TCP
  - language/in/English
---

# CUBIC TCP

CUBIC TCP is a congestion control algorithm that keeps Reno's loss signal but replaces its straight-line window growth with a cubic curve. The window races back toward the size it had before the last loss, then flattens as it reaches that size, so a flow spends its time near the path's capacity rather than climbing there one segment per round trip. Its growth depends on elapsed time rather than on the number of round trips, which keeps flows of different round-trip times on even terms.

---

Flashcards for this section are as follows:

- CUBIC TCP: how does the window growth of CUBIC TCP differ from that of TCP Reno? ::@:: The window follows a cubic curve in time instead of growing linearly by one segment per round trip.
- the shape: what does the cubic curve make the window do after a loss? ::@:: It rises quickly toward the window size at the previous loss, then flattens as it reaches that size.
- even terms: why do two flows with different round trip times share a path more evenly under CUBIC TCP than under TCP Reno? ::@:: The window grows with elapsed time rather than with round trips, so a short and a long round trip gain the same window in the same second.

## window growth

The window follows $W_{\text{cubic}} = C(t - K)^3 + W_{\max}$, with $C$ a scaling factor, $t$ the time since the last reduction, and $W_{\max}$ the window at that reduction. $K = \sqrt[3]{W_{\max}\beta/C}$ is the time the curve takes to return to $W_{\max}$, with $\beta$ the multiplicative decrease factor. Before $K$ the curve sits below $W_{\max}$ and flattens as it rises. After $K$ it turns upward again.

Take a window that reached 100 segments before the loss, a decrease factor of $\beta = 0.8$ that matches the 20% cut, and a scaling factor of $C = 0.4$ segments per second cubed. Then $K = \sqrt[3]{100 \times 0.8 / 0.4} = \sqrt[3]{200} \approx 5.85$ s, so the window returns to 100 segments 5.85 s after the loss and stands at 180 segments at $2K$, about 11.7 s.

One form writes $K$ with $\beta$ in the numerator; RFC 8312 writes $K = \sqrt[3]{W_{\max}(1-\beta)/C}$ instead. The standard form starts the curve at the window the loss left behind, $W_{\max}\beta$, whereas the $\beta$ form starts it lower, at $C K^3$ below $W_{\max}$, which is 20 segments for the numbers above rather than the 80 that a 20% cut leaves. The shape of the curve, and the argument that follows from it, are the same either way.

Between $K$ and $2K$ the curve adds 80 segments, and between $2K$ and $3K$ it adds 560, seven times as many over the same stretch of time. At $3K$, 17.5 s after the loss, the curve stands at 740 segments, and at $4K$, 23.4 s, at 2,260 segments. The flow spends little of its time near $W_{\max}$ and most of it far above it, where the capacity of a long path lies.

Because the curve runs on elapsed time, two flows on one path grow alike whatever their round trips. A flow with a 10 ms round trip and one with a 100 ms round trip add the same number of segments in the same second. Reno gives the 10 ms flow 100 segments a second and the 100 ms flow 10, so the faster flow takes a larger share of the path.

---

Flashcards for this section are as follows:

- window function: which formula gives the CUBIC TCP window $t$ seconds after a reduction? ::@:: $W_{\text{cubic}} = C(t - K)^3 + W_{\max}$.
- the symbols: in that formula, what are $C$, $t$, and $W_{\max}$? ::@:: $C$ is a scaling factor, $t$ the time since the last reduction, and $W_{\max}$ the window at that reduction.
- K: what does $K = \sqrt[3]{W_{\max}\beta/C}$ measure? ::@:: The time the window takes to grow back to $W_{\max}$, with $\beta$ the decrease factor.
- the return time: with $W_{\max} = 100$ segments, a decrease factor of $\beta = 0.8$ and a scaling factor of $C = 0.4$ segments per second cubed, how long does the window take to return to $W_{\max}$? ::@:: $K = \sqrt[3]{100 \times 0.8 / 0.4} = \sqrt[3]{200} \approx 5.85$ seconds.
- the window at twice K: with $W_{\max} = 100$ segments, a decrease factor of $\beta = 0.8$ and a scaling factor of $C = 0.4$ segments per second cubed, what window does the curve reach at $t = 2K$? ::@:: $t - K = K$, so $W = C K^3 + W_{\max} = W_{\max}(1 + \beta) = 100 \times 1.8 = 180$ segments.
- the window at three K: with $W_{\max} = 100$ segments, $\beta = 0.8$ and $C = 0.4$, what window does the curve reach at $t = 3K$? ::@:: $t - K = 2K$, so $W = C(2K)^3 + W_{\max} = 8 \times 80 + 100 = 640 + 100 = 740$ segments.
- the standard form: which formula does Request for Comments (RFC) 8312 give for $K$, against the $\beta$ form $K = \sqrt[3]{W_{\max}\beta/C}$? ::@:: $K = \sqrt[3]{W_{\max}(1 - \beta)/C}$, which starts the curve at the window the loss left behind, $W_{\max}\beta$.
- the starting window: with $W_{\max} = 100$ segments, $\beta = 0.8$ and $C = 0.4$ segments per second cubed, what window does each form of the cubic curve start from at $t = 0$? ::@:: The $\beta$ form starts at $W_{\max} - C K^3 = 100 - 0.4 \times 200 = 100 - 80 = 20$ segments, while the standard form starts at $W_{\max}\beta = 80$ segments.
- the window at four K: with $W_{\max} = 100$ segments, $\beta = 0.8$ and $C = 0.4$ segments per second cubed, what window does the curve reach at $t = 4K$? ::@:: $t - K = 3K$, so $W = C(3K)^3 + W_{\max} = 27 \times 80 + 100 = 2{,}160 + 100 = 2{,}260$ segments.
- Reno's shares: on a path shared by a flow with a $10\text{ ms}$ round trip and one with a $100\text{ ms}$ round trip, how many segments a second does TCP Reno give each? ::@:: $1\text{ s}/0.01\text{ s} = 100$ round trips give the $10\text{ ms}$ flow $100$ segments a second, and $1\text{ s}/0.1\text{ s} = 10$ round trips give the $100\text{ ms}$ flow $10$, so the faster flow takes the larger share of the path.

## loss response

A drop cuts the window by 20% rather than by half, so the flow gives up less capacity for the same loss. The reduction deepens to 40% when its estimate of the recent maximum shrinks, which happens when the path itself has got smaller. Holding the old window would then be unfair to everyone else.

A window at 100 segments loses 20 segments to the 20% cut and keeps 80, while the deeper 40% cut takes 40 and leaves 60. Halving the same window would cost 50 segments and leave 50, so the shallower cut returns the least room and puts the flow back near its old size soonest. Repeated losses separate the two rules further. After two losses Reno's window has fallen from 100 segments to 25, while the CUBIC TCP window has fallen to 64, so the flow keeps more than twice the window Reno would give it.

---

Flashcards for this section are as follows:

- normal reduction: by how much does CUBIC TCP cut the window at a loss? ::@:: 20%.
- deeper reduction: when does CUBIC TCP cut the window by 40% instead? ::@:: When its estimate of the window at the previous maximum shrinks.
- the deeper cut: a window of $100$ segments meets the deeper $40\%$ cut; what window is left? ::@:: $100 \times (1 - 0.4) = 100 \times 0.6 = 60$ segments.
- repeated losses: a window of $100$ segments meets two losses; what window is left under CUBIC TCP, and under TCP Reno? ::@:: $100 \times 0.8 = 80$, then $80 \times 0.8 = 64$ segments under CUBIC TCP, against $100/2 = 50$ then $50/2 = 25$ under TCP Reno.
- the 20 percent cut: a window of $100$ segments meets the usual $20\%$ reduction; how many segments are lost and how many kept? ::@:: $100 \times 0.2 = 20$ segments lost and $100 - 20 = 80$ kept.

## long fat paths

Reno's linear growth fails on long, fat paths. A 10 Gbps path with a 100 ms round trip holds 83,333 segments in flight, and climbing there one segment per round trip takes 83,333 round trips, or 2.3 hours. CUBIC's curve covers that distance in a fraction of the time. The flattening near $W_{\max}$ then keeps it from overshooting into a queue that would delay everything behind it.

From a window of 80 segments after the loss and a $W_{\max}$ of 100 segments, reaching 83,333 segments takes Reno 83,253 round trips, which is 8,325 s, or 2.3 hours, on a path with a 100 ms round trip. With the same scaling factor of $C = 0.4$, CUBIC covers the distance in about 65 s after the loss, which is about 128 times faster than Reno's climb. For the first seconds the linear climb is ahead: at $t = 12$ s the curve stands at 193 segments while Reno's window stands at 200, and a second later the curve is at 246 and Reno's at 210. What the curve buys is the distance, not the first few seconds.

---

Flashcards for this section are as follows:

- Reno's failure: which property of Reno's growth makes it hopeless on a long, fat path? ::@:: The growth is linear, one segment per round trip, so reaching a huge window takes hours.
- the 10 Gbps case: how many $1500$-byte segments must be in flight for $10\text{ Gbps}$ over a $100\text{ ms}$ round trip? ::@:: $10\text{ Gbps} = 1.25$ GB/s, so $1.25 \times 10^9 \times 0.1 = 1.25 \times 10^8$ bytes are in flight, and $1.25 \times 10^8 / 1500 = 83{,}333$ segments.
- the comparison: after a loss leaves the window at $80$ segments with $W_{\max} = 100$ segments, how long does each algorithm take to reach $500$ segments on a path with a $100\text{ ms}$ round trip, with $C = 0.4$ segments per second cubed for CUBIC TCP? ::@:: TCP Reno needs $500 - 80 = 420$ round trips at $0.1\text{ s}$ each, which is $42$ seconds, while CUBIC TCP needs $0.4(t - K)^3 = 400$, so $(t - K)^3 = 1{,}000$, $t = 5.85 + 10 = 15.85$ s, about $15.9$ seconds.
- the ratio of climb times: after a loss leaves the window at $80$ segments, how much faster does CUBIC TCP reach $83{,}333$ segments than TCP Reno's $8{,}325$ s climb on a path with a $100\text{ ms}$ round trip? ::@:: About $128$ times faster, since $8{,}325 / 65 = 128$: $65$ seconds against $8{,}325$ seconds.
- Reno's round trips: from a window of $80$ segments to $83{,}333$ segments at one segment per round trip, how many round trips and how much time does TCP Reno need on a path with a $100\text{ ms}$ round trip? ::@:: $83{,}333 - 80 = 83{,}253$ round trips, at $0.1\text{ s}$ each $8{,}325$ s, which is $8{,}325 / 3{,}600 \approx 2.3$ hours.
