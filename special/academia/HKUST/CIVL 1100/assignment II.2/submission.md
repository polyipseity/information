---
aliases:
  - HKUST CIVL 1100 assignment II.2 submission
tags:
  - date/2024/04/15
  - language/in/English
---

# assignment II.2 submission

- HKUST CIVL 1100

CIVL 1100<br/>
Discovering Civil and Environmental Engineering

<!-- markdownlint-disable-next-line MD036 -->
__Assignment II.2__

<!-- markdownlint-disable-next-line MD036 -->
__Assigned date: 8 April 2024__

__Due date: <span style="color: red;"><u>15 April 2024</u></span>__

__Submit <span style="color: red;">a PDF copy</span> of your assignment to <span style="color: red;"><u>Canvas by 23:59 on 15 April 2024</u></span> (late submissions will not be accepted).__

__Complete all the problems. Give the answers in <span style="color: red;">two decimal places</span>.__

Assignment 4

## problem 4.1

Given a flow rate of 8500 m<sup>3</sup>/d and an overflow rate of 50 m<sup>3</sup>/(d·m<sup>2</sup>), calculate the following design parameters of a proposed circular primary sedimentation tank.

### problem 4.1.i

Height of the sedimentation tank (assuming a criterion of diameter/height ratio of 3.5) (<span style="color: red;">2 marks</span>)

> $$\begin{aligned}
> \text{overflow rate} & = \frac {\text{flow rate} } {\text{area} } \\
> \text{area} & = \frac {\text{flow rate} } {\text{overflow rate} } \\
> & = \frac {8500} {50} \\
> & = 170\mathrm{\ m^2} \\
> \text{diameter} & = 2 \sqrt{\frac {170} \pi }\mathrm{\ m} \\
> \text{height} & = \frac {\text{diameter} } {3.5} \\
> & = \frac 4 7 \sqrt{\frac {170} \pi } \\
> & = 4.20350410\mathrm{\ m}\text{ (cor. to 9 sig. fig.)} \\
> & = 4.20\mathrm{\ m}\text{ (cor. to 2 d.p.)}
> \end{aligned}$$

### problem 4.1.ii

Hydraulic retention time (HRT) of the sedimentation tank. (<span style="color: red;">1 mark</span>)

> $$\begin{aligned}
> \text{volume} & = 170 \cdot 4.20350410 \\
> & = 714.59570\mathrm{\ m^3}\text{(cor to 8. sig. fig.)} \\
> \text{HRT} & = \frac {\text{volume} } {\text{flow rate} } \\
> & = \frac {714.59570} {8500} \\
> & = 0.08407008\mathrm{\ d}\text{ (cor. to 7 sig. fig.)} \\
> & = 0.08\mathrm{\ d}\text{ (cor. to 2 d.p.)}
> \end{aligned}$$

## problem 4.2

There is an outdoor renovation project ongoing next to the lobby (G/F) of one of the hall in HKUST. You are a civil engineering student living in the hall and would like to estimate the noise level at your room. <u>Give your answers to the nearest dB for this question.</u>

### problem 4.2.i

Someone claimed that under the same noise source, if receiving distance is <u>doubled</u>, the sound pressure level would be attenuated by approximately <u>6 dB</u>. Do you agree? _(Hint: Assuming two receivers with distances and sound levels $r_1$, $L_1$ and $r_2$, $L_2$ respectively and prove the relationship above.)_ (<span style="color: red;">2 marks</span>)

> $$\begin{aligned}
> & \text{Let }r_1, L_1\text{ be the distance and sound level resp. of the closer receiver.} \\
> & \text{Let }r_2, L_2\text{ be the distance and sound level resp. of the further receiver.} \\
> & \begin{aligned} r_2 & = 2 r_1 && (\text{given}) \\
> \frac {r_2} {r_1} & = 2 \\
> \\
> L_2 & = L_1 - 20 \log_{10}\left(\frac {r_2} {r_1} \right) \\
> L_2 & = L_1 - 20 \log_{10} 2 \\
> L_1 - L_2 & = 20 \log_{10} 2 \\
> & = 6.02059991\mathrm{\ dB}\text{ (cor. to 9 sig. fig.)} \\
> & = 6\mathrm{\ dB}\text{ (cor. to the nearest dB)} \end{aligned}
> \end{aligned}$$

### problem 4.2.ii

Hence, if you are living on the 8<sup>th</sup> floor, and the measured noise level under unmitigated scenario is 98 dB on the 2<sup>nd</sup> floor, what is the estimated noise level at your room without any mitigation measures? (<span style="color: red;">2 marks</span>)

> [Problem 4.2.i](#problem%204.2.i) shows that doubling the receiving distance approximately decreases the sound pressure level by approximately 6 dB.
>
> The 8/F is twice as far away from the G/F as the 4/F, and 4/F is twice as far away from the G/F as the 2/F.
>
> Then, if the noise level on the 2/F is 98 dB, then the noise level on the 4/F is approximately 98 - 6 = 92 dB. If the noise level on the 4/F is 92 dB, then the noise level on the 8/F is approximately 92 - 6 = 86 dB.
>
> Therefore, the estimated noise level at my room without any mitigation measures is approximately 86 dB.

### problem 4.2.iii

Sugggest one engineering solution that the can be taken to minimize the noise impact to the residents in the hall. (<span style="color: red;">2 marks</span>)

> Use acoustic-insulated materials to build the halls. Then the noise level are reduced by the acosutic-insulated materials in the hall walls and floors.

## problem 4.3

You are performing carbon auditing for a construction contractor Company A for construction work, and some activity data and related emission factors of Company A in 2020 are tabulated in __Table 1__ as follows.

__Table 1.__ Activity data and emission factor of Company A in year 2020

| __Activities__                            | __Activity data__         | __Emission factors__                                                                            |
|-------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------------|
| Operation of mobile cars (biodiesel)      | (To e calculated in (i)   | (To e calculated in (i)                                                                         |
| Electricity                               | 5000 kWh per month        | 0.37 kg CO<sub>2</sub>e/kWh                                                                     |
| Operation of light vans (unleaded petrol) | Fuel consumption: 27000 L | EF<sub>CO2</sub> = 2.360 kg/L<br/>EF<sub>CH4</sub> = 0.203 g/L<br/>EF<sub>N2O</sub> = 1.105 g/L |
| Paper consumption                         | 8 tonnes                  | 4.8 kg CO<sub>2</sub>e/kg of waste                                                              |

__Note:__

1. Carbon emission = Activity data (e.g. fuel consumption) × Emission Facgtor
2. Emission (CO<sub>2</sub> equivalent) = Σ (Fuel consumption × Emission Factor of each GHG × GWP)
3. GWP of different GHGs

| GHG            | Global warming potential (GWP) |
|----------------|--------------------------------|
| CO<sub>2</sub> | 1                              |
| CH<sub>4</sub> | 28                             |
| N<sub>2</sub>O | 265                            |

### problem 4.3.i

Assuming that B35 biodiesel is adopted by Company A to reduce carbon footprint, and the fuel economy of the car used is 50 km/gal. Find the daily carbon footprint caused by mobile combustion if 4 cars are needed to travel for 30 km every day. _(Assuming that CO<sub>2</sub> is the only GHG emitted.)_ (<span style="color: red;">2 marks</span>)

> $$\begin{aligned}
> \text{total travelled distance daily} & = 30 \cdot 4 \\
> & = 120\mathrm{\ km} \\
> \text{B35 biodiesel used daily} & = \frac {120} {50} \\
> & = 2.4\mathrm{\ gal} \\
> \text{required daily carbon footprint} & = 2.4 \cdot (0.35 \cdot 9.46 + 0.65 \cdot 10.15) \\
> & = 2.4 \cdot 9.9085 \\
> & = 23.7804\mathrm{\ kg\ CO_2e} \\
> & = 23.78\mathrm{\ kg\ CO_2e}\text{ (cor to 2 d.p.)}
> \end{aligned}$$

### problem 4.3.ii

Categorize the activities in __Table 1__ by scope 1, 2 and 3. (<span style="color: red;">3 marks</span>)

> - scope 1: Operation of mobile cars (biodiesel), Operation of light vans (unleaded petrol)
> - scope 2: Electricity
> - scope 3: Paper consumption

### problem 4.3.iii

By [(i)](#problem%204.3.i), [(ii)](#problem%204.3.ii) and __Table 1__, calculate the total annual carbon footprint of Company A in 2020 _(Hint: You should calculate the annual carbon footprint of each activities in __Table 1__ and sum them up)._ (<span style="color: red;">6 marks</span>)

> $$\begin{aligned}
> & \phantom{=} \text{annual carbon footprint in the first ativity} \\
> & = 23.7804 \cdot 366 \\
> & = 8703.6264\mathrm{\ kg\ CO_2e} \\
> & \phantom{=} \text{annual carbon footprint in the second activity} \\
> & = 5000 \cdot 12 \cdot 0.37 \\
> & = 22200\mathrm{\ kg\ CO_2e} \\
> & \phantom{=} \text{annual carbon footprint in the third activity} \\
> & = 27000 \cdot \left(2.360 \cdot 1 + \frac {0.203} {1000} \cdot 28 + \frac {1.105} {1000} \cdot 265 \right) \\
> & = 27000 \cdot 2.658509 \\
> & = 71779.743\mathrm{\ kg\ CO_2e} \\
> & \phantom{=} \text{annual carbon footprint in the fourth activity} \\
> & = 4.8 \cdot 8 \cdot 1000 \\
> & = 38400\mathrm{\ kg\ CO_2e} \\
> & \phantom{=} \text{required total annual carbon footprint} \\
> & = 8703.6264 + 22200 + 71779.743 + 38400 \\
> & = 141083.3694\mathrm{\ kg\ CO_2e} \\
> & = 141083.37\mathrm{\ kg\ CO_2e}\text{ (cor. to 2 d.p.)}
> \end{aligned}$$
