---
aliases:
  - HKUST ISOM 2700
  - HKUST ISOM 2700 index
  - HKUST ISOM2700
  - HKUST ISOM2700 index
  - ISOM 2700
  - ISOM 2700 index
  - ISOM2700
  - ISOM2700 index
  - Operations Management
  - Operations Management index
tags:
  - flashcard/active/special/academia/HKUST/ISOM_2700/index
  - function/index
  - language/in/English
---

# index

- HKUST ISOM 2700
- name: Operations Management

The content is in teaching order.

- grading
  - scheme
    - participation (5 of 7): 0.05
      - iPRS
      - no participation in the first 2 weeks
    - homework (2): 0.1
      - due at Sunday 23:59
      - no late submission
    - online quizzes (best 3 of 4): 0.15
      - each 10 multiple choice questions
      - release in the Monday morning
      - due at Sunday 23:59
      - no makeup quiz
    - midterm exam: 0.3
      - covers part A
      - 40 multiple choice questions
      - lasts 1 hour 40 minutes
      - 1 double-side A4 cheatsheet
      - formula sheet provided
    - final exam: 0.4
      - covers part B
      - 45 multiple choice questions
      - lasts 2 hours
      - 1 double-side A4 cheatsheet
      - formula sheet provided
- logistics
  - regrading policy: appeal within 3 days of posting of grade, regraded entirely
- syllabus
  - Module I: Managing Process and Service System
    - Identify bottlenecks, handle variability, improve performance
  - Module II: Quality and Resource Allocation
    - Measure quality, allocate resources, and make decisions
  - Module III: Matching Supply with Demand
    - Manage inventory, benefit of centralization and pooling
  - Module IV: Managing Supply Chain
    - Coordinate different players in supply chain by contract design

## children

- [assignments](assignments/)
- [questions](questions.md)

## assessments

## week 1 lecture

- datetime: 2025-02-03T10:30:00+08:00/2025-02-03T11:50:00+08:00
- topic: introduction to OM
- about the instructor
- course logistics
- [operations management](../../../../general/operations%20management.md) ::@:: to manage how a firm creates its products and/or services
  - operations management / examples ::@:: Intel: CPU, HSKH Medical: healthcare services, Ernst & Young: accounting services, HSBC: financial services, HKUST: education service
  - operations management / transformation ::@:: design, analyze, and improve the _transformation_ of _inputs_ to _outputs_, to deliver the firm's _products and services_ ("physics" of the business world)
    - operations management / transformation / elements ::@:: capital (finance), labor (management), raw resources (purchasing), technology (engineering), transformed by operations, to final products (marketing)
  - operations management / features ::@:: generality and broadness, modeling and abstraction, practical relevance, quantitative analysis
  - operations management / generality and broadness ::@:: apply to many business settings
    - operations management / generality and broadness / examples ::@:: Little's Law: flow time, flow rate, inventory level; newsvendor model: production and ordering level under uncertainty
  - operations management / modeling and abstraction ::@:: captures the key decision-making step and trade-off from a complex setting, and then apply the results back; simplifications are needed, which is convenient but can also bring limitation
  - operations management / quantitative analysis ::@:: mathematical tools are needed; relatively easy now, difficult later; but understanding the problem/picture is more important
  - operations management / practical relevance ::@:: focuses on real-world business problems and usually has substantial implications on humans; good business acumen are needed: key trade-offs, managerial insights
    - operations management / practical relevance / examples ::@:: allocation of ICU beds during the pandemic; fairness, equity, social responsibility, not just profit maximization
  - operations management / steps ::@:: description, optimization
  - operations management / description ::@:: estimate and understand the dynamics and performance of the system (like physics), e.g. expected waiting time, average inventory level, expected revenue
  - operations management / optimization ::@:: identify the ways to improve the system performance (like engineering), e.g. how to order, how to allocate
  - operations management / decisions
    - operations management / decisions / examples ::@:: capacity, demand, inventory, pricing, supply chain
  - operations management / concepts
    - operations management / concepts / examples ::@:: (chronological order) manufacturing strategy, just-in-time (JIT) production, business process re-engineering, business analytics, sustainability
  - operations management / current topics ::@:: balancing profitability and sustainability, coordination in complex global supply network, customer touch-points with technology, enhancing performance using data
  - operations management / reasons for studying ::@:: career development, rich opportunities, understanding real world firm decisions
    - operations management / reasons for studying / understanding real world firm decisions ::@:: Look inside the box. For example, there are many processes before putting products onto a storefront, such as customer services (management), distribution centers (inventory), suppliers (supply chain), plants (capacity)
    - operations management / reasons for studying / rich opportunities ::@:: management consulting, supply-chain management, synergy with other areas (e.g. accounting, finance, marketing, technology)
    - operations management / reasons for studying / career development ::@:: case interview, future study, stock-pitching/investment competitions
  - operations management / learning methods ::@:: business magazines and news media, lectures, spreadsheet analysis, real world examples; understand concepts using examples, then solve problems, then gain managerial insights

## week 1 lecture 2

- datetime: 2025-02-05T10:30:00+08:00/2025-02-05T11:50:00+08:00
- topic: process analysis, a process view of organization, Little's law, flow time analysis
- [business process](../../../../general/business%20process.md) ::@:: a set of activities; different views depending on if you are the customer or the manager
  - business process / customers' view ::@:: Let's say you are a patient in a hospital. You need to go through a set of processes: registration, preparation, procedure, recovery, and discharge. You can use a _Gantt chart_ to visualize the duration of your activities.
- [Gantt chart](../../../../general/Gantt%20chart.md) ::@:: It is a bar chart that illustrates a project schedule. It can show the sequence, duration, and dependence of activities.
- [business process](../../../../general/business%20process.md)
  - business process / managers' view ::@:: Let's say you are a manager in a hospital. There are too many patients, so you cannot create a Gantt chart for every patient. Instead, view the activities as a _process_ for each patient to pass through, i.e. _business process modeling_.
- [business process modeling](../../../../general/business%20process%20modeling.md) ::@:: The action of capturing and representing processes of an enterprise (i.e. modeling them), so that the current business processes may be analyzed, applied securely and consistently, improved, and automated.
  - business process modeling / benefits ::@:: Allows you to build a holistic/macro view of a process without delving into the (often unnecessary) details of each customer. This is using _modeling_ and _abstraction_ of OM. Then you can identify _key challenges_ and _improve_ on them.
  - business process modeling / limitation ::@:: You lose granular information on each customer. But this is often fine for the purpose of improving processes.
  - business process modeling / network model ::@:: It is a network of _activities_ (e.g. activity, _buffer_) performed by _resources_ (e.g. capital, labor, material) that transforms _inputs_ (e.g. materials, customers) into _outputs_ (e.g. goods, services). There can be more than one inputs. There can also be more than one output.
  - business process modeling / flow unit ::@:: It is what is tracked through a process, and defines the _outputs_ (not _inputs_) of interest.
- [process flow diagram](../../../../general/process%20flow%20diagram.md) ::@:: A diagram that presents major elements of a process.
  - process flow diagram / major elements ::@:: activities/operations, decision points, product flows, resources
  - process flow diagram / activity, operation ::@:: represented by a square or rectangle
  - process flow diagram / buffer, queue, storage ::@:: represented by a triangle, that may or may not be upside-down
  - process flow diagram / flow of goods or materials ::@:: represented by an arrow
  - process flow diagram / decision point ::@:: represented by a diamond (square rotated by 45 degrees), with the decision to be made written on the shape in text
  - process flow diagram / considerations ::@:: boundaries of the process (where does a process start and end), level of simplification (the more detailed, the less convenient), targets (goal-oriented, problem-driven)
- [business process modeling](../../../../general/business%20process%20modeling.md)
  - business process modeling / performance measures ::@:: capacity, cycle time, flow time, flow/through rate, work-in-process inventory
  - business process modeling / flow time ::@:: time spent by a given flow unit in the process
  - business process modeling / cycle time ::@:: time between two successive flow units outputted (product completions); this is the reciprocal of flow/through rate, _by definition_
  - business process modeling / flow/through rate ::@:: rate of flow units outputted, i.e. number of flow units outputted per unit of time; this is the reciprocal of cycle time, _by definition_
  - business process modeling / capacity ::@:: maximum flow/through rate, so this assumes there are sufficient inputs, resources, and demand
  - business process modeling / work-in-process (WIP) inventory ::@:: number of flow units in a process at a given time
- [Gantt chart](../../../../general/Gantt%20chart.md)
  - Gantt chart / multiple flow units ::@:: When representing multiple flow units over several activities, a different color is used for each flow unit.
  - Gantt chart / bottlenecks ::@:: An activity that keeps processing units. Other activities may finish faster, so the other activities may wait for new units due to the aforementioned activity being unfinished.
  - Gantt chart / finding flow time ::@:: Find the duration a color stays in the diagram. Or (assuming the system is stable) given a process diagram, add up the duration of tasks a unit needs to go through.
  - Gantt chart / finding flow rate ::@:: Find a regular pattern. Then find the number of colors being outputted in that time. Then divide by the time. <p> This is the reciprocal of cycle time, _by definition_.
  - Gantt chart / finding capacity ::@:: If there is a bottleneck, this equals the found flow rate.
  - Gantt chart / finding cycle time ::@:: Find a regular pattern. Then find the time between two colors being outputted. <p> This is the reciprocal of flow rate, _by definition_.
  - Gantt chart / finding average work-in-process (WIP) inventory ::@:: Find a regular pattern that repeats. Then find the area covered with color, which has the unit unit-time. Divide it by the duration of the regular pattern.
- cumulative inflow/outflow chart ::@:: A cumulative chart with two lines, with the _x_-axis being time and _y_-axis being the number of units. One line is the _cumulative inflow_, which increases by 1 every time a flow unit enters the process. The other line is the _cumulative outflow_, which increases by 1 every time a flow unit exits the process.
  - cumulative inflow/outflow chart / _x_-gap ::@:: The _x_-gap at a particular _y_ is the flow time for the _y_-th unit. The average _x_-gap is the average flow time.
  - cumulative inflow/outflow chart / _y_-gap ::@:: The _y_-gap at a particular _x_ is the WIP inventory at time _x_. The average _y_-gap is the average WIP inventory.
  - cumulative inflow/outflow chart / slope ::@:: The average slope of the cumulative inflow is the input flow rate. The average slope of the cumulative output flow rate. <p> These two average slopes should be the same for a _stable process_.
  - cumulative inflow/outflow chart / relation ::@:: y-gap = x-gap × slope; this is also known as Little's law
- [Little's law](../../../../general/Little's%20law.md) ::@:: It is a theorem by John Little which states that the long-term average number _L_ (_I_: average inventory) of customers in a stationary system is equal to the long-term average effective arrival rate _λ_ (_R_: average flow rate) multiplied by the average time _W_ (_T_: average flow time) that a customer spends in the system.
  - Little's law / equation ::@:: _I_ = _R_ × _T_, where _I_ is average inventory, _R_ is average flow rate, and _T_ is average flow time
  - Little's law / subprocess ::@:: It can be applied to the whole process or part of the process. When doing the latter, use the corresponding _I_, _R_, and _T_ for the part of the process.
  - Little's law / conditions ::@:: It holds for _all stable processes_, regardless of complexity (e.g. multiple flow units), sequence (e.g. FIFO, LIFO), and randomness (e.g. arrival time, flow time). <p> A _stable process_ is a process where the average rate of input equals the average rate of output, so inventory does not accumulate to infinity as time passes by.
  - Little's law / implications ::@:: Given the conditions are satisfied, one is that we can find one variable from the other two variables in the set of variables _I_, _R_, and _T_. It also means there are trade-offs when setting management goals.
  - Little's law / example ::@:: customers in supermarkets: The amount of time spent by a customer in a supermarket is important to the management. We can use Little's law to find the average time customers spend in the store.

## week 2 lecture

- datetime: 2025-02-10T10:30:00+08:00/2025-02-10T11:50:00+08:00
- topic: bottleneck analysis, throughput analysis
- [bottleneck](../../../../general/bottleneck%20(production).md) ::@:: a process in a chain of processes, such that its limited capacity reduces the capacity of the whole chain
  - bottleneck / motivation ::@:: _Process capacity_ is the _maximum_ flow rate. _Bottlenecks_ determine the process capacity. This is useful for improving process capacity, since bottlenecks determine the process capacity, we should prioritize improving the bottleneck.
- [law of the minimum](../../../../general/Liebig's%20law%20of%20the%20minimum.md) ::@:: For a process to produce a unit, every resource must finish its own job. Thus, the process capacity is determined by the slowest resource.
  - law of the minimum / examples ::@:: The capacity of a barrel with staves of unequal length is limited by the shortest stave. <p> A chain is only as strong as its weakest link. <p> The flow rate of an irregular pipe is limited by its narrowest gap.
- [bottleneck](../../../../general/bottleneck%20(production).md)
  - bottleneck / identification ::@:: List activities, resources (workers to perform activities), and processing times. Assign resources to activities (the assignment can be very complex). For each resource (not activity), compute its workload needed to produce a unit and thus its _capacity_. Finally, identify the _bottleneck resource_, which is the resource with the _lowest_ capacity.
    - bottleneck / identification / scenarios ::@:: In general, multiple resources can be assigned to multiple tasks, with AND/OR connecting the resources. <p> For this course, we consider 3 simple scenarios: one-to-one (each resource is required by exactly one activity), and (one resource is needed in multiple activities), and or (one activity can be performed by multiple resources).
    - bottleneck / identification / one-to-one ::@:: Simple. Simply find the resource with the _lowest_ capacity.
    - bottleneck / identification / and ::@:: Determine activities by each resources that is required to produce a unit. Find the time required per unit, and thus its capacity. Then find the resource with the _lowest_ capacity.
    - bottleneck / identification / or ::@:: Pool multiple resources that can perform the same process into one, effectively treating the resource as one. Its capacity is the sum of the capacities of the multiple resources. Then find the resource with the _lowest_ capacity.
    - bottleneck / identification / random process ::@:: Sometimes, only a percentage (not all) units flow from a process (process A) to another process (process B). In this case, we should find process B's _effective_ capacity from its actual capacity. It can be obtained by dividing its actual capacity by the percentage of units that flow from process A to process B.
- [production leveling](../../../../general/production%20leveling.md) (line balancing) ::@:: By moving capacity to bottlenecks or moving workload to underutilized resources, we can balance the workload among resources in the process. This helps raise the capacity of bottlenecks and reduces _supply—demand mismatch_ within the process.
  - production leveling / examples ::@:: flexible line layouts: Operators can move nearby instead of being stuck to a fixed location to self-balance the workload. It also makes it easier to add or remove operators. <br/> U-shaped lines: Operators do not need to move as much to reach a process that is further away. Less operators are also needed as operators can work on multiple processes that are far away from each other.
- [capacity utilization](../../../../general/capacity%20utilization.md) ::@:: flow rate / resource capacity <p> It measures how much of the resource capacity is being used.
- [bottleneck](../../../../general/bottleneck%20(production).md)
  - bottleneck / utilization ::@:: Given the flow rate is the same for all resources (which may _not_ be the case if the process is random), if a resource has lower capacity, it has higher utilization. So the bottleneck can also be stated as the resource with _highest utilization_.
- [capacity utilization](../../../../general/capacity%20utilization.md)
  - capacity utilization / utilization profile chart ::@:: Plot a bar chart of each resource and its utilization (in percentage).
    - capacity utilization / utilization profile chart / interpretation ::@:: Given the flow rate is the same for all resources (which may _not_ be the case if the process is random), the resource with the highest utilization is the _bottleneck_. The gap between the highest utilization and the lowest utilization is the _imbalance_ relative to the bottleneck. The gap between 100% and the highest utilization is the _mismatch between supply and demand_ (explained below).
- flow rate
  - flow rate / input, process capacity, potential demand ::@:: It is the minimum between input, process capacity, and potential demand.
  - flow rate / input-constrained ::@:: Input is fully used. Process capacity is not fully used. Potential demand is not fully satisfied.
  - flow rate / demand-constrained ::@:: Input is not fully used. Process capacity is not fully used. Potential demand is fully satisfied.
  - flow rate / capacity-constrained ::@:: Input is not fully used. Process capacity is fully used. Potential demand is not fully satisfied.
- [capacity utilization](../../../../general/capacity%20utilization.md)
  - capacity utilization / process utilization ::@:: It is defined as the _bottleneck_ utilization.
    - capacity utilization / process utilization / lower than 100% ::@:: Given the flow rate is the same for all resources (which may _not_ be the case if the process is random), this means the process is _not_ capacity-constrained, but either input-constrained or demand-constrained (or both).

---

- tag: optional
- [capacity utilization](../../../../general/capacity%20utilization.md)
  - capacity utilization / complex processes ::@:: If the process have multiple flow units or is complex with different paths, e.g. patients of different severity, then we calculate the _implied utilization_ for each resource. The _bottleneck_ is the resource with the highest _implied utilization_ (this is true even for complex processes).
  - capacity utilization / implied utilization ::@:: demand for a resource over all types of flow units / capacity of a resource <p> It can be higher than 100%, implying that the capacity cannot meet the demand.

## week 2 lecture 2

- datetime: 2025-02-12T10:30:00+08:00/2025-02-12T11:50:00+08:00
- topic: OM and finance, inventory turnover analysis, ROIC tree, basic statistics concepts
- [operations management](../../../../general/operations%20management.md)
  - operations management / accounting & finance ::@:: It plays an important role in understanding and improving a firm's financial performance. <p> Examples are inventory costs, inventory turnover, and return on invested capital (ROIC).
- [inventory](../../../../general/inventory.md) ::@:: It refers to the goods and materials that a business holds for the ultimate goal of resale, production or utilization.
  - inventory / importance ::@:: They are everywhere. So it is an important signal for managers and analysts to determine how well a retailer is running its business. <p> An empirical analysis for over 353 publicly listed U.S. retailers for the period 1985–2003 inventory shows: 57% publicly traded retailers has inventory as the largest asset on the balance sheet. On average, the inventory takes up 35.1% of total assets.
  - inventory / benefits ::@:: economics of scale (i.e. produce more than the _current_ demand), meet variation in demand or processes (e.g. unexpected shocks), independence between operations (the inventory act as a buffer)
  - inventory / costs ::@:: carrying/holding costs, overhead costs (e.g. ordering, production change, setup), shortage costs (due to lost sales)
  - inventory / inventory turnover ::@:: $$\frac 1 {\text{flow time} } = \frac {\text{\# units sold in a period (flow rate)} } {\text{\# units in inventory (inventory)} } = \frac {\text{COGS in a period} } {\text{average inventory at cost} }$$ <p> The first equality is by Little's law. The second equality is by multiplying average purchase cost on both top and bottom, since we generally do not know the numbers of units in inventory and sold in financial statements.
    - inventory / inventory turnover / sources ::@:: _Flow time_ is how long a unit spends in the inventory before being sold. COGS in a period and _average_ inventory at (purchasing) cost can be obtained from financial statements.
  - inventory / weeks of supply ::@:: This is basically how long the _average_ inventory at cost can last (assuming no new purchases), in number of weeks. <p> To calculate it, it is the _reciprocal_ of inventory turnover multiplied by _52_ weeks. It is also the flow time (which is in years) multiplied by _52_ weeks.
  - inventory / per unit inventory holding cost ::@:: It measures the holding cost per unit relative to the unit's purchase cost. <p> To calculate it, divide annual inventory holding cost (in % of average inventory) by annual inventory turnover. <p> The key insight is that each inventory turnover "refreshes" the average inventory.
  - inventory / inventory turnover
    - inventory / inventory turnover / interpretation ::@:: It can evaluate a firm's performance by comparing it with firms in the _same_ sector, since it can vary drastically across sectors (e.g. from 6.70 in consumer sector to 48.76 in finance sector).
- [return on invested capital](../../../../general/return%20on%20capital.md) (ROIC) ::@:: It is a ratio used in finance, valuation and accounting, as a measure of the profitability and value-creating potential of companies relative to the amount of capital invested by shareholders and other debtholders. <p> It is calculated as: return (NOPAT) / average invested capital, where NOPAT is net operating income after tax
  - return on invested capital / economic value created ::@:: economic value created = capital \* (ROIC - WACC), where WACC is the weighted average cost of capital
  - return on invested capital / OM ::@:: We can either calculate NOPAT (which may be easier sometimes...), or use the DuPont model to see how ROIC is related to OM measures, e.g. flow rate.
  - return on invested capital / [DuPont analysis](../../../../general/DuPont%20analysis.md) ::@:: ROIC = return (NOPAT) / average invested capital = (return / revenue) \* (revenue / invested capital) = margin \* asset turnover
    - return on invested capital / DuPoint analysis / OM ::@:: margin = 1 − fixed costs / (_flow rate_ \* price) − variable costs / price <br/> asset turnover = _flow rate_ \* price / invested capital
      - return on invested capital / DuPoint analysis / OM / margin ::@:: Increasing flow rate increases margin by dividing the fixed costs by a larger denominator. This means the fixed costs are spread throughout more units. (Imagine infinite flow rate: fixed cost would be negligible compared to variable cost.)
      - return on invested capital / DuPoint analysis / OM / asset turnover ::@:: Increasing flow rate increases asset turnover by increasing revenue by simply selling more units in a period for the same amount of invested capital.
  - return on invested capital / what-if analysis ::@:: Using DuPoint analysis, we can quickly figure out how increase in flow rate increases ROIC. <p> To calculate them, calculate the old and new ROIC. You can then calculate the (percentage) increase in ROIC. You can also calculate the increase in return by multiplying the ROIC difference with the invested capital (assuming the invested capital remains the same).
- [random variable](../../../../general/random%20variable.md) (r.v.) ::@:: A __random variable__ (__r.v.__) is a mathematical function. Its _domain_ is the sample space. Its _range_ is a measurable space, usually a finite set of integers or the real numbers. The function need not be _injective_ (different samples need not map to different values). It is commonly denoted by capital letters, with its possible numerical values (also called __realizations__) by the same but lowercase letters. <p> A way to think about random variable is that it maps each outcome to a real number.
  - random variable / for business ::@:: Many random variables in practice can be described by mean and variance (square of standard deviation). The exact distribution can be specified using a cumulative distribution function (CDF) $F(Q)$ or probability density function (PDF) $f(q)$ (actually for discrete values, it should be probability mass function (PMF)).
  - random variable / motivation ::@:: Demand for a product or service is usually random. Demand forecasting is important in OM (learn later/below), and is done by obtaining demand distribution from historical or survey data. <p> But before we do that, how do we describe demand more mathematically? Random variables can do so.
- [cumulative distribution function](../../../../general/cumulative%20distribution%20function.md) (CDF, cdf) ::@:: A __cumulative distribution function__ (__CDF__, __cdf__) of a real-valued random variable _X_ is the probability that _X_ will take a value less than or equal to _x_. It is given by: $$F_X(x) = P(X \le x) \,.$$ The probability that _X_ will take a value in between \(_a_, _b_\], where _a_ < _b_, is $$P(a < X \le b) = F_X(b) - F_X(a) \,.$$
- [probability density function](../../../../general/probability%20density%20function.md) (PDF, pdf) ::@:: The __probability density function__ (__PDF__, __pdf__) of an _absolutely continuous_ random variable is a function whose value at any given sample (or point) in the sample space (the set of possible values taken by the random variable) can be interpreted as providing a _relative likelihood_ that the value of the random variable would be equal to that sample. <p> Probability density is the probability per unit length, in other words, the _absolute likelihood_ for a continuous random variable to take on any particular value is 0 since there is an infinite set of possible values to begin with. <p> It is commonly denoted $f_X(x)$ for an absolutely continuous random variable _X_.
- [probability mass function](../../../../general/probability%20mass%20function.md) (PMF, pmf) ::@:: A __probability mass function__ (__PMF__, __pmf__) is a function that gives the probability that a _discrete random variable_ is exactly equal to some value. It is given by: $$p_X(x) = P(X = x) \,.$$ It is not defined for a continuous random variable. <p> The PMF has the following properties: $$\begin{aligned} \sum_x p_X(x) & = 1 \\ p_X(x) & \ge 0 \,. \end{aligned}$$
- [expected value](../../../../general/expected%20value.md) ::@:: The __expected value__ (__population mean__, __first moment__) is a generalization of the weighted average. Informally, the expected value is the mean of the possible values a random variable can take, weighted by the probability of those outcomes. It is commonly denoted $E(X)$.
  - expected value / discrete random variable ::@:: The expected value of a discrete random variable is the weighted average of all possible outcomes $\mathcal X$: $$\operatorname E[X] = \sum_{x \in \mathcal X} x p(x) \,.$$ <p> (optional, uncovered) This is only defined if the sum converges absolutely, so it is possible for a discrete random variable to have a undefined expected value. <p> Also, $$\operatorname E[g(X)] = \sum_{x \in \mathcal X} g(x) p(x) \,.$$ for an arbitrary function $g(x)$.
  - expected value / continuous random variable (optional) ::@:: The expected value of a continuous random variable is the weighted average of all possible outcomes $\mathcal X$: $$\operatorname E[X] = \int_{-\infty}^{+\infty} \! x f(x) \,\mathrm{d}x = \int_{-\infty}^{+\infty} x \,\mathrm{d}F(x) \,.$$ <p> (uncovered) This is only defined if the integral converges absolutely, so it is possible for a continuous random variable to have a undefined expected value. <p> Also, $$\operatorname E[g(X)] = \int_{-\infty}^{+\infty} \! g(x) f(x) \,\mathrm{d}x = \int_{-\infty}^{+\infty} g(x) \,\mathrm{d}F(x) \,.$$ for an arbitrary function $g(x)$.
- [coefficient of variation](../../../../general/coefficient%20of%20variation.md) ::@:: It is defined as the ratio of the standard deviation (_not_ variance) $\sigma$ to the mean $\mu$, $CV={\frac {\sigma }{\mu } }$. <p> It shows the extent of variability in relation to the mean of the population.
  - coefficient of variation / OM ::@:: Widely used in OM to measure the degree of variation for different objectives. It shows the core OM idea of _standardization_.
- [sample mean](sample%20mean%20and%20covariance.md)
  - sample mean / equation ::@:: Given _N_ samples of a random variable _X_, its _sample mean_ is: $$\overline X = \frac 1 N \sum_{k = 1}^N X_k \,.$$
  - sample mean / properties ::@:: It is _unbiased_: $\operatorname E[\overline X] = \mu_X$. It has a variance that is inversely proportional to the number of samples: $\operatorname{Var}(\overline X) = \frac {\sigma_X^2} N$ (hence $\operatorname{Sd}(\overline X) = \frac {\sigma_X} {\sqrt N}$).
  - sample mean / sample sum ::@:: The sample mean but without dividing by _N_. Same properties as sample mean, except multiply the expected value (mean) by _N_ and variance by _N_<sup>2</sup> (hence multiply standard deviation by _N_).
    - sample mean / sample sum / pooling ::@:: Calculate the coefficient of variation (CV) for a sample versus a sample sum (_n_ samples). We can see the latter's CV is divided by $\sqrt n$. This shows pooling can reduce variability.
      - sample mean / sample sum / pooling / examples ::@:: In retailing, prefer consolidated distribution over direct delivery. In queueing, prefer pooled queues over dedicated queues.
- [normal distribution](../../../../general/normal%20distribution.md) ::@:: The __normal distribution__ or __Gaussian distribution__ is important in statistics and is often used in the natural and social sciences to represent real-valued random variables whose distributions are not known. Their importance is partly due to the central limit theorem. It is denoted $\mathcal N(\mu, \sigma^2)$, where $\mu \in \mathbb R$ is the mean and $\sigma^2 \in \mathbb R_{> 0}$ is the variance. <p> Note: When you see $\mathcal N(0, 100)$, do not mistake the 100 as the standard deviation! It is the variance.
  - normal distribution / motivation ::@:: Many probability distributions in OM can be described by normal distributions... Further, normal distributions can be standardized easily.
  - normal distribution / shape ::@:: All normal distribution have the bell-shaped regardless of its parameters. Changing the mean simply translates the shape, while increasing the variance fattens (becomes wider) and flattens (the maximum value becomes lower) the shape.
  - normal distribution / standard normal distribution ::@:: The __standard normal distribution__ has the mean, $\mu$, 0, and the variance, $\sigma^2$, 1. Its CDF is commonly denoted by $\Phi(z)$ while its PDF is commonly denoted by $\varphi(z)$. <p> A property of its CDF due to the even symmetry of its PDF: $$\Phi(-z) = 1 - \Phi(z) \,.$$
  - normal distribution / standardization ::@:: Any normal distribution can be __standardized__ by defining the random variable $$Z = \frac {X - \mu} {\sigma} \qquad X = \sigma Z + \mu \,.$$ Further, $$z = \frac {x - \mu} \sigma$$ is also known as the __standard score__ of the data _x_. <p> After standardization, a standard normal table that provides $\Phi(z)$ for different values of _z_ may be used to evaluate the CDF of any normal distribution. (The table may not show negative values of _z_. In that case, you need to use the property of its CDF above.)

## week 3 lecture

- datetime: 2025-02-17T10:30:00+08:00/2025-02-17T11:50:00+08:00
- topic: managing uncertainty in service system, basics of queueing system
- [queueing theory](../../../../general/queueing%20theory.md)
  - queueing theory / motivation (OM) ::@:: Consider offering a service. Ideally there should be no variability in both arrival and service time, since in that case ensuring the utilization is below 100% suffices to avoid waiting. But in practice there are variability, which can cause waiting even if utilization is below 100%. The cause are that: one, services cannot be buffered (stored), unlike goods; two, there is short-term (temporary) mismatch between demand and supply.
    - queueing theory / motivation (OM) / examples ::@:: call centers, hospitals, restaurants, theme parks
  - queueing theory / why study ::@:: It can model queueing systems. Then we can describe its performance (description; e.g. queue length, waiting time) and improve it (optimization; e.g. reduce waiting time). For services, it can improve customer services, enhance their satisfaction, and increase our profits.
  - queueing theory / queueing model ::@:: It can be described as _customers_ lining up in _queues_ to be served by _servers_. For simplicity, we assume any server can serve any customer here. <p> Many models require customer arrival (random) distribution, service time (random) distribution, and system configuration (e.g. FIFO, \# of queues, \# of servers). Then the model can tell us the system performance, e.g. average customers in a queue or the system, average waiting time in a queue or the system.
  - queueing theory / server ::@:: A server is necessary resources to serve one customer _independently_ at _one time_. $n$ servers means you can at most server $n$ customers simultaneously. Note that a server does not necessarily correspond to a single machine or person.
  - queueing theory / inter-arrival time ::@:: Time between two consecutive arrivals of customers. It can be random. <p> The others can be inferred from knowing one of these: arrival time, inter-arrival time, total arrivals.
  - queueing theory / service time ::@:: Time to serve a customer. It can be random.
  - queueing theory / arrival time ::@:: The time when a certain customer arrives. It can be random. <p> The others can be inferred from knowing one of these: arrival time, inter-arrival time, total arrivals.
  - queueing theory / total arrivals ::@:: The number of customers that has arrived up to a time. It can be random. <p> The others can be inferred from knowing one of these: arrival time, inter-arrival time, total arrivals.
  - queueing theory / note ::@:: The term _waiting time_ usually refers to the average _queue_ waiting time, excluding the _service time_.
- [M/M/c queue](../../../../general/M_M_c%20queue.md) (slides: M/M/s model) ::@:: M/M/c: _exponential_ inter-arrival time/_exponential_ service time/number of servers; assume one FIFO (first-in first-out)/FCFS (first-come first-serve) queue <p> However, we prefer to use rates instead of time. Exponential distributions in terms of _time_ can be converted into Poisson distributions in terms of _rate_. So arrival rate and service capacity follow Poisson instead.
  - M/M/c queue / inputs ::@:: arrival _rate_ (follows Poisson distribution): $\lambda$, average service _rate_ of _one_ server (follows Poisson distribution): $\mu$, number of servers: $c$ (slides: $s$), number of queues: 1 (fixed)
  - M/M/c queue / assumptions ::@:: Since arrival rate and and average service rate are parameters of a Poisson distribution, we assume occurrences are independent. In this context, this means number of arrivals in two different periods (arrival rate \* period length) and inter-arrival times are independent. <p> In this course, we assume $\lambda < c \mu$. That is, on average, we can serve customers faster than they can come, so that our queues will not become unbounded (infinite).
  - M/M/c queue / capacity, flow rate ::@:: The arrival rate $\lambda$ is the flow rate. The service rate $\mu$ is the capacity of _one_ server.
  - M/M/c queue / server utilization ::@:: Calculated as: $\rho = \frac {\lambda} {c \mu} \,,$ which can be interpreted as the average fraction a server is busy. The _stable_ condition is when $\rho < 1$, i.e. $\lambda < c \mu$ (serve customers faster than they can come), which is what we have assumed above.
  - M/M/c queue / performance metrics ::@:: average queue/system length, average queue/system waiting time, probability of waiting on arrival (queue being nonempty), server utilization
  - M/M/c queue / average queue waiting time, average system waiting time ::@:: $W_s = W_q + \frac 1 \mu \,,$ where $W_s$ is average system waiting time and $W_q$ is average queue waiting time. They can be interpreted as flow time.
  - M/M/c queue / average queue length, average system length ::@:: $L_s = L_q + c \rho \,,$ where $L_s$ is average system length and $L_q$ is average queue length. They can be interpreted as average inventory.
  - M/M/c queue / Little's law ::@:: $L_s = \lambda W_s \qquad L_q = \lambda W_q$
- [M/M/1 queue](../../../../general/M_M_1%20queue.md) ::@:: M/M/1: _exponential_ inter-arrival time/_exponential_ service time/1 server; assume one FIFO (first-in first-out)/FCFS (first-come first-serve) queue
  - M/M/1 queue / server utilization ::@:: Assuming the system is stable ($\lambda < \mu$). It is: $\rho = \frac \lambda \mu \,,$ since $c = 1$.
  - M/M/1 queue / system length distribution ::@:: Assuming the system is stable ($\lambda < \mu$). The probability of having $n$ customers in the system (including the one being served): $P_n = \rho^n (1 - \rho)$, a _unshifted_ geometric distribution with the success probability $1 - \rho$. <p> Intuition: Each $\rho$ term corresponds to the probability of adding 1 customer to the queue. $1 - \rho$ corresponds to the probability of ending the queue, which is independent of the number of customers being added.
  - M/M/1 queue / probability of waiting ::@:: Assuming the system is stable ($\lambda < \mu$). This equals the probability of having nonzero customers in the system: $1 - P_0 = 1 - (1 - \rho) = \rho$, which equals server utilization (intuitively).
  - M/M/1 queue / average system length ::@:: Assuming the system is stable ($\lambda < \mu$). $L_s = \frac {\lambda} {\mu - \lambda} = \frac {\rho} {1 - \rho}$, the mean of a _unshifted_ geometric distribution with the success probability $1 - \rho$.
  - M/M/1 queue / average queue length ::@:: Assuming the system is stable ($\lambda < \mu$). $L_q = \rho L_s = \frac {\lambda} {\mu} \frac {\lambda} {\mu - \lambda} = \frac {\rho^2} {1 - \rho}$
  - M/M/1 queue / average system waiting time ::@:: Assuming the system is stable ($\lambda < \mu$). $W_s = \frac {L_s} {\lambda} = \frac 1 {\mu - \lambda}$
  - M/M/1 queue / average queue waiting time ::@:: Assuming the system is stable ($\lambda < \mu$). $W_q = \frac {L_q} {\lambda} = \frac \rho {\mu - \lambda}$
  - M/M/1 queue / insight ::@:: The average system length being $\frac {\rho} {1 - \rho}$ implies that it grows super-linearly (growth that is faster than linear) as $\rho$ approaches 1. That means it is very costly (congestion) to have near maximum utilization when there are variations. With no variations, congestion will not happen even if $\rho < 1$ is very near 1.

## week 3 lecture 2

- datetime: 2025-02-19T10:30:00+08:00/2025-02-19T11:50:00+08:00
- topic: managing uncertainty in service system, M/M/s queuing systems
- attendance
- M/M/1 queue
- M/M/c queue
  - M/M/c queue / difference from M/M/1 queue ::@:: Arrival rate $\lambda$ and service rate (of _one_ server) $\mu$ means the same thing. The only difference is that $c$ is not restricted to being 1. <p> We still assume the system is _stable_, i.e. $\lambda < c \mu$.
  - M/M/c queue / metrics ::@:: Similar to that of M/M/1 queue, we have: $L_q$, $L_s$, $W_q$, $W_s$, $P(0)$, $P(\mathrm{delay})$, and $\rho$.
    - M/M/c queue / metrics / equations ::@:: Unfortunately, there are equations for the performance of the system, but many of them are complicated, so we provide a M/M/c queueing spreadsheet for you instead.
    - M/M/c queue / metrics / equations (simple) ::@:: Little's law; utilization $\rho = \lambda / c \mu$; relation between $L_q$ and $L_s$: $L_s = L_q + c \rho$; and relation between $W_q$ and $W_s = W_q + \frac 1 \mu$ still hold. <p> However, $P(\mathrm{delay})$ can be less than $1 - P(0)$ instead of being equal to, since there can be multiple servers now. Indeed, $P(\mathrm{delay}) = 1 - (P(0) + P(1) + \cdots + P(c - 1)) \,.$
  - M/M/c queue / benefits over M/M/1 queue ::@:: Average queue length, average system length, average waiting time, and probability of waiting all decrease significantly.
- queueing theory
  - queueing theory / cost ::@:: There can be many ways to measure cost. One simple way is: <p> &emsp; total cost (per unit of time) = service cost (per unit of time) + waiting cost (per unit of time) <p> where service cost is proportional to number of servers $S$ while waiting cost is proportional to mean queue length $L_q$ (_not_ mean system length $L_s$). So we have: $$C = C_s S + C_w L_q \,,$$ where $C_s$ is the service cost per server (per unit of time) and $C_w$ is the waiting cost per customer (per unit of time).
    - queueing theory / cost / optimization ::@:: To optimize it, find where the total cost is minimum. <p> To compare two scenarios, compare their total costs and choose the one that is lower. Irrelevant costs (cost that do not differ between the scenarios) can be ignored.
    - queueing theory / cost / insight ::@:: How many servers should we add? It is not the case that more servers is better. This is because while service cost grows linearly wth number of servers, waiting cost does not shrink linearly: an example of diminishing returns.
  - queueing theory / pooled vs. separate ::@:: Pooled queue (1 queue for all servers) and separate queue (1 queue per server) can be compared using queue theory.
    - queueing theory / pooled vs. separate / models ::@:: Let $\lambda'$ be the arrival rate, $\mu'$ be the service rate of _one_ server, and $s$ be the number of servers. Then: <p> (former): M/M/c model with $\lambda = \lambda', \mu = \mu', c = s$ <br/> (latter) M/M/1 model with $\lambda = \lambda' / s, \mu = \mu', c = 1$.
    - queueing theory / pooled vs. separate / results ::@:: We see that the utilization $\rho$ is still the same, but significantly less average queue waiting time $L_q$ for the former. <p> Indeed, as utilization approaches 1, while $L_q$ for both goes to infinity quickly, the former does so significantly slower than the latter.
    - queueing theory / pooled vs. separate / insight ::@:: In the former, it is impossible for someone to be in queue while there are server being idle. This is possible in the latter. So this is why the former performs better than the latter: it leads to better _matching_ between _supply and demand_. <p> So how should we pool the servers? If we _only_ care about waiting time, then we should pool all servers together. Even if this is not possible, some initial degree of pooling still yields most of the improvements (with further pooling yielding diminishing returns).
    - queueing theory / disadvantages ::@:: The advantages are obvious. But there are also disadvantages. The queue is more crowded/longer. As a result, customers _feel_ they have less ownership, and there may be negative behavioral and psychological effects on them. <p> Remember that _feelings of your customers_ sometimes matter as much as the _actual_ waiting time, and it all depends on the situation.
- [questions § week 3 lecture 2](questions.md#week%203%20lecture%202)

## week 4 lecture

- datetime: 2025-02-24T10:30:00+08:00/2025-02-24T11:50:00+08:00
- topic: queueing system, simulation method
- M/M/1 queue
- M/M/c queue
- [G/G/1 queue](../../../../general/G_G_1%20queue.md) ::@:: M/M/1: _general_ (unknown distribution) inter-arrival time/_general_ (unknown distribution) service time/1 server; assume one FIFO (first-in first-out)/FCFS (first-come first-serve) queue
  - G/G/1 queue / motivation ::@:: In M/M/1 queue, we assume inter-arrival times and service times follow exponential distributions. But this may not hold in many situations. If we drop the above assumption, then we get this model. <p> Note that M/M/1 (_not_ M/M/c though) is a _special case_ of this.
  - G/G/1 queue / parameters ::@:: arrival: average rate $\lambda$, coefficient of variation $\text{CV}_a$ (use the distribution of the inter-arrival time, e.g. exponential) <br/> service: average rate $\mu$ (average service time: $T_p = 1 / \mu$), coefficient of variation $\text{CV}_p$ (use the distribution of the service time, e.g. exponential)
  - G/G/1 queue / average queue waiting time ::@:: It is given by the [Kingman's formula](../../../../general/Kingman's%20formula.md): $$W_q = \left(\frac \rho {1 - \rho}\right) \left(\frac {\text{CV}_a^2 + \text{CV}_p^2} 2 \right) T_p \,.$$ <p> Note that this is the _queue_ average waiting time, not _system_ average waiting time.
    - [Kingman's formula](../../../../general/Kingman's%20formula.md)
    - G/G/1 queue / average queue waiting time / utilization factor ::@:: The term is $\frac \rho {1 - \rho}$. Higher utilization increases the average waiting time. The effect of it is very similar to that of M/M/1 queue and M/M/c queue: it grows super-linearly (growth that is faster than linear) as $\rho$ approaches 1.
    - G/G/1 queue / average queue waiting time / variability factor ::@:: The term is $\frac {\text{CV}_a^2 + \text{CV}_p^2} 2$. Higher variability in inter-arrival time or service time increases the average waiting time.
    - G/G/1 queue / average queue waiting time / service time factor ::@:: The term is $T_p = \frac 1 \mu$. Obviously, the longer the service time, the longer the waiting time.
  - G/G/1 queue / other performance metrics ::@:: Little's law; utilization $\rho$; relation between $L_q$ and $L_s$: $L_s = L_q + \rho$ ($c = 1$); and relation between $W_q$ and $W_s = W_q + \frac 1 \mu = W_q + T_q$ still hold.
  - G/G/1 queue / special case: M/M/1 queue ::@:: In M/M/1 queue, $\lambda$ and $\mu$ have the same values. For coefficients of variation: $\text{CV}_a = \frac {\sqrt{1 / \lambda^2} } {1 / \lambda} = 1$ and $\text{CV}_p = \frac {\sqrt{1 / \mu^2} } {1 / \mu} = 1$, since for exponential distributions, both mean and standard deviation are the same. <p> This means we have: $$W_q = \left(\frac \rho {1 - \rho} \right) \left(\frac {1^2 + 1^2} 2 \right) T_p = \frac \rho {1 - \rho} \frac 1 \mu = \frac {\lambda} {\mu - \lambda} \frac 1 \mu = \frac \rho {\mu - \lambda} \,,$$ which is the same as above.
  - G/G/1 queue / special case: no variability ::@:: Assume the system is stable, i.e. utilization is below 1. We can see that if there are no variability for both inter-arrival time and service time, then $CV_a = CV_p = 0$. The formula tells us that the average queue waiting time is 0, as expected.
- [patience](../../../../general/patience.md)
  - patience / psychology of waiting ::@:: anxiety, comfortableness, explainability, fairness, occupancy, progress, social, uncertainty
    - patience / psychology of waiting / occupancy ::@:: Unoccupied time feels longer than occupied time. <p> mitigations: Divert customer's attention while waiting, e.g. entertain, enlighten, and engage (Katz et al., 1991).
    - patience / psychology of waiting / progress ::@:: Pre-process/pre-progress waiting feels longer than in-process/in-progress waiting. <p> mitigations: Minimize the first queue waiting time to avoid balking. Quick "foot in the door".
    - patience / psychology of waiting / anxiety ::@:: It makes waiting feels longer. <p> mitigations: Ensure customers do not feel forgotten. Serve new or infrequent customers keeping in mind that they feel they wait longer (due to uncertainty causing anxiety).
    - patience / psychology of waiting / uncertainty  ::@:: Uncertain waiting feels longer than known and finite waiting. <p> mitigations: Inform customers how long to expect, e.g. a wait time noticeboard. One may _surprise_ the customer with a shorter actual waiting time.
    - patience / psychology of waiting / explainability ::@:: Unexplained waiting feels longer than explained waiting. <p> mitigations: Provide (real) reasons to keep customers waiting, e.g. on a noticeboard.
    - patience / psychology of waiting / fairness ::@:: Unfair waiting feels longer than fair/equitable waiting. <p> mitigations: Design the system to ensure fairness, e.g. FCFS (first-come first-serve).
    - patience / psychology of waiting / comfortableness ::@:: Uncomfortable waiting feels longer than comfortable waiting. <p> mitigations: Design a more comfortable waiting environment, e.g. adding sofas.
    - patience / psychology of waiting / social ::@:: Solo waiting feels longer than group waiting. <p> mitigations: Design a more social waiting environment that encourages interactions.
    - patience / psychology of waiting / importance ::@:: How long customers _actually_ wait is as important as how long customers _feel_ like they have waited. In some cases, it is possible that customers _actually_ wait longer but they _feel_ like they have waited less.
- [simulation](../../../../general/simulation.md) ::@:: an imitative representation of a process or system that could exist in the real world
  - simulation / motivation ::@:: What if a system (e.g. queue system) is complex enough (e.g. queue abandonment, queue deterioration, queue layers) that no closed formulas exist? Make a model that _mimics_ the real system, that incorporates its dynamics and _variability_. Then we can _estimate_ _average_ system performance metrics after running the simulation for many times or for a long time period.
  - simulation / applications ::@:: financial investments (backtesting, estimating stock prices), inventory ordering (estimating order amount), waiting lines
  - simulation / advantages ::@:: It can handle very complex systems. It can answer "what if"/counterfactual questions. It does not interfere with the real system (since you are running a model of it).
  - simulation / disadvantages ::@:: It does not necessarily yield an _exact_ and _optimal_ solution. The model may not completely reflect the real system. It requires good inputs from the management (i.e. garbage in, garbage out).
  - simulation / key ingredients ::@:: dynamics/evolution (how it evolves, e.g. decision making), performance measures (how it performs, e.g. portfolio return, inventory costs), variability sources (where it varies, e.g. arrival time, processing time), randomness (how to model its variability, e.g. distribution of random variables)
- [Monte Carlo method](../../../../general/Monte%20Carlo%20method.md) ::@:: a broad class of computational algorithms that rely on repeated random sampling to obtain numerical results
  - Monte Carlo method / steps ::@:: define the problem → define performance variables and _representative_ random variables → generate random variables → identify relations between random and performance variables → run simulation and inspect results
  - Monte Carlo method / define the problem ::@:: What is the problem you are trying to solve? It could be estimating a performance metric of your queue system.
  - Monte Carlo method / define performance variables and _representative_ random variables ::@:: _Representative_ random variables are _exogenous_ (not determinable from the system dynamics only) random variables determining the system dynamics, e.g. inter-arrival time, service time, etc. <p> Performance variables are the metrics that you are interested in finding out to help you solve the problem. They are usually determined by the system dynamics given the representative random variables, eg. waiting time in queue, etc.
  - Monte Carlo method / generate random variables ::@:: Collect data from the real world. Then set up its probabilistic model, balancing analytical convenience vs. fitting power for reality. Finally, sample the random variable according to its distribution (using the field of probability and statistics).
  - Monte Carlo method / identify relations between random and performance variables ::@:: Determine how system dynamics relate the variables in the system. The relations start from the representative random variables. Intermediate variables may be used, e.g. arrival time, service completion time, service start time, etc.
  - Monte Carlo method / run simulation and inspect results ::@:: This highly depends on how you make the model, e.g. using Microsoft Excel spreadsheets and its `RAND()` function, etc.

## week 4 lecture 2

- datetime: 2025-02-26T10:30:00+08:00/2025-02-26T11:50:00+08:00
- topic: quality management, variability in quality, capability analysis
- [quality](../../../../general/quality%20(business.md)) ::@:: It has a pragmatic interpretation as the non-inferiority or superiority of something (goods or services); it is also defined as being suitable for the intended purpose (fitness for purpose) while satisfying customer expectations.
  - quality / definitions
    - quality / definitions / goodness ::@:: design quality, distinctiveness, outcomes, standards
    - quality / definitions / conformance, consistency ::@:: measure of process variability
    - quality / definitions / relativity ::@:: degree of satisfaction, expectation vs. perception
    - quality / definitions / who ::@:: competitors, customers, producers, regulators
  - quality / cost ::@:: cost of good quality, cost of poor quality
    - quality / cost / good quality ::@:: appraisal (e.g. inspection, testing), prevention (e.g. maintenance, training)
    - quality / cost / poor quality ::@:: external (e.g. recall, warranty), hidden (e.g. brand reputation, customer satisfaction, market share), internal (e.g. reworking, scrapping)
      - quality / cost / poor quality / examples ::@:: Boeing having their planes grounded. Tesla recalling their cars. J&J scrapping their COVID-19 vaccines.
- [common cause and special cause](../../../../general/common%20cause%20and%20special%20cause%20(statistics).md) ::@:: two distinct origins of variation in a process, as defined in the statistical thinking and methods of Walter A. Shewhart and W. Edwards Deming
  - common cause and special cause / synonyms ::@:: (former): natural variations, normal variability <br/> (latter): abnormal variability, assignable variations, systematic errors
  - common cause and special cause / common cause (natural variations) ::@:: inherent random errors; cannot be eliminated without changing the process; describable by a pattern or distribution
  - common cause and special cause / special cause (assignable variations) ::@:: discoverable and traceable reason; can be eliminated by operation or management; e.g. machine fault, poor material, unskilled workers
  - common cause and special cause / effect on processes ::@:: (former): process output forms a distribution that is _predictable_ and _stable over time_ <br/> (latter): process output is _unpredictable_ and _unstable over time_
- [statistical process control](../../../../general/statistical%20process%20control.md) ::@:: It is the application of statistical methods to monitor and control the quality of a production process. This helps to ensure that the process operates efficiently, producing more specification-conforming products with less waste scrap.
  - statistical process control / capability analysis ::@:: It analyzes how variation affects process capability, e.g. defect likelihood, outcome specification, etc.
    - statistical process control / capability analysis / tools ::@:: capability index, six-sigma criteria, etc.
  - statistical process control / conformance analysis ::@:: It analyzes if assignable variations exist in a process, e.g. abnormal instances, actions to take, system errors, etc.
    - statistical process control / conformance analysis / tools ::@:: control chart, p-chart, etc.
  - statistical process control / steps ::@:: capability analysis → conformance analysis → cause identification → cause elimination → (repeat)
  - statistical process control / goals ::@:: _capable_: output likely meets design specifications <br/> _in control_/_controllable_: process is consistent and stable over time, i.e. no assignable variations; if _out of control_, take corrective actions
- [engineering tolerance](../../../../general/engineering%20tolerance.md) (specification limits) ::@:: specified by engineering designs; has lower spec limit (LSL) and upper spec limit (USL), and quality is consider _acceptable_ if within this range, otherwise a _defect_
  - engineering tolerance / defective likelihood ::@:: How likely is an output defective? It depends on the _tightness_ of the two limits (wider means less defects) and _variability_ of the outputs (higher means more defects).
- [process capability index](../../../../general/process%20capability%20index.md) ::@:: It is a statistical measure of process capability: the ability of an engineering process to produce an output within specification limits.
  - process capability index / variability ::@:: It can be measured using _standard deviation_. Larger means higher defective likelihood.
  - process capability index / asymmetry ::@:: Sometimes the _mean_ may not lie in the middle of the LSL and USL. We will focus on the narrower side since it is more likely to violate the limit on that side. The idea is to be conservative in quality management. This is why we take the minimum of the two terms in the formula.
  - process capability index / intuition ::@:: How many 3 standard deviations can we fit in between the _smaller_ side of the mean and its corresponding spec limit (LSL/USL)? Obviously, the higher the better.
  - process capability index / formula ::@:: $$C_{\text{pk} } = \min \left[ \frac {\hat \mu - \text{LSL} } {3 \hat \sigma}, \frac {\text{USL} - \hat \mu} {3 \hat \sigma} \right] \,,$$ whee $\hat \mu$ is the _sample_ average and $\hat \sigma$ is the _sample_ standard deviation.
  - process capability index / interpretation ::@:: A higher index means less defective likelihood. <p> Widening the limits leads to a larger index. Decreasing standard deviation can also lead to a larger index.
- \#-sigma quality ::@:: Literally just process capability index multiplied by 3.
  - \#-sigma quality / interpretation ::@:: The number of standard deviations that we can fit in between the _smaller_ side of the mean and its corresponding spec limit (LSL/USL).
  - \#-sigma quality / examples ::@:: 3-sigma quality: C<sub>pk</sub> ≥ 1 <br/> 6-sigma quality: C<sub>pk</sub> ≥ 2
  - 3-sigma quality ::@:: tolerance distance on both sides is at least 3 times of the standard deviation <p> defective likelihood: \< 0.27% or 1 in 370
  - 6-sigma quality ::@:: tolerance distance on both sides is at least 6 times of the standard deviation; likely requires limiting process variability to be viable <p> defective likelihood: 0.000&nbsp;000&nbsp;001&nbsp;973 (no %) or 1 in 506&nbsp;797&nbsp;346
- [Six Sigma](../../../../general/Six%20Sigma.md) ::@:: a set of techniques and tools for process improvement (e.g. manufacturing quality)
  - Six Sigma / brief history ::@:: It was first developed at Motorola in the 1980s. Then it was adopted by 2/3 of Fortune 500 organizations by the late 1990s.
  - Six Sigma / core ideas ::@:: _All_ processes (especially those requiring humans) have variations which is the _main cause_ for quality issues. We can _identify, quantify, and control_ the variations to _effectively_ improve quality.
- \#-sigma quality
  - 6-sigma quality
    - 6-sigma quality / need ::@:: There are industries with very high quality requirements, e.g. cars, jet engines, medicines, vaccines, etc. <p> Further, errors can accumulate. Chaining multiple processes with very low defective likelihoods together can lead to a process with high defective likelihood.
- Six Sigma
  - Six Sigma / defect handling ::@:: rework/bounce-back: requires additional resources that increase workload; requires balancing making things right the first time (which may decrease efficiency) vs. save capacity (by avoiding rework); e.g. early discharge of patients from hospital <br/> scrap/eliminate: output volume uncertainty, waste resources
  - Six Sigma / tools ::@:: (optional in this course) Ishikawa diagram/fishbone diagram, process control chart, etc.
- [Ishikawa diagram](../../../../general/Ishikawa%20diagram.md) ::@:: They are causal diagrams created by Kaoru Ishikawa that show the potential causes of a specific event.
- Six Sigma
  - Six Sigma / process control chart ::@:: Essentially a process flow chart with decisions. Value-added activities are on the left and non-value added activities are on the right.
- statistical process control
  - statistical process control / conformance analysis
  - statistical process control / goals
  - statistical process control / conformance analysis
    - statistical process control / conformance analysis / goals ::@:: Control the process to control the output quality. Make use of control charts and statistics to indicate when to adjust a process.
    - statistical process control / conformance analysis / steps ::@:: create standards (LSL, USL) → measure sample outputs (e.g. mean, range) → take corrective actions if necessary
- [control chart](../../../../general/control%20chart.md) ::@:: They are graphical plots used in production control to determine whether quality and manufacturing processes are being controlled under stable conditions.
  - control chart / idea ::@:: Monitor the variation of outputs to assess process evolution. If the process is indeed stable, the probability of violating the limits is _rare_. So if the limits are violated, then the process is _likely unstable_.
  - control chart / types ::@:: based on variables: continuous variables (e.g. $\bar x$ chart/x-bar chart), discrete/attribute variables (e.g. p-chart) <p> There are other classifications unmentioned here.
- [x̅ and s chart](../../../../general/x̅_and_s_chart.md) ::@:: It is a type of control chart used to monitor the _mean_ and _standard deviation_ of a _normally distributed_ variables data when samples are collected at regular intervals from a business or industrial process.
- [x̅ and R chart](../../../../general/x̅_and_R_chart.md) ::@:: It is a type of scheme, popularly known as control chart, used to monitor the _mean_ and _range_ of a _normally distributed_ variables simultaneously, when samples are collected at regular intervals from a business or industrial process.
- [p-chart](../../../../general/p-chart.md) ::@:: It is a type of control chart used to monitor the _proportion of nonconforming units_ in a sample, where the sample proportion nonconforming is defined as the ratio of the number of nonconforming units to the sample size, _n_.

## week 5 lecture

- datetime: 2025-03-03T10:30:00+08:00/2025-03-03T11:50:00+08:00
- topic: quality management, conformance analysis, acceptance sampling
- statistical process control
  - statistical process control / conformance analysis
    - statistical process control / conformance analysis / goals
    - statistical process control / conformance analysis / steps
- control chart
  - control chart / idea
  - control chart / types
- [continuous or discrete variable](../../../../general/continuous%20or%20discrete%20variable.md) ::@:: a quantitative variable may be __continuous__ or __discrete__ if it is typically obtained by _measuring_ or _counting_, respectively
  - continuous variable ::@:: can be measured continuously
    - continuous variable / examples ::@:: length, speed, temperature, weight, width
- x̅ and R chart
  - x̅ and R chart / data ::@:: Take a series of samples over _time_. Each sample is taken on a small group (fixed size _n_) of products.
  - x̅ and R chart / method ::@:: For each sample, compute mean $\overline x$ and range $R$. Then across all samples, compute mean of mean $\overline {\overline x}$ and mean of range $\overline R$. Compute _control_ \(not _specification_\) limits by multiplying the mean of range $\overline R$ by $A_2$ that is obtained given $n$.
  - x̅ and R chart / center line ::@:: $${\bar {\bar {x} } }={\frac {\sum _{i=1}^{m}\sum _{j=1}^{n}x_{ij} }{mn} }$$
  - x̅ and R chart / control limits ::@:: $${\bar {\bar {x} } }\pm A_{2}{\bar {R} }$$
  - x̅ and R chart / plotted statistic ::@:: $${\bar {x} }_{i}={\frac {\sum _{j=1}^{n}x_{j} }{n} }$$
  - x̅ and R chart / sample size-specific anti-biasing constants ::@:: _A_<sub>2</sub> controls the width of lower and upper control limits \(LCL/UCL\). The larger the sample size _n_, the smaller _A_<sub>2</sub>, because less variation in the sample mean should be expected. <p> You do not need to compute this. A table will be provided.
  - x̅ and R chart / plot ::@:: Plot the center line, control limits, and the data points for the plotted statistic. Optionally, join the data points.
- statistical process control
  - statistical process control / conformance analysis
    - statistical process control / conformance analysis / control limits ::@:: used to tell if a process is _in-control_, computed from _samples_
      - statistical process control / conformance analysis / control limits / vs. specification limits ::@:: determine if a process is _in-control_ vs. determine if a product is _defective_ <br/> computed from _samples_ vs. explicitly _specified_ beforehand
  - statistical process control / conformance analysis / anomalies ::@:: long runs \(≥7) of consecutive points going up or down, long runs \(≥7\) of consecutive points on one side of the center line, points falling outside the control limits
- continuous or discrete variable
  - discrete variable ::@:: can be obtained by _counting_; binary: two possible values
    - discrete variable / examples ::@:: defective or non-defective, good or bad, yes or no
- p-chart
  - p-chart / data ::@:: Take a series of samples over _time_. Each sample is taken on a small group (fixed size _n_) of products. The attribute should be binary, e.g. defectiveness.
  - p-chart / method ::@:: For each sample, compute fraction of defects $p$. Then across all samples, compute mean of fraction of defects $\overline p$. Compute _control_ \(not _specification_\) limits by multiplying the standard deviation of $\overline p$ by 3.
  - p-chart / center line ::@:: $${\bar {p} }={\frac {\sum _{i=1}^{m}\sum _{j=1}^{n}{\begin{cases}1&{\text{if } }x_{ij}{\text{ defective} }\\0&{\text{otherwise} }\end{cases} } }{mn} }$$
  - p-chart / control limits ::@:: $${\bar {p} }\pm 3{\sqrt {\frac { {\bar {p} }(1-{\bar {p} })}{n} } }$$ <p> \(__Important__: In this course, the lower control limit should be _at least 0_.\)
  - p-chart / plotted statistic $${\bar {p} }_{i}={\frac {\sum _{j=1}^{n}{\begin{cases}1&{\text{if } }x_{ij}{\text{ defective} }\\0&{\text{otherwise} }\end{cases} } }{n} }$$
  - p-chart / plot ::@:: Plot the center line, control limits, and the data points for the plotted statistic. Optionally, join the data points.
- [_kaizen_](../../../../general/kaizen.md) \(改善, "improvement"\) ::@:: a concept referring to business activities that continuously improve all functions and involve all employees
  - _kaizen_ / control chart ::@:: from out-of-control (has anomalies), to in-control (no anomalies), to improvements (narrower control limits)
- [acceptance sampling](../../../../general/acceptance%20sampling.md) ::@:: It uses statistical sampling to determine whether to accept or reject a production lot of material.
  - acceptance sampling / decision rule ::@:: For a lot, specify the sample size _n_ and acceptance number _c_. Find the number of defectives _d_. If _d_ ≤ _c_, _accept_ the lot. Otherwise, _reject_ and _follow up_: perform full inspection, return lot, etc.
  - acceptance sampling / model ::@:: In a lot, there are _N_ (population size) items with _P_ (_true_ population defective rate) of them being defective. We sample _n_ (sample size) size and find its _p_ (_estimated_ sample defective rate). <p> We want to _estimate_ _P_ using _p_, while ensuring _N_ ≫ _n_.
  - acceptance sampling / conditions ::@:: In general, it is employed when one or several of the following hold: <p> testing is destructive; <br/> the cost of 100% inspection is very high; and <br/> 100% inspection takes too long.
  - acceptance sampling / trade-off ::@:: cost of sampling vs. risk of wrong decision
  - acceptance sampling / wrong decisions ::@:: rejected "good" lot: Type I error with probability $\alpha$ \(typically 5%\), false positive/rejection, _producer's risk_ <br/> accepted "bad" lot: Type II error with probability $\beta$ \(typically 10%\), false negative/acceptance, _consumer's risk_
- [acceptable quality limit](../../../../general/acceptable%20quality%20limit.md) \(AQL\) ::@:: Maximum _true_ defective rate for producers. A lot is acceptable or "good" if _P_ ≤ AQL.
- [lot tolerance percent defective](../../../../general/lot%20tolerance%20percent%20defective.md) \(LTPD\) ::@:: Maximum _true_ defective rate for consumers. A lot is unacceptable or "bad" if _P_ \> LTPD.
- acceptance sampling
  - acceptance sampling / wrong decisions
    - acceptance sampling / wrong decisions / neither "good" nor "bad" ::@:: If the _true_ defective rate for a lot is AQL \< _P_ ≤ LTPD, then it is neither "good" nor "bad". Accept or reject are both "correct" decisions, i.e. neither Type I error nor Type II error.
  - acceptance sampling / sampling plan ::@:: Given maximum Type I error rate $\alpha$, maximum Type II error rate $\beta$, AQL, and LTPD; solve for sample size \(_not_ lot size\) _n_ and acceptance number _c_, represented as a tuple \(_n_, _c_\).
    - acceptance sampling / sampling plan / table ::@:: Fixed parameters are maximum Type I error rate _α_ nd maximum Type II error rate _β_. The table has 3 columns: _c_ \(starting from 0\), LTPD÷AQL, n×AQL.
      - acceptance sampling / sampling plan / table / use ::@:: Find the table for fixed maximum Type I error rate _α_ and maximum Type II error rate _β_. <p> acceptance number _c_: Calculate LTPD÷AQL, and find the _largest integer_ _c_ that has a value _at least_ the calculated LTPD÷AQL. This is the _c_. <br/> sample size \(_not_ lot size\) _n_: Use n×AQL of the found _c_. Find the _smallest integer_ _n_ such that n×AQL has a value of _at least_ that of the found _c_. Equivalently, divide n×AQL by AQL, and round up to the nearest integer.
  - acceptance sampling / operating characteristic curve (OC curve) ::@:: \(optional\) The probability of acceptance given \(_n_, _c_\) is plotted on the _y_-axis, against the _true_ population defective rate plotted on the _x_-axis. _α_ and _β_ are indicated on the _y_-axis. AQL and LTPD are indicated on the _x_-axis.
    - acceptance sampling / operating characteristic curve / _α_, _β_, AQL, LTPD ::@:: Type I error rate _α_ is the distance of the graph value from 100% at AQL. Type II error rate _β_ is the graph value at LTPD.
    - acceptance sampling / operating characteristic curve / ideal curve ::@:: The ideal curve is 100% acceptance probability for true defective rate from 0 to AQL, and then 0% forever thereafter.

## week 5 lecture 2

- datetime: 2025-03-05T10:30:00+08:00/2025-03-05T11:50:00+08:00
- topic: capacity planning, decision tree method and EVPI
- [lean manufacturing](../../../../general/lean%20manufacturing.md) ::@:: It is a method of manufacturing goods aimed primarily at reducing times within the production system as well as response times from suppliers and customers. It is closely related to another concept called __just-in-time manufacturing__ (JIT manufacturing in short).
  - just-in-time manufacturing ::@:: \(optional\) Using production flow management and quality improvement to match supply with demand.
    - just-in-time manufacturing / brief history ::@:: It was pioneered by Toyota in the 1980s. Later it was adopted by many famous manufacturers globally.
- [capacity planning](../../../../general/capacity%20planning.md) ::@:: It is the process of determining the production capacity needed by an organization to meet changing demands for its products.
  - capacity planning / capacity ::@:: It is the amount of output that a system can achieve over a specific period of time.
  - capacity planning / levels ::@:: operational \(e.g. assignment, control, planning\), strategic \(e.g. fixed assets investments\), tactical \(e.g. human resources, minor investments\)
- [economies of scale](../../../../general/economies%20of%20scale.md) ::@:: When output increases, average unit cost (LRATC) falls.
- [diseconomies of scale](../../../../general/diseconomies%20of%20scale.md) ::@:: When output increases, average unit cost (LRATC) rises.
- [minimum efficient scale](../../../../general/minimum%20efficient%20scale.md) ::@:: Output level with minimum average unit cost (LRATC).
  - minimum efficient scale / aliases ::@:: best operating level
- capacity planning
  - capacity planning / uncertainty ::@:: In the real world, this comes in and affects demand, extreme events, production, supply, etc. <p> This makes capacity planning challenging, especially strategic planning in the _long term_.
  - capacity planning / steps ::@:: specify _objectives_, find _alternatives_ in each step, analyze and compare, select the best alternative, implement and monitor
- [decision tree](../../../../general/decision%20tree.md) ::@:: It is a decision support recursive partitioning structure that uses a tree-like model of decisions and their possible consequences, including chance event outcomes, resource costs, and utility.
  - decision tree / conditions ::@:: It cannot model any _arbitrary_ uncertainty. We need to know the possible random _scenarios_ and their _probabilities_, possible _actions_, and _payoffs_.
  - decision tree / construction ::@:: We assume each _period_ has a decision, and then a random scenario. After a period, there may or may not be more periods after it. <p> Then your decision tree is listing all possible _actions_, and then for each action, listing all possible _scenarios_. Repeat until all periods have been exhausted. Finally, write the _payoffs_ at the tree ends (leaves).
    - decision tree / construction / decision point ::@:: Represented by a square. Followed by alternative _decisions_ and their _expected values_ (either _given_ or computed backwardly via _backward induction_).
    - decision tree / construction / event point ::@:: Represented by a circle. Followed by possible random _scenarios_ and their _probabilities_.
  - decision tree / expected value ::@:: Consider a _period_. The expected payoff of an action is the weighted sum of the payoffs of its random _scenarios_ given the action, weighted by the scenario _probabilities_. <p> Since we choose the action with the best payoff, the _expected value of the whole tree_ is the payoff of the best action. <p> For multiple periods, use _backward induction_ as described below.
    - decision tree / expected value / note ::@:: In practice, we also need to consider the decision _risk_, not just the expected payoff.
  - decision tree / solution ::@:: Use _backward induction_ to find the _optimal_ action. <p> Start from the _last period_, and find the expected payoffs of all _actions_. Propagate the expected payoff of the _best_ action as the payoff of the corresponding random scenario of the previous period. Repeat until you have reached the _first period_. The action in the first period with the highest payoff is the _optimal_ action _right now_, and is also the _expected value_.
- [backward induction](../../../../general/backward%20induction.md) ::@:: It is the process of determining a sequence of optimal choices by reasoning from the endpoint of a problem or situation back to its beginning using individual events or actions.
- [expected value of perfect information](expected%20value%20of%20perfect%20information.md) \(EVPI\) ::@:: It is the price that one would be willing to pay in order to gain access to perfect information.
  - expected value of perfect information / idea ::@:: The scenarios are still _random_, but you can know them _before_ making the decision.
  - expected value of perfect information / equation ::@:: \(expected\) value _of_ perfect information = expected value _under_ perfect information − expected value \(_without_ perfect information\)
  - expected value of perfect information / expected value _under_ perfect information ::@:: _List_ all scenarios. If there are multiple periods, combinations of all scenarios across periods. Compute their _probabilities_, either given, or calculated if across periods. <p> Then, for each combination of scenarios, compute the expected value of the decision tree again, but the random scenarios are fixed by the combination. <p> Finally, _sum_ the above expected values _weighted_ by their probabilities, and this is the expected value _under_ perfect information.
- decision tree
  - decision tree / summary ::@:: Information about the future is valuable (actually information in general is valuable). Thus it is desirable to reduce uncertainty as soon as possible.
  - decision tree / summary / uncertainty reduction ::@:: data analytics, demand forecasting, feasibility study, market research, etc.

## week 6 lecture

- datetime: 2025-03-10T10:30:00+08:00/2025-03-10T11:50:00+08:00
- topic: capacity planning, resource allocation, linear programming techniques
- [linear programming](../../../../general/linear%20programming.md) ::@:: It is a method to achieve the best outcome \(such as maximum profit or lowest cost\) in a [mathematical model](../../../../general/mathematical%20model.md) whose requirements and objective are represented by [linear relationships](../../../../general/linear%20function.md#as%20a%20polynomial%20function). Linear programming is a special case of mathematical programming \(also known as [mathematical optimization](../../../../general/mathematical%20optimization.md)\).
  - linear programming / examples ::@:: You have several types of resources, each limited in number. You have several types of goods to produce, each with different price and requiring different resources. You want to maximize sales. <p> This assumes each type of good always take a constant amount of resources, so that the resource constraints \(constraints\) are _linear_ functions. This also assumes each type of good has a constant price, so that the sales \(objective function\) is also a _linear_ function. <p> In this case, you can use linear programming to maximize sales.
  - linear programming / standard form ::@:: It is the usual and most intuitive form of describing a linear programming problem. It consists of the following three parts: <p> - A __linear \(or affine\) function to be maximized__ <br/> &emsp; e.g. $f(x_{1},x_{2})=c_{1}x_{1}+c_{2}x_{2}$ <br/> - __Problem constraints__ of the following form <br/> &emsp; e.g. ${\begin{matrix}a_{11}x_{1}+a_{12}x_{2}&\leq b_{1}\\a_{21}x_{1}+a_{22}x_{2}&\leq b_{2}\\a_{31}x_{1}+a_{32}x_{2}&\leq b_{3}\\\end{matrix} }$ <br/> - __Non-negative variables__ <br/> &emsp; e.g. ${\begin{matrix}x_{1}\geq 0\\x_{2}\geq 0\end{matrix} }$
- [feasible region](../../../../general/feasible%20region.md) ::@:: It is the set of all possible points (sets of values of the choice variables) of an optimization problem that satisfy the problem's constraints, potentially including inequalities, equalities, and integer constraints.
  - feasible region / linear programming ::@:: If a solution satisfies all _problem constraints_ and _non-negative variables constraints_, then it is in the __feasible region__, and is a _feasible solution_. Otherwise, it is an _infeasible solution_.
- linear programming
  - linear programming / optimal solution ::@:: Assuming the feasible region exists and is bounded. Then an optimal solution exist \(there can be multiple optimal solutions\). An optimal solution is a solution in the feasible region that achieves the _maximum_ possible objective value. <p> For a _minimization_ problem, such a solution achieves the _minimum_ possible objective value instead.
  - linear programming / optimal objective value ::@:: This is the value of the objective function at the _optimal solution_.
- [linear function](../../../../general/linear%20function%20(calculus).md) ::@:: It from the real numbers to the real numbers is a function whose graph (in Cartesian coordinates) is a non-vertical line in the plane. The characteristic property of linear functions is that when the input variable is changed, the change in the output is proportional to the change in the input.
  - linear function / form ::@:: It is a [polynomial function](../../../../general/polynomial%20function.md#polynomial%20functions) in which the [variable](../../../../general/variable%20(mathematics).md) _x_ has degree at most one: $$f(x)=ax+b \,.$$
- linear programming
  - linear programming / linearity ::@:: Both the object function and constraints need to be _linear_ with respect to the variables. A _linear function_ means each variable appears in a separate term raised to the 1st power and multiplied by a constant \(could be 0\).
    - linear programming / linearity / constraints ::@:: They are _linear functions_ that are either ≥, ≤, or = to a constant \(could be 0\). <p> Note that some seemingly nonlinear constraints can be transformed into linear constraints, e.g. A/B≥2 becoming A–2B≥0 \(given B ≥ 0\), A=B becoming A–B=0, etc.
- [constraint](constraint%20(mathematics).md) ::@:: It is a condition of an optimization problem that the solution must satisfy.
  - constraint / binding ::@:: If an inequality constraint holds with _equality_ at the optimal point, the constraint is said to be __binding__, as the point _cannot_ be varied in the direction of the constraint even though doing so would improve the value of the objective function.
  - constraint / non-binding ::@:: If an inequality constraint holds as a _strict inequality_ at the optimal point \(that is, does not hold with equality\), the constraint is said to be __non-binding__, as the point _could_ be varied in the direction of the constraint, although it would not be optimal to do so.
    - constraint / non-binding / slack ::@:: It is obtained by subtracting the right hand side of the inequality by the left hand side. It can be interpreted as the amount of resources left over. <p> It is zero for binding constraints, and positive for non-binding constraints.
- linear programming
  - linear programming / formulation ::@:: Define the variables. Write the objective in terms of the decision. Write the constraints and non-negativity constraints in terms of the variables \(i.e. availability, non-negativity\). _Importantly_, ensure the objective function and the constraints are _linear_.
  - linear programming / applications ::@:: blend, investment strategies, production planning, product mix, transport
  - linear programming / solving ::@:: graphical method \(max 2 variables\), Excel solver \(underlying algorithms are unmentioned here\)
    - linear programming / solving / graphical method ::@:: Assume you have 2 variables. Graph the constraints and non-negativity constraints. Color the feasible region. Draw an _iso-cost_/_iso-profit_ line \(through the origin, if you need help finding a starting point\). An iso-cost/iso-profit line represents the solutions \(regardless of its feasibility\) that give the same objective value. Examine the iso-cost/iso-profit line "pushed" to each corner \(vertex\) of the feasible region. The vertex for which the line is the farthest away from the origin is an optimal solution.
      - linear programming / solving / graphical method / binding ::@:: Constraints that cross an optimal solution point are the binding constraints. The rest are non-binding constraints

## week 6 lecture 2

- datetime: 2025-03-12T10:30:00+08:00/2025-03-12T11:50:00+08:00
- topic: capacity planning, resource allocation, linear programming techniques
- [shadow price](../../../../general/shadow%20price.md) ::@:: It is the monetary value assigned to an abstract or intangible commodity which is not traded in the marketplace. This often takes the form of an externality.
  - shadow price / constrained optimization ::@:: In [constrained optimization](../../../../general/constrained%20optimization.md) in [economics](../../../../general/economics.md), the shadow price is the change, per [infinitesimal](../../../../general/infinitesimal.md) unit of the constraint, in the optimal value of the objective function of an [optimization problem](../../../../general/optimization%20problem.md) obtained by relaxing the [constraint](../../../../general/constraint%20(mathematics).md). If the objective function is [utility](../../../../general/utility.md), it is the [marginal utility](../../../../general/marginal%20utility.md) of relaxing the constraint. If the objective function is [cost](../../../../general/cost.md), it is the [marginal cost](../../../../general/marginal%20cost.md) of strengthening the constraint.
    - shadow price / constrained optimization / complementary slackness ::@:: shadow price × slack = 0, i.e. cannot be both positive. <p> This shows that non-binding constraints must have zero shadow prices. Binding constraints may have zero or nonzero shadow prices.
- Excel Solver Function ::@:: A nonlinear solver adjusted to spreadsheets in which function evaluations are based on the recalculating cells. Basic version available as a standard add-on for Excel.
  - Excel Solver Function / steps ::@:: Write the linear program in a spreadsheet in a fancy format. Specify solver parameters, e.g. constraints, objective function, variables. Use "simplex LP" as the solving method. Solve. Select "Answer" and "Sensitivity" to generate two extra reports as two spreadsheets.
  - Excel Solver Function / note ::@:: In sensitivity analysis, you may see "1E+30". Treat it as infinity.
- [sensitivity analysis](../../../../general/sensitivity%20analysis.md) ::@:: It is the study of how the uncertainty in the output of a mathematical model or system (numerical or otherwise) can be divided and allocated to different sources of uncertainty in its inputs. This involves estimating sensitivity indices that quantify the influence of an input or group of inputs on the output.
  - sensitivity analysis / motivation ::@:: How will the LP optimal solution and its value change in uncertainty, e.g. contract impact, true economic value of resources, etc.? This can help ensure the robustness of the production plan.
- linear programming
  - linear programming / sensitivity analysis ::@:: For each change, there is an _allowable increase_ and _allowable decrease_, forming the _allowable range_. Their interpretation depends of the type of change. We will consider 2 types of changes. <p> Here, exactly one type of change is considered. That is, we do not consider changing coefficients and inequality RHS at the same time.
    - linear programming / sensitivity analysis / types ::@:: change in objective function coefficients \(e.g. profits\), change in inequality right hand side (e.g. resource amount)
    - linear programming / sensitivity analysis / objective function coefficients ::@:: If the new coefficient is within the _allowable range_, an currently optimal solution _remains an optimal solution_. However, the _optimal objective value_ will _change_, and will need to be _recalculated_ using the new objective function.
    - linear programming / sensitivity analysis / inequality right hand side ::@:: Excel Solver Function also shows the shadow price. <p> If the new right hand side \(e.g. resource amount\) is within the _allowable range_ \(note that it is calculated from the inequality right hand side, _not_ from an optimal solution\), then the shadow price remains unchanged. The _change in the optimal objective value_ is calculated as the shadow price × change in RHS \(do not forget its sign\). The new _optimal solution_ can be _recalculated_.
    - linear programming / sensitivity analysis / example ::@:: For example, we want to price a new product. The new product requires a variable cost \(independent of the limited resources\) and some types of limited resources. The opportunity cost of the product \(i.e. minimum price to prevent loss compared to the current optimal solution\) is obtained by adding the variable cost and the amount of limited resources per unit of new product multiplied by its shadow price for each type of limited resource.
  - linear programming / brief history ::@:: A discipline from the 1940s. Some methods include: simplex method \(1947\), interior method \(1984\), etc.
  - linear programming / versatility ::@:: It is a simple but powerful model that is flexible \(e.g. sensitivity analysis\), has a wide range of applications, and has solvers in many applications \(e.g. Excel\) and programming languages \(e.g. MATLAB, Python\).

## midterm examination

## final examination

## aftermath

### total
