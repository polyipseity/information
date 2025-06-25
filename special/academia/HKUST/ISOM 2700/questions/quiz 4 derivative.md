---
aliases:
  - HKUST ISOM 2700 quiz 4 derivative
  - HKUST ISOM2700 quiz 4 derivative
  - ISOM 2700 quiz 4 derivative
  - ISOM2700 quiz 4 derivative
tags:
  - flashcard/active/special/academia/HKUST/ISOM_2700/questions/quiz_4_derivative
  - language/in/English
---

# quiz 4 derivative

- HKUST ISOM 2700

> __question 1__
>
> You are a news vendor. Each paper cost \$3. Each paper sells for \$10. There is no salvage value. The demand follows a normal distribution with mean of 100 and standard deviation of 25.
>
> What is the optimal expected profit?
>
> ---
>
> - solution: {@{\$618}@}
> - explanation: {@{Find critical fractile and corresponding z-score: $$\frac {C_u} {C_u + C_o} = \frac {10 - 3} {(10 - 3) + (3 - 0)} = 0.7 \implies z^* \approx 0.53 \,.$$ Optimal quantity: $$Q^* = 100 + 0.53 \cdot 25 = 113.25 \approx 114 \,.$$ Expected sales: $$\text{expected sales} = 114 - I(0.53) \cdot 25 = 114 - 0.7187 \cdot 25 = 96.0325 \approx 96 \,.$$ Expected profit: $$\operatorname E[P] = 96 \cdot 10 - 114 \cdot 3 = \$618 \,.$$}@}

---

> __question 2__
>
> You are a news vendor \(again\). But you have two newsstands.
>
> Each paper cost \$3. Each paper sells for \$10. There is salvage value of \$1 from recycling. The demand for a single newsstand follows a normal distribution with mean of 100 and standard deviation of 25. The demands of different newsstands are independent.
>
> What is the optimal order quantity for a single newsstand?
>
> ---
>
> - solution: {@{120}@}
> - explanation: {@{Find critical fractile and corresponding z-score: $$\frac {C_u} {C_u + C_o} = \frac {10 - 3} {(10 - 3) + (3 - 1)} \approx 0.7778 \implies z^* \approx 0.77 \,.$$ Optimal quantity: $$Q^* = 100 + 0.77 \cdot 25 = 119.25 \approx 120 \,.$$}@}

---

> __question 3__
>
> You are a news vendor \(again\). But you have two newsstands.
>
> Each paper cost \$3. Each paper sells for \$10. There is salvage value of \$1 from recycling. The demand for a single newsstand follows a normal distribution with mean of 100 and standard deviation of 25. The demands of different newsstands are independent.
>
> What is the combined demand for the two newsstands?
>
> ---
>
> - solution: {@{mean=200 <br/> standard deviation≈35.3553390593}@}
> - explanation: {@{mean=2\*100=200 <br/> standard deviation=25\*√\(2\)≈35.3553390593}@}

---

> __question 4__
>
> You are a news vendor \(again\). But you have two newsstands.
>
> Each paper cost \$3. Each paper sells for \$10. There is salvage value of \$1 from recycling. The demand for a single newsstand follows a normal distribution with mean of 100 and standard deviation of 25. The demands of different newsstands are independent.
>
> What is the optimal order quantity for the two newsstands?
>
> ---
>
> - solution: {@{228}@}
> - explanation: {@{Find critical fractile and corresponding z-score: $$\frac {C_u} {C_u + C_o} = \frac {10 - 3} {(10 - 3) + (3 - 1)} \approx 0.7778 \implies z^* \approx 0.77 \,.$$ Optimal quantity: $$Q^* = 200 + 0.77 \cdot 35.3553 \approx 227.2236 \approx 228 \,.$$}@}

---

> __question 5__
>
> Which statement\(s\) is/are correct about the newsvendor model?
>
> 1. Multiplying both understocking cost and overstocking cost by a constant multiplies the critical fractile by the same constant.
> 2. Critical fractile is affected by the demand.
> 3. A higher critical fractile increases optimal quantity.
> 4. Critical fractile increases with understocking cost and decreases with overstocking cost.
> 5. Optimal quantity is affected by the demand.
>
> ---
>
> - solution: {@{3, 4, 5}@}

---

> __question 6__
>
> You are an internet service provider. In an area, there are 20 more internet subscribers than you can concurrently handle at the same time. The number of inactive internet subscribers \(not using the internet\) follows a normal distribution with mean of 25 and standard deviation of 10.
>
> What is the probability of an internet subscriber needing to wait to use the internet?
>
> ---
>
> - solution: {@{27.43%}@}
> - explanation: {@{Find the standard z-score: $$z = \frac {(20 - 1) - 25} {10} = -0.6 \,.$$ The corresponding fractile is 0.2743.}@}

---

> __question 7__
>
> An airline offers two types of tickets. One expensive. one cheap. Cheap tickets have infinite demand and are booked in advance. Expensive tickets have a last-minute demand that follows a normal distribution of mean 100 and standard deviation 10.
>
> Expensive tickets are worth \$4&nbsp;000. Cheap tickets are worth \$2&nbsp;000, but the airline pays \$200 to the booking platform as commission.
>
> How many _cheap_ tickets should be booked in advance if the capacity is 200? What about 150? 100? 50?
>
> ---
>
> - solution: {@{200: 98, 150: 48, 100: 0, 50: 0}@}
> - explanation: {@{Critical fractile and its corresponding z-score: $$\frac {C_u} {C_u + C_o} = \frac {4000 - (2000 - 200)} {(4000 - (2000 - 200)) + (2000 - 200)} = 0.55 \implies z^* \approx 0.13 \,.$$ Optimal protection level: $$Q^* = 100 + 10 \cdot 0.13 = 101.3 \approx 102 \,.$$ <p> If the capacity is less than the optimal protection level, then the entire capacity should be reserved for _expensive_ tickets, i.e. no _cheap_ tickets.}@}

---

> __question 8__
>
> Your company sells game consoles at a price of $p_1$. Another company sells video games at a price of $p_2$.
>
> - demand for game consoles: $$D_1 = 1234 - 56p_1 + 78p_2$$
> - demand for video games: $$D_2 = 98765 - 43p_1 - 21 p_2$$
>
>
> If $p_2 = 19$, then what is the optimal $p_1^*$?
>
> ---
>
> - solution: {@{\$24.25}@}
> - explanation: {@{$$\begin{aligned} D_1 & = 1234 - 56p_1 + 78p_2 \\ R_1 & = 1234p_1 - 56p_1^2 + 78p_2 p_1 \\ p_1^* & = \frac {1234 + 78p_2} {2 \cdot 56} = \frac {1234 + 78 \cdot 19} {2 \cdot 56} = \$24.25 \end{aligned}$$}@}

---

> __question 9__
>
> Your company sells game consoles at a price of $p_1$. Another company sells video games at a price of $p_2$.
>
> - demand for game consoles: $$D_1 = 1234 - 56p_1 + 78p_2$$
> - demand for video games: $$D_2 = 98765 - 43p_1 - 21 p_2$$
>
>
> 1. What are the optimal prices $p_1^*$ and $p_2^*$?
> 2. If your company cooperates with the other company to maximize the total revenue, what are the optimal prices $p_1^*$ and $p_2^*$?
>
> ---
>
> - solution: {@{1. $(p_1^*, p_2^*) \approx (962.45942, 1366.1725)$ \(Yeah, the numbers make no sense... At least they are both positive.\) <br/> 2. $(p_1^*, p_2^*) \approx (1008.50905, 3191.97183)$ \(Same observations as above...\)}@}
> - explanation: {@{1. For 1: $$\begin{aligned} D_1 & = 1234 - 56p_1 + 78p_2 \\ R_1 & = 1234p_1 - 56p_1^2 + 78p_2 p_1 \\ p_1^* & = \frac {1234 + 78p_2} {112} \\ \\ D_2 & = 98765 - 43p_1 - 21p_2 \\ R_2 & = 98765p_2 - 43p_1 p_2 - 21p_2^2 \\ p_2^* & = \frac {98765 - 43p_1} {42} \\ \\ (p_1^*, p_2^*) & \approx (962.45942, 1366.1725) \,. \end{aligned}$$ <br/> 2. For 2: $$\begin{aligned} R & = 1234p_1 - 56p_1^2 + 78p_2 p_1 + 98765p_2 - 43p_1 p_2 - 21p_2^2 \\ & = 1234p_1 - 56p_1^2 + 35 p_1 p_2 + 98765 p_2 - 21p_2^2 \\ \\ p_1^* & = \frac {1234 + 35p_2} {112} \\ p_2^* & = \frac {98765 + 35p_1} {42} \\ \\ (p_1^*, p_2^*) & \approx (1008.50905, 3191.97183) \,. \end{aligned}$$}@}

---

> __question 10__
>
> Which statement\(s\) is/are correct about separate pricing and joint pricing?
>
> 1. Each of the separate revenues from optimal joint pricing must be at least that from optimal separate pricing.
> 2. Joint pricing cannot be applied to 3 products or above.
> 3. The total revenue from optimal joint pricing must be at least that from optimal separate pricing.
> 4. Two businesses always prefer cooperating with each other to adopt joint pricing over separate pricing to maximize their own revenues.
>
> ---
>
> - solution: {@{3}@}
