---
aliases:
  - Grossman and Stiglitz paradox
  - Grossman-Stiglitz impossibility theorem
  - Grossman-Stiglitz paradox
  - Grossman–Stiglitz paradox
tags:
  - flashcard/active/special/academia/HKUST/FINA_4103/Grossman–Stiglitz_paradox
  - language/in/English
---

# Grossman–Stiglitz paradox

A market price aggregates information that someone must pay to produce. The Grossman–Stiglitz paradox holds that when information is costly the equilibrium price cannot be strong-form efficient: if the price fully revealed the private information of traders, gathering information would not pay, so nobody would gather it, and the price could not reveal it. Grossman and Stiglitz (1980, American Economic Review (AER)) state the point as the impossibility of (strong) market efficiency: the price never fully reflects the private information of traders.

Real markets trade heavily and information asymmetry matters, so the circle needs a way out. The [no-trade theorem](no-trade%20theorem.md) settles a neighbouring circle: traders who reason about each other's signals do not trade on asymmetric information alone. The setting below is a version of that world built to prevent the no-trade result, and it answers whether the prices of the [financial system](financial%20system.md) can be strong-form efficient.

---

Flashcards for this section are as follows:

- the Grossman–Stiglitz paradox ::@:: When information is costly, the equilibrium market price cannot be strong-form efficient: if the price fully revealed the private information of traders, gathering information would not pay, so nobody would gather it, and the price could not reveal it.
- how noise trading resolves the Grossman–Stiglitz paradox ::@:: Random orders from noise traders let informed traders hide their signal, so buying the costly signal still pays and the price stays informative without fully revealing the information.
- which model shows that costly information forces an equilibrium price that cannot be strong-form efficient, and that noise trading is what keeps informed trading worth paying for? ::@:: Sanford J. Grossman and Joseph E. Stiglitz, 1980, American Economic Review (AER), the paper that states the Grossman–Stiglitz paradox as the impossibility of strong-form market efficiency.

## trading model

$N$ traders hold mean-variance (MV) utility and trade an asset whose payoff is normal, $v \sim N(0, \sigma_v^2)$, with mean $\mu = 0$ for simplicity. The supply of the asset is fixed at $X > 0$ units. A signal $s = v + e$ about the payoff, with noise $e \sim N(0, \sigma_e^2)$, is available at price $f$ before trading. $n_I$ traders decide to buy the signal and become the informed traders, and the remaining $n_U = N - n_I$ traders are uninformed. Precisions are written $\tau_v = 1/\operatorname{Var}(v) = 1/\sigma_v^2$ for the initial uncertainty and $\tau_e = 1/\sigma_e^2$ for the signal.

A trader who holds $x$ units bought at price $p$ earns $x(v - p)$ and chooses $x$ to maximize mean-variance utility $U(x) = \operatorname{E}[x(v - p)] - \frac{\gamma}{2}\operatorname{Var}(xv)$, with risk aversion $\gamma > 0$. The first term is the expected profit of the position. The second is what the same position pays for the risk it carries, and $\gamma$ prices the trade-off between them: a larger $\gamma$ makes every unit of variance cost more profit, so the same expected profit supports a smaller position. The model fixes $\gamma = 1$ throughout, leaving $U(x) = \operatorname{E}[x(v - p)] - \frac{1}{2}\operatorname{Var}(xv)$, so one more unit of variance is worth exactly one unit of expected profit. Each demand below maximizes this utility, once over the prior and once over the posterior given the signal.

---

Flashcards for this section are as follows:

- the setting of the Grossman–Stiglitz model, with trader count $N$, risk aversion $\gamma = 1$, payoff $v$, fixed supply $X > 0$, signal $s = v + e$ at price $f$, and counts $n_I$ and $n_U = N - n_I$ ::@:: $N$ mean-variance (MV) traders with risk aversion $\gamma = 1$ trade an asset with payoff $v \sim N(0, \sigma_v^2)$ and fixed supply $X > 0$; a signal $s = v + e$ with $e \sim N(0, \sigma_e^2)$ sells at price $f$, and $n_I$ traders buy it while $n_U = N - n_I$ stay uninformed.
- the mean-variance (MV) utility a trader with risk aversion $\gamma$ maximizes by holding $x$ units of an asset with payoff $v$ at price $p$ ::@:: $U(x) = \operatorname{E}[x(v - p)] - \frac{\gamma}{2}\operatorname{Var}(xv)$: expected profit minus a penalty for the risk of the position, with $\gamma$ pricing the trade-off, so a larger $\gamma$ holds fewer units for the same expected profit.
- the mean-variance utility in the Grossman–Stiglitz model, where risk aversion is set to $\gamma = 1$, for a trader holding $x$ units at price $p$ with payoff $v$ ::@:: $U(x) = \operatorname{E}[x(v - p)] - \frac{1}{2}\operatorname{Var}(xv)$: expected profit minus half the variance of the position, so one unit of variance costs exactly one unit of expected profit.
- the precision notation in the Grossman–Stiglitz model, with payoff $v$, signal $s = v + e$, and variances $\sigma_v^2$ and $\sigma_e^2$ ::@:: $\tau_v = 1/\operatorname{Var}(v) = 1/\sigma_v^2$ measures the initial uncertainty about the payoff $v$, and $\tau_e = 1/\sigma_e^2$ measures the precision of the signal $s = v + e$.

### uninformed demand

The uninformed trader knows only the prior over the payoff, so the utility above takes the prior's moments: $U(x_U) = \operatorname{E}[x_U(v - p)] - \frac{1}{2}\operatorname{Var}(x_U v) = x_U(\operatorname{E}[v] - p) - \frac{1}{2}x_U^2\sigma_v^2$. Expected profit is linear in the position and the risk penalty is quadratic, so differentiating and setting the derivative to zero gives the first-order condition $\operatorname{E}[v] - p - x_U\sigma_v^2 = 0$. With $\operatorname{E}[v] = 0$ it solves to $x_U = -p/\sigma_v^2 = -\tau_v p$, the standard mean-variance optimal portfolio.

The demand is an edge divided by a risk. With no information the edge is $\operatorname{E}[v] - p = -p$, the distance between what the payoff is expected to be worth and what the position costs, and the risk is $\sigma_v^2 = 1/\tau_v$, the variance of holding one unit. The first-order condition does that division, and it leaves the precision $\tau_v$ multiplying the price. A payoff known to within a small variance supports a large position on the same gap; a payoff that may surprise holds the position near zero.

An uninformed trader expects the asset to be worth nothing. A negative price is a bargain and the trader goes long; a positive price is an overpayment and the trader goes short; at a price of zero the trader holds nothing. The size of the position is that distance from zero over how much the payoff can surprise, so a trader who knows the payoff more precisely reacts harder to the same price: a position of a given size can no longer turn into a large loss.

---

Flashcards for this section are as follows:

- the uninformed trader's demand in the Grossman–Stiglitz model, with price $p$, payoff variance $\sigma_v^2$, and precision $\tau_v = 1/\sigma_v^2$ ::@:: $x_U = -p/\sigma_v^2 = -\tau_v p$, from maximizing $U(x_U) = \operatorname{E}[x_U(v - p)] - \frac{1}{2}\operatorname{Var}(x_U v)$ at price $p$, with $\operatorname{E}[v] = 0$ and $\tau_v = 1/\sigma_v^2$.
- the first-order condition behind the uninformed demand, with expectation $\operatorname{E}[v] = 0$, price $p$, demand $x_U$, and payoff variance $\sigma_v^2$ ::@:: $\operatorname{E}[v] - p - x_U\sigma_v^2 = 0$ for a mean-variance trader choosing $x_U$ units at price $p$ with payoff variance $\sigma_v^2$.
- the reading of the uninformed demand $x_U = -p/\sigma_v^2 = -\tau_v p$ for a trader with $\operatorname{E}[v] = 0$ at price $p$ ::@:: The position is the edge $\operatorname{E}[v] - p = -p$ divided by the risk $\sigma_v^2$ of holding a unit, so a more precisely known payoff, with a larger $\tau_v = 1/\sigma_v^2$, gives a larger position on the same gap.
- where an uninformed trader with $\operatorname{E}[v] = 0$ and payoff variance $\sigma_v^2$ is long, short, or flat at price $p$ ::@:: Long when $p < 0$, since a negative price is a bargain; short when $p > 0$, since a positive price is an overpayment; flat at $p = 0$. The position grows with the absolute gap and with the precision $\tau_v = 1/\sigma_v^2$ of the payoff.

### informed demand

The informed trader maximizes the same utility, now conditional on the signal: $U(x_I) = \operatorname{E}[x_I(v - p) \mid s] - \frac{1}{2}\operatorname{Var}(x_I v \mid s) = x_I(\operatorname{E}[v \mid s] - p) - \frac{1}{2}x_I^2\operatorname{Var}(v \mid s)$. [Bayesian updating](Bayes'%20theorem.md) on the normal signal gives $\operatorname{E}[v \mid s] = \frac{\tau_v}{\tau_v + \tau_e}\mu + \frac{\tau_e}{\tau_v + \tau_e}s = \frac{\tau_e}{\tau_v + \tau_e}s$ and $\operatorname{Var}(v \mid s) = \frac{1}{\tau_v + \tau_e}$; the two precisions add, so observing the signal is worth exactly $\tau_e$ of precision on top of the $\tau_v$ the trader already had. Each term of the mean enters with its share of that total precision: the prior mean takes $\frac{\tau_v}{\tau_v + \tau_e}$ and the signal $\frac{\tau_e}{\tau_v + \tau_e}$, so the belief moves off the prior by exactly the signal's share of the gap between the signal and the prior. A signal of negligible precision leaves the mean at $\mu$; one of unbounded precision puts it at $s$. The addition of precisions is the independence argument set out in [Bayes' theorem](Bayes'%20theorem.md#posterior%20variance%20as%20added%20precision), where a signal correlated with the prior adds less than its own precision because the overlap is counted twice. The same first-order condition as the uninformed trader's, with these posterior moments in place of the prior ones, gives demand $x_I(s) = \frac{\operatorname{E}[v \mid s] - p}{\operatorname{Var}(v \mid s)} = \tau_e s - (\tau_v + \tau_e)p$.

The position is again an edge over a risk, with both taken after the signal. The edge is $\operatorname{E}[v \mid s] - p$ and the risk is $\operatorname{Var}(v \mid s) = 1/(\tau_v + \tau_e)$. Cleared of the fraction, the signal enters with weight $\tau_e$, its own precision, and the price enters with the full posterior precision $\tau_v + \tau_e$. The signal moves the position by how much it says, scaled by how precisely it says it; the price is subtracted at both precisions together, because the posterior mean already carries the signal's weight.

The signal tells the informed trader what the asset is worth and the price tells them what it costs. They go long when the price sits below their posterior mean $\tau_e s/(\tau_v + \tau_e)$ and short when it sits above: the same rule as the uninformed trader's, around a value the signal has moved away from zero. At the same price their position is the larger one, because the signal has cut the risk of holding the asset and less risk licenses more units. A trader with a strong signal buys at prices an uninformed trader calls dear and sells at prices an uninformed trader calls cheap.

---

Flashcards for this section are as follows:

- the informed trader's posterior on the payoff in the Grossman–Stiglitz model, with signal $s = v + e$, prior mean $\mu$, and precisions $\tau_v$ and $\tau_e$ ::@:: $\operatorname{E}[v \mid s] = \frac{\tau_v}{\tau_v + \tau_e}\mu + \frac{\tau_e}{\tau_v + \tau_e}s = \frac{\tau_e}{\tau_v + \tau_e}s$ (with $\mu = 0$) and $\operatorname{Var}(v \mid s) = \frac{1}{\tau_v + \tau_e}$, for signal $s = v + e$ with precisions $\tau_v$ and $\tau_e$.
- the informed trader's demand in the Grossman–Stiglitz model, with price $p$, signal $s$, and posterior moments $\operatorname{E}[v \mid s]$ and $\operatorname{Var}(v \mid s)$ ::@:: $x_I(s) = \frac{\operatorname{E}[v \mid s] - p}{\operatorname{Var}(v \mid s)} = \tau_e s - (\tau_v + \tau_e)p$, at price $p$, with posterior $\operatorname{E}[v \mid s] = \frac{\tau_e}{\tau_v + \tau_e}s$ and posterior variance $\operatorname{Var}(v \mid s) = \frac{1}{\tau_v + \tau_e}$.
- the reading of the informed demand $x_I(s) = \tau_e s - (\tau_v + \tau_e)p$, with signal $s$, prior precision $\tau_v$, posterior mean $\operatorname{E}[v \mid s] = \frac{\tau_e}{\tau_v + \tau_e}s$, and posterior variance $\operatorname{Var}(v \mid s) = \frac{1}{\tau_v + \tau_e}$ ::@:: The position is the posterior edge $\operatorname{E}[v \mid s] - p$ over the posterior risk $1/(\tau_v + \tau_e)$: the signal enters with weight $\tau_e$, its own precision, and the price with the posterior precision $\tau_v + \tau_e$.
- when an informed trader with signal $s$, signal precision $\tau_e$, and prior precision $\tau_v$ buys and when they sell at price $p$ ::@:: Long when $p < \frac{\tau_e s}{\tau_v + \tau_e}$, below the posterior mean, and short above it. The position is larger than an uninformed trader's at the same price, because the signal has cut the risk of holding the asset.
- read the two coefficients of $\operatorname{E}[v \mid s] = \frac{\tau_v}{\tau_v + \tau_e}\mu + \frac{\tau_e}{\tau_v + \tau_e}s$ as shares of one quantity, with prior mean $\mu$ and precisions $\tau_v$ and $\tau_e$ ::@:: Shares of the total precision $\tau_v + \tau_e$: the prior mean takes $\frac{\tau_v}{\tau_v + \tau_e}$ and the signal takes $\frac{\tau_e}{\tau_v + \tau_e}$, so the belief moves off $\mu$ by exactly the signal's share of the gap $s - \mu$.
- as the signal precision $\tau_e$ goes to zero and to infinity, what the informed trader's posterior mean $\operatorname{E}[v \mid s] = \frac{\tau_e}{\tau_v + \tau_e}s$ becomes, with prior mean $\mu$ and prior precision $\tau_v$ ::@:: $\tau_e \to 0$: it returns to the prior mean $\mu$, since the signal carries no precision; $\tau_e \to \infty$: it lands on the signal $s$.

## equilibrium without noise

Equilibrium is a price $p^*$ at which every trader optimizes and the market clears: the fixed supply equals total demand, $X = n_I x_I(s) + n_U x_U$. The condition says the whole supply must end up in someone's hands, and both demands fall as the price rises, so one price makes the sum come out at $X$. Substituting the two demands gives $X = n_I(\tau_e s - (\tau_v + \tau_e)p^*) - n_U\tau_v p^*$, and solving for the price gives $p^* = \frac{n_I \tau_e s - X}{n_I(\tau_v + \tau_e) + n_U \tau_v}$.

The numerator is the pressure the signal puts on demand, $n_I\tau_e s$, less the supply that has to be held, $X$: informed traders bid the price up on a good signal, and a larger supply pushes it down, because whoever takes the asset must be paid to hold it. The denominator is the total sensitivity of demand to the price, how much demand falls for each unit the price rises, so a larger denominator means the same pressure moves the price less.

Written with known constants, the price reads $p^* = \alpha + \beta s$, and it then fully reveals $s$: uninformed traders infer the signal perfectly from the price and no longer need to pay $f$ for it, the free-riding problem of indexers. The information is a public good the moment anyone trades on it, because the trade itself publishes it, and the people who paid for it cannot charge the people who only read the price. Nobody buys the signal at that price. The price then carries no information, so observing $s$ becomes valuable again, traders are willing to pay for $s$, and the price reveals $s$ again. No equilibrium exists where traders pay for the signal and the price fully reveals it.

---

Flashcards for this section are as follows:

- the market-clearing price without noise trading in the Grossman–Stiglitz model, with supply $X$, counts $n_I$ and $n_U$, demands $x_I(s) = \tau_e s - (\tau_v + \tau_e)p$ and $x_U = -\tau_v p$, and precisions $\tau_v$ and $\tau_e$ ::@:: $p^* = \frac{n_I \tau_e s - X}{n_I(\tau_v + \tau_e) + n_U \tau_v}$, from clearing $X = n_I x_I(s) + n_U x_U$ with $x_I(s) = \tau_e s - (\tau_v + \tau_e)p$ and $x_U = -\tau_v p$.
- the reading of the equilibrium price without noise, $p^* = \frac{n_I \tau_e s - X}{n_I(\tau_v + \tau_e) + n_U \tau_v}$, with informed count $n_I$, uninformed count $n_U$, fixed supply $X$, signal $s$, and precisions $\tau_v$ and $\tau_e$ ::@:: The signal enters weighted by informed demand $n_I\tau_e$, the fixed supply $X$ pulls the price down, and the denominator $n_I(\tau_v + \tau_e) + n_U \tau_v$ is the total sensitivity of demand to the price.
- what a price $p^* = \alpha + \beta s$ with known constants $\alpha$ and $\beta$ does to the signal ::@:: It fully reveals $s$, so uninformed traders infer it without paying the signal's price $f$, and nobody buys the signal.
- the free-rider circle behind the Grossman–Stiglitz paradox ::@:: If the price fully reveals the signal, nobody pays for it; the price then reveals no information, observing the signal becomes valuable again, traders pay for it, and the price reveals it again. No equilibrium exists where traders pay for the signal.
- what the market-clearing condition $X = n_I x_I(s) + n_U x_U$ requires in the Grossman–Stiglitz model, with fixed supply $X$, informed count $n_I$, uninformed count $n_U = N - n_I$, informed demand $x_I(s)$, and uninformed demand $x_U$ ::@:: The whole fixed supply must be held, so total demand has to equal $X$; both demands fall as the price $p$ rises, so a single price makes the sum come out at $X$.
- why a larger fixed supply $X$ lowers the equilibrium price $p^* = \frac{n_I \tau_e s - X}{n_I(\tau_v + \tau_e) + n_U \tau_v}$ in the Grossman–Stiglitz model ::@:: The extra units have to be held by someone, so the price must fall until traders are willing to take them; with a smaller supply the same signal $s$ supports a higher price.

## noisy equilibrium

Noise traders break the circle. They have exogenous trading needs, so they trade a random quantity $z \sim N(0, \sigma_z^2)$ regardless of the price and their information. Market clearing now reads $X = n_I x_I(s) + n_U x_U + z$, equivalently the net supply is random, $X - z \sim N(X, \sigma_z^2)$. Solving for the price gives $p^* = \frac{n_I \tau_e s - X + z}{n_I(\tau_v + \tau_e) + n_U \tau_v}$, so the equilibrium price takes the form $p^* = \alpha + \beta s + \gamma z$ for constants $\alpha$, $\beta$, and $\gamma$: both demands are linear in the signal and in the price, and clearing adds the demands and divides by their price sensitivity. One demand term is added and nothing else moves: a unit of noise trading lifts the price by as much as a unit less of supply, and the same total demand sensitivity divides it.

The price is now the signal with noise added, not the signal itself: $s$ enters with weight $\beta$ and the random quantity $z$ with weight $\gamma$, so it does not fully reveal the information, because a very high $p^*$ is consistent with a high $s$ or a high $z$. The noise solves the free-riding problem. Informed traders hide their signal by trading alongside the noise traders, so the price no longer hands the signal out for free and buying it at price $f$ can pay again. How far the traded price departs from the price the information would justify is the subject of [price discovery](price%20discovery.md), and here one cause of the departure is the noise term $\gamma z$. These information frictions contribute to the spread and trade dynamics studied in [market microstructure](market%20microstructure.md).

---

Flashcards for this section are as follows:

- noise traders in the Grossman–Stiglitz model ::@:: Traders with exogenous trading needs who trade a random quantity $z \sim N(0, \sigma_z^2)$ regardless of the price and their information. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the noisy equilibrium price in the Grossman–Stiglitz model, with signal component $\alpha + \beta s$, noise term $\gamma z$, supply $X$, demands $x_I(s)$ and $x_U$, and noise quantity $z \sim N(0, \sigma_z^2)$ ::@:: $p^* = \alpha + \beta s + \gamma z$, from market clearing $X = n_I x_I(s) + n_U x_U + z$ with the noise-trader quantity $z \sim N(0, \sigma_z^2)$.
- how a very high noisy-equilibrium price $p^*$ should be read ::@:: It is consistent with a high signal $s$ or a high noise draw $z$; the price does not fully reveal the signal.
- the reading of $p^* = \alpha + \beta s + \gamma z$ in the Grossman–Stiglitz model, with payoff $v$, signal $s = v + e$, noise-trader quantity $z \sim N(0, \sigma_z^2)$, and constants $\alpha$, $\beta$, and $\gamma$ ::@:: The price is the signal with noise added, not the signal itself: the signal $s$ enters with weight $\beta$ and the noise-trader quantity $z$ with weight $\gamma$.
- why noise trading keeps information gathering profitable in the Grossman–Stiglitz model ::@:: Informed traders hide their signal by trading with the noise traders, so the price no longer reveals $s$ for free and buying the signal at price $f$ can pay. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why a unit of noise-trader demand $z$ lifts the Grossman–Stiglitz price as much as a unit less fixed supply $X$ in $p^* = \frac{n_I \tau_e s - X + z}{n_I(\tau_v + \tau_e) + n_U \tau_v}$ ::@:: Both enter the numerator with the same size and opposite signs, so they shift the price by the same amount; only the total demand sensitivity in the denominator, and not the source of the imbalance, decides how far the price moves.

## measuring price efficiency

The constant $\alpha$ is irrelevant to informativeness, so the price behaves as $p^* = \beta s + \gamma z$: what matters is how much of the uncertainty about the payoff $v$ observing the price resolves. $\alpha$ holds whatever does not vary, here the supply term $-X$ over the total demand sensitivity: it moves the level of the price without changing what the price says about the asset.

---

Flashcards for this section are as follows:

- what price efficiency compares in the Grossman–Stiglitz model ::@:: How much uncertainty about the payoff $v$ remains after observing the price $p^*$, against how much remains after observing the private signal $s$ directly. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- what the constant $\alpha$ in $p^* = \alpha + \beta s + \gamma z$ carries, with fixed supply $X$, informed count $n_I$, uninformed count $n_U$, and precisions $\tau_v$ and $\tau_e$ ::@:: Everything in the price that does not vary: the supply term $-X$ over the total demand sensitivity $n_I(\tau_v + \tau_e) + n_U \tau_v$. A constant shifts the price without changing what it says about the payoff $v$, so price efficiency ignores it.

### weights on signal and noise

The weight on the signal is $\beta = \frac{n_I \tau_e}{n_I(\tau_v + \tau_e) + n_U \tau_v}$ and the weight on the noise is $\gamma = \frac{1}{n_I(\tau_v + \tau_e) + n_U \tau_v}$. The two weights share the denominator, the total sensitivity of demand to the price: with $n_U = N - n_I$ it simplifies to $n_I \tau_e + N \tau_v$, since every trader responds to the price through the prior precision $\tau_v$ and each informed trader adds the signal's precision $\tau_e$ on top. A unit rise in $s$ lifts informed demand by $n_I\tau_e$, and the price has to rise by $\beta$, informed demand's response over that sensitivity, to make total demand fall back by the same amount; $\beta$ is the share of a signal move that reaches the price. $\gamma$ is the reciprocal of the sensitivity: one extra unit of demand is choked off by a price rise of $\gamma$, which is how far one unit of noise trading moves the price. Both depend on the number of informed and uninformed traders, the precision of the signal $\tau_e$, and the initial uncertainty $\tau_v$.

---

Flashcards for this section are as follows:

- the weight $\beta$ on the signal in the Grossman–Stiglitz price ::@:: $\beta = \frac{n_I \tau_e}{n_I(\tau_v + \tau_e) + n_U \tau_v}$ in $p^* = \alpha + \beta s + \gamma z$, the share of a signal move that reaches the price: informed demand's response to the signal divided by total demand sensitivity, with informed count $n_I$, uninformed count $n_U = N - n_I$, and precisions $\tau_v$ and $\tau_e$.
- the weight $\gamma$ on the noise in the Grossman–Stiglitz price ::@:: $\gamma = \frac{1}{n_I(\tau_v + \tau_e) + n_U \tau_v}$ in $p^* = \alpha + \beta s + \gamma z$, how far one unit of noise trading moves the price: the reciprocal of total demand sensitivity, with informed count $n_I$, uninformed count $n_U = N - n_I$, and precisions $\tau_v$ and $\tau_e$.
- the total demand sensitivity $n_I(\tau_v + \tau_e) + n_U \tau_v$ shared by the weights $\beta$ and $\gamma$ of $p^* = \alpha + \beta s + \gamma z$, with $N$ total traders, $n_U = N - n_I$ uninformed, and precisions $\tau_v$ and $\tau_e$ ::@:: It is how much total demand falls for each unit the price rises, and with $n_U = N - n_I$ it equals $n_I \tau_e + N \tau_v$: every trader responds to the price through the prior precision $\tau_v$, and each informed trader adds the signal precision $\tau_e$ on top.

### precision of the price signal

Dividing the price by $\beta$ extracts the relevant terms: $p^* = \beta s + \gamma z = \beta\left(s + \frac{\gamma}{\beta}z\right)$, so observing $p^*$ is informationally equivalent to observing $s_p = s + \frac{\gamma}{\beta}z = v + e + \frac{\gamma}{\beta}z$, where $\frac{\gamma}{\beta}z$ is the noise of $s_p$. With $\beta = 10$, observing $p^* = 100$ is the same as observing $s_p = p^*/\beta = 10$, that is, $10 = v + e_p$.

The signal $s_p$ is noisier than $s$ because noise trading adds to the signal's own noise. From the weights, $\frac{\gamma}{\beta} = \frac{1}{n_I \tau_e}$ is a noise-to-signal ratio in the price: it falls as more traders buy the signal or as the signal gets sharper, and doubling either $n_I$ or $\tau_e$ halves it. The two noises on $s_p$ are independent, so no cross term stands between them and their variances add: the precision of the price signal is the reciprocal of that sum, $\tau_p = \frac{1}{\operatorname{Var}\left(e + \frac{\gamma}{\beta}z\right)} = \frac{1}{\sigma_e^2 + \left(\frac{\sigma_z}{n_I\tau_e}\right)^2}$. Had the two moved together, the sum would overstate the precision the price carries, because the part they share would be counted in both terms. An observer of the price knows the informed trader's signal with extra noise on top, never more than the informed trader knows. Only the second denominator term moves with $n_I$, so $\tau_p$ rises with the informed count while staying below the signal's own precision $\tau_e$.

---

Flashcards for this section are as follows:

- the scaled price $s_p$ equivalent to observing the Grossman–Stiglitz price ::@:: $s_p = v + e + \frac{\gamma}{\beta}z$, with $\frac{\gamma}{\beta}z$ the noise of $s_p$; observing $p^* = \beta s + \gamma z$ carries the same information as observing $s_p = p^*/\beta$.
- the ratio of noise weight to signal weight in the Grossman–Stiglitz price $p^* = \alpha + \beta s + \gamma z$, with informed count $n_I$ and signal precision $\tau_e$ ::@:: $\frac{\gamma}{\beta} = \frac{1}{n_I \tau_e}$, a noise-to-signal ratio in the price that halves when either the informed count $n_I$ or the signal precision $\tau_e$ doubles.
- the precision $\tau_p$ of the price signal in the Grossman–Stiglitz model ::@:: $\tau_p = \frac{1}{\operatorname{Var}\left(e + \frac{\gamma}{\beta}z\right)} = \frac{1}{\sigma_e^2 + \left(\frac{\sigma_z}{n_I \tau_e}\right)^2}$, using $\frac{\gamma}{\beta} = \frac{1}{n_I \tau_e}$ for signal noise $e \sim N(0, \sigma_e^2)$ and noise-trader quantity $z$ with standard deviation $\sigma_z$.
- why the price-signal precision $\tau_p$ rises with the informed count $n_I$ in the Grossman–Stiglitz model, with signal noise $e \sim N(0, \sigma_e^2)$, noise-trader quantity $z$ with standard deviation $\sigma_z$, and signal precision $\tau_e$ ::@:: $\tau_p = \frac{1}{\sigma_e^2 + \left(\frac{\sigma_z}{n_I \tau_e}\right)^2}$ has only the second denominator term moving with $n_I$, so $\tau_p$ rises with the informed count and stays below $\tau_e$.
- why the price signal's precision $\tau_p$ falls short of the signal's own precision $\tau_e$ in the Grossman–Stiglitz model, with signal noise $e \sim N(0, \sigma_e^2)$, noise-trader quantity $z$ with standard deviation $\sigma_z$, informed count $n_I$, and signal precision $\tau_e$ ::@:: Independent noises have variances that add, so $\tau_p = \frac{1}{\sigma_e^2 + (\sigma_z/(n_I\tau_e))^2}$ is the reciprocal of the signal's own noise variance plus the noise traded into the price, which keeps $\tau_p < \tau_e = 1/\sigma_e^2$ whenever $\sigma_z > 0$.

### efficiency relative to the signal

An informed trader who has bought the signal is still uncertain about the payoff, with variance $\operatorname{Var}(v \mid s) = \frac{1}{\tau_v + \tau_e}$, and that is the numerator: what such a trader does not know. An observer of the price alone, who knows $\beta$ and $\gamma$ and so reads $s_p = p^*/\beta$, faces $\operatorname{Var}(v \mid p^*) = \operatorname{Var}(v \mid s_p) = \frac{1}{\tau_v + \tau_p}$, the denominator: what an observer of the price alone does not know. Price efficiency relative to the signal is their ratio, $\eta = \frac{\operatorname{Var}(v \mid s)}{\operatorname{Var}(v \mid p^*)} = \frac{\tau_v + \tau_p}{\tau_v + \tau_e} \le 1$, so $\eta$ measures how much of the informed trader's knowledge the price transfers, reaching 1 only when the price carries everything the signal does. Strong-form efficiency is $\eta = 1$, which requires $\sigma_z = 0$ and $\tau_p = \tau_e$; with $\sigma_z > 0$ the price is noisier than the signal, $\tau_p < \tau_e$, and $\eta < 1$. The price transfers part of what the informed trader knows, never all of it while noise trades: an observer of the price is better off than one who ignored the price and worse off than the trader who bought the signal.

---

Flashcards for this section are as follows:

- the price efficiency ratio $\eta$ in the Grossman–Stiglitz model, with payoff $v$, private signal $s = v + e$, noisy-equilibrium price $p^* = \alpha + \beta s + \gamma z$, and precisions $\tau_v$, $\tau_e$, and $\tau_p$ ::@:: $\eta = \frac{\operatorname{Var}(v \mid s)}{\operatorname{Var}(v \mid p^*)} = \frac{\tau_v + \tau_p}{\tau_v + \tau_e} \le 1$: how much of the informed trader's knowledge the price transfers, reaching 1 only when the price carries everything the signal does.
- which conditional variance sits in the numerator of the price efficiency ratio $\eta$ and which in the denominator, with payoff $v$, private signal $s = v + e$, noisy-equilibrium price $p^* = \alpha + \beta s + \gamma z$, and precisions $\tau_v$, $\tau_e$, and $\tau_p$ ::@:: The numerator is $\operatorname{Var}(v \mid s) = \frac{1}{\tau_v + \tau_e}$, the uncertainty of a trader who has bought the signal; the denominator is $\operatorname{Var}(v \mid p^*) = \frac{1}{\tau_v + \tau_p}$, the uncertainty of an observer of the price alone.
- what strong-form efficiency means in the Grossman–Stiglitz model, measured by $\eta$ with noise variance $\sigma_z^2$ and price-signal precision $\tau_p$ ::@:: $\eta = 1$, obtained when the noise-trader quantity is zero, $\sigma_z = 0$, and the price-signal precision reaches the signal precision, $\tau_p = \tau_e$.
- what the efficiency ratio $\eta = \frac{\tau_v + \tau_p}{\tau_v + \tau_e} \le 1$ says in words about a price watcher and an informed trader, with prior precision $\tau_v$, price-signal precision $\tau_p$, and signal precision $\tau_e$ ::@:: The price hands the watcher part of what the informed trader knows, never all of it while noise trades. The watcher is better off than someone who ignored the price and worse off than the trader who bought the signal; the gap closes only as the noise-trading variance $\sigma_z^2$ goes to zero.

## comparative statics

Price precision $\tau_p$ and price efficiency $\eta$ move with three margins of the model: the number of informed traders, the variance of noise trading, and the precision of the private signal.

---

Flashcards for this section are as follows:

- how price precision $\tau_p$ and price efficiency $\eta$ move with the model's margins ::@:: More informed traders raise both; a larger noise-trading variance $\sigma_z^2$ lowers both; a more precise private signal raises $\tau_p$ but moves $\eta$ ambiguously.

### number of informed traders

As the number of informed traders grows, $n_I$ enters $\beta$'s numerator and the shared denominator $n_I\tau_e + N\tau_v$ together, so $\beta = n_I\tau_e/(n_I\tau_e + N\tau_v)$ rises toward 1 while $\gamma = 1/(n_I\tau_e + N\tau_v)$ falls toward 0: the price relies more on the signal and less on the noise. The noise-to-signal ratio $\gamma/\beta = 1/(n_I\tau_e)$ falls in proportion, so the price-signal noise $\sigma_z/(n_I\tau_e)$ shrinks, $\tau_p$ climbs toward the signal's own precision $\tau_e$, and $\eta = (\tau_v + \tau_p)/(\tau_v + \tau_e)$ climbs toward 1. Both climb steeply at small $n_I$ and flatten as $n_I$ grows, because each additional informed trader adds the same $\tau_e$ to a denominator that is already large.

More traders buying the signal means more price moves come from news and fewer from the random needs of noise traders. Each informed trade adds signal to the price while a noise trade keeps the force it always had, so the signal wins by accumulation. Someone with neither the signal nor the model sees a price that sits closer to the asset's value, and the informed traders themselves gain less from the next unit of information, since the price already carries much of what their signal would tell them. The price still never reaches what an insider knows, because the noise never disappears.

---

Flashcards for this section are as follows:

- the effect of a larger informed count $n_I$ on the weights of $p^* = \alpha + \beta s + \gamma z$ ::@:: The price relies more on the signal $s$: the weight $\beta$ rises and the weight $\gamma$ falls as $n_I$ grows.
- the effect of a larger informed count $n_I$ on price efficiency ::@:: The price becomes more precise, $\tau_p$ rises toward the signal's own precision $\tau_e$, and more efficient, $\eta$ rises toward 1; both flatten as the informed count $n_I$ grows.
- why the weight $\beta$ on the signal rises and the weight $\gamma$ on the noise falls as the informed count $n_I$ grows in $p^* = \alpha + \beta s + \gamma z$, with $N$ traders, prior precision $\tau_v$, and signal precision $\tau_e$ ::@:: The shared denominator $n_I(\tau_v + \tau_e) + n_U \tau_v$ equals $n_I \tau_e + N \tau_v$, so $n_I$ appears once in the numerator of $\beta = n_I\tau_e/(n_I\tau_e + N\tau_v)$ and once in the denominator of both weights: $\beta$ rises toward 1 and $\gamma$ falls toward 0.
- what more informed traders do to the Grossman–Stiglitz price, to the informed traders, and to a reader of the price ::@:: More traders buying the signal means more price moves come from news and fewer from the random needs of noise traders, so the price sits closer to the asset's value. An outsider reads it better, and an informed trader gains less from the next unit of information, since the price already carries much of it.

### variance of noise trading

The noise-trading variance $\sigma_z^2$ enters neither weight: $\beta$ and $\gamma$ are built from counts and precisions, so the price still loads on the signal and on the noise draw exactly as before, and what changes is the size of the draw. It reaches the price signal through the noise term $\sigma_z/(n_I\tau_e)$ in $\tau_p = \frac{1}{\sigma_e^2 + (\sigma_z/(n_I\tau_e))^2}$, where a larger $\sigma_z^2$ raises the second denominator term, lowers $\tau_p$, and lowers $\eta = (\tau_v + \tau_p)/(\tau_v + \tau_e)$ with it. Both decline steadily as $\sigma_z^2$ grows: at the parameter values used above, $\tau_p$ falls from 1.00 to about 0.72 and $\eta$ from 1.00 to about 0.86 as $\sigma_z^2$ runs from 0 to 10.

Noise trading makes the price a worse witness: the same quoted price can now come from a better-informed market or from a random surge in the needs of traders who ignore value, and someone reading the price cannot separate the two. Nothing about the information itself has changed, and the informed trader's own edge is untouched, since the demand rule does not involve $\sigma_z$. The noise is also the cover that keeps information gathering worth paying for: the same random demand that makes the price a worse witness is what keeps the informed trader's signal worth buying.

---

Flashcards for this section are as follows:

- the effect of a larger noise-trading variance $\sigma_z^2$ on the Grossman–Stiglitz price ::@:: The price becomes less precise, $\tau_p$ falls, and less efficient, $\eta$ falls; with no noise, $\sigma_z = 0$, they reach $\tau_p = \tau_e$ and $\eta = 1$.
- how the noise-trading variance $\sigma_z^2$ reaches the price precision $\tau_p$ and the efficiency $\eta$ without touching the weights $\beta$ and $\gamma$ of $p^* = \alpha + \beta s + \gamma z$, with signal noise $e \sim N(0, \sigma_e^2)$, informed count $n_I$, signal precision $\tau_e$, and prior precision $\tau_v$ ::@:: It enters only the price signal's noise variance $\sigma_z^2/(n_I\tau_e)^2$, so a larger $\sigma_z^2$ raises the denominator of $\tau_p = \frac{1}{\sigma_e^2 + (\sigma_z/(n_I\tau_e))^2}$ and lowers $\eta = \frac{\tau_v + \tau_p}{\tau_v + \tau_e}$, while the weights depend only on counts and precisions.
- what more noise trading does to the Grossman–Stiglitz price and to someone reading it ::@:: The same quoted price can come from a better-informed market or from a random surge in the needs of traders who ignore value, so the price is a worse witness: an outsider reading it learns less about the asset, even though nothing about the information itself has changed.

### precision of private signals

A sharper signal enters $\beta$'s numerator and the shared denominator at once, so $\beta = n_I\tau_e/(n_I\tau_e + N\tau_v)$ rises toward 1 and $\gamma = 1/(n_I\tau_e + N\tau_v)$ falls: the informed trader's response to the signal grows relative to everyone's response to the price. A sharper signal also divides the price-signal noise $\sigma_z/(n_I\tau_e)$, so $\tau_p = 1/(\sigma_e^2 + (\sigma_z/(n_I\tau_e))^2)$ rises, roughly in proportion to $\tau_e$ and always below it. The efficiency $\eta = (\tau_v + \tau_p)/(\tau_v + \tau_e)$ compares two variances, though, and $\tau_e$ sits in its denominator as well, so $\eta$ can fall even while $\tau_p$ rises: it falls steeply as $\tau_e$ starts to grow, reaches a minimum, and then climbs back, and the direction of the relationship depends on the starting level of $\tau_e$.

In the market, a sharper signal changes what both sides know. The informed trader trades harder and with more confidence on it. The price becomes a better estimate of the asset's value in absolute terms, because the same noise trading is now small next to the informed response. The efficiency ratio is a comparison, though, and the sharper signal sharpens the benchmark as well. When the signal is nearly worthless, the informed trader and the price watcher both know little and look alike. As the signal starts to bite, the insider gains a lot while the price's precision grows only in proportion to the square of the signal's sharpness, so the distance between what insiders know and what the price reveals widens. Once the signal is sharp, the price catches up and the distance narrows again. A sharper signal does not always make the price relatively more informative: it makes everyone better informed, and it can widen the gap between an insider and an outsider before closing it.

---

Flashcards for this section are as follows:

- the effect of a more precise signal $\tau_e$ on the price precision $\tau_p$ ::@:: The price becomes more precise: $\tau_p$ rises roughly in proportion to the signal precision $\tau_e$.
- the effect of a more precise signal $\tau_e$ on the weights of $p^* = \alpha + \beta s + \gamma z$ ::@:: The weight $\beta$ on the signal rises and the weight $\gamma$ on the noise falls as the signal precision $\tau_e$ grows.
- the effect of a more precise signal $\tau_e$ on price efficiency $\eta$ ::@:: The reaction is ambiguous: $\eta$ first falls to a minimum and then rises back as the signal precision $\tau_e$ grows, so the direction depends on the starting level of $\tau_e$.
- why a sharper private signal $\tau_e$ raises the price precision $\tau_p$ while leaving the price efficiency $\eta$ ambiguous in the Grossman–Stiglitz model, with signal noise $e \sim N(0, \sigma_e^2)$, noise-trader quantity $z$ with standard deviation $\sigma_z$, informed count $n_I$, and prior precision $\tau_v$ ::@:: $\tau_e$ divides the price-signal noise $\sigma_z/(n_I\tau_e)$, so $\tau_p$ rises with it; $\eta = \frac{\tau_v + \tau_p}{\tau_v + \tau_e}$ also has $\tau_e$ in its denominator, which rises faster at first, so $\eta$ falls to a minimum before rising back.
- why a sharper private signal need not make the Grossman–Stiglitz price relatively more informative, even though it makes the price more precise in absolute terms ::@:: A sharper signal sharpens the informed trader and the price together: the insider gains a lot at first while the price gains little. The distance between what insiders know and what the price reveals widens before it narrows, so the efficiency ratio can fall while the price precision rises.

## impossibility of strong-form efficiency

The Grossman–Stiglitz impossibility theorem: when the information is costly, the equilibrium price cannot be strong-form efficient. The price $p^* = \alpha + \beta s + \gamma z$ is strong-form efficient if and only if there is no noise ($z$), and without noise traders do not pay for the information, because the price would reveal it for free.

Noise is what keeps information gathering profitable, and the same noise keeps $\tau_p < \tau_e$ and $\eta < 1$. The equilibrium price must be semi-strong efficient at best: the deviation $\gamma z$ that hides the signal inside the price is the deviation that keeps the price from fully reflecting the private information of traders.

---

Flashcards for this section are as follows:

- the Grossman–Stiglitz impossibility theorem ::@:: When the information is costly, the equilibrium price cannot be strong-form efficient.
- when the Grossman–Stiglitz price $p^* = \alpha + \beta s + \gamma z$ is strong-form efficient ::@:: If and only if there is no noise, $z = 0$; but then traders do not pay for the information, because the price would reveal it for free.
- the efficiency ceiling of the Grossman–Stiglitz equilibrium price, with noise variance $\sigma_z^2 > 0$, price-signal precision $\tau_p$, signal precision $\tau_e$, and efficiency $\eta$ ::@:: Semi-strong efficient at best: with $\sigma_z > 0$ needed to keep information gathering profitable, the price-signal precision stays below the signal precision, $\tau_p < \tau_e$, and $\eta < 1$.
