// FINA 4103 midterm examination cheatsheet: recall-only, notes 1-5
// Names, papers, rule numbers and real-world facts that reasoning cannot rebuild.
#set document(title: "FINA 4103 midterm examination cheatsheet", author: "author")
#set page(
  paper: "a4",
  margin: (x: 6.5mm, y: 5.5mm),
  columns: 2,
  header: align(center, text(6.2pt, fill: luma(115))[FINA 4103 midterm · notes 1–5, plus the note 6–9 formulas]),
  footer: align(center, text(6.2pt, fill: luma(115))[#context counter(page).display()]),
)
#set text(font: ("Libertinus Serif", "Source Serif 4"), size: 8.2pt, lang: "en")
#set par(justify: false, leading: 0.30em, spacing: 1.2pt)
#show heading.where(level: 1): it => block(
  above: 7pt, below: 2pt, breakable: false,
  text(10.6pt, weight: "bold", fill: rgb("#14504a"))[#it.body],
)
#show heading.where(level: 2): it => block(
  above: 6pt, below: 2.5pt, breakable: false,
  text(9.4pt, weight: "semibold", fill: rgb("#7a3b1e"))[#it.body],
)

#let part(t) = heading(level: 1, t)

// One recall item: bold key, then what it is.
#let e(k, v) = block(
  breakable: false, width: 100%, inset: (x: 1pt, y: 0.6pt),
  [#text(7.8pt, fill: rgb("#14504a"), weight: "semibold")[#k] #h(2.5pt) #text(7.8pt)[#v]],
)
#let eh(x) = text(6.6pt, weight: "bold", x)

#align(center)[#text(10.6pt, weight: "bold")[FINA 4103 midterm]]

#part("1 · Papers and people")

#e([three reasons for a spread], [order processing (Demsetz), inventory risk (Smidt, Stoll), and information (Glosten–Milgrom); only the last one reverses in the price.])
#e([Garman 1976 JFE], [coined “microstructure”; orders as a Poisson process; two models, dealership and auction.])
#e([Demsetz 1968 QJE], [the spread is the price of immediacy: order-processing cost and time value.])
#e([Smidt 1971 FAJ], [the spread is inventory cost.])
#e([Stoll 1978 JF], [the spread pays for the price risk of the dealer's inventory.])
#e([Glosten & Milgrom 1985 JFE], [the spread is information friction: the maker loses to a trader who knows more.])
#e([Zhu 2014 RFS], [“Do Dark Pools Harm Price Discovery?” No: informed traders are rationed in the dark, leave for lit venues, and the lit price improves (a monopolist informed trader may differ).])
#e([Boulatov & George 2013 RFS], [hidden orders benefit the market overall.])
#e([Cao et al. 2022 JFE], [the share of immediate-or-cancel orders grew through the 2000s.])
#e([Lewis 2014 Flash Boys], [the direct data feed outruns the consolidated feed, so a quote vanishes as an order arrives.])
#e([Park, Suen & Wan 2022 JFM], [Hong Kong close sniping: sell orders at 4:09:57 drove the indicative close from 37 to 33 dollars.])
#e([Chen et al. 2024 JF], [“The Dark Side of Circuit Breakers”: a halt makes the market more volatile and more fragile.])
#e([Budish, Cramton & Shim 2015 QJE], [the frequent batch auction, proposed against the high-frequency arms race.])
#e([Budish, Lee & Shim 2023 JPE], [exchange fees fall to negligible, because every venue sells the same execution (Bertrand).])
#e([Li, Ye & Zheng 2022 JFE], [“Refusing the best price?” New York Stock Exchange order-type data: 57% of orders refuse routing; races, price improvement.])
#e([Aquilina et al. 2020], [the London Stock Exchange platform circuit; 6% of orders arrive at a gateway first but are sequenced behind a rival.])
#e([Basel CBS 2013], [the post-crisis central-counterparty framework.])
#e([Stoll 2000 JF], [“Friction”: tests Roll's estimator on 61 trading days; it recovers 0.0381 of the 0.079 quoted on the NYSE and 0.1115 of 0.129 on Nasdaq, so it understates the quote because processing and inventory cost never reverse.])
#e([Roll 1984 JF], [bid-ask bounce; the spread read from the negative autocovariance of price changes.])
#e([Kyle 1985 ECTA], [a strategic insider trades against noise; the size of the order he submits reveals part of what he knows and is the illiquidity the market charges.])
#e([named results], [asset pricing owns Black–Scholes–Merton, corporate finance owns Modigliani–Miller, and market microstructure owns this course.])

#part("2 · Statutes and rule numbers")

#e([Securities Exchange Act 1934], [Rule 12(f) grants unlisted trading privileges: a stock listed on one exchange trades on all, so listing and trading are separate decisions. Apple lists only on Nasdaq and trades everywhere; BATS runs no listing service.])
#e([national market system], [the project from the mid-1970s to 2007 that made the 16 United States exchanges behave as one.])
#e([Regulation NMS], [Securities and Exchange Commission (SEC) rule, June 2005; four numbered rules.])
#e([Rule 611], [order protection: no trade-through; the receiving exchange must route to the best protected quote, which a smart order router does.])
#e([Rule 610], [access: no locked or crossed market from a resting order; routing fee capped at 0.3 cents a share.])
#e([Rule 612], [sub-penny: minimum tick one cent.])
#e([611 against 610], [Rule 611 catches orders that execute, Rule 610 orders that rest, and the locking and crossing ban does not reach hidden quotes.])
#e([what Rule 611 protects], [the price and nothing else: a complying order still pays the venue fee, still consumes its liquidity, and still leaks how much remains.])
#e([Rules 601, 603], [market data: the direct feed.])
#e([securities information processor], [aggregates every exchange's book and trades into the consolidated quotation and consolidated tape, which give the NBBO; nothing trades through it.])
#e([flickering quotes], [exempt from trade-through for up to one second, because the data is older than the market.])
#e([NYSE Rule 104], [a designated market maker must trade for its own account to keep a fair and orderly market (code 12a).])
#e([settlement cycle], [T+2 for stocks, bonds, mutual funds and municipal securities; T+1 for short-term secured bonds and Treasury bills; T+0 for futures.])

#part("3 · Venues and mechanisms")

#e([one venue or many], [Hong Kong runs the HKEX, the United Kingdom the LSE, Japan the TSE; China splits into A and B shares; the US, Canada and India are fragmented.])
#e([16 exchanges], [13 by 2020. Cboe: BZX, BYX, EDGA, EDGX. ICE: NYSE, Arca, American, National. Nasdaq: Nasdaq, BX, PHLX. Outside: CHX, IEX.])
#e([1998 volume], [NYSE 52%, Nasdaq 40%, other exchanges 8%.])
#e([2015 volume], [FINRA trade reporting facility 20.3%, Nasdaq 15.9%, dark pools 15.1%, NYSE 12.6%, Arca 11.2% (Credit Suisse).])
#e([market data revenue], [the Wall Street Journal of 16 October 2018 reported the SEC blocking higher data fees, the offset to falling trading revenue.])
#e([specialist vs dealer], [NYSE and AMEX run specialist (designated market maker) auctions, whose members may not trade for profit or outbid floor traders; Nasdaq runs a dealer market of registered makers that may.])
#e([over-the-counter venues], [dealer-customer and inter-dealer; request-for-quote platforms from the 2000s; electronic communication networks; the cost is search-and-matching plus counterparty risk, ex-ante and ex-post.])
#e([foreign exchange], [inter-dealer through Reuters/Refinitiv and EBS; about 30 secondary networks, 22 single-dealer platforms, 12 principal trading firms, 2–3 dark pools; volume against volatility $R^2 = 0.6$ over 2010–2021.])
#e([Tradition 2019], [inter-dealer broker revenue: currencies and rates 43%, securities 32%, commodities 21%, retail foreign exchange 4%.])
#e([auction forms], [first-price, second-price, all-pay; a Dutch auction is a descending clock (first-price), an English one an ascending outcry (second-price); revenue equivalence links them.])
#e([gold fixing], [London, twice a day at 10:30 and 15:00, set by a small panel of members as the reference price, which makes collusion possible.])
#e([United States Treasuries], [primary market runs as a first-price single-sided auction, about a trillion dollars a quarter.])
#e([closing price uses], [fund net asset values, margin, mark-to-market flows, index inclusion, and derivative settlement.])
#e([clearing house], [buyer to every seller and seller to every buyer; guarantees completion, not value; central clearing covers interest-rate swaps and credit default swaps.])
#e([central securities depository], [keeps ownership and custody, completes the trade when one side fails, charges both sides into a buffer, and restricts the failing party's trading.])

#part("4 · Hard numbers")

#e([Chicago–New York link], [cable, mid-1980s: 1,000 miles, 14.5 ms; Spread Networks fiber, August 2010: 825 miles, 13.1 ms, the 3 ms saved put at 300 million dollars; McKay and Tradeworx microwave, July 2012: 744 miles, 9 ms, then 731 miles, 8.5 ms; light in vacuum about 5 ms.])
#e([May 2024], [the Commodity Futures Trading Commission fined J.P. Morgan Securities 100 million dollars over eight years of unsurveilled spoofing.])
#e([high-frequency clock], [microseconds to nanoseconds, a human cannot follow it.])
#e([spoofing], [stack the book on one side with orders meant to be pulled, pull them, then sweep the other side.])
#e([quote stuffing], [Abbott Laboratories, 17 August, 10:07:27: 11,557 orders in one second against a normal 38 a second (Nanex); another burst ran 10,704 then 5,483, all but 14 cancelled within the second.])
#e([sniping races], [the intermarket sweep supplies about 77% of them.])
#e([hidden orders 2019], [over 18% on NASDAQ, 20% on Frankfurt, 22% on Euronext-Paris.])
#e([London, 2003], [a random end time for the closing auction, after traders gamed the indicative price.])
#e([HKEX closing auction], [ran from 2008 and was suspended ten months later over suspected manipulation.])
#e([NYSE fees], [take ¢0.21, make ¢0.13; routing ¢0.30, the Rule 610 cap; an inverted schedule pays the taker. A routed make order becomes a taker, and Rule 611 picks price, not fees. Explicit fees overall ≈ 0.05 bp.])
#e([sessions], [pre-market 8:00–9:15, after-market 16:15–18:30; on-open and on-close orders activate at those auctions.])

#part("5 · Order vocabulary")

#e([four instruction classes], [time (day, good-till-cancel), execution (immediate-or-cancel, all-or-nothing, fill-or-kill), price (pegged, stop), display (hidden, reserve).])
#e([all-or-nothing, fill-or-kill], [never filled in part; fill-or-kill is all-or-nothing plus immediate-or-cancel.])
#e([immediate-or-cancel], [fills at once, cancels the rest; a RegNMS-compliant form is the NMS IOC at the NYSE.])
#e([order lists], [the NYSE and IEX publish different order-type lists.])
#e([stop], [dormant until the last price touches the stop; a buy triggers upward, a sell downward.])
#e([primary peg], [a buy one tick below the national best bid, a sell one tick above the national best offer; hidden.])
#e([midpoint peg], [priced at the national best bid and offer (NBBO) midpoint.])
#e([hidden order], [shows part of its size; ranks behind displayed orders at the same price.])
#e([dark pool], [an alternative trading system, fully hidden, executing at the NBBO midpoint by pro-rata crossing: $P = min(1, n_s/n_b)$.])
#e([intermarket sweep], [the broker merges all quote feeds and releases one child order per venue in the same instant; exempt from Rule 611.])
#e([do-not-ship], [the venue's router is switched off, trading price protection away; the limit form cancels whatever would lock or cross.])
#e([non-routable], [intermarket sweep and do-not-ship, each in immediate-or-cancel and limit form: four types.])
#e([splitting an order], [pro-rata allocation is the most popular routing pattern, then time priority, then round robin.])

#part("6 · What NYSE order types do (Li, Ye & Zheng 2022)")

#table(
  columns: (52pt, 34pt, 34pt, 30pt, 32pt, 26pt, 32pt),
  inset: 2pt, stroke: 0.3pt + luma(190),
  align: (left, right, right, right, right, right, right),
  [#eh[type]], [#eh[trades]], [#eh[size]], [#eh[fill]], [#eh[take]], [#eh[route]], [#eh[make]],
  [plain market], [6.36M], [278.96], [100%], [66.34], [33.64], [0],
  [plain IOC], [4.20M], [268.63], [19.48%], [98.07], [1.93], [0],
  [ISO], [25.41M], [244.30], [22.48%], [100], [0], [0],
  [DNS IOC], [14.65M], [307.09], [31.86%], [100], [0], [0],
  [day limit], [43.36M], [220.50], [2.71%], [29.78], [14.28], [55.94],
  [DNS limit], [44.24M], [182.38], [3.72%], [11.43], [0], [88.57],
)

#e([routing refused], [57% of New York Stock Exchange orders refuse the routing Regulation NMS requires.])
#e([first responders], [495 a day against 1,652 trades, a non-marketable limit refilling a consumed price within 0.1 s; 75.6% do-not-ship limit, 24.4% day limit.])
#e([cancellation race], [a do-not-ship limit escapes a sniping event 42% of the time; a routable limit almost never does.])
#e([race winners], [only the plain IOC announces itself, and it alone loses more races than it wins (13.42 against 17.37); the ISO wins 57.26% of 140.71, the DNS IOC 37.28% of 91.63.])
#e([weighted price contribution], [the order types partition the price move and sum to 100%; the non-routable types contribute more than the whole move, so they trade on new information.])
#e([price improvement], [26.99% of routed market orders fill at the arrival quote, none of the routed plain IOC; 77.49% of day limit and 79.51% of reserve orders get no improvement.])

#part("7 · Data traps")

#e([bid-ask bounce], [execution prices zigzag between bid and ask with no change in value, so a computed variance reads mechanics as news; Roll (1984) measures it.])
#e([inside the spread], [internalized orders (NYSE floor traders), hidden orders, and midpoint pegs at IEX; the terms are not in limit-order-book (LOB) data.])
#e([outside the spread], [an intermarket sweep prints worse than the NBBO and the securities information processor records it; negotiated blocks trade “upstairs” through NYSE specialists at prices far off the NBBO.])
#e([VWAP prints], [a block sold by negotiation at 3:30 pm at the volume-weighted average price prints above the best ask, so price data alone reads it as a buy.])
#e([double counting], [where both brokers report, the consolidated tape counts each trade twice.])
#e([LOB data], [records winners only: a failed cancel and a losing immediate-or-cancel order are absent.])
#e([message data], [every attempt, time-stamped at the gateway; London Stock Exchange data are available under Section 165 of the Financial Services and Markets Act; TAQ and MIDAS are the consolidated LOB sets.])

#part("8 · Platform and post-trade")

#e([circuit], [firewall, gateways (validating), sequencer (round-robin, fixing arrival order), matching engine (serial, price-time), then distribution server and market data processor.])
#e([disclosed platforms], [the London Stock Exchange, Deutsche Börse, and the Chicago Mercantile Exchange publish their design; most others do not.])
#e([speed bump], [a venue that sells speed services, such as a direct data feed, while deliberately slowing incoming orders.])
#e([delivery versus payment], [each leg is released only once the other is in place, so a failure on one side leaves the other side whole.])
#e([physical delivery], [in-kind commodities and futures add storage and financing cost, and markets for temporary storage and substitutes.])
#e([participants], [broker earns a fee and keeps no position, dealer is the other side and earns the spread, broker-dealers do both.])
#e([investors], [retail trade through brokers; institutions hold only vetted securities, so index inclusion shifts the investor base, the index effect.])
#e([speculators and arbitrageurs], [speculators take a directional view; arbitrageurs trade a price gap between two markets or instruments.])
#e([hedgers, producers, government], [hedgers offload other risk and are the “noise” of theory; producers hold private supply information; governments act through open market operations and quantitative easing.])

#part("9 · Course vocabulary")

#e([two liquidity senses], [market liquidity is how cheaply an asset trades; funding liquidity is the financing a trader needs.])
#e([market quality], [two pillars: liquidity, and price discovery (price efficiency).])
#e([three perspectives], [positive (what happens), equilibrium (what each player does, what results), normative (how to design and regulate).])
#e([market-based evaluation], [welfare is unobservable, so structure is judged on prices and market metrics through the efficient-market hypothesis.])
#e([efficient price], [$p^* = E[v | "available information"]$; deviations come from absent informed trading, information frictions, and structural frictions.])
#e([trading needs], [private value, information or belief, and non-fundamental needs such as needing cash.])
#e([order attributes], [price, quantity, direction, plus priority and speed, execution quality and risk, transparency.])
#e([locked and crossed], [the best bid equals the best ask (locked) or exceeds it (crossed); impossible on one book, routine across venues and in limit-order-book data.])
#e([marketable limit order], [priced at or through the far quote, so it takes liquidity and, once filled, is indistinguishable from a market order.])
#e([near and far side], [a buyer's near side is the bid and its far side the ask; a seller's is the reverse.])
#e([mid-point quote], [the average of the best bid and the best ask, used as the fair-price reference and never traded at.])
#e([auction phases], [call phase (indicative price and quantity only, ending at a random time), price determination (maximizes volume), market balancing (makers absorb the excess).])
#e([Walras], [an auctioneer calls a tentative price and moves it until demand equals supply; with frictions the clearing problem is NP-hard and several prices can clear.])

#part("10 · Formulas (notes 1–5)")

#e([spread], [$a - b$ quoted; relative spread $(a - b)/m$; a buyer pays $a - m = (a - b)/2$ above the mid, a seller the same below.])
#e([mid price], [$m = (a + b)/2$, the reference the pegs and the dark pools track.])
#e([effective spread], [$2|p - m|$ for a trade at $p$; price improvement is $a - p$ on a buy, $p - b$ on a sell.])
#e([fee arithmetic], [the venue keeps $f_"take" - f_"make"$; Rule 610 caps $f_"route" <= 0.3$ cents, and 0.3 cents on a 100-dollar share is 0.3 bp.])
#e([tick value], [1 cent on a 100-dollar share is 1 bp; the grid is $p_0 + k$ cents, so 101.255 is not a price.])
#e([dark pool fill], [$P = min(1, n_s/n_b)$; an informed buyer faces $min(1, n_s^U/(n_b^U + n_b^I))$.])
#e([light in fiber], [about $2 times 10^8$ m/s, so 5 microseconds a kilometre; New York to Chicago is roughly 1,200 km one way.])
#e([order arrivals], [Poisson with rate $lambda$, so $op("Pr")("none in" Delta t) = e^(-lambda Delta t)$ and the mean wait is $1/lambda$ (Garman).])
#e([a race of equals], [with rival orders of equal speed each wins with probability $1/k$, so speed is a winner-takes-all investment.])
#e([funding a settlement], [two extra days of cash cost $2r/365$ of the notional at rate $r$, the price of $T+2$ over $T+0$.])
#e([auction price], [one price clears the largest volume, where the demand and supply curves cross; Walras moves the tentative price up while $D > S$ and down while $D < S$.])

#part("11 · Information and spread formulas (notes 6–9, taught before this midterm)")

#e([conditional probability], [$op("Pr")(A|B) = op("Pr")(A inter B)/op("Pr")(B)$.])
#e([Bayes worked], [prior 0.6 infected, $op("Pr")(-|I) = 0.05$, $op("Pr")(-|N) = 0.95$: posterior odds $1.5/19$, so $op("Pr")(I|-) = 3/41$, about 7%.])
#e([total probability], [$op("Pr")(A) = sum_i op("Pr")(B_i) op("Pr")(A|B_i)$ over a partition $B_i$.])
#e([Bayes], [$op("Pr")(A|B) = op("Pr")(B|A) op("Pr")(A)/op("Pr")(B)$; posterior odds $=$ prior odds $times$ likelihood ratio.])
#e([binary signal], [prior $1/2$ and precision $delta$ give $op("Pr")(V_H|S_H) = delta$, posterior odds $delta/(1-delta)$.])
#e([normal update], [$E[v|s] = tau/(tau + tau_e) mu + tau_e/(tau + tau_e) s$, with $tau = 1/sigma^2$ and $tau_e = 1/sigma_e^2$.])
#e([conditioning on $y$], [$E[x|y] = mu_x + rho (sigma_x/sigma_y)(y - mu_y)$ and $op("Var")(x|y) = sigma_x^2 (1 - rho^2)$, the general form the normal update is a case of.])
#e([posterior variance], [$op("Var")(v|s) = 1/(tau + tau_e) = sigma^2 sigma_e^2/(sigma^2 + sigma_e^2)$; independence is what lets the precisions add.])
#e([signal response], [$E[v|s] = mu + rho^2 (s - mu)$, the same weight written as the squared correlation $rho^2 = sigma^2/(sigma^2 + sigma_e^2)$, which is the regression $R^2$.])
#e([signal informativeness], [$eta_"s" = op("Var")(v)/op("Var")(v|s) = 1 + tau_e/tau = 1/(1 - rho^2) >= 1$, so $op("Var")(v|s) = op("Var")(v)/eta_"s"$.])
#e([price efficiency], [$eta_"p" = op("Var")(v|s)/op("Var")(v|p) = (tau_v + tau_p)/(tau_v + tau_e) <= 1$, a different ratio: the price against the insider, not the prior. It reaches 1 only when $sigma_z = 0$.])
#e([price precision], [$tau_p = 1/(sigma_e^2 + (sigma_z/(n_I tau_e))^2)$, so it rises with $n_I$ and with $tau_e$ but never reaches $tau_e$.])
#e([the two etas], [opposite directions: $eta_"s" >= 1$ says how much a signal adds and equals 1 when it adds nothing, while $eta_"p" <= 1$ says how much of the insider the price carries and equals 1 when the price knows everything.])
#e([standardized signal], [$(s - mu)/sigma$ leaves the informativeness unchanged, so signals in different units can be ranked by one number.])
#e([demand in equilibrium], [$x = (E[v|"info"] - p)/(gamma op("Var")(v|"info"))$ and $p^* = (n_I tau_e s - X)/(n_I (tau_v + tau_e) + n_U tau_v)$, so supply $X$ lowers the price and the signal raises it.])
#e([price as signal], [$p = alpha + beta s + gamma z$ with $beta = n_I tau_e/(n_I tau_e + N tau_v)$ and $gamma/beta = 1/(n_I tau_e)$.])
#e([price efficiency], [$tau_p = 1/op("Var")(v|p) < tau_e$ and $eta < 1$ once noise trades; at $z = 0$ the price reveals $s$ exactly and the informed pay for nothing.])
#e([Glosten–Milgrom quote], [$op("Pr")("buy"|v = +-sigma) = (1 +- mu)/2$, so $A^* = E[v|"buy"] = mu sigma$ and $B^* = -mu sigma$.])
#e([spread from information], [$S = A^* - B^* = 2 mu sigma$; the maker loses $(1-mu)sigma$ on each informed trade and gains $mu sigma$ on each noise trade, so the transfer is $mu(1-mu)sigma$.])
#e([pure adverse selection], [in Glosten–Milgrom no inventory and no processing cost enters, so the whole spread is information.])
#e([Roll price], [$p_t = m_t + (S/2) d_t$ with $d_t = +-1$ equally likely and $m_t = m_(t-1) + e_t$, $e_t$ i.i.d. normal.])
#e([Roll changes], [$Delta p_t = (S/2)(d_t - d_(t-1)) + e_t$: only a switch of side moves the print, and then by $S$.])
#e([Roll moments], [$E[Delta p_t] = 0$ and $op("Var")(Delta p_t) = S^2/2 + sigma_e^2$, so the bounce alone is a floor under measured variance.])
#e([Roll estimator], [$op("Cov")(Delta p_t, Delta p_(t-1)) = -S^2/4$, hence $S = 2 sqrt(-op("Cov")(Delta p_t, Delta p_(t-1)))$ and $sigma_e^2 = op("Var")(Delta p) - S^2/2$.])
#e([bounce share], [$100 times (S^2/2)/op("Var")(Delta p_t)$ per cent of measured variance is trading cost, not news.])
#e([no-trade theorem], [identical information rules out trade at every price; differing signals leave the open interval between the two valuations, and full common knowledge closes it.])
#e([no-trade worked], [with $V_H = 120$, $V_L = 0$ and precision $2/3$ the two valuations are 80 and 40, so the trade interval is the open span between them.])
#e([complete markets], [the theorem needs complete markets and common knowledge of rationality as well as common priors; drop any one and trade returns.])
#e([tied races], [a race that $q$ orders tie is split $1/q$ each, then averaged at the stock-day level (Li, Ye & Zheng).])
#e([Grossman–Stiglitz demand], [$U(x) = E[x(v-p)] - (gamma/2) op("Var")(x v)$, so $x = (E[v|"info"] - p)/(gamma op("Var")(v|"info"))$: an edge over a risk.])
#e([strong-form efficiency], [impossible when information is costly, since it needs $z = 0$ and without noise nobody pays to learn; the price is semi-strong at best.])

#part("12 · Weighted price contribution by order type (Li, Ye & Zheng 2022)")

#table(
  columns: (86pt, 56pt, 44pt),
  inset: 2pt, stroke: 0.3pt + luma(190),
  align: (left, right, right),
  [#eh[type]], [#eh[volume share]], [#eh[WPC]],
  [plain market], [6.77%], [-4.56%],
  [plain IOC], [6.36%], [3.86%],
  [ISO], [35.69%], [90.32%],
  [DNS IOC], [25.87%], [27.10%],
  [day limit], [16.37%], [-13.78%],
  [DNS limit], [5.30%], [-2.34%],
  [reserve limit], [3.43%], [-0.95%],
  [DNS reserve limit], [0.21%], [0.35%],
)

#e([sums], [the non-routable types reach 115.43% and the routable ones -15.43%, so the types that refuse routing produce the whole move and the excess.])
#e([which type moves the price], [the ISO, on a third of the taking volume; the largest negative is the day limit order.])
#e([waiting beats arriving late], [the DNS IOC and the DNS limit share a routing instruction but score +27.10% and -2.34%: what separates them is whether the order waits on the book or executes on arrival.])
