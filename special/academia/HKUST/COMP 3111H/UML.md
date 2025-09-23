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

- see: [general/Unified Modeling Language](../../../../general/Unified%20Modeling%20Language.md)

{@{__Unified Modeling Language__ \(__UML__\)}@} is {@{a general-purpose, object-oriented, visual modeling language}@} that provides {@{a way to visualize the architecture and design of a system}@}; like {@{a blueprint}@}. <!--SR:!2025-10-28,18,321!2025-10-26,16,302!2025-10-28,18,321!2025-10-27,17,302-->

## classes

{@{A _class_}@} represents {@{a _type_ of object in the application domain}@}. _Instances_ of a class have {@{_common_ attributes, operations, relations with other objects, and semantics}@}, which are {@{_classified_ by the class \(a _classifier_\)}@}. There can be {@{many instances of a class}@}. It can be considered as {@{a "factory" for creating new instances of it}@}. <!--SR:!2025-10-28,18,321!2025-10-27,17,302!2025-10-26,16,302!2025-10-27,17,302!2025-10-27,17,302!2025-10-28,18,330-->

A good class should {@{capture exactly one abstract object in the application domain}@}. It should have {@{one major theme \(not too general, no mixing of concepts\)}@}. {@{Abstract objects _outside_ the application domain}@}, e.g. {@{physical objects not represented by the digital system}@}, should {@{not be modeled at all}@}! An example is {@{physical passbooks issued by a bank}@}. They are {@{physical objects not represented by the bank's digital system}@}. They should be {@{excluded if you are only designing the digital system}@}. <!--SR:!2025-10-28,18,321!2025-10-26,16,302!2025-10-28,18,321!2025-10-28,18,321!2025-10-28,18,321!2025-10-25,15,302!2025-10-27,17,302!2025-10-26,16,302-->

A class is drawn by {@{a rectangle box with 3 sections \(from top to bottom\)}@}: {@{class name, attributes, and operations}@}. <!--SR:!2025-10-28,18,330!2025-10-27,17,302-->

{@{The _name_}@} of a class should be {@{_unique_ \(including classes and associations\)}@}, and uses {@{vocabularies according to the application domain}@}. <!--SR:!2025-10-28,18,321!2025-10-26,16,302!2025-10-26,16,302-->

### why classes

There are {@{many objects in the application domain}@}. Classes allow us to {@{_abstract_ a collection of objects}@} that {@{_share semantics_}@}. This reduce {@{development _complexity_}@} by allowing {@{better understanding and specification}@}. It is {@{an important _design decision_}@} that helps {@{promote _modular development_}@}. Note as {@{a design decision}@}, there is not {@{the single "correct" way to model a system}@}. <!--SR:!2025-10-27,17,302!2025-10-27,17,302!2025-10-28,18,321!2025-10-25,15,302!2025-10-27,17,302!2025-10-27,17,302!2025-10-26,16,302!2025-10-27,17,302!2025-10-28,18,321-->

{@{Better _understanding_}@} comes from {@{reduced complexity}@}, as {@{collections of many objects}@} become {@{a few classes}@}. We only need to understand {@{the class instead of the collection of objects \(instances\)}@}. <!--SR:!2025-10-24,14,290!2025-10-26,16,302!2025-10-28,18,330!2025-10-27,17,302!2025-10-28,18,321-->

{@{Better _specification_}@} comes from {@{UML requiring details of the classes}@}. These details provide {@{a _common_ place to define and store _common_ definitions exactly once}@}. <!--SR:!2025-10-28,18,330!2025-10-28,18,330!2025-10-28,18,321-->

## attributes

{@{An _attribute_}@} represents {@{a _data value_ held by the class}@}. It has {@{6 major properties \(and possibly more\)}@}: {@{name, type, visibility}@}, {@{initial value, multiplicity, and mutability}@}. <!--SR:!2025-10-28,18,321!2025-10-27,17,302!2025-10-28,18,330!2025-10-27,17,302!2025-10-28,18,330-->

{@{The _name_}@} of an attribute describes {@{the _semantics_ for the data value}@}. It should be {@{_unique_ \(including attributes and operations\) in a class}@}. For {@{modeling using the simplest possible model \(__this course__: may be used in this course\)}@}, it should {@{always be specified}@}. <!--SR:!2025-10-27,17,302!2025-10-28,18,321!2025-10-25,15,302!2025-10-28,18,321!2025-10-27,17,302-->

{@{The _type_}@} of an attribute describes {@{the _domain of values_ for the data value}@}, e.g. {@{integer, string, money, etc.}@} For {@{modeling using the simplest possible model \(__this course__: may be used in this course\)}@}, it should {@{always be specified}@}. <!--SR:!2025-10-26,16,302!2025-10-27,17,302!2025-10-27,17,302!2025-10-28,18,330!2025-10-25,15,302-->

{@{The _visibility_}@} of an attribute describe {@{who can _access_ the data value}@}. In {@{Java}@}, there are {@{4 visibilities \(in order of decreasing visibility\)}@}: {@{public \(all classes\), protected \(additionally, subclasses\), package-local \(additionally, classes in the same package\), and private \(the class itself\)}@}. They are respectively represented by the symbols {@{`+`, `#`, `~`, and `-`}@}. <!--SR:!2025-10-27,17,302!2025-10-25,15,302!2025-10-28,18,321!2025-10-25,15,302!2025-10-28,18,321!2025-10-24,14,290-->

{@{The _initial value_}@} of an attribute describe {@{the initial value for the data value if _unspecified_}@}. It is {@{_optional_}@}, and by default {@{requires the data value to be _specified_ since there is no initial value}@}. <!--SR:!2025-10-28,18,330!2025-10-28,18,330!2025-10-28,18,321!2025-10-28,18,321-->

{@{The _multiplicity_}@} of an attribute describe {@{how many _simultaneous values_ the data value can take}@}. It is {@{_optional_}@}, and by default {@{is 1}@}. <!--SR:!2025-10-27,17,302!2025-10-28,18,321!2025-10-27,17,302!2025-10-27,17,302-->

{@{The _mutability_ \(_changeability_\)}@} of attribute describe {@{if the data value can be changed}@}. It can be {@{writable \(_unspecified_\) or read-only \(`readOnly`\)}@}. By default, it is {@{writable as it is unspecified}@}. <!--SR:!2025-10-28,18,330!2025-10-28,18,330!2025-10-28,18,321!2025-10-28,18,321-->

{@{The syntax}@} to {@{describe an attribute}@} is {@{`<visibility> <name> : <type> = <initial value>`}@}. <!--SR:!2025-10-27,17,302!2025-10-28,18,321!2025-10-28,18,321-->

## operations

{@{An _operation_}@} represents {@{a _function_ or _transformation_ that can be applied to or by instances of the class}@}. It has {@{4 major properties \(and possibly more\)}@}: {@{operation name, parameter names, result type, and visibility}@}. {@{The first 3 properties}@} is known as {@{the _operation signature_}@}. For {@{modeling using the simplest possible model \(__this course__: may be used in this course\)}@}, the operation signature should {@{always be specified}@}. <!--SR:!2025-10-27,17,302!2025-10-28,18,330!2025-10-28,18,321!2025-10-28,18,321!2025-10-28,18,321!2025-10-25,15,302!2025-10-28,18,330!2025-10-25,15,302-->

{@{An instance of an operation}@} is called {@{a _method_}@}. This matters because there {@{can be several methods implementing the same operation \(a _polymorphic_ operation\)}@}. One way to do this is via {@{_overriding_ to achieve _polymorphism_}@}. <!--SR:!2025-10-28,18,321!2025-10-27,17,302!2025-10-28,18,321!2025-10-28,18,321-->

{@{The _operation name_}@} of an operation describes {@{the _semantics_ of the operation}@}. It should be {@{_unique_ \(including attributes and operations\) in a class}@}. For {@{modeling using the simplest possible model \(__this course__: may be used in this course\)}@}, it should {@{always be specified}@}. <!--SR:!2025-10-24,14,290!2025-10-27,17,302!2025-10-27,17,302!2025-10-28,18,321!2025-10-28,18,321-->

{@{The _parameter names_}@} of an operation describe {@{the _semantics_ of the _arguments_ \(inputs\) to the operation}@}. They should be {@{_unique_ in an operation}@}. For {@{modeling using the simplest possible model \(__this course__: may be used in this course\)}@}, it should {@{always be specified}@}. It can be {@{empty for no arguments}@}. <!--SR:!2025-10-27,17,302!2025-10-28,18,321!2025-10-28,18,321!2025-10-27,17,302!2025-10-28,18,321!2025-10-28,18,321-->

{@{The _return type_}@} of an operation describe {@{the _domain of values_ the operation can return}@}, e.g. {@{integer, string, money, etc.}@} If {@{no return value \(`void`\)}@}, {@{omit it}@}. For {@{modeling using the simplest possible model \(__this course__: may be used in this course\)}@}, it should {@{always be specified \(because omitting it implies no return value \(`void`\)\)}@}. <!--SR:!2025-10-26,16,302!2025-10-28,18,321!2025-10-27,17,302!2025-10-27,17,302!2025-10-28,18,321!2025-10-28,18,330!2025-10-28,18,321-->

{@{The _visibility_}@} of an operation describe {@{who can _use_ the operation}@}. In {@{Java}@}, there are {@{4 visibilities \(in order of decreasing visibility\)}@}: {@{public \(all classes\), protected \(additionally, subclasses\), package-local \(additionally, classes in the same package\), and private \(the class itself\)}@}. They are respectively represented by the symbols {@{`+`, `#`, `~`, and `-`}@}. <!--SR:!2025-10-28,18,321!2025-10-26,16,302!2025-10-26,16,302!2025-10-20,10,270!2025-10-25,15,302!2025-10-28,18,321-->

{@{The syntax}@} to {@{describe an operation}@} is {@{`<visibility> <name>(<parm name 1>, ..., <parm name N>) : <return type>`}@}. <!--SR:!2025-10-28,18,321!2025-10-28,18,330!2025-10-27,17,302-->

## associations

{@{An _association_ \(a _classifier_\)}@} _classifies_ {@{a collection of links with _common semantics_}@}. {@{A _link_}@} is {@{a _relation_ between objects \(of different classes or the same class\)}@}, and is an _instance_ of {@{an association}@}. They are {@{_bidirectional_}@}, so {@{no arrowhead is needed}@}. You can {@{still add it}@} to show {@{the _navigability_ of association \(the object at the tail _references_ that at the arrowhead\)}@}, making the association {@{_unidirectional_}@}. <!--SR:!2025-10-24,14,290!2025-10-28,18,321!2025-10-28,18,321!2025-10-25,15,302!2025-10-27,17,302!2025-10-28,18,321!2025-10-28,18,330!2025-10-28,18,321!2025-10-26,16,302!2025-10-28,18,321-->

{@{Multiple associations}@} between {@{the same set of objects}@} are {@{allowed if they have _different semantics_}@}. Avoid associations that have semantics that are {@{simply the _composition_ of two associations}@}. For example, if there are {@{two associations `C ? -IsChild- ? B` and `B ? -IsChild- ? A`}@}, there is no need to {@{add the association `C ? -IsChild- ? A`}@}, but it would be okay to {@{add the association `C ? -IsFriend- ? A` because this association has a different meaning}@}. <!--SR:!2025-10-24,14,290!2025-10-25,15,302!2025-10-26,16,302!2025-10-28,18,321!2025-10-27,17,302!2025-10-28,18,321!2025-10-26,16,302-->

Associations have {@{6 major properties \(and possibly more\)}@}: {@{name, degree, multiplicity}@}, {@{roles, additional semantics, and class}@}. <!--SR:!2025-10-28,18,321!2025-10-28,18,321!2025-10-28,18,333-->

{@{The _name_}@} of an association should be {@{_unique_ \(including classes and associations\)}@}, and uses {@{vocabularies according to the application domain}@}. Normally, the name can {@{only be _read meaningfully_ in one direction}@}, and the name for {@{the other direction is _inferred_}@}. <!--SR:!2025-10-27,17,302!2025-10-28,18,321!2025-10-25,15,302!2025-10-28,18,321!2025-10-28,18,321-->

An association is drawn by {@{a line connecting the class to itself \(unary\)}@}, {@{a line between two classes \(binary\)}@}, or {@{a diamond shape connecting many classes \(ternary, etc.\)}@}. \(__this course__: We consider {@{unary and binary associations only}@}.\) <!--SR:!2025-10-28,18,330!2025-10-25,15,290!2025-10-25,15,302!2025-10-28,18,333-->

### association degree

{@{The _degree_}@} of an association is {@{the number of _distinct_ classes the association relates to}@}. {@{A single class}@} is {@{_unary_}@}. {@{Two classes}@} are {@{_binary_}@}. {@{Three classes}@} are {@{_ternary_}@}. There are {@{other words for higher degrees}@}. <!--SR:!2025-10-25,15,302!2025-10-28,18,330!2025-10-27,17,302!2025-10-27,17,302!2025-10-28,18,321!2025-10-28,18,321!2025-10-28,18,330!2025-10-28,18,330!2025-10-27,17,302-->

In practice, most associations are {@{binary}@}. A few are {@{unary}@}, and even fewer are {@{ternary or higher degree}@}. Often, {@{a ternary or higher degree association}@} can be {@{replaced by multiple binary associations}@}, but {@{not always}@}. <!--SR:!2025-10-28,18,330!2025-10-27,17,302!2025-10-25,15,302!2025-10-28,18,321!2025-10-28,18,330!2025-10-28,18,321-->

Associations of {@{different degree}@} are {@{drawn differently}@}. An association is drawn by {@{a line connecting the class to itself \(unary\)}@}, {@{a line between two classes \(binary\)}@}, or {@{a diamond shape connecting many classes \(ternary, etc.\)}@}.  \(__this course__: We consider {@{unary and binary associations only}@}.\) <!--SR:!2025-10-27,17,302!2025-10-24,14,290!2025-10-28,18,321!2025-10-26,16,302!2025-10-28,18,330!2025-10-28,18,333-->

### association multiplicity

{@{A _multiplicity_}@} of an association is {@{the possible numbers of the association that an instance of the _current_ class may be related to}@}. It is an {@{_application domain_}@} constraint. Note that this is written on {@{the side of the _other_ class rather than the current class}@}. This should not be confused with {@{how multiplicity is placed}@} on {@{the entity–relationship model \(ER model\)}@}, which is {@{commonly used for databases}@}. <!--SR:!2025-10-27,17,302!2025-10-28,18,321!2025-10-26,16,302!2025-10-28,18,330!2025-10-28,18,321!2025-10-24,14,290!2025-10-28,18,321-->

To {@{specify multiplicity}@}, specify {@{the _minimum cardinality_ \(min count\) and _maximum cardinality_ \(max count\)}@} on {@{the _other_ class \(not the _current_ class\)}@}. Both are {@{inclusive}@}. {@{_Cardinality_}@} can be {@{any _nonnegative_ integer}@}, or {@{the special wildcard `*` representing infinity}@}. Then, write it using {@{`<min card>..<max card>`}@}. There are {@{shorthands for some multiplicities}@}: <!--SR:!2025-10-28,18,321!2025-10-28,18,330!2025-10-28,18,330!2025-10-25,15,302!2025-10-28,18,330!2025-10-27,17,302!2025-10-26,16,302!2025-10-27,17,302!2025-10-28,18,330-->

- `1` ::@:: `1..1` <!--SR:!2025-10-28,18,330!2025-10-28,18,321-->
- `*` ::@:: `0..*` <!--SR:!2025-10-27,17,302!2025-10-28,18,321-->

When {@{minimum cardinality is 0}@}, this means {@{participation of instances of the other class is _optional_}@}. Otherwise \({@{minimum cardinality is greater than 0}@}\), this means {@{participation of instances of the other class is _mandatory_}@}. Often, there are application domains in which {@{it is not clear if participation of the other class should be optional or mandatory}@}. It may be {@{arbitrary and is simply a matter of taste \(design decision\)}@}. It may also be due to {@{underspecification by the client}@}, and requires {@{further questioning the client}@} to resolve. <!--SR:!2025-10-26,16,302!2025-10-26,16,302!2025-10-28,18,321!2025-10-27,17,302!2025-10-25,15,302!2025-10-28,18,330!2025-10-27,17,302!2025-10-28,18,321-->

In practice, there are {@{"multiplicities" that are _soft_ constraints}@}. We {@{do not use them as multiplicities}@}, because multiplicities are {@{_hard_ constraints that _must_ be followed at _all times_}@}. For example, {@{a student}@} is {@{required to enroll into at least 5 courses}@}. However, the model should {@{still use `*` instead of `5..*` for the multiplicity}@}, because when {@{creating a student needs to be created first}@}, and {@{we cannot automatically determine the 5 courses to enroll}@}. So the above constraint is {@{a soft constraint}@}. To express it, we should {@{write a brief text description next to the _hard_ multiplicity}@}. <!--SR:!2025-10-28,18,321!2025-10-28,18,321!2025-10-28,18,330!2025-10-28,18,330!2025-10-28,18,330!2025-10-28,18,321!2025-10-25,15,302!2025-10-25,15,302!2025-10-28,18,321!2025-10-28,18,321-->

### association roles

{@{A _role_}@} of an association is {@{one _end_ of an association}@}. It describes {@{the _semantics_ of a class participating in the association}@}. It is written on {@{the side of the _current_ class}@}. It is usually {@{_optional_ for binary associations}@}, and always {@{_required_ for unary associations}@}. <!--SR:!2025-10-25,15,302!2025-10-26,16,302!2025-10-27,17,302!2025-10-28,18,321!2025-10-27,17,302!2025-10-25,15,302-->

{@{The _name_}@} of a role should be {@{_unique_ in an association}@}. <!--SR:!2025-10-27,17,302!2025-10-28,18,330-->

### association with additional semantics

An association can {@{have additional semantics}@}. {@{The most general way}@} to specify additional semantics is by {@{writing a piece of text next to the association}@}. <!--SR:!2025-10-28,18,321!2025-10-26,16,302!2025-10-28,18,321-->

However, there are {@{some additional semantics common enough}@} to {@{warrant special representations}@}. There are {@{3 major ones}@}: {@{aggregation, composition, and generalization}@}. <!--SR:!2025-10-26,16,302!2025-10-25,15,302!2025-10-27,17,302!2025-10-26,16,302-->

### association aggregations

{@{_Aggregation_}@} represents {@{a _possible_ "part-of" relationship}@}. {@{The component object \(child\)}@} {@{_may_ belong to an aggregate object \(parent\)}@}, and {@{_can_ exist _independently_ of the aggregate object}@}. <!--SR:!2025-10-25,15,302!2025-10-27,17,302!2025-10-28,18,330!2025-10-28,18,321!2025-10-28,18,330-->

Often, the association name is {@{"Has", but can be other names as appropriate for the application domain}@}. We can {@{omit the name as well}@}. Conversely, however, {@{an association with the name "Has"}@} {@{does not imply composition}@}. Aggregation or composition should have {@{intrinsic _asymmetry_ to the association}@}. <!--SR:!2025-10-28,18,330!2025-10-25,15,302!2025-10-28,18,330!2025-10-25,15,302!2025-10-28,18,333-->

In many cases, {@{whether an aggregation \(or composition\)}@} should be used is {@{unclear, and is mostly a matter of taste \(design decision\)}@}. When {@{in doubt}@}, use {@{a pure association}@}. <!--SR:!2025-10-28,18,333!2025-10-28,18,333!2025-10-28,18,333!2025-10-28,18,333-->

To {@{represent aggregation}@}, use {@{a _hollow_ diamond \(_adornment_\) at the end of the aggregate object \(child\)}@}. Multiplicity can be {@{omitted if the cardinality range is `0..1`}@}. In some cases, you may want to specify {@{`0..*` as the multiplicity}@}. <!--SR:!2025-10-28,18,321!2025-10-28,18,321!2025-10-28,18,330!2025-10-24,14,290-->

### association compositions

{@{_Composition_}@} represents {@{a _mandatory_ "part-of" relationship}@}. {@{The component object \(child\)}@} {@{_must_ belong to an aggregate object \(parent\)}@}, and {@{_cannot_ exist _independently_ of the aggregate object}@}. <!--SR:!2025-10-28,18,330!2025-10-27,17,302!2025-10-26,16,302!2025-10-25,15,302!2025-10-26,16,302-->

Often, the association name is {@{"Has", but can be other names as appropriate for the application domain}@}. We can {@{omit the name as well}@}. Conversely, however, {@{an association with the name "Has"}@} {@{does not imply composition}@}. Aggregation or composition should have {@{intrinsic _asymmetry_ to the association}@}. Composition should also have {@{operations applied to the whole that should also be applied to its parts}@}, e.g. {@{destroying the whole object _requires_ destroying its parts}@}. <!--SR:!2025-10-28,18,330!2025-10-28,18,321!2025-10-28,18,330!2025-10-28,18,321!2025-10-27,17,302!2025-10-28,18,321!2025-10-28,18,333-->

In many cases, {@{whether a composition \(or aggregation\)}@} should be used is {@{unclear, and is mostly a matter of taste \(design decision\)}@}. When {@{in doubt}@}, use {@{a pure association}@}. <!--SR:!2025-10-28,18,333!2025-10-28,18,333!2025-10-28,18,333!2025-10-28,18,333-->

To {@{represent composition}@}, use {@{a _solid_ diamond \(_adornment_\) at the end of the aggregate object \(child\)}@}. Multiplicity can be {@{omitted if the cardinality range is `1..1`}@}. In some cases, you may want to specify {@{`1..*` as the multiplicity}@}. <!--SR:!2025-10-28,18,321!2025-10-26,16,302!2025-10-27,17,302!2025-10-28,18,321-->

### association generalizations

{@{_Generalization_}@} represent {@{a "is-a" or "kind-of" relationship between _subclasses_ and a _superclass_}@}. The subclasses are said to be {@{the _same kind_}@}, and should have {@{_similar_ \(but not the same\) attributes, operations, and associations}@}. It is represented by {@{_inheritance_ in object-oriented programming languages}@}. It allows us to {@{_simplify_ diagrams for _clarity_}@}. <!--SR:!2025-10-27,17,302!2025-10-25,15,302!2025-10-27,17,302!2025-10-28,18,330!2025-10-27,17,302!2025-10-28,18,330-->

To {@{construct a generalization}@}, we have {@{top-down and bottom-up}@} approaches. Both can be {@{used together}@}. <!--SR:!2025-10-27,17,302!2025-10-28,18,321!2025-10-28,18,330-->

In {@{the top-down approach}@}, we start with {@{a class with an _discriminator_ attribute}@}, which contains {@{an _enumeration type_}@} to indicate {@{the which other attributes or operations are valid}@} for {@{a particular instance of the class}@}. Then, we {@{generalize the superclass}@}: {@{add a new subclass for each possible value of the discriminator attribute}@}, and {@{remove the discriminator attribute from the superclass}@}. {@{Each subclass}@} should have attributes and operations that are {@{_specific_ \(non-common\) to the subclass}@}. {@{The superclass}@} should only have {@{attributes and operations _common_ to all subclasses}@}. Finally, indicate that {@{it is a generalization \(see below\)}@}. <!--SR:!2025-10-28,18,330!2025-10-28,18,330!2025-10-25,15,302!2025-10-28,18,321!2025-10-28,18,321!2025-10-26,16,302!2025-10-27,17,302!2025-10-25,15,302!2025-10-28,18,321!2025-10-27,17,302!2025-10-28,18,321!2025-10-28,18,321!2025-10-28,18,321-->

In {@{the bottom-up approach}@}, we start with {@{several classes with similar attributes or operations}@}. Then, we {@{generalize the subclasses}@}: {@{add a superclass with attributes or operations _common_ to all subclasses}@}, and {@{remove them from all subclasses}@}. Finally, indicate that {@{it is a generalization \(see below\)}@}. {@{_Common_ associations}@} may {@{have objects they are referring to changed}@} and {@{their multiplicity changed}@}. <!--SR:!2025-10-28,18,321!2025-10-24,14,290!2025-10-28,18,321!2025-10-26,16,302!2025-10-27,17,302!2025-10-28,18,321!2025-10-28,18,321!2025-10-27,17,302!2025-10-25,15,302-->

To {@{indicate a generalization}@}, {@{connect all subclasses}@} to {@{the superclass}@}, and {@{add a _hollow_ triangle pointing towards the superclass}@}. {@{Generalization properties}@} are described by {@{text near it}@}, e.g. {@{`{overlapping, incomplete}`, `{disjoint, complete}`}@}. <!--SR:!2025-10-28,18,321!2025-10-27,17,302!2025-10-28,18,321!2025-10-24,14,290!2025-10-28,18,321!2025-10-28,18,321!2025-10-28,18,321-->

#### generalization and inheritance

As mentioned above, {@{generalization}@} is represented by {@{_inheritance_ in object-oriented programming languages}@}. {@{_Inheritance_}@} is {@{inheriting attributes, operations, and relations of a superclass by its subclasses}@}. A subclass can either {@{_add_ new attributes, operations, and relations}@} \({@{indicated}@} in the subclasses\); or {@{_override_ attributes, operations, and relations already defined by a _direct_ or _indirect_ superclass}@} \({@{not indicated}@} in the subclasses\). {@{_Common_ associations on subclasses}@} may be {@{replaced by a single association on the superclass}@}. Note {@{its _multiplicity_}@} may {@{need to be modified}@} to {@{_summarize_ the common associations \(should accommodate them all\)}@} and have {@{an additional text description next to it}@} to {@{describe any semantics \(e.g. different multiplicities\) not carried to the single association}@}. <!--SR:!2025-10-25,15,302!2025-10-25,15,302!2025-10-24,14,290!2025-10-28,18,321!2025-10-28,18,330!2025-10-28,18,321!2025-10-28,18,321!2025-10-26,16,302!2025-10-25,15,302!2025-10-28,18,321!2025-10-28,18,330!2025-10-28,18,321!2025-10-28,18,321!2025-10-28,18,330!2025-10-28,18,330-->

This allows us to {@{_simplify_ diagrams for _clarity_}@}, because {@{common attributes, operations, and relations}@} are {@{only defined in one class}@} rather than {@{duplicated over multiple classes}@}. This helps with {@{modifiability \(maintainability\), redundancy, and reusability}@}. <!--SR:!2025-10-28,18,321!2025-10-27,17,302!2025-10-28,18,330!2025-10-28,18,321!2025-10-28,18,321-->

{@{Most programming languages}@} support {@{_single inheritance_}@}, in which {@{a class can only have at most one _direct_ superclass}@}. {@{A few programming languages}@} support {@{_multiple inheritance_}@}, in which {@{a class can have multiple _direct_ superclasses}@}. <!--SR:!2025-10-27,17,302!2025-10-27,17,302!2025-10-26,16,302!2025-10-27,17,302!2025-10-27,17,302!2025-10-27,17,302-->

\(__this course__: We only consider {@{_single inheritance_ but not _multiple inheritance_}@}.\) <!--SR:!2025-10-25,15,302-->

#### generalization properties

{@{Generalization}@} can be characterized by {@{2 main properties \(and possibly more\)}@}: {@{_completeness_ and _disjointness_}@}. These two are also called {@{_coverage constraints_}@}. These depend on {@{the semantics of the superclass and subclasses}@} and {@{the _application domain_}@} \(e.g. {@{the exact same generalization in different domains may have different properties}@}\). <!--SR:!2025-10-28,18,321!2025-10-28,18,321!2025-10-28,18,330!2025-10-28,18,321!2025-10-28,18,321!2025-10-26,16,302!2025-10-28,18,321-->

{@{_Disjointness_}@} refers to {@{whether an instance of a superclass is also an instance of _at most_ one subclass}@}. A {@{_disjoint_ generalization}@} is {@{one where all instances of a superclass is also an instance of _at most_ one subclass}@}. Its opposite is {@{_overlapping_}@}, in which {@{there are instances of a superclass that are also instances of _multiple_ subclasses}@}. <!--SR:!2025-10-27,17,302!2025-10-27,17,302!2025-10-28,18,321!2025-10-28,18,330!2025-10-28,18,321!2025-10-27,17,302-->

{@{_Completeness_}@} refers to {@{whether an instance of a superclass must be an instance of a subclass \(i.e. _indirect_\)}@}. A {@{_complete_ generalization}@} is {@{one where all instances of a superclass is an instance of \(_at least_\) one subclass \(i.e. only _indirect_ instances of the superclass can exist\)}@}. Its opposite is {@{_incomplete_}@}, in which {@{there may be _direct_ instances of a superclass that are not instances of any subclasses \(i.e. _direct_ instances of the superclass can exist\)}@}. <!--SR:!2025-10-28,18,330!2025-10-28,18,321!2025-10-27,17,302!2025-10-25,15,302!2025-10-25,15,302!2025-10-28,18,321-->

{@{These properties}@} are described by {@{text near the generalization}@}, e.g. {@{`{overlapping, incomplete}`, `{disjoint, complete}`}@}. <!--SR:!2025-10-27,17,302!2025-10-27,17,302!2025-10-28,18,330-->

### association classes

{@{Most attributes}@} clearly {@{belongs to a class}@}. However, there are attributes that {@{do not clearly belong to a class}@}, but {@{rather to associations}@}. It is often needed in {@{many-to-many associations}@}. <!--SR:!2025-10-26,16,302!2025-10-27,17,302!2025-10-28,18,321!2025-10-28,18,321!2025-10-28,18,321-->

There are {@{4 major solutions}@}: {@{many attributes in a class, multi-valued attributes in a class, association class, or separate class}@}. The {@{first 2 solutions}@} {@{do not work \(1st solution: unknown number of attributes; 2nd solution: unknown mapping to links\)}@}, and {@{should not be used}@}. {@{The latter 2 solutions}@} are {@{fine depending on the _application domain_}@}. The 4th solution is {@{applicable to more situations than the 3rd solution}@} since {@{there cannot be multiple links of the same association between the same two objects}@}. <!--SR:!2025-10-28,18,321!2025-10-25,15,302!2025-10-26,16,302!2025-10-25,15,302!2025-10-28,18,330!2025-10-28,18,321!2025-10-28,18,330!2025-10-26,16,302!2025-10-28,18,321-->

{@{An _association class_}@} is {@{a class used to represent an association}@}. To represent it, you need to use {@{dashed line to connect the association with the association class}@}. <!--SR:!2025-10-28,18,321!2025-10-28,18,321!2025-10-27,17,302-->

## abstract entities

{@{_Abstract entities_}@} are {@{entities created for _modeling_ purposes}@} that {@{do not have _direct_ instances of it}@}. It can be applied to {@{classes and operations}@}. <!--SR:!2025-10-28,18,321!2025-10-28,18,330!2025-10-26,16,302!2025-10-27,17,302-->

{@{An _abstract class_}@} is {@{a class with no _direct_ instances}@}. {@{Its name}@} is {@{_italicized_}@}. A special type of abstract class is {@{an _interface_}@}, which is {@{an _abstract class_ with _operations_ only}@}. <!--SR:!2025-10-25,15,302!2025-10-28,18,321!2025-10-28,18,321!2025-10-27,17,302!2025-10-28,18,321!2025-10-27,17,302-->

{@{An _abstract operation_}@} is {@{an operation with no _direct_ method \(_direct_ implementation\)}@}. {@{Its name}@} is {@{_italicized_}@}. <!--SR:!2025-10-28,18,330!2025-10-25,15,302!2025-10-28,18,330!2025-10-27,17,302-->

## constraints

{@{A _constraint_}@} is {@{an _assertion_ about properties of model elements}@} that {@{must be satisfied at all times \(i.e. they are _hard_ constraints\)}@}. It should be {@{_testable_ \(returns true or false\)}@} and {@{_enforceable_ by the system implementation}@}. <!--SR:!2025-10-26,16,302!2025-10-26,16,302!2025-10-27,17,302!2025-10-26,16,302!2025-10-28,18,330-->

An {@{_attribute constraint_}@} constrains {@{an _attribute_ of a class}@}. It can be indicated by {@{`{<boolean expr>}` next to the attribute or on a note linked with the class by a dashed line}@}, which represents {@{an expression that must always be true}@}, e.g. {@{`balance: money {balance >= 100}`}@}. <!--SR:!2025-10-27,17,302!2025-10-26,16,302!2025-10-28,18,321!2025-10-28,18,321!2025-10-28,18,321-->

An {@{_operation constraint_}@} constrains {@{an _operation_ of a class}@}. It can be indicated by {@{`{<boolean expr>}` next to the operation or on a _note_ linked with the class by a _dashed_ line}@}, which represents {@{an expression that must always be true}@}, e.g. {@{`balance(): money {balance() >= 100}`}@}. <!--SR:!2025-10-26,16,302!2025-10-28,18,330!2025-10-28,18,321!2025-10-28,18,321!2025-10-28,18,321-->

An {@{_association constraint_}@} constrains {@{an _association_}@}. It can involve {@{one association only}@}, which is indicated by {@{`{<constraint 1>, ..., <constraint N>}` next to the association}@}. It can involve {@{multiple associations}@}, which is indicated by {@{a _dashed line_ with text like `{<constraint 1>, ..., <constraint N>}` next to it}@}. Some constraints {@{make the _dashed line_ a _dashed arrow_ instead}@}. Example association constraints include: <!--SR:!2025-10-28,18,321!2025-10-25,15,290!2025-10-27,17,302!2025-10-25,15,302!2025-10-28,18,330!2025-10-28,18,330!2025-10-28,18,321-->

- association constraint: ordering ::@:: `{ordered, FIFO}`, `{ordered, LIFO}`, etc.; for one association <!--SR:!2025-10-27,17,302!2025-10-27,17,302-->
- association constraint: subset ::@:: `{subset}`; the specialized \(subset\) association has a _dashed arrow_ towards the general \(superset\) association <!--SR:!2025-10-27,17,302!2025-10-27,17,302-->
- association constraint: xor ::@:: `{xor}`; a _dashed line_ linking two associations; exactly one of the two associations can be _instantiated_ \(have _instances_ or _links_\) <!--SR:!2025-10-28,18,321!2025-10-27,17,302-->

For {@{constraints in general}@}, UML provides {@{a text-based _formal_ constraint specification language}@} called {@{_Object Constraint Language \(OCL\)_}@}, similar to {@{C++ or Java}@}. \(__this course__: {@{not covered}@}\) <!--SR:!2025-10-27,17,302!2025-10-26,16,302!2025-10-27,17,302!2025-10-27,17,302!2025-10-27,17,302-->

## dependencies

{@{A _dependency_}@} relates {@{classes whose behavior or implementation affect other classes}@}. It is indicated by {@{a _dashed arrow_}@}. Some example dependencies are: {@{_flow_ and _usage_}@}. <!--SR:!2025-10-26,16,302!2025-10-28,18,321!2025-10-28,18,321!2025-10-27,17,302-->

- flow ::@:: An instance of some class may become another class later. The dashed arrow points from the old class to the new class. <!--SR:!2025-10-26,16,302!2025-10-27,17,302-->
- usage ::@:: A class may require another class for its correct functioning. The dashed arrow points from the dependant \(requires\) to the dependency \(required by\). <!--SR:!2025-10-25,15,302!2025-10-24,14,290-->

## realizations

{@{A _realization_}@} relates {@{an _implementation_ to its _specification_}@}, e.g. {@{relating an class implementing an interface to the interface}@}. It is indicated by {@{a _dashed arrow_ with a _hollow_ triangle as the arrow head}@}. It points from {@{the implementation to the specification}@}. <!--SR:!2025-10-28,18,321!2025-10-27,17,302!2025-10-28,18,330!2025-10-28,18,321!2025-10-28,18,321-->
