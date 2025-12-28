---
aliases:
  - DSSS
  - ELEC 4110 DSSS
  - ELEC 4110 direct sequence spread spectrum
  - ELEC 4110 direct-sequence spread spectrum
  - ELEC4110 DSSS
  - ELEC4110 direct sequence spread spectrum
  - ELEC4110 direct-sequence spread spectrum
  - direct sequence spread spectrum
  - direct-sequence spread spectrum
tags:
  - flashcard/active/special/academia/HKUST/ELEC_4110/DSSS
  - language/in/English
---

# direct-sequence spread spectrum

- see: [general/direct-sequence spread spectrum](../../../../general/direct-sequence%20spread%20spectrum.md)

{@{__Direct-sequence spread spectrum__ (__DSSS__)}@} transmits a data stream by first {@{modulating it in the usual way}@}—typically with {@{BPSK}@}—then {@{multiplying that baseband signal by a high‑frequency spreading sequence}@}. The result is a {@{wideband waveform}@} whose {@{spectrum is spread over many more chips than the original data bandwidth}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

## spread spectrum

{@{_Spread‑spectrum_ techniques}@} were introduced to {@{mitigate the effects of _frequency‑selective fading_}@}, notably {@{_inter‑symbol interference_ (ISI) and the irreducible error floor}@} that arise from {@{multiple propagation paths}@}. While {@{diversity}@} can address {@{flat‑fading}@}, {@{spread spectrum}@} offers a {@{complementary solution}@} by {@{widening the transmitted signal's bandwidth}@}. <!--SR:!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270-->

{@{A system is classified as _spread‑spectrum_}@} when {@{its transmitted bandwidth $B_s$}@} greatly {@{exceeds the message bandwidth $B_m$}@}, and this relationship remains {@{independent of the data rate}@}: {@{$$B_s \gg B_m, \qquad B_s\;\text{is independent of}\; B_m \,.$$}@} By transmitting {@{over a wide spectrum}@}, {@{narrowband interference}@} is {@{suppressed}@} and {@{ISI in multipath channels}@} can be {@{mitigated}@}, enabling {@{reliable communication even in challenging frequency‑selective environments}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

## spreading

{@{The binary data $b(t)$ and the PN (pseudo-noise) spreading sequence $c(t)$}@} are both {@{bipolar, taking values $\pm 1$}@}: {@{$$b(t)= \pm 1 \quad\text{(binary message)} , \qquad c(t)= \pm 1 \quad\text{(PN spreading code)}$$}@} {@{Each data bit}@} occupies a {@{_bit period_ $t_m$}@}, while {@{each chip of the PN code}@} occupies {@{a much shorter _chip period_ $t_c$}@}. {@{A single bit}@} is {@{represented by several chips}@}; for example, one bit may be {@{spread over 1024 chips}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290-->

{@{The baseband BPSK output}@} can be written as {@{$$s_{BPSK}(t) = \sqrt{2P_t}\;b(t)\;\cos(\omega_c t + \phi)$$}@} where {@{$P_t$}@} is {@{the transmitted power (_not_ bit energy)}@} and {@{$\omega_c$}@} {@{the carrier frequency}@}. After spreading, {@{the final transmitted signal}@} becomes {@{$$s(t)=\sqrt{2P_t}\;c(t)\,b(t)\;\cos(\omega_c t+\phi) \,.$$}@} {@{The multiplication by $c(t)$}@} {@{spreads the spectrum}@} because {@{$c(t)$ changes many times within a single bit interval (chip period $t_c$)}@}. The carrier is {@{no longer a narrow spike}@} but {@{a band whose width is determined by the chip rate}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290-->

### spreading in time domain

{@{Each bit}@} is {@{replaced by a sequence of chips}@}, so the receiver sees a {@{long "spread" waveform}@} even though {@{only one bit was sent}@}, which {@{spreads its spectrum over a larger bandwidth}@}. The {@{resulting _spread signal_}@} looks like {@{a train of chips}@} whose {@{polarity follows the data bits}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270-->

### spreading in frequency domain

In {@{the frequency domain}@} the {@{spreading operation}@} can be seen as a {@{convolution between the data spectrum and the PN‑code spectrum}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290-->

{@{The spectrum of the _spread signal_}@} {@{occupies over a band $W_s$}@} that is {@{much wider than the original narrowband carrier}@}. A {@{non‑spread BPSK signal}@} would occupy a {@{_passband_ bandwidth $W_{\text{non-spread} } = 1/t_b$}@}, whereas the {@{DSSS signal}@} occupies a {@{_passband_ bandwidth $W_{\text{spread} } \approx 1/t_c$}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290-->

## despreading

{@{The receiver}@} performs the {@{inverse of the transmitter's spreading operation}@}. First it {@{multiples the incoming signal $s(t)$ by the _known_ PN sequence $c(t)$}@}. Because {@{the sequence is bipolar, $$c(t)\,c(t)=1$$}@}, so the {@{spread spectrum collapses to its underlying data waveform}@}: {@{$$s_{demod}(t)=c(t)\,s(t)\;\longrightarrow\; \text{data carrier}$$}@} <!--SR:!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270-->

After {@{despreading}@}, the signal is {@{demodulated in the ordinary way (e.g., coherent BPSK detection)}@}) The {@{data modulation}@} {@{need not be BPSK; any scheme}@} may be used. Often, however, the {@{same modulation format}@} is employed {@{for both spreading and data to simplify hardware}@}. The {@{order of spreading and data modulation}@} can be {@{swapped}@}: both yield the {@{same transmitted waveform}@} because {@{multiplication is commutative}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270-->

To {@{recover the data reliably}@} a receiver must {@{know exactly which PN sequence was used for spreading}@}; and {@{align its local replica of $c(t)$}@} with the {@{received signal at the correct chip‑rate timing}@}. When these conditions hold, {@{despreading recovers the original data stream}@} with the {@{same spectral properties as an ordinary narrowband link}@}. <!--SR:!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270-->

## advantages

{@{The key advantages}@} of {@{DS spreading}@} are: (annotation: 3 items: {@{interference suppression, low probability of interception, no additional channel-noise penalty}@}) <!--SR:!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290-->

- _Interference suppression_ ::@:: – spreading reduces the effect of narrowband interference because the energy is spread over a larger spectrum; it is the _primary_ benefits, but there are other benefits below. <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->
- _Low probability of interception (LPI)_ ::@:: – an unintended receiver that does not know the PN sequence sees only noise, making detection difficult. <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->
- _No additional channel‑noise penalty_ ::@:: – the process preserves the signal‑to‑noise ratio of the underlying channel. <!--SR:!2025-12-25,4,270!2025-12-25,4,290-->

If {@{no external interference exists}@}, the {@{bandwidth cost outweighs the benefit}@}; spreading would {@{be pointless}@}. There are {@{two common scenarios}@} where it helps: {@{frequency‑selective fading}@} causing {@{inter‑symbol interference}@}; and {@{multi‑user interference in CDMA systems}@} where {@{many users share the same time/frequency resources}@}. <!--SR:!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290-->

## DS-CDMA

In {@{_DS-CDMA_ systems}@} each user is {@{assigned a unique PN code}@}. The {@{transmitted data}@} are {@{multiplied by that code before transmission}@}; at the receiver, {@{correlation with the same code}@} recovers {@{the data while simultaneously rejecting signals from other users}@}. This {@{code division multiple access}@} allows {@{many users to share the same frequency band}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,290-->

When {@{several users transmit simultaneously over the same time slot and bandwidth}@}—so that {@{their spectra completely overlap}@}—it is {@{impossible to separate them by conventional filtering}@} in either the {@{time or frequency domain}@}; {@{all user signals}@} appear {@{indistinguishable at the front‑end}@}. Treating the {@{unwanted signals as simple additive noise}@} would yield a {@{very low SINR (e.g., <0&nbsp;dB for BPSK)}@}, leading to {@{prohibitively high error rates}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290-->

{@{The key advantage of DS-CDMA}@} is that {@{each user's data}@} is {@{first spread by its unique PN sequence}@}. At the {@{intended receiver}@}, {@{multiplying the received waveform by the correct code}@} {@{"despreads" the desired signal}@}: it {@{collapses back into a narrowband BPSK spectrum}@}, while {@{signals from other users remain widely spread across frequency}@}. A {@{subsequent band‑pass filter}@} can therefore {@{pass only the despread desired component}@} and {@{reject most of the residual interference}@}. {@{This filtering}@} reduces {@{the effective interference power of _each interfering user_}@} to {@{roughly its original value multiplied by the reciprocal of the _spreading_ factor}@} (e.g., {@{a 1/64 "discount factor" per interfering user}@} for {@{a spreading factor of  64}@}), dramatically {@{improving the SINR and enabling reliable demodulation}@}. <!--SR:!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

## pseudo-noise code

A {@{spread‑spectrum system}@} relies on the {@{statistical properties of its pseudorandom noise (PN) codes}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->  

The {@{_correlation_ function}@} quantifies {@{how similar two sequences are as one is shifted relative to the other}@}: {@{$$R_{xy}(\tau)=\sum_n x[n]\,y^*[n-\tau]$$}@} When {@{the two sequences are identical}@}, this reduces to the {@{_auto‑correlation_ of a single sequence $c[n]$}@}: {@{$$R_{cc}(\tau)=\sum_n c[n]\,c^*[n-\tau].$$}@} <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270-->

For {@{DS/CDMA}@}, a {@{_good PN code_}@} is one whose {@{auto‑correlation}@} has a {@{pronounced peak at zero shift}@} and {@{very small values for all non‑zero offsets}@}. Such a sequence provides {@{near‑perfect orthogonality between different shifts}@}, ensuring that {@{correlation with the correct code}@} yields a {@{strong response}@} while {@{cross‑correlation with other codes or shifted versions}@} remains {@{negligible}@}. This property minimizes {@{interference}@} and maximizes {@{security in DS/CDMA communications}@}. <!--SR:!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290-->

## intersymbol interference

{@{Direct‑sequence spread spectrum (DSSS)}@} expands a data signal by {@{multiplying it with a pseudo‑random noise (PN) code}@}. Because {@{the spreading bandwidth is large}@}, DS‑SS signals usually propagate over {@{_frequency‑selective fading channels_ that contain many resolvable echoes}@}. The {@{superposition of these delayed replicas}@} produces {@{_inter‑symbol interference_ (ISI)}@}. In the {@{absence of any countermeasure}@}, ISI {@{drives the error floor to very high values}@}. <!--SR:!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290-->

The {@{standard way a DS‑SS system suppresses ISI}@} is to {@{employ a _RAKE receiver_}@}. A {@{RAKE receiver}@} contains {@{one or more _fingers_}@}. Each finger {@{despreads the received waveform}@} with a {@{PN sequence that has been time‑aligned to one of the multipath delays}@}. Because {@{the autocorrelation of a good PN code is sharply peaked}@}, {@{cross‑correlation terms from non‑matched paths}@} are {@{small}@}; thus {@{each finger}@} sees only {@{a weak ISI contribution from the other paths}@}. <!--SR:!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

### rake receiver

The {@{received signal}@} can be written as a {@{combination of $L = \lfloor W / B_c \rfloor$}@} (where {@{$W$}@} is {@{spread passband bandwidth}@} and {@{$B_c$}@} is the {@{coherence bandwidth}@}) {@{resolved paths}@}: {@{$$y(t)=\sum_{i=1}^{L}\alpha_i\,s(t-\tau_i)c(t-\tau_i)+n(t),$$}@} where {@{$s(\cdot)$}@} is the {@{modulated data}@}, {@{$c(\cdot)$}@} the {@{PN code}@}, {@{$\alpha_i$}@} the {@{complex channel coefficient for path $i$}@}, and {@{$\tau_i$}@} its {@{delay}@}. <!--SR:!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->  

{@{A finger that targets path $j$}@} computes {@{$$r_j(t)=\text{Despread}\!\bigl(y(t),\,c(t-\tau_j)\bigr) =\alpha_j\,s(t-\tau_j)\;\!+\! \sum_{i\neq j}\alpha_i\,s(t-\tau_i)\,\underbrace{\langle c(t-\tau_i), c(t-\tau_j)\rangle}_{\text{small} }\; +\;\langle c(t-\tau_i), n(t)\rangle.$$}@} The {@{term $\langle c(t-\tau_i), c(t-\tau_j)\rangle$}@} is the {@{_normalized cross‑correlation_}@} ("normalized" means {@{divided by the number of chips $N$}@}) of {@{two PN sequences that are misaligned in time}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290-->

For an {@{i.i.d. PN sequence}@} the {@{_normalized_ cross-correlation of two misaligned ($i \ne j$) PN sequences}@} tends to {@{zero variance as the code length $N$ grows}@}: {@{$$\operatorname E[\langle c(t-\tau_i), c(t-\tau_j)\rangle] = 0\,, \qquad \operatorname{Var}(\langle c(t-\tau_i), c(t-\tau_j)\rangle) = \frac 1 N \,.$$}@} Thus {@{each finger}@} extracts a {@{clean observation of the desired data}@} with only {@{residual ISI from other paths and additive noise}@}, which has a {@{power of roughly $1/N$ of the original power}@}. {@{The set of observations $\{r_1,r_2,\dots ,r_L\}$}@} are {@{effectively independent}@}, which yields {@{_diversity gain_}@} from {@{diversity on top of the _processing gain_ from DSSS}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290-->

## effective SINR

The {@{spread spectrum}@} introduces a {@{_processing gain_}@} {@{$\text{PG} = W_{\text{spread} }/W_{\text{non-spread} }$}@}. The {@{_signal‑to‑interference‑plus‑noise ratio_ (SINR) per bit}@} at {@{each finger}@} is {@{multipled by this factor}@}: {@{$$\text{SINR}_{\text{effective} } = \frac {\lvert a_i \rvert^2 E_b} {N_0 + \frac {(\text{\# users}) \cdot \lvert a_i \rvert^2 E_b} {\text{PG} } } \approx \frac {\text{PG} } {\text{\# users} } \,,$$}@} where {@{$E_b$}@} is the {@{energy per bit}@}, {@{$N_0$}@} is the {@{noise spectral density}@}, and {@{$(\text{\# users})$}@} refers to {@{number of _other_ users (excluding self) that can interfere with the current user}@}. The {@{final approximation}@} holds well for {@{high SNR situations}@} (so {@{$N_0$}@} is small relative to {@{$E_b$}@}) in which the {@{error rate becomes interference-limited}@}, and the {@{_BER floor_ from ISI}@} becomes the {@{limiting factor}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

Moreover, because {@{each finger provides an independent measurement of the same bit}@}, {@{combining (e.g., maximal ratio combining or equal‑gain combining)}@} improves the {@{slope of the BER curve}@}: the {@{diversity order equals the number of fingers $L$}@}. <!--SR:!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290-->

## performance

Compare three scenarios: {@{_BPSK_ without spreading}@}. {@{_BPSK + DSSS_ with a single RAKE finger}@}, and {@{_BPSK + DSSS_ with multiple ($L>1$) RAKE fingers}@}. Even {@{one finger dramatically reduces the BER floor}@} due to the {@{processing gain}@}, while {@{adding more fingers}@} steepens the {@{curve further due to diversity gain}@}. {@{The key takeaway}@} is that {@{processing gain and finger diversity}@} jointly mitigate {@{ISI in frequency‑selective fading channels}@}. <!--SR:!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270-->

## implementation

In {@{a DSSS receiver}@} {@{each incoming chip}@} is multiplied by the {@{locally stored spreading sequence}@} and {@{accumulated over one spread period (e.g., 64 chips, 1024 chips)}@}. {@{The multiplication}@} reduces to {@{sign inversion for the $\pm1$ chips}@}, so {@{no dedicated multiplier is required}@}; a {@{simple full‑adder suffices}@}. After {@{accumulation}@} the result is {@{right‑shifted six times to divide by 64}@}, exploiting that {@{$64=2^6$}@}. {@{Two or more parallel despreaders}@} can be {@{instantiated to process distinct multipath components (the “fingers” of a rake receiver)}@}, each producing {@{an observation $W_i$}@} that is later fed into a {@{diversity combiner operating at symbol rate}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270-->

{@{Practical receivers (e.g., 3G handsets)}@} often have {@{only four despreaders}@} because {@{each operates at a high clock rate}@}, yet can still {@{capture full diversity by selecting the strongest paths}@}. {@{This principle}@} underlies why {@{spread‑spectrum systems (3G and earlier)}@} remain {@{power‑efficient despite supporting many multipaths}@}. <!--SR:!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270-->

### time and power considerations

The {@{despreader core}@} must run at the {@{chip rate}@}, which is typically {@{many times (e.g. 64, 1024) faster than the symbol clock}@}. Because {@{dynamic power scales with frequency}@}, the {@{high‑speed despreader dominates the receiver's power budget}@}. The {@{combinatorial logic between clocks (adders, sign‐inverters)}@} has to {@{finish within one chip period}@}; {@{oversized logic}@} forces a {@{lower clock or increased latency and thus higher energy consumption}@}. <!--SR:!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,290-->

The {@{core arithmetic to spread and despread}@} is {@{deliberately simple}@}: {@{full adders for accumulation}@} and {@{bit‑shift units for division by powers of two}@}. {@{Multiplication by $\pm1$}@} is {@{handled by sign inversion}@}, eliminating the need for a {@{multiplier}@}. This keeps {@{the data path short and power‑efficient}@} while still {@{satisfying the timing constraints imposed by the chip clock}@}. <!--SR:!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290-->

### rake receiver architecture

A {@{rake receiver}@} comprises {@{multiple "fingers"}@}, each {@{correlating with one delayed copy of the incoming waveform}@}. The {@{output of each finger}@} is a {@{weighted observation $W_i$}@}; these are {@{combined (selection, equal‑gain or maximal‑ratio)}@} to provide {@{diversity and interference suppression}@}. The {@{number of fingers}@} determines {@{linear scalability in complexity}@}; {@{adding more paths}@} does not {@{explode the hardware cost}@} because the {@{spreading sequence and pilot channel give the receiver structure to exploit}@}. <!--SR:!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270-->

{@{Accurate chip‑level timing}@} is {@{essential for despreading}@}. A {@{pilot channel, transmitted with the same timing as data}@}, provides a {@{known sequence that the receiver correlates against}@}. An {@{exhaustive search over possible despreading timings $D_1, D_2, \ldots$}@} is {@{performed frame by frame}@}, feeding the {@{best estimate to the despreaders}@}. The {@{auto‑correlation of the spreading sequence}@} must be {@{sharply peaked}@}; otherwise {@{timing resolution degrades}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290-->

### implementation with a single RF chain

Even with {@{only one despreader}@}, diversity can be {@{achieved by combining multiple observations across time or frequency (e.g., selection combining)}@}. A {@{single RF/ADC chain}@} can thus {@{realise a two‑branch diversity order}@} by moving {@{the selection switch to the front end}@}. This mirrors {@{Wi‑Fi's antenna‑diversity technique}@}, in which the {@{pilot bits of each frame}@} is {@{split into two in time to estimate the SNR}@}. It demonstrates that {@{low‑complexity receivers}@} can still {@{exploit multipath without additional hardware chains}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,290!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,290!2025-12-25,4,270-->
