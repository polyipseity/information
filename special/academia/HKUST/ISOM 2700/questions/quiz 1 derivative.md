---
aliases:
  - HKUST ISOM 2700 quiz 1 derivative
  - HKUST ISOM2700 quiz 1 derivative
  - ISOM 2700 quiz 1 derivative
  - ISOM2700 quiz 1 derivative
tags:
  - flashcard/active/special/academia/HKUST/ISOM_2700/questions/quiz_1_derivative
  - language/in/English
---

# quiz 1 derivative

- HKUST ISOM 2700

> __question 1__
>
> Assume a train running between A and B serves 420 customers per hour on average. On a weekday, there are 210 customers riding or waiting on average. What is the average flow time?
>
> - solution: {@{0.5&nbsp;hours}@}
> - explanation: {@{By Little's law, average flow time = 210/420 = 0.5&nbsp;hours.}@} <!--SR:!2025-07-02,63,310!2025-07-04,65,310-->

<!-- markdownlint MD028 -->

> __question 2__
>
> Influenza is a disease that may require hospitalization, especially for old people. In a place of population 42 million, there have been 294 new hospitalization weekly. They, on average, stay in the hospital for 5 days. How many hospital beds are occupied by said patients on average?
>
> - solution: {@{210 patients}@}
> - explanation: {@{There are 294/7 = 42 new hospitalization daily. By Little's law, average inventory = 42\*5 = 210 patients.}@} <!--SR:!2025-07-05,66,310!2025-07-06,67,310-->

<!-- markdownlint MD028 -->

> __question 3__
>
> To test which type of influenza the patient has contacted, the hospital needs to collect a sample, transport it to its testing lab, and test it. The process is described below:
>
> | activity          | collection     | transport       | testing     |
> | ----------------- |:--------------:|:---------------:|:-----------:|
> | __time per unit__ | 5&nbsp;minutes | 15&nbsp;minutes | 1&nbsp;hour |
> | __resources__     | 5 people       | 3 transporters  | 20 machines |
>
> How long on average does it take for a patient to get their testing result?
>
> - solution: {@{80&nbsp;minutes}@}
> - explanation: {@{This is asking for the _flow time_. We also assume the process is _stable_. Thus, simply add up the activity time: 5+15+60 = 80&nbsp;minutes.}@} <!--SR:!2025-07-06,67,310!2025-07-01,62,310-->

<!-- markdownlint MD028 -->

> __question 4__
>
> To test which type of influenza the patient has contacted, the hospital needs to collect a sample, transport it to its testing lab, and test it. The process is described below:
>
> | activity          | collection     | transport       | testing     |
> | ----------------- |:--------------:|:---------------:|:-----------:|
> | __time per unit__ | 5&nbsp;minutes | 15&nbsp;minutes | 1&nbsp;hour |
> | __resources__     | 5 people       | 3 transporters  | 20 machines |
>
> What is the process capacity \(per hour\)?
>
> - solution: {@{12 units per hour}@}
> - explanation: {@{Transport is the bottleneck activity. In transport, each unit takes 15/3 = 5&nbsp;minutes. The process capacity is thus 60/5 = 12 units per hour.}@} <!--SR:!2025-07-05,66,310!2025-07-01,62,310-->

<!-- markdownlint MD028 -->

> __question 5__
>
> To test which type of influenza the patient has contacted, the hospital needs to collect a sample, transport it to its testing lab, and test it. The process is described below:
>
> | __activity__      | collection     | transport       | testing     |
> | ----------------- |:--------------:|:---------------:|:-----------:|
> | __time per unit__ | 5&nbsp;minutes | 15&nbsp;minutes | 1&nbsp;hour |
> | __resources__     | 5 people       | 3 transporters  | 20 machines |
>
> At process capacity, what is the utilization of the testing machines?
>
> - solution: {@{60%}@}
> - explanation: {@{The process capacity is calculated above as 12 units per hour. In testing, each unit takes 60/20 = 3&nbsp;minutes. The capacity is thus 60/3 = 20 units per hour. Thus, utilization is 12/20 = 60%.}@} <!--SR:!2025-07-02,63,310!2025-07-06,67,310-->

<!-- markdownlint MD028 -->

> __question 6__
>
> Consider the following process and resources:
>
> | __activity__           | collection     | transport               | testing     |
> | ---------------------- |:--------------:|:-----------------------:|:-----------:|
> | __time per unit__      | 5&nbsp;minutes | 15&nbsp;minutes         | 1&nbsp;hour |
> | __resources required__ | 1 person       | 1 person, 1 transporter | 1 machine   |
>
> | __resource__ | person   | transporter    | machine     |
> | ------------ |:--------:|:--------------:|:-----------:|
> | __amount__   | 1 person | 3 transporters | 20 machines |
>
> What is the process capacity?
>
> - solution: {@{3 units per hour}@}
> - explanation: {@{For people, each unit takes 5+15 = 20&nbsp;minutes. Its capacity is 3 units per hour. For transporter, each unit takes 15&nbsp;minutes. Its capacity is 4\*3 = 12 units per hour. For machine, each unit takes 60&nbsp;minutes. Its capacity is 1\*20 = 20 units per hour. So people is the bottleneck resource, thus its capacity is the process capacity.}@}
> - annotation: {@{The person resource is explicitly set to 1 person to simplify the calculations.}@} <!--SR:!2025-07-01,62,310!2025-07-03,64,310!2025-07-02,63,310-->

<!-- markdownlint MD028 -->

> __question 7__
>
> Which of the following statements is/are correct?
>
> 1. Theoretically, a process can be capacity-constrained, demand-constrained, and input-constrained at the same time.
> 2. In a purely input-constrained process, increasing input increases process capacity.
> 3. A process running at its capacity must have a process utilization of 100%.
> 4. In a purely demand-constrained process, increasing input increases process capacity.
> 5. A process running at its capacity must have utilizations of all its resources equal 100%.
> 6. Theoretically, a process can be neither capacity-constrained, demand-constrained, nor input-constrained.
> 7. A capacity-constrained process may have a less than 100% process utilization.
>
> - solution: {@{1, 2}@} <!--SR:!2025-07-01,62,310-->

<!-- markdownlint MD028 -->

> __question 8__
>
> You manage a theater. The theater can hold 4 shows at a time. You expect to start at most 3 shows in an hour. What should be the maximum show duration? Assume the process is _stable_.
>
> - solution: {@{80 minutes}@}
> - explanation: {@{The required average inventory is 4 shows. The required arrival rate is 3 shows per hour. By Little's law, required flow time = 4/3&nbsp;hours = 80&nbsp;minutes.}@} <!--SR:!2025-07-03,64,310!2025-07-05,66,310-->

<!-- markdownlint MD028 -->

> __question 9__
>
> In a process, the average flow time is 30 minutes, and the average work-in-process inventory is 7 units. What is its cycle time?
>
> - solution: {@{1/14&nbsp;hours}@}
> - explanation: {@{By Little's law, rate = 7 / 0.5 = 14 units per hour. Thus, cycle time = 1/14&nbsp;hours.}@} <!--SR:!2025-07-02,63,310!2025-07-04,65,310-->

<!-- markdownlint MD028 -->

> __question 10__
>
> A company sells a product. The selling price is \$42 per unit. The sales this year is 1&nbsp;000&nbsp;000. The variable cost is \$10 per unit. The fixed cost is \$370&nbsp;000. The invested capital into this product is \$100&nbsp;000&nbsp;000. Calculate its return on invested capital \(ROIC\).
>
> - solution: {@{31.63%}@}
> - explanation: {@{It is calculated as: $$\text{ROIC} = \left(1 - \frac {10} {42} - \frac {370\,000} {42 \times 1\,000\,000} \right) \frac {42 \times 1\,000\,000} {100\,000\,000} = 0.3163 = 31.63\% \,.$$ <p> Alternatively \(untaught\), you can calculate: $$\text{ROIC} = \frac {(42 - 10) \times 1\,000\,000 - 370\,000} {100\,000\,000} = 0.3163 = 31.63\% \,,$$ which is actually simpler... ;p}@} <!--SR:!2025-07-02,63,310!2025-06-15,46,290-->
