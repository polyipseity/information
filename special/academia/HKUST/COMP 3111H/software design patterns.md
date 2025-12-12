---
aliases:
  - COMP 3111 software design pattern
  - COMP 3111 software design patterns
  - COMP 3111H software design pattern
  - COMP 3111H software design patterns
  - software design pattern
  - software design patterns
tags:
  - flashcard/active/special/academia/HKUST/COMP_3111H/software_design_patterns
  - language/in/English
---

# software design patterns

- COMP 3111H

---

- see: [general/software design pattern](../../../../general/software%20design%20pattern.md)

{@{A design pattern}@} is {@{a general, reusable solution to a commonly occurring problem in software design}@}. It represents a {@{problem/solution pair}@} within a {@{specific context}@} and describes {@{how and why a particular design approach resolves nonfunctional requirements}@} such as {@{scalability, maintainability, and performance}@}.

{@{Design patterns}@} are {@{not finished implementations}@} that can be {@{directly translated into code}@}. Instead, they serve as {@{templates or blueprints}@}—describing {@{the structure, behavior, and interactions between classes or objects}@}—without specifying {@{the exact types or instances involved}@}. They emphasize {@{relationships such as _inheritance_ (is-a) and _delegation_ (asks-to-do)}@}, enabling developers to {@{build flexible and extensible systems}@}.

{@{Patterns}@} facilitate {@{code reuse}@} by providing {@{proven, tested solutions to recurring design challenges}@}. They help {@{novice developers learn by example}@}, guiding them to {@{adopt expert-level design practices}@}. {@{A pattern catalog}@} compiles {@{useful patterns tailored to a specific domain or context}@}, acting as a {@{reference for effective software design decisions}@}.

## application

To {@{understand and apply design patterns effectively}@}, one must {@{first master foundational knowledge}@}—such as {@{programming languages, algorithms, and data structures}@}—and then {@{grasp core principles}@} like {@{modularization, encapsulation, and object-oriented design}@}. However, {@{true mastery of software design}@} comes from {@{studying real-world designs created by experienced practitioners}@}.

{@{These designs}@} contain {@{recurring patterns}@}—such as those found in {@{chess strategies}@}—that must be {@{observed, understood, memorized, and applied repeatedly}@}. Just as a {@{chess master}@} learns from {@{analyzing past games}@} to {@{recognize and exploit common strategic patterns}@}, a {@{software designer}@} learns from {@{examining well-designed systems}@} to {@{identify and reuse effective design solutions}@}.

There are {@{hundreds of design patterns}@}, each addressing a {@{specific scenario}@}. While {@{no single pattern fits every situation}@}, they {@{collectively form a rich toolkit}@} for solving {@{complex software problems}@} in a {@{structured, maintainable, and scalable way}@}.

## problems with inheritance

The {@{SimUDuck example}@} from {@{Tom Zimmermann of Microsoft Research}@} shows a {@{problem with using inheritance to share behavior}@}. The {@{base class Duck}@} defines {@{`quack()`}@} and {@{`swim()`}@}, and {@{subclasses like `MallardDuck`, `RedheadDuck`, and `RubberDuck`}@} inherit these.

When {@{`fly()`}@} is {@{added to `Duck`}@}, all ducks—including those that {@{shouldn't fly}@}—gain {@{flying ability}@}. This unintended behavior reveals a {@{key flaw}@}: inheritance forces {@{all subclasses to share the same behavior}@}, regardless of their {@{actual capabilities}@}. Further, as {@{new duck types are added}@}, each must {@{override `fly()`}@} to {@{prevent flying}@}, increasing {@{maintenance and risk of inconsistency}@}. This illustrates the {@{problems with rigid inheritance}@}: (annotation: 4 items: {@{capability hiding, new behaviors, rippling effect, runtime modification}@})

- \(annotation: capability hiding\) ::@:: _Hard to know duck behaviors_ – Shared base behavior hides actual subclass capabilities.  
- \(annotation: new behaviors\) ::@:: _Can't easily add new behaviors_ – New actions (like dancing) are hard to support without changing existing classes.
- \(annotation: rippling effect\) ::@:: _Changes affect all ducks_ – Adding or modifying a method to the base class impacts all subclasses, causing ripple effects.  
- \(annotation: runtime modification\) ::@:: _Runtime changes are risky_ – Modifying behavior at runtime may lead to unexpected behavior.  

{@{Rigid inheritance}@} leads to {@{unintended behavior, inconsistency, and high maintenance}@}. It highlights the {@{need for flexible, context-aware design patterns}@}—solutions that {@{emerge from real-world practice}@}, not {@{single problems}@}.

## principles

There are {@{5 key principles in design pattens}@}: {@{program to an interface, not an implementation; identify aspects that vary and separate them from what stays the same}@}; {@{loose coupling between interacting objects; favor composition over inheritance; and the open—closed principle}@}.

{@{The first key principle in design pattern}@} is {@{"_Program to an interface, not an implementation_"}@}. To {@{properly create the interfaces}@}, follow {@{the second principle}@}: {@{_identify aspects that vary and separate them from what stays the same_}@}.  Write {@{code that talks to abstractions (interfaces or abstract super‑types)}@} instead of {@{concrete classes}@}. {@{Abstractions}@} represent {@{aspects that stay the same}@}, while {@{concrete classes}@} represent {@{aspects that vary}@}. This keeps the {@{system flexible, maintainable, and extensible}@}.

In the {@{SimUDuck example}@}, a duck's behaviors—{@{flying and quacking}@}—are {@{not hard‑coded}@} in the {@{base `Duck` class}@}. Instead: (annotation: 3 items: {@{interfaces, concrete classes, composition}@})

- Each behavior ::@:: is an interface (`FlyBehaviour`, `QuackBehaviour`) that declares methods such as `fly()` or `quack()`.
- Concrete classes (`FlyWithWings`, `FlyNoWay`, `QuackSqueak`, `MuteQuack`) ::@:: implement those behavior interfaces (`FlyBehaviour`, `QuackBehaviour`).
- Ducks compose ::@:: these behaviors, so the same behavior can be shared by many ducks without duplication.

With {@{this implementation of SimUDuck}@}, there are {@{4 major advantages}@}: (annotation: 4 items: {@{greater flexibility, improved maintainability, reduced code duplication, runtime polymorphism}@})

- _Greater flexibility_ ::@:: – New duck types or new behaviors can be added without touching existing code.
- _Improved maintainability_ ::@:: – Changing how a duck flies or quacks only requires editing one implementation class.  
- _Reduced code duplication_ ::@:: – Behaviors \(concrete classes\) are reused across different duck types.  
- _Runtime polymorphism_ ::@:: – Any object, not just ducks, that implements `FlyBehaviour`/`QuackBehaviour`, such as a `RobotDuck` or a `Penguin`, can be treated uniformly.

The above actually illustrates {@{a classic design pattern}@} known as the {@{_strategy pattern_}@}; see below. It follows {@{the third design principle}@}: of {@{_favouring composition (has-a) over inheritance (is-a)_}@}. Rather than having {@{each duck subclass inherit different behaviors}@} (which would require a {@{large number of subclasses}@}), {@{the duck class}@} simply holds {@{references to behavior objects}@}.

The {@{fourth design principle}@} advocates for {@{_loose coupling between interacting objects_}@}. In a system, {@{loose coupling minimizes interdependencies between objects}@}, enabling {@{better scalability, maintainability, and performance}@}. This {@{fourth principle}@} is illustrated by the {@{_observer pattern_}@}. The {@{Observer pattern}@} exemplifies this principle by allowing the {@{subject to manage state changes and notify observers automatically}@}—without needing to {@{communicate directly with every observer}@}. This separation allows {@{components to change at runtime without needing to know each other}@}. Observers can {@{respond to data changes independently}@}, and new observers can be {@{added or removed without modifying the system}@}. {@{This dynamic model}@} supports {@{scalable systems}@} where {@{views can respond to changes in data}@}—such as in a {@{spreadsheet or financial report}@}.

The {@{fifth design principle}@} advocates that {@{software entities (classes, modules, functions)}@} should be {@{_open_ for extension but _closed_ for modification}@}. This is known as {@{the _open—closed principle_}@}.

## categories

{@{Design patterns}@} are typically {@{categorized into four main groups}@} based on their {@{purpose and the aspects of software design they address}@}: (annotation: 4 items: {@{creational, structural, behavioral, concurrency}@})

- {@{_Creational patterns_}@}: Deal with the {@{instantiation of objects}@} and the {@{mechanisms for creating and configuring them}@}. These patterns {@{decouple the client code from the specifics of object creation}@}, enabling {@{more flexible and maintainable systems}@}. <p> Examples include {@{the Factory, Abstract Factory, Singleton, and Prototype patterns}@}. They are {@{especially useful}@} when {@{the object creation process is complex or depends on context}@}.

- {@{_Structural patterns_}@}: Focus on {@{how classes and objects are composed to form larger structures}@}. These patterns define {@{how classes and objects are combined to create more complex structures}@}, promoting {@{loose coupling and reusability}@}. <p> Examples include {@{the Adapter, Decorator, Facade, Proxy, and Composite patterns}@}. They help manage {@{relationships between objects and provide interfaces that simplify interactions}@}.

- {@{_Behavioral patterns_}@}: Address {@{dynamic interactions among classes and objects}@}. These patterns define {@{how responsibilities are assigned, how objects communicate, and how tasks are distributed among components}@}. They emphasize the {@{flow of control and coordination between objects}@}. <p> Examples include {@{the Observer, Command, Strategy}@}, {@{Mediator, Chain of Responsibility, and Visitor patterns}@}. {@{Behavioral patterns}@} are essential for modeling {@{interactions such as event handling, request processing, and policy-based decision-making}@}.

- {@{_Concurrency patterns_}@}: Specifically address {@{challenges in multi-threaded programming}@}. These patterns manage the {@{interactions and coordination of multiple concurrent objects or threads}@}, ensuring {@{safe and efficient execution in parallel environments}@}. <p> They help avoid {@{race conditions, ensure synchronization, and manage shared resources}@}. While {@{less commonly used in general software design}@}, they are {@{critical in real-time, high-performance, or distributed systems}@}. <p> Examples include {@{the Active Object, Balking, Monitor, Reactor}@}, {@{Read—Write Lock, Scheduler, Thread Pool patterns}@}.

{@{The categorization of design patterns}@} reflects {@{a structured approach to software design}@}, organizing {@{solutions by the type of problem they solve}@}. {@{This classification}@} helps {@{developers identify the appropriate pattern for a given scenario}@} and {@{understand how different patterns relate to one another}@}.

## documentation

{@{Design patterns}@} are not {@{language-specific}@} and are typically {@{described in a way that is independent of implementation details}@}. A well-designed {@{pattern description}@} includes the following {@{key components}@}: (annotation: 9 items: {@{name and intent, problem, context}@}, {@{concerns, solution, consequences}@}, {@{implementation guidelines, sample code, known uses and related patterns}@})

1. _Name and intent_ ::@:: – A concise explanation of what the pattern does and its primary purpose.
2. _Problem_ ::@:: – The specific challenge or difficulty being addressed in a real-world or abstract scenario.
3. _Context_ ::@:: – The general situation or environment in which the pattern applies.
4. _Concerns_ ::@:: – Issues to consider while solving the problem.
5. _Solution_ ::@:: – An abstract description of the structure, collaboration, and behavior of the pattern.
6. _Consequences_ ::@:: – Both positive and negative effects of using the pattern (e.g., benefits like flexibility, drawbacks like complexity or performance cost).
7. _Implementation guidelines_ ::@:: – Practical advice on how to apply the pattern in code, often including recommendations for when and how to use it.
8. _Sample code_ ::@:: – Illustrative code snippets (though not always included in formal documentation).
9. _Known uses and related patterns_ ::@:: – Real-world applications and connections to other patterns that may be used in tandem.

{@{Patterns}@} are most effective when {@{studied in context and applied through practice}@}. Just as in {@{chess}@}, where {@{mastery comes from analyzing master-level games}@}, {@{software design proficiency}@} grows through {@{repeated exposure to real-world designs that embody these patterns}@}. {@{Understanding the underlying principles and common structures}@} allows {@{developers to recognize, adapt, and reuse patterns effectively}@} across {@{diverse systems}@}.

{@{The seminal work _Elements of Reusable Object-Oriented Software_}@} by {@{Gamma, Helm, Johnson, and Vlissides}@} introduced {@{many of the most widely recognized design patterns}@} and {@{remains a foundational reference in software engineering}@}. {@{Patterns such as the Observer, Strategy, and Singleton}@} have become {@{standard tools in object-oriented design}@} and are {@{frequently cited in modern software architecture}@}.

## strategy pattern

{@{The _strategy pattern_}@} is {@{a _behavioral_ design pattern}@} that allows an object to {@{vary its behavior at runtime}@} by {@{encapsulating different algorithms or behaviors within separate objects}@}. Instead of {@{hardcoding behavior into a class}@}, {@{the behavior}@} is {@{delegated to a set of interchangeable, reusable components}@}—each {@{implementing a common interface}@}.

In {@{the Simuduck example}@}, {@{the `Duck` class}@} maintains {@{references to two behavior interfaces}@}: {@{`FlyBehaviour` and `QuackBehaviour`}@}. {@{These interfaces}@} define {@{operations such as `fly()` and `quack()`}@}, and {@{their implementations (e.g., `FlyWithWings`, `FlyNoWay`, `Quack`, `Squeak`, `MuteQuack`)}@} are {@{dynamically assigned to individual duck subclasses}@}. {@{The `Duck` class itself}@} does not {@{implement these behaviors directly}@}—it {@{delegates them to the behavior objects it holds}@}. This allows {@{new behaviors to be added without modifying the existing class structure}@}, promoting {@{loose coupling and easier maintenance}@}.

{@{The key components of the Strategy pattern}@} are: (annotations: 3 items: {@{strategy interface, concrete strategies, context class}@})

- _Strategy Interface_: ::@:: A common interface that defines the operations (e.g., `fly()`, `quack()`) that all supported behaviors must implement. This interface is used by the client to invoke the behavior without knowing which specific implementation is active.
- _Concrete Strategies_: ::@:: Classes that implement the strategy interface. Each provides a specific behavior (e.g., a mallard duck flies using `FlyWithWings`, while a rubber duck cannot fly and uses `FlyNoWay`).
- _Context Class_: ::@:: The class that uses the strategy (e.g., `Duck`). It maintains a reference to a strategy object and delegates behavior to it via method calls such as `performFly()` or `performQuack()`.

{@{Behavior}@} can be {@{set dynamically at runtime}@} through {@{operations like `setFlyBehaviour(FlyBehaviour fb)` or `setQuackBehaviour(QuackBehaviour qb)`}@}. {@{These methods}@} allow {@{the duck to change its behavior on-the-fly}@}—without needing to {@{modify the class structure}@}.

{@{This pattern}@} is {@{widely applicable to solving recurring software problems}@}—such as {@{maintaining behavior in a system that varies in scale or performance}@}.

{@{The core idea behind the Strategy pattern}@} is {@{not a finished implementation}@}, but {@{a reusable solution to a common problem}@}—where {@{behavior is encapsulated, delegated, and changed at runtime}@}. {@{This flexibility}@} enables developers to build {@{systems that are scalable, maintainable, and responsive to nonfunctional requirements}@}.

## observer pattern

{@{The _Observer pattern_}@} is {@{a _behavioral_ design pattern}@} that defines {@{a one-to-many dependency between objects}@} so that when {@{one object's state changes}@}, {@{all its dependent objects}@} are {@{automatically notified and updated}@}. {@{This enables loose coupling}@} between {@{the object that holds state (the _subject_)}@} and {@{the objects that react to changes (the _observers_)}@}.

In essence, {@{the Observer pattern}@} establishes {@{a dynamic relationship}@} where {@{observers can register themselves with a subject}@} to {@{receive updates whenever the subject's state changes}@}. When {@{the subject changes}@}, it {@{broadcasts a notification to all registered observers}@}, who then {@{retrieve the relevant portion of the updated state from the subject}@}. {@{This mechanism}@} allows for {@{decoupled, scalable, and flexible systems}@} where {@{components can respond to data changes without being tightly bound to one another}@}. {@{The system}@} does not {@{require direct communication}@} between {@{the subject and any observer}@}, eliminating the need for {@{a concrete implementation to manage all changes}@}.

{@{The key components of the observer pattern}@} are: (annotations: 4 items: {@{subject, observer, concrete subject, concrete observers}@})

- _Subject_: ::@:: An _interface_ (`<<interface>>`) representing an object that maintains a list of observers and provides methods to register, remove, and notify them of state changes. It maintains a list of observers (dependency arrow from _Subject_ to _Observer_ named `observers`).
- _Observer_: ::@:: A general _interface_ (`<<interface>>`) or class that defines a method (typically `update()`) to be called when the subject's state changes. Observers implement this interface and react to updates based on their own logic.
- _Concrete Subject_: ::@:: A class that implements the subject interface and manages its state and list of observers. It may provide operations to get or set its state, and trigger notifications when the state changes.
- _Concrete Observers_: ::@:: Classes that implement the observer interface and respond to state changes by querying the subject for the subset of state they are responsible for. It may know the _Subject_ (dependency arrow from _Concrete Observer_ to _Concrete Subject_ named `subject`),

{@{An issue with the observer pattern}@} is that {@{an event-notification protocol is needed}@} to establish {@{how and when the subject announces events}@}. {@{The protocol}@} must define {@{which events the subject should announce}@}—such as {@{a change in data or a financial metric}@}—and whether {@{every event should be broadcast to every observer}@}. {@{It should also specify}@} if subjects can {@{define different kinds of events}@} and enable observers {@{to subscribe selectively}@}, based on {@{the subset of state they are responsible for monitoring}@}. Lastly, in {@{concurrent environments}@}, the pattern needs to take care of {@{thread safety and synchronization}@}.

## mediator pattern

{@{The _Mediator_ pattern}@} is {@{a _behavioral_ design pattern}@} that {@{centralizes communication between many objects}@}, reducing {@{tight coupling}@}. In {@{Bob's House of the Future}@} each {@{appliance (alarm, coffee pot, sprinkler, calendar)}@} runs its own {@{logic but talks only to a central Mediator}@} instead of {@{directly to one another}@}.

There are {@{4 key components in the mediator pattern}@}: (annotation: 4 items: {@{mediator, colleague, concrete mediator, concrete colleague}@})

- `Mediator` ::@:: – an _interface_ (`<<interface>>`) that defines how colleagues talk and knows all of them. It receives events and coordinates actions.  
- `Colleague` ::@:: – an _interface_ (`<<interface>>`) representing any component that uses the mediator for communication; it only knows `Mediator` doesn't know other colleagues.
- `ConcreteMediator` ::@:: – implements `Mediator`, holds references to `ConcreteColleague`s, and contains the coordination logic.  
- `ConcreteColleague` ::@:: – implements `Colleague`, talks only to the mediator via its interface `Mediator`.

{@{A component (e.g., calendar)}@} emits {@{an event (`weekend`, `trashDay`)}@}. {@{The mediator}@} receives {@{the event}@}, decides {@{what should happen}@}, and {@{calls methods on the relevant colleagues (e.g., reset alarm, start sprinkler)}@}. {@{Example}@}: when {@{the alarm rings}@}, the mediator {@{checks if it's a weekend or trash day}@} and then {@{tells the coffee pot or shower to act}@}.

There are {@{4 major advantages to the mediator pattern}@}: (annotation: 4 items: {@{centralized control, decoupled colleagues, reduced subclassing, simplified protocols}@})

- _Decoupled colleagues_ ::@:: – each class is independent; easier to develop, test, reuse.  
- _Centralized control_ ::@:: – logic lives in one place, simplifying debugging and changes.  
- _Simplified protocols_ ::@:: – only mediator‑to‑colleague links, not many direct connections.  
- _Reduced subclassing_ ::@:: – extending only the mediator suffices to extend the system logic.

There are {@{2 major disadvantages to the mediator pattern}@}: (annotation: 2 items: {@{mediator can grow large, single point of failure}@})

- _Mediator can grow large_ ::@:: – with many colleagues/events it may become complex and hard to maintain.  
- _Single point of failure_ ::@:: – if the mediator fails, all coordinated components are affected.

{@{The Mediator pattern}@} shines when {@{many interdependent parts exist (UI widgets, smart‑home devices)}@}. It {@{keeps systems}@} {@{loosely coupled and more modular}@}.

## proxy pattern

{@{A _proxy_}@} is {@{a _structural_ design pattern}@} that gives {@{a surrogate object control over access to another object}@}, often delaying {@{the creation of an expensive resource until it is actually needed}@}.

The pattern may be used in {@{the following illustrative example of a document editor}@}: {@{Objects like large images or remote services}@} are {@{costly to create}@}. {@{Opening a document}@} should be {@{fast}@}; {@{creating every embedded image at once}@} would {@{hurt performance}@}. {@{Not all objects}@} are {@{visible simultaneously}@}.

{@{The solution}@} is to use {@{a virtual proxy}@}. {@{The client}@} uses {@{the same interface as the real object (`Subject`)}@}. {@{A lightweight `Proxy`}@} holds {@{a reference to the real subject (`RealSubject`)}@}, initially {@{null}@}. On {@{first request (e.g., `draw()`)}@}, the proxy {@{creates the real object, stores it, and forwards the call}@}. {@{Subsequent calls}@} use {@{the already‑created instance}@}.

There are {@{3 key components to the proxy pattern}@}: (annotations: 3 items: {@{`Subject`, `RealSubject`, `Proxy`}@})

- `Subject` ::@:: – interface/abstract class defining operations for both real and proxy objects.
- `RealSubject` :;@:: – implements full functionality, often expensive to instantiate.
- `Proxy` ::@:: – implements `Subject`, holds a reference to `RealSubject`. It may create, cache, or restrict access to the real object.

{@{Other common use cases for the proxy pattern}@} include {@{_virtual proxies_ that lazily initialize heavy objects}@}, {@{_protection proxies_ that enforce security checks before delegating requests}@}, {@{_remote proxies_ that represent objects located in another address space}@}, and {@{_caching proxies_ that store results from expensive operations for reuse}@}.

## bridge pattern

{@{The _bridge_}@} is {@{a _structural_ design pattern}@} that {@{separates an abstraction from its implementation}@} so that the two can {@{vary independently}@}. It solves {@{the tight coupling}@} that arises when {@{a class hierarchy of abstractions}@} is {@{directly tied to a parallel hierarchy of concrete implementations}@}.

{@{The problem to tackle}@}: {@{An abstraction (e.g., `Window`)}@} may have {@{many concrete forms (`MSWindow`, `MacWindow`)}@}. Using {@{inheritance to connect them}@} forces {@{every subclass of the abstraction}@} to {@{inherit from a specific implementation type}@}. This makes it {@{hard to change, extend, or reuse either side without touching the other}@}.

{@{The solution}@} is to {@{define an abstract base for the abstraction (`Window`)}@} that contains {@{a reference to an object implementing the `WindowImp` interface}@}. This {@{creates separate hierarchies}@}, one for {@{abstractions}@}: {@{`Window`, `IconWindow`, `ApplicationWindow`}@}, and the other for {@{implementations}@}: {@{`MSWindowImp`, `MacWindowImp`}@}. {@{The abstraction delegates all work}@} to {@{its implementation (`drawRect()`, `drawText()`, etc.)}@}, allowing {@{each side to evolve independently}@}.

There are {@{4 key components}@}: (annotation: 4 items: {@{abstraction, refined abstraction, implementor, concrete implementor}@})

- _Abstraction_ (`Window`) ::@:: Declares an interface for high‑level operations and holds a reference to the implementation.
- _Refined Abstraction_ (e.g., `IconWindow`, `ApplicationWindow`) ::@:: Extends or specializes the abstraction without changing the implementation contract.
- _Implementor_ (`WindowImp` interface) ::@:: Declares the low‑level interface that concrete implementations must provide.
- _Concrete Implementor_ (`MSWindowImp`, `MacWindowImp`) ::@:: Implements the low‑level operations for a specific platform or environment.

{@{The bridge}@} allows clients to work with {@{any combination of abstraction and implementation at runtime}@}, enabling {@{dynamic configuration}@} and {@{easy addition of new platforms}@}.

It may be used when {@{both an abstraction and its implementation need independent extension}@}. It {@{avoids a combinatorial explosion of subclasses}@} (e.g., {@{every UI widget on every OS}@}). It may also be used when {@{the abstraction should be able to change at run time by swapping implementations}@}.

{@{The bridge pattern}@} is a classic example of {@{_composition over inheritance_}@}: the abstraction {@{_contains_ an implementor}@} rather than {@{_being_ one}@}. This design keeps systems {@{modular, testable, and easier to maintain as requirements evolve}@}.

## singleton pattern

{@{A _singleton_}@} is {@{a _creational_ design pattern}@} that {@{guarantees a class has _exactly one_ instance}@} and {@{provides a global point of access to it}@}. {@{Typical use cases}@} include {@{thread pools, caches, dialog boxes}@}, {@{logging facilities, system-wide configuration managers (e.g., `System.out`)}@}, or {@{any object whose multiple instances would be redundant or harmful}@}.

When {@{an object represents a shared resource or service}@}, creating {@{multiple instances}@} can lead to {@{inconsistent state, wasted memory, or conflicting operations}@}. {@{The singleton pattern}@} solves this by enforcing {@{a single instance}@}, preventing {@{other parts of the program from constructing additional objects}@}, and exposing {@{that sole instance in a convenient way}@}. In {@{concurrent environments}@}, the pattern needs to take care of {@{thread safety and synchronization}@}.

There are {@{3 core components to the singleton pattern}@}: (annotation: 3 items: {@{instance storage, controlled creation, access method}@})

- _Instance storage_ ::@:: A private static field, often called `uniqueInstance`, holds the sole instance.
- _Controlled creation_ ::@:: The constructor is made private (or protected) so external code cannot instantiate the class directly.
- _Access method_ ::@:: A public static method, conventionally named `getInstance()`, returns the stored instance. If it hasn't been created yet, the method creates it (`lazy instantiation`). <p> `getInstance()` checks if `uniqueInstance == null`. If so, it constructs a new object and assigns it to `uniqueInstance`; otherwise it simply returns the existing reference. This defers object creation until first use, saving resources when the singleton is never needed.

{@{The singleton pattern}@} provides a {@{controlled, globally accessible instance}@} while preventing {@{accidental duplication}@}. It's {@{ideal for shared resources}@} that must {@{remain unique across an application}@}.

## multiton pattern

{@{A _multiton_}@} generalises {@{a singleton}@} by keeping {@{a controlled set of instances keyed by a unique identifier}@} (e.g., {@{an enum or string}@}). It stores {@{objects in a thread‑safe map}@} and lazily {@{creates one instance per key through `getInstance(key)`}@}. This pattern is ideal for {@{shared but differentiated resources}@}—like {@{per‑URL connection pools or module loggers}@}—while still {@{preventing accidental duplication}@}.

## factory pattern

{@{The factory pattern}@} is {@{a _creational_ design pattern}@} that {@{provides a single place where objects of varying concrete types are created at run time}@}, instead of {@{scattering `new` calls throughout the codebase}@}.

Typically, a method that creates {@{different subclasses directly with `new`}@} is {@{_closed_ for modification}@}, but {@{_not_ open for extension}@}. violating {@{the _open‑closed principle_}@}. Adding a new type {@{forces changes to every place where the factory logic lives}@}.

{@{The solution using the factory pattern}@} is: First, extract {@{all creation logic into one class (`SimplePizzaFactory`)}@}. Then, let {@{clients ask this factory for a product by passing a type identifier}@}. The factory returns {@{an instance of the requested concrete subclass}@}, leaving the rest of the system unchanged. Finally, refactor {@{users to use the factory}@}.

In summary, {@{_simple factory_}@} centralizes {@{object creation}@}, making it {@{easier to add new concrete types without touching client code}@}. It exemplifies {@{the _open‑closed principle_}@} by isolating {@{the varying part (which subclass is created)}@} from {@{the invariant behavior (how a pizza is made)}@}. {@{The refactoring shown}@} replaces {@{scattered `new` calls}@} with {@{a single factory method}@}, keeping the rest of the system {@{unchanged and more maintainable}@}.

## usage

- {@{_Recurring problems with variations_}@} – Patterns are most useful when {@{a problem appears in multiple contexts, each with its own nuances}@}. If {@{the issue arises only once}@}, {@{pattern reuse provides little benefit}@}.  
- {@{_Multi‑step solutions_}@} – {@{Some problems}@} require {@{several coordinated steps (e.g., construction, initialization, and configuration)}@}. {@{Simple linear procedures}@} may not {@{justify a full pattern}@}; {@{patterns are most valuable}@} when the solution {@{naturally decomposes into distinct stages}@}.  
- {@{_Focus on existence over derivation_}@} – When the designer is more interested in {@{_having_ a working approach}@} than in {@{deriving it from first principles}@}, a pattern offers {@{a ready‑made blueprint}@}. For those who want to {@{understand every detail}@}, {@{patterns can feel opaque}@}, though they can serve as {@{temporary bridges while deeper learning occurs}@}.

For example, {@{the _observer_ pattern}@} is often cited for {@{event‑driven systems}@}; a developer may adopt it quickly without {@{fully deriving the observer–observable relationship from scratch}@}.

## advantages

- {@{_Reusable architectural ideas_}@} – {@{Patterns capture proven solutions}@} that can be {@{applied across projects}@}, enabling {@{large‑scale reuse of software designs}@}.  
- {@{_Improved documentation and comprehension_}@} – By {@{naming common structures (e.g., _Factory_, _Decorator_)}@}, {@{patterns provide a shared vocabulary}@} that makes {@{system architecture easier to explain and reason about}@}.  
- {@{_Expert knowledge transfer_}@} – {@{Patterns codify design trade‑offs}@} decided by {@{experienced practitioners}@}, making that {@{expertise accessible to teams}@} that might otherwise {@{reinvent the wheel}@}.  
- {@{_Facilitates transition to object‑oriented paradigms_}@} – {@{Many classic patterns}@} embody {@{core OO concepts (encapsulation, polymorphism)}@}, easing {@{adoption of OO techniques}@} in {@{legacy or procedural codebases}@}.

## disadvantages

- {@{_No direct code reuse_}@} – {@{Patterns describe _how_ components should interact}@}, not {@{the actual code}@}; developers still need to {@{implement the specific classes and interfaces}@}.  
- {@{_Can appear deceptively simple_}@} – {@{The succinct notation}@} can {@{hide underlying complexity}@}, leading {@{some teams to underestimate effort}@} or {@{over‑apply a pattern where it's unnecessary}@}.  
- {@{_Risk of overload_}@} – {@{An excessive focus on patterns}@} may {@{clutter design discussions}@}, making the {@{architecture harder to grasp}@}.  
- {@{_Validation relies on experience, not testing_}@} – {@{Patterns are historically validated}@} by {@{practice and peer discussion}@}; they {@{lack formal test suites}@} that guarantee {@{correctness in every context}@}.  
- {@{_Human‑intensive integration_}@} – {@{Incorporating a pattern into a development process}@} requires {@{careful communication, training, and alignment}@} among {@{team members}@}.  

For example, {@{overusing the _decorator_ pattern}@} for {@{trivial configuration}@} can {@{inflate class hierarchies}@} without {@{tangible benefit}@}, illustrating the {@{overload risk}@}.

## anti-patterns

- see: [general/anti-pattern](../../../../general/anti-pattern.md)

{@{An __anti‑pattern__}@} is {@{a commonly used solution}@} that {@{appears attractive at first}@} but {@{ultimately proves harmful in the long run}@}. {@{Typical anti‑pattern documentation}@} explains: why {@{the approach seems appealing}@}; what {@{problems it causes over time}@} (e.g., {@{maintenance burden, poor scalability}@}); and {@{alternative, healthier solutions}@} that should be {@{considered instead}@}.

{@{Anti‑patterns}@} are found {@{throughout software projects}@}—from {@{design decisions}@} to {@{organizational practices}@}—and can {@{serve as useful warnings}@} for {@{practitioners}@}.

{@{Software anti‑patterns}@} can be {@{grouped by the context in which they arise}@}. {@{Several types are often cited}@}: {@{_development_, _object‑oriented_, _organizational_, _domain-specific_}@}, etc. {@{These categories}@} are {@{not mutually exclusive}@}; {@{a single anti‑pattern}@} may {@{span several domains}@}.

- _Spaghetti Code_ ::@:: – tangled, unstructured logic with no clear hierarchy.  
- _Stovepipe System_ ::@;: – siloed subsystems that cannot communicate.  
- _Analysis Paralysis_ ::@:: – excessive deliberation that stalls progress.  
- _Design by Committee_ ::@:: – conflicting requirements from too many stakeholders.  
- _God Class_ ::@:: – a single class that knows or does too much.  
- _Mythical Man-Month_ ::@:: – underestimating effort and over‑optimistic schedules.  
- _Death March Project_ ::@:: – projects with unrealistic deadlines and high risk of failure.

{@{Anti‑patterns}@} are {@{not merely "bad habits"}@}; they {@{expose hidden risks}@} that can {@{cripple a project or organization}@}. {@{Recognizing an anti‑pattern early}@} lets {@{teams pivot to healthier alternatives}@}—such as {@{modular design, clear ownership, or realistic planning}@}. {@{Documenting both the problem and viable solutions}@} turns {@{each anti‑pattern}@} into {@{a learning opportunity for future projects}@}.

### spaghetti code

{@{_Spaghetti code_}@} is {@{a tangled, undocumented implementation}@} that becomes {@{impossible to extend or modify}@}. It often evolves {@{from a quick prototype}@} written by a {@{single "lone ranger" developer}@}, leaving {@{little documentation}@} and forcing {@{about half of maintenance effort into rediscovering existing logic}@}. {@{Developers hesitate to touch it}@} because they {@{fear breaking something}@}; {@{rewriting}@} is therefore seen as {@{easier than refactoring}@}.

{@{Object‑oriented spaghetti code}@} takes {@{the same form}@} but with {@{many methods that lack parameters}@} and {@{rely on global state}@}. {@{Suspicious class variables and intertwined relationships between objects}@} undermine {@{inheritance and polymorphism}@}, so {@{the OO advantages are lost}@} and the system behaves {@{like a monolith}@}.

### god class

{@{The _blob_ or _god class_ anti‑pattern}@} occurs when {@{one massive class contains too many attributes or operations}@}, violating {@{cohesion and single responsibility}@}. {@{Every change risks new defects}@} because {@{responsibilities are mixed}@}, making the code {@{difficult to understand, reuse, or test}@}. The class also bloats {@{memory usage and slows loading}@}.

{@{Typical causes}@} include {@{poorly specified requirements}@}, lack of {@{a clear object‑oriented architecture}@}, and failure to {@{enforce architectural boundaries}@}. {@{The consequence}@} is {@{loss of OO benefits and unnecessary complexity}@}.

{@{The remedy for both anti‑patterns}@} is {@{refactoring}@}: break {@{monolithic structures into smaller modules}@} or split {@{responsibilities across cohesive classes}@}, and enforce {@{a disciplined architecture}@} to keep {@{the code maintainable}@}.
