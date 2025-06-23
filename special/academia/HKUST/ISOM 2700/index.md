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
    - participation \(5 of 7\): 0.05
      - iPRS
      - no participation in the first 2 weeks
    - homework (2): 0.1
      - due at Sunday 23:59
      - no late submission
    - online quizzes \(best 3 of 4\): 0.15
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

- [assignments](assignments/index.md)
- [questions](questions/index.md)

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
- operations management
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
- status: attendance
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
- [questions § week 3 lecture 2](questions/index.md#week%203%20lecture%202)

## week 4 lecture

- datetime: 2025-02-24T10:30:00+08:00/2025-02-24T11:50:00+08:00
- topic: queueing system, simulation method
- M/M/1 queue
- M/M/c queue
- [G/G/1 queue](../../../../general/G_G_1%20queue.md) ::@:: G/G/1: _general_ (unknown distribution) inter-arrival time/_general_ (unknown distribution) service time/1 server; assume one FIFO (first-in first-out)/FCFS (first-come first-serve) queue
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
- status: attendance
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
- [questions § week 5 lecture 2](questions/index.md#week%205%20lecture%202)

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
    - linear programming / solving / graphical method ::@:: Assume you have 2 variables. Graph the constraints and non-negativity constraints. Color the feasible region. <p> Draw an _iso-cost_/_iso-profit_ line \(through the origin, if you need help finding a starting point\). An iso-cost/iso-profit line represents the solutions \(regardless of its feasibility\) that give the same objective value. <p> Examine the iso-cost/iso-profit line "pushed" \(keeping the slope\) to each corner \(vertex\) of the feasible region. The vertex for which the line has the maximum/minimum objective value is an optimal solution.
      - linear programming / solving / graphical method / binding ::@:: Constraints that cross an optimal solution point are the binding constraints. The rest are non-binding constraints.

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
  - linear programming / sensitivity analysis ::@:: For each change, there is an _allowable increase_ and _allowable decrease_, forming the _allowable range_. Their interpretation depends of the type of change. We will consider 2 types of changes. <p> Here, exactly one change is considered. That is, we do not consider changing coefficients and inequality RHS at the same time, or changing multiple coefficients or multiple inequality RHS at the same time.
    - linear programming / sensitivity analysis / types ::@:: change in objective function coefficients \(e.g. profits\), change in inequality right hand side (e.g. resource amount)
    - linear programming / sensitivity analysis / objective function coefficients ::@:: If the new coefficient is within the _allowable range_, an currently optimal solution _remains an optimal solution_. However, the _optimal objective value_ will _change_, and will need to be _recalculated_ using the new objective function. <p> __caution__: This _allowable range_ is valid only if exactly one coefficient changes.
    - linear programming / sensitivity analysis / inequality right hand side ::@:: Excel Solver Function also shows the shadow price. <p> If the new right hand side \(e.g. resource amount\) is within the _allowable range_ \(note that it is calculated from the inequality right hand side, _not_ from an optimal solution\), then the shadow price remains unchanged. The _change in the optimal objective value_ is calculated as the shadow price × change in RHS \(do not forget its sign\). The new _optimal solution_ can be _recalculated_. <p> __caution__: This _allowable range_ is valid only if exactly one coefficient changes.
    - linear programming / sensitivity analysis / example ::@:: For example, we want to price a new product. The new product requires a variable cost \(independent of the limited resources\) and some types of limited resources. The opportunity cost of the product \(i.e. minimum price to prevent loss compared to the current optimal solution\) is obtained by adding the variable cost and the amount of limited resources per unit of new product multiplied by its shadow price for each type of limited resource.
  - linear programming / brief history ::@:: A discipline from the 1940s. Some methods include: simplex method \(1947\), interior method \(1984\), etc.
  - linear programming / versatility ::@:: It is a simple but powerful model that is flexible \(e.g. sensitivity analysis\), has a wide range of applications, and has solvers in many applications \(e.g. Excel\) and programming languages \(e.g. MATLAB, Python\).

## week 7 lecture

- datetime: 2025-03-17T10:30:00+08:00/2025-03-17T11:50:00+08:00, PT1H20M
- topic: midterm examination review
- status: attendance
- [§ midterm examination](#midterm%20examination)
- [questions § week 7 lecture](questions/index.md#week%207%20lecture)

## week 7 lecture 2

- datetime: 2025-03-19T10:30:00+08:00/2025-03-19T11:50:00+08:00, PT1H20M
- status: unscheduled

> Note that we do <span style="color: red;">NOT</span> have class on this Wednesday \(Mar 19<sup>th</sup>\) and next Monday \(Mar 24<sup>th</sup>\)

## midterm examination

- datetime: 2025-03-21T20:00:00+08:00/2025-03-21T21:40:00+08:00, PT1H40M
- venue: Lecture Theater A, Academic Building; Lecture Theater J, Academic Building
- format
  - calculator: yes
  - cheatsheet: A4-sized, double-sided
  - referencing: closed book
  - provided: formulas, necessary tables
  - questions: multiple choice questions ×40
- grades: 38/40 → 38/40
  - statistics
    - timestamps: 2025-03-26T20:34:00+08:00 → 2025-04-11+08:00
    - mean: ? \(provided: 29.5\) → ?
    - standard deviation: ? \(provided: 7.1\) → ?
    - low: ? → ?
    - lower quartile: ? → ?
    - median: ? \(provided: 30\) → ?
    - upper quartile: ? \(provided: 35\) → ?
    - high: ? → ?
    - distribution: ? → ?
- report
  - "careless" mistake \(–1\) ::@:: Somehow the activity with the highest capacity \(lowest utilization\) instead of the highest utilization is found instead...
  - capable vs. in control \(–1\) ::@:: Process capability is about meeting specifications, while process control is about not having assignable variations.
- check
  - datetime
    - 2025-04-09T14:30:00+08:00/2025-04-09T17:00:00+08:00, PT2H30M
    - 2025-04-10T10:00:00+08:00/2025-04-10T12:10:00+08:00, PT2H10M
  - venue: Room 4083, LSKBB
  - report: \(none\)

## week 8 lecture

- datetime: 2025-03-24T10:30:00+08:00/2025-03-24T11:50:00+08:00, PT1H20M
- status: unscheduled

> Dear Class,
>
> It is nice to see you today. Thank you for coming to the midterm exam. I hope you don't find the questions too stressful.
>
> Please note that we do NOT have class on next Monday \(March 24th\). The class will continue from next Wednesday \(March 26th\). So I will see you again on Wednesday.
>
> Have some good rest during the weekend! Wish you best luck with your remaining exams. Feel free to let me know if you have any questions.
>
> Best regards,
>
> \[redacted\]

## week 8 lecture 2

- datetime: 2025-03-26T10:30:00+08:00/2025-03-26T11:50:00+08:00, PT1H20M
- topic: forecasting: qualitative and qualitative approaches, time series forecasting models
- [demand forecasting](../../../../general/demand%20forecasting.md) ::@:: It involves the prediction of the quantity of goods and services that will be demanded by consumers or business customers at a future point in time.
  - demand forecasting / use ::@:: capacity planning, inventory management, revenue optimization, supply chain management, etc.
  - demand forecasting / types ::@:: dependent demand: derived from other products or services <br/> independent demand: final customer demand, not derivable from other products or services
- [forecasting](../../../../general/forecasting.md) ::@:: It is the process of making predictions based on past and present data. Later these can be compared with what actually happens.
  - forecasting / types ::@:: tactical \(short-term\) vs. strategic \(long-term\) <br/> qualitative \(subjective\) vs. quantitative \(objective\)
  - forecasting / principles ::@:: data: aggregate forecasts are usually more accurate <br/> error: has errors, never perfect <br/> uncertainty: the longer the time horizon, the more uncertain <br/> use: balance business acumen and quantitative analysis
  - forecasting / methods ::@:: consensus building, forecast combination, market research, prediction markets
  - forecasting / biases ::@:: behavioral bias may arise, e.g. anchoring, group thinking, overconfidence, etc.
- [time series](../../../../general/time%20series.md) ::@:: It is a series of data points indexed (or listed or graphed) in time order. Most commonly, a time series is a sequence taken at successive equally spaced points in time. Thus it is a sequence of discrete-time data.
  - time series / forecasting ::@:: A form of _extrapolation_ in time: It assumes data in the past is useful for the future, i.e. old patterns continue in the future. Thus, it could not respond to breakthroughs or emerging new trends.
  - time series / components ::@:: random variation, seasonality, trend \(shrink/grow\)
  - time series / forecasting
    - time series / forecasting / issues ::@:: autocorrelation, noise control/reduction, seasonality modeling \(e.g. seasonality index\), structural break, trend modeling \(e.g. double exponential smoothing\), etc.
    - time series / forecasting / tradeoffs ::@:: responsiveness \(capture recent changes by relying more on recent data\) vs. robustness/stability \(smoothing to reduce noise\)
- [moving average](../../../../general/moving%20average.md) ::@:: It is a calculation to analyze data points by creating a series of averages of different selections of the full data set.
  - moving average / types ::@:: naive, simple, weighted, exponential, etc.
  - moving average / naive ::@:: $$F_t = A_{t - 1} \,,$$ i.e. take the last value as the prediction. It is highly sensitive to noise and does not account for trends.
  - moving average / simple ::@:: $$F_t = \frac 1 n (A_{t - 1} + \cdots + A_{t - n}) \,,$$ i.e. take the average of the last _n_ values as the prediction. _n_ is the sampling/look-back window.
  - moving average / sampling window ::@:: The sampling/look-back window is specified by a number _n_. <p> Larger values smooth out noise \(_robustness_/_stability_\), while smaller values is more _responsive_.
  - moving average / weighted ::@:: $$F_t = w_1 A_{t - 1} + \cdots + w_n A_{t - n} \,,$$ where the _n_ weights $w_i$ sum up to 1. <p> Simple moving average is a special case where $w_i = 1 / n$ for all _i_.
    - moving average / weighted / weights ::@:: The weights may be selected by trial and error. <p> A reasonable assignment is allocating more weight to recent data. This increases _responsiveness_ against _robustness_/_stability_.
  - moving average / simple
    - moving average / simple / advantages & disadvantages ::@:: It is based on average past demand, and assigns equal importance to each observation. <p> It requires carrying large amounts of historical data, and data before the sampling window are entirely ignored.
  - moving average / weighted
    - moving average / weighted / advantages & disadvantages ::@:: It is based on average past demand, and usually assigns more importance to recent data. <p> It requires carrying large amounts of historical data, and data before the sampling window are entirely ignored.
  - moving average / exponential ::@:: $$F_t = F_{t - 1} + \alpha(A_{t - 1} - F_{t - 1}) = \alpha A_{t - 1} + (1 - \alpha) F_{t - 1} \,,$$ where $\alpha$ is the alpha smoothing constant, where higher values increase _responsiveness_ against _robustness_/_stability_. <p> It only requires the most recent observation and the most recent forecast.
    - moving average / exponential / intuition ::@:: New forecast revises the old forecast in the direction of the actual observation by $\alpha$. <p> Higher $\alpha$ makes the forecast move more. When $\alpha = 0$, this means using the old forecast only. When $\alpha = 1$, this means using the new observation only \(same as the naive model\).
- [forecast error](../../../../general/forecast%20error.md) ::@:: It is the difference between the actual or real and the predicted or forecast value of a time series or any other phenomenon of interest.
  - forecast error / calculation ::@:: $$\text{error}_t = \text{observation}_t - \text{forecast}_t \,.$$ Remember that the observation comes before the forecast in the formula.
- [mean absolute error](../../../../general/mean%20absolute%20error.md) \(MAE\) ::@:: It is a measure of errors between paired observations expressing the same phenomenon. <p> MAE is calculated as the __sum of absolute errors__ \(i.e., the [Manhattan distance](../../../../general/Manhattan%20distance.md)\) divided by the [sample size](../../../../general/sample%20size.md): $$\mathrm {MAE} ={\frac {\sum _{i=1}^{n}\left|y_{i}-x_{i}\right|}{n} }={\frac {\sum _{i=1}^{n}\left|e_{i}\right|}{n} }.$$ It is thus an arithmetic average of the absolute errors $|e_{i}|=|y_{i}-x_{i}|$, where $y_{i}$ is the prediction and $x_{i}$ the true value.
  - mean absolute error / note ::@:: \(__this course__: It is called _mean absolute deviation_ \(_MAD_\) instead...? It seems like misnomer, since _deviation_ compares the observation with the _observation mean_ rather than the _predictions_.\)
- [tracking signal](../../../../general/tracking%20signal.md) \(TS\) ::@:: It monitors any forecasts that have been made in comparison with actuals, and warns when there are unexpected departures of the outcomes from the forecasts.
  - tracking signal / definition ::@:: The formula for this tracking signal is: $${\text{Tracking signal} }={\frac {\Sigma (a_{t}-f_{t})}{\text{MAD} } }$$ where _a<sub>t</sub>_ is the actual value of the quantity being forecast, and _f<sub>t</sub>_ is the forecast. MAD is the [mean absolute deviation](../../../../general/mean%20absolute%20deviation.md). The formula for the MAD is: $${\text{MAD} }={\frac {\Sigma \left|a_{t}-f_{t}\right|}{n} }$$ where _n_ is the number of periods.
    - tracking signal / definition / full ::@:: The entire formula for tracking signal is: $${\text{Tracking signal} }={\frac {\Sigma (a_{t}-f_{t})}{ {\frac {1}{n} }\Sigma \left|a_{t}-f_{t}\right|} } \,.$$
- mean absolute error
  - mean absolute error / measure ::@:: It accounts for both overshooting and undershooting of the observations. It measures the average deviation from true value.
- tracking signal
  - tracking signal / measure ::@:: It accounts for _cumulative_ errors over time. It shows how consistently the observations overshoots or undershoots the predictions. A positive tracking signal means the observations mostly overshoot the predictions, and vice versa for negative.
    - tracking signal / measure / warn ::@:: It can warn when there are unexpected deviations from the prediction, similar to that in _control charts_. In general, $$\lvert TS \rvert > 3.75$$ implies the prediction is poor.
  - tracking signal / vs. mean absolute error ::@:: They are different accuracy measures. Better performance in one measure does _not_ imply better performance in the other.

## week 9 lecture

- datetime: 2025-03-31T10:30:00+08:00/2025-03-31T11:50:00+08:00, PT1H20M
- topic: inventory management: introduction to inventory management, economic order quantity \(EOQ\) model
- inventory
  - inventory / types ::@:: raw materials, work-in-progress, finished goods, supplies, etc.
- [field inventory management](../../../../general/field%20inventory%20management.md) ::@:: It is the task of understanding the stock mix of a company and the handling of the different demands placed on that stock. The demands are influenced by both external and internal factors and are balanced by the creation of purchase order requests to keep supplies at a reasonable or prescribed level.
  - field inventory management / goal ::@:: match \(inventory\) supply with demand
  - field inventory management / importance ::@:: convergence point of supply chain and customer touch-point <br/> inventory can be the largest asset of a firm <br/> multiple stakeholders involved
  - field inventory management / components ::@:: inventory tracking, order management, purchasing, reporting and analysis, shipping and delivery, transfer management, etc.
    - field inventory management / components / new ::@:: artificial intelligence \(AI\), big data, blockchain, internet of things \(IoT\), etc.
  - field inventory management / challenges ::@:: control difficulty, high costs
    - field inventory management / challenges / high costs ::@:: holding cost per unit per time, ordering cost per order, shortage cost per lost sale
    - field inventory management / challenges / control difficulty ::@:: demand uncertainty, quality variance, random delivery lead-time
- inventory
  - inventory / types ::@:: buffer, cycle, pipeline, safety, seasonal
    - inventory / types / pipeline ::@:: related to units in a ongoing process; recall Little's law
    - inventory / types / seasonal ::@:: fixed capacity but variable demand, e.g. festival products
    - inventory / types / cycle ::@:: related to economics of scale, as it is usually beneficial to produce units in batches
    - inventory / types / buffer ::@:: buffers between activities in a process to enhance activity independence and robustness
    - inventory / types / safety ::@:: to hedge _unpredictable_ demand variations; tradeoff is ordering too few \(to meet unpredictable demand\) vs. too many \(and incur high holding costs\)
- field inventory management
  - field inventory management / models ::@:: economic order quantity \(EOQ\) model, fixed-time period model \(optional\), newsvendor model
    - field inventory management / models / economic order quantity ::@:: used for deterministic demand and long lifecycle products \(holdable for a long time without depreciation\)
    - field inventory management / models / newsvendor ::@:: used for uncertain demand and short lifecycle products \(becomes valueless after a short time\)
    - field inventory management / models / fixed-time period ::@:: \(__this course__: optional\) usually used for ordering a group of items together
- [economic order quantity](../../../../general/economic%20order%20quantity.md) \(EOQ\) ::@:: It is the order quantity that minimizes the total holding costs and ordering costs in inventory management. It is one of the oldest classical production scheduling models.
  - economic order quantity / outputs ::@:: order frequency, order quantity
  - economic order quantity / assumptions ::@:: constant demand rate, constant delivery lead time \(after ordering\), constant holding cost, constant ordering cost
  - economic order quantity / graph ::@:: Under the assumptions of EOQ, the graph of inventory \(y-axis\) against time \(x-axis\) has a sawtooth pattern. <p> A sawtooth pattern starts with a vertical line ascending from zero to a fixed positive number, then linearly declines to zero. Then the pattern repeats.
    - economic order quantity / graph / interpretation ::@:: In a sawtooth, several things can be identified: <p> D: _Demand_ is the absolute slope of the declining portion of the sawtooth. <br/> L: _Delivery lead time_ is how long you need to wait after order to get the inventory. <br/> Q: _Order quantity_ is the height of the sawtooth. The vertical ascending portion of the sawtooth is when the shipment arrives.
  - economic order quantity / variables ::@:: D: _Demand_ is the demand quantity per time. <br/> L: _Delivery lead time_ is how long you need to wait after order to get the inventory. <br/> Q: _Order quantity_ is how many to order each time.
    - economic order quantity / variables / derived ::@:: average inventory: $Q / 2$. This is due to the sawtooth pattern. <br/> frequency of order/shipment: $D / Q$. <br/> reorder point: $D \times L$. The inventory level that indicates you need to order. <br/> time between order/shipment: $Q / D$.
  - economic order quantity / tradeoff ::@:: Ordering more at a time \(higher order quantity\) increases holding cost due to increased average inventory, but decreases ordering cost due to decreased order frequency. <p> The delivery lead time has no effect on the total cost.
  - economic order quantity / cost ::@:: S = order/setup cost, H = marginal holding cost per unit per time <br/> holding cost = H × Q / 2 <br/> ordering cost = S × D / Q <br/> total cost = H × Q / 2 + S × D / Q <p> As expected, increasing Q increases one term while decreases the other.
    - economic order quantity / cost / graph ::@:: In a graph of cost per time \(y-axis\) against order quantity \(x-axis\): The holding cost curve increases linearly from the origin. The order/setup cost curve decreases quickly at first, then decreases increasingly slowly. The total cost curve is U-shaped, and has a _minimum_. Its corresponding order quantity is the _optimal order quantity_. <p> Note that for EOQ, where the holding cost curve and order/setup cost curve _intersects_ is the optimal order quantity.
  - economic order quantity / optimal solution ::@:: The optimal order quantity is: $$Q^* = \sqrt {\frac {2 \times \text{demand rate} \times \text{order or setup cost} } {\text{holding cost} } } \,.$$
    - economic order quantity / optimal solution / derivation ::@:: $$\begin{aligned} C & = HQ / 2 + SD / Q \\ C' & = H / 2 - SD / Q^2 \\ 0 & = H / 2 - SD / Q^2 \\ Q & = \sqrt{\frac {2SD} H} \end{aligned}$$
    - economic order quantity / optimal solution / cost ::@:: The optimal total cost _per time_ is: $$T^* = \sqrt{2 \times \text{demand rate} \times \text{order or setup cost} \times \text{holding cost} } \,.$$ Also, the optimal order cost and optimal holding cost are equal \(divide the above expression by 2\): $$\sqrt{\frac {\text{demand rate} \times \text{order or setup cost} \times \text{holding cost} } 2} \,.$$
      - economic order quantity / optimal solution / cost / derivation ::@:: $$\begin{aligned} T^* & = HQ^* / 2 + SD / Q^* \\ & = \frac H 2 \sqrt{\frac {2SD} H} + SD \sqrt{\frac H {2SD} } \\ & = \sqrt{SDH / 2} + \sqrt{SDH / 2} \\ & = \sqrt{2SDH} \,. \end{aligned}$$
    - economic order quantity / optimal solution / cost per unit ::@:: The optimal cost _per unit_ is: $$\frac {T^*} D = \sqrt{\frac {2 \times \text{order or setup cost} \times \text{holding cost} } {\text{demand rate} } } \,.$$ As demand rate increases, cost per unit decreases \(_economics of scale_\).
    - economic order quantity / optimal solution / inventory turnover ::@:: The optimal inventory turnover _per time_ is: $$\frac D {Q^* / 2} = D \sqrt {\frac {2H} {DS} } = \sqrt{\frac {2 \times \text{demand rate} \times \text{holding cost} } {\text{order or setup cost} } } \,.$$ The intuition is that if holding cost is high or ordering cost is low, we should turn the inventory more frequently.
  - economic order quantity / unit cost ::@:: The above model assumes purchasing a unit is free. This is obviously not the case in the real world. <p> The total cost is the same, with the _purchasing cost_ added. The _purchasing cost per unit time_ equals $D \times C$, where $C$ is the unit cost.
    - economic order quantity / unit cost / optimal solution ::@:: Since the purchasing cost does not depend on the order quantity, the _optimal order quantity_ is unchanged. <p> The _optimal costs_ are increased by taking the purchasing cost into account.
  - economic order quantity / lead time ::@:: The delivery lead time _does not_ affect the optimal order frequency or the optimal order quantity. It only affects when to order.
    - economic order quantity / lead time / reorder point ::@:: It is the inventory level that indicates that we should place a new order, calculated as: $$\text{ROP} = \text{demand rate} \times \text{lead time} \,.$$ <p> \(__this course__: We _always_ assume the reorder point is strictly less than the order quantity. Though you could try to interpret what happens if the reorder point exceeds the order quantity...\)

## week 9 lecture 2

- datetime: 2025-04-02T10:30:00+08:00/2025-04-02T11:50:00+08:00, PT1H20M
- status: unscheduled, midterm break

## week 10 lecture

- datetime: 2025-04-07T10:30:00+08:00/2025-04-07T11:50:00+08:00, PT1H20M
- topic: inventory management, newsvendor model
- status: attendance
- [newsvendor model](../../../../general/newsvendor%20model.md) ::@:: It is a mathematical model in operations management and applied economics used to determine optimal inventory levels.
  - newsvendor model model / motivation ::@:: A news stand buys newspaper to sell. At the end of the day, they become outdated. <p> How many newspaper should the news stand buy? Too many, then loss from unsold newspapers. Too little, then loss from potential sales.
  - newsvendor model model / characteristics ::@:: It is \(typically\) characterized by fixed prices and uncertain demand for a perishable product. If the inventory level is $q$, each unit of demand above $q$ is lost in potential sales.
    - newsvendor model model / characteristics / vs. EOQ model ::@:: demand: random vs. deterministic <br/> method: marginal expected value vs. first-order derivative of cost function <br/> objective: maximize _profit_ vs. minimize _cost_ <br/> order opportunity: once vs. multiple <br/> period \#: single vs. multiple <br/> product lifecycle: short vs. long
  - newsvendor model model / assumptions ::@:: - Products are separable <br/> - Planning is done for a single period <br/> - Demand is random <br/> - Deliveries are made in advance of demand <br/> - Costs of overage or underage are linear
  - newsvendor model model / marginal analysis ::@:: It can be solved by considering the effect of adding one more unit on profits, i.e. _marginal profit_. <p> If it is positive, add. If it is negative, do not add \(or remove\). If it is zero, we are indifferent. The optimal solution is _usually_ obtained when the marginal profit is zero.
    - newsvendor model model / marginal analysis / derivation ::@:: The demand is modeled by the CDF $F(x)$ \(for simplicity, assume its PDF $f(x) := F'(x)$ exists and is _continuous_\). Consider adding one more unit when we are already selling $x$. If sold, you gain profit $g$ \(more generally _understocking_ cost\). If unsold, you lose cost $l$ \(more generally _overstocking_ cost\). <p> The expected utility of selling one more unit is: $$g (1 - F(x)) - l F(x) = g - (g + l) F(x) \,,$$ since $F(x)$ is the probability of demand being at most $x$. To optimize it, set it to zero: $$g - (g + l) F(x) = 0 \implies F(x) = \frac g {g + l} \implies x = F^{-1}\left(\frac {g} {g + l} \right) \,.$$ <p> An alternative expression with price $p$ and cost $c$ with zero salvage value: $$x = F^{-1}\left(\frac {p - c} p\right) \,.$$
  - newsvendor model model / intuition ::@:: As we have more inventory, the probability of selling another unit becomes smaller. So the expected utility of a marginal unit becomes smaller.
  - newsvendor model model / costs ::@:: The conventional way is to use price $p$ and cost $c$. If there is any salvage value $s$, treat the price as $p - s$ and the cost as $c - s$. <p> More generally, we can use _understocking_ \(opportunity\) cost: $$C_u = p - c \,,$$ which is the cost of not having an unit \(compared to having the unit\) when there is demand; and _overstocking_ cost: $$C_o = c - s \,,$$ which is the cost of having an unit \(compared to not having the unit\) when there is no demand.
    - newsvendor model model / costs / intuition ::@:: A larger understocking cost encourages ordering more. A larger overstocking cost encourages ordering less.
  - newsvendor model model / critical fractile ::@:: We see above that the solution is: $$F\left(x\right) = \frac {C_u} {C_u + C_o} \implies x = F^{-1}\left(\frac {C_u} {C_u + C_o}\right) \,.$$ The rightmost term is known as the _critical fractile_.
    - newsvendor model model / critical fractile / properties ::@:: Increasing understocking cost $C_u$ increases the critical fractile, so order more, and vice versa. Increasing overstocking cost $C_o$ decreases the critical fractile, so order less, and vice versa. <p> They match our intuition!
  - newsvendor model model / discrete distribution ::@:: Find the critical fractile. Then find the corresponding quantity in the _cumulative_ distribution table. You may need to find the cumulative distribution table yourself first. \(__this course__: Use the _round-up rule_, i.e. choosing a larger value of integer _n_ if _x_ is not an integer or if the CDF is given as a table.\)
- normal distribution
  - normal distribution / standardization
- newsvendor model model
  - newsvendor model model / normal distribution ::@:: Find the critical fractile. Using the Z-table, find the corresponding z-score. Finally, convert the z-score $z^*$ into the quantity we want: $$Q^* = \mu + \sigma \times z^* \,.$$ \(__this course__: Use the _round-up_ rule to lookup the z-score, i.e. choose a larger value of z-score if in between two z-scores, and then use the round-up rule _again_ if the quantity needs to be an integer.\)
- [questions § week 10 lecture](questions/index.md#week%2010%20lecture)

## week 10 lecture 2

- datetime: 2025-04-09T10:30:00+08:00/2025-04-09T11:50:00+08:00, PT1H20M
- topic: newsvendor model applications
- newsvendor model model
  - newsvendor model model / service level ::@:: The probability that the demand is fulfilled. This is literally just the critical fractile at the optimal ordering quantity. \(__this course__: Using the _round-up_ rule may raise it slightly...\)
  - newsvendor model model / shortage probability ::@:: The probability the demand is not fully fulfilled. This is literally just one subtracted by the critical fractile at the optimal ordering quantity. \(__this course__: Using the _round-up_ rule may reduce it slightly...\)
  - newsvendor model model / metrics ::@:: leftover, lost sales, sales <p> They are also random since the demand is random.
    - newsvendor model model / metrics / leftover ::@:: $$\text{leftover} = \max\set{Q - D, 0} \,.$$
    - newsvendor model model / metrics / sales ::@:: $$\text{sales} = \min\set{Q, D} \,.$$
    - newsvendor model model / metrics / lost sales ::@:: $$\text{lost sales} = \max\set{D - Q, 0} \,.$$
  - newsvendor model / expected leftover ::@:: Theoretically, we can derive it. But it is not simply $\operatorname E[Q] - \operatorname E[D]$ because leftover cannot be negative \(limited by the $\max$ function\). <p> For normal distribution, this is $$\text{expected leftover} = \sigma \cdot I(z^*) \,,$$ where $\sigma$ is the _standard deviation_, $I(z)$ is the  _standard normal inventory function_, and $z^*$ is the z-score of the optimal order quantity. \(__this course__: Just round to the nearest integer. The instructor promised this will not matter in exams.\)
  - newsvendor model / standard normal inventory distribution ::@:: It is a distinct distribution distinct from the standard normal distribution. it is used to calculate expected leftover. \(__this course__: A table is provided.\)
  - newsvendor model / expected sales ::@:: Quite intuitive: $$\text{expected sales} = Q^* - \text{expected leftover} \,,$$ derived from $$\text{sales} + \text{leftover} = Q^* \,.$$
  - newsvendor model / lost sales ::@:: Quite intuitive: $$\text{expected lost sales} = \text{expected demand} - \text{expected sales} \,,$$ derived from $$\text{sales} + \text{lost sales} = \text{demand} \,.$$
  - newsvendor model / expected profit ::@:: It is _maximized_ at $Q^*$. <p> You can calculate it normally using expected sales and expected leftover inventory. It equals: $$\begin{aligned} \text{expected profit} & = \text{profit per unit} \times \text{expected sales} \\ & - \text{leftover cost per unit} \times \text{expected leftover} \,, \end{aligned}$$ where profit per unit is $C_u = p - c$ and leftover cost per unit is $C_o = c - s$.
    - newsvendor model / expected profit ::@:: A more intuitive way: $$\text{expected profit} = p \times \text{expected sales} + s \times (Q^* - \text{expected sales}) - c \times Q^* \,.$$
  - newsvendor model / tradeoff ::@:: Profit is obvious important. But _service level_ is also important as it may affect customer satisfaction and market share. <p> Profit increases until the optimal order quantity, and decreases thereafter. Service level _always_ increase, but with _diminishing returns_.
- [pooling](../../../../general/pooling%20(resource%20management).md) ::@:: In resource management, \(_this_\) is the grouping together of resources \(assets, equipment, personnel, effort, etc.\) for the purposes of maximizing advantage or minimizing risk to the users. The term is used in finance, computing and equipment management.
- [risk pool](../../../../general/risk%20pool.md) ::@:: \(_this_\) suggests that demand variability is reduced if one aggregates demand across locations because as demand is aggregated across different locations, it becomes more likely that high demand from one customer will be offset by low demand from another. The reduction in variability allows a decrease in safety stock and therefore reduces average inventory.
  - risk pool / conditions ::@:: The demand needs to be _independent_.
  - risk pool / location pooling ::@:: It combines the inventory originally in multiple locations into a single location. <p> We need to consider sale efficiency impact, setup cost, incentive conflicts, etc.
- [mean](../../../../general/mean.md)
  - mean / addition ::@:: The mean of adding several probability distributions equals the sum of the means of them.
- [standard deviation](../../../../general/standard%20deviation.md)
  - standard deviation / addition ::@:: The standard deviation of adding several _mutually independent_ \(weakened: _uncorrelated_\) probability distributions equals the square root sum of the squares of the standard deviations of them. <p> Special case: For two _independent_ normal distributions: $$\sigma = \sqrt{\sigma_1^2 + \sigma_2^2} \,.$$
- risk pool
  - risk pool / newsvendor model ::@:: It does not change the critical fractile. It also increases the _standard deviation_ but reduces the _coefficient of variation_ \(CV\).
    - risk pool / newsvendor model / effects ::@:: By reducing variability \(coefficient of variation\), pooling has many good effects. <p> Order quantity or inventory is smaller \(relative to demand\). Expected leftover inventory and lost sales are reduced. Expected sales are increased. Thus, expected profit is higher.
  - risk pool / correlation ::@:: \(__this course__: optional\) Above, we assume demands are independent. Positive correlation reduces the benefit. When perfectly positive correlated, there is no benefit.
  - risk pool / diminishing returns ::@:: \(__this course__: optional\) As pool size increase, benefit increases, but with _diminishing returns_. That is, the _marginal benefit_ of pooling another inventory decreases.

## week 11 lecture

- datetime: 2025-04-14T10:30:00+08:00/2025-04-14T11:50:00+08:00, PT1H20M
- topic: revenue management, capacity-based revenue management
- status: attendance
- [revenue management](../../../../general/revenue%20management.md) \(RM\) ::@:: It is a discipline to maximize profit by optimizing rate \(ADR\) and occupancy \(Occ\). In its day to day application the maximization of Revenue per Available Room \(RevPAR\) is paramount. It is seen by some as synonymous with yield management.
  - revenue management / history ::@:: It was first developed in airline industry in 1980.
  - revenue management / types ::@:: two main types \(there are more\): capacity-based, price-based
  - revenue management / capacity-based ::@:: fixed and perishable resources, widely used in transport industries
  - revenue management / price-based ::@:: dynamic pricing, markdown pricing, surge pricing, etc.
  - revenue management / motivation ::@:: Increasing revenue without increasing cost increases gross margin and net margin significantly.
  - revenue management / applications ::@:: car rental, dynamic pricing \(e.g. airplane tickets gets more expensive as flight time approaches\), media & broadcasting, price differentiation \(e.g. different classes\), retailing
  - revenue management / key ::@:: Using demand, supply, and _analytics_ to perform _customer segmentation_ based on _time_ and _quality_.
  - revenue management / goal ::@:: To match supply with demand on a customer basis.
- [Littlewood's rule](../../../../general/Littlewood's%20rule.md) ::@:: The earliest revenue management model is known as \(_this_\), developed by Ken Littlewood while working at British Overseas Airways Corporation.
  - Littlewood's rule / strategy ::@:: two-price strategy: Cheap tickets target low-spending customers, while expensive tickets target high-spending customers. Capacity \(empty seats\) is _perishable_.
  - Littlewood's rule / assumptions ::@:: Cheap tickets are always sold out in _advance_ with _sufficient_ demand. Expensive tickets are sold at the _last minute_ with _limited_ random demand.
  - Littlewood's rule / tradeoff ::@:: If you sell too many cheap tickets, then you may lose revenue from demand for the expensive tickets. If you sell too little cheap tickets, then you may have wasted capacity due to the random demand for the expensive tickets.
  - Littlewood's rule / protection level ::@:: The capacity reserved for _expensive_ tickets. It with booking limit adds up to the total capacity.
  - Littlewood's rule / booking limit ::@:: The capacity remaining for _cheap_ tickets. It with protection level adds up to the total capacity.
  - Littlewood's rule / newsvendor model ::@:: An alternative but equivalent way to solve the problem. <p> demand → expensive ticket customers <br/> overstocking: too high protection level <br/> understocking: too little protection level
    - Littlewood's rule / newsvendor model / understocking cost ::@:: Cost due to too little protection level, It equals the expensive ticket price \("price"\) subtracted by the cheap ticket price \("salvage value"\).
    - Littlewood's rule / newsvendor model / overstocking cost ::@:: Cost due to too much protection level. It equals the cheap ticket price.
    - Littlewood's rule / newsvendor model / metrics ::@:: demand → expensive ticket customers <br/> expected leftover → expected unsold expensive tickets <br/> expected lost sales → unfulfilled expensive ticket customers <br/> expected revenue: includes both classes <br/> expected sales → expected sold expensive tickets
  - Littlewood's rule / the problem ::@:: Those two fare classes have a fare of $R_{1}$ and $R_{2}$, whereby $R_{1}>R_{2}$. The total capacity is $C$ and demand for class $j$ is indicated with $D_{j}$. The demand has a [probability distribution](../../../../general/probability%20distribution.md) whose cumulative distribution function is denoted $F_{j}$. The demand for class 2 comes before demand for class 1. The question now is how much demand for class 2 should be accepted so that the optimal mix of passengers is achieved and the highest revenue is obtained.
  - Littlewood's rule / the rule ::@:: Littlewood suggests closing down class 2 when the certain revenue from selling another low fare seat is exceeded by the expected revenue of selling the same seat at the higher fare. In formula form this means: accept demand for class 2 as long as: $$R_{2}\geq R_{1}\cdot \operatorname {Prob} (D_{1}>x)$$ where <p> &emsp; $R_{2}$ is the value of the lower valued segment <br/> &emsp; $R_{1}$ is the value of the higher valued segment <br/> &emsp; $D_{1}$ is the demand for the higher valued segment and <br/> &emsp; $x$ is the capacity left \(for class 1\) <p> This suggests that there is an optimal protection limit $y_{1}^{\star }$.
  - Littlewood's rule / the solution ::@:: This suggests that there is an optimal protection limit $y_{1}^{\star }$. If the capacity left is less than this limit demand for class 2 is rejected. If a [continuous distribution](../../../../general/continuous%20distribution.md#absolutely%20continuous%20probability%20distribution) $F_{j}(x)$ is used to model the demand, then $y_{1}^{\star }$ can be calculated using what is called _Littlewood’s rule_: $$y_{1}^{\star }=F_{1}^{-1}\left(1-{\frac {R_{2} }{R_{1} } }\right)$$ This gives the optimal protection limit, in terms of the division of the marginal revenue of both classes.
    - Littlewood's rule / the solution / equivalency ::@:: $$y_1^* = F_1^{-1} \left(1 - \frac {R_2} {R_1} \right) = F_1^{-1}\left(\frac {R_1 - R_2} {R_1} \right) \,,$$ where $C_u = R_1 - R_2$ \(expensive ticket minus cheaper ticket\) is the _understocking/underprotection cost_ and $C_o = R_2$ \(cheaper ticket\) is the _overstocking/overprotection cost_.
  - Littlewood's rule / generalization ::@:: \(__this course__: optional\) Littlewood's model is limited to two classes. Peter Belobaba developed a model based on this rule called expected marginal seat revenue, abbreviated as EMSR, which is an _n_-class model.
- [expected marginal seat revenue](../../../../general/expected%20marginal%20seat%20revenue.md) \(EMSR\) ::@:: \(__this course__: optional\) \(_this_\) is a very popular heuristic in Revenue Management. There are two versions: EMSRa and EMSRb, both of which were introduced by Peter Belobaba. Both methods are for n-class, static, single-resource problems.
  - expected marginal seat revenue / idea ::@:: \(__this course__: optional\) Apply Littlewood's rule/newsvendor model iteratively to successive classes, from the highest fare to the lowest.
- [overselling](../../../../general/overselling.md) ::@:: \(_this_\) is sale of a volatile good or service in excess of actual supply.
  - overselling / motivation ::@:: Overselling is a common practice in the travel and hospitality sectors, in which it is expected that some people will cancel. The practice occurs as an intentional business strategy in which sellers expect that some buyers will not consume all of the resources they are entitled to, or that some buyers will cancel. The practice of overselling aims to ensure that 100% of available supply will be used, resulting in the maximum return on investment.
  - overselling / cost ::@:: If more customers than the seller expects do wish to purchase or use the sold commodity, it may leave some customers lacking a service they expected to receive. <p> In airlines, this is known as _bumping_, where customers are voluntarily or involuntarily denied boarding. There are _direct costs_ for compensation and _implicit costs_ for customer dissatisfaction.
  - overselling / newsvendor model ::@:: demand → number of customers _not_ showing up <br/> overstocking: too high overbooking level <br/> understocking: too little overbooking level
    - overselling / newsvendor model / understocking cost ::@:: Cost due to too little overbooking level, It equals the ticket price.
    - overselling / newsvendor model / overstocking cost ::@:: Cost due to too high overbooking level. It equals the _bumping_ cost \(includes the price of a new free ticket\) subtracted by the ticket price \("salvage value"\).
    - overselling / newsvendor model / metrics ::@:: expected leftover → expected bumped customers <br/> expected lost sales → expected empty seats <br/> expected revenue from overbooking \(relative to _not_ overbooking\): $$C_u \times \text{expected (additional) sales} - C_o \times \text{expected leftover/bumps}$$ <br/> expected sales → expected _additional_ customers served due to other customers _not_ showing up
    - overselling / newsvendor model / service level ::@:: The probability that no customer bumping happens. It equals the probability of _not_-showing-up customers being _at least_ \(it matters\) the overbooking level.
- newsvendor model
  - newsvendor model / generalization ::@:: The above two examples applies the newsvendor model to other problems such as two-price strategy and overselling. <p> To generalize the model for other problems, identify the demand and the inventory. The demand should be _random_, and higher of it should increase _revenue_. The inventory should be _controllable_ and optimal when it _matches_ demand.
- [questions § week 11 lecture](questions/index.md#week%2011%20lecture)

## week 11 lecture 2

- datetime: 2025-04-16T10:30:00+08:00/2025-04-16T11:50:00+08:00, PT1H20M
- topic: price-based revenue management
- revenue management
  - revenue management / types
  - revenue management / price-based
- [price optimization](../../../../general/price%20optimization.md) ::@:: \(_this_\) is the use of mathematical analysis by a company to determine how customers will respond to different prices for its products and services through different channels and is in contrast to market value. It is also used to determine the prices that the company determines will best meet its objectives such as maximizing operating profit.
  - price optimization / prevalence ::@:: It is becoming more prevalent because of big data \(on customer demand\), decreasing computing cost, and increased price flexibility.
  - price optimization / examples ::@:: Verm City, dynamic pricing \(e.g. Amazon, HKTVMall\)
- [willingness to pay](../../../../general/willingness%20to%20pay.md) (WTP) ::@:: It is the maximum price at or below which a consumer will definitely buy one unit of a product.
  - willingness to pay / price optimization ::@:: For customer segmentation, so that firms can charge different price for different customers. \(_c.f._ price discrimination\)
  - willingness to pay / factors ::@:: customer characteristics, product characteristics, substitutability
  - willingness to pay / table ::@:: A table that shows WTP prices and the corresponding number of customers with that _exact_ \(_not_ equal to or lower than\) WTP price.
    - willingness to pay / table / revenue maximization ::@:: Given a WTP table, build the _cumulative_ WTP table from highest WTP to lowest WTP. The cumulative count is also the _demand_. Then calculate the revenue for each price or demand level, and choose the one with the highest revenue.
- [demand curve](../../../../general/demand%20curve.md) ::@:: It is a graph depicting the inverse demand function, a relationship between the price of a certain commodity \(the y-axis\) and the quantity of that commodity that is demanded at that price \(the x-axis\).
  - demand curve / linear ::@:: $$D(p) = a - bp \,,$$ where $a$ is a constant, and $b$ is price sensitivity.
    - demand curve / linear / revenue maximization ::@:: Revenue is: $$p \cdot D(p) = ap - bp^2 \,,$$ It is maximized when: $$a - 2bp = 0 \implies p = \frac a {2b} \,.$$ <p> It is equivalent to profit maximization when the cost is _constant_.
    - demand curve / linear / advantages ::@:: easy to communicate, estimate, and model: customer questionnaire, linear regression, market survey, etc. <br/> only need few data
    - demand curve / linear / disadvantages ::@:: cannot capture non-linear relationship, e.g. marginal price \(price change rate\) changes with price level
- price optimization
  - price optimization / multiple products ::@:: Pricing multiple products that may affect each others' demands. <p> If the pricing can be done _individually_ or _jointly_.
    - price optimization / multiple products / assumptions ::@:: There are multiple products. Assume the demand for each product is linear with respect to each price of all products, e.g. $$\begin{aligned} D_1 & = c_{1,0} + c_{1,1} p_1 + c_{1,2} p_2 \\ D_2 & = c_{2,0} + c_{2,1} p_1 + c_{2,2} p_2 \,. \end{aligned}$$ <p> If $c_{i,j} > 0$ where $i \ne j$, then these two products are _substitutes_. If $c_{i,j} < 0$ where $i \ne j$, then these two products are _complements_.
    - price optimization / multiple products / individual pricing ::@:: For each product, assume the price of all other products are fixed. Maximize revenue due to the product itself with respect to its own price. <p> The above procedure gives an equation for each product. Find the solution satisfying all equations, which are the optimal prices for all products under _individual pricing_, which is used when the prices are set by different businesses competing with each other.
    - price optimization / multiple products / intuition ::@:: Imagine a player for each product controlling its own price. The procedure for individual pricing is finding a _Nash equilibrium_. In a Nash equilibrium, no players want to change their own price, since there is no other price that gives more revenue, given all other players' price are fixed. <p> In general, optimizing things considering more things together give better results than optimizing things considering each thing individually. This explains why joint pricing give higher total revenue than individual pricing.
    - price optimization / multiple products / joint pricing ::@:: For each product, assume the price of all other products are fixed. Maximize revenue due to _all products_ with respect to its own price. <p> The above procedure gives an equation for each product. Find the solution satisfying all equations, which are the optimal prices for all product under _joint pricing_, which is used when the prices are set by the same business optimizing its pricing or businesses cooperating together to set their pricing.
    - price optimization / multiple products / individual pricing vs. joint pricing ::@:: With joint pricing, total revenue increases \(or at least not decrease\). <p> This implies competing businesses can cooperate on pricing to increase total revenue. This does not imply individual revenues for each business must increase though. Instead, total revenue should be _distributed_ between the businesses such that individual revenues of each business is not less than before.
- [partial derivative](../../../../general/partial%20derivative.md) ::@:: \(__this course__: optional\) It of a function of several variables is its derivative with respect to one of those variables, with the others held constant (as opposed to the total derivative, in which all variables are allowed to vary).
  - partial derivative / in univariate calculus ::@:: \(__this course__: optional\) There is only one (or two) direction $x$ can change in. Thus in this case, the derivative definition is quite simple and we only have one (first) derivative.
  - partial derivative / intuition ::@:: \(__this course__: optional\) Fix all arguments to a multivariate function except for one. Then differentiate it with respect to that argument. This is the _partial derivative with respect to that argument_. <p> One partial derivative can be constructed for each argument in this way.
  - partial derivative / notations ::@:: \(__this course__: optional\) The partial derivative of a function $f(x,y,\dots )$ with respect to the variable $x$ is variously denoted by <p> $f_{x}$, $f'_{x}$, $\partial _{x}f$, $\ D_{x}f$, $D_{1}f$, ${\frac {\partial }{\partial x} }f$, or ${\frac {\partial f}{\partial x} }$.
  - partial derivative / computation ::@:: \(__this course__: optional\) Assume all other variables are constant. Then differentiate as if it is a univariate function. <p> Implicit differentiation is another technique. It works similar to that applied to a univariate function. If a variable is neither the variable being differentiated against (output) nor being differentiated with respect to (input), consider it fixed.
- [derivative test](../../../../general/derivative%20test.md) ::@:: \(__this course__: optional\) It uses the derivatives of a function to locate the critical points of a function and determine whether each point is a local maximum, a local minimum, or a saddle point. Derivative tests can also give information about the concavity of a function.
- price optimization
  - price optimization / multiple products
    - price optimization / multiple products / optimality ::@:: \(__this course__: optional\) For joint pricing, when the partial derivatives of total revenue with respect to all prices are all zero, we get an optimal solution by the first derivative test \(note we are skipping quite a lot of mathematical rigour\). <p> For individual pricing, the partial derivative of the revenue of each product with respect to its own price is zero.
- [price markdown](../../../../general/price%20markdown.md) ::@:: A \(_this_\) is a deliberate reduction in the selling price of retail merchandise. It is used to increase the _velocity_ \(rate of sale\) of an article, typically for clearance at the end of a season, or to sell off obsolete merchandise at the end of its life.
  - price markdown / vs. promotion ::@:: The former is permanent \(at least for the foreseeable future\) while the latter is temporary.
  - price markdown / motivation ::@:: deterioration/spoilage \(e.g. bread\), obsolescence \(e.g. new iPad\), time of use \(e.g. holiday-specific decorations\)
  - price markdown / problems ::@:: cannibalization effect: Customers wait for the markdown, which erodes regular sales.
- [product bundling](../../../../general/product%20bundling.md) ::@:: In marketing, \(_this_\) is offering several products or services for sale as one combined product or service package. It is a common feature in many imperfectly competitive product and service markets.
  - product bundling / advantages ::@:: Buyers and sellers can simultaneously benefit, measured using _revenue_ for sellers and _consumer surplus_ for buyers.
  - product bundling / uses ::@:: entertainment, games, retail, restaurants, telecommunications
  - product bundling / intuition ::@:: It exploits heterogeneity in customers' WTP for different products. By bundling them together and offering a lower price than buying separately, sellers obviously earn more revenue as buyers now buy both, but buyers get more as bundling allows them to buy both at a lower price. <p> You can construct an example using WTP.
- [decoy effect](../../../../general/decoy%20effect.md) ::@:: In marketing, the \(_this_\) is the phenomenon whereby consumers will tend to have a specific change in preference between two options when also presented with a third option that is _asymmetrically dominated_.
  - decoy effect / asymmetric domination ::@:: An option is asymmetrically dominated when it is inferior in all respects to one option; but, in comparison to the other option, it is inferior in some respects and superior in others. In other words, in terms of specific attributes determining preferences, it is completely dominated by \(i.e., inferior to\) one option and only partially dominated by the other.
  - decoy effect / effect ::@:: When the asymmetrically dominated option is present, a higher percentage of consumers will prefer the dominating option than when the asymmetrically dominated option is absent. The asymmetrically dominated option is therefore a decoy serving to increase preference for the dominating option.
- [psychological pricing](../../../../general/psychological%20pricing.md) ::@:: \(_this_\) is a pricing and marketing strategy based on the theory that certain prices have a psychological impact. In this pricing method, retail prices are often expressed as just-below numbers: numbers that are just a little less than a round number, e.g. \$19.99 or £2.98.  
  - psychological pricing / effect ::@:: There is evidence that consumers tend to perceive just-below prices \(also referred to as "odd prices"\) as being lower than they are, tending to round to the next lowest monetary unit. Thus, prices such as \$1.99 may to some degree be associated with spending \$1 rather than \$2. The theory that drives this is that pricing practices such as this cause greater demand than if consumers were perfectly rational.
- [supply chain](../../../../general/supply%20chain.md) ::@:: A \(_this_\) is a complex logistics system that consists of facilities that _convert_ raw materials into finished products and _distribute_ them to end consumers or end customers, while _supply chain management_ deals with the _flow of goods in distribution channels_ within the supply chain in the most _efficient_ manner.
  - supply chain / elements ::@:: \(upstream\) supplier → manufacturer → distributor → retailer → customer \(downstream\)
  - supply chain / goal ::@:: To match supply and demand \(again\), as to increase revenue and reduce cost.
    - supply chain / goal / factors ::@:: right... customer, price, product, quantity, store, time
  - supply chain / flows::@:: Material flows forwards. Information flows bidirectionally. Cash flows backwards.
- [supply chain management](../../../../general/supply%20chain%20management.md) \(SCM\) ::@:: In commerce, \(_this_\) deals with a system of procurement \(purchasing raw materials/components\), operations management, logistics and marketing channels, through which raw materials can be developed into finished products and delivered to their end customers.
  - supply chain management / perspective ::@::  a firm competing in our own industry → a firm competing in our own supply chain against other supply chains for end customers
  - supply chain management / strategies & challenges ::@:: adaptability: shortened \(product and technology\) cycles <br/> agility: increased uncertainty \(in demand and/or supply\) <br/> alignment: complexity
  - supply chain management / agility ::@:: Ability to _quickly_ adjust strategy to meeting changing supply chain _requirements_.
  - supply chain management ::@:: Ability to meet _structural_ changes in markets and supply chains.
  - supply chain management / uncertainty framework ::@:: \(__this course__: optional\) understand nature of demand and devise supply chain
  - supply chain management / alignment ::@:: Coordinate between entities in a supply chain to achieve better outcomes for all, which requires efficient _sharing_ of information, revenue, risk, etc. to facilitate internal and external alignments.
  - supply chain management / contract ::@:: A set of rules to control or modify flow of goods \(forward\) and/or cash \(backward\) in a supply chain. It should be _enforceable_ and _verifiable_.
- [double marginalization](../../../../general/double%20marginalization.md) ::@:: \(_this_\) is a vertical externality that occurs when two firms with market power \(i.e., not in a situation of perfect competition\), at different vertical levels in the same supply chain, apply a mark-up to their prices.
  - double marginalization / cause ::@:: This is caused by the prospect of facing a steep demand curve slope, prompting the firm to mark-up the price beyond its marginal costs.
  - double marginalization / effect ::@:: Double marginalization is clearly negative from a welfare point of view, as the double markup induces a deadweight loss, because the retail price is higher than the optimal monopoly price a vertically integrated company would set, leading to underproduction. Thus all social groups are negatively affected because the overall profit for the company is lower, the consumer has to pay more and a smaller amount of units are consumed.
- [bullwhip effect](../../../../general/bullwhip%20effect.md) ::@:: The \(_this_\) is a supply chain phenomenon where orders to suppliers tend to have a larger variability than sales to buyers, which results in an amplified demand variability upstream. In part, this results in increasing swings in inventory in response to shifts in consumer demand as one moves further up the supply chain.
  - bullwhip effect / reasons ::@:: forward buying, order batching/synchronization, over-reactive ordering, trade promotion, etc.
  - bullwhip effect / solutions ::@:: collaborative planning, forecasting, replenishment, etc.
- supply chain
  - supply chain / recent developments ::@:: AI, COVID-19 pandemic, automation, risk mitigation, US—China trade/tariffs, etc.
    - supply chain / recent developments / COVID-19 pandemic ::@:: economic slowdown, increased delivery time, inflation, shortage of products
    - supply chain / recent developments / risk mitigation ::@:: Firms need to focus more on mitigation hidden risks. <p> regionalization \(produce closer\), single-sourcing to multi-sourcing, sustainability, tradeoff between efficiency \(cost\) and robustness \(risk\)
    - supply chain / recent developments / opportunities ::@:: Firms need contingency plan to deal with recent disruptions in supply chains. Thus there may be rich opportunities for risk management in supply chains.
    - supply chain / recent developments / tariffs ::@:: Tariffs by the second Trump administration and retaliation is impacting the global economy and financial markets. <p> It may lead to disorderly economic decoupling. Or not, instead lengthening supply chains and making it more complex and less visible, e.g. products going through intermediate countries, etc.

## week 12 lecture

- datetime: 2025-04-21T10:30:00+08:00/2025-04-21T11:50:00+08:00, PT1H20M
- status: unscheduled, public holiday: Easter Monday

## week 12 lecture 2

- datetime: 2025-04-23T10:30:00+08:00/2025-04-23T11:50:00+08:00, PT1H20M
- topic: supply chain management, win strategies

## week 13 lecture

- datetime: 2025-04-28T10:30:00+08:00/2025-04-28T11:50:00+08:00, PT1H20M
- topic: incentive conflict: risk-sharing strategies
- status: attendance
- [wholesaling](../../../../general/wholesaling.md) ::@:: \(_this_\) is the sale of goods or merchandise to retailers; to industrial, commercial, institutional or other professional business users; or to other __wholesalers__ \(__wholesale businesses__\) and related subordinated services.
  - wholesaling / model ::@:: supplier → retailer → \(customers\) <p> The customer demand is random. <p> A wholesale price contract involves the retailer ordering _q_ units at a _wholesale price_ _w_ \(assume _w_ is higher than the salvage value _s_\).
- supply chain
  - supply chain / optimum ::@:: The _entire supply chain_ optimum can be found by considering the entire supply chain as one entity. Then maximize the _total expected profit_ of the entire supply chain \(includes supplier and retailer\).
- wholesaling
  - wholesaling / supply chain optimum ::@:: Consider the entire supply chain as one. Then only production cost, retail price, and salvage value matters. In particular, ignore wholesale price. Maximize _total profit_ using the newsvendor model.
  - wholesaling / retailer optimum ::@:: Now consider the retailer only. Then only wholesale price \(as cost\), retail price, and salvage value matters. In particular, ignore production cost, since wholesale price is the cost for the retailer. Maximize profit for the retailer using the newsvendor model. <p> The optimal inventory quantity is also how much the retailer orders from the supplier. The profit for the supplier can then be calculated. Finally, the _total profit_ can be calculated.
    - wholesaling / retailer optimum / vs. supply chain optimum ::@:: Due to _misalignment of interest_, this results in _double marginalization_. The misalignment is due to the retailer basing its decision on the wholesale price instead of the production cost \(lack of alignment\), and the supplier does not bear the uncertainty of the random demand \(conflicting incentives\). <p> This explains why the retailer optimum has a _total profit_ lower than the supply chain optimum. This shows a cooperation opportunity for the supplier and the retailer to increase their total profit.
  - wholesaling / critical fractile ::@:: The order quantity is completely determined by the critical fractile of the entity responsible for meeting the random demand. <p> For supply chain optimum, that entity is the entire supply chain. For retailer optimum, that entity is the retailer.
    - wholesaling / critical fractile / retailer optimum ::@:: We see that the wholesaling price needs to equal the production cost for the retailer optimum to equal the supply chain optimum: $$\frac {p - w} {p - s} = \frac {p - c} {p - s} \implies w = c \,.$$ That means the supplier receives zero profit, which it is unlikely to accept. <p> This is a _fundamental limitation_ of the _traditional_ wholesale price contract.
  - wholesaling / expected profit distribution ::@:: When wholesale price is zero, the retailer gets all the expected profit. The expected total profit equals that of the supply chain optimum. <p> When wholesale price increases, the retailer expected profit always decrease, while the supplier expected profit increases at first, but then decreases as the total profit decreases.
    - wholesaling / profit distribution / wholesaler ::@:: As the wholesaler, you need to set a wholesale price such that you have a large share of the total profit, but the total profit does not decrease too much. So there is an optimum wholesale price.
- [revenue sharing](../../../../general/revenue%20sharing.md) ::@:: \(_this_\) is the distribution of revenue, the total amount of income generated by the sale of goods and services among the stakeholders or contributors.
  - revenue sharing / model ::@:: supplier → retailer → \(customers\) <p> The customer demand is random. <p> A wholesale price contract involves the retailer ordering _q_ units at a _wholesale price_ _w_ \(assume _w_ is higher than the salvage value _s_\), and additionally a fixed percentage _y_ of the _retail_ price is transferred from the retailer to the supplier per sale unit. <p> The traditional wholesale price contract is reobtained when _y_ equals zero.
  - revenue sharing / critical fractile ::@:: The order quantity is completely determined by the critical fractile of the entity responsible for meeting the random demand. <p> For supply chain optimum, that entity is the entire supply chain. For retailer optimum, that entity is the retailer. But under revenue sharing, the supply chain optimum can always be obtained under some conditions.
    - revenue sharing / critical fractile / retailer optimum ::@:: For the retailer optimum to equal the supply chain optimum, we need to equate the critical fractiles: $$\begin{aligned} \frac {p(1 - y) - w} {p(1 - y) - s} & = \frac {p - c} {p - s} \\ (p(1 - y) - w) (p - s) & = (p(1 - y) - s)(p - c) \\ (p - yp - w) (p - s) & = (p - yp - s) (p - c) \\ p^2 - yp^2 - wp - ps + yps + ws & = p^2 - yp^2 - sp - pc + ypc + sc \\ -wp + yps + ws & = -pc + ypc + sc \\ ypc - yps & = -wp + ws + pc - sc \\ y & = \frac {(p - s) (c - w)} {p (c - s)} \\ & = \frac {p - s} {c - s} \frac {c - w} p \,. \end{aligned}$$ <p> For memorization, $$\frac {c - w} p$$ can be interpreted as the percentage markdown of $w$ from $c$ relative to $p$, while $$\frac {p - s} {c - s}$$ can be interpreted as the ratio of $p$ over $c$, both offset by the salvage value.
      - revenue sharing / critical fractile / retailer optimum / conditions ::@:: Referencing $$y = \frac {p - s} {c - s} \frac {c - w} p \,.$$ <p> We see for $0 \le y \le 1$, $w \le c$. That is, the supplier loses money \(or at least not earn any profit\) at first, but gets compensated from revenue sharing. The more money the supplier loses initially, the larger the $y$ as compensation. <p> For the upper bound on markdown such that $0 \le y \le 1$, $$c - w \le p \cdot \frac {c - s} {p - s} \,,$$ which when $s = 0$: $$c - w \le p \cdot \frac c p = c \,.$$ <p> \(__this course__: We also additionally assume $w \ge s$, so $$c - w \le c - s \,,$$ which is a stricter upper bound, thus we have: $s \le w \le c$.\)
  - revenue sharing / expected profit ::@:: The expected profit for the supplier and the retailer can be calculated separately using $(w, y)$, and should add up to the total expected profit. <p> You can always use this equation for the retailer: $$C_u \times \text{expected sales} - C_o \times \text{expected leftover} \,.$$ For the supplier, you need to use a different equation, which should be easy to figure out from $(w, y)$.
  - revenue sharing / intuition ::@:: Using proper $(w, y)$, this contracts allows the _decentralized_ supply chain to achieve the same profit as a _centralized_ supply chain. <p> Intuitively, now both the supplier and the retailer bears the uncertainty. Their incentives are better aligned.
  - revenue sharing / expected profit distribution ::@:: Again, increasing _total_ expected profit does not imply the _individual_ expected profits for the supplier and the retailer both increase \(but at least one must increase\). <p> Within a specific range of $w$ \(and corresponding $y$\), the individual profits both increase.
    - revenue sharing / expected profit distribution / conditions ::@:: For each $s \le w \le c$, plot the supplier and retailer profit. The higher the $w$, the lower corresponding $y$. You should see the retailer profit is anti-correlated with $y$, and the supplier profit is correlated with $y$, which is expected. <p> Then, simply compute the range of $w$ \(and corresponding $y$\) for which both the retailer and supplier profits exceed that of before.
    - revenue sharing / expected profit distribution / practice ::@:: In practice, the $(w, y)$ parameters depend on the relative _bargaining power_ of the retailer and supplier.
  - revenue sharing / other types ::@:: \(__this course__: optional\) option contract, price protection contract, quantity contract, quantity flexibility contract, return contract
    - revenue sharing / other types / return contract ::@:: \(__this course__: optional\) The retailer can return leftovers to the supplier at a price higher than the salvage value.
    - revenue sharing / other types / quantity contract ::@:: \(__this course__: optional\) The retailer receives a discount on all units if ordering quantity exceeds a threshold. This encourages buying more at once.
    - revenue sharing / other types / option contract ::@:: \(__this course__: optional\) The retailer pays the supplier to build capacity and buys an option to purchase later. This motivates increasing capacity before selling season.
    - revenue sharing / other types / quantity flexibility contract ::@:: \(__this course__: optional\) Both the retailer and the supplier agree to buy and sell quantity within a certain range of forecast. This helps with capacity planning under uncertain demand.
    - revenue sharing / other types / price protection contract ::@:: \(__this course__: optional\) The supplier compensates the retailer for any price reduction on remaining inventory. This is used in the technology sectors to mitigate price drops from product updates.
- [questions § week 13 lecture](questions/index.md#week%2013%20lecture)

## week 13 lecture 2

- datetime: 2025-04-30T10:30:00+08:00/2025-04-30T11:50:00+08:00, PT1H20M
- topic: pricing in supply chain
- wholesaling
  - wholesaling / linear demand ::@:: Above, we have considered wholesaling in the context of random demand. We can also instead consider linear demand. That is, demand is a linear function in terms of the price.<p> The derivation and results are similar: wholesaling _cannot_ achieve the supply chain optimum. However, you use first derivative of _retailer profit_ \(or whatever the question wants you to maximize\) instead of the newsvendor model to maximize _retailer profit_ \(or whatever the question wants you to maximize\).
- revenue sharing
  - revenue sharing / linear demand ::@:: Above, we have considered revenue sharing in the context of random demand. We can also instead consider linear demand. That is, demand is a linear function in terms of the price. <p> The derivation and results are similar: revenue sharing can achieve the supply chain optimum. However, you use first derivative of _total profit_ \(or whatever the question wants you to maximize\) instead of the newsvendor model to maximize _total profit_ \(or whatever the question wants you to maximize\).
    - revenue sharing / linear demand / parameters ::@:: Unlike that in random demand, the wholesale price $w$ must equal the production cost $c$. Then $0 \le y \le 1$ can be set arbitrarily. In this special case, $y$ is not only the _revenue_ split, but is also the _profit_ split.
- [behavioral operations management](../../../../general/behavioral%20operations%20management.md) ::@:: \(__this course__: optional\) \(_this_\) examines and takes into consideration human behaviours and emotions when facing complex decision problems. It relates to the behavioral aspects of the use of operations research and operations management. In particular, it focuses on understanding behavior in, with and beyond models.
  - behavioral operations management / traditional economics ::@:: \(__this course__: optional\) people are perfectly rational \(always make optimal choices\), and operates like perfect machines
  - behavioral operations management / behavioral economics ::@:: \(__this course__: optional\) make _less_ unrealistic assumptions about people
  - behavioral operations management / idea ::@:: \(__this course__: optional\) People use simpler decision _heuristics_ based on _limited_ information to make most decisions. People are not perfect machines. Social factors matter. Strategic sophistication is limited.
  - behavioral operations management / judgement biases ::@:: \(__this course__: optional\) availability bias, confirmation bias, representativeness bias, etc. \(with many subtypes underneath\)
- [availability heuristic](../../../../general/availability%20heuristic.md) ::@:: \(__this course__: optional\) The \(_this_\), also known as \(_this_\), is a mental shortcut that relies on immediate examples that come to a given person's mind when evaluating a specific topic, concept, method, or decision. This heuristic, operating on the notion that, if something can be recalled, it must be important, or at least more important than alternative solutions not as readily recalled, is inherently biased toward recently acquired information.
  - availability heuristic / examples ::@:: \(__this course__: optional\) inattention: use information currently being focused and ignore others, e.g. a police chasing a suspect may fail to notice fights along the way <br/> recent and vivid information: believe they are more likely or frequent, e.g. buying earthquake insurance immediately after an earthquake <br/> retrievability: prefer easy to retrieve information, e.g. searching for job-seekers with similar backgrounds to our own first
- [representativeness heuristic](../../../../general/representativeness%20heuristic.md) ::@:: \(__this course__: optional\) The \(_this_\) is used when making judgments about the probability of an event being representational in character and essence of a known prototypical event. <p> The \(_this_\) works by comparing an event to a prototype or stereotype that we already have in mind.
  - representativeness heuristic / examples ::@:: \(__this course__: optional\) base rate neglect: ignore base rate, e.g. likelihood of rare diseases given positive test result <br/> reversion to the mean: failing to predict reversion to the mean in next periods, e.g. tending to overestimate demand if current demand is high
- [confirmation bias](../../../../general/confirmation%20bias.md) ::@:: \(__this course__: optional\) \(_this_\) \(also \(_this_\), \(_this_\) or \(_this_\)\) is the tendency to search for, interpret, favor and recall information in a way that confirms or supports one's prior beliefs or values. People display this bias when they select information that supports their views, ignoring contrary information or when they interpret ambiguous evidence as supporting their existing attitudes.
  - confirmation bias / examples ::@:: \(__this course__: optional\) anchoring bias: search for numbers or information near an anchor until it is plausible, e.g. estimating the price of new car from influential car brands <br/> over-precision: overestimate accuracy or truth of own knowledge, e.g. not putting enough weights on others' advice
- [risk aversion](../../../../general/risk%20aversion.md) ::@:: \(__this course__: optional\) In economics and finance, \(_this_\) is the tendency of people to prefer outcomes with low uncertainty to those outcomes with high uncertainty, even if the average outcome of the latter is equal to or higher in monetary value than the more certain outcome.
  - risk aversion / risk seeking ::@:: \(__this course__: optional\) When gain is reframed as loss instead, _risk seeking_ may occur instead.
  - risk aversion / utility function ::@:: \(__this course__: optional\) A concave function may be used to model risk aversion. That is, utility grows sub-linearly with gain. <p> Conversely, a convex function may be used to model risk seeking. That is, negative utility grows sub-linearly with loss. <p> Combining both, we get a curve that looks like sigmoid function \("S" shape\). The _reference point_ \(point of neither gain nor loss\) matters but is not always obvious.
- [preference](../../../../general/preference.md) ::@:: \(__this course__: optional\) In psychology, economics and philosophy, \(_this_\) is a technical term usually used in relation to choosing between alternatives. For example, someone prefers A over B if they would rather choose A than B. \(_this_\) are central to decision theory because of this relation to behavior.
  - preference / other topics ::@:: \(__this course__: optional\) mental accounting, probability weighting, time preferences, utility function kink
- [questions § week 14 lecture](questions/index.md#week%2014%20lecture)

## week 14 lecture

- datetime: 2025-05-05T10:30:00+08:00/2025-05-05T11:50:00+08:00, PT1H20M
- status: unscheduled, public holiday: Buddha's Birthday

## week 14 lecture 2

- datetime: 2025-05-07T10:30:00+08:00/2025-05-07T11:50:00+08:00, PT1H20M
- topic: behavioral operations management \(optional\), final examination review
- status: attendance
- operations management
  - operations management / intuitions ::@:: coordination: generally improve efficiency/performance in ways similar to pooling, but need to split fairly <br/> description + optimization: understand, then improve <br/> marginal analysis: first derivative test <br/> pooling: generally improve efficiency/performance by reducing variability and/or better matching demand and supply; with diminishing returns <br/> probability: modeling tool <br/> tradeoffs: they are _everywhere_ <br/> variability: generally hurts efficiency/performance
- [§ final examination](#final%20examination)
- [questions § week 14 lecture 2](questions/index.md#week%2014%20lecture%202)

## final examination

- datetime: 2025-05-26T08:30:00+08:00/2025-05-26T10:30:00+08:00, PT2H
- venue: S H Ho Sports Hall, Academic Building
- format
  - calculator: yes
  - cheatsheet: 1 page, A4-sized, double-sided
  - referencing: closed book
  - provided: formulas, necessary tables
  - questions: multiple choice questions ×45
- grades: 43/40 → 43/45
  - statistics
    - timestamps: 2025-06-01T17:03:00+08:00 → 2025-06-07+08:00
    - mean: ? \(provided: 32.4\) → ?
    - standard deviation: ? \(provided: 7.79\) → ?
    - low: ? → ?
    - lower quartile: ? \(provided: 27\) → ?
    - median: ? \(provided: 34\) → ?
    - upper quartile: ? \(provided: 39\) → ?
    - high: ? → ?
    - distribution: ? → ?
- report: \(none\)
- check
  - datetime
    - 2025-06-06T14:00:00+08:00/2025-06-06T15:40:00+08:00, PT1H40M
    - 2025-06-07T10:00:00+08:00/2025-06-07T12:00:00+08:00, PT2H
  - venue: Room 4083, LSKBB
  - report: \(none; did not go\)

> __<big><big>Final Exam Schedule || Solution for HW2</big></big>__
>
> Dear Class,
>
> Hope all is going well with you in the final season. Take care!
>
> As mentioned in the review session, the final exam is scheduled at <span style="background-color: #fbeeb8;">8:30 to 10:30 AM, May 26th at S H Ho Sport Hall</span>. The concrete seating plan will be posted later before exam.
>
> For the exam, please remember to bring your __stationery, student ID card, one A4 double-sided cheat sheet, and any type of calculator__ \(We won't prepare backups, please be sure to have one with you\). No other materials are allowed.
>
> The formula sheet \(already on Canvas\) will be provided by us, so you don't need to print it by yourself. In addition, note that we will not return your cheatsheet after exam. So please make a copy in advance if you would like to keep it. As for the midterm exam, we do not allow early submission in the last 15 minutes of exam.
>
> Besides, I have uploaded the <span style="background-color: #fbeeb8;">solution for homework 2</span> under the "Online Quiz || Homework" module on Canvas. Feel free to check it. Your homework grade will be posted later.
>
> Dont hestitate to reach out if you have any questions. Have a good day!
>
> Best regards,
>
> \[redacted\]

## aftermath

### total

- grades: 96.72/100
  - statistics: \(none\)
