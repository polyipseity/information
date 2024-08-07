---
aliases:
  - HKUST CIVL 1100 assignment II.1 submission
tags:
  - date/2024/03/26
  - language/in/English
---

# assignment II.1 submission

- HKUST CIVL 1100

CIVL 1100<br/>
Discovering Civil and Environmental Engineering

<!-- markdownlint-disable-next-line MD036 -->
__Assignment II.1__

__Complete all the problems. Give the answers in <span style="color: red;">two decimal places</span>.__

Assignment 3

## problem 3.1

There is an air mixture under the following conditions: P is 3.5 atm, T is 20 °C, and assume that the molecular concentration of the air is 19 g/mol. (1 mol ideal gas at 0°C and 1 atm occupies a volume of 22.4 L)

### problem 3.1.i

What's the volume of 2 mol of the above air? (<span style="color: red;">1 mark</span>)

> $$\begin{aligned}
> pV & = nRT \\
> V & = \frac {nRT} p \\
> V & \propto \frac {nT} p \\
> \text{2 mol of above air} & = (22.4) \frac 2 1 \frac {273.15 + 20} {273.15} \frac 1 {3.5} \\
> & \approx 13.737214\text{ L} \\
> & \approx 13.74\text{ L}
> \end{aligned}$$

### problem 3.1.ii

Assume there is an air pollutant with a concentration of 20 ppmv, what's the air pollutant concentration in mg/m<sup>3</sup> (<span style="color: red;">1 mark</span>)

> $$\begin{aligned}
> \text{concentration} & = (1) \frac {20} {1 \times 10^6} \frac {2} {13.737214 \times 10^{-3}} (19) \\
> & \approx 5.5324173 \times 10^{-2}\text{ g/m}^3 \\
> & = 55.324173\text{ mg/m}^3 \\
> & \approx 55.32\text{ mg/m}^3
> \end{aligned}$$

## problem 3.2

Table 1: Composition of municipal solid waste (MSW) in country A

| Composition         | Average daily quantity (tpd) |
|---------------------|------------------------------|
| Leather             | 256                          |
| Cardboard and paper | 1,745                        |
| Plastic and rubber  | 2,396                        |
| Food waste          | 4,025                        |

Estimate HHV of the MSW in country A based on the information given in Table 1. (<span style="color: red;">4 marks</span>)

> $$\begin{aligned}
> \text{total daily} & = 256 + 1745 + 2396 + 4025 \\
> & = 8422 \\
> \text{HHV} & = 53.5(\text{F} + 3.6\text{CP}) + 372\text{PLR} \\
> & = 53.5 \left(\frac {4025} {8422} (100) + (3.6) \frac {1745} {8422} (100) \right) + (372) \frac {256 + 2396} {8422} (100) \\
> & \approx 18261.3215\text{ kJ/kg} \\
> & \approx 18261.32\text{ kJ/kg}
> \end{aligned}$$

## problem 3.3

Typical MSW has a moisture content of around 25%. Given the empirical of dry mass of the MSW in country A is C<sub>50</sub>H<sub>102</sub>O<sub>49</sub>N.

Note: __Molecular weight of elements:__

| Element | Molecular weight (g/mol) |
|---------|--------------------------|
| C       | 12                       |
| H       | 1                        |
| O       | 16                       |
| N       | 14                       |

### problem 3.3.i

Calculate the percentage of hydrogen by mass (in dry basis) in the MSW from the empirical formula. (<span style="color: red;">1 mark</span>)

> $$\begin{aligned}
> \text{percentage by mass} & = \frac {102(1)} {50(12) + 102(1) + 49(16) + 1(14)} (100\%) \\
> & = \frac {102} {1500} (100\%) \\
> & = 6.8\%
> \end{aligned}$$

### problem 3.3.ii

Find the latent heat of water vapor released in 1 kg of the MSW. (<span style="color: red;">1 mark</span>)

> $$\begin{aligned}
> Q_L & = 2440(W + 9H) \\
> & = 2440(1(0.25) + (9)(1)(1 - 0.25)(0.068)) \\
> & = 1729.96\text{ kJ}
> \end{aligned}$$

### problem 3.3.iii

Based on the results obtained from [Problem 3.2](#problem%203.2) and [Problem 3.3](#problem%203.3), find the LHV of the MSW in country A. (<span style="color: red;">1 mark</span>)

> $$\begin{aligned}
> \text{LHV} & = \text{HHV} - \frac {Q_L} m \\
> & = 18261.3215 - \frac {1729.96} 1 \\
> & = 16531.3615\text{ kJ/kg} \\
> & \approx 16531.36\text{ kJ/kg}
> \end{aligned}$$

## problem 3.4

In order to make full use of the MSW, HKSAR decided to build a modern waste-to-energy incinerator for MSW treatment. The Hong Kong government plans to use MSW to produce 2500 MWh/day of electricty for public facilities operation. Given that the LHV of the MSW in Hong Kong is about 12,500 kJ/kg and the efficiency of the incinerqator for electricty generation is 15%. To reach the electricty demand, please calculate the minimum capacity of the incinerator. (<span style="color: red;">3 marks</span>)

> $$\begin{aligned}
> \text{minimum capacity} & = \text{minimum power} \cdot \frac 1 {\text{LHV}} \cdot \frac 1 {\text{efficiency}} \\
> & = \left( 2500 \times 10^6 \right) (3600) \frac 1 {12500 \times 10^3} \frac 1 {15\%} \\
> & = 4800000\text{ kg/day} \\
> & = 4800\text{ tpd}
> \end{aligned}$$
