__ Cyclomatic complexity__ is a [software metric](software%20metric.md) used to indicate the [complexity of a program](programming%20complexity.md). It is a quantitative measure of the number of linearly independent [paths](path%20(graph%20theory).md) through a program's [source code](source%20code.md). It was developed by [Thomas J. McCabe, Sr.](Thomas%20J.%20McCabe,%20Sr..md) in 1976.

Cyclomatic complexity is computed using the [control-flow graph](control-flow%20graph.md) of the program. The nodes of the [graph](directed%20graph.md) correspond to indivisible groups of commands of a program, and a [directed edge](directed%20edge.md) connects two nodes if the second command might be executed immediately after the first command. Cyclomatic complexity may also be applied to individual [functions](function%20(computer%20science).md), [modules](modular%20programming.md), [methods](method%20(computer%20science).md), or [classes](class%20(computer%20science).md) within a program.

One [testing](software%20testing.md) strategy, called [basis path testing](basis%20path%20testing.md) by McCabe who first proposed it, is to test each linearly independent path through the program. In this case, the number of test cases will equal the cyclomatic complexity of the program.<sup>[\[1\]](#^ref-1)</sup>

## description

### definition

> ![See caption](../../archives/Wikimedia%20Commons/Control%20flow%20graph%20of%20function%20with%20loop%20and%20an%20if%20statement%20without%20loop%20back.svg)
>
> A control-flow graph of a simple program. The program begins executing at the red node, then enters a loop \(group of three nodes immediately below the red node\). Exiting the loop, there is a conditional statement \(group below the loop\) and the program exits at the blue node. This graph has nine edges, eight nodes and one [connected component](connected%20component%20(graph%20theory).md), so the program's cyclomatic complexity is 9 − 8 + 2×1 = 3.

There are multiple ways to define cyclomatic complexity of a section of [source code](source%20code.md). One common way is the number of linearly independent [paths](path%20(graph%20theory).md) within it. A set S of paths is linearly independent if the edge set of any path P in S is not the union of edge sets of the paths in some subset of S/P. If the source code contained no [control flow statements](control%20flow.md) \(conditionals or decision points\) the complexity would be 1, since there would be only a single path through the code. If the code had one single-condition [IF statement](if%20statement.md#conditional-statement), there would be two paths through the code: one where the IF statement is TRUE and another one where it is FALSE. Here, the complexity would be 2. Two nested single-condition IFs, or one IF with two conditions, would produce a complexity of 3.

Another way to define the cyclomatic complexity of a program is to look at its [control-flow graph](control-flow%20graph.md), a [directed graph](directed%20graph.md) containing the [basic blocks](basic%20block.md) of the program, with an edge between two basic blocks if control may pass from the first to the second. The complexity _M_ is then defined as<sup>[\[2\]](#^ref-2)</sup>

M=E−N+2P,

where

- _E_ = the number of edges of the graph.
- _N_ = the number of nodes of the graph.
- _P_ = the number of [connected components](component%20(graph%20theory).md).

> ![A [control flow graph](https://en.wikipedia.org/wiki/control_flow_graph) with a cycle from exit to entry \(as used in [cyclomatic complexity](https://en.wikipedia.org/wiki/cyclomatic_complexity) calculation\)](../../archives/Wikimedia%20Commons/Control%20flow%20graph%20of%20function%20with%20loop%20and%20an%20if%20statement.svg)
>
> The same function, represented using the alternative formulation where each exit point is connected back to the entry point. This graph has 10 edges, eight nodes and one [connected component](connected%20component%20(graph%20theory).md), which also results in a cyclomatic complexity of 3 using the alternative formulation \(10 − 8 + 1 = 3\).

An alternative formulation of this, as originally proposed, is to use a graph in which each exit point is connected back to the entry point. In this case, the graph is [strongly connected](strongly%20connected.md). Here, the cyclomatic complexity of the program is equal to the [cyclomatic number](cyclomatic%20number.md) of its graph \(also known as the [first Betti number](Betti%20number.md#example%202%20the%20first%20Betti%20number%20in%20graph%20theory)\), which is defined as<sup>[\[2\]](#^ref-2)</sup>M=E−N+P.

This may be seen as calculating the number of [linearly independent cycles](linearly%20independent%20cycle.md) that exist in the graph: those cycles that do not contain other cycles within themselves. Because each exit point loops back to the entry point, there is at least one such cycle for each exit point.

For a single program \(or subroutine or method\), _P_ always equals 1; a simpler formula for a single subroutine is<sup>[\[3\]](#^ref-3)</sup>M=E−N+2.

Cyclomatic complexity may be applied to several such programs or subprograms at the same time \(to all of the methods in a class, for example\). In these cases, _P_ will equal the number of programs in question, and each subprogram will appear as a disconnected subset of the graph.

McCabe showed that the cyclomatic complexity of a structured program with only one entry point and one exit point is equal to the number of decision points \("if" statements or conditional loops\) contained in that program plus one. This is true only for decision points counted at the lowest, machine-level instructions.<sup>[\[4\]](#^ref-4)</sup> Decisions involving compound predicates like those found in [high-level languages](high-level%20language.md) like `IF cond1 AND cond2 THEN ...` should be counted in terms of predicate variables involved. In this example, one should count two decision points because at machine level it is equivalent to `IF cond1 THEN IF cond2 THEN ...`.<sup>[\[2\]](#^ref-2)</sup><sup>[\[5\]](#^ref-5)</sup>

Cyclomatic complexity may be extended to a program with multiple exit points. In this case, it is equal toπ−s+2,where π is the number of decision points in the program and _s_ is the number of exit points.<sup>[\[5\]](#^ref-5)</sup><sup>[\[6\]](#^ref-6)</sup>

### interpretation

In his presentation "[Software Quality](software%20quality.md) Metrics to Identify Risk"<sup>[\[7\]](#^ref-7)</sup> for the Department of Homeland Security, Tom McCabe introduced the following categorization of cyclomatic complexity:

- 1–10: Simple procedure, little risk
- 11–20: More complex, moderate risk
- 21–50: Complex, high risk
- \> 50: Untestable code, very high risk

<a id="explanation in terms of algebraic topology"></a>

## in algebraic topology

An even subgraph of a graph \(also known as an [Eulerian subgraph](Eulerian%20path.md)\) is one in which every [vertex](vertex%20(graph%20theory).md) is [incident](graph%20(discrete%20mathematics).md#graph) with an even number of edges. Such subgraphs are unions of cycles and isolated vertices. Subgraphs will be identified with their edge sets, which is equivalent to only considering those even subgraphs which contain all vertices of the full graph.

The set of all even subgraphs of a graph is closed under [symmetric difference](symmetric%20difference.md), and may thus be viewed as a [vector space](vector%20space.md) over [GF\(2\)](GF(2).md). This vector space is called the [cycle space](cycle%20space.md) of the graph. The [cyclomatic number](cyclomatic%20number.md) of the graph is defined as the [dimension](dimension%20(vector%20space).md) of this space. Since GF\(2\) has two elements and the cycle space is necessarily finite, the cyclomatic number is also equal to the [2-logarithm](binary%20logarithm.md) of the number of elements in the cycle space.

A [basis](basis%20(linear%20algebra).md) for the cycle space is easily constructed by first fixing a [spanning forest](glossary%20of%20graph%20theory.md#trees) of the graph, and then considering the cycles formed by one edge not in the forest and the path in the forest connecting the endpoints of that edge. These cycles form a basis for the cycle space. The cyclomatic number also equals the number of edges not in a maximal spanning forest of a graph. Since the number of edges in a maximal spanning forest of a graph is equal to the number of vertices minus the number of components, the formula E−N+P defines the cyclomatic number.<sup>[\[8\]](#^ref-8)</sup>

Cyclomatic complexity can also be defined as a relative [Betti number](Betti%20number.md), the size of a [relative homology](relative%20homology.md) group:M:=b1(G,t):=rank⁡H1(G,t),

which is read as "the rank of the first [homology](homology%20(mathematics).md) group of the graph _G_ relative to the [terminal nodes](tree%20(data%20structure).md#terminology) _t_". This is a technical way of saying "the number of linearly independent paths through the flow graph from an entry to an exit", where:

- "linearly independent" corresponds to homology, and [backtracking](backtracking.md) is not double-counted;
- "paths" corresponds to first homology \(a path is a one-dimensional object\); and
- "relative" means the path must begin and end at an entry \(or exit\) point.

This cyclomatic complexity can be calculated. It may also be computed via absolute [Betti number](Betti%20number.md) by identifying the terminal nodes on a given component, or drawing paths connecting the exits to the entrance. The new, augmented graph G~ obtainsM=b1(G~)=rank⁡H1(G~).

It can also be computed via [homotopy](homotopy.md). If a \(connected\) control-flow graph is considered a one-dimensional [CW complex](CW%20complex.md) called X, the [fundamental group](fundamental%20group.md) of X will be π1(X)≅ℤ∗n. The value of n+1 is the cyclomatic complexity. The fundamental group counts how many loops there are through the graph up to homotopy, aligning as expected.

## applications

### limiting complexity during development

One of McCabe's original applications was to limit the complexity of routines during program development. He recommended that programmers should count the complexity of the modules they are developing, and split them into smaller modules whenever the cyclomatic complexity of the module exceeded 10.<sup>[\[2\]](#^ref-2)</sup> This practice was adopted by the [NIST](NIST.md) Structured Testing methodology, which observed that since McCabe's original publication, the figure of 10 had received substantial corroborating evidence. However, it also noted that in some circumstances it may be appropriate to relax the restriction and permit modules with a complexity as high as 15. As the methodology acknowledged that there were occasional reasons for going beyond the agreed-upon limit, it phrased its recommendation as "For each module, either limit cyclomatic complexity to \[the agreed-upon limit\] or provide a written explanation of why the limit was exceeded."<sup>[\[9\]](#^ref-9)</sup>

### measuring the "structuredness" of a program

- Main article: [Essential complexity](essential%20complexity.md)

Section VI of McCabe's 1976 paper is concerned with determining what the control-flow graphs \(CFGs\) of non-[structured programs](structured%20programming.md) look like in terms of their subgraphs, which McCabe identified. \(For details, see [structured program theorem](structured%20program%20theorem.md).\) McCabe concluded that section by proposing a numerical measure of how close to the structured programming ideal a given program is, i.e. its "structuredness". McCabe called the measure he devised for this purpose [essential complexity](essential%20complexity.md).<sup>[\[2\]](#^ref-2)</sup>

To calculate this measure, the original CFG is iteratively reduced by identifying subgraphs that have a single-entry and a single-exit point, which are then replaced by a single node. This reduction corresponds to what a human would do if they extracted a subroutine from the larger piece of code. \(Nowadays such a process would fall under the umbrella term of [refactoring](refactoring.md).\) McCabe's reduction method was later called _condensation_ in some textbooks, because it was seen as a generalization of the [condensation to components used in graph theory](condensation%20(graph%20theory).md#definitions).<sup>[\[10\]](#^ref-10)</sup> If a program is structured, then McCabe's reduction/condensation process reduces it to a single CFG node. In contrast, if the program is not structured, the iterative process will identify the irreducible part. The essential complexity measure defined by McCabe is simply the cyclomatic complexity of this irreducible graph, so it will be precisely 1 for all structured programs, but greater than one for non-structured programs.<sup>[\[9\]](#^ref-9)</sup><sup>:&hairsp;80&hairsp;</sup>

### implications for software testing

Another application of cyclomatic complexity is in determining the number of test cases that are necessary to achieve thorough test coverage of a particular module.

It is useful because of two properties of the cyclomatic complexity, _M_, for a specific module:

- _M_ is an upper bound for the number of test cases that are necessary to achieve a complete [branch coverage](branch%20coverage.md).
- _M_ is a lower bound for the number of paths through the control-flow graph \(CFG\). Assuming each test case takes one path, the number of cases needed to achieve [path coverage](path%20coverage.md) is equal to the number of paths that can actually be taken. But some paths may be impossible, so although the number of paths through the CFG is clearly an upper bound on the number of test cases needed for path coverage, this latter number \(of _possible_ paths\) is sometimes less than _M_.

All three of the above numbers may be equal: branch coverage ≤ cyclomatic complexity ≤ number of paths.

For example, consider a program that consists of two sequential if-then-else statements.

__if__ \(c1\(\)\) f1\(\); __else__ f2\(\); __if__ \(c2\(\)\) f3\(\); __else__ f4\(\);> ![A [control flow graph](https://en.wikipedia.org/wiki/control_flow_graph) of the example function on the [cyclomatic complexity](https://en.wikipedia.org/wiki/cyclomatic_complexity) page.](../../archives/Wikimedia%20Commons/Control%20flow%20graph%20of%20function%20with%20two%20if%20else%20statements.svg)
>
> The control-flow graph of the source code above; the red circle is the entry point of the function, and the blue circle is the exit point. The exit has been connected to the entry to make the graph strongly connected.

In this example, two test cases are sufficient to achieve a complete branch coverage, while four are necessary for complete path coverage. The cyclomatic complexity of the program is 3 \(as the strongly connected graph for the program contains 8 edges, 7 nodes, and 1 connected component\) \(8 − 7 + 2\).

In general, in order to fully test a module, all execution paths through the module should be exercised. This implies a module with a high complexity number requires more testing effort than a module with a lower value since the higher complexity number indicates more pathways through the code. This also implies that a module with higher complexity is more difficult to understand since the programmer must understand the different pathways and the results of those pathways.<sup>[\[11\]](#^ref-11)</sup> Cyclomatic complexity captures only one aspect of software, so relying on it alone may provide an incomplete representation of the overall complexity of a program.

Unfortunately, it is not always practical to test all possible paths through a program. Considering the example above, each time an additional if-then-else statement is added, the number of possible paths grows by a factor of 2. As the program grows in this fashion, it quickly reaches the point where testing all of the paths becomes impractical.

One common testing strategy, espoused for example by the NIST Structured Testing methodology, is to use the cyclomatic complexity of a module to determine the number of [white-box tests](white-box%20testing.md) that are required to obtain sufficient coverage of the module. In almost all cases, according to such a methodology, a module should have at least as many tests as its cyclomatic complexity. In most cases, this number of tests is adequate to exercise all the relevant paths of the function.<sup>[\[9\]](#^ref-9)</sup>

As an example of a function that requires more than mere branch coverage to test accurately, reconsider the above function. However, assume that to avoid a bug occurring, any code that calls either `f1()` or `f3()` must also call the other.<sup>[\[a\]](#^ref-a)</sup> Assuming that the results of `c1()` and `c2()` are independent, the function as presented above contains a bug. Branch coverage allows the method to be tested with just two tests, such as the following test cases:

- `c1()` returns true and `c2()` returns true
- `c1()` returns false and `c2()` returns false

Neither of these cases exposes the bug. If, however, we use cyclomatic complexity to indicate the number of tests we require, the number increases to 3. We must therefore test one of the following paths:

- `c1()` returns true and `c2()` returns false
- `c1()` returns false and `c2()` returns true

Either of these tests will expose the bug.

### correlation to number of defects

Multiple studies have investigated the correlation between McCabe's cyclomatic complexity number with the frequency of defects occurring in a function or method.<sup>[\[12\]](#^ref-12)</sup> Some studies<sup>[\[13\]](#^ref-13)</sup> find a positive correlation between cyclomatic complexity and defects; functions and methods that have the highest complexity tend to also contain the most defects. However, the correlation between cyclomatic complexity and program size \(typically measured in [lines of code](lines%20of%20code.md)\) has been demonstrated many times.<sup>[\[14\]](#^ref-14)</sup> [Les Hatton](Les%20Hatton.md) has claimed<sup>[\[15\]](#^ref-15)</sup> that complexity has the same predictive ability as lines of code. Studies that controlled for program size \(i.e., comparing modules that have different complexities but similar size\) are generally less conclusive, with many finding no significant correlation, while others do find correlation. Some researchers question the validity of the methods used by the studies finding no correlation.<sup>[\[16\]](#^ref-16)</sup> Although this relation likely exists, it is not easily used in practice.<sup>[\[17\]](#^ref-17)</sup> Since program size is not a controllable feature of [commercial software](commercial%20software.md), the usefulness of McCabe's number has been questioned.<sup>[\[12\]](#^ref-12)</sup> The essence of this observation is that larger programs tend to be more complex and to have more defects. Reducing the cyclomatic complexity of code is [not proven](correlation%20does%20not%20imply%20causation.md) to reduce the number of errors or bugs in that code. International safety standards like [ISO 26262](ISO%2026262.md), however, mandate coding guidelines that recommend to monitor and aim to reduce code complexity, where complexity is high additional measures including scrutiny of the more difficult [verification and validation](verification%20and%20validation.md) activities including testing is expected.<sup>[\[18\]](#^ref-18)</sup>

## see also

- [Programming complexity](programming%20complexity.md)
- [Complexity trap](complexity%20trap.md)
- [Computer program](computer%20program.md)
- [Computer programming](computer%20programming.md)
- [Control flow](control%20flow.md)
- [Decision-to-decision path](decision-to-decision%20path.md)
- [Design predicates](design%20predicates.md)
- [Essential complexity](essential%20complexity.md)
- [Halstead complexity measures](Halstead%20complexity%20measures.md)
- [Software engineering](software%20engineering.md)
- [Software testing](software%20testing.md)
- [Static program analysis](static%20program%20analysis.md)
- [Maintainability](maintainability.md)

## notes

1. This is a fairly common type of condition; consider the possibility that `f1` allocates some resource which `f3` releases. <a id="^lower-alpha-1"></a>^lower-alpha-1

## references

1. <a id="CITEREFA J Sobey"></a> A J Sobey. ["Basis Path Testing"](https://users.csc.calpoly.edu/~jdalbey/206/Lectures/BasisPathTutorial/index.html). <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFMcCabe1976"></a> McCabe \(December 1976\). "A Complexity Measure". _IEEE Transactions on Software Engineering_. __SE-2__ \(4\): 308–320. [Bibcode](bibcode%20(identifier).md):[1976ITSEn...2..308M](https://ui.adsabs.harvard.edu/abs/1976ITSEn...2..308M). [doi](doi%20(identifier).md):[10.1109/tse.1976.233837](https://doi.org/10.1109%2Ftse.1976.233837). [S2CID](S2CID%20(identifier).md#S2CID) [9116234](https://api.semanticscholar.org/CorpusID:9116234). <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFPhilip A. Laplante2007"></a> Philip A. Laplante \(25 April 2007\). _What Every Engineer Should Know about Software Engineering_. CRC Press. p. 176. [ISBN](ISBN%20(identifier).md) [978-1-4200-0674-2](https://en.wikipedia.org/wiki/Special:BookSources/978-1-4200-0674-2). <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFFricker2018"></a> Fricker, Sébastien \(April 2018\). ["What exactly is cyclomatic complexity?"](https://www.froglogic.com/blog/tip-of-the-week/what-is-cyclomatic-complexity/). _froglogic GmbH_. Retrieved October 27, 2018. To compute a graph representation of code, we can simply disassemble its assembly code and create a graph following the rules: ... <a id="^ref-4"></a>^ref-4
5. <a id="CITEREFJ. BelzerA. KentA. G. HolzmanJ. G. Williams1992"></a> J. Belzer; A. Kent; A. G. Holzman; J. G. Williams \(1992\). _Encyclopedia of Computer Science and Technology_. CRC Press. pp. 367–368. <a id="^ref-5"></a>^ref-5
6. <a id="CITEREFHarrison1984"></a> Harrison \(October 1984\). "Applying Mccabe's complexity measure to multiple-exit programs". _Software: Practice and Experience_. __14__ \(10\): 1004–1007. [doi](doi%20(identifier).md):[10.1002/spe.4380141009](https://doi.org/10.1002%2Fspe.4380141009). [S2CID](S2CID%20(identifier).md#S2CID) [62422337](https://api.semanticscholar.org/CorpusID:62422337). <a id="^ref-6"></a>^ref-6
7. <a id="CITEREFThomas McCabe Jr.2008"></a> Thomas McCabe Jr. \(2008\). ["Software Quality Metrics to Identify Risk"](http://www.mccabe.com/ppt/SoftwareQualityMetricsToIdentifyRisk.ppt). [Archived](https://web.archive.org/web/20220329072759/http://www.mccabe.com/ppt/SoftwareQualityMetricsToIdentifyRisk.ppt) from the original on 2022-03-29. <a id="^ref-7"></a>^ref-7
8. <a id="CITEREFDiestel2000"></a> Diestel, Reinhard \(2000\). _Graph theory_. Graduate texts in mathematics __173__ \(2 ed.\). New York: Springer. [ISBN](ISBN%20(identifier).md) [978-0-387-98976-1](https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-98976-1). <a id="^ref-8"></a>^ref-8
9. <a id="CITEREFArthur H. WatsonThomas J. McCabe1996"></a> Arthur H. Watson; Thomas J. McCabe \(1996\). ["Structured Testing: A Testing Methodology Using the Cyclomatic Complexity Metric"](http://www.mccabe.com/pdf/mccabe-nist235r.pdf) \(PDF\). NIST Special Publication 500-235. <a id="^ref-9"></a>^ref-9
10. <a id="CITEREFPaul C. Jorgensen2002"></a> Paul C. Jorgensen \(2002\). [_Software Testing: A Craftsman's Approach, Second Edition_](https://books.google.com/books?id=Yph_AwAAQBAJ&pg=PA150) \(2nd ed.\). CRC Press. pp. 150–153. [ISBN](ISBN%20(identifier).md) [978-0-8493-0809-3](https://en.wikipedia.org/wiki/Special:BookSources/978-0-8493-0809-3). <a id="^ref-10"></a>^ref-10
11. <a id="CITEREFEbertCainAntoniolCounsell2016"></a> Ebert, Christof; Cain, James; Antoniol, Giuliano; Counsell, Steve; Laplante, Phillip \(2016\). "Cyclomatic Complexity". _IEEE Software_. __33__ \(6\): 27–29. [Bibcode](bibcode%20(identifier).md):[2016ISoft..33f..27E](https://ui.adsabs.harvard.edu/abs/2016ISoft..33f..27E). [doi](doi%20(identifier).md):[10.1109/MS.2016.147](https://doi.org/10.1109%2FMS.2016.147). [ISSN](ISSN%20(identifier).md) [1937-4194](https://search.worldcat.org/issn/1937-4194). <a id="^ref-11"></a>^ref-11
12. <a id="CITEREFNorman E FentonMartin Neil1999"></a> Norman E Fenton; Martin Neil \(1999\). ["A Critique of Software Defect Prediction Models"](http://www.eecs.qmul.ac.uk/~norman/papers/defects_prediction_preprint105579.pdf) \(PDF\). _IEEE Transactions on Software Engineering_. __25__ \(3\): 675–689. [Bibcode](bibcode%20(identifier).md):[1999ITSEn..25..675F](https://ui.adsabs.harvard.edu/abs/1999ITSEn..25..675F). [CiteSeerX](CiteSeerX%20(identifier).md) [10.1.1.548.2998](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.548.2998). [doi](doi%20(identifier).md):[10.1109/32.815326](https://doi.org/10.1109%2F32.815326). `{{[cite journal](https://en.wikipedia.org/wiki/Template:Cite%20journal)}}`: Cite uses deprecated parameter `|citeseerx=` \([help](https://en.wikipedia.org/wiki/Help:CS1%20errors#deprecated_params)\) <a id="^ref-12"></a>^ref-12
13. <a id="CITEREFSchroeder, Mark1999"></a> Schroeder, Mark \(1999\). "A Practical guide to object-oriented metrics". _IT Professional_. __1__ \(6\): 30–36. [Bibcode](bibcode%20(identifier).md):[1999ITPro...1f..30S](https://ui.adsabs.harvard.edu/abs/1999ITPro...1f..30S). [doi](doi%20(identifier).md):[10.1109/6294.806902](https://doi.org/10.1109%2F6294.806902). [S2CID](S2CID%20(identifier).md#S2CID) [14945518](https://api.semanticscholar.org/CorpusID:14945518). <a id="^ref-13"></a>^ref-13
14. <a id="CITEREFAfriyieLabiche2021"></a> Afriyie, Daniel; Labiche, Yvan \(2021\). "Predictors of Software Metric Correlation: A Non-parametric Analysis". _2021 IEEE 21st International Conference on Software Quality, Reliability and Security \(QRS\)_. pp. 524–533. [Bibcode](bibcode%20(identifier).md):[2021qrs..conf...63A](https://ui.adsabs.harvard.edu/abs/2021qrs..conf...63A). [doi](doi%20(identifier).md):[10.1109/QRS54544.2021.00063](https://doi.org/10.1109%2FQRS54544.2021.00063). [ISBN](ISBN%20(identifier).md) [978-1-6654-5813-9](https://en.wikipedia.org/wiki/Special:BookSources/978-1-6654-5813-9). <a id="^ref-14"></a>^ref-14
15. <a id="CITEREFLes Hatton2008"></a> Les Hatton \(2008\). ["The role of empiricism in improving the reliability of future software"](http://www.leshatton.org/TAIC2008-29-08-2008.html). version 1.1. <a id="^ref-15"></a>^ref-15
16. <a id="CITEREFKan2003"></a> Kan \(2003\). _Metrics and Models in Software Quality Engineering_. Addison-Wesley. pp. 316–317. [ISBN](ISBN%20(identifier).md) [978-0-201-72915-3](https://en.wikipedia.org/wiki/Special:BookSources/978-0-201-72915-3). <a id="^ref-16"></a>^ref-16
17. <a id="CITEREFG.S. Cherf1992"></a> G.S. Cherf \(1992\). "An Investigation of the Maintenance and Support Characteristics of Commercial Software". _Journal of Software Quality_. __1__ \(3\): 147–158. [doi](doi%20(identifier).md):[10.1007/bf01720922](https://doi.org/10.1007%2Fbf01720922). [ISSN](ISSN%20(identifier).md) [1573-1367](https://search.worldcat.org/issn/1573-1367). [S2CID](S2CID%20(identifier).md#S2CID) [37274091](https://api.semanticscholar.org/CorpusID:37274091). <a id="^ref-17"></a>^ref-17
18. <a id="mwAmQ"></a> [_ISO 26262-3:2011\(en\) Road vehicles — Functional safety — Part 3: Concept phase_](https://www.iso.org/obp/ui/#iso:std:iso:26262:-3:ed-1:v1:en). International Standardization Organization. <a id="^ref-18"></a>^ref-18

## external links

- [Generating cyclomatic complexity metrics with Polyspace](https://www.mathworks.com/discovery/cyclomatic-complexity.html)
- [The role of empiricism in improving the reliability of future software](https://www.leshatton.org/Documents/TAIC2008-29-08-2008.pdf)
- [McCabe's Cyclomatic Complexity and Why We Don't Use It](https://web.archive.org/web/20230203195937/https://www.cqse.eu/en/news/blog/mccabe-cyclomatic-complexity//)

> [Category](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Software metrics](https://en.wikipedia.org/wiki/Category:Software%20metrics)
