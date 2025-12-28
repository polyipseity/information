---
aliases:
  - FINA 3103 efficient-market hypothesis
  - FINA3103 efficient-market hypothesis
  - HKUST FINA 3103 efficient-market hypothesis
  - HKUST FINA3103 efficient-market hypothesis
  - efficient-market hypothesis
tags:
  - flashcard/active/special/academia/HKUST/FINA_3103/efficient-market_hypothesis
  - language/in/English
---

# efficient-market hypothesis

- HKUST FINA 3103

---

- see: [general/efficient-market hypothesis](../../../../general/efficient-market%20hypothesis.md)

The __efficient market hypothesis__ (__EMH__) states that in a _financial market_ prices fully reflect all available information about the value of assets. The concept was formalized by Eugene Fama in 1970 and has since become central to modern finance theory.

## definition

Fama defines an _informationally efficient_ market as one where “market prices reflect all available information about assets’ value.” The hypothesis raises three key questions: what counts as _all_ available information, how can we quantify it, and whether traders can earn abnormal profits if some relevant data has not yet been priced in.

_Example_: On March 17 2018 the news that Facebook had shared user data with Cambridge Analytica broke. The scandal was reported on that day and led to lawsuits, while Mark Zuckerberg testified before Congress on April 12. If the market were perfectly efficient, the price of Facebook’s stock should have adjusted immediately after the first report. Empirical evidence suggests that the actual share price drop sharply when the news broke out, providing evidence for efficient-market hypothesis.

## assumptions

The EMH rests on several assumptions. First, news events arrive randomly; for instance, the Facebook–Cambridge Analytica scandal was unpredictable. Second, investors are rational and use all information to maximize expected returns. Finally, a non‑arbitrage condition holds so that no riskless profit can be obtained from mispriced securities.

## types of information

Investors may access various kinds of data: public market data, public fundamental information, and insider or private information.

1. _Public market data_ ::@:: – historical prices, trading volume, dividends, and other observable statistics. <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->
2. _Public fundamental information_ ::@:: – apart from public market data, additionally includes news releases, corporate announcements, macroeconomic reports. <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->
3. _Insider or private information_ ::@:: – material facts not yet public. <!--SR:!2025-12-25,4,270!2025-12-25,4,270-->

In an efficient market each of these categories should be incorporated into the current price as soon as it becomes known.

## mechanism

When new information $I$ becomes available, an efficient price $P_{EM}$ would equal the value implied by all known data. Suppose $P_{EM}= \$100$ but the current market price is $P=\$120$; this discrepancy shows that the market has not yet incorporated $I$. A rational trader who knows $I$ could trade on the expectation that the price will converge toward $P_{EM}$, earning abnormal returns until the mispricing disappears.

## three forms of market efficiency

The hypothesis can be split into three progressively stronger versions that differ in the amount of information that must already be priced in.

_Weak‑form efficiency_ requires that _past_ prices, trading volumes and other historical market data are fully reflected in today’s price. If a trader could predict future returns from past patterns—say, using a moving‑average strategy—then the market would not be weak‑form efficient.  A concrete illustration is a simple technical indicator such as the 50‑day moving average: if stock prices systematically rose when the short‑term average crossed above the long‑term one, an investor could earn abnormal profits, contradicting weak‑form efficiency.

_Semi‑strong‑form efficiency_ expands the set of information to include all publicly available data, such as earnings releases, macroeconomic reports or news about a scandal. In this case even sudden announcements—like Facebook’s Cambridge Analytica breach—must be absorbed immediately by the price. A rapid drop in Facebook shares after the first report would support semi‑strong efficiency.

_Strong‑form efficiency_ is the most demanding: every piece of information, public or private (including insider data), is already incorporated. Under this form no rational trader could profit from any known fact, even if that fact is confidential. Because it rules out even insider trading, strong form is often regarded as too strict for real markets.

The hierarchy is therefore _strong > semi‑strong > weak_. Each stronger form imposes stricter predictions about price behaviour and the possibility of abnormal returns.

### static vs. dynamic efficiency

Market efficiency is normally conceived as a static property: the current price $P_t$ should equal the fair value that incorporates all information available at time $t$. However, when new data arrives, prices may adjust gradually rather than instantaneously. This is also what happens in practice, as prices cannot instantaneously change. This leads to a dynamic view of efficiency.

Let $\{P_{t+s}\}_{s\ge0}$ denote the price process after an event at time $t$. In a truly efficient market, the limit $$\lim_{s\to\infty} P_{t+s}=P_t^{*},$$ where $P_t^{*}$ is the fair value based on the new information. The speed with which $\{P_{t+s}\}$ converges to $P_t^{*}$ reflects how quickly markets discover and disseminate news. Empirical studies often measure this convergence by examining how quickly abnormal returns vanish after an announcement, thereby testing whether real markets satisfy the three forms of market efficiency.

### weak-form efficiency

Weak‑form efficiency requires that all information contained in past market data—historical prices, volumes and other trading statistics—is already embedded in today’s price $P_t$.  Because the price has already absorbed earlier information, a rational investor cannot anticipate future movements from any pattern in historical series.  Consequently the price process is usually modelled as a _random walk_, $$P_t \;=\; P_{t-1}+ \varepsilon_t ,$$ where the shock $ \varepsilon_t$ is unpredictable and has zero mean.  If the market truly behaved this way, technical analysis would have no economic justification: attempts to profit from chart patterns or moving‑average crossovers would fail because future price changes are independent of past values.

#### evidence for weak-form efficiency

A common test is to compare simulated random‑walk paths with real stock prices.  In one illustration the daily closing prices of _The Gap_ were generated by a random‑walk process and then plotted together with the actual series.  The empirical series showed irregular movements that resembled the simulation, suggesting that price changes behaved like white noise.

More systematic evidence comes from tests for serial correlation in daily returns.  Solnik (1973) found that the coefficient of autocorrelation was close to zero in most European markets: 0.03 in the United States, 0.08 in the United Kingdom, –0.01 in France and –0.02 in Italy, with small positive values elsewhere.  These negligible correlations imply that past returns contain essentially no predictive power for next‑day returns. Another strand of evidence comes from studies on individual investor behaviour.  Barber and Odean (2000) examined turnover rates of retail traders.  They found that investors who traded more frequently earned similar gross returns but lower net returns, a pattern consistent with weak‑form efficiency because the price already reflects all past trading activity; excess trade simply adds transaction costs without generating abnormal profits.

Taken together, these findings support the idea that, at least for short horizons, market prices move in an essentially random fashion and cannot be reliably steered by historical patterns.

### semi-strong-form efficiency

When the market is semi‑strong efficient every piece of _public_ information—earnings releases, regulatory filings or any news that is freely available—is instantly incorporated into asset prices.  In that case no trader can earn abnormal profits from public data because the price already reflects it.

If the hypothesis holds, a fundamental analyst who relies on earnings reports, macro announcements or other public disclosures will find no systematic edge. The price will move in line with the new information; any deviation is only temporary noise.

Suppose morning news declares that Facebook’s stock is worth $90 per share, while the market quotes $105.  If the price does not adjust (almost) immediately, an informed trader could sell until the valuation reaches $90. The existence of such a mispricing shows that the market would be _not_ semi‑strong efficient.

#### evidence for semi-strong-form efficiency

A common test for semi‑strong-form efficiency is the event‑study methodology.  An analyst selects a date when new public information arrives and measures abnormal returns around that window: $$\text{CAR}_{t}=\sum_{s=t_1}^{t_2}\bigl(R_{s}-E[R_{s}]\bigr),$$ where $R_s$ is the observed return and $E[R_s]$ is the expected return from a market model.  If the cumulative abnormal return (CAR) is statistically indistinguishable from zero, the event is deemed fully priced. Deviations before the event is considered _leakage_, possible due to insider information, which _does not_ contradict semi-strong-form efficiency; deviations after the event is considered _drfit_, which _does_ contradict semi-strong-form efficiency if it is persistent.

When analysts examine abnormal returns around earnings releases or dividend changes, they often observe a small pre‑announcement _leakage_, and small post-announcement _drift_ exists: prices rise (or fall) before the official disclosure, implying that some information leaks early. After the official closure, prices typically fluctuates slightly. Take‑over announcements typically trigger a sharp jump followed by a gradual adjustment. Similar patterns have been observed around Federal Open Market Committee statements. Early reactions can be explained by insider trading while later returns trend toward zero, providing evidence for semi-strong-form efficiency.

Calendar anomalies—such as the January effect or weekend effects—reveal that not every piece of public news is priced instantly, which contradicts semi-strong-form efficiency.

Some of these anomalies may be explained, preserving semi-strong-form efficiency. One explanation is that individual anomalies tend to be very small, which may not cover trading costs, so arbitrage does not operate. Another explanation is that anomalies tend to disappear after being reported. However, these cannot explain _leakage_; see strong-form efficiency below.

Overall, while many event studies show rapid price adjustments, the persistence of small abnormal movements and calendar patterns suggests that semi-strong-form efficiency typically approximates the reality well, but is still an idealisation rather than a complete description of real markets.

### strong-form efficiency

Strong‑form efficiency requires that every piece of information—public or private—is instantly embedded in prices. In this extreme case, even material facts known only to insiders cannot be exploited because the price already reflects them. Thus no investor can earn abnormal profits from any kind of information.

Private information is divided into two broad classes.  The first type is _insider_ data that belongs to a firm’s management or employees; an example is knowledge of an impending takeover bid before it becomes public. The second type is _private assessment_: different traders may interpret the same publicly available news differently and form distinct private signals. Trading on such signals is called informed trading, which is illegal when it relies on information obtained by violating fiduciary duties.

#### no-trade theorem and noise trading

If a market is strongly efficient, every security’s price already equals its fundamental value that incorporates all public and private facts. Consequently, fund managers cannot achieve persistent alpha, even if they possess insider knowledge. The _no‑trade theorem_ formalises this: The theorem states that if markets are _strongly efficient_ with no _noise traders_, two rational traders with opposite private signals will not trade. Even though each trader knows the true value of the asset, the price already incorporates both views; therefore trading would not change the equilibrium price and offers no advantage. For example, when two traders hold opposing private valuations of the same stock—one valuing it at $100, the other at $80—the rational outcome is that no trade occurs because the price must already reveal all information.

Noise refers to random, non‑informational fluctuations in market activity. Fisher & Black (1986) argued that such _noise_ is essential for liquidity: it keeps prices moving even when there is no new information. In their model, investors trade on what they perceive as “information” but is actually just noise; the resulting trades increase depth and allow other participants to adjust positions.

The argument against strong-form efficiency goes like this: Under strong-form efficiency, the no-trade theorem implies trading is unnecessary. That trading occurs in reality implies that strong-form efficiency does not hold in practice.

#### evidence for strong-form efficiency

Empirical work on insider trading shows systematic abnormal returns.  Meulbroek (1992) examined mutual‑fund trades and found large cumulative abnormal returns (CARs) after insider‑related events, such as takeover bids or negative earnings news. For example, in a sample of takeover‑related holdings the CAR was 12.5% over a one‑day holding period. These results contradict strong‑form efficiency because they demonstrate that private information can be turned into profit.

## implications

Because weak‑form evidence suggests that past price patterns are useless, and strong‑form evidence shows that insider trading can earn abnormal profits, real markets appear to lie somewhere between the weak and strong extremes. The semi‑strong form is often taken as a useful benchmark: it predicts that publicly announced facts are reflected almost immediately but allows for small, persistent anomalies such as calendar effects or delayed reactions to earnings announcements.

In practice, investors who rely on fundamental analysis—examining financial statements or macro releases—find only modest out‑performance because the price has already incorporated most of the public data. Noise trading and behavioural biases further complicate the picture, producing temporary mispricings that can be exploited only if transaction costs are low enough.

Overall, the efficient‑market hypothesis remains a useful ideal: it explains why random walks dominate weak‑form tests, why insider trades sometimes earn abnormal returns, and why most publicly available information is priced at once. However, the existence of private signals and noise trading shows that no market is perfectly efficient in reality.
