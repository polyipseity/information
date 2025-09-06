---
aliases:
  - resolution
  - resolution (logic)
  - resolution rule
  - resolution rules
tags:
  - flashcard/active/general/eng/resolution__logic_
  - language/in/English
---

# resolution (logic)

In {@{[mathematical logic](mathematical%20logic.md) and [automated theorem proving](automated%20theorem%20proving.md)}@}, {@{__resolution__}@} is {@{a [rule of inference](rule%20of%20inference.md) leading to a [refutation-complete](#refutation-completeness) [theorem-proving](theorem-proving.md) technique}@} for {@{sentences in [propositional logic](propositional%20logic.md) and [first-order logic](first-order%20logic.md)}@}. For {@{propositional logic}@}, {@{systematically applying the resolution rule acts}@} as {@{a [decision procedure](decision%20procedure.md) for formula unsatisfiability}@}, solving {@{the \(complement of the\) [Boolean satisfiability problem](Boolean%20satisfiability%20problem.md)}@}. For {@{[first-order logic](first-order%20logic.md)}@}, resolution can be used as the basis for {@{a [semi-algorithm](RE%20(complexity).md) for the unsatisfiability problem of [first-order logic](first-order%20logic.md)}@}, providing {@{a more practical method than one following from [Gödel's completeness theorem](Gödel's%20completeness%20theorem.md)}@}.

{@{The resolution rule}@} can be traced back to {@{[Davis](Martin%20Davis%20(mathematician).md) and [Putnam](Hilary%20Putnam.md) \(1960\)}@};<sup>[\[1\]](#^ref-1)</sup> however, {@{their [algorithm](Davis-Putnam%20algorithm.md)}@} required {@{trying all [ground instances](ground%20instance.md#first-order%20logic) of the given formula}@}. {@{This source of [combinatorial explosion](combinatorial%20explosion.md)}@} was {@{eliminated in 1965}@} by {@{[John Alan Robinson](John%20Alan%20Robinson.md)'s syntactical [unification algorithm](unification%20(computer%20science).md)}@}, which allowed one to {@{instantiate the formula during the proof "on demand" just as far as needed to keep [refutation completeness](refutation%20completeness.md#refutation-completeness)}@}.<sup>[\[2\]](#^ref-2)</sup>

{@{The clause produced by a resolution rule}@} is sometimes called {@{a __resolvent__}@}.

## resolution in propositional logic

<!-- markdownlint-disable-next-line MD024 -->
### resolution rule

{@{The __resolution rule__ in propositional logic}@} is {@{a single valid inference rule that produces a new clause}@} implied by {@{two [clauses](clause%20(logic).md) containing complementary literals}@}. {@{A [literal](literal%20(mathematical%20logic).md)}@} is {@{a [propositional variable](propositional%20variable.md) or the negation of a propositional variable}@}. {@{Two literals are said to be complements}@} if {@{one is the negation of the other}@} \(in the following, $\lnot c$ is {@{taken to be the complement to $c$}@}\). {@{The resulting clause}@} contains {@{all the literals that do not have complements}@}. Formally: {@{$${\frac {a_{1}\lor a_{2}\lor \cdots \lor c,\quad b_{1}\lor b_{2}\lor \cdots \lor \neg c}{a_{1}\lor a_{2}\lor \cdots \lor b_{1}\lor b_{2}\lor \cdots } }$$}@} where

&emsp; all $a_{i}$, $b_{i}$, and $c$ ::@:: are literals, <br/>
&emsp; the dividing line ::@:: stands for "[entails](logical%20consequence.md)".

The above may also be written as: \(annotation: {@{form using implications}@}\) {@{$${\frac {(\neg a_{1}\land \neg a_{2}\land \cdots )\rightarrow c,\quad c\rightarrow (b_{1}\lor b_{2}\lor \cdots )}{(\neg a_{1}\land \neg a_{2}\land \cdots )\rightarrow (b_{1}\lor b_{2}\lor \cdots )} }$$}@}

Or {@{schematically}@} as: {@{$${\frac {\Gamma _{1}\cup \left\{\ell \right\}\,\,\,\,\Gamma _{2}\cup \left\{ {\overline {\ell } }\right\} }{\Gamma _{1}\cup \Gamma _{2} } }|\ell |$$}@}

We have the following terminology:

- The clauses $\Gamma _{1}\cup \left\{\ell \right\}$ and $\Gamma _{2}\cup \left\{ {\overline {\ell } }\right\}$ ::@:: are the inference's premises
- $\Gamma _{1}\cup \Gamma _{2}$ \(the resolvent of the premises\) ::@:: is its conclusion.
- The literal $\ell$ ::@:: is the left resolved literal,
- The literal ${\overline {\ell } }$ ::@:: is the right resolved literal,
- $|\ell |$ ::@:: is the resolved atom or pivot.

{@{The clause produced by the resolution rule}@} is called {@{the _resolvent_ of the two input clauses}@}. It is {@{the principle of _[consensus](consensus%20theorem.md)_}@} applied to {@{clauses rather than terms}@}.<sup>[\[3\]](#^ref-3)</sup>

When the two clauses {@{contain more than one pair of complementary literals}@}, the resolution rule can be {@{applied \(independently\) for each such pair}@}; however, the result is {@{always a [tautology](tautology%20(logic).md)}@}.

{@{[Modus ponens](modus%20ponens.md)}@} can be seen as {@{a special case of resolution \(of a one-literal clause and a two-literal clause\)}@}. {@{$${\frac {p\rightarrow q,\quad p}{q} }$$}@} is equivalent to {@{$${\frac {\lnot p\lor q,\quad p}{q} }$$}@}

### a resolution technique

When coupled with {@{a complete [search algorithm](search%20algorithm.md)}@}, the resolution rule yields {@{a [sound](soundness.md) and [complete](completeness%20(logic).md) algorithm}@} for {@{deciding the _satisfiability_ of a propositional formula}@}, and, by extension, {@{the [validity](validity%20(logic).md) of a sentence under a set of axioms}@}.

{@{This resolution technique}@} uses {@{[proof by contradiction](proof%20by%20contradiction.md)}@} and is based on the fact that any sentence in propositional logic can be {@{transformed into an equivalent sentence in [conjunctive normal form](conjunctive%20normal%20form.md)}@}.<sup>[\[4\]](#^ref-4)</sup> The steps are as follows.

- All sentences in the knowledge base and the _negation_ of the sentence to be proved \(the _conjecture_\) ::@:: are conjunctively connected.
- The resulting sentence ::@:: is transformed into a conjunctive normal form with the conjuncts viewed as elements in a set, _S_, of clauses.<sup>[\[4\]](#^ref-4)</sup>
  - For example, $(A_{1}\lor A_{2})\land (B_{1}\lor B_{2}\lor B_{3})\land (C_{1})$ ::@:: gives rise to the set $S=\{A_{1}\lor A_{2},B_{1}\lor B_{2}\lor B_{3},C_{1}\}$.
- The resolution rule is applied to {@{all possible pairs of clauses that contain complementary literals}@}. After {@{each application of the resolution rule}@}, the resulting sentence is {@{simplified by removing repeated literals}@}. If {@{the clause contains complementary literals}@}, it is {@{discarded \(as a tautology\)}@}. If {@{not, and if it is not yet present in the clause set _S_}@}, it is {@{added to _S_, and is considered for further resolution inferences}@}.
- If after {@{applying a resolution rule}@} {@{the _empty clause_ is derived}@}, {@{the original formula is unsatisfiable \(or _contradictory_\)}@}, and hence it can be concluded that {@{the initial conjecture [follows from](logical%20consequence.md) the axioms}@}.
- If, on the other hand, {@{the empty clause cannot be derived}@}, and {@{the resolution rule cannot be applied to derive any more new clauses}@}, the conjecture is {@{not a theorem of the original knowledge base}@}.

{@{One instance of this algorithm}@} is {@{the original [Davis–Putnam algorithm](Davis–Putnam%20algorithm.md)}@} that was later refined into {@{the [DPLL algorithm](DPLL%20algorithm.md)}@} that {@{removed the need for explicit representation of the resolvents}@}.

{@{This description of the resolution technique}@} uses {@{a set _S_ as the underlying [data-structure](data%20structure.md) to represent resolution derivations}@}. {@{[Lists](list%20(data%20structure).md), [Trees](tree%20(data%20structure).md) and [Directed Acyclic Graphs](Directed%20acyclic%20graph.md)}@} are {@{other possible and common alternatives}@}. {@{Tree representations}@} are more faithful to {@{the fact that the resolution rule is binary}@}. Together with {@{a sequent notation for clauses}@}, a tree representation also makes it clear to see how {@{the resolution rule is related to a special case of the [cut-rule](cut%20rule.md)}@}, restricted to {@{atomic cut-formulas}@}. However, tree representations are {@{not as compact as set or list representations}@}, because they {@{explicitly show redundant subderivations of clauses}@} that are {@{used more than once in the derivation of the empty clause}@}. {@{Graph representations}@} can be {@{as compact in the number of clauses as list representations}@} and they also store {@{structural information regarding which clauses were resolved to derive each resolvent}@}.

#### a simple example

{@{$${\frac {a\vee b,\quad \neg a\vee c}{b\vee c} }$$}@} In plain language: Suppose {@{$a$ is false}@}. In order for {@{the premise $a\vee b$ to be true}@}, {@{$b$ must be true}@}. Alternatively, suppose {@{$a$ is true}@}. In order for {@{the premise $\neg a\vee c$ to be true}@}, {@{$c$ must be true}@}. Therefore, regardless of {@{falsehood or veracity of $a$}@}, if {@{both premises hold}@}, then {@{the conclusion $b\vee c$ is true}@}.

## resolution in first-order logic

{@{Resolution rule}@} can be {@{generalized to [first-order logic](first-order%20logic.md)}@} to:<sup>[\[5\]](#^ref-5)</sup> {@{$${\frac {\Gamma _{1}\cup \left\{L_{1}\right\}\,\,\,\,\Gamma _{2}\cup \left\{L_{2}\right\} }{(\Gamma _{1}\cup \Gamma _{2})\phi } }\phi$$}@} where $\phi$ is {@{a [most general unifier](most%20general%20unifier.md#syntactic%20unification%20of%20first-order%20terms) of $L_{1}$ and ${\overline {L_{2} } }$}@}, and $\Gamma _{1}$ and $\Gamma _{2}$ {@{have no common variables}@}.

### example

{@{The clauses $P(x),Q(x)$ and $\neg P(b)$}@} can {@{apply this rule with $[b/x]$ as unifier}@}.

Here x is {@{a variable}@} and b is {@{a constant}@}. {@{$${\frac {P(x),Q(x)\,\,\,\,\neg P(b)}{Q(b)} }[b/x]$$}@} Here we see that

- The clauses $P(x),Q(x)$ and $\neg P(b)$ ::@:: are the inference's premises
- $Q(b)$ \(the resolvent of the premises\) ::@:: is its conclusion.
- The literal $P(x)$ ::@:: is the left resolved literal,
- The literal $\neg P(b)$ ::@:: is the right resolved literal,
- $P$ ::@:: is the resolved atom or pivot.
- $[b/x]$ ::@:: is the most general unifier of the resolved literals.

### informal explanation

In {@{first-order logic}@}, resolution condenses {@{the traditional [syllogisms](syllogism.md) of [logical inference](rule%20of%20inference.md) down to a single rule}@}.

To understand {@{how resolution works}@}, consider {@{the following example syllogism of [term logic](term%20logic.md)}@}:

> \(annotation: {@{example 1}@}\)
>
> All Greeks are Europeans. <br/>
> Homer is a Greek. <br/>
> Therefore, Homer is a European.

Or, more generally:

> \(annotation: {@{example 1 in symbols}@}\)
>
> $\forall x.P(x)\Rightarrow Q(x)$ <br/>
> $P(a)$ <br/>
> Therefore, $Q(a)$

To {@{recast the reasoning using the resolution technique}@}, first the clauses must be {@{converted to [conjunctive normal form](conjunctive%20normal%20form.md) \(CNF\)}@}. In this form, {@{all [quantification](quantification%20(logic).md) becomes implicit}@}: {@{[universal quantifiers](universal%20quantification.md) on variables \(_X_, _Y_, ...\)}@} are {@{simply omitted as understood}@}, while {@{[existentially-quantified](existential%20quantification.md) variables}@} are {@{replaced by [Skolem functions](Skolem%20function.md)}@}.

> \(annotation: {@{example 1 in symbols with implicit quantification}@}\)
>
> $\neg P(x)\vee Q(x)$ <br/>
> $P(a)$ <br/>
> Therefore, $Q(a)$

So the question is, how does {@{the resolution technique derive the last clause from the first two}@}? The rule is simple:

- Find {@{two clauses containing the same predicate}@}, where {@{it is negated in one clause but not in the other}@}.
- Perform {@{a [unification](unification%20(computing).md) on the two predicates}@}. \(If {@{the unification fails}@}, you {@{made a bad choice of predicates}@}. Go back to {@{the previous step and try again}@}.\)
- If {@{any unbound variables which were bound in the unified predicates}@} also {@{occur in other predicates in the two clauses}@}, {@{replace them with their bound values \(terms\) there as well}@}.
- Discard {@{the unified predicates}@}, and combine {@{the remaining ones from the two clauses into a new clause}@}, also {@{joined by the "∨" operator}@}.

To {@{apply this rule to the above example}@}, we find {@{the predicate _P_ occurs in negated form}@}

&emsp; ¬<!-- markdown separator -->_P_\(_X_\)

in the first clause, and in {@{non-negated form}@}

&emsp; _P_\(_a_\)

in the second clause. _X_ is {@{an unbound variable}@}, while {@{_a_ is a bound value \(term\)}@}. {@{Unifying the two produces}@} the substitution \(annotation: {@{_X_ ↦ _a_}@}\)

&emsp; _X_ ↦ _a_

Discarding {@{the unified predicates}@}, and {@{applying this substitution to the remaining predicates}@} \({@{just _Q_\(_X_\)}@}, in this case\), produces the conclusion: \(annotation: {@{_Q_\(_a_\)}@}\)

&emsp; _Q_\(_a_\)

For another example, consider the syllogistic form

> \(annotation: {@{example 2}@}\)
>
> All Cretans are islanders. <br/>
> All islanders are liars. <br/>
> Therefore all Cretans are liars.

Or more generally,

> \(annotation: {@{example 2 in symbols}@}\)
>
> ∀<!-- markdown separator -->_X_ _P_\(_X_\) → _Q_\(_X_\) <br/>
> ∀<!-- markdown separator -->_X_ _Q_\(_X_\) → _R_\(_X_\) <br/>
> Therefore, ∀<!-- markdown separator -->_X_ _P_\(_X_\) → _R_\(_X_\)

In CNF, the antecedents become:

> \(annotation: {@{example 2 in CNF}@}\)
>
> ¬<!-- markdown separator -->_P_\(_X_\) ∨ _Q_\(_X_\) <br/>
> ¬<!-- markdown separator -->_Q_\(_Y_\) ∨ _R_\(_Y_\)

\(The variable in the second clause was renamed to make it clear that variables in different clauses are distinct.\)

Now, unifying {@{_Q_\(_X_\) in the first clause with ¬<!-- markdown separator -->_Q_\(_Y_\) in the second clause}@} means that {@{_X_ and _Y_ become the same variable anyway}@}. Substituting this into {@{the remaining clauses and combining them}@} gives the conclusion: \(annotation: {@{¬<!-- markdown separator -->_P_\(_X_\) ∨ _R_\(_X_\)}@}\)

&emsp; ¬<!-- markdown separator -->_P_\(_X_\) ∨ _R_\(_X_\)

### factoring

{@{The resolution rule, as defined by Robinson}@}, also {@{incorporated factoring}@}, which {@{unifies two literals in the same clause}@}, before or during {@{the application of resolution}@} as defined above. The resulting inference rule is {@{refutation-complete}@},<sup>[\[6\]](#^ref-6)</sup> in that {@{a set of clauses is unsatisfiable}@} {@{[if and only if](if%20and%20only%20if.md) there exists a derivation of the empty clause using only resolution, enhanced by factoring}@}.

An example for {@{an unsatisfiable clause set for which factoring is needed to derive the empty clause}@} is: {@{$${\begin{array}{rlcl}(1):&P(u)&\lor &P(f(u))\\(2):&\lnot P(v)&\lor &P(f(w))\\(3):&\lnot P(x)&\lor &\lnot P(f(x))\\\end{array} }$$}@}

Since {@{each clause consists of two literals}@}, so does {@{each possible resolvent}@}. Therefore, by {@{resolution without factoring}@}, {@{the empty clause can never be obtained}@}. Using {@{factoring}@}, it {@{can be obtained}@} e.g. as follows:<sup>[\[7\]](#^ref-7)</sup> {@{$${\begin{array}{rll}(4):&P(u)\lor P(f(w))&{\text{by resolving (1) and (2), with } }v=f(u)\\(5):&P(f(w))&{\text{by factoring (4), with } }u=f(w)\\(6):&\lnot P(f(f(w')))&{\text{by resolving (5) and (3), with } }w=w',x=f(w')\\(7):&{\text{false} }&{\text{by resolving (5) and (6), with } }w=f(w')\\\end{array} }$$}@}

## non-clausal resolution

{@{Generalizations of the above resolution rule}@} have been devised that {@{do not require the originating formulas to be in [clausal normal form](clausal%20normal%20form.md)}@}.<sup>[\[8\]](#^ref-8)</sup><sup>[\[9\]](#^ref-9)</sup><sup>[\[10\]](#^ref-10)</sup><sup>[\[11\]](#^ref-11)</sup><sup>[\[12\]](#^ref-12)</sup><sup>[\[13\]](#^ref-13)</sup>

These techniques are useful mainly in {@{interactive theorem proving}@} where it is {@{important to preserve human readability of intermediate result formulas}@}. Besides, they avoid {@{combinatorial explosion during transformation to clause-form}@},<sup>[\[10\]](#^ref-10)</sup><sup>:&hairsp;98&hairsp;</sup> and sometimes {@{save resolution steps}@}.<sup>[\[13\]](#^ref-13)</sup><sup>:&hairsp;425&hairsp;</sup>

### non-clausal resolution in propositional logic

For {@{propositional logic}@}, Murray<sup>[\[9\]](#^ref-9)</sup><sup>:&hairsp;18&hairsp;</sup> and Manna and Waldinger<sup>[\[10\]](#^ref-10)</sup><sup>:&hairsp;98&hairsp;</sup> use the rule {@{$${\begin{array}{c}F[p]\;\;\;\;\;\;\;\;\;\;G[p]\\\hline F[{\textit {true} }]\lor G[{\textit {false} }]\\\end{array} } \,$$}@} \(annotation: Assume {@{the premises $F[p]$ and $G[p]$ are true for any fixed assignment to $p$}@}. Then if {@{$p$ is true}@}, then {@{$F[true]$ is true and the consequent is true}@}. Otherwise if {@{$p$ is false}@}, then {@{$G[false]$ is true and the consequent is true}@}. In both cases, {@{the premises imply the consequent}@}.\) where $p$ denotes {@{an arbitrary formula \(annotation: not restricted to literals\)}@}, $F[p]$ denotes {@{a formula containing $p$ as a subformula}@}, and $F[{\textit {true} }]$ is {@{built by replacing in $F[p]$ every occurrence of $p$ by ${\textit {true} }$}@}; likewise {@{for $G$}@}. {@{The resolvent $F[{\textit {true} }]\lor G[{\textit {false} }]$}@} is intended to be {@{simplified using rules like $q\land {\textit {true} }\implies q$, etc.}@} In order to {@{prevent generating useless trivial resolvents}@}, the rule shall be {@{applied only when $p$ has at least one "negative" and "positive"<sup>[\[14\]](#^ref-14)</sup> occurrence in $F$ and $G$, respectively}@}. Murray has shown that {@{this rule is complete}@} if {@{augmented by appropriate logical transformation rules}@}.<sup>[\[10\]](#^ref-10)</sup><sup>:&hairsp;103&hairsp;</sup>

Traugott uses the rule {@{$${\begin{array}{c}F[p^{+},p^{-}]\;\;\;\;\;\;\;\;G[p]\\\hline F[G[{\textit {true} }],\lnot G[{\textit {false} }]]\\\end{array} } \,,$$}@} \(annotation: It uses some properties of {@{polarity}@}.\) where the exponents of $p$ indicate {@{the polarity of its occurrences}@}. \(annotation: {@{Polarity}@} counts {@{the number of implicit \(e.g. the premise of $\supset$\) and explicit negations enclosing $p$}@}, with {@{even being positive and odd being negative}@}.\) While {@{$G[{\textit {true} }]$ and $G[{\textit {false} }]$ are built as before}@}, the formula $F[G[{\textit {true} }],\lnot G[{\textit {false} }]]$ is {@{obtained by replacing each positive and each negative occurrence of $p$ in $F$ with $G[{\textit {true} }]$ and $\lnot G[{\textit {false} }]$, respectively}@}. \(annotation: The $\lnot$ is to {@{neutralize the $\lnot$ appearing before a negative occurrence of $p$}@}.\) Similar to Murray's approach, {@{appropriate simplifying transformations}@} are {@{to be applied to the resolvent}@}. Traugott proved {@{his rule to be complete}@}, provided {@{$\land ,\lor ,\rightarrow ,\lnot$ are the only connectives used in formulas}@}.<sup>[\[12\]](#^ref-12)</sup><sup>:&hairsp;398–400&hairsp;</sup>

{@{Traugott's resolvent}@} is {@{stronger than Murray's}@}.<sup>[\[12\]](#^ref-12)</sup><sup>:&hairsp;395&hairsp;</sup> Moreover, it does not {@{introduce new binary junctors}@}, thus avoiding {@{a tendency towards clausal form in repeated resolution}@}. However, formulas may {@{grow longer}@} when {@{a small $p$ is replaced multiple times with a larger $G[{\textit {true} }]$ and/or $G[{\textit {false} }]$}@}.<sup>[\[12\]](#^ref-12)</sup><sup>:&hairsp;398&hairsp;</sup>

### propositional non-clausal resolution example

As an example, starting from the user-given assumptions {@{$${\begin{array}{rccc}(1):&a&\rightarrow &b\land c\\(2):&c&\rightarrow &d\\(3):&b\land d&\rightarrow &e\\(4):&\lnot (a&\rightarrow &e)\\\end{array} }$$}@} {@{the Murray rule}@} can be used as follows to {@{infer a contradiction}@}:<sup>[\[15\]](#^ref-15)</sup> {@{$${\begin{array}{rrclccl}(5):&({\textit {true} }\rightarrow d)&\lor &(a\rightarrow b\land {\textit {false} })&\implies &d\lor \lnot a&{\text{from (2) and (1), with } }p=c\\(6):&(b\land {\textit {true} }\rightarrow e)&\lor &({\textit {false} }\lor \lnot a)&\implies &(b\rightarrow e)\lor \lnot a&{\text{from (3) and (5), with } }p=d\\(7):&(({\textit {true} }\rightarrow e)\lor \lnot a)&\lor &(a\rightarrow {\textit {false} }\land c)&\implies &e\lor \lnot a\lor \lnot a&{\text{from (6) and (1), with } }p=b\\(8):&(e\lor \lnot {\textit {true} }\lor \lnot {\textit {true} })&\lor &\lnot ({\textit {false} }\rightarrow e)&\implies &e&{\text{from (7) and (4), with } }p=a\\(9):&\lnot (a\rightarrow {\textit {true} })&\lor &{\textit {false} }&\implies &{\textit {false} }&{\text{from (4) and (8), with } }p=e\\\end{array} }$$}@} For the same purpose, {@{the Traugott rule}@} can be used as follows:<sup>[\[12\]](#^ref-12)</sup><sup>:&hairsp;397&hairsp;</sup> {@{$${\begin{array}{rcccl}(10):&a\rightarrow b\land ({\textit {true} }\rightarrow d)&\implies &a\rightarrow b\land d&{\text{from (1) and (2), with } }p=c\\(11):&a\rightarrow ({\textit {true} }\rightarrow e)&\implies &a\rightarrow e&{\text{from (10) and (3), with } }p=(b\land d)\\(12):&\lnot {\textit {true} }&\implies &{\textit {false} }&{\text{from (11) and (4), with } }p=(a\rightarrow e)\\\end{array} }$$}@}

From {@{a comparison of both deductions}@}, the following issues can be seen:

- Traugott's rule may yield a sharper resolvent: ::@:: compare \(5\) and \(10\), which both resolve \(1\) and \(2\) on $p=c$.
- Murray's rule introduced 3 new disjunction symbols: in \(5\), \(6\), and \(7\), ::@:: while Traugott's rule did not introduce any new symbol; in this sense, Traugott's intermediate formulas resemble the user's style more closely than Murray's.
- Due to the latter issue, Traugott's rule can take advantage of the implication in assumption \(4\), using as $p$ the [non-atomic formula](atomic%20formula.md) $a\rightarrow e$ in step \(12\). ::@:: Using Murray's rules, the semantically equivalent formula $e\lor \lnot a\lor \lnot a$ was obtained as \(7\), however, it could not be used as $p$ due to its syntactic form.

### non-clausal resolution in first-order logic

For {@{first-order predicate logic}@}, {@{Murray's rule}@} is generalized to {@{allow distinct, but unifiable, subformulas $p_{1}$ and $p_{2}$ of $F$ and $G$}@}, respectively. If $\phi$ is {@{the most general unifier of $p_{1}$ and $p_{2}$}@}, then the generalized resolvent is {@{$F\phi [{\textit {true} }]\lor G\phi [{\textit {false} }]$}@}. While {@{the rule remains sound if a more special substitution $\phi$ is used}@}, no such rule applications are {@{needed to achieve completeness}@}.<sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup>

{@{Traugott's rule}@} is generalized to {@{allow several pairwise distinct subformulas $p_{1},\ldots ,p_{m}$ of $F$ and $p_{m+1},\ldots ,p_{n}$ of $G$}@}, as long as {@{$p_{1},\ldots ,p_{n}$ have a common most general unifier}@}, say $\phi$. The generalized resolvent is obtained after {@{applying $\phi$ to the parent formulas}@}, thus {@{making the propositional version applicable}@}. {@{Traugott's completeness proof}@} relies on the assumption that {@{this fully general rule is used}@};<sup>[\[12\]](#^ref-12)</sup><sup>:&hairsp;401&hairsp;</sup> it is not clear whether {@{his rule would remain complete if restricted to $p_{1}=\cdots =p_{m}$ and $p_{m+1}=\cdots =p_{n}$}@}.<sup>[\[16\]](#^ref-16)</sup>

## paramodulation

{@{Paramodulation}@} is {@{a related technique for reasoning on sets of clauses}@} where {@{the [predicate symbol](predicate%20symbol.md) is equality}@}. It generates {@{all "equal" versions of clauses, except reflexive identities \(annotation: i.e. $x \simeq x$\)}@}. The paramodulation operation takes {@{a positive _from_ clause \(annotation: one of the two premises\), which must contain an equality literal}@}. It then {@{searches an _into_ clause \(annotation: the other premise\)}@} with {@{a subterm that unifies with one side of the equality \(annotation: has a most general unifier\)}@}. The subterm is then {@{replaced by the other side of the equality}@}. \(annotation: Finally, the consequent is {@{the disjunction of the from clause and the replaced into clause}@}, discarding {@{the equality literal}@}, and {@{unified by the above most general unifier}@}.\) {@{The general aim of paramodulation}@} is to {@{reduce the system to atoms, reducing the size of the terms when substituting}@}.<sup>[\[17\]](#^ref-17)</sup>

## implementations

- [CARINE](CARINE.md)
- [GKC](GKC%20Theorem%20Prover.md)
- [Otter](Otter%20(theorem%20prover).md)
- [Prover9](Prover9.md)
- [SNARK](SNARK%20(theorem%20prover).md)
- [SPASS](SPASS.md)
- [Vampire](Vampire%20(theorem%20prover).md)
- [Logictools](https://logictools.org/) online prover

## see also

- [Condensed detachment](condensed%20detachment.md) ::@:: — an earlier version of resolution
- [Inductive logic programming](inductive%20logic%20programming.md)
- [Inverse resolution](inverse%20resolution.md#inverse%20resolution)
- [Logic programming](logic%20programming.md)
- [Method of analytic tableaux](method%20of%20analytic%20tableaux.md)
- [SLD resolution](SLD%20resolution.md)

## notes

1. <a id="CITEREFDavisPutnam1960"></a> Davis, Martin; Putnam, Hilary \(1960\). ["A Computing Procedure for Quantification Theory"](https://doi.org/10.1145%2F321033.321034). _J. ACM_. __7__ \(3\): 201–215. [doi](doi%20(identifier).md):[10.1145/321033.321034](https://doi.org/10.1145%2F321033.321034). [S2CID](S2CID%20(identifier).md#S2CID) [31888376](https://api.semanticscholar.org/CorpusID:31888376). Here: p. 210, "III. Rule for Eliminating Atomic Formulas". <a id="^ref-1"></a>^ref-1
2. [Robinson 1965](#CITEREFRobinson1965) <a id="^ref-2"></a>^ref-2
3. D.E. Knuth, _[The Art of Computer Programming](The%20Art%20of%20Computer%20Programming.md)_ __4A__: _Combinatorial Algorithms_, part 1, p. 539 <a id="^ref-3"></a>^ref-3
4. [Leitsch 1997](#CITEREFLeitsch1997), p. 11 "Before applying the inference method itself, we transform the formulas to quantifier-free conjunctive normal form." <a id="^ref-4"></a>^ref-4
5. <a id="CITEREFArísGonzálezRubio2005"></a> Arís, Enrique P.; González, Juan L.; Rubio, Fernando M. \(2005\). [_Lógica Computacional_](https://books.google.com/books?id=pS_6oZVbY2cC&pg=PR5). Ediciones Paraninfo, S.A. [ISBN](ISBN%20(identifier).md) [9788497321822](https://en.wikipedia.org/wiki/Special:BookSources/9788497321822). <a id="^ref-5"></a>^ref-5
6. <a id="CITEREFRussellNorvig2009"></a> Russell, Stuart J.; Norvig, Peter \(2009\). _Artificial Intelligence: A Modern Approach_ \(3rd ed.\). Prentice Hall. p. 350. [ISBN](ISBN%20(identifier).md) [978-0-13-604259-4](https://en.wikipedia.org/wiki/Special:BookSources/978-0-13-604259-4). <a id="^ref-6"></a>^ref-6
7. <a id="CITEREFDuffy1991"></a> Duffy, David A. \(1991\). _Principles of Automated Theorem Proving_. Wiley. [ISBN](ISBN%20(identifier).md) [978-0-471-92784-6](https://en.wikipedia.org/wiki/Special:BookSources/978-0-471-92784-6). See p. 77. The example here is slightly modified to demonstrate a not-trivial factoring substitution. For clarity, the factoring step, \(5\), is shown separately. In step \(6\), the [fresh variable](fresh%20variable.md) $w'$ was introduced to enable unifiability of \(5\) and \(6\), needed for \(7\). <a id="^ref-7"></a>^ref-7
8. <a id="CITEREFWilkins1973"></a> Wilkins, D. \(1973\). _QUEST: A Non-Clausal Theorem Proving System_ \(Master's Thesis\). University of Essex. <a id="^ref-8"></a>^ref-8
9. <a id="CITEREFMurray1979"></a> Murray, Neil V. \(February 1979\). [_A Proof Procedure for Quantifier-Free Non-Clausal First Order Logic_](https://surface.syr.edu/eecs_techreports/39) \(Technical report\). Electrical Engineering and Computer Science, Syracuse University. 39. \(Cited from Manna, Waldinger, 1980 as: "A Proof Procedure for Non-Clausal First-Order Logic", 1978\) <a id="^ref-9"></a>^ref-9
10. <a id="CITEREFMannaWaldinger1980"></a> [Manna, Zohar](Zohar%20Manna.md); [Waldinger, Richard](Richard%20Waldinger.md) \(January 1980\). ["A Deductive Approach to Program Synthesis"](https://apps.dtic.mil/sti/citations/ADA065558). _[ACM Transactions on Programming Languages and Systems](ACM%20Transactions%20on%20Programming%20Languages%20and%20Systems.md)_. __2__: 90–121. [doi](doi%20(identifier).md):[10.1145/357084.357090](https://doi.org/10.1145%2F357084.357090). [S2CID](S2CID%20(identifier).md#S2CID) [14770735](https://api.semanticscholar.org/CorpusID:14770735). <a id="^ref-10"></a>^ref-10
11. <a id="CITEREFMurray1982"></a> Murray, N.V. \(1982\). "Completely Non-Clausal Theorem Proving". _[Artificial Intelligence](Artificial%20Intelligence%20(journal).md)_. __18__: 67–85. [doi](doi%20(identifier).md):[10.1016/0004-3702\(82\)90011-x](https://doi.org/10.1016%2F0004-3702%2882%2990011-x). <a id="^ref-11"></a>^ref-11
12. <a id="CITEREFTraugott1986"></a> Traugott, J. \(1986\). ["Nested Resolution"](https://doi.org/10.1007/3-540-16780-3_106). _8th International Conference on Automated Deduction. CADE 1986_. [LNCS](LNCS.md). Vol. 230. Springer. pp. 394–403. [doi](doi%20(identifier).md):[10.1007/3-540-16780-3\_106](https://doi.org/10.1007%2F3-540-16780-3_106). [ISBN](ISBN%20(identifier).md) [978-3-540-39861-5](https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-39861-5). <a id="^ref-12"></a>^ref-12
13. <a id="CITEREFSchmerl1988"></a> Schmerl, U.R. \(1988\). "Resolution on Formula-Trees". _[Acta Informatica](Acta%20Informatica.md)_. __25__ \(4\): 425–438. [doi](doi%20(identifier).md):[10.1007/bf02737109](https://doi.org/10.1007%2Fbf02737109). [S2CID](S2CID%20(identifier).md#S2CID) [32702782](https://api.semanticscholar.org/CorpusID:32702782). [Summary](http://www.zentralblatt-math.org/ioport/en/?id=2297405&type=pdf) <a id="^ref-13"></a>^ref-13
14. These notions, called "polarities", refer to the number of explicit or implicit negations found above $p$. For example, $p$ occurs positive in $(p\land q)\lor r$ and in $q\rightarrow p$, negative in $\lnot (p\land q)\lor r$ and in $p\rightarrow q$, and in both polarities in $p\leftrightarrow q$. <a id="^ref-14"></a>^ref-14
15. "$\implies$" is used to indicate simplification after resolution. <a id="^ref-15"></a>^ref-15
16. Here, "$=$" denotes [syntactical term equality modulo renaming](term%20(logic).md#structural%20equality) <a id="^ref-16"></a>^ref-16
17. <a id="CITEREFNieuwenhuisRubio2001"></a> Nieuwenhuis, Robert; Rubio, Alberto \(2001\). ["7. Paramodulation-Based Theorem Proving"](http://www.cmi.ac.in/~madhavan/courses/theorem-proving-2014/reading/Nieuwenhuis-Rubio.pdf) \(PDF\). In Robinson, Alan J.A.; Voronkov, Andrei \(eds.\). [_Handbook of Automated Reasoning_](https://books.google.com/books?id=HxaWA4lep_kC&pg=PR9). Elsevier. pp. 371–444. [ISBN](ISBN%20(identifier).md) [978-0-08-053279-0](https://en.wikipedia.org/wiki/Special:BookSources/978-0-08-053279-0). <a id="^ref-17"></a>^ref-17

## references

This text incorporates [content](https://en.wikipedia.org/wiki/resolution_(logic)) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- <a id="CITEREFRobinson1965"></a> [Robinson](John%20Alan%20Robinson.md), J. Alan \(1965\). ["A Machine-Oriented Logic Based on the Resolution Principle"](https://doi.org/10.1145%2F321250.321253). _[Journal of the ACM](Journal%20of%20the%20ACM.md)_. __12__ \(1\): 23–41. [doi](doi%20(identifier).md):[10.1145/321250.321253](https://doi.org/10.1145%2F321250.321253). [S2CID](S2CID%20(identifier).md#S2CID) [14389185](https://api.semanticscholar.org/CorpusID:14389185).
- <a id="CITEREFLeitsch1997"></a> Leitsch, Alexander \(1997\). [_The Resolution Calculus_](https://books.google.com/books?id=81LmCAAAQBAJ&pg=PA1). Texts in Theoretical Computer Science. An EATCS Series. [Springer](Springer%20Science+Business%20Media.md). [ISBN](ISBN%20(identifier).md) [978-3-642-60605-2](https://en.wikipedia.org/wiki/Special:BookSources/978-3-642-60605-2).
- <a id="CITEREFGallier1986"></a> [Gallier, Jean H.](Jean%20Gallier.md) \(1986\). [_Logic for Computer Science: Foundations of Automatic Theorem Proving_](http://www.cis.upenn.edu/~jean/gbooks/logic.html). [Harper & Row](Harper%20&%20Row.md#Harper%20and%20Row).
- <a id="CITEREFLee1987"></a> Lee, Chin-Liang Chang, Richard Char-Tung \(1987\). [_Symbolic logic and mechanical theorem proving_](https://archive.org/details/symboliclogicmec00chan). Academic Press. [ISBN](ISBN%20(identifier).md) [0-12-170350-9](https://en.wikipedia.org/wiki/Special:BookSources/0-12-170350-9).

## external links

- <a id="CITEREFWeisstein"></a> Alex Sakharov. ["Resolution Principle"](https://mathworld.wolfram.com/ResolutionPrinciple.html). _[MathWorld](MathWorld.md)_.
- <a id="CITEREFWeisstein"></a> Alex Sakharov. ["Resolution"](https://mathworld.wolfram.com/Resolution.html). _[MathWorld](MathWorld.md)_.

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [1965 introductions](https://en.wikipedia.org/wiki/Category:1965%20introductions)
> - [Automated theorem proving](https://en.wikipedia.org/wiki/Category:Automated%20theorem%20proving)
> - [Propositional calculus](https://en.wikipedia.org/wiki/Category:Propositional%20calculus)
> - [Proof theory](https://en.wikipedia.org/wiki/Category:Proof%20theory)
> - [Rules of inference](https://en.wikipedia.org/wiki/Category:Rules%20of%20inference)
> - [Theorems in propositional logic](https://en.wikipedia.org/wiki/Category:Theorems%20in%20propositional%20logic)
