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

{@{__Power control__ (PC)}@} is {@{a transmit‑power adjustment strategy}@} so that {@{the _received signal‑to‑noise ratio_ ($\mathrm{SNR}$) stays near a pre‑specified target}@}, giving {@{a desired bit error probability ($P_e$)}@}. <!--SR:!2027-02-17,293,330!2027-02-15,291,330!2027-02-13,289,330!2027-02-18,294,330-->

## open-loop power control

{@{_Open-loop power control_}@} has {@{no receiver feedback}@}. The transmitter {@{estimates output power}@} from {@{local information}@}—{@{the strength of a base‑station reference signal}@}, {@{the network's transmit‑power limit}@}, and {@{fixed standard‑defined scaling factors}@}. It then {@{sets transmission power}@} so {@{the signal is decodable}@} within {@{regulatory and interference limits}@}. <!--SR:!2026-12-12,255,330!2026-12-06,250,330!2026-11-15,232,330!2026-11-30,245,330!2026-11-25,241,330!2027-02-12,288,330!2026-12-28,268,330!2026-11-24,240,330!2026-12-07,251,330!2026-12-12,255,330-->

This method is {@{used mainly for initial access or first uplink bursts}@} (e.g., {@{PRACH in LTE}@}). With {@{no feedback loop}@}, {@{transmit power}@} depends only on {@{channel‑state information available locally}@}—{@{a quick, low‑overhead estimate}@} before {@{a link is established}@}. <!--SR:!2026-11-22,238,330!2026-12-03,247,330!2026-11-24,240,330!2027-02-16,292,330!2027-02-06,282,330!2026-11-10,227,330!2026-12-03,247,330-->

The approach works only when {@{uplink and downlink see the same large‑scale fading}@}: {@{shadowing, blockage, distance‑dependent path loss}@}. In {@{frequency division duplex (FDD) systems}@} this {@{often fails because the two bands propagate differently}@}, producing {@{mismatched fading statistics}@}. <!--SR:!2026-11-25,241,330!2026-12-11,254,330!2026-11-24,240,330!2026-12-11,254,330!2027-01-11,278,330-->

## closed-loop power control

{@{_Closed-loop power control_}@} adds {@{receiver feedback}@}. The receiver {@{measures received power (or a quality metric)}@} and {@{sends a TPC command}@} telling the transmitter to {@{increase, decrease, or hold power}@}. The transmitter {@{follows the command}@}. <!--SR:!2026-11-29,244,330!2026-11-15,232,330!2026-12-01,246,330!2027-02-14,290,330!2026-12-12,255,330!2027-02-10,286,330-->

{@{This loop}@} runs {@{during active data transmission in most mobile systems}@} (e.g., {@{CDMA, WCDMA, LTE, Bluetooth}@}). By reacting to {@{real‑time channel and interference changes}@}, {@{closed‑loop control}@} maintains {@{target signal quality with far more precision than open‑loop}@}, at {@{the cost of additional signalling overhead}@}. <!--SR:!2026-12-05,249,330!2026-12-12,255,330!2027-01-02,272,330!2026-11-16,233,330!2026-12-01,246,330!2026-12-03,247,330!2027-02-08,284,330-->

For {@{closed‑loop control}@} to work, {@{feedback must be timely}@}. If {@{the delay exceeds the fading coherence time}@}, power adjustments {@{lag and become ineffective}@}. <!--SR:!2026-12-12,255,330!2027-01-07,276,330!2027-02-11,287,330!2026-12-06,250,330-->

## advantages and disadvantages

{@{Power control}@} is {@{simple to implement}@} and {@{handles path loss and shadowing}@}. {@{Closed‑loop schemes}@} track {@{slow fading with limited feedback overhead}@}; when {@{fading is slow enough}@}, the channel reduces to {@{a fixed‑gain AWGN link}@}, simplifying {@{modem design}@}. <!--SR:!2027-01-12,279,330!2027-02-16,292,330!2026-12-05,249,330!2026-11-25,241,330!2027-02-07,283,330!2026-11-18,235,330!2026-12-12,255,330!2026-11-24,240,330-->

Power control cannot {@{track fast Rayleigh fading}@}. {@{The feedback channel}@} adds overhead, and near {@{a cell boundary}@}, {@{higher transmit power}@} worsens {@{co‑channel interference (CCI)}@}. Power control is a poor fit for {@{fast‑fading or latency‑critical links}@}. <!--SR:!2026-12-04,248,330!2026-12-09,252,330!2026-12-07,251,330!2026-12-04,248,330!2026-11-28,243,330!2027-01-02,272,330-->

## optimality

You might expect {@{sending more power when the channel is bad and less when it is good}@} to be {@{efficient}@}. {@{The optimal strategy}@} does the opposite: it sends {@{_more bits_ during good channel conditions}@} while keeping {@{energy per bit ($E_b$) low}@}; in {@{poor channels}@} it {@{transmits fewer bits with higher $E_b$}@}—the reverse of {@{plain power control}@}. <!--SR:!2026-12-12,255,330!2026-11-17,234,330!2026-12-12,255,330!2027-02-05,281,330!2027-02-11,287,330!2026-11-23,239,330!2026-12-10,253,330!fsrs,2026-10-23T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-15T00:00:00.000Z-->

{@{Cellular systems}@} still {@{use simple power control}@} because they need {@{two‑way real‑time communication}@} and cannot {@{support adaptive bit loading}@}. {@{Non‑real‑time traffic like Wi-Fi}@} can {@{afford slower adaptation}@} for {@{better energy efficiency}@}. <!--SR:!2026-11-23,239,330!2026-11-11,228,330!2027-01-07,276,330!2026-12-07,251,330!2026-12-07,251,330!2026-11-12,229,330!2027-02-18,294,330-->
