---
aliases:
  - divergence
  - divergence (computer science)
  - terminating
tags:
  - flashcard/active/general/eng/divergence__computer_science_
  - language/in/English
---

# divergence

- {@{"Terminating"}@} redirects here. For other uses, see {@{[Termination](termination%20(disambiguation).md)}@}. <!--SR:!2025-10-07,14,290!2025-10-08,15,290-->

In {@{[computer science](computer%20science.md)}@}, {@{a computation is said to __diverge__}@} if {@{it does not terminate or terminates in an exceptional [state](state%20(computer%20science).md)}@}.<sup>[\[1\]](#^ref-1)</sup><sup>:&hairsp;377&hairsp;</sup> Otherwise {@{it is said to __converge__}@}.<sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup> In domains where {@{computations are expected to be infinite}@}, such as {@{[process calculi](process%20calculi.md)}@}, a computation is said to diverge if {@{it fails to be productive \(i.e. to continue producing an action within a finite amount of time\)}@}. <!--SR:!2025-10-08,15,290!2025-10-09,16,290!2025-10-07,14,290!2025-10-09,16,290!2025-10-09,16,290!2025-10-07,14,290!2025-10-09,16,290-->

## definitions

{@{Various subfields of computer science}@} use {@{varying, but mathematically precise, definitions}@} of what it means for {@{a computation to converge or diverge}@}. <!--SR:!2025-10-07,14,290!2025-10-09,16,290!2025-10-09,16,290-->

### rewriting

In {@{[abstract rewriting](abstract%20rewriting.md)}@}, {@{an [abstract rewriting system](abstract%20rewriting%20system.md) is called convergent}@} if it is {@{both [confluent](confluent%20(abstract%20rewriting).md) and [terminating](abstract%20rewriting%20system.md#termination%20and%20convergence)}@}.<sup>[\[2\]](#^ref-2)</sup> <!--SR:!2025-10-09,16,290!2025-10-08,15,290!2025-10-07,14,290-->

The notation {@{_t_ ↓ _n_}@} means that {@{_t_ reduces to normal form _n_}@} in {@{zero or more [reductions](reduction%20(abstract%20rewriting).md)}@}, {@{_t_<!-- markdown separator -->↓}@} means {@{_t_ reduces to some normal form in zero or more reductions}@}, and {@{_t_<!-- markdown separator -->↑}@} means {@{_t_ does not reduce to a normal form}@}; the latter is {@{impossible in a terminating rewriting system}@}. <!--SR:!2025-10-07,14,290!2025-10-07,14,290!2025-10-07,14,290!2025-10-07,14,290!2025-10-08,15,290!2025-10-09,16,290!2025-10-09,16,290!2025-10-08,15,290-->

In {@{the [lambda calculus](lambda%20calculus.md)}@} {@{an expression is divergent}@} if it has {@{no [normal form](normal%20form%20(abstract%20rewriting).md)}@}.<sup>[\[3\]](#^ref-3)</sup> <!--SR:!2025-10-08,15,290!2025-10-08,15,290!2025-10-07,14,290-->

### denotational semantics

In {@{[denotational semantics](denotational%20semantics.md)}@} {@{an [object function](function%20(computer%20science).md)}@} {@{_f_ : _A_ → _B_}@} can be modelled as {@{a [mathematical function](function%20(mathematics).md)}@} {@{$f:A\cup \{\perp \}\rightarrow B\cup \{\perp \}$}@} where {@{⊥ \([bottom](bottom%20element.md)\)}@} indicates that {@{the object function or its [argument](argument%20(computer%20science).md) diverges}@}. <!--SR:!2025-10-08,15,290!2025-10-09,16,290!2025-10-08,15,290!2025-10-07,14,290!2025-10-09,16,290!2025-10-09,16,290!2025-10-08,15,290-->

### concurrency theory

- See also: ::@:: [Communicating sequential processes § Failures/divergences model](communicating%20sequential%20processes.md#failures%2Fdivergences%20model) <!--SR:!2025-10-09,16,290!2025-10-08,15,290-->

In {@{the calculus of [communicating sequential processes](communicating%20sequential%20processes.md) \(CSP\)}@}, {@{divergence occurs}@} when a process {@{performs an endless series of hidden actions}@}.<sup>[\[4\]](#^ref-4)</sup> For example, consider {@{the following process, defined by CSP notation}@}: {@{$$Clock=tick\rightarrow Clock$$}@} {@{The traces of this process}@} are defined as: {@{$$\operatorname {traces} (Clock)=\{\langle \rangle ,\langle tick\rangle ,\langle tick,tick\rangle ,\ldots \}=\{tick\}^{*}$$}@} Now, consider {@{the following process}@}, which {@{hides the _tick_ event of the _Clock_ process}@}: {@{$$P=Clock\setminus tick$$}@} As $P$ {@{cannot do anything other than perform hidden actions forever}@}, it is equivalent to {@{the process that does nothing but diverge}@}, denoted {@{$\mathbf {div}$}@}. {@{One semantic model of CSP}@} is {@{the failures-divergences model}@}, which refines {@{the stable failures model}@} by distinguishing {@{processes based on the sets of traces after which they can diverge}@}. <!--SR:!2025-10-08,15,290!2025-10-08,15,290!2025-10-09,16,290!2025-10-07,14,290!2025-10-07,14,290!2025-10-08,15,290!2025-10-09,16,290!2025-10-07,14,290!2025-10-08,15,290!2025-10-09,16,290!2025-10-07,14,290!2025-10-07,14,290!2025-10-08,15,290!2025-10-07,14,290!2025-10-07,14,290!2025-10-08,15,290!2025-10-09,16,290-->

## see also

- [Infinite loop](infinite%20loop.md)
- [Termination analysis](termination%20analysis.md)

## notes

1. <a id="CITEREFC.A.R. Hoare1969"></a> C.A.R. Hoare \(Oct 1969\). ["An Axiomatic Basis for Computer Programming"](http://extras.springer.com/2002/978-3-642-63970-8/DVD3/rom/pdf/Hoare_hist.pdf) \(PDF\). _Communications of the ACM_. __12__ \(10\): 576–583. [doi](doi%20(identifier).md):[10.1145/363235.363259](https://doi.org/10.1145%2F363235.363259). [S2CID](S2CID%20(identifier).md#S2CID) [207726175](https://api.semanticscholar.org/CorpusID:207726175). <a id="^ref-1"></a>^ref-1
2. [Baader & Nipkow 1998](#CITEREFBaaderNipkow1998), p. 9. <a id="^ref-2"></a>^ref-2
3. [Pierce 2002](#CITEREFPierce2002), p. 65. <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFRoscoe2010"></a> Roscoe, A.W. \(2010\). _Understanding Concurrent Systems_. Texts in Computer Science. [doi](doi%20(identifier).md):[10.1007/978-1-84882-258-0](https://doi.org/10.1007%2F978-1-84882-258-0). [ISBN](ISBN%20(identifier).md) [978-1-84882-257-3](https://en.wikipedia.org/wiki/Special:BookSources/978-1-84882-257-3). <a id="^ref-4"></a>^ref-4

## references

This text incorporates [content](https://en.wikipedia.org/wiki/divergence_(computer_science)) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- <a id="CITEREFBaaderNipkow1998"></a> [Baader, Franz](Franz%20Baader.md); [Nipkow, Tobias](Tobias%20Nipkow.md) \(1998\). [_Term Rewriting and All That_](https://books.google.com/books?id=N7BvXVUCQk8C&q=Divergent). Cambridge University Press. [ISBN](ISBN%20(identifier).md) [9780521779203](https://en.wikipedia.org/wiki/Special:BookSources/9780521779203).
- <a id="CITEREFPierce2002"></a> [Pierce, Benjamin C.](Benjamin%20C.%20Pierce.md) \(2002\). [_Types and Programming Languages_](Types%20and%20Programming%20Languages.md). MIT Press.
- J. M. R. Martin and S. A. Jassim \(1997\). "[How to Design Deadlock-Free Networks Using CSP and Verification Tools: A Tutorial Introduction](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.19.1615&rep=rep1&type=pdf)" in _Proceedings of the WoTUG-20_.

|                                                                    |                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Stub icon](../../archives/Wikimedia%20Commons/LampFlowchart.svg) | _This [computer science](computer%20science.md) article is a [stub](https://en.wikipedia.org/wiki/Wikipedia:Stub). You can help Wikipedia by [expanding it](https://en.wikipedia.org/w/index.php?title=Divergence_(computer_science)&action=edit)._ |

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Programming language theory](https://en.wikipedia.org/wiki/Category:Programming%20language%20theory)
> - [Process \(computing\)](https://en.wikipedia.org/wiki/Category:Process%20%28computing%29)
> - [Rewriting systems](https://en.wikipedia.org/wiki/Category:Rewriting%20systems)
> - [Lambda calculus](https://en.wikipedia.org/wiki/Category:Lambda%20calculus)
> - [Denotational semantics](https://en.wikipedia.org/wiki/Category:Denotational%20semantics)
> - [Computer science stubs](https://en.wikipedia.org/wiki/Category:Computer%20science%20stubs)
