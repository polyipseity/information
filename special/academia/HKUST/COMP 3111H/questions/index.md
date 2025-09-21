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

## week 1 lecture

\(none\)

## week 2 lecture

> In a course registration system, there are students and courses.
>
> A student must be in 1 to 5 courses. A course must have 10 to 50 students.
>
> What should be the _multiplicities_ of the `Student ? -EnrollsIn- ? Course` relation?
>
> ---
>
> - solution: {@{`Student 0..50 -EnrollsIn- 0..5 Course`. Add notes next to the multiplicities to indicate the minimum counts instead.}@}
> - explanation: {@{Multiplicities are _hard_ constraints that must be followed at all times. <p> Consider creating a student or a course. There is no "natural" way to associate courses to a student or students to a course. So we must allow 0 when creating a student or a course. The notes next to the multiplicities are meant to fill in the _missing_ semantics.}@} <!--SR:!2025-09-25,4,270!2025-09-25,4,270-->

---

> Fill in the missing multiplicities using _common sense_
>
> 1. `Customer ? -Makes- ? Shi[ment`
> 2. `Shipment ? -Contains- ? Package`
> 3. `Shipment ? -SentTo- ? City`
>
> ---
>
> - solution: {@{1. `Customer 1 -Makes- * Shipment` <br/> 2. `Shipment 1 -Contains- 1..* Package` <br/> 3. `Shipment * -SentTo- 1 City`}@}
> - annotation: {@{There are other possible multiplicities according to the _application domain_.}@} <!--SR:!2025-09-25,4,270!2025-09-25,4,270-->

---

> Given the following association: `Student ? -EnrollsIn- ? Course`, how to put an enrollment attribute, e.g. grade? There may be multiple enrollments for a pair of a `Student` instance and a `Course` instance, e.g. retaking a course due to failing the previous pre-enrollment.
>
> ---
>
> - solution: {@{Use a _mew separate class_ replacing the association. The new class is associated with `Student` and `Course`.}@}
> - annotation: {@{An _association class_ would have worked if multiple enrollments were impossible.}@} <!--SR:!2025-09-25,4,270!2025-09-25,4,270-->

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
> - annotation: {@{There are other possible answers according to the _application domain_.}@} <!--SR:!2025-09-25,4,270!2025-09-25,4,270-->

## week 3 lecture
