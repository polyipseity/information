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

{@{__Power control__ (PC)}@} is {@{a strategy that adjusts the transmit power}@} so that {@{the _received signal‑to‑noise ratio_ ($\mathrm{SNR}$) remains close to a pre‑specified target}@}, targeting {@{a desired bit error probability ($P_e$)}@}. <!--SR:!2027-02-17,293,330!2027-02-15,291,330!2027-02-13,289,330!2027-02-18,294,330-->

## open-loop power control

{@{_Open-loop power control_}@} does {@{not rely on any feedback from the receiver}@}. The transmitter {@{estimates the required output power}@} by using {@{information that it can obtain locally}@} – for example, {@{the strength of a reference signal broadcast by the base station}@}, {@{the maximum transmit‑power limit that the network has allotted}@}, and {@{fixed scaling factors defined in the standard}@}. With this estimate, the device {@{sets its transmission power}@} so that {@{the received signal will be strong enough to be decoded}@} while staying {@{within regulatory or interference limits}@}. <!--SR:!2026-12-12,255,330!2026-12-06,250,330!2026-11-15,232,330!2026-11-30,245,330!2026-11-25,241,330!2027-02-12,288,330!2026-12-28,268,330!2026-11-24,240,330!2026-12-07,251,330!2026-12-12,255,330-->

This technique is {@{most often used for initial access or for the first uplink burst}@} (e.g., {@{PRACH in LTE}@}). Because {@{there is no feedback loop}@}, {@{the transmit power}@} is only {@{as accurate as the channel‑state information available at the transmitter}@}. It provides a {@{quick, low‑overhead way}@} to obtain a {@{reasonable transmit power}@} before {@{any active communication link is established}@}. <!--SR:!2026-11-22,238,330!2026-12-03,247,330!2026-11-24,240,330!2027-02-16,292,330!2027-02-06,282,330!2026-11-10,227,330!2026-12-03,247,330!2026-12-16,259,330-->

This works only if {@{uplink and downlink experience identical large‑scale fading phenomena}@}, such as {@{shadowing, blockage, or distance‑dependent path loss}@}. In {@{frequency division duplex (FDD) systems}@} this assumption often {@{fails because the two bands propagate differently}@}, leading to {@{mismatched fading statistics}@}. <!--SR:!2026-11-25,241,330!2026-12-11,254,330!2026-11-24,240,330!2026-12-11,254,330!2027-01-11,278,330-->

## closed-loop power control

{@{_Closed-loop power control_}@} adds a {@{feedback step}@} that allows the {@{receiver to influence the transmitter's output}@}. After {@{sending a signal}@}, the receiver measures {@{its received power (or other quality metric) and sends back a command}@}—often called {@{TPC or a similar control message}@}—indicating whether the transmitter should {@{increase, decrease, or keep its current power level}@}. The transmitter {@{follows the command}@}. <!--SR:!2026-11-29,244,330!2026-11-15,232,330!2026-12-01,246,330!2027-02-14,290,330!2026-12-12,255,330!2027-02-10,286,330!2026-12-11,254,330!2026-11-20,237,330-->

{@{This loop}@} runs during {@{active data transmission in almost all mobile systems}@} (e.g., {@{CDMA, WCDMA, LTE, Bluetooth, etc.}@}). Because it reacts to {@{real‑time channel variations and interference conditions}@}, {@{closed-loop control}@} can maintain a {@{target received signal quality}@} with {@{much higher precision than open-loop methods}@}, though it {@{requires additional signalling overhead}@}. <!--SR:!2026-12-05,249,330!2026-12-12,255,330!2027-01-02,272,330!2026-11-16,233,330!2026-12-01,246,330!2026-12-03,247,330!2027-02-08,284,330!2027-02-17,293,330-->

For {@{closed-loop control}@} to work, {@{the feedback must be timely}@}; if the {@{delay exceeds the coherence time of the fading process}@}, the power adjustment will {@{lag and become ineffective}@}. <!--SR:!2026-12-12,255,330!2027-01-07,276,330!2027-02-11,287,330!2026-12-06,250,330-->

## advantages and disadvantages

{@{Power control}@} is {@{simple to implement}@} and {@{counteracts path loss and shadowing}@} well in {@{open‑loop fashion}@}. {@{Closed‑loop schemes}@} can {@{track very slow fading}@} with {@{limited feedback overhead}@}; when the fading is slow enough, this reduces {@{the channel to a fixed‑gain AWGN link}@} and simplifies {@{modem design}@}. <!--SR:!2027-01-12,279,330!2027-02-16,292,330!2026-12-05,249,330!2026-11-25,241,330!2027-02-07,283,330!2026-11-18,235,330!2026-12-12,255,330!2026-11-24,240,330!2026-11-13,230,330-->

{@{Power control}@} cannot {@{track fast Rayleigh fading}@}. {@{The requirement for a feedback channel}@} adds {@{overhead}@}, and when a mobile is {@{near a cell boundary}@}, {@{increased transmit power}@} can {@{worsen co‑channel interference (CCI)}@}. Power control is therefore a poor fit for {@{fast-changing channels or latency‑critical links}@}. <!--SR:!2026-12-04,248,330!2026-12-09,252,330!2026-12-07,251,330!2026-12-04,248,330!2026-11-28,243,330!2027-01-02,272,330!2026-11-25,241,330!2027-01-07,275,330-->

## optimality

You might expect {@{sending more power when the channel is bad and less when it is good}@} to be {@{efficient}@}. In fact, {@{the optimal strategy}@} does the opposite: it sends {@{_more bits_ during favorable channel conditions}@} while keeping {@{the energy per bit ($E_b$) low}@}; conversely, it {@{transmits fewer bits with higher $E_b$ in poor channels}@}—the reverse of {@{plain power control}@}. <!--SR:!2026-12-12,255,330!2026-11-17,234,330!2026-12-12,255,330!2027-02-05,281,330!2027-02-11,287,330!2026-11-23,239,330!2026-12-10,253,330-->

{@{Cellular systems}@} still {@{use simple power control}@} because they require {@{two‑way real‑time communication}@} and cannot yet {@{support more sophisticated adaptive bit loading}@}. {@{Non-real-time traffic such as Wi-Fi}@}, by contrast, can {@{afford slower adaptation}@}, allowing {@{more energy‑efficient schemes}@}. <!--SR:!2026-11-23,239,330!2026-11-11,228,330!2027-01-07,276,330!2026-12-07,251,330!2026-12-07,251,330!2026-11-12,229,330!2027-02-18,294,330-->
