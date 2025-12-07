---
aliases:
  - COMP 3111 UML
  - COMP 3111 unified modeling language
  - COMP 3111H UML
  - COMP 3111H unified modeling language
  - UML
  - unified modeling language
tags:
  - flashcard/active/special/academia/HKUST/COMP_3111H/UML
  - language/in/English
---

# unified modeling language

- COMP 3111H

---

- see: [general/Unified Modeling Language](../../../../general/Unified%20Modeling%20Language.md), [UML](UML.md)

{@{__Unified Modeling Language__ \(__UML__\)}@} is {@{a general-purpose, object-oriented, visual modeling language}@} that provides {@{a way to visualize the architecture and design of a system}@}; like {@{a blueprint}@}.

## classes

{@{A _class_}@} represents {@{a _type_ of object in the application domain}@}. _Instances_ of a class have {@{_common_ states \(attributes\), behaviors \(operations\), relations with other objects, and semantics}@}, which are {@{_classified_ by the class \(a _classifier_\)}@}. There can be {@{many instances of a class}@}. It can be considered as {@{a "factory" for creating new instances of it}@}.

A good class should {@{capture exactly one abstract object in the application domain}@}. It should have {@{one major theme \(not too general, no mixing of concepts\)}@}. {@{Abstract objects _outside_ the application domain}@}, e.g. {@{physical objects not represented by the digital system}@}, should {@{not be modeled at all}@}! An example is {@{physical passbooks issued by a bank}@}. They are {@{physical objects not represented by the bank's digital system}@}. They should be {@{excluded if you are only designing the digital system}@}.

A class is drawn by {@{a rectangle box with 3 sections \(from top to bottom\)}@}: {@{class name, attributes, and operations}@}.

{@{The _name_}@} of a class should be {@{_unique_ \(including classes and associations\)}@}, and uses {@{vocabularies according to the application domain}@}.

### why classes

There are {@{many objects in the application domain}@}. Classes allow us to {@{_abstract_ a collection of objects}@} that {@{_share semantics_}@}. This reduce {@{development _complexity_}@} by allowing {@{better understanding and specification}@}. It is {@{an important _design decision_}@} that helps {@{promote _modular development_}@}. Note as {@{a design decision}@}, there is not {@{the single "correct" way to model a system}@}.

{@{Better _understanding_}@} comes from {@{reduced complexity}@}, as {@{collections of many objects}@} become {@{a few classes}@}. We only need to understand {@{the class instead of the collection of objects \(instances\)}@}.

{@{Better _specification_}@} comes from {@{UML requiring details of the classes}@}. These details provide {@{a _common_ place to define and store _common_ definitions exactly once}@}.

## attributes

{@{An _attribute_}@} represents {@{a _data value_ held by the class}@}. It has {@{6 major properties \(and possibly more\)}@}: {@{name, type, visibility}@}, {@{initial value, multiplicity, and mutability}@}. It is {@{a _classifier_}@} for {@{_values_}@}. For {@{modeling using the simplest possible model \(__this course__: may be used in this course\)}@}, {@{_name_ and _type_}@} should {@{always be specified}@}.

{@{The _name_}@} of an attribute describes {@{the _semantics_ for the data value}@}. It should be {@{_unique_ \(including attributes and operations\) in a class}@}. For {@{modeling using the simplest possible model \(__this course__: may be used in this course\)}@}, it should {@{always be specified}@}.

{@{The _type_}@} of an attribute describes {@{the _domain of values_ for the data value}@}, e.g. {@{integer, string, money, etc.}@} For {@{modeling using the simplest possible model \(__this course__: may be used in this course\)}@}, it should {@{always be specified}@}.

{@{The _visibility_}@} of an attribute describe {@{who can _access_ the data value}@}. In {@{Java}@}, there are {@{4 visibilities \(in order of decreasing visibility\)}@}: {@{public \(all classes\), protected \(additionally, subclasses\), package-local \(additionally, classes in the same package\), and private \(the class itself\)}@}. They are respectively represented by the symbols {@{`+`, `#`, `~`, and `-`}@}.

{@{The _initial value_}@} of an attribute describe {@{the initial value for the data value if _unspecified_}@}. It is {@{_optional_}@}, and by default {@{requires the data value to be _specified_ since there is no initial value}@}.

{@{The _multiplicity_}@} of an attribute describe {@{how many _simultaneous values_ the data value can take}@}. It is {@{_optional_}@}, and by default {@{is 1}@}. Its syntax is {@{the same as that for association multiplicity}@} but {@{inside square brackets `[]`}@}, i.e. {@{`[min..max]`}@}, e.g. {@{`accounts: Account [0..10]`}@}. \(__this course__: Tested in the midterm examination.\)

{@{The _mutability_ \(_changeability_\)}@} of attribute describe {@{if the data value can be changed}@}. It can be {@{writable \(_unspecified_\) or read-only \(`readOnly`\)}@}. By default, it is {@{writable as it is unspecified}@}. Its syntax is {@{writing the property inside curly brackets `{}`}@}, i.e. {@{`{readOnly}`}@}, e.g. {@{`account: Account {readonly}`}@}.

{@{The syntax}@} to {@{describe an attribute}@} is {@{`<visibility> <name> : <type> <multiplicity> <mutability> = <initial value>`}@}, e.g. {@{`+ accounts: Account [0..10] {readOnly} = []`}@}.

## operations

{@{An _operation_}@} represents {@{a _function_ or _transformation_ that can be applied to or by instances of the class}@}. It has {@{4 major properties \(and possibly more\)}@}: {@{operation name, parameter names, result type, and visibility}@}. {@{The first 3 properties}@} is known as {@{the _operation signature_}@}. It is {@{a _classifier_}@} for {@{_methods_}@}. For {@{modeling using the simplest possible model \(__this course__: may be used in this course\)}@}, the operation signature should {@{always be specified}@}.

{@{An instance of an operation}@} is called {@{a _method_}@}. This matters because there {@{can be several methods implementing the same operation \(a _polymorphic_ operation\)}@}. One way to do this is via {@{_overriding_ to achieve _polymorphism_}@}.

{@{The _operation name_}@} of an operation describes {@{the _semantics_ of the operation}@}. It should be {@{_unique_ \(including attributes and operations\) in a class}@}. For {@{modeling using the simplest possible model \(__this course__: may be used in this course\)}@}, it should {@{always be specified}@}.

{@{The _parameter names_}@} of an operation describe {@{the _semantics_ of the _arguments_ \(inputs\) to the operation}@}. They should be {@{_unique_ in an operation}@}. For {@{modeling using the simplest possible model \(__this course__: may be used in this course\)}@}, it should {@{always be specified}@}. It can be {@{empty for no arguments}@}.

{@{The _return type_}@} of an operation describe {@{the _domain of values_ the operation can return}@}, e.g. {@{integer, string, money, etc.}@} If {@{no return value \(`void`\)}@}, {@{omit it}@}. For {@{modeling using the simplest possible model \(__this course__: may be used in this course\)}@}, it should {@{always be specified \(because omitting it implies no return value \(`void`\)\)}@}.

{@{The _visibility_}@} of an operation describe {@{who can _use_ the operation}@}. In {@{Java}@}, there are {@{4 visibilities \(in order of decreasing visibility\)}@}: {@{public \(all classes\), protected \(additionally, subclasses\), package-local \(additionally, classes in the same package\), and private \(the class itself\)}@}. They are respectively represented by the symbols {@{`+`, `#`, `~`, and `-`}@}.

{@{The syntax}@} to {@{describe an operation}@} is {@{`<visibility> <name>(<parm name 1>, ..., <parm name N>) : <return type>`}@}.

## associations

{@{An _association_ \(a _classifier_\)}@} _classifies_ {@{a collection of links with _common semantics_}@}. {@{A _link_}@} is {@{a _relation_ between objects \(of different classes or the same class\)}@}, and is an _instance_ of {@{an association}@}. They are {@{_bidirectional_}@}, so {@{no arrowhead is needed}@}. You can {@{still add it}@} to show {@{the _navigability_ of association \(the object at the tail _references_ that at the arrowhead\)}@}, making the association {@{_unidirectional_}@}.

{@{Multiple associations}@} between {@{the same set of objects}@} are {@{allowed if they have _different semantics_}@}. Avoid associations that have semantics that are {@{simply the _composition_ of two associations}@}. For example, if there are {@{two associations `C ? -IsChild- ? B` and `B ? -IsChild- ? A`}@}, there is no need to {@{add the association `C ? -IsChild- ? A`}@}, but it would be okay to {@{add the association `C ? -IsFriend- ? A` because this association has a different meaning}@}.

Associations have {@{6 major properties \(and possibly more\)}@}: {@{name, degree, multiplicity}@}, {@{roles, additional semantics, and class}@}.

{@{The _name_}@} of an association should be {@{_unique_ \(including classes and associations\)}@}, and uses {@{vocabularies according to the application domain}@}. Normally, the name can {@{only be _read meaningfully_ in one direction}@}, and the name for {@{the other direction is _inferred_}@}.

An association is drawn by {@{a line connecting the class to itself \(unary\)}@}, {@{a line between two classes \(binary\)}@}, or {@{a diamond shape connecting many classes \(ternary, etc.\)}@}. \(__this course__: We consider {@{unary and binary associations only}@}.\)

### association degree

{@{The _degree_}@} of an association is {@{the number of _distinct_ classes the association relates to}@}. {@{A single class}@} is {@{_unary_}@}. {@{Two classes}@} are {@{_binary_}@}. {@{Three classes}@} are {@{_ternary_}@}. There are {@{other words for higher degrees}@}.

In practice, most associations are {@{binary}@}. A few are {@{unary}@}, and even fewer are {@{ternary or higher degree}@}. Often, {@{a ternary or higher degree association}@} can be {@{replaced by multiple binary associations}@}, but {@{not always}@}.

Associations of {@{different degree}@} are {@{drawn differently}@}. An association is drawn by {@{a line connecting the class to itself \(unary\)}@}, {@{a line between two classes \(binary\)}@}, or {@{a diamond shape connecting many classes \(ternary, etc.\)}@}. \(__this course__: We consider {@{unary and binary associations only}@}.\)

### association multiplicity

{@{A _multiplicity_}@} of an association is {@{the possible numbers of the association that an instance of the _current_ class may be related to}@}. It is an {@{_application domain_}@} constraint. Note that this is written on {@{the side of the _other_ class rather than the current class}@}. This should not be confused with {@{how multiplicity is placed}@} on {@{the entity—relationship model \(ER model\)}@}, which is {@{commonly used for databases}@}.

To {@{specify multiplicity}@}, specify {@{the _minimum cardinality_ \(min count\) and _maximum cardinality_ \(max count\)}@} on {@{the _other_ class \(not the _current_ class\)}@}. Both are {@{inclusive}@}. {@{_Cardinality_}@} can be {@{any _nonnegative_ integer}@}, or {@{the special wildcard `*` representing infinity}@}. Then, write it using {@{`<min card>..<max card>`}@}. There are {@{shorthands for some multiplicities}@} for {@{`1..` and `0..*`}@}:

- `1` ::@:: `1..1`
- `*` ::@:: `0..*`

When {@{minimum cardinality is 0}@}, this means {@{participation of instances of the other class is _optional_}@}. Otherwise \({@{minimum cardinality is greater than 0}@}\), this means {@{participation of instances of the other class is _mandatory_}@}. Often, there are application domains in which {@{it is not clear if participation of the other class should be optional or mandatory}@}. It may be {@{arbitrary and is simply a matter of taste \(design decision\)}@}. It may also be due to {@{underspecification by the client}@}, and requires {@{further questioning the client}@} to resolve.

In practice, there are {@{"multiplicities" that are _soft_ constraints}@}. We {@{do not use them as multiplicities}@}, because multiplicities are {@{_hard_ constraints that _must_ be followed at _all times_}@}. For example, {@{a student}@} is {@{required to enroll into at least 5 courses}@}. However, the model should {@{still use `*` instead of `5..*` for the multiplicity}@}, because when {@{creating a student instance}@}, we cannot {@{_naturally_ determine the 5 courses to enroll}@}, and vice versa for {@{creating a course instance}@}. So the above constraint is {@{a soft constraint}@}. To express it, we should {@{write a brief text description next to the _hard_ multiplicity}@}.

### association roles

{@{A _role_}@} of an association is {@{one _end_ of an association}@}. It describes {@{the _semantics_ of a class participating in the association}@}. It is written on {@{the side of the _current_ class}@}. It is usually {@{_optional_ for binary associations}@}, and always {@{_required_ for unary associations}@}.

{@{The _name_}@} of a role should be {@{_unique_ in an association}@}.

### association with additional semantics

An association can {@{have additional semantics}@}. {@{The most general way}@} to specify additional semantics is by {@{writing a piece of text next to the association}@}.

However, there are {@{some additional semantics common enough}@} to {@{warrant special representations}@}. There are {@{3 major ones}@}: {@{aggregation, composition, and generalization}@}.

### association aggregations

{@{_Aggregation_}@} represents {@{a _possible_ "part-of" relationship}@}. {@{The component object \(child\)}@} {@{_may_ belong to an aggregate object \(parent\)}@}, and {@{_can_ exist _independently_ of the aggregate object}@}.

Often, the association name is {@{"Has", but can be other names as appropriate for the application domain}@}. We can {@{omit the name as well}@}. Conversely, however, {@{an association with the name "Has"}@} {@{does not imply composition}@}. Aggregation or composition should have {@{intrinsic _asymmetry_ to the association}@}.

In many cases, {@{whether an aggregation \(or composition\)}@} should be used is {@{unclear, and is mostly a matter of taste \(design decision\)}@}. When {@{in doubt}@}, use {@{a pure association}@}.

To {@{represent aggregation}@}, use {@{a _hollow_ diamond \(_adornment_\) at the end of the aggregate object \(child\)}@}. Multiplicity can be {@{omitted if the cardinality range is `0..1`}@}. In some cases, you may want to specify {@{`0..*` as the multiplicity}@}.

### association compositions

{@{_Composition_}@} represents {@{a _mandatory_ "part-of" relationship}@}. {@{The component object \(child\)}@} {@{_must_ belong to an aggregate object \(parent\)}@}, and {@{_cannot_ exist _independently_ of the aggregate object}@}.

Often, the association name is {@{"Has", but can be other names as appropriate for the application domain}@}. We can {@{omit the name as well}@}. Conversely, however, {@{an association with the name "Has"}@} {@{does not imply composition}@}. Aggregation or composition should have {@{intrinsic _asymmetry_ to the association}@}. Composition should also have {@{operations applied to the whole that should also be applied to its parts}@}, e.g. {@{destroying the whole object _requires_ destroying its parts}@}.

In many cases, {@{whether a composition \(or aggregation\)}@} should be used is {@{unclear, and is mostly a matter of taste \(design decision\)}@}. When {@{in doubt}@}, use {@{a pure association}@}.

To {@{represent composition}@}, use {@{a _solid_ diamond \(_adornment_\) at the end of the aggregate object \(child\)}@}. Multiplicity can be {@{omitted if the cardinality range is `1..1`}@}. In some cases, you may want to specify {@{`1..*` as the multiplicity}@}.

### association generalizations

{@{_Generalization_}@} represent {@{a "is-a" or "kind-of" relationship between _subclasses_ and a _superclass_}@}. The subclasses are said to be {@{the _same kind_}@}, and should have {@{_similar_ \(but not the same\) attributes, operations, and associations}@}. It is represented by {@{_inheritance_ in object-oriented programming languages}@}. It allows us to {@{_simplify_ diagrams for _clarity_}@}.

To {@{construct a generalization}@}, we have {@{top-down and bottom-up}@} approaches. Both can be {@{used together}@}.

In {@{the top-down approach}@}, we start with {@{a class with an _discriminator_ attribute}@}, which contains {@{an _enumeration type_}@} to indicate {@{the which other attributes or operations are valid}@} for {@{a particular instance of the class}@}. Then, we {@{generalize the superclass}@}: {@{add a new subclass for each possible value of the discriminator attribute}@}, and {@{remove the discriminator attribute from the superclass}@}. {@{Each subclass}@} should have attributes and operations that are {@{_specific_ \(non-common\) to the subclass}@}. {@{The superclass}@} should only have {@{attributes and operations _common_ to all subclasses}@}. Finally, indicate that {@{it is a generalization \(see below\)}@}.

In {@{the bottom-up approach}@}, we start with {@{several classes with similar attributes or operations}@}. Then, we {@{generalize the subclasses}@}: {@{add a superclass with attributes or operations _common_ to all subclasses}@}, and {@{remove them from all subclasses}@}. Finally, indicate that {@{it is a generalization \(see below\)}@}. {@{_Common_ associations}@} may {@{have objects they are referring to changed}@} and {@{their multiplicity changed}@}.

To {@{indicate a generalization}@}, {@{connect all subclasses}@} to {@{the superclass}@}, and {@{add a _hollow_ triangle pointing towards the superclass}@}. {@{Generalization properties}@} are described by {@{text near it}@}, e.g. {@{`{overlapping, incomplete}`, `{disjoint, complete}`}@}.

#### generalization and inheritance

As mentioned above, {@{generalization}@} is represented by {@{_inheritance_ in object-oriented programming languages}@}. {@{_Inheritance_}@} is {@{inheriting attributes, operations, and relations of a superclass by its subclasses}@}. A subclass can either {@{_add_ new attributes, operations, and relations}@} \({@{indicated}@} in the subclasses\); or {@{_override_ attributes, operations, and relations already defined by a _direct_ or _indirect_ superclass}@} \({@{not indicated}@} in the subclasses\). {@{_Common_ associations on subclasses}@} may be {@{replaced by a single association on the superclass}@}. Note {@{its _multiplicity_}@} may {@{need to be modified}@} to {@{_summarize_ the common associations \(should accommodate them all\)}@} and have {@{an additional text description next to it}@} to {@{describe any semantics \(e.g. different multiplicities\) not carried to the single association}@}.

This allows us to {@{_simplify_ diagrams for _clarity_}@}, because {@{common attributes, operations, and relations}@} are {@{only defined in one class}@} rather than {@{duplicated over multiple classes}@}. This helps with {@{modifiability \(maintainability\), redundancy, and reusability}@}.

{@{Most programming languages}@} support {@{_single inheritance_}@}, in which {@{a class can only have at most one _direct_ superclass}@}. {@{A few programming languages}@} support {@{_multiple inheritance_}@}, in which {@{a class can have multiple _direct_ superclasses}@}.

\(__this course__: We only consider {@{_single inheritance_ but not _multiple inheritance_}@}.\)

#### generalization properties

{@{Generalization}@} can be characterized by {@{2 main properties \(and possibly more\)}@}: {@{_completeness_ and _disjointness_}@}. These two are also called {@{_coverage constraints_}@}. These depend on {@{the semantics of the superclass and subclasses}@} and {@{the _application domain_}@} \(e.g. {@{the exact same generalization in different domains may have different properties}@}\).

{@{_Disjointness_}@} refers to {@{whether an instance of a superclass is also an instance of _at most_ one subclass}@}. A {@{_disjoint_ generalization}@} is {@{one where all instances of a superclass is also an instance of _at most_ one subclass}@}. Its opposite is {@{_overlapping_}@}, in which {@{there are instances of a superclass that are also instances of _multiple_ subclasses}@}.

{@{_Completeness_}@} refers to {@{whether an instance of a superclass must be an instance of a subclass \(i.e. _indirect_\)}@}. A {@{_complete_ generalization}@} is {@{one where all instances of a superclass is an instance of \(_at least_\) one subclass \(i.e. only _indirect_ instances of the superclass can exist\)}@}. Its opposite is {@{_incomplete_}@}, in which {@{there may be _direct_ instances of a superclass that are not instances of any subclasses \(i.e. _direct_ instances of the superclass can exist\)}@}.

{@{These properties}@} are described by {@{text near the generalization}@}, e.g. {@{`{overlapping, incomplete}`, `{disjoint, complete}`}@}.

### association classes

{@{Most attributes}@} clearly {@{belongs to a class}@}. However, there are attributes that {@{do not clearly belong to a class}@}, but {@{rather to associations}@}. It is often needed in {@{many-to-many associations}@}.

There are {@{4 major solutions}@}: {@{many attributes in a class, multi-valued attributes in a class, association class, or separate class}@}. The {@{first 2 solutions}@} {@{do not work \(1st solution: unknown number of attributes; 2nd solution: unknown mapping to links\)}@}, and {@{should not be used}@}. {@{The latter 2 solutions}@} are {@{fine depending on the _application domain_}@}. The 4th solution is {@{applicable to more situations than the 3rd solution}@} since {@{there cannot be multiple links of the same association between the same two objects}@}.

{@{An _association class_}@} is {@{a class used to represent an association}@}. To represent it, you need to use {@{dashed line to connect the association with the association class}@}.

## abstract entities

{@{_Abstract entities_}@} are {@{entities created for _modeling_ purposes}@} that {@{do not have _direct_ instances of it}@}. It can be applied to {@{classes and operations}@}.

{@{An _abstract class_}@} is {@{a class with no _direct_ instances}@}. {@{Its name}@} is {@{_italicized_}@}. A special type of abstract class is {@{an _interface_}@}, which is {@{an _abstract class_ with _operations_ only}@}.

{@{An _abstract operation_}@} is {@{an operation with no _direct_ method \(_direct_ implementation\)}@}. {@{Its name}@} is {@{_italicized_}@}.

## constraints

{@{A _constraint_}@} is {@{an _assertion_ about properties of model elements}@} that {@{must be satisfied at all times \(i.e. they are _hard_ constraints\)}@}. It should be {@{_testable_ \(returns true or false\)}@} and {@{_enforceable_ by the system implementation}@}.

An {@{_attribute constraint_}@} constrains {@{an _attribute_ of a class}@}. It can be indicated by {@{`{<boolean expr>}` next to the attribute or on a note linked with the class by a dashed line}@}, which represents {@{an expression that must always be true}@}, e.g. {@{`balance: money {balance >= 100}`}@}.

An {@{_operation constraint_}@} constrains {@{an _operation_ of a class}@}. It can be indicated by {@{`{<boolean expr>}` next to the operation}@} or {@{on a _note_ linked with the class by a _dashed_ line}@}, which represents {@{an expression that must always be true}@}, e.g. {@{`balance(): money {balance() >= 100}`}@}.

An {@{_association constraint_}@} constrains {@{an _association_}@}. It can involve {@{one association only}@}, which is indicated by {@{`{<constraint 1>, ..., <constraint N>}` next to the association}@}. It can involve {@{multiple associations}@}, which is indicated by {@{a _dashed line_ with text like `{<constraint 1>, ..., <constraint N>}` next to it}@}. Some constraints {@{make the _dashed line_ a _dashed arrow_ instead}@}. Example association constraints include: \(annotation: 3 items: {@{ordering, subset, xor}@}\)

- association constraint: ordering ::@:: `{ordered, FIFO}`, `{ordered, LIFO}`, etc.; for one association, with the text placed closer to the class to be ordered
- association constraint: subset ::@:: `{subset}`; the specialized \(subset\) association has a _dashed arrow_ towards the general \(superset\) association
- association constraint: xor ::@:: `{xor}`; a _dashed line_ linking two associations; exactly one of the two associations can be _instantiated_ \(have _instances_ or _links_\)

For {@{constraints in general}@}, UML provides {@{a text-based _formal_ constraint specification language}@} called {@{_Object Constraint Language \(OCL\)_}@}, similar to {@{C++ or Java}@}. \(__this course__: {@{not covered}@}\)

## dependencies

{@{A _dependency_}@} relates {@{classes whose behavior or implementation affect other classes}@}. It is indicated by {@{a _dashed arrow_}@}. Some example dependencies are: {@{_flow_ and _usage_}@}.

- flow ::@:: An instance of some class may become another class later. The dashed arrow points from the old class to the new class.
- usage ::@:: A class may require another class for its correct functioning. The dashed arrow points from the dependant \(requires\) to the dependency \(required by\).

## realizations

{@{A _realization_}@} relates {@{an _implementation_ to its _specification_}@}, e.g. {@{relating an class implementing an interface to the interface}@}. It is indicated by {@{a _dashed arrow_ with a _hollow_ triangle as the arrow head}@}. It points from {@{the implementation to the specification}@}.

## domain model

{@{_Domain modeling_}@} aims to {@{capture the _most important_ classes and associations}@}. They have {@{_data_ that must be stored}@}. The sources are {@{domain experts \(includes users\), requirements statements, etc.}@}

It is {@{developed _incrementally_ and _concurrently_}@} with {@{the use case model}@}.

### modeling classes

Identify {@{_naturally occurring_ things or concepts}@}. Its name should be {@{a _singular form noun_}@}. It should be {@{_relevant_ to make a _stable system_}@}: {@{_essential_ and _persistent_}@}.

{@{Best practices}@}: \(annotation: 5 items: {@{action/operation, implementation, irrelevant}@}; {@{vague; redundant; dependent; role}@}\)

- action/operation class, implementation class, irrelevant class ::@:: Eliminate.
- vague class ::@:: Eliminate or make specific.
- redundant class ::@:: Eliminate the least descriptive classes.
- dependent class ::@:: Consider application requirements and potentially convert them into attributes or eliminate.
- role class ::@:: Usually eliminate, but depends on the situation. They should be made into roles of associations.

To actually {@{specify the class}@}, specify {@{its name \(singular form noun\) unique in the diagram}@}, {@{attributes, and operations}@}. We assume {@{each attribute has a getter and setter _operation_}@}, which {@{do not need to be specified}@}.

### modeling associations

Identify {@{_naturally occurring_ things or concepts}@}. Its name should be {@{an _active voice verb_}@}. It should be {@{_relevant_ to make a _stable system_}@}: {@{_essential_ and _persistent_}@}.

{@{Best practices}@}: \(annotation: 5 items: {@{action/operation, implementation, irrelevant}@}; {@{ternary; derivable; vague; redundant}@}\)

- action/operation association, implementation association, irrelevant association ::@:: Eliminate.
- ternary association ::@:: Decompose into binary associations. \(__this course__: We do not consider ternary associations anyway...\)
- derivable association :;@:: Eliminate if the _semantics_ of an association is the _composition_ \(or _derivable_ from\) of that of two or more associations.
- vague association ::@:: Eliminate or make specific.
- redundant association ::@:: Eliminate the least descriptive associations.

To actually {@{specify the association}@}, specify {@{its name \(active voice verb; say "what" but not "how" or "why"\) unique in the diagram}@}, {@{multiplicities \(if known\), roles \(if needed\), and association class \(if needed\)}@}.

### modeling attributes

Identify {@{_data_ needed to be stored by classes or associations}@}. Often they are {@{_not_ given in the requirements statement}@} and come from {@{application docs, domain experts, etc.}@} It should be {@{_relevant_ to the _application domain_}@}.

It should correspond to either {@{a _noun_ followed by _possessive_ phrases \(e.g. a person's _date of birth_\)}@} or {@{_adjectives_ \(e.g. _fall_ semester\)}@}. The latter are often {@{_enumerated_ values}@}.

{@{Best practices}@}: \(annotation: 4 items: {@{irrelevant; independent}@}; {@{association; identifier}@}\)

- irrelevant attribute ::@:: Eliminate, to make the class _coherent_ and _simple_.
- independent attribute ::@:: Consider application requirements and potentially convert them into classes or eliminate.
- association attribute ::@:: Put into an association class or, if multiple instances between the same pair of instances are needed, put into a new class replacing the original association.
- identifier attribute ::@:: Eliminate. It is an implementation detail.

To actually {@{specify the attribute}@}, specify {@{its name unique in the class}@}, {@{type \(e.g. date, integer, money, string etc.\), and multiplicity \(if greater than 1\)}@}.

## use case models

{@{_Use case modeling_}@} aims to {@{capture the _system behavior_}@} from {@{the user's point of view}@}. It helps to capture {@{_data_ and _functional_ requirements}@}, plan {@{development _iterations_}@}, and {@{_validate_}@} the system. Overall, it drives {@{_development effort_}@}. It should describe all {@{_required_ functionalities}@}.

It is {@{developed _incrementally_ and _concurrently_}@} with {@{the domain model}@}.

### modeling actors

{@{An _actor_}@} represents {@{any entity that _interacts_ directly with a system from _outside_ its boundary}@}. It can be {@{a person, another system, or a role played by multiple people}@}. In {@{UML terms}@}, an actor is {@{a _stereotype_ of a class \(a kind of class\)}@}; the actor itself is {@{a _classifier_}@} and {@{each concrete _instance_}@} corresponds to {@{a specific user or external system}@}. It is possible that {@{some identified actors}@} have {@{the same name as some of the identified classes}@}. {@{Use cases}@} are {@{_discovered_ from actors}@}.

Each actor has {@{one or more _roles_ when _interacting_ with the system}@}. {@{A single user}@} may {@{assume several distinct roles}@}, and {@{multiple users can share the same role}@}. Actors {@{supply input to the system or receive output from it}@}; in particular, {@{input/output devices themselves}@} are {@{_never_ actors}@}.

To {@{_identify_ actors}@}, ask: \(4 items: {@{end users, information, systems, administration}@}\)

- end users ::@:: Who will use the system?
- information ::@:: Who supplies information to or receives information from the system?
- systems ::@:: Which other systems interact with it?
- administration ::@:: Who is responsible for installation, startup, shutdown, or maintenance?

For {@{each identified actor}@}, ask: {@{What roles do they play during interaction?}@} Then briefly {@{describe its role in the system}@}.

Below is an example of {@{_roles_ \(actor _description_\) in a course registration system}@}:

- course registration system, student ::@:: — enrolls, selects alternatives, changes schedule.
- course registration system, instructor ::@:: — declares teaching assignments, views enrollments.
- course registration system, billing system ::@:: — external system that receives registration data to bill students.

{@{Actors}@} are represented by {@{_stick figures_ with annotating text showing their _names_}@}.

### modeling use cases

{@{A _use case_}@} captures {@{a _concrete_ way an _actor_ interacts with the system to accomplish _part_ of its functionality}@}. It is written from {@{the actor's perspective}@} and describes {@{a complete, normal _sequence_ of _events_ that starts with the actor _initiating_ the interaction}@}. {@{_Alternative_ or _exceptional_ flows}@} are {@{omitted at first}@}; they can be {@{added in the use case _specification_ \(but not use case _diagram_\) later as needed}@}.

A use case must {@{deliver _value_}@} to an actor, e.g. {@{_individual_ functions}@} most likely {@{do not make good use cases}@}. To do so, prefer {@{_longer_ and _extensive_ use cases}@} over {@{smaller use cases}@}; in other words, {@{_real_ and _complete_ use cases}@} are preferred over {@{_sub-cases_ of aforementioned use cases}@}. These preferred use cases can be obtained, after {@{identifying _individual_ use cases \(sub-cases\)}@}, by {@{_grouping_ \(and eliminate redundant\) use cases together}@}.

{@{A _scenario_}@} is {@{the concrete _instantiation_ of a use case}@}. Think of it as {@{a _single run-through_ of the use case}@} from {@{the viewpoint of one particular actor}@}. Scenarios provide {@{a focused, informal description}@} that shows {@{how the system behaves in a real situation}@}. When {@{developing requirements}@} you can adopt either {@{a top-down approach}@}—start with {@{abstract use cases and refine them into scenarios}@}—or {@{a bottom-up approach}@}—begin with {@{detailed scenarios and then generalize to broader use cases}@}. In {@{practice}@} most analysts {@{blend both viewpoints}@}.

In {@{UML terms}@}, a use case is {@{a _stereotype_ of a class \(a kind of class\)}@}; it's {@{a _classifier_}@} that {@{represents a set of interactions}@}. {@{A _scenario_}@}, on the other hand, is {@{an _instance_ of that classifier}@}.

To {@{_identify_ use cases and scenarios}@}, ask {@{these questions for each actor}@}: \(5 items: {@{performance, information, external notifications, internal notifications, administration}@}\)

- performance ::@:: What tasks does the actor want the system to perform?
- information ::@:: Which information will the actor create, store, modify, delete, or read?
- external notifications ::@:: Does the actor need to inform the system of any external changes?
- internal notifications ::@:: Which events must the system notify the actor about?
- administration ::@:: How will the system be supported and maintained?

When {@{naming a use case}@}, use {@{a _present-tense_, _active-voice_ _verb phrase_ from the actor's perspective}@} \(e.g., {@{"student: select course offering"}@} in {@{a course registration system}@}\). Follow this with {@{a brief purpose statement that outlines the functionality}@} in {@{terms familiar to domain experts}@} \(use {@{glossary or data dictionary terminology}@}\).

After {@{identifying use cases and scenarios}@}, we can {@{_expand_ the role \(actor _description_\) of each actor}@} by {@{adding use cases for that actor}@}. Also, write {@{a document listing the use cases}@} \(e.g., {@{"student: select course offering"}@} in {@{a course registration system}@}\). Finally, {@{_group_ use cases}@} so that the use cases are {@{_real_ and _complete_ rather than being sub-cases}@}, and give {@{a name for each grouping}@}; and {@{_eliminate_ _redundant_ use cases}@}, e.g. {@{when a use case is a _composition_ of two or more other use cases}@}. Henceforth, we will call these groups {@{simply "use cases"}@}.

For each \(grouping of\) _use cases_, produce {@{a use case _specification_ \(not diagram\)}@}. Initially, produce {@{a brief _description_ of the _purpose_ of the use case}@} and {@{a _flow of events_ \(steps\) required to _perform_ it}@}. We will {@{_refine_ the steps and describe them in _more detail_}@} as we {@{_discover_ more about the required functionality}@}. For example, a use case called {@{"register for courses"}@} in {@{a course registration system}@} could have a flow of event like {@{"Add course offering. → Drop course offering. → Send billing information."}@}.

{@{\(Groupings of\) _use cases_}@} are represented by {@{_ovals_ with annotating text showing their _names_}@}.

### use case diagrams

{@{A _use case diagram_ \(_context_ diagram\)}@} is {@{a graphical depiction of a user's possible interactions with a system}@}. Its main elements are {@{_actors_ and \(groupings of\) _use cases_}@}.

To {@{draw a use case diagram}@}, identify {@{its main elements}@}. Then, draw {@{a large _rectangle_ to represent the _system boundary_}@}. {@{_Within_}@} the system boundary, draw {@{an _oval_ for each _use case_ with its name}@}. {@{_Outside_}@} the system boundary, draw {@{a _stick figure_ for each _actor_ with its name}@}. Finally, for each {@{actor potentially initiating a use case}@}, draw {@{an _solid arrow_ pointing from the actor to the use case}@}, indicating {@{an _unidirectional association_ with the _implicit_ association name "use"}@}. Optionally, identify {@{_communication_ associations \(flow of information between a \(system\) actor and a use case\)}@}, and draw {@{a _solid line_ \(no arrow as it is _bidirectional_\) connecting the actor and the use case}@}. No need to {@{_name_ the association}@} as {@{the "communication" association name is _implied_ in the context of a use case diagram}@}.

In {@{UML terms}@}, {@{actors and use cases}@} are {@{_stereotypes_ of classes \(kinds of classes\)}@}. So {@{_generalization_}@} also {@{applies to actors and use cases}@}, indicated by {@{a _dashed arrow_ with a _hollow_ triangle as the arrow head}@}, pointing from {@{the sub-actors to the super-actor}@}. Again, using generalization is {@{a _design decision_}@}. \(__this course__: Do _not_ use {@{generalization for use cases}@} in our project. It is {@{_unnecessary_ and often used _incorrectly_}@}.\)

### use case specification

{@{A detailed use case specification}@} is structured around {@{several key elements}@}. {@{The specification}@} should {@{remain concise yet exhaustive enough}@} for {@{developers, testers, and users to understand precisely what the system must do}@}. {@{The elements}@} are: \(annotation: 8 items: {@{name → description → actors → preconditions \(if any\) → flow of events → postconditions \(if any\) → alternative flows \(if any\) → special requirements \(if any\)}@}\)

1. __Name__ ::@:: concise title written as an active-voice verb phrase in the present tense.
2. __Brief description__ ::@:: a short \(one-sentence\) summary of the scenario.
3. __Actors__ ::@:: the participants initiating the use case; it may be listed or illustrated with a use case diagram fragment showing the actor and the use case.
4. __Preconditions__ \(if any\) ::@:: conditions that must hold before the use case can start; they state _what_ is required, not _how_ it is achieved.
5. __Flow of events__ ::@:: a step-by-step narrative of actions performed by actors and the system, written declaratively and numbered.
6. __Postconditions__ \(if any\) ::@:: the state that must hold after completion if it matters to stakeholders or for subsequent use cases.
7. __Alternative flows__ \(if any\) ::@:: optional, variant, or exceptional paths that diverge from the basic flow.
8. __Special (non-functional) requirements__ \(if any\) ::@:: any constraints such as performance or security that apply to this scenario.

#### use case preconditions

In use-case modelling {@{a precondition}@} is {@{a statement about the required state of the system and/or actors that allows the use case to be initiated}@}, e.g. {@{"balance ≥ \$100"}@} in an ATM withdrawal use case. It describes {@{what conditions are required to start the use case}@} \(the "{@{what}@}"\), but it deliberately avoids {@{specifying how those conditions are achieved}@} \(the "{@{how}@}"\).

Preconditions serve to keep {@{each use-case description independent of others}@} by focusing only on {@{the necessary state of both the system and its participants}@}. They are typically written in {@{a declarative style}@} (e.g., {@{"The user is logged in"}@}) and are considered {@{necessary but not sufficient for the use case to proceed}@}, considering that starting a use case {@{always requires an actor to do something}@}.

#### use case postconditions

{@{A postcondition}@} captures {@{the state that the system must be in after the conclusion of a use case}@}, provided that this final state {@{matters to an actor or influences subsequent behaviour}@}, e.g. {@{"after withdrawal, the account balance must remain non-negative"}@} in an ATM withdrawal use case. {@{Postconditions are written}@} when {@{the outcome of the scenario is non-obvious}@} or when {@{the resulting state will act as a precondition for another use case}@}. They help {@{readers—developers, testers, and stakeholders}@}—to understand {@{what has changed in the system}@} and ensure that {@{the intended effects of the interaction have been achieved}@} \(e.g., "{@{The order record}@} is {@{saved in the database}@}"\).

#### use case flow of events

{@{The _flow of events_}@} is {@{a concise \(avoid excessive jargons\), step-by-step narrative}@} that describes {@{exactly what the actors and the system must do to carry out a use case}@}. It does _not_ describe {@{how they are done, thus ignoring use case interactions}@}. It is written {@{declaratively in the form of "&lt;entity&gt; &lt;action&gt;"}@}, e.g., {@{"the actor enters a name"}@}; and each action is {@{numbered in temporal order}@}. The flow begins with {@{the __basic flow__}@}, which represents {@{the most common, normal path from start to finish}@}; this sequence is {@{mandatory and must be fully specified}@}. An example in a course registration system is: {@{instructor selects "Choose courses" → system displays interface}@} → {@{instructor specifies term/year → system shows available courses for that term}@}. Only then, {@{alternative flows are added}@}: \(annotation: 3 items: {@{optional, variant, exceptional}@}\)

- Optional behavior ::@:: — Actions that may occur _in addition_ to the normal flow but are not required for completion.
- Variant behavior ::@:: — A different sequence of steps that can _replace_ part of the normal flow under certain conditions. <p> example: If a schedule already exists when creating one, a pop-up informs the user and jumps to "SelectCourse".
- Exceptional behavior ::@:: — Steps that _handle abnormal situations_ (e.g., invalid input or system errors) and usually lead back to a normal state or terminate the use case. <p> example: If the instructor enters an invalid term, the system shows an error and resumes at "EnterTerm".

From there, {@{optional, variant, or exceptional behaviour}@} can be attached through {@{__alternative flows__ (A1, A2...) that diverge at designated _extension points_}@}. {@{These alternatives}@} may be {@{specific (triggered at a particular step)}@}, {@{bounded (occurring between two extension points; typically inclusive, but best to specify)}@}, or {@{general (starting anywhere in the flow)}@}. {@{Each alternative}@} must explicitly state where {@{control returns to the main sequence}@}—usually {@{the original extension point, another named point, or the end of the use case}@}.

There can be {@{_multiple basic flows_}@}, which are indicated by {@{numbering the basic flows}@}. {@{Each basic flow}@} comes with {@{its own _preconditions_ and _postconditions_}@}, which are also indicated by {@{numbering them}@}.

{@{The structure}@} also supports {@{__branching__ (`if` statements) and __loops__ (`for`, `while`)}@} to model {@{conditional decisions and repeated actions}@}. However, {@{repetition is used sparingly}@} to keep {@{the narrative readable}@}; the emphasis is on {@{an event-response orientation}@} \(i.e. {@{the user does something, then the system does something, etc.}@}\) that focuses on {@{what happens rather than how it is implemented}@}.

> [!example] __branching using `if`__
>
> The syntax for {@{branching}@} using {@{`if`}@}:
>
> ```text
> n.  If <boolean-expression>
>     n.1  <declarative-statement>
>     n.2  <declarative-statement>
>     ...
> n+1.
> ```

<!-- markdownlint MD028 -->

> [!example] __iteration using `for`__
>
> The syntax for {@{iteration}@} using {@{`for`}@}:
>
> ```text
> n.  For <iteration-expression>
>     n.1  <declarative-statement>
>     n.2  <declarative-statement>
>     ...
> n+1.
> ```

<!-- markdownlint MD028 -->

> [!example] __iteration using `while`__
>
> The syntax for {@{iteration}@} using {@{`while`}@}:
>
> ```text
> n.  While <boolean-expression>
>     n.1  <declarative-statement>
>     n.2  <declarative-statement>
>     ...
> n+1.
> ```

#### use case extension points

{@{An _extension point_}@} is {@{a _named_ location in the flow}@} where {@{additional behaviour may be inserted}@}. They come in three forms: \(annotation: 3 items: {@{single location, set of discrete locations, region}@}\)

- _single location_ ::@:: occurs at a single place (e.g., `{Validate Term}` in a course registration system)
- _set of discrete locations_ ::@:: occurs at multiple places (e.g., `{Confirm Selection}` used after both adding and dropping courses)
- _region_ ::@:: a matched pair of points that delimit a set of positions, which are suitably named to make clear that they are matched (e.g., from `{Begin Editing Schedule}` to `{End Editing Schedule}` in a course registration system)

{@{Extension points}@} are mainly employed to {@{host alternative flows}@}, allowing {@{optional, variant, or exceptional behaviour to be attached in a modular way}@} without {@{cluttering the basic sequence}@}.

#### use case alternative flows

{@{An _alternative flow_}@} describes {@{a path that diverges from the normal (basic) sequence of actions}@} in order to {@{capture infrequently used, variant, or exceptional behaviour}@}. {@{Each alternative}@} is {@{numbered (A1, A2, ...)}@} and given {@{a name that is unique within the use case}@}, reflecting {@{its purpose}@}. {@{The first line of an alternative flow}@} indicates {@{where it can be triggered}@}: \(annotation: 3 items: {@{specific, bounded, general}@}\)

- __Specific__ ::@:: "At {extension point} when ...", "At {extension point} if ..."
- __Bounded__ ::@:: "At any point between {extension point 1} and {extension point 2} ..." \(typically both ends inclusive, but best to specify\)
- __General__ ::@:: "At any time in the flow of events ..."

{@{The body}@} lists {@{the steps that occur while the alternative is active}@}. Crucially, {@{every alternative flow—whether optional, variant, or exceptional}@}—must {@{explicitly state where control returns to the main flow}@}: typically {@{the original extension point \(typically optional and exceptional\)}@}, {@{another designated point \(typically variant and exceptional\)}@}, or {@{the end of the use case if it terminates there \(typically exceptional\)}@}. {@{This explicit return}@} ensures that readers understand {@{how the alternative integrates with the overall scenario}@} and prevents {@{ambiguity about the system's subsequent behaviour}@}.

#### use case subflows

{@{A _subflow_}@} is {@{a self-contained segment of behaviour}@} that is {@{referenced from the main flow of events}@} to {@{improve readability and structure}@}. Subflows are {@{__atomic__ in the sense}@} that they have {@{a clear purpose but are not independent use cases}@}; they remain {@{part of the same scenario}@}. They should be {@{numbered (S1, S2, ...)}@} and given {@{unique \(within the use case\), active names}@} that {@{indicate their intent}@}, e.g. {@{"CreateSchedule", "ModifySchedule"}@}. {@{The main flow references a subflow}@} with {@{the phrase "Perform subflow &lt;subflow-name&gt;".}@} Subflows are meant to encapsulate {@{repetitive or complex sequences without creating new use cases}@}; therefore, {@{excessive nesting of subflows}@} should be {@{avoided to keep the specification concise and comprehensible}@}.

### use case detail level

{@{The goal of a use-case specification}@} is to provide {@{sufficient detail so that all stakeholders}@}—{@{developers, testers, business users, and customers}@}—{@{agree on what the system must do}@}. For example, {@{the _basic flow_}@} should {@{unambiguously describe the required behaviour}@}; {@{any ambiguity}@} triggers {@{questions such as "What does this mean?" and should be resolved}@}.

When {@{decomposing behaviour into use cases}@}, avoid {@{fragmenting it into overly small, low-value steps}@} (e.g., {@{_Select Product_, _Enter Order Information_}@}, {@{_Enter Shipping Information_, _Enter Payment Information_, _Confirm Order_}@} should be {@{combined into _Place Order_}@}). {@{Each use case}@} should represent {@{an interaction that provides independent value to the user}@}; otherwise the decomposition becomes {@{counterproductive and increases maintenance effort}@}. This balance ensures {@{clarity without sacrificing cohesion}@}.

To summarize, {@{a single use case}@} should capture {@{a complete, meaningful transaction or activity}@}, with {@{optional subflows handling any complex internal sequences}@}. It should _not_ {@{communicate _directly_ with other use cases}@}, as use cases are {@{_independent_ by design}@}.

## analysis models

{@{The analysis phase}@} of a software project often expands {@{the number of conceptual classes by up to five times compared with earlier stages}@}. In this phase, analysis focuses on {@{functional requirements only}@}; {@{implementation details}@} such as {@{programming-language types or UI layouts}@} are {@{deliberately omitted}@}.

{@{Class descriptions}@} are {@{intentionally kept abstract and independent}@} of {@{any specific programming language or implementation framework}@}. {@{Attribute types}@} describe {@{real-world concepts rather than concrete data types}@}; {@{behavior}@} is captured through {@{textual responsibilities instead of method signatures}@}, and {@{relationships between classes}@} are defined in terms of {@{conceptual associations, not low-level references}@}.

### analysis classes

{@{An analysis class}@} can be {@{one of three stereotypes}@}: {@{_boundary_, _control_, or _entity_}@}. {@{Each stereotype}@} represents {@{a distinct aspect of the system}@} and guides {@{later design decisions}@}.

- boundary classes ::@:: model interactions with actors
- entity classes ::@:: encapsulate long-lived domain data
- control classes ::@:: coordinate behaviour that does not naturally belong to either boundary or entity

{@{Partitioning a use case}@} distributes {@{responsibilities across boundary, entity and control classes}@}. {@{Boundary classes}@} handle {@{environment and external interaction}@}, {@{entity classes}@} manage {@{data storage and processing}@}, and {@{control classes}@} implement {@{the specific logic of the use case}@}. {@{This separation}@} facilitates {@{_localization_ of changes}@} and improves {@{maintainability and _traceability_ \(to use cases\)}@} by resulting in {@{a _stable system_}@}. This means if there is {@{a change in requirements}@}, we start {@{from the use case diagram}@}, identify {@{affected actors}@}, and then {@{trace through boundary, control, and entity classes}@}; this {@{minimizes effort to change requirements}@}.

In practice, we need to {@{make many judgement calls}@} to {@{place the functionalities in their best places}@}. {@{_Design patterns_}@} can help with this.

#### boundary classes

{@{A boundary class}@} models {@{interactions between the system and actors}@}. It abstracts {@{user interface elements}@} such as {@{windows, forms or device interfaces}@}. {@{Its description}@} remains at {@{a high conceptual level}@}; it does not {@{detail individual buttons or menu items}@}.

It is typically {@{drawn in two ways}@}. First, it can appear as {@{an ordinary class box}@} {@{above whose name}@} carries {@{the stereotype `<<boundary>>`}@}; second, it can appear as {@{a circle with an `T` shape extending outward \(typically leftward\)}@}, looking like {@{a push button on a circle}@}. \(__this course__: Use {@{the second way}@}.\)

{@{Boundary classes}@} are derived from {@{use-case descriptions}@} by beginning with {@{the actors}@} and determining {@{what forms, windows or messages}@} they require to {@{interact with the system}@}. The focus is on {@{functional elements}@}—{@{data entry and response}@}—not on {@{visual layout details}@}. When {@{naming and describing these interfaces}@}, practitioners should adopt {@{the terminology that users themselves employ}@}, ensuring the model remains {@{close to real-world language and user expectations}@}.

When {@{specifying boundaries class for a model}@}, begin by creating {@{a single boundary object for every actor—use case combination}@}. For {@{human actors}@} this object represents {@{the main user-interface window through which they interact with the system}@}, while for {@{non-human or external system actors}@} it stands for {@{the communication endpoint that connects to those systems}@}. {@{This one-to-one mapping}@} keeps {@{boundary responsibilities focused and simplifies later refinement}@}. If possible, {@{reuse the same boundary object}@} for an actor, e.g. {@{the boundary object `ProfessorUI` for the actor `Professor`}@}, which includes {@{`CreateScheduleUI`, `SelectCoursesUI` among others}@}.

{@{Boundary objects}@} interact {@{only with control objects and actors}@}, at least {@{_initially_}@}, providing {@{an encapsulation and isolation layer}@} that isolate {@{changes in the system interface}@}. {@{Actors}@} interact {@{only with boundary objects}@}. They should {@{_never_ interact with other boundary objects}@} directly. These result in a {@{well structured and maintainable}@} system.

#### entity classes

{@{Entity classes}@} model {@{long-lived and often persistent information}@}. They represent {@{real-world concepts}@} such as {@{people, events, courses, or departments}@}. They are treated as {@{dynamic objects within the analysis model}@} but typically correspond to {@{persistent data stored in a database}@}.

It is typically {@{drawn in two ways}@}. First, it can appear as {@{an ordinary class box}@} {@{above whose name}@} carries {@{the stereotype `<<entity>>`}@}; second, it can appear as {@{a circle with an underline under it}@}. \(__this course__: Use {@{the second way}@}.\)

To {@{specify entity classes for a model}@}, dissect {@{each use-case scenario}@} and asking {@{which domain entities must participate in that flow}@}. By tracing {@{the steps of a scenario}@}—such as {@{retrieving data, performing calculations or persisting results}@}—you can pinpoint {@{the concrete entity classes}@} that are {@{necessary to fulfil the use case's responsibilities}@}. \(e.g. {@{`Course`, `CourseOffering`, and `Professor`}@} in {@{a course registration system}@}\) The process is somewhat similar to {@{constructing a domain model}@}.

{@{Entity objects}@} interact {@{only with control objects}@}, at least {@{_initially_}@}, providing {@{an encapsulation and isolation layer}@} that isolate {@{changes in information}@}. These result in a {@{well structured and maintainable}@} system.

#### control classes

{@{A control class}@} models {@{control, coordination, sequencing, or transactions}@} for {@{one or more use cases}@}. It typically has {@{no direct counterpart in the application domain}@}; instead, it provides {@{the "glue" tieing other classes together in one or more use cases}@}. It may represent {@{control specific to use case}@} or {@{business logic}@} \(e.g. {@{calculations, complex derivations}@}\). {@{Each control object}@} should be {@{tied to at most one actor}@} to {@{localize changes to business or control logic}@}.

It is typically {@{drawn in two ways}@}. First, it can appear as {@{an ordinary class box}@} {@{above whose name}@} carries {@{the stereotype `<<control>>`}@}; second, it can appear as {@{a circle with an arrowhead pointing to the left overlapping on the top edge of the circle}@}. \(__this course__: Use {@{the second way}@}.\)

To {@{specify control classes for a model}@}, start by creating {@{a single control object for every actor—use case pair}@}, assigning it the task of {@{steering the sequence of events that realize the use case}@}, e.g. {@{`SelectCoursesToTeachMgr`}@} in {@{a course registration system}@}. If {@{the logic is intricate}@}, {@{split the responsibilities}@} across {@{several control objects}@}; conversely, {@{simple or overlapping flows}@} may be {@{merged to avoid redundancy}@}. Importantly, {@{each control object}@} should {@{belong to no more than one actor}@}—this restriction {@{isolates changes and keeps the system's behavior tightly scoped}@} to {@{the actor that initiated it}@}.

{@{Control objects}@} interact {@{with boundary, entity, and other control objects}@}, providing {@{an encapsulation and isolation layer}@} that isolate {@{changes in business or control logic}@}. These result in a {@{well structured and maintainable}@} system.

## design models

{@{The analysis phase}@} establishes {@{a conceptual model}@} using {@{boundary, entity, and control classes}@}, while {@{the design phase}@} translates {@{this model into concrete implementation classes}@}.

{@{Clear separation of concerns, low coupling, high cohesion}@}, {@{active-class identification, and adherence to SOLID principles}@} help produce {@{a robust, maintainable system}@} that can {@{adapt to evolving requirements}@}.

### design classes

{@{A _design class_}@} is {@{a fully specified component}@} that has been {@{completed to the point where it can be translated directly into code}@}. It represents {@{a problem-domain concept \(analysis\) whose behavior and interface have been completely defined}@}, enabling developers to {@{implement it using solution-domain (technology) classes}@}. Design classes form {@{the core of the system's architecture}@} and serve as {@{the blueprint for subsequent implementation phases}@}.

{@{Boundary classes}@} are determined by {@{the choice of user-interface or communication technologies}@}. They act as {@{the system's interface layer}@}, translating {@{external input into internal data structures}@} and presenting {@{output back to users or other systems}@}. By {@{encapsulating UI logic}@}, boundary classes keep {@{presentation concerns separate from business rules}@}.

{@{Entity classes}@} are determined by {@{the choice of technology for data persistence and management}@}. These classes model {@{domain objects that correspond to database tables or other storage mechanisms}@}. They contain {@{attributes and basic operations}@} required for {@{CRUD (create-read-update-delete) interactions}@}, thereby bridging {@{the gap between in-memory representations and durable storage}@}.

{@{Control classes}@} are determined by {@{system behavior across multiple concerns}@} such as {@{distribution, performance, and transactions}@}. They determine whether {@{a separate design class}@} is {@{necessary on each node}@}, decide when to {@{merge with boundary classes for efficiency}@}, and enforce {@{transaction management}@}.

In practice, {@{design classes}@} are described by {@{the syntax of the programming language}@}. When {@{refining an analysis model into design model}@} you should perform these activities: \(annotation: 4 items: {@{reuse, complete, restructure, optimize}@}\)

- _select reusable components_ ::@:: — choose class libraries \(e.g. networking, logging, etc.\) and design patterns \(e.g. factory, observer, singleton, strategy, etc.\) that can be leveraged across the system.
- _complete the specification_ ::@:: — add _attributes_, _associations_, _operations_, types, visibility, and _constraints_ \(in OCL or natural language\); identify which classes are active (i.e., perform behavior).
- _restructure the design model_ ::@:: — introduce new _associations_, use _inheritance_, and _refactor_ duplicated code to common classes to increase reuse among related classes.
- _optimize the design model_ ::@:: — revise access paths with _interfaces or mediators_ to avoid _cycles_, collapse redundant or tightly _coupled_ classes, and apply _caching or lazy evaluation_ to improve performance.

### active classes

{@{An _active class_}@} runs {@{its own thread of control}@} and is typically a {@{boundary or control class}@}. They are shown with {@{_a thicker border_ in class diagrams}@} to {@{distinguish them from passive ones}@}. It is identified by {@{performance, throughput or availability requirements}@}; when {@{distribution across multiple nodes}@} is required; or {@{other requirements}@}.

- performance, throughput, availability ::@:: e.g., real-time input handling may require a dedicated active object for fast response
- system distribution ::@:: e.g., one active object per node and additional objects for inter-node communication enable distributed operation
- other requirements ::@:: Some require an active object capable of initiating or monitoring activity, e.g., system startup/termination, liveness guarantees, deadlock or starvation avoidance, dynamic reconfiguration of nodes, managing connection capacity, etc,

## cohesion and coupling

In {@{both analysis and design}@} we aim for {@{_highly cohesive_ yet _loosely coupled_ classes}@}, balancing {@{these often competing goals}@}. {@{The 7±2 rule}@} guides {@{acceptable coupling}@}. The rule—originating from {@{cognitive psychology's limits on working-memory capacity}@}—suggests that {@{a class or component}@} should expose {@{no more than seven (plus or minus two) other classes, modules, or interfaces}@}.

{@{_Cohesion_}@} measures {@{how many distinct responsibilities a _class_ bears}@}; {@{the most cohesive design}@} is {@{one that performs a single, well-defined function}@}. {@{_Coupling_}@} {@{counts and categorizes a _class_'s dependencies on others}@}; {@{minimal, simple connections}@} yield {@{the lowest coupling}@}, reducing {@{interclass interference and enhancing maintainability}@}.

### cohesion

{@{The spectrum of cohesion}@} ranges from _classes_ that {@{serve no clear purpose (coincidental)}@} up through those that {@{perform a single, well-defined task (functional)}@}. {@{Acceptable cohesion}@} includes {@{"_functional_" \(highest cohesion\) only}@}. The list from {@{lowest cohesion \("scatter-minded"\) to highest cohesion \("single-minded"\)}@} is: \(annotation: 7 items: {@{coincidental &lt; logical &lt; temporal}@} &lt; {@{procedural &lt; communicational &lt; sequential &lt; functional}@}\)

1. __Coincidental__ ::@:: — the class has no discernible function.
2. __Logical__ ::@:: — it groups several related but distinct responsibilities.
3. __Temporal__ ::@:: — its operations are bundled together simply because they occur at the same time.
4. __Procedural__ ::@:: — methods must be executed in a specific sequence.
5. __Communicational__ ::@:: — all operations work on the same data stream or structure.
6. __Sequential__ ::@:: — the output of one operation feeds directly into another within the class.
7. __Functional__ ::@:: — the class has one clear, singular responsibility.

### coupling

{@{The spectrum of coupling}@} ranges from {@{"no direct" to "content"}@}. {@{Acceptable coupling}@} includes {@{"no direct", "data", and "stamp" \(first 3 lowest coupling\)}@}. {@{"Data" \(2nd lowest coupling\) being the preferred form}@} because it {@{involves only simple parameter passing}@}. The list from {@{lowest coupling to highest coupling}@} is: \(annotation: 7 items: {@{no direct &lt; data &lt; stamp}@} &lt; {@{control &lt; external &lt; common &lt; content}@}\)

1. __No direct__ ::@:: — classes have no relationship.
2. __Data__ ::@:: — classes communicate solely through primitive data or simple value objects (ideal).
3. __Stamp__ ::@:: — a fragment of a larger structure is passed as an argument.
4. __Control__ ::@:: — decision-making information such as flags or switches is shared.
5. __External__ ::@:: — both classes rely on external environment resources.
6. __Common__ ::@:: — multiple classes share a global data area or singleton.
7. __Content__ ::@:: — one class accesses the internal data or control information of another (to be _avoided_).

### SOLID principles

{@{The _SOLID principles_}@} are {@{a set of guidelines}@} that promote {@{maintainable, extensible, and robust object-oriented design}@}. {@{Each letter}@} stands for {@{one principle}@} that addresses {@{a different aspect of class responsibility, flexibility, and abstraction}@}. {@{Applying these principles}@} during design promotes {@{modularity and ease of maintenance}@}. They stand for: \(annotation: 5 items: {@{single responsibility, open—closed, Liskov substitution, interface segregation, dependency inversion}@}\)

- _Single Responsibility Principle_ ::@:: Each class has one responsibility.
- _Open—Closed Principle_ ::@:: Classes accept extension but resist modification.
- _Liskov Substitution Principle_ ::@:: Subclasses must be substitutable for superclasses.
- _Interface Segregation Principle_ ::@:: Clients should not depend on unused interfaces.
- _Dependency Inversion Principle_ ::@:: High-level modules should _not_ depend on low-level modules. Both should depend on abstractions. Further, details should depend on abstractions, not the reverse.

## state machine diagrams

{@{A _state machine diagram_}@} is {@{a directed graph}@} that models {@{the lifetime behavior of a single _object_ \(loosely speaking, _class_\)}@}. It contains {@{_every_ possible states and transitions}@}. {@{Nodes}@} represent {@{states}@} and {@{arcs \(arrows, directed edges\)}@} denote {@{transitions triggered by events}@}. The diagram shows {@{all possible messages an object can send or receive}@} during {@{its life cycle}@}.

{@{A state machine diagram}@} is represented by {@{large rectangle with slightly rounded corners}@}. It contains {@{the class name at top}@}, separated by {@{a horizontal line}@} from {@{the state machine diagram below}@} in the rectangle.

When {@{constructing a state-machine diagram}@}, we begin by {@{listing every possible state the class can occupy}@}. Next, we identify {@{the conditions or triggers}@} that determine {@{which state the class is in at any time}@}. Finally, for {@{each state}@} we specify how it {@{responds to incoming events or messages}@} and detail {@{the actions executed when those events occur}@}.

{@{Not every class}@} needs {@{a state machine diagram}@}. They are best suited for {@{classes exhibiting _critical_ or significant _dynamic_ behavior}@}—such as {@{bank accounts, traffic lights, or user interfaces}@}. They provide {@{a concise visual representation}@} of {@{an object's possible behaviors and interactions over time and multiple use cases}@} for {@{clarity and communication to stakeholders}@}.

### states

{@{A _state_}@} represents {@{a period in which an object}@} {@{satisfies certain conditions, performs actions, or waits for events}@}. States have {@{duration}@} and may be {@{named (e.g., _InCredit_) or anonymous \(_anonymous states_\)}@}. Prefer {@{named ones over anonymous ones}@} so that {@{stakeholders can understand them}@}. They can be identified by {@{attribute values, links to other objects, or both}@}.

{@{A state}@} is drawn as {@{a rectangle with slightly rounded corners}@}. If it {@{has a name}@}, then {@{its name is also indicated}@}. If it {@{has self-transition adornments}@}, then {@{a horizontal line is added}@} to separate {@{the name \(if any\)}@}, and below the line {@{the self-transitions are listed}@}.

#### initial and final states

{@{Each diagram}@} must contain {@{at most one _initial state_}@} that marks {@{the entry point of the object's life cycle}@}. {@{_Final states_}@} indicate {@{termination \(object deleted or destructed\)}@}; a diagram may have {@{multiple final states}@}, and {@{no explicit initial or final state}@} implies {@{looping behavior}@}.

{@{An initial state}@} is drawn as {@{a solid black circle}@}. {@{A final state}@} is drawn as {@{a solid black circle with another hollow circle surrounding it}@}. They are treated as {@{states}@} with respect to {@{other things in the state machine diagram}@}. They typically do not {@{need a name}@}.

### transitions

{@{A _transition_}@} connects {@{an origin (source) state to a target state and}@} is {@{triggered by an event}@}. Transitions can be {@{self-loops when source and target are the same}@}. They occur {@{_instantaneously_, cannot be _interrupted_}@}, and may {@{carry _optional adornments_}@}: {@{an event trigger, guard condition, and effect list}@}.

For {@{self-transitions}@}, {@{the adornments are listed inside the state}@}. For {@{transitions to other states}@}, {@{an arrow}@} is {@{drawn from the source state to the target}@}, and {@{all adornments are listed}@} next to it. {@{The syntax}@} for {@{a transition}@} is {@{`event trigger [guard condition] / effect list`}@}.

An {@{_event trigger_}@} specifies {@{the _event name_ that _triggers_ a transition, optionally with _parameters_}@} which will be available to {@{the transition's effects or activities in the _target state_}@}.

{@{A _guard condition_}@} is {@{a Boolean expression evaluated when the event occurs}@}. {@{The transition _fires_}@} {@{only if the guard evaluates to true}@}. Guards are {@{passive and evaluated at the time of the event}@}. It is written in terms of {@{parameters of the event, attributes, and links of the object in _source state_}@}.

An {@{_effect list_}@} contains {@{one or more atomic actions}@} (e.g., {@{calling operations, sending messages}@}) that {@{execute _immediately_ after a transition fires}@}. Effects may refer to {@{_source state_ operations, attributes, links, and event parameters}@}. {@{The atomic actions}@} are {@{separated by _semicolons_ `;`}@} and {@{executed _sequentially_}@}.

### events

An {@{_event_}@} is {@{something that happens at an _instantaneous_ point in time}@}. It can be classified as: \(annotation: 4 items: {@{call, change, signal, time}@}\)

{@{A _call event_}@} is triggered by {@{the receipt of a _synchronous call_}@}. The event trigger contains {@{the operation name and its parameters}@}, which are {@{exactly the same as the parameters passed to the invoked operation}@}.

{@{A _change event_}@} occurs whenever {@{a Boolean expression that depends _solely_ on the _source state_}@} {@{changes from false to true}@}, e.g. {@{`when(balance < 0)`}@}. {@{The condition}@} is {@{evaluated _continuously_}@}; unlike {@{a guard}@}, which is {@{checked only when encountered}@}, a change event {@{_actively_ monitors its expression}@}. Because {@{it has no parameters}@}, {@{any transition triggered by a change event}@} relies {@{entirely on the _source state_}@}.

{@{A _time event_}@} represents either {@{an absolute point in time (e.g., `when(date=2025-11-11)`)}@} or {@{a relative delay (e.g., `after(7 seconds)`)}@}. It causes {@{a transition when the specified moment arrives}@}, and it can be used to model {@{timed actions}@} such as {@{automatic state changes or periodic checks}@}.

{@{A _signal event_}@} is {@{an _asynchronous message_ represented by a _stereotyped_ class (`<<signal>>`)}@}. It carries {@{a package of information between objects}@} without {@{waiting for a response}@} and is commonly employed in {@{real-time system specifications}@} to model {@{non-blocking communication}@}.

{@{Events in a state machine}@} are {@{handled _sequentially_}@}: {@{each event}@} is {@{examined one at a time}@} and, if {@{no transition matches it}@}, {@{the event is simply _ignored_}@}. {@{At most a _single_ transition}@} may {@{fire for any given event}@}; if {@{two transitions could fire simultaneously}@} the choice becomes {@{nondeterministic (a race condition)}@} and usually indicates {@{a specification error}@}. Consequently, {@{every state transition}@} must be triggered by {@{a distinct event to avoid ambiguity}@}.

{@{A state}@} can be {@{exited either automatically or non-automatically}@}. {@{_Automatic_ transitions}@} {@{fire immediately once the state's internal activity (if any) finishes}@}, occurring when {@{there are transitions without any _adornments_ \(labels\)}@}; {@{_non-automatic_ transitions}@} are driven by {@{an explicit event}@} that occurs while {@{the object remains in that state}@}.

### actions and activities

In a state machine, {@{_actions_}@} are {@{instantaneous, uninterruptible steps}@} that occur {@{during transitions or at state entry/exit}@}, while {@{_activities_}@} are {@{time-consuming tasks that can be interrupted}@} and run {@{while the object remains in the state}@}. {@{A state}@} may exhibit {@{one of several behaviors}@}: \(annotation: 5 items: {@{no behavior, adornment, `do`, `entry`, `exit`}@}\)

- no behavior ::@:: it may do nothing and simply wait for an event to exit the state
- \(action\) adornment ::@:: execute a \(potentially guarded\) transition whose effect list runs when its trigger occurs, e.g. `help / display help`, etc.
- \(activity\) `do` ::@:: perform a continuous activity (e.g., looping operations), e.g. `do / collect telemetry`, etc.
- \(action\) `entry`, `exit` ::@:: run entry/exit _actions_ \(not _activities_\) each time the state is entered or left, e.g. `entry / set echo to star; clear password`, `exit / set echo to normal`, etc.

### composite states

{@{A _composite state machine diagram_}@} represents {@{a higher-level state \(_superstate_\)}@} that {@{contains one or more nested state machines \(_substates_\)}@}. {@{The outer state}@} encapsulates {@{its sub-states}@}, allowing the model to hide {@{internal complexity}@}. {@{Each nested diagram}@} can be treated as {@{an independent behavioral unit}@}. {@{The nested state machine}@} may be {@{_sequential_ or _concurrent_}@}.

{@{A composite state}@} is indicated by {@{a glasses-looking symbol on the bottom right corner}@}. Actually, the symbol is supposed to be {@{two states connected together}@}. Alternatively, to {@{show the substates as well}@}, simply {@{draw another state machine diagram inside the state}@}.

For {@{an overall composite state}@}, {@{a transition that _ends_ at its _boundary_ \(but no further inside\)}@} is equivalent to {@{entering the all of its initial states for all regions}@}; when this occurs {@{all entry actions for the state of every region entered}@} are executed. {@{A transition that _starts_ from its _boundary_ \(but no further inside\)}@} is equivalent to {@{exiting all of its states for all regions}@}; when this occurs {@{all exit actions for the state of every region}@} are executed.

There can be {@{direct transitions}@} from {@{a specific region}@} to {@{outside the composite state or to the composite state _itself_}@}, or from {@{outside the composite state or the composite state _itself_}@} to {@{a specific region}@}. For {@{_concurrent_ composite states}@}, there can even be {@{transitions with multiple source and target states}@} \(see below\).

#### sequential composite states

{@{A _sequential_ composite state machine diagram}@} \(also called {@{a choice or "or" composite}@}\) models situations in which {@{an object occupies _exactly one_ of several sub-states at any time}@}. {@{The selection among these sub-states}@} is governed by {@{an exclusive condition}@}, meaning that {@{the outer state}@} behaves as though it were {@{in one particular nested state based on the current context}@}. This construct is useful for {@{_abstracting_ or _generalizing_ a set of mutually exclusive behaviors}@}.

Inside {@{a sequential composite state}@}, it should have {@{an initial state}@}. It need not {@{have an final state}@}, as {@{outside transitions outgoing the overall composite state}@} can represent {@{exiting the state}@}.

#### concurrent composite states

{@{A _concurrent_ composite state machine diagram}@} \(also known as {@{a parallel or "and" composite}@}\) allows an object to be {@{simultaneously in one sub-state from each of several independent _regions_}@}. {@{The conjunction of these sub-states}@} captures {@{multi-threaded or concurrent behavior}@}, where {@{the overall state}@} reflects {@{the combination of all active region states}@}. {@{Concurrency arises}@} when an object ca be {@{partitioned into subsets of attributes and links}@}. Each region can evolve {@{independently}@}, and {@{transitions in one region}@} do not {@{preclude activity in another}@}.

Inside {@{a concurrent composite state}@}, {@{each region}@} should have {@{an initial state}@} and {@{one or more final states}@}. {@{The regions}@} are separated by {@{_dashed horizontal lines_}@}.

For {@{concurrent composite states}@}, there can be {@{transitions involving multiple source or target states simultaneously}@}, which model either {@{splitting control flow across concurrent regions \(_fork_\)}@} or {@{synchronizing concurrent sub-states \(_join_\)}@}. It is indicated by {@{a _synchronization bar_ \(a vertical line outside the composite state\)}@}, with {@{potentially multiple arrows targeting one side of the bar}@} and {@{potentially multiple arrows originating from the other side of the bar}@}. Their semantics are:

- _fork_: multiple target states ::@:: — after firing a transition from a source state, all target states become enabled concurrently.
- _join_: multiple source states ::@:: — a transition into the target state fires only after _all_ source transitions have completed, enabling coordinated actions.

Without {@{a synchronization bar}@}, {@{a transition}@} can {@{only have one source and target state}@}, and {@{multiple transitions}@} are {@{mutually exclusive; only one path is taken}@}.

## common mistakes

There are {@{many possible mistakes}@} when {@{learning to draw UML diagrams}@}. Here describes {@{some of the most common ones}@}.

### common mistakes: bad name

Students frequently use {@{the same term}@} for both {@{a class and an attribute}@} or choose {@{names that reflect programming constructs}@} (e.g., {@{"int" or "string"}@}) instead of {@{domain terms}@}. This occurs when {@{the analyst's mental model}@} is still {@{tightly coupled to code rather than to the problem space}@}. The result is {@{a diagram that looks syntactically correct}@} but fails to communicate {@{intent to stakeholders}@}. To remedy this, insist on using {@{vocabulary from the application domain}@} for {@{every classifier and attribute name}@}, and verify {@{each name against a glossary}@} <!-- or requirement traceability matrix --> before {@{committing it to the diagram}@}.

In the banking example, when an association is {@{for the result of an operation}@}, students often think {@{use the action as the association name}@} (e.g., {@{`Customer` creates `Account`}@}). In UML, {@{naming an association}@} expresses {@{its relationship}@}, not {@{an invoked action}@}. {@{The correct practice}@} is to name {@{associations based on their semantic contribution}@} (e.g., {@{`Customer` holds `Account`}@}) rather than {@{operation verbs}@}.

### common mistakes: "has" relation

{@{Many "Has" associations}@} are better {@{represented as simple associations}@} rather than {@{aggregations or compositions}@}. Yet students often {@{default to aggregation}@} because they see {@{a part-whole phrase in natural language}@} and automatically {@{apply the adornment}@}. This mistake arises from {@{a lack of judgment}@} about {@{the life cycle coupling between objects}@}. Evaluate whether {@{the part can exist independently}@}; if so, {@{use aggregation}@}. If {@{the part's existence is strictly tied to the whole}@}, {@{use composition}@}. When {@{uncertain}@}, lean toward {@{a plain association to avoid over-engineering}@}.

In the {@{banking example}@}, students sometimes mark {@{a "has-a" relationship between `Account` and `Transaction`}@} as {@{an aggregation or composition}@}, implying that {@{a transaction belongs to a particular account}@}. In reality, a transaction often {@{involves multiple accounts}@}; there is {@{no account that a transaction belongs to}@}. This should be modeled with {@{a regular association}@}. Another example is {@{composition between `Customer` and `Account`}@} when {@{a customer owns an account}@}, but {@{composition}@} implies that {@{the accounts are integral to the existence of customers}@}. The proper modeling is {@{still a regular association}@}. {@{Aggregation or composition}@} should only be used when {@{the part is highly dependent on the whole}@}.

### common mistakes: ER model

{@{The placement of cardinalities}@} differs between {@{ER models and UML class diagrams}@}. Students who copy {@{ER notations directly into UML}@} often {@{misinterpret constraints}@} \(e.g., writing {@{`0..1` on both ends}@} when only {@{one side should be optional}@}\). This confusion is rooted in treating {@{UML as a database schema tool}@} rather than {@{a behavioral model}@}. Clarify that {@{UML multiplicity}@} applies to {@{object relationships at runtime}@}, whereas {@{ER cardinalities}@} describe {@{persistent data constraints}@}. When translating {@{an ER diagram into UML}@}, {@{reassess each association's semantics}@} before {@{assigning cardinalities}@}.

### common mistakes: unary association roles

When {@{two instances of the same class are linked}@}, i.e. {@{_unary_ associations}@}, \(e.g., {@{"manages" or "friends"}@}\) students sometimes {@{omit role names}@}, leading to {@{ambiguity about which end represents which role}@}, e.g. {@{the manager and the subordinate}@}. This mistake occurs because they assume {@{symmetry in the relationship}@}. _Always_ provide distinct role names at {@{each end of a unary association}@}; for {@{binary associations}@}, {@{the roles should be added}@} whenever {@{the roles are not obvious from the association name}@}. <!-- This disambiguates navigation and clarifies intent. -->

### common mistakes: implementation details

Many students think that once {@{a class diagram is complete}@}, it can be {@{directly turned into code with little modification}@}. This misconception leads to {@{diagrams that are too fine-grained}@} (e.g., {@{modeling every private field}@}) or omit {@{necessary abstraction layers}@}. Remember that UML models should capture {@{essential structure and behavior at the appropriate level of abstraction}@}; {@{refine or abstract}@} as needed before {@{mapping to implementation}@}.

An example involves treating {@{internal object identifiers (OIDs)}@} as {@{regular attributes}@} and then using {@{those same attributes}@} to {@{represent relationships}@} — for example, {@{`personID`, `vehicleID`, `loanID`, `ownerID`, etc.}@} {@{Other attributes}@} that are {@{internal details}@} include {@{"type" attributes associated with relationships}@}, e.g. {@{`customerType`, `ownerID`, etc.}@} When students {@{simply copy these attributes into their diagrams}@} they create {@{unnecessary data fields}@} that clutter {@{the model}@} and hide {@{the true cardinality of relationships}@}. The root cause is a misunderstanding that identifiers are {@{always required in the diagram}@}; in reality they belong to {@{the underlying database implementation}@}, not {@{the conceptual model}@}. The fix is straightforward: remove {@{all OID attributes from the class diagram}@}, replace {@{each with an association to the appropriate target class}@}, and then annotate {@{the association with the correct multiplicity}@} (e.g., {@{a `Person` or `Company`}@} "owns" {@{zero or more `Car`s}@}). This keeps the diagram {@{focused on structural relationships}@} rather than {@{persistence details}@}.

### common mistakes: association class

When {@{an association}@} requires {@{attributes or operations}@}, students sometimes {@{attach them directly to one end}@} rather than creating {@{an explicit association class}@}. This leads to {@{a cluttered diagram}@} and obscures the fact that {@{the relationship itself has its own identity}@}. Use {@{an association class}@} ({@{a separate rectangle}@} connected to {@{the association line by a _dashed line_}@}) whenever {@{the link carries state or behaviour}@}.

### common mistakes: uniqueness of names

{@{The collection of class and association names}@} must be {@{unique}@}. Students often {@{overlook this rule}@}, especially in {@{large diagrams with many similar entities}@}, resulting in {@{name collisions that confuse readers and tooling}@}. Before {@{finalizing a diagram}@}, run {@{a quick consistency check}@}—either {@{manually}@} or using {@{a UML tool's validation feature}@}—to ensure {@{every class and association has a distinct identifier}@}.

### common mistakes: XOR associations

A frequent mistake is {@{the construction of exclusive-or \(XOR\) associations}@} that either {@{duplicate each other}@} or do not reflect {@{the business rules stated in the requirements}@}. For instance, students often draw both {@{a "OwnsPersonal" and an "OwnsCorporate" association}@} from {@{`Car` to `Person` and `Company`}@}, respectively, without recognising that a car can {@{have only one owner who may be either a person or a company but not both}@}. {@{Multiplicities for XOR associations}@} are frequently {@{set incorrectly}@}: If {@{`1` is used on the owner's side}@}, it allows {@{multiple owners for a single car}@}. If {@{`0..1` is used on the owner's side}@}, it allows {@{no owners for a single car}@}. The remedy is to {@{use `1` on the owner's side to ensure a car has an owner}@}, and then {@{enforce an exclusive-or (XOR) constraint between the two associations}@} to ensure that {@{only one of the owner types is present}@}. {@{The exclusive-or \(XOR\) constraint}@} is denoted by {@{a _dashed line_ connecting the two associations with the label text `{xor}`}@}.

Sometimes, {@{an alternative}@} to {@{using XOR associations}@} is {@{using generalization}@}. Using the same car example, {@{`Person` and `Company`}@} may be {@{generalized to a superclass `Owner` with `{complete, disjoint}` coverage}@}, and then {@{the two associations with an XOR constraint between them}@} becomes {@{a single association: `Owner` _owns_ `Car`}@}.

### common mistakes: operations as associations

A frequent slip is drawing a {@{line between two classes}@} to represent {@{an operation that one class performs on another}@}. Operations are {@{not structural links}@}; they belong {@{inside a class box or in a separate operation diagram}@}. {@{Mixing them with associations}@} confuses {@{the modeler}@} and obscures {@{true dependencies}@}. To fix this, keep {@{operations within the class where they reside}@} and use {@{associations only}@} for {@{persistent relationships such as ownership or participation}@}.

### common mistakes: redundant associations

In {@{a UML class diagram}@}, it is common to introduce {@{an association}@} simply because {@{two classes appear to "talk" to each other}@} in {@{the problem description}@}.  However, when {@{several associations}@} share {@{the same participants and multiplicities}@}, {@{some of them may be redundant}@}: they can be {@{inferred from others without being drawn explicitly}@}.  For example, if {@{`Person` _owns_ `Car` and `Loan` _is for_ `Car`}@}, then {@{a direct association between `Person` and `Loan` is unnecessary}@} because {@{the relationship "a person's car loans"}@} can be {@{derived by following the two existing links}@} ({@{`Person` → `Car` → `Loan`}@}). {@{Redundant associations}@} clutter {@{the diagram, obscure intent}@}, and may lead to {@{inconsistent multiplicities}@}.

{@{A systematic way to eliminate redundant associations}@} is to check {@{whether one can reach the target class through a chain of existing associations}@} whose {@{roles and multiplicities}@} satisfy {@{the same constraints as the proposed direct link}@}, and additionally, {@{the semantics of the association to be eliminated}@} can be {@{derived}@} \(see below\). If so, {@{omit the redundant association}@}; keep {@{only the minimal set}@} that preserves {@{all required navigation and cardinality rules}@}.

Nevertheless, not {@{every seemingly superfluous link}@} is {@{truly dispensable}@}. When {@{three associations}@} involve {@{the same classes}@} but {@{the third association}@} carry {@{distinct semantic roles or constraints from the other two associations}@}, then {@{all of them must be kept}@}.  For instance, {@{`Customer` _owns_ `Account` and `Transaction` _is against_ `Account`}@} are separate from {@{`Customer` _makes_ `Transaction`}@} because {@{the customer making the transaction}@} can be {@{different from the owners of the accounts involved in an transaction}@}. In these cases, {@{the third association}@} conveys {@{unique information from the other two associations}@} and {@{omitting the third association}@} would erase {@{critical business rules}@}.

Another example involves {@{generalization}@}. For instance, {@{`Employee` generalizes `Manager`}@}, and {@{both `Employee` and `Manager` manages sales as a use case}@}. If {@{every scenario a `Manager` can take in the use case}@} is {@{also takable by the `Employee`}@}, then we do not {@{need an arrow from `Manager` to "manage sales"}@}. However, if there are {@{functionalities a `Manager` can _additionally_ take compared to an `Employee`}@}, {@{both arrows from `Employee` and `Manager` to "manage sales"}@} are {@{needed as these two arrows convey somewhat different semantics}@}.

### common mistakes: real world knowledge

{@{Real world knowledge}@} is {@{important when constructing UML diagrams}@}, e.g. {@{setting multiplicities, etc.}@}

{@{Multiplicity}@} tells the modeler {@{how many instances participate in a relationship}@}. {@{Leaving it blank or marking it with "?"}@} when {@{the domain knowledge suggests a clear bound}@} (e.g., {@{a `Bank`}@} can issue {@{zero or more `CreditCards`}@}) leads to {@{ambiguity}@}. The fix is to infer {@{multiplicities from real-world constraints}@} and annotate {@{them explicitly, such as `*` for unlimited or `1` for mandatory}@}.

### common mistakes: misusing modeling elements

In the banking example, students sometimes add {@{a XOR operator between `Savings` and `Checking`}@} to {@{indicate exclusivity}@}. However, UML does not {@{support XOR on generalizations}@}; it only applies to {@{associations that are mutually exclusive}@}. {@{The correct way}@} is to note {@{in documentation}@} or use {@{`{disjoint}` and `{complete}` constraints}@}, but avoid {@{visual XOR symbols that UML does not support}@}.

### common mistakes: modeling out-of-scope entities

In the banking example, {@{a `Passbook` should not be represented}@} because {@{it is outside the system}@}. Yet many diagrams add {@{a separate class for it}@}. This mistake stems from treating {@{every real-world object as a candidate class}@} without considering {@{whether it is part of the _system_ being considered}@}. The fix is to model {@{only classes in the _system_ required by the problem statement}@}.

Often but not always, {@{out-of-scope entities}@}, when {@{wrongly represented in the system}@}, are {@{not connected to any other class by associations}@}. So {@{a class without associations to other classes}@} may be {@{a sign that the class is out-of-scope}@}.

### common mistakes: not using notes

When there are {@{semantics not modeled by standard modeling elements}@}, use {@{notes containing brief text}@}.

In the banking example, marking {@{a `Transaction`'s "IsAgainst" association to `Account`}@} with {@{`1..2`}@} when the requirement is that {@{a transfer \(`Transfer`\)}@} involves {@{exactly two accounts}@} but {@{a deposit \(`Deposit`\) or withdrawal \(`Withdrawl`\)}@} involves {@{one}@}. Students often generalize {@{`Transaction`}@} and have {@{the 3 types of transactions as subclasses}@}. This is {@{okay}@}, but apart from {@{marking the "IsAgainst" association to `Account` with `1..2`}@}, also refine {@{multiplicities at the subclass level}@} by {@{adding an extra note describing the details}@} (e.g., for {@{`Transfer`}@}, use {@{`2`}@}; in {@{`Deposit` and `Withdrawal`}@}, set {@{it to `1`}@}).

### common mistakes: multiple links between the same pair of objects

{@{An association}@} represents {@{a collection of links}@}, and {@{for the same pair of objects}@}, there is {@{at most one link}@}. Sometimes, {@{the requirements}@} may require {@{possibly more than one link between the same pair of objects}@}. In this case, replace {@{the association}@} by {@{a class \(not an _association class_\)}@}, and the class {@{connects the two classes originally connected by the association}@}.

In the course enrollment system example, there may be {@{multiple enrollments}@} between {@{a `Student` and a `Course`}@}, e.g. {@{retaking a failed course}@}. In that case, {@{an association \(including association class\)}@} is {@{inappropriate}@} and should be replaced by {@{a class `Enrollment`}@} connecting {@{`Student` and `Course` with two new associations}@}.

However, sometimes that {@{at most one link can be created between the same pair of objects}@} can be {@{useful}@}. In said cases, you may instead want to replace {@{the class connecting other two classes by two associations}@} with {@{an association}@} instead.

\(__this course__: __Important__. Tested in the midterm examination.\)

### common mistakes: generalization and multiplicity

When {@{a subclass}@} participates in {@{an association that other subclasses also uses}@}, students sometimes fail to {@{adjust the multiplicities appropriately}@} when generalizing {@{these subclasses as a superclass}@} and then replacing {@{common associations on the subclasses with an association on the superclass}@}. They may copy {@{the exact cardinalities from one of the subclass association}@} without considering {@{the more restrictive bounds of other subclass associations}@}. The mistake occurs because the learner overlooks that {@{the resulting association on the superclass}@} must satisfy {@{the original set of associations on the subclasses}@}. Correcting this requires either taking {@{the maximum of the lower bounds and the minimum of the upper bounds}@}, and then adding {@{a note to indicate multiplicities for each subclass}@}; or defining {@{the association for each subclass}@} if {@{the semantics differ}@} \(i.e. do not {@{replace the common associations on the subclasses with an association on the superclass}@}\).

### common mistakes: missing generalization coverage

Students often draw {@{a generalization hierarchy}@} but do not indicate whether {@{the subclasses are disjoint, overlapping, complete, or incomplete}@}. This omission leads to {@{ambiguous models}@} where {@{an instance}@} could {@{belong to multiple subclasses or none at all}@}. The cause is usually {@{a lack of attention to the domain rules}@} that dictate {@{exclusivity and completeness}@}. To fix this, add the {@{appropriate coverage notation}@} (e.g., {@{`{disjoint, complete}`}@}) next to {@{the generalization arrow}@} so that the diagram conveys whether {@{instances must belong to exactly one subclass or may belong to several}@}.

### common mistakes: missing association constraints

Students sometimes model {@{an association between two classes}@} without specifying {@{whether it is ordered, unique, or has subset/xor constraints}@} (e.g., {@{a car}@} can be owned by {@{either a company or a person}@} but {@{not both}@}). The error comes from treating {@{associations as unqualified links}@}. To correct this, add {@{the appropriate OCL constraint syntax}@} \(e.g. {@{`{xor}`, `{subset}`, `{ordered, FIFO}`}@}\) on {@{the association line}@}.

### common mistakes: not using specialized associations

{@{Complex relationships}@} such as {@{dependencies, realizations, or usages}@} are {@{frequently omitted or modeled by simple associations}@} because students think they are {@{unnecessary for a data model}@}. This leads to models that cannot capture {@{how classes influence one another during execution}@}. The fix is to include {@{these relationship types where relevant}@}—use {@{a dependency arrow}@} when {@{a class's implementation relies on another}@}, or {@{a realization arrow}@} to link {@{an interface with its implementing classes}@}.

\(__this course__: __Important__. So far, it seems like we just need to {@{know about them}@} but {@{no need to use them}@}... Is it?\)

### common mistakes: use case scope

A frequent pitfall arises when students craft {@{use cases}@} that are {@{either too granular or too sweeping}@}, which undermines {@{the very purpose of a _use case_ as a _classifier_}@} for {@{a complete, actor-initiated _scenario_}@}. When a use case is {@{split into many tiny fragments}@}—such as {@{separate cases}@} for {@{"Validate Student ID", "Select Course", and "Confirm Registration"}@}—the diagram becomes {@{cluttered with redundant elements}@} that merely {@{state different parts of a complete interaction}@}. This fragmentation often occurs because analysts mistake {@{every user action or system step}@} for {@{a distinct functional requirement}@}, driven by a desire to {@{capture everything explicitly}@}. The result is {@{a fragmented model}@} where {@{the overarching business process ("Register for Courses")}@} is {@{obscured}@}, making it hard to trace {@{responsibilities and evaluate completeness}@}.

Conversely, when {@{a use case}@} is {@{too broad}@}—encompassing {@{"Manage Course Catalog", "Handle Billing", and "Process Enrollment"}@} in {@{one single box}@}—it loses {@{its focus}@} and fails to represent {@{a coherent interaction}@}. {@{Such monolithic cases}@} arise from {@{an over-generalization mindset}@}: analysts aim for {@{minimalism}@} by collapsing {@{all related actions into one umbrella}@}, thinking that fewer {@{diagrams mean less work}@}. However, the consequence is {@{a lack of clarity}@} about who {@{initiates the use case}@}, what {@{steps are involved}@}, and how {@{the system's response should be measured}@}.

The core issue lies in misunderstanding {@{the definition of a use case}@} as {@{a _classifier_ that encapsulates a complete scenario initiated by an actor}@}. To remedy this, first identify {@{each distinct business goal from the actor's perspective}@}—what value {@{does the actor receive}@}? {@{Each goal}@} becomes {@{a single use case with a clear name}@} (e.g., {@{"Register for Courses"}@}). Then, within {@{that use case}@}, document {@{the full sequence of events}@}: {@{success path}@} and any {@{necessary alternative flows}@}. Avoid creating {@{separate cases}@} for {@{low-level operations}@} unless they constitute {@{an independent business process}@}. By aligning {@{each use case}@} with {@{one complete scenario driven by an actor}@}, the model remains {@{both manageable and expressive}@}, faithfully reflecting {@{the system's intended behavior}@}.

### common mistakes: misusing use case generalization

{@{Misusing use-case generalization}@} often {@{occurs}@}.

\(__this course__: __Important__. Use case generalization is {@{easily misused}@}. Further, it is {@{not needed in the course}@}. So {@{don't use it}@}.\)

### common mistakes: IO as actors

{@{Input or output \(IO\) devices}@} are {@{_never_ actors}@}.

In the billing example, {@{the handheld device used by meter readers}@} is {@{occasionally labeled an actor}@}, despite being {@{merely a data entry tool}@}. The mistake stems from treating {@{any physical interface that can "perform" an action as an actor}@}, rather than recognizing {@{it as part of the human's interaction channel}@}. Fix this by documenting {@{such interfaces as system components or input devices}@}, {@{not actors}@}.

### common mistakes: nonfunctional requirements as use case

{@{_Non-functional requirements_}@} such as {@{"login", "10% discount", or "by email"}@} are {@{mistakenly modeled as ordinary use cases or part of them}@}. For example, in the movie shop example, {@{"by email"}@} should not be part of {@{use case functionality "receive overdue notice"}@};  that is, {@{how the notice is received}@} is {@{not important}@}. Another example is {@{"login"}@}, which is {@{a _security_ non-functional requirement}@}. It may be represented by {@{an _administration use case_}@} instead.

### common mistakes: wrong initiating actors

{@{The initiating actors of a use case}@} should be {@{the actor _outside_ the system}@} that {@{_directly_ interacts with the system}@}. A common example is {@{an actor acting on behalf of another person}@}; in such cases, {@{that other person should not be the initiating actor}@}. For example, if {@{a customer can buy a movie through an online system or via an employee}@}, there should be {@{two arrows pointing from customer and employee to "buy movie"}@} in {@{the use case diagram}@}, with the former for {@{buying via the online system}@} and the latter for {@{buying via an employee}@}.

### common mistakes: not using actor generalization

There is a tendency to {@{_duplicate functionality across actors_ without justification}@} and overlook {@{_actor hierarchy and role reuse_}@}. The requirement {@{"A sales clerk must look up customer information"}@} is sometimes drawn as {@{separate arrows to the same use case}@} for {@{every type of clerk \(e.g. cashier, manager\)}@}. In practice, {@{the same _Lookup Customer_ action}@} is {@{the same by any staff member}@}; UML encourages {@{such reuse}@} through {@{actor generalization}@} rather than {@{duplicating the association}@}. Failure to do so inflates {@{the diagram}@} and obscures the fact that {@{the operation is common across roles}@}.

However, as mentioned above in {@{redundant associations}@}, if {@{the sub-actor can perform _additional_ functionalities for the use case}@}, then {@{the association from the sub-actor to the same use case}@} is {@{_not_ redundant}@}.

### common mistakes: use case without initiating actors

A frequent source of confusion in {@{use case modeling and use case diagram}@} is the appearance of {@{a use case that has no clear initiating actor}@}. When a diagram shows {@{an isolated oval labeled}@}, for example, {@{"Prepare Bill" or "Produce Payment Report"}@}, yet none {@{of the surrounding actors}@} are {@{connected to it with a solid arrow}@} \(also includes {@{having only communication associations}@}\), readers immediately {@{wonder who starts this activity}@}. {@{This situation typically arises}@} when students translate {@{functional requirements verbatim into use-case names}@} without first asking {@{_who_ will trigger that action in the real system}@}.

The consequences of {@{leaving a use case uninitiated}@} are {@{twofold}@}. First, it breaks {@{the fundamental UML rule}@} that {@{every use case}@} must be {@{triggered by at least one actor}@}; otherwise the model becomes {@{ambiguous and incomplete}@}. Second, {@{such orphaned use cases}@} often indicate {@{an over-splitting of functionality}@}: the activity may {@{actually belong to another, already-identified use case}@}. For instance, {@{"Prepare Bill"}@} might simply be {@{a sub-step within "Bill Customer"}@}, or it could be part of {@{the overall billing workflow}@} that is initiated by {@{a meter reader's reading entry}@} \(so {@{"Enter Meter Reading"}@} can also be {@{merged into "Bill Customer"}@}\).

To {@{resolve this issue}@}, begin by reviewing {@{the business scenario for each orphaned use case}@} and asking {@{which actor ultimately performs the first step}@}. If {@{no external actor can initiate the action}@}, then the activity should likely be {@{merged into an existing use case that does have an initiator}@}. For example, if {@{"Produce Payment Report" is only ever invoked}@} after {@{some payments have been processed}@}, it makes sense to fold {@{"Produce Payment Report" into the broader "Process Payment" use case}@}.

When a use case appears to have {@{only communication associations}@}—such as {@{sending a message to another system component}@}—but {@{no direct actor link}@}, examine {@{the surrounding context}@} for {@{a higher-level use case that initiates the communication chain}@}. Often the communication is {@{merely a side effect of a larger transaction}@}. Merge {@{the isolated case into that parent use case}@} and represent {@{the communication as an internal step}@} or {@{a secondary activity within the merged use case}@}.

### common mistakes: missing nonfunctional requirements

{@{Nonfunctional requirements}@} (e.g. {@{performance, reliability, security}@}) should be represented {@{alongside functional ones}@}. Yet students often leave {@{these out of their use-case diagrams or class models}@}, resulting in {@{a specification that looks complete}@} but misses {@{critical quality attributes}@}. {@{The root cause}@} is {@{the misconception that UML only describes behaviour and structure}@}. To {@{fix this}@}, add {@{text describing nonfunctional requirements}@} to {@{the relevant use cases}@}; or {@{the entire system for whole-system requirements}@}.
