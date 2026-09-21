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

The Mathis equation predicts the throughput a TCP Reno connection settles into when segments are lost at a steady rate, from the segment size, the round-trip time, and the loss probability. The loss rate enters under a square root, so it has to worsen greatly before the throughput falls much.

---

Flashcards for this section are as follows:

- overview ::@:: The Mathis equation predicts the throughput of a TCP Reno connection from the segment size, the round-trip time, and the loss probability.
- why the square root matters: what does the $1/\sqrt{p}$ term say about the cost of a lossy path? ::@:: That throughput falls only with the square root of the loss probability.

## the equation and its terms

The equation reads $$\text{throughput} = \frac{MSS}{RTT} \cdot \frac{C}{\sqrt{p}}$$ with $MSS$ the maximum segment size, $RTT$ the round-trip time, $p$ the loss probability, and $C$ a constant of proportionality. It is a steady-state result for a connection already settled into congestion avoidance, so $p$ is a rate rather than a count of losses. $C$ depends on how the protocol reacts to loss, and it is the one term the equation leaves open.

---

Flashcards for this section are as follows:

- the equation relating throughput to $MSS$, $RTT$, $C$, and $p$ ::@:: $\text{throughput} = (MSS/RTT) \cdot (C/\sqrt{p})$.
- meaning of $p$: what does the loss probability $p$ measure? ::@:: The rate at which segments are lost.
- the constant $C$: what does its value depend on? ::@:: How the protocol reacts to loss.
- the other term in the numerator: which quantity sits in the numerator besides $C$? ::@:: The maximum segment size $MSS$.
- what the path sets: which of $MSS$, $RTT$, and $p$ does the path set? ::@:: The round-trip time $RTT$.
- steady state: what does treating the loss probability $p$ as a rate assume about the connection? ::@:: That it has settled into congestion avoidance.

## measuring the constant

$C$ can be measured rather than assumed. Holding the segment size and the round-trip time fixed, the sender varies the link's loss probability and measures the throughput each value produces. Plotting throughput against $1/\sqrt{p}$ turns the equation into a straight line through the origin with slope $(MSS/RTT) \cdot C$, which a fitted line recovers; the Pearson correlation coefficient then says how well the points follow it. Each loss probability has to be averaged over many runs, since one run depends on where in its cycle the connection happened to be. Each transfer must also last long enough to get past slow start, before which the throughput reflects the window's growth rather than the loss rate.

---

Flashcards for this section are as follows:

- measurement setup: to measure $C$, what varies, what stays fixed, and what is measured? ::@:: The loss probability varies while the segment size and round-trip time stay fixed, and the throughput is measured for each value.
- the plot: what is plotted against $1/\sqrt{p}$? ::@:: The measured throughput.
- the slope: on a plot of throughput against $1/\sqrt{p}$, what does the slope of the fitted line equal? ::@:: $(MSS/RTT) \cdot C$.
- line fit: why does fitting a line to the points say something about the equation? ::@:: The equation predicts a straight line through the origin, so points that follow it corroborate it.
- Pearson correlation: what does the Pearson coefficient between throughput and $1/\sqrt{p}$ measure? ::@:: How closely the measured points follow a straight line.
- repetition: why must each loss probability be measured many times? ::@:: A single run is dominated by where in its congestion cycle the connection happened to be.
- transfer length: why must each transfer run for several seconds before its throughput counts? ::@:: The connection has to get past slow start, since before that its throughput reflects the growth of the window rather than the loss rate.

## references

- Mathis, M., Semke, J., Mahdavi, J., & Ott, T. (1997). The macroscopic behavior of the TCP congestion avoidance algorithm. _ACM SIGCOMM Computer Communication Review_, _27_(3), 67-82. <https://doi.org/10.1145/263932.264023>
    - Source of the throughput equation.
