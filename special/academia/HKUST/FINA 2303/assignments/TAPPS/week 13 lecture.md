---
aliases:
  - FINA 2303 TAPPS - week 13 lecture
  - FINA 2303 thinking aloud paired problem solving - week 13 lecture
  - FINA2303 TAPPS - week 13 lecture
  - FINA2303 thinking aloud paired problem solving - week 13 lecture
  - HKUST FINA 2303 TAPPS - week 13 lecture
  - HKUST FINA 2303 thinking aloud paired problem solving - week 13 lecture
  - HKUST FINA2303 TAPPS - week 13 lecture
  - HKUST FINA2303 thinking aloud paired problem solving - week 13 lecture
tags:
  - date/2025/04/30
  - flashcard/active/special/academia/HKUST/FINA_2303/assignments/TAPPS/week_13_lecture
  - language/in/English
---

# thinking aloud paired problem solving \(TAPPS\) - week 13 lecture

- HKUST FINA 2303
- thinking aloud paired problem solving \(TAPPS\)

## problem

Suppose we hold a portfolio with $\operatorname{SD}(R_p) = 40\%$. We want to add a stock to the portfolio and are choosing between two stocks with the same expected return. The percentage of the new stock in the portfolio would be 10%. Both stocks are fairly priced.

|                                       | Stock A | Stock B |
| ------------------------------------- |:-------:|:-------:|
| SD \(R<sub>i</sub>\)                  | 30%     | 40%     |
| Corr \(R<sub>i</sub>, R<sub>p</sub>\) | 1       | 0       |

$$\operatorname{Var}(R_p) = w_1^2 \operatorname{SD}(R_1)^2 + w_2^2 \operatorname{SD}(R_2)^2 + 2 w_1 w_2 \operatorname{SD}(R_1) \operatorname{SD}(R_2) \operatorname{Corr}(R_1, R_2)$$

1. Which stock should we buy? Justify your answer with clear explanation.
2. Compute the SD of the portfolios with stock A or stock B.

## submission

1. Stock B, because even though its SD is higher, its correlation with the original stock is 0 compared to 1 for the other stock. The effect of lack of correlation \(should\) outweighs that of higher SD.
2. Calculate the SD of 2 stocks:
    - SD of stock A: $$\begin{aligned} & \phantom = \sqrt{0.9^2 (40\%)^2 + 0.1^2(30\%)^2 + 2(0.9)(0.1) (1) (40\%) (30\%)} \\ & = \sqrt{1521\%^2} = 39\% \,. \end{aligned}$$
    - SD of stock B: $$\begin{aligned} & \phantom = \sqrt{0.9^2 (40\%)^2 + 0.1^2(40\%)^2 + 2(0.9)(0.1) (0) (40\%) (40\%)} \\ & = \sqrt{1312\%^2} \approx 36.2215405525\%  \end{aligned}$$
