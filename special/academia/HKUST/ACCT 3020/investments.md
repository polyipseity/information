---
aliases:
  - debt investments
  - derivatives and hedging
  - equity investments
  - investments
tags:
  - flashcard/active/special/academia/HKUST/ACCT_3020/investments
  - language/in/English
---

# investments

This note covers the ACCT 3020 material on debt investments, equity investments, the equity method, impairment, and the derivative-and-hedging appendix taught together with the investments topic. The recurring question is: __what is the business purpose of the instrument__? The answer drives measurement, income-statement treatment, and whether fair-value changes go to profit or loss or to other comprehensive income.

A useful map is:

- __debt investments__: contractual principal-and-interest cash flows;
- __equity investments__: ownership interests or rights linked to ownership interests;
- __derivatives__: contracts whose value is derived from an underlying such as a share price, interest rate, commodity price, or exchange rate.

Before applying any of these investment categories, the course first asks whether the instrument is really __debt__ or __equity__. Debt has a contractual principal amount, interest pattern, and settlement logic. Equity does __not__ promise a fixed maturity amount or coupon stream, so the accounting turns instead on fair value, influence, and control.

## classification of debt investments

Under IFRS 9, the course groups debt investments into three categories:

- __held-for-collection__: measured at amortized cost;
- __held-for-collection and selling__: measured using amortized cost during the period but adjusted to fair value at reporting dates, with unrealized gains and losses in OCI; and
- __trading__: measured at fair value, with unrealized gains and losses in net income.

The classification follows two ideas taught repeatedly in the slides:

1. What is the company's __business model__ for managing the financial asset?
2. What are the __contractual cash flow characteristics__ of the investment?

The second criterion is often called the __SPPI test__: the instrument's contractual cash flows must consist __solely of payments of principal and interest__ on the principal outstanding. A plain fixed-rate bond with regular coupons typically passes. An instrument whose cash flows depend on equity returns, a leveraged multiple, or any non-principal-and-interest formula fails — and must be measured at FVTPL regardless of business model. Separately, a company may irrevocably designate an otherwise SPPI-eligible debt instrument at __FVTPL__ (the fair value option, or __FVO__) if doing so eliminates or significantly reduces a measurement inconsistency; that designation cannot later be revoked.

If the company mainly wants to collect contractual interest and principal, amortized-cost accounting is appropriate. If it may both collect and sell, fair value still matters, but the unrealized changes stay out of ordinary profit and loss until realization. If it is actively trading, fair value changes belong in income immediately.

The transcript repeatedly links this classification to a practical investor question: is the company buying the bond to collect contractual cash flows, to collect and later sell, or to trade for a quicker gain? The accounting follows that stated purpose rather than treating every bond as if it had the same exit plan.

> _Initial classification example._ A company buys {@{€100&nbsp;000 face amount of 8% bonds}@} for {@{€92&nbsp;000}@}. Management documents that the purpose is to {@{collect contractual interest and principal rather than to sell actively}@}. The initial entry is the same purchase entry that any debt investment would use, but the stated business model determines whether later accounting will follow amortized cost, HFCS, or trading rules.
>
> | {@{Purchase debt investment classified as held-for-collection}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Debt investments}@} | {@{92&nbsp;000}@} | |
> | {@{Cash}@} | | {@{92&nbsp;000}@} |
>
> _Explanation._ The initial purchase entry does {@{not by itself reveal the later category}@}. The category comes from the documented business purpose: {@{collect}@}, {@{collect and sell}@}, or {@{trade}@}.

---

Flashcards for this section are as follows:

- debt investments: three IFRS 9 categories in this course ::@:: Held-for-collection, held-for-collection and selling, and trading.
- debt investment classification: the two core questions ::@:: What is the company's business model for managing the asset, and what are the contractual cash flow characteristics of the investment?
- held-for-collection: measurement basis ::@:: Amortized cost.
- held-for-collection and selling: fair-value changes go where? ::@:: Unrealized holding gains and losses go to OCI, not to net income.
- trading debt investments: fair-value changes go where? ::@:: To net income immediately.
- debt investment classification: practical business-purpose triad ::@:: The investor may buy the bond to collect contractual cash flows, to collect and later sell, or to trade for a quicker gain.
- debt investment classification: does the initial cash entry alone determine the category? ::@:: No. The same purchase entry can appear across categories; the classification is determined by business purpose and contractual cash-flow characteristics.
- SPPI test: what does it require? ::@:: Contractual cash flows must consist solely of payments of principal and interest on the principal outstanding; any equity-linked, leveraged, or other non-standard cash flow component causes the instrument to fail the test and forces FVTPL classification.
- FVO irrevocable designation: when can it be used for debt instruments? ::@:: A company may irrevocably elect to measure an eligible debt instrument at FVTPL if doing so eliminates or significantly reduces an accounting mismatch. The election cannot later be revoked.

## debt investments at amortized cost

A held-for-collection debt investment is initially recorded at cost and then carried using the __effective-interest method__. The effective-interest method keeps two numbers distinct:

- __cash interest received__: based on the bond's stated coupon; and
- __interest revenue__: based on the bond's carrying amount and effective yield.

The difference between them is the amortization of discount or premium.

- For a __discount bond__, interest revenue is greater than cash received, so the carrying amount rises over time.
- For a __premium bond__, interest revenue is less than cash received, so the carrying amount falls over time.

> _Discount bond at amortized cost._ Robinson buys {@{€100&nbsp;000 of 8% bonds}@} for {@{€92&nbsp;278}@}. The bonds mature in {@{5 years and yield 10%}@}. Interest is paid each {@{July 1 and January 1}@}.
>
> | {@{Purchase debt investment at amortized cost}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Debt investments}@} | {@{92&nbsp;278}@} | |
> | {@{Cash}@} | | {@{92&nbsp;278}@} |

<!-- markdownlint MD028 -->

> _Purchase between coupon dates instead of on a clean interest date._ Suppose the same bond is purchased {@{3 months after the last semiannual coupon date}@}. The investor still records the bond at its {@{92&nbsp;278 carrying amount}@}, but must also pay the seller {@{3 months of accrued coupon interest = €100&nbsp;000 × 8% × 3/12 = €2&nbsp;000}@}.
>
> | {@{Purchase amortized-cost debt investment between coupon dates}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Debt investments}@} | {@{92&nbsp;278}@} | |
> | {@{Interest receivable}@} | {@{2&nbsp;000}@} | |
> | {@{Cash}@} | | {@{94&nbsp;278}@} |
>
> _Explanation._ The buyer pays for both the {@{bond itself at its 92&nbsp;278 carrying amount}@} and the {@{seller's already-earned coupon period up to the purchase date}@}. The accrued-interest piece is {@{not part of the bond's carrying amount}@}.
>
> _At the next coupon date (3 months later)._ The investor receives the full {@{€4&nbsp;000 semiannual coupon}@}. Of that amount, {@{€2&nbsp;000 clears the Interest receivable recorded at purchase}@}. The remaining {@{3 months belong to the new investor}@}, so current-period interest revenue is {@{€92&nbsp;278 × 10% × 3/12 ≈ €2&nbsp;307}@}. Discount amortization for the 3-month holding period is therefore {@{€2&nbsp;307 − €2&nbsp;000 = €307}@}.
>
> | {@{Record the next coupon receipt after purchasing the bond between coupon dates}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{4&nbsp;000}@} | |
> | {@{Debt investments}@} | {@{307}@} | |
> | {@{Interest receivable}@} | | {@{2&nbsp;000}@} |
> | {@{Interest revenue}@} | | {@{2&nbsp;307}@} |
>
> _Interpretation._ The next coupon date mixes {@{recovery of the seller's accrued interest}@} with the {@{new investor's own 3-month effective-interest revenue and discount amortization}@}. That is why this entry differs from a clean-date purchase. The later year-end accrual uses the same structure again, except that {@{Interest receivable replaces Cash because the coupon has not yet been collected}@}.

<!-- markdownlint MD028 -->

> _Sale of held-for-collection bonds before maturity._ Assume the carrying amount has already been updated through the sale date to {@{€96&nbsp;200}@}. Immediately before the sale entry, assume the investor must still record the last amortization update for the stub period: carrying amount before the update is {@{€95&nbsp;555}@}, and the final discount amortization needed to reach the sale-date amortized cost is therefore {@{€645 = €96&nbsp;200 − €95&nbsp;555}@}. That final stub-period interest revenue consists of {@{€2&nbsp;667 accrued interest revenue plus €645 discount amortization = €3&nbsp;312 total interest revenue}@}. The bonds are then sold for {@{99.60 plus accrued interest}@}, so cash received is {@{€102&nbsp;267 = €99&nbsp;600 + €2&nbsp;667 accrued interest}@}.
>
> | {@{Update the held-for-collection bond to its sale-date amortized cost before recording the sale}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Interest receivable}@} | {@{2&nbsp;667}@} | |
> | {@{Debt investments}@} | {@{645}@} | |
> | {@{Interest revenue}@} | | {@{3&nbsp;312}@} |
>
> | {@{Sell held-for-collection debt investment before maturity}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{102&nbsp;267}@} | |
> | {@{Interest receivable}@} | | {@{2&nbsp;667}@} |
> | {@{Debt investments}@} | | {@{96&nbsp;200}@} |
> | {@{Gain on sale of investments}@} | | {@{3&nbsp;400}@} |
>
> _Explanation._ The sale-date entry combines the {@{collection of the already-accrued interest receivable}@} and the {@{realized gain on disposal versus carrying amount}@}. That is why the cash figure is larger than the clean bond price alone.

If a held-for-collection investment is sold before maturity, the company must first update amortized cost through the sale date and then compare sale proceeds with carrying amount to compute the realized gain or loss.

An alternative endpoint method is often the safest way to handle fair-value questions. First update the book or amortized-cost amount for everything that happened before the fair-value adjustment (interest, amortization, dividends, and so on). Then compare that updated amount with fair value. If the course uses a separate _Fair value adjustment_ account, the required ending balance in that account is simply {@{fair value − updated book value}@}. The current-period fair-value entry is whatever amount moves the account from its existing balance to that required ending balance. This endpoint method always works for ordinary fair-value-adjustment problems because the accounting target is just the correct ending carrying amount. The caveat is that if a separate {@{credit-loss allowance also exists}@}, the total gap to fair value still gives the combined valuation reduction needed, but you must split that total between the {@{market-driven fair value adjustment}@} and the {@{credit-loss allowance}@}; the endpoint method alone does not decide that split.

---

Flashcards for this section are as follows:

- effective-interest method: why is cash interest different from interest revenue? ::@:: Because cash interest uses the coupon rate, while interest revenue uses the carrying amount times the effective yield.
- discount bond at amortized cost: what happens to carrying amount over time? ::@:: It increases toward face value as the discount is amortized.
- premium bond at amortized cost: what happens to carrying amount over time? ::@:: It decreases toward face value as the premium is amortized.
- held-for-collection sale before maturity: what must be done before computing gain or loss? ::@:: Update interest accrual and discount or premium amortization through the sale date so the carrying amount is current.
- amortized cost intuition ::@:: It is the investment's adjusted carrying amount after applying the effective-interest method, not simply face value or historical purchase price.
- debt investment purchased between coupon dates: what is the common trap? ::@:: Accrued coupon paid to the seller is recorded separately as _Interest receivable_; it is not added to the bond's amortized-cost carrying amount. Example: €100&nbsp;000 × 8% × 3/12 = €2&nbsp;000 of accrued coupon is debited to _Interest receivable_, not to _Debt investments_.
- debt investment purchased between coupon dates: what happens at the next coupon date? ::@:: The investor receives the full coupon, but part of it merely clears the accrued-interest receivable recorded at purchase. Example: Dr _Cash_ 4&nbsp;000 and Dr _Debt investments_ 307; Cr _Interest receivable_ 2&nbsp;000 and Cr _Interest revenue_ 2&nbsp;307.

## debt investments at fair value

---

Flashcards for this section are as follows:

- debt investments at fair value: common measurement idea ::@:: Update interest and amortized-cost mechanics first, then apply fair-value accounting; the classification determines whether the unrealized fair-value change goes to OCI or net income.
- debt investments at fair value: key split in this note ::@:: Held-for-collection-and-selling debt sends unrealized fair-value changes to OCI, while trading debt sends them directly to current net income.
- fair value adjustment: endpoint method with a separate Fair value adjustment account ::@:: First update the book or amortized-cost amount for everything else. Then compute the required ending _Fair value adjustment_ balance as fair value minus updated book value. The current-period entry is the amount needed to move the existing balance to that required ending balance.
- fair value adjustment endpoint method: does it always work? ::@:: It always works for ordinary fair-value-adjustment problems if the carrying amount has already been updated for interest, amortization, dividends, and similar items. If a separate credit-loss allowance also exists, the total gap to fair value still gives the combined valuation reduction needed, but you must still split that total between the fair value adjustment and the impairment allowance.

### held-for-collection and selling

Debt investments held for both collection and possible sale follow the same interest-revenue and amortized-cost entries during the period, but at each reporting date the company also adjusts them to __fair value__. The unrealized change goes to __OCI__ rather than net income.

> _HFCS bond at premium._ Graff buys {@{£100&nbsp;000 of 10% bonds}@} for {@{£108&nbsp;111}@}, giving an effective yield of {@{8%, so the bond carries a premium above face}@}. After recording interest revenue and premium amortization during the year, the amortized carrying amount at year-end is {@{£106&nbsp;732, but fair value is only £105&nbsp;000}@}.
>
> | {@{Record first semiannual HFCS interest revenue and premium amortization}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{5&nbsp;000}@} | |
> | {@{Debt investments}@} | | {@{676}@} |
> | {@{Interest revenue}@} | | {@{4&nbsp;324}@} |
>
> | {@{Accrue year-end HFCS interest revenue and premium amortization}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Interest receivable}@} | {@{5&nbsp;000}@} | |
> | {@{Debt investments}@} | | {@{703}@} |
> | {@{Interest revenue}@} | | {@{4&nbsp;297}@} |
>
> | {@{Apply fair value to HFCS debt investment}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Unrealized holding gain or loss — equity (OCI)}@} | {@{1&nbsp;732}@} | |
> | {@{Fair value adjustment}@} | | {@{1&nbsp;732}@} |
>
> _Explanation._ The bond is still shown at fair value on the statement of financial position, but the unrealized decline is kept out of current net income. Using the endpoint method, the required ending {@{Fair value adjustment credit balance is £1&nbsp;732 because fair value £105&nbsp;000 is £1&nbsp;732 below amortized carrying amount £106&nbsp;732}@}. If no earlier fair value adjustment balance exists, the full {@{£1&nbsp;732}@} is recorded now.

<!-- markdownlint MD028 -->

> _HFCS portfolio fair value adjustment._ A company holds two HFCS bonds. One shows an unrealized loss of {@{€12&nbsp;000}@} and the other an unrealized gain of {@{€2&nbsp;500}@}. The portfolio therefore has a {@{net unrealized loss of €9&nbsp;500}@} at year-end.
>
> | {@{Record net portfolio fair value loss on HFCS debt investments}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Unrealized holding gain or loss — equity (OCI)}@} | {@{9&nbsp;500}@} | |
> | {@{Fair value adjustment}@} | | {@{9&nbsp;500}@} |
>
> _Explanation._ This is the same endpoint method at the portfolio level: the required ending {@{Fair value adjustment credit balance is €9&nbsp;500}@}, so the entry simply moves the account to that balance.

<!-- markdownlint MD028 -->

> _Sale of an HFCS bond._ One HFCS bond is sold for {@{€90&nbsp;000 plus accrued interest}@} when its amortized cost is {@{€94&nbsp;200}@}. Immediately before the sale entry, assume the investor must still record the last amortization update for the stub period: carrying amount before the update is {@{€93&nbsp;555}@}, and the final discount amortization needed to reach the sale-date amortized cost is therefore {@{€645 = €94&nbsp;200 − €93&nbsp;555}@}. That final stub-period interest revenue consists of {@{€2&nbsp;667 accrued interest revenue plus €645 discount amortization = €3&nbsp;312 total interest revenue}@}. Total cash received is therefore {@{€92&nbsp;667 = €90&nbsp;000 clean price + €2&nbsp;667 accrued interest}@}.
>
> | {@{Update the held-for-collection bond to its sale-date amortized cost before recording the sale}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Interest receivable}@} | {@{2&nbsp;667}@} | |
> | {@{Debt investments}@} | {@{645}@} | |
> | {@{Interest revenue}@} | | {@{3&nbsp;312}@} |
>
> | {@{Sell HFCS debt investment and recognize realized loss}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{92&nbsp;667}@} | |
> | {@{Interest receivable}@} | | {@{2&nbsp;667}@} |
> | {@{Loss on sale of investments}@} | {@{4&nbsp;200}@} | |
> | {@{Debt investments}@} | | {@{94&nbsp;200}@} |
>
> _Explanation._ If this bond carries {@{no accumulated OCI / AOCI balance at the sale date}@}, there is {@{no OCI layer left to clear}@}; the disposal entry simply compares sale proceeds with the bond's {@{amortized cost at the sale date}@}. That is also why __trading debt investments__ never need an OCI-clearing step on sale: their fair-value changes were already recognized in {@{net income rather than OCI}@}.

<!-- markdownlint MD028 -->

> _Sale of an HFCS bond with an accumulated OCI balance._ Suppose the same bond also carries an existing {@{€3&nbsp;800 cumulative unrealized loss in OCI}@} from earlier fair-value adjustments, with a matching {@{€3&nbsp;800 credit balance in Fair value adjustment}@}. The bond's {@{amortized cost is still €94&nbsp;200}@}, but its {@{fair-value carrying amount is only €90&nbsp;400 = €94&nbsp;200 − €3&nbsp;800}@}. Because the note is measuring the disposal loss against {@{amortized cost}@}, the company should __not__ add a second standalone loss entry for OCI recycling on top of that. Instead it clears the fair-value layer as part of the overall disposal mechanics.
>
> | {@{Sell HFCS debt investment when a prior OCI loss and matching fair value adjustment are still on the books}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{92&nbsp;667}@} | |
> | {@{Fair value adjustment}@} | {@{3&nbsp;800}@} | |
> | {@{Loss on sale of investments}@} | {@{4&nbsp;200}@} | |
> | {@{Interest receivable}@} | | {@{2&nbsp;667}@} |
> | {@{Debt investments}@} | | {@{94&nbsp;200}@} |
> | {@{Accumulated comprehensive income}@} | | {@{3&nbsp;800}@} |

_Explanation._ Your concern is correct: if the sale loss is already being recorded as {@{sale proceeds versus amortized cost}@}, then a separate extra {@{Dr Loss on sale / Cr Accumulated comprehensive income}@} line would __double count__ the OCI loss. The correct mechanics are to record the total {@{€4&nbsp;200 loss once}@} and also clear the old {@{Fair value adjustment and related accumulated OCI balance}@}. A separate standalone OCI-to-loss reclassification entry would be used only under a different presentation where the disposal gain or loss were first measured against the bond's {@{fair-value carrying amount instead of amortized cost}@}.

---

Flashcards for this section are as follows:

- HFCS debt investment: where do unrealized fair-value changes go before sale? ::@:: To OCI rather than net income, while interest revenue and amortized-cost updates still follow the debt-investment mechanics.
- HFCS debt sale without prior OCI balance: is a separate AOCI reclassification entry needed? ::@:: No. If no cumulative OCI balance remains, the sale entry just compares proceeds with amortized cost and removes accrued interest separately.
- HFCS debt sale with prior OCI balance: what must be cleared, and what must not be double counted? ::@:: Clear the old _Fair value adjustment_ and the related accumulated OCI balance, but do not add a second standalone loss entry if the disposal loss is already measured against amortized cost.
- HFCS sale: realized gain or loss is based on what comparison? ::@:: Sale proceeds versus the investment's amortized cost at the sale date.
- HFCS sale with prior OCI history: what extra step is needed? ::@:: Clear the accumulated OCI balance related to that debt investment out of equity when the bond is sold, but do not double count the loss if disposal is already measured against amortized cost.

When an HFCS debt investment is sold, the realized gain or loss is based on sale proceeds versus __amortized cost__, not versus original purchase price. The company must also update the fair-value-adjustment balances appropriately.

### trading debt investments

Trading debt investments are simpler conceptually but more volatile in income:

- they are held for short-term sale or active portfolio management;
- they are measured at __fair value__; and
- unrealized holding gains and losses go to __net income__.

The fair-value adjustment for trading securities is usually done at the __portfolio__ level in this course.

> _Trading portfolio year-end adjustment._ Western Publishing measures a newly acquired trading debt portfolio and finds that fair value exceeds carrying amount by {@{3&nbsp;750}@}.
>
> | {@{Record year-end fair value increase for trading debt portfolio}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Fair value adjustment}@} | {@{3&nbsp;750}@} | |
> | {@{Unrealized holding gain or loss — income}@} | | {@{3&nbsp;750}@} |
>
> _Explanation._ The endpoint method works here too: the required ending {@{Fair value adjustment debit balance is 3&nbsp;750 because fair value exceeds carrying amount by that amount}@}. If the account already had a balance, only the difference needed to reach the required ending balance would be recorded.

---

Flashcards for this section are as follows:

- trading debt investments: where do unrealized gains and losses go? ::@:: Directly to current net income, not to OCI or AOCI.
- trading debt investments: why is there no OCI recycling step on sale? ::@:: Because trading debt investments do not park fair-value changes in OCI first; those gains and losses have already gone through income.
- trading debt portfolio: why does income become more volatile? ::@:: Because every fair-value change is recognized in current net income.

## equity investments at fair value

An equity investment represents an ownership interest such as ordinary shares, preference shares, warrants, or similar rights. For investments with less than 20% influence, the course separates two broad fair-value treatments. Because both categories are already carried at __fair value__, no separate impairment test is required for FVTPL or FVOCI-equity investments — any economic decline is captured through the recurring fair-value remeasurement each period.

---

Flashcards for this section are as follows:

- equity investments at fair value: common measurement idea ::@:: Small equity investments are measured at fair value, but the chosen classification decides whether unrealized changes run through income or through OCI.
- trading versus non-trading small equity investment ::@:: Trading equity sends unrealized fair-value changes to income, while the non-trading OCI election sends them to OCI on an investment-by-investment basis.
- equity investments: how are cash dividends received treated in this course? ::@:: As dividend revenue.
- trading versus non-trading equity investment: common measurement basis ::@:: Both are measured at fair value; the key difference is whether unrealized changes go to income or OCI.
- equity investments: is a separate impairment test required for FVTPL or FVOCI-equity? ::@:: No. Both categories are already measured at fair value, so economic declines are immediately captured through the recurring fair-value remeasurement — no separate impairment model applies.

### trading equity investments

Under IFRS, a small equity investment is often presumed to be held for trading unless the company elects a non-trading OCI presentation for the particular investment. Trading equity investments are:

- measured at fair value; and
- all unrealized gains and losses go to __net income__.

Cash dividends received are recognized as __dividend revenue__.

> _Trading equity portfolio acquired and remeasured._ A company buys a trading portfolio of ordinary shares for {@{€720&nbsp;000}@}. Before year-end, it receives {@{€4&nbsp;500 cash dividends}@}. At year-end the portfolio's fair value has fallen by {@{€36&nbsp;000}@}.
>
> | {@{Purchase trading equity investments}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Equity investments}@} | {@{720&nbsp;000}@} | |
> | {@{Cash}@} | | {@{720&nbsp;000}@} |
>
> | {@{Record dividend revenue on trading equity investments}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{4&nbsp;500}@} | |
> | {@{Dividend revenue}@} | | {@{4&nbsp;500}@} |
>
> | {@{Record year-end fair value loss on trading equity portfolio}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Unrealized holding gain or loss — income}@} | {@{36&nbsp;000}@} | |
> | {@{Fair value adjustment}@} | | {@{36&nbsp;000}@} |
>
> _Explanation._ The endpoint method works here as well: the required ending {@{Fair value adjustment credit balance is €36&nbsp;000 because fair value is €36&nbsp;000 below carrying amount}@}. If the account already had a balance, only the amount needed to move it to that ending balance would be recorded.

<!-- markdownlint MD028 -->

> _Sale of a trading equity investment._ Later, one block of shares is sold for {@{€287&nbsp;000}@} when its adjusted carrying amount is {@{€260&nbsp;000}@}.
>
> | {@{Sell trading equity investment and recognize realized gain}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{287&nbsp;000}@} | |
> | {@{Equity investments}@} | | {@{260&nbsp;000}@} |
> | {@{Gain on sale of investments}@} | | {@{27&nbsp;000}@} |
>
> _Explanation._ No separate {@{AOCI or OCI reclassification entry is needed for the sale of a trading equity investment}@} because the investment's earlier unrealized fair-value changes were already recognized in {@{net income rather than OCI}@}. The sale entry therefore just removes the adjusted carrying amount and records the realized gain or loss.

---

Flashcards for this section are as follows:

- trading equity investments: where do unrealized fair-value changes go? ::@:: To net income, so the investment builds no OCI / AOCI balance from ordinary remeasurement.
- trading equity investment sale: is any AOCI recycling entry needed? ::@:: No. Trading equity investments do not build up AOCI from fair-value changes because those unrealized gains and losses were already recognized in net income.
- trading equity investment sale: what carrying amount is removed? ::@:: Remove the investment at its adjusted carrying amount at the sale date and compare that amount with sale proceeds to determine the realized gain or loss.

### non-trading equity investments (OCI)

Some small equity investments are strategic rather than trading-oriented. The course treats these as fair-value investments whose unrealized changes go to __OCI__ instead of net income. One detail from the slides matters:

- the non-trading classification is applied __investment by investment__, not as a whole portfolio bucket.

> _Non-trading strategic equity investment._ Republic buys {@{1&nbsp;000 Hawthorne ordinary shares}@} for {@{€20&nbsp;750}@}. At year-end, fair value is {@{€24&nbsp;000}@}, so the carrying value must increase by {@{€3&nbsp;250}@}.
>
> | {@{Increase non-trading equity investment to fair value}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Equity investment}@} | {@{3&nbsp;250}@} | |
> | {@{Unrealized holding gain or loss — equity (OCI)}@} | | {@{3&nbsp;250}@} |
>
> _Interpretation._ Dividends still go to income, but the unrealized fair-value movement does not. The same endpoint logic still works: {@{€24&nbsp;000 fair value − €20&nbsp;750 carrying amount = €3&nbsp;250}@}. The only difference is that this course records the adjustment {@{directly in the Equity investment account instead of using a separate Fair value adjustment account}@}.

<!-- markdownlint MD028 -->

> _Dividend and downward adjustment before sale for a non-trading equity investment._ Assume the same investment later pays a {@{€450 dividend}@}. Before sale, fair value falls from {@{€24&nbsp;000 to €22&nbsp;500}@}, so part of the earlier OCI gain must be reversed.
>
> | {@{Record dividend revenue on non-trading equity investment}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{450}@} | |
> | {@{Dividend revenue}@} | | {@{450}@} |
>
> | {@{Reduce carrying amount of non-trading equity investment to new fair value}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Unrealized holding gain or loss — equity (OCI)}@} | {@{1&nbsp;500}@} | |
> | {@{Equity investment}@} | | {@{1&nbsp;500}@} |
>
> | {@{Sell non-trading equity investment at adjusted carrying amount}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{22&nbsp;500}@} | |
> | {@{Equity investment}@} | | {@{22&nbsp;500}@} |

_Explanation._ The investment is sold at its {@{already-updated fair-value carrying amount}@}, so there is {@{no additional gain or loss in net income from the sale entry itself}@}. Under the IFRS treatment used in this course, the earlier unrealized OCI balance on this non-trading equity investment is {@{not recycled to profit or loss on sale}@}; it remains an equity-side OCI history unless the company separately transfers it within equity.

---

Flashcards for this section are as follows:

- non-trading equity investment: where do unrealized fair-value changes go? ::@:: To OCI rather than to current net income.
- non-trading equity investment sale under IFRS in this course: is prior OCI recycled into profit or loss? ::@:: No. The sale entry removes the investment at its adjusted carrying amount, but the earlier OCI history is not recycled through net income.
- non-trading equity investment OCI election: is it made by portfolio or by investment? ::@:: By investment, not by a whole equity portfolio bucket.
- non-trading equity investment: how does the endpoint method look when no separate Fair value adjustment account is used? ::@:: Compute fair value minus carrying amount to get the required change, then record that amount directly in the _Equity investment_ account. Example: €24&nbsp;000 − €20&nbsp;750 = €3&nbsp;250.
- non-trading equity investment before sale: what happens if fair value declines? ::@:: Reverse part of the prior OCI gain or recognize an OCI loss so the carrying amount is updated to fair value before the sale entry.

## influence levels, the equity method, and control

The course uses ownership influence to decide how to account for larger equity investments.

- __Less than 20%__: usually fair-value accounting.
- __20% to 50%__: presumed __significant influence__ and usually use the __equity method__.
- __More than 50%__: control exists, so the investor is the parent and normally prepares consolidated financial statements.

Under the __equity method__:

- record the investment initially at cost;
- increase the carrying amount for the investor's share of the investee's income;
- decrease the carrying amount for dividends received, because dividends are treated as a return of investment rather than as revenue; and
- do __not__ keep remeasuring the investment to market value each period.

> _Equity-method example._ Company A buys a {@{20% interest in Company B}@} for {@{480&nbsp;000}@}. In the same year Company B reports {@{200&nbsp;000 net income}@} and later declares {@{100&nbsp;000 dividends}@}.
>
> | {@{Record initial equity-method investment}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Equity investment}@} | {@{480&nbsp;000}@} | |
> | {@{Cash}@} | | {@{480&nbsp;000}@} |
>
> | {@{Record investor's share of investee income}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Equity investment}@} | {@{40&nbsp;000}@} | |
> | {@{Investment income}@} | | {@{40&nbsp;000}@} |
>
> | {@{Record dividends received under equity method}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{20&nbsp;000}@} | |
> | {@{Equity investment}@} | | {@{20&nbsp;000}@} |

---

Flashcards for this section are as follows:

- influence levels: what accounting method is usually used below 20%? ::@:: Fair-value accounting.
- influence levels: what accounting method is usually used from 20% to 50%? ::@:: The equity method, because significant influence is presumed.
- influence levels: what happens above 50% ownership? ::@:: Control usually exists, so the investor becomes the parent and generally prepares consolidated financial statements.
- equity method: what increases the carrying amount of the investment? ::@:: The investor's share of the investee's income.
- equity method: why do dividends reduce the carrying amount instead of being recognized as revenue? ::@:: Because dividends are treated as a return of investment under the equity method.
- equity method versus fair-value method: what key periodic adjustment differs? ::@:: The equity method tracks the investor's share of changes in the investee's net assets instead of remeasuring the investment to market price each period.

### equity method: unrealized intercompany profit elimination

Under IAS 28, the investor eliminates its proportionate share of any __unrealized profit__ from transactions between the investor and the investee — whether __downstream__ (investor sells to investee) or __upstream__ (investee sells to investor). As long as the goods remain unsold to an independent third party, the embedded profit has not been realized from the economic group's perspective.

> _Downstream unrealized profit elimination._ Company A holds a {@{20% interest}@} in Company B. Company A sells inventory to Company B at a mark-up generating a profit of {@{€50&nbsp;000}@}. At year-end, Company B still holds {@{half of that inventory unsold}@}, leaving {@{€25&nbsp;000 of unrealized profit in Company B's closing inventory}@}. Company A must reduce its equity-method income by its ownership share: {@{20% × €25&nbsp;000 = €5&nbsp;000}@}.
>
> | {@{Eliminate investor's share of unrealized downstream profit in investee's closing inventory}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Investment income}@} | {@{5&nbsp;000}@} | |
> | {@{Equity investment}@} | | {@{5&nbsp;000}@} |
>
> _Explanation._ The entry reduces both {@{investment income}@} and the {@{equity investment carrying amount}@}. Once Company B later sells that inventory to a third party, the profit becomes realized and the investor reverses the elimination entry by {@{debiting Equity investment and crediting Investment income for the same €5&nbsp;000}@}. The same mechanics apply to upstream transactions using the investee's mark-up and the investor's ownership percentage.

---

Flashcards for this section are as follows:

- equity method unrealized profit: what kinds of intercompany transactions require elimination? ::@:: Both downstream (investor sells to investee) and upstream (investee sells to investor), for the investor's proportionate share of any profit still unrealized in closing inventory or other unsold assets.
- equity method downstream profit elimination: what is the entry when profit is unrealized? ::@:: Debit _Investment income_ and credit _Equity investment_ for the investor's ownership percentage of the unrealized profit remaining in the investee's closing inventory.
- equity method unrealized profit: when is the elimination reversed? ::@:: When the goods are eventually sold to an unrelated third party, the profit becomes realized and the deferral is reversed: debit _Equity investment_ and credit _Investment income_.

### loss limitation when the equity-method investment would become negative

Under the equity method, the investor does __not__ keep pushing the _Equity investment_ asset below zero just because the investee keeps reporting losses. Once the carrying amount has been reduced to __zero__, the normal rule is:

- stop recognizing additional equity-method losses;
- keep the excess loss as an __unrecognized loss memorandum amount__; and
- resume recognizing future profits only after those later profits first absorb the previously unrecognized loss.

The main exception is when the investor has gone beyond passive ownership and has __incurred a legal or constructive obligation__ to support the investee, or has already made payments on the investee's behalf. In that case, additional losses are recognized through a __liability__, not by making the investment asset negative.

> _Equity-method losses larger than the remaining carrying amount._ Assume the investor's carrying amount in an associate is only {@{€30&nbsp;000}@}, but its share of the associate's current-year loss is {@{€50&nbsp;000}@}. The investor has {@{no guarantee or support obligation}@}, so it can recognize only the portion that reduces the investment to zero.
>
> | {@{Recognize equity-method loss only up to the remaining carrying amount of the investment}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Loss from equity-method investment}@} | {@{30&nbsp;000}@} | |
> | {@{Equity investment}@} | | {@{30&nbsp;000}@} |
>
> _Explanation._ The remaining {@{€20&nbsp;000 share of loss is not recorded by making Equity investment negative}@}. Instead it becomes an {@{unrecognized loss tracked off-book for future equity-method profit recognition}@}.

<!-- markdownlint MD028 -->

> _Same fact pattern, but the investor has a support obligation._ Suppose the investor has also guaranteed {@{€8&nbsp;000 of the associate's obligations}@}. That extra supported portion is recognized as a liability.
>
> | {@{Recognize additional equity-method loss to the extent of the investor's support obligation}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Loss from equity-method investment}@} | {@{8&nbsp;000}@} | |
> | {@{Liability related to associate support}@} | | {@{8&nbsp;000}@} |
>
> _Explanation._ The extra loss is recognized only because the investor has {@{gone beyond ordinary ownership and now has an obligation tied to the associate}@}. The accounting still does {@{not create a negative Equity investment asset}@}.

<!-- markdownlint MD028 -->

> _Later return to profit after unrecognized losses existed._ If the associate later generates profit and the investor's share is {@{€25&nbsp;000}@}, while the previously unrecognized loss memorandum amount is still {@{€20&nbsp;000}@}, the investor recognizes only the excess {@{€5&nbsp;000}@}.
>
> | {@{Resume equity-method profit recognition only after prior unrecognized losses have first been absorbed}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Equity investment}@} | {@{5&nbsp;000}@} | |
> | {@{Investment income}@} | | {@{5&nbsp;000}@} |
>
> _Explanation._ The first {@{€20&nbsp;000 of the new profit merely reverses the previously unrecognized loss memorandum amount economically}@}. Only the excess {@{€5&nbsp;000}@} becomes current-period recognized investment income.

---

Flashcards for this section are as follows:

- equity method loss limitation: can the investment asset normally become negative? ::@:: No. Once the carrying amount reaches zero, additional losses are normally not recognized through a negative _Equity investment_ balance.
- equity method after carrying amount reaches zero: what happens to further losses? ::@:: They become unrecognized memorandum losses unless the investor has a legal or constructive support obligation or has made payments on the investee's behalf.
- equity method with support obligation: where do additional losses go? ::@:: To a liability, not to a negative investment asset.
- equity method after prior unrecognized losses: when do future profits become recognized income again? ::@:: Only after the new profit first absorbs the previously unrecognized losses.

### equity method: impairment

Even before the carrying amount reaches zero, the investor must assess at each reporting date whether there is objective evidence that the equity-method investment is impaired. The impairment test compares the investment's __carrying amount__ with its __recoverable amount__ — the higher of (a) value in use and (b) fair value less costs to sell. Any excess of carrying amount over recoverable amount is recognized as an impairment loss in income and the carrying amount is written down directly.

> _Equity-method investment impairment._ An investor carries its {@{25% interest}@} in an associate at a carrying amount of {@{€320&nbsp;000}@}. Due to prolonged operating losses and deteriorating market conditions at the associate, the estimated recoverable amount has fallen to {@{€260&nbsp;000}@}. The impairment loss is {@{€60&nbsp;000}@}.
>
> | {@{Recognize impairment loss on equity-method investment}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Loss on impairment of equity investment}@} | {@{60&nbsp;000}@} | |
> | {@{Equity investment}@} | | {@{60&nbsp;000}@} |
>
> _Explanation._ This test is separate from the loss-limitation rule. {@{Loss limitation}@} applies when accumulated equity-method losses reduce the carrying amount toward zero. {@{Impairment}@} applies when the carrying amount still has positive value but exceeds the recoverable amount. If conditions later improve, the impairment loss may be reversed up to the carrying amount that would have existed (including normal equity-method adjustments) if no impairment had been recognized.

---

Flashcards for this section are as follows:

- equity method impairment: when is it triggered? ::@:: When there is objective evidence that the investment's carrying amount exceeds its recoverable amount (the higher of value in use and fair value less costs to sell).
- equity method impairment versus loss-limitation rule: key difference ::@:: Loss limitation applies when accumulated equity-method losses erode the carrying amount to zero. Impairment applies when the carrying amount is still positive but exceeds the recoverable amount.
- equity method impairment: can the loss be reversed? ::@:: Yes. If the recoverable amount subsequently increases, the impairment loss is reversed in income up to the carrying amount that would have existed without the prior impairment.

## impairment of debt investments

The impairment material in this course focuses on debt investments, not on a broad everything-at-once write-down rule. The central distinction is between a decline caused by ordinary __market interest rate__ movement and a decline caused by worsening __credit quality__.

The transcript's expected-credit-loss structure is:

- __stage 1__: no significant increase in credit risk -> recognize __12-month expected credit loss__;
- __stage 2__: significant increase in credit risk -> recognize __lifetime expected credit loss__;
- __stage 3__: the asset is credit-impaired or close to default -> still use __lifetime expected credit loss__, but now the situation is no longer just a warning signal.

So the accounting question is not merely whether fair value fell. The accounting question is whether the fall reflects a higher expected cash shortfall from the debtor.

---

Flashcards for this section are as follows:

- debt-investment impairment: what core distinction drives the accounting? ::@:: Separate a decline caused by ordinary market-rate movement from a decline caused by worsening credit quality.
- debt-investment impairment: why is the cause of the decline important? ::@:: Because market-driven valuation change and credit-loss impairment can go to different reporting locations even when the total fair-value decline looks similar.
- debt-investment impairment: what cash-flow comparison drives the loss? ::@:: Compare the contractual cash flows with the expected cash flows and measure the credit-driven shortfall.
- impairment testing intuition ::@:: The course separates ordinary market-value movement from credit-loss evidence, because they have different income-statement effects.

### expected credit loss stages and what they mean for entries

The stage labels matter because they change the __required allowance balance__, not because each stage has a completely different kind of account. The same basic allowance structure stays in place:

- record impairment losses by increasing the __allowance for impaired debt investments__ and recognizing loss in income;
- when credit risk worsens, increase the allowance to the newly required amount; and
- when credit risk improves, reverse the allowance only to the extent justified under the reversal rules.

The practical accounting meaning of the three stages is:

- __stage 1__: no significant increase in credit risk -> allowance equals __12-month expected credit loss__;
- __stage 2__: significant increase in credit risk -> allowance equals __lifetime expected credit loss__;
- __stage 3__: asset is credit-impaired -> allowance still equals __lifetime expected credit loss__, but now the asset is in a much more severe condition and later estimates often change again.

So the stage transition entry is usually an __incremental top-up or reversal__, not a brand-new accounting model. The key comparison is always: __what allowance balance is required now versus what allowance balance is already on the books__?

> _Allowance mechanics across stages 1, 2, and 3._ Assume a debt investment starts the year in {@{stage 1 with required 12-month expected credit loss of €1&nbsp;200}@}. Later credit risk increases significantly, so the required allowance becomes {@{€6&nbsp;500 lifetime expected credit loss in stage 2}@}. By the following reporting date the asset becomes credit-impaired and the required lifetime expected credit loss rises further to {@{€9&nbsp;000 in stage 3}@}.
>
> | {@{Record stage 1 expected credit loss allowance}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Loss on impairment}@} | {@{1&nbsp;200}@} | |
> | {@{Allowance for impaired debt investments}@} | | {@{1&nbsp;200}@} |
>
> | {@{Top up the allowance when the investment moves from stage 1 to stage 2}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Loss on impairment}@} | {@{5&nbsp;300}@} | |
> | {@{Allowance for impaired debt investments}@} | | {@{5&nbsp;300}@} |
>
> | {@{Top up the allowance again when the investment moves from stage 2 to stage 3 and lifetime expected credit loss increases further}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Loss on impairment}@} | {@{2&nbsp;500}@} | |
> | {@{Allowance for impaired debt investments}@} | | {@{2&nbsp;500}@} |
>
> _Explanation._ Stage 2 does {@{not mean record a whole new €6&nbsp;500 loss on top of the existing €1&nbsp;200 without comparison}@}; it means the allowance must end at {@{€6&nbsp;500 total, so only the extra €5&nbsp;300 is recorded}@}. The same logic applies again in {@{stage 3}@}: if the required allowance becomes {@{€9&nbsp;000 total}@}, only the additional {@{€2&nbsp;500 top-up}@} is recognized at that date.

<!-- markdownlint MD028 -->

> _Credit improvement after stage 3._ Suppose improved expectations later reduce the required allowance from {@{€9&nbsp;000 to €4&nbsp;000}@}. The company reverses only the excess allowance now on the books.
>
> | {@{Reverse the excess allowance when expected credit loss falls}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Allowance for impaired debt investments}@} | {@{5&nbsp;000}@} | |
> | {@{Recovery of impairment loss}@} | | {@{5&nbsp;000}@} |
>
> _Explanation._ The entry is still driven by the same endpoint logic for the allowance: the account currently stands at {@{€9&nbsp;000}@}, but only {@{€4&nbsp;000 is still required}@}, so the excess {@{€5&nbsp;000}@} is reversed.

---

Flashcards for this section are as follows:

- expected credit loss stages: what does stage 1 require? ::@:: Recognize a 12-month expected credit loss allowance.
- expected credit loss stages: what changes when an investment moves to stage 2? ::@:: The required allowance becomes lifetime expected credit loss, so the company records only the incremental top-up needed to move the existing allowance to that lifetime amount.
- expected credit loss stages: what does stage 3 change in entry mechanics? ::@:: The allowance is still based on lifetime expected credit loss, so the entry is again just the incremental increase or decrease needed to reach the newly required allowance balance.
- impairment stages and entries: what is the core accounting question at each date? ::@:: Compare the allowance balance already recorded with the allowance balance now required, then book only the difference.

### investments measured at amortized cost

For amortized-cost debt investments, the company evaluates at each reporting date whether the investment has suffered credit-related impairment. If the investment is impaired, the carrying amount is written down and the loss is recognized in __net income__.

> _Amortized-cost impairment with ECL schedule — Mayhew and Bao._ Mayhew holds a {@{¥200&nbsp;000 par-value}@} debt investment in Bao, bearing {@{10% annual interest}@} with {@{4 years to maturity}@} (EIR 10%). At initial recognition the credit risk is low (Stage 1). By year-end, credit risk has increased significantly (Stage 2), requiring lifetime ECL. Expected annual interest receipts fall to {@{¥16&nbsp;000}@} against the contractual {@{¥20&nbsp;000}@}; the principal repayment is still expected in full.
>
> | Year | Contractual cash flow | Expected cash flow | ECL shortfall |
> | ---: | ---: | ---: | ---: |
> | 1 | {@{20&nbsp;000}@} | {@{16&nbsp;000}@} | {@{4&nbsp;000}@} |
> | 2 | {@{20&nbsp;000}@} | {@{16&nbsp;000}@} | {@{4&nbsp;000}@} |
> | 3 | {@{20&nbsp;000}@} | {@{16&nbsp;000}@} | {@{4&nbsp;000}@} |
> | 4 | {@{20&nbsp;000}@} | {@{16&nbsp;000}@} | {@{4&nbsp;000}@} |
>
> _Stage 1 (12-month ECL):_ only year 1's shortfall, discounted at the EIR of 10%: {@{¥4&nbsp;000 ÷ 1.10 = ¥3&nbsp;636}@}.
>
> | {@{Record stage 1 impairment allowance (12-month ECL)}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Loss on impairment}@} | {@{3&nbsp;636}@} | |
> | {@{Allowance for impaired debt investments}@} | | {@{3&nbsp;636}@} |
>
> _Stage 2 (lifetime ECL):_ all four years' shortfalls discounted at 10%: {@{¥4&nbsp;000 × (1 − 1/1.10^4) / 0.10 = ¥12&nbsp;680}@}. The existing Stage 1 allowance is {@{¥3&nbsp;636}@}, so only the incremental {@{¥9&nbsp;044}@} is recognized now.
>
> | {@{Top up allowance on moving from stage 1 to stage 2 (lifetime ECL)}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Loss on impairment}@} | {@{9&nbsp;044}@} | |
> | {@{Allowance for impaired debt investments}@} | | {@{9&nbsp;044}@} |
>
> _Explanation._ The ECL shortfall arises entirely from {@{lower expected cash flows — ¥16&nbsp;000 instead of ¥20&nbsp;000 — not from any change in market interest rates}@}. A rise in market rates can reduce the bond's fair value but does not by itself create an ECL shortfall if contractual principal and interest are still expected to be paid in full.

<!-- markdownlint MD028 -->

> _Recovery of impairment loss on amortized-cost debt investment._ If credit quality later improves and the allowable reversal is {@{€12&nbsp;680}@}, the recovery entry is:
>
> | {@{Reverse previously recognized impairment loss within the allowed limit}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Allowance for impaired debt investments}@} | {@{12&nbsp;680}@} | |
> | {@{Recovery of impairment loss}@} | | {@{12&nbsp;680}@} |

<!-- markdownlint MD028 -->

> _Partial recovery limited by the carrying-amount ceiling._ Suppose the impaired bond would have had amortized cost of only {@{€97&nbsp;000}@} if no impairment had ever been recognized. Its current carrying amount after impairment is {@{€88&nbsp;000}@}, and improved expected cash flows now support only {@{€95&nbsp;000}@}. The allowed recovery is therefore {@{€7&nbsp;000}@}, not the full gap back to original cost.
>
> | {@{Reverse impairment only up to the supported carrying amount}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Allowance for impaired debt investments}@} | {@{7&nbsp;000}@} | |
> | {@{Recovery of impairment loss}@} | | {@{7&nbsp;000}@} |
>
> _Explanation._ The recovery stops at the {@{carrying amount actually supported by the new expected cash flows}@}. Students often over-recover here by jumping straight back to the no-impairment amount.

If credit conditions later improve, part or all of the impairment loss may be reversed, but the carrying amount after reversal cannot exceed the amortized cost that would have existed if no impairment had ever been recognized.

The measurement intuition is to compare __contractual cash flows__ with __expected cash flows__. If the borrower still owes the same coupon and principal on paper but the investor now expects to collect less, the gap is the credit-loss problem. That is why the course warns students not to treat every lower present value as a credit impairment automatically; some declines are caused by market-rate movement rather than weaker cash collection.

---

Flashcards for this section are as follows:

- amortized-cost debt investment impairment: where is the loss reported? ::@:: In net income through impairment loss, typically with an allowance account.
- amortized-cost impairment reversal ceiling ::@:: After recovery, the carrying amount still cannot exceed the amortized cost that would have existed if no impairment had ever been recognized.
- impairment reversal: what account is debited? ::@:: Debit the _Allowance for impaired debt investments_ and credit _Recovery of impairment loss_, subject to the ceiling that carrying amount cannot exceed amortized cost without prior impairment.
- ECL stage 1 vs stage 2 — Mayhew (annual shortfall = ¥4&nbsp;000, EIR = 10%, 4 years): how does the allowance calculation differ? ::@:: Stage 1 uses only 12-month ECL: ¥4&nbsp;000 ÷ 1.10 = ¥3&nbsp;636. Stage 2 uses lifetime ECL: ¥4&nbsp;000 × annuity factor (4 yrs, 10%) = ¥12&nbsp;680. Moving from stage 1 to stage 2 requires a top-up entry of ¥9&nbsp;044 (not a brand-new ¥12&nbsp;680 entry).

#### recovery cannot exceed the no-impairment amortized cost

The reversal ceiling has two layers that students often mix up:

1. the carrying amount after reversal must be supported by the updated expected-cash-flow estimate; and
2. even if expected cash flows look very strong, the carrying amount still cannot rise above the __amortized cost that would have existed if no impairment had ever been recognized__.

That second ceiling is the point of the allowance rule: you may reverse a loss, but you may not create a carrying amount that is better than the no-impairment path would have produced.

> _Improved expected cash flows still do not permit recovery above the no-impairment amortized cost._ Suppose an impaired bond currently has carrying amount of {@{€88&nbsp;000}@}. If no impairment had ever been recognized, its amortized cost at the same date would have been only {@{€97&nbsp;000}@}. Updated expectations now look strong enough that management estimates recoverable value at {@{€101&nbsp;000}@}. The company still may reverse only {@{€9&nbsp;000}@}, not {@{€13&nbsp;000}@}.
>
> | {@{Reverse impairment only up to the no-impairment amortized-cost ceiling}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Allowance for impaired debt investments}@} | {@{9&nbsp;000}@} | |
> | {@{Recovery of impairment loss}@} | | {@{9&nbsp;000}@} |
>
> _Explanation._ The ceiling is the {@{€97&nbsp;000 amortized cost that would have existed without prior impairment}@}, not the more optimistic {@{€101&nbsp;000 updated estimate}@}. The extra {@{€4&nbsp;000}@} is {@{not recoverable through the reversal entry because it would push the carrying amount above the no-impairment path}@}.

---

Flashcards for this section are as follows:

- impairment recovery ceiling: what does "cannot recover what was not lost before" mean? ::@:: A reversal cannot raise the carrying amount above the amortized cost that would have existed if no impairment had ever been recognized.
- impairment recovery ceiling versus improved estimate: what is the trap? ::@:: Even if updated expected cash flows seem to justify a higher amount, the entry still stops at the no-impairment amortized-cost ceiling.
- impairment reversal ceiling: what is the common mistake? ::@:: Students often reverse all the way back to the no-impairment carrying amount even when updated expected cash flows support only a smaller recovery; the reversal is limited to the amount actually supportable under the improved estimate.

### impairment of HFCS debt investments

HFCS debt investments are already at fair value, so the course distinguishes between:

- fair-value change caused by __market interest rate movements__, which stays in OCI; and
- fair-value change caused by __credit deterioration__, which is treated as impairment and goes to income.

This is one of the most exam-friendly distinctions in the investments material: same overall fair-value decline, but different reporting locations depending on the cause.

In other words, the company may need both:

- a __fair value adjustment__ for the market-rate component; and
- an __allowance for impaired debt investments__ for the credit-loss component.

The slide logic is to separate cause before deciding the journal-entry destination.

<!-- markdownlint MD028 -->

> _HFCS impairment split between OCI and income._ An HFCS debt investment has amortized cost of {@{€100&nbsp;000}@}, but its year-end fair value has fallen to {@{€75&nbsp;000}@}. Of the total {@{€25&nbsp;000 decline}@}, management concludes that {@{€20&nbsp;000 comes from ordinary market-interest-rate movement}@} and {@{€5&nbsp;000 comes from credit deterioration}@}.
>
> | {@{Record market-driven fair value decline for HFCS debt investment}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Unrealized holding gain or loss — equity (OCI)}@} | {@{20&nbsp;000}@} | |
> | {@{Fair value adjustment}@} | | {@{20&nbsp;000}@} |
>
> | {@{Record credit-loss impairment on HFCS debt investment}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Loss on impairment}@} | {@{5&nbsp;000}@} | |
> | {@{Allowance for impaired debt investments}@} | | {@{5&nbsp;000}@} |
>
> _Explanation._ The same total decline is split by {@{cause}@}: the {@{market-rate component stays in OCI}@}, while the {@{credit-loss component goes to income as impairment}@}.

<!-- markdownlint MD028 -->

> _Sale of an HFCS debt investment after both OCI and credit-loss adjustments._ Assume a bond still has original cost of {@{€1&nbsp;000&nbsp;000}@}, but it also carries a {@{€30&nbsp;000 allowance for impaired debt investments}@} and a {@{€10&nbsp;000 fair value adjustment related to market-rate decline}@}. The bond is sold for {@{€960&nbsp;000 cash}@}.
>
> | {@{Sell HFCS debt investment after separate OCI and impairment adjustments}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{960&nbsp;000}@} | |
> | {@{Allowance for impaired debt investments}@} | {@{30&nbsp;000}@} | |
> | {@{Fair value adjustment}@} | {@{10&nbsp;000}@} | |
> | {@{Loss on sale of debt investment}@} | {@{10&nbsp;000}@} | |
> | {@{Debt investments}@} | | {@{1&nbsp;000&nbsp;000}@} |
> | {@{Accumulated comprehensive income}@} | | {@{10&nbsp;000}@} |
>
> _Explanation._ The sale removes the {@{cost basis, allowance, and fair value adjustment together}@}. The separate credit-loss allowance and market-rate OCI component do not vanish magically; they must be cleared as part of the disposal accounting.

<!-- markdownlint MD028 -->

> _Recovery of HFCS credit impairment._ If later credit risk improves and the company can reverse {@{€15&nbsp;000}@} of previously recognized credit-loss impairment, it records:
>
> | {@{Reverse credit-loss impairment on HFCS debt investment}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Allowance for impaired debt investments}@} | {@{15&nbsp;000}@} | |
> | {@{Recovery of impairment loss}@} | | {@{15&nbsp;000}@} |

---

Flashcards for this section are as follows:

- HFCS debt impairment split: what stays in OCI and what goes to income? ::@:: The market-rate component of the decline stays in OCI, while the credit-deterioration component goes to income as impairment.
- HFCS debt investment with both fair value adjustment and impairment allowance: what must be cleared on sale? ::@:: Remove the debt investment, the impairment allowance, the fair value adjustment, and the related accumulated OCI / AOCI tied to the market-rate component.
- HFCS debt investment: which part of a fair-value decline stays in OCI? ::@:: The part caused by market interest rate changes.
- HFCS debt investment: which part of a fair-value decline goes to income as impairment? ::@:: The part caused by credit deterioration.
- HFCS impairment split: why are two entries sometimes needed? ::@:: Because the market-rate component of a decline stays in OCI while the credit-loss component is recognized separately in income as impairment.
- HFCS debt investment with both fair value adjustment and impairment allowance: why is the endpoint shortcut not enough by itself? ::@:: The total gap between fair value and amortized cost still tells you the combined valuation reduction needed, but you must split that total by cause: the market-rate component goes to _Fair value adjustment_ and the credit-loss component goes to _Allowance for impaired debt investments_.
- HFCS sale after separate impairment and OCI adjustments: what must be cleared? ::@:: Clear the debt investment itself, the impairment allowance, the fair value adjustment, and the related accumulated OCI so the disposal entry removes the entire adjusted carrying structure.

## financial statement disclosures under IFRS 7

IFRS 7 _Financial Instruments: Disclosures_ requires entities to provide information that enables users to evaluate the __significance of financial instruments__ for financial position and performance, and the __nature and extent of the risks__ arising from those instruments.

Key disclosure areas:

- __Credit risk__: maximum exposure to credit loss, concentrations of risk, collateral held, and — for instruments subject to the ECL model — a movement table showing the allowance balance by stage from opening to closing.
- __Liquidity risk__: maturity analysis of financial liabilities, presenting contractual undiscounted cash flows arranged by time bucket (e.g., within one year, one to five years, over five years).
- __Market risk__: sensitivity analysis showing the effect on profit or loss and on equity of a reasonably possible change in each relevant market variable (e.g., a 100 basis-point increase in interest rates, or a 10% depreciation of a functional currency).

For equity investments irrevocably designated at FVOCI (non-trading), IFRS 7 additionally requires disclosure of the reason for making the irrevocable election and the amount of dividends recognized from those investments during the period.

---

Flashcards for this section are as follows:

- IFRS 7: what is its primary purpose? ::@:: To require disclosures enabling users to evaluate the significance of financial instruments for financial position and performance, and the nature and extent of the risks arising from them.
- IFRS 7: three main risk disclosure categories ::@:: Credit risk (including ECL allowance movements by stage), liquidity risk (maturity analysis of contractual cash flows across time buckets), and market risk (sensitivity analysis for interest rates, currencies, or other market variables).
- IFRS 7 and non-trading FVOCI equity: what additional disclosures are required? ::@:: Identify each investment carrying the irrevocable FVOCI election, disclose the reason for the election, and separately report dividends recognized from those investments during the period.

## derivatives used for speculation

A derivative is a financial instrument whose value is derived from an __underlying__ such as a share price, interest rate, commodity price, or exchange rate.

The slides stress three basic characteristics:

1. it has an __underlying__;
2. it requires little or no initial investment relative to the exposure created; and
3. it permits or requires __net settlement__.

The three main derivative families in the course are:

- forwards or futures;
- options; and
- swaps.

The transcript gives three quick recognition clues for a derivative:

1. its value depends on an __underlying__ such as a share price, commodity price, or interest rate;
2. it usually requires little or no initial investment compared with the exposure created; and
3. it permits or requires __net settlement__ rather than forcing full physical delivery in every case.

When derivatives are used for __speculation__, the accounting rule is direct:

- recognize the derivative as an asset or liability;
- measure it at __fair value__; and
- report gains and losses in __income__ immediately.

A call option example makes the mechanics concrete.

- __intrinsic value__ = market price of the underlying minus strike price, if positive;
- __time value__ = total option value minus intrinsic value.

A __call option__ profits when the underlying price rises above the strike price. A __put option__ profits when the underlying price falls below the strike price. The lecture stresses that option premium is not all one thing: part is current exercise value, and part is the value of having time left before expiry.

A __futures contract__ differs from an option in one crucial way: the holder is not just buying a right but entering a binding price commitment. Because of that, futures are especially useful in hedge questions about locking in a purchase price or sale price.

> _Call option bought for speculation._ A company buys a call option for {@{€400}@} on {@{1&nbsp;000 shares}@} with strike price {@{€100}@}. By March 31 the share price rises to {@{€120, so intrinsic value becomes €20&nbsp;000}@}. The option's remaining time value is only {@{€100, so almost all of the option's value is now intrinsic rather than time value}@}.
>
> | {@{Record increase in intrinsic value of call option}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Call option}@} | {@{20&nbsp;000}@} | |
> | {@{Unrealized holding gain or loss — income}@} | | {@{20&nbsp;000}@} |
>
> | {@{Record decline in time value of call option}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Unrealized holding gain or loss — income}@} | {@{300}@} | |
> | {@{Call option}@} | | {@{300}@} |
>
> _Explanation._ Both the gain from intrinsic value and the loss from time-value decay hit income immediately because the option is being accounted for as a speculative derivative.

<!-- markdownlint MD028 -->

> _Final remeasurement and settlement of a speculative call option._ Before settlement, intrinsic value falls by {@{€5&nbsp;000}@} and time value falls by another {@{€40, leaving a carrying amount of €15&nbsp;060 before settlement for €15&nbsp;000 cash}@}.
>
> | {@{Record decline in intrinsic value before settlement}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Unrealized holding gain or loss — income}@} | {@{5&nbsp;000}@} | |
> | {@{Call option}@} | | {@{5&nbsp;000}@} |
>
> | {@{Record final decline in time value before settlement}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Unrealized holding gain or loss — income}@} | {@{40}@} | |
> | {@{Call option}@} | | {@{40}@} |
>
> | {@{Settle speculative call option}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{15&nbsp;000}@} | |
> | {@{Loss on settlement of call option}@} | {@{60}@} | |
> | {@{Call option}@} | | {@{15&nbsp;060}@} |

---

Flashcards for this section are as follows:

- derivative: three basic characteristics ::@:: It has an underlying, requires little or no initial investment relative to exposure, and permits or requires net settlement.
- main derivative types in this topic ::@:: Forwards or futures, options, and swaps.
- speculative derivative accounting: the three-step rule ::@:: Recognize the derivative, measure it at fair value, and report gains and losses in income immediately.
- call option: intrinsic value ::@:: The positive difference between the market price of the underlying and the strike price.
- call option: time value ::@:: The option's total value above its intrinsic value.
- put option: basic profit direction ::@:: A put option becomes more valuable as the underlying price falls below the strike price, because the holder has the right to sell at the fixed strike price.
- futures versus options: basic contractual difference ::@:: An option gives a right, while a futures contract is a binding price commitment that can create gains or losses in either direction.
- speculative derivative: why can both a gain and a loss appear before settlement? ::@:: Because different components of fair value, such as intrinsic value and time value, can move in opposite directions while the option is still open.
- call option settlement: why can there still be a final settlement loss after earlier gains? ::@:: Because the option must first be remeasured again before settlement, and the final cash proceeds may still be below the remeasured carrying amount.

## hedge accounting and swaps

The course covers two hedge types that receive special accounting under IFRS.

---

Flashcards for this section are as follows:

- hedge accounting in this note: main split ::@:: Fair value hedges send both sides of the hedge to income, while cash flow hedges park the derivative's unrealized gain or loss in OCI first and reclassify it later.
- hedge accounting: why is location of gain or loss the key idea? ::@:: Because hedge accounting tries to make the derivative and the hedged item affect earnings in the same period or location where the underlying risk shows up.

### fair value hedges

A __fair value hedge__ offsets exposure to changes in the fair value of a recognized asset or liability or of an unrecognized firm commitment.

The key accounting idea is symmetrical:

- the __hedged item__ is adjusted for the fair-value change attributable to the hedged risk; and
- the __hedging derivative__ is also adjusted to fair value;
- both effects go to __income__.

The transcript frames the reason very practically: if the hedged inventory or liability is already creating an income-statement gain or loss, the hedging derivative must hit __the same location__ or the hedge will fail to offset the reported volatility.

> _Inventory hedged with a put option._ Hayward holds tractor-tire inventory with cost {@{€200&nbsp;000}@}. At March 31 the inventory's fair value declines by {@{10%}@}, or {@{€20&nbsp;000}@}. At the same time, the put option used as the hedge rises by {@{€20&nbsp;000}@}.
>
> | {@{Record fair-value decline on hedged inventory}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Unrealized holding gain or loss — income}@} | {@{20&nbsp;000}@} | |
> | {@{Allowance to reduce inventory to fair value}@} | | {@{20&nbsp;000}@} |
>
> | {@{Record fair-value increase on put option}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Put option}@} | {@{20&nbsp;000}@} | |
> | {@{Unrealized holding gain or loss — income}@} | | {@{20&nbsp;000}@} |
>
> _Interpretation._ In a perfect hedge, the income effects offset.

---

Flashcards for this section are as follows:

- fair value hedge: what is being hedged? ::@:: Exposure to changes in the fair value of a recognized asset or liability or of an unrecognized firm commitment.
- fair value hedge: where do the hedged-item adjustment and derivative gain/loss go? ::@:: Both go to income so that the reported volatility from the hedged item is offset in the same place.
- fair value hedge: is OCI used for the derivative's unrealized gain or loss? ::@:: No. In this hedge type, the derivative and hedged-item fair-value effects go straight to income.
- why does a fair value hedge hit income immediately? ::@:: Because the hedged item's fair-value change is already affecting income, so the derivative must go to the same location to offset it.

### cash flow hedges

A __cash flow hedge__ offsets variability in expected future cash flows, not current fair value.

For a qualifying cash flow hedge:

- the derivative is still shown at fair value on the statement of financial position; but
- the unrealized gain or loss goes to __OCI__ first.

Later, when the hedged forecast transaction affects earnings, the accumulated OCI is reclassified into income.

That OCI-first treatment matches the transcript's logic. At the start of a cash flow hedge, the future purchase or future sale has not yet hit profit or loss. So the hedge gain or loss is parked in OCI first and only released when the forecast transaction later affects cost of goods sold, revenue, or some other earnings line.

> _Forecast inventory purchase hedged by futures._ Allied enters a futures contract to lock in the price of aluminum at {@{¥1&nbsp;550 per ton}@}. By year-end the futures contract has gained {@{¥25&nbsp;000}@}.
>
> | {@{Record year-end gain on qualifying cash flow hedge}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Futures contract}@} | {@{25&nbsp;000}@} | |
> | {@{Unrealized holding gain or loss — equity (OCI)}@} | | {@{25&nbsp;000}@} |
>
> Later, when the related inventory is sold and _Cost of goods sold_ is recognized, the OCI amount is reclassified so that the hedge effect enters income in the same period as the hedged item.

<!-- markdownlint MD028 -->

> _Reclassification from OCI when the hedged inventory affects earnings._ When the finished goods made from the hedged inventory are sold, the accumulated hedge gain of {@{¥25&nbsp;000}@} is reclassified out of OCI.
>
> | {@{Reclassify cash flow hedge gain from OCI into cost of goods sold}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Unrealized holding gain or loss — equity (OCI)}@} | {@{25&nbsp;000}@} | |
> | {@{Cost of goods sold}@} | | {@{25&nbsp;000}@} |

---

Flashcards for this section are as follows:

- cash flow hedge: where does the derivative's unrealized gain or loss go first? ::@:: To OCI, because the forecast transaction has not yet affected earnings.
- cash flow hedge reclassification: when does OCI move into income? ::@:: When the hedged forecast transaction later affects earnings, such as when hedged inventory flows into _Cost of goods sold_.
- cash flow hedge: what is being hedged? ::@:: Variability in expected future cash flows.

#### forecast purchase hedged through basis adjustment into inventory

One common accounting path for a cash flow hedge of a forecast purchase of a __non-financial item__ is to remove the accumulated OCI amount from equity and build it into the carrying amount of the asset when that asset is finally recognized. For inventory, that means the hedge effect can be absorbed into __Inventory__ first and then flow into __Cost of goods sold__ naturally when the inventory is sold.

> _Forecast inventory purchase with later basis adjustment._ Suppose the futures contract above has already produced a {@{¥25&nbsp;000 gain in OCI at year-end}@}. Before the actual inventory purchase date, the futures gain increases by another {@{¥7&nbsp;000}@}, so the total effective hedge gain accumulated in OCI is now {@{¥32&nbsp;000}@}. The inventory is then purchased for the current spot-based cash price of {@{¥1&nbsp;582&nbsp;000}@}, and the futures contract is settled for {@{¥32&nbsp;000 cash}@}.
>
> | {@{Record additional gain on the qualifying cash flow hedge before the forecast purchase occurs}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Futures contract}@} | {@{7&nbsp;000}@} | |
> | {@{Unrealized holding gain or loss — equity (OCI)}@} | | {@{7&nbsp;000}@} |
>
> | {@{Purchase the hedged inventory at the actual spot-based cash price}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Inventory}@} | {@{1&nbsp;582&nbsp;000}@} | |
> | {@{Cash}@} | | {@{1&nbsp;582&nbsp;000}@} |
>
> | {@{Settle the futures contract for cash}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{32&nbsp;000}@} | |
> | {@{Futures contract}@} | | {@{32&nbsp;000}@} |
>
> | {@{Remove the accumulated hedge gain from OCI and use it to reduce the carrying amount of the purchased inventory}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Unrealized holding gain or loss — equity (OCI)}@} | {@{32&nbsp;000}@} | |
> | {@{Inventory}@} | | {@{32&nbsp;000}@} |
>
> | {@{Later recognize cost of goods sold after the basis-adjusted inventory is sold}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cost of goods sold}@} | {@{1&nbsp;550&nbsp;000}@} | |
> | {@{Inventory}@} | | {@{1&nbsp;550&nbsp;000}@} |
>
> _Explanation._ The hedge gain first sits in {@{OCI because the forecast purchase has not yet affected earnings}@}. Once the inventory is recognized, the accumulated OCI is {@{taken out of equity and used to reduce Inventory from ¥1&nbsp;582&nbsp;000 to the hedged effective amount of ¥1&nbsp;550&nbsp;000}@}. The hedge effect then reaches income naturally through later {@{Cost of goods sold}@}.

---

Flashcards for this section are as follows:

- cash flow hedge of forecast inventory purchase: what is basis adjustment doing? ::@:: It removes the accumulated effective hedge amount from OCI and builds that amount into the carrying amount of the purchased inventory.
- cash flow hedge basis adjustment for an inventory purchase: why can inventory be credited after a hedge gain? ::@:: Because the hedge gain reduces the effective acquisition cost of the inventory, so the accumulated OCI gain is removed from equity and used to reduce the inventory carrying amount.

#### floating-rate debt hedged to fixed cash flows with a swap

Cash flow hedge accounting is also common when a company wants to turn __floating-rate interest cash flows into fixed-like interest cash flows__. The debt itself still produces ordinary interest expense. The effective part of the swap's gain or loss is parked in __OCI__ first and then reclassified into __Interest expense__ when the hedged interest cash flow affects earnings.

> _Floating-rate debt hedged with a pay-fixed, receive-floating swap._ Assume a company has floating-rate debt that produces {@{€52&nbsp;000 interest expense for the period}@}. The effective portion of the swap creates a {@{€8&nbsp;000 loss}@} for the same period because the company is effectively locking itself into a higher fixed rate. The swap is then settled for {@{€8&nbsp;000 cash}@}.
>
> | {@{Record periodic interest on the floating-rate debt itself}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Interest expense}@} | {@{52&nbsp;000}@} | |
> | {@{Cash}@} | | {@{52&nbsp;000}@} |
>
> | {@{Record the effective loss on the cash flow hedge in OCI}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Unrealized holding gain or loss — equity (OCI)}@} | {@{8&nbsp;000}@} | |
> | {@{Swap contract}@} | | {@{8&nbsp;000}@} |
>
> | {@{Settle the swap liability for cash}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Swap contract}@} | {@{8&nbsp;000}@} | |
> | {@{Cash}@} | | {@{8&nbsp;000}@} |
>
> | {@{Reclassify the accumulated OCI loss into interest expense when the hedged interest cash flow affects earnings}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Interest expense}@} | {@{8&nbsp;000}@} | |
> | {@{Unrealized holding gain or loss — equity (OCI)}@} | | {@{8&nbsp;000}@} |
>
> _Explanation._ The floating-rate debt itself creates {@{€52&nbsp;000 of ordinary interest expense}@}. The swap's effective loss is first parked in {@{OCI}@}, then reclassified into {@{Interest expense}@} so that total reported borrowing cost becomes {@{€60&nbsp;000 fixed-like cost}@} for the period.

---

Flashcards for this section are as follows:

- cash flow hedge of floating-rate debt: where does the effective swap gain or loss go first? ::@:: To OCI first, then later into _Interest expense_ when the hedged interest cash flow affects earnings.
- floating-rate debt hedged to fixed cash flows: why is OCI later reclassified into interest expense? ::@:: So the derivative effect reaches earnings in the same period as the hedged floating-rate interest cash flow and makes the reported borrowing cost look fixed-like.

### swaps and qualifying criteria

A __swap__ is a contract in which two parties exchange payment streams. The most common example in the slides is an __interest rate swap__. One party pays fixed and receives floating; the other does the opposite.

The classroom motivation is duration and interest-rate-risk management. A company with a fixed-rate bond liability may fear falling market rates, because falling rates increase the fair value of that liability. By entering a swap that receives fixed and pays floating, the company creates a derivative whose value can move in the opposite direction and offset part of that risk.

> _Interest rate swap used as a fair value hedge of bonds payable._ A company has {@{€1&nbsp;000&nbsp;000 of 8% bonds payable}@}. It enters a pay-floating, receive-fixed swap that qualifies as a fair value hedge. At year-end it pays regular bond interest, receives a {@{€12&nbsp;000 swap settlement}@}, recognizes a {@{€40&nbsp;000 increase in the swap's fair value}@}, and recognizes the matching {@{€40&nbsp;000 loss from the increase in the fair value of the hedged bonds payable}@}.
>
> | {@{Record annual interest payment on bonds payable}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Interest expense}@} | {@{80&nbsp;000}@} | |
> | {@{Cash}@} | | {@{80&nbsp;000}@} |
>
> | {@{Record cash settlement received on interest rate swap}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{12&nbsp;000}@} | |
> | {@{Interest expense}@} | | {@{12&nbsp;000}@} |
>
> | {@{Record increase in fair value of swap contract}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Swap contract}@} | {@{40&nbsp;000}@} | |
> | {@{Unrealized holding gain or loss — income}@} | | {@{40&nbsp;000}@} |
>
> | {@{Record fair value loss on hedged bonds payable}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Unrealized holding gain or loss — income}@} | {@{40&nbsp;000}@} | |
> | {@{Bonds payable}@} | | {@{40&nbsp;000}@} |
>
> _Explanation._ In a fair value hedge, the {@{derivative gain and hedged-item loss go to the same income location}@}, so the accounting visibly shows the offset.

To qualify for hedge accounting, the hedge relationship must be properly:

- documented;
- designated as part of risk management; and
- shown to be effective.

Without that qualification, derivative gains and losses fall back to ordinary fair-value-through-income treatment.

---

Flashcards for this section are as follows:

- swap: basic idea in this course ::@:: A swap exchanges payment streams, commonly fixed for floating, so it can offset interest-rate exposure on another item.
- hedge-accounting qualification: what happens if the relationship is not properly documented, designated, and effective? ::@:: The derivative loses hedge accounting and falls back to ordinary fair-value-through-income treatment.
- interest rate swap: basic idea ::@:: Two parties exchange payment streams, commonly one fixed-rate stream for one floating-rate stream.
- non-qualifying hedge or unhedged derivative: where do fair-value changes go? ::@:: To income under ordinary derivative accounting.
- hedge accounting qualification: what three conditions must the hedge relationship satisfy? ::@:: It must be (1) properly documented at inception, (2) designated as part of the entity's risk management strategy, and (3) shown to be effective at offsetting the hedged risk.
- interest rate swap as fair value hedge of fixed-rate bonds payable: what risk motivates the strategy? ::@:: Falling market interest rates increase the fair value of fixed-rate bond liabilities. A pay-floating, receive-fixed swap gains in value when rates fall, offsetting the fair-value increase of the bonds payable.

- cash flow hedge reclassification: why is cost of goods sold credited rather than another OCI account? ::@:: Because once the hedged forecast transaction affects earnings, the accumulated OCI must be reclassified into the same income-statement line affected by the hedged item.
