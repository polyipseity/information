"""The answer-line style pinned on the owner's forty hand-corrected lines.

The lines below are the owner's hand corrections of 2026-11-13; the acceptance
corpus for the card style.  Each entry names the file and line it was copied
from, and the text is verbatim, so the fixture is the record rather than a
reading of the tree: 34 lines from the parent repository and 6 from the
private submodule.  A rule that rejects one of them has drifted from the style
the owner wrote by hand, whatever its own docstring says.
"""

from collections.abc import Callable

from main_mods.models import ValidationContext, ValidationMessage
from main_mods.question_blocks import (
    answer_explanation_shape,
    answer_sentence_all_hidden,
)
from main_mods.rules import answer_formula_alone, answer_visible_calculation

from .test_question_blocks import make_ctx

"""Public symbols exported by this module (none)."""
__all__ = ()

"""Frontmatter that makes a fixture a flashcard-enabled academic note."""
FRONT = """---
tags:
  - flashcard/inactive/special/academia/HKUST/FINA_4103
---

"""

"""The rules a corrected answer line passes, each with the defect it names."""
CORRECTED_RULES: tuple[Callable[[ValidationContext], list[ValidationMessage]], ...] = (
    answer_explanation_shape,
    answer_sentence_all_hidden,
    answer_visible_calculation,
)

"""The five lines that keep a formula alone by the owner's choice.

Each receives a per-line suppression when the content pass reaches it, so this
set pins the rule where it stands today rather than demanding a rewrite of the
line.
"""
FORMULA_ALONE_KEPT = frozenset(
    {
        "special/academia/HKUST/FINA 2303/quiz 2 derivative.md:32",
        "special/academia/HKUST/ISOM 2700/questions/quiz 2 derivative.md:71",
        "special/academia/HKUST/ISOM 2700/questions/quiz 2 derivative.md:107",
        "special/academia/HKUST/ELEC 2400/tutorials/week 2 tutorial 1/tutorial.md:105",
        "private/special/academia/HKUST/ELEC 2100/questions/quiz 3.md:60",
    }
)

"""The owner's forty corrected lines, each with the file and line it came from."""
CORPUS: tuple[tuple[str, str], ...] = (
    (
        "special/academia/HKUST/ACCT 3020/dilutive securities and earnings per share.md:448",
        # Recorded for the gallery, not pinned by the answer-line rules: the
        # owner wrote `_Explanation._`, a lead-in no answer-line rule reads, so
        # this line is a prose card. Its two clozes would break the short-line
        # rule if the label were `- explanation:`, which is why it stays as the
        # owner wrote it.
        "> _Explanation._ Liability-settled SARs are {@{remeasured each reporting period}@}, so compensation expense can {@{move up or down before settlement}@}.",
    ),
    (
        "special/academia/HKUST/COMP 3111H/UML.md:92",
        "In practice, most associations are {@{binary}@}. A few are {@{unary}@}, and even fewer are {@{ternary or higher degree}@}. Often, {@{a ternary or higher degree association}@} can be {@{replaced by multiple binary associations, but not always}@}.",
    ),
    (
        "special/academia/HKUST/COMP 3111H/UML.md:343",
        'In use-case modelling {@{a precondition}@} is {@{a statement about the required state of the system and/or actors that allows the use case to be initiated}@}, e.g. {@{"balance ≥ \\$100"}@} in an ATM withdrawal use case. It describes {@{what conditions are required to start the use case}@} \\(the "what"\\), but it deliberately avoids {@{specifying how those conditions are achieved}@} \\(the "how"\\).',
    ),
    (
        "special/academia/HKUST/COMP 3111H/UML.md:746",
        "Students sometimes model {@{an association between two classes}@} without specifying {@{whether it is ordered, unique, or has subset/xor constraints}@} (e.g., {@{a car}@} can be owned by {@{either a company or a person but not both}@}). The error comes from treating {@{associations as unqualified links}@}. To correct this, add {@{the appropriate OCL constraint syntax}@} \\(e.g. {@{`{xor}`, `{subset}`, `{ordered, FIFO}`}@}\\) on {@{the association line}@}.",
    ),
    (
        "special/academia/HKUST/COMP 3111H/questions/index.md:58",
        "> - explanation: Multiplicities are {@{_hard_ constraints that must be followed at all times}@}. <p> Consider {@{creating a student or a course}@}. There is no {@{_natural_ way to associate courses to a student or students to a course}@}. So we must {@{allow 0 when creating a student or a course}@}. The notes next to the multiplicities are {@{meant to fill in the _missing_ semantics}@}.",
    ),
    (
        "special/academia/HKUST/COMP 3511/labs/lab 3/lab.md:308",
        "> - explanation: The parent of the first `fork()` returns {@{a non-zero process identifier (PID), which is true and ends the test}@}, so it {@{never runs the second `fork()`}@}. The child returns {@{$0$, so it runs the second `fork()`}@}. That second call splits {@{the child the same way}@}. {@{The child of that second call}@} is {@{the single process that reaches the `else` branch}@}.",
    ),
    (
        "special/academia/HKUST/COMP 3511/labs/lab 6/lab.md:612",
        "> - explanation: {@{Thread 2's `c = 2`}@} stands alone: it may be {@{the last write of `c`, which makes `2` a possible answer}@}. Every other run ends at {@{thread 1's `c = a - b`, whose two reads need not agree}@}, so the answer turns on {@{which write each read sees}@}. The choice starts at {@{thread 1's first read, of `b` in `a = b + 1`}@}, which can see {@{3 or 10}@}. Reading 10 means {@{thread 2 has already run `a = 13`}@}, so {@{thread 1 writes `a = 11`}@} afterwards and the subtraction can then {@{read only 11 and 10, giving `1`}@}. Reading {@{3 means thread 1 writes `a = 4`}@}, and {@{the pair the subtraction reads}@} may then be {@{4 and 3, 4 and 10, 13 and 3, or 13 and 10}@}, giving {@{`1`, `-6`, `10` and `3`}@}. {@{With `2`}@} these are {@{the five values}@}.",
    ),
    (
        "special/academia/HKUST/ECON 2103/questions.md:52",
        "> - explanation: Do not consider {@{the already spent $10&nbsp;000 as it is a sunk cost}@}. Only consider {@{the marginal profit}@}, which is {@{the selling price, perhaps subtracted by the repair cost if you decide to repair the transmission}@}. The decision for which {@{the marginal profit is higher}@} is what you should do.",
    ),
    (
        "special/academia/HKUST/ECON 2103/questions.md:79",
        '> - explanation: Seat belt makes one {@{less likely to be seriously injured in accidents}@}, but the drivers may {@{drive faster}@} because {@{they feel "safer", compensating for the risk reduction}@}. We do not know if {@{the resulting risk is lower or higher than the resulting one}@} _theoretically_. But from our _empirical_ studies (studies of {@{having seat belt laws vs. not having seat belt laws in the real world}@}), {@{compulsory use of seat belt does reduce the no. of causality}@}.',
    ),
    (
        "special/academia/HKUST/ECON 2103/questions.md:147",
        "> - explanation: If {@{the production–possibility frontiers (PPFs) for X and Y are both linear}@}, then {@{full specialization in one of the goods}@} will always lead to {@{the lowest marginal (or equal) opportunity cost for both A and B}@}. Their {@{total output will be the _largest_}@}. <p> Note that if {@{the PPFs are nonlinear}@}, then {@{full specialization may not always produce the _largest_ total output}@}, and {@{may or may not lead to a _larger_ total output}@}.",
    ),
    (
        "special/academia/HKUST/ECON 2103/questions.md:169",
        "> - explanation: We only consider {@{CA when thinking what to specialize}@}. For Teresa, {@{his/her opportunity cost for B is $$10 / 20 = 0.5~\\text{A/B}$$}@}, while {@{that for Astor is $$30 / 30 = 1~\\text{A/B}$$}@}. So {@{Teresa has CA in B and better specializes in B}@}.",
    ),
    (
        "special/academia/HKUST/ECON 2103/questions.md:191",
        "> - explanation: Consider {@{the marginal (opportunity) costs for Albert if he specializes in meat: $$16 / 24 = 2 / 3~\\mathrm{potato/meat}\\,.$$}@} Also consider that if he {@{specializes in potato: $$24 / 16 = 1.5~\\mathrm{meat/potato}\\,.$$}@} If {@{the marginal cost is lower than the marginal benefit}@}, then {@{Albert will exchange}@}. In this case, if {@{he specializes in meat}@}, his {@{marginal cost of meat is 2/3 potatoes per meat}@}, which is lower than {@{the marginal benefit of 1 potato per meat (market price) in the market}@}. So {@{he will specialize in meat and likes exchange}@}.",
    ),
    (
        "special/academia/HKUST/ECON 2103/questions.md:203",
        "> - explanation: Note that {@{100 cars is the marginal (opportunity) cost of an airplane}@}. Thus, simply check if {@{the change in airplane multiplied by -100 equals the change in cars}@}.",
    ),
    (
        "special/academia/HKUST/ECON 2103/questions.md:281",
        "> - explanation: Tax burden depends on {@{both the elasticities of the demand and supply curve}@}. Since neither {@{curves are very unlikely to be perfectly elastic in the real world}@}, both sellers and consumers {@{bear the tax burden}@}. However, we {@{cannot tell the distribution of tax burden}@} unless {@{we have more information}@}.",
    ),
    (
        "special/academia/HKUST/ELEC 1100/tutorials/week 11 tutorial 1/tutorial.md:43",
        '> - explanation: {@{A "0 1" sensor rotation means left sensor not on white, right sensor on white, which corresponds to rotating left.}@}',
    ),
    (
        "special/academia/HKUST/ELEC 1100/tutorials/week 11 tutorial 1/tutorial.md:55",
        "> - explanation: {@{`digitalWrite` treats any nonzero value as HIGH. Only `1==5` evaluates to zero, and the remaining evaluates to nonzero.}@}",
    ),
    (
        "special/academia/HKUST/ELEC 2400/tutorials/week 2 tutorial 1/tutorial.md:105",
        "> - explanation:  Every {@{arrow points into the node}@}, so no {@{current carries a negative sign for its direction}@} and the equation is {@{the bare sum of the four values}@}. {@{A sum of four currents that all run inward}@} can only be {@{zero if some of the values are negative}@}, which means {@{at least one of the four currents in fact runs outward, against its arrow}@}. {@{The values $3$, $2$, $-4$, and $-1$}@} satisfy it as {@{$(+3) + (+2) + (-4) + (-1) = 0$}@}, and so do their {@{negations,  $(-3) + (-2) + (+4) + (+1) = 0$ }@}, since {@{negating all four values negates the sum}@}.",
    ),
    (
        "special/academia/HKUST/FINA 2303/questions.md:127",
        "> - explanation: For 3, if {@{arbitrage exists}@}, this likely means {@{there are some barriers preventing the arbitrage from being eliminated by itself}@}, so {@{the market is not competitive}@}.",
    ),
    (
        "special/academia/HKUST/FINA 2303/questions.md:202",
        "> - explanation: The price, when {@{evaluated at any time, is always the same}@}. However, the price represents {@{the present value at the _time of evaluation_}@}, so this means...",
    ),
    (
        "special/academia/HKUST/FINA 2303/questions.md:212",
        "> - explanation: Compare {@{the two annuities}@}. The latter is {@{simply the former}@}, but with {@{all cash flows moving backward in time by 1 period}@}.",
    ),
    (
        "special/academia/HKUST/FINA 2303/questions.md:439",
        '> - annotation: If you accidentally {@{subtract from the project B \\(smaller\\) the project A \\(larger\\)}@}, you still get {@{the same incremental IRR}@}. <p> This does not mean {@{you should accept the "alternative" project, project B}@}. It still means {@{you should accept project A}@}. Consider {@{the cash flows you obtained by subtracting in the wrong direction}@}. It becomes {@{a loan/delayed investment}@}, so {@{the IRR decision rule is reversed}@}.',
    ),
    (
        "special/academia/HKUST/FINA 2303/questions.md:724",
        "> - annotation: What if {@{the alternative option \\(if not reused in a new project\\)}@} is {@{to leave the equipment to be depreciated}@} \\(i.e. {@{assume that no firms want to buy it}@}\\)? In that case, {@{the initial cost is \\$0}@}. Additionally, you need to be {@{careful when handling the depreciation of that asset for the new project}@}. The principle is that {@{you should compare the cash flows between taking and not taking the project}@}.",
    ),
    (
        "special/academia/HKUST/FINA 2303/questions.md:1189",
        "> - explanation: Even though {@{its SD is higher}@}, its correlation with the original stock is {@{0 compared to 1 for the other stock}@}. {@{The effect of lack of correlation}@} \\(should\\) {@{outweighs that of higher SD}@}.",
    ),
    (
        "special/academia/HKUST/FINA 2303/questions.md:1219",
        "> - annotation: ρ=1 corresponds to {@{the blue line}@}. ρ=0 corresponds to {@{the red line}@}. <p> ρ=−1 {@{does not correspond to any line}@}. Two stocks are enough: simply take {@{two stocks and hold them with equal weights}@}, then {@{volatility is 0}@}.",
    ),
    (
        "special/academia/HKUST/FINA 2303/questions.md:1307",
        "> - explanation: {@{Same expected return}@} means {@{they have the same price}@}. \\({@{Higher expected return}@} means {@{lower price}@}.\\) If we assume {@{they are wrongly priced}@}, then {@{Rackspace is underpriced, SolarWinds is overpriced, or both}@}. <p> Alternatively, if we assume {@{they are correctly priced}@}, then {@{Rackspace has a higher risk-free return rate}@}. <p> Both cases yield {@{an arbitrage opportunity}@}.",
    ),
    (
        "special/academia/HKUST/FINA 2303/quiz 2 derivative.md:32",
        "> - explanation: Assume {@{the par value is \\$1}@}. The current {@{price of the bond is: $$\\frac {0.03} {0.025} \\left(1 - \\frac 1 {{1.025}^{20} } \\right) + \\frac 1 {{1.025}^{20} } \\approx \\$1.07794581 \\,.$$}@} The price {@{after 2 years is: $$\\frac {0.03} {0.015} \\left(1 - \\frac 1 {{1.015}^{16} } \\right) + \\frac 1 {{1.015}^{16} } \\approx \\$1.21196896 \\,.$$}@} {@{The capital gain rate}@} is {@{$$\\frac {1.21196896 - 1.07794581} {1.07794581} \\approx 0.12433199 = 12.433199\\% \\,.$$}@}",
    ),
    (
        "special/academia/HKUST/FINA 2303/quiz 2 derivative.md:43",
        "> - annotation: It is okay that {@{the dividend growth rate exceeds the required rate of return}@}. However, the dividend discount model {@{does not work in this case}@}: {@{you would get negative stock price}@}.",
    ),
    (
        "special/academia/HKUST/ISOM 2700/questions/quiz 1 derivative.md:46",
        "> - explanation: This is {@{asking for the _flow time_}@}. We also {@{assume the process is _stable_}@}. Thus, simply {@{add up the activity time: 5+15+60 = 80&nbsp;minutes}@}.",
    ),
    (
        "special/academia/HKUST/ISOM 2700/questions/quiz 1 derivative.md:78",
        "> - explanation: The process capacity is {@{calculated above as 12 units per hour}@}. In testing, each {@{unit takes 60/20 = 3&nbsp;minutes}@}. The capacity is thus {@{60/3 = 20 units per hour}@}. Thus, {@{utilization is 12/20 = 60%}@}.",
    ),
    (
        "special/academia/HKUST/ISOM 2700/questions/quiz 1 derivative.md:98",
        "> - explanation: For people, each {@{unit takes 5+15 = 20&nbsp;minutes}@}. Its capacity is {@{3 units per hour}@}. For transporter, each {@{unit takes 15&nbsp;minutes}@}. Its capacity is {@{4\\*3 = 12 units per hour}@}. For machine, each {@{unit takes 60&nbsp;minutes}@}. Its capacity is {@{1\\*20 = 20 units per hour}@}. So {@{people is the bottleneck resource}@}, thus its {@{capacity is the process capacity}@}.",
    ),
    (
        "special/academia/HKUST/ISOM 2700/questions/quiz 1 derivative.md:124",
        "> - explanation: {@{The required average inventory}@} is {@{4 shows}@}. {@{The required arrival rate}@} is {@{3 shows per hour}@}. By {@{Little's law}@}, {@{required flow time = 4/3&nbsp;hours = 80&nbsp;minutes}@}.",
    ),
    (
        "special/academia/HKUST/ISOM 2700/questions/quiz 2 derivative.md:71",
        "> - explanation: Consider {@{one machine and its queue}@}. {@{The average number of customers}@} in the system = {@{0.375/\\(1–0.375\\) = 0.6}@}. There are two machines, so {@{the answer is 0.6\\*2 = 1.2}@}.",
    ),
    (
        "special/academia/HKUST/ISOM 2700/questions/quiz 2 derivative.md:107",
        "> - explanation: {@{The average waiting time in queue}@} is: {@{$$\\frac {\\rho} {\\mu - \\lambda} = \\frac 1 \\mu \\frac {\\rho} {1 - \\rho} \\,.$$}@} {@{A certain increase in arrival rate}@} increases {@{$\\rho$ by the same amount}@}. {@{$\\rho / (1 - \\rho)$ means the average waiting time in queue}@} would {@{increase by more than that certain amount}@}.",
    ),
    (
        "special/academia/HKUST/ISOM 2700/questions/quiz 2 derivative.md:116",
        "> - explanation: Arrival rate is {@{5 customers per hour}@}. Service rate per seat is {@{2 customers per hour}@}. So you need {@{5/2 = 2.5&nbsp;seats at least}@}. Round {@{it up to 3}@}.",
    ),
    (
        "private/special/academia/HKUST/COMP 3111H/questions/quiz 14.md:106",
        "> - explanation: For {@{a \\(large\\) loop with _n_ iterations}@}, execute {@{loops for 0, 1, 2 passes}@}; then {@{test _m_ passes for some _m &lt; n_}@}, and finally {@{_n−1_, _n_, _n+1_ passes to cover boundary behavior}@}. So a loop {@{in general requires at least _7 minimum test cases_}@}.",
    ),
    (
        "private/special/academia/HKUST/ELEC 2100/questions/quiz 1.md:43",
        "> Explanation: {@{Discrete-time sinusoids are equivalent}@} only when {@{their digital frequencies differ by an integer multiple of $2\\pi$}@}; here $\\frac{21\\pi}{5}-\\frac{2\\pi}{5}=\\frac{19\\pi}{5}$, which is {@{not an integer multiple of $2\\pi$}@}, so this equality is the {@{false statement}@}.",
    ),
    (
        "private/special/academia/HKUST/ELEC 2100/questions/quiz 2.md:62",
        "> Explanation: {@{A periodic impulse train}@} has {@{equal Fourier-series weight at every harmonic line}@}; evaluating one period with the {@{sifting property of the impulse}@} gives {@{$F_k=1/T$ for every integer $k$, not only for the DC term}@}.",
    ),
    (
        "private/special/academia/HKUST/ELEC 2100/questions/quiz 2.md:115",
        "> Explanation: {@{The Fourier series of a periodic signal}@} produces {@{a discrete line spectrum at harmonic frequencies}@}, not {@{a continuous spectrum}@}; {@{continuous frequency-domain descriptions}@} belong to {@{the Fourier transform of aperiodic signals}@}.",
    ),
    (
        "private/special/academia/HKUST/ELEC 2100/questions/quiz 3.md:43",
        "> Explanation: {@{A pure delay of $t_0$ seconds}@} has {@{frequency response $H(\\omega)=e^{-j\\omega t_0}$}@}, which keeps {@{unit magnitude across frequency}@} and contributes only {@{the linear phase shift $-\\omega t_0$}@}; here $t_0=1$.",
    ),
    (
        "private/special/academia/HKUST/ELEC 2100/questions/quiz 3.md:60",
        "> Explanation: Since {@{$(2+j\\omega)(2-j\\omega)=4+\\omega^2$}@}, {@{the spectrum is real and even}@}; under {@{Fourier-transform symmetry}@}, that means {@{the time-domain signal is real and even rather than complex-valued}@}.",
    ),
)


def corpus_context(line: str) -> ValidationContext:
    """Return the context a corpus line is judged in, behind a note's frontmatter."""
    return make_ctx(FRONT + line + "\n", name="questions.md")


def test_corpus_records_forty_distinct_lines():
    """The corpus is the owner's forty corrections, one entry each."""
    assert len(CORPUS) == 40
    assert len({source for source, _ in CORPUS}) == 40


def test_corpus_passes_every_corrected_line_rule():
    """A line the owner wrote by hand passes the rules that judge it."""
    findings = [
        (rule.__name__, source, message.msg)
        for source, line in CORPUS
        for rule in CORRECTED_RULES
        for message in rule(corpus_context(line))
    ]
    assert not findings, findings


def test_corpus_keeps_the_formula_alone_warnings():
    """Exactly the five formulas the owner keeps alone warn, and nothing else does."""
    flagged = {
        source for source, line in CORPUS if answer_formula_alone(corpus_context(line))
    }
    assert flagged == set(FORMULA_ALONE_KEPT)
