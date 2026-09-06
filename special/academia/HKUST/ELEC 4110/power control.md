---
aliases:
  - ELEC 4110 power control
  - ELEC4110 power control
  - power control
tags:
  - flashcard/active/special/academia/HKUST/ELEC_4110/power_control
  - language/in/English
---

# power control

- see: [general/power control](../../../../general/power%20control.md)

{@{__Power control__ (PC)}@} is {@{a strategy that adjusts the transmit power}@} so that {@{the _received signal‑to‑noise ratio_ ($\mathrm{SNR}$) remains close to a pre‑specified target}@}, targeting {@{a desired bit error probability ($P_e$)}@}.

## open-loop power control

{@{_Open-loop power control_}@} is {@{a one‑way procedure}@} that does {@{not rely on any feedback from the receiver}@}. The transmitter {@{estimates the required output power}@} by using {@{information that it can obtain locally}@} – for example, {@{the strength of a reference signal broadcast by the base station}@}, {@{the maximum transmit‑power limit that the network has allotted}@}, and {@{fixed scaling factors defined in the standard}@}. With this estimate, the device {@{sets its transmission power}@} so that {@{the received signal will be strong enough to be decoded}@} while staying {@{within regulatory or interference limits}@}.

This technique is {@{most often used for initial access or for the first uplink burst}@} (e.g., {@{PRACH in LTE}@}). Because {@{there is no feedback loop}@}, the {@{power setting}@} can only be {@{as accurate as the channel‑state information available at the transmitter}@}. It provides a {@{quick, low‑overhead way}@} to obtain a {@{reasonable transmit power}@} before {@{any active communication link is established}@}.

This works only if {@{uplink and downlink experience identical large‑scale fading phenomena}@}, such as {@{shadowing, blockage, or distance‑dependent path loss}@}. In {@{frequency division duplex (FDD) systems}@} this assumption often {@{fails because the two bands propagate differently}@}, leading to {@{mismatched fading statistics}@}.

## closed-loop power control

{@{_Closed-loop power control_}@} adds a {@{feedback step}@} that allows the {@{receiver to influence the transmitter's output}@}. After {@{sending a signal}@}, the receiver measures {@{its received power (or other quality metric) and sends back a command}@}—often called {@{TPC or a similar control message}@}—indicating whether the transmitter should {@{increase, decrease, or keep its current power level}@}. The transmitter {@{follows the command}@}.

{@{This iterative process}@} is used during {@{active data transmission in almost all mobile systems}@} (e.g., {@{CDMA, WCDMA, LTE, Bluetooth, etc.}@}). Because it reacts to {@{real‑time channel variations and interference conditions}@}, {@{closed-loop control}@} can maintain a {@{target received signal quality}@} with {@{much higher precision than open-loop methods}@}, though it {@{requires additional signalling overhead}@}.

For {@{closed-loop control}@} to work, {@{the feedback must be timely}@}; if the {@{delay exceeds the coherence time of the fading process}@}, the power adjustment will {@{lag and become ineffective}@}.

## advantages and disadvantages

{@{Power control}@} is {@{simple to implement}@} and {@{counteracts path loss and shadowing}@} well in {@{open‑loop fashion}@}. {@{Closed‑loop schemes}@} can {@{track very slow fading}@} with {@{limited feedback overhead}@}; when the fading is slow enough, this reduces {@{the channel to a fixed‑gain AWGN link}@} and simplifies {@{modem design}@}.

{@{Power control}@} cannot {@{track fast Rayleigh fading}@}. {@{The requirement for a feedback channel}@} adds {@{overhead}@}, and when a mobile is {@{near a cell boundary}@}, {@{increased transmit power}@} can {@{worsen co‑channel interference (CCI)}@}. Power control is therefore a poor fit for {@{fast-changing channels or latency‑critical links}@}.

## optimality

One might expect that {@{sending more power in bad channel conditions and less power when the channel is good}@} would be {@{efficient}@}. In fact, {@{the optimal strategy}@} does the opposite: it sends {@{_more bits_ (and therefore more power) during favorable channel conditions}@} while keeping {@{the energy per bit ($E_b$) low}@}; conversely, it {@{transmits fewer bits with higher $E_b$ in poor channels}@}—the reverse of {@{plain power control}@}.

{@{Cellular systems}@} still {@{use simple power control}@} because they require {@{two‑way real‑time communication}@} and cannot yet {@{support more sophisticated adaptive bit loading}@}. {@{Non-real-time traffic such as Wi-Fi}@}, by contrast, can {@{afford slower adaptation}@}, which opens the door to {@{more energy-efficient schemes}@}.
