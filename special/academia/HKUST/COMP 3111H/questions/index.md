---
aliases:
  - COMP 3111H question
  - COMP 3111H questions
  - COMP3111H question
  - COMP3111H questions
  - HKUST COMP 3111H question
  - HKUST COMP 3111H questions
  - HKUST COMP3111H question
  - HKUST COMP3111H questions
tags:
  - flashcard/active/special/academia/HKUST/COMP_3111H/questions
  - language/in/English
---

# questions

- HKUST COMP 3111H

## children

- [quiz 1](quiz%201.md)
- [quiz 2](quiz%202.md)
- [quiz 3](quiz%203.md)
- [quiz 4](quiz%204.md)
- [quiz 5](quiz%205.md)
- [quiz 6](quiz%206.md)
- [quiz 7](quiz%207.md)
- [quiz 8](quiz%208.md)
- [quiz 9](quiz%209.md)
- [quiz 10](quiz%2010.md)
- [quiz 11](quiz%2011.md)
- [quiz 12](quiz%2012.md)
- [quiz 13](quiz%2013.md)
- [quiz 14](quiz%2014.md)
- [quiz 15](quiz%2015.md)
- [quiz 16](quiz%2016.md)
- [quiz 17](quiz%2017.md)
- [quiz 18](quiz%2018.md)
- [quiz 19](quiz%2019.md)
- [quiz 20](quiz%2020.md)

## week 1 lecture

\(none\)

## week 2 pre-lecture

> In a course registration system, there are students and courses.
>
> A student must be in 1 to 5 courses. A course must have 10 to 50 students.
>
> What should be the _multiplicities_ of the `Student ? -EnrollsIn- ? Course` relation?
>
> ---
>
> - solution: {@{`Student 0..50 -EnrollsIn- 0..5 Course`. Add notes next to the multiplicities to indicate the minimum counts instead.}@}
> - explanation: {@{Multiplicities are _hard_ constraints that must be followed at all times. <p> Consider creating a student or a course. There is no _natural_ way to associate courses to a student or students to a course. So we must allow 0 when creating a student or a course. The notes next to the multiplicities are meant to fill in the _missing_ semantics.}@} <!--SR:!fsrs,2030-01-11T00:00:00.000Z,1195,1195.07164214,1,2,9,0,0,2026-10-04T00:00:00.000Z!fsrs,2029-12-29T00:00:00.000Z,1184,1183.64577796,1,2,9,0,0,2026-10-02T00:00:00.000Z-->

---

> Fill in the missing multiplicities using _common sense_
>
> 1. `Customer ? -Makes- ? Shipment`
> 2. `Shipment ? -Contains- ? Package`
> 3. `Shipment ? -SentTo- ? City`
>
> ---
>
> - solution: {@{1. `Customer 1 -Makes- * Shipment` <br/> 2. `Shipment 1 -Contains- 1..* Package` <br/> 3. `Shipment * -SentTo- 1 City`}@}
> - annotation: {@{There are other possible multiplicities according to the _application domain_.}@} <!--SR:!2028-06-23,753,330!fsrs,2029-08-25T00:00:00.000Z,1096,1095.51488793,1,2,9,0,0,2026-08-25T00:00:00.000Z-->

---

> Given the following association: `Student ? -EnrollsIn- ? Course`, how to put an enrollment attribute, e.g. grade? There may be multiple enrollments for a pair of a `Student` instance and a `Course` instance, e.g. retaking a course due to failing the previous pre-enrollment.
>
> ---
>
> - solution: {@{Use a _new separate class_ replacing the association. The new class is associated with `Student` and `Course`.}@}
> - annotation: {@{An _association class_ would have worked if multiple enrollments were impossible.}@} <!--SR:!fsrs,2029-08-14T00:00:00.000Z,1088,1087.80493378,1,2,9,0,0,2026-08-22T00:00:00.000Z!fsrs,2030-01-16T00:00:00.000Z,1199,1198.87680538,1,2,9,0,0,2026-10-05T00:00:00.000Z-->

---

> Characterize the following generalizations using _common sense_.
>
> 1. payment \(can be a mix of payment methods\): cash, credit card, debit card
> 2. package: box, envelope, pak, tube
> 3. bank account: business, personal
> 4. course: undergraduate, postgraduate
> 5. student: undergraduate, postgraduate
>
> ---
>
> - solution: {@{1. overlapping, incomplete <br/> 2. disjoint, incomplete <br/> 3. disjoint, complete <br/> 4. overlapping, complete <br/> 5. disjoint, complete}@}
> - annotation: {@{There are other possible answers according to the _application domain_.}@} <!--SR:!fsrs,2029-06-30T00:00:00.000Z,1053,1053.01305103,1,2,9,0,0,2026-08-12T00:00:00.000Z!2026-10-11,280,330-->

## week 2 lecture

> Can association names be the same?
>
> ---
>
> - solution: {@{No. Each association must have an unique name.}@} <!--SR:!2026-12-05,323,340-->

---

> What attributes relating to other classes with associations should be replaced?
>
> ---
>
> - solution: {@{Obviously, ID attributes used to refer to instances of other classes should be removed. But attributes that can be inferred from instances of the association \(or through multiple associations\) should also be removed, e.g. type of the referred instance of other classes.}@} <!--SR:!2026-12-12,330,340-->

---

> Should you ignore classes or associations stated in the requirements?
>
> ---
>
> - solution: {@{No. Stick to user requirements as closely as possible. However, if the entity described by the requirements is outside the scope of the system, you should ignore it.}@} <!--SR:!2026-11-10,310,340-->

---

> Should you add extra classes or associations not stated in the requirements?
>
> ---
>
> - solution: {@{No. Stick to user requirements as closely as possible. Do not be creative.}@} <!--SR:!2026-11-16,304,340-->

---

> Should associations that have meanings that are obtainable by composing two or more associations kept?
>
> ---
>
> - solution: {@{No. This helps to simplify the diagram. However, this simplification can only be done when the meaning \(semantics\) of the redundant association is obtainable by composing the meanings of two or more associations.}@} <!--SR:!2026-11-01,301,340-->

---

> What should you do if there are semantics that cannot be represented by standard UML diagram elements?
>
> ---
>
> - solution: {@{Add a small note next to the relevant place with text describing the semantics. This could come in handy for examinations, e.g. stating your less-than-obvious assumptions about the requirements, etc.}@} <!--SR:!2026-11-23,311,340-->

## week 3 pre-lecture

\(none\)

## week 3 lecture

> When should you ignore classes or associations stated in the requirements?
>
> ---
>
> - solution: {@{If the entity described by the requirements is outside the scope of the system, you should ignore it.}@} <!--SR:!2027-01-16,365,358-->

---

> What do you need to consider to determine the multiplicities of an association connecting a class that is a superclass \(generalization\)?
>
> ---
>
> - solution: {@{You need to consider the multiplicities for each subclass individually \(and also the superclass if the generalization is incomplete\), and then find the _least relaxed multiplicities_ that can accommodate the multiplicities found above. You may add a note next to the superclass multiplicity with text describing the multiplicities for each subclass. <p> You will likely need to use real-world knowledge, common sense, or application domain knowledge.}@} <!--SR:!fsrs,2029-10-04T00:00:00.000Z,1122,1121.50772511,1,2,9,0,0,2026-09-08T00:00:00.000Z-->

---

> Is there always a single correct answer for multiplicity?
>
> ---
>
> - solution: {@{No. Some are simply _design decisions_. For example, modeling a bank and its bank accounts, the multiplicity for the number of bank accounts per bank could be either `0..*` or `1..*`, depending on if the user requires a bank instance to have at least one bank account.}@} <!--SR:!fsrs,2029-07-07T00:00:00.000Z,1062,1061.94139538,1,2,9,0,0,2026-08-10T00:00:00.000Z-->

---

> When should an association class _not_ be used?
>
> ---
>
> - solution: {@{An association class is attached to an association. Each combination of instances of both classes can have _at most one_ link \(instance of the association\). When the application domain requires this to be _not_ the case, then a new class instead of an association class should be used.}@} <!--SR:!fsrs,2029-09-29T00:00:00.000Z,1118,1117.55099027,1,2,9,0,0,2026-09-07T00:00:00.000Z-->

---

> What is the relation between _associations_ and _operations_?
>
> ---
>
> - solution: {@{_Associations_ represent _results_ of operations, but not the operation _itself_. <p> For example, you most likely should _not_ have an association with the name "shows", which is likely an operation rather than its result.}@} <!--SR:!2027-12-31,607,338-->

## week 4 pre-lecture

\(none\)

## week 4 lecture

\(none\)

## week 5 pre-lecture

\(none\)

## week 5 lecture

\(none\)

## week 6 pre-lecture

\(none\)

## week 6 lecture

\(none\)

## week 7 pre-lecture

\(none\)

## week 7 lecture

\(none\)

## week 8 pre-lecture

\(none\)

## week 8 lecture

\(none\)

## week 9 pre-lecture

\(none\)

## week 9 lecture

\(none\)

## week 10 pre-lecture

\(none\)

## week 10 lecture

\(none\)

## week 11 pre-lecture

\(none\)

## week 11 lecture

\(none\)

## week 12 pre-lecture

\(none\)

## week 12 lecture

\(none\)

## week 13 pre-lecture

\(none\)

## week 13 lecture

\(none\)
