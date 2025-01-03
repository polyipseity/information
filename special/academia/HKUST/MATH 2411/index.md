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
    - venue: Lecture Theater B (L1), Lecture Theater J (L2)
  - final exam: Make-up exam if absent due to special reasons, e.g. sick. Provide evidence.
- syllabus: descriptive statistics, probability theory, inferential statistics
  - syllabus / descriptive statistics: descriptive statistics
  - syllabus / probability theory: introduction to probability theory → discrete random variable, discrete probability distribution → continuous random variable, continuous probability distribution
  - syllabus / inferential statistics: estimation of parameters: point estimation, interval estimation → hypothesis testing → simple linear regression → other topics: goodness of fit test, etc.

## children

- [assignments](assignments/)
- [MATH 2411 final examination cheatsheet](MATH%202411%20final%20examination%20cheatsheet.pdf)
- [MATH 2411 midterm examination cheatsheet](MATH%202411%20midterm%20examination%20cheatsheet.pdf)

## assessments

- [assignment 1](assignments/assignent%201/index.md): 20/20, graded
  - statistics: L1
    - mean: 15.09
    - low: 0
    - lower quartile: 11.25
    - median: 14
    - upper quartile: 20
    - high: 20
- [assignment 2](assignments/assignent%202/index.md): 20/20, graded
  - statistics: L1
    - mean: 17.37
    - low: 0
    - lower quartile: 17
    - median: 20
    - upper quartile: 20
    - high: 20
- [assignment 3](assignments/assignent%203/index.md): 20/20, graded
  - statistics: L1
    - mean: 16.94
    - low: 0
    - lower quartile: 16.25
    - median: 19.5
    - upper quartile: 20
    - high: 20
- [assignment 4](assignments/assignent%204/index.md): 20/20, graded
  - statistics: L1
    - mean: 16.79
    - low: 0
    - lower quartile: 16
    - median: 20
    - upper quartile: 20
    - high: 20

## week 1 lecture

- datetime: 2024-09-02T10:30:00+08:00/2024-09-02T11:50:00+08:00
- course logistics
- [statistics](../../../../general/statistics.md)
  - statistics / definition (data) ::@:: a mathematical science that pertains to the _data_ collection, analysis, interpretation, explanation, and presentation <!--SR:!2025-08-25,272,330!2025-01-21,105,290-->
    - statistics / definition (data) / examples ::@:: Almost all fields of studies make use of data and statistics. _Statistical literacy_ has become a very important thing. <!--SR:!2025-12-21,353,310!2025-06-24,228,330-->
  - statistics / definition (decision making) ::@:: a method for processing and analyzing the collected data so as to help reduce the uncertainty inherent in _decision making_ <!--SR:!2025-07-16,246,330!2025-06-22,218,310-->
    - statistics / definition (decision making) / examples ::@:: choosing the best medication, driving to work in the shortest time, marketing (and choosing good grade courses) <!--SR:!2025-07-24,251,330!2025-03-26,136,290-->
  - statistics / definition (inference) ::@:: the art and science of answering questions and exploring ideas through the processes of gathering data, describing data, and _making inferences_ about a population on the basis of a smaller sample <!--SR:!2025-01-19,101,290!2025-03-12,131,290-->
  - statistics / branches ::@:: descriptive statistics, inferential statistics <!--SR:!2025-04-18,174,310!2025-05-08,186,310-->
- [descriptive statistics](../../../../general/descriptive%20statistics.md) ::@:: data collection, summarization, and presentation <!--SR:!2025-04-21,162,310!2025-07-08,239,330-->
  - descriptive statistics / methodologies ::@:: graphical (e.g. box plot, histogram), numerical (e.g. sample mean, sample median, sample quartile, sample variance), tabular (e.g. frequency table) <!--SR:!2025-04-11,166,310!2025-05-18,193,310-->
  - descriptive statistics / steps ::@:: collect (e.g. sampling, surveying) → classify (e.g. grouping) → characterize (e.g. sample mean) → present (e.g. box plot, table) <!--SR:!2025-05-12,182,290!2025-07-01,212,310-->
- [inferential statistics](../../../../general/statistical%20inference.md) ::@:: statistical procedures that use data from an observed _sample_ to make a conclusion about a _population_ <!--SR:!2025-03-19,147,310!2025-08-11,261,330-->
  - inferential statistics / key terms ::@:: _population_: a collection of all objects of interest, _sample_: an analyzed part of the _population_; _parameter_: a numerical measure describing a _population_, _statistic_: a numerical measure describing a _sample_ <!--SR:!2025-07-03,235,330!2025-03-29,139,290-->
  - inferential statistics / reasons for sampling ::@:: cost-effectiveness, practicality <!--SR:!2025-02-06,112,290!2025-07-21,249,330-->
  - inferential statistics / procedures ::@:: analysis of variance, estimation of parameters, goodness of fit test, hypothesis testing, probability distribution, regression, ... <!--SR:!2025-02-16,122,290!2025-02-26,119,290-->
    - inferential statistics / procedures / analysis of variance ::@:: used to test the difference between two or more means <!--SR:!2025-09-20,294,330!2025-02-01,103,290-->
    - inferential statistics / procedures / estimation of parameters ::@:: estimate unknown parameters of a population based on a sample of the population <!--SR:!2025-10-17,316,330!2025-04-22,168,310-->
    - inferential statistics / procedures / goodness of fit test ::@:: test how well a hypothesized statistical model (distribution) fits the observed samples <!--SR:!2025-01-29,99,270!2025-03-26,152,290-->
    - inferential statistics / procedures / hypothesis testing ::@:: test a statement about the unknown parameters <!--SR:!2025-06-19,224,330!2025-01-13,95,290-->
    - inferential statistics / procedures / probability distribution ::@:: mathematical function that gives the probabilities of occurrence of possible outcomes for an experiment <!--SR:!2025-09-15,289,330!2025-10-26,297,290-->
    - inferential statistics / procedures / regression ::@:: estimate the relationships between a dependent variable (output) and one or more independent variables (inputs) <!--SR:!2025-06-24,227,330!2025-08-01,258,330-->
  - inferential statistics / example
    - inferential statistics / example / question ::@:: Sampling 100 products from a process, 3 are defective. Is the process acceptable if the long-term (true/real) defective rate should not exceed 1%? <!--SR:!2025-06-23,227,330!2025-07-12,242,330-->
    - inferential statistics / example / answer (Sampling 100 products from a process, 3 are defective. Is the process acceptable if the long-term (true/real) defective rate should not exceed 1%?) ::@:: Assume the true defective rate of the process is 1%. Calculate the _probability of 10 or more products being defective in a random sample of 100 products_: $$\begin{aligned} P(\text{defective} \ge 3) & = 1 - P(\text{defective} < 3) \\ & = 1 - \sum_{k = 0}^2 P(\text{defective} = k) \\ & = 1 - \sum_{k = 0}^2 \binom {100} k (0.01)^k (0.99)^{100 - k} \\ & \approx 0.0794 \end{aligned}$$. This suggests the actual process likely has a true defective rate exceeding 1%. <!--SR:!2025-05-20,185,310!2025-07-29,255,330-->
  - inferential statistics / -duction ::@:: induction: draw conclusions on the population from the statistics of a sample; deduction: characterize hypothetical samples of a population from its parameters <!--SR:!2025-09-02,279,330!2025-01-17,101,290-->
- [_R_](../../../../general/R%20(programming%20language).md) ::@:: a programming language for statistical computing and data visualization <!--SR:!2025-06-13,210,310!2025-10-12,311,330-->
  - _R_ / website ::@:: <https://r-project.org/> <!--SR:!2025-08-06,262,330!2025-07-07,237,330-->
  - _R_ / components ::@:: _R_, _R_ console, RStudio <!--SR:!2025-09-24,297,330!2025-06-28,231,330-->
  - _R_ / help commands ::@:: `help.start()`: general help, `help(<foo>)`, `?<foo>`: help about `<foo>`, `apropos("<foo>")`: list all functions containing the string `<foo>`, `example(<foo>)`: show an example of the function `<foo>` <!--SR:!2025-05-01,173,290!2025-08-31,277,330-->
- [descriptive statistics](../../../../general/descriptive%20statistics.md)
  - descriptive statistics / why ::@:: communicate data and support your reasoning from data <!--SR:!2025-08-04,259,330!2025-02-26,81,290-->
  - descriptive statistics / methodologies
  - descriptive statistics / steps
- [data](../../../../general/data.md) (singular: datum) ::@:: a collection of measurements and identifiers, which can take make many forms like numbers, strings, etc. <!--SR:!2025-04-16,168,310!2025-09-05,281,330-->
  - data / reason for summarizing ::@:: Data cannot inform us well without summarization. Also see [DIKW pyramid](../../../../general/DIKW%20pyramid.md) (data, knowledge, information, wisdom). <!--SR:!2025-04-30,170,310!2025-10-23,320,330-->
  - data / reading a table ::@:: Data are commonly listed in a table. Each column is a characteristic which we called a _variable_. Each row (except for the header) is a datum which we called an _observation_. <!--SR:!2025-01-17,101,290!2025-06-25,228,330-->
  - data / types of variables ::@:: _categorical/qualitative_: distinct categories or labels, and can be subdivided into _nominal_ if the categories cannot be ranked or _ordinal_ if they can be ranked; _quantitative_: numerical, and can be subdivided into _continuous_ if it arises from measurement or _discrete_ if it arises from counting <!--SR:!2025-05-06,175,310!2025-07-04,236,330-->
    - data / types of variables / importance ::@:: proper interpretation of data, proper selection of statistical analysis (e.g. not averaging nominal variables) <!--SR:!2025-07-15,245,330!2025-01-23,95,270-->
    - data / types of variables / note ::@:: Sometimes for data processing, categorical values are mapped to numbers. Do not mistake them for quantitative values! <!--SR:!2025-08-24,271,330!2025-04-06,145,290-->
- [descriptive statistics](../../../../general/descriptive%20statistics.md)
  - descriptive statistics / common measures ::@:: central tendency (location), variability (spread/dispersion) <!--SR:!2025-04-16,168,310!2025-05-05,179,310-->
    - central tendency ::@:: sample mean, sample median, trimmed sample mean, ... <!--SR:!2025-07-01,232,330!2025-07-05,237,330-->
    - variability ::@:: inter-quartile range, sample range, sample standard deviation, sample variance <!--SR:!2025-05-31,200,310!2025-07-12,241,330-->
  - sample mean ::@:: Suppose we have $n$ _samples_ of a random variable $x$, labeled $x_1, \ldots, x_n$. Then its _sample mean_ is $$\bar x = \frac 1 n \sum_{k = 1}^n x_n$$. <!--SR:!2025-07-28,255,330!2025-08-04,260,330-->
    - sample mean / _R_ ::@:: use `mean(...)` <!--SR:!2025-07-05,236,330!2025-10-02,303,330-->
  - sample median ::@:: Suppose we have $n$ _samples_ of a random variable $x$, labeled $x_1, \ldots, x_n$. They are sorted in increasing (or decreasing) order, i.e. $x_1 \le \ldots \le x_n$. Then its _sample median_ is $$\tilde x = \frac 1 2 \left(x_{\lfloor \frac {x + 1} 2 \rfloor} + x_ {\lceil \frac {x + 1} 2 \rceil} \right) = \begin{cases} x_{\frac {n + 1} 2} & \text{if }n\text{ is odd} \\ \frac 1 2 \left(x_{\frac x 2} + x_{\frac x 2 + 1} \right) & \text{if }n\text{ is even} \end{cases}$$. <!--SR:!2025-04-22,164,310!2025-07-20,248,330-->
  - sample mean vs sample median ::@:: The former is sensitive to outliers while the latter is not. This motivates trimming the outliers of the observations before calculating the former to reduce its sensitiveness to outliers (while still being more sensitive than the latter). <!--SR:!2025-04-23,169,310!2025-06-19,223,330-->
    - sample mean vs sample median / details ::@:: The former is used if the distribution is symmetric, unimodal and there are no outliers. Otherwise the latter is usually better. <!--SR:!2025-08-04,260,330!2025-05-04,173,310-->
    - sample mean vs sample median / trimmed (sample) mean ::@:: It is found by removing a certain percent of both the least and greatest values of the observations before computing its mean. <!--SR:!2025-07-08,238,330!2025-09-19,293,330-->
      - sample mean vs sample median / trimmed (sample) mean / notation (examples) ::@:: For example, $\bar x_{\operatorname{tr}(10)}$, called _10% trimmed mean_, is the mean after trimming the least 10% and greatest 10% of the observations. <!--SR:!2025-06-18,202,310!2025-04-01,141,290-->

## week 1 lecture 2

- datetime: 2024-09-04T10:30:00+08:00/2024-09-04T11:50:00+08:00
- [descriptive statistics](../../../../general/descriptive%20statistics.md)
  - sample [variance](../../../../general/variance.md) ::@:: Suppose we have $n$ _samples_ (with replacement) of a random variable $x$, labeled $x_1, \ldots, x_n$. Then its _unbiased sample variance_ is $$s^2_{n - 1} = \frac 1 {n - 1} \sum_{i = 1}^n (x_i - \bar x)^2$$. The _biased sample variance_, denoted $s^2_n$, replaces the factor $\frac 1 {n - 1}$ with $\frac 1 n$ in the above equation. Unless otherwise specified, the unbiased sample variance is used in this course. <!--SR:!2025-08-03,259,330!2025-08-21,273,330-->
    - sample [variance](../../../../general/variance.md) / dividing by $n - 1$ ::@:: $n - 1$ is also the _degree of freedom associated with the variance estimate_, which is the number of independent information pieces available for computing variability. Since $\bar x$ is usually the sample mean, which is determined from the sample mean, a degree of freedom is lost, as $\sum_{i = 1}^n (x_i - \bar x)$ is always forced to be zero. So the degree of freedom is $n - 1$. The original $n$ degrees of freedom comes from the $n$ observations being independent. This explains why dividing $n - 1$ instead of $n$ is _unbiased_. (If the $n$ observations are the entire population, then we divide by $n$ to get the _population variance_ instead.) <!--SR:!2025-08-30,281,330!2025-09-16,290,330-->
    - sample [variance](../../../../general/variance.md) / dividing by $n$ ::@:: However, if $\bar x$ is the population mean, then $\sum_{i = 1}^n (x_i - \bar x)$ is not forced to be zero, so the degree of freedom is still $n$ (from $n$ independent observations) instead. In this case, we divide by $n$ instead of $n - 1$ to get an _unbiased_ (sample/population) variance. This is regardless if the $n$ observations are a sample or the entire population. <!--SR:!2025-06-21,217,310!2025-07-25,251,330-->
    - sample variance / _R_ ::@:: use `var(...)` <!--SR:!2025-08-06,262,330!2025-06-25,227,330-->
  - sample standard deviation ::@:: It is the square root of the sample variance: $$s = \sqrt{s^2}$$. However, no matter if the sample variance is biased or unbiased, the resulting sample standard deviation is biased. This is because the square root is a concave function and introduces additional negative bias (smaller than the corresponding population parameter). <!--SR:!2025-04-10,147,290!2025-06-26,208,310-->
    - sample standard deviation / _R_ ::@:: use `sd(...)` <!--SR:!2025-02-05,111,290!2025-10-03,304,330-->
  - sample range ::@:: It is defined as $$\text{range} = \max\set{x_i} - \min\set{x_i}$$. It is useful for statistical quality control (e.g. finding unusual outliers caused by bad measurement). <!--SR:!2025-05-10,183,310!2025-08-13,262,330-->
  - inter-quartile range (IQR) ::@:: It is defined as the range of the middle 50% of the data, or equivalently the third (75%) quartile subtracted by the first (25%) quartile: $$\text{IQR} = Q_3 - Q_1$$. It is also a measure of data dispersion. It can also eliminate problems with outliers. <!--SR:!2025-07-09,239,330!2025-09-01,278,330-->
    - inter-quartile range / _R_ ::@:: use `IQR(...)`, not `iqr` <!--SR:!2025-08-12,262,330!2025-09-18,292,330-->
  - variability / characteristics (common to most or all measures of variability) ::@:: All measures must be nonnegative. Most measures (exceptions: inter-quartile range, trimmed variants of statistics, ...) are zero [iff](../../../../general/if%20and%20only%20if.md) all data are the same (i.e. no spread). <!--SR:!2025-09-06,282,330!2025-07-06,215,310-->
- [data presentation](../../../../general/data%20and%20information%20visualization.md) ::@:: A graphical summary can communicate information better as people prefers to look at them rather than numbers. The method of presentation depends on the data _nature_ and visualization _goals_. <!--SR:!2025-04-09,167,310!2025-02-28,133,290-->
  - data presentation / quantitative data ::@:: box plot, frequency table, histogram, line chart, scatter plot, ... <!--SR:!2025-03-27,141,290!2025-02-13,113,290-->
  - data presentation / categorical data ::@:: bar chart, frequency table, pie chart, ... <!--SR:!2025-04-11,166,310!2025-02-26,121,290-->
  - line chart ::@:: It visualizes the trend of data over time well. Good for time-series data like stock prices. <!--SR:!2025-07-10,238,330!2025-07-11,239,330-->
    - line chart / reading ::@:: Start from the x-axis, then to the line, and lastly to the y-axis. <!--SR:!2025-08-02,259,330!2025-06-01,209,330-->
    - line chart / _R_ ::@:: use `plot(...)` <!--SR:!2025-10-04,305,330!2025-07-26,252,330-->
  - frequency table (quantitative) ::@:: Data is grouped into numerically ordered non-overlapping _categories_ or _class intervals_. Then a _summary table_ is drawn based on the grouped data. This condenses the data and allows for quicker data interpretation. <!--SR:!2025-04-19,154,290!2025-05-24,187,310-->
    - frequency table (quantitative) / procedure ::@:: Decide the number of class intervals (usually 5 to 20). Divide the data into that many intervals (usually covering the data range evenly). Adjust the class interval boundaries to avoid overlapping (as endpoints are inclusive). Construct the summary table. <!--SR:!2025-05-05,149,250!2025-04-05,161,310-->
    - frequency table (quantitative) / table headers ::@:: class interval, class midpoint, frequency, relative frequency, ... <!--SR:!2025-06-01,193,310!2025-05-21,155,270-->
  - histogram ::@:: A bar chart based on the frequency table. The x-axis labels the class intervals while the y-axis labels the frequency or density (relative frequency). <!--SR:!2025-07-04,213,310!2025-01-06,81,270-->
    - histogram / _R_ ::@:: use `hist(...)`, or `histogram(...)` after importing `library(lattice)` (different style) <!--SR:!2025-06-07,213,330!2025-06-10,216,330-->
- [descriptive statistics](../../../../general/descriptive%20statistics.md)
  - modality ::@:: It is the number of peaks (local modes) in the probability distribution. If there are no significant peaks, then it is _uniform_. If there are peaks, it may be _unimodal_ (1), _bimodal_ (2), ...; or _multimodal_ (>1) in general for multiple peaks. <!--SR:!2025-10-16,315,330!2025-07-10,241,330-->
    - [unimodaility](../../../../general/unimodality.md)
      - [§ unimodal probability distribution](../../../../general/unimodality.md#unimodal%20probability%20distribution)
    - [multimodal distribution](../../../../general/multimodal%20distribution.md)
  - [skewness](../../../../general/skewness.md) ::@:: Intuitively for graphs, a distribution is __left-skewed__ or __negative-skewed__ if _its tail is on the left_, and vice versa for __right-skewed__ or __positive-skewed__. Otherwise, it is __unskewed__. Intuitively for numbers, a distribution is left-skewed if its mean is on the left of (smaller than) its median, and vice versa for right-skewed. Otherwise, it is unskewed. (But actually, said intuition is very very wrong sometimes... See the item below.) <!--SR:!2025-07-29,208,270!2025-09-11,266,290-->
    - [skewness § relationship of mean and median](../../../../general/skewness.md#relationship%20of%20mean%20and%20median) ::@:: The above intuition is _usually_ correct if the distribution is unimodal. But in general, there are no direct relationships between skewness, mean, and median. Furthermore, an unskewed distribution is not necessarily symmetric. But its converse, a symmetric distribution is unskewed, is true. <!--SR:!2025-05-11,177,310!2025-04-23,169,310-->
  - percentile, quantile (not quartile) ::@:: percentile, quantile: the number for which a specified portion of the sample or population is _equal to or less than_ (e.g. 90th percentile = 0.90 quantile, which means the number 90% of the sample or population is equal to or less than) <!--SR:!2025-02-09,79,250!2025-04-27,143,250-->
  - quartile ::@:: 1st quartile/lower quartile (Q1) = 25th percentile/0.25 quantile, 2nd quartile/median (Q2) = 50th percentile/0.50 quantile, 3rd quartile/upper quartile (Q3) = 75th percentile/0.75 quantile <!--SR:!2025-07-19,247,330!2025-05-15,191,310-->
    - quartile / procedure ::@:: One would find the quartiles hard to define when the number of samples is not divisible by 4. In this case, there are many different ways to define them, and we will use the following equation (this is different from that in HKDSE): $$x(p) = \frac 1 2 \left(x_{\lfloor np + 0.5 \rfloor} + x_{\lceil np + 0.5 \rceil} \right) \qquad p = 0.25, 0.50, 0.75$$. <!--SR:!2025-04-26,172,310!2025-03-18,135,290-->
    - quartile / _R_ ::@:: use `quantile(...)`, not `quartile` (note that the procedure of `quantile` is different from discussed above) <!--SR:!2025-04-28,169,310!2025-06-07,214,330-->
  - extrema ::@:: 0th quartile/minimum (Q0) = 0th percentile/0.00 quantile, 4th quartile/maximum (Q4) = 100th percentile/1.00 quantile <!--SR:!2025-07-28,254,330!2025-08-25,276,330-->
- [data presentation](../../../../general/data%20and%20information%20visualization.md)
  - box plot ::@:: A box plot labels the least data that is not an outlier (instead of the value $Q_1 - 1.5 \cdot \text{IQR}$), the lower quartile (Q1), median (Q2), upper quartile (Q3), and the greatest data that is not an outlier (instead of the value $Q_3 + 1.5 \cdot \text{IQR}$) as lines; and outliers as dots (with "min" and "max" labels on 2 of them). Additional lines are added so that the lines of Q1 and Q3 forms a rectangle (box). (See that thing on Canvas grade stats...?) <!--SR:!2025-04-02,142,290!2025-04-05,144,290-->
    - box plot / outliers ::@:: They $x$ are points that are $x \le Q_1 - 1.5 \cdot \text{IQR}$ or $x \ge Q_3 + 1.5 \cdot \text{IQR}$. Usually they are far away from the majority of the data and are _likely_ produced by measurement errors. Assuming a normal distribution, outliers are expected to appear rarely (~0.007). <!--SR:!2025-10-04,277,290!2025-03-18,135,290-->
    - box plot / _R_ ::@:: use `boxplot(...)` <!--SR:!2025-07-07,238,330!2025-09-11,285,330-->

## week 1 tutorial

- datetime: 2024-09-06T09:30:00+08:00/2024-09-06T10:20:00+08:00
- status: unscheduled

## week 2 lecture 1

- datetime: 2024-09-09T10:30:00+08:00/2024-09-09T11:50:00+08:00
- [data presentation](../../../../general/data%20and%20information%20visualization.md)
  - sample size / _R_ ::@:: use `length(...)` <!--SR:!2025-08-26,273,330!2025-10-01,302,330-->
  - first _n_ observations / _R_ ::@:: use `head(...)` <!--SR:!2025-06-11,217,330!2025-07-23,250,330-->
  - scatter plot ::@:: Plots data that comes as pairs. Good for visualizing relationship between two variables (e.g. regression). <!--SR:!2025-10-11,310,330!2025-01-09,93,290-->
    - scatter plot / _R_ ::@:: use `plot(...)` <!--SR:!2025-08-02,258,330!2025-07-06,237,330-->
  - frequency table (categorical) ::@:: Categorical data is already pre-grouped. Then a _summary table_ is drawn based on the categories. This condenses the data and allows for quicker data interpretation. <!--SR:!2025-05-14,180,310!2025-01-06,81,270-->
    - frequency table (categorical) / table headers ::@:: \<variable name\>, count, cumulative count (if ordinal), percent, cumulative percent (if ordinal), ... <!--SR:!2025-01-22,60,250!2025-02-05,105,270-->
  - pie chart ::@:: A filled circle showing proportions of different categories. <!--SR:!2025-07-27,253,330!2025-04-13,166,310-->
    - pie chart / _R_ ::@:: use `pie(...)` <!--SR:!2025-07-13,241,330!2025-06-29,232,330-->
  - bar chart ::@:: Bars showing counts of different categories. <!--SR:!2025-06-18,223,330!2025-08-22,274,330-->
    - bar chart / _R_ ::@:: use `barplot(...)` <!--SR:!2025-06-09,207,310!2025-10-15,314,330-->
- [sampling](../../../../general/sampling%20(statistics).md) ::@:: The act of creating a _sample_ from a _population_. It can be mainly classified into _probability sampling_ and _non-probability sampling_. <!--SR:!2025-04-26,172,310!2025-04-13,166,310-->
  - sampling / [errors](../../../../general/sampling%20(statistics).md#errors%20in%20sample%20surveys) ::@:: It is very important to sample correctly. Some biases include survivorship bias (as demonstration, unlikely related in most statistics), selection bias, non-response bias (participation bias), and voluntary response bias. <!--SR:!2025-01-17,92,270!2025-02-19,115,290-->
    - sampling / errors / survivorship bias ::@:: (as demonstration, unlikely related in most statistics) A famous example: Many planes were flying through enemy territories. Some survived. Engineers found holes on some parts of the survived planes. So they decided to reinforce those parts. But this did not improve survival rates. The actual best parts to reinforce were those without holes on the survived planes, because this implied the other planes did not survive because of holes in said parts. Hence the name. <!--SR:!2025-06-02,210,330!2025-02-13,119,290-->
    - sampling / errors / selection bias ::@:: A sample of convenience, which probably makes certain subjects more likely than others to be sampled. <!--SR:!2025-05-06,180,310!2025-04-20,173,310-->
    - sampling / errors / non-response bias (participation bias) ::@:: For example, parents are less likely to answer a survey at 6 pm because they are busy with children and dinner. <!--SR:!2025-05-09,182,310!2025-05-15,181,310-->
    - sampling / errors / voluntary response bias ::@:: Websites for posting reviews are more likely to get responses from customers who had very bad or very good experiences. <!--SR:!2025-01-04,88,290!2025-05-23,199,310-->
    - [sampling § sampling errors and biases](../../../../general/sampling%20(statistics).md#sampling%20errors%20and%20biases)
    - [sampling § non-sampling errors](../../../../general/sampling%20(statistics).md#non-sampling%20errors)
  - [probability sampling](../../../../general/sampling%20(statistics).md#sampling%20frame) ::@:: It supports strong statistical inferences from a sample to the population, minimizing selection bias. It involves random selection: any individual has a nonzero probability being picked, and said probability can be determined. <!--SR:!2025-06-05,204,310!2025-08-07,263,330-->
    - probability sampling / examples ::@:: cluster sampling, simple random sampling, stratified sampling, systematic sampling, ... <!--SR:!2025-03-16,120,250!2025-03-19,137,290-->
    - probability sampling / simple random sampling ::@:: All individual in a population has equal probability of being selected. <!--SR:!2025-08-08,263,330!2025-09-09,285,330-->
    - probability sampling / systematic sampling ::@:: A _probabilistic_ method is used to select individuals of a population, such as sampling every third person. <!--SR:!2025-05-06,183,310!2025-09-30,301,330-->
    - probability sampling / stratified sampling ::@:: Individuals are split into groups based on certain characters. Then simple random sampling is applied on each group. <!--SR:!2025-05-05,174,310!2025-09-08,265,290-->
    - probability sampling / cluster sampling ::@:: Split the population into clusters and select some of the clusters (cannot select an individual in a cluster without selecting other in the same cluster). <!--SR:!2025-01-29,82,270!2025-06-01,189,310-->
  - [non-probability sampling](../../../../general/sampling%20(statistics).md#nonprobability%20sampling) ::@:: It supports weaker statistical inferences from a sample to the population. The advantage is that non-probability sampling may be more convenient in many contexts. <!--SR:!2025-06-14,211,310!2025-05-30,205,310-->
    - non-probability sampling / examples ::@:: convenience sampling, purposive sampling, voluntary response sampling, snowball sampling, ... <!--SR:!2025-03-14,128,290!2025-01-06,81,270-->
    - non-probability sampling / convenience sampling ::@:: Sampling whoever is most convenient to you, e.g. nearest people. <!--SR:!2025-06-01,201,310!2025-06-04,209,310-->
    - non-probability sampling / voluntary response sampling ::@:: Individuals in a population are made known of your sample and voluntarily decides to participate or not. <!--SR:!2025-01-15,97,290!2025-03-26,152,310-->
    - non-probability sampling / purposive sampling ::@:: A _non-probabilistic_ method is used to select individuals in a population. <!--SR:!2025-05-25,202,330!2025-07-09,240,330-->
    - non-probability sampling / snowball sampling ::@:: Some individuals of a population are sampled initially. Individuals sampled recruit other individuals for sampling. This recruitment chain continues indefinitely, hence snowballing. <!--SR:!2025-07-28,253,330!2025-06-08,215,330-->

## week 2 lecture 2

- datetime: 2024-09-11T10:30:00+08:00/2024-09-11T11:50:00+08:00
- [probability](../../../../general/probability.md)
  - probability / subject ::@:: __Probability__ is the study of randomness. <!--SR:!2025-02-08,89,361!2025-02-04,85,358-->
  - probability / event ::@:: A __probability__ of an uncertain outcome / event is the chance (or likelihood) that it will occur. It must be in between 0 and 1, inclusively. <!--SR:!2025-02-09,90,361!2025-02-08,89,361-->
- random experiment ::@:: A __random experiment__ is a process that generates observations, and its outcome cannot be known beforehand and is only known after its performance. <!--SR:!2025-02-09,90,361!2025-02-09,90,361-->
- sample space ::@:: A __sample space__ is a set of _all_ possible outcomes of a random experiment, often denoted by _S_. Each outcome is called  __sample point__, denoted by _s_. <!--SR:!2025-02-06,87,358!2025-02-07,88,361-->
  - sample space / set-builder notation ::@:: To describe sample spaces for a large or infinite sample points, we can use the set-builder notation (__statement__ or __rule method__). It has the form: $$\set{x \mid P(x)} \,.$$, where _x_ is an indeterminate and _P_(_x_) is a predicate on the indeterminate. An element is in the set iff _P_(_x_) is true. <!--SR:!2025-02-07,88,361!2025-02-05,86,358-->
- event ::@:: An __event__ is any subset of the sample space, often denoted by capital letters. The set of all events is the __event space__. Equivalently, it is the power set of the sample space. <!--SR:!2025-01-18,68,341!2025-01-04,60,341-->
- Venn diagram ::@:: A __Venn diagram__ is a graph that can illustrate relationships among events. A rectangle is often used to represent the _sample space_, while circles often represent _events_ we are interested in. The circles may overlap, or be inside of one another completely. <!--SR:!2025-02-05,86,361!2025-02-09,90,361-->
- set theory
  - set theory / union ::@:: The __union__ of two events _A_ and _B_ is the event that at least one of _A_ or _B_ occur, denoted by _A_ ∪ _B_. It is defined as: $$A \cup B = \set{s \mid s \in A \text{ or } s \in B} \,.$$ <!--SR:!2025-02-04,85,358!2025-02-06,87,361-->
  - set theory / exhaustive ::@:: If the _union_ of several events is the sample space, the events are said to be __exhaustive__. <!--SR:!2025-02-10,91,361!2025-02-10,91,361-->
  - set theory / intersection ::@:: The __intersection__ of two events _A_ and _B_ is the even that both of _A_ and _B_ occur, denoted by _A_ ∩ _B_. It is defined as: $$A \cap B = \set{s \mid s \in A \text{ and } s \in B} \,.$$ A property: _A_ ∩ _B_ = _A_ iff _A_ is a subset of _B_ (_A_ ⊆ _B_). <!--SR:!2025-02-04,85,358!2025-02-11,92,361-->
  - set theory / disjoint ::@:: If two events have no common element, their intersection is an empty set Φ. The events are said to be __disjoint__. If a set of two or more events is __pairwise disjoint__, that is any two events from the set of events are _disjoint_, then the set of events are said to be __mutually exclusive__. <!--SR:!2025-01-18,68,341!2025-02-04,85,358-->
  - set theory / complement ::@:: The __complement__ of an event _A_ is the sample space excluding outcomes in event _A_, denoted $A^\complement, A^c, \overline A, A'$. Intuitively, it is the event that event _A_ does not occur. It is defined as $$A^\complement = \set{s \mid s \in S, s \notin A} \,.$$ Three properties: _S_<sup>c</sup> = Φ and Φ<sup>c</sup> = _S_, and an event and its complement must be _disjoint_. <!--SR:!2025-01-14,64,338!2025-02-10,91,361-->
  - set theory / difference ::@:: The __difference__ of two events _A_ and _B_ is the event that _A_ occurs but _B_ does not occur, denoted _A_ − _B_. It is defined as: $$A - B = \set{s \mid s \in A \text{ and } s \notin B} = A \cap B^\complement \,.$$ <!--SR:!2025-02-06,87,361!2025-02-05,86,361-->
  - set theory / commutative laws ::@:: $$\begin{aligned} A \cup B & = B \cup A \\ A \cap B & = B \cap A \end{aligned}$$ <!--SR:!2025-02-05,86,361!2025-02-08,89,361-->
  - set theory / associative laws ::@:: $$\begin{aligned} A \cup (B \cup C) & = (A \cup B) \cup C \\ A \cap (B \cap C) & = (A \cap B) \cap C \end{aligned}$$ <!--SR:!2025-02-08,89,361!2025-02-08,89,361-->
  - set theory / distributive laws ::@:: $$\begin{aligned} A \cup (B \cap C) & = (A \cup B) \cap (A \cup C) \\ A \cap (B \cup C) & = (A \cap B) \cup (A \cap C) \end{aligned}$$ <!--SR:!2025-02-11,92,361!2025-02-11,92,361-->
  - set theory / De Morgan's laws ::@:: $$\begin{aligned} (A \cup B)^\complement & = A^\complement \cap B^\complement \\ (A \cap B)^\complement & = A^\complement \cup B^\complement \\ \left(\bigcup_{k = 1}^n A_k \right)^\complement & = \bigcap_{k = 1}^n A_k^\complement \\ \left(\bigcap_{k = 1}^n A_k \right)^\complement & = \bigcup_{k = 1}^n A_k^\complement \end{aligned}$$ <!--SR:!2025-02-04,85,358!2025-02-07,88,361-->

## week 2 tutorial

- datetime: 2024-09-13T09:30:00+08:00/2024-09-13T10:20:00+08:00

## week 3 lecture

- datetime: 2024-09-16T10:30:00+08:00/2024-09-16T11:50:00+08:00
- assignments: [assignment 1](assignments/assignent%201/index.md)
- [probability axioms](../../../../general/probability%20axioms.md)
  - probability axioms / history ::@:: In 1933, a Russian mathematician named Andrei Nikolayevich Kolmogorov published the axiomatic structure of probability theory. <!--SR:!2025-01-18,68,341!2025-01-14,64,341-->
  - probability axioms / first axiom ::@:: The first axiom is __non-negativity__. The probability of any event in a sample space is nonnegative. <!--SR:!2025-02-07,88,361!2025-02-08,89,358-->
  - probability axioms / second axiom ::@:: The second axiom is __normalization__. The probability of the event that is the entire sample space is 1. <!--SR:!2025-02-08,89,361!2025-02-10,91,361-->
  - probability axioms / third axiom ::@:: The third axiom is __countable additivity__. For any _countable_ (finite or infinite) sequence of _mutually exclusive_ events, the probability of the union of them is the sum of their probabilities. <p> A set is _countable_ if it is finite or its element can be enumerated (has a one-to-one correspondence with the natural numbers). For example, the natural numbers are _countable_, while the real numbers or any nonempty intervals of it are not. <!--SR:!2025-02-05,86,358!2025-01-14,64,341-->
- probability measure ::@:: A __probability measure__, denoted _P_, is a real-valued function that assigns probabilities to events in a sample space. It is a __measure__, a mathematical abstraction of area, volume, probability, etc. <!--SR:!2025-09-10,255,358!2025-02-07,88,361-->
- probability axioms
  - probability axioms / probability of the empty set ::@:: The probability of the empty set is 0. Proof: $$\begin{aligned} P(\varnothing \cap \varnothing) & = P(\varnothing) + P(\varnothing) && \sigma\text{-additivity} \\ P(\varnothing) & = P(\varnothing) + P(\varnothing) \\ P(\varnothing) & = 0 \end{aligned}$$ <!--SR:!2025-02-09,90,361!2025-02-09,90,361-->
  - probability axioms / finite additivity ::@:: It is just the first axiom limited to finite sequences. Proof: Append an infinite number of empty sets to the finite sequence to make it infinite. Then _countable additivity_ can be applied. <!--SR:!2025-09-18,263,361!2025-02-08,89,361-->
  - probability axioms / monotonicity ::@:: If _A_ is a subset of _B_ then _P_(_A_) ≤ _P_(_B_). Proof: $$\begin{aligned} P(A) + P(B - A) & = P(B) && A \subseteq B, \sigma\text{-additivity} \\ P(A) & \le P(B) && \text{non-negativity} \end{aligned}$$ <!--SR:!2025-09-19,264,361!2025-02-08,89,358-->
  - probability axioms / numeric bound ::@:: The probability of any event is in between 0 and 1, inclusive. The lower bound is the non-negativity axiom, while the upper bound can be proved using the normalization axiom, monotonicity theorem, with the larger set being the sample space. <!--SR:!2025-02-05,86,361!2025-02-09,90,361-->
  - probability axioms / complement rule ::@:: The probability of the complement of any event is one minus the probability of that event. Proof: $$P\left(A^\complement \right) = P(S - A) = P(S) - P(A) = 1 - P(A)$$ <!--SR:!2025-02-06,87,361!2025-02-05,86,361-->
  - probability axioms / additive law ::@:: The __additive law__ is: $$P(A \cup B) = P(A) + P(B) - P(A \cap B) \,.$$ When _A_ and _B_ are disjoint, then _P_(_A_ ∩ _B_) is 0 and the above degenerates into the finite additivity theorem. <p> The above is a special case of the [inclusion–exclusion principle](../../../../general/inclusion–exclusion%20principle.md), which can handle any countable number of events: $$\mathbb {P} \left(\bigcup _{i=1}^{n}A_{i}\right)=\sum _{k=1}^{n}\left((-1)^{k-1}\sum _{I\subseteq \{1,\ldots ,n\} \atop |I|=k}\mathbb {P} (A_{I})\right) \,.$$ <!--SR:!2025-02-11,92,361!2025-01-18,68,341-->

## week 3 lecture 2

- datetime: 2024-09-18T10:30:00+08:00/2024-09-18T11:50:00+08:00
- status: unscheduled, public holiday: Day after Mid-Autumn Festival

## week 3 tutorial

- datetime: 2024-09-20T09:30:00+08:00/2024-09-20T10:20:00+08:00

## week 4 lecture

- datetime: 2024-09-23T10:30:00+08:00/2024-09-23T11:50:00+08:00
- content: Probably taught _R_ only...

## week 4 lecture 2

- datetime: 2024-09-25T10:30:00+08:00/2024-09-25T11:50:00+08:00
- probability of an event in a sample space with _finite equally likely_ outcomes ::@:: If each outcome in a sample space is _equally likely_, then the probability of an event is the number of outcomes in the event divided by the number of outcomes in the sample space. This can be proved using the sigma-additivity axiom on an event. <!--SR:!2025-02-08,89,361!2025-09-18,263,361-->
  - probability of an event in a sample space with _finite equally likely_ oucomes / _R_ ::@:: `sample(x=<sample space>, size=<number of times to sample>, replace=<sample with/without replacement?>)` <!--SR:!2025-02-06,87,358!2025-04-20,127,321-->
- Simpson's paradox ::@:: An example: If the probability of having a property is higher than that of another property for both of two groups separately, this may still not be the case when the groups are combined. <!--SR:!2025-02-04,85,358!2025-02-04,85,358-->
- [combinatorial principles](../../../../general/combinatorial%20principles.md) ::@:: rule of sum, rule of product <!--SR:!2025-02-05,86,361!2025-09-18,263,361-->
  - [§ rule of sum](../../../../general/combinatorial%20principles.md#rule%20of%20sum) ::@:: The __rule of sum__ is an intuitive principle stating that if there are _a_ possible outcomes for an event (or ways to do something) and _b_ possible outcomes for another event (or ways to do another thing), and the two events cannot both occur (or the two things can't both be done), then there are _a + b_ total possible outcomes for the events (or total possible ways to do one of the things). <!--SR:!2025-02-07,88,361!2025-02-11,92,361-->
  - [§ rule of product](../../../../general/combinatorial%20principles.md#rule%20of%20product) ::@:: The rule of product is another intuitive principle stating that if there are _a_ ways to do something and _b_ ways to do another thing, then there are _a_ · _b_ ways to do both things. <!--SR:!2025-02-08,89,361!2025-02-11,92,361-->
- [permutation](../../../../general/permutation.md) ::@:: The number of ways to order _k_ things from _n_ things is $$P(n, k) = \frac {n!} {(n - k)!} \,.$$ <!--SR:!2025-02-08,89,361!2025-02-10,91,361-->
  - permutation / circular permutation ::@:: If the ordering is circular, we need to divide the permutation by the size of the circle: $$\frac {P(n, k)} {k} = \frac {n!} {(n - k)! k} \,.$$ <!--SR:!2025-02-09,90,361!2025-02-09,90,361-->
- [combination](../../../../general/combination.md) ::@:: The number of ways to select _k_ things from _n_ things, where the order of selection does not matter, is $$C(n, k) = \binom n k = \frac {n!} {(n - k)! k!} = \frac {P(n, k)} {k!} \,.$$ <!--SR:!2025-02-11,92,361!2025-02-09,90,361-->
  - combination / partition ::@:: The number of ways to partition _n_ things into _r_ labelled partitions, where _k_<sub>_i_</sub> is the number of things in the _i_-th partition, is: $${n\choose k_1,k_2,\ldots,k_r} =\frac{n!}{k_1!k_2!\cdots k_r!} \,.$$ When there are only two partitions, this is the same as above, the number of ways to select _k_ things from _n_ things. <!--SR:!2025-02-06,87,361!2025-02-08,89,361-->

## week 4 tutorial

- datetime: 2024-09-27T09:30:00+08:00/2024-09-27T10:20:00+08:00

## week 5 lecture

- datetime: 2024-09-30T10:30:00+08:00/2024-09-30T11:50:00+08:00
- [conditional probability](../../../../general/conditional%20probability.md) ::@:: The __conditional probability__ of an event _A_ given that an event _B_, where _P_(_B_) > 0, has happened is: $$P(A \mid B) = \frac {P(A \cap B)} {P(B)} \,.$$ A property: $P(A \mid B) \ge P(A \cap B)$. <!--SR:!2025-02-07,88,361!2025-02-04,85,358-->
  - conditional probability / motivation ::@:: Knowing an event has happened may modify the probability of other events. Conditional probability can model this. <!--SR:!2025-09-19,264,361!2025-02-07,88,361-->
  - conditional probability / multiplicative rule ::@:: If _P_(_B_) > 0, then $$P(A \cap B) = P(A \mid B) P(B) \,.$$ This may be directly proved from the definition of conditional probability. Sometimes, the above is taken to be the definition of conditional probability instead (but not in this course). <!--SR:!2025-02-07,88,361!2025-02-04,85,358-->
  - conditional probability / conserved properties ::@:: Many other properties of probability hold under conditional probability. This can be easily seen by making the event that has happened to be the sample space instead. Example: $$\begin{aligned} P(A \mid B) & = 1 - P\left(A^\complement \mid B \right) \\ P(A \cup B \mid C) & = P(A \mid C) + P(B \mid C) - P(A \cap B \mid C) \\ P(A \cap B \mid C) & = P(A \mid B \cap C) P(B \mid C) \,. \end{aligned}$$ For the last example, if you reinterpret _C_ as the sample space, then $P(A \mid B \cap C)$ becomes $P(A \mid B)$. <!--SR:!2025-02-11,92,361!2025-02-11,92,361-->
- [chain rule](../../../../general/chain%20rule%20(probability).md) ::@:: generalization of the _multiplicative rule_ <!--SR:!2025-01-18,68,341!2025-02-10,91,361-->
  - [chain rule § two events](../../../../general/chain%20rule%20(probability).md#two%20events) ::@:: This is the same as the _multiplicative rule_. <!--SR:!2025-02-08,89,361!2025-02-04,85,358-->
  - [chain rule § finitely many events](../../../../general/chain%20rule%20(probability).md#finitely%20many%20events) ::@:: $$\begin{aligned} \mathbb P(A_1 \cap \ldots \cap A_n) & = \mathbb P(A_1 \cap \ldots \cap A_{n - 1}) \mathbb P(A_n \mid A_1 \cap \ldots \cap A_{n - 1}) \\ & = \mathbb P(A_1) \mathbb P(A_2 \mid A_1) \ldots \mathbb P(A_n \mid A_1 \cap \ldots \cap A_{n - 1}) \\ & = \prod_{k = 1}^n \mathbb P(A_k \mid A_1 \cap \ldots A_{k - 1}) \\ & = \prod_{k = 1}^n \mathbb P\left(A_k \,\Bigg|\, \bigcap_{j = 1}^{k - 1} A_j \right) \end{aligned}$$ <!--SR:!2025-02-05,86,361!2025-01-17,67,338-->
- [law of total probability](../../../../general/law%20of%20total%20probability.md#statement) ::@:: If $$\left\{ B_n : n = 1, 2, 3, \ldots \right\}$$ is a _finite or countably infinite_ set of _mutually exclusive_ and _collectively exhaustive_ events $$P(A)=\sum_n P(A\mid B_n)P(B_n) \,,$$ where, for any $n$, if $P(B_n) = 0$, then these terms are simply omitted from the summation since $P(A\mid B_n)$ is finite. <p> The set of $B_n$ is also known as a __partition__ of the sample space. <!--SR:!2025-01-04,60,341!2025-01-04,60,341-->
- [Bayes' theorem](../../../../general/Bayes'%20theorem.md#statement%20of%20the%20theorem) ::@:: __Bayes' theorem__ relates _P_(_A_|_B_) to _P_(_B_|_A_). It states $$P(A \mid B) = \frac {P(B \mid A) P(A)} {P(B)} \qquad P(B) \ne 0 \,.$$ (The course also states _P_(_A_) ≠ 0, but this is not actually required.) Sometimes the theorem is stated in the form where the denominator is replaced using the _law of total probability_. <!--SR:!2025-02-06,87,361!2025-02-05,86,361-->
- supplementary examples
  - [randomized response](../../../../general/randomized%20response.md) ::@::  It allows respondents to respond to sensitive issues (such as criminal behavior or sexuality) while maintaining confidentiality. <p> For example, we want to know about if how much of a population has done something. We prepare two questions: one asking if the person has done something, the other asking if the person has NOT done something. The person randomly choose one of the questions, the probability of which can be calculated by us (e.g. coin flip), to ask. <p> We do not know which question the person gets, so confidentiality is preserved. However, applying Bayes' theorem can still reveal the true prevalence in the population. Therefore, this is an application of Bayes' theorem. <!--SR:!2025-02-08,89,361!2025-02-09,90,361-->
  - the boy who cried wolf ::@:: We can apply Bayes' theorem to mathematically analyze this fable. <!--SR:!2025-09-19,264,361!2025-02-07,88,358-->
  - [Monty Hall problem](../../../../general/Month%20Hall%20problem.md)
- [independence](../../../../general/independence%20(probability%20theory).md) ::@:: Two events _A_ and _B_ are __independent__ iff $$P(A \cap B) = P(A) P(B) \,.$$ otherwise they are __dependent__. <p> Informally speaking, knowing either of the event has happened does not affect the probability of the other. <!--SR:!2025-02-07,88,361!2025-02-11,92,361-->
  - independence / equivalence ::@:: The following statements are equivalent: <ul> <li>_A_ and _B_ are independent.</li> <li>_A_ and _B_<sup>c</sup> are independent.</li> <li>_A_<sup>c</sup> and _B_ are independent.</li> <li>_A_<sup>c</sup> and _B_<sup>c</sup> are independent.</li> </ul> The above can be seen by seeing that the complement of an event is uniquely defined by the event. There is a one-to-one correspondence between a set and its complement (unless the sample space is the empty set, which is impossible for probability). <!--SR:!2025-02-06,87,361!2025-02-10,91,361-->
  - independence vs disjoint ::@:: Independent is not disjoint. End of story. <!--SR:!2025-02-10,91,361!2025-02-05,86,361-->
  - independence / pairwise independence ::@:: A finite set of events is __pairwise independent__ iff any two events from the set is _independent_. <p> Pairwise independence does NOT automatically imply _mutual independence_. <!--SR:!2025-02-07,88,361!2025-02-11,92,361-->
  - independence / mutual independence ::@:: A finite set of _n_ events is __mutually independent__ iff any 2 ≤ _k_ ≤ _n_ events from the set is _independent_. For the _independence_ of 2 ≤ _k_ events, this is simply: $$P\left(\bigcap_{i = 1}^k A_k \right) = \prod_{i = 1}^k A_k \,.$$ <p> Mutual independence automatically implies _pairwise independence_. However, note that the above statement must hold for all 2 ≤ _k_ ≤ _n_, not just _k_ = _n_. It is possible to create a sample space such that three events _A_, _B_, and _C_ are independent but none of the three events are _pairwise independent_. <!--SR:!2025-02-11,92,361!2025-10-02,272,361-->

## week 5 lecture 2

- datetime: 2024-10-02T10:30:00+08:00/2024-10-02T11:50:00+08:00
- assignments: [assignment 2](assignments/assignent%202/index.md)
- [random variable](../../../../general/random%20variable.md) (r.v.) ::@:: A __random variable__ (__r.v.__) is a mathematical function. Its _domain_ is the sample space. Its _range_ is a measurable space, usually a finite set of integers or the real numbers. The function need not be _injective_ (different samples need not map to different values). It is commonly denoted by capital letters, with its possible numerical values (also called __realizations__) by the same but lowercase letters. <p> A way to think about random variable is that it maps each outcome to a real number. <!--SR:!2025-02-04,85,358!2025-01-04,60,341-->
  - random variable / motivation ::@:: How do we describe random process more mathematically? Random variables can do so. <!--SR:!2025-02-09,90,361!2025-02-11,92,361-->
  - random variable / notations ::@:: Some notations for a random variable _X_ on the sample space _S_: $$\begin{aligned} \set{X = x} & = \set{s \in S \mid X(s) = x} \\ \set{X \le x} & = \set{s \in S \mid X(s) \le x} \\ P(X = x) & = P(\set{X = x}) \\ P(X \le x) & = P(\set{X \le x}) \end{aligned}$$ <!--SR:!2025-02-09,90,361!2025-02-08,89,361-->
  - random variable / types ::@:: There are two common types: _discrete_ random variables and _continuous_ random variables. If a random variable's range is _countable_ (finite or infinite), then the random variable is discrete. if a random variable's range is _uncountable_ and its _cumulative probability distribution_ (CDF) is _continuous everywhere_, then the random variable is continuous. <p> Other types not discussed here are _mixed_ random variables (a mix of discrete and continuous) and _singular_ random variables (neither discrete nor continuous). <!--SR:!2025-02-07,88,361!2025-01-04,60,341-->
- discrete random variable ::@:: A __discrete random variable__ has a _countable_ (finite or infinite) range. <!--SR:!2025-02-10,91,361!2025-02-04,85,358-->
  - [probability mass function](../../../../general/probability%20mass%20function.md) (PMF, pmf) ::@:: A __probability mass function__ (__PMF__, __pmf__) is a function that gives the probability that a _discrete random variable_ is exactly equal to some value. It is given by: $$p_X(x) = P(X = x) \,.$$ It is not defined for a continuous random variable. <p> The PMF has the following properties: $$\begin{aligned} \sum_x p_X(x) & = 1 \\ p_X(x) \ge 0 \,. \end{aligned}$$ <!--SR:!2025-02-11,92,361!2025-02-08,89,361-->
    - probability mass function / graph ::@:: To graph a PMF, draw an empty _xy_ graph. Maybe add a title to the graph. Draw _solid_ vertical lines on where the probability mass returns nonzero, representing its value at that point. Draw a _filled_ circle on top of each vertical line. <!--SR:!2025-01-23,65,360!2025-02-24,97,380-->
- [cumulative distribution function](../../../../general/cumulative%20distribution%20function.md) (CDF, cdf) ::@:: A __cumulative distribution function__ (__CDF__, __cdf__) of a real-valued random variable _X_ is the probability that _X_ will take a value less than or equal to _x_. It is given by: $$F_X(x) = P(X \le x) \,.$$ The probability that _X_ will take a value in between \(_a_, _b_\], where _a_ < _b_, is $$P(a < X \le b) = F_X(b) - F_X(a) \,.$$ <!--SR:!2025-02-05,86,361!2025-02-10,91,361-->
  - cumulative distribution function / properties ::@:: A CDF of any probability distribution _supported on the real numbers_ is a right-continuous monotone increasing function (a càdlàg function) $F: \mathbb R \rightarrow [0, 1]$ satisfying $\lim_{x \to -\infty} F(x) = 0$ and $\lim_{x \to +\infty} F(x) = 1$. <!--SR:!2025-02-07,88,361!2025-02-06,87,361-->
  - cumulative distribution function / existence and uniqueness ::@:: Every probability distribution _supported on the real numbers_, discrete, continuous, "mixed", as well as singular, is uniquely identified by its CDF. Thus, a CDF is defined for every probability distribution supported on the real numbers, even if its probability mass function (PMF) or probability density function (PDF) may be undefined. <!--SR:!2025-02-09,90,361!2025-01-18,68,341-->
  - cumulative distribution function / discrete random variable ::@:: The CDF of a discrete random variable is a non-decreasing step function. <!--SR:!2025-02-11,92,361!2025-01-17,67,338-->
    - cumulative distribution function / discrete random variable / graph ::@:: To graph a CDF for a discrete random variable, draw an empty _xy_ graph. Maybe add a title to the graph. Draw horizontal lines to indicate values of the CDF. Ensure the leftmost and rightmost lines touch the graph edge to show that it extends forever. Draw a _filled_ circle on the left endpoint of all horizontal lines except for the leftmost one. Draw a _hollow_ circle on the right endpoint of all horizontal lines except for the rightmost one. Optionally, draw _dotted_ or _dashed_ vertical lines to make the graph connected. <!--SR:!2025-01-07,52,340!2025-01-07,52,340-->
- [expected value](../../../../general/expected%20value.md) ::@:: The __expected value__ (__population mean__, __first moment__) is a generalization of the weighted average. Informally, the expected value is the mean of the possible values a random variable can take, weighted by the probability of those outcomes. It is commonly denoted $E(X)$. <!--SR:!2025-01-04,60,341!2025-02-09,90,361-->
  - expected value / discrete random variable ::@:: The expected value of a discrete random variable is the weighted average of all possible outcomes $\mathcal X$: $$\operatorname E[X] = \sum_{x \in \mathcal X} x p(x) \,.$$ This is only defined if the sum converges absolutely, so it is possible for a discrete random variable to have a undefined expected value. <p> Also, $$\operatorname E[g(X)] = \sum_{x \in \mathcal X} g(x) p(x) \,.$$ for an arbitrary function $g(x)$. <!--SR:!2025-02-11,92,361!2025-02-09,90,361-->
  - expected value / linearity ::@:: An important property is its linearity: $$\begin{aligned} E(b) & = b \\ E(aX) & = a E(X) \\ E(aX + b) & = a E(x) + b \\ E(aX + bY) & = a E(x) + b E(Y) \,, \end{aligned}$$ where _a_, _b_ are constants and _X_, _Y_ are random variables _independent_ from each other, i.e. $$P(X \le x, Y \le y) = P(X \le x) P(Y \le y) \,.$$ <!--SR:!2025-02-05,86,361!2025-02-10,91,361-->
- [variance](../../../../general/variance.md) ::@:: __Variance__ is the expected value of the squared deviation from the mean of a random variable. It is often represented by $\sigma ^{2}$, $s^{2}$, $\operatorname {Var} (X)$, $V(X)$, or $\mathbb {V} (X)$. <!--SR:!2025-02-10,91,361!2025-02-08,89,361-->
  - variance / discrete random variable ::@:: The variance fo a discrete random variable is $$\operatorname{Var}(X) = \sum_{x \in \mathcal X} \left((x - \mu)^2 p(x) \right) \,.$$ This is only defined if the above sum and $\mu$ exists, so it is possible for a discrete random variable to have undefined variance. <!--SR:!2025-02-04,85,358!2025-02-06,87,358-->
  - variance / properties ::@:: A well-known identity relating variance to expected value is $$\operatorname{Var}(X) = \operatorname E\left[X^2\right] - (\operatorname E[X])^2 = \operatorname E\left[X^2\right] - \mu^2 \,.$$ With this identity, the following properties can be proved: $$\begin{aligned} \operatorname{Var}(b) & = 0 \\ \operatorname{Var}(aX) & = a^2 \operatorname{Var}(X) \\ \operatorname{Var}(aX + b) & = a^2 \operatorname{Var}(X) \\ \operatorname{Var}(aX \pm bY) & = a^2 \operatorname{Var}(X) + b^2 \operatorname{Var}(Y) && \text{important, uses }\pm \,, \end{aligned}$$ where _a_, _b_ are constants and _X_, _Y_ are random variables _independent_ from each other, i.e. $$P(X \le x, Y \le y) = P(X \le x) P(Y \le y) \,.$$ <!--SR:!2025-01-17,67,341!2025-02-09,90,361-->

## week 5 tutorial

- datetime: 2024-10-04T09:30:00+08:00/2024-10-04T10:20:00+08:00

## week 6 lecture

- datetime: 2024-10-07T10:30:00+08:00/2024-10-07T11:50:00+08:00
- cumulative distribution function (CDF, cdf)
  - cumulative distribution function / continuous random variable ::@:: The CDF of a continuous random variable is a continuous monotone increasing function $F: \mathbb R \rightarrow [0, 1]$ satisfying $\lim_{x \to -\infty} F(x) = 0$ and $\lim_{x \to +\infty} F(x) = 1$. <!--SR:!2025-01-04,60,341!2025-02-10,91,361-->
    - cumulative distribution function / continuous random variable / graph ::@:: To graph a CDF for a continuous random variable, draw an empty _xy_ graph. Maybe add a title to the graph. Then graph it like a normal function. Ensure the leftmost and rightmost lines touch the graph edge to show that it extends forever. <!--SR:!2025-02-24,97,380!2025-02-24,97,380-->
- [probability density function](../../../../general/probability%20density%20function.md) (PDF, pdf) ::@:: The __probability density function__ (__PDF__, __pdf__) of an _absolutely continuous_ random variable is a function whose value at any given sample (or point) in the sample space (the set of possible values taken by the random variable) can be interpreted as providing a _relative likelihood_ that the value of the random variable would be equal to that sample. <p> Probability density is the probability per unit length, in other words, the _absolute likelihood_ for a continuous random variable to take on any particular value is 0 since there is an infinite set of possible values to begin with. <p> It is commonly denoted $f_X(x)$ for an absolutely continuous random variable _X_. <!--SR:!2025-02-08,89,361!2025-01-17,67,341-->
  - probability density function / properties ::@:: A PDF is nonnegative at all points, and its integral over the entire real numbers exists and equals to 1. <!--SR:!2025-02-05,86,358!2025-02-10,91,358-->
  - probability density function / from and to cumulative distribution function ::@:: For an _absolutely continuous_ random variable _X_, $$\begin{aligned} f_X(x) & = \frac {\mathrm d} {\mathrm dx} F_X(x) \\ F_X(x) & = \int_{-\infty}^x \! f_X(x) \,\mathrm{d}x \,. \end{aligned}$$ <p> Note that the _absolute continuity_ of $F_X(x)$ is required for $f_X(x)$ to be defined, or otherwise differentiating $F_X(x)$ and then integrating the resulting $f_X(x)$ may yield a different $F_X(x)$. <!--SR:!2025-01-04,60,341!2025-02-04,85,358-->
  - probability density function / to and from cumulative distribution function ::@:: For a _Lebesgue-integrable_ function $f_X(x)$, $$\begin{aligned} F_X(x) & = \int_{-\infty}^x \! f_X(x) \,\mathrm{d}x  \\ f_X(x) & = \frac {\mathrm d} {\mathrm dx} F_X(x) && \text{if }f_X(x)\text{ is continuous at }x \,. \end{aligned}$$ <p> Note that if two Lebesgue-integrable functions differ from each other on measure zero, then the resulting $F_X(x)$ is the same. So the PDF cannot uniquely determine a CDF. <!--SR:!2025-02-10,91,361!2025-02-10,91,361-->
  - probability density function / graph ::@:: To graph a PDF for an absolutely continuous random variable, draw an empty _xy_ graph. Maybe add a title to the graph. Then graph it like a normal function. Ensure the leftmost and rightmost lines touch the graph edge to show that it extends forever. <!--SR:!2025-02-23,96,380!2025-01-23,65,360-->
- expected value
  - expected value / continuous random variable ::@:: The expected value of a continuous random variable is the weighted average of all possible outcomes $\mathcal X$: $$\operatorname E[X] = \int_{-\infty}^{+\infty} \! x f(x) \,\mathrm{d}x = \int_{-\infty}^{+\infty} x \,\mathrm{d}F(x) \,.$$ This is only defined if the integral converges absolutely, so it is possible for a continuous random variable to have a undefined expected value. <p> Also, $$\operatorname E[g(X)] = \int_{-\infty}^{+\infty} \! g(x) f(x) \,\mathrm{d}x = \int_{-\infty}^{+\infty} g(x) \,\mathrm{d}F(x) \,.$$ for an arbitrary function $g(x)$. <!--SR:!2025-02-08,89,358!2025-01-04,60,338-->
- variance
  - variance / continuous random variable ::@:: The variance of a continuous random variable is $$\operatorname{Var}(X) = \int_{-\infty}^{+\infty} \! (x - \mu)^2 f(x) \,\mathrm{d}x = \int_{-\infty}^{+\infty} \! (x - \mu)^2 \,\mathrm{d}F(x) \,.$$ This is only defined if the integral exists, so it is possible for a continuous random variable to have undefined variance. <!--SR:!2025-02-07,88,361!2025-02-06,87,361-->
- [Chebyshev's inequality](../../../../general/Chebyshev's%20inequality.md) ::@:: The probability that a random variable deviates from its mean by at least $k\sigma$ is at most $1/k^{2}$, where $k$ is any positive constant and $\sigma$, required to be finite non-zero (also implies finite expected value $\mu$), is the standard deviation (the square root of the variance): $$P(\lvert X - \mu \rvert \ge k \sigma) \le \frac 1 {k^2} \,.$$ <!--SR:!2025-01-17,67,338!2025-01-04,60,338-->
  - Chebyshev's inequality / proof for continuous random variable ::@:: This a proof for continuous random variable, but a similar one applies for discrete random variable: $$\begin{aligned} P(\lvert X - \mu \rvert \ge k \sigma) & = \int_{\lvert x - \mu \rvert \ge k \sigma} \! f(x) \,\mathrm{d}x \\ & \le \int_{\lvert x - \mu \rvert \ge k \sigma} \! \frac {(x - \mu)^2} {k^2 \sigma^2} f(x) \,\mathrm{d}x \\ & = \frac 1 {k^2 \sigma^2} \operatorname{Var}(X) \\ & = \frac 1 {k^2} \,. \end{aligned}$$ <!--SR:!2025-01-04,60,338!2025-02-06,87,361-->

## week 6 lecture 2

- datetime: 2024-10-09T10:30:00+08:00/2024-10-09T11:50:00+08:00
- [binomial distribution](../../../../general/binomial%20distribution.md) ::@:: The __binomial distribution__ with parameters _n_ and _p_ is the discrete probability distribution of the number of successes in a sequence of $n \in \mathbb N_0$ independent experiments, each asking a yes–no question, and each with its own Boolean-valued outcome: success (with probability $p \in [0, 1]$) or failure (with probability $q = 1 - p$). It is denoted $B(n, p)$. <!--SR:!2025-01-04,60,338!2025-02-06,87,361-->
  - binomial distribution / random variable ::@:: A single trial (_n_ = 1) is also known as a __Bernoulli trial__. Its random variable is: $$p(x) = \begin{cases} p & \text{for }x = 1 \\ 1 - p & \text{for }x = 0 \\ 0 & \text{otherwise} \,, \end{cases}$$ or sometimes more conveniently, $$p(x) = \begin{cases} p^x (1 - p)^{1 - x} & \text{for }x \in \set{0, 1} \\ 0 & \text{otherwise} \,. \end{cases}$$ <!--SR:!2025-02-16,94,368!2025-01-26,73,348-->
  - binomial distribution / proof of being probability distribution ::@:: It is very easy to see that its probability mass function is nonnegative. To see that it sums up to 1, apply the binomial theorem in reverse. <!--SR:!2025-01-18,71,348!2025-02-19,97,368-->
  - binomial distribution / probability _mass_ function ::@:: For $X \sim B(n, p) \,,$ $$p_X(k) = \binom n k p^k (1 - p)^{n - k}\,.$$ <!--SR:!2025-02-08,89,361!2025-02-06,87,361-->
  - binomial distribution / mean ::@:: For $X \sim B(n, p) \,,$ $$\operatorname E[X] = np \,.$$ <!--SR:!2025-02-07,88,361!2025-02-09,90,361-->
  - binomial distribution / variance ::@:: For $X \sim B(n, p) \,,$ $$\operatorname{Var}(X) = np(1 - p) \,.$$ <!--SR:!2025-01-17,67,338!2025-02-09,90,361-->
  - binomial distribution / _R_: evaluate PMF ::@:: `dbinom(<number of successes>, size=<number of trials>, prob=<success probability>)` <!--SR:!2025-08-17,231,348!2025-03-18,101,308-->
  - binomial distribution / _R_: evaluate CDF ::@:: `pbinom(<number of successes>, size=<number of trials>, prob=<success probability>)` <!--SR:!2025-01-17,70,348!2025-01-26,73,348-->
  - binomial distribution / _R_: realize ::@:: `rbinom(<number of successes>, size=<number of trials>, prob=<success probability>)` <!--SR:!2025-06-01,156,328!2025-02-02,81,348-->
- [Poisson distribution](../../../../general/Poisson%20distribution.md) ::@:: The __Poisson distribution__ is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time if these events occur with a known constant mean rate and independently of the time since the last event. It can also be used for the number of events in other types of intervals than time, and in dimension greater than 1 (e.g., number of events in a given area or volume). It is denoted $\operatorname{Pois}(\lambda)$, where $\lambda \in (0, \infty)$ is the expectation of number of events in a given interval. <!--SR:!2025-06-01,170,338!2025-02-11,92,361-->
  - Poisson distribution / probability _mass_ function ::@:: For $X \sim \operatorname{Pois}(\lambda) \,,$ $$p_X(k) = \begin{cases} e^{-\lambda} \frac {\lambda^k} {k!} & \text{for }k \in \mathbb N_0 \\ 0 & \text{otherwise} \,. \end{cases}$$ <!--SR:!2025-04-22,132,321!2025-01-14,64,338-->
  - Poisson distribution / proof of being probability distribution ::@:: It is also very easy to see its probability mass function is nonnegative (in fact, positive). To see it sums up to 1, realize that the sum actually contains a Maclaurin expansion of $e^\lambda$. <!--SR:!2025-01-25,72,348!2025-01-26,73,348-->
  - Poisson distribution / mean ::@:: For $X \sim \operatorname{Pois}(\lambda) \,,$ $$\operatorname E[X] = \lambda \,.$$  To prove this, one will need to cancel _k_ in the denominator with the numerator in the sum when finding its expectation value. <!--SR:!2025-01-17,67,341!2025-02-10,91,361-->
  - Poisson distribution / variance ::@:: For $X \sim \operatorname{Pois}(\lambda) \,,$ $$\operatorname{Var}(X) = \lambda \,.$$  To prove this, one will need to cancel $k (k - 1)$ in the denominator with the numerator in the sum when finding its expectation value. <!--SR:!2025-02-10,91,361!2025-01-17,67,341-->
  - Poisson distribution / _R_: evaluate PMF ::@:: `dpois(<number of events>, lambda=<expectation value of number of events>)` <!--SR:!2025-01-18,71,348!2025-02-21,99,368-->
  - Poisson distribution / _R_: evaluate CDF ::@:: `ppois(<number of events>, lambda=<expectation value of number of events>)` <!--SR:!2025-06-15,168,328!2025-05-19,149,328-->
- [Poisson limit theorem](../../../../general/Poisson%20limit%20theorem.md) ::@:: The Poisson distribution may be used as an approximation to the binomial distribution, if $p_n$ is a sequence of real numbers in $[0, 1]$ such that the sequence $n p_n$ converges to a finite limit $\lambda$: $$\lim_{n \to \infty} \binom n k p_n^k (1 - p_n)^{n - k} = e^{-\lambda} \frac {\lambda^k} {k!} \,.$$ Informally, the Poisson distribution closely approximates the binomial distribution when _n_ is large. <!--SR:!2025-03-28,108,308!2025-06-12,165,328-->
- [continuous uniform distribution](../../../../general/continuous%20uniform%20distribution.md) ::@:: The __continuous uniform distribution__ describes uniform relative likelihood in between the interval _a_ and _b_ (both inclusive). It is denoted $U(a, b)$, where $-\infty < a < b < +\infty$. <!--SR:!2025-02-11,92,361!2025-01-18,68,341-->
  - continuous uniform distribution / probability _density_ function ::@:: For $X \sim U(a, b) \,,$ $$f(x) = \begin{cases} \frac 1 {b - a} & \text{for }a \le x \le b \\ 0 & \text{otherwise} \,. \end{cases}$$ <!--SR:!2025-02-09,90,361!2025-02-09,90,358-->
  - continuous uniform distribution / proof of being probability distribution ::@:: It is extremely easy to see its probability density function is nonnegative and integrates up to 1 over the real numbers. <!--SR:!2025-02-19,97,368!2025-02-18,96,368-->
  - continuous uniform distribution / mean ::@:: For $X \sim U(a, b) \,,$ $$\operatorname E[X] = \frac {a + b} 2 \,.$$ <!--SR:!2025-02-10,91,361!2025-02-06,87,361-->
  - continuous uniform distribution / variance ::@:: For $X \sim U(a, b) \,,$ $$\operatorname{Var}(X) = \frac {(b - a)^2} {12} \,.$$ <!--SR:!2025-02-06,87,361!2025-01-14,64,338-->
- [normal distribution](../../../../general/normal%20distribution.md) ::@:: The __normal distribution__ or __Gaussian distribution__ is important in statistics and is often used in the natural and social sciences to represent real-valued random variables whose distributions are not known. Their importance is partly due to the central limit theorem. It is denoted $\mathcal N(\mu, \sigma^2)$, where $\mu \in \mathbb R$ is the mean and $\sigma^2 \in \mathbb R_{> 0}$ is the variance.  <p> Note: When you see $\mathcal N(0, 100)$, do not mistake the 100 as the standard deviation! It is the variance. Almost screwed this up in the midterm examination... <!--SR:!2025-02-10,91,361!2025-02-04,85,358-->
  - normal distribution / probability _density_ function ::@:: For $X \sim \mathcal N(\mu, \sigma^2) \,,$ $$f(x) = \frac 1 {\sqrt{2\pi \sigma^2} } \exp\left(-\frac {(x - \mu)^2} {2 \sigma^2} \right) \,.$$ <!--SR:!2025-06-14,185,341!2025-01-14,64,341-->
  - normal distribution / proof of being probability distribution ::@:: It is also very easy to see its probability density function is nonnegative (in fact, positive). To see it integrates up to 1 over the real numbers, integrate with respect to $t = \frac {x - \mu} {\sqrt {2 \sigma^2} }$ first (substitution), then the resulting integral contains a Gaussian integral $\int_{-\infty}^\infty \! e^{-t^2} \,\mathrm{d}t$, which has no elementary antiderivative, but when evaluated over the real numbers, yields $\sqrt \pi$. <!--SR:!2025-01-14,67,348!2025-03-27,107,308-->
  - normal distribution / mean ::@:: For $X \sim \mathcal N\left(\mu, \sigma^2 \right) \,,$ $$\operatorname E[X] = \mu \,.$$  To prove this, turn the additional $x$ in the integrand into $(x - \mu + \mu)$, apply linearity of integration (split into $(x - \mu)$ and $\mu$), and then substitute $t = \frac {x - \mu} {\sqrt {2 \sigma^2} }$. Then the expression should contain a Gaussian integral and an integral that has an odd function as the integrand. The former integral is $\sqrt \pi$ and the latter integral is 0 by symmetry. <!--SR:!2025-01-18,68,341!2025-01-17,67,338-->
  - normal distribution / variance ::@:: For $X \sim \mathcal N\left(\mu, \sigma^2\right) \,,$ $$\operatorname{Var}(X) = \sigma^2 \,.$$  To prove this, substitute $t = \frac {x - \mu} {\sqrt {2 \sigma^2} }$, then substitute $e^{-t^2}$, and finally apply integration by part. The resulting expression should contain an expression that is 0 and a Gaussian integral, which evaluates to $\sqrt \pi$. <!--SR:!2025-01-18,68,341!2025-02-09,90,358-->
  - normal distribution / shape ::@:: All normal distribution have the bell-shaped regardless of its parameters. Changing the mean simply translates the shape, while increasing the variance fattens (becomes wider) and flattens (the maximum value becomes lower) the shape. <!--SR:!2025-02-17,95,368!2025-01-17,70,348-->
  - normal distribution / examples ::@:: human height, one component of the velocity of a turbulent wind flow, Galton board <!--SR:!2025-02-16,94,368!2025-02-20,98,368-->
  - normal distribution / standard normal distribution ::@:: The __standard normal distribution__ has the mean, $\mu$, 0, and the variance, $\sigma^2$, 1. Its CDF is commonly denoted by $\Phi(z)$ while its PDF is commonly denoted by $\varphi(z)$. <p> A property of its CDF due to the even symmetry of its PDF: $$\Phi(-z) = 1 - \Phi(z) \,.$$ <!--SR:!2025-01-26,73,348!2025-01-26,73,348-->
  - normal distribution / standardization ::@:: Any normal distribution can be __standardized__ by defining the random variable $$Z = \frac {X - \mu} {\sigma} \qquad X = \sigma Z + \mu \,.$$ Further, $$z = \frac {x - \mu} \sigma$$ is also known as the __standard score__ of the data _x_.  <p> After standardization, a standard normal table that provides $\Phi(z)$ for different values of _z_ may be used to evaluate the CDF of any normal distribution. (The table may not show negative values of _z_. In that case, you need to use the property of its CDF above.) <!--SR:!2025-02-11,92,361!2025-02-05,86,361-->
  - normal distribution / _R_: evaluate CDF ::@:: `pnorm(<value>[, mean=<mean>][, sd=<standard deviation>])` <!--SR:!2025-08-05,220,348!2025-01-26,73,348-->

## week 6 tutorial

- datetime: 2024-10-11T09:30:00+08:00/2024-10-11T10:20:00+08:00
- status: unscheduled, public holiday: Chung Yeung Festival

## week 7 lecture

- datetime: 2024-10-14T10:30:00+08:00/2024-10-14T11:50:00+08:00
- [moment](../../../../general/moment%20(mathematics).md) ::@:: The ___k_-th (population) moment__ (also called __raw moment__), which is about _the origin_ (not about _the mean_), of a random variable _X_ is defined by $$\operatorname E\left[X^k \right] \qquad k \in \mathbb N_{\ge 1} \,,$$ if _it exists_. (When _k_ = 0 (the "zeroth" moment), this always equal to 1, so we ignore it here.) <p> A _k_-th moment exists if $\operatorname E\left[\left\lvert X^k \right\rvert\right] < \infty$ (Lebesgue integrable). If the _n_-th moment exists _about any point_, so does the $(n - 1)$-th moment (and thus, all lower-order moments) _about every point_. <!--SR:!2025-02-19,97,368!2025-02-18,96,368-->
  - moment / population mean ::@:: The population mean is the 1st _raw_ moment. <!--SR:!2025-02-20,98,368!2025-02-20,98,368-->
- [central moment](../../../../general/central%20moment.md) ::@:: The ___k_-th (population) central moment__, which is about _the mean_ (not about _the origin_), of a random variable _X_ is defined by $$\operatorname E\left[(X - \operatorname E[X])^k\right] \qquad k \in \mathbb N_{\ge 1} \,,$$ if _it exists_. (When _k_ = 0 (the "zeroth" moment), this always equal to 1, so we ignore it here.) <p> A _k_-th central moment exists if $\operatorname E[\lvert X \rvert] < \infty$ and $\operatorname E\left[\left\lvert (X - \operatorname E[X])^k \right\rvert \right] < \infty$ (both Lebesgue integrable). If the _n_-th moment exists _about any point_ (including the value $\operatorname E[X]$), so does the $(n - 1)$-moment (and thus, all lower-order moments) _about every point_. <!--SR:!2025-01-17,70,348!2025-02-21,99,368-->
  - central moment / population variance ::@:: The population variance is the 2nd _central_ moment. <!--SR:!2025-02-17,95,368!2025-02-18,96,368-->
  - standardized (central) moment ::@:: The ___k_-th standardized (central) moment__ is the _k_-th (central) moment that is standardized by dividing by $\sigma^k$, where $\sigma$ is the standard deviation. Mathematically, $$\tilde \mu_k = \frac {\mu_k} {\sigma^k} = \frac {\operatorname E\left[(X - \mu)^k \right]} {\operatorname E\left[(X - \mu)^2 \right]^{k / 2} } = \operatorname E\left[\left(\frac {X - \mu} \sigma \right)^k \right] \,.$$ <p> Hence, the 1st standardized central moment is 0, the 2nd standardized central moment is 1, the 3rd standardized central moment is the _skewness_, the 4th standardized central moment is the _kurtosis_, etc. <!--SR:!2025-02-15,93,368!2025-02-21,99,368-->
    - standardized central moment / skewness ::@:: __Skewness__ is the 3rd _standardized_ central moment: $$\tilde \mu_3 = \operatorname E\left[\left(\frac {X - \mu} \sigma\right)^3 \right] = \frac {\mu_3} {\sigma^3} \,.$$ <!--SR:!2025-01-18,71,348!2025-01-25,72,348-->
    - standardized central moment / kurtosis ::@:: __Kurtosis__ is the 4th _standardized_ central moment: $$\tilde \mu_4 = \operatorname E\left[\left(\frac {X - \mu} \sigma\right)^4 \right] = \frac {\mu_4} {\sigma^4} \,.$$ <!--SR:!2025-01-25,72,348!2025-02-15,93,368-->
- [skewness](../../../../general/skewness.md)
  - [skewness § relationship of mean and median](../../../../general/skewness.md#relationship%20of%20mean%20and%20median)
- [moment-generating function](../../../../general/moment-generating%20function.md) (MGF, mgf) ::@:: The __moment-generating function__ (__MGF__, __mgf__) of _a real-valued random variable_ is defined as $$M_X(t) = \operatorname E\left[e^{tX} \right] \,,$$ provided that _this expectation exists (and is finite) for $t$ in some open neighborhood (open interval) of 0_. Otherwise, the moment generating function does not exist (e.g. Cauchy distributions). <p> In this course, unless otherwise specified, we assume the MGF exists. <!--SR:!2025-01-14,67,348!2025-02-18,96,368-->
  - moment-generating function / use ::@:: Its primary use is finding the _k_-th raw moment of a real-valued random variable _X_. The _k_-th raw moment is obtained by evaluating the _k_-th derivative of its moment-generating function at 0: $$\operatorname E\left[X^k \right] = M_X^{(k)}(0) = \left[\frac {\mathrm d^k} {\mathrm dt^k} M_X(t) \right]\Bigr|_{t = 0} \qquad k \in \mathbb N_0 \,.$$ When _k_ = 0, the "zeroth" raw moment is always 1, and the above formula also gives 1. <p> The above can be proved by differentiating the expectation, assuming the interchange of the differentiation and expectation operator is legitimate. <!--SR:!2025-01-18,71,348!2025-02-17,95,368-->
  - moment-generating function / binomial distribution ::@:: For $X \sim B(n, p) \,,$ $$M_X(t) = \left(pe^t + 1 - p \right)^n \,.$$ To find the above function, merge $e^{tk}$ into $p^k$ and apply the binomial theorem in reverse. <!--SR:!2025-07-23,214,348!2025-03-19,102,308-->
  - moment-generating function / normal distribution ::@:: For $X \sim \mathcal N\left(\mu, \sigma^2 \right) \,,$ $$M_X(t) = \exp\left(\mu t + \frac {\sigma^2 t^2} 2 \right) \,.$$ To find the above function, merge $e^{tx}$ into $e^{-\frac {(x - \mu)^2} {2\sigma^2} }$, extracting the constants out and completing the square in the exponent to get a Gaussian integral $\int_{-\infty}^\infty \! e^{-x^2} \,\mathrm{d}x$, which yields $\sqrt \pi$. Another way to prove the above that may be easier is by finding the moment-generating function $M_Z(t)$ for the _standard_ normal distribution _Z_ first, then use the fact $X = \sigma Z + \mu$. <!--SR:!2025-02-24,57,288!2025-03-25,105,308-->

## week 7 lecture 2

- datetime: 2024-10-16T10:30:00+08:00/2024-10-16T11:50:00+08:00
- [estimation theory](../../../../general/estimation%20theory.md) ::@:: It is a branch of statistics that deals with estimating the values of parameters based on measured empirical data that has a random component. The parameters describe an underlying physical setting in such a way that their value affects the distribution of the measured data. An _estimator_ attempts to approximate the unknown parameters using the measurements. <!--SR:!2025-01-07,19,356!2025-01-13,25,375-->
- [statistical population](../../../../general/statistical%20population.md) ::@:: It is a set of similar items or events which is of interest for some question or experiment. <p> A statistical population can be a group of existing objects (e.g. the set of all stars within the Milky Way galaxy) or a hypothetical and potentially infinite group of objects conceived as a generalization from experience (e.g. the set of all possible hands in a game of poker). <!--SR:!2025-01-07,19,356!2025-01-07,19,356-->
  - [statistical parameter](../../../../general/statistical%20parameter.md) ::@:: It is any quantity of a _statistical population_ that summarizes or describes an aspect of the population, such as a mean or a standard deviation. <!--SR:!2025-01-07,19,355!2025-01-13,25,376-->
- [sampling](../../../../general/sampling%20(statistics).md)
  - [statistic](../../../../general/statistic.md) ::@:: It is any quantity computed from values in a _sample_ which is considered for a statistical purpose. <p> Statistical purposes include estimating a population parameter, describing a sample, or evaluating a hypothesis. <!--SR:!2025-01-07,19,355!2025-02-06,42,355-->
- [estimator](../../../../general/estimator.md) ::@:: It is a rule for calculating an estimate of a given quantity based on observed data: thus the rule (the estimator), the quantity of interest (the estimand) and its result (the estimate) are distinguished. For example, the sample mean is a commonly used estimator of the population mean. <p> An estimator is itself a _random variable_. <!--SR:!2025-01-13,25,376!2025-01-13,25,375-->
  - [estimate](../../../../general/estimation.md) ::@:: It is is a value that is usable for some purpose even if input data may be incomplete, uncertain, or unstable. <!--SR:!2025-01-13,25,375!2025-01-13,25,376-->
  - estimator / notation ::@:: The parameter to be estimated (_estimand_), its _estimator_, and its _estimate_ (an realization of the estimator) usually have slightly different notations. <p> Usually, an estimate's symbol is uncapitalized compared to its corresponding estimator's symbol. <!--SR:!2025-01-07,19,356!2025-01-13,25,376-->
    - estimator / notation / examples ::@:: Examples: <br/> $\mu, \overline X, \overline x$ are respectively the population mean, sample mean, and calculated sample mean of actual samples. <br/> $\operatorname E\left[X^k\right], \overline {X^k}, \overline {x^k}$ are respectively the _k_-th population moment about the origin, _k_-th sample moment about the origin, and calculated _k_-th population moment about the origin of actual samples. <br/> $\sigma^2, S_n^2/S_{n - 1}^2, s_n^2/s_{n - 1}^2$ are respectively the population variance, _uncorrected/corrected_ sample variance, and calculated _uncorrected/corrected_ sample variance of actual samples. <br/> $\theta, \hat \theta, \theta$ are respectively a generic population parameter of a CDF $F(x; \theta, \ldots)$, its estimator, and its estimate given actual samples. Notice that the notations for the first and the last are the same. <!--SR:!2025-01-13,25,376!2025-03-17,75,375-->
- [sample mean](sample%20mean%20and%20covariance.md)
  - sample mean / equation ::@:: Given _N_ samples of a random variable _X_, its _sample mean_ is: $$\overline X = \frac 1 N \sum_{k = 1}^N X_k \,.$$ <!--SR:!2025-01-13,25,376!2025-01-13,25,375-->
  - sample mean / properties ::@:: It is _unbiased_: $\operatorname E[\overline X] = \mu_X$. It has a variance that is inversely proportional to the number of samples: $\operatorname{Var}(\overline X) = \frac {\sigma_X^2} N$. <!--SR:!2025-01-13,25,376!2025-03-16,74,376-->
- [sample covariance](sample%20mean%20and%20covariance.md)
  - sample covariance / equation ::@:: Given _N_ samples for each of the random variables _X_ and _Y_, their _sample covariance_ is: $$\operatorname{Cov}(X, Y) = \operatorname{Cov}(Y, X) = \frac 1 {N - 1} \sum_{k = 1}^N (X_k - \overline X) (Y_k - \overline Y) \,.$$ If _X_ and _Y_ are the same random variable _Z_, then it is also the _sample variance_ of _Z_: $$S_{Z, n - 1}^2 = \operatorname{Cov}(Z, Z) = \frac 1 {N - 1} \sum_{k = 1}^N (Z_k - \overline Z)^2 \,.$$ <!--SR:!2025-03-15,73,376!2025-01-13,25,376-->
  - [sample variance](../../../../general/sample%20variance.md)
    - sample variance / properties ::@:: It is _unbiased_ (for the _corrected_ one only): $\operatorname E\left[S_{X, n - 1}^2\right] = \sigma_X^2$. <!--SR:!2025-01-07,19,356!2025-01-13,25,376-->
- sample moment
  - sample moment / equations ::@:: Given _N_ samples of a random variable _X_, its _k-th raw sample moment_ and _k-th central sample moment_ are respectively: $$\begin{aligned} \overline {X^k} & = \frac 1 N \sum_{i = 1}^N X_i^k \\ \hat \mu_k & = \frac 1 N \sum_{i = 1}^N (X_i - \overline X)^k \,. \end{aligned}$$ <!--SR:!2025-01-13,25,375!2025-01-13,25,376-->
  - sample moment / properties ::@:: It is unbiased (for the _raw_ one only): $\operatorname E\left[\overline {X^k}\right] = \operatorname E\left[X^k\right]$. <!--SR:!2025-01-13,25,375!2025-01-13,25,376-->
- estimation theory
  - estimation theory / types ::@:: point estimation, interval estimation <!--SR:!2025-03-16,74,376!2025-01-13,25,376-->
- [point estimation](../../../../general/point%20estimation.md) ::@:: It involves the use of sample data to calculate a single value (known as a point estimate since it identifies a point in some parameter space) which is to serve as a "best guess" or "best estimate" of an unknown population parameter (for example, the population mean). <!--SR:!2025-03-18,76,376!2025-01-13,25,375-->
  - point estimation / methods ::@:: method of moments estimation (MME), maximum likelihood estimation (MLE; untaught), Bayesian estimation (untaught), etc. <!--SR:!2025-01-13,25,376!2025-01-13,25,376-->
- [interval estimation](../../../../general/interval%20estimation.md) ::@:: It is is the use of sample data to estimate an interval of possible values of a parameter of interest. <!--SR:!2025-01-13,25,375!2025-01-13,25,376-->
  - interval estimation / methods ::@:: (confidence interval) for the population mean, (confidence interval) for the population variance, etc. <!--SR:!2025-01-13,25,376!2025-01-07,19,356-->

## week 7 tutorial

- datetime: 2024-10-18T09:30:00+08:00/2024-10-18T10:20:00+08:00

## midterm examination

- datetime: 2024-10-20T14:00:00+08:00/2024-10-20T15:30:00+08:00, PT1H30M
- venue: Lecture Theater B (L1), Lecture Theater J (L2)
- [cheatsheet](MATH%202411%20midterm%20examination%20cheatsheet.pdf)
- grades: 48/50
  - statistics: L1
    - mean: 29.93 → 29.96
    - low: 2 → 2
    - lower quartile: 22 → 22
    - median: 30 → 30
    - upper quartile: 37 → 37
    - high: 50 → 50
  - statistics: L2
    - mean: 32.14
    - low: 8
    - lower quartile: 25
    - median: 32
    - upper quartile: 41
    - high: 50
- report
  - When you see $\mathcal N(0, 100)$, do not mistake the 100 as the standard deviation! It is the variance. Almost screwed this up in the midterm examination...
    - $\mathcal N(0, 100)$ (0) ::@:: The mean of the normal distribution is 0. The standard deviation of the normal distribution is 10, not 100. <!--SR:!2025-03-04,93,384!2025-03-12,99,384-->
  - Inputted $\binom {100} 1$ as 1 instead of 100 into the calculator when evaluating a binomial distribution...
    - $\binom {100} 1$ (-1) ::@:: It evaluates to 100, not 1. <!--SR:!2025-03-11,98,384!2025-03-13,100,384-->
  - Simplified $\frac 4 {b^2} \left(b\right)$ into $\frac 4 {b^3}$ instead of $\frac 4 b$... (-1)
  - time limit ::@:: Time limit was really really tight. Only 10 minutes left for checking, even if you are familiar with the content. <!--SR:!2025-01-21,25,387!2025-01-22,26,387-->
- check
  - datetime: 2024-10-29T10:00:00+08:00/2024-10-29T11:00:00+08:00, PT1H
  - venue: Room 3472 (Lift 25-26), Academic Building

## week 8 lecture

- datetime: 2024-10-21T10:30:00+08:00/2024-10-21T11:50:00+08:00
- [point estimation](../../../../general/point%20estimation.md)
  - point estimation / motivation ::@:: Assume there is a random variable _X_. We know its probability distribution type $F$ (CDF) but not all of its parameters $\theta, \ldots$: $X \sim F(x; \theta, \ldots)$. <p> From a sample of _X_, we want to estimate the unknown parameters. <!--SR:!2025-01-07,19,356!2025-01-13,25,375-->
  - [parameter space](../../../../general/parameter%20space.md) ::@:: It is the space of all possible parameter values that define a particular mathematical model. It is also sometimes called weight space, and is often a subset of finite-dimensional Euclidean space. <p> For CDFs with known parameters $\vec \varphi$ and unknown parameters $\vec \theta$ $F(x; \vec \varphi, \vec \theta)$, the family of CDFs is $\set{F(x; \vec \varphi, \vec \theta) : \vec \theta \in \vec \Theta}$, where $\Theta$ is the set of all reasonable values (depends on the given information) that $\vec \theta$ can take on. <!--SR:!2025-01-15,25,377!2025-03-21,77,377-->
  - point estimation / terminology ::@:: A statistic used to estimate a _parameter_ (or a _function of parameters_) is a _point estimator_ of that parameter. A realization of such a statistic is a _point estimate_ of the same parameter. <p> For example, <br/> $\overline X$ and $\overline x$ are respectively a point estimator and point estimate of $\mu = \operatorname E[X]$. <br/> $S_{n - 1}^2$ and $s_{n - 1}^2$ are respectively a point estimator and point estimate of $\sigma^2$. <br/> $S_n^2$ and $s_n^2$ are respectively a point estimator and point estimate of $\sigma^2$ (yes, it is the same as above). <!--SR:!2025-01-15,25,377!2025-01-16,26,377-->
  - point estimation / uniqueness ::@:: A parameter or a function of parameters can have multiple different point estimators and point estimates. <p> For example, $S_{n - 1}^2$ and $S_n^2$ are both point estimators for $\sigma^2$. The former is used for its _unbiasedness_, while the latter is used in method of moments (since $\overline {X^2} = (\overline X)^2 + S_n^2$ but $\overline {X^2} \ne (\overline X)^2 + S_{n - 1}^2$). <!--SR:!2025-01-15,25,377!2025-03-21,77,377-->
- [method of moments](../../../../general/method%20of%20moments%20(statistics).md) ::@:: You have _k_ parameters of a known distribution to estimate. Express the first _k_ raw population moments in terms of the _k_ parameters, assuming _they exist_: $\operatorname E[X], \ldots, \operatorname E\left[X^k\right]$. Calculate the _k_ raw sample moments: $\overline X, \ldots \overline {X^k}$. Equate them: $\operatorname E[X] = \overline X, \ldots, \operatorname E\left[X^k\right] = \overline {X^k}$. Now there are _k_ (nonlinear in general) equations to solve for _k_ parameters. If _a solution exist_, the solution produce the estimators for _k_ parameters. <!--SR:!2025-01-16,26,377!2025-01-16,26,377-->
  - method of moments / choice of moments ::@:: While choosing any _k_ raw moments would work, first _k_ raw moments are used as errors due to sampling increase with the order of the moments. Different choices yield different estimators. <p> For multiple random variables, there are many choices of raw moments leading to different estimators. <!--SR:!2025-01-15,25,377!2025-01-08,18,357-->
    - method of moments / choice of moments / in this course ::@:: In this course, we choose estimators that require the lowest moments. <p> For example, for $X \sim \operatorname{Poisson}(\lambda)$, since $\mu_X = \lambda$ and $\sigma_X^2 = \lambda$, $\hat \lambda = \overline X$ and $\hat \lambda = S_n^2$ are both point estimators for $\lambda$. We choose the first one. <!--SR:!2025-01-15,25,377!2025-03-20,76,377-->
  - method of moments / solving ::@:: Since the _k_ equations are nonlinear in general, there are no guarantees that tractable solutions exist. <p> For hand computation, if it is linear, you can use matrix methods. If not, you need to think of ways to substitute equations into each other. <p> In general, this involves changing the subject of $\overline {X^i} = \operatorname E\left[X^i\right]$ to a parameter $\theta_i$ to get a new equation, and then substitute this equation into other equations, until you have an equation that that is a function of a parameter in terms of the raw sample moments $\overline {X}, \ldots, \overline {X^k}$ _only_ (i.e. no other parameters $\theta_k$). <!--SR:!2025-01-14,24,377!2025-01-16,26,377-->
  - method of moments / estimator properties ::@:: The estimators are _consistent_ (under very weak assumptions) but _often biased_. <!--SR:!2025-01-14,24,377!2025-03-21,77,377-->
  - method of moments / advantages, disadvantages ::@:: Advantages are the estimators are _consistent_ (under very weak assumptions). <p> Disadvantages are the estimators are _often biased_, may not be _unique_, requires the existence of the first _k_ raw population moments, and only works well when the sample size is large. <!--SR:!2025-01-16,26,377!2025-02-06,38,337-->
- [point estimation](../../../../general/point%20estimation.md)
  - point estimation / properties ::@:: biasedness, consistency, efficiency, sufficiency <!--SR:!2025-01-15,25,377!2025-01-16,26,377-->
  - point estimation / biasedness ::@:: The expected value of an estimator may be written as: $$\operatorname E[\hat \theta] = \theta + b_N(\hat \theta) \,$$ where $b_N(\hat \theta)$ is the __bias__ (it _may_ be a function of the number of samples _N_ or other things). <p> The estimator is __unbiased__ if $b_N(\hat \theta) = 0$. If not _unbiased_, it is __biased__. Additionally an _biased_ estimator is _also_ __asymptotic unbiased__ if $\lim_{N \to +\infty} b_N(\hat \theta) = 0$. <p> Intuitively, this describes how _accurate_ (but not how _precise_) an estimator is. <!--SR:!2025-01-16,26,377!2025-01-16,26,377-->
  - point estimation / efficiency ::@:: An estimator for $\theta$, denoted $\hat \theta_1$, meter, denoted $\hat \theta_2$, if $\operatorname{Var}(\hat \theta_1) < \operatorname{Var}(\hat \theta_2)$, regardless of the actual value of $\theta$ (that is, is more _efficient_ than another estimator for the same parayou do not need to care about if the estimators are biased or not). <p> (In this course, the lecture slides only compare estimators that are _unbiased_ for _all possible values_ in the parameter space. And it also uses $\le$ instead of $<$...) <p> Intuitively, this describes how _precise_ (but not how _accurate_) an estimator is. <!--SR:!2025-01-14,24,377!2025-02-06,38,337-->
  - point estimation / consistency (untaught) ::@:: (untaught) It is about whether the point estimate stays close to the value when the parameter increases its (sample) size. <p> An estimator $T_n$ (in this context, _n_ is the number of samples, but can be other things) is __weakly consistent__ iff $$(\forall \theta \in \Theta) (\forall \varepsilon > 0) \left( \lim_{n \to \infty} \Pr(\lvert T_n - \theta \rvert > \varepsilon) = 0 \right)\,.$$ It is __strongly consistent__ iff $$\Pr\left(\lim_{n \to \infty} T_n = \theta \right) = 1 \quad \forall \theta \in \Theta\,.$$ <!--SR:!2025-01-05,6,317!2025-01-09,19,357-->
    - [consistent estimator](../../../../general/consistent%20estimator.md)
  - point estimation / sufficiency (untaught) ::@:: (untaught) Let X =\(X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>n</sub>\) be a random sample. A statistic T(X) is said to be __sufficient__ for θ (or for the family of distribution) if the conditional distribution of X given T is free from θ. <p> Intuitively, this is saying all information about θ contained in X is used in T. So conditioning X on T is independent of the actual value of θ. <p> The motivation is that statisticians can use sufficient statistics for analysis without losing relevant information of the original samples. <!--SR:!2025-01-14,24,377!2025-02-26,54,357-->
    - [sufficient statistic](../../../../general/sufficient%20statistic.md)

## week 8 lecture 2

- datetime: 2024-10-23T10:30:00+08:00/2024-10-23T11:50:00+08:00
- [interval estimation](../../../../general/interval%20estimation.md)
  - interval estimation / Why interval estimation instead of point estimation? ::@:: The latter cannot provide the precision (i.e. is the actual parameter close) and reliability (i.e. is the actual parameter _likely_ to be close) of the estimators. And sometimes, a range is more meaningful than a point. <!--SR:!2025-01-15,25,377!2025-01-16,26,377-->
  - interval estimation / terminology ::@:: __Random interval__ is the methodology. <p> Given a sample, the calculated random interval is a __confidence interval__ (or if using other methods, it could be __credible interval__, __likelihood interval__, etc. but we will not touch these). <!--SR:!2025-01-08,18,357!2025-01-15,25,377-->
  - random interval ::@:: Assume the parameter space is 1-dimensional (i.e. only 1 parameter). <p> In point estimation, we estimate a point in the parameter space using a statistic: $\hat \theta = T$. In interval estimation, we estimate a interval in the parameter space using two statistics: $\theta \in (T_1, T_2)$. Said interval is a __random interval__. <p> In general, the larger the interval, the more _reliable_ it is, but the less _precise_ it is, and vice versa. <!--SR:!2025-01-14,24,377!2025-01-16,26,377-->
- [confidence interval](../../../../general/confidence%20interval.md) ::@:: It is an interval which is expected to typically contain the parameter being estimated. More specifically, given a __confidence level__ $\gamma$ (95% and 99% are typical values), a CI is a random interval which contains the parameter being estimated $100\gamma$% of the time. <p> Note: This course uses $100(1 - \alpha)$% instead of $\gamma$%. So $\alpha$ is the probability that a random interval from a theoretical sample does not contain the population parameter. <!--SR:!2025-01-08,18,357!2025-01-14,24,377-->
  - confidence interval / definition ::@:: Wikipedia uses $$P(T_1 < \theta < T_2) \ge \gamma \,,$$, with equality replacing $\ge$ when the distribution is continuous. This course uses $$P(T_1 \le \theta \le T_2) \ge 1 - \alpha \,,$$ with equality replacing $\ge$ when the distribution is continuous. <!--SR:!2025-03-20,76,377!2025-01-16,26,377-->
  - confidence interval / construction ::@:: Simply find two statistics. <p> In practice, the two statistics are found _symmetrically_ (i.e. the confidence interval of a random sample has the same probability of lying on the left or right of and outside the actual population parameter), so that its precision is the highest (the interval is the smallest), given the underlying probability is unimodal and symmetric. <!--SR:!2025-01-14,24,377!2025-01-16,26,377-->
  - confidence interval / interpretations ::@:: It can be expressed in terms of a long-run frequency in _repeated samples_, probability with respect to _a single theoretical (yet to be realized) sample_, _statistical significance_, etc. <!--SR:!2025-01-16,26,377!2025-01-15,25,377-->
    - confidence interval / interpretations / misinterpretations ::@:: It does not mean for a given realized interval, there is a $1 - \alpha$% probability that the population parameter lies within the interval. The frequentist interpretation says once an interval is calculated, this interval _either covers_ the parameter value _or it does not_; it is no longer a matter of probability. <p> Less common misinterpretations include $1 - \alpha$% of the sample data lie within the confidence interval; and $1 - \alpha$% probability of the parameter estimate from a _repeat_ of the experiment falling within the confidence interval computed from a given experiment. <!--SR:!2025-01-08,18,357!2025-01-08,18,357-->
- [chi-squared distribution](../../../../general/chi-squared%20distribution.md) ::@:: It with $k$ _degrees of freedom_ is the distribution of a sum of the _squares_ of $k$ _independent standard normal random variables_. It is denoted $\chi^2(k)$ (in this course) or $\chi_k^2$. <!--SR:!2025-01-08,18,357!2025-01-16,26,377-->
  - chi-squared distribution / probability density function (PDF) ::@:: (Probably no need to memorize this...) $$f(y) = \begin{cases} \frac 1 {2^{n / 2} \Gamma(n / 2) } y^{n / 2 - 1} e^{-y / 2} & \text{if }y > 0, \\ 0 & \text{otherwise} \end{cases}$$ <!--SR:!2025-02-05,37,337!2025-02-04,36,337-->
  - chi-squared distribution / shape ::@:: It looks like a right-skewed (left-leaning) hill. The higher the $k$, the lower the peak and the fatter the hill. Note that for $k = 1, 2$, the peak is at $x = 0$. <!--SR:!2025-01-16,26,377!2025-01-09,19,357-->
  - chi-squared distribution / additivity ::@:: If $V \sim \chi^2(v)$ and $W \sim \chi^2(w)$ are _independent_, then $V + W \sim \chi^2(v + w)$. This is obvious from the definition... <!--SR:!2025-01-16,26,377!2025-01-15,25,377-->
  - chi-squared distribution / statistics ::@:: Let $Y \sim \chi^2(k)$. Then $\operatorname E[Y] = k$ and $\operatorname{Var}(Y) = 2k$. <!--SR:!2025-01-16,26,377!2025-02-25,53,357-->
- [Student's t-distribution](../../../../general/Student's%20t-distribution.md) ::@:: It is continuous probability distribution that generalizes the standard normal distribution. Like the latter, it is symmetric around zero and bell-shaped. (This course denotes it by $t(\nu)$ instead of $t_\nu$.) <p> However, it has heavier tails and the amount of probability mass in the tails is controlled by the parameter $\nu$. For $\ \nu =1\ {}$ the Student's _t_ distribution $t_{\nu }$ becomes the standard [Cauchy distribution](../../../../general/Cauchy%20distribution.md), which has very ["fat" tails](../../../../general/fat-tailed%20distribution.md); whereas for $\ \nu \rightarrow \infty \ {}$ it becomes the standard normal distribution $\ {\mathcal {N} }(0,1)\,$ which has very "thin" tails. <!--SR:!2025-01-09,19,357!2025-02-25,53,357-->
  - Student's t-distribution / definition ::@:: If $Z \sim \mathcal N(0, 1)$, $Y \sim \chi^2(\nu)$, and $Z$ and $Y$ are _independent_, then $W = Z \sqrt{\nu / Y}$ means $W \sim t(\nu)$. <!--SR:!2025-02-28,56,357!2025-02-27,55,357-->
  - Student's t-distribution / probability density function (PDF) ::@:: (Probably no need to memorize this...) $$f(w) = \frac {\Gamma((n + 1) / 2)} {\sqrt{\pi n} \Gamma(n / 2)} \left(1 + \frac {w^2} n\right)^{-(n + 1) / 2}$$ <!--SR:!2025-02-05,37,337!2025-01-09,19,357-->
  - Student's t-distribution / brief history ::@:: William Sealy Gosset, known as "Student" <p> Student (1908). The probable error of a mean. _Biometrika_, 6(1), 1-25. <!--SR:!2025-02-06,38,337!2025-01-16,26,377-->
- [normal distribution](../../../../general/normal%20distribution.md)
  - normal distribution / sample mean ::@:: For _n_ samples of a population $X \sim \mathcal N\left(\mu_X, \sigma_X^2\right)$, we have $$\begin{aligned} \overline X & \sim \mathcal N\left(\mu_X, \sigma_X^2 / n\right) \\ (\overline X - \mu_X)\sqrt{n / \sigma_X^2} & \sim \mathcal N(0, 1) \,. \end{aligned}$$ <!--SR:!2025-01-15,25,377!2025-03-20,76,377-->
- [Cochran's theorem](../../../../general/Cochran's%20theorem.md)
  - Cochran's theorem / special case ::@:: For _n_ samples of a population $X \sim \mathcal N\left(\mu_X, \sigma_X^2\right)$ and its _corresponding_ normalized population $Z \sim \mathcal N(0, 1)$, $\overline X$ and $S_{X, n - 1}^2$ (or $S_{X, n}^2$) are _independent_. Further, we have $$\begin{aligned} \sum_{i = 1}^n (Z_i - \overline Z)^2 & \sim \chi^2(n - 1) \\ \sum_{i = 1}^n \left(\frac {X_i - \overline X} {\sigma_X} \right)^2 = \frac {(n - 1) S_{X, n - 1}^2 } {\sigma_X^2} & \sim \chi^2(n - 1) \,. \end{aligned}$$ (For the second line, $n S_{X, n}^2 = (n - 1) S_{X, n - 1}^2$ would also work.) <!--SR:!2025-01-14,24,377!2025-02-04,36,337-->
    - Cochran's theorem / special case / intuition ::@:: The squared deviations from the mean (SDM) of a sample of a normal population, given the _population mean_ is known, has _n_ degrees of freedom. But only the sample mean is known, which has 1 degree of freedom. So if we compute the SDM of a sample using the _sample mean_ instead of the _population mean_, it has $n - 1$ degrees of freedom.F <!--SR:!2025-01-15,25,377!2025-01-16,26,377-->
      - Cochran's theorem / special case / intuition / execution ::@:: For example: Consider $$U_{n - 1} := \frac {(n - 1) S_{X, n - 1}^2 } {\sigma_X^2} \sim \chi^2(n - 1) \,.$$ Wrapping it in $\sqrt{n - 1 / U_{n - 1} }$, we get: $$\sqrt{\sigma_X^2 / S_{X, n - 1}^2} \,,$$ which can be used to replace $\sigma_X^2$ in $(\overline X - \mu_X) \sqrt{n / \sigma_X^2} \sim \mathcal N(0, 1)$ to $(\overline X - \mu_X) \sqrt{n / S_{X, n - 1}^2} \sim t(n - 1)$. <p> Another example: Consider $$U_{n - 2} := \frac {(n - 2) s_{\varepsilon, n - 2}^2 } {\sigma_\varepsilon^2} \sim \chi^2(n - 2) \,.$$ Wrapping it in $\sqrt{n - 2 / U_{n - 2} }$, we get: $$\sqrt{\sigma_\varepsilon^2 / S_{\varepsilon, n - 2}^2 } \,,$$ which can be used to replace $\sigma_\varepsilon^2$ in $(\hat \beta_1 - \beta_1) \sqrt{S_{XX} / \sigma_\varepsilon^2} \sim \mathcal N(0, 1)$ to $(\hat \beta_1 - \beta_1) \sqrt{S_{XX} / S_{\varepsilon, n - 2}^2} \sim t(n - 2)$. <!--SR:!2025-02-26,54,357!2025-01-08,18,357-->
  - Cochran's theorem / corollary ::@:: For _n_ samples of a population $X \sim \mathcal N\left(\mu_X, \sigma_X^2\right)$ and its _corresponding_ normalized population $Z \sim \mathcal N(0, 1)$, we have $$\begin{aligned} \overline Z \sqrt {n / S_{Z, n - 1}^2} & \sim t(n - 1) \\ (\overline X - \mu_X) \sqrt{n / S_{X, n - 1}^2} & \sim t(n - 1) \,. \end{aligned}$$ (Notice how similar this is to $(\overline X - \mu_X) \sqrt{n / \sigma_X^2} \sim \mathcal N(0, 1)$...) <!--SR:!2025-02-05,37,337!2025-01-15,25,377-->

## week 8 tutorial

- datetime: 2024-10-25T09:30:00+08:00/2024-10-25T10:20:00+08:00

## week 9 lecture

- datetime: 2024-10-28T10:30:00+08:00/2024-10-28T11:50:00+08:00
- [confidence interval](../../../../general/confidence%20interval.md)
  - confidence interval / realization ::@:: Simply substitute the estimators with their corresponding estimates to find the confidence interval. <!--SR:!2025-01-09,19,357!2025-02-19,51,357-->
  - confidence interval / normal distribution ::@:: For normal distribution, we have 4 cases. We can estimate either $\mu$ or $\sigma^2$, either given we know the other parameter or we do not know the other parameter. <!--SR:!2025-01-14,24,377!2025-01-15,25,377-->
    - confidence interval / normal distribution / for mean with known variance ::@:: Assume $X \sim \mathcal N\left(\mu_X, \sigma_X^2\right)$. We use $$\begin{aligned} (\overline X - \mu_X) \sqrt{n / \sigma_X^2} & \sim \mathcal N(0, 1) \,. \end{aligned}$$ Then we have $$\begin{aligned} \Pr(-z_{\alpha / 2} \le (\overline X - \mu_X) \sqrt{n / \sigma_X^2} \le z_{\alpha / 2} ) & \ge 1 - \alpha \\ \Pr\left(\overline X - z_{\alpha / 2} \sqrt{\sigma_X^2 / n} \le \mu_X \le \overline X + z_{\alpha / 2} \sqrt{\sigma_X^2 / n} \right) & \ge 1 - \alpha \,, \end{aligned}$$ where $z_\alpha$ is $P(Z > z_\alpha) = \alpha \quad Z \sim \mathcal N(0, 1)$. <!--SR:!2025-02-25,53,357!2025-02-20,52,357-->
    - confidence interval / normal distribution / for mean with unknown variance ::@:: Assume $X \sim \mathcal N\left(\mu_X, \sigma_X^2\right)$. We use $$\begin{aligned} (\overline X - \mu_X) \sqrt{n / S_{X, n - 1}^2} & \sim \mathcal t(n - 1) \,. \end{aligned}$$ Then we have $$\begin{aligned} \Pr(-t_{n - 1, \alpha / 2} \le (\overline X - \mu_X) \sqrt{n / S_{X, n - 1}^2} \le t_{n - 1, \alpha / 2} ) & \ge 1 - \alpha \\ \Pr\left(\overline X - t_{n - 1, \alpha / 2} \sqrt{S_{X, n - 1}^2 / n} \le \mu_X \le \overline X + t_{n - 1, \alpha / 2} \sqrt{S_{X, n - 1}^2 / n} \right) & \ge 1 - \alpha \,, \end{aligned}$$ where $t_{n - 1, \alpha}$ is $P(T_{n - 1} > t_{n - 1, \alpha}) = \alpha \quad T \sim \mathcal t(n - 1)$. <p> Note that we have simply replaced $\sigma_X^2$ with $S_{X, n - 1}^2$ and $\mathcal N(0, 1)$ with $t(n - 1)$. <!--SR:!2025-02-06,38,337!2025-01-08,18,357-->
- [Student's t-distribution](../../../../general/Student's%20t-distribution.md)
  - Student's t-distribution / _R_ ::@:: To find $t_{\mathrm{df}, \alpha}$, use: `qt(<alpha>, df=<df>, lower.tail=F)`. <p> If you want to do t-test, use `t.test(<sample>, conf.level=<confidence level>)$conf.int`. <!--SR:!2025-01-16,26,377!2025-01-09,19,357-->
  - Student's t-distribution / table ::@:: To find $t_{\mathrm{df}, \alpha}$, look up $\nu = \mathrm{df}$ and $\alpha$ (be mindful of if the area is the lower or upper area), and find its corresponding value. <!--SR:!2025-01-15,25,377!2025-03-20,76,377-->

## week 9 lecture 2

- datetime: 2024-10-30T10:30:00+08:00/2024-10-30T11:50:00+08:00
- assignments: [assignment 3](assignments/assignent%203/index.md)
- [confidence interval](../../../../general/confidence%20interval.md)
  - confidence interval / normal distribution ::@:: We will only consider the confidence intervals when $X$ follows a normal distribution. <!--SR:!2025-01-16,26,377!2025-01-15,25,377-->
    - confidence interval / normal distribution / for variance with known mean ::@:: Assume $X \sim \mathcal N\left(\mu_X, \sigma_X^2\right)$. We use $$\begin{aligned} \sum_{i = 1}^n \left(\frac {X_i - \mu_X} {\sigma_X} \right)^2 & \sim \chi^2(n) \,. \end{aligned}$$ Then we have $$\begin{aligned} \Pr\left(\chi^2_{n, 1 - \alpha / 2} \le \sum_{i = 1}^n \left(\frac {X_i - \mu_X} {\sigma_X} \right)^2 \le \chi^2_{n, \alpha / 2} \right) & \ge 1 - \alpha \\ \Pr\left(\frac {\sum_{i = 1}^n (X_i - \mu_X)^2} {\chi^2_{n, \alpha / 2} } \le \sigma_X^2 \le \frac {\sum_{i = 1}^n (X_i - \mu_X)^2} {\chi^2_{n, 1 - \alpha / 2} } \right) & \ge 1 - \alpha \,, \end{aligned}$$ where $\chi^2_{n, \alpha}$ is $P\left(Y > \chi^2_{n, \alpha}\right) = \alpha \quad Y \sim \chi^2(n)$. (Remember, $\chi^2_{n, \alpha}$ is _not_ symmetric.) <!--SR:!2025-02-04,36,337!2025-02-19,51,357-->
    - confidence interval / normal distribution / for variance with unknown mean ::@:: Assume $X \sim \mathcal N\left(\mu_X, \sigma_X^2\right)$. We use $$\begin{aligned} \sum_{i = 1}^n \left(\frac {X_i - \overline X} {\sigma_X} \right)^2 & \sim \chi^2(n - 1) \,. \end{aligned}$$ Then we have $$\begin{aligned} \Pr\left(\chi^2_{n - 1, 1 - \alpha / 2} \le \sum_{i = 1}^n \left(\frac {X_i - \overline X} {\sigma_X} \right)^2 \le \chi^2_{n - 1, \alpha / 2} \right) & \ge 1 - \alpha \\ \Pr\left(\frac {\sum_{i = 1}^n (X_i - \overline X)^2} {\chi^2_{n - 1, \alpha / 2} } \le \sigma_X^2 \le \frac {\sum_{i = 1}^n (X_i - \overline X)^2} {\chi^2_{n - 1, 1 - \alpha / 2} } \right) & \ge 1 - \alpha \\  \Pr\left(\frac {(n - 1) S_{X, n - 1}^2} {\chi^2_{n - 1, \alpha / 2} } \le \sigma_X^2 \le \frac {(n - 1) S_{X, n - 1}^2} {\chi^2_{n - 1, 1 - \alpha / 2} } \right) & \ge 1 - \alpha \,, \end{aligned}$$ where $\chi^2_{n, \alpha}$ is $P\left(Y > \chi^2_{n, \alpha}\right) = \alpha \quad Y \sim \chi^2(n)$. (Remember, $\chi^2_{n, \alpha}$ is _not_ symmetric.) <p> Note that we have simply replaced $\mu_X$ with $\overline X$ and $\chi^2(n)$ with $\chi^2(n - 1)$. <!--SR:!2025-02-26,54,357!2025-02-25,53,357-->
- [chi-squared distribution](../../../../general/chi-squared%20distribution.md)
  - chi-squared distribution / _R_ ::@:: To find $\chi^2_{\mathrm{df}, \alpha}$, use: `qchisq(<alpha>, df=<df>, lower.tail=F)`. <p> If you want to do chi-squared-test, use `VarCI(<sample>, conf.level=<confidence level>)` from the package `DescTools` (install using `install.packages("DescTools")`). <!--SR:!2025-02-06,38,337!2025-01-09,19,357-->
  - chi-squared distribution / table ::@:: To find $\chi^2_{\mathrm{df}, \alpha}$, look up $\nu = \mathrm{df}$ and $\alpha$ (be mindful of if the area is the lower or upper area), and find its corresponding value. <!--SR:!2025-01-15,25,377!2025-01-16,26,377-->
- [central limit theorem](../../../../general/central%20limit%20theorem.md) (CLT) (optional) ::@:: (optional) It states that, under _appropriate conditions_, the distribution of a _normalized version of the sample mean_ converges to a _standard normal distribution_. This holds even if the original variables themselves are _not_ normally distributed. <!--SR:!2025-01-09,19,357!2025-01-09,19,357-->
  - central limit theorem / classical CLT (optional) ::@:: (optional) If $\overline {X_n}$ is the _sample mean_ of a random sample (sequence of _i.i.d._ random variables) of size $n$ taken from _any_ population with population mean $\mu_X$ and _finite_ variance $\sigma_X^2 < \infty$, then as $n \to \infty$, the random variable $\overline {X_n}$ _converges in distribution_ to $\mathcal N\left(\mu_X, \sigma_X^2 / n\right)$. The latter can be rewritten as $\overline {Z_n} = (\overline {X_n} - \mu_X) \sqrt{n / \sigma_X^2}$ _converges in distribution_ to $\mathcal N(0, 1)$. <!--SR:!2025-02-05,37,337!2025-02-27,55,357-->
  - central limit theorem / implications (optional) ::@:: (optional) Many real-life quantities are normal since they are often the balanced sum of many unobserved random events. This fact is frequently used in _statistical inference_. <!--SR:!2025-01-09,19,357!2025-01-08,18,357-->

## week 9 tutorial

- datetime: 2024-11-01T09:30:00+08:00/2024-11-01T10:20:00+08:00

## week 10 lecture

- datetime: 2024-11-04T10:30:00+08:00/2024-11-04T11:50:00+08:00
- [statistical hypothesis test](../../../../general/statistical%20hypothesis%20test.md) ::@:: It is a method of _statistical inference_ used to decide whether the data sufficiently supports a particular hypothesis. A statistical hypothesis test typically involves a _calculation of a test statistic_. Then a decision is made, either by comparing the test statistic to a _critical value_ or equivalently by _evaluating a p-value_ computed from the test statistic. <!--SR:!2025-01-15,25,377!2025-01-09,19,357-->
  - statistical hypothesis test / brief history (untaught) ::@:: (untaught) Historically, there were two approaches: Fisher's null hypothesis testing and Neyman–Pearson decision theory. <p> Nowadays, we are basically doing a hybrid of both. <!--SR:!2025-01-15,25,377!2025-01-15,25,377-->
    - statistical hypothesis test / brief history / Fisher's null hypothesis testing (untaught) ::@:: (untaught) It sets up a null hypothesis (but no alternative hypothesis), which need not be a nil (zero difference) hypothesis. <p> Then report the exact level of significance. But in any case, you are neither "accepting" nor "rejecting" the null hypothesis. If the result is not significant, make no decision and suspend judgement: you do not "accept" the null hypothesis. <p> As a result, there is no Type II (false negative) error, since if the result is not significant, you neither "accept" nor "reject". <!--SR:!2025-01-08,18,357!2025-01-15,25,377-->
    - statistical hypothesis test / brief history / Neyman–Pearson decision theory (untaught) ::@:: (untaught) It sets up two hypothesis, H1 and H2. Define a rejection region for each hypothesis. <p> If the data falls into the rejection region of H1, accept H2; otherwise accept H1. Accepting a hypothesis does not mean that you believe in it, but only that you act as if it were true. <p> As a result, there are Type I (false positive) error and Type II (false negative) error. <!--SR:!2025-01-09,19,357!2025-01-09,19,357-->
  - statistical hypothesis ::@:: It is an assertion or conjecture or statement about the population, usually formulated in terms of _population parameters_. <!--SR:!2025-01-15,25,377!2025-01-16,26,377-->
  - [null hypothesis](../../../../general/null%20hypothesis.md) ::@:: It is denoted $H_0$. It is the hypothesis that is assumed to be true and then tested to be rejected or not to be rejected formally. <p> It always contains a "=" sign (i.e. =, ≤, ≥). <!--SR:!2025-01-14,24,377!2025-01-15,25,377-->
  - [alternative hypothesis](../../../../general/alternative%20hypothesis.md) ::@:: It is denoted $H_1$. It is the hypothesis that contains the values of the parameter we would _accept_ if we _reject_ $H_0$. <o> It never contains a "=" sign, except in a _simple test_ (only two possible values for the parameter). <!--SR:!2025-01-15,25,377!2025-01-14,24,377-->
  - statistical hypothesis test / types ::@:: There are 4 types: simple test, one-sided left test (alternative is smaller), one-sided right test (alternative is larger), and two-sided test. <p> We do a two-sided test by default unless we have enough information (e.g. if a parameter being too high is acceptable, then we do a one-sided left test). <!--SR:!2025-01-16,26,377!2025-01-08,18,357-->
    - statistical hypothesis test / types / notation ::@:: simple test: $\begin{cases} H_0: \theta = \theta_0 \\ H_1: \theta = \theta_1 \end{cases}$ <br/> one-sided left test: $\begin{cases} H_0: \theta = \theta_0 \\ H_1: \theta < \theta_0 \end{cases}$ <br/> one-sided right test: $\begin{cases} H_0: \theta = \theta_0 \\ H_1: \theta > \theta_0 \end{cases}$ <br/> two-sided test: $\begin{cases} H_0: \theta = \theta_0 \\ H_1: \theta \ne \theta_0 \end{cases}$ <!--SR:!2025-01-15,25,377!2025-01-14,24,377-->
  - statistical hypothesis test / steps ::@:: Define $H_0$ and $H_1$. Assuming $H_0$ is true, define a _rare event_. Collect data. If the data contradicts $H_0$ (by having the _rare event_ happen), we reject $H_0$ and accept $H_1$. Otherwise, we "_do not reject_" (not "_accept_") $H_0$. <!--SR:!2025-01-09,19,357!2025-03-21,77,377-->
  - statistical hypothesis test / errors ::@:: There are two types of error: Type I error/false positive and Type II error/false negative. <p> Since "positive" means rejecting $H_0$, so Type I error/false positive is rejecting $H_0$ but $H_0$ is true, while Type II error/false negative is _not_ rejecting $H_0$ but $H_0$ is false. <!--SR:!2025-01-16,26,377!2025-01-09,19,357-->
    - statistical hypothesis test / errors / calculations ::@:: We can calculate the two errors' probabilities using conditional probability: $$\begin{aligned} \alpha = \Pr(\text{Type I error}) & = \Pr(\text{reject }H_0 \mid H_0\text{ is true}) \\ \beta = \Pr(\text{Type II error}) & = \Pr(\text{not reject }H_0 \mid H_0\text{ is false}) \end{aligned}$$ <!--SR:!2025-01-16,26,377!2025-01-16,26,377-->
    - statistical hypothesis test / errors / use ::@:: We want both Type I error $\alpha$ and Type II error $\beta$ to be as low as possible. But in general, we cannot decrease both simultaneously when the sample size is fixed. <p> We usually instead guarantee $\alpha$ does not exceed a desired low value, then find a test statement with the smallest $\beta$. <p> $\alpha$ is also known as the __level of significance__. $1 - \beta$ is also known as the __power__ of the test statement. <!--SR:!2025-01-15,25,377!2025-01-15,25,377-->
      - [statistical significance](../../../../general/statistical%20significance.md) ::@:: It is the probability of the study rejecting the null hypothesis, given that the null hypothesis is true. <p> Common misconception: It is very easy to swap the two events in the above conditional probability around, e.g. "A level of significance of 5% means, on average, 5 out of 100 times that we reject the null hypothesis, it is the wrong decision." <!--SR:!2025-02-20,52,357!2025-03-20,76,377-->
  - critical values ::@:: They, of a statistical test, are the boundaries of the acceptance region of the test. The acceptance region is the set of values of the test statistic for which the null hypothesis is not rejected (not "_accepted_", however, even if the region is called "acceptance region"). Depending on the shape of the acceptance region, there can be one or more than one critical value. <!--SR:!2025-01-08,18,357!2025-01-15,25,377-->
    - critical values / determination ::@:: If we fix the Type I error/false positive $\alpha$, we determine the critical values by determining the distribution of the test statistic (e.g. $\overline X$), and then make the rejection regions cover enough of the distribution so that its area equals $\alpha$, while minimizing $\beta$. <p> For a one-sided test or simple test, there is _usually_ only one critical value, and this _usually_ minimizes $\beta$ automatically. For a two-sided test, there are _usually_ only two critical values, chosen to have equal areas (i.e. $\alpha / 2$) on both sides, and this _usually_ minimizes $\beta$ automatically. <!--SR:!2025-02-25,53,357!2025-02-04,36,337-->
  - [_p_-value](../../../../general/p-value.md) ::@:: It is the probability of obtaining test results at least as extreme as the result actually observed, under the assumption that the null hypothesis is correct. <p> Common misconception: It is very easy to swap the two events in the above conditional probability around, e.g. "_p_-value is the possibility of making the wrong decision if you reject the null hypothesis." <!--SR:!2025-01-16,26,377!2025-01-16,26,377-->
    - _p_-value / use ::@:: $p$ is the ___p_-value__. $\alpha$ is the __significance level__. If $p \le \alpha$ (the slides use $p < \alpha$), then we have enough evidence to reject $H_0$ _at a significance level_ $\alpha$. Otherwise, if $p > \alpha$ (the slides _still_ use $p > \alpha$), then we do _not_ have enough evidence to reject $H_0$ _at a significance level_ $\alpha$ (but we are not _accepting_ it). <!--SR:!2025-01-09,19,357!2025-01-16,26,377-->

## week 10 lecture 2

- datetime: 2024-11-06T10:30:00+08:00/2024-11-06T11:50:00+08:00
- [statistical hypothesis test](../../../../general/statistical%20hypothesis%20test.md)
  - statistical hypothesis test / methods ::@:: two _equivalent_ methods: by critical value, by _p_-value <!--SR:!2025-01-16,26,377!2025-01-16,26,377-->
  - statistical hypothesis test / by critical value ::@:: Define $H_0$ and $H_1$. Fix the significance level $\alpha$. Choose a test statistic. Compute the critical value(s). Reject or not reject $H_0$. Use judgement based on if $H_0$ is rejected or not. <!--SR:!2025-03-21,77,377!2025-01-16,26,377-->
  - statistical hypothesis test / by _p_-value ::@:: Define $H_0$ and $H_1$. Choose a test statistic. Compute the _p_-value. Use judgement based on the _p_-value. <!--SR:!2025-01-15,25,377!2025-01-15,25,377-->
- [power](../../../../general/power%20(statistics).md) ::@:: It is a measure of the ability of an experimental design and hypothesis testing setup to detect a particular effect if it is truly present. <p> For hypothesis testing, this is the probability of rejecting $H_0$ given $H_0$ is false. Thus it is calculated as $1 - \beta$. <!--SR:!2025-03-20,76,377!2025-01-16,26,377-->
  - power / use ::@:: It is often used to assess the _goodness of a test statement_. Two test statements having the same significance level $\alpha$ can be compared using this. <p> To increase the power $1 - \beta$, we can increase $\alpha$, or we can increase the sample size if we do not want to change $\alpha$. <!--SR:!2025-01-09,19,357!2025-01-16,26,377-->

## week 10 tutorial

- datetime: 2024-11-08T09:30:00+08:00/2024-11-08T10:20:00+08:00

## week 11 lecture

- datetime: 2024-11-11T10:30:00+08:00/2024-11-11T11:50:00+08:00
- [statistical hypothesis test](../../../../general/statistical%20hypothesis%20test.md)
  - statistical hypothesis test / normal distribution ::@:: We will only consider the test statements when $X$ follows a normal distribution. <!--SR:!2025-01-16,26,377!2025-01-15,25,377-->
    - statistical hypothesis test / normal distribution / for mean when variance is known ::@:: Assume $X \sim \mathcal N\left(\mu_0, \sigma_X^2\right)$. We use $$Z := (\overline X - \mu_0) \sqrt{n / \sigma_X^2} \sim \mathcal N(0, 1) \,.$$ Then we have $$\begin{aligned} p_l & = \Pr\left(Z < (c - \mu_0) \sqrt{n / \sigma_X^2}\right) && \text{one-sided left} \\ p_r & = \Pr\left(Z > (c - \mu_0) \sqrt{n / \sigma_X^2}\right) && \text{one-sided right} \\ p_{lr} & = \Pr\left(\lvert Z \rvert > \left\lvert (c - \mu_0) \sqrt{n / \sigma_X^2} \right\rvert \right) = 2 \min\set{p_l, p_r} && \text{two-sided (by symmetry)} \,. \end{aligned}$$ <p> If using critical value, $c$ is the critical value for $\overline x$ and $p := \alpha$. If using _p_-value, $c := \overline x$ and $p$ is the _p_-value. Note that for two-sided test, when using critical value, the critical value approach uses $\left\lvert (\overline x - \mu_0) \sqrt{n / \sigma_X^2} \right\rvert > c := z_{\alpha / 2}$, instead of comparing $\overline x$ against the $c$ as first defined. <!--SR:!2025-02-04,36,337!2025-02-21,53,357-->
    - statistical hypothesis test / normal distribution / for mean when variance is unknown ::@:: Assume $X \sim \mathcal N\left(\mu_0, \sigma_X^2\right)$. We use $$T_{n - 1} := (\overline X - \mu_0) \sqrt{n / S_{X, n - 1}^2} \sim t(n - 1) \,.$$ Then we have $$\begin{aligned} p_l & = \Pr\left(T_{n - 1} < (c - \mu_0) \sqrt{n / s_{X, n - 1}^2}\right) && \text{one-sided left} \\ p_r & = \Pr\left(T_{n - 1} > (c - \mu_0) \sqrt{n / s_{X, n - 1}^2}\right) && \text{one-sided right} \\ p_{lr} & = \Pr\left(\lvert T_{n - 1} \rvert > \left\lvert (c - \mu_0) \sqrt{n / s_{X, n - 1}^2} \right\rvert \right) = 2 \min\set{p_l, p_r} && \text{two-sided (by symmetry)} \,. \end{aligned}$$ <p> If using critical value, $c$ is the critical value for $\overline x$ and $p := \alpha$. If using _p_-value, $c := \overline x$ and $p$ is the _p_-value. Note that for two-sided test, when using critical value, the critical value approach uses $\left\lvert (\overline x - \mu_0) \sqrt{n / s_{X, n - 1}^2} \right\rvert > c := t_{n - 1, \alpha / 2}$, instead of comparing $\overline x$ against the $c$ as first defined. <p> Note that we have simply replaced $Z$ with $T_{n - 1}$ and $\sigma_X^2$ with $S_{X, n - 1}^2$. <!--SR:!2025-02-04,36,337!2025-02-04,36,337-->
  - statistical hypothesis test / t-test
    - statistical hypothesis test / t-test / _R_ ::@:: We can use `t.test(<data>, alternative="less"/"greater"/"two.sided", mu=<H0 mean>)`. Also note this methods can also give the 95% confidence interval for the population mean as well. (But it does not have any direct relationship to hypothesis testing.) <!--SR:!2025-01-08,18,357!2025-02-05,37,337-->

## week 11 lecture 2

- datetime: 2024-11-13T10:30:00+08:00/2024-11-13T11:50:00+08:00
- assignments: [assignment 4](assignments/assignent%204/index.md)
- [statistical hypothesis test](../../../../general/statistical%20hypothesis%20test.md)
  - statistical hypothesis test / normal distribution
    - statistical hypothesis test / normal distribution / for variance when mean is known ::@:: Assume $X \sim \mathcal N\left(\mu_X, \sigma_0^2\right)$. We use $$U_n := \sum_{i = 1}^n \left(\frac {X_i - \mu_X} {\sigma_0} \right)^2 \sim \mathcal \chi^2(n) \,.$$ Then we have $$\begin{aligned} p_l & = \Pr\left(U_n < \frac {\sum_{i = 1}^n (x_i - \mu_X)^2} {\sigma_0^2} \right) && \text{one-sided left} \\ p_r & = \Pr\left(U_n > \frac {\sum_{i = 1}^n (x_i - \mu_X)^2} {\sigma_0^2} \right) && \text{one-sided right} \\ p_{lr} & = 2 \min \set{p_l, p_r} && \text{one-sided two-sided} \,. \end{aligned}$$ <p> If using critical value, compare $\frac {\sum_{i = 1}^n (x_i - \mu_X)^2} {\sigma_0^2}$ against $\chi^2_{n, \alpha}$, $\chi^2_{n, 1 - \alpha}$, $\chi^2_{n, \alpha / 2}$, or $\chi^2_{n, 1 - \alpha / 2}$ (note: not symmetric); and $p := \alpha$. If using _p_-value, $p$ is the _p_-value. Note that when using _p_-value, $p_l + p_r = 1$. <!--SR:!2025-01-08,18,357!2025-02-05,37,337-->
    - statistical hypothesis test / normal distribution / for variance when mean is unknown ::@:: Assume $X \sim \mathcal N\left(\mu_X, \sigma_0^2\right)$. We use $$U_{n - 1} := \sum_{i = 1}^n \left(\frac {X_i - \overline X} {\sigma_0} \right)^2 \sim \mathcal \chi^2(n - 1) \,.$$ Then we have $$\begin{aligned} p_l & = \Pr\left(U_{n - 1} < \frac {(n - 1) s_{X, n - 1}^2 } {\sigma_0^2} \right) && \text{one-sided left} \\ p_r & = \Pr\left(U_{n - 1} > \frac {(n - 1) s_{X, n - 1}^2 } {\sigma_0^2} \right) && \text{one-sided right} \\ p_{lr} & = 2 \min\set{p_l, p_r} && \text{one-sided two-sided} \,. \end{aligned}$$ <p> If using critical value, compare $\frac {(n - 1) s_{X, n - 1}^2} {\sigma_0^2}$ against $\chi^2_{n - 1, \alpha}$, $\chi^2_{n - 1, 1 - \alpha}$, $\chi^2_{n - 1, \alpha / 2}$, or $\chi^2_{n - 1, 1 - \alpha / 2}$ (note: not symmetric); and $p := \alpha$. If using _p_-value, $p$ is the _p_-value. Note that when using _p_-value, $p_l + p_r = 1$. <p> Note that we have simply replaced $U_n$ with $U_{n - 1}$ and $\mu_X$ with $\overline X$. <!--SR:!2025-02-04,36,337!2025-02-05,37,337-->

## week 11 tutorial

- datetime: 2024-11-15T09:30:00+08:00/2024-11-15T10:20:00+08:00

## week 12 lecture

- datetime: 2024-11-18T10:30:00+08:00/2024-11-18T11:50:00+08:00
- [regression analysis](../../../../general/regression%20analysis.md) ::@:: It is a very useful statistical model used to capture _relationship_ between related variables of our interest. <!--SR:!2025-01-14,24,377!2025-01-14,24,377-->
- [linear regression](../../../../general/linear%20regression.md) ::@:: ... if the relationship is _linear_. <!--SR:!2025-01-14,24,377!2025-01-14,24,377-->
- [simple linear regression](../../../../general/simple%20linear%20regression.md) ::@:: ... if there is only one variable called _explanatory variable_, labeled by _x_, used to explain our target variable _y_. <!--SR:!2025-01-15,25,377!2025-01-15,25,377-->
  - simple linear regression / note ::@:: It is nowhere close to "simple" mathematically... <!--SR:!2025-01-15,25,377!2025-01-15,25,377-->
- [regression analysis](../../../../general/regression%20analysis.md)
  - regression analysis / brief history ::@:: Around the turn of the 20th century, geneticist Francis Galton discovered "regression toward the mean". Later, Sir Francis Galton referred to this as "regression toward mediocrity". <!--SR:!2025-02-27,55,357!2025-01-14,24,377-->
- [scatter plot](../../../../general/scatter%20plot.md) ::@:: It is a type of plot or mathematical diagram using Cartesian coordinates to display values for typically two variables for a set of data. <!--SR:!2025-02-18,50,357!2025-01-14,24,377-->
  - scatter plot / simple linear regression ::@:: In elementary mathematics, $y = mx + c$ is a perfect line on a graph. In statistics, things are never too clean. Data do not perfectly fit onto a line on a scatter plot. <!--SR:!2025-01-14,24,377!2025-03-21,77,377-->
  - scatter plot / _R_ ::@:: `plot(<x>, <y>, main=<title>, ylab=<y label>, xlab=<x label>)` <!--SR:!2025-01-15,25,377!2025-01-16,26,377-->
- [simple linear regression](../../../../general/simple%20linear%20regression.md)
  - simple linear regression / model ::@:: The model function is $$y = \beta_0 + \beta_1 x \,.$$ The actual data has __residual__ $e_i$ and may be modeled as using $$y_i = \beta_0 + \beta_1 x_i + \varepsilon_i \,.$$ <!--SR:!2025-01-16,26,377!2025-01-16,26,377-->
  - simple linear regression / fit ::@:: Ordinary least square (OLS) is used to find the best fit line. That is, we _minimize_ $$\sum_{i = 1}^n \varepsilon_i^2 = \sum_{i = 1}^n (y_i - \beta_0 - \beta_1 x_i)^2 \,.$$ <!--SR:!2025-01-16,26,377!2025-01-16,26,377-->
    - simple linear regression / fit / minimization (untaught) ::@:: (untaught) Minimize the above by expanding to get a quadratic expression: $$\begin{aligned} & \phantom = \sum_{i = 1}^n (y_i - \beta_0 - \beta_1 x_i)^2 \\ & = \sum_{i= 1}^n \left(y_i^2 - 2 \beta_0 y_i - 2\beta_1 x_i y_i + \beta_0^2 + 2\beta_0 \beta_1 x_i + \beta_1^2 x_i^2\right) \\ & \propto \overline {y^2} - 2 \beta_0 \overline y - 2\beta_1 \overline{xy} + \beta_0^2 + 2 \beta_0 \beta_1 \overline x + \beta_1^2 \overline {x^2} \,. \end{aligned}$$ Fix $\beta_1$ and find $\beta_0$ that minimizes: $$\begin{aligned} & \phantom = -2\beta_0 \overline y + \beta_0^2 + 2 \beta_0 \beta_1 \overline x + C \\ & = \beta_0^2 + (2 \beta_1 \overline x - 2 \overline y) \beta_0 + C \\ & = (\beta_0 + \beta_1 \overline x - \overline y)^2 + C \end{aligned}$$ So $\beta_0 = \overline y - \beta_1 \overline x$ minimizes. Now find $\beta_1$ that minimizes: $$\begin{aligned} & \phantom = - 2 \beta_0 \overline y - 2\beta_1 \overline{xy} + \beta_0^2 + 2 \beta_0 \beta_1 \overline x + \beta_1^2 \overline {x^2} + C \\ & = -2 \overline y^2 + 2 \beta_1 \overline x \cdot \overline y - 2 \beta_1 \overline {xy} + \overline y^2 - 2 \beta_1 \overline x \cdot \overline y + \beta_1^2 \overline x^2 + 2 \beta_1 \overline x \cdot \overline y - 2 \beta_1^2 \overline x^2 + \beta_1^2 \overline {x^2} + C \\ & = - 2 \beta_1 \overline {xy} - \beta_1^2 \overline x^2 + 2 \beta_1 \overline x \cdot \overline y + \beta_1^2 \overline {x^2} + C \\ & = \left(\overline {x^2} - \overline x^2\right) \beta_1^2 + 2(\overline x \cdot \overline y - \overline{xy}) \beta_1 + C \\ & = \overline {(x - \overline x)^2} \beta_1^2 - 2 \overline {(x - \overline x)(y - \overline y)} \beta_1 + C \\ & \phantom = \text{note the similarity to: }S_{XY} = \operatorname{Cov}(X, Y) = \operatorname E[XY] -  \operatorname E[X] \operatorname E[Y] \end{aligned}$$ So $\beta_1 = \frac {\overline {(x - \overline x) (y - \overline y)} } {\overline {(x - \overline x)^2} } = \frac {\sum_{i = 1}^n (x_i - \overline x) (y_i - \overline y)} {\sum_{i = 1}^n (x_i - \overline x)^2}$ minimizes, using the fact that $-b / 2a$ is the argument minimum of a quadratic equation. <!--SR:!2025-02-04,36,337!2025-03-21,77,377-->
  - simple linear regression / solution ::@:: $$\begin{aligned} b & = \frac {\operatorname{Cov}(X, Y)} {\operatorname{Cov}(X, X)} \\ & = \frac {\operatorname E[XY] - \operatorname E[X] \operatorname E[Y]} {\operatorname E\left[X^2\right] - (\operatorname E[X])^2} \\ & = \frac {S_{XY} } {S_{XX} } = \frac {\sum_{i = 1}^n (x_i - \overline x) (y_i - \overline y)} {\sum_{i = 1}^n (x_i - \overline x)^2} \\ & = \frac {\sum_{i = 1}^n x_i y_i - (\sum_{i = 1}^n x_i) (\sum_{i = 1}^n y_i) / n} {\sum_{i = 1}^n x_i^2 - (\sum_{i = 1}^n x_i)^2 / n} \\ a & = \overline y - b \overline x \end{aligned}$$ <!--SR:!2025-01-08,18,357!2025-02-28,56,357-->
- [residual sum of squares](../../../../general/residual%20sum%20of%20squares.md) (RSS (avoid using in this course), SSE (use in this course)) ::@:: It the sum of the _squares_ of _residuals_ (deviations predicted from actual empirical values of data). <p> This can be used to quantify the _goodness of the simple linear regression models_. Suppose we have two simple linear regression models, one using the explanatory variable _x_, the other using the explanatory variable _w_. The model with less RSS is better. <p> Note: RSS is also a short form for _regression sum of squares_. So use _SSE_ instead. <!--SR:!2025-01-16,26,377!2025-01-15,25,377-->
- [simple linear regression](../../../../general/simple%20linear%20regression.md)
  - simple linear regression / interpretation ::@:: $\beta_1$ can be interpreted as the average increase of $y$ per $x$. Also, the regression line passes through the _center of mass_ point $(\overline x, \overline y)$. <!--SR:!2025-01-14,24,377!2025-01-09,19,357-->
  - simple linear regression / _R_ ::@:: `lm(<y>~<x>)`, `abline(a=<b0>, b=<b1>)`, `abline(lm(<y>~<x>))` <!--SR:!2025-01-08,18,357!2025-01-15,25,377-->

## week 12 lecture 2

- datetime: 2024-11-20T10:30:00+08:00/2024-11-20T11:50:00+08:00
- [Pearson correlation coefficient](../../../../general/Pearson%20correlation%20coefficient.md) ::@:: It is a _correlation coefficient_ that measures linear correlation between two sets of data. <p> It is the ratio between the covariance of two variables and the product of their standard deviations; thus, it is essentially a normalized measurement of the covariance, such that the result always has a value between −1 and 1. <!--SR:!2025-01-15,25,377!2025-02-27,55,357-->
  - Pearson correlation coefficient / sample ::@:: $$r_{xy} = \frac {S_{XY} } {\sqrt{S_{XX} S_{YY} } } =\frac{\sum ^n _{i=1}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum ^n _{i=1}(x_i - \bar{x})^2} \sqrt{\sum ^n _{i=1}(y_i - \bar{y})^2} } = \frac {\sum x_i y_i - (\sum x_i) (\sum y_i) / n} {\sqrt{\sum x_i^2 - (\sum x_i)^2 / n} {\sqrt{\sum y_i^2 - (\sum y_i)^2 / n} } }$$ It is undefined when the denominator is 0. (It looks like the dot product of two vectors divided by the two Euclidean lengths of both vectors...) <!--SR:!2025-02-05,37,337!2025-01-09,19,357-->
    - Pearson correlation coefficient / sample / _R_ ::@:: `cor.test(<x>, <y>, method="pearson")$estimate` <!--SR:!2025-01-15,25,377!2025-01-09,19,357-->
  - Pearson correlation coefficient / population ::@:: $$\rho_{X,Y}= \frac{\operatorname{cov}(X,Y)}{\sigma_X \sigma_Y} = \frac {\operatorname E[(X - \mu_X) (Y - \mu_Y)] } {\sigma_X \sigma_Y}$$ It is undefined when the denominator is 0. <p> $r_{xy}$ is an estimator for $\rho_{X, Y}$. <!--SR:!2025-01-09,19,357!2025-01-16,26,377-->
  - Pearson correlation coefficient / interpretation ::@:: If positive, then they are _positively linearly correlated_. If negative, then they are _negatively linearly correlated_. Otherwise, it means they have no linear relationship (_linearly uncorrelated_), but it does not take _nonlinear relationships_ into account. <p> The coefficient takes neither _nonlinear relationships_ nor _slope_ into account. It only indicates the _strength_ and _direction_ of a _linear_ relationship. <p> If the points have no variance in one direction, then the points lie on a horizontal or vertical line. But the Pearson correlation coefficient is _undefined_. <!--SR:!2025-01-09,19,357!2025-01-08,18,357-->
- [Fisher transformation](../../../../general/Fisher%20transformation.md) (optional) ::@:: (optional) $$z={1 \over 2}\ln \left({1+r \over 1-r}\right)=\operatorname {artanh} (r) \,,$$ where $r$ is the sample Pearson correlation coefficient. <!--SR:!2025-01-08,18,357!2025-01-14,24,377-->
  - Fisher transformation / brief history ::@:: R.A. Fisher in 1915 proposed this to a _transformed estimator_ and its _approximated normal distribution_, and then make a _back-transformation_ to produce the confidence interval for $\rho$. <!--SR:!2025-01-14,24,377!2025-01-16,26,377-->
  - Fisher transformation / properties ::@:: If the two random variables being considered is a bivariate normal distribution and the sample pairs are i.i.d., then $z = \frac 1 2 \ln \left(\frac {1 + r} {1 - r}\right)$ is _approximately_ $$\begin{aligned} Z & \sim \mathcal N\left(\frac 1 2 \ln \left(\frac {1 + \rho} {1 - \rho} \right), \frac 1 {N - 3 }\right) \\ \left(Z - \frac 1 2 \ln \left(\frac {1 + \rho} {1 - \rho}\right) \right) \sqrt{N - 3} & \sim \mathcal N(0, 1) \end{aligned} \,$$ where $N$ is the number of samples. (Note, $\frac 1 {N - 3}$ is the _variance_, while $\frac 1 {\sqrt{N - 3} }$ is the _standard deviation_.) <!--SR:!2025-02-21,53,357!2025-02-19,51,357-->
  - Fisher transformation / use ::@:: We can use this to produce a confidence interval for $\rho$. <!--SR:!2025-01-15,25,377!2025-01-16,26,377-->
  - Fisher transformation / back-transformation ::@:: $$r = \frac {\exp(2z) - 1} {\exp(2z) + 1} = \tanh(z)$$ <!--SR:!2025-03-20,76,377!2025-01-09,19,357-->
  - Fisher transformation / _R_ ::@:: If you want to find the confidence interval for population Pearson correlation coefficient, use `CorCI(<sample coefficient>, <sample count>, conf.level=<confidence level>)` from the package `DescTools` (install using `install.packages("DescTools")`). <!--SR:!2025-01-15,25,377!2025-01-08,18,357-->
- [total sum of squares](../../../../general/total%20sum%20of%20squares.md) (TSS, SST (use in this course)) ::@:: For a set of observations, $y_{i},i\leq n$, it is defined as the sum over all squared differences between the observations and their overall [mean](mean.md) ${\bar {y} }$: $$\sum _{i=1}^{n}\left(y_{i}-{\bar {y} }\right)^{2} \,.$$ <!--SR:!2025-01-15,25,377!2025-01-16,26,377-->
  - total sum of squares / linear regression ::@:: For wide classes of linear models, the total sum of squares equals the _explained sum of squares_ plus the _residual sum of squares_. <!--SR:!2025-01-16,26,377!2025-01-08,18,357-->
- [residual sum of squares](../../../../general/residual%20sum%20of%20squares.md) (RSS (avoid using in this course), SSE (use in this course))
- [explained sum of squares](../../../../general/explained%20sum%20of%20squares.md) (ESS, RSS (use in this course)) ::@:: It is a quantity used in describing how well a model, often a regression model, represents the data being modelled. <br/> It is calculated as: $$\sum _{i=1}^{n}\left({\hat {y} }_{i}-{\bar {y} }\right)^{2} \,,$$ where ${\hat {y} }_{i}$ is the value estimated by the regression line. <!--SR:!2025-03-21,77,377!2025-01-15,25,377-->
- [coefficient of determination](../../../../general/coefficient%20of%20determination.md) ::@:: It, denoted _R_<sup>2</sup> or _r_<sup>2</sup> and pronounced "R squared", is the proportion (thus between 0 and 1) of the variation in the dependent variable that is predictable from the independent variable(s). <p> It is calculated as: $$\frac {\text{RSS} } {\text{SST} } = 1 - \frac {\text{SSE} } {\text{SST} } \,.$$ <!--SR:!2025-01-14,24,377!2025-01-16,26,377-->
  - coefficient of determination / _R_ ::@:: `summary(<model>)`, where `<model>` can be obtained by `lm(<y>~<x>[, data=<dataframe>])`. "Multiple R-squared" gives the result. <!--SR:!2025-01-15,25,377!2025-01-08,18,357-->
  - coefficient of determination / Pearson correlation coefficient ::@:: In a [linear least squares regression with _a single explanator_](../../../../general/simple%20linear%20regression.md) \(with _fitted intercept and slope_\), this is also equal to $\rho ^{2}(y,x)$ the squared Pearson correlation coefficient between the dependent variable $y$ and explanatory variable $x$. <!--SR:!2025-01-09,19,357!2025-01-15,25,377-->

## week 12 tutorial

- datetime: 2024-11-22T09:30:00+08:00/2024-11-22T10:20:00+08:00

## week 13 lecture

- datetime: 2024-11-25T10:30:00+08:00/2024-11-25T11:50:00+08:00
- [simple linear regression](../../../../general/simple%20linear%20regression.md)
  - simple linear regression / model assumptions ::@:: We assume the errors are: $$\varepsilon_i \sim \mathcal N\left(0, \sigma_\varepsilon^2\right) \quad i = 1, \ldots, n \quad (\text{i.i.d.}) \,.$$ __We assume this is the case henceforth.__ <!--SR:!2025-01-16,26,377!2025-01-15,25,377-->
  - simple linear regression / slope estimator
    - simple linear regression / slope estimator / known error variance ::@:: $$\begin{aligned} \hat \beta_1 & \sim \mathcal N\left(\beta_1, \sigma_\varepsilon^2 / S_{XX}\right) \\ (\hat \beta_1 - \beta_1) \sqrt{S_{XX} / \sigma_\varepsilon^2} & \sim \mathcal N(0, 1) \end{aligned}$$ <!--SR:!2025-02-27,55,357!2025-02-28,56,357-->
      - simple linear regression / slope estimator / known error variance / proof ::@:: $$\begin{aligned} \operatorname E[\hat \beta_1] & = \operatorname E\left[\frac {\sum_{i = 1}^n (x_i - \overline x) (Y_i - \overline Y)} {\sum_{i = 1}^n (x_i - \overline x)^2}\right] \\ & = \operatorname E\left[\frac {\sum_{i = 1}^n (x_i - \overline x) Y_i} {\sum_{i = 1}^n (x_i - \overline x)^2}\right] \\ & = \frac {\sum_{i = 1}^n (x_i - \overline x) \operatorname E[Y_i]} {\sum_{i = 1}^n (x_i - \overline x)^2} \\ & = \frac {\sum_{i = 1}^n (x_i - \overline x) (\beta_0 + \beta_1 x_i)} {\sum_{i = 1}^n (x_i - \overline x)^2} \\ & = \beta_1 \frac {\sum_{i = 1}^n (x_i - \overline x)^2} {\sum_{i = 1}^n (x_i - \overline x)^2} \\ & = \beta_1 \\ \operatorname{Var}(\hat \beta_1) & = \operatorname{Var}\left(\frac {\sum_{i = 1}^n (x_i - \overline x) (Y_i - \overline Y)} {\sum_{i = 1}^n (x_i - \overline x)^2} \right) \\ & = \operatorname{Var}\left(\frac {\sum_{i = 1}^n (x_i - \overline x) Y_i} {\sum_{i = 1}^n (x_i - \overline x)^2} \right) \\ & = \frac {\sum_{i = 1}^n (x_i - \overline x)^2 \operatorname {Var}(Y_i)} {\left(\sum_{i = 1}^n (x_i - \overline x)^2\right)^2} \\ & = \frac {\sum_{i = 1}^n (x_i - \overline x)^2 \operatorname {Var}(\beta_1 x_i + \varepsilon_i)} {\left(\sum_{i = 1}^n (x_i - \overline x)^2\right)^2} \\ & = \frac {\sigma_\varepsilon^2} {\sum_{i = 1}^n (x_i - \overline x)^2} \\ & = \sigma_\varepsilon^2 / S_{XX} \end{aligned}$$ <!--SR:!2025-03-20,76,377!2025-02-21,53,357-->
  - simple linear estimator / intercept estimator
    - simple linear estimator / intercept estimator / known error variance ::@:: $$\begin{aligned} \hat \beta_0 & \sim \mathcal N\left(\beta_0, \overline {x^2} \sigma_\varepsilon^2 / S_{XX}\right) \\ (\hat \beta_0 - \beta_0) \sqrt{S_{XX} / \overline {x^2} \sigma_\varepsilon^2} & \sim \mathcal N(0, 1) \end{aligned}$$ <!--SR:!2025-02-06,38,337!2025-02-18,50,357-->
      - simple linear estimator / intercept estimator / known error variance / proof ::@:: $$\begin{aligned} \operatorname E[\hat \beta_0] & = \operatorname E[\overline Y - \hat \beta_1 \overline x] \\ & = \operatorname E[\overline {\beta_0 + \beta_1 x + \varepsilon} - \hat \beta_1 \overline x] \\ & = \beta_0 + \beta_1 \overline x + 0 - \beta_1 \overline x \\ & = \beta_0 \\ \operatorname {Var}(\hat \beta_0) & = \operatorname{Var}(\overline Y - \hat \beta_1 \overline x) \\ & = \operatorname{Var}(\overline{\beta_0 + \beta_1 x + \varepsilon} - \hat \beta_1 \overline x) \\ & = 0 + 0 + \frac {\sigma_\varepsilon^2} {n} + \frac {\overline x^2 \sigma_\varepsilon^2} {S_{XX} } \\ & = \frac {\sigma_\varepsilon^2 \left(\overline {(x_i - \overline x)^2} + \overline x^2 \right)} {S_{XX} } \\ & = \frac {\overline {x^2} \sigma_\varepsilon^2} {S_{XX} } \end{aligned}$$ <!--SR:!2025-02-28,56,357!2025-02-28,56,357-->
  - simple linear regression / error variance estimator ::@:: The estimator (the slides use $S^2$) is $$S_{\varepsilon, n - 2}^2 := \frac {\sum_{i = 1}^n (Y_i - \hat Y_i)^2} {n - 2} \,. $$ Its actual value (the slides use $s^2$) can be calculated by: $$s_{\varepsilon, n - 2}^2 = \frac {\sum_{i = 1}^n (y_i - \hat y_i)^2} {n - 2} = \frac {S_{YY} - b S_{XY} } {n - 2} = \frac {\mathrm{SSE} } {n - 2} \,.$$ <!--SR:!2025-01-12,9,337!2025-01-05,6,317-->
    - simple linear regression / error variance estimator / properties ::@:: The following holds: $$\frac {(n - 2)s_{\varepsilon, n - 2}^2} {\sigma_{\varepsilon}^2} \sim \chi^2(n - 2) \,.$$ <p> It is an unbiased estimator of $\sigma_\varepsilon^2$. <!--SR:!2025-02-26,54,357!2025-03-20,76,377-->
- [mean squared error](../../../../general/mean%20squared%20error.md) ::@:: It, of an estimator (of a procedure for estimating an unobserved quantity) measures the _average of the squares of the errors_—that is, the average squared difference between the estimated values and the actual value. <!--SR:!2025-03-21,77,377!2025-01-09,19,357-->

## week 13 lecture 2

- datetime: 2024-11-27T10:30:00+08:00/2024-11-27T11:50:00+08:00
- [simple linear regression](../../../../general/simple%20linear%20regression.md)
  - simple linear regression / slope estimator
    - simple linear regression / slope estimator / unknown error variance ::@:: $$(\hat \beta_1 - \beta_1) \sqrt{S_{XX} / S_{\varepsilon, n - 2}^2} \sim \mathcal t(n - 2)$$ <!--SR:!2025-03-20,76,377!2025-03-21,77,377-->
      - simple linear regression / slope estimator / unknown error variance / confidence interval ::@:: $$b \pm t_{n - 2, \alpha / 2} \sqrt{S_{\varepsilon, n - 2}^2 / S_{XX} }$$ <!--SR:!2025-02-28,56,357!2025-02-06,38,337-->
      - simple linear regression / slope estimator / unknown error variance / hypothesis testing ::@:: Compare using $$(b - b_1) \sqrt{S_{XX} / s_{\varepsilon, n - 2}^2}$$ against $t(n - 2)$. Use the absolute value of it if two-sided test. <!--SR:!2025-02-26,54,357!2025-02-04,36,337-->
  - simple linear estimator / intercept estimator
    - simple linear estimator / intercept estimator / unknown error variance ::@:: $$(\hat \beta_0 - \beta_0) \sqrt{S_{XX} / \overline {x^2} S_{\varepsilon, n - 2}^2} \sim \mathcal t(n - 2)$$ <!--SR:!2025-02-06,38,337!2025-01-08,18,357-->
      - simple linear regression / intercept estimator / unknown error variance / confidence interval ::@:: $$a \pm t_{n - 2, \alpha / 2} \sqrt{\overline {x^2} S_{\varepsilon, n - 2}^2 / S_{XX} }$$ <!--SR:!2025-02-05,37,337!2025-02-26,54,357-->
      - simple linear regression / intercept estimator / unknown error variance / hypothesis testing ::@:: Compare using $$(a - b_0) \sqrt{S_{XX} / \overline {x^2} s_{\varepsilon, n - 2}^2}$$ against $t(n - 2)$. Use the absolute value of it if two-sided test. <!--SR:!2025-01-16,26,377!2025-01-16,26,377-->
  - simple linear estimator / _R_: confidence level of estimators ::@:: If unknown error variance, then use `confint(lm(<y>~<x>), level=<confidence level>))`. <!--SR:!2025-01-14,24,377!2025-02-27,55,357-->
  - simple linear estimator / _R_: hypothesis testing of estimators ::@:: `summary(<model>)`, where `<model>` can be obtained by `lm(<y>~<x>[, data=<dataframe>])`. But note that the null hypothesis are respectively $\beta_0 = 0$ and $\beta_1 = 0$. <!--SR:!2025-01-14,24,377!2025-01-08,18,357-->
  - simple linear estimator / prediction ::@:: $$\hat y_{\mathrm{new} } = a + b x_{\mathrm{new} } \,,$$ which is a _point estimate_ of $y_{\mathrm{new} }$. <!--SR:!2025-01-14,24,377!2025-01-14,24,377-->
    - simple linear estimator / prediction / interval ::@:: $$y_{\mathrm{new} } \pm t_{n - 2, \alpha / 2} \sqrt{s_{\varepsilon, n - 2}^2 \left(1 + \frac 1 n + \frac {(x_{\mathrm{new} } - \overline x)^2} {S_{XX} } \right)}$$ <!--SR:!2025-01-08,9,297!2025-01-09,19,357-->
  - simple linear estimator / _R_: prediction ::@:: For a point estimate, use `predict(<model>, data.frame(x=<new x>))`. For an interval estimate, use `predict(<model>, data.frame(x=<new x>), interval="prediction", level=<confidence level>)`. <!--SR:!2025-01-08,18,357!2025-01-08,18,357-->

## week 13 tutorial

- datetime: 2024-11-29T09:30:00+08:00/2024-11-29T10:20:00+08:00

## final examination

- datetime: 2024-12-14T08:30:00+08:00/2024-12-14T11:00:00+08:00, PT2H30M
- venue: S H Ho Sports Hall
- format: closed book, calculator, 2 sides of a A4-sized cheatsheet
  - [cheatsheet](MATH%202411%20final%20examination%20cheatsheet.pdf)
- grades: 100/100 → 100/100
  - statistics: L1
    - mean: 56.6 → 56.9
    - standard deviation: ? → ?
    - low: 2 → 2
    - lower quartile: 36 → 36.5
    - median: 62 → 62
    - upper quartile: 75 → 78
    - high: 100 → 100
    - distribution: ? → ?
  - statistics: L2
    - mean: 63.3
    - standard deviation: ? → ?
    - low: 13
    - lower quartile: 47
    - median: 68.5
    - upper quartile: 82
    - high: 99
    - distribution: ? → ?
- report
  - Is a report necessary in this case...?
  - time limit ::@:: The time limit was enough to finish all questions and check them for 20 minutes. This, of course, assumes you are very familiar with the methods used. <!--SR:!2025-01-22,26,387!2025-01-07,13,367-->
  - moment-generating function (0) ::@:: Remember to always check the domain of the expression you have gotten. If the domain is missing some numbers, you may still be able to evaluate $\operatorname E\left[e^{tX}\right]$ with $t$ set to the missing numbers to fill the domain. For example, after filling in the missing numbers, you may finally get $$\begin{cases} \frac {e^{5t} - e^{2t} } {3t}, & t \ne 0 \\ 1, & t = 0 \,. \end{cases}$$ <!-- <p> (The instructor said only I had gotten it correct...) --> <!--SR:!2025-01-15,19,367!2025-01-21,25,387-->
- check
  - datetime: 2024-12-20T14:30:00+08:00/2024-12-20T16:00:00+08:00, PT1H30M
  - venue: Room 1410 (Lift 25-26), Academic Building

> __Announcement on MATH 2411 Final Exam \[Fall 2024\]__
>
> __<u>MATH 2411 Final Exam \[Fall 2024\]</u>__ <br/>
> Time: __16th December, 2024 (Monday), 8:30 am - 11:00 am__. (EARLY in the morning) <br/>
> Venue: __S. H. Ho Sports Hall__
>
> Several things to note:
>
> - __You are advised to arrive before 8:20 am__. Please take your __student ID card__ with you. __If you are late for 30 minutes or more, you will NOT be admitted to the examination.__
> - You are NOT allowed to leave the exam venue in the first 30 minutes or the last 20 minutes during the exam.
> - If you need to go to toilet during the exam, you should raise your hand and remain seated first. The invigilator will bring your ID card to the Entrance for queuing.
> - Each of you has been assigned a unique seat number. [__<u>Seating plan</u>__](https://canvas.ust.hk/courses/59562/files/9905191 "Seating Plan -L1.pdf") and [__<u>floor plan of the venue</u>__](https://canvas.ust.hk/courses/59562/files/9905192 "HALL-MATH2411.pdf") are attached.
> - __Coverage__: Chapter 2 to Chapter 6. The materials which have been covered in midterm will be examined less. The software __R__ will NOT be tested. Optional topics such as Central Limit Theorem, Fisher z-transformation will NOT be tested.
> - __Format__: Short questions + Long questions.  For short questions, give your answers directly; for long questions, you need show ALL your working steps to receive full marks.
> - The final exam is a closed book examination. However, you are allowed to bring <u>a cheat sheet: one piece of A4 paper (double sided), printed or handwritten</u>. All the papers, including your cheat sheet and scratch paper will be collected when the exam ends, and you can take your cheat sheet back during the __Paper Checking Session \[Time/Date: 14:30-16:00, Dec 20, 2024 (Fri); Venue:   Room 1410 (Lifts 25/26) \]__.
> - You can bring ONE calculator. No restriction of the model.
> - Scratch paper will be provided. Do not use your own scratch\blank paper.
> - Necessary statistical tables of the quantiles will be provided. Use the most appropriate values from the table and indicate in your answer which values you have used.

## aftermath

### total

- grades: 100/100
  - statistics: L1
    - mean: 61.53
    - standard deviation: ?
    - low: 8.33
    - lower quartile: 43.73
    - median: 63.93
    - upper quartile: 80.36
    - high: 100
    - distribution: ?
  - statistics: L2
    - mean: 67.41
    - standard deviation: ?
    - low: 22.28
    - lower quartile: 53.33
    - median: 70.39
    - upper quartile: 84.59
    - high: 99.35
    - distribution: ?
