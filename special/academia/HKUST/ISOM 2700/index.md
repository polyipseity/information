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
  - business process modeling / network model ::@:: It is a network of _activities_ (e.g. activity, _buffer_) performed by _resources_ (e.g. capital, labor, material) that transforms _inputs_ (e.g. materials, customers) into _outputs_ (e.g. goods, services). There can be more than one input. There can also be more than one output.
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
  - Gantt chart / finding flow time ::@:: Find the duration a color stays in the diagram.
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

## midterm examination

## final examination

## aftermath

### total
