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

- [UML](UML.md)
- [assignments](assignments/index.md)
- [questions](questions.md)

## week 1 pre-lecture

- topic: introduction; complexity of software development; handling complexity; software engineering
- [software engineering](../../../../general/software%20engineering.md) ::@:: It is a branch of both computer science and engineering focused on designing, developing, testing, and maintaining software applications. It involves applying engineering principles and computer programming expertise to develop software systems that meet user needs.
- [source lines of code](../../../../general/source%20lines%20of%20code.md) \(SLOC\) ::@:: It is a software metric used to measure the size of a computer program by counting the number of lines in the text of the program's source code.
  - source lines of code / acronyms ::@:: - LLOC: logical lines of code; logical SLOC <br/> - LOC: lines of code; physical SLOC <br/> - MLOC: million lines of code <br/> - SLOC: source lines of code
  - source lines of code / examples ::@:: \(less\) <br/> 1. Rome: Total War <br/> 2. Boeing 787 &lt; F-35 Fighter Jet <br/> 3. Windows 7 &lt; Windows 10 <br/> 4. Facebook <br/> 5. Mac OS X <br/> 6. luxury passenger car <br/> \(more\)
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
      - programming complexity / problems / development / statistics ::@:: \(2012\) For _large_ software projects in _decreasing_ proportion: <p> 1. deliver less value <br/> 2. over budget <br/> 3. company threatening <br/> 4. over time <br/> 5. etc.
  - programming complexity / mitigations ::@:: There are many desirable _characteristics_ considered part of quality. It is impossible and unnecessary to achieve all of them. <p> Instead, we should under the client's _goals_ and _prioritize_ certain characteristics. This reduces complexity somewhat.
    - programming complexity / mitigations / characteristics ::@:: correct, efficient, evolvable, interoperable, maintainable, portable, productive, reliable, repairable, reusable, robust, timely, usable, verifiable, visible, etc.
- [modular programming](../../../../general/modular%20programming.md) ::@:: It is a programming paradigm that emphasizes organizing the functions of a codebase into independent modules – each providing an aspect of a computer program in its entirety without providing other aspects.
  - modular programming / motivation ::@:: Humans cannot understand things that are too _complex_. Often, we break down a complex systems into _modules_, parts of a system that makes sense to _consider separately_ and interact with other modules. This is known as _divide and conquer_.
  - modular programming / module ::@:: It is a part of a system that can be _considered separately_. To model _interactions_ with other modules, they are limited to _interfaces_, which _abstracts_ and _encapsulates_ a module via _information hiding_.
    - modular programming / module / abstraction ::@:: The internals of a module are hidden away. Interaction is defined via its interface only. The usage of the module by other modules can be understood by looking at its interface only \(ideally\). This reduces complexity of _understanding_ the system.
    - modular programming / module / encapsulation ::@:: When we want to modify a module, we only need to modify the module without changing other modules \(ideally\). The internals of a module can be changed without affecting other modules \(ideally\). This reduces _maintenance_ burden.
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
  - COMP 3111H / project ::@:: specification \(from system requirements\) → implementation and testing
- [§ week 1 pre-lecture](#week%201%20pre-lecture)
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
    - COMP 3111H / lab extra / tools ::@:: The development stack is a modern Java SE environment \(JDK 21\) running on IntelliJ IDEA 2024, with access to the free Llama-based models hosted at Groq \(<https://groq.com/>\) and the Continue API for code generation and understanding.
    - COMP 3111H / lab extra / exercises ::@:: setup Groq & Continue; generate login screen in JavaFX; understand generated code, generate test
    - COMP 3111H / lab extra / Groq API keys ::@:: Create a Groq account, explore available models in the Playground, then generate an API key from "API Keys". This key is one-time visible; store it securely. <p> As of 2025, Groq is unavailable in Hong Kong.
    - COMP 3111H / lab extra / models ::@:: examples: Llama3.1 70b Chat, etc.
    - COMP 3111H / lab extra / prompts ::@:: You can prompt it to edit code, explain code, generate docs, generate tests, and etc. Take care to use it with some _human oversight_!
      - COMP 3111H / lab extra / prompts / edit ::@:: examples: <p> - Change the GUI to a login screen that requires the user to input 'Username' and 'Password', and there should only be one button 'Login'. <br/> - Change login to successful only when the username is equal to the password, and fail in another case.
      - COMP 3111H / lab extra / prompts / explain ::@:: examples: <p> Carefully read and understand the code, clearly describe the functionality of both classes and explain the method of each class.
      - COMP 3111H / lab extra / prompts / docs ::@:: Add Javadoc descriptions to the classes and methods. Also add comments to the implementation details for high-level explanation.

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
  - Unified Model Language / abstraction levels ::@:: - requirements: A _requirement model_ is constructed. Objects and their relations in the _application domain_ are identified. Their _implementation_ details are omitted. <br/> - analysis, design: A _solution model_ is constructed. On top of the _requirement model_, _interface_ implementation details are considered, but no _internal_ implementation details. <br/> - implementation: A _solution model_ is _implemented_. Even _internal_ implementation details are considered.
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
- [UML](UML.md)
  - [§ common mistakes](UML.md#common%20mistakes)
  - [§ common mistakes: bad name](UML.md#common%20mistakes%20bad%20name)
  - [§ common mistakes: "has" relation](UML.md#common%20mistakes%20"has"%20relation)
  - [§ common mistakes: ER model](UML.md#common%20mistakes%20ER%20model)
  - [§ common mistakes: unary association roles](UML.md#common%20mistakes%20unary%20association%20roles)
  - [§ common mistakes: implementation details](UML.md#common%20mistakes%20implementation%20details)
  - [§ common mistakes: association class](UML.md#common%20mistakes%20association%20class)
  - [§ common mistakes: uniqueness of names](UML.md#common%20mistakes%20uniqueness%20of%20names)
  - [§ common mistakes: XOR associations](UML.md#common%20mistakes%20XOR%20associations)
  - [§ common mistakes: operations as associations](UML.md#common%20mistakes%20operations%20as%20associations)
  - [§ common mistakes: redundant associations](UML.md#common%20mistakes%20redundant%20associations)
  - [§ common mistakes: real world knowledge](UML.md#common%20mistakes%20real%20world%20knowledge)
  - [§ common mistakes: misusing modeling elements](UML.md#common%20mistakes%20misusing%20modeling%20elements)
- [§ week 2 pre-lecture](#week%202%20pre-lecture)
- [questions § week 2 lecture](questions/index.md#week%202%20lecture)

## week 2 lab

- datetime: 2025-09-11T18:00:00+08:00/2025-09-11T19:50:00+08:00, PT1H50M
- topic: IntelliJ IDEA; Git; GitHub
- COMP 3111H
  - COMP 3111H / labs ::@:: The lab series has an assessment weight of 10%. It is split into two distinct phases: a _tool-based_ phase \(Git, Java basics, JavaFX, project briefing & UML\) and an _implementation_ phase \(GitHub, debugger, unit testing, conflict resolution\). Both phases assist in working on the group project.
  - COMP 3111H / grading
  - COMP 3111H / lab 1 ::@:: IntelliJ IDEA; Git; GitHub
    - COMP 3111H / lab 1 / Git ::@:: It is the most widely used tool for _version control_.
    - COMP 3111H / lab 1 / GitHub ::@:: It is the largest _web-based_ source code hosting service \(software _forge_\) integrated with version control.
    - COMP 3111H / lab 1 / exercises ::@:: create Java project in IntelliJ IDEA; setup Git; setup repository on GitHub
    - COMP 3111H / lab 1 / Git setup ::@:: Students create a local Git repository from an IntelliJ Maven project, then commit changes to the repository.
    - COMP 3111H / lab 1 / GitHub tokens ::@:: Personal Access Tokens \(PATs\) are generated in the GitHub settings under _Developer settings → Personal access tokens_ to authenticate command-line operations. The token should have a custom expiry of more than six months, include the `repo` scope, and be stored securely.
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
      - software / types / uses / generic ::@:: - copies in use: medium \(relative to embedded\) <br/> - development effort: medium \(relative to custom\) <br/> - source of user requirements: market research
      - software / types / uses / custom ::@:: - copies in use: low <br/> - development effort: high \(due to having to capture requirements from the client\) <br/> - source of user requirements: client needs
      - software / types / uses / embedded ::@:: - copies in use: high \(there are _many_ embedded devices...\) <br/> - development effort: low \(due to knowing all requirements already and less functionalities\) <br/> - source of user requirements: client needs, hardware needs
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
  - project management / 4Ps ::@:: A _project_ \(center\) involves _people_ \(input\) using _processes_ \(input\) to produce _products_ \(output\) according to requirements from the application domain \(input\).
    - project management / 4Ps / process ::@:: set of activities: tools \(support\), workflows, etc.
    - project management / 4Ps / people ::@:: stakeholders: clients, developers, end users, etc.
    - project management / 4Ps / product ::@:: set of artifacts: code, manuals, models, etc.
    - project management / 4Ps / project ::@:: It requires _planning_, _management_, and _control_. It involves a _project plan_.
      - project management / 4Ps / project / plan ::@:: activities & tasks, monitoring & reporting, organization, resources, risks, schedule, scope \(i.e. constraints and objectives; e.g. budget, time, etc.\)
- [software development process](../../../../general/software%20development%20process.md) ::@:: It prescribes a process for developing software. It typically divides an overall effort into smaller steps or sub-processes that are intended to ensure high-quality results. The process may describe specific deliverables – artifacts to be created and completed. <p> \(__this course__: It is a process _template_ that is _adaptable_ for different application domains. It aids in _dividing_ work.\)
- project management
  - project management / scope ::@:: The _first_ task when planning a project: understand scope, i.e. constraints and objectives. <p> 1. define problem \(e.g. design goals\) <br/> 2. analyze requirements \(e.g. estimate system size\) <br/> 3. make top-level diagrams \(i.e. estimate the system; e.g. class diagrams, use case diagrams\) <br/> 4. estimate effort and time \(i.e. prepare the rest of the project plan\)
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
    - project management / organization / good practices ::@:: experience, modularity, person in charge \(PIC\), etc.
      - project management / organization / good practices / experience ::@:: We should assign people with _experience relevant_ to their tasks.
      - project management / organization / good practices / modularity ::@:: Teams should be modular \(not too few or many people\) and have clear responsibilities, e.g. a team corresponds to one or more identified parts of the system \(divide and conquer\). This helps with having the _right level of communication_.
      - project management / organization / good practices / person in charge \(PIC\) ::@:: Identify a person in charge \(PIC\) for each part and the system as a whole, so you can talk to them when the relevant parts go wrong.
  - project management / activities & tasks ::@:: A _task_ is a _well-defined_ work assignment for a role. An _activity_ is a group of _related_ tasks.
    - project management / activities & tasks / principles ::@:: - agile-driven: details are _incrementally_ planned as the project progresses <br/> - plan-driven: details are planned at project _start_ <p> Which one to use highly depends on the project. Often, a combination is the best.
  - project management / schedule ::@:: deliverables \(outputs\), milestones \(_important_ management decision points\), resources assignment, time estimates, ordering \(dependency\)
    - project management / schedule / levels ::@:: \(high level, rigid\) <br/> - master: client, management <br/> - macro: day-to-day management; e.g. Gantt chart, burndown chart <br/> - micro: team management <br/> \(low level, flexible\)
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
    - software development process / iterative and incremental / properties ::@:: - incremental: Separate functions are implemented one-by-one. <br/> - iterative: A function is implemented and refined over time. <br/> - both: Possible with various degrees.
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
    - software development process / code and fix / characteristics ::@:: changing requirements \(due to undocumented requirements\), many changes, messy code structure, unsuitable for large systems
    - software development process / code and fix / disadvantages ::@:: fail to meet expectations, over budget, over schedule, uncontrollable, unpredictable
- [software prototyping](../../../../general/software%20prototyping.md) ::@:: It is the activity of creating prototypes of software applications, i.e., incomplete versions of the software program being developed.
  - software prototyping / steps ::@:: gather and refine requirements → design → prototype \(not the entire system\) → evaluate → EITHER refine prototype \(→ design\) OR engineer product \(which may or may not be the final product\)
  - software prototyping / comparison ::@:: Similar to code and fix, but there is slightly more discipline and incorporates user feedback.
  - software prototyping / characteristics ::@:: exploratory \(e.g. functionalities, user interfaces, etc.\), good for unknown or vague requirements
  - software prototyping / advantages ::@:: explore multiple different solutions, explore user requirements, incorporates user feedback
  - software prototyping / disadvantages ::@:: incomplete process \(engineering the final product may need a separate process\), invisible to management \(e.g. the number of prototypes needed\), missing or sparse docs
- [spiral model](../../../../general/spiral%20model.md) ::@:: It is a risk-driven software development process model. Based on the unique risk patterns of a given project, the spiral model guides a team to adopt elements of one or more process models, such as incremental, waterfall, or evolutionary prototyping.
  - spiral model / steps ::@:: plan → risk analysis → \(EITHER go OR no go\) → engineer → evaluate → \(repeat until we have a complete system\)
  - spiral model / the spiral ::@:: The 4 quadrants of a 2D plane are respectively the 4 steps \(clockwise from the _x_-axis between quadrant II and III\), and the process is represented by arrowheads spiraling outwards.
  - spiral model / advantages ::@:: incorporates risk evaluation, incorporates user feedback to better meet expectations \(from evaluate and plan\), iterative and incremental
  - spiral model / disadvantages ::@:: expertise on risk evaluation required, for internal development rather than contract development as you know all the requirements, phases are not elaborated \(a separate process may be used\)
- [software release life cycle](../../../../general/software%20release%20life%20cycle)
  - software release life cycle / name ::@:: \(__this course__: use _phased release_\)
  - software release life cycle / motivation ::@:: Since change is inevitable \(by user requirements\), so produce releases over time and make changes accordingly.
  - software release life cycle / flow ::@:: Developers release multiple _development releases_ over time. _Concurrently_, users make _use/production releases_ out of each development release.
  - software release life cycle / incremental and iterative ::@:: Releases can be incremental or iterative or both. Often both are used in practice. <p> - incremental: Separate functions of a system are implemented one-by-one \(partial system\). If used alone, each function is fully implemented at once \(full functionality\). <br/> - iterative: Functions are implemented and refined over time \(partial functionality\). If used alone, all functions begin implementation at once \(full system\).
  - software release life cycle / advantages ::@:: apply appropriate expertise, early training, early user feedback, frequent releases, promote modularity, reduce risk
  - software release life cycle / disadvantages ::@:: common facilities for all functions are hard to identify, each function \(part\) needs to be small
- [agile software development](../../../../general/agile%20software%20development.md) ::@:: It is an umbrella term for approaches to developing software that reflect the values and principles agreed upon by _The Agile Alliance_, a group of 17 software practitioners, in 2001.
  - agile software development / principles ::@:: - emphasized: client involvement, individuals and interactions, responsive to change, working software <br/> - deemphasized \(but not completely ignored\): comprehensive docs, contract negotiation, plan following, processes and tools
  - agile software development / methods ::@:: continuous integration \(CI\), extreme programming \(XP\), scrum, etc.
  - agile software development / practices ::@:: - pair programming: implement a feature with another person checking to reduce mistakes <br/> - planning poker: estimate implementation time <br/> - test-driven development \(TDD\): think of tests before implementing <br/> - etc.
- [extreme programming](../../../../general/extreme%20programming.md) \(XP\) ::@:: It is a software development methodology intended to improve software quality and responsiveness to changing customer requirements. As a type of agile software development, it advocates frequent releases in short development cycles, intended to improve productivity and introduce checkpoints at which new customer requirements can be adopted.
  - extreme programming / steps ::@:: gather and analyze requirements → implement → \(repeat _quickly_\)
  - extreme programming / gather and analyze requirements ::@:: The developer determines features needed and estimate cost and time. Then the client selects features for each _iteration_.
  - extreme programming / implement ::@:: Each _iteration_ has many tasks. The developer implement features using _pair programming_ and design test cases using _TDD_.
- [continuous integration](../../../../general/continuous%20integration.md) \(CI\) ::@:: It is the practice of integrating source code changes frequently and ensuring that the integrated codebase is in a workable state.
  - continuous integration / mechanism ::@:: Typically, developers merge changes to an integration branch, and an automated system \(__this course__: CI server\) builds and tests the software system. Often, the automated process runs on each commit or runs on a schedule such as once a day. <p> \(__this course__: Work is submitted daily and/or as soon as possible to the main repository. Whenever that happens, CI servers run build and test scripts, and notify if there are failures.\)
  - continuous integration / advantages ::@:: automate build and test, catch build-breaking bugs early, check progress, integrate and test early, reduce integration conflicts
- [scrum](../../../../general/scrum.md) ::@:: It is an agile team collaboration framework commonly used in software development and other industries.
  - scrum / overview ::@:: It specifies what to do to develop a software product. But the detailed specifics \(how to do\) are decided by teams. <p> Requirements are items in a _product backlog_. The _product owner_ \(the client\) sets _priorities_. Then, the software is developed in _sprints_. Teams _self-organize_ to determine the best way to deliver the product.
  - scrum / sprint ::@:: Scrum prescribes for teams to break work into goals to be completed within time-boxed iterations, called _sprints_. Each sprint is no longer than one month and commonly lasts two weeks. <p> The scrum team assesses progress in time-boxed, stand-up meetings of up to 15 minutes, called _daily scrums_. <p> At the end of the sprint, the team holds two further meetings: one sprint review to demonstrate the work for stakeholders and solicit feedback, and one internal sprint retrospective.
    - scrum / sprint / activities ::@:: In a sprint, the software is designed, implemented, and tested. The requirements are not allowed to change.
  - scrum / release ::@:: A release should have 4 to 12 sprints. The shorter the release cycle, the shorter the duration of each sprint. <p> It may be associated with a _release backlog_.
  - scrum / framework ::@:: artifacts, meetings, roles
  - scrum / roles ::@:: product owner, scrum master, team
  - scrum / meetings ::@:: sprint planning → daily scrum meeting → sprint review \(external-oriented\), sprint retrospective \(internal-oriented\)
  - scrum / artifacts ::@:: - burndown charts, product backlog, sprint backlog <br/> - additional: defect backlog, release backlog
  - scrum / roles
    - scrum / roles / product owner ::@:: The key stakeholder represents the client or end users. It defines and prioritize requirements, and adjusts both every iteration. It decides on content and timing. It accepts or rejects results.
    - scrum / roles / scrum master ::@:: enable close cooperation, enact scrum values and practices, ensure functional and productive teams, remove progress obstacles, shield external interferences
    - scrum / roles / team ::@:: Apart from the scrum master, the other roles are similar to those in other development processes, e.g. developers, testers, etc.
  - scrum / meetings
    - scrum / meetings / sprint planning ::@:: Considers business conditions, current product, product backlog, team capacity, technology, etc. Prioritize product backlog to select _sprint goal_. Then, plan to achieve the sprint goal, and create a _sprint backlog_ from product backlog and estimate time \(ideally by subject matter experts\).
    - scrum / meetings / daily scrum meeting ::@:: They are stand-up \(no sitting down\) meetings up to 15 minutes. This is great for less experienced teams, but may hurt _morale_ in more experienced teams. They focus on review, plan, and obstacles.
      - scrum / meetings / daily scrum meeting / questions ::@:: - review: What did you do yesterday? <br/> - plan: What will you do today? <br/> - obstacles: Is anything in your way?
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
  - software development process / discipline ::@:: - spiral: The 4 phases must be followed in a spiral without backtracking. <br/> - waterfall: SDLC is followed sequentially without possibility of backtracking.
  - software development process / separation of concerns ::@:: - phased release: Development and release is separate. <br/> - spiral: Planning, risk analysis, engineering, and evaluation are separate. <br/> - waterfall: Each phase of SDLC is separate.
  - software development process / abstraction or generality ::@:: - spiral: Allows using other processes for the actual development and testing. <br/> - waterfall: As a direct implementation of the general SDLC.
  - software development process / adaptable to changes ::@:: - agile: By its nature. <br/> - phased release: Releases happen over time. <br/> - spiral: Planning happens periodically.
  - software development process / incremental ::@:: - agile: Many sprints are needed. <br/> - phased release: Many releases are needed. <br/> - prototyping: Many prototypes are needed. <br/> - spiral: Many spirals are needed.
  - software development process / risk assessment ::@:: - spiral: The only process to explicitly integrate risk analysis.
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
  - unified process / features ::@:: - defines activities: workflows to transform user requirements to a system <br/> - defines models: abstract or concrete entities that are transformed by workflows; e.g. artifacts <br/> - generic: a generic process _framework_ needing to be _specialized_ to use
- software development process
  - software development process / considerations ::@:: people \(e.g. expertise, skills\), project \(e.g. novelty, size, vagueness\), organization \(e.g. accessibility, formality, size\)
- unified process
  - unified process / advantages ::@:: It incorporates _best practices_ from all the previous software development processes and provides a _generic framework_.
- quiz: [quiz 5](questions/quiz%205.md)
- [questions § week 3 pre-lecture](questions/index.md#week%203%20pre-lecture)

## week 3 lecture

- datetime: 2025-09-17T12:30:00+08:00/2025-09-17T14:20:00+08:00, PT1H50M
- topic: modeling; unified modeling language; class diagram; association; aggregation; association class; generalization; UML summary
- [UML](UML.md)
  - [§ common mistakes: modeling out-of-scope entities](UML.md#common%20mistakes%20modeling%20out-of-scope%20entities)
  - [§ common mistakes: not using notes](UML.md#common%20mistakes%20not%20using%20notes)
  - [§ common mistakes: multiple links between the same pair of objects](UML.md#common%20mistakes%20multiple%20links%20between%20the%20same%20pair%20of%20objects)
  - [§ common mistakes: generalization and multiplicity](UML.md#common%20mistakes%20generalization%20and%20multiplicity)
  - [§ common mistakes: missing generalization coverage](UML.md#common%20mistakes%20missing%20generalization%20coverage)
  - [§ common mistakes: missing association constraints](UML.md#common%20mistakes%20missing%20association%20constraints)
  - [§ common mistakes: not using specialized associations](UML.md#common%20mistakes%20not%20using%20specialized%20associations)
- [§ week 2 pre-lecture](#week%202%20pre-lecture)
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
      - COMP 3111H / lab 2 / access modifier / class-level visibility ::@:: When you declare a class at the top level \(outside any other class\), Java allows only two modifiers: <p> - `public`: the class can be referenced from any package; it must reside in a file whose name matches the class name. <br/> - _default_ \(no modifier\): the class is __package-private__ – it can be used only by classes that live in the same package.
      - COMP 3111H / lab 2 / access modifier / member-level visibility ::@:: They apply to attributes, methods, and constructors in a class. <p> - `public`: the member can be accessed from any other class in any package. <br/> - `protected`: visible within its own package and by subclasses even if they are in different packages. <br/> - `private`: accessible only inside the class that declares it. <br/> - _default_ \(no modifier\): visible to all classes in the same package, but invisible outside of it.
    - COMP 3111H / lab 2 / `final` keyword ::@:: It can be applied to a variable \(e.g. attributes, local variables, etc.\): once assigned it becomes read-only; this is useful for constants \(e.g. `public static final int MAX_SIZE = 10;`\) or configuration values that must not change after initialization. It can still have any visibility modifier.
    - COMP 3111H / lab 2 / printing arrays ::@:: Learn to use `java.util.Arrays.toString()` to display array contents easily. Compare this with manual printing \(e.g., looping over elements\) to see the convenience of the utility method.
    - COMP 3111H / lab 2 / inheritance ::@:: It lets one class \(the subclass/child\) inherit fields and methods from another \(the superclass/parent\). <p> In Java, use the `extends` keyword for classes inheriting other classes or interfaces inheriting other interfaces. Use the `implements` keyword for classes inheriting interfaces. Interfaces cannot inherit classes. <p> A class can extend at most one other class. Both classes and interfaces can extend multiple other interfaces.
    - COMP 3111H / lab 2 / `@Override` annotation ::@:: It tells the compiler you intend to override a base-class method; it helps catch mistakes that make the method not actually overriding any base-class method, e.g. forget to inherit, wrong method signature, etc.
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
    - requirements elicitation / importance / failures ::@:: Major causes of software development failures or problems: <p> - changing requirements <br/> - incomplete requirements <br/> - unneeded system <br/> - unrealistic expectations <br/> - user involvement lacking <br/> - etc.
    - requirements elicitation / importance / cost ::@:: Whenever there is a defect, the later we discover it, the higher the cost it takes to fix it \(usually grows exponentially\). This is the cheapest when we are specifying the requirements, being the first step.
  - requirements elicitation / difficulty ::@:: It requires the collaboration of stakeholders with different background, resulting in _knowledge gap_. We need to bridge this gap, which is difficult.
    - requirements elicitation / difficulty / solution ::@:: Developers need to learn about the _application domain_ and its requirements. They need to transform said _vague_ requirements to _precise_ specifications. They also need to _represent_ the specifications that can be understood by clients. <p> They may even need to give _feedback_ on the requirements given by the clients and ask them to _revise_ \(i.e. "_educate_" the clients\), e.g. unrealistic requirements, etc.
  - requirements elicitation / activities ::@:: understand application domain and user needs, determine risks, capture system requirements, validate system requirements
    - requirements / elicitation / activities / understand ::@:: collect system _requirements_ and _constraints_, and determine _development scope_ and _design goals_ \(for reducing design _complexity_\)
    - requirements / elicitation / activities / risks ::@:: economic, legal, operational, organizational, technical, etc.
    - requirements / elicitation / activities / capture ::@:: - data requirements → _domain model_ <br/> - functional requirements → _use-case model_ <br/> - nonfunctional requirements → _supplementary text_
    - requirements / elicitation / activities / validate ::@:: verify _correctness_ and _completeness_ \(all important requirements\) of system requirements; use a checklist of questions to examine each requirement
- [software requirements specification](../../../../general/software%20requirements%20specification.md) \(SRS\) ::@:: It is a description of a software system to be developed. It is modeled after the business requirements specification \(CONOPS\). It lays out functional and non-functional requirements, and it may include a set of use cases that describe user interactions that the software must provide to the user for perfect interaction.
  - software requirements specification / name ::@:: \(__this course__: use _system requirements specification_\)
  - software requirements specification / elements ::@:: definition of user requirements, specification of system requirements
  - software requirements specification / not ::@:: Like requirements \(which it contains\), it states _what_ the system does, but not _how_ the system does. It is not a _design document_.
  - software requirements specification / agile software development ::@:: They argue producing such a thing is a waste of time when requirements change quickly. However, even they are using some aspects, albeit reduced, of SRS, e.g. product backlog, etc.
  - software requirements specification / languages :: - design description language: most restricted, like programming languages <br/> - graphical notations: + text annotations <br/> - mathematical specifications <br/> - natural language: + diagrams, tables, etc. <br/> - structured natural language: restricted, follows fixed template
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
- [§ week 4 pre-lecture](#week%204%20pre-lecture)
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
- topic: JavaFX; scene builder
- COMP 3111H
  - COMP 3111H / lab 3 ::@:: Lab 3 focuses on creating JavaFX UIs using Scene Builder and integrating them into an IntelliJ Maven project.
    - COMP 3111H / lab 3 / objectives ::@:: Build a simple UI, link it to Java code, use JDK 21, IntelliJ 2022+, and Scene Builder 19+.
    - COMP 3111H / lab 3 / tools ::@:: Install _Java SE Development Kit_ 21 for the compiler and runtime. Use _IntelliJ IDEA_ version 2022 or newer as the IDE. Download and install _Scene Builder_ 19+ (recommended 22.0.0 for Java 17+).
    - COMP 3111H / lab 3 / JavaFX ::@:: A framework built on Java that supplies libraries for building graphical user interfaces (GUIs). It provides standard controls—buttons, menus, text fields—and supports custom components.
    - COMP 3111H / lab 3 / scene builder ::@:: Visual design tool where you drag and drop _JavaFX_ UI elements onto a canvas. It generates an _.fxml_ file that describes the layout in XML; JavaFX reads this at runtime to construct the interface. <p> Many apps encode GUIs in markup (XML, HTML); writing them by hand can be error-prone and tedious. Scene Builder visualises the structure, making it easier to understand and modify complex layouts quickly.
      - COMP 3111H / lab 3 / scene builder / drag-and-drop ::@:: Select a component from the library panel. Drag it onto the design surface; drop where you want it positioned. The tool automatically creates the corresponding XML tags in the _.fxml_ file.
    - COMP 3111H / lab 3 / linking Java and JavaFX ::@:: Design your UI in Scene Builder and export the _.fxml_ file to `src/main/resources`. <p> In the controller class (e.g., _HelloController_), annotate fields and methods mentioned by the _.fxml_ file with `@FXML` and implement event handlers. Link the controller in the FXML header: `fx:controller="your.package.HelloController"`.
    - COMP 3111H / lab 3 / running ::@:: Use IntelliJ's "Run" configuration for a JavaFX Application. Verify that clicking the button invokes the controller method and updates the UI as expected. If problems occur, check the console output for stack traces and confirm that the `fx:controller` path matches the package of your controller class.
<!-- - assignment: [lab 3](assignments/lab%203/index.md) -->

## week 5 pre-lecture

- topic: use case specification; basic flow; extension point; alternative flow; subflow; non-functional requirement; validation
- requirements elicitation
- UML
  - [§ use case specification](UML.md#use%20case%20specification)
  - [§ use case preconditions](UML.md#use%20case%20preconditions)
  - [§ use case postconditions](UML.md#use%20case%20postconditions)
  - [§ use case flow of events](UML.md#use%20case%20flow%20of%20events)
  - [§ use case extension points](UML.md#use%20case%20extension%20points)
  - [§ use case alternative flows](UML.md#use%20case%20alternative%20flows)
  - [§ use case subflows](UML.md#use%20case%20subflows)
  - [§ use case detail level](UML.md#use%20case%20detal%20level)
- quiz: [quiz 8](questions/quiz%208.md)
- [non-functional requirement](../../../../general/non-functional%20requirement.md) ::@:: It is a requirement that specifies criteria that can be used to judge the operation of a system, rather than specific behaviours. They are contrasted with functional requirements that define specific behavior or functions. <p> It places _constraints_ on use cases or the system.
  - non-functional requirement / discovery ::@:: A key challenge highlighted was that non-functional requirements often remain implicit until they surface during validation. <p> To mitigate this, read each requirement statement line-by-line, identify the hidden constraint, and classify it into one of the NFR categories.
  - non-functional requirement / categories ::@:: design quality, documentation, hardware, implementation, interface \(user, system\), management, performance, physical environment, security
    - non-functional requirement / categories / design quality ::@:: reliability, supportability, maintainability; e.g., "No software faults should require a user reset."
    - non-functional requirement / categories / documentation ::@:: who the docs are for and what they contain; e.g., "User manuals must be written in plain English."
    - non-functional requirement / categories / hardware ::@:: platform constraints, e.g. implementation platform, memory size, storage size, etc.
    - non-functional requirement / categories / implementation ::@:: language choices, error handling standards, etc.
    - non-functional requirement / categories / interface ::@:: UI learnability/usability and external system formats/timing; e.g., "Any user who knows how to read a digital watch and understand international time should be able to use our watch."
    - non-functional requirement / categories / management ::@:: backup, installation, maintenance procedures
    - non-functional requirement / categories / performance ::@:: speed, throughput, response time, accuracy; e.g., "Display must update within 5 min after GPS blackout."
    - non-functional requirement / categories / physical environment ::@:: abnormal conditions, distributed operations, etc.
    - non-functional requirement / categories / security ::@:: access control, data access, physical access, system access, etc.
  - non-functional requirement / specification ::@:: Record them either as supplementary constraints on top of use cases or as system-wide constraints. <p> _Operational_ NFRs can be attached to _administration_ use cases (e.g., "Login" for security) or expressed at the system level when they affect overall architecture. Administration use cases address operational concerns such as system start-up, shutdown, backup, and security policies.
- [software verification and validation](../../../../general/software%20verification%20and%20validation.md) ::@:: It is the process of checking that a software system meets specifications and requirements so that it fulfills its intended purpose. It may also be referred to as software quality control. It is normally the responsibility of software testers as part of the software development lifecycle.
  - software verification and validation / simple definition ::@:: In simple terms, software verification is: "Assuming we should build X, does our software achieve its goals without any bugs or gaps?" On the other hand, software validation is: "Was X what we should have built? Does X meet the high-level requirements?"
  - software verification and validation / characteristics ::@:: completeness, consistency, clarity, correctness, realism
    - software verification and validation / characteristics / completeness ::@:: every feature and exception must be described; the SRS should cover all stakeholder interests <p> example: Missing boundary behaviour near GPS accuracy limits → add a rule that zone changes only after five minutes.
    - software verification and validation / characteristics / consistency ::@:: no internal contradictions; requirements must align logically with each other <p> example: Contradictory upgrade requirements → revise one to resolve conflict.
    - software verification and validation / characteristics / clarity ::@:: unambiguous language that yields a single interpretation for any reader <p> example: Ambiguity about daylight-saving handling → explicitly state the policy in the spec, e.g. explicitly requiring DST support.
    - software verification and validation / characteristics / correctness ::@:: faithfully reflects what the client actually wants <p> Claim of only 24 time zones when half-hour offsets exist → broaden requirement to cover all legal zones.
    - software verification and validation / characteristics / realism ::@:: feasible within time, cost, and technical constraints
  - software verification and validation / methods ::@:: Acceptance tests are the primary means to validate a system _implementation_ satisfies the requirements. They are prescribed later in the _testing_ phase. <p> They are conducted with clients or end users, who confirm that implemented features satisfy the written requirements.
- requirements elicitation
  - requirements elicitation / workflow ::@:: 1. Capture data requirements → domain model / class diagram. <br/> 2. Capture functional requirements → use case model, diagram and specifications. <br/> 3. Capture non-functional constraints as described above. <br/> 4. Validate the entire SRS against completeness, consistency, clarity, correctness, and realism. <br/> 5. Refine through iterative cycles: add test cases, produce analysis and design models, then implement.
- UML
  - [§ domain models](UML.md#domain%20models) ::@:: Use class diagrams to depict entities, attributes, and associations; this informs data persistence and object interactions.
  - [§ use case models](UML.md#use%20case%20models) ::@:: The use-case diagram lists actors and system functions; each use case is further detailed by a flow of events that sequences actions and decision points.
- software verification and validation
- software requirements specification
  - software requirements specification / iteration ::@:: The SRS is a living artifact that evolves with stakeholder feedback, forming the foundation for all later phases (analysis, design, implementation). <p> Early iterations produce high-level _domain_, _use-case_ models, and _nonfunctional_ requirements; subsequent passes add detail, test cases to the _test model_, matching use case realizations to the _analysis model_ and _design model_. <p> We can see use cases _drive_ subsequent development.
- quiz: [quiz 9](questions/quiz%209.md)
- [questions § week 5 pre-lecture](questions/index.md#week%205%20pre-lecture)

## week 5 lecture

- datetime: 2025-10-01T12:30:00+08:00/2025-10-01T14:20:00+08:00, PT1H50M
- status: unscheduled; public holiday: National Day
- [§ week 5 pre-lecture](#week%205%20pre-lecture)
- [questions § week 5 lecture](questions/index.md#week%205%20lecture)

---

> Dear Comp3111/H Students,
>
> To synchronize the progress of L1 and L2, we will not have lecture for both L1 and L2 this week. But please make sure to complete all the necessary quizzes online before the deadlines : \)
>
> Regards,
>
> \[redacted\]

## week 5 lab

- datetime: 2025-10-02T18:00:00+08:00/2025-10-02T19:50:00+08:00, PT1H50M
- topic: UML modeling; draw.io; project demonstration
- COMP 3111H
  - COMP 3111H / lab 4 ::@:: UML data modeling (class & use-case diagrams)
    - COMP 3111H / lab 4 / objectives ::@:: - Gain hands-on experience drawing _UML Class Diagrams_ and _Use-Case Diagrams_. <br/> - Learn to model relationships, cardinalities, inheritance, and associations accurately. <br/> - Practice using an online diagramming tool (draw.io) integrated with Google Drive for collaborative work.
    - COMP 3111H / lab 4 / draw.io ::@:: Web-based application that supports flowcharts, ER diagrams, UML diagrams, etc. Fully integrated with Google Workspace; diagrams can be auto-saved to a Google Drive folder or Gmail account. Offers editing options for color, line type, and connector points directly on each shape.
    - COMP 3111H / lab 4 / multiple generalization ::@:: It is possible to model _multiple inheritance_. For example, in a UNO game, the following cards may be modeled like below: <p> - `PlusTwoCard` ⟶ `SkipCard` <br/> - `PlusFourWildCard` ⟶ `SkipCard` and `WildCard`.
  - COMP 3111H / project
    - COMP 3111H / project / demonstration
<!-- - assignment: [lab 4](assignments/lab%204/index.md) -->

---

> Dear Students,
>
> Please note the lab 4 schedule change:
>
> Old schedule:
> Lab 4           Week \# 6
>
> New schedule:
> Lab 4               Week \# 5 \(2nd October and 3rd October\)
>
> The schedule is updated on Canvas as well.
>
> Reminder: In lab 4 I will present the project demo, and discuss the project requirements \(available on Canvas as well\). Furthermore, if you got any questions regarding project requirements you can feel free to email me or attend the lab 4 session.
>
> Thanks.
>
> Regards,
> COMP3111 Teaching Team

## week 6 pre-lecture

- topic: implementation; defensive programming; code review; refactoring; debugging; configuration management
- [implementation](../../../../general/implementation.md) ::@:: It is the realization of an application, execution of a plan, idea, model, design, specification, standard, algorithm, policy, or the administration or management of a process or objective.
- systems development life cycle
  - systems development life cycle / implementation ::@:: It occurs after design, before testing – the "Construction" phase of the engineering workflow. <p> It Involves turning design artifacts into executable _modules_ (classes, binaries, scripts) and _subsystems_. It requires a clear integration plan and disciplined version-control usage.
- implementation
  - implementation / module ::@:: It is a replaceable component that implements specific interfaces, e.g. auth module, user module.
  - implementation / subsystem ::@:: They group related modules for manageability, e.g. login subsystem = auth module + user module.
  - implementation / examples ::@:: source files (`.java`/`.cs`), compiled binaries (DLL/EXE), shell scripts, configuration bundles, etc.
- modular programming
- implementation
  - implementation / activities ::@:: generation → modularization → packaging → deployment
    - implementation / activities / generation ::@:: Generate source code for each class using suitable algorithms and data structures.
    - implementation / activities / modularization ::@:: Assign classes to language-specific modules; this decision is often guided by encapsulation rules and package boundaries.
    - implementation / activities / packaging ::@:: Compile and link modules into a coherent _executable module_, requiring _version control_ to track changes across builds, and also _integration plan_.
    - implementation / activities / deployment ::@:: Deploy the final binaries onto target nodes or runtime environments.
- [defensive programming](../../../../general/defensive%20programming.md) ::@:: It is a form of defensive design intended to develop programs that are capable of detecting potential security abnormalities and make predetermined responses. It ensures the continuing function of a piece of software under unforeseen circumstances.
  - defensive programming / simple definition ::@:: Protect yourself at all times! Never trust anyone! <p> Check all data from external sources. Check all input parameters. Handle bad inputs.
  - defensive programming / scenarios ::@:: Defensive programming practices are often used where high availability, safety, or security is needed.
  - defensive programming / techniques ::@:: assertion, code refactoring, code review, validation, etc.
  - defensive programming / validation ::@:: Separate code into two layers: _validation classes_ that cleanse input, and _internal classes_ that assume clean data. <p> Example: a student registration system checks IDs and emails before storing them.
    - defensive programming / validation / validation ::@:: Validation converts raw user input (GUI, CLI, files, streams) to the proper types before any business logic runs. These are like "barricade" classes.
    - defensive programming / validation / internal ::@:: Internal code can be written faster because it does not need to re-check every assumption.
- [assertion](../../../../general/assertion%20(software%20development).md) ::@:: In computer programming, specifically when using the imperative programming paradigm, an assertion is a predicate (a Boolean-valued function over the state space, usually expressed as a logical proposition using the variables of a program) connected to a point in the program, that always should evaluate to true at that point in code execution.
  - assertion / uses ::@:: Assertions can help a programmer read the code, help a compiler compile it, or help the program detect its own defects.
  - assertion / conditions ::@:: Precondition assertions check inputs before a routine executes; postcondition assertions verify outputs after execution.
  - assertion / reasoning ::@:: Forward reasoning (pre → post; what will happen) is intuitive but may introduce irrelevant facts that increase in number hopelessly; backward reasoning (post → pre; what should happen) guides test case creation and bug reproduction.
    - assertion / reasoning / forward ::@:: Simulate the program's execution step-by-step starting from a known _precondition_ to predict the resulting _postcondition_. <p> _Example:_ Given `x` is even, after executing `x = x + 3; y = 2 * x;`, forward reasoning tells us `y = 2*(x+3)` and that `y` will be even (since adding 3 to an even number yields odd, then doubling makes it even again).
    - assertion / reasoning / backward ::@:: Work backwards from a desired _postcondition_ to deduce the necessary _preconditions_ that must hold before execution. It may also be used to _deduce_ the required inputs to achieve a _goal_ or reproduce a _bug_. <p> _Example:_ To guarantee after running `x = x + 3; y = 2 * x;` that `y > x`, backward reasoning solves `2*(x+3) > x` → `x > -6`. Thus, the precondition needed is "`x` is an integer larger than `-6`."
  - assertion / uses
    - assertion / uses / typical ::@:: verifying array bounds, non-null pointers, expected file states, invariant maintenance across method calls, etc.
  - assertion / documentation ::@:: Document and verify contract conditions—use them to express both _what should happen_ and _what must never happen_.
  - assertion / vs. error handling ::@:: Reserve error-handling mechanisms for recoverable faults; assertions are for impossible or programmer errors that should crash the program.
  - assertion / side effects ::@:: Avoid embedding side effects in assertions because some runtimes may strip them out in release builds.
  - assertion / examples ::@:: The assertion guards against division-by-zero errors during debugging but can be removed in release builds without affecting performance. <p> Example in C\#: <p> `// Precondition: denominator != 0` <br/> `Debug.Assert(denominator != 0, "Denominator is unexpectedly equal to 0.");` <br/> `double result = numerator / denominator;`
- [code review](../../../../general/code%20review.md) ::@:: It is a software quality assurance activity in which one or more people examine the source code of a computer program, either after implementation or during the development process. <p> It is kinda like an _offline_ version of _pair programming_.
  - code review / uses ::@:: Peer reviews catch bugs early, expose design flaws \(articulate decisions\), and enforce coding standards before integration. Juniors can also learn without hurting code quality. <p> While it holds both authors and reviewers _accountable_, it is _not_ for assessing performance. Reviewers should find faults in code (but not in people). Reviewers should be voluntary.
  - code review / artifacts ::@:: coherent module \(sometimes called "inspection"\), completed code \("incremental review"\), design document, spec, etc.
  - code review / participants ::@:: It should involve at least one other developer not writing the code. It can be a group of developers.
  - code review / format ::@:: The review process can be formal (in-person meeting) or informal (email/instant chat). Best to prepare by distributing the artifacts in advance. Often discovery happens during preparation instead of meeting.
  - code review / goals ::@:: verifying specifications, inspecting coherent modules, ensuring incremental code quality, etc.
  - code review / focuses ::@:: coding standards \(automated tools can be better\), common problem types, error-prone code, security
  - code review / techniques ::@:: - walkthroughs where the author presents the artifact <br/> - defect discovery only or fix brainstorming <br/> - targeted checks for known defect patterns <br/> - use of checklists (e.g., "Are all public methods documented?").
  - code review / vs. testing ::@:: Reviews or inspections can be considered as part of testing, as they both detect faults to improve quality.
- [code refactoring](../../../../general/code%20refactoring.md) ::@:: In computer programming and software design, it is the process of restructuring existing source code—changing the _factoring_—without changing its external behavior.
  - code refactoring / uses ::@:: Refactoring is intended to improve the design, structure, and/or implementation of the software (its non-functional attributes), while preserving its functionality.
  - code refactoring / motivation ::@:: Good code should be _executable_, _maintainable_ \(allow change\), and _clear_ \(communicate well to readers\). <p> Unchecked growth turns code into "code rot".
  - code refactoring / low-level ::@:: It targets code readability: renaming variables/methods, extracting constants, moving duplicated logic into helper methods, inlining small routines, or reordering statements for cohesion.
  - code refactoring / high-level ::@:: It aims at architectural improvement: replacing unsafe idioms with safer constructs, clarifying ambiguous logic, optimizing performance hotspots, and applying design patterns where appropriate. <p> They are often not well-supported by tools but are much more _important_.
  - code refactoring / IDE support ::@:: IDE support \(e.g. Eclipse, IntelliJ IDEA, Visual Studio\) offers automated renaming, extraction, inlining, and signature changes; however, high-level refactoring, while more important, still requires manual judgment.
  - code refactoring / examples ::@:: For example, refactoring a "_god_ class" into several classes by looking for "_natural_ homes" for each functionality: <p> 1. Identify clusters of related attributes and operations (e.g., `AddItem`, `CheckOutItem`). <br/> 2. Move these groups into cohesive classes (e.g., `Catalog`, `Person`) to reduce cross-cutting concerns. <br/> 3. Replace transient associations with explicit attribute and method arguments, thereby clarifying data ownership and lifecycle.
  - code refactoring / refactoring plan ::@:: Assuming you have enough time: <p> 1. First, write unit tests that capture the current external behavior of the existing system. <br/> 2. Refactor the code base to remove obvious smells (duplicate logic, magic numbers) while preserving functionality. <br/> 3. Finally, add the new feature incrementally, verifying against the established test suite.
  - code refactoring / timing ::@:: Ideally performed continuously during development—like how unit tests are written—to maintain a clean codebase that supports rapid feature addition.
    - code refactoring / timing / late vs. early ::@:: Late-project refactoring is risky because it can introduce regressions and delays delivery; early investment pays off with higher developer morale and lower maintenance costs (ROI estimates up to 500%).
  - code refactoring / effort ::@:: Although refactoring incurs _upfront_ effort, it pays dividends in reduced defect rates, easier feature integration, and higher team productivity. The _overall_ effort becomes lower.
  - code refactoring / culture ::@:: Adopt a culture of continuous improvement: write tests first, refactor as you go, and review code regularly to keep the system maintainable.
- quiz: [quiz 10](questions/quiz%2010.md)
- defensive programming
  - defensive programming / principles ::@:: avoiding bugs before they are written, failing fast to make bugs observable, making bugs impossible by design; debugging is _last resort_
  - defensive programming / making bugs impossible ::@:: discipline, language guarantees, self-imposed restrictions, well-tested protocols or libraries
    - defensive programming / making bugs impossible / language guarantees ::@:: Treat the language as a safety net: Java, for instance, prevents memory-overwrite bugs by using managed arrays and bounds checks.
    - defensive programming / making bugs impossible / well-tested protocols or libraries ::@:: Rely on well-tested protocols or libraries to guarantee correctness—TCP/IP guarantees packet order; Java `BigInteger` throws on overflow instead of silently wrapping.
    - defensive programming / making bugs impossible / self-imposed restrictions ::@:: Adopt self-imposed conventions that eliminate whole classes of defects, e.g.: <p> - hierarchical locking eliminates deadlocks <br/> - banning recursion removes infinite-recursion stack overflows <br/> - immutable collections guarantee behavioral equality across threads
    - defensive programming / making bugs impossible / discipline ::@:: Discipline is essential; once you "make it impossible", you must keep the rules in force—forgetting a lock order can re-introduce a deadlock you thought was gone.
  - defensive programming / avoiding bugs ::@:: simple and modular, think before code
    - defensive programming / avoiding bugs / think before code ::@:: Think first: plan the data flow and error handling, then code. "If you're writing lots of trivial bugs, you're also probably creating hard-to-track ones."
    - defensive programming / avoiding bugs / don'ts ::@:: Don't rely on the compiler to catch everything—especially in concurrency or time-sensitive systems where race conditions can slip through. Don't rely on debugging, especially when deadlines are tight.
    - defensive programming / avoiding bugs / simple and modular ::@:: Keep code simple and modular with well-documented specs; a flat monolith is harder to reason about than a collection of well-encapsulated modules.
  - defensive programming / failing fast ::@:: Use assertions to capture invariants as soon as they are violated: `assert(i < a.length): "Value not found in a[]"` aborts the program right where the assumption fails. <p> Insert precondition checks and consistency checks early; if a check fails, halt execution rather than letting the error propagate.
  - defensive programming / bug observability ::@:: A loop to find  `k` that assumes `k` is present in an array \(`while(true)`\) will throw an out-of-bounds exception if the guarantee is broken—this makes the failure obvious. <p> Making the loop "safe" by adding `i < a.length` hides the root cause: you no longer know whether `k` was actually missing or whether another bug caused it. Adding an assertion \(`assert(i < a.length): "Value not found in a[]"`\) restores visibility and documents the invariant, turning silent failures into explicit errors.
- [debugging](../../../../general/debugging.md) ::@:: It is the process of finding the root cause, workarounds, and possible fixes for bugs.
  - debugging / "the first bug" ::@:: The first recorded "bug" was a moth stuck in a relay on the Harvard Mark 1 computer \(1947\); it shows how small hardware errors can cascade into system failures.
  - debugging / localization ::@:: binary-search debugging, modularity, etc.
    - debugging / localization / modularity ::@:: Modularity allows one to add or remove modules one-by-one and locate the module the bug appears in. It also helps with reasoning, as you can easily inspect intermediate values across interfaces between modules.
    - debugging / localization / binary-search debugging ::@:: Binary-search debugging helps isolate faults quickly: divide the code into halves, test each half, repeat until you find the offending segment.
  - debugging / techniques ::@:: common mistakes, exclusion, stale binaries
  - debugging / exclusion ::@:: Start by asking "where can't it be?"—e.g., a typo in an identifier will never affect runtime logic, but a swapped argument order will.
  - debugging / common mistakes ::@:: Look for common mistakes: reversed arguments (`Collection.copy(src, dest)`), `==` vs. `.equals()`, uninitialized variables, deep vs. shallow copy errors.
  - debugging / stale binaries ::@:: Always recompile and verify you are debugging the current source; stale binaries can mislead.
- assertion
  - assertion / production ::@:: The goal of placing assertions in production: to stop execution as close to the defect as possible; a debugger will stop at the check, and you can explore nearby only to locate the problem.
    - assertion / production / inclusion ::@:: Production inclusion depends on context: if a failure would corrupt data, abort immediately; if the error is benign, you might allow continued operation with a warning.
- [regression testing](../../../../general/regression%20testing.md) ::@:: It is re-running functional and non-functional tests to ensure that previously developed and tested software still performs as expected after a change. If not, that would be called a _regression_.
  - regression testing / workflow ::@:: After finding a bug \(but before fixing\), add a test that reproduces it \(with _triggering_ input and _correct_ output\), fix it, and run the full suite to verify the fix. Thereafter, rerunning the full suite guards against regressions. <p> This can generate _good tests_ and protect against _bug reintroduction_.
  - regression testing / benefits ::@:: Frequent regression testing cycles catch newly introduced bugs early and build confidence in the code base.
  - regression testing / automation ::@:: Regression suites can be automated to run after each build, catching side effects early in the development cycle.
  - regression testing / maintenance ::@:: Keep tests focused on _public behavior_. Keep them _concise_: remove redundant or obsolete tests to reduce noise and regression testing time. <p> Use version control tags or snapshots to compare regression results across releases. This helps identify subtle regressions.
- debugging
  - debugging / vs. testing ::@:: The latter reveals a problem exist. The former further pinpoints its location and cause.
  - debugging / occurrences ::@:: Typical industry defect rate ≈ 10 bugs per 1,000 lines; many surface only after integration or from real user reports.
  - debugging / steps ::@:: (1) clarify the symptom, (2) reproduce it deterministically and create a test case, (3) debug to find root cause and fix, (4) re-run all tests.
  - debugging / getting unstuck ::@:: When debugging fails, consider whether external assumptions have changed (OS updates, disk space), document the system anew, seek help from peers \(see your own blind spots\), or walk away \(prefer efficiency over latency\).
- [configuration management](../../../../general/configuration%20management.md) \(CM\) ::@:: It is a management process for establishing and maintaining consistency of a product's performance, functional, and physical attributes with its requirements, design, and operational information throughout its life.
  - configuration management / simple definition ::@:: It manages, controls, and monitor _changes_ to lifecycle _artifacts_, so that cost-effective or urgent changes are prioritized and changes are traceable.
  - configuration management / components ::@:: change management, version management, system building, release management
- [change management](../../../../general/change%20management%20(engineering).md) \(CM\) ::@:: It in systems engineering is the process of requesting, determining attainability, planning, implementing, and evaluating of changes to a system. Its main goals are to support the processing and traceability of changes to an interconnected set of factors.
  - change management / simple definition ::@:: It ensues system evolution is _managed_.
  - change management / configuration items ::@:: They are artifacts for which we want to control changes: datadata, documents, plans, procedures, programs, specifications, etc.
  - change management / activities ::@:: It supports many activities: audit, control, identify, report, support, etc.
  - change management / software library ::@:: To support change management, the library provides facilities to store, label, and identify versions, and tracks status of configuration items.
    - change management / software library / hierarchy ::@:: \(local\) <br/> - developer's workspace: everyday development; check-in/check-out configuration items to/from master directory <br/> - master directory: stores and tracks promotions for other developers; after software QA, they are uploaded to software repository <br/> - software repository: stores and tracks releases for users <br/> \(remote\)
- [change control](../../../../general/change%20control.md) ::@:: Within quality management systems (QMS) and information technology (IT) systems, it is a process—either formal or informal—used to ensure that changes to a product or system are introduced in a controlled and coordinated manner.
  - change control / baseline ::@:: It is a snapshot of the system; any modification must pass review before becoming part of the baseline. <p> \(__this course__: It may also refer to a time/phase after which any changes must be _formalized_ and _controlled_.\)
    - change control / baseline / addition ::@:: To add configuration items, it needs to pass a set of _formal_ review procedures, usually at a _milestone_. Then it becomes part of the software library and is checked-in to the master directory.
    - change control / baseline / modification ::@:: To modify configuration items, the configuration item to replace the old one needs to pass a set of _formal_ review procedures, similar to addition. _Version management_ is needed.
  - change control / simple definition ::@:: It is a \(__this course__: _formal_\) process to make changes to a project.
  - change control / workflow ::@:: request → evaluate → implement & quality assurance → promote & release
    - change control / workflow / request ::@:: user \(external request\) or developer \(internal request\) submits change request
    - change control / workflow / evaluate ::@:: authority assesses merit, cost, impact; may queue, approve, or deny
    - change control / workflow / implement & quality assurance ::@:: item is checked out, modified, then checked in after QA; this establishes a new _baseline_ for further QA and testing
    - change control / workflow / promote & release ::@:: approved changes are released to developers \(promotion\); and users \(release\) after auditing all changes again
  - change control / audits ::@:: They verify that each step of the change process was followed correctly; usually performed by a Quality Assurance team. <p> This is done by a QA group if there is one in the organization.
  - change control / status reports ::@:: They keep all stakeholders informed about who made which changes and why—critical for coordination, accountability, and governance.
- [version control](../../../../general/version%20control.md) ::@:: It is the software engineering practice of controlling, organizing, and tracking different versions in history of computer files; primarily source code text files, but generally any type of file.
  - version control / names ::@:: revision control, source control, source code management \(__this course__: use _version management_\)
  - version control / concepts ::@:: branch, codeline, variant, version, evolution graph, etc.
    - version control / concepts / codeline ::@:: It is a linear history of an item where every new revision directly supersedes its predecessor; think of it as the "main" trunk that evolves over time with each commit creating a newer version. <p> There is a separate codeline for each branch.
    - version control / concepts / version ::@:: It is a specific, immutable snapshot of a configuration item (e.g., `v2.1.4`); once created it never changes, and all modifications produce a distinct new version rather than overwriting the old one.
    - version control / concepts / branch ::@:: It is a diverging path off the main codeline that allows _parallel_  or experimentation; branches can be merged back later, enabling isolated feature work without disrupting the stable trunk.
    - version control / concepts / variant ::@:: It is a _co-existing_ configuration of an item tailored for different environments or use cases (e.g., Windows builds vs. Linux builds), each variant may follow its own codeline and versioning scheme while sharing common core code.
    - version control / concepts / evolution graph ::@:: It visualizes the history: nodes represent versions, edges indicate derivations or merges.
- implementation
  - implementation / summary ::@:: Implement classes (operations) in modules, then group modules into subsystems. Integrate all subsystems into a final system and assign executable modules to processing nodes (in distributed contexts).
  - implementation / quality ::@:: It depends on _continuous improvement_ via defensive programming, rigorous code review, refactoring practices, effective debugging, and robust configuration management.
- quiz: [quiz 11](questions/quiz%2011.md)
- [questions § week 6 pre-lecture](questions/index.md#week%206%20pre-lecture)

## week 6 lecture

- datetime: 2025-10-08T12:30:00+08:00/2025-10-08T14:20:00+08:00, PT1H50M
- topic: software development; project risks; project planning; software development process; agile; unified process; requirements capture; domain model; modeling classes; modeling associations; modeling attributes; use case model; actor; use case diagram
- [UML](UML.md)
  - [§ common mistakes](UML.md#common%20mistakes)
  - [§ common mistakes: use case scope](UML.md#common%20mistakes%20use%20case%20scope)
  - [§ common mistakes: misusing use case generalization](UML.md#common%20mistakes%20misusing%20use%20case%20generalization)
- [§ week 3 pre-lecture](#week%203%20pre-lecture)
- [§ week 4 pre-lecture](#week%204%20pre-lecture)
- [questions § week 6 lecture](questions/index.md#week%206%20lecture)

## week 6 lab

- datetime: 2025-10-09T18:00:00+08:00/2025-10-09T19:50:00+08:00, PT1H50M
- topic: Git; GitHub
- COMP 3111H
  - COMP 3111H / lab 5 ::@:: team development on GitHub
    - COMP 3111H / lab 5 / summary ::@:: The lab lets teams practice real-world collaboration using GitHub: create a team repo, clone it locally, experiment with branching, submit pull requests (PRs), and review code.
    - COMP 3111H / lab 5 / GitHub import ::@:: One designated person (ideally the leader) imports the project's GitHub repo as a new "Lab 5" repo to keep it separate from the main project.
    - COMP 3111H / lab 5 / clone ::@:: Every member clones the newly created team repo onto their machine: `git clone <repo-url>`. Alternatively, you may use command line or IntelliJ's VCS integration; consistency is key so that all branches are tracked correctly.
    - COMP 3111H / lab 5 / new branch ::@:: Create a new branch: `git checkout -b <feature-name>`. It automatically switches to it.
    - COMP 3111H / lab 5 / commit ::@:: Edit files, stage (`git add .`), and commit (`git commit -m "..."`).
    - COMP 3111H / lab 5 / push ::@:: Push the branch to GitHub: `git push --set-upstream origin <feature-name>`.
    - COMP 3111H / lab 5 / GitHub pull requests \(PRs\) ::@:: 1. On GitHub, click "New pull request" and choose your feature branch against `main`. <br/> 2. Fill in a descriptive title and optional checklist or template. <br/> 3. Add assignee\(s\) and reviewers (e.g., teammates, TA). <br/> 4. Submit the PR; the reviewer(s) will comment, approve, or request changes. <br/> 5. Once approved, merge into `main` (either via "Merge pull request" button or command line).
    - COMP 3111H / lab 5 / GitHub issues ::@:: Write an issue before starting a branch: "Issue \#1 – server-connection feature". Name the corresponding branch, e.g. `issue-1_server-connection`. Link PRs to issues; GitHub will auto-close the issue when the PR is merged.
    - COMP 3111H / lab 5 / GitHub projects ::@:: Use GitHub's Project board to track tasks, assign labels, and move cards through columns (e.g., "To Do → In Progress → Done"). This visual aid keeps everyone aware of ongoing work and deadlines.
    - COMP 3111H / lab 5 / GitHub templates ::@:: Create markdown templates in the `.github/ISSUE_TEMPLATE` and `.github/PULL_REQUEST_TEMPLATE` folders. Templates standardise information (e.g., steps to reproduce, test coverage) and reduce review overhead.
    - COMP 3111H / lab 5 / GitHub network ::@:: The "Network" view shows how branches diverge and merge, helping you spot conflicts or orphaned commits early.
    - COMP 3111H / lab 5 / GitHub wiki ::@:: Use the repository Wiki to maintain design docs, setup guides, or any shared knowledge that evolves during the course.
    - COMP 3111H / lab 5 / GitHub Actions ::@:: Configure actions in `.github/workflows/`, e.g. run tests on every PR (`push` and `pull_request`), auto-deploy a staging environment after merging into `main`, etc. Actions keep code quality high by catching bugs before they hit the main branch.
- assignment: [lab 5](assignments/lab%205/index.md)

## week 7 pre-lecture

- topic: testing; test design; basis path testing
- __Course objectives__
  - Grasp why testing is essential for software quality.
  - Identify three fundamental test case types (equivalence, boundary, random) and how to generate them.
  - Understand component-level vs system-level testing principles.
  - Learn practical strategies for designing unit, integration, and system tests.
- unified process
  - unified process / testing ::@:: Testing happens throughout the 4 phases of UP: inception → elaboration → construction → transition. <p> It is more emphasized during the middle two phases: elaboration and construction.
    - unified process / testing / inception ::@:: Set up initial test strategy; focus on early architecture validation.
    - unified process / testing / elaboration ::@:: Run executable architectural baseline tests to confirm core design choices.
    - unified process / testing / construction ::@:: Perform heavy _integration/system testing_ for each incremental build.
    - unified process / testing / transition ::@:: Emphasize _defect correction_ and _regression testing_; reuse existing cases as regressions.
    - unified process / testing / test cases ::@:: Remove obsolete test cases. Refine some test cases into regression test cases. Add new test cases for each new build.
- [software testing](../../../../general/software%20testing.md) ::@:: It is the act of checking whether software satisfies expectations.
  - software testing / failures ::@:: Skipping testing can lead to \(catastrophic\) failures: Mars polar lander crash, Vancouver Stock Exchange, rocket self-destruct, etc.
    - software testing / failures / rocket self-destruct ::@:: Ariane 5 rocket: 16-bit conversion error, disabled exception handler, crashed program, exploded rocket → 1 billion USD loss
    - software testing / failures / Mars polar lander crash ::@:: sensor logic bug caused premature engine shutdown 130 feet above the surface → 120 million USD loss
    - software testing / failures / Vancouver Stock Exchange ::@:: truncation instead of rounding led to a drastic index drop in the long-term due to repeated truncation; illustrates subtle software bugs can have huge economic impact
  - software testing / goals ::@:: Find discrepancies between _expected_ and _actual_ behavior, e.g. finding bugs. <p> There are 2 aspects: _validation_ and _verification_.
    - software testing / goals / validation ::@:: Does the product meet user requirements? Perform _acceptance tests_.
    - software testing / goals / verification ::@:: Is the implementation correct? Most _unit/integration tests_ focus here.
  - software testing / non-goals ::@:: It cannot show the _absence_ of software errors, e.g. ensuring no bugs.
  - software testing / constraints ::@:: Exhaustive testing is infeasible; sometimes, a trillion runs would be required for a small example. <p> Further, testing is inherently destructive – you deliberately try to make the system fail, but developers often lack incentive to test their own code because they do not want to make it fail.
  - software testing / planning ::@:: It consists of a _testing strategy_ \(what? how? coverage?\), _schedule_ \(when\), and resource estimate \(human, system, etc.\).
    - software testing / planning / goals ::@:: Without planning, attempting all inputs (e.g., $1 \le x,y,z \le 10\,000$) is impossible. A well-designed test suite balances _coverage_ against _cost_. It should be _small enough_ to _finish quickly_, but also _large enough_ to properly _validate and verify_ the software. <!-- Up to 40% of project effort can be spent on testing; planning saves time and money. -->
  - software testing / input partitioning ::@:: An important aspect of test planning is to partition all possible valid and invalid inputs. 3 important concepts: _ideal partitioning_, _execution equivalence_, and _revealing subdomains_.
    - software testing / input partitioning / ideal partitioning ::@:: Split inputs into equivalence classes where the program has the _same behavior_. <p> However, this requires a precise definition of "_same behavior_" to be translated into practice.
    - software testing / input partitioning / execution equivalence ::@:: A _naive_ definition of "_same behavior_". Inputs are equivalent if the program _takes the same sequence of steps_. <p> However, it is highly dependent on the actual implementation \(as we are considering the _steps_ a program takes\), which may be buggy itself.
    - software testing / input partitioning / revealing subdomains ::@:: A _better_ definition of "_same behavior_". Inputs are equivalent if the program _either_ runs correctly _or_ incorrectly on all of them. <p> A _subdomain_ is a _subset_ of the set of all possible inputs. It is _revealing_ for a particular error _E_ if inputs in the subdomain are equivalent \(using the above definition\) and if the program has error _E_, it is revealed by testing. <p> This improves upon _execution equivalence_ by relying _less_ on the actual implementation.
    - software testing / input partitioning / heuristics ::@:: Use _program-dependent_ information (compiler diagnostics, control flow, data structures). Combine with _program-independent_ cues (algorithms, domain knowledge, specifications). _Multiple heuristics_ are combined in practice, e.g. mixing execution equivalence and revealing subdomains. <p> A good heuristic yields _few subdomains_ yet _high probability_ of revealing errors \(in some class of errors _E_\).
- [test case](../../../../general/test%20case%20(software).md) ::@:: It is a specification of the inputs, execution conditions, testing procedure, and expected results that define a single test to be executed to achieve a particular software testing objective, such as to exercise a particular program path or to verify compliance with a specific requirement.
  - test case / properties ::@:: what to test, what conditions, how to test, expected result
  - test case / simple definition ::@:: It is one way to test the system: <p> 1. Select input data or configuration. <br/> 2. Specify the expected outcome (including error codes). <br/> 3. Execute and record actual result. <br/> 4. Compare against expectation.
  - test case / taxonomy ::@:: black-box testing, regression testing \(mix\), white-box testing
    - test case / taxonomy / white-box ::@:: "_Testing-in-the-small_": Uses internal knowledge; verifies component logic, requires source code.
    - test case / taxonomy / black-box ::@:: "_Testing-in-the-large_": Tests based on specification; no source access needed.
    - test case / taxonomy / regression ::@:: Re-tests after _changes_ to ensure _no new defects appear_; mixes white and black box techniques, with more emphasized on white box.
  - test case / documentation ::@:: recommended fields: name, description → target component, target operation → test type, test value\(s\) → verification \(expected result\), notes on verification <p> It takes a lot of time and effort to generate these information!!
    - test case / documentation / test type ::@:: black/white box; valid/invalid input/output; etc.
- [white-box testing](../../../../general/white-box%20testing.md) ::@:: It is a method of software testing that tests internal structures or workings of an application, as opposed to its functionality (i.e. black-box testing).
  - white-box testing / strategies ::@:: basis path testing, condition testing, data flow testing, loop testing, etc.
    - white-box testing / strategies / basis path testing ::@:: Cover every _independent path_ at least once.
    - white-box testing / strategies / condition testing ::@:: Exercise each _decision_'s true/false branches.
    - white-box testing / strategies / loop testing ::@:: Hit loop _boundaries_ \(e.g. starting values, ending values\) and _interior_ iterations.
    - white-box testing / strategies / data flow testing ::@:: Ensure all internal data structures are validated.
- [basis path testing](../../../../general/basis%20path%20testing.md) ::@:: It is a white box method for designing test cases. The method analyzes the control-flow graph of a program to find a set of linearly independent paths of execution.
  - basis path testing / motivation ::@:: Running every statement is insufficient. Some errors only appear when a particular branch is _not taken_.
  - basis path testing / steps ::@:: 1. Draw the _statement graph_: a node for each statement \(_short-circuiting operators_ are considered multiple statements\), edges for control flow. Label "T" \(true\) and "F" \(false\) for branching. <br/> 2. Draw the _flow graph_: collapse blocks of consecutive statements that are always executed together. <br/> 3. Compute _cyclomatic complexity_ $V(G)$ via any of formulas below. <br/> 4. Identify a _basis set_ consisting of _at most_ $V(G)$ _independent paths_; the basis paths should traverse all _edges_ \(not all _nodes_\), and each path must traverse at least _one new edge_. <br/> 5. Create test cases that exercise each path; guarantee every statement runs at least once.
- [control-flow graph](../../../../general/control-flow%20graph.md) \(CFG\) ::@:: It is a representation, using graph notation, of all paths that might be traversed through a function during its execution.
  - control-flow graph / definition ::@:: It is the directed graph of the basic blocks of the function (the nodes of the graph) and the control flow between them (the edges of the graph).
  - control-flow graph / basic block ::@:: It is a straight-line code sequence with no branches in except to the entry and no branches out except at the exit.
  - control-flow graph / construction ::@:: First, draw the _statement graph_ _line-by-line_, including _starting_ and _ending_ statements. Use _statement number_. Label "T" \(true\) and "F" \(false\) for branching. Note _short-circuiting operators_ are considered _separate statements_ even if they appear in line. <p> Then, collapse blocks of consecutive statements that are always executed together. These blocks are _basic blocks_. Reassign _flow graph number_. Still label "T" \(true\) and "F" \(false\) for branching. Also, add a _flow graph number_ to _statement number_ mapping \(__this course__: __important__\).
- [cyclomatic complexity](../../../../general/cyclomatic%20complexity.md) ::@:: It is a software metric used to indicate the complexity of a program. It is a quantitative measure of the number of linearly independent paths through a program's source code. It was developed by Thomas J. McCabe, Sr. in 1976.
  - cyclomatic complexity / basis set ::@:: It consists of _at most_ $V(G)$ _independent paths_; the basis paths should traverse all _edges_ \(not all _nodes_\), and each path must traverse at least _one new edge_. <p> It is _not unique_. It is the _minimum_ number of test cases required. <p> \(__this course__: When writing a independent path, use _statement number_, not _flow graph number_.\)
  - cyclomatic complexity / formulas ::@:: edges & nodes, decision points, regions
    - cyclomatic complexity / formulas / edges & nodes ::@:: $$E - N + 2P\,,$$ where $E$ is the number of edges, $N$ is the number of nodes, and $P$ is the number of connected components \(CCs\). <p> For a single program \(1 CC\), it simplifies to $E - N + 2$.
    - cyclomatic complexity / formulas / decision points ::@:: $$\pi - s + 2\,,$$ where $\pi$ is the number of _binary_ decision points \(predicates\) and $s$ is the number of exit points. <p> For a single-exit program, it simplifies to $\pi + 1$.
    - cyclomatic complexity / formulas / regions ::@:: Assuming there is a single program \(1 CC\). It is the number of regions partitioned by the flow graph, including the _outside_ "region".
  - cyclomatic complexity / interpretation ::@:: The value reflects the logical richness of the procedure; higher values mean more _testing effort_ or less _maintainability_.
    - cyclomatic complexity / interpretation / too high ::@:: If too high \(__this course__: say &gt;10\), then consider additionally strategies: branch reduction, basis path generation, modularization, etc.
- basis path testing
  - basis path testing / basis set ::@:: It can be used to prepare test cases that tests _every edge_ at least once \(_not every path_ at least once\). <p> Note that the number of independent paths in a basis set \(hence, the _minimum_ number of necessary test cases\) can be less than $V(G)$ because some paths may overlap in executed statements.
  - basis path testing / scope ::@:: It should _always_ be applied to _critical components_, and ideally should apply to _all components_.
  - basis path testing / benefits ::@:: Every statement executes at least once. Both sides of control flow decisions are taken at least once. All of these are done without enumerating every possible input combination. <p> Thus, it helps uncover defects tied to specific branches or loop conditions.
  - basis path testing / limitations ::@:: It is _systematic_ but still limited to _control-flow coverage_, not data-space or interaction coverage, thus not _exhaustive_.
- quiz: [quiz 12](questions/quiz%2012.md)
- [questions § week 7 pre-lecture](questions/index.md#week%207%20pre-lecture)

## week 7 lecture

- datetime: 2025-10-15T12:30:00+08:00/2025-10-15T14:20:00+08:00, PT1H50M
- topic: use case diagram; use case specification; basic flow; extension point; alternative flow; subflow
- [UML](UML.md)
  - [§ common mistakes](UML.md#common%20mistakes)
  - [§ common mistakes: redundant associations](UML.md#common%20mistakes%20redundant%20associations)
  - [§ common mistakes: IO as actors](UML.md#common%20mistakes%20IO%20as%20actors)
  - [§ common mistakes: nonfunctional requirements as use case](UML.md#common%20mistakes%20nonfunctional%20requirements%20as%20use%20case)
- [§ week 5 pre-lecture](#week%205%20pre-lecture)
- [questions § week 7 lecture](questions/index.md#week%207%20lecture)

## week 7 lab

- datetime: 2025-10-16T18:00:00+08:00/2025-10-16T19:50:00+08:00, PT1H50M
- topic: debugging in IntelliJ IDEA
- COMP 3111H
  - COMP 3111H / lab 6 ::@:: clone → run to see error → set breakpoint → identify bug → fix bug
    - COMP 3111H / lab 6 / breakpoint ::@:: In IntelliJ IDEA, click in the left gutter to toggle a red dot, marking a breakpoint. <p> Start debugging with "Debug" (`Shift+F9`) so execution pauses at this spot. Use the "Resume Program" button (`F9`) to continue execution until the next breakpoint.
    - COMP 3111H / lab 6 / code step-through ::@:: Use "Step Over" (`F8`) and "Step Into" (`F7`) to respectively traverse over and into method calls, watching the state evolve line by line.
    - COMP 3111H / lab 6 / state debugging ::@:: While stopped at a breakpoint, examine the current state in the "Variables" pane.
    - COMP 3111H / lab 6 / stacktrace ::@:: Trace the call stack to understand why an exception is thrown or a value is incorrect.
- assignment: [lab 6](assignments/lab%206/index.md)

## week 8 pre-lecture

- topic: \(none\)
- status: unscheduled
- [questions § week 8 pre-lecture](questions/index.md#week%208%20pre-lecture)

## week 8 lecture

- datetime: 2025-10-22T12:30:00+08:00/2025-10-22T14:20:00+08:00, PT1H50M
- topic: use case diagram; non-functional requirement; validation; implementation; defensive programming; code review; refactoring; debugging; configuration management
- [UML](UML.md)
  - [§ common mistakes](UML.md#common%20mistakes)
  - [§ common mistakes: wrong initiating actors](UML.md#common%20mistakes%20wrong%20initiating%20actors)
  - [§ common mistakes: not using actor generalization](UML.md#common%20mistakes%20not%20using%20actor%20generalization)
  - [§ common mistakes: use case without initiating actors](UML.md#common%20mistakes%20use%20case%20without%20initiating%20actors)
  - [§ common mistakes: missing nonfunctional requirements](UML.md#common%20mistakes%20missing%20nonfunctional%20requirements)
- basis path testing
  - basis path testing / redundant paths ::@:: In practice, redundant paths are added \(i.e. more test cases\) for safety, especially when boundary or error conditions might be missed otherwise. <p> \(__this course__: In examinations, do _not_ add redundant paths when asked for independent paths.\)
- COMP 3111H
  - COMP 3111H / midterm examination ::@:: The midterm will be a one-hour quiz that tests the basics of software engineering concepts (e.g., use-case diagrams, class diagrams, testing). It is designed to confirm whether you have grasped the fundamental material from the first part of the course; nothing trickier than last year's format. <p> Historically the average score has hovered around 78–79%, so students who attend lectures and study regularly tend to perform well.
    - COMP 3111H / midterm examination / multiple choice questions ::@:: Roughly 10–20% of marks, usually three options per question. These questions will be straightforward and test recognition of concepts \(e.g., "What is a functional requirement?"\).
    - COMP 3111H / midterm examination / short questions ::@:: Questions that ask you to match items or fill in blanks; e.g., map UML symbols to their meanings, list functional vs non-functional requirements. No _precise_ memorization required – just recall the core definitions and relationships.
    - COMP 3111H / midterm examination / class diagrams ::@:: You may be asked to draw missing parts of a class diagram \(multiplicities, composition/aggregation diamonds\). Pay special attention to "contain" vs "compose"; only composition uses a filled diamond.
    - COMP 3111H / midterm examination / use case diagrams ::@:: Given a short scenario, first list all functionalities \(operations\), then group them into use cases. The instructor will give you a paragraph and expect you to extract the relevant operations before sketching a use-case diagram. <p> If the question only asks for _functionalities_, simply list all functionalities; no need to group them into use cases.
- [§ week 6 pre-lecture](#week%206%20pre-lecture)
- [§ week 7 pre-lecture](#week%207%20pre-lecture)
- [questions § week 8 lecture](questions/index.md#week%208%20lecture)

## week 8 lab

- datetime: 2025-10-23T18:00:00+08:00/2025-10-23T19:50:00+08:00, PT1H50M
- topic: unit testing; JUnit 5
- COMP 3111H
  - COMP 3111H / lab 7 ::@:: unit testing using JUnit 5
    - COMP 3111H / lab 7 / unit test ::@:: - _Define Input_ – Choose values that exercise the target function. <br/> - _Specify Expected Outcome_ – Know what the correct result should be. <br/> - _Invoke Function_ – Call the method with your chosen input. <br/> - _Assert Equality_ – Compare the actual output to the expected outcome using JUnit assertions.
    - COMP 3111H / lab 7 / inputs ::@:: Include common cases as well as edge or boundary values. Aim for a minimal set of tests that still covers all logical branches. <p> Ideally, the developer who wrote the function should write its tests because they best understand the intended behavior.
    - COMP 3111H / lab 7 / test framework ::@:: Uses JUnit 5; students must migrate any existing JUnit 4 code to version 5.
    - COMP 3111H / lab 7 / run tests ::@:: Execute all tests via IntelliJ's built-in runner or the command line. Review the test report to confirm that every test passes (100% success). Generate a coverage report; at least 10% of lines should be covered by your tests.
    - COMP 3111H / lab 7 / test-driven development \(TDD\) ::@:: Tests are written before implementing the corresponding code. <p> Benefits include fewer bugs, improved collaboration, and tests that double as documentation.
      - COMP 3111H / lab 7 / test-driven development / steps ::@:: 1. Write a test first. <br/> 2. Implement minimal logic to make the test pass. <br/> 3. Refactor both code and test for clarity while ensuring all tests remain green.
- assignment: [lab 7](assignments/lab%207/index.md)

## week 9 pre-lecture

- topic: white-box testing; black-box testing; regression testing; testing; unit testing; software testing; integration testing; system testing; acceptance testing
- white-box testing
  - white-box testing / condition testing ::@:: Focuses on exercising every possible truth value of logical conditions; a condition can be a simple condition, compound condition, relational expression, boolean expression, etc.
    - white-box testing / condition testing / detected errors ::@:: Errors arise from wrong relational operators, missing Boolean operators, incorrect arithmetic expressions, or misplaced parentheses.
    - white-box testing / condition testing / types ::@:: branch testing \(covered by _basis path testing_\), domain testing, etc.
    - white-box testing / condition testing / branch testing ::@:: For a _compound condition_ $C$, test the overall truth/false outcome plus the true/false value of every simple condition (e.g., for `C = (a>b) AND (c<d)` test all of `C`, `a>b`, and `c<d` with `true` and `false`). <p> Already covered by _basis path testing_.
    - white-box testing / condition testing / domain testing ::@:: When checking a relational expression `E1 rel-op E2`, use values that make `E1` greater than, equal to, and less than `E2`; this ensures detection of operator errors while also stressing the arithmetic parts. <p> The _absolute difference_ between `E1` and `E2` for the two unequal cases should be _as small as possible_.
  - white-box testing / loop testing ::@:: For a \(large\) loop with _n_ iterations, execute loops for 0, 1, 2 passes; then test _m_ passes for some _m &lt; n_, and finally _n−1_, _n_, _n+1_ passes to cover boundary behavior. So a loop in general requires at least _7 minimum test cases_.
    - white-box testing / loop testing / nested ::@:: Start with the innermost loop using _simple loop test_, then incrementally move outward, testing each loop level while keeping \(already tested\) inner loops and outer loops fixed at their _minima_; this strategy makes test count grow _geometrically_ with the level of _nesting_.
    - white-box testing / loop testing / independent ::@:: _Independent concatenated_ loops can be tested individually (simple loop testing).
    - white-box testing / loop testing / dependent ::@:: _Dependent concatenated_ loops \(the latter loop depends on a variable set in the former loop\) require techniques similar to those for nested loops \(e.g. using _minima_\) because inner loop behaviour changes with outer loop variables.
    - white-box testing / loop testing / unstructured ::@:: If loops cannot be easily expressed in a structured form, _refactor_ the code; such loops are especially prone to bugs and often reveal errors early when re-tested after restructuring.
    - white-box testing / loop testing / effort ::@:: By following these rules for _simple_, _nested_, _independent_, and _dependent_ loops, they are _likely_ to uncover errors with _minimum effort_ and _test overlap_.
  - white-box testing / data flow testing ::@:: Verify that each variable's value is correct at every use point by cover each _definition use \(DU\) chain_ at least once. <p> It may be combined with basis path testing.
    - white-box testing / data flow testing / definition use chain ::@:: It is the set of the tuple `(var, stmt1, stmt2)`, where `var` is not _redefined_ between `stmt1` and `stmt2`. `stmt1` is a _definition_ of `var` while `stmt2` is a _use_ of `var`.
- [black-box testing](../../../../general/black-box%20testing.md) ::@:: It is a method of software testing that examines the functionality of an application without peering into its internal structures or workings.
  - black-box testing / detected errors ::@:: Detect missing or incorrect functions, interface mismatches, database access errors, performance bottlenecks, improper initialization/termination, etc.
  - black-box testing / inputs ::@:: They should be a range of input and output values, not just a single value, so that it can probabilistically tell if a _class of errors_ is present or not.
- [equivalence partitioning](../../../../general/equivalence%20partitioning.md) \(EP\) ::@:: It is a software testing technique that divides the input data of a software unit into partitions of equivalent data from which test cases can be derived.
  - equivalence partitioning / benefits ::@:: In principle, test cases are designed to cover each partition at least once. This technique tries to define test cases that uncover classes of errors, thereby reducing the total number of test cases that must be developed. An advantage of this approach is reduction in the time required for testing software due to lesser number of test cases.
  - equivalence partitioning / subdomain selection ::@:: Select subdomains based on _valid_ and _invalid_ inputs and outputs. <p> - range, value \(ordered\): 1 valid subdomain; 2 invalid subdomains: less than, greater than; e.g. array indices, decimals, integers, etc. <br/> - set, type \(unordered\): 1 valid subdomain; 1 invalid subdomain: not of the set or type; e.g. boolean, enumeration, etc.
  - equivalence partitioning / boundary values ::@:: Test values just inside, on, and just outside the limits of each partition because off-by-one errors, null handling, overflows, and aliasing are _most likely_ near boundaries rather than the interior.
    - equivalence partitioning / boundary values / ordered ::@:: For a range or a number of discrete value \(ordered\), identify minimum and maximum. Test _minimum_, _maximum_, and the _4 values_ just below or above the minimum or maximum. Examples: array indices, decimals, integers, etc.
    - equivalence partitioning / boundary values / unordered ::@:: For a set of values or a specific type \(unordered\), test _all valid values_ \(if possible\) and at least _one invalid value_. Examples: boolean, enumeration, etc.
    - equivalence partitioning / boundary values / examples ::@:: - _`abs(int x)`_: _Typical values_ test inputs include `-1`, `0`, `1`; _boundary values_ might use `Integer.MIN_VALUE`, `Integer.MIN_VALUE + 1`, `Integer.MAX_VALUE`, and `Integer.MAX_VALUE - 1` to check overflow handling. <br/> - _student record search_ – Valid IDs range from 1&nbsp;000&nbsp;000 to 9&nbsp;999&nbsp;999; test cases include minimum/maximum valid IDs \(_boundary_\), just-outside limits \(_boundary_\), mid-range existing/non-existing records \(_typical_\), and non-numeric strings to confirm error handling \(_other_\).
  - equivalence partitioning / value types ::@:: boundary, typical, other
    - equivalence partitioning / value types / boundary ::@:: Values at and near boundaries of domains.
    - equivalence partitioning / value types / typical ::@:: Values in the interior of domains, including valid domains and invalid domains.
    - equivalence partitioning / value types / other ::@:: Values that are neither boundary nor typical, e.g. wrong type.
- black-box testing
  - black-box testing / advanced techniques ::@:: They help uncover integration or concurrency bugs that surface only when objects interact in realistic sequences.
  - black-box testing / thread testing ::@:: It is an _event-based approach_ where tests are based on _event triggers_, which is particularly suitable for _object-oriented systems_.
    - black-box testing / thread testing / workflow ::@:: After unit testing, _identify_ and _execute_ each possible event thread (sequence of object interactions or _call chain_) in a use case; focus on the most frequently executed threads \(similar to _basic flow_ in _use case diagram_\) because exhaustive coverage is impractical.
    - black-box testing / thread testing / types ::@:: - single thread: only at most one object is involved at every interaction <br/> - multiple thread: parallel or interleaved chain; multiple objects may be involved in a single interaction <br/> - multi-input thread: several inputs are fed to the same object to start a thread
  - black-box testing / state-based testing ::@:: It verifies that _a class_ reaches the _correct state_ after each event by comparing its actual _attributes_ and _relationships_ with those specified in the expected state.
    - black-box testing / state-based testing / workflow ::@:: For a class, use a _state-machine diagram_ to derive test cases. For each _transition_, derive a _representative set_ of _events_ \("stimuli"\) that cause the transition. <p> Before each event, set an object of the class to the desired state. Apply the event. Verify that the actual state matches the expected state, ensuring correct state progression. <p> This is similar to equivalence testing but on _transitions_.
  - black-box testing / workflow ::@:: Start with _equivalence partitioning_ and _boundary value_ analysis \(BVA\) to write test cases. Add special test cases \(e.g. wrong input type\). Then add _thread tests_ for _critical_ interaction paths. Finally, add _state-based tests_ to verify internal transitions or transitions due to external event triggers.
- regression testing
  - regression testing / workflow
  - regression testing / benefits
  - regression testing / maintenance
- software testing
  - software testing / white-box vs. black box ::@:: Both approaches are complementary; white-box is often used for unit tests, while black-box is favored for integration, system, and acceptance testing. <p> Combine black-box, data-flow, branch, loop, and state tests with regression checks to form a comprehensive suite that balances coverage and effort while minimizing overlap.
- quiz: [quiz 13](questions/quiz%2013.md)
- software testing
  - software testing / goals
  - software testing / benefits ::@:: It aims to detect defects early, reduce maintenance costs, and increase user confidence. A systematic process helps ensure reliability, safety, and compliance with requirements.
  - software testing / automation ::@:: Running tests manually is tedious and time consuming, as there are many possible inputs and states. <p> A _test component_ automates some test procedures. Tools are available to record actions \(like macros\) and parameterize them to accept varying inputs.
    - software testing / automation / storage ::@:: _Spreadsheets_ or _databases_ can be used to store _inputs_ and _actual outputs_ of each test. It may also keep track of test _history_.
    - software testing / automation / tools ::@:: JUnit, Selenium, etc.
  - software testing / evaluation ::@:: test \(software config, test config\) → evaluate → done \(if no errors\), debug \(if errors; later, → test\), and always update _reliability and quality model_ using new _error rate_ data
  - software testing / testing strategy ::@:: A _testing strategy_ outlines which techniques—such as white-box or black-box—are suitable at each stage of development, integrating test cases into a structured sequence of _steps_ that define _what_ to test, _when_ it will occur, and the required _effort, time, and resources_.
    - software testing / testing strategy / tradeoff ::@:: Because _debugging_ introduces _unpredictable delays_, the strategy must balance _flexibility and creativity_ with disciplined _planning and management_. Testing typically intensifies under _tight deadlines_, so progress needs to be _measurable_ and issues _uncovered_ as early as possible.
    - software testing / testing strategy / typical ::@:: - design system _outside in_: requirements capture → analysis → design → implement <br/> - test system _inside out_: unit testing → integration testing → system testing \(developer\) → acceptance testing \(client\)
- [unit testing](../../../../general/unit%20testing.md) ::@:: It is a form of software testing by which isolated source code is tested to validate expected behavior.
  - unit testing / nature ::@:: white-box \(emphasized\) and black-box, run by developers
- [integration testing](../../../../general/integration%20testing.md) ::@:: It is a form of software testing in which multiple software components, modules, or services are tested together to verify they work as expected when combined.
  - integration testing / nature ::@:: white-box and black-box, run by developers or independent test group
- [system testing](../../../../general/system%20testing.md) ::@:: It  is testing conducted on a complete software system. It describes testing at the system level to contrast to testing at the system integration, integration or unit level.
  - system testing / nature ::@:: black-box, run by independent test group
- [acceptance testing](../../../../general/acceptance%20testing.md) ::@:: It is a test conducted to determine if the requirements of a specification or contract are met. It may involve chemical tests, physical tests, or performance tests.
  - acceptance testing / nature ::@:: black-box, run by client or user
- unit testing
  - unit testing / aspects ::@:: boundary values, exception handling, independent paths, interfaces, internal data structures, etc.
  - unit testing / techniques ::@:: Each unit (typically a class or method) is tested individually using _drivers_ and _stubs_ to isolate dependencies. <p> - _driver_: a component to call the component under testing <br/> - _stub_: a component called by the component under testing
    - unit testing / techniques / drivers ::@:: A driver supplies values to a function or method being tested. Drivers also capture and verify output against known correct outcomes. <p> _Example_: testing an `abs()` routine – the driver sends positive, negative, and zero inputs, then checks that the returned absolute value matches the expected result.
    - unit testing / techniques / stubs ::@:: When the unit calls another class that isn't implemented yet, a stub mimics that collaborator's behavior. Stubs provide deterministic, repeatable responses so tests are not affected by external systems. <p> _Example_: a student info request is answered by a stub that always returns a fixed record, allowing the unit to finish its execution path without real data access.
    - unit testing / techniques / object orientation ::@:: Object-oriented tests must cover at least a class \(not simply a field or method\). Check all possible states of an object. For subclasses, test both _inherited_ and _overridden_ methods due to dynamic binding and substitutability \(Liskov substitution principle\).
    - unit testing / techniques / bypassing encapsulation ::@:: Encapsulation can be addressed by providing test-only accessors that expose internal state for verification.
- integration testing
  - integration testing / detected errors ::@:: _interaction errors_, e.g. interface misunderstanding, interface misuse, timing errors, etc.
  - integration testing / approaches ::@:: These approaches uses _incremental construction_, _incremental builds_, and _regression testing_: bottom-up, top-down, sandwich \(hybrid\).
  - integration testing / top-down ::@:: Start from high-level components, use stubs for lower modules, and integrate progressively: replace lower modules _depth-first_ or _breadth-first_, and use _regression testing_. <p> Useful when the UI is critical early on.
    - integration testing / top-down / advantages ::@:: - Allows early _validation_ of user interface components, enabling quick demonstration of core system functionality. <br/> - Facilitates immediate detection of UI-related defects.
    - integration testing / top-down / disadvantages ::@:: - Delays testing of deeper, low-level processing until later stages because those modules cannot be exercised without stubs. <br/> - Requires the creation and maintenance of stub components to simulate lower layers.
  - integration testing / bottom-up ::@:: Begin with low-level units \(which are grouped into _builds_\), replace drivers gradually: replace upper modules _depth-first_ \(not _breadth-first_\). <p> Easier to detect interface faults but delays user-interface testing.
    - integration testing / bottom-up / advantages ::@:: - Makes it simpler to uncover interaction faults because lower-level modules are integrated first. <br/> - Test case design is straightforward and does not rely on stub components \(only drivers\).
    - integration testing / bottom-up / disadvantages ::@:: - The user interface is only examined after all underlying layers have been tested, delaying UI _validation_.
  - integration testing / sandwich ::@:: Combine top-down and bottom-up to test upper and lower modules simultaneously, and merge them at the end for a complete integration test; can reduce overall test time.
    - integration testing / sandwich / advantages ::@:: - _parallel testing_: By building lower-level subsystems first with real drivers while simultaneously testing higher-level modules through stubs, the overall testing cycle can be compressed considerably.
    - integration testing / sandwich / disadvantages ::@:: - The need to manage both driver and stub layers for different parts of the system adds complexity to test setup. <br/> - Coordination between the two "sides" of the integration may require additional effort to ensure consistency.
  - integration testing / critical subsystems ::@:: Identify components with high _risk_, multiple _use-case coverage_, high _control level_, high _complexity_, or _performance constraints_ as critical. <p> Test these subsystems early and repeatedly. Must apply _regression tests_ after each change to maintain stability.
- system testing
  - system testing / types ::@:: functional, performance, pilot \(alpha, beta\), acceptance, installation
  - system testing / functional ::@:: Test the whole system to verify that all user operations work per the _system requirements specification_ \(SRS\).
  - system testing / performance ::@:: Assess stress (max concurrent users), volume (large data sets), security (access controls), timing (real-time constraints), recovery (fail-over scenarios), etc.
  - system testing / pilot ::@:: Conduct controlled or real-world tests with a subset of users to uncover environment-specific defects in common _functionality_.
  - system testing / acceptance ::@:: The end-user or client _verifies_ that the system is _usable_ and _validates_ that all _functional_ and _non-functional_ specifications meet the documented requirements \(SRS\).
  - system testing / installation ::@:: The user _verifies_ _usability_ and _validates_ that both _functional_ and _nonfunctional_ criteria are satisfied when the software runs in its intended _production environment_.
  - system testing / pilot
    - system testing / pilot / alpha ::@:: Conducted in a _controlled setting_ (typically at the developer's site) where users perform tests under observation, allowing developers to monitor usage and gather immediate feedback.
    - system testing / pilot / beta ::@:: Executed in the _user's own environment_; participants run the software during normal operations, identify defects from everyday use, and report issues back to the development team.
- acceptance testing
  - acceptance testing / aspects ::@:: We confirm three key aspects and an additional aspect: <p> - _functional validity_, ensuring the software actually performs the features it promises <br/> - _interface validity_, verifying that each user interface accepts the correct inputs and delivers the expected outputs while conforming to design guidelines <br/> - _information content_, checking that stored data are accurate, correctly formatted, and respect all constraints. <br/> - _performance_: Additionally, we evaluate whether the system satisfies its performance targets.
  - acceptance testing / workflow ::@:: restatement → addition → scenarios
    - acceptance testing / workflow / restatement ::@:: Translate written requirements into _concise_, _precise_, and _testable_ criteria by _grouping_ related items and _eliminating_ non-testable statements \(e.g. decisions made by users\).
    - acceptance testing / workflow / addition ::@:: Include any extra user-derived requirements by examining the _use cases_ to uncover missing _functional_ and _interface_ needs, consulting the _domain model_ to identify _information-content_ constraints, and reviewing the _non-functional_ specifications for _performance_ expectations.
    - acceptance testing / workflow / scenarios ::@:: For each requirement, create an _evaluation scenario_ that demonstrate to the client the _requirement is met_. The set of scenarios should be _run by the client_ to confirm _system readiness_, so the language should be _client-friendly_.
      - acceptance testing / workflow / scenarios / format ::@:: Scenarios should be written such that it tests the system, not the client or user. Thus, most if not all scenarios should start with the keyword "_demonstrate_". <p> Scenarios can be _grouped_.
- software testing
  - software testing / evaluation ::@:: _Compare_ outcomes against planned _test goals_ and measure _metrics_ to determine software _quality_. Also know when to _stop testing_.
    - software testing / evaluation / metrics ::@:: - completeness/coverage: % of tests cases run, % of code tested <br/> - reliability: based on testing error rates compared to previous projects
    - software testing / evaluation / historical data ::@:: Use historical data to predict expected failure rates, e.g. plotting _failures per test hour_ against _testing time_. <p> If _actual failure rate_ is too high compared to expected, _additional testing_ may be needed or criteria should be _relaxed_. Alternatively, deliver  _acceptance parts_ of the system only for now \(_incremental release_\).
    - software testing / evaluation / readiness ::@:: Establish clear stop-criteria: when coverage meets thresholds and the error rate falls below acceptable limits \(e.g. 99% pass rate\), consider the build ready for release.
  - software testing / prioritization ::@:: Prioritize tests that validate _core_ functionality \(black-box testing\), _legacy_ features, and _typical_ usage scenarios over, respectively, system components \(white-box testing\), new features, or boundary cases. <p> These focus on preventing _user-impacting defects_; functional completeness outweighs exhaustive corner-case coverage when deadlines loom.
- quiz: [quiz 14](questions/quiz%2014.md)
- [questions § week 9 pre-lecture](questions/index.md#week%209%20pre-lecture)

## week 9 lecture

- datetime: 2025-10-29T12:30:00+08:00/2025-10-22T14:20:00+08:00, PT1H50M
- status: unscheduled; public holiday: Chung Yeung Festival
- [§ week 9 pre-lecture](#week%209%20pre-lecture)
- [questions § week 9 lecture](questions/index.md#week%209%20lecture)

---

> Dear Comp3111 Students,
>
> We don't have class today in order to synchronize the progress with L1 \(public holiday yesterday\). Thanks.
>
> Regards,
>
> \[redacted\]

## midterm examination

- datetime: 2025-10-29T12:00:00+08:00/2025-10-29T13:00:00+08:00, PT1H
- venue: Lecture Theater A
- format
  - calculator: no
  - cheatsheet: no
  - referencing: closed book, closed notes
  - provided: \(none\)
  - questions: question ×5 \(with subquestions\)
- grades: 95/100 → 96/100
  - statistics
    - timestamps: 2025-10-30T14:52:04+08:00 → 2025-10-31T12:50:24+08:00
    - mean: 79.68 \(provided: 80.13872832\) → 80.95
    - standard deviation: ? → ?
    - low: 0 \(provided: 37\) → 0
    - lower quartile: 75 → 76
    - median: 81.5 → 83.75
    - upper quartile: 87.38 → 89
    - high: 96 \(provided: 96\) → 97
    - distribution: ? → ?
    - data: ? → ?
  - breakdown
    - question 1 \(multiple choice questions\): 14/15 → 14/15
    - question 2 \(short questions\): 24/25 → 24/25
    - question 3 \(software development process matching\): 8/10 → 8/10
    - question 4 \(UML diagram\): 34/35 → 35/35
    - question 5 \(use case functionalities\): 15/15 → 15/15
- report
  - What do quality design goals help _most_ in reducing the complexity of? \(–1\) ::@:: _Designing_ the system, not _building_ the system.
  - software development complexity matching \(0\) ::@:: - application domain: often complex problems <br/> - communication between stakeholders: different background, different vocabularies, inherent ambiguity <br/> - managing large projects: requires division of labor and coordination; both difficult <br/> - coding: complicated engineering process
  - software engineer skills \(0\) ::@:: - communication: Because software projects are often large and require a team to work on them, so communication with other developers is important. <br/> - project management: Because software projects are often large, they require planning and division of labor, which requires project management skills. <br/> - etc.
  - attribute multiplicity notation \(–1\) ::@:: `name: type [min..max]`. Wrote `[3]` instead.
  - software development process matching \(–2\) ::@:: Correct \(got them swapped\): <p> - waterfall: rigorous and formalized process <br/> - spiral: planning helps meet user expectations
  - UML diagram \(–1\) ::@:: No one knows why a point was deducted... Rectified \(see below\).
  - use case functionalities \(0\) ::@:: When asked for "use case _functionalities_" rather than "use case _diagram_", you should simply list out the functionalities required by each actor. Do not include implementation details in the functionalities, e.g. the medium through which communication happens, etc.
- check
  - datetime: 2025-10-30T18:00:00+08:00/2025-10-30T19:30:00+08:00, PT1H30M
  - venue: Room 2465, Academic Building
  - report
    - UML diagram \(+1\) ::@:: No one knows why a point was deducted...

---

> Dear COMP3111 Students,
>
> Just a reminder about the midterm quiz on Oct29 \(12nn-1pm\) in LTA \(H, L1, L2 altogether in LTA\). It's a closed book exam, and it covers the following topics L01-L09:
>
> \#1 - Introduction <br/>
> \#2 - Modeling Software Systems using UML <br/>
> \#3 - Software Development <br/>
> \#4 - Domain Modeling and Use Case Modeling <br/>
> \#5 - Use Case Specification and Non-Functional Requirements
>
> Regards, <br/>
> Kenneth
>
> Regards,
>
> \[redacted\]

---

> Dear Students,
>
> __Lab 8 and paper checking session arrangements are as follows:__
>
> Lab 8: <br/>
> The first LA1 session for lab 8 will be used/replaced by a paper checking session \(more details in this email\). <br/>
> We will have only one session for Lab 8 tomorrow \(Friday\) from 10:30 am to 12:20 pm in Room 2465. A Zoom recording will be available for this lab in case you are unable to join the session. And that will be our last lab. There will be no lab sessions after that \(unless required or announced\).
>
> __Paper Checking:__ <br/>
> We will have our paper checking session today \(30-October-2025, Thursday\) from 06:00-07:30 pm in Room 2465
>
> __Things to consider when you come for a paper checking session:__ <br/>
> 1\) Please bring your student ID and give it to the TA to get your exam. Return the exam paper to get your student ID back <br/>
> 2\) Please don't take pictures/videos of your exam and exam solution \(if we find that, we will take strict action\) <br/>
> 3\) Please don't leave the exam checking venue with the exam or the exam solution <br/>
> 4\) We will have a limited number of exam solutions available in the venue (10 copies only), so you have to share the solution with others. <br/>
> 5\) If you cannot join today's paper checking session, you can ask your friend to check the exam on your behalf. <br/>
> 6\) There will be no other paper checking session after today.
>
> Regards, <br/>
> COMP3111 Teaching Team

## week 9 lab

- datetime: 2025-10-30T18:00:00+08:00/2025-10-30T19:50:00+08:00, PT1H50M
- status: rescheduled
- topic: merge conflict; Javadoc
- COMP 3111H
  - COMP 3111H / lab 8 ::@:: Resolve merge conflict in Git. Write Javadoc.
    - COMP 3111H / lab 8 / merge conflict ::@:: Merge conflicts arise when two branches modify the same line or file differently; Git cannot decide automatically. Common scenarios: parallel edits on a single line, one branch deletes while another edits the same file.
    - COMP 3111H / lab 8 / resolve merge conflict ::@:: - _GitHub_ \(rarely used\): Use the online conflict editor when creating or merging a pull request. Select which version of the conflicting lines to keep and mark the conflict as resolved before committing. <br/> - _Locally_ \(recommended\): Pull the latest changes from the remote branch into your local clone. Merge the target branch into your working branch using IntelliJ or the command line. Resolve conflicts by choosing left/right/combined code in the IDE's conflict dialog, then commit the merge.
    - COMP 3111H / lab 8 / Javadoc ::@:: Placed immediately above a class, method or field declaration. Provides a description plus metadata tags such as `@param`, `@return`, `@throws`, etc.
    - COMP 3111H / lab 8 / Javadoc template ::@:: Type `/**` before the declaration and press Enter; the IDE inserts a template with placeholders for summary and tags. <p> Alternatively, place the caret on the declaration, hit `Alt`+`Enter` (Windows) or `Option`+`Enter` (macOS). Select "Add Javadoc" from the quick-fix menu; the IDE generates a ready-to-edit comment block.

---

> Dear Students,
>
> __Lab 8 and paper checking session arrangements are as follows:__
>
> Lab 8: <br/>
> The first LA1 session for lab 8 will be used/replaced by a paper checking session \(more details in this email\). <br/>
> We will have only one session for Lab 8 tomorrow \(Friday\) from 10:30 am to 12:20 pm in Room 2465. A Zoom recording will be available for this lab in case you are unable to join the session. And that will be our last lab. There will be no lab sessions after that \(unless required or announced\).
>
> __Paper Checking:__ <br/>
> We will have our paper checking session today \(30-October-2025, Thursday\) from 06:00-07:30 pm in Room 2465
>
> __Things to consider when you come for a paper checking session:__ <br/>
> 1\) Please bring your student ID and give it to the TA to get your exam. Return the exam paper to get your student ID back <br/>
> 2\) Please don't take pictures/videos of your exam and exam solution \(if we find that, we will take strict action\) <br/>
> 3\) Please don't leave the exam checking venue with the exam or the exam solution <br/>
> 4\) We will have a limited number of exam solutions available in the venue (10 copies only), so you have to share the solution with others. <br/>
> 5\) If you cannot join today's paper checking session, you can ask your friend to check the exam on your behalf. <br/>
> 6\) There will be no other paper checking session after today.
>
> Regards, <br/>
> COMP3111 Teaching Team

## week 10 pre-lecture

- topic:
- quiz: [quiz 15](questions/quiz%2015.md)
- quiz: [quiz 16](questions/quiz%2016.md)
- [questions § week 10 pre-lecture](questions/index.md#week%2010%20pre-lecture)

## week 10 lecture

- datetime: 2025-11-05T12:30:00+08:00/2025-11-05T14:20:00+08:00, PT1H50M
- topic: white-box testing; black-box testing; regression testing; testing; unit testing; software testing; integration testing; system testing; acceptance testing
- [§ week 9 pre-lecture](#week%209%20pre-lecture)
- [questions § week 10 lecture](questions/index.md#week%2010%20lecture)

## week 10 lab

- datetime: 2025-11-06T18:00:00+08:00/2025-11-06T19:50:00+08:00, PT1H50M
- status: unscheduled

## aftermath

### total

- grades: ?/100
  - statistics: ?
