---
aliases:
  - rules of inference
  - rules of inferences
tags:
  - flashcard/active/general/eng/rules_of_inference
  - language/in/English
---

# rules of inference

In [logic](logic.md) and [philosophy of logic](philosophy%20of%20logic.md), specifically in [deductive reasoning](deductive%20reasoning.md), a __rule of inference__, {@{__inference rule__ or __transformation rule__}@} is {@{a [logical form](logical%20form.md) consisting of a function which takes premises, analyzes their [syntax](syntax%20(logic).md), and returns a conclusion (or [conclusions](multiple-conclusion%20logic.md))}@}. <!--SR:!2029-04-05,1302,354!2025-10-27,294,294-->

For example, the rule of inference called {@{_[modus ponens](modus%20ponens.md)_}@} takes {@{two premises, one in the form "If p then q" and another in the form "p", and returns the conclusion "q"}@}. The rule is {@{[valid](validity%20(logic).md) with respect to the semantics of [classical logic](classical%20logic.md) (as well as the semantics of many other [non-classical logics](non-classical%20logic.md))}@}, in the sense that {@{if the premises are true (under an interpretation), then so is the conclusion}@}. <!--SR:!2028-10-27,1124,314!2029-01-16,1240,354!2026-06-06,475,314!2025-10-30,321,334-->

Typically, a rule of inference {@{preserves truth, a semantic property}@}. In {@{[many-valued logic](many-valued%20logic.md)}@}, it {@{preserves a general designation}@}. But a rule of inference's action is {@{purely syntactic, and does not need to preserve any semantic property: any function from sets of formulae to formulae counts as a rule of inference}@}. Usually {@{only rules that are [recursive](recursion.md)}@} are {@{important}@}; i.e. rules such that there is {@{an [effective procedure](effective%20method.md) for determining whether any given formula is the conclusion of a given set of formulae according to the rule}@}. An example of a rule that is not effective in this sense is {@{the infinitary [ω-rule](ω-consistent%20theory.md)}@}.<sup>[\[1\]](#^ref-1)</sup> <!--SR:!2026-01-16,138,310!2026-09-11,550,314!2027-03-31,591,274!2026-11-29,532,274!2025-12-01,83,363!2025-12-01,83,363!2025-11-12,56,346!2025-11-29,66,346-->

Popular rules of inference in [propositional logic](propositional%20calculus.md) include {@{_[modus ponens](modus%20ponens.md)_, _[modus tollens](modus%20tollens.md)_, and [contraposition](contraposition.md)}@}. First-order [predicate logic](first-order%20logic.md) uses rules of inference to {@{deal with [logical quantifiers](quantifier%20(logic).md)}@}. <!--SR:!2027-01-12,608,294!2025-12-16,342,314-->

## standard form

In {@{[formal logic](logic.md#formal%20logic) (and many related areas)}@}, rules of inference are usually given in the following standard form: (description: {@{All premises are listed above a line. One conclusion is listed below the line.}@}) <!--SR:!2027-01-25,664,334!2025-10-22,315,334-->

Premise#1 <br/>
Premise#2 <br/>
__...__<br/>
<u>Premise#n</u> <br/>
Conclusion

This expression states that {@{whenever in the course of some logical derivation the given premises have been obtained, the specified conclusion can be taken for granted as well}@}. The exact formal language that is used to describe both premises and conclusions {@{depends on the actual context of the derivations}@}. In a simple case, one may use logical formulae, such as in: {@{$$\begin{aligned} & A \rightarrow B \\ & \underline{A \phantom{\rightarrow B} } \\ & B & \end{aligned}$$}@}. <!--SR:!2027-05-23,751,334!2027-02-19,682,334!2029-04-06,1302,354-->

This is {@{the _[modus ponens](modus%20ponens.md)_ rule of [propositional logic](propositional%20calculus.md)}@}. Rules of inference are often formulated as {@{[schemata](logical%20form.md) employing [metavariables](metavariable.md)}@}.<sup>[\[2\]](#^ref-2)</sup> In the rule (schema) above, the metavariables A and B can be {@{instantiated to any element of the universe (or sometimes, by convention, a restricted subset such as [propositions](proposition.md)) to form an [infinite set](infinite%20set.md) of inference rules}@}. <!--SR:!2027-09-29,855,334!2026-06-05,474,314!2026-04-21,401,294-->

A proof system is formed from {@{a set of rules chained together to form proofs, also called _derivations_}@}. Any derivation has {@{only one final conclusion, which is the statement proved or derived}@}. If {@{premises are left unsatisfied in the derivation}@}, then {@{the derivation is a proof of a _hypothetical_ statement: "_if_ the premises hold, _then_ the conclusion holds."}@} <!--SR:!2028-03-29,977,334!2027-01-07,593,314!2028-10-31,1175,350!2029-01-19,1241,354-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/rules_of_inference) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. Boolos, George; Burgess, John; Jeffrey, Richard C. (2007). [_Computability and logic_](https://archive.org/details/computabilitylog0000bool/page/364). Cambridge: Cambridge University Press. p. [364](https://archive.org/details/computabilitylog0000bool/page/364). [ISBN](ISBN.md) [978-0-521-87752-7](https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-87752-7). <a id="^ref-1"></a>^ref-1
2. John C. Reynolds (2009) [1998]. [_Theories of Programming Languages_](https://books.google.com/books?id=2OwlTC4SOccC&pg=PA12). Cambridge University Press. p. 12. [ISBN](ISBN.md) [978-0-521-10697-9](https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-10697-9). <a id="^ref-2"></a>^ref-2
