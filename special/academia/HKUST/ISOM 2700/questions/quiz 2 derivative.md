---
aliases:
  - HKUST ISOM 2700 quiz 2 derivative
  - HKUST ISOM2700 quiz 2 derivative
  - ISOM 2700 quiz 2 derivative
  - ISOM2700 quiz 2 derivative
tags:
  - flashcard/active/special/academia/HKUST/ISOM_2700/questions/quiz_2_derivative
  - language/in/English
---

# quiz 2 derivative

- HKUST ISOM 2700

> __question 1__
>
> An ATM machine takes on average 3 minutes to serve a customer, and follows an exponential distribution. Customers arrive at an average rate of 15 customers per hour, and follows a Poisson distribution.
>
> What is the average service rate \(per hour\)?
>
> - solution: {@{20 customers per hour}@}
> - explanation: {@{60/3 = 20 customers per hour}@} <!--SR:!2025-05-29,37,290!2025-06-30,61,310-->

<!-- markdownlint MD028 -->

> __question 2__
>
> An ATM machine takes on average 3 minutes to serve a customer, and follows an exponential distribution. Customers arrive at an average rate of 15 customers per hour, and follows a Poisson distribution.
>
> What is the average number of customers in the system?
>
> - solution: {@{3}@}
> - explanation: {@{Utilization is 15/20 = 0.75. Average number of customers in the system is 0.75/\(1–0.75\) = 3.}@} <!--SR:!2025-06-15,46,290!2025-07-01,62,310-->

<!-- markdownlint MD028 -->

> __question 3__
>
> An ATM machine takes on average 3 minutes to serve a customer, and follows an exponential distribution. Customers arrive at an average rate of 15 customers per hour, and follows a Poisson distribution.
>
> What is the idle time fraction?
>
> - solution: {@{0.25}@}
> - explanation: {@{Utilization is 15/20 = 0.75. Idle time fraction is simply 1–0.75 = 0.25.}@} <!--SR:!2025-07-02,63,310!2025-07-01,62,310-->

<!-- markdownlint MD028 -->

> __question 4__
>
> An ATM machine takes on average 3 minutes to serve a customer, and follows an exponential distribution. Customers arrive at an average rate of 15 customers per hour, and follows a Poisson distribution.
>
> Now we have 2 ATM machines with separate queues, keeping everything else the same.
>
> What is the utilization level of the system?
>
> - solution: {@{0.375}@}
> - explanation: {@{15/\(20\*2\) = 0.375. Alternatively, 0.75/2 = 0.375.}@} <!--SR:!2025-07-02,63,310!2025-07-02,63,310-->

<!-- markdownlint MD028 -->

> __question 5__
>
> An ATM machine takes on average 3 minutes to serve a customer, and follows an exponential distribution. Customers arrive at an average rate of 15 customers per hour, and follows a Poisson distribution.
>
> Now we have 2 ATM machines with separate queues, keeping everything else the same.
>
> What is the average number of customers in the system?
>
> - solution: {@{1.2}@}
> - explanation: {@{Consider one machine and its queue. The average number of customers in the system = 0.375/\(1–0.375\) = 0.6. There are two machines, so the answer is 0.6\*2 = 1.2.}@} <!--SR:!2025-07-02,63,310!2025-07-02,63,310-->

<!-- markdownlint MD028 -->

> __question 6__
>
> A manufacturing process produces 15-cm rulers, with an acceptable tolerance of 0.2&nbsp;cm. Measuring the outputs, the process produces rulers with an average length of 14.95&nbsp;cm and standard deviation of 0.04&nbsp;cm.
>
> What is its process capability index?
>
> - solution: {@{1.25}@}
> - explanation: {@{0.15/0.04/3 = 1.25}@} <!--SR:!2025-06-30,61,310!2025-07-01,62,310-->

<!-- markdownlint MD028 -->

> __question 7__
>
> A manufacturing process produces 15-cm rulers, with an acceptable tolerance of 0.2&nbsp;cm. Measuring the outputs, the process produces rulers with an average length of 14.95&nbsp;cm and standard deviation of 0.04&nbsp;cm.
>
> What is the maximum standard deviation to ensure a process capability index of 2?
>
> - solution: {@{0.025&nbsp;cm}@}
> - explanation: {@{0.15/\(3\*2\) = 0.025&nbsp;cm}@} <!--SR:!2025-06-30,61,310!2025-06-04,43,290-->

<!-- markdownlint MD028 -->

> __question 8__
>
> In a M/M/1 queue model, which of the following could produce a 10% increase in average waiting time \(in queue\)?
>
> 1. less than 10% increase in arrival rate
> 2. 10% increase in arrival rate
> 3. more than 10% increase in arrival rate
> 4. none of the above
>
> - solution: {@{1}@}
> - explanation: {@{The average waiting time in queue is: $$\frac {\rho} {\mu - \lambda} = \frac 1 \mu \frac {\rho} {1 - \rho} \,.$$ A certain increase in arrival rate increases $\rho$ by the same amount. $\rho / (1 - \rho)$ means the average waiting time in queue would increase by more than that certain amount.}@} <!--SR:!2025-07-01,62,310!2025-05-29,37,290-->

<!-- markdownlint MD028 -->

> __question 9__
>
> A customer arrives at a restaurant every 12&nbsp;minutes on average, and takes 30&nbsp;minutes on average to finish a meal. How many seats do you need at least to serve the customers \(without the queue exploding\)?
>
> - solution: {@{3}@}
> - explanation: {@{Arrival rate is 5 customers per hour. Service rate per seat is 2 customers per hour. So you need 5/2 = 2.5&nbsp;seats at least. Round it up to 3.}@} <!--SR:!2025-06-30,61,310!2025-06-30,61,310-->

<!-- markdownlint MD028 -->

> __question 10__
>
> Which of the following statements is/are true?
>
> 1. In a G/G/1 model, increasing the standard deviation of inter-arrival time increases the average waiting time in queue.
> 2. In a G/G/1 model, increasing the standard deviation of inter-arrival time increases the average waiting time in system.
> 3. A G/G/1 model must have a higher average waiting time in queue than a M/M/1 model of the same arrival rate and service rate.
> 4. In a G/G/1 model, increasing the standard deviation of service time increases the utilization.
> 5. The G/G/1 model is a generalization of the M/M/c model.
> 6. The G/G/1 model cannot be used for non-random inter-arrival time and/or non-random service time.
> 7. The M/M/1 model is a special case of the G/G/1 model.
>
> - solution: {@{1, 2, 7}@} <!--SR:!2025-06-04,43,290-->
