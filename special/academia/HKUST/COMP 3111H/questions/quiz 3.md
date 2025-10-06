---
aliases:
  - COMP 3111H quiz 3
  - COMP3111H quiz 3
  - HKUST COMP 3111H quiz 3
  - HKUST COMP3111H quiz 3
tags:
  - flashcard/active/special/academia/HKUST/COMP_3111H/questions/quiz_3
  - language/in/English
---

# quiz 3

- HKUST COMP 3111H

---

- type: quiz
- due: 2025-09-18T23:59:59+08:00
- points: 5
- questions: 5
- available: 2025-09-01T23:59:00+08:00/2025-09-18T23:59:59+08:00, P17DT59S
- time limit: none
- allowed attempts: 2

## hints

1. association class ::@:: Most attributes clearly belongs to a class. However, there are attributes that do not clearly belong to a class, but rather to associations. It is often needed in many-to-many associations. <!--SR:!2025-10-25,15,290!2025-10-26,16,290-->
2. associations between the same set of objects ::@:: Multiple associations between the same set of objects are allowed if they have _different semantics_. <!--SR:!2025-10-26,16,290!2025-12-21,58,310-->
3. association ::@:: An _association_ \(a _classifier_\) _classifies_ a collection of links with _common semantics_. A _link_ is a _relation_ between objects \(of different classes or the same class\), and is an _instance_ of an association. They are _bidirectional_, so no arrowhead is needed. You can still add it to show the _navigability_ of association \(the object at the tail _references_ that at the arrowhead\), making the association _unidirectional_. <p> The _name_ of an association should be _unique_ \(including classes and associations\), and uses vocabularies according to the application domain. Normally, the name can only be _read meaningfully_ in one direction, and the name for the other direction is _inferred_. <!--SR:!2025-11-15,26,270!2025-10-25,15,290-->
4. completeness coverage constraints ::@:: A _complete_ generalization is one where all instances of a superclass is an instance of \(_at least_\) one subclass \(i.e. only _indirect_ instances of the superclass\). Its opposite is _incomplete_, in which there may be _direct_ instances of a superclass that are not instances of any subclasses \(i.e. there are _direct_ instances of the superclass\). <!--SR:!2025-12-06,43,290!2025-10-26,16,290-->
5. coverage constraints ::@:: Generalization can be characterized by 2 main properties \(and possibly more\): _completeness_ and _disjointness_. <!--SR:!2025-12-20,57,310!2025-10-25,15,290-->
