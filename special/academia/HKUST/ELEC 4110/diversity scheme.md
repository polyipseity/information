---
aliases:
  - ELEC 4110 diversity scheme
  - ELEC4110 diversity scheme
  - diversity scheme
tags:
  - flashcard/active/special/academia/HKUST/ELEC_4110/diversity_scheme
  - language/in/English
---

# diversity scheme

- see: [general/diversity scheme](../../../../general/diversity%20scheme.md)

In telecommunications, a __diversity scheme__ refers to a method for improving the reliability of a message signal by using two or more communication channels with different characteristics.

## diversity

Typical diversity sources include time diversity, frequency diversity, multipath diversity, and antenna diversity.

### time and frequency diversity

The _coherence time_ $T$ is the interval over which the channel's fading coefficient can be regarded as constant. When a symbol duration $\tau$ satisfies $\tau < T$, successive symbols experience correlated fades; if $\tau > T$, they are effectively independent.

Similarly, the _coherence bandwidth_ $B$ is the frequency span over which the channel's transfer function remains flat. If two carrier frequencies differ by more than $B$, the received signals are statistically independent.

_Time diversity_ exploits the fact that channel fading changes over time. By transmitting the same data symbol (or a coded version) at multiple, well‑separated instants—typically spaced beyond the _coherence time_ $T$—the receiver obtains independent copies of the signal. If one copy suffers deep fade, another is likely to arrive when the channel conditions are favorable, allowing combining techniques such as maximal‑ratio or selection combining to recover the original data with a lower error probability.

_Frequency diversity_ leverages the frequency selectivity of wireless channels. The transmitter spreads identical information across several carrier frequencies that differ by more than the _coherence bandwidth_ $B$. Because each frequency band experiences an independent fading coefficient, the receiver can combine the distinct replicas (again via maximal‑ratio or other methods) to reduce the likelihood that all paths simultaneously degrade, thereby improving link reliability without requiring additional time resources.

Time or frequency diversity offers a systematic way to lower the variability of channel gain by repeating each symbol $L$ times, thereby reducing the variance of the channel response by a factor of $1/L$.  Because the transmitter can explicitly control each repetition, it is possible to apply sophisticated coding schemes rather than merely duplicating bits, which enhances error‑correction performance.  The method also provides a clear trade‑off: for every additional order of diversity the system gains robustness at the cost of proportionally expanded bandwidth.

The primary drawback is the linear increase in required bandwidth—an $L$-order scheme consumes $L$ times more spectrum.  Moreover, when the total energy per information bit $E_b$ is fixed, each repeated copy receives only $1/L$ of that energy, so while the SNR variations are damped (its variance is divided by $L$), the average SNR remains unchanged.  This bandwidth penalty can be prohibitive in spectrally crowded environments.

### multipath diversity

_Multipath diversity_ arises naturally in environments where signals reach the receiver through multiple propagation paths—direct line‑of‑sight, reflections, diffraction, etc. Each path imposes its own delay and fading coefficient; if these delays exceed a few symbol periods, the resulting multipath components are effectively independent; they become resolvable paths. By employing techniques such as equal‑gain or maximal‑ratio combining over the received multipath replicas (often implemented in OFDM or MIMO receivers), the system capitalizes on spatial richness to mitigate deep fades that would otherwise cripple a single‑path link.

### spatial diversity

_Spatial_ diversity, also known as _antenna diversity_, uses multiple transmit and/or receive antennas separated by enough distance (typically several wavelengths) to decorrelate the fading seen at each element. In a receiver with $L$ antennas, the signals from all elements are combined—often using maximal‑ratio combining—to produce an aggregate SNR that grows roughly as $\sqrt{L}$. Unlike time or frequency diversity, antenna diversity does not consume extra bandwidth and offers robust performance even in static channels where temporal or spectral variations are limited.

The minimum distance between two receive antennas required to obtain independent fading—i.e., effective spatial diversity—is governed by the channel's _coherence distance_, which is inversely proportional to the angle-spread of arriving waves, because smaller angle-spread implies fewer diverse scattering paths. When a mobile terminal receives signals that arrive from almost all directions (≈360°), the coherence distance is roughly one half of the carrier wavelength, λ/2; for example, at 2&nbsp;GHz (λ≈15&nbsp;cm) the antennas should be separated by about 7.5&nbsp;cm.  Conversely, a base‑station receiver typically experiences a much smaller angle‑spread (≈30°), yielding a coherence distance on the order of ten wavelengths; thus, two antennas at a 2&nbsp;GHz base station would need to be spaced around 1.5&nbsp;m apart to achieve uncorrelated fading.

Spatial (antenna) diversity achieves the same variance reduction as time/frequency schemes (variance is divided by $L$) but without any bandwidth expansion.

The cost of spatial diversity lies in the increased number of RF chains: an $L$-order system requires $L$ antennas and associated circuitry, which raises both complexity and power consumption.  Receiver‑side antenna diversity offers no freedom to alter or encode the transmitted symbols—each antenna simply captures the same signal—so it cannot leverage advanced coding strategies that time/frequency diversity can provide. Transmit-side antenna diversity is not straightforward to implement.

#### receiver-antenna diversity

_Receiver-antenna diversity_ is far more common than transmit‑antenna diversity because it can be added to the receiving side without changing the transmitter's power budget or waveform design. A mobile handset or base station can simply mount an extra antenna and use signal‑combining algorithms (maximal ratio, selection, etc.) to improve the effective SNR, all while keeping the transmitted signal unchanged. Consequently, most modern wireless systems favor receiver‑side diversity whenever extra antennas can be accommodated.

Another reason for its common use is that it imposes no requirement on the transmitter design or standardisation of modulation, coding and frame structure. Because modern standards such as LTE, 5G NR and IEEE&nbsp;802.11 specify only the output that a receiver must be able to decode, vendors can freely innovate in antenna configuration, detection algorithms and equalisation without altering the transmitted waveform. This "transmitter‑transparent" property enables rapid deployment of diversity gains through simple hardware upgrades (e.g., adding an extra antenna) while preserving interoperability across devices from different manufacturers; at the same time it allows companies to differentiate performance—better sensitivity or higher throughput—without competing on the core physical‑layer specifications that are locked by the standard.

#### transmit-antenna diversity

In contrast, _transmit-antenna diversity_ would require additional RF chains, careful phase coordination, and potentially higher power consumption at the transmitter—costs that are hard to justify for a single user link. It is typically employed only in CDMA systems or, when multiple receive antennas are available as in MIMO, the system can exploit spatial diversity on both sides. In a pure CDMA link, the base station receives from many users over a single antenna but benefits from transmit‑side spreading codes that allow coherent combining of the signals from several transmit antennas at the mobile. If the receiver has several antennas—as is common in MIMO deployments—each transmit antenna can be paired with multiple receive paths, yielding independent spatial channels and either higher data rates or greater link robustness through diversity combining.

## space–time block code

_Space–time block codes_ (STBCs) exploit multiple transmit antennas to provide diversity without sacrificing spectral efficiency.  

A prototypical example is the Alamouti scheme, which transmits two data symbols $S_1$ and $S_2$ over two consecutive time slots using two antennas. In the first slot both antennas emit $S_1$ and $S_2$ simultaneously, yielding a received sample $y_1=\alpha_1 S_1+\alpha_2 S_2+n_1$. In the second slot the transmit vector is $(-S_2^*,\,S_1^*)$, producing $y_2=-\alpha_1 S_2^*+\alpha_2 S_1^*+n_2$. By conjugating the second observation, both equations contain only the unknown symbols, allowing the receiver to solve a 2×2 linear system and recover both data streams.  

The Alamouti code achieves full diversity order 2 while maintaining 100% spectral efficiency—two symbols are transmitted in two channel uses, unlike time‑switch transmit (TST) schemes that halve throughput. Because it requires a specific transmit format, adoption of STBCs typically necessitates updates to communication standards; once incorporated (e.g., Wi‑Fi, 3G/4G/5G), compliant devices automatically support the scheme.

## diversity combining

_Diversity combining_ refers to the use of multiple _independent_ observations of a signal in order to mitigate fading or interference. When several replicas of a symbol arrive through different channels, they can be combined to improve reliability.  The basic question is _how_ to combine them.  The most common approaches are: (annotation: 3 items: selection combining, equal-gain combining, maximal-ratio combining)

- _Selection combining_ (SC) ::@:: – choose the replica with the highest instantaneous channel SNR $\gamma_i \propto \lvert \alpha_i \rvert^2$.
- _Equal-gain combining_ (EGC) ::@:: – add all received signals _coherently_ with equal weight.
- _Maximal-ratio combining_ (MRC) ::@:: – weight each branch by the _conjugate_ of its channel gain $\alpha_i$.

A fourth, related technique is _switched combining_ (or _scanning combining_), where the receiver switches to another branch when the current one falls below a preset threshold. This method is efficient in some scenarios.

These techniques can be combined depending on system requirements and channel conditions. For example, _lucky imaging_ first selects the best&nbsp;(e.g., 10%) of images using SC, then applies EGC to those selected images.

### diversity combining error analysis

In a diversity system each branch experiences independent fading.  At high SNR the dominant error event is that _every_ branch's instantaneous SNR falls below the decision threshold.  Since the branches are independent, $$P_{\text{error} }\;\approx\; \prod_{i=1}^{L}\Pr(\gamma_i<\gamma_{\!th}) \;\propto\; \left(\frac{1}{\text{SNR} }\right)^{L} \,,$$ so the _symbol_ error rate behaves like $$\boxed{\text{SER}\;\approx\;\frac{C}{(\text{SNR})^{L} } }$$ with $L$ being the _diversity order_.  The constant $C$ varies with the combining rule, modulation, channel statistics, etc., and is captured by the _diversity gain_.

While the constant $C$ varies according to the _diversity gain_, most diversity schemes share this same power-law asymptotic dependence, so they share the same asymptotic slope $-D$ on a log‑log SER vs. SNR plot; only the prefactor $C$ differs.

### selection combining

In selection combining, choose the replica with the largest instantaneous channel SNR $\gamma_i \propto \lvert \alpha_i \rvert^2$: $$r_{\text{sc} } = r_{i^*}, \qquad i^* = \arg\max_i \lvert \alpha_i \rvert^2 .$$

If all $L$ branches are independent and Rayleigh‑faded (so that SNR $\gamma_i := \lvert \alpha_i \rvert^2 E_b / N_0$ is exponentially distributed with mean $\overline{\gamma}$), the probability that _every_ branch has SNR below a threshold $c$ is $$P_e = P(\gamma_1,\ldots,\gamma_L < c) = \bigl(1-e^{-\,c/\overline{\gamma} }\bigr)^L .$$

The expected diversity gain, i.e. increase in _linear_ SINR ratio, for independent, Rayleigh‑distributed branches equals $$G_{\text{SC} }=\sum_{k=1}^{L}\frac{1}{k},$$ which shows that the incremental benefit decreases rapidly as more channels are added. It can be a fallback when hardware or power budgets are tight, but expect higher error rates. (annotation: __this course__: For simplicity, treat the _diversity gain_ as 1 or 0&nbsp;dB.)

### equal-gain combining

In equal-gain combining, all received signals are summed with equal weights, but first each one is phase‑aligned to cancel the channel's complex rotation (hence the word "_coherently_"): $$r_{\text{eq} } = e^{-j \arg \alpha_1}\, r_1 + e^{-j \arg \alpha_2}\, r_2 + \dots + e^{-j \arg \alpha_L}\, r_L.$$ The exponential factors rotate each replica so that their phases match before addition, ensuring constructive combination.

EGC performs better than SC when every branch has low SNR, but it is suboptimal if one branch dominates the others (i.e., its SNR is much larger). (annotation: __this course__: For simplicity, treat the _diversity gain_ in dB to be halfway between selection combining and maximal-ratio combining.)

### maximal-ratio combining

In maximal-ratio combining, each branch is weighted with the _complex conjugate_ of its channel gain $\alpha_i$ so that the received signals are _coherently_ added: $$r_{\text{opt} } = a_1^*\, r_1 + a_2^*\, r_2 + \dots + a_L^*\, r_L,$$ where $a_i^*$ (the complex conjugate of $\alpha_i$) aligns the phase and scales the amplitude of each replica for optimal signal‑to‑noise ratio.

When channel statistics are known (or can be estimated accurately), MRC minimizes the output noise variance and yields the lowest possible error probability. The resulting SNR is simply the sum of the individual branch SNRs $\gamma_k := \lvert \alpha_k \rvert^2 E_b / N_0$: $$\mathrm{SNR}_{\text{MRC} } = \sum_{k=1}^{L} \gamma_k .$$  (annotation: __this course__: For simplicity, treat the _diversity gain_ to be $L$, or $10 \log L$ in dB.)

Implementing MRC requires knowledge of channel coefficients $\alpha_i$, obtained via pilot symbols or training sequences. Modern Wi‑Fi chipsets use this principle to combine multiple antennas while keeping hardware complexity manageable.

Maximal-ratio combining is optimal In a flat‑fading MIMO system with $N$ receive antennas. In such a system, the received vector is $\mathbf{y}=\mathbf hs+\rho\mathbf{n}$, where $\mathbf h=[h_0,\dots ,h_{N-1}]^T$ contains the complex channel gains and $\mathbf{n}\sim{\cal CN}(0,I_N)$ follows a multivariate complex normal distribution.  The quantity $\hat{s} = (\mathbf h^\dagger \mathbf h)^{-1} \mathbf h^\dagger \mathbf y$ is the linear estimate of the transmitted symbol obtained from the _least‑squares solution_ to the observation model; it serves as the decision statistic in maximum‑likelihood (ML) detection.  The ML rule for detecting a symbol $s\in\mathcal M$ chooses the candidate that minimizes $|\hat{s}-s|^2$.  Expanding this least‑squares estimate yields $$\hat{s}= \frac{\sum_{i=0}^{N-1} h_i^{*} y_i} {\sum_{i=0}^{N-1}|h_i|^2},$$which is precisely the maximal‑ratio combining (MRC) rule: each branch is de‑rotated by $h_i^{*}$ and weighted in proportion to its channel magnitude $|h_i|$.  This weighting maximizes the output signal‑to‑noise ratio (SNR), because the combined signal power scales with $\sum|h_i|^2$ while the noise variance remains $\rho^2$; the resulting SNR is $E_s/\rho^2\,\sum_{i}|h_i|^2$.  Moreover, the weighted sum is a _sufficient statistic_ for the transmitted symbol: conditioning on $\hat{s}$ renders all other information irrelevant to ML detection.  Consequently MRC achieves the same error probability as the optimal ML detector under additive white Gaussian noise, making it globally optimal among linear receivers in this scenario.

### implementing diversity combining

In the early 2000s, Chinese operator Xiaolintong pursued a low‑cost wireless strategy by repurposing cordless‑phone technology for voice and later for Wi‑Fi data. Because conventional Wi‑Fi provides only ~100&nbsp;m outdoor coverage, extending range to about one kilometre required recovering roughly 20–25&nbsp;dB of link budget loss without altering the standard. The most practical remedy was receive spatial diversity: adding a second RF antenna and employing maximal‑ratio combining (MRC) in digital baseband. While MRC delivers optimal error performance, its analog implementation is complex; thus it is typically executed on a DSP or ASIC after ADC conversion of two independent data streams.

Cost considerations drive alternative designs. Selection combining (SC), which simply chooses the stronger of the two antenna signals, can be realised with an inexpensive RF switch and minimal software logic. However, SC requires accurate channel estimates for both antennas to decide which path to use. Because Wi‑Fi frames contain pilot symbols but no continuous reference channel, a time‑division approach is employed: each frame's pilots are split between the two antennas, allowing simultaneous estimation of both channel gains while keeping hardware identical to a single‑antenna system. However, halving the training sequence halves the number of samples per estimate, which degrades estimation SNR by roughly 3&nbsp;dB; with four antennas this loss becomes about 6&nbsp;dB and can render selection essentially random. Consequently, two‑antenna diversity is usually the practical ceiling for single‑RF‑chain designs—additional RF/ADC chains are needed to keep pilot length per antenna acceptable.

These examples illustrates how practical constraints—silicon area, power, and real‑estate costs—often necessitate suboptimal but cost‑effective diversity schemes in commercial Wi‑Fi chipsets.

## alternatives

Error‑correcting codes (ECC) offer an attractive alternative—or complement—to physical diversity techniques by introducing redundancy in the transmitted data rather than repeating identical symbols.  By encoding each block of information into a longer codeword, the receiver can detect and correct errors that arise from fading or noise without consuming extra bandwidth; the coding gain effectively boosts the average SNR experienced by each logical bit.  When combined with diversity combining, ECC provides two independent layers of protection: diversity reduces the probability that all copies of a symbol are simultaneously corrupted, while the error‑correcting code restores any remaining errors, yielding a markedly lower overall error rate than either technique alone.
