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

{@{__Power control__ (PC)}@} is {@{a strategy that adjusts the transmit power}@} so that {@{the _received signal‑to‑noise ratio_ ($\mathrm{SNR}$) remains close to a pre‑specified target}@}, thereby aiming for {@{a desired bit error probability ($P_e$)}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

## open-loop power control

{@{_Open-loop power control_}@} is {@{a one‑way procedure}@} that does {@{not rely on any feedback from the receiver}@}. The transmitter {@{estimates the required output power}@} by using {@{information that it can obtain locally}@} – for example, {@{the strength of a reference signal broadcast by the base station}@}, {@{the maximum transmit‑power limit that the network has allotted}@}, and {@{fixed scaling factors defined in the standard}@}. With this estimate, the device {@{sets its transmission power}@} so that {@{the received signal will be strong enough to be decoded}@} while staying {@{within regulatory or interference limits}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

This technique is {@{most often used for initial access or for the first uplink burst}@} (e.g., {@{PRACH in LTE}@}). Because {@{there is no feedback loop}@}, the {@{power setting}@} can only be {@{as accurate as the channel‑state information available at the transmitter}@}. It provides a {@{quick, low‑overhead way}@} to obtain a {@{reasonable transmit power}@} before {@{any active communication link is established}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

Its {@{effectiveness hinges on the assumption}@} that {@{uplink and downlink experience identical large‑scale fading phenomena}@}—such as {@{shadowing, blockage, or distance‑dependent path loss}@}. In {@{frequency division duplex (FDD) systems}@} this assumption often {@{fails because the two bands propagate differently}@}, leading to {@{mismatched fading statistics}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

## closed-loop power control  

{@{_Closed-loop power control_}@} adds a {@{feedback step}@} that allows the {@{receiver to influence the transmitter's output}@}. After {@{sending a signal}@}, the receiver measures {@{its received power (or other quality metric) and sends back a command}@}—often called {@{TPC or a similar control message}@}—indicating whether the transmitter should {@{increase, decrease, or keep its current power level}@}. The transmitter then {@{adjusts accordingly}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{This iterative process}@} is used during {@{active data transmission in almost all mobile systems}@} (e.g., {@{CDMA, WCDMA, LTE, Bluetooth, etc.}@}). Because it reacts to {@{real‑time channel variations and interference conditions}@}, {@{closed-loop control}@} can maintain a {@{target received signal quality}@} with {@{much higher precision than open-loop methods}@}, though it {@{requires additional signalling overhead}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

Its {@{effectiveness hinges on}@} that {@{the feedback must be timely}@}; if the {@{delay exceeds the coherence time of the fading process}@}, the power adjustment will {@{lag and become ineffective}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

## advantages and disadvantages

{@{Power control}@} is {@{simple to implement}@} and can {@{effectively counteract path loss and shadowing}@} when used in an {@{open‑loop fashion}@}. {@{Closed‑loop schemes}@} can {@{adapt to very slow fading}@} with {@{modest feedback overhead}@}, which, if successful, reduces {@{the channel to a fixed‑gain AWGN link}@} and simplifies {@{modem design}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

On {@{the downside}@}, power control cannot {@{track fast Rayleigh fading}@}. {@{The requirement for a feedback channel}@} adds {@{overhead}@}, and when a mobile is {@{near a cell boundary}@}, {@{increased transmit power}@} can {@{worsen co‑channel interference (CCI)}@}. These limitations make power control less attractive for {@{scenarios demanding rapid adaptation or low-latency communication}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

## optimality

Intuitively one might think that {@{sending more power in bad channel conditions and less power when the channel is good}@} would be {@{efficient}@}. Yet, {@{a truly optimal strategy}@} behaves differently: it sends {@{_more bits_ (and therefore more power) during favorable channel conditions}@} while keeping {@{the energy per bit ($E_b$) low}@}; conversely, it {@{transmits fewer bits with higher $E_b$ in poor channels}@}—essentially {@{the opposite of plain power control}@}. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->

{@{Cellular systems}@} continue to {@{employ simple power control}@} because they require {@{two‑way real‑time communication}@} and cannot yet {@{support more sophisticated adaptive bit loading}@}. In contrast, {@{non-real-time traffic such as Wi-Fi}@} may {@{tolerate slower adaptation}@}, allowing {@{more energy-efficient schemes}@} to be used. <!--SR:!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270!2025-12-25,4,270-->
