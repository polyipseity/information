---
aliases:
  - HKUST ISOM 2700 quiz 3 derivative
  - HKUST ISOM2700 quiz 3 derivative
  - ISOM 2700 quiz 3 derivative
  - ISOM2700 quiz 3 derivative
tags:
  - flashcard/active/special/academia/HKUST/ISOM_2700/questions/quiz_3_derivative
  - language/in/English
---

# quiz 3 derivative

- HKUST ISOM 2700

> __question 1__
>
> | day | forecasted | actual |
> |:---:|:----------:|:------:|
> | 1   | 29         | 31     |
> | 2   | 30         | 33     |
> | 3   | 28         | 26     |
> | 4   | 33         | 28     |
> | 5   | 32         | 27     |
> | 6   | 29         | 28     |
>
> Forecast for day 7 using the following methods:
>
> 1. simple moving average with 4 periods
> 2. weighted moving average with $w_{t - 1} = 0.4, w_{t - 2} = 0.3, w_{t - 3} = 0.2, w_{t - 4} = 0.1$
> 3. exponential smoothing with $\alpha = 0.25$
>
> ---
>
> - solution: {@{1. 27.25 <br/> 2. 27.5 <br/> 3. 28.75}@}
> - explanation: {@{1. \(28+27+28+26\)/4=27.25 <br/> 2. 0.4\*28+0.3\*27+0.2\*28+0.1\*26=27.5 <br/> 3. 29+0.25\*\(28−29\)=28.75}@} <!--SR:!2028-06-05,830,330!2028-04-05,782,330-->

---

> __question 2__
>
> | day | forecasted | actual |
> |:---:|:----------:|:------:|
> | 1   | 29         | 31     |
> | 2   | 30         | 33     |
> | 3   | 28         | 26     |
> | 4   | 33         | 28     |
> | 5   | 32         | 27     |
> | 6   | 29         | 28     |
>
> What is mean absolute deviation \(MAD\) and tracking signal \(TS\) from day 3 to day 6 \(both days inclusive\).
>
> ---
>
> - solution: {@{MAD=3.25 <br/> TS=−4}@}
> - explanation: {@{MAD=\(2+5+5+1\)/4=3.25 <br/> TS=\(−2−5−5−1\)/3.25=−4}@} <!--SR:!fsrs,2029-09-20T05:03:20.972Z,1203,1202.68030072,1,2,9,0,0,2026-06-05T05:03:20.972Z!2028-07-10,843,330-->

---

> __question 3__
>
> Which statement\(s\) is/are correct about exponential smoothing? Assuming $0 < \alpha < 1$.
>
> 1. A large amount of data samples need to be stored using exponential smoothing.
> 2. A large alpha is more sensitive to random noise.
> 3. Past data points become increasingly less important.
> 4. It can be calculated as a weighted average of the most recent actual data and the most recent forecast data.
> 5. Past data points eventually does not have any influence on the forecast. \(Assume the number of data points are finite.\)
>
> ---
>
> - solution: {@{2, 3, 4}@} <!--SR:!fsrs,2029-09-06T05:03:05.492Z,1189,1189.40989388,1,2,9,0,0,2026-06-05T05:03:05.492Z-->

---

> __question 4__
>
> ABC company sells computers. The demand is 100 units daily. The fixed cost for an order is \$200. The holding cost is \$1 per unit daily. The purchasing cost is \$10 per unit. It takes 3 days to deliver computers from the supplier. If at least 200 computers are purchased together, the supplier offers a purchasing cost discount of \$5 per unit.
>
> What is the optimal order quantity?
>
> ---
>
> - solution: {@{200}@}
> - explanation: {@{$$Q^* = \sqrt{\frac {2DS} {H} } = \sqrt{\frac {2 \cdot 100 \cdot 200} {1} } = 200 \,.$$ <p> The purchasing cost discount does not affect the result. It does not change the optimal order quantity. Increasing the number of order quantity must be suboptimal. Decreasing the number of order quantity must also be suboptimal, and losing the purchasing cost discount makes it even more suboptimal.}@} <!--SR:!fsrs,2029-09-24T05:23:46.452Z,1206,1206.48213635,1,2,9,0,0,2026-06-06T05:23:46.452Z!2028-08-06,825,330-->

---

> __question 5__
>
> ABC company sells computers. The demand is 100 units daily. The fixed cost for an order is \$200. The holding cost is \$1 per unit daily. The purchasing cost is \$10 per unit. It takes 3 days to deliver computers from the supplier. If at least 200 computers are purchased together, the supplier offers a purchasing cost discount of \$5 per unit.
>
> What is the optimal total cost in a year \(365.25 days\)?
>
> ---
>
> - solution: {@{\$255&nbsp;675}@}
> - explanation: {@{From above, the optimal order quantity is 200. Thus the purchasing cost discount applies. <p> Calculate the daily cost: $$C_{\text{daily} } = \sqrt{2DSH} = \sqrt{2 \cdot 100 \cdot 200 \cdot 1} + 100 \cdot (10 - 5) = \$700 \,.$$ Calculate the cost in a year: $$C = 700 \cdot 365.25 = \$255\,675 \,.$$}@} <!--SR:!2027-05-21,518,310!fsrs,2029-09-02T05:03:24.488Z,1185,1185.06110203,1,2,9,0,0,2026-06-05T05:03:24.488Z-->

---

> __question 6__
>
> How to increase noise robustness for the following forecast methods?
>
> 1. simple moving average
> 2. weighted moving average
> 3. exponential smoothing
>
> ---
>
> - solution: {@{1. Increase lookback period. <br/> 2. Increase lookback period, or assign less weights to more recent data. <br/> 3. Decrease the smoothing alpha.}@} <!--SR:!2028-07-02,838,330-->

---

> __question 7__
>
> Which statement\(s\) is/are correct about mean absolute deviation \(MAD\) and tracking signal \(TS\)?
>
>
> 1. If MAD is zero, TS must be zero.
> 2. MAD can be positive or negative.
> 3. The smaller the MAD, the better the predictions.
> 4. The absolute value of TS should be within 3.75 for good predictions.
> 5. TS can be positive or negative.
> 6. Theoretically, MAD can be zero.
> 7. The larger the TS, the better the predictions.
> 8. Theoretically, TS can be zero.
>
> ---
>
> - solution: {@{1, 3, 4, 5, 6, 8}@} <!--SR:!2028-03-25,776,330-->

---

> __question 8__
>
> Consider an EOQ model. Which of the following changes decrease cost per unit?
>
> 1. increase demand
> 2. decrease holding cost per unit per time
> 3. decrease setup cost per order
> 4. decrease purchasing cost per unit
>
> ---
>
> - solution: {@{1, 2, 3, 4}@} <!--SR:!2029-06-09,1132,350-->

---

> __question 9__
>
> DEF company sells toys. The demand is 25 units daily. The fixed cost for an order is \$200. The holding cost is \$1 per unit daily. The purchasing cost is \$10 per unit. It takes 3 days to deliver toys from the supplier.
>
> What is the optimal order quantity?
>
> ---
>
> - solution: {@{100}@}
> - explanation: {@{$$Q^* = \sqrt{\frac {2DS} {H} } = \sqrt{\frac {2 \cdot 25 \cdot 200} {1} } = 100 \,.$$}@} <!--SR:!fsrs,2029-09-04T05:03:03.730Z,1187,1186.51440941,1,2,9,0,0,2026-06-05T05:03:03.730Z!fsrs,2029-09-15T05:03:06.670Z,1198,1198.00877281,1,2,9,0,0,2026-06-05T05:03:06.670Z-->

---

> __question 10__
>
> DEF company sells toys. The demand is 25 units daily. The fixed cost for an order is \$200. The holding cost is \$1 per unit daily. The purchasing cost is \$10 per unit. It takes 3 days to deliver toys from the supplier.
>
> At what inventory level should you place an order?
>
> ---
>
> - solution: {@{75}@}
> - explanation: {@{25\*3=75}@} <!--SR:!2029-07-06,1153,350!fsrs,2029-09-09T05:03:19.369Z,1192,1192.29051934,1,2,9,0,0,2026-06-05T05:03:19.369Z-->
