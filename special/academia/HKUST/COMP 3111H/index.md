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
- [software engineering](../../../../general/software%20engineering.md) ::@:: It is a branch of both computer science and engineering focused on designing, developing, testing, and maintaining software applications. It involves applying engineering principles and computer programming expertise to develop software systems that meet user needs. <!--SR:!2025-12-09,61,310!2025-12-09,62,310-->
- [source lines of code](../../../../general/source%20lines%20of%20code.md) \(SLOC\) ::@:: It is a software metric used to measure the size of a computer program by counting the number of lines in the text of the program's source code. <!--SR:!2025-12-02,56,310!2025-12-10,62,310-->
  - source lines of code / acronyms ::@:: LLOC: logical lines of code; logical SLOC <br/> LOC: lines of code; physical SLOC <br/> MLOC: million lines of code <br/> SLOC: source lines of code <!--SR:!2025-11-30,54,310!2025-12-08,61,310-->
  - source lines of code / examples ::@:: Rome: Total War &lt; Boeing 787 &lt; F-35 Fighter Jet &lt; Windows 7 &lt; Windows 10 &lt; Facebook &lt; Mac OS X &lt; luxury passenger car <!--SR:!2025-11-07,33,270!2025-10-12,12,230-->
  - source lines of code / effort ::@:: Effort is not _linearly_ proportional to source lines of code!! <!--SR:!2025-12-11,63,310!2025-12-10,63,310-->
- [software maintenance](../../../../general/software%20maintenance.md) ::@:: It is the modification of software after delivery. <p> It is often considered lower skilled and less rewarding than new development. As such, it is a common target for outsourcing or offshoring. <!--SR:!2025-11-30,54,310!2025-12-10,63,310-->
  - software maintenance / complexity ::@:: It can be complex. Indeed, given the large amount of existing software, it uses the most time of most developers. <!--SR:!2025-12-07,60,310!2025-12-04,58,310-->
- [programming complexity](../../../../general/programming%20complexity.md) ::@:: It is a term that includes software properties that affect internal interactions. <!--SR:!2025-12-07,60,310!2025-12-02,56,310-->
  - programming complexity / sources ::@:: application domain, communication, management, tools <!--SR:!2025-12-10,63,310!2025-12-09,61,310-->
    - programming complexity / sources / application domain ::@:: A problem is often _complex_ and outside the domain of most developers \(i.e. not _domain experts_\). <!--SR:!2025-12-13,65,310!2025-12-14,66,310-->
    - programming complexity / sources / communication ::@:: Clients and developers have different _background_, _vocabulary_, etc. which is made worse by _ambiguity_ of human languages. <!--SR:!2025-12-06,59,310!2025-12-08,61,310-->
    - programming complexity / sources / management ::@:: _Dividing_ a project and _reassembling_ it is difficult. _Coordination_ between different _parts_ and _people_ is also difficult. <!--SR:!2025-12-15,67,310!2025-11-16,40,290-->
    - programming complexity / sources / tools ::@:: Creating useful _tools_ for software development is also complex. Indeed, creating the tools themselves also require software engineering. <!--SR:!2025-11-15,39,290!2025-12-06,59,310-->
  - programming complexity / problems ::@:: development, quality <!--SR:!2025-12-04,58,310!2025-12-11,63,310-->
    - programming complexity / problems / quality ::@:: abandonment \(London Stock Exchange; after 5 years of development\), inflexible, unreliable \(Ariane 5 \(rocket\)\), unsafe \(London Ambulance Service; fell twice in 1992\), etc. <!--SR:!2025-11-23,45,290!2025-11-24,46,290-->
      - programming complexity / problems / quality / examples ::@:: A small software update to Amazon, a large and complex website, caused \$2.8 million in lost revenue. <!--SR:!2025-11-18,44,290!2025-12-14,66,310-->
- [Ariane 5](../../../../general/Ariane%205.md) ::@:: It is a retired European heavy-lift space launch vehicle operated by Arianespace for the European Space Agency \(ESA\). <!--SR:!2025-11-21,47,290!2025-12-10,62,310-->
  - Ariane 5 / notable launches
    - Ariane 5 / notable launches / first test flight ::@:: Ariane 5's first test flight \(Ariane 5 Flight 501\) on 4 June 1996 failed, with the rocket self-destructing 37 seconds after launch because of a malfunction in the control software. <!--SR:!2025-11-19,45,290!2025-12-01,55,310-->
      - Ariane 5 / notable launches / first test flight / cause ::@:: A data conversion from 64-bit floating-point value to 16-bit signed integer value to be stored in a variable representing horizontal bias caused a processor trap \(operand error\) because the floating-point value was too large to be represented by a 16-bit signed integer. <!--SR:!2025-12-01,55,310!2025-11-22,45,290-->
- programming complexity
  - programming complexity / problems
    - programming complexity / problems / development ::@:: does not meet user requirements, difficult to measure progress, over budget, over time, etc. <!--SR:!2025-12-07,60,310!2025-11-22,45,290-->
      - programming complexity / problems / development / statistics ::@:: \(2012\) For _large_ software projects: deliver less value &gt; over budget &gt; company threatening &gt; over time &gt; etc. <!--SR:!2025-10-10,9,190!2025-11-25,47,290-->
  - programming complexity / mitigations ::@:: There are many desirable _characteristics_ considered part of quality. It is impossible and unnecessary to achieve all of them. <p> Instead, we should under the client's _goals_ and _prioritize_ certain characteristics. This reduces complexity somewhat. <!--SR:!2025-11-18,44,290!2025-11-15,39,290-->
    - programming complexity / mitigations / characteristics ::@:: correct, efficient, evolvable, interoperable, maintainable, portable, productive, reliable, repairable, reusable, robust, timely, usable, verifiable, visible, etc. <!--SR:!2025-11-17,43,290!2025-11-22,45,290-->
- [modular programming](../../../../general/modular%20programming.md) ::@:: It is a programming paradigm that emphasizes organizing the functions of a codebase into independent modules – each providing an aspect of a computer program in its entirety without providing other aspects. <!--SR:!2025-12-06,59,310!2025-11-30,54,310-->
  - modular programming / motivation ::@:: Humans cannot understand things that are too _complex_. Often, we break down a complex systems into _modules_, parts of a system that makes sense to _consider separately_ and interact with other modules. This is known as _divide and conquer_. <!--SR:!2025-12-11,63,310!2025-11-16,40,290-->
  - modular programming / module ::@:: It is a part of a system that can be _considered separately_. To model _interactions_ with other modules, they are limited to _interfaces_, which _abstracts_ and _encapsulates_ a module via _information hiding_. <!--SR:!2025-12-09,61,310!2025-12-03,57,310-->
    - modular programming / module / abstraction ::@:: The internals of a module are hidden away. Interaction is defined via its interface only. The usage of the module by other modules can be understood by looking at its interface only \(ideally\). This reduces complexity of the system. <!--SR:!2025-12-04,58,310!2025-12-06,59,310-->
    - modular programming / module / encapsulation ::@:: When we want to modify a module, we only need to modify the module without changing other modules \(ideally\). The internals of a module can be changed without affecting other modules \(ideally\). This reduces maintenance burden. <!--SR:!2025-12-03,57,310!2025-12-07,60,310-->
  - modular programming / advantages ::@:: bug reduction, _incremental_ development, maintainability, productive teams, reusability <p> This makes software development _more predictable_, leading to better cost and time estimation. <!--SR:!2025-12-10,63,310!2025-12-14,66,310-->
- [engineer](../../../../general/engineer.md) ::@:: It is a practitioner of engineering. <p> They apply ingenuity, mathematics, and scientific knowledge to develop _solutions_ \(e.g. materials, structures, _systems_\) for specific _problems_. They need consider _limitations_ from cost, practicality, regulation, and safety. <!--SR:!2025-11-20,46,290!2025-12-07,60,310-->
  - engineer / vs. scientist ::@:: The former builds things for _quality_ \(e.g. avoiding engineering failures\) while the latter builds things for discovering _new_ things \(e.g. scientific breakthroughs\). <!--SR:!2025-12-12,64,310!2025-12-05,58,310-->
- software engineering
  - software engineering / vs. computer scientist ::@:: The former studies practices and principles for building _quality_ systems while the latter studies _algorithms_ and _foundations_ of computing. <p> The former considers the _context_ to use the appropriate technologies \(e.g. frameworks\) according to their _characteristics_, while the latter focuses on _basic_ technologies, i.e. algorithms and foundations of computing. <!--SR:!2025-12-03,57,310!2025-11-22,45,290-->
  - software engineering / jobs ::@:: Coding or programming is only "programming-in-the-small". Software engineering is "programming-in-the-large", which includes communication, execution, etc. <!--SR:!2025-12-06,59,310!2025-12-05,58,310-->
    - software engineering / jobs / communication ::@:: communication, documentation, teamwork, translating user requirements, etc. <!--SR:!2025-12-04,58,310!2025-12-08,61,310-->
    - software engineering / jobs / execution ::@:: choose design alternatives, modeling \(at different abstraction levels\), use and apply, etc. <!--SR:!2025-12-01,55,310!2025-12-13,65,310-->
  - software engineering / characteristics ::@:: disciplined \(engineering principles\), multi-person, multi-version, problem solving \(solves real user problems\), quality \(e.g. economic, efficient, reliable, etc.\) <!--SR:!2025-12-09,61,310!2025-11-15,39,290-->
  - software engineering / activities ::@:: knowledge acquisition, modeling, problem solving, rationale management, etc. <!--SR:!2025-12-12,64,310!2025-12-09,62,310-->
    - software engineering / activities / modeling ::@:: Model user requirement. Model the system to be built. <!--SR:!2025-12-09,62,310!2025-11-16,40,290-->
    - software engineering / activities / problem solving ::@:: _Systematically_ \(but not _algorithmically_ as there are changes\) find an appropriate solution according to the user requirement. Note that user requirements can _change_ or be clarified over time. <!--SR:!2025-12-13,65,310!2025-12-03,57,310-->
    - software engineering / activities / knowledge acquisition ::@:: Knowledge about the problem needs to be learnt on the go. It may also need to be _unlearnt_ due to changing requirements or misunderstandings. You may even need to _start over_. <!--SR:!2025-12-02,56,310!2025-12-02,56,310-->
    - software engineering / activities / rationale management ::@:: As acquired knowledge, solutions \(new technologies\), user requirements _change_, we need to _revisit_ decisions and their rationale. <!--SR:!2025-12-10,62,310!2025-12-08,61,310-->
- quiz: [quiz 1](questions/quiz%201.md)

## week 1 lecture

- datetime: 2025-09-03T12:30:00+08:00/2025-09-03T14:20:00+08:00, PT1H50M
- topic: logistics; introduction
- COMP 3111H
  - COMP 3111H / logistics
  - COMP 3111H / textbook ::@:: _Object-Oriented Software Engineering: Using UML, Patterns, and Java, 3/E_, B. Bruegge and A.H. Dutoit, Pearson Education, Inc., 2010. <!--SR:!2025-12-01,55,310!2025-11-30,54,310-->
  - COMP 3111H / tools ::@:: Git, GitHub, Java, <https://app.diagrams.net/>; lab notes, web resources <!--SR:!2025-12-09,62,310!2025-12-03,57,310-->
  - COMP 3111H / grading
  - COMP 3111H / objectives ::@:: _disciplined_ approach to software development, theoretical and practical aspects of software engineering <!--SR:!2025-11-30,54,310!2025-12-10,62,310-->
  - COMP 3111H / course intended learning outcomes \(CILO\)
  - COMP 3111H / motivation ::@:: communication, design, leadership, modeling, project management, etc. <!--SR:!2025-12-14,66,310!2025-12-15,67,310-->
  - COMP 3111H / syllabus ::@:: introduction → modeling language → development approaches → development activities → project management <!--SR:!2025-12-12,64,310!2025-12-15,67,310-->
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

## week 2 pre-lecture

- topic: modeling; unified modeling language; class diagram; association; aggregation; association class; generalization; UML summary
- [Unified Modeling Language](../../../../general/Unified%20Modeling%20Language.md) \(UML\) ::@:: It is a general-purpose, object-oriented, visual modeling language that provides a way to visualize the architecture and design of a system; like a blueprint. <p> It makes us think about the world in a certain way. <!--SR:!2025-09-25,4,331!2025-09-25,4,331-->
  - Unified Model Language / characteristics ::@:: current best practices, independent of software development methodology, industry standard \(especially for object-oriented systems, but can be used for non-OO systems as well\), visual modeling language <!--SR:!2025-09-25,4,338!2025-09-25,4,331-->
  - Unified Model Language / idea ::@:: A \(software\) system can modeled as a _collection_ of _collaborating_ objects. <!--SR:!2025-09-25,4,331!2025-09-25,4,323-->
  - Unified Model Language / building blocks ::@:: diagrams, relations, things, etc. <!--SR:!2025-09-25,4,338!2025-09-25,4,323-->
  - Unified Model Language / mechanisms ::@:: adornments, division, extension, specification, etc. <!--SR:!2025-09-25,4,323!2025-09-25,4,338-->
  - Unified Model Language / architectures ::@:: They are perspectives to build a requirement model and solution model: deployment view, implementation view, logical view, process view, use-case view, etc. <!--SR:!2025-09-25,4,331!2025-09-25,4,331-->
  - Unified Model Language / motivation ::@:: Models can describe the _essential_ details of reality only. This facilitates better communication \(e.g. ensure the system idea is the same\) among different stakeholders, e.g. clients, developers, etc. This also allows focusing on the _big picture_ without excess details \(e.g. programming-in-the-large, etc.\). By reducing _complexity_, user requirements are better _understood_, architectures/designs are _cleaner_, and implementations are more _maintainable_. <!--SR:!2025-09-25,4,338!2025-09-25,4,323-->
  - Unified Model Language / object orientation ::@:: Many application domains can be modeled easily using _objects_. The _semantic gap_ is smaller. This is also how most people view reality. <!--SR:!2025-09-25,4,331!2025-09-25,4,338-->
  - Unified Model Language / abstraction levels ::@:: requirements: A _requirement model_ is constructed. Objects and their relations in the _application domain_ are identified. Their _implementation_ details are omitted. <br/> analysis, design: A _solution model_ is constructed. On top of the _requirement model_, _interface_ implementation details are considered, but no _internal_ implementation details. <br/> implementation: A _solution model_ is _implemented_. Even _internal_ implementation details are considered. <!--SR:!2025-09-25,4,338!2025-09-25,4,331-->
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
  - Unified Model Language / static modeling ::@:: It is for modeling data. <!--SR:!2025-09-25,4,323!2025-09-25,4,331-->
  - Unified Model Language / dynamic modeling ::@:: It is for modeling programs \(program behavior\). <!--SR:!2025-09-25,4,331!2025-09-25,4,331-->
- quiz: [quiz 3](questions/quiz%203.md)

## week 2 lecture

- datetime: 2025-09-10T12:30:00+08:00/2025-09-10T14:20:00+08:00, PT1H50M
- topic: modeling; unified modeling language; class diagram; association; aggregation; association class; generalization; UML summary
- [§ week 2 pre-lecture](#week%202%20pre%20lecture)
- [questions § week 2 lecture](questions/index.md#week%202%20lecture)

## week 2 lab

- datetime: 2025-09-11T18:00:00+08:00/2025-09-11T19:50:00+08:00, PT1H50M
- topic:

## week 3 pre-lecture

- topic: software development; project risks; project planning; software development process; agile; unified process
- [software](../../../../general/software.md) ::@:: It consists of computer programs that instruct the execution of a computer. It also includes design documents and specifications. <!--SR:!2025-09-25,4,323!2025-09-25,4,331-->
  - software / nature ::@:: does not wear out, easy to create and modify, easy to mass produce, intangible, labor-intensive <!--SR:!2025-09-25,4,323!2025-09-25,4,331-->
    - software / nature / intangible ::@:: hard to appreciate its development effort, assess its quality, visualize <!--SR:!2025-09-25,4,338!2025-09-25,4,331-->
    - software / nature / easy to mass produce ::@:: It is easy to copy and distribute software. The main cost is development, not manufacture. <!--SR:!2025-09-25,4,331!2025-09-25,4,331-->
    - software / nature / labor-intensive ::@:: Design and programming is hard to automate. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
    - software / nature / easy to create and modify ::@:: While easy to create and modify, it is also easy to create and modify software _badly_, creating _defects_ or decreasing _maintainability_. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
    - software / nature / does not wear out ::@:: Unlike physically assets, software do not wear out. However, the codebase do "wear out" in the sense of usually getting worse when modified, creating _defects_ or decreasing _maintainability_. <!--SR:!2025-09-25,4,338!2025-09-25,4,331-->
  - software / types ::@:: social aspects, timeliness, uses <!--SR:!2025-09-25,4,338!2025-09-25,4,323-->
    - software / types / uses ::@:: custom, embedded, generic <p> They can be characterized by copies in use, development effort, and source of user requirements. <!--SR:!2025-09-25,4,338!2025-09-25,4,323-->
      - software / types / uses / generic ::@:: copies in use: medium \(relative to embedded\) <br/> development effort: medium \(relative to custom\) <br/> source of user requirements: market research <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
      - software / types / uses / custom ::@:: copies in use: low <br/> development effort: high <br/> source of user requirements: client needs <!--SR:!2025-09-25,4,331!2025-09-25,4,323-->
      - software / types / uses / embedded ::@:: copies in use: high \(there are _many_ embedded devices...\) <br/> development effort: low \(due to less functionalities\) <br/> source of user requirements: client needs, hardware needs <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
    - software / types / timeliness ::@:: data processing, real-time processing <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
      - software / types / timeliness / data processing ::@:: organize and store _business data_, which may not be _real time_ <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
      - software / types / timeliness / real-time processing ::@::  control devices or processes in _real time_ <!--SR:!2025-09-25,4,323!2025-09-25,4,323-->
    - software / types / social aspects ::@:: technical, social-technical <!--SR:!2025-09-25,4,323!2025-09-25,4,331-->
      - software types / social aspects / technical ::@:: does not include _knowledge_ of _work procedures and processes_ <p> This is the main focus of software engineering. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
      - software types / social aspects / social-technical ::@:: includes _knowledge_ of _work procedures and processes_ <p> This is less _emphasized_ by software engineering. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
- [software development](../../../../general/software%20development.md) ::@:: It is the process of designing and implementing a software solution to satisfy a user. The process is more encompassing than programming, writing code, in that it includes conceiving the goal, evaluating feasibility, analyzing requirements, design, testing and release. <!--SR:!2025-09-25,4,323!2025-09-25,4,331-->
  - software development / types ::@:: green field projects, evolutionary projects \(most common\), component or framework projects <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
    - software development / types / green field projects ::@:: Develop a _new_ software from scratch. <!--SR:!2025-09-25,4,338!2025-09-25,4,331-->
    - software development / types / evolutionary projects ::@:: _Maintain_ an existing software, to _adapt_ for new environment, _correct_ detects, _enhance_ features, or _re-engineering_ \(_perfect_\) for maintainability. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
    - software development / types / component or framework projects ::@:: _Reuse_ an existing component or framework to create a new software. The existing component or framework is designed for reuse in new software but needs to be _adapted_ for _specific requirements_. <!--SR:!2025-09-25,4,338!2025-09-25,4,331-->
- [systems development life cycle](../../../../general/systems%20development%20life%20cycle.md) \(SDLC\) ::@:: It describes the typical phases and progression between phases during the development of a computer-based system; from inception to retirement. At base, there is just one life cycle even though there are different ways to describe it; using differing numbers of and names for the phases. <p> It is still often used for large complex systems. <!--SR:!2025-09-25,4,338!2025-09-25,4,331-->
  - systems development life cycle / name ::@:: \(__this course__: use "software development life cycle"\) <!--SR:!2025-09-25,4,323!2025-09-25,4,323-->
  - systems development life cycle / lifecycle ::@:: A software from its _inception_ to _retirement_ consist of many groups of 4 phases \(see below\). <!--SR:!2025-09-25,4,331!2025-09-25,4,331-->
  - systems development life cycle / phases ::@:: definition \(what\) → design \(how\) → development \(build\) → operation \(use\) <p> After each phase is a _major milestone_. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
  - systems development life cycle / motivation ::@:: It _structures_ software development. The phases allows for _control_ and _management_, e.g. deliverables, _milestones_. <!--SR:!2025-09-25,4,331!2025-09-25,4,338-->
  - systems development life cycle / milestone ::@:: It is a management _decision point_, where the management can make major decisions. <!--SR:!2025-09-25,4,323!2025-09-25,4,338-->
- [project management](../../../../general/project%20management.md) ::@:: It is the process of supervising the work of a team to achieve all project goals within the given constraints. <!--SR:!2025-09-25,4,323!2025-09-25,4,331-->
  - project management / 4Ps ::@:: A _project_ involves _people_ \(input\) using _processes_ \(input\) to produce _products_ \(output\) according to requirements from the application domain \(input\). <!--SR:!2025-09-25,4,331!2025-09-25,4,338-->
    - project management / 4Ps / process ::@:: set of activities: tools \(support\), workflows, etc. <!--SR:!2025-09-25,4,331!2025-09-25,4,331-->
    - project management / 4Ps / people ::@:: stakeholders: clients, developers, end users, etc. <!--SR:!2025-09-25,4,331!2025-09-25,4,338-->
    - project management / 4Ps / product ::@:: set of artifacts: code, manuals, models, etc. <!--SR:!2025-09-25,4,338!2025-09-25,4,331-->
    - project management / 4Ps / project ::@:: It requires _control_, _management_, and _control_. It involves a _project plan_. <!--SR:!2025-09-25,4,323!2025-09-25,4,323-->
      - project management / 4Ps / project / plan ::@:: activities & tasks, monitoring & reporting, organization, resources, risks, schedule, scope \(i.e. constraints and objectives; e.g. budget, time, etc.\) <!--SR:!2025-09-25,4,338!2025-09-24,3,303-->
- [software development process](../../../../general/software%20development%20process.md) ::@:: It prescribes a process for developing software. It typically divides an overall effort into smaller steps or sub-processes that are intended to ensure high-quality results. The process may describe specific deliverables – artifacts to be created and completed. <p> \(__this course__: It is a process _template_ that is _adaptable_ for different application domains.\) <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
- project management
  - project management / scope ::@:: The _first_ task when planning a project: understand scope, i.e. constraints and objectives. <p> define problem \(e.g. design goals\) → analyze requirements \(e.g. estimate system size\) → make top-level diagram \(i.e. estimate the system\) → estimate effort and time \(i.e. prepare the rest of the project plan\) <!--SR:!2025-09-25,4,331!2025-09-25,4,331-->
  - project management / steps ::@:: scope → risks → schedule \(e.g. deliverables\) → implement <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
- [project risk management](../../../../general/project%20risk%20management.md) ::@:: Within project management, it refers to activities for minimizing project risks, and thereby ensuring that a project is completed within time and budget, as well as fulfilling its goals. <!--SR:!2025-09-25,4,323!2025-09-25,4,338-->
  - project risk management / risk ::@:: Anything that can go wrong in a project, which endangers project success. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
    - project risk management / risk / types ::@:: estimation, organization, people, requirements, technology, tools, etc. <!--SR:!2025-09-25,4,338!2025-09-25,4,323-->
  - project risk management / mitigations ::@:: avoid, confine, mitigate, monitor, etc. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
  - project risk management / risk
    - project risk management / risk / characteristics ::@:: accuracy of estimates of characteristics \(e.g. rationale, etc.\), consequences \(e.g. nature, scope, timing, etc.\), likelihood \(e.g. boolean, probabilities, subjective, etc.\) <p> Use these to _prioritize_ tasks by _perceived impact_ on the project. <!--SR:!2025-09-25,4,338!2025-09-25,4,331-->
  - project risk management / mitigations
    - project risk management / mitigations / characteristics ::@:: benefit, cost <p> We should perform cost–benefit analysis. <!--SR:!2025-09-25,4,331!2025-09-25,4,338-->
- [Pareto principle](../../../../general/Pareto%20principle.md) ::@:: It states that, for many outcomes, roughly 80% of consequences come from 20% of causes \(the "vital few"\). <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
- project risk management
  - project risk management / Pareto principle ::@:: 80% of risk _impact_ is roughly accounted by 20% of identified risks \(in numbers\). <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
- project management
  - project management / organization ::@:: number of people, roles and responsibilities, teams, etc. <!--SR:!2025-09-25,4,323!2025-09-25,4,323-->
    - project management / organization / good practices ::@:: We should assign people with _experience relevant_ to their tasks. <p> Teams should be modular and have clear responsibilities, e.g. a team corresponds to one or more identified parts of the system. This helps with having the _right level of communication_. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
  - project management / activities & tasks ::@:: A _task_ is a well-defined work assignment for a role. An _activity_ is a group of related tasks. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
    - project management / activities & tasks / principles ::@:: agile-driven: details are _incrementally_ planned as the project progresses <br/> plan-driven: details are planned at project _start_ <p> Which one to use highly depends on the project. Often, a combination is the best. <!--SR:!2025-09-25,4,338!2025-09-25,4,323-->
  - project management / schedule ::@:: deliverables \(outputs\), milestones \(_important_ management decision points\), resources assignment, time estimates, ordering \(dependency\) <!--SR:!2025-09-25,4,331!2025-09-25,4,338-->
    - project management / schedule / levels ::@:: \(high level, rigid\) master: client, management &gt; macro: day-to-day management &gt; micro: team management \(low level, flexible\) <!--SR:!2025-09-25,4,338!2025-09-25,4,331-->
    - project management / schedule / tools ::@:: charts, graphs \(dependency graphs\) <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
  - project management / estimates ::@:: Quantify something before it occurs. It carries inherent _risk_. <p> For a project, it includes cost, duration, effort, productivity, size, etc. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
    - project management / estimates / skills ::@:: _courage_, experience, historical data, model <!--SR:!2025-09-25,4,338!2025-09-25,4,323-->
    - project management / estimates / tips ::@:: better project scoping, divide and conquer the thing to be estimated, more historical data, etc. <!--SR:!2025-09-25,4,323!2025-09-25,4,338-->
  - project management / process ::@:: A _sequence_ of _activities_ \(i.e. _workflows_\) to _transform_ user requirements into products. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
    - project management / process / elements ::@:: guiding principles. major activities, subprocesses, etc. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
    - project management / process / details ::@:: A process uses _resources_ to transform _inputs_ to _outputs_ \(including _intermediates_\) under some _constraints_ \(or _controls_\). There are _entry_ and _exit_ criteria for each activity. <p> A process may have _subprocesses_. <!--SR:!2025-09-25,4,331!2025-09-25,4,338-->
    - project management / process / importance ::@:: communication is better, consistency, division of labor, eases project management, eases training, expertise are reused, productivity is higher, products are better, structure, etc. <!--SR:!2025-09-25,4,331!2025-09-25,4,338-->
- quiz: [quiz 4](questions/quiz%204.md)
- software development process
  - software development process / common steps ::@:: gather _requirements_ → _analyze_ and _design_ → _implement_ → _test_ <!--SR:!2025-09-25,4,331!2025-09-25,4,338-->
  - software development process / differences ::@:: The major differences are: carrying out the steps, combining the steps, and emphasizing the steps. These lead to different strengths and weaknesses. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
  - software development process / types ::@:: monolithic, iterative and incremental \(these two are slightly _different_ things\) <!--SR:!2025-09-25,4,338!2025-09-25,4,323-->
  - software development process / monolithic ::@:: 1+ items: waterfall, etc. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
    - software development process / monolithic / characteristics ::@:: All functionalities are planned and the entire system is implemented at once. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
  - software development process / iterative and incremental ::@:: 6+ items: agile, code and fix, phased release, prototyping, spiral, unified process \(UP\) <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
    - software development process / iterative and incremental / properties ::@:: incremental: Separate functions are implemented one-by-one. <br/> iterative: Each function is implemented and refined over time. <br/> both: possible <!--SR:!2025-09-25,4,323!2025-09-25,4,331-->
- [waterfall model](../../../../general/waterfall%20model.md) ::@:: It is the process of performing the typical software development life cycle \(SDLC\) phases in sequential order. Each phase is completed before the next is started, and the result of each phase drives subsequent phases. <!--SR:!2025-09-25,4,323!2025-09-25,4,338-->
  - waterfall model / steps ::@:: gather requirements \(requirements specification document\) → analysis & design \(design specification document\) → implementation \(modules\) → test \(tested modules\) → maintain <!--SR:!2025-09-25,4,338!2025-09-25,4,323-->
  - waterfall model / additional steps ::@:: other deliverables \(e.g. code, docs, training materials, etc.\), review \(for correctness and standards\) <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
  - waterfall model / use cases ::@:: Requirements are well-defined, well-understood, and very unlikely to change. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
  - waterfall model / comparison ::@:: Compared to alternative SDLC methodologies such as Agile, it is among the least iterative and flexible, as progress flows largely in one direction \(like a waterfall\) through the phases of conception, requirements analysis, design, construction, testing, deployment, and maintenance. <!--SR:!2025-09-25,4,331!2025-09-25,4,331-->
  - waterfall model / advantages ::@:: discipline \(formality, rigor\), docs are approved and standardized, easy and predictable development, fits well with non-software engineering processes \(e.g. hardware development\) <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
  - waterfall model / disadvantages ::@:: assumes sequentiality and linearity, different languages in different phases, rigid as it freezes the results of a phase, user feedback cannot be incorporated on the fly <!--SR:!2025-09-25,4,338!2025-09-25,4,323-->
- software development process
  - software development process / code and fix ::@:: Requirements are obtained \(and usually stored in the developer's mind only\). Loop implementation and testing until it is completed. <!--SR:!2025-09-25,4,331!2025-09-25,4,331-->
    - software development process / code and fix / characteristics ::@: changing requirements, many changes, messy code structure, unsuitable for large systems <!--SR:!2025-09-25,4,338-->
    - software development process / code and fix / disadvantages ::@:: fail to meet expectations, over budget, over schedule, uncontrollable, unpredictable <!--SR:!2025-09-25,4,331!2025-09-25,4,338-->
- [software prototyping](../../../../general/software%20prototyping.md) ::@:: It is the activity of creating prototypes of software applications, i.e., incomplete versions of the software program being developed. <!--SR:!2025-09-25,4,331!2025-09-25,4,338-->
  - software prototyping / steps ::@:: gather and _refine_ requirements → design → prototype → evaluate → EITHER refine prototype \(→ design\) OR engineer product \(which may not be the final product\) <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
  - software prototyping / comparison ::@:: Similar to code and fix, but there is slightly more discipline and incorporates user feedback. <!--SR:!2025-09-25,4,323!2025-09-25,4,338-->
  - software prototyping / characteristics ::@:: exploratory \(e.g. functions, user interfaces, etc.\), good for unknown or vague requirements <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
  - software prototyping / advantages ::@:: explore multiple different solutions, explore user requirements, incorporates user feedback <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
  - software prototyping / disadvantages ::@:: incomplete process \(engineering the final product may need a separate process\), invisible to management, missing or sparse docs <!--SR:!2025-09-25,4,331!2025-09-25,4,338-->
- [spiral model](../../../../general/spiral%20model.md) ::@:: It is a risk-driven software development process model. Based on the unique risk patterns of a given project, the spiral model guides a team to adopt elements of one or more process models, such as incremental, waterfall, or evolutionary prototyping. <!--SR:!2025-09-25,4,338!2025-09-25,4,331-->
  - spiral model / steps ::@:: plan → risk analysis → \(EITHER go OR no go\) → engineer → evaluate → \(repeat until we have a complete system\) <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
  - spiral model / the spiral ::@:: The 4 quadrants of a 2D plane are respectively the 4 steps \(clockwise from quadrant II\), and the process is represented by an arrowheads spiraling outwards. <!--SR:!2025-09-25,4,323!2025-09-25,4,331-->
  - spiral model / advantages ::@:: incorporates risk evaluation, incorporates user feedback to meet expectations \(from evaluate and plan\), iterative and incremental <!--SR:!2025-09-25,4,331!2025-09-25,4,338-->
  - spiral model / disadvantages ::@:: expertise on risk evaluation required, for internal development rather than contract development, phases are not elaborated \(a separate process may be used\) <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
- [software release life cycle](../../../../general/software%20release%20life%20cycle)
  - software release life cycle / name ::@:: \(__this course__: use _phased release_\) <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
  - software release life cycle / motivation ::@:: Since change is inevitable \(by user requirements\), so produce releases over time and make changes accordingly. <!--SR:!2025-09-25,4,338!2025-09-25,4,323-->
  - software release life cycle / flow ::@:: Developers release multiple _development releases_ over time. _Concurrently_, users make _use/production releases_ out of each development release. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
  - software release life cycle / incremental and iterative ::@:: Releases can be incremental or iterative or both. Often both are used in practice. <p> incremental: Separate functions of a system are implemented one-by-one \(partial system\). If used alone, each function is fully implemented at once \(full functionality\). <br/> iterative: Functions are implemented and refined over time \(partial functionality\). If used alone, all functions begin implementation at once \(full system\). <!--SR:!2025-09-25,4,323!2025-09-25,4,323-->
  - software release life cycle / advantages ::@:: apply appropriate expertise, early training, early user feedback, frequent releases, promote modularity, reduce risk <!--SR:!2025-09-25,4,338!2025-09-25,4,323-->
  - software release life cycle / disadvantages ::@:: common facilities for all functions are hard to identify, each function \(part\) needs to be small <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
- [agile software development](../../../../general/agile%20software%20development.md) ::@:: It is an umbrella term for approaches to developing software that reflect the values and principles agreed upon by _The Agile Alliance_, a group of 17 software practitioners, in 2001. <!--SR:!2025-09-25,4,323!2025-09-25,4,338-->
  - agile software development / principles ::@:: emphasized: client involvement, individuals and interactions, responsive to change, working software <br/> deemphasized: comprehensive docs, contract negotiation, plan following, processes and tools <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
  - agile software development / methods ::@:: continuous integration \(CI\), extreme programming \(XP\), scrum, etc. <!--SR:!2025-09-25,4,338!2025-09-25,4,323-->
  - agile software development / practices ::@:: pair programming: implement a feature <br/> planning poker: estimate implementation time <br/> test-driven development \(TDD\) <br/> etc. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
- [extreme programming](../../../../general/extreme%20programming.md) \(XP\) ::@:: It is a software development methodology intended to improve software quality and responsiveness to changing customer requirements. As a type of agile software development, it advocates frequent releases in short development cycles, intended to improve productivity and introduce checkpoints at which new customer requirements can be adopted. <!--SR:!2025-09-25,4,338!2025-09-25,4,323-->
  - extreme programming / steps ::@:: gather and analyze requirements → implement → \(repeat _quickly_\) <!--SR:!2025-09-25,4,331!2025-09-25,4,338-->
  - extreme programming / gather and analyze requirements ::@:: The developer determines features needed and estimate cost and time. Then the client selects features for each _iteration_. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
  - extreme programming / implement ::@:: Each _iteration_ has many tasks.The developer implement \(pair programming\) and design test cases \(TDD\). <!--SR:!2025-09-25,4,331!2025-09-25,4,323-->
- [continuous integration](../../../../general/continuous%20integration.md) \(CI\) ::@:: It is the practice of integrating source code changes frequently and ensuring that the integrated codebase is in a workable state. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
  - continuous integration / mechanism ::@:: Typically, developers merge changes to an integration branch, and an automated system \(__this course__: CI server\) builds and tests the software system. Often, the automated process runs on each commit or runs on a schedule such as once a day. <p> \(__this course__: Work is submitted daily to the main repository. CI servers runs build and test scripts. They notify if there are failures.\) <!--SR:!2025-09-25,4,338!2025-09-25,4,331-->
  - continuous integration / advantages ::@:: automate build and test, catch build-breaking bugs early, check progress, integrate and test early, reduce integration conflicts <!--SR:!2025-09-25,4,323!2025-09-25,4,331-->
- [scrum](../../../../general/scrum.md) ::@:: It is an agile team collaboration framework commonly used in software development and other industries. <!--SR:!2025-09-25,4,323!2025-09-25,4,338-->
  - scrum / overview ::@:: It specifies what to do to develop a software product. But the detailed specifics \(how to do\) are decided by teams. <p> Requirements are items in a _product backlog_. The _product owner_ \(the client\) sets _priorities_. Then, the software is developed in _sprints_. Teams _self-organize_ to determine the best way to deliver the product. <!--SR:!2025-09-25,4,323!2025-09-25,4,338-->
  - scrum / sprint ::@:: Scrum prescribes for teams to break work into goals to be completed within time-boxed iterations, called _sprints_. Each sprint is no longer than one month and commonly lasts two weeks. The scrum team assesses progress in time-boxed, stand-up meetings of up to 15 minutes, called _daily scrums_. At the end of the sprint, the team holds two further meetings: one sprint review to demonstrate the work for stakeholders and solicit feedback, and one internal sprint retrospective. <!--SR:!2025-09-25,4,338!2025-09-25,4,323-->
    - scrum / sprint / activities ::@:: In a sprint, the software is designed, implemented, and tested. The requirements are not allowed to change. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
  - scrum / framework ::@:: artifacts, meetings, roles <!--SR:!2025-09-25,4,338!2025-09-25,4,331-->
  - scrum / roles ::@:: product owner, scrum master, team <!--SR:!2025-09-25,4,331!2025-09-25,4,331-->
  - scrum / meetings ::@:: sprint planning → daily scrum meeting → sprint review \(external-oriented\), sprint retrospective \(internal-oriented\) <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
  - scrum / artifacts ::@:: burndown charts, product backlog, spring backlog <!--SR:!2025-09-25,4,323!2025-09-25,4,323-->
  - scrum / roles
    - scrum / roles / product owner ::@:: The key stakeholder represents the client or end users. It defines and prioritize requirements, and adjusts both every iteration. It decides on content and timing. It accepts or rejects results. <!--SR:!2025-09-25,4,338!2025-09-25,4,331-->
    - scrum / roles / scrum master ::@:: enable close cooperation, enact scrum values and practices, ensure functional and productive teams, remove progress obstacles, shield external interferences <!--SR:!2025-09-25,4,331!2025-09-25,4,338-->
  - scrum / meetings
    - scrum / meetings / sprint planning ::@:: Considers business conditions, current product, product backlog, team capacity, technology, etc. Prioritize product backlog to select _sprint goal_. Then, plan to achieve the sprint goal, and create a _sprint backlog_ from product backlog and estimate time. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
    - scrum / meetings / daily scrum meeting ::@:: review: What did you do yesterday? <br/> plan: What will you do today? <br/> obstacles: Is anything in your way? <!--SR:!2025-09-25,4,323!2025-09-25,4,331-->
  - scrum / artifacts
    - scrum / artifacts / product backlog ::@:: Requirements, which have values to the client or end users. Prioritized by the product owner and re-prioritized before each sprint. <!--SR:!2025-09-25,4,323!2025-09-25,4,323-->
    - scrum / artifacts / spring backlog ::@:: Selected items from the product backlog based on item priority and team capacity. Some product backlog items may become multiple spring backlog items. During the spring, team members select items to work on. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
    - scrum / artifacts / burndown chart ::@:: For each task, we _estimate_ the hours remaining to complete it. Then, the chart sums them up and plot them as a line chart, which shows the _estimated_ total hours remaining to complete the sprint. <p> It may _fluctuate_, but should _tend to zero_, otherwise you have problems in your sprint. <!--SR:!2025-09-25,4,338!2025-09-25,4,331-->
- agile software development
  - agile software development / advantages ::@:: adaptable/flexible to changing requirements, faster speed-to-market, fewer defects, immediate user feedback <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
  - agile software development / disadvantages ::@:: close collaboration between developers and product owner required, daily meetings may be costly, docs are often missing, scope creep due to adding requirements <!--SR:!2025-09-25,4,331!2025-09-25,4,331-->
- software development process
  - software development process / characteristics ::@:: abstraction or generality \(of process\), adaptable to changes, discipline \(formal, rigor\), incremental, risk assessment, separation of concerns \(modularity\) <!--SR:!2025-09-25,4,338!2025-09-25,4,331-->
  - software development process / discipline ::@:: spiral: The 4 phases must be followed in a spiral without backtracking. <br/> waterfall: SDLC is followed sequentially without possibility of backtracking. <!--SR:!2025-09-25,4,331!2025-09-25,4,338-->
  - software development process / separation of concerns ::@:: phased release: Development and release is separate. <br/> spiral: Planning, risk analysis, engineering, and evaluation are separate. <br/> waterfall: Each phase of SDLC is separate. <!--SR:!2025-09-25,4,338!2025-09-25,4,331-->
  - software development process / abstraction or generality ::@:: spiral: Allows using other processes for the actual development and testing. <br/> waterfall: As a direct implementation of the general SDLC. <!--SR:!2025-09-25,4,323!2025-09-25,4,338-->
  - software development process / adaptable to changes ::@:: agile: By its nature. <br/> phased release: Releases happen over time. <br/> spiral: Planning happens periodically. <!--SR:!2025-09-25,4,331!2025-09-25,4,331-->
  - software development process / incremental ::@:: agile: Many sprints are needed. <br/> phased release: Many releases are needed. <br/> prototyping: Many prototypes are needed. <br/> spiral: Many spirals are needed. <!--SR:!2025-09-25,4,331!2025-09-25,4,331-->
  - software development process / risk assessment ::@:: spiral: The only process to explicitly integrate risk analysis. <!--SR:!2025-09-25,4,338!2025-09-25,4,331-->
- [unified process](../../../../general/unified%20process.md) ::@:: It is an iterative and incremental software development process framework. <p> It is not simply a process, but rather an extensible framework which should be customized for specific organizations or projects. <!--SR:!2025-09-25,4,338!2025-09-25,4,331-->
  - unified process / cycle ::@:: inception → elaboration → construction → transition <!--SR:!2025-09-25,4,331!2025-09-25,4,331-->
  - unified process / phase ::@:: It may be divided into a series of timeboxed _iterations_. Each iteration results in an _increment_, which is a release of the system that contains added or improved functionality compared with the previous release. <!--SR:!2025-09-25,4,331!2025-09-25,4,331-->
    - unified process / phase / iteration & increment ::@:: \(__this course__: Each iteration produces a _working product_. Each increment establishes a _system baseline_.\) <!--SR:!2025-09-25,4,338!2025-09-25,4,323-->
  - unified process / activities ::@:: The activities _vary_, but can usually be categorized into engineering activities and management activities <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
    - unified process / activities / engineering ::@:: for reference; requirements capture → analysis → design → implement → test → \(management\) <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
    - unified process / activities / management ::@:: for reference; \(engineering\) → software quality assurance → project management <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
  - unified process / diagram ::@:: The diagram charts phases and iterations on the _x_-axis \(time axis\), and activities on the _y_-axis \(dimension axis\). <p> For each activity, there is an area chart that varies over time \(and can be zero\), showing how the relative emphasis of different disciplines changes over the course of the project. <!--SR:!2025-09-25,4,338!2025-09-25,4,338-->
  - unified process / features ::@:: defines activities: workflows to transform user requirements to a system <br/> defines models abstract or concrete entities that are transformed by workflows; e.g. artifacts <br/> generic: a generic process _framework_ needing to be _specialized_ to use <!--SR:!2025-09-25,4,338!2025-09-25,4,331-->
- software development process
  - software development process / considerations ::@:: people \(e.g. expertise, skills\), project \(e.g. novelty, size, vagueness\), organization \(e.g. accessibility, formality, size\) <!--SR:!2025-09-25,4,338!2025-09-25,4,331-->
- unified process
  - unified process / advantages ::@:: It incorporates _best practices_ from all the previous software development processes and provides a _generic framework_. <!--SR:!2025-09-25,4,323!2025-09-25,4,338-->
- quiz: [quiz 5](questions/quiz%205.md)

## week 3 lecture

- datetime: 2025-09-17T12:30:00+08:00/2025-09-17T14:20:00+08:00, PT1H50M
- topic: software development; project risks; project planning; software development process; agile; unified process
- [§ week 3 pre-lecture](#week%203%20pre%20lecture)
- [questions § week 3 lecture](questions/index.md#week%203%20lecture)

## week 3 lab

- datetime: 2025-09-18T18:00:00+08:00/2025-09-18T19:50:00+08:00, PT1H50M
- topic:

## aftermath

### total

- grades: ?/100
  - statistics: ?
