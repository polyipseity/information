---
aliases:
  - ELEC 4110 cellular network
  - ELEC4110 cellular network
  - cellular network
tags:
  - flashcard/active/special/academia/HKUST/ELEC_4110/cellular_network
  - language/in/English
---

# cellular network

- see: [general/cellular network](../../../../general/cellular%20network.md)

{@{A __cellular network__}@} is {@{a radio system that divides a mobile operator's coverage area into cells}@}, each served by {@{its own base station}@}. {@{Frequency reuse across non‑adjacent cells}@} {@{increases spectral efficiency}@} while {@{limiting interference}@}. Key operational concerns are {@{handover procedures}@} and {@{cell planning to balance coverage and capacity}@}.

## history

{@{A quick historical recap}@}: {@{wireless telegraph (1896)}@}, {@{early NYC wireless voice (1920s)}@}, {@{first‑generation mobile phones (~1980s)}@}.

{@{Mobile telephony}@} started with {@{Marconi's 1896 wireless‑telegraphy experiments}@}, showing {@{messages could travel long distances without wires}@}. In the {@{early twentieth century}@}, engineers {@{demonstrated wireless telephony}@}: {@{radio waves could carry speech across city‑wide networks}@}.

{@{The first commercial mobile phone}@} appeared in {@{1973}@}, but it had a {@{critical limitation}@}: {@{CDMA capacity grows with spreading factor}@}, which {@{ties capacity to bandwidth}@}, and the {@{finite radio spectrum}@} cannot {@{expand thousands of times}@}, so it {@{supported only a handful of users}@}.

{@{Bell Labs}@} solved this with {@{the cellular architecture}@}: {@{dividing geographic areas into small cells}@} that {@{reuse the same frequencies in a controlled manner}@}. {@{Spatial frequency reuse}@} turned {@{limited spectrum into capacity}@} and {@{made modern mobile telephony possible}@}. CAPEX rises {@{linearly with the number of sites}@}: each {@{macro‑cell costs roughly $300k}@}, and {@{OPEX (power, rental/real‑estate fees, utilities)}@} {@{scales with site count}@}. {@{Revenue from additional subscribers}@} offsets these {@{costs, justifying the investment}@}.

## architecture

{@{Mobile users}@} connect to {@{the _Base Transceiver Station (BTS)_}@} via {@{radio}@}. {@{Several BTSs}@} link {@{through a _Backhaul_ to a _Base Station Controller (BSC)_}@}; {@{multiple BSCs}@} forward {@{traffic to the core, the _Mobile Switching Center (MSC)_}@}. {@{The MSC}@} interfaces with {@{the _Public Switched Telephone Network (PSTN)_}@} for {@{voice and the Internet for data}@}.

{@{The _BSC–MSC backhaul_}@} is {@{typically the capacity bottleneck}@}: {@{all BTS‑to‑core traffic}@} {@{must pass through it}@}, so its {@{bandwidth caps overall system throughput}@}.

## principles

{@{Cellular systems}@} work by {@{partitioning geographic coverage into cells}@} and {@{reusing frequencies in non‑overlapping cells}@} to {@{maximize use of limited radio spectrum}@}. Since {@{signal power falls off with distance}@}, {@{two transmitters using the same channel}@} can {@{operate without interference if far enough apart}@}.

With {@{no reuse}@}, {@{all $N$ channels}@} are divided into {@{$B$ distinct sets}@} and {@{each set serves one cell}@}; the {@{total capacity equals $(N/B)\times B = N$}@}. This {@{gives excellent signal quality}@} but {@{poor system capacity}@}: only {@{$B$ cells can exist}@}.

With {@{reuse}@}, an {@{appropriate _frequency reuse factor_ $K$}@} (i.e. {@{the number of channel sets}@}) balances {@{interference against bandwidth utilization}@}: {@{larger $K$}@} reduces {@{interference but limits capacity}@}; {@{smaller $K$}@} increases {@{capacity at the cost of higher co‑channel interference}@}. The {@{design goal}@} is to space {@{co‑channel cells far enough apart that attenuated signals do not degrade quality}@}.

### frequency reuse

In {@{cellular networks}@}, {@{the same spectrum}@} is used by {@{multiple cells that are sufficiently far apart to limit mutual interference}@}. {@{The set of frequencies assigned to a group of non‑adjacent cells}@} is a {@{_reuse pattern_}@}.

With {@{$K$ disjoint channel sets}@}, {@{the _frequency reuse factor_}@} is {@{$$K \;=\; \frac{\text{total number of frequency channels} }{\text{channels per base station} } \,.$$}@} {@{A smaller $K$}@} (e.g., 4 or 7) means {@{more aggressive reuse}@}: each {@{base station uses a larger fraction of the spectrum}@}, giving {@{higher capacity per unit area}@} but also {@{higher co‑channel interference}@}. {@{A larger $K$}@} reduces {@{interference at the cost of spectral efficiency}@}. Total network capacity scales with {@{base station count $N_{\mathrm{BS} }$}@} as {@{$$C_{\text{tot} } = \frac{N_{\mathrm{ch} } }{K}\; N_{\mathrm{BS} } \,,$$}@} so {@{the capacity‑versus‑$N_{\mathrm{BS} }$ slope}@} is {@{proportional to $1/K$}@}.

{@{An optimal $K$}@} balances two extremes: {@{reuse factor 1}@} gives {@{maximal spectral use but intolerable interference}@}; {@{no reuse (each cell gets a unique set)}@} gives {@{zero interference but no capacity scaling}@}.

{@{The allowable reuse factor}@} depends on {@{the physical‑layer technology}@} and {@{propagation environment}@}. {@{Analog 1G systems}@}, which need about {@{18&nbsp;dB SIR}@}, typically use {@{$K\approx7$}@}. {@{Digital GSM 2G systems}@} tolerate a {@{lower SIR (~13&nbsp;dB)}@} and can {@{use $K=4$}@}. {@{Propagation characteristics}@} also matter: in {@{rural or line‑of‑sight areas}@} with {@{path‑loss exponent close to 2}@}, interference extends farther, so {@{a larger $K$ (e.g., 7)}@} is needed. In {@{dense urban settings with exponent near 4}@}, interference decays faster and {@{smaller $K$ (≈4)}@} is feasible. In sum, {@{frequency reuse}@} trades {@{spectral efficiency against interference tolerance}@}, guided by {@{modulation/coding capability and terrain}@}.

### path loss

{@{_Path loss_ (attenuation of radio signals with distance)}@} plays a dual role: it {@{limits individual cell reach}@} but also {@{reduces co‑channel interference between cells}@}, which {@{enables capacity}@}. Without {@{sufficient path loss}@}, frequency reuse would be {@{impractical}@}.

{@{The received power}@} decreases with {@{distance according to a _path‑loss model_}@}. {@{The log‑distance model}@} is {@{$$L(d) = L_0 + 10\,n_{\!p}\,\log_{10}\!\left(\frac{d}{d_0}\right) \,,$$}@} where {@{$L_0$}@} is the {@{loss at reference distance $d_0$}@}, {@{$d$}@} is the {@{link length}@}, and {@{$n_{\!p}$}@} is the {@{_path‑loss exponent_}@}.

- $n_p \approx 2$ – rural or line‑of‑sight environments where the signal propagates with little obstruction. ::@:: Interference from distant cells decays slowly, so a larger reuse factor (e.g., $K=7$) is required to keep co‑channel interference below acceptable limits.
- $n_p \approx 4$ – dense urban areas with many buildings and scatterers. ::@:: Signal power falls off more rapidly; consequently, the same technology can employ a smaller reuse factor (e.g., $K=4$) while still meeting signal‑to‑interference ratio (SIR) targets.

{@{The $n_{\!p}$ value}@} directly shapes {@{cell size, base‑station density, and reuse strategy}@}.

## handover

In {@{cellular networks}@}, {@{_handover_ (also called _handoff_)}@} is {@{the procedure by which a mobile device transfers a call or data session from one cell to another while maintaining service continuity}@}. It requires {@{signalling between the mobile and both the current and target cells}@} to establish {@{a new radio link before tearing down the old one}@}. {@{Successful handover}@} depends on {@{mobile speed, cell layout geometry, signalling protocol timing, and network equipment capabilities}@}.

{@{High mobility}@} makes {@{handover harder}@}: {@{the time window in which the device remains within a single cell}@} becomes {@{very short}@}. If {@{signalling cannot complete before the device exits coverage}@}, {@{the call drops}@}. {@{Most terrestrial systems}@} assume {@{speeds below 200&nbsp;km&nbsp;h⁻¹}@}; exceeding this leads to {@{missed handover triggers and connection failures}@}.

### handover examples

Consider {@{high‑speed rail}@}: {@{trains at 300–400&nbsp;km&nbsp;h⁻¹}@}, such as {@{the Guangzhou‑Wuhan line}@}, experience {@{frequent dropped calls and poor live‑streaming quality}@} because {@{rapid cell‑boundary crossing}@} overwhelms {@{handover signalling}@}.

{@{Commercial aircraft}@} present a different case: {@{a plane cruising at ~800&nbsp;km&nbsp;h⁻¹}@} is {@{faster}@}, but its {@{high altitude reduces angular velocity relative to ground cells}@} (≈0.64°&nbsp;s⁻¹ at 10&nbsp;km altitude and 30° inclination). With {@{a typical macro‑cell beamwidth of ~60°}@}, the vehicle spends {@{roughly 100&nbsp;seconds within one cell}@}, giving {@{handover algorithms more time than on the ground}@}. {@{New problems appear}@} though: reduced {@{link budget due to antenna sidelobe reception}@} and metallic {@{shielding inside the aircraft}@}, as well as {@{Doppler shift (≈2&nbsp;kHz at 2&nbsp;GHz)}@} (still {@{manageable by modern oscillators with ~20&nbsp;kHz tolerance}@}). In practice, mobile phones may {@{receive occasional SMS or voice near an airport}@}, but {@{reliable in‑flight connectivity}@} is {@{difficult and generally disallowed under aviation regulations}@}.

## link budgeting

{@{A 3G macro cell}@} typically transmits {@{≈20&nbsp;W (43&nbsp;dBm) total power}@}, but each {@{traffic channel receives about 2% of that}@} (~25.4&nbsp;dBm). {@{Beamforming}@} adds {@{≈17&nbsp;dBi gain}@} ({@{decibel isotropic}@}; {@{antenna gain relative to a theoretical isotropic antenna}@} that {@{uniformly radiates in all directions}@}) while {@{cable loss subtracts ~2&nbsp;dB}@}, yielding {@{an effective radiated power of ≈40.8&nbsp;dBm}@}. {@{The receiver sensitivity}@} is {@{roughly –112&nbsp;dBm}@}, and with {@{a 7.5&nbsp;dBm safety margin}@}, {@{the maximum tolerable path loss}@} is {@{about 145&nbsp;dB}@}.

Under {@{an NYC‑style propagation model}@}, {@{145&nbsp;dB path loss}@} translates to {@{<2&nbsp;km ground coverage}@}; in the air, losing {@{beamforming gain (~17&nbsp;dBi)}@} and suffering {@{≈20&nbsp;dB penetration loss}@} reduces {@{the allowable path loss to ~100&nbsp;dB}@}, but {@{free‑space propagation (exponent≈2)}@} extends {@{range to about 3&nbsp;km}@}. {@{Distance, antenna patterns, and environmental shielding}@} all affect {@{handover feasibility}@}.

## 1G

{@{First‑generation (1G) systems}@} were {@{analog, using FM voice at 30&nbsp;kHz}@} and {@{simple digital signalling such as FSK}@}. {@{The primary design goal}@} was {@{_capacity_}@}, with {@{many incompatible standards worldwide}@}—{@{_AMPS_ (US) and _TACS_ (UK)}@} are typical examples. Signals were separated by {@{FDMA}@}, so {@{the number of distinct channels}@} was {@{limited}@}; {@{a signal‑to‑interference ratio of roughly $\text{SIR}\approx 18\;\text{dB}$}@} was needed, and {@{frequency reuse followed a pattern with $K=7$}@}.

During {@{_initial deployment_}@}, {@{coverage rather than capacity}@} limited performance. Networks used {@{large macro‑cells}@} to reduce {@{base station count}@}. As {@{subscriber numbers rose}@} in {@{densely populated areas}@}, operators {@{split or sectorised cells}@} to handle load. In {@{the _mature stage_}@}, {@{the bottleneck shifted back to capacity}@} and further {@{engineering gains}@} required {@{fundamental architectural changes}@}.

## 2G

{@{Second‑generation (2G) systems}@} enhanced {@{voice capacity}@} and used {@{spectrum more efficiently}@}. {@{New bands}@} combined {@{traditional cellular frequencies with PCS allocations}@}: {@{Europe/Hong&nbsp;Kong: $900\,\text{MHz}$ cellular + $1.8\,\text{GHz}$ PCS}@}, {@{US: $800\,\text{MHz}$ cellular + $1.9\,\text{GHz}$ PCS}@}. {@{Digital transmission}@} added {@{error‑correction coding}@} for {@{better noise and interference immunity}@} while {@{lowering the K factor}@}.

Speech was {@{compressed digitally}@} so each user {@{occupied less bandwidth}@}; {@{Digital AMPS}@} fits {@{three users into a single 30&nbsp;kHz carrier}@}. {@{Data services remained circuit‑switched}@}: {@{the air interface}@} was {@{dedicated to a user throughout the session}@}, giving {@{speeds between 9.6&nbsp;kbps and 14.4&nbsp;kbps}@}.

Europe replaced {@{all legacy 1G infrastructure with a unified standard—GSM}@}—because {@{existing systems were incompatible}@}; GSM quickly {@{captured over 90% of the worldwide market}@}. {@{The US pursued an evolutionary path}@}, maintaining {@{backward compatibility with AMPS}@} through {@{Digital‑AMPS (IS&nbsp;54) and CDMA (IS&nbsp;95)}@}.

## 3G

{@{The transition to 3G}@} was driven by {@{the need for high‑speed wireless data}@}. While {@{2G systems}@} focused on {@{spectral efficiency}@}, 3G targeted {@{data‑centric applications}@} such as {@{mobile Internet access, multimedia messaging, video telephony}@}, and {@{location‑based services}@}.

In {@{3G networks}@}, the design goal is {@{end‑to‑end service}@} across {@{a range of data rates}@}. This is achieved through {@{multi‑mode, multi‑media support}@} that lets operators deliver {@{both voice and high‑bandwidth data from the same infrastructure}@}. {@{Maximum data speeds}@} reach {@{_2&nbsp;Mbps_ for mobile broadband}@} while {@{legacy 3G services}@} offer {@{_144&nbsp;kbps_ or _384&nbsp;kbps_ for narrowband applications}@}.

### 3G services

{@{Mobile operators}@} introduced {@{value‑added services}@}:

- _Multimedia Messaging Service (MMS)_ ::@:: enabled users to send pictures, audio clips, and short video fragments.
- _Rich Voice_ ::@:: encompassed video telephony and combined text‑audio conversations.
- _Location Based Services (LBS)_ ::@:: leveraged GPS or network positioning to provide navigation, local search, and context‑aware advertising.
- _Mobile Internet Access_ ::@:: gave users worldwide connectivity for browsing, email, and early social networking.

These services were marketed as {@{_seamless_}@}: users could switch between {@{voice calls, data sessions, and multimedia streams}@} without {@{noticeable disruption}@}.

## 4G

{@{The shift from 3G to 4G}@} brought {@{large increases in data rates}@} and {@{broadband‑grade mobile services}@}. {@{3G systems}@}, standardized under {@{IMT‑2000}@}, offered {@{peak data speeds of roughly 2&nbsp;Mbps}@}, far beyond {@{the 100&nbsp;kbps limits of 2G digital networks}@}.

Around {@{2010 the first _LTE_ (Long Term Evolution)}@} deployments began to {@{replace or augment 3G infrastructure}@}. LTE pushed {@{peak rates up to 100&nbsp;Mbps}@}. In {@{South Korea}@}, {@{4G/LTE traffic}@} grew to about {@{63% of monthly data volume by 2013}@}, while {@{smartphone penetration}@} climbed from {@{20% in 2010 to roughly 60% by 2012}@}.

This shift reshaped {@{mobile usage}@}: people moved from {@{voice‑centric services to data‑intensive applications}@} such as {@{social networking, music streaming, online gaming and video playback}@}.

## 5G

{@{_5G_}@} builds on {@{LTE's bandwidth}@} but adds {@{_latency_ as a first‑class requirement}@}. {@{Current deployments}@} target {@{sub‑50&nbsp;ms round‑trip times}@}, which is needed for {@{smooth VoIP and low‑delay video streaming}@}.

5G aims to support {@{a _tactile wireless network_}@} for {@{machine‑type communications, real‑time control loops, and immersive interactive gaming}@}. Here {@{end‑to‑end delays must drop below _1&nbsp;ms_}@}. This requires {@{dense small‑cell deployments, massive MIMO}@}, and {@{ultra‑reliable low‑latency communication (URLLC) protocols}@} that handle {@{high‑throughput data and time‑critical control signals}@}.

### 5G implementation

{@{Implementing 5G}@} means turning {@{theoretical data‑rate gains}@} into {@{working hardware}@}. {@{The primary approach}@} is deploying {@{_massive MIMO_—hundreds of antennas per base station}@} so each user gets {@{its own narrow beam}@}.

But {@{adding antennas}@} {@{multiplies the number of RF chains}@}, driving up {@{cost and power consumption}@}. Another challenge: keeping {@{_pilot training overhead_ independent of antenna count}@} so the system is not {@{overwhelmed by channel estimation traffic}@}. {@{Intercell interference mitigation}@} requires {@{global real‑time channel state information (CSI)}@}, so the network needs {@{_low‑latency backhaul_}@} for {@{macro cell and small‑cell coordination}@} in real time. {@{Radio resource management algorithms}@}—{@{dynamic spectrum sharing, user‑centric scheduling, and interference coordination}@}—must operate on {@{fine timescales to keep latency below a few milliseconds}@} while {@{maximizing throughput}@}.

Another design choice exploits {@{the large bandwidth available in sub‑6&nbsp;GHz and mmWave bands}@}. At these frequencies, {@{line‑of‑sight (LOS) propagation dominates}@}, making {@{_beamforming_ necessary to overcome severe path loss}@}.

The combination of {@{_massive MIMO_, high‑bandwidth carriers, precise beamforming, and ultra‑low‑latency backhaul}@} should deliver {@{1000× improvement in data rates}@}. The remaining hurdles are {@{largely engineering}@}: minimizing {@{cost and energy of large RF arrays}@}, reducing {@{pilot overhead through code design}@}, and ensuring {@{backhaul links keep pace with rapid beamforming updates}@} in {@{mmWave deployments}@}.

## applications

{@{Video streaming on mobile devices}@} is sensitive to {@{_playback queue_ dynamics}@}: a queue that {@{falls below its lower boundary}@} triggers {@{playback interruption}@}; one that {@{exceeds its upper boundary}@} causes {@{buffer overflow and packet loss}@}. {@{An RRM scheme}@} aware of {@{Quality‑of‑Experience (QoE)}@} monitors {@{these queue trajectories in real time}@}, allocating {@{radio resources to keep the buffer within safe limits}@}. By adjusting {@{modulation, coding and scheduling rates}@} based on {@{instantaneous queue length}@}, the system prevents {@{stalls and reduces packet loss}@}.

In {@{networked control systems}@}, {@{_control theory_}@} must be reconciled with {@{communication constraints}@} such as {@{limited capacity, variable delay, and packet loss}@}. {@{Queueing behaviour at the link level}@} can destabilize {@{controller performance}@}: {@{late or dropped packets}@} degrade {@{feedback quality}@}. {@{Controllers that explicitly model these network impairments}@}—using concepts like {@{bounded‑delay channels or stochastic packet loss models}@}—keep {@{performance stable}@} even when the {@{physical plant and its sensors/actuators}@} are connected over a {@{shared wireless medium}@}.
