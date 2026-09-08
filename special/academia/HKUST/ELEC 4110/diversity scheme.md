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

In {@{telecommunications}@}, {@{a __diversity scheme__}@} {@{improves signal reliability}@} by using {@{two or more channels with different characteristics}@}.

## diversity

Typical {@{diversity sources}@}: {@{time diversity, frequency diversity}@}, {@{multipath diversity, and antenna diversity}@}.

### time and frequency diversity

{@{The _coherence time_ $T$}@} is the interval over which {@{the channel's fading coefficient remains constant}@}. Symbols with {@{duration $\tau < T$}@} {@{experience correlated fades}@}; when {@{$\tau > T$}@}, they are {@{effectively independent}@}. Similarly, {@{the _coherence bandwidth_ $B$}@} is the frequency span where {@{the channel transfer function stays flat}@}. Carriers {@{differing by more than $B$}@} yield {@{statistically independent}@} received signals.

{@{Time diversity}@} transmits {@{the same symbol (or a coded version)}@} at {@{instants spaced beyond $T$}@}, giving the receiver {@{independent copies}@}. If one copy {@{suffers deep fade}@}, another likely arrives when {@{the channel is favorable}@}, and {@{combining techniques}@} recover the data.

{@{Frequency diversity}@} sends {@{identical data on multiple carriers separated by more than $B$}@}. Because {@{each carrier}@} sees {@{an independent fading coefficient}@}, the receiver {@{combines the replicas}@} to reduce {@{the chance all paths degrade simultaneously}@}.

Both methods lower {@{the variance of channel gain by a factor of $1/L$}@} by {@{repeating each symbol $L$ times}@}. The transmitter can {@{apply coding rather than simply duplicating bits}@}, improving {@{error‑correction performance}@}. The trade‑off: every {@{additional order of diversity}@} costs {@{proportionally more bandwidth or symbol time}@}.

{@{The main drawback}@} is {@{the linear bandwidth increase}@}—{@{an $L$-order scheme consumes $L$ times more spectrum or time}@}, which can be {@{prohibitive in spectrally crowded environments}@} or {@{ruin time-sensitive applications}@}.

Moreover, when {@{the _total_ SNR at transmission is fixed}@}, each copy {@{carries only $1/L$ of that energy}@}, so {@{the _effective_ SNR at reception stays the same or drops}@}. (annotation: __this course__: Tested in {@{the final examination}@}.) For example, with {@{maximal-ratio combining}@} and {@{equal energy per branch}@}, each branch's {@{_individual_ SNR is $1/L$ of the _total_ SNR at transmission}@}, so {@{the _effective_ SNR at reception}@} equals {@{the _total_ SNR at transmission}@}. With {@{other combining methods}@}, {@{the effective SNR}@} may {@{even be reduced}@}. One does not gain {@{"extra" SNR for free by using diversity}@}.

### multipath diversity

{@{_Multipath diversity_}@} uses {@{multiple propagation paths}@}—{@{direct line‑of‑sight, reflections, diffraction}@}—each with its {@{own delay and fading coefficient}@}. When {@{delays exceed a few symbol periods}@}, {@{the multipath components}@} are {@{effectively independent}@} and become {@{resolvable paths}@}. Combining them (e.g., in {@{OFDM or MIMO receivers}@}) {@{resists deep fades}@} that would {@{cripple a single‑path link}@}.

### spatial diversity

{@{_Spatial diversity_ (also _antenna diversity_)}@} uses {@{multiple transmit/receive antennas}@} spaced {@{several wavelengths apart}@} to {@{decorrelate the fading}@} at each element. With {@{$L$ antennas}@}, combining their signals (often via {@{maximal‑ratio combining}@}) yields {@{an aggregate SNR growing as $\sqrt{L}$ or $L$}@} depending on the method. Unlike {@{time or frequency diversity}@}, {@{antenna diversity}@} does not {@{consume extra bandwidth}@} and works {@{even in static channels}@}.

{@{The minimum antenna spacing for independent fading}@} depends on the channel's {@{_coherence distance_}@}, which is {@{inversely proportional to angle‑spread}@}. {@{A mobile terminal}@} receiving {@{signals from all directions (≈360°)}@} has {@{coherence distance ≈ λ/2}@}—at {@{2&nbsp;GHz (λ≈15&nbsp;cm)}@}, antennas should be {@{separated by ≈7.5&nbsp;cm}@}. {@{A base station}@} with {@{smaller angle‑spread (≈30°)}@} has {@{coherence distance ≈ 10λ}@}, so two antennas at {@{2&nbsp;GHz}@} need {@{≈1.5&nbsp;m spacing}@}.

{@{Spatial diversity}@} achieves {@{the same variance reduction (divided by $L$) as time/frequency schemes}@} but {@{without bandwidth expansion}@}.

{@{The cost}@} is {@{the increased number of RF chains}@}: {@{an $L$-order system}@} needs {@{$L$ antennas and circuitry}@}, raising {@{complexity and power consumption}@}. {@{Receiver‑side diversity}@} can't {@{alter or encode the transmitted symbols}@}—each antenna {@{captures the same signal}@}—so it {@{can't leverage coding strategies}@} that {@{time/frequency diversity}@} allows. {@{Transmit‑side diversity}@} is {@{harder to implement}@}.

#### receiver-antenna diversity

{@{_Receiver-antenna diversity_}@} is {@{more common}@} because it requires {@{no changes to the transmitter's power budget or waveform design}@}. {@{A handset or base station}@} can {@{add an extra antenna}@} and use {@{combining algorithms}@} to improve {@{the _effective_ SNR}@} while {@{keeping the transmitted signal unchanged}@}.

It also imposes {@{no requirement on transmitter design or standardisation}@}. Because {@{standards like LTE, 5G NR and IEEE&nbsp;802.11}@} specify {@{only the output a receiver must decode}@}, vendors can {@{innovate in antenna configuration and equalisation}@} without {@{altering the transmitted waveform}@}. {@{This "transmitter‑transparent" property}@} lets operators {@{deploy diversity gains}@} via {@{simple hardware upgrades}@} while maintaining {@{interoperability}@}. Companies can {@{differentiate performance}@} without {@{competing on locked physical‑layer specs}@}.

#### transmit-antenna diversity

{@{_Transmit-antenna diversity_}@} requires {@{additional RF chains, phase coordination, and power}@}—costs {@{hard to justify for a single user link}@}. It is {@{typically employed only in CDMA systems}@} or when {@{multiple receive antennas are available (MIMO)}@}. In {@{a pure CDMA link}@}, {@{transmit‑side spreading codes}@} allow {@{coherent combining at the mobile}@} from {@{several transmit antennas}@}. In {@{MIMO deployments}@}, each transmit antenna can be {@{paired with multiple receive paths}@}, yielding {@{independent spatial channels}@} and either {@{higher data rates or greater reliability}@}.

## space–time block code

{@{Space–time block codes (STBCs)}@} exploit {@{multiple transmit antennas}@} to provide {@{diversity without sacrificing spectral efficiency}@}.

{@{The prototypical Alamouti scheme}@} transmits {@{two symbols $S_1$, $S_2$}@} over {@{two time slots using two antennas}@}. First slot: transmit vector {@{$(S_1, S_2)$}@}, yielding {@{$y_1=\alpha_1 S_1+\alpha_2 S_2+n_1$}@}. Second slot: transmit vector {@{$(-S_2^*,\,S_1^*)$}@}, yielding {@{$y_2=-\alpha_1 S_2^*+\alpha_2 S_1^*+n_2$}@}. By {@{conjugating the second observation}@}, the receiver solves {@{a 2×2 linear system to recover both symbols}@}.

{@{The Alamouti code}@} achieves {@{full diversity order 2}@} while keeping {@{spectral efficiency the same}@}—two symbols in two channel uses, unlike {@{time‑switch transmit (TST) schemes}@} that {@{halve throughput}@}. Because it requires {@{a specific transmit format}@}, {@{STBC adoption}@} typically {@{requires standard updates}@}; once {@{incorporated (e.g., Wi‑Fi, 3G/4G/5G)}@}, {@{devices}@} support {@{it without further changes}@}.

## diversity combining

{@{_Diversity combining_}@} merges {@{multiple independent signal observations}@} to {@{combat fading or interference}@}. {@{The three main approaches}@} are: (annotation: 3 items: {@{selection combining, equal-gain combining, maximal-ratio combining}@}).

- _Selection combining_ (SC) ::@:: – choose the replica with the highest instantaneous channel SNR $\gamma_i \propto \lvert \alpha_i \rvert^2$.
- _Equal-gain combining_ (EGC) ::@:: – add all received signals _coherently_ with equal weight and divide by $L$ at either transmitter or receiver.
- _Maximal-ratio combining_ (MRC) ::@:: – weight each branch by the _conjugate_ of its channel gain $\alpha_i$ and divide by the sum of squared weights.

{@{A fourth technique}@} is {@{_switched combining_ (or _scanning combining_)}@}, where the receiver {@{switches to another branch when the current one falls below a threshold}@}, working {@{well when channel conditions change slowly}@}.

These can be {@{combined depending on system requirements}@}. In {@{_lucky imaging_}@}, the method first {@{selects the best images via SC}@}, then applies {@{EGC to those selected images}@}.

### diversity combining error analysis

In {@{a diversity system}@} each branch experiences {@{independent fading}@}. At {@{high SNR}@}, errors occur when {@{_every_ branch's SNR falls below the decision threshold}@}. Since {@{the branches are independent}@}, {@{$$P_{\text{error} }\;\approx\; \prod_{i=1}^{L}\Pr(\gamma_i<\gamma_{\!th}) \;\propto\; \left(\frac{1}{D \cdot \text{SNR} }\right)^{L} \,,$$}@} so {@{the _symbol_ error rate}@} behaves like {@{$$\boxed{\text{SER}\;\approx\;\frac{C}{(D \cdot \text{SNR})^{L} } }$$}@} with {@{$L$}@} being {@{the _diversity order_}@}. {@{The constant $C$}@} captures {@{the _diversity gain_}@} and depends on {@{the combining rule and channel statistics}@}; {@{$D$}@} varies with {@{the modulation scheme}@} (e.g., {@{$D = 4$ for BPSK at high SNR}@}).

{@{All diversity schemes}@} share {@{this power‑law asymptotic dependence}@}—{@{the same asymptotic slope $-L$}@} on {@{a log‑log SER vs. SNR plot}@}; only {@{the prefactors $C$ and $D$}@} differ.

### selection combining

In {@{selection combining}@}, choose {@{the replica with the largest instantaneous channel SNR}@} {@{$\gamma_i \propto \lvert \alpha_i \rvert^2$}@}: {@{$$r_{\text{sc} } = r_{i^*}, \qquad i^* = \arg\max_i \lvert \alpha_i \rvert^2 .$$}@}

If {@{all $L$ branches are independent and Rayleigh‑faded}@} (so {@{SNR $\gamma_i \propto \lvert \alpha_i \rvert^2$}@} is {@{exponentially distributed with mean $\overline{\gamma}$}@}), the probability that {@{_every_ branch has SNR below threshold $c$}@} is {@{$$P_e = P(\gamma_1,\ldots,\gamma_L < c) = \bigl(1-e^{-\,c/\overline{\gamma} }\bigr)^L .$$}@}

{@{The expected diversity gain}@} (increase in {@{_linear_ SNR ratio}@}) equals {@{$$G_{\text{SC} }=\sum_{k=1}^{L}\frac{1}{k},$$}@} showing {@{incremental benefit decreases rapidly with more channels}@}. SC works as {@{a fallback when budgets are tight}@} but gives {@{higher error rates}@}. (annotation: __this course__: For simplicity, treat {@{the _diversity gain_ as 1 or 0&nbsp;dB}@}.)

### equal-gain combining

In {@{equal-gain combining}@}, {@{all received signals}@} are {@{phase‑aligned and summed with equal weights}@}, then {@{divided by $L$}@}: {@{$$r_{\text{eq} } = \frac 1 L \left( e^{-j \arg \alpha_1}\, r_1 + e^{-j \arg \alpha_2}\, r_2 + \dots + e^{-j \arg \alpha_L}\, r_L \right) \,,$$}@} The exponential factors {@{rotate each replica so phases match}@} before addition.

{@{EGC outperforms SC}@} when {@{all branches have low SNR}@} but is {@{suboptimal if one branch dominates}@}. (annotation: __this course__: For simplicity, treat {@{the _diversity gain_ in dB to be halfway between SC and MRC}@}.)

### maximal-ratio combining

In {@{maximal-ratio combining}@}, each branch is weighted by {@{the _complex conjugate_ of its channel gain $\alpha_i$}@} and {@{coherently added}@}: {@{$$r_{\text{opt} } = \frac 1 {\sum_{k = 1}^L \lvert a_L \rvert^2} \left(a_1^*\, r_1 + a_2^*\, r_2 + \dots + a_L^*\, r_L\right) \,,$$}@}

When {@{channel statistics are known}@}, MRC minimizes {@{output noise variance}@} and yields {@{the lowest error probability}@}. {@{The resulting SNR}@} is {@{the sum of branch SNRs}@}: {@{$$\mathrm{SNR}_{\text{MRC} } = \sum_{k=1}^{L} \gamma_k .$$}@}  (annotation: __this course__: For simplicity, treat {@{the _diversity gain_ to be $L$, or $10 \log L$ in dB}@}.)

{@{Implementing MRC}@} requires {@{channel coefficients $\alpha_i$}@}, obtained via {@{pilot symbols or training sequences}@}.

In {@{a flat‑fading MIMO system with $N$ receive antennas}@}, {@{the received vector}@} is {@{$\mathbf{y}= s \mathbf h + \rho \mathbf{n}$}@}, where {@{$\mathbf h=[h_0,\dots ,h_{N-1}]^T$}@} contains {@{the complex channel gains}@} and {@{$\rho \mathbf{n}\sim{\cal CN}\!\left(0, \rho^2 \mathbf I_N\right)$}@}. {@{The ordinary least squares (OLS) estimate}@} is {@{$\hat{s} = (\mathbf h^\dagger \mathbf h)^{-1} \mathbf h^\dagger \mathbf y$}@}, which equals {@{the maximum‑likelihood (ML) decision statistic}@} since minimizing {@{$\sum_i \lvert \hat y_i - y_i \rvert^2$}@} maximizes {@{the joint probability of $\mathbf y$}@}. Expanding yields {@{$$\hat{s}= \frac{\sum_{i=0}^{N-1} h_i^{*} y_i} {\sum_{i=0}^{N-1}|h_i|^2},$$}@} {@{the MRC rule}@}: each branch is {@{de‑rotated by $h_i^{*}$}@} and {@{weighted by $|h_i|$}@}. {@{The estimation variance}@} is {@{$\frac {\rho^2} {\sum_i \lvert h_i \rvert^2}$}@}, so the SNR is {@{multiplied by $\sum_i \lvert h_i \rvert^2 = \sum_i \text{SNR}_i$, the _diversity gain_}@}. {@{The weighted sum}@} is {@{a _sufficient statistic_ for the transmitted symbol}@}—conditioning on $\hat{s}$ renders {@{all other information irrelevant to ML detection}@}. Thus MRC achieves {@{the same error probability as the optimal ML detector under AWGN}@}, making it {@{globally optimal among linear receivers}@}.

### implementing diversity combining

In {@{the early 2000s, Chinese operator Xiaolintong}@} repurposed {@{cordless‑phone technology}@} for {@{voice and Wi‑Fi data}@}. {@{Conventional Wi‑Fi}@} covers {@{only ~100&nbsp;m outdoors}@}, but extending {@{range to about one kilometre}@} required {@{recovering 20–25&nbsp;dB of link budget}@} without {@{altering the standard}@}. The solution was {@{receive spatial diversity}@}: {@{a second RF antenna}@} with {@{maximal‑ratio combining (MRC) in digital baseband}@}. {@{MRC gives optimal performance}@} but is {@{complex in analog}@}; it is typically {@{executed on a DSP or ASIC}@} after ADC.

{@{Cost considerations}@} drive {@{simpler designs}@}. {@{Selection combining (SC)}@} can be realised with {@{an RF switch and minimal logic}@}, but requires {@{accurate channel estimates for both antennas}@}. Because {@{Wi‑Fi frames}@} contain {@{pilot symbols but no continuous reference}@}, {@{a time‑division approach}@} splits {@{each frame's pilots}@} between antennas, allowing {@{simultaneous channel estimation}@}. However, {@{halving the training}@} sequence {@{degrades estimation SNR by ~3&nbsp;dB}@}; with {@{four antennas}@} the loss is {@{≈6&nbsp;dB}@}, making SC {@{essentially random}@}. So {@{two‑antenna diversity}@} is {@{the practical ceiling for single‑RF‑chain designs}@}.

In practice, {@{silicon area, power, and cost}@} often demand {@{suboptimal but cost‑effective diversity schemes}@} in {@{commercial Wi‑Fi chipsets}@}.

## alternatives

{@{Error‑correcting codes (ECC)}@} provide {@{an alternative to physical diversity}@} by introducing {@{redundancy in the transmitted data}@} rather than {@{repeating identical symbols}@}. Encoding {@{each block into a longer codeword}@} lets the receiver {@{detect and correct errors}@} from {@{fading or noise without extra bandwidth}@}. When {@{combined with diversity}@}, ECC gives {@{two independent protection layers}@}: {@{diversity}@} reduces {@{the chance all symbol copies are corrupted simultaneously}@}, while {@{the ECC}@} {@{fixes remaining errors}@}, yielding {@{lower error rates than either alone}@}.
