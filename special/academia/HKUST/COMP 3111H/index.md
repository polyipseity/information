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
- [software engineering](../../../../general/software%20engineering.md) ::@:: It is a branch of both computer science and engineering focused on designing, developing, testing, and maintaining software applications. It involves applying engineering principles and computer programming expertise to develop software systems that meet user needs. <!--SR:!2025-10-09,16,290!2025-10-08,15,290-->
- [source lines of code](../../../../general/source%20lines%20of%20code.md) \(SLOC\) ::@:: It is a software metric used to measure the size of a computer program by counting the number of lines in the text of the program's source code. <!--SR:!2025-10-07,14,290!2025-10-09,16,290-->
  - source lines of code / acronyms ::@:: LLOC: logical lines of code; logical SLOC <br/> LOC: lines of code; physical SLOC <br/> MLOC: million lines of code <br/> SLOC: source lines of code <!--SR:!2025-10-07,14,290!2025-10-08,15,290-->
  - source lines of code / examples ::@:: Rome: Total War &lt; Boeing 787 &lt; F-35 Fighter Jet &lt; Windows 7 &lt; Windows 10 &lt; Facebook &lt; Mac OS X &lt; luxury passenger car <!--SR:!2025-10-05,12,270!2025-10-12,12,230-->
  - source lines of code / effort ::@:: Effort is not _linearly_ proportional to source lines of code!! <!--SR:!2025-10-09,16,290!2025-10-08,15,290-->
- [software maintenance](../../../../general/software%20maintenance.md) ::@:: It is the modification of software after delivery. <p> It is often considered lower skilled and less rewarding than new development. As such, it is a common target for outsourcing or offshoring. <!--SR:!2025-10-07,14,290!2025-10-08,15,290-->
  - software maintenance / complexity ::@:: It can be complex. Indeed, given the large amount of existing software, it uses the most time of most developers. <!--SR:!2025-10-08,15,290!2025-10-07,14,290-->
- [programming complexity](../../../../general/programming%20complexity.md) ::@:: It is a term that includes software properties that affect internal interactions. <!--SR:!2025-10-08,15,290!2025-10-07,14,290-->
  - programming complexity / sources ::@:: application domain, communication, management, tools <!--SR:!2025-10-08,15,290!2025-10-09,16,290-->
    - programming complexity / sources / application domain ::@:: A problem is often _complex_ and outside the domain of most developers \(i.e. not _domain experts\). <!--SR:!2025-10-09,16,290!2025-10-09,16,290-->
    - programming complexity / sources / communication ::@:: Clients and developers have different _background_, _vocabulary_, etc. which is made worse by _ambiguity_ of human languages. <!--SR:!2025-10-08,15,290!2025-10-08,15,290-->
    - programming complexity / sources / management ::@:: _Dividing_ a project and _reassembling_ it is difficult. _Coordination_ between different _parts_ and _people_ is also difficult. <!--SR:!2025-10-09,16,290!2025-10-07,14,290-->
    - programming complexity / sources / tools ::@:: Creating useful _tools_ for software development is also complex. Indeed, creating the tools themselves also require software engineering. <!--SR:!2025-10-07,14,290!2025-10-08,15,290-->
  - programming complexity / problems ::@:: development, quality <!--SR:!2025-10-07,14,290!2025-10-09,16,290-->
    - programming complexity / problems / quality ::@:: abandonment \(London Stock Exchange; after 5 years of development\), inflexible, unreliable \(Ariane 5 \(rocket\)\), unsafe \(London Ambulance Service; fell twice 1992\), etc. <!--SR:!2025-10-09,16,290!2025-10-09,16,290-->
      - programming complexity / problems / quality / examples ::@:: A small software update to Amazon, a large and complex website, caused \$2.8 million in lost revenue. <!--SR:!2025-10-05,12,270!2025-10-09,16,290-->
- [Ariane 5](../../../../general/Ariane%205.md) ::@:: It is a retired European heavy-lift space launch vehicle operated by Arianespace for the European Space Agency \(ESA\). <!--SR:!2025-10-05,12,270!2025-10-09,16,290-->
  - Ariane 5 / notable launches
    - Ariane 5 / notable launches / first test flight ::@:: Ariane 5's first test flight \(Ariane 5 Flight 501\) on 4 June 1996 failed, with the rocket self-destructing 37 seconds after launch because of a malfunction in the control software. <!--SR:!2025-10-05,12,270!2025-10-07,14,290-->
      - Ariane 5 / notable launches / first test flight / cause ::@:: A data conversion from 64-bit floating-point value to 16-bit signed integer value to be stored in a variable representing horizontal bias caused a processor trap \(operand error\) because the floating-point value was too large to be represented by a 16-bit signed integer. <!--SR:!2025-10-07,14,290!2025-10-08,15,290-->
- programming complexity
  - programming complexity / problems
    - programming complexity / problems / development ::@:: does not meet user requirements, difficult to measure progress, over budget, over time, etc. <!--SR:!2025-10-08,15,290!2025-10-08,15,290-->
      - programming complexity / problems / development / statistics ::@:: \(2012\) For _large_ software projects: deliver less value &gt; over budget &gt; company threatening &gt; over time &gt; etc. <!--SR:!2025-10-10,9,190!2025-10-09,16,290-->
  - programming complexity / mitigations ::@:: There are many desirable _characteristics_ considered part of quality. It is impossible and unnecessary to achieve all of them. <p> Instead, we should under the client's _goals_ and _prioritize_ certain characteristics. This reduces complexity somewhat. <!--SR:!2025-10-05,12,270!2025-10-07,14,290-->
    - programming complexity / mitigations / characteristics ::@:: correct, efficient, evolvable, interoperable, maintainable, portable, productive, reliable, repairable, reusable, robust, timely, usable, verifiable, visible, etc. <!--SR:!2025-10-05,12,270!2025-10-08,15,290-->
- [modular programming](../../../../general/modular%20programming.md) ::@:: It is a programming paradigm that emphasizes organizing the functions of a codebase into independent modules – each providing an aspect of a computer program in its entirety without providing other aspects. <!--SR:!2025-10-08,15,290!2025-10-07,14,290-->
  - modular programming / motivation ::@:: Humans cannot understand things that are too _complex_. Often, we break down a complex systems into _modules_, parts of a system that makes sense to _consider separately_ and interact with other modules. This is known as _divide and conquer_. <!--SR:!2025-10-09,16,290!2025-10-07,14,290-->
  - modular programming / module ::@:: It is a part of a system that can be _considered separately_. To model _interactions_ with other modules, they are limited to _interfaces_, which _abstracts_ and _encapsulates_ a module via _information hiding_. <!--SR:!2025-10-09,16,290!2025-10-07,14,290-->
    - modular programming / module / abstraction ::@:: The internals of a module are hidden away. Interaction is defined via its interface only. The usage of the module by other modules can be understood by looking at its interface only \(ideally\). This reduces complexity of the system. <!--SR:!2025-10-07,14,290!2025-10-08,15,290-->
    - modular programming / module / encapsulation ::@:: When we want to modify a module, we only need to modify the module without changing other modules \(ideally\). The internals of a module can be changed without affecting other modules \(ideally\). This reduces maintenance burden. <!--SR:!2025-10-07,14,290!2025-10-08,15,290-->
  - modular programming / advantages ::@:: bug reduction, _incremental_ development, maintainability, productive teams, reusability <p> This makes software development _more predictable_, leading to better cost and time estimation. <!--SR:!2025-10-08,15,290!2025-10-09,16,290-->
- [engineer](../../../../general/engineer.md) ::@:: It is a practitioner of engineering. <p> They apply ingenuity, mathematics, and scientific knowledge to develop _solutions_ \(e.g. materials, structures, _systems_\) for specific _problems_. They need consider _limitations_ from cost, practicality, regulation, and safety. <!--SR:!2025-10-05,12,270!2025-10-08,15,290-->
  - engineer / vs. scientist ::@:: The former builds things for _quality_ \(e.g. avoiding engineering failures\) while the latter builds things for discovering _new_ things \(e.g. scientific breakthroughs\). <!--SR:!2025-10-09,16,290!2025-10-08,15,290-->
- software engineering
  - software engineering / vs. computer scientist ::@:: The former studies practices and principles for building _quality_ systems while the latter studies _algorithms_ and _foundations_ of computing. <p> The former considers the _context_ to use the appropriate technologies \(e.g. frameworks\) according to their _characteristics_, while the latter focuses on _basic_ technologies, i.e. algorithms and foundations of computing. <!--SR:!2025-10-07,14,290!2025-10-08,15,290-->
  - software engineering / jobs ::@:: Coding or programming is only "programming-in-the-small". Software engineering is "programming-in-the-large", which includes communication, execution, etc. <!--SR:!2025-10-08,15,290!2025-10-08,15,290-->
    - software engineering / jobs / communication ::@:: communication, documentation, teamwork, translating user requirements, etc. <!--SR:!2025-10-07,14,290!2025-10-08,15,290-->
    - software engineering / jobs / execution ::@:: choose design alternatives, modeling \(at different abstraction levels\), use and apply, etc. <!--SR:!2025-10-07,14,290!2025-10-09,16,290-->
  - software engineering / characteristics ::@:: disciplined \(engineering principles\), multi-person, multi-version, problem solving \(solves real user problems\), quality \(e.g. economic, efficient, reliable, etc.\) <!--SR:!2025-10-09,16,290!2025-10-07,14,290-->
  - software engineering / activities ::@:: knowledge acquisition, modeling, problem solving, rationale management, etc. <!--SR:!2025-10-09,16,290!2025-10-08,15,290-->
    - software engineering / activities / modeling ::@:: Model user requirement. Model the system to be built. <!--SR:!2025-10-08,15,290!2025-10-07,14,290-->
    - software engineering / activities / problem solving ::@:: _Systematically_ \(but not _algorithmically_ as there are changes\) find an appropriate solution according to the user requirement. Note that user requirements can _change_ or be clarified over time. <!--SR:!2025-10-09,16,290!2025-10-07,14,290-->
    - software engineering / activities / knowledge acquisition ::@:: Knowledge about the problem needs to be learnt on the go. It may also need to be _unlearnt_ due to changing requirements or misunderstandings. You may even need to _start over_. <!--SR:!2025-10-07,14,290!2025-10-07,14,290-->
    - software engineering / activities / rationale management ::@:: As acquired knowledge, solutions \(new technologies\), user requirements _change_, we need to _revisit_ decisions and their rationale. <!--SR:!2025-10-09,16,290!2025-10-08,15,290-->
- quiz: [quiz 1](questions/quiz%201.md)

## week 1 lecture

- datetime: 2025-09-03T12:30:00+08:00/2025-09-03T14:20:00+08:00, PT1H50M
- topic: logistics; introduction
- COMP 3111H
  - COMP 3111H / logistics
  - COMP 3111H / textbook ::@:: _Object-Oriented Software Engineering: Using UML, Patterns, and Java, 3/E_, B. Bruegge and A.H. Dutoit, Pearson Education, Inc., 2010. <!--SR:!2025-10-07,14,290!2025-10-07,14,290-->
  - COMP 3111H / tools ::@:: Git, GitHub, Java, <https://app.diagrams.net/>; lab notes, web resources <!--SR:!2025-10-08,15,290!2025-10-07,14,290-->
  - COMP 3111H / grading
  - COMP 3111H / objectives ::@:: _disciplined_ approach to software development, theoretical and practical aspects of software engineering <!--SR:!2025-10-07,14,290!2025-10-09,16,290-->
  - COMP 3111H / course intended learning outcomes \(CILO\)
  - COMP 3111H / motivation ::@:: communication, design, leadership, modeling, project management, etc. <!--SR:!2025-10-09,16,290!2025-10-09,16,290-->
  - COMP 3111H / syllabus ::@:: introduction → modeling language → development approaches → development activities → project management <!--SR:!2025-10-09,16,290!2025-10-09,16,290-->
  - COMP 3111H / rules
  - COMP 3111H / project ::2:: specification \(from system requirements\) → implementation and testing
- [§ week 1 pre-lecture](#week%201%20pre%20lecture)
- [questions § week 1 lecture](questions.md#week%201%20lecture)

## week 1 lab

- datetime: 2025-09-04T18:00:00+08:00/2025-09-04T19:50:00+08:00, PT1H50M
- status: unscheduled
- [questions § week 1 lab](questions.md#week%201%20lab)

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

## aftermath

### total

- grades: ?/100
  - statistics: ?
