---
aliases:
  - COMP 3111 software quality assurance
  - COMP 3111 software quality assurances
  - COMP 3111H software quality assurance
  - COMP 3111H software quality assurances
  - software quality assurance
  - software quality assurances
tags:
  - flashcard/active/special/academia/HKUST/COMP_3111H/software_quality_assurance
  - language/in/English
---

# software quality assurance

- COMP 3111H

---

- see: [general/software quality assurance](../../../../general/software%20quality%20assurance.md)

{@{__Software quality assurance__ (__SQA__)}@} is {@{a cross‑cutting discipline applied throughout the software life cycle}@}: from {@{_inception_ through _transition_}@}. In each phase, {@{SQA activities}@} are {@{tailored to support the development workflow}@}—{@{requirements analysis, design, implementation, testing, and project management}@}. <!--SR:!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,274!2025-12-25,4,296-->

## overview

{@{A quality manual}@} must {@{document the organization’s QA procedures}@}, and {@{each project}@} creates a {@{_quality plan_}@} that specifies its {@{most critical design goals and how they will be assessed}@}. Standards for {@{both the development process and its artifacts}@} are essential; they define {@{acceptable practice and embed quality into everyday work}@}. <!--SR:!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296-->

{@{Mechanisms—processes, tools, or checklists}@}—are required to {@{verify compliance with all quality requirements}@}, ensuring {@{deviations are caught early and corrected before release}@}. {@{Formal reviews (requirements, design, code)}@} remain the primary vehicle for {@{detecting defects and enforcing standards}@} throughout development. <!--SR:!2025-12-25,4,274!2025-12-25,4,274!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,294-->

Where practical, {@{metrics}@} highlight {@{anomalous parts of the software}@}. For example, {@{cyclomatic complexity}@} can be computed as {@{$E - N + 2P$}@} where {@{$E$ is edges, $N$ is nodes, and $P$ is connected components}@}, flagging {@{sections that may need deeper inspection}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296-->

{@{Quality software}@} does not {@{emerge by chance}@}; it requires {@{management support, strict adherence to standards}@}, {@{continuous metric collection, and a firm commitment to follow the process}@}—even under {@{pressure}@}. {@{Testing is vital}@} but only {@{one element of a comprehensive QA strategy}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296-->

## purpose and importance

{@{SQA’s purpose}@} is to {@{_ensure that a product meets or exceeds predefined standards_}@} during {@{its entire development cycle}@}. It establishes {@{organizational norms}@} that guide developers toward {@{higher quality outcomes}@} and supports {@{continuous improvement}@} by {@{monitoring compliance and identifying gaps early}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296-->

During {@{_inception_}@}, {@{planning}@} defines {@{goals and standards}@}. In {@{_elaboration_}@}, {@{reviews}@} validate {@{requirements against those standards}@}. {@{_Construction_}@} sees {@{code inspections and unit tests}@}, while {@{_transition_}@} involves {@{system testing and user acceptance}@}. {@{Iterative increments}@} bring {@{incremental quality checks}@} into each cycle. <!--SR:!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296-->

A {@{logarithmic cost curve}@} shows how the {@{expense of fixing a defect rises dramatically}@} as it moves from {@{requirements to field use}@}: {@{$\text{Cost} \propto e^{n}$}@} where {@{$n$ represents the defect’s stage}@}. {@{Early detection during _requirements_}@} is {@{far cheaper than post‑deployment fixes}@}, underscoring why QA {@{emphasizes early reviews and continuous monitoring}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296-->

## aspects

{@{Quality _assurance_}@} defines {@{organizational standards}@} to produce {@{high quality software}@}. {@{Quality _planning_}@} selects and tailors {@{relevant standards for a specific product}@}. {@{Quality _control_}@} verifies that {@{these standards are followed}@} through {@{audits, inspections, and metrics collection}@}. Together they form the {@{_WHAT_ (standards), _HOW_ (methods), and _MONITOR_ (enforcement)}@} of SQA. <!--SR:!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296-->

{@{Quality}@} is achieved at {@{several levels}@}: {@{_product quality_}@} focuses on {@{defect reduction in the final artifact}@}; {@{_project quality_}@} concerns {@{schedule, cost, and scope adherence}@}; {@{_process quality_}@} involves the {@{effectiveness of development practices}@}; {@{_people quality_}@} addresses {@{skills, training, and teamwork}@}. {@{Each level}@} relies on {@{targeted SQA activities}@} to {@{measure and enhance performance}@}, which follows the {@{four interlinked steps}@}: (annotation: 4 items: {@{define → measure → track → feedback}@}). <!--SR:!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296-->

1. _Define_ ::@:: a set of quality attributes that the product must satisfy. <!--SR:!2025-12-25,4,274!2025-12-25,4,296-->
2. _Measure_ ::@:: each attribute so compliance can be quantified. <!--SR:!2025-12-25,4,274!2025-12-25,4,274-->
3. _Track_ ::@:: attribute values over time to evaluate progress toward the goals. <!--SR:!2025-12-25,4,296!2025-12-25,4,296-->
4. _Feedback_ ::@:: the results into future projects, closing the improvement loop. <!--SR:!2025-12-25,4,274!2025-12-25,4,274-->

## activities

{@{SQA}@} encompasses {@{a range of activities that form its foundation}@}: (annotation: 6 items: {@{configuration management, formal reviews, methods & tools}@}, {@{metrics, standards, testing}@}) <!--SR:!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,294!2025-12-25,4,274-->

- _Standards_: ::@:: _foundational_; develop and apply repeatable development norms. <!--SR:!2025-12-25,4,296!2025-12-25,4,296-->
- _Metrics_: ::@:: _foundational_; establish quantitative measures to monitor and improve processes. <!--SR:!2025-12-25,4,296!2025-12-25,4,296-->
- _Methods & Tools_: ::@:: use appropriate techniques for system design and implementation. <!--SR:!2025-12-25,4,296!2025-12-25,4,296-->
- _Formal Reviews_: ::@:: conduct technical inspections at each step for defect discovery and managerial approval. <!--SR:!2025-12-25,4,294!2025-12-25,4,296-->
- _Configuration Management_: ::@:: control changes to ensure traceability and stability. <!--SR:!2025-12-25,4,296!2025-12-25,4,296-->
- _Testing_: ::@:: perform thorough testing to detect defects, though it is _not_ a cure‑all. <!--SR:!2025-12-25,4,296!2025-12-25,4,296-->

{@{These activities}@} collectively support the goal of {@{delivering high‑quality software}@} while continuously {@{refining development practices}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296-->

### standards

{@{A _technical standard_}@} establishes {@{uniform engineering criteria, methods, processes and practices}@}. In {@{software engineering}@} we distinguish {@{two main types}@}: {@{_product standards_}@} define the {@{desired characteristics that every artifact must exhibit to be considered quality}@}; and {@{_process standards_}@} prescribe {@{how work should be carried out so that quality outcomes are reliably produced}@}. {@{Each project}@} decides whether a standard is {@{ignored, used as‑is, modified or newly created}@}. <!--SR:!2025-12-25,4,274!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,274!2025-12-25,4,274!2025-12-25,4,296-->

{@{Standards matter}@} because they: document {@{best practices}@}, helping teams avoid {@{past mistakes}@}; provide {@{a framework for implementing quality control}@}, ensuring that {@{good habits are followed}@}; and guarantee {@{continuity of work}@}, reducing the {@{learning curve when new tasks begin}@}. <!--SR:!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,274-->

### metrics

{@{A _metric_}@} is {@{any measurable quantity related to a software product, process or artifact}@}. {@{Metrics}@} serve {@{two main purposes}@}: {@{_control_}@} – they allow {@{planning and management of effort, time and budget}@}; and {@{_prediction_}@} – they can {@{forecast associated quality attributes}@} (e.g., {@{cyclomatic complexity predicts maintenance ease}@}). Because {@{metrics are objective}@}, they replace {@{subjective judgments in assessing quality}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,274!2025-12-25,4,296-->

An example of {@{a non-software metric}@} is {@{_quality of conformance_}@}, which is {@{the degree to which the design specifications are followed during manufacturing}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,274-->

## product quality

{@{_Product quality_}@} focuses on {@{defect reduction in the final artifact}@}. It may be achieved via {@{design goals, system design metrics, implementation metrics, and reliability approaches}@}. These are used within SQA to {@{monitor design quality, predict maintenance effort, and guide continuous improvement}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296-->

### design goals

{@{A _design goal_}@} is {@{an external quality attribute we wish the system to possess}@}, such as {@{safety, portability or usability}@}. These attributes are {@{_external_ and cannot be measured directly from the code until the system is complete}@}; therefore we {@{infer them during development}@} by observing {@{_internal_ measurable attributes}@} (e.g., {@{lines of code, cyclomatic complexity}@}). {@{Typical internal metrics}@} used to predict {@{external goals}@} include: <!--SR:!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296-->

- maintainability ::@:: → cyclomatic complexity, error messages count, lines of code, number of parameters, etc. <!--SR:!2025-12-25,4,294!2025-12-25,4,296-->
- usability ::@:: → error messages count, user-manual length, etc. <!--SR:!2025-12-25,4,274!2025-12-25,4,274-->

{@{Formulating and validating the relationships}@} between {@{internal metrics and external goals}@} is {@{difficult}@}. {@{Accurate predictions}@} require {@{careful collection, calibration and interpretation}@} of {@{quantitative data}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,294-->

### system design metrics

{@{Design maintainability}@} is inferred from the {@{complexity of a component}@}. {@{Complexity}@} correlates with {@{cohesion, coupling and understandability}@}—attributes that are {@{not directly measurable}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296-->

{@{Two families of metrics}@} help bridge this gap: {@{_structural fan‑in/fan‑out_}@}, which counts {@{how many other components call a given component (fan‑in)}@} and {@{how many components it calls (fan‑out)}@}; and {@{_informational fan‑in/fan‑out_}@}, which augments the counts with {@{the number of parameters and shared data accesses}@}. {@{_Complexity_}@}, defined as: {@{$$\text{complexity} := \text{component-length} \cdot (\text{fan-in} \cdot \text{fan-out})^2 \,,$$}@} has been {@{validated in large operating systems (e.g. Unix)}@} as a predictor of {@{implementation effort}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,274-->

{@{IEEE 982.1‑1988}@} introduces the {@{_Design Structure Quality Index_ (DSQI), a value between 0 and 1}@} that summarizes {@{subsystem coupling, database attributes and classes}@}; a {@{low DSQI}@} signals that {@{further design review is warranted}@}. {@{A complementary metric}@}, {@{the _Software Maturity Index_ (SMI)}@}, tracks {@{how many subsystems change in each release}@}; {@{an SMI approaching 1}@} indicates {@{increasing stability}@}. <!--SR:!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,270!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296-->

### implementation metrics  

{@{Halstead’s software science}@} assigns {@{numeric values to operators and operands}@}: let {@{$n_1$ be unique operators, $n_2$ be unique operands}@}, {@{$N_1$ be total operators, and $N_2$ be total operands}@}. {@{The component length}@} is {@{$L=N_1+N_2$}@}. {@{Volume, difficulty, and their product, effort}@}, is {@{calculated from these}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296-->

- _Volume_: ::@:: $\displaystyle V=L\,\log_{2}(n_1+n_2)$ (bits). <!--SR:!2025-12-25,4,274!2025-12-25,4,296-->
- _Difficulty_: ::@:: $\displaystyle D=\frac{n_1}{2}\,\frac{N_2}{n_2}$. <!--SR:!2025-12-25,4,296!2025-12-25,4,296-->
- _Effort_: ::@:: $\displaystyle E=V\times D$. <!--SR:!2025-12-25,4,296!2025-12-25,4,296-->

{@{McCabe’s cyclomatic complexity}@} counts the {@{number of linearly independent paths through a control‑flow graph}@}; {@{higher values}@} correlate with {@{more defects and greater testing effort}@}. <!--SR:!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,296-->

{@{Other simple metrics}@}—{@{lines of code, identifier length and depth of conditional nesting}@}—also serve as {@{proxies for implementation difficulty}@}. {@{Standards}@} use these metrics to {@{highlight and avoid complex components}@}. <!--SR:!2025-12-25,4,294!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296-->

### reliability approaches

{@{Statistical quality assurance}@} focuses on {@{defect causation}@}: {@{the Pareto principle (80% of defects stem from 20% of causes)}@} guides {@{targeted remediation}@}. {@{The Cleanroom process}@} fuses {@{formal verification with statistical analysis}@} to produce {@{highly reliable software}@}, and {@{program correctness}@} can be {@{proven by logical deduction of assertions that trace requirements to code}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296-->

## project quality

{@{_Project quality_}@} concerns {@{schedule, cost, and scope adherence}@}. {@{Common approaches}@} include {@{formal technical reviews and software configuration management}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,274-->

### formal technical reviews

{@{_Reviews_}@} are the {@{primary method for achieving project quality}@}. During {@{requirements, analysis, and design stages}@}, {@{50‑60% of defects originate from them}@}. {@{Adding code reviews}@} after each stage (including {@{implementation and testing}@}) uncover about {@{_75%_ of those issues}@}. <!--SR:!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296-->

### software configuration management

{@{_Software configuration management_ (SCM)}@} {@{controls, monitors and records changes}@} to all {@{life‑cycle artifacts}@}. In {@{software development}@}, {@{change (e.g. user requests) is certain}@}. By {@{tracking modifications}@}, SCM ensures that {@{every change is auditable}@} and that the correct versions are {@{used throughout development, testing, and deployment}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,294-->

## process quality

{@{_Process quality_}@} involves the {@{effectiveness of development practices}@}. {@{Approaches}@} include {@{ISO&nbsp;9000-3 and SEI Capability Maturity Model (CMM)}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,296-->

Although {@{process design can influence quality}@}, {@{several unique factors}@} dominate: Software is {@{_designed_ rather than manufactured}@}; creativity {@{matters more than mechanical repetition}@}. Individual {@{skill level and experience often outweigh procedural rigor}@}. Resource {@{constraints always degrade quality}@}, regardless of {@{how detailed the process is}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296-->

Thus, while {@{a well‑defined process provides structure}@}, {@{people, tools, and resources}@} frequently have {@{a greater impact on final product quality}@}. Further, {@{a highly specific process}@} rarely {@{transfers between organizations}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296-->

### ISO 9000‑3

{@{ISO 9000‑3}@} helps clients evaluate {@{a software organisation’s process management capability}@}. The standard extends {@{ISO 9001}@}, which requires {@{a documented quality system—a _quality manual_}@} that defines {@{the organisation’s processes and procedures}@}. {@{ISO 9000‑3}@} specifies how this quality system should be {@{woven through every phase of software development}@}, providing {@{generic procedures that support a robust quality process}@}. The standard is {@{divided into three main parts}@}: {@{Management Responsibility, Quality Life Cycle Activities, and Supporting Activities}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,294!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,270-->

{@{_Quality System Framework_}@} defines {@{core responsibilities and activities}@}. {@{Management responsibility}@} ensures {@{leadership supports quality goals}@}. {@{A quality system}@} is established to ensure {@{consistent processes}@}. {@{Internal audits}@} check that {@{the system works as planned}@}. {@{Corrective action}@} is taken when {@{problems are found to prevent recurrence}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296-->

{@{_Quality Life Cycle Activities_}@} covers key steps in {@{delivering a product or service from start to finish}@}. These include {@{reviewing contracts, defining customer needs, planning development}@}, {@{creating quality records, designing and implementing solutions, testing}@}, {@{getting customer approval, delivering the product, and providing ongoing maintenance}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296-->

{@{_Quality System Supporting Activities_}@} are {@{behind-the-scenes processes that support quality}@}. They include {@{managing changes to products (configuration management), controlling documents}@}, {@{recording quality data, measuring performance, using standard rules and tools}@}, {@{managing purchases, handling software components, and training staff}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,274-->

### SEI Capability Maturity Model

SEI CMM is a framework for assessing and improving software development processes.  Five maturity levels describe increasing process rigor: (annotation: 5 items: initial → repeatable → defined → managed → optimizing)

1. Level 1 – _Initial_ ::@:: – ad‑hoc, no formal procedures or estimates. <!--SR:!2025-12-25,4,296!2025-12-25,4,296-->
    - Level 1 – _initial_ / key processes ::@:: none. <!--SR:!2025-12-25,4,296!2025-12-25,4,296-->
2. Level 2 – _Repeatable_ ::@:: – basic controls; intuitive methods and some management oversight. <!--SR:!2025-12-25,4,296!2025-12-25,4,296-->
    - Level 2 – _repeatable_ / key processes ::@:: requirements management, project planning, tracking & oversight, subcontract management, quality assurance, configuration management. <!--SR:!2025-12-25,4,296!2025-12-25,4,296-->
3. Level 3 – _Defined_ ::@:: – processes are documented, institutionalised, and staff receive training. <!--SR:!2025-12-25,4,274!2025-12-25,4,296-->
    - Level 3 – _defined_ / key processes ::@:: organisational process focus/definition, training program, integrated software management, product engineering, inter‑group coordination, peer reviews. <!--SR:!2025-12-25,4,296!2025-12-25,4,296-->
4. Level 4 – _Managed_ ::@:: – quantitative metrics track process performance; a database of data is maintained. <!--SR:!2025-12-25,4,274!2025-12-25,4,296-->
    - Level 4 – _managed_ / key processes ::@:: quantitative process management, quality management. <!--SR:!2025-12-25,4,296!2025-12-25,4,296-->
5. Level 5 – _Optimizing_ ::@:: – continuous improvement via defect‑cause analysis and prevention. <!--SR:!2025-12-25,4,274!2025-12-25,4,274-->
    - Level 5 – _optimizing_ / key processes ::@:: fault prevention, technology change management, process change management. <!--SR:!2025-12-25,4,294!2025-12-25,4,296-->

{@{Typical high‑performing organizations}@} reach {@{only Level 3–4}@} on the SEI CMM model; {@{achieving Level 5}@} requires {@{a sustained culture of optimisation and data‑driven decision making}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296-->

## people quality

{@{_People quality_}@} addresses {@{skills, training, and teamwork}@}. Approaches include {@{People Capability Maturity Model (PCMM)}@}. <!--SR:!2025-12-25,4,296!2025-12-25,4,274!2025-12-25,4,274-->

### People Capability Maturity Model

{@{The People Capability Maturity Model (PCMM)}@} {@{evaluates and enhances the knowledge and skill base}@} of {@{an organization’s workforce}@}. It links {@{training, talent management, and performance measurement}@} to {@{overall business objectives}@}. <!--SR:!2025-12-25,4,274!2025-12-25,4,274!2025-12-25,4,296!2025-12-25,4,296!2025-12-25,4,296-->

1. Level 1 – _Initial_ ::@:: No formal training or technical guidance is offered. Talent is not viewed as a strategic asset; employee skills remain static and organizational loyalty is weak. <!--SR:!2025-12-25,4,296!2025-12-25,4,274-->
2. Level 2 – _Repeatable_ ::@:: Basic work practices are defined, and the organization begins to recruit, develop, and retain staff. Targeted training fills identified skill gaps, while performance is formally assessed. <!--SR:!2025-12-25,4,296!2025-12-25,4,274-->
3. Level 3 – _Defined_ ::@:: Work processes are tailored to business needs. A strategic talent plan locates critical skills, and compensation aligns with expertise, ensuring that people roles support organizational goals. <!--SR:!2025-12-25,4,296!2025-12-25,4,296-->
4. Level 4 – _Managed_ ::@:: The focus shifts to raising competence in key areas through mentoring, team‑building, and quantitative competency targets. Effectiveness of work practices is measured against these goals. <!--SR:!2025-12-25,4,274!2025-12-25,4,296-->
5. Level 5 – _Optimizing_ ::@:: Continuous improvement drives the development of both individual and team skills. Best practices are adopted organization‑wide, creating a culture that adapts rapidly to new challenges. <!--SR:!2025-12-25,4,274!2025-12-25,4,296-->

{@{Typical high‑performing organizations}@} reach {@{only Level 3–4}@} on the PCMM model; {@{achieving Level 5}@} requires {@{a sustained culture of optimisation and data‑driven decision making}@}.
