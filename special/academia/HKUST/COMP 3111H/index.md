---
aliases:
  - COMP 3111H
  - COMP 3111H index
  - COMP3111H
  - COMP3111H index
  - HKUST COMP 3111H
  - HKUST COMP 3111H index
  - HKUST COMP3111H
  - HKUST COMP3111H index
  - Honors Software Engineering
  - Honors Software Engineering index
tags:
  - flashcard/active/special/academia/HKUST/COMP_3111H
  - function/index
  - language/in/English
---

# index

- HKUST COMP 3111H
- name: Honors Software Engineering

The content is in teaching order.

- grading
  - scheme
    - pre-lecture quizzes: 5%
    - in-class practice, exercises, assignments: 5%
    - labs: 10%
    - project: 20%
    - midterm examination \(midterm quiz\): 20%
    - final examination: 40%

## children

- [assignments](assignments/index.md)
- [questions](questions.md)

## week 1 pre-lecture

- topic: introduction; complexity of software development; handling complexity; software engineering
- [software engineering](../../../../general/software%20engineering.md) ::@:: It is a branch of both computer science and engineering focused on designing, developing, testing, and maintaining software applications. It involves applying engineering principles and computer programming expertise to develop software systems that meet user needs.
- [source lines of code](../../../../general/source%20lines%20of%20code.md) \(SLOC\) ::@:: It is a software metric used to measure the size of a computer program by counting the number of lines in the text of the program's source code.
  - source lines of code / acronyms ::@:: LLOC: logical lines of code; logical SLOC <br/> LOC: lines of code; physical SLOC <br/> MLOC: million lines of code <br/> SLOC: source lines of code
  - source lines of code / examples ::@:: Rome: Total War &lt; Boeing 787 &lt; F-35 Fighter Jet &lt; Windows 7 &lt; Windows 10 &lt; Facebook &lt; Mac OS X &lt; luxury passenger car
  - source lines of code / effort ::@:: Effort is not _linearly_ proportional to source lines of code!!
- [software maintenance](../../../../general/software%20maintenance.md) ::@:: It is the modification of software after delivery. <p> It is often considered lower skilled and less rewarding than new development. As such, it is a common target for outsourcing or offshoring.
  - software maintenance / complexity ::@:: It can be complex. Indeed, given the large amount of existing software, it uses the most time of most developers.
- [programming complexity](../../../../general/programming%20complexity.md) ::@:: It is a term that includes software properties that affect internal interactions.
  - programming complexity / sources ::@:: application domain, communication, management, tools
    - programming complexity / sources / application domain ::@:: A problem is often _complex_ and outside the domain of most developers \(i.e. not _domain experts_\).
    - programming complexity / sources / communication ::@:: Clients and developers have different _background_, _vocabulary_, etc. which is made worse by _ambiguity_ of human languages.
    - programming complexity / sources / management ::@:: _Dividing_ a project and _reassembling_ it is difficult. _Coordination_ between different _parts_ and _people_ is also difficult.
    - programming complexity / sources / tools ::@:: Creating useful _tools_ for software development is also complex. Indeed, creating the tools themselves also require software engineering.
  - programming complexity / problems ::@:: development, quality
    - programming complexity / problems / quality ::@:: abandonment \(London Stock Exchange; after 5 years of development\), inflexible, unreliable \(Ariane 5 \(rocket\)\), unsafe \(London Ambulance Service; fell twice in 1992\), etc.
      - programming complexity / problems / quality / examples ::@:: A small software update to Amazon, a large and complex website, caused \$2.8 million in lost revenue.
- [Ariane 5](../../../../general/Ariane%205.md) ::@:: It is a retired European heavy-lift space launch vehicle operated by Arianespace for the European Space Agency \(ESA\).
  - Ariane 5 / notable launches
    - Ariane 5 / notable launches / first test flight ::@:: Ariane 5's first test flight \(Ariane 5 Flight 501\) on 4 June 1996 failed, with the rocket self-destructing 37 seconds after launch because of a malfunction in the control software.
      - Ariane 5 / notable launches / first test flight / cause ::@:: A data conversion from 64-bit floating-point value to 16-bit signed integer value to be stored in a variable representing horizontal bias caused a processor trap \(operand error\) because the floating-point value was too large to be represented by a 16-bit signed integer.
- programming complexity
  - programming complexity / problems
    - programming complexity / problems / development ::@:: does not meet user requirements, difficult to measure progress, over budget, over time, etc.
      - programming complexity / problems / development / statistics ::@:: \(2012\) For _large_ software projects: deliver less value &gt; over budget &gt; company threatening &gt; over time &gt; etc.
  - programming complexity / mitigations ::@:: There are many desirable _characteristics_ considered part of quality. It is impossible and unnecessary to achieve all of them. <p> Instead, we should under the client's _goals_ and _prioritize_ certain characteristics. This reduces complexity somewhat.
    - programming complexity / mitigations / characteristics ::@:: correct, efficient, evolvable, interoperable, maintainable, portable, productive, reliable, repairable, reusable, robust, timely, usable, verifiable, visible, etc.
- [modular programming](../../../../general/modular%20programming.md) ::@:: It is a programming paradigm that emphasizes organizing the functions of a codebase into independent modules – each providing an aspect of a computer program in its entirety without providing other aspects.
  - modular programming / motivation ::@:: Humans cannot understand things that are too _complex_. Often, we break down a complex systems into _modules_, parts of a system that makes sense to _consider separately_ and interact with other modules. This is known as _divide and conquer_.
  - modular programming / module ::@:: It is a part of a system that can be _considered separately_. To model _interactions_ with other modules, they are limited to _interfaces_, which _abstracts_ and _encapsulates_ a module via _information hiding_.
    - modular programming / module / abstraction ::@:: The internals of a module are hidden away. Interaction is defined via its interface only. The usage of the module by other modules can be understood by looking at its interface only \(ideally\). This reduces complexity of the system.
    - modular programming / module / encapsulation ::@:: When we want to modify a module, we only need to modify the module without changing other modules \(ideally\). The internals of a module can be changed without affecting other modules \(ideally\). This reduces maintenance burden.
  - modular programming / advantages ::@:: bug reduction, _incremental_ development, maintainability, productive teams, reusability <p> This makes software development _more predictable_, leading to better cost and time estimation.
- [engineer](../../../../general/engineer.md) ::@:: It is a practitioner of engineering. <p> They apply ingenuity, mathematics, and scientific knowledge to develop _solutions_ \(e.g. materials, structures, _systems_\) for specific _problems_. They need consider _limitations_ from cost, practicality, regulation, and safety.
  - engineer / vs. scientist ::@:: The former builds things for _quality_ \(e.g. avoiding engineering failures\) while the latter builds things for discovering _new_ things \(e.g. scientific breakthroughs\).
- software engineering
  - software engineering / vs. computer scientist ::@:: The former studies practices and principles for building _quality_ systems while the latter studies _algorithms_ and _foundations_ of computing. <p> The former considers the _context_ to use the appropriate technologies \(e.g. frameworks\) according to their _characteristics_, while the latter focuses on _basic_ technologies, i.e. algorithms and foundations of computing.
  - software engineering / jobs ::@:: Coding or programming is only "programming-in-the-small", which includes implementation, validating user inputs, etc. <p> Software engineering is "programming-in-the-large", which includes communication, execution, etc.
    - software engineering / jobs / communication ::@:: communication, documentation, teamwork, translating user requirements, etc.
    - software engineering / jobs / execution ::@:: choose design alternatives, modeling \(at different abstraction levels\), use and apply, etc.
  - software engineering / characteristics ::@:: disciplined \(engineering principles\), multi-person, multi-version, problem solving \(solves real user problems\), quality \(e.g. economic, efficient, reliable, etc.\)
  - software engineering / activities ::@:: knowledge acquisition, modeling, problem solving, rationale management, etc.
    - software engineering / activities / modeling ::@:: Model user requirement. Model the system to be built.
    - software engineering / activities / problem solving ::@:: _Systematically_ \(but not _algorithmically_ as there are changes\) find an appropriate solution according to the user requirement. Note that user requirements can _change_ or be clarified over time.
    - software engineering / activities / knowledge acquisition ::@:: Knowledge about the problem needs to be learnt on the go. It may also need to be _unlearnt_ due to changing requirements or misunderstandings. You may even need to _start over_.
    - software engineering / activities / rationale management ::@:: As acquired knowledge, solutions \(new technologies\), user requirements _change_, we need to _revisit_ decisions and their rationale.
- quiz: [quiz 1](questions/quiz%201.md)

## week 1 lecture

- datetime: 2025-09-03T12:30:00+08:00/2025-09-03T14:20:00+08:00, PT1H50M
- topic: logistics; introduction
- COMP 3111H
  - COMP 3111H / logistics
  - COMP 3111H / textbook ::@:: _Object-Oriented Software Engineering: Using UML, Patterns, and Java, 3/E_, B. Bruegge and A.H. Dutoit, Pearson Education, Inc., 2010.
  - COMP 3111H / tools ::@:: Git, GitHub, Java, <https://app.diagrams.net/>; lab notes, web resources
  - COMP 3111H / grading
  - COMP 3111H / objectives ::@:: _disciplined_ approach to software development, theoretical and practical aspects of software engineering
  - COMP 3111H / course intended learning outcomes \(CILO\)
  - COMP 3111H / motivation ::@:: communication, design, leadership, modeling, project management, etc.
  - COMP 3111H / syllabus ::@:: introduction → modeling language → development approaches → development activities → project management
  - COMP 3111H / rules
  - COMP 3111H / project ::2:: specification \(from system requirements\) → implementation and testing
- [§ week 1 pre-lecture](#week%201%20pre%20lecture)
- [questions § week 1 lecture](questions/index.md#week%201%20lecture)

## week 1 lab

- datetime: 2025-09-04T18:00:00+08:00/2025-09-04T19:50:00+08:00, PT1H50M
- status: unscheduled

---

> Dear COMP3111 Students,
>
> Welcome aboard! The Canvas page for COMP3111 is now available here: <br/>
> 👉 \[redacted\]
>
> Just a quick reminder: there will be __no lab in Week 1__. I look forward to seeing you all in the lecture tomorrow.
>
> To stay connected and receive quick updates, please also join our course Telegram group: <br/>
> 👉 \[redacted\]
>
> Cheers, <br/>
> \[redacted\]

## week 1 extra lab

- topic: LLM assistant in IntelliJ IDEA
- status: optional
- COMP 3111H
  - COMP 3111H / lab extra ::@:: LLM assistant in IntelliJ IDEA
    - COMP 3111H / lab extra / objectives ::@:: Students are expected to become comfortable using the "Continue" plugin in IntelliJ IDEA alongside the Groq LLM service.
    - COMP 3111H / lab extra / tools ::@:: The development stack is a modern Java SE environment \(JDK 21\) running on IntelliJ IDEA 2024, with access to the free Llama‑based models hosted at Groq \(<https://groq.com/>\) and the Continue API for code generation and understanding.
    - COMP 3111H / lab extra / exercises ::@:: setup Groq & Continue; generate login screen in JavaFX; understand generated code, generate test
    - COMP 3111H / lab extra / Groq API keys ::@:: Create a Groq account, explore available models in the Playground, then generate an API key from "API Keys". This key is one‑time visible; store it securely. <p> As of 2025, Groq is unavailable in Hong Kong.
    - COMP 3111H / lab extra / models ::@:: examples: Llama3.1 70b Chat, etc.
    - COMP 3111H / lab extra / prompts ::@:: You can prompt it to edit code, explain code, generate docs, generate tests, and etc. Take care to use it with some _human oversight_!
      - COMP 3111H / lab extra / prompts / edit ::@:: examples: <p> Change the GUI to a login screen that requires the user to input 'Username' and 'Password', and there should only be one button 'Login'. <br/> Change login to successful only when the username is equal to the password, and fail in another case.
      - COMP 3111H / lab extra / prompts / explain ::@:: examples: <p> Carefully read and understand the code, clearly describe the functionality of both classes and explain the method of each class.
      - COMP 3111H / lab extra / prompts / docs ::@:: Add Javadoc descriptions to the classes and methods. Also add comments to the implementation details for high‑level explanation.

## week 2 pre-lecture

- topic: modeling; unified modeling language; class diagram; association; aggregation; association class; generalization; UML summary
- [Unified Modeling Language](../../../../general/Unified%20Modeling%20Language.md) \(UML\) ::@:: It is a general-purpose, object-oriented, visual modeling language that provides a way to visualize the architecture and design of a system; like a blueprint. <p> It makes us think about the world in a certain way.
  - Unified Model Language / characteristics ::@:: current best practices, independent of software development methodology, industry standard \(especially for object-oriented systems, but can be used for non-OO systems as well\), visual modeling language
  - Unified Model Language / idea ::@:: A \(software\) system can modeled as a _collection_ of _collaborating_ objects.
  - Unified Model Language / building blocks ::@:: diagrams, relations, things, etc.
  - Unified Model Language / mechanisms ::@:: adornments, division, extension, specification, etc.
  - Unified Model Language / architectures ::@:: They are perspectives to build a requirement model and solution model: deployment view, implementation view, logical view, process view, use-case view, etc.
  - Unified Model Language / motivation ::@:: Models can describe the _essential_ details of reality only. This facilitates better communication \(e.g. ensure the system idea is the same\) among different stakeholders, e.g. clients, developers, etc. This also allows focusing on the _big picture_ without excess details \(e.g. programming-in-the-large, etc.\). <p> By reducing _complexity_, user requirements are better _understood_, architectures/designs are _cleaner_, and implementations are more _maintainable_.
  - Unified Model Language / object orientation ::@:: Many application domains can be modeled easily using _objects_. The _semantic gap_ is smaller. This is also how most people view reality.
  - Unified Model Language / abstraction levels ::@:: requirements: A _requirement model_ is constructed. Objects and their relations in the _application domain_ are identified. Their _implementation_ details are omitted. <br/> analysis, design: A _solution model_ is constructed. On top of the _requirement model_, _interface_ implementation details are considered, but no _internal_ implementation details. <br/> implementation: A _solution model_ is _implemented_. Even _internal_ implementation details are considered.
- [UML](UML.md)
  - [§ classes](UML.md#classes)
  - [§ attributes](UML.md#attributes)
  - [§ operations](UML.md#operations)
  - [§ why classes](UML.md#why%20classes)
  - [§ associations](UML.md#associations)
  - [§ association degree](UML.md#association%20degree)
  - [§ association multiplicity](UML.md#association%20multiplicity)
  - [§ association roles](UML.md#association%20roles)
  - [§ association with additional semantics](UML.md#association%20with%20additional%20semantics)
  - [§ association aggregations](UML.md#association%20aggregations)
  - [§ association compositions](UML.md#association%20compositions)
- quiz: [quiz 2](questions/quiz%202.md)
- UML
  - [§ association classes](UML.md#association%20classes)
  - [§ association generalizations](UML.md#association%20generalizations)
  - [§ generalization and inheritance](UML.md#generalization%20and%20inheritance)
  - [§ abstract entities](UML.md#abstract-entities)
  - [§ generalization properties](UML.md#generalization%20properties)
  - [§ constraints](UML.md#constraints)
  - [§ dependencies](UML.md#dependencies)
  - [§ realizations](UML.md#realizations)
- Unified Model Language
  - Unified Model Language / static modeling ::@:: It is for modeling data.
  - Unified Model Language / dynamic modeling ::@:: It is for modeling programs \(program behavior\).
- quiz: [quiz 3](questions/quiz%203.md)
- [questions § week 2 pre-lecture](questions/index.md#week%202%20pre-lecture)

## week 2 lecture

- datetime: 2025-09-10T12:30:00+08:00/2025-09-10T14:20:00+08:00, PT1H50M
- topic: modeling; unified modeling language; class diagram; association; aggregation; association class; generalization; UML summary
- [§ week 2 pre-lecture](#week%202%20pre%20lecture)
- [questions § week 2 lecture](questions/index.md#week%202%20lecture)

## week 2 lab

- datetime: 2025-09-11T18:00:00+08:00/2025-09-11T19:50:00+08:00, PT1H50M
- topic: IntelliJ IDEA; Git; GitHub
- COMP 3111H
  - COMP 3111H / labs ::@:: The lab series has an assessment weight of 10%. It is split into two distinct phases: a _tool‑based_ phase \(Git, Java basics, JavaFX, project briefing & UML\) and an _implementation_ phase \(GitHub, debugger, unit testing, conflict resolution\). Both phases assist in working on the group project.
  - COMP 3111H / grading
  - COMP 3111H / lab 1 ::@:: IntelliJ IDEA; Git; GitHub
    - COMP 3111H / lab 1 / Git ::@:: It is the most widely used tool for _version control_.
    - COMP 3111H / lab 1 / GitHub ::@:: It is the largest _web-based_ source code hosting service \(software _forge_\) integrated with version control.
    - COMP 3111H / lab 1 / exercises ::@:: create Java project in IntelliJ IDEA; setup Git; setup repository on GitHub
    - COMP 3111H / lab 1 / Git setup ::@:: Students create a local Git repository from an IntelliJ Maven project, then commit changes to the repository.
    - COMP 3111H / lab 1 / GitHub tokens ::@:: Personal Access Tokens \(PATs\) are generated in the GitHub settings under _Developer settings → Personal access tokens_ to authenticate command‑line operations. The token should have a custom expiry of more than six months, include the `repo` scope, and be stored securely.
    - COMP 3111H / lab 1 / readme ::@:: Within the Maven project created in IntelliJ, a `readme.md` file is added. The README must contain comments or remarks describing the project's purpose, then embed a screenshot of IntelliJ IDEA, showing project folder with `.idea` and `src/main/java/Lab1` expanded, Git log, and file editor opening any of the two Java files.
    - COMP 3111H / lab 1 / commits ::@:: You can use IntelliJ IDEA to add files and commit them. This adds an entry to the Git log. The commits are stored locally, and still needs to be pushed to a GitHub repository to be public.
    - COMP 3111H / lab 1 / GitHub repository ::@:: The local repository is pushed to a remote GitHub account. Both Java source files and the README are pushed to GitHub; the repository should be publicly accessible so that its URL can be shared on Canvas.
    - COMP 3111H / lab 1 / requirements ::@:: `readme.md`, 2 Java files, 3 or more commits, screenshot
  - COMP 3111H / communication ::@:: Students may email the instructor or TAs, ask questions during lecture or lab sessions, attend TA office hours, or post on a dedicated Telegram group to seek peer support.
- assignment: [lab 1](assignments/lab%201/index.md)

## week 3 pre-lecture

- topic: software development; project risks; project planning; software development process; agile; unified process
- [software](../../../../general/software.md) ::@:: It consists of computer programs that instruct the execution of a computer. It also includes design documents and specifications.
  - software / nature ::@:: does not wear out, easy to create and modify, easy to mass produce, intangible, labor-intensive
    - software / nature / intangible ::@:: hard to appreciate its development effort, assess its quality, visualize
    - software / nature / easy to mass produce ::@:: It is easy to copy and distribute software. The main cost is development, not manufacture.
    - software / nature / labor-intensive ::@:: Design and programming is hard to automate.
    - software / nature / easy to create and modify ::@:: While easy to create and modify, it is also easy to create and modify software _badly_, creating _defects_ or decreasing _maintainability_.
    - software / nature / does not wear out ::@:: Unlike physically assets, software do not wear out. However, the codebase do "wear out" in the sense of usually getting worse when modified, creating _defects_ or decreasing _maintainability_.
  - software / types ::@:: social aspects, timeliness, uses
    - software / types / uses ::@:: custom, embedded, generic <p> They can be characterized by copies in use, development effort, and source of user requirements.
      - software / types / uses / generic ::@:: copies in use: medium \(relative to embedded\) <br/> development effort: medium \(relative to custom\) <br/> source of user requirements: market research
      - software / types / uses / custom ::@:: copies in use: low <br/> development effort: high \(due to having to capture requirements from the client\) <br/> source of user requirements: client needs
      - software / types / uses / embedded ::@:: copies in use: high \(there are _many_ embedded devices...\) <br/> development effort: low \(due to knowing all requirements already and less functionalities\) <br/> source of user requirements: client needs, hardware needs
    - software / types / timeliness ::@:: data processing, real-time processing
      - software / types / timeliness / data processing ::@:: organize and store _business data_, which may not be _real time_
      - software / types / timeliness / real-time processing ::@::  control devices or processes in _real time_
    - software / types / social aspects ::@:: technical, social-technical
      - software types / social aspects / technical ::@:: does not include _knowledge_ of _work procedures and processes_ <p> This is the main focus of software engineering.
      - software types / social aspects / social-technical ::@:: includes _knowledge_ of _work procedures and processes_ <p> This is less _emphasized_ by software engineering.
- [software development](../../../../general/software%20development.md) ::@:: It is the process of designing and implementing a software solution to satisfy a user. The process is more encompassing than programming, writing code, in that it includes conceiving the goal, evaluating feasibility, analyzing requirements, design, testing and release.
  - software development / types ::@:: green field projects, evolutionary projects \(most common\), component or framework projects
    - software development / types / green field projects ::@:: Develop a _new_ software from scratch.
    - software development / types / evolutionary projects ::@:: _Maintain_ an existing software, to _adapt_ for new environment, _correct_ detects, _enhance_ features, or _re-engineering_ \(_perfect_\) for maintainability.
    - software development / types / component or framework projects ::@:: _Reuse_ an existing component or framework to create a new software. The existing component or framework is designed for reuse in new software but needs to be _adapted_ for _specific requirements_.
- [systems development life cycle](../../../../general/systems%20development%20life%20cycle.md) \(SDLC\) ::@:: It describes the typical phases and progression between phases during the development of a computer-based system; from inception to retirement. At base, there is just one life cycle even though there are different ways to describe it; using differing numbers of and names for the phases. <p> It is still often used for large complex systems.
  - systems development life cycle / name ::@:: \(__this course__: use "software development life cycle"\)
  - systems development life cycle / lifecycle ::@:: A software from its _inception_ to _retirement_ consist of many groups of 4 phases \(see below\).
  - systems development life cycle / phases ::@:: definition \(what\) → design \(how\) → development \(build\) → operation \(use\) <p> After each phase is a _major milestone_.
  - systems development life cycle / motivation ::@:: It _structures_ software development. The phases allows for _control_ and _management_, e.g. deliverables, _milestones_.
  - systems development life cycle / milestone ::@:: It is a management _decision point_, where the management can make major decisions.
- [project management](../../../../general/project%20management.md) ::@:: It is the process of supervising the work of a team to achieve all project goals within the given constraints.
  - project management / 4Ps ::@:: A _project_ involves _people_ \(input\) using _processes_ \(input\) to produce _products_ \(output\) according to requirements from the application domain \(input\).
    - project management / 4Ps / process ::@:: set of activities: tools \(support\), workflows, etc.
    - project management / 4Ps / people ::@:: stakeholders: clients, developers, end users, etc.
    - project management / 4Ps / product ::@:: set of artifacts: code, manuals, models, etc.
    - project management / 4Ps / project ::@:: It requires _control_, _management_, and _control_. It involves a _project plan_.
      - project management / 4Ps / project / plan ::@:: activities & tasks, monitoring & reporting, organization, resources, risks, schedule, scope \(i.e. constraints and objectives; e.g. budget, time, etc.\)
- [software development process](../../../../general/software%20development%20process.md) ::@:: It prescribes a process for developing software. It typically divides an overall effort into smaller steps or sub-processes that are intended to ensure high-quality results. The process may describe specific deliverables – artifacts to be created and completed. <p> \(__this course__: It is a process _template_ that is _adaptable_ for different application domains. It aids in _dividing_ work.\)
- project management
  - project management / scope ::@:: The _first_ task when planning a project: understand scope, i.e. constraints and objectives. <p> define problem \(e.g. design goals\) → analyze requirements \(e.g. estimate system size\) → make top-level diagrams \(i.e. estimate the system; e.g. class diagrams, use case diagrams\) → estimate effort and time \(i.e. prepare the rest of the project plan\)
  - project management / steps ::@:: scope → risks → schedule \(e.g. deliverables\) → implement
- [project risk management](../../../../general/project%20risk%20management.md) ::@:: Within project management, it refers to activities for minimizing project risks, and thereby ensuring that a project is completed within time and budget, as well as fulfilling its goals.
  - project risk management / risk ::@:: Anything that can go wrong in a project, which endangers project success.
    - project risk management / risk / types ::@:: estimation, organization, people, requirements, technology, tools, etc.
  - project risk management / mitigations ::@:: avoid before it happens, confine in case it happens, mitigate after it happens, monitor to know when it happens
  - project risk management / risk
    - project risk management / risk / characteristics ::@:: accuracy of estimates of characteristics \(e.g. rationale, etc.\), consequences \(e.g. nature, scope, timing, etc.\), likelihood \(e.g. boolean, probabilities, subjective, etc.\) <p> Use these to _prioritize_ tasks by _perceived impact_ on the project.
  - project risk management / mitigations
    - project risk management / mitigations / characteristics ::@:: benefit, cost <p> We should perform cost–benefit analysis, e.g. letting the risk happen if its impact is very small, etc.
- [Pareto principle](../../../../general/Pareto%20principle.md) ::@:: It states that, for many outcomes, roughly 80% of consequences come from 20% of causes \(the "vital few"\).
- project risk management
  - project risk management / Pareto principle ::@:: 80% of risk _impact_ is roughly accounted by 20% of identified risks \(in numbers\).
- project management
  - project management / organization ::@:: number of people, roles and responsibilities, teams, etc.
    - project management / organization / good practices ::@:: We should assign people with _experience relevant_ to their tasks. <p> Teams should be modular \(not too few or many people\) and have clear responsibilities, e.g. a team corresponds to one or more identified parts of the system \(divide and conquer\). This helps with having the _right level of communication_. <p> Identify a person in charge \(PIC\) for each part and the system as a whole, so you can talk to them when the relevant parts go wrong.
  - project management / activities & tasks ::@:: A _task_ is a _well-defined_ work assignment for a role. An _activity_ is a group of _related_ tasks.
    - project management / activities & tasks / principles ::@:: agile-driven: details are _incrementally_ planned as the project progresses <br/> plan-driven: details are planned at project _start_ <p> Which one to use highly depends on the project. Often, a combination is the best.
  - project management / schedule ::@:: deliverables \(outputs\), milestones \(_important_ management decision points\), resources assignment, time estimates, ordering \(dependency\)
    - project management / schedule / levels ::@:: \(high level, rigid\) master: client, management &gt; macro: day-to-day management; e.g. Gantt chart, burndown chart &gt; micro: team management \(low level, flexible\)
    - project management / schedule / tools ::@:: charts \(Gantt charts, burndown charts, etc.\), graphs \(dependency graphs, etc.\)
  - project management / estimates ::@:: Quantify something before it occurs. It carries inherent _risk_. Ideally, you should have someone with _experience_ on similar projects to estimate them. <p> For a project, things to estimate include cost, duration, effort, productivity, size, etc.
    - project management / estimates / skills ::@:: _courage_, experience, historical data, model
    - project management / estimates / tips ::@:: better project scoping, divide and conquer the thing to be estimated, expertise of estimators, more historical data, etc.
  - project management / process ::@:: A _sequence_ of _activities_ \(i.e. _workflows_\) to _transform_ user requirements into products.
    - project management / process / elements ::@:: guiding principles, major activities, subprocesses, etc.
    - project management / process / details ::@:: A process uses _resources_ to transform _inputs_ to _outputs_ \(including _intermediates_\) under some _constraints_ \(or _controls_\). There are _entry_ and _exit_ criteria for each activity. <p> A process may have _subprocesses_.
    - project management / process / importance ::@:: communication is better, consistency, division of labor, eases project management, eases training, expertise are reused \(by reusing processes that have proven to be successful\), productivity is higher, products are better, structure, etc.
- quiz: [quiz 4](questions/quiz%204.md)
- software development process
  - software development process / common steps ::@:: gather _requirements_ → _analyze_ and _design_ → _implement_ → _test_
  - software development process / differences ::@:: The major differences are: carrying out the steps, combining the steps, and emphasizing the steps. These lead to different strengths and weaknesses.
  - software development process / types ::@:: monolithic, iterative and incremental \(these two are _slightly different_ things\)
  - software development process / monolithic ::@:: 1+ items: waterfall, etc.
    - software development process / monolithic / characteristics ::@:: All functionalities are planned and the entire system is implemented at once.
  - software development process / iterative and incremental ::@:: 6+ items: agile, code and fix, phased release, prototyping, spiral, unified process \(UP\)
    - software development process / iterative and incremental / properties ::@:: incremental: Separate functions are implemented one-by-one. <br/> iterative: Each function is implemented and refined over time. <br/> both: Possible with various degrees.
- [waterfall model](../../../../general/waterfall%20model.md) ::@:: It is the process of performing the typical software development life cycle \(SDLC\) phases in sequential order. Each phase is completed before the next is started, and the result of each phase drives subsequent phases.
  - waterfall model / steps ::@:: gather requirements \(requirements specification document\) → analysis & design \(design specification document\) → implement \(modules\) → test \(tested modules\) → maintain <p> After each step except for the final step, comprehensive docs are created. Going back is _costly_, so you will want to check the docs for any errors before entering the next step.
  - waterfall model / the waterfall ::@:: By placing the next step below the previous step, it looks like we are following a "waterfall" along the steps.
  - waterfall model / additional steps ::@:: other deliverables \(e.g. code, docs, training materials, etc.\), review \(for correctness and standards\)
  - waterfall model / use cases ::@:: Requirements are well-defined, well-understood, and very unlikely to change. <p> This is because going back is _costly_.
  - waterfall model / comparison ::@:: Compared to alternative SDLC methodologies such as Agile, it is among the least iterative and flexible, as progress flows largely in one direction \(like a waterfall\) through the phases of conception, requirements analysis, design, construction, testing, deployment, and maintenance.
  - waterfall model / advantages ::@:: discipline \(formality, rigor\), docs are approved and standardized, easy and predictable development, suitable as well for non-software engineering processes \(e.g. hardware development\)
  - waterfall model / disadvantages ::@:: assumes sequentiality and linearity, different languages in different phases, rigid as it freezes results of each phase, user feedback cannot be incorporated on the fly
- software development process
  - software development process / code and fix ::@:: Gather _requirements_ \(and usually store in the developer's mind only\). Based on the requirements, _implement_. _Test_ if it meets all requirements. If yes, you are done! If not, go back to implement to fix the errors.
    - software development process / code and fix / characteristics ::@:: changing requirements, many changes, messy code structure, unsuitable for large systems
    - software development process / code and fix / disadvantages ::@:: fail to meet expectations, over budget, over schedule, uncontrollable, unpredictable
- [software prototyping](../../../../general/software%20prototyping.md) ::@:: It is the activity of creating prototypes of software applications, i.e., incomplete versions of the software program being developed.
  - software prototyping / steps ::@:: gather and refine requirements → design → prototype \(not the entire system\) → evaluate → EITHER refine prototype \(→ design\) OR engineer product \(which may or may not be the final product\)
  - software prototyping / comparison ::@:: Similar to code and fix, but there is slightly more discipline and incorporates user feedback.
  - software prototyping / characteristics ::@:: exploratory \(e.g. functionalities, user interfaces, etc.\), good for unknown or vague requirements
  - software prototyping / advantages ::@:: explore multiple different solutions, explore user requirements, incorporates user feedback
  - software prototyping / disadvantages ::@:: incomplete process \(engineering the final product may need a separate process\), invisible to management \(e.g. the number of prototypes needed\), missing or sparse docs
- [spiral model](../../../../general/spiral%20model.md) ::@:: It is a risk-driven software development process model. Based on the unique risk patterns of a given project, the spiral model guides a team to adopt elements of one or more process models, such as incremental, waterfall, or evolutionary prototyping.
  - spiral model / steps ::@:: plan → risk analysis → \(EITHER go OR no go\) → engineer → evaluate → \(repeat until we have a complete system\)
  - spiral model / the spiral ::@:: The 4 quadrants of a 2D plane are respectively the 4 steps \(clockwise from quadrant II\), and the process is represented by arrowheads spiraling outwards.
  - spiral model / advantages ::@:: incorporates risk evaluation, incorporates user feedback to better meet expectations \(from evaluate and plan\), iterative and incremental
  - spiral model / disadvantages ::@:: expertise on risk evaluation required, for internal development rather than contract development as you know all the requirements, phases are not elaborated \(a separate process may be used\)
- [software release life cycle](../../../../general/software%20release%20life%20cycle)
  - software release life cycle / name ::@:: \(__this course__: use _phased release_\)
  - software release life cycle / motivation ::@:: Since change is inevitable \(by user requirements\), so produce releases over time and make changes accordingly.
  - software release life cycle / flow ::@:: Developers release multiple _development releases_ over time. _Concurrently_, users make _use/production releases_ out of each development release.
  - software release life cycle / incremental and iterative ::@:: Releases can be incremental or iterative or both. Often both are used in practice. <p> incremental: Separate functions of a system are implemented one-by-one \(partial system\). If used alone, each function is fully implemented at once \(full functionality\). <br/> iterative: Functions are implemented and refined over time \(partial functionality\). If used alone, all functions begin implementation at once \(full system\).
  - software release life cycle / advantages ::@:: apply appropriate expertise, early training, early user feedback, frequent releases, promote modularity, reduce risk
  - software release life cycle / disadvantages ::@:: common facilities for all functions are hard to identify, each function \(part\) needs to be small
- [agile software development](../../../../general/agile%20software%20development.md) ::@:: It is an umbrella term for approaches to developing software that reflect the values and principles agreed upon by _The Agile Alliance_, a group of 17 software practitioners, in 2001.
  - agile software development / principles ::@:: emphasized: client involvement, individuals and interactions, responsive to change, working software <br/> deemphasized \(but not completely ignored\): comprehensive docs, contract negotiation, plan following, processes and tools
  - agile software development / methods ::@:: continuous integration \(CI\), extreme programming \(XP\), scrum, etc.
  - agile software development / practices ::@:: pair programming: implement a feature with another person checking to reduce mistakes <br/> planning poker: estimate implementation time <br/> test-driven development \(TDD\): think of tests before implementing <br/> etc.
- [extreme programming](../../../../general/extreme%20programming.md) \(XP\) ::@:: It is a software development methodology intended to improve software quality and responsiveness to changing customer requirements. As a type of agile software development, it advocates frequent releases in short development cycles, intended to improve productivity and introduce checkpoints at which new customer requirements can be adopted.
  - extreme programming / steps ::@:: gather and analyze requirements → implement → \(repeat _quickly_\)
  - extreme programming / gather and analyze requirements ::@:: The developer determines features needed and estimate cost and time. Then the client selects features for each _iteration_.
  - extreme programming / implement ::@:: Each _iteration_ has many tasks. The developer implement features using _pair programming_ and design test cases using _TDD_.
- [continuous integration](../../../../general/continuous%20integration.md) \(CI\) ::@:: It is the practice of integrating source code changes frequently and ensuring that the integrated codebase is in a workable state.
  - continuous integration / mechanism ::@:: Typically, developers merge changes to an integration branch, and an automated system \(__this course__: CI server\) builds and tests the software system. Often, the automated process runs on each commit or runs on a schedule such as once a day. <p> \(__this course__: Work is submitted daily and/or as soon as possible to the main repository. Whenever that happens, CI servers run build and test scripts, and notify if there are failures.\)
  - continuous integration / advantages ::@:: automate build and test, catch build-breaking bugs early, check progress, integrate and test early, reduce integration conflicts
- [scrum](../../../../general/scrum.md) ::@:: It is an agile team collaboration framework commonly used in software development and other industries.
  - scrum / overview ::@:: It specifies what to do to develop a software product. But the detailed specifics \(how to do\) are decided by teams. <p> Requirements are items in a _product backlog_. The _product owner_ \(the client\) sets _priorities_. Then, the software is developed in _sprints_. Teams _self-organize_ to determine the best way to deliver the product.
  - scrum / sprint ::@:: Scrum prescribes for teams to break work into goals to be completed within time-boxed iterations, called _sprints_. Each sprint is no longer than one month and commonly lasts two weeks. The scrum team assesses progress in time-boxed, stand-up meetings of up to 15 minutes, called _daily scrums_. At the end of the sprint, the team holds two further meetings: one sprint review to demonstrate the work for stakeholders and solicit feedback, and one internal sprint retrospective.
    - scrum / sprint / activities ::@:: In a sprint, the software is designed, implemented, and tested. The requirements are not allowed to change.
  - scrum / release ::@:: A release should have 4 to 12 sprints. The shorter the release cycle, the shorter the duration of each sprint. <p> It may be associated with a _release backlog_.
  - scrum / framework ::@:: artifacts, meetings, roles
  - scrum / roles ::@:: product owner, scrum master, team
  - scrum / meetings ::@:: sprint planning → daily scrum meeting → sprint review \(external-oriented\), sprint retrospective \(internal-oriented\)
  - scrum / artifacts ::@:: burndown charts, product backlog, sprint backlog <br/> additional: defect backlog, release backlog
  - scrum / roles
    - scrum / roles / product owner ::@:: The key stakeholder represents the client or end users. It defines and prioritize requirements, and adjusts both every iteration. It decides on content and timing. It accepts or rejects results.
    - scrum / roles / scrum master ::@:: enable close cooperation, enact scrum values and practices, ensure functional and productive teams, remove progress obstacles, shield external interferences
    - scrum / roles / team ::@:: Apart from the scrum master, the other roles are similar to those in other development processes, e.g. developers, testers, etc.
  - scrum / meetings
    - scrum / meetings / sprint planning ::@:: Considers business conditions, current product, product backlog, team capacity, technology, etc. Prioritize product backlog to select _sprint goal_. Then, plan to achieve the sprint goal, and create a _sprint backlog_ from product backlog and estimate time \(ideally by subject matter experts\).
    - scrum / meetings / daily scrum meeting ::@:: They are stand-up \(no sitting down\) meetings up to 15 minutes. This is great for less experienced teams, but may hurt _morale_ in more experienced teams. Possible questions to ask: <p> review: What did you do yesterday? <br/> plan: What will you do today? <br/> obstacles: Is anything in your way?
  - scrum / artifacts
    - scrum / artifacts / product backlog ::@:: Requirements, which have values to the client or end users. Prioritized by the product owner and re-prioritized before each sprint. <p> This backlog may be further split into multiple _release backlogs_.
    - scrum / artifacts / sprint backlog ::@:: Selected items from the product backlog based on item priority and team capacity. Some product backlog items may become multiple sprint backlog items. During the sprint, team members select items to work on.
    - scrum / artifacts / burndown chart ::@:: For each task, we _estimate_ the hours remaining to complete it. Then, the chart sums them up and plot them as a line chart, which shows the _estimated_ total hours remaining to complete the sprint. <p> It may _fluctuate_, but should _tend to zero_, otherwise you have problems in your sprint. <p> The slope of the line chart is the _burndown velocity_.
    - scrum / artifacts / defect backlog ::@:: Try to avoid defects, but they are inevitable. When you encounter them, track them separately in this backlog to avoid mixing up items with the product or sprint backlog. The backlog may persists across sprints. Any defects related to a feature should be fixed before marking the feature as complete.
- agile software development
  - agile software development / advantages ::@:: adaptable/flexible to changing requirements, faster speed-to-market, fewer defects, immediate user feedback
  - agile software development / disadvantages ::@:: close collaboration between developers and product owner required, daily meetings may be costly, docs are often missing, scope creep due to adding requirements
- software development process
  - software development process / characteristics ::@:: abstraction or generality \(of process\), adaptable to changes, discipline \(formal, rigor\), incremental, risk assessment, separation of concerns \(modularity\)
  - software development process / discipline ::@:: spiral: The 4 phases must be followed in a spiral without backtracking. <br/> waterfall: SDLC is followed sequentially without possibility of backtracking.
  - software development process / separation of concerns ::@:: phased release: Development and release is separate. <br/> spiral: Planning, risk analysis, engineering, and evaluation are separate. <br/> waterfall: Each phase of SDLC is separate.
  - software development process / abstraction or generality ::@:: spiral: Allows using other processes for the actual development and testing. <br/> waterfall: As a direct implementation of the general SDLC.
  - software development process / adaptable to changes ::@:: agile: By its nature. <br/> phased release: Releases happen over time. <br/> spiral: Planning happens periodically.
  - software development process / incremental ::@:: agile: Many sprints are needed. <br/> phased release: Many releases are needed. <br/> prototyping: Many prototypes are needed. <br/> spiral: Many spirals are needed.
  - software development process / risk assessment ::@:: spiral: The only process to explicitly integrate risk analysis.
- [unified process](../../../../general/unified%20process.md) ::@:: It is an iterative and incremental software development process framework. <p> It is not simply a process, but rather an extensible framework which should be customized for specific organizations or projects.
  - unified process / cycle ::@:: inception → elaboration → construction → transition
    - unified process / cycle / inception ::@:: Gather requirements. See if the requirements are feasible. Decide if to continue with the project or not.
    - unified process / cycle / elaboration ::@:: Based on the gathered requirements, come up with a design to be implemented.
    - unified process / cycle / construction ::@:: Based on the gathered requirements and elaborated design, implement the system.
    - unified process / cycle / transition ::@:: Deploy and maintain the system.
  - unified process / phase ::@:: It may be divided into a series of timeboxed _iterations_. Each iteration results in an _increment_, which is a release of the system that contains added or improved functionality compared with the previous release.
    - unified process / phase / iteration & increment ::@:: \(__this course__: Each iteration produces a _working product_. Each increment establishes a _system baseline_.\)
  - unified process / activities ::@:: The activities _vary_, but can usually be categorized into engineering activities and management activities
    - unified process / activities / engineering ::@:: for reference; requirements capture → analysis → design → implement → test → \(management\)
    - unified process / activities / management ::@:: for reference; \(engineering\) → software quality assurance → project management
  - unified process / diagram ::@:: The diagram charts phases and iterations on the _x_-axis \(time axis\), and activities on the _y_-axis \(dimension axis\). <p> For each activity, there is an area chart that varies over time \(and can be zero\), showing how the relative emphasis of different disciplines changes over the course of the project.
  - unified process / features ::@:: defines activities: workflows to transform user requirements to a system <br/> defines models: abstract or concrete entities that are transformed by workflows; e.g. artifacts <br/> generic: a generic process _framework_ needing to be _specialized_ to use
- software development process
  - software development process / considerations ::@:: people \(e.g. expertise, skills\), project \(e.g. novelty, size, vagueness\), organization \(e.g. accessibility, formality, size\)
- unified process
  - unified process / advantages ::@:: It incorporates _best practices_ from all the previous software development processes and provides a _generic framework_.
- quiz: [quiz 5](questions/quiz%205.md)
- [questions § week 3 pre-lecture](questions/index.md#week%203%20pre-lecture)

## week 3 lecture

- datetime: 2025-09-17T12:30:00+08:00/2025-09-17T14:20:00+08:00, PT1H50M
- topic: software development; project risks; project planning; software development process; agile; unified process
- [§ week 3 pre-lecture](#week%203%20pre%20lecture)
- [questions § week 3 lecture](questions/index.md#week%203%20lecture)

## week 3 lab

- datetime: 2025-09-18T18:00:00+08:00/2025-09-18T19:50:00+08:00, PT1H50M
- topic: Java basics; object; class; attribute; constructor; method; access modifier; inheritance; interface
- COMP 3111H
  - COMP 3111H / lab 2 ::@:: Java basics; object; class; attribute; constructor; method; access modifier; inheritance; interface
    - COMP 3111H / lab 2 / exercise ::@:: write, compile, and run Java programs; inheritance, interface
    - COMP 3111H / lab 2 / Java basics ::@:: Design a small application that showcases the use of classes, objects, constructors, attributes, and methods. Pay attention to how each component interacts: constructors create and initialize objects; attributes hold state; methods define behavior.
    - COMP 3111H / lab 2 / class ::@:: In Java everything revolves around classes and objects, which contain both data \(attributes\) and code \(methods\).
    - COMP 3111H / lab 2 / attribute ::@:: It is a field inside a class that represents the characteristics or state of an object. It can be accessed or modified via getter and setter methods.
    - COMP 3111H / lab 2 / constructor ::@:: It is a special method invoked automatically when a new instance of a class is created; its main job is to allocate memory and initialize fields.
    - COMP 3111H / lab 2 / method ::@:: They are functions defined within a class that describe what the class can do. They may accept parameters, perform operations, and return values.
    - COMP 3111H / lab 2 / package ::@:: If you create an additional package \(e.g., `Lab2b` under `src`\) you can still use classes from another package \(`Score` in `Lab2a`\). This is possible because Java projects allow packages to reference each other, provided the necessary imports and access modifiers are set correctly. <p> This also allows creating classes of the same name in different packages.
    - COMP 3111H / lab 2 / object ::@:: Use `new <class name>(<args>)` to create an new object. Afterwards, you can invoke methods and access attributes on it, provided the access modifiers allow it.
    - COMP 3111H / lab 2 / access modifier ::@:: They work differently for classes \(class-level visibility\) and members \(member-level visibility\).
      - COMP 3111H / lab 2 / access modifier / class-level visibility ::@:: When you declare a class at the top level \(outside any other class\), Java allows only two modifiers: <p> - `public`: the class can be referenced from any package; it must reside in a file whose name matches the class name. <br/> - _default_ \(no modifier\): the class is __package‑private__ – it can be used only by classes that live in the same package.
      - COMP 3111H / lab 2 / access modifier / member-level visibility ::@:: They apply to attributes, methods, and constructors in a class. <p> - `public`: the member can be accessed from any other class in any package. <br/> - `protected`: visible within its own package and by subclasses even if they are in different packages. <br/> - `private`: accessible only inside the class that declares it. <br/> - _default_ \(no modifier\): visible to all classes in the same package, but invisible outside of it.
    - COMP 3111H / lab 2 / `final` keyword ::@:: It can be applied to a variable \(e.g. attributes, local variables, etc.\): once assigned it becomes read‑only; this is useful for constants \(e.g. `public static final int MAX_SIZE = 10;`\) or configuration values that must not change after initialization. It can still have any visibility modifier.
    - COMP 3111H / lab 2 / printing arrays ::@:: Learn to use `java.util.Arrays.toString()` to display array contents easily. Compare this with manual printing \(e.g., looping over elements\) to see the convenience of the utility method.
    - COMP 3111H / lab 2 / inheritance ::@:: It lets one class \(the subclass/child\) inherit fields and methods from another \(the superclass/parent\). <p> In Java, use the `extends` keyword for classes inheriting other classes or interfaces inheriting other interfaces. Use the `implements` keyword for classes inheriting interfaces. Interfaces cannot inherit classes. <p> A class can extend at most one other class. Both classes and interfaces can extend multiple other interfaces.
    - COMP 3111H / lab 2 / `@Override` annotation ::@:: It tells the compiler you intend to override a base‑class method; it helps catch mistakes that make the method not actually overriding any base-class method, e.g. forget to inherit, wrong method signature, etc.
    - COMP 3111H / lab 2 / interface ::@:: They provide a way to "hide" implementation details while exposing only essential operations \(security\), and they enable multiple inheritance of type \(a class can implement many interfaces but only extend at most one class\). <p> They cannot contain non-`static` attributes.
- assignment: [lab 2](assignments/lab%202/index.md)

## week 4 pre-lecture

- topic: requirements capture; domain model; modeling classes; modeling associations; modeling attributes; use case model; actor; use case diagram
- unified process
  - unified process / activities
    - unified process / activities / engineering
- [requirement](../../../../general/requirement.md) ::@:: It is a _condition_ that must be satisfied for the output of a work effort to be _acceptable_. It is an explicit, _objective_, clear and often quantitative description of a condition to be satisfied by a material, design, product, or service.
  - requirement / nots ::@:: It states _what_ the system does, but not _how_ it does.
  - requirement / formality ::@:: It could range from high-level abstract statement to detailed mathematical description.
  - requirement / types ::@:: system requirements, user requirements
  - requirement / user requirements ::@:: For _clients_. Usually in _natural language_ or _diagrams_. It describes _user_ operations and constraints.
  - requirement / system requirements ::@:: For both _clients_ and _developers_. Usually _structured documents_. It describes _detailed_ functions, operational constraints, services, etc. It defines _things to implement_ as part of a _contract_.
- [requirements elicitation](../../../../general/requirements%20elicitation.md) ::@:: It is the practice of researching and discovering the requirements of a system from users, customers, and other stakeholders.
  - requirements elicitation / names ::@:: The practice is also sometimes referred to as "requirement gathering". \(__this course__: use _requirements capture_\)
  - requirements elicitation / goals ::@:: Learn about the problem that needs a solution. Specify the required features and constraints that the client understands and can approve.
  - requirements elicitation / non-goals ::@:: It specifies the _problem_, not the solution. While it does specifies behaviors of the final software system, it does not _specify_ how the system do them.
  - requirements elicitation / importance ::@:: We are overly optimistic. If we do not research requirements, we may think we know every detail, until when we actually develop the system at which point you discover ambiguous, forgotten, or undefined details. <p> This increases error. So researching requirements _reduces error_.
    - requirements elicitation / importance / failures ::@:: Major causes of software development failures or problems: changing requirements, incomplete requirements, unneeded system, unrealistic expectations, user involvement lacking, etc.
    - requirements elicitation / importance / cost ::@:: Whenever there is a defect, the later we discover it, the higher the cost it takes to fix it \(usually grows exponentially\). This is the cheapest when we are specifying the requirements, being the first step.
  - requirements elicitation / difficulty ::@:: It requires the collaboration of stakeholders with different background, resulting in _knowledge gap_. We need to bridge this gap, which is difficult.
    - requirements elicitation / difficulty / solution ::@:: Developers need to learn about the _application domain_ and its requirements. They need to transform said _vague_ requirements to _precise_ specifications. They also need to _represent_ the specifications that can be understood by clients. <p> They may even need to give _feedback_ on the requirements given by the clients and ask them to _revise_ \(i.e. "_educate_" the clients\), e.g. unrealistic requirements, etc.
  - requirements elicitation / activities ::@:: understand application domain and user needs determine risks, capture system requirements, validate system requirements
    - requirements / elicitation / activities / understand ::@:: collect system _requirements_ and _constraints_, and determine _development scope_ and _design goals_ \(for reducing design _complexity_\)
    - requirements / elicitation / activities / risks ::@:: economic, legal, operational, organizational, technical, etc.
    - requirements / elicitation / activities / capture ::@:: data requirements → _domain model_ <br/> functional requirements → _use-case model_ <br/> nonfunctional requirements → _supplementary text_
    - requirements / elicitation / activities / validate ::@:: verify _correctness_ and _completeness_ \(all important requirements\) of system requirements; use a checklist of questions to examine each requirement
- [software requirements specification](../../../../general/software%20requirements%20specification.md) \(SRS\) ::@:: It is a description of a software system to be developed. It is modeled after the business requirements specification \(CONOPS\). It lays out functional and non-functional requirements, and it may include a set of use cases that describe user interactions that the software must provide to the user for perfect interaction.
  - software requirements specification / name ::@:: \(__this course__: use _system requirements specification_\)
  - software requirements specification / elements ::@:: definition of user requirements, specification of system requirements
  - software requirements specification / not ::@:: Like requirements \(which it contains\), it states _what_ the system does, but not _how_ the system does. It is not a _design document_.
  - software requirements specification / agile software development ::@:: They argue producing such a thing is a waste of time when requirements change quickly. However, even they are using some aspects, albeit reduced, of SRS, e.g. product backlog, etc.
  - software requirements specification / languages :: design description language: most restricted, like programming languages <br/> graphical notations: + text annotations <br/> mathematical specifications <br/> natural language: + diagrams, tables, etc. <br/> structured natural language: restricted, follows fixed template
    - software requirements specification / languages / UML ::@:: UML is a kind of _graphical notation_. It can be accompanied by _structured text_, a kind of _structured natural language_.
- [domain model](../../../../general/domain%20model.md) ::@:: It is a conceptual model of the domain that incorporates both behavior \(__this course__: associations\) and data \(__this course__: classes\). <p> \(__this course__: They are things for which _data_ must be stored.\)
  - domain model / sources ::@:: domain experts \(includes users\), requirement statements
  - domain model / classes ::@:: They provide a _glossary of terms_ \(_nouns_\) and are described in _class diagrams_.
    - domain model / classes / sources ::@:: They are _naturally occurring_ things and concepts in the _user requirements_. They should be _relevant_, _essential_, and _persistent_ \(always exist\). They should be _nouns_. <p> examples: business objects, events, real-world concepts and objects, etc.
    - domain model / classes / names ::@:: The _nouns_ should be in _singular form_.
  - domain model / associations ::@:: They provide a _glossary of terms_ \(_verbs_\) and are described by _associations_.
    - domain model / associations / sources ::@:: They are _naturally occurring_ things and concepts in the _user requirements_. They should be _relevant_, _essential_, and _persistent_ \(always exist\). They should be _verbs_. <p> examples: business objects, events, real-world concepts and objects, etc.
    - domain model / associations / names ::@:: The _verbs_ should be in _active voice_.
  - domain model / stable system ::@:: By modeling _relevant_, _essential_, and _persistent_ classes and associations, the system is _stable_. We do not need to _modify_ the system very frequently.
  - domain model / decomposition ::@:: Converting user requirements into classes and associations depends on _experience_, problem _nature_, and _judgement_. There are usually multiple _good_ \("correct"\) decompositions.
- UML
  - [§ domain models](UML.md#domain%20models)
  - [§ modeling classes](UML.md#modeling%20classes)
  - [§ modeling associations](UML.md#modeling%20associations)
  - [§ modeling attributes](UML.md#modeling%20attributes)
- quiz: [quiz 6](questions/quiz%206.md)
- [use case diagram](../../../../general/use%20case%20diagram.md) ::@:: It is a graphical depiction of a user's possible interactions with a system. A use case diagram shows various use cases and different types of users the system has and will often be accompanied by other types of diagrams as well.
  - use case diagram / elements ::@:: The use cases are represented by either circles or ellipses. The actors are often shown as stick figures.
  - use case diagram / actor ::@:: It is something _outside_ the system that interacts with the system _directly_. Interact means providing _input_ or receiving _output_. It should have a single _role_. <p> It can be persons, systems, etc. Note that a person may have multiple roles, hence represented by multiple actors; or multiple people play a single role, hence represented by a single actor.
    - use case diagram / actor / motivation ::@:: It is a _source_ to discover use cases.
    - use case diagram / actor / classification ::@:: Like how classes _classify_ collections of objects and associations _classify_ collections of links, actors \(a _classifier_\) _classify_ collections of systems or users \(_instances_\).
  - use case diagram / use case ::@:: A _specific way_ to use the system by an actor. It may only use _part_ of the system's functionality.
    - use case diagram / use case / scenario ::@:: A concrete and focused _single use_ of the system by a _single_ actor.
    - use case diagram / use case / classification ::@:: Like how classes _classify_ collections of objects and associations _classify_ collections of links, use cases \(a _classifier_\) _classify_ collections of scenarios \(_instances_\).
- UML
  - [§ use case models](UML.md#use%20case%20models)
  - [§ modeling actors](UML.md#modeling%20actors)
  - [§ modeling use cases](UML.md#modeling%20use%20cases)
  - [§ use case diagrams](UML.md#use%20case%20diagrams)
- quiz: [quiz 7](questions/quiz%207.md)
- [questions § week 4 pre-lecture](questions/index.md#week%204%20pre-lecture)

## week 4 lecture

- datetime: 2025-09-24T12:30:00+08:00/2025-09-24T14:20:00+08:00, PT1H50M
- status: canceled
- [§ week 4 pre-lecture](#week%204%20pre%20lecture)
- [questions § week 4 lecture](questions/index.md#week%204%20lecture)

---

> Dear COMP3111 Students,
>
> Pre-emptive Actions for Typhoon \(颱風超前部署\):
>
> As Super Typhoon Ragasa is approaching, the Hong Kong Observatory has issued warnings of worsening weather on 23–24 September.
>
> I have decided to cancel Lecture L1 on Wednesday and Lecture L2 on Thursday \(L2 is also cancelled to keep progress synchronized across sections\). Since COMP3111 is blended, the online content will continue as usual — please follow the current deadlines for quizzes on Canvas. However, we will extend the deadline for this week’s exercises, and likely adjust some future exercise deadlines as well. Don’t worry — we are slightly ahead of schedule, so there will still be enough time to cover all required exercises this semester.
>
> All labs will still be conducted on Thursday and Friday. If road conditions are not good on Thursday, I recommend students attend the Friday section instead, or watch the Zoom recording.
>
> B.t.w., HKUST students are always hard working \(they are definitely not lazy at all\)! Please stay safe, and make good use of this little "typhoon break" during the busy Fall semester. If possible, we will also release the project description and sign-up form, so you guys can spend some time on it during the break =\)
>
> Best regards,
>
> \[redacted\]

## week 4 lab

- datetime: 2025-09-25T18:00:00+08:00/2025-09-25T19:50:00+08:00, PT1H50M
- topic:
- COMP 3111H
  - COMP 3111H / lab 3
- assignment: [lab 3](assignments/lab%203/index.md)

## aftermath

### total

- grades: ?/100
  - statistics: ?
