---
aliases:
  - HKUST MATH 2411
  - HKUST MATH 2411 index
  - HKUST MATH2411
  - HKUST MATH2411 index
  - MATH 2411
  - MATH 2411 index
  - MATH2411
  - MATH2411 index
tags:
  - flashcard/active/special/academia/HKUST/MATH_2411/index
  - function/index
  - language/in/English
---

# index

- HKUST MATH 2411
- name: Applied Statistics

The content is in teaching order.

- grading schemes: take highest
  1. homework 10%, midterm exam 25%, final exam 65%
  2. homework 10%, midterm exam 0%, final exam 90%
- logistics
  - _R_, a programming language, is discussed and used in homework only.
  - homework: No late submissions.
  - midterm exam: No make-up exams.
    - datetime: 2024-10-20T14:00:00+08:00/2024-10-20T15:30:00+08:00
    - venue: LT-B (L1), LT-J (L2)
  - final exam: Make-up exam if absent due to special reasons, e.g. sick. Provide evidence.
- syllabus: descriptive statistics, probability theory, inferential statistics
  - syllabus / descriptive statistics: descriptive statistics
  - syllabus / probability theory: introduction to probability theory → discrete random variable, discrete probability distribution → continuous random variable, continuous probability distribution
  - syllabus / inferential statistics: estimation of parameters: point estimation, interval estimation → hypothesis testing → simple linear regression → other topics: goodness of fit test, etc.

## week 1 lecture

- time: 2024-09-02T10:30:00+08:00/2024-09-02T11:50:00+08:00
- course logistics
- [statistics](../../../../general/statistics.md)
  - statistics / definition (data) ::: a mathematical science that pertains to the _data_ collection, analysis, interpretation, explanation, and presentation <!--SR:!2024-09-20,16,290!2024-10-08,28,270-->
    - statistics / definition (data) / examples ::: Almost all fields of studies make use of data and statistics. _Statistical literacy_ has become a very important thing. <!--SR:!2024-10-07,23,270!2024-11-08,52,310-->
  - statistics / definition (decision making) ::: a method for processing and analyzing the collected data so as to help reduce the uncertainty inherent in _decision making_ <!--SR:!2024-11-12,56,310!2024-09-21,17,290-->
    - statistics / definition (decision making) / examples ::: choosing the best medication, driving to work in the shortest time, marketing (and choosing good grade courses) <!--SR:!2024-09-19,15,290!2024-09-20,16,290-->
  - statistics / definition (inference) ::: the art and science of answering questions and exploring ideas through the processes of gathering data, describing data, and _making inferences_ about a population on the basis of a smaller sample <!--SR:!2024-10-09,27,270!2024-09-19,15,290-->
  - statistics / branches ::: descriptive statistics, inferential statistics <!--SR:!2024-10-26,42,290!2024-09-19,15,290-->
- [descriptive statistics](../../../../general/descriptive%20statistics.md) ::: data collection, summarization, and presentation <!--SR:!2024-11-10,53,310!2024-11-11,55,310-->
  - descriptive statistics / methodologies ::: graphical (e.g. box plot, histogram), numerical (e.g. sample mean, sample median, sample quartile, sample variance), tabular (e.g. frequency table) <!--SR:!2024-10-27,40,290!2024-09-19,15,290-->
  - descriptive statistics / steps ::: collect (e.g. sampling, surveying) → classify (e.g. grouping) → characterize (e.g. sample mean) → present (e.g. box plot, table) <!--SR:!2024-09-23,14,250!2024-09-21,17,290-->
- [inferential statistics](../../../../general/statistical%20inference.md) ::: statistical procedures that use data from an observed _sample_ to make a conclusion about a _population_ <!--SR:!2024-10-23,36,290!2024-09-20,16,290-->
  - inferential statistics / key terms ::: _population_: a collection of all objects of interest, _sample_: an analyzed part of the _population_; _parameter_: a numerical measure describing a _population_, _statistic_: a numerical measure describing a _sample_ <!--SR:!2024-11-10,54,310!2024-09-20,16,290-->
  - inferential statistics / reasons for sampling ::: cost-effectiveness, practicality <!--SR:!2024-10-16,30,270!2024-11-14,57,310-->
  - inferential statistics / procedures ::: analysis of variance, estimation of parameters, goodness of fit test, hypothesis testing, probability distribution, regression, ... <!--SR:!2024-10-17,33,270!2024-09-19,15,290-->
    - inferential statistics / procedures / analysis of variance ::: used to test the difference between two or more means <!--SR:!2024-09-21,17,290!2024-10-21,34,290-->
    - inferential statistics / procedures / estimation of parameters ::: estimate unknown parameters of a population based on a sample of the population <!--SR:!2024-09-21,17,290!2024-09-20,16,290-->
    - inferential statistics / procedures / goodness of fit test ::: test how well a hypothesized statistical model (distribution) fits the observed samples <!--SR:!2024-10-22,36,270!2024-10-25,39,270-->
    - inferential statistics / procedures / hypothesis testing ::: test a statement about the unknown parameters <!--SR:!2024-11-07,51,310!2024-10-10,25,270-->
    - inferential statistics / procedures / probability distribution ::: mathematical function that gives the probabilities of occurrence of possible outcomes for an experiment <!--SR:!2024-09-21,17,290!2024-10-13,27,270-->
    - inferential statistics / procedures / regression ::: estimate the relationships between a dependent variable (output) and one or more independent variables (inputs) <!--SR:!2024-11-09,52,310!2024-11-16,59,310-->
  - inferential statistics / example
    - inferential statistics / example / question ::: Sampling 100 products from a process, 3 are defective. Is the process acceptable if the long-term (true/real) defective rate should not exceed 1%? <!--SR:!2024-11-08,52,310!2024-11-12,56,310-->
    - inferential statistics / example / answer (Sampling 100 products from a process, 3 are defective. Is the process acceptable if the long-term (true/real) defective rate should not exceed 1%?) ::: Assume the true defective rate of the process is 1%. Calculate the _probability of 10 or more products being defective in a random sample of 100 products_: $$\begin{aligned} P(\text{defective} \ge 3) & = 1 - P(\text{defective} < 3) \\ & = 1 - \sum_{k = 0}^2 P(\text{defective} = k) \\ & = 1 - \sum_{k = 0}^2 \binom {100} k (0.01)^k (0.99)^{100 - k} \\ & \approx 0.0794 \end{aligned}$$. This suggests the actual process likely has a true defective rate exceeding 1%. <!--SR:!2024-11-16,59,310!2024-09-19,15,290-->
  - inferential statistics / -duction ::: induction: draw conclusions on the population from the statistics of a sample; deduction: characterize hypothetical samples of a population from its parameters <!--SR:!2024-09-20,16,290!2024-10-08,26,270-->
- [_R_](../../../../general/R%20(programming%20language).md) ::: a programming language for statistical computing and data visualization <!--SR:!2024-09-21,17,290!2024-09-21,17,290-->
  - _R_ / website ::: <https://r-project.org/> <!--SR:!2024-11-17,60,310!2024-11-12,55,310-->
  - _R_ / components ::: _R_, _R_ console, RStudio <!--SR:!2024-09-21,17,290!2024-11-09,53,310-->
  - _R_ / help commands ::: `help.start()`: general help, `help(<foo>)`, `?<foo>`: help about `<foo>`, `apropos("<foo>")`: list all functions containing the string `<foo>`, `example(<foo>)`: show an example of the function `<foo>` <!--SR:!2024-09-22,13,250!2024-09-20,16,290-->
- [descriptive statistics](../../../../general/descriptive%20statistics.md)
  - descriptive statistics / why ::: communicate data and support your reasoning from data <!--SR:!2024-09-19,15,290!2024-11-10,53,310-->
  - descriptive statistics / methodologies
  - descriptive statistics / steps
- [data](../../../../general/data.md) (singular: datum) ::: a collection of measurements and identifiers, which can take make many forms like numbers, strings, etc. <!--SR:!2024-10-30,42,290!2024-09-20,16,290-->
  - data / reason for summarizing ::: Data cannot inform us well without summarization. Also see [DIKW pyramid](../../../../general/DIKW%20pyramid.md) (data, knowledge, information, wisdom). <!--SR:!2024-11-11,54,310!2024-09-21,17,290-->
  - data / reading a table ::: Data are commonly listed in a table. Each column is a characteristic which we called a _variable_. Each row (except for the header) is a datum which we called an _observation_. <!--SR:!2024-10-08,27,270!2024-11-09,52,310-->
  - data / types of variables ::: _categorical/qualitative_: distinct categories or labels, and can be subdivided into _nominal_ if the categories cannot be ranked or _ordinal_ if they can be ranked; _quantitative_: numerical, and can be subdivided into _continuous_ if it arises from measurement or _discrete_ if it arises from counting <!--SR:!2024-11-12,56,310!2024-11-10,54,310-->
    - data / types of variables / importance ::: proper interpretation of data, proper selection of statistical analysis (e.g. not averaging nominal variables) <!--SR:!2024-11-12,56,310!2024-10-20,34,270-->
    - data / types of variables / note ::: Sometimes for data processing, categorical values are mapped to numbers. Do not mistake them for quantitative values! <!--SR:!2024-09-20,16,290!2024-09-20,16,290-->
- [descriptive statistics](../../../../general/descriptive%20statistics.md)
  - descriptive statistics / common measures ::: central tendency (location), variability (spread/dispersion) <!--SR:!2024-10-30,42,290!2024-09-20,16,290-->
    - central tendency ::: sample mean, sample median, trimmed sample mean, ... <!--SR:!2024-11-11,54,310!2024-11-10,54,310-->
    - variability ::: inter-quartile range, sample range, sample standard deviation, sample variance <!--SR:!2024-09-21,17,290!2024-11-13,56,310-->
  - sample mean ::: Suppose we have $n$ _samples_ of a random variable $x$, labeled $x_1, \ldots, x_n$. Then its _sample mean_ is $$\bar x = \frac 1 n \sum_{k = 1}^n x_n$$. <!--SR:!2024-11-15,58,310!2024-11-17,60,310-->
    - sample mean / _R_ ::: use `mean(...)` <!--SR:!2024-11-11,54,310!2024-09-21,17,290-->
  - sample median ::: Suppose we have $n$ _samples_ of a random variable $x$, labeled $x_1, \ldots, x_n$. They are sorted in increasing (or decreasing) order, i.e. $x_1 \le \ldots \le x_n$. Then its _sample median_ is $$\tilde x = \frac 1 2 \left(x_{\lfloor \frac {x + 1} 2 \rfloor} + x_ {\lceil \frac {x + 1} 2 \rceil} \right) = \begin{cases} x_{\frac {n + 1} 2} & \text{if }n\text{ is odd} \\ \frac 1 2 \left(x_{\frac x 2} + x_{\frac x 2 + 1} \right) & \text{if }n\text{ is even} \end{cases}$$. <!--SR:!2024-11-09,53,310!2024-11-14,57,310-->
  - sample mean vs sample median ::: The former is sensitive to outliers while the latter is not. This motivates trimming the outliers of the observations before calculating the former to reduce its sensitiveness to outliers (while still being more sensitive than the latter). <!--SR:!2024-09-20,16,290!2024-11-08,52,310-->
    - sample mean vs sample median / details ::: The former is used if the distribution is symmetric, unimodal and there are no outliers. Otherwise the latter is usually better. <!--SR:!2024-11-17,60,310!2024-11-12,55,310-->
    - sample mean vs sample median / trimmed (sample) mean ::: It is found by removing a certain percent of both the least and greatest values of the observations before computing its mean. <!--SR:!2024-11-12,55,310!2024-09-20,16,290-->
      - sample mean vs sample median / trimmed (sample) mean / notation (examples) ::: For example, $\bar x_{\operatorname{tr}(10)}$, called _10% trimmed mean_, is the mean after trimming the least 10% and greatest 10% of the observations. <!--SR:!2024-09-20,16,290!2024-09-20,16,290-->

## week 1 lecture 2

- time: 2024-09-02T10:30:00+08:00/2024-09-02T11:50:00+08:00
- [descriptive statistics](../../../../general/descriptive%20statistics.md)
  - sample [variance](../../../../general/variance.md) ::: Suppose we have $n$ _samples_ (with replacement) of a random variable $x$, labeled $x_1, \ldots, x_n$. Then its _unbiased sample variance_ is $$s^2_{n - 1} = \frac 1 {n - 1} \sum_{i = 1}^n (x_i - \bar x)^2$$. The _biased sample variance_, denoted $s^2_n$, replaces the factor $\frac 1 {n - 1}$ with $\frac 1 n$ in the above equation. Unless otherwise specified, the unbiased sample variance is used in this course. <!--SR:!2024-09-19,15,290!2024-09-19,15,290-->
    - sample [variance](../../../../general/variance.md) / dividing by $n - 1$ ::: $n - 1$ is also the _degree of freedom associated with the variance estimate_, which is the number of independent information pieces available for computing variability. Since $\bar x$ is usually the sample mean, which is determined from the sample mean, a degree of freedom is lost, as $\sum_{i = 1}^n (x_i - \bar x)$ is always forced to be zero. So the degree of freedom is $n - 1$. The original $n$ degrees of freedom comes from the $n$ observations being independent. This explains why dividing $n - 1$ instead of $n$ is _unbiased_. (If the $n$ observations are the entire population, then we divide by $n$ to get the _population variance_ instead.) <!--SR:!2024-09-19,15,290!2024-09-21,17,290-->
    - sample [variance](../../../../general/variance.md) / dividing by $n$ ::: However, if $\bar x$ is the population mean, then $\sum_{i = 1}^n (x_i - \bar x)$ is not forced to be zero, so the degree of freedom is still $n$ (from $n$ independent observations) instead. In this case, we divide by $n$ instead of $n - 1$ to get an _unbiased_ (sample/population) variance. This is regardless if the $n$ observations are a sample or the entire population. <!--SR:!2024-09-21,17,290!2024-09-19,15,290-->
    - sample variance / _R_ ::: use `var(...)` <!--SR:!2024-11-17,60,310!2024-11-10,53,310-->
  - sample standard deviation ::: It is the square root of the sample variance: $$s = \sqrt{s^2}$$. However, no matter if the sample variance is biased or unbiased, the resulting sample standard deviation is biased. This is because the square root is a concave function and introduces additional negative bias (smaller than the corresponding population parameter). <!--SR:!2024-09-21,17,290!2024-09-21,17,290-->
    - sample standard deviation / _R_ ::: use `sd(...)` <!--SR:!2024-10-15,30,270!2024-09-21,17,290-->
  - sample range ::: It is defined as $$\text{range} = \max\set{x_i} - \min\set{x_i}$$. It is useful for statistical quality control (e.g. finding unusual outliers caused by bad measurement). <!--SR:!2024-09-20,16,290!2024-09-20,16,290-->
  - inter-quartile range (IQR) ::: It is defined as the range of the middle 50% of the data, or equivalently the third (75%) quartile subtracted by the first (25%) quartile: $$\text{IQR} = Q_3 - Q_1$$. It is also a measure of data dispersion. It can also eliminate problems with outliers. <!--SR:!2024-11-12,55,310!2024-09-20,16,290-->
    - inter-quartile range / _R_ ::: use `IQR(...)`, not `iqr` <!--SR:!2024-09-20,16,290!2024-09-21,17,290-->
  - variability / characteristics (common to most or all measures of variability) ::: All measures must be nonnegative. Most measures (exceptions: inter-quartile range, trimmed variants of statistics, ...) are zero [iff](../../../../general/if%20and%20only%20if.md) all data are the same (i.e. no spread). <!--SR:!2024-09-20,16,290!2024-09-21,17,290-->
- [data presentation](../../../../general/data%20and%20information%20visualization.md) ::: A graphical summary can communicate information better as people prefers to look at them rather than numbers. The method of presentation depends on the data _nature_ and visualization _goals_. <!--SR:!2024-10-24,40,290!2024-10-18,34,270-->
  - data presentation / quantitative data ::: box plot, frequency table, histogram, line chart, scatter plot, ... <!--SR:!2024-09-19,15,290!2024-10-23,39,290-->
  - data presentation / categorical data ::: bar chart, frequency table, pie chart, ... <!--SR:!2024-10-27,40,290!2024-10-28,41,290-->
  - line chart ::: It visualizes the trend of data over time well. Good for time-series data like stock prices. <!--SR:!2024-09-19,15,290!2024-09-19,15,290-->
    - line chart / reading ::: Start from the x-axis, then to the line, and lastly to the y-axis. <!--SR:!2024-11-16,59,310!2024-11-04,48,310-->
    - line chart / _R_ ::: use `plot(...)` <!--SR:!2024-09-21,17,290!2024-09-19,15,290-->
  - frequency table (quantitative) ::: Data is grouped into numerically ordered non-overlapping _categories_ or _class intervals_. Then a _summary table_ is drawn based on the grouped data. This condenses the data and allows for quicker data interpretation. <!--SR:!2024-09-21,17,290!2024-09-19,15,290-->
    - frequency table (quantitative) / procedure ::: Decide the number of class intervals (usually 5 to 20). Divide the data into that many intervals (usually covering the data range evenly). Adjust the class interval boundaries to avoid overlapping (as endpoints are inclusive). Construct the summary table. <!--SR:!2024-10-06,24,250!2024-10-26,39,290-->
    - frequency table (quantitative) / table headers ::: class interval, class midpoint, frequency, relative frequency, ... <!--SR:!2024-09-19,15,290!2024-10-15,29,270-->
  - histogram ::: A bar chart based on the frequency table. The x-axis labels the class intervals while the y-axis labels the frequency or density (relative frequency). <!--SR:!2024-09-21,17,290!2024-10-15,31,270-->
    - histogram / _R_ ::: use `hist(...)`, or `histogram(...)` after importing `library(lattice)` (different style) <!--SR:!2024-11-06,50,310!2024-11-06,50,310-->
- [descriptive statistics](../../../../general/descriptive%20statistics.md)
  - modality ::: It is the number of peaks (local modes) in the probability distribution. If there are no significant peaks, then it is _uniform_. If there are peaks, it may be _unimodal_ (1), _bimodal_ (2), ...; or _multimodal_ (>1) in general for multiple peaks. <!--SR:!2024-09-21,17,290!2024-11-11,55,310-->
    - [unimodaility](../../../../general/unimodality.md)
      - [§ unimodal probability distribution](../../../../general/unimodality.md#unimodal%20probability%20distribution)
    - [multimodal distribution](../../../../general/multimodal%20distribution.md)
  - [skewness](../../../../general/skewness.md) ::: Intuitively for graphs, a distribution is left-skewed if its tail is on the left, and vice versa for right-skewed. Otherwise, it is unskewed. Intuitively for numbers, a distribution is left-skewed if its mean is on the left of (smaller than) its median, and vice versa for right-skewed. Otherwise, it is unskewed. (But actually, said intuition is very very wrong sometimes... See the item below.) <!--SR:!2024-10-13,29,270!2024-10-08,26,270-->
    - [skewness § relationship of mean and median](../../../../general/skewness.md#relationship%20of%20mean%20and%20median) ::: The above intuition is _usually_ correct if the distribution is unimodal. But in general, there are no direct relationships between skewness, mean, and median. Furthermore, an unskewed distribution is not necessarily symmetric. But its converse, a symmetric distribution is unskewed, is true. <!--SR:!2024-09-19,15,290!2024-09-20,16,290-->
  - percentile, quantile (not quartile) ::: percentile, quantile: the number for which a specified portion of the sample or population is _equal to or less than_ (e.g. 90th percentile = 0.90 quantile, which means the number 90% of the sample or population is equal to or less than) <!--SR:!2024-10-06,24,270!2024-10-05,23,250-->
  - quartile ::: 1st quartile/lower quartile (Q1) = 25th percentile/0.25 quantile, 2nd quartile/median (Q2) = 50th percentile/0.50 quantile, 3rd quartile/upper quartile (Q3) = 75th percentile/0.75 quantile <!--SR:!2024-11-14,57,310!2024-09-19,15,290-->
    - quartile / procedure ::: One would find the quartiles hard to define when the number of samples is not divisible by 4. In this case, there are many different ways to define them, and we will use the following equation (this is different from that in HKDSE): $$x(p) = \frac 1 2 \left(x_{\lfloor np + 0.5 \rfloor} + x_{\lceil np + 0.5 \rceil} \right) \qquad p = 0.25, 0.50, 0.75$$. <!--SR:!2024-09-20,16,290!2024-09-19,15,290-->
    - quartile / _R_ ::: use `quantile(...)`, not `quartile` (note that the procedure of `quantile` is different from discussed above) <!--SR:!2024-11-10,54,310!2024-11-05,49,310-->
  - extrema ::: 0th quartile/minimum (Q0) = 0th percentile/0.00 quantile, 4th quartile/maximum (Q4) = 100th percentile/1.00 quantile <!--SR:!2024-09-19,15,290!2024-09-19,15,290-->
- [data presentation](../../../../general/data%20and%20information%20visualization.md)
  - box plot ::: A box plot labels the least data that is not an outlier (instead of the value $Q_1 - 1.5 \cdot \text{IQR}$), the lower quartile (Q1), median (Q2), upper quartile (Q3), and the greatest data that is not an outlier (instead of the value $Q_3 + 1.5 \cdot \text{IQR}$) as lines; and outliers as dots (with "min" and "max" labels on 2 of them). Additional lines are added so that the lines of Q1 and Q3 forms a rectangle (box). (See that thing on Canvas grade stats...?) <!--SR:!2024-09-20,16,290!2024-09-21,17,290-->
    - box plot / outliers ::: They $x$ are points that are $x \le Q_1 - 1.5 \cdot \text{IQR}$ or $x \ge Q_3 + 1.5 \cdot \text{IQR}$. Usually they are far away from the majority of the data and are _likely_ produced by measurement errors. Assuming a normal distribution, outliers are expected to appear rarely (~0.007). <!--SR:!2024-10-11,27,270!2024-09-19,15,290-->
    - box plot / _R_ ::: use `boxplot(...)` <!--SR:!2024-11-11,55,310!2024-09-20,16,290-->

## week 1 tutorial

- time: 2024-09-06T09:30:00+08:00/2024-09-06T10:20:00+08:00
- unscheduled

## week 2 lecture 1

- time: 2024-09-09T10:30:00+08:00/2024-09-09T11:50:00+08:00
- [data presentation](../../../../general/data%20and%20information%20visualization.md)
  - sample size / _R_ ::: use `length(...)` <!--SR:!2024-09-20,16,290!2024-09-21,17,290-->
  - first _n_ observations / _R_ ::: use `head(...)` <!--SR:!2024-11-06,50,310!2024-09-19,15,290-->
  - scatter plot ::: Plots data that comes as pairs. Good for visualizing relationship between two variables (e.g. regression). <!--SR:!2024-09-21,17,290!2024-10-07,25,270-->
    - scatter plot / _R_ ::: use `plot(...)` <!--SR:!2024-09-19,15,290!2024-11-11,54,310-->
  - frequency table (categorical) ::: Categorical data is already pre-grouped. Then a _summary table_ is drawn based on the categories. This condenses the data and allows for quicker data interpretation. <!--SR:!2024-11-15,58,310!2024-10-17,31,270-->
    - frequency table (categorical) / table headers ::: \<variable name\>, count, cumulative count (if ordinal), percent, cumulative percent (if ordinal), ... <!--SR:!2024-09-26,9,270!2024-10-23,37,270-->
  - pie chart ::: A filled circle showing proportions of different categories. <!--SR:!2024-09-19,15,290!2024-10-29,41,290-->
    - pie chart / _R_ ::: use `pie(...)` <!--SR:!2024-09-19,15,290!2024-11-09,53,310-->
  - bar chart ::: Bars showing counts of different categories. <!--SR:!2024-11-07,51,310!2024-09-19,15,290-->
    - bar chart / _R_ ::: use `barplot(...)` <!--SR:!2024-09-21,17,290!2024-09-21,17,290-->
- [sampling](../../../../general/sampling%20(statistics).md) ::: The act of creating a _sample_ from a _population_. It can be mainly classified into _probability sampling_ and _non-probability sampling_. <!--SR:!2024-09-20,16,290!2024-09-19,15,290-->
  - sampling / [errors](../../../../general/sampling%20(statistics).md#errors%20in%20sample%20surveys) ::: It is very important to sample correctly. Some biases include survivorship bias (as demonstration, unlikely related in most statistics), selection bias, non-response bias (participation bias), and voluntary response bias. <!--SR:!2024-10-17,33,270!2024-10-27,39,290-->
    - sampling / errors / survivorship bias ::: (as demonstration, unlikely related in most statistics) A famous example: Many planes were flying through enemy territories. Some survived. Engineers found holes on some parts of the survived planes. So they decided to reinforce those parts. But this did not improve survival rates. The actual best parts to reinforce were those without holes on the survived planes, because this implied the other planes did not survive because of holes in said parts. Hence the name. <!--SR:!2024-11-04,48,310!2024-10-17,32,270-->
    - sampling / errors / selection bias ::: A sample of convenience, which probably makes certain subjects more likely than others to be sampled. <!--SR:!2024-09-20,16,290!2024-10-29,41,290-->
    - sampling / errors / non-response bias (participation bias) ::: For example, parents are less likely to answer a survey at 6 pm because they are busy with children and dinner. <!--SR:!2024-09-20,16,290!2024-11-15,58,310-->
    - sampling / errors / voluntary response bias ::: Websites for posting reviews are more likely to get responses from customers who had very bad or very good experiences. <!--SR:!2024-10-08,24,270!2024-11-05,50,290-->
    - [sampling § sampling errors and biases](../../../../general/sampling%20(statistics).md#sampling%20errors%20and%20biases)
    - [sampling § non-sampling errors](../../../../general/sampling%20(statistics).md#non-sampling%20errors)
  - [probability sampling](../../../../general/sampling%20(statistics).md#sampling%20frame) ::: It supports strong statistical inferences from a sample to the population, minimizing selection bias. It involves random selection: any individual has a nonzero probability being picked, and said probability can be determined. <!--SR:!2024-09-21,17,290!2024-11-17,60,310-->
    - probability sampling / examples ::: cluster sampling, simple random sampling, stratified sampling, systematic sampling, stratified sampling, ... <!--SR:!2024-09-29,19,250!2024-11-02,45,290-->
    - probability sampling / simple random sampling ::: All individual in a population has equal probability of being selected. <!--SR:!2024-09-19,15,290!2024-09-21,17,290-->
    - probability sampling / systematic sampling ::: A _probabilistic_ method is used to select individuals of a population, such as sampling every third person. <!--SR:!2024-09-19,15,290!2024-09-21,17,290-->
    - probability sampling / stratified sampling ::: Individuals are split into groups based on certain characters. Then simple random sampling is applied on each group. <!--SR:!2024-11-12,55,310!2024-10-07,25,270-->
    - probability sampling / cluster sampling ::: Split the population into clusters and select some of the clusters (cannot select an individual in a cluster without selecting other in the same cluster). <!--SR:!2024-09-21,17,290!2024-09-20,16,290-->
  - [non-probability sampling](../../../../general/sampling%20(statistics).md#nonprobability%20sampling) ::: It supports weaker statistical inferences from a sample to the population. The advantage is that non-probability sampling may be more convenient in many contexts. <!--SR:!2024-09-21,17,290!2024-11-06,51,290-->
    - non-probability sampling / examples ::: convenience sampling, purposive sampling, voluntary response sampling, snowball sampling, ... <!--SR:!2024-09-20,16,290!2024-10-17,31,270-->
    - non-probability sampling / convenience sampling ::: Sampling whoever is most convenient to you, e.g. nearest people. <!--SR:!2024-09-21,17,290!2024-11-07,52,290-->
    - non-probability sampling / voluntary response sampling ::: Individuals in a population are made known of your sample and voluntarily decides to participate or not. <!--SR:!2024-10-10,26,270!2024-10-25,37,290-->
    - non-probability sampling / purposive sampling ::: A _non-probabilistic_ method is used to select individuals in a population. <!--SR:!2024-11-04,48,310!2024-11-11,55,310-->
    - non-probability sampling / snowball sampling ::: Some individuals of a population are sampled initially. Individuals sampled recruit other individuals for sampling. This recruitment chain continues indefinitely, hence snowballing. <!--SR:!2024-09-19,15,290!2024-11-05,49,310-->
