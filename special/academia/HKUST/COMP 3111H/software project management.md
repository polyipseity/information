---
aliases:
  - COMP 3111 software project management
  - COMP 3111H software project management
  - software project management
tags:
  - flashcard/active/special/academia/HKUST/COMP_3111H/software_project_management
  - language/in/English
---

# software project management

- COMP 3111H

---

- see: [general/software project management](../../../../general/software%20project%20management.md)

{@{__Software project management__}@} is {@{the process of planning and leading software projects}@}. It is {@{a sub-discipline of project management}@} in which {@{software projects are planned, implemented, monitored and controlled}@}.

## purpose

{@{_Project management_}@} spans {@{all four phases of the unified process}@}: {@{inception → elaboration → construction → transition}@}.  Each phase triggers {@{distinct engineering workflows}@}: {@{requirements analysis, design, implementation, testing}@}; and {@{management workflows}@} such as {@{quality assurance and project control}@}.

{@{Software projects}@} begin with {@{_incomplete knowledge_}@}: {@{uncertain requirements, limited people, scarce resources (time, money, skills)}@}.  In {@{project management}@}, managers must decide on: {@{features to deliver, tasks required, build‑or‑buy options, effort estimates}@}, {@{resource allocation, schedules, risk mitigation, and tool selection}@}. The process is {@{continuous}@}: {@{_plan the work_ and _work the plan_}@}. {@{Failing to iterate on the plan}@} or {@{neglecting early estimates}@} typically spirals into {@{project failure}@}.

{@{Continuous monitoring}@} compares {@{planned vs. actual progress}@}. {@{Key control activities}@} include {@{variance analysis, trend evaluation, and corrective actions}@} to keep the project {@{on schedule, within budget, and meeting quality goals}@}. The quote "{@{_Manage the process, don't let the process manage you._}@}" by {@{Khoa Nguyen}@} reminds managers to keep {@{control over the development process}@} rather than allowing {@{the process itself to dictate their actions}@}. It stresses that {@{effective software management}@} requires {@{active oversight and decision‑making}@}, not {@{passive and rigid adherence to procedures}@}.

## software development plan

{@{The _software development plan_ (SDP)}@} is {@{the master document}@} that defines {@{project scope and governs how the effort will be managed}@}. It specifies {@{objectives, constraints, deliverables, schedules}@}, {@{resources, risk mitigation strategies, and quality assurance requirements}@}, thereby serving as {@{the blueprint for the entire development cycle}@}. A SDP includes: (annotation: 9 items: {@{deliverables, development environment, work breakdown structure}@}, {@{staffing and organization, schedules, estimates}@}, {@{metrics plan, risk planning, time-phased budget}@}).

1. _Deliverables_ ::@:: – tangible outputs of each phase.  
2. _Development Environment_ ::@:: – tools, platforms, standards.  
3. _Work Breakdown Structure_ (WBS) ::@:: – hierarchical decomposition of tasks.  
4. _Staffing and Organization_ ::@:: – roles and responsibilities.  
5. _Schedules_ ::@:: – time‑phased milestones and activities.  
6. _Estimates_ ::@:: – effort, cost, and size predictions.  
7. _Metrics Plan_ ::@:: – measurement strategy for quality and progress.  
8. _Risk Planning_ ::@:: – identification, analysis, mitigation.  
9. _Time-phased Budget_ ::@:: – allocation of financial resources over time.

{@{Developing the SDP}@} is a {@{constrained-optimization problem}@}. Because {@{data are incomplete}@}—{@{requirements may be ambiguous, resource availability uncertain, and technical complexity difficult to estimate}@}—the plan must {@{balance competing goals (budget, schedule, quality)}@} while satisfying {@{contractual and organizational constraints}@}.

{@{Inputs from people are synthesized}@} to produce a {@{coherent SDP}@} that guides all subsequent {@{planning, execution, monitoring, and control activities}@}. They include {@{the _development manager_}@} who {@{organizes tasks, allocates budget, and coordinates the team}@}; {@{an _experienced system architect_}@} who {@{designs the top-level structure and provides estimates of technical size}@}; and {@{a _domain expert or user representative_}@} who {@{supplies deep knowledge of functional requirements and business context}@}.

## deliverables

{@{The SDP}@} defines {@{_what_ is produced, _for whom_, and _when_}@}. It includes {@{client-directed items, process artifacts, internal deliverables, and services}@}.

{@{_Client-directed items_}@} are {@{tangible products}@} such as {@{executable code, installation scripts, tutorials}@}, {@{user manuals, help files, and licensing tools}@}. {@{_Process artifacts_}@} {@{capture the work itself}@}: {@{requirements documents, analysis and design specifications, source code and object-design files}@}.  {@{_Internal deliverables_}@} of {@{lasting value to the organization}@} include {@{reusable libraries, build scripts and test repositories}@}.  {@{_Services_}@} that {@{augment the core product}@}—{@{training, installation, customization, consulting, or on-site support}@}—are also listed in {@{the SDP}@}.  

These classifications guide {@{staffing decisions and team structure}@}: {@{larger client products}@} may require {@{dedicated delivery teams}@}, whereas {@{internal artifacts}@} can be handled by {@{cross-functional developers}@}.

## development environment

{@{The SDP}@} specifies the {@{_hardware_ and _software_ tools}@} (which {@{_support_ development _processes_}@} but do not {@{_replace_ them}@}) that will {@{support the project lifecycle}@}.  A tool is only useful if it {@{enhances an already well-understood process}@}; it must {@{improve efficiency without adding complexity}@}.

When evaluating a support system, consider {@{lifecycle coverage}@} ({@{UML modeling, oversight, architectural control, collaboration}@}, {@{developer productivity, library integration, documentation}@}) and {@{adoption risk}@} ({@{external cost, internal cost, time loss}@}, {@{product instability, investment protection}@}). {@{Tool selection}@} is thus an {@{optimization problem}@} balancing {@{functional fit against financial and temporal impact}@}.

## work-breakdown structure

{@{The SDP}@} decomposes the project into {@{tasks and sub-tasks}@} to enable {@{precise planning, estimation, tracking and budgeting}@}.  {@{A typical work-breakdown structure (WBS)}@} is {@{a tree}@}: {@{each leaf node}@} represents {@{an actionable activity with a clear start, end, owner and cost estimate}@}.  {@{Estimates}@} are {@{rolled up from leaves to give total effort and budget figures}@}.  

For {@{effective monitoring}@} the WBS must satisfy: {@{_plannability_}@}: tasks have {@{defined durations}@}; {@{_assignability_}@}: each task can be {@{allocated to an individual or team}@}; {@{_trackability_}@}: progress is {@{measurable against a schedule and cost baseline}@}; and {@{_appropriate granularity_}@}: neither {@{too fine (unmanageable) nor too coarse (inaccurate)}@}.  

{@{An example hierarchy}@} might list {@{phases—Inception, Elaboration, Construction, Transition}@}—each subdivided into {@{Build, Requirements, Design, Implementation}@}, {@{testing, Packaging, and Installation}@} activities.

## staffing and organization

{@{The SDP}@} specifies a {@{hierarchical structure}@} that {@{assigns roles and responsibilities, sets staff numbers per role, and forms modular teams}@}. Each team is responsible for {@{one or more subsystems}@}; {@{a PIC (person-in-charge)}@} is identified for {@{each subsystem and for the overall system}@}. {@{The key to success}@} is achieving {@{an optimal level of communication while limiting cross-team interaction}@}.

## schedules

{@{The schedule}@} contains {@{task ordering (dependencies), time estimates (start, duration), resource assignments (people, hardware, software)}@}, {@{milestones, deliverables, and a critical path}@} that determines {@{total duration}@}. {@{Three schedule levels}@} are maintained: (annotation: 3 items: {@{master, macro, micro}@})

- _Master schedule_ ::@:: – rigid, for management and client communication.  
- _Macro‑schedule_ ::@:: – semi‑rigid, used daily by project managers.  
- _Micro‑schedule_ ::@:: – flexible, tailored to team operations.

{@{Gantt, PERT and burndown charts}@} are {@{the most common visual tools}@}.

### Gantt chart

{@{A Gantt chart}@} visualises {@{the project schedule as a horizontal bar chart}@}. {@{Each task }@}is represented by {@{a bar whose length corresponds to its duration}@} and whose position reflects {@{its start date relative to the overall timeline}@}. Bars can be {@{colour-coded for status (planned, in progress, completed)}@} and {@{overlapped to show parallel work}@}. {@{Dependencies}@} are often indicated with {@{arrows or linking lines between bars}@}.

{@{Gantt charts}@} provide an {@{at-a-glance view of resource utilisation and potential schedule conflicts}@}. It cannot, however, provide {@{critical path activity}@}, and {@{a PERT chart}@} is used for this purpose instead.

### PERT chart

{@{A Program Evaluation and Review Technique (PERT) chart}@} is {@{a network diagram of tasks with durations}@}. {@{Each _node_}@} represents {@{a milestone (a point in time)}@}; {@{_edges_ (arrows)}@} denote {@{tasks or precedence}@} and is weighted by {@{the task duration}@}. {@{Dummy tasks (edges with zero weight)}@} may be {@{added so every in-between node has at least one incoming and one outgoing edge}@}.

{@{The critical path}@} is the {@{longest time-path from start to finish}@}; its length equals the {@{project duration}@}. {@{Slack}@} (difference between {@{earliest and latest completion times}@}) indicates how much a {@{milestone (node)}@} can be {@{delayed without affecting the overall schedule}@}, which provides {@{buffer information for risk management}@}.

The {@{PERT chart}@} may be accompanied by {@{two tables}@}. The {@{_task table_}@} lists each {@{task (edge)}@}. Each row contains {@{the task name, its edge ID in the chart, its duration, and its precedent tasks}@}. The {@{_node table_}@} lists each {@{milestone (node)}@}. Each row contains the {@{node ID in the chart (possibly labeled with a task preceding it)}@}, {@{its earliest completion time (ECT), its latest completion time (LCT)}@}, and {@{its slack (the difference between ECT and LCT)}@}.

## estimates

{@{The SDP}@} contains {@{quantitative predictions}@} for {@{size, effort, duration, productivity and cost}@}.  {@{Size}@} may be expressed as {@{LOC, number of subsystems or classes}@}; {@{effort}@} is {@{persons×time}@}; {@{duration}@} is {@{months to delivery}@}; {@{productivity}@} is {@{size per person-month}@}; {@{cost}@} follows from {@{labour rates}@}.

{@{Estimates}@} are derived from {@{experience, historical data, analytic models or a combination}@}.  They carry {@{risk}@} but the {@{risk can be reduced}@} by defining {@{scope early, using past project metrics}@} and breaking {@{the work into small parts that can be summed}@}.

{@{Metrics used for estimating}@} includes: (annotation: 6 items: {@{function-oriented, human-oriented, productivity}@}, {@{quality, sized-oriented, technical}@})

- _technical metrics_ ::@:: focus on software properties (e.g., complexity).  
- _quality metrics_ ::@:: measure conformity to requirements (errors per LOC).  
- _productivity metrics_ ::@:: evaluate output from the engineering process.  
- _size‑oriented metrics_ ::@:: directly count development artifacts (LOC, KLOC).  
- _function‑oriented metrics_ ::@:: assess functional characteristics (function points).  
- _human‑oriented metrics_ ::@:: capture people factors and tool effectiveness.

### function-point counting

{@{A weighted sum of project elements}@} gives {@{a _count-total_ value}@}: {@{$$\text{count-total} = \sum w_i \times \text{count}_i$$}@} where {@{$w_i$ is the weighting factor for each element}@} such as {@{user inputs, outputs, inquiries, files and interfaces}@}. Then, this count-total is {@{multiplied by a multiplier to give a _function-point_ (FP) value}@}: {@{$$\text{FP} = \text{count-total} \cdot (0.65 + 0.01 \cdot F_i)$$}@} where {@{$F_i$ are answers to questions about the system complexity}@}, ranging {@{from 0 (no influence) to 5 (essential)}@}. The FP number feeds into {@{productivity, quality, cost and documentation estimates}@}:

- _Productivity_ ::@:: = FP / effort  
- _Quality_ ::@:: = errors / FP  
- _Cost_ ::@:: = \$ / FP  
- _Documentation_ ::@:: = pages / FP

It improves upon using {@{size (e.g. KLOC in place of FP, and where all data comes from "similar" previous projects)}@} or {@{_Delphi technique_ (average 3 or more previous estimates from independent experts)}@}, which use {@{a previously completed, similar project as a template}@} and {@{adjust for differences}@}, as {@{this adjustment may not be perfect}@}.

### PERT estimation

{@{Experts}@} give {@{optimistic ($o$), most likely ($m$) and pessimistic ($p$) estimates}@}.  The expected value is  {@{$$E = \frac{o + 4m + p}{6}$$}@} and the standard deviation {@{$$\sigma = \frac{p - o}{6}.$$}@} {@{The true size lies within $E \pm \sigma$}@} about {@{68% of the time}@}.

### planning poker

{@{A team leader}@} provides {@{overview of a feature to be estimated}@}. {@{The team estimates the feature}@} by {@{playing numbered cards face-down}@}. While estimating, team members may {@{clarify assumptions and risks}@}, but {@{no numbers are mentioned}@}.  Finally, all cards are {@{revealed, then discussed}@}.

### parametric models

{@{Empirical formulas}@} predict {@{effort (E) or duration (D) from measurable inputs}@}.  Examples include {@{_COCOMO_ (Constructive Cost Model) and the _Putnam Estimation Model_}@}.  They require {@{accurate input data}@} but can be {@{highly reliable when calibrated with local project history}@}.

### estimation risk mitigation

Verify that the team has {@{experience on comparable systems}@}.  Collect {@{detailed metrics (FP, LOC, error counts)}@} from previous projects to {@{calibrate models}@}.  Perform {@{multiple estimation methods}@} and {@{cross-check results}@}.  Recognise that {@{incomplete requirements inflate uncertainty}@}; aim for {@{clear scope before estimating}@}.

{@{A well-calibrated cost model}@} should predict {@{within 20% of actual costs}@} in roughly {@{70% of cases on the same set of projects}@}.

## metrics plan

{@{The SDP}@} defines {@{which metrics to track and the procedures that will gather them}@}.  {@{Typical project-management metrics}@} relate to {@{size: use cases, classes, lines of code}@}.  {@{Comparing planned sizes with current values}@} reveals {@{progress—how much of the planned work is finished}@}—and {@{stability—how much change has occurred in requirements or estimates}@}.

## risk planning

{@{Risk planning}@} anticipates {@{problems before they arise}@}, assesses their {@{likelihood and impact}@}, and devises {@{cost-effective contingency actions}@}.  It is an element of {@{preventive management}@}: {@{identify a risk, plan an action to mitigate it, and execute that action before the problem materialises}@}.  {@{Effective risk planning}@} demonstrates {@{managerial competence}@}.

## time-phased budget

{@{The SDP}@} allocates {@{funds over time}@}, tying each {@{expenditure level to expected accomplishments}@}.  {@{Manpower}@} usually {@{dominates cost in software projects}@}; each {@{WBS item}@} receives a {@{cost based on duration, staffing mix, and staff rates}@}.  {@{Additional costs—training, licenses, hardware}@}—and {@{a reserve (10–15%)}@} are also included.  

{@{Monitoring budget}@} requires {@{regular comparison of planned versus actual spending and completion}@}.  {@{Tracking these variances}@} enables {@{timely corrective action}@}.

## project tracking and control  

{@{Software projects}@} {@{slip gradually}@}; {@{continuous, unobtrusive monitoring}@} keeps them on target.  The main aim is to verify that the {@{schedule and budget remain within acceptable limits}@}. {@{Simply adding people to catch up with the schedule}@} does not work: {@{Adding people to a late project usually makes it complete later}@}, as famously noted in {@{_The Mythical Man-Month_ by Frederick P. Brooks}@}.

{@{Change is unavoidable}@}, so {@{a disciplined _software change management_ (SCM) process}@} is essential.

### project tracking and control methods

{@{These practices}@} together create {@{a feedback loop}@} that keeps the project {@{aligned with its commitments}@} while allowing {@{controlled change through SCM}@}:

- Periodic status meetings ::@:: —daily, weekly or monthly—provide an official forum for updates.  
- Project reviews ::@:: evaluate the outcomes of each meeting and identify corrective actions.  
- Key performance indicators (KPIs) and milestones ::@:: are checked against planned dates to spot delays early.  
- Budget versus forecast ::@:: is compared continually; any variance triggers a reassessment of resource allocation.  
- Informal conversations ::@:: with team members surface subjective insights into progress, risks and emerging problems.
