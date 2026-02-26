---
aliases:
  - Derivative Securities
  - Derivative Securities index
  - FINA 3103
  - FINA 3103 index
  - FINA3103
  - FINA3103 index
  - HKUST FINA 3103
  - HKUST FINA 3103 index
  - HKUST FINA3103
  - HKUST FINA3103 index
tags:
  - flashcard/active/special/academia/HKUST/FINA_3103
  - function/index
  - language/in/English
---

# index

- HKUST FINA 3103
- name: Intermediate Investments

The content is in teaching order.

- grading
  - scheme
    - homework assignments ×4: 20%
    - midterm examination: 25%
    - final examination: 55%

## children

- [arbitrage pricing theory](arbitrage%20pricing%20theory.md)
- [assignments](assignments/index.md)
- [behavioural finance](behavioural%20finance.md)
- [capital asset pricing model](capital%20asset%20pricing%20model.md)
- [efficient frontier](efficient%20frontier.md)
- [efficient-market hypothesis](efficient-market%20hypothesis.md)
- [fixed income](fixed%20income.md)
- [forward and futures](forward%20and%20futures.md)
- [investment fund](investment%20fund.md)
- [option](option.md)
- [questions](questions.md)

## week 1 lecture

- datetime: 2025-09-02T15:00:00+08:00/2025-09-02T16:20:00+08:00, PT1H20M
- topic: logistics; introduction
- FINA 3103
  - FINA 3103 / logistics
  - FINA 3103 / textbook ::@:: Bodie, Kane and Marcus \(BKM\), "Essentials of Investments", 13th Edition <!--SR:!2026-07-31,246,330!2026-08-28,267,330-->
  - FINA 3103 / prerequisites
  - FINA 3103 / background ::@:: statistics: covariance, expectation, linear regression \(OLS\), population, random variable, sample, variance, etc. <!--SR:!2026-08-22,262,330!2026-08-31,268,330-->
  - FINA 3103 / grading
  - FINA 3103 / rules
  - FINA 3103 / schedule
- [investment](../../../../general/investment.md) ::@:: It is traditionally defined as the "commitment of resources into something expected to gain value over time". <p> \(__this course__: Allocate _resources_ between _time_ \(sacrifice now to get something later\) and _states_ \(current commitment of money\).\) <!--SR:!2026-08-27,267,330!2026-05-25,186,310-->
  - investment / motivation ::@:: You want to get more _resources_. Investment allows you to do so in the future. However, there is also _uncertainty_. <p> All of these can be modeled using _utility_, which measures _satisfaction_ and incorporates resource value, risk, time value, etc. Then, we want to _maximize utility_. <!--SR:!2026-09-16,282,330!2026-08-05,250,330-->
- [finance](../../../../general/finance.md) ::@:: It refers to monetary resources and to the study and discipline of money, currency, assets and liabilities. <!--SR:!2026-08-27,266,330!2026-09-07,276,330-->
  - finance / fields ::@:: 3 main fields: asset pricing, corporate finance, market microstructure <!--SR:!2026-08-29,268,330!2026-07-24,240,330-->
    - finance / fields / asset pricing ::@:: Calculate asset _fair price_. <p> examples: Black–Scholes–Merton model \(a mathematical model\) <!--SR:!2026-08-29,267,330!2026-08-30,269,330-->
    - finance / fields / corporate finance ::@:: Calculate _firm value_ and decision making based on it. <p> examples: Modigliani–Miller theorem \(capital structure irrelevance principle\) <!--SR:!2026-04-30,170,310!2027-02-18,410,370-->
    - finance / fields / market microstructure ::@:: Relation between _market quality_ and environment, mechanisms, trading rules, etc. <!--SR:!2026-08-25,264,330!2026-08-20,260,330-->
- FINA 3103
  - FINA 3103 / objectives ::@:: Investigate asset pricing and market \(micro\)structure. Invest _wisely_ under different market structures, different trading rules, and uncertainty. <!--SR:!2026-08-26,265,330!2026-09-08,276,330-->
- [security](../../../../general/security%20(finance).md) ::@:: It is a tradable financial asset. The term commonly refers to any form of financial instrument, but its legal definition varies by jurisdiction. <!--SR:!2026-07-24,240,330!2026-09-01,269,330-->
  - security / assets ::@:: 2 main categories: safe assets, risky assets <!--SR:!2026-09-03,272,330!2026-07-18,235,330-->
    - security / assets / safe assets ::@:: bank savings, corporate bonds \(AAA\), government bonds, etc. <!--SR:!2026-08-26,265,330!2026-08-08,252,330-->
    - security / assets / risky assets ::@:: commodities, cryptocurrencies, currencies, derivatives, digital tokens \(e.g. NFTs\), high-yield bonds, stocks/equities, real estates, etc. <!--SR:!2026-09-05,274,330!2026-09-12,279,330-->
  - security / type of holder ::@:: retail: members of the public investing personally, other than by way of business <br/> wholesale: by financial institutions acting on their own account, or on behalf of clients <!--SR:!2026-09-07,276,330!2026-05-29,189,310-->
  - security / trading by individuals ::@:: bank savings: direct, easy \(open a bank account\) <br/> bonds: via _secondary markets_ and _designated dealers_ <br/> crypto: direct \(setup a crypto wallet\) <br/> stocks, derivatives: via _brokers_, e.g. Robinhood, SoFi, etc. <!--SR:!2026-03-31,133,290!2026-06-09,188,310-->
- [order book](../../../../general/order%20book.md) ::@:: It is the list of orders \(manual or electronic\) that a trading venue \(in particular stock exchanges\) uses to record the interest of buyers and sellers in a particular financial instrument. <!--SR:!2026-09-09,276,330!2026-09-13,280,330-->
- [order](../../../../general/order%20(exchange).md) ::@:: It is an instruction to buy or sell on a trading venue such as a stock market, bond market, commodity market, financial derivative market or cryptocurrency exchange. <!--SR:!2026-08-26,266,330!2026-08-30,269,330-->
  - order / types ::@:: 3 main types: conditional order, market order, limit order <!--SR:!2026-09-10,277,330!2026-08-07,251,330-->
  - order / market order ::@:: It is a buy or sell order to be executed immediately at the _current market_ prices. <!--SR:!2026-07-20,237,330!2026-05-29,189,310-->
  - order / limit order ::@:: It is an order to buy a security at no more than a specific price, or to sell a security at no less than a specific price \(called "or better" for either direction\). \(annotation: __Important__. "No more than" and "no less than" includes "equals to".\) <!--SR:!2026-04-28,166,310!2026-08-10,254,330-->
  - order / conditional order ::@:: It is any order other than a limit order which is executed only when a specific condition is satisfied. <!--SR:!2026-08-23,262,330!2026-08-09,253,330-->
- [stock exchange](../../../../general/stock%20exchange.md) ::@:: \(__this course__: "on exchange"\) It is an exchange where stockbrokers and traders can buy and sell securities, such as shares of stock, bonds and other financial instruments. <!--SR:!2026-09-04,272,330!2026-09-03,272,330-->
  - stock exchange / advantages ::@:: facilities liquidity, maintains the current market price, provides transparency <!--SR:!2026-09-17,283,330!2026-09-04,273,330-->
- [alternative trading system](../../../../general/alternative%20trading%20systen.md) \(ATS\) ::@:: \(__this course__: "off exchange"\) It is a US and Canadian regulatory term for a non-exchange trading venue that matches buyers and sellers to find counterparties for transactions. <!--SR:!2026-09-02,271,330!2026-09-14,280,330-->
- [dark pool](../../../../general/dark%20pool.md) ::@:: \(__this course__: "off exchange"\) It is a private forum \(alternative trading system or ATS\) for trading securities, derivatives, and other financial instruments. <!--SR:!2026-07-30,245,330!2026-09-04,273,330-->
- [market microstructure](../../../../general/market%20microstructure.md) ::@:: It is a branch of finance concerned with the details of how exchange occurs in markets. <!--SR:!2026-09-06,274,330!2026-08-06,251,330-->
- [risk–return spectrum](../../../../general/risk–return%20spectrum.md) ::@:: It is the relationship between the amount of return gained on an investment and the amount of risk undertaken in that investment. The more return sought, the more risk that must be undertaken. <!--SR:!2026-09-19,285,330!2026-04-23,162,310-->
  - risk–return spectrum / examples ::@:: gambling: high return \(if you win\), high risk \(of losing\) <br/> saving: low return, low-to-no risk <!--SR:!2026-08-28,268,330!2026-07-18,235,330-->
- [risk aversion](../../../../general/risk%20aversion.md) ::@:: It is the tendency of people to prefer outcomes with low uncertainty to those outcomes with high uncertainty, even if the average outcome of the latter is equal to or higher in monetary value than the more certain outcome. <!--SR:!2026-09-09,276,330!2026-08-29,268,330-->
  - risk aversion / examples ::@:: receive \$1 with certainty vs. receive either \$0 or \$2 with equal probability \(50%\) <!--SR:!2026-07-30,245,330!2026-09-14,281,330-->
- [risk-seeking](../../../../general/risk-seeking.md) ::@:: It is a person who has a preference _for_ risk. <!--SR:!2026-09-13,280,330!2026-09-15,281,330-->
  - risk-seeking / people ::@:: While most investors are considered risk averse, one could view casino-goers as risk-seeking. <!--SR:!2026-08-05,250,330!2026-08-27,266,330-->
- [risk neutral preferences](../../../../general/risk%20neutral%20preferences.md) ::@:: They are preferences that are neither risk averse nor risk seeking. <!--SR:!2026-07-20,237,330!2026-09-17,283,330-->
  - risk neutral preferences / decision making ::@:: A risk neutral party's decisions are not affected by the degree of uncertainty in a set of outcomes, so a risk neutral party is indifferent between choices with equal expected payoffs even if one choice is riskier. <!--SR:!2026-07-30,245,330!2026-09-11,278,330-->
- [utility](../../../../general/utility.md) ::@:: It is a measure of a certain person's satisfaction from a certain state of the world. <!--SR:!2026-08-11,255,330!2026-09-11,278,330-->
  - utility / motivation ::@:: It can model _expected return_ and _risk_ together. <!--SR:!2026-08-06,251,330!2026-08-23,263,330-->
- [modern portfolio theory](../../../../general/modern%20portfolio%20theory.md) \(MPT\) ::@:: It is a mathematical framework for assembling a portfolio of assets such that the expected return is maximized for a given level of risk. <!--SR:!2026-08-06,251,330!2026-08-27,264,330-->
  - modern portfolio theory / motivation ::@:: To avoid \(diversifiable\) risk or control risk–return tradeoff by assembling a portfolio \(combination of assets\) optimally. <!--SR:!2026-08-18,258,330!2026-07-31,246,330-->
  - modern portfolio theory / intuition ::@:: Assume there is a stock with low return. Now consider two other stocks, stock A and stock B, both with equally high return. Stock A moves with the low-return stock. Stock B moves _opposite_ to the low-return stock. <p> Combining the low-return stock with stock A does not reduce risk \(variance, volatility\), because they have _similar_ risk factors. Combining it with stock B instead reduces risk \(variance, volatility\), resulting in _risk diversification_ due to their _different_ risk factors. <!--SR:!2026-08-17,257,330!2026-06-10,189,310-->
- [asset pricing](../../../../general/asset%20pricing.md) ::@:: It refers to the formal development of the principles used in pricing, together with the resultant models. <!--SR:!2026-09-18,284,330!2026-07-19,236,330-->
  - asset pricing / return, risk ::@:: Asset price affects return and risk, mostly via capital gain/loss. <!--SR:!2026-05-11,176,310!2026-09-05,273,330-->
  - asset pricing / motivation ::@:: To find the _efficient_/_fair_ price of an asset, which we assume the actual price of the asset will _eventually_ approach. <!--SR:!2026-08-28,267,330!2026-08-31,269,330-->
  - asset pricing / concepts ::@:: arbitrage, friction \(causing slight price differences in practice\), law of one price, market efficiency, etc. <!--SR:!2026-08-24,263,330!2026-05-15,181,310-->
- [arbitrage](../../../../general/arbitrage.md) ::@:: The practice of taking advantage of a difference in prices in two or more markets – striking a combination of matching deals to capitalize on the difference, the profit being the difference between the market prices at which the unit is traded. <!--SR:!2026-09-06,275,330!2026-08-25,265,330-->
  - arbitrage / effect ::@:: Arbitrage has the effect of causing prices of the same or very similar assets in different markets to converge. <!--SR:!2026-09-12,279,330!2026-08-30,267,330-->
- [law of one price](../../../../general/law%20of%20one%20price.md) ::@:: In the absence of trade frictions \(such as transport costs and tariffs\), and under conditions of free _competition_ and price flexibility \(where no individual sellers or buyers have power to manipulate prices and prices can freely adjust\), _identical goods_ sold at _different locations_ should be sold for the _same price_ when prices are expressed in a common currency. <!--SR:!2026-03-07,125,290!2026-09-19,285,330-->
  - law of one price / mechanism ::@:: This law is derived from the assumption of the inevitable _elimination of all arbitrage_. <!--SR:!2026-07-25,241,330!2026-09-07,275,330-->
- [efficient-market hypothesis](../../../../general/efficient-market%20hypothesis.md) \(EMH\) ::@:: It is a hypothesis in financial economics that states that asset prices reflect all available information. <!--SR:!2026-09-03,271,330!2026-08-05,250,330-->
  - efficient-market hypothesis / implication ::@:: A direct implication is that it is impossible to "beat the market" consistently on a risk-adjusted basis since market prices should only react to new information. <!--SR:!2026-08-31,270,330!2026-08-10,254,330-->
  - efficient-market hypothesis / intuition ::@:: Suppose you know some private information on a stock. You buy or sell the stock. Its price changes due to your action, reflecting the private information. <!--SR:!2026-09-05,274,330!2026-05-14,177,310-->
  - efficient-market hypothesis / reality ::@:: Grossman-Stiglitz paradox, irrationality, etc. <!--SR:!2026-08-22,261,330!2026-07-25,241,330-->
- [Grossman-Stiglitz paradox](../../../../general/Grossman-Stiglitz%20paradox.md) ::@:: It argues perfectly informationally efficient markets are an impossibility since, if prices perfectly reflected available information, there is no profit to gathering information, in which case there would be little reason to trade and markets would eventually collapse. <!--SR:!2026-09-18,284,330!2026-08-09,253,330-->
- [behavioural finance](../../../../general/behavioural%20finance.md) ::@:: It is the study of the influence of psychology on the behaviour of investors or financial analysts. It assumes that investors are not always rational, have limits to their self-control and are influenced by their own biases. <!--SR:!2026-07-24,240,330!2026-07-31,246,330-->
- efficient-market hypothesis
  - efficient-market hypothesis / reality
    - efficient-market hypothesis / reality / reasons ::@:: framing \(e.g. effect of salience\), information, luck, sophistication, skills, etc. <!--SR:!2026-05-23,185,310!2026-05-03,170,310-->
- [performance appraisal](../../../../general/performance%20appraisal.md) ::@:: It is a periodic and systematic process whereby the job performance of an employee is documented and evaluated. <!--SR:!2026-09-14,281,330!2026-07-19,236,330-->
  - performance appraisal / finance ::@:: need to separate the skill of portfolio manager from luck <!--SR:!2026-09-19,285,330!2026-08-21,261,330-->
- [fixed income](../../../../general/fixed%20income.md) ::@:: It refers to any type of investment under which the borrower or issuer is obliged to make payments of a fixed amount on a fixed schedule. <!--SR:!2026-09-15,281,330!2026-04-28,166,310-->
- [derivative](../../../../general/derivative%20(finance).md) ::@:: It is a contract between a buyer and a seller. The derivative can take various forms, depending on the transaction, but every derivative has the following four elements: ... <!--SR:!2026-03-17,129,390!2026-03-18,130,390-->
  - derivative / elements ::@:: tradeable item, future act, future act price, future act time <!--SR:!2026-08-24,264,330!2026-09-06,274,330-->
    - derivative / elements / tradeable item ::@:: an item \(the "underlier"\) that can or must be bought or sold, e.g. commodity, event, financial asset, intangible good, natural condition index, etc. <!--SR:!2026-07-21,237,330!2026-05-13,177,310-->
    - derivative / elements / future act ::@:: a future act which must occur \(such as a sale or purchase of the underlier\) <!--SR:!2026-08-16,256,330!2026-08-19,259,330-->
    - derivative / elements / future act price ::@:: a price at which the future transaction must take place <!--SR:!2026-09-02,271,330!2026-08-30,268,330-->
    - derivative / elements / future act time ::@:: a future date by which the act \(such as a purchase or sale\) must take place <!--SR:!2026-09-16,282,330!2026-09-13,280,330-->
- market microstructure
  - market microstructure / concepts ::@:: fragmented markets, number of exchanges in a country or region, trading speed, transparency, etc. <!--SR:!2026-09-03,272,330!2026-09-12,279,330-->
  - market microstructure / measures ::@:: liquidity: How easy is it to trade assets? <br/> price discovery: How fast does price reacts to news? <!--SR:!2026-08-28,265,330!2026-08-29,266,330-->
- [high-frequency trading](../../../../general/high-frequency%20trading.md) \(HFT\) ::@:: It is a type of algorithmic automated trading system in finance characterized by high speeds, high turnover rates, and high order-to-trade ratios that leverages high-frequency financial data and electronic trading tools. <!--SR:!2026-09-06,275,330!2026-04-24,163,310-->
  - high-frequency trading / latency arbitrage ::@:: Assume there are two assets that _theoretically_ should always have the same price in two distinct locations. In practice, one asset may update its price slightly later \(by a few milliseconds or even nanoseconds\), which can be exploited by high-frequency trading. <p> This shows trading speed matters. It matters so much that dedicated communication channels to exchanges with extremely low latency are built and improved. <!--SR:!2026-04-24,163,310!2026-08-31,270,330-->
- [decentralized finance](../../../../general/decentralized%20finance.md) \(DeFi\) ::@:: It provides financial instruments and services through smart contracts on a programmable, permissionless blockchain. This approach reduces the need for intermediaries such as brokerages, exchanges, or banks. <!--SR:!2026-05-04,171,310!2026-05-26,187,310-->
  - decentralized finance / technologies ::@:: blockchain, crypto, etc. <!--SR:!2026-09-01,270,330!2026-07-25,241,330-->
  - decentralized finance / advantages ::@:: democratize finance, efficient \(in some aspects\), robust, etc. <!--SR:!2026-08-29,268,330!2026-07-30,245,330-->
  - decentralized finance / decentralized exchanges \(DEX\) ::@:: They are a type of cryptocurrency exchange, which allow for either direct peer-to-peer, or Automated Market Maker \(AMM\) liquidity pool cryptocurrency transactions to take place without the need for an intermediary. The lack of an intermediary differentiates them from centralized exchanges \(CEX\). <!--SR:!2026-05-12,176,310!2026-08-18,258,330-->
    - decentralized finance / decentralized exchanges / examples ::@:: PancakeSwap, Uniswap, etc. <!--SR:!2026-09-02,270,330!2026-09-10,277,330-->

## week 1 lecture 2

- datetime: 2025-09-04T15:00:00+08:00/2025-09-04T16:20:00+08:00, PT1H20M
- topic: trading securities
- finance
  - finance / components ::@:: financial assets + participants + financial systems <!--SR:!2027-03-16,426,390!2027-03-20,429,387-->
- [financial asset](../../../../general/financial%20asset.md) ::@:: It is a non-physical asset whose value is derived from a contractual claim, such as bank deposits, bonds, and participations in companies' share capital. <p> \(__this course__: A contract allocating _resources_ between _time_ \(sacrifice now to get something later\) and _states_ \(current commitment of money\).\) <!--SR:!2027-05-19,475,390!2027-05-03,461,390-->
  - financial asset / examples ::@:: bank deposits, bonds, cash or cash equivalent, certificate of deposit \(CD\), derivatives, loans, receivables, stocks, etc. <!--SR:!2027-05-06,464,387!2027-03-15,425,390-->
- [financial system](../../../../general/financial%20system.md) ::@:: It is a system that allows the exchange of funds between financial market participants such as lenders, investors, and borrowers. Financial systems operate at national and global levels. <!--SR:!2027-04-21,454,390!2027-05-24,480,390-->
  - financial system / examples ::@:: banks, financial institutions, financial markets <!--SR:!2027-04-21,454,390!2027-04-29,462,390-->
- [financial regulatory authority](../../../../general/financial%20regulatory%20authority.md) ::@:: It is a public authority whose role is to ensure the proper implementation of financial regulation within its scope of responsibility. <!--SR:!2026-10-26,295,370!2027-03-27,434,390-->
  - financial regulatory authority / examples ::@:: China: CBIRC <br/> Hong Kong: HKMA, HKSFC <br/> United States: CFTC, SEC <!--SR:!2027-05-22,478,390!2027-03-16,426,390-->
- financial asset
  - financial asset / classification ::@:: marketable \(tradeable\), non-marketable <!--SR:!2027-03-04,416,390!2027-04-06,439,390-->
    - financial asset / classification / marketable ::@:: derivative: forwards, futures, options, swaps, etc. <br/> primitive: debt, equity <!--SR:!2026-08-20,253,367!2027-03-14,416,370-->
    - financial asset / classification / non-marketable ::@:: debt: securitized claims, etc. <br/> equity <!--SR:!2027-04-09,442,390!2027-04-07,440,390-->
- [money market](../../../../general/money%20market.md) ::@:: It is a component of the economy that provides short-term funds. The money market deals in short-term loans, generally for a period of a year or less. <!--SR:!2027-03-31,438,390!2027-03-09,420,390-->
  - money market / importance ::@:: As short-term securities became a commodity, the money market became a component of the financial market for assets involved in short-term borrowing, lending, buying and selling with original maturities of one year or less. Trading in money markets is done over the counter and is wholesale. <!--SR:!2026-06-05,188,350!2027-03-20,429,390-->
  - money market / instruments ::@:: certificates of deposit \(CD\), commercial papers, eurodollars, \(reverse\) repos, treasury bills <!--SR:!2027-03-06,418,390!2026-11-08,308,370-->
    - money market / instruments / treasury bills ::@:: They are zero-coupon bonds that mature in one year or less, issued by the United States Treasury. <!--SR:!2027-05-27,483,390!2026-12-07,337,370-->
    - money market / instruments / commercial papers ::@:: It is an unsecured promissory note with a fixed maturity of usually less than 270 days. <!--SR:!2027-03-21,430,390!2027-04-30,458,387-->
    - money market / instruments / certificates of deposit \(CD\) ::@:: It is a time deposit sold by banks, thrift institutions, and credit unions in the United States. CDs typically differ from savings accounts because the CD has a specific, fixed term before money can be withdrawn without penalty and generally higher interest rates. <!--SR:!2027-05-22,480,390!2027-05-10,468,390-->
    - money market / instruments / eurodollars ::@:: They are U.S. dollars held in time deposit accounts in banks outside the United States. <!--SR:!2026-08-31,262,370!2027-04-09,442,390-->
    - money markets / instruments / repos ::@:: It is a form of secured short-term borrowing, usually, though not always using government securities as collateral. A contracting party sells a security to a lender and, by agreement between the two parties, repurchases the security back shortly afterwards, at a slightly higher contracted price. <!--SR:!2026-11-16,316,370!2026-05-29,181,347-->
- [capital market](../../../../general/capital%20market.md) ::@:: It is a financial market in which long-term debt \(over a year\) or equity-backed securities are bought and sold, in contrast to a money market where short-term debt is bought and sold. <!--SR:!2027-04-06,439,390!2027-04-19,452,390-->
  - capital market / importance ::@:: Capital markets channel the wealth of savers to those who can put it to long-term productive use, such as companies or governments making long-term investments. <!--SR:!2027-04-27,453,387!2027-03-22,431,390-->
  - capital market / debt ::@:: corporate bonds, eurobonds, foreign bonds, mortgage-backed securities, municipal bonds, treasury notes and bonds, etc. <!--SR:!2026-08-21,254,370!2026-04-10,132,330-->
    - capital market / debt / treasury notes and bonds ::@:: They are long-term bonds that mature in more than a year, issued by the United States Treasury. <p> _Treasury notes_ \(_T-notes_\) have maturities of 2, 3, 5, 7, or 10 years, have a coupon payment every six months, and are sold in increments of \$100. <p> _Treasury bonds_ \(_T-bonds_, also called a _long bond_\) have the longest maturity at twenty or thirty years. <!--SR:!2027-04-17,450,390!2027-04-20,453,390-->
    - capital market / debt / municipal bonds ::@:: It is a bond issued by state or local governments, or entities they create such as authorities and special districts. <!--SR:!2027-03-12,423,390!2027-05-09,467,390-->
    - capital market / debt / corporate bonds ::@:: It is a bond issued by a corporation in order to raise financing for a variety of reasons such as to ongoing operations, mergers & acquisitions, or to expand business. It is a longer-term debt instrument indicating that a corporation has borrowed a certain amount of money and promises to repay it in the future under specific terms. <!--SR:!2027-04-22,455,390!2027-03-14,424,390-->
    - capital market / debt / foreign bonds ::@:: Some companies, banks, governments, and other sovereign entities may decide to issue bonds in foreign currencies as the foreign currency may appear to potential investors to be more stable and predictable than their domestic currency. <p> They are bonds issued in country _B_ by a company in country _A_, denominated by the currency in country _B_. <!--SR:!2027-04-09,442,390!2027-04-11,444,390-->
    - capital market / debt / eurobonds ::@:: It is an international bond that is denominated in a currency not native to the country where it is issued. <p> They are bonds issued in country _B_ by a company in country _A_, denominated by the currency in country _A_. <!--SR:!2026-09-14,275,370!2027-04-30,463,390-->
    - capital market / debt / mortgage-backed securities ::@:: It is a type of asset-backed security \(an "instrument"\) which is secured by a mortgage or collection of mortgages. The mortgages are aggregated and sold to a group of individuals \(a government agency or investment bank\) that securitizes, or packages, the loans together into a security that investors can buy. <!--SR:!2027-05-23,481,390!2026-05-30,182,347-->
  - capital market / equity ::@:: common stocks, depository receipts, preferred stocks, etc. <p> stock characteristics: limited liability, residual income, zero or some voting rights <!--SR:!2027-04-30,456,390!2026-06-03,186,350-->
    - capital market / equity / preferred stocks ::@:: It is a component of share capital that may have any combination of features not possessed by common stock, including properties of both an equity and a debt instrument, and is generally considered a hybrid instrument. <p> Typically, they have no voting rights but receive dividends with higher priority. <!--SR:!2027-04-25,458,390!2026-11-07,307,370-->
    - capital market / equity / common stocks ::@:: It is a form of corporate equity ownership, a type of security. <p> Typically, they have voting rights and receive dividends. <!--SR:!2027-05-16,472,390!2026-11-05,305,370-->
    - capital market / equity / depository receipts ::@:: It is a negotiable financial instrument issued by a bank to represent a foreign company's publicly traded securities. <!--SR:!2027-04-18,451,390!2027-04-14,447,390-->
- derivative
  - derivative / examples ::@:: futures/forwards, options, swaps, etc. <!--SR:!2027-04-19,452,390!2027-05-12,468,390-->
    - derivative / examples / futures/forwards ::@:: It is a contract between two parties to buy or sell an asset at a specified future time at a price agreed on in the contract. <p> The former is standardized, while the latter is non-standardized. <!--SR:!2026-09-25,283,367!2027-05-09,467,390-->
    - derivative / examples / swaps ::@:: It is a derivative contract between two counterparties to exchange, for a certain time, financial instruments, unconventional cashflows, or payments. <!--SR:!2027-04-07,440,387!2026-12-06,336,370-->
    - derivative / examples / options ::@:: It is a contract which conveys to its owner, the _holder_, the right, but not the obligation, to buy or sell a specific quantity of an underlying asset or instrument at a specified strike price on or before a specified date, depending on the style of the option. <!--SR:!2027-05-21,479,390!2027-03-07,418,390-->
- [index](../../../../general/index%20(economics).md) ::@:: It is a number that measures how a group of related data points—like prices, company performance, productivity, or employment—changes over time to track different aspects of economic health from various sources. <!--SR:!2027-05-25,483,390!2027-05-23,479,390-->
  - index / finance ::@:: It indicates the price performance of a basket \(combination\) of securities. <p> Some derivatives are priced based on indices. <!--SR:!2027-04-17,450,390!2027-05-08,466,390-->
  - index / characteristics ::@:: debt or equity, coverage, geographical coverage, sector coverage <!--SR:!2026-11-24,324,370!2027-04-23,456,390-->
  - index / examples ::@:: Barclays: debt <br/> DJI: equity, narrow coverage, general sectors, country <br/> HSCI: broad coverage <br/> HSI: narrow coverage, general sectors <br/> HSI-Fin: sectoral <br/> MSCI: regional <br/> Merrill: debt <br/> S&P&nbsp;500: debt, broad coverage <!--SR:!2027-07-29,514,350!2026-04-01,126,327-->
  - index / weighing ::@:: 2 common methodology: value-weighted, price-weighted <!--SR:!2027-03-31,438,390!2026-08-18,252,367-->
    - index / weighing / price-weighted ::@:: Sum the price of all stocks included in the index. Finally, divide by a divisor, which is initially 1. <p> The divisor is adjusted to mitigate drastic price changes due to stock mergers and splits. <p> examples: Dow Jones Index \(DJI\), etc. <!--SR:!2027-04-28,461,390!2027-03-19,428,387-->
    - index / weighing / value-weighted ::@:: _Market capitalization_ of a stock is the number of outstanding stock multiplied by its price. <p> Sum the market capitalization of all stocks in the index. Divide by the sum of the market capitalization of all stocks in the index at an initial time. Finally, multiply by 100. <p> It is not affected by stock mergers and splits. <p> examples: FTSE&nbsp;100, Hang Seng Index, Nasdaq Composite, S&P&nbsp;500, etc. <!--SR:!2027-03-28,435,390!2026-06-02,185,350-->
- [primary market](../../../../general/primary%20market.md) ::@:: It is the part of the capital market that deals with the issuance and sale of securities to purchasers directly by the issuer, with the issuer being paid the proceeds. <!--SR:!2026-05-31,183,347!2027-04-26,459,390-->
  - primary market / vs. secondary market ::@:: A primary market means the market for new issues of securities, as distinguished from the secondary market, where previously issued securities are bought and sold. A market is primary if the proceeds of sales go to the issuer of the securities sold. Buyers buy securities that were not previously traded.  <p> Note, only certain types of secondary markets use standardized algorithms to match traders and price assets, e.g. exchanges. \(__this course__: Tested in the midterm examination.\) <!--SR:!2027-03-24,433,390!2027-03-03,415,387-->
  - primary market / offerings ::@:: initial public offering \(IPO\), seasoned offering \(new issuance of stocks that are already publicly traded\), etc. <!--SR:!2027-04-14,447,390!2027-03-27,434,390-->
- [underwriting](../../../../general/underwriting.md) \(UW\) ::@:: These services are provided by some large financial institutions, such as banks, insurance companies and investment houses, whereby they guarantee payment in case of damage or financial loss and accept the financial risk for liability arising from such guarantee. <!--SR:!2027-03-08,419,390!2027-03-28,435,390-->
  - underwriting / steps ::@:: Underwriters provide advice to the firm, e.g. expected raised money, price, type of securities, etc. <p> After the underwriters agree to underwrite, they are obligated to purchase the entire issue at a predetermined price before reselling the securities in the market. Should they not be able to find buyers, they will have to hold some securities themselves. <!--SR:!2027-05-08,464,390!2027-03-24,433,390-->
- [government auction](../../../../general/government%20auction.md) ::@:: It is an auction held on behalf of a government in which the property to be auctioned is either property owned by the government or property which is sold under the authority of a court of law or a government agency with similar authority. <!--SR:!2027-03-25,432,390!2026-09-26,284,370-->
  - government auction / government bonds ::@:: The government holds periodic _auctions_ to sell bonds to _primary dealers_ \(PD\), which are usually large financial institutions. They are _obligated_ to bid a certain amount to stabilize bond issuance. <p> Small investors can only buy said bonds _directly_ via PDs or _indirectly_ from secondary markets. <!--SR:!2027-04-18,451,390!2027-04-10,443,390-->
- [secondary market](../../../../general/secondary%20market.md) ::@:: It is the financial market in which previously issued financial instruments such as stock, bonds, options, and futures are bought and sold. <!--SR:!2027-05-24,482,390!2027-05-10,466,390-->
  - secondary market / vs. primary market ::@:: The initial sale of the security by the issuer to a purchaser, who pays proceeds to the issuer, is the primary market. All sales after the initial sale of the security are sales in the secondary market. <!--SR:!2027-04-24,457,390!2027-04-27,455,390-->
- [market maker](../../../../general/market%20marker.md) ::@:: It is a company or an individual that quotes both a buy and a sell price in a tradable asset held in inventory, hoping to make a profit on the difference, which is called the _bid–ask spread_ or _turn_. <!--SR:!2027-03-30,437,390!2027-04-04,437,387-->
  - market maker / terminology ::@:: liquidity: trading opportunities \(in this context\) <br/> liquidity provider: provides trading opportunities <br/> liquidity taker: consumes trading opportunities <!--SR:!2027-05-13,471,390!2027-04-12,445,390-->
  - market maker / example ::@:: For a simple example, consider trading a stock. If there are no market makers, both parties of a trade need to state their intention at the same time and place for trades to occur. <p> Market makers allow trading to occur without both parties stating their intention at the same time and place. <!--SR:!2027-04-29,455,390!2027-03-23,432,390-->
- [exchange](../../../../general/exchange%20(organized%20market).md) ::@:: It is an organized market where people can buy and sell financial instruments, such as tradable securities, commodities, foreign exchange and derivative contracts. <!--SR:!2027-03-05,417,390!2027-03-13,423,390-->
- stock exchange
  - stock exchange / examples ::@:: HKEX, LSE, NYSE, Nasdaq, etc. <p> \(__this course__: typically stocks\) <!--SR:!2027-04-23,456,390!2027-04-12,445,390-->
- [over-the-counter](../../../../general/over-the-counter%20(finance).md) \(OTC\) ::@:: It is done directly between two parties, without the supervision of an exchange. It is contrasted with exchange trading, which occurs via exchanges. <p> In an OTC trade, the price is not necessarily publicly disclosed. <!--SR:!2027-03-15,425,390!2027-04-23,456,390-->
  - over-the-counter / characteristics ::@:: customized contracts, exotic contracts, mediated by dealers, not a place <!--SR:!2027-03-14,423,387!2026-11-06,306,370-->
  - over-the-counter / disadvantages ::@:: counterparty risk, less liquid, opaque, systemic risk \(if major dealers are distressed\) <!--SR:!2027-04-24,457,390!2027-04-10,443,387-->
  - over-the-counter / examples ::@:: exotic options, forwards, structured products, swaps <p> \(__this course__: typically bonds\) <!--SR:!2026-08-19,253,367!2027-04-13,446,390-->
- stock exchange
  - stock exchange / competition ::@:: There are multiple exchanges in the United States. This competition benefits users. <p> However, there are unintended consequences, e.g. enabling high-frequency trading \(HFT\), enabling latency arbitrage, etc. <!--SR:!2026-10-01,285,370!2027-04-25,458,390-->
- order book
- order
  - order / types
  - order / limit order
- order book
  - order book / limit order book ::@:: It accumulates limit orders. They are removed when a matching trade is executed or canceled by the user. <!--SR:!2027-04-28,456,390!2027-04-08,441,390-->
- order
  - order / limit order
    - order / limit order / priority ::@:: Better prices are matched and executed first. Then orders that are placed earlier are matched and executed first. <!--SR:!2027-03-14,424,390!2027-04-15,448,390-->
    - order / limit order / liquidity ::@:: In general, by stating the intentions of traders, liquidity is provided. <p> But traders can also take away liquidity by placing a limit order that can be satisfied by orders in the limit book when it is received, which are called _marketable_ limit orders. <!--SR:!2027-03-22,431,390!2027-04-28,461,390-->
  - order / market order
    - order / market order / limit order ::@:: Can be treated as a limit order with negative infinite ask price \(ensures instant sale if there are enough buyers\) or positive infinite bid price \(ensures instant purchase if there are enough sellers\). <!--SR:!2026-12-02,332,370!2027-04-03,436,387-->
    - order / market order / liquidity ::@:: It takes away liquidity by consuming orders in the limit order book. <!--SR:!2027-04-20,453,390!2027-04-22,455,390-->
- [bid–ask spread](../../../../general/bid–ask%20spread.md) ::@:: A type of _transaction cost_. It is the difference between the prices quoted \(either by a single market maker or in a limit order book\) for an immediate sale \(ask\) and an immediate purchase \(bid\). <!--SR:!2027-04-27,460,390!2027-04-05,438,387-->
  - bid–ask spread / bid price ::@:: The price a market dealer or maker is willing to buy. Investor's \(your\) sale price. Usually lower than the ask price. <!--SR:!2027-03-18,428,390!2026-04-19,139,350-->
  - bid–ask spread / ask price ::@:: The price a market dealer or maker is willing to sell. Investor's \(your\) purchase price. Usually higher than the bid price. <!--SR:!2027-05-05,463,390!2027-04-15,448,387-->
  - bid–ask spread / liquidity ::@:: The size of the bid–ask spread in a security is one measure of the liquidity of the market and of the size of the transaction cost. If the spread is 0 then it is a frictionless asset. <!--SR:!2027-05-17,475,390!2027-03-29,436,390-->
  - bid–ask spread / midpoint ::@:: $$\frac {\text{bid price} + \text{ask price} } 2$$ <p> Sometimes, it may be used as the fair price of an asset. <!--SR:!2027-04-16,449,390!2027-05-16,474,390-->
  - bid–ask spread / market depth ::@:: It is the quantity offered at a specific price based on the limit order book. <p> It must increase as the price moves away from the midpoint \(in either direction\), as the number of executable limit orders are _accumulated_. <!--SR:!2027-05-20,476,390!2027-04-17,450,390-->
  - bid–ask spread / quoted price ::@:: Typically the quoted price is the last execution price, which is neither the bid price, ask price, nor midpoint price. <!--SR:!2027-05-07,463,390!2027-03-10,421,390-->
- order
  - order / conditional order
  - order / stop order ::@:: It is an order to buy or sell a stock once the price of the stock reaches a specified price, known as the __stop price__. When the stop price is reached, a stop order becomes a market order.  <p> \(__this course__: If the stop order is triggered, it becomes either a market order or limit order.\) <!--SR:!2027-04-06,439,390!2027-04-18,451,390-->
    - order / stop order / buy-stop order ::@:: A buy-stop order is entered at a stop price above the current market price. Investors generally use a buy-stop order to limit a loss, or to protect a profit, on a stock that they have sold short. <!--SR:!2026-11-09,309,370!2027-05-13,469,390-->
    - order / stop order / sell-stop order ::@:: A sell-stop order is entered at a stop price below the current market price. Investors generally use a sell-stop order to limit a loss or to protect a profit on a stock that they own. <!--SR:!2026-06-04,187,350!2027-05-12,470,390-->
    - order / stop order / note ::@:: A buy-stop order waits for the price to go _above_ \(excluding _equal to_\), not _below or equal to_ the stop price to buy. Otherwise, it would be a buy-limit order instead. The same goes for sell-stop order. <p> \(__this course__: If the stop order is triggered, it becomes either a market order or limit order.\) <!--SR:!2027-03-22,431,390!2026-10-09,295,370-->
- order book
  - order book / limit order book
    - order book / limit order book / features ::@:: discriminatory double auction, _ex-ante_ commitment \(trade after placing order\), price—time priority, transparency regime <!--SR:!2027-03-04,416,390!2026-12-13,343,370-->
      - order book / limit order book / features / discriminatory double auction ::@:: It is possible that there is no unique market-clearing price \(in which demand equals supply\). <!--SR:!2027-04-11,444,390!2027-03-29,436,390-->
      - order book / limit order book / features / price—time priority ::@:: Better prices are matched first. If tied, earlier orders are matched first. <p> It is a structural flow that may be exploited by high-frequency trading. <!--SR:!2027-04-17,450,390!2027-05-21,479,390-->
      - order book / limit order book / features / transparency regime ::@:: Orders may have different transparency \(not visible on the limit order book\), e.g. a stop order may only be placed when the price reaches a certain threshold. <!--SR:!2027-05-28,484,390!2027-04-08,441,387-->
- [New York Stock Exchange](../../../../general/New%20York%20Stock%20Exchange.md) \(NYSE\) ::@:: It is an American stock exchange in the Financial District of Lower Manhattan in New York City. It is the largest stock exchange in the world by market capitalization, exceeding \$25 trillion in July 2024. <!--SR:!2027-04-26,459,390!2027-03-30,437,390-->
  - New York Stock Exchange / mechanism ::@:: _auction market_/double auction, mostly electronic, retained physical trading floor <!--SR:!2027-05-04,462,387!2027-03-17,427,390-->
    - New York Stock Exchange / mechanism / details ::@:: Brokers, dealers, and traders can place orders directly or via \(physical\) floor traders indirectly. <p> Each stock has a designated market maker \(DMM\) as an auctioneer, which come from large institutions. They enhance trading and does not trade for profits. They interact with \(physical\) floor traders. <!--SR:!2027-03-05,417,390!2027-04-13,446,390-->
- [Nasdaq](../../../../general/Nasdaq.md) ::@:: It is an American stock exchange based in New York City. It is the most active stock trading venue in the U.S. by volume, and ranked second on the list of stock exchanges by market capitalization of shares traded, behind the New York Stock Exchange. <!--SR:!2027-03-23,432,390!2027-03-11,422,390-->
  - Nasdaq / full name ::@:: National Association of Securities Dealers Automated Quotations <!--SR:!2027-05-11,467,390!2027-05-17,473,390-->
  - Nasdaq / mechanism ::@:: fully electronic, _dealer market_ <!--SR:!2027-03-18,427,387!2027-05-07,465,390-->
    - Nasdaq / mechanism / details ::@:: As a _dealer market_, dealers or market makers directly participate in trading. They are registered firms trading for its own account \(principal traders\) and/or customer accounts \(agency traders\). They display their own trading interests and/or their customers' limit orders. <p> _Order entry firms_ are brokers, dealers, or trading systems that brings _additional_ orders. <!--SR:!2027-03-25,432,390!2027-04-03,436,387-->
- alternative trading system
- dark pool
  - dark pool / characteristics ::@:: Your order is _not_ displayed. Typically, the midpoint of regular exchanges is used to match and execute trades \(but other references are possible\). <p> You potentially get better execution price but there is _execution risk_. <!--SR:!2027-04-16,449,390!2027-03-13,423,390-->
- market microstructure
- [margin](../../../../general/margin%20(finance).md) ::@:: It is the collateral that a holder of a financial instrument has to deposit with a counterparty \(most often a broker or an exchange\) to cover some or all of the credit risk the holder poses for the counterparty. <!--SR:!2026-08-25,257,370!2027-04-28,454,387-->
  - margin / risks ::@::  This risk can arise if the holder has done any of the following: <p> - Borrowed cash from the counterparty to buy financial instruments, <br/> - Borrowed financial instruments to sell them short, <br/> - Entered into a derivative contract. <!--SR:!2027-03-24,431,390!2027-04-09,442,387-->
  - margin / margin buying ::@:: It refers to the buying of securities with cash borrowed from a broker, using the bought securities as collateral. This has the effect of magnifying any profit or loss made on the securities. The securities serve as collateral for the loan. <!--SR:!2027-05-09,465,390!2027-03-17,427,390-->
    - margin / margin buying / net value ::@:: The net value—the difference between the value of the securities and the loan—is initially equal to the amount of one's own cash used. <!--SR:!2026-10-27,296,367!2027-03-26,433,390-->
    - margin / margin buying / margin ::@:: $$\text{margin} = \frac {\text{account equity} } {\text{account market value} } \times 100\% \,,$$ where account market value is the market value of the assets \(i.e. cash or securities you have put in as collateral, and securities you have bought using the loan\) in your account and account equity is the account market value subtracted by the loan amount. <!--SR:!2027-08-15,529,350!2026-03-15,123,330-->
    - margin / margin buying / interpretation ::@:: Indeed, when the security market value rises, the margin increases, and vice versa. This is because both account equity and account market value will increase by the same rise. <!--SR:!2027-05-21,477,390!2027-05-11,469,387-->
  - margin / initial margin ::@:: Required margin at the beginning of investment.  When a _margin call_ occurs, you need to restore the margin to this rather than the maintenance margin. <!--SR:!2027-03-09,420,390!2027-05-22,480,390-->
  - margin / maintenance margin ::@:: Minimum required margin during an investment. If the margin falls below this, a _margin call_ occurs. You either deliver more money to the broker or sell some securities in the account to restore the margin to _initial_ \(not _maintenance_\) margin. The motivation is to _improve_ the likelihood of _repayment_. <!--SR:!2027-03-01,413,387!2027-05-20,478,390-->
  - margin / leverage ::@:: $$\text{leverage} = 1 / \text{margin} \,,$$ which is the _multiplier_ any return on investment \(_percentage_ gains or losses relative to your own investment, which excludes the loan or loan security\) are magnified by. <p> For example, if margin is 100%, then leverage is 1, i.e. no leverage. If margin is 50%, then leverage is 2, i.e. any _percentage_ gains or losses are magnified by 2 times. <!--SR:!2027-04-04,437,387!2027-05-20,476,390-->
  - margin / short selling ::@:: It refers to the selling of securities that the trader does not own, borrowing them from a broker, and using the cash as collateral. This has the effect of reversing any profit or loss made on the securities. The initial cash deposited by the trader, together with the amount obtained from the sale, serve as collateral for the loan. <!--SR:!2027-04-16,449,390!2027-05-01,457,390-->
    - margin / short selling / net value ::@:: The net value—the difference between the cash amount and the value of loan security—is initially equal to the amount of one's own cash used. <!--SR:!2027-03-21,430,390!2027-04-30,463,390-->
    - margin / short selling / margin ::@:: $$\text{margin} = \frac {\text{account equity} } {\text{loan security market value} } \times 100\% \,,$$ where account equity is the market value of the assets \(i.e. cash or securities you have put in as collateral, and cash you have obtained by selling the loan security\) in your account subtracted by the market value of the loan security. <!--SR:!2026-07-13,205,347!2026-04-01,126,327-->
    - margin / short selling / interpretation ::@:: Indeed, when the loan security market value rises, the margin decreases, and vice versa. This is because account equity decreases by the rise and loan security market value increases by the rise. <!--SR:!2027-05-18,474,390!2026-07-17,212,350-->

## week 2 lecture

- datetime: 2025-09-09T15:00:00+08:00/2025-09-09T16:20:00+08:00, PT1H20M
- topic: interest rate; compound interest; holding period return; expected return; variance; normal distribution
- [interest rate](../../../../general/interest%20rate.md) ::@:: It is the amount of interest due per period, as a proportion of the amount lent, deposited, or borrowed. Interest rate periods are ordinarily a year and are often annualized when not. <!--SR:!2026-04-25,138,405!2026-04-21,135,405-->
  - interest rate / lending ::@:: It is the cost a borrower pays to a lender, expressed as a percentage of the loan amount (e.g., borrowing \$1&nbsp;000 at 10% yields a \$100 interest payment). <!--SR:!2026-04-19,133,405!2026-04-19,133,405-->
  - interest rate / nominal rate, real rate ::@:: Rates can be quoted nominally or in real terms; the relationship $1+r = \frac{1+i}{1+\pi}$ links real rate $r$, nominal rate $i$, and inflation $\pi$, which approximates to $r ≈ i - π$ when rates are small and periods are short. <!--SR:!2026-04-25,138,405!2026-04-26,139,405-->
    - interest rate / nominal, real / difference ::@:: Understanding this distinction is essential for comparing returns across time periods and adjusting for purchasing-power changes. <!--SR:!2026-04-23,136,401!2026-04-15,129,405-->
  - interest rate / factors ::@:: money demand and supply, government actions, monetary policy, credit risk, etc. <!--SR:!2026-04-12,127,405!2026-04-13,127,401-->
    - interest rate / factors / money demand and supply ::@:: The supply of loanable funds (household savings funneled through banks) meets the demand from businesses needing capital, forming the core market mechanism. <!--SR:!2026-04-14,129,405!2026-04-07,122,401-->
    - interest rate / factors / government actions ::@:: They—spending levels, bond issuance, and net fiscal position—shift the supply-demand balance by altering how much money is available for borrowing. <!--SR:!2026-04-14,128,401!2026-04-25,138,405-->
    - interest rate / factors / monetary policy ::@:: It and market expectations, particularly anticipated inflation, also influence lenders' required compensation; higher expected inflation typically raises nominal rates. <!--SR:!2026-04-10,125,405!2026-03-06,90,385-->
    - interest rate / factors / credit risk ::@:: It (default probability) adds a further premium: riskier borrowers demand higher yields to compensate lenders. <!--SR:!2026-04-14,129,405!2026-04-16,130,405-->
    - interest rate / factors
  - interest rate / risk-free rate ::@:: It represents the return on an investment with virtually no default risk. It serves as a baseline for evaluating other assets: any excess return above this benchmark is considered a "risk premium". <!--SR:!2026-04-12,127,405!2026-04-21,135,405-->
    - interest rate / risk-free rate / proxies ::@:: Government securities such as US Treasury bills or Secured Overnight Financing Rate \(SOFR\) are common proxies. The choice of risk-free asset matters—using a T-Bill rate versus SOFR can slightly shift the computed premiums and ratios. <!--SR:!2026-04-09,124,405!2026-04-09,124,405-->
  - interest rate / annual percentage rate \(APR\) ::@:: It specifies the nominal yearly rate, but compounding frequency (daily, e.g. bank accounts; monthly, e.g. leases, mortgages; semi-annual, e.g. US bonds) determines the effective yield over a year. <!--SR:!2026-04-08,123,405!2026-04-23,136,401-->
  - interest rate / effective annual rate \(EAR\) ::@:: It is calculated as $(1 + r/n)^n - 1$, where $r$ is APR and $n$ the number of compounding periods per year; \(assuming nonnegative rates\) EAR ≥ APR when compounding occurs more than once annually, and vice versa. <!--SR:!2026-04-07,122,401!2026-04-16,130,405-->
    - interest rate / effective annual rate / example ::@:: A one-year CD with a 5% APR compounded semi-annually yields an EAR of 5.0625%, slightly higher than the stated rate. <!--SR:!2026-04-14,128,401!2026-04-11,126,405-->
- [compound interest](../../../../general/compound%20interest.md) ::@:: It is interest accumulated from a principal sum and previously accumulated interest. It is the result of reinvesting or retaining interest that would otherwise be paid out, or of the accumulation of debts from a borrower. <!--SR:!2026-04-07,122,401!2026-04-27,140,405-->
  - compound interest / continuous compounding ::@:: When the number of compounding periods per year increases without limit, continuous compounding occurs, in which case the effective annual rate approaches an upper limit of _e_<sup>_r_</sup> − 1. Continuous compounding can be regarded as letting the compounding period become infinitesimally small, achieved by taking the [limit](../../../../general/limit%20(mathematics).md) as _n_ goes to [infinity](../../../../general/infinity.md). <!--SR:!2026-04-10,125,405!2026-04-19,133,405-->
    - compound interest / continuous compounding / formula ::@:: The amount after _t_ periods of continuous compounding can be expressed in terms of the initial amount _P_<sub>0</sub> as: $$P(t)=P_{0}e^{rt}.$$ Or, finding the interest rate $r$: $$r = \frac 1 t \ln \left(\frac {P_t} {P_0}\right) \,.$$ <!--SR:!2026-03-21,103,385!2026-04-11,126,405-->
    - compound interest / continuous compounding / use ::@:: It simplifies many formulas (e.g., exponential growth models) and often approximates real-world scenarios for high-frequency financial instruments. <!--SR:!2026-04-25,138,405!2026-04-23,136,405-->
- [holding period return](../../../../general/holding%20period%20return.md) \(HPR\) ::@:: It is the return on an asset or portfolio over the whole period during which it was held. It is one of the simplest and most important measures of investment performance. <!--SR:!2026-04-09,124,405!2026-04-27,140,405-->
  - holding period return / calculation ::@:: HPR is the change in value of an investment, asset or portfolio over a particular period. It is the entire gain or loss, which is the sum [income](../../../../general/income.md) and [capital gains](../../../../general/capital%20gains.md), divided by the value at the beginning of the period. <p> &emsp; __HPR__ = \(End Value - Initial Value\) / Initial Value <p> where the End Value includes income, such as dividends, earned on the investment: $$HPR_{n}\ =\ {\frac {\text{Income}+P_{n+1}-P_{n} }{P_{n} } }$$ where $P_{n}$ is the value at the start of the holding period and $\text{Income}+P_{n+1}$ is the total value at the end of the holding period. <!--SR:!2026-04-26,139,405!2026-04-21,135,405-->
  - holding period return / annualization ::@:: Often, we want the return over an year instead of some arbitrary periods. We assume, whenever you receive a cash flow, you _immediately reinvest_ it into the same asset. <p> Then, for each cash flow in the year, calculate the non-annual returns. Then simply multiply them altogether. <!--SR:!2026-04-17,131,405!2026-04-08,123,405-->
  - holding period return / random variable ::@:: Both price changes and dividend payouts are uncertain; thus HPR is a random variable whose distribution reflects market volatility. <!--SR:!2026-04-11,126,405!2026-04-10,125,405-->
    - holding period return / random variable / estimation ::@:: Time-series data (monthly or yearly returns) allow empirical estimation of expected return and risk measures. <!--SR:!2026-04-27,140,405!2026-04-08,123,401-->
- [expected return](../../../../general/expected%20return.md) ::@:: It  on a financial investment is the expected value of its return (of the profit on the investment). It is a measure of the center of the distribution of the random variable that is the return. <!--SR:!2026-04-27,140,405!2026-04-18,132,405-->
  - expected return / formula ::@:: For a finite set of economic states $\{s_i\}$, each with probability $p(s_i)$ and asset return $r(s_i)$, the expected return is $\mu = \sum p(s_i) r(s_i)$. <!--SR:!2026-04-10,125,405!2026-04-12,127,405-->
  - expected return / interpretation ::@:: This weighted average captures forward-looking investor expectations; higher probabilities for favorable states elevate $\mu$. <!--SR:!2026-04-20,134,405!2026-04-09,124,405-->
  - expected return / formula
    - expected return / formula / example ::@:: Example calculation: a portfolio with returns 20%, 5%, 1% and −10% in four scenarios (probabilities 5%, 40%, 40%, 15%) yields $\mu = 1.9\%$. <!--SR:!2026-04-13,127,401!2026-04-24,137,405-->
  - expected return / moment ::@:: It is the _1st_ moment of return as a random variable. <!--SR:!2026-04-12,127,405!2026-04-10,125,405-->
- [variance](../../../../general/variance.md) ::@:: __Variance__ is the expected value of the squared deviation from the mean of a random variable. It is often represented by $\sigma ^{2}$, $s^{2}$, $\operatorname {Var} (X)$, $V(X)$, or $\mathbb {V} (X)$. <!--SR:!2026-04-08,123,405!2026-04-21,134,405-->
  - variance / discrete random variable ::@:: The variance of a discrete random variable is $$\operatorname{Var}(X) = \sum_{x \in \mathcal X} \left((x - \mu)^2 p(x) \right) \,.$$ This is only defined if the above sum and $\mu$ exists, so it is possible for a discrete random variable to have undefined variance. <!--SR:!2026-04-19,133,405!2026-04-20,134,405-->
  - variance / standard deviation ::@:: Taking the square root gives standard deviation $\sigma$, often called volatility; larger $\sigma$ implies a wider spread of possible outcomes. <!--SR:!2026-04-26,139,405!2026-04-11,126,405-->
  - variance / example ::@:: Example calculation: a portfolio with returns 20%, 5%, 1% and −10% in four scenarios (probabilities 5%, 40%, 40%, 15%) yields $\mu = 1.9\%$. <p> The variance is $0.42\%$ \(alternatively expressed as $0.0042$ or $42\%\%$\) and SD is $6.5\%$, indicating moderate risk relative to the mean. <!--SR:!2026-04-08,123,405!2026-04-13,127,401-->
  - variance / percentage ::@:: When calculating variance or standard deviation, avoid using percentage. If you do use it, note the number for variance is in units of _double_ percent %%, where 1%% = 0.0001. <p> \(__this course__: Show the final answer of variance and SD in percentage.\) <!--SR:!2026-04-15,129,405!2026-04-25,138,405-->
  - variance / moment ::@:: It is the _2nd_ centralized moment of a random variable. <!--SR:!2026-04-21,135,405!2026-04-08,123,405-->
- [normal distribution](../../../../general/normal%20distribution.md) ::@:: The __normal distribution__ or __Gaussian distribution__ is important in statistics and is often used in the natural and social sciences to represent real-valued random variables whose distributions are not known. Their importance is partly due to the central limit theorem. It is denoted $\mathcal N(\mu, \sigma^2)$, where $\mu \in \mathbb R$ is the mean and $\sigma^2 \in \mathbb R_{> 0}$ is the variance. <p> \(When you see $\mathcal N(0, 100)$, do not mistake the 100 as the standard deviation! It is the variance.\) <!--SR:!2026-04-26,139,405!2026-04-13,128,405-->
- [68–95–99.7 rule](../../../../general/68–95–99.7%20rule.md) ::@:: It is a shorthand used to remember the percentage of values that lie within an interval estimate in a normal distribution: approximately 68%, 95%, and 99.7% of the values lie within one, two, and three standard deviations of the mean, respectively. <!--SR:!2026-04-22,135,405!2026-04-09,124,405-->
- variance
  - variance / interpretation ::@:: A lager standard deviation \($\sigma$\) indicates that realized values are more widely dispersed around the mean, meaning outcomes vary considerably from one another. When $\sigma$ equals zero, the outcome is certain and always equal to the mean, so any increase in $\sigma$ makes future returns increasingly unpredictable. <!--SR:!2026-04-24,137,405!2026-04-13,128,405-->
- expected return
  - expected return / estimation ::@:: With observed returns $(r_1,\dots,r_n)$, the sample mean $$\bar{r} = \frac{1}{n}\sum r_t$$ approximates expected return. <p> These plug-in estimators are unbiased for large samples and form the basis for most portfolio calculations. <!--SR:!2026-04-25,138,405!2026-04-09,124,405-->
  - expected return / vs. realized return ::@:: From today's viewpoint, we look at _expected return_ \($\sigma$\) as a forward-looking estimate of the average outcome and assess _risk_ through its variance or standard deviation \($\sigma^2, \sigma$\), assuming we know the return distribution. <p> In contrast, the _realized return_ is what actually occurred, measured after the fact; observing many past returns lets us infer the underlying distribution $p(s)$ and $r(s)$ and then use that empirical knowledge to predict future performance. <!--SR:!2026-03-06,90,381!2026-04-11,126,405-->
- variance
  - variance / estimation ::@:: With observed returns $(r_1,\dots,r_n)$,sample variance $$\hat{\sigma}^2 = \frac{1}{n-1}\sum (r_t - \bar{r})^2$$ estimates risk. \(__this course__: Use $n - 1$ instead of _n_ as the divisor.\) <p> These plug-in estimators are unbiased for large samples and form the basis for most portfolio calculations. <!--SR:!2026-04-25,138,405!2026-04-07,122,401-->

## week 2 lecture 2

- datetime: 2025-09-11T15:00:00+08:00/2025-09-11T16:20:00+08:00, PT1H20M
- status: unscheduled

---

> __<big><big>Announcements and Notes</big></big>__
>
> For those who missed the first class, please take note of the following:
>
> Please read the syllabus and follow the course/email rules outlined there. In particular, if you have questions about exam arrangements or wish to request a recording of the class, __please contact your TA__. If your inquiry is about the class quota and waiting list, __please contact the FINA department__ \(\[redacted\]\).
>
> If you are requesting the recording, make sure to follow the instructions provided in the syllabus or in Lecture Slide #1.
>
> Please note that there will be __no class on Thursday, September 11__, as I will be attending a conference.

## week 3 lecture

- datetime: 2025-09-16T15:00:00+08:00/2025-09-16T16:20:00+08:00, PT1H20M
- topic: skewness; kurtosis; two-moment decision model; risk premium; Sharpe ratio; value at risk
- [skewness](../../../../general/skewness.md) ::@:: It in probability theory and statistics is a measure of the asymmetry of the probability distribution of a real-valued random variable about its mean. <!--SR:!2026-04-07,122,401!2026-04-10,125,405-->
  - skewness / formula ::@:: $$\gamma_1 = \frac{E[(r-\mu)^3]}{\sigma^3}$$ A normal distribution is _symmetric_ and thus has zero skewness. <p> \(__this course__: $\sigma$ uses _unbiased_ estimator.\) <!--SR:!2026-04-25,138,405!2026-04-26,139,405-->
  - skewness / direction ::@:: Intuitively for graphs, a distribution is __left-skewed__ or __negative-skewed__ if _its tail is on the left_, and vice versa for __right-skewed__ or __positive-skewed__. Otherwise, it is __unskewed__. Intuitively for numbers, a distribution is left-skewed if its mean is on the left of (smaller than) its median, and vice versa for right-skewed. Otherwise, it is unskewed. (But actually, said intuition is very very wrong sometimes... See the item below.) <!--SR:!2026-04-22,135,405!2026-04-12,127,405-->
  - [skewness § relationship of mean and median](../../../../general/skewness.md#relationship%20of%20mean%20and%20median) ::@:: The above intuition is _usually_ correct if the distribution is unimodal. But in general, there are no direct relationships between skewness, mean, and median. Furthermore, an unskewed distribution is not necessarily symmetric. But its converse, a symmetric distribution is unskewed, is true. <!--SR:!2026-04-26,139,405!2026-04-18,132,405-->
  - skewness / interpretation ::@:: It indicates asymmetry: positive skew means rare big gains and common small losses; negative skew implies rare large losses and common small gains. <p> These moments help assess whether mean-variance metrics fully capture an asset's risk profile. <!--SR:!2026-04-22,135,405!2026-04-17,131,405-->
  - skewness / moment ::@:: It is the normalized _3rd_ centralized moment of a random variable. <!--SR:!2026-04-11,126,405!2026-04-09,124,401-->
- [kurtosis](../../../../general/kurtosis.md) ::@:: It refers to the degree of tailedness in the probability distribution of a real-valued, random variable in probability theory and statistics. <!--SR:!2026-04-24,137,405!2026-04-07,122,401-->
  - kurtosis / formula ::@:: $$\gamma_2 = \frac{E[(r-\mu)^4]}{\sigma^4}$$ <p> \(__this course__: Use _excess kurtosis_ instead, even though the lecture slides call it simply "_kurtosis_". $\sigma$ uses _unbiased_ estimator.\) <!--SR:!2026-04-20,134,405!2026-04-24,137,405-->
  - kurtosis / excess kurtosis
    - kurtosis / excess kurtosis / formula ::@:: $$\gamma_2 = \frac{E[(r-\mu)^4]}{\sigma^4} - 3$$ A normal distribution has a kurtosis of 3, thus an _excess_ kurtosis of 0. <p> \(__this course__: Use _excess kurtosis_ instead, even though the lecture slides call it simply "_kurtosis_". $\sigma$ uses _unbiased_ estimator.\) <!--SR:!2026-04-12,127,405!2026-04-11,126,405-->
    - kurtosis / excess kurtosis / interpretation ::@:: It gauges tail heaviness; excess kurtosis >&nbsp;0 signals fat tails and higher likelihood of extreme events than a normal distribution predicts. <p> These moments help assess whether mean-variance metrics fully capture an asset's risk profile. <p> For example, positive excess kurtosis means variance/SD _underestimates_ extreme events. <!--SR:!2026-04-13,128,405!2026-04-21,135,405-->
  - kurtosis / moment ::@:: It is the normalized _4th_ centralized moment of a random variable. <!--SR:!2026-04-25,138,405!2026-04-19,133,405-->
- [two-moment decision model](../../../../general/two-moment%20decision%20model.md) ::@:: It is a model that describes or prescribes the process of making decisions in a context in which the decision-maker is faced with random variables whose realizations cannot be known in advance, and in which choices are made based on knowledge of two moments of those random variables. <!--SR:!2026-04-26,139,405!2026-04-11,126,405-->
  - two-moment decision model / names ::@:: mean-variance analysis \(__this course__: uses the name _mean-variance investor_\) <!--SR:!2026-04-26,139,405!2026-04-25,138,405-->
  - two-moment decision model / assumptions ::@:: Investors focus on two attributes: expected return (higher is better) and variance/volatility (lower is preferable). Higher-order moments, e.g. skewness, kurtosis, are _ignored_. <p> The trade-off assumption—"higher return comes with higher risk"—underpins many modern portfolio theories. <!--SR:!2026-04-17,131,405!2026-04-08,123,405-->
  - two-moment decision model / risk aversion ::@:: Risk-averse investors will prefer assets or portfolios that maximize return for a given level of volatility. <!--SR:!2026-04-16,130,405!2026-04-27,140,405-->
  - two-moment decision model / moments ::@:: The two moments are almost always the mean—that is, the expected value, which is the first moment about zero—and the variance, which is the second moment about the mean (or the standard deviation, which is the square root of the variance). <!--SR:!2026-04-21,135,405!2026-04-09,124,401-->
- [risk premium](../../../../general/risk%20premium.md) ::@:: It is a measure of excess return that is required by an individual to compensate being subjected to an increased level of risk. It is used widely in finance and economics, the general definition being the expected risky [return](../../../../general/rate%20of%20return.md) less the [risk-free return](../../../../general/risk-free%20interest%20rate.md), as demonstrated by the formula below. <!--SR:!2026-04-24,137,405!2026-04-20,133,401-->
  - risk premium / formula ::@:: It is used widely in finance and economics, the general definition being the expected risky [return](../../../../general/rate%20of%20return.md) less the [risk-free return](../../../../general/risk-free%20interest%20rate.md), as demonstrated by the formula below. $$\text{risk premium}=E(r)-r_{f} \,,$$ where $E(r)$ is the risky expected rate of return and $r_{f}$ is the risk-free return. <!--SR:!2026-04-27,140,405!2026-04-12,127,405-->
  - risk premium / nature ::@:: The value of this forward-looking \(unobservable\) figure is theoretical and depends on investors' risk assessments rather than observable market prices alone. <!--SR:!2026-04-22,135,405!2026-04-09,124,405-->
- [Sharpe ratio](../../../../general/Sharpe%20ratio.md) ::@:: It measures the performance of an investment such as a security or portfolio compared to a risk-free asset, after adjusting for its risk. <p> It represents the additional amount of return that an investor receives per unit of increase in risk. It provides a unitless measure of efficiency. <!--SR:!2026-04-07,122,401!2026-04-24,137,405-->
  - Sharpe ratio / name ::@:: It was named after William F. Sharpe, who developed it in 1966. He won the 1990 Nobel Memorial Prize in Economic Sciences \(annotation: with Harry Markowitz\). <!--SR:!2026-04-18,132,405!2026-04-14,128,401-->
  - Sharpe ratio / formula ::@:: It is defined as the difference between the returns of the investment and the risk-free return, divided by the standard deviation of the investment returns: $$\text{SR} = \frac{\mu - r_f}{\sigma} \,.$$ <!--SR:!2026-04-25,138,405!2026-04-10,125,405-->
  - Sharpe ratio / interpretation ::@:: A higher SR indicates better compensation per unit of risk; investors compare assets to choose those with superior SRs. <!--SR:!2026-04-23,136,401!2026-04-15,129,405-->
  - Sharpe ratio / example ::@:: With $r_f=4.3\%$, Apple's mean 6.5% and SD 8% give $\text{SR}_{AAPL} = \frac{2.2}{8} ≈ 0.275$; Amazon's mean 7.8% and SD 20% yield $\text{SR}_{AMZN} = \frac{3.5}{20} ≈ 0.175$. Apple offers a higher Sharpe ratio, suggesting better risk-adjusted performance. <!--SR:!2026-04-25,138,405!2026-04-17,131,405-->
- [value at risk](../../../../general/value%20at%20risk.md) \(VaR\) ::@:: It is a measure of the risk of loss of investment/capital. It estimates how much a set of investments might lose (with a given probability), given normal market conditions, in a set time period such as a day. <!--SR:!2026-04-09,124,405!2026-04-07,122,401-->
  - value at risk / definition ::@:: It is the threshold loss value such that there is a specified probability $p$ (commonly 5% or 10%) that actual losses exceed it. <!--SR:!2026-04-22,135,401!2026-04-16,130,405-->
    - value at risk / definition / inversion ::@:: The probability level is about equally often specified as one minus the probability of a VaR break, so that one-day 5% VaR would be called a one-day 95% VaR instead. This generally does not lead to confusion because the probability of VaR breaks is almost always small, certainly less than 50%. <p> \(__this course__: We do not invert _p_.\) <!--SR:!2026-04-26,139,405!2026-04-10,125,401-->
  - value at risk / normal distribution ::@:: Under normality, VaR = $\bar{r} - z_p \hat{\sigma}$, where $z_{0.05} ≈ 1.65$ and $z_{0.01} = 2.33$. <!--SR:!2026-04-16,130,401!2026-04-23,136,405-->
  - value at risk / non-normality ::@:: It does not require the return distribution to be normal. Empirical percentiles (e.g., Excel's `PERCENTILE`) compute VaR directly from data, even if they are non-normal. <!--SR:!2026-04-27,140,405!2026-04-22,135,405-->
  - value at risk / example ::@:: For a portfolio with mean 2% and SD 5%, the 5%/95% VaR is $2 - 1.65 \times 5 ≈ -6.25\%$, meaning there's a 5% chance of losing more than 6.25%. <!--SR:!2026-04-08,123,401!2026-04-19,133,405-->
- interest rate
  - interest rate / risk-free rate
    - interest rate / risk-free rate / historical ::@:: Historical risk-free rates have been slightly positive, reflecting real economic growth and inflation expectations. <!--SR:!2026-04-24,137,405!2026-04-12,127,405-->
  - interest rate / historical ::@:: Riskier assets generally deliver higher average returns to compensate for their volatility; this is observable across asset classes (equities vs bonds). <!--SR:!2026-04-09,124,401!2026-04-23,136,405-->
    - interest rate / historical / correlation ::@:: Returns on risky assets often move together—high correlation arises from shared macroeconomic drivers—yet they tend to be serially uncorrelated \(i.e. uncorrelated over short periods of time\), implying no predictable momentum or reversal patterns over short horizons. <!--SR:!2026-04-11,126,405!2026-04-19,133,405-->

## week 3 lecture 2

- datetime: 2025-09-18T15:00:00+08:00/2025-09-18T16:20:00+08:00, PT1H20M
- topic: expected value; variance; independence; covariance; Pearson correlation coefficient; capital asset pricing model
- [expected value](../../../../general/expected%20value.md) ::@:: The __expected value__ (__population mean__, __first moment__) is a generalization of the weighted average. Informally, the expected value is the mean of the possible values a random variable can take, weighted by the probability of those outcomes. It is commonly denoted $E(X)$. <!--SR:!2026-04-24,137,405!2026-04-21,134,401-->
  - expected value / discrete random variable ::@:: The expected value of a discrete random variable is the weighted average of all possible outcomes $\mathcal X$: $$\operatorname E[X] = \sum_{x \in \mathcal X} x p(x) \,.$$ This is only defined if the sum converges absolutely, so it is possible for a discrete random variable to have a undefined expected value. <p> Also, $$\operatorname E[g(X)] = \sum_{x \in \mathcal X} g(x) p(x) \,.$$ for an arbitrary function $g(x)$. <!--SR:!2026-04-22,135,401!2026-04-15,129,405-->
  - expected value / linearity ::@:: An important property is its linearity: $$\begin{aligned} E(b) & = b \\ E(aX) & = a E(X) \\ E(aX + b) & = a E(x) + b \\ E(aX + bY) & = a E(x) + b E(Y) \,, \end{aligned}$$ where _a_, _b_ are constants and _X_, _Y_ are any random variables (independence is not required). <!--SR:!2026-04-26,139,405!2026-04-24,137,405-->
- variance
  - variance / properties ::@:: A well-known identity relating variance to expected value is $$\operatorname{Var}(X) = \operatorname E\left[X^2\right] - (\operatorname E[X])^2 = \operatorname E\left[X^2\right] - \mu^2 \,.$$ With this identity, the following properties can be proved: $$\begin{aligned} \operatorname{Var}(b) & = 0 \\ \operatorname{Var}(aX) & = a^2 \operatorname{Var}(X) \\ \operatorname{Var}(aX + b) & = a^2 \operatorname{Var}(X) \\ \operatorname{Var}(aX \pm bY) & = a^2 \operatorname{Var}(X) + b^2 \operatorname{Var}(Y) && \text{important, only uses }+ \,, \end{aligned}$$ where _a_, _b_ are constants and _X_, _Y_ are random variables _independent_ from each other, i.e. $P(X \le x, Y \le y) = P(X \le x) P(Y \le y)$. \(Note: There are random variables that are not _independent_ but the above still holds. Such variables are said to be _uncorrelated_.\) <!--SR:!2026-03-18,100,385!2026-04-11,126,405-->
- expected return
  - expected return / estimation
    - expected return / estimation / unbiasedness ::@:: Observing returns $r_1,\dots,r_T$ over $T$ periods, the sample mean $$\bar r = \frac{1}{T}\sum_{t=1}^T r_t$$ satisfies $E[\bar r] = \mu \,.$ Hence the sample mean is a statistically sound estimator of the true expected return. <!--SR:!2026-04-24,137,401!2026-04-20,134,405-->
- variance
  - variance / estimation
    - variance / estimation / unbiasedness ::@:: The usual sample variance estimator uses $1/(T-1)$: $$\hat\sigma^2 = \frac{1}{T-1}\sum_{t=1}^T (r_t-\bar r)^2 \,.$$ This choice cancels the bias that would otherwise arise if we used $1/T$. <!--SR:!2026-04-14,129,405!2026-04-11,126,405-->
- [independence](../../../../general/independence%20(probability%20theory).md) ::@:: Two events _A_ and _B_ are __independent__ iff $$P(A \cap B) = P(A) P(B) \,.$$ otherwise they are __dependent__. <p> Informally speaking, knowing either of the event has happened does not affect the probability of the other. <!--SR:!2026-04-26,139,405!2026-04-07,122,401-->
  - independence / equivalence ::@:: The following statements are equivalent: <ul> <li>_A_ and _B_ are independent.</li> <li>_A_ and _B_<sup>c</sup> are independent.</li> <li>_A_<sup>c</sup> and _B_ are independent.</li> <li>_A_<sup>c</sup> and _B_<sup>c</sup> are independent.</li> </ul> The above can be seen by seeing that the complement of an event is uniquely defined by the event. There is a one-to-one correspondence between a set and its complement (unless the sample space is the empty set, which is impossible for probability). <!--SR:!2026-04-16,130,405!2026-04-08,123,405-->
  - independence / vs. disjoint ::@:: Independent is not disjoint. End of story. <!--SR:!2026-04-13,128,405!2026-04-17,131,405-->
  - independence / pairwise independence ::@:: A finite set of events is __pairwise independent__ iff any two events from the set is _independent_. <p> Pairwise independence does NOT automatically imply _mutual independence_. <!--SR:!2026-04-19,133,405!2026-04-09,124,405-->
  - independence / mutual independence ::@:: A finite set of _n_ events is __mutually independent__ iff any 2 ≤ _k_ ≤ _n_ events from the set is _independent_. For the _independence_ of 2 ≤ _k_ events, this is simply: $$P\left(\bigcap_{i = 1}^k A_k \right) = \prod_{i = 1}^k A_k \,.$$ <p> Mutual independence automatically implies _pairwise independence_. However, note that the above statement must hold for all 2 ≤ _k_ ≤ _n_, not just _k_ = _n_. It is possible to create a sample space such that the set of three events _A_, _B_, and _C_ is independent but no pairs from the three events are _pairwise independent_. <!--SR:!2026-04-18,132,401!2026-03-20,102,385-->
- [joint probability distribution](../../../../general/joint%20probability%20distribution.md) ::@:: Given [random variables](../../../../general/random%20variable.md) $X,Y,\ldots$, that are defined on the same [probability space](../../../../general/probability%20space.md), the __multivariate__ or __joint probability distribution__ for $X,Y,\ldots$ is a [probability distribution](../../../../general/probability%20distribution.md) that gives the probability that each of $X,Y,\ldots$ falls in any particular range or discrete set of values specified for that variable. <!--SR:!2026-04-26,139,405!2026-03-16,99,385-->
  - joint probability distribution / expressions ::@:: The joint probability distribution can be expressed in terms of a joint cumulative distribution function and either in terms of a joint probability density function (in the case of continuous variables) or joint probability mass function (in the case of discrete variables). <!--SR:!2026-04-15,129,405!2026-04-23,136,401-->
  - joint probability distribution / cumulative distribution function \(CDF\) ::@:: It gives the probability that both variables lie within specified ranges; it is analogous to the CDF for one variable but now two-dimensional. <p> If this joint CDF is smooth, its derivative with respect to both variables yields the _joint PDF_, which can be visualized as a surface or contour plot. A two-dimensional histogram approximates the joint PDF by counting samples in each bin; refining the bins (more data) leads closer to the true continuous density. <!--SR:!2026-04-13,128,405!2026-04-07,122,401-->
  - joint probability distribution / marginal distribution ::@:: It gives the probabilities for any one of the variables with no reference to any specific ranges of values for the other variables. <!--SR:!2026-04-17,131,405!2026-04-21,135,405-->
  - joint probability distribution / independence ::@:: For two variables $X,Y$, the joint CDF $F_{XY}(x,y)=P(X \le x,\;Y \le y)$ factorizes into the product of marginals iff $X$ and $Y$ are independent. For multiple variables, they must be _mutually_ independent, and vice versa. <p> Independence can also be checked via the joint PDF: $f_{XY}(x,y)=f_X(x)f_Y(y)$. <!--SR:!2026-04-24,137,405!2026-04-27,140,405-->
- [uncorrelatedness](../../../../general/uncorrelatedness%20(probability%20theory).md) ::@:: In [probability theory](../../../../general/probability%20theory.md) and [statistics](../../../../general/statistics.md), two real-valued [random variables](../../../../general/random%20variable.md), $X$, $Y$, are said to be __uncorrelated__ if their [covariance](../../../../general/covariance.md), $\operatorname {cov} [X,Y]=\operatorname {E} [XY]-\operatorname {E} [X]\operatorname {E} [Y]$, is zero. If two variables are uncorrelated, there is no linear relationship between them. <!--SR:!2026-04-20,133,401!2026-04-15,129,405-->
  - uncorrelatedness / independence ::@:: If $X$ and $Y$ are independent, with finite second moments, then they are uncorrelated. However, not all uncorrelated variables are independent. <p> In particular, joint Gaussianity guarantees that zero covariance actually implies independence, bridging the two separability notions. <!--SR:!2026-04-22,135,405!2026-04-25,138,405-->
- variance
  - variance / weighted sum of variables ::@:: The scaling property and the Bienaymé formula, along with the property of the [covariance](../../../../general/covariance.md) Cov\(_aX_, _bY_\) = _ab_ Cov\(_X_, _Y_\) jointly imply that $$\operatorname {Var} (aX\pm bY)=a^{2}\operatorname {Var} (X)+b^{2}\operatorname {Var} (Y)\pm 2ab\,\operatorname {Cov} (X,Y) \,.$$ <!--SR:!2026-04-23,136,401!2026-04-27,140,405-->
- [covariance](../../../../general/covariance.md) ::@:: It is a measure of the joint variability of two random variables. <!--SR:!2026-04-23,136,401!2026-04-20,134,405-->
  - covariance / correlation coefficient ::@:: The correlation coefficient normalizes the covariance by dividing by the geometric mean of the total variances for the two random variables. <!--SR:!2026-04-08,123,401!2026-04-20,134,405-->
- [sample covariance](../../../../general/sample%20mean%20and%20covariance.md)
  - sample covariance / equation ::@:: Given _N_ samples for each of the random variables _X_ and _Y_, their _sample covariance_ is: $$\operatorname{Cov}(X, Y) = \operatorname{Cov}(Y, X) = \frac 1 {N - 1} \sum_{k = 1}^N (X_k - \overline X) (Y_k - \overline Y) \,.$$ If _X_ and _Y_ are the same random variable _Z_, then it is also the _sample variance_ of _Z_: $$S_{Z, n - 1}^2 = \operatorname{Cov}(Z, Z) = \frac 1 {N - 1} \sum_{k = 1}^N (Z_k - \overline Z)^2 \,.$$ <!--SR:!2026-04-20,134,405!2026-04-12,127,405-->
- [Pearson correlation coefficient](../../../../general/Pearson%20correlation%20coefficient.md) ::@:: It is a correlation coefficient that measures linear correlation between two sets of data. It is the ratio between the covariance of two variables and the product of their standard deviations; thus, it is essentially a normalized measurement of the covariance, such that the result always has a value between −1 and 1. <!--SR:!2026-04-09,124,401!2026-04-09,124,405-->
  - Pearson correlation coefficient / covariance ::@:: $$\operatorname{Corr}(R_i, R_j) = \frac {\operatorname{Cov}(R_i, R_j) } {\operatorname{SD}(R_i) \operatorname{SD}(R_j) } \,,$$ where the standard deviations are sample standard deviations \(for the sample correlation coefficient\). <!--SR:!2026-04-18,132,405!2026-04-08,123,405-->
  - Pearson correlation coefficient / interpretation ::@:: If −1, the two sets of data always move oppositely. If 0, they have no tendency. If 1, they always move together. In between, you can interpolate. <!--SR:!2026-04-16,130,405!2026-04-22,135,405-->
- covariance
  - covariance / linear combinations ::@:: If $X$, $Y$, $W$, and $V$ are real-valued random variables and $a,b,c,d$ are real-valued constants, then the following facts are a consequence of the definition of covariance: $${\begin{aligned}\operatorname {cov} (X,a)&=0\\\operatorname {cov} (X,X)&=\operatorname {var} (X)\\\operatorname {cov} (X,Y)&=\operatorname {cov} (Y,X)\\\operatorname {cov} (aX,bY)&=ab\,\operatorname {cov} (X,Y)\\\operatorname {cov} (X+a,Y+b)&=\operatorname {cov} (X,Y)\\\operatorname {cov} (aX+bY,cW+dV)&=ac\,\operatorname {cov} (X,W)+ad\,\operatorname {cov} (X,V)+bc\,\operatorname {cov} (Y,W)+bd\,\operatorname {cov} (Y,V)\end{aligned} }$$ <!--SR:!2026-04-20,134,405!2026-04-16,130,405-->
    - covariance / linear combinations / variance ::@:: For a sequence $X_{1},\ldots ,X_{n}$ of random variables in real-valued, and constants $a_{1},\ldots ,a_{n}$, we have $$\operatorname {var} \left(\sum _{i=1}^{n}a_{i}X_{i}\right)=\sum _{i=1}^{n}a_{i}^{2}\sigma ^{2}(X_{i})+2\sum _{i,j\,:\,i<j}a_{i}a_{j}\operatorname {cov} (X_{i},X_{j})=\sum _{i,j}{a_{i}a_{j}\operatorname {cov} (X_{i},X_{j})}$$ <p> \(__this course__: This will be useful in modern portfolio theory...\) <!--SR:!2026-04-21,135,405!2026-04-19,133,405-->
- [capital asset pricing model](../../../../general/capital%20asset%20pricing%20model.md) \(CAPM\) ::@:: It is a model used to determine a theoretically appropriate required rate of return of an asset, to make decisions about adding assets to a well-diversified portfolio. <!--SR:!2026-04-27,140,405!2026-04-22,135,401-->
  - capital asset pricing model / equilibrium ::@:: Under CAPM, all traded assets satisfy $$\text{RRR}_i = \frac{\mu_i-r_f}{\sigma_{i,M} / \sigma_M} = \frac{\mu_j-r_f}{\sigma_{j,M} / \sigma_M},\quad \forall i,j = \text{RRR}_j \,,$$ where $\sigma_{i,M}$ is the covariance of asset $i$ with the market. The denominator can be recognized as the _systematic risk_ $\sigma_M \beta_i$ of asset of $i$. <p> This condition forces the market's risk-return ratio to equal that of every individual asset: $$\text{RRR}_M = \frac{\mu_M-r_f}{\sigma_M} = \text{RRR}_i \,.$$ Proof: $$\begin{aligned} \lambda & \equiv \frac {\mu_i - r_f} {\sigma_{i, M} / \sigma_M} \\ \frac \lambda {\sigma_M} \sigma_{i, M} & = \mu_i - r_f \\ \frac \lambda {\sigma_M} \sum_{i = 1}^N w_i \sigma_{i, M} & = \sum_{i = 1}^N w_i(\mu_i - r_f) \\ \frac \lambda {\sigma_M} \operatorname{Cov}\left(\sum_{i = 1}^n w_i r_i, r_M \right) & = \sum_{i = 1}^N w_i \mu_i - r_f \\ \frac \lambda {\sigma_M} \sigma_M^2 & = \mu_M - r_f \\ \lambda & = \frac {\mu_M - r_f} {\sigma_M} \,. \end{aligned}$$ <!--SR:!2026-04-21,135,405!2026-03-16,99,385-->

## week 4 lecture

- datetime: 2025-09-23T15:00:00+08:00/2025-09-23T16:20:00+08:00, PT1H20M
- topic: two-moment decision model; utility function; certainty equivalent; indifference curve; utility maximization; indirect utility
- two-moment decision model
  - two-moment decision model / assumptions
    - two-moment decision model / assumptions / utility ::@:: Investors seek higher mean returns but dislike volatility, measured by standard deviation or variance. They ignore skewness and kurtosis; utility depends solely on μ and σ². <!--SR:!2026-04-12,127,405!2026-04-18,132,401-->
  - two-moment decision model / utility ::@:: Utility is expressed as $$U = \operatorname E[V] - \frac{\gamma}{2}\operatorname{Var}(V) \,,$$ where _V_ represents the end-of-period wealth and $\gamma$ as the risk-aversion parameter. <!--SR:!2026-04-15,129,401!2026-04-16,130,405-->
    - two-moment decision model / utility / initial wealth ::@:: Normalizing the initial wealth $W$ to 1, the function becomes $$U = 1 + \mu - \frac{\gamma}{2}\sigma^2 \,$$ with $\mu$ the expected return and $\sigma^2$ the variance. <p> In general, the function is $$U = W + W \mu - \frac{\gamma}{2} W^2 \sigma^2 \,.$$ <!--SR:!2026-04-22,135,405!2026-04-10,125,405-->
    - two-moment decision model / utility / interpretation ::@:: The function is derived from constant absolute risk aversion \(CARA\) assuming $r$ is normally distributed. <p> It does not capture the real world fully, as it assumes returns are perfectly normal \(ignoring higher moments\), and CARA does not change with wealth level. <!--SR:!2026-04-27,140,405!2026-04-10,125,405-->
  - two-moment decision model / risk-aversion parameter ::@:: γ&nbsp;>&nbsp;0 → risk-averse; γ&nbsp;=&nbsp;0 → risk-neutral; γ&nbsp;<&nbsp;0 → risk-loving. <!--SR:!2026-04-25,138,405!2026-04-22,135,405-->
  - two-moment decision model / risk aversion ::@:: Assuming γ&nbsp;>&nbsp;0. The utility decreases with increasing variance for risk-averse investors, illustrating why higher volatility reduces perceived happiness. <!--SR:!2026-04-17,131,405!2026-04-17,131,405-->
  - two-moment decision model / utility
    - two-moment decision model / utility / example ::@:: Example: Asset A (10% μ, 0.02 σ²). With γ&nbsp;=&nbsp;4, $U = 1 + 0.10 - 2 \times 0.02 = 1.06$; with γ&nbsp;=&nbsp;2, $U = 1 + 0.10 - 1 \times 0.02 = 1.08$. <p> These calculations show how a less risk-averse investor values the same asset more highly due to a lower penalty on variance. <!--SR:!2026-04-17,131,405!2026-04-21,134,401-->
  - two-moment decision model / certainty equivalent \(CE\) ::@:: It is the risk-free return that makes an investor indifferent between a risky asset and a risk-free one. <!--SR:!2026-04-12,127,405!2026-04-21,134,401-->
    - two-moment decision model / certainty equivalent / formula ::@:: $$r_{CE} = \mu - \frac{\gamma}{2} W \sigma^2 \,.$$ The higher the variance, $\gamma$, or $W$, the lower the CE. <!--SR:!2026-03-16,99,385!2026-04-17,131,405-->
    - two-moment decision model / certainty equivalent / example ::@:: Two assets A (μ&nbsp;=&nbsp;30%, σ²&nbsp;=&nbsp;0.15) and B (μ&nbsp;=&nbsp;20%, σ²&nbsp;=&nbsp;0.05); an indifferent investor of initial wealth $W = 1$ has γ&nbsp;=&nbsp;2 and a CE of ≈&nbsp;15%. <!--SR:!2026-04-20,133,401!2026-04-18,132,405-->
  - two-moment decision model / risk aversion
    - two-moment decision model / risk aversion / levels ::@:: - __Hedging__: Reduces future loss by taking offsetting positions or buying insurance; suitable for highly risk-averse individuals. <br/> - __Speculation__: Accepts risk to enhance returns, often via leverage or volatile assets; aligns with moderate risk tolerance. <br/> - __Gambling__: Increases risk without a proportional return increase; characteristic of risk-loving investors who seek higher utility from uncertainty. <!--SR:!2026-04-07,122,401!2026-04-07,122,401-->
- [indifference curve](../../../../general/indifference%20curve.md) ::@:: It connects points on a graph representing different quantities of two goods, points between which a consumer is _indifferent_. <!--SR:!2026-04-26,139,401!2026-04-21,135,405-->
  - indifference curve / interpretation ::@:: That is, any combinations of two products indicated by the curve will provide the consumer with equal levels of utility, and the consumer has no preference for one combination or bundle of goods over a different combination on the same curve. <!--SR:!2026-04-11,126,405!2026-04-07,122,401-->
  - indifference curve / two-moment decision model ::@:: - Plotting _μ_ against _σ_ \(not _σ²_\) for fixed _γ_ yields curves where each point gives the same utility. <p> The constant $W$ can be dropped since it does not affect the indifference curves. <!--SR:!2026-04-27,140,405!2026-04-23,136,405-->
    - indifference curve / two-moment decision model / risk aversion ::@:: For _γ_&nbsp;>&nbsp;0, the curve slopes upward \(and increasingly fast\): higher risk requires a higher expected return to maintain the same happiness level. <!--SR:!2026-04-16,130,405!2026-04-10,125,405-->
    - indifference curve / two-moment decision model / changing _γ_ ::@:: As _γ_ increases, the slope steepens; risk-neutral (_γ_&nbsp;=&nbsp;0) produces a flat line _μ_&nbsp;=&nbsp;constant, while risk-loving (_γ_&nbsp;<&nbsp;0) yields a downward-sloping curve \(and increasingly fast\). <!--SR:!2026-04-18,132,405!2026-04-13,128,405-->
- two-moment decision model
  - two-moment decision model / utility
    - two-moment decision model / utility / maximization ::@:: Consider investing fraction $x$ of $\$W$ in a risky asset $\left(\mu, \sigma^2\right)$ and $1-x$ in a risk-free rate $r_f$. <p> End-of-period wealth: $V = W + Wr_f + Wx(r - r_f)$. Utility: $$U(x) = W + Wr_f + Wx(\mu - r_f) - \tfrac{\gamma}{2}W^2x^2\sigma^2 \,.$$ First-order condition gives the optimal allocation: $$x^* = \frac{\mu - r_f}{W\gamma\sigma^2} \,.$$ <!--SR:!2026-04-13,127,401!2026-04-23,136,405-->
      - two-moment decision model / utility / maximization / interpretation ::@:: Invest more when excess return is higher, volatility lower, or risk aversion weaker. <p> We also see the _absolute_ amount invested into the risky asset is independent of the initial wealth $W$. Doubling $W$ halves $x^*$, which cancels out each others' effect. <!--SR:!2026-04-23,136,405!2026-04-18,132,405-->
    - two-moment decision model / utility / indirect utility ::@:: Substituting $x^* = \frac{\mu - r_f}{W\gamma\sigma^2}$ back yields the _indirect utility_ $$U^* = W + Wr_f + \frac{(\mu - r_f)^2}{2\gamma\sigma^2} \,.$$ The second term represents the utility gain from optimal risky investment; it increases with higher excess return and decreases with greater risk or risk aversion. Notice it does not depend on the initial wealth $W$. <!--SR:!2026-04-25,138,401!2026-04-10,125,405-->

## week 4 lecture 2

- datetime: 2025-09-25T15:00:00+08:00/2025-09-25T16:20:00+08:00, PT1H20M
- topic: portfolio; expected return; variance; covariance; Pearson correlation coefficient; capital allocation line
- [portfolio](../../../../general/portfolio%20(finance).md) ::@:: It is a collection of investments. <!--SR:!2026-04-24,137,405!2026-04-18,132,405-->
  - portfolio / examples ::@:: It is simply a bundle of investments (stocks, bonds, cash, derivatives, etc.). <!--SR:!2026-04-16,130,405!2026-04-27,140,405-->
  - portfolio / motivation ::@:: By holding more than one asset we can diversify away some of the uncertainty that comes from any single investment. This can be shown mathematically. <!--SR:!2026-04-10,125,405!2026-04-23,136,405-->
  - portfolio / expected return ::@:: If two assets A and B have returns $r_A$ and $r_B$, and we allocate fractions $w_A$ and $w_B=1-w_A$, the portfolio return is $$r_p = w_A r_A + w_B r_B \,.$$ The expected return is just a weighted average of the individual means: $$E[r_p]=w_AE[r_A]+w_BE[r_B] = w_A\mu_A + w_B\mu_B \,.$$ <!--SR:!2026-04-19,133,405!2026-04-21,135,405-->
  - portfolio / variance ::@:: Starting from $\operatorname{Var}(r_p)=E[(r_p-\mu_p)^2]$ and substituting the linear combination gives three terms: two "own-variance" terms and one cross-term. The cross-term is the covariance of the two assets, $\sigma_{AB}=\operatorname{Cov}(r_A,r_B)$. Thus $$\operatorname{Var}(r_p)=w_A^2\sigma_A^2 + w_B^2\sigma_B^2 + 2w_Aw_B\sigma_{AB}.$$ <!--SR:!2026-04-23,136,401!2026-04-20,134,405-->
- covariance
  - covariance / interpretation ::@:: If negative, the two sets of data tend to move oppositely. If 0, they have no tendency. If positive, they tend to move together. In between, you can interpolate. <!--SR:!2026-04-14,129,405!2026-04-16,130,405-->
  - covariance / variance ::@:: If we set asset B equal to A, $\sigma_{AA}=\operatorname{Var}(r_A)=\sigma_A^2$, so variance is simply a special case of covariance with itself. <!--SR:!2026-04-21,134,405!2026-04-14,129,405-->
- Pearson correlation coefficient
  - Pearson correlation coefficient / covariance
  - Pearson correlation coefficient / interpretation
  - Pearson correlation coefficient / motivation ::@:: It is a unit-free, normalized form of covariance that divides the raw co-movement by each variable's standard deviation, making it comparable across assets with different scales or units, as it always lies between –1 and +1. <!--SR:!2026-04-14,128,401!2026-04-27,140,405-->
- correlation
  - correlation / using percentages ::@:: When returns are expressed in percentages rather than decimals, every variance or covariance term gets multiplied by $100^2=10~000$ (because each return is scaled up by a factor of 100). <p> Since the standard deviations are also scaled by 100, the extra factor cancels out in the correlation formula $\rho_{AB}=\sigma_{AB}/(\sigma_A\sigma_B)$, so the numerical value of the correlation stays exactly the same; it merely looks larger in intermediate steps but ultimately represents the identical strength and direction of association. <!--SR:!2026-04-19,133,405!2026-04-20,134,405-->
- portfolio
  - portfolio / correlation ::@:: Correlation is defined by dividing covariance by the product of standard deviations: $$\rho_{AB} = \frac{\sigma_{AB} }{\sigma_A\sigma_B} \,.$$ It always lies between –1 and +1; values close to ±1 indicate very strong linear relationships. <!--SR:!2026-04-09,124,401!2026-04-12,127,405-->
    - portfolio / correlation / interpretation ::@:: By choosing assets that are not fully correlated, the covariance term does not add enough variance, reducing overall risk. <p> If you choose assets that are negatively correlated (e.g., $\rho=-0.5,-1$), the covariance term can even reduce overall risk below either asset's individual variance. If you choose assets that are _perfectly_ correlated \(i.e. $\rho=1$\), the _standard deviation_ is simply a _weighted sum_. <!--SR:!2026-04-13,128,405!2026-04-15,129,405-->
- correlation
  - correlation / valid combinations ::@:: For a portfolio to be mathematically sound, the pairwise correlations among all assets must form a _valid correlation matrix_ – that is, one that can arise from actual joint returns and whose associated covariance matrix is _positive-semi-definite_. <p> This simply means that while some asset pairs may exhibit negative correlation, the overall pattern cannot be arbitrarily extreme; the correlations must satisfy consistency conditions. <!--SR:!2026-04-21,135,405!2026-04-23,136,401-->
- portfolio
  - portfolio / complete portfolio \(CP\) ::@:: Allocation decisions are made in two steps: first you select a _risky portfolio_ by weighting the available risky assets (stocks, bonds, etc.) to obtain a mean return $\mu_p$ and volatility $\sigma_p$; second you combine that risky mix with a risk-free asset (or borrow at a fixed rate), creating a _complete portfolio_ whose characteristics are determined by how much weight $y$ is placed on the risky portion versus the safe component. <!--SR:!2026-04-27,140,405!2026-04-22,135,401-->
  - portfolio / risk-free asset ::@:: Combining a risky portfolio $r_p$ with a risk-free rate $r_f$ using weight $y$: $$r_C = y\,r_p + (1-y)\,r_f \,.$$ <p> Expected return: $$E[r_C]=yE[r_p]+(1-y)r_f = r_f + y(\mu_p-r_f) \,.$$ The second term can be interpreted as the _risk premium_ $\mu_p - r_f$ multiplied by _risk exposure_ $y$. Because the risk-free rate is non-random ($\operatorname{Var}(r_f)=0$), portfolio variance becomes simply $\sigma_C^2=y^2\sigma_p^2$; the safe asset does not add any risk \(apart from risk reduction from reducing the risky portion\). <!--SR:!2026-04-16,130,405!2026-04-19,133,405-->
- [capital allocation line](../../../../general/capital%20allocation%20line.md) \(CAL\) ::@:: It is a graph created by investors to measure the risk of risky and risk-free assets. The graph displays the return to be made by taking on a certain level of risk. <!--SR:!2026-04-17,131,405!2026-04-14,128,401-->
  - capital allocation line / complete portfolio ::@:: It is also the straight-line graph that shows how a _complete portfolio_—a mix of a risky bundle and a risk-free asset—moves between expected return and volatility as you change the fraction invested in the risky part. <!--SR:!2026-04-09,124,405!2026-04-18,132,405-->
  - capital allocation line / plotting ::@:: Plotting $(\sigma_C,\mu_C)$ as $y$ varies gives a straight line that starts at $(0,r_f)$ and passes through the risky portfolio point $(\sigma_p,\mu_p)$. <!--SR:!2026-04-12,127,405!2026-04-07,122,401-->
  - capital allocation line / formula ::@:: Starting from a complete portfolio that mixes a risky bundle ($\mu_p,\sigma_p$) with a risk-free rate $r_f$ at weight $y$: $$\mu_C = r_f + y(\mu_p-r_f),\qquad \sigma_C = y\sigma_p \,.$$ Solving the second equation for $y=\sigma_C/\sigma_p$ and substituting into the first gives the CAL equation: $$\boxed{\;\mu_C = r_f + \frac{\mu_p-r_f}{\sigma_p}\,\sigma_C\;}$$ which shows a straight-line relationship between expected return and risk for all possible allocations. <!--SR:!2026-04-08,123,401!2026-04-07,122,401-->
  - capital allocation line / slope ::@:: The slope of this line is the Sharpe ratio: $$\frac{\mu_p-r_f}{\sigma_p} \,,$$ representing the risk-adjusted return per unit of volatility \(_standard deviation_\). <!--SR:!2026-04-08,123,405!2026-04-08,123,405-->
  - capital allocation line / movement ::@:: You can move along the CAL by shifting weight between risky and risk-free assets. <p> When $y>1$ you're _leveraging_—borrowing at a rate $r_B$ higher than $r_f$—which stretches the line outward: the Sharpe ratio generally falls because the extra borrowing cost erodes the risk-adjusted gain, so returns rise at a slower rate as volatility increases. <!--SR:!2026-04-13,127,401!2026-04-17,131,405-->
  - capital allocation line / borrowing ::@:: If you borrow at a higher rate $r_B > r_f$, the effective slope of the CAL for $y>1$ changes: the risk-free return is replaced by $r_B$ in the expected return formula. <!--SR:!2026-04-10,125,405!2026-04-26,139,401-->
    - capital allocation line / borrowing / formula ::@:: When you finance a leveraged position at a borrowing rate $r_B>r_f$, the expected return of the complete portfolio becomes $$\mu_C = y\mu_p - (y - 1) r_B = r_B + y(\mu_p-r_B) \,,$$ while its volatility remains $\sigma_C=y\sigma_p$. <p> Eliminating $y=\sigma_C/\sigma_p$ gives a new slope $(\mu_p-r_B)/\sigma_p$, which is smaller than the original $(\mu_p-r_f)/\sigma_p$; thus the Sharpe ratio—return per unit of risk—drops because borrowing adds cost without reducing variance. <!--SR:!2026-04-22,135,405!2026-04-24,137,405-->
    - capital allocation line / borrowing / example ::@:: A practical example: with \$100 on hand, a risky portfolio yielding 10%, and a bank offering 5% borrowing, borrowing \$600 to buy \$700 worth of risky assets gives 40% \($10\% \times 7 - 5\% \times 6 = 40\%$\) return, illustrating how leverage can amplify gains (but also losses). <!--SR:!2026-04-24,137,405!2026-03-21,103,385-->

## week 5 lecture

- datetime: 2025-09-30T15:00:00+08:00/2025-09-30T16:20:00+08:00, PT1H20M
- topic: modern portfolio theory; portfolio; portfolio weights; portfolio statistics; Markowitz model; portfolio opportunity set; minimumv-variance portfolio; efficient frontier; tangency portfolio
- modern portfolio theory
  - modern portfolio theory / history ::@:: Economist Harry Markowitz introduced MPT in a 1952 paper, for which he was later awarded the 1990 Nobel Memorial Prize in Economic Sciences \(annotation: with William F. Sharpe\); see Markowitz model. <p> \(__this course__: Use _Markowitz portfolio theory_.\) <!--SR:!2026-04-22,135,401!2026-04-23,136,405-->
    - modern portfolio theory / history / paper ::@:: Harry Markowitz's 1952 "Portfolio Selection" paper formalised diversification and optimisation, laying the groundwork for modern investment theory. <!--SR:!2026-04-26,139,405!2026-04-23,136,405-->
- portfolio
  - portfolio / weight ::@:: A portfolio is specified by the set of assets held and their corresponding weight $w_i$. If _not leveraged_, $$w_i=\frac{Q_iP_i}{\sum_{j=1}^n Q_jP_j}$$ where $P_i$ is the price and $Q_i$ the quantity of asset $i$; weights sum to one. If an asset is omitted, its weight is zero. <p> If leveraged, multiply all weights by the leverage, so that the weights sum to the leverage. <!--SR:!2026-04-12,127,405!2026-04-09,124,405-->
    - portfolio / weight / short, leverage ::@:: Leveraged positions allow weights &gt; 1 or negative \(short selling\). <!--SR:!2026-04-07,122,401!2026-04-08,123,401-->
    - portfolio / weight / examples ::@:: - _Example 1:_ A \$100&nbsp;000 account with 200 shares of stock A, 1&nbsp;000 of B and 750 of C yields specific $w_A, w_B, w_C$ once current prices are inserted. <br/> - _Example 2:_ If the same portfolio is financed only with \$50&nbsp;000 (margin = 50%), the weights double \($w_{\text{total} }=2$\). <br/> _Example 3:_ Buying a \$500&nbsp;000 property with 20% down payment gives an initial margin of 20%, so $w_{\text{property} }=5$. <!--SR:!2026-04-25,138,405!2026-04-15,129,405-->
  - portfolio / risks ::@:: Choosing a single “best” stock is impossible because future performance is uncertain; portfolios spread risk across assets, reducing idiosyncratic volatility while preserving exposure to desirable systematic factors. <!--SR:!2026-04-19,133,405!2026-04-25,138,405-->
  - portfolio / statistics ::@:: The goal is to quantify how each asset's expected return $\mu_i$ and covariance $\sigma_{ij}$ shape the overall risk–return profile. <!--SR:!2026-04-14,129,405!2026-04-12,127,405-->
  - portfolio / expected return
    - portfolio / expected return / general ::@:: $$\displaystyle \mu_p=\sum_{i=1}^n w_i\,\mu_i$$ by linearity of expected value. <!--SR:!2026-04-14,128,401!2026-04-21,135,405-->
  - portfolio / variance
    - portfolio / variance / general ::@:: $$\sigma_p^2=\sum_{i=1}^n\sum_{j=1}^n w_iw_j\sigma_{ij} =\sum_{i=1}^n w_i^2\sigma_i^2+\!\!\sum_{i\neq j}\! w_iw_j\rho_{ij}\sigma_i\sigma_j \,,$$ where $\sigma_{ij} = \rho_{ij} \sigma_i \sigma_j$. As $n$ increase, variance terms $\sigma_{ii} = \sigma_{i}^2$ diminishes in contribution while covariance terms become crucial; without considering the latter, the risk of diversification would be misestimated. <!--SR:!2026-04-11,126,405!2026-04-19,133,405-->
- [Markowitz model](../../../../general/Markowitz%20model.md) ::@:: It, put forward by Harry Markowitz in 1952 ─ is a portfolio optimization model; it assists in the selection of the most efficient portfolio by analyzing various possible portfolios of the given securities. <!--SR:!2026-04-18,132,405!2026-03-16,99,385-->
  - Markowitz model / opportunity set \(POS\) ::@:: It is the collection of all attainable $(\mu_p,\sigma_p)$ pairs as weights vary. In two-asset cases it becomes a curve (or line) in mean–variance space; with more assets it turns into a higher-dimensional region. Visualising this helps identify which combinations are feasible. <!--SR:!2026-04-11,126,405!2026-04-09,124,401-->
    - Markowitz model / opportunity set / risky and risk-free assets ::@:: For one risky asset $A$ and the risk-free rate $r_f$: $$\mu_p=(1-w_A)r_f+w_A\mu_A,\qquad \sigma_p^2=w_A^2\sigma_A^2 \,.$$ The resulting set of portfolios is a straight line (the Capital Allocation Line, CAL) from $r_f$ to the risky asset's point $(\sigma_A,\mu_A)$. <!--SR:!2026-04-25,138,405!2026-04-10,125,405-->
    - Markowitz model / opportunity set / two risky assets ::@:: With risky assets A and B: $$\mu_p=w_A\mu_A+(1-w_A)\mu_B ,\qquad \sigma_p^2=w_A^2\sigma_A^2+(1-w_A)^2\sigma_B^2+2w_A(1-w_A)\rho_{AB}\sigma_A\sigma_B \,.$$ The shape of the POS depends on $\rho_{AB}$. <!--SR:!2026-04-24,137,405!2026-04-10,125,405-->
      - Markowitz model / opportunity set / two risky assets / perfectly positive ::@:: When $\rho_{AB}=1$, the covariance equals the product of the individual volatilities, so the portfolio variance reduces to $(w_A\sigma_A+(1-w_A)\sigma_B)^2$. <p> Consequently every feasible mix lies on a straight line in mean–variance space that connects the two asset points $K_A=(\sigma_A,\mu_A)$ and $K_B=(\sigma_B,\mu_B)$. This linearity means no diversification benefit is possible; all portfolios are simply weighted averages of the two risky assets. <!--SR:!2026-04-26,139,405!2026-04-07,122,401-->
      - Markowitz model / opportunity set / two risky assets / perfectly negative ::@:: With $\rho_{AB}=-1$, the covariance term becomes $-\sigma_A\sigma_B$, and the portfolio variance reduces to $(w_A\sigma_A-(1-w_A)\sigma_B)^2$. <p> By choosing weights such that $w_A = w_{\text{RF} } =\frac{\sigma_B}{\sigma_A+\sigma_B}$ (and $w_B=1-w_A$), the portfolio variance collapses to zero, yielding a risk-free combination of two otherwise risky assets. The opportunity set therefore degenerates to a triangle \(omitting the line segment $K_A K_B$\) formed by $K_A$, $K_B$, and a single point at $K_0 = (0,\mu_{\text{RF} })$, where $\mu_{\text{RF} }$ is the weighted average return that matches the risk-free rate. <!--SR:!2026-04-18,132,405!2026-04-25,138,405-->
      - Markowitz model / opportunity set / two risky assets / intermediate ::@:: When $-1<\rho_{AB}<1$, the covariance lies strictly between its extreme values, and the resulting $(\mu_p,\sigma_p)$ pairs trace a concave conic segment. <p> This curve is bounded inside the triangle formed by the risk-free point $K_0$ and the two asset points $K_A$ and $K_B$, reflecting partial diversification: portfolios achieve lower variance than the line segment but cannot reach zero unless $\rho=-1$. The efficient frontier emerges as the upper boundary of this conic, offering the optimal trade-off between return and risk. <!--SR:!2026-04-08,123,405!2026-04-08,123,405-->
    - Markowitz model / opportunity set / margin trading, short selling ::@:: With margin trading and short selling, the portfolio opportunity set expands beyond the two asset points $K_A$ and $K_B$. Investors are no longer restricted to weights between 0 and 1; they can hold leveraged positions ($w_A>1$) or borrow/short securities ($w_A<0$). This broader range allows the efficient frontier to include portfolios that exploit leverage or short exposure for potentially higher risk-adjusted returns. <!--SR:!2026-04-22,135,401!2026-03-07,91,385-->
  - Markowitz model / minimum-variance portfolio \(MVP\) ::@:: For any $w_A,w_B=1-w_A$ and $\sigma_A,\sigma_B$, the variance is $$\sigma_p^2 = w_A^2\sigma_A^2 + w_B^2\sigma_B^2 + 2w_Aw_B\rho_{AB}\,\sigma_A\sigma_B \,.$$ By setting its derivative with respect to $w_A$ to zero, the weight that minimizes risk is $$w_{\min}=\frac{\sigma_B^2-\rho_{AB}\sigma_A\sigma_B}{\sigma_A^2+\sigma_B^2-2\rho_{AB}\sigma_A\sigma_B} \,,$$ which shifts toward the lower-volatility asset as correlation rises. <!--SR:!2027-01-28,353,381!2026-04-11,126,405-->
  - Markowitz model / efficient frontier \(EF\) ::@:: It is the upper part of the POS above the minimum-variance point. An investor prefers portfolios on the EF because, for a given level of expected return, they offer the lowest possible variance, and conversely, for a given variance, they provide the highest return. <!--SR:!2026-04-14,129,405!2026-04-20,134,405-->
    - Markowitz model / efficient frontier / lower section ::@:: The lower section of the portfolio opportunity set is discarded because every point there is _dominated_—it delivers either a higher variance for the same expected return or a lower return for the same variance, so no rational mean-variance investor would choose it. Consequently, only the upper, non-dominated segment (the efficient frontier) remains relevant for portfolio selection. <!--SR:!2026-04-14,128,401!2026-04-14,128,401-->
  - Markowitz model / capital asset line \(CAL\) ::@:: A complete portfolio mixing a risky mix $p$ \(with $\mu_p,\sigma_p$\) and the risk-free asset yields: $$\mu_C=r_f+y(\mu_p-r_f),\qquad \sigma_C=y\,\sigma_p \,,$$ where $y$ is the fraction invested in the risky mix. Eliminating $y$ gives the CAL equation: $$\mu_C=r_f+\frac{\mu_p-r_f}{\sigma_p}\,\sigma_C \,.$$ The slope of this line equals the Sharpe ratio of portfolio $p$. <!--SR:!2026-04-16,130,401!2026-04-20,134,405-->
  - Markowitz model / tangency portfolio ::@:: The optimal risky portfolio is the unique point on the EF where the CAL is tangent. This maximises the Sharpe ratio, i.e., the reward-per-unit-risk measure $(\mu_p-r_f)/\sigma_p$. For mean-variance investors under _some conditions_, allocating funds between the risk-free asset and this tangency portfolio achieves the best possible trade-off. <!--SR:!2026-04-14,128,401!2026-04-11,126,405-->
    - Markowitz model / tangency portfolio / conditions ::@:: If the risk-aversion parameter is positive \(risk averse\), then the CAL of the tangency portfolio contains an unique point that is consistent with MV utility maximization. <!--SR:!2026-04-26,139,405!2026-04-09,124,405-->
    - Markowitz model / tangency portfolio / identification ::@:: 1. Compute the POS using the weight-dependent formulas. <br/> 2. Identify the EF (upper envelope of the POS) by solving the minimum-variance problem. <br/> 3. Draw the CAL from $r_f$ to any point on the EF; increase slope until it just touches the EF to maximize Sharpe ratio. <br/> 4. The touching point is the tangency portfolio; its weights $w_A^*$ and $1-w_A^*$ are the optimal risky allocation. <!--SR:!2026-04-20,134,405!2026-04-27,140,405-->

## week 5 lecture 2

- datetime: 2025-10-02T15:00:00+08:00/2025-10-02T16:20:00+08:00, PT1H20M
- topic: multiple risk assets; diversification; portfolio frontier; two-fund theorem; multiple tangency portfolios
- portfolio
  - portfolio / multiple risky assets ::@:: A single-asset or two-asset view is limited; with $n\ge3$ risky securities we can exploit diversification, reduce idiosyncratic risk, and construct portfolios that better match investors' preferences. <!--SR:!2026-03-19,101,385!2026-04-13,127,401-->
  - portfolio / statistics
  - portfolio / expected return
  - portfolio / variance
  - portfolio / correlation ::@:: Combining assets with correlation $\rho<1$ always lowers portfolio volatility below a weighted average of individual _standard deviations_. The exact reduction depends on both the magnitude of $\rho$ and the disparity between $\sigma_A$ and $\sigma_B$. <p> _Example_: Two assets A and B each have SD $\sigma=35\%$. For any weight $w\in(0,1)$, the portfolio SD satisfies $$\begin{aligned} \sigma_p & = \sqrt{w^2\sigma^2+(1-w)^2\sigma^2+2w(1-w)\rho\sigma^2} \\ & < \sqrt{w^2 \sigma^2 + (1 - w)^2 \sigma^2 + 2w(1 - w) \sigma^2} \\ & = \sqrt{(w\sigma + (1 - w)\sigma)^2} \\ & = \sigma \,, \end{aligned}$$ when $\rho<1$. <!--SR:!2026-04-24,137,405!2026-04-24,137,405-->
  - portfolio / variance
    - portfolio / variance / matrix form ::@:: For $n$ assets, $\mathbf\Sigma$ is an $n\times n$ symmetric matrix of _covariances_ \(_variance—covariance matrix_\); portfolio variance can be written compactly as $$\mathbf{w}^\top \mathbf\Sigma \mathbf{w} \,.$$ <!--SR:!2026-04-19,133,405!2026-03-16,99,385-->
  - portfolio / risks
    - portfolio / risks / systematic risks ::@:: Common to many stocks; cannot be diversified away (e.g., market, interest-rate shocks). <p> Investors earn compensation only for bearing systematic risk. <!--SR:!2026-04-20,134,405!2026-04-22,135,405-->
    - portfolio / risks / idiosyncratic risks ::@:: Specific to a single firm or industry; diversifiable through portfolio construction. <p> Investors earn compensation only for bearing systematic risk. <!--SR:!2026-04-21,134,401!2026-04-15,129,401-->
- Markowitz model
  - Markowitz model / diversification ::@:: For an equally-weighted portfolio, the variance simplifies to $$\sigma_p^2 = \frac{1}{n}\bar\sigma^2 + \frac{n(n-1)}{n^2}\overline{\text{Cov} } \,,$$ where $\bar\sigma^2$ and $\overline{\text{Cov} }$ are average variance and covariance. <p> As $n\to\infty$, the first term vanishes, leaving only the systematic component: $$\lim_{n\to\infty} \frac {n(n - 1)} {n^2} \overline{\text{Cov} } = \overline{\text{Cov} } \,.$$ Thus idiosyncratic risk is eliminated; only systematic risk remains. <!--SR:!2026-04-10,125,405!2026-04-20,133,401-->
  - portfolio / risks
    - portfolio / risks / total risks ::@:: It is the sum of systematic risks and idiosyncratic risks. <!--SR:!2026-04-23,136,401!2026-04-21,134,405-->
    - portfolio / risks / systematic risks
      - portfolio / risks / systematic risks / examples ::@:: It in an airline portfolio comprises company-specific events such as aircraft failures, employee strikes, or flight bans that affect only the airlines involved. <!--SR:!2026-04-08,123,405!2026-04-27,140,405-->
    - portfolio / risks / idiosyncratic risks
      - portfolio / risks / idiosyncratic risks / examples ::@:: It encompasses macro-level shocks—interest-rate changes, financial crises, pandemics, wars, and natural disasters—that impact the entire market regardless of individual firm characteristics. <!--SR:!2026-04-10,125,401!2026-04-17,131,401-->
  - Markowitz model / portfolio frontier ::@:: It is the collection of all minimum-variance portfolios \(MVPs\), including the part below the minimum-variance point. <!--SR:!2026-04-17,131,405!2026-04-21,135,405-->
    - Markowitz model / portfolio frontier / formulation ::@:: Minimize portfolio variance $\mathbf{w}^\top\mathbf\Sigma\mathbf{w}$ subject to $\sum w_i=1$ and $\sum w_i\mu_i=\bar{\mu}_p$. Finding the solution is _not tractable_ in most cases. We will solve it by generating random weights and inspecting the resulting graph. <p> The solution for each target interest $\bar{\mu}_p$ traces the _portfolio frontier_, from which the _efficient frontier_ is extracted by selecting portfolios with highest expected return for a given risk. <!--SR:!2026-04-27,140,405!2027-06-22,474,405-->
  - Markowitz model / opportunity set
    - Markowitz model / opportunity set / Excel method ::@:: With $n=3$ assets, generate random weight vectors $\mathbf{w}$ satisfying $\sum w_i=1$. Compute each portfolio's mean $\mu_p$ and SD $\sigma_p$; plot $(\sigma_p,\mu_p)$ to visualize the cloud of attainable points. <!--SR:!2026-04-22,135,405!2026-04-08,123,405-->
  - Markowitz model / portfolio frontier
    - Markowitz model / portfolio frontier / adding assets ::@:: Adding an extra asset to the investment universe can reduce the portfolio frontier's minimum attainable risk by providing an additional source of diversification. <p> The frontier shifts leftward \(with volatility as _x_-axis and return as _y_-axis\) whenever the new asset's return exhibits lower variance or weak correlation with the existing assets, enabling a more efficient mean-variance trade-off. <!--SR:!2026-04-18,132,405!2027-07-14,496,401-->
  - Markowitz model / efficient frontier
  - Markowitz model / tangency portfolio
    - Markowitz model / tangency portfolio / two-fund theorem ::@:: Every mean–variance efficient investor holds a combination of only two assets: the risk-free bond and the tangency portfolio. <p> The relative weights differ across investors due to differing risk aversion ($\gamma$), but all lie on the same CAL. <!--SR:!2026-04-21,135,405!2026-04-07,122,401-->
    - Markowitz model / tangency portfolio / indifference curve ::@:: For a quadratic _indirect utility_ $U=\mu_C-\frac{\gamma}{2}\sigma_C^2$, each point $(\mu_C,\sigma_C)$ corresponds to an indifference curve: $\mu_C = U + \frac \gamma 2 \sigma_C^2$. <p> The optimal allocation $y^*$ (fraction invested in the tangency portfolio) is found where the utility indifference curve tangent \(solve for the same slope\) to the CAL, yielding $$y^*=\frac{\mu_{p^*}-r_f}{\gamma\sigma_{p^*}^2} \,.$$ This expression matches the MV solution $y^*= (\mu_p-r_f)/(\gamma\sigma_p^2)$, confirming consistency. <!--SR:!2026-04-21,135,405!2026-04-07,122,401-->
    - Markowitz model / tangency portfolio / risk aversion ::@:: High risk aversion ($\gamma$ large) leads to a smaller $y^*$; investors prefer more of the risk-free asset. <p> Low $\gamma$ pushes $y^*$ closer to one, sometimes exceeding it if borrowing is allowed (leveraged position). <!--SR:!2026-04-09,124,405!2026-04-10,125,401-->
    - Markowitz model / tangency portfolio / leverage ::@:: With unrestricted borrowing at rate $r_B \ge r_f$, investors can extend beyond the tangency point along the CAL, creating a _kink_ at $y=1$ \(or just a _straight line_ if $r_B = r_f$\). <!--SR:!2026-04-18,132,405!2026-04-21,135,405-->
      - Markowitz model / tangency portfolio / leverage / forbidden ::@:: If borrowing is prohibited, efficient _complete_ portfolios lie on the portion of the frontier where $0\le y \le 1$, and then extended by the efficient frontier thereafter; risk-tolerant investors are forced to accept lower Sharpe ratio \(SR\) for higher return when $y > 1$. <!--SR:!2026-04-13,127,401!2026-04-23,136,401-->
    - Markowitz model / tangency portfolio / multiple portfolios ::@:: When borrowing $r_B$ and lending $r_f$ rates differ, the _kink_ causes two distinct tangency portfolios arise: one for borrowing $p^*_2$, one for lending $p^*_1$ \(investing at risk-free rate\). <p> The efficient frontier is the combined CAL \(with a kink\), with the part between $p_1^*$ and $p_2^*$ replaced by the efficient frontier. <!--SR:!2026-04-24,137,405!2026-04-26,139,405-->
      - Markowitz model / tangency portfolio / multiple portfolios / risk-adverse ::@:: These investors keep most of their capital in the safe asset or the lending tangency portfolio $p^*_1$, accepting only minimal exposure to risk; they trade off a small increase in expected return for a substantial drop in variance. <!--SR:!2026-04-13,127,401!2026-04-20,134,405-->
      - Markowitz model / tangency portfolio / multiple portfolios / risk-tolerant ::@:: Willing to leverage, these participants borrow at rate $r_B$ and allocate heavily to the borrowing tangency portfolio $p^*_2$, thereby pushing their position above the risk-free line to capture higher returns at the cost of amplified volatility. <!--SR:!2026-04-12,127,405!2026-04-11,126,405-->
      - Markowitz model / tangency portfolio / multiple portfolios / intermediate ::@:: Straddling the two extremes, they blend holdings in both $p^*_1$ and $p^*_2$ along the constrained efficient frontier \(not on CALs containing the risk-free asset, so neither lending at $r_f$ nor borrowing at $r_B$\); their optimal mix is governed by the curvature of the utility indifference curves compared to that of the CAL, which in this context, is the same as the efficient frontier. <!--SR:!2026-04-14,128,401!2026-04-15,129,405-->
    - Markowitz model / tangency portfolio / formulation ::@:: The tangency portfolio, obtained by maximizing the Sharpe ratio $\text{SR}=(\mu_p-r_f)/\sigma_p$, satisfies first-order conditions \(by setting its derivative to zero for $i = 1, \ldots, n$\) of the form $$\mu_i-r_f=\lambda\sum_{j=1}^{n}w_j\sigma_{ij}\,,\qquad i=1,\dots,n \,,$$ which are identical to those derived \(using the same method\) from maximizing a quadratic mean–variance utility $U=(1-\sum w_i)r_f+\sum w_i\mu_i-\tfrac{\gamma}{2}\sigma_p^2$. In the utility problem the Lagrange multiplier $\lambda$ plays the role of the risk-aversion parameter $\gamma$, so the optimal weights that maximize Sharpe ratio also maximize MV utility. Hence, the tangency portfolio is fully consistent with the investor's mean–variance preferences. <!--SR:!2026-03-16,99,385!2026-04-13,128,405-->
      - Markowitz model / tangency portfolio / formulation / Sharpe ratio ::@:: Start from $$\text{SR}(w)=\frac{\sum_i w_i\mu_i-r_f} {\sqrt{\sum_{i}\sum_{j}w_iw_j\sigma_{ij}}}\,,$$ with the only restriction that all capital is invested in risky plus risk-free assets ($1-\!\sum_i w_i$ goes to the risk-free). Differentiate SR with respect to a generic weight $w_k$: $$\frac{\partial \text{SR}}{\partial w_k}=\frac{(\mu_k-r_f)\sigma_p^2-0.5(\sum_i w_i\mu_i-r_f)(\partial\sigma_p^2/\partial w_k)} {\sigma_p^3}=0 \,,$$ where $\sigma_p^2=\sum_{i}\sum_{j}w_iw_j\sigma_{ij}$. Since $\frac{\partial\sigma_p^2}{\partial w_k}=2\sum_{j}w_j\sigma_{kj}$, the first-order condition reduces to $$\mu_k-r_f=\lambda\,\sum_{j=1}^{n}w_j\sigma_{kj}, \qquad \lambda\equiv\frac{\sum_i w_i\mu_i-r_f}{\sigma_p^2}.$$ <!--SR:!2026-03-09,92,381!2026-04-08,123,405-->
      - Markowitz model / tangency portfolio / formulation / utility ::@:: Utility with a risk-free asset is $$U(w)=\Bigl(1-\!\sum_{i}w_i\Bigr)r_f+\sum_{i}w_i\mu_i-\frac{\gamma}{2}\sigma_p^2 \,.$$ Differentiate $U$ w.r.t. $w_k$: $$\frac{\partial U}{\partial w_k}=(\mu_k-r_f)-\frac{\gamma}{2}\,\frac{\partial\sigma_p^2}{\partial w_k}=0 \,.$$ Using the same derivative of variance as above $\frac{\partial\sigma_p^2}{\partial w_k}=2\sum_{j}w_j\sigma_{kj}$ gives a first-order condition for each stock $k$: $$\mu_k-r_f=\gamma\,\sum_{j=1}^{n}w_j\sigma_{kj} \,.$$ <!--SR:!2026-04-15,129,405!2026-04-24,137,405-->
  - Markowitz model / implications ::@:: Diversification dramatically reduces idiosyncratic risk; the more assets, the closer the portfolio SD approaches systematic risk alone. <p> All investors ultimately invest in a _common risky bundle_ (tangency portfolio) plus or minus a risk-free asset; only the mix changes with risk tolerance. <!--SR:!2026-04-20,133,401!2026-04-20,134,405-->
  - Markowitz model / optimize portfolio ::@:: 1. Estimate $\mu_i$, $\sigma_i^2$, and $\sigma_{ij}$. <br/> 2. Solve the minimum-variance problem to trace the efficient frontier. <br/> 3. Identify the tangency point (maximizing Sharpe ratio). There may be multiple if there are multiple rates. <br/> 4. Determine $y^*$ using risk aversion $\gamma$. <br/> 5. Construct the complete portfolio: $C^* = y^*p^* + (1-y^*)r_f = r_f + y^* (p^* - r_f)$. <!--SR:!2026-04-26,139,405!2026-04-20,134,405-->
- assignment: [homework 1](assignments/homework%201/index.md)

## week 6 lecture

- datetime: 2025-10-07T15:00:00+08:00/2025-10-07T16:20:00+08:00, PT1H20M
- status: unscheduled; public holiday: Day after Mid-Autumn Festival

## week 6 lecture 2

- datetime: 2025-10-09T15:00:00+08:00/2025-10-09T16:20:00+08:00, PT1H20M
- topic: Markowitz model; portfolio opportunity set; efficient frontier
- FINA 3103
  - FINA 3013 / [efficient frontier](efficient%20frontier.md)
    - [§ mathematical representation](efficient%20frontier.md#mathematical%20representation)
    - [§ visualization](efficient%20frontier.md#visualization)
    - [§ visualizing opportunity set](efficient%20frontier.md#visualizing%20opportunity%20set)
    - [§ visualizing CAL](efficient%20frontier.md#visualizing%20CAL)
    - [§ visualizing short selling and leverage](efficient%20frontier.md#visualizing%20short%20selling%20and%20leverage)

## week 7 lecture

- datetime: 2025-10-14T15:00:00+08:00/2025-10-14T16:20:00+08:00, PT1H20M
- topic:
- FINA 3103
  - FINA 3103 / [capital asset pricing model](capital%20asset%20pricing%20model.md)
    - [§ history](capital%20asset%20pricing%20model.md#history)
    - [§ background](capital%20asset%20pricing%20model.md#background)  
    - [§ market portfolio](capital%20asset%20pricing%20model.md#market%20portfolio)  
    - [§ tangent portfolio](capital%20asset%20pricing%20model.md#tangent%20portfolio)  
    - [§ assumptions](capital%20asset%20pricing%20model.md#assumptions)  
    - [§ derivation](capital%20asset%20pricing%20model.md#derivation)  
    - [§ CAPM equation](capital%20asset%20pricing%20model.md#CAPM%20equation)  
    - [§ beta](capital%20asset%20pricing%20model.md#beta)  
    - [§ portfolio CAPM](capital%20asset%20pricing%20model.md#portfolio%20CAPM)  
    - [§ security market line](capital%20asset%20pricing%20model.md#security%20market%20line)  
    - [§ empirical testing](capital%20asset%20pricing%20model.md#empirical%20testing)  
    - [§ alpha](capital%20asset%20pricing%20model.md#alpha)  
    - [§ sigma](capital%20asset%20pricing%20model.md#sigma)  
    - [§ validity](capital%20asset%20pricing%20model.md#validity)  
    - [§ advantages and disadvantages](capital%20asset%20pricing%20model.md#advantages%20and%20disadvantages)

## week 7 lecture 2

- datetime: 2025-10-16T15:00:00+08:00/2025-10-16T16:20:00+08:00, PT1H20M
- topic:
- FINA 3103
  - FINA 3103 / [arbitrage pricing theory](arbitrage%20pricing%20theory.md)
    - [§ single index model](arbitrage%20pricing%20theory.md#single%20index%20model)
    - [§ variance and covariance under SIM](arbitrage%20pricing%20theory.md#variance%20and%20covariance%20under%20SIM)  
    - [§ CAPM and SIM](arbitrage%20pricing%20theory.md#CAPM%20and%20SIM)  
    - [§ SIM limitations](arbitrage%20pricing%20theory.md#SIM%20limitations)  
    - [§ multiple factors model](arbitrage%20pricing%20theory.md#multiples%20factors%20model)  
    - [§ factor-mimicking portfolio](arbitrage%20pricing%20theory.md#factor-mimicking%20portfolio)  
    - [§ interpretation of multiple factors model](arbitrage%20pricing%20theory.md#interpretation%20of%20multiple%20factors%20model)  
    - [§ background](arbitrage%20pricing%20theory.md#background)  
    - [§ APT formula](arbitrage%20pricing%20theory.md#APT%20formula)  
    - [§ arbitrage](arbitrage%20pricing%20theory.md#abitrage)  
    - [§ APT and multiple factors model](arbitrage%20pricing%20theory.md#APT%20and%20multiple%20factors%20model)  
    - [§ advantages and disadvantages](arbitrage%20pricing%20theory.md#advantages%20and%20disadvantages)

## week 8 lecture

- datetime: 2025-10-21T15:00:00+08:00/2025-10-21T16:20:00+08:00, PT1H20M
- status: unscheduled; midterm examination

## week 8 lecture 2

- datetime: 2025-10-23T15:00:00+08:00/2025-10-23T16:20:00+08:00, PT1H20M
- topic:
- FINA 3103
  - FINA 3103 / [capital asset pricing model](capital%20asset%20pricing%20model.md)
  - FINA 3103 / [arbitrage pricing theory](arbitrage%20pricing%20theory.md)

## week 9 lecture

- datetime: 2025-10-28T15:00:00+08:00/2025-10-28T16:20:00+08:00, PT1H20M
- topic:
- FINA 3103
  - FINA 3103 / [arbitrage pricing theory](arbitrage%20pricing%20theory.md)
    - [§ law of one price](arbitrage%20pricing%20theory.md#law%20of%20one%20price)  
    - [§ factors](arbitrage%20pricing%20theory.md#factors)
    - [§ hypothesis testing](arbitrage%20pricing%20theory.md#hypothesis%20testing)
    - [§ Fama–French three-factor model](arbitrage%20pricing%20theory.md#Fama–French%20three-factor%20model)
    - [§ Carhart four-factor model](arbitrage%20pricing%20theory.md#Carhart%20four-factor%20model)

## week 9 lecture 2

- datetime: 2025-10-30T15:00:00+08:00/2025-10-30T16:20:00+08:00, PT1H20M
- topic:
- FINA 3103
  - FINA 3103 / [investment fund](investment%20fund.md)
    - [§ net asset value](investment%20fund.md#net%20asset%20value)
    - [§ asset under management](investment%20fund.md#asset%20under%20management)  
    - [§ types](investment%20fund.md#types)  
    - [§ open-end funds](investment%20fund.md#open-end%20funds)  
    - [§ closed-end funds](investment%20fund.md#closed-end%20funds)  
    - [§ exchange-traded funds](investment%20fund.md#exchange-traded%20funds)  
    - [§ real estate investment trusts](investment%20fund.md#real%20estate%20investment%20trusts)  
    - [§ hedge funds](investment%20fund.md#hedge%20funds)  
    - [§ taxation](investment%20fund.md#taxation)  
    - [§ management styles](investment%20fund.md#management%20styles)  
    - [§ performance evaluation](investment%20fund.md#performance%20evaluation)

## week 10 lecture

- datetime: 2025-11-04T15:00:00+08:00/2025-11-04T16:20:00+08:00, PT1H20M
- topic:
- FINA 3103
  - FINA 3103 / [investment fund](investment%20fund.md)
    - [§ style analysis](investment%20fund.md#style%20analysis)  
    - [§ risk-adjusted performance measures](investment%20fund.md#risk-adjusted%20performance%20measures)  
    - [§ estimating the measures](investment%20fund.md#estimating%20the%20measures)  
    - [§ market timing strategy](investment%20fund.md#market%20timing%20strategy)

## week 10 lecture 2

- datetime: 2025-11-06T15:00:00+08:00/2025-11-06T16:20:00+08:00, PT1H20M
- topic:
- FINA 3103
  - FINA 3103 / [efficient-market hypothesis](efficient-market%20hypothesis.md)
    - [§ definition](efficient-market%20hypothesis.md#definition)
    - [§ assumptions](efficient-market%20hypothesis.md#assumptions)  
    - [§ types of information](efficient-market%20hypothesis.md#types%20of%20information)  
    - [§ mechanism](efficient-market%20hypothesis.md#mechanism)  
    - [§ three forms of market efficiency](efficient-market%20hypothesis.md#three%20forms%20of%20market%20efficiency)  
    - [§ static vs. dynamic efficiency](efficient-market%20hypothesis.md#static%20vs.%20dynamic%20efficiency)  
    - [§ weak-form efficiency](efficient-market%20hypothesis.md#weak-form%20efficiency)  
    - [§ evidence for weak-form efficiency](efficient-market%20hypothesis.md#evidence%20for%20weak-form%20efficiency)  
    - [§ semi-strong-form efficiency](efficient-market%20hypothesis.md#semi-strong-form%20efficiency)  
    - [§ evidence for semi-strong-form efficiency](efficient-market%20hypothesis.md#evidence%20for%20semi-strong-form%20efficiency)  
    - [§ strong-form efficiency](efficient-market%20hypothesis.md#strong-form%20efficiency)  
    - [§ no-trade theorem and noise trading](efficient-market%20hypothesis.md#no-trade%20theorem%20and%20noise%20trading)  
    - [§ evidence for strong-form efficiency](efficient-market%20hypothesis.md#evidence%20for%20strong-form%20efficiency)  
    - [§ implications](efficient-market%20hypothesis.md#implications)

## week 11 lecture

- datetime: 2025-11-11T15:00:00+08:00/2025-11-11T16:20:00+08:00, PT1H20M
- topic:
- FINA 3103
  - FINA 3103 / [behavioural finance](behavioural%20finance.md)
    - [§ motivation](behavioural%20finance.md#motivation)  
    - [§ projection bias](behavioural%20finance.md#projection%20bias)  
    - [§ overconfidence](behavioural%20finance.md#overconfidence)  
    - [§ inattention](behavioural%20finance.md#inattention)  
    - [§ inattention model](behavioural%20finance.md#inattention%20model)  
    - [§ framing](behavioural%20finance.md#framing)  
    - [§ propsect theory](behavioural%20finance.md#propsect%20theory)  
    - [§ endowment and disposition effects](behavioural%20finance.md#endowment%20and%20disposition%20effects)

## week 11 lecture 2

- datetime: 2025-11-13T15:00:00+08:00/2025-11-13T16:20:00+08:00, PT1H20M
- topic:
- FINA 3103
  - FINA 3103 / [fixed income](fixed%20income.md)
    - [§ definition](fixed%20income.md#definition)  
    - [§ valuation](fixed%20income.md#valuation)  
    - [§ zero-coupon bonds](fixed%20income.md#zero-coupon%20bonds)  
    - [§ coupon bonds](fixed%20income.md#coupon%20bonds)  
    - [§ yield to maturity](fixed%20income.md#yield%20to%20maturity)  
    - [§ yield curve](fixed%20income.md#yield%20curve)  
    - [§ spot rate](fixed%20income.md#spot%20rate)  
    - [§ spot rate versus YTM](fixed%20income.md#spot%20rate%20versus%20YTM)  
    - [§ forward rate](fixed%20income.md#forward%20rate)  
    - [§ risks](fixed%20income.md#risk)  
    - [§ yield decomposition](fixed%20income.md#yield%20decomposition)  
    - [§ interest rate risk and duration](fixed%20income.md#interest%20rate%20risk%20and%20duration)  
    - [§ convexity correction](fixed%20income.md#convexity%20correction)  
    - [§ portfolio duration](fixed%20income.md#portfolio%20duration)  
    - [§ immunization](fixed%20income.md#immunization)  
    - [§ limitations of immunization](fixed%20income.md#limitations%20of%20immunization)  
    - [§ portfolio strategies](fixed%20income.md#portfolio%20strategies)

## week 12 lecture

- datetime: 2025-11-18T15:00:00+08:00/2025-11-18T16:20:00+08:00, PT1H20M
- topic:
- FINA 3103
  - FINA 3103 / [forward and futures](forward%20and%20futures.md)
    - [§ derivatives](forward%20and%20futures.md#derivatives)  
    - [§ motivation](forward%20and%20futures.md#moti​vation)  
    - [§ history](forward%20and%20futures.md#history)  
    - [§ forward](forward%20and%20futures.md#forward)  
    - [§ futures](forward%20and%20futures.md#futures)  
    - [§ market-to-market mechanism](forward%20and%20futures.md#market-to-market%20mechanism)  
    - [§ counterparty risk and clearing house](forward%20and%20futures.md#counterparty%20risk%20and%20clearing%20house)  
    - [§ pricing](forward%20and%20futures.md#pricing)  
    - [§ payoffs](forward%20and%20futures.md#payoffs)  
    - [§ replicating portfolio](forward%20and%20futures.md#replicating%20portfolio)  
    - [§ contango and backwardation](forward%20and%20futures.md#contango%20and%20backwardation)  
    - [§ holding cost and convenience yield](forward%20and%20futures.md#holding%20cost%20and%20convenience%20yield)  
    - [§ pricing examples](forward%20and%20futures.md#pricing%20examples)  
    - [§ implied rates](forward%20and%20futures.md#implied%20rates)  
    - [§ basis trading](forward%20and%20futures.md#basis%20trading)  
    - [§ hedging](forward%20and%20futures.md#hedging)

## week 12 lecture 2

- datetime: 2025-11-20T15:00:00+08:00/2025-11-20T16:20:00+08:00, PT1H20M
- topic:
- FINA 3103
  - FINA 3103 / [forward and futures](forward%20and%20futures.md)

## week 13 lecture

- datetime: 2025-11-25T15:00:00+08:00/2025-11-25T16:20:00+08:00, PT1H20M
- topic:
- FINA 3103
  - FINA 3103 / [option](option.md)
    - [§ option rights](option.md#option%20rights)  
    - [§ option styles](option.md#option%20styles)  
    - [§ contract specification](option.md#contract%20specification)  
    - [§ payoff and profit](option.md#payoff%20and%20profit)  
    - [§ moneyness](option.md#moneyness)  
    - [§ trading strategies](option.md#trading%20strategies)  
    - [§ protective put](option.md#protective%20put)  
    - [§ money spread](option.md#money%20spread)  
    - [§ straddle](option.md#straddle)  
    - [§ put–call parity](option.md#put–call%20parity)  
    - [§ put–call arbitrage](option.md#put–call%20arbitrage)  
    - [§ valuation](option.md#valuation)  
    - [§ binomial options pricing model](option.md#binomial%20options%20pricing%20model)  
    - [§ recursive binomial options pricing model](option.md#recursive%20binomial%20options%20pricing%20model)  
    - [§ Black–Scholes model](option.md#Black–Scholes%20model)  
    - [§ implied volatility](option.md#implied%20volatility)  
    - [§ interpretation of the Black–Scholes model](option.md#interpretation%20of%20the%20Black–Scholes%20model)  
    - [§ Long-Term Capital Management example](option.md#Long-Term%20Capital%20Management%20example)

## week 13 lecture 2

- datetime: 2025-11-27T15:00:00+08:00/2025-11-27T16:20:00+08:00, PT1H20M
- status: unscheduled

---

> We’ve finished covering all the course material, so there will be __no class on Thursday__. I’ll be in my office, so anyone with questions or discussions is welcome to drop by without an appointment.

## aftermath

### total

- grades: ?/100
  - statistics: ?
